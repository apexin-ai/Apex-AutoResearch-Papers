# experiment dir d dpp trace selection

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-d-dpp-trace-selection_20260520T155410_result.json`
- **Structured JSON:** [`8a44e0f38a23d3375cd0.json`](../../sessions/8a/8a44e0f38a23d3375cd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

| K_select | DPP-SC | Full-SC (K=12) | Delta | McNemar p | DPP-only correct | Full-only correct |
|----------|--------|----------------|-------|-----------|-------------------|-------------------|
| 4 | 50.98% | 54.41% | -3.43% | 0.2649 | 11 | 18 |
| 6 | 53.43% | 54.41% | -0.98% | 0.8318 | 10 | 12 |
| 8 | 55.88% | 54.41% | +1.47% | 0.6291 | 10 | 7 |

Full SC baseline confirmed at 54.41%. DPP diversity selection shows no statistically significant difference at any K_select (all McNemar p > 0.26). The trend is monotonic: accuracy increases with K_select, and K=8 slightly outperforms full SC — suggesting that on these traces, simply having more votes matters more than diversity-based filtering. DPP with K=6 loses ~1 point vs full K=12, not recovering it through diversity.

Results saved to `/root/symb_invariant_consensus/results/dir_d_dpp_trace_selection/results.json`.

---
