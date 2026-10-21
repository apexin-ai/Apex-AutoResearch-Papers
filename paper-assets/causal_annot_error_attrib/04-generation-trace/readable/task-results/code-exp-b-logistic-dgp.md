# code exp b logistic dgp

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_b_logistic_dgp_20260522T112822_result.json`
- **Structured JSON:** [`49c3442c1178f7dcda95.json`](../../sessions/49/49c3442c1178f7dcda95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs generated. Key findings from the full run:

**Confounding** (τ = treatment effect):
- SF_τ = 0.000 for both linear and logistic — τ never flips, as predicted
- SF_any = 0.56-0.57 — driven by dummy variable attenuation, identical across models

**Exposure** (dummy coefs are treatment):
- SF_any = 0.57-0.58 — confirms sign flips persist under logistic DGP
- Linear ≈ Logistic (difference < 0.01) — qualitatively identical behavior

**IV**:
- SF_τ ≈ 0.07 for both 2SLS and CF — treatment effect rarely flips
- SF_any: 2SLS = 0.07, CF = 0.57 — CF's second-stage logistic has higher any-coef SF due to the residual term

**Critical result**: Linear and logistic DGPs produce virtually identical sign flip rates (|Δ| < 0.02 across all topologies), confirming the paper's linear-SEM findings are robust to nonlinearity.

Output files:
- `artifacts/exp_b_logistic_results.json` — full results
- `artifacts/exp_b_logistic_table.tex` — LaTeX table
- `artifacts/exp_b_logistic_dgp.py` — reproducible script

---
