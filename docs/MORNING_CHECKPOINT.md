# Morning checkpoint

**Historical, superseded:** user resumed at venue. Read [HANDOFF.md](../HANDOFF.md). Old pause below no longer applies. App dependencies installed and more stack/footage inspection completed; no app built yet.

Paused at the user's request on October 9, 2026. Do not continue research, downloads or setup until the user resumes.

## Completed and verified locally

- GitHub read/push access already works for LaboriouslyExquisite/or-waste-tracker. The original Markdown specification package is published on codex/vast-build-brief.
- Saved project settings: GPT-6.1 Sol, Extra High reasoning, live web search, workspace permissions, on-request approvals with automatic review, and a network allowlist of 21 host patterns. Exact repository trust added to user config. Installed Codex CLI loaded the project and reported workspace-write, network enabled, automatic approval review and the correct repository writable root.
- Applied settings: `.codex/config.toml`; tracked template: `config/codex.project.toml`. Global settings backup: `C:\Users\Craft\.codex\config.toml.or-tracker-backup-20261009-034201`. Reopen this exact repository/start a new session to load saved settings; current chat permissions are unchanged. Actual VAST/CoreWeave gateway/storage hosts still need adding after the organizer handoff.
- Bundled Python 3.12.14 works. Isolated `.venv-data` has pinned h5py 3.16.0, NumPy 2.5.3 and Pillow 12.3.0. Node 24.19.0, FFmpeg 8.0.1 and Git work. No app dependencies installed yet.
- `.gitignore` excludes credentials, environments, local Codex settings and media/runtime outputs.

## Footage research and actual inspection

Follow-up Exa research covered 50 results across five queries, in addition to the initial 55 across eight. Do not describe all these as distinct usable datasets.

- Closest supply-workflow leads: [JOMI OR preparation](https://jomi.com/article/383/surgical-technologist-prepares-the-or-for-a-case) and [opening sterile packs](https://jomi.com/article/300.4/opening-sterile-surgical-packs). Educational footage, not a complete clinical waste case. [Publisher terms](https://jomi.com/terms) require permission beyond personal noncommercial use. Permission contact: contact@jomi.com. No email sent and no download attempted.
- Real open surgery/tool labels: [EgoSurgery](https://github.com/Fujiry0/EgoSurgery). [Access form](https://forms.gle/T7Kdqozz9C2kFBZs5), CC BY-NC-SA 4.0 with academic-research restriction. Not submitted; event-demo permission and back-table coverage unresolved.
- Publicly viewable educational sterile-table video on [Theseus](https://www.theseus.fi/items/12e40826-3e17-4b03-ba57-c31101767f85) is all-rights-reserved, so not an approved demo source.
- [SurgPub](https://github.com/Yaoqian-Li/SurgPub-Video) also requires a request form. LEMON is endoscopic, unsuitable for back-table package tracking. Team-OR is explicitly unavailable publicly. MVOR consists of sampled real OR frames, not continuous opening-to-use coverage.
- Openly licensed simulated fallback: [EgoExOR legacy](https://huggingface.co/datasets/ardamamur/EgoExOR) and [HQ](https://huggingface.co/datasets/TUM/EgoExOR), Apache-2.0. Real people performing emulated procedures; must label simulated. Smallest phase ultrasound_1.h5 is 1,669,545,224 bytes legacy or 21,180,012,030 bytes HQ. No whole archive downloaded.
- `scripts/inspect_egoexor.py` performs validated bounded HTTP-range reads. First recursive metadata attempt safely hit a 120 MiB cap. Fixed it to target camera/take paths and avoid huge annotation tables. Successful legacy inspection transferred 38 MiB and saved `runtime/media-prep/egoexor/receipt.json`, inventory and a private contact sheet.
- Contact sheet actually viewed: gowning/draping in a simulated OR. It does not establish unopened-to-used-to-unused disposable histories. Take has 1,192 frames at the documented 15 FPS, five cameras: assistant, head_surgeon, circulator, or_light, simstation. Camera index 4 is fixed room view. Legacy 336x336 is weak for small supply details.
- HQ metadata inspected successfully: same take/cameras, 1344x1344 RGB; chunks include 10 frames/all five cameras. Extraction of frames 390–419, camera 4, under `runtime/media-prep/egoexor-hq-clip` ended at its 300 MiB transfer cap after saving at least the first frame. No complete clip/receipt was produced. Process is no longer running. Check partial frames before retrying; do not repeat expensive reads blindly. Source frames are private and unredacted; do not show/upload them as approved demo assets.

## Resume work

1. Inspect HQ extraction status and frames if present. Continue only after user resumes.
2. Finish ranked `FOOTAGE_READY.md` and an unsent publisher permission request; do not send messages or submit forms without explicit authorization.
3. Update DATASETS.md, SETUP.md and README.md: their old statements about no downloaded media/unverified Python are now stale. No app is built yet.
4. Document saved settings and the remaining stack credentials/hosts. No secrets in chat, Git or browser assets.
5. Validate preparation scripts and Markdown links, commit/push the preparation changes. Current `.gitignore`, config template, scripts and this checkpoint are LOCAL and not yet committed/pushed.
6. Organizer footage first if suitable; public real OR next; explicitly simulated fallback only. Never align the synthetic financial fixture to this footage as if it were observed truth.

The event listing says Friday October 9, 2026, which is the current local date; the user's "tomorrow" wording needs checking against organizer communications when they resume.
