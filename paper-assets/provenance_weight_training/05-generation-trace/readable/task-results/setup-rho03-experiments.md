# setup rho03 experiments

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_rho03_experiments_20260522T183602_result.json`
- **Structured JSON:** [`dd0205ecf1dd9f296c27.json`](../../sessions/dd/dd0205ecf1dd9f296c27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完成。汇总结果：

---

## 产出

### 1. 数据路径
**已生成**: `data/scored_data_rho03.jsonl`
- 235555 行，ρ=0.3000（70667 synthetic + 164888 human）
- 712MB，从 scored_data.jsonl 重采样，q_scores 复用已有评分
- 生成脚本: `scripts/prepare_rho03_data.py`

### 2. 磁盘空间
/root/autodl-tmp: 64GB 可用（75% 已用），充足。

### 3. 两个训练命令

**实验 1 — rho03_adaptive_seed42 (cuda:0)**:
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_rho03.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/rho03_adaptive_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.3 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing"
```

**实验 2 — rho03_uniform_seed42 (cuda:1)**:
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_rho03.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/rho03_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.3 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing"
```

### 4. 注意事项
- 最近成功的 ρ=0.4 实验（bs8_nmin4_adaptive_seed42）用的是 `batch_size=8, grad_accum=2, n_min=4, max_steps=6103`。上面按任务模板用 `batch_size=4, grad_accum=4`（effective batch 同为 16，n_min 默认 2）。如需对齐最新配置请调整。
- `--contamination_ratio 0.3` 仅为元数据标记，不影响训练逻辑。
- `--num_train_tokens 200000000` 等效 max_steps=6103。

---
