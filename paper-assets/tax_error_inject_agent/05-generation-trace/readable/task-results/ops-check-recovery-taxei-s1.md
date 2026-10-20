# ops check recovery taxei s1

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-recovery-taxei-s1_20260516T091606_result.json`
- **Structured JSON:** [`d36a2e60fd22582a2361.json`](../../sessions/d3/d36a2e60fd22582a2361.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已完成。结果：

**=== Recovery TaxEI s1 ===**

| 指标 | 值 |
|------|-----|
| **recovery_rate** | **0.617** (29/47) |
| **detection_rate** | **0.0** (0/47) |
| seed | 42 |
| model | checkpoint-3387 (v4 seed1) |

**Per-operator recovery rate:**

| Operator | Total | Recovered | Rate |
|----------|-------|-----------|------|
| C1_context_truncation | 12 | 9 | **0.750** |
| C4_observation_masking | 11 | 7 | **0.636** |
| P1_step_order_swap | 12 | 7 | **0.583** |
| P2_sub_goal_deletion | 12 | 6 | **0.500** |

**Per-task recovery rate:**

| Task Type | Total | Rate |
|-----------|-------|------|
| pick_heat_then_place | 8 | 0.875 |
| look_at_obj_in_light | 6 | 0.833 |
| pick_two_obj_and_place | 7 | 0.714 |
| pick_and_place_simple | 8 | 0.500 |
| pick_clean_then_place | 11 | 0.455 |
| pick_cool_then_place | 7 | 0.429 |

detection_rate 为 0 — 模型从未主动检测到错误注入，但仍有 61.7% 的 episode 通过隐式恢复完成了任务。C1（上下文截断）最容易恢复，P2（子目标删除）最难。

---
