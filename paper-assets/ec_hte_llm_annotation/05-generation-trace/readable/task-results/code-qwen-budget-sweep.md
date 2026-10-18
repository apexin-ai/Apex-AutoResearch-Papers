# code qwen budget sweep

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen-budget-sweep_20260521T215055_result.json`
- **Structured JSON:** [`ad423ce46a58f4a15570.json`](../../sessions/ad/ad423ce46a58f4a15570.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 outputs generated successfully:

1. **`qwen_cm_profile.md`** — Per-subgroup CM tables for K=4 and K=2, with Δπ and Proposition 2 checks
2. **`qwen_budget_sweep_k4.csv`** — 8000 rows (4 subgroups × 2 z_levels × 4 methods × 5 budgets × 50 seeds)
3. **`qwen_budget_sweep_k2.csv`** — 4000 rows (2 subgroups × 2 z_levels × 4 methods × 5 budgets × 50 seeds)
4. **`qwen_sweep_analysis.md`** — Full summary tables + crossover analysis

Key findings:

**K=4**: EC-HTE beats Naive on |Bias| at all budgets (crossover at n=100), but RMSE never crosses — high variance from estimating 4 separate CMs dominates. Δ_FPR=0.24, Δ_FNR=0.15 show substantial CM heterogeneity.

**K=2**: EC-HTE beats Naive on |Bias| at all budgets, **and RMSE crosses at n=1000** — fewer subgroups means less variance penalty. Δ_FPR=0.02, Δ_FNR=0.05 are smaller but still nonzero.

**K=4 vs K=2**: K=2 achieves lower |Bias| than K=4 across all budgets (e.g., 0.014 vs 0.070 at n=100) because fewer groups means more data per CM estimate. K=2 also achieves the RMSE crossover that K=4 cannot.

---
