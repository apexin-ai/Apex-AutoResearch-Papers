# check read diagnostic data

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_read-diagnostic-data_20260516T013022_result.json`
- **Structured JSON:** [`5ab48cdbd5367c2ac4c3.json`](../../sessions/5a/5ab48cdbd5367c2ac4c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### margin_distribution_stats.json

```json
{
  "n_vis": 64,
  "n_samples": 400,
  "mean": -6.0494,
  "median": -2.8366,
  "std": 10.8459,
  "min": -150.3705,
  "max": 23.4338,
  "n_peaks": 1,
  "peaks": [
    {"score": -0.7861, "density": 0.0948}
  ],
  "per_sample_range_mean": 70.4355
}
```

### keep_ratio_sensitivity.json

```json
{
  "keep_ratios": [0.3, 0.5, 0.7, 0.9],
  "acis_losses": [0.0622, 0.0421, 0.0392, 0.0393],
  "random_losses": [0.0687, 0.0424, 0.0398, 0.0402],
  "full_loss": 0.0444,
  "n_batches": 100
}
```

关键观察：
- Margin 分布单峰（peak 在 -0.79），均值 -6.05，范围极大（-150 ~ +23），std=10.85
- ACIS 在所有 keep ratio 下均优于 random pruning，且在 0.7 和 0.9 时 loss（0.0392/0.0393）低于 full loss（0.0444），说明剪枝反而有正则化效果
- 0.5 是性价比拐点：keep 50% tokens 时 ACIS loss 0.0421 已接近 full loss

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "keep_ratios": [
      0.3,
      0.5,
      0.7,
      0.9
    ],
    "acis_losses": [
      0.0622,
      0.0421,
      0.0392,
      0.0393
    ],
    "random_losses": [
      0.0687,
      0.0424,
      0.0398,
      0.0402
    ],
    "full_loss": 0.0444,
    "n_batches": 100
  }
}
```

</details>

---
