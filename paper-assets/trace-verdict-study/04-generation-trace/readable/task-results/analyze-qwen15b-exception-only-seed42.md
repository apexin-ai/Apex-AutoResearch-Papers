# analyze qwen15b exception only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen15b_exception_only_seed42_20260516T095450_result.json`
- **Structured JSON:** [`a80e78e7a62eb1905112.json`](../../sessions/a8/a80e78e7a62eb1905112.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果: `qwen15b_exception_only_seed42`

### 评估指标

| 指标 | 值 | 95% CI |
|------|-----|--------|
| **Accuracy** | 99.83% | [99.58%, 100.0%] |
| **n** | 1190 | — |
| **Pass F1** | 0.9988 | [0.9971, 1.0] |
| **Pass Precision** | 1.0000 | — |
| **Pass Recall** | 0.9976 | [0.9941, 1.0] |
| **Fail F1** | 0.9971 | [0.9926, 1.0] |
| **Fail Precision** | 0.9941 | [0.9852, 1.0] |
| **Fail Recall** | 1.0000 | — |
| Majority baseline | 71.5% (always predict pass) | — |
| Lift | +28.3pp | [+25.9pp, +30.8pp] |

### 训练状态

正常完成。3 epochs, 444 steps, 总耗时 29m22s。
- train_loss: 0.1347
- eval_loss: 0.5761
- mean_token_accuracy: 0.9038

### Checkpoint

路径: `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final/`

| 文件 | 大小 |
|------|------|
| adapter_model.safetensors | 70.5 MB |
| tokenizer.json | 10.9 MB |
| vocab.json | 2.6 MB |
| predictions.jsonl | 1.6 MB |
| 总目录 | ~88 MB |

### 异常/警告

- `torch_dtype` deprecated 警告（无影响）
- `top_k` generation flag 被忽略（无影响）
- 无实质性错误，EXIT_CODE=0

---
