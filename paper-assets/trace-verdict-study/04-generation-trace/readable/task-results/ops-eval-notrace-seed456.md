# ops eval notrace seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-notrace-seed456_20260523T001232_result.json`
- **Structured JSON:** [`f20f78824841f0e8b03e.json`](../../sessions/f2/f20f78824841f0e8b03e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## no_trace_seed456 评估结果

### Metrics

| Metric | Value |
|--------|-------|
| **accuracy** | **75.04%** |
| accuracy 95% CI | [72.35%, 77.48%] |
| n | 1190 |
| pass_precision | 0.8805 |
| pass_recall | 0.7532 |
| pass_f1 | 0.8119 |
| fail_precision | 0.5455 |
| fail_recall | 0.7434 |
| fail_f1 | 0.6292 |
| eval_loss | 0.6092 |
| train_loss | 0.1781 |
| checkpoint | `/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace_seed456/final` |
| log | `/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace_seed456.log` |

### 3-seed 对比 (no_trace condition)

| Seed | Accuracy |
|------|----------|
| seed42 | 75.13% |
| seed123 | 79.08% |
| seed456 | 75.04% |
| **Mean ± Std** | **76.42 ± 2.31%** |

seed456 与 seed42 接近，seed123 偏高。3-seed 标准差 2.31 个百分点，方差较大，主要由 seed123 拉高。

---
