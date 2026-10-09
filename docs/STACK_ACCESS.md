# Verified venue stack handoff — October 9

Official source: [workshop repository](https://github.com/vast-data/vast-builders-challenge). VM checkout `~/vast-builders-challenge`, observed revision `0c6b756`. Windows checkout is separate; no SSH or remote filesystem mount established. Read current VM skills before mutations. [HANDOFF.md](../HANDOFF.md) records state and gaps.

## Infrastructure and limits

Remote pipeline models: Cosmos3-Reason, YOLO11s, Cosmos Embed1 on CoreWeave. Use existing VSS retrieval/re-ingest, not local provisioning. Published corpus lists traffic, street, warehouse and indoor material, without OR footage. Team 8 inventory/runtime remain untested. YOLO is not a footage library or an established surgical supply detector.

The event guide prohibits internet-video ingest; its architecture describes re-ingesting pre-indexed segments. A technical upload route exists, but **organizer permission for external/staged OR content is unresolved**. Do not bulk re-ingest or modify DataEngine. [Architecture reference](https://github.com/vast-data/vast-builders-challenge/blob/main/ARCHITECTURE_REFERENCE.md).

## Credentials and configuration

Use the VM's single `/config/*.config` and exported environment server-side. Resolve Team 8 only. No config values, passwords, JWTs or signed URLs in logs/Git. Do not inspect other teams' files or request secrets in chat.

Documented variable names: `INGRESS_URL`, `USERNAME`, `PASSWORD`; `S3_ENDPOINT`, `ACCESS_KEY`, `SECRET_KEY`, `S3_CHUNKS_BUCKET`, `S3_SEGMENTS_BUCKET`; `VDB_ENDPOINT`, `VASTDB_BUCKET`, `VDB_SCHEMA`, `VDB_COLLECTION`; `WANDB_API_KEY`, `WANDB_TEAM`, `WANDB_PROJECT`; `COSMOS3_REASON_URL`, `YOLO_URL`, `COSMOS_EMBED1_URL`. Model endpoints are independent; do not derive one host from another. W&B report-model ID, Weave configuration and trace permissions remain unverified. [config.example](https://github.com/vast-data/vast-builders-challenge/blob/main/config.example).

## Verified public contracts

Routes below were read from organizer skills; successful calls have **not** yet been made. Base is configured `INGRESS_URL`. Preserve actual response shapes before normalizing to application contracts.

| Operation | Route and important fields | Primary skill |
| --- | --- | --- |
| Login | `POST /api/v1/auth/login`: username/password JSON; access_token response. `GET /api/v1/auth/me` verifies. Cache server-side; refresh once on 401. | [login](https://github.com/vast-data/vast-builders-challenge/blob/main/.cursor/skills/retrieval/login/SKILL.md) |
| Search | `POST /api/v1/search`: query, top_k, llm_top_n, min_similarity, metadata_filters, time_filter, tags. Returns results/chunk_results/optional llm_synthesis. | [search](https://github.com/vast-data/vast-builders-challenge/blob/main/.cursor/skills/retrieval/search/SKILL.md) |
| Explore | `GET /api/v1/videos/explore`: scope, limit/offset, optional date/location; returned original_video/source references. | [videos](https://github.com/vast-data/vast-builders-challenge/blob/main/.cursor/skills/retrieval/videos/SKILL.md) |
| Evidence | `GET /api/v1/videos/metadata` and `/detections`: source parameter. Sidecar 404 means unavailable detection evidence. | videos skill |
| Playback | `GET /api/v1/videos/stream` or `/playback-url`: source; provider accepts token in query. Proxy server-side to hide token and enforce approved media allowlist. | videos skill |
| Synthesis | `POST /api/v1/videos/synthesize`: original_video, question, max_segments, optional system_prompt. Language summary, not a financial projection. | videos skill |
| Re-ingest | `POST /api/v1/dashboard/reingest`: exact Explore original_video, chunk_count=1 and chosen prompt/metadata. Status `GET /api/v1/dashboard/reingest/{job_id}`. | [reingest-chunk](https://github.com/vast-data/vast-builders-challenge/blob/main/.cursor/skills/ingest/reingest-chunk/SKILL.md) |
| Upload (permission pending) | `POST /api/v1/videos/upload`: multipart file, is_public, optional metadata/custom_prompt. Discover live limits through config/ingest-config. Upload success is not indexing success. | [upload-video](https://github.com/vast-data/vast-builders-challenge/blob/main/.cursor/skills/ingest/upload-video/SKILL.md) |

Discover metadata values. Similarity is not event certainty. Verify timestamp units and media offsets; exact within-segment action timing requires refinement/review.

Custom prompt candidate for qualified permitted footage; check live length limit:

```text
Describe visible disposable supply package opening, removal of contents,
holding, handoff, functional use, discard and items on the table at segment
end. Distinguish these actions. Give approximate offsets within this segment
and observable evidence. State occlusion, ambiguity and missing history.
Do not infer use from disappearance, never-used from absence, a surgeon's
role from appearance, or brand/SKU/price. Reusable tools are separate.
```

Descriptions are proposals, not accepted ledger facts. Validate observations and identity. The pipeline's text output is not assumed to satisfy our structured JSON schema.

## Deployment and receipts

Read [deploy-app-no-registry](https://github.com/vast-data/vast-builders-challenge/blob/main/.cursor/skills/deployment/deploy-app-no-registry/SKILL.md): team Kubernetes namespace, code ConfigMap, credentials Secret, ingress `/app`, portal **App** button. Use actual configured host, not hardcoded examples. React/API base paths must support `/app`. Check bundle limits and persistence; media does not belong in ConfigMaps. Local development is useful for verification; hosted event deliverable follows current team skill. No deployment attempted yet.

Each connection needs sanitized operation, request ID, provider/version, asset hash if relevant, timestamp, latency, response shape and actual status. Needed receipts: VSS login/inventory, search plus permitted playback, detections, authorized re-ingest/indexing, W&B grounded report, Weave trace/evaluation. Adapter without receipt = unconnected. Distinguish fixture replay, cached provider output and fresh inference.
