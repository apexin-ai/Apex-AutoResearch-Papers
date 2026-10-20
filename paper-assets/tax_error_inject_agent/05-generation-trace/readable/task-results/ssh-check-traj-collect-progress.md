# ssh check traj collect progress

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-traj-collect-progress_20260514T162625_result.json`
- **Structured JSON:** [`36d0b26a7231a35e0e29.json`](../../sessions/36/36d0b26a7231a35e0e29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态：已完成**

- **进程 61438**：已退出（不再运行）
- **结果**：成功完成，耗时 5245 秒（~87 分钟）
- **成功轨迹**：501 条（目标 500，已超额完成）
- **失败轨迹**：213 条
- **总计**：714 条，成功率 70.2%
- **API 开销**：$8.86（2796 请求，1.83M input tokens，429K output tokens）

**按任务类型分布**：
| 任务类型 | 成功数 |
|---------|--------|
| look_at_obj_in_light | 101 |
| pick_and_place_simple | 102 |
| pick_clean_then_place_in_recep | 67 |
| pick_cool_then_place_in_recep | 68 |
| pick_heat_then_place_in_recep | 74 |
| pick_two_obj_and_place | 89 |

轨迹收集已顺利完成，数据在 `data/trajectories/successful_trajectories.jsonl`。

---
