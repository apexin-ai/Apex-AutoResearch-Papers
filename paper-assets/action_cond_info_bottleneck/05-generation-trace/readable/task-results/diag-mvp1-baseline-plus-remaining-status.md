# diag mvp1 baseline plus remaining status

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mvp1_baseline_plus_remaining_status_20260515T234053_result.json`
- **Structured JSON:** [`c96c83479576d895a952.json`](../../sessions/c9/c96c83479576d895a952.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 评测进度报告

### 进程状态
- **PID 471056**: 存活，已运行 26 分 44 秒
- 当前命令：`lerobot-eval --env.task=libero_goal`（只跑 libero_goal，非全部 suite）

### 已完成 Suite

| Suite | Success Rate | 状态 |
|-------|-------------|------|
| libero_spatial | **81.6%** (408/500) | ✅ 完成 |
| libero_object | **88.8%** (444/500) | ✅ 完成 |

### 当前进行：libero_goal
- task 0: ✅ 完成（10 个视频已写入）
- task 1: ✅ 完成（10 个视频已写入）
- task 2: 进行中（9/10 个视频已写入，接近完成）
- task 3-9: 未开始
- 日志显示当前 rollout 在 step 90/300，running_success_rate=0.0%

**进度**：10 个 task 中完成了约 2.5 个（~125/500 episodes）

### 预估剩余时间
- **libero_goal 剩余**：~375 episodes，按 ~4.6 eps/min 估算，约 **80 分钟**
- **libero_10**：尚未启动，当前进程只跑 libero_goal。需要单独启动，预计 ~100 分钟

### 注意
输出目录是 `baseline_plus_v2`（非 v3）。libero_10 需要在 libero_goal 完成后手动启动。

---
