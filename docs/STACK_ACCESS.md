# Builders Stack handoff

Status: **no organizer API documentation or credentials supplied yet**. Fill this document with non-secret information at the event. Public vendor docs are reference material; they do not establish the event service contract.

## Confirm with organizers

| Question | Answer / link |
| --- | --- |
| Official quickstart / example repository | Pending |
| Event rules on advance preparation, public code and data | Pending |
| Provided videos and their permitted demo/export uses | Pending; use organizer footage first when available |
| Is provided footage OR footage, and does it show supply opening? | Pending |
| Ingest mechanism: API, SDK, object store or mounted path? | Pending |
| Pipeline readiness/status operation | Pending |
| Semantic search request and response example | Pending |
| YOLO model/version, supported classes and vocabulary changes | Pending; YOLO-World is not assumed |
| Detector returns tracks or only frame detections? | Pending |
| Cosmos model/version and supported media transport | Pending |
| Cosmos clip limits, sampling, JSON/reasoning format | Pending |
| W&B inference endpoint, model IDs, auth and project | Pending |
| Weave account/entity/project and logging constraints | Pending |
| CoreWeave-hosted inference already running, or deployment needed? | Pending; prefer supplied serving |
| Service quotas, timeouts, concurrency and credit expiry | Pending |
| Allowed outbound destinations and signed-URL lifetime | Pending |
| Local backend / hosted backend / demo connectivity | Pending |

## Record one contract per provider

For VAST ingest, VAST search, YOLO, Cosmos, W&B agent and Weave, collect:

```text
Documentation URL:
Service owner / organizer contact role:
Base URL (no embedded credentials):
Model ID / API version:
Authentication method:
Environment variable containing credential (name only):
Minimal secret-free request example:
Minimal sanitized response example:
Supported input media and size/duration limits:
Timestamp units and offset convention:
Request quota and concurrency:
Storage or dataset namespace:
Network / access requirements:
Smoke-test request ID and time:
Smoke-test result:
```

Keep request/response examples sanitized; remove authorization headers and signed URLs. Do not commit event keys just because they expire soon.

## Proposed application environment

These names belong to our app and can change when provider contracts are known. Generate a real `.env.example` during implementation, with empty secrets. Never put secrets in `VITE_` variables.

```dotenv
APP_MODE=fixture_replay
APP_HOST=127.0.0.1
APP_PORT=8000
DATABASE_PATH=runtime/or-waste.sqlite
STACK_CONFIG_PATH=config/stack.local.json
MEDIA_ROOT=media/redacted
VAST_BASE_URL=
VAST_API_KEY=
YOLO_BASE_URL=
YOLO_API_KEY=
COSMOS_BASE_URL=
COSMOS_API_KEY=
COSMOS_MODEL_ID=
AGENT_BASE_URL=
AGENT_API_KEY=
AGENT_MODEL_ID=
WANDB_API_KEY=
WEAVE_PROJECT=
```

No one-to-one credential relationship is assumed. The organizer may supply one shared token, per-service keys, a gateway login or no token inside an isolated environment. If ingest is confirmed S3-compatible, collect the specific endpoint, bucket, region and access/secret credentials then; do not require AWS credentials otherwise. Only use a Hugging Face token if the selected download actually requires it.

## Integration smoke tests

1. Ingest one small **approved redacted** derivative; persist the returned asset ID and readiness receipt.
2. Detect a known visible item and normalize output coordinates; confirm tracking/vocabulary behavior.
3. Ask Cosmos about one known action; parse its actual final-answer format and verify source-time conversion.
4. Query semantic search against that asset; play the returned permitted interval.
5. Ask the W&B-served model to summarize a computed sample ledger; validate output IDs.
6. Send a sanitized Weave trace and a tiny evaluation; confirm the run exists in the intended project.

Receipts include provider/version, derivative hash, job/request ID, status, latency and redacted response shape. An adapter implementation without a successful receipt is `unconnected`. If search is still indexing, show `indexing`; do not label local text search as VAST semantic search.

## References, not assumed event defaults

- [VAST event stack](https://www.vastdata.com/lp/vast-builders-challenge) describes supplied services without public API schemas.
- [NVIDIA NIM Reason2 example](https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/cosmos-reason2/api.html) documents one `video_url` transport.
- [W&B Serverless Inference](https://docs.wandb.ai/inference/) documents an OpenAI-compatible option; use event-specific access and model IDs.
- [Weave evaluation](https://docs.wandb.ai/weave/tutorial-eval) provides the evaluation workflow.
