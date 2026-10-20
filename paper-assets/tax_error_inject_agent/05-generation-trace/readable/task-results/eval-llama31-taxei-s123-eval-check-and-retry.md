# eval llama31 taxei s123 eval check and retry

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama31-taxei-s123-eval-check-and-retry_20260516T153151_result.json`
- **Structured JSON:** [`b3178fd61ee5c1abfc94.json`](../../sessions/b3/b3178fd61ee5c1abfc94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE。

**结果摘要：**

| 指标 | 值 |
|------|-----|
| recovery_rate | 0.596 |
| detection_rate | 0.362 (假阳性) |
| total_episodes | 47 |

**By operator:**

| Operator | Recovery | Detection |
|----------|----------|-----------|
| C1_context_truncation | 0.583 | 0.25 |
| C4_observation_masking | 0.727 | 0.545 |
| P1_step_order_swap | 0.500 | 0.417 |
| P2_sub_goal_deletion | 0.583 | 0.25 |

无需重跑，eval 实际已于 May 16 23:25 完成。Cron 误判已在 notes 中标注。

---
