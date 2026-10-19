# ssh diagnose crm goal seed44 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-crm-goal-seed44-r2_20260519T232838_result.json`
- **Structured JSON:** [`4ca390b10f5b8ae8381f.json`](../../sessions/4c/4ca390b10f5b8ae8381f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功完成。结果如下：

**Overall SR: 0.64** (64/100 episodes, 10 tasks × 10 rollouts)

**Per-task breakdown:**

| Task | SR | Successes |
|------|----|-----------|
| turn_on_the_stove | **1.0** | 10/10 |
| put_the_bowl_on_the_plate | **1.0** | 10/10 |
| put_the_bowl_on_the_stove | **0.9** | 9/10 |
| push_the_plate_to_the_front_of_the_stove | **0.8** | 8/10 |
| put_the_bowl_on_top_of_the_cabinet | **0.7** | 7/10 |
| open_the_middle_drawer_of_the_cabinet | **0.6** | 6/10 |
| put_the_wine_bottle_on_top_of_the_cabinet | **0.5** | 5/10 |
| put_the_wine_bottle_on_the_rack | **0.4** | 4/10 |
| put_the_cream_cheese_in_the_bowl | **0.3** | 3/10 |
| open_the_top_drawer_and_put_the_bowl_inside | **0.2** | 2/10 |

配置: `mode=crm_obs_only`, `baseline_mode=single`, `benchmark=goal`, `n_rollouts=10`。

---
