# run exp 001 hyperprior

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp-001-hyperprior_20260520T225155_result.json`
- **Structured JSON:** [`fcd9bc4e854c26a0d6ce.json`](../../sessions/fc/fcd9bc4e854c26a0d6ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment completed successfully — 600 runs in 3741s (~62 minutes). Results saved to `results/exp001_hyperprior_sensitivity.csv`.

### Key finding: HB is robust to hyperprior scale

**K=2 (n=250, averaged over subgroups):**

| Scale | HB RMSE_z0 | HB RMSE_z1 | HB Cov_z0 | HB Cov_z1 | MLE RMSE_z0 (ref) |
|-------|-----------|-----------|----------|----------|------------------|
| 0.5   | 0.0734    | 0.0770    | 0.985    | 0.950    | 0.0732           |
| 1.0   | 0.0730    | 0.0767    | 0.985    | 0.950    | 0.0732           |
| 2.0   | 0.0727    | 0.0764    | 0.985    | 0.950    | 0.0732           |

**K=4 (n=100, averaged over subgroups):**

| Scale | HB RMSE_z0 | HB RMSE_z1 | HB Cov_z0 | HB Cov_z1 | MLE RMSE_z0 (ref) |
|-------|-----------|-----------|----------|----------|------------------|
| 0.5   | 0.1185    | 0.1265    | 0.973    | 0.930    | 0.1190           |
| 1.0   | 0.1154    | 0.1235    | 0.972    | 0.928    | 0.1190           |
| 2.0   | 0.1131    | 0.1212    | 0.972    | 0.930    | 0.1190           |

### Summary

- **RMSE variation across scale 0.5-2.0 is <1% for K=2 and ~4-5% for K=4** — well within the <10% threshold.
- **Coverage is essentially invariant** to hyperprior scale in both configs.
- Wider prior (scale=2.0) gives slightly lower RMSE, consistent with less shrinkage when data is informative.
- HB and MLE perform nearly identically for K=2 (large n), while HB slightly outperforms MLE for K=4 (small n) — the shrinkage helps.
- The Gibbs sampler is robust to hyperprior specification across a 4x range of prior variance.

---
