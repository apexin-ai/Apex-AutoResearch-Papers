---
round: 13
review_mode: fresh
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-24T01:28:49.883028+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Round 19 (Fresh Review)

**论文**: "When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects"
**Venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)
**截止日期**: 2026-05-25
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验完整性; R2: 新颖性+相关工作+写作质量)

---

## Summary

本文研究 LLM 注释在异质性处理效应（HTE）分析中的测量误差问题。当 LLM 分类器的误差率在亚组间存在异质性时，标准全局混淆矩阵校正会引入亚组级偏差，甚至反转 CATE 估计符号。论文提出三项贡献：(1) Theorem 1——精确偏差分解恒等式 δ_s·Δτ/(1−2π̄)；(2) Proposition 5——仅需亚组误差率的 Δτ-free 诊断准则；(3) EC-HTE——基于层次贝叶斯混淆矩阵估计的亚组校正方法。实验涵盖 520 个合成配置、11 个真实 LLM 错误分布、三种下游估计器。

---

## Strengths

1. **问题定位精准且时机恰当**：Effect modifier misclassification 是 PPI/DSL 框架未覆盖的真实 gap，LLM 注释用于因果推断正快速普及，sign-reversal 发现对实践有直接警示价值。[R1, R2 一致]

2. **理论结果干净且可解释**：Theorem 1 的 product form (δ_s·Δτ/(1−2π̄)) 将全局校正偏差分解为三个独立可估计分量，直接导出诊断准则和校正方案。与 Frazis-Loewenstein (2003) 的 scalar attenuation 有明确区分——刻画 correction-induced bias 而非 attenuation。[R1: "优雅且新颖"; R2: "干净且可解释"]

3. **证明完整且可验证**：Appendix B 的矩阵代数推导对 2×2 对称混淆矩阵可手动验证。Proposition 3 (A5 relaxation) 和 Corollary 4 (aggregate bias = Cov_w) 是自然推广。[R1]

4. **实验覆盖面极其全面**：520 个合成配置验证恒等式 R²≥0.97；8 个 LLM × 2 数据集；三个下游估计器（DIM, CausalForest, R-learner）；22 页附录覆盖几乎所有假设违反情形。[R1, R2 一致: "同类论文中罕见"]

5. **方法定位诚实**：论文承认 EC-HTE 基于 Dawid-Skene 架构，展示与 PPI/DSL 的互补性而非竞争关系，在 hate speech 数据上 EC-HTE 表现不佳时如实报告。[R2]

6. **诊断准则具有独立实用价值**：Proposition 5 的 Δτ-free 特性使实践者可仅通过亚组误差率判断是否需要分层校正。[R1, R2 一致]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, 共识] **Abstract "14.9% sign reversal" 省略关键条件 τ(0)=0.03**
- Abstract 称 "global correction reverses CATE sign in 14.9% of configurations"，但这仅在 τ(0)=0.03 条件下成立
- τ(0)=0.01 时升至 31%，τ(0)≥0.089 时降至 0%（Appendix Z.8）
- 论文最有影响力的数字之一，不透明的条件限定构成结果呈现的误导
- **修改方向**：Abstract 加 "under small baseline effects (τ(0) < 0.09)" 或 "at τ(0) = 0.03"
- *R1 列为 Must-Fix，R2 完全同意*

**MF2** [critical, 共识] **所有"真实数据验证"因果效应均为合成注入，但 framing 不透明**
- TweetEval/Civil Comments 的 CATE 均为合成注入（τ(z) = τ + Δτ·z）
- "11 real LLM-dataset combinations" 的措辞暗示真实因果验证，实质是 semi-synthetic
- Limitations 提及此局限但正文和 Abstract 的 framing 对不仔细阅读的读者具有误导性
- **修改方向**：改为 "semi-synthetic evaluations with empirical LLM confusion matrices"；Section 5 明确标注所有 CATE 为合成注入
- *R1 列为 Must-Fix，R2 完全同意（与 R2-W3 一致）*

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, 共识] **Theorem 1 的 novelty 定位需更精确**
- 偏差恒等式在数学上是标准混淆矩阵代数的直接推导（Fuller 1987, Carroll et al. 2006）
- 真正的新颖性在于：(a) effect modifier misclassification 的 setting identification；(b) product form 使诊断成为可能；(c) sign-reversal 的识别与量化
- **修改方向**：Contribution 1 明确 "algebraic structure follows from standard confusion-matrix calculus; our contribution is identifying that this structure produces sign reversal in the LLM annotation setting"
- *R2 列为 Must-Fix，R1 同意但认为应降级为 Should-Fix——见 Divergence D1*

**SF2** [warning, 共识] **A1 假设敏感性分析对 NLP 场景不够充分**
- A1（误分类独立于潜在结局 | Z, S）不可检验，但在 LLM 注释中很可能被违反
- Treatment-dependent misclassification 在 γ_T=0.10 时 coverage 降至 75%，breakeven 偏低
- Outcome-correlated misclassification（LLM 准确率与文本复杂度/情感极性相关）未被检验
- **修改方向**：正文加 1-2 句关于 A1 违反的定量描述；讨论 NLP 中的具体违反模式
- *R1-W1, R2-W4 一致*

**SF3** [warning, 共识] **诊断 AUC=0.63 削弱"actionable"定位**
- 全部亚组 AUC=0.63 仅略高于随机（0.5），实践者事前不知 Δτ 是否为零
- 多版本 AUC (0.63, 0.86, 1.0) 选择性呈现有 cherry-picking 嫌疑
- 论文解释逻辑合理（Δτ≈0 时误判无代价），但正文未充分阐述
- **修改方向**：Section 5.4 前置讨论为什么未筛选 AUC 较低；Abstract 使用最保守值或标注完整条件
- *R1-W2, R2-W2 一致*

**SF4** [warning, 共识] **适用条件窄（Δπ>0.15, K≤4）且真实数据常不满足**
- 真实 LLM 数据 Δπ∈[0.10, 0.20]，常低于 0.15 阈值
- Hate speech 数据上 EC-HTE 表现逊于 Naive 和 Global
- 正文 Section 5.4 列出 operating conditions 但 Conclusion/Abstract 未充分反映
- **修改方向**：Conclusion 或 Abstract 明确限定适用范围
- *R1-W4, R2-W5(K), R18-SF5 一致*

**SF5** [warning] **"7.4× bias reduction" 比较基准选择有倾向性**
- 用已被证明有害的 Global (0.059) 作基准；与 Strat. MLE (0.012) 比较仅 1.5×
- R2 部分反驳：Global 是 PPI/DSL 默认做法，作为比较有实践合理性
- **修改方向**：同时报告与 Naive 和 Strat. MLE 的比较
- *R1 列为 Should-Fix，R2 认为有实践合理性但同意折中——见 Divergence D2*

**SF6** [warning, 共识] **有限样本余项 R_n = O_p(n^{-1/2}·κ) 缺乏形式化证明**
- 论文以一句话断言收敛率，对"exact identity"定位的论文过于随意
- 经验验证（R̂<1.01, ESS>1618）部分弥补但不替代形式化推导
- **修改方向**：Appendix B 补充 sketch proof（基于矩阵摄动理论）或引用 Stewart & Sun (1990)
- *R1-W6, R2 同意*

### Minor（不影响接收）

- **M1**: Figure 2 热力图打印尺寸下颜色区分度不足 [R2]
- **M2**: Abstract 需确认 ≤200 words [R2]
- **M3**: CausalForest coverage=0.90 低于名义水平，主表应交叉引用 bootstrap 结果 [R1]
- **M4**: Contribution list 信息密度过高，应精简为定性描述 [R2]
- **M5**: Table 1 中 Naive bias 0.058 vs Global 0.059 的比较基准区分不清 [R1]
- **M6**: AI assistant 使用声明（page 30）应确认符合 ACL 2026 披露要求 [R1, R2]
- **M7**: Gamma(α₀, β₀) 超参数敏感性分析应在正文至少提及 [R2]

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键判断上完全一致：

1. **Overall 3.5 (Borderline Conference)** — 一致同意
2. **Theorem 1 是论文核心优势** — R1 称"优雅且新颖"，R2 称"干净且可解释"
3. **Abstract/framing 需要更谨慎的条件限定** — 14.9% sign reversal 省略 τ(0) 条件（MF1），"real data" 实为 semi-synthetic（MF2）
4. **A1 假设讨论不足** — 敏感性分析深度不够，NLP 中的具体违反模式未讨论（SF2）
5. **诊断 AUC=0.63 在实践中判别力有限** — 需更透明的讨论（SF3）
6. **适用条件窄** — 真实 LLM 数据常不满足 Δπ>0.15（SF4）
7. **实验覆盖面是主要加分项** — 22 页附录覆盖几乎所有假设违反情形
8. **论文适合 Findings** — 高质量执行但 novelty 有限

---

## Reviewer Divergence [REBUT]

**D1: Theorem 1 novelty 的严重程度**
- **R2**: Must-Fix — 标准矩阵代数在新场景的应用，数学新颖性不足以支撑 main conference
- **R1**: Should-Fix — 同意数学技术标准，但 setting identification（effect modifier misclassification）和 product form 的诊断价值有独立贡献；与 Frazis-Loewenstein 的区分（correction-induced bias vs attenuation）是结构性的
- **Director 判断**: 降级为 **Should-Fix**。论文的新颖性确实不在数学推导本身，但 (a) effect modifier misclassification 确属文献 gap，(b) sign-reversal 的识别和量化对实践有直接价值，(c) 完整的恒等式→诊断→校正链条在 CSS/causal-NLP 交叉领域少见。修改 Contribution 1 措辞即可，不需重构。

**D2: EC-HTE 方法论贡献**
- **R2**: Must-Fix — per-subgroup Dawid-Skene + CausalForest 的工程组合，方法论创新不足
- **R1**: 不同意 — EC-HTE 的价值在 pipeline 集成（κ-guard, uncertainty propagation, partial pooling），且论文 contribution profile 不依赖 EC-HTE 的方法论新颖性——恒等式+诊断已足够
- **Director 判断**: R1 论点更有说服力。论文 Contribution 3 的措辞可优化（重新定位为"reference implementation + empirical validation"），但这不构成接收障碍。**降级为 Minor 建议**。

**D3: "7.4× bias reduction" 的比较基准**
- **R1**: Should-Fix — Global 已被证明有害，用它作基准夸大效果
- **R2**: 部分反驳 — Global 是 PPI/DSL 默认做法，与默认实践比较有合理性
- **Director 判断**: **保留为 Should-Fix** 但降低优先级。两种比较各有合理性，折中方案（同时报告与 Global 和 Strat. MLE 的比较）成本低、收益高。

**D4: 校准方法 baseline**
- **R1**: Should-Fix — 缺少 Platt/Temperature scaling 作为 baseline
- **R2**: 反驳 — Appendix Z.7 已系统评估校准的作用（Calibrated+EC-HTE=96.5% coverage），处理方式恰当
- **Director 判断**: R2 反驳有效。Appendix Z.7 的覆盖面充分，**降级为 Minor 建议**（将关键结果在正文简要提及即可）。

**D5: K 限制的讨论充分性**
- **R2**: Should-Fix — K=2 限制未充分讨论，实际 NLP 应用中亚组数量远大于 2
- **R1**: 反驳 — 论文已覆盖 K=2,4,8 且明确声明 K≤4 限制；demographic HTE 中 K=2-4 是主流
- **Director 判断**: R1 反驳合理，论文对 K 的讨论已基本充分。**合并入 SF4（适用条件窄）**，不单独列出。

---

## Questions to Authors

1. 能否提供一个真实 NLP 因果问题的案例，其中四个操作条件（Δπ>0.15, K≤4, FNR<0.5, 足够 expert budget）同时满足？[R1-Q2]
2. 当子群是数据驱动（如文本嵌入聚类）而非预定义时，EC-HTE 如何表现？Theorem 1 的 product form 是否仍然适用？[R1-Q1]
3. 诊断 AUC=0.63 在实际场景中的误判（预测"有害"但实际无害，或反之）导致的 excess RMSE 是多少？[R2 交叉回应]
4. 是否考虑过 non-parametric 的混淆矩阵估计方法（如基于 calibration 而非 Dawid-Skene 的方法）？[R2-Q4]
5. EC-HTE 的端到端 wall-clock 时间是多少？Gibbs 采样在 K>4 时是否成为瓶颈？[R1-Q3]

---

## Missing References

两位 Reviewer 均认为引用覆盖面良好。以下为建议补充的潜在遗漏（均非核心遗漏）：

1. **Blette et al. (2024)** — "Assessing treatment effect heterogeneity in the presence of missing effect modifier data" (Statistical Methods in Medical Research)，直接研究 effect modifier 误测下的 HTE 估计 [R2, R2 交叉回应]
2. **SIMEX (Cook & Stefanski 1994)** — 经典替代测量误差校正方法，与混淆矩阵逆方法形成互补 [R1]
3. **Active PPI (2025-2026)** — 预测器选择和预算分配，与 EC-HTE 的 expert budget 讨论相关 [R2]

---

## External Review (Stanford Agentic Reviewer)

**状态**: pending（已请求，尚未返回）

外部审稿已于 2026-05-24T01:04 发出请求，截至报告投递时未收到结果。8 小时后将自动提醒用户跟进。

---

## Visual Layout Check（非评分项）

**状态**: done (3 warnings, 0 critical, 15 info)

关键发现：
- ⚠️ **Pages 1-2 无 display item**：连续两页纯文本（Title/Abstract/Introduction/Related Work 开头），缺乏视觉锚点。Figure 1 直到第 3 页才出现——尚在可接受范围。
- ⚠️ **Pages 4-7 跨 4 页无 figure/table**：从 Figure 1（page 3）到 Table 1（page 8）之间无 display item。Pages 4-5 有 displayed equations 部分弥补，但 pages 6-7 纯文本方法描述可能使审稿人失去注意力。
- ⚠️ **Table 1 出现在第 8 页（最后一页）**：核心实验数据在最后一页才出现，理想应在 page 6-7。
- ✅ 主正文 8 页，符合页数限制。Limitations 简短（约半栏），位置正确。
- ✅ 无 margin 溢出、无未解析引用 [?]、排版质量专业。
- ✅ Figure 1 三面板清晰，颜色方案色盲友好。Table 1 使用 booktabs 风格，格式规范。
- ℹ️ 主正文仅 2 个 display items（Figure 1 + Table 1），密度偏低，大量结果在附录中。

---

## Overall Assessment

**Overall: 3.5 / 5 (Borderline Conference)**

**Soundness**: 3.75/5 (R1: 3.5, R2: 4)
**Excitement**: 3.5/5 (R1: 3.5, R2: 3.5)
**Confidence**: 4/5

### 评分理由

**加分项**：
- 问题定位精准，effect modifier misclassification 是真实且未被覆盖的 gap
- Theorem 1 的 product form 优雅可解释，恒等式→诊断→校正的理论链条完整
- 实验覆盖面在同类论文中罕见（22 页附录，几乎所有假设违反情形）
- 方法定位诚实，不回避自身局限性

**降分项**：
- **Framing 高估实际证据强度**（2 个 Must-Fix）：Abstract 省略关键条件限定、"real data" 实为 semi-synthetic
- **数学新颖性有限**：Theorem 1 是标准技术在新 setting 的应用，EC-HTE 是现有方法的组合
- **理论优雅性与实际实用性落差**：适用条件（Δπ>0.15, K≤4）在真实 LLM 数据中常不满足；诊断在真实数据上 AUC 仅 0.63

### 修订后上调条件

如果以下问题在修订中解决，可上调至 **4.0 (Conference)**：
1. 收紧 Abstract 和 Section 5 的 framing：诚实标注 semi-synthetic 性质 + 14.9% 的条件限定
2. 修改 Contribution 1 和 3 的 novelty 定位：强调 setting identification 而非数学推导本身
3. 正文加 A1 违反的定量讨论（γ_T=0.10 breakeven）
4. 7.4× 同时报告与 Naive 和 Strat. MLE 的比较

### Findings 适配性

作为 Findings 论文非常合适（score 3.0-3.5）：clean applied theory + exhaustive experiments + practical diagnostics 的贡献模式符合 Findings 的定位。是否达到 main conference 取决于审稿委员会对 "setting identification + thorough validation" 这一贡献类型的评价。

---

## Detailed Comments

### Section 1 (Introduction)
- 开篇 scenario 有效但可更具体——"consider estimating whether a content moderation policy reduces hate speech" 应标注这是合成示例还是真实案例
- Footnote 1 对 "debiasing" 的消歧放置位置恰当，但标题 "When Debiasing Hurts" 在 NLP fairness 语境下仍可能误导
- Contribution list 3 个 bullet points 信息密度过高，混入了 R² 值、配置数量、AUC 值等定量细节——建议精简为定性描述

### Section 3 (Theory)
- Theorem 1 证明正确且完整，Appendix B 的矩阵代数可手动验证
- 5 个假设 (A1)-(A5) 列举清晰；Proposition 3 (A5 relaxation) 和 Corollary 4 (aggregate bias) 是自然推广
- Remark 1 指出 A2 对乘积结构非必需是重要的理论卫生，但与 Theorem 1 假设列表包含 (A2) 存在表面矛盾——措辞可更精确
- 有限样本余项段落（theory.tex line 100-102）过于简略，需要形式化支撑

### Section 4 (Method)
- HB 模型规格完整（Dirichlet-Multinomial + empirical Bayes），MCMC 收敛诊断充分
- κ>100 singularity guard 的动机清晰（π_s > 0.495 = near-random），Appendix R 的 sweep 验证充分
- Section 4.3 Variance-Adjusted CausalForest 的 SE 传播是 plug-in 方法，条件性忽略 CM 估计不确定性——论文自己承认这一局限性
- "21 of 24 configurations" (method.tex line 18) 缺乏上下文

### Section 5 (Experiments)
- 合成 DGP 设计合理（K∈{2,4}, controlled Δπ and Δτ），520 配置覆盖关键 regime
- Baselines 充分（Naive, Global, Strat. MLE, F-L, PPCI, EC-HTE+PPCI）
- CausalForest 和 R-learner 一致验证偏差来自混淆矩阵结构
- Operating conditions (Δπ>0.15, n_expert≥250, FNR<0.5, K≤4) 列出但分散——建议集中讨论
- Hate speech case study 诚实报告 EC-HTE 表现不佳，但应更突出这一负面结果的含义

### Abstract
- 需确认 ≤200 words（EMNLP 2026 要求）
- "14.9% of configurations" 必须加 τ(0) 条件限定
- "11 real LLM-dataset combinations" 必须改为 semi-synthetic 表述
- AUC 多版本呈现需要更清晰的条件说明

### Limitations
- 简短（约半栏），覆盖了关键限制（expert budget、A1、离散亚组、合成 CATE）
- 可增加：数据驱动子群的限制、A1 在 NLP 中的具体违反模式
