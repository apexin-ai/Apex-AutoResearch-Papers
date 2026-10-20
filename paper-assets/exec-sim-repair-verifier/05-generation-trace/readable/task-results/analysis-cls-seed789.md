# analysis cls seed789

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls-seed789_20260512T112455_result.json`
- **Structured JSON:** [`13a657a6eb9e9a07f1e2.json`](../../sessions/13/13a657a6eb9e9a07f1e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练和评估均正常完成，checkpoint 存在。

```json
{
  "seed": 789,
  "status": "COMPLETED",
  "accuracy": 88.99,
  "per_class": {
    "pass": { "precision": 93.26, "recall": 84.87, "f1": 88.87 },
    "fail": { "precision": 85.20, "recall": 93.42, "f1": 89.12 }
  },
  "confusion_matrix": { "tn": 852, "fp": 60, "fn": 148, "tp": 830 },
  "unparseable_predictions": 0,
  "train_loss": 0.2357,
  "eval_loss": 0.0871,
  "train_runtime_sec": 3433.07,
  "train_samples_per_second": 13.361,
  "checkpoint_path": "/home/sonny/exec-sim-repair-verifier/checkpoints_seed789/best/",
  "checkpoint_confirmed": true,
  "warnings": [],
  "mvp_b_criteria": "PASS"
}
```

**4-seed 汇总：**

| Seed | Accuracy | Pass F1 | Fail F1 |
|------|----------|---------|---------|
| 42   | 87.83    | 88.06   | 87.59   |
| 123  | 89.52    | 89.64   | 89.40   |
| 456  | 87.88    | 87.53   | 88.21   |
| **789** | **88.99** | **88.87** | **89.12** |
| **Mean** | **88.56** | **88.53** | **88.58** |
| **Std**  | **0.77**  | **0.89**  | **0.76**  |

seed789 accuracy=88.99 在正常范围内（87-90%），与 seed123 接近，标准差 <1pp，结果稳定。还差 seed 1 个即可完成 5-seed comparison。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "seed": 789,
    "status": "COMPLETED",
    "accuracy": 88.99,
    "per_class": {
      "pass": {
        "precision": 93.26,
        "recall": 84.87,
        "f1": 88.87
      },
      "fail": {
        "precision": 85.2,
        "recall": 93.42,
        "f1": 89.12
      }
    },
    "confusion_matrix": {
      "tn": 852,
      "fp": 60,
      "fn": 148,
      "tp": 830
    },
    "unparseable_predictions": 0,
    "train_loss": 0.2357,
    "eval_loss": 0.0871,
    "train_runtime_sec": 3433.07,
    "train_samples_per_second": 13.361,
    "checkpoint_path": "/home/sonny/exec-sim-repair-verifier/checkpoints_seed789/best/",
    "checkpoint_confirmed": true,
    "warnings": [],
    "mvp_b_criteria": "PASS"
  }
}
```

</details>

---
