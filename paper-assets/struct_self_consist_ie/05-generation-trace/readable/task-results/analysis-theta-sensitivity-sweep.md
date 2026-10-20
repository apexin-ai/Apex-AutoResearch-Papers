# analysis theta sensitivity sweep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_theta_sensitivity_sweep_20260519T053845_result.json`
- **Structured JSON:** [`e63595d139aae7ed667c.json`](../../sessions/e6/e63595d139aae7ed667c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Summary:

**θ sweep data** (from `fair_results.json`, all datasets, N=8):

| Dataset | Best θ (LP-w) | Best Δ LP-w | θ=0.25 Δ LP-w |
|---------|--------------|-------------|----------------|
| SciERC  | 0.30/0.35    | +1.71 pp    | +1.67 pp       |
| Few-NERD| 0.25         | +0.88 pp    | +0.88 pp       |
| CoNLL   | 0.30         | -0.39 pp    | -0.71 pp       |

Key pattern: θ ∈ [0.15, 0.35] is a stable plateau on all datasets. Below 0.10, spurious entities crash F1 (up to -7 pp on Few-NERD). Above 0.40, over-filtering degrades recall.

**Files modified:**
- `appendix.tex:1526–1577` — new `\subsection{Entity Construction Threshold Sensitivity}` with `\label{app:theta_sweep}` and Table~\ref{tab:theta_sweep}
- `experiments.tex:188` — replaced the tuning-free sentence with θ robustness claim referencing Appendix~\ref{app:theta_sweep}

---
