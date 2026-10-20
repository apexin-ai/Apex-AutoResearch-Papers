# exp grpo standard 20 seed456

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_grpo_standard_20_seed456_20260520T062038_result.json`
- **Structured JSON:** [`ca3d8fee9636e3542b83.json`](../../sessions/ca/ca3d8fee9636e3542b83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，所有验证通过：

- **Registry**: `grpo_standard_20_seed456` 已创建，parent=`grpo_stage2_standard_20_fair`
- **Tmux**: session `grpo_standard_20_seed456`，PID 211803
- **GPU**: cuda:3 (CUDA_VISIBLE_DEVICES=3)
- **Config**: 与 seed=42 一致 — beta=0.01, loss_type=dapo, temperature=0.4, max_steps=100, max_completion_length=1024, optim=adamw_8bit
- **Model**: `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/` (12.3GB，正在加载中)
- **Output**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456/`

模型正从磁盘加载到 GPU 3（12.3GB，需要几分钟）。加载完成后 GPU 显存会上升并开始训练。Cron 自动监控后续状态。

---
