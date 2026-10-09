"""Inspect/extract a bounded EgoExOR subset through validated HTTP byte ranges.

Only the explicitly Apache-licensed simulated dataset is supported. No tokens,
form submissions, patient footage, whole-file downloads or public uploads.
"""
import argparse
import collections
import io
import json
from pathlib import Path
import re
import urllib.request

import h5py
import numpy as np
from PIL import Image


class HTTPRanges(io.RawIOBase):
    def __init__(self, url, size, max_bytes):
        self.url, self.size, self.max_bytes = url, size, max_bytes
        self.position = self.transferred = self.requests = 0
        self.block_size = 1024 * 1024
        self.blocks = collections.OrderedDict()

    def readable(self): return True
    def seekable(self): return True
    def tell(self): return self.position

    def seek(self, offset, whence=0):
        position = offset if whence == 0 else (self.position if whence == 1 else self.size) + offset
        if not 0 <= position <= self.size: raise ValueError('Out-of-range seek')
        self.position = position
        return position

    def block(self, number):
        if number in self.blocks:
            self.blocks.move_to_end(number)
            return self.blocks[number]
        start = number * self.block_size
        end = min(start + self.block_size, self.size) - 1
        if self.transferred + end - start + 1 > self.max_bytes:
            raise RuntimeError('Transfer budget reached; no whole dataset download attempted')
        # Range-specific query avoids a CDN caching a signed redirect for another range.
        url = self.url + f'?download=true&range_start={start}&range_end={end}'
        req = urllib.request.Request(url, headers={'Range':f'bytes={start}-{end}', 'User-Agent':'ORWasteTracker-data-prep/1.0'})
        with urllib.request.urlopen(req, timeout=45) as response:
            expected = f'bytes {start}-{end}/{self.size}'
            if response.status != 206 or response.headers.get('Content-Range') != expected:
                raise RuntimeError('Server did not honor exact byte range; refusing whole-file download')
            data = response.read(end - start + 2)
        if len(data) != end - start + 1: raise RuntimeError('Unexpected range length')
        self.transferred += len(data)
        self.requests += 1
        self.blocks[number] = data
        if len(self.blocks) > 32: self.blocks.popitem(last=False)
        if self.requests == 1 or self.requests % 20 == 0:
            print(f'Fetched {self.transferred / 1048576:.1f} MiB in {self.requests} ranges', flush=True)
        return data

    def read(self, size=-1):
        if size < 0: size = self.size - self.position
        size = min(size, self.size - self.position)
        parts = []
        remaining = size
        while remaining:
            number, offset = divmod(self.position, self.block_size)
            block = self.block(number)
            count = min(remaining, len(block) - offset)
            parts.append(block[offset:offset+count])
            self.position += count
            remaining -= count
        return b''.join(parts)

    def readinto(self, buffer):
        data = self.read(len(buffer))
        buffer[:len(data)] = data
        return len(data)


def serial(value):
    if isinstance(value, bytes): return value.decode('utf-8', 'replace')
    if isinstance(value, np.ndarray): return serial(value.tolist())
    if isinstance(value, np.generic): return serial(value.item())
    if isinstance(value, (list, tuple)): return [serial(x) for x in value]
    if isinstance(value, dict): return {str(k): serial(v) for k, v in value.items()}
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', default='ardamamur/EgoExOR', choices=['ardamamur/EgoExOR','TUM/EgoExOR'])
    parser.add_argument('--file', default='ultrasound_1.h5')
    parser.add_argument('--output', default='runtime/media-prep/egoexor')
    parser.add_argument('--max-mib', type=int, default=250)
    parser.add_argument('--rgb-path')
    parser.add_argument('--camera', type=int)
    parser.add_argument('--start-frame', type=int, default=0)
    parser.add_argument('--frames', type=int, default=150)
    parser.add_argument('--preview-camera', type=int, help='Inspect only one camera column; indices come from take metadata')
    parser.add_argument('--metadata-only', action='store_true')
    parser.add_argument('--sample-count', type=int, default=4)
    parser.add_argument('--take-limit', type=int, default=3)
    args = parser.parse_args()
    if not re.fullmatch(r'(miss_[1-4]|ultrasound_[1-4]|ultrasound_5_(14|58))\.h5', args.file):
        raise ValueError('Only known dataset phase filenames are accepted')
    if not 1 <= args.max_mib <= 500 or not 1 <= args.frames <= 450:
        raise ValueError('Bounded transfer and extraction limits exceeded')
    if not 1 <= args.sample_count <= 4 or not 1 <= args.take_limit <= 3:
        raise ValueError('Preview limits exceeded')
    output = Path(args.output).resolve()
    root = Path(__file__).resolve().parents[1]
    if not output.is_relative_to(root): raise ValueError('Output must remain in this repository')
    output.mkdir(parents=True, exist_ok=True)
    base = f'https://huggingface.co/datasets/{args.repo}/resolve/main/{args.file}'
    api = f'https://huggingface.co/api/datasets/{args.repo}/tree/main?recursive=false&expand=false'
    with urllib.request.urlopen(api, timeout=30) as response: entries = json.load(response)
    size = next(x['size'] for x in entries if x['path'] == args.file)
    stream = HTTPRanges(base, size, args.max_mib * 1048576)
    with h5py.File(stream, 'r', rdcc_nbytes=320*1048576, rdcc_nslots=1009) as h5:
        inventory = []
        rgb_paths = []
        # Never recurse into per-frame annotation groups: they contain enormous
        # object tables and are unnecessary for obtaining a camera preview.
        for name in ['metadata/sources/sources', 'metadata/vocabulary/entity', 'metadata/vocabulary/relation']:
            if name in h5:
                obj = h5[name]
                row = {'path':name,'shape':list(obj.shape),'dtype':str(obj.dtype)}
                if obj.size <= 500: row['values'] = serial(obj[()])
                inventory.append(row)
        root_key = 'data' if 'data' in h5 else 'procedures'
        for procedure in h5[root_key]:
            procedure_path = f'{root_key}/{procedure}'
            phases_path = procedure_path if root_key == 'data' else f'{procedure_path}/phases'
            for phase in h5[phases_path]:
                phase_path = f'{phases_path}/{phase}'
                takes_path = next((f'{phase_path}/{key}' for key in ['take','takes'] if f'{phase_path}/{key}' in h5), None)
                if takes_path is None: continue
                for take in h5[takes_path]:
                    take_path = f'{takes_path}/{take}'
                    name = f'{take_path}/frames/rgb'
                    if name not in h5: continue
                    obj = h5[name]
                    row = {'path':name,'shape':list(obj.shape),'dtype':str(obj.dtype),'chunks':obj.chunks}
                    sources_path = f'{take_path}/sources'
                    if sources_path in h5:
                        row['camera_attributes'] = serial(dict(h5[sources_path].attrs))
                    inventory.append(row)
                    if len(obj.shape) == 5: rgb_paths.append(name)
        receipt = {'repo':args.repo,'file':args.file,'source_bytes':size,'source_type':'public_simulated_or','license':'Apache-2.0','rgb_paths':rgb_paths,'datasets':inventory}
        (output/'inventory.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
        print(json.dumps({'rgb_paths':rgb_paths,'metadata':[r for r in inventory if r['path'].startswith('metadata/sources')],'source_bytes':size},indent=2),flush=True)
        if args.rgb_path:
            if args.rgb_path not in rgb_paths: raise ValueError('Choose an RGB path listed by inspection')
            dataset = h5[args.rgb_path]
            if args.camera is None or not 0 <= args.camera < dataset.shape[1]: raise ValueError('Choose a valid inspected external camera index')
            if not 0 <= args.start_frame < dataset.shape[0]: raise ValueError('Invalid start frame')
            frames = min(args.frames,dataset.shape[0]-args.start_frame)
            frame_dir=output/'frames'
            frame_dir.mkdir(exist_ok=True)
            for index in range(frames):
                array=dataset[args.start_frame+index,args.camera]
                Image.fromarray(np.asarray(array,dtype=np.uint8)).save(frame_dir/f'{index:05d}.png')
                if index % 30 == 0: print(f'Extracted frame {index+1}/{frames}',flush=True)
            receipt.update({'selected_rgb_path':args.rgb_path,'camera_index':args.camera,'start_frame':args.start_frame,'frames':frames,'redaction_status':'pending','aligned_event_fixture':None})
        elif not args.metadata_only:
            # Private contact sheets: four times across each take and every camera.
            for take_index,rgb_path in enumerate(rgb_paths[:args.take_limit]):
                dataset=h5[rgb_path]
                indices=np.linspace(0,dataset.shape[0]-1,min(args.sample_count,dataset.shape[0]),dtype=int)
                cell=168
                cameras = list(range(dataset.shape[1])) if args.preview_camera is None else [args.preview_camera]
                if any(not 0 <= camera < dataset.shape[1] for camera in cameras): raise ValueError('Invalid preview camera')
                sheet=Image.new('RGB',(cell*len(cameras),cell*len(indices)),'white')
                for row,frame in enumerate(indices):
                    for column,camera in enumerate(cameras):
                        tile=Image.fromarray(np.asarray(dataset[int(frame),camera],dtype=np.uint8)).resize((cell,cell))
                        sheet.paste(tile,(column*cell,row*cell))
                sheet.save(output/f'take-{take_index}-contact.png')
                receipt.setdefault('contact_sheets',[]).append({'file':f'take-{take_index}-contact.png','rgb_path':rgb_path,'frame_indices':indices.tolist(),'camera_indices':cameras})
        receipt.update({'transferred_bytes':stream.transferred,'http_ranges':stream.requests})
        (output/'receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    stream.close()
    print(f'Saved private dataset preparation receipt under {output}',flush=True)


if __name__ == '__main__': main()
