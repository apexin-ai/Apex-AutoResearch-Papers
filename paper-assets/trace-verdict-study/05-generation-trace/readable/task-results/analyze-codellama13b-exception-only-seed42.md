# analyze codellama13b exception only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_codellama13b_exception_only_seed42_20260516T144625_result.json`
- **Structured JSON:** [`a9aac7933cf19a8651a9.json`](../../sessions/a9/a9aac7933cf19a8651a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告：`codellama13b_exception_only_seed42`

### 评估结果

| 指标 | 值 |
|------|-----|
| **Accuracy** | **99.83%** (1188/1190) |
| 95% CI | [99.58%, 100.0%] |
| Majority baseline | 71.5% (always predict "pass") |
| Lift over baseline | +28.3pp |

### Per-class 指标

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| pass | 1.00 | 1.00 | 1.00 |
| fail | 0.99 | 1.00 | 1.00 |

### 错误分析

仅 **2 个错误**，均为 pass→fail 误判（false negative for pass）：
- id=901, id=905：label=pass, pred=fail

无 fail→pass 误判（fail recall = 100%）。

### 训练状态

- 训练正常完成，`EXIT_CODE=0`
- 无 error / OOM
- Checkpoint 完整：adapter_model.safetensors (239MB) + tokenizer + eval_results + predictions

### Checkpoint 文件

```
adapter_config.json, adapter_model.safetensors (239MB), 
tokenizer.json, tokenizer.model, tokenizer_config.json,
eval_results.json, predictions.jsonl, training_args.bin
```

---
