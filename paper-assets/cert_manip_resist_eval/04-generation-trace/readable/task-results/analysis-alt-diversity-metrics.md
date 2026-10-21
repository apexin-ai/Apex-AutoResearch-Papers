# analysis alt diversity metrics

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alt-diversity-metrics_20260522T193159_result.json`
- **Structured JSON:** [`a5ce476b2e9800bff12d.json`](../../sessions/a5/a5ce476b2e9800bff12d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果：

### Part A: Alternative Diversity Metrics

| Metric | η_max FDR sig | D FDR sig | D方向 | r(K_eff) | ρ(K_eff) |
|--------|-------------|-----------|-------|----------|----------|
| Q-statistic (1-Q) | **12/12** | 2/12 | 1+/1- | 0.674 | 0.708 |
| Disagreement rate | **11/12** | 8/12 | 7+/1- | 0.861 | 0.860 |
| κ-diversity (1-κ) | **11/12** | 7/12 | 7+/0- | 0.942 | 0.947 |

η_max 在所有 3 种 diversity metrics 下都稳定显著（11-12/12），diversity 的独立效应则较弱且不稳定（2-8/12）。与 K_eff 的相关性从 0.674 (Q) 到 0.942 (κ)，κ-diversity 与 MI-based K_eff 高度重合。

### Part B: Effect Sizes

- **Canonical OLS std β**: η_max = 0.387 ± 0.179, K_eff = 0.164 ± 0.182（η_max 效应约为 K_eff 的 2.4 倍）
- **Practical Δ_ASR (IQR)**: mean = 0.0133 ± 0.0164（K_eff 从 25th 到 75th 分位对应约 1.3pp ASR 变化）
- **Clustered SE 95% CI**: K_eff 在 **11/12** conditions 包含 0，η_max 仅 4/12 包含 0

结论与 canonical K_eff 分析一致：weakest-link dominance 在所有 diversity operationalization 下都成立。

---
