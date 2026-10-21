---
round: 2
review_mode: fresh
overall_score: weak reject (4/10)
timestamp: 2026-05-28T12:03:10.303737+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 3（Fresh 模式）

**项目**: occsafe_vla
**论文**: "Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? An Empirical Investigation"
**目标 Venue**: CoRL 2026
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计 + 统计分析；R2: 新颖性 + 完整性 + 格式）
**轮次**: 1 轮初审 + 交叉分享，全 [AGREE] 共识，无需第二轮
**外部审稿**: 未请求
**视觉审查**: 已完成

---

## Summary

论文通过 12 条件 factorial 研究，考察辅助空间监督（occupancy prediction）对 VLA 模型碰撞安全的影响。核心发现被框架为 "normalization-dependent gradient flow effect"：BN 下 gradient flow 降低 CAR（0.725 vs Vanilla 0.745），LN 下无害（0.773）。实验基于 OpenVLA-7B + OFT + LoRA rank 32，在 SafeLIBERO Level I 上评估，每 cell n=3-4。论文提出 BN running statistics 假说解释该现象，并给出实践指南。

---

## Strengths

- **S1**: 研究问题重要且及时——在 15+ 篇空间 VLA 方法均假设 "更好的空间感知→更安全" 的背景下，首次系统验证该假设对碰撞安全的影响
- **S2**: 坦诚报告 v1→v2 codebase sensitivity（同 seed 偏移 8.6pp）——大多数论文会隐藏此类信息，透明度值得肯定
- **S3**: 梯度分析（CKA、per-layer gradient norms、cosine similarity）提供了超越单纯指标对比的机制洞察
- **S4**: 2×2 factorial 设计在 VLA auxiliary supervision 文献中填补方法论空白——该领域此前完全依赖单因子 ablation
- **S5**: 实验设计中的 v1/v2 分离处理（Table 分区、★标记、ΔCAR="---"）显示对数据完整性的认真态度

---

## Weaknesses

### Must-Fix（Critical — 需解决后方可接受）

**C1: "Normalization-dependent gradient flow effect" 框架与 ANOVA 结果根本矛盾** [R1 发现, R2 认同]

论文中心主张使用 "normalization-dependent gradient flow effect" 一词（Abstract, Introduction Contribution 1），这在统计学上是交互效应（interaction effect）——即 gradient flow 的效应取决于（is moderated by）normalization type。然而论文自身 2×2 ANOVA（results.tex, Appendix F Table 6）报告交互项 F(1,10)=0.10, p=0.76, η²&lt;0.01——完全不显著。Figure 2 两条线近似平行，视觉确认 additive pattern。

实际发现是两个独立的 additive main effects：
1. Gradient flow 一致性地降低 CAR ~3-4pp（主效应 1）
2. LN 一致性地提高 CAR ~3.5-4.8pp（主效应 2）
3. 两者独立叠加，不存在调节关系

"Gradient flow is safe under LN" 的表述误导——LN 下 gradient flow 同样有 ~2.9pp penalty（Table 3: ON→OFF 差异），只是因为 LN 基线高所以最终 CAR 仍可接受。

结合 C3（interaction power &lt;20%），Abstract 中 "A 2×2 ANOVA confirms additive main effects with negligible interaction" 犯了 "absence of evidence ≠ evidence of absence" 的统计推理错误——underpowered test 的非显著结果不能被解读为对 null hypothesis 的确认。

- **修复方案**: (a) 将 "normalization-dependent gradient flow effect" 改为 "two independent additive main effects: gradient flow penalty and normalization advantage"；(b) 删除 "confirms additive"，改为 "interaction was not detected, though power to detect interaction was low"；(c) 重写 Contribution 1 的框架

**C2: v1/v2 codebase confound 破坏跨条件比较** [R1+R2]

v1→v2 同条件 CAR 偏移 ~8.6pp，而论文报告的最大实验效应（gradient flow penalty）仅 ~4-6pp。即 codebase version 的效应量大于实验处理的效应量。任何涉及 v1 条件的跨条件比较都被这一未控制变量污染。

- Content irrelevance 发现（Full OCC vs Random OCC vs Depth）仅有 v1 证据
- v1→v2 已导致效应模式翻转（Discussion: "the effect pattern itself changed from an apparent crossover under v1 to the dual main effects reported here"）
- Gradient orthogonality 作为间接支撑的逻辑有缺陷——orthogonality 在 v1 下也成立但定性结论仍翻转
- v1/v2 混合还意味着 Table 1 中 supplementary conditions（v1）与 core conditions（v2）不可直接比较
- **修复方案**: (a) v2 下重训 Random OCC 验证 content irrelevance；或 (b) 从 Abstract/Contributions 移除，降级为 Discussion 中的 preliminary observation + 明确 v1 caveat

**C3: 统计效力严重不足** [R1+R2]

n=3-4 per cell：
- 对 medium effect size 的 power &lt;50%
- 对交互效应的 power &lt;20%（经验法则：交互检测需主效应 4 倍样本量）
- Cohen's d=0.93（n₁=n₂=3）的 95% CI 约 [-0.8, 2.7]——包含零甚至反向效应
- ANOVA 两个主效应 p=0.104 和 p=0.060，在任何常规标准下均不显著
- Hedges' g 校正后 d=0.93→g≈0.75，从 "large"（≥0.80）滑入 "medium-to-large"
- Discussion 使用因果语言（"gradient flow degrades safety"、"gradient flow reduces CAR by 4.2pp"），超出关联性证据支撑
- **修复方案**: (a) 增加样本量至 n≥5（理想 n≥8）达到 power=0.80；(b) 将所有因果语言降级为关联性描述（"is associated with"）；(c) 报告 Hedges' g 和 bootstrap CI

**C4: 格式违规 — Limitations 不在正文 + 超页** [R1+R2]

- discussion.tex 仅有指针句 "Limitations are in Appendix"，全文在 Appendix H
- CoRL 2026 要求 Limitations 计入 8 页正文
- PDF 第 8 页被 Discussion 占满，Conclusion 起始于第 9 页
- 加上需移入的 Limitations，总正文量约 10 页，需压缩至少 2 页
- 明确格式违规，desk reject 风险
- **修复方案**: Limitations 移入正文 + 压缩 Related Work / Method / Discussion 冗余段落

---

### Should-Fix（Warning — 强烈建议修复）

**W1: ANOVA 前提假设不可验证** [R1+R2]
- n=3-4 下 Shapiro-Wilk 和 Levene's test 几乎无统计功效
- 未提供残差分布诊断图或非参数替代方案
- **建议**: 补充 permutation test（Anderson 2001）作为稳健替代

**W2: 梯度正交性与 gradient flow harmful 的矛盾 — 机制解释空白** [R1+R2 互补]
- Gradient cosine similarity ≈ 0（正交），排除 PCGrad 意义上的 gradient conflict
- 但论文同时声称 gradient flow 有害，"indirect effect through LoRA optimization trajectory" 无直接证据
- R2 补充可能机制：BN running statistics corruption 不需要梯度方向冲突——forward pass 即可更新 running mean/variance
- 但论文既未清晰提出此机制假说，也未提供 BN running stats 漂移的直接测量
- **建议**: 在 Discussion 中明确区分 gradient conflict（已排除）和 BN forward-pass statistics corruption（假说），提供测量或标注为 unverified

**W3: Cohen's d 小样本偏差未校正** [R1+R2]
- n₁=n₂=3 时 Hedges' g 校正因子 J≈0.81，d=0.93→g≈0.75
- 从 "large"（≥0.80）边界滑入 "medium-to-large"，改变叙事力度
- **建议**: 正文所有效应量改报 Hedges' g + bootstrap CI

**W4: 单一 benchmark + 架构** [R1+R2]
- 仅 SafeLIBERO Level I（static obstacles, 7 tasks）+ OpenVLA-7B + OFT + LoRA rank 32
- Level II/III 有不同约束类型，normalization-gradient flow 效应可能呈现不同模式
- 标题 "Vision-Language-Action Models" 暗示对整个 VLA 类别的回答
- Conclusion "Practitioners should omit auxiliary spatial heads" 无限定条件
- **建议**: 标题加副标题限定范围；Conclusion 加 LoRA-specificity 和 benchmark 限定

**W5: λ₀=0.01 固定，缺乏超参数敏感度分析** [R1+R2]
- λ₀ 直接控制 auxiliary gradient 幅度——λ₀ 极小（0.001）时效应可能消失，λ₀ 较大（0.1）时可能更强
- 当前结论可能高度依赖 λ₀=0.01 这一特定选择
- **建议**: 补充 λ₀ ∈ {0.001, 0.01, 0.1} 消融实验验证鲁棒性

**W6: Factorial 设计不完整，声明过度** [R1+R2]
- Introduction 声称 "twelve conditions varying five factors"
- 完整 factorial crossing 仅限 2×2（gradient flow × normalization）
- Label content、reference frame、temporal extent 均为单因子 ablation
- Contribution 2 将 factorial methodology 列为独立贡献不恰当——factorial design 是标准统计方法（Fisher, 1935）
- Introduction 声称 "single-factor ablations cannot detect interactions" 但论文自己的 factorial 也未检测到交互（p=0.76）
- **建议**: Method 修正为 "2×2 factorial core + single-factor ablations"；Contribution 2 降级

**W7: BN running statistics 假说未直接验证** [R1+R2]
- Discussion 明确承认 "hypothesize but do not directly test"
- 低成本验证方案已知但未执行：eval mode（frozen running stats）或 momentum=0
- **建议**: 在已训练 v2 模型上执行 BN eval mode 消融。若 eval mode BN 恢复 CAR，直接验证假说

**W8: Codebase sensitivity 削弱实践指导价值** [R1+R2]
- 同 seed v1→v2 偏移 8.6pp ≈ 核心效应量（4.2pp）的 2 倍——实现噪声与信号同量级
- Discussion 将此框架为 "independent finding"，但双刃剑：v2 结论可能在 v3 下再次改变
- Practical guidelines 需在特定实现下稳健才有实际价值
- **建议**: 降低 guidelines 普适性声明；明确标注适用范围限定

**W9: 缺少关键前驱文献** [R1+R2]
- **task-specific BN 文献**（BN 假说直接前驱）：Bilen & Vedaldi (2017), Maninis et al. (2019 ASTMT), Rebuffi et al. (2018) [强烈建议]
- **统计方法论**：Montgomery — Design and Analysis of Experiments; Anderson (2001) — Permutation tests [建议]
- **BN fine-tuning**：Li et al. (2016) / Ioffe (2017) [建议]
- **Multi-objective optimization**：Sener & Koltun (2018 MGDA) [建议]
- **当前 VLA 架构**：π₀ (Black et al. 2024), Octo (Team Octo 2024) [强烈建议]

---

## Reviewer Consensus（交叉分享共识）

以下问题两位 Reviewer 完全一致 [AGREE]（无任何 [REBUT]）：

1. **Interaction framing 矛盾**（C1）——"normalization-dependent gradient flow effect" 暗示交互，但 ANOVA 交互项为零。本轮最重要的新发现（R1 识别，R2 初审遗漏后完全认同）
2. **统计功效**（C3）——n=3-4 power 不足，因果声明无法支撑。C1+C3 构成最致命组合
3. **v1/v2 confound**（C2）——codebase 效应量（8.6pp）大于实验效应量（4.2pp）
4. **格式违规**（C4）——Limitations 不在正文 + 超页，desk reject 风险
5. **BN 假说未验证**（W7）——低成本 eval mode 实验应执行
6. **λ₀ 敏感度缺失**（W5）——需消融实验
7. **梯度正交矛盾**（W2）——机制解释存在核心空白
8. **单一 benchmark**（W4）+ **标题过宽** + **Conclusion 无限定**

R1 独有关键贡献：C1（interaction framing 矛盾）——直接动摇论文中心叙事结构
R2 独有关键贡献：C4 中格式违规的精确识别（Limitations 位置 + 超页量化）——desk rejection 级别硬伤

## Reviewer Divergence（分歧点）

本轮无分歧。Reviewer 2 对 Reviewer 1 所有观点均 [AGREE]，无 [REBUT]。

---

## Questions（需作者回应）

1. **Interaction framing**: 论文核心框架 "normalization-dependent gradient flow effect" 在统计学上是 interaction effect，但 ANOVA interaction F(1,10)=0.10, p=0.76。为什么选择了一个暗示交互的术语来描述两个 additive main effects？
2. **Statistical inference**: ANOVA 主效应 p=0.104 和 p=0.060 均不显著。论文通过效应量叙事（"large d"）规避这一事实。在何种统计框架下，这些结果足以支撑 "large effect" 的因果结论？
3. **Codebase stability**: v1→v2 codebase revision（无超参数/架构变化）导致 8.6pp 偏移和效应模式翻转。如何论证 v2 下的 practical guidelines 在其他合理实现中仍然成立？
4. **λ₀ dependence**: gradient flow 效应是否依赖于 λ₀=0.01 这一特定选择？若 λ₀=0.001 或 λ₀=0.1，结论是否改变？
5. **Orthogonality paradox**: gradient cosine similarity ≈ 0 排除了 gradient conflict，但 gradient flow 仍被报告为有害。"Indirect effect through optimization trajectory" 有无任何直接证据？

---

## Missing References

两位 Reviewer 共识应补充：
1. **Montgomery — Design and Analysis of Experiments** — factorial design 方法论经典教材 [强烈建议]
2. **Anderson (2001) — Permutation tests for multi-factorial experiments** — ANOVA 非参数替代 [建议]
3. **Bilen & Vedaldi (2017)** — task-specific BN，BN 假说的直接前驱 [强烈建议]
4. **Maninis et al. (2019, ASTMT)** — task-specific normalization in multi-task vision
5. **Rebuffi et al. (2018)** — domain-specific BN adapters
6. **Sener & Koltun (2018, MGDA)** — multi-objective optimization
7. **Li et al. (2016) / Ioffe (2017)** — BN fine-tuning 问题
8. **π₀ (Black et al. 2024)** — 当前代表性 VLA 架构 [强烈建议]
9. **Octo (Team Octo 2024)** — 当前代表性 VLA 架构

---

## External Review

**状态**: 未请求。本轮未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: 已完成 (2026-05-28 11:34–11:37 UTC)

**Critical (1)**:
- **Page 12**: 仅 2 条参考文献（[45]-[46], ~6 行），页面剩余 ~85% 空白。审稿人翻到整页空白会留下 "论文未完成" 或 "空间浪费" 的负面印象。建议将附录标题移到本页开始或调整分页。

**Warning (4)**:
- **Pages 3-4**: 连续 2 页纯文本（Related Work + Method 开头），仅 page 4 底部有公式(1)。视觉疲劳风险。考虑提前 Table 1 或加入架构示意图。
- **Pages 5-7**: 连续 3 页密集出现 3 tables + 1 figure，与 pages 3-4 的纯文本形成不均匀对比。
- **Page 16**: Figure 4 子图 axis label 和 legend 字号偏小（约正文 60-65%），打印或低分辨率下可能难辨认。建议增大字号或减少每子图线条数。
- **Page 19**: 最后一页仅 ~11 行文字（Limitations 续文），~80% 空白。

**Info (20)**: 
- Figure/Table 位置与首次引用匹配良好，无 float 漂移
- 正文 2 figures + 3 tables = 5 display items（0.56/页），合理范围低端
- 附录额外 3 figures + 4 tables，补充材料充分
- booktabs 格式规范，无竖线，专业
- Figure 1 多面板设计信息密度高，caption 详细自包含
- Figure 2 清晰简洁，颜色编码可区分，error bars 标注清晰
- 无 overfull hbox 或 margin 溢出
- 行号已启用（投稿格式），符合匿名审稿要求
- 参考文献 [1]-[46] 连续，无跳号或未解析引用

---

## Overall Assessment

**评分: 4/10 — Weak Reject**
**置信度: 高（两位 Reviewer 全 [AGREE] 共识，无任何分歧）**

论文提出了重要且及时的研究问题，factorial 设计方向正确，v1/v2 codebase sensitivity 的坦诚报告值得肯定。

但四个 critical 问题的复合效应使论文在当前状态下不达 CoRL 接收标准：

1. **框架矛盾**（C1）——论文核心概念 "normalization-dependent gradient flow effect" 暗示交互效应，但论文自身 ANOVA 显示交互为零（F=0.10, p=0.76, η²&lt;0.01）。这不是措辞微调——它影响论文的中心叙事结构和 Contribution 1 的有效性。正确的框架是 "两个独立的 additive main effects"。

2. **统计功效**（C3）——n=3-4 的 power 不足以支撑任何因果声明。ANOVA 主效应 p-values 均不显著（0.104, 0.060），效应量 CI 包含零。论文通过 "large d" 叙事回避了推断不显著的事实。Hedges' g 校正后 d=0.93→g≈0.75，跌破 "large" 阈值。

3. **格式违规**（C4）——Limitations 不在正文 + 正文超 8 页，在 CoRL 严格页数限制下可能直接 desk reject。

4. **v1/v2 confound**（C2）——codebase 效应量（8.6pp）大于实验效应量（4.2pp），content irrelevance 仅有已知存在 bug 的 v1 证据。

**C1+C3 构成最致命组合**：论文声称发现了依赖于 normalization 的效应（暗示交互），但 ANOVA 说没有交互（p=0.76）——而这个 ANOVA 本身也没有足够 power 检测交互（&lt;20%）。论文陷入无法自洽的困境：要么承认效应是 additive（推翻核心框架），要么坚持交互框架（需更大样本量证明）。

**修复路径**：若能 (a) 修正框架为 additive main effects、(b) 增加样本量至 n≥5-8、(c) 解决格式问题、(d) v2 验证 content irrelevance 或降级处理，论文有潜力提升至 borderline accept。研究方向正确，需要更扎实的执行。

---

## Detailed Comments

### Abstract
- "normalization-dependent gradient flow effect" → 改为描述两个 additive main effects
- "A 2×2 ANOVA confirms additive main effects" → 不能 "confirm"，只能说 "interaction was not detected"
- "Cohen's d = -0.93, large" → 应改为 Hedges' g 并注明 CI
- Content irrelevance caveat（"v1 codebase"）位置正确，但建议补充 "verification under v2 is pending"

### Introduction
- Contribution 1 "Normalization-dependent gradient flow effect"：interaction framing 与 ANOVA 结果矛盾，需重写为 additive main effects
- Contribution 2 "the first systematic factorial comparison"：factorial design 是标准方法，"first" 声明需验证或弱化
- L5 "single-factor ablations cannot detect interactions"：论文自己的 factorial 也未检测到交互——这一反讽需要在修订中处理

### Method
- "twelve conditions varying five factors" → 修正为 "a 2×2 factorial core (gradient flow × normalization) supplemented by single-factor ablations across three additional factors"
- λ₀=0.01 的选择需补充敏感度分析或在 Limitations 中明确讨论

### Results
- 所有 Cohen's d → Hedges' g + CI
- "degrades"、"reduces" 等因果语言 → 降级为 "is associated with"、"co-occurs with"
- ANOVA p-values（0.104, 0.060）应在正文中明确报告并讨论不显著的含义，而非仅在 Appendix 中出现
- Table 3 caption 建议加注 "the design is underpowered for interaction detection"

### Discussion
- BN hypothesis "hypothesize but do not directly test"：建议执行 eval mode 验证或更明确标注为 "speculative"
- Codebase sensitivity 作为 "independent finding"：需同时承认这削弱 practical guidelines 的外部效度
- Gradient orthogonality 支撑 content irrelevance 的逻辑需删除或重写——orthogonality 在 v1 下也成立但结论仍翻转

### Conclusion
- "Practitioners should omit auxiliary spatial heads"：加限定（LoRA fine-tuning, SafeLIBERO, OpenVLA-7B）
- Content irrelevance：确认编译 PDF 中 v1 caveat 与源码一致

### Related Work
- 补充 task-specific BN 文献线（Bilen & Vedaldi 2017, Maninis et al. 2019, Rebuffi et al. 2018）
- 补充 Montgomery (factorial design) 和 Anderson 2001 (permutation tests)
- 补充 π₀ 和 Octo

### Format
- Limitations 从 Appendix H 移入正文
- 压缩正文至 8 页以内
- Page 12 参考文献后空白需解决
- Figure 4 字号适当增大