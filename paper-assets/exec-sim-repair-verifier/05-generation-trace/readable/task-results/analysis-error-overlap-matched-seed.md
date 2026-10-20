# analysis error overlap matched seed

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error-overlap-matched-seed_20260512T190303_result.json`
- **Structured JSON:** [`fc07356d987e6ddfbea9.json`](../../sessions/fc/fc07356d987e6ddfbea9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 每个 Seed 的指标表

| 指标 | Seed 0 | Seed 42 | Seed 456 |
|------|--------|---------|----------|
| n_samples | 1890 | 1890 | 1890 |
| cls_accuracy | 87.78 | 87.83 | 87.88 |
| cwm_accuracy | 87.57 | 87.51 | 86.98 |
| both_correct | 1611 | 1601 | 1610 |
| cls_only_wrong | 44 | 53 | 34 |
| cwm_only_wrong | 48 | 59 | 51 |
| both_wrong | 187 | 177 | 195 |
| total_errors | 279 | 289 | 280 |
| oracle_correct | 1703 | 1713 | 1695 |
| oracle_accuracy | 90.11 | 90.63 | 89.68 |
| jaccard_overlap | 0.6703 | 0.6125 | 0.6964 |
| complementarity_rate | 0.3297 | 0.3875 | 0.3036 |
| cls_unique_error_rate | 15.77% | 18.34% | 12.14% |
| cwm_unique_error_rate | 17.20% | 20.42% | 18.21% |

## 聚合结果 (3 seeds)

| 指标 | 值 |
|------|-----|
| mean_cls_accuracy | 87.83 |
| mean_cwm_accuracy | 87.35 |
| mean_oracle_accuracy | 90.14 |
| mean_complementarity_rate | 0.3403 |
| mean_jaccard_overlap | 0.6597 |
| mean_cls_unique_error_rate | 15.42% |
| mean_cwm_unique_error_rate | 18.61% |
| oracle_gain_over_cls | +2.31 |
| oracle_gain_over_cwm | **30.05 (bug)** |

**注意：`oracle_gain_over_cwm` 值 30.05 是脚本 bug**。base64 脚本中该行计算为 `sum / n / n`（除了两次 n），正确值应为 `90.14 - 87.35 = 2.79`。

## error_overlap_matched_seed.json 完整内容

```json
{
  "per_seed": [
    {
      "seed": 0,
      "n_samples": 1890,
      "cls_accuracy": 87.78,
      "cwm_accuracy": 87.57,
      "both_correct": 1611,
      "cls_only_wrong": 44,
      "cwm_only_wrong": 48,
      "both_wrong": 187,
      "total_errors": 279,
      "oracle_correct": 1703,
      "oracle_accuracy": 90.11,
      "jaccard_overlap": 0.6703,
      "complementarity_rate": 0.3297,
      "cls_unique_error_rate": 15.77,
      "cwm_unique_error_rate": 17.2
    },
    {
      "seed": 42,
      "n_samples": 1890,
      "cls_accuracy": 87.83,
      "cwm_accuracy": 87.51,
      "both_correct": 1601,
      "cls_only_wrong": 53,
      "cwm_only_wrong": 59,
      "both_wrong": 177,
      "total_errors": 289,
      "oracle_correct": 1713,
      "oracle_accuracy": 90.63,
      "jaccard_overlap": 0.6125,
      "complementarity_rate": 0.3875,
      "cls_unique_error_rate": 18.34,
      "cwm_unique_error_rate": 20.42
    },
    {
      "seed": 456,
      "n_samples": 1890,
      "cls_accuracy": 87.88,
      "cwm_accuracy": 86.98,
      "both_correct": 1610,
      "cls_only_wrong": 34,
      "cwm_only_wrong": 51,
      "both_wrong": 195,
      "total_errors": 280,
      "oracle_correct": 1695,
      "oracle_accuracy": 89.68,
      "jaccard_overlap": 0.6964,
      "complementarity_rate": 0.3036,
      "cls_unique_error_rate": 12.14,
      "cwm_unique_error_rate": 18.21
    }
  ],
  "aggregated": {
    "mean_cls_accuracy": 87.83,
    "mean_cwm_accuracy": 87.35,
    "mean_oracle_accuracy": 90.14,
    "mean_complementarity_rate": 0.3403,
    "mean_jaccard_overlap": 0.6597,
    "mean_cls_unique_error_rate": 15.42,
    "mean_cwm_unique_error_rate": 18.61,
    "oracle_gain_over_cls": 2.31,
    "oracle_gain_over_cwm": 30.05
  }
}
```

`oracle_gain_over_cwm` 的正确值应为 **2.79**（= 90.14 - 87.35），JSON 中的 30.05 是脚本 bug 产生的错误值。其余指标均正确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "per_seed": [
      {
        "seed": 0,
        "n_samples": 1890,
        "cls_accuracy": 87.78,
        "cwm_accuracy": 87.57,
        "both_correct": 1611,
        "cls_only_wrong": 44,
        "cwm_only_wrong": 48,
        "both_wrong": 187,
        "total_errors": 279,
        "oracle_correct": 1703,
        "oracle_accuracy": 90.11,
        "jaccard_overlap": 0.6703,
        "complementarity_rate": 0.3297,
        "cls_unique_error_rate": 15.77,
        "cwm_unique_error_rate": 17.2
      },
      {
        "seed": 42,
        "n_samples": 1890,
        "cls_accuracy": 87.83,
        "cwm_accuracy": 87.51,
        "both_correct": 1601,
        "cls_only_wrong": 53,
        "cwm_only_wrong": 59,
        "both_wrong": 177,
        "total_errors": 289,
        "oracle_correct": 1713,
        "oracle_accuracy": 90.63,
        "jaccard_overlap": 0.6125,
        "complementarity_rate": 0.3875,
        "cls_unique_error_rate": 18.34,
        "cwm_unique_error_rate": 20.42
      },
      {
        "seed": 456,
        "n_samples": 1890,
        "cls_accuracy": 87.88,
        "cwm_accuracy": 86.98,
        "both_correct": 1610,
        "cls_only_wrong": 34,
        "cwm_only_wrong": 51,
        "both_wrong": 195,
        "total_errors": 280,
        "oracle_correct": 1695,
        "oracle_accuracy": 89.68,
        "jaccard_overlap": 0.6964,
        "complementarity_rate": 0.3036,
        "cls_unique_error_rate": 12.14,
        "cwm_unique_error_rate": 18.21
      }
    ],
    "aggregated": {
      "mean_cls_accuracy": 87.83,
      "mean_cwm_accuracy": 87.35,
      "mean_oracle_accuracy": 90.14,
      "mean_complementarity_rate": 0.3403,
      "mean_jaccard_overlap": 0.6597,
      "mean_cls_unique_error_rate": 15.42,
      "mean_cwm_unique_error_rate": 18.61,
      "oracle_gain_over_cls": 2.31,
      "oracle_gain_over_cwm": 30.05
    }
  }
}
```

</details>

---
