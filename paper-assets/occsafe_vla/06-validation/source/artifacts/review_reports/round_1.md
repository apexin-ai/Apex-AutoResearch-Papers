---
round: 1
review_mode: continue
overall_score: borderline reject (5/10)
timestamp: 2026-05-28T11:06:17.463014+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 2（Continue 模式）

**项目**: occsafe_vla
**论文**: "Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? An Empirical Investigation"
**目标 Venue**: CoRL 2026
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计；R2: 新颖性 + 完整性 + 格式）
**轮次**: 1 轮初审 + 交叉分享，共识充分，无需第二轮
**外部审稿**: 未请求
**视觉审查**: 已完成（见附录）

---

## Summary

论文研究辅助空间监督（occupancy prediction）对 VLA 模型碰撞避免安全性的影响。通过 OpenVLA-7B + OFT + LoRA rank 32 在 SafeLIBERO Level I 上的 12 条件 factorial 研究，发现 normalization-dependent gradient flow effect：BN + gradient flow 降低 CAR（0.725 vs Vanilla 0.745, d=-0.93），LN + gradient flow 则无害（0.773）。论文提出 BN running statistics 假说解释该现象，并给出实践指南。

---

## Strengths

- **S1**: 研究问题重要且及时——在 15+ 篇空间 VLA 方法均假设"更好的空间感知→更安全"的背景下，首次系统验证该假设对碰撞安全的影响
- **S2**: 坦诚报告 v1→v2 codebase sensitivity（同 seed 偏移 8.6pp）——大多数论文会隐藏此类信息，这种透明度值得肯定
- **S3**: 梯度分析（CKA、per-layer gradient norms、cosine similarity）提供了超越单纯指标对比的机制洞察
- **S4**: Factorial 设计在 VLA auxiliary supervision 文献中填补方法论空白——该领域此前完全依赖单因子 ablation
- **S5**: 实验设计中的 v1/v2 分离处理（Table 分区、★标记、ΔCAR="---"）显示了对数据完整性的认真态度

---

## Weaknesses

### Must-Fix（Critical — 需解决后方可接受）

**N1: 统计功效不足以支撑核心因果声明** [共识: R1+R2]
- n=3-4 per cell，达到 power=0.80 需 n≥8（G*Power, 2×2 ANOVA, α=0.05）。当前 power 估计仅 ~0.35-0.45
- Cohen's d=0.93（n₁=n₂=3）的 95% CI 约 [-0.8, 2.7]，不能排除零效应甚至反向效应
- ANOVA 两个主效应 p=0.104 和 p=0.060，在任何常规标准下均不显著
- Discussion 使用因果语言（"gradient flow drops CAR below the Vanilla baseline"），超出关联性证据的支撑范围
- **修复方案**: (a) 增加样本量至 n≥5（理想 n≥8）；(b) 将所有因果语言降级为关联性描述（"is associated with"）；(c) 报告 Hedges' g 和 bootstrap CI 替代 Cohen's d

**N2: Content irrelevance 声明仅有 v1 证据** [共识: R1+R2]
- v1→v2 Full OCC CAR 从 0.797 降至 0.725（7.2pp shift），crossover 效应在 v2 下完全消失
- Discussion line 13 承认 "whether it persists under v2 remains open"
- 间接支撑（gradient orthogonality）逻辑有缺陷：orthogonality 在 v1 下也成立，但 v1→v2 的定性结论仍翻转
- 在 v1 存在已知 bug 且定性结论因 bug 修复而翻转的情况下，将 v1-only 发现写入 Abstract 和 Contribution list 不当
- Introduction 贡献(1)（line 20）用 "under the conditions tested" 而非明确 "under v1 codebase"；Conclusion（line 4）完全无限定
- **修复方案**: (a) v2 下重训 Random OCC 验证 content irrelevance；或 (b) 从 Abstract/Contributions 移除，降级为 Discussion 中的 preliminary observation + 明确 v1 caveat

**N3: Limitations 不在正文内 — CoRL 格式违规** [共识: R1+R2]
- discussion.tex line 19 仅有指针句 "Limitations are in Appendix"，全文在 Appendix H
- CoRL 2026 要求 Limitations 计入 8 页正文
- 明确格式违规，可能导致 desk reject
- **修复方案**: 将 Limitations 从 Appendix H 移入正文

**N4: 正文超过 8 页** [共识: R1+R2]
- PDF 第 8 页被 Discussion（Section 5）占满，Conclusion（Section 6）起始于第 9 页
- 加上需移入的 Limitations（约 1 页），总正文量约 10 页
- 需压缩至少 2 页才能满足 CoRL 8 页限制
- **修复方案**: 压缩 Related Work、Method 描述、Discussion 冗余段落；考虑将部分分析移入 Appendix

---

### Should-Fix（Warning — 强烈建议修复）

**W1: Factorial 设计不完整，声明过度** [共识: R1+R2]
- Introduction 声称 "twelve conditions varying five factors"，但完整 factorial crossing 仅限 2×2（gradient flow × normalization）
- Label content、reference frame、temporal extent 均为单因子 ablation，不在 factorial 交叉中
- Contribution 2 将 factorial methodology 列为独立贡献不恰当——factorial design 是标准统计方法
- **建议**: Method Section 3.1 修正为 "2×2 factorial core + single-factor ablations"；Contribution 2 降级为研究设计特色

**W2: Cohen's d 小样本偏差未校正** [共识: R1+R2]
- n₁=n₂=3 时 Hedges' g 校正因子 J≈0.81，d=0.93 校正后 g≈0.75
- 从 "large" 边界（0.80）滑入 "medium-to-large"，改变叙事力度
- **建议**: 正文所有效应量改报 Hedges' g

**W3: 标题与实验范围不匹配** [共识: R1+R2]
- 标题 "Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer?" 暗示对整个 VLA 类别的回答
- 实验仅覆盖 OpenVLA-7B + OFT + LoRA rank 32 + SafeLIBERO Level I（单一架构 + 单一 benchmark）
- Conclusion "Practitioners should omit auxiliary spatial heads" 无限定条件
- **建议**: 标题加副标题限定范围；Conclusion 建议加 LoRA-specificity 和 benchmark 限定

**W4: BN running statistics 假说未直接验证** [共识: R1+R2]
- Discussion 提出 BN running statistics 机制假说作为核心解释，但未验证
- 论文声称发现 "normalization-dependent gradient flow effect" 作为核心贡献，却未验证所提出的机制，形成 claim-evidence gap
- **建议**: 在已训练 v2 模型上执行 BN eval mode（frozen running stats）或 momentum=0 消融。低成本实验，无需重新训练

**W5: Codebase sensitivity 削弱实践指导价值** [共识: R1+R2]
- 同 seed v1→v2 偏移 8.6pp，接近核心效应量（gradient flow effect = 4.2pp）——实现噪声与信号同量级
- 论文将此框架为 "independent finding"，但这是双刃剑：如果实现细节能改变定性结论，当前 v2 结论也可能在 v3 下再次改变
- Practical guidelines 需要在特定实现下稳健才有实际价值
- **建议**: 降低 guidelines 的普适性声明；明确标注适用范围

**W6: 缺少 MTL-BN 交互相关文献** [共识: R1+R2]
- 缺少直接讨论 "shared BN statistics in multi-task settings cause interference" 的关键前驱：
  - Bilen & Vedaldi (2017): task-specific BN
  - Maninis et al. (2019, ASTMT): task-specific normalization in multi-task vision
  - Rebuffi et al. (2018): domain-specific BN adapters
  - Sener & Koltun (2018, MGDA): multi-objective optimization
- 缺少当前 VLA 代表性架构：π₀ (Black et al. 2024), Octo (Team Octo 2024)
- **建议**: Related Work 补充 task-specific BN 文献线；Discussion 引用 MGDA

**W7: Introduction/Conclusion 中 content irrelevance 缺 v1 caveat** [R1 发现，R2 初审遗漏]
- Abstract 和 Section 4.1 有 v1 caveat ✓
- Introduction 贡献(1)（line 20）写 "under the conditions tested" 而非明确 v1 — 读者不会从此措辞理解为仅限 v1
- Conclusion（line 4）"spatial label content showed no detectable effect" 完全无限定
- Introduction 和 Conclusion 是读者最先和最后看到的位置
- **建议**: 两处均显式标注 "observed under v1 codebase"

---

## Reviewer Consensus（交叉分享共识）

以下问题两位 Reviewer 完全一致 [AGREE]：
1. **统计功效**是论文最大软肋——n=3-4 无法支撑因果声明，p-values 不显著被效应量叙事掩盖
2. **Content irrelevance** 缺乏 v2 证据，不可列为确立贡献
3. **格式违规**（Limitations 不在正文 + 超页）可能导致 desk reject
4. **Factorial 声明过度**——实为 2×2 核心 + 单因子 ablation
5. **BN 假说**需直接验证，低成本 eval mode 实验应执行
6. **标题/Conclusion** 范围过宽，需限定

## Reviewer Divergence（分歧点）

**D1: λ(t) 指数衰减的功能形式** [R1-W3]
- R1: Should-Fix——应测试 linear/step/cosine schedule
- R2: REBUT——λ(t) 不在核心因果路径上（BN/LN 差异作用于 normalization statistics 耦合，非 loss weight schedule）；论文 Appendix H 已在 Limitations 提及。降级为 future work 更合适
- **Director 判断**: 采纳 R2 立场。loss weight schedule 确实与 normalization mechanism 在不同 causal pathway 上，作为 Limitations 中的 future work 充分

**D2: 碰撞检测阈值 10⁻³ 的敏感性** [R1-W4]
- R1: Should-Fix
- R2: AGREE 但认为重要性较低——阈值沿用 SafeLIBERO benchmark 定义，非论文自定义
- **Director 判断**: 降级为 info。在 Appendix 补充一句物理尺度解释即可

---

## Questions（需作者回应）

1. 论文声称 gradient orthogonality "间接支撑" content irrelevance 在 v2 下仍成立。既然 orthogonality 在 v1 下也成立但定性结论仍因 codebase 修复而翻转，请解释为什么 orthogonality 的稳定性能担保 content irrelevance 的稳定性？
2. ANOVA 主效应 p=0.104 和 p=0.060 均不显著。论文主要依赖效应量叙事回避这一事实。请明确：在何种统计框架下，这些结果足以支撑 "large effect" 的结论？
3. 如果 v1→v2 codebase revision（非任何超参数/架构改变）能导致 8.6pp 偏移和效应模式翻转，如何论证当前 v2 下的 practical guidelines 在其他合理实现中仍然成立？
4. Contribution 2 将 factorial methodology 列为独立贡献。Factorial design 是标准统计方法（Fisher, 1935）。请说明其在 VLA 文献中的具体方法论创新点。

---

## Missing References

两位 Reviewer 共识应补充：
1. **Bilen & Vedaldi (2017)** — task-specific BN，BN 假说的直接前驱 [强烈建议]
2. **Maninis et al. (2019, ASTMT)** — task-specific normalization in multi-task vision
3. **Rebuffi et al. (2018)** — domain-specific BN adapters
4. **Sener & Koltun (2018, MGDA)** — multi-objective optimization 核心方法
5. **π₀ (Black et al. 2024)** — 当前代表性 VLA 架构
6. **Octo (Team Octo 2024)** — 当前代表性 VLA 架构

---

## External Review

**状态**: 未请求。本轮未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: 已完成 (2026-05-28 10:46–10:49 UTC)

**Critical (1)**:
- **Page 12**: 引用仅占页面顶部 ~10%（[45]、[46] 两条），剩余 ~90% 纯空白。建议将 Appendix A 提前或调整排版

**Warning (3)**:
- **Page 19**: 最后一页仅 ~11 行文字（Limitations 续文），~85% 空白
- **Page 3-4**: 连续 2 页无 figure/table（Related Work 纯文本 + Method 仅有公式(1)）。考虑加入架构示意图或提前 Table 1
- **Page 8**: Discussion 整页纯文本，无 display item

**Info (9)**:
- Page 2: Figure 1 作为视觉锚点位置良好，caption 偏长（~8-9 行）
- Page 6: Table 2 格式规范（booktabs、±标准差、ΔCAR 列清晰）
- Page 7: Table 3 + Figure 2 同页，视觉密度合理，建议确认色盲安全性
- Page 15-16: Figure 3/4 轴标签和图例文字偏小（建议 ≥9pt），灰度打印下可能难以区分
- 全文: 无 margin 溢出、公式渲染错误、heading 孤悬等排版缺陷。主体正文 2 figures + 3 tables = 5 个 display items，偏下限但可接受

---

## Overall Assessment

**评分: 5/10 — Borderline Reject**
**置信度: 高 (两位 Reviewer 高度共识)**

论文提出了重要且及时的研究问题，factorial 设计填补了 VLA safety 文献的方法论空白，对 codebase sensitivity 的坦诚报告值得肯定。

但当前版本存在多个严重问题：

1. **统计功效**是根本性缺陷——n=3-4 无法支撑论文的因果声明，ANOVA p-values 均不显著，效应量 CI 包含零。这不是"样本量偏小"的程度问题，而是"当前数据不足以得出论文声称的结论"的定性判断。
2. **格式违规**（Limitations 不在正文 + Conclusion 超页至第 9 页）在 CoRL 严格执行页数限制的情况下可能直接导致 desk reject。
3. **Content irrelevance** 作为三大贡献之一，仅有已知存在 bug 的 v1 证据支撑，且 v1→v2 已导致其他效应模式翻转。
4. **Codebase sensitivity**（实现噪声 8.6pp vs 信号 4.2pp）从根本上削弱了 practical guidelines 的可信度。

若统计功效问题（增加样本量至 n≥5-8）和格式问题（压缩至 8 页 + Limitations 移入正文）能得到解决，论文有潜力提升至 borderline accept。Content irrelevance 需要 v2 验证或降级处理。

---

## Detailed Comments

### Abstract
- "Cohen's d = -0.93, large"：应改为 Hedges' g 并注明 CI
- "Spatial label content shows no detectable effect on safety (observed under v1 codebase)"：caveat 位置正确，但 Abstract 读者可能不理解 v1 codebase 的含义——建议补充一句 "under the original codebase; verification under the corrected codebase (v2) is pending"

### Introduction
- Line 20 贡献(1)："under the conditions tested" 应改为 "observed under v1 codebase"
- 贡献(2) "the first systematic factorial comparison"：factorial design 是标准方法，"first" 的声明需谨慎

### Method
- Section 3.1：修正 "twelve conditions varying five factors" 为 "a 2×2 factorial core (gradient flow × normalization) supplemented by single-factor ablations across three additional factors"
- λ(t) 指数衰减：当前描述充分，无需测试其他 schedule（仅在 Limitations 中提及即可）

### Results
- 所有效应量 Cohen's d → Hedges' g
- ANOVA p-values（0.104, 0.060）应在正文中明确报告并讨论其不显著的含义，而非仅在 Appendix 中出现
- 因果语言（"degrades", "drops", "reduces"）全部降级为关联性描述（"is associated with", "co-occurs with"）

### Discussion
- BN running statistics 假说需直接验证（eval mode 消融）或明确标注为 "unverified hypothesis"
- "constitutes an independent finding"（codebase sensitivity）：此论证需更谨慎——同时承认这削弱了 practical guidelines 的外部效度
- Content irrelevance 的间接支撑逻辑（gradient orthogonality → content irrelevance 跨 codebase 稳定）需删除或重写——orthogonality 在 v1 下也成立但结论仍翻转

### Conclusion
- Line 4："spatial label content showed no detectable effect" 需加 v1 caveat
- "Practitioners should omit auxiliary spatial heads"：需加限定（LoRA fine-tuning, SafeLIBERO, OpenVLA-7B）

### Related Work
- 补充 task-specific BN 文献（Bilen & Vedaldi 2017; Maninis et al. 2019; Rebuffi et al. 2018）
- 补充 MGDA（Sener & Koltun 2018）
- 补充 π₀ 和 Octo

### Format
- Limitations 从 Appendix H 移入正文
- 压缩正文至 8 页以内
- Table caption 加注 "v1 and v2 rows are not directly comparable due to codebase differences (see Appendix E)"
- Appendix 中碰撞检测阈值补充物理尺度解释