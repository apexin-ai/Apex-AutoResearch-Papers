# eval vanilla s123 injected gpu0 MUST COMPLETE

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_vanilla-s123-injected-gpu0-MUST-COMPLETE_20260516T145224_result.json`
- **Structured JSON:** [`1e4bb6171b2565a2cfa4.json`](../../sessions/1e/1e4bb6171b2565a2cfa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成，registry 已更新为 DONE。

**最终结果汇总：**

| 指标 | 值 |
|------|-----|
| recovery_rate | **70.2%** |
| detection_rate | **21.3%** |
| total_episodes | 47 |

**按 operator 分组：**

| Operator | Recovery Rate | Detection Rate |
|----------|--------------|----------------|
| C1_context_truncation | 75.0% | 8.3% |
| C4_observation_masking | 72.7% | 36.4% |
| P1_step_order_swap | 66.7% | 33.3% |
| P2_sub_goal_deletion | 66.7% | 8.3% |

**对比参考值：** s42=74.5%, s0=74.5%, **s123=70.2%**。偏低约 4 个百分点但在合理波动范围内。

文件已验证存在且完整：`eval_results/llama31_vanilla_s123_injected.json`（678594 bytes）。

---
