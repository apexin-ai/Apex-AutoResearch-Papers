# analysis label only seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_label_only_seed456_20260516T090219_result.json`
- **Structured JSON:** [`e84fb95f056c2b8377a6.json`](../../sessions/e8/e84fb95f056c2b8377a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常完成（EXIT_CODE=0）。评估结果：

## label_only_seed456 评估结果

| 指标 | 值 | 95% CI |
|------|-----|--------|
| **Accuracy** | 85.9% | [83.9%, 87.7%] |
| Majority baseline | 71.5% | [69.2%, 73.9%] |
| **Lift** | +14.4pp | [+11.8pp, +16.9pp] |
| n | 1190 | — |

### Per-class metrics

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| **pass** | 0.874 [0.854, 0.895] | 0.938 [0.921, 0.954] | 0.905 [0.891, 0.918] |
| **fail** | 0.809 [0.762, 0.854] | 0.661 [0.612, 0.711] | 0.727 [0.687, 0.764] |

模型对 pass 类预测较强（高 recall），对 fail 类 recall 偏低（66.1%），存在一定漏检。

---
