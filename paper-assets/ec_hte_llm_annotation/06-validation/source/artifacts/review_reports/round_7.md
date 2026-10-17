---
round: 7
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T13:51:12.280151+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 10 (Fresh)

**论文**: Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts
**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)
**审稿人**: Reviewer 1 (方法严谨性) + Reviewer 2 (新颖性/完整性)

---

## Summary

本文证明当 LLM 标注的分类错误率在子群间存在异质性时，使用全局（pooled）混淆矩阵纠正标注错误会在 HTE 分析中引入子群级偏差，偏差大小为精确乘积形式 δ_s·Δτ/(1−2π̄)（Theorem 1）。在此基础上提出 EC-HTE 方法（HB Dirichlet-Multinomial 子群分层混淆矩阵估计 + CausalForestDML），并给出 Δτ-free 先验诊断条件（Proposition 3, AUC=0.86）。实验覆盖 520 个合成配置（100 MC runs）、半合成 TweetEval、真实 Hate Speech，以及 7 个 LLM（4 开源 + 3 闭源）× 2 数据集的多模型验证。

---

## Strengths

1. **精确的偏差恒等式（Theorem 1）**：δ_s·Δτ/(1−2π̄) 是 exact population-level identity（非上界），代数推导经 R1 逐步手工验证确认无误。乘积结构的分解极具解释力——偏差仅在子群误差异质性与处理效应异质性同时存在时出现。在 measurement error 文献中，exact identity（而非 bound）较为罕见。[R1-S1, R2-S1, AGREE]

2. **Δτ-free 诊断准则（Proposition 3）**：|δ_s|/((1−2π̄)·π_s) > 1 的条件仅依赖可从 pilot sample 估计的分类错误率，打破了"需要先估计 CATE 才能判断是否该校正"的循环依赖。AUC=0.86（子群级别）、0.89（setting 级别）。[R1-S2, R2-S4, AGREE]

3. **实验设计全面且诚实报告负面结果**：520 合成配置 × 100 MC runs 覆盖关键参数空间。半合成 TweetEval 中 EC-HTE 劣于 Global 的结果（RMSE 0.225 vs. 0.124, 1.8×）在 Section 5.3 被详细分析而非隐藏。Hate Speech 边界条件（FNR=53.3%）坦诚报告。[R1-S3, R2-S2, AGREE]

4. **Remark 2 优雅泛化**：利用 B_s·1=0（源于 M_s 和 M_global 的行随机性），证明 bias(z,s) = Δτ·[B_s]_{z,1} 在非对称混淆矩阵下精确成立，核心乘积结构不依赖对称假设 (A2)。[R1-S4, R2-S6, AGREE]

5. **可复现性良好**：Algorithm 1 完整清晰；MCMC 诊断充分（R̂ < 1.0034, ESS > 1618, 0 divergent transitions）；CausalForestDML 超参数固定且明确记录；代码/数据声明于 Limitations 末尾。[R1-S5, R2-S3, AGREE]

6. **PPCI 互补性验证**：4-DGP 正交设计验证 EC-HTE 和 PPCI 的互补性（DGP C: bias 0.179→0.007）。[R2-S5, AGREE]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [CRITICAL] 假设 (A1) 条件独立性不可检验且无敏感性分析。** [R1-N1 + R2-W5 → 共识 CRITICAL]
- (A1) 要求 misclassification 独立于潜在结果 Y(0),Y(1)（给定 Z,S）。这是 Theorem 1 推导的基石——若违反，τ_obs(z,s) ≠ Σ M_s[z,z']·τ(z')，整个框架失效。
- 在 NLP 场景中违反是 plausible 的：LLM 对极端情感的分类准确率更高，而这些观测的处理效应也更大。
- 论文未提供任何针对 (A1) 违反的敏感性分析、部分识别结果、或实际场景讨论。
- **建议**：(a) 引入 sensitivity parameter 量化 Corr(misclassification, Y(1)−Y(0))，推导偏差退化公式；(b) 讨论 (A1) 最可能/最不可能成立的实际场景；(c) 引用 Dorn, Guo, Kallus (2022) 或 Lash, Fox, Fink (2009) 的 sensitivity analysis 框架。

**N2 [MAJOR] 半合成 TweetEval 结果为负面，但 Abstract/Intro 叙事倾向于合成极端配置的正面数字。** [R1-N2 + R2-W2 → 共识 MAJOR]
- 半合成实验（最接近真实场景的设置）中，Global 在 |bias|（0.023 vs. 0.027）和 RMSE（0.124 vs. 0.225）上均优于 EC-HTE。RMSE 相差 1.8 倍。
- Abstract/Introduction 的 headline 数字（"bias from 0.059 to 0.010"）仅来自合成极端配置。Abstract L8-9 有 TweetEval RMSE 对比，但权重远低于正面数字。
- **建议**：Abstract/Intro 中正面和负面结果应获得对等 prominence。可考虑将 EC-HTE 定位为 "never worse than naive + 在 extreme heterogeneity 下大幅改善" 的保险策略。

### Should-Fix（影响评分但不一票否决）

**N3 [MAJOR] CausalForest 覆盖率缺口归因不充分。** [R1-N3 + R2 AGREE]
- CausalForest plug-in SE 在 K=2 极端配置下仅达 83-85% 覆盖率（vs. 名义 95%）。论文归因于 "CausalForest's inherent SE calibration"，证据是 "CM-only bootstrap contributes <2% of total variance"。
- 但 2% 方差贡献 ≠ 0% 覆盖率影响；且 Global+CF=0.58 vs EC-HTE+CF=0.83-0.91 说明 CM 校正质量影响覆盖率特征。
- **建议**：提供 oracle 实验（使用真实 C_s 进行校正），隔离 CM 估计误差对覆盖率的贡献。

**N4 [MAJOR→SHOULD-FIX] 非对称诊断准则缺失。** [R1-N4, R2 降为 should-fix]
- Proposition 3 在非对称下 AUC 降至 0.82，且论文将 "fully general asymmetric diagnostic" 留给 future work。
- 真实 LLM CM 高度非对称（GPT-4.1 某子群 FPR=0.054, FNR=0.526）。
- R2 指出 Theorem 1 和 EC-HTE 方法本身不依赖 (A2)，仅诊断工具受影响。共识降为 should-fix。
- **建议**：至少提供基于 ||B_s||_∞ > max(FPR_s, FNR_s)（Appendix D, eq.20）的实用非对称诊断并报告 AUC。

**N5 [MAJOR] EC-HTE 方法论新颖性有限，存在定位张力。** [R2-W1 + R1 AGREE]
- 三个组件（HB Dirichlet-Multinomial、confusion matrix inversion、CausalForestDML）均为已有技术的组合。论文标题和结构暗示方法论文，但核心贡献是 Theorem 1（bias identity）+ Proposition 3（diagnostic）。
- R1 补充：HB 在 HTE 语境下的特定组合方式有工程新颖性，但不构成独立方法论贡献。
- **建议**：重新定位为 "problem identification paper with a principled fix"。C2 贡献声明弱化为 "the natural correction prescribed by the bias structure"。

**N6 [MAJOR] 与 Frazis-Loewenstein (2003) 的公式级区分缺失。** [R2-W3, R1 partial REBUT]
- Section 2 列出三个散文级区分点，但未在公式层面对比。
- R1 rebut：区别比 R2 暗示的更本质——F-L 分析 naive estimator 的衰减（OLS projection algebra），Theorem 1 分析 correction procedure 的残差偏差（mixing matrix algebra），不可通过变量替换互推。但 R1 也同意论文应加公式级对比。
- **共识方向**：应在 Section 2 或 3 加 1-2 段公式级对比，明确 F-L 公式中不存在 δ_s 项（子群偏差维度）。
- **分歧记录**：R1 认为区别是 fundamental（不同数学结构），R2 认为可能是 specialization。

### Minor

- **W1**：仅测试 K=2 和 K=4，K>4 时 HB shrinkage 可能退化为全局校正（"shrinkage 悖论"）。[R1-W1 + R2-Q4, AGREE]
- **W2**：DGP 较简单（Y = τ(Z)·T + ε），无混杂变量。[R1-W2]
- **W3**：R² 验证高 R²=0.994 无法区分 exact identity 与 high-precision approximation；应报告 R² vs MC 次数趋势。[R1-W3]
- **W4**："Debiasing" 术语在 NLP 社区可能引起歧义（fairness vs. measurement error）。脚注 1 已澄清但标题仍可能误导。[R2-W4 + R1 AGREE]
- **W5**：Limitations 未覆盖 (A1) 违反场景、K 选择 tradeoff、expert labels selection bias。[R2-W5 + R1 AGREE]
- **W6**：Table 1 DIM K=2 extreme 行中 Naive |bias|=0.058 vs Global |bias|=0.059——global 校正后偏差反增，是 Theorem 1 核心预测的直接验证，应在正文显著强调。[R2-W6 + R1 AGREE]

---

## Reviewer Consensus [AGREE]

1. **(A1) 敏感性分析缺失是最关键问题**：两位 Reviewer 均标为 critical。(A1) 是整个框架的基石，缺乏 sensitivity analysis 是论文最大的理论弱点。
2. **半合成叙事选择性**：两位 Reviewer 独立指出 Abstract/Intro 的 headline 数字偏向合成极端配置的正面结果，半合成 TweetEval 的负面结果权重不足。
3. **CausalForest 覆盖率归因需 oracle 实验**：两位 Reviewer 均同意当前归因（"inherent SE calibration"）不够充分。
4. **方法论定位调整**：两位 Reviewer 一致建议从 methods paper 转向 problem identification + principled fix。
5. **Theorem 1 的理论贡献被认可**：两位 Reviewer 均确认 exact bias identity 的新颖性和正确性。

---

## Reviewer Divergence [REBUT]

**与 Frazis-Loewenstein (2003) 的区分程度**：
- R1 认为区别是 fundamental（mixing matrix algebra vs. OLS projection，不可变量替换互推，δ_s 项在 F-L 中不存在）。
- R2 认为可能是 specialization（Theorem 1 或许可视为 F-L 在 CATE 场景的推广）。
- **两位 Reviewer 均同意**论文应在 Section 2/3 加公式级对比来明确区别。

---

## Questions（需要作者澄清）

1. Theorem 1 推导中 (A1) 何时最可能违反？给出具体 NLP 场景。[R1-Q1, R2-Q3]
2. Table 1 中 CausalForest EC-HTE coverage 0.91 vs. Appendix 中 83-85% 分别对应什么配置？提供 coverage vs. n_expert 曲线。[R1-Q2]
3. TweetEval S3 子群 RMSE 0.480 vs. 0.145（3.3×），能否通过更激进 shrinkage 或自适应 α_0 缓解？[R1-Q3]
4. 当 Δτ_s 与 δ_s 高度相关时偏差更严重，这在实践中多常见？[R1-Q4]
5. Gamma(3,1) 在 K=4 时 sensitivity 4-5%，是否探索过经验贝叶斯？[R1-Q5]
6. Multi-LLM 高 Spearman ρ 是否暗示跨 LLM 混淆矩阵可迁移？[R2-Q5 → R1 rebut：rank correlation ≠ absolute rate transferability，不可迁移]

---

## Missing References

1. **Dorn, Guo, and Kallus (2022)** — 处理效应中的误差灵敏度分析，与 (A1) sensitivity analysis 直接相关。[R2-MR1 + R1 AGREE]
2. **Lash, Fox, and Fink (2009)** — "Applying Quantitative Bias Analysis to Epidemiologic Data"，分类错误偏差量化框架，与 "when correction hurts" 角度直接相关。[R1-MR1]
3. **Nie and Wager (2021)** — R-learner，HTE 估计方法 landscape（Appendix S 已测试但 Section 2 引用不足）。[R2-MR3 + R1 AGREE]
4. **Text-as-data 因果推断文献（Spirling 等）** — 在 Section 2 应有更明确位置。[R2-MR4 + R1 AGREE]
5. **Audinet de Pieuchon et al. (2025)** — 已在主文引用，但可在 Section 2 Related Work 中更充分讨论。[R1-MR2 → R2 纠正：已在主文 Section 4.2 出现，非仅 Appendix]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

视觉审查已完成（4 warnings / 0 critical / 8 info）：

**Warnings**:
1. Pages 3-7 连续 5 页无 display item。Pages 3-5 有数学推导可部分豁免，但 pages 6-7（实验 setup + 结果）为纯文本，审稿人失去视觉锚点。建议将 Figure 2 或 Table 1 前移。
2. Page 8 极度拥挤：Figure 2 + Table 1 + Section 5.5 + Conclusion 开头挤在同一页。核心结果页面视觉过密。
3. 主文 8 页仅 3 个 display items（Figure 1, Figure 2, Table 1），对实证论文偏少（通常 5-8 个）。大量重要结果仅以文字描述。
4. Figure 5（Applicability Frontier）红绿配色对色盲不友好，建议改用蓝/橙或添加纹理。

**Info**（正面）：
- Figure 1 位置合理（page 2），Title-Abstract-Figure 1 叙事一致。
- Figure 2 heatmap 颜色区分度好，hatched region 清晰。
- Table 1 格式规范（booktabs, bold），Appendix 表格一致。
- Limitations 段落简洁覆盖三个要点，符合 EMNLP 规范。
- Appendix 充实（17 表 + 3 图），格式专业。

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**
**Confidence: 4/5**

本文提供了一个在 HTE 分析中全局分类错误校正引入子群偏差的精确恒等式（Theorem 1），理论新颖且推导正确（R1 逐步代数验证），实验全面（520+ 配置 × 100 MC runs）且诚实报告负面结果。Δτ-free 诊断准则（Proposition 3, AUC=0.86）具有独立实用价值。

阻碍更高评分的关键问题：(1) 核心假设 (A1) 缺乏敏感性分析，是唯一可能完全摧毁框架的假设；(2) 在最接近真实场景的半合成实验中 EC-HTE 劣于 Global（RMSE 1.8×），但 Abstract/Intro 叙事倾向正面数字；(3) CausalForest 覆盖率缺口归因需 oracle 实验支撑。

**若 rebuttal 能提供 (A1) sensitivity bounds 并在 Abstract/Conclusion 平衡正负结果权重，论文可提升至 Conference (4.0) 水平。** Theorem 1 的 exact identity 和 Proposition 3 的诊断准则本身已达 Findings 水准。

### ARR 维度打分

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 4/5 | 3.5/5 |
| Excitement | 3.5/5 | 3/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |

---

## Detailed Comments

### Abstract
- L2 的 δ_s·Δτ 精确符号使用正确。
- 正面数字（"bias 0.059→0.010"）占据突出位置，负面结果（TweetEval RMSE 0.124 vs. 0.225）虽在 L8-9 提及但权重不足。
- "50% of K=2 configurations (260/520) across our parameter grid" 的限定已到位。

### Section 1 (Introduction)
- Figure 1 位置合理，有效传达核心 bias 机制。
- "derive an exact bias identity" 措辞准确（vs. 先前 "discover"）。
- C2 "the natural correction prescribed by the bias structure" 定位合理但仍暗示方法论贡献。
- 脚注 1 区分 measurement-error debiasing 和 fairness debiasing，位置已从 Section 3 提前到 Section 1。

### Section 2 (Related Work)
- 三层技术区分（effect modifier vs. regressor、correction-induced bias vs. attenuation、δ_s·Δτ product structure）已到位。
- 与 Frazis-Loewenstein 的区分停留在散文层面，缺乏公式级对比（见 N6）。
- Audinet de Pieuchon et al. (2025) 已在主文 Related Work 中讨论。
- Nie and Wager (2021) R-learner 在 Appendix S 测试但 Section 2 引用不足。

### Section 3 (Theory)
- Theorem 1 推导正确（R1 验证）。Appendix B 的代数步骤完整。
- (A1)-(A5) 五个假设清晰列出，(A5) 有 Corollary 泛化。
- Remark 2 利用行随机性的 B_s·1=0 性质优雅泛化到非对称情形。
- **缺失**：(A1) 违反后的 bias 退化讨论（N1）；Proposition 3 非对称 AUC 降幅（N4）；与 F-L 的公式级对比（N6）。

### Section 4 (Method)
- HB 模型规格完整（Dirichlet-Multinomial + Gamma(3,1) hyperprior + Gibbs sampling）。
- 两层阈值（κ>100 singularity guard + κ≤1.25 empirical diagnostic）区分清晰。
- Algorithm 1 fallback 时 SE 使用 C̄^{-1} 已明确。
- PPCI 互补性清晰描述。

### Section 5 (Experiments)
- 5.2 (Bias Identity Verification): R²=0.994/0.974 验证充分。但 R² vs. MC runs 趋势未报告（W3）。
- 5.3 (EC-HTE Evaluation): 三因素分析（moderate Δπ, unbalanced subgroups, per-subgroup RMSE heterogeneity）到位。p=0.395 标注诚实。但 headline 数字选择有叙事偏向（N2）。Table 1 DIM K=2 行中 Naive |bias|=0.058 vs Global |bias|=0.059 是 Theorem 1 的直接验证，应更显著强调（W6）。
- 5.4 (Diagnostic): AUC=0.86 子群级别有实用价值。CV(π_s) vs. Proposition 3 trade-off 已讨论。
- 5.5 (Multi-LLM): 7 LLM × 2 datasets 验证 Δπ heterogeneity 的普遍性。R²=0.975 across 11 combinations。

### Limitations
- 覆盖 budget threshold、classifier quality、class balance、additive CATE。
- **缺失**：(A1) 违反场景、K 选择 tradeoff、expert labels selection bias（W5）。

### Appendix
- 内容充实（15+ sections, 17 tables, 3 figures）。
- MCMC 诊断（Appendix G）充分。
- Corollary 1 (Appendix C) 证明中 h(j,j') 未推导，g(π̄) 仅给特殊情形。
- Applicability Frontier (Figure 5) 信息价值高但主文无空间。

### 格式
- 正文 ≤ 8 页 ✅
- Anonymous ✅
- ACL template ✅
- 参考文献 34 条，格式规范 ✅