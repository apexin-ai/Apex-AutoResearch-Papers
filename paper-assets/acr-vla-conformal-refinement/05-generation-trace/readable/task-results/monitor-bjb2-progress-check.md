# monitor bjb2 progress check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb2-progress-check_20260514T212451_result.json`
- **Structured JSON:** [`c2749d5b2518418fbcad.json`](../../sessions/c2/c2749d5b2518418fbcad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval-vla-mean-spatial 状态

**进程**: 存活，正常运行
- PID 143106 (wrapper) → PID 143112 (Python worker)
- 状态: `Rl`（Running，多线程），CPU 138%，RSS 7.4 GB，GPU 1915 MiB
- 已运行 18h16m

**进度**: 85/100 rollouts 完成 (**85%**)

| # | Task | Success Rate |
|---|------|-------------|
| 1 | bowl between plate and ramekin → plate | **70%** (7/10) |
| 2 | bowl next to ramekin → plate | **100%** (10/10) |
| 3 | bowl from table center → plate | **0%** (0/10) |
| 4 | bowl on cookie box → plate | **30%** (3/10) |
| 5 | bowl in top drawer → plate | **0%** (0/10) |
| 6 | bowl on ramekin → plate | **0%** (0/10) |
| 7 | bowl next to cookie box → plate | **80%** (8/10) |
| 8 | bowl on stove → plate | **0%** (0/10) |
| 9 | bowl next to plate → plate | **进行中** 1/5 (rollout 5/10) |
| 10 | (未开始) | — |

**中间汇总**: 已完成 8 个 task，成功 28/80 = **35%**。相比上次交接的 "~40%, 7/10 tasks"，新增完成了 task 8（0%），task 9 进行中。

**预估剩余时间**: 85 rollouts 用了 ~17h，平均 ~12 min/rollout。剩余 15 rollouts ≈ **3 小时**完成。

日志最后更新约 1 小时前（task 9 rollout 5/10），进程仍在正常消耗 CPU+GPU，运行正常，可能是输出缓冲导致日志未实时刷新。

---
