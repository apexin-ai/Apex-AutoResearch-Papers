# code agnews mc v2

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_agnews-mc-v2_20260524T154635_result.json`
- **Structured JSON:** [`339f0c41c046f59e7334.json`](../../sessions/33/339f0c41c046f59e7334.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。关键结果：

- **Asymmetric R² = 0.9534**（vs symmetric R² = -1.24），完整的非对称 bias identity 准确预测了 Global correction 的残差偏差
- **P(Z=1)=0.5** 后 π̄ = 0.173（从之前的更高值降下来），Δπ = 0.19
- EC-HTE 在 n_expert ≥ 500 时 |Bias| 胜出（2/3 budget levels），但 RMSE 全输（variance-bias tradeoff：stratified 估计方差更大）
- Sign reversal 极低（Global 0.13%，EC-HTE 3%）
- 按 n_expert 分的 asymmetric R²：250 → 0.929，500 → 0.962，1000 → 0.966

三个输出文件已覆盖：`agnews_raw.csv`、`agnews_summary.csv`、`agnews_analysis.md`。

---
