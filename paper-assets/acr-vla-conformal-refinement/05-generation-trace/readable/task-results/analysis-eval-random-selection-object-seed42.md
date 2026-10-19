# analysis eval random selection object seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-random-selection-object-seed42_20260520T091553_result.json`
- **Structured JSON:** [`be1590a6625605387405.json`](../../sessions/be/be1590a6625605387405.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常完成（EXIT_CODE=0）。注意：当前 seed42 JSON 的结果是 SR=11%，与之前记录的 SR=13% 不同——之前那个是 seed44 的结果被覆盖前的值，现在已被正确的 seed42 结果替换。

seed44 当前磁盘上的文件也已更新（时间戳 May 20 16:44），SR=11%。

## eval-random-selection-object-seed42 结果

| 指标 | 值 |
|------|-----|
| **overall SR** | **11%** (11/100) |
| n_tasks | 10 |
| n_rollouts per task | 10 |
| total_rollouts | 100 |
| mode | random_selection (K=10) |
| benchmark | LIBERO-Object |

### per_task_sr

| Task | SR |
|------|-----|
| alphabet_soup | 0.0 |
| cream_cheese | 0.1 |
| salad_dressing | 0.1 |
| bbq_sauce | 0.1 |
| ketchup | 0.0 |
| tomato_sauce | 0.1 |
| butter | 0.1 |
| milk | 0.1 |
| chocolate_pudding | 0.2 |
| orange_juice | 0.3 |

**per_task_sr 向量**: `[0, 0.1, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0.2, 0.3]`

### Random Selection 跨 seed 对比

| Seed | SR | per_task_sr |
|------|----|-------------|
| 42 | **11%** | [0, 0.1, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0.2, 0.3] |
| 43 | **9%** | [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3] |
| 44 | **11%** | [0, 0.1, 0.2, 0.2, 0, 0.1, 0.1, 0.1, 0.2, 0.1] |

**3-seed 均值: SR = 10.3%**

注意：之前记录的 seed43=10%, seed44=13% 与当前磁盘上的数据（9%, 11%）不一致，可能是 notes 中提到的旧结果被新 run 覆盖了。当前磁盘上的文件时间戳表明 seed42 和 seed44 都在 May 20 16:44-16:45 被写入（同一批次重跑）。

---
