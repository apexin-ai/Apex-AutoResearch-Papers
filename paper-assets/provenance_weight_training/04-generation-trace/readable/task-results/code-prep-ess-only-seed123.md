# code prep ess only seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_ess_only_seed123_20260515T164923_result.json`
- **Structured JSON:** [`a5fa056f2d68d639ebcc.json`](../../sessions/a5/a5fa056f2d68d639ebcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 验证通过。以下是完整训练命令：

---

### ess_only_seed123

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/provenance_weight_training

python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir output/models/ess_only_seed123 \
    --model_name models/Qwen/Qwen3-0.6B \
    --weighting_method ess_only \
    --contamination_ratio 0.4 \
    --num_train_tokens 200000000 \
    --n_min 2 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --learning_rate 5e-5 \
    --max_length 2048 \
    --seed 123 \
    --logging_steps 10 \
    --save_steps 500 \
    --eval_steps 500 \
    --bf16 \
    --save_total_limit 3 \
    --save_only_model
```

### ess_only_seed456

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/provenance_weight_training

python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir output/models/ess_only_seed456 \
    --model_name models/Qwen/Qwen3-0.6B \
    --weighting_method ess_only \
    --contamination_ratio 0.4 \
    --num_train_tokens 200000000 \
    --n_min 2 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --learning_rate 5e-5 \
    --max_length 2048 \
    --seed 456 \
    --logging_steps 10 \
    --save_steps 500 \
    --eval_steps 500 \
    --bf16 \
    --save_total_limit 3 \
    --save_only_model
```

### Dry-run 验证结果

**成功。** 用 `--max_steps 3` + `CUDA_VISIBLE_DEVICES=0` 在 GPU 0 上完成 3 步训练，ess_only weighting 正常工作（b 值自动搜索，ESS≈2.0，alpha_eff 在 0.12-0.94 范围波动），模型保存正常。

### 注意事项

1. **GPU 资源**：当前 4 张 GPU 均有负载（各占 ~46.5 GiB），每张有 ~50 GiB 空闲。Qwen3-0.6B 单卡训练需 ~4 GiB 显存，资源充足，但需用 `CUDA_VISIBLE_DEVICES` 指定空闲 GPU 避免与现有实验冲突。
2. **W&B**：上述命令未启用 W&B（与 seed42 一致）。如需 W&B 记录，加 `--use_wandb --wandb_project provenance-weight-training --wandb_run_name ess_only_seed123`。
3. **eval_data_path**：seed42 未使用 eval set。如需与 adaptive_v2 对齐加入 eval，加 `--eval_data_path data/human/eval_holdout.jsonl`。
4. **预计时长**：seed42 用了 12978 秒（~3.6 小时），新 seed 同配置，耗时相近。两个 seed 可分别放不同 GPU 并行跑。

---
