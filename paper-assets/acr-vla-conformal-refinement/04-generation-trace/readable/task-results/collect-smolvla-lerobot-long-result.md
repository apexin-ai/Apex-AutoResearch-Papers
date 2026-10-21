# collect smolvla lerobot long result

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_smolvla-lerobot-long-result_20260522T135122_result.json`
- **Structured JSON:** [`72a13a638875d9591355.json`](../../sessions/72/72a13a638875d9591355.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 seeds completed. Here are the SmolVLA baseline (vla_only) Long suite results:

## SmolVLA Long Suite — vla_only baseline

**Overall SR: 15.7%** (avg across 3 seeds: 16.0%, 16.0%, 15.0%)

### Per-task breakdown (averaged over 3 seeds, 30 rollouts each):

| Task | s49 | s50 | s51 | Avg SR |
|------|-----|-----|-----|--------|
| LIVING_ROOM_SCENE2 (soup + sauce → basket) | 0/10 | 0/10 | 0/10 | **0.0%** |
| LIVING_ROOM_SCENE2 (cheese + butter → basket) | 0/10 | 0/10 | 0/10 | **0.0%** |
| KITCHEN_SCENE3 (stove on + moka pot) | 9/10 | 8/10 | 9/10 | **86.7%** |
| KITCHEN_SCENE4 (bowl → drawer, close) | 0/10 | 0/10 | 0/10 | **0.0%** |
| LIVING_ROOM_SCENE5 (white mug left, yellow mug right) | 3/10 | 3/10 | 2/10 | **26.7%** |
| STUDY_SCENE1 (book → caddy back) | 1/10 | 2/10 | 1/10 | **13.3%** |
| LIVING_ROOM_SCENE6 (mug on plate + pudding right) | 2/10 | 1/10 | 1/10 | **13.3%** |
| LIVING_ROOM_SCENE1 (soup + cheese → basket) | 0/10 | 0/10 | 0/10 | **0.0%** |
| KITCHEN_SCENE8 (both moka pots → stove) | 0/10 | 0/10 | 0/10 | **0.0%** |
| KITCHEN_SCENE6 (mug → microwave, close) | 1/10 | 2/10 | 2/10 | **16.7%** |

### 4-suite summary so far:

| Suite | SR |
|-------|-----|
| Object | 66.5% |
| Spatial | 59.5% |
| Goal | 75.5% |
| **Long** | **15.7%** |

Long suite is dramatically harder — 5/10 tasks at 0%, only KITCHEN_SCENE3 (stove+moka) is reliably solved. The multi-step sequential manipulation tasks (put both X and Y somewhere) consistently fail.

---
