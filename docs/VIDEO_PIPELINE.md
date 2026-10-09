# Video and inference pipeline

## Media selection and redaction

Use the source order in [DATASETS.md](DATASETS.md). The primary camera should show the package-opening area and supply table, not just tools that were already opened. A view of the table alone cannot establish all clinical usage.

Before ingest, register source permission, source type, duration, timestamps and original hash locally. Produce a separate derivative with a reviewed crop, masks and stripped audio/metadata. Keep its own hash and source time mapping. Raw originals remain outside all served/public directories. A browser-side blur is insufficient: the browser would still receive the original pixels.

Prefer a crop around the opening zone, back table and visible gloved hands. If sensitive content remains, use opaque masks for patient/body/surgical-field regions and identifying text, with face blur or masking as appropriate. The user-facing requirement is that blood and patient imagery cannot be seen; use opaque redaction where blur still reveals it. Configure moving masks if the camera or patient region moves. Face detectors are an aid, not a complete privacy check.

Inspect beginning/end, scene changes, every event evidence interval and thumbnails; check the entire demo clip before approval. Mute audio by default and strip titles containing names. Store `redaction_status=approved` with reviewer and transform version. Only approved derivatives may be ingested, sent to inference/search, traced or served. Masked thumbnails and exports must derive from that same file. Reprocessing invalidates approval until rechecked.

The mask can remove clinically informative action. In that case record handoff/holding if visible and mark use unresolved. Never infer visible use from entry into a hidden surgical field.

## Detection and tracking

Use organizer YOLO first; test its supported classes and output. If open-vocabulary detection is available, start with category prompts such as "sealed surgical supply package", "syringe", "surgical gauze pack", "suture packet", "suction tubing", "sterile drape" and "disposable scalpel". Prompts must match actual footage, packaging and view scale. Generic boxes do not establish sterile status or SKU.

YOLO-World is a possible fallback, not confirmed event infrastructure. Its official integration supports vocabulary customization and tracking. ByteTrack is an explicit baseline choice for a fixed camera; maintain tracker state per stream. [YOLO-World](https://docs.ultralytics.com/models/yolo-world/), [tracking](https://docs.ultralytics.com/modes/track/)

Detect at an initial 5 FPS and maintain normalized boxes in derivative coordinates. Keep full video timing. A detector score threshold is tuned on development clips, never chosen to make the test results look better. If small items fail, improve crop/lighting or reduce classes; avoid a hackathon training project.

Create application instances from reviewed initial inventory plus opening proposals. Relate package and contents through temporal/spatial continuity. Similar identical items, an occlusion, changing labels, a handoff and a lost/recreated tracker ID require conservative association. No reliable association means unresolved, rather than two charges or an invented continuity.

Reusable forceps/scissors may be highlighted with a "reusable tool" label; they do not enter the disposable cost meter. If a visible instrument is not known to be disposable, leave its billing classification unresolved.

## Candidate windows and Cosmos

Maintain an 8-second ring buffer with 2-second overlap as a starting configuration. Include candidate openings, handoffs, use and discard actions; also run periodic windows so detector-triggered sampling does not miss entire actions. Preserve the opening zone and hand context in the provided clip; an object crop alone may omit the package seal or relationship.

Provide the approved derivative window, absolute window start/end milliseconds, candidate track references, a concise vocabulary, visible regions and coverage gaps. Media comes before task text where the actual model API supports it. Output temporal observations using [PROMPTS.md](PROMPTS.md). The endpoint can be Reason1, Reason2 or an organizer wrapper; discover the actual model and video transport at the event.

NVIDIA's Reason2 guide describes prompt-requested JSON and temporal outputs. They still need schema parsing, range checks and behavior evaluation. NIM documents a `video_url` extension, which is an example of a provider transport, not a verified organizer payload. [Prompt guide](https://nvidia-cosmos.github.io/cosmos-cookbook/getting_started/prompt_guide/reason_guide.html), [NIM API](https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/cosmos-reason2/api.html)

## Validation and timing

Require a strict schema, approved action names, known track references and valid source times. Do not scrape an arbitrary JSON-like substring from a reasoning transcript. Use a documented final-answer format if the provider includes reasoning. One bounded repair retry is permitted; record original failure and repair separately. A second invalid response becomes a failed window and coverage gap.

Start with at most one concurrent reasoning request and tune from measured quota/latency. Timeouts and bounded retries are configurable. Retry keys and derivative/window/config hashes prevent duplicate jobs. Window overlaps reconcile into the same physical event. Reasoning is observational; the financial ledger applies deterministic rules afterward.

Opening recognition must see a seal/wrapper being breached and associate the exposed disposable unit. A tool already unwrapped at clip start is `opening_not_captured`. "Used" needs observable functional use, not carrying or preparing. "Unused" is a retrospective reviewed disposition; it cannot be inferred solely from absence of observed use.

## Case end and trace policy

Stop new intake, drain inference jobs, report gaps, reconcile disputed items, then close. A human reviews proposed unused items with linked intervals and coverage. Full visibility is supporting evidence, not a guarantee. Any source with partial case coverage should be labeled a segment analysis.

The application can generate an `unused_review_candidate` from an opened disposable instance with no accepted use event and a captured final disposition. Attach the opening/final intervals, every visibility or processing gap, and the reason it may be unused. It is a review proposal, not a Cosmos assertion of never-used truth. An instance with gaps is proposed as unresolved instead. Compute processing coverage from successful window intervals over the analyzed span, and item visibility coverage from observed track intervals; report these separately. Neither percentage proves absence of use between sampled frames. Evaluate this candidate-generation rule against adjudicated final dispositions before using it in the demo.

Weave traces record redacted asset IDs/hashes, window times, configuration/prompt versions, sanitized request IDs, latency, parsed observations, validation outcomes and scorer results. Do not attach raw video, headers, tokens, signed URLs or sensitive captions. Redacted media export requires source permission separately from local analysis.
