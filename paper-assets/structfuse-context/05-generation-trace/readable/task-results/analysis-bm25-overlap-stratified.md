# analysis bm25 overlap stratified

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bm25_overlap_stratified_20260514T170408_result.json`
- **Structured JSON:** [`b93aaee524de34735068.json`](../../sessions/b9/b93aaee524de34735068.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分层结果清晰，验证了 Director 的假设：

| Tier | Repos | Instances | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |
|------|-------|-----------|-------------------|----------------|------------------|
| **small** (<50 files) | 46 | 4,467 | **88.2%** | **88.2%** | 74.3% |
| **medium** (50-200) | 29 | 3,300 | **68.0%** | **53.5%** | 53.8% |
| **large** (200+) | 8 | 601 | **28.0%** | **7.1%** | 17.6% |
| overall | 83 | 8,368 | 75.9% | 68.7% | 62.2% |

关键发现：
- **小 repo** 候选池平均仅 25 个文件，所有策略被迫选相同 negatives（embedding 和 random 与 BM25 重合度完全相同，88.2%）
- **中 repo** 开始分化，BM25 vs random 降到 53.5%
- **大 repo**（平均 315 文件）差异巨大，BM25 vs random 仅 7.1%，vs embedding 仅 28.0%——BM25 在大 repo 上选出的 negatives 与其他策略截然不同

overlap 指标：`|BM25_negs ∩ other_negs| / |BM25_negs|`。小 repo 的 neg 数量平均只有 23（远低于 50 上限），候选池太小无选择余地。

---
