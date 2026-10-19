# analysis nested cv fix

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nested_cv_fix_20260519T115440_result.json`
- **Structured JSON:** [`a9d5cb6af81832c6c6f5.json`](../../sessions/a9/a9d5cb6af81832c6c6f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Here's the summary:

**R1-8B** (209 traces, 9667 steps):
- HS precision: 0.563 +/- 0.066, Text: 0.389 +/- 0.051
- **ΔPrec = +0.174 +/- 0.026** (HS > Text in 5/5 folds)
- Selected layers: L12 (3/5 folds), L13, L14 (early-mid layers)
- W_hs mixed: [3,3,5,5,3]

**OT-7B** (228 traces, 18260 steps):
- HS precision: 0.421 +/- 0.062, Text: 0.257 +/- 0.034
- **ΔPrec = +0.164 +/- 0.033** (HS > Text in 5/5 folds)
- Selected layers: L21-L27 (all late layers), L26 (2/5 folds)
- W_hs unanimous: W=5 in all 5 folds

**Cross-model**: HS beats text in all 10/10 folds across both models. R1-8B has higher absolute precision but similar delta. Layer selection patterns differ (R1-8B early, OT-7B late) but both consistently select late-ish layers relative to their architectures.

Files saved:
- Local: `artifacts/nested_cv/{r1_8b_results.json, ot_7b_results.json, report.txt}`
- Remote: `artifacts/nested_cv/{r1_8b_results.json, ot_7b_results.json, results.json, report.txt}`

---
