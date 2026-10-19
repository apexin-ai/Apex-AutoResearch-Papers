# diagnose lm eval mistral kl 50pct

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_lm_eval_mistral_kl_50pct_20260516T041602_result.json`
- **Structured JSON:** [`422c73d4bd92f12869b7.json`](../../sessions/42/422c73d4bd92f12869b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**没有失败**，已正常完成并输出全部结果。

```json
{"root_cause":"无失败——进程正常退出(rc=0)，所有 task 结果已写入 results/lm_eval_mistral_kl_50pct/。Cron 误判原因：脚本无 sentinel 文件和 W&B 集成，进程退出后 Cron 5次探测 PID 已死即标记 failed","error_type":"infrastructure","fix_steps":["无需修复，实验已成功完成","若要避免 Cron 误报，在 lm_eval_sparse.py 结束时写一个 sentinel 文件(如 touch results/lm_eval_mistral_kl_50pct/.done)"],"can_auto_fix":true,"partial_results":"有完整结果：arc_challenge acc=0.293 acc_norm=0.318, winogrande acc=0.629, mmlu acc=0.230, gsm8k exact_match=0.005/0.021"}
```

注意：MMLU 0.23（接近随机水平）和 GSM8K 0.005 偏低，可能是 50% sparsity 下 predictor 质量问题，但这属于实验结论而非运行故障。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "无失败——进程正常退出(rc=0)，所有 task 结果已写入 results/lm_eval_mistral_kl_50pct/。Cron 误判原因：脚本无 sentinel 文件和 W&B 集成，进程退出后 Cron 5次探测 PID 已死即标记 failed",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复，实验已成功完成",
      "若要避免 Cron 误报，在 lm_eval_sparse.py 结束时写一个 sentinel 文件(如 touch results/lm_eval_mistral_kl_50pct/.done)"
    ],
    "can_auto_fix": true,
    "partial_results": "有完整结果：arc_challenge acc=0.293 acc_norm=0.318, winogrande acc=0.629, mmlu acc=0.230, gsm8k exact_match=0.005/0.021"
  }
}
```

</details>

---
