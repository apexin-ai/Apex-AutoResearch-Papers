# ops check chem read eval cleanup

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-chem-read-eval-cleanup_20260514T051435_result.json`
- **Structured JSON:** [`69ed6ed04b7ccdfd7951.json`](../../sessions/69/69ed6ed04b7ccdfd7951.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

---

### 1. chemistry-mix 进度

| 指标 | 值 |
|---|---|
| PID 788058 | **存活**，已运行 2h02m57s |
| episodes.jsonl | **16 行** |
| GPU 占用 | PID 789051 占用 28004 MiB（注意不是 788058，可能是子进程） |

**未完成**，仍在运行中。16 条 episode 产出偏少，可能是 chemistry-mix 单条耗时较长。

---

### 2. eval_report.json（plan-002-dryrun）

```json
{
  "overall_accuracy": 0.9231,
  "confusion_matrix": [[0, 30], [0, 360]],
  "confusion_labels": ["internal", "deterministic"],
  "per_task": {
    "chemistry-mix":           {"accuracy": 0.0,  "n_samples": 30},
    "find-animal":             {"accuracy": 1.0,  "n_samples": 30},
    "find-non-living-thing":   {"accuracy": 1.0,  "n_samples": 90},
    "freeze":                  {"accuracy": 1.0,  "n_samples": 30},
    "grow-fruit":              {"accuracy": 1.0,  "n_samples": 30},
    "identify-life-stages-1":  {"accuracy": 1.0,  "n_samples": 30},
    "identify-life-stages-2":  {"accuracy": 1.0,  "n_samples": 30},
    "inclined-plane-determine-angle": {"accuracy": 1.0, "n_samples": 30},
    "lifespan-longest-lived":  {"accuracy": 1.0,  "n_samples": 30},
    "lifespan-longest-lived-then-shortest-lived": {"accuracy": 1.0, "n_samples": 30},
    "measure-melting-point-unknown-substance": {"accuracy": 1.0, "n_samples": 30}
  }
}
```

overall 92.3%，**chemistry-mix 是唯一 0% 的任务**（30 samples 全错），所有 deterministic 类任务全部 100%。confusion matrix 显示模型把所有 30 个 internal 样本都预测成了 deterministic。

---

### 3. 磁盘清理

三个目标文件**均已不存在**（之前已被清理）。无需再次删除。

| 指标 | 值 |
|---|---|
| 数据盘 | 250G 总量，55G 已用（22%），196G 可用 |
| lifespan-longest-lived 目录 | 仅剩 416K（3 个小文件） |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "overall_accuracy": 0.9231,
    "confusion_matrix": [
      [
        0,
        30
      ],
      [
        0,
        360
      ]
    ],
    "confusion_labels": [
      "internal",
      "deterministic"
    ],
    "per_task": {
      "chemistry-mix": {
        "accuracy": 0.0,
        "n_samples": 30
      },
      "find-animal": {
        "accuracy": 1.0,
        "n_samples": 30
      },
      "find-non-living-thing": {
        "accuracy": 1.0,
        "n_samples": 90
      },
      "freeze": {
        "accuracy": 1.0,
        "n_samples": 30
      },
      "grow-fruit": {
        "accuracy": 1.0,
        "n_samples": 30
      },
      "identify-life-stages-1": {
        "accuracy": 1.0,
        "n_samples": 30
      },
      "identify-life-stages-2": {
        "accuracy": 1.0,
        "n_samples": 30
      },
      "inclined-plane-determine-angle": {
        "accuracy": 1.0,
        "n_samples": 30
      },
      "lifespan-longest-lived": {
        "accuracy": 1.0,
        "n_samples": 30
      },
      "lifespan-longest-lived-then-shortest-lived": {
        "accuracy": 1.0,
        "n_samples": 30
      },
      "measure-melting-point-unknown-substance": {
        "accuracy": 1.0,
        "n_samples": 30
      }
    }
  }
}
```

</details>

---
