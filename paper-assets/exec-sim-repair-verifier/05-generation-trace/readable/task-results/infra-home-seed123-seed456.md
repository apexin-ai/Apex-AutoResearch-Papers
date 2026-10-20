# infra home seed123 seed456

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_home-seed123-seed456_20260512T074551_result.json`
- **Structured JSON:** [`b4a1eadb3280408ee34c.json`](../../sessions/b4/b4a1eadb3280408ee34c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_traj_seed123.json 完整内容

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

**traj-level-seed456 已提交。** PID 2542385，日志 `~/runs/exec-sim-repair-verifier/traj-level-seed456.log`。

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
