# ssh verify 29046 and pipeline

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-29046-and-pipeline_20260522T112258_result.json`
- **Structured JSON:** [`3382d6de8fa7f1add92b.json`](../../sessions/33/3382d6de8fa7f1add92b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### exp-003-s2 (R3-only seed 2)
- **PID**: 237437（GPU0，97% 利用率，38GB 显存）
- **当前 step**: 7424/8000，~25.5s/step
- **ckpt-7500 ETA**: ~19:55 服务器时间（距现在约 30 分钟）
- **训练完成 ETA**: ~23:30 服务器时间（约 4 小时后）
- **Checkpoint 路径**: `/root/autodl-tmp/checkpoints/exp003_r3only_seed2/`（最新 ckpt-7000）

### exp-004-s2 (ACT seed 2 resume)
- **PID**: 494017（GPU1，34% 利用率，23GB 显存）
- **状态**: 已自动重启，从 ckpt-2000 恢复，18:49 开始
- **当前 step**: 2230/8000，~9s/step
- **ckpt-2500 ETA**: ~20:05 服务器时间（约 40 分钟后）
- **训练完成 ETA**: ~09:45 May 23
- **Checkpoint 路径**: `/root/autodl-tmp/contrastive_entrain_calib/outputs/exp-004-act-baseline-s2/`（数据盘，不会再磁盘满）
- **崩溃原因**: 前一次运行保存到根分区（93% 满），在 step 2500 保存时 "No space left on device"。resume 脚本已改为写入 autodl-tmp。

### SCP / Eval
- **ckpt-7500 和 ckpt-2500 均尚未生成**，无法立即 SCP 和提交 eval
- 两个 checkpoint 预计 30-40 分钟后可用

需要我稍后回来检查并执行 SCP + eval 吗？

---
