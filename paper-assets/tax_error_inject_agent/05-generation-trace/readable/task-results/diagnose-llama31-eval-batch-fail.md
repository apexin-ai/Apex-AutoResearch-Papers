# diagnose llama31 eval batch fail

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama31-eval-batch-fail_20260516T152114_result.json`
- **Structured JSON:** [`4119bf3f55c503c4c626.json`](../../sessions/41/4119bf3f55c503c4c626.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。结论如下：

```json
{
  "llama31-taxei-s123-eval": {
    "actually_completed": false,
    "metrics": null,
    "root_cause": "cron false positive — 进程当前正在运行中 (PID 293496, 已完成 35/47 episodes, CUDA:0)，系被手动重新启动。原始 run 可能确实死过（cron 正确检测到进程消失），后被重新拉起。",
    "output_file": null,
    "note": "输出将写入 eval_results/llama31_taxei_s123_injected.json，预计 ~5-7 分钟完成"
  },
  "llama31-taxei-s123-clean": {
    "actually_completed": true,
    "metrics": {
      "success_rate": 0.617,
      "by_task_type": {
        "look_at_obj_in_light": {"total": 6, "success": 4, "rate": 0.667},
        "pick_and_place_simple": {"total": 8, "success": 3, "rate": 0.375},
        "pick_clean_then_place_in_recep": {"total": 11, "success": 5, "rate": 0.455},
        "pick_cool_then_place_in_recep": {"total": 7, "success": 4, "rate": 0.571},
        "pick_heat_then_place_in_recep": {"total": 8, "success": 7, "rate": 0.875},
        "pick_two_obj_and_place": {"total": 7, "success": 6, "rate": 0.857}
      }
    },
    "root_cause": "cron false positive — eval 正常完成但不写 sentinel/W&B，cron 无法确认完成状态",
    "output_file": "/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_taxei_s123_clean.json"
  },
  "llama31-random-s123-clean": {
    "actually_completed": true,
    "metrics": {
      "success_rate": 0.766,
      "by_task_type": {
        "look_at_obj_in_light": {"total": 6, "success": 6, "rate": 1.0},
        "pick_and_place_simple": {"total": 8, "success": 5, "rate": 0.625},
        "pick_clean_then_place_in_recep": {"total": 11, "success": 7, "rate": 0.636},
        "pick_cool_then_place_in_recep": {"total": 7, "success": 4, "rate": 0.571},
        "pick_heat_then_place_in_recep": {"total": 8, "success": 7, "rate": 0.875},
        "pick_two_obj_and_place": {"total": 7, "success": 7, "rate": 1.0}
      }
    },
    "root_cause": "cron false positive — eval 正常完成但不写 sentinel/W&B，cron 无法确认完成状态",
    "output_file": "/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_random_s123_clean.json"
  }
}
```

**额外发现**: 服务器上还有一个 `llama31_random_s123_injected` eval 在排队运行（PID 294869, 已完成 21/47 episodes, CUDA:1），是等 vanilla 完成后自动启动的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "llama31-taxei-s123-eval": {
      "actually_completed": false,
      "metrics": null,
      "root_cause": "cron false positive — 进程当前正在运行中 (PID 293496, 已完成 35/47 episodes, CUDA:0)，系被手动重新启动。原始 run 可能确实死过（cron 正确检测到进程消失），后被重新拉起。",
      "output_file": null,
      "note": "输出将写入 eval_results/llama31_taxei_s123_injected.json，预计 ~5-7 分钟完成"
    },
    "llama31-taxei-s123-clean": {
      "actually_completed": true,
      "metrics": {
        "success_rate": 0.617,
        "by_task_type": {
          "look_at_obj_in_light": {
            "total": 6,
            "success": 4,
            "rate": 0.667
          },
          "pick_and_place_simple": {
            "total": 8,
            "success": 3,
            "rate": 0.375
          },
          "pick_clean_then_place_in_recep": {
            "total": 11,
            "success": 5,
            "rate": 0.455
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
            "success": 6,
            "rate": 0.857
          }
        }
      },
      "root_cause": "cron false positive — eval 正常完成但不写 sentinel/W&B，cron 无法确认完成状态",
      "output_file": "/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_taxei_s123_clean.json"
    },
    "llama31-random-s123-clean": {
      "actually_completed": true,
      "metrics": {
        "success_rate": 0.766,
        "by_task_type": {
          "look_at_obj_in_light": {
            "total": 6,
            "success": 6,
            "rate": 1.0
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
            "success": 7,
            "rate": 1.0
          }
        }
      },
      "root_cause": "cron false positive — eval 正常完成但不写 sentinel/W&B，cron 无法确认完成状态",
      "output_file": "/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_random_s123_clean.json"
    }
  }
}
```

</details>

---
