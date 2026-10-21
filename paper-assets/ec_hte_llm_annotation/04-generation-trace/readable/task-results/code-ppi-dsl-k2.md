# code ppi dsl k2

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ppi-dsl-k2_20260522T045457_result.json`
- **Structured JSON:** [`35a3e526e44a1d32dab9.json`](../../sessions/35/35a3e526e44a1d32dab9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

**EC-HTE 在 K=2 TweetEval DGP 下没有在任何 n 值胜出 Global**，与 exp-006 的预测不符。

### EC-HTE vs Global 平均 RMSE

| n_expert | EC-HTE | Global | Winner |
|----------|--------|--------|--------|
| 100 | 1.558 | 0.132 | Global |
| 250 | 0.185 | 0.124 | Global |
| 500 | 0.132 | 0.117 | Global |

### 原因分析

1. **子群大小不平衡**：TweetEval 中 hashtag 率约 25-30%，S1 远小于 S0。n=100 时 S1 只分到约 25 个 expert label，导致 per-subgroup CM 估计爆炸（S1 的 RMSE 高达 4.1）。

2. **K=2 的 partial pooling 杠杆不足**：只有 2 个子群可供 HB 借力，shrinkage 效果微弱，EC-HTE ≈ Strat MLE。

3. **exp-006 差异**：exp-006 用平衡 DGP（子群等大），crossover 在 n=250。TweetEval 的不平衡子群把 crossover 推到更高的 n。

### 产出文件
- `results/exp023_ppi_dsl_k2.csv`（聚合指标）
- `results/exp023_ppi_dsl_k2_raw.csv`（3150 行原始数据）
- 分析报告已注册到 artifacts

---
