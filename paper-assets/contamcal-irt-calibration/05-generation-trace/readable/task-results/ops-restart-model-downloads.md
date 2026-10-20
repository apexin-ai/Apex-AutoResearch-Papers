# ops restart model downloads

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-model-downloads_20260518T162814_result.json`
- **Structured JSON:** [`3495e999177885a4a875.json`](../../sessions/34/3495e999177885a4a875.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**不需要重启 — 三个下载进程都在活跃下载中。**

之前的 xet-bridge timeout 已经自动恢复（`--max-workers 1` 和 `HF_HUB_DISABLE_XET=1` 帮助了稳定性）。所有 `.incomplete` 文件的时间戳都在最近几分钟内（00:20-00:29），确认正在写入。

当前状态汇总：

| 模型 | PID | 完成 shards | 正在下载 | 进度估算 |
|------|-----|------------|---------|---------|
| **OLMo-2-7B** | 35305 | 4/6 | 00003 (~4.1G), 00004 (~450M) | ~70% |
| **Gemma-2-9B** | 35312 | 7/8 | 00006 (~900M/~5G) | ~90% |
| **Phi-4** | 19608 | 4/6 | 00004 (~4.1G), 00005 (~4.0G) | ~65% |

- 磁盘空间充足：124G free
- Gemma-2 最接近完成（只差 1 个 shard）
- 所有进程都在通过 xet-bridge timeout 自动重试，无需人工干预

---
