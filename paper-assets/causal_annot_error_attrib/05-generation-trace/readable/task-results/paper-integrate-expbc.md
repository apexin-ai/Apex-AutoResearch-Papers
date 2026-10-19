# paper integrate expbc

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_integrate_expbc_20260522T115404_result.json`
- **Structured JSON:** [`1257673604105a8c6ec8.json`](../../sessions/12/1257673604105a8c6ec8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Compilation: 0 errors, 0 undefined references, 20 pages total. Main text ends on page 8, Limitations starts on page 9.

Summary of changes:
- **appendix_proofs.tex**: Added two subsections before Notation:
  - `\subsection{Robustness to Nonlinear DGP}` (`\ref{sec:logistic_dgp}`) — 3-row summary table showing SF_τ differences < 0.01 between linear and logistic DGPs across confounding/exposure/IV, with the IV SF_any dimensionality note
  - `\subsection{Bootstrap Uncertainty of ASV}` (`\ref{sec:bootstrap_asv}`) — 3-row table with point estimates and 95% CIs, plus the bootstrap figure
- **experiments.tex**: Added two reference sentences:
  - After N-sensitivity paragraph (Section 4.3): bootstrap CI sentence for exposure/IV ASV
  - After empirical validation overlay paragraph (Section 4.4): logistic DGP robustness sentence
- **Figures**: Copied `exp_c_bootstrap_figure.pdf` to both `docs/paper/` and `figures/paper/`

---
