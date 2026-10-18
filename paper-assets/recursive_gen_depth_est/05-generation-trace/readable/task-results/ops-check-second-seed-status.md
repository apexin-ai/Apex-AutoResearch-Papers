# ops check second seed status

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_second_seed_status_20260517T043444_result.json`
- **Structured JSON:** [`7b8123d61e093eae5ac4.json`](../../sessions/7b/7b8123d61e093eae5ac4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态：已完成 (completed)**

`summary.json` 已生成，实验结束。完整结果：

```json
{
  "seed": 43,
  "4class_acc": 0.7715,
  "ci_95": [0.764, 0.7815],
  "d1v2_auc": 0.8531,
  "delta_vs_baseline": -0.0105,
  "baseline_acc": 0.782,
  "top_features": ["var_surprisal", "p90_ppl", "mean_ppl", "var_ppl", "p75_ppl"],
  "per_class_recall": {
    "d0": 0.99,
    "d1": 0.816,
    "d2": 0.586,
    "d3": 0.694
  },
  "fold_accuracies": [0.77, 0.77, 0.79, 0.7675, 0.76]
}
```

**关键数据：**
- 4-class accuracy: **77.15%** (baseline 78.2%, delta = -1.05%)
- 95% CI: [76.4%, 78.15%]
- d1v2 AUC: 0.8531
- seed 43 的结果略低于 baseline，d2 recall 偏弱 (0.586)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "seed": 43,
    "4class_acc": 0.7715,
    "ci_95": [
      0.764,
      0.7815
    ],
    "d1v2_auc": 0.8531,
    "delta_vs_baseline": -0.0105,
    "baseline_acc": 0.782,
    "top_features": [
      "var_surprisal",
      "p90_ppl",
      "mean_ppl",
      "var_ppl",
      "p75_ppl"
    ],
    "per_class_recall": {
      "d0": 0.99,
      "d1": 0.816,
      "d2": 0.586,
      "d3": 0.694
    },
    "fold_accuracies": [
      0.77,
      0.77,
      0.79,
      0.7675,
      0.76
    ]
  }
}
```

</details>

---
