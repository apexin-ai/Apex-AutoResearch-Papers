# ops westb disk cleanup step100

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb-disk-cleanup-step100_20260515T214137_result.json`
- **Structured JSON:** [`0d51fa9e96d2f10945ed.json`](../../sessions/0d/0d51fa9e96d2f10945ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**释放 ~38GB，当前可用 63GB**（超过 55GB 目标）。

删除内容：
- `grpo_stage2_standard_20_v8/checkpoint-50/optimizer.pt` — 15.8GB（model.safetensors 保留）
- `sft_rasp_20/checkpoint-935/optimizer.pt` — 24.6GB（中间 checkpoint，训练已完成到 step 1870，模型文件保留）

---
