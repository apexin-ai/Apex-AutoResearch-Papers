# diagnose crm goal seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_crm-goal-seed42_20260519T212128_result.json`
- **Structured JSON:** [`ab18399441b599d4f42b.json`](../../sessions/ab/ab18399441b599d4f42b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验状态：完成，metrics 完整。**

### 结果摘要

- **overall_success_rate: 0.67**
- mode: `crm_obs_only`, benchmark: `goal`, n_rollouts: 10/task, 10 tasks

### Per-task 成功率

| Task | Success Rate | Successes/Total |
|------|:-----------:|:---------------:|
| turn_on_the_stove | **1.0** | 10/10 |
| put_the_bowl_on_top_of_the_cabinet | **1.0** | 10/10 |
| put_the_bowl_on_the_stove | 0.9 | 9/10 |
| push_the_plate_to_the_front_of_the_stove | 0.9 | 9/10 |
| put_the_bowl_on_the_plate | 0.9 | 9/10 |
| open_the_middle_drawer_of_the_cabinet | 0.8 | 8/10 |
| put_the_wine_bottle_on_top_of_the_cabinet | 0.4 | 4/10 |
| put_the_wine_bottle_on_the_rack | 0.4 | 4/10 |
| open_the_top_drawer_and_put_the_bowl_inside | **0.2** | 2/10 |
| put_the_cream_cheese_in_the_bowl | **0.2** | 2/10 |

进程已正常退出，JSON 完整写出（1319 bytes）。无运行日志文件（可能直接输出到 stdout 未重定向，或日志路径不同）。

---
