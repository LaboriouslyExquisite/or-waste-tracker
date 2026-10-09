# Footage research and selection

Reviewed October 9, 2026. Initial Exa search returned 55 results across eight queries; further research and actual bounded EgoExOR inspections are in [HANDOFF.md](../HANDOFF.md). Private samples now exist under ignored runtime/media directories. No complete real OR waste case qualified. Event guide prohibits internet-video ingest; external/staged VSS import permission is unresolved. Comparison below is initial research, not approved demo assets.

## User's priority

1. **Organizer footage first when available.** Determine whether it actually covers the supply workflow. If it contains a different environment, use it honestly to demonstrate retrieval/detection and keep any OR example separately labeled; never call factory footage a surgery.
2. **Suitable public real OR footage next.** Require continuous external views, permission for the intended use and visible actions after redaction.
3. **Explicit fallback only:** public simulated OR footage, then a team-recorded tabletop example. These are options if the preferred sources cannot support the demo; label them prominently.

No verified free source found in this search satisfies all of continuous real OR video, clear supply opening-to-use coverage and explicit broad reuse permission. This is a specific data gap, not evidence that no such source exists.

## Candidate comparison

| Source | Nature / documented access | Fit and decision |
| --- | --- | --- |
| Organizer library | Published corpus: traffic, streets, warehouse/indoor scenes; live Team 8 inventory unqueried | First priority if suitable OR footage exists; nonmedical footage is not a surgery |
| [MVOR](https://github.com/CAMMA-public/MVOR) | Real clinical external views; 732 synchronized multi-view frame samples; download instructions; CC BY-NC-SA 4.0 | Real OR reference/pose baseline. Sampled frames do not provide an uninterrupted opening/use history. Not the full waste demo |
| [AVOS](https://research.bidmc.org/surgical-informatics/avos) | Open-surgery video research based on publicly available recordings | Lead for tool-use examples. Primary page does not establish reusable package-opening footage or redistribution rights for source videos. Per-video rights and suitability remain unverified |
| [Team-OR](https://github.com/CAMMA-public/Team-OR) | Real surgical recordings studied by authors | Exclude as downloadable media: maintainers explicitly state dataset cannot be made public due to privacy/ethical concerns |
| [EgoExOR-HQ](https://huggingface.co/datasets/TUM/EgoExOR) | Emulated procedures, ego/external RGB; Apache 2.0 data card; phase-level HDF5 | Strong accessible **simulated** fallback; actual package-opening coverage still needs visual inspection |
| [EgoExOR code/data guide](https://github.com/ardamamur/EgoExOR/blob/main/data/README.md) | Legacy/HQ utilities and take visualization | Useful extraction route; choose one external camera and phase, not a whole dataset download |
| [MM-OR](https://github.com/egeozsoy/MM-OR) | Rich OR scene data; access form required | Request-based option. Data terms are separate from the code license; no immediate-access promise or verified supply labels |
| [4D-OR](https://github.com/egeozsoy/4D-OR) | Simulated knee procedures, six RGB-D views, sampled at 1 FPS; access form | Context fallback; 1 FPS is weak for brief package-opening actions |
| Public educational/stock videos | License and clinical authenticity vary | Do not assume public viewing allows copying. Reject AI-generated stock as real OR evidence; reject purely staged material as real surgery |

Endoscopic/laparoscopic datasets may show tool use inside the body, but cannot establish what sterile packages were opened at the back table. They do not solve this dataset requirement.

## Access routes

MVOR's maintained repository links its archive at [the CAMMA server](https://s3.unistra.fr/camma_public/datasets/mvor/camma_mvor_dataset.zip). Download size, link health and intended-use/license compatibility must be checked before acquiring it. Do not convert sparse frames into a fake continuous case or make non-use claims between samples.

MM-OR links an [access form](https://forms.gle/kj47QXEcraQdGidg6); 4D-OR links a [separate form](https://forms.gle/9cR3H5KcFUr5VKxr9). No form has been submitted. Access timing is unknown. Keep any agreed dataset terms with the local manifest.

EgoExOR-HQ's data card lists phase HDF5 files and exocentric sources. The separate utility guide supports discovering takes and rendering previews. During implementation, inspect file sizes first, obtain one phase, discover available takes/camera IDs, export an external-camera interval, preserve the original timing, then redact and inspect it. The code's group-view visualization is useful for private inspection; the final public derivative should contain only the selected approved view. Avoid downloading the full collection by default.

## Qualification checklist for any clip

- Permission permits model processing, on-stage playback and any planned export; retain attribution.
- Free access or provided event access is verified; size fits the available time/storage.
- External perspective shows package opening plus the relevant item association.
- Frame rate/resolution supports the action; camera timing is known.
- At least two clean opening events and one visible use can survive masking.
- Items can be mapped to known billing units; reusable instruments are separable.
- End-of-case or final disposition is shown, or the demo is explicitly a partial segment.
- Coverage gaps and off-camera use are labeled; unused ground truth comes from review, not missing events.
- Patient, faces, surgical field, blood, names and audio are redacted in the approved derivative.
- A human can annotate the demo action intervals independently of model output.

If no real clip passes, continue application development with the ledger fixture and a clear missing-media state. An honest limited demo is reviewable; fabricated OR evidence is not.
