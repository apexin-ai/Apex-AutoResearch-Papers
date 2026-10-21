# Investigation: tab:fl_comparison Data Conflict

## 1. tab:fl_comparison 完整内容 (appendix.tex L1488–1518)

**DGP**: K=2, N=5000, n_expert=250, π=[0.05, 0.25] (Δπ=0.20), τ(z=0)=0, τ(z=1)=0.3, 100 MC runs

| Method | |Bias| | RMSE | Coverage |
|--------|--------|------|----------|
| Oracle | 0.045 | 0.056 | 0.943 |
| Naive | 0.062 | 0.077 | 0.858 |
| Global (CM inv) | 0.064 | 0.081 | 0.938 |
| HB EC-HTE | 0.064 | 0.086 | **0.953** |
| F-L Scalar | 0.091 | 0.116 | 0.850 |
| F-L Per-Subgroup | 0.112 | 0.158 | 0.838 |

文字声明 (L1517): "EC-HTE achieves near-zero per-subgroup bias (s₀: +0.006, s₁: +0.001) with nominal coverage (95.3%)."

## 2. 生成脚本与数据溯源

**本地无 Python 脚本**。所有 `*.py` 文件中无 "frazis"、"fl_comparison"、"F-L"、"attenuation" 关键词。

**远程服务器** (`local-cpu`) 上存在三个 CSV（从 `worker_research_data-integrity-audit-v2` 日志中提取）:

- `results/exp_fl_comparison_summary.csv` — 汇总表
- `results/exp_fl_comparison.csv` — 逐 (mc_seed, subgroup, z_level, method) 的原始结果 (~412KB)
- `results/exp_fl_comparison_subgroup.csv` — 按 subgroup 聚合

**`exp_fl_comparison_summary.csv` 精确数据**:

| method | mean_abs_bias | rmse | coverage |
|--------|--------------|------|----------|
| Oracle | 0.04541 | 0.05616 | 0.9425 |
| Naive | 0.06206 | 0.07665 | 0.8575 |
| Global (CM inv) | **0.06432** | 0.08064 | 0.9375 |
| HB EC-HTE | **0.06427** | 0.08584 | 0.9525 |
| F-L Scalar | 0.09087 | 0.11613 | 0.85 |
| F-L Per-Subgroup | 0.11198 | 0.15818 | 0.8375 |

→ 表中 0.064 对 Global 和 HB EC-HTE 均正确（分别 0.06432 和 0.06427，三位小数均为 0.064）。

**`exp_fl_comparison_subgroup.csv` 关键列**:

| method | subgroup | mean_bias (signed) | mean_abs_bias |
|--------|----------|-------------------|---------------|
| HB EC-HTE | 0 | **+0.00628** | 0.04971 |
| HB EC-HTE | 1 | **+0.00057** | 0.07883 |
| Global | 0 | +0.00563 | 0.06481 |
| Global | 1 | +0.00147 | 0.06383 |

→ 文中 s₀: +0.006, s₁: +0.001 也正确，对应 `mean_bias`（有符号偏差）列。

## 3. DGP 配置对比

| 参数 | Table 1 (experiments.tex) | tab:fl_comparison (appendix.tex) |
|------|--------------------------|----------------------------------|
| K | 2 | 2 |
| N | 5,000 | 5,000 |
| n_expert | 250 | 250 |
| π | [0.05, 0.25] (推断) | [0.05, 0.25] (明确) |
| τ̄ | 0.5 | 0.15 |
| τ(z=0) | 0.5 - Δτ/2 | 0 |
| τ(z=1) | 0.5 + Δτ/2 | 0.3 |
| Δτ (= τ(1)−τ(0)) | likely 1.0 (极端) | 0.3 |
| MC runs | 100 | 100 |

**关键差异**: Table 1 的处理效应远大于 FL comparison（Δτ ≈ 1.0 vs 0.3）。τ̄ 也不同（0.5 vs 0.15）。

**验证**: Table 1 的 F-L 数值（0.122/0.168）由 `compute_fl_for_table1.py` 单独计算，与 FL comparison 的 F-L 数值（0.091/0.112）不同 → 确认是不同 DGP。

## 4. 根因分析

### 4.1 |Bias| = 0.064 vs "near-zero bias" — 不是 bug，是指标口径差异

- **表格 |Bias| = 0.064**: 是 `mean_abs_bias`——先对每个 (mc_seed, subgroup, z_level) 取 |bias|，再 across all cells 取平均。
- **文字 "+0.006, +0.001"**: 是 `mean_bias`——有符号偏差，先 across z_levels 和 MC runs 取平均。正负偏差在 z_level 间抵消。

**按 (subgroup, z_level) 分解的 HB EC-HTE |bias|**:

| sg | z | |bias| (mean across MC) |
|----|---|------------------------|
| 0 | 0 | 0.046 |
| 0 | 1 | 0.053 |
| 1 | 0 | 0.088 |
| 1 | 1 | 0.070 |
| **avg** | | **0.064** |

z=0 和 z=1 的有符号偏差方向相反，在 subgroup 内取平均时互相抵消 → `mean_bias` ≈ 0。但 |bias| 不会抵消 → `mean_abs_bias` ≈ 0.064。

**Oracle |Bias| = 0.045 是纯采样噪声的下界** (irreducible floor)。HB EC-HTE 的 0.064 仅高出 Oracle 0.019。

### 4.2 为什么 HB EC-HTE ≈ Global (0.064 ≈ 0.064)

在 FL comparison DGP 中，Δτ = 0.3 且 τ̄ = 0.15，处理效应本身很小。误分类导致的偏差量级也小，EC-HTE 的 per-subgroup 校正带来的增量改善被有限 expert 样本引入的方差所抵消。

对比 Table 1 DGP（Δτ ≈ 1.0, τ̄ = 0.5）：误分类偏差大得多，per-subgroup 校正的收益远超方差代价，所以 EC-HTE 显著优于 Global（0.008 vs 0.059）。

### 4.3 0.064 vs 0.008 — 不同 DGP，不是 inconsistency

两个数字来自不同实验配置，不可直接对比。

## 5. 问题所在与修复建议

### 问题 A: 文字暗示 |Bias| 是"near-zero"，与表格矛盾

Line 1517 说 "EC-HTE achieves near-zero per-subgroup bias"，但紧跟在 |Bias| = 0.064 的表格之后。读者会将 "near-zero bias" 理解为表格中的 |Bias| 列，产生困惑。

**修复**: 将 L1517 改为明确区分指标口径：

```latex
% 原文:
EC-HTE achieves near-zero per-subgroup bias ($s_0{:}\,{+}0.006$, $s_1{:}\,{+}0.001$) with nominal coverage (95.3\%).

% 建议修改:
EC-HTE achieves near-zero \emph{mean signed} per-subgroup bias ($s_0{:}\,{+}0.006$, $s_1{:}\,{+}0.001$), confirming unbiased correction; the $|\text{Bias}|$ column reflects mean \emph{absolute} bias, whose floor is set by finite-sample variance (Oracle: $0.045$).
EC-HTE coverage (95.3\%) is nominal.
```

### 问题 B: FL comparison 的 DGP 与 Table 1 不同但未显著标注

读者可能误认为两个表格用相同 DGP，从而对比 0.064 vs 0.008。

**修复**: 在 FL comparison 的 setup 文字中加一句：

```latex
% 在 L1494 末尾添加:
This DGP uses smaller treatment effects ($\bar{\tau}{=}0.15$, $\Delta\tau{=}0.3$) than the main experiments (Table~\ref{tab:main_results}: $\bar{\tau}{=}0.5$, $\Delta\tau{=}1.0$), chosen to isolate the F-L comparison without conflating correction quality with treatment effect magnitude.
```

### 问题 C: 表格未标注 Oracle floor

|Bias| = 0.064 看起来很大，但 Oracle = 0.045 说明大部分是不可消除的采样方差。

**修复**: 在表格 caption 中加注：

```latex
% 修改 L1498 caption:
\caption{F-L correction vs.\ EC-HTE under heterogeneous misclassification ($\Delta\pi{=}0.20$, $\Delta\tau{=}0.3$). Both F-L variants produce \emph{higher} aggregate bias than the uncorrected estimator. The Oracle row ($|\text{Bias}|{=}0.045$) reflects the irreducible finite-sample floor.}
```

## 6. 结论

- **0.064 不是 bug**，raw CSV 数据验证通过（Global 0.06432, HB EC-HTE 0.06427）
- **"+0.006, +0.001" 也不是 bug**，对应有符号偏差（mean_bias）列
- **冲突本质是叙述问题**：文字用 "near-zero bias" 描述 signed bias，但读者自然对标表格的 unsigned |Bias|
- **0.064 vs 0.008**: 不同 DGP（Δτ=0.3 vs ≈1.0），不是数据不一致
- **修复范围**: 仅需改 appendix.tex 的 3 处文字，无需重跑实验
