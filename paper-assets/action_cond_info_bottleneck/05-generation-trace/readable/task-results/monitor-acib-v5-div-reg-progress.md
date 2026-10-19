# monitor acib v5 div reg progress

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_acib_v5_div_reg_progress_20260516T040654_result.json`
- **Structured JSON:** [`d1bb0560366462dc9613.json`](../../sessions/d1/d1bb0560366462dc9613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "acib_v5_div_reg": {
    "current_step": 8100,
    "total_steps": 20000,
    "scorer_std": 0.445,
    "scorer_mean": 0.551,
    "task_loss": 0.0603,
    "ib_loss": 0.1600,
    "div_loss": -0.4473,
    "beta": 0.01,
    "speed": "0.9 steps/s",
    "healthy": true,
    "eta_completion": "~3.7h",
    "checkpoint_exists": true,
    "checkpoint": "checkpoint-5000",
    "process_uptime": "2h36m",
    "gpu": "cuda:0, 11% util, 21.6GB/97.9GB",
    "notes": "非常稳定。scorer_std 从 step 3300 的 0.434 微升至 0.445，无 collapse 迹象。task_loss 从 ~0.10 降到 ~0.05，持续下降。"
  },
  "acib_v5_div_reg_seed2": {
    "current_step": 1400,
    "total_steps": 20000,
    "scorer_std": 0.422,
    "scorer_mean": 0.559,
    "task_loss": 0.0612,
    "ib_loss": 0.1472,
    "div_loss": -0.4238,
    "beta": 0.004,
    "speed": "0.7 steps/s",
    "healthy": true,
    "eta_completion": "~7.4h",
    "gpu": "cuda:1, 65% util, 22.8GB/97.9GB",
    "notes": "日志恢复正常。β 仍在 warmup 中（0.004/0.01）。scorer_std=0.422 健康。"
  }
}
```

两个 run 都健康，scorer_std 远高于 0.05 阈值。v5_div_reg 已过 40%，task_loss 持续下降，预计约 3.7 小时完成。seed2 刚起步（step 1400），β 仍在 warmup，预计约 7.4 小时完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "acib_v5_div_reg": {
      "current_step": 8100,
      "total_steps": 20000,
      "scorer_std": 0.445,
      "scorer_mean": 0.551,
      "task_loss": 0.0603,
      "ib_loss": 0.16,
      "div_loss": -0.4473,
      "beta": 0.01,
      "speed": "0.9 steps/s",
      "healthy": true,
      "eta_completion": "~3.7h",
      "checkpoint_exists": true,
      "checkpoint": "checkpoint-5000",
      "process_uptime": "2h36m",
      "gpu": "cuda:0, 11% util, 21.6GB/97.9GB",
      "notes": "非常稳定。scorer_std 从 step 3300 的 0.434 微升至 0.445，无 collapse 迹象。task_loss 从 ~0.10 降到 ~0.05，持续下降。"
    },
    "acib_v5_div_reg_seed2": {
      "current_step": 1400,
      "total_steps": 20000,
      "scorer_std": 0.422,
      "scorer_mean": 0.559,
      "task_loss": 0.0612,
      "ib_loss": 0.1472,
      "div_loss": -0.4238,
      "beta": 0.004,
      "speed": "0.7 steps/s",
      "healthy": true,
      "eta_completion": "~7.4h",
      "gpu": "cuda:1, 65% util, 22.8GB/97.9GB",
      "notes": "日志恢复正常。β 仍在 warmup 中（0.004/0.01）。scorer_std=0.422 健康。"
    }
  }
}
```

</details>

---
