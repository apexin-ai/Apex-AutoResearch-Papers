# ssh check 15pct checkpoints

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_15pct_checkpoints_20260521T192427_result.json`
- **Structured JSON:** [`badf544fe61217ed01a0.json`](../../sessions/ba/badf544fe61217ed01a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部在 **westd-29022** 上。汇总如下：

## 15% Checkpoint 可用性报告

所有 15% checkpoint 均在 **westd-29022** 的 `/root/autodl-tmp/recovery_aware_struct_prune/` 下，**westb-23072 上无 15% checkpoint**。

### Pruned models（剪枝后、未恢复训练）

| 目录 | model.safetensors 大小 | 状态 |
|------|----------------------|------|
| `pruned_cka_only_15/` | 13.07 GB | 完整 |
| `pruned_standard_15/` | 13.04 GB | 完整 |

### SFT 恢复模型

| 目录 | model.safetensors 大小 | 状态 |
|------|----------------------|------|
| `sft_cka_only_15/` | 13.07 GB | 完整 |
| `sft_standard_15/` | 13.04 GB | 完整 |

### GRPO 恢复模型

| 目录 | model.safetensors 大小 | 状态 |
|------|----------------------|------|
| `grpo_cka_only_15_seed123/` | 1.62 GB (LoRA adapter) + `checkpoint-100/` 13.07 GB (full) | 完整 |
| `grpo_cka_only_15_seed456/` | 仅 `checkpoint-100/` 13.07 GB (full)，**根目录无合并模型** | 部分完整 |

**注意**: `grpo_cka_only_15_seed456` 根目录缺少合并的 model.safetensors，只有 checkpoint-100 子目录有完整权重。`grpo_cka_only_15_seed123` 根目录有 1.62 GB 的文件（可能是 LoRA adapter 而非完整模型），checkpoint-100 里有完整的 13.07 GB 权重。没有 `grpo_standard_15` 目录。

### eval_math500.py

位于 `/root/recovery_aware_struct_prune/src/eval_math500.py`（westd-29022），7983 bytes。

### Eval 命令模板

```bash
# === westd-29022, GPU 白名单: cuda:0/1/2/3 ===

# SFT CKA-only 15%
CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_15/results.json --max_new_tokens 2048 --seed 42

# SFT Standard 15%
CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_15/results.json --max_new_tokens 2048 --seed 42

# GRPO CKA-only 15% seed123 (用 checkpoint-100 完整权重)
CUDA_VISIBLE_DEVICES=2 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed123/checkpoint-100 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_15_seed123/results.json --max_new_tokens 2048 --seed 42

# GRPO CKA-only 15% seed456 (用 checkpoint-100 完整权重)
CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed456/checkpoint-100 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_15_seed456/results.json --max_new_tokens 2048 --seed 42

# Pruned baselines (无恢复训练)
CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_15 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_pruned_cka_only_15/results.json --max_new_tokens 2048 --seed 42

CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_15 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_pruned_standard_15/results.json --max_new_tokens 2048 --seed 42
```

**缺失项**: 无 `grpo_standard_15` 系列 checkpoint（两个 seed 都没有）。如需此条件需先训练。

---
