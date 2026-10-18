# code mistral budget sweep

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral-budget-sweep_20260521T221037_result.json`
- **Structured JSON:** [`5e505887699c4cc2c917.json`](../../sessions/5e/5e505887699c4cc2c917.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 outputs generated successfully:

1. **`mistral_cm_profile.md`** — Per-subgroup FPR, FNR, π_s, κ for K=4 and K=2
2. **`mistral_budget_sweep_k4.csv`** — 8000 rows (4 subgroups × 2 z-levels × 4 methods × 5 budgets × 50 seeds)
3. **`mistral_budget_sweep_k2.csv`** — 4000 rows (2 subgroups × 2 z-levels × 4 methods × 5 budgets × 50 seeds)
4. **`mistral_sweep_analysis.md`** — Full analysis with all metrics

**Key findings:**

**K=4:**
- |Bias| crossover at n_expert=200 (EC-HTE beats Naive)
- RMSE crossover never reached — variance cost of 4 per-subgroup CMs is too high relative to Mistral's mild misclassification bias
- Coverage improves from 0.688→0.943 as budget grows

**K=2:**
- |Bias| crossover at n_expert=100 (immediately)
- RMSE crossover at n_expert=1000
- Fewer CMs to estimate → lower variance → K=2 dominates K=4 on both RMSE and |Bias| at every budget

Consistent with Mistral's balanced error profile: correction helps bias quickly, but with K=4 the variance penalty from estimating 4 CMs with limited expert labels keeps RMSE above Naive.

---
