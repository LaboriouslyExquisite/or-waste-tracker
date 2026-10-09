# Implementation request

Paste the following into Codex with this repository selected, after filling the stack handoff. File paths below are relative to this repository root.

```text
Build the complete OR Waste Tracker MVP in this repository for the VAST
Builders Challenge. Continue through implementation, appropriate tests,
visual verification and a working demo; do not stop at a plan or scaffold.

Read AGENTS.md and README.md, then docs/PRD.md, docs/CONTRACTS.md,
docs/ARCHITECTURE.md, docs/VIDEO_PIPELINE.md, docs/PROMPTS.md,
docs/STACK_ACCESS.md, docs/DATASETS.md, docs/DEMO_FIXTURES.md,
docs/UX.md, docs/EVALUATION.md, docs/BUILD_PLAN.md, docs/PITCH.md,
docs/SETUP.md, docs/RISKS.md and docs/SOURCES.md.

Use the actual organizer docs and non-secret configuration supplied in
docs/STACK_ACCESS.md. Credentials are in the environment; never echo them.
Inspect the existing repository and preserve unrelated work.

Build React/TypeScript/Vite frontend + FastAPI/SQLite backend. First deliver
a runnable deterministic replay path with an event ledger, evidence view,
video overlays, cumulative cost chart, review actions, case report and
local event search. Materialize the documented synthetic ledger fixtures
and tests; do not present them as outputs from real video inference.

Use organizer footage first if available. Otherwise select rights-cleared
public real OR footage that actually shows the required actions. Check
access, download size and license before acquisition. A simulated OR clip
or staged tabletop is a visibly disclosed fallback; never pass it off as
real patient footage. If no suitable video is available, complete the
ledger demo with a clear media-unavailable state and identify the gap.

Create and inspect a redacted derivative that hides the patient, faces,
blood, surgical field, identifying text and audio before cloud upload or
browser delivery. Preserve opening and instrument-handling regions where
possible. If masking hides usage evidence, mark that item unresolved.

Connect verified VAST ingest and semantic search, organizer YOLO detection
and tracking, NVIDIA Cosmos video observations, W&B-served report agent,
and Weave traces/evaluations through adapters. Use organizer-provided
CoreWeave serving; do not train or provision a GPU cluster for this MVP.
Check actual request schemas before wiring each provider. Keep fixture,
cached inference and fresh inference modes unmistakably distinct.

Highlight a supply package when it is opened, distinguish handoff/holding
from visible use, and show exact arithmetic for mapped catalog prices over
source-video time. Separate committed opened cost, current opened-unused
exposure, human-verified waste and unpriced/unresolved supplies. Do not
count reusable tools as disposable waste. Do not treat disappearance as
proof of use. Close a case only after inference jobs drain; make revisions
auditable and prevent duplicate charges on retries, reconnects or seeks.

Generate an evidence-linked report and clinician-review candidates for
auto-open quantities / keeping items sealed until requested. Compute all
money in code. The agent explains findings from allowed tools and cannot
write preference cards, invent savings or make clinical decisions.

Implement meaningful tests from docs/EVALUATION.md: money, lifecycle,
duplicates, tracking identity, unknowns, failed inference, reconnect/seek,
privacy boundaries and report constraints. Run Weave evaluation against
held-out human labels with precision/recall, coverage, false waste and
cost error. Display actual results and sample counts; targets are not
measurements. Visually inspect the dashboard and evidence clips.

Provide README run commands, a secret-free .env.example, dependency locks,
a seed/import command, evaluation/export commands, local demo startup,
integration receipts and a concise demo script. Commit to a codex/ branch
and push to this repository when authenticated access is available. Do
not publish clinical media or make a public deployment by default.

If a provider is inaccessible, finish the independent local path and
report which smoke test remains unavailable. Make routine reversible
implementation decisions independently. Ask only for a missing answer
that changes authorized scope or genuinely blocks dependent work.
```

This prompt becomes specific enough for an end-to-end build once service contracts and usable media are supplied. It cannot make unknown APIs, unseen video events or absent catalog prices true.
