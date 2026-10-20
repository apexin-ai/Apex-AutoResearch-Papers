# ops check vanilla s0 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-vanilla-s0-eval_20260516T111301_result.json`
- **Structured JSON:** [`3c7948e1baf9cbf2f02c.json`](../../sessions/3c/3c7948e1baf9cbf2f02c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已完成，结果文件 588KB，生成于 18:43。

### LLaMA 3.1 Vanilla s0 Injected Eval 结果

| 指标 | 值 |
|------|-----|
| Total episodes | 47 |
| **Recovery rate** | **0.745** |
| **Detection rate** | **0.277** |

**Per-operator breakdown:**

| Operator | Recovery | Detection |
|----------|----------|-----------|
| C1_context_truncation | 8/12 (0.667) | 2/12 (0.167) |
| C4_observation_masking | 8/11 (0.727) | 4/11 (0.364) |
| P1_step_order_swap | 11/12 (0.917) | 4/12 (0.333) |
| P2_sub_goal_deletion | 8/12 (0.667) | 3/12 (0.250) |

**GPU 0 状态：** 未释放，仍占用 16837 MiB，利用率 87%。模型仍在显存中。

---
