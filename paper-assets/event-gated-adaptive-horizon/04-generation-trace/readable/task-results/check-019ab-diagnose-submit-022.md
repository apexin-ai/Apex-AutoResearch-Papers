# check 019ab diagnose submit 022

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_019ab-diagnose-submit-022_20260517T073927_result.json`
- **Structured JSON:** [`170a89fa350ff98f5ece.json`](../../sessions/17/170a89fa350ff98f5ece.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 019a_v2：**未 hang，仍在活跃训练**

- 最新步数：**200,248**（已超过 200K 目标）
- metrics.jsonl 最后修改时间：15:40:16（刚刚）
- GPU 1 利用率 21%，内存 4152MiB，活跃运行中
- 进程仍在收集新 episode（train_eps 目录 15:40 修改）

**原因**：DreamerV3 的 `--steps 200000` 检查发生在 episode 边界，当前正在完成最后几个 episode 后退出（每 episode 200 步，已 overshoot 248 步）。预计很快自行退出，**不需要 kill**。

### 019b：正常运行中

- 当前步数：**75,800**（38% of 200K）
- 最新 eval (step 72500)：eval_return = 8.55
- 趋势令人担忧：eval_return 从 step 22500 的 24.9 **下跌**到 72500 的 8.5

---

### 完整 V/E Trajectory JSON

```json
{
  "exp_019a_v2": [
    {"step": 2500, "eval_return": 1.1101, "value_mean": 0.0009, "value_step": 2500, "ve_ratio": 0.0008},
    {"step": 12500, "eval_return": 24.8974, "value_mean": 4.0142, "value_step": 12500, "ve_ratio": 0.1612},
    {"step": 22500, "eval_return": 19.3449, "value_mean": 20.6274, "value_step": 22500, "ve_ratio": 1.0663},
    {"step": 32500, "eval_return": 33.1948, "value_mean": 34.9113, "value_step": 32500, "ve_ratio": 1.0517},
    {"step": 42500, "eval_return": 21.6646, "value_mean": 45.4839, "value_step": 42500, "ve_ratio": 2.0995},
    {"step": 52500, "eval_return": 37.304, "value_mean": 55.8039, "value_step": 52500, "ve_ratio": 1.4959},
    {"step": 62500, "eval_return": 29.251, "value_mean": 67.6433, "value_step": 62500, "ve_ratio": 2.3125},
    {"step": 72500, "eval_return": 35.8551, "value_mean": 78.0064, "value_step": 72500, "ve_ratio": 2.1756},
    {"step": 82500, "eval_return": 47.0267, "value_mean": 90.7225, "value_step": 82500, "ve_ratio": 1.9292},
    {"step": 92500, "eval_return": 52.8245, "value_mean": 103.1891, "value_step": 92500, "ve_ratio": 1.9534},
    {"step": 102500, "eval_return": 34.4681, "value_mean": 122.5622, "value_step": 102500, "ve_ratio": 3.5558},
    {"step": 112500, "eval_return": 54.5089, "value_mean": 136.3336, "value_step": 112500, "ve_ratio": 2.5011},
    {"step": 122500, "eval_return": 64.0628, "value_mean": 138.4998, "value_step": 122500, "ve_ratio": 2.1619},
    {"step": 132500, "eval_return": 67.9603, "value_mean": 139.6969, "value_step": 132500, "ve_ratio": 2.0556},
    {"step": 142500, "eval_return": 50.2919, "value_mean": 140.7631, "value_step": 142500, "ve_ratio": 2.7989},
    {"step": 152500, "eval_return": 64.1783, "value_mean": 141.6879, "value_step": 152500, "ve_ratio": 2.2077},
    {"step": 162500, "eval_return": 69.7027, "value_mean": 143.1686, "value_step": 162500, "ve_ratio": 2.054},
    {"step": 172500, "eval_return": 53.1707, "value_mean": 143.0454, "value_step": 172500, "ve_ratio": 2.6903},
    {"step": 182500, "eval_return": 60.3929, "value_mean": 143.2542, "value_step": 182500, "ve_ratio": 2.372},
    {"step": 192500, "eval_return": 69.4327, "value_mean": 143.4017, "value_step": 192500, "ve_ratio": 2.0653}
  ],
  "exp_019b": [
    {"step": 2500, "eval_return": 0.8219, "value_mean": 0.0008, "value_step": 2500, "ve_ratio": 0.001},
    {"step": 12500, "eval_return": 16.8697, "value_mean": 3.4753, "value_step": 12500, "ve_ratio": 0.206},
    {"step": 22500, "eval_return": 24.8962, "value_mean": 17.5993, "value_step": 22500, "ve_ratio": 0.7069},
    {"step": 32500, "eval_return": 10.6161, "value_mean": 27.174, "value_step": 32500, "ve_ratio": 2.5597},
    {"step": 42500, "eval_return": 14.3773, "value_mean": 25.1861, "value_step": 42500, "ve_ratio": 1.7518},
    {"step": 52500, "eval_return": 3.6862, "value_mean": 20.8537, "value_step": 52500, "ve_ratio": 5.6573},
    {"step": 62500, "eval_return": 5.9489, "value_mean": 15.9264, "value_step": 62500, "ve_ratio": 2.6772},
    {"step": 72500, "eval_return": 8.5459, "value_mean": 11.7682, "value_step": 72500, "ve_ratio": 1.3771}
  ]
}
```

### 关键观察

**019a_v2 (baseline)**：
- eval_return 从 ~20 缓慢升至 ~65-70（大方差）
- value_mean 持续上升到 ~143 后饱和（step 120K+）
- V/E ratio 稳定在 **2.0-2.8**，说明 value function 系统性高估约 2x

**019b (CIVO trigger)**：
- eval_return **崩塌**：从 step 22500 的 24.9 跌至 52500 的 3.7，目前缓慢回升到 8.5
- value_mean 也在下降（27 → 11.8），但速度慢于 eval_return
- V/E ratio 在 step 52500 飙到 5.66（value 严重脱离现实），现已回落到 1.38
- **019b 存在明显的训练不稳定问题**，CIVO trigger 机制可能在早期引入了过多干扰

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exp_019a_v2": [
      {
        "step": 2500,
        "eval_return": 1.1101,
        "value_mean": 0.0009,
        "value_step": 2500,
        "ve_ratio": 0.0008
      },
      {
        "step": 12500,
        "eval_return": 24.8974,
        "value_mean": 4.0142,
        "value_step": 12500,
        "ve_ratio": 0.1612
      },
      {
        "step": 22500,
        "eval_return": 19.3449,
        "value_mean": 20.6274,
        "value_step": 22500,
        "ve_ratio": 1.0663
      },
      {
        "step": 32500,
        "eval_return": 33.1948,
        "value_mean": 34.9113,
        "value_step": 32500,
        "ve_ratio": 1.0517
      },
      {
        "step": 42500,
        "eval_return": 21.6646,
        "value_mean": 45.4839,
        "value_step": 42500,
        "ve_ratio": 2.0995
      },
      {
        "step": 52500,
        "eval_return": 37.304,
        "value_mean": 55.8039,
        "value_step": 52500,
        "ve_ratio": 1.4959
      },
      {
        "step": 62500,
        "eval_return": 29.251,
        "value_mean": 67.6433,
        "value_step": 62500,
        "ve_ratio": 2.3125
      },
      {
        "step": 72500,
        "eval_return": 35.8551,
        "value_mean": 78.0064,
        "value_step": 72500,
        "ve_ratio": 2.1756
      },
      {
        "step": 82500,
        "eval_return": 47.0267,
        "value_mean": 90.7225,
        "value_step": 82500,
        "ve_ratio": 1.9292
      },
      {
        "step": 92500,
        "eval_return": 52.8245,
        "value_mean": 103.1891,
        "value_step": 92500,
        "ve_ratio": 1.9534
      },
      {
        "step": 102500,
        "eval_return": 34.4681,
        "value_mean": 122.5622,
        "value_step": 102500,
        "ve_ratio": 3.5558
      },
      {
        "step": 112500,
        "eval_return": 54.5089,
        "value_mean": 136.3336,
        "value_step": 112500,
        "ve_ratio": 2.5011
      },
      {
        "step": 122500,
        "eval_return": 64.0628,
        "value_mean": 138.4998,
        "value_step": 122500,
        "ve_ratio": 2.1619
      },
      {
        "step": 132500,
        "eval_return": 67.9603,
        "value_mean": 139.6969,
        "value_step": 132500,
        "ve_ratio": 2.0556
      },
      {
        "step": 142500,
        "eval_return": 50.2919,
        "value_mean": 140.7631,
        "value_step": 142500,
        "ve_ratio": 2.7989
      },
      {
        "step": 152500,
        "eval_return": 64.1783,
        "value_mean": 141.6879,
        "value_step": 152500,
        "ve_ratio": 2.2077
      },
      {
        "step": 162500,
        "eval_return": 69.7027,
        "value_mean": 143.1686,
        "value_step": 162500,
        "ve_ratio": 2.054
      },
      {
        "step": 172500,
        "eval_return": 53.1707,
        "value_mean": 143.0454,
        "value_step": 172500,
        "ve_ratio": 2.6903
      },
      {
        "step": 182500,
        "eval_return": 60.3929,
        "value_mean": 143.2542,
        "value_step": 182500,
        "ve_ratio": 2.372
      },
      {
        "step": 192500,
        "eval_return": 69.4327,
        "value_mean": 143.4017,
        "value_step": 192500,
        "ve_ratio": 2.0653
      }
    ],
    "exp_019b": [
      {
        "step": 2500,
        "eval_return": 0.8219,
        "value_mean": 0.0008,
        "value_step": 2500,
        "ve_ratio": 0.001
      },
      {
        "step": 12500,
        "eval_return": 16.8697,
        "value_mean": 3.4753,
        "value_step": 12500,
        "ve_ratio": 0.206
      },
      {
        "step": 22500,
        "eval_return": 24.8962,
        "value_mean": 17.5993,
        "value_step": 22500,
        "ve_ratio": 0.7069
      },
      {
        "step": 32500,
        "eval_return": 10.6161,
        "value_mean": 27.174,
        "value_step": 32500,
        "ve_ratio": 2.5597
      },
      {
        "step": 42500,
        "eval_return": 14.3773,
        "value_mean": 25.1861,
        "value_step": 42500,
        "ve_ratio": 1.7518
      },
      {
        "step": 52500,
        "eval_return": 3.6862,
        "value_mean": 20.8537,
        "value_step": 52500,
        "ve_ratio": 5.6573
      },
      {
        "step": 62500,
        "eval_return": 5.9489,
        "value_mean": 15.9264,
        "value_step": 62500,
        "ve_ratio": 2.6772
      },
      {
        "step": 72500,
        "eval_return": 8.5459,
        "value_mean": 11.7682,
        "value_step": 72500,
        "ve_ratio": 1.3771
      }
    ]
  }
}
```

</details>

---
