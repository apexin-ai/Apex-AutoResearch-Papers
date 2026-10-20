# code exp047 read results

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp047-read-results_20260517T072029_result.json`
- **Structured JSON:** [`c0ed2fc77e709568c4bd.json`](../../sessions/c0/c0ed2fc77e709568c4bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1. multi_domain_results_t07.json

```json
{
  "experiment": "multi_domain_t07",
  "generation_params": {
    "temperature": 0.7,
    "top_p": 0.9
  },
  "per_domain": {
    "news": {
      "binary_f1": 0.7119,
      "binary_ci": [0.6898, 0.7332],
      "3class_f1": 0.7149,
      "3class_ci": [0.6984, 0.7314],
      "per_generator_binary": {
        "mistral-7b": 0.7129,
        "pythia-1b": 0.7606,
        "qwen3-1.7b": 0.6556
      },
      "per_generator_3class": {
        "mistral-7b": 0.6756,
        "pythia-1b": 0.7689,
        "qwen3-1.7b": 0.6993
      },
      "n_samples": 2400
    },
    "academic": {
      "binary_f1": 0.6279,
      "binary_ci": [0.6027, 0.6515],
      "3class_f1": 0.6564,
      "3class_ci": [0.6381, 0.6735],
      "per_generator_binary": {
        "mistral-7b": 0.6009,
        "pythia-1b": 0.7383,
        "qwen3-1.7b": 0.5132
      },
      "per_generator_3class": {
        "mistral-7b": 0.6362,
        "pythia-1b": 0.751,
        "qwen3-1.7b": 0.5762
      },
      "n_samples": 2400
    },
    "code": {
      "binary_f1": 0.6872,
      "binary_ci": [0.6641, 0.71],
      "3class_f1": 0.6729,
      "3class_ci": [0.6537, 0.6918],
      "per_generator_binary": {
        "mistral-7b": 0.6342,
        "pythia-1b": 0.7549,
        "qwen3-1.7b": 0.6648
      },
      "per_generator_3class": {
        "mistral-7b": 0.6463,
        "pythia-1b": 0.7407,
        "qwen3-1.7b": 0.634
      },
      "n_samples": 2400
    }
  },
  "overall": {
    "binary_f1": 0.6757,
    "3class_f1": 0.6814
  },
  "comparison_with_t10": {
    "news": {"t07": 0.7119, "t10": 0.7459, "delta": -0.034},
    "academic": {"t07": 0.6279, "t10": 0.7386, "delta": -0.1107},
    "code": {"t07": 0.6872, "t10": 0.7535, "delta": -0.0663}
  }
}
```

## 2. wc -l generations_t07/*.jsonl

```
    800 mistral-7b_academic.jsonl
    800 mistral-7b_code.jsonl
    800 mistral-7b_news.jsonl
    800 pythia-1b_academic.jsonl
    800 pythia-1b_code.jsonl
    800 pythia-1b_news.jsonl
    800 qwen3-1.7b_academic.jsonl
    800 qwen3-1.7b_code.jsonl
    800 qwen3-1.7b_news.jsonl
   7200 total
```

全部 9 个文件均为 800 行。

## 3. tail -30 run_t07.log

```
  --- news (n=2400) ---
    Binary F1: 0.7119 CI: [0.6898, 0.7332]
    3-class F1: 0.7149 CI: [0.6984, 0.7314]
    Per-generator (bin): {'mistral-7b': 0.7129, 'pythia-1b': 0.7606, 'qwen3-1.7b': 0.6556}
    Per-generator (3c): {'mistral-7b': 0.6756, 'pythia-1b': 0.7689, 'qwen3-1.7b': 0.6993}

  --- academic (n=2400) ---
    Binary F1: 0.6279 CI: [0.6027, 0.6515]
    3-class F1: 0.6564 CI: [0.6381, 0.6735]
    Per-generator (bin): {'mistral-7b': 0.6009, 'pythia-1b': 0.7383, 'qwen3-1.7b': 0.5132}
    Per-generator (3c): {'mistral-7b': 0.6362, 'pythia-1b': 0.751, 'qwen3-1.7b': 0.5762}

  --- code (n=2400) ---
    Binary F1: 0.6872 CI: [0.6641, 0.71]
    3-class F1: 0.6729 CI: [0.6537, 0.6918]
    Per-generator (bin): {'mistral-7b': 0.6342, 'pythia-1b': 0.7549, 'qwen3-1.7b': 0.6648}
    Per-generator (3c): {'mistral-7b': 0.6463, 'pythia-1b': 0.7407, 'qwen3-1.7b': 0.634}

  Results saved: /root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results_t07.json

=== COMPARISON t=0.7 vs t=1.0 ===
  news: t07=0.7119, t10=0.7459, delta=-0.0340
  academic: t07=0.6279, t10=0.7386, delta=-0.1107
  code: t07=0.6872, t10=0.7535, delta=-0.0663
  Overall binary F1: 0.6757

============================================================
COMPLETE in 1.3h (79min)
============================================================
```

实验正常完成，耗时 79 分钟。所有数据完整。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment": "multi_domain_t07",
    "generation_params": {
      "temperature": 0.7,
      "top_p": 0.9
    },
    "per_domain": {
      "news": {
        "binary_f1": 0.7119,
        "binary_ci": [
          0.6898,
          0.7332
        ],
        "3class_f1": 0.7149,
        "3class_ci": [
          0.6984,
          0.7314
        ],
        "per_generator_binary": {
          "mistral-7b": 0.7129,
          "pythia-1b": 0.7606,
          "qwen3-1.7b": 0.6556
        },
        "per_generator_3class": {
          "mistral-7b": 0.6756,
          "pythia-1b": 0.7689,
          "qwen3-1.7b": 0.6993
        },
        "n_samples": 2400
      },
      "academic": {
        "binary_f1": 0.6279,
        "binary_ci": [
          0.6027,
          0.6515
        ],
        "3class_f1": 0.6564,
        "3class_ci": [
          0.6381,
          0.6735
        ],
        "per_generator_binary": {
          "mistral-7b": 0.6009,
          "pythia-1b": 0.7383,
          "qwen3-1.7b": 0.5132
        },
        "per_generator_3class": {
          "mistral-7b": 0.6362,
          "pythia-1b": 0.751,
          "qwen3-1.7b": 0.5762
        },
        "n_samples": 2400
      },
      "code": {
        "binary_f1": 0.6872,
        "binary_ci": [
          0.6641,
          0.71
        ],
        "3class_f1": 0.6729,
        "3class_ci": [
          0.6537,
          0.6918
        ],
        "per_generator_binary": {
          "mistral-7b": 0.6342,
          "pythia-1b": 0.7549,
          "qwen3-1.7b": 0.6648
        },
        "per_generator_3class": {
          "mistral-7b": 0.6463,
          "pythia-1b": 0.7407,
          "qwen3-1.7b": 0.634
        },
        "n_samples": 2400
      }
    },
    "overall": {
      "binary_f1": 0.6757,
      "3class_f1": 0.6814
    },
    "comparison_with_t10": {
      "news": {
        "t07": 0.7119,
        "t10": 0.7459,
        "delta": -0.034
      },
      "academic": {
        "t07": 0.6279,
        "t10": 0.7386,
        "delta": -0.1107
      },
      "code": {
        "t07": 0.6872,
        "t10": 0.7535,
        "delta": -0.0663
      }
    }
  }
}
```

</details>

---
