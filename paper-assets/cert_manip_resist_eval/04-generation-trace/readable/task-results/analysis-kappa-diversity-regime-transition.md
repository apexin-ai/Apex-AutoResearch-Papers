# analysis kappa diversity regime transition

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kappa-diversity-regime-transition_20260524T031621_result.json`
- **Structured JSON:** [`a62f521aa61c0f31e341.json`](../../sessions/a6/a62f521aa61c0f31e341.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 输出完整。汇报结果。

## κ-diversity vs K_eff 的 Regime Transition 对比

| K | η_max (K_eff模型) | K_eff | η_max (κ-div模型) | κ-diversity |
|---|-------------------|-------|-------------------|-------------|
| 3 | 3/12 | **4/12** | 1/12 | **8/12** |
| 5 | 0/12 | **10/12** | 4/12 | **7/12** |
| 7 | 0/12 | **9/12** | 1/12 | **6/12** |

**相关性**：κ-diversity 与 K_eff 的 Pearson r = 0.9796, Spearman ρ = 0.9733。

### 关键发现

**Predictor shift pattern 不同**：

- **K_eff**：存在明确的 regime transition — K=3 时两个 predictor 都温和显著，K≥5 时 K_eff 压倒性主导（10-9/12），η_max 完全消失（0/12）。
- **κ-diversity**：**从 K=3 起就是主导 predictor**（8/12），随 K 增大略有下降（7→6/12），无明显 transition。η_max 在 κ-diversity 模型中的表现不稳定（1/4/1）。

### 原因

尽管两个 metric 高度相关（r≈0.98），但 wild cluster bootstrap 测试的是 predictor 在不同 cluster 结构下的鲁棒性。κ-diversity 直接衡量 label 一致性（与投票机制直接相关），K=3 时已能有效预测攻击抵抗力。K_eff 基于 MI 的信息论度量，需要更大 panel（K≥5）才能展现 "effective independent judges" 效应。

**结论**：regime transition 是 K_eff（MI-based）的特有属性，不是所有 diversity metric 的共性。

---
