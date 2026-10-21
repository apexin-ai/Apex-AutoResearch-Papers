# prep pi05 crm training setup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_pi05-crm-training-setup_20260524T082515_result.json`
- **Structured JSON:** [`3d09dd3d6fff4ed17404.json`](../../sessions/3d/3d09dd3d6fff4ed17404.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕，汇报如下：

---

## 1. GPU 占用状态

| GPU | 进程 | PID | 显存占用 | 状态 |
|-----|------|-----|---------|------|
| 0 | pi05 object precompute | 113456 | 9884/24564 MiB | 运行中 |
| 1 | long-vla-s47-r2 | 278846 | 4930/24564 MiB | 运行中 |
| 2 | goal-vla-s47 | 279117 | 2799/24564 MiB | 运行中 |
| 3 | pi05 long precompute | 114507 | 9874/24564 MiB | 运行中 |

**4 卡全部占用。** CRM 训练极轻量（模型 ~500K 参数，训练时 GPU 显存 <2GB），可以和 GPU 1 或 GPU 2 共享，也可以等 GPU 0 释放（之前说约 2h 后完成）。

## 2. 代码兼容性 — 无需修改

代码**已完全支持 π0.5**：
- `--reuse_merged_cache` 标志已存在，`--merged_cache_dir` 默认就是 `/root/autodl-tmp/crm_cache_pi05_2048/`
- `--obs_dim` 可配置，传 2048 即可
- `MultiScaleCRM` 自动处理单尺度 fallback（π0.5 是 1×2048 而非 SmolVLA 的 4×960）
- `action_dim = H_EFF(5) × CORRECTION_DIM(6) = 30`，与 cache 格式完全匹配
- `set_normalization_stats` 正确处理 1D obs stats → broadcast 到 (4, 2048)

## 3. Cache 完整性 — 完整

| Benchmark | 样本数 | obs_features | k_samples | expert_actions | manifest |
|-----------|--------|-------------|-----------|----------------|----------|
| spatial | 60,250 | (60250, 2048) | (60250, 10, 5, 6) | (60250, 5, 6) | K=10, obs_dim=2048, action_dim=6, h_eff=5 |
| goal | 61,728 | (61728, 2048) | (61728, 10, 5, 6) | (61728, 5, 6) | K=10, obs_dim=2048, action_dim=6, h_eff=5 |

## 4. 训练命令

**Spatial CRM（GPU X 可用时）：**
```bash
cd /root/acr-vla-conformal-refinement && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=X nohup python src/train_crm_k1.py \
  --benchmark spatial \
  --reuse_merged_cache \
  --obs_dim 2048 \
  --output_dir /root/autodl-tmp/checkpoints/crm_pi05_k1_multiscale/spatial/ \
  --epochs 50 \
  --batch_size 256 \
  --lr 1e-3 \
  --wandb_run_name crm-pi05-k1-spatial \
  --seed 42 \
  > /tmp/crm_pi05_spatial.log 2>&1 &
```

**Goal CRM（GPU Y 可用时）：**
```bash
cd /root/acr-vla-conformal-refinement && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=Y nohup python src/train_crm_k1.py \
  --benchmark goal \
  --reuse_merged_cache \
  --obs_dim 2048 \
  --output_dir /root/autodl-tmp/checkpoints/crm_pi05_k1_multiscale/goal/ \
  --epochs 50 \
  --batch_size 256 \
  --lr 1e-3 \
  --wandb_run_name crm-pi05-k1-goal \
  --seed 42 \
  > /tmp/crm_pi05_goal.log 2>&1 &
```

关键参数说明：
- `--loss_mode multi` 是默认值（L2 + direction + triplet + magnitude），无需显式指定
- `--merged_cache_dir` 默认已指向 `/root/autodl-tmp/crm_cache_pi05_2048/`，无需显式指定
- batch_size=256（SmolVLA CRM 用 512，π0.5 obs 更大所以降到 256 更安全）
- CRM 可以和其他进程共享 GPU（GPU 2 剩余 ~21GB 足够）

---
