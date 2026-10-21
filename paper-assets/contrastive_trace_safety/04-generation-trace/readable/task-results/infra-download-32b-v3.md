# infra download 32b v3

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download_32b_v3_20260516T195512_result.json`
- **Structured JSON:** [`ee814ead8087a837016c.json`](../../sessions/ee/ee814ead8087a837016c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载进程活跃中，两个 32B 模型并行通过 ModelScope 下载：

- **R1-32B** (8 shards × ~8GB): 各 shard 8-24% 完成，速度 2-7 MB/s
- **QwQ-32B** (14 shards × ~4.5GB): 各 shard 12-38% 完成，速度 2.5-9 MB/s

当前缓存 36GB，磁盘剩余 212GB。预计还需 1-2 小时完成。已设置 ~5 分钟后自动轮询。

---
