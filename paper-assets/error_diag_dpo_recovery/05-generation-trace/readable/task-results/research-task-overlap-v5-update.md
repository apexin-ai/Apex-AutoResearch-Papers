# research task overlap v5 update

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_task_overlap_v5_update_20260512T185708_result.json`
- **Structured JSON:** [`3b87eb4de8e957c6fa97.json`](../../sessions/3b/3b87eb4de8e957c6fa97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### 1. Expert 分布（3119 条）

| Task Type | Unique Tasks |
|---|---|
| look_at_obj | 279 |
| pick_and_place | 759 |
| pick_clean_then_place | 576 |
| pick_cool_then_place | 472 |
| pick_heat_then_place | 371 |
| pick_two_obj | 662 |

### 2. V5 当前状态（270 条轨迹，两卡各 ~135）

| Task Type | Total | Fail | Fail Tasks | Matched | Overlap% | SR |
|---|---|---|---|---|---|---|
| look_at_obj | 14 | 2 | 1 | 1 | 100% | 85.7% |
| pick_and_place | 67 | 17 | 10 | 9 | 90% | 74.6% |
| pick_clean_then_place | 57 | 38 | 23 | 21 | 91% | 33.3% |
| pick_cool_then_place | 41 | 41 | 21 | 19 | 90% | **0.0%** |
| pick_heat_then_place | 35 | 35 | 18 | 15 | 83% | **0.0%** |
| pick_two_obj | 56 | 31 | 21 | 16 | 76% | 44.6% |
| **TOTAL** | **270** | **164** | **94** | **81** | **86%** | — |

### 3. Overlap 分析

从之前 40 条时的 100% 下降到 **86%**。随着数据量增加，模型在更多 task 上失败，其中部分 task 不在 expert 数据中。按 task type 看，`look_at_obj` 仍 100%，`pick_two_obj` 最低 76%。

### 4. 未匹配 failure tasks（13 个）

- pick_and_place: 1 个
- pick_clean_then_place: 2 个
- pick_cool_then_place: 2 个
- pick_heat_then_place: 3 个
- pick_two_obj: 5 个

### 5. DPO Pair 可行性

- **81 个 unique failure tasks 有 expert 匹配**，可直接构建 DPO pairs
- 13 个未匹配的 failure tasks（14%）无法配对，需要丢弃或另找 positive 样本
- `pick_cool_then_place` 和 `pick_heat_then_place` SR=0%，说明模型在这两类任务上完全失败，是 DPO 训练的重点改善方向
- 86% 的 overlap 率对 DPO 构建仍然充足

---
