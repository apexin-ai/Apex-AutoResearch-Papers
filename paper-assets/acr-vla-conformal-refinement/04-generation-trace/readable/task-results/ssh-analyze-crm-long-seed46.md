# ssh analyze crm long seed46

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_analyze-crm-long-seed46_20260520T001152_result.json`
- **Structured JSON:** [`6df6c02d7681890966a0.json`](../../sessions/6d/6df6c02d7681890966a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval-crm-long-seed46 结果

**Overall SR: 18.0%** (18/100 episodes)

### Per-task breakdown

| Task | SR | Succ/Total |
|------|----|------------|
| KITCHEN_SCENE3 — turn on stove, put moka pot | **90%** | 9/10 |
| KITCHEN_SCENE6 — mug in microwave, close it | **50%** | 5/10 |
| LIVING_ROOM_SCENE5 — white mug left plate, yellow mug right plate | **20%** | 2/10 |
| STUDY_SCENE1 — book in back compartment of caddy | **20%** | 2/10 |
| LIVING_ROOM_SCENE2 — alphabet soup + tomato sauce in basket | 0% | 0/10 |
| LIVING_ROOM_SCENE2 — cream cheese + butter in basket | 0% | 0/10 |
| KITCHEN_SCENE4 — black bowl in drawer, close it | 0% | 0/10 |
| LIVING_ROOM_SCENE6 — white mug on plate, pudding to right | 0% | 0/10 |
| LIVING_ROOM_SCENE1 — alphabet soup + cream cheese in basket | 0% | 0/10 |
| KITCHEN_SCENE8 — both moka pots on stove | 0% | 0/10 |

模式为 `crm_obs_only`，baseline `single`，每 task 10 rollouts。成功集中在 KITCHEN_SCENE3（90%）和 KITCHEN_SCENE6（50%），6 个 task 完全失败（均为多物体操作或需要开关抽屉/门的任务）。

---
