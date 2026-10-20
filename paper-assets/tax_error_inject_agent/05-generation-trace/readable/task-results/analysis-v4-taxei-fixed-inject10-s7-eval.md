# analysis v4 taxei fixed inject10 s7 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-taxei-fixed-inject10-s7-eval_20260515T212122_result.json`
- **Structured JSON:** [`6ccabffb3eeb2758125b.json`](../../sessions/6c/6ccabffb3eeb2758125b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整指标如下：

```json
{
  "success_rate": 0.681,
  "successes": 32,
  "total": 47,
  "by_task_type": {
    "look_at_obj_in_light":        {"total": 6,  "success": 5, "rate": 0.833},
    "pick_and_place_simple":       {"total": 8,  "success": 5, "rate": 0.625},
    "pick_clean_then_place_in_recep": {"total": 11, "success": 7, "rate": 0.636},
    "pick_cool_then_place_in_recep":  {"total": 7,  "success": 4, "rate": 0.571},
    "pick_heat_then_place_in_recep":  {"total": 8,  "success": 7, "rate": 0.875},
    "pick_two_obj_and_place":         {"total": 7,  "success": 4, "rate": 0.571}
  }
}
```

**Checkpoint 路径**: `checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-1635`（eval 使用的版本），完整目录含两个 run：`v0-20260516-025729` 和 `v1-20260516-040128`。

**Log 路径**: `~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s7-eval.log`

**结果 JSON**: `eval_results/v4_taxei_fixed_inject10_s7_eval.json`

**警告**:
- `bitsandbytes` 加载失败（`libnvJitLink.so.13` 缺失），但未影响推理
- `torch_dtype` deprecated 警告
- 无 W&B 相关输出

**最强 task type**: `pick_heat_then_place_in_recep` (87.5%)，**最弱**: `pick_cool_then_place_in_recep` 和 `pick_two_obj_and_place` (均 57.1%)。所有失败 episode 均跑满 50 步上限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "success_rate": 0.681,
    "successes": 32,
    "total": 47,
    "by_task_type": {
      "look_at_obj_in_light": {
        "total": 6,
        "success": 5,
        "rate": 0.833
      },
      "pick_and_place_simple": {
        "total": 8,
        "success": 5,
        "rate": 0.625
      },
      "pick_clean_then_place_in_recep": {
        "total": 11,
        "success": 7,
        "rate": 0.636
      },
      "pick_cool_then_place_in_recep": {
        "total": 7,
        "success": 4,
        "rate": 0.571
      },
      "pick_heat_then_place_in_recep": {
        "total": 8,
        "success": 7,
        "rate": 0.875
      },
      "pick_two_obj_and_place": {
        "total": 7,
        "success": 4,
        "rate": 0.571
      }
    }
  }
}
```

</details>

---
