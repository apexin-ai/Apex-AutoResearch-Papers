# code ensemble 5fold cv

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ensemble_5fold_cv_20260522T072555_result.json`
- **Structured JSON:** [`efa374bef3a57b0776fa.json`](../../sessions/ef/efa374bef3a57b0776fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Complete results JSON:

```json
{
  "R1-8B": {
    "model": "R1-8B",
    "n_traces": 209,
    "n_folds": 5,
    "cv_type": "5-fold_stratified",
    "window": 15,
    "layer_offset": 12,
    "metrics": {
      "ensemble_cv": {
        "bal_acc": 0.711,
        "precision": 0.5516,
        "fpr": 0.1631
      },
      "single_precision_cv": {
        "bal_acc": 0.7119,
        "precision": 0.5417,
        "fpr": 0.1731
      },
      "single_ba_cv": {
        "bal_acc": 0.6982,
        "precision": 0.515,
        "fpr": 0.1891
      },
      "single_fpr_cv": {
        "bal_acc": 0.7002,
        "precision": 0.5257,
        "fpr": 0.1793
      }
    },
    "per_trace_stats": {
      "ensemble_ba": {
        "mean": 0.7813,
        "std": 0.1754,
        "min": 0.1875,
        "max": 1.0
      },
      "ensemble_precision": {
        "mean": 0.5663,
        "std": 0.3672,
        "min": 0.0,
        "max": 1.0
      },
      "ensemble_fpr": {
        "mean": 0.1783,
        "std": 0.2453,
        "min": 0.0,
        "max": 1.0
      }
    },
    "layer_selection_stability": {
      "precision_layers": [22, 18, 23, 22, 24],
      "ba_layers": [15, 17, 23, 22, 15],
      "fpr_layers": [13, 18, 19, 24, 22],
      "precision_counts": {"22": 2, "18": 1, "23": 1, "24": 1},
      "ba_counts": {"15": 2, "17": 1, "23": 1, "22": 1},
      "fpr_counts": {"13": 1, "18": 1, "19": 1, "24": 1, "22": 1}
    },
    "fold_details": [
      {"fold": 0, "n_train": 167, "n_test": 42, "selected_layers": {"precision": 22, "ba": 15, "fpr": 13}, "n_unique_layers": 3, "elapsed_seconds": 125.2},
      {"fold": 1, "n_train": 167, "n_test": 42, "selected_layers": {"precision": 18, "ba": 17, "fpr": 18}, "n_unique_layers": 2, "elapsed_seconds": 85.0},
      {"fold": 2, "n_train": 167, "n_test": 42, "selected_layers": {"precision": 23, "ba": 23, "fpr": 19}, "n_unique_layers": 2, "elapsed_seconds": 86.1},
      {"fold": 3, "n_train": 167, "n_test": 42, "selected_layers": {"precision": 22, "ba": 22, "fpr": 24}, "n_unique_layers": 2, "elapsed_seconds": 76.5},
      {"fold": 4, "n_train": 168, "n_test": 41, "selected_layers": {"precision": 24, "ba": 15, "fpr": 22}, "n_unique_layers": 3, "elapsed_seconds": 89.8}
    ],
    "elapsed_seconds": 462.8
  },
  "_meta": {
    "script": "n7_ensemble_loocv.py",
    "elapsed_seconds": 466.2,
    "seed": 42,
    "n_folds": 5,
    "timestamp": "2026-05-22T15:35:54",
    "description": "5-fold stratified CV validation of multi-metric ensemble layer selection. Layer selection happens INSIDE each fold (inner 80/20 split of training set). R1-8B only."
  }
}
```

Ensemble achieves the best precision (0.5516) and lowest FPR (0.1631) among all methods, while maintaining competitive BA (0.711). Layer selection stability is moderate — precision favors L22 (2/5 folds), BA favors L15 (2/5), FPR has no repeats across folds.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "R1-8B": {
      "model": "R1-8B",
      "n_traces": 209,
      "n_folds": 5,
      "cv_type": "5-fold_stratified",
      "window": 15,
      "layer_offset": 12,
      "metrics": {
        "ensemble_cv": {
          "bal_acc": 0.711,
          "precision": 0.5516,
          "fpr": 0.1631
        },
        "single_precision_cv": {
          "bal_acc": 0.7119,
          "precision": 0.5417,
          "fpr": 0.1731
        },
        "single_ba_cv": {
          "bal_acc": 0.6982,
          "precision": 0.515,
          "fpr": 0.1891
        },
        "single_fpr_cv": {
          "bal_acc": 0.7002,
          "precision": 0.5257,
          "fpr": 0.1793
        }
      },
      "per_trace_stats": {
        "ensemble_ba": {
          "mean": 0.7813,
          "std": 0.1754,
          "min": 0.1875,
          "max": 1.0
        },
        "ensemble_precision": {
          "mean": 0.5663,
          "std": 0.3672,
          "min": 0.0,
          "max": 1.0
        },
        "ensemble_fpr": {
          "mean": 0.1783,
          "std": 0.2453,
          "min": 0.0,
          "max": 1.0
        }
      },
      "layer_selection_stability": {
        "precision_layers": [
          22,
          18,
          23,
          22,
          24
        ],
        "ba_layers": [
          15,
          17,
          23,
          22,
          15
        ],
        "fpr_layers": [
          13,
          18,
          19,
          24,
          22
        ],
        "precision_counts": {
          "22": 2,
          "18": 1,
          "23": 1,
          "24": 1
        },
        "ba_counts": {
          "15": 2,
          "17": 1,
          "23": 1,
          "22": 1
        },
        "fpr_counts": {
          "13": 1,
          "18": 1,
          "19": 1,
          "24": 1,
          "22": 1
        }
      },
      "fold_details": [
        {
          "fold": 0,
          "n_train": 167,
          "n_test": 42,
          "selected_layers": {
            "precision": 22,
            "ba": 15,
            "fpr": 13
          },
          "n_unique_layers": 3,
          "elapsed_seconds": 125.2
        },
        {
          "fold": 1,
          "n_train": 167,
          "n_test": 42,
          "selected_layers": {
            "precision": 18,
            "ba": 17,
            "fpr": 18
          },
          "n_unique_layers": 2,
          "elapsed_seconds": 85.0
        },
        {
          "fold": 2,
          "n_train": 167,
          "n_test": 42,
          "selected_layers": {
            "precision": 23,
            "ba": 23,
            "fpr": 19
          },
          "n_unique_layers": 2,
          "elapsed_seconds": 86.1
        },
        {
          "fold": 3,
          "n_train": 167,
          "n_test": 42,
          "selected_layers": {
            "precision": 22,
            "ba": 22,
            "fpr": 24
          },
          "n_unique_layers": 2,
          "elapsed_seconds": 76.5
        },
        {
          "fold": 4,
          "n_train": 168,
          "n_test": 41,
          "selected_layers": {
            "precision": 24,
            "ba": 15,
            "fpr": 22
          },
          "n_unique_layers": 3,
          "elapsed_seconds": 89.8
        }
      ],
      "elapsed_seconds": 462.8
    },
    "_meta": {
      "script": "n7_ensemble_loocv.py",
      "elapsed_seconds": 466.2,
      "seed": 42,
      "n_folds": 5,
      "timestamp": "2026-05-22T15:35:54",
      "description": "5-fold stratified CV validation of multi-metric ensemble layer selection. Layer selection happens INSIDE each fold (inner 80/20 split of training set). R1-8B only."
    }
  }
}
```

</details>

---
