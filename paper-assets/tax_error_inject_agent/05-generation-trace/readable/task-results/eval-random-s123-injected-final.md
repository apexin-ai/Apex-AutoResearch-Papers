# eval random s123 injected FINAL

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_random-s123-injected-FINAL_20260516T151732_result.json`
- **Structured JSON:** [`6cd0cfeee5be64a1c16c.json`](../../sessions/6c/6cd0cfeee5be64a1c16c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

random-s123 injected eval 完成，registry 已注册为 DONE。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| Recovery rate | **78.7%** (37/47) |
| Detection rate | **25.5%** (12/47) |

**Per-operator recovery:**
| Operator | Recovery | Detection |
|----------|----------|-----------|
| C1_context_truncation | 83.3% (10/12) | 8.3% |
| C4_observation_masking | 72.7% (8/11) | 18.2% |
| P1_step_order_swap | 83.3% (10/12) | 41.7% |
| P2_sub_goal_deletion | 75.0% (9/12) | 33.3% |

**Cross-seed comparison (LLaMA Random injected):**
- s42: 76.6%
- s0: 74.5%
- **s123: 78.7%** — highest of the three seeds, within expected range.

---
