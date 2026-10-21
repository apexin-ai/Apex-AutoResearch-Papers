# analysis qwen15b no trace seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_no_trace_seed42_20260516T101415_result.json`
- **Structured JSON:** [`07464029fad82f752996.json`](../../sessions/07/07464029fad82f752996.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果: `qwen15b_no_trace_seed42`

### 评估指标

| 指标 | 值 | 95% CI |
|------|-----|--------|
| accuracy | 0.6731 | [0.646, 0.699] |
| pass_f1 | 0.7527 | [0.730, 0.775] |
| fail_f1 | 0.5180 | [0.476, 0.559] |
| **f1_macro** | **0.6353** | — |

Majority baseline: 0.7151 (always predict "pass")，lift = -4.2pp — 模型准确率低于多数类基线。

### 训练状态

**正常完成。** 3 epochs, train_loss=0.2235, runtime=850.8s, EXIT_CODE=0。

### Checkpoint 文件

- `adapter_model.safetensors`: 70.5 MB (LoRA adapter)
- `tokenizer.json`: 10.9 MB
- 其余配置文件齐全，共 ~85 MB

### 异常信息

- **模型表现低于 majority baseline**（accuracy 67.3% vs baseline 71.5%），说明 no_trace 条件下模型没有学到比"全部预测 pass"更好的判别能力。
- fail 类的 precision 很低（0.45），大量 pass 样本被误判为 fail。
- 两个 deprecation warning（`torch_dtype` deprecated, `top_k` generation flag ignored），不影响结果。

---
