# Demo fixtures and expected arithmetic

These are **synthetic ledger fixtures** to make the app and financial rules testable. They are not detections from a real OR recording. Materialize them as JSON during implementation; mark every event `origin=fixture`. No aligned video currently exists. Never overlay these timestamps on unrelated real footage.

## Illustrative catalog

| SKU | Category | Unit | Cents | Policy |
| --- | --- | --- | ---: | --- |
| `demo-suture` | suture packet | packet | 1800 | Disposable; auto-open quantity 1 |
| `demo-syringe` | syringe | each | 300 | Disposable; auto-open quantity 1 |
| `demo-gauze` | gauze pack | pack | 400 | Disposable; pack-level accounting |
| `demo-drape` | sterile drape | each | 1200 | Disposable; auto-open quantity 1 |
| `demo-suction-tubing` | suction tubing | each | 2200 | Disposable; auto-open quantity 1 |
| `demo-scalpel` | disposable scalpel | each | 800 | Disposable; auto-open quantity 1 |
| `demo-forceps` | reusable forceps | each | null | Reusable; excluded from disposable totals |

All prices are invented demo assumptions, not procurement quotes. The fixture sets these disposable SKUs `safety_critical=false` solely to exercise review candidate logic; real catalog flags require an authorized reviewer. Do not infer an instrument's safety role from this fixture.

## Event schedule

Duration: 180,000 ms. Case: `demo-case-001`; run: `fixture-run-001`; asset: `fixture-ledger-only`. Seed stable event IDs from the row name. All disposable quantities are one billed unit.

| Source ms | Instance / SKU | Event | Expected outcome |
| ---: | --- | --- | --- |
| 12000 | `suture-1` / demo-suture | OPENED | Opened cost $18 |
| 24000 | `syringe-1` / demo-syringe | OPENED | Opened cost $21 |
| 32000 | `gauze-1` / demo-gauze | OPENED | Opened cost $25 |
| 40000 | `forceps-1` / demo-forceps | HELD | Highlight reusable tool; no disposable dollars |
| 45000 | `drape-1` / demo-drape | OPENED | Opened cost $37 |
| 50000 | `syringe-1` | USED | Used cost $3 |
| 55000 | `drape-1` | USED | Used cost $15 |
| 60000 | `gauze-1` | USED | Used cost $19; do not price leftover individual pieces |
| 65000 | `suction-1` / demo-suction-tubing | OPENED | Opened cost $59 |
| 75000 | `suture-1` | USED | Used cost $37 |
| 85000 | `scalpel-1` / demo-scalpel | OPENED | Opened cost $67 |
| 90000 | `suture-2` / demo-suture | OPENED | Opened cost $85 |
| 100000 | `suture-2` | VISIBILITY_GAP through end | Its use remains unresolved |
| 105000 | `suction-1` | DISCARDED | Discard alone does not establish unused |
| 150000 | `scalpel-1` | VISIBLE_AT_END | Still needs full-history review |
| 180000 | `suction-1` | REVIEW_UNUSED | Fixture reviewer confirms never used through discard |
| 180000 | `scalpel-1` | REVIEW_UNUSED | Fixture reviewer confirms never used through case end |
| 180000 | `suture-2` | REVIEW_UNRESOLVED | No invented use or waste |

Reviewer events include `reviewer_id=fixture-reviewer`, a fixture reason and evidence IDs. A review timestamp is processing time, separate from its source evidence interval. The transcript marks these as authored ground truth, not an actual person reviewing unavailable video.

## Final expected result

```json
{
  "case_id": "demo-case-001",
  "inference_mode": "fixture_replay",
  "price_source": "illustrative_fixture",
  "opened_disposable_units": 7,
  "used_disposable_units": 4,
  "verified_unused_units": 2,
  "unresolved_opened_units": 1,
  "opened_cost_cents": 8500,
  "used_cost_cents": 3700,
  "verified_waste_cents": 3000,
  "opened_unused_exposure_cents": 1800,
  "unpriced_disposable_units": 0,
  "estimated_recurring_savings_cents": null
}
```

At 95 seconds, before unused dispositions, exposure is $48 ($22 + $8 + $18). At close it is $18, while verified waste is $30. Final partition: $85 = $37 used + $30 verified unused + $18 unresolved exposure. Supply cost is counted once despite multiple events. Replaying or seeking the same case leaves those totals unchanged.

## Mutation fixtures for tests

- Duplicate the suction opening from a retry and an overlapping window: final opened cost stays $85.
- Change suction tracker ID after an occlusion but retain the reviewed physical instance: no second billed unit.
- Void `suture-2` opening as a mapping mistake: opened cost becomes $67, exposure becomes zero; report revision increases.
- Add conflicting `USED` evidence for `scalpel-1`: its $8 leaves verified waste and becomes unresolved exposure until corrected. Final waste $22, exposure $26, used $37, opened $85.
- Remove suction price: opened priced subtotal $63, used $37, verified priced waste $8, exposure $18; one opened disposable unit is unpriced.
- Mark scalpel safety-critical: it remains $8 verified unused but receives no reduction candidate.
- Start a clip with an already unwrapped item: no `OPENED` charge without reviewed opening evidence.

## Selected media manifest template

This template is for future footage acquisition. Nulls mean unavailable, not verified.

```json
{
  "asset_id": "pending-selection",
  "source_type": null,
  "source_url": null,
  "rights_basis": null,
  "attribution": null,
  "source_sha256": null,
  "derivative_sha256": null,
  "duration_ms": null,
  "fps": null,
  "width": null,
  "height": null,
  "source_time_offset_ms": 0,
  "redaction_status": "pending",
  "redaction_transform_version": null,
  "reviewer_id": null,
  "visible_regions": [],
  "coverage_gaps": [],
  "contains_patient_footage": null,
  "may_process_with_models": false,
  "may_show_in_demo": false,
  "may_redistribute": false,
  "aligned_event_fixture": null
}
```

Allowed source types: `organizer`, `public_real_or`, `public_simulated_or`, `staged`. A rights-reviewed source derivative may be shown while source redistribution remains prohibited. Keep original and derivative filenames local, outside this public template. An application with no selected video shows a media-unavailable panel and ledger timeline, not a fake surgical player.
