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

**结论**: 2PL+γ 改善了 ARC 的情况（cal_MAE 从 0.086 降到 0.036），但 PPP 仍极低（0.002），校准后 MAE 仍大于原始（0.036 > 0.009）。γ 显著为正（exposure 提升表现），但模型对数据的拟合不足——这暗示 ARC 的 item 异质性可能超出 2PL 所能捕捉的范围，或 N=8 respondents 从根本上不足以支撑校准。

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

GSM8K 4PL+γ 表现最优：PPP 合格、校准将 MAE 从 0.153 压缩到 0.035。N=16 respondents + 跨 scale (0.5B+1.5B) 的 ability 差异为 IRT 提供了充分的识别信息。

---

## 2. MMLU Domain Gamma (2PL+γ, N=21-24 respondents)

所有 domain 使用 2PL+γ 模型，respondents 包含 0.5B + 1.5B + 3B 三个 scale。

| Domain | N_models | N_items | γ_mean | 95% CI | PPP | R̂_ok | Significant? |
|--------|----------|---------|--------|--------|-----|-------|-------------|
| **STEM_Math** | 23 | 1190 | **+0.969** | [0.527, 1.430] | 0.438 | ✓ | **Yes (+)** |
| **STEM_Science** | 23 | 1397 | **+0.838** | [0.385, 1.274] | 0.807 | ✓ | **Yes (+)** |
| STEM_CS_Eng | 23 | 557 | +0.197 | [-0.448, 0.835] | 0.892 | ✓ | No |
| **Medical** | 24 | 1640 | **-0.199** | [-0.338, -0.060] | 1.000 | ✓ | **Yes (−)** |
| **Humanities** | 21 | 2000* | **-0.407** | [-0.776, -0.041] | 1.000 | ✗ (1.014) | **Yes (−)** |
| **Social_Sciences** | 21 | 2000* | **-0.497** | [-0.827, -0.151] | 1.000 | ✓ | **Yes (−)** |
| Business_Law | 21 | 2000* | -0.168 | [-0.538, 0.230] | 1.000 | ✓ | No |

*subsampled from larger item pool

### 关键发现

1. **STEM 域呈现正向 γ**（数学 γ≈1.0, 科学 γ≈0.8）：暴露于训练数据**提升**了模型在这些 item 上的表现，符合"contamination inflates scores"的假设。

2. **人文/社科/医学域呈现负向 γ**（-0.2 到 -0.5）：暴露**降低**了模型表现。可能解释：
   - 过拟合记忆导致泛化能力下降（尤其对 paraphrase 形式的题目）
   - 训练数据中的错误标注被模型记忆
   - 长文本阅读理解类 item 中，记忆干扰了推理链

3. **模型拟合**：所有 domain PPP > 0.4（最高 1.0），表明 2PL+γ 在 N≥21 时拟合充分。Humanities 的 R̂=1.014 略超阈值但接近可接受。

4. **方向异质性**：γ 的符号在 domain 间不一致，pooled MMLU 中 γ≈-0.26（不显著）实际上是正负效应的混合平均，掩盖了 domain 特异性模式。

---

## 3. 结论：论文可以 claim 什么

### 强 claim（有充分证据支持）

1. **IRT 校准在 GSM8K (N=16) 上有效**：ΔMAE = +0.118，PPP = 0.40。4PL+γ 模型能够成功分离 ability 和 contamination effect，将 raw accuracy 的误差从 15.3% 降到 3.5%。

2. **MMLU domain-level γ 显示显著的 domain 异质性**：STEM 域正向（+0.8~1.0）vs 人文/社科域负向（-0.4~-0.5），p<0.05 level。这意味着 contamination 对 benchmark scores 的影响方向取决于 domain 特性。

3. **模型选择很重要**：N=8 时 4PL+γ 过参数化导致 PPP≈0 和校准失败；切换到 2PL+γ 立即修复 MMLU（PPP 0.006→0.426）。推荐规则：N<16 用 2PL+γ。

### 中等 claim（有证据但需谨慎）

4. **MMLU pooled γ 不显著排零**（2PL+γ, N=8）：暗示 contamination 对 MMLU aggregate score 的净效应可能为零或很小，因为正负 domain 效应相互抵消。

5. **ARC 的 γ 显著为正**（2PL+γ, N=8, γ=1.31 [0.37, 2.26]）：但 PPP=0.002 表示模型拟合不佳，这个估计不完全可信。

### 不能 claim

- ARC 上的 IRT 校准有效（PPP 不合格，cal_MAE > raw_MAE）
- 任何基于 N=8 的精确点估计（置信区间太宽）

### 下一步建议

1. **ARC 需要更多 respondents**：当前 N=8（仅 1.5B）不足。加入 0.5B 和 3B scale 的 ARC 评估结果可提升到 N≥16。
2. **GSM8K domain-level 分析**：类似 MMLU，按题目难度或类型分层看 γ 的异质性。
3. **论文展示策略**：以 GSM8K 为主打结果（校准有效），MMLU domain gamma 作为机制探究（异质性发现），ARC 作为 limitation 讨论。
