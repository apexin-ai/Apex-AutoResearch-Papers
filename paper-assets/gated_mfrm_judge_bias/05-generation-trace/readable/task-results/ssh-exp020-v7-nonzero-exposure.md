# ssh exp020 v7 nonzero exposure

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp020-v7-nonzero-exposure_20260525T161724_result.json`
- **Structured JSON:** [`d2810778249cadbe0ee8.json`](../../sessions/d2/d2810778249cadbe0ee8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v7 结果

| 指标 | v7 (e_i>0, 231 items) | v3 (317 items) | raw_average (same items) |
|------|----------------------|----------------|--------------------------|
| Kendall τ | **0.779** | 0.809 | 0.779 |
| Spearman ρ | 0.904 | 0.921 | 0.917 |
| Δτ vs raw | **0.000** | -0.015 | — |
| R̂ max | 1.0038 | — | — |
| ESS min | 1044 | — | — |
| Divergences | 0 | — | — |

**判断**：Δτ = 0.000 > v3 的 -0.015，说明去掉 86 个 e_i=0 items 确实消除了 v3 中 G-MFRM 比 raw_average 差的问题。但 G-MFRM 仍然没有正向改善（Δτ 仍为零而非正数），即使在纯非零 exposure 的 items 上，contamination gating 也没能 beat raw_average。

注意 v7 的绝对 τ (0.779) 低于 v3 (0.809)，这是因为 item pool 更小、信息更少，而非模型变差。c_n 分布合理——gpt-4-turbo 最高(3.08)、claude-3-opus 最低(1.51)。

---
