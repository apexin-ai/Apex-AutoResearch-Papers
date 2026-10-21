# code exp 014 asymmetric

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-014-asymmetric_20260521T072959_result.json`
- **Structured JSON:** [`370c865f5a3e23efb88e.json`](../../sessions/37/370c865f5a3e23efb88e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs verified. Here's the summary:

**exp-014 Asymmetric Misclassification — Complete**

Results:
- **R² = 0.992** (analytic vs MC bias) — formula verified
- **Product structure CV ≈ 10⁻¹⁶** — bias(z,s) = Δτ · [B_s]_{z,1} holds exactly, regardless of symmetry
- **EC-HTE dominates** across all 3 configs:

| Method | |Bias| | RMSE | Coverage |
|--------|-------|------|----------|
| naive | 0.047 | 0.053 | 0.48 |
| global_est | 0.025 | 0.040 | 0.78 |
| echte | 0.006 | 0.033 | 0.90 |

EC-HTE reduces bias ~7x vs naive, ~4x vs global. Config 2 (co-directional asymmetry) is where global performs worst (|bias| = 0.037 vs echte 0.007).

Output files:
- `exp014_asymmetric.py` — experiment script
- `results/exp014_asymmetric_bias.csv` — analytic vs MC bias (60 rows)
- `results/exp014_asymmetric_correction.csv` — method comparison (180 rows)
- `results/exp014_asymmetric_analysis.md` — full analysis with LaTeX derivation

---
