# pipeline qwen math rasp rlvr

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pipeline_qwen_math_rasp_rlvr_20260516T161827_result.json`
- **Structured JSON:** [`f25109779a601951b3f6.json`](../../sessions/f2/f25109779a601951b3f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GRPO `grpo_rasp_25` 在 cuda:0 上只跑到 step 30/100，按当前速度还需 ~90 分钟才能完成。同时 eval 也在 GPU 0 上跑（89/200，~10min 剩余）。

但 **cuda:2 和 cuda:3 完全空闲**（0% utilization, 0MiB）。建议改用 cuda:2 跑这个 pipeline，无需等待。是否同意切换到 cuda:2？还是坚持等 cuda:0 空闲？

---
