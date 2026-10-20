# status westd 47453 progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westd-47453-progress_20260516T141909_result.json`
- **Structured JSON:** [`56e3c10e4ed8a37481b3.json`](../../sessions/56/56e3c10e4ed8a37481b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。

---

## Part 1: 实验进度

### 1. cuda:0 — threshold_q07 (PID 324550) ✅ ALIVE
- **Step**: 3999 / 6103 (65.5%)
- **已运行**: 3h 36min（从 checkpoint-2000 恢复）
- **速度**: ~6.49 s/step（有效步 1999 步用了 3.6h）
- **剩余**: 2104 steps × 6.49s ≈ **3.8h**
- **预计完成**: ~May 17 02:00
- **最新 checkpoint**: checkpoint-3500

### 2. cuda:1 — rho02_uniform (PID 316980) ✅ ALIVE
- **Step**: 2674 / 6103 (43.8%)
- **已运行**: 5h 14min
- **速度**: ~2.12 s/it（进度条显示）
- **剩余**: 3429 steps × 2.12s ≈ **2.0h**
- **预计完成**: ~May 17 00:20
- **最新 checkpoint**: checkpoint-2500

### 3. cuda:2 — batch_adaptive_tau_rho04 (PID 326274) ✅ ALIVE
- **Step**: 1762 / 6103 (28.9%)
- **已运行**: 3h 17min
- **速度**: ~2.27 s/it（进度条显示）
- **剩余**: 4341 steps × 2.27s ≈ **2.7h**
- **预计完成**: ~May 17 01:00
- **最新 checkpoint**: checkpoint-1500

### 4. cuda:3 — threshold_q03 (PID 325196) ✅ ALIVE
- **Step**: 1999 / 6103 (32.7%)
- **已运行**: 3h 33min
- **速度**: ~6.39 s/step
- **剩余**: 4104 steps × 6.39s ≈ **7.3h**
- **预计完成**: ~May 17 05:30
- **最新 checkpoint**: checkpoint-1500

> **注意**: threshold_q07 和 threshold_q03 的速度（~6.4 s/step）明显慢于 rho02_uniform 和 batch_adaptive（~2.2 s/step），约慢 3x。可能与数据过滤后的 dataloader 行为有关。

---

## Part 2: random_reweight_v2 脚本确认

脚本完整内容：

```bash
#!/bin/bash
# Random reweighting baseline v2 (seed=42) — fixed checkpoint saving
# Fix: WANDB_MODE=disabled, output to data disk, explicit eval batch size
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export WANDB_MODE=disabled
export CUDA_VISIBLE_DEVICES=0
cd /root/provenance_weight_training

python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --eval_data_path data/human/eval_holdout.jsonl \
    --output_dir /root/autodl-tmp/output/models/random_reweight_seed42 \
    --model_name models/Qwen/Qwen3-0.6B \
    --weighting_method random \
    --contamination_ratio 0.4 \
    --tau 0.8 \
    --n_min 2 \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --learning_rate 5e-5 \
    --max_length 2048 \
    --seed 42 \
    --eval_steps 500 \
    --save_steps 500 \
    --logging_steps 10 \
    --bf16 \
    --save_total_limit 3 \
    --save_only_model

echo "DONE: random_reweight_v2 seed42"
```

检查结果：

| 检查项 | 状态 |
|--------|------|
| WANDB_MODE=disabled | ✅ 正确 |
| output_dir 在数据盘 | ✅ `/root/autodl-tmp/output/models/random_reweight_seed42` |
| CUDA_VISIBLE_DEVICES | `0` — 当前 cuda:0 被 threshold_q07 占用，**需等其完成后再启动** |
| 无 --use_wandb 等参数 | ✅ 无 wandb 相关训练参数 |

---
