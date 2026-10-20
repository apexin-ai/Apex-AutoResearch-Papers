# paper figure fig1 framework

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1_framework_20260518T024533_result.json`
- **Structured JSON:** [`987f953231b6ad023579.json`](../../sessions/98/987f953231b6ad023579.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure generated and registered. Output files:

- **PDF**: `artifacts/figures/fig1_framework.pdf` (58 KB)
- **PNG**: `artifacts/figures/fig1_framework.png` (349 KB)
- **Script**: `artifacts/figures/gen_fig1_framework.py`

The figure shows the 3-row pipeline: Pretrained LLM → Structural Analysis (Taylor I(h) + CKA F(h)) → 4 scoring criteria (color-coded with Okabe-Ito scheme) → identical SFT+GRPO recovery → divergent outcomes from Active Learning (green, reward 0.342) to Immediate Collapse (red-orange, reward ~0.01). A horizontal gradient bar at the bottom reinforces the recovery capacity spectrum. Standard and RASP boxes carry warning markers highlighting their reliance on gradient importance I(h).

---
