# diag extract metrics and check v6

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_extract-metrics-and-check-v6_20260514T035907_result.json`
- **Structured JSON:** [`435e8e753d681b5417ab.json`](../../sessions/43/435e8e753d681b5417ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新成功。

## Metrics 提取结果

### mvp_v5_random_s030
```json
{
  "ii_high_median": 5.377512,
  "ii_mid_median": 5.886454,
  "ii_low_median": 3.776818,
  "ii_high_mean": 22.734534,
  "ii_mid_mean": 10.943319,
  "ii_low_mean": 11.840449,
  "ii_high_ci": [10.352118, 42.551951],
  "ii_mid_ci": [7.398611, 14.765315],
  "ii_low_ci": [4.097309, 23.545273],
  "kv_ppl_high": 8.1027,
  "kv_ppl_mid": 8.5701,
  "kv_ppl_low": 13.4922,
  "both_ppl_high": 41.3452,
  "both_ppl_mid": 24.1992,
  "both_ppl_low": 68.5301,
  "problems": 50
}
```

### mvp_v5_random_s020
```json
{
  "ii_high_median": 0.321331,
  "ii_mid_median": 0.455663,
  "ii_low_median": 0.591916,
  "ii_high_mean": 0.855584,
  "ii_mid_mean": 1.258123,
  "ii_low_mean": 0.956933,
  "ii_high_ci": [-0.124133, 1.616883],
  "ii_mid_ci": [0.674852, 2.075565],
  "ii_low_ci": [0.583856, 1.413355],
  "kv_ppl_high": 4.2537,
  "kv_ppl_mid": 4.3064,
  "kv_ppl_low": 5.4048,
  "both_ppl_high": 7.9749,
  "both_ppl_mid": 6.8553,
  "both_ppl_low": 22.5868,
  "problems": 50
}
```

## v6 实验状态
- **v6_importance_s025**: running, 进度 21/50 (cuda:2, PID 62967, elapsed ~12min)
- **v6_importance_s030**: running, 进度 20/50 (cuda:3, PID 63113, elapsed ~12min)
- **v6_importance_s015**: running, 进度 10/50 (cuda:0, 有日志输出)
- **v6_importance_s020**: running, 进度 10/50 (cuda:1, 有日志输出)

## GPU 状态
```
GPU 0: 77% util, 27717 / 97887 MiB  (v6_importance_s015)
GPU 1: 76% util, 27717 / 97887 MiB  (v6_importance_s020)
GPU 2: 96% util, 33509 / 97887 MiB  (v6_importance_s025)
GPU 3: 77% util, 30829 / 97887 MiB  (v6_importance_s030)
```

4 个 v6 实验全部在跑，4 张 GPU 满载。按当前速率估算，s025/s030 约再需 ~20min 完成，s015/s020 约需 ~30min。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "ii_high_median": 0.321331,
    "ii_mid_median": 0.455663,
    "ii_low_median": 0.591916,
    "ii_high_mean": 0.855584,
    "ii_mid_mean": 1.258123,
    "ii_low_mean": 0.956933,
    "ii_high_ci": [
      -0.124133,
      1.616883
    ],
    "ii_mid_ci": [
      0.674852,
      2.075565
    ],
    "ii_low_ci": [
      0.583856,
      1.413355
    ],
    "kv_ppl_high": 4.2537,
    "kv_ppl_mid": 4.3064,
    "kv_ppl_low": 5.4048,
    "both_ppl_high": 7.9749,
    "both_ppl_mid": 6.8553,
    "both_ppl_low": 22.5868,
    "problems": 50
  }
}
```

</details>

---
