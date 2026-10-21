# ops westd urgent process check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_urgent_process_check_20260522T160944_result.json`
- **Structured JSON:** [`2fda04a2c5f2f87b4626.json`](../../sessions/2f/2fda04a2c5f2f87b4626.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-47453 训练状态

### seed100: **存活，正常训练中**
- 进程: PID 883370 `python train.py --config-name _alfworld_exp029_seed100_episode` (启动于 May22)
- Ray workers 活跃: TaskRunner (PID 896114), 2x WorkerDict, wandb 上报正常
- 日志最后更新: `2026-05-22 23:48:34` — **Training Progress: 60% (3/5 steps)**, 预计剩余 ~42 min

### seed200: **已崩溃**
- **无进程存活**（ps 中无 seed200 相关进程）
- 崩溃原因: `OSError: [Errno 28] No space left on device` — 磁盘满

### GPU 占用

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 44777 MiB | 56% |
| 1 | 45061 MiB | 100% |
| 2 | 0 MiB | 0% |
| 3 | 0 MiB | 0% |

GPU 0,1 被 seed100 占用。GPU 2,3 空闲（seed200 崩溃后已释放）。

**结论**: seed100 在跑、占 2 卡，seed200 磁盘满挂了。如果 Manager 要收卡，GPU 2,3 当前空闲可收；GPU 0,1 需等 seed100 完成（~42 min）或主动终止。

---
