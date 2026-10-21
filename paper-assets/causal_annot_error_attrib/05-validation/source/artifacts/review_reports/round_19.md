---
round: 19
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T17:23:04.277497+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 19 审稿报告

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ACL ARR Long Paper)
**Deadline**: 2026-05-25
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性+理论证明+实验验证；R2: 新颖性+相关工作+写作质量+格式合规）

---

## Summary

本文系统研究 K-class non-differential misclassification 在七种典型 DAG 拓扑下对因果估计的偏差传播。主要贡献包括：(1) 推导了七种拓扑下的闭合形式偏差表达式，建立 sign-preserving（5 种）vs sign-reversing（exposure, IV）的二分法；(2) 引入 Annotation Sensitivity Values (ASV) 框架，在 K=2 下证明了 envelope monotonicity（Theorem 1），在 K≥3 下以 Conjecture 形式给出 ε-approximate monotonicity；(3) 证明 FWL invariance 导致 matrix-based corrections 对四种协变量拓扑无效，并提供拓扑感知的校正决策流程。实验覆盖 100,000 Monte Carlo 矩阵 + 23 个 empirical LLM 配置 + 3 个 NLP 数据集（HumAID K=10, VAST K=3, CivilComments K=2），161 个场景下 theory-MC MAPE 仅 1.6%。

---

## Strengths

**S1. [共识] 重要且及时的研究问题。** LLM 标注在 CSS 中的快速普及（Gilardi 2023; Ziems 2024; Baumann 2025）使标注误差对因果推断的影响成为紧迫问题。F₁ 与因果偏差无显著相关（Spearman ρ = −0.10, p = 0.45; Figure 4）有力论证了拓扑分析的必要性。

**S2. [共识] 全面的拓扑覆盖和系统性实证验证。** 7 种 DAG × K=2,3,5,7,10 × 4 个 LLM × 3 个 NLP 数据集 → 161 场景，grand MAPE 1.6%。多层级验证（理论-MC 对比 + 真实 LLM 矩阵 + 跨 K 鲁棒性）有说服力。

**S3. [共识] 清晰的安全/脆弱二分法。** Table 1 将 7 种拓扑分为 sign-preserving vs sign-reversing，为从业者提供直接可用的风险指引——这是论文最有实用价值的贡献。

**S4. [R1] Theorem 1（K=2 monotonicity）证明完整。** Appendix A.4 使用 perspective function convexity 建立严格证明，论证结构清晰。

**S5. [R1] Proposition 7（K≥3 exposure sign reversal counterexample）是强力构造性结果。** 直接构造了 C_kk > 0.5 仍导致符号反转的反例，明确了 K=2 vs K≥3 的分界线。

**S6. [R2] Abstract 信息密度高且合规（约 187 words，< 200 限制）。** 格式总体合规，8 页正文限制已满足。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1. [共识, critical] K≥3 Conjecture 1 未证明，但承载了 ASV 框架的核心实用性**

两位 Reviewer 一致认为这是本文最大的理论空白。论文的核心叙事围绕 K≥3 的结构性新现象（sign reversal, topology-dependent vulnerability），但 ASV 框架的理论基石——envelope monotonicity——仅对 K=2 且在 proportional effects (f=λg) 条件下得到证明（Theorem 1）。K≥3 的结果以 Conjecture 1 形式呈现，依赖 Dirichlet(1,...,1) 采样的数值验证。

R1 指出：K=2 证明方法（perspective function convexity + V_B(0)=0）结构上依赖 2×2 代数简化（"for K=2 only"），无法直接推广。数值验证未覆盖 adversarial 矩阵结构（near-permutation, block-diagonal）。R2 补充：这意味着论文对最不需要理论支撑的简单情况（K=2 经典衰减已有 Brenner 1993）给出了证明，对最需要的核心情况给出了猜想。

ASV vulnerability ranking（Table 3）和 Algorithm 1 在 K≥3 时的有效性完全依赖此 conjecture。如果 K≥3 的 ε-approximate monotonicity 在特定结构化矩阵上失效，ASV 排序的可靠性将受质疑。

**建议**：(a) 尝试 K=3 特殊情况证明（如对称混淆矩阵）；(b) 补充 adversarial 矩阵测试；(c) 在正文更显著标注 K≥3 结果的 conjecture 性质——不是 Limitations 中的 "primary open question"，而是 ASV 框架可靠性的前提条件。

**MF-2. [R2 首提, R1 部分同意] Contribution 3（FWL invariance + correction routing）分量不足**

R2 指出 FWL invariance（matrix-based corrections 对四种协变量拓扑无效）是 FWL 定理的直接推论：对协变量 dummy 变量的线性变换不改变处理变量系数——这从 FWL 的列空间保持性质直接可得。Section 4.5 两句话即推导完毕。

R1 交叉回应部分同意 FWL invariance 本身的 triviality，但认为 Contribution 3 的完整范围包括 Algorithm 1（拓扑→校正方法决策流程）和 Table 4 的五种方法跨拓扑比较（210 configurations），这些超越了单纯的 FWL 推论。

**共识**：FWL invariance 降为 Observation/Remark，Contribution 3 重聚焦于拓扑依赖的校正方法排序和决策流程（实证发现，非理论推论）。

### Should-Fix（影响评分但不一票否决）

**SF-1. [共识, major] "2.1% sign reversal under realistic accuracy (diagonal ≥ 0.7)" 采样方法不透明**

R1 计算后过滤法下约 73 个矩阵通过 diagonal ≥ 0.7 过滤（2.1% × 73 ≈ 1.5 个矩阵），统计功效极低。R2 核实发现附录 IV 分析使用 truncated sampling（每阈值 100K），但主文 Section 4.2 的 2.1% 未说明采样方法。Abstract 和 Introduction 均引用此数字作为核心 claim 证据。

**共识**：主文需明确标注采样方法和有效样本量。如果使用后过滤，需补充 truncated sampling 实验和 CI。

**SF-2. [共识, major] Proportional effects (f=λg) 在 NLP 场景中验证不足**

两位一致：(a) 97.3% 检验的方法和标准不透明——可能仅指单一 DGP 配置下 23 个 LLM 的比例；(b) f 和 g 依赖真实 A（非观测 A*），可验证性存疑；(c) Appendix Table 13 显示 OOB 率 23%（K=3 mediation, non-proportional f），说明条件在非平凡场景下不满足。

**建议**：明确 97.3% 的检验方法、DGP 数量和判定标准；讨论条件在什么 NLP 任务中合理（单维质量 vs 多维质量）。

**SF-3. [共识, major] Linear SEM 限定不足**

两位一致：Abstract 和 Conclusion 未限定 "under linear structural equation models"，可能给读者普遍适用的印象。Appendix B.14 的 logistic regression 验证（偏差 < 0.02）仅在 Section 4.5 一句话提及。CSS 研究中 logistic regression 远比 linear OLS 常见。

**建议**：在 Abstract 或 Contribution 列表加入 "under linear SEMs" 限定；Conclusion 讨论 nonlinear 扩展。

**SF-4. [R2 首提, R1 同意, major] MC-SIMEX 未引原始论文**

MC-SIMEX 在 Section 4.5、Table 4、Algorithm 1 中多次使用，但原始论文 Küchenhoff, Mwalili & Lesaffre (2006, *Biometrics*) 完全未引用。MLA 也缺规范引用来源。引用规范问题。

**SF-5. [R2 首提, R1 同意, major] "First systematic topology-specific comparison" 声称需限定**

TeBlunthuis et al. (2024) 已做 K=2 + 4 种拓扑的系统比较。本文的增量贡献在于 K≥3 + 7 种拓扑——建议改为 "the first multi-class (K≥3) topology-specific comparison"。

**SF-6. [R2 首提, R1 同意, minor] τ 符号拓扑依赖定义可能造成混淆**

τ 在不同拓扑下含义不同（confounding: X 系数; exposure: β_j; mediation: τ_direct），但后续 ASV 和 correction 讨论中频繁用 τ 进行跨拓扑比较。建议用下标区分或在 Table 1 增加定义列。

**SF-7. [共识, minor] NLP 读者可及性**

plim, FWL, Wald estimator, column-stochastic polytope, perspective function convexity 等术语对 EMNLP 读者群不友好。plim 有脚注定义，但其他术语处理不一致。

**SF-8. [R2, minor] 5 个 orphan bib 条目**

imai_keele_tingley2010, miles2024measurement, neuhaus1999, richardson1993bayesian, valeri_vanderweele2014 在 .bib 中存在但未引用。

**SF-9. [R1 首提, R2 同意, minor] C(δ) 线性路径假设的路径依赖性未讨论**

C(δ)=(1−δ)I+δC₀ 是一条线性路径，但 column-stochastic polytope 中存在无数从 I 到 C₀ 的路径。不同路径上 ASV 阈值可能不同。Bootstrapping C₀ 部分缓解但路径形状影响未讨论。

---

## Reviewer Consensus [AGREE]

1. **K≥3 Conjecture 1 未证明**是本文最大理论空白——两位一致标为 critical
2. **FWL invariance 本身是 trivial corollary**——应降为 Observation，Contribution 3 重聚焦
3. **Proportional effects 验证不足**——97.3% 声称缺乏透明度
4. **Linear SEM 限定**——Abstract/Conclusion 需加限定词
5. **MC-SIMEX 引用缺失**——must-add
6. **"First systematic" overclaiming**——需限定为 K≥3
7. **实证工作扎实**——161 scenarios, 1.6% MAPE, 3 real datasets

## Reviewer Divergence [REBUT]

1. **Conjecture 1 术语**：R2 建议改为 "Empirical Observation"，R1 反驳认为 Conjecture 有可证伪的定量声称，比 Observation 更精确。→ **Director 采纳 R1**：Conjecture 是诚实且精确的数学用语。

2. **Limitations 长度**：R2 认为过短（3 句话），R1 反驳符合 EMNLP 2026 规则（覆盖 3 个核心限制点）。→ **Director 采纳 R1**：格式合规。但建议在 linear SEM 局限性上增加 1-2 句。

3. **F₁ vs bias 讨论充分性**：R1 认为主文讨论不足，R2 反驳 Section 4.4 + Figure 4 + Appendix Table 21 已充分。→ **Director 采纳 R2**：讨论已充分。

4. **R1-W2 "21 vs 23 configurations" 不一致**：R1 报告数值矛盾，R2 全文搜索未复现，可能是 R1 误读表号。→ **Director 撤销此项**。

---

## Questions（需要作者澄清）

1. Section 4.2 的 "2.1% sign reversal at diagonal ≥ 0.7"：采样方法是后过滤还是 truncated sampling？有效样本量是多少？95% CI？
2. Conjecture 1 的数值验证是否测试了 adversarial 矩阵结构（near-permutation, block-diagonal）？ε < 0.02 是否在 Dirichlet 之外的结构化矩阵上被验证？
3. K=3 对称混淆矩阵（C_ij = c for i≠j）能否给出 monotonicity 的严格证明？
4. "97.3% of empirical LLM configurations satisfy proportional effects"——检验方法、DGP 数量和判定标准是什么？
5. 0% primary coefficient reversal 是 β 向量结构（dominant category）的产物，还是对 β₁ ≈ β₂ 的边界情况也成立？
6. MC-SIMEX 和 MLA 的原始引用来源？
7. "binarization amplifies this gap 154×"（Introduction）的精确含义：偏差比值还是概率比值？

---

## Missing References

**Must-add:**
- Küchenhoff, H., Mwalili, S. M., & Lesaffre, E. (2006). "A general method for dealing with misclassification in regression: The misclassification SIMEX." *Biometrics*, 62(1), 85-96. — MC-SIMEX 原始论文
- Frisch, R. & Waugh, F. V. (1933). "Partial time regressions as compared with individual trends." *Econometrica*, 1(4), 387-401. — FWL 原始来源

**Nice-to-have:**
- Bross, I. D. J. (1954). "Misclassification in 2×2 tables." *Biometrics*, 10(4), 478-486. — non-differential bias toward null 奠基论文
- Yi, G. Y. (2017). *Statistical Analysis with Measurement Error or Misclassification.* Springer.
- Hausman, J. A., Abrevaya, J., & Scott-Morton, F. M. (1998). "Misclassification of the dependent variable in a discrete-response setting." *Journal of Econometrics*, 87(2), 239-269.
- Miao, W., Geng, Z., & Tchetgen Tchetgen, E. J. (2018). "Identifying causal effects with proxy variables of an unmeasured confounder." *Biometrika*, 105(4), 987-993.

---

## External Review

**状态**：未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

**状态**：Agent 超时（300s timeout）。视觉审查未能完成，无 findings 可报告。用户可决定是否重新触发。

---

## Overall Assessment

**评分: 3.5 / 5 (Borderline Conference)**

**置信度**: 4/5（两位 Reviewer 均有因果推断和 NLP/CSS 背景，仔细检查了证明和数值声称）

**评分理由**：

本文解决了一个重要且及时的问题——LLM 标注误差在因果推断中的拓扑依赖性传播。Bias taxonomy（7 种拓扑 × K≥3）是扎实的实证贡献，safe/fragile 二分法对从业者有直接价值，F₁ 与偏差脱钩的论证令人信服。实验覆盖面广（161 scenarios, 1.6% MAPE, 3 real datasets），Theorem 1 的 K=2 证明严格，Proposition 7 的构造性反例有力。

但论文存在一个核心结构性矛盾：**整篇叙事围绕 K≥3 的结构性转变展开（Abstract 第 2 句, Introduction 第 2 段），但 ASV 框架的理论基石仅对 K=2 得到证明。** K=2 的结果有成熟的先行文献（Brenner 1993），论文真正的理论增量在 K≥3——但这部分停留在 Conjecture 层面。此外，Contribution 3（FWL invariance）是 FWL 定理的直接推论，作为独立贡献分量不足。

**如果作者能**：(a) 提供 K=3 特殊情况的 monotonicity 证明或更强的理论界；(b) 将 FWL invariance 降格并重构第三个贡献；(c) 明确 "2.1%" 的采样方法和 proportional effects 的检验标准；(d) 补充缺失引用——**论文有望达到 Conference 水平 (4.0)**。

当前状态：实证工作足以支撑 **Findings 接收**，但理论深度不足以支撑主会议。

---

## Detailed Comments

### Section 1 (Introduction)
- "the first systematic topology-specific comparison" → 需限定为 K≥3（TeBlunthuis 2024 已做 K=2 + 4 topologies）
- "binarization amplifies this gap 154×" → 需在正文解释 154× 的精确含义
- 三个贡献的排列合理，但 Contribution 3 建议降级

### Section 3.1 (Setup and Notation)
- Non-differential misclassification 的 "architectural invariant" 论证已较充分（Y-stratified permutation test, stress test），是近期修改的改进点
- plim 脚注定义有效，但 FWL, Wald, column-stochastic 等术语建议统一添加直觉解释

### Section 3.2 (Multi-Class Bias Expressions)
- 偏差表达式推导正确，七种拓扑的覆盖系统
- τ 的拓扑依赖性定义需更清晰标注
- "83.4% sign reversal" 和 "2.1% under realistic accuracy" 需注明 Dirichlet 先验和采样方法

### Section 3.3 (ASV)
- Theorem 1 (K=2) 证明严格
- Conjecture 1 (K≥3) 是最大理论空白
- Remark 1 (ASV vs E-values) 已重写为 "complementary tools"，定位合理
- proportional effects (f=λg) 的 97.3% 声称需透明化

### Section 4 (Experiments)
- Theory-MC 对比（1.6% MAPE, 161 scenarios）有说服力
- Table 1 的 safe/fragile 分区清晰
- "2.1%" 采样方法需澄清
- Figure 2 x 轴 scale 差异大，Figure 4 的 F₁ vs bias 讨论充分
- Table 3 (ASV ranking) 是 headline result 但视觉不够醒目

### Section 4.5 (Correction Guidance)
- FWL invariance 作为 FWL 定理推论可在两句话内完成——建议降为 Observation
- PPI++ 对 M-bias 有害 (−88%) 和 MC-SIMEX 对 front-door 有害 (−62.4%) 是非平凡的实证发现
- Algorithm 1 有实用价值

### Section 5 (Conclusion) + Limitations
- Conclusion 在 page 8，格式合规
- Limitations 覆盖 3 个核心限制点（non-differential, linear SEM, Monte Carlo），符合 EMNLP 2026 规则
- 建议在 linear SEM 限制上增加 1-2 句讨论 logistic regression 的适用性

### 格式合规
- 正文 ≤ 8 页 ✓
- Abstract < 200 words (187 words) ✓
- Double-blind (Anonymous ACL submission) ✓
- Limitations 在正文中 ✓
- 5 个 orphan bib entries 需清理
- MC-SIMEX / FWL 原始引用需补充