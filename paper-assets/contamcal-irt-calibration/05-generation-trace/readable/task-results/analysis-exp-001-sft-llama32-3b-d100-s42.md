# analysis exp 001 sft llama32 3B d100 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_llama32_3B_d100_s42_20260516T182115_result.json`
- **Structured JSON:** [`8f560a2c4b5c8f9d14b1.json`](../../sessions/8f/8f560a2c4b5c8f9d14b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

### 训练状态：成功完成
- `EXIT_CODE=0`，正常退出
- LoRA adapter 保存 → merged model 保存 → "Training complete." 日志确认

### Final Train Loss
- **d100**: `1.5435` (train_runtime: 9847s ≈ 2h44m, 4159 steps, epoch=1.0)
- mean_token_accuracy: 0.6505

### Checkpoint 完整性
```
/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d100_s42/  (总计 6.4G)
├── merged/
│   ├── model-00001-of-00002.safetensors  (4.97GB)
│   ├── model-00002-of-00002.safetensors  (1.46GB)
│   ├── config.json, generation_config.json
│   ├── tokenizer.json, tokenizer_config.json, special_tokens_map.json
│   └── chat_template.jinja, model.safetensors.index.json
├── lora_adapter/
│   ├── adapter_model.safetensors (97MB)
│   ├── adapter_config.json, training_args.bin
│   ├── checkpoint-4159/
│   └── tokenizer files
└── train_config.json
```
完整，merged 模型 ~6.4GB 符合 Llama-3.2-3B 预期。

### W&B
日志中未搜到 wandb 相关信息，本次训练未启用 W&B logging。

### Train Loss 对比

| 实验 | Final Train Loss | Token Accuracy | Runtime |
|------|-----------------|----------------|---------|
| d005 (5% 污染) | 1.5206 | 0.6599 | 2h15m |
| d025 (25% 污染) | 1.5265 | 0.6755 | 2h19m |
| d100 (100% 污染) | **1.5435** | 0.6505 | 2h44m |

### 异常发现
1. **d100 loss 比 d005/d025 略高**（1.5435 vs 1.52-1.53），且 token accuracy 更低（0.6505 vs 0.66-0.68）。这可能是因为 100% 污染数据量更大（21M tokens vs 19M），训练仅跑 1 epoch 尚未充分收敛。
2. **d005 的 merged model 保存失败**（磁盘空间不足 `No space left on device`，EXIT_CODE=1）。但 LoRA adapter 已保存成功。如果后续需要 d005 的 merged 模型需要重新 merge。
3. d100 训练时间更长（9847s vs 8140-8349s），与 100% 污染数据量更大一致。

---
