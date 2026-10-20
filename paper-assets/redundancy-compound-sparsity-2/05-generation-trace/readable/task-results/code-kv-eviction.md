# code kv eviction

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kv_eviction_20260512T093327_result.json`
- **Structured JSON:** [`91a9aae21570ff557e0b.json`](../../sessions/91/91a9aae21570ff557e0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已创建、语法验证通过、已注册。

实现概要：

- **`CARCKVEviction`** — 核心类，维护 per-position cumulative EMA score registry
  - `update_scores()` — 支持多种输入 shape（scalar / (seq_len,) / (batch, seq_len) / (batch, num_layers, 1)），累积到内部 score 向量
  - `should_evict()` — cache_length > budget 时触发
  - `compute_eviction_mask()` — 保护 position 0（attention sink）和最后 grace_window 个 token，在可驱逐区间按 cumulative score 降序选 top-k 驱逐，eviction 后自动 compact 内部 scores
  - `apply_eviction()` — 兼容 DynamicCache（key_cache/value_cache lists）和 legacy tuple format，按 seq_len 维度 mask 过滤
  - `eviction_stats()` / `reset()` — 统计和重置

- **`create_eviction_hook()`** — 返回可在每个 generation step 调用的 hook，自动计算 EMA scores → 更新 → 判断 → 驱逐

---
