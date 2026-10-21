# diagnose w2 qwen3 8b isr pilot

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w2-qwen3-8b-isr-pilot_20260516T100844_result.json`
- **Structured JSON:** [`7bbda6ee2c8647b22bc8.json`](../../sessions/7b/7bbda6ee2c8647b22bc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**w2-qwen3-8b-isr-pilot 训练失败 — OOM**

- **失败点**：step 1/500，forward pass 的 `lm_head` 分配 1.16 GiB 失败
- **显存状况**：H800 95GB 全卡，PyTorch 已占 93.42 GiB，剩余仅 502 MiB
- **配置**：Qwen3-8B, num_generations=4, per_device_batch_size=1, gradient_checkpointing=True, adamw_bnb_8bit
- **Checkpoint**：无（仅 reward_log.jsonl）
- **Registry**：已更新 conclusion=failed，记录 failure_reason
- **Cron**：已删除

**可行方向**：8B 模型单卡 GRPO 需要进一步降低显存——可选方案包括 num_generations=2、LoRA/QLoRA、或双卡并行。

---
