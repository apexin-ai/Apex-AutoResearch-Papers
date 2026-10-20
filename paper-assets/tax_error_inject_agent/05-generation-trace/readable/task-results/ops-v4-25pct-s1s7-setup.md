# ops v4 25pct s1s7 setup

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v4-25pct-s1s7-setup_20260515T213138_result.json`
- **Structured JSON:** [`71bfc385e26dc33519c7.json`](../../sessions/71/71bfc385e26dc33519c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全部在跑，cuda:0 和 cuda:1 已被新任务占用。

**汇报：**

| 实验 | GPU | PID | 数据 | Registry |
|------|-----|-----|------|----------|
| v4-random-fixed-inject25-s1 | cuda:0 | 200146 | `sft_random_v4_fixed_inject25.jsonl` (4358行) | RUNNING |
| v4-taxei-fixed-inject25-s7 | cuda:1 | 200226 | `sft_taxei_v4_fixed_inject25.jsonl` (4358行) | RUNNING |

cuda:0-3 四卡全部在用，GPU 利用率 54-94%，显存 18-19GB/32GB。

---
