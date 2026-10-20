# ssh rsft shard progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rsft-shard-progress_20260515T022408_result.json`
- **Structured JSON:** [`78411ba69bdbf82d9fac.json`](../../sessions/78/78411ba69bdbf82d9fac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前时间: **2026-05-15 02:28 UTC**，启动时间约 01:40 UTC，已运行 **~48 分钟**。

| Shard | 已完成 | 总 docs | 进度% | 速度 (docs/min) | 剩余 | ETA (UTC) |
|-------|--------|---------|-------|-----------------|------|-----------|
| shard_0 | 183 | 682 | 26.8% | 3.76 | 499 | ~04:41 |
| shard_1 | 195 | 681 | 28.6% | 4.00 | 486 | ~04:30 |
| shard_2 | 199 | 681 | 29.2% | 4.09 | 482 | ~04:27 |
| shard_3 | 180 | 681 | 26.4% | 3.70 | 501 | ~04:44 |
| **合计** | **757** | **2725** | **27.8%** | **15.55** | **1968** | — |

**GPU 状态**: 4 个 GPU 均在运行，显存占用 14.9–19.3 GiB，正常。

**Root 目录**: `progress.json` 有 302 docs（应是分片前的旧数据），`generations.jsonl` 2416 行。

**预计全部完成**: ~04:44 UTC（约 2 小时 16 分钟后），瓶颈在 shard_3。

---
