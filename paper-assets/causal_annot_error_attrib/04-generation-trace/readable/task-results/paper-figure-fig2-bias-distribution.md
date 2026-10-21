# paper figure fig2 bias distribution

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig2_bias_distribution_20260520T152611_result.json`
- **Structured JSON:** [`8c9b0fd07829cf86ad18.json`](../../sessions/8c/8c9b0fd07829cf86ad18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 2 generated and registered (`art_20260520_4ceda6`).

**Summary of changes from previous version:**

1. **IV panel fixed**: Replaced the catastrophically unstable Wald estimator with naive OLS (`Y ~ 1 + D*₁ + D*₂`) in the endogenous DGP. The Wald blew up because `E[FS*₁] = 0` under Dirichlet(1,1,1) — the misclassification completely destroys the first stage. The OLS approach shows the compound effect of endogeneity + misclassification.

2. **Per-panel x-axis ranges**: Replaced `sharex=True` with per-panel ranges computed from the [0.5, 99.5] percentiles of each distribution. Confounding [1.0, 1.3] and M-bias [0.97, 1.04] are now readable instead of appearing as thin spikes.

3. **τ_true label positioning**: Uses blended transform (data-x, axes-y) at y=0.75, so the label is always visible regardless of density scale.

4. **Output**: PDF 98 KB, PNG 481 KB. All 6 panels non-empty with correct qualitative patterns.

---
