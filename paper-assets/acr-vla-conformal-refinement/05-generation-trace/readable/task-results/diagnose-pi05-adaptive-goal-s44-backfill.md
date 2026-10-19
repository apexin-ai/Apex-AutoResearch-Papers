# diagnose pi05 adaptive goal s44 backfill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-adaptive-goal-s44-backfill_20260528T112747_result.json`
- **Structured JSON:** [`cddc3da12c7b7fa9aef1.json`](../../sessions/cd/cddc3da12c7b7fa9aef1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成：

**失败根因**：启动命令缺少 `--obs_dim 2048 --unified_obs_dim 2088`。CRM checkpoint 训练时 input_dim=2118，但默认参数初始化 CRM 为 input_dim=990，`load_state_dict` 维度不匹配直接报错。

**对比**：同服务器上成功的 s42/s43 实验均带了这两个参数。

**修复**：重跑时补上 `--obs_dim 2048 --unified_obs_dim 2088` 即可。GPU cuda:0 当前空闲，磁盘充足。

---
