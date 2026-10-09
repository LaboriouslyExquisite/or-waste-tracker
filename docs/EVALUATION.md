# Evaluation and acceptance

Weave records experiments and scorer results; it does not itself prove correctness. Compare predictions against independent human labels and report uncertainty, sample size and coverage. No accuracy has been measured yet.

## Ground truth

Human annotators label the **same approved derivative** the model sees. Record case/asset/instance IDs, time intervals, opening, holding/handoff, visible use, discard, visibility gaps, billing unit and reviewed final disposition. A supply already open at recording start is not a captured opening. Hidden clinical use is unknown. Catalog mapping truth is separately reviewed.

Create development and held-out splits by whole case/take, not overlapping clips from one recording. Start with at least three separate takes and aim for 20+ opening/use events plus hard negatives, then report the actual achieved count. Two team members independently review ambiguous intervals and adjudicate disagreements. Synthetic ledger fixture tests do not count as video inference accuracy.

Freeze prompts, thresholds and preprocessing using development clips before the held-out run. Keep raw model output private/sanitized and predicted events distinct from ground truth. Evaluate the untouched model outputs before any human correction, and separately report reviewed operational results.

## Metrics

| Metric | Calculation / interpretation |
| --- | --- |
| Opening / visible-use precision and recall | One-to-one matching by case, true instance and action; start-time tolerance initially +/- 2 sec, fixed before evaluation |
| Temporal error | Absolute start-time error for matched events; report median/p95 and misses separately |
| False waste rate | Incorrect model unused proposals / all predicted unused proposals; unknown truth cannot count as correct |
| Unused-proposal precision / recall | Compare reviewer-candidate classifier against adjudicated complete disposition truth; include denominator and exclude unknown truth only with its count reported |
| Coverage / abstention | Determinate predictions / eligible units; unknowns and failed windows remain visible |
| Identity errors | Switches/incorrect physical associations and duplicate billed units per case |
| Cost error | Absolute opened-cost and proposed-unused-cost error in cents per case using the same catalog snapshot |
| Schema validity | First-response validity and post-repair validity, reported separately |
| Latency | Capture/window end to validated event, plus ingest, search and report latency; p50/p95, timeout count |
| Search retrieval | Human-labeled query-to-interval relevance; top-3 recall on a small fixed query set |
| Report validity | Existing IDs only; correct numeric fields; no disallowed suggestion or invented savings |

If the model never proposes unused items, false waste rate is undefined, not 0% excellence. Human-verified waste is not an automatic model prediction; reporting its post-review correctness as model accuracy would be misleading. Do not collapse opening detection, use reasoning and waste accounting into one headline "accuracy".

Money metrics exclude unknown-priced units only when their count is also reported. For temporal matching, unmatched predicted events are false positives, unmatched labels are false negatives; one prediction can match at most one label. Ground-truth instances, not raw tracker IDs, define correct identity. Include coverage failures from detector misses and failed inference, not only successful Cosmos windows.

## Weave implementation

Use a versioned dataset, instrumented predictor and deterministic scorers. Record model IDs, prompt/schema versions, preprocessing hash, derivative hashes, split, run mode and thresholds. The official tutorial shows `weave.Model`, `weave.Dataset`, `weave.Evaluation` and `@weave.op`; use the SDK version actually installed. [Weave tutorial](https://docs.wandb.ai/weave/tutorial-eval), [scorer reference](https://docs.wandb.ai/weave/guides/evaluation/scorers)

Trace detection normalization, Cosmos parsing, reconciliation and report generation. Log sanitized IDs/metadata only. Weave connectivity failure must not halt local projections; persist local eval JSON with "Weave upload pending". Show a live run link only after verifying the upload. A judge-facing eval panel includes counts, split name and whether inputs were real or simulated footage.

## Functional tests required during implementation

1. Fixture arithmetic: $85 opened, $37 used, $30 verified unused and $18 unresolved, using integer cents.
2. Pack price counted once; reusable tool excluded; null price never silently becomes zero.
3. Opening does not imply waste; holding/handoff does not imply use; disappearance produces unresolved state.
4. Duplicate delivery, overlapping windows, new tracker ID, repeated close and reconnect never bill the same physical unit twice.
5. Void/replacement and contradictory evidence create the expected recalculation and report revision.
6. Source-time offsets, late events, cursor seeking, resize and letterboxing preserve correct chart and overlay timing.
7. Malformed JSON, unknown references, out-of-window timestamps and timeouts yield failed jobs/gaps, not invented events.
8. Draining waits for accepted jobs or records explicit failures; unknown items survive finalization.
9. Agent rejects nonexistent IDs, fabricated costs, safety-critical reduction candidates and one-case recurring savings.
10. Search remains within permitted derivatives/case IDs; invalid remote hits are rejected.
11. No original media is served or sent to provider/trace mocks. Use raw/derivative sentinel paths and request capture to test the boundary.
12. Restart preserves ledger/catalog/review state; reset creates a separate run/case with independent tracker state.

## Demo acceptance targets

Targets to tune toward, not claims: opening precision >= 0.90 and recall >= 0.80; visible-use precision >= 0.85; valid accepted-event schema 100%; duplicate charged units zero; fixture arithmetic exact; fresh inference p95 lag <= 15 seconds on the selected clip. Show observed metrics even if targets are missed.

Before demo, manually inspect every evidence clip/thumbnail for redaction and verify one complete path: start -> opening highlight -> cost increment -> visible use -> reviewed unused -> close -> report -> semantic search. Test provider outage fallback with an explicit cached/replay mode badge. Record the demo once as a recovery artifact if source permissions allow it.
