# viz paper figures v3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_paper-figures-v3_20260515T032514_result.json`
- **Structured JSON:** [`f13e495a14feaa50f454.json`](../../sessions/f1/f13e495a14feaa50f454.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 figures generated successfully (PDF + PNG each) at `/root/solver-trace-ablation/figures/`:

| File | PDF size | PNG size |
|------|----------|----------|
| `fig2_isr_collapse.pdf/.png` | 18 KB | 103 KB |
| `fig3_hacking_composition.pdf/.png` | 25 KB | 116 KB |
| `fig4_prolog_cross_logic.pdf/.png` | 23 KB | 117 KB |

Generator script: `/root/solver-trace-ablation/figures/gen_figs.py`

**Figure summaries:**
- **Fig 2** — Dual Y-axis: PR (blue, left) climbs 32→93→96%, ISR* (orange, right) drops 0.642→0.132→0.003; "Structural collapse" shaded between 500–1000 steps.
- **Fig 3** — 5-condition stacked bar (H1/H7/Genuine/Other %) with two annotations: ISR β=0.3 PR=18% callout, and arrow highlighting ISR β=0.1's unique H7-only pathway (64.5%).
- **Fig 4** — 2-panel scatter: left shows Prolog Exec-only ISR* (all <0.1, dashed reference line at 0.1); right shows Prolog STA Genuine=0% with per-seed gaming pathways (100% H7 / 97.4% H1 / 97.9% H7 functional).

Files ready for `register_artifact`.

---
