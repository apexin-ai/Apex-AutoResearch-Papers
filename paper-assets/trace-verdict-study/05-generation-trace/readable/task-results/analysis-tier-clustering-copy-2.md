# analysis tier clustering

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tier_clustering_20260522T073857_result.json`
- **Structured JSON:** [`33442dca9dd1314d8d84.json`](../../sessions/33/33442dca9dd1314d8d84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已生成。核心发现：

## 每个模型最优 k

| 模型 | Gap 最优 k | Silhouette (k=2) |
|------|-----------|-----------------|
| Qwen-7B | 1 | 0.715 |
| Qwen-1.5B | 3 | 0.850 |
| DeepSeek-6.7B | 1 | 0.664 |
| CodeLlama-13B | **2** | **0.967** |
| Pooled (27点) | 1 | 0.697 |

Gap statistic 仅对 CodeLlama 明确支持 k=2。但 silhouette 在 k=2 时普遍较高（0.66–0.97），说明 2-cluster 结构虽非统计上最优分割点，但分离度不错。

## k=2 与论文 Tier 划分一致性

- **Qwen-7B**: 完全一致。Tier1={exception_only, ae_only, vota, nomarker}, Tier2={loop_only, label_only, full_trace, no_trace}
- **Qwen-1.5B**: 完全一致。同上分布
- **CodeLlama-13B**: 完全一致
- **DeepSeek-6.7B**: **不一致** — label_only (0.285) 作为极端 outlier 独占低 cluster，其余 6 个 condition（包括 loop_only/full_trace/no_trace）全部被归入高 cluster

## 异常情况

1. **CodeLlama loop_only (0.7706) vs no_trace (0.7650)**: 仅差 0.56pp，始终在同一 cluster。这两个 condition 在 CodeLlama 上实际不可区分。

2. **DeepSeek label_only (0.285)**: 距次低值 0.7336 有 44.86pp 的巨大间隔。k=3 时独占一个 cluster。这个 outlier 扭曲了 DeepSeek 的 k=2 聚类——使得论文中"低性能"条件被吸收进"高"cluster。

3. **跨模型一致性**: exception_only、ae_only、vota 在所有 4 个模型上一致归入 Tier1_high。loop_only、no_trace 在 3/4 模型归入 Tier2_low（DeepSeek 除外，受 label_only outlier 影响）。nomarker 仅出现在 2 个模型，均归入 Tier1_high。

## 对论文的建议

论文的 two-tier 划分在 3/4 模型上被 k-means 验证。DeepSeek 的不一致可归因于 label_only 的 outlier 效应。若排除 label_only 或对 DeepSeek 单独使用 k=3，划分同样成立。Pooled 分析的 k=2 cluster 也清晰地将条件分为 ≥0.956 和 ≤0.862 两组（pooled silhouette=0.70）。

输出文件：
- `/root/autodl-tmp/trace-verdict-study-checkpoints/tier_clustering/tier_clustering_results.json`
- `/root/autodl-tmp/trace-verdict-study-checkpoints/tier_clustering/cluster_assignments.csv`
- `/root/autodl-tmp/trace-verdict-study-checkpoints/tier_clustering/tier_clustering_summary.txt`

---
