# monitor eval progress check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_eval-progress-check_20260514T031649_result.json`
- **Structured JSON:** [`99b39a6fc3dd996666a4.json`](../../sessions/99/99b39a6fc3dd996666a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

### bjb1-18228

| # | 实验 | PID | 进程状态 | 进度 | 已用时间 | 预估剩余 | Errors |
|---|------|-----|---------|------|---------|---------|--------|
| 1 | **eval-acr-spatial-v2** | 117814 | ✅ 存活, CPU 135%, 10GB RSS | 3/10 tasks (30/100 episodes) | 3h33m | ~8h | 0 |
| 2 | **eval-reconvla-spatial-v3** | 118108 | ✅ 存活, CPU 136%, 10GB RSS | 3.5/10 tasks (35/100 episodes) | 3h33m | ~6.5h | 0 |
| 3 | **eval-scalar-unc-spatial** | 143206 | ⚠️ 存活, CPU 0%, 2MB RSS | 1/10 tasks (10/100 episodes) | 54m | ~8h | 0 |
| 4 | **crm-train-k5** | 139839 | ⚠️ 存活, CPU 0%, 3.5MB RSS | Epoch 33/50 (batch 150/752, ~64%) | 1h34m | ~53min | 0 |

### bjb2-40593

| # | 实验 | PID | 进程状态 | 进度 | 已用时间 | 预估剩余 | Errors |
|---|------|-----|---------|------|---------|---------|--------|
| 5 | **eval-vla-mean-spatial** | 143106 | ⚠️ 存活, CPU 0%, 2MB RSS | 0/10 tasks (刚加载完模型) | 7m | 无法估计 | 0 |

### 各 eval 已完成 task 的 success rate

**eval-acr-spatial-v2** (3 tasks done):
- Task 0 (bowl between plate & ramekin): **40%** (4/10)
- Task 1 (bowl next to ramekin): **70%** (7/10)
- Task 2 (bowl from table center): **0%** (0/10)

**eval-reconvla-spatial-v3** (3 tasks done, task 3 in progress at rollout 5/10):
- Task 0: **60%** (6/10)
- Task 1: **100%** (10/10)
- Task 2: **0%** (0/10)

**eval-scalar-unc-spatial** (1 task done):
- Task 0: **50%** (5/10)

**crm-train-k5**: train_loss 0.0149 → val_loss 0.0096, lr 2.87e-4 (cosine decay), loss 持续下降中。

### 注意事项

⚠️ PID 143206 / 139839 / 143106 的 CPU=0%、RSS 极低（2-3.5MB），可能是 shell wrapper 进程，实际 Python/GPU 进程是其子进程。eval-vla-mean-spatial 日志显示模型已加载但尚未开始 rollout，可能还在初始化环境中。

---
