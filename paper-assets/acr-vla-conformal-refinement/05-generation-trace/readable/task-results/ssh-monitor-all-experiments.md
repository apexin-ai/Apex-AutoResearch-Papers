# ssh monitor all experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_monitor-all-experiments_20260523T033446_result.json`
- **Structured JSON:** [`570146304ed9fc769a0c.json`](../../sessions/57/570146304ed9fc769a0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

12 个实验全部正常运行，无崩溃。核心要点：

**Object VLA-only baseline**（最关注）：3 seed 均在 task 7/10，约 65% 完成，3-seed 暂估均值 **79.7%**，预计 ~14:30 完成。

**CRM 4-suite training r5**：epoch 38/50，val_loss 持续下降至 0.005903，收敛健康，预计 ~16:30 完成。

**Spatial eval sweep**（bjb1，4 个实验）：刚启动 ~35 min，全部在 task 2/10。首 task 结果 — norm=0.2 和 tau=0.15 达 100%，tau=0.25 和 tau=0.35 达 95%。

**bjb2 新启 eval**（obj_adapt, obj_reconvla, goal_crm005）：均在 task 1/10 rollout 10/20，预计 ~5 小时完成。

报告已写入 `artifacts/experiment_status_20260523_session25.md`。

---
