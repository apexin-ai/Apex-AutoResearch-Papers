# analyze eval goal vla only wrapper s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-goal-vla-only-wrapper-s42_20260523T100549_result.json`
- **Structured JSON:** [`3dc38e543ffc1cf60c7d.json`](../../sessions/3d/3dc38e543ffc1cf60c7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。结果：

**Overall: 83.5% (167/200)**

| Task | Success Rate | Successes/Rollouts |
|------|-------------|-------------------|
| open_the_middle_drawer_of_the_cabinet | 85.0% | 17/20 |
| put_the_bowl_on_the_stove | 100.0% | 20/20 |
| put_the_wine_bottle_on_top_of_the_cabinet | 90.0% | 18/20 |
| open_the_top_drawer_and_put_the_bowl_inside | 75.0% | 15/20 |
| put_the_bowl_on_top_of_the_cabinet | 80.0% | 16/20 |
| push_the_plate_to_the_front_of_the_stove | 85.0% | 17/20 |
| put_the_cream_cheese_in_the_bowl | 40.0% | 8/20 |
| turn_on_the_stove | 100.0% | 20/20 |
| put_the_bowl_on_the_plate | 95.0% | 19/20 |
| put_the_wine_bottle_on_the_rack | 85.0% | 17/20 |

与之前确认的 Goal VLA-only 结果一致：**83.5%**。Wrapper pipeline 没有引入偏差。`put_the_cream_cheese_in_the_bowl` 仍然是最弱任务（40%）。

---
