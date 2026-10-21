# code exp a stress test

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_a_stress_test_20260522T110940_result.json`
- **Structured JSON:** [`bbaf115632f64bb06811.json`](../../sessions/bb/bbaf115632f64bb06811.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 outputs generated successfully. Here's the results summary:

**96 configs** (4 topologies × 2 K × 3 CM qualities × 4 ε), each with 100 MC reps at N=10,000. Completed in 58s.

**Key findings:**

| | ε=0 (non-diff) | ε=0.01 | ε=0.05 | ε=0.10 |
|---|---|---|---|---|
| Mean SF rate | 0.000 | 0.000 | 0.001 | 0.005 |
| Max SF rate | 0.000 | 0.000 | 0.020 | 0.070 |
| Mean BR | 1.72 | 1.72 | 2.13 | 3.38 |

**By topology:**
- **Confounding**: No sign flips at any ε. BR ≈ 1.10–1.15 (mild amplification due to residual confounding from misclassified confounder). Stable across ε.
- **Mediation**: No sign flips. BR ≈ 1.15–1.61 (indirect effect leakage). Increases moderately with ε.
- **Exposure**: Sign flips appear at ε≥0.05 for K=3 low-quality CM (SF=5% at ε=0.10). BR < 1 (attenuation toward null), decreasing with ε.
- **IV**: Most sensitive. Sign flips at ε=0.10 for K=3 low-quality (SF=7%). Extreme BR for low-quality CMs (up to 44× for K=3) due to weak first-stage amplification in the Wald estimator.

**Verification:**
- ε=0: zero sign flips across all configs (consistent with non-differential theory for symmetric CMs)
- Sign flips monotonically increase with ε
- All CMs validated as column-stochastic

**Output files:**
- `artifacts/exp_a_stress_test_results.json` — full results with per-config metrics
- `artifacts/exp_a_stress_test_table.tex` — LaTeX table for Appendix B.3
- `artifacts/exp_a_stress_test.py` — reproducible script

---
