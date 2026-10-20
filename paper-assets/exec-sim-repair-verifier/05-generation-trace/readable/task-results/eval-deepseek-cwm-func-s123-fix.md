# eval deepseek cwm func s123 fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_deepseek-cwm-func-s123-fix_20260516T084207_result.json`
- **Structured JSON:** [`1dbce2644ff67ca933db.json`](../../sessions/1d/1dbce2644ff67ca933db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM Func Eval 结果对比

| 指标 | seed42 | seed123 | Δ |
|------|--------|---------|---|
| **Accuracy** | 85.77% | **87.88%** | +2.11pp |
| **F1 macro** | 85.73% | **87.88%** | +2.15pp |
| Unparseable | 0% | 0% | — |
| F1 (fail) | 86.42% | 88.09% | +1.67pp |
| F1 (pass) | 85.05% | 87.67% | +2.62pp |
| Precision (fail) | 80.07% | 83.78% | +3.71pp |
| Recall (fail) | 93.86% | 92.87% | -0.99pp |
| Precision (pass) | 93.18% | 92.61% | -0.57pp |
| Recall (pass) | 78.22% | 83.23% | +5.01pp |

**seed123 比 seed42 高出 +2.1pp accuracy / +2.15pp F1**，且 class balance 验证一致 (fail=912, pass=978)。

---
