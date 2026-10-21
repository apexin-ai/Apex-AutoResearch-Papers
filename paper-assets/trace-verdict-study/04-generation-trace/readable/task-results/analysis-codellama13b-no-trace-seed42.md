# analysis codellama13b no trace seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_codellama13b_no_trace_seed42_20260516T142138_result.json`
- **Structured JSON:** [`2e54a82e9beb61be4b48.json`](../../sessions/2e/2e54a82e9beb61be4b48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果: `codellama13b_no_trace_seed42`

### 核心指标

| 指标 | 值 | 95% CI |
|------|------|--------|
| **Accuracy** | **76.5%** | [73.8%, 78.7%] |
| Majority baseline | 71.5% (always predict 'pass') | |
| **Lift over baseline** | **+5.0pp** | [+2.0pp, +8.0pp] |

### Per-class 指标

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| pass | 0.84 | 0.83 | 0.84 |
| fail | 0.59 | 0.59 | 0.59 |

### 训练状态

- **正常完成**，EXIT_CODE=0，评估流程全部跑完
- 样本数 n=1190，Bootstrap 1000 resamples

### Checkpoint

- 路径: `/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final/`
- LoRA adapter 大小: **239MB** (`adapter_model.safetensors`)
- 含完整 tokenizer、eval_results.json、predictions.jsonl

### 小结

no_trace 条件下 accuracy 76.5%，比 majority baseline 高 5pp，但 fail 类召回率偏低（0.59），模型对 fail 样本的区分力有限。

---
