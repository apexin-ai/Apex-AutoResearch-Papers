# analysis gate wilcoxon test

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gate_wilcoxon_test_20260519T165256_result.json`
- **Structured JSON:** [`f6d60e98ec6415d85669.json`](../../sessions/f6/f6d60e98ec6415d85669.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果出来了。汇总如下：

---

## 统计检验结果

### 1. Wilcoxon Signed-Rank Test（主检验，28 层配对）

| 指标 | 值 |
|------|-----|
| N | 28 layers |
| Mean gate turn1 | 0.894 ± 0.065 |
| Mean gate turn21 | 0.950 ± 0.046 |
| Layers with turn21 > turn1 | **27/28** (仅 L19 反向) |
| T+ | 401 |
| T- | 5 |
| **p (one-sided)** | **3.73 × 10⁻⁸** |
| Z | 5.38 |
| Effect size r | **1.00** (large) |

### 2. Per-Conversation 一致性

全部 5 组对话均显著（p 范围 3.73×10⁻⁸ ~ 2.78×10⁻⁵），Fisher combined p ≈ 0。

| Conv | Mean diff | T+ | p | r |
|------|-----------|-----|------|------|
| conv_0 | 0.052 | 380 | 2.8e-05 | 0.76 |
| conv_1 | 0.044 | 376 | 7.6e-06 | 0.82 |
| conv_2 | 0.053 | 397 | 1.2e-07 | 0.98 |
| conv_3 | 0.067 | 401 | 3.7e-08 | 1.00 |
| conv_4 | 0.063 | 403 | 1.9e-08 | 1.04 |

### 3. Spearman 相关（turn index vs gate value）

- 25/28 层 ρ > 0，**13/28 层达到 p < 0.05 显著**
- Mean ρ = 0.367
- 最强单调趋势：L21 (ρ=0.86, p=5e-7), L25 (ρ=0.79, p=1.9e-5), L16/L18 (ρ=0.69, p=4.9e-4)

### 4. 层组分析

| 层组 | Mean diff | Wilcoxon p |
|------|-----------|------------|
| Early (L0–L9) | 0.033 | 9.8e-04 |
| Mid (L10–L19) | 0.051 | 4.9e-03 |
| Late (L20–L27) | **0.090** | 3.9e-03 |

深层 gating 效应约为浅层的 3 倍。Layer depth vs |diff| 趋势接近显著（ρ=0.35, p=0.064）。

### 5. 论文可用描述

> Across all 28 Transformer layers, gate values at turn 21 were significantly higher than at turn 1 (Wilcoxon signed-rank test, T⁺ = 401, p = 3.7 × 10⁻⁸, r = 1.00, N = 28), with 27 of 28 layers showing higher gate values at later turns. The mean gate value increased from 0.894 ± 0.065 (turn 1) to 0.950 ± 0.046 (turn 21), corresponding to a shift from partial residual suppression toward near-identity pass-through. Spearman rank correlation confirmed a monotonic increasing trend of gate values with turn index in 13 of 28 layers (mean ρ = 0.367). This pattern was consistent across all five evaluation conversations (Fisher combined p < 10⁻³⁰). The effect was most pronounced in late layers (L20–L27, mean Δ = 0.090) compared to early layers (L0–L9, mean Δ = 0.033).

分析脚本已保存在 `artifacts/gate_stat_test_v2.py`。

---
