# ssh exp002 weight sensitivity

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp002_weight_sensitivity_20260522T170028_result.json`
- **Structured JSON:** [`4d03ff84304b772d3dd2.json`](../../sessions/4d/4d03ff84304b772d3dd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Sensitivity Analysis 结果

### 对比表

| Variant | Weights (A,C) | Mean | Std | Median | Q1 | Q3 | e_i>0.5 (%) | Spearman vs 75/25 |
|---------|--------------|------|-----|--------|-----|-----|-------------|-------------------|
| **Current** | **(75,25)** | **0.2121** | **0.2359** | **0.1251** | **0.0000** | **0.3228** | **59/317 (18.6%)** | **1.000** |
| A | (100,0) | 0.2008 | 0.2124 | 0.1358 | 0.0000 | 0.3140 | 41/317 (12.9%) | 0.998 |
| B | (50,50) | 0.2268 | 0.2708 | 0.0965 | 0.0000 | 0.3536 | 71/317 (22.4%) | 0.998 |
| C | (90,10) | 0.2050 | 0.2207 | 0.1289 | 0.0000 | 0.3147 | 44/317 (13.9%) | 0.999 |

### Rank Stability
- 所有变体与 baseline 的 category agreement（low/med/high）均 **>92%**
- Top-20 overlap: 14-16/20

### Pairwise Spearman Matrix
所有 pair 间 ρ ≥ 0.992。

### 产出路径
- `results/sensitivity_100_0/exposure_scores.csv`
- `results/sensitivity_50_50/exposure_scores.csv`
- `results/sensitivity_90_10/exposure_scores.csv`

### 结论

**权重选择对 e_i 排序几乎没有影响**（Spearman ≥ 0.992），但对分布形态有显著影响：
- 增大 Source C 权重（50/50）→ 标准差增大到 0.271，高 exposure 比例升至 22.4%（因为 Source C 的 z-score 分布更 heavy-tailed）
- 纯 Source A（100/0）→ 标准差压缩到 0.212，高 exposure 比例降至 12.9%
- 当前 75/25 和 90/10 差异很小

**核心发现：权重改变的是 e_i 的阈值灵敏度（有多少 items 被标为 "high exposure"），而非 items 的相对排序。** 75/25 是一个合理的折中——如果需要更保守的 gating（更少 items 被 flag），可用 90/10；如果想更激进，用 50/50。

---
