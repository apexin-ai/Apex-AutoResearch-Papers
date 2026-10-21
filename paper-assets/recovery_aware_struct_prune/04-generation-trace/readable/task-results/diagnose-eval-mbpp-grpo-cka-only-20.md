# diagnose eval mbpp grpo cka only 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_mbpp_grpo_cka_only_20_20260519T180955_result.json`
- **Structured JSON:** [`64945331e289abc7d108.json`](../../sessions/64/64945331e289abc7d108.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型权重在 `checkpoint-100/` 子目录（12.3GB safetensors）。实际可用模型路径是 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100/`。

```json
{"root_cause":"python: can't open file '/root/recovery_aware_struct_prune/src/eval_mbpp.py': [Errno 2] No such file or directory","error_type":"infrastructure","fix_steps":["eval_mbpp.py 存在于本地但未同步到服务器","已通过 base64 传输将 eval_mbpp.py 部署到服务器 src/ 目录","dry-run --help 验证通过","注意：模型权重在 grpo_cka_only_20/checkpoint-100/ 而非 grpo_cka_only_20/，重跑时需确认 --model_path 指向正确路径"],"can_auto_fix":true,"fixed":true,"model_path":"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "python: can't open file '/root/recovery_aware_struct_prune/src/eval_mbpp.py': [Errno 2] No such file or directory",
    "error_type": "infrastructure",
    "fix_steps": [
      "eval_mbpp.py 存在于本地但未同步到服务器",
      "已通过 base64 传输将 eval_mbpp.py 部署到服务器 src/ 目录",
      "dry-run --help 验证通过",
      "注意：模型权重在 grpo_cka_only_20/checkpoint-100/ 而非 grpo_cka_only_20/，重跑时需确认 --model_path 指向正确路径"
    ],
    "can_auto_fix": true,
    "fixed": true,
    "model_path": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100"
  }
}
```

</details>

---
