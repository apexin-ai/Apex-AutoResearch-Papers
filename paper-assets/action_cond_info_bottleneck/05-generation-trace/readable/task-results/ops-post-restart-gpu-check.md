# ops post restart gpu check

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-gpu-check_20260516T215617_result.json`
- **Structured JSON:** [`6e45c308708e4b748156.json`](../../sessions/6e/6e45c308708e4b748156.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. Eval 进程状态：两个都存活

| PID | 运行时间 | GPU | 状态 |
|-----|---------|-----|------|
| 104743 (seed1) | 4h35m | GPU 1 (4913 MiB) | R (running) |
| 111920 (seed2) | 4h30m | GPU 0 (5398 MiB) | R (running) |

### 2. 已完成 Eval 结果

| Suite | seed1 SR | seed2 SR |
|-------|----------|----------|
| libero_spatial | **58.4%** | **51.4%** |
| libero_object | **58.6%** | **49.4%** |
| libero_goal | 进行中 (7/10 tasks done) | 进行中 (6/10 tasks done) |
| libero_10 | 未开始 | 未开始 |

### 3. GPU 状态：两个都被占用

- GPU 0: seed2 eval 占用
- GPU 1: seed1 eval 占用

**无法启动 alpha sweep，两个 GPU 均被 eval 进程占据。**

### 4. 进度估算

已运行约 4.5h 完成 ~2.7/4 suites。剩余：
- seed1: goal 剩 3 tasks + libero_10 全部 → 预计还需 ~2-2.5h
- seed2: goal 剩 4 tasks + libero_10 全部 → 预计还需 ~2.5-3h

**ETA：约 2-3 小时后两个 eval 完成，届时可启动 alpha sweep。**

---
