# ssh restart prep 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_restart_prep_30476_20260517T205624_result.json`
- **Structured JSON:** [`efa4305070c07259a290.json`](../../sessions/ef/efa4305070c07259a290.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。

---

## 结果

**训练脚本**: `/root/provenance_weight_training/training/pretrain_weighted.py`

---

### 实验 1: grid_b0_1_seed42

| 项目 | 值 |
|------|------|
| checkpoint_path | `/root/autodl-tmp/output/models/grid_b0_1_seed42/checkpoint-1500` |
| total_steps | 6103 |
| current_step | 1500 |
| remaining_steps | 4603 |

**重启命令（去掉 inline eval）:**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export WANDB_MODE=disabled
export CUDA_VISIBLE_DEVICES=0
cd /root/provenance_weight_training

python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir /root/autodl-tmp/output/models/grid_b0_1_seed42 \
    --model_name models/Qwen/Qwen3-0.6B \
    --weighting_method grid \
    --grid_b_value 0.1 \
    --contamination_ratio 0.4 \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --learning_rate 5e-5 \
    --max_length 2048 \
    --seed 42 \
    --save_steps 500 \
    --logging_steps 10 \
    --bf16 \
    --save_total_limit 3 \
    --save_only_model \
    --resume_from_checkpoint /root/autodl-tmp/output/models/grid_b0_1_seed42/checkpoint-1500
```

---

### 实验 2: grid_b0_3_seed123 (即 grid_b0_3_seed123_r2)

| 项目 | 值 |
|------|------|
| checkpoint_path | `/root/autodl-tmp/output/models/grid_b0_3_seed123/checkpoint-1000` |
| total_steps | 6103 |
| current_step | 1000 |
| remaining_steps | 5103 |

**重启命令（去掉 inline eval）:**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export WANDB_MODE=disabled
export CUDA_VISIBLE_DEVICES=1
cd /root/provenance_weight_training

python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir /root/autodl-tmp/output/models/grid_b0_3_seed123 \
    --model_name models/Qwen/Qwen3-0.6B \
    --weighting_method grid \
    --grid_b_value 0.3 \
    --contamination_ratio 0.4 \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --learning_rate 5e-5 \
    --max_length 2048 \
    --seed 123 \
    --save_steps 500 \
    --logging_steps 10 \
    --bf16 \
    --save_total_limit 3 \
    --save_only_model \
    --resume_from_checkpoint /root/autodl-tmp/output/models/grid_b0_3_seed123/checkpoint-1000
```

---

**去 eval 的方法**: 脚本中 eval 由 `--eval_data_path` 控制，不传该参数即不做 eval。同时移除了 `--eval_steps`。脚本无 `--evaluation_strategy` 参数。

**注意**: 实验 2 的 `_r2` 日志显示它在 eval step（step 1000 后的 eval，处理到 2900/8477 eval batches）被 kill (SIGTERM=143)，训练本身已完成 step 1000 并保存了 checkpoint。

---
