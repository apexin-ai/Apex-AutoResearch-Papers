# ssh westb standard 25 grpo

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westb_standard_25_grpo_20260521T025856_result.json`
- **Structured JSON:** [`c4bdb6d6888e69008408.json`](../../sessions/c4/c4bdb6d6888e69008408.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 已在运行（29599 MiB, 98% util），第一个 step 的 generation 正在进行中。训练正常启动。

**汇报**：

- **SFT checkpoint**: 存在 `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870/`（model.safetensors 10.8GB，完整）
- **GRPO**: 之前不存在，已提交训练
- **修复**: tokenizer_config.json 的 `tokenizer_class` 从 `Qwen2Tokenizer`（慢）改为 `Qwen2TokenizerFast`，否则缺 `vocab.json` 无法加载
- **训练状态**: 已在 GPU 1（cuda:1）上启动，100 steps，wandb run `7v9jorwy`
  - PID: 64189 (bash) → 64194 (python)
  - GPU 显存: 29.6GB / 96GB
  - 日志: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb.log`
  - 输出: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/`
- **磁盘**: `/root/autodl-tmp/` 24GB free，GRPO checkpoint ~15GB，刚好够用

---
