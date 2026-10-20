# ops eval rp s1 check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-rp-s1-check_20260516T062052_result.json`
- **Structured JSON:** [`f09316f88ec1256177b2.json`](../../sessions/f0/f09316f88ec1256177b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval-rp-s1 **已完成**，结果文件已生成。

## 结果摘要

| 指标 | 数值 |
|------|------|
| 总 episodes | 47 |
| Recovery rate (task success) | **0.489** (23/47) |
| Detection rate (think analysis) | **0.0** (0/47) |

### Per-operator 分解

| Operator | Recovery | Detection |
|----------|----------|-----------|
| C1_context_truncation | 5/12 (0.417) | 0/12 (0.0) |
| C4_observation_masking | 4/11 (0.364) | 0/11 (0.0) |
| P1_step_order_swap | 9/12 (0.750) | 0/12 (0.0) |
| P2_sub_goal_deletion | 5/12 (0.417) | 0/12 (0.0) |

关键发现：
- P1_step_order_swap 恢复率最高 (75%)，agent 能较好地应对步骤顺序错误
- C4_observation_masking 恢复率最低 (36.4%)，观测遮蔽对 agent 影响最大
- 检测率全部为 0——agent 完全没有在 think 中识别出注入的错误

---
