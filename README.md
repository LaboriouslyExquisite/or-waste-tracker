# OR Waste Tracker

Build preparation for the VAST Builders Challenge. Working product name: **OR Waste Tracker**, built on the VAST Builders Stack; VAST is the infrastructure sponsor, not a claimed product affiliation.

**Camera -> YOLO detections and tracking -> Cosmos observations -> deterministic cost ledger -> W&B agent and Weave evaluation -> evidence-linked case report.**

This repository currently contains a specification package, not a running application. No sponsor endpoints, footage, prices, or measured accuracy have been supplied. The next implementation session should start with [BUILD_PROMPT.md](BUILD_PROMPT.md).

## Agreed experience

Use organizer-provided footage first when available, then suitable public real OR footage. Highlight sterile supply package opening, tool handoffs and visible use. Hide patients, faces, blood and the surgical field before footage reaches the browser or external models. Show how mapped disposable supply cost accumulates over source-video time, then show reviewed opened-but-unused waste at case end.

Opening a disposable sterile supply commits its cost; it does not itself establish waste. Reusable instruments are tracked separately and excluded from disposable waste. An item leaving the camera is unresolved unless there is evidence of use or a reviewed final disposition.

## Read the package

| File | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Implementation constraints and definition of done |
| [BUILD_PROMPT.md](BUILD_PROMPT.md) | Ready-to-paste implementation request |
| [Product](docs/PRD.md) | MVP, financial semantics and boundaries |
| [Architecture](docs/ARCHITECTURE.md) | Services, data flow and operational behavior |
| [Contracts](docs/CONTRACTS.md) | Events, schemas, ledger, API and report |
| [Video pipeline](docs/VIDEO_PIPELINE.md) | Detection, tracking, reasoning and redaction |
| [Prompts](docs/PROMPTS.md) | Cosmos observation and report-agent templates |
| [Stack access](docs/STACK_ACCESS.md) | Editable organizer handoff and secret checklist |
| [Datasets](docs/DATASETS.md) | Source research, access and suitability |
| [Demo fixtures](docs/DEMO_FIXTURES.md) | Known ledger outcomes and media manifest |
| [Interface](docs/UX.md) | Video overlay, cost timeline and review workflow |
| [Evaluation](docs/EVALUATION.md) | Ground truth, metrics and Weave integration |
| [Build schedule](docs/BUILD_PLAN.md) | Priorities, time boxes and fallback rules |
| [Pitch](docs/PITCH.md) | Demo script, evidence and expansion story |
| [Setup](docs/SETUP.md) | Codex, GitHub, runtime and deployment guidance |
| [Risks](docs/RISKS.md) | Specific failure modes and mitigations |
| [Sources](docs/SOURCES.md) | Verified references and limits of claims |

## Start when stack access arrives

1. Complete the non-secret handoff in [STACK_ACCESS.md](docs/STACK_ACCESS.md); put tokens in local environment variables.
2. Select a permitted clip using [DATASETS.md](docs/DATASETS.md), preprocess and inspect its redacted derivative.
3. Open this repository in Codex and paste [BUILD_PROMPT.md](BUILD_PROMPT.md).
4. Build the complete local replay path, then attach verified providers and run measured evaluations.

The best demo is one trustworthy case with clickable evidence. Claims about deployment at hospitals, hours searched, exact SKU costs or real-time accuracy must match the data actually demonstrated.
