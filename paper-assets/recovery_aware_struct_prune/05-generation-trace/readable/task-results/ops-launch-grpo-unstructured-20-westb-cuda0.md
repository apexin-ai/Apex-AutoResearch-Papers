# ops launch grpo unstructured 20 westb cuda0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch_grpo_unstructured_20_westb_cuda0_20260519T033310_result.json`
- **Structured JSON:** [`58d2a4f180ef9c067d22.json`](../../sessions/58/58d2a4f180ef9c067d22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GRPO 训练确认运行中：

- **PID**: 860053
- **GPU 0**: 69.3GB VRAM, 527W, **GPU-Util 100%**, 59°C
- **W&B**: `grpo_unstructured_20` — run `xj46p92t`
- **Config**: beta=0.01, temp=0.4, maxlen=1024, DAPO, lr=1e-6, 100 steps, adamw_8bit
- **模型**: `/root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20`（从 7B 基模型重建的 20% unstructured magnitude pruning，非 SFT）
- **输出**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20`
- **日志**: `/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_unstructured_20.log`

注意：eval 记录确认原始 `pruned_unstructured_20` 的 87.87% accuracy 是 pruned-only 模型（从未 SFT），本次 GRPO 直接在 pruned model 上训练。

---
