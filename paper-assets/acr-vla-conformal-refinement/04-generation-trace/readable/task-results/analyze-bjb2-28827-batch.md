# analyze bjb2 28827 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_bjb2-28827-batch_20260520T121702_result.json`
- **Structured JSON:** [`83bee45056dc0bdc2943.json`](../../sessions/83/83bee45056dc0bdc2943.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**这 3 个实验仍在运行中，尚未完成。**

从 `ps aux` 可以确认：

| 实验 | PID | 启动时间 | CPU 时间 | 状态 |
|------|-----|---------|---------|------|
| eval-vla-only-spatial-seed48 | 336826 | 20:07 | 58min | 运行中，完成 1/10 tasks（task0: 7/10 = 70%），正在跑 task1 |
| eval-vla-only-goal-seed47 | 336621 | 20:07 | 63min | 运行中，完成 1/10 tasks（task0: 8/10 = 80%） |
| eval-obs-only-spatial-norm02-seed42 | 340026 | 20:08 | 53min | 运行中，完成 1/10 tasks（task0: 9/10 = 90%），正在跑 task1 |

每个实验需要跑 10 tasks × 10 rollouts = 100 个 episode，目前每个只完成了约 10-20 个。按当前速度估计还需要 **1-2 小时**才能全部完成。

**当前部分结果（仅 task 0）：**

| 实验 | Task 0 | 成功率 |
|------|--------|--------|
| vla-only-spatial-seed48 | pick_up_the_black_bowl_between_plate_and_ramekin... | 70% (7/10) |
| vla-only-goal-seed47 | open_the_middle_drawer_of_the_cabinet | 80% (8/10) |
| obs-only-spatial-norm02-seed42 | pick_up_the_black_bowl_between_plate_and_ramekin... | 90% (9/10) |

JSON 结果文件尚未生成（实验结束时才会写入）。无错误信息，实验运行正常。

服务器上同时还有 2 个 adaptive-k 实验在跑（spatial-p75-seed44 和 spatial-p90-seed42，从 18:45 开始）。

---
