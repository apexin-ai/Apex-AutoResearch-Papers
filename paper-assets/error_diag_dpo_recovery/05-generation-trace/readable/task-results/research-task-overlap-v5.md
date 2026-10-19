# research task overlap v5

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_task_overlap_v5_20260512T172424_result.json`
- **Structured JSON:** [`cd9015336e919a42e2fa.json`](../../sessions/cd/cd9015336e919a42e2fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### 1. Task 标识字段
- **Expert SFT**: `game_file` 字段（JSON 数组，keys: `id`, `game_file`, `conversations`，无 `reward`/`task_type` 字段，全部为成功轨迹）
- **V5 失败轨迹**: `game_file` 字段（JSONL，keys: `task_id`, `task_type`, `game_file`, `reward`, `steps`, `conversations`）
- 用 `game_file` 路径中的 task folder name 作为匹配 key（如 `pick_heat_then_place_in_recep-Apple-None-CounterTop-30`）

### 2. 覆盖统计
| 数据源 | 总条目 | Unique Tasks |
|--------|--------|-------------|
| Expert SFT | 3,119 | 1,395 |
| V5 轨迹 | 71 | 40（20 fail, 20 success）|

### 3. Overlap: **20/20 = 100%**

所有 20 个 v5 失败 task 都在 expert 成功轨迹中找到了匹配。**无非重叠的失败 task。**

### 4. 按 Task Type 的 Overlap 分布

| Task Type | Expert | V5 Fail | Overlap | Overlap% |
|-----------|--------|---------|---------|----------|
| pick_and_place | 318 | 2 | 2 | 100% |
| pick_clean_then_place | 257 | 5 | 5 | 100% |
| pick_cool_then_place | 201 | 2 | 2 | 100% |
| pick_heat_then_place | 175 | 10 | 10 | 100% |
| pick_two_obj | 322 | 1 | 1 | 100% |
| look_at_obj | 122 | 0 | - | - |

注意：`pick_heat_then_place` 是 v5 失败最集中的类型（10/20），且 v5 中该类型成功率为 0%。`look_at_obj` 在 v5 中无失败（4/4 成功）。

### 5. 数据 Split
两个数据源均来自 ALFWorld **train** split，无 split 不匹配问题。

### 6. DPO Pair 构建可行性评估

**完全可行。** 100% overlap 意味着当前所有 20 个失败 task 都可以构建 DPO pair（expert 成功 + model 失败）。Expert 数据覆盖 1,395 个 unique task，远大于 v5 当前 40 个 task，随着 v5 收集继续推进，预计 overlap 率将保持在高水平。

唯一值得注意的是 expert SFT 中同一 task 有多条轨迹（3,119 条 / 1,395 task ≈ 2.2 条/task），DPO 配对时可按轨迹质量（步数等）选择最佳 expert 轨迹。

---
