# submit d022 phaseD

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_d022-phaseD_20260515T093247_result.json`
- **Structured JSON:** [`22ffff076bbf4e83420e.json`](../../sessions/22/22ffff076bbf4e83420e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## Random inject25 训练 & Eval 结果

### 训练
| 实验 | 状态 | 耗时 | Final Loss | Token Acc |
|------|------|------|-----------|-----------|
| v4-random-fixed-inject25-s0 | success | 56m13s | 0.425 | 0.919 |
| v4-random-fixed-inject25-s123 | success | 56m24s | 0.425 | 0.924 |

### Eval (no_inject, valid_unseen, 47 episodes)
| 实验 | Success Rate | Successes/Total |
|------|-------------|-----------------|
| s0 | **61.7%** | 29/47 |
| s123 | **51.1%** | 24/47 |

### 按任务类型分解
| Task Type | s0 | s123 |
|-----------|-----|------|
| look_at_obj_in_light | 66.7% | 66.7% |
| pick_and_place_simple | 62.5% | 37.5% |
| pick_clean_then_place | 45.5% | 54.5% |
| pick_cool_then_place | 57.1% | 14.3% |
| pick_heat_then_place | 75.0% | 75.0% |
| pick_two_obj_and_place | 71.4% | 57.1% |

对标 seed=42 的 55.3%，三个 seed 的平均 success rate 为 **(61.7 + 51.1 + 55.3) / 3 = 56.0%**。s123 的 pick_cool_then_place (14.3%) 拉低了整体，s0 表现最好。GPU 0,1 现已空闲。

---
