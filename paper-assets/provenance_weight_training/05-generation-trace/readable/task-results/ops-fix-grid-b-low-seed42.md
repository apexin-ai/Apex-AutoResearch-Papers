# ops fix grid b low seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_grid_b_low_seed42_20260515T085303_result.json`
- **Structured JSON:** [`34a99979731c81464538.json`](../../sessions/34/34a99979731c81464538.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 1. Kill 确认
- PID 163662 已终止（SIGTERM 成功，无需 SIGKILL）
- tmux session `grid_b_low_seed42` 已清除

### 2. GPU 释放确认
- GPU 1: **0MiB / 97887MiB**，已完全释放
- GPU 0/2/3 仍在跑其他任务（各 ~46.5GB）

### 3. Checkpoint 删除确认
- `grid_b0_1_seed42` 已删除（唯一产生了 fp32 checkpoint 的目录）
- `grid_b0_2_seed42` / `grid_b0_3_seed42` 原本不存在（b=0.1 还没跑完）

### 4. 修复后的脚本

修复了两个 bug + 一个参数名错误：
- **加了 `--bf16`**（原来缺失，导致 fp32 占 75GB）
- **去掉了 `--eval_data_path` 和 `--eval_steps`**（改为 post-hoc eval）
- **`--b_value` → `--grid_b_value`**（代码实际参数名）

完整脚本位于 `/root/provenance_weight_training/training/run_grid_b_low_seed42.sh`：

```bash
#!/bin/bash
set -e
# Grid-b low values (0.1/0.2/0.3) serial training, seed=42, bf16, no inline eval

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/provenance_weight_training

# b=0.1
WANDB_MODE=disabled python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir output/models/grid_b0_1_seed42 \
    --weighting_method grid \
    --grid_b_value 0.1 \
    --model_name models/Qwen/Qwen3-0.6B \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --max_length 2048 \
    --learning_rate 5e-5 \
    --seed 42 \
    --logging_steps 10 \
    --save_steps 500 \
    --save_total_limit 2 \
    --save_only_model \
    --contamination_ratio 0.4 \
    --bf16

echo "b=0.1 seed42 complete"

# b=0.2
WANDB_MODE=disabled python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir output/models/grid_b0_2_seed42 \
    --weighting_method grid \
    --grid_b_value 0.2 \
    --model_name models/Qwen/Qwen3-0.6B \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --max_length 2048 \
    --learning_rate 5e-5 \
    --seed 42 \
    --logging_steps 10 \
    --save_steps 500 \
    --save_total_limit 2 \
    --save_only_model \
    --contamination_ratio 0.4 \
    --bf16

echo "b=0.2 seed42 complete"

# b=0.3
WANDB_MODE=disabled python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir output/models/grid_b0_3_seed42 \
    --weighting_method grid \
    --grid_b_value 0.3 \
    --model_name models/Qwen/Qwen3-0.6B \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --max_length 2048 \
    --learning_rate 5e-5 \
    --seed 42 \
    --logging_steps 10 \
    --save_steps 500 \
    --save_total_limit 2 \
    --save_only_model \
    --contamination_ratio 0.4 \
    --bf16

echo "All grid-b low seed42 training complete"
```

等待审阅，不启动训练。

---
