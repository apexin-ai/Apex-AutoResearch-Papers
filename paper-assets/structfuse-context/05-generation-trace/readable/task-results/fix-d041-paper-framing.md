# fix d041 paper framing

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d041-paper-framing_20260515T020943_result.json`
- **Structured JSON:** [`745d146abbcb8fafd69c.json`](../../sessions/74/745d146abbcb8fafd69c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成三处修改：

1. **Formal Definition 公式**：`argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)` → `argmax_{x ∈ D : reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)`，并补充说明"Negatives are selected from CodeQL-connected files (structural filtering), ranked by BM25 (lexical similarity)"

2. **Core Insight 三策略难度维度**：插入 `(1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking)`，同步将"orthogonal signal dimension (structure)"改为"(structure + lexical)"

3. **文件末尾**：添加 `&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->`

embedding-distance 策略的描述未改动。

---
