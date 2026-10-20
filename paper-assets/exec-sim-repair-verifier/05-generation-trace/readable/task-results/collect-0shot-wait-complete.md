# collect 0shot wait complete

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_0shot-wait-complete_20260517T231617_result.json`
- **Structured JSON:** [`74b09c279c9b141a842d.json`](../../sessions/74/74b09c279c9b141a842d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 0-shot Repo-Level 评估结果 (Qwen3-8B)

| 指标 | 值 |
|---|---|
| **Accuracy** | 49.9% |
| **Pass F1** | 48.95% |
| **Fail F1** | 50.81% |
| **Unparseable rate** | 0.00% (0/9784) |
| **Truncated** | 0 |
| **总运行时间** | 1018.2s (~17 分钟) |

**Confusion Matrix:**

|  | Pred Neg | Pred Pos |
|---|---|---|
| **Actual Neg** | TN = 2532 | FP = 114 |
| **Actual Pos** | FN = 4788 | TP = 2350 |

关键观察：模型严重偏向预测 "fail"（负类）。FN=4788 远超 FP=114，说明大量真正 pass 的样本被错误判为 fail。总体性能接近随机（~50%），0-shot 在 repo-level 上基本无效。

---
