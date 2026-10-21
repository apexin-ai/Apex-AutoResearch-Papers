# analysis bernoulli adjustment

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bernoulli_adjustment_20260521T085720_result.json`
- **Structured JSON:** [`16c0dc5047fd3061d35c.json`](../../sessions/16/16c0dc5047fd3061d35c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`results/analysis/bernoulli_adjustment.json` 已生成。核心结果：

**Bernoulli ceiling 验证**：所有 5 个数据集的 ceiling ratio ≈ 1.000（mean=1.000002），确认 binary 数据的 total variance 严格等于 p(1-p)。

**关键论点**：既然 total variance = p(1-p)，那么 variance component 的百分比分解**天然就是 Bernoulli-adjusted 的**（% = component / p(1-p) × 100）。跨数据集比较百分比不受 accuracy 水平影响。

**经验验证**：
- 3 个 resampling samples（accuracy 0.62–0.72），item_id% = 72.2–75.9%，CV = 2.69%
- Correlation(accuracy, item_id%) = −0.048，近乎零相关
- 梯度稳定，不是 Bernoulli artifact

**Per-model 交互调整**：
- Mistral（最低 accuracy 0.638，最高 ceiling 0.231）：raw 29.25% → adjusted 26.33%
- 调整后排序变化但梯度持续存在，不是纯 ceiling 效应

---
