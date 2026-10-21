# paper figure fig3 collapse dynamics

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig3_collapse_dynamics_20260518T023102_result.json`
- **Structured JSON:** [`14ecc6701655b635a3fc.json`](../../sessions/14/14ecc6701655b635a3fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure generated. All 4 subplots render correctly with v5 data:

- **(a)** CKA-only's 0.125 minimum annotated; collapse threshold at 0.85 with RASP crossing it
- **(b)** Standard's gradient collapse to 0.017 at step 60 annotated; RASP flat near zero throughout
- **(c)** CKA-only peak at 0.342 annotated; clear separation from other methods
- **(d)** KL divergence shows Random highest (~0.004), CKA-only stable low (~0.0015), RASP/Standard near-zero

Output files:
- PDF: `figures/paper/fig3_collapse_dynamics.pdf` (34 KB)
- PNG: `figures/paper/fig3_collapse_dynamics.png` (406 KB)
- Script: `figures/paper/gen_fig3_collapse_dynamics.py`

---
