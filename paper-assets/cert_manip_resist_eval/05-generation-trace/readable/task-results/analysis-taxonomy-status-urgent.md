# analysis taxonomy status urgent

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_taxonomy-status-urgent_20260522T045116_result.json`
- **Structured JSON:** [`8ce0d4bdc07427bc516a.json`](../../sessions/8c/8ce0d4bdc07427bc516a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。以下是完整结果。

---

## 1. Individual ASR 表格

### MMLU

| Model | Verbosity Bias | Position Bias | Authority Bias |
|-------|---------------|--------------|----------------|
| qwen2.5-72b | 0.0929 | 0.0044 | 0.0531 |
| llama3.1-70b | 0.1230 | 0.0738 | 0.0410 |
| mistral-large | 0.0085 | 0.0513 | 0.0684 |
| qwen2.5-32b | 0.0396 | 0.0264 | 0.0925 |
| qwen2.5-14b | 0.1059 | 0.0353 | 0.0706 |
| llama3.1-8b | 0.0862 | **0.1782** | 0.1034 |

### ARC Challenge

| Model | Verbosity Bias | Position Bias | Authority Bias |
|-------|---------------|--------------|----------------|
| qwen2.5-72b | 0.0659 | 0.0078 | 0.0155 |
| llama3.1-70b | 0.0783 | 0.0107 | 0.0249 |
| mistral-large | 0.0000 | 0.0173 | 0.0208 |
| qwen2.5-32b | 0.0560 | 0.0112 | 0.0373 |
| qwen2.5-14b | **0.1632** | 0.0263 | 0.0263 |
| llama3.1-8b | 0.0863 | 0.0406 | 0.0254 |

---

## 2. 回归结果表格

| 条件 | B(K_eff) | p(K_eff) | B(η_max) | p(η_max) | R² | η_max CV |
|------|----------|----------|----------|----------|----|----------|
| MMLU × verbosity | **-0.438** | 0.612 ns | **+1.931** | **0.006** | 0.407 | 0.113 |
| MMLU × position | +3.357 | **0.035** * | -0.016 | 0.945 ns | 0.543 | 0.483 |
| MMLU × authority | +0.616 | 0.486 ns | +0.368 | 0.468 ns | 0.143 | 0.135 |
| ARC × verbosity | -1.606 | 0.211 ns | **+1.117** | **0.011** | 0.333 | 0.334 |
| ARC × position | +9.646 | 0.084 ns | -2.690 | 0.110 ns | 0.166 | 0.320 |
| ARC × authority | +0.124 | 0.835 ns | **+1.254** | **0.003** | 0.433 | 0.181 |

---

## 3. 诊断判断

**K_eff 是否在两个数据集上一致显著为负？** — **否。** 0/6 条件 K_eff 显著为负。唯一显著的 K_eff（MMLU × position, p=0.035）方向为**正**（+3.36），与假设完全相反——更多有效评委反而关联更高 ASR。

**K_eff 仅在 η_max CV 低的条件下显著吗？** — 唯一显著的 K_eff（MMLU × position）η_max CV=0.483，是所有条件中最高的。这不是 artifact——但问题是方向错误。position bias 的 ASR 跨模型差异极大（0.004–0.178），高 CV 下 η_max 被"稀释"，K_eff 吸收了残差方差并呈现伪正相关。

**核心结论：taxonomy 假设被否定。**
- 即使对 broad-spectrum attacks，K_eff 也不提供额外保护
- η_max 是 3/6 条件中唯一显著预测因子（verbosity×两数据集 + authority×ARC）
- Panel 的安全性由**最脆弱的单个评委**决定（η_max），而非评委数量/多样性（K_eff）
- broad-spectrum vs targeted 的 taxonomy 分类不改变 K_eff 的无效性

---
