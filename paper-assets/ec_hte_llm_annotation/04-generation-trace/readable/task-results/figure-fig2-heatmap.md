# figure fig2 heatmap

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig2-heatmap_20260521T052638_result.json`
- **Structured JSON:** [`36705f943e09449184eb.json`](../../sessions/36/36705f943e09449184eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure is clean and paper-ready.

**Output**: `artifacts/figures/fig2_heatmap.pdf` + `.png`

Key visual elements:
- **(a)** Subgroup A stays entirely blue (ratio < 1) — global debiasing always helps the low-error subgroup
- **(b)** Subgroup B crosses ratio=1 at Δπ ≈ 0.12, with hatching marking where debiasing actively hurts; the ratio escalates rapidly to 5+ at high Δπ
- Dashed contour at ratio=1.0 with label, diverging RdBu_r colormap centered at 1.0, shared colorbar

---
