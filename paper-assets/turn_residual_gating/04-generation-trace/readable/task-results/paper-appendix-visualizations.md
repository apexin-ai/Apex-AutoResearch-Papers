# paper appendix visualizations

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_visualizations_20260522T160647_result.json`
- **Structured JSON:** [`d3bece746c060050c59b.json`](../../sessions/d3/d3bece746c060050c59b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No label conflicts. All labels are unique across the paper.

Changes made:

1. **`main.tex:18`** — Added `{../artifacts/}` to `\graphicspath` so figures in `artifacts/` are found at compile time
2. **`artifacts/table_steering_full.tex:1`** — Changed `\section` → `\subsection` to nest under Appendix D instead of creating a separate Appendix E
3. **`appendix.tex:34-81`** — Added Appendix D "Additional Visualizations" with 5 `figure*` environments (heatmap, cross-model, AR GAR decay, gate distribution, loss curves) + `\input` for the steering table

The 5 figure PDFs (`fig_gate_profile_heatmap.pdf`, `fig_gate_profile_crossmodel.pdf`, `fig_ar_gar_perturn.pdf`, `fig_gate_distribution.pdf`, `fig_training_loss_curves.pdf`) need to exist in `artifacts/` at compile time — they're currently only on the remote server.

---
