# audit bjb1 18228 full oom check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb1-18228-full-oom-check_20260526T135129_result.json`
- **Structured JSON:** [`8bf151770b8130f9d261.json`](../../sessions/8b/8bf151770b8130f9d261.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部正常启动，正在加载 PI05 模型。每个独占一卡，cuda:3 保留空闲。

---

## 审计报告

### 1. 实验状态

| 实验 | GPU | OOM 次数 | 完成度 | 状态 |
|------|-----|---------|--------|------|
| pi05-vla-only-goal-s42-4090 | cuda:1 | 400 行 (200 rollouts 全 OOM) | 0/200 | **FAILED** (已标记) |
| pi05-vla-only-object-s42-4090 | cuda:3 | 17 exceptions | 9/10 tasks, 无 JSON | **FAILED** (已标记) |
| pi05-vla-only-spatial-s42-4090 | cuda:0 | 8 exceptions | 9/10 tasks, 无 JSON | **FAILED** (已标记) |
| pi05-adaptive-goal-s44-bjb1 | cuda:2 | 0 | 200/200, SR=86.5% | **CLEAN** |
| pi05-adaptive-goal-s43-bjb1 | - | 0 | 200/200, SR=89.5% | **CLEAN** |
| pi05-k2mean-long-s42 | - | 14 exceptions | killed (143) | **FAILED** (已标记) |
| pi05-k2mean-object-s42 | - | 3 exceptions | killed (143) | **FAILED** (已标记) |
| pi05-k2mean-spatial-s42 | - | 11 exceptions | killed (143) | **FAILED** (已标记) |

### 2. 已 Kill 进程
所有进程已自行终止。bjb1-18228 当前无任何 GPU 进程，4 卡全空（0 MiB）。无需手动 kill。

### 3. 重跑调度
- **bjb1-32546**: 6 卡全满（CRM K=2 实验），无法使用
- **bjb1-18228**: 4 卡空闲，已提交 3 个 vla_only 重跑：

| 重跑实验 | GPU | PID |
|----------|-----|-----|
| pi05-vla-only-goal-s42-4090-r2 | cuda:0 | 239947 |
| pi05-vla-only-object-s42-4090-r2 | cuda:1 | 240882 |
| pi05-vla-only-spatial-s42-4090-r2 | cuda:2 | 241740 |

cuda:3 保留空闲。每个实验独占一卡，不再有碰撞风险。

### 4. bjb1-18228 当前 GPU 状态
- GPU 0: ~3 MiB (goal-r2 加载中)
- GPU 1: ~3 MiB (object-r2 加载中)
- GPU 2: ~3 MiB (spatial-r2 加载中)
- GPU 3: 0 MiB (空闲)

### 待处理
k2mean 的 3 个重跑（long/object/spatial）需要等 GPU 空出后调度。

---
