---
round: 21
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T03:51:48.332357+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 21 审稿报告
## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
## Venue: EMNLP 2026 via ARR May cycle
## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)
## 审稿模式: Fresh (重新审稿)

---

## Summary

本文研究 LLM agent 在自然语言策略规范中遇到歧义时的安全违规行为。作者构建 300 对匹配的歧义/非歧义 clause pairs，涵盖六类歧义（两层：语言层 + 规范层），在 τ²-bench 上评估五个模型（2,997 episodes），并扩展至七模型跨架构复现。核心发现：(1) 歧义在合成控制条件下增加 34.0pp 违规率（confound-free range: +18.7 to +36.0pp）；(2) clause wording 解释 22.4% 方差 vs. type 仅 0.4%，但 type 预测 failure mechanism 的能力远强于预测违规率（NMI=0.23 vs 0.01）；(3) agent 对歧义元认知意识极低（≤11%），41.3% 歧义 clause 触发多模型趋同违规。

---

## Strengths

**S1 [共识]** 匹配对因果设计是 agent safety 领域的方法论创新。相比 DRIP-R 的关联性设计和 PolicyBank 的迭代优化，这是唯一提供因果证据的工作。300 clause pairs 的匹配质量（κ=0.95）可信，perturbation control（Δ=-0.67pp, CI 含零）有效排除表面改写效应。

**S2 [共识]** 多层 robustness 堪称全面：perturbation control（n=300）、cross-judge 三族验证（Fleiss' κ=0.717）、cross-benchmark 复现（SOPBench +12.6pp）、七模型跨六 provider 复现（+20.0 to +33.6pp）。对 C1 的支撑层层递进。

**S3 [共识]** "clause wording drives risk, type predicts mechanism" 的双重分解是最有洞察力的发现。22.4% vs. 0.4% 的方差分解将 taxonomy 从分类标签转化为诊断工具，是有说服力的 reframing。NMI=0.23 vs 0.01 的比值虽绝对水平 modest，但相对差异成立。

**S4 [共识]** Claims 校准诚实：C3 标注 inconclusive（p=0.017 未通过 Holm-Bonferroni），C4 标注 exploratory；incompleteness confound 被充分讨论并提供 confound-free range；authorization scope 的低可靠性（κ=0.385）被反复提示。统计方法与数据结构匹配（McNemar, TOST, Holm-Bonferroni, bootstrap cluster, permutation test）。

**S5 [共识]** Appendix 深度可圈可点：19 个 appendix sections 覆盖几乎所有可预见的质疑。Limitations 覆盖五方面（生态效度、范围、测量、confound、disambiguation channel），坦诚且具体。Ambig-SWE 引用已补充，interactive vs. non-interactive disambiguation 对比已在 §6.2 和 Limitations 讨论。

---

## Weaknesses

### Must-Fix 问题（Critical，两位 Reviewer 共识）

**N1 [critical, 共识]** SESOI ±15pp 缺乏外部锚定

±15pp 是论文 C2 partial ordering 的核心参数，但缺乏外部理据（无生产事故率数据、无监管阈值引用、无行业标准 SESOI）。perturbation control Δ=0.67pp 作为 negligible 基线无争议，但从 0.67pp 到 ±15pp 的跳跃缺乏论证链。论文的 Table 3（七 margin 敏感性）和 bootstrap cluster analysis 部分缓解了 margin 依赖——R2 指出 bootstrap cluster 作为 margin-free 补充有效——但不能替代外部锚定本身。在 ±10pp 下，mid-tier 仅 3/6 pairs 等价（power=0.57），C2 mid-tier 结构瓦解。

**要求修改**：(1) §4.6 明确承认无行业标准 SESOI；(2) Abstract 中 "partial ordering" 附 margin 条件限定；(3) 讨论安全场景下 ±15pp 是否过于宽松（对比 medical/financial 领域的 SESOI 实践）。

**N2 [critical, 共识]** 46% 未解释系统方差讨论深度不足

方差分解显示 condition 仅解释 15.8%，clause identity 22.4%，model 1.0%，残差 60.8%（其中 ~46pp 为系统性未测量因素，ICC=0.749）。Discussion §7 仅一句 "clause-level auditing addresses the largest actionable component (22.4%) but not the majority of outcome variance"。R2 指出论文将歧义定位为 "largest actionable component" 而非 "dominant driver"，叙事定位合理；但两位 Reviewer 均认为讨论深度不足——未列举候选因素（对话轨迹复杂度？任务类型？策略文档结构？用户行为？），未讨论这些因素的可操作性相对排序。

**要求修改**：Discussion 中增加 2-3 句列举系统性残差的候选因素及其对审计策略的启示。

**N3 [critical, 共识]** Cross-judge-group 类型排序 ρ=0.09 严重削弱 C2 partial ordering 可信度

这是本轮最严重的方法论发现。Within-judge-group type rankings 的 Spearman ρ=0.09（p=0.87）意味着不同 judge 家族对类型排序几乎完全不一致。排除 authorization scope 后 ρ 跳至 0.90（p=0.037），但 n=5 的统计功效极低。R2 补充了重要上下文：Appendix K 三法官 pooled type ranking ρ=0.71-0.89 远高于 within-group 0.09，表明问题根源在 judge-model pairing 而非 judge 偏差。

C2 partial ordering 实质退化为两个极端点（incompleteness 最高，coreferential 最低），中间四类型等价——信息量有限。Authorization scope 的 κ=0.385 进一步削弱其在排序中的定位可靠性。

**要求修改**：(1) 正文明确 C2 的有效范围为 "robust extremes only"（incompleteness upper bound + coreferential lower bound），mid-tier ordering 为 margin-dependent 且 judge-dependent；(2) ρ=0.09 disclosure 已在 §5.2 出现（良好），但 Abstract 和 Conclusion 的 "partial ordering" 表述应匹配正文的限定。

**N4 [critical, 共识]** Taxonomy 新颖性不足以支撑独立 contribution 定位

六类歧义直接源自 Li et al. (2024) 和 Massey et al. (2014) 的已有分类体系。C3 层级假说（specification > linguistic）p=0.017 未通过 Holm-Bonferroni，类型选择标准（"frequency in operational policy documents"）缺乏定量依据——无真实策略文档的歧义频率数据。R1 指出 Introduction 的 contribution 列表已避免将 taxonomy 列为独立贡献（三条贡献均以因果研究和方差分解为核心），这是正确的处理。

**要求修改**：(1) §3 增加类型选择的操作标准说明（为何选这六类而非 Li et al. 的 11 类中其他类型）；(2) §3 末尾或 §5.2 明确声明 C3 层级假说未通过多重比较校正，两层结构为组织便利。

### Should-Fix 问题（Warning，影响评分但不一票否决）

**W1 [warning, 共识]** Error analysis LLM 编码循环性

LLM 编码 LLM 失败的循环性风险论文已在 §6 承认。但 Gwet's AC₁=0.62 低于 good agreement 阈值 0.80，MI=0.41 是间接反循环证据但不能替代直接人工验证。两位 Reviewer 均建议至少 100 条 trace 的人工 failure mode 编码验证。论文已区分 2/6 definitional vs 4/6 empirical type→mechanism 映射（相比 R20 的改进），但编码可靠性本身需要加强。

**建议**：camera-ready 前完成人工验证子集，或在 Limitations 中更显著标注此局限。

**W2 [warning, 共识]** Disambiguation neglect 是 ambiguity collapse 的场景迁移，非概念创新

Liu et al. (2023) 已证明 LLM 坍缩歧义，Gur-Arieh et al. (2026) 已系统化 epistemic risks。本文贡献在于验证该现象在 agentic context 下产生不可逆策略违规（而非仅 response inaccuracy），这是有价值的实证验证，但非概念创新。当前 §6.2 的表述（"we refer to this pattern as disambiguation neglect"）暗示独立概念。

**建议**：定位为 "extending ambiguity collapse to agentic settings where it produces irreversible policy violations"（论文 §6.2 已有此方向的一句话，建议前移为段落主题句）。

**W3 [warning, 共识（partial）]** Abstract 应以 confound-free range 为核心效应量

Abstract 以 34.0pp 领头，含 incompleteness confound。R2 建议以 confound-free range (+18.7 to +36.0pp) 为主数字。R1 部分同意，补充 Appendix F 逻辑回归 token count 正系数暗示 confound 若存在为 attenuating（即 34.0pp 可能是下界）。Director 判断：Abstract 第二句已报告 confound-free range，但段首 "34.0 percentage points" 作为第一印象可能误导。

**建议**：Abstract 首句改为 confound-free pooled effect（如 "+31.0pp excluding the confounded type"），34.0pp 作为全类型参考值移至后文。

**W4 [warning, 共识]** Human validation 样本量不足

n=100, 2 annotators, per-type n≈32-34。Pooled κ=0.735 对 pipeline validation 充分（R2 确认），但 per-type 层面 scopal κ CI=[0.00, 1.00] 几乎无信息量。

**建议**：正文 §4.4 更明确指出 human validation 仅支持 pooled 层面的 pipeline 可靠性，per-type reliability 需更大样本。

**W5 [warning, 共识]** Temperature=0 跨 provider 确定性假设未讨论

不同 provider 对 temperature=0 实现不同（strict argmax vs. near-deterministic with residual stochasticity）。ICC 复制（Appendix D）仅限 OpenAI 模型。

**建议**：Limitations 增加一句讨论 temperature=0 跨 provider 的语义差异及对 ICC 估计的潜在影响。

**W6 [warning, 共识]** BibTeX key mou_ambigswe_2026 与 author 字段不匹配

key 暗示第一作者 Mou，但 author 字段为 Vijayvargiya 等人。可能是引用更新后 key 未同步。

**要求修复**。

### Minor Issues（Info，不影响评分）

**M1 [info, 共识]** Abstract 信息密度偏高——仍有 5 个具体数字（34.0pp, +18.7 to +36.0pp, 22.4% vs 0.4%, NMI, ≤11%, 40%+）。建议精简至 3 个核心数值：confound-free effect、variance decomposition、convergent violation rate。

**M2 [info, 共识]** Systematic nocuity 与 Berry & Kamsties (2004) 原始定义方向偏差——原始 "nocuous" 指 divergent interpretations，论文指 convergent errors（方向相反）。应明确说明术语重新定义。R2 补充：34pp 绝对增幅足以支撑 "nocuous" 定性判断（因果效应大小与方差解释比例是不同概念）。Director 采纳 R2 判断——"nocuous" 作为定性描述成立，但方向偏差需澄清。

**M3 [info, 共识]** NMI=0.23 绝对水平 modest，"order of magnitude" 表述在比值意义上成立（23× > 10×）但绝对值仅为 moderate association。建议同时报告 Cramér's V=0.45 并措辞为 "moderate but actionable association"。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：

1. **SESOI 缺乏外部锚定是核心方法论弱点** (N1)——bootstrap cluster 部分缓解但不充分
2. **46% 未解释方差需更深入讨论** (N2)——叙事定位合理但候选因素讨论缺失
3. **ρ=0.09 是最严重的方法论发现** (N3)——C2 有效范围为 robust extremes only
4. **Taxonomy 非独立贡献** (N4)——C3 未通过多重比较，类型选择标准缺定量依据
5. **方法论质量高** (Soundness 4)——matched-pair 因果设计、多层 robustness、claims 校准诚实
6. **新颖性处于 borderline** (Excitement 3)——结果方向可预期，taxonomy 增量，DN 是场景迁移
7. **Error analysis 编码循环性需人工验证** (W1)
8. **Human validation pooled 充分，per-type 不足** (W4)

## Reviewer Divergence（交叉回应中已收敛）

以下三个分歧在交叉回应中解决：

1. **SOPBench 衰减解读**：R1 视 34pp→12.6pp 为生态效度弱点；R2 反驳——结构性解释（pre-existing policies、不同域）成立，且七模型扩展复现（+20-33.6pp）是更有力的泛化证据。**Director 判断**：采纳 R2 反驳，SOPBench 是 secondary evidence，model expansion 是 primary generalizability。不升级为 issue。

2. **ICC CI 上界数值**：R1 引用 0.910；R2 更正为 0.940。**Director 判断**：采纳 R2 事实更正，不影响整体评估。

3. **"Nocuous" 定性判断是否过度**：R1 质疑歧义仅解释 15.8% 方差是否支撑 "nocuous" 标题；R2 反驳——因果效应大小（34pp 绝对增幅）与方差解释比例是不同概念，34pp 在安全场景下足以构成 "harmful"。**Director 判断**：采纳 R2 区分，因果效应足以支撑定性判断。M2 仅保留 Berry & Kamsties 方向偏差的术语澄清建议。

---

## Questions

1. 系统性残差 ~46pp 中，作者是否有候选因素的初步探索数据（如对话轮次、任务复杂度与违规率的相关性）？
2. 同批 annotators 是否既创建又验证了 clause pairs？如果是，如何排除 confirmation bias？
3. Authorization scope 的 within-judge-group type ranking 是否可通过增加 judge 数量或换用 human judges 稳定？
4. Failure mode 编码的 AC₁=0.62 中，哪些 mechanism 类别的一致性最低？是否有 per-category 的 κ 分解？

---

## Missing References

本轮无新遗漏（R20 提出的 Ambig-SWE 已补充，其余 R20-W10 文献已核实不威胁核心 claim）。

---

## External Review

外部审稿：未请求（项目配置未启用）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2026-05-23 03:22–03:26 UTC）。结果摘要：

- **0 critical, 1 warning, 17 info**
- **Warning**: pp.4-5 连续两页纯文本（Method 4.1–4.4 及 Experiments/Controls 4.5–5.1），无 display item 穿插。Method 部分缺少方法示意图或 clause pair 构造示例图。
- **Info highlights**: Figure 1 内子类别标签字号偏小（估计 ≤7pt，低于推荐 8pt）；pp.6-7 display item 密度高与 pp.4-5 形成对比。References 无 [?] 未解析引用，引用格式统一。主文 8 页利用率 100%。

整体排版质量良好，无格式硬伤。建议考虑 Method 部分插入一个 clause pair 构造示例（如 Table 或 Figure），缓解 pp.4-5 的视觉疲劳。

---

## Overall Assessment

**Overall Score: 3.5 / 5 (Borderline Conference)**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Overall | 3.5 | 3.5 | **3.5** |
| Soundness | 4 | 4 | **4** |
| Excitement | 3 | 3 | **3** |
| Confidence | 4 | 4 | **4** |

**核心判断**：方法论执行到位（Soundness 4），matched-pair 因果设计、多层 robustness checks、诚实的 claims 校准在 agent safety 文献中属上乘。R20 的两个 must-fix（failure mode tautological 循环 + 遗漏 Ambig-SWE）均已有效修复——17× 弱化为 "order of magnitude" 并区分 definitional vs empirical mappings；Ambig-SWE 已引用并在 §6.2 和 Limitations 讨论。

但本轮 fresh review 暴露了四个 critical 问题：(1) SESOI ±15pp 的外部锚定缺失使 C2 mid-tier ordering 的有效性依赖于读者对 margin 的接受度；(2) 46% 系统性残差的讨论深度不足，限制了 auditing implications 的说服力；(3) cross-judge type ranking ρ=0.09 严重削弱 C2——partial ordering 实质退化为两个极端点；(4) taxonomy 新颖性不足，C3 检验失败未在 Intro 反映。新颖性处于 borderline——核心结果（歧义增加违规）方向可预期，taxonomy 为增量贡献，disambiguation neglect 是 ambiguity collapse 的场景迁移。

**接收条件**：如果作者能 (1) Abstract/Conclusion 限定 C2 为 "robust extremes" + margin 条件，(2) Discussion 增加残差候选因素讨论，(3) §3 补充类型选择操作标准和 C3 inconclusive 说明，(4) Abstract 以 confound-free effect 为主数字，(5) 修复 bib key，本文可达 Conference 水准（4.0）。

**与 R20 对比**：R20 的两个 critical（tautological + Ambig-SWE）已修复，方法论在 failure mode 分析上有实质改进。但 fresh review 发现的新 criticals（SESOI 锚定、ρ=0.09、未解释方差、taxonomy novelty）使总评维持 3.5。这些问题主要是解释/呈现层面的（而非基础方法论缺陷），修复路径清晰。

---

## Detailed Comments

### Abstract
- 首句 34.0pp 含 incompleteness confound → 建议以 confound-free pooled effect 领头 (W3)
- 5 个具体数字信息密度偏高 → 精简至 3 个 (M1)
- "partial ordering" 未附 margin 条件 (N1)

### §1 Introduction
- Contribution (2) "order of magnitude" 比值成立但 NMI=0.23 绝对值 modest → 考虑补充 Cramér's V=0.45 (M3)
- 三条 contribution 均以因果研究和方差分解为核心，未将 taxonomy 列为独立贡献——这是正确的处理 (N4 context)

### §2 Related Work
- Ambig-SWE 已引用且讨论充分 ✓
- "disambiguation neglect" 的定位可在此段更早明确为 ambiguity collapse 的 agentic extension (W2)

### §3 Ambiguity Taxonomy
- 类型选择标准缺定量依据（为何这六类？排除 ellipsis/pragmatic implicature 的量化理由？）(N4)
- 建议末尾明确声明 taxonomy 是实验 IV 的操作化，C3 层级假说未通过多重比较校正 (N4)

### §4 Method
- §4.4 Human validation per-type 不确定性在正文传达不足 (W4)
- §4.6 SESOI ±15pp 缺外部锚定 (N1)

### §5 Results
- §5.1 方差全景图中 ~46pp 系统残差的候选因素讨论缺失 (N2)
- §5.2 ρ=0.09 disclosure 已在正文——这是良好实践。但 Abstract/Conclusion 的 "partial ordering" 应匹配此限定 (N3)
- §5.2 C2 有效范围应明确为 "robust extremes only" (N3)

### §6 Error Analysis
- AC₁=0.62 低于 good agreement → 需人工验证 (W1)
- 2/6 definitional vs 4/6 empirical 区分是 R20 后的改进 ✓
- §6.2 disambiguation neglect 定位调整建议 (W2)
- §6.3 "systematic nocuity" 与 Berry & Kamsties 原始方向偏差需澄清 (M2)

### §7 Discussion
- "clause-level auditing addresses the largest actionable component" — 增加残差候选因素讨论 (N2)
- Temperature=0 跨 provider 差异 (W5)

### §9 Limitations
- 整体质量高 ✓
- 建议增加 temperature=0 跨 provider 讨论 (W5)
- Failure mode 编码的人工验证缺失可更显著标注 (W1)

### References
- mou_ambigswe_2026 key 与 author 不匹配 → 修复 (W6)

### Appendix
- Appendix K 三法官 pooled ρ=0.71-0.89 vs within-group ρ=0.09 的差异值得在正文 §5.2 简要提及，帮助读者理解问题根源在 judge-model pairing 而非 judge bias (N3)