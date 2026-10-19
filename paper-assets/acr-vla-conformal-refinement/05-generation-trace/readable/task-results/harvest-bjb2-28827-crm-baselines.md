# harvest bjb2 28827 crm baselines

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb2-28827-crm-baselines_20260524T210947_result.json`
- **Structured JSON:** [`2b3fdf8849910995b161.json`](../../sessions/2b/2b3fdf8849910995b161.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**仍在运行**，不是已完成。任务前提有误。

### 现状
3 个 CRM 实验进程都还活着，从今早 04:18 启动，已跑约 4.5 小时：

| exp_id | PID | CPU 时间 | GPU | 日志进度 |
|--------|-----|---------|-----|---------|
| eval-supp-crm-norm005-spatial-s48 | 429934 | 277:52 | 0 | 任务 5/10 进行中 (37 行) |
| eval-supp-crm-norm005-spatial-s49 | 430199 | 277:22 | 4 | 37 行 |
| eval-supp-crm-norm005-goal-s48 | 430467 | 281:50 | 5 | 32 行 |

### 误判原因
GPU 利用率看似低（4-5GB 显存、20-30% util）是因为 LIBERO 是 MuJoCo CPU 仿真，每个 python 进程 CPU 都在 528-537%（吃满 5+ 核），属正常 rollout 中状态。tmux session 也都在。

### 建议
**不要更新 registry 为 DONE。** 这些实验仍在 RUNNING 状态合理。

spatial-s48 当前进度（log 显示）：
- task 1: 20/20 (100%)
- task 2: 19/20 (95%)
- task 3: 20/20 (100%)
- task 4: 19/20 (95%)
- task 5: 12/15 进行中

按这个速度，预计还要 4-5 小时才能跑完全部 10 个 task。需要我设个 wakeup 稍后再来收割吗？

---
