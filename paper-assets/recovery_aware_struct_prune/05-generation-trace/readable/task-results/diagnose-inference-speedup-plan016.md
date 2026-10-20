# diagnose inference speedup plan016

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_inference_speedup_plan016_20260516T214950_result.json`
- **Structured JSON:** [`2c3b499b2f00abe2c363.json`](../../sessions/2c/2c3b499b2f00abe2c363.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被删除或从未创建）。无影响。

```json
{
  "root_cause": "剪枝模型 sft_rasp_20 的 checkpoint 权重形状与 Qwen2ForCausalLM 原始结构不匹配（MLP up/down/gate_proj 维度不一致），from_pretrained 因 ignore_mismatched_sizes=False 抛出 RuntimeError",
  "status": "failed",
  "metrics": {
    "dense_baseline": {
      "total_time_sec": 335.15,
      "total_tokens": 25477,
      "tokens_per_second": 76.02,
      "avg_latency_per_prompt_sec": 6.703,
      "peak_memory_gb": 16.22,
      "model_path": "/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B"
    }
  },
  "error_message": "RuntimeError: ignore_mismatched_sizes=False — sft_rasp_20 checkpoint 的 MLP 权重维度 (up_proj: [8128,3584], gate_proj: [11508,3584], down_proj: [3584,9480]) 与模型期望的 [18944,3584] 不匹配。剪枝模型需要用匹配的 config.json（intermediate_size 已修改）加载，或设置 ignore_mismatched_sizes=True 并自定义加载逻辑"
}
```

**根因**：`benchmark_inference.py` 用标准 `AutoModelForCausalLM.from_pretrained` 加载剪枝后的模型，但剪枝模型的 `config.json` 仍保留原始 `intermediate_size=18944`，而实际权重已被结构化剪枝缩小。需要在保存剪枝模型时同步更新 `config.json` 中的维度信息，或在 benchmark 脚本中使用项目自定义的加载方式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "剪枝模型 sft_rasp_20 的 checkpoint 权重形状与 Qwen2ForCausalLM 原始结构不匹配（MLP up/down/gate_proj 维度不一致），from_pretrained 因 ignore_mismatched_sizes=False 抛出 RuntimeError",
    "status": "failed",
    "metrics": {
      "dense_baseline": {
        "total_time_sec": 335.15,
        "total_tokens": 25477,
        "tokens_per_second": 76.02,
        "avg_latency_per_prompt_sec": 6.703,
        "peak_memory_gb": 16.22,
        "model_path": "/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B"
      }
    },
    "error_message": "RuntimeError: ignore_mismatched_sizes=False — sft_rasp_20 checkpoint 的 MLP 权重维度 (up_proj: [8128,3584], gate_proj: [11508,3584], down_proj: [3584,9480]) 与模型期望的 [18944,3584] 不匹配。剪枝模型需要用匹配的 config.json（intermediate_size 已修改）加载，或设置 ignore_mismatched_sizes=True 并自定义加载逻辑"
  }
}
```

</details>

---
