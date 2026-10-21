# GPU Scan R7 — 2026-05-25 03:30 UTC

## 1. 服务器 GPU 状态总览

### bjb2-40593 (1× A6000 24GB)

| GPU | Util | Mem Used | Experiment |
|-----|------|----------|------------|
| 0 | 11% | 3299/24564 MiB | eval-adaptive-k5-spatial-s42 (K=5) |

**状态**: K=5 spatial 实验仍在运行中，当前进度约 7/10 tasks 完成。

### bjb1-18228 (4× A6000 24GB)

| GPU | Util | Mem Used | Experiment |
|-----|------|----------|------------|
| 0 | 10% | 580/24564 MiB | precompute pi05 long K=10 |
| 1 | 0% | 0 MiB | **IDLE** |
| 2 | 0% | 0 MiB | **IDLE** |
| 3 | 36% | 9883/24564 MiB | train-crm-pi05-unified-3suite-r2 |

**CRM 训练进度**: Epoch 25/50, train_loss=0.008440, **best val_loss=0.004854** (epoch 24), lr=5.31e-04
- 收敛良好，val_loss 持续下降
- 预计还需 ~8-10 小时完成

**Precompute**: pi05 long benchmark K=10 仍在运行（已运行 62h+, CPU 131%）

**已完成**: eval-long-vla-s47: 59.5% (119/200)

### bjb1-32546 (6× A6000 24GB)

| GPU | Util | Mem Used | Experiment |
|-----|------|----------|------------|
| 0 | 0% | 2 MiB | **IDLE** |
| 1 | 22% | 2383/24564 MiB | eval-supp-adapt-tau025-obj-s50 (running) |
| 2 | 0% | 2 MiB | **IDLE** |
| 3 | 0% | 2 MiB | **IDLE** |
| 4 | 0% | 2 MiB | **IDLE** |
| 5 | 0% | 2 MiB | **IDLE** |

**eval-a1-baseline-object-s42**: 未在运行（已确认 A1 方案放弃 per D137）

### bjb2-28827 (6× A6000 24GB)

| GPU | Util | Mem Used | Experiment |
|-----|------|----------|------------|
| 0 | 0% | 1 MiB | **IDLE** |
| 1 | 0% | 1 MiB | **IDLE** |
| 2 | 20% | 13966/24564 MiB | eval-pi05-reconvla-goal-s42 |
| 3 | 45% | 14088/24564 MiB | eval-pi05-reconvla-object-s42 |
| 4 | 0% | 1 MiB | **IDLE** |
| 5 | 0% | 1 MiB | **IDLE** |

**已完成**: eval-supp-adapt-tau025-spatial-s48: **81.0% (162/200)**, mean_unc=0.1853, trigger_rate=19.8%

### cqa1-32758 (6× A6000 24GB)

| GPU | Util | Mem Used | Experiment |
|-----|------|----------|------------|
| 0-5 | 0% | 0 MiB | **ALL IDLE** |

全部 6 张 GPU 空闲，无任何实验在运行。

---

## 2. 已完成实验结果收割

### π0.5 VLA-only baselines (bjb1-32546, 已完成)

| exp_id | benchmark | seed | success_rate | json_path |
|--------|-----------|------|-------------|-----------|
| eval-pi05-vla-only-object-s42-v2 | object | 42 | **96.5%** (193/200) | eval_object_vla_only_pi05_seed42.json |
| eval-pi05-vla-only-spatial-s43-v2 | spatial | 43 | **96.0%** (192/200) | eval_spatial_vla_only_pi05_seed43.json |
| eval-pi05-vla-only-goal-s42-v2 | goal | 42 | **95.5%** (191/200) | eval_goal_vla_only_pi05_seed42.json |
| eval-pi05-vla-only-goal-s43-v2 | goal | 43 | **97.0%** (194/200) | eval_goal_vla_only_pi05_seed43.json |
| eval-pi05-vla-only-spatial-s42-v2 | spatial | 42 | ⚠️ **0.0%** (0/200) | eval_spatial_vla_only_pi05_seed42.json |

### Tau sweep (bjb1-32546, 已完成)

| exp_id | tau | benchmark | success_rate | trigger_rate |
|--------|-----|-----------|-------------|-------------|
| eval-tau010-spatial-s42 | 0.10 | spatial | 79.0% (158/200) | 75.2% |
| eval-tau020-spatial-s42 | 0.20 | spatial | 81.0% (162/200) | 26.6% |
| eval-tau030-spatial-s42 | 0.30 | spatial | 80.5% (161/200) | 16.7% |

### CRM reeval (bjb1-32546, 已完成)

| exp_id | mode | benchmark | success_rate |
|--------|------|-----------|-------------|
| eval-crm-obj-s47-reeval | crm_obs_only (norm=0.05) | object | 82.5% (165/200) |

### Supplementary seeds — VLA-only (cqa1-32758, 已完成)

| exp_id | benchmark | seed | success_rate |
|--------|-----------|------|-------------|
| eval-supp-vla-only-obj-s48 | object | 48 | 79.0% (158/200) |
| eval-supp-vla-only-obj-s49 | object | 49 | 75.5% (151/200) |
| eval-supp-vla-only-spatial-s48 | spatial | 48 | 79.5% (159/200) |
| eval-supp-vla-only-spatial-s49 | spatial | 49 | 78.5% (157/200) |
| eval-supp-vla-only-goal-s48 | goal | 48 | 85.0% (170/200) |
| eval-supp-vla-only-goal-s49 | goal | 49 | 82.0% (164/200) |

### Supplementary — Long horizon (cqa1-32758 + bjb1-18228, 已完成)

| exp_id | mode | seed | success_rate | trigger_rate |
|--------|------|------|-------------|-------------|
| eval-supp-long-adapt-tau025-s47 | adaptive_conformal_crm | 47 | 56.5% (113/200) | 3.8% |
| eval-supp-long-vla-only-s47 | vla_only | 47 | 58.5% (117/200) | — |
| eval-long-vla-s47 (bjb1-18228) | vla_only | 47 | 59.5% (119/200) | — |

### Supplementary — Adaptive spatial (bjb2-28827, 已完成)

| exp_id | mode | seed | success_rate | trigger_rate |
|--------|------|------|-------------|-------------|
| eval-supp-adapt-tau025-spatial-s48 | adaptive_conformal_crm | 48 | **81.0%** (162/200) | 19.8% |

---

## 3. 空闲 GPU 列表

| 服务器 | 空闲 GPU IDs | 数量 |
|--------|-------------|------|
| bjb1-18228 | 1, 2 | 2 |
| bjb1-32546 | 0, 2, 3, 4, 5 | 5 |
| bjb2-28827 | 0, 1, 4, 5 | 4 |
| cqa1-32758 | 0, 1, 2, 3, 4, 5 | 6 |
| **Total** | | **17 GPUs** |

---

## 4. π0.5 CRM 训练进度 (bjb1-18228)

- **实验**: train-crm-pi05-unified-3suite-r2
- **配置**: 3 benchmarks (object+spatial+goal), obs_dim=2048, batch=256, lr=1e-3, 50 epochs
- **当前**: Epoch 25/50 (50% complete)
- **Best val_loss**: 0.004854 @ epoch 24 (持续改善中)
- **Train loss**: 0.008440 (稳定下降)
- **Learning rate**: 5.31e-04 (cosine schedule)
- **ETA**: ~8-10 hours to completion

---

## 5. 异常 / 需注意事项

### ⚠️ CRITICAL: eval-pi05-vla-only-spatial-s42-v2 OOM 失败
- **服务器**: bjb1-32546
- **原因**: CUDA out of memory at step 0，所有 200 rollouts 全部失败
- **影响**: spatial s42 的 π0.5 baseline 数据缺失
- **建议**: 需要在单独 GPU 上重跑（确保无其他进程共享显存）

### ⚠️ cqa1-32758 完全空闲
- 6 张 A6000 无任何实验运行
- 可调度新实验

### ℹ️ bjb1-18228 precompute 长时间运行
- pi05 long benchmark K=10 precompute 已运行 62+ 小时
- 占用 GPU 0（低显存 580 MiB，CPU-bound）

### ℹ️ bjb2-40593 K=5 实验进度
- eval-adaptive-k5-spatial-s42 仍在运行
- 已完成的 tasks 中表现参差不齐（0%~100%）
- 部分难题（on_the_ramekin）完全失败 0/20

### ℹ️ Long horizon 结果
- adaptive_conformal_crm 在 long 上只有 56.5%，低于 vla_only 的 58.5-59.5%
- trigger_rate 仅 3.8%，CRM 几乎未触发修正
