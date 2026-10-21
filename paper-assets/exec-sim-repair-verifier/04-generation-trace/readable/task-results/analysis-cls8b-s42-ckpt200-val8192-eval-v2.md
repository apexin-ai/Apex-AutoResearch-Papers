# analysis cls8b s42 ckpt200 val8192 eval v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls8b-s42-ckpt200-val8192-eval-v2_20260514T223733_result.json`
- **Structured JSON:** [`5a71a1ddc3b4589fa984.json`](../../sessions/5a/5a71a1ddc3b4589fa984.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cls8b-s42-ckpt200-val8192-eval-v2 评估结果

| 指标 | 值 |
|------|-----|
| **Accuracy** | 63.52% |
| **F1 macro** | 61.17% |
| **F1 (fail)** | 51.6% |
| **F1 (pass)** | 70.7% |
| **Precision (fail)** | 38.0% |
| **Precision (pass)** | 90.4% |
| **Recall (fail)** | 80.6% |
| **Recall (pass)** | 58.1% |
| **Samples evaluated** | 9335 |
| **Class balance** | pass=7083, fail=2252 |
| **Majority baseline** | 75.9% |
| **Accuracy vs majority** | -12.3pp |
| **Unparseable** | 9 (0.10%) |
| **Exit code** | 0 (成功) |

**Confusion Matrix:**

|  | Pred fail | Pred pass |
|--|-----------|-----------|
| **Actual fail** | 1815 | 437 |
| **Actual pass** | 2968 | 4115 |

**关键发现：**
- Accuracy 63.52% **低于** majority baseline 75.9%（差 -12.3pp），模型在 val set 上表现不佳
- 模型对 fail 类 recall 高（80.6%）但 precision 极低（38.0%），大量 pass 样本被误判为 fail（2968 个 false positive）
- pass 类 precision 高（90.4%）但 recall 低（58.1%），说明模型过度倾向预测 fail
- 无错误或异常，9 个 unparseable 用了 majority fallback

---
