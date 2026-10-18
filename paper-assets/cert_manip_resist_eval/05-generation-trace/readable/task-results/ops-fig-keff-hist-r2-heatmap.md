# ops fig keff hist r2 heatmap

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fig-keff-hist-r2-heatmap_20260525T155945_result.json`
- **Structured JSON:** [`9d267dc9d169d1e6d871.json`](../../sessions/9d/9d267dc9d169d1e6d871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个图均正确：

**图 A (K_eff Histogram)**：K=3/5/7 三组分布清晰分离，均值分别为 2.09/3.48/4.87，虚线标注到位。K=3 分布最宽（相对范围），K_eff 值域 [0.75, 6.21]，符合预期。

**图 B (R² Heatmap)**：Threshold 聚合方法在所有 K 值下 R² 最高（0.83/0.41/0.51），Bayesian 最低（0.09/0.17/0.10）。Majority 和 Weighted 表现接近。颜色映射和数值标注清晰。

输出文件：
- `docs/paper/figures/fig_keff_hist.pdf` + `.png`
- `docs/paper/figures/fig_aggregation_r2_heatmap.pdf` + `.png`

---
