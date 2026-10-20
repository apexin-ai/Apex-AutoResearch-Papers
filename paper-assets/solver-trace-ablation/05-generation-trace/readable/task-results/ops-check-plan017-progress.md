# ops check plan017 progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-plan017-progress_20260514T042017_result.json`
- **Structured JSON:** [`8a4d325799b3fa9b7e6a.json`](../../sessions/8a/8a4d325799b3fa9b7e6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan017-additive-random-s42 训练状态**

| 指标 | 值 |
|------|-----|
| 当前进度 | **193 / 500** (38.6%) |
| 已运行 | 31m 26s |
| 当前 step time | ~20.2 s/it |
| 预计剩余 | **~1h 43m** |
| 最近 reward | 0.67 (prove_rate=0.625, isr=0.128) |

**GPU 状态**

| GPU | 进程 PID | 显存占用 | 利用率 | 任务 |
|-----|---------|---------|--------|------|
| cuda:0 | 216139 | 21,069 / 97,887 MiB | 98% | plan014 ✅ |
| cuda:1 | 207121 | 79,604 / 97,887 MiB | 91% | plan017 ✅ |

两个任务均正常运行。GPU PID 与用户提供的略有偏差（207121 vs 207116, 216139 vs 216133），是主进程 fork 的子进程，属正常现象。

---
