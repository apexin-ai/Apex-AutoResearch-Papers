# analysis exp 001 sft 0pct 15B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_0pct_15B_20260513T212654_result.json`
- **Structured JSON:** [`be040ba038c428b46f2d.json`](../../sessions/be/be040ba038c428b46f2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_001_sft_0pct_15B 完成总结

训练正常完成，registry 已更新为 DONE。

```json
{
  "steps": "3125/3125",
  "final_loss": 1.2039,
  "mean_train_loss": 1.2599,
  "token_accuracy": 0.711,
  "training_time_min": 101.5,
  "checkpoint_size_mb": 313,
  "adapter_size_mb": 71,
  "exit_code": 0
}
```

**Checkpoint 验证**：`adapter_model.safetensors` (71M) 存在，含完整 tokenizer 文件和 `checkpoint-3125` 子目录。

**与 0.5B 对比**：1.5B 模型 mean_train_loss 1.2599 低于 0.5B 的 1.5388，token_accuracy 0.711 vs 0.682，符合预期（更大模型更低 loss）。训练时间 101.5 min vs 52.9 min，约为 2 倍。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "steps": "3125/3125",
    "final_loss": 1.2039,
    "mean_train_loss": 1.2599,
    "token_accuracy": 0.711,
    "training_time_min": 101.5,
    "checkpoint_size_mb": 313,
    "adapter_size_mb": 71,
    "exit_code": 0
  }
}
```

</details>

---
