# exp fwl logistic w4

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_fwl_logistic_w4_20260522T172212_result.json`
- **Structured JSON:** [`ff96a7d48ebf5560a711.json`](../../sessions/ff/ff96a7d48ebf5560a711.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both the experiment script and paper content already exist and are complete. Let me verify the results are consistent between the JSON and the paper table.

The paper already contains:

1. **`experiments.tex` (line 96)**: The FWL paragraph includes the logistic regression sentence: "This invariance is specific to OLS; under logistic regression the column-space argument no longer applies, but the empirical breakdown is small (mean bias reduction |·| < 0.1% across six VAST confusion matrices), so matrix-based corrections remain effectively useless (Appendix~\ref{sec:fwl_logistic})."

2. **`appendix_proofs.tex` (lines 898-925)**: Full `\paragraph{FWL breakdown under logistic regression.}` with:
   - Explanation of why FWL fails under logistic (implicit σ' weighting depends on actual column values, not just span)
   - Table with all 6 VAST CMs showing OLS |Δ|_max ≈ 10⁻¹⁵ vs logistic |Δ|_max ≈ 10⁻³
   - Mean bias reduction: OLS = 0.0%, Logistic = -0.04%
   - Two-finding summary paragraph

3. **`artifacts/exp_fwl_logistic_breakdown.py`**: The experiment script (312 lines) with results in `exp_fwl_logistic_results.json`.

Everything matches the task requirements and the JSON results. The experiment, paper edits, and appendix are all already done. No changes needed.

---
