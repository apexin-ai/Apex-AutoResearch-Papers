# ops gpu status loop7

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_loop7_20260514T200623_result.json`
- **Structured JSON:** [`b6ff8ea327c9e55cb014.json`](../../sessions/b6/b6ff8ea327c9e55cb014.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "gpu_status": [
    {"gpu": 0, "memory_used_mb": 17731, "memory_total_mb": 24564, "utilization_pct": 53, "processes": [{"pid": 430416, "memory_mb": 17722, "cmd": "python compute_signals.py --model-path .../Qwen2.5-1.5B_d000_s42/lora_adapter --benchmark mmlu --signals embedding minkpp selfcritique"}]},
    {"gpu": 1, "memory_used_mb": 0, "memory_total_mb": 24564, "utilization_pct": 0, "processes": []},
    {"gpu": 2, "memory_used_mb": 0, "memory_total_mb": 24564, "utilization_pct": 0, "processes": []},
    {"gpu": 3, "memory_used_mb": 13341, "memory_total_mb": 24564, "utilization_pct": 44, "processes": [{"pid": 420195, "memory_mb": 13332, "cmd": "python train_sft.py --model-name Qwen2.5-3B --data-path sft_dosage_100.jsonl --output-dir Qwen2.5-3B_d100_s42 --gpu 3 --batch-size 1 --grad-accum 16"}]},
    {"gpu": 4, "memory_used_mb": 5857, "memory_total_mb": 24564, "utilization_pct": 55, "processes": [{"pid": 420910, "memory_mb": 5848, "cmd": "python evaluate.py --model-path Qwen2.5-1.5B --adapter-path Qwen2.5-1.5B_d025_s42/lora_adapter --output-dir eval_results/Qwen2.5-1.5B_d025_s42_aligned --mc-format aligned"}]},
    {"gpu": 5, "memory_used_mb": 0, "memory_total_mb": 24564, "utilization_pct": 0, "processes": []}
  ],
  "pid_check": {
    "430406": "alive (exp002-signals-1p5B wrapper → child 430416 on GPU 0)",
    "426813": "dead",
    "426474": "dead",
    "422128": "dead",
    "420905": "alive (exp_001_eval_15B_d025_aligned wrapper → child 420910 on GPU 4)",
    "405515": "dead",
    "406017": "dead",
    "398501": "dead"
  },
  "zombie_pids": [],
  "other_notable": {
    "318413": "alive (exp_001_eval_05B_raw wrapper on GPU 1, but NO gpu process — likely finished, shell still waiting)"
  },
  "cuda3_check": "PID 420195 active — train_sft.py Qwen2.5-3B d100_s42, 13332 MiB",
  "summary": "3 GPUs active: GPU 0 (exp002 compute_signals 1.5B), GPU 3 (SFT training 3B d100), GPU 4 (eval 1.5B d025 aligned). GPUs 1/2/5 idle. Note: exp002 wrapper claims CUDA_VISIBLE_DEVICES=2 but compute_signals.py --gpu 0 overrides to physical GPU 0 — GPU 2 is actually free. PID 318413 (eval_05B_raw) wrapper still alive on GPU 1 but no GPU process running."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "gpu_status": [
      {
        "gpu": 0,
        "memory_used_mb": 17731,
        "memory_total_mb": 24564,
        "utilization_pct": 53,
        "processes": [
          {
            "pid": 430416,
            "memory_mb": 17722,
            "cmd": "python compute_signals.py --model-path .../Qwen2.5-1.5B_d000_s42/lora_adapter --benchmark mmlu --signals embedding minkpp selfcritique"
          }
        ]
      },
      {
        "gpu": 1,
        "memory_used_mb": 0,
        "memory_total_mb": 24564,
        "utilization_pct": 0,
        "processes": []
      },
      {
        "gpu": 2,
        "memory_used_mb": 0,
        "memory_total_mb": 24564,
        "utilization_pct": 0,
        "processes": []
      },
      {
        "gpu": 3,
        "memory_used_mb": 13341,
        "memory_total_mb": 24564,
        "utilization_pct": 44,
        "processes": [
          {
            "pid": 420195,
            "memory_mb": 13332,
            "cmd": "python train_sft.py --model-name Qwen2.5-3B --data-path sft_dosage_100.jsonl --output-dir Qwen2.5-3B_d100_s42 --gpu 3 --batch-size 1 --grad-accum 16"
          }
        ]
      },
      {
        "gpu": 4,
        "memory_used_mb": 5857,
        "memory_total_mb": 24564,
        "utilization_pct": 55,
        "processes": [
          {
            "pid": 420910,
            "memory_mb": 5848,
            "cmd": "python evaluate.py --model-path Qwen2.5-1.5B --adapter-path Qwen2.5-1.5B_d025_s42/lora_adapter --output-dir eval_results/Qwen2.5-1.5B_d025_s42_aligned --mc-format aligned"
          }
        ]
      },
      {
        "gpu": 5,
        "memory_used_mb": 0,
        "memory_total_mb": 24564,
        "utilization_pct": 0,
        "processes": []
      }
    ],
    "pid_check": {
      "430406": "alive (exp002-signals-1p5B wrapper → child 430416 on GPU 0)",
      "426813": "dead",
      "426474": "dead",
      "422128": "dead",
      "420905": "alive (exp_001_eval_15B_d025_aligned wrapper → child 420910 on GPU 4)",
      "405515": "dead",
      "406017": "dead",
      "398501": "dead"
    },
    "zombie_pids": [],
    "other_notable": {
      "318413": "alive (exp_001_eval_05B_raw wrapper on GPU 1, but NO gpu process — likely finished, shell still waiting)"
    },
    "cuda3_check": "PID 420195 active — train_sft.py Qwen2.5-3B d100_s42, 13332 MiB",
    "summary": "3 GPUs active: GPU 0 (exp002 compute_signals 1.5B), GPU 3 (SFT training 3B d100), GPU 4 (eval 1.5B d025 aligned). GPUs 1/2/5 idle. Note: exp002 wrapper claims CUDA_VISIBLE_DEVICES=2 but compute_signals.py --gpu 0 overrides to physical GPU 0 — GPU 2 is actually free. PID 318413 (eval_05B_raw) wrapper still alive on GPU 1 but no GPU process running."
  }
}
```

</details>

---
