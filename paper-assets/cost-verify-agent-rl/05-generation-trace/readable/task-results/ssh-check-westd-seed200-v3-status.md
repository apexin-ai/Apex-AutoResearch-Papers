# ssh check westd seed200 v3 status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_seed200_v3_status_20260522T194836_result.json`
- **Structured JSON:** [`8109d5a9d53ec359d200.json`](../../sessions/81/8109d5a9d53ec359d200.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### seed100 — 已完成 (5/5)
- **PID**: 78400 (TaskRunner), GPU workers 78937/78938
- **GPU**: cuda:0,1，各占 12.6GB，利用率 6%/72%（正在收尾）
- **进度**: 5/5 steps 全部完成，checkpoint 已保存至 `/root/autodl-tmp/checkpoints/exp029-seed100/global_step_5/`
- **最终 val 指标**: `val-core/unknown/reward/best@32/mean: 9.98`, `val-core/unknown/reward/mean@32: 0.625`（step 0 baseline）
- **训练 step 2 指标**: success=16.4%, pass@8=68.8%

### seed200 v3 — 已崩溃 (step 2/5)
- **原因**: `ActorUnavailableError: RPC error: Socket closed rpc_code: 14`（Ray actor 通信断裂）
- **最后记录**: step 2, success=21.1%, pass@8=81.25%（W&B run `sy10o3te` 最后写入 03:40）
- **无 checkpoint 保存**
- **GPU 2,3 有孤儿 Ray workers**（PID 132938/132939），各占 ~96GB 显存，利用率 94-100%，在空转。需要手动清理。

### 磁盘
- `/root/autodl-tmp`: 116G/250G (47%)，健康

### 需要处理
1. 清理 GPU 2,3 上的孤儿 Ray workers（kill 132938, 132939 + 停止 Ray seed200 session）
2. seed200 v3 需要重跑（无 checkpoint，从头开始）

---
