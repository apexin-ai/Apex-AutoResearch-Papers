# analysis eval acr spatial v4 small r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-acr-spatial-v4-small-r2_20260515T090657_result.json`
- **Structured JSON:** [`a25685da6b22e42d8666.json`](../../sessions/a2/a25685da6b22e42d8666.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval-acr-spatial-v4-small-r2 结果

### Per-Task Results (from r2 restart)
- T7 (pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate): **10%** (1/10)
- T8 (pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate): **40%** (4/10)
- T9 (pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate): **0%** (0/10)

### 完整 10-Task 汇总 (合并前序 T0-T6)

| Task | 成功率 |
|------|--------|
| T0 | 60% |
| T1 | 100% |
| T2 | 10% |
| T3 | 40% |
| T4 | 0% |
| T5 | 0% |
| T6 | 90% |
| T7 | 10% |
| T8 | 40% |
| T9 | 0% |

- **10-task 平均: 35.0%**
- r2 子集 (T7-T9) 平均: 16.7%
- 退出状态: **正常** (EXIT_CODE=0)

### 原始日志片段

```json
{
  "mode": "acr_vla",
  "baseline_mode": "single",
  "benchmark": "spatial",
  "n_rollouts": 10,
  "overall_success_rate": 0.16666666666666666,
  "per_task": {
    "pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate": {"success_rate": 0.1, "successes": 1, "total": 10},
    "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate": {"success_rate": 0.4, "successes": 4, "total": 10},
    "pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate": {"success_rate": 0.0, "successes": 0, "total": 10}
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "mode": "acr_vla",
    "baseline_mode": "single",
    "benchmark": "spatial",
    "n_rollouts": 10,
    "overall_success_rate": 0.16666666666666666,
    "per_task": {
      "pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate": {
        "success_rate": 0.1,
        "successes": 1,
        "total": 10
      },
      "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate": {
        "success_rate": 0.4,
        "successes": 4,
        "total": 10
      },
      "pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate": {
        "success_rate": 0.0,
        "successes": 0,
        "total": 10
      }
    }
  }
}
```

</details>

---
