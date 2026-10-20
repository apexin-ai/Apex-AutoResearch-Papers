# ops check table3 file

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-table3-file_20260516T182951_result.json`
- **Structured JSON:** [`16e188512b1694be2da3.json`](../../sessions/16/16e188512b1694be2da3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
-rw-r--r-- 1 root root 3028 May 17 01:54 /root/gen-depth-fingerprint/results/8gen_table3_unified.json
```

```json
{
  "method": "pooled_logo",
  "n_generators": 8,
  "generators": [
    "llama-3.2-3b",
    "mistral-7b-v0.3",
    "olmo-2-1b",
    "pythia-1b",
    "pythia-2.8b",
    "qwen3-0.6b",
    "qwen3-1.7b",
    "qwen3-8b"
  ],
  "xgb_params": {
    "n_estimators": 200,
    "max_depth": 6,
    "learning_rate": 0.1,
    "random_state": 42
  },
  "total_samples": {
    "feat_data": 37058,
    "det_data": 34131,
    "merged": 37058,
    "det_available": 34131,
    "det_missing": 2927
  },
  "results": {
    "7feature_ours": {
      "3class_f1": 0.7614,
      "3class_ci95": [0.7572, 0.7658],
      "binary_f1": 0.6939,
      "binary_ci95": [0.6876, 0.7],
      "features": ["entropy_mean","entropy_std","entropy_max","entropy_min","ttr","hapax_ratio","tail_decay"],
      "n_samples_3class": 37058,
      "n_samples_binary": 29095,
      "n_dropped": 0
    },
    "3det_surface": {
      "3class_f1": 0.794,
      "3class_ci95": [0.7897, 0.7981],
      "binary_f1": 0.7125,
      "binary_ci95": [0.7063, 0.7185],
      "features": ["avg_logprob","fastdetectgpt","binoculars","ttr","hapax_ratio"],
      "n_samples_3class": 34131,
      "n_samples_binary": 26168,
      "n_dropped": 2927
    },
    "3det_ensemble": {
      "3class_f1": 0.7692,
      "3class_ci95": [0.765, 0.7737],
      "binary_f1": 0.6832,
      "binary_ci95": [0.6771, 0.6896],
      "features": ["avg_logprob","fastdetectgpt","binoculars"],
      "n_samples_3class": 34131,
      "n_samples_binary": 26168,
      "n_dropped": 2927
    },
    "avg_logprob": {
      "3class_f1": 0.6905,
      "3class_ci95": [0.6857, 0.6952],
      "binary_f1": 0.6566,
      "binary_ci95": [0.6505, 0.6625],
      "features": ["avg_logprob"],
      "n_samples_3class": 34131,
      "n_samples_binary": 26168,
      "n_dropped": 2927
    },
    "fastdetectgpt": {
      "3class_f1": 0.5837,
      "3class_ci95": [0.5805, 0.5872],
      "binary_f1": 0.4468,
      "binary_ci95": [0.442, 0.4515],
      "features": ["fastdetectgpt"],
      "n_samples_3class": 34131,
      "n_samples_binary": 26168,
      "n_dropped": 2927
    },
    "binoculars": {
      "3class_f1": 0.2905,
      "3class_ci95": [0.287, 0.2945],
      "binary_f1": 0.4384,
      "binary_ci95": [0.4342, 0.4427],
      "features": ["binoculars"],
      "n_samples_3class": 34131,
      "n_samples_binary": 26168,
      "n_dropped": 2927
    }
  },
  "notes": "D039 unified evaluation. All methods use identical XGB(200/6/lr0.1/seed42), same LOGO folds, pooled macro-F1. ld_score unavailable (no public implementation)."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "method": "pooled_logo",
    "n_generators": 8,
    "generators": [
      "llama-3.2-3b",
      "mistral-7b-v0.3",
      "olmo-2-1b",
      "pythia-1b",
      "pythia-2.8b",
      "qwen3-0.6b",
      "qwen3-1.7b",
      "qwen3-8b"
    ],
    "xgb_params": {
      "n_estimators": 200,
      "max_depth": 6,
      "learning_rate": 0.1,
      "random_state": 42
    },
    "total_samples": {
      "feat_data": 37058,
      "det_data": 34131,
      "merged": 37058,
      "det_available": 34131,
      "det_missing": 2927
    },
    "results": {
      "7feature_ours": {
        "3class_f1": 0.7614,
        "3class_ci95": [
          0.7572,
          0.7658
        ],
        "binary_f1": 0.6939,
        "binary_ci95": [
          0.6876,
          0.7
        ],
        "features": [
          "entropy_mean",
          "entropy_std",
          "entropy_max",
          "entropy_min",
          "ttr",
          "hapax_ratio",
          "tail_decay"
        ],
        "n_samples_3class": 37058,
        "n_samples_binary": 29095,
        "n_dropped": 0
      },
      "3det_surface": {
        "3class_f1": 0.794,
        "3class_ci95": [
          0.7897,
          0.7981
        ],
        "binary_f1": 0.7125,
        "binary_ci95": [
          0.7063,
          0.7185
        ],
        "features": [
          "avg_logprob",
          "fastdetectgpt",
          "binoculars",
          "ttr",
          "hapax_ratio"
        ],
        "n_samples_3class": 34131,
        "n_samples_binary": 26168,
        "n_dropped": 2927
      },
      "3det_ensemble": {
        "3class_f1": 0.7692,
        "3class_ci95": [
          0.765,
          0.7737
        ],
        "binary_f1": 0.6832,
        "binary_ci95": [
          0.6771,
          0.6896
        ],
        "features": [
          "avg_logprob",
          "fastdetectgpt",
          "binoculars"
        ],
        "n_samples_3class": 34131,
        "n_samples_binary": 26168,
        "n_dropped": 2927
      },
      "avg_logprob": {
        "3class_f1": 0.6905,
        "3class_ci95": [
          0.6857,
          0.6952
        ],
        "binary_f1": 0.6566,
        "binary_ci95": [
          0.6505,
          0.6625
        ],
        "features": [
          "avg_logprob"
        ],
        "n_samples_3class": 34131,
        "n_samples_binary": 26168,
        "n_dropped": 2927
      },
      "fastdetectgpt": {
        "3class_f1": 0.5837,
        "3class_ci95": [
          0.5805,
          0.5872
        ],
        "binary_f1": 0.4468,
        "binary_ci95": [
          0.442,
          0.4515
        ],
        "features": [
          "fastdetectgpt"
        ],
        "n_samples_3class": 34131,
        "n_samples_binary": 26168,
        "n_dropped": 2927
      },
      "binoculars": {
        "3class_f1": 0.2905,
        "3class_ci95": [
          0.287,
          0.2945
        ],
        "binary_f1": 0.4384,
        "binary_ci95": [
          0.4342,
          0.4427
        ],
        "features": [
          "binoculars"
        ],
        "n_samples_3class": 34131,
        "n_samples_binary": 26168,
        "n_dropped": 2927
      }
    },
    "notes": "D039 unified evaluation. All methods use identical XGB(200/6/lr0.1/seed42), same LOGO folds, pooled macro-F1. ld_score unavailable (no public implementation)."
  }
}
```

</details>

---
