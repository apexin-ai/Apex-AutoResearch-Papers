# infra gpu2 wait and launch D124

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu2-wait-and-launch-D124_20260518T032453_result.json`
- **Structured JSON:** [`bff79b1f07e8cd5fa028.json`](../../sessions/bf/bff79b1f07e8cd5fa028.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 1. CLS s123 eval 结果

| Metric | Value |
|---|---|
| **Accuracy** | 74.93% |
| **Majority baseline** | 72.96% |
| **Gap vs majority** | +1.97 pp |
| **F1 (fail)** | 22.84 |
| **F1 (pass)** | 85.03 |
| **F1 (macro)** | 53.94 |
| **Precision (fail/pass)** | 68.11 / 75.32 |
| **Recall (fail/pass)** | 13.72 / 97.62 |
| **Confusion matrix** | TN=363, FP=2283, FN=170, TP=6968 |
| **Support** | fail=2646, pass=7138 |
| **N instances** | 9784 |

CLS s123 几乎把所有样本预测为 pass（recall_pass=97.62%），对 fail 的召回极低（13.72%），accuracy 只比 majority baseline 高 ~2pp。

### 2. D124 启动确认

| Item | Value |
|---|---|
| **PID** | 700398 |
| **GPU** | 2 |
| **GPU Memory** | 16528 MiB |
| **Tmux session** | `cwm-s42-epoch2-eval` ✓ |

D124 (CWM s42 epoch2 eval) 已在 GPU 2 上正常运行。

---
