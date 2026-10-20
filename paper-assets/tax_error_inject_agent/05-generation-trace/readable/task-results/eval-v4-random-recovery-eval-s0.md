# eval v4 random recovery eval s0

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v4-random-recovery-eval-s0_20260516T105206_result.json`
- **Structured JSON:** [`1769fd824fa6afeddb2f.json`](../../sessions/17/1769fd824fa6afeddb2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

**v4-random-recovery-eval-s0 — DONE (success)**

| 指标 | 值 |
|------|-----|
| **recovery_rate** | **55.3%** (26/47) |
| detection_rate | 0% |
| total_episodes | 47 |

**Per-operator breakdown:**

| Operator | Recovered/Total | Rate |
|----------|----------------|------|
| P1_step_order_swap | 7/12 | 58.3% |
| C1_context_truncation | 7/12 | 58.3% |
| C4_observation_masking | 6/11 | 54.5% |
| P2_sub_goal_deletion | 6/12 | 50.0% |

对比 Random s42 (63.8%)，s0 的 recovery rate 低约 10pp，在预期范围内（40-70%）。

---
