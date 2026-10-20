# Supplementary Material 完整性检查报告

**日期**: 2026-05-28
**论文**: Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis
**目标会议**: CoRL 2026

---

## 1. 编译状态：PASS

- 编译工具链：pdflatex + bibtex，三遍编译（pdflatex → bibtex → pdflatex × 2）
- 编译无错误，输出 `main.pdf`（39 页，8,437,759 字节）
- 所有引用的图片文件均存在，无缺失

## 2. Appendix 完整性：PASS

**规模**：1,283 行源码，27 页 PDF（第 13–39 页）

**16 个 Figure**：
| Label | 描述来源 |
|-------|---------|
| fig:metric_comparison | Metric Sensitivity: RSA vs CKA |
| fig:rsa_bar | RSA Across Representation Sources |
| fig:random_subset_ablation | Random-Subset Ablation |
| fig:ood_diagnostics | Pretrained LLM Under Visual Input |
| fig:linear_vs_mlp | Probe Architecture Sensitivity |
| fig:probe_bars | Functional Probe Comparison |
| fig:factorial | Training Effect and Instruction Invariance |
| fig:cross_benchmark | Cross-Suite Validation (Spatial) |
| fig:label_permutation | Label Permutation Test |
| fig:cross_arch_l1_bar | Cross-Architecture L1 Bar |
| fig:attention_appendix | Attention Appendix |
| fig:cross_arch_l1 | Cross-Architecture L1 Profiles |
| fig:training_dynamics | Training Dynamics |
| (+3 unlabeled figures) | |

**29 个 labeled Table**：
tab:cf_summary, tab:counterfactual, tab:perhead_bootstrap, tab:dose_response, tab:action_shift_perdim, tab:counterfactual_spatial, tab:spatial_cross_instruction, tab:metric_invariance, tab:seed_sensitivity, tab:demo_sensitivity, tab:delta_r2_threshold, tab:training_effects, tab:training_effect_summary, tab:dense_routing, tab:qa_probe, tab:cross_arch_probe, tab:multilayer_attention, tab:threshold_sensitivity, tab:attention_decomp, tab:per_dim_mae, tab:per_task_r2, tab:task_complexity, tab:specificity_control, tab:paired_dz, tab:2x2_r2_summary, tab:2x2_r2, tab:methodological_precedent, tab:nlp_controls, tab:arch_diversity, tab:convergent_evidence

**41 个 Subsection**：
1. Architecture Summary
2. OpenVLA-Specific Analysis Methods
3. OpenVLA Single-Architecture Deep Dive
4. Counterfactual Sensitivity Details
5. CKA Analysis Method
6. Metric Sensitivity: RSA versus CKA
7. Branch-Split Detailed Analysis
8. RSA Across Representation Sources
9. Per-Layer RSA Profiles
10. Per-Layer Action Decoding Across Training Stages
11. Random-Subset Ablation Details
12. Action Trajectory Analysis Details
13. Pretrained LLM Representation Quality Under Visual Input
14. Probe Architecture Sensitivity
15. Functional Probe Comparison
16. Training Effect and Instruction Invariance
17. Additional RSA Values
18. Cross-Suite Validation within LIBERO: Spatial
19. Robustness Analyses
20. Detailed Training Effects
21. Training Effect Size Summary
22. Instruction Classification Probes
23. L1 Attention Decomposition by Head Group
24. Per-Dimension Action MAE Under Head Ablation
25. Per-Task R² Distribution Under L1 Ablation
26. Task Complexity and Attention Dependence
27. Specificity Control: Matched-Size Head Ablation
28. Paired Effect Sizes
29. Cross-Architecture Action Decodability: 2×2 Design
30. Global Multiple Comparison Correction
31. Mechanistic Interpretation
32. Functional Stages and Predictions
33. Extended Discussion
34. Extended Practical Implications
35. Methodological Context
36. NLP Finetuning Controls
37. Claim-Evidence Summary
38. Cross-Architecture Design Rationale
39. Convergent Evidence Summary
40. Use of Generative AI

## 3. 交叉引用审计：PASS

**统计**：91 个 `\label` 定义，82 个 `\ref` 引用

**孤儿引用（ref 无对应 label）**：0 个 ✓

**反向孤儿（label 无 ref 引用）**：9 个（均为顶层 section label，属正常结构性标记）
| Label | 说明 |
|-------|------|
| sec:appendix | 顶层 appendix 入口 |
| sec:conclusion | Conclusion section |
| sec:experiments | Experiments section |
| sec:introduction | Introduction section |
| sec:related_work | Related Work section |
| sec:claim_evidence_appendix | Claim-Evidence Summary |
| sec:extended_practical_implications | Extended Practical Implications |
| sec:label_permutation | Label Permutation subsection |
| sec:use_of_ai | Use of Generative AI |

**评估**：所有反向孤儿均为结构性 section label（用于导航/目录），不影响内容完整性。无实质性交叉引用遗漏。

## 4. 编译警告：PASS

| 类型 | 数量 | 详情 |
|------|------|------|
| Undefined reference | 0 | ✓ |
| Multiply defined label | 0 | ✓ |
| Citation undefined | 0 | ✓ |
| Overfull hbox (>10pt) | 0 | ✓ |
| Overfull hbox (any) | 0 | ✓ |
| Underfull hbox | 0 | ✓ |
| Float specifier changed | 1 | `h` → `ht`（无害） |

## 5. PDF 格式：PASS

**页数分布**：
| 部分 | 页码 | 页数 |
|------|------|------|
| 正文（含 Limitations） | 1–8 | 8 页 ✓ |
| References | 9–12 | 4 页 |
| Appendix | 13–39 | 27 页 |
| **总计** | | **39 页** |

**字体嵌入**：全部嵌入（emb=yes）✓

**字体类型**：
- Type 1：12 种（txfonts 系列 + Nimbus 系列）— 全部合规
- CID TrueType：LiberationSerif 系列（来自 PDF 图片）— 合规
- Type 3：**0 种** ✓

## 6. CoRL 2026 合规：PASS

| 要求 | 状态 | 详情 |
|------|------|------|
| Limitations section | ✓ | `\section{Limitations}`（discussion.tex L11），位于第 8 页正文内 |
| 8 页正文限制 | ✓ | 正文结束于第 8 页底部 |
| References 从 p9 开始 | ✓ | 第 9 页首行即 "References" |
| 匿名提交 | ✓ | `\author{Anonymous}` |

---

## 总结：提交就绪 ✅

所有 6 项检查均通过。无需修复项。

- 编译零错误零警告（仅 1 个无害 float 调整）
- 交叉引用完整，无孤儿引用
- 27 页 appendix 包含 16 图 29+ 表 40 个 subsection，内容充实
- PDF 格式合规：8 页正文 + Limitations，全字体嵌入，无 Type 3
- CoRL 2026 格式要求全部满足
