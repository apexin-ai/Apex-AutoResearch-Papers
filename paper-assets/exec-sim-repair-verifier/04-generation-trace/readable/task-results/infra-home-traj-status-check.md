# infra home traj status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_home-traj-status-check_20260512T054632_result.json`
- **Structured JSON:** [`aa1b843509b3f4b7d06f.json`](../../sessions/aa/aa1b843509b3f4b7d06f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. traj-level-finetuned — 已完成 ✅

训练于 2026-05-11 22:24 完成，EXIT_CODE=0。3 epochs, 756 steps, 33 分钟，train_loss=0.228。

Checkpoint 已保存：`checkpoints_traj/best/adapter_model.safetensors` (45MB)

**eval_traj_results.json：**
```json
{
  "test_set_size": 1032,
  "class_balance": {"resolved": 479, "unresolved": 553, "resolved_pct": 46.4},
  "majority_baseline_accuracy": 53.59,
  "overall_accuracy": 85.66,
  "accuracy_vs_baseline_gap_pp": 32.07,
  "per_class": {
    "unresolved": {"precision": 82.09, "recall": 93.67, "f1": 87.5, "support": 553},
    "resolved":   {"precision": 91.27, "recall": 76.41, "f1": 83.18, "support": 479}
  },
  "confusion_matrix": {"tn": 518, "fp": 35, "fn": 113, "tp": 366},
  "unparseable_predictions": 0,
  "per_test_consistency": {"n_compared": 1032, "n_consistent": 825, "consistency_rate": 79.94}
}
```

### 2. SWE-bench full run — 运行中 🔄

PID 2312582 仍在运行，已运行 1h23m。

- 总计 240 个实例待评估（10 个已跳过）
- 当前进度：**143/240 (60%)**，✓=141, ✖=2, error=0
- 已生成 5 个预测文件，共 665 行：

| 文件 | 行数 |
|------|------|
| predictions_gold.jsonl | 250 |
| predictions_mutation_boundary_removal.jsonl | 127 |
| predictions_mutation_off_by_one.jsonl | 61 |
| predictions_mutation_operator_swap.jsonl | 138 |
| predictions_mutation_return_value.jsonl | 89 |

按当前速度（~60-100s/it），预计还需 **1.5-2.5 小时**完成。

### 3. GPU 状态 — 空闲

| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| 0 | 0% | 0 MiB | 32607 MiB |

GPU 完全空闲，SWE-bench 任务为 CPU-bound（Docker 容器内执行测试）。

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
    "overall_accuracy": 85.66,
    "accuracy_vs_baseline_gap_pp": 32.07,
    "per_class": {
      "unresolved": {
        "precision": 82.09,
        "recall": 93.67,
        "f1": 87.5,
        "support": 553
      },
      "resolved": {
        "precision": 91.27,
        "recall": 76.41,
        "f1": 83.18,
        "support": 479
      }
    },
    "confusion_matrix": {
      "tn": 518,
      "fp": 35,
      "fn": 113,
      "tp": 366
    },
    "unparseable_predictions": 0,
    "per_test_consistency": {
      "n_compared": 1032,
      "n_consistent": 825,
      "consistency_rate": 79.94
    }
  }
}
```

</details>

---
