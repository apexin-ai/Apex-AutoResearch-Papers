# ops check llama31 vanilla eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-llama31-vanilla-eval_20260516T080539_result.json`
- **Structured JSON:** [`957338090e4b7a30212d.json`](../../sessions/95/957338090e4b7a30212d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## llama31-vanilla-s42 Eval 结果

| 指标 | 值 |
|------|-----|
| Total episodes | 47 |
| **Recovery rate (task success)** | **0.745** (35/47) |
| **Detection rate (think analysis)** | **0.213** (10/47) |

### Per-operator breakdown

| Operator | Recovery | Detection |
|----------|----------|-----------|
| C1_context_truncation | 9/12 (0.750) | 2/12 (0.167) |
| C4_observation_masking | 8/11 (0.727) | 3/11 (0.273) |
| P1_step_order_swap | 9/12 (0.750) | 2/12 (0.167) |
| P2_sub_goal_deletion | 9/12 (0.750) | 3/12 (0.250) |

### GPU 状态

GPU 0 已空闲：0 MiB 显存占用，0% 利用率。

---
