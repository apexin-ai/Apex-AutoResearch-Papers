# infra read seed123 submit seed456

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_read-seed123-submit-seed456_20260512T070033_result.json`
- **Structured JSON:** [`c9f56f3431697786c7f4.json`](../../sessions/c9/c9f56f3431697786c7f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_traj_seed123.json

```json
{
  "test_set_size": 1032,
  "class_balance": {
    "resolved": 479,
    "unresolved": 553,
    "resolved_pct": 46.4
  },
  "majority_baseline_accuracy": 53.59,
  "overall_accuracy": 85.47,
  "accuracy_vs_baseline_gap_pp": 31.88,
  "per_class": {
    "unresolved": {
      "precision": 83.53,
      "recall": 90.78,
      "f1": 87.0,
      "support": 553
    },
    "resolved": {
      "precision": 88.17,
      "recall": 79.33,
      "f1": 83.52,
      "support": 479
    }
  },
  "confusion_matrix": {
    "tn": 502,
    "fp": 51,
    "fn": 99,
    "tp": 380
  },
  "unparseable_predictions": 0,
  "per_test_consistency": {
    "n_compared": 1032,
    "n_consistent": 811,
    "consistency_rate": 78.59
  }
}
```

## seed456 提交状态

已提交，tmux session `traj-level-seed456` 运行中（PID 2489224）。日志显示已加载 tokenizer 和数据集（train=8052, val=1001），训练正常启动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "test_set_size": 1032,
    "class_balance": {
      "resolved": 479,
      "unresolved": 553,
      "resolved_pct": 46.4
    },
    "majority_baseline_accuracy": 53.59,
    "overall_accuracy": 85.47,
    "accuracy_vs_baseline_gap_pp": 31.88,
    "per_class": {
      "unresolved": {
        "precision": 83.53,
        "recall": 90.78,
        "f1": 87.0,
        "support": 553
      },
      "resolved": {
        "precision": 88.17,
        "recall": 79.33,
        "f1": 83.52,
        "support": 479
      }
    },
    "confusion_matrix": {
      "tn": 502,
      "fp": 51,
      "fn": 99,
      "tp": 380
    },
    "unparseable_predictions": 0,
    "per_test_consistency": {
      "n_compared": 1032,
      "n_consistent": 811,
      "consistency_rate": 78.59
    }
  }
}
```

</details>

---
