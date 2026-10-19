# GPU Status: bjb1-32546 (6×RTX 4090)
**Timestamp**: 2026-05-23 11:29 CST

## GPU 使用状态

| GPU | VRAM 占用 | GPU-Util | PID | 任务 | 日志 |
|-----|----------|----------|-----|------|------|
| 0 | 6306/24564 MiB | 26% | 625804 | eval crm_obs_only spatial (norm=0.2) | crm_norm02_spatial_s42.log |
| 1 | 6212/24564 MiB | 26% | 626005 | eval adaptive_conformal_crm spatial (τ=0.15) | adapt_tau015_spatial_s42.log |
| 2 | 6212/24564 MiB | 23% | 626274 | eval adaptive_conformal_crm spatial (τ=0.25) | adapt_tau025_spatial_s42.log |
| 3 | 544/24564 MiB | 10% | 548664 | **train_crm** 4-suite unified (epoch 38/50) | crm_unified_4suite_r4/train_resume.log |
| 4 | 6212/24564 MiB | 21% | 626543 | eval adaptive_conformal_crm spatial (τ=0.35) | adapt_tau035_spatial_s42.log |
| 5 | 5731/24564 MiB | 36% | 626812 | eval crm_obs_only object (norm=0.05) | obj_crm005_s42.log |

## 空闲 GPU

**无空闲 GPU。** 全部 6 块 GPU 均被占用。

## 训练进度: train-crm-unified-4suite-r5-resumed

- **配置**: 4-suite (object, spatial, goal, long), obs_only, 50 epochs, bs=32, lr=1e-3
- **恢复自**: checkpoint_epoch0032.pt（09:16 启动）
- **当前进度**: epoch 38, batch ~2250/6316
- **已完成 epoch 的 val_loss**:
  - Epoch 33: val_loss=0.006031
  - Epoch 34: val_loss=0.006011
  - Epoch 35: val_loss=0.006015
  - Epoch 36: val_loss=0.005962
  - Epoch 37: val_loss=0.005903 ← 持续下降
- **当前 batch loss**: ~0.008-0.015 范围
- **速度估计**: ~25 min/epoch（5 epochs in ~133 min）
- **剩余**: ~12.6 epochs × 25 min ≈ **~5.3 小时**（预计 ~16:45 完成）

## CRM Eval 状态

5 个新 eval 进程于 11:24 启动，均处于早期阶段（task 1/10）：

| Eval | GPU | 模式 | 基准 | 当前进度 | 早期表现 |
|------|-----|------|------|---------|---------|
| crm_norm02_spatial | 0 | crm_obs_only (norm=0.2) | spatial | task 1, rollout 15/20 | 15/15 成功 |
| adapt_tau015_spatial | 1 | adaptive_conformal_crm (τ=0.15) | spatial | task 1, rollout 15/20 | 15/15 成功 |
| adapt_tau025_spatial | 2 | adaptive_conformal_crm (τ=0.25) | spatial | task 1, rollout 10/20 | 10/10 成功 |
| adapt_tau035_spatial | 4 | adaptive_conformal_crm (τ=0.35) | spatial | task 1, rollout 10/20 | 10/10 成功 |
| obj_crm005 | 5 | crm_obs_only (norm=0.05) | object | task 1, rollout 5/20 | 2/5 成功 |

之前的 3-direction eval (dirA_norm005/norm01/norm03, dirB_adaptive, dirC_reconvla) 已于 11:10-11:19 完成。

## 已完成的 eval 结果文件（今日）

- `eval_spatial_crm_obs_only_norm0.05_seed42.json` (11:10)
- `eval_spatial_crm_obs_only_norm0.1_seed42.json` (11:14)
- `eval_spatial_reconvla_seed42.json` (11:17)
- `eval_spatial_adaptive_conformal_crm_tau0.074855_seed42.json` (11:18)

## 可部署实验建议

当前无空闲 GPU。可安排的实验需等待：
1. **eval 完成后**（预计 1-2 小时）：GPU 0/1/2/4/5 释放 → 可用于 CRM goal eval、更多 seed 的 spatial/object eval
2. **训练完成后**（预计 ~16:45）：GPU 3 释放 → 可用于新的 4-suite CRM eval 或下一轮训练
