# analysis deepseek full trace seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_full_trace_seed42_20260515T163712_result.json`
- **Structured JSON:** [`8bebb495b57e0bf7f86c.json`](../../sessions/8b/8bebb495b57e0bf7f86c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部更新，status 已转为 DONE。

## 结果摘要

| 指标 | 值 |
|------|-----|
| **Accuracy** | **28.5%** [26.1%, 30.8%] |
| Majority baseline | 71.5% |
| Lift | **-43.0pp** |
| Pass P/R/F1 | 0.00 / 0.00 / 0.00 |
| Fail P/R/F1 | 0.28 / 1.00 / 0.44 |
| Train loss | 0.052 |
| Eval loss (ep2→ep3) | 0.090 → 0.110 |
| 训练时长 | 2.7h (2.85 GPU-hours) |

## 诊断：模型坍塌，全部预测为 fail

**关键对比：**

| Condition | DeepSeek | Qwen |
|-----------|----------|------|
| no_trace | 73.4% | — |
| full_trace | **28.5%** ❌ | 81.8% |
| VOTA | 84.5% | — |
| exception_only | 99.3% | — |

**核心发现：**
1. 模型将 1190 个测试样本全部预测为 fail（少数类），pass recall = 0
2. Qwen 在同一 full_trace 数据上正常工作 (81.8%)，说明数据没问题
3. DeepSeek 在 VOTA/exception_only 上表现优秀，说明模型本身有能力
4. eval_loss 从 epoch2 到 epoch3 上升，存在 overfitting，但核心问题是 generation collapse
5. Registry 中的 metrics.note 提到 **与 Qwen full_trace_v2 (28.4%) chat template fix 前的模式相同**——可能是 chat template 导致 label 被截断

---
