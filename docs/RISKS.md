# Risks and concrete responses

| Failure mode | Observable signal | MVP response |
| --- | --- | --- |
| Footage never shows opening | Items begin already exposed | Segment analysis; no inferred opening charge; choose another permitted clip |
| Patient/field masking hides use | Item enters masked area | Show handoff/holding, preserve unknown use |
| Clinical media appears in thumbnail/export | Derivative bypass or unmasked scene | Serve only approved derivative IDs; check all demo evidence intervals |
| Incomplete case mistaken for complete | Missing beginning/end or skipped windows | Segment/coverage badge; no automatic never-used claim |
| Generic object mapped to wrong SKU | Brand/size invisible | Review catalog mapping; null price until mapped |
| Package and contents double billed | Two tracker IDs on one opening | One persistent billing instance with linked tracks |
| Identical items switch identity | Occlusion/handoff/re-entry | Association review; disputed instance unresolved |
| Reusable instrument counted as trash | Metal tool with unknown disposability | Reusable/unresolved category; exclude disposable totals |
| Used item discarded called waste | Discard without full history | Separate discard from reviewed unused disposition |
| Confidence mistaken for probability | High score despite wrong temporal inference | Label score; evaluate precision/coverage and inspect evidence |
| Pack leftovers overcounted | Multiple pieces from one pack | Pack-level accounting only in MVP |
| Endpoint assumed from vendor docs | Organizer payload differs | Verified service examples, adapter smoke-test receipts |
| Provider timeout or malformed JSON | Failed job / invalid schema | Bounded retries; coverage gap; no guessed event |
| Search index lag | Ingest complete, retrieval unavailable | Indexing status; label local search separately |
| One provider outage stops all reporting | Agent/Weave unavailable | Deterministic ledger survives; explicit narrative/logging status |
| Cost meter counts retries/seeks | Duplicate events or UI effects | Transactional canonical events and idempotent projections |
| LLM invents money/savings | Unsupported fields or wrong IDs | Compute dollars in code; validate references; recurring savings null |
| Reduction suggestion removes needed stock | Safety-critical flag or incomplete evidence | Review-only sealed-until-requested suggestions; retain availability |
| Data/license confused with code license | Code open, media gated | Read dataset-specific terms and maintain source manifest |
| Cached demo presented as live | No fresh provider receipt | Independent source/mode badges and real latency |
| Attribution/sponsor claims overstated | Unknown deployment or indexed duration | Match claims to receipts and actual media duration |

## Highest priority unknowns

Actual provider APIs; usable organizer media; supply opening/use visibility after redaction; catalog prices and unit semantics; detector vocabulary; latency on provided serving; source-use permissions. Resolve these before promising live accuracy or exact real procurement costs.

This is an operational prototype. It makes no clinical-use validation claim. Real-world extension would require representative data, procurement reconciliation, institutional permission, authentication, retention/access design and clinical review before preference-card decisions.
