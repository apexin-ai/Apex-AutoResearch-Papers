# code p0a fl table1

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p0a-fl-table1_20260523T135821_result.json`
- **Structured JSON:** [`ad2953286bbbca4bd2fc.json`](../../sessions/ad/ad2953286bbbca4bd2fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No LaTeX errors (only pre-existing undefined reference warnings from appendix cross-refs that resolve on second pass).

Here's a summary of everything completed:

**Part 1 — F-L Metrics** (computed via `compute_fl_for_table1.py`, same DGP as Table 1):
| Method | |Bias| | RMSE | Coverage |
|--------|--------|------|----------|
| F-L Scalar | 0.122 | 0.159 | 0.68 |
| F-L Per-sub. | 0.168 | 0.220 | 0.65 |

Both are worse than naive (0.058, 0.090, 0.82) — the scalar correction cannot handle heterogeneous error rates.

**Part 2 — Table 1** (`experiments.tex:50-56`): Added F-L Scalar and F-L Per-sub rows, updated `multirow{4}` to `multirow{6}`.

**Part 2 — Section 5.3 text** (`experiments.tex:31`): Added F-L comparison sentence noting bias 0.122/0.168 and coverage 0.68/0.65.

**Part 3 — theory.tex** (`theory.tex:50-53`): Added "Relationship to classical scalar attenuation" paragraph covering all 4 required points (F-L bias formula, structurally distinct quantity, over/under-correction mechanism, singularity divergence).

**Part 3 — Sign-reversal sentence** (`theory.tex:104`): Added after Proposition 3 interpretation.

**Part 4 — Proposition 3 format**: Already had an itemize structure separating high-error and low-error cases (pre-existing).

**Page count**: Conclusion is on page 9, but this was **pre-existing** before my edits (confirmed via the pre-edit page images at `_pdf_images/main_p9.png`). My additions (~8 rendered lines) did not cause the overflow.

---
