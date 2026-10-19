# check bjb1 eval progress d021

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-eval-progress-d021_20260515T020440_result.json`
- **Structured JSON:** [`22d2fbb82ee3145e5f65.json`](../../sessions/22/22d2fbb82ee3145e5f65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总 (2026-05-15 10:05 UTC)

所有 5 个进程全部 **ALIVE**。GPU 2 上有两个进程共享（232820 + 288939），利用率 99%。

---

## 1. eval-argmin-only-spatial (GPU 1, PID 231421/231426)
- **模式**: reconvla baseline
- **状态**: ALIVE, 运行 8h17m
- **进度**: 7/10 tasks completed
- Per-task results:
  - T1 (between plate & ramekin): 6/10 (60%)
  - T2 (next to ramekin): **10/10 (100%)**
  - T3 (table center): 0/10 (0%)
  - T4 (on cookie box): 3/10 (30%)
  - T5 (top drawer): 1/10 (10%)
  - T6 (on ramekin): 1/10 (10%)
  - T7 (next to cookie box): 9/10 (90%)
- **当前**: Task 8, 日志未输出中间进度
- **预计剩余**: ~3.5h（~71 min/task × 3 tasks）

---

## 2. eval-acr-spatial-v4-obs-only-r2 (GPU 0, PID 270097)
- **模式**: crm_obs_only, crm_v3_norm/obs_only, max_norm=0.1
- **状态**: ALIVE, 运行 3h43m
- **进度**: 4/10 tasks completed
- Per-task results:
  - T1: **9/10 (90%)**
  - T2: **10/10 (100%)**
  - T3: 0/10 (0%)
  - T4: 4/10 (40%)
- **当前**: Task 5 进行中
- **预计剩余**: ~5.5h（~56 min/task × 6 tasks）

---

## 3. eval-acr-spatial-v4-small (GPU 3, PID 253085)
- **模式**: acr_vla, crm_v3_norm/perdof, max_norm=0.1
- **状态**: ALIVE, 运行 5h35m
- **进度**: 4/10 tasks completed, Task 5 进行中
- Per-task results:
  - T1: 6/10 (60%)
  - T2: **10/10 (100%)**
  - T3: 1/10 (10%)
  - T4: 4/10 (40%)
- **当前**: Task 5, rollout 5/10 (0/5 so far)
- **预计剩余**: ~6.5h（~75 min/task × 5.5 tasks）

---

## 4. eval-acr-spatial-v4-scalar (GPU 2, PID 288939)
- **模式**: crm_scalar, crm_v3_norm/scalar_unc, max_norm=0.1
- **状态**: ALIVE, 运行 30m
- **进度**: Task 1 进行中
- Per-task results:
  - T1: 3/5 halfway (rollout 5/10)
- **当前**: Task 1, rollout 5/10
- **预计剩余**: ~10-12h（与 PID 232820 共享 GPU 2，速度受影响）

---

## 5. eval-tiny-correction-spatial (GPU 2, PID 232820) ⚠️ 不在预期列表中
- **模式**: acr_vla, **crm_v2/perdof** (旧 checkpoint), max_norm=**0.05**
- **状态**: ALIVE, 运行 8h16m
- **进度**: 7/10 tasks completed, Task 8 进行中
- Per-task results:
  - T1: 7/10 (70%)
  - T2: 9/10 (90%)
  - T3: 0/10 (0%)
  - T4: 3/10 (30%)
  - T5: 0/10 (0%)
  - T6: 0/10 (0%)
  - T7: 9/10 (90%)
- **当前**: Task 8, rollout 5/10
- **预计剩余**: ~2.5h

---

### ⚠️ 注意

1. **GPU 2 资源竞争**: PID 232820 (tiny-correction) 和 PID 288939 (scalar) 共享 GPU 2（总占用 2914MiB），利用率已 99%。scalar 实验速度会受影响。
2. **PID 232820 未在预期列表中**: 这是一个使用旧 crm_v2 checkpoint 和 max_norm=0.05 的实验，可能是遗留任务。如果不需要，kill 掉可以释放 GPU 2 给 scalar 实验加速。
3. **PID 231421 不是 231426**: 用户给的 PID 231421 是 bash wrapper，实际 python 进程是 PID 231426。

---
