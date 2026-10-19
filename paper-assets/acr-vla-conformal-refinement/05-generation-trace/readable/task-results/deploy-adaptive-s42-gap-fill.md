# deploy adaptive s42 gap fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_adaptive-s42-gap-fill_20260525T101923_result.json`
- **Structured JSON:** [`8a013dcc91a68fdb8ed1.json`](../../sessions/8a/8a013dcc91a68fdb8ed1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

7 个实验全部启动 + 注册成功。

**bjb2-28827（cuda:1-5，5 个 Adaptive，CRM=crm_smolvla_3suite_v1）：**
| GPU | exp_id | benchmark | seed | 状态 |
|----|--------|-----------|------|------|
| 1 | eval-adaptive-goal-s42-d149 | goal | 42 | RUNNING |
| 2 | eval-adaptive-object-s42-d149 | object | 42 | RUNNING |
| 3 | eval-adaptive-long-s42-d149 | long | 42 | RUNNING |
| 4 | eval-adaptive-long-s44-d149 | long | 44 | RUNNING |
| 5 | eval-adaptive-spatial-s47-d149 | spatial | 47 | RUNNING |

**bjb1-18228（cuda:0,1）：**
| GPU | exp_id | benchmark | mode | seed | 状态 |
|----|--------|-----------|------|------|------|
| 0 | eval-vla-only-spatial-s47-d149 | spatial | vla_only | 47 | RUNNING |
| 1 | eval-adaptive-spatial-s47-bjb1-d149 | spatial | adaptive_conformal_crm | 47 | RUNNING |

注意事项：
- **submit_training_job 工具未在 MCP 中暴露**，只能用 `ssh_execute` + tmux session（命名为 exp_id），效果等价：`tmux list-sessions` 可见 7 个会话，全部已加载 LIBERO 环境进入 rollout 阶段
- bjb1-18228 cuda:2 正在跑 pi05 goal adaptive s42（任务描述的"cuda:3 在跑 precompute pi05 long"与实际不符，但 0/1 仍然空闲，未冲突）
- CRM checkpoint 用 `crm_smolvla_3suite_v1/crm_best.pt`（与 cuda:0 上正在跑的 SmolVLA CRM spatial s47 一致；bjb1-18228 上 unified_4suite_r4 不存在）
- vla_only s47 输出文件命名为 `eval_spatial_vla_only_seed47_n20.json` 以避免覆盖已有 n=10 结果
- bjb1 spatial adaptive 输出文件命名为 `eval_spatial_adaptive_seed47_bjb1.json` 以区分 bjb2 的同名实验

---
