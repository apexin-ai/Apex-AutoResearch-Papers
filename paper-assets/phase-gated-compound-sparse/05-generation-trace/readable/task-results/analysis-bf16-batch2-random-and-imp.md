# analysis bf16 batch2 random and imp

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_batch2_random_and_imp_20260514T064655_result.json`
- **Structured JSON:** [`2a07e818f12b810a5475.json`](../../sessions/2a/2a07e818f12b810a5475.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。以下是 5 个实验的完整分析结果。

---

## 1. bf16_ds_rand_s015

```json
{
  "exp_id": "bf16_ds_rand_s015",
  "conclusion": "success",
  "metrics": {
    "interaction_index": {
      "high": {"mean": 0.3849, "ci": [-0.5409, 1.3147], "median": 0.1147, "winsorized_mean": 0.3161, "skewness": -5.4014},
      "mid":  {"mean": -172.6626, "ci": [-427.0058, -9.0687], "median": 0.0969, "winsorized_mean": -0.6366, "skewness": -10.5634},
      "low":  {"mean": -5.7326, "ci": [-10.9283, -1.4391], "median": 0.1121, "winsorized_mean": 0.0521, "skewness": -11.5715}
    },
    "per_problem_ii_stats": {
      "high": {"n": 49, "min": -17.4797, "max": 22.5146, "mean": 0.2208, "median": 0.0931, "std": 4.1856},
      "mid":  {"n": 40, "min": -75.8992, "max": 6.2495, "mean": -3.3604, "median": 0.0967, "std": 15.4282},
      "low":  {"n": 50, "min": -59.7311, "max": 5.0415, "mean": -1.8952, "median": 0.1026, "std": 10.2205}
    },
    "gradient_paired_aggregate": 0.98,
    "n_problems": 50,
    "pass_fail": {"ci_overlap": true, "sign_reversal": false, "overall": "PASS"},
    "phase_stats": {"high": {"n_tokens": 21086, "n_segments": 387}, "low": {"n_tokens": 27748, "n_segments": 397}, "mid": {"n_tokens": 13306, "n_segments": 191}},
    "perplexity": {
      "high": {"dense": 1.1687, "attn": 3.5947, "kv": 2.9239, "both": 5.7569},
      "low":  {"dense": 1.2284, "attn": 11.3419, "kv": 3.6161, "both": 6.2886},
      "mid":  {"dense": 1.2269, "attn": 297.7957, "kv": 2.915, "both": 11.3156}
    }
  }
}
```

---

## 2. bf16_ds_rand_s020

```json
{
  "exp_id": "bf16_ds_rand_s020",
  "conclusion": "success",
  "metrics": {
    "interaction_index": {
      "high": {"mean": 2.5259, "ci": [1.2546, 4.2356], "median": 0.3278, "winsorized_mean": 1.7664, "skewness": 9.5932},
      "mid":  {"mean": -36.0516, "ci": [-93.2484, -2.2016], "median": 0.2977, "winsorized_mean": 0.5839, "skewness": -12.3126},
      "low":  {"mean": -2.4805, "ci": [-5.6296, 0.1128], "median": 0.3909, "winsorized_mean": 0.9942, "skewness": -10.0661}
    },
    "per_problem_ii_stats": {
      "high": {"n": 49, "min": -4.5854, "max": 29.4003, "mean": 1.1216, "median": 0.2918, "std": 4.6109},
      "mid":  {"n": 40, "min": -80.8773, "max": 11.0717, "mean": -1.5827, "median": 0.3504, "std": 13.8427},
      "low":  {"n": 50, "min": -38.3425, "max": 8.3532, "mean": -0.4116, "median": 0.2763, "std": 7.3481}
    },
    "gradient_paired_aggregate": 1.19,
    "n_problems": 50,
    "pass_fail": {"ci_overlap": true, "sign_reversal": true, "overall": "PASS"},
    "phase_stats": {"high": {"n_tokens": 21086, "n_segments": 387}, "low": {"n_tokens": 27748, "n_segments": 397}, "mid": {"n_tokens": 13306, "n_segments": 191}},
    "perplexity": {
      "high": {"dense": 1.1687, "attn": 3.1905, "kv": 3.8002, "both": 8.8129},
      "low":  {"dense": 1.2284, "attn": 8.592, "kv": 5.0078, "both": 9.2001},
      "mid":  {"dense": 1.2269, "attn": 67.8504, "kv": 3.788, "both": 11.4974}
    }
  }
}
```

---

## 3. bf16_ds_rand_s025

```json
{
  "exp_id": "bf16_ds_rand_s025",
  "conclusion": "success",
  "metrics": {
    "interaction_index": {
      "high": {"mean": 5.5906, "ci": [1.1716, 9.4656], "median": 1.5545, "winsorized_mean": 6.3965, "skewness": -7.566},
      "mid":  {"mean": -514.2418, "ci": [-1361.4741, -24.9357], "median": 1.0202, "winsorized_mean": 3.1014, "skewness": -12.7601},
      "low":  {"mean": -9.1062, "ci": [-25.8045, 2.5166], "median": 1.8937, "winsorized_mean": 4.1866, "skewness": -15.8457}
    },
    "per_problem_ii_stats": {
      "high": {"n": 49, "min": -13.5968, "max": 44.5263, "mean": 3.5900, "median": 0.8182, "std": 8.6725},
      "mid":  {"n": 40, "min": -126.2488, "max": 18.7198, "mean": -1.8455, "median": 0.9324, "std": 26.7996},
      "low":  {"n": 50, "min": -91.2344, "max": 25.7084, "mean": 0.7212, "median": 1.3627, "std": 16.9395}
    },
    "gradient_paired_aggregate": 1.22,
    "n_problems": 50,
    "pass_fail": {"ci_overlap": true, "sign_reversal": true, "overall": "PASS"},
    "phase_stats": {"high": {"n_tokens": 21086, "n_segments": 387}, "low": {"n_tokens": 27748, "n_segments": 397}, "mid": {"n_tokens": 13306, "n_segments": 191}},
    "perplexity": {
      "high": {"dense": 1.1687, "attn": 7.237, "kv": 4.9751, "both": 17.7423},
      "low":  {"dense": 1.2284, "attn": 24.3571, "kv": 6.7993, "both": 17.9694},
      "mid":  {"dense": 1.2269, "attn": 868.3199, "kv": 5.1165, "both": 29.4661}
    }
  }
}
```

---

## 4. bf16_importance_s020

```json
{
  "exp_id": "bf16_importance_s020",
  "conclusion": "success",
  "metrics": {
    "interaction_index": {
      "high": {"mean": 0.1289, "ci": [-0.1975, 0.6647], "median": 0.0145, "winsorized_mean": -0.0297, "skewness": 16.6701},
      "mid":  {"mean": 1.2604, "ci": [0.7466, 1.8962], "median": 0.2027, "winsorized_mean": 0.7660, "skewness": 7.0541},
      "low":  {"mean": 6.0288, "ci": [4.4671, 7.9237], "median": 1.4963, "winsorized_mean": 4.3426, "skewness": 6.012}
    },
    "per_problem_ii_stats": {
      "high": {"n": 49, "min": -0.1884, "max": 0.4196, "mean": 0.0025, "median": 0.0036, "std": 0.0976},
      "mid":  {"n": 40, "min": -0.0519, "max": 8.6969, "mean": 0.6795, "median": 0.1977, "std": 1.5189},
      "low":  {"n": 50, "min": -1.6151, "max": 22.6875, "mean": 2.2301, "median": 1.1280, "std": 4.4202}
    },
    "gradient_paired_aggregate": 103.10,
    "n_problems": 50,
    "pass_fail": {"ci_overlap": true, "sign_reversal": false, "overall": "PASS"},
    "phase_stats": {"high": {"n_tokens": 21086, "n_segments": 387}, "low": {"n_tokens": 27748, "n_segments": 397}, "mid": {"n_tokens": 13306, "n_segments": 191}},
    "perplexity": {
      "high": {"dense": 1.1689, "attn": 1.5233, "kv": 1.6191, "both": 2.1047},
      "low":  {"dense": 1.2286, "attn": 1.6486, "kv": 15.7987, "both": 23.74},
      "mid":  {"dense": 1.2269, "attn": 1.5375, "kv": 3.5164, "both": 5.4246}
    }
  }
}
```

---

## 5. bf16_importance_s030

```json
{
  "exp_id": "bf16_importance_s030",
  "conclusion": "success",
  "metrics": {
    "interaction_index": {
      "high": {"mean": 0.5547, "ci": [0.2773, 0.9198], "median": 0.0534, "winsorized_mean": 0.3367, "skewness": 10.622},
      "mid":  {"mean": 11.3000, "ci": [6.8650, 17.2633], "median": 2.2833, "winsorized_mean": 8.1752, "skewness": 9.1908},
      "low":  {"mean": 57.7946, "ci": [41.4416, 77.0467], "median": 14.6395, "winsorized_mean": 39.3143, "skewness": 8.3142}
    },
    "per_problem_ii_stats": {
      "high": {"n": 49, "min": -0.5095, "max": 4.4457, "mean": 0.1976, "median": 0.0343, "std": 0.6864},
      "mid":  {"n": 40, "min": -0.1989, "max": 34.0258, "mean": 5.2585, "median": 1.5173, "std": 8.0394},
      "low":  {"n": 50, "min": -7.3027, "max": 126.7985, "mean": 22.6601, "median": 9.9731, "std": 28.6981}
    },
    "gradient_paired_aggregate": 274.24,
    "n_problems": 50,
    "pass_fail": {"ci_overlap": true, "sign_reversal": false, "overall": "PASS"},
    "phase_stats": {"high": {"n_tokens": 21086, "n_segments": 387}, "low": {"n_tokens": 27748, "n_segments": 397}, "mid": {"n_tokens": 13306, "n_segments": 191}},
    "perplexity": {
      "high": {"dense": 1.1689, "attn": 1.7123, "kv": 2.0544, "both": 3.2372},
      "low":  {"dense": 1.2286, "attn": 1.9347, "kv": 51.6485, "both": 122.609},
      "mid":  {"dense": 1.2269, "attn": 1.7894, "kv": 9.4821, "both": 24.2847}
    }
  }
}
```

---

## 汇总表

| exp_id | masking | sparsity | gradient | II_low_median | conclusion |
|--------|---------|----------|----------|---------------|------------|
| bf16_ds_rand_s015 | random | 0.15 | **0.98×** | 0.112 | success |
| bf16_ds_rand_s020 | random | 0.20 | **1.19×** | 0.391 | success |
| bf16_ds_rand_s025 | random | 0.25 | **1.22×** | 1.894 | success |
| bf16_importance_s020 | importance | 0.20 | **103.10×** | 1.496 | success |
| bf16_importance_s030 | importance | 0.30 | **274.24×** | 14.639 | success |

**Random 对照组**：3 个 sparsity 级别的 gradient 均在 0.98×–1.22× 范围内（< 3× 阈值），确认 random masking 无 compound effect。

**Importance 完整趋势**（含已完成参考值）：

| sparsity | gradient | II_low_median |
|----------|----------|---------------|
| 0.15 | 69.24× | 0.398 |
| 0.20 | 103.10× | 1.496 |
| 0.25 | 222.35× | 7.196 |
| 0.30 | 274.24× | 14.639 |

Gradient 和 II_low_median 均随 sparsity 单调递增，compound sparsity effect 在 importance masking 下持续增强。全部 5 个实验 conclusion = **success**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exp_id": "bf16_importance_s030",
    "conclusion": "success",
    "metrics": {
      "interaction_index": {
        "high": {
          "mean": 0.5547,
          "ci": [
            0.2773,
            0.9198
          ],
          "median": 0.0534,
          "winsorized_mean": 0.3367,
          "skewness": 10.622
        },
        "mid": {
          "mean": 11.3,
          "ci": [
            6.865,
            17.2633
          ],
          "median": 2.2833,
          "winsorized_mean": 8.1752,
          "skewness": 9.1908
        },
        "low": {
          "mean": 57.7946,
          "ci": [
            41.4416,
            77.0467
          ],
          "median": 14.6395,
          "winsorized_mean": 39.3143,
          "skewness": 8.3142
        }
      },
      "per_problem_ii_stats": {
        "high": {
          "n": 49,
          "min": -0.5095,
          "max": 4.4457,
          "mean": 0.1976,
          "median": 0.0343,
          "std": 0.6864
        },
        "mid": {
          "n": 40,
          "min": -0.1989,
          "max": 34.0258,
          "mean": 5.2585,
          "median": 1.5173,
          "std": 8.0394
        },
        "low": {
          "n": 50,
          "min": -7.3027,
          "max": 126.7985,
          "mean": 22.6601,
          "median": 9.9731,
          "std": 28.6981
        }
      },
      "gradient_paired_aggregate": 274.24,
      "n_problems": 50,
      "pass_fail": {
        "ci_overlap": true,
        "sign_reversal": false,
        "overall": "PASS"
      },
      "phase_stats": {
        "high": {
          "n_tokens": 21086,
          "n_segments": 387
        },
        "low": {
          "n_tokens": 27748,
          "n_segments": 397
        },
        "mid": {
          "n_tokens": 13306,
          "n_segments": 191
        }
      },
      "perplexity": {
        "high": {
          "dense": 1.1689,
          "attn": 1.7123,
          "kv": 2.0544,
          "both": 3.2372
        },
        "low": {
          "dense": 1.2286,
          "attn": 1.9347,
          "kv": 51.6485,
          "both": 122.609
        },
        "mid": {
          "dense": 1.2269,
          "attn": 1.7894,
          "kv": 9.4821,
          "both": 24.2847
        }
      }
    }
  }
}
```

</details>

---
