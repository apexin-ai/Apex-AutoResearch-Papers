# fix figure3 legend caption

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_figure3_legend_caption_20260519T135158_result.json`
- **Structured JSON:** [`60c5f932c96fb8731201.json`](../../sessions/60/60c5f932c96fb8731201.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure is included on page 15. Everything compiles correctly.

## Summary

**Red line (red, #FF5722, square markers, solid) = `full_trace` condition**

Data source: `qwen7b_full_trace_dynamics_seed42/dynamics_log.jsonl` — this is definitively **full_trace** data, NOT label_only. Final accuracy in dynamics: ~88.2% (consistent with full_trace behavior; the 81.76% in the paper table is from the final 3-epoch model, not the dynamics checkpoints).

**What was fixed:**
- The training_dynamics figure was **not included** in the paper LaTeX. The figure existed as a PDF but had no `\begin{figure}` block or caption in any .tex file.
- Added a `figure*` environment in `appendix.tex` (line 243) within the "Training Dynamics and Loss Decoupling" section (`\label{sec:training_dynamics}`) with a **correct caption** describing:
  - `exception_only` = blue, circles
  - `full_trace` = red, squares (solid in Accuracy/Loss panels, dashed only for fail-F1 in the per-class panel)
  - No mention of "label-only loss" (which is a different condition at 86.22%)
- The plot code legend ("Full-trace") was already correct — no changes needed to `plot_dynamics.py`

**Regenerated PDF path:** `/root/trace-verdict-study/figures/paper/training_dynamics.pdf` (also copied to `docs/paper/figures/`)

**Compiled paper:** `/root/trace-verdict-study/docs/paper/main.pdf` (20 pages, figure on page 15)

---
