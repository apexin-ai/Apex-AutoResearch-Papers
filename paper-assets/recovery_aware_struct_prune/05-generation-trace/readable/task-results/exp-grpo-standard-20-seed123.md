# exp grpo standard 20 seed123

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_grpo_standard_20_seed123_20260520T062029_result.json`
- **Structured JSON:** [`8ff73d6eac7bcab0338e.json`](../../sessions/8f/8ff73d6eac7bcab0338e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**总结：**

- **Registry**: `grpo_standard_20_seed123` → RUNNING
- **服务器**: westd-29022, cuda:2, tmux session `grpo_standard_20_seed123`
- **PID**: 211972 (Python), 211967 (wrapper)
- **配置**: v5 fair config — 100 steps, beta=0.01, loss_type=dapo, temperature=0.4, max_completion_length=1024, seed=123, WANDB_MODE=offline
- **SFT checkpoint**: `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20`
- **输出**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123`
- **当前状态**: 模型已加载到 GPU (12.5GB)，正在加载 ref_model，数据集已从缓存加载 (7473 samples)
- **注**: cuda:2 上同时有 seed=456 的 GRPO 任务（另一 agent 提交），但 98GB VRAM 足够两个训练共存。实际 seed=456 在 cuda:3。

---
