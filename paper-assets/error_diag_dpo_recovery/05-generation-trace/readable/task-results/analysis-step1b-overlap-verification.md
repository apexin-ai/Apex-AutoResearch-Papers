# analysis step1b overlap verification

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_step1b-overlap-verification_20260512T145125_result.json`
- **Structured JSON:** [`06717a07c82e3b90256a.json`](../../sessions/06/06717a07c82e3b90256a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 指标 | 数值 |
|------|------|
| 失败轨迹 unique task_name | 87 |
| Expert 轨迹 unique task_name | 1,395 |
| **重叠数** | **86** |

### 按 task_type 重叠分布

| task_type | 重叠 | 失败总数 |
|-----------|------|----------|
| pick_and_place_simple | 16 | 16 |
| pick_clean_then_place | 21 | 21 |
| pick_heat_then_place | 18 | 18 |
| pick_cool_then_place | 7 | 7 |
| look_at_obj_in_light | 7 | 7 |
| pick_two_obj_and_place | 17 | 18 |

### 结论

**重叠 86 条，远超 50 条门槛。** 89 条失败轨迹中有 86 条在 expert 数据中找到了对应的 task_name，覆盖率 96.6%。

仅 1 条 `pick_two_obj_and_place` 类型的失败轨迹在 expert 中没有对应 task，无需额外补充。6 种 task_type 均有覆盖，分布合理。

---
