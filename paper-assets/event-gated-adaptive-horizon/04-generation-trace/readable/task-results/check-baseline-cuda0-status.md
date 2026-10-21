# check baseline cuda0 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_baseline-cuda0-status_20260513T114755_result.json`
- **Structured JSON:** [`764e2f3bf1092c37adeb.json`](../../sessions/76/764e2f3bf1092c37adeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

| 项目 | 状态 |
|------|------|
| **PID 9409** | 存活，运行约 9h45m，CPU time 6676min |
| **cuda:0 GPU-Util** | 0%（当前空闲周期，正常波动） |
| **cuda:0 显存** | 4165 MiB / 97887 MiB |
| **当前 step** | **268000** / 500000（53.6%） |
| **最新 train_return** | 967.67（近几个 episode 在 890~977 之间） |
| **最近 eval_return** | 925.09 @ step 265000 |
| **FPS** | 7.27 |

另外 cuda:1 上跑着 exp_004 (event_gated_v4_s1, PID 36645)，GPU-Util 28%，4173 MiB 显存。

按 FPS 7.27 估算，剩余 232k steps 约需 ~8.9h 完成。

---
