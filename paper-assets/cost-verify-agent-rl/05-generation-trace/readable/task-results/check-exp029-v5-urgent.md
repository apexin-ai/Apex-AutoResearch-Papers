# check exp029 v5 urgent

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_v5_urgent_20260516T175747_result.json`
- **Structured JSON:** [`2a511ddce57ff6ceb2bf.json`](../../sessions/2a/2a511ddce57ff6ceb2bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029 attempt 5 状态

**进程**:
- PID 879991: **ALIVE** (运行 1h32m)
- PID 883223: **ALIVE** (运行 1h31m)

**GPU**:
- GPU 0: 0% util, 44539 MiB used
- GPU 1: 0% util, 45407 MiB used

**当前阶段**: 已完成 initial validation (step 0)，进入训练。

**关键错误**: wandb 日志尝试写 `/tmp/tmpzicbifxf` 时报 `FileNotFoundError: No such file or directory`。`/tmp` 目录不存在（`df -h /tmp` 报错 No such file or directory）。

**Initial Validation Metrics (step 0)**:
- `val-env/AlfworldSG/success`: **12.5%** (32 episodes)
- `val-env/AlfworldSG/pass@1`: 12.5%
- `val-core/unknown/reward/mean@32`: 1.25
- `val-core/unknown/reward/best@32/mean`: 9.84

**磁盘**: 根分区 30G, 已用 14G, 剩余 17G (46%)

**问题**: GPU utilization 0% + `/tmp` 不存在 + wandb FileNotFoundError → 训练可能已经 **挂起/卡死**。进程虽存活但未在做有效计算。建议创建 `/tmp` 目录后重启，或检查进程是否已进入 error loop。

---
