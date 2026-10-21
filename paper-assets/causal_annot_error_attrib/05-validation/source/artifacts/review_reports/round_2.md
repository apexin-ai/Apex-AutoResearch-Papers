---
round: 2
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T11:00:08.998625+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 2 (Fresh Review)

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**目标 Venue**: EMNLP 2026 (via ARR May 2026 cycle)
**截止日期**: 2026-05-25
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验验证; R2: 新颖性+相关工作+写作质量）
**审稿模式**: Fresh（初审）
**交叉轮次**: 1 轮（Round 1 独立审稿 → 交叉分享 → 收敛，未进入 Round 2）

---

## Summary

本文系统研究了 K-class LLM 标注误差在 7 种因果 DAG 拓扑下的偏差传播。核心发现：(1) K≥3 时 exposure 和 IV 拓扑可产生符号翻转（83.4% under Dirichlet prior; 2.1% under realistic accuracy），而 5 种拓扑维持符号保持性（2 种已证明，3 种经验验证）；(2) ASV 灵敏度框架揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑依赖脆弱性谱；(3) FWL 不变性导致矩阵校正方法对 4 种拓扑完全无效。论文建立了有用的分类法，但核心理论结果部分依赖数值验证而非完整解析证明。

---

## Strengths

**S1. 选题及时且填补明确研究空白**
LLM 标注在计算社会科学中快速普及，但多分类标注误差在因果推断中的系统性传播此前缺乏跨拓扑研究。先前工作（Lee & Wood-Doughty 2024）仅覆盖 confounding 单一拓扑，本文扩展到 7 种拓扑的统一框架，是实质性进步。[R1, R2 共识]

**S2. K≥3 符号翻转发现具有理论和实践价值**
K=2 → K≥3 的定性断裂（符号翻转在二分类中不可能但在多分类中成为结构性风险）是非显而易见的理论发现。Appendix A.5 的反例构造严格且具教育意义，直接指导实践者不应将多分类标签简单二值化。[R1, R2 共识]

**S3. FWL invariance 洞察新颖且可操作**
证明 4 种拓扑下矩阵校正方法（Naive plug-in, MLA）因 FWL 不变性而恰好 0% 偏差缩减——这是结构性结果（非数值近似），为校正方法选择提供了明确的负面指导。Section 4.6 的 210 配置系统评估有较高实践价值。[R1, R2 共识]

**S4. 理论-经验层级区分诚实**
论文清晰标注 Proposition（已证）、Empirical Finding（数值验证）、Conjecture（猜想），这种分层在同类论文中较少见。[R1 首发, R2 同意]

**S5. 解析推导与 MC 验证高度一致**
Grand MAPE 2.0%（126 scenarios），per-topology range 0.5%-5.5%，理论预测与实验验证吻合度高。[R1, R2 共识]

**S6. ASV 框架设计合理**
三种互补灵敏度度量（magnitude, significance, sign-flip）类比 E-value 设计思路，为研究者提供简洁的"标注误差预算"工具。δ_max 约束的引入确保了参数化的有效性。[R1, R2 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [CRITICAL] Theorem 1 一般情形证明不完整** [R1-N1, R2-N1 共识]
- Theorem 1 声称 confounding 拓扑下 |B(C(δ))| 对 δ 单调非递减。比例情形 (f=λg) 有完整代数推导（Appendix A.4），但一般情形使用 Cauchy-Schwarz 界后以 "Tightness is confirmed numerically (500 random (C₀, δ) pairs, zero violations)" 收尾。
- **核心问题**：Cauchy-Schwarz 仅证明上界 B̄(δ) 的单调性，不能推出 |B(C(δ))| 本身的单调性。R2 举例：f(δ)=sin(δ) 被 g(δ)=δ 界住，g 单调但 f 不单调。
- **影响**：ASV 框架的 δ* 唯一性和解释性直接依赖该单调性。论文将唯一标记为 "Theorem" 的结果在一般情形下依赖数值验证，模糊了 theorem 和 conjecture 的界限。
- **建议**：一般情形降级为 "Theorem (proportional case) + Empirical Finding (general case)"，明确讨论 ASV 在单调性仅为经验验证时的可靠性。

**MF2. [MAJOR] 3/5 "安全"拓扑的符号保持缺乏解析证明** [R1-N2, R2-N1 共识]
- Mediation、M-bias、front-door 的符号保持仅通过 100,000 随机列随机矩阵数值验证，论文明确承认 "analytic proofs for general K remain open"。
- Abstract 使用 "five topologies never produce sign reversal"，"never" 是全称量词，与 Empirical Finding 的认识论地位不匹配。
- **建议**：Abstract 修改为 "five topologies show no sign reversal across extensive numerical verification (proven analytically for confounding and collider)"；正文讨论解析证明的困难所在。

**MF3. [MAJOR] Non-differential misclassification stress test 覆盖不足** [R1 首发, R2 同意(nuance)]
- Stress test（Appendix B.3, Table 6）仅覆盖 exposure 拓扑、K=3、ε ∈ {0.00, 0.01, 0.05, 0.10}。
- LLM 标注误差在实践中几乎必然是 differential 的（不同类别的分类能力系统性不同，可能与结果变量相关）。
- R2 补充：论文 Limitations 提到 "outcome-conditional prompting" 可破坏该假设，但讨论不够深入。
- **缓解因素**（R2）：non-differential 是测量误差文献标准假设（Carroll 2006），Table 6 显示 ε≤0.10 下 sign-flip 仅从 2.0% 升至 4.5%，表明小偏离下稳健。
- **建议**：扩展至 confounding/mediation 拓扑 + K=10 HumAID 设置；从实际数据估计 LLM 误差的 differential 程度。

### Should-Fix（影响评分但不一票否决）

**SF1. [MAJOR] 线性 SEM 假设限制对 NLP 受众的实用性** [R1-W5, R2-W1 共识]
- 所有理论结果基于线性结构方程。NLP 中 logistic regression、非参数方法广泛使用。
- Limitations 仅一句 "FWL invariance result does not hold for logistic regression"，未讨论线性假设的适用边界或非线性下核心发现是否定性保持。
- **建议**：至少添加一个 K=3 logistic DGP 模拟验证 sign-flip 现象是否定性保持。

**SF2. [MAJOR] 缺少 2 篇高度相关引用** [R2 首发, R1 同意]
- **Feder et al. (2022) TACL**："Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond"——NLP+因果推断领域引用量最高的综述（400+ 引用），投 EMNLP 必引。
- **Cheng, Mayya & Sedoc (2024)**："To Err Is Human; To Annotate, SILICON?"——将 LLM 标注误差分解为四种上游来源，与本文下游传播分析互补。（注：此文已在 references.bib 中但未在正文 \cite。）
- **建议**：Related Work 补充引用并明确区分。

**SF3. [MAJOR] ASV 参数化选择缺乏讨论和敏感性分析** [R1-W2, R2-W3 共识]
- C(δ) = (1-δ)I + δC₀ 的线性插值是一个特定参数化选择，替代方案（对角线衰减、精度参数化）未讨论。
- 论文 Section 3.3 提到 "we recommend bootstrapping C₀"，但未展示实际 bootstrap 结果。
- **建议**：讨论参数化选择理由；展示至少一个 C₀ bootstrap 示例分析 δ* 置信区间。

**SF4. [WARNING] 实证验证不完整** [R1-W3, R2-W4 共识]
- 仅完成 14/38 计划配置（36.8%），VAST (K=3) 和 CivilComments (K=2) 覆盖不足。
- 4 个 LLM 均为开源模型，无商业模型（GPT-4, Claude）对比。
- **建议**：补完缺失配置；讨论开源 vs 商业 LLM 误差模式差异。

**SF5. [WARNING] Conjecture 1 数值验证样本量不足** [R1-W4, R2-N1 共识]
- 每拓扑仅 500 scenarios 验证 ASV envelope 单调性，而 Empirical Finding 1 用了 100,000 个矩阵。200 倍差异缺乏解释。
- Conjecture 1 是 ASV 框架的理论基础，重要性不亚于 Empirical Finding 1。
- **建议**：增加到至少 10,000 scenarios per topology。

**SF6. [WARNING] DGP 条件在实践中难以事前验证** [R1-W1, R2-W5 共识]
- Proposition 1 的充分条件（如 sign(τ) = sign(τ + B_OV)）涉及未知 DGP 参数，实践者无法事前判断。
- 论文通过 ASV 部分缓解，但 ASV 本身依赖 Conjecture 1。
- **建议**：讨论基于数据的诊断方法或典型参数范围下的满足率。

### Minor（不影响接收）

- Abstract "five topologies never" 措辞需与正文 Empirical Finding 对齐
- Section 3.4 Binarization Collapse 仅 4 行，信息密度低，建议移至附录或扩充
- Table 1 混排两种先验条件下的结果，建议分行标注
- 多套符号系统（τ, τ̂, f(A*), β）快速阅读时易混淆，建议增加符号表
- Appendix B.1 Applied Illustration（ClinicalBERT Case Study）有价值，建议主文增加交叉引用

---

## Reviewer Consensus

以下问题双方完全一致（[AGREE]）：

| # | 问题 | 严重程度 |
|---|------|---------|
| 1 | 核心理论结果（Theorem 1 一般情形、Empirical Finding 1、Conjecture 1）依赖数值验证 | Must-Fix |
| 2 | 3/5 安全拓扑符号保持缺乏解析证明 + Abstract 措辞不匹配 | Must-Fix |
| 3 | 线性 SEM 假设限制 NLP 实用性 | Should-Fix |
| 4 | ASV 参数化限制 + C₀ 不确定性未展示 | Should-Fix |
| 5 | 实验不完整（14/38 配置，无商业 LLM） | Should-Fix |
| 6 | DGP 条件实践可验证性 | Should-Fix |
| 7 | Conjecture 1 验证量（500 vs 100,000）不足 | Should-Fix |

---

## Reviewer Divergence

**唯一分歧：83.4% framing 的严重程度**

- **R2 立场 [CRITICAL]**：83.4% 基于 Dirichlet(1,1,1)（平均精度 ~0.33），realistic accuracy 下仅 2.1%。以极端场景数字为 headline 构成 sensationalization，影响论文诚实性信任。
- **R1 反驳 [REBUT → WARNING]**：(1) 论文 Abstract 已同时报告两组数字，条件透明；(2) Dirichlet(1,1,1) 作为参数空间均匀采样有方法论正当性——刻画结构性风险而非估计实际频率；(3) 83.4% 证明符号翻转不是稀有角落情形。
- **R2 未反驳 R1 的 REBUT**。
- **Director 裁定**：降级为 Should-Fix。论文事实准确、条件透明，但建议调整叙事重心——以 realistic accuracy 为主叙事。

---

## Questions for Authors

**Q1** (R1, R2 共识): Theorem 1 一般情形能否补全解析证明？若不能，是否考虑将一般情形降级为 Empirical Finding？

**Q2** (R1, R2 共识): Conjecture 1 是否做过 adversarial search（专门寻找反例的优化搜索）？当前 500 scenarios 的搜索策略是什么？

**Q3** (R2 首发, R1 同意): 在 logistic regression 下，sign-flip 现象是否定性保持？即使不提供完整理论，一个 K=3 × 3 topologies 的模拟也能大幅增强实用性。

**Q4** (R2): ASV 的 C₀ 估计来自有限验证集。如果 C₀ 对角线估计误差为 ±0.05，ASV 的 safe/unsafe 判断是否会翻转？

**Q5** (R1): 能否从 3 个实证数据集直接估计 LLM 混淆矩阵的 differential 程度（如按 Y 值分层计算 C 差异）？

---

## Missing References

1. **Feder, A., Keith, K.A., Manzoor, E., et al. (2022). "Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond." TACL.** — NLP+因果推断领域最重要综述，400+ 引用，投 EMNLP 必引。[R2 首发, R1 同意]

2. **Cheng, X., Mayya, R., & Sedoc, J. (2024). "To Err Is Human; To Annotate, SILICON?" arXiv:2412.14461.** — LLM 标注误差上游来源分解，与本文下游传播分析互补。已在 references.bib 中但未在正文引用。[R2 首发, R1 条件性同意]

---

## External Review (Stanford Agentic Reviewer)

**状态**：已跳过（用户未提交外部审稿）。

---

## Visual Layout Check（非评分项）

**状态**：已完成（5 warnings, 9 info, 0 critical）

### Warnings

1. **前 5 页无任何 figure/table**：审稿人翻过 5 页纯文字+公式后才看到第一个 display item（Figure 1, p6）。建议将 Figure 3（DAG 拓扑图，当前在 p18 附录）前移至 p2-3。
2. **主文 display item 密度低**：8 页正文仅 3 个 display items（Figure 1, Table 1, Figure 2），大量关键结果图表在附录。
3. **Figure 3 远离引用位置**：主文 p3 引用 "Figure 3" 展示 7 种 DAG 拓扑，但 Figure 3 在 p18，需翻 15 页。
4. **p7 纯文本整页**：Empirical Validation 讨论，夹在 p6（Figure 1 + Table 1）和 p8（Figure 2）之间，视觉节奏断裂。
5. **p20 约 40% 空白**：Figure 7 + Table 6 布局空间利用不足。

### Info（参考）
- Figure 1 子面板字体偏小（正文字号 65-70%）
- Figure 2 线条颜色在灰度打印下区分度可能不足
- p19 三张图挤在同一页，部分标签难以辨认
- Figure 1 色板可能对色盲用户不友好（红/绿），建议 Okabe-Ito 色板
- 格式合规：匿名处理正确，booktabs 三线表规范，References 格式统一

---

## Overall Assessment

**评分**: 3.5/5 — Borderline Conference

**置信度**: 4/5（双方 Reviewer 均仔细检查了证明结构和实验设计）

**评估理由**:

论文填补了 LLM 多分类标注误差 × 因果 DAG 拓扑的明确研究空白，K≥3 符号翻转发现和 FWL invariance 洞察具有理论与实践双重价值。框架设计系统，理论-经验层级区分诚实。

但存在两个阻碍明确接收推荐的结构性问题：
1. **理论完整性缺口**：唯一标记为 Theorem 的结果在一般情形下依赖数值验证；3/5 "安全"拓扑的符号保持仅有经验证据；ASV 框架依赖的 Conjecture 1 仅 500 scenarios 验证。这些问题影响论文的核心理论贡献可信度。
2. **实用性边界模糊**：线性 SEM 假设未充分讨论对 NLP 场景的适用性；non-differential misclassification stress test 覆盖不足；实验完成率仅 36.8%。

**接收条件**：若以下修改可在 camera-ready 阶段完成，论文有望达到主会议水平：
- MF1: Theorem 1 一般情形降级为 Empirical Finding 或补完证明
- MF2: Abstract/正文措辞与证明状态对齐
- MF3: Stress test 扩展至 2+ 拓扑和 K=10
- SF1-SF6: 至少解决线性假设讨论和缺失引用

**当前论文质量高于 Findings 门槛（3.0），处于 Borderline Conference 区间（3.5）。**

---

## Detailed Comments

### Section 1 (Introduction)
- "83.4% of confusion matrices cause sign reversal" 作为 headline 在技术上准确（Dirichlet(1,1,1) prior），但叙事效果倾向于 sensationalization。建议将 "under realistic classifier accuracy (diagonal ≥ 0.7), the violation rate is 13.7% with 2.1% sign reversal" 提升到与 83.4% 同等显著位置。
- 三项贡献的表述清晰，层次分明。

### Section 2 (Related Work)
- 三段式结构（measurement error / text classifiers / sensitivity analysis）覆盖面广。
- 缺少 Feder et al. (2022) TACL 综述——NLP+因果推断领域的 canonical reference。
- Cheng et al. (2024) 已在 .bib 中但未引用。

### Section 3 (Method)
- **3.1 Setup**: 清晰简洁。Non-differential misclassification 定义明确。
- **3.2 Bias Expressions**: 7 种拓扑的偏差表达式推导是论文的核心技术贡献。Proposition 1 的分层处理（proved / empirical finding / counterexample）是正确做法，但 Abstract 未反映此层级。
- **3.3 ASV**: 三种度量设计合理。δ_max 约束已引入。C₀ bootstrap 建议已提出但未实际展示。
- **3.4 Binarization Collapse**: 仅 4 行，信息密度低。

### Section 4 (Experiments)
- **4.1-4.2**: 理论-MC 一致性验证充分（MAPE 2.0%）。
- **4.3-4.4**: ASV 验证和 binarization collapse 分析有价值。
- **4.5 Empirical Validation**: 核心实证部分。3 tasks × 4 LLMs 设计合理但完成率低（14/38）。"F1 does not predict downstream bias" 发现（Figure 2）有实用价值。
- **4.6 Correction Guidance**: 210 配置系统评估，FWL invariance 的实证确认（exactly 0.0%）有力。

### Section 5 (Conclusion)
- 简洁准确，未过度声称。

### Limitations
- 覆盖面合理（non-differential 假设、线性假设、实验不完整），但每项讨论偏简略。
- 缺少线性假设适用边界的讨论。

### Appendix
- Appendix A（证明）是论文的技术核心。比例情形证明完整严谨；一般情形的数值验证不足（500 scenarios）。
- Appendix B.1（ClinicalBERT Case Study）展示框架实用性，建议主文交叉引用。
- Appendix B.3（Stress Test）覆盖面过窄。