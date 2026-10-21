# analysis qwen25 14b topk50

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen25_14b_topk50_20260520T053249_result.json`
- **Structured JSON:** [`3c674a25cca254c2e7ee.json`](../../sessions/3c/3c674a25cca254c2e7ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果

**qwen25_14b_topk50 → SUCCESS**

| Metric | Value |
|--------|-------|
| RF 4-class acc | **47.93%** [47.26%, 48.59%] |
| LR 4-class acc | 43.95% |
| RF 3-class (no d0) | 51.64% |
| d0v3 AUC | 0.9253 |
| d1v2 AUC | 0.6868 |
| d2v3 AUC | 0.6788 |

### 14B 三策略对比

| Strategy | RF 4-class |
|----------|-----------|
| nucleus | 54.05% |
| temp 0.9 | 50.50% |
| **top-k 50** | **47.93%** |

Top-k 是最难的采样策略，但仍然接近 2× 随机基线（25%）。三种策略排序 nucleus > temp > topk 与 1.5B scale 一致。

特征重要性有变化：top-k 下词汇多样性特征（TTR, hapax_ratio）排名上升，高于纯 perplexity 统计量，说明 top-k 的截断效应使判别信号从 perplexity 尾部转移到词汇分布。

Registry 已更新为 DONE/success，报告已注册。

---
