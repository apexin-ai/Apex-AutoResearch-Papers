# fix d041 method drafts

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d041-method-drafts_20260515T020954_result.json`
- **Structured JSON:** [`d18d8e5e9f6b78d23e57.json`](../../sessions/d1/d18d8e5e9f6b78d23e57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改已完成且验证通过。`experiment_setup_v1.md` 无 dataflow-aware 排序描述，无需修改。

修改汇总：

| 文件 | 修改内容 |
|------|---------|
| **method_v1.md** (×2) | 公式 `sim(E_θ0)` → `BM25(q,f)`；约束 `f ∉ R_G` → `f ∈ R_G`；"structurally disconnected" → "structurally connected"；`E*` 改为 2-hop bounded；Difficulty Gradient 段同步修正 |
| **experiments_v1.md** (×2) | "selecting by embedding distance" → "rank them by BM25 to select top-K negatives" |
| **introduction_v2.md** (×2) | "filters structurally connected files from the embedding-distance candidate set" → "selects negatives from structurally connected files ranked by BM25" |
| **experiment_setup_v1.md** | 无改动（不含 dataflow-aware 排序描述） |

所有修改文件末尾已添加 `&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->`。embedding-distance 策略描述未改动。

---
