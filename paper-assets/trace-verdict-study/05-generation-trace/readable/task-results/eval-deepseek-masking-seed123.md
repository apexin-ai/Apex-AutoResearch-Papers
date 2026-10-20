# eval deepseek masking seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_deepseek-masking-seed123_20260523T134012_result.json`
- **Structured JSON:** [`288ba35ca6f7b7ada7bd.json`](../../sessions/28/288ba35ca6f7b7ada7bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### seed123 Eval 结果

| 指标 | seed123 | seed42 |
|------|---------|--------|
| **Accuracy** | **93.95%** | **99.33%** |
| Pass Precision | 0.924 | 1.000 |
| Pass Recall | 0.998 | 0.991 |
| Pass F1 | 0.959 | 0.995 |
| Fail Precision | 0.993 | 0.977 |
| Fail Recall | 0.794 | 1.000 |
| Fail F1 | 0.882 | 0.988 |

### 2-seed 统计

| 指标 | Mean | Std |
|------|------|-----|
| Accuracy | **96.64%** | **3.80pp** |

### 分析

seed123 accuracy 比 seed42 低了 **5.38pp**，差异很大。主要问题在 **fail recall**：seed123 只有 79.4%（seed42 是 100%），说明 seed123 漏判了约 20% 的 fail 样本。Pass recall 两者都接近 100%，所以 seed123 的问题集中在 fail → pass 的误分类。

标准差 3.80pp 说明 gradient masking 在 DeepSeek 上的训练稳定性存在问题——两个 seed 之间方差过大。可能需要检查 seed123 的训练 loss 曲线是否有异常，或者考虑跑第三个 seed 确认。

---
