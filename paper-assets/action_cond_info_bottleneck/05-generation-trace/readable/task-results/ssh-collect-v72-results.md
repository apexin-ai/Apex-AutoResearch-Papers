# ssh collect v72 results

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect_v72_results_20260517T222842_result.json`
- **Structured JSON:** [`035c507ba1a5ba230173.json`](../../sessions/03/035c507ba1a5ba230173.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总报告：

---

## 1. 进程状态

**仍在运行。** PID 40598 (GPU 0, α=0.0) 和 PID 44022 (GPU 1, α=1.0) 均在跑 libero_10（第 4 个也是最后一个 suite）。前 3 个 suite 已完成。

## 2. libero_10 结果

**尚未产出。** 两个进程正在执行 libero_10 评估，eval_info.json 尚未写出。

## 3. 已完成的 3-suite 结果

| Suite | α=0.0 | α=1.0 |
|-------|--------|--------|
| libero_spatial | **59.40%** | **61.00%** |
| libero_object | **65.60%** | **66.20%** |
| libero_goal | **78.60%** | **78.00%** |
| libero_10 | (running) | (running) |
| 3-suite avg | **67.87%** | **68.40%** |

4-suite avg 待 libero_10 完成后计算。

## 4. v7.3 LoRA 代码验证

**通过。**
- `ACIBConfig(freeze_mode='connector_lora', lora_rank=8, lora_scale=1.0)` 正常创建
- `ACIBConfig(freeze_mode='connector_only')` 正常创建
- `LoRALinear` 类（定义在 `acib/acib_policy.py`）：forward 正常，zero-init B=0 验证通过（diff=0.00e+00）
- `test_v73_t2.py` 需加载完整模型（>30s），因 SSH 超时和 GPU 被占用无法完整运行，但轻量级功能验证已通过

## 5. 训练脚本完整内容

### run_v73_connector_lora.sh
```bash
#!/bin/bash
# v7.3: connector LoRA + scorer
# Trainable: LoRA A+B (~20K) + scorer (~0.1M), all else frozen
set -euo pipefail
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/acib
export WANDB_MODE=disabled MUJOCO_GL=egl PYOPENGL_PLATFORM=egl

SEED=${1:-42}
GPU=${2:-0}
OUTPUT_DIR="/root/autodl-tmp/acib_v73_connector_lora_seed${SEED}"

python3 -u scripts/train_acib.py \
  --model_id lerobot/smolvla_libero \
  --dataset_id lerobot/libero \
  --data_root /root/autodl-tmp/libero_dataset \
  --hidden_dim 64 \
  --alpha 0.01 --beta 0.01 --beta_warmup_steps 1000 \
  --mode soft --condition_source language --conditioning_mode concat \
  --lambda_contrastive 0.1 --diversity_lambda 0.1 --lambda_ent 0.0 --lambda_drift 0.0 \
  --steps 20000 --batch_size 64 --lr 5e-5 --warmup_steps 1000 --grad_clip 1.0 \
  --save_freq 5000 --dtype bfloat16 \
  --gpu ${GPU} --seed ${SEED} \
  --freeze_mode connector_lora --lora_rank 8 --lora_scale 1.0 \
  --output_dir "${OUTPUT_DIR}"
```

### run_connector_only.sh
```bash
#!/bin/bash
# Connector-only ablation: only task loss, no scorer/contrastive/IB
# Purpose: isolate whether v7.2 gains come from connector tuning vs scorer-driven learning
SEED=${1:-42}
GPU=${2:-0}
OUTPUT_DIR="/root/autodl-tmp/acib_connector_only_seed${SEED}"

cd /root/acib
/root/miniconda3/bin/python3 -u scripts/train_acib.py \
  --model_id lerobot/smolvla_libero \
  --dataset_id lerobot/libero \
  --data_root /root/autodl-tmp/libero_dataset \
  --hidden_dim 64 \
  --alpha 0.01 --beta 0.01 --beta_warmup_steps 1000 \
  --mode soft --condition_source language --conditioning_mode concat \
  --lambda_contrastive 0.0 --diversity_lambda 0.0 --lambda_ent 0.0 \
  --steps 20000 --batch_size 64 --lr 5e-5 --warmup_steps 1000 --grad_clip 1.0 \
  --save_freq 5000 --dtype bfloat16 \
  --gpu ${GPU} --seed ${SEED} \
  --freeze_mode connector_only \
  --lambda_drift 0.0 \
  --output_dir "${OUTPUT_DIR}"
```

---
