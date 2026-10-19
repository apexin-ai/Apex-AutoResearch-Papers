# diagnose spon supp eval retry

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_spon_supp_eval_retry_20260515T200321_result.json`
- **Structured JSON:** [`e2ddbc0aa1e3139af3e2.json`](../../sessions/e2/e2ddbc0aa1e3139af3e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：`eval_spon_supplementary.py` 在 May 16 03:44 被更新，新增了 `--predictor_checkpoint` 参数（`required=True`），但 cron 运行命令未包含此参数。每次重试 argparse 立即报错退出，错误信息写入 stderr（不在 stdout log 中）。

日志中的内容是旧版脚本（使用 "vanilla TEAL"）的残留输出，不是当前版本的运行结果。旧版本本身在 step [4/5] 也未完成（可能被手动终止后触发了脚本重写）。

`spon_2048_s42/` 目录只有 `spon_biases.pt`，没有 predictor checkpoint。可用的 predictor 在其他目录，如 `checkpoints/predictor_kl.pt`、`checkpoints/mvp_kl_s42/predictor_kl.pt` 等。

```json
{"root_cause":"argparse: error: the following arguments are required: --predictor_checkpoint (脚本 May 16 03:44 更新增加了 required=True 的 --predictor_checkpoint 参数，但运行命令未提供)","error_type":"infrastructure","fix_steps":["确定正确的 predictor checkpoint（如 checkpoints/predictor_kl.pt 或 checkpoints/mvp_kl_s42/predictor_kl.pt）","在运行命令中添加 --predictor_checkpoint &lt;path>","更新 cron 监控的启动命令"],"can_auto_fix":false}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "argparse: error: the following arguments are required: --predictor_checkpoint (脚本 May 16 03:44 更新增加了 required=True 的 --predictor_checkpoint 参数，但运行命令未提供)",
    "error_type": "infrastructure",
    "fix_steps": [
      "确定正确的 predictor checkpoint（如 checkpoints/predictor_kl.pt 或 checkpoints/mvp_kl_s42/predictor_kl.pt）",
      "在运行命令中添加 --predictor_checkpoint &lt;path>",
      "更新 cron 监控的启动命令"
    ],
    "can_auto_fix": false
  }
}
```

</details>

---
