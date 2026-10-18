# code gemma budget sweep

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma-budget-sweep_20260521T221030_result.json`
- **Structured JSON:** [`dc1ee9cab5c3cdc8b517.json`](../../sessions/dc/dc1ee9cab5c3cdc8b517.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 outputs generated successfully:

| File | Status |
|------|--------|
| `gemma_cm_profile.md` | Gemma Accuracy=0.764, FPR=0.098, FNR=0.310, Δπ=0.212, strong FNR>FPR asymmetry confirmed |
| `gemma_budget_sweep_k4.csv` | 8000 rows (5 budgets × 50 seeds × 4 subgroups × 2 z-levels × 4 methods) |
| `gemma_budget_sweep_k2.csv` | 4000 rows (5 budgets × 50 seeds × 2 subgroups × 2 z-levels × 4 methods) |
| `gemma_sweep_analysis.md` | Full analysis with summary tables, crossover, bias-variance decomposition, K4 vs K2 comparison |

Key findings:

**CM Profile:** Max κ=2.21 (K=4), only 1/4 subgroups with κ>2 (vs. task's claimed 4/4 — the "known" Gemma stats appear to be from a different binarization or dataset version). The `False_medium` subgroup has the worst FNR (0.437).

**K=4:** |Bias| crossover at n_expert=200, RMSE crossover never reached (variance cost of 4-way stratification is high at small budgets — K=4 with only 490 eligible observations means thin cells).

**K=2:** |Bias| crossover at n_expert=100, RMSE crossover at n_expert=1000. K=2 dominates K=4 across all budgets — fewer subgroups = less variance, and Gemma's CM heterogeneity between hashtag groups is substantial enough that K=2 still captures the important variation.

---
