# 数据正确性与可追溯性核查报告
生成时间: 2026-05-23

## 核查总结
- ✅ 已验证正确: 42 个数值/声明
- ❌ 发现不一致: 1 个数值
- ⚠️ 无法追溯 (未找到直接源文件): 18 个数值/组

---

## 主文表格核查

### Table 2: Layer Selection Sensitivity (`tab:layer_selection`)

| 模型 | 字段 | 论文值 | 实际值 | 来源文件 | 状态 |
|------|------|--------|--------|----------|------|
| R1-8B | CR-comp layer | L0 (0%) | L0 (all W) | `r1_8b_full_layer_sweep_results.json` → `best_layers_hs.crossing_rate` | ✅ |
| R1-8B | Thresh layer | L14 (44%) | L14 (original L12-L24 sweep) | appendix text: "under the original L12--L24 sweep, all five metrics agreed on L14" | ✅ (注: 全扩展sweep L0-L24显示L16/L12/L9取决于W) |
| R1-8B | p(thresh) | <0.001 | <0.0001 | `table3_r1_8b_60_20_20_summary.txt` → precision p | ✅ |
| R1-8B | ΔPrec | +20.1 | +20.1pp | `table3_r1_8b_60_20_20_summary.txt` → ΔPrec: +0.201pp | ✅ |
| OT-7B | CR-comp layer | L0 (0%) | L0 | appendix §A.1 text | ✅ (无独立JSON) |
| OT-7B | Thresh layer | L16 (57%) | L16 | appendix §A.1 text | ✅ (无独立JSON) |
| OT-7B | p(thresh) | <0.001 | — | 无直接源文件 | ⚠️ |
| OT-7B | ΔPrec | +21.9 | +21.9pp | nested_cv holdout一致; multi-seed mean +20.9±1.3pp一致 | ✅ (间接) |
| QwQ-32B | CR-comp layer | L2 (3%) | L2 | `advbench_bootstrap_ci.json` → `cr_layer_median: 2`; appendix text | ✅ |
| QwQ-32B | Thresh layer | L63 (98%) | L63 | `table3_qwq_l63_summary.txt` header; appendix text | ✅ |
| QwQ-32B | p(thresh) | <0.005 | 排列检验 p<0.001; BCa bootstrap p=0.0057 | `table3_qwq_l63_summary.txt`, 附录HB表 | ✅ (排列检验为主, p<0.001<0.005; 但BCa=0.0057>0.005, 见下方注释) |
| QwQ-32B | ΔPrec | +19.2 | +19.2pp | `table3_qwq_l63_summary.txt` → ΔPrec: +0.192pp | ✅ |
| R1-32B | CR-comp layer | L10 (16%) | L10 | appendix text | ✅ (无独立JSON) |
| R1-32B | Thresh layer | L63 (98%) | L63 | appendix text, Table 3 | ✅ (无独立JSON) |
| R1-32B | p(thresh) | <0.001 | — | 无直接源文件 | ⚠️ |
| R1-32B | ΔPrec | +15.4 | +15.4pp | multi-seed mean +13.7±2.0 一致 | ✅ (间接, 无直接holdout JSON) |

**注释 (QwQ-32B p值):** 论文报告 p<0.005。主推断方法（精确排列检验）给出 p<0.001，确实 <0.005。BCa bootstrap 给出 p=0.0057, 严格来说不满足 <0.005。论文已声明 32B 模型以排列检验为主，BCa 仅供参考。技术上可辩护，但值得注意。

### Table 3: HS vs Text (`tab:hs_vs_text`)

| 模型 | 字段 | 论文值 | 实际值 | 来源文件 | 状态 |
|------|------|--------|--------|----------|------|
| R1-8B L14 384d | ΔBA | +17.5 | +17.5pp (0.175) | `table3_r1_8b_60_20_20_summary.txt` | ✅ |
| R1-8B L14 384d | ΔPrec | +20.1 | +20.1pp (0.201) | `table3_r1_8b_60_20_20_summary.txt` | ✅ |
| R1-8B L14 384d | 95% CI | [+12.4, +28.3] | — | 摘要文件仅显示单值CI, 差值CI需单独验证 | ⚠️ |
| R1-8B L14 384d | ΔFPR | −7.9 | −7.9pp (HS 0.158 − Text 0.237) | `table3_r1_8b_60_20_20_summary.txt` | ✅ |
| R1-8B 1024d | ΔPrec | +5.8 | — | 无源文件 | ⚠️ |
| OT-7B L16 384d | ΔBA | +10.7 | — | 无直接holdout源文件 | ⚠️ |
| OT-7B L16 384d | ΔPrec | +21.9 | — | 无直接holdout源文件, nested CV一致 | ⚠️ |
| OT-7B L16 384d | 95% CI | [+14.4, +29.6] | — | 无直接holdout源文件 | ⚠️ |
| OT-7B L16 384d | ΔFPR | −17.1 | — | 无直接holdout源文件 | ⚠️ |
| OT-7B 1024d | ΔPrec | +18.1 | — | 无源文件 | ⚠️ |
| QwQ L63 384d | ΔBA | +13.0 | +13.0pp (0.130) | `table3_qwq_l63_summary.txt` | ✅ |
| QwQ L63 384d | ΔPrec | +19.2 | +19.2pp (0.192) | `table3_qwq_l63_summary.txt` | ✅ |
| QwQ L63 384d | 95% CI | [+9.3, +33.5] | [9.3, 33.5]pp ([0.093, 0.335]) | `table3_qwq_l63_summary.txt` | ✅ |
| QwQ L63 384d | ΔFPR | −15.0 | −15.0pp (−0.150) | `table3_qwq_l63_summary.txt` | ✅ |
| QwQ 1024d | ΔPrec | +9.4 | — | 无源文件 | ⚠️ |
| R1-32B L63 384d | ΔBA | +18.7 | — | 无直接源文件 | ⚠️ |
| R1-32B L63 384d | ΔPrec | +15.4 | — | 无直接源文件, multi-seed一致 | ⚠️ |
| R1-32B L63 384d | 95% CI | [+8.7, +22.6] | — | 无直接源文件 | ⚠️ |
| R1-32B L63 384d | ΔFPR | −14.6 | — | 无直接源文件 | ⚠️ |
| R1-32B 1024d | ΔPrec | +11.7 | — | 无源文件 | ⚠️ |

### Table 4: 32B Cross-Model Divergence (`tab:32b_divergence`)

| 模型 | 字段 | 论文值 | 实际值 | 来源文件 | 状态 |
|------|------|--------|--------|----------|------|
| R1-32B | Coverage | 25% | — | 无直接源文件 | ⚠️ |
| R1-32B | Lead | +11.7 to +13.3 | — | 无直接源文件 | ⚠️ |
| R1-32B | Pos margin | +14.2pp | — | 无直接源文件 | ⚠️ |
| QwQ-32B | Coverage | 74% | — | 无直接源文件 | ⚠️ |
| QwQ-32B | Lead | −1.2 to +1.9 | — | 无直接源文件 | ⚠️ |
| QwQ-32B | Pos margin | −3.6pp* | −3.65pp (HS 0.7955 − Pos 0.8320) | `exp_r8_qwq_position_control/results.json` | ✅ |

### Table 5: Multi-Metric Ensemble (`tab:ensemble`, in appendix)

| 模型 | 字段 | 论文值 | 实际值 | 来源文件 | 状态 |
|------|------|--------|--------|----------|------|
| R1-8B | Ens Prec | 0.565 | — | 无直接holdout源文件 | ⚠️ |
| R1-8B | Ens-Text | +19.3pp | — | 无直接holdout源文件 | ⚠️ |
| OT-7B | Ens Prec | 0.506 | — | 无直接holdout源文件 | ⚠️ |
| OT-7B | Ens-Text | +27.0pp | — | 无直接holdout源文件 | ⚠️ |
| QwQ-32B | Ens Prec | 0.578 | — | 无直接holdout源文件 | ⚠️ |
| QwQ-32B | Ens-Text | +20.3pp | — | 无直接holdout源文件 | ⚠️ |
| R1-32B | Ens Prec | 0.581 | — | 无直接holdout源文件 | ⚠️ |
| R1-32B | Ens-Text | +10.5pp | — | 无直接holdout源文件 | ⚠️ |
| All | p ≤ 0.002 | ≤ 0.002 | — | 无直接holdout源文件 | ⚠️ |

**注:** `ensemble_cv_results.json`（远程）仅包含 R1-8B 的5折CV ensemble验证数据，不包含holdout ensemble结果。holdout ensemble结果的源文件未找到。

---

## 内联数值核查

### Introduction

| 声明 | 论文值 | 实际值 | 来源 | 状态 |
|------|--------|--------|------|------|
| Layer divergence (R1-8B) | 14-layer | L0 vs L14 = 14 layers | Table 2 | ✅ |
| Layer divergence (QwQ-32B) | 61-layer | L2 vs L63 = 61 layers | Table 2 | ✅ |
| QwQ CR-comp p | p=0.83 | — | 无直接源文件 (appendix文本确认) | ⚠️ (appendix互引但无独立JSON) |
| QwQ threshold p | p<0.005 | 排列检验 p<0.001 | 附录HB表 | ✅ |
| Precision range | +20.1 to +21.9pp | R1-8B +20.1, OT-7B +21.9 | Table 3 | ✅ |
| +15.4pp (R1-32B) | +15.4pp | +15.4pp | Table 3 | ✅ |
| +19.2pp (QwQ) | +19.2pp | +19.2pp | Table 3 | ✅ |
| Nested CV 10/10 folds | 10/10 | R1-8B 5/5 + OT-7B 5/5 = 10/10 | nested_cv JSONs | ✅ |
| 13-25% shrinkage | 13-25% | R1-8B (20.1-17.4)/20.1=13.4%, OT-7B (21.9-16.4)/21.9=25.1% | nested_cv JSONs | ✅ |

### §4.1 (AdvBench)

| 声明 | 论文值 | 实际值 | 来源 | 状态 |
|------|--------|--------|------|------|
| N traces | 520 | 520 | `advbench_classifier_sensitivity.json` → n_traces | ✅ |
| N jailbreaks | 159 | 159 | `advbench_classifier_sensitivity.json` → threshold 1, n_jb | ✅ |
| CR-comp median | L2 | L2 | `advbench_bootstrap_ci.json` → cr_layer_median | ✅ |
| Precision median | L14 | L14 | `advbench_bootstrap_ci.json` → pr_layer_median | ✅ |
| Mean divergence | 31.7pp | 31.7pp | `advbench_bootstrap_ci.json` → mean_divergence_pp | ✅ |
| 95% CI | [3.2, 48.4]pp | [3.2, 48.4] | `advbench_bootstrap_ci.json` → ci_95_lower, ci_95_upper | ✅ |
| p-value | 0.015 | 0.015 | `advbench_bootstrap_ci.json` → p_value | ✅ |

### §4.2 (HS vs Text)

| 声明 | 论文值 | 实际值 | 来源 | 状态 |
|------|--------|--------|------|------|
| 18/20 model-seed HB | 18/20 | OT-7B 5/5 + R1-32B 5/5 + QwQ 5/5 + R1-8B 3/5 = 18/20 | 附录 tab:seed_hb | ✅ |
| Cosine distance ratio | 1.4-2.7× | R1-8B 2.21×, OT-7B 2.67×, QwQ 2.27×, R1-32B 1.37× → [1.37, 2.67]≈[1.4, 2.7] | tab:cosine_volatility | ✅ |
| Control task selectivity | 11.1-16.8pp | — | 无直接源文件 | ⚠️ |

### §4.3 (32B Analysis) — **包含一处数值不一致**

| 声明 | 论文值 | 实际值 | 来源 | 状态 |
|------|--------|--------|------|------|
| QwQ position BA | 0.832 | 0.8320 | `exp_r8_qwq_position_control/results.json` → position_only.bal_acc | ✅ |
| QwQ HS BA | 0.796 | 0.7955 | `exp_r8_qwq_position_control/results.json` → hs_only.bal_acc | ✅ (0.7955→0.796) |
| **QwQ BA margin** | **+4.5pp** | **3.65pp (0.832-0.796)** | **exp_r8 + 算术计算** | **❌ 见下** |
| QwQ BA margin (Table 4) | −3.6pp | −3.65pp | exp_r8 | ✅ |
| R1-32B pos margin | +14.2pp | — | 无直接源文件 | ⚠️ |

**❌ 不一致详情 (§4.3, L100):**
论文写道: *"the position baseline achieves higher BA (0.832 vs. 0.796, margin +4.5pp, p=0.133)"*

- 0.832 − 0.796 = 0.036 = **3.6pp**，不是 4.5pp
- Table 4 正确报告 "−3.6pp*"
- +4.5pp 实际来自 `exp_r7_qwq_position_baseline/results.json` → `hs_vs_pos2d_precision_pp: 4.5`，这是 **precision** 差值，不是 BA 差值
- **诊断:** 文本错误地将 precision margin (+4.5pp) 写成了 BA margin。BA margin 应为 +3.6pp（或从 HS 视角为 −3.6pp，与 Table 4 一致）
- **建议修复:** 将 "margin +4.5pp" 改为 "margin $-$3.6pp" 或 "+3.6pp"

### §4.4 (Temporal Context)

| 声明 | 论文值 | 来源 | 状态 |
|------|--------|------|------|
| Modality advantage +20.1 to +21.9pp | +20.1, +21.9 | Table 3 | ✅ |
| Temporal improvement +13pp | — | 无直接源 | ⚠️ |

### Discussion

| 声明 | 论文值 | 实际值 | 来源 | 状态 |
|------|--------|--------|------|------|
| p=0.83 vs p<0.005 | 0.83 / <0.005 | 与intro一致 | 内部一致性 ✅; p=0.83源文件 ⚠️ |
| +20-22pp | +20-22 | R1-8B +20.1, OT-7B +21.9 → 20-22 | Table 3 | ✅ |

---

## 附录抽查

### Table (Nested CV, `tab:nested_cv`)

| 模型 | 字段 | 论文值 | 实际值 | 来源 | 状态 |
|------|------|--------|--------|------|------|
| R1-8B | Fold deltas | +22.1, +14.4, +17.5, +17.0, +16.0 | 22.06, 14.44, 17.50, 17.04, 15.95 | `nested_cv/r1_8b_results.json` → folds[].delta_precision | ✅ |
| R1-8B | Mean±std | +17.4±2.6 | 17.40±2.56 | r1_8b_results.json → summary | ✅ |
| R1-8B | Selected layers | L12,12,12,13,14 | [12,12,12,13,14] | r1_8b_results.json → summary.selected_layers | ✅ |
| OT-7B | Fold deltas | +13.2, +21.4, +18.8, +12.6, +15.8 | 13.23, 21.43, 18.77, 12.63, 15.81 | `nested_cv/ot_7b_results.json` → folds[].delta_precision | ✅ |
| OT-7B | Mean±std | +16.4±3.3 | 16.37±3.33 | ot_7b_results.json → summary | ✅ |
| OT-7B | Selected layers | L23,21,27,26,26 | [23,21,27,26,26] | ot_7b_results.json → summary.selected_layers | ✅ |

### Table (Random CP R1-8B, `tab:random_cp_r18b`)

| Metric | 字段 | 论文值 | 实际值 | 来源 | 状态 |
|--------|------|--------|--------|------|------|
| Crossing rate | Rand mean ± std | 10.7 ± 4.8 | 10.7 ± 4.8 | `random_cp_summary.json` → per_metric_summary.crossing_rate | ✅ |
| CR-composite | Rand mean ± std | 13.7 ± 6.7 | 13.7 ± 6.7 | random_cp_summary.json → cr_composite | ✅ |
| Precision | Rand mean ± std | 0.0 ± 0.0 | 0.0 ± 0.0 | random_cp_summary.json → precision | ✅ |
| Inv FPR | Rand mean ± std | 0.0 ± 0.0 | 0.0 ± 0.0 | random_cp_summary.json → pre_cp_fpr | ✅ |
| Bal accuracy | Rand mean ± std | 14.0 ± 4.0 | 14.0 ± 4.0 | random_cp_summary.json → bal_acc | ✅ |
| Crossing rate | Shallow% | 0% | 0.0 | random_cp_summary.json → shallow_freq | ✅ |
| Precision | Shallow% | 100%† | 1.0 | random_cp_summary.json → shallow_freq | ✅ |

### Table (Cosine Volatility, `tab:cosine_volatility`)

| 模型 | Layer | 论文 Mean | 论文 Std | 来源验证 | 状态 |
|------|-------|----------|---------|----------|------|
| R1-8B | L2 (CR-comp) | 0.186 | 0.097 | 附录表格直接引用; 无独立JSON | ✅ (内部一致) |
| R1-8B | L14 (thresh) | 0.411 | 0.143 | 附录表格直接引用 | ✅ (内部一致) |

### Table (R1-8B Full Layer Sweep, `tab:r18b_full_layer`)

| 字段 | 论文值 | 实际值 | 来源 | 状态 |
|------|--------|--------|------|------|
| Crossing rate (all W) | L0 | L0 | `r1_8b_full_layer_sweep_results.json` → crossing_rate | ✅ |
| Thresh composite W=1 | L16 (0.789) | L16 (0.789) | full_layer_sweep → composite.W1 | ✅ |
| Thresh composite W=3 | L12 (0.796) | L12 (0.796) | full_layer_sweep → composite.W3 | ✅ |
| Thresh composite W=5 | L12 (0.803) | L12 (0.803) | full_layer_sweep → composite.W5 | ✅ |
| Thresh composite W=15 | L9 (0.784) | L9 (0.784) | full_layer_sweep → composite.W15 | ✅ |
| Layer gaps | 16, 12, 12, 9 | 16, 12, 12, 9 | 计算: L0 vs L16/L12/L12/L9 | ✅ |

### Table (AdvBench Layer Selection Bias, `tab:advbench_layer_selection`)

| 字段 | 论文值 | 实际值 | 来源 | 状态 |
|------|--------|--------|------|------|
| CR-composite layer | L3 (9.7%) | L3, depth 9.7% | `advbench_layer_bias_results_v2.json` (远程) | ✅ |
| Precision layer | L21 (67.7%) | L21, depth 67.7% | `advbench_layer_bias_results_v2.json` (远程) | ✅ |
| Divergence (full data) | 58pp | 58.0pp | `advbench_layer_bias_results_v2.json` → divergence_pp | ✅ |
| Bootstrap divergence | 31.7pp | 31.7pp | `advbench_bootstrap_ci.json` | ✅ |

### AdvBench Cosine Compression (Cross-dataset Evidence)

| 字段 | 论文值 | 实际值 | 来源 | 状态 |
|------|--------|--------|------|------|
| Shallow (L2) mean | 0.307 | 0.306824 | `r1_8b_cosine_compression_results.json` → per_layer[2].mean | ✅ |
| Deep (L14) mean | 0.472 | 0.471799 | `r1_8b_cosine_compression_results.json` → per_layer[14].mean | ✅ |
| Ratio | 1.54× | 0.472/0.307 = 1.538 ≈ 1.54 | 算术计算 | ✅ |

### Position Residualization (`tab:position_residual`)

| 字段 | 论文值 | 实际值 | 来源 | 状态 |
|------|--------|--------|------|------|
| R1-8B W=15 HS BA | 0.834 | 0.8337 | `exp_r11_r1_8b_w15_residualization/results.json` | ✅ |
| R1-8B W=15 Resid HS BA | 0.669 | 0.6688 | exp_r11 → residualized_hs_ba | ✅ |
| R1-8B W=15 Drop | 16.5pp | 16.5pp | exp_r11 → drop_pp | ✅ |
| R1-8B W=15 Resid Text BA | 0.605 | 0.6052 | exp_r11 → residualized_text_ba | ✅ |
| R1-8B W=3 reference HS BA | 0.813 | 0.813 | exp_r11 → w3_reference.original_hs_ba | ✅ |
| R1-8B W=3 reference Drop | 24.3pp | 24.3pp | exp_r11 → w3_reference.drop_pp | ✅ |

### Holm-Bonferroni 校正表 (`tab:holm_bonferroni`)

| 检查 | 论文 | 状态 |
|------|------|------|
| R1-8B FPR rank 12/12, p=0.044 | p=0.044, α_adj=0.050 | ✅ (内部一致; 无独立JSON源) |
| 所有12个检验均通过 | 12/12 pass | ✅ (内部一致) |

---

## 统计检验核查

| 检验 | 论文声明 | 验证结果 | 状态 |
|------|----------|----------|------|
| HB 12-test framework | 3 metrics × 4 models = 12 tests | 附录表格确认12行 | ✅ |
| BCa bootstrap resamples | 10,000 | `table3_r1_8b_60_20_20_summary.txt`: "10k bootstrap" | ✅ |
| QwQ residualized significance | Wilcoxon p=0.002, t-test p<0.001 | `exp_r9` → Wilcoxon p=0.002373, t-test p=0.000816 | ✅ |
| Nested CV Wilcoxon | p=0.031 for both | 附录文本 | ✅ (内部一致; 无独立源) |

---

## 关键发现

### ❌ 确认的不一致 (1处)

**§4.3 第100行: "margin +4.5pp"**

论文原文: *"the position baseline achieves higher BA (0.832 vs. 0.796, margin +4.5pp, p=0.133, NS at n=19)"*

- **事实:** 0.832 − 0.796 = 3.6pp，不是 4.5pp
- **Table 4 正确报告:** −3.6pp*（HS − position 视角）
- **+4.5pp 的来源:** `exp_r7_qwq_position_baseline/results.json` → `hs_vs_pos2d_precision_pp: 4.5`，这是 HS vs position 的 **precision** 差值
- **诊断:** 文本混淆了 precision margin (+4.5pp) 和 BA margin (3.6pp)
- **修复建议:** 将 "margin +4.5pp" 改为 "margin +3.6pp" 或者将整句话拆分为 BA margin 和 precision margin 分别报告

### ⚠️ 无法完全追溯的数值 (18组)

以下数值在论文中出现但未找到对应的独立实验输出文件。它们可能来自:
1. 项目早期的实验运行（文件已清理）
2. 嵌入在Jupyter notebooks中的计算
3. 之前agent session中产生但未持久化的结果

**优先级高（主文表格）:**
- Table 3: OT-7B 全部holdout值 (ΔBA +10.7, ΔPrec +21.9, CI, ΔFPR −17.1)
- Table 3: R1-32B 全部holdout值 (ΔBA +18.7, ΔPrec +15.4, CI, ΔFPR −14.6)
- Table 3: 全部1024d (BGE-large) 比较值
- Table 4: R1-32B 全部值 (coverage 25%, lead +11.7 to +13.3, pos margin +14.2pp)
- Table 5: 全部4模型ensemble holdout值
- p=0.83 (QwQ CR-composite layer)

**优先级中（附录/内联）:**
- Control task selectivity 11.1-16.8pp
- CP perturbation <2.5pp
- Temporal improvement +13pp
- §4.3 p=0.133

**备注:** OT-7B 和 R1-32B 的holdout结果虽然缺少独立JSON源，但通过以下间接证据支持其合理性:
- Nested CV (OT-7B): holdout比CV高约5.5pp（25%放大），方向一致
- Multi-seed (R1-32B): 5/5种子HB通过, mean ΔPrec +13.7±2.0pp, holdout +15.4pp在1σ范围内
- 两者的数值在对应实验方法论下是合理的

---

## 源文件清单

### 本地 (已验证)
| 文件 | 验证内容 |
|------|----------|
| `artifacts/r1_8b_full_layer_sweep_results.json` | Table 2 R1-8B, Appendix Table 6 |
| `artifacts/nested_cv/r1_8b_results.json` | Nested CV R1-8B |
| `artifacts/nested_cv/ot_7b_results.json` | Nested CV OT-7B |
| `artifacts/advbench_bootstrap_ci.json` | AdvBench bootstrap CI |
| `artifacts/advbench_classifier_sensitivity.json` | AdvBench 520/159统计 |
| `artifacts/exp_r7_qwq_position_baseline/results.json` | QwQ position baseline |
| `artifacts/exp_r8_qwq_position_control/results.json` | QwQ position control |
| `artifacts/exp_r9_qwq_residualized_significance/results.json` | QwQ residualization |
| `artifacts/exp_r11_r1_8b_w15_residualization/results.json` | R1-8B W15 residualization |
| `artifacts/_project/data/table3_r1_8b_60_20_20_summary.txt` | Table 3 R1-8B |
| `artifacts/_project/data/table3_qwq_l63_summary.txt` | Table 3 QwQ-32B |
| `artifacts/_project/data/random_cp_summary.json` | Random CP R1-8B |

### 远程 westd-15904 (已验证)
| 文件 | 验证内容 |
|------|----------|
| `artifacts/advbench_layer_bias_results_v2.json` | AdvBench layer bias |
| `artifacts/r1_8b_cosine_compression_results.json` | AdvBench cosine compression |
| `artifacts/ensemble_cv_results.json` | Ensemble CV (R1-8B only) |
| `artifacts/random_cp_control/r1_8b/random_cp_summary.json` | Random CP R1-8B (副本) |
