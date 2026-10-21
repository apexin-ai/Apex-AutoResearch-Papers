# bjb1-18228 诊断报告

**时间**: 2026-05-18 06:59 UTC

## 服务器状态
- **健康**: 是
- **Driver**: NVIDIA 580.105.08, CUDA 13.0
- **GPU**: 4x RTX 4090 (24GB)

## GPU 状态

| GPU | 显存占用 | 利用率 | 状态 | 进程 |
|-----|---------|--------|------|------|
| 0 | 3342/24564 MiB | 22% | 占用 | PID 713405 - evaluate.py crm_obs_only, object, seed42, K=5 |
| 1 | 4/24564 MiB | 0% | **空闲** | - |
| 2 | 4/24564 MiB | 0% | **空闲** | - |
| 3 | 5200/24564 MiB | 23% | 占用 | PID 749547 - evaluate.py crm_perdof, object, seed45, K=10 |

## 可用 GPU
**GPU 1, 2** 完全空闲，可立即提交新实验。

## PID 检查
- **476529**: 已死亡（不存在）
- **449068**: 已死亡（不存在）

Cron 中记录的这两个 PID 需要清理。

## 活跃进程
1. **PID 713405** (GPU 0): `evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint crm_v3_norm/obs_only/crm_best.pt` — 已运行 ~7h
2. **PID 749547** (GPU 3): `evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint crm_v3_norm/perdof/crm_best.pt` — 已运行 ~2h

## tmux 会话
- `eval-obs-k5` (1 window) — 对应 GPU 0 的 obs_only 评估

## 近期活跃日志
- `eval_object_obs_only_norm02_k5_seed42.log` — 最后写入 06:57
- `eval_object_perdof_norm02_seed45_r3.log` — 最后写入 06:59
- `openvla_action_analysis.log` — 最后写入 06:47

## 结论
服务器健康可用。GPU 1、2 空闲，可安全提交新实验。PID 476529/449068 已死亡，cron 记录需更新。
