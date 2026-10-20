# eval gpu2 read and monitor

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gpu2-read-and-monitor_20260516T123454_result.json`
- **Structured JSON:** [`f7fd2ee9093e1fd1e3cd.json`](../../sessions/f7/f7fd2ee9093e1fd1e3cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项 eval 均已完成。结果如下：

## LLaMA Random s0 — Injected Eval

| 指标 | 值 |
|------|-----|
| recovery_rate | **0.745** |
| detection_rate | **0.255** |
| total_episodes | 47 |

**By operator:**

| Operator | Total | Recovered | Recovery Rate | Detected | Detection Rate |
|----------|-------|-----------|---------------|----------|----------------|
| C1_context_truncation | 12 | 10 | 0.833 | 1 | 0.083 |
| C4_observation_masking | 11 | 8 | 0.727 | 4 | 0.364 |
| P1_step_order_swap | 12 | 8 | 0.667 | 4 | 0.333 |
| P2_sub_goal_deletion | 12 | 9 | 0.750 | 3 | 0.250 |

## LLaMA Random s0 — Clean Eval

| 指标 | 值 |
|------|-----|
| success_rate | **0.745** |
| total_episodes | 47 |

Clean 和 injected 的 recovery_rate 均为 0.745，说明模型在注入干扰后仍能恢复到与无干扰时相同的成功率。检测率最高的是 C4_observation_masking (0.364) 和 P1_step_order_swap (0.333)，最低的是 C1_context_truncation (0.083)。

---
