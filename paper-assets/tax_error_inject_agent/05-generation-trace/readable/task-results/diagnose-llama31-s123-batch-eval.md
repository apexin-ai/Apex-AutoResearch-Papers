# diagnose llama31 s123 batch eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama31-s123-batch-eval_20260516T152051_result.json`
- **Structured JSON:** [`73ba9c29bd020616673e.json`](../../sessions/73/73ba9c29bd020616673e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 实验 | 状态 | 关键指标 |
|------|------|----------|
| **llama31-taxei-s123-eval** (injected) | `still_running` | 32/47 episodes done (~68%) |
| **llama31-taxei-s123-clean** | `completed` | success_rate = 0.617 |
| **llama31-random-s123-clean** | `completed` | success_rate = 0.766 |

### 详细 metrics

**llama31-taxei-s123-clean** (success_rate=0.617):
- look_at_obj_in_light: 4/6 (0.667)
- pick_and_place_simple: 3/8 (0.375)
- pick_clean_then_place_in_recep: 5/11 (0.455)
- pick_cool_then_place_in_recep: 4/7 (0.571)
- pick_heat_then_place_in_recep: 7/8 (0.875)
- pick_two_obj_and_place: 6/7 (0.857)

**llama31-random-s123-clean** (success_rate=0.766):
- look_at_obj_in_light: 6/6 (1.0)
- pick_and_place_simple: 5/8 (0.625)
- pick_clean_then_place_in_recep: 7/11 (0.636)
- pick_cool_then_place_in_recep: 4/7 (0.571)
- pick_heat_then_place_in_recep: 7/8 (0.875)
- pick_two_obj_and_place: 7/7 (1.0)

### GPU 状态
| GPU | Memory | Utilization |
|-----|--------|-------------|
| 0 | 16837 MiB | 44% |
| 1 | 16837 MiB | 88% |
| 2 | 16837 MiB | 88% |
| 3 | 0 MiB | 0% |

注：GPU 1 上还有一个额外的 `llama31-random-s123-injected` eval 在运行（queued after vanilla finished）。

```json
{"results": {"llama31-taxei-s123-eval": {"status": "still_running", "progress": "32/47 episodes"}, "llama31-taxei-s123-clean": {"status": "completed", "metrics": {"success_rate": 0.617, "by_task_type": {"look_at_obj_in_light": 0.667, "pick_and_place_simple": 0.375, "pick_clean_then_place_in_recep": 0.455, "pick_cool_then_place_in_recep": 0.571, "pick_heat_then_place_in_recep": 0.875, "pick_two_obj_and_place": 0.857}}}, "llama31-random-s123-clean": {"status": "completed", "metrics": {"success_rate": 0.766, "by_task_type": {"look_at_obj_in_light": 1.0, "pick_and_place_simple": 0.625, "pick_clean_then_place_in_recep": 0.636, "pick_cool_then_place_in_recep": 0.571, "pick_heat_then_place_in_recep": 0.875, "pick_two_obj_and_place": 1.0}}}}, "gpu_status": "GPU0-2 active (16.8GB, 44-88%), GPU3 idle"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "results": {
      "llama31-taxei-s123-eval": {
        "status": "still_running",
        "progress": "32/47 episodes"
      },
      "llama31-taxei-s123-clean": {
        "status": "completed",
        "metrics": {
          "success_rate": 0.617,
          "by_task_type": {
            "look_at_obj_in_light": 0.667,
            "pick_and_place_simple": 0.375,
            "pick_clean_then_place_in_recep": 0.455,
            "pick_cool_then_place_in_recep": 0.571,
            "pick_heat_then_place_in_recep": 0.875,
            "pick_two_obj_and_place": 0.857
          }
        }
      },
      "llama31-random-s123-clean": {
        "status": "completed",
        "metrics": {
          "success_rate": 0.766,
          "by_task_type": {
            "look_at_obj_in_light": 1.0,
            "pick_and_place_simple": 0.625,
            "pick_clean_then_place_in_recep": 0.636,
            "pick_cool_then_place_in_recep": 0.571,
            "pick_heat_then_place_in_recep": 0.875,
            "pick_two_obj_and_place": 1.0
          }
        }
      }
    },
    "gpu_status": "GPU0-2 active (16.8GB, 44-88%), GPU3 idle"
  }
}
```

</details>

---
