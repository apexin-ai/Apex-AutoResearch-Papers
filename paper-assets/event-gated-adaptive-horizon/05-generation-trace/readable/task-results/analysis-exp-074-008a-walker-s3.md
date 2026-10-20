# analysis exp 074 008a walker s3

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_074_008a_walker_s3_20260525T120625_result.json`
- **Structured JSON:** [`f2c89ae0278457790f54.json`](../../sessions/f2/f2c89ae0278457790f54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已提取完毕。

## exp_074_008a_walker_s3 Metrics Summary

```json
{
  "experiment": "exp_074_008a_walker_s3",
  "config": "008a (trained dt_emb unexposed, subsample OFF, gate_fixed_dt=2, H=15)",
  "env": "walker_walk",
  "seed": 3,
  "total_steps": 105000,
  "status": "completed (EXIT_CODE=0)",

  "eval_return_trajectory": {
    "5K": 36.1, "15K": 281.0, "25K": 389.8, "35K": 303.8,
    "45K": 437.3, "55K": 411.3, "65K": 566.4, "75K": 513.9,
    "85K": 645.9, "95K": 776.6, "105K": 855.9
  },

  "final_105K": {
    "eval_return": 855.9,
    "civo_ve_ratio_final": 0.3,
    "civo_delta_ve_final": -0.0,
    "civo_alert": 0,
    "value_mean": 295.2,
    "value_std": 8.9,
    "target_mean": 295.9,
    "target_std": 9.3,
    "normed_target_mean": 0.7,
    "EMA_005": 275.6,
    "EMA_095": 303.6,
    "gate_dt_mean": 2.0,
    "gate_dt_std": 0.0,
    "gate_dt_2_frac": 1.0,
    "gate_empirical_entropy": 0.0,
    "actor_entropy": -5.1,
    "model_loss": 3.8,
    "kl": 4.4,
    "value_loss": 0.9,
    "actor_loss": -0.0
  },

  "civo_trajectory": {
    "15K":  {"ve_ratio": 0.0, "delta_ve": 0.0, "alert": 0},
    "25K":  {"ve_ratio": 0.1, "delta_ve": 0.1, "alert": 0},
    "35K":  {"ve_ratio": 0.3, "delta_ve": 0.2, "alert": 0},
    "45K":  {"ve_ratio": 0.3, "delta_ve": 0.0, "alert": 0},
    "85K":  {"ve_ratio": 0.4, "delta_ve": -0.1, "alert": 0},
    "95K":  {"ve_ratio": 0.4, "delta_ve": -0.0, "alert": 0},
    "105K": {"ve_ratio": 0.3, "delta_ve": -0.0, "alert": 0}
  },

  "anomalies": "none"
}
```

## CIVO 判定

**civo_alert = 0** — 无 CIVO。ve_ratio 全程 ≤ 0.4，105K 时降至 0.3，delta_ve 为负（value 未过度膨胀）。

## 4-seed 对比

| Metric | seed 0 | seed 1 | seed 2 | **seed 3** |
|---|---|---|---|---|
| eval_return_105K | 777.7 | 630.9 | 899.4 | **855.9** |
| civo_ve_ratio_final | 0.59 | 0.43 | 0.33 | **0.30** |
| civo_alert | 0 | 0 | 0 | **0** |
| gate_dt_2_frac | 1.0 | 1.0 | 1.0 | **1.0** |

**4/4 seeds 全部 civo_alert=0，C3 claim (value suppression without CIVO) 统计上稳固。**

- 4-seed eval_return 均值: **791.0 ± 102.2**（range: 630.9–899.4）
- seed 3 是第二高 return（855.9），ve_ratio 最低（0.3），表现优异
- gate 行为完全一致：dt_2_frac=1.0，fixed gate 无变异

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment": "exp_074_008a_walker_s3",
    "config": "008a (trained dt_emb unexposed, subsample OFF, gate_fixed_dt=2, H=15)",
    "env": "walker_walk",
    "seed": 3,
    "total_steps": 105000,
    "status": "completed (EXIT_CODE=0)",
    "eval_return_trajectory": {
      "5K": 36.1,
      "15K": 281.0,
      "25K": 389.8,
      "35K": 303.8,
      "45K": 437.3,
      "55K": 411.3,
      "65K": 566.4,
      "75K": 513.9,
      "85K": 645.9,
      "95K": 776.6,
      "105K": 855.9
    },
    "final_105K": {
      "eval_return": 855.9,
      "civo_ve_ratio_final": 0.3,
      "civo_delta_ve_final": -0.0,
      "civo_alert": 0,
      "value_mean": 295.2,
      "value_std": 8.9,
      "target_mean": 295.9,
      "target_std": 9.3,
      "normed_target_mean": 0.7,
      "EMA_005": 275.6,
      "EMA_095": 303.6,
      "gate_dt_mean": 2.0,
      "gate_dt_std": 0.0,
      "gate_dt_2_frac": 1.0,
      "gate_empirical_entropy": 0.0,
      "actor_entropy": -5.1,
      "model_loss": 3.8,
      "kl": 4.4,
      "value_loss": 0.9,
      "actor_loss": -0.0
    },
    "civo_trajectory": {
      "15K": {
        "ve_ratio": 0.0,
        "delta_ve": 0.0,
        "alert": 0
      },
      "25K": {
        "ve_ratio": 0.1,
        "delta_ve": 0.1,
        "alert": 0
      },
      "35K": {
        "ve_ratio": 0.3,
        "delta_ve": 0.2,
        "alert": 0
      },
      "45K": {
        "ve_ratio": 0.3,
        "delta_ve": 0.0,
        "alert": 0
      },
      "85K": {
        "ve_ratio": 0.4,
        "delta_ve": -0.1,
        "alert": 0
      },
      "95K": {
        "ve_ratio": 0.4,
        "delta_ve": -0.0,
        "alert": 0
      },
      "105K": {
        "ve_ratio": 0.3,
        "delta_ve": -0.0,
        "alert": 0
      }
    },
    "anomalies": "none"
  }
}
```

</details>

---
