# paper fix figure2 overlap

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_figure2_overlap_20260522T101657_result.json`
- **Structured JSON:** [`0bd8f272d4d8edf736aa.json`](../../sessions/0b/0bd8f272d4d8edf736aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

23 pages total (8 main text + appendix). Page count unchanged from the original. 

**Summary:**

**Root cause:** `figsize=(7, 4.2)` — the figure was designed at 7 inches wide but rendered at `\columnwidth` (~3.31 inches), causing ~53% horizontal compression. X-tick labels, legends, and markers all became cramped.

**Fix** (in `scripts/plot_fig2_merged.py`):
- `figsize` → `(3.4, 2.8)`: designed at column width so it renders at ~1:1 scale
- `font.size` 10 → 8, axis labels 10.5 → 8.5, reference text 8 → 6.5
- Line widths 1.6/1.4 → 1.2/1.0, marker sizes 4.5/4 → 3.5/3
- Legend fonts 7.5 → 6 with tighter padding (`labelspacing=0.25`, `handletextpad=0.4`)
- `xlim` left edge −0.25 → −0.4 for more left padding
- Replaced `constrained_layout=True` with `fig.tight_layout(pad=0.4)`

No data changes. Page count unchanged.

---
