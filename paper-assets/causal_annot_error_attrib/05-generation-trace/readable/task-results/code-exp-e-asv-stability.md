# code exp e asv stability

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_e_asv_stability_20260522T112928_result.json`
- **Structured JSON:** [`b813442fd6462126cc77.json`](../../sessions/b8/b813442fd6462126cc77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs are in order. Here's a summary of the Exp-E results:

**Outputs produced:**
- `artifacts/exp_e_asv_stability.py` — self-contained script
- `artifacts/exp_e_asv_stability_results.json` — full results with per-C₀ detail
- `artifacts/exp_e_asv_stability_table.tex` — LaTeX table

**Key findings:**

| | Confounding | Exposure | IV |
|---|---|---|---|
| Alt. large β=[0,1.0,-0.5] | 0.348 | **0.090** | 0.203 |
| Same-sign β=[0,0.5,0.3] | ∞ | 0.223 | **0.203** |
| Alt. small β=[0,0.2,-0.1] | ∞ | **0.090** | 0.203 |

1. **Confounding is always most robust** — bias on τ from annotation error is small because T has independent variation (σ_T). For same-sign/small DGPs, the max OVB is <10% of τ, so the threshold is never reached.

2. **Ranking partially stable**: Exposure < IV < Confounding holds for alternating-sign β (2/3 configs). For same-sign β, IV and exposure swap because same-sign misclassification causes less bias.

3. **IV ASV is invariant to β** (0.203 for all DGPs) — the Wald estimator's relative bias depends only on the first-stage distortion C@FS, which cancels out the effect magnitude.

4. **Exposure alternating = exposure small** (0.090 for both) — the exposure plim is linear in β, so relative bias is scale-invariant. Only the sign structure matters.

5. **Sign-flip ASV is invariant** (≈2.223 for all DGPs) — occurs at the uniform confusion boundary where all coefficients hit zero. A universal property of symmetric C₀ matrices in the exposure model.

---
