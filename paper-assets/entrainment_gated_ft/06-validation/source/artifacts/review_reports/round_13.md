---
round: 13
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T10:03:00.428750+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 13

**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计, R2 新颖性+完整性+写作）
**交叉分享轮数**: 1 轮（关键问题已收敛）

---

## Summary

论文使用 Wang et al. (2025) 的 controlled model zoo（3 架构 × 5 attention ratio × 2 scale = 30 配置），在 10 个 benchmark 上系统分析了 hybrid recurrent 架构中 attention 对 per-example 预测行为的影响。核心发现：(1) 不同架构在 aggregate benchmark 上可近似等效，但在 per-example 层面影响近乎不重叠的样本子集（pairwise Jaccard ≤ 0.10）；(2) ambiguity α 在 0.14–0.30 范围内随 task type 变化但不随 attention dose 变化；(3) 在 LAMBADA 上观察到 aggregate convergence 与 per-example divergence 的脱耦现象（Bonferroni-adjusted p = .100，exploratory）。

---

## Strengths

1. **研究问题新颖且及时**：在 hybrid recurrent 架构快速发展的背景下，首次系统研究 per-example predictive multiplicity 如何受 attention 分配策略影响，切中 practitioners 基于 aggregate benchmark 选择架构的实际痛点。[R1-S1, R2-S4]

2. **Controlled model zoo 设计优秀**：固定 training data / hyperparameters / tokenizer，仅变化 architecture 和 attention ratio，是研究 architectural effects 的理想设置。[R1-S2, R2-S3]

3. **统计方法论的透明度和严谨性**：论文在每一步提供 exact p-values、power analysis、bootstrap CIs，坦诚 n=3 和 n=5 的局限性。GDN confound 的 sensitivity analysis 是特别好的做法。[R1-S3, R2-S1]

4. **附录极其详尽**：12 页、17+ 张表，covering cross-scale analysis, supplementary benchmarks (BoolQ, WinoGrande), within-architecture stability, normalized Jaccard effect sizes, confidence margin analysis, complementarity decomposition——每个 claim 都有 backup evidence。[R1-S4, R2-S2]

5. **Per-example overlap 饱和现象稳健**：Jaccard 在首个 attention level (4%) 即饱和的发现在四个 benchmark 上一致，不依赖特定统计假设，是论文最可靠的贡献。[R1-S5]

6. **格式完全合规**：8 页正文、ACL 模板、double-blind、Limitations 简洁覆盖 3 点、Ethics Statement 存在。[R2-S5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**[N1] [Critical] Convergence claim 统计不足却占据核心叙事位置** [R1-N1 + R2-N2, 交叉共识 AGREE]
- LAMBADA 是唯一显示 monotonic convergence 的 benchmark（ρ = −1.0, p = .017），但 Bonferroni 校正后 p = .100（6-benchmark）或 .170（10-benchmark），均未达传统显著性。排除 GDN 后进一步弱化（ρ = −0.7, p = .233）。
- 然而 convergence 占据 Abstract 第2句、Introduction 第1段、§4.3 全节，给读者留下 convergence 是 established finding 的印象。
- 如果 convergence 不成立，"decoupling" 叙事退化为"无 convergence，per-example 也无 convergence"，叙事价值大幅下降。
- **两位 Reviewer 完全一致**：convergence claim 降级是必要修改条件。

**[N2] [Critical] n=5 Spearman 检验严重 underpowered** [R1-N2, R2 AGREE with nuance]
- n=5 exact Spearman 仅 |ρ| = 1.0 时达 p < .05；|ρ| = 0.9 无法检测（p = .083）。
- 论文在 §3.3 Power considerations 已承认，但 §4.1 讨论中"No other benchmark shows significant convergence"缺少 power caveat，容易被误读为 evidence of absence。
- R2 不认为 Bayesian analysis 是必要的，建议聚焦 effect size direction + 在 Table 1 附加 power caveat。

**[N3] [Critical] 单次训练 run 无法分离架构效应与种子效应** [R1-N3 + R2-Q4, 交叉共识 AGREE]
- 每个配置仅一次训练，within-architecture Jaccard ~3× cross-architecture 是间接证据但不充分（within-architecture 比较跨 attention ratio，引入第二变量）。
- R2 指出补充 seed replicates 不现实（公开 model zoo，需重新 pre-train 30 个 1.3B 模型）。
- **共识建议**：将 "architecture-specific" 系统性替换为 "configuration-specific"，在 claims 不依赖 architecture vs. seed 区分的地方保持原表述。

**[N4] [Critical/Major, 分歧] 新颖性有限** [R2-N3 Critical, R1 REBUT 建议 Major]
- R2 认为：方法论无创新（所有分析工具为已有方法直接套用），核心发现是已知现象（ecological fallacy + seed variation 文献）的新场景验证。Excitement 2/5。
- R1 反驳：(a) ACL 论文不要求方法论创新，empirical contribution 是合法贡献类型；(b) cross-architecture multiplicity 的量化发现（4% 饱和、task-dependent α 变异、3× Jaccard gap）不可从已有文献推断；(c) seed variation 与 architecture variation 的实践含义不同。建议降为 Major。Excitement 3/5。
- **分歧未完全解决**，但双方均给 Overall 3.0 (Findings)。

**[N5] [Critical] Decoupling finding 缺乏对 Ecological Fallacy 的讨论** [R2-N1, R1 AGREE with nuance]
- Aggregate convergence 与 per-example divergence 的脱耦是 ecological fallacy (Robinson, 1950) 的具体实例。论文完全未引用或讨论。
- R1 同意应引用 Robinson (1950)，但认为量化 characterization（Jaccard 饱和点、task-dependent α 变异）超越概念预期——建议添加讨论但无需重新定位论文。

### Should-Fix（影响评分但不一票否决）

**[W1] [Major] GDN h3-1 16-head confound 应在主文讨论** [R1-W1, R2 AGREE]
- 排除 GDN 后唯一显著 convergence 结果消失。当前仅在 §4.4 和 Appendix 处理。
- 共识：应在 §4.1 首次报告 LAMBADA 结果时即讨论此 confound。

**[W2] [Major/Warning, 分歧] Bootstrap CI (n=3) 信息量低** [R1-W2 Major, R2 partial REBUT]
- R1：n=3 仅 27 unique resamples，Figure 2 CI bars 视觉上易被误读。建议改用 strip plot。
- R2：论文已标注 "heuristic"，不构成 Major 问题，但同意 strip plot 是更好的可视化方案。

**[W3] [Major/REBUT, 分歧] Binary decomposition 丢失效应量** [R1-W3 Major, R2 REBUT]
- R1：主文核心 Jaccard 分析基于二值分类，0.51→0.49 和 0.99→0.01 被同等对待。
- R2 反驳：Appendix H 已提供完整 continuous confidence margin analysis（Tables 12-16, AUC-based prediction framework），R1 可能遗漏。论文已做了 R1 建议的补充。

**[W4] [Warning] 残余因果语言** [R2-W1, R1 AGREE]
- Abstract "they help and hurt almost entirely different examples"、§4.2 "attention consistently rescues near-miss errors" 仍含因果语言。共识：统一使用关联语言。

**[W5] [Warning] Abstract 信息密度过高** [R2-W2, R1 AGREE]
- ~150 词含 α 值、p 值、Jaccard、百分比、oracle accuracy 等多个数字。共识：保留 1-2 个关键数字，其余移至 Introduction/Results。

**[W6] [Warning] Practical implications 泛化过度** [R2-W3, R1 AGREE]
- §5 "whenever hybrid designs achieve comparable aggregate scores" 从 3 架构/2 scale/4 benchmark 泛化过度。共识：限定到论文实际覆盖场景。

**[W7] [Warning] Ensemble diversity 文献连接不充分** [R2-W5, R1 AGREE]
- §2 仅引用 Kuncheva & Whitaker (2003)，未讨论 Q-statistic、bias-variance-covariance decomposition 等与 Jaccard-based analysis 直接相关的 diversity measures。

**[W8] [Warning] Confirmatory/exploratory split 缺乏时间戳** [R1-W4, R2 AGREE]
- Appendix A 承认 "no external timestamp exists"。共识：标注为 "informal pre-analysis plan"。

**[W9] [Warning] 评估覆盖范围有限** [R1-W5, R2 AGREE]
- 不含 Mamba/Mamba-2/RWKV，无 generation tasks，仅 pre-training evaluation。Limitations 中应更具体讨论 generalization 边界。

### 小问题
- lm-eval-harness 版本 "v0.4.x" 应改为精确版本号和 commit hash [R1]
- Table 1 脚注 Bonferroni p 两个数字 (0.100 vs 0.102) 同时出现造成混淆 [R2-M3]
- §4.2 "normalized ES" 缩写首次出现未定义 [R2-M4]
- Conclusion 中 "confidence-informed routing" 无初步实验支撑 [R2-M5]
- Figure 1 caption (b) 应说明 cross-architecture pairwise [R1]
- Appendix 最后一页 >75% 空白 [视觉审查]

---

## Questions

1. 如果补充 2-3 个 seed replicate（即使仅在 1.3B LAMBADA h3-1），within-seed vs cross-seed Jaccard 的预期比值是多少？[R1-Q1]
2. MMLU/ARC-Easy 的 non-significance 是完全由 power 限制解释还是反映 true null？如果 n=10，这些 ρ 值是否会显著？[R1-Q2]
3. Jaccard 在 4% attention 饱和的发现在 340M 上是否成立？缺少 340M ratio-by-ratio 轨迹数据。[R1-Q3, R2 确认数据缺口]
4. "per-example audits" 在无 oracle 标签的 deployment 场景下如何操作？Appendix O.2 的 confidence margin framework (AUC 0.70-0.74) 是否可发展为 practical tool？[R2-Q3, R1 指出 Appendix 有初步方案]
5. 如何将 decoupling finding 与 ecological fallacy (Robinson 1950) 区分？量化 characterization 是否足以构成超越概念预期的贡献？[R2-Q1, R1 认为是]

---

## Missing References

**两位共识**：
- Robinson, W.S. (1950) "Ecological Correlations and the Behavior of Individuals" — ecological fallacy 经典参考，直接关联 decoupling finding
- Brown et al. (2005) "Diversity Creation Methods: A Survey and Categorisation" — ensemble diversity measures 综述

**R1 建议（R2 部分同意）**：
- Peng et al. (2025) RWKV-7 — Related Work 中的 hybrid architecture landscape

**R2 建议**：
- Jiang et al. (2021) "How Can We Know When Language Models Know?" — 与 confidence margin analysis 相关

**R1 建议（R2 REBUT）**：
- Wen et al. (2024) BatchEnsemble — R2 认为相关性低

---

## External Review

外部审稿未配置。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 6 info）：
- **[Warning]** Pages 3-4：连续约 2 页纯文本（Method 节），无 figure/table/equation 穿插。Model Zoo 的 30 个配置可考虑用概览表/示意图打破视觉单调。
- **[Warning]** Pages 1-8：正文 8 页仅 4 个 display items（2 figure + 2 table），对于实证论文偏少（典型 5-8 个）。大量结果表格被推到附录，正文 text-heavy。
- **[Info]** Figure 1 subfigure axis label 和 legend 字号偏小（~60-65% 正文字号）。
- **[Info]** Figure 2 单栏宽度，散点密集区域标签有轻微重叠。
- **[Info]** 附录最后一页 >75% 空白。
- **[Info]** Table 1 Ratio 列最大值未加粗标注。
- **[Info]** Table 2 偏小，周围留白较多。
- **[Info]** Figure 1 caption (c) subfigure y 轴 "pairwise Jaccard" 初次出现无含义说明。

---

## Reviewer Consensus

**[AGREE] 以下问题两位 Reviewer 达成完全共识**：
- Convergence claim 统计不足 + 叙事权重过高 → 必须降格为 exploratory/secondary
- 单次训练 run 无法分离 seed/architecture → 结构性限制，建议 "architecture-specific" → "configuration-specific"
- Ecological fallacy 应明确讨论 → 引用 Robinson (1950)
- GDN 16-head confound → 应在 §4.1 首次报告时讨论
- 因果语言 → 统一使用关联语言
- Abstract 信息密度 → 保留 1-2 个关键数字
- Practical implications → 限定到实际覆盖场景
- 评估覆盖范围 → Limitations 更具体

## Reviewer Divergence

**[REBUT/分歧] 以下问题存在分歧**：
1. **新颖性严重程度**：R2 Critical（方法论无创新 + 已知现象验证）vs R1 Major（empirical contribution 合法，量化发现不可从已有文献推断）。双方最终均给 Overall 3.0。
2. **Binary decomposition**：R1 Major（主文应引入 continuous Jaccard）vs R2 REBUT（Appendix H 已充分）。
3. **Bootstrap CI**：R1 Major vs R2 非 Major（论文已标注 heuristic）。
4. **Intro/Abstract 重复**：R2 Warning vs R1 REBUT（正常学术结构）。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3/5 | 3/5 |
| Excitement | 3/5 | 2/5 | 2.5/5 |
| Reproducibility | 3.5/5 | 4/5 | 3.5/5 |
| Overall | 3.0 | 3.0 | 3.0 |

**评分依据**：

论文在 controlled experiment 设计、统计透明度和附录详尽度上表现优秀。Per-example multiplicity 的存在性及其 task-dependent variation（α = 0.14–0.30）得到了可靠的实证支撑，Jaccard 饱和在 4% attention level 的发现是稳健且新颖的。

但三个核心问题限制了论文影响力：
1. **Convergence claim 是全文叙事的核心支柱，但统计上不显著**（Bonferroni p = .100），且依赖 GDN 的 16-head confound——这使得 "decoupling" 这一核心框架的一半缺乏支撑。
2. **单次训练 run 使所有 "architecture-specific" 的 claim 无法与 seed 效应区分**——这是一个不可通过分析弥补的实验设计限制。
3. **方法论无创新**——所有分析工具为已有方法直接套用（R1/R2 分歧在于此问题的严重程度，但均同意论文定位为 Findings）。

论文适合 Findings 接收：分析彻底、统计透明、实证有价值，但新颖性和影响力不足以支撑主会议接收。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度过高（~150 词含 6+ 数字），建议精简至 1-2 个关键量化结论
- "they help and hurt almost entirely different examples" → 因果语言，改为关联表述
- Bonferroni-adjusted p = .100 作为 convergence 证据呈现有误导性

### Introduction (§1)
- 前 3 段与 Abstract 内容重叠度高（R2 Warning, R1 认为正常）
- Contributions 列表中 C2 (decoupling) 的表述需与 convergence 降格同步调整
- "architecture-specific" 措辞应改为 "configuration-specific"

### Related Work (§2)
- 缺少 ecological fallacy (Robinson 1950) 的讨论——这是与 decoupling finding 最直接的理论连接
- Ensemble diversity 文献连接不足：仅引用 Kuncheva & Whitaker 2003，缺 Brown et al. 2005 综述和 Q-statistic 等 diversity measures
- Rashomon set 区分已到位（Fisher 2019, Semenova 2022）

### Method (§3)
- §3.2 lm-eval-harness "v0.4.x" 应改为精确版本号
- §3.3 Power considerations 段内容好，但 §4.1 讨论时未一致引用
- §3.4 binary decomposition limitation 讨论充分，bias direction argument 有说服力
- Pages 3-4 连续纯文本，缺乏 visual break（视觉审查 Warning）

### Experiments (§4)
- §4.1 Table 1：LAMBADA 是唯一显著结果，但 non-significant benchmarks 的讨论缺 power caveat
- §4.1 应在首次报告 LAMBADA 结果时即讨论 GDN confound，而非延后到 §4.4
- §4.2 Per-example analysis 是论文最强的部分——Jaccard 统计严格，confidence margin mechanism 有洞察力
- §4.3 Decoupling 叙事需重构——convergence 降格后，应以 per-example multiplicity 为核心

### Conclusion (§5)
- "whenever hybrid designs achieve comparable aggregate scores" 泛化过度
- "confidence-informed routing" 无初步实验支撑
- 建议增加 1-2 句 deployment-side implication（Appendix O.2 有初步方案但未在主文提及）

### Limitations
- 3 段 3 点，格式合规
- 内容覆盖 seed limitation、scale limitation、pre-training only
- 应更具体讨论 generalization 边界（缺 Mamba/RWKV/generation tasks）