# diagnose westd32935 status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd32935_status_check_20260522T111802_result.json`
- **Structured JSON:** [`591e15cf40af34a79136.json`](../../sessions/59/591e15cf40af34a79136.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "server": "westd-32935",
  "timestamp": "2026-05-22 ~19:18 CST",

  "gpu_status": {
    "gpu0": {"mem_used": "0 MiB", "mem_total": "97887 MiB", "util": "0%", "status": "IDLE"},
    "gpu1": {"mem_used": "17651 MiB", "mem_total": "97887 MiB", "util": "98%", "status": "BUSY"},
    "gpu2": {"mem_used": "16261 MiB", "mem_total": "97887 MiB", "util": "92%", "status": "BUSY"},
    "gpu3": {"mem_used": "16243 MiB", "mem_total": "97887 MiB", "util": "93%", "status": "BUSY"}
  },

  "experiments": {
    "pipeline_depth_first_20": {
      "pid": 40073,
      "alive": true,
      "elapsed": "11m19s",
      "gpu": "cuda:3",
      "phase": "Phase 4 — eval_gsm8k (GRPO model)",
      "model_path": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_depth_first_20",
      "output_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_depth_first_20.json",
      "progress": "84/1319 (~6%)",
      "note": "GRPO training completed, model saved. 50-sample checkpoint showed acc=0.08 (very low — possibly warm-up samples or genuine poor perf). NOT failed."
    },

    "eval_gsm8k_sft_alpha3p0_20": {
      "pid": 37026,
      "alive": true,
      "elapsed": "47m48s",
      "gpu": "cuda:2",
      "model_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935",
      "output_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_alpha3p0_20.json",
      "progress": "450/1319 (34%)",
      "accuracy_so_far": 0.6356,
      "eos_rate": "98.44%",
      "avg_len": 196,
      "note": "⚠️ PID 37026 is running sft_rasp_alpha3p0_20, NOT grpo_random_20_seed123 as memory.md stated. NOT failed."
    },

    "eval_math500_sft_random_20_v3": {
      "pid": 5241,
      "alive": true,
      "elapsed": "432min (7h+)",
      "gpu": "cuda:1",
      "model_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20",
      "output_path": "/root/recovery_aware_struct_prune/results/eval_math500_sft_random_20_v3.json",
      "note": "Untracked long-running process. 7 hours is abnormally long for MATH-500 eval — may be stuck."
    },

    "eval_math500_grpo_standard_20_fair_2048_v2": {
      "status": "COMPLETE",
      "file": "/root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json",
      "accuracy": 0.264,
      "n_correct": 132,
      "n_total": 500,
      "natural_eos_pct": 0.556,
      "truncated_pct": 0.444,
      "avg_response_length": 1127.8
    }
  },

  "disk": {
    "root_partition": {"used": "5.2G", "total": "30G", "pct": "18%"},
    "autodl_tmp": {"used": "636G", "total": "650G", "pct": "98%", "warning": "⚠️ 数据盘几乎满"}
  },

  "action_items": [
    "PID 5241 (eval_math500 sft_random_20, cuda:1) 运行 7 小时异常——建议检查是否卡死",
    "数据盘 /root/autodl-tmp 98% 满 (仅剩 15G)——需要清理旧 checkpoint",
    "memory.md 关于 PID 37026 的记录有误：实际跑的是 sft_rasp_alpha3p0_20，不是 grpo_random_20_seed123",
    "3 个被 cron 误判 failed 的实验（depth_first pipeline, alpha3p0 eval, random_20 math500 eval）实际均在运行中"
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "server": "westd-32935",
    "timestamp": "2026-05-22 ~19:18 CST",
    "gpu_status": {
      "gpu0": {
        "mem_used": "0 MiB",
        "mem_total": "97887 MiB",
        "util": "0%",
        "status": "IDLE"
      },
      "gpu1": {
        "mem_used": "17651 MiB",
        "mem_total": "97887 MiB",
        "util": "98%",
        "status": "BUSY"
      },
      "gpu2": {
        "mem_used": "16261 MiB",
        "mem_total": "97887 MiB",
        "util": "92%",
        "status": "BUSY"
      },
      "gpu3": {
        "mem_used": "16243 MiB",
        "mem_total": "97887 MiB",
        "util": "93%",
        "status": "BUSY"
      }
    },
    "experiments": {
      "pipeline_depth_first_20": {
        "pid": 40073,
        "alive": true,
        "elapsed": "11m19s",
        "gpu": "cuda:3",
        "phase": "Phase 4 — eval_gsm8k (GRPO model)",
        "model_path": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_depth_first_20",
        "output_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_depth_first_20.json",
        "progress": "84/1319 (~6%)",
        "note": "GRPO training completed, model saved. 50-sample checkpoint showed acc=0.08 (very low — possibly warm-up samples or genuine poor perf). NOT failed."
      },
      "eval_gsm8k_sft_alpha3p0_20": {
        "pid": 37026,
        "alive": true,
        "elapsed": "47m48s",
        "gpu": "cuda:2",
        "model_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935",
        "output_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_alpha3p0_20.json",
        "progress": "450/1319 (34%)",
        "accuracy_so_far": 0.6356,
        "eos_rate": "98.44%",
        "avg_len": 196,
        "note": "⚠️ PID 37026 is running sft_rasp_alpha3p0_20, NOT grpo_random_20_seed123 as memory.md stated. NOT failed."
      },
      "eval_math500_sft_random_20_v3": {
        "pid": 5241,
        "alive": true,
        "elapsed": "432min (7h+)",
        "gpu": "cuda:1",
        "model_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20",
        "output_path": "/root/recovery_aware_struct_prune/results/eval_math500_sft_random_20_v3.json",
        "note": "Untracked long-running process. 7 hours is abnormally long for MATH-500 eval — may be stuck."
      },
      "eval_math500_grpo_standard_20_fair_2048_v2": {
        "status": "COMPLETE",
        "file": "/root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json",
        "accuracy": 0.264,
        "n_correct": 132,
        "n_total": 500,
        "natural_eos_pct": 0.556,
        "truncated_pct": 0.444,
        "avg_response_length": 1127.8
      }
    },
    "disk": {
      "root_partition": {
        "used": "5.2G",
        "total": "30G",
        "pct": "18%"
      },
      "autodl_tmp": {
        "used": "636G",
        "total": "650G",
        "pct": "98%",
        "warning": "⚠️ 数据盘几乎满"
      }
    },
    "action_items": [
      "PID 5241 (eval_math500 sft_random_20, cuda:1) 运行 7 小时异常——建议检查是否卡死",
      "数据盘 /root/autodl-tmp 98% 满 (仅剩 15G)——需要清理旧 checkpoint",
      "memory.md 关于 PID 37026 的记录有误：实际跑的是 sft_rasp_alpha3p0_20，不是 grpo_random_20_seed123",
      "3 个被 cron 误判 failed 的实验（depth_first pipeline, alpha3p0 eval, random_20 math500 eval）实际均在运行中"
    ]
  }
}
```

</details>

---
