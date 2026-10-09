# Build plan and event execution

The supplied listing is Friday, October 9, 2026, America/New_York, with build start 9:30 AM and demos at 4:30 PM. The organizer's latest instructions take precedence. The user described stack access as "tomorrow" while this session is dated October 9; confirm the actual access date from event communications before scheduling. No reminder is created by this document. [Organizer listing](https://luma.com/vastnyc)

## Preparation before stack access

This repository is the Markdown handoff. Create/select the GitHub repository, connect authorized access, prepare runtimes and FFmpeg, gather candidate data permissions, and rehearse the hook. Avoid costly GPU setup or guessed API wiring. Check event rules before doing any competition implementation in advance.

## Critical build order

| Priority | Deliverable | Gate |
| --- | --- | --- |
| P0 | Synthetic replay, item ledger, price snapshot, money tests | Replayed case matches expected cents, with fixture badge |
| P0 | Approved media and synchronized video/UI | No graphic/identifying content; usable opening evidence |
| P0 | Detection + stable physical identity + Cosmos observation | Actual provider receipts and evidence-linked action |
| P0 | Cost timeline, review, close and deterministic report | Unknowns preserved; no duplicate charge |
| P0 | VAST ingest + scoped semantic search | Real asset/index/search receipt and playable hit |
| P1 | W&B agent and Weave held-out evaluation | Valid narrative and uploaded actual scores |
| P1 | Visual polish, exports, rehearsal and outage recovery | Full end-to-end demo inspected |
| Stretch | Webcam source, extra cases, aggregate review candidates | Only after P0/P1 path is stable |

The ledger and UI can proceed while service access is pending. Provider integration depends on verified schemas. Footage redaction and label creation precede upload/evaluation.

## Compressed 11:00 AM to 4:30 PM schedule

| ET | Work and checkpoint |
| --- | --- |
| 11:00-11:20 | Collect contracts/keys; inspect organizer footage; pick usable media, catalog and masks |
| 11:20-12:00 | Scaffold, fixture seed, ledger tests, UI player/timeline; provider smoke tests |
| 12:00-12:45 | Wire actual ingest/detection/tracking; approved clip and label first events |
| 12:45-1:30 | Cosmos observations, strict validation, reconciliation and real opening/use path |
| 1:30-2:10 | Case review/report; W&B agent; semantic search and timestamps |
| 2:10-2:50 | Held-out evaluation, Weave logging, cost/privacy/recovery checks |
| 2:50-3:20 | Fix meaningful failures; polish overlays, chart, unknown states and exports |
| 3:20-4:00 | Freeze features; full demo rehearsals; prepare permitted backup recording/cache |
| 4:00-4:30 | Final run, credentials/connectivity check, pitch timing and setup |

If starting at 9:30, use the extra 90 minutes for data selection, masks, labels and adapter discovery. The lunch agenda is not extra build time. App wiring takes priority over training a detector or expanding to many tool classes.

## Team responsibilities

These are human roles, not an instruction to launch Codex subagents: frontend/demo operator; provider/video pipeline; ledger/catalog/evaluation; pitch/data labeling. A smaller team combines roles. Team rehearses the pitch while implementation progresses, but one person owns each provider connection and the shared source/case IDs.

## Cut rules and blockers

- Missing API example after 20 minutes: ask the relevant organizer for a minimal working request and keep building the local path. Do not invent an endpoint.
- Organizer footage available: use it first. If unsuitable for OR claims, describe the actual scene and ask for another permitted clip; separate any fallback OR media clearly.
- No usable clinical video: use visibly disclosed simulated footage if feasible, or finish the ledger demo with missing-media state. Do not spend the event scraping random surgical videos.
- YOLO misses small supplies: reduce categories, improve permitted crop, label the limitation. Manually seeded item identities must be labeled; they do not count as automated detection accuracy.
- Cosmos lag: reduce bounded window demand, show lag or use cached actual inference with a badge. Do not call cached results live reasoning.
- VAST index slow: retain ingest/index receipts; do not silently substitute local text search under VAST branding.
- Agent unavailable: show deterministic report and narrative-unavailable state; the money still works.
- Weave unavailable: save local evaluation output and upload when access works; do not invent a dashboard link.
- By 3:20: feature freeze. Drop webcam, multi-case recommendations and manufacturing code before dropping evidence, correct money or recovery.

## Deliverables at implementation completion

Working startup commands and dependency locks; secret-free environment template; approved media manifest; fixture and test runner; verified adapter receipts; measured held-out eval with coverage; CSV/JSON report; exact demo click path; limitations and unresolved integrations; code on a repository branch. Public deployment is a separate explicit choice, especially for clinical footage.
