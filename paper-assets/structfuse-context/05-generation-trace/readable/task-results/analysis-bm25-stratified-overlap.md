# analysis bm25 stratified overlap

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bm25_stratified_overlap_20260514T170331_result.json`
- **Structured JSON:** [`8f5beeff794ba3fa4326.json`](../../sessions/8f/8f5beeff794ba3fa4326.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**分层后 BM25 与其他策略的 top-7 Jaccard 重叠率差异巨大：**

| 层级 | Repos | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |
|------|-------|-------------------|----------------|------------------|
| Small (<50) | 39 | 0.668 | 0.411 | 0.667 |
| Medium (50-200) | 29 | 0.380 | 0.067 | 0.363 |
| Large (200+) | 15 | 0.297 | 0.007 | 0.405 |

关键点：

1. **小 repo 重叠高但不是 1.0**：平均 pool 只有 22.3 个候选，取 top-7 时各策略仍有 ~33% 差异（Jaccard 0.67 而非 1.0），说明即使候选池小，BM25 排序与 embedding/dataflow 排序也不同。

2. **大 repo BM25 vs random 几乎为零**（0.007）：候选池 200+ 文件，随机抽 7 个和 BM25 top-7 基本不重合——BM25 确实在做有意义的筛选。

3. **BM25 vs dataflow 在大 repo 反而高于 vs embedding**（0.405 > 0.297）：大 repo 中 BM25 的词汇相似性信号与数据流依赖比与纯嵌入距离更一致。

4. **matched_queries 只有 2920/12290**：因 BM25 和其他策略的 train/val 划分不同，只有约 24% 的 query 能做配对比较。

脚本：`/root/structfuse/scripts/analyze_bm25_overlap_stratified.py`
产出：`artifacts/bm25_overlap_stratified.json`

---
