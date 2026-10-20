# diagnose full occ ln v2 s0c

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full_occ_ln_v2_s0c_20260527T004657_result.json`
- **Structured JSON:** [`7a37ed9af5e023a720fd.json`](../../sessions/7a/7a37ed9af5e023a720fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-34685 所有 4 张 GPU 都被占用，全是正常训练实验：

```json
{
  "pid_681204_cmd": "finetune.py --run_id_note detach_ln_v2_s1 --seed 43 --occ_detach true --occ_norm_type ln (cuda:0)",
  "pid_681124_cmd": "bash wrapper for detach_ln_v2_s1 (parent shell)",
  "relationship": "parent-child (681124 spawned 681204)",
  "gpu_usage": {
    "cuda:0": {"pid": 681204, "experiment": "detach_ln_v2_s1", "memory_used_gb": 60.7, "uptime": "1h13m"},
    "cuda:1": {"pid": 677648, "experiment": "detach_ln_s4", "memory_used_gb": 60.7, "uptime": "1h14m"},
    "cuda:2": {"pid": 735982, "experiment": "ablation_occ_detach_s4", "memory_used_gb": 60.7, "uptime": "30m"},
    "cuda:3": {"pid": 736344, "experiment": "mvp_occ_s4", "memory_used_gb": 61.6, "uptime": "29m"}
  },
  "all_gpus_utilization": "98-99%",
  "is_making_progress": true,
  "detach_ln_v2_s1_progress": "4594/50005 (9%), ~1.09 it/s, ETA ~11.6h",
  "recommendation": "keep all — westd-34685 全部 4 张 GPU 已满载运行合法实验，full_occ_ln_v2_s0c 无法在此服务器启动，需要等待某个实验结束或改到 westd-10894 上运行"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "pid_681204_cmd": "finetune.py --run_id_note detach_ln_v2_s1 --seed 43 --occ_detach true --occ_norm_type ln (cuda:0)",
    "pid_681124_cmd": "bash wrapper for detach_ln_v2_s1 (parent shell)",
    "relationship": "parent-child (681124 spawned 681204)",
    "gpu_usage": {
      "cuda:0": {
        "pid": 681204,
        "experiment": "detach_ln_v2_s1",
        "memory_used_gb": 60.7,
        "uptime": "1h13m"
      },
      "cuda:1": {
        "pid": 677648,
        "experiment": "detach_ln_s4",
        "memory_used_gb": 60.7,
        "uptime": "1h14m"
      },
      "cuda:2": {
        "pid": 735982,
        "experiment": "ablation_occ_detach_s4",
        "memory_used_gb": 60.7,
        "uptime": "30m"
      },
      "cuda:3": {
        "pid": 736344,
        "experiment": "mvp_occ_s4",
        "memory_used_gb": 61.6,
        "uptime": "29m"
      }
    },
    "all_gpus_utilization": "98-99%",
    "is_making_progress": true,
    "detach_ln_v2_s1_progress": "4594/50005 (9%), ~1.09 it/s, ETA ~11.6h",
    "recommendation": "keep all — westd-34685 全部 4 张 GPU 已满载运行合法实验，full_occ_ln_v2_s0c 无法在此服务器启动，需要等待某个实验结束或改到 westd-10894 上运行"
  }
}
```

</details>

---
