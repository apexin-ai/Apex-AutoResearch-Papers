# code mvp simulation v2

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_simulation_v2_20260520T183830_result.json`
- **Structured JSON:** [`cbd5de26b5072efb2982.json`](../../sessions/cb/cbd5de26b5072efb2982.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Key results from the N_MC=100 run:

**Extreme regime** (misclass 0.25 vs 0.05, τ gap = 0.4):
- **Naive** has large bias: +0.053 (z0), -0.063 (z1), coverage drops to 79%/70%
- **Global-corrected** substantially corrects: bias near 0, coverage ~88-94%
- **EC-HTE** also corrects well, with coverage improving as n_expert grows (82%→93%)
- **Oracle** baseline: ~94% coverage

**v1 bug is fixed**: Global and Naive are now clearly different (v1 had Global ≈ Naive with <0.001 difference).

**Moderate/Homogeneous**: Corrections work but the naive bias is smaller to begin with, so the gap is narrower. In homogeneous regime, all methods perform similarly — as expected when misclassification is uniform.

Results saved to `results/mvp_results_v2.csv` (summary) and `results/mvp_results_v2_raw.csv` (per-run).

---
