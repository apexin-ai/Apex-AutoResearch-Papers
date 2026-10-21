# diagnose w2 qwen3 8b exec pilot r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w2-qwen3-8b-exec-pilot-r2_20260516T105106_result.json`
- **Structured JSON:** [`9d1672f8a0e21770022d.json`](../../sessions/9d/9d1672f8a0e21770022d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：训练失败（OOM）。**

- 崩溃点：step 1 完成后 step 2 forward pass 时 OOM
- 原因：Qwen3-8B 即使用 K=2、batch=1、gradient checkpointing、8bit optimizer，仍然占用 ~94.75GB，单卡 A800 (95GB) 放不下
- 已标记 `conclusion=failed`，cron 已删除

**结论：Qwen3-8B GRPO 在单卡 A800 上不可行。** 若要跑 8B 模型，需要：
1. 双卡 FSDP/DeepSpeed，或
2. LoRA（仅训少量参数减少 activation memory），或
3. 进一步降低 max_completion_length 减少 activation 占用

---
