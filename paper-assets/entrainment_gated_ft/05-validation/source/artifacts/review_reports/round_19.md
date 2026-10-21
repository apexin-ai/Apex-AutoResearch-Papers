---
round: 19
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T13:40:35.916191+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 19 (Fresh Review)

**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewers**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + Related Work）
**模式**: 圆桌审稿，1 轮独立审稿 + 交叉分享，达成共识无需进入 Round 2

---

## Summary

本文利用 Wang et al. (2025) 的 controlled model zoo（3 种 hybrid linear recurrent 架构 × 5 种 attention ratio × 2 种规模），首次系统分析了 hybrid recurrent architectures 之间的 per-example predictive multiplicity。核心发现：(1) 聚合指标可互换的架构在逐样本层面差异显著（pairwise Jaccard ≈ 0.10）；(2) per-example Jaccard 在 4% attention 时即饱和并保持平坦；(3) confidence-based routing 在高 multiplicity 任务上可部分利用互补性（LAMBADA +5.2pp，但 PIQA 显著为负）。

---

## Strengths

**S1. 实验控制度极高** [R1-S5, R2-S1]：基于公开 model zoo，所有模型共享训练数据、tokenizer、超参，仅变化架构和 attention 配置。这种控制在 hybrid architecture 文献中罕见。

**S2. 统计诚实度优秀** [R1-S3, R2-S2]：始终对 LAMBADA 的 aggregate trend 标记为 "non-significant"（Bonferroni 校正后 p=.170），在 Table 1 脚注明确 n=5 功效限制。这在 NLP 实证论文中属上乘。

**S3. Robustness 验证极为充分** [R1-S4, R2-S3]：13 个 Appendix（A–X）系统检查了 GDN confound exclusion、continuous Jaccard、5 架构扩展、seed calibration、confidence margin cross-benchmark 等。

**S4. Per-example Jaccard 饱和是稳健发现** [R1-S2, R2-S4]：四个 benchmark 上 Jaccard 在第一个 attention level（4%）即饱和（Figure 4, all ρ ≤ 0.80, p ≥ .333），跨 benchmark 一致，不依赖任何单一 benchmark。

**S5. Permutation test 提供了 robust 的描述性证据** [R1-S2]：10,000 次置换下所有 architecture pair 均 p < .0001，为 "cross-architecture overlap 是结构性的" 提供可靠统计证据。

**S6. 写作规范透明** [R2-S5]：结构清晰，Abstract ≈ 148 词符合限制，多处使用 hedged language，ecological fallacy 自我承认（Related Work）。

---

## Weaknesses

### Critical

**W1. [Critical] Decoupling 叙事建立在统计上不成立的前提上** [R1-N1, R2-N1, 交叉 AGREE]

Contribution 2 的核心逻辑是 "aggregate variance 下降，但 per-example overlap 没有同步下降"。然而 aggregate convergence 本身不显著：
- LAMBADA 是唯一 ρ=-1.0 的 benchmark，Bonferroni 后 p=.170
- 排除 GDN 后 ρ 降至 -0.7, p=.233
- 340M 上不复现（ρ=-0.50, p=.45）
- 其余 9 个 benchmark 无此 trend

R2 精确指出：如果 aggregate narrowing 本身不成立，decoupling 是在回答一个不需要回答的问题。Section 4.2 的 "Regardless of whether this reflects a genuine trend, we ask..." 试图绕过但不充分。

**建议**：将 Contribution 2 重构为条件式 observation（"even on LAMBADA where the trend is strongest..."），或将重心转移到 Jaccard 饱和（S4）作为主发现。

**W2. [Critical] 单次训练 run 无法分离架构效应与 seed 效应** [R1-N2, R2-W4, 交叉 AGREE]

每个配置仅一次 run。Pythia 70M seed calibration 存在双重 mismatch：scale（70M vs 340M/1.3B）和 architecture（Transformer vs hybrid gating）。主文引用 calibration 时使用 "consistent with architecture-driven divergence"——高估了证据力度。

**状态**：结构性限制（第三方 zoo 无法重训），维持 wont_fix。但需强化 Limitations 讨论。

**W3. [Critical] 遗漏高度相关的先行工作 Yang & Wang (2026) "Benchmark Illusion"** [R2-N3, NEW]

Yang & Wang (2026, arXiv:2602.11898) 在 frontier LLMs 上展示了几乎相同的现象：comparable accuracy + 16-66% per-item disagreement + disagreement 传播到下游任务。这使本文的 "first systematic per-example analysis" claim 需重新界定。

**建议**：必须引用并在 Related Work 中定位本文增量贡献（controlled within-family analysis, Jaccard saturation quantification, attention-ratio parametric sweep）。

### Major

**W4. [Major] LAMBADA format confound 未被充分讨论** [R1-W1, R2-W2, 交叉 AGREE]

LAMBADA 是唯一 free-form generation benchmark（α=0.30，最高），其余全部 multiple-choice（α=0.14–0.21）。最高 multiplicity 和最强 convergence 恰巧都在唯一 open-ended 任务上。Multiple-choice 的有限答案空间机械约束 per-example divergence。§3.2 的 within-MC format mitigation（2-way vs 4-way）不够——远小于 MC vs free-form 的区别。

**建议**：Limitations 显式加入 format confound；§4.1 "multiplicity depends on task type" 改为 "task type or evaluation format"。

**W5. [Major] 新颖性为增量式——ecological fallacy 的 controlled instance** [R2-N2, R1 未 REBUT]

论文自己承认 decoupling 是 ecological fallacy 的 controlled instance，但未充分解释 beyond ecological fallacy 提供了什么 non-trivial 的新 insight。没有回答 WHY（mechanism）、WHEN（boundary conditions）、HOW severe（impact beyond routing）。

**状态**：Findings 标准下可接受，但需加强 mechanistic insight（如 Appendix F attention weight analysis 提升到正文）。

**W6. [Major] Routing 实践意义有限且结果不一致** [R1-W4, R2-W1, ���叉 AGREE]

4 个 benchmark 中仅 LAMBADA 有效（+5.2pp），ARC-Easy 微弱（+1.2pp），HellaSwag 无效（-0.06pp），PIQA 显著为负（-0.49pp, p=.006）。循环依赖：需先知道 multiplicity 水平才能 route。缺少 average-logits ensemble baseline。Abstract 中缺少 qualifier。

**建议**：Abstract routing 句加 "on the highest-multiplicity task"；补充 ensemble baseline；降级为 preliminary exploration。

**W7. [Major] GDN 16-head confound 导致 MMLU ρ 完全反转** [R1-W2, R2-W2]

GDN h3-1 使用 16 attention head（其他 32），排除后 MMLU ρ 从 -0.7 反转为 +0.6——方向完全逆转。应在 Table 1 首次引入 GDN 时即 flag。

**W8. [Major] 仅两个 scale 点且结果矛盾** [R1-W3]

340M：无 convergence（所有 |ρ| ≤ 0.4）；1.3B：仅 LAMBADA 有。两个数据点无法建立 scaling trend。Convergence 可能是 capacity-gated emergent phenomenon 而非 attention 的固有属性。

**W9. [Major] Confidence margin predictor 的 AUC 导出违反正态假设** [R1-W4]

Shapiro-Wilk 显示 rescue-set skewness 1.33-1.41（p<10⁻⁴），但 AUC point estimate 仍基于 Gaussian assumption。建议改用 non-parametric AUC（Mann-Whitney U）。

**W10. [Major] Task taxonomy 是 post-hoc 的** [R1-W5]

"Informal, not pre-registered"，缺乏可验证时间证据。Taxonomy 创建者与数据分析者为同一批人。用于 confirmatory claim 存在循环论证风险。

### Minor

**W11. [Minor] Bootstrap CI 在 n=3 下不具备名义覆盖率** [R1-W7]：Section 4.3 的 "excludes zero" 叙述可能误导。

**W12. [Minor] 全文 causal vs associative 语言不完全一致** [R1-W8]："reflects"、"modulated by"、"controlled" 等偶现的 causal 用语与 Section 3.5 的 "descriptive and exploratory" 声明矛盾。

**W13. [Minor] LAMBADA 和 ARC-Easy routing 增益数值完全相同（+1.2pp, SD=0.5pp）** [R1-W9]：需确认是否为独立计算。

**W14. [Minor] "Attention dose" 术语非标准** [R2-W5]：建议统一为 "attention ratio"。

**W15. [Minor] Introduction 贡献列表过长** [R2-W6]：每条 >100 词，建议精简为核心 claim + section 引用。

---

## Reviewer Consensus [AGREE]

1. **Overall 评分**：双方独立给出 3.0 (Findings)——完全一致
2. **Convergence claim 统计不足**：双方 Critical，交叉 AGREE
3. **LAMBADA format confound**：双方 Major，交叉 AGREE
4. **Routing 效果不一致**：双方 Major��交叉 AGREE
5. **Seed confound 为结构性限制**：双方认可���交叉 AGREE
6. **执行质量高**：双方肯定 statistical honesty, robustness coverage, experimental control
7. **Jaccard 饱和是最强发现**：双方 Strength，交叉 AGREE
8. **适合 Findings 而非主会议**：双方一致

## Reviewer Divergence [REBUT]

1. **Soundness 评分**：R1 = 2.5/5（更严格评估 inferential claims）vs R2 = 4/5（更注重 descriptive analysis 质量）。分歧源于对 "soundness" 的理解——R1 侧重 inferential validity，R2 侧��� methodological rigor。**Director 判断**：描述性分析确实 sound（permutation test, robustness），但推断性 claims（convergence, task-type causality）确实 underpowered。综合评为 3/5。

2. **Benchmark Illusion 的影响程度**：R2 认为是 critical missing reference（直接影响 novelty claim），R1 未提及该文献。**Director 判断**：R2 有理——Yang & Wang (2026) 在更大规模上展示了类似现象，本文需引用并重新定位贡献。

---

## Questions

1. LAMBADA 高 multiplicity（α=0.30）是否由 free-form generation format 而非 retrieval task type 驱动？是否有 TriviaQA generative 等其他 free-form benchmark 的初步数据？
2. Average-logits ensemble 的初步结果是否可获得？缺少此对比使 routing 的 practical value 评估不完整。
3. Pythia 70M within-seed J vs cross-architecture J 的比值在 hybrid 架构 340M/1.3B 上是否会保持？
4. LAMBADA 和 ARC-Easy routing 增益完全相同（+1.2pp, SD=0.5pp）——这是独立计算的精确值还是 reporting error？
5. GDN exclusion 后 MMLU ρ 从 -0.7 反转为 +0.6 如何解释？
6. Task taxonomy "was fixed prior to analysis" 有无客观时间证据（pre-registration ID/git commit hash）？
7. 本文与 Yang & Wang (2026) "Benchmark Illusion" 的关系——独立发现、互补分析、还是 partial overlap？

---

## Missing References

**必须引用**：
- Yang & Wang (2026) "Benchmark Illusion: Disagreement among LLMs and Its Scientific Consequences" (arXiv:2602.11898) — 核心发现高度重叠

**建议引用**：
- Li et al. (2024) "Dropout-Based Rashomon Set Exploration for Efficient Predictive Multiplicity Estimation" (arXiv:2402.00728)
- "Why are there many equally good models? An Anatomy of the Rashomon Effect" (2026, arXiv:2601.06730)
- MoE routing 文献（至少 1 篇代表性工作）— confidence-based routing 与 MoE per-token routing 概念相关
- MultiBERTs (Sellam et al. 2022) 在 seed calibration 语境中的引用

---

## External Review

**状态**：未请求（项目配置未启用外部审稿）。

---

## Visual Layout Check（非评分项）

**状态**：已完成（2026-05-24T13:15–13:19 UTC）

**Findings**（1 warning, 15 info）：

- ⚠️ **[Warning] Page 8**：三个 figure（5、6、7）挤在同一页，加上 Limitations 和 Code Availability 段落，页面极度拥挤。Figure 6 和 Figure 7 尺寸很小，内部文字 axis label 估计 <6pt，可读性受影响。
- ℹ️ Page 1：首页无视觉锚点（纯文本），Figure 1 在 page 2 顶部，位置尚可但非最优。
- ℹ️ Page 2：Figure 1 四子图 axis label/legend 字号偏小（估计 6-7pt）。
- ℹ��� Page 4：Figure 2 尺寸偏小（占左栏约 1/4 高度）。
- ���️ Pages 1-8：主体 8 页符合限制。Display items 共 9 个（7 figure + 2 table），密度 1.1/页，正常。布局节奏可接受。
- ℹ️ 全文：无 LaTeX 渲染错误、margin 溢出、section heading 孤悬。公式渲染正确。颜色语义基本一致。

---

## Overall Assessment

**Overall**: **3.0 (Findings)**

**置信度**: 4/5（两位 Reviewer 均仔细审查全文 21 页含 Appendix，交叉后完全收敛于 3.0）

**综合维度评分**：

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3/5 | 描述性分析 sound（permutation test robust, robustness 充分），但推断性 claims underpowered（convergence p=.170, seed confound, format confound）|
| Excitement | 2/5 | 核心发现在 Benchmark Illusion 和 ensemble diversity 文献中有先例。Ecological fallacy 自我承认削弱 novelty。Routing 仅 1/4 有效。|
| Reproducibility | 4/5 | 公开 model zoo + 标准 eval harness + 承诺代码公开。单次 run 无法验证 seed robustness 小幅扣分。|

**总结判断**：

本文执行质量属于 EMNLP 主会议水准——实验控制好、统计诚实、robustness 充分、写作规范。Jaccard 饱和（4% attention 即达稳态）是跨 benchmark 一致的稳健发现。

但作为主会议论文存在三个根本性问题：

1. **Decoupling 叙事的前提不成立**：aggregate convergence 本身 p=.170、GDN-dependent、不跨 scale 复现。论文的标志性发现建立在一个 non-finding 之上。
2. **新颖性为增量式**：ecological fallacy 的 controlled instance + Benchmark Illusion 的先行发现。本文增量贡献在于 controlled model zoo 上的系统量化，而非 "首次发现"。
3. **Practical actionability 不足**：routing 仅 1/4 benchmark 有效且 1/4 显著为负。

**适合 Findings track**：描述性贡献有价值（per-example multiplicity 的存在、结构性、Jaccard 饱和），方法论严谨度满足 Findings 要求。

**升至 Conference（4.0）的路径**：
- (a) 引用 Benchmark Illusion 并明确定位增量贡献
- (b) 将叙事重心从 decoupling 转移到 Jaccard 饱和
- (c) 至少一个 hybrid 架构 multi-seed 实验
- (d) 增加一个 free-form generation benchmark 以解耦 format confound
- (e) 补充 average-logits ensemble baseline

---

## Detailed Comments

### Abstract
- 148 词，符合 200 词限制 ✓
- "non-significant decreasing trend" 标注正确
- 缺少 routing 仅 1/4 有效的 qualifier

### Introduction
- 第1段信息密度过高（4行内 90%/10%/14%/p<.01）
- 贡献列表每条 >100 词，可精简
- "first systematic per-example analysis" 需在 Benchmark Illusion 上下文中重新界定

### Related Work
- 结构良好，三段覆盖三主题
- Ecological fallacy 自我承认是加分项
- 缺失 Yang & Wang (2026) Benchmark Illusion
- 缺失 MoE routing 文献
- Ensemble diversity 讨论过于简短

### Method
- 3.1 Model Zoo：GDN 16-head anomaly 应在此提及
- 3.2 Task Taxonomy："Mixed" 类别定义模糊；format confound 讨论不够
- 3.4 Per-Example Decomposition：binary decomposition 的 conservative bias 论证良好
- 3.5 Statistical Methods：n=5 power caveat 在此出现正确，但后文不一致遵循

### Experiments
- 4.1：核心描述性分析是论文最强部分。Routing 段落需加 significance test + 确认相同数值
- 4.2："The answer is no" 措辞暗示 clean result，但 aggregate convergence 本身不显���
- 4.3：GDN exclusion 讨论存在但 MMLU ρ 反转未在此报告

### Conclusion
- 避免了 over-claim，使用 "observations" 和 "preliminary suggest"
- "Per-example audit before architecture substitution is advisable" 可更具体

### Limitations
- 3 段覆盖 3 点，符合 EMNLP 规则 ✓
- 遗漏：format confound、n=5 statistical power、Pythia calibration 三重 mismatch

### 格式合规 ✓
- 正文 ≤ 8 页 ✓
- Limitations 在正文（非 appendix）✓
- 匿名完整 ✓
- Abstract < 200 词 ✓
- ACL template [review] ✓
- References 格式正确 ✓