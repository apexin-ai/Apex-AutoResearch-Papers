# code exp 026 low budget hb v2

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-026-low-budget-hb-v2_20260522T132122_result.json`
- **Structured JSON:** [`17eb8fa31cc1654d9aaa.json`](../../sessions/17/17eb8fa31cc1654d9aaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Script completed in ~3.5 minutes, 0 errors, 360 rows output.

**Key findings:**

- **K=2**: HB shows clear advantage at n_expert=50 (+16.1% RMSE reduction). At n_expert=25 HB is slightly worse (-4.9%), likely because even Gibbs can't overcome extreme data scarcity with only ~6 labels per subgroup-cell. At n_expert≥75, both converge.

- **K=4**: HB underperforms MLE at very low budgets (n_expert=25,50) — with 4 subgroups the per-cell counts are ~3-6, causing even Gibbs posteriors to be dominated by the prior. At n_expert≥75, HB consistently beats MLE (+1-4% RMSE), confirming the shrinkage benefit in the moderate-data regime.

- **Coverage**: Both methods maintain ≥0.88 across the board. No catastrophic blowups (MLE RMSE stays under 1.0).

- **Notable**: At very low budgets, `global_corrected` (pooled CM) actually outperforms both MLE and HB, suggesting that when per-subgroup data is near-zero, pooling all subgroups is the better strategy.

---
