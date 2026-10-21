# diag westd38929 gpu3 verify

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd38929-gpu3-verify_20260523T190422_result.json`
- **Structured JSON:** [`ce81cc9a967cbb943dcc.json`](../../sessions/ce/ce81cc9a967cbb943dcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. v3 日志（被杀前）

v3 并非只跑了几分钟，实际跑了约 16 分钟（02:46:06 → 03:01:47），完成了：
- **Task 0** (open the middle drawer): **42.0%** (21/50)
- **Task 1** (put the bowl on the stove): **92.0%** (46/50)
- **Task 2** (put the wine bottle on top of the cabinet): 跑到 ep 10/50 时被杀，当时全 FAIL（仅 ep 5 成功）

### 2. v4 运行状态

v4 **正常运行中**。PID 367660（非 367651），占用 4838 MiB 显存。
- 启动时间：03:02:49
- 当前进度：**Task 0, ep 11/50**（刚开始不久）
- 前 10 个 episode 结果与 v3 一致（相同 seed42），说明复现正常

### 3. GPU 3 状态

- 利用率 1%，显存 4856/97887 MiB
- 唯一进程：PID 367660 (python, 4838 MiB)
- **无孤儿进程**

> 注：`ps aux | grep` 和 `tmux list-sessions | grep` 被 ssh_read_only 的管道限制阻断，但 nvidia-smi 确认 v4 进程在跑，GPU 3 干净。

---
