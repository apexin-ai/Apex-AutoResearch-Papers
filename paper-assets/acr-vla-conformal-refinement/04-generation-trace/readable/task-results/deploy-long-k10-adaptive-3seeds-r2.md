# deploy long k10 adaptive 3seeds r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_long-k10-adaptive-3seeds-r2_20260525T023934_result.json`
- **Structured JSON:** [`70eec80ee7f92ae99480.json`](../../sessions/70/70eec80ee7f92ae99480.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这 3 个实验**已经在跑了**。Registry 显示：

| exp_id | GPU | 状态 | 启动时间 |
|--------|-----|------|----------|
| eval-long-adaptive-k10-s42 | cuda:3 | RUNNING | 02:38 UTC |
| eval-long-adaptive-k10-s43 | cuda:4 | RUNNING | 02:43 UTC |
| eval-long-adaptive-k10-s44 | cuda:5 | RUNNING | 02:43 UTC |

nvidia-smi 上 cuda:3/4/5 各占用 ~6530 MiB 的进程就是它们。无需重复部署。

---
