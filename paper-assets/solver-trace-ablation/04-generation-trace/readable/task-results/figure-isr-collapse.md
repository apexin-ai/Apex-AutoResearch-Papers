# figure isr collapse

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_isr-collapse_20260515T202713_result.json`
- **Structured JSON:** [`db7fb6da26f566017cff.json`](../../sessions/db/db7fb6da26f566017cff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure looks clean and publication-ready. The key narrative is clear:

- **ISR β=0.1** (orange): ISR rises sharply to ~0.9+ (Goodhart collapse), reproducible across seeds
- **Exec-only** (blue): moderate ISR increase to ~0.5 (natural growth from better formalizations)  
- **Random β=0.1** (sky blue): ISR stays flat at ~0.05-0.1 (no ISR gaming)

Output:
- PDF: `paper/figures/fig2_isr_collapse.pdf`
- PNG: `paper/figures/fig2_isr_collapse.png`
- Script: `paper/figures/gen_fig2.py` (loads from `fig2_data.json`, self-contained locally)

---
