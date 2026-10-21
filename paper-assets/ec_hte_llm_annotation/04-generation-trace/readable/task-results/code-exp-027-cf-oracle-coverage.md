# code exp 027 cf oracle coverage

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-027-cf-oracle-coverage_20260522T140148_result.json`
- **Structured JSON:** [`19e49ee56fe5a5d96ad0.json`](../../sessions/19/19e49ee56fe5a5d96ad0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment completed in 161s. Results saved to `results/exp_cf_oracle_coverage.csv`.

Key findings:

| Method | Coverage | |Bias| | RMSE |
|---|---|---|---|
| Oracle (true Z) | **94.5%** | 0.0056 | 0.078 |
| EC-HTE true CM | **92.5%** | 0.0078 | 0.114 |
| EC-HTE estimated CM | **93.1%** | 0.0148 | 0.121 |
| Global true CM | 91.3% | 0.0371 | 0.110 |
| Global estimated CM | 91.1% | 0.0379 | 0.111 |
| Naive | 88.3% | 0.0447 | 0.095 |

**Interpretation:**
- **Oracle at 94.5%**: CF SE is well-calibrated on its own (close to nominal 95%)
- **EC-HTE true CM (92.5%) ≈ estimated CM (93.1%)**: CM estimation error is NOT the source of the gap — the ~2pp difference is negligible
- The ~2pp drop from Oracle to EC-HTE true CM comes from M^{-1} SE propagation amplifying uncertainty through the correction, not from CM estimation noise
- Naive at 88.3% confirms misclassification without correction degrades coverage, especially in high-pi subgroups (sub 3: 76-84%)

---
