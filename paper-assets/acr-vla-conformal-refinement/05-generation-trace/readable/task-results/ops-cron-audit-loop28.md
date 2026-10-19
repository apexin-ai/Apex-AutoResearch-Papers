# ops cron audit loop28

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cron-audit-loop28_20260526T101507_result.json`
- **Structured JSON:** [`49f20b336524b334a2f2.json`](../../sessions/49/49f20b336524b334a2f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计完成

### bjb1-32546（6 个 r2 实验，全部 RUNNING ~30 分钟）
- pi05-crm-k2-goal-s42-bjb1-r2: running PID=690807 GPU=cuda:0
- pi05-crm-k2-goal-s43-bjb1-r2: running PID=691080 GPU=cuda:1
- pi05-crm-k2-goal-s44-bjb1-r2: running PID=691360 GPU=cuda:2
- pi05-crm-k2-object-s42-bjb1-r2: running PID=691701 GPU=cuda:3
- pi05-crm-k2-object-s43-bjb1-r2: running PID=692172 GPU=cuda:4
- pi05-crm-k2-object-s44-bjb1-r2: running PID=692577 GPU=cuda:5

注意：磁盘上有 r1 输出 JSON（如 eval_goal_crm_k2_pi05_seed42.json，SR=83.5%；eval_object_crm_k2_pi05_seed44.json，SR=88.0%），r2 重跑会覆盖。

### cqa1-32758（3 个实验，全部 RUNNING ~4h21m）
- pi05-adaptive-long-s43-cqa1-r2: running PID=198442 GPU=cuda:4
- pi05-adaptive-long-s44-cqa1-r2: running PID=199049 GPU=cuda:5
- pi05-adaptive-object-s44-cqa1-r2: running PID=197917 GPU=cuda:3（**cron 已存在，未重新注册**）

注意：long-s43/s44 的 JSON 是空模板（overall_success_rate=0.0、per_task 全 0/20），但日志显示实际进度正常（per-task 80-100%），python 还在跑。

### bjb1-18228
- pi05-adaptive-goal-s43-bjb1-18228: **completed** PID=42110 已死，JSON `eval_goal_adaptive_pi05_seed43_bjb1.json` 显示 overall_success_rate=0.895 → **已标记 DONE/success, SR=89.5%**
- 检测到新进程 pi05-adaptive-goal-s44-bjb1（log 4 分钟前更新）

### Crons registered (8 个新注册)
- pi05-crm-k2-goal-s42-bjb1-r2
- pi05-crm-k2-goal-s43-bjb1-r2
- pi05-crm-k2-goal-s44-bjb1-r2
- pi05-crm-k2-object-s42-bjb1-r2
- pi05-crm-k2-object-s43-bjb1-r2
- pi05-crm-k2-object-s44-bjb1-r2
- pi05-adaptive-long-s43-cqa1-r2
- pi05-adaptive-long-s44-cqa1-r2

（pi05-adaptive-object-s44-cqa1-r2 已有 cron，跳过）

### Completed experiments updated
- pi05-adaptive-goal-s43-bjb1-18228 → DONE/success, SR=89.5%

### Free GPUs discovered
- bjb1-18228 cuda:2（idle，1 MiB used）

---
