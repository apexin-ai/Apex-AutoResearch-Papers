# collect ckpt600 test8192 final metrics

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_ckpt600-test8192-final-metrics_20260514T220239_result.json`
- **Structured JSON:** [`02f2076e2e65e9c8bc31.json`](../../sessions/02/02f2076e2e65e9c8bc31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ckpt-600 test@8192 完整指标

| 指标 | 值 |
|------|-----|
| **Accuracy** | 79.05% |
| **F1 macro** | 75.12% |
| **F1 fail (positive)** | 65.24% |
| **F1 pass (negative)** | 85.00% |
| **Precision fail** | 59.16% |
| **Precision pass** | 88.95% |
| **Recall fail** | 72.71% |
| **Recall pass** | 81.40% |
| **Unparseable rate** | 0 / 9784 (0.00%) |
| **Gap vs majority** | +6.09pp |

**混淆矩阵：**
|  | Pred fail | Pred pass |
|--|-----------|-----------|
| **Actual fail** | 1924 (TN) | 722 (FP) |
| **Actual pass** | 1328 (FN) | 5810 (TP) |

测试集 9784 条，类别分布 pass=7138 / fail=2646，majority baseline 73.0%。模型 Qwen3-8B，checkpoint-600，max_seq_length=8192。

---
