---
round: 2
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-21T15:03:29.560538+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts

**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计, R2 新颖性+完整性）
**轮次**: Round 1 初审 → 交叉分享 → 1 轮收敛

---

## Summary

本文证明当 LLM 标注误分类率在子群间存在异质性时，标准全局混淆矩阵修正引入与 Δπ × Δτ 成正比的偏差（Theorem 1，exact population-level identity，R²=0.994）。基于此提出 EC-HTE 框架：层级贝叶斯子群级混淆矩阵估计 + CausalForestDML + plug-in SE propagation。在 520 合成配置和半合成 TweetEval 实验中验证，并与 PPCI 组合处理双重误差。论文对失败案例（Appendix H hate speech null result, Appendix K semi-real CM 负面结果）进行了诚实报告。

---

## Strengths

**S1. Theorem 1 正确且优雅** [R1+R2 共识]
Bias decomposition identity 是精确的总体级恒等式（非 bound），将偏差分解为 δ_s · Δτ / (1−2π̄) 的乘积形式，三个成分可解释。完整证明可逐步验证（Appendix B），520 配置经验验证 R²=0.994(K=2)/0.974(K=4)。Remark 2 推广至非对称 CM（R²=0.991）。Proposition 2 给出 debiasing hurts 的充要条件。

**S2. 异常诚实的失败报告** [R1 highlight]
完整报告两个 EC-HTE 失败案例：(1) Appendix H hate speech FNR=53.3% 导致 null result；(2) Appendix K semi-real CM 在所有 n_expert 下 EC-HTE RMSE 均高于 Global（n=100 时 0.784 vs 0.263）。Table 7 明确报告 TweetEval 中 EC-HTE vs Global 差异不显著（p=0.395）。这种透明度在投稿论文中罕见。

**S3. 实验覆盖全面** [R1+R2 共识]
520 配置 × 100 MC runs + PPCI 4-DGP 正交设计 + R-learner 替代估计器 + 乘法 DGP + 子群误指定鲁棒性（p_flip 达 50%）+ 6 个 OpenAI 模型跨模型一致性 + MC standard errors。远超多数投稿论文的验证深度。

**S4. 实用工作流设计** [R1 highlight]
Section 5.4 推荐工作流（pilot → Δπ → check conditions → decide）为 practitioner 提供具体可操作指导，包括明确适用条件和降级策略。

**S5. PPCI 组合正交性论证** [R1+R2 共识]
4-DGP 实验巧妙分离协变量/结果两个误差维度，DGP C 下 EC-HTE+PPCI |bias| 从 0.179 降至 0.007（25×），互补性论证完整。

---

## Weaknesses

### Critical

**C1. 所有正面结果来自模拟误分类，唯二真实 LLM 数据实验均为负面结果** [R1-W1, R2-W3, R1+R2 共识]
主实验和 TweetEval 半合成的误分类率均为合成注入（π_s ∈ {0.05, 0.10, 0.15, 0.25}），非实际 LLM 标注。唯二使用真实 LLM CM 的实验：
- Appendix H (Hate Speech, GPT-4.1): null result，所有修正后 CI 包含零
- Appendix K (Semi-real CM, GPT-4.1): EC-HTE RMSE 在所有 n_expert 下均高于 Global（Table 9: 0.784 vs 0.263 at n=100; 0.260 vs 0.196 at n=500）
- Appendix K (GPT-3.5-Turbo): EC-HTE RMSE 超出 Global 1.3-3.5×

论文将失败归因于 FNR≈0.5 或类别不平衡，但未提供"在多少真实 LLM 标注场景中所有子群满足 max(FPR,FNR)<0.5"的经验证据。这从根本上削弱了方法的实用性主张。

**C2. 正文超 EMNLP 2026 8 页限制** [R2-N1, R1 AGREE]
Section 6 Conclusion 起始于第 9 页。EMNLP 2026 long paper 正文严格 8 页（Limitations/Ethics 不计入）。Desk reject 级别格式违规。

**C3. Abstract 选择性报告诊断 AUC** [R2-N2, R1 AGREE]
Abstract 仅报告 subgroup-level AUC=0.83，省略 setting-level AUC=0.47（Section 5.4 明确称 "no better than random"）。虽已加 "at the subgroup level" 限定词，但读者仅看 Abstract 会获得对诊断准则的过度乐观印象。

### Major (Reviewer 共识)

**M1. 诊断准则存在根本矛盾** [R1-W3, R2 AGREE]
(a) Setting-level AUC=0.47：practitioner 面对的决策是"是否对这个研究应用 EC-HTE"，但 setting-level 诊断完全无效。
(b) 循环依赖：诊断需要 Δτ，但获得好的 CATE 估计恰恰是 EC-HTE 的目的。Pilot 估计受噪声标注影响，这个 bootstrap-like 论证未被 formalized。

**M2. 假设 A2(对称) + A3(平衡) 过强，放松分析不足** [R1-W4, R2-W2, 共识]
- A2：GPT-4.1 真实 CM（Table 8）S0 FPR=0.054 vs FNR=0.526（10× 不对称），A2 直接失败
- A3：Semi-real 用 P(Z=1)=0.18，远离 0.5。Appendix B 完整证明假设 M_s=C_s（仅 A3 下成立）
- Appendix J 非对称扩展仅 3 配置且均假设 P(Z=1)=0.5
- 缺少 P(Z=1) 连续变化时 bias identity R² 衰减的定量分析

**M3. 半合成实验子群定义缺乏外部效度** [R1-W6]
hashtag × text_length 与实际 CSS 研究的子群定义（种族、性别、年龄等人口统计学变量）不同。Ashwin et al. (2025) 的 5× 差异来自人口统计学子群，与文本特征子群的可比性未论证。极端不平衡（80/5/5/10）未测试。

### Major (存在分歧)

**M4. Multi-class Extension g(π̄) 未给闭合形式** [R1 Critical → R2 降级 Major]
Corollary 1 中 g(π̄) "collects matrix-inversion amplification terms" 但未给显式表达式。R1 认为 J>2 + asymmetric 组合的因式分解条件未严格证明；R2 认为核心场景 J=2 数学完整，g(π̄) 是可解释性问题而非正确性问题。
**Director 裁定**: Warning（R2 论点成立——核心定理在 J=2 下完整，Corollary 定位为 extension 而非核心结果）

**M5. EMNLP scope 边界** [R2-W4 Major, R1 REBUT]
R2 认为 Theorem 1 是纯统计结果，与 NLP 方法无直接关系。R1 反驳：(1) 问题定义来自 NLP（LLM 标注偏差）；(2) ARR guidelines 明确 diverse contribution types in scope；(3) 先例：Egami et al. 2024 NeurIPS、Audinet de Pieuchon et al. 2025 EMNLP 均为统计方法解决 LLM 问题。
**Director 裁定**: 不构成降分因素。R1 的反驳证据充分。

### Minor

**m1.** κ>100 singularity guard 阈值缺乏依据 [R1 Major → R2 降级 Minor → Director 采纳 Minor]
**m2.** 贡献列表 5 项偏多 [R2 Major, R1 部分反驳 → 共识缩减至 3-4 项]
**m3.** R-learner + 乘法 DGP 使用 50 MC seeds vs 主实验 100 [R1-W7]
**m4.** Gamma(3,1) hyperprior 敏感性分析范围过窄（0.5×-2×）[R1-W8]
**m5.** sui2026ppci 作者名有误 [R2-W6]
**m6.** 术语不一致（4 个术语指代同一结果）[R2-W7, R1 AGREE]
**m7.** 遗漏 Fong & Tyler (2021) [R1+R2 独立提出]

---

## Reviewer Consensus [AGREE]

1. **Theorem 1 正确优雅**：两位 Reviewer 均确认 proof 完整、product form 有独立理论价值
2. **真实数据验证是最大软肋**：所有真实 LLM 数据实验均为负面结果，理论与实践间存在显著鸿沟
3. **诊断工具实用性矛盾**：setting-level AUC=0.47，循环依赖问题
4. **假设过强**：A2+A3 在真实场景极少成立，放松分析不足
5. **页数超限**：desk reject 级别格式违规
6. **Abstract 选择性报告**：应同时报告两个层级 AUC
7. **遗漏 Fong & Tyler (2021)**

## Reviewer Divergence [REBUT]

| 问题 | R1 | R2 | Director 裁定 |
|------|----|----|--------------|
| Multi-class g(π̄) | Critical | Major/Warning | Warning（核心 J=2 完整） |
| κ>100 阈值 | Major | Minor | Minor（安全 fallback） |
| EMNLP scope | In scope | Borderline | In scope（先例充分） |
| 贡献数量 | 4 项合理 | 3 项 | 建议 3-4 项 |
| Overall score | 3.5 | 3.0 | 3.0（见下文） |

---

## Questions

**Q1.** [R1] 在多少真实 LLM 标注场景中，所有子群满足 max(FPR, FNR) < 0.5？请提供经验证据或文献综述。
**Q2.** [R1] Var(Ĉ_s) / Var(Y|Z,S) 在不同 n_expert 水平下的数值，以 justify plug-in SE 在 n≥100 时的合理性。
**Q3.** [R1] 4 数据点的 Spearman ρ（Appendix O cross-model consistency）是否有足够统计功效？
**Q4.** [R1] K=4 时诊断 pilot n=50（50/4=12.5 < 25 阈值）——诊断准则和方法本身在 K=4 时是否需要不同 pilot 规模？
**Q5.** [R2] K=4 实验使用的是 Theorem 1 还是 Corollary 4？（R1 交叉回应已澄清：K 是子群数非 Z 类别数，Theorem 1 直接适用）
**Q6.** [R1] Semi-real CM 的 CATE 注入方式 τ(z=0,s) = 0.3+0.1s 是否人为加剧了 EC-HTE 失败？

---

## Missing References

1. **Fong & Tyler (2021)** "Machine Learning Predictions as Regression Covariates," *Political Analysis* [R1+R2 共识]
2. **Semenova & Chernozhukov (2021)** "Debiased machine learning of conditional average treatment effects" [R1 建议]
3. **arXiv:2604.11581 (2026)** "Hidden Measurement Error in LLM Pipelines" [R2 建议, 待核实]
4. **arXiv:2601.02370 (2026)** "Variance-Aware LLM Annotation for Strategy Research" [R2 建议, 待核实]

**引用验证**: 31 条引用中 22 条 OpenAlex 验证通过，8 条轻微 mismatch（LaTeX 编码/年份），1 条手动确认（sui2026ppci 存在但作者名有误）。无虚假引用。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：**未请求**（项目配置未启用 external_review）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 warnings, 9 info, 0 critical）。

**Warnings**:
1. **Pages 3-6 连续 4 页无 figure/table**：理论推导部分尚可接受，但 page 6（Section 5.1 实验设置）纯文本加剧视觉单调。建议将 Figure 2 提前或插入 pipeline 示意图。
2. **主体仅 3 个 display items（Figure 1, Figure 2, Table 1）**：密度 0.33/页，偏低（通常 5-8/9 页）。大量实验结果仅文字描述引用 Appendix。建议提升 Figure 4（budget crossover）或 Figure 5（applicability frontier）至正文。
3. **Section 5 的 6 个子节均无 inline display item**（除 Table 1），视觉锚点不足。

**Info highlights**:
- Figure 1 位置优秀（p2），title-abstract-figure 一致性好
- Figure 2 heatmap 质量好，颜色方案直观
- Table 1 booktabs 格式规范
- 无 LaTeX 编译错误、未解析引用或 margin 溢出
- Appendix 图表丰富且格式统一

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

### 评分理由

**理论贡献有独立价值**：Theorem 1 的 exact bias decomposition identity 是一个正确且有启发性的结果，将全局校正偏差分解为可解释的乘积形式，对 LLM-annotation-for-CSS 社区有持久的警示价值。即使 EC-HTE 方法本身有条件限制，这个理论发现已足以支撑 Findings 发表。

**方法实用性证据不足以支撑 Main Conference**：
1. 所有正面实验结果来自模拟误分类，唯二真实 LLM 数据实验均为负面结果——这是区分 3.0 和 3.5+ 的核心因素
2. 诊断准则 setting-level 完全失效（AUC=0.47），practitioner 无法用它做出"是否应用 EC-HTE"的决策
3. 假设 A2+A3 在真实 LLM 场景中极少成立，放松后的行为分析不足

**格式问题加剧风险**：正文超 8 页是 desk reject 级别违规，虽可修复但反映提交准备不充分。

**R1 (3.5) vs R2 (3.0) 分歧裁定**：R1 的 3.5 基于"如果补充真实正面实验可达 4.0"的条件性评估。当前版本不满足该条件。R2 的 3.0 更准确反映论文现状：理论贡献足以 Findings，但实证缺口阻止 Main Conference。

### 接收建议

**Findings 接收条件**（可在 revision 中完成）：
1. 修复正文至 8 页以内
2. Abstract 平衡报告两个层级的诊断 AUC
3. 正文增加假设违反时退化行为的讨论

**Main Conference 升级条件**（需实质性新实验）：
1. 增加至少一个真实 LLM 端到端标注且 EC-HTE 有效的实验
2. 开发 setting-level 诊断替代指标
3. 补充 P(Z=1) ≠ 0.5 时的定量分析

---

## Detailed Comments

### Section 1 (Introduction)
- 贡献列表 5 项偏多，建议合并至 3-4 项（#3 诊断合并入 #1，#4 PPCI 合并入 #2）
- "achieving AUC = 0.83 in cross-validated evaluation"：应加 "though at the setting level, the diagnostic performs no better than random (AUC = 0.47)"

### Section 3 (Theory)
- Theorem 1 证明正确完整
- 建议更突出地讨论 A2/A3 放松的代价（当前仅 1 句话引用 Appendix）
- Corollary 1 (Appendix C) 的 g(π̄) 应给显式表达式或标注为 approximate structure

### Section 4 (Method)
- κ>100 阈值应提供 MC 实验 sweep 或自适应公式
- Plug-in SE 在 n≥100 时的合理性需定量 justify（Var(Ĉ_s) vs Var(Y|Z,S)）

### Section 5 (Experiments)
- Section 5.4 诊断准则：报告 pilot-estimated Δτ 的噪声影响，或开发仅基于 Δπ 的替代指标
- Section 5.5/5.6 建议移至 Appendix 以修复页数问题
- Table 1 可精简（5 block → 3 代表性配置）

### Limitations
- 篇幅和覆盖面合适（覆盖 3 个核心 limitation）
- 建议补充：A2/A3 假设在真实 LLM 标注中普遍不成立的明确承认

### References
- 补充 Fong & Tyler (2021)
- 修正 sui2026ppci 作者信息
- 考虑补充 Semenova & Chernozhukov (2021)