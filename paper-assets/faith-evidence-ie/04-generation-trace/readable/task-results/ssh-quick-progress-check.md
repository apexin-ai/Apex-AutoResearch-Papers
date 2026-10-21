# ssh quick progress check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_quick-progress-check_20260515T025507_result.json`
- **Structured JSON:** [`8863e8391bd6ac97557f.json`](../../sessions/88/8863e8391bd6ac97557f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个进程全部在跑，当前状态 (UTC 10:55):

| Shard | 完成 | 总量 | 进度 | 已用时间 | 预估剩余 |
|-------|------|------|------|----------|----------|
| shard_0 (GPU0) | 285 | 682 | 41.8% | ~75min | ~104min |
| shard_1 (GPU1) | 322 | 681 | 47.3% | ~74min | ~82min |
| shard_2 (GPU2) | 323 | 681 | 47.4% | ~74min | ~82min |
| shard_3 (GPU3) | 297 | 681 | 43.6% | ~66min | ~85min |
| **整体** | **1227** | **2725** | **45.0%** | — | — |

shard_0 最慢（启动最早但完成数最少），是瓶颈。预计全部完成约需 **1h45min**（~UTC 12:40）。

---
