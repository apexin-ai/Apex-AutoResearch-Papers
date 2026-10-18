# paper appendix wording fix

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix-wording-fix_20260523T014745_result.json`
- **Structured JSON:** [`8566bc7d3b67658af890.json`](../../sessions/85/8566bc7d3b67658af890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes complete. Summary of edits across 3 files:

---

**`appendix.tex` (lines 45–50)** — Rewrote `\subsection{Oracle Adversary Limitations}` → `\subsection{Metric Robustness Under Partial Panel Information}`:
- Removed all adversary-capability framing ("attacker cannot optimally select", "partial-knowledge attacker can exploit", "effect attenuates")
- Replaced with metric-robustness framing: η_max recomputed from 2/3 known judges via leave-one-out masking
- Reports actual results: partial + clustered SE gives η_max 12/12 (stronger than oracle 8/12), K_eff 0/12, β_std = 0.589
- Explains mechanism: averaging over masking scenarios smooths estimation noise

**`methodology.tex` (after line 2)** — Inserted `figure*` environment:
- Full-width framework overview figure (`fig_framework.pdf`)
- Caption references corrected to actual labels: `sec:experiments`, `sec:threat_model`, `sec:aggregation`
- Label: `fig:framework`

**`main.tex` (Limitations, line 40)** — Updated future-work sentence:
- Old: "Future directions also include partial-knowledge adversary models and bootstrapped GAM confidence intervals."
- New: "A partial-information analysis (Appendix~\ref{app:oracle}) shows that η_max computed from incomplete panel knowledge retains full predictive power; future directions include bootstrapped GAM confidence intervals and causal identification via training-time diversity control."

---
