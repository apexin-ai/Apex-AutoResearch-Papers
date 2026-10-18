# code exp 007 ppci fix

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-007-ppci-fix_20260520T221446_result.json`
- **Structured JSON:** [`4bfde0f8c59fbaa109da.json`](../../sessions/4b/4bfde0f8c59fbaa109da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All validations pass. Summary of changes to `exp007_ppci_dsl.py`:

1. **Renamed `method_ppci` → `method_mi_rubin`** — the old MI + Rubin's rules implementation, now correctly labeled
2. **New `method_ppci`** — true PPI rectifier that uses Y_true + true Z on the gold subset to compute a bias correction term (rectifier = tau_gold - tau_hat_gold)
3. **Treatment-differential outcome error DGP** — `Y_obs = Y_true + bias_s * T + noise` instead of mean-zero noise; `OUTCOME_BIAS` config per regime/subgroup
4. **4 DGP matrix** — A (covariate only), B (outcome only), C (both), D (no error); `dgp` column in output CSV
5. **`method_ec_hte_ppci`** — applies M^{-1} covariate correction first, then PPI rectifier for residual outcome error
6. **`generate_data` restructured** — `has_covariate_error`/`has_outcome_error` flags control error injection; outcome noise only applied when `has_outcome_error=True`

---
