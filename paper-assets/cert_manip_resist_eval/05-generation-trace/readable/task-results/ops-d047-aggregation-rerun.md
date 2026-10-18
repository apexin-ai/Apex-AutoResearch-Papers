# ops d047 aggregation rerun

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d047-aggregation-rerun_20260525T215005_result.json`
- **Structured JSON:** [`7eca2a4aab5abb3f81c3.json`](../../sessions/7e/7eca2a4aab5abb3f81c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits look correct. Here's the summary:

**旧值 → 新值对比：**

| 方法 | 列 | 旧 | 新 | 变化原因 |
|---|---|---|---|---|
| Threshold | K_eff sig | 11/12 | 9/12 | position_bias 修正后3个条件 K_eff 不再FDR显著 |
| Threshold | β dir | 11+/0− | 8+/1− | arc×position_bias 的 K_eff β 变为负值 (−0.860) |
| Threshold | R² | 0.829 | 0.745 | position_bias 条件 R² 大幅下降 |
| Weighted | β dir | 12+/0− | 10+/2− | 两个 position_bias 条件 β_keff 变负（与 Majority 一致） |
| Weighted | R² | 0.328 | 0.336 | 微调 |
| Bayesian | η_max sig | 9/12 | 8/12 | 一个条件变为非显著 |
| Bayesian | R² | 0.087 | 0.136 | position_bias 修正后 R² 提升 |

**方向变化分析：** Position bias bug 修复对 K_eff β 方向的影响在 Threshold 和 Weighted 上与 Majority 一致——两个 position_bias 条件（mmlu×position_bias, arc×position_bias）的 K_eff β 均为负值。Bayesian 的 K_eff 方向未变（仍为 5+/1−），因为其中一个 position_bias 条件的 K_eff 本就不显著。

**注意事项：**
1. Majority 行 R² (0.327) 可能也是旧值——重算结果为 0.349，但遵照指示未修改。
2. Appendix K=5/K=7 表格使用 WCB（非 OLS FDR），也受 position bias 修正影响，但需要单独重跑 WCB 分析。

---
