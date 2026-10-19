# SmolVLA Baseline Eval Status — 2026-05-22

## Eval 进程状态

| experiment_id | status | progress | success_rate | n_episodes |
|---|---|---|---|---|
| eval-smolvla-lerobot-spatial-seed43-v3 | DONE | 10/10 tasks | **54.5%** | 200 |
| eval-smolvla-lerobot-goal-seed43-v3 | DONE | 10/10 tasks | **82.0%** | 200 |
| eval-smolvla-lerobot-goal-seed44-v3 | DONE | 10/10 tasks | **78.0%** | 200 |

所有 3 个 eval 已完成，进程已退出，log 显示 "End of eval"。Registry 已从 RUNNING → DONE。

## SmolVLA Baseline 完整汇总 (3-seed mean±std)

| Suite | seed42 | seed43 | seed44 | Mean±Std |
|---|---|---|---|---|
| Object | 66.5% | 66.5% | 65.0% | **66.0%±0.9%** |
| Spatial | 59.5% | 54.5% | 60.0% | **58.0%±3.0%** |
| Goal | 75.5% | 82.0% | 78.0% | **78.5%±3.3%** |
| Long | — | — | — | **50.8%±2.3%** |

所有 4 个 suite 的 SmolVLA baseline 已齐全。

## CRM 4-Suite 训练进度

| experiment_id | status | progress | note |
|---|---|---|---|
| train-crm-unified-4suite-r5 | RUNNING | epoch 28/50 (~56%) | loss ~0.011, batch 5950/6316 |

训练在 bjb1-32546 GPU3 上运行，PID 322367。

## 其他正在运行的任务

- **eval-pi05-crm-object-seed42**: Pi0.5 CRM eval 在 bjb1-32546 GPU0 上运行（tmux session）
- **precompute-pi05-{object,spatial,goal,long}-2048**: 4 个 Pi0.5 precompute 在 bjb1-18228 上运行
