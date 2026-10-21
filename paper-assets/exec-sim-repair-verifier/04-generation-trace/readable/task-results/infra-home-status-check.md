# infra home status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_home-status-check_20260512T075106_result.json`
- **Structured JSON:** [`5d96d1d23479c01d8cf6.json`](../../sessions/5d/5d96d1d23479c01d8cf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 任务 1: traj-level-seed123
**状态：已完成**

PID 2427622 已退出。结果文件内容：

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

---

## 任务 2: traj-level-seed456
**状态：运行中**

PID 2542385 存活，已运行 5min22s。训练进度 **118/756 steps (16%)**，~2.5s/step，预计剩余 ~26 分钟完成训练，之后还有 eval 阶段。

---

## 任务 3: SWE-bench 数据构建
**状态：运行中**

PID 2312582 存活，已运行 3h28m。当前阶段：`pilot_mutation_return_value` 评估中 (22/88, 25%)。上一阶段 `pilot_mutation_boundary_removal` 已完成（250 instances 提交 127，完成 53，错误 74，resolved 仅 4）。

`swebench_full/` 目录已产出 5 个 predictions 文件：
- `predictions_gold.jsonl` (410KB)
- `predictions_mutation_boundary_removal.jsonl` (265KB)
- `predictions_mutation_off_by_one.jsonl` (150KB)
- `predictions_mutation_operator_swap.jsonl` (302KB)
- `predictions_mutation_return_value.jsonl` (224KB)

当前阶段 error 率偏高（8/22），且 0 个 resolved（✓=0），后续可能需要排查 Docker image 构建失败问题。

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
