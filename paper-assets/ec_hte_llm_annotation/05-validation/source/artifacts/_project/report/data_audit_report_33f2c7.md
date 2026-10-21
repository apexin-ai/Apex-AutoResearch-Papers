# Data Audit Report

Generated: 2026-05-23

## Summary
- 总数字数: 52
- 可追溯: 44 (84.6%)
- 数值匹配: 40 (76.9%)
- ⚠️ 数值不匹配或无法精确追溯: 8

---

## Table 1 审计

Source CSV: `results/exp_centered_eb_table1_dim.csv` (DIM rows), `results/exp_centered_eb_table1_cf.csv` (CF rows)

All Table 1 values computed as averages across subgroups, z-levels, and 100 MC runs.

| Config | Method | Paper |Bias| | CSV |Bias| | Paper RMSE | CSV RMSE | Paper Cov | CSV Cov | Verified |
|--------|--------|-------------|------------|------------|----------|-----------|---------|----------|
| DIM K=2 n=250 | Naive | 0.058 | 0.058 | 0.090 | 0.090 | 0.82 | 0.82 | ✓ |
| DIM K=2 n=250 | Global | 0.059 | 0.059 | 0.099 | 0.099 | 0.87 | 0.87 | ✓ |
| DIM K=2 n=250 | Strat. MLE | 0.012 | 0.012 | 0.094 | 0.094 | 0.95 | 0.95 | ✓ |
| DIM K=2 n=250 | HB EC-HTE | 0.008 | 0.008 | 0.089 | 0.089 | 0.94 | 0.94 | ✓ |
| DIM K=4 n=500 | Naive | 0.062 | 0.062 | 0.113 | 0.113 | 0.88 | 0.88 | ✓ |
| DIM K=4 n=500 | Global | 0.056 | 0.056 | 0.125 | 0.125 | 0.91 | 0.91 | ✓ |
| DIM K=4 n=500 | Strat. MLE | 0.010 | 0.010 | 0.127† | 0.127† | 0.95 | 0.95 | ✓ |
| DIM K=4 n=500 | HB EC-HTE | 0.012 | 0.012 | 0.120 | 0.120 | 0.96 | 0.96 | ✓ |
| CF K=4 n=500 | Naive | 0.208 | 0.208 | 0.231 | 0.231 | 0.44 | 0.44 | ✓ |
| CF K=4 n=500 | Global | 0.191 | 0.191 | 0.244 | 0.244 | 0.58 | 0.58 | ✓ |
| CF K=4 n=500 | EC-HTE Forest | 0.039 | 0.039 | 0.180 | 0.180 | 0.90 | 0.90 | ✓ |

**Table 1 结论**: 所有 33 个 cell 均与 source CSV 精确匹配。

---

## 主文定量声明审计

### abstract.tex

| 行号 | 声明 | 数值 | Source CSV | Exp ID | Status |
|------|------|------|-----------|--------|--------|
| 3 | global correction worsens bias in 50% of configurations | 50% (260/520) | exp002_debiasing_hurts.csv + exp002_bias_bound.csv | exp-002 | ✓ 260/520 confirmed |
| 5 | diagnostic achieves AUC = 1.0 on τ_s > 0 subgroups | AUC = 1.0 | exp_asym_diag_v2_analysis.md | exp-028 + asym_diag_v2 | ✓ |
| 6 | 7.4× bias reduction | 7.4× (0.059/0.008) | exp_centered_eb_table1_dim.csv | Table 1 run | ✓ 0.059/0.008=7.375≈7.4 |
| 6 | ≥0.90 coverage | 0.94 | exp_centered_eb_table1_dim.csv | Table 1 run | ✓ 0.94≥0.90 |

### introduction.tex

| 行号 | 声明 | 数值 | Source CSV | Exp ID | Status |
|------|------|------|-----------|--------|--------|
| 6 | LLM misclassification rates vary by up to 5× | 5× | — | — | ✓ Citation: Ashwin et al. (not our data) |
| 7 | GPT-4.1 achieves 85.8% binary accuracy | 85.8% | pilot_gpt41_analysis.md | exp-012 | ✓ Confirmed |
| 7 | error rates range from 10.2% to 20.0% | 10.2%, 20.0% | pilot_gpt41_analysis.md | exp-012 | ✓ nohash_medium=0.102, hash_medium=0.200 |
| 7 | Δπ = 0.098 | 0.098 | pilot_gpt41_analysis.md | exp-012 | ✓ 0.200−0.102=0.098 |
| 14 | R² = 0.994 (K=2) | 0.994 | exp002_bias_bound.csv | exp-002 | ✓ Registry: 0.9939→0.994 |
| 14 | R² = 0.974 (K=4) | 0.974 | exp002_k4_validation.csv | exp-002 | ⚠️ CSV recomputation gives 0.966–0.972; registry says 0.9738→0.974. Possible filtering difference. |
| 14 | R² = 0.975 across 11 real LLM CMs | 0.975 | exp_realcm_bias_identity.csv, exp_realcm_summary.csv | exp-024 | ✓ Recomputed R²=0.9747≈0.975 |
| 15 | 50% of K=2 configurations (260/520) | 260/520 = 50% | exp002_bias_bound.csv | exp-002 | ✓ 26×20=520 configs, 260 hurts confirmed |
| 15 | amplification reaching 2.86× (K=2) | 2.86× | exp002_debiasing_hurts.csv | exp-002 | ✓ Row: extreme_k2 subgroup B ratio=2.857 |
| 15 | 5.9× (K=4 with CausalForest) | 5.9× | exp011_causal_forest.csv | exp-011 | ✓ K=4 extreme sg=0 z=1 ratio=5.91 |
| 16 | AUC = 1.0 on subgroups with non-zero effect heterogeneity | AUC = 1.0 | exp_asym_diag_v2_analysis.md | exp-028/asym_diag_v2 | ✓ tau_s>0 subgroups: sym AUC=1.000 |
| 17 | |bias| from 0.059 to 0.008 | 0.059, 0.008 | exp_centered_eb_table1_dim.csv | Table 1 run | ✓ Table 1 K=2: Global=0.059, HB=0.008 |

### experiments.tex

| 行号 | 声明 | 数值 | Source CSV | Exp ID | Status |
|------|------|------|-----------|--------|--------|
| 1 | N=5000, K∈{2,4}, 100 MC runs | DGP params | exp_centered_eb_table1_dim.csv (n_mc=100) | multiple | ✓ |
| 5 | π ∈ {0.05, 0.10, 0.15, 0.25} | semi-synth setup | exp003_phase_a_v3.csv | exp-003 | ✓ |
| 10 | all ≥93.5% coverage (robustness) | ≥93.5% | multiple | exp-010/029/031/032/035 | ⚠️ Min=93.5% at exp-029 γ=0.20. Borderline exact match. |
| 16 | R² = 0.994 (K=2) and 0.974 (K=4) | 0.994, 0.974 | exp002_bias_bound.csv, exp002_k4_validation.csv | exp-002 | ✓/⚠️ K=2 ✓; K=4 see intro note |
| 16 | R² ≥ 0.976 even at P(Z=1) = 0.1 | ≥0.976 | exp019_pz1_sweep_results.csv | exp-019 | ✓ K=2:0.998, K=4:0.984 both≥0.976 |
| 17 | 50% of K=2 configurations (260/520) | 260/520 | exp002_bias_bound.csv | exp-002 | ✓ |
| 17 | amplification reaching 2.86× (K=2) and 2.41× (K=4) | 2.86×, 2.41× | exp002_debiasing_hurts.csv | exp-002 | ✓ Confirmed from debiasing_hurts.csv |
| 30 | global increases |bias| 0.059 vs naive 0.058 | 0.059, 0.058 | exp_centered_eb_table1_dim.csv | Table 1 run | ✓ |
| 31 | 7.4× at K=2, 4.7× at K=4 | 7.4×, 4.7× | exp_centered_eb_table1_dim.csv | Table 1 run | ✓ 0.059/0.008=7.375; 0.056/0.012=4.67 |
| 31 | coverage 0.94–0.96 | 0.94, 0.96 | exp_centered_eb_table1_dim.csv | Table 1 run | ✓ K=2: 0.94, K=4: 0.96 |
| 37 | CF |bias| from 0.191 to 0.039 (4.9×) | 4.9× | exp_centered_eb_table1_cf.csv | Table 1 run | ✓ 0.191/0.039=4.90 |
| 37 | coverage from 0.58 to 0.90 | 0.58, 0.90 | exp_centered_eb_table1_cf.csv | Table 1 run | ✓ |
| 37 | global amplifies naive bias up to 5.9× | 5.9× | exp011_causal_forest.csv | exp-011 | ✓ K=4 extreme sg=0 z=1: 5.91× |
| 73 | AUC = 0.86 at the subgroup level | 0.86 | exp005_diagnostic_subgroups.csv | exp-005 | ⚠️ Registry shows subgroup_level_auc=0.833, NOT 0.86. The 0.86 matches subgroup_correlation, not AUC. |
| 74 | AUC decreases to 0.63 on real LLM CMs | 0.63 | exp_asymmetric_diagnostic_auc_summary.csv | exp-028 | ✓ Overall symmetric AUC=0.626≈0.63 |
| 74 | AUC reaches 1.0 on τ_s > 0 | 1.0 | exp_asym_diag_v2_analysis.md | asym_diag_v2 | ✓ |
| 76 | max_s score(s) > 1 → AUC ≥ 0.75 | ≥0.75 | exp_positive_scenario_summary.md | exp-025 | Partial ✓ (appendix claim, complex meta-criterion) |
| 79 | K=8, n_expert=250, coverage 95.6% | 95.6% | exp_k8_subgroups_summary.csv | exp-030 | ✓ Registry: hb_echte_coverage=0.956 |

### theory.tex

| 行号 | 声明 | 数值 | Source CSV | Exp ID | Status |
|------|------|------|-----------|--------|--------|
| 58 | AUC decreases from 0.86 to 0.82 (asymmetric) | 0.86→0.82 | — | — | ⚠️ 0.86 not verified (see above). 0.82 not found in any CSV. Exp_asym_diag_v2 shows all-subgroup Sym AUC=0.657, tau>0 only=1.0. Cannot trace 0.82. |
| 61 | R² = 0.991 (asymmetric) | 0.991 | exp014_asymmetric_bias.csv | exp-014 | ✓ Recomputed: 0.9917≈0.992. Paper says 0.991, registry says 0.992. Minor rounding. |
| 65 | ≥93% coverage (A5 relaxation) | ≥93% | exp_w8_a5_violation.csv | w8 A5 exp | ✓ EC-HTE coverage: 0.953–0.960 |
| 65 | 74–82% global degradation (A5) | 74–82% | exp_w8_a5_violation.csv | w8 A5 exp | ⚠️ Data shows global coverage 84.5–86.5%, NOT 74–82%. |
| 70 | R² ≥ 0.976 even at P(Z=1) = 0.1 | ≥0.976 | exp019_pz1_sweep_results.csv | exp-019 | ✓ K=2:0.998, K=4:0.984 |
| 72 | R² = 0.994 for K=2 and R² = 0.974 for K=4 | same | exp002 CSVs | exp-002 | ✓/⚠️ (see intro note on K=4) |
| 99 | 2.86× for K=2 and 2.41× for K=4 | 2.86×, 2.41× | exp002_debiasing_hurts.csv | exp-002 | ✓ |
| 99 | 260 of 520 | 260/520 | exp002_bias_bound.csv | exp-002 | ✓ |

### method.tex

| 行号 | 声明 | 数值 | Source CSV | Exp ID | Status |
|------|------|------|-----------|--------|--------|
| 16 | 87.5% of configurations (21/24) HB outperforms MLE | 87.5% | exp006_budget_sensitivity.csv | exp-006 | ✓ Registry: "HB ≥ MLE in 21/24 configs (87.5%)" |
| 18 | At n_expert ≥ 1000, HB and MLE converge within 0.5% | <0.5% | exp006_budget_sensitivity.csv | exp-006 | ✓ Registry: "convergence" |
| 19 | <5% RMSE variation under 2× hyperprior perturbation | <5% | exp001_hyperprior_sensitivity.csv, exp022_ppi_dsl_agg.csv | exp-001/exp-022 | ⚠️ exp-022 shows 6.0% for "reasonable" range; paper says <5%. |
| 52 | AUC = 0.86 | 0.86 | exp005_diagnostic_subgroups.csv | exp-005 | ⚠️ Same discrepancy as above: data shows 0.833 |
| 52 | reaching 1.0 on τ_s > 0 | 1.0 | exp_asym_diag_v2_analysis.md | asym_diag_v2 | ✓ |
| 59 | PPCI composition reduces |bias| from 0.179 to 0.007 | 0.179, 0.007 | exp007_ppci_dsl.csv | exp-007 | ⚠️ Closest match: DGP C extreme K=2 n=250 z=0: ec_hte |bias|=0.178, ec_hte_ppci=0.010. At n=500 z=0: 0.184→0.006. No exact (0.179, 0.007) pair found. |

### conclusion.tex

| 行号 | 声明 | 数值 | Source CSV | Exp ID | Status |
|------|------|------|-----------|--------|--------|
| 2 | 50% of K=2 configurations | 50% | exp002 | exp-002 | ✓ |
| 4 | AUC = 1.0 on τ_s > 0 | 1.0 | exp_asym_diag_v2_analysis.md | asym_diag_v2 | ✓ |

---

## ⚠️ 无法追溯或数值不匹配的数字

### 1. AUC = 0.86 (3处引用: abstract:5, experiments:73, method:52)
- **Paper**: "A threshold classifier achieves AUC = 0.86 at the subgroup level"
- **Data**: exp-005 registry shows `subgroup_level_auc = 0.833`, `subgroup_correlation = 0.86`
- **诊断**: Paper 可能误用了 correlation (0.86) 替代 AUC (0.833)。差异 = 0.027。
- **严重性**: 🔴 高。AUC 是论文中多次引用的核心指标。

### 2. AUC 0.86 → 0.82 (asymmetric) (theory:58)
- **Paper**: "the AUC decreases from 0.86 to 0.82 (Appendix)"
- **Data**: 无法在任何 CSV 中找到 0.82。exp_asym_diag_v2 shows all-subgroup Sym AUC=0.657。
- **诊断**: 如果 0.86 本身有误(应为 0.833)，则 0.82 的来源也不清楚。可能是旧版实验数据。
- **严重性**: 🟡 中。仅出现在 Remark 中一次。

### 3. R² = 0.974 (K=4) (intro:14, experiments:16, theory:72)
- **Paper**: R² = 0.974
- **Data**: 直接从 exp002_k4_validation.csv 计算得 0.966–0.972 (取决于过滤方式)。Registry 记录为 0.9738。
- **诊断**: Registry 值 0.9738 四舍五入为 0.974 合理。但 CSV 直接计算无法精确复现。可能 registry 使用了不同的过滤条件。
- **严重性**: 🟢 低。差异 <0.01，方向一致。

### 4. 74–82% global degradation under A5 violation (theory:65)
- **Paper**: "global correction degrades to 74–82%"
- **Data**: exp_w8_a5_violation.csv 显示 global coverage = 84.5% (aligned), 84.5% (adversarial)
- **诊断**: 论文声称 74–82%，但数据显示 84.5%。可能来源于旧版实验或不同的 A5 violation 参数化。
- **严重性**: 🟡 中。出现在 theory 章节一次，影响方法论评估。

### 5. <5% RMSE hyperprior sensitivity (method:19)
- **Paper**: "<5% RMSE variation under 2× hyperprior perturbation"
- **Data**: exp-022 registry: `rmse_range_reasonable = 6.0%`, `rmse_range_all = 17.3%`
- **诊断**: "reasonable" range 下 6.0% > 5%。Paper 可能使用更窄的 perturbation 范围或 exp-001 的数据 (`k2_rmse_variation < 1%`, `k4_rmse_variation ~4-5%`)。
- **严重性**: 🟢 低。如果仅看 K=2 (<1%)，声明成立；K=4 ~5% 边界值。

### 6. PPCI 0.179 → 0.007 (method:59)
- **Paper**: "composition reduces |bias| from 0.179 to 0.007"
- **Data**: exp-007 DGP C extreme K=2 最接近匹配:
  - n=250 z=0: ec_hte=0.178, ec_hte_ppci=0.010
  - n=500 z=0: ec_hte=0.184, ec_hte_ppci=0.006
  - Registry: dgp_c_extreme_n250_k2: ec_hte_bias_z0=0.178, ec_hte_ppci_bias_z0=0.005
- **诊断**: 数量级一致但无法精确复现 (0.179, 0.007) 对。可能来自特定 subgroup 或旧版实验。
- **严重性**: 🟢 低。结论方向正确，数量级匹配。

### 7. ≥93.5% coverage robustness (experiments:10)
- **Paper**: "all ≥93.5% coverage"
- **Data**: exp-029 γ=0.20: EC-HTE coverage = 0.935 (精确等于 93.5%)
- **诊断**: 声明精确在边界值成立。非有意义的不匹配，但报告精度可能过高。
- **严重性**: 🟢 低。

### 8. 论文 intro 提及 TweetEval semi-synthetic: p=0.395 / RMSE 差异 (experiments:33)
- **Paper**: "EC-HTE and Global achieve comparable |bias| (p=0.395)"
- **Data**: 来自 exp-003 或 exp-023 semi-synthetic 实验。未直接验证 p-value。
- **严重性**: 🟢 低。统计检验需要完整 raw data 复现。

---

## 实验 ID 映射表

| Exp ID | 描述 | 关键输出文件 |
|--------|------|-------------|
| exp-002 | Bias identity validation (R², 260/520, amplification) | exp002_bias_bound.csv, exp002_debiasing_hurts.csv, exp002_k4_validation.csv |
| exp-005 | Diagnostic AUC | exp005_diagnostic.csv, exp005_diagnostic_subgroups.csv |
| exp-006 | Budget sensitivity, HB vs MLE crossover | exp006_budget_sensitivity.csv |
| exp-007 | PPCI+EC-HTE composition | exp007_ppci_dsl.csv |
| exp-011 | CausalForest (5.9× amplification) | exp011_causal_forest.csv |
| exp-012 | GPT-4.1 pilot (85.8%, Δπ=0.098) | pilot_gpt41_analysis.md |
| exp-014 | Asymmetric CM (R²=0.992) | exp014_asymmetric_bias.csv |
| exp-019 | Class imbalance (R²≥0.976) | exp019_pz1_sweep_results.csv |
| exp-022 | Hyperprior sensitivity | exp022_ppi_dsl_agg.csv |
| exp-024 | Real LLM CM validation (R²=0.975) | exp_realcm_bias_identity.csv |
| exp-028 | Asymmetric diagnostic AUC (0.63 real CMs) | exp_asymmetric_diagnostic_auc_summary.csv |
| exp-029 | A1 sensitivity (γ sweep) | exp_a1_sensitivity_summary.csv |
| exp-030 | K=8 scalability (95.6% coverage) | exp_k8_subgroups_summary.csv |
| exp-035 | Asymmetric CM correction | exp_asymmetric_cm_summary.csv |
| Table 1 | Main results | exp_centered_eb_table1_dim.csv, exp_centered_eb_table1_cf.csv |
| w8 A5 | A5 violation robustness | exp_w8_a5_violation.csv |

---

## 结论

**Table 1**: 所有 33 个数值精确匹配。✅

**主文定量声明**: 52 个数字中 44 个可追溯，40 个精确匹配。

**最需要关注的问题**:
1. 🔴 **AUC = 0.86** 在论文中出现 3 次，但源数据显示 AUC = 0.833。疑似将 correlation (0.86) 误报为 AUC。建议修正为 0.83 或重新计算确认。
2. 🟡 **AUC 0.82 (asymmetric)** 无法追溯到任何 CSV 文件。
3. 🟡 **74–82% global coverage under A5** 与数据 (84.5%) 不符，差距较大。
