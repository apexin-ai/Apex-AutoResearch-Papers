# fix method fallback rate

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_method-fallback-rate_20260514T231101_result.json`
- **Structured JSON:** [`74407553ee800c2d813b.json`](../../sessions/74/74407553ee800c2d813b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改报告：

**Fix 1（method_v1.md line 63）— 已修正**
- 原文：`approximately 34% of training instances`
- 改为：`approximately 66% of training instances, which lack structural connectivity data and therefore cannot supply structurally disconnected candidates`
- 原因：34.3% 是 structural coverage rate（有 CodeQL 数据的比例），~66% 才是缺乏结构数据需要 fallback 的比例。与 experiments_v1.md §4.1 的 "65.7%" 一致。

**Fix 2（experiments_v1.md §4.2）— 已被其他 Worker 修正，跳过**
- 当前文本已是 "mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear)"，与 method_v1.md §3.3 一致。

---
