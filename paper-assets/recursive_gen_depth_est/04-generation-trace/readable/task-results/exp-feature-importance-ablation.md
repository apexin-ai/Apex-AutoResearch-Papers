# exp feature importance ablation

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_feature_importance_ablation_20260517T205142_result.json`
- **Structured JSON:** [`7d89e63b2e02639006c5.json`](../../sessions/7d/7d89e63b2e02639006c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `results/feature_importance_ablation.json`。

## 结果摘要

### Group Ablation (leave-one-model-out CV, 4-class accuracy)

| Group | #Features | Accuracy | Delta |
|---|---|---|---|
| **Full model (all 19)** | 19 | **0.6655** | — |
| Perplexity only | 9 | 0.6601 | -0.0054 |
| Entropy/Surprisal only | 5 | 0.6319 | -0.0336 |
| Repetition/Diversity only | 5 | 0.5297 | -0.1358 |

### Feature Importance Ranking (top 10)

| Rank | Feature | Importance |
|---|---|---|
| 1 | p90_ppl | 0.2242 |
| 2 | var_surprisal | 0.1884 |
| 3 | mean_surprisal | 0.0909 |
| 4 | p75_ppl | 0.0901 |
| 5 | type_token_ratio | 0.0490 |
| 6 | p50_ppl | 0.0417 |
| 7 | hapax_ratio | 0.0383 |
| 8 | entropy_of_surprisal | 0.0361 |
| 9 | p25_ppl | 0.0347 |
| 10 | skewness_ppl | 0.0287 |

关键发现：
- **Perplexity 组单独就能达到 66.0%**，仅比全特征低 0.5 个点，是最强特征组
- Top-2 特征（p90_ppl + var_surprisal）占总 importance 的 41%
- mean_ppl 和 var_ppl importance 接近零（被 percentile 特征替代）
- Repetition/Diversity 组单独只有 53.0%，贡献最弱

---
