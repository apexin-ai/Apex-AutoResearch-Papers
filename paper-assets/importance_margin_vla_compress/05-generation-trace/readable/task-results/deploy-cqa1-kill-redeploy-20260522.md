# deploy cqa1 kill redeploy 20260522

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_kill_redeploy_20260522_20260522T205817_result.json`
- **Structured JSON:** [`0c0c1960e48133dc0cf1.json`](../../sessions/0c/0c0c1960e48133dc0cf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已成功启动：

- **cuda:0** `eval_pi05_l2norm_k07_goal`: 模型已加载，pruning l2norm keep 179/256 tokens，正在运行
- **cuda:1** `eval_pi05_random_k095_goal`: 模型正在加载中

**执行摘要：**

| 操作 | 状态 |
|------|------|
| Kill OpenVLA Spatial (cuda:0) | 完成，tmux session `openvla_spatial` 已清除 |
| 部署 π0.5 L2norm k=0.7 Goal seed42 (cuda:0) | 运行中，模型已加载 |
| 部署 π0.5 Random k=0.95 Goal seed42 (cuda:1) | 运行中，模型加载中 |
| Registry: `eval_pi05_l2norm_k095_goal_seed42` | DONE, conclusion=negative, SR=89.4% |
| Registry: `eval_openvla_baseline_spatial_seed42` | DONE, conclusion=failed, 环境问题 |
| Registry: `eval_pi05_l2norm_k07_goal_seed42` | 卡在 DEPLOYED（旧实验状态机死路，实际已在 cqa1 运行） |
| Registry: `eval_pi05_random_k095_goal_seed42` | RUNNING |

**cuda:2/3 现有任务**：`eval_pi05_random_k03_goal_seed42` 和 `pi05_long` 仍在运行。

---
