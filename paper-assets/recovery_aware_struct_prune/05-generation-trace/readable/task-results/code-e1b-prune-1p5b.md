# code e1b prune 1p5b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e1b_prune_1p5b_20260518T104250_result.json`
- **Structured JSON:** [`985893d8a0feef284b32.json`](../../sessions/98/985893d8a0feef284b32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`grpo_cka_only_20/checkpoint-100` 占 27GB，包含 optimizer/scheduler states。最终模型已在顶层保存（12GB `model.safetensors`）。

**删除 `checkpoint-100` 可释放 ~27GB，足够 1.5B 实验所需的 ~10GB。** 确认可以删除吗？

---
