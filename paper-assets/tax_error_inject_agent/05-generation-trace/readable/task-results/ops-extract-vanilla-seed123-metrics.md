# ops extract vanilla seed123 metrics

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract-vanilla-seed123-metrics_20260514T204319_result.json`
- **Structured JSON:** [`c3ef356266d066bdb8f2.json`](../../sessions/c3/c3ef356266d066bdb8f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

**v4-vanilla-seed123-eval: 31/47 = 66.0%**

| seed | success_rate | vs seed42 |
|------|-------------|-----------|
| 42 | 61.7% (29/47) | baseline |
| 0 | 68.1% (32/47) | +6.4pp |
| 123 | 66.0% (31/47) | +4.3pp |

三 seed 均值：**65.3%**

分任务类型：
- pick_heat_then_place: 87.5% (最高)
- look_at_obj_in_light: 83.3%
- pick_and_place_simple: 75.0%
- pick_cool_then_place: 57.1%
- pick_two_obj_and_place: 57.1%
- pick_clean_then_place: 45.5% (最低)

---
