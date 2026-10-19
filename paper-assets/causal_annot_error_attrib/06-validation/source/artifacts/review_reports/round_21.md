---
round: 21
review_mode: fresh
overall_score: borderline
timestamp: 2026-05-23T20:08:38.795952+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 21 (Fresh Review)

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**目标 Venue**: EMNLP 2026 (ARR Long Paper)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人 — R1 方法严谨性 / R2 新颖性与完整性
**轮次**: 1 轮达成共识（无需第二轮）

---

## Summary

本文研究 LLM 生成的 K 类标注误差如何在 7 种典型 DAG 拓扑（confounding, exposure, mediation, collider, M-bias, front-door, IV）下传播到下游因果估计。作者推导了每种拓扑的 bias 表达式，证明 K≥3 时 exposure 和 IV 拓扑可发生符号反转（二分类情况下不可能），提出 Annotation Sensitivity Values (ASV) 诊断工具，并基于 FWL 不变性给出 topology-aware 校正路由。理论结果通过 100,000 Dirichlet 矩阵采样、545,945 adversarial 曲线、23 个真实 LLM 配置和 Monte Carlo 验证（MAPE 1.6%）支撑。

---

## Strengths

**[S1] 系统性填补文献空白（R1-S1, R2-S1, 双方 AGREE）。** 7 种 DAG 拓扑 × K≥3 多分类的统一分析是此前文献中缺失的。Brenner (1993) 仅覆盖多分类混杂变量，Dosemeci (1990) 仅覆盖多分类暴露，Teblunthuis (2024) 限于二分类，Lee & Wood-Doughty (2024) 限于单一拓扑。"first systematic analysis" 声明在合理范围内。

**[S2] K≥3 符号反转结果具有实践警示价值（R1-S1, R2-S2, 双方 AGREE）。** Figure 2 展示的拓扑分化（exposure 83.4% sign reversal, IV 52.6%, 其余 5 种拓扑 0%）是一个有意义的负面发现，直接告知实践者哪些拓扑需要额外警惕。

**[S3] 证明严谨（R1-S2, R2 交叉 AGREE）。** R1 逐步验证了 Theorem 1（perspective function 凸性论证）、Theorem 2（对称分解 + 因式分解）和 Proposition 1-3（Cauchy-Schwarz），均正确。R2 独立确认。

**[S4] 诚实的理论边界声明（R1-S3, R2 交叉 AGREE）。** Theorem 2 对称假设在 Remark 4 中被坦诚讨论为 "theoretical anchor"；Conjecture 1 被正确标注；proportional effects 违反率（23%）被量化报告。

**[S5] 多层数值验证体系超出同类工作标准（R1-S4, R2-S4, 双方 AGREE）。** 100,000 Dirichlet + 545,945 adversarial + 23 真实 LLM 配置 + Monte Carlo (MAPE 1.6%)。

**[S6] FWL 不变性的"负面结果"有实践指导价值（R1-S5, R2-S5, 双方 AGREE）。** 矩阵校正在 4 种 covariate 拓扑下无效（RMSE 减少 0%），阻止了盲目应用校正方法。

**[S7] Related Work 覆盖全面，引用验证通过（R2-S6）。** R2 验证了关键引用的真实性（Brenner 1993, Dosemeci 1990, Angelopoulos et al. 2023, Lee & Wood-Doughty 2024, Baumann et al. 2025）。

---

## Weaknesses

### Must-Fix

**[MF-1] K≥3 理论贡献呈现"已证但不实用 vs 实用但未证"的尴尬结构（R1-W1 must-fix, R2-W1 should-fix, 共识）。**
- Theorem 1 仅对 K=2 完全成立——对 NLP 场景最不相关（多数任务 K≥3）
- Theorem 2 要求 K=3 对称混淆矩阵——10 个 VAST 配置的实际偏差 d_rel=0.33（Remark 4, p.18），不是"近似成立"而是"显著偏离"
- Conjecture 1（一般 K≥3）有充分数值支持（ε < 0.017）但未获证明
- 论文在正文 p.6 将 Theorem 2 呈现为主要理论结果，附录才承认局限，可能误导读者
- **建议**：在正文中将 Theorem 2 明确定位为 theoretical anchor（证明单调性结构在特定条件下精确成立，为 Conjecture 1 提供结构性支撑），而非实用保证；讨论 Conjecture→Theorem 的证明障碍（是 K≥3 列随机矩阵的组合复杂性，还是存在根本困难？）

**[MF-2] 缺少端到端的真实 NLP 因果推断应用（R1-W2 must-fix, R2-W3 should-fix, 强共识）。**
- 对 EMNLP 应用导向 venue，当前所有实验均为"验证理论正确性"（Monte Carlo vs 解析解）或"验证假设成立"（non-differential test），缺少完整场景：在真实 NLP 任务中使用 LLM 标注→ASV 诊断→校正→因果估计，展示框架如何改变实质性因果结论
- ClinicalBERT (Appendix B.3) 使用真实混淆矩阵但合成 ground truth；End-to-End Demo (B.19) 同样基于合成 DGP
- 论文已有 HumAID (K=10) 的混淆矩阵，增加对应的端到端因果分析（如灾害类型→公众响应的因果效应估计）可行性较高
- **建议**：增加至少一个真实 NLP 因果推断案例，完整展示 annotate→estimate→correct 全流程

### Should-Fix

**[SF-1] Non-differential misclassification 假设在 NLP 中可能过强，主文讨论不足（R1-W3/Q4, R2-W2, 共识）。**
- 主文 Section 3.1 以"architectural invariant"（LLM 只看 text，不看 Y）为由论证 non-differential 成立，但 Appendix B.25 的 content-dependent proxy 测试（topic, sentiment）显示显著 Y-stratification（12/12 中仅 1/12 拒绝是因为 content-independent proxy 占多数）
- R1 指出关键细微之处：如果 A 完全中介 text features→Y，non-differential 仍可成立；但 NLP 中 Y 和 text 的关系通常更复杂
- **建议**：在 Section 3.1 或 Limitations 中增加 2-3 句讨论：(a) 哪些 NLP 任务满足 non-differential（content-independent proxy）；(b) 违反时偏差表达式如何变化；(c) 引导到附录 B.25 的实证检验

**[SF-2] Proportional effects 假设的 NLP 适用性缺少实质论证（R1-W3, R2 交叉 AGREE, 共识）。**
- 该假设（f=λg）是 Theorems 1-2 的核心前提
- Table 14 (B.13) 显示独立 f,g 下 OOB 率达 23%；Table 18 报告 97.3% sign preservation，但混合了 proportional/non-proportional
- 主文几乎未讨论 NLP 因果场景中 f=λg 的实质合理性
- **建议**：增加 1-2 句 domain-specific 论证，说明哪些 NLP 场景 proportional effects 合理（如单一质量维度驱动两条路径），哪些不合理

**[SF-3] Linear SEM 适用范围在 Limitations 中讨论过于简略（R1-W4 should-fix, R2 partial REBUT, 部分共识）。**
- R1 指出 exposure 下 logistic 校正恶化 -78%，Limitations 仅"assume linear SEMs"一句
- R2 partial REBUT：附录 B.7/B.14 已提供充分非线性验证（covariate 拓扑 FWL invariance 保持，mean logistic bias reduction ≤5%），R1 的批评主要针对呈现方式
- **建议**：在 Limitations 中明确引用附录结论——哪些拓扑在非线性下仍成立（covariate），哪些不成立（exposure），实践者应如何调整

**[SF-4] Conjecture 1 的 adversarial search 系统性不明（R1-W5, R2 交叉 AGREE with balance, 共识但低优先级）。**
- 4 种结构族基于直觉选择，未解释为何足以覆盖潜在 counterexample 空间
- R2 提供平衡：max violation 0.017 极小，实践影响可忽略
- **建议**：增加一段说明为何这 4 种族具有代表性，或是否尝试过梯度优化寻找最大违反

### Minor

**[MI-1] 对 EMNLP 读者可达性有待提升（R1-W6, R2-W4, 双方 AGREE）。**
- plim, FWL, column-stochastic 等计量经济学概念对 NLP/ML 读者不够直观
- **建议**：Section 3.1 增加 2-3 句"Reader's Guide"，用非技术语言解释 bias 传播核心机制

**[MI-2] Correction routing (Algorithm 1) 作为三大贡献之一的权重定位（R2-W5 minor, R1 REBUT, 分歧存在）。**
- R2 认为 Algorithm 1 本质是已有方法的拓扑适配决策树
- R1 REBUT：FWL 不变性发现是核心理论基础，topology-dependent routing 概念本身有贡献
- 分歧已缩小为定位方式问题
- **建议**：强调 FWL 不变性发现作为独立贡献，将 Algorithm 1 定位为该发现的实践推论

**[MI-3] Venue 适配度处于边界（R2-W6, R1 隐含同意）。**
- 核心贡献在统计/计量层面，NLP 连接主要通过应用背景
- 不构成拒稿理由——ARR guidelines 允许跨学科方法
- 如补充真实 NLP 因果应用（MF-2），此问题自然消解

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致（交叉回应中均 [AGREE]）：

| # | 问题 | R1 定级 | R2 定级 | 共识定级 |
|---|------|---------|---------|----------|
| 1 | K≥3 理论贡献依赖 conjecture | must-fix | should-fix | **must-fix** |
| 2 | 缺少端到端真实 NLP 因果应用 | must-fix | should-fix | **must-fix** |
| 3 | Non-differential 假设主文讨论不足 | should-fix (Q4) | should-fix | **should-fix** |
| 4 | Proportional effects NLP 适用性 | should-fix | should-fix (交叉 AGREE) | **should-fix** |
| 5 | EMNLP 读者可达性 | minor | minor | **minor** |

---

## Reviewer Divergence

| # | 问题 | R1 立场 | R2 立场 | 解决状态 |
|---|------|---------|---------|----------|
| 1 | Algorithm 1 贡献权重 | REBUT：FWL 不变性赋予实质价值 | minor：本质是决策树 | 分歧缩小为定位方式，非根本矛盾 |
| 2 | Linear SEM 讨论 | should-fix：Limitations 过于简略 | partial REBUT：附录证据充分 | R2 论证有力（B.7/B.14），共识为改善 Limitations 呈现 |
| 3 | Soundness 评分 | 3.5/5 | 4.0/5 | R2 论证合理（claims 在 stated assumptions 内被充分支撑），取均值 3.75 |

---

## Questions（需作者澄清）

**[Q1]** Conjecture 1 的证明障碍具体是什么？是 K≥3 列随机矩阵的组合复杂性，还是特定拓扑存在结构性困难？是否有证据表明该 conjecture 可能为假？（R1-Q1, R2-Q1 共同追问）

**[Q2]** DAG 拓扑不确定时（NLP 因果推断中常见），实践者应如何使用本框架？是否对所有 7 种拓扑计算 ASV 并取最坏情况？（R2-Q2）

**[Q3]** ASV bootstrap CI 的 gold-standard 标签样本量对估计精度的影响？是否有最低样本量的经验规则？（R2-Q3）

**[Q4]** Algorithm 1 的阈值（risk level 分类）如何确定？是否应取决于 sample size 或其他条件？是否有 sensitivity analysis？（R1-Q3, R2 交叉 AGREE）

**[Q5]** Content-dependent proxy 导致 Y-stratification 显著时（如 stance detection），实践者应如何使用本框架？non-differential 假设在这类核心 NLP 任务中是否系统性地不成立？（R1-Q4）

**[Q6]** 非比例效应 (non-proportional f,g) 下 Theorem 1 的 monotonicity violation magnitude 有多大？Table 14 报告 OOB 率但未报告 violation 幅度。（R1-Q1, R2 交叉补充）

---

## Missing References

两位 Reviewer 均未发现重大引用遗漏。R2 验证了关键引用的真实性。可选补充：proximal causal inference with text data 文献（Mozer et al., Tchetgen Tchetgen 系列）——与本文 measurement error 视角互补但非必须。

---

## External Review (Stanford Agentic Reviewer)

**状态**：未启用。项目配置中 `external_review.paperreview_ai.enabled` 未设置。

---

## Visual Layout Check（非评分项）

**状态**：已完成（3 warnings, 0 critical, 19 info）

关键发现：
- **[Warning]** Pages 1-2 为连续纯文本（Title/Abstract/Introduction/Related Work），第一个 display item（Figure 1 DAG 拓扑图）直到 page 3 才出现。审稿人前 2 页看到的全是文字，缺少视觉锚定。建议考虑将 Figure 1 提前。
- **[Warning]** Figure 2 的 "Red = sign reversal" 图例文字非常小（~7pt），灰度打印时红色填充对比度可能不足。
- **[Warning]** Table 9（Appendix B.6, pp.25-26）跨两页，数值密度极高，建议在 caption 中标注关键行/列。
- **[Info]** 正文 8 页含 4 figures + 1 table = 5 个 display items，密度合理。所有表格使用 booktabs 风格。无 margin 溢出、引用未解析等排版问题。格式合规（8 页正文，Limitations 在正文内，双盲匿名）。

---

## Overall Assessment

**Overall**: 3.5 / 5 (Borderline Conference)
**Soundness**: 3.75 / 5 (R1: 3.5, R2: 4.0)
**Excitement**: 3.0 / 5 (R1: 3.0, R2: 3.0)
**Reproducibility**: 4.0 / 5
**Confidence**: 4.0 / 5

### 评分理由

本文在一个重要且日益相关的问题（LLM 标注误差的因果传播）上做出了系统性贡献。7 种拓扑的 bias 分类学填补了文献空白（S1），K≥3 符号反转结果对实践者有直接警示价值（S2），证明在其假设范围内严格正确（S3），数值验证体系超出同类工作标准（S5）。

阻碍达到 4.0 (Conference) 的原因：

1. **理论覆盖与实际需求的错位（MF-1）**：Theorem 2 对称假设偏差约 33%，K≥3 核心结论依赖未证 Conjecture 1。论文的理论贡献呈现"已证但不实用 vs 实用但未证"的结构性矛盾。

2. **应用验证的缺失（MF-2）**：对 EMNLP 应用导向 venue，缺少一个真实 NLP 因果推断端到端案例是显著短板。所有实验均为"验证理论"而非"展示影响"。

3. **核心假设的 NLP 适用性论证不足（SF-1, SF-2）**：Non-differential misclassification 和 proportional effects 两个核心假设在 NLP 场景中的合理性讨论分散在附录，主文几乎未触及。

### 修改建议优先级

| 优先级 | 问题 | 预估工作量 |
|--------|------|-----------|
| P0 | 增加端到端真实 NLP 因果案例 | 中（已有 HumAID 混淆矩阵） |
| P0 | 正文重新定位 Theorem 2（theoretical anchor + Conjecture 证明障碍讨论） | 小 |
| P1 | Non-differential 假设的 NLP 适用性讨论前置到主文 | 小 |
| P1 | Proportional effects 的 NLP 场景论证 | 小 |
| P2 | Limitations 中引用附录非线性验证结论 | 小 |
| P2 | Section 3.1 增加 Reader's Guide | 小 |
| P3 | Conjecture 1 adversarial search 系统性说明 | 小 |

如 P0 问题得到解决，评分可上调至 **4.0 (Conference)**。

---

## Detailed Comments

### Section 1 (Introduction)
- 叙事逻辑清晰，K=2→K≥3 的 structural transition 论证有力
- 三个贡献的陈述可微调：Contribution 3 (correction routing) 的 FWL 不变性发现值得更突出
- 数字密度尚可接受（相比早期版本已显著改善）

### Section 2 (Related Work)
- 三段覆盖（measurement error / text classifiers / sensitivity analysis）结构合理
- 引用验证通过，无虚构引用
- 与已有工作的定位公平——既不过度贬低也不过度夸大自身贡献

### Section 3 (Method)
- Definition 1 (non-differential) 简洁但主文讨论不足——需增加 NLP 适用性论证（SF-1）
- Equations 1-2 (confounding/exposure bias) 推导正确
- Theorem 1-2 证明严格但适用范围窄——需正文重新定位（MF-1）
- Conjecture 1 表述诚实，数值证据充分，但证明障碍未讨论
- Remark 1 (ASV vs E-values) 区分有说服力（topology dependence + sign-flip 维度）
- 符号负担较重——Reader's Guide 段落可显著改善可达性

### Section 4 (Experiments)
- 4.2 Bias Taxonomy：Monte Carlo 验证 (MAPE 1.6%) 可靠
- 4.3 ASV Framework：Figure 3 vulnerability ranking 直观有效
- 4.4 Empirical Validation：HumAID/VAST/CivilComments 真实混淆矩阵验证了理论预测，但缺少端到端因果应用（MF-2）
- 4.5 Correction Guidance：FWL invariance observation 有价值；Algorithm 1 阈值需要 sensitivity analysis

### Conclusion / Limitations
- Conclusion 简洁到位
- Limitations 段落过短——需增加 non-differential、proportional effects、linear SEM 的整合讨论
- 当前 Limitations 仅 3 个点，符合 EMNLP 规范但不够充分

### Appendix
- 证明完整（A.4-A.6），R1 逐步验证通过
- 数值验证附录极其详尽（24 页），超出审稿期望
- Table 9 (B.6) 跨页密集，建议标注关键行列