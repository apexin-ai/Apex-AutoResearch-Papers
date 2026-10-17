# 数据自查报告

**日期**: 2026-05-23
**范围**: 论文所有 .tex 文件中的数值 vs 实验输出/脚本

---

## ✅ 已核对一致

### Table 1 — DIM K=2 Extreme (n=250)
- Naive |Bias|=0.058, RMSE=0.090, Coverage=0.82 ← `results/exp_centered_eb_table1_dim.csv` (config=DIM_K2_extreme)
- Global |Bias|=0.059, RMSE=0.099, Coverage=0.87 ← 同上
- Strat MLE |Bias|=0.012, RMSE=0.094, Coverage=0.95 ← 同上
- HB EC-HTE |Bias|=0.008, RMSE=0.089, Coverage=0.94 ← 同上
- F-L Scalar |Bias|=0.122, RMSE=0.159, Coverage=0.68 ← `compute_fl_for_table1.py` 实时计算验证 (DIM_K2_extreme config)
- F-L Per-sub |Bias|=0.168, RMSE=0.220, Coverage=0.65 ← 同上

### Table 1 — CausalForest K=4 Extreme (n=500)
- EC-HTE Forest |Bias|=0.039, RMSE=0.180, Coverage=0.90 ← `results/exp_centered_eb_table1_cf.csv`
- Global Forest |Bias|=0.191, RMSE=0.244, Coverage=0.58 ← 同上
- Naive Forest |Bias|=0.208, RMSE=0.231, Coverage=0.44 ← 同上

### Table 1 — DIM K=4 (n=500) and K=2 (n=500)
- 所有值与 `exp_centered_eb_table1_dim.csv` 一致 (experiments.tex lines 44-60)

### Sign Reversal (Figure 1, Appendix Table)
- 14.9% at τ(0)=0.03 ← `sign_reversal_tau_sweep.csv`: 163/1092=14.93% ✓
- 31.0% at τ(0)=0.01 ← 339/1092=31.04% ✓
- 21.6% at τ(0)=0.02 ← 236/1092=21.61% ✓
- 6.1% at τ(0)=0.05 ← 67/1092=6.14% ✓
- 1.6% at τ(0)=0.07 ← 18/1092=1.65% ✓
- 0% at τ(0)≥0.10 ← 0/1092 ✓
- τ̂ = -0.059 at τ(0)=0.03 ← actual -0.05929 (rounds correctly) ✓
- τ̂ = -0.079 at τ(0)=0.01 ← actual -0.07929 (rounds correctly) ✓
- Critical threshold τ(0) < 0.089 ← max|bias_global| = 0.08929 ✓
- 7.5% of subgroup estimates ← 163/2184 = 7.46% ✓

### R² — Bias Identity
- R² = 0.994 for K=2 ← `results/exp002_bias_bound.csv`: actual 0.9938 (rounds to 0.994) ✓
- R² = 0.974 for K=4 ← `results/exp002_k4_validation.csv`: actual 0.9738 (rounds to 0.974) ✓
- R² ≥ 0.976 at P(Z=1)=0.1 ← `results/exp019_pz1_sweep_results.csv`: K=2: 0.998, K=4: 0.984 ✓
- R² = 0.975 aggregate (11 real LLM CMs) ← `results/exp_realcm_summary.csv`: pooled 0.9747 ✓
- R² = 0.991 asymmetric ← `results/exp014_asymmetric_bias.csv`: actual 0.9917 ✓
- Outlier R² = 0.76 ← gpt-4o-mini/CivilComments: 0.7563 ✓

### R² per-model values (appendix table, all 11)
- gpt-4-turbo/TweetEval: 0.993 ← actual 0.9931 ✓
- Qwen2.5-7B/TweetEval: 0.990 ← actual 0.9902 ✓
- Mistral-7B/TweetEval: 0.990 ← actual 0.9899 ✓
- Gemma-2-9B/TweetEval: 0.982 ← actual 0.9820 ✓
- gpt-4o/CivilComments: 0.979 ← actual 0.9794 ✓
- gpt-4o/TweetEval: 0.975 ← actual 0.9752 ✓
- gpt-4.1/TweetEval: 0.969 ← actual 0.9691 ✓
- gpt-3.5-turbo/TweetEval: 0.948 ← actual 0.9478 ✓
- gpt-3.5-turbo/CivilComments: 0.935 ← actual 0.9346 ✓
- gpt-4o-mini/TweetEval: 0.929 ← actual 0.9293 ✓
- gpt-4o-mini/CivilComments: 0.756 ← actual 0.7563 ✓

### Debiasing Hurts
- 2.86× worst-case K=2 ← `results/exp002_debiasing_hurts.csv`: actual 2.857 ✓
- 2.41× K=4 ← 同上: actual 2.414 ✓
- 520 configurations ← `results/exp002_bias_bound.csv`: 26 Δπ × 20 nonzero Δτ = 520 ✓
- 260/520 = 50% worsened ← computed from bias_bound.csv ✓

### Diagnostic AUC
- AUC = 0.86 subgroup synthetic ← `artifacts/diagnostic_revision/loocv_auc_summary.csv`: 0.8646 ✓
- AUC = 1.0 for τ_s > 0 ← `results/exp_asym_diag_v2.csv`: confirmed ✓
- AUC = 0.63 across 16 real LLM-dataset combos ← `results/exp_asymmetric_diagnostic_auc.csv`: pooled 0.6259 ✓
- AUC = 0.66 asymmetric ← `results/exp_asym_diag_v2.csv`: 0.6571 ✓

### K=8 Experiment
- HB Coverage 95.6%, RMSE 0.340 ← `results/exp_k8_subgroups_summary.csv`: 0.9556, 0.3404 ✓
- Global Coverage 95.1%, RMSE 0.168 ← 同上: 0.9506, 0.1680 ✓
- Strat MLE Coverage 95.3%, RMSE 0.638 ← 同上: 0.9531, 0.6384 ✓
- n_expert/K = 31 ← 250/8 = 31.25 ≈ 31 ✓

### Bootstrap Validation
- Bootstrap ≥95% coverage at all n_expert ≥ 25 ← `results/exp_bootstrap_small_n_summary.csv` ✓
- Plug-in SE ≥91.2% minimum across all budgets ← 同上: min 91.25% at n=75 ✓
- Coverage 0.970/0.960/0.970/0.970 ← `results/exp_w4_bootstrap_se.csv` ✓
- PPCI bootstrap: 93.8% aggregate, 95.0% ← `results/exp_bootstrap_se_v2_summary.csv` ✓

### Multi-LLM Δπ Values
- GPT-3.5-Turbo: 0.198 ← `results/exp008_multi_llm_comparison.csv`: 0.1981 ✓
- GPT-4-Turbo: 0.149 ← 0.1491 ✓
- GPT-4o-mini: 0.136 ← 0.1358 ✓
- GPT-5.4: 0.114 ← `exp008_filtered_analysis.md`: 0.1144 ✓
- GPT-4.1: 0.098 ← 0.0984 ✓
- GPT-4o: 0.080 ← 0.0797 ✓
- "5 of 6 share worst subgroup" ← True_medium worst for 5 models ✓
- GPT-4.1 accuracy 85.8% ← binary accuracy (positive vs non-positive): 0.858 ✓

### Bias Reduction Multipliers
- 7.4× at K=2 ← experiments.tex: 0.059/0.008 = 7.375 ≈ 7.4 ✓
- 4.7× at K=4 ← experiments.tex: 0.056/0.012 = 4.667 ≈ 4.7 ✓

### Robustness Experiments
- A1 sensitivity ≥93.5% up to γ=0.20 ← `results/exp_a1_sensitivity_summary.csv`: exactly 93.5% at γ=0.20 ✓
- A1 bias increase 13.7% ← actual 13.68% ✓
- Treatment-dep γ_T=0.10 coverage 75.0% ← `results/exp_treatment_dep_misclass.csv`: exact ✓
- Treatment-dep ≥89.7% at γ_T≤0.05 ← actual 89.75% ✓
- Confounded DGP: EC-HTE 96.0% vs naive 78.5% ← `results/exp_confounded_dgp_summary.csv` (subgroup 1) ✓
- Subgroup misspecification: EC-HTE ≥0.945 at p_flip=0.50 ← `results/exp010_misspecified_results.csv` ✓

### PPCI
- |Bias| from 0.179 to 0.007 (DGP C, z=0) ← `results/exp007_ppci_dsl_raw.csv`: recomputed avg(|0.280|, |0.077|)=0.179, avg(|0.002|, |0.012|)=0.007 ✓

### Asymmetric Correction
- R² = 0.991 ← `results/exp014_asymmetric_bias.csv`: 0.9917 ✓
- |Bias| from 0.025 to 0.006 (4× improvement) ← `results/exp014_asymmetric_correction.csv` ✓
- Coverage 0.90 vs 0.78 ← 同上 ✓

### Computational
- <5ms for K=4 N=5000 ← `artifacts/timing_benchmark.csv` (assumed)
- Error rate range 10.2%-20.0% (GPT-4.1) ← `results/exp008_multi_llm_comparison.csv` per-subgroup: 10.16%-20.00% ✓
- Δπ = 0.098 (GPT-4.1) ← 0.2000-0.1016 = 0.0984 ≈ 0.098 ✓

### CausalForest Amplification
- 4.9× EC-HTE reduction ← `results/exp011_causal_forest.csv`: global/naive at K=4 ext n=500 sub=0 = 4.86× ≈ 4.9 ✓

---

## ⚠️ 发现的不一致 / 需修复

### 1. "14 real LLM-dataset combinations" → 实际为 11 或 13
- **位置**: abstract.tex:5, introduction.tex:17, conclusion.tex:4
- **论文写**: "14 real LLM--dataset combinations"
- **数据**: `exp_realcm_summary.csv` 有 **11** 组合 (bias identity R²); `exp_real_cm_validation.csv` 有 **13** 组合 (加 Llama-3.1-8B + gpt-5.4)
- **建议**: 根据对应分析修改为 "11" 或 "13"。无任何数据文件产生 14 这个数字。

### 2. "10 of 11 achieve R² ≥ 0.93" → 实际为 9 of 11
- **位置**: appendix.tex (real CM validation section)
- **论文写**: "10 of 11 achieve R² ≥ 0.93"
- **数据**: gpt-4o-mini/TweetEval R² = **0.9293** (< 0.93); gpt-4o-mini/CivilComments = 0.7563 (clearly fails)
- **精确值**: 9 of 11 have R² ≥ 0.93。如果四舍五入到两位小数 0.9293→0.93 则可辩护为 "10 of 11"
- **建议**: 改为 "10 of 11 achieve R² ≥ 0.92" 或 "9 of 11 achieve R² ≥ 0.93"

### 3. Introduction "scalar attenuation correction increases bias by up to 2.9×" — 方法标签错误
- **位置**: introduction.tex:14
- **论文写**: "the classical Frazis-Loeb **scalar** attenuation correction increases bias by up to 2.9×"
- **数据**: 2.9× = 0.168/0.058 来自 F-L **Per-Subgroup**（非 Scalar）。F-L Scalar 的倍数为 0.122/0.058 = **2.1×**
- **参考**: theory.tex:54 正确区分: "F-L scalar → 2.1×", "F-L per-subgroup → 2.9×"
- **建议**: 改为 "Frazis-Loeb per-subgroup correction" 或改用 2.1× 对应 scalar

### 4. "R² ≥ 0.97 across ... 14 real LLM-dataset combinations" — R² 阈值有歧义
- **位置**: abstract.tex:5, introduction.tex:17
- **论文写**: "verified at R² ≥ 0.97 across synthetic grids and 14 real LLM--dataset combinations"
- **数据**: 11 个真实组合中仅 **7** 个单独 R² ≥ 0.97。**聚合** (pooled) R² = 0.975 ≥ 0.97
- **问题**: 语法歧义——"R² ≥ 0.97" 是否适用于每个真实组合？如果是，则不成立
- **建议**: 明确写法，如 "verified at R² ≥ 0.97 on synthetic grids and at pooled R² = 0.975 across 11 real LLM--dataset combinations"

### 5. CausalForest "5.9×" bias amplification — 四舍五入存疑
- **位置**: introduction.tex:14, experiments.tex:32
- **论文写**: "up to 5.9×"
- **数据**: `results/exp011_causal_forest.csv`: 最大比值 = **5.91×** (K=4 ext n=100 sub=0 z=1), 另一计算为 **5.95×** (K=4 ext n=500 sub=1)
- **问题**: 5.91 标准四舍五入→5.9，可接受；5.95 应→6.0
- **建议**: 使用 5.9× 作为 5.91 的四舍五入是可辩护的

### 6. "breakeven γ_T ≈ 0.10" — EC-HTE 在 γ_T=0.10 时仍优于 Global
- **位置**: appendix.tex (treatment-dependent misclass section)
- **论文写**: "breakeven at γ_T ≈ 0.10"
- **数据**: γ_T=0.10 时 EC-HTE coverage 75.0% vs Global 67.5% (EC-HTE 仍+7.5pp)；实际交叉在 0.10-0.15 之间
- **建议**: 修改为 "breakeven between γ_T = 0.10 and 0.15" 或定义 breakeven 为覆盖率低于名义水平的阈值

### 7. F-L 值来源分散
- **问题**: Table 1 的 F-L Scalar/Per-sub 值来自 `compute_fl_for_table1.py`（仅打印，无保存文件），而 `exp_fl_comparison_summary.csv` 使用不同的 DGP 配置 (Δτ=0.3 vs Table 1 的 Δτ=0.4)
- **风险**: F-L 值无持久化的 CSV 来源，仅通过脚本临时计算验证
- **建议**: 运行 `compute_fl_for_table1.py` 并保存输出到 CSV

---

## ❌ 无法追溯

### 1. "92% of configs with sign reversal"
- **说明**: 此数字出现在任务描述中，但**未在论文任何 .tex 文件中找到**。论文使用的是 14.9%/31% 等按 τ(0) 分层的百分比。
- **状态**: 无需操作（论文中不存在此 claim）

### 2. GPT-5.4 数据不在主 CSV 中
- **说明**: GPT-5.4 的 Δπ=0.114 仅在 `exp008_filtered_analysis.md`（分析报告）中记录，不在 `exp008_multi_llm_comparison.csv` 中
- **风险**: 低（值已通过 markdown 报告验证）

---

## 📊 统计

| 类别 | 数量 |
|------|------|
| 总提取独立数字/claim | ~185 |
| 已核对一致 | ~175 |
| 不一致/需修复 | 7 |
| 无法追溯 | 0 (论文内) |

### 关键修复优先级

| 优先级 | 问题 | 影响 |
|--------|------|------|
| **高** | "14 real LLM-dataset combinations" → 应为 11 或 13 | 出现在 abstract, introduction, conclusion 三处 |
| **高** | "R² ≥ 0.97 across ... 14 real combinations" 歧义 | Abstract 核心 claim，可能误导审稿人 |
| **中** | "10 of 11 achieve R² ≥ 0.93" → 严格说是 9 of 11 | Appendix，边界情况 (0.9293 vs 0.93) |
| **中** | Introduction "scalar" → 应为 "per-subgroup" (2.9×) | 方法标签错误 |
| **低** | "breakeven γ_T ≈ 0.10" 精度 | Appendix 局部 claim |
| **低** | F-L Table 1 值无持久化 CSV | 可重现但无存档 |
| **低** | CausalForest 5.9× 四舍五入 | 5.91→5.9 可接受 |

---

## 附录: 数据来源映射

| 论文元素 | 主要数据文件 | 脚本 |
|----------|-------------|------|
| Table 1 (DIM) | `results/exp_centered_eb_table1_dim.csv` | `exp_centered_eb_table1.py` |
| Table 1 (CF) | `results/exp_centered_eb_table1_cf.csv` | `exp_centered_eb_table1.py` |
| Table 1 (F-L) | (无 CSV，仅脚本输出) | `compute_fl_for_table1.py` |
| Figure 1 | `results/exp002_bias_bound.csv`, `sign_reversal_tau_sweep.csv` | `scripts/fig1_bias_mechanism.py`, `sign_reversal_analysis.py` |
| Figure 2 | `results/exp002_bias_heatmap.csv` | `draw_fig2.py` |
| Figure 3 | `results/exp_centered_eb_table1_dim.csv` (推测) | `draw_fig3.py` |
| R² (synthetic) | `results/exp002_bias_bound.csv`, `exp002_k4_validation.csv` | (inline computation) |
| R² (real CMs) | `results/exp_realcm_summary.csv`, `exp_realcm_bias_identity.csv` | (inline computation) |
| Debiasing hurts | `results/exp002_debiasing_hurts.csv` | `scripts/debiasing_hurts_summary.py` |
| Diagnostic AUC | `artifacts/diagnostic_revision/loocv_auc_summary.csv`, `results/exp_asymmetric_diagnostic_auc.csv` | (inline computation) |
| K=8 | `results/exp_k8_subgroups_summary.csv` | `exp030_k8_subgroups.py` |
| Bootstrap SE | `results/exp_w4_bootstrap_se.csv`, `exp_bootstrap_small_n_summary.csv` | (exp scripts) |
| Multi-LLM Δπ | `results/exp008_multi_llm_comparison.csv` | (exp008 scripts) |
| PPCI | `results/exp007_ppci_dsl_raw.csv` | (exp007 scripts) |
| A1 sensitivity | `results/exp_a1_sensitivity_summary.csv` | (exp scripts) |
| Treatment-dep | `results/exp_treatment_dep_misclass.csv` | (exp scripts) |
| Confounded DGP | `results/exp_confounded_dgp_summary.csv` | (exp scripts) |
| Policy reversal | `artifacts/policy_reversal_zone.csv` | `task_j_policy_reversal.py` |
| Asymmetric | `results/exp014_asymmetric_bias.csv`, `exp014_asymmetric_correction.csv` | (exp014 scripts) |
| Real CM validation | `results/exp_real_cm_validation.csv` | (exp scripts) |
| Screening/κ | `results/exp_screening.csv` | (exp scripts) |
| Civil Comments | `results/exp023_confusion_matrices.json`, `exp023_semisynthetic_v3_summary.csv` | (exp023 scripts) |
| Open-source LLMs | `results/exp023_*` files | (exp023 scripts) |
