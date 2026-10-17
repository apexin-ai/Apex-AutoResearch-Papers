## 数据自查报告 V2

审计日期: 2026-05-23

---

### A. Table 1 (experiments.tex, tab:main_results)

数据源: `results/exp_centered_eb_table1_dim.csv` (DIM), `results/exp_centered_eb_table1_cf.csv` (CF)

| Row | Column | Paper Value | Source Value | Match? |
|-----|--------|-------------|-------------|--------|
| DIM K=2, Naive | \|Bias\| | 0.058 | 0.0579 | ✅ |
| DIM K=2, Naive | RMSE | 0.090 | 0.0900 | ✅ |
| DIM K=2, Naive | Coverage | 0.82 | 0.8225 | ✅ |
| DIM K=2, Global | \|Bias\| | 0.059 | 0.0589 | ✅ |
| DIM K=2, Global | RMSE | 0.099 | 0.0994 | ✅ |
| DIM K=2, Global | Coverage | 0.87 | 0.8675 | ✅ |
| DIM K=2, F-L Scalar | \|Bias\| | 0.122 | 0.1217 | ✅ |
| DIM K=2, F-L Scalar | RMSE | 0.159 | 0.1595 | ✅ |
| DIM K=2, F-L Scalar | Coverage | 0.68 | 0.6825 | ✅ |
| DIM K=2, F-L Per-sub | \|Bias\| | 0.168 | 0.1679 | ✅ |
| DIM K=2, F-L Per-sub | RMSE | 0.220 | 0.2196 | ✅ |
| DIM K=2, F-L Per-sub | Coverage | 0.65 | 0.6475 | ✅ |
| DIM K=2, Strat. MLE | \|Bias\| | 0.012 | 0.0123 | ✅ |
| DIM K=2, Strat. MLE | RMSE | 0.094 | 0.0938 | ✅ |
| **DIM K=2, Strat. MLE** | **Coverage** | **0.95** | **0.9450** | **⚠️** |
| DIM K=2, HB EC-HTE | \|Bias\| | 0.008 | 0.0080 | ✅ |
| DIM K=2, HB EC-HTE | RMSE | 0.089 | 0.0888 | ✅ |
| DIM K=2, HB EC-HTE | Coverage | 0.94 | 0.9375 | ✅ |
| DIM K=4, Naive | \|Bias\| | 0.062 | 0.0624 | ✅ |
| DIM K=4, Naive | RMSE | 0.113 | 0.1126 | ✅ |
| DIM K=4, Naive | Coverage | 0.88 | 0.8775 | ✅ |
| DIM K=4, Global | \|Bias\| | 0.056 | 0.0558 | ✅ |
| DIM K=4, Global | RMSE | 0.125 | 0.1253 | ✅ |
| DIM K=4, Global | Coverage | 0.91 | 0.9113 | ✅ |
| DIM K=4, Strat. MLE | \|Bias\| | 0.010 | 0.0101 | ✅ |
| DIM K=4, Strat. MLE | RMSE | 0.127 | 0.1274 | ✅ |
| DIM K=4, Strat. MLE | Coverage | 0.95 | 0.9500 | ✅ |
| DIM K=4, HB EC-HTE | \|Bias\| | 0.012 | 0.0116 | ✅ |
| DIM K=4, HB EC-HTE | RMSE | 0.120 | 0.1201 | ✅ |
| DIM K=4, HB EC-HTE | Coverage | 0.96 | 0.9562 | ✅ |
| CF K=4, Naive | \|Bias\| | 0.208 | 0.2075 | ✅ |
| CF K=4, Naive | RMSE | 0.231 | 0.2314 | ✅ |
| CF K=4, Naive | Coverage | 0.44 | 0.4412 | ✅ |
| CF K=4, Global | \|Bias\| | 0.191 | 0.1906 | ✅ |
| CF K=4, Global | RMSE | 0.244 | 0.2442 | ✅ |
| CF K=4, Global | Coverage | 0.58 | 0.5825 | ✅ |
| CF K=4, EC-HTE Forest | \|Bias\| | 0.039 | 0.0389 | ✅ |
| CF K=4, EC-HTE Forest | RMSE | 0.180 | 0.1798 | ✅ |
| CF K=4, EC-HTE Forest | Coverage | 0.90 | 0.9025 | ✅ |

**Table 1 小结**: 39 cells 中 38 一致, 1 个边界舍入问题 (Strat. MLE Coverage: 0.9450 报为 0.95, banker's rounding 应为 0.94)

---

### B. 正文数字

| # | Number | Paper Location | Source File | Source Value | Match? |
|---|--------|---------------|------------|-------------|--------|
| B1a | R²=0.994 (K=2 synthetic) | experiments.tex:16, theory.tex:81, appendix.tex:872 | results/exp002_bias_bound.csv | R²=0.9932 | **⚠️ 0.993→0.994 向上舍入** |
| B1b | R²=0.974 (K=4 synthetic) | experiments.tex:16, theory.tex:81 | results/exp002_k4_validation.csv | R²=0.9654 | **⚠️ 实际0.965, 差0.009** |
| B1c | R²=0.975 (multi-LLM aggregate) | experiments.tex:73, related_work.tex:36, appendix.tex:948 | results/exp_realcm_bias_identity.csv | R²=0.9749 | ✅ |
| B2 | 14.9% sign reversal | experiments.tex:18, abstract.tex:5, introduction.tex:13,28 | artifacts/policy_reversal_zone.csv | 163/1092=14.93% | ✅ |
| B3a | 2.86× amplification (K=2) | experiments.tex:17, theory.tex:108 | results/exp002_debiasing_hurts.csv | ratio=2.857 | ✅ |
| B3b | 2.41× amplification (K=4) | experiments.tex:17, theory.tex:108 | results/exp002_debiasing_hurts.csv | ratio=2.414 | ✅ |
| B4 | 7.4× reduction | experiments.tex:26, abstract.tex:7 | Table 1: 0.059/0.008 | 7.375 | ✅ |
| B5a | 0.059 (Global bias) | experiments.tex:24,26,45 | Table 1 Global \|Bias\| K=2 | 0.0589 | ✅ |
| B5b | 0.008 (HB EC-HTE bias) | experiments.tex:26,49 | Table 1 HB EC-HTE \|Bias\| K=2 | 0.0080 | ✅ |
| B6 | 11 LLM-dataset combinations | abstract.tex:5, related_work.tex:36, conclusion.tex:4 | results/exp_realcm_summary.csv | 11 unique pairs | ✅ |
| B7 | eight real LLMs | abstract.tex:5, introduction.tex:13, experiments.tex:18 | results/exp_realcm_bias_identity.csv | 8 unique LLMs | ✅ |

**注意 B1b**: R²=0.974 可能与 real-CM aggregate R²=0.975 混淆, 而非来自 synthetic K=4 (实为 0.965)

**注意 B7**: appendix.tex:981 写 "seven LLMs (four open-source, three proprietary)" 与主文 "eight" 不一致, 且 Table 21 实际列出 9 个 model name

---

### C. Appendix 关键表格

| # | Number | Paper Location | Source File | Source Value | Match? |
|---|--------|---------------|------------|-------------|--------|
| C1 | Aggregate R²=0.975 | appendix.tex:948,973 | results/exp_realcm_bias_identity.csv | pooled R²=0.9747 | ✅ |
| C1-sub | "10 of 11 ≥ 0.93" | appendix.tex:948 | results/exp_realcm_summary.csv | **9 of 11** (gpt-4o-mini×TweetEval R²=0.929 < 0.93) | **⚠️** |
| C2 | GPT-4o-mini R²=0.76 | appendix.tex:949,971 | results/exp_realcm_summary.csv | R²=0.7563 | ✅ |

---

### D. AUC 数字

| # | Number | Paper Location | Source File | Source Value | Match? |
|---|--------|---------------|------------|-------------|--------|
| D1 | AUC=0.63 (16 real combos) | experiments.tex:69, appendix.tex:1022 | results/exp_asymmetric_diagnostic_auc.csv | pooled AUC=0.626 | ✅ |
| D2 | AUC=1.0 (Δτ>0 subgroups) | experiments.tex:69, abstract.tex:6, introduction.tex:18 | results/exp_asymmetric_diagnostic_auc_summary.csv | 6/16 combos AUC=1.0 | ❓ 无法完全复现 pooling 逻辑 |
| D3 | AUC=0.86 (synthetic) | method.tex:52, theory.tex:64, appendix.tex:282 | artifacts/_project/report/delta_pi_only_auc.md | subgroup AUC=0.865 | ✅ |

---

### E. 其他频繁引用数字

| # | Number | Paper Location | Source File | Source Value | Match? |
|---|--------|---------------|------------|-------------|--------|
| E1 | ≥93.5% coverage | experiments.tex:10, limitations.tex:15, appendix.tex:1278 | results/exp_a1_sensitivity_summary.csv | EC-HTE min coverage=93.5% at γ=0.20 | ✅ |
| E2 | 520 configs | experiments.tex:15,17, theory.tex:108 | results/exp002_bias_heatmap.csv | 546 total - 26 (Δτ=0) = 520 | ✅ |
| E3 | Bootstrap ≥95% at n≥25 | method.tex:46, limitations.tex:19, appendix.tex:1127 | results/exp_bootstrap_small_n_summary.csv | n=25: 100%, n=50: 98.75%, n=75: 97.5%, n=100: 96.25%, n=200: 95.0% | ✅ |

---

### Summary

| 类别 | 已核对项数 | 一致 | 不一致/存疑 |
|------|-----------|------|------------|
| A. Table 1 cells | 39 | 38 | 1 |
| B. 正文数字 | 11 | 9 | 2 |
| C. Appendix 表格 | 3 | 2 | 1 |
| D. AUC 数字 | 3 | 2 | 1 |
| E. 其他 | 3 | 3 | 0 |
| **合计** | **59** | **54** | **5** |

### 需关注的问题

1. **⚠️ Table 1 Strat. MLE Coverage**: 论文报 0.95, 数据 0.9450, banker's rounding 应为 0.94 — **边界舍入问题**
2. **⚠️ R²=0.994 (B1a)**: 数据 R²=0.993, 论文向上舍入为 0.994 — **微小偏差**
3. **⚠️ R²=0.974 for K=4 (B1b)**: 数据 R²=0.965, 差 0.009 — **可能与 real-CM R²=0.975 混淆**, 需核实
4. **⚠️ "10 of 11 ≥ 0.93" (C1-sub)**: 数据显示 9 of 11 (gpt-4o-mini×TweetEval R²=0.929) — **计数偏差**, 依赖是否将 0.929 视为 ≈0.93
5. **❓ AUC=1.0 (D2)**: 方向一致但无法从 CSV 精确复现 pooling 逻辑
6. **注意**: appendix.tex:981 "seven LLMs" 与主文 "eight" 及 Table 21 (9 models) 存在内部不一致
