# 图表数据审计

## 统计
- 审计图表总数：14（含正文 7 + 附录 7；另有 ~9 个附录图无本地脚本，仅验证 caption 数字）
- 数据点总数：~750（硬编码在脚本中的数值）
- 完全匹配：12
- 问题：2（1 个数据不一致，1 个文本不一致）

---

## 逐图审计

### Figure 1 (fig_teaser): VLA Architecture + 32-Layer Attention Bar
- 脚本：`scripts/plot_teaser.py`
- 数据源：硬编码（32-layer bulk extraction）
- 数据：vla_trained[32], pretrained[32]
- Caption 数字：无具体数字
- 数据匹配：✅
- 详情：teaser 的 32-layer 数据与 multi-layer 4-point 采样使用不同提取方式（bulk vs dedicated），已知差异（appendix 有注释 "threshold boundary effects"）。teaser L32=18 与 appendix table L31=18 一致。

### Figure 2 (fig_overview): Analysis Framework Diagram
- 脚本：`scripts/plot_overview.py`
- 数据源：概念图，无数值数据
- 数据匹配：✅ (N/A)
- 详情：纯架构/方法论示意图，无需数值审计。

### Figure 3 (fig_result_matrix): Cross-Architecture Heatmap
- 脚本：`scripts/gen_fig_matrix_heatmap.py`
- 数据源：硬编码（与 Table 1 一致）
- Caption 数字：ΔR² > 0.10 threshold
- 数据匹配：✅
- 详情：全部 10 个有效 cell 的 ΔR² 值与 Table 1 (tab:cross_arch_matrix) 完全一致：
  - OpenVLA: Goal 0.086, Spatial 0.037, Object 0.037, Long 0.033
  - TraceVLA: Goal 0.333, Spatial 0.156, Object 0.362, Long 0.358
  - NORA: Goal 0.455, Spatial 0.308, Object/Long N/A

### Figure 4 (fig_action_r2_threecond): Per-Layer R² Three Conditions
- 脚本：`scripts/plot_action_r2_threecond.py`
- 数据源：硬编码（3-seed mean ± std, 32 layers × 3 conditions = 192 values）
- Caption 数字："all share L0 (R² = 0.645)", "Trained model peaks at L9"
- 数据匹配：✅
- 详情：
  - L0 共享值：trained_mean[0] = llama2base_mean[0] = untrained_mean[0] = 0.6451 → 0.645 ✓
  - Trained L9: trained_mean[9] = 0.6434 → 0.643（3dp 四舍五入）✓
  - L0 是 embedding 层，L9 是 transformer 处理后的峰值——framing 正确
  - Appendix text: "L9 (R² = 0.643 ± 0.014)" — trained_std[9] = 0.0137 → 0.014 ✓
  - L0 baseline 水平线：y=0.645 ✓

### Figure 5 (fig_counterfactual_bar): Counterfactual Sensitivity
- 脚本：`scripts/plot_counterfactual_bar.py`
- 数据源：硬编码（Panel A: 8×4=32 Cohen's d; Panel B: 8×4=32 cosine dist）
- Caption 数字："E=empty, W=wrong, S=shuffled, P=paraphrased", "dashed: d=0.8"
- 数据匹配：✅
- 详情：
  **Panel A (Cohen's d) 与 Appendix Table 7 (tab:counterfactual) 逐值核对：**
  | Cell | Script [E,W,S,P] | Table ranking | Match |
  |------|-----------------|---------------|-------|
  | OV-G | [1.17, 1.18, 1.10, 1.00] | W 1.18, E 1.17, S 1.10, P 1.00 | ✅ |
  | OV-S | [1.17, 0.89, 0.98, 0.81] | E 1.17, S 0.98, W 0.89, P 0.81 | ✅ |
  | OV-O | [1.21, 1.19, 1.12, 0.90] | E 1.21, W 1.19, S 1.12, P 0.90 | ✅ |
  | OV-L | [0.51, 0.55, 0.57, 0.45] | S 0.57, W 0.55, E 0.51, P 0.45 | ✅ |
  | TV-G | [1.52, 1.40, 1.34, 1.21] | E 1.52, W 1.40, S 1.34, P 1.21 | ✅ |
  | TV-S | [1.33, 1.17, 1.30, 1.18] | E 1.33, S 1.30, P 1.18, W 1.17 | ✅ |
  | TV-O | [1.21, 1.06, 1.16, 0.97] | E 1.21, S 1.16, W 1.06, P 0.97 | ✅ |
  | TV-L | [1.47, 1.42, 1.39, 1.16] | E 1.47, W 1.42, S 1.39, P 1.16 | ✅ |

  **Main text claims 验证：**
  - "Empty ranks first in 6/8 cells": OV-G(W first), OV-S(E), OV-O(E), OV-L(S first), TV-G(E), TV-S(E), TV-O(E), TV-L(E) → 6/8 ✅
  - "Paraphrased ranks last in 7/8": all except TV-S where W=1.17 is last → 7/8 ✅
  - "TraceVLA d = 0.97–1.52": min TV-O P=0.97, max TV-G E=1.52 ✅
  - "OpenVLA d = 0.45–1.21": min OV-L P=0.45, max OV-O E=1.21 ✅

  **Panel B (Cosine distance) 与 analysis reports 核对：**
  - NORA Goal trained saturates: [1.0, 1.0, 1.0, 1.0] ✅
  - Phi-3-Vision Goal (untrained): [0.1530, 0.0160, 0.0839, 0.0043] — 与 cf_batch_part2 report (E=0.153, W=0.016, S=0.084, P=0.004) 一致 ✅
  - Phi-3-Vision Spatial: [0.1805, 0.0046, 0.1395, 0.0044] — 与 cf_batch_missing report (E=0.180, S=0.140, W=0.005, P=0.004) 一致 ✅
  - Phi-3-Vision Object: [0.1850, 0.0044, 0.0977, 0.0052] — 与 report (E=0.185, S=0.098, W=0.004, P=0.005) 一致 ✅

  **已知问题验证 — TraceVLA Spatial/Object wrong↔shuffled：**
  ✅ **NOT AN ISSUE**。通过 `cf_batch_missing_v1_analysis.md` 和 `cf_batch_part2_v1_analysis.md` 交叉验证，trained ordering 与脚本中的条件映射完全一致：
  - TV-S trained: E(1.33) > S(1.30) > P(1.18) > W(1.17) — report confirms "E > S > P > W"
  - TV-O trained: E(1.21) > S(1.16) > W(1.06) > P(0.97) — report confirms "E > S > W > P"
  条件数组 `['empty', 'wrong', 'shuffled', 'paraphrased']` 映射正确，wrong 和 shuffled 未交换。

### Figure 6 (fig_r2_collapse): Layer-Wise R² Three-Panel
- 脚本：`scripts/plot_r2_collapse.py`
- 数据源：硬编码（3 panels × 2 curves = 6 arrays, total ~200 values）
- Caption 数字："ΔR² = 0.16–0.46", "< 0.09", "ΔR² = 0.000", "R² = 0.155"
- 数据匹配：✅
- 详情：
  **Peak/exit/ΔR² 与 Table 1 核对：**
  | Panel | Peak idx | Peak R² | Exit R² | ΔR² | Table | Match |
  |-------|----------|---------|---------|-----|-------|-------|
  | OpenVLA tr | L1 | 0.418 | 0.331 | 0.086 | 0.086 | ✅ |
  | OpenVLA ref | L27 | 0.423 | 0.367 | 0.056 | 0.056 | ✅ |
  | TraceVLA tr | L13 | 0.540 | 0.207 | 0.333 | 0.333 | ✅ |
  | TraceVLA ref | L11 | 0.505 | 0.440 | 0.065 | 0.065 | ✅ |
  | NORA tr | L8 | 0.449 | -0.006 | 0.455 | 0.455 | ✅ |
  | NORA ref | L5 | 0.420 | 0.340 | 0.081 | 0.081 | ✅ |

  - NLP_VAL = 0.155 in script, caption says "R² = 0.155" ✅
  - Caption "ΔR² = 0.16–0.46": full range across table is 0.156–0.455 ✅
  - Caption "< 0.09": OpenVLA max trained ΔR² = 0.086 < 0.09 ✅
  - NLP_VAL 使用单一值 0.155 代表三个不同 NLP 模型（见下方 ℹ️ 注释）

### Figure 7 (fig_synthesis_panels): Multi-Layer Attention + Dose-Response
- 脚本（左）：`scripts/plot_multi_layer_attention.py`
- 脚本（右）：`scripts/plot_dose_response.py`
- Caption 数字："L1: 24, L31: 18" (left); "d = 0.48–0.64" (right)
- 数据匹配：⚠️ 左 panel L31 值不一致

  **左 Panel (Multi-Layer Attention):**
  - Script: trained_heads = [24, 4, 10, 19] for [L1, L8, L16, L31]
  - Main text: "L1: 24, L31: 18"
  - Appendix Table 10: L31 Trained = 18/32
  - **⚠️ 脚本 L31 = 19, 论文 = 18** — 差值 1 head
  - L1=24, L8=4, L16=10 与 appendix table 一致 ✅
  - Llama-2 base: script [9, 8, 25, 8] 与 table [9, 8, 25, 8] ✅
  - Untrained: script [0, 0, 0, 0] 与 table [0, 0, 0, 0] ✅

  **右 Panel (Dose-Response):**
  - Script values 与 Appendix Table 8 (tab:dose_response) 逐值核对（8 data points + 16 CI bounds）：全部匹配 ✅
  - d range: 0.482–0.639 → "0.48–0.64" ✓
  - Control line: ref_control_d = 0.41 — appendix "d = 0.41" ✅

### Figure (fig_rsa_perlayer_curve): Per-Layer RSA
- 脚本：`scripts/plot_rsa_perlayer.py`
- 数据源：硬编码（4 curves × 33 layers + CI bounds）
- Caption 数字："Trained: inverted-U peaking at L12; reference: monotonic decline"
- 数据匹配：✅
- 详情：
  - Trained image_mean peak: L12, ti_m[12] = 0.6282 → "0.628" ✓
  - Trained readout peak: L12, tp_m[12] = 0.6425 → "0.643" ✓
  - Method.tex says ρ = 0.584 (readout exit) and 0.422 (image_mean exit): tp_m[32]=0.5843→0.584 ✅, ti_m[32]=0.4223→0.422 ✅

### Figure (fig_l1_attention / fig_cross_arch_l1): Cross-Architecture L1 Bar
- 脚本：`scripts/plot_l1_attention.py`
- 数据源：硬编码
- Caption 数字：无具体数字
- 数据匹配：⚠️ 附近文本值不完全匹配
- 详情：
  - Script: ref_counts = [26, 32, 14], trained_counts = [23, 29, 13]
  - Appendix paragraph near figure: "OpenVLA: 23/32 vs. 26/32" ✅
  - Appendix paragraph: "TraceVLA: **27**/32 vs. 32/32" — script plots **29**/32 ⚠️
  - Appendix paragraph: "NORA: 13/16 vs. **13**/16" — script ref = **14**/16 ⚠️
  - experiments.tex 使用范围值 "27–30/32" 和 "13–14/16"，script 值在范围内
  - Main text 对 OpenVLA 使用 dedicated analysis 值 24/32，与此图的 bulk extraction 值 23/32 是已知方法差异（documented in appendix）

### Figure (fig_training_dynamics): ΔR² Strip Plot
- 脚本：`scripts/plot_training_dynamics.py`
- 数据源：硬编码（与 Table 1 相同数据）
- Caption 数字：无
- 数据匹配：✅
- 详情：全部 23 个数据点与 Table 1 逐值一致（4 VLA→VLA trained, 6 VLM→VLA trained, 10 reference, 3 NLP）。

### Figure (fig_label_permutation): Label Permutation Control
- 脚本：`scripts/plot_label_permutation.py`
- 数据源：硬编码
- Caption 数字："ρ drops from 0.955 to 0.001 (trained) and from 0.933 to 0.000 (reference)"
- 数据匹配：✅
- 详情：real_rho = [0.955, 0.933], shuf_rho = [0.0012, 0.0003] → 0.001 和 0.000（四舍五入）✓

### Figure (fig_nlp_control_r2): NLP Control Overlay (Appendix)
- 脚本：`scripts/plot_nlp_control_overlay.py`
- 数据源：硬编码（与 fig_r2_collapse 完全相同的数据数组）
- 数据匹配：✅
- 详情：数据与 fig_r2_collapse 完全一致（共用同一组数值）。NLP_VAL = 0.155。

### Figure (fig_claim_evidence): Claim-Evidence Summary (Appendix)
- 脚本：`scripts/plot_claim_evidence.py`
- 数据源：概念图
- 数据匹配：✅ (N/A)
- 详情：结构化摘要图，文本内容与论文 findings 一致。"6/6 VLM→VLA conditions show Δ > 0.10; 0/4 VLA→VLA; 0/10 reference conditions" 与 Table 1 一致。"Cohen's d ≥ 0.45" 与 counterfactual 数据最小值 OV-L P=0.45 一致。

### 附录 Figures（无本地脚本，仅验证 caption 数字）

以下 figures 在附录中引用，但无本地 plot 脚本。通过 caption 中的数字与正文/表格交叉验证：

| Figure | File | Caption 关键数字 | 验证 |
|--------|------|----------------|------|
| fig_metric_comparison | fig6.pdf | RSA: DINOv2 0.692, Fused 0.634, Proj 0.615; CKA: Ref 0.089, Trained 0.083 | ✅ 与附录文本一致 |
| fig_rsa_bar | fig2.pdf | DINOv2 cls ρ=0.692, CLIP 0.557 | ✅ 与附录文本一致 |
| fig_cross_benchmark | fig7.pdf | Spatial RSA L14 ρ=0.691, Δ=+0.023 | ✅ 与附录文本一致 |
| fig_ood_diagnostics | fig_ood_diagnostics.pdf | 无具体数字 in caption | ✅ N/A |
| fig_linear_vs_mlp | fig_linear_vs_mlp_probe.pdf | 无具体数字 in caption | ✅ N/A |
| fig_probe_bars | fig4.pdf | R²=0.678 L13, 0.655 L8, 0.630 proj | ✅ 与 tab:training_effect_summary 一致 |
| fig_factorial | fig5.pdf | RSA peak shift L0(0.612)→L12(0.628), Δ=+0.017; |Δ|<0.006 | ✅ 与附录表格一致 |
| fig_random_subset_ablation | fig_specificity_bootstrap_30seeds.pdf | dominant +0.030, random +0.071±0.013, z=-3.11 | ✅ 与附录文本一致 |
| fig_probe_conditions | fig_probe_conditions.pdf | 99.6% at L1, 100% saturation, 82% L31 decay | ✅ 与 tab:dense_routing 一致 |

---

## 问题清单

### ⚠️ P1: plot_multi_layer_attention.py L31 trained = 19, 论文 = 18
- **位置**：Figure 7 左 panel（fig_multi_layer_attn.pdf），L31 数据点
- **脚本值**：`trained_heads = [24, 4, 10, 19]` → L31 = 19
- **论文值**：
  - experiments.tex line 131: "L1: 24, L31: 18"
  - appendix Table 10 (tab:multilayer_attention): L31 Trained = 18/32
  - plot_teaser.py: vla_trained[31] = 18（同一个数据的另一来源）
- **影响**：Figure 7 左 panel 中 L31 的 VLA-trained 数据点偏高 1 head（19 vs 18）
- **根因推测**：脚本硬编码时可能使用了不同 threshold 或不同 batch 的提取结果；teaser 和 appendix table 使用了更新后的数据
- **严重程度**：低（1/32 head 差异，不影响定性结论）

### ⚠️ P2: Appendix 段落文本与 fig_l1_attention 脚本数据不一致
- **位置**：appendix.tex line 725 附近段落
- **文本值**："TraceVLA: 27/32 vs. 32/32" 和 "NORA: 13/16 vs. 13/16"
- **脚本值**：TraceVLA trained = 29/32, NORA ref = 14/16
- **影响**：appendix 正文中引用的具体值与图表实际绘制的值不一致（尽管 experiments.tex 使用了覆盖这些值的范围表述 "27–30/32" 和 "13–14/16"）
- **严重程度**：低（在论文认可的范围内，但段落中的 point estimate 与图不匹配）

### ℹ️ INFO: NLP control R² = 0.155 统一值
- **位置**：fig_r2_collapse (Figure 6) 和 fig_nlp_control_r2，NLP_VAL = 0.155
- **说明**：三个不同的 NLP 模型（Llama-2-chat, Phi-3-instruct, Qwen2.5-Instruct）共用同一个 R² = 0.155 水平线。如果这是三个模型的平均值或代表值，属于合理简化。但如果三个模型各有不同的 R² 值，则图表丢失了差异信息。
- **论文 claim**：ΔR² = 0.000（flat profile），不依赖 R² 的绝对值
- **严重程度**：信息性，不影响结论

### ✅ RESOLVED: TraceVLA Spatial/Object wrong↔shuffled 交换
- **原始关注**：Figure 5 中 TraceVLA Spatial 和 Object 的 wrong 与 shuffled 值可能交换
- **验证结果**：通过 `cf_batch_missing_v1_analysis.md` 和 `cf_batch_part2_v1_analysis.md` 分析报告交叉验证，trained ordering 与脚本中的条件映射完全一致
- **结论**：条件映射正确，wrong 和 shuffled 未交换

### ✅ RESOLVED: OpenVLA L1 heads 24 vs 23
- **说明**：main text 使用 dedicated L1 analysis 的 24/32，bar chart 使用 32-layer bulk extraction 的 23/32。差异来自不同提取方法（threshold boundary effects），appendix 已明确注释。
- **结论**：已知方法差异，不是数据错误
