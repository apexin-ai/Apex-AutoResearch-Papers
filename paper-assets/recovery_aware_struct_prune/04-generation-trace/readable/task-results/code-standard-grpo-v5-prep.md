# code standard grpo v5 prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_standard-grpo-v5-prep_20260515T123134_result.json`
- **Structured JSON:** [`05c91087825d4d884858.json`](../../sessions/05/05c91087825d4d884858.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总如下：

### 1. Standard v5 脚本内容

```bash
#!/bin/bash
# GRPO v5 Standard — cuda:1
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/recovery_aware_struct_prune

CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py \
    --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 \
    --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20 \
    --gpu 0 \
    --max_completion_length 512 \
    --steps_per_generation 4 \
    --num_train_epochs 1 \
    --max_samples 1000 \
    --learning_rate 1e-6 \
    --beta 0.01 \
    --loss_type dapo \
    --format_reward_weight 0.1 \
    --temperature 0.4 \
    --repetition_penalty 1.15 \
    --gradient_checkpointing true \
    --save_total_limit 3 \
    --save_steps 100 \
    --reward_desert_patience 50 \
    --run_name grpo_stage2_standard_20_v5
```

### 2. 与 RASP v5 的参数差异

| 参数 | RASP v5 | Standard v5 |
|------|---------|-------------|
| `CUDA_VISIBLE_DEVICES` | 0 | **1** |
| `--model_path` | `sft_rasp_20` | **`sft_standard_20`** |
| `--output_dir` | `grpo_stage2_rasp_20_v5` | **`grpo_stage2_standard_20`** |
| `--run_name` | `grpo_stage2_rasp_20_v5` | **`grpo_stage2_standard_20_v5`** |

其余参数完全一致（beta=0.01, temp=0.4, rep_penalty=1.15, format_reward=0.1, max_completion_length=512, gradient_checkpointing=true, steps_per_generation=4 等）。

### 3. sft_standard_20_retrain 进度

**已完成。** `sft_standard_20` 目录下 `model.safetensors` (12GB) 已保存，包含 checkpoint-935 和 checkpoint-1870。tmux session `sft_standard_20_retrain` 已不存在（训练结束后自动关闭）。可以立即启动 Standard v5 GRPO。

### 4. 脚本验证

- 脚本路径：`/root/recovery_aware_struct_prune/scripts/run_grpo_v5_standard.sh`
- `bash -n` 语法检查：**通过**
- 已设置可执行权限

---
