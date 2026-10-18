# analysis r4 a3 mi plugin vs closedform

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r4-a3-mi-plugin-vs-closedform_20260524T110501_result.json`
- **Structured JSON:** [`8b18cc3c073e9424cb84.json`](../../sessions/8b/8b18cc3c073e9424cb84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `artifacts/results/plan001/keff_plugin_vs_closedform.json`。

**核心发现**：

| 维度 | Pearson r | RMSE | Rank Spearman |
|------|-----------|------|---------------|
| **Overall** (2910 panels) | 0.966 | 1.009 | 0.970 |
| K=3 | 0.866 | 0.479 | 0.861 |
| K=5 | 0.875 | 0.927 | 0.864 |
| K=7 | 0.874 | 1.376 | 0.860 |
| MMLU | 0.972 | 1.035 | 0.981 |
| ARC | 0.957 | 0.982 | 0.966 |

- **排序一致性高**：within-K rank correlation ~0.86，两种方法对 panel diversity 排序基本一致
- **系统性偏移**：closed-form K_eff 系统性偏高（mean 4.29 vs 3.38），因为 plug-in MI 的 Miller-Madow 校正增大了 MI 值 → exp(-2·MI) 更小 → K_eff 更低
- **Overall r=0.97 偏高**：受 K 值跨度影响（K=3 vs K=7 天然拉开分布），within-K 的真实一致性在 0.86-0.87
- element-wise |exp(-2·MI) - (1-ρ²)| 均值 0.22，Gaussian copula 近似引入了中等偏差，但不影响排序结论

---
