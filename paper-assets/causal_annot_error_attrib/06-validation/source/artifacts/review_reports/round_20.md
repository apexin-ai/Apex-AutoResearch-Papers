---
round: 20
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T18:50:35.079974+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 20 (Fresh Review)

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿模式**: Fresh（重新审稿，无历史记忆）
**Reviewer 配置**: 2人（R1: 方法严谨性; R2: 新颖性/完整性）

---

## Summary

本文分析了 K≥3 多类别非差异性误分类在 7 种因果 DAG 拓扑下的偏差传播，证明 5 种拓扑保持符号而 exposure 和 IV 可发生符号反转。提出 Annotation Sensitivity Values (ASV) 框架量化拓扑依赖的脆弱性，并证明矩阵校正方法对 4 种协变量拓扑因 FWL 不变性而无效。理论在限定条件下正确，100,000 次 Monte Carlo 验证与 545,945 条对抗曲线支撑。

---

## Strengths

**S1. 系统性覆盖填补文献空白。** 将 K≥3 多类别误分类与 7 种 DAG 拓扑的交叉分析做到前所未有的完整度。Teblunthuis (2024) 仅 K=2/4 拓扑；Lee & Wood-Doughty (2024) 仅单一 confounding。同时推广两个维度并发现质性新现象（sign reversal），非简单笛卡尔积。

**S2. K≥3 sign reversal 发现有实际价值。** 经典 "toward the null" 保证在 K≥3 下被系统性打破（exposure 83.4% sign reversal under uniform Dirichlet; 2.1% under realistic diagonal ≥ 0.7）。对使用 LLM 标注进行因果推断的研究者是重要警示。

**S3. FWL 不变性负结果优雅且有实践指导意义。** 证明 naive plug-in/MLA 对 4 种协变量拓扑下 bias reduction = 0%。直接改变 practitioner 的方法选择策略。

**S4. 理论-数值三层协同验证模式优秀。** 每个定理配有 analytic proof + Monte Carlo verification (MAPE 1.6%) + adversarial testing (545,945 curves)。这种验证深度在方法论论文中罕见。

**S5. 26 页 Appendix 验证充分。** 完整证明（A.1-A.9）、对抗验证（A.11）、非差异性压力测试（B.6）、非线性鲁棒性（B.7）、混淆矩阵估计鲁棒性（B.23）等形成完整的可信度链条。

**S6. 实证锚定。** 23 组真实 LLM 混淆矩阵（HumAID K=10, VAST K=3, CivilComments K=2）将理论预测与实际 LLM 配置对接，F₁ disconnect (Spearman ρ=-0.10, p=0.45) 论证有力。

**S7. 校正方法对比全面。** 5 方法 × 7 拓扑 × 210 配置，附带 Algorithm 1 决策流程。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [Critical, 共识] 缺少端到端因果应用验证。**
- R2 列为唯一 Must-Fix; R1 列为 Should-Fix
- 论文声称 "Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations"（Abstract 末句），但没有任何实验真正回答一个因果问题。Section 4.4 仅验证理论 violation rate 与真实混淆矩阵匹配；B.18 ClinicalBERT case study 仅回顾性分析已有混淆矩阵。缺少前瞻性的 annotate → estimate → correct 全流程 demonstration。
- **影响**：对 EMNLP 这样的应用导向 venue，声称"对 practitioner 有指导意义"的框架需要至少一个端到端 demo。
- **建议**：选择一个 text-as-treatment 数据集走完全流程，即使结果简单也比纯理论推导更有说服力。

**W2. [Critical, R1] Proportional effects 假设在 Limitations 中完全缺失。**
- Theorem 1（K=2）和 Theorem 2（K=3 symmetric）均要求 f = λg（proportional effects）
- Limitations 提到了 non-differential misclassification、linear SEMs、symmetric matrices、general K 开放性——唯独未提及 proportional effects
- B.13 Table 14 显示：non-proportional effects 下 OOB rate 达 84.6%，sign preservation 降至 75.5%
- **影响**：读者可能高估定理的一般性。这是论文理论贡献的核心假设。
- **建议**：(1) Limitations 明确列出 proportional effects 及其限制性；(2) Section 3.2 引入定理时加 scope caveat；(3) 引用 Table 14 数据说明退化行为。

**W3. [Critical, R1; Should-Fix, R2] Theorem → Conjecture 理论缺口在主文中表述不清。**
- Theorem 1（K=2）→ Theorem 2（K=3 symmetric）→ Conjecture 1（general K≥3, ε-approximate）连续呈现，"已证明"与"数值猜测"的边界模糊
- Conjecture 1 依赖 545,945 adversarial curves，但 adversarial search 结构类型为手动选择，无法排除未覆盖的病态结构
- **影响**：读者容易将 Conjecture 1 误读为已证明定理。
- **建议**：(1) 明确标注 "analytic proofs end here; the following is supported by numerical evidence only"；(2) 讨论 adversarial search 覆盖范围限制。

### Should-Fix（影响评分但不一票否决）

**W4. [共识] Theorem 2 的 symmetric C₀ 假设在实际 LLM 场景中很少成立。**
- 真实 LLM 混淆矩阵通常高度不对称
- 论文未报告 23 个经验矩阵中有多少满足或近似满足对称性
- **建议**：量化经验矩阵的对称性偏离程度（Frobenius distance to nearest symmetric matrix），讨论 Theorem 2 对轻微不对称的鲁棒性。

**W5. [共识] 线性 SEM 推广讨论不足。**
- 所有定理建立在线性 SEM 上。B.7 logistic 回归 sign-flip 率为零（积极），但 B.15 FWL breakdown 显示 logistic 下矩阵校正方法可能有效。
- **影响**：核心负结果（矩阵校正无效）在非线性模型下可能不适用，论文对此讨论不充分。
- **建议**：Limitations 增加线性→非线性推广讨论。

**W6. [共识] Non-differential misclassification 假设讨论应更前置。**
- B.25 Y-stratified 验证显示 content-dependent proxies 违反假设（12/12 rejections for topic）
- 主文仅 Limitations 一句带过
- **建议**：Section 3.1 增加 2-3 句讨论实践合理性和验证策略，引导读者到 B.5-B.6。

**W7. [R2] ASV 与 E-values 区分度论证不够锐利。**
- 两者都将"扰动强度"映射到"效果是否翻转"的阈值。Remark 1 称 "analogous to E-values" 但未深入解释增量价值。
- **建议**：增加 "Why not E-values?" 讨论，明确 ASV 回答的问题（标注误差强度阈值）与 E-values 回答的问题（未观测混淆强度阈值）的本质区别。

**W8. [R1] Algorithm 1 决策阈值缺乏理论依据。**
- 阈值来自特定模拟设置（K=3, Dirichlet, 7 topologies）的经验平均
- 未验证对不同 K、DGP 参数、样本量的稳定性
- **建议**：报告跨 K 性能，或明确定位为启发式指南而非普适算法。

**W9. [R2] "first multi-class topology-specific analysis" 声称需更精确界定。**
- Brenner (1993) 已有 polytomous confounder；Lee & Wood-Doughty (2024) 有 K≥3 confounding。
- **建议**：改为 "first systematic analysis that jointly addresses multi-class (K≥3) misclassification across multiple DAG topologies"。

---

## Reviewer Consensus [AGREE]

1. **评分一致**：两位 Reviewer 独立给出 3.5/5（Borderline Conference）。
2. **端到端验证缺失是核心短板**：对 EMNLP 应用导向 venue，声称 practitioner guidance 但无实际因果问题 demo 是显著弱点。
3. **Theorem/Conjecture 边界需更清晰**：K≥3 一般情况下 ASV 排序仅有数值支撑，主文语气应更谨慎。
4. **Non-differential 假设讨论应前置到主文**。
5. **理论贡献的条件（proportional effects, symmetric C₀, linear SEM）在实践中限制性强**，论文未充分告知读者。
6. **核心发现（sign reversal, FWL invariance, ASV ranking）有实际价值**，对 NLP 社区有警示意义。
7. **验证深度（MAPE 1.6%, 545,945 curves, 23 LLM configs）令人信服**。

## Reviewer Divergence [REBUT]

1. **端到端验证的严重程度**：R2 视为唯一 Must-Fix（critical）；R1 视为 Should-Fix（认为论文的理论贡献自身有价值，端到端 demo 是 nice-to-have）。
2. **Proportional effects 缺失**：R1 视为 Critical（核心假设未在 Limitations 中披露）；R2 未单独列出（在 W1 ASV 单调性下间接触及，但未升级为 critical）。

---

## Questions for Authors

Q1. Algorithm 1 假设 DAG topology 已知。当 topology 不确定时，是否考虑过在多个候选 DAG 上运行 ASV 并报告 sensitivity 范围？

Q2. MC-SIMEX 需要已知/估计的混淆矩阵，PPI++ 只需 gold labels。在 gold labels 昂贵时（如 K=10），两者的 trade-off 如何？

Q3. 非线性 DGP（logistic）下 bias magnitude 如何变化？线性 ASV 能否作为保守近似？

Q4. K=10 时混淆矩阵有 100 个参数。B.23 bootstrap 分析在 n_gold=500 时 ASV 排序稳定（Spearman ρ≥0.99），但对 K=10 是否也成立？

Q5. 23 个经验 LLM 混淆矩阵中有多少满足或近似满足 Theorem 2 的对称性条件？

---

## Missing References

未发现重大遗漏。Related Work 覆盖了 measurement error (Carroll 2006, Gustafson 2004)、binary misclassification (Brenner 1993, Bross 1954)、LLM annotation (Gilardi 2023, Ziems 2024, Baumann 2025)、sensitivity analysis (VanderWeele & Ding 2017, Cinelli 2020) 等主要方向。引用中未发现明显虚构或年份错误。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置未启用）。

---

## Visual Layout Check（非评分项）

状态：**已完成** (2026-05-23 18:34 → 18:39, ~5min)

主要发现：
- **[Warning]** 前两页纯文本（Title + Abstract + Introduction），无 display item。Figure 1 到第 3 页才出现。审稿人前 2 分钟只看到密集文字，无视觉锚点。建议将 Figure 1 提前到第 2 页。
- **[Warning]** 页 4-6 理论密度高但视觉节奏略显单调（3 页中仅 1 个 display item）。考虑到是理论核心区域，属可接受例外。
- **[Info]** 正文恰好 8 页，符合 EMNLP 2026 Long Paper 限制。
- **[Info]** 主文 4 个 display items (3 figures + 1 table) across 8 页 = 0.5/页。对理论+实证混合型论文偏低端但可接受。
- **[Info]** References 无 [?] 未解析引用，格式一致。
- 0 critical / 2 warning / 16 info。总体排版专业、格式合规。

---

## Overall Assessment

**评分：3.5 / 5 — Borderline Conference (介于 Conference 和 Findings 之间)**

**置信度：4 / 5**

**判断依据**：
- 理论贡献在限定条件下正确且有新颖性（sign reversal dichotomy, ASV framework, FWL invariance insight）
- 验证深度优秀（三层协同：analytic + MC + adversarial）
- 但核心定理的实际适用范围受 proportional effects + symmetric C₀ + linear SEM 三重限制，且 Limitations 未充分披露
- 对 EMNLP 应用导向 venue 而言，缺少端到端 NLP 因果应用 demo 是显著短板
- Conjecture 1 的理论缺口（K≥3 一般情况未证明）使 ASV 排序的理论保障不完整

**升级条件（→ 4.0 Conference）**：
1. 增加一个端到端因果应用 demo（即使简单）
2. Limitations 补充 proportional effects 假设讨论
3. 主文明确标注 Theorem/Conjecture 边界

**降级风险（→ 3.0 Findings）**：
- 如果 Reviewer 认为 proportional effects 下 OOB rate 84.6% 意味着定理在实践中基本无用
- 如果 EMNLP AC 倾向惩罚纯方法论贡献（无 NLP 应用 demo）

---

## Detailed Comments

### Section 1 (Introduction)
- "first multi-class (K≥3) topology-specific analysis" 需更精确限定（Brenner 1993, Lee & Wood-Doughty 2024 部分覆盖）
- 83.4% headline 后续有 realistic regime 数字（2.1%），叙事节奏合理

### Section 3.1 (Setup)
- Non-differential 假设的实践合理性讨论应从 Appendix 部分前置到此处
- Notation density 高（p.3-4 一页内引入大量符号），Table 26 出现太晚

### Section 3.2 (Bias Expressions + Theorems)
- Theorem 1/2 → Conjecture 1 的递进需更显式标注证明终点
- Proportional effects 假设需在定理引入时加 caveat
- Theorem 2 symmetric 假设的实际合理性需讨论

### Section 4.2 (Bias Taxonomy Results)
- "grand MAPE" 非标准术语，建议改为 "mean absolute percentage error averaged across"
- Dirichlet(1,1,1) 83.4% 是最坏情况，Figure 2 caption 建议注明 realistic-accuracy 对比

### Section 4.4 (Empirical Validation)
- 使用真实混淆矩阵但在模拟 DGP 上运行——最接近但仍非端到端验证
- F₁ disconnect 论证有力（Spearman ρ=-0.10, p=0.45）

### Section 4.5 (Correction)
- Algorithm 1 阈值为启发式，应明确标注
- FWL invariance 描述应加 "matrix-based" 修饰，避免误导

### Section 5 (Limitations)
- 缺 proportional effects（最关键遗漏）
- "experiments lack end-to-end causal benchmarks" 一笔带过，应展开
- 三个限制覆盖合适，但深度不足

### Format Compliance
- 正文 ≤ 8 页 ✅
- Abstract ≈ 190 words（边界合规）⚠️
- Limitations 存在且适当 ✅
- 匿名性 ✅（无 self-citation leak）
- 单一 Limitations section ✅
- AI 辅助声明 ✅（Section D, p.34）
