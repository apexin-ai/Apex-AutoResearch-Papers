---
round: 8
overall_score: 3.0 (Findings)
timestamp: 2026-05-18T14:23:39.191189+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 11 (Fresh Review)

**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）
**轮次**: Round 1（1 轮独立审稿 + 1 轮交叉分享，关键问题达成共识）

---

## Summary

本文将 recursive generation depth estimation 形式化为 ordinal classification，构建了 180K 样本基准（3 model families × 3 decoding strategies × 4 depths），提出 Effective Discriminable Depth (EDD) 指标。基于 19 个统计特征的 Random Forest 分类器达到 69-86% 四分类准确率，perplexity tail statistics (p90_ppl, var_surprisal) 被识别为跨配置一致的深度标记。论文在 8 个泛化轴上进行了系统测试，但核心能力（d1-d3 区分）远弱于 headline metrics 所暗示。

---

## Strengths

**S1. 新颖且重要的任务形式化。** 首次将 recursive depth estimation 从 binary detection 推进到 ordinal classification，EDD 定义提供了操作性量化框架。在 model collapse 成为共识问题的背景下，"文本经历了多少轮递归生成"具有明确的实际需求。[R1, R2 一致]

**S2. 系统性实验设计。** 3×3 Atlas 网格有效隔离了 model family 和 decoding strategy 的贡献。8 个泛化轴的覆盖面在同类工作中罕见。1-1.5B 的窄参数区间是有意的实验控制，而非资源限制。[R1, R2 一致]

**S3. 特征分析有洞察力。** p90_ppl 9/9 cells top-2、var_surprisal 8/9 cells top-2、cross-model Spearman ρ=0.868，三种重要性度量 Kendall's W=0.90。特征层级随深度边界转移（浅层 var_surprisal → 深层 p90_ppl）提供了连接 model collapse 理论与实证信号的机制性洞察。[R1, R2 一致]

**S4. 透明的局限性报告。** 对 domain bias 实现 bug 的发现与修复、GPT-2 XL 跨种子 CI 不重叠、C4 上 20-22% FPR、跨策略 d1/d2 boundary inversion 等不利结果的坦诚报告超出大多数投稿的标准。[R1, R2 一致]

**S5. 实用性考量。** GPU-free 推理（2 min/5K samples）、5 特征精简模型保留 97.6% 性能、详细的计算资源报告。[R1]

**S6. 写作质量。** 全文无 AI 写作痕迹（无 em-dash、-ing phrases、AI 高频词汇），匿名化完整，引用覆盖充分（60+ unique cited keys），结构清晰。[R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**[CONSENSUS] W-C1: 序数分类形式化与实际方法/指标不一致**
- R1 首提 (N3)，R2 交叉回应称其为"R1 最有力的批评"并完全同意
- §3.1 将任务定义为 ordinal classification，但 (a) 主分类器 RF 不利用序数结构；(b) CORAL 仅在 1 cell 测试且与 RF 无显著差异（78.1% vs 78.7%）；(c) 全文无任何序数指标（MAE、QWK、相邻 vs 非相邻错误分布）
- 形式化与执行的不一致削弱了 Contribution 1 的实质性
- **Action**: 补充 MAE/QWK 指标；分析混淆矩阵中相邻 vs 非相邻类别错误分布；讨论为什么 CORAL 未超越 RF

**[CONSENSUS] W-C2: Discussion 过于简略**
- R2 首提 (N2)，R1 交叉回应升级同意
- §6 仅约 7 行，不符合包含 3×3 atlas + 8 个泛化轴的完整论文标准
- 缺少：(a) depth signal 机制性解释（tail erosion + memorization prerequisite，Appendix 有数据但主文未展开）；(b) 与 Dohmatob 2024 scaling law 的定量偏离分析；(c) deployment roadmap（strategy identification → depth classification pipeline）
- **Action**: 扩展 Discussion 至 3-4 段，整合 Appendix Extended Discussion 精华到正文

### Should-Fix（影响评分但不一票否决）

**[CONSENSUS] W-C3: d0 inflation 导致 headline metrics 与实际 d1-d3 区分能力有显著落差**
- R2 列为 Must-Fix (N3)，R1 认为是 Should-Fix (W1)（AI detection 领域普遍存在，论文已在 Table 2 括号中报告 d1-d3）
- 关键数据：cross-model d1-d3 balanced accuracy 55.4% (chance 33%)，within-distribution d2 recall 最低 45.6%，最弱配置 d2 recall 26.8%
- Abstract 的 "69-86%" 和 "66.4% cross-model" 是读者首先看到的数字，d1-d3 表现被严重弱化
- **Director 判定**: Should-Fix（R1 的论证有效——d0 inflation 是领域性问题且论文已部分 address，但展示优先级需调整）
- **Action**: Abstract/Contributions 同时突出报告 d1-d3 balanced accuracy

**[CONSENSUS] W-C4: 跨策略迁移近乎失败，two-stage pipeline 未验证**
- R1-W2 = R2-W2，双方一致
- d1-d3 仅 45.9% (chance 33%)，d1/d2 boundary inversion (AUC < 0.5)
- Two-stage pipeline 仅在 Limitations 提及，未报告策略识别模块的独立准确率
- **Action**: 在 Discussion 中更显著讨论此限制；验证并报告策略识别模块的独立性能

**[CONSENSUS] W-C5: 单 LoRA 种子构成混淆因子**
- R1 列为 critical (N2)，R2 降级为 should-fix（feature ranking 稳定，准确率波动不改变核心叙事）
- 跨种子复制仅覆盖 2/9 cells，GPT-2 XL CI 不重叠（差 2.04pp）
- **Director 判定**: Should-Fix（R2 的论证有效——feature ranking 跨种子一致是更重要的信号）
- **Action**: 对关键 cells 补充多种子复制，或降低跨 cell 比较结论的置信度

**[CONSENSUS] W-C6: 跨规模 7-8B 实验 confounds 未隔离**
- R1-W3 = R2-W3，双方一致
- 4-bit QLoRA、样本量缩减、仅 nucleus、vocabulary mismatch 四个因子同时变化
- **Action**: 主文弱化跨规模声明置信度

**[CONSENSUS] W-C7: 下游 curation PoC 不支撑实用价值叙事**
- R1-W5 = R2-W5，双方一致
- RF vs unfiltered p > 0.4；Discussion 仅引用 RF vs random 的 p<0.001，选择性引用
- **Action**: 降低 curation 声明力度；增加与简单困惑度阈值过滤的对比

**[CONSENSUS] W-C8: Abstract "19 perplexity-based features" 事实性不准确**
- R2-W1，R1 交叉同意
- 7/19 特征（lexical diversity + repetition）不依赖 reference model perplexity
- **Action**: 修正为 "19 statistical features" 或 "19 features anchored in reference-model perplexity statistics"

### Minor

**M1.** EDD binary classifiers 500 trees vs 主实验 200 trees 不一致未解释 [R1, R2 agree]
**M2.** Prompted generation 验证仅 1 cell (GPT-2 XL nucleus)，至少应覆盖 2-3 cells [R1, R2 agree]
**M3.** 存在 orphan bib entries (pareek2024understanding 等)，应清理或引用 [R1, R2 agree]
**M4.** 遗漏 Janitza et al. 2016 (ordinal random forest)、C2PA/data provenance 标准 [R1, R2 agree]
**M5.** Table 2 caption 中 d1-d3 括号值展示不够清晰 [R1]
**M6.** "43pp below RF" 数值不精确，应指定参照点 [R2, R1 agree]
**M7.** Curation PoC 多次配对比较未做多重比较校正 [R1]

---

## Reviewer Consensus

以下问题双方达成共识 [AGREE]：
1. 序数形式化与执行不一致是真实的方法论缺陷
2. Discussion 需大幅扩展
3. d0 inflation 是展示问题（严重性分歧已由 Director 裁定为 Should-Fix）
4. 跨策略迁移失败是实用性的根本限制
5. 单 LoRA 种子问题存在但 feature ranking 稳定性部分缓解（Director 裁定 Should-Fix）
6. 下游 curation PoC 不具说服力
7. 7-8B confounds 需更透明讨论
8. Abstract 特征描述需修正

## Reviewer Divergence

**[REBUT 未解决] 方法论新颖性**
- R2 (N1): RF + 手工特征缺乏算法贡献，EMNLP 期望方法论创新或显著新洞见
- R1 (REBUT): 论文属于任务定义 + 系统实证类型，分类器收敛本身是科学发现，ACL 系列接受 analysis/resource 型论文
- **Director 评估**: R1 的反驳部分有效——ACL venues 确实接受 empirical/analysis 论文（如 Binoculars, GLTR），且 strategy-dependent trajectories 和特征层级转移是理论未预测的新发现。但 R2 的担忧也有道理：EDD 的形式新颖性确实有限。综合判断，方法论新颖性不足不应作为单独的 reject 理由，但需要更诚实的定位。

**[REBUT 未解决] EDD 统计声明**
- R1 (N1): EDD_{0.75}=4 仅 1/3 模型显著，headline claim 过度
- R2 (REBUT): 论文措辞已限定 "best-characterized family"，建议 T=0.70 为主指标作为改进
- **Director 评估**: 论文当前措辞在正文中确实较谨慎（p 值已列出），但 Abstract 第 5 行的 "EDD_{0.75}=4" 仍可能给快速阅读者留下过强印象。以 T=0.70 为主指标是实用的改进方向。

---

## Questions（需作者澄清）

**Q1.** 主实验和跨模型 transfer 的 MAE 和 Quadratic Weighted Kappa 是多少？混淆矩阵中相邻类别错误占总错误的比例是多少？[R1-Q1, R2-Q1, 与 W-C1 直接相关]

**Q2.** 如果将 EDD 默认阈值设为 T=0.70（8/9 cells 达标），核心叙事是否改变？[R1-Q2, R2 同意]

**Q3.** Perplexity tail statistics 作为 depth marker 是 LoRA fine-tuning 特有的，还是任何 fine-tuning 方法都会产生？[R2-Q2]

**Q4.** 从 controlled benchmark 到 wild web data 的 generalization gap 如何评估？C4 上 20-22% FPR 对实际部署意味着什么？[R2-Q3]

**Q5.** Two-stage pipeline（策略识别 → 深度分类）中策略识别模块的独立准确率是多少？[R1-W2, R2-W2]

---

## Missing References

1. **Janitza et al. 2016** — "Random forest for ordinal responses" — ordinal RF 应在 Related Work §2 讨论或作 baseline [R1, R2 agree]
2. **Pareek et al. 2024** — "Understanding the Gains from Repeated Self-Distillation" — 已在 bib 中但未引用 (orphan) [R1]
3. **C2PA / Content Credentials 标准** — 与 provenance toolkit vision 直接相关 [R2]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**评分依据：**

两位 Reviewer 评分分别为 3.5 (R1, Borderline Conference) 和 3.0 (R2, Findings)。

核心分歧在于方法论新颖性的权重：R1 认为任务定义 + 系统实证的贡献类型足以支撑 Borderline Conference；R2 认为缺乏算法创新和有限的 d1-d3 区分能力将其限制在 Findings。

Director 裁定 Overall 3.0 (Findings)，理由如下：

**支持 Findings (3.0) 而非 Borderline Conference (3.5) 的因素：**
1. 序数形式化与执行的不一致（W-C1）是方法论层面的真实缺陷，且两位 Reviewer 一致同意——这直接削弱了 Contribution 1
2. Discussion 仅 7 行（W-C2）是完整性问题——关键科学洞察（memorization prerequisite、Dohmatob 定量偏离、deployment roadmap）藏在附录，正文缺乏深度
3. d1-d3 实际区分能力有限（cross-model balanced acc 55.4%，d2 recall 最低 26.8%），与 headline 69-86% 之间的落差（W-C3）降低了 excitement
4. 跨策略迁移失败（W-C4）限制了实际应用场景

**支持 Findings (3.0) 而非 Borderline Findings (2.5) 的因素：**
1. 任务定义确实新颖且有明确需求——recursive depth estimation 是一个值得研究的问题
2. 3×3 Atlas + 8 个泛化轴的系统性实验设计在同类工作中罕见
3. Feature consistency 发现（p90_ppl 9/9 cells top-2）和 strategy-dependent trajectories 是有价值的科学贡献
4. 透明诚实的局限性报告和高可复现性
5. 写作质量高，无 AI 痕迹

**如果作者能在 rebuttal 中充分回应以下问题，论文有望上升至 3.5：**
1. 补充 MAE/QWK 等序数指标，实证展示序数结构的存在
2. 扩展 Discussion 至 3-4 段，将 Appendix 精华整合
3. 在 Abstract/Contributions 中同等突出 d1-d3 balanced accuracy
4. 验证 two-stage pipeline 策略识别模块

**Confidence: 4/5** — 两位 Reviewer 均表达高置信度（4/5），覆盖了方法/实验（R1）和新颖性/写作（R2）两个维度，交叉分享过程充分。

---

## Detailed Comments（逐节）

### Abstract
- "19 perplexity-based features" 应修正为 "19 statistical features"（W-C8）
- "≈69-86% four-class accuracy" 应平行报告 d1-d3 balanced accuracy（W-C3）
- "43 pp below RF" 数值不精确，应指定参照 cell（M6）

### Introduction
- Contribution 1 ("task formalization") 需要配套的序数指标和方法论支撑（W-C1）
- 论文定位应更明确为 empirical study + problem formalization（R11-D1）

### Method
- EDD Definition 1 中 binary classifiers 500 trees vs 主实验 200 trees 不一致（M1）
- 19 特征选择缺乏系统论证（R1-M3）

### Atlas (§4)
- 核心结果表现良好，feature consistency 分析是论文亮点
- EDD 报告建议以 T=0.70 为主、T=0.75 为辅（R11-D2）

### Generalization (§5)
- Cross-model/cross-strategy/cross-scale 实验覆盖面好
- Prompted generation 仅 1 cell，应扩展（M2）

### Discussion (§6)
- 需大幅扩展，当前严重不足（W-C2）

### Limitations
- 已有内容诚实详尽，但跨策略失败的部署影响应在 Discussion 中更显著讨论（W-C4）

### Appendix
- 内容丰富但部分关键 insight 应回到正文（Extended Discussion, Curation PoC caveat）
- Curation PoC 的 selective reporting 需修正（W-C7）