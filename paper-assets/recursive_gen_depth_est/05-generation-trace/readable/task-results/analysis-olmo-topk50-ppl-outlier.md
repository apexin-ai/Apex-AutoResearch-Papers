# analysis olmo topk50 ppl outlier

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_olmo_topk50_ppl_outlier_20260515T043814_result.json`
- **Structured JSON:** [`a5081e4ccaa33567c109.json`](../../sessions/a5/a5081e4ccaa33567c109.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 核心发现

**1 个样本贡献了 depth-1 mean_ppl 总和的 94.4%**（sample_id=6923, mean_ppl=1.43e13, 但 p90_ppl 仅 105.3）。少量 token 的灾难性预测失败主导了 sample-level mean。

### mean_ppl 无法修复

即使用最激进的过滤（剔除 >1e6 或 trimming 到 p99），mean_ppl 的 depth 排序仍然非单调：
- 原始: 2.96e4 → **3.03e9** → 1.88e8 → 1.75e6
- 剔除 >1e6: 17484 → 21794 → **29779** → 14723（depth 0→2 反而递增）

### p90_ppl 完美单调

566.8 → 143.0 → 91.7 → 73.1，无需任何过滤。Spearman ρ = −0.853 vs mean_ppl 的 −0.406。

### 根因

Token-level perplexity 分布极度重尾（depth 1-2 的 kurtosis > 4900），CV 达 67×。p90_ppl 的 CV 仅 0.28-0.67，skewness < 1，接近高斯分布。

### 论文用文本

已写入 artifact，3 句话解释 percentile-based features 优于 mean-based 的统计机制。

产出文件: `artifacts/olmo_topk50_mean_ppl_outlier_analysis.md`

---
