# 数字一致性检查报告

## 检查时间: 2026-05-22

## 论文文件位置
- `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex`

---

## 一致 ✅

### Table 1 (tab:main_results) — experiments.tex:57-79
- [experiments.tex:63] Naive K=2/ext/n=250: |Bias|=0.058, RMSE=0.090, Cov=0.82 — 源: combined_100_seeds.csv 计算值 0.0579, 0.0900, 0.8225
- [experiments.tex:64] Global K=2/ext/n=250: |Bias|=0.059, RMSE=0.099, Cov=0.87 — 源: combined_100_seeds.csv 计算值 0.0589, 0.0994, 0.8675
- [experiments.tex:65] Strat MLE K=2/ext/n=250: |Bias|=0.012, RMSE=0.094 — 源: 0.0123, 0.0938
- [experiments.tex:69] Naive K=4/ext/n=500: |Bias|=0.062, RMSE=0.113, Cov=0.88 — 源: 0.0624, 0.1126, 0.8775
- [experiments.tex:70] Global K=4/ext/n=500: |Bias|=0.056, RMSE=0.125, Cov=0.91 — 源: 0.0558, 0.1253, 0.9113
- [experiments.tex:71] Strat MLE K=4/ext/n=500: |Bias|=0.010, RMSE=0.127, Cov=0.95 — 源: 0.0101, 0.1274, 0.9500

### Table (tab:main_supp) — appendix.tex:300-322
- [appendix.tex:310] Naive K=2/mod/n=250: |Bias|=0.018, RMSE=0.064, Cov=0.95 — 源: 0.0183, 0.0644, 0.9550
- [appendix.tex:311] Global K=2/mod/n=250: |Bias|=0.009, RMSE=0.074, Cov=0.96 — 源: 0.0089, 0.0738, 0.9600
- [appendix.tex:312] Strat MLE K=2/mod/n=250: |Bias|=0.005, RMSE=0.075, Cov=0.97 — 源: 0.0049, 0.0751, 0.9675
- [appendix.tex:313] HB EC-HTE K=2/mod/n=250: |Bias|=0.005, RMSE=0.075, Cov=0.97 — 源: 0.0049, 0.0746, 0.9675

### §5.7 Coverage Improvement — experiments.tex:118
- [experiments.tex:118] "0.714→0.941 (+22.7pp)" — 源: appendix Table 平均值 (0.675+0.715+0.705+0.760)/4=0.714, (0.950+0.925+0.945+0.945)/4=0.941 (论文内部一致，但 Llama 源数据有问题，见下方不一致项)

### Multi-LLM Table (tab:multilm_cm) — appendix.tex:432-447
- [appendix.tex:441] Llama Acc=0.755, Δπ=0.141, Prop2=1/4 — 源: all_models_summary.csv 值 0.7551, 0.1406, 1
- [appendix.tex:442] Qwen Acc=0.798, Δπ=0.165, Prop2=1/4 — 源: 0.798, 0.1647, 1
- [appendix.tex:443] Gemma Acc=0.763, Δπ=0.125, Prop2=4/4 — 源: 0.7633, 0.1251, 4
- [appendix.tex:444] Mistral Acc=0.802, Δπ=0.134, Prop2=0/4 — 源: 0.802, 0.1336, 0

### §5.7 Δπ range — experiments.tex:117
- [experiments.tex:117] "Δπ ∈ [0.125, 0.165]" — 源: all_models_summary.csv [0.1251, 0.1647] 四舍五入正确

### Hetero-τ DGP — appendix.tex:481
- [appendix.tex:481] "n=500: 0.010 vs. 0.031, a 68% reduction" — 源: hetero_tau_analysis.md n=500 Global=0.0314→0.031, ECHTE=0.0099→0.010, (0.031-0.010)/0.031=67.7%≈68%

### Hetero-τ RMSE — appendix.tex:482
- [appendix.tex:482] "True_short n=1000: 0.212 vs 0.258, 18% improvement" — 源: hetero_tau_analysis.md z=0 Global=0.2577→0.258, ECHTE=0.2117→0.212, (0.258-0.212)/0.258=17.8%≈18%

### Gamma(3,1) vs best — gamma_sensitivity/analysis.md
- [method.tex:20] "Gamma(3,1) within 1.9% of best" — 源: (0.0841-0.0825)/0.0825=1.94%≈1.9% ✓

### Setting-level AUC — experiments.tex:88
- [experiments.tex:88] "AUC = 0.89" — 源: loocv_auc_summary.csv Pool B setting Δπ-only = 0.8895 → 0.89 ✓

### PPCI Complementarity — experiments.tex:108
- [experiments.tex:108] "|bias| from 0.179 to 0.007" — 源: appendix Table tab:ppci, DGP C, EC-HTE z=0 |bias|=0.179, EC-HTE+PPCI z=0 |bias|=0.007 ✓

### R-learner bias reduction — experiments.tex:108
- [experiments.tex:108] "R-learner bias reduction: 89%" — 源: appendix Table tab:rlearner, R-learner Naive=0.121→EC-HTE=0.013, (0.121-0.013)/0.121=89.3%≈89% ✓

### Bias reduction ratios (internally consistent with paper's Table 1) — experiments.tex:42-43
- [experiments.tex:42] "5.4× reduction" — 0.059/0.011=5.36≈5.4 ✓ (uses paper's Table 1 values)
- [experiments.tex:43] "6.2× reduction" — 0.056/0.009=6.22≈6.2 ✓ (uses paper's Table 1 values)
- [experiments.tex:49] "4.8× improvement" — 0.191/0.040=4.78≈4.8 ✓

### Budget crossover — experiments.tex:100-101
- [experiments.tex:100] "n=250 for K=2/extreme, n=1000 for K=4/extreme" — 源: seeds_100 data and budget sweep analysis confirm crossover points

### Multi-LLM per-subgroup data — all_models_metrics.csv
- [appendix.tex:441-444] All per-model accuracy, Δπ, and Prop2 counts match source CSV within rounding

### Appendix Budget Table Coverage (non-Llama) — appendix.tex:465-467
- [appendix.tex:465] Qwen Naive=0.715, HB(n=1000)=0.925 — 源: qwen_sweep_analysis.md K=2 n=1000 Cov_naive=0.715, Cov_echte=0.925 ✓
- [appendix.tex:466] Gemma Naive=0.705, HB(n=1000)=0.945 — 源: gemma_sweep_analysis.md K=2 n=1000 Cov_naive=0.705, Cov_echte=0.945 ✓
- [appendix.tex:467] Mistral Naive=0.760, HB(n=1000)=0.945 — 源: mistral_sweep_analysis.md K=2 n=1000 Cov_naive=0.760, Cov_echte=0.945 ✓

### Robustness coverage — appendix.tex:515
- [appendix.tex:515] "EC-HTE maintains coverage ≥0.945" — 源: Table tab:robustness shows min HB coverage = 0.945 (K=2 p_flip=0.50) and 0.946 (K=4 p_flip=0.50) ✓

---

## 不一致 ❌

### 1. Table 1, HB EC-HTE |Bias| (K=2/extreme/n=250)
- [experiments.tex:66] 论文值: **0.011** vs 源值: **0.0104** (标准四舍五入→0.010)
- 差异: 论文向上取整 (0.0104→0.011 而非 0.010)
- 源: combined_100_seeds.csv, hb_dirichlet method, 跨subgroup和z-level平均
- 影响: 文本中的"5.4×"倍数也受影响 (实际 0.0589/0.0104=5.7×)

### 2. Table 1, Strat MLE Coverage (K=2/extreme/n=250)
- [experiments.tex:65] 论文值: **0.95** vs 源值: **0.9450** (标准四舍五入→0.94)
- 差异: 论文向上取整 (0.945→0.95 而非 0.94)
- 源: combined_100_seeds.csv, mle_laplace method

### 3. Table 1, HB EC-HTE |Bias| (K=4/extreme/n=500)
- [experiments.tex:72] 论文值: **0.009** vs 源值: **0.0083** (标准四舍五入→0.008)
- 差异: 论文向上取整
- 源: combined_100_seeds.csv, hb_dirichlet method
- 影响: 文本中的"6.2×"倍数也受影响 (实际 0.0558/0.0083=6.7×)

### 4. Table 1, HB EC-HTE RMSE (K=4/extreme/n=500)
- [experiments.tex:72] 论文值: **0.127** vs 源值: **0.1262** (标准四舍五入→0.126)
- 差异: 0.1262 rounds to 0.126, not 0.127
- 源: combined_100_seeds.csv

### 5. Appendix Table tab:multilm_budget, Llama HB Coverage (n=1000)
- [appendix.tex:464] 论文值: **0.950** vs 源值: **0.940**
- 差异: 0.010 absolute
- 源: budget_sweep_k2_analysis.md, Llama K=2 n=1000 hb_ec_hte coverage = 0.940
- 影响: 如果修正为0.940，则平均值变为(0.940+0.925+0.945+0.945)/4 = 0.939 (非0.941)，coverage improvement = 22.5pp (非22.7pp)

### 6. Subgroup-level AUC
- [experiments.tex:87] 论文值: **0.87** vs 源值: **0.8646** (标准四舍五入→0.86)
- 差异: 0.8646 rounds to 0.86, paper reports 0.87
- 源: loocv_auc_summary.csv, Pool B subgroup Δπ-only AUC = 0.8645833
- 注: loocv_auc_results.md 建议报告 0.87，但这不符合标准四舍五入规则

### 7. Gamma sensitivity "<6%" claim
- [论文中隐含引用] Source says "Max RMSE difference: **6.0%**" (reasonable prior range)
- 论文未直接使用 "<6%" 但 gamma 分析文档标题为 "6.0%" — 如果论文任何位置写 "<6%" 则不严格准确
- 注: method.tex:20 claims "<5% RMSE variation under 2× hyperprior perturbation" — 这是不同实验(仅扰动Gamma(3,1)的scale 0.5x~2x)，与完整15配置sweep的6.0%不同

---

## 未找到源数据 ⚠️

### 1. CausalForest Table 1 数字
- [experiments.tex:75-77] Naive(0.208, 0.231, 0.44), Global(0.191, 0.244, 0.58), EC-HTE Forest(0.040, 0.224, 0.91)
- 无法在 artifacts/ 中找到 CausalForest 实验的源 CSV
- combined_100_seeds.csv 仅包含 DIM 估计器结果

### 2. Semi-synthetic TweetEval Table 数字
- [appendix.tex:316-319] TweetEval extreme n=250: Naive(0.027, 0.103, 0.93), Global(0.023, 0.124, 0.92), etc.
- 无法找到 exp-003 (semi-synthetic) 的原始汇总 CSV

### 3. R² = 0.994 (K=2) 和 R² = 0.974 (K=4)
- [experiments.tex:25] 引用于多处
- 无法找到产生这些R²的回归源数据/脚本输出

### 4. "50% of configurations (260/520)"
- [experiments.tex:26] 和 "84.6% of cases"
- [experiments.tex:27]
- 无法找到产生这些统计量的汇总文件

### 5. "2.86× (K=2) and 2.41× (K=4)" 最大放大倍数
- [experiments.tex:28]
- 无法追溯到具体源数据文件

### 6. "5.9× amplification" (CausalForest)
- [experiments.tex:50]
- 无 CausalForest 源数据

### 7. Hate speech Δπ = 0.117
- [experiments.tex:15] "Real-data validation confirms Δπ = 0.117"
- 未找到 hate speech 实验源 CSV

### 8. "≥94.5% coverage under up to 50% subgroup misspecification noise"
- [experiments.tex:17]
- Tab:robustness 显示 min 0.945 (K=2 p=0.50) 和 0.946 (K=4 p=0.50)，与 ≥94.5% 匹配
- 但原始实验 CSV 未找到

---

## [TBD] Placeholders

### c1_integration_template.tex
- [artifacts/c1_integration_template.tex] 全文均为 [TBD] placeholder — 这是模板文件，实际数据已填入 docs/paper/ 中的正式论文文件

---

## 总结

| 类别 | 数量 |
|------|------|
| 一致 ✅ | 28 |
| 不一致 ❌ | 7 |
| 无源数据 ⚠️ | 8 |

### 不一致严重性评估

**低风险 (rounding at boundary):** 项目 1-4, 6 — 这些是边界值的四舍五入偏差（如 0.0104→0.011 vs 0.010），差异在小数第三位。可能来源于：(a) 使用50-seed初始结果后未更新至100-seed, (b) 不同的取整惯例, (c) 中间计算精度差异。

**中风险:** 项目 5 — Llama HB Coverage 0.950 vs 源数据 0.940 差异为 0.01，影响 §5.7 的 "+22.7pp" 主张。如果修正，变为 "+22.5pp"。

**低风险:** 项目 7 — Gamma 6.0% 是边界值，论文主要文本使用 "<5% under 2× perturbation" 是不同（更保守）的实验，可能OK。

### 建议
1. 将 Table 1 中 HB EC-HTE 数值更新为标准四舍五入: K=2 |Bias|→0.010, K=4 |Bias|→0.008, RMSE→0.126
2. 核实 Llama K=2 n=1000 的 HB coverage 是 0.940 还是 0.950 (可能需要重新运行或检查不同的 seed batch)
3. 将 subgroup AUC 报告为 0.86 或明确说明取 2 significant figures 的约定
4. 确认 Strat MLE Coverage 是 0.94 还是 0.95
