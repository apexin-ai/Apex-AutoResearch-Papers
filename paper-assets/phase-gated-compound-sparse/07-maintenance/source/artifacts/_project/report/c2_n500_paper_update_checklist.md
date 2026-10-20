# C2 n=500 论文更新清单

> 当 C2 n=500 实验（DeepSeek 8 conditions + Qwen 8 conditions）全部完成后，用此清单逐项替换论文中所有 n=50 数据。
> 数据来源均在服务器 `/root/autodl-tmp/pacs/analysis_output/` 下。
> **原则**：DeepSeek 和 Qwen 数值绝对值差 ~5×，不可混用；所有数值精确替换，不可近似。

---

## 1. 样本量文本替换（全局搜索 "50"）

| 文件 | 行号 | 当前文本 | 替换为 | 类型 |
|------|------|---------|--------|------|
| abstract.tex | 6 | `50 MATH-500 problems` | `500 MATH-500 problems` | 文本 |
| methodology.tex | 10 | `50 problems stratified from MATH-500` | `500 problems from MATH-500` | 文本 |
| results.tex | 13 | `$n{=}50$ MATH-500 problems` (Table 1 caption) | `$n{=}500$` | 文本 |
| results.tex | 34 | `medians across 50 problems` (Table 2 caption) | `medians across 500 problems` | 文本 |
| appendix_moved.tex | 26 | `$n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek)` | n=500 后的有效样本量（需从数据计算） | 文本 |
| appendix_moved.tex | 73 | `$n{=}49$, $10{,}000$ permutations` (Table permutation caption) | 新 n 值 | 文本 |
| appendix_disc_analysis.tex | 45 | `$n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded)` | 新排除数/有效 n | 文本 |

---

## 2. Tables

### Table 1: Aggregate II (tab:aggregate-ii) — results.tex L10-23

| 行/列 | 当前值 | 数据来源 | 更新类型 |
|--------|--------|----------|----------|
| Importance s=0.15 | 0.39 | experiment_summary_table.json → DS imp s015 median_diff | 数值替换 |
| Importance s=0.20 | 1.48 | experiment_summary_table.json → DS imp s020 median_diff | 数值替换 |
| Importance s=0.25 | 7.16 | experiment_summary_table.json → DS imp s025 median_diff | 数值替换 |
| Importance s=0.30 | 14.59 | experiment_summary_table.json → DS imp s030 median_diff | 数值替换 |
| Random s=0.15 | 0.01 | experiment_summary_table.json → DS rand s015 median_diff | 数值替换 |
| Random s=0.20 | −0.02 | experiment_summary_table.json → DS rand s020 median_diff | 数值替换 |
| Random s=0.25 | 0.54 | experiment_summary_table.json → DS rand s025 median_diff | 数值替换 |
| Random s=0.30 | 1.54 | experiment_summary_table.json → DS rand s030 median_diff | 数值替换 |
| 正文 L8 | `$0.39$...$14.59$...37×` | 同上，37× = 14.59/0.39 需重算 | 数值+比率 |
| 正文 L8 | `$-0.02$ to $1.54$` | random range 需从新数据取 | 数值替换 |

### Table 2: Per-phase II breakdown (tab:main-results) — results.tex L31-53

| 行 | II_high | II_mid | II_low | Δ | G | 数据来源 |
|----|---------|--------|--------|---|---|----------|
| 0.15 Imp | 0.006 | 0.081 | 0.398 | 0.39 | 69 | DS imp s015 per-phase medians |
| 0.15 Rand | 0.093 | 0.097 | 0.103 | 0.01 | 1.1 | DS rand s015 per-phase medians |
| 0.20 Imp | 0.015 | 0.203 | 1.496 | 1.48 | 103 | DS imp s020 per-phase medians |
| 0.20 Rand | 0.292 | 0.350 | 0.276 | −0.02 | 0.9 | DS rand s020 per-phase medians |
| 0.25 Imp | 0.032 | 1.118 | 7.196 | 7.16 | 222 | DS imp s025 per-phase medians |
| 0.25 Rand | 0.818 | 0.932 | 1.363 | 0.54 | 1.7 | DS rand s025 per-phase medians |
| 0.30 Imp | 0.053 | 2.283 | 14.639 | 14.59 | 274 | DS imp s030 per-phase medians |
| 0.30 Rand | 2.503 | 2.592 | 4.041 | 1.54 | 1.6 | DS rand s030 per-phase medians |

数据来源：`experiment_summary_table.json` 中各 condition 的 `median_low`, `median_mid`, `median_high`。

### Table 3: Cohen's d (tab:cohens-d) — results.tex L81-97

| 行 | DS d_z | DS Δ̃ [CI] | QW d_z | QW Δ̃ [CI] | 数据来源 |
|----|--------|-----------|--------|-----------|----------|
| s=0.15 | 0.44 | 0.32 [0.20, 0.47] | 0.28 | 0.05 [−0.01, 0.11]^ns | cohens_d_bf16.json / cohens_d_bf16_qwen.json |
| s=0.20 | 0.52 | 1.15 [0.66, 1.26] | 0.55 | 0.21 [0.07, 0.40] | 同上 |
| s=0.25 | 0.68 | 3.97 [2.83, 5.29] | 0.89 | 1.11 [0.61, 1.47] | 同上 |
| s=0.30 | 0.80 | 9.94 [8.39, 16.65] | 1.02 | 2.62 [1.72, 3.65] | 同上 |

**注意**：n=500 后 CI 会显著收窄（~√10 倍）。QW s015 的 `ns` 标注取决于 CI 是否仍含零。

### Table: Cross-model comparison (tab:cross-model) — appendix_moved.tex L30-43

| 行 | 当前值 | 数据来源 |
|----|--------|----------|
| DeepSeek s015/s020/s025/s030 | 0.39 / 1.48 / 7.16 / 14.59 | experiment_summary_table.json DS imp |
| Qwen s015/s020/s025/s030 | 0.04 / 0.23 / 1.27 / 2.94 | experiment_summary_table.json QW imp |

### Table: Permutation test (tab:permutation) — appendix_moved.tex L70-85

| s | Observed Δ̃ | 95% CI | p_Bonf | 数据来源 |
|---|-----------|--------|--------|----------|
| 0.15 | 0.37 | [0.19, 0.62] | 0.0032 | permutation_test_results.json |
| 0.20 | 0.97 | [0.69, 1.49] | <0.001 | 同上 |
| 0.25 | 3.34 | [1.66, 6.64] | <0.001 | 同上 |
| 0.30 | 9.85 | [6.70, 16.29] | <0.001 | 同上 |

### Table: Discrimination metrics (tab:discrimination-metrics-full) — appendix_moved.tex L103-123

| Model | s | ΔGini | ΔCV | 数据来源 |
|-------|---|-------|-----|----------|
| DS 0.15 | −0.030 | −0.56 | c4_entropy_deepseek |
| DS 0.20 | −0.040 | −0.77 | 同上 |
| DS 0.25 | −0.065 | −1.29 | 同上 |
| DS 0.30 | −0.081 | −1.66 | 同上 |
| QW 0.15 | −0.010 | −0.05 | c4_entropy_qwen |
| QW 0.20 | −0.012 | −0.21 | 同上 |
| QW 0.25 | −0.010 | −1.49 | 同上 |
| QW 0.30 | −0.020 | −1.14 | 同上 |

**注意**：C4 entropy 分析需要用 n=500 数据重跑 `analysis/entropy_analysis.py`。

### Table: Entropy deltas (tab:entropy-deltas) — appendix_moved.tex L143-163

| Model | s | ΔH | 数据来源 |
|-------|---|----|----------|
| DS 0.15 | −0.040 | c4_entropy_deepseek |
| DS 0.20 | −0.047 | 同上 |
| DS 0.25 | −0.045 | 同上 |
| DS 0.30 | −0.044 | 同上 |
| QW 0.15 | −0.073 | c4_entropy_qwen |
| QW 0.20 | −0.076 | 同上 |
| QW 0.25 | +0.045 | 同上 |
| QW 0.30 | −0.007 | 同上 |

---

## 3. Figures

| Figure | 文件 | 数据来源 | 需更新内容 |
|--------|------|----------|-----------|
| Fig 1 (fig:hero) — fig1_dose_response.pdf | results.tex L55-60 | experiment_summary_table.json G values | G 曲线数据点 + caption 中 `$69{\times}$ to $274{\times}$` |
| Fig 2 — fig2_cohens_d (如存在) | 位置待定 | cohens_d_bf16.json, cohens_d_bf16_qwen.json | Cohen's d 森林图 |
| Fig 3 (fig:crossover) — fig3_crossover.pdf | appendix_moved.tex L13-18 | experiment_summary_table.json DS s025 | 柱状图数据 + caption 中 `$5.3{\times}$` |
| Fig 4 (fig:permtest-forest) — fig4_bootstrap.pdf | appendix_moved.tex L87-92 | permutation_test_results.json | CI 横条 + 点估计值 |
| Fig 5 (fig:cross-model) — fig5_crossmodel.pdf | appendix_moved.tex L46-50 | experiment_summary_table.json DS+QW imp | 双曲线数据点 + caption 中 `one-fifth` 比例 |

**图表生成脚本**（服务器端）：
- `/root/autodl-tmp/pacs/analysis/generate_paper_figures.py` — fig4, fig5
- `/root/autodl-tmp/pacs/analysis/generate_summary_table.py` — experiment_summary_table.json
- `/root/autodl-tmp/pacs/analysis/cross_model_analysis.py` — cross_model_analysis.json
- `/root/autodl-tmp/pacs/analysis/compute_cohens_d.py` — cohens_d_bf16.json

**更新流程**：先用 n=500 profiling 数据重跑 `generate_summary_table.py`，再重跑各分析脚本，最后重新生成所有图表 PDF。

---

## 4. 正文中的内联统计声明

### abstract.tex

| 行 | 当前文本 | 数据来源 | 类型 |
|----|---------|----------|------|
| 7 | `median Interaction Index difference...increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |
| 7 | `paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)` | cohens_d_bf16.json | 数值 |
| 7 | `$p < 0.005$ at all four sparsity levels` | permutation_test_results.json | 阈值判断 |
| 8 | `7/8 conditions` | 重新统计 random PASS/FAIL | 计数 |
| 8 | `Qwen $s{=}0.30$, $p{=}0.012$` | QW rand s030 permutation test | 数值 |
| 8 | `$d_z{=}{-}0.04$` | QW rand s030 Cohen's d | 数值 |
| 9 | `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` | DS imp/rand s025 high-phase medians | 数值 |
| 9 | `$\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$` | DS imp/rand s025 low-phase medians | 数值 |
| 10 | `$d_z \geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |
| 10 | `Spearman $\rho = 1.0$` | cross_model_analysis.json | 数值 |
| 10 | `gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |

### introduction.tex

| 行 | 当前文本 | 数据来源 | 类型 |
|----|---------|----------|------|
| 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | experiment_summary_table.json DS imp | 数值 |
| 14 | `$d_z$: $0.44 \to 0.80$` | cohens_d_bf16.json | 数值 |
| 14 | `Bonferroni-corrected $p < 0.005$ at all levels` | permutation_test_results.json | 阈值判断 |
| 15 | `$d_z \geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |
| 16 | `7/8 conditions non-significant` | 重新统计 random PASS/FAIL | 计数 |

### methodology.tex

| 行 | 当前文本 | 数据来源 | 类型 |
|----|---------|----------|------|
| 18 | `mean/median ratios up to 43:1` | 从 n=500 数据重新计算 | 数值 |
| 22 | `$p_{\text{Bonf}} < 0.005$ at every sparsity level` | permutation_test_results.json | 阈值判断 |

### results.tex (正文段落)

| 行 | 当前文本 | 数据来源 | 类型 |
|----|---------|----------|------|
| 8 | `$37{\times}$ amplification` | 新 Δ_s030 / Δ_s015 需重算 | 比率 |
| 29 | `$69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$` | Table 2 G 列 | 数值 |
| 29 | `$0.006$ to $0.053$` | Table 2 II_high 列 min/max | 数值 |
| 29 | `$G \approx 0.9$--$1.7{\times}$` | Table 2 random G 列 range | 数值 |
| 66 | `$0.032$ vs.\ $0.818$`...`$7.196$ vs.\ $1.363$---a $5.3{\times}$` | s025 per-phase medians | 数值+比率 |
| 71 | `$\Delta$ increases from $0.04$...$2.94$...${\sim}1/5$` | experiment_summary_table.json QW imp | 数值+比率 |
| 71 | `$d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$` | cross_model_analysis.json | 数值 |
| 71 | `$d_z{=}0.28$, CI includes zero` | cohens_d_bf16_qwen.json s015 | 数值+判断 |
| 77 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` | permutation_test_results.json | 数值 |
| 79 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | cohens_d_bf16.json | 数值 |
| 79 | `$d_z{=}0.28$...CI includes zero`...`$d_z \geq 0.55$` | cohens_d_bf16_qwen.json | 数值+判断 |
| 79 | `$d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$` | cohens_d 两模型对比 | 数值 |

### analysis.tex

| 行 | 当前文本 | 数据来源 | 类型 |
|----|---------|----------|------|
| 4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | c4_entropy 分析 ΔGini ranges | 数值 |
| 4 | `16 conditions` | 确认是否仍为 16 | 计数 |
| 6 | `$\Delta\mathcal{H} \in [-0.047, -0.040]$` | c4_entropy_deepseek entropy deltas | 数值 |
| 6 | `$\Delta\mathcal{H} = +0.045$` | c4_entropy_qwen s025 | 数值 |
| 6 | `22 of 30 problems` | n=500 后需重算（可能变为 ~220 of 300） | 计数 |

### discussion.tex

| 行 | 当前文本 | 数据来源 | 类型 |
|----|---------|----------|------|
| 5 | `$69$--$274{\times}$` | Table 2 G range | 数值 |
| 5 | `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` | s025 high-phase | 数值 |
| 5 | `$7.196$ vs.\ $1.363$` | s025 low-phase | 数值 |
| 5 | `$G \approx 1$` | random G（确认仍成立） | 数值 |

### conclusion.tex

| 行 | 当前文本 | 数据来源 | 类型 |
|----|---------|----------|------|
| 4 | `$69{\times}$ to $274{\times}$` | Table 2 G range | 数值 |
| 4 | `$d_z$: $0.44 \to 0.80$` | cohens_d_bf16.json | 数值 |
| 4 | `7/8 conditions non-significant` | random PASS/FAIL 重统计 | 计数 |
| 4 | `$d_z \geq 0.55$` | cohens_d_bf16_qwen.json s020 | 阈值 |

### appendix.tex

| 行 | 当前文本 | 数据来源 | 类型 |
|----|---------|----------|------|
| 38 | `$G_{\times} = 58$--$241{\times}$` | 乘法 null 下 G range 需重算 | 数值 |

### appendix_moved.tex (正文段落)

| 行 | 当前文本 | 数据来源 | 类型 |
|----|---------|----------|------|
| 11 | `$0.032$ vs.\ $0.818$`...`$7.196$ vs.\ $1.363$---a $5.3{\times}$` | s025 per-phase medians | 数值+比率 |
| 11 | `$3.9{\times}$...$5.4{\times}$...$5.3{\times}$...$3.6{\times}$` | 各 sparsity level crossover reversal magnitudes | 数值 |
| 26 | `Four of the 50 problems are excluded` | QW excluded count n=500 | 计数 |
| 53 | `mean $\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |
| 56 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |
| 64 | `mean/median ratios ranging from $1.2{\times}$...$1.6{\times}$` and `$1.1{\times}$ to $1.4{\times}$ for Qwen` | 从 n=500 per-problem diffs 计算 | 数值 |
| 66 | `$99.92$th percentile...p_Bonf = 0.0032` | permutation_test_results.json s015 | 数值 |
| 68 | `$0.37$...$9.85$...CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$)` | permutation_test_results.json | 数值 |

### appendix_disc_analysis.tex (正文段落)

| 行 | 当前文本 | 数据来源 | 类型 |
|----|---------|----------|------|
| 4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | random eviction Gini 变化 | 数值 |
| 11 | `$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$` | Table 2 high-phase range | 数值 |
| 11 | `$s = 0.35$, high-phase II rises to $0.105$` | bf16_ds_imp_s035 数据 | 数值 |
| 14 | `7/8...Qwen $s{=}0.30$, $p{=}0.012$...$d_z{=}{-}0.04$` | QW rand s030 统计 | 数值 |
| 45 | `$n{=}49$...$n{=}46$` | 有效样本量 | 计数 |
| 46 | `mean/median ratio ${\sim}1.6{:}1$...mean_diff=22.94, median_diff=14.59` | s030 skewness stats | 数值 |
| 47 | CIs: `$[0.19,\; 0.62]$...$[0.69,\; 1.49]$...$[1.66,\; 6.64]$...$[6.70,\; 16.29]$` | permutation_test_results.json | 数值 |
| 49 | `$p{=}0.012$...$d_z{=}{-}0.04$...d=-0.035` | QW rand s030 re-bootstrap | 数值 |

### appendix_results.tex

| 行 | 当前文本 | 数据来源 | 类型 |
|----|---------|----------|------|
| 7 | `mean $\rho = -0.11$, $p = 0.926$` | cross_model_analysis.json | 数值 |
| 10 | `$p = 0.012$...d_z = -0.04` | QW rand s030 | 数值 |

---

## 5. Qwen s015 预注册决策点 (D037/D038)

### 当前状态
Qwen s015: d_z=0.28, CI=[−0.006, 0.60] → **不显著**，论文采用 "threshold narrative"。

### 决策矩阵

| n=500 结果 | CI 位置 | 操作 |
|-----------|---------|------|
| CI 完全 > 0 | 例如 [0.05, 0.35] | **升级**：删除 `^ns` 标注，改叙事为 "effect reliable at all four sparsity levels for both models" |
| CI 仍跨零 | 例如 [−0.02, 0.15] | **维持 threshold narrative**：保持当前表述不变，仅更新数值 |

### CI 跨零时需更新的叙事位置（仅更新数值，保留 threshold 表述）

| 文件 | 行 | 当前叙事 | 操作 |
|------|------|---------|------|
| abstract.tex | 10 | `replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$` | 更新 d_z 数值，保留 `$s \geq 0.20$` |
| introduction.tex | 15 | `$d_z \geq 0.55$` | 更新阈值数值 |
| results.tex | 71 | `marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$)` | 更新所有数值 |
| results.tex | 90 | `0.28` & `0.05\; $[-0.01, 0.11]$\textsuperscript{ns}` | 更新数值，保留 `^ns` |
| results.tex | 95 | `\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \geq 0.20$.` | 保留 |
| conclusion.tex | 4 | `$d_z \geq 0.55$` | 更新数值 |

### CI > 0 时需更新的叙事位置（升级方案）

| 文件 | 行 | 当前叙事 | 备选叙事 |
|------|------|---------|----------|
| abstract.tex | 10 | `at $s \geq 0.20$` | `at all four sparsity levels` |
| introduction.tex | 15 | `$d_z \geq 0.55$` | `$d_z \geq [新s015值]$`（改用 s015 值） |
| results.tex | 71 | `marginal at $s{=}0.15$...reliable at $s \geq 0.20$` | `reliable at all four sparsity levels ($d_z \geq [新值]$)` |
| results.tex | 90 | `\textsuperscript{ns}` | 删除 `^ns` 标注 |
| results.tex | 95 | 脚注 `Marginal at...reliable at...` | 删除或改为 `All levels significant.` |
| conclusion.tex | 4 | `$d_z \geq 0.55$` | `$d_z \geq [新s015值]$` |

---

## 6. 附属统计量（可能变化但方向不变）

以下数值的 n=500 版本大概率方向不变，但绝对值会变：

| 统计量 | 当前值 | 出现位置 | 预期变化 |
|--------|--------|---------|----------|
| mean/median ratio | up to 43:1 | methodology.tex L18 | n=500 尾部更极端，可能变大或变小 |
| "7/8 conditions" random non-significant | 7/8 | abstract, intro, conclusion, appendix_disc | n=500 CI 更窄，QW rand s030 borderline PASS 可能翻转为 FAIL → 变成 8/8 |
| DS/QW magnitude ratio | ~1/5 | results.tex L71, fig5 caption | 可能略变 |
| Crossover reversal magnitudes | 3.9×–5.4× | appendix_moved.tex L11 | 数据驱动，需重算 |
| Spearman ρ for monotonicity | 1.0 | abstract L10, results L71 | 4 点排序，大概率仍=1.0 |
| Gradient permutation p | 0.043 | abstract L10, results L71 | 4! = 24 种排列，最小 p=1/24≈0.042 |
| Per-problem concordance | ρ=−0.11, p=0.926 | appendix_moved L53, appendix_results L7 | n=500 统计功效更高，可能变显著 |

---

## 7. 数据管道执行顺序

1. **等 C2 n=500 全部 16 conditions 完成**（含 DeepSeek 8 + Qwen 8）
2. 在服务器执行分析脚本（按依赖顺序）：
   ```bash
   cd /root/autodl-tmp/pacs
   # Step 1: 生成汇总表
   python analysis/generate_summary_table.py        # → analysis_output/experiment_summary_table.json

   # Step 2: 统计分析（可并行）
   python analysis/compute_cohens_d.py               # → analysis_output/cohens_d_bf16.json, cohens_d_bf16_qwen.json
   python analysis/cross_model_analysis.py           # → analysis_output/cross_model_analysis.json
   python analysis/run_permutation_test.py           # → analysis_output/permutation_test_results.json
   python analysis/entropy_analysis.py               # → C4 entropy data (如需更新)

   # Step 3: 生成图表
   python analysis/generate_paper_figures.py         # → paper_figures/fig1-fig5 PDFs
   ```
3. 从 JSON 文件提取所有新数值，按本清单 §1-§4 逐项替换
4. **关键决策点**：检查 QW s015 Cohen's d CI 是否含零 → 决定 §5 中的叙事方案
5. 检查 QW rand s030 是否仍 PASS → 决定 "7/8" vs "8/8"
6. 重新编译 LaTeX 验证 → `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`
7. 全文搜索残留的旧数值（grep "n=50"、"0.39"、"14.59" 等）

---

## 8. 不需更新的部分

- **related_work.tex** — 无实验数据
- **background.tex** — 公式定义，无实验数据
- **limitations.tex** — 无具体实验数值（sparsity range $s \in \{0.15,...,0.30\}$ 不变）
- **methodology.tex** 公式/方法部分 — 无变化（仅 n 和统计描述需更新）
- 所有 `\cite{}` 引用 — 无变化

---

## 9. 更新总量统计

| 类别 | 数量 |
|------|------|
| 样本量文本 "50"→"500" | 7 处 |
| 表格（含 8 个表） | ~80 个单元格 |
| 图表重新生成 | 5 个 PDF |
| 内联统计数值 | ~55 处 |
| 条件性叙事更新 (Qwen s015) | 6 处（两套方案） |
| 条件性叙事更新 (7/8 vs 8/8) | 4 处 |
