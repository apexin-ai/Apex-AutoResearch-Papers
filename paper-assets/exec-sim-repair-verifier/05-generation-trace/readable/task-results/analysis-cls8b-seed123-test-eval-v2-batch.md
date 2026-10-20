# analysis cls8b seed123 test eval v2 batch

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls8b-seed123-test-eval-v2-batch_20260515T103218_result.json`
- **Structured JSON:** [`561a02f1b3e3c26e601c.json`](../../sessions/56/561a02f1b3e3c26e601c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已更新为 DONE。

## 结果对比（Qwen3-8B CLS，seed123，test set n=9784）

| 指标 | ckpt-6400 | ckpt-6200 | 差值 |
|------|-----------|-----------|------|
| **Accuracy** | **85.08%** | 84.70% | +0.38pp |
| F1 macro | **77.91%** | 77.01% | +0.90pp |
| F1 fail | **65.32%** | 63.71% | +1.61pp |
| F1 pass | 90.49% | 90.31% | +0.18pp |
| Precision fail | 87.92% | **88.84%** | -0.92pp |
| Recall fail | **51.97%** | 49.66% | +2.31pp |
| Recall pass | 97.35% | **97.69%** | -0.34pp |

**结论**：ckpt-6400 全面优于 ckpt-6200，主要提升来自 fail 类的 recall（+2.3pp），带动 F1 fail 提升 1.6pp。两个 checkpoint 的 precision_fail 都很高（~88%），瓶颈在 recall_fail（~50-52%），模型倾向保守——预测为 fail 时大概率正确，但漏掉近一半真实 fail 样本。

---
