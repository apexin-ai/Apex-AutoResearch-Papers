---
round: 10
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T09:14:20.278890+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 13 (Fresh Review)

**论文**: "Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts"
**Venue**: EMNLP 2026 (ARR May cycle)
**审稿模式**: Fresh（初审，2 Reviewers × 1 轮 + 交叉分享）

---

## Summary

本文研究 LLM 标注作为 effect modifier 用于异质性处理效应（HTE）分析时，subgroup-heterogeneous misclassification 对 CATE 估计引入的 bias。核心贡献：(1) Bias Decomposition Identity（Theorem 1）——精确恒等式将 correction-induced bias 分解为 δ_s · Δτ / (1−2π̄) 的乘积形式；(2) EC-HTE——基于 hierarchical Bayesian subgroup-stratified confusion matrix 的纠偏框架；(3) Δτ-free diagnostic（Proposition 3）——仅需 per-subgroup error rates 即可判断 global correction 是否有害；(4) EC-HTE+PPCI 组合处理 covariate+outcome 双重误差。实验覆盖 520 synthetic configurations、semi-synthetic TweetEval、Hate Speech real-data case study、8 LLMs（6 proprietary + 4 open-source）。

---

## Strengths

**S1. 问题识别的实际价值与非直觉性。** 论文揭示了一个重要的失败模式：当 LLM 误分类率跨 subgroup 异质时，标准 global confusion-matrix correction 在 50% 的 K=2 配置中恶化 CATE 估计（Section 5.2）。"debiasing can be worse than doing nothing" 的发现对 CSS 实践者有直接警示意义。[两位 Reviewer 一致认可]

**S2. Theorem 1 的理论贡献干净且有独立价值。** bias = δ_s · Δτ · amplification factor 的乘积分解结构直观地揭示了 misclassification heterogeneity 与 treatment effect heterogeneity 的交互作用。证明（Appendix B）完整可验证，R² > 0.994 (K=2) 和 R² > 0.974 (K=4) 的经验验证覆盖 520 synthetic configurations + 11 real LLM confusion matrices。[两位 Reviewer 一致认可，Soundness 评 4/5]

**S3. 实验设计系统全面。** 520 configurations 参数网格、100 MC runs + MC SE 报告、semi-synthetic TweetEval（真实文本特征 + 合成 CATE）、multi-LLM 一致性验证（Spearman ρ ≥ 0.82）、21 个 Appendix 覆盖主要 assumption violation 场景。实验规模在同类论文中属上乘。[两位 Reviewer 一致认可]

**S4. Diagnostic 工具的实用性。** Proposition 3 的 Δτ-free diagnostic 打破了 "要诊断需要先知道答案" 的循环依赖，AUC = 0.86 at subgroup level。独立于 EC-HTE 可使用，为实践者提供低成本 screening tool。[两位 Reviewer 一致认可]

**S5. 完整的实践指南。** Algorithm 1 伪代码可直接实现，expert budget crossover curves（Appendix I-J）、diagnostic threshold guidance（Section 5.4）构成完整 workflow。[两位 Reviewer 一致认可]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W-MF1. [CONSENSUS] Plug-in SE 与方法优势的 regime 矛盾**
- **来源**: R1-N1（critical），R2 交叉完全 [AGREE]
- **问题**: EC-HTE 的 HB shrinkage 在低 expert budget（n_expert < 100）时提供最大的点估计优势（Table 3, K=2 n=25: HB RMSE 0.256 vs MLE 0.269），但恰好在这个 regime 下 plug-in SE（Eq. 5）不传播 confusion matrix estimation uncertainty，CI coverage 不可靠。Appendix Y 的 bootstrap 修复仅验证 n_expert=200（coverage 93.8%→95.0%），**未覆盖 n_expert < 100 的关键区间**。方法的核心卖点与其已知缺陷在同一参数区间内存在结构性矛盾。
- **影响**: 实践者在最需要 EC-HTE 的场景下无法信赖其置信区间。
- **修改方向**: (a) 提供 n_expert ∈ {25, 50, 75} 下 bootstrap coverage（含 per-subgroup breakdown）；(b) 正文 Section 4.3 明确标注 plug-in SE valid regime；(c) 如 bootstrap 在小 n 下也不恢复 nominal coverage，诚实讨论。

### Should-Fix（影响评分但不一票否决）

**W-SF1. [DIVERGENT → Director 裁定 should-fix] 与经典测量误差文献的区分不够锐利**
- **来源**: R2-N1（critical），R1 [REBUT] 降级
- **分歧**: R2 认为 "misspecified correction amplifies MSE" 在 Carroll et al. (2006)/Fuller (1987) 中已有论述，要求数学语言论证区分。R1 反驳：Theorem 1 的 δ_s·Δτ 乘积分解在 Carroll 框架无对应物——前者处理 mismeasured regressor 的 scalar attenuation，后者处理 effect modifier misclassification 下 global vs subgroup correction 的 mismatch，结构不可互推。
- **Director 裁定**: R1 论证有说服力，贡献不被 Carroll 涵盖。但论文表述可更锐利——应在 Section 3 增加 Remark 用数学符号对比 F-L attenuation formula 与 Theorem 1 的 structured decomposition。降为 should-fix。

**W-SF2. [DIVERGENT → Director 裁定 should-fix] HB partial pooling 方法新颖性有限**
- **来源**: R2-N2（critical），R1 [REBUT] 降级
- **分歧**: R2 认为 Dirichlet-Multinomial HB 是 James-Stein shrinkage 的直接应用，方法新颖性不足。R1 反驳：应评价框架整体（Theorem 1 → HB → variance-adjusted CF → diagnostic → PPCI 组合），不应剥离 HB 单独评价。
- **Director 裁定**: HB 组件确实不新颖（论文自承），但框架设计有工程价值。论文应更坦诚地定位贡献——主要在 problem identification + bias identity，EC-HTE 是 "the right tool for the right problem" 而非方法创新。降为 should-fix。

**W-SF3. [DIVERGENT → Director 裁定 should-fix] 缺乏真实数据 CATE 基准验证**
- **来源**: R1-N2（critical），R2 [AGREE 但建议降级]
- **分歧**: R1 认为所有定量评估依赖 synthetic/semi-synthetic DGP 是 must-fix。R2 同意问题存在但认为是因果推断方法论文的固有局限——CausalForest、PPI 原始论文同样如此。
- **Director 裁定**: 结构性限制，非本文特有。验证层次（520 synthetic → semi-synthetic → 11 real CMs R²=0.975 → Hate Speech patterns）在方法论文中已属充分。降为 should-fix，建议在 Hate Speech case study 中用 held-out expert labels 构建 pseudo ground-truth CATE 进行方向性比较。

**W-SF4. [CONSENSUS] Subgroup 选择指导缺失**
- **来源**: R1-W2 + R2-W4，交叉完全 [AGREE]
- **问题**: EC-HTE 要求预定义 subgroup mapping S: X → {1,...,K}，但未提供 subgroup misspecification 后果分析或 data-driven discovery 指导。与 CausalForest 自动发现异质性相比是显著实用性差距。Appendix P 的随机 subgroup 实验是极端情况，缺乏 "partially correct subgroup" 测试。
- **修改方向**: Limitations 补充 subgroup selection guidance；讨论 Proposition 3 diagnostic 反向用于 subgroup selection 的可能性。

**W-SF5. [CONSENSUS] Abstract 信息密度过高**
- **来源**: R2-W2，R1 交叉 [AGREE]
- **问题**: ~250 词内塞入 10+ 个具体数字，核心 message 被稀释。
- **修改方向**: 精简到 3-4 个关键数字（R² > 0.97、50% configurations worsened、AUC 0.86、7.4× bias reduction），其余移至 Introduction。

**W-SF6. [CONSENSUS] "Exact identity" 强调过度**
- **来源**: R2-W3，R1 交叉 [AGREE]
- **问题**: 论文多处强调 "exact identity, not a bound"，但 Frazis & Loewenstein (2003) 的 scalar attenuation 同样是 exact。真正新颖性在于 δ_s × Δτ 的结构化分解。
- **修改方向**: 将措辞重心从 "exact identity (not a bound)" 转移到 "structured bias decomposition identity"。

**W-SF7. [CONSENSUS] 遗漏若干相关文献**
- **来源**: R2-W1，R1 交叉 [AGREE]
- **遗漏**: Mellon et al. (2025) LLM annotation variance sources；Bauer et al. (2024) LLM annotation ME reduction；Calvi et al. (2015) HTE with mismeasured treatment。

---

## Reviewer Consensus

以下问题两位 Reviewer **达成共识** [AGREE]：
1. Plug-in SE regime 矛盾是最实质性的技术缺陷 [Must-Fix]
2. 问题识别的实际价值和 Theorem 1 的理论贡献是论文最大的强项
3. 实验覆盖面令人印象深刻
4. Subgroup 选择指导缺失需要补充
5. Abstract 应精简数字密度
6. "Exact identity" 措辞应调整为 "structured decomposition"
7. A3 balanced classes 是 expositional convenience 非 structural limitation（R2 rebut R1-W1，R1 接受）
8. κ > 100 singularity guard 是 safety net 非 tuning parameter（R2 rebut R1-W4，R1 接受）
9. PPCI 组合的 Table 8 factorial design 提供了充分经验证据（R2 rebut R1-W3，部分接受）

## Reviewer Divergence

以下问题存在分歧，**Director 已裁定**：
1. **Carroll et al. 区分**：R2 标 critical → R1 rebut（乘积分解结构性不同）→ Director 裁定 should-fix（presentation fix）
2. **HB 方法新颖性**：R2 标 critical → R1 rebut（框架 vs 组件）→ Director 裁定 should-fix（重新定位贡献）
3. **Real data validation**：R1 标 critical → R2 同意但降级 → Director 裁定 should-fix（结构性限制）

---

## Questions（需作者回应）

**Q1.** [R1] Plug-in SE 在 n_expert ∈ {25, 50, 75} 下的 bootstrap coverage 是多少（含 per-subgroup breakdown）？

**Q2.** [R2] Theorem 1 的 bias identity 能否从 Carroll et al. (2006) 的 functional measurement error framework 中作为 special case 推导？如果不能，请用数学语言说明。

**Q3.** [R1+R2] 如果实践者不确定 subgroup 定义是否正确，Proposition 3 的 diagnostic 能否反向用于 subgroup selection？

**Q4.** [R2] Diagnostic 的 precision-recall 分析（false negative vs false positive 代价不对称）？

**Q5.** [R2] A1 violation strength γ ∈ [0, 0.2] 是否覆盖了实际 LLM 标注的 outcome-dependence 幅度？有无 empirical calibration？

**Q6.** [R1] Corollary 5 下，若 Δτ_s 与 δ_s 正相关（treatment effect heterogeneity 与 misclassification heterogeneity 沿同一维度），amplification 效应会更严重还是更轻？

---

## Missing References

- Mellon et al. (2025). "Variance-Aware LLM Annotation for Strategy Research." arXiv:2601.02370.
- Bauer et al. (2024). "To Err Is Human; To Annotate, SILICON?" arXiv:2412.14461.
- Calvi et al. (2015). "Heterogeneous Treatment Effects with Mismeasured Endogenous Treatment." arXiv:1511.04162.

---

## External Review

**外部审稿**: 未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（4 warnings, 0 critical, 12 info）。主要发现：

1. **[warning] Pages 3-6 连续 4 页无 figure/table**。Related Work（p3）和 Method 4.1-4.3（p6）完全缺乏 display item，审稿人可能在此段感到节奏单调。
2. **[warning] 主文仅 3 个 display items**（Figure 1 p2, Table 1 p7, Figure 2 p8），密度 0.33/页偏低。大量关键实验结果全在 Appendix，审稿人可能不会翻阅。
3. **[warning] Page 8 极度拥挤**：Figure 2 + Section 5.4 + Conclusion + Limitations 起始全挤在一页，Conclusion 被压缩。
4. **[warning] Page 9 Limitations 延伸**：整页纯文本，无 display item。需确认 Limitations 完整归入豁免页。

格式合规确认：正文 ≤ 8 页 ✓，`[review]` 选项 ✓，匿名性 ✓，Limitations section 存在 ✓，参考文献格式 ✓。

---

## Overall Assessment

**评分**: 3.5 / 5（Borderline Conference）

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 4/5 | 4/5 | **4/5** |
| Excitement | 3.5/5 | 3/5 | **3/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Overall | 3.5 | 3.5 | **3.5** |
| Confidence | 4/5 | 4/5 | **4/5** |

**综合判断**: 论文识别了一个重要且非直觉的问题，提供了严谨的理论刻画（exact bias identity, R² > 0.97）和全面的实验验证（520 configurations, 8 LLMs, 11 model-dataset combos）。主要限制因素：(1) plug-in SE 与方法优势的 regime 矛盾是唯一的共识 must-fix——如果 rebuttal 能提供小 n 下的 bootstrap coverage 数据，可消除此顾虑；(2) 方法贡献（HB partial pooling）是标准工具的直接应用，创新性有限但工程价值明确；(3) 缺乏真实 CATE ground truth 验证是结构性限制，非本文特有。

**推荐**: Strong Findings candidate。如果 rebuttal 有力回应 W-MF1（提供小 n bootstrap coverage）并调整贡献定位（W-SF1/SF2），可上调至 4（Conference）。

**EMNLP 2026 ARR 评分对照**: 3.5 = Borderline Conference。

---

## Detailed Comments

### Section 1 (Introduction)
- 叙事逻辑清晰：Problem → Gap → Solution → Results。"a researcher who corrects for annotation noise using a pooled confusion matrix may introduce more bias than doing nothing" 准确有力。
- 贡献列表 3 项（identity, EC-HTE, diagnostic）层次分明。
- Footnote 1 澄清 "debiasing" 含义（annotation measurement-error bias, not algorithmic fairness）是好的，但可增加对 DML "debiased" 的区分。

### Section 2 (Related Work)
- 三层区分（measurement error, annotation models, HTE+LLM）结构合理。
- 与 Frazis & Loewenstein (2003) 的区分需加强数学层面的论证。
- 遗漏 Mellon et al. (2025)、Bauer et al. (2024)、Calvi et al. (2015)。

### Section 3 (Bias Decomposition)
- Theorem 1 证明完整（Appendix B 可验证），R² 验证有力。
- 5 个假设（A1-A5）逐条列出，sensitivity 分析覆盖各假设违反。
- Remark 2 声称 "does not require (A2)" 与 Theorem 1 假设列表的表面矛盾需澄清。
- Proposition 3 的 diagnostic 有独立实用价值，AUC = 0.86（synthetic symmetric），但真实 LLM CM 上 AUC 降至 0.63——需在正文讨论。

### Section 4 (EC-HTE)
- HB estimation (Section 4.1) 描述完整，α₀ 的 empirical Bayes 估计合理。
- Singularity guard κ > 100 是合理的 safety net（Appendix A 验证阈值不敏感）。
- **Plug-in SE (Section 4.3, Eq. 5) 是主要弱点**：不传播 CM estimation uncertainty，n_expert < 100 时 coverage 缺口需量化。
- PPCI 组合描述清晰，Table 8 的 4-DGP factorial design 提供充分经验证据。

### Section 5 (Experiments)
- 520 configurations + 100 MC runs 设计系统，MC SE < 3.2%。
- Table 1 仅展示 extreme heterogeneity 有利结果——caption 已注明 moderate/TweetEval 在 Table 7，但审稿人可能不翻 Appendix。
- Semi-synthetic TweetEval 中 EC-HTE 未显著优于 Global（p=0.395）——论文在正文诚实报告，是加分项。
- Section 5.4 的 diagnostic workflow 有独立实用价值。

### Section 6 (Conclusion)
- 过于压缩（视觉审查确认 page 8 拥挤）。

### Limitations
- 覆盖 5 个要点，整体诚实。
- 未提及：continuous effect modifiers、Corollary 4 多分类扩展无实验验证。
