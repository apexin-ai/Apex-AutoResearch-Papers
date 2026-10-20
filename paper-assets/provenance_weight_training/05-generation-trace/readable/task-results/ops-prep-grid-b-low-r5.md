# ops prep grid b low r5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_grid_b_low_r5_20260516T001323_result.json`
- **Structured JSON:** [`86981376d9507db4eb37.json`](../../sessions/86/86981376d9507db4eb37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集。以下是对比和 3 条命令：

**参数对齐说明**（与成功脚本 `run_grid_b_seed42.sh` 一致）：
- `--eval_steps 500` ✓（low_serial 漏了，但代码默认值是 500）
- `--save_total_limit 2`（成功脚本用 2，low_serial 用 3，对齐成功脚本）
- `--tau 0.8`（代码默认值，显式传入）
- `--bf16` 代码默认 True，无需显式传
- `--contamination_ratio 0.4` ✓

---

## 3 条独立训练命令

### b=0.3（最高优先级，cuda:1 释放时提交）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && \
nohup python training/pretrain_weighted.py \
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
    --tau 0.8 \
    --seed 42 \
    --logging_steps 10 \
    --save_steps 500 \
    --eval_steps 500 \
    --save_total_limit 2 \
    --save_only_model \
    --contamination_ratio 0.4 \
    > output/models/grid_b0_3_seed42.log 2>&1 &
```

### b=0.1

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && \
nohup python training/pretrain_weighted.py \
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
    --tau 0.8 \
    --seed 42 \
    --logging_steps 10 \
    --save_steps 500 \
    --eval_steps 500 \
    --save_total_limit 2 \
    --save_only_model \
    --contamination_ratio 0.4 \
    > output/models/grid_b0_1_seed42.log 2>&1 &
```

### b=0.2

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && \
nohup python training/pretrain_weighted.py \
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
    --tau 0.8 \
    --seed 42 \
    --logging_steps 10 \
    --save_steps 500 \
    --eval_steps 500 \
    --save_total_limit 2 \
    --save_only_model \
    --contamination_ratio 0.4 \
    > output/models/grid_b0_2_seed42.log 2>&1 &
```

---

**完成状态**：
- `grid_b0_1_seed42/` 残留目录已清理 ✓
- 环境：conda base，python3.12 ✓
- 3 条命令均带 nohup + 独立日志，可直接用 `ssh_execute` 各提交到不同 GPU（需配合 `CUDA_VISIBLE_DEVICES`）

---
