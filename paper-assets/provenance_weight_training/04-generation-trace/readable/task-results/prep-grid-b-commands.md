# prep grid b commands

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_grid_b_commands_20260516T010253_result.json`
- **Structured JSON:** [`723c61929434cb70303e.json`](../../sessions/72/723c61929434cb70303e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。

---

## 验证报告

### 1. --eval_steps 支持 grid 模式：**是**
- Line 270: argparse 定义 `--eval_steps`，默认 500
- Line 357: 传入 TrainingArguments：`eval_steps=args.eval_steps if eval_dataset else None`
- eval_steps 与 weighting_method 无关，对所有模式（包括 grid）生效
- **注意**：eval_steps 仅在有 eval_dataset 时生效（否则设为 None）。若训练命令未指定 eval 数据集，该参数不会实际触发评估，但传入不会报错

### 2. --tau 在 grid 模式下生效：**是**
- Line 94: 构造函数 `__init__(self, weighting_method, tau, ...)`
- Line 144: `elif self.weighting_method == "grid":` 分支
- Line 152: `b_val = find_optimal_b(q_scores, tau=self.tau, ...)` — grid 模式直接使用 tau

### 3. 数据文件确认
- `scored_data.jsonl` — 930M ✓
- `scored_data_filtered_q05.jsonl` — 477M ✓

### 4. 磁盘空间：**充足**
- 数据盘 250G，已用 153G，剩余 **98G**
- 3 个实验（save_total_limit=3，Qwen3-0.6B ~1.2G/ckpt）预计占用 ~11G，空间充足

### 5. 三条完整训练命令

**grid_b0_3_seed42:**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_3_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.3 --contamination_ratio 0.4 --num_train_tokens 200000000 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --eval_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model
```

**grid_b0_1_seed42:**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_1_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.1 --contamination_ratio 0.4 --num_train_tokens 200000000 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --eval_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model
```

**detect_remove_baseline_seed42:**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir output/models/detect_remove_baseline_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --eval_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model
```

---
