# diagnose exp 001 sft d025 15B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_d025_15B_20260514T174905_result.json`
- **Structured JSON:** [`3cb7a69163d8cc43b546.json`](../../sessions/3c/3cb7a69163d8cc43b546.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**CRON FALSE POSITIVE — 训练已成功完成。**

日志证据：
- 最终 step 3384/3384，epoch 1.0
- `train_runtime: 11610.65s`（~3.2h），`train_loss: 1.2715`
- checkpoint-3384 + 最终 lora_adapter 均已保存（May 15 01:32）
- 无任何 OOM/CUDA error/NaN/Traceback

Cron 在 ~17:47 UTC 检测到 wrapper PID 已死并连续 5 次未发现 sentinel/W&B，误判为 failed。实际上训练进程已在 ~01:32 正常退出，只是没有写 sentinel 文件。

```json
{"root_cause":"Cron monitored wrapper PID which exited after training completed normally. No sentinel/W&B was configured, so 5 consecutive checks all returned negative → auto-resolved as failed. Training actually completed successfully: 3384/3384 steps, train_loss=1.2715, lora_adapter saved at checkpoint-3384.","error_type":"cron_false_positive","fix_steps":["将实验状态从 failed 改为 completed","后续 train_sft.py 结束后写 sentinel 文件（如 DONE 标记），避免 cron 误判"],"can_auto_fix":true,"is_still_running":false,"current_pid":null,"training_progress":"3384/3384 (100%, completed)"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "Cron monitored wrapper PID which exited after training completed normally. No sentinel/W&B was configured, so 5 consecutive checks all returned negative → auto-resolved as failed. Training actually completed successfully: 3384/3384 steps, train_loss=1.2715, lora_adapter saved at checkpoint-3384.",
    "error_type": "cron_false_positive",
    "fix_steps": [
      "将实验状态从 failed 改为 completed",
      "后续 train_sft.py 结束后写 sentinel 文件（如 DONE 标记），避免 cron 误判"
    ],
    "can_auto_fix": true,
    "is_still_running": false,
    "current_pid": null,
    "training_progress": "3384/3384 (100%, completed)"
  }
}
```

</details>

---
