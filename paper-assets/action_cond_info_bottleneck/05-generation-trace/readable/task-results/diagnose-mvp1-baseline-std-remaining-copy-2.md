# diagnose mvp1 baseline std remaining

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp1_baseline_std_remaining_20260515T234823_result.json`
- **Structured JSON:** [`a9b73e049683620b47c5.json`](../../sessions/a9/a9b73e049683620b47c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

```json
{"root_cause":"进程在 libero_goal 评测中途被外部 kill（日志在 rollout step 126/300 处截断，无 Traceback/OOM/Error，无 dmesg 权限确认），Stepping through eval batches: 54% (27/50) running_success_rate=77.8%","error_type":"infrastructure","fix_steps":["重新运行仅剩余 suites: bash /root/acib/scripts/run_remaining_suites_eval.sh lerobot/smolvla_libero 1 'libero_goal libero_10' /root/acib/outputs/baseline_std_v3","运行前删除不完整的 libero_goal 目录: rm -rf /root/acib/outputs/baseline_std_v3/libero_goal"],"can_auto_fix":true,"partial_results":{"suites_completed":["libero_spatial","libero_object"],"suites_missing":["libero_goal","libero_10"],"metrics":{"libero_spatial":"66.0%","libero_object":"67.8%"}}}
```

**摘要**:
- **libero_spatial**: 完成，Avg SR=66.0%（与 mvp1_baseline_std 一致）
- **libero_object**: 完成，Avg SR=67.8%，per-task=[62,58,56,56,86,52,82,64,80,82]
- **libero_goal**: 评测到 ~54% (27/50 batches) 时进程被 kill，仅 task_0 有视频，无 eval_info.json
- **libero_10**: 未开始
- **根因**: 外部 kill，日志无任何错误信息，纯截断。根分区 82% 用量不足以触发 OOM killer（且无 dmesg 权限验证）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "进程在 libero_goal 评测中途被外部 kill（日志在 rollout step 126/300 处截断，无 Traceback/OOM/Error，无 dmesg 权限确认），Stepping through eval batches: 54% (27/50) running_success_rate=77.8%",
    "error_type": "infrastructure",
    "fix_steps": [
      "重新运行仅剩余 suites: bash /root/acib/scripts/run_remaining_suites_eval.sh lerobot/smolvla_libero 1 'libero_goal libero_10' /root/acib/outputs/baseline_std_v3",
      "运行前删除不完整的 libero_goal 目录: rm -rf /root/acib/outputs/baseline_std_v3/libero_goal"
    ],
    "can_auto_fix": true,
    "partial_results": {
      "suites_completed": [
        "libero_spatial",
        "libero_object"
      ],
      "suites_missing": [
        "libero_goal",
        "libero_10"
      ],
      "metrics": {
        "libero_spatial": "66.0%",
        "libero_object": "67.8%"
      }
    }
  }
}
```

</details>

---
