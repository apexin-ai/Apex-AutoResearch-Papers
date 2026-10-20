# diagnose cls8b deepseek eval fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cls8b-deepseek-eval-fix_20260519T231845_result.json`
- **Structured JSON:** [`921b812c9f0813f95c10.json`](../../sessions/92/921b812c9f0813f95c10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

```json
{"cls8b_ckpt_path": "/root/autodl-tmp/checkpoints_repo_cls_8b_s456_v2/checkpoint-2200", "deepseek_ckpt_path": "/root/autodl-tmp/checkpoints_deepseek_cls_repo_s456_v2/checkpoint-2163", "free_gpus": [0, 3], "eval_output_arg": "--output", "notes": "两个 checkpoint 均完整存在(adapter_model.safetensors + optimizer 等)。CLS8B 有 5 个 checkpoint(600/1600/1800/2000/2200)，DeepSeek 仅 1 个(2163)。GPU1 utilization=100% 但显存 0MiB(异常态)，GPU2 占用 29.6/32.6GB。GPU0 和 GPU3 完全空闲可用。eval 脚本参数确认是 --output 不是 --output_dir。"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "cls8b_ckpt_path": "/root/autodl-tmp/checkpoints_repo_cls_8b_s456_v2/checkpoint-2200",
    "deepseek_ckpt_path": "/root/autodl-tmp/checkpoints_deepseek_cls_repo_s456_v2/checkpoint-2163",
    "free_gpus": [
      0,
      3
    ],
    "eval_output_arg": "--output",
    "notes": "两个 checkpoint 均完整存在(adapter_model.safetensors + optimizer 等)。CLS8B 有 5 个 checkpoint(600/1600/1800/2000/2200)，DeepSeek 仅 1 个(2163)。GPU1 utilization=100% 但显存 0MiB(异常态)，GPU2 占用 29.6/32.6GB。GPU0 和 GPU3 完全空闲可用。eval 脚本参数确认是 --output 不是 --output_dir。"
  }
}
```

</details>

---
