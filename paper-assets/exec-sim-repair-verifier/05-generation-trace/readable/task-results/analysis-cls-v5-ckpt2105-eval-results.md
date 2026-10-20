# analysis cls v5 ckpt2105 eval results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls-v5-ckpt2105-eval-results_20260518T211955_result.json`
- **Structured JSON:** [`fac9a4c3f58a0ca9091e.json`](../../sessions/fa/fac9a4c3f58a0ca9091e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。结果汇总：

## DeepSeek CLS repo-v5 ckpt-2105 eval (s42, Table 4 canonical)

| 指标 | 值 |
|---|---|
| **Accuracy** | **82.61%** |
| Macro F1 | 75.07 |
| Pass F1 | 88.78 |
| Fail F1 | 61.35 |
| Precision (fail / pass) | 76.92 / 83.86 |
| Recall (fail / pass) | 51.02 / 94.33 |
| Unparseable | **0 / 9784 (0.00%)** |

**Confusion matrix**: TP=6733, FP=1296, TN=1350, FN=405

### 与 s123 参考值对比

| | s123 | s42 (本次) | Δ |
|---|---|---|---|
| Accuracy | 74.93% | **82.61%** | **+7.68 pp** |
| Unparseable rate | 1.36% | **0.00%** | -1.36 pp |

s42 大幅超过 s123 参考值，accuracy +7.68 pp，且 unparseable 降至 0。这是一个非常强的结果，可以直接用于 Table 4。

---
