# Application contracts

Version: `1.0`. These schemas define our application, not the unknown Builders Stack API.

## Units and identity

Use UTC ISO-8601 processing timestamps, integer source-video milliseconds, integer USD cents and normalized `[x, y, width, height]` boxes in the redacted video's coordinate space. Bound each coordinate to `[0,1]`; require `x + width <= 1` and `y + height <= 1`. Dimensions, crop transforms and time offsets belong to the media manifest.

`case_id` identifies a case; `analysis_run_id` identifies a particular processing run; `instance_id` identifies one physical billed unit. Detector `track_id` is scoped to an asset, camera and tracker run. It is never the billing key. A packaging track can link to its contents under one instance. Ambiguous package-to-item association enters review without charging multiple identities.

## Catalog row

```json
{
  "sku": "demo-suction-tubing",
  "display_name": "Disposable suction tubing",
  "category": "suction_tubing",
  "billing_unit": "each",
  "unit_price_cents": 2200,
  "currency": "USD",
  "price_source": "illustrative_fixture",
  "price_as_of": "2026-10-09",
  "disposable": true,
  "safety_critical": false,
  "auto_open_quantity": 1
}
```

Unknown price is `null`, never zero. Unknown SKU remains unmapped. Freeze a versioned catalog snapshot when the case starts. Map labels to supplied SKUs through an operator selection or unambiguous package identifier; generic object recognition is not enough to establish a brand, size or price. Treat pack contents as the parent's billing unit in the MVP.

## Observation proposed by Cosmos

```json
{
  "schema_version": "1.0",
  "window_id": "window-0008",
  "observations": [
    {
      "track_ref": "table-cam:tracker-1:17",
      "action": "package_opened",
      "start_ms": 65000,
      "end_ms": 67000,
      "confidence": 0.86,
      "visibility": "clear",
      "evidence": "Sealed package separates and tubing is removed.",
      "uncertainty_reason": null
    }
  ]
}
```

Allowed actions: `package_opened`, `item_held`, `item_handed_off`, `item_visibly_used`, `item_discarded`, `item_visible_at_end`, `uncertain`. Visibility: `clear`, `partial`, `occluded`. Confidence is a model score, not a calibrated probability. Require the model to return only allowed track references or `null`; a null reference becomes an unassociated review proposal. Event times must be inside the supplied window and use global source time.

There is no model action called `confirmed_unused`. Observations do not directly write dollars.

After full-history reconciliation, the app may create an `unused_review_candidate` for an opened item without a use event and with captured final disposition, recording supporting intervals and coverage. This proposal is separate from accepted ledger events and verified waste. Missing visibility or failed windows instead yield an unresolved review proposal. The reviewer confirms or rejects the candidate using the available evidence; model non-observation alone never confirms non-use.

## Accepted ledger event

```json
{
  "schema_version": "1.0",
  "event_id": "evt-open-suction-1",
  "case_id": "demo-case-001",
  "analysis_run_id": "fixture-run-001",
  "instance_id": "suction-1",
  "asset_id": "fixture-ledger-only",
  "type": "OPENED",
  "source_start_ms": 65000,
  "source_end_ms": 67000,
  "observed_at": "2026-10-09T15:01:07Z",
  "origin": "fixture",
  "evidence_ids": ["evidence-suction-open"],
  "supersedes_event_id": null
}
```

Types: `OPENED`, `HELD`, `HANDOFF`, `USED`, `DISCARDED`, `VISIBLE_AT_END`, `VISIBILITY_GAP`, `REVIEW_UNUSED`, `REVIEW_USED`, `REVIEW_UNRESOLVED`, `VOID`. Origins: `provider`, `human`, `fixture`. Evidence IDs may point to ledger-only fixture descriptions, but those must not pretend a video clip exists.

`REVIEW_UNUSED` includes reviewer ID, reason, review timestamp and reviewed evidence IDs. It asserts the reviewed billing unit was never used through final disposition. `VOID` references the invalidated event. Replacement events append and supersede the original. Never edit old audit events in place.

## Reconciliation

1. Validate provider output and store it as an observation.
2. Map track/package identity to a persistent instance, or request review.
3. Reconcile overlapping proposals for the same physical instance, action and overlapping time interval into one canonical event. Use a deterministic reconciliation key, not an LLM-generated event ID.
4. Commit the canonical event in a transaction with a unique `event_id`.
5. Rebuild the projection from effective non-voided events, ordered by source time with stable tie breaking.

Transport retry uses the same job/event IDs. A separate inference run on the same case reconciles against existing physical instances; it does not create another charge. A deliberate reset creates another case. Keep all candidate proposals for debugging, but charge the unit once.

## Item projection

Store opening evidence, use evidence, held/handoff history, visibility intervals, final disposition, mapping status and review status separately. Do not force these independent facts into a single last-seen status.

- No opening evidence: do not count opened cost, even if the item was already unwrapped when the recording started. Show "opening not captured"; a reviewer can add an opening only with supporting evidence.
- An effective opening and observed/reviewed use: used disposable cost.
- An effective opening and reviewer-unused disposition, with no conflicting use: verified waste.
- An effective opening but neither established use nor reviewed unused disposition: opened-unused exposure. Mark unresolved when coverage or identity is incomplete.
- Contradictory use and unused reviews: keep committed cost, classify unresolved, remove verified waste until corrected.
- Discarding is a separate event. A used item discarded remains used.

Reviewing an item as used does not invalidate its original opening cost. A gap prevents a model-only never-used assertion; a reviewer can resolve the gap only with explicit supporting evidence, recorded in the audit.

## Money

For each mapped disposable instance `i`, let `p_i` be the frozen billing-unit price in cents. Compute sets from the effective projection:

```text
opened_cost = sum(p_i for known-priced opened disposable instances)
used_cost = sum(p_i for opened instances with established use)
verified_waste = sum(p_i for opened instances with reviewed unused disposition)
opened_unused_exposure = opened_cost - used_cost - verified_waste
```

Used and verified-waste sets must be disjoint. Contradictory instances belong to exposure. Unresolved exposure is a subset of exposure, not an additional cost. Unknown-priced items appear as counts outside these subtotals. Total unopened inventory, reusable instrument prices, hospital charges, taxes, reimbursement and procurement commitments are outside this calculation.

Chart series are projections as of the source cursor. Corrections can revise prior points; show report/version metadata. Billing quantities are integers with reviewed unit semantics; do not multiply a pack price by its contents.

## Our backend API

| Method and path | Behavior |
| --- | --- |
| `GET /api/health` | Local health and actual adapter states; no secrets |
| `POST /api/cases` | Create a case with approved derivative and frozen catalog |
| `GET /api/cases/{id}` | Case projection, cursor-independent totals, coverage and revision |
| `POST /api/cases/{id}/start` | Start configured processing/replay, idempotent request key |
| `POST /api/cases/{id}/pause` | Pause intake/pacing without clearing the ledger |
| `POST /api/cases/{id}/close` | Enter draining and finalize when ready; repeated calls are safe |
| `GET /api/cases/{id}/events?after_seq=...` | Durable ordered event transport |
| `GET /api/cases/{id}/stream` | SSE with IDs, resumable through Last-Event-ID |
| `POST /api/cases/{id}/reviews` | Human disposition/mapping/correction with expected revision |
| `POST /api/cases/{id}/search` | Scoped semantic retrieval, or explicitly local event search |
| `GET /api/cases/{id}/report` | Latest revision; distinguish provisional/final |
| `GET /api/cases/{id}/report/export?format=json` | JSON; implement CSV as a second format |
| `GET /api/media/{derivative_id}` | Only approved redacted media, range requests supported |

Accept only manifest-registered asset IDs; no arbitrary filesystem paths or remote URL fetches in public API requests. Search returns `asset_id`, `start_ms`, `end_ms`, `score`, `description`, `backend`, `derivative_hash`. Reject out-of-scope or out-of-range hits. Stream messages carry `seq`, `case_id`, `revision`, `event`, `projection`; reconnect never applies money twice. Return consistent errors: `code`, `message`, `retryable`, `request_id`; conflict reviews return HTTP 409.

## Report and agent constraints

Report fields: case/run IDs; mode and footage origin; catalog/derivative hashes; finalization status; coverage; opened/used/exposure/waste cents; unknown-price count; unresolved count; per-instance evidence; review audit; recommendation candidates; measured evaluation run link if applicable; report revision.

A candidate has `sku`, `suggestion` (`review_auto_open_quantity` or `keep_sealed_until_requested`), supporting item/evidence IDs, case count, verified unused count, observed unused cents, price source and rationale. Single-case output has `estimated_recurring_savings_cents: null` and "single-case review candidate".

For a stretch aggregate, require at least 20 reviewed complete cases matched by procedure and card version, and no safety-critical SKU. Estimate avoidable units as `max(0, current_auto_open_quantity - reviewer_approved_trial_quantity)`; report price times units as a scenario ceiling, plus observed use frequency and denominator. Do not claim realized savings until an actual matched intervention is measured. Agent output must cite valid IDs; reject fabricated money and recompute every displayed numeric field server-side.
