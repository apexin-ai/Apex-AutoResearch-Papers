# analysis 23config regression

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_23config_regression_20260519T072221_result.json`
- **Structured JSON:** [`260682fbc2d2c5b35732.json`](../../sessions/26/260682fbc2d2c5b35732.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果保存在 `output/decomposition_regression/regression_results.json`。

---

## 汇报

### 23 Configs 完整列表

| Config | d (%) | Δ_oracle (pp) | ρ_within | Predicted (pp) | Actual (pp) |
|--------|------:|------:|------:|------:|------:|
| SciERC s42 | 17.8 | +13.19 | +0.18 | +1.95 | +0.61 |
| CoNLL s42 | 58.0 | +4.24 | +0.35 | +0.63 | -0.81 |
| FewNERD s42 | 14.4 | +12.09 | +0.52 | +5.42 | +1.32 |
| SciERC s123 | 17.2 | +13.48 | +0.18 | +1.96 | -0.21 |
| SciERC s456 | 20.4 | +12.50 | +0.19 | +1.88 | -0.28 |
| CoNLL s123 | 63.0 | +3.99 | +0.31 | +0.46 | -0.77 |
| CoNLL s456 | 62.9 | +3.84 | +0.32 | +0.45 | -0.73 |
| FewNERD s123 | 13.1 | +12.92 | +0.51 | +5.70 | +1.44 |
| FewNERD s456 | 12.1 | +12.65 | +0.51 | +5.65 | +1.37 |
| LLaMA SciERC s42 | 24.9 | +12.88 | +0.15 | +1.49 | +0.19 |
| LLaMA SciERC s123 | 26.6 | +12.04 | +0.16 | +1.41 | -0.38 |
| LLaMA SciERC s456 | 27.4 | +11.73 | +0.18 | +1.50 | +0.10 |
| LLaMA CoNLL s42 | 89.4 | +2.11 | +0.20 | +0.05 | +0.14 |
| LLaMA CoNLL s123 | 89.3 | +2.00 | +0.23 | +0.05 | +0.11 |
| LLaMA CoNLL s456 | 89.4 | +2.06 | +0.23 | +0.05 | +0.02 |
| 3-epoch | 6.4 | +14.97 | +0.27 | +3.82 | -1.18 |
| 10-epoch | 47.8 | +8.64 | +0.07 | +0.31 | +0.99 |
| rank=8 | 7.2 | +16.01 | +0.24 | +3.63 | -0.47 |
| T=0.5 | 41.4 | +9.05 | +0.13 | +0.70 | -0.23 |
| T=0.8 | 23.8 | +12.51 | +0.16 | +1.57 | +0.03 |
| T=1.2 | 14.9 | +14.63 | +0.23 | +2.84 | -0.61 |
| 4B SciERC | 10.4 | +13.02 | +0.19 | +2.21 | -2.23 |
| 4B CoNLL | 90.6 | +1.70 | +0.24 | +0.04 | +0.09 |

### Full-sample 统计

| Metric | Value |
|--------|-------|
| Spearman ρ | 0.074 (p=0.737) |
| Pearson r | 0.358 (p=0.094) |
| R² (raw formula) | **-8.53** |
| R² (calibrated OLS) | 0.128 |
| MAE | 2.04 pp |

### Leave-one-dataset-out CV R²

全部为大幅负值（-1.2 到 -2933），公式在交叉验证中完全无预测力。

### 各因子单独与 actual ΔF1 的相关性

- (1-d): Spearman ρ = -0.05 (p=0.81)
- Δ_oracle: Spearman ρ = -0.11 (p=0.61)
- ρ_within: Spearman ρ = -0.04 (p=0.86), Pearson r = +0.38 (p=0.07)
- (1-d)×Δ_oracle: Spearman ρ = -0.11 (p=0.62)

### 结论

**分解公式 ΔF1 ≈ (1-d) × Δ_oracle × ρ_within 不具备预测力。**

核心问题：
1. **系统性高估**：predicted 始终为正（因 ρ_within > 0），但 23 configs 中 13 个 actual ΔF1 为负
2. **FewNERD 极端过估**：predicted ~5.5 pp vs actual ~1.4 pp（4x 偏差）
3. **极端失配**：3-epoch (pred +3.82, actual -1.18)、rank=8 (pred +3.63, actual -0.47)、4B SciERC (pred +2.21, actual -2.23)
4. **三因子无单独预测力**：没有任何一个因子与 actual ΔF1 有显著 Spearman 相关
5. 唯一略有信号的是 ρ_within 的 Pearson r = 0.38 (p=0.07)，但这不足以支撑公式

根本原因：within-instance Spearman ρ（仅 8 samples）的正均值不代表 LP 选择能有效捕获 oracle gap。ρ_within 作为乘法因子的假设在小样本下不成立。

---
