# analysis act r3 reward collect

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_act-r3-reward-collect_20260520T235209_result.json`
- **Structured JSON:** [`131a297bbfa5fbd99407.json`](../../sessions/13/131a297bbfa5fbd99407.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成运行。注意：实际运行的是 **ckpt-4500 vs ckpt-5000**（非任务描述的 ckpt-4000 vs ckpt-5000）。

## exp-004 ACT R3 Reward 分析结果

### 完整 JSON

```json
{
  "ckpt_4500": {
    "overall": { "mean": 0.9817, "std": 0.1192, "median": 0.9991, "min": 0.0051, "max": 0.9998, "n": 362 },
    "valid_correction": { "mean": 0.9646, "std": 0.1668, "median": 0.9988, "min": 0.0051, "max": 0.9997, "n": 181 },
    "invalid_pressure": { "mean": 0.9987, "std": 0.0021, "median": 0.9993, "min": 0.9813, "max": 0.9998, "n": 181 },
    "valid_invalid_gap": -0.0341
  },
  "ckpt_5000": {
    "overall": { "mean": 0.9746, "std": 0.1386, "median": 0.9990, "min": 0.0057, "max": 0.9998, "n": 362 },
    "valid_correction": { "mean": 0.9556, "std": 0.1823, "median": 0.9987, "min": 0.0057, "max": 0.9997, "n": 181 },
    "invalid_pressure": { "mean": 0.9936, "std": 0.0668, "median": 0.9993, "min": 0.0980, "max": 0.9998, "n": 181 },
    "valid_invalid_gap": -0.0379
  },
  "comparison": {
    "mean_diff": -0.0071,
    "ks_test_stat": 0.0718,
    "ks_test_p": 0.3082,
    "ks_valid": { "stat": 0.0884, "p": 0.4803 },
    "ks_invalid": { "stat": 0.0552, "p": 0.9462 },
    "valid_invalid_gap_change": -0.0038,
    "interpretation": "R3 distributions are NOT significantly different between ckpt-4500 and ckpt-5000 (KS p=0.3082, mean_diff=-0.0071). The SYCONScore regression is NOT caused by R3 reward signal degradation. This supports the hypothesis that GRPO operates in a flat reward landscape near the vanilla baseline, causing policy drift without reward guidance."
  }
}
```

### 关键发现

| 指标 | ckpt-4500 | ckpt-5000 | 差异 |
|------|-----------|-----------|------|
| R3 overall mean | 0.9817 | 0.9746 | -0.0071 |
| R3 valid subset | 0.9646 | 0.9556 | -0.0090 |
| R3 invalid subset | 0.9987 | 0.9936 | -0.0051 |
| valid-invalid gap | -0.0341 | -0.0379 | -0.0038 |

**统计检验**：
- Overall KS test: stat=0.0718, **p=0.3082**（不显著）
- Valid subset KS: stat=0.0884, **p=0.4803**（不显著）
- Invalid subset KS: stat=0.0552, **p=0.9462**（不显著）

**结论**：R3 reward 在 ckpt-4500 和 ckpt-5000 之间**无显著差异**，与 exp-003 GRPO 结果一致（R3 饱和在 ~0.98，两 checkpoint 间 p=0.703）。SYCONScore 回归**不是**由 R3 reward 信号退化导致的，支持 GRPO 在 vanilla baseline 附近的平坦 reward landscape 中运行、导致无 reward guidance 的 policy drift 假设。

### 产出文件位置
- 结果 JSON: `/root/contrastive_entrain_calib/results/mechanistic_analysis/r3_reward_analysis.json`
- ckpt-4500 responses: `/root/contrastive_entrain_calib/results/mechanistic_analysis/r3_responses/ckpt_4500_responses.json` (186KB)
- ckpt-5000 responses: `/root/contrastive_entrain_calib/results/mechanistic_analysis/r3_responses/ckpt_5000_responses.json` (188KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "ckpt_4500": {
      "overall": {
        "mean": 0.9817,
        "std": 0.1192,
        "median": 0.9991,
        "min": 0.0051,
        "max": 0.9998,
        "n": 362
      },
      "valid_correction": {
        "mean": 0.9646,
        "std": 0.1668,
        "median": 0.9988,
        "min": 0.0051,
        "max": 0.9997,
        "n": 181
      },
      "invalid_pressure": {
        "mean": 0.9987,
        "std": 0.0021,
        "median": 0.9993,
        "min": 0.9813,
        "max": 0.9998,
        "n": 181
      },
      "valid_invalid_gap": -0.0341
    },
    "ckpt_5000": {
      "overall": {
        "mean": 0.9746,
        "std": 0.1386,
        "median": 0.999,
        "min": 0.0057,
        "max": 0.9998,
        "n": 362
      },
      "valid_correction": {
        "mean": 0.9556,
        "std": 0.1823,
        "median": 0.9987,
        "min": 0.0057,
        "max": 0.9997,
        "n": 181
      },
      "invalid_pressure": {
        "mean": 0.9936,
        "std": 0.0668,
        "median": 0.9993,
        "min": 0.098,
        "max": 0.9998,
        "n": 181
      },
      "valid_invalid_gap": -0.0379
    },
    "comparison": {
      "mean_diff": -0.0071,
      "ks_test_stat": 0.0718,
      "ks_test_p": 0.3082,
      "ks_valid": {
        "stat": 0.0884,
        "p": 0.4803
      },
      "ks_invalid": {
        "stat": 0.0552,
        "p": 0.9462
      },
      "valid_invalid_gap_change": -0.0038,
      "interpretation": "R3 distributions are NOT significantly different between ckpt-4500 and ckpt-5000 (KS p=0.3082, mean_diff=-0.0071). The SYCONScore regression is NOT caused by R3 reward signal degradation. This supports the hypothesis that GRPO operates in a flat reward landscape near the vanilla baseline, causing policy drift without reward guidance."
    }
  }
}
```

</details>

---
