# diagnose llama3b adaptive seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama3b_adaptive_seed42_20260517T140045_result.json`
- **Structured JSON:** [`1916c6d9265c3f624166.json`](../../sessions/19/1916c6d9265c3f624166.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

```json
{
  "training_completed": true,
  "root_cause": "run script 设置了 WANDB_MODE=offline，W&B 数据只保存在本地（/root/provenance_weight_training/wandb/），未同步到云端。同时脚本没有重定向日志到 /root/runs/，也没有写 sentinel 文件。Cron 监控依赖 W&B 云端 run 和 sentinel 文件来判定状态，两者都不存在，因此误判为 failed。",
  "actual_metrics": {
    "eval_ppl": 10.580212712678067,
    "eval_loss": 2.3589855313961063,
    "eval_num_tokens": 4017316,
    "eval_elapsed_seconds": 223.6,
    "total_steps": 6103
  },
  "checkpoint_path": "/root/provenance_weight_training/output/models/llama3b_adaptive_seed42/final",
  "log_path": "无独立日志文件（stdout 输出到终端，未重定向）",
  "error_type": "monitoring_gap",
  "fix_steps": [
    "将 registry 中 llama3b_adaptive_seed42 状态从 failed 更新为 completed",
    "后续 run script 改用 WANDB_MODE=online 或添加 sentinel 文件写入（如 touch $OUTPUT_DIR/.done）",
    "run script 添加日志重定向：2>&1 | tee /root/runs/provenance_weight_training/llama3b_adaptive_seed42.log",
    "W&B offline 数据可通过 wandb sync 上传到云端补录"
  ]
}
```

**总结**：训练正常完成（6103 steps，eval PPL=10.58），与 memory.md 记录一致。失败判定是监控误报——`WANDB_MODE=offline` + 无 sentinel + 无日志重定向导致 cron 无法检测到运行状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "training_completed": true,
    "root_cause": "run script 设置了 WANDB_MODE=offline，W&B 数据只保存在本地（/root/provenance_weight_training/wandb/），未同步到云端。同时脚本没有重定向日志到 /root/runs/，也没有写 sentinel 文件。Cron 监控依赖 W&B 云端 run 和 sentinel 文件来判定状态，两者都不存在，因此误判为 failed。",
    "actual_metrics": {
      "eval_ppl": 10.580212712678067,
      "eval_loss": 2.3589855313961063,
      "eval_num_tokens": 4017316,
      "eval_elapsed_seconds": 223.6,
      "total_steps": 6103
    },
    "checkpoint_path": "/root/provenance_weight_training/output/models/llama3b_adaptive_seed42/final",
    "log_path": "无独立日志文件（stdout 输出到终端，未重定向）",
    "error_type": "monitoring_gap",
    "fix_steps": [
      "将 registry 中 llama3b_adaptive_seed42 状态从 failed 更新为 completed",
      "后续 run script 改用 WANDB_MODE=online 或添加 sentinel 文件写入（如 touch $OUTPUT_DIR/.done）",
      "run script 添加日志重定向：2>&1 | tee /root/runs/provenance_weight_training/llama3b_adaptive_seed42.log",
      "W&B offline 数据可通过 wandb sync 上传到云端补录"
    ]
  }
}
```

</details>

---
