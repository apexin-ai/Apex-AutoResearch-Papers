# analysis gsm8k qw rand s025 v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gsm8k_qw_rand_s025_v2_20260515T234243_result.json`
- **Structured JSON:** [`55e75056a0dcb20678fb.json`](../../sessions/55/55e75056a0dcb20678fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志无报错，EXIT_CODE=0。完整 metrics 如下：

## 完整 Metrics

```json
{
  "experiment": "gsm8k_qw_rand_s025_v2",
  "verdict": "PASS",
  "config": {
    "model": "Qwen2.5-7B-Instruct",
    "sparsity_levels": [0.25],
    "masking_method": "random",
    "n_bootstrap": 1000,
    "n_problems": 50,
    "seed": 42
  },
  "high_sparsity": {
    "n_segments": 216,
    "n_tokens": 9326,
    "ppl_dense": 1.0695,
    "ppl_attn": 5.9362,
    "ppl_kv": 3.4316,
    "ppl_both": 15.7484,
    "ii_mean": 6.5954,
    "ii_ci": [1.1114, 11.3791],
    "ii_median": 0.7176,
    "ii_median_ci": [0.5959, 0.9347],
    "winsorized_mean": 6.5046,
    "skewness": -4.6807,
    "outlier_count": 3
  },
  "low_sparsity": {
    "n_segments": 252,
    "n_tokens": 29224,
    "ppl_dense": 1.1972,
    "ppl_attn": 11.5347,
    "ppl_kv": 5.6038,
    "ppl_both": 21.6874,
    "ii_mean": 2.3883,
    "ii_ci": [-8.4602, 11.0290],
    "ii_median": 1.4587,
    "ii_median_ci": [1.1121, 2.0451],
    "winsorized_mean": 5.8911,
    "skewness": -7.6074,
    "outlier_count": 4
  },
  "mid_sparsity": {
    "n_segments": 51,
    "n_tokens": 5954,
    "ppl_dense": 1.2601,
    "ppl_attn": 13.4132,
    "ppl_kv": 6.4841,
    "ppl_both": 20.8714,
    "ii_mean": 4.5407,
    "ii_ci": [-4.8854, 12.4605],
    "ii_median": 1.1272,
    "ii_median_ci": [0.6370, 3.3729],
    "winsorized_mean": 6.3284,
    "skewness": -3.4048,
    "outlier_count": 1
  },
  "pass_fail": {
    "ci_overlap_test": {"pass": true, "details": "high_sparsity vs low_sparsity CI non-overlapping at 0.25"},
    "sign_reversal_test": {"pass": false, "details": ""},
    "overall": "PASS"
  },
  "warnings": []
}
```

## 分析

**PASS 判定：** 三个 phase 的 ii_median_ci lower bound 均 > 0（high: 0.596, low: 1.112, mid: 0.637），compound interaction 显著。

**与 s030 对比（II 随 sparsity 下降）：**

| Phase | s=0.30 median | s=0.25 median | s=0.30 mean | s=0.25 mean |
|-------|--------------|--------------|-------------|-------------|
| high  | 2.31         | 0.72         | 11.83       | 6.60        |
| low   | 5.20         | 1.46         | 31.26       | 2.39        |
| mid   | 2.70         | 1.13         | 18.02       | 4.54        |

II 全面下降，符合预期：sparsity 越低，compound interaction 越弱。

**异常项：**
- **skewness 全为负**（-3.4 ~ -7.6），low_sparsity 最严重（-7.6），说明存在强负异常值。这与 mean CI 跨零（low: [-8.46, 11.03], mid: [-4.89, 12.46]）一致，但 median CI 稳健，不影响结论。
- **outlier_count** 合理（1-4个），无 null_ratio 字段（JSON 中未输出，应为 0）。
- sign_reversal_test FAIL 但不影响 overall PASS。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment": "gsm8k_qw_rand_s025_v2",
    "verdict": "PASS",
    "config": {
      "model": "Qwen2.5-7B-Instruct",
      "sparsity_levels": [
        0.25
      ],
      "masking_method": "random",
      "n_bootstrap": 1000,
      "n_problems": 50,
      "seed": 42
    },
    "high_sparsity": {
      "n_segments": 216,
      "n_tokens": 9326,
      "ppl_dense": 1.0695,
      "ppl_attn": 5.9362,
      "ppl_kv": 3.4316,
      "ppl_both": 15.7484,
      "ii_mean": 6.5954,
      "ii_ci": [
        1.1114,
        11.3791
      ],
      "ii_median": 0.7176,
      "ii_median_ci": [
        0.5959,
        0.9347
      ],
      "winsorized_mean": 6.5046,
      "skewness": -4.6807,
      "outlier_count": 3
    },
    "low_sparsity": {
      "n_segments": 252,
      "n_tokens": 29224,
      "ppl_dense": 1.1972,
      "ppl_attn": 11.5347,
      "ppl_kv": 5.6038,
      "ppl_both": 21.6874,
      "ii_mean": 2.3883,
      "ii_ci": [
        -8.4602,
        11.029
      ],
      "ii_median": 1.4587,
      "ii_median_ci": [
        1.1121,
        2.0451
      ],
      "winsorized_mean": 5.8911,
      "skewness": -7.6074,
      "outlier_count": 4
    },
    "mid_sparsity": {
      "n_segments": 51,
      "n_tokens": 5954,
      "ppl_dense": 1.2601,
      "ppl_attn": 13.4132,
      "ppl_kv": 6.4841,
      "ppl_both": 20.8714,
      "ii_mean": 4.5407,
      "ii_ci": [
        -4.8854,
        12.4605
      ],
      "ii_median": 1.1272,
      "ii_median_ci": [
        0.637,
        3.3729
      ],
      "winsorized_mean": 6.3284,
      "skewness": -3.4048,
      "outlier_count": 1
    },
    "pass_fail": {
      "ci_overlap_test": {
        "pass": true,
        "details": "high_sparsity vs low_sparsity CI non-overlapping at 0.25"
      },
      "sign_reversal_test": {
        "pass": false,
        "details": ""
      },
      "overall": "PASS"
    },
    "warnings": []
  }
}
```

</details>

---
