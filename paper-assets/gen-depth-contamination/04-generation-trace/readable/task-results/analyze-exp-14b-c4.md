# analyze exp 14b c4

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_14b_c4_20260518T082213_result.json`
- **Structured JSON:** [`0739d561fe5a04e628e1.json`](../../sessions/07/0739d561fe5a04e628e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据完整，depth_0~5 各 5000 行。无 bootstrap CI 文件。结果汇总：

```json
{
  "k_star": 2,
  "auc": {"0v1": 0.96, "1v2": 0.6211, "2v3": 0.5494, "3v4": 0.5243, "4v5": 0.5152},
  "jsd": {"0v1": 0.109709, "1v2": 0.01123, "2v3": 0.006152, "3v4": 0.004436, "4v5": 0.003589},
  "ordinal": {"mae": 1.2266, "accuracy": 0.3497},
  "top_features": ["freq_entropy", "surp_d1_skew", "surp_std", "surp_d1_mean", "surp_d2_mean", "freq_kurtosis", "surp_mean", "surp_kurt", "surp_skew", "hapax_ratio"],
  "bootstrap_ci": null,
  "conclusion": "success",
  "summary": "Qwen2.5-14B on C4 confirms K*=2 (1v2 AUC=0.6211, 2v3 AUC=0.5494), consistent with 1.5B/7B/8B results — K*=2 dominant mode is stable across 1.5B–14B scale."
}
```

**关键观察**：
- **K\*=2 确认**：1v2 AUC=0.6211 > 0.60 阈值，2v3 AUC=0.5494 < 0.60，与 1.5B/7B/8B 完全一致
- **0v1 AUC=0.96**：14B 的 depth-0 vs depth-1 区分度极高，与其他规模类似
- **1v2 AUC=0.6211**：比 1.5B 的 ~0.62-0.64 略低但仍在阈值之上，5-fold 各 fold 稳定在 0.61-0.63
- **JSD 模式**：0v1 JSD=0.1097 远高于后续 pair，1v2 后急剧衰减，符合预期的指数衰减模式
- **Feature importance**：freq_entropy 和 surp_d1_skew 为 top-2，与之前实验一致

Hypothesis 验证通过：K\*=2 在 Qwen 系列 1.5B→7B→14B 均稳定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "k_star": 2,
    "auc": {
      "0v1": 0.96,
      "1v2": 0.6211,
      "2v3": 0.5494,
      "3v4": 0.5243,
      "4v5": 0.5152
    },
    "jsd": {
      "0v1": 0.109709,
      "1v2": 0.01123,
      "2v3": 0.006152,
      "3v4": 0.004436,
      "4v5": 0.003589
    },
    "ordinal": {
      "mae": 1.2266,
      "accuracy": 0.3497
    },
    "top_features": [
      "freq_entropy",
      "surp_d1_skew",
      "surp_std",
      "surp_d1_mean",
      "surp_d2_mean",
      "freq_kurtosis",
      "surp_mean",
      "surp_kurt",
      "surp_skew",
      "hapax_ratio"
    ],
    "bootstrap_ci": null,
    "conclusion": "success",
    "summary": "Qwen2.5-14B on C4 confirms K*=2 (1v2 AUC=0.6211, 2v3 AUC=0.5494), consistent with 1.5B/7B/8B results — K*=2 dominant mode is stable across 1.5B–14B scale."
  }
}
```

</details>

---
