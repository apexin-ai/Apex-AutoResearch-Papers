# analysis full trace 1024tok seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_full_trace_1024tok_seed42_20260516T015538_result.json`
- **Structured JSON:** [`fad8f0bcf46215596c32.json`](../../sessions/fa/fad8f0bcf46215596c32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## full_trace_1024tok_seed42 实验结果

### 核心指标

| 指标 | 值 | 95% CI |
|------|------|--------|
| **Accuracy** | **77.23%** | [74.87%, 79.58%] |
| Majority baseline | 71.51% | [69.16%, 73.87%] |
| Lift over majority | +5.71pp | [+2.52pp, +9.16pp] |

### Per-class 指标

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| **pass** | 0.9006 [0.8795, 0.9231] | 0.7662 [0.7375, 0.7939] | 0.8279 [0.8071, 0.8469] |
| **fail** | 0.5730 [0.5319, 0.6172] | 0.7876 [0.7442, 0.8338] | 0.6634 [0.6269, 0.7005] |

### 训练指标

- train_loss: **0.0634**
- train_runtime: 5553s (~92min)
- epoch: 3.0
- test samples: 1190
- bootstrap resamples: 1000

### 缺失项

- **无 ECE / calibration 指标**
- **无 predictions.jsonl**（paired bootstrap 不可用）
- **无 eval_loss**

### Trace Length Ablation 汇总

| 截断长度 | Accuracy |
|----------|----------|
| 256tok | 78.82% |
| 512tok | 80.42% |
| **1024tok** | **77.23%** |
| no_limit | 81.76% |

1024tok 的 accuracy (77.23%) **低于** 256tok (78.82%) 和 512tok (80.42%)，这个结果异常——更长的 trace 反而表现更差。可能需要检查数据预处理或训练是否有问题。

---
