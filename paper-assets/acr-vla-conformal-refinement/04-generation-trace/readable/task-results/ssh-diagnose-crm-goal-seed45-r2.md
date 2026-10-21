# ssh diagnose crm goal seed45 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-crm-goal-seed45-r2_20260520T000839_result.json`
- **Structured JSON:** [`975ecd3c30e20f00caa5.json`](../../sessions/97/975ecd3c30e20f00caa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。baseline JSON (`eval_goal_obs_only_norm02_seed45`) 未找到。

## eval-crm-goal-seed45-r2 结果

- **模式**: `crm_obs_only` / baseline_mode: `single` / benchmark: `goal`
- **Overall SR**: **0.65** (65/100 episodes, 每 task 10 rollouts × 10 tasks)

### Per-task breakdown

| Task | SR | Successes |
|---|---|---|
| turn_on_the_stove | **1.0** | 10/10 |
| put_the_bowl_on_the_plate | **1.0** | 10/10 |
| push_the_plate_to_the_front_of_the_stove | **0.9** | 9/10 |
| put_the_bowl_on_the_stove | **0.9** | 9/10 |
| put_the_bowl_on_top_of_the_cabinet | **0.8** | 8/10 |
| open_the_middle_drawer_of_the_cabinet | **0.7** | 7/10 |
| put_the_wine_bottle_on_top_of_the_cabinet | 0.4 | 4/10 |
| put_the_wine_bottle_on_the_rack | 0.4 | 4/10 |
| open_the_top_drawer_and_put_the_bowl_inside | 0.2 | 2/10 |
| put_the_cream_cheese_in_the_bowl | 0.2 | 2/10 |

弱项集中在精细放置类任务（wine bottle placement、cream cheese in bowl、drawer+place 组合），强项是简单 pick-place 和 push/turn 操作。

---
