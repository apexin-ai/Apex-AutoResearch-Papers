# paper r29 group3 appendix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r29-group3-appendix_20260522T144647_result.json`
- **Structured JSON:** [`1f14a6950fae2686f1a1.json`](../../sessions/1f/1f14a6950fae2686f1a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Line 827 is the last line. No `\clearpage` or `\newpage` at the end — nothing to fix for task O.

---

**Summary of changes:**

### D. N=2 Sensitivity Analysis — `appendix.tex:758–779` (new)
- Inserted `\subsection{$N{=}2$ Sensitivity Analysis (Excluding Seed 43)}` with `\label{app:n2-sensitivity}` between seed-convergence (E.5) and 8B results (E.7)
- Table `tab:n2-sensitivity` with 3 rows computed from per-seed data in `tab:fol-detailed`:
  - Exec-only 500: PR=95.5±3.5, ISR*=0.357±0.318, N-H=3.8±5.3
  - Exec-only 1000: PR=98.0±2.8, ISR*=0.003±0.001, N-H=0.0±0.0
  - ISR β=0.1 500: PR=85.0±5.7, ISR*=0.659±0.344, N-H=8.7±12.2
- Text notes TS dominance in both seeds (s42: 16%, s44: 100%) and that ISR* variance reflects mode difference (CE vs TS), not data quality

### Cross-reference fix — `experiments.tex:18`
Already pointed to `app:n2-sensitivity` (was updated prior to this session or by a concurrent edit).

### F. TS Recall Lower Bound — `appendix.tex:231–232` (new)
- Added after Classifier Validation paragraph: TSb bounds TS recall at ≥91% (149/163); other modes not estimable; non-hacking rates are upper bounds.
- Denominator 163 = TSa(149) + TSb(14, including 12 from s44 + 2 from s43)

### O. Last-page whitespace
No `\clearpage`/`\newpage` at end of appendix.tex. File ends with substantive 8B-results text (line 827). No action needed.

---
