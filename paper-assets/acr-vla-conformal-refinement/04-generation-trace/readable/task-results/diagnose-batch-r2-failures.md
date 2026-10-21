# diagnose batch r2 failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_batch-r2-failures_20260519T162210_result.json`
- **Structured JSON:** [`6e727bfb900a7ac8509e.json`](../../sessions/6e/6e727bfb900a7ac8509e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。所有 6 个 r2 实验**实际上都成功完成了**，不是真正的失败。

```json
{
  "root_cause": "所有 r2 实验均正常运行完毕并产出了 JSON 结果文件，但因通过 tmux 直接启动（非 submit_training_job），没有写 sentinel 文件，导致 cron 监控系统无法检测到完成状态。进程退出后被 registry 误判为 failed/dead。",
  "error_type": "infrastructure",
  "affected_experiments": [
    "eval-random-selection-object-k5-seed42-r2",
    "eval-random-selection-object-k5-seed44-r2",
    "eval-random-selection-object-k5-seed45-r2",
    "eval-random-selection-object-k5-seed43-r2",
    "eval-obs-only-spatial-norm02-k5-seed44-r2",
    "eval-obs-only-spatial-norm02-k5-seed45-r2"
  ],
  "original_processes_alive": false,
  "r2_actually_completed": true,
  "json_outputs_exist": {
    "seed42 (object, bjb1)": true,
    "seed44 (object, bjb1)": true,
    "seed45 (object, bjb1)": true,
    "seed43 (object, bjb2)": true,
    "seed44 (spatial, bjb2)": true,
    "seed45 (spatial, bjb2)": true
  },
  "results_summary": {
    "eval-random-selection-object-k5-seed42-r2": "14.0% (14/100)",
    "eval-random-selection-object-k5-seed44-r2": "10.0% (10/100)",
    "eval-random-selection-object-k5-seed45-r2": "7.0% (7/100)",
    "eval-random-selection-object-k5-seed43-r2": "11.0% (11/100)",
    "eval-obs-only-spatial-norm02-k5-seed44-r2": "37.0% (37/100)",
    "eval-obs-only-spatial-norm02-k5-seed45-r2": "34.0% (34/100)"
  },
  "json_timestamps": {
    "seed42": "May 19 23:45",
    "seed44 (object)": "May 19 23:50",
    "seed45 (object)": "May 19 23:57",
    "seed43": "May 20 00:03",
    "seed44 (spatial)": "May 19 23:45",
    "seed45 (spatial)": "May 19 23:49"
  },
  "gpu_status": {
    "bjb1-32546": "GPU0,2-5 idle (2 MiB); GPU1 active (3132 MiB) — running eval-obs-only-spatial-norm02-seed47",
    "bjb2-28827": "GPU0,4,5 idle; GPU1 (1906 MiB, argmin-object-k5-seed44), GPU2 (1906 MiB, random-seed46), GPU3 (3660 MiB, obs-only-spatial-norm02-seed46) active"
  },
  "active_experiments": {
    "bjb1-32546": ["eval-obs-only-spatial-norm02-seed47 (GPU 1)"],
    "bjb2-28827": ["eval-random-seed46 (GPU 2)", "eval-argmin-object-k5-seed44 (GPU 1)", "eval-obs-only-spatial-norm02-seed46 (GPU 3)"]
  },
  "fix_recommendation": "将这 6 个实验的 registry 状态从 failed/RUNNING 更新为 completed。JSON 结果文件已存在，可直接采集。无需重试。根因是 tmux 直接启动的实验绕过了 sentinel 文件机制，建议后续统一通过 submit_training_job 启动以确保监控覆盖。"
}
```

**核心结论**：没有 GPU 冲突，没有 OOM，没有启动失败。6 个 r2 实验全部正常跑完，只是监控系统的盲区——tmux 启动的实验不写 sentinel，cron 检测不到完成状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "所有 r2 实验均正常运行完毕并产出了 JSON 结果文件，但因通过 tmux 直接启动（非 submit_training_job），没有写 sentinel 文件，导致 cron 监控系统无法检测到完成状态。进程退出后被 registry 误判为 failed/dead。",
    "error_type": "infrastructure",
    "affected_experiments": [
      "eval-random-selection-object-k5-seed42-r2",
      "eval-random-selection-object-k5-seed44-r2",
      "eval-random-selection-object-k5-seed45-r2",
      "eval-random-selection-object-k5-seed43-r2",
      "eval-obs-only-spatial-norm02-k5-seed44-r2",
      "eval-obs-only-spatial-norm02-k5-seed45-r2"
    ],
    "original_processes_alive": false,
    "r2_actually_completed": true,
    "json_outputs_exist": {
      "seed42 (object, bjb1)": true,
      "seed44 (object, bjb1)": true,
      "seed45 (object, bjb1)": true,
      "seed43 (object, bjb2)": true,
      "seed44 (spatial, bjb2)": true,
      "seed45 (spatial, bjb2)": true
    },
    "results_summary": {
      "eval-random-selection-object-k5-seed42-r2": "14.0% (14/100)",
      "eval-random-selection-object-k5-seed44-r2": "10.0% (10/100)",
      "eval-random-selection-object-k5-seed45-r2": "7.0% (7/100)",
      "eval-random-selection-object-k5-seed43-r2": "11.0% (11/100)",
      "eval-obs-only-spatial-norm02-k5-seed44-r2": "37.0% (37/100)",
      "eval-obs-only-spatial-norm02-k5-seed45-r2": "34.0% (34/100)"
    },
    "json_timestamps": {
      "seed42": "May 19 23:45",
      "seed44 (object)": "May 19 23:50",
      "seed45 (object)": "May 19 23:57",
      "seed43": "May 20 00:03",
      "seed44 (spatial)": "May 19 23:45",
      "seed45 (spatial)": "May 19 23:49"
    },
    "gpu_status": {
      "bjb1-32546": "GPU0,2-5 idle (2 MiB); GPU1 active (3132 MiB) — running eval-obs-only-spatial-norm02-seed47",
      "bjb2-28827": "GPU0,4,5 idle; GPU1 (1906 MiB, argmin-object-k5-seed44), GPU2 (1906 MiB, random-seed46), GPU3 (3660 MiB, obs-only-spatial-norm02-seed46) active"
    },
    "active_experiments": {
      "bjb1-32546": [
        "eval-obs-only-spatial-norm02-seed47 (GPU 1)"
      ],
      "bjb2-28827": [
        "eval-random-seed46 (GPU 2)",
        "eval-argmin-object-k5-seed44 (GPU 1)",
        "eval-obs-only-spatial-norm02-seed46 (GPU 3)"
      ]
    },
    "fix_recommendation": "将这 6 个实验的 registry 状态从 failed/RUNNING 更新为 completed。JSON 结果文件已存在，可直接采集。无需重试。根因是 tmux 直接启动的实验绕过了 sentinel 文件机制，建议后续统一通过 submit_training_job 启动以确保监控覆盖。"
  }
}
```

</details>

---
