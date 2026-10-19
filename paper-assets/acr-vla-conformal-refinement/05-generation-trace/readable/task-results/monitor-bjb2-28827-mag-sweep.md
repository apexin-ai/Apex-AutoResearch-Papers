# monitor bjb2 28827 mag sweep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb2-28827-mag-sweep_20260515T044423_result.json`
- **Structured JSON:** [`bced7b5676ad8a0db829.json`](../../sessions/bc/bced7b5676ad8a0db829.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个实验全部在跑，进度汇总如下（每个实验共 10 tasks × 10 rollouts）：

| 实验 | GPU | Tasks Done | 当前进度 | 已完成 task SR |
|------|-----|-----------|---------|---------------|
| **perdof-norm003** | 0 | 1/10 | Task 2 rollout 5/10 (5/5) | T1: 60% |
| **perdof-norm005** | 1 | 1/10 | Task 2 rollout 5/10 (5/5) | T1: 50% |
| **perdof-norm02** | 2 | 1/10 | Task 2 rollout 5/10 (4/5) | T1: 60% |
| **perdof-norm03** | 3 | 1/10 | Task 2 尚未开始 | T1: 70% |
| **obsonly-norm005** | 4 | 2/10 | Task 3 进行中 | T1: 80%, T2: 90% |
| **obsonly-norm02** | 5 | 2/10 | Task 3 进行中 | T1: 90%, T2: 100% |

关键观察：
- 所有进程正常运行，GPU 利用率 17-19%，温度正常 (34-38°C)
- 大约完成 10-20%，预计还需 ~6-8 小时
- obs_only 组略快于 perdof 组（已完成 2 tasks vs 1 task）
- 初步趋势：**更大的 norm 倾向于更高的 SR**（perdof: 0.03→60%, 0.05→50%, 0.2→60%, 0.3→70%；obsonly: 0.05→80%/90%, 0.2→90%/100%），但仅 1-2 个 task 的数据，不能下结论

---
