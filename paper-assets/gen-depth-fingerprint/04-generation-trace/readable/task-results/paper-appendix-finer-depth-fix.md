# paper appendix finer depth fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix-finer-depth-fix_20260516T003102_result.json`
- **Structured JSON:** [`e3db7c6ecde1313c8c39.json`](../../sessions/e3/e3db7c6ecde1313c8c39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All corrected values are consistent across all 4 files (2× appendix_finer_depth.tex + 2× discussion.tex). The `_backup/results_b30771.tex` match on 0.476 is unrelated (it's a correlation coefficient, not a classifier F1).

**Summary of fixes** (all values corrected to match `finer_ordinal_results.json`):

| Location | Old → New |
|---|---|
| Table 1 per-gen Macro F1 | 6 values, all off by 0.3–1.4pp |
| Table 1 per-gen Accuracy | 6 values, all off by 0.2–1.2pp |
| Table 1 Average | 0.507±0.036 → 0.501±0.038, Acc 0.546→0.541 |
| Table 2 per-class F1 | Gen-0: 0.936→0.921, Gen-2: 0.276→0.268, Gen-4: 0.425→0.423 |
| Analysis: drop magnitude | 0.282 → 0.288 |
| Analysis: confusion % | 36.2%→36.5%, 37.2%→37.8% |
| Classifier comparison | HGBT 0.503→0.501, CI adjusted, RF 0.477→0.476, XGBoost 0.507→0.501 |
| Discussion: all echoed values | Same corrections propagated |

Weighted F1 column left unchanged — the JSON doesn't contain per-generator weighted F1, so those values can't be verified from this data source.

---
