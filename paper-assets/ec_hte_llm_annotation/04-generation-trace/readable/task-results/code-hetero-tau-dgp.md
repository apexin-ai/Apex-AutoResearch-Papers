# code hetero tau dgp

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hetero-tau-dgp_20260521T230410_result.json`
- **Structured JSON:** [`414d805e66317dbb72bd.json`](../../sessions/41/414d805e66317dbb72bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment complete. Key results:

**EC-HTE vs Global under heterogeneous-τ DGP:**

| n_expert | \|Bias\| Global | \|Bias\| EC-HTE | RMSE Global | RMSE EC-HTE |
|----------|----------------|-----------------|-------------|-------------|
| 200 | 0.0365 | **0.0248** | **0.1780** | 0.2606 |
| 500 | 0.0314 | **0.0099** | **0.1580** | 0.1760 |
| 1000 | 0.0286 | **0.0130** | **0.1554** | 0.1602 |

- **EC-HTE wins on |Bias| at all 3 budget levels** — the bias advantage is largest at n=500 (68% reduction vs Global).
- **Global still wins on RMSE** due to lower variance, but the gap shrinks rapidly: from 0.083 at n=200 to only 0.005 at n=1000. At n=1000, RMSE is nearly tied.
- **True_short (Δτ=0.6)** shows the biggest EC-HTE bias improvement: Global's |Bias|≈0.10 vs EC-HTE≈0.01 at n=500, matching the theoretical prediction that Global cannot handle subgroups with very different Δτ.
- The bias-variance decomposition confirms: EC-HTE has 10x lower Bias² than Global at n≥500, but higher variance at small budgets.

---
