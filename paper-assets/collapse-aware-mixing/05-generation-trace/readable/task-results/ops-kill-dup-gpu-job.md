# ops kill dup gpu job

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_dup_gpu_job_20260513T181040_result.json`
- **Structured JSON:** [`d84c5183c337b0b63c0b.json`](../../sessions/d8/d84c5183c337b0b63c0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

| | PID | 启动时间 | 状态 |
|---|---|---|---|
| **已 Kill** | 93719 | 01:51:51 | 已终止 |
| **保留** | 93514 | 01:50:31 | 运行中 |

**GPU 利用率**: 100% GPU / 41% 显存 / 32683 MiB used / 97887 MiB total — 显存占用从 ~65GB 降到 ~32GB，只剩一个进程。

**当前进度**: 保留进程正在跑 `token-entropy` 指标计算，进度 44%（137/313），速度 ~1.82 it/s，预计还需约 1 分 36 秒完成此阶段。之前已完成 `spectral-rank` 阶段。

---
