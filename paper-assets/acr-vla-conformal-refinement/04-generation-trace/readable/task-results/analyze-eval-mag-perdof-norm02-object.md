# analyze eval mag perdof norm02 object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-mag-perdof-norm02-object_20260516T060632_result.json`
- **Structured JSON:** [`103281183a88e5868df7.json`](../../sessions/10/103281183a88e5868df7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 内容：

```json
{
  "mode": "crm_perdof",
  "baseline_mode": "single",
  "benchmark": "object",
  "n_rollouts": 10,
  "overall_success_rate": 0.11,
  "per_task": {
    "pick_up_the_alphabet_soup_and_place_it_in_the_basket": {
      "success_rate": 0.0,
      "successes": 0,
      "total": 10
    },
    "pick_up_the_cream_cheese_and_place_it_in_the_basket": {
      "success_rate": 0.1,
      "successes": 1,
      "total": 10
    },
    "pick_up_the_salad_dressing_and_place_it_in_the_basket": {
      "success_rate": 0.1,
      "successes": 1,
      "total": 10
    },
    "pick_up_the_bbq_sauce_and_place_it_in_the_basket": {
      "success_rate": 0.1,
      "successes": 1,
      "total": 10
    },
    "pick_up_the_ketchup_and_place_it_in_the_basket": {
      "success_rate": 0.0,
      "successes": 0,
      "total": 10
    },
    "pick_up_the_tomato_sauce_and_place_it_in_the_basket": {
      "success_rate": 0.0,
      "successes": 0,
      "total": 10
    },
    "pick_up_the_butter_and_place_it_in_the_basket": {
      "success_rate": 0.1,
      "successes": 1,
      "total": 10
    },
    "pick_up_the_milk_and_place_it_in_the_basket": {
      "success_rate": 0.1,
      "successes": 1,
      "total": 10
    },
    "pick_up_the_chocolate_pudding_and_place_it_in_the_basket": {
      "success_rate": 0.4,
      "successes": 4,
      "total": 10
    },
    "pick_up_the_orange_juice_and_place_it_in_the_basket": {
      "success_rate": 0.2,
      "successes": 2,
      "total": 10
    }
  }
}
```

**汇总：**

- 完成 tasks: **10/10**，每个 task 均跑满 10 rollouts
- **Overall success rate: 0.11 (11%)**
- 无错误信息

| Task | Success Rate |
|------|-------------|
| alphabet_soup | 0.0 |
| cream_cheese | 0.1 |
| salad_dressing | 0.1 |
| bbq_sauce | 0.1 |
| ketchup | 0.0 |
| tomato_sauce | 0.0 |
| butter | 0.1 |
| milk | 0.1 |
| chocolate_pudding | **0.4** |
| orange_juice | 0.2 |

chocolate_pudding 最高 (40%)，alphabet_soup / ketchup / tomato_sauce 三个 task 完全失败。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "mode": "crm_perdof",
    "baseline_mode": "single",
    "benchmark": "object",
    "n_rollouts": 10,
    "overall_success_rate": 0.11,
    "per_task": {
      "pick_up_the_alphabet_soup_and_place_it_in_the_basket": {
        "success_rate": 0.0,
        "successes": 0,
        "total": 10
      },
      "pick_up_the_cream_cheese_and_place_it_in_the_basket": {
        "success_rate": 0.1,
        "successes": 1,
        "total": 10
      },
      "pick_up_the_salad_dressing_and_place_it_in_the_basket": {
        "success_rate": 0.1,
        "successes": 1,
        "total": 10
      },
      "pick_up_the_bbq_sauce_and_place_it_in_the_basket": {
        "success_rate": 0.1,
        "successes": 1,
        "total": 10
      },
      "pick_up_the_ketchup_and_place_it_in_the_basket": {
        "success_rate": 0.0,
        "successes": 0,
        "total": 10
      },
      "pick_up_the_tomato_sauce_and_place_it_in_the_basket": {
        "success_rate": 0.0,
        "successes": 0,
        "total": 10
      },
      "pick_up_the_butter_and_place_it_in_the_basket": {
        "success_rate": 0.1,
        "successes": 1,
        "total": 10
      },
      "pick_up_the_milk_and_place_it_in_the_basket": {
        "success_rate": 0.1,
        "successes": 1,
        "total": 10
      },
      "pick_up_the_chocolate_pudding_and_place_it_in_the_basket": {
        "success_rate": 0.4,
        "successes": 4,
        "total": 10
      },
      "pick_up_the_orange_juice_and_place_it_in_the_basket": {
        "success_rate": 0.2,
        "successes": 2,
        "total": 10
      }
    }
  }
}
```

</details>

---
