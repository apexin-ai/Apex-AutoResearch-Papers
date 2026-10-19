# ops m1 progress check v3

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m1-progress-check-v3_20260513T103626_result.json`
- **Structured JSON:** [`9e99c7e33d2b4ca678de.json`](../../sessions/9e/9e99c7e33d2b4ca678de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

| 指标 | 数值 |
|------|------|
| **实例进度** | 42,114 / 59,136 (71.2%) |
| **Repo 完成** | 109 / 222 |
| **Repo 进行中** | 14 (含 getmoto/moto、pydicom、freezegun、string2string 等) |
| **Repo 未开始** | 99 |
| **主进程 PID** | 577864，已运行 13h49m |
| **清理守护进程** | PID 580662，运行正常 |
| **磁盘** | extraction 6.3G + repos 1.1G，剩余 26G (85%) |
| **错误** | 114 条，主要是 `Stale file handle` (ERRNO 116) |
| **预计剩余** | ~6-8 小时 |

进度比之前加速很多——从 27% 跳到 71%，清理守护进程有效控制了磁盘。当前正在并行处理 getmoto/moto (大 repo, 541 instances) 和 pydicom (1328 instances)，这两个完成后还有 99 个 repo 未开始。

---
