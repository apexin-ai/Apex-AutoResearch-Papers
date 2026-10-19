---
round: 18
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T15:44:43.616326+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Round 18（Fresh Review）

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿模式**: Fresh（重新审稿）
**Reviewer**: R1（方法严谨性）+ R2（新颖性/完整性）
**日期**: 2026-05-23

---

## Summary

本文研究 LLM 标注器产生的多类别标注误差（K≥3）如何在 7 种典型因果 DAG 拓扑下传播到下游因果估计。核心贡献包括：(1) 在非差异错分类假设下推导 7 种拓扑的闭式偏差表达式，建立 sign-preservation/reversal 二分法（5 种拓扑保持符号，exposure 和 IV 可逆转）；(2) 定义 Annotation Sensitivity Values (ASV) 框架，包含幅度、显著性和符号翻转三种诊断，揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑依赖脆弱性谱；(3) 证明 FWL 不变性使得矩阵校正方法在四种协变量拓扑下精确无效（0% bias reduction），并评估 5 种校正方法。论文通过 Monte Carlo 模拟（161 场景，grand MAPE 1.6%）和 23 个真实 LLM 配置（HumAID K=10, VAST K=3, CivilComments K=2）进行实证验证。

---

## Strengths

**S1. 真正的统一拓扑分析**: 首次在统一框架内系统比较同一 confusion matrix 在 7 种 DAG 拓扑下产生定性不同的偏差。sign-preservation/reversal 二分法是一个清晰有力的核心发现，填补了流行病学测量误差理论与 NLP 实践之间的缺口。[R1-S1, R2-Strength-1, 共识]

**S2. FWL 不变性负面结果**: 证明矩阵校正方法（confusion matrix inversion）对 4 种协变量拓扑的 bias reduction 为精确 0%——这是一个干净、完整的结构性结果（Appendix B.2 列空间论证），对实践者有直接警示意义。[R1-S3, R2-Strength-2, 共识]

**S3. 诚实的认知层级**: Proved（K=2, Theorem 1）→ Verified（K≥3, Observation 1）→ Conjectured（Conjecture 1）的三级层次在理论论文中值得赞赏，避免了对 K≥3 结果的过度声称。[R1-S2, R2-Strength-4, 共识]

**S4. 全面的实证验证**: 161 scenarios × 23 LLM configurations × 3 NLP tasks；100,000 Dirichlet matrices；theory-MC MAPE 1.6%（per-topology 0.3%-3.7%）。F₁ 与因果 bias 无显著相关性（Spearman ρ = -0.10, p = 0.45）的发现对 CSS 研究者有直接可操作价值。[R1-S4, R2-Strength-3/5, 共识]

**S5. 实用决策框架**: ASV 与 E-value 类比设计得当，Algorithm 1 的拓扑感知校正决策树为实践者提供清晰操作指南。[R1-S5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [format] **正文页数超出 EMNLP 2026 strict 8-page limit**
- Section 5 Conclusion 完整位于第 9 页（约 13-14 行主文内容溢出）。EMNLP 2026 strict 8-page limit 是硬约束，违规可致 desk rejection。
- R2 首提为 critical，R1 交叉确认违规存在但建议降级。**Director 裁决 must-fix**：格式合规是硬约束，修复成本极低（压缩 Section 4.5 + 精简 Conclusion）。
- 修复方案：(a) 精简 Section 4.5 "Case studies and sensitivity" 段落（细节已在 Appendix）；(b) Conclusion 压缩至 5-6 行；(c) 或将 Figure 4/5 之一移至 Appendix。

**MF-2** [soundness] **非差异错分类假设在 LLM 标注器语境下缺乏直接实证检验**
- Definition 1 要求 P(A*=j|A=k,Y) = P(A*=j|A=k)。LLM 预训练数据编码 A-Y 关联，可能系统性违反此假设。现有检验不充分：Appendix B.5 VAST topic-stratified 检验仅一个数据集，且 topic 分层 ≠ Y 分层；Appendix B.6/B.8 stress test 显示 ε=0.01 structured departure 即导致 14/16 K≥3 exposure 配置 sign reversal。
- R1 首提为 critical，R2 交叉 AGREE（但补充结构性论证——LLM API 不观测 Y——比 R1 承认的更强）。**共识 must-fix**。
- 修复方案：在至少一个有 gold labels 的 NLP 数据集上，按 Y 值分层计算 LLM 错分类矩阵，直接检验 P(A*|A,Y=0) ≈ P(A*|A,Y=1)。即使只做一个数据集（如 HumAID），也能为结构性论证提供 empirical backing。

### Should-Fix（影响评分但不一票否决）

**SF-1** [soundness, 高优先级] **K≥3 ASV monotonicity 仅为 Conjecture，削弱 Contribution 2 的理论定位**
- Theorem 1（envelope monotonicity）仅在 K=2 + proportional effects 下证明。K≥3 依赖 Observation 1（数值验证，ε<0.02）和 Conjecture 1。论文核心论点是 K≥3 引入结构性新现象，但其 ASV 框架恰恰无法为 K≥3 提供形式化保证。
- R2 首提为 critical，R1 交叉 AGREE with nuance（K≥3 贡献多维——偏差表达式、sign preservation、FWL 均对一般 K 成立，不仅限于 monotonicity；ε<0.02 使 ASV 误差在 2% 以内）。**Director 裁决 should-fix（高优先级）**：R1 论点有力，K≥3 贡献确实不仅限于 monotonicity。
- 修复方案：(a) 将 Contribution 2 重新表述为 "empirically validated diagnostic with proved K=2 foundation"；(b) 补充 monotonicity failure 的后果分析（如果 ε 达到极端值，对 ASV ranking 的影响有多大）。

**SF-2** [soundness, 高优先级] **比例效应假设 (f=λg) 在 NLP 场景下缺乏具体讨论**
- Theorem 1 依赖 f=λg。在 NLP 多类别处理（如 stance detection 的 favor/against/neutral）中，不同类别可能有质性不同的效应，不满足比例关系。论文仅一句话提及 "plausible in NLP tasks with a single quality dimension"。
- R1 首提为 critical，R2 REBUT 降为 should-fix（假设仅影响 Theorem 1 monotonicity，Proposition 3 提供 general case fallback，97.3% 实证保持率）。**Director 采纳 should-fix（高优先级）**：R2 论证有力——假设范围比 R1 描述的更窄。
- 修复方案：增加 2-3 句具体 NLP 因果推断场景的分析（如 stance detection 3-class 是否接近 proportional）。

**SF-3** [scope] **Logistic regression 讨论不充分**
- NLP 最常用 logistic regression。主文仅一句话提及 FWL invariance 在 logistic 下的破缺（Section 4.5）。Appendix B.14 显示 FWL 破缺幅度随 accuracy 增大（exposure: -22% to -78%）。Algorithm 1 未区分 OLS/logistic 路径。
- R1 首提，R2 强烈同意。**共识 should-fix**。
- 修复方案：Section 4.5 增加 1-2 段 logistic regression 指导，引用 Appendix B.2/B.7/B.14；Algorithm 1 增加 OLS/logistic 分支。

**SF-4** [presentation, 高优先级] **术语壁垒对 NLP 读者可达性不足**
- plim、FWL theorem、Wald estimator、column-stochastic matrix、Birkhoff polytope、Dirichlet prior——对 EMNLP 受众属于高门槛术语，直觉解释不充分。如果多数 reviewer 无法流畅理解 method section，将影响 soundness 和 confidence 打分。
- R2 首提，R1 交叉 AGREE。**共识 should-fix**。
- 修复方案：每个关键术语首次使用时增加 1-2 句直觉解释（约增 6-8 行，页数压缩后有空间）。

**SF-5** [presentation] **Contribution 3（correction guidance）正文深度与"贡献"定位不匹配**
- "Topology-aware correction guidance" 被列为三大贡献之一，但正文仅约 0.7 页。Algorithm 1 仅在 Appendix。与 Contribution 1（~3 页 method）和 Contribution 2（~1.5 页 ASV + experiments）相比深度不足。
- R2 首提，R1 交叉 AGREE（倾向降级为 practical implication）。**共识 should-fix**。
- 修复方案：(a) 将 Algorithm 1 提升至正文（需结合 MF-1 的压缩方案）；或 (b) 降级为 "practical implication" 而非 co-equal contribution。

**SF-6** [novelty] **ASV 与 E-value 的比较框架有误导性**
- Remark 1 的三点 "structural distinctions from E-values" 本质上是不同工具解决不同问题（annotation error vs. unmeasured confounding）。当前表述暗示 ASV 是 E-values 的改进版。ASV 的真正贡献是将 sensitivity analysis 范式适配到 annotation error + topology dependence。
- R2 首提，R1 交叉 AGREE with nuance（distinctions 准确但表述暗含 improvements over）。**共识 should-fix**。
- 修复方案：Remark 1 重新框定为互补工具（complementary tools for different sources of bias）。

**SF-7** [experiments] **Dirichlet(1,1,...,1) 采样对高维 K 代表性不足**
- K=5（20 参数）和 K=7（42 参数）下，均匀 Dirichlet 采样偏离实际 LLM 矩阵分布（对角线期望 1/K vs 实际 >0.6）。R2 补充：23 个经验 LLM 矩阵已验证核心结论，代表性问题不影响最终结论。
- R1 首提，R2 交叉 AGREE。**共识 should-fix（低优先级）**。
- 修复方案：补充 Dirichlet(α,1,...,1) (α>>1) 采样验证，或报告对角线 >0.6 子空间的 ε 值。

**SF-8** [method] **Significance ASV 对样本量 N 的依赖未充分探讨**
- δ_sig 通过 SE(N) 依赖于 N，Figure 3 仅展示单一 N 值。不同 N 下 significance ASV 的变化是 practitioners 的关键决策信息。
- R1 首提，R2 交叉 AGREE。**共识 should-fix**。
- 修复方案：增加不同 N（如 1K, 5K, 10K, 50K）下各拓扑 δ*_sig 变化的可视化（Figure 或 Table）。

**SF-9** [soundness] **Conjecture 1 的 ε<0.02 约束缺乏理论直觉**
- ε 约束完全来自数值实验，论文未解释为什么 ε 应该很小。R2 补充可能的直觉路径：proportional effects 下精确单调，deviations 来自 non-proportional residual。
- R1 首提，R2 交叉 AGREE。**共识 should-fix**。
- 修复方案：补充 1 段关于 ε 小的直觉论证（如与列随机矩阵空间的凸体结构或 proportional residual 分析相关）。

### Minor（不影响接收）

1. **Abstract 信息密度过高**：约 184 words 符合 ≤200 限制，但 7+ 具体数字首次阅读难以消化。建议精简至 2-3 个最具冲击力的数字。[R2-minor-2, R1 AGREE]
2. **Figure 2 灰度打印可辨识性**：红色 sign reversal 标识在灰度下难以区分，建议增加 hatching/pattern fill。[R2-W4, R1 AGREE]
3. **τ 符号 overloading**：τ 在不同拓扑下含义不同但未充分标注。[R2-minor-1, R1 AGREE]
4. **Orphan bib entries**：manski1990 未在正文引用，应移除或添加引用。[R2-minor-3]
5. **引用格式不一致**：部分 bib 条目缺 doi 或页码。[R2-minor-4]
6. **"First unified analysis" 措辞**：限定词过多，建议简化为 "first systematic topology-specific comparison"。[R2-W5, R1 partial REBUT: claim 有合理基础但措辞可优化]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识（[AGREE] 或交叉后无争议）：

1. **非差异错分类假设需要 Y-stratified 实证检验** [must-fix] — R1 首提，R2 AGREE
2. **页数超限需修复** [must-fix (R2) / should-fix (R1)] — 违规存在无争议，仅严重性有分歧
3. **Logistic regression 讨论不充分** [should-fix] — R1 首提，R2 强烈同意
4. **NLP 术语壁垒** [should-fix] — R2 首提，R1 AGREE
5. **Contribution 3 深度不足** [should-fix] — R2 首提，R1 AGREE
6. **ASV vs E-value 框架重新定位** [should-fix] — R2 首提，R1 AGREE with nuance
7. **Figure 2 灰度可辨识性** [minor] — R2 首提，R1 AGREE
8. **Significance ASV N-dependence** [should-fix] — R1 首提，R2 AGREE
9. **Conjecture 1 ε 理论直觉** [should-fix] — R1 首提，R2 AGREE

---

## Reviewer Divergence

以下问题存在严重性分级分歧（**Director 已裁决**）：

| 问题 | R1 判断 | R2 判断 | Director 裁决 | 理由 |
|------|---------|---------|---------------|------|
| 比例效应 f=λg 假设论证 | critical | should-fix (REBUT) | **should-fix（高优先级）** | R2 论证有力：假设仅影响 Theorem 1 monotonicity，Proposition 3 提供 fallback，97.3% 实证保持率 |
| 页数超限 | should-fix (M5) | must-fix (N1) | **must-fix** | 格式合规是硬约束，修复成本极低 |
| K≥3 monotonicity 理论缺口 | strong should-fix | must-fix (N2) | **should-fix（高优先级）** | K≥3 贡献多维（偏差表达式 + sign preservation + FWL），不应仅以 monotonicity 证明缺口评判 |

---

## Questions

汇总两位 Reviewer 的关键提问（供 author response 参考）：

1. **ClinicalBERT case study 中是否检验了 f=λg？** 不同吸烟状态类别对死亡率的效应是否近似成比例？[R1-Q1]
2. **2.7% 不满足 Theorem 1 条件的 LLM 配置有什么共同特征？** 是否与特定 LLM 或数据集相关？[R1-Q3]
3. **Sign-flip ASV 的实际使用循环**：practitioners 需要先知道真实 τ 的符号才能计算 sign-flip ASV，如何处理这个 bootstrap 循环？[R2-Q3]
4. **Logistic regression 下 FWL 破缺幅度对大 K 如何变化？** Table 5 只测试了 K=3。[R1-Q4]
5. **多维 ASV 的可能性**：当前沿单一 C(δ) 路径搜索，是否考虑过 per-category sensitivity？[R1-Q5]
6. **非差异假设的 stress test 含义**：ε=0.01 即导致 14/16 K≥3 exposure sign reversal，是否意味着论文分析对 differential misclassification 极其脆弱？[R2-Q4]

---

## Missing References

- **Imai and Yamamoto (2010)**, "Causal Inference with Differential Measurement Error" — 与非差异假设形成对比 [R1 建议, R2 AGREE]
- **Nguimkeu, Denteh & Tchernis (2019)**, "On the estimation of treatment effects with endogenous misreporting" — treatment misclassification 相关 [R2 建议]
- **Ogburn and VanderWeele (2013)** — bias amplification under covariate misclassification 后续工作 [R1 建议, R2 指出 2012 版已引用]

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求。本项目未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: error — 视觉审查 Agent 因 rate limit 未能完成检查（"You've hit your limit · resets 4pm (UTC)"）。用户可在 limit 重置后重新触发。

---

## Overall Assessment

**Overall Score: 3.5 / 5 — Borderline Conference**

| 维度 | R1 | R2 | 合并 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 3.5 | 3.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Confidence | 4 | 4 | 4 |

**综合评语**：

论文在统一框架内首次系统分析了多类别标注误差在 7 种 DAG 拓扑下的因果偏差传播，贡献真实（bias taxonomy + FWL invariance 负面结果）、验证充分（161 scenarios, 1.6% MAPE）、认知层级诚实。FWL 不变性证明和 F₁ 与因果 bias 无相关性的发现对实践者有直接价值。

制约评分的主要因素：

1. **Must-fix 阻塞项**：(a) 页数超限需压缩（修复成本低）；(b) 非差异错分类假设缺乏 Y-stratified 实证检验（修复需要实验工作，但在 HumAID 上可行）。

2. **理论-应用鸿沟**：核心理论保证（Theorem 1 monotonicity）仅在 K=2 + proportional effects 下成立，而论文的核心卖点是 K≥3 的结构性新现象。虽然偏差表达式和 FWL 不变性对一般 K 成立（不依赖 Theorem 1），ASV 框架的 K≥3 保证仍是 conjectural。Contribution 2 需要更谨慎的定位。

3. **受众适配**：面向 EMNLP 的论文使用大量计量经济学术语（plim、FWL、Wald estimator），NLP 读者的可达性不足。Correction guidance（Contribution 3）作为核心贡献之一但正文深度不匹配。

**条件上调**：如果作者在 revision/rebuttal 中充分回应 MF-2（Y-stratified 检验）、SF-1（Contribution 2 重新定位）和 SF-4（术语直觉解释），评分可上调至 **4.0（Conference）**。MF-1（页数超限）是纯排版修复，不影响学术评价。

---

## Detailed Comments

### Section-by-Section

**Abstract**: 184 words 符合 ≤200 限制（R17 已验证）。信息密度高但主要结论完整。建议减少具体数字（保留 83.4% sign reversal 和 1.6% MAPE 两个核心数字即可）。FWL invariance 声明建议加 "under linear OLS" 限定。

**Introduction**: 三大贡献清晰列出。"first unified analysis" claim 在当前文献范围内成立（R1 确认），但限定词过多，建议简化措辞。Contribution 3 的正文深度需与定位匹配。

**Related Work**: 覆盖全面，四个关键领域（measurement error、LLM annotation、sensitivity analysis、correction methods）均有充分引用。可考虑补充 Imai & Yamamoto (2010) 和 Nguimkeu et al. (2019)。

**Method (Section 3)**: 核心理论贡献所在。Bias expressions (公式 1-5) 推导清晰。Theorem 1 → Observation 1 → Conjecture 1 层次诚实。主要问题：(1) 术语壁垒（plim、FWL、Wald 等需直觉解释）；(2) proportional effects 假设缺 NLP 场景讨论；(3) Remark 1 的 ASV-E-value 比较需重新框定为互补工具。

**Experiments (Section 4)**: 验证充分（161 scenarios, 1.6% MAPE）。Empirical validation 使用 3 个真实 NLP 数据集和 23 个 LLM 配置。F₁ 无预测因果 bias 的发现有力。主要问题：(1) Correction guidance (Section 4.5) 深度不足；(2) logistic regression 讨论不充分；(3) Significance ASV 的 N-dependence 需更系统展示。

**Conclusion + Limitations**: Conclusion 需压缩（当前导致超页）。Limitations 覆盖三个点（non-differential 假设、linear SEM、C 可估计性），位置正确（正文内）。

**Appendix**: 24 页，B.1-B.24 共 24 个子节，验证详尽。FWL 证明（B.2）完整。Logistic regression 验证（B.7, B.14）存在但主文未充分引用。交叉引用密集但结构清晰。