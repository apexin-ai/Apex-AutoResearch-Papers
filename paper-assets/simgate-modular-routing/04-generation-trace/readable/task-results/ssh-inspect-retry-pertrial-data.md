# ssh inspect retry pertrial data

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_inspect-retry-pertrial-data_20260518T171238_result.json`
- **Structured JSON:** [`c9307fa92f1cf44f5a93.json`](../../sessions/c9/c9307fa92f1cf44f5a93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 <5 trials 的 episode 都是因为 early success 提前终止，数据完全正确。

## Retry Per-Trial Data Availability

**有/无 per-trial 数据: YES**

**数据路径:** `/root/autodl-tmp/simgate-modular-routing/results/retry_dose_response/retry_n5/`

**数据格式:** 每个 episode 一个 JSON 文件（`{task_name}_ep{NNN}.json`），结构：
```json
{
  "task_name": "...",
  "variation_idx": 0,
  "mode": "retry",
  "trials": [
    {
      "trial_idx": 0,
      "score": -100.0,
      "is_death": true,
      "is_success": false,
      "num_steps": 18,
      "time_s": 15.9,
      "actions": ["..."],
      "reflection_text": null
    },
    // ... trial_idx 1..4
  ],
  "num_trials": 5,
  "final_score": -100.0,
  "final_is_death": true,
  "final_is_success": false,
  "success_trial": null
}
```

**统计:**
- N=5 episode 文件数: **200**（10 tasks × 20 eps）
- Trial 数分布: 180 个有 5 trials, 20 个因 early success 提前终止（14×1 trial, 3×2, 1×3, 2×4）
- **N=3 数据不存在**，只跑了 N=5 条件

**Cutoff=1 验证:**
- trial[0] death rate = **96/200 = 48.0%**
- vs 已知 N=1 DR = 46.5%
- 差异 1.5pp，在 200 episodes 的采样误差范围内（SE ≈ 3.5pp），**验证通过**

**结论:** Per-trial 数据完整且格式良好，可以从 N=5 数据中合成任意 cutoff (1-5) 的 dose-response 曲线，无需补跑。

---
