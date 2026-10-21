# CRM Eval Fix Status — 2026-05-23 07:31 UTC

## 问题
Spatial/Goal CRM eval 命令错误使用了 `--input_mode obs_only`（train_crm.py 参数，evaluate.py 不接受），导致 argparse 报错。由于 `tee` 管道掩盖了非零退出码，`&&` 链继续执行了 VLA-only baseline。

## 正确命令模板（从 bjb2-28827 object CRM eval 获取）

```bash
python -u src/evaluate.py \
    --mode crm_obs_only \
    --model smolvla \
    --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt \
    --benchmark {suite} \
    --seed {seed} \
    --n_rollouts 20 --K 10 --obs_dim 960 \
    --n_action_steps 50 --max_steps {280 for spatial, 300 for goal}
```

**⚠️ 无 `--input_mode obs_only`！**

VLA-only baseline 链式命令使用 `--mode vla_only --K 1`，去掉 `--crm_checkpoint` 和 `--obs_dim`。

使用 `PIPESTATUS[0]` 捕获 python 退出码，防止 tee 掩盖错误。

## bjb1-32546 部署（新部署，已修复）

| GPU | tmux session | 任务 | PID | 状态 |
|-----|-------------|------|-----|------|
| cuda:0 | crm_spatial_seed42 | Spatial CRM seed42 → VLA-only | 494055 | ✅ 运行中 |
| cuda:1 | crm_spatial_seed43 | Spatial CRM seed43 → VLA-only | 494320 | ✅ 运行中 |
| cuda:2 | crm_spatial_seed44 | Spatial CRM seed44 → VLA-only | 494589 | ✅ 运行中 |
| cuda:3 | train-crm-unified-4suite-r4 | CRM 4-suite 训练 | — | 🔒 不动 |
| cuda:4 | crm_goal_seed42 | Goal CRM seed42 → VLA-only | 494865 | ✅ 运行中 |
| cuda:5 | crm_goal_seed43 | Goal CRM seed43 → VLA-only | 495134 | ✅ 运行中 |

**Goal seed44**: 无可用 GPU（cuda:3 训练中）。待 bjb2-28827 cuda:3/4/5 的 VLA-only spatial 完成后，可在那边部署。

日志路径: `/root/autodl-tmp/logs/crm_{spatial,goal}_seed{42,43,44}.log`

## bjb2-28827 状态（未修改）

| GPU | 任务 | 状态 |
|-----|------|------|
| cuda:0 | Object CRM seed42 | ✅ 正常运行（task 1/10, rollout 15/20）|
| cuda:1 | Object CRM seed43 | ✅ 正常运行（task 1/10, rollout 15/20）|
| cuda:2 | Object CRM seed44 | ✅ 正常运行（task 1/10, rollout 15/20）|
| cuda:3 | VLA-only Spatial seed42 | ⏳ 跑中（task 1/10 完成，还需数小时）|
| cuda:4 | VLA-only Spatial seed43 | ⏳ 跑中（task 2/10）|
| cuda:5 | VLA-only Spatial seed44 | ⏳ 跑中（task 1/10 完成）|

说明：cuda:3,4,5 原本应跑 spatial CRM eval，因 `--input_mode obs_only` 错误，CRM 失败后直接跑了 VLA-only baseline。VLA-only 数据仍然可用，让其跑完。

## 异常
- bjb1-32546 上之前有错误的 goal CRM eval sessions（crm_goal_s42/s43/s44），已 kill
- bjb1-32546 cuda:3 训练占用仅 542MiB，可能是 CPU 阶段或 checkpoint 保存间隙
- Goal seed44 CRM eval 暂时无 GPU 可用
