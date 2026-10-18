# util qwen72b download

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_util_qwen72b_download_20260514T134813_result.json`
- **Structured JSON:** [`e6bfd1edbc67614f901b.json`](../../sessions/e6/e6bfd1edbc67614f901b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**模型尚未下载，但磁盘空间不足。**

当前状态：
- `/root/autodl-tmp/` 总共 250GB，已用 152GB，剩余 **99GB**
- `.hf_cache/` 占用 53GB
- Qwen2.5-72B 模型约需 **140GB**（FP16 权重）
- **缺口约 41GB，无法开始下载**

需要先清理磁盘腾出空间，或者确认是否可以删除 `.hf_cache/` 中已有的部分模型。要我查看缓存目录里有哪些模型，评估哪些可以清理？

---
