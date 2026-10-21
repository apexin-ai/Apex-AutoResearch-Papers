# diagnose eval humaneval grpo rasp 20 fair 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_humaneval_grpo_rasp_20_fair_2048_20260519T094259_result.json`
- **Structured JSON:** [`6abbe4f0869713d5f9fd.json`](../../sessions/6a/6abbe4f0869713d5f9fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认无 wandb 引用。

```json
{"root_cause":"实验实际已成功完成（pass@1=0.1098, 18/164, 耗时2h53m）。Cron 误报失败原因：eval_humaneval.py 不含任何 W&B logging 代码，进程正常退出后 Cron 框架检测不到 W&B metrics，将其判定为 'Process exited without valid W&B metrics'。结果已保存至 JSON 文件。","error_type":"infrastructure","fix_steps":["无需修复——实验已成功，结果在 /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json","如需 Cron 正确识别完成状态，在 eval_humaneval.py 末尾添加 wandb.log() 或调整 Cron 的成功判定逻辑（如检查 JSON 输出文件而非 W&B metrics）"],"can_auto_fix":true,"log_path":"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.log"}
```

附加发现：median_response_length=2048.0（即多数生成触达 max_new_tokens 上限），avg=1321 tokens。模型倾向于不终止生成，可能影响代码质量（大量 SyntaxError），pass@1 仅 10.98%。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "实验实际已成功完成（pass@1=0.1098, 18/164, 耗时2h53m）。Cron 误报失败原因：eval_humaneval.py 不含任何 W&B logging 代码，进程正常退出后 Cron 框架检测不到 W&B metrics，将其判定为 'Process exited without valid W&B metrics'。结果已保存至 JSON 文件。",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复——实验已成功，结果在 /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json",
      "如需 Cron 正确识别完成状态，在 eval_humaneval.py 末尾添加 wandb.log() 或调整 Cron 的成功判定逻辑（如检查 JSON 输出文件而非 W&B metrics）"
    ],
    "can_auto_fix": true,
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.log"
  }
}
```

</details>

---
