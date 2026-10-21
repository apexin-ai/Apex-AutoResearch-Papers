# diagnose mvp vanilla s0 s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_vanilla_s0_s1_20260520T225117_result.json`
- **Structured JSON:** [`db20ac3f5ab15e76c6b1.json`](../../sessions/db/db20ac3f5ab15e76c6b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Diagnosis complete. Here's the summary:

```json
{
  "s0_status": "completed",
  "s0_last_step": 50005,
  "s0_checkpoints": ["35000_chkpt", "40000_chkpt", "45000_chkpt", "50000_chkpt"],
  "s1_status": "completed",
  "s1_last_step": 50005,
  "s1_checkpoints": ["35000_chkpt", "40000_chkpt", "45000_chkpt", "50000_chkpt"],
  "eval_running": true,
  "monitor_status": "monitor_and_eval.sh detected s0/s1 completion, launched eval on both. s0 eval (PID 232984) on GPU0 evaluating 50000_chkpt, ~40% done (Task 0 TSR=1.0/CAR=0.95, Task 3 TSR=1.0/CAR=0.5). s1 eval (PID 240384) on GPU1 evaluating 50000_chkpt, started ~5min after s0. s2 (PID 225562) still training on GPU2 at 99% util.",
  "root_cause": "False alarm. Both runs completed normally — logs show 'Max step 50005 reached! Stopping training...' and 50000_chkpt saved. EXIT_CODE=143 is from torchrun's process group cleanup: child python exits normally, torchrun sends SIGTERM during shutdown (destroy_process_group warning), resulting in 128+15=143. This is standard torchrun behavior, not an actual failure.",
  "fix_steps": ["无需修复，训练已正常完成", "Eval 已由 monitor_and_eval.sh 自动启动，等待 eval 结果即可", "如需消除 143 误报，可在 job tracker 中将 exit_code=143 且有 50000_chkpt 的任务标记为 completed"]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "s0_status": "completed",
    "s0_last_step": 50005,
    "s0_checkpoints": [
      "35000_chkpt",
      "40000_chkpt",
      "45000_chkpt",
      "50000_chkpt"
    ],
    "s1_status": "completed",
    "s1_last_step": 50005,
    "s1_checkpoints": [
      "35000_chkpt",
      "40000_chkpt",
      "45000_chkpt",
      "50000_chkpt"
    ],
    "eval_running": true,
    "monitor_status": "monitor_and_eval.sh detected s0/s1 completion, launched eval on both. s0 eval (PID 232984) on GPU0 evaluating 50000_chkpt, ~40% done (Task 0 TSR=1.0/CAR=0.95, Task 3 TSR=1.0/CAR=0.5). s1 eval (PID 240384) on GPU1 evaluating 50000_chkpt, started ~5min after s0. s2 (PID 225562) still training on GPU2 at 99% util.",
    "root_cause": "False alarm. Both runs completed normally — logs show 'Max step 50005 reached! Stopping training...' and 50000_chkpt saved. EXIT_CODE=143 is from torchrun's process group cleanup: child python exits normally, torchrun sends SIGTERM during shutdown (destroy_process_group warning), resulting in 128+15=143. This is standard torchrun behavior, not an actual failure.",
    "fix_steps": [
      "无需修复，训练已正常完成",
      "Eval 已由 monitor_and_eval.sh 自动启动，等待 eval 结果即可",
      "如需消除 143 误报，可在 job tracker 中将 exit_code=143 且有 50000_chkpt 的任务标记为 completed"
    ]
  }
}
```

</details>

---
