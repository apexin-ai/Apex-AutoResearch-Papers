# ops check seed123 eval results

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-seed123-eval-results_20260522T145854_result.json`
- **Structured JSON:** [`951fbc1d5889242dadc0.json`](../../sessions/95/951fbc1d5889242dadc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已完成，结果如下：

| 指标 | 值 |
|------|-----|
| **accuracy** | 0.9933 |
| **pass_f1** | 0.9953 |
| **pass_precision** | 1.0000 |
| **pass_recall** | 0.9906 |
| **fail_f1** | 0.9883 |
| **fail_precision** | 0.9769 |
| **fail_recall** | 1.0000 |
| **n_test** | 1190 |

condition: `exception_only`, majority baseline: 0.7151, lift: +0.2782。fail 类别实现了完美 recall (1.0)，pass 类别实现了完美 precision (1.0)。

---
