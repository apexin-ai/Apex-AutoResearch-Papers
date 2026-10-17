---
round: 3
review_mode: fresh
overall_score: borderline
timestamp: 2026-05-22T06:16:24.385290+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts

**目标 Venue**: EMNLP 2026 (via ARR May 2026 cycle)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性，R2: 新颖性与完整性）
**轮次**: Round 1 + 交叉分享，一轮收敛

---

## Summary

本文证明了一个 exact population-level bias identity（Theorem 1）：当 LLM 标注的误分类率在子群间异质时，使用 pooled confusion matrix 进行全局纠正会在子群 CATE 估计中引入与 δ_s × Δτ 成正比的偏差。在 50% 的实验配置中，全局纠正比不纠正更差。论文提出 EC-HTE（基于 hierarchical Bayesian 子群分层混淆矩阵估计 + CausalForestDML）和一个 Δτ-free 诊断准则（Proposition 3, AUC=0.86），后者仅凭可估计的误分类率即可判断全局纠正是否有害。方法在 520 合成配置、semi-synthetic TweetEval、7 个 LLM（4 开源 + 3 私有）× 2 NLP 数据集上验证。

---

## Strengths

**S1** [共识] 问题识别的原创性与重要性。首次形式化了 LLM 标注中 subgroup-heterogeneous misclassification 对 CATE 估计的影响——CSS 研究中日益重要但未被充分认识的问题。"Debiasing can hurt" 的洞察对 NLP+CSS 社区有实际警示价值。

**S2** [共识] Exact identity 而非 bound。Theorem 1 给出的是精确的 population-level identity（R²=0.994 验证），具有很强的理论优雅性和可解释性。product form δ_s × Δτ/(1−2π̄) 直接给出偏差来源和放大机制。

**S3** [共识] Δτ-free diagnostic 的独立实用价值。Proposition 3 不需要知道处理效应异质性 Δτ（通常不可观测），仅凭误分类率诊断全局纠正是否有害。即使不采用 EC-HTE，这一工具也有独立价值。

**S4** [共识] 异常诚实的 failure case 报告。Hate speech（FNR 过高导致失败）、semi-real validation（全 budget 下劣于 Global）、semi-synthetic TweetEval（EC-HTE 未显著优于 Global）等 negative results 均如实报告，并给出明确的 applicability conditions。这在同类工作中很少见。

**S5** [共识] 极为全面的 robustness checks。Asymmetric errors（Appendix J, R²=0.991）、class imbalance（Appendix T, R²≥0.976）、subgroup misspecification（Appendix P, coverage≥0.945 at 50% noise）、estimator choice（R-learner 89% bias reduction）、multiplicative DGP（coverage 0.955）、7 LLM cross-model consistency——覆盖面远超一般 EMNLP 论文。

**S6** [共识] 与 PPCI 的互补性论证。4-DGP 正交设计证明 EC-HTE（covariate-side）和 PPCI（outcome-side）各自必要、联合充分，|bias| 从 0.179 降至 0.007。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1** [共识, Critical] **正文超过 8 页限制**。Section 6 Conclusion 从 page 8 延伸至 page 9 顶部，明确违反 EMNLP 2026 正文 ≤8 页的严格限制。Limitations 章节从 p9 中部开始（不计入页数），但 Conclusion 属于正文。此前 Round 2 曾修复此问题但再次回归。**格式违规可能导致 desk reject，必须优先修复。**
- R1: 初审遗漏，交叉分享时确认并升级为 Must-Fix
- R2: 初审发现，定为 Warning，R1 升级后同意

### Should-Fix（影响评分但不一票否决）

**W1** [共识, Warning] **Appendix B 证明中间步骤代数错误**。(1−π̄)(1−π_s) − π̄π_s 展开应为 1−π̄−π_s，论文写为 1−π̄−π_s+2π̄π_s。最终结果通过独立的 "More directly" 推导验证正确，520 配置 MC 实证确认（R²=0.994）。但在以理论贡献为核心卖点的论文中，证明中的代数错误损害可信度。
- R1: 定为 Critical
- R2: 独立验证错误存在，建议降为 Warning（typo 不影响结果）
- **Director 裁定: Warning**。最终结果正确有独立验证和 MC 确认，属 typo 性质。但必须修正。

**W2** [共识, Warning] **Abstract/正文对方法适用范围的表述不够平衡**。Abstract 中 "reducing |bias| from 0.059 to 0.010" 来自合成极端异质性配置（K=2, extreme）。Semi-synthetic TweetEval（最接近真实场景）中 EC-HTE |bias|=0.027 未显著优于 Global 0.023（p=0.395），RMSE 更差（0.225 vs 0.124）。Hate speech 和 semi-real validation 中 EC-HTE 均劣于 Global。论文的核心贡献不仅是 EC-HTE 方法，更包含理论洞察和诊断工具，但 Abstract 的框架过于侧重方法优势。
- R1: 定为 Critical（实际场景未展示优势）
- R2: 部分 REBUT（核心贡献含理论+诊断；失败场景已诚实报告；EC-HTE 在设计适用区间内有效）
- **Director 裁定: Warning**。R2 的论点成立——论文的核心贡献不仅是方法本身，且失败场景已诚实报告。但 Abstract 需更平衡。

**W3** [共识, Warning] **主文未点明实验已联合违反 (A2)+(A3) 却仍有效**。Theorem 1 在 symmetric (A2) + balanced (A3) 下推导。附录分别放松了这些假设，但 Section 5.5 的 open-source LLM 实验隐含地在联合违反下运行（P(Z=1)≈0.65, FPR≠FNR），这恰恰是鲁棒性证据，但论文没有点明。
- R2: 提出，定为 Critical（叙事断层）
- R1: AGREE，补充 caveat（鲁棒性主要体现在 coverage 维持而非 bias/RMSE 优势）
- **Director 裁定: Warning**。叙事修复，不影响技术内容。但需如实反映 mixed picture。

**W4** [共识, Warning] **遗漏因果推断中二元变量误分类的计量经济学文献**。Frazis & Loewenstein (2003), Mahajan (2006), Lewbel (2007), Bound et al. (2001), Black et al. (2000) 与本文主题相关但未引用。论文的创新点与这些经典工作互补而非重叠（不需 IV、针对 HTE 非 ATE、heterogeneous 非 homogeneous misclassification），但需明确讨论区别。
- R2: 定为 Critical
- R1: AGREE 但建议降为 Warning（EMNLP vs Econometrica 期望不同）
- **Director 裁定: Warning**。在 Appendix F 增加讨论即可。

**W5** [共识, Warning] **"50% of configurations" claim 有误导性**。50% 在很大程度上是实验设计的机械产物（K=2 时每个配置必有一个 low-error subgroup）。更有信息的统计是 "among low-π subgroups, 84.6% experience increased bias"。

**W6** [共识, Warning] **τ(z) 不依赖于 S 的隐含假设未声明**。Theorem 1 假设 CATE 仅依赖 Z 不依赖 S，DGP 中 Y=τ(Z)·T+ε 确认了这一点，但未作为正式假设（A5）声明。

**W7** [共识, Warning] **部分 claims 统计显著性不足**。1,020 个 pairwise comparisons 中 72.7% 在 α=0.05 下显著。TweetEval 下 EC-HTE vs Global bias 差异 p=0.395，但 Abstract 措辞未附 significance qualifier。

**W8** [共识, Warning] **κ>100 singularity guard 阈值缺乏支撑**。Algorithm 1 使用 κ>100 作为 fallback 触发条件，未说明选择依据。两位 Reviewer 均指出此问题。

**W9** [R2, Warning] **Δτ-free 诊断 AUC=0.86 的 FP/FN 代价不对称未分析**。约 14% 子群收到错误建议。FN（漏报 global correction hurts）代价高于 FP（误报需要 EC-HTE）。论文仅报告 AUC，未讨论最优 threshold 或代价敏感决策。

### Minor（不影响接收）

- Section 3 符号密度高，Theorem 1 前缺直觉性数值例子（R2 提出，R1 同意但非 blocker）
- 子群数量仅测试 K∈{2,4}，未探索 K>4 可扩展性（R2 提出 K=8 合理建议）
- Proposition 3 诊断公式未推广到 asymmetric 情形（R1）
- "debiasing" 在 NLP 社区有歧义（fairness bias vs. measurement error correction），建议首次使用时定义（R2）
- Figure 2 heatmap 打印时偏小（R2）
- Table 1 CausalForest block 缺少 Strat. MLE baseline（R1）
- M_s 与 C_s 等价仅在 (A2)+(A3) 下成立，应明确标注（R1）

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成完全共识 [AGREE]：

1. 理论贡献有价值（exact identity + diagnostic），Overall 3.5 Borderline Conference
2. 正文超 8 页限制，必须修复
3. Appendix B 代数错误必须修正（分歧仅在严重程度）
4. Abstract 表述需更平衡（分歧仅在严重程度）
5. "50%" claim 有误导性，应改用条件统计
6. CATE 不依赖 S 的假设应正式声明
7. κ>100 阈值需补充依据
8. 假设联合失效的叙事桥接需要补充
9. 计量经济学文献需补充（分歧仅在严重程度和位置）

---

## Reviewer Divergence

三个问题存在严重程度定级分歧，均已由 Director 裁定：

| 问题 | R1 定级 | R2 定级 | Director 裁定 | 理由 |
|------|---------|---------|---------------|------|
| Appendix B 代数错误 | Critical | Warning | **Warning** | Typo 性质，最终结果有独立验证+MC确认 |
| 真实场景方法劣势 | Critical | Warning | **Warning** | 核心贡献含理论+诊断；失败已诚实报告 |
| 计量经济学文献遗漏 | Warning | Critical | **Warning** | EMNLP 投稿的文献覆盖期望不同 |
| 页数超限 | Must-Fix(升级) | Warning | **Critical** | 格式违规可能导致 desk reject |

分歧均为程度之争而非方向之争，不影响整体评估。

---

## Questions for Authors

**Q1**: 当子群由数据驱动方法（如聚类或决策树）发现而非预定义时，EC-HTE 的表现如何？Appendix P 测试了 subgroup label noise 但未测试 subgroup discovery。

**Q2**: Theorem 1 的乘积结构在连续协变量场景下是否有类似积分形式？

**Q3**: EC-HTE+PPCI 组合是否存在两种误差交互的场景，使得组合效果不是简单的加性改善？

**Q4**: 论文在 Abstract 中声称 "standard practice when LLM labels serve as effect modifiers"——能否提供具体引用说明 pooled confusion matrix correction 是当前 CSS 社区的标准做法？

---

## Missing References

以下文献与论文主题直接相关，建议在 Appendix F (Extended Related Work) 中增加讨论：

1. Frazis, H. & Loewenstein, M. (2003). Estimating linear regressions with mismeasured binary explanatory variables. *Journal of Econometrics*.
2. Mahajan, A. (2006). Identification and estimation of regression models with misclassification. *Econometrica*.
3. Lewbel, A. (2007). Estimation of average treatment effects with misclassification. *Econometrica*.
4. Bound, J., Brown, C. & Mathiowetz, N. (2001). Measurement error in survey data. In *Handbook of Econometrics*, Vol. 5.
5. Black, D., Berger, M. & Scott, F. (2000). Bounding parameter estimates with nonclassical measurement error. *JASA*.

区分要点：这些经典工作处理 marginal/average 效应下的 binary misclassification，不涉及 subgroup-level heterogeneity 结构下的乘积放大效应。

---

## External Review (Stanford Agentic Reviewer)

未配置，不适用。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 超时（300s 内未完成），未产生有效 findings。用户可选择重新触发。

---

## Overall Assessment

**Overall Score: 3.5 / 5 — Borderline Conference**

**置信度: 4 / 5**（两位 Reviewer 均熟悉因果推断、测量误差和 Bayesian 方法）

### 评分理由

**支持接收的因素**：
- 理论贡献扎实且干净——exact bias identity 不是 bound，有强 MC 验证
- Δτ-free diagnostic 有独立实用价值，即使不采用 EC-HTE
- 实验验证极为全面（520 合成 + semi-synthetic + 7 LLM + 2 数据集 + 15+ 附加实验）
- 诚实报告 failure cases，给出明确 applicability conditions
- 问题对 CSS+NLP 社区有实际紧迫性

**限制接收的因素**：
- 正文超 8 页（格式违规，desk reject 风险）
- 方法仅在极端异质性合成配置下展示优势，最接近真实的实验均未展示方法的 bias/RMSE 优势
- 核心方法本质是经典测量误差纠正的领域适配，NLP 原创性有限
- 证明中间步骤有代数错误（虽最终结果正确）
- 理论假设（symmetric, balanced）与实际 LLM 标注场景有距离，虽然实验隐含验证了鲁棒性但主文叙事未桥接

### 提升至 Conference (4.0) 的路径

若作者在修订中完成以下修改，论文可提升至 Conference 水平：
1. **修复页数超限**（必须，否则 desk reject）
2. **修正 Appendix B 代数错误**
3. **平衡 Abstract 表述**，明确标注结果适用条件
4. **补充假设联合失效的叙事桥接**
5. **声明 CATE 不依赖 S 的假设**
6. **补充计量经济学文献讨论**

其中 1-2 为硬性修复，3-6 为叙事/框架改善。核心技术内容无需修改。

---

## Detailed Comments

### Section 1 (Introduction)
- "standard practice" 的说法需要引用支撑或弱化为 "a common correction approach"
- 三条贡献清晰，但第二条信息过于密集（一句话包含方法描述 + 4 类实验 + 数字），建议拆分

### Section 3 (Theory)
- Theorem 1 的推导严谨，product form 优雅
- 建议在 Theorem 1 前增加一个具体数值例子（如 π₁=0.05, π₂=0.25, π̄=0.15 的场景），帮助 NLP 读者建立直觉
- (A2)+(A3)+(A4) 的条件应在 M_s=C_s 等式处明确标注
- 需要增加正式假设 (A5): τ(z,s) = τ(z) for all s

### Section 4 (Method)
- HB 估计的描述完整，MCMC 诊断详尽
- κ>100 singularity guard 需要补充选择依据（数值分析经验惯例或 sensitivity analysis）
- Variance-adjusted CausalForest 的 plug-in 近似局限已在 Limitations 中承认，处理恰当

### Section 5 (Experiments)
- Table 1 结构清晰，但 CausalForest block 缺少 Strat. MLE 行
- Section 5.2 的 "50%" claim 应附条件统计解释
- Section 5.3 对 TweetEval 的不利结果（p=0.395, RMSE 更差）讨论过于简略，应给予更显著的篇幅
- Section 5.4 recommended workflow 实用性强，但缺少 FP/FN 代价分析
- Section 5.5 multi-LLM validation 有说服力，但未点明实验联合违反 (A2)+(A3)

### Section 6 (Conclusion)
- 必须压缩至 page 8 以内
- 内容简洁有效，无冗余

### Limitations
- 覆盖面良好（budget threshold, classifier quality, symmetric assumption, plug-in SE, discrete subgroups, text vs demographic features, future real-data validation）
- 适当长度，符合 EMNLP 要求

### Appendices
- Appendix B: 修正代数错误（删除错误化简路径或修正中间步骤）
- Appendix F: 增加计量经济学 binary misclassification 文献讨论
- Appendix Q: 考虑按 heterogeneity level 分层的显著性分析
- 整体附录质量极高，robustness checks 全面