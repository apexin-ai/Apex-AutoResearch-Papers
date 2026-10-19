# code plan 018 bm25 phase1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_018_bm25_phase1_20260514T163821_result.json`
- **Structured JSON:** [`1b5bc605d1645937a0b4.json`](../../sessions/1b/1b5bc605d1645937a0b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Schema 完全匹配，k=50，所有字段正确。最终汇报：

---

## BM25 Negative Mining — 完成

### 数据统计

| Seed | Train records | Train size | Val records | Val size |
|------|-------------|-----------|------------|---------|
| 42 | 11308 | 1280.8 MB | 2980 | 344.6 MB |
| 43 | 11236 | 1280.9 MB | 3052 | 316.0 MB |
| 44 | 11264 | 1347.1 MB | 3024 | 295.9 MB |

Record counts 与其他策略完全一致，0 fallback。

### BM25 Score 分布 (top-50 negatives, 全部 3 seeds)
- count: 392,954
- mean: 246.50, std: 155.96
- 25%: 128.38, 50%: 228.41, 75%: 347.85
- max: 2585.74

### 重叠率 (averaged across seeds)

| 对比 | Mean overlap | Median |
|------|-------------|--------|
| BM25 vs embedding_distance | ~87.1% | 1.000 |
| BM25 vs random | ~76.2% | 1.000 |
| BM25 vs dataflow_aware | ~71.8% | 0.787 |

**解读**：BM25 与 embedding_distance 高度重叠（87%），因为两者都选 "hard" negatives（lexically/semantically similar）。与 random 重叠 76% 是因为小 repo 候选池<50 导致所有策略完全重合（median=1.0）。BM25 与 dataflow_aware 重叠最低（72%），因为后者排除了 call-graph 连接的文件。

### 值得注意的发现
- **高 median=1.0**：说明大量 repo 的候选池 ≤50 个文件，导致所有策略选出的 negatives 完全一致。BM25 的 differentiation 主要体现在大 repo 上（dataflow_aware overlap median=0.78 说明了这一点）。
- **BM25 tokenization**：使用了 code-aware tokenization（camelCase/snake_case 分割 + 标点分割 + 小写 + 过滤长度≤1 的 token），比原始 `dataflow_aware` 中使用的简单 `.split()` 更精细。

### 文件路径
- 脚本：`/root/structfuse/scripts/mine_bm25_negatives.py`
- 输出：`/root/autodl-tmp/structfuse/full_m2_training_data/train_bm25_s{42,43,44}.jsonl`
- 输出：`/root/autodl-tmp/structfuse/full_m2_training_data/val_bm25_s{42,43,44}.jsonl`

---
