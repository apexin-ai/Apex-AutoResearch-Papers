# 提交前全量数据正确性与可追溯性审计
**日期**: 2026-05-23 | **审计员**: Agent | **论文版本**: v34+ submission-ready

## 任务 1: 论文核心数字追溯

### Abstract & Introduction

| 数字 | 论文位置 | 来源文件 | 原始值 | 匹配? |
|------|---------|---------|--------|------|
| semipartial R²=0.273 | abstract L3, results §4.3 | `artifacts/semipartial_r2_verification.json` L25 | delta_R2_BCS: 0.272922 | ✅ |
| VIF=1.18 | abstract L3, results §4.3 | `artifacts/semipartial_r2_verification.json` L36 | VIF_approx: 1.18; `r1_statistical_supplements.json` L13: vif_bcs: 1.182 | ✅ |
| TOST p=0.003 | abstract L3, results §4.4 | `logs/workers/worker_exp_fewrel_factorial_tost_*.json`: TOST p=0.003 at ±3pp margin (n=69, 5 count levels) | 0.003 | ✅ |
| count degradation −49pp | abstract L3, intro L5 | DocRED: `artifacts/exp_docred_confusability/count_curve_results.json`: count_1=0.88, count_96=0.387 → Δ=−49.3pp | −49.3→"up to −49" | ✅ |
| NER recall 0.72 (count 1) | intro L5, results §4.1 | `artifacts/fig_count_curves_v2.py` L51: ner_mean[0]=0.720 | 0.720 | ✅ |
| NER recall 0.51 (count 2) | results §4.1 | `artifacts/fig_count_curves_v2.py` L51: ner_mean[1]=0.515 | 0.515→0.52 | ⚠️ 截断非四舍五入 |
| NER recall 0.27 (count 22) | results §4.1 | `artifacts/fig_count_curves_v2.py` L51: ner_mean[4]=0.279 | 0.279→0.28 | ⚠️ 截断非四舍五入 |
| NER recall 0.41 (count 66) | results §4.1 | `artifacts/fig_count_curves_v2.py` L51: ner_mean[6]=0.407 | 0.407→0.41 | ✅ |
| RE 85.7%→50.4% (FewRel) | intro L5, results §4.1 | `artifacts/fig_count_curves_v2.py` L46: re_mean=[0.857, ..., 0.504] | 0.857, 0.504 | ✅ |
| RE 88.0%→38.7% (DocRED) | results §4.1 | `artifacts/exp_docred_confusability/count_curve_results.json`: count_1=0.88, count_96=0.387 | 0.88, 0.387 | ✅ |

### 核心实验结果 (§4.x)

| 数字 | 论文位置 | 来源文件 | 原始值 | 匹配? |
|------|---------|---------|--------|------|
| Pairwise SCS r=0.112 (NER) | Table 1, §4.2 | provenance C009 → exp002_confusability_controlled | Pearson r=0.112 [0.076, 0.156] (n=1953) | ✅ |
| Pairwise SCS r=0.129 (MAVEN) | Table 1, §4.2 | provenance C028 → exp004_maven_bcs | MAVEN MiniLM r=0.129 [0.104, 0.156] | ✅ |
| IntraSub ρ=1.0 (Few-NERD) | §4.4, Table 2 | provenance C025 → exp007_error_taxonomy | NER IntraSub ρ=1.0 (p<0.001) | ✅ |
| IntraSub ρ=0.954 (FewRel) | §4.4, Table 2 | provenance C025 → exp016_fewrel_error_taxonomy | RE IntraSub ρ=0.954 (p<1e-6) | ✅ |
| IntraSub ρ=0.843 (DocRED) | §4.4, Table 2 | registry exp_docred_error_taxonomy | ρ=0.843 (p=8.1e-31, n=110) | ✅ |
| BCS–acc r=-0.22, R²≈0.05 (n=100) | §4.3 practical magnitude | provenance C033 → exp_fewrel_80pool_16sub_bootstrap | r=-0.221, p=0.027 | ✅ |
| DocRED ρ=-0.762 (count 16, n=55) | §4.3 | registry exp_docred_bcs_expanded | spearman_r=-0.762 (count16, n=55) | ✅ |
| DocRED ρ=-0.693 (count 32, n=55) | §4.3 | registry exp_docred_bcs_expanded | spearman_r=-0.693 (count32, n=55) | ✅ |
| Format indep. r=-0.45 constrained | §4.3, Appendix | registry exp_paired_constrained | Pearson r=-0.4479 | ✅ |
| Format indep. r=-0.44 unconstrained | §4.3, Appendix | registry exp_paired_constrained | Pearson r=-0.4393 | ✅ |
| Format indep. Fisher z=-0.04, p=0.97 | §4.3, Appendix | registry exp_paired_constrained | z=-0.036→-0.04, p=0.972→0.97 | ✅ |
| Qwen3-32B Δ=-31.2pp | §4.3, Fig 1b | provenance C022 → exp_fewrel_formal_80rel; `gen_fig_bcs_scaling.py` L29: bcs_effect_qwen[2]=31.2 | 31.2pp | ✅ |
| LLaMA-8B Δ=-27.1pp | §4.3, Table 3 | provenance C013 → exp012_llama_fewrel_ch2; `gen_fig_bcs_scaling.py`: bcs_effect_llama_80=27.1 | 27.1pp | ✅ |
| LLaMA-70B Δ=-10.9pp (count 16) | §4.3, Table 3 | `checkpoints/exp_llama70b_cross_model_*.json` L37: delta_pp=10.94 | 10.94→10.9 | ✅ |
| Gemini 2.5 Flash Δ=-17.6pp | §4.3, Table 3 | registry exp_gemini_flash_bcs_controlled: gap_pp=-17.6 (count_8) | -17.6 | ✅ |
| Oracle routing 0.802 (RE) | §5 SDGD | `checkpoints/exp_confusability_batch_composition_DONE_*.json` L30: accuracy=0.8021 | 0.8021→0.802 | ✅ |
| Single-pass 0.504 (RE) | §5 SDGD | `fig_count_curves_v2.py` L46: re_mean[7]=0.504; provenance C018 | 0.504 | ✅ |
| SDGD NER F1 0.445→0.251 | §5 SDGD | provenance C030 → exp008_sdgd_zero_fewnerd_r2: single_pass=0.4451, sdgd_zero=0.2514 | 0.445, 0.251 | ✅ |
| SDGD precision 0.56→0.21 | §5 SDGD | provenance C031 → exp008: single_pass P=0.5631, sdgd_zero P=0.210 | 0.563→0.56, 0.210→0.21 | ✅ |
| MAVEN SDGD F1 0.207→0.123 | §5, Appendix | registry exp_sdgd_zero_maven: single_pass F1=0.2068, sdgd_zero F1=0.1233 | 0.207, 0.123 | ✅ |
| Domain entropy p=0.97 | §4.3 | `artifacts/analysis_w3_domain_control.json` | p_entropy=0.97 | ✅ |

### 不匹配/需关注的数字

**⚠️ NER 截断 vs 四舍五入 (2处, 影响 ≤1pp)**

| 位置 | 论文值 | 源数据值 | 标准四舍五入 | 差异 |
|------|--------|----------|------------|------|
| results.tex §4.1 "count 2" | 0.51 | 0.515 | 0.52 | −1pp |
| results.tex §4.1 "count 22" | 0.27 | 0.279 | 0.28 | −1pp |

**建议**: 改为 0.52 和 0.28，或统一使用 floor 规则并注明。当前与同段其他数值(0.72, 0.41)的四舍五入规则不一致。

**⚠️ Provenance YAML 过时 (1处, 不影响论文)**

| 字段 | provenance 值 | 原始数据值 | 论文值 |
|------|-------------|-----------|--------|
| C040 DocRED count_1 | 0.875 | 0.88 | 88.0% ✅ |
| C040 DocRED count_96 | 0.392 | 0.387 | 38.7% ✅ |

论文数值与原始数据一致，但 provenance YAML 记录过时。不影响提交。

## 任务 2: 图表数据一致性

### Figure 1a (Count Curves)
- **源数据**: `artifacts/fig_count_curves_v2.py` L44-52
- FewRel RE: [0.857, 0.870, 0.805, 0.719, 0.652, 0.606, 0.539, 0.504] at counts [1,4,8,16,32,40,64,80]
- Few-NERD NER: [0.720, 0.515, 0.399, 0.318, 0.279, 0.309, 0.407] at counts [1,2,6,12,22,44,66]
- **匹配**: Figure 由此脚本生成，数据内嵌于脚本 ✅
- **交叉验证**: RE 值与 `d051_fewrel_n25_s42/count_curve_summary.json` 一致 ✅

### Figure 1b (BCS Scaling)
- **源数据**: `artifacts/anonymous_github/scripts/gen_fig_bcs_scaling.py` L29-35
- bcs_effect_qwen = [9.1, 33.3, 31.2]; bcs_effect_llama_80 = 27.1
- **匹配**: 与 provenance C022, C013, exp_fewrel_formal_80rel 一致 ✅

### Table 1 (Pairwise SCS–confusion)
- Few-NERD: r=0.112, r²=0.013, 95% CI [0.076, 0.156], n=1953 → exp002 ✅
- MAVEN: r=0.129, r²=0.017, 95% CI [0.104, 0.156], n=11026 → exp004 ✅

### Table 2 (Error taxonomy)
- NER IntraSub 0%→49.4%, ρ=1.0 → exp007 ✅
- RE IntraSub 0%→32.3%, ρ=0.954 → exp016 ✅
- DocRED IntraSub ρ=0.843 → exp_docred_error_taxonomy ✅

### Table 3 (Cross-model BCS)
- Qwen3 count_8 Δ=-31.2pp → exp_fewrel_formal_80rel ✅
- LLaMA-8B count_8 Δ=-27.1pp → exp012 ✅
- LLaMA-70B count_16 Δ=-10.9pp → exp_llama70b_cross_model (10.94pp) ✅
- Gemini count_8 Δ=-17.6pp → exp_gemini_flash_bcs_controlled ✅

## 任务 3: 统计分析可复现性

### 代码包内容 (`artifacts/anonymous_github/`)
- **85 文件**: src/ (核心代码 41文件), scripts/ (实验脚本 24文件), configs/ (3 JSON), data/ (README)
- **完整覆盖**: batch composition, error taxonomy, pairwise confusion, bootstrap CI, per-type analysis, SDGD decomposition, count curves, BCS-controlled experiments

### 核心统计分析脚本状态

| 分析 | 代码包内脚本 | 状态 |
|------|------------|------|
| Bootstrap CI | `src/bootstrap_ci.py`, `src/run_fewrel_16rel_bootstrap.py`, `src/run_fewrel_80pool_16sub_bootstrap.py` | ✅ 在代码包 |
| Error taxonomy | `src/error_taxonomy.py`, `src/fewrel_error_taxonomy.py` | ✅ 在代码包 |
| Partial correlation | `src/per_type_analysis.py`, `src/analyze_results.py` | ✅ 在代码包 |
| Regression slope | `scripts/d033_regression_slope.py`, `scripts/three_way_comparison.py` | ✅ 在代码包 |
| Cluster bootstrap | `scripts/d037/w3_cluster_bootstrap.py` | ✅ 在代码包 |
| Aggregation simulation | `scripts/aggregation_monte_carlo.py` | ✅ 在代码包 |
| **Semipartial R²** | 无专用脚本 | 🔴 **不在代码包** |
| **TOST equivalence** | 无专用脚本 | 🔴 **不在代码包** |
| **Permutation equivalence** | `artifacts/permutation_equivalence_test.py` (在 artifacts, 不在代码包) | 🟡 需移入代码包 |
| **Range-matched interaction** | 无专用脚本 | 🔴 **不在代码包** |

### 输入数据完整性
- `configs/`: 类型配置 (Few-NERD 66类, FewRel 80关系, MAVEN 168事件) ✅
- `data/README.md`: 外部数据集下载指南 ✅
- 中间结果 (embeddings, confusion matrices): 需用户按 README 生成 ✅
- `requirements.txt`: 14 依赖包完整 ✅

## 总结

### 通过 (28/30 数字)
所有核心定量 claim 均可追溯至实验输出文件，原始值与论文一致。

### 需处理 (按优先级)

**P0 — 代码包缺失脚本 (影响可复现性)**:
1. Semipartial R² 计算脚本（`r1_statistical_supplements.py` 或等价物）
2. TOST equivalence test 脚本
3. `permutation_equivalence_test.py` 从 artifacts/ 移入 `anonymous_github/scripts/`
4. Range-matched interaction 分析脚本

**P1 — NER 截断问题 (影响数据准确性)**:
- results.tex 中 count_2=0.51 应为 0.52，count_22=0.27 应为 0.28

**P2 — Provenance YAML 过时 (不影响提交)**:
- C040 DocRED 数值需更新为 0.88/0.387
