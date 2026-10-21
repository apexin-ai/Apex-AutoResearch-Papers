# fix verify model consistency

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_verify-model-consistency_20260516T040356_result.json`
- **Structured JSON:** [`91a9024ff95e7eb340ab.json`](../../sessions/91/91a9024ff95e7eb340ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 10 experiments: `Qwen3ForCausalLM`, 36 layers — identical to the base Qwen3-4B model on disk. No Qwen2.5-1.5B-Instruct exists on this server at all.

## 模型一致性检查
- 之前实验模型: **Qwen3-4B** (`Qwen3ForCausalLM`, 36 layers) — 全部 10 个已完成实验一致
- sweep-isr-b02-s42 模型: **Qwen3-4B** (config yaml 指向 `/root/autodl-tmp/models/Qwen3-4B`, PID 626802 仍在 GPU:1 运行)
- sweep-isr-b02-s43 模型: **Qwen3-4B** (同 config)，但 PID 629684 已死（GPU:0 空闲，0MiB）
- config yaml 中模型: **Qwen3-4B** — 所有 19 个 yaml 均指向 `/root/autodl-tmp/models/Qwen3-4B`
- train_grpo.py 默认模型: 无硬编码默认（`default=None`），由 config yaml 传入
- 服务器上模型目录: 仅 Qwen3-4B、Qwen3-8B，**不存在 Qwen2.5-1.5B-Instruct**
- 一致性结论: **MATCH** — 全部实验统一使用 Qwen3-4B
- 执行动作: **无需 kill b02-s42**。但 b02-s43 (PID 629684) 已自行退出，GPU:0 空闲，需要排查原因并可能重新提交。

---
