# analysis beta std trajectory

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_beta-std-trajectory_20260524T190134_result.json`
- **Structured JSON:** [`23435f9965c5ed6a7697.json`](../../sessions/23/23435f9965c5ed6a7697.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs generated successfully. Summary:

| K | β_std(K_eff) | β_std(η_max) | K_eff sig | η_max sig |
|---|---|---|---|---|
| 3 | 0.349 ± 0.183 | 0.266 ± 0.179 | 7/12 | 5/12 |
| 5 | 0.437 ± 0.293 | 0.101 ± 0.327 | 8/12 | 5/12 |
| 7 | 0.401 ± 0.222 | 0.084 ± 0.284 | 9/12 | 3/12 |

Predictor shift 在 standardized effect size 上得到了确认：β_std(K_eff) 在 K=3→7 保持稳定偏高（0.35→0.44→0.40），而 β_std(η_max) 从 0.27 下降到 0.08，向零收敛。这与 significance count 的趋势一致，但提供了连续量化的证据。

输出文件：
- JSON: `artifacts/results/plan001/beta_std_trajectory.json`
- 轨迹图: `artifacts/results/plan001/fig_beta_std_trajectory.pdf`
- p-value 分布图: `artifacts/results/plan001/fig_pvalue_distribution.pdf`

---
