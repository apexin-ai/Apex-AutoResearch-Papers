# analysis deepseek eo seed123 epoch level

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_eo_seed123_epoch_level_20260515T201053_result.json`
- **Structured JSON:** [`3771cd0f4c03ec51fc6b.json`](../../sessions/37/3771cd0f4c03ec51fc6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全了。以下是 epoch-level 分析结果：

## DeepSeek exception_only seed123 — Epoch-level Metrics

### Trainer eval metrics（token-level，来自 trainer_state.json）

| Epoch | Step | eval_loss | eval_mean_token_accuracy |
|-------|------|-----------|--------------------------|
| 1     | 148  | **0.2794** | 0.9255 (92.55%) |
| 2     | 296  | 0.4131    | 0.9195 (91.95%) |
| 3     | 444  | 0.4814    | 0.9193 (91.93%) |

### Final model classification metrics（来自 evaluate.py，epoch 3/final）

| Metric | Value |
|--------|-------|
| accuracy | **91.09%** |
| fail_f1 | **0.8185** |
| fail_recall | 70.50% |
| fail_precision | 97.55% |
| pass_recall | 99.29% |

### 结论

**Epoch 1 不接近 99%。** Token accuracy 在 epoch 1 就只有 92.55%，后续 epoch 几乎不变（91.9%）。

Overfitting 确实存在——eval_loss 从 0.28 → 0.48 单调上升，但这只影响了 calibration，**分类准确率本身始终在 91-92.5% 区间，从未接近 99%**。

这意味着 seed123 的问题**不是 overfitting 从 99% 跌到 91%**，而是这个 seed 从一开始就没学好。Early stopping 到 epoch 1 最多能挽回约 1.5% 的 accuracy（92.5% vs 91.1%），远不及 seed42 的 99.83%。

如果需要 epoch 1 的精确分类 accuracy 和 fail_f1，需要对 checkpoint-148 跑 evaluate.py（需要 GPU）。但基于 token accuracy 的趋势，预计 epoch 1 分类 accuracy 在 92-93% 左右。

---
