# bjb1-18228 部署报告

**时间**: 2026-05-17 13:57 UTC
**服务器**: bjb1-18228 (4x GPU)

## 发现

到达时 4 张 GPU **已全部被占用**，运行的正是本次任务要求部署的 4 个实验。另一个 Worker 已于 21:35-21:37 完成提交，但未将 registry 状态同步为 RUNNING。

## 部署状态

| GPU | exp_id | PID | 启动时间 | 实验内容 | 操作 |
|-----|--------|-----|----------|----------|------|
| cuda:0 | eval-perdof-object-norm02-seed45-r2 | 634438 | 21:35:37 | perdof ε=0.2 seed45 K=10 | registry PREPARING→QUEUED→RUNNING |
| cuda:1 | eval-obs-only-object-norm005-seed43-r3 | 633649 | 21:35:14 | obs_only ε=0.05 seed43 K=10 | registry PREPARING→QUEUED→RUNNING |
| cuda:2 | eval-obs-only-object-norm02-k5-seed42 | 633662 | 21:35:16 | obs_only ε=0.2 seed42 K=5 | registry QUEUED→RUNNING |
| cuda:3 | eval-obs-only-object-norm02-k20-seed42 | 636638 | 21:37:48 | obs_only ε=0.2 seed42 K=20 | registry QUEUED→RUNNING |

## 异常记录

1. **exp_id 不匹配**: 任务要求 `eval-perdof-object-norm02-seed45-r3`，但服务器上实际提交的 exp_id 是 `eval-perdof-object-norm02-seed45-r2`。已按实际 exp_id 更新 registry。
2. **LIBERO 进程数**: 检测到 16 个 evaluate.py 进程（4 个主进程各有子进程），符合 4 实验预期。
3. **tmux 无 session**: `tmux ls` 返回空，但进程正常运行（agent-ml 框架 detach 后 tmux server 可能已退出）。
4. **无需重新部署**: 所有实验已在运行，仅需 registry 同步。

## Checkpoint 确认

- `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt` (327,198 params) ✓
- `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt` ✓
- `/root/acr-vla-conformal-refinement/src/evaluate.py` ✓
