# poll westd cuda3 ckpt3000 v4

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_poll_westd-cuda3-ckpt3000-v4_20260515T080800_result.json`
- **Structured JSON:** [`002d7a2431132a718ab7.json`](../../sessions/00/002d7a2431132a718ab7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已完成，metrics 已注册。完整结果：

**cls8b-seed123-ckpt3000 Test@8192 Results** (n=9784)

| Metric | Value |
|---|---|
| **Accuracy** | **85.60%** |
| Majority baseline | 72.96% |
| **Gap vs majority** | **+12.64pp** |
| **F1 macro** | **78.38%** |
| F1 fail | 65.89% |
| F1 pass | 90.87% |
| Precision fail | 91.65% |
| Recall fail | 51.44% |
| Precision pass | 84.52% |
| Recall pass | 98.26% |
| Unparseable | 0 |

**Confusion matrix:**

|  | Pred fail | Pred pass |
|---|---|---|
| Actual fail | 1361 (TN) | 1285 (FP) |
| Actual pass | 124 (FN) | 7014 (TP) |

模型在 pass 类上表现很强 (recall 98.3%)，但 fail 类 recall 偏低 (51.4%)——近一半的 fail 样本被误判为 pass。Precision fail 很高 (91.7%)，说明预测为 fail 的大多是对的，但模型偏保守不敢预测 fail。

---
