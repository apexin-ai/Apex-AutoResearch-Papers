# ops check bjb1 exp029 seed2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-bjb1-exp029-seed2_20260518T091347_result.json`
- **Structured JSON:** [`3ae2ee4f7ff21988e632.json`](../../sessions/3a/3ae2ee4f7ff21988e632.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp029_seed2 已死。**

- **PID 16575 存活？** 否。进程不存在（`ps -p 16575` 未匹配到 train.py）
- **GPU 0 占用：** 0MiB 显存 / 100% 利用率 / 无进程（GPU-Util 100% 但 Processes 列为空，可能是残留状态或驱动异常）
- **GPU 1 占用：** 0MiB 显存 / 0% 利用率 / 无进程
- **Ray worker PID 19997/19998 存活？** 否。均不存在
- **双卡都在用？** 否，两张卡均空闲，无任何训练进程

训练主进程和 Ray worker 全部已终止，GPU 上无运行中的进程。

---
