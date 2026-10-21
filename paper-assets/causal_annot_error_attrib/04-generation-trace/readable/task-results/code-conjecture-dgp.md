# code conjecture dgp

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_conjecture_dgp_20260523T143200_result.json`
- **Structured JSON:** [`45a5c2cec213f684bde2.json`](../../sessions/45/45a5c2cec213f684bde2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The script exists, runs correctly, and has full results (10,000 C₀, 105 cells). Here's a summary of the findings:

**Results already generated.** All three artifacts exist:
- `artifacts/conjecture_dgp_sensitivity.py` — complete, uses analytic GH quadrature via `exp_d_conjecture_verify_v2`
- `artifacts/conjecture_dgp_sensitivity_results.json` — 105 cells, 1,050,000 total C₀ matrices, ran in ~187s
- `artifacts/conjecture_dgp_sensitivity_table.tex` — LaTeX table ready

**Key finding: `all_below_006 = false`**

Per-topology max ε_rel:

| Topology | max ε_rel | Status |
|----------|-----------|--------|
| confounding | 0.0230 | OK |
| collider | 0.0305 | OK |
| mbias | 0.0156 | OK |
| iv | 0.0000 | OK (exact, weak-IV filtered) |
| **frontdoor** | **0.0945** | **> 0.06** at β=5, σ²=2 |
| **exposure** | **0.2153** | **> 0.06** at β=1, σ²=2 |
| **mediation** | **0.9082** | **> 0.06** at β=5, σ²=2 |

The conjecture holds robustly for 4/7 topologies across all DGP parameters. Three topologies (mediation, exposure, frontdoor) breach the 0.06 relative bound at large β — where structural coefficients scale up while τ_true remains fixed (mediation τ=0.5, exposure τ=β[1]). The absolute violations for mediation at β=5 reach ε_abs=0.454.

Do you want me to:
1. Investigate whether the mediation/exposure violations are genuine or a scaling artifact (τ_true stays small while coefficients grow)?
2. Adjust the experiment (e.g., co-scale τ with β)?
3. Leave results as-is and update the paper to honestly report the DGP sensitivity?

---
