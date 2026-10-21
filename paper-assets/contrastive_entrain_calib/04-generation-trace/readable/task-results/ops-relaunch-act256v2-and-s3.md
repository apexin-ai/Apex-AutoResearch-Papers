# ops relaunch act256v2 and s3

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_relaunch-act256v2-and-s3_20260525T172530_result.json`
- **Structured JSON:** [`3d4e47b6a7d36a6cdfc8.json`](../../sessions/3d/3d4e47b6a7d36a6cdfc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已成功启动：

**exp-act-256-v2** (cuda:0, PID 2112):
- 从头开始训练，模型已加载，128 pairs 已读取，training loop 已启动
- 脚本已修改：checkpoint 现在会保存 optimizer/scheduler/training_state（下次被 kill 可 resume）

**exp-003-s3** (cuda:1, PID 2191):
- 成功从 checkpoint-500 resume，进度条显示已跳到 step 501/8000 开始继续训练
- 速度 ~8.26 it/s（每 step 含生成 + reward 计算）

预估完成时间：
- exp-act-256-v2: 8000 steps × ~6.6s/step ≈ 14.7h
- exp-003-s3: 剩余 7500 steps，按当前速度 ≈ 15min（TRL 的 it/s 是 micro-batch 级别，实际 optimizer step 约 19s，总计 ~2.5h）

---
