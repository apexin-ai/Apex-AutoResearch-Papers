---
round: 16
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T12:46:30.765234+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Multi-Class Annotation Errors in Causal Inference

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿轮次**: Round 16 (Fresh)
**Reviewer 编排**: 2 人（R1 方法严谨性, R2 新颖性/完整性）
**收敛状态**: 1 轮独立审稿 + 1 轮交叉分享后收敛

---

## Summary

本文系统分析了 K-class（K≥3）LLM 标注误差在七种因果 DAG 拓扑下的传播机制。核心贡献包括：(1) 推导每种拓扑的闭式 bias 表达式并建立 sign preservation taxonomy（confounding/collider 证明 sign preserved, exposure/IV 可反转）；(2) 提出 Annotation Sensitivity Values (ASVs) 诊断框架，包含 magnitude/significance/sign-flip 三个维度；(3) 基于 FWL 不变性证明矩阵校正方法在四种协变量拓扑下无效，并给出拓扑感知校正指南。实验涵盖 Monte Carlo 模拟（161 场景 MAPE 1.6%）、23 组真实 LLM 混淆矩阵验证和五种校正方法的系统比较。

---

## Strengths

**S1. 填补重要文献空白。** 首次在 K≥3 条件下统一分析七种标准 DAG 拓扑的标注误差传播。Brenner (1993) 仅处理二值混杂，TeBlunthuis et al. (2024) 覆盖二值四种拓扑，Lee & Wood-Doughty (2024) 仅 confounding。这一系统性本身是真正的贡献。[R1 S1, R2 S1 共识]

**S2. FWL 不变性结果具有高实用价值。** Section 4.5 + Appendix B.2 证明 matrix-based corrections（Naïve plug-in, MLA）在线性 OLS 下对四种协变量拓扑无效。这个非平凡的负面贡献（impossibility result）对实践者有直接指导意义，避免了无效校正尝试。[R1 S3, R2 S2 共识]

**S3. 理论-实验三层证据结构设计良好。** 每个理论 claim 都有解析证明（K=2）+ 数值验证（K≥3, 100K-210K 矩阵）+ 真实 LLM 混淆矩阵验证的三层支撑。[R1 S1, R2 S3 共识]

**S4. Sign preservation taxonomy 优雅且实用。** Proposition 1 将七种拓扑清晰分为 sign-preserving（confounding/collider, 解析证明）、conditionally preserving（mediation/M-bias/front-door）和 sign-vulnerable（exposure/IV），为实践者提供直接可用的风险评估维度。[R1 S2]

**S5. Algorithm 1 降低理论到实践的转化门槛。** 校正决策树覆盖风险评估、方法选择和 FWL 检查三步流程，具有工具价值。[R1 S5, R2 S4 共识]

**S6. Appendix 极其详尽。** 22 页 19 个 subsection 覆盖了几乎所有可预见的 reviewer 质疑点（非微分 stress test、非线性 DGP、ClinicalBERT 案例、校正方法敏感性等），体现严谨研究态度。[R1 S6, R2 S5 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [critical] K≥3 envelope monotonicity 仅为 Conjecture，与 "Multi-Class" 标题和核心 narrative 不匹配**
- 位置：Section 3.3 Theorem 1, Conjecture 1 (p.6), Table 10 (p.27)
- Theorem 1（envelope monotonicity）仅对 K=2 有解析证明。K≥3 为 Conjecture 1（ε-approximate, ε < 0.06），依赖 210,000 矩阵数值验证。
- 问题：(1) Dirichlet 均匀采样在高维空间覆盖率极低（K=7 时 42 自由度），210K 样本可能遗漏 adversarial corner cases；(2) Table 10 显示 60-97% 矩阵存在 exact monotonicity 违反（magnitude ≤ 0.013），说明 exact monotonicity 在 K≥3 下**系统性不成立**；(3) 论文未分析 "多大的违反会导致 ASV ranking 翻转"——0.013 的 bound 是否足以保证实用稳定性？
- 论文标题聚焦 "Multi-Class" 但核心结论在 K≥3 下仅为经验观察，ASV 框架的理论基础不完整。
- **建议**：(a) Abstract/Introduction 精确区分 "K=2 proven" vs "K≥3 conjectured with numerical support"；(b) 增加采样量到 10⁶ 并报告违反分布的尾部行为；(c) 分析 ε=0.013 下 ASV ranking 翻转的条件。
- **共识**：R1 N1 提出, R2 交叉 AGREE 并补充 ranking 稳定性分析缺失。两位均评为 critical。

**W2 [critical] 缺乏真实因果数据的端到端验证——实验仅验证公式正确性和 confusion matrix 属性**
- 位置：Section 4 整体, Appendix B.3
- 验证三层中缺第三层：Layer 1（解析 vs MC, MAPE 1.6%）验证数学正确性 ✓；Layer 2（23 LLM 配置性质）验证输入端行为 ✓；**Layer 3 缺失**：在已知 ground-truth 因果效应的数据上完整演示 "估计 C → ASV 诊断 → 选择校正 → 改善估计" 的端到端流程。
- ClinicalBERT case study (Appendix B.3) 的 ground truth 来自 OLS on gold labels，不是真正已知因果效应。
- **建议**：构建 NLP-native 半合成因果数据集（如 VAST stance K=3 + 注入已知因果效应 + LLM 重标注），对比无校正 vs ASV 校正的估计精度。或至少在 Limitations 明确承认此缺失（目前未提及）。
- **共识**：R1 N2 提出, R2 W5 独立提出, 交叉 AGREE。两位一致。R2 补充 rebuttal 周期内完整验证工作量偏大，接受 Limitations 承认作为最低修复。

### Should-Fix（影响评分但不一票否决）

**W3. Non-differential misclassification 假设主文讨论不足**
- 位置：Definition 1 (Section 3.1, p.4)
- 主文仅一句 "This holds when the LLM classifies without observing the outcome"。需增加何时成立（LLM 未观察 outcome）、何时失败（prompt 含 outcome-correlated context）、如何检验的讨论，并引用 Appendix B.6 stress test 结果。
- **共识**：R1 W1 提出, R2 AGREE。

**W4. Proportional effects 假设 (f = λg) 缺乏实践验证指导**
- 位置：Theorem 1 (p.6), Appendix B.13 Table 12
- Treatment effect 是待估计未知量，无法先验验证成比例性。Independent effects 下 sign failure rate 达 23%——直接削弱 "confounding preserves sign" 的适用范围。需讨论 testable implications 和哪类 NLP 任务可能满足。
- **共识**：R1 W2 提出, R2 AGREE。

**W5. ASV 创新性阐述需加强（降级自 R2 must-fix）**
- 位置：Section 3.3 (p.5-6), Remark 1
- R2 认为 ASV 仅为 E-value 的 reparametrization（must-fix）。R1 REBUT：topology-dependence（同一 C 在不同拓扑下 ASV 不同）和 sign-flip ASV（E-value 无对应物）是结构性创新。Confusion matrix 的 Birkhoff polytope 参数空间 vs E-value 的 [1,∞) 半线有本质几何差异。
- **Director 判定**：降为 should-fix。ASV 有真实创新但论文未充分 articulate 技术挑战的新颖性。Remark 1 需强化技术区别的深度。
- **分歧记录**：R2 维持 must-fix, R1 认为 should-fix。

**W6. Abstract 信息密度过高**
- 188 词覆盖 7 拓扑 + sign reversal + ASV + monotonicity + correction + FWL。建议精简到 3-4 核心信息点，移除具体百分比（2.1%, 52.6%）到正文。
- **共识**：R2 W1 提出, R1 AGREE。

**W7. EMNLP 受众可及性不足——核心术语解释薄弱**
- plim（仅脚注）、FWL theorem（无直觉解释）、Wald estimator、column-stochastic matrix、Dirichlet prior 均缺乏 NLP 语境下的直觉说明。建议 Section 3.1 增加 Intuition 段落用具体 NLP 例子建立直觉。
- **共识**：R2 W2 提出, R1 AGREE。高优先级。

**W8. "2.1% sign reversal" 限定不清晰——secondary vs primary coefficient**
- Abstract "sign reversal occurs in 2.1% of exposure configurations" 易误解为 primary treatment effect reversal，实际为 secondary coefficient（小效应量）。Table 1 Sign Flip 列为 0%（primary）。需在 Abstract 明确 "secondary-coefficient" 并在 Table 1 增加脚注。
- **共识**：R1 W4 提出, R2 W3 独立提出, 交叉 AGREE。

**W9. Correction guidance 作为三大贡献之一深度不足**
- Section 4.5 仅半页，五种方法选择标准未说明，缺计算成本讨论，Algorithm 1 放在 Appendix p.31。建议充实 Section 4.5 并将 Algorithm 1 简化版移入主文。
- **共识**：R2 W6 提出, R1 AGREE。

**W10. FWL invariance 在 logistic regression 下失效的含义未在主文讨论**
- Appendix B.14 显示 FWL invariance 在 logistic regression 下不成立（exposure bias ~78%）。这意味着对使用 logistic regression 的 NLP 研究者，matrix-based corrections 可能有效——完全改变 Section 4.5 的 correction guidance。主文应增加此讨论。
- **来源**：R2 Q3 提出, R1 交叉回应提升为 should-fix。

**W11. ASV C(δ) 均匀退化假设与 LLM 实际误差模式不符**
- C(δ) = (1−δ)I + δC₀ 假设所有类别以相同速率退化，但 LLM 中稀有类别通常先出错。需增加 class-frequency-weighted degradation path 稳健性实验。
- **共识**：R1 W3 提出, R2 AGREE（但认为影响程度偏低，因 empirical LLM 矩阵本身包含不均匀退化且 ASV ranking 仍稳定）。

**W12. "First unified analysis" novelty claim 需与经典文献区分**
- 需与 Carroll et al. (2006) Ch.15 和 Schennach (2020) 做显式区分。建议限定为 "first unified analysis for LLM-generated multi-class annotations across seven topologies"。
- **共识**：R2 N2 提出为 must-fix, R1 AGREE。Director 采纳 should-fix（限定修辞即可解决）。

**W13. Figure 2 子图过小，灰度打印无法区分**
- 七个子图挤在半页宽度，红/灰颜色区分依赖彩色打印。建议使用 hatching pattern 或拆分 figure。
- **共识**：R2 W4 提出, R1 AGREE。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识 [AGREE]：

1. K≥3 monotonicity 仅为 conjecture 是论文最大理论缺口
2. 缺乏端到端真实因果数据验证
3. Abstract 信息过载需精简
4. EMNLP 受众可及性需提升（术语解释）
5. "2.1% sign reversal" 限定不清（secondary coefficient）
6. Non-differential 假设主文讨论不足
7. Proportional effects 假设缺乏验证指导
8. Correction guidance 深度不足
9. Figure 2 视觉质量
10. Table 1 列定义需明确
11. FWL under logistic regression 主文缺讨论

---

## Reviewer Divergence

**D1. ASV vs E-value 创新性（R2: must-fix → Director: should-fix）**
- R2 认为 ASV 仅为 E-value reparametrization，核心逻辑均为 "minimum perturbation to nullify effect"。
- R1 REBUT：topology-dependence 和 sign-flip ASV 是 E-value 不具备的结构性创新。Confusion matrix 参数空间（Birkhoff polytope）与 relative risk 空间（[1,∞) 半线）有本质几何差异。
- **Director 采纳 R1**：ASV 有真实方法论创新，但论文需更好 articulate 技术新颖性。降为 should-fix。

**D2. Sign reversal 风险是否被高估（R2: should-fix vs R1: REBUT）**
- R2 认为 5/7 拓扑 sign reversal 为 0%，framing 暗示风险普遍严重。
- R1 REBUT：论文价值在于 topology-dependent risk taxonomy，不在于声称 sign reversal 普遍——告诉实践者哪些拓扑安全、哪些危险本身就是贡献。但同意 Abstract/Introduction framing 可更平衡。
- **Director 判定**：R1 论证更有说服力——taxonomy 是核心价值。但同意 framing 需平衡，作为 W8 的一部分处理。

**D3. IV 52.6% vs 0% gap 解释充分性（R1: should-fix vs R2: REBUT）**
- R1 认为需要比 "structural properties" 更具体的解释。
- R2 REBUT：Appendix B.10 已解释 Dirichlet 产生极端矩阵、LLM diagonal dominant、IV sign reversal 需 first-stage 符号翻转（真实 LLM 不太可能），但同意主文可增加 1-2 句直觉解释。
- **Director 判定**：R2 REBUT 有效——Appendix 已有合理解释。采纳 R2 建议在主文增加直觉说明即可，不额外列为 weakness。

**D4. Veitch et al. (2020) 引用必要性（R1: AGREE vs R2: REBUT）**
- R1 认为应引用。R2 REBUT：该工作处理 text-as-treatment 的连续表示学习，与本文离散多类别 measurement error 主题关联较弱。已引用的 Feder et al. (2022) 和 Pryzant et al. (2021) 覆盖了 text-based causal inference。
- **Director 判定**：R2 REBUT 有效。不列为缺失引用。

---

## Questions（需作者澄清）

**Q1.** Conjecture 1 在 non-proportional effects 下是否可能完全失败（而非 ε-approximate 违反）？Table 12 的 23% sign failure rate 与 monotonicity failure 的关系是什么？

**Q2.** 23 个 LLM confusion matrices 在 IV 拓扑下全部 0% sign reversal——具体哪些结构属性（diagonal dominance? off-diagonal 对称性? eigenvalue 分布?）阻止了 sign reversal？能否构造 realistic-looking 的矩阵使 IV sign reversal 发生？

**Q3.** Class-imbalanced 场景（如 K=10 中 rare class 占 5%）下 ASV ranking 是否仍可靠？C(δ) 的均匀退化与实际不均匀退化的差异会否改变 topology vulnerability ranking？

**Q4.** Non-differential 假设失败时（ε > 0.10），ASV topology vulnerability ranking（IV > Exposure > ... > M-bias）是否仍保持？Appendix B.6 覆盖了弱违反但未报告 ranking 稳定性。

**Q5.** ASV 的 topology-dependent 特性能否反向推断 DAG 拓扑？Appendix B.11 Table 9 暗示某些维度可区分拓扑（sign-flip behavior），但 magnitude ASV 跨拓扑可能相同——这个方向的可行性和局限性是什么？

---

## Missing References

以下引用经两位 Reviewer 交叉确认为应引用：

1. **Miles, Valeri, and Coull (2024)**. "Measurement Error-Robust Causal Inference via Constructed Instrumental Variables." arXiv:2406.00940. — 与 IV 拓扑分析直接相关。[R2 提出, R1 AGREE]
2. **Wei, He, Li, and Geng (2025)**. "Multiply robust causal inference in the presence of an error-prone treatment." Statistical Methods in Medical Research. — 与 exposure 拓扑分析直接相关。[R2 提出, R1 AGREE]
3. **Hernán MA, Robins JM (2020)**. "Causal Inference: What If." Chapman & Hall/CRC. Chapter 9 关于 measurement error 对 identification 的影响。— 因果推断标准教材。[R1 提出, R2 AGREE]
4. **Schennach (2020)**. 已在 bib 中但未在正文引用。应在 Related Work 引用或从 bib 移除。[R2 提出, R1 AGREE]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 因 API 限额耗尽（rate limit reset at 4pm UTC）而失败，未能完成 PDF 逐页检查。

**状态**: error
**原因**: Agent exited 1: You've hit your limit · resets 4pm (UTC)
**建议**: 用户可在限额恢复后重新触发视觉审查。

---

## Overall Assessment

**Overall Score: 3.5 / 5 (Borderline Conference)**

**评分分解**:

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 4/5 | 3.5/5 |
| Excitement | 3.5/5 | 3/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Clarity | — | 3/5 | 3/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**综合评价**:

论文选题重要且及时——LLM 标注误差在因果推断中的传播是 NLP×CSS 交叉领域的新兴关键问题。Sign preservation taxonomy 和 FWL invariance impossibility 是有价值的理论贡献，附录极其详尽，三层证据结构设计良好。

但两个核心问题制约了评分：

**(1) 理论完整性 gap**：论文标题和 narrative 聚焦 "Multi-Class"（K≥3），但最关键的 envelope monotonicity 结论在 K≥3 下仅为数值验证的 conjecture（且 exact monotonicity 系统性不成立，60-97% 矩阵违反）。这使得 ASV 框架在论文主要聚焦的 K≥3 情形下缺乏理论保证——从 reviewer 角度看，这是可以改善但目前存在的 gap。

**(2) 实验验证深度 gap**：Monte Carlo 验证了公式正确性，LLM empirical validation 验证了 confusion matrix 输入端，但从未在 outcome level 展示过 "使用本文方法确实改善了因果估计" 的端到端闭环。对 EMNLP 受众，这限制了对框架实际应用价值的判断。

此外，对 EMNLP 受众的可及性（术语解释、信息密度）和 correction guidance 的深度也需要提升。

**提升路径**：如果能 (a) 在 K≥3 理论保证上取得进展（至少 ranking 稳定性分析 + 增加验证规模），(b) 增加端到端案例研究或在 Limitations 明确承认此缺失，(c) 精简 Abstract + 增加术语直觉解释 + 充实 correction guidance，论文可达 Conference (4.0) 水平。

**EMNLP 2026 ARR 评分映射**：3.5 = Borderline Conference。论文有 Findings 级别的贡献，如上述问题得到充分修复可达主会议水平。

---

## Detailed Comments

### Section 1 (Introduction)
- "first unified analysis" claim 需限定为 "for LLM-generated multi-class annotations"，与 Carroll et al. (2006) 区分 [W12]
- Sign reversal framing 建议增加平衡性表述："five of seven topologies provide structural sign protection" [W8]

### Section 3.1 (Setup)
- 增加 Intuition 段落用 NLP 例子建立直觉 [W7]
- Non-differential 假设讨论扩充：何时成立/失败/检验 [W3]
- 核心符号内联定义或引用 Table 19 [minor]
- τ vs β_T 在不同拓扑下含义需首次出现时明确 [minor]

### Section 3.2 (Bias Expressions)
- Proportional effects 假设增加 testable implications 讨论 [W4]

### Section 3.3 (ASV)
- Remark 1 扩充技术挑战来源（Birkhoff polytope vs [1,∞) 几何差异）[W5]
- Conjecture 1 主文补充 worst-case 实际量级（"empirically ≤ 0.013"）[minor]
- C₀ 选取方式在主文简述 [minor]

### Abstract
- 精简到 3-4 核心信息点，移除 2.1%/52.6% 等具体数字 [W6]
- "sign reversal" 改为 "secondary-coefficient sign reversal" [W8]
- FWL invariance 声明加 "under linear regression" 限定 [existing issue R15-W2]

### Section 4.2 (Sign Reversal Results)
- Table 1 caption 增加 Violation/Sign Flip 列精确定义和脚注 [minor]

### Section 4.5 (Correction Guidance)
- 扩充：方法选择标准、FWL invariance 约束说明 [W9]
- 增加 logistic regression 下 FWL 失效讨论 [W10]
- Algorithm 1 简化版移入主文 [W9]

### Figure 2
- 改为全页宽度或拆分，增加 hatching pattern 替代颜色区分 [W13]

### Limitations
- 增加"仅模拟验证、无真实因果数据集端到端验证"的明确承认 [W2]

### Related Work
- 引用 Miles et al. (2024), Wei et al. (2025), Hernán & Robins (2020), Schennach (2020) [MR]