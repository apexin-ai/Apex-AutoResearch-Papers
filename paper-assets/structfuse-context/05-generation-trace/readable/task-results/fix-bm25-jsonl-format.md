# fix bm25 jsonl format

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bm25_jsonl_format_20260514T171535_result.json`
- **Structured JSON:** [`ca2cfbd01a051110d46e.json`](../../sessions/ca/ca2cfbd01a051110d46e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已经是正常状态，无需修复。验证结果：

**所有 6 个 BM25 JSONL 文件格式正确：**

| 文件 | lines | queries | lines==queries | bad_lines |
|------|-------|---------|----------------|-----------|
| train_bm25_s42.jsonl | 11,308 | 11,308 | YES | 0 |
| train_bm25_s43.jsonl | 11,236 | 11,236 | YES | 0 |
| train_bm25_s44.jsonl | 11,264 | 11,264 | YES | 0 |
| val_bm25_s42.jsonl | 2,980 | 2,980 | YES | 0 |
| val_bm25_s43.jsonl | 3,052 | 3,052 | YES | 0 |
| val_bm25_s44.jsonl | 3,024 | 3,024 | YES | 0 |

**与 random 对照：** 三个 seed 的 bm25 行数均与 random 完全一致（s42=11308, s43=11236, s44=11264）。

每行都是合法 JSON 且包含 `query_id` 字段。这些文件可能已经被之前的操作修复过，当前状态没有任务描述中提到的问题。

---
