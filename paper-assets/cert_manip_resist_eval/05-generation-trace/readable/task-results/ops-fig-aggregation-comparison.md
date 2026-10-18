# ops fig aggregation comparison

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fig-aggregation-comparison_20260525T150752_result.json`
- **Structured JSON:** [`930205af85936e0f0b45.json`](../../sessions/93/930205af85936e0f0b45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出文件：
- `docs/paper/figures/fig_aggregation_comparison.pdf` (23KB)
- `docs/paper/figures/fig_aggregation_comparison.png` (132KB)

数据来源：
- **K=3** (OLS, from `k5_aggregation_analysis.json`): Majority=8, Weighted=9, Threshold=11, Bayesian=7
- **K=5** (WCB, from `k5_aggregation_bootstrap.json`): 全部=7/12
- **K=7** (WCB, from `k7_aggregation_bootstrap.json`): Majority=8, Weighted=6, Threshold=10, **Bayesian=0**
- **R²** (K=5 OLS mean): Majority=0.26, Weighted=0.25, Threshold=0.51, Bayesian=0.08

关键视觉对比：Bayesian 在 K=7 归零（红色 X + "0/12"），而 Threshold Supermajority 在 K=7 反而增至 10/12 且 R²最高（0.51）。

---
