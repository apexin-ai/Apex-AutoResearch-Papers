# merge qwen06b shards

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_merge_qwen06b-shards_20260514T230234_result.json`
- **Structured JSON:** [`be6bff8fd860217eef90.json`](../../sessions/be/be6bff8fd860217eef90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

合并结果：

| 指标 | 值 |
|------|-----|
| 总行数 | 4538 |
| Unique seeds | 996 |
| Depth 分布 | {0: 996, 1: 986, 2: 938, 3: 840, 4: 778} |
| 文件大小 | 4.75 MB |
| JSON 错误 | 0 |

合并成功，无数据损坏。996 个 unique seeds（预期 ~996，两个 shard 各 ~498），depth 0-4 分布合理，逐层递减符合生成深度衰减预期。

---
