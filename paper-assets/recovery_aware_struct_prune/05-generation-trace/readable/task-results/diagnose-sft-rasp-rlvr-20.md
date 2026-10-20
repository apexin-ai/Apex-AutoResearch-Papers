# diagnose sft rasp rlvr 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sft_rasp_rlvr_20_20260516T142219_result.json`
- **Structured JSON:** [`b512658c944a73e4f412.json`](../../sessions/b5/b512658c944a73e4f412.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载成功：6.16B 参数，tokenizer vocab=151643。现在汇总结果。

```json
{
  "disk_free_gb": 0.002,
  "disk_total_gb": 250,
  "model_dir_gb": 51,
  "model_loadable": true,
  "model_params": "6.16B",
  "missing_files": [
    "checkpoint-1870/rng_state.pth",
    "checkpoint-1870/scheduler.pt",
    "checkpoint-1870/trainer_state.json"
  ],
  "checkpoint_1870_issue": "optimizer.pt 仅 4.3GB（应为 ~23GB，对比 checkpoint-935），写入被磁盘满截断",
  "cleanup_candidates": [
    {"path": "sft_rasp_rlvr_20/checkpoint-935/", "size_gb": 35, "note": "中间 checkpoint，optimizer.pt=23G + model=12G，模型权重与 checkpoint-1870 重复"},
    {"path": "sft_rasp_rlvr_20/checkpoint-1870/optimizer.pt", "size_gb": 4.3, "note": "截断的 optimizer state，不可恢复训练"},
    {"path": "grpo_stage2_rasp_20_v9/", "size_gb": 38, "note": "如果 GRPO v9 已完成且不再需要"},
    {"path": "grpo_stage2_standard_20_v8/", "size_gb": 12, "note": "如果不再需要"},
    {"path": "DeepSeek-R1-Distill-Qwen-7B/ (autodl-tmp 根)", "size_gb": 15, "note": "基座模型，如不再使用"},
    {"path": "models/Qwen2.5-Math-7B/ (autodl-tmp 根)", "size_gb": 15, "note": "如果不再需要"}
  ],
  "fix_steps": [
    "1. 清理 checkpoint-935 整个目录（-35GB），这是最大收益：最终模型在 checkpoint-1870，中间 checkpoint 可删",
    "2. 删除 checkpoint-1870/optimizer.pt（-4.3GB）：已截断不可用，无法恢复训练",
    "3. 将 checkpoint-1870 中的模型文件（model.safetensors + config/tokenizer）提升到 sft_rasp_rlvr_20/ 根目录作为最终模型，然后删除 checkpoint-1870 子目录",
    "4. 评估 grpo_stage2_* 和基座模型目录是否仍需要（潜在释放 65-80GB）"
  ]
}
```

**关键结论**：
- 数据盘 250GB **100% 满**，仅剩 2MB
- checkpoint-1870 **模型权重完好可用**（6.16B params，需用 `load_pruned_model` 加载，不能用原生 `from_pretrained`）
- optimizer state 被截断（4.3G vs 预期 23G），缺失 rng/scheduler/trainer_state → **无法从此 checkpoint 恢复训练**
- 最快释放空间：删 checkpoint-935（35GB）+ 截断的 optimizer.pt（4.3GB）= **~39GB**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "disk_free_gb": 0.002,
    "disk_total_gb": 250,
    "model_dir_gb": 51,
    "model_loadable": true,
    "model_params": "6.16B",
    "missing_files": [
      "checkpoint-1870/rng_state.pth",
      "checkpoint-1870/scheduler.pt",
      "checkpoint-1870/trainer_state.json"
    ],
    "checkpoint_1870_issue": "optimizer.pt 仅 4.3GB（应为 ~23GB，对比 checkpoint-935），写入被磁盘满截断",
    "cleanup_candidates": [
      {
        "path": "sft_rasp_rlvr_20/checkpoint-935/",
        "size_gb": 35,
        "note": "中间 checkpoint，optimizer.pt=23G + model=12G，模型权重与 checkpoint-1870 重复"
      },
      {
        "path": "sft_rasp_rlvr_20/checkpoint-1870/optimizer.pt",
        "size_gb": 4.3,
        "note": "截断的 optimizer state，不可恢复训练"
      },
      {
        "path": "grpo_stage2_rasp_20_v9/",
        "size_gb": 38,
        "note": "如果 GRPO v9 已完成且不再需要"
      },
      {
        "path": "grpo_stage2_standard_20_v8/",
        "size_gb": 12,
        "note": "如果不再需要"
      },
      {
        "path": "DeepSeek-R1-Distill-Qwen-7B/ (autodl-tmp 根)",
        "size_gb": 15,
        "note": "基座模型，如不再使用"
      },
      {
        "path": "models/Qwen2.5-Math-7B/ (autodl-tmp 根)",
        "size_gb": 15,
        "note": "如果不再需要"
      }
    ],
    "fix_steps": [
      "1. 清理 checkpoint-935 整个目录（-35GB），这是最大收益：最终模型在 checkpoint-1870，中间 checkpoint 可删",
      "2. 删除 checkpoint-1870/optimizer.pt（-4.3GB）：已截断不可用，无法恢复训练",
      "3. 将 checkpoint-1870 中的模型文件（model.safetensors + config/tokenizer）提升到 sft_rasp_rlvr_20/ 根目录作为最终模型，然后删除 checkpoint-1870 子目录",
      "4. 评估 grpo_stage2_* 和基座模型目录是否仍需要（潜在释放 65-80GB）"
    ]
  }
}
```

</details>

---
