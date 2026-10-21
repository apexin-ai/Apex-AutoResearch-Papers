---
round: 7
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-25T21:39:59.073420+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 7 审稿报告 — EMNLP 2026 (ARR May cycle)

**论文**: "Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction"
**Venue**: EMNLP 2026 via ARR May 2026 cycle
**审稿模式**: Fresh（重新审稿）
**Reviewer**: R1（方法严谨性 + 理论 + 实验设计）, R2（新颖性 + 完整性 + Related Work + 写作）

---

## Summary

本文诊断了 step-independent agent RL（GRPO + 固定窗口分解）中的两种结构性失败机制：策略信息丢失（M1，窗口截断导致恒定性能天花板）和优势符号误归因（M2，group normalization 使梯度符号反映 episode 结果而非局部动作质量）。通过 3-of-4 部分析因实验在 ALFWorld 上分离机制贡献，并提出 episode-level GRPO 作为结构性修复（11 seed 中 36% 实现显著 OOD 泛化，均值 17.7% vs SFT 6.72%）。理论分析在 binary reward 假设下推导了错误符号梯度的上界。

---

## Strengths

**S1. M1/M2 诊断框架有概念贡献和实用价值。** [R1-S1, R2-S1, 共识] 双机制分解（推理层 M1 vs 训练层 M2，恒定天花板 vs 累积退化）为从业者提供了有操作性的诊断思路，且能正确预测并发方法（HCAPO, GiGPO）的成功（Section 6）。Appendix E 的 method selection guide 有实践指导意义。

**S2. 部分析因实验设计方法学意识强。** [R1-S2, R2-S1, 共识] A→B→D 比较链 + 三类验证指标（sign-episode correlation 99.6%, credit agreement 52.1%, P(correct|update) ≤19.1%）构成多角度证据体系。Discount factor sweep 排除了折扣衰减作为替代解释。Break-even magnitude ratio 分析（实测 2.6 < 理论需要 4.2, Section 5.4）有洞察力。

**S3. 科学诚实的报告标准。** [R1-S5, R2-S2, 共识] 坦诚披露 36% 泛化率、seed 变异性、Cell C 不稳定性、单 seed 跨环境验证的局限。11-seed 评估（含 Fisher exact test, Wilson CI, unified step-5 defense, eval variance analysis）超过领域 3-5 seed 标准。

**S4. 理论与实验对照验证完整。** [R1-S4, R2-S3, 共识] Propositions 1-2 在 binary reward 下提供 closed-form 上界，实证三指标分别从不同角度确认。论文区分了 binary caliber（deterministic misattribution）与 penalty caliber（near-random noise），虽有 gap 但分析框架清晰。

**S5. 写作质量整体较高。** [R2-S4, R1 agree] Figure 1 高效传达核心思想，论文结构从诊断→理论→实验逻辑流畅。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [Critical, 共识]: Cell A vs Cell B 操作差异不精确——"消除 M2" 声称存在根本性 confound**
- R1-W3 (Critical), R2 交叉后强烈 AGREE 并下调 Soundness
- 由于 R_w = γ^(N-w) · R_episode（Eq.2），Cell A per-window GRPO 归一化后 advantage sign 与 Cell B episode-level advantage 近似相同（折扣因子在分子分母中抵消）。Cell B 使用 episode-level advantage 时，失败 episode 的所有 token 仍获负 advantage——**这正是 M2（sign misattribution）的定义**。
- 因此 A→B 的改善可能来自：(a) 消除累积错误放大（N 次独立错误→1 次错误）；(b) per-window vs per-episode KL penalty 差异；(c) effective batch size 差异——而非"消除 M2"。
- **这是因果推断链第一步的解释基础。** 如果 Cell B 并未真正消除 M2，则 "dual mechanism diagnosis" 的实验支撑被显著削弱。
- **Round 7 新发现。**

**N2 [Critical, 共识]: Cell C 缺失使析因不完整，可能暗示 M1/M2 非加性交互**
- R1-W1 (Critical), R2 初审 W3 (Should-Fix) 交叉后升级为 Critical AGREE
- Cell C（full trajectory + step-level advantage; only M2 active）在 6 组超参数下均 NaN 发散。无 Cell C：(a) 无法独立验证 M1 效应（需 C→D）；(b) 无法估计 M1×M2 交互效应；(c) Cell C 发散暗示 M1 可能通过限制梯度方差无意中稳定训练——即 M1 同时是 failure mechanism 和 stabilizer，与"两个独立失败机制"框架矛盾。
- 论文 Discussion 承认 "our factorial interpretation assumes approximate separability"，但标题 "Dual Mechanism Diagnosis" 暗示了比证据更强的因果确认。
- 连续 7 轮提出。

**N3 [Critical, 共识]: 析因条件仅 2 seeds，Cell B OOD 仅 1 seed，统计效力严重不足**
- R1-W2 (Critical), R2 AGREE
- 论文自身 11-seed 评估展示了三种结果类型（27% collapsed, 36% stagnant, 36% generalized），OOD 从 8.2% 到 30.6%——**反过来证明 n=2 无法可靠代表**。Cell B 的 OOD 5.97% 实际仅 1 seed（Table 1 脚注），是因果链关键中间节点却缺乏统计基础。
- 连续 2 轮提出。

**N4 [Critical, R2 Critical + R1 AGREE (建议降为 Should-Fix)]: Abstract/Intro overclaiming**
- R2-W2 (Critical), R1 强烈 AGREE（尤其中位数分析），但认为核心诊断贡献不受影响
- "structurally eliminates both failure modes" 技术正确但与 36% seed 泛化率并置时严重误导
- 11 seed OOD **中位数 12.69%**，远低于论文报告的 mean 17.7%（右偏分布，被 4 个 generalized seeds 拉高）。过半数 seeds 未达统计显著 OOD 改善
- 单 seed 8B (90.3% OOD) 证据弱——8B SFT baseline 已 80.6%，增量 ~10pp 与 1.7B ~11pp 相似

**N5 [Critical→Should-Fix, 分歧]: Episode-level GRPO 方法论新颖性有限**
- R2-W1 (Critical), R1 AGREE 但建议降为 Should-Fix
- 标题含 "Episode-Level Correction" 但修复本质是恢复标准 GRPO 原始设计（Section 3.4 自陈）
- **分歧**: R1 认为诊断论文的修复简洁性反而是优势（Occam's razor），问题在于 framing 而非内容；R2 认为缺乏独立方法论价值是结构性问题
- 连续 7 轮提出。

### Should-Fix（影响评分但不一票否决）

**W1 [Warning, 共识]: Binary reward 理论与 ternary reward 实验之间的桥接不够严格**
- R1-W4, R2-W5
- 19.1%（binary bound）vs 52.1%（ternary credit agreement）反映**质的不同**失败模式——deterministic misattribution vs near-random noise。论文承认 "measure different quantities" 但缺乏 ternary 下的 formal bound。
- 连续 7 轮提出。

**W2 [Warning, 共识]: 未与并发方法做 head-to-head 实验对比**
- R1-W6, R2-W6
- Section 6 声称 "unified explanation" 但纯属 post-hoc rationalization。真正验证需在相同设置下实验比较，或框架对新方法的先验预测。
- 连续 6 轮提出。

**W3 [Warning, 共识]: 跨环境验证薄弱**
- R1-W5, R2-W4
- ScienceWorld 单 seed，仅展示 collapse（不令人惊讶），未报告 episode-level 对比。存在 scale confound。
- 连续 4 轮提出。

**W4 [Warning, R1 Should-Fix, R2 Partially Agree]: Proposition 1 中 p 的条件化不够精确**
- R1-W7: locally correct actions 应使 P(episode success | correct window) = p_w > p，独立性假设未明确
- R2: 技术正确但低 p regime 下不改变定性结论

### Minor

- **M1** [R1, R2 共识]: Table 1 Cell A 缺 OOD 评估，Cell B OOD 仅 1 seed——主表关键条件缺失 OOD 数据
- **M2** [R2, R1 AGREE]: Figure 3(b) h=10 两 seed 差异大（6.25% vs 21.9%），仅报告均值 14.1% 掩盖不确定性
- **M3** [R1, R2 AGREE]: Eq.6 假设 g+/g- 对称但实测非对称（ratio=2.6）；break-even 分析已补充但 Eq.6 表述应注明
- **M4** [R2, R1 AGREE]: Equation 2 中 γ=0.95 仅在 Appendix B 给出，主文未提
- **M5** [R1, R2 AGREE]: Cohen's h=0.041 的 small-effect threshold 0.2 应显式引用
- **M6** [R1, R2 AGREE]: Appendix H early signal analysis n=4 per group，检验效力极低，应标注为 exploratory
- **M7** [R2-M3, R1 REBUT]: 12.5% SFT baseline 是否偏低——R1 论证低 p 是 M2 最严重区间，但 8B (p≈80.6%) collapse 可能由 M1 主导，暗示框架在不同 baseline 下解释力可能不统一

---

## Reviewer Consensus [AGREE]

1. **Overall 评分**: 两位 Reviewer 初审均给 3.0 (Findings)。R2 交叉后下调至 2.5 (Borderline Findings)，R1 维持 3.0。
2. **Cell C 缺失是核心弱点**: 两位均认为 Critical，且 Cell C NaN 可能暗示 M1/M2 非加性交互
3. **2-seed 析因统计效力不足**: 两位均认为 Critical，Cell B OOD 仅 1 seed 尤为薄弱
4. **Overclaiming**: "structurally eliminates" vs 36% 泛化率矛盾，中位数 12.69% 远低于 mean 17.7%
5. **Binary/ternary theory gap**: 连续 7 轮未解决，两位共识
6. **缺乏并发方法实验对比**: 连续 6 轮未解决，两位共识
7. **诊断框架有实用价值**: 两位均肯定 M1/M2 框架的概念贡献和实践指导意义
8. **科学诚实度**: 两位均肯定透明报告标准

## Reviewer Divergence [REBUT]

1. **Excitement**: R1 给 3.0（诊断框架对从业者有实际指导价值，excitement 应基于 insight 质量而非修复方案新颖性）；R2 给 2.5（方法新颖性不足是结构性问题）
2. **N5 严重性**: R1 认为 Should-Fix（修改 framing 即可）；R2 认为 Critical（缺乏独立方法论价值）
3. **M7 低 baseline 普适性**: R1 REBUT（低 p 是 M2 最严重区间，合理实验选择）；R2 认为可能影响诊断普适性。R1 进一步指出 8B (p≈80.6%) 的 collapse 可能由 M1 主导而非 M2，暗示双机制框架在不同 baseline 水平下解释力不统一——这是一个有价值但未充分讨论的延伸分析

---

## Questions（需作者澄清）

**Q1** [R1-Q1, 关键]: Cell B "episode-level advantage" 的精确实现是什么？每个 episode 计算单个 Â 应用于所有 tokens？如果是，请解释为何在 sign 模式与 Cell A 相同的情况下表现出质的不同。

**Q2** [R2-Q1, R1 AGREE]: 11 seed OOD success rate 的中位数是多少？（计算得 12.69%，请确认）

**Q3** [R1-Q2]: 27% collapsed seeds 在 episode-level 下的失败模式是什么？如果 episode-level 已"消除 M2"，collapse 来自第三种机制？

**Q4** [R1-Q4, R2 AGREE]: 8B 90.3% OOD vs 1.7B 17.7%——差异来自 scale 还是方法？8B SFT baseline 80.6% 意味着增量仅 ~10pp。

**Q5** [R2-Q3]: Cell C NaN 是否代表 M1/M2 框架外的独立现象？M1 是否同时有正则化作用？

**Q6** [R2-Q6, R1 AGREE]: REINFORCE++ 为何不帮助？能否分离 normalization 方式 vs reward sparsity 的影响？

---

## Missing References

两位 Reviewer 共识：
1. **RLOO** (Ahmadian et al., 2024, "Back to Basics") — 与 GRPO group normalization 和 episode-level 设计直接相关 [R1, R2 共识]（注：references.bib 已含 ahmadian2024back，但 Related Work 可能未充分讨论其与 episode-level GRPO 的关系）

R2 建议、R1 部分同意：
2. **COMA** (Foerster et al., 2018) — Appendix A.3 讨论了多智能体类比但未引用具体方法。加入可增强 scholarly completeness，但非必须。

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: ✅ 完成（8 个 info 级别发现，0 critical，0 warning）

主要发现：
- Page 3: Figure 2 散点图坐标轴标签和图例字号偏小（约正文 60%），建议放大至 70%+
- Page 5: Figure 3(b) x 轴标签与数值标签间距较紧，部分数值字号偏小
- Page 7: Table 1 "Single seed" 脚注标记（†）字号较小，审稿人可能不易注意
- Page 8: 页面极密集（Table 2 + Figure 5 + Conclusion + Limitations 全挤一页），视觉呼吸感不足；Limitations 仅 ~5 行可能显得仓促
- Page 8: Figure 5 颜色区分在色盲模式下可能混淆（绿色/橙色）
- Appendix: Figure 6/7/8 面板标签字号偏小但可辨认；Figure 8 y 轴标签文字过长

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 (交叉后) | 综合 |
|------|-----|-------------|------|
| **Soundness** | 3.0/5 | 2.5/5 | 2.75/5 |
| **Excitement** | 3.0/5 | 2.5/5 | 2.75/5 |
| **Reproducibility** | 3.5/5 | 4.0/5 | 3.75/5 |
| **Confidence** | 4/5 | 4/5 | 4/5 |
| **Overall** | 3.0 | 2.5 | **3.0 (Findings)** |

### 综合判断

**Overall: 3.0 — Findings**

M1/M2 诊断框架是对 step-independent agent RL 训练崩溃的有价值的概念贡献，实验方法学（部分析因 + 多指标验证 + 11-seed 评估）和科学诚实度均超过领域平均水平。

但三个核心问题制约了评分：
1. **Cell A/B 操作差异 confound**（Round 7 新发现）——Cell B 可能并未真正消除 M2，因果推断链第一步的解释基础存疑
2. **Cell C 缺失 + 2-seed 统计效力不足**（连续 7 轮）——析因设计不完整且样本量不支撑因果声称
3. **Overclaiming**——abstract/intro 的 framing 与实际证据强度不匹配（中位数 12.69% vs 报告均值 17.7%，36% 泛化率 vs "structurally eliminates"）

论文适合作为 Findings 发表：诊断框架对社区有参考价值，诚实报告值得肯定，但因果声称的实验基础需要加强才能达到主会议标准。

### 关键改进路径（提升至 Borderline Conference 3.5 所需）
1. 精确化 Cell B 实现：提供 Cell A/B 的 advantage sign 分布统计比较，明确 "消除 M2" vs "减缓 M2 累积伤害" 的概念区分
2. 增加析因 seed 数至 ≥5（尤其 Cell B OOD）
3. Abstract/Intro overclaiming 修复：报告中位数、弱化 "structurally eliminates" 措辞
4. 至少复现一个并发方法（如 GiGPO）验证框架预测能力

---

## Detailed Comments（逐节）

### Abstract
- "structurally eliminates both failure modes" 与 36% 泛化率矛盾，建议改为 "structurally removes the conditions for both failure modes but remains seed-dependent"
- 报告 mean 17.7% 但未报告 median 12.69%，分布右偏，中位数更能反映 typical 性能
- Word count: ~200 words，符合 EMNLP 限制

### Section 1 (Introduction)
- "achieving substantial OOD improvement where step-independent collapses to 0%" 被少数 generalized seeds 主导，需 qualifier
- Contribution 2 "controlled empirical separation" 措辞过强——实为 partial (3-of-4) factorial，且 Cell B 操作差异可能未真正消除 M2
- 8B 单 seed 结果应标注 "preliminary single-seed"

### Section 2 (Related Work)
- 覆盖面广（GRPO 变体、credit assignment、collapse 现象），引用量充足（35 entries）
- "our framework provides a unified explanation" 是声明而非验证——缺乏实证支撑
- ArCHer/VinePPO/Lightman 已引用（Round 5-6 修复确认）
- 建议更充分讨论 RLOO (Ahmadian et al., 2024) 与 episode-level GRPO 的关系

### Section 3 (Method)
- Section 3.4 "restores GRPO's original per-sample granularity to the episode level" 表述已校准（Round 6 修复确认）
- Section 3.5 "partial factorial" 措辞已改善，但 Cell B 被声称 "only M1 active" 存在定义矛盾（Cell B episode-level advantage 下失败 episode 所有 token 仍获负 advantage = M2 定义）
- Equation 2 γ 值应在主文给出

### Section 4 (Theoretical Analysis)
- Propositions 1-2 推导在 binary reward 假设内严谨
- Prop 1 → Prop 2 的有限样本细化关系已明确阐述（Round 6 修复确认）
- Definition 1 脚注已添加 policy drift 适用范围限定（Round 6 修复确认）
- Binary → ternary 桥接仍为定性论证（"two calibers"），缺形式化分析
- Eq.6 cumulative divergence 依赖对称假设，break-even 分析已补充但 Eq.6 本身未注明

### Section 5 (Experiments)
- 析因实验设计良好但 Cell C 缺失和 2-seed 限制是实质缺陷
- 11-seed 评估统计方法严谨（Fisher exact, Wilson CI, eval variance analysis）
- Section 5.4 sign verification 三指标互补，Cohen's h=0.041 + (+2pp) 措辞已校准
- Table 1: Cell B OOD 仅 1 seed, Cell A OOD 缺失——主表数据不完整
- 8B/ScienceWorld 单 seed，ScienceWorld 仅展示 collapse 未展示 fix

### Section 6 (Discussion)
- Cell C 讨论到位但可更深入分析非加性交互的含义
- 并发方法的一致性声称缺乏实证验证

### Section 7 (Conclusion)
- "GRPO-style methods under step-level windowing, sparse reward, and group-relative normalization" 限定范围已改善
- "structurally eliminates both" 需进一步弱化

### Limitations
- 覆盖面合理（环境/规模限制、seed 依赖、单次评估、sequence length scalability）
- 篇幅较短（~5 行），视觉审查也注意到 page 8 密度高

### Appendix
- 理论证明完整，Why Defaults 和 Classical Connection 分析有附加价值
- Cell C 尝试记录详尽（6 组超参数），但未尝试 gradient clipping per window position 作为 stabilization
- Method Selection Guide (Appendix E) 有实践价值
- Early Signal Analysis (Appendix H) n=4 太小，应标注 exploratory