# figure probe trajectory

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_probe_trajectory_20260519T070720_result.json`
- **Structured JSON:** [`ad3f9ee03058e10c2e25.json`](../../sessions/ad/ad3f9ee03058e10c2e25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 outputs are in place:

| Output | Path | Size |
|--------|------|------|
| PDF | `docs/paper/figures/fig_trajectory.pdf` | 24KB |
| PNG | `docs/paper/figures/fig_trajectory.png` | 424KB |
| Data JSON | `artifacts/fig_trajectory_data.json` | 75KB |
| Caption | `artifacts/fig_trajectory_caption.txt` | 425B |

**Narrative verification** (first step where mean HS > 0.5 vs text > 0.5, near CP):

| Model | HS crosses 0.5 | Text crosses 0.5 | HS earlier? |
|-------|----------------|-------------------|-------------|
| R1-8B | step 0 | step 1 | Yes |
| OT-7B | step 0 | step 0 | Tie (HS lower pre-CP baseline) |
| R1-32B | step -2 | step -4 (noisy, n=18) | HS sharper jump (0.41→0.70 vs 0.48→0.54) |
| QwQ-32B | step 0 | step 2 | Yes |

The figure honestly shows the data. The core story holds: HS probes exhibit a sharper, more discriminative transition at CP than text probes across all 4 models, with lower pre-CP false-positive baseline. The "earlier detection" framing applies cleanly to R1-8B and QwQ-32B; for R1-32B and OT-7B the advantage is better characterized as "sharper contrast between pre and post-CP regions."

---
