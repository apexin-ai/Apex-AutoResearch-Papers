# code exp 003 phase a

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-003-phase-a_20260520T220635_result.json`
- **Structured JSON:** [`3f3ae52fee5e4a705e11.json`](../../sessions/3f/3f3ae52fee5e4a705e11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Completed in 31s. All 4 output files generated:

- `results/exp003_phase_a_raw.csv` — 24,000 rows (100 MC × 3 regimes × 4 n_expert × 5 levels × 4 methods)
- `results/exp003_phase_a.csv` — 240 aggregated rows (bias/RMSE/coverage)
- `results/exp003_dgp_spec.md` — DGP documentation
- `results/exp003_run.log` — run log

Key findings from the results:

1. **Naive** has clear bias on Z=1 across all regimes (~-0.05 at marginal), confirming misclassification attenuates CATE estimates.
2. **Global-corrected** reduces naive bias but introduces its own bias at subgroup level (especially S0/S1 where misclass differs from the global average).
3. **Stratified MLE** converges to near-oracle bias as n_expert increases (250+), but has high variance at small expert budgets (n_expert=50) — particularly in the small subgroups S2/S3 (hashtag subgroups, ~23% of data). This is the expected motivation for HB partial pooling in Phase B.
4. The **homogeneous** regime confirms that when misclass rates are equal, global correction works well and stratified has no bias advantage — only a variance penalty from smaller per-subgroup samples.

---
