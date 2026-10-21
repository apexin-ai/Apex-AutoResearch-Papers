# code gamma sensitivity rd2m5

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gamma-sensitivity-rd2m5_20260521T193704_result.json`
- **Structured JSON:** [`5ca51316c694cd78f941.json`](../../sessions/5c/5ca51316c694cd78f941.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs are complete. Summary:

**Deliverables:**
- `artifacts/gamma_sensitivity/run_gamma_sweep.py` — sweep script with MAP-EB (fast penalized EB incorporating Gamma prior)
- `artifacts/gamma_sensitivity/results.csv` — 1800 rows (15 configs x 20 seeds x 2 subgroups x 3 methods)
- `artifacts/gamma_sensitivity/analysis.md` — full analysis

**Key findings:**
- For reasonable priors (shape 1-5), RMSE varies by only **6.0%** across 12 configurations
- The full 17.3% range is inflated by Gamma(10,2) which has prior mean α₀=20 (extreme over-regularization)
- Gamma(3,1) default ranks 8/15, within 1.9% of best — solidly mid-pack
- Coverage is stable (0.925-0.938) across all configs
- 9/15 HB configs beat stratified MLE; global correction happens to do well here because K=2 pooling is safe

---
