# Product specification

Venue update: [LATEST_BUILD_BRIEF.md](LATEST_BUILD_BRIEF.md) governs procedure ranking, multi-case navigation, clinical visual design and unused balance. [HANDOFF.md](../HANDOFF.md) records verified stack/data constraints and the 3:30 PM ET working-demo target.

## Problem and promise

Disposable sterile supplies opened for a procedure can incur cost even when never used. OR Waste Tracker connects video evidence to a catalog and produces an auditable account of what was opened, visibly used, left unresolved and verified unused.

The UCSF study observed 58 neurosurgeries in August 2015. It reported a sample mean of $653 unused supplies, and a case-mix-adjusted departmental estimate of $968 per case and $2.9 million per year. These are historical figures for that department, not a present-day universal surgery benchmark. [Original study](https://pubmed.ncbi.nlm.nih.gov/27153160/)

## Users and workflow

The demo user is an OR operations or supply reviewer. They select one permitted recording, inspect tracked supply events, reconcile uncertain items, close the case and review preference-card candidates. The app supports operational review; it does not direct surgery or replace supply counts.

1. Import organizer footage, or suitable public real OR footage.
2. Review a cropped/masked derivative and set supply-table and handoff regions.
3. Start paced video analysis or replay with the source type and inference mode visible.
4. See opening, handoff and visible-use highlights with click-to-play evidence.
5. Follow committed disposable supply cost and current unused exposure over video time.
6. Review uncertain identities, SKU mappings and final unused dispositions.
7. Close after pending analysis drains; export a versioned case report.
8. Search a question such as "where was suction tubing opened?" and jump to a matching evidence clip.

## MVP scope

Procedure overview and multi-case navigation are required. Start actual video analysis with one qualified camera/case, one currency (USD), distinguishable disposable classes and a reviewed catalog. Match actual visible classes; fixture categories are not detector accuracy promises. Synthetic cohorts remain separate. Show reusable tools separately. Paced recording analysis first; webcam streaming is a stretch. External VSS import requires organizer clarification.

Required screens: case workspace with video and timeline, evidence/review drawer, case-end report and clip search. Required systems: video redaction, provider adapters, deterministic ledger, SSE updates, report agent, Weave evaluation, explicit fallback modes.

Also required: procedure ranking, procedure case list and preference review navigation. Live unused balance is opened minus used, equal to verified waste plus exposure; it is not refunded money.

## Monetary meanings

| UI label | Meaning |
| --- | --- |
| Opened supply cost | Sum of mapped disposable billing units with an effective opening event |
| Opened-unused exposure | Known opened disposable units without observed use or verified unused disposition; includes unresolved units |
| Verified waste | Opened disposable units a reviewer confirms were unused at final disposition |
| Unresolved | Usage, opening, identity or mapping cannot be established from available evidence |
| Unpriced items | Items counted without a known catalog price; excluded from dollar subtotals |

All subtotals state catalog provenance. Illustrative prices produce exact arithmetic under assumptions, not exact hospital procurement costs. Opened-unused exposure can decrease when an item is used. A verified unused disposition can occur before case end when sufficiently documented, so the waste meter can tick during review. Never force an upward waste animation just because something opens.

For an opened item with obscured use, committed cost is still known if identity and price are known; waste is unresolved. Merely holding an item does not establish use. Merely finding it on the table at case end does not establish that it was never used earlier.

Count packs at their billing unit. In the MVP any visible use of a gauze pack means the pack is used; estimating leftover individual sponges is out of scope. Opening reusable instrument packaging does not make the instrument a disposable waste item.

## Recommendations

For a single case, show "review whether this item can remain sealed until requested" with evidence and that case's verified unused cost. Keep the item available. No guaranteed savings or automatic card edits. Recurring recommendations require matched procedures, reviewed complete cases, an explicit minimum sample rule and exclusion of safety-critical items. Detail is in [CONTRACTS.md](CONTRACTS.md).

## Out of scope

Hospital deployment, EHR integration, inventory purchasing, clinical instructions, patient identity, surgical quality scoring, model training, fine-tuning, per-sponges partial-use waste, exact brand recognition from an unlabeled tool, robotic manufacturing implementation and autonomous preference-card editing.

## Success

A judge can watch a redacted clip, see a correctly timed opening highlight and catalog cost increment, inspect a use event, review a final unused item, verify the cost arithmetic, retrieve a relevant clip with VAST search, and inspect real evaluation results. Each sponsor's role is backed by an actual provider call or clearly identified as unconnected.
