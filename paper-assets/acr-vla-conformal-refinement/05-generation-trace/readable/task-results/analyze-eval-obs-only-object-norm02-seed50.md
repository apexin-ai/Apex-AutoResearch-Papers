# analyze eval obs only object norm02 seed50

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-obs-only-object-norm02-seed50_20260520T145649_result.json`
- **Structured JSON:** [`35bb483fb395c94c45a6.json`](../../sessions/35/35bb483fb395c94c45a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval-obs-only-object-norm02-seed50 结果

### JSON 内容

```json
{
  "mode": "crm_obs_only",
  "baseline_mode": "single",
  "benchmark": "object",
  "n_rollouts": 10,
  "overall_success_rate": 0.18,
  "per_task": {
    "pick_up_the_alphabet_soup_and_place_it_in_the_basket":    {"success_rate": 0.0, "successes": 0,  "total": 10},
    "pick_up_the_cream_cheese_and_place_it_in_the_basket":     {"success_rate": 0.1, "successes": 1,  "total": 10},
    "pick_up_the_salad_dressing_and_place_it_in_the_basket":   {"success_rate": 0.2, "successes": 2,  "total": 10},
    "pick_up_the_bbq_sauce_and_place_it_in_the_basket":        {"success_rate": 0.5, "successes": 5,  "total": 10},
    "pick_up_the_ketchup_and_place_it_in_the_basket":          {"success_rate": 0.0, "successes": 0,  "total": 10},
    "pick_up_the_tomato_sauce_and_place_it_in_the_basket":     {"success_rate": 0.1, "successes": 1,  "total": 10},
    "pick_up_the_butter_and_place_it_in_the_basket":           {"success_rate": 0.1, "successes": 1,  "total": 10},
    "pick_up_the_milk_and_place_it_in_the_basket":             {"success_rate": 0.3, "successes": 3,  "total": 10},
    "pick_up_the_chocolate_pudding_and_place_it_in_the_basket":{"success_rate": 0.3, "successes": 3,  "total": 10},
    "pick_up_the_orange_juice_and_place_it_in_the_basket":     {"success_rate": 0.2, "successes": 2,  "total": 10}
  }
}
```

### 日志尾部（最后 50 行）

```
[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 50, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_obs_only_object_norm02_seed50.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5}
[eval] Mode: crm_obs_only, benchmark: object
[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...
Loading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...
[transformers] `torch_dtype` is deprecated! Use `dtype` instead!
Loading weights: 100%|██████████| 489/489 [00:00<00:00, 3208.96it/s]
Reducing the number of VLM layers to 16 ...
Loading weights from local directory
[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)
[eval] Override max_correction_norm = 0.2
[eval] Loading LIBERO object environments...
[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[eval] 10 tasks loaded.
  alphabet_soup:        0.0% (0/10)
  cream_cheese:        10.0% (1/10)
  salad_dressing:      20.0% (2/10)
  bbq_sauce:           50.0% (5/10)
  ketchup:              0.0% (0/10)
  tomato_sauce:        10.0% (1/10)
  butter:              10.0% (1/10)
  milk:                30.0% (3/10)
  chocolate_pudding:   30.0% (3/10)
  orange_juice:        20.0% (2/10)

============================================================
Overall success rate (crm_obs_only): 18.0% (18/100)
============================================================
[eval] Results saved to logs/eval_obs_only_object_norm02_seed50.json
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
EXIT_CODE=0
```

### 摘要

| 指标 | 值 |
|------|-----|
| **overall_success_rate** | **18%** |
| **total_rollouts** | 100 (10 tasks x 10 rollouts) |
| **total_successes** | 18 |
| error/warning | 无错误。1 个 DeprecationWarning（`torch_dtype` deprecated）和 1 个 `swigvarlink` DeprecationWarning，均不影响结果。EXIT_CODE=0。 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "mode": "crm_obs_only",
    "baseline_mode": "single",
    "benchmark": "object",
    "n_rollouts": 10,
    "overall_success_rate": 0.18,
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
        "success_rate": 0.2,
        "successes": 2,
        "total": 10
      },
      "pick_up_the_bbq_sauce_and_place_it_in_the_basket": {
        "success_rate": 0.5,
        "successes": 5,
        "total": 10
      },
      "pick_up_the_ketchup_and_place_it_in_the_basket": {
        "success_rate": 0.0,
        "successes": 0,
        "total": 10
      },
      "pick_up_the_tomato_sauce_and_place_it_in_the_basket": {
        "success_rate": 0.1,
        "successes": 1,
        "total": 10
      },
      "pick_up_the_butter_and_place_it_in_the_basket": {
        "success_rate": 0.1,
        "successes": 1,
        "total": 10
      },
      "pick_up_the_milk_and_place_it_in_the_basket": {
        "success_rate": 0.3,
        "successes": 3,
        "total": 10
      },
      "pick_up_the_chocolate_pudding_and_place_it_in_the_basket": {
        "success_rate": 0.3,
        "successes": 3,
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
