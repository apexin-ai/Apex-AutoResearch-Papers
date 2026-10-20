# paper seed robustness 8seed update

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_seed-robustness-8seed-update_20260515T193336_result.json`
- **Structured JSON:** [`6028cadfc47380638af8.json`](../../sessions/60/6028cadfc47380638af8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits are complete. Summary of changes across `docs/paper/`:

| File | Change |
|------|--------|
| `abstract.tex` | 55.4±5.2% cross-split → 54.1±5.8% across 8 seeds |
| `experiments.tex` §4.3 | 55.4±5.2% → 54.1±5.8% across 8 seeds |
| `conclusion.tex` | 55.4±5.2% cross-split → 54.1±5.8% across 8 seeds |
| `discussion.tex` | 55.4±5.2% cross-split → 54.1±5.8% across 8 seeds |
| `main.tex` appendix | Table expanded from 4→8 cross-split rows (seeds 46-49 added); mean±std updated to 54.1±5.8 / 48.1±15.2; caption updated (10×→~12×, 5.2→5.8pp); seed 46 outlier paragraph added with range expansion [0.485,0.607]→[0.446,0.611] |

57.6% (single best seed, fixed split) is preserved unchanged throughout. Seed 46 outlier (44.63% bal acc, 23.33% int recall) is explicitly discussed as evidence that split selection drives router variance, not as a problem to fix.

---
