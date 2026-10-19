# code r8 bge ci readback

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r8_bge_ci_readback_20260518T073238_result.json`
- **Structured JSON:** [`25dc7602d3e1ce526660.json`](../../sessions/25/25dc7602d3e1ce526660.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "n_resamples": 10000,
  "seed": 42,
  "elapsed_seconds": 110.4,
  "probe": "LogisticRegression(C=1.0, class_weight='balanced', max_iter=2000)",
  "text_encoder": "BAAI/bge-large-en-v1.5",
  "note": "Correct layer indexing: hs[:, layer_idx, :] for (steps, layers, dim) tensors",
  "diff_convention": {
    "bal_acc": "HS - BGE (positive = HS better)",
    "fpr": "BGE - HS (positive = HS better, i.e. lower FPR)",
    "precision": "HS - BGE (positive = HS better)"
  },
  "models": {
    "r1_8b": {
      "n_traces": 209, "n_test": 43, "layer": 2, "window": 15,
      "bootstrap": {
        "bal_acc":   { "hs_value": 0.7293, "bge_value": 0.6457, "observed_diff": 0.0837, "ci_95": [-0.0069, 0.1701], "p_value": 0.0291, "bootstrap_std": 0.0452 },
        "fpr":       { "hs_value": 0.2332, "bge_value": 0.2209, "observed_diff": -0.0122, "ci_95": [-0.1184, 0.1082], "p_value": 0.5638, "bootstrap_std": 0.0575 },
        "precision": { "hs_value": 0.4971, "bge_value": 0.4358, "observed_diff": 0.0613, "ci_95": [-0.0735, 0.1946], "p_value": 0.1816, "bootstrap_std": 0.0682 }
      }
    },
    "ot_7b": {
      "n_traces": 228, "n_test": 47, "layer": 16, "window": 3,
      "bootstrap": {
        "bal_acc":   { "hs_value": 0.6821, "bge_value": 0.5745, "observed_diff": 0.1076, "ci_95": [0.0411, 0.1798], "p_value": 0.0019, "bootstrap_std": 0.0353 },
        "fpr":       { "hs_value": 0.1379, "bge_value": 0.2432, "observed_diff": 0.1053, "ci_95": [0.0385, 0.1682], "p_value": 0.0003, "bootstrap_std": 0.0333 },
        "precision": { "hs_value": 0.4460, "bge_value": 0.2629, "observed_diff": 0.1832, "ci_95": [0.0839, 0.2902], "p_value": 0.0003, "bootstrap_std": 0.0526 }
      }
    },
    "qwq_32b": {
      "n_traces": 95, "n_test": 19, "layer": 60, "window": 3,
      "bootstrap": {
        "bal_acc":   { "hs_value": 0.7353, "bge_value": 0.6428, "observed_diff": 0.0926, "ci_95": [-0.0307, 0.2093], "p_value": 0.0665, "bootstrap_std": 0.0629 },
        "fpr":       { "hs_value": 0.2304, "bge_value": 0.2575, "observed_diff": 0.0271, "ci_95": [-0.1272, 0.1773], "p_value": 0.3682, "bootstrap_std": 0.0771 },
        "precision": { "hs_value": 0.5455, "bge_value": 0.4540, "observed_diff": 0.0914, "ci_95": [-0.0706, 0.2774], "p_value": 0.1534, "bootstrap_std": 0.0895 }
      }
    },
    "r1_32b": {
      "n_traces": 100, "n_test": 20, "layer": 63, "window": 1,
      "bootstrap": {
        "bal_acc":   { "hs_value": 0.7419, "bge_value": 0.6326, "observed_diff": 0.1093, "ci_95": [0.0232, 0.1993], "p_value": 0.0077, "bootstrap_std": 0.0449 },
        "fpr":       { "hs_value": 0.2730, "bge_value": 0.3510, "observed_diff": 0.0780, "ci_95": [-0.0747, 0.2255], "p_value": 0.1654, "bootstrap_std": 0.0780 },
        "precision": { "hs_value": 0.5882, "bge_value": 0.4750, "observed_diff": 0.1132, "ci_95": [-0.0015, 0.2426], "p_value": 0.0423, "bootstrap_std": 0.0641 }
      }
    }
  }
}
```

HS (hidden states) 在所有 4 个模型上 bal_acc 均优于 BGE baseline。统计显著性方面：**ot_7b** 三项指标全部显著 (p<0.002)；**r1_32b** bal_acc 显著 (p=0.0077)；**r1_8b** bal_acc 显著 (p=0.029)；**qwq_32b** 趋势明显但 CI 跨零 (p=0.067)，样本量最小 (n=95)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "n_resamples": 10000,
    "seed": 42,
    "elapsed_seconds": 110.4,
    "probe": "LogisticRegression(C=1.0, class_weight='balanced', max_iter=2000)",
    "text_encoder": "BAAI/bge-large-en-v1.5",
    "note": "Correct layer indexing: hs[:, layer_idx, :] for (steps, layers, dim) tensors",
    "diff_convention": {
      "bal_acc": "HS - BGE (positive = HS better)",
      "fpr": "BGE - HS (positive = HS better, i.e. lower FPR)",
      "precision": "HS - BGE (positive = HS better)"
    },
    "models": {
      "r1_8b": {
        "n_traces": 209,
        "n_test": 43,
        "layer": 2,
        "window": 15,
        "bootstrap": {
          "bal_acc": {
            "hs_value": 0.7293,
            "bge_value": 0.6457,
            "observed_diff": 0.0837,
            "ci_95": [
              -0.0069,
              0.1701
            ],
            "p_value": 0.0291,
            "bootstrap_std": 0.0452
          },
          "fpr": {
            "hs_value": 0.2332,
            "bge_value": 0.2209,
            "observed_diff": -0.0122,
            "ci_95": [
              -0.1184,
              0.1082
            ],
            "p_value": 0.5638,
            "bootstrap_std": 0.0575
          },
          "precision": {
            "hs_value": 0.4971,
            "bge_value": 0.4358,
            "observed_diff": 0.0613,
            "ci_95": [
              -0.0735,
              0.1946
            ],
            "p_value": 0.1816,
            "bootstrap_std": 0.0682
          }
        }
      },
      "ot_7b": {
        "n_traces": 228,
        "n_test": 47,
        "layer": 16,
        "window": 3,
        "bootstrap": {
          "bal_acc": {
            "hs_value": 0.6821,
            "bge_value": 0.5745,
            "observed_diff": 0.1076,
            "ci_95": [
              0.0411,
              0.1798
            ],
            "p_value": 0.0019,
            "bootstrap_std": 0.0353
          },
          "fpr": {
            "hs_value": 0.1379,
            "bge_value": 0.2432,
            "observed_diff": 0.1053,
            "ci_95": [
              0.0385,
              0.1682
            ],
            "p_value": 0.0003,
            "bootstrap_std": 0.0333
          },
          "precision": {
            "hs_value": 0.446,
            "bge_value": 0.2629,
            "observed_diff": 0.1832,
            "ci_95": [
              0.0839,
              0.2902
            ],
            "p_value": 0.0003,
            "bootstrap_std": 0.0526
          }
        }
      },
      "qwq_32b": {
        "n_traces": 95,
        "n_test": 19,
        "layer": 60,
        "window": 3,
        "bootstrap": {
          "bal_acc": {
            "hs_value": 0.7353,
            "bge_value": 0.6428,
            "observed_diff": 0.0926,
            "ci_95": [
              -0.0307,
              0.2093
            ],
            "p_value": 0.0665,
            "bootstrap_std": 0.0629
          },
          "fpr": {
            "hs_value": 0.2304,
            "bge_value": 0.2575,
            "observed_diff": 0.0271,
            "ci_95": [
              -0.1272,
              0.1773
            ],
            "p_value": 0.3682,
            "bootstrap_std": 0.0771
          },
          "precision": {
            "hs_value": 0.5455,
            "bge_value": 0.454,
            "observed_diff": 0.0914,
            "ci_95": [
              -0.0706,
              0.2774
            ],
            "p_value": 0.1534,
            "bootstrap_std": 0.0895
          }
        }
      },
      "r1_32b": {
        "n_traces": 100,
        "n_test": 20,
        "layer": 63,
        "window": 1,
        "bootstrap": {
          "bal_acc": {
            "hs_value": 0.7419,
            "bge_value": 0.6326,
            "observed_diff": 0.1093,
            "ci_95": [
              0.0232,
              0.1993
            ],
            "p_value": 0.0077,
            "bootstrap_std": 0.0449
          },
          "fpr": {
            "hs_value": 0.273,
            "bge_value": 0.351,
            "observed_diff": 0.078,
            "ci_95": [
              -0.0747,
              0.2255
            ],
            "p_value": 0.1654,
            "bootstrap_std": 0.078
          },
          "precision": {
            "hs_value": 0.5882,
            "bge_value": 0.475,
            "observed_diff": 0.1132,
            "ci_95": [
              -0.0015,
              0.2426
            ],
            "p_value": 0.0423,
            "bootstrap_std": 0.0641
          }
        }
      }
    }
  }
}
```

</details>

---
