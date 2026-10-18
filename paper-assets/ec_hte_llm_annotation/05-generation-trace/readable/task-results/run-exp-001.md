# run exp 001

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp-001_20260520T202832_result.json`
- **Structured JSON:** [`2324625e3a48aa29780b.json`](../../sessions/23/2324625e3a48aa29780b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### Complete Summary

**Run**: 3600 MC runs, 36 cells, 69 min, 0 errors, Gibbs sampler (median 0.86s/fit)

**MCMC Diagnostics**:
- R-hat max: 1.024 (a few small-sample cells slightly above 1.01)
- ESS min: 129 (worst case; bulk of runs well above 200)
- Divergent: 0

**HB vs MLE RMSE** — HB consistently beats MLE, but gains are modest:
- K=2: +1–9% at n=50, <1% at n≥250
- K=4: +6–9% at n=50 (moderate/homogeneous), +1–3% at n=100, <1% at n≥500
- K=4 extreme at n=50/100: both MLE and HB blow up (too few labels per subgroup for stable matrix inversion)

**HB Coverage** — all ≥ 0.90:
- z0 coverage: 0.91–0.99 across all configs
- z1 coverage: 0.91–0.96
- Lowest: K=4 extreme n=50 (z1=0.907) — borderline but passes

**K=4 vs K=2**: K=4 shows larger RMSE everywhere (more subgroups = fewer expert labels each), bigger HB advantage at small n_expert, and more fragility in the extreme regime at low budgets.

**Output files**:
- `results/exp001_hb_results.csv` — 540 rows (36 cells × 5 methods × 3 subgroup-averaged entries)
- `results/exp001_hb_diagnostics.csv` — 3600 rows

---
