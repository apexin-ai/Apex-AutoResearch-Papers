# code llama budget sweep k2

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-budget-sweep-k2_20260521T212758_result.json`
- **Structured JSON:** [`9535866f12dcf02f7602.json`](../../sessions/95/9535866f12dcf02f7602.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Run complete (92s). Both outputs saved.

**Key results:**

| n_expert | Naive RMSE | Global RMSE | HB EC-HTE RMSE | HB/Naive |
|----------|-----------|-------------|----------------|----------|
| 100 | 0.1000 | 0.1456 | 0.1927 | 1.93 |
| 200 | 0.1000 | 0.1223 | 0.1557 | 1.56 |
| 500 | 0.1000 | 0.1070 | 0.1242 | 1.24 |
| **1000** | **0.1000** | **0.0952** | **0.0997** | **1.00** |
| 2000 | 0.1000 | 0.0908 | 0.0920 | 0.92 |

**Findings:**
- **RMSE crossover at n_expert=1000** — HB EC-HTE just barely beats Naive (ratio=0.998)
- **|Bias| is always lower for HB** (5-8x reduction over Naive at all budgets), but variance inflation dominates until n_expert≈1000
- **Global corrected dominates HB EC-HTE at every budget** — with Δπ=0.051, the per-subgroup CM heterogeneity is too small to justify the extra variance from stratified estimation
- Bias-variance decomposition confirms: Naive has Bias²=0.0082 (stable), HB trades this for Var that shrinks from 0.041→0.009 as n_expert grows

**Bottom line:** K=2 merging reduced Δπ from 0.137 (K=4) to 0.051, pushing the crossover from ~200 to ~1000. The global corrected estimator (single CM) is the best choice here since CM heterogeneity is negligible.

---
