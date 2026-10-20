# ops gpu status and collect

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-and-collect_20260516T123812_result.json`
- **Structured JSON:** [`be7d6d45b8a6c2c6f624.json`](../../sessions/be/be7d6d45b8a6c2c6f624.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

**所有 GPU 空闲（0 MiB 显存占用），全部任务已完成。**

### Eval 结果

| 模型 | Split | Success Rate | Total Episodes |
|------|-------|-------------|----------------|
| **TaxEI s42** (clean) | valid_unseen | **0.766** (36/47) | 47 |
| **Random s0** (clean) | valid_unseen | **0.745** (35/47) | 47 |

### TaxEI s42 按任务类型

| Task Type | Rate |
|-----------|------|
| look_at_obj_in_light | 1.000 (6/6) |
| pick_heat_then_place | 0.875 (7/8) |
| pick_two_obj_and_place | 0.857 (6/7) |
| pick_cool_then_place | 0.714 (5/7) |
| pick_clean_then_place | 0.636 (7/11) |
| pick_and_place_simple | 0.625 (5/8) |

### Random s0 按任务类型

| Task Type | Rate |
|-----------|------|
| pick_heat_then_place | 1.000 (8/8) |
| pick_two_obj_and_place | 1.000 (7/7) |
| look_at_obj_in_light | 0.667 (4/6) |
| pick_clean_then_place | 0.636 (7/11) |
| pick_and_place_simple | 0.625 (5/8) |
| pick_cool_then_place | 0.571 (4/7) |

### GPU 1: TaxEI s0 训练

训练已完成，产出 3 个 checkpoint：
- `v1-20260516-181826/checkpoint-1129`
- `v1-20260516-181826/checkpoint-2258`
- `v1-20260516-181826/checkpoint-3387` (final)

### GPU 3

空闲，无进程。

---
