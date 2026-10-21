# infra read pr results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_read-pr-results_20260512T060822_result.json`
- **Structured JSON:** [`80005e61bde4ec4a2d55.json`](../../sessions/80/80005e61bde4ec4a2d55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "overall": {
    "support": 1890,
    "accuracy": 87.51,
    "confusion_matrix": { "tn": 854, "fp": 58, "fn": 178, "tp": 800 },
    "fail": { "precision": 82.75, "recall": 93.64, "f1": 87.86 },
    "pass": { "precision": 93.24, "recall": 81.80, "f1": 87.15 },
    "majority_baseline": 51.75,
    "class_balance": { "pass": 978, "fail": 912 }
  },
  "per_mutation_type": {
    "boundary_removal": { "support": 36,  "accuracy": 91.67 },
    "off_by_one":       { "support": 671, "accuracy": 82.56 },
    "operator_swap":    { "support": 298, "accuracy": 87.92 },
    "original":         { "support": 398, "accuracy": 84.17 },
    "return_value":     { "support": 402, "accuracy": 97.26 },
    "variable_swap":    { "support": 85,  "accuracy": 92.94 }
  },
  "per_problem_test_count_bucket": {
    "6-10":  { "support": 81,   "accuracy": 96.30 },
    "11+":   { "support": 1809, "accuracy": 87.12 }
  },
  "error_analysis": {
    "false_positives": {
      "count": 58,
      "by_mutation_type": { "off_by_one": 33, "return_value": 4, "operator_swap": 20, "variable_swap": 1 }
    },
    "false_negatives": {
      "count": 178,
      "by_mutation_type": { "off_by_one": 84, "return_value": 7, "operator_swap": 16, "boundary_removal": 3, "variable_swap": 5, "original": 63 }
    }
  },
  "unparseable_predictions": 0
}
```

**关键数据：**
- **Overall accuracy: 87.51%**（majority baseline 51.75%）
- **Fail 类**: precision 82.75, recall 93.64, F1 87.86
- **Pass 类**: precision 93.24, recall 81.80, F1 87.15
- 最强 mutation type: `return_value` (97.26% acc)，最弱: `off_by_one` (82.56% acc)
- FP 58 个（主要来自 off_by_one 33 + operator_swap 20），FN 178 个（off_by_one 84 + original 63 占大头）
- 少测试题（6-10 tests）准确率 96.3%，多测试题（11+）87.1%
- 0 个 unparseable predictions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "overall": {
      "support": 1890,
      "accuracy": 87.51,
      "confusion_matrix": {
        "tn": 854,
        "fp": 58,
        "fn": 178,
        "tp": 800
      },
      "fail": {
        "precision": 82.75,
        "recall": 93.64,
        "f1": 87.86
      },
      "pass": {
        "precision": 93.24,
        "recall": 81.8,
        "f1": 87.15
      },
      "majority_baseline": 51.75,
      "class_balance": {
        "pass": 978,
        "fail": 912
      }
    },
    "per_mutation_type": {
      "boundary_removal": {
        "support": 36,
        "accuracy": 91.67
      },
      "off_by_one": {
        "support": 671,
        "accuracy": 82.56
      },
      "operator_swap": {
        "support": 298,
        "accuracy": 87.92
      },
      "original": {
        "support": 398,
        "accuracy": 84.17
      },
      "return_value": {
        "support": 402,
        "accuracy": 97.26
      },
      "variable_swap": {
        "support": 85,
        "accuracy": 92.94
      }
    },
    "per_problem_test_count_bucket": {
      "6-10": {
        "support": 81,
        "accuracy": 96.3
      },
      "11+": {
        "support": 1809,
        "accuracy": 87.12
      }
    },
    "error_analysis": {
      "false_positives": {
        "count": 58,
        "by_mutation_type": {
          "off_by_one": 33,
          "return_value": 4,
          "operator_swap": 20,
          "variable_swap": 1
        }
      },
      "false_negatives": {
        "count": 178,
        "by_mutation_type": {
          "off_by_one": 84,
          "return_value": 7,
          "operator_swap": 16,
          "boundary_removal": 3,
          "variable_swap": 5,
          "original": 63
        }
      }
    },
    "unparseable_predictions": 0
  }
}
```

</details>

---
