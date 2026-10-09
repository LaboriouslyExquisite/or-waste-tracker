# Interface specification

Venue update: [LATEST_BUILD_BRIEF.md](LATEST_BUILD_BRIEF.md) controls overview/procedure/case navigation, light clinical palette, final-table review and unused balance. Evidence interactions below still apply.

The central experience is a redacted recording with synchronized supply observations and an honest cost timeline. Keep opening and evidence visible; keep model/service internals in a compact provenance drawer.

## Case workspace

Header: product name, anonymized case ID, source type, inference mode, playback/analysis state. Prominent badges distinguish real organizer footage, public real OR, simulated OR, staged media and synthetic ledger replay. Show provider lag and stale-data state when material.

Main area: video on left, live summary/event feed on right, chart below. White/light slate workspace, navy navigation/type and dark video frame. Teal for used, amber exposure, restrained red verified waste, grey uncertain and violet reusable tools. Labels/icons carry the same information as colors.

Metric cards:

1. Opened supply cost, with "priced disposable units only" and price provenance.
2. Opened-unused exposure, with unresolved portion/count.
3. Verified unused waste, with reviewer count.
4. Unpriced/unresolved item counts, selectable for review.

Before any reviewed unused disposition, the verified-waste card may be zero. Explain that openings increase committed cost, not verified waste. Do not use a misleading escalating dollar animation.

## Highlights and playback

Opening: a short amber pulse around the supply package, label "Package opened", category, source time and mapped unit price or "unpriced". Handoff: label "Handed off", without a use claim. Visible use: teal label "Use observed" with evidence. Reusable tools: category plus "Reusable - excluded from disposable waste". If staff role is configured from known context, a handoff can say "to surgeon"; never infer identity from a face.

Scale normalized boxes against the actual displayed video rectangle, including letterboxing and cropping. Overlay bounds are in the redacted derivative's coordinate space. Hide detections in masked regions. User controls: play/pause, source-time scrubber, speed, overlay toggle and event filters.

Cost chart: cumulative opened cost as the primary stepped line, with separate used, exposure and verified-waste series. X-axis is source-video time, not server processing time. Marker clicks open evidence; cursor movement synchronizes both views. Show revisions if late evidence changes earlier projections. Future events remain hidden during paced playback.

## Evidence and review drawer

Selecting an event opens the permitted clip interval, action label, item identity, mapping, source time, short evidence description, coverage gaps and provenance. A model score is labeled "model score" without a certainty claim. Include opening, use and final-disposition links for the same instance.

Actions: map SKU/billing unit, confirm unused with evidence and reason, confirm used with evidence, leave unresolved, or correct an event. Show the financial effect of a review before recording it. Each review is auditable and concurrency-checked. An uncertain item must not become confirmed just because the drawer closes.

On `Close case`, enter draining, display remaining jobs/gaps and list review candidates. The final report can be finalized with unresolved items, which stay explicitly unresolved. Do not force a clean total by guessing.

## Case report

Show source/mode, analyzed time span, catalog provenance, exact mapped-cost arithmetic, verified-unused items with evidence, unresolved/unpriced lists and candidate preference-card reviews. For fixture case: $85 opened, $37 used, $30 verified unused, $18 unresolved. Use the fixtures' authored-review label.

Recommendations use "Review auto-open quantity" or "Keep sealed until requested". A single-case row displays that case's unused cost, and "Recurring savings not established". Download JSON/CSV. Exported records retain source type, inference mode, coverage and report revision.

## Search

Search within approved case assets. Result cards show time, masked thumbnail, description and backend badge. VAST semantic results and local event-text results have different labels. Search retrieval is evidence discovery, not new ledger truth. Empty results are useful states; do not return an unrelated highlight as a match.

Example queries: "package opening near the table", "suction tubing handed off", "tool visibly used". "Never used" should retrieve reviewed ledger evidence if available; a generic semantic result cannot establish a negative across a whole case.

## States and visual acceptance

Handle: no media, unapproved redaction, ingest/indexing, paused, stale, provider timeout, invalid response, failed window, unpriced item, disputed identity, drain-in-progress, empty search and report unavailable. These states retain the ledger and show a concise recovery action.

Check the 1440px laptop/judge view and a 1024px fallback; desktop first. Keyboard controls and readable type are required. No graphic patient imagery in hero images, thumbnails, tooltips, evidence or exports. Verify overlays after resize and fullscreen. Do not put credential names or developer logs into the routine product flow.
