# code hgrn2 h3 1 repair v2

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hgrn2_h3_1_repair_v2_20260518T162752_result.json`
- **Structured JSON:** [`4c6f9b2d74b43b9c304c.json`](../../sessions/4c/4c6f9b2d74b43b9c304c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。文件状态汇报：

| 文件 | 修复前 | 修复后 |
|------|--------|--------|
| model-00001-of-00002.safetensors | 4.6GB (完好) | 4.6GB (未动) |
| model-00002-of-00002.safetensors | 61MB (损坏) | 88MB (232→3 keys, OK) |
| tokenizer.json | 0 字节 | 3.3MB |

两个 shard 均可正常打开 (shard-1: 232 keys, shard-2: 3 keys)，验证通过。

---
