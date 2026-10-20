# check download status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_download_status_20260516T072755_result.json`
- **Structured JSON:** [`28b9433b77f9ac7a22e9.json`](../../sessions/28/28b9433b77f9ac7a22e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D077 资源下载状态

| 资源 | 状态 | 路径 | 说明 |
|------|------|------|------|
| **Qwen3-8B** | ✅ 已完成 | `/root/autodl-tmp/models/Qwen/Qwen3-8B/` | 16GB，5 个 shard 齐全 |
| **LLaMA-3.1-8B** | ⏳ 下载中 | `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B/` | 11GB/~15GB，shard 1,2,4 完成，shard 3 正在下载（148MB/~5GB）。有两个下载进程在跑（PID 311976 + 313132） |
| **Re-DocRED** | ✅ 已完成 | `/root/autodl-tmp/data/re-docred/` | train_annotated.json + dev.json + test.json 齐全 |

**磁盘空间**: `/root/autodl-tmp/` 250GB 已用 242GB，剩余 **8.3GB (97%)**。LLaMA shard 3 还需 ~4.7GB，下载完后只剩 ~3.6GB，空间极其紧张。

**注意**: Qwen3-8B 实际路径是 `/root/autodl-tmp/models/Qwen/Qwen3-8B/`（不是 `/root/autodl-tmp/models/Qwen3-8B/`），实验代码引用时需注意。

---
