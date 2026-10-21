# CRM Eval Cron 监控状态

**时间**: 2026-05-23 ~07:45 UTC

## bjb2-28827 进程状态

### CRM Object Eval (cuda:0,1,2)

| Tmux Session | GPU | Seed | PID | Log | 进度 |
|---|---|---|---|---|---|
| eval-crm-object-s42 | 0 | 42 | 366365 | /tmp/eval_crm_object_seed42.log | 1/10 tasks done, task 2 rollout 5/20 |
| eval-crm-object-s43 | 1 | 43 | 367985 | /tmp/eval_crm_object_seed43.log | 1/10 tasks done |
| eval-crm-object-s44 | 2 | 44 | 368249 | /tmp/eval_crm_object_seed44.log | 1/10 tasks done |

Registry IDs: `eval-smolvla-crm-object-seed42-v1`, `eval-smolvla-crm-object-seed43-v1`, `eval-smolvla-crm-object-seed44-v1`

**Task 1 结果** (pick_up_the_alphabet_soup): 所有 3 seeds 均为 70% (14/20)

### VLA-only Spatial (cuda:3,4,5) — 原 CRM spatial 因 `--input_mode obs_only` 参数错误已失败

| Tmux Session | GPU | Seed | PID | Log | 进度 |
|---|---|---|---|---|---|
| crm_spa_s42 | 3 | 42 | 373281 | /tmp/eval_vla_spatial_seed42.log | 1/10 tasks done, task 2 rollout 10/20 |
| crm_spa_s43 | 4 | 43 | 373273 | /tmp/eval_vla_spatial_seed43.log | 1/10 tasks done, task 2 rollout 15/20 |
| crm_spa_s44 | 5 | 44 | 373275 | /tmp/eval_vla_spatial_seed44.log | 1/10 tasks done, task 2 rollout 10/20 |

**预计完成时间**: ~4 小时后 (~11:20 UTC)

**注意**: CRM spatial 在 bjb2 上失败（`--input_mode obs_only` 不是有效参数），VLA-only 部分因 pipe+tee 导致继续执行。CRM spatial 已在 bjb1-32546 上正确重新部署。

---

## bjb1-32546 进程状态

### CRM Spatial Eval (cuda:0,1,2)

| Tmux Session | GPU | Seed | PID | Log | 进度 |
|---|---|---|---|---|---|
| crm_spatial_seed42 | 0 | 42 | 494055 | /root/autodl-tmp/logs/crm_spatial_seed42.log | Task 1/10, rollout 10/20 |
| crm_spatial_seed43 | 1 | 43 | 494320 | /root/autodl-tmp/logs/crm_spatial_seed43.log | Task 1/10, rollout 10/20 |
| crm_spatial_seed44 | 2 | 44 | 494589 | /root/autodl-tmp/logs/crm_spatial_seed44.log | Task 1/10, rollout 10/20 |

Registry IDs: `eval-smolvla-crm-spatial-seed42`, `eval-smolvla-crm-spatial-seed43`, `eval-smolvla-crm-spatial-seed44`

### CRM Goal Eval (cuda:4,5)

| Tmux Session | GPU | Seed | PID | Log | 进度 |
|---|---|---|---|---|---|
| crm_goal_seed42 | 4 | 42 | 494865 | /root/autodl-tmp/logs/crm_goal_seed42.log | Task 1/10, rollout 5/20 |
| crm_goal_seed43 | 5 | 43 | 495134 | /root/autodl-tmp/logs/crm_goal_seed43.log | Task 1/10, rollout 5/20 |

Registry IDs: `eval-smolvla-crm-goal-seed42`, `eval-smolvla-crm-goal-seed43`

---

## Cron 监控

| Cron ID | 频率 | 目标 | 内容 |
|---|---|---|---|
| b52cfb81 | 每 2 分钟（偶数分） | bjb2-28827 | 监控 3 个 object CRM eval |
| f60874d2 | 每 2 分钟（奇数分） | bjb1-32546 | 监控 3 spatial + 2 goal CRM eval |
| a7e693bb | 每 5 分钟 | bjb2-28827 | 检查 VLA-only spatial 完成 → 自动部署 goal seed44 |

---

## Goal Seed44 部署状态

**状态**: 待部署

- **目标服务器**: bjb2-28827, cuda:3
- **阻塞原因**: VLA-only spatial seed42 仍在 cuda:3 上运行（1/10 tasks done, ~4h 剩余）
- **触发条件**: cron a7e693bb 每 5 分钟检查 VLA-only spatial seed42 是否完成
- **部署命令**: 不含 `--input_mode obs_only`，链式执行 CRM eval + VLA-only eval
- **log 路径**: /root/autodl-tmp/logs/crm_goal_seed44.log
- **部署后**: 注册 registry `eval-smolvla-crm-goal-seed44`，加入 bjb2 监控 cron
