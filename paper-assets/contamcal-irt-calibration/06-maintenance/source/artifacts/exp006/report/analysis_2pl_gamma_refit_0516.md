# Pooled IRT 2PL+γ Refit Analysis (2026-05-16)

## 1. MMLU/ARC: 2PL+γ vs 4PL+γ 对比

### Background
Pooled IRT N=25 v2 中 MMLU 和 ARC 仅有 N=8 respondents（均为 1.5B scale），使用 4PL+γ（含 guessing c 和 upper-bound d 参数）导致过参数化。
本次用 2PL+γ（仅 discrimination a + difficulty b + exposure γ）重新拟合。

### MMLU (N=8 respondents, 300 items)

| Metric | 4PL+γ | 2PL+γ | Δ |
|--------|--------|--------|---|
| **PPP** | 0.006 | **0.426** | +0.420 (从 bad → adequate) |
| γ_mean | -0.404 | -0.259 | — |
| γ 95% CI | [-1.836, 1.071] | [-1.582, 1.021] | — |
| CI excludes 0? | No | No | — |
| R̂_max | 1.008 | 1.009 | Both OK |
| ESS_min | 1483 | 1539 | Both OK |
| Divergences | 0 | 0 | — |
| raw_MAE | 0.0078 | 0.0078 | — |
| **cal_MAE** | 0.0214 | **0.0023** | -0.019 |
| **ΔMAE** | -0.0136 | **+0.0055** | 方向逆转 |

**结论**: 2PL+γ 完全解决了 MMLU 过参数化问题。PPP 从 0.006 提升到 0.426（模型拟合良好），校准后 MAE 从 0.0214 降到 0.0023（优于原始 0.0078）。γ 不显著排零，表明 MMLU exposure 对 1.5B 模型的 item-level 影响不可与 ability 区分。

### ARC Challenge (N=8 respondents, 300 items)

| Metric | 4PL+γ | 2PL+γ | Δ |
|--------|--------|--------|---|
| **PPP** | 0.000 | **0.002** | +0.002 (仍不合格) |
| γ_mean | 1.513 | 1.307 | — |
| γ 95% CI | [0.234, 2.866] | [0.368, 2.262] | 收窄 |
| CI excludes 0? | Yes | Yes | — |
| R̂_max | 1.007 | 1.007 | Both OK |
| ESS_min | 1314 | 1398 | Both OK |
| Divergences | 0 | 0 | — |
| raw_MAE | 0.0088 | 0.0088 | — |
| **cal_MAE** | 0.0857 | **0.0362** | -0.050 |
| **ΔMAE** | -0.077 | **-0.0275** | 恶化幅度减小 |

**结论**: 2PL+γ 改善了 ARC 的情况（cal_MAE 从 0.086 降到 0.036），但 PPP 仍极低（0.002），校准后 MAE 仍大于原始（0.036 > 0.009）。γ 显著为正（exposure 提升表现），但模型对数据的拟合不足。

### GSM8K (N=16 respondents, 4PL+γ — 保持不变)

| Metric | Value |
|--------|-------|
| PPP | **0.398** (good) |
| γ_mean | 0.142 |
| γ 95% CI | [-0.749, 0.962] |
| CI excludes 0? | No |
| R̂_max | 1.007 |
| ESS_min | 1597 |
| raw_MAE | 0.1525 |
| cal_MAE | 0.0348 |
| **ΔMAE** | **+0.118** (大幅改善) |

---

## 2. MMLU Domain Gamma (2PL+γ, N=21-24 respondents)

| Domain | N_models | N_items | γ_mean | 95% CI | PPP | R̂_ok | Significant? |
|--------|----------|---------|--------|--------|-----|-------|-------------|
| **STEM_Math** | 23 | 1190 | **+0.969** | [0.527, 1.430] | 0.438 | ✓ | **Yes (+)** |
| **STEM_Science** | 23 | 1397 | **+0.838** | [0.385, 1.274] | 0.807 | ✓ | **Yes (+)** |
| STEM_CS_Eng | 23 | 557 | +0.197 | [-0.448, 0.835] | 0.892 | ✓ | No |
| **Medical** | 24 | 1640 | **-0.199** | [-0.338, -0.060] | 1.000 | ✓ | **Yes (−)** |
| **Humanities** | 21 | 2000* | **-0.407** | [-0.776, -0.041] | 1.000 | ✗ (1.014) | **Yes (−)** |
| **Social_Sciences** | 21 | 2000* | **-0.497** | [-0.827, -0.151] | 1.000 | ✓ | **Yes (−)** |
| Business_Law | 21 | 2000* | -0.168 | [-0.538, 0.230] | 1.000 | ✓ | No |

### 关键发现

1. **STEM 域正向 γ**（Math γ≈1.0, Science γ≈0.8）：exposure 提升表现，符合"contamination inflates scores"。
2. **人文/社科/医学域负向 γ**（-0.2 to -0.5）：exposure 降低表现。
3. **所有 domain PPP > 0.4**，2PL+γ 在 N≥21 时拟合充分。
4. **Pooled MMLU γ≈-0.26（不显著）是正负效应混合平均。**

---

## 3. 结论：论文可以 claim 什么

### 强 claim
1. IRT 校准在 GSM8K (N=16) 上有效：ΔMAE = +0.118，PPP = 0.40
2. MMLU domain-level γ 显示显著异质性：STEM (+) vs Humanities/Social (−)
3. 模型选择规则：N<16 用 2PL+γ，N≥16 MCQ 可用 4PL+γ

### 中等 claim
4. MMLU pooled γ 不显著排零，contamination 净效应可能≈0
5. ARC γ 显著为正但模型拟合不佳

### 不能 claim
- ARC IRT 校准有效（PPP=0.002）
- 基于 N=8 的精确点估计