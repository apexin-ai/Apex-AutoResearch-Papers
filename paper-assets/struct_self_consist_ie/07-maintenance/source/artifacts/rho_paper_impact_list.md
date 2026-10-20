# ρ 值论文影响清单

**生成日期**: 2026-05-15
**数据源**: `analysis_unified_rho.json` (unified pipeline, gold-filtered)
**管道变化**: 排除 gold-empty 实例 + 统一 consistency.py FK/SJ + evaluation.py per_instance_f1

---

## 统一管道修正值摘要

| 实验 | Signal | 旧 Registry ρ | 统一 ρ | Δ | 说明 |
|------|--------|---------------|--------|---|------|
| LLaMA CoNLL N=16 seed42 | FK | 0.8095 | 0.4752 | **-0.334** | 排名反转 |
| LLaMA CoNLL N=16 seed42 | SJ | 0.1815 | 0.4836 | **+0.302** | 排名反转 |
| LLaMA CoNLL N=16 seed456 | FK | 0.8085 | 0.4690 | **-0.340** | 排名反转 |
| LLaMA CoNLL N=16 seed456 | SJ | 0.1895 | 0.4734 | **+0.284** | 排名反转 |
| Qwen SciERC N=16 seed456 NER | FK | 0.3448 | 0.2723 | **-0.073** | 幅度下降 |
| Qwen SciERC N=16 seed456 NER | SJ | 0.4134 | 0.4098 | -0.004 | 基本不变 |
| OOD CoNLL→SciERC | — | — | — | — | 已正确，无需变更 |

**关键发现**: LLaMA CoNLL N=16 旧管道中 FK ρ 严重虚高（0.81），SJ 严重偏低（0.18），统一管道修正后二者趋同（~0.48），**排名发生反转**。

---

## 需更新的 ρ 值位置

### 1. Table tab:robustness — LLaMA CoNLL N=16 3-seed section

**文件**: `sections/appendix.tex`, L52-57

**当前值**:
```
SJ:  0.463 ± 0.007
FK:  0.455 ± 0.006
EM:  0.460 ± 0.008
VC:  0.458 ± 0.003
LP:  0.310 ± 0.005
```

**统一管道 (2/3 seeds available)**:
| Signal | seed42 | seed456 | 论文3-seed mean | 差异 |
|--------|--------|---------|----------------|------|
| SJ | 0.4836 | 0.4734 | 0.463 | 论文偏低 ~0.015 |
| FK | 0.4752 | 0.4690 | 0.455 | 论文偏低 ~0.017 |
| EM | 0.4818 | 0.4752 | 0.460 | 论文偏低 ~0.018 |
| VC | 0.4746 | 0.4722 | 0.458 | 论文偏低 ~0.015 |
| LP | 0.3136 | 0.3099 | 0.310 | 基本一致 |

**问题**: 论文 3-seed mean 系统性低于统一管道两个 seed 的值（一致性信号低 ~0.015-0.018，LP 无差异）。推测论文使用了与统一管道不同的计算路径。**需用统一管道重算 3 seed 并更新此表。** seed123 的统一值不在 JSON 中，需补算。

**σ 值也需更新**: 当前 σ(SJ)=0.007，若统一 seed42=0.484、seed456=0.473，新 σ 取决于 seed123。

### 2. Table tab:robustness — Qwen SciERC N=16 section

**文件**: `sections/appendix.tex`, L47-50

**当前值**:
```
SJ N=16: 0.411 (3-seed mean, footnote †)
FK N=16: 0.283
```

**统一管道 seed456**:
- SJ: 0.4098 (vs 旧 registry 0.4134, Δ=-0.004, 几乎不变)
- FK: 0.2723 (vs 旧 registry 0.3448, **Δ=-0.073**)

**影响**: FK 3-seed mean 可能从 0.283 降至 ~0.259（估算: 若 seed456 从 0.345→0.272，其他 2 seed 不变）。需用统一管道重算全部 3 seed。SJ 基本不受影响。

### 3. Table tab:n-scaling — Qwen SciERC 3-seed

**文件**: `sections/appendix.tex`, L582-596

**当前值** (受影响行):
```
FK: N=8: 0.2536, N=16: 0.2833, Δ: +0.0297
```

**影响**: 若 FK N=16 3-seed mean 降至 ~0.259，则:
- FK Δ(N=8→N=16) 从 +0.030 降至 **~+0.005**
- FK N-scaling 从"弱正"变为"近乎零"

其他行 (SJ, VC, EM, LP) 受影响较小。需重算。

### 4. Table tab:quality_estimation (Table 1) — CoNLL (LLaMA) N=8

**文件**: `sections/experiments.tex`, L38-42

**当前值**: VC .426, SJ .431, FK .428, EM .431, LP .307

**状态**: ⚠️ **统一 JSON 不含 N=8 数据**。但同一管道问题（gold-empty filtering + FK/SJ 计算）同样影响 N=8 实验。**需用统一管道重算 N=8 LLaMA CoNLL 并验证**。

> 若 N=8 也出现 FK↓SJ↑ 的趋势，Table 1 数值和排名可能变化。

### 5. Table tab:sigma-comparison

**文件**: `sections/appendix.tex`, L619-637

LLaMA CoNLL 不在此表（此表是 Qwen SciERC），但 Qwen SciERC N=16 σ 值受 seed456 FK 变化影响。需重算。

### 6. Table tab:ranking-stability (Kendall's W)

**文件**: `sections/appendix.tex`, L599-615

Qwen NER N=16 行: 当前 W=0.956, consensus "SJ ≈ VC > EM > FK > LP"。若 FK N=16 下降，排名可能变为 "SJ ≈ VC > EM > LP > FK"（FK 和 LP 可能交换）。需验证。

---

## 正文引用

### experiments.tex

| 行号 | 原文 | 影响 | 优先级 |
|------|------|------|--------|
| L71 | "SJ achieves ρ=0.436 (Qwen) vs. 0.431 (LLaMA) on CoNLL (Δ=0.005, within 3-seed σ≈0.007)" | N=8 LLaMA CoNLL SJ=0.431 需验证；σ≈0.007 可能变化 | ⚠️ 需 N=8 数据 |
| L140 | "structural signals maintaining their advantage over LP across all NER settings (Δρ=+0.135 to +0.175)" | 此 Δρ 范围源自 N=16 各配置。统一管道下 LLaMA CoNLL SJ-LP Δ≈+0.170 (seed42)，可能使范围上移 | 中 |

### appendix.tex

| 行号 | 原文 | 影响 | 优先级 |
|------|------|------|--------|
| L53-54 | "SJ ρ=0.463±0.007 vs. LP 0.310±0.005, Δ=+0.153" | 统一管道 SJ 更高，Δ 增大至 ~+0.170 | 高 |
| L77 | "LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain Δρ≈+0.030 (range: +0.027 to +0.032) while LP gains only +0.003" | 依赖 N=8 和 N=16 差值。若 N=16 升高而 N=8 不变，Δρ 增大；若 N=8 也升高，可能抵消 | ⚠️ 需 N=8 数据 |
| L78-79 | "FK N-scaling is inconsistent: degradation on SciERC (-0.007 to -0.019) but improvement on CoNLL with LLaMA (+0.027)" | SciERC FK N-scaling Δ 可能从+0.030 变为+0.005，且 CoNLL 的+0.027 可能变化 | 高 |
| L84 | "LLaMA SciERC NER (SJ ρ=0.325±0.021, FK ρ=0.256±0.024)" | LLaMA SciERC N=8 — 不在 JSON 中，但可能受同一管道影响 | ⚠️ 需验证 |
| L85-86 | "SJ achieves ρ=0.431 (LLaMA) vs. 0.436 (Qwen), Δ=0.005" | N=8 LLaMA CoNLL 值 | ⚠️ 需 N=8 数据 |
| L86 | "LLaMA CoNLL 3-seed (SJ ρ=0.463±0.007 vs. LP 0.310±0.005, Δ=+0.153)" | 同 L53-54 | 高 |
| L138 | "CoNLL LLaMA 3-seed (ρ=0.462)" [conditional EM] | 条件过滤值，受管道变化影响 | 高 |
| L191-193 | "SJ already achieves ρ=0.431 on LLaMA CoNLL (vs. LP ρ=0.307, Δ=+0.124), and the gap widens at N=16 (Δ=+0.153)" | N=8 + N=16 混合引用 | 高 |
| L199 | "VC achieves the largest gain over greedy (+0.28 pp, p=0.003–0.027 across 3 seeds)" | 选择 F1 非 ρ，但若实例集变化，选择结果可能不同 | 中 |

### sections/discussion.tex

| 行号 | 原文 | 影响 | 优先级 |
|------|------|------|--------|
| L6 | "At higher sample sizes (N=16), SJ converges to comparable NER performance with VC (Δ=0.002) with lower cross-seed variance (σ=0.010 vs. 0.026)" | SJ/VC N=16 值变化 → Δ 和 σ 需重算 | 中 |

### sections/limitations.tex

| 行号 | 原文 | 影响 | 优先级 |
|------|------|------|--------|
| L15 | "On CoNLL with LLaMA, the SJ-FK gap is only 0.003 (ρ=0.431 vs. 0.428)" | N=8 值。统一管道 N=16 gap≈0.009 (seed42)。若 N=8 也扩大，此 claim 需修改 | ⚠️ 需 N=8 数据 |

---

## 排名变化

### LLaMA CoNLL N=16 (最重要)

**旧 Registry 排名**: FK (0.81) >> SJ (0.18) — FK 绝对主导
**论文当前排名**: SJ (0.463) > EM (0.460) > VC (0.458) > FK (0.455) > LP (0.310) — SJ 略高于 FK
**统一管道排名 (seed42)**: SJ (0.484) > EM (0.482) > FK (0.475) ≈ VC (0.475) > LP (0.314) — SJ > FK，但 FK 上升
**统一管道排名 (seed456)**: EM (0.475) > SJ (0.473) > VC (0.472) > FK (0.469) > LP (0.310) — 四信号趋同

**关键变化**:
1. 旧 registry → 统一: **FK/SJ 排名完全反转**（FK 从第一降至中间，SJ 从最后升至顶部）
2. 论文 → 统一: 排名方向一致（SJ ≥ FK），但**绝对值系统性偏低 ~0.015**
3. 统一管道下四个一致性信号更加趋同（range 0.009 vs 论文的 0.008），LP 差距更大

### Qwen SciERC N=16 NER

**旧 Registry**: FK=0.345, SJ=0.413
**统一管道 seed456**: FK=0.272, SJ=0.410

**排名影响**: FK 从 SJ 的 83% 降至 66%。在 3-seed 排名中，FK 可能从 #4 降至 #5（与 LP 交换）。

---

## 核心 Claim 影响评估

### 1. Correlation-Selection Gap (核心贡献)

**Claim**: "ρ up to 0.38, AUROC up to 0.75, yet none significantly improves sample selection"

**影响**: ✅ **不受影响**。此 claim 基于 SciERC N=8 seed=42 结果（VC ρ=0.379），不在本次修正范围内。选择实验也在 SciERC N=8 上进行。

### 2. Difficulty-Dependent Signal Complementarity

**Claim**: "EM leads on easy tasks (CoNLL), SJ on hard tasks (SciERC)"

**影响**: ⚠️ **需验证 N=8 CoNLL LLaMA**。
- CoNLL Qwen N=8: EM=0.451 明确领先 → 不受影响
- CoNLL LLaMA N=8: EM=0.431 = SJ=0.431（并列） → 若统一管道下排名变化，claim 需调整措辞
- SciERC N=8: VC/SJ 领先 → 不受影响

### 3. Signal Stability Across Model Families

**Claim**: "SJ achieves ρ=0.436 (Qwen) vs. 0.431 (LLaMA) on CoNLL (Δ=0.005)"

**影响**: ⚠️ **需 N=8 统一值**。若 LLaMA CoNLL N=8 SJ 值变化，Δ 可能不再是 0.005。但 claim 的方向（跨模型稳定）可能仍成立。

### 4. Structural Advantage Over LP

**Claim**: "Δρ=+0.135 to +0.175"

**影响**: ✅ **加强**。统一管道下 SJ-LP 差距更大（N=16 seed42: 0.484-0.314=+0.170），structural advantage 更明显。

### 5. "Uniform N-Scaling" on LLaMA CoNLL

**Claim**: "all four consistency signals gain Δρ≈+0.030"

**影响**: ⚠️ **需全面重算**。N=16 值升高但 N=8 值未知。若 N=8 也升高，Δ 可能不变；若只有 N=16 升高，Δ 增大。

### 6. FK N-Scaling on SciERC

**Claim**: FK N=16 Δ=+0.030 (tab:n-scaling)

**影响**: ❌ **可能失效**。seed456 FK 从 0.345 降至 0.272，3-seed mean N=16 FK 可能降至 ~0.259，使 Δ 从 +0.030 降至 +0.005。相关文本 "FK N-scaling is inconsistent" 的具体数值需更新。

### 7. SJ-FK Gap on CoNLL (Limitations)

**Claim**: "SJ-FK gap is only 0.003 (ρ=0.431 vs. 0.428)"

**影响**: ⚠️ **需 N=8 验证**。统一 N=16 gap=0.009 (seed42)。若 N=8 gap 也扩大，此 limitation 的具体数值需更新，但方向（gap 较小）可能仍成立。

### 8. 3-Seed σ Values

**Claim**: "σ≤0.026" (multiseed stability)

**影响**: ⚠️ σ 值会随 ρ 值变化。需用统一管道重算所有 3-seed 统计量。

---

## 未覆盖的缺口

以下实验/配置受同一管道问题影响，但统一 JSON 未提供修正值:

1. **LLaMA CoNLL N=8** (Table 1, 多处正文引用) — 697 gold-empty 实例同样存在
2. **LLaMA CoNLL N=16 seed123** — 3-seed mean 需要全部 3 个 seed
3. **Qwen SciERC N=16 seed42 和 seed123** — 3-seed mean 需要全部 3 个 seed
4. **Qwen CoNLL N=8 / N=16** — 同一 CoNLL 数据集，可能受影响
5. **WNUT-17** — 有 gold-empty 实例（JSON 中 WNUT 未出现，需确认）
6. **LLaMA SciERC N=8** (appendix L84) — 可能受影响
7. **条件过滤值** (conditional ρ) — JSON 仅提供部分 conditional 值
8. **AUROC 值** — JSON 提供了统一 AUROC，但论文中的 AUROC 主要在 Table 1 (N=8)，无法直接比对
9. **Selection F1 值** — 管道变化可能影响实例集，间接影响选择实验结果

---

## 建议行动

### 立即执行 (高优先级)
1. **重算全部 3 seed 的统一 ρ** for LLaMA CoNLL N=16 → 更新 tab:robustness 和所有引用
2. **重算全部 3 seed 的统一 ρ** for Qwen SciERC N=16 → 更新 tab:robustness 和 tab:n-scaling
3. **重算 LLaMA CoNLL N=8 统一 ρ** → 更新 Table 1 和所有 N=8 引用

### 随后更新 (中优先级)
4. 更新所有衍生统计量 (Δρ, σ, Kendall's W, conditional ρ)
5. 重跑 N-scaling 分析 (tab:n-scaling)，特别关注 FK
6. 验证 AUROC 值是否也受影响
7. 检查 selection F1 是否需要重算（实例集 n 是否变化）

### 最后检查 (低优先级)
8. 审查所有正文 claim 是否仍与更新后数值一致
9. 更新 Figure fig_signal_heatmap（若 heatmap 包含 N=16 数据）
10. 确认 WNUT-17 不受影响（或补算）

---

## 核心结论

**论文的核心贡献（correlation-selection gap）不受影响**，因为它基于 SciERC N=8 实验，不在本次修正范围内。

主要影响集中在:
- **Appendix robustness 分析** (LLaMA CoNLL N=16 和 Qwen SciERC N=16)
- **N-scaling 分析** (FK scaling 可能失效)
- **跨模型稳定性的具体数值** (N=8 LLaMA CoNLL 需验证)

论文的 claim 方向大多不变，但**具体数值需全面更新**。唯一可能受实质影响的是 FK N-scaling 的 claim 和 SJ-FK gap 的 limitations 描述。
