# fix bm25 s44 alignment

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bm25_s44_alignment_20260514T171332_result.json`
- **Structured JSON:** [`a2de18163c21a52e6d93.json`](../../sessions/a2/a2de18163c21a52e6d93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件已经对齐，不存在需要修复的问题：

| split | seed | bm25 | random | 状态 |
|-------|------|------|--------|------|
| train | s42 | 11,308 | 11,308 | 已对齐 |
| train | s43 | 11,236 | 11,236 | 已对齐 |
| train | s44 | 11,264 | 11,264 | 已对齐 |
| val | s42 | 2,980 | 2,980 | 已对齐 |
| val | s43 | 3,052 | 3,052 | 已对齐 |
| val | s44 | 3,024 | 3,024 | 已对齐 |

train_bm25_s44.jsonl 现在是 11,264 行，与 train_random_s44.jsonl 完全一致。val 文件同样对齐。这个问题看起来已经被修复过了，无需再操作。

---
