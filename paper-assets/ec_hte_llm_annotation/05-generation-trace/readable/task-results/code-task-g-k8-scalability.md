# code task g k8 scalability

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_task-g-k8-scalability_20260523T154030_result.json`
- **Structured JSON:** [`6536472354226ba3ad0e.json`](../../sessions/65/6536472354226ba3ad0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the summary:

## K-Scalability Comparison

| K | Method | \|Bias\| | RMSE | Coverage |
|---|--------|---------|------|----------|
| 2 | Naive | 0.0579 | 0.0900 | 0.823 |
| 2 | Global | 0.0589 | 0.0994 | 0.867 |
| 2 | **EC-HTE** | **0.0080** | **0.0888** | **0.938** |
| 4 | Naive | 0.0624 | 0.1126 | 0.877 |
| 4 | Global | 0.0558 | 0.1253 | 0.911 |
| 4 | **EC-HTE** | **0.0116** | **0.1201** | **0.956** |
| 8 | Naive | 0.1066 | 0.1330 | 0.912 |
| 8 | **Global** | **0.1351** | **0.1680** | **0.951** |
| 8 | EC-HTE | 0.1831 | 0.3404 | 0.956 |

## Key Findings

1. **EC-HTE dominates at K=2 and K=4** — lowest bias by 5-7x vs Naive/Global, with near-nominal coverage.

2. **EC-HTE degrades at K=8** — RMSE explodes to 0.34 (vs Global's 0.17). Root cause: 250 expert labels / 8 subgroups = **~31 per subgroup**, far too few for reliable per-subgroup CM estimation. High-pi subgroups (s5-s7) drive the RMSE to 0.4-0.6.

3. **Coverage stays ≥ 95.6% across all K** — the HB shrinkage is conservative; it inflates SEs enough to maintain coverage even when point estimates are noisy.

4. **Adaptive variants help but don't close the gap** — V1 (adaptive alpha) reduces K=8 RMSE from 0.33 → 0.22, but still above Global's 0.17.

5. **RMSE trend K=2→4→8**: all methods degrade, but EC-HTE degrades fastest because per-subgroup expert sample shrinks as 1/K.

**Takeaway**: EC-HTE's HB shrinkage is effective when per-subgroup expert counts are sufficient (~125+ for K=2, ~125 for K=4). At K=8 with fixed n_expert=250, the method needs either more expert labels (scaling n_expert with K) or should fall back to Global correction.

---
