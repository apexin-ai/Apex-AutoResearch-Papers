# bjb2-28827 GPU 诊断报告

**时间**: 2026-05-18 07:00 UTC

## GPU 状态总览

| GPU | 显存占用 | GPU-Util | PID | 实验 | 状态 |
|-----|---------|----------|-----|------|------|
| 0 | 1MiB / 24564MiB | 0% | - | train-crm-k1-v2 已完成 | **空闲可用** |
| 1 | 4735MiB | 18% | 448782 | mag_obs_only_norm01_seed47 | 运行中 |
| 2 | 2875MiB | 18% | 404983 | eval_object_perdof_norm02_seed47 | 运行中 |
| 3 | 4268MiB | 18% | 449068 | mag_obs_only_norm01_seed46 | 运行中 |
| 4 | 2410MiB | 19% | 389051 | eval_object_perdof_norm02_seed46 | 运行中 |
| 5 | 1MiB / 24564MiB | 0% | - | mag_perdof_norm02_seed43_r3 已被杀 | **空闲可用** |

## cuda:0 状态

**空闲可用。** train-crm-k1-v2 训练已完成（50/50 epochs, best val_loss=0.007199），tmux session 已自动退出。checkpoint 保存在 `/root/autodl-tmp/checkpoints/crm_k1/`。

## cuda:5 状态

**空闲可用。** `mag_perdof_norm02_seed43_r3` 被 SIGKILL (exit 137) 杀死于 2026-05-17T22:59:24Z。

## PID 749540 (eval-perdof-object-norm02-seed45-r3)

**已死亡。** `ps -p 749540` 无结果，nvidia-smi 中无记录，无 exit file。进程已不存在。

## Registry 不一致项

| Registry 名称 | Registry 状态 | 实际状态 | 说明 |
|---------------|-------------|---------|------|
| mag_perdof_norm02_seed43_r3 | RUNNING | **KILLED** | exit 137 (SIGKILL) @ 2026-05-17T22:59Z，GPU 5 已释放 |
| mag_obs_only_norm01_seed47 | RUNNING | RUNNING | 正常，GPU 1，有 tmux session |
| mag_obs_only_norm01_seed46 | RUNNING | RUNNING | 正常，GPU 3，有 tmux session |
| eval-perdof-object-norm02-seed45-r3 | ? | **DEAD** | PID 749540 不存在，无 exit file |

## 各实验进度估算

所有 eval 实验均为 object benchmark (10 tasks, 每 task 10 rollouts)。

| 实验 | GPU | 已完成 tasks | 当前进度 | 估算完成度 |
|------|-----|-------------|---------|-----------|
| eval_object_perdof_norm02_seed46 | 4 | 7/10 | task 8 rollout 5/10 | ~75% |
| eval_object_perdof_norm02_seed47 | 2 | 6/10 | task 7 开始中 | ~65% |
| mag_obs_only_norm01_seed46 | 3 | 3/10 | task 4 开始中 | ~30% |
| mag_obs_only_norm01_seed47 | 1 | 2/10 | task 3 rollout 9/10 | ~29% |

## tmux sessions

- `mag_obs_only_norm01_seed46` (创建于 02:04)
- `mag_obs_only_norm01_seed47` (创建于 02:04)
- `train-crm-k1-v2` — 已不存在（训练完成后自动退出）

## 可用资源

- **GPU 0 和 GPU 5 空闲**，可立即分配新实验
- GPU 1-4 预计还需数小时完成（obs_only 进度较慢，约 30%）
