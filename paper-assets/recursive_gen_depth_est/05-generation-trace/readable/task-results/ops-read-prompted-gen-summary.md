# ops read prompted gen summary

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-prompted-gen-summary_20260518T040930_result.json`
- **Structured JSON:** [`cbbc1e74237494486c91.json`](../../sessions/cb/cbbc1e74237494486c91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

summary.json 中字段为 `top5_features`（不是 `top_features`），内容如下：

```json
{
  "experiment": "prompted_gen_gpt2xl_001",
  "model": "gpt2-xl",
  "reference_model": "pythia-1.4b",
  "generation_mode": "topic_prompted",
  "num_prompts": 50,
  "samples_per_prompt": 100,
  "samples_per_depth": 5000,
  "four_class_accuracy": 0.6952,
  "accuracy_ci_95": [0.689, 0.7015],
  "fold_accuracies": [0.6885, 0.707, 0.6987, 0.6943, 0.6877],
  "pairwise_auc": {
    "d0_vs_d1": 0.9162,
    "d0_vs_d2": 0.9934,
    "d0_vs_d3": 0.9974,
    "d1_vs_d2": 0.7823,
    "d1_vs_d3": 0.9553,
    "d2_vs_d3": 0.7444
  },
  "top5_features": [
    ["p90_ppl", 0.1887],
    ["p75_ppl", 0.1335],
    ["mean_surprisal", 0.0916],
    ["var_surprisal", 0.0849],
    ["p50_ppl", 0.0612]
  ],
  "baseline_bos_seeded_acc": 0.833,
  "delta_vs_baseline_pp": -13.78,
  "elapsed_hours": 5.14
}
```

**top5_features 完整列表：**

| Rank | Feature | Importance |
|------|---------|-----------|
| 1 | p90_ppl | 0.1887 |
| 2 | p75_ppl | 0.1335 |
| 3 | mean_surprisal | 0.0916 |
| 4 | var_surprisal | 0.0849 |
| 5 | p50_ppl | 0.0612 |

目录下只有 `summary.json` 一个文件，无其他 feature_importance 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment": "prompted_gen_gpt2xl_001",
    "model": "gpt2-xl",
    "reference_model": "pythia-1.4b",
    "generation_mode": "topic_prompted",
    "num_prompts": 50,
    "samples_per_prompt": 100,
    "samples_per_depth": 5000,
    "four_class_accuracy": 0.6952,
    "accuracy_ci_95": [
      0.689,
      0.7015
    ],
    "fold_accuracies": [
      0.6885,
      0.707,
      0.6987,
      0.6943,
      0.6877
    ],
    "pairwise_auc": {
      "d0_vs_d1": 0.9162,
      "d0_vs_d2": 0.9934,
      "d0_vs_d3": 0.9974,
      "d1_vs_d2": 0.7823,
      "d1_vs_d3": 0.9553,
      "d2_vs_d3": 0.7444
    },
    "top5_features": [
      [
        "p90_ppl",
        0.1887
      ],
      [
        "p75_ppl",
        0.1335
      ],
      [
        "mean_surprisal",
        0.0916
      ],
      [
        "var_surprisal",
        0.0849
      ],
      [
        "p50_ppl",
        0.0612
      ]
    ],
    "baseline_bos_seeded_acc": 0.833,
    "delta_vs_baseline_pp": -13.78,
    "elapsed_hours": 5.14
  }
}
```

</details>

---
