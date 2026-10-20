# Director coordination — Part 7 of 11

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

[← Part 6](part-006.md) · [Transcript overview](../director-coordination.md) · [Part 8 →](part-008.md) · [Structured JSON](../../../sessions/0e/0e806c5d99edfa05e2ae.json)

## Round 178

### Tool call

_source line 1883 · 2026-05-23T03:51:48.302925+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 21 审稿报告\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)\n## 审稿模式: Fresh (重新审稿)\n\n---\n\n## Summary\n\n本文研究 LLM agent 在自然语言策略规范中遇到歧义时的安全违规行为。作者构建 300 对匹配的歧义/非歧义 clause pairs，涵盖六类歧义（两层：语言层 + 规范层），在 τ²-bench 上评估五个模型（2,997 episodes），并扩展至七模型跨架构复现。核心发现：(1) 歧义在合成控制条件下增加 34.0pp 违规率（confound-free range: +18.7 to +36.0pp）；(2) clause wording 解释 22.4% 方差 vs. type 仅 0.4%，但 type 预测 failure mechanism 的能力远强于预测违规率（NMI=0.23 vs 0.01）；(3) agent 对歧义元认知意识极低（≤11%），41.3% 歧义 clause 触发多模型趋同违规。\n\n---\n\n## Strengths\n\n**S1 [共识]** 匹配对因果设计是 agent safety 领域的方法论创新。相比 DRIP-R 的关联性设计和 PolicyBank 的迭代优化，这是唯一提供因果证据的工作。300 clause pairs 的匹配质量（κ=0.95）可信，perturbation control（Δ=-0.67pp, CI 含零）有效排除表面改写效应。\n\n**S2 [共识]** 多层 robustness 堪称全面：perturbation control（n=300）、cross-judge 三族验证（Fleiss' κ=0.717）、cross-benchmark 复现（SOPBench +12.6pp）、七模型跨六 provider 复现（+20.0 to +33.6pp）。对 C1 的支撑层层递进。\n\n**S3 [共识]** \"clause wording drives risk, type predicts mechanism\" 的双重分解是最有洞察力的发现。22.4% vs. 0.4% 的方差分解将 taxonomy 从分类标签转化为诊断工具，是有说服力的 reframing。NMI=0.23 vs 0.01 的比值虽绝对水平 modest，但相对差异成立。\n\n**S4 [共识]** Claims 校准诚实：C3 标注 inconclusive（p=0.017 未通过 Holm-Bonferroni），C4 标注 exploratory；incompleteness confound 被充分讨论并提供 confound-free range；authorization scope 的低可靠性（κ=0.385）被反复提示。统计方法与数据结构匹配（McNemar, TOST, Holm-Bonferroni, bootstrap cluster, permutation test）。\n\n**S5 [共识]** Appendix 深度可圈可点：19 个 appendix sections 覆盖几乎所有可预见的质疑。Limitations 覆盖五方面（生态效度、范围、测量、confound、disambiguation channel），坦诚且具体。Ambig-SWE 引用已补充，interactive vs. non-interactive disambiguation 对比已在 §6.2 和 Limitations 讨论。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（Critical，两位 Reviewer 共识）\n\n**N1 [critical, 共识]** SESOI ±15pp 缺乏外部锚定\n\n±15pp 是论文 C2 partial ordering 的核心参数，但缺乏外部理据（无生产事故率数据、无监管阈值引用、无行业标准 SESOI）。perturbation control Δ=0.67pp 作为 negligible 基线无争议，但从 0.67pp 到 ±15pp 的跳跃缺乏论证链。论文的 Table 3（七 margin 敏感性）和 bootstrap cluster analysis 部分缓解了 margin 依赖——R2 指出 bootstrap cluster 作为 margin-free 补充有效——但不能替代外部锚定本身。在 ±10pp 下，mid-tier 仅 3/6 pairs 等价（power=0.57），C2 mid-tier 结构瓦解。\n\n**要求修改**：(1) §4.6 明确承认无行业标准 SESOI；(2) Abstract 中 \"partial ordering\" 附 margin 条件限定；(3) 讨论安全场景下 ±15pp 是否过于宽松（对比 medical/financial 领域的 SESOI 实践）。\n\n**N2 [critical, 共识]** 46% 未解释系统方差讨论深度不足\n\n方差分解显示 condition 仅解释 15.8%，clause identity 22.4%，model 1.0%，残差 60.8%（其中 ~46pp 为系统性未测量因素，ICC=0.749）。Discussion §7 仅一句 \"clause-level auditing addresses the largest actionable component (22.4%) but not the majority of outcome variance\"。R2 指出论文将歧义定位为 \"largest actionable component\" 而非 \"dominant driver\"，叙事定位合理；但两位 Reviewer 均认为讨论深度不足——未列举候选因素（对话轨迹复杂度？任务类型？策略文档结构？用户行为？），未讨论这些因素的可操作性相对排序。\n\n**要求修改**：Discussion 中增加 2-3 句列举系统性残差的候选因素及其对审计策略的启示。\n\n**N3 [critical, 共识]** Cross-judge-group 类型排序 ρ=0.09 严重削弱 C2 partial ordering 可信度\n\n这是本轮最严重的方法论发现。Within-judge-group type rankings 的 Spearman ρ=0.09（p=0.87）意味着不同 judge 家族对类型排序几乎完全不一致。排除 authorization scope 后 ρ 跳至 0.90（p=0.037），但 n=5 的统计功效极低。R2 补充了重要上下文：Appendix K 三法官 pooled type ranking ρ=0.71-0.89 远高于 within-group 0.09，表明问题根源在 judge-model pairing 而非 judge 偏差。\n\nC2 partial ordering 实质退化为两个极端点（incompleteness 最高，coreferential 最低），中间四类型等价——信息量有限。Authorization scope 的 κ=0.385 进一步削弱其在排序中的定位可靠性。\n\n**要求修改**：(1) 正文明确 C2 的有效范围为 \"robust extremes only\"（incompleteness upper bound + coreferential lower bound），mid-tier ordering 为 margin-dependent 且 judge-dependent；(2) ρ=0.09 disclosure 已在 §5.2 出现（良好），但 Abstract 和 Conclusion 的 \"partial ordering\" 表述应匹配正文的限定。\n\n**N4 [critical, 共识]** Taxonomy 新颖性不足以支撑独立 contribution 定位\n\n六类歧义直接源自 Li et al. (2024) 和 Massey et al. (2014) 的已有分类体系。C3 层级假说（specification > linguistic）p=0.017 未通过 Holm-Bonferroni，类型选择标准（\"frequency in operational policy documents\"）缺乏定量依据——无真实策略文档的歧义频率数据。R1 指出 Introduction 的 contribution 列表已避免将 taxonomy 列为独立贡献（三条贡献均以因果研究和方差分解为核心），这是正确的处理。\n\n**要求修改**：(1) §3 增加类型选择的操作标准说明（为何选这六类而非 Li et al. 的 11 类中其他类型）；(2) §3 末尾或 §5.2 明确声明 C3 层级假说未通过多重比较校正，两层结构为组织便利。\n\n### Should-Fix 问题（Warning，影响评分但不一票否决）\n\n**W1 [warning, 共识]** Error analysis LLM 编码循环性\n\nLLM 编码 LLM 失败的循环性风险论文已在 §6 承认。但 Gwet's AC₁=0.62 低于 good agreement 阈值 0.80，MI=0.41 是间接反循环证据但不能替代直接人工验证。两位 Reviewer 均建议至少 100 条 trace 的人工 failure mode 编码验证。论文已区分 2/6 definitional vs 4/6 empirical type→mechanism 映射（相比 R20 的改进），但编码可靠性本身需要加强。\n\n**建议**：camera-ready 前完成人工验证子集，或在 Limitations 中更显著标注此局限。\n\n**W2 [warning, 共识]** Disambiguation neglect 是 ambiguity collapse 的场景迁移，非概念创新\n\nLiu et al. (2023) 已证明 LLM 坍缩歧义，Gur-Arieh et al. (2026) 已系统化 epistemic risks。本文贡献在于验证该现象在 agentic context 下产生不可逆策略违规（而非仅 response inaccuracy），这是有价值的实证验证，但非概念创新。当前 §6.2 的表述（\"we refer to this pattern as disambiguation neglect\"）暗示独立概念。\n\n**建议**：定位为 \"extending ambiguity collapse to agentic settings where it produces irreversible policy violations\"（论文 §6.2 已有此方向的一句话，建议前移为段落主题句）。\n\n**W3 [warning, 共识（partial）]** Abstract 应以 confound-free range 为核心效应量\n\nAbstract 以 34.0pp 领头，含 incompleteness confound。R2 建议以 confound-free range (+18.7 to +36.0pp) 为主数字。R1 部分同意，补充 Appendix F 逻辑回归 token count 正系数暗示 confound 若存在为 attenuating（即 34.0pp 可能是下界）。Director 判断：Abstract 第二句已报告 confound-free range，但段首 \"34.0 percentage points\" 作为第一印象可能误导。\n\n**建议**：Abstract 首句改为 confound-free pooled effect（如 \"+31.0pp excluding the confounded type\"），34.0pp 作为全类型参考值移至后文。\n\n**W4 [warning, 共识]** Human validation 样本量不足\n\nn=100, 2 annotators, per-type n≈32-34。Pooled κ=0.735 对 pipeline validation 充分（R2 确认），但 per-type 层面 scopal κ CI=[0.00, 1.00] 几乎无信息量。\n\n**建议**：正文 §4.4 更明确指出 human validation 仅支持 pooled 层面的 pipeline 可靠性，per-type reliability 需更大样本。\n\n**W5 [warning, 共识]** Temperature=0 跨 provider 确定性假设未讨论\n\n不同 provider 对 temperature=0 实现不同（strict argmax vs. near-deterministic with residual stochasticity）。ICC 复制（Appendix D）仅限 OpenAI 模型。\n\n**建议**：Limitations 增加一句讨论 temperature=0 跨 provider 的语义差异及对 ICC 估计的潜在影响。\n\n**W6 [warning, 共识]** BibTeX key mou_ambigswe_2026 与 author 字段不匹配\n\nkey 暗示第一作者 Mou，但 author 字段为 Vijayvargiya 等人。可能是引用更新后 key 未同步。\n\n**要求修复**。\n\n### Minor Issues（Info，不影响评分）\n\n**M1 [info, 共识]** Abstract 信息密度偏高——仍有 5 个具体数字（34.0pp, +18.7 to +36.0pp, 22.4% vs 0.4%, NMI, ≤11%, 40%+）。建议精简至 3 个核心数值：confound-free effect、variance decomposition、convergent violation rate。\n\n**M2 [info, 共识]** Systematic nocuity 与 Berry & Kamsties (2004) 原始定义方向偏差——原始 \"nocuous\" 指 divergent interpretations，论文指 convergent errors（方向相反）。应明确说明术语重新定义。R2 补充：34pp 绝对增幅足以支撑 \"nocuous\" 定性判断（因果效应大小与方差解释比例是不同概念）。Director 采纳 R2 判断——\"nocuous\" 作为定性描述成立，但方向偏差需澄清。\n\n**M3 [info, 共识]** NMI=0.23 绝对水平 modest，\"order of magnitude\" 表述在比值意义上成立（23× > 10×）但绝对值仅为 moderate association。建议同时报告 Cramér's V=0.45 并措辞为 \"moderate but actionable association\"。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n\n1. **SESOI 缺乏外部锚定是核心方法论弱点** (N1)——bootstrap cluster 部分缓解但不充分\n2. **46% 未解释方差需更深入讨论** (N2)——叙事定位合理但候选因素讨论缺失\n3. **ρ=0.09 是最严重的方法论发现** (N3)——C2 有效范围为 robust extremes only\n4. **Taxonomy 非独立贡献** (N4)——C3 未通过多重比较，类型选择标准缺定量依据\n5. **方法论质量高** (Soundness 4)——matched-pair 因果设计、多层 robustness、claims 校准诚实\n6. **新颖性处于 borderline** (Excitement 3)——结果方向可预期，taxonomy 增量，DN 是场景迁移\n7. **Error analysis 编码循环性需人工验证** (W1)\n8. **Human validation pooled 充分，per-type 不足** (W4)\n\n## Reviewer Divergence（交叉回应中已收敛）\n\n以下三个分歧在交叉回应中解决：\n\n1. **SOPBench 衰减解读**：R1 视 34pp→12.6pp 为生态效度弱点；R2 反驳——结构性解释（pre-existing policies、不同域）成立，且七模型扩展复现（+20-33.6pp）是更有力的泛化证据。**Director 判断**：采纳 R2 反驳，SOPBench 是 secondary evidence，model expansion 是 primary generalizability。不升级为 issue。\n\n2. **ICC CI 上界数值**：R1 引用 0.910；R2 更正为 0.940。**Director 判断**：采纳 R2 事实更正，不影响整体评估。\n\n3. **\"Nocuous\" 定性判断是否过度**：R1 质疑歧义仅解释 15.8% 方差是否支撑 \"nocuous\" 标题；R2 反驳——因果效应大小（34pp 绝对增幅）与方差解释比例是不同概念，34pp 在安全场景下足以构成 \"harmful\"。**Director 判断**：采纳 R2 区分，因果效应足以支撑定性判断。M2 仅保留 Berry & Kamsties 方向偏差的术语澄清建议。\n\n---\n\n## Questions\n\n1. 系统性残差 ~46pp 中，作者是否有候选因素的初步探索数据（如对话轮次、任务复杂度与违规率的相关性）？\n2. 同批 annotators 是否既创建又验证了 clause pairs？如果是，如何排除 confirmation bias？\n3. Authorization scope 的 within-judge-group type ranking 是否可通过增加 judge 数量或换用 human judges 稳定？\n4. Failure mode 编码的 AC₁=0.62 中，哪些 mechanism 类别的一致性最低？是否有 per-category 的 κ 分解？\n\n---\n\n## Missing References\n\n本轮无新遗漏（R20 提出的 Ambig-SWE 已补充，其余 R20-W10 文献已核实不威胁核心 claim）。\n\n---\n\n## External Review\n\n外部审稿：未请求（项目配置未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-23 03:22–03:26 UTC）。结果摘要：\n\n- **0 critical, 1 warning, 17 info**\n- **Warning**: pp.4-5 连续两页纯文本（Method 4.1–4.4 及 Experiments/Controls 4.5–5.1），无 display item 穿插。Method 部分缺少方法示意图或 clause pair 构造示例图。\n- **Info highlights**: Figure 1 内子类别标签字号偏小（估计 ≤7pt，低于推荐 8pt）；pp.6-7 display item 密度高与 pp.4-5 形成对比。References 无 [?] 未解析引用，引用格式统一。主文 8 页利用率 100%。\n\n整体排版质量良好，无格式硬伤。建议考虑 Method 部分插入一个 clause pair 构造示例（如 Table 或 Figure），缓解 pp.4-5 的视觉疲劳。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Overall | 3.5 | 3.5 | **3.5** |\n| Soundness | 4 | 4 | **4** |\n| Excitement | 3 | 3 | **3** |\n| Confidence | 4 | 4 | **4** |\n\n**核心判断**：方法论执行到位（Soundness 4），matched-pair 因果设计、多层 robustness checks、诚实的 claims 校准在 agent safety 文献中属上乘。R20 的两个 must-fix（failure mode tautological 循环 + 遗漏 Ambig-SWE）均已有效修复——17× 弱化为 \"order of magnitude\" 并区分 definitional vs empirical mappings；Ambig-SWE 已引用并在 §6.2 和 Limitations 讨论。\n\n但本轮 fresh review 暴露了四个 critical 问题：(1) SESOI ±15pp 的外部锚定缺失使 C2 mid-tier ordering 的有效性依赖于读者对 margin 的接受度；(2) 46% 系统性残差的讨论深度不足，限制了 auditing implications 的说服力；(3) cross-judge type ranking ρ=0.09 严重削弱 C2——partial ordering 实质退化为两个极端点；(4) taxonomy 新颖性不足，C3 检验失败未在 Intro 反映。新颖性处于 borderline——核心结果（歧义增加违规）方向可预期，taxonomy 为增量贡献，disambiguation neglect 是 ambiguity collapse 的场景迁移。\n\n**接收条件**：如果作者能 (1) Abstract/Conclusion 限定 C2 为 \"robust extremes\" + margin 条件，(2) Discussion 增加残差候选因素讨论，(3) §3 补充类型选择操作标准和 C3 inconclusive 说明，(4) Abstract 以 confound-free effect 为主数字，(5) 修复 bib key，本文可达 Conference 水准（4.0）。\n\n**与 R20 对比**：R20 的两个 critical（tautological + Ambig-SWE）已修复，方法论在 failure mode 分析上有实质改进。但 fresh review 发现的新 criticals（SESOI 锚定、ρ=0.09、未解释方差、taxonomy novelty）使总评维持 3.5。这些问题主要是解释/呈现层面的（而非基础方法论缺陷），修复路径清晰。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 首句 34.0pp 含 incompleteness confound → 建议以 confound-free pooled effect 领头 (W3)\n- 5 个具体数字信息密度偏高 → 精简至 3 个 (M1)\n- \"partial ordering\" 未附 margin 条件 (N1)\n\n### §1 Introduction\n- Contribution (2) \"order of magnitude\" 比值成立但 NMI=0.23 绝对值 modest → 考虑补充 Cramér's V=0.45 (M3)\n- 三条 contribution 均以因果研究和方差分解为核心，未将 taxonomy 列为独立贡献——这是正确的处理 (N4 context)\n\n### §2 Related Work\n- Ambig-SWE 已引用且讨论充分 ✓\n- \"disambiguation neglect\" 的定位可在此段更早明确为 ambiguity collapse 的 agentic extension (W2)\n\n### §3 Ambiguity Taxonomy\n- 类型选择标准缺定量依据（为何这六类？排除 ellipsis/pragmatic implicature 的量化理由？）(N4)\n- 建议末尾明确声明 taxonomy 是实验 IV 的操作化，C3 层级假说未通过多重比较校正 (N4)\n\n### §4 Method\n- §4.4 Human validation per-type 不确定性在正文传达不足 (W4)\n- §4.6 SESOI ±15pp 缺外部锚定 (N1)\n\n### §5 Results\n- §5.1 方差全景图中 ~46pp 系统残差的候选因素讨论缺失 (N2)\n- §5.2 ρ=0.09 disclosure 已在正文——这是良好实践。但 Abstract/Conclusion 的 \"partial ordering\" 应匹配此限定 (N3)\n- §5.2 C2 有效范围应明确为 \"robust extremes only\" (N3)\n\n### §6 Error Analysis\n- AC₁=0.62 低于 good agreement → 需人工验证 (W1)\n- 2/6 definitional vs 4/6 empirical 区分是 R20 后的改进 ✓\n- §6.2 disambiguation neglect 定位调整建议 (W2)\n- §6.3 \"systematic nocuity\" 与 Berry & Kamsties 原始方向偏差需澄清 (M2)\n\n### §7 Discussion\n- \"clause-level auditing addresses the largest actionable component\" — 增加残差候选因素讨论 (N2)\n- Temperature=0 跨 provider 差异 (W5)\n\n### §9 Limitations\n- 整体质量高 ✓\n- 建议增加 temperature=0 跨 provider 讨论 (W5)\n- Failure mode 编码的人工验证缺失可更显著标注 (W1)\n\n### References\n- mou_ambigswe_2026 key 与 author 不匹配 → 修复 (W6)\n\n### Appendix\n- Appendix K 三法官 pooled ρ=0.71-0.89 vs within-group ρ=0.09 的差异值得在正文 §5.2 简要提及，帮助读者理解问题根源在 judge-model pairing 而非 judge bias (N3)",
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 21 审稿报告\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)\n## 审稿模式: Fresh (重新审稿)\n\n---\n\n## Summary\n\n本文研究 LLM agent 在自然语言策略规范中遇到歧义时的安全违规行为。作者构建 300 对匹配的歧义/非歧义 clause pairs，涵盖六类歧义（两层：语言层 + 规范层），在 τ²-bench 上评估五个模型（2,997 episodes），并扩展至七模型跨架构复现。核心发现：(1) 歧义在合成控制条件下增加 34.0pp 违规率（confound-free range: +18.7 to +36.0pp）；(2) clause wording 解释 22.4% 方差 vs. type 仅 0.4%，但 type 预测 failure mechanism 的能力远强于预测违规率（NMI=0.23 vs 0.01）；(3) agent 对歧义元认知意识极低（≤11%），41.3% 歧义 clause 触发多模型趋同违规。\n\n---\n\n## Strengths\n\n**S1 [共识]** 匹配对因果设计是 agent safety 领域的方法论创新。相比 DRIP-R 的关联性设计和 PolicyBank 的迭代优化，这是唯一提供因果证据的工作。300 clause pairs 的匹配质量（κ=0.95）可信，perturbation control（Δ=-0.67pp, CI 含零）有效排除表面改写效应。\n\n**S2 [共识]** 多层 robustness 堪称全面：perturbation control（n=300）、cross-judge 三族验证（Fleiss' κ=0.717）、cross-benchmark 复现（SOPBench +12.6pp）、七模型跨六 provider 复现（+20.0 to +33.6pp）。对 C1 的支撑层层递进。\n\n**S3 [共识]** \"clause wording drives risk, type predicts mechanism\" 的双重分解是最有洞察力的发现。22.4% vs. 0.4% 的方差分解将 taxonomy 从分类标签转化为诊断工具，是有说服力的 reframing。NMI=0.23 vs 0.01 的比值虽绝对水平 modest，但相对差异成立。\n\n**S4 [共识]** Claims 校准诚实：C3 标注 inconclusive（p=0.017 未通过 Holm-Bonferroni），C4 标注 exploratory；incompleteness confound 被充分讨论并提供 confound-free range；authorization scope 的低可靠性（κ=0.385）被反复提示。统计方法与数据结构匹配（McNemar, TOST, Holm-Bonferroni, bootstrap cluster, permutation test）。\n\n**S5 [共识]** Appendix 深度可圈可点：19 个 appendix sections 覆盖几乎所有可预见的质疑。Limitations 覆盖五方面（生态效度、范围、测量、confound、disambiguation channel），坦诚且具体。Ambig-SWE 引用已补充，interactive vs. non-interactive disambiguation 对比已在 §6.2 和 Limitations 讨论。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（Critical，两位 Reviewer 共识）\n\n**N1 [critical, 共识]** SESOI ±15pp 缺乏外部锚定\n\n±15pp 是论文 C2 partial ordering 的核心参数，但缺乏外部理据（无生产事故率数据、无监管阈值引用、无行业标准 SESOI）。perturbation control Δ=0.67pp 作为 negligible 基线无争议，但从 0.67pp 到 ±15pp 的跳跃缺乏论证链。论文的 Table 3（七 margin 敏感性）和 bootstrap cluster analysis 部分缓解了 margin 依赖——R2 指出 bootstrap cluster 作为 margin-free 补充有效——但不能替代外部锚定本身。在 ±10pp 下，mid-tier 仅 3/6 pairs 等价（power=0.57），C2 mid-tier 结构瓦解。\n\n**要求修改**：(1) §4.6 明确承认无行业标准 SESOI；(2) Abstract 中 \"partial ordering\" 附 margin 条件限定；(3) 讨论安全场景下 ±15pp 是否过于宽松（对比 medical/financial 领域的 SESOI 实践）。\n\n**N2 [critical, 共识]** 46% 未解释系统方差讨论深度不足\n\n方差分解显示 condition 仅解释 15.8%，clause identity 22.4%，model 1.0%，残差 60.8%（其中 ~46pp 为系统性未测量因素，ICC=0.749）。Discussion §7 仅一句 \"clause-level auditing addresses the largest actionable component (22.4%) but not the majority of outcome variance\"。R2 指出论文将歧义定位为 \"largest actionable component\" 而非 \"dominant driver\"，叙事定位合理；但两位 Reviewer 均认为讨论深度不足——未列举候选因素（对话轨迹复杂度？任务类型？策略文档结构？用户行为？），未讨论这些因素的可操作性相对排序。\n\n**要求修改**：Discussion 中增加 2-3 句列举系统性残差的候选因素及其对审计策略的启示。\n\n**N3 [critical, 共识]** Cross-judge-group 类型排序 ρ=0.09 严重削弱 C2 partial ordering 可信度\n\n这是本轮最严重的方法论发现。Within-judge-group type rankings 的 Spearman ρ=0.09（p=0.87）意味着不同 judge 家族对类型排序几乎完全不一致。排除 authorization scope 后 ρ 跳至 0.90（p=0.037），但 n=5 的统计功效极低。R2 补充了重要上下文：Appendix K 三法官 pooled type ranking ρ=0.71-0.89 远高于 within-group 0.09，表明问题根源在 judge-model pairing 而非 judge 偏差。\n\nC2 partial ordering 实质退化为两个极端点（incompleteness 最高，coreferential 最低），中间四类型等价——信息量有限。Authorization scope 的 κ=0.385 进一步削弱其在排序中的定位可靠性。\n\n**要求修改**：(1) 正文明确 C2 的有效范围为 \"robust extremes only\"（incompleteness upper bound + coreferential lower bound），mid-tier ordering 为 margin-dependent 且 judge-dependent；(2) ρ=0.09 disclosure 已在 §5.2 出现（良好），但 Abstract 和 Conclusion 的 \"partial ordering\" 表述应匹配正文的限定。\n\n**N4 [critical, 共识]** Taxonomy 新颖性不足以支撑独立 contribution 定位\n\n六类歧义直接源自 Li et al. (2024) 和 Massey et al. (2014) 的已有分类体系。C3 层级假说（specification > linguistic）p=0.017 未通过 Holm-Bonferroni，类型选择标准（\"frequency in operational policy documents\"）缺乏定量依据——无真实策略文档的歧义频率数据。R1 指出 Introduction 的 contribution 列表已避免将 taxonomy 列为独立贡献（三条贡献均以因果研究和方差分解为核心），这是正确的处理。\n\n**要求修改**：(1) §3 增加类型选择的操作标准说明（为何选这六类而非 Li et al. 的 11 类中其他类型）；(2) §3 末尾或 §5.2 明确声明 C3 层级假说未通过多重比较校正，两层结构为组织便利。\n\n### Should-Fix 问题（Warning，影响评分但不一票否决）\n\n**W1 [warning, 共识]** Error analysis LLM 编码循环性\n\nLLM 编码 LLM 失败的循环性风险论文已在 §6 承认。但 Gwet's AC₁=0.62 低于 good agreement 阈值 0.80，MI=0.41 是间接反循环证据但不能替代直接人工验证。两位 Reviewer 均建议至少 100 条 trace 的人工 failure mode 编码验证。论文已区分 2/6 definitional vs 4/6 empirical type→mechanism 映射（相比 R20 的改进），但编码可靠性本身需要加强。\n\n**建议**：camera-ready 前完成人工验证子集，或在 Limitations 中更显著标注此局限。\n\n**W2 [warning, 共识]** Disambiguation neglect 是 ambiguity collapse 的场景迁移，非概念创新\n\nLiu et al. (2023) 已证明 LLM 坍缩歧义，Gur-Arieh et al. (2026) 已系统化 epistemic risks。本文贡献在于验证该现象在 agentic context 下产生不可逆策略违规（而非仅 response inaccuracy），这是有价值的实证验证，但非概念创新。当前 §6.2 的表述（\"we refer to this pattern as disambiguation neglect\"）暗示独立概念。\n\n**建议**：定位为 \"extending ambiguity collapse to agentic settings where it produces irreversible policy violations\"（论文 §6.2 已有此方向的一句话，建议前移为段落主题句）。\n\n**W3 [warning, 共识（partial）]** Abstract 应以 confound-free range 为核心效应量\n\nAbstract 以 34.0pp 领头，含 incompleteness confound。R2 建议以 confound-free range (+18.7 to +36.0pp) 为主数字。R1 部分同意，补充 Appendix F 逻辑回归 token count 正系数暗示 confound 若存在为 attenuating（即 34.0pp 可能是下界）。Director 判断：Abstract 第二句已报告 confound-free range，但段首 \"34.0 percentage points\" 作为第一印象可能误导。\n\n**建议**：Abstract 首句改为 confound-free pooled effect（如 \"+31.0pp excluding the confounded type\"），34.0pp 作为全类型参考值移至后文。\n\n**W4 [warning, 共识]** Human validation 样本量不足\n\nn=100, 2 annotators, per-type n≈32-34。Pooled κ=0.735 对 pipeline validation 充分（R2 确认），但 per-type 层面 scopal κ CI=[0.00, 1.00] 几乎无信息量。\n\n**建议**：正文 §4.4 更明确指出 human validation 仅支持 pooled 层面的 pipeline 可靠性，per-type reliability 需更大样本。\n\n**W5 [warning, 共识]** Temperature=0 跨 provider 确定性假设未讨论\n\n不同 provider 对 temperature=0 实现不同（strict argmax vs. near-deterministic with residual stochasticity）。ICC 复制（Appendix D）仅限 OpenAI 模型。\n\n**建议**：Limitations 增加一句讨论 temperature=0 跨 provider 的语义差异及对 ICC 估计的潜在影响。\n\n**W6 [warning, 共识]** BibTeX key mou_ambigswe_2026 与 author 字段不匹配\n\nkey 暗示第一作者 Mou，但 author 字段为 Vijayvargiya 等人。可能是引用更新后 key 未同步。\n\n**要求修复**。\n\n### Minor Issues（Info，不影响评分）\n\n**M1 [info, 共识]** Abstract 信息密度偏高——仍有 5 个具体数字（34.0pp, +18.7 to +36.0pp, 22.4% vs 0.4%, NMI, ≤11%, 40%+）。建议精简至 3 个核心数值：confound-free effect、variance decomposition、convergent violation rate。\n\n**M2 [info, 共识]** Systematic nocuity 与 Berry & Kamsties (2004) 原始定义方向偏差——原始 \"nocuous\" 指 divergent interpretations，论文指 convergent errors（方向相反）。应明确说明术语重新定义。R2 补充：34pp 绝对增幅足以支撑 \"nocuous\" 定性判断（因果效应大小与方差解释比例是不同概念）。Director 采纳 R2 判断——\"nocuous\" 作为定性描述成立，但方向偏差需澄清。\n\n**M3 [info, 共识]** NMI=0.23 绝对水平 modest，\"order of magnitude\" 表述在比值意义上成立（23× > 10×）但绝对值仅为 moderate association。建议同时报告 Cramér's V=0.45 并措辞为 \"moderate but actionable association\"。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n\n1. **SESOI 缺乏外部锚定是核心方法论弱点** (N1)——bootstrap cluster 部分缓解但不充分\n2. **46% 未解释方差需更深入讨论** (N2)——叙事定位合理但候选因素讨论缺失\n3. **ρ=0.09 是最严重的方法论发现** (N3)——C2 有效范围为 robust extremes only\n4. **Taxonomy 非独立贡献** (N4)——C3 未通过多重比较，类型选择标准缺定量依据\n5. **方法论质量高** (Soundness 4)——matched-pair 因果设计、多层 robustness、claims 校准诚实\n6. **新颖性处于 borderline** (Excitement 3)——结果方向可预期，taxonomy 增量，DN 是场景迁移\n7. **Error analysis 编码循环性需人工验证** (W1)\n8. **Human validation pooled 充分，per-type 不足** (W4)\n\n## Reviewer Divergence（交叉回应中已收敛）\n\n以下三个分歧在交叉回应中解决：\n\n1. **SOPBench 衰减解读**：R1 视 34pp→12.6pp 为生态效度弱点；R2 反驳——结构性解释（pre-existing policies、不同域）成立，且七模型扩展复现（+20-33.6pp）是更有力的泛化证据。**Director 判断**：采纳 R2 反驳，SOPBench 是 secondary evidence，model expansion 是 primary generalizability。不升级为 issue。\n\n2. **ICC CI 上界数值**：R1 引用 0.910；R2 更正为 0.940。**Director 判断**：采纳 R2 事实更正，不影响整体评估。\n\n3. **\"Nocuous\" 定性判断是否过度**：R1 质疑歧义仅解释 15.8% 方差是否支撑 \"nocuous\" 标题；R2 反驳——因果效应大小（34pp 绝对增幅）与方差解释比例是不同概念，34pp 在安全场景下足以构成 \"harmful\"。**Director 判断**：采纳 R2 区分，因果效应足以支撑定性判断。M2 仅保留 Berry & Kamsties 方向偏差的术语澄清建议。\n\n---\n\n## Questions\n\n1. 系统性残差 ~46pp 中，作者是否有候选因素的初步探索数据（如对话轮次、任务复杂度与违规率的相关性）？\n2. 同批 annotators 是否既创建又验证了 clause pairs？如果是，如何排除 confirmation bias？\n3. Authorization scope 的 within-judge-group type ranking 是否可通过增加 judge 数量或换用 human judges 稳定？\n4. Failure mode 编码的 AC₁=0.62 中，哪些 mechanism 类别的一致性最低？是否有 per-category 的 κ 分解？\n\n---\n\n## Missing References\n\n本轮无新遗漏（R20 提出的 Ambig-SWE 已补充，其余 R20-W10 文献已核实不威胁核心 claim）。\n\n---\n\n## External Review\n\n外部审稿：未请求（项目配置未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-23 03:22–03:26 UTC）。结果摘要：\n\n- **0 critical, 1 warning, 17 info**\n- **Warning**: pp.4-5 连续两页纯文本（Method 4.1–4.4 及 Experiments/Controls 4.5–5.1），无 display item 穿插。Method 部分缺少方法示意图或 clause pair 构造示例图。\n- **Info highlights**: Figure 1 内子类别标签字号偏小（估计 ≤7pt，低于推荐 8pt）；pp.6-7 display item 密度高与 pp.4-5 形成对比。References 无 [?] 未解析引用，引用格式统一。主文 8 页利用率 100%。\n\n整体排版质量良好，无格式硬伤。建议考虑 Method 部分插入一个 clause pair 构造示例（如 Table 或 Figure），缓解 pp.4-5 的视觉疲劳。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Overall | 3.5 | 3.5 | **3.5** |\n| Soundness | 4 | 4 | **4** |\n| Excitement | 3 | 3 | **3** |\n| Confidence | 4 | 4 | **4** |\n\n**核心判断**：方法论执行到位（Soundness 4），matched-pair 因果设计、多层 robustness checks、诚实的 claims 校准在 agent safety 文献中属上乘。R20 的两个 must-fix（failure mode tautological 循环 + 遗漏 Ambig-SWE）均已有效修复——17× 弱化为 \"order of magnitude\" 并区分 definitional vs empirical mappings；Ambig-SWE 已引用并在 §6.2 和 Limitations 讨论。\n\n但本轮 fresh review 暴露了四个 critical 问题：(1) SESOI ±15pp 的外部锚定缺失使 C2 mid-tier ordering 的有效性依赖于读者对 margin 的接受度；(2) 46% 系统性残差的讨论深度不足，限制了 auditing implications 的说服力；(3) cross-judge type ranking ρ=0.09 严重削弱 C2——partial ordering 实质退化为两个极端点；(4) taxonomy 新颖性不足，C3 检验失败未在 Intro 反映。新颖性处于 borderline——核心结果（歧义增加违规）方向可预期，taxonomy 为增量贡献，disambiguation neglect 是 ambiguity collapse 的场景迁移。\n\n**接收条件**：如果作者能 (1) Abstract/Conclusion 限定 C2 为 \"robust extremes\" + margin 条件，(2) Discussion 增加残差候选因素讨论，(3) §3 补充类型选择操作标准和 C3 inconclusive 说明，(4) Abstract 以 confound-free effect 为主数字，(5) 修复 bib key，本文可达 Conference 水准（4.0）。\n\n**与 R20 对比**：R20 的两个 critical（tautological + Ambig-SWE）已修复，方法论在 failure mode 分析上有实质改进。但 fresh review 发现的新 criticals（SESOI 锚定、ρ=0.09、未解释方差、taxonomy novelty）使总评维持 3.5。这些问题主要是解释/呈现层面的（而非基础方法论缺陷），修复路径清晰。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 首句 34.0pp 含 incompleteness confound → 建议以 confound-free pooled effect 领头 (W3)\n- 5 个具体数字信息密度偏高 → 精简至 3 个 (M1)\n- \"partial ordering\" 未附 margin 条件 (N1)\n\n### §1 Introduction\n- Contribution (2) \"order of magnitude\" 比值成立但 NMI=0.23 绝对值 modest → 考虑补充 Cramér's V=0.45 (M3)\n- 三条 contribution 均以因果研究和方差分解为核心，未将 taxonomy 列为独立贡献——这是正确的处理 (N4 context)\n\n### §2 Related Work\n- Ambig-SWE 已引用且讨论充分 ✓\n- \"disambiguation neglect\" 的定位可在此段更早明确为 ambiguity collapse 的 agentic extension (W2)\n\n### §3 Ambiguity Taxonomy\n- 类型选择标准缺定量依据（为何这六类？排除 ellipsis/pragmatic implicature 的量化理由？）(N4)\n- 建议末尾明确声明 taxonomy 是实验 IV 的操作化，C3 层级假说未通过多重比较校正 (N4)\n\n### §4 Method\n- §4.4 Human validation per-type 不确定性在正文传达不足 (W4)\n- §4.6 SESOI ±15pp 缺外部锚定 (N1)\n\n### §5 Results\n- §5.1 方差全景图中 ~46pp 系统残差的候选因素讨论缺失 (N2)\n- §5.2 ρ=0.09 disclosure 已在正文——这是良好实践。但 Abstract/Conclusion 的 \"partial ordering\" 应匹配此限定 (N3)\n- §5.2 C2 有效范围应明确为 \"robust extremes only\" (N3)\n\n### §6 Error Analysis\n- AC₁=0.62 低于 good agreement → 需人工验证 (W1)\n- 2/6 definitional vs 4/6 empirical 区分是 R20 后的改进 ✓\n- §6.2 disambiguation neglect 定位调整建议 (W2)\n- §6.3 \"systematic nocuity\" 与 Berry & Kamsties 原始方向偏差需澄清 (M2)\n\n### §7 Discussion\n- \"clause-level auditing addresses the largest actionable component\" — 增加残差候选因素讨论 (N2)\n- Temperature=0 跨 provider 差异 (W5)\n\n### §9 Limitations\n- 整体质量高 ✓\n- 建议增加 temperature=0 跨 provider 讨论 (W5)\n- Failure mode 编码的人工验证缺失可更显著标注 (W1)\n\n### References\n- mou_ambigswe_2026 key 与 author 不匹配 → 修复 (W6)\n\n### Appendix\n- Appendix K 三法官 pooled ρ=0.71-0.89 vs within-group ρ=0.09 的差异值得在正文 §5.2 简要提及，帮助读者理解问题根源在 judge-model pairing 而非 judge bias (N3)",
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 1884 · 2026-05-23T03:51:52.317793+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4014
}
```

</details>

---


### Assistant

_source line 1885 · 2026-05-23T03:52:02.569567+00:00_

Round 21 审稿报告已投递。

**本轮结论：3.5 / 5（Borderline Conference）**

关键发现：
- **4 个 critical**：SESOI 外部锚定缺失、46% 残差讨论不足、cross-judge ρ=0.09 严重削弱 C2、taxonomy 新颖性不足
- **6 个 warning**：LLM 编码循环性、DN 场景迁移定位、Abstract confound-free 效应量、human validation per-type 不足、temperature=0 讨论、bib key 错误
- **3 个 info**：Abstract 数字密度、nocuity 术语方向、NMI 绝对水平

R20 的两个 must-fix（tautological 循环 + Ambig-SWE 遗漏）已有效修复。本轮新 criticals 主要在解释/呈现层面，修复路径清晰——如果 N1-N4 全部修复，论文可达 4.0（Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 179

## Round 179

60 recorded events


### User

_source line 1886 · 2026-05-23T04:23:45.636636+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1887 · 2026-05-23T04:23:50.909858+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1888 · 2026-05-23T04:23:50.960894+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1889 · 2026-05-23T04:23:58.037849+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1890 · 2026-05-23T04:23:58.088551+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1891 · 2026-05-23T04:24:00.603139+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1892 · 2026-05-23T04:24:01.155746+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1893 · 2026-05-23T04:24:01.156113+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1894 · 2026-05-23T04:24:01.206605+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1895 · 2026-05-23T04:24:05.925084+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 1896 · 2026-05-23T04:24:08.134350+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1897 · 2026-05-23T04:24:08.185283+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1898 · 2026-05-23T04:24:08.587114+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "experiment_plan.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "experiment_plan.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1899 · 2026-05-23T04:24:13.556307+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's information about EMNLP 2026 call for papers submission guidelines related to ARR:

## Key Guidelines:

**Paper Types and Scope:**
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

**Presentation Requirements:**
All accepted papers must be presented at the conference to appear in the proceedings, with both in-person and virtual presentation options.

**ARR-Specific Policy:**
Fo
…[truncated 611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 7631
}
```

</details>

---


### Tool result

_source line 1900 · 2026-05-23T04:24:13.556827+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4969
}
```

</details>

---


### Tool call

_source line 1901 · 2026-05-23T04:24:19.534910+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1902 · 2026-05-23T04:24:19.986928+00:00_

1	\begin{abstract}
2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. We present a matched-pair causal study on $\tau^2$-bench with 300 ambiguous/unambiguous clause pairs spanning a six-type taxonomy, evaluated across five models. Ambiguous clauses are consistently nocuous (i.e., harmful), increasing violation rates by 34.0 percentage points under controlled synthetic conditions ($+$18.7 to $+$36.0\,pp excluding the confounded incompleteness type). Clause wording explains 22.4\% of violation variance versus 0.4\% for type; however, type predicts failure \emph{mechanism} an order of magnitude more strongly than violation rate, establishing the taxonomy as a diagnostic tool. Error analysis reveals disambiguation neglect ($\leq$11\% awareness) and \emph{systematic nocuity}: over 40\% of clauses triggering model-convergent violations. These results, observed in customer-service policy domains under synthetic ambiguity injection, motivate clause-level policy auditing and type-targeted diagnosis for policy-governed deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1903 · 2026-05-23T04:24:19.987424+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1904 · 2026-05-23T04:24:20.490002+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 2002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1905 · 2026-05-23T04:24:20.490519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1906 · 2026-05-23T04:24:21.444450+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_l
…[truncated 4048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1907 · 2026-05-23T04:24:21.444897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 1908 · 2026-05-23T04:24:21.947075+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers (Table~\ref{tab:taxonomy}), selected from \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types) based on three design criteria: (1)~theoretical attestation in prior RE literature \citep{massey_ambiguity_re_2014,berry_kamsties_2004,drip_r_2026}, (2)~amenability to minimal-pair construction without altering clause semantics beyond the target ambiguity, and (3)~mutual exclusivity for unambiguous IV assignment. Types such as ellipsis and pragmatic implicature were excluded because they resist minimal-pair construction within the single-clause policy format.
7	
8	\begin{table}[t]
9	\centering
10	\footnotesize
11	\caption{Six-type ambiguity taxonomy. Disambiguation channel indicates the primary mechanism required to resolve the ambiguity.}
12	\label{tab:taxonomy}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}llll@{}}
15	\toprule
16	\textbf{Type} & \textbf{Layer} & \textbf{Definition} & \textbf{Disambig.\ Channel} \\
17	\midrule
18	Lexical & Ling. & Word/phrase admits multiple senses & Context \\
19	Scopal & Ling. & Quantifier/operator scope underdetermined & Bracketing \\
20	Coreferential & Ling. & Pronoun/NP referent is ambiguous & Resolution \\
21	Auth.\ Scope & Spec. & Permission boundary is vague & Boundary def. \\
22	Incompleteness & Spec. & Required information is absent & Content addition \\
23	Cond.\ Prec. & Spec. & Rules conflict under certain conditions & Priority rule \\
24	\bottomrule
25	\end{tabular}}%
26	\end{table}
27	
28	\paragraph{Linguistic layer.} These types operate at the syntactic or 
…[truncated 2646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1909 · 2026-05-23T04:24:21.947513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1910 · 2026-05-23T04:24:22.399437+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300; Cohen's $\kappa = 0.95$ on six-type classification); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We
…[truncated 5079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1911 · 2026-05-23T04:24:22.399927+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1912 · 2026-05-23T04:24:22.952319+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around three analyses: the binary ambiguity effect (C1), the type partial ordering (C2, including the inconclusive layer effect C3), and the model$\times$type interaction (C4). C1 and C2 are primary claims; C4 is exploratory.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS avoids ordering dependence in our unbalanced design; logistic regression (Appendix~\ref{app:regression}) confirms concordant results (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}).} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (of which $\sim$15\% is run-to-run stochasticity and $\sim$46\% systematic-but-unmeasured factors; ICC replication in Appendix~\ref{app:residual}). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; controlling for token count changes no type's predicted effect by more than
…[truncated 7217 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1913 · 2026-05-23T04:24:23.605324+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template double blind anonymity",
  "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit template double blind anonymity",
    "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool result

_source line 1914 · 2026-05-23T04:24:35.885443+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template double blind anonymity"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LM Playschool: Improving Language Models through Learning from Dialogue Interaction | ACL Member Portal","url":"https://www.aclweb.org/portal/content/lm-playschool-improving-language-models-through-learning-dialogue-game-interaction"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"}]

Let me search for more specific information about the main EMNLP 2026 paper submission requirements.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal
…[truncated 4580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 12280
}
```

</details>

---


### Tool call

_source line 1915 · 2026-05-23T04:24:45.324943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1916 · 2026-05-23T04:24:45.375917+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes (Gwet's AC$_1$ $= 0.62$, $\kappa = 0.52$ \citep{gwet_2014,cohen_1960}). Using LLMs to code LLM failures introduces circularity risk; however, mutual information between type (exogenous) and mechanism labels ($I(\text{type}; \text{mechanism}) = 0.41$ bits, $V = 0.45$; Appendix~\ref{app:type_mechanism}) provides structural evidence against this. Two of the six type--mechanism mappings reflect partial definitional affinity (authorization scope$\to$boundary violation, incompleteness$\to$gap-filling); the remaining four (e.g., scopal$\to$structural misparse, 82.7\% cross-model consistency) are empirically derived.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse}: the agent commits to an incorrect parse, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}. Dominates scopal (5/5), conditional precedence (4/5), and coreferential (3/5).
13	
14	\emph{Information gap-filling}: the agent fills missing information with plausible but incorrect defaults. Dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation}: the agent exceeds permission boundaries when authorization scope is underspecified; 69.2\% involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial). Dominates authorization scope exclusively (5/5).
17	
18	All dominant modes achieve $\geq$3/5 model consistency; scopal and authorization scope are unanimous (5/5).
19	
20	\subsection{Disambiguation Neglect}
21	\label{sec:dn}
22	
23	Agents rarely recogniz
…[truncated 1580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1917 · 2026-05-23T04:24:45.376599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1918 · 2026-05-23T04:24:45.376799+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Our results support a \emph{differential nocuity} hypothesis \citep{berry_kamsties_2004,willis_nocuous_2008}: the binary effect is domain-robust ($p = 0.187$) but type-specific profiles require per-domain calibration ($\rho = 0.26$). Of the 60.8\% unexplained variance, $\sim$15\% is stochastic and $\sim$46\% systematic (ICC $= 0.749$; Appendix~\ref{app:residual}). In customer-service domains, clause-level auditing addresses the largest \emph{actionable} component (22.4\%) but not the majority of outcome variance. Candidate sources of the $\sim$46\% systematic residual include conversation trajectory complexity, task difficulty gradients, and latent policy structure beyond the clause level; conversation trajectory is the most readily measurable next target.
6	
7	\paragraph{Taxonomy as diagnostic tool.}
8	Type membership explains only 0.4\% of violation variance versus 22.4\% for clause wording; however, it predicts failure \emph{mechanism} an order of magnitude more strongly than violation rate (NMI $= 0.23$ vs.\ $0.01$, Cram\'{e}r's $V = 0.45$; Appendix~\ref{app:type_mechanism}), validating the taxonomy as a diagnostic tool: each type maps to a dominant failure mechanism (\S\ref{sec:analysis}).
9	
10	\paragraph{Prompt-based mitigation.}
11	Prompt-based mitigation is type-dependent (effective for authorization scope and lexical but not incompleteness; Appendix~\ref{app:mitigation}), reinforcing policy-design over prompt-level fixes.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1919 · 2026-05-23T04:24:45.427220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1920 · 2026-05-23T04:24:45.427723+00:00_

1	\section{Conclusion}
2	
3	Under controlled synthetic conditions, policy ambiguity increases agent violations by 34.0\,pp ($+$18.7 to $+$36.0\,pp excluding the confounded incompleteness type). Clause wording explains 22.4\% of variance versus 0.4\% for type, while the taxonomy predicts failure mechanisms an order of magnitude better than violation rate. With $>$89\% disambiguation neglect and over 40\% convergent violations, clause-level auditing is critical for policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1921 · 2026-05-23T04:24:45.428049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1922 · 2026-05-23T04:24:45.428442+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Ecological validity.} Our ambiguity pairs are synthetically constructed via templates (\S\ref{sec:method}), so the 34.0\,pp effect is an upper bound under controlled conditions; naturally occurring ambiguity in deployed policies may produce smaller effects. The SOPBench replication ($+$12.6\,pp), while directionally consistent, also uses researcher-constructed benchmarks. Neither study measures ambiguity prevalence in real-world policy documents; a dose-response study varying ambiguity density in production policies would help calibrate practical impact.
5	
6	\paragraph{Scope.} We evaluate seven API-accessible models from six providers (Appendix~\ref{app:model_expansion}); smaller open-source models (7B--70B) may exhibit different vulnerability patterns. $\tau^2$-bench covers retail and airline customer service only---effects in other domains remain untested. Cross-domain consistency holds for the overall effect (C1, interaction $p = 0.19$) and model ranking ($\rho = 0.90$, $p = 0.037$), but type rankings vary across domains ($\rho = 0.26$, $p = 0.62$); conditional precedence in particular differs by 22\,pp between retail and airline, further motivating the partial-ordering framing. Different providers implement temperature$=$0 with varying determinism (strict argmax vs.\ near-deterministic sampling); our ICC replication (Appendix~\ref{app:residual}) covers only OpenAI models, and cross-provider stochasticity may affect reproducibility estimates. Our matched-pair design requires synthetic ambiguity construction, which may not capture the full distribution of naturally occurring ambiguities; realism validation (\S\ref{sec:method}) confirms lexical comparability but cannot rule out distributional gaps. Coreferential ambiguity was excluded from mitigation and replication experiments due to benchmark-specific structural constraints (Appendix~\ref{app:mitigation}); consequently, the confound-free lower bo
…[truncated 2855 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1923 · 2026-05-23T04:24:45.430079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 1924 · 2026-05-23T04:24:45.430401+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1925 · 2026-05-23T04:24:45.531402+00:00_

1	@inproceedings{li_ambiguity_taxonomy_2024,
2	  title={A Taxonomy of Ambiguity Types for {NLP}},
3	  author={Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.},
4	  booktitle={Proceedings of EACL 2024},
5	  year={2024}
6	}
7	
8	@inproceedings{massey_ambiguity_re_2014,
9	  title={Identifying and Classifying Ambiguity for Regulatory Requirements},
10	  author={Massey, Aaron K. and Rutledge, Richard L. and Ant{\'o}n, Annie I. and Swire, Peter P.},
11	  booktitle={22nd IEEE International Requirements Engineering Conference (RE)},
12	  year={2014},
13	  doi={10.1109/RE.2014.6912250}
14	}
15	
16	@techreport{berry_kamsties_2004,
17	  title={From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook},
18	  author={Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.},
19	  institution={University of Waterloo},
20	  year={2004}
21	}
22	
23	@inproceedings{chantree_2006,
24	  title={Identifying Nocuous Ambiguities in Natural Language Requirements},
25	  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},
26	  booktitle={14th IEEE International Requirements Engineering Conference (RE)},
27	  year={2006}
28	}
29	
30	@incollection{wasow_ambiguity_2005,
31	  title={The Puzzle of Ambiguity},
32	  author={Wasow, Thomas and Perfors, Amy and Beaver, David},
33	  booktitle={Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe},
34	  publisher={CSLI Publications},
35	  year={2005}
36	}
37	
38	@article{kennedy_vagueness_2007,
39	  title={Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives},
40	  author={Kennedy, Christopher},
41	  journal={Linguistics and Philosophy},
42	  volume={30},
43	  number={1},
44	  pages={1--45},
45	  year={2007},
46	  doi={10.1007/s10988-006-9008-0}
47	}
48	
49	@article{willis_nocuous_2008,
50	  title={Automatic Identification of Nocuous Ambiguity},
51	  author={Willis, Alistair and Chantree, Francis and De Roeck
…[truncated 17467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1926 · 2026-05-23T04:24:45.733134+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 37141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1927 · 2026-05-23T04:24:55.421084+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1928 · 2026-05-23T04:24:55.522006+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1929 · 2026-05-23T04:25:01.043624+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1930 · 2026-05-23T04:25:02.148694+00:00_

## Review Issues Tracker — policy_ambiguity_safety
## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
## Venue: EMNLP 2026 via ARR May cycle
## Latest Round: 21

# ============================================================
# R21 ISSUES — ALL RESOLVED (Reviewer verified 12/13 PASS + 1 CONDITIONAL PASS fixed)
# ============================================================

- id: "R21-N1"
  summary: "SESOI ±15pp 缺乏外部锚定，C2 mid-tier 在 ±10pp 下瓦解"
  category: method
  severity: critical
  status: resolved
  resolution: "§4.6 加 Lakens (2017) 两项原则性锚定; Intro partial ordering 加 ±15pp margin 限定; 无 clinical/financial 类比. Reviewer PASS."
  resolution_round: 21
  first_raised_round: 20
  last_seen_round: 21
  mentions:
    - round: 20
      note: "R20 列为 W1 (warning)"
    - round: 21
      note: "升级为 critical; 要求 §4.6 承认无行业标准 + Abstract margin 限定"
  action_items:
    - round: 21
      action: "§4.6 加 Lakens (2017) SESOI 原则; Abstract/Conclusion 加 margin 限定; 不引用 clinical/financial 类比"
      assigned_to: "main_agent"
      status: "done"

- id: "R21-N2"
  summary: "46% 系统性残差候选因素讨论深度不足"
  category: writing
  severity: critical
  status: resolved
  resolution: "Discussion 加候选因素 (conversation trajectory, task difficulty, policy structure); pp→% 单位统一. Reviewer CONDITIONAL PASS → 修复单位后 PASS."
  resolution_round: 21
  first_raised_round: 18
  last_seen_round: 21
  mentions:
    - round: 19
      note: "R19-W3: 加了方差全景图一句"
    - round: 21
      note: "升级为 critical; 要求列候选因素"
  action_items:
    - round: 21
      action: "Discussion 加候选因素列表; experiments.tex+discussion.tex 统一 ~15%/~46% 单位"
      assigned_to: "main_agent+director"
      status: "done"

- id: "R21-N3"
  summary: "Cross-judge type ranking ρ=0.09 严重削弱 C2 partial ordering"
  category: method
  severity: critical
  status: resolved
  resolution: "§5.2 加 judge-model pairing 解释 + pooled ρ≥0.71; Intro partial ordering 加 ±15pp 限定. Reviewer PASS."
  resolution_round: 21
  first_raised_round: 20
  las
…[truncated 7229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool call

_source line 1931 · 2026-05-23T04:25:02.250368+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_22/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_22/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1932 · 2026-05-23T04:25:03.058788+00:00_

-rw-r--r-- 1 ubuntu ubuntu 457448 May 23 04:20 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_22/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 808
}
```

</details>

---


### Tool call

_source line 1933 · 2026-05-23T04:25:03.109352+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/project_config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/project_config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review"
  }
}
```

</details>

---


### Tool result

_source line 1934 · 2026-05-23T04:25:03.160012+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1935 · 2026-05-23T04:25:06.729382+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"project_config*\" -o -name \"config.yaml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"project_config*\" -o -name \"config.yaml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 1936 · 2026-05-23T04:25:06.880476+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/configs/config.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1937 · 2026-05-23T04:25:11.951618+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/projects/policy_ambiguity_safety.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/config.yaml 2>/dev/null || find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config -name \"*policy*\" 2>/dev/null | head -5",
  "description": "Find project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/projects/policy_ambiguity_safety.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/config.yaml 2>/dev/null || find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config -name \"*policy*\" 2>/dev/null | head -5",
    "description": "Find project config"
  }
}
```

</details>

---


### Tool result

_source line 1938 · 2026-05-23T04:25:12.054528+00:00_

execution:
  account: ubuntu
  project_path: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts
  servers:
  - localhost
feishu:
  chat_id: oc_10fa2e89afc5e9b8a13613245e008dd9
  check_references: false
  operational_chat_id: oc_c58486bc9afb8c730ded5e31c0e7d639
  review_mode: fresh
  review_paper_path: projects/policy_ambiguity_safety/docs/paper/main.tex
  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_22/submitted.pdf
  review_round: 22
  review_supplementary_paths: ''
  submission_chat_id: oc_967344d166ba485ad606d14379e69d85
project:
  created_at: '2026-05-20T07:09:49.941Z'
  description: 'From Ambiguity Type to Safety Severity: Causal Mapping of Linguistic
    Policy Ambiguities to Agent Safety Violations'
  name: policy_ambiguity_safety
  phase: research
  source_idea_id: idea_034
venue: emnlp-2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1939 · 2026-05-23T04:25:31.633416+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 1940 · 2026-05-23T04:25:53.200341+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21566
}
```

</details>

---


### Tool call

_source line 1941 · 2026-05-23T04:25:53.301136+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，Long paper 正文 8 页限制，参考文献不限页数\n- **匿名**: double-blind\n- **评分标准**: ARR Overall Assessment（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文\n- TeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_22/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 实验设计与因果推断\n- matched-pair 设计是否真正建立因果关系？内部有效性是否充分？\n- 300 对 clause pairs 的构建流程是否存在系统性偏差？\n- perturbation control (n=300) 是否充分排除非语义因素？\n- incompleteness 的 information-addition confound 处理是否令人信服？\n\n### 2. 统计分析\n- Type III SS 方差分解的合理性（22.4% clause, 0.4% type, 15.8% condition）\n- SESOI ±15pp 的选择依据是否充分？sensitivity analysis 是否覆盖关键范围？\n- McNemar test + TOST equivalence testing 的方法学适当性\n- Holm-Bonferroni 校正的族定义是否合理？\n- ICC replication (0.919) 的覆盖范围——仅 OpenAI 模型，能否推广？\n\n### 3. 评估管道可靠性\n- cross-judge 设计（GPT-5.4 judging Claude/Qwen3; GPT-4.1 judging GPT-5.4/DeepSeek）的 bias 控制\n- authorization scope κ=0.385 低一致性对 C4 interaction 结论的影响\n- human validation (n=100) 样本量是否足够支撑 pipeline 可靠性声明？\n- failure mode coding 的 LLM 循环性风险评估\n\n### 4. 外部有效性\n- 仅在 τ²-bench（retail + airline）上的结果能否推广？\n- SOPBench replication (+12.6pp) 效应量大幅缩小的解释是否令人信服？\n- 7 个模型覆盖的架构多样性是否足够？\n\n请完成后输出完整审稿报告，结构如下：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，每条标注 severity: Must-Fix / Should-Fix / Minor）\n4. Questions for Authors（逐条）\n5. Missing References（如有）\n6. Overall Assessment（评分 + 置信度 + 一句话总评）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，Long paper 正文 8 页限制，参考文献不限页数\n- **匿名**: double-blind\n- **评分标准**: ARR Overall Assessment（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文\n- TeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_22/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 实验设计与因果推断\n- matched-pair 设计是否真正建立因果关系？内部有效性是否充分？\n- 300 对 clause pairs 的构建流程是否存在系统性偏差？\n- perturbation control (n=300) 是否充分排除非语义因素？\n- incompleteness 的 information-addition confound 处理是否令人信服？\n\n### 2. 统计分析\n- Type III SS 方差分解的合理性（22.4% clause, 0.4% type, 15.8% condition）\n- SESOI ±15pp 的选择依据是否充分？sensitivity analysis 是否覆盖关键范围？\n- McNemar test + TOST equivalence testing 的方法学适当性\n- Holm-Bonferroni 校正的族定义是否合理？\n- ICC replication (0.919) 的覆盖范围——仅 OpenAI 模型，能否推广？\n\n### 3. 评估管道可靠性\n- cross-judge 设计（GPT-5.4 judging Claude/Qwen3; GPT-4.1 judging GPT-5.4/DeepSeek）的 bias 控制\n- authorization scope κ=0.385 低一致性对 C4 interaction 结论的影响\n- human validation (n=100) 样本量是否足够支撑 pipeline 可靠性声明？\n- failure mode coding 的 LLM 循环性风险评估\n\n### 4. 外部有效性\n- 仅在 τ²-bench（retail + airline）上的结果能否推广？\n- SOPBench replication (+12.6pp) 效应量大幅缩小的解释是否令人信服？\n- 7 个模型覆盖的架构多样性是否足够？\n\n请完成后输出完整审稿报告，结构如下：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，每条标注 severity: Must-Fix / Should-Fix / Minor）\n4. Questions for Authors（逐条）\n5. Missing References（如有）\n6. Overall Assessment（评分 + 置信度 + 一句话总评）"
  }
}
```

</details>

---


### Tool result

_source line 1942 · 2026-05-23T04:26:14.613798+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21312
}
```

</details>

---


### Tool call

_source line 1943 · 2026-05-23T04:26:14.764717+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性/完整性**审查。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，Long paper 正文 8 页限制，参考文献不限页数\n- **匿名**: double-blind\n- **评分标准**: ARR Overall Assessment（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文\n- TeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_22/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- \"first matched-pair causal study of policy ambiguity's safety impact\" 这一声明是否成立？与 DRIP-R (2026)、PolicyBank (2026) 等 concurrent work 的区分是否清晰？\n- variance decomposition (22.4% clause vs 0.4% type) 是否构成足够的贡献？\n- \"disambiguation neglect\" 作为概念的独立性——论文自己承认是 ambiguity collapse 的场景迁移，是否还够 novel？\n- taxonomy 定位为 experimental instrument 而非 classification standard——这一策略是否损害了可引用性？\n\n### 2. Related Work 覆盖\n- 近期 agent safety 文献覆盖是否充分？特别是：\n  - ASPI (Sehwag et al., 2026) 关于 clarification seeking 引入 prompt injection 的 tension\n  - Ambig-SWE (Vijayvargiya et al., 2026) 的 interactive disambiguation\n  - 是否有其他重要遗漏？\n- 与 RE (requirements engineering) 文献的桥接是否充分？\n- psycholinguistics 引用是否恰当且必要？\n\n### 3. 写作质量与叙事结构\n- Abstract 信息密度是否合适？（当前含 34.0pp、22.4%/0.4%、≤11%、40% 等多个数字）\n- Introduction 的 narrative flow：从 opening example → gap → method → results 是否连贯？\n- Discussion 是否充分讨论了 implications？\n- Limitations 的覆盖是否全面？是否有未讨论的重要限制？\n- Conclusion 是否过于简短？\n\n### 4. 格式合规\n- 正文是否在 8 页以内？\n- double-blind 合规：是否有作者身份泄露？\n- ACL template 使用是否正确？（\\usepackage[review]{acl}）\n- 参考文献格式是否一致？BibTeX 条目是否完整？\n- Limitations section 是否存在且位于正文中（非 appendix）？\n- 图表标题是否自解释？表格是否使用 booktabs？\n\n### 5. Taxonomy 设计\n- 六类分类的互斥性和完备性\n- linguistic vs specification 两层划分的理论依据\n- 排除的类型（ellipsis, pragmatic implicature）的理由是否充分？\n- 与 Li et al. (2024) 11-type taxonomy 的映射是否清晰？\n\n请完成后输出完整审稿报告，结构如下：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，每条标注 severity: Must-Fix / Should-Fix / Minor）\n4. Questions for Authors（逐条）\n5. Missing References（如有）\n6. Overall Assessment（评分 + 置信度 + 一句话总评）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性/完整性**审查。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，Long paper 正文 8 页限制，参考文献不限页数\n- **匿名**: double-blind\n- **评分标准**: ARR Overall Assessment（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文\n- TeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_22/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- \"first matched-pair causal study of policy ambiguity's safety impact\" 这一声明是否成立？与 DRIP-R (2026)、PolicyBank (2026) 等 concurrent work 的区分是否清晰？\n- variance decomposition (22.4% clause vs 0.4% type) 是否构成足够的贡献？\n- \"disambiguation neglect\" 作为概念的独立性——论文自己承认是 ambiguity collapse 的场景迁移，是否还够 novel？\n- taxonomy 定位为 experimental instrument 而非 classification standard——这一策略是否损害了可引用性？\n\n### 2. Related Work 覆盖\n- 近期 agent safety 文献覆盖是否充分？特别是：\n  - ASPI (Sehwag et al., 2026) 关于 clarification seeking 引入 prompt injection 的 tension\n  - Ambig-SWE (Vijayvargiya et al., 2026) 的 interactive disambiguation\n  - 是否有其他重要遗漏？\n- 与 RE (requirements engineering) 文献的桥接是否充分？\n- psycholinguistics 引用是否恰当且必要？\n\n### 3. 写作质量与叙事结构\n- Abstract 信息密度是否合适？（当前含 34.0pp、22.4%/0.4%、≤11%、40% 等多个数字）\n- Introduction 的 narrative flow：从 opening example → gap → method → results 是否连贯？\n- Discussion 是否充分讨论了 implications？\n- Limitations 的覆盖是否全面？是否有未讨论的重要限制？\n- Conclusion 是否过于简短？\n\n### 4. 格式合规\n- 正文是否在 8 页以内？\n- double-blind 合规：是否有作者身份泄露？\n- ACL template 使用是否正确？（\\usepackage[review]{acl}）\n- 参考文献格式是否一致？BibTeX 条目是否完整？\n- Limitations section 是否存在且位于正文中（非 appendix）？\n- 图表标题是否自解释？表格是否使用 booktabs？\n\n### 5. Taxonomy 设计\n- 六类分类的互斥性和完备性\n- linguistic vs specification 两层划分的理论依据\n- 排除的类型（ellipsis, pragmatic implicature）的理由是否充分？\n- 与 Li et al. (2024) 11-type taxonomy 的映射是否清晰？\n\n请完成后输出完整审稿报告，结构如下：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，每条标注 severity: Must-Fix / Should-Fix / Minor）\n4. Questions for Authors（逐条）\n5. Missing References（如有）\n6. Overall Assessment（评分 + 置信度 + 一句话总评）"
  }
}
```

</details>

---


### Tool result

_source line 1944 · 2026-05-23T04:26:16.181608+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1416
}
```

</details>

---


### Assistant

_source line 1945 · 2026-05-23T04:26:19.842316+00:00_

Round 1 已启动：
- 视觉审查 Agent 已派发（fire-and-forget）
- Reviewer 1（方法严谨性）已分配
- Reviewer 2（新颖性/完整性）已分配

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 180

## Round 180

2 recorded events


### User

_source line 1946 · 2026-05-23T04:35:17.542921+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性审查

### 论文信息
**标题**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety
**Venue**: EMNLP 2026 (ARR May cycle)

---

## 1. Summary

本文提出一项 matched-pair 因果研究，在 τ²-bench（零售+航空客服）上构建 300 对歧义/非歧义条款对，覆盖六类歧义分类法，在五个前沿模型上评估。核心发现：歧义条款使违规率增加 34.0pp（排除 incompleteness confound 后为 +18.7 至 +36.0pp）；条款措辞（22.4%）远比类型（0.4%）更能解释方差；类型预测失败机制（NMI=0.23）比预测违规率（NMI=0.01）强一个数量级。

---

## 2. Strengths

**S1: 严格的 matched-pair 因果设计。** 最小编辑条款对构建（§4.2）配合高标注一致性（κ=0.95, 96% 初始一致率）和 perturbation control（n=300, Δ=−0.67pp, §4.5）建立了真正的因果推断，超越了前人工作的相关性证据。matched-pair 设计优雅地消除了系统性 judge 偏差对处理效应的影响。

**S2: 信息量丰富的方差分解。** Type III SS 分析（§5.1）定量分离了条款措辞（22.4%）、类型（0.4%）、条件（15.8%）和残差（60.8%）的贡献，并进一步将残差分解为 ~15% 随机噪声和 ~46% 系统性未测量因素（Appendix X, ICC(1)=0.749）。这为审计投入方向提供了可操作的指引。

**S3: 对方法论复杂性的透明处理。** 本文对局限性的坦诚程度超出常见水平：authorization scope 低 κ=0.385（§4.4, Figure 3 caption）、cross-judge-group 类型排名不一致（ρ=0.09, §5.2）、incompleteness confound（§4.5, Appendix F）、severity threshold 未预注册（§9）。这种透明度增强而非削弱了论文的可信度。

**S4: 分类法的诊断价值重构。** 类型预测失败机制（NMI=0.23）比预测违规率（NMI=0.014）强 16.8×（Appendix S），将分类法从风险预测器重构为诊断工具——这是概念上的重要区分，具有实际意义。

**S5: 全面的稳健性分析。** 七级 TOST 敏感性分析（Appendix A）、bootstrap 聚类（Appendix I）、三个 judge 家族的交叉验证（Fleiss' κ=0.717, Appendix W）、替代严重度阈值（Appendix C）和跨域分析（Appendix U）提供了广泛的稳健性证据。

**S6: 可操作的缓解实验。** 缓解实验（Appendix B）展示了类型依赖的 prompt 有效性（authorization scope −18.0pp vs incompleteness −3.3pp n.s.），直接指导部署策略。

---

## 3. Weaknesses

**W1 [Should-Fix]: SOPBench 复制显示 63% 效应压缩，缺乏原则性归因。**
- 具体位置：§5.1, Appendix V
- 问题：τ²-bench 主效应 34.0pp，SOPBench 仅 +12.6pp（Table 16）。论文提供三个事后解释（测量粒度差异、负向任务设计、结构差异），但未量化各因素的贡献。对于框定为安全相关发现的论文，3× 的效应量差异值得关注。如果测量粒度是主要驱动因素，34.0pp 是 benchmark-specific 的数字，不是歧义的内在属性；如果领域差异驱动压缩，则对非客服场景的推广存疑。
- 建议：在 τ²-bench 上以 constraint-level 重新分析（类比 SOPBench 指标），隔离测量粒度效应。或提供原则性论证说明方向一致性为何足以支撑安全论述。

**W2 [Should-Fix]: Authorization scope 测量不可靠性渗透 C4 交互发现。**
- 具体位置：§5.3, Figure 3, Appendix M/W/X
- 问题：C4 model×type 交互完全由 authorization scope 驱动（排除后 p=0.97, Appendix M）。该类型同时具有：最低 inter-judge κ（0.385, §4.4）、最高 cross-judge 方差（41.6%–65.6%, Appendix W）、within-replication ICC≈0（Appendix X）、跨 judge 组排名不一致的唯一驱动因素（ρ=0.09→0.90 排除后, §5.2）。四个独立指标同时指向测量不稳定，C4 的统计显著性（p=0.006）可能被差异化测量噪声所膨胀。
- 论文已标记 C4 为 "[Exploratory]" 并提供了充分 caveats，但在 §5.3 和 Figure 3 中的呈现规格（独立小节+专门图表）仍暗示这是一个实质性发现。
- 建议：模拟 κ=0.385 噪声水平下交互 χ² 的期望假阳性率，以区分真实信号与测量伪影。

**W3 [Should-Fix]: ICC 复制仅覆盖 OpenAI 家族，但残差方差分解应用于所有模型。**
- 具体位置：§4.5, Appendix X
- 问题：ICC=0.919（§4.5）和残差分解（Appendix X, ICC(1)=0.749）均在 OpenAI 内计算。论文确认了这一限制（§9），但仍使用这些数字来刻画所有五个模型的 60.8% 残差。不同提供商以不同方式实现 temperature=0（strict argmax vs near-deterministic sampling），跨提供商随机性可能更高。如果随机成分实际占比更大，"~46% 系统性未测量因素"的解释将发生变化。
- 建议：在至少一个非 OpenAI 模型上进行小规模 ICC 复制（如 30 对×3 replicate），或明确标注残差分解的适用范围。

**W4 [Should-Fix]: SESOI ±15pp 缺乏领域接地的论证。**
- 具体位置：§4.6
- 问题：论文承认不存在行业标准（§4.6），并以两个标准论证 ±15pp：（a）超过测量噪声 2× 以上——这是精度论证，非实际显著性论证；（b）低于此阈值的差异不需要不同的缓解策略——这是作者判断，无经验支撑。在安全关键评估中，10pp 的违规率增加可能具有实际意义（如从 30% 到 40%）。七级敏感性分析（Appendix A）部分缓解了这一问题。
- 建议：补充讨论 ±15pp 在高风险部署场景中是否过于宽松，或提供基于后果严重度的 SESOI 校准。

**W5 [Should-Fix]: Token count 是 incompleteness information-addition confound 的粗糙代理。**
- 具体位置：Appendix F
- 问题：逻辑回归控制 token count（β=+0.027, p=0.003），论文将正系数解释为反驳信息添加假设。但 token count 无法捕获语义信息密度："manager approval required"（3 tokens）添加的策略约束远多于"within 14 business days of the original purchase date"（8 tokens）。排除 incompleteness 的 confound-free 范围（+18.7 至 +36.0pp, §5.1）是更强的证据。但 incompleteness 驱动了多个二级结论（最高系统性 nocuity 率 24%, OR=2.61, §6.3；对 prompt 缓解最有抵抗力, −3.3pp n.s., Appendix B），这些类型特异性声明仍受 confound 影响。
- 建议：考虑使用语义相似度指标（如 BERTScore）替代 token count，或更明确地限定 incompleteness 特异性结论的 confounded 性质。

**W6 [Minor]: 生态效度缺口未量化。**
- 具体位置：§9 Limitations
- 论文承认合成构建并称 34.0pp 为"上界"，但未提供量化合成与自然策略歧义差距的证据。τ²-bench 和 SOPBench 均使用研究者构建的刺激。真实策略文档中歧义的频率和类型分布仍然未知。

**W7 [Minor]: 层级结构（linguistic vs specification）未通过校正。**
- 具体位置：§5.2
- C3（层效应）未通过 Holm-Bonferroni 校正（p=0.017 vs threshold 0.0125），但仍保留在分类法呈现中（Table 1）。论文正确注释为"organizational convenience"，但读者可能误解两层结构为经验发现。

**W8 [Minor]: 人工 failure-mode 验证缺失。**
- 具体位置：§6, §9
- Failure-mode 编码（§6）使用 LLM 标注 LLM 失败，仅达到中等一致性（Gwet's AC₁=0.62, κ=0.52）。论文提到"100 个违规 traces 的人工编码验证正在进行中"（§9），但目前未完成。Mutual information 证据（I=0.41 bits）提供了结构性反循环性证据，但编码级别的可靠性仍未经人工验证。

---

## 4. Questions for Authors

**Q1**: 能否将 SOPBench 效应压缩分解为三个因素？例如，在 τ²-bench 上以 constraint-level 重新分析（类比 SOPBench 指标），以隔离测量粒度效应？

**Q2**: 在模拟 κ=0.385（authorization scope）vs κ=0.65+（其他类型）测量噪声下，C4 交互测试的期望假阳性率是多少？这将澄清统计显著的交互效应是否可能仅由差异化测量可靠性产生。

**Q3**: Appendix X 的 per-type ICC 显示 authorization scope ICC≈0。在 within-cell 方差基本最大化的情况下，Figure 3 中该类型 52pp 的跨模型范围应如何解释？这是否与 authorization scope 效应主要是随机性的结论一致？

**Q4**: 是否考虑过使用语义相似度指标（如 BERTScore）替代 token count 来控制 incompleteness confound？这能更好地捕获信息内容差异。

**Q5**: 跨域类型排名不一致（ρ=0.26, Appendix U），条件优先级在零售和航空之间差异 22pp。这是否削弱了分类法作为诊断工具的实用性？实践者是否需要领域特定的校准？

**Q6**: 数据集中对话轨迹长度的分布如何？轨迹复杂性是否可能同时与歧义类型和违规率相关，从而混淆类型级别分析？

---

## 5. Missing References

未发现关键缺失引用。Related work（§2）充分覆盖了关键前人工作。建议补充 Cohen's κ 流行度悖论相关文献（Byrt et al., 1993），这与 Appendix G 中 coreferential κ=0.479 的讨论直接相关。

---

## 6. Overall Assessment

### 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | matched-pair 设计和 perturbation control 建立了严格的因果推断。统计分析全面，包含 TOST、方差分解、多重比较校正。主要不足：authorization scope 测量不可靠（κ=0.385）影响 C4；ICC 复制仅覆盖 OpenAI；SESOI 缺乏领域接地论证 |
| Excitement | 3.5/5 | 研究问题有实际意义，从相关性到因果性的方法论转变是真正的进步。条款措辞>>类型的发现可操作。但范围受限（两个客服领域、合成刺激、仅前沿模型），SOPBench 效应压缩 63% 削弱了实际影响力 |
| Reproducibility | 4/5 | ICC=0.919（OpenAI 内）表明高可复制性；代码和数据承诺发布；实验细节充分（temperature=0, top_p=1, max_tokens=4096, 日期标记）。扣分：ICC 未跨提供商验证 |
| Overall Assessment | **3.5 — Borderline Conference** | 方法论扎实的因果研究，matched-pair 设计和全面的控制实验是亮点 |

### Confidence: 4/5
我仔细阅读了论文全文（包括所有 appendix），对照 TeX 源码验证了关键统计数据，并查阅了 ARR 官方 reviewer guidelines。

### 一句话总评

方法论严谨的因果研究，matched-pair 设计与 perturbation control 建立了可信的因果推断，方差分解提供了实用洞见；但外部有效性证据不足（SOPBench 效应压缩 63%、仅两个客服领域、合成刺激），authorization scope 测量不可靠（κ=0.385）导致 C4 交互分析可信度存疑，SESOI 选择缺乏领域接地论证。建议接收前补充 SOPBench 压缩的原则性归因分析和 authorization scope 测量噪声对 C4 的影响模拟。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1947 · 2026-05-23T04:35:24.693293+00:00_

Reviewer 1 审稿报告已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 181

## Round 181

2 recorded events


### User

_source line 1948 · 2026-05-23T04:35:42.387142+00:00_

[Reviewer 1 审稿结果]:
审稿完成。核心结论：

- **Overall: 3.5（Borderline Conference）**，Soundness 4/5，Excitement 3.5/5
- **主要优势**：matched-pair 因果设计严格，perturbation control 有效，方差分解（条款措辞 22.4% >> 类型 0.4%）有实用价值，limitation 处理透明
- **5 个 Should-Fix**：SOPBench 效应压缩 63% 缺乏原则性归因；authorization scope κ=0.385 影响 C4 可信度；ICC 仅覆盖 OpenAI；SESOI ±15pp 缺乏领域接地；token count 作为 incompleteness confound 代理过于粗糙
- **3 个 Minor**：生态效度缺口未量化；层级结构未通过校正；人工 failure-mode 验证缺失

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1949 · 2026-05-23T04:35:47.498652+00:00_

收到 Reviewer 1 报告。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 182

## Round 182

6 recorded events


### User

_source line 1950 · 2026-05-23T04:37:49.927077+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：新颖性/完整性审查

**论文**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
**Venue**: EMNLP 2026 (ARR May cycle)
**审查侧重**: 新颖性与贡献定位、Related Work 覆盖、写作质量与叙事结构、格式合规、Taxonomy 设计

---

## 1. Summary

本文提出首个针对策略歧义对 LLM agent 安全影响的 matched-pair 因果研究。在 τ²-bench 上构建 300 对歧义/无歧义策略条款，跨 5 个模型、2,997 episodes 评估六类歧义的影响。核心发现：歧义条款使违规率增加 34.0 pp；条款措辞解释 22.4% 方差（vs. 类型 0.4%）；类型预测失败机制能力远强于预测违规率（NMI 29:1）；agent 几乎不主动消歧（4.6% 意识率）。研究设计严谨，附录详尽（A-X 共 24 个），具有较好的方法论贡献。

---

## 2. Strengths

**S1. 干净的因果推断设计。** Matched-pair 设计是本文的核心方法论贡献。每对条款仅在歧义维度上差异，消除了混淆变量。扰动控制实验（Δ_perturb = −0.67 pp, Section 4.5）进一步验证效应非来自表面文本变化。交叉评审设计（cross-judge）消除模型自评偏差。这一设计在 ambiguity → safety 的因果链上是真正 novel 的。

**S2. 多层次验证体系。** 本文不止于报告一个效应量，而是系统性地从多个角度验证：方差分解（Type III SS）、排列检验（p < 0.001）、ICC 复制（Appendix N）、TOST 等价性检验（Appendix A）、Bootstrap 聚类（Appendix I）、Holm-Bonferroni 校正（Appendix K）。这一验证密度在同类工作中罕见。

**S3. 方差分解产出可操作洞察。** 22.4% clause vs. 0.4% type 的发现直接指导实践：条款级审计比类型级分类更有效。这比单纯报告"歧义有害"更进一步，具有工程可落地性。

**S4. 跨模型、跨基准复制。** 5 个主模型 + 2 个复制模型（Gemini 2.5 Flash, LLaMA 4 Scout, Appendix E）+ SOPBench 跨基准复制（Appendix V, 4 个领域）。效应方向在所有 7 个模型上一致。SOPBench 复制确认方向性一致（+12.6 pp），增强了外部效度。

**S5. 失败机制分析提供诊断价值。** Section 6.1 识别的三种失败机制（structural misparse 37%, information gap-filling 35%, boundary violation 28%）及其与歧义类型的映射（NMI = 0.23, Appendix S），使 taxonomy 从分类工具升级为诊断工具。尤其是 boundary violation 与 authorization scope 的排他性关联，具有实践价值。

**S6. 诚实的贡献定位。** 论文在多处主动承认局限：disambiguation neglect 是 ambiguity collapse 的场景迁移（Section 6.2）；taxonomy 定位为 experimental instrument 而非 classification standard（Section 3）；34.0 pp 是 controlled upper bound（Section 9）。这种诚实降低了被审稿人攻击的风险。

**S7. 消歧缓解实验。** Appendix B 的 mitigation experiment 展示类型特定的消歧指令可减少违规，提供了从诊断到干预的闭环证据。

---

## 3. Weaknesses

### Should-Fix 问题（影响评分但不一票否决）

**W1** [Should-Fix] **Cross-judge 类型排序不一致未在正文充分讨论**
- 具体位置：Section 5.2 仅提及 partial ordering；cross-judge discordance (ρ = 0.09, p = 0.57) 藏在 Appendix P
- 问题：三组 judge 对六类歧义的违规率排序几乎零相关。这意味着"authorization scope 是最高风险类型"这一主文 claim（Section 5.1, 5.2）是 judge-dependent 的。论文在 Appendix W 中做了控制分析，确认极端值稳定（incompleteness 最高、conferential 最低），但中间四类排序不稳定。这一重要 caveat 应在正文 Section 5.2 或 Discussion 中明确讨论，而非仅放在 appendix
- 建议：在 Section 5.2 增加 1-2 句说明 cross-judge type ranking discordance，并将 C2（per-type ordering）明确标注为 exploratory/judge-dependent

**W2** [Should-Fix] **68.8% 残差方差的讨论不够充分**
- 具体位置：Section 6（p.6）提到残差分解（~15% 随机 + ~46% 系统性但未测量），但未深入讨论其含义
- 问题：clause identity 仅解释 22.4% 方差，意味着即使完美消除歧义，仍有大量违规变异不可控。这限制了"clause-level auditing"作为干预手段的实际天花板。论文在 Discussion（Section 7）中将 clause-level auditing 描述为"the most readily measurable intervention"，这一措辞是谨慎的，但未明确量化干预的预期上限
- 建议：在 Discussion 中增加对残差方差来源的假设（conversation trajectory complexity, task difficulty, prompt sensitivity）以及对干预天花板的讨论

**W3** [Should-Fix] **Abstract 信息密度过高**
- 具体位置：Abstract 全文
- 问题：Abstract 中包含 34.0 pp、≤18.7、>36.0、22.4%、0.4%、40% 等 6+ 个数字。对首次阅读的读者，"≤18.7 to >36.0 pp excluding the confounded incompleteness type" 这一括号内容需要大量背景知识才能理解。Abstract 的首要功能是传递核心信息，而非精确量化所有边界条件
- 建议：简化为报告 overall effect（34.0 pp）并注明 confound-free qualification，将 per-type range 移至正文。例如："increasing violation rates by 34.0 pp under controlled conditions (with confound-free effects remaining substantial across all non-confounded types)"

**W4** [Should-Fix] **Taxonomy 定位为 "instrument" 可能削弱独立贡献价值**
- 具体位置：Section 3 开头 "Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard"
- 问题：这一定位虽然诚实，但在 contribution framing 上有代价。Taxonomy 作为 classification standard 可被后续工作直接引用和扩展；作为 instrument 则可能被视为一次性工具。论文的 taxonomy 实际上有独立价值——它从 Li et al. (2024) 的 11 类中筛选出与 policy specification 最相关的 6 类，并增加了 specification layer（Section 3），这一贡献值得更积极的定位
- 为什么影响评分：Reviewer 评估 contribution 时，taxonomy 的可引用性和可扩展性是重要考量
- 建议：考虑在 Section 3 或 Discussion 中增加一段讨论 taxonomy 的独立适用性（如可用于其他 agent benchmark 的 policy 审计），同时保持 "primarily designed as instrument" 的诚实态度

### Minor 问题（不影响接收）

**W5** [Minor] **"Disambiguation neglect" 的概念新颖性有限**
- Section 6.2 坦承这是 ambiguity collapse (Gur-Arieli et al., 2020; Hu et al., 2023) 的 "context-specific manifestation"。概念本身不新，贡献在于量化测量（4.6% 意识率、41.3% 收敛违规率）。建议在 abstract/conclusion 中弱化 "disambiguation neglect" 的术语创新性，强调量化发现本身

**W6** [Minor] **Conclusion 过于简短**
- Section 8 仅约 5 句话。对于一篇含 6 个核心发现的论文，conclusion 可扩展至 2 段，涵盖：(1) 方法论启示（matched-pair 设计可推广至其他 specification quality 问题）、(2) 更广泛的 policy design implications。但这可能受页面限制

**W7** [Minor] **Incompleteness confound 处理**
- incompleteness 的 information-addition confound（Section 5.1, Appendix H）处理得当（logistic regression 控制 token delta），但论文仍在 Table 2 和 Figure 2 中展示 incompleteness 的原始效应量。建议在这些位置加注脚明确标注 confound status

**W8** [Minor] **Limitations 未提及 cross-judge discordance**
- Section 9 的 Limitations 覆盖了 synthetic benchmark、domain specificity、model coverage，但未提及 cross-judge type ranking discordance（ρ = 0.09）。这是一个对类型级结论有实质影响的限制

---

## 4. Questions for Authors

**Q1.** 68.8% 残差方差中，作者对 ~46% "systematic-but-unmeasured" 部分有何假设？是否有计划在后续工作中分解这些方差来源（如 conversation trajectory features, user query complexity, policy document structure）？

**Q2.** Cross-judge type ranking discordance（ρ = 0.09, Appendix P）如何影响 Section 5.2 中关于 authorization scope 是 "highest-risk type" 的 claim？如果使用不同的 judge 模型，这一排序是否会逆转？

**Q3.** 4.6% 的 disambiguation awareness rate 是跨模型平均值。各模型间是否存在显著差异？特别是 Claude Sonnet 4.6（RLHF 对齐较强的模型）是否比 DeepSeek-V3（开源模型）有更高的意识率？

**Q4.** Mitigation experiment（Appendix B）显示类型特定的消歧指令可减少违规。但这一干预是否实际可行——在部署场景中，如何在不知道歧义类型的情况下选择正确的消歧指令？Appendix D 的 type detection classifier（F1 = 0.81）是否足以支撑自动化管道？

**Q5.** 论文使用 τ²-bench 的 policy-injection mechanism 替换单个条款。但真实 policy documents 中，歧义往往是多条款交互的结果（如条款 A 的 authorization scope 与条款 B 的 conditional precedence 组合）。作者是否考虑过多条款歧义交互效应？

---

## 5. Missing References

**无关键遗漏。** 论文的 related work 覆盖面较全：
- Agent safety: Ruan et al. (2024), Wu & Gong (2026), Sharma (2026), Ye et al. (2026), Suri et al. (2025) ✓
- Ambiguity in NLP/LLMs: Li et al. (2024), Hu et al. (2023), Sedova et al. (2024), Liu et al. (2025) ✓
- ASPI tension (Sehwag et al., 2026): ✓ 在 Section 2 (p.3) 明确讨论了 clarification-seeking 引入 prompt injection 的 tension
- Ambig-SWE (Vijayvargiya et al., 2026b): ✓ 在 Section 2 (p.3) 引用了 interactive disambiguation 恢复 74% 性能
- RE literature: Berry et al. (2004), Dalpiaz et al. (2018), Fanmuy et al. (2012) ✓
- Psycholinguistics: Frazier & Rayner (1982), Ferreira et al. (2002), Kennedy (2007) ✓ —— 引用恰当且必要，用于支撑 disambiguation neglect 的 cognitive parallel

**可选补充**（非必须）：
- Kinniment et al. (2024) "Evaluating Language-Model Agents on Realistic Autonomous Tasks" —— 关于 agent 自主性评估的更广泛框架，可在 Discussion 中简要提及
- Gabriel et al. (2024) "The Ethics of Advanced AI Assistants" —— 关于 AI 助手的伦理框架，与 policy compliance 的伦理讨论相关

---

## 6. Taxonomy 设计评估

### 互斥性
六类分类在条款级别互斥。Section 5.2 的统计检验拒绝了均匀性假设（χ² = 28.02, V = 1.137），Appendix T 的 confusion matrix 显示检测分类器对六类的区分能力合理（macro F1 = 0.63）。Authorization scope 与 lexical 之间存在一定混淆（Appendix T Table 14），这是因为 authorization boundary 条款常含多义词，但论文在 Section 3 中解释了分类优先级（specification layer 优先于 linguistic layer）。互斥性在实验目的下可接受。

### 完备性
六类覆盖了 policy specification 中最相关的歧义类型。排除的类型：
- **Ellipsis**: 排除理由充分——属于 discourse-level gap，需要跨句推理，不适合单条款实验设计（Section 3）
- **Pragmatic implicature**: 排除理由充分——依赖共享背景知识，在 human RE 中通常不构成问题，但在缺乏 domain knowledge 的 LLM agent 中可能有不同表现。这是一个有趣的未来方向，但不是本文的必要覆盖

### Linguistic vs. Specification 两层划分
理论依据来自 Berry et al. (2004) 的 nocuous/innocuous ambiguity 区分，以及 Kennedy (2007) 关于 vagueness 与 ambiguity 的区分。论文在 Section 3 末段明确假设："linguistic ambiguity can be partially resolved through tool responses or world knowledge, while specification ambiguity has no external resolution channel, forcing the agent to guess." 这一假设在 Section 5 和 6 中得到实验支持（specification types 如 authorization scope 的 failure mechanism 与 linguistic types 如 lexical 不同）。理论依据合理。

### 与 Li et al. (2024) 11-type taxonomy 的映射
Appendix L 提供了详细映射。关键差异：
- Li et al. 的 11 类中，scopal 和 conferential 直接对应
- 本文新增 authorization scope 和 conditional precedence（Li et al. 未覆盖 specification-level 歧义）
- 映射清晰但可以更显式地讨论为什么 Li et al. 的其余 5 类被排除（目前仅在 Section 3 简要提及）

---

## 7. 格式合规检查

| 项目 | 结果 | 备注 |
|------|------|------|
| 正文 ≤ 8 页 | ✅ 合规 | Sections 1-8 (Introduction → Conclusion) 约 7.5 页；Section 9 (Limitations) 在 p.8 底部，不计入页数限制 |
| Double-blind | ✅ 合规 | p.1 标题下 "Anonymous ACL submission"；代码链接使用 anonymous placeholder URL |
| ACL template | ✅ 合规 | 使用 \usepackage[review]{acl}，review mode 正确 |
| Limitations section | ✅ 合规 | Section 9, 位于正文 p.8，非 appendix；覆盖 3 个主要限制 |
| 参考文献格式 | ✅ 基本一致 | BibTeX 条目使用 acl_natbib.bst；arXiv preprint 格式一致 |
| 图表标题自解释 | ✅ 合规 | Figure 1 (experimental overview), Figure 2 (per-type effects), Figure 3 (model×type interaction) 均有描述性标题 |
| 表格使用 booktabs | ✅ 合规 | 所有表格使用水平线（无垂直线） |
| 伦理考虑 | — | 未见 Ethics Statement section，但 Limitations 覆盖了部分内容。ARR checklist 在 OpenReview form 中填写，不在 PDF 中，符合规范 |

---

## 8. 总体评分

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 4.0 / 5 | 研究设计严谨（matched-pair + cross-judge + perturbation control），统计分析全面（方差分解、排列检验、ICC、TOST、Bootstrap），所有主 claim 都有充分支撑。扣分点：68.8% 残差未充分讨论；cross-judge type discordance 未在正文提及 |
| **Excitement** | 3.0 / 5 | 主题时效性强（agent safety 是热点），matched-pair 因果设计有方法论贡献。但：(1) 个体组件（taxonomy、disambiguation neglect）是增量贡献；(2) 领域窄（customer service）；(3) 发现的实践影响受限于高残差方差 |
| **Reproducibility** | 4.0 / 5 | 方法描述详尽（Section 4），承诺开源代码和数据，300 clause pairs + evaluation pipeline + raw traces。API 调用参数完整（temperature = 0, top_p = 1, max_tokens = 4096）。扣分：依赖闭源 API（GPT-5.4, GPT-4.1）的可复现性受 API 版本变动限制 |
| **Confidence** | 4 / 5 | 我仔细阅读了全文及附录，熟悉 agent safety、NLP ambiguity、因果推断方面的相关工作 |

### Overall Assessment

**Overall: 3.5 — Borderline Conference**

**一句话总评**: 方法论严谨、执行扎实的实证研究，matched-pair 因果设计是真正的方法论贡献，但个体组件的增量性（taxonomy 是 Li et al. 的子集重组，disambiguation neglect 是 ambiguity collapse 的重命名）和领域局限性（customer service）使其 excitement 未达到 main conference 的确定门槛，属于强 Findings 到 borderline Conference 的区间。

**关键决定因素**:
- **支持 Conference (4.0)**: 如果 reviewer panel 认为 matched-pair causal design 在 agent safety 领域的首次应用本身构成足够的方法论贡献，且 22.4% vs. 0.4% 的 clause > type finding 对实践有直接指导价值
- **支持 Findings (3.0)**: 如果 reviewer panel 认为各组件的增量性累积未达到单篇 main conference paper 的 novelty bar，或认为 customer service 领域的局限性过强
- **我的判断偏向 3.5**: 方法论贡献实在但不突破性，执行质量高于平均 submission，适合 borderline 讨论


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1951 · 2026-05-23T04:38:25.922626+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见（方法严谨性审查）。请逐条回应：对每个 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Weaknesses\n\n**W1 [Should-Fix]: SOPBench 复制显示 63% 效应压缩，缺乏原则性归因。**\nτ²-bench 主效应 34.0pp，SOPBench 仅 +12.6pp。论文提供三个事后解释（测量粒度差异、负向任务设计、结构差异），但未量化各因素贡献。建议在 τ²-bench 上以 constraint-level 重新分析。\n\n**W2 [Should-Fix]: Authorization scope 测量不可靠性渗透 C4 交互发现。**\nC4 model×type 交互完全由 authorization scope 驱动（排除后 p=0.97）。该类型同时具有最低 κ(0.385)、最高 cross-judge 方差、within-replication ICC≈0。建议模拟 κ=0.385 噪声下 C4 交互测试的期望假阳性率。\n\n**W3 [Should-Fix]: ICC 复制仅覆盖 OpenAI 家族。**\nICC=0.919 和残差分解 ICC(1)=0.749 均在 OpenAI 内计算，但用于刻画所有五个模型的残差。\n\n**W4 [Should-Fix]: SESOI ±15pp 缺乏领域接地论证。**\n两个标准（超过测量噪声 2×; 低于阈值不需要不同缓解策略）分别是精度论证和无经验支撑的判断。\n\n**W5 [Should-Fix]: Token count 是 incompleteness information-addition confound 的粗糙代理。**\ntoken count 无法捕获语义信息密度。incompleteness 驱动的二级结论（最高系统性 nocuity 率、对 prompt 缓解最有抵抗力）仍受 confound 影响。\n\n**W6 [Minor]: 生态效度缺口未量化。**\n\n**W7 [Minor]: 层级结构未通过校正。**\n\n**W8 [Minor]: 人工 failure-mode 验证缺失。**\n\n---\n\n## Reviewer 1 的 Questions\n\n**Q1**: SOPBench 效应压缩能否分解为测量粒度 vs 领域差异 vs 结构差异？\n**Q2**: 模拟 κ=0.385 测量噪声下 C4 的假阳性率？\n**Q3**: Authorization scope ICC≈0 下 Figure 3 的 52pp 跨模型范围如何解释？\n**Q4**: 是否考虑过 BERTScore 替代 token count 控制 incompleteness confound？\n**Q5**: 跨域类型排名不一致(ρ=0.26)是否削弱 taxonomy 诊断实用性？\n**Q6**: 对话轨迹长度分布是否可能混淆类型级别分析？\n\n---\n\n## Reviewer 1 的评分\n- Soundness: 4/5\n- Excitement: 3.5/5\n- Overall: 3.5 (Borderline Conference)\n\n请逐条回应后，给出你对 Reviewer 1 评分的看法。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见（方法严谨性审查）。请逐条回应：对每个 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Weaknesses\n\n**W1 [Should-Fix]: SOPBench 复制显示 63% 效应压缩，缺乏原则性归因。**\nτ²-bench 主效应 34.0pp，SOPBench 仅 +12.6pp。论文提供三个事后解释（测量粒度差异、负向任务设计、结构差异），但未量化各因素贡献。建议在 τ²-bench 上以 constraint-level 重新分析。\n\n**W2 [Should-Fix]: Authorization scope 测量不可靠性渗透 C4 交互发现。**\nC4 model×type 交互完全由 authorization scope 驱动（排除后 p=0.97）。该类型同时具有最低 κ(0.385)、最高 cross-judge 方差、within-replication ICC≈0。建议模拟 κ=0.385 噪声下 C4 交互测试的期望假阳性率。\n\n**W3 [Should-Fix]: ICC 复制仅覆盖 OpenAI 家族。**\nICC=0.919 和残差分解 ICC(1)=0.749 均在 OpenAI 内计算，但用于刻画所有五个模型的残差。\n\n**W4 [Should-Fix]: SESOI ±15pp 缺乏领域接地论证。**\n两个标准（超过测量噪声 2×; 低于阈值不需要不同缓解策略）分别是精度论证和无经验支撑的判断。\n\n**W5 [Should-Fix]: Token count 是 incompleteness information-addition confound 的粗糙代理。**\ntoken count 无法捕获语义信息密度。incompleteness 驱动的二级结论（最高系统性 nocuity 率、对 prompt 缓解最有抵抗力）仍受 confound 影响。\n\n**W6 [Minor]: 生态效度缺口未量化。**\n\n**W7 [Minor]: 层级结构未通过校正。**\n\n**W8 [Minor]: 人工 failure-mode 验证缺失。**\n\n---\n\n## Reviewer 1 的 Questions\n\n**Q1**: SOPBench 效应压缩能否分解为测量粒度 vs 领域差异 vs 结构差异？\n**Q2**: 模拟 κ=0.385 测量噪声下 C4 的假阳性率？\n**Q3**: Authorization scope ICC≈0 下 Figure 3 的 52pp 跨模型范围如何解释？\n**Q4**: 是否考虑过 BERTScore 替代 token count 控制 incompleteness confound？\n**Q5**: 跨域类型排名不一致(ρ=0.26)是否削弱 taxonomy 诊断实用性？\n**Q6**: 对话轨迹长度分布是否可能混淆类型级别分析？\n\n---\n\n## Reviewer 1 的评分\n- Soundness: 4/5\n- Excitement: 3.5/5\n- Overall: 3.5 (Borderline Conference)\n\n请逐条回应后，给出你对 Reviewer 1 评分的看法。"
  }
}
```

</details>

---


### Tool result

_source line 1952 · 2026-05-23T04:38:48.127828+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22205
}
```

</details>

---


### Tool call

_source line 1953 · 2026-05-23T04:38:48.279104+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见（新颖性/完整性审查）。请逐条回应：对每个 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Weaknesses\n\n**W1 [Should-Fix]: Cross-judge 类型排序不一致未在正文充分讨论。**\nρ = 0.09 (p=0.57) 藏在 Appendix P，但这意味着 Section 5.2 中的 per-type ordering 是 judge-dependent 的。建议在 Section 5.2 增加 1-2 句说明 cross-judge type ranking discordance。\n\n**W2 [Should-Fix]: 68.8% 残差方差的讨论不够充分。**\nclause identity 仅解释 22.4% 方差，即使完美消除歧义仍有大量违规变异不可控。建议在 Discussion 增加对干预天花板的讨论。\n\n**W3 [Should-Fix]: Abstract 信息密度过高。**\n6+ 个数字，\"≤18.7 to >36.0 pp excluding the confounded incompleteness type\" 对首次阅读需大量背景知识。\n\n**W4 [Should-Fix]: Taxonomy 定位为 \"instrument\" 可能削弱独立贡献价值。**\ntaxonomy 实际有独立价值（从 11 类筛选 + 新增 specification layer），但 \"instrument\" 定位可能被视为一次性工具，影响可引用性。\n\n**W5 [Minor]: \"Disambiguation neglect\" 概念新颖性有限。**\n承认是 ambiguity collapse 的场景迁移，贡献在于量化测量（4.6% 意识率、41.3% 收敛违规率）。\n\n**W6 [Minor]: Conclusion 过于简短。**\n约 5 句话，对于含 6 个核心发现的论文偏短。\n\n**W7 [Minor]: Incompleteness confound 处理。**\nlogistic regression 控制得当，但 Table 2/Figure 2 中展示原始效应量，建议加注脚标注 confound status。\n\n**W8 [Minor]: Limitations 未提及 cross-judge discordance。**\n\n---\n\n## Reviewer 2 的 Questions\n\n**Q1**: 68.8% 残差中 ~46% systematic-but-unmeasured 有何假设？是否有计划分解？\n**Q2**: Cross-judge type ranking discordance 如何影响 authorization scope \"highest-risk type\" 的 claim？\n**Q3**: 4.6% disambiguation awareness 各模型间是否有显著差异？\n**Q4**: Mitigation experiment 在部署中如何在不知歧义类型的情况下选择正确消歧指令？Appendix D 的 type detector (F1=0.81) 是否足够？\n**Q5**: 是否考虑过多条款歧义交互效应？\n\n---\n\n## Reviewer 2 的评分\n- Soundness: 4.0/5\n- Excitement: 3.0/5\n- Overall: 3.5 (Borderline Conference)\n- Taxonomy 评估：互斥性可接受，完备性覆盖面合理，两层划分理论依据合理\n- 格式合规：全部通过\n\n请逐条回应后，给出你对 Reviewer 2 评分的看法。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见（新颖性/完整性审查）。请逐条回应：对每个 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Weaknesses\n\n**W1 [Should-Fix]: Cross-judge 类型排序不一致未在正文充分讨论。**\nρ = 0.09 (p=0.57) 藏在 Appendix P，但这意味着 Section 5.2 中的 per-type ordering 是 judge-dependent 的。建议在 Section 5.2 增加 1-2 句说明 cross-judge type ranking discordance。\n\n**W2 [Should-Fix]: 68.8% 残差方差的讨论不够充分。**\nclause identity 仅解释 22.4% 方差，即使完美消除歧义仍有大量违规变异不可控。建议在 Discussion 增加对干预天花板的讨论。\n\n**W3 [Should-Fix]: Abstract 信息密度过高。**\n6+ 个数字，\"≤18.7 to >36.0 pp excluding the confounded incompleteness type\" 对首次阅读需大量背景知识。\n\n**W4 [Should-Fix]: Taxonomy 定位为 \"instrument\" 可能削弱独立贡献价值。**\ntaxonomy 实际有独立价值（从 11 类筛选 + 新增 specification layer），但 \"instrument\" 定位可能被视为一次性工具，影响可引用性。\n\n**W5 [Minor]: \"Disambiguation neglect\" 概念新颖性有限。**\n承认是 ambiguity collapse 的场景迁移，贡献在于量化测量（4.6% 意识率、41.3% 收敛违规率）。\n\n**W6 [Minor]: Conclusion 过于简短。**\n约 5 句话，对于含 6 个核心发现的论文偏短。\n\n**W7 [Minor]: Incompleteness confound 处理。**\nlogistic regression 控制得当，但 Table 2/Figure 2 中展示原始效应量，建议加注脚标注 confound status。\n\n**W8 [Minor]: Limitations 未提及 cross-judge discordance。**\n\n---\n\n## Reviewer 2 的 Questions\n\n**Q1**: 68.8% 残差中 ~46% systematic-but-unmeasured 有何假设？是否有计划分解？\n**Q2**: Cross-judge type ranking discordance 如何影响 authorization scope \"highest-risk type\" 的 claim？\n**Q3**: 4.6% disambiguation awareness 各模型间是否有显著差异？\n**Q4**: Mitigation experiment 在部署中如何在不知歧义类型的情况下选择正确消歧指令？Appendix D 的 type detector (F1=0.81) 是否足够？\n**Q5**: 是否考虑过多条款歧义交互效应？\n\n---\n\n## Reviewer 2 的评分\n- Soundness: 4.0/5\n- Excitement: 3.0/5\n- Overall: 3.5 (Borderline Conference)\n- Taxonomy 评估：互斥性可接受，完备性覆盖面合理，两层划分理论依据合理\n- 格式合规：全部通过\n\n请逐条回应后，给出你对 Reviewer 2 评分的看法。"
  }
}
```

</details>

---


### Tool result

_source line 1954 · 2026-05-23T04:38:49.641181+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1362
}
```

</details>

---


### Assistant

_source line 1955 · 2026-05-23T04:38:52.991478+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 183

## Round 183

2 recorded events


### User

_source line 1956 · 2026-05-23T04:38:55.543272+00:00_

[Reviewer 2 审稿结果]:
已清理完毕。审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1957 · 2026-05-23T04:38:59.542870+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 184

## Round 184

2 recorded events


### User

_source line 1958 · 2026-05-23T04:40:41.618749+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

## Weaknesses 逐条回应

**[AGREE] R1-W1: SOPBench 63% 效应压缩缺乏原则性归因**
同意这是一个实质性问题。论文在 Appendix V 中列出三个 post-hoc 解释（测量粒度、负向任务设计、结构差异），但未量化各因素贡献比例。34.0pp → 12.6pp 的压缩幅度（63%）足以让读者质疑主效应的外部效度。论文的措辞是"directional consistency"，这虽然诚实但也暗示作者知道效应量不可迁移。R1 建议在 τ²-bench 上以 constraint-level 重新分析是可行的，可以分离测量粒度这一因素。我在自己的审稿中将此归为 domain specificity（W7/Minor），现在认为 R1 将其升级为 Should-Fix 更恰当——63% 的压缩需要比现有三句话解释更系统的归因。

**[AGREE] R1-W2: Authorization scope 测量不可靠性渗透 C4 交互**
这是 R1 提出的最强技术点。三个事实的组合具有破坏性：(1) C4 交互完全由 authorization scope 驱动（排除后 p = 0.97, Appendix N）；(2) authorization scope 有最低 judge agreement（κ = 0.385, Table 9/Appendix G）；(3) within-replication ICC ≈ 0。这意味着 C4 的 model×type 交互（Section 5.2, Figure 3）很可能是测量噪声的产物。论文在 Section 5.2 将 C4 标注为"exploratory"，这一标注在 R1 的分析下显得更加必要。建议作者要么模拟 κ = 0.385 下的假阳性率（如 R1 所建议），要么在正文中明确将 C4 降级为"suggestive but unreliable due to measurement limitations in the driving category"。我的审稿中虽提到 cross-judge discordance（W1），但未将其与 C4 的可靠性直接关联——R1 的分析更精准。

**[AGREE] R1-W3: ICC 复制仅覆盖 OpenAI 家族**
同意。ICC = 0.919（Appendix N）在 OpenAI 内部计算（GPT-5.4 vs GPT-4.1），但论文用它来刻画所有五个模型的残差结构（Section 6, p.6: "68.8% residual"）。跨 provider 的 ICC 可能显著不同——特别是 Qwen3-235B（MoE 架构）和 DeepSeek-V3（开源 dense）的行为模式可能与 OpenAI 系列存在系统性差异。这一局限削弱了残差分解的通用性声明。不过，论文确实在 Appendix E 中展示了 Gemini 和 LLaMA 的复制结果方向一致，部分缓解了这一问题。建议作者至少计算一个跨 provider 的 ICC 下界。

**[AGREE] R1-W4: SESOI ±15pp 缺乏领域接地**
同意，但补充一个 nuance：在 agent safety 这一新兴领域，domain-grounded SESOI 几乎不可能从现有文献中获得，因为没有先例研究建立了"多大的违规率差异在实践中重要"的经验标准。论文的两个理由（2× 测量噪声、缓解策略阈值）虽非理想的领域锚点，但在 pilot study 阶段是可接受的权宜之计。建议作者 (1) 明确承认 SESOI 是统计驱动而非领域驱动的，(2) 在 Discussion 中讨论什么样的领域信息（如 deployment incident rate data）能在未来提供更好的锚点。

**[AGREE with nuance] R1-W5: Token count 作为 incompleteness confound 的粗糙代理**
部分同意。Token count 确实无法捕获语义信息密度——一个 20-token 的条款可能比一个 30-token 的条款包含更多操作约束。R1 提出的 BERTScore 替代方案（Q4）有道理但也有局限：BERTScore 测量的是语义相似度而非信息增量。更直接的方法可能是计算每个条款变体中的独立操作约束数量（如 "condition count"）。

但我认为论文在此问题上的整体策略是保守的：(1) 明确标注 incompleteness 为 confounded（Section 5.1）；(2) 在报告 confound-free range 时排除 incompleteness（abstract, Section 5.1）；(3) 即使用粗糙的 token count 控制，残差效应仍显著（Appendix H: OR = 1.022, p = 0.018）。问题在于基于 incompleteness 的二级结论（最高系统性 nocuity 率 Section 6.3, OR = 2.61；对 prompt 缓解最有抵抗力 Appendix B）是否受 confound 污染。这里我同意 R1：这些二级结论需要更强的 caveat。

**[AGREE] R1-W6: 生态效度缺口未量化**
同意。这与我的 W8（template-based pair generation）对应。论文承认"34.0 pp effect is an upper bound"（Section 9），但未量化上界与真实世界效应之间的预期差距。SOPBench 的 +12.6pp 可以作为一个粗略的下界参考点，但这一连接未在论文中明确建立。

**[AGREE] R1-W7: 层级结构未通过校正**
同意。Section 5.2 的 partial ordering（incompleteness > {auth scope, cond prec, scopal, lexical} > conferential）如果中间四类的两两比较未通过 Holm-Bonferroni 校正（Appendix K），则 "partial ordering" 的表述可能过于自信。论文应在 Section 5.2 中明确说明哪些两两比较通过了校正。

**[AGREE] R1-W8: 人工 failure-mode 验证缺失**
同意。论文在 p.9 提及"A human failure-mode coding validation of 100 violation traces is underway"，说明作者意识到这一缺口。在当前版本中，三种 failure mechanism（structural misparse, information gap-filling, boundary violation）的分类完全基于 LLM 标注，缺乏人工验证。考虑到 failure mechanism 分析是论文的重要贡献之一（支撑 taxonomy 的诊断价值，Section 6.1, Appendix S），人工验证的缺失确实是一个需要在 camera-ready 前解决的问题。

---

## Questions 逐条回应

**Q1: SOPBench 效应压缩的分解**
[AGREE] 合理的要求。当前的三因素解释（测量粒度、负向任务、结构差异）是定性的。在 τ²-bench 上以 constraint-level 重新分析（如 R1 建议）可以至少分离出测量粒度因素的贡献。

**Q2: 模拟 κ=0.385 下 C4 假阳性率**
[AGREE] 这是一个可以直接执行的分析。如果 κ=0.385 噪声下的交互检验假阳性率 >10%，则 C4 应在正文中降级或附加强 caveat。这与我的 W1（cross-judge discordance）直接相关。

**Q3: Authorization scope ICC≈0 下 Figure 3 的 52pp 跨模型范围**
[AGREE] 这是 R1-W2 的直接推论。如果 ICC ≈ 0，则同一 clause 在同一模型的不同 run 中的方差已经非常大，52pp 的跨模型范围很可能包含大量测量噪声。Figure 3 中 authorization scope 的跨模型 pattern 可能不可靠。但我补充一点：Figure 3 的其他五种类型的跨模型 pattern 应该更可靠（κ 更高），论文可以考虑在 Figure 3 中为 authorization scope 添加置信区间或标注其低可靠性。

**Q4: BERTScore 替代 token count**
[AGREE with reservation] 方向正确但 BERTScore 也不是理想工具——它测量 surface-level 语义相似度，不直接测量 information gain。更好的替代可能是：(1) 独立标注每个 clause variant 的操作约束数量，(2) 使用 information-theoretic measures（如 PMI-based features）。不过，考虑到论文已经将 incompleteness 标注为 confounded 并在主分析中排除，这一改进的紧迫性有限。

**Q5: 跨域类型排名不一致 (ρ=0.26)**
[AGREE] 这与我的 W1（cross-judge ρ = 0.09）指向同一问题：类型级排名在 judge 和 domain 之间都不稳定。ρ = 0.26（跨域）和 ρ = 0.09（跨 judge）共同表明 taxonomy 的诊断价值主要体现在 type → failure mechanism 映射（NMI = 0.23, Appendix S），而非 type → violation rate 预测。论文的 Discussion（Section 7.2）已经朝这个方向论述，但应更明确地在正文中承认 type → violation rate 排名的不稳定性。

**Q6: 对话轨迹长度作为混淆变量**
[AGREE] 合理的担忧。不同歧义类型可能系统性地产生不同长度的对话（如 incompleteness 可能导致更多轮次的探索），对话长度本身可能独立于歧义类型影响违规率（更多轮次 = 更多出错机会）。Appendix O（Per-Type Clause Length Analysis）控制了 clause 长度但不是 conversation trajectory 长度。这是一个未控制的潜在混淆变量。

---

## 对 Reviewer 1 评分的看法

| 维度 | R1 评分 | R2（我的）评分 | 差异分析 |
|------|---------|--------------|----------|
| Soundness | 4.0 | 4.0 | **一致。** 方法论严谨，主要 claims 有充分支撑。R1 和我的扣分点不同（R1 侧重 ICC/SESOI/confound proxy；我侧重 cross-judge discordance/residual variance），但结论相同：soundness strong but not excellent |
| Excitement | 3.5 | 3.0 | **R1 稍高。** 我认为 R1 可能对 matched-pair 因果设计在 agent safety 领域的方法论贡献给予了更多权重。我的 3.0 更多受到各组件增量性（taxonomy 重组、disambiguation neglect 重命名）的影响。这一分歧是主观偏好差异，我维持 3.0 但认为 3.5 也可接受 |
| Overall | 3.5 | 3.5 | **一致。** Borderline Conference。两位 reviewer 独立得出相同结论，增强了评分可信度 |

**总结**: R1 的审稿质量很高，尤其是 W2（authorization scope 不可靠性 → C4 交互可靠性）的分析比我的 cross-judge discordance 分析更精准地定位了问题。我在 8 个 weakness 中同意了全部 8 个（其中 W5 为部分同意），这反映了 R1 审查的准确性。两位 reviewer 的主要分歧在于 Excitement（3.0 vs 3.5），这属于正常的 reviewer 间主观差异。

**我对论文最终走向的判断**: 3.5 应为共识评分。论文 soundness 足以被 Findings 接收，是否进入 main conference 取决于 AC 对方法论贡献（matched-pair causal design 的首次应用）的估值。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1959 · 2026-05-23T04:40:46.305795+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 185

## Round 185

2 recorded events


### User

_source line 1960 · 2026-05-23T04:40:50.381610+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心结论：**8 条 Weakness 全部 AGREE**（W5 部分同意），与 R1 在 Soundness 4.0 和 Overall 3.5 上一致。唯一分歧在 Excitement（我 3.0 vs R1 3.5），源于我对各组件增量性的更严格判断。

R1 最强的技术贡献是 W2：将 authorization scope 的低 κ（0.385）、低 ICC（≈0）与 C4 交互发现的完全依赖性（排除后 p=0.97）串联起来，精确定位了 C4 为潜在测量伪影——这比我对 cross-judge discordance 的笼统指摘更具杀伤力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1961 · 2026-05-23T04:40:57.415723+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 186

## Round 186

10 recorded events


### User

_source line 1962 · 2026-05-23T04:40:58.920866+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Weaknesses 回应

**[REBUT] R2-W1: Cross-judge 类型排序不一致已在正文 §5.2 明确报告。**
Reviewer 2 称 ρ=0.09 "藏在 Appendix P"，但实际上 §5.2 主文第四段明确写道："An important qualification: cross-judge-group type rankings are discordant (ρ = 0.09, p = 0.87; Appendix P), driven by authorization scope. Excluding it, ρ = 0.90 (p = 0.037)"。这不是附录中的隐藏信息，而是正文中带有"important qualification"标签的显著声明。后续还有三行关于三家族验证（ρ = 0.71–0.89）的讨论。建议保留现状——该信息已获得与其重要性匹配的正文篇幅。

**[AGREE] R2-W2: 残差方差的干预天花板讨论值得加强。**
同意这是一个可改进的方向。但需修正 Reviewer 2 引用的数字：残差是 60.8%（§5.1），不是 68.8%。Discussion §7 确实已提及"clause-level auditing addresses the largest actionable component (22.4%) but not the majority of outcome variance"，并列出了候选来源（conversation trajectory complexity, task difficulty gradients, latent policy structure）。但我同意这个讨论可以更明确地框架化为"干预天花板"——即使完美消除所有歧义，仍有 60.8% 的违规变异来自其他因素。建议在 Discussion 增加 2-3 句，明确量化这一干预上限的实际含义。

**[REBUT] R2-W3: Abstract 信息密度对因果研究论文是合理的。**
对于一篇以因果推断为核心方法论贡献的论文，Abstract 中报告效应量及其置信区间是学术惯例。"±18.7 to >36.0 pp excluding the confounded incompleteness type" 这一表述确实需要背景知识，但它传达了一个关键方法论决策：主效应不依赖于有 confound 的类型。如果去掉这些数字，Abstract 将退化为定性声明，削弱论文作为定量因果研究的定位。ARR 审稿人通常期望 Abstract 包含主要效应量。认为当前密度在可接受范围内。

**[REBUT] R2-W4: Taxonomy 定位为 "instrument" 是诚实且策略性的正确选择。**
论文明确声明 taxonomy "serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard"（§3, page 3）。这一定位恰当，因为：（1）六类分类法是从已有 11 类中筛选+重组的（§3），不是从头构建的完整分类体系；（2）C3（层效应）未通过 Holm-Bonferroni 校正（§5.2, p=0.017 vs threshold 0.0125），两层结构不具备经验支撑；（3）跨域类型排名不一致（ρ=0.26, Appendix U）。在这些限制下，声称 taxonomy 有"独立贡献价值"反而会招致更严厉的批评。"Instrument" 定位是在已知限制下的合理 framing，不影响实际可引用性——后人引用的是方差分解结果和失败机制映射，不是分类法本身。

**[AGREE] R2-W5: "Disambiguation neglect" 确实是概念迁移而非原创概念。**
同意。论文自己承认这一点（§6.2: "the agentic-context manifestation of what Liu et al. (2023) call ambiguity collapse"）。贡献在于定量测量（4.6% 意识率、41.3% 收敛违规率）和 agentic context 的新发现（不可逆策略违规 vs 一般不准确回应）。新颖性有限，但量化本身有价值。

**[AGREE] R2-W6: Conclusion 可适当扩展。**
同意 Conclusion（§8）偏短（约 5 句），但这在 8 页正文限制下是合理的权衡。如果要扩展，建议增加 1-2 句关于（1）干预天花板的含义和（2）从 C1→C2→failure mechanism 的分析逻辑链总结。但不建议大幅扩展以免挤占正文其他内容的空间。

**[AGREE] R2-W7: Table 2/Figure 2 应标注 incompleteness confound。**
同意。Table 2 展示 incompleteness 原始效应量 +49.2pp，但最近的 confound 讨论在 §5.1 末段和 Appendix F，相隔较远。在 Table 2 的 incompleteness 行或 caption 中加一个脚注（如"†Conditional on information-addition confound; see Appendix F"）会显著提高表格的自包含可读性。这是一个简单且有效的改进。

**[REBUT] R2-W8: Limitations 已涵盖 cross-judge 测量限制。**
Limitations §9 "Measurement" 段落明确讨论了：（1）Fleiss' κ=0.717 三家族验证；（2）模型排名跨三个 judge 家族保持一致（ρ≥0.70）；（3）authorization scope 的 within-judge 范围是 judge-dependent 的（52pp vs 24-30pp）；（4）per-type reliability 差异（κ=0.385 最低）。虽然没有直接引用 ρ=0.09 这个数字，但 Limitations 覆盖了导致该不一致的根本原因（authorization scope 的 judge-dependent 测量）。如果 Reviewer 2 要求在 Limitations 中再加一句引用 ρ=0.09，这可以做但并非遗漏——根本机制已经讨论。

---

### Questions 回应

**R2-Q1 (残差分解假设)**:
Discussion §7 已列出三个候选来源：conversation trajectory complexity, task difficulty gradients, latent policy structure。Appendix X 进一步分解：ICC(1)=0.749 表明 74.9% between-cell（系统性）、25.1% within-cell（随机性）。86.5% 的 cells 产生一致结果（173/200）。论文正确识别 conversation trajectory 为"most readily measurable next target"。这个分解超出了当前论文范围，但候选假设已明确且合理。

**R2-Q2 (Cross-judge discordance 对 authorization scope 风险评估的影响)**:
需要澄清：论文**没有**声称 authorization scope 是 "highest-risk type"。Table 2 清楚显示 incompleteness（53.6%）是违规率最高的类型，authorization scope（41.6%）位于 mid-tier cluster。C4 分析（§5.3）报告 authorization scope 有最大的**跨模型范围**（52pp），这是关于变异性而非风险水平的声明。Cross-judge discordance 影响的是 C4 交互分析的可信度，而非 C2 类型排序——后者的两个极端（incompleteness 上界、coreferential 下界）跨三个 judge 家族一致。我在自己的审稿中已将此标记为 W2（Should-Fix）。

**R2-Q3 (4.6% 意识率的模型间差异)**:
§6.2 提供了部分信息："Overall awareness is 4.6% (≤11% per model); Qwen3 and DeepSeek show zero across all 278 combined traces." 这意味着 GPT 和 Claude 系列有非零但仍极低的意识率（≤11%）。样本量限制（每模型约 120 个违规 trace）使得模型间差异的统计检验不太可靠。但方向性发现清晰：所有模型的意识率都极低，"disambiguation neglect" 是跨模型的普遍现象。

**R2-Q4 (实际部署中的 type-specific mitigation)**:
这是一个实际且重要的问题。论文报告了：（1）type-specific prompt（Appendix B, Table 4）——authorization scope −18.0pp, lexical −8.9pp, incompleteness −3.3pp n.s.；（2）generic awareness prompt 模板（Appendix B prompt text 段落）。但论文**未直接比较** generic vs type-specific prompt 的效果量，这是一个遗漏。Appendix D 的 type detector（binary F1=0.81, type-level macro F1=0.63）提供了初步自动化路径，但 F1=0.63 确实不足以可靠地选择 type-specific 指令。建议论文补充 generic prompt 的效果量报告，这对部署指导更直接有用。

**R2-Q5 (多条款歧义交互)**:
论文研究单条款操纵，这是建立因果关系的正确起点。多条款交互效应（例如：同一策略中同时存在 authorization scope 和 incompleteness 歧义）在实际部署中很可能存在，但实验设计上的组合爆炸（6 类型×C(n,k) 组合）使其超出当前研究范围。论文可在 Future Work 中简要提及。

---

### 对 Reviewer 2 评分的看法

| 维度 | R2 评分 | R1 评分 | R1 意见 |
|------|--------|--------|--------|
| Soundness | 4.0/5 | 4.0/5 | 完全同意 |
| Excitement | 3.0/5 | 3.5/5 | 认为 R2 偏低。从相关性到因果推断的方法论转变（matched-pair + perturbation control）是该领域的真正进步；方差分解（clause 22.4% >> type 0.4%）是新颖且可操作的发现；failure mechanism 映射（NMI=0.23 vs 0.01）提供了超越风险量化的诊断视角。Excitement 3.0 更适合增量性改进的论文，而本文在方法论层面有显著推进 |
| Overall | 3.5 | 3.5 | 一致。Borderline Conference 合理——方法论贡献够格，但外部有效性不足（SOPBench 63% 压缩、仅两个领域）阻止了明确接收 |

**总结**: Reviewer 2 的审查全面，大部分关切合理。主要分歧在于：（1）W1/W8 关于 cross-judge discordance 的信息实际已在正文和 Limitations 中覆盖；（2）W3/W4 的风格建议见仁见智；（3）Excitement 评分 3.0 偏低，未充分认可方法论层面的推进。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1963 · 2026-05-23T04:41:41.402114+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1964 · 2026-05-23T04:41:41.452879+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1965 · 2026-05-23T04:41:41.453263+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1966 · 2026-05-23T04:41:41.554010+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T04:25:35.492062+00:00\", \"completed_at\": \"2026-05-23T04:28:38.886808+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 4-6\", \"message\": \"连续三页纯文本（Method §4 至 Results §5.2），无任何 figure/table/equation 穿插。Method 中的匹配对设计和统计分析描述可考虑用流程图或示意图辅助，Results 早期的 C1 主效应数据可提前放置 Table 2 或一个汇总图来打破文字墙\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Table 2 + Figure 2 + Figure 3 三个 display items 集中在同一页，与前三页纯文本形成强烈反差。建议将 Table 2 或 Figure 3 前移至 page 5-6（Results §5.1 首次报告数据的位置），均衡视觉节奏\"}, {\"severity\": \"warning\", \"dimension\": \"pages 8-9\", \"message\": \"Error Analysis (§6)、Discussion (§7)、Conclusion (§8)、Limitations 连续两页无 display item。§6 的失败模式分析（structural misparse、information gap-filling、boundary violation）适合用一个示例表或 confusion matrix 可视化来增强可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（仅 title + abstract + introduction 开头），第一个 display item（Figure 1）出现在 page 2 顶部——位置可接受，但审稿人翻开第一页时完全是文字\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 全宽实验概览图：整体清晰，三个面板（Taxonomy → Evaluation → Cross-Judge）传达核心实验流程。但图内文字偏小（模型名称列表 GPT-5.4 / GPT-4.1 / Claude Sonnet 等），建议适当增大字号或简化布局\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2（per-type effect sizes 水平条形图）和 Figure 3（model × type violation rates 分组条形图）压缩在半栏宽度内，轴标签和图例字号接近可读下限。建议：若空间允许，Figure 3 可用 figure*（全宽）展示以提高可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Table 1（六类歧义分类表）使用 booktabs 风格，格式规范。\\\"Disambig. Channel\\\" 列文字较密，但整体可读\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 最优值已加粗标注，格式规范。Overall 行清晰突出\"}, {\"severity\": \"info\", \"dimension\": \"pages 12-19\", \"message\": \"附录包含 Tables 3-17（15 个表），密度极高但格式统一，booktabs 风格一致。附录无 figure，全部以表格 + 文字呈现\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"主文本末页（Limitations + References 开始）
…[truncated 550 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1967 · 2026-05-23T04:43:28.680641+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 22\n\n# ============================================================\n# R22 ISSUES — OPEN\n# ============================================================\n\n- id: \"R22-W1\"\n  summary: \"C4 model×type 交互完全由 authorization scope 驱动，该类型测量不可靠（κ=0.385, ICC≈0），C4 可能是测量伪影\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1 提出（W2），R2 完全同意。四个独立指标同时指向测量不稳定：lowest κ, highest cross-judge variance, ICC≈0, C4 排除后 p=0.97。R2 称这是 R1 最强技术点。\"\n  action_items:\n    - round: 22\n      action: \"选项A：模拟 κ=0.385 噪声下 C4 交互检验假阳性率；选项B：在正文明确将 C4 降级为 suggestive but unreliable due to measurement limitations\"\n      assigned_to: \"pending\"\n      status: \"open\"\n\n- id: \"R22-W2\"\n  summary: \"SOPBench 复制效应压缩 63%（34.0pp→12.6pp），缺乏原则性归因\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1 提出（W1），R2 完全同意并升级认同度。三个 post-hoc 解释未量化各因素贡献。R1 建议在 τ²-bench 上以 constraint-level 重新分析。\"\n  action_items:\n    - round: 22\n      action: \"在 Appendix V 中补充原则性归因分析，或在正文明确建立 directional consistency 为何足以支撑安全论述\"\n      assigned_to: \"pending\"\n      status: \"open\"\n\n- id: \"R22-W3\"\n  summary: \"ICC 复制仅覆盖 OpenAI 家族，但残差方差分解应用于所有模型\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1 提出（W3），R2 同意。跨 provider ICC 可能不同（MoE vs dense, 不同 temperature=0 实现）。\"\n  action_items:\n    - round: 22\n      action: \"在至少一个非 OpenAI 模型上进行小规模 ICC 复制，或明确标注残差分解的适用范围\"\n      assigned_to: \"pending\"\n      status: \"open\"\n\n- id: \"R22-W4\"\n  summary: \"SESOI ±15pp 缺乏领域接地论证，为统计驱动而非领域驱动\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1 提出（W4），R2 同意但补充 nuance：agent safety 新兴领域无先例标准，pilot study 阶段可接受。\"\n  action_items:\n    - round: 22\n      action: \"明确承认 SESOI 是统计驱动的；在 Discussion 讨论什么领域信息能提供更好锚点\"\n      assigned_to: \"pending\"\n      status: \"open\"\n\n- id: \"R22-W5\"\n  summary: \"Token count 作为 incompleteness information-addition confound 代理过于粗糙，基于 incompleteness 的二级结论仍受 confound 影响\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1 提出（W5），R2 部分同意。Token count 无法捕获语义信息密度。但论文整体策略保守（已排除 incompleteness 报告 confound-free range）。问题在二级结论（最高系统性 nocuity 率 OR=2.61; 对 prompt 缓解最有抵抗力 −3.3pp n.s.）。\"\n  action_items:\n    - round: 22\n      action: \"对基于 incompleteness 的二级结论添加更强 caveat，或考虑语义复杂度指标替代 token count\"\n      assigned_to: \"pending\"\n      status: \"open\"\n\n- id: \"R22-W6\"\n  summary: \"残差方差（60.8%）的干预天花板讨论不够充分\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R2 提出（W2），R1 同意。Discussion §7 已提及但未明确框架化为干预天花板。R1 修正数字：残差是 60.8% 非 68.8%。\"\n  action_items:\n    - round: 22\n      action: \"Discussion 增加 2-3 句，明确量化干预上限的实际含义\"\n      assigned_to: \"pending\"\n      status: \"open\"\n\n- id: \"R22-M1\"\n  summary: \"生态效度缺口未量化——合成刺激与真实策略文档歧义的差距未知\"\n  category: framing\n  severity: minor\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1（W6），R2 同意。34.0pp 为上界但未量化与真实世界效应的预期差距。\"\n\n- id: \"R22-M2\"\n  summary: \"层级结构（linguistic vs specification）C3 未通过 Holm-Bonferroni 校正，但保留在分类法呈现中\"\n  category: framing\n  severity: minor\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1（W7），R2 同意。p=0.017 vs threshold 0.0125，已标注为 organizational convenience，但读者可能误解。\"\n\n- id: \"R22-M3\"\n  summary: \"人工 failure-mode 编码验证缺失（camera-ready 前需完成）\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1（W8），R2 同意。100 traces 人工验证在进行中但未完成。LLM 编码 LLM 失败的循环性风险。\"\n\n- id: \"R22-M4\"\n  summary: \"Table 2/Figure 2 中 incompleteness 应标注 confound status\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R2（W7），R1 同意。Table 2 展示原始 +49.2pp 但 confound 讨论在 §5.1 末段和 Appendix F，相隔较远。加脚注即可。\"\n\n- id: \"R22-M5\"\n  summary: \"Conclusion 偏短（约 5 句），可适当扩展\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R2（W6），R1 同意但认为 8 页限制下合理。建议增加干预天花板含义和分析逻辑链总结。\"\n\n# ============================================================\n# R21 ISSUES — ALL RESOLVED (from prior rounds)\n# ============================================================\n\n- id: \"R21-N1\"\n  summary: \"SESOI ±15pp 缺乏外部锚定，C2 mid-tier 在 ±10pp 下瓦解\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"§4.6 加 Lakens (2017) 两项原则性锚定; Intro partial ordering 加 ±15pp margin 限定; 无 clinical/financial 类比. Reviewer PASS.\"\n  resolution_round: 21\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R21-N2\"\n  summary: \"46% 系统性残差候选因素讨论深度不足\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Discussion 加候选因素 (conversation trajectory, task difficulty, policy structure); pp→% 单位统一.\"\n  resolution_round: 21\n  first_raised_round: 18\n  last_seen_round: 21\n\n- id: \"R21-N3\"\n  summary: \"Cross-judge type ranking ρ=0.09 严重削弱 C2 partial ordering\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"§5.2 加 judge-model pairing 解释 + pooled ρ≥0.71; Intro partial ordering 加 ±15pp 限定.\"\n  resolution_round: 21\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R21-N4\"\n  summary: \"Taxonomy 类型选择缺定量依据 + C3 inconclusive 未在 Intro 反映\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"§3 加三项 design criteria (attestation + minimal-pair + mutual exclusivity).\"\n  resolution_round: 21\n  first_raised_round: 18\n  last_seen_round: 21\n\n- id: \"R21-W1\"\n  summary: \"Error analysis LLM 编码循环性需人工验证\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Limitations Measurement 段加 camera-ready human validation 声明.\"\n  resolution_round: 21\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R21-W2\"\n  summary: \"DN 是 ambiguity collapse 场景迁移非概念创新\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"§6.2 主题句改为 agentic-context manifestation of ambiguity collapse.\"\n  resolution_round: 21\n  first_raised_round: 18\n  last_seen_round: 21\n\n- id: \"R21-W3\"\n  summary: \"Abstract 应突出 confound-free range\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"34.0pp headline 在前, confound-free range 紧随其后.\"\n  resolution_round: 21\n  first_raised_round: 19\n  last_seen_round: 21\n\n- id: \"R21-W4\"\n  summary: \"Human validation per-type 样本量不足\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"§4.4 加 pooled-only 限定 + per-type wide CI 警告.\"\n  resolution_round: 21\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R21-W5\"\n  summary: \"Temperature=0 跨 provider 确定性假设未讨论\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Limitations Scope 段加 cross-provider stochasticity + ICC 覆盖范围限定.\"\n  resolution_round: 21\n  first_raised_round: 21\n  last_seen_round: 21\n\n- id: \"R21-W6\"\n  summary: \"BibTeX key mou_ambigswe_2026 与 author 不匹配\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"全文替换 mou_ambigswe_2026 → vijayvargiya_ambigswe_2026.\"\n  resolution_round: 21\n  first_raised_round: 21\n  last_seen_round: 21\n\n- id: \"R21-M1\"\n  summary: \"Abstract 信息密度偏高 (5 个数字)\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"删除 NMI 具体值, 保留 order-of-magnitude; ≤4 核心数值.\"\n  resolution_round: 21\n\n- id: \"R21-M2\"\n  summary: \"Systematic nocuity 与 Berry & Kamsties 方向偏差\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"§6.3 加 divergent→convergent 方向反转说明.\"\n  resolution_round: 21\n\n- id: \"R21-M3\"\n  summary: \"NMI=0.23 绝对值 modest, 补 Cramér's V\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Discussion taxonomy 段补 Cramér's V=0.45.\"\n  resolution_round: 21\n\n- id: \"R20-N1\"\n  summary: \"17× definitional circularity\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"17× → order-of-magnitude; §6.1 区分 definitional vs empirical\"\n  resolution_round: 20\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R20-N2\"\n  summary: \"Missing Ambig-SWE\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Added citation in §2, §6.2, §9\"\n  resolution_round: 20\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R20-W9\"\n  summary: \"Bib fixes (duplicate + Anonymous + type)\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"All fixed\"\n  resolution_round: 20\n  first_raised_round: 20\n  last_seen_round: 20\n\n- id: \"R20-W11\"\n  summary: \"Abstract density\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Reduced from 7+ to ≤4 numbers across R20-R21\"\n  resolution_round: 21\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R19-N1\"\n  summary: \"Ecological validity\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Synthetic conditions qualifier + Limitations paragraph\"\n  resolution_round: 19\n  first_raised_round: 19\n\n- id: \"R19-N2\"\n  summary: \"Behaviorally indistinguishable contradiction\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Reworded to comparable safety impact\"\n  resolution_round: 19\n  first_raised_round: 19\n\n- id: \"R19-N3\"\n  summary: \"Auth scope κ=0.385 claims\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Downgraded with caution caveats\"\n  resolution_round: 19\n  first_raised_round: 19\n\n- id: \"R18-N1\"\n  summary: \"C2 mid-tier ordering\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"C2 降为 secondary, robust extremes only\"\n  resolution_round: 18\n  first_raised_round: 18\n\n- id: \"R18-N2\"\n  summary: \"Judge-model confound\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Cross-family validation κ=0.717\"\n  resolution_round: 19\n  first_raised_round: 18\n\n- id: \"R17-N1\"\n  summary: \"30× MI ratio\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"30× → 17× → order-of-magnitude\"\n  resolution_round: 20\n  first_raised_round: 17"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 22\n\n# ============================================================\n# R22 ISSUES — OPEN\n# ============================================================\n\n- id: \"R22-W1\"\n  summary: \"C4 model×type 交互完全由 authorization scope 驱动，该类型测量不可靠（κ=0.385, ICC≈0），C4 可能是测量伪影\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1 提出（W2），R2 完全同意。四个独立指标同时指向测量不稳定：lowest κ, highest cross-judge variance, ICC≈0, C4 排除后 p=0.97。R2 称这是 R1 最强技术点。\"\n  action_items:\n    - round: 22\n      action: \"选项A：模拟 κ=0.385 噪声下 C4 交互检验假阳性率；选项B：在正文明确将 C4 降级为 suggestive but unreliable due to measurement limitations\"\n      assigned_to: \"pending\"\n      status: \"open\"\n\n- id: \"R22-W2\"\n  summary: \"SOPBench 复制效应压缩 63%（34.0pp→12.6pp），缺乏原则性归因\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1 提出（W1），R2 完全同意并升级认同度。三个 post-hoc 解释未量化各因素贡献。R1 建议在 τ²-bench 上以 constraint-level 重新分析。\"\n  action_items:\n    - round: 22\n      action: \"在 Appendix V 中补充原则性归因分析，或在正文明确建立 directional consistency 为何足以支撑安全论述\"\n      assigned_to: \"pending\"\n      status: \"open\"\n\n- id: \"R22-W3\"\n  summary: \"ICC 复制仅覆盖 OpenAI 家族，但残差方差分解应用于所有模型\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1 提出（W3），R2 同意。跨 provider ICC 可能不同（MoE vs dense, 不同 temperature=0 实现）。\"\n  action_items:\n    - round: 22\n      action: \"在至少一个非 OpenAI 模型上进行小规模 ICC 复制，或明确标注残差分解的适用范围\"\n      assigned_to: \"pending\"\n      status: \"open\"\n\n- id: \"R22-W4\"\n  summary: \"SESOI ±15pp 缺乏领域接地论证，为统计驱动而非领域驱动\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1 提出（W4），R2 同意但补充 nuance：agent safety 新兴领域无先例标准，pilot study 阶段可接受。\"\n  action_items:\n    - round: 22\n      action: \"明确承认 SESOI 是统计驱动的；在 Discussion 讨论什么领域信息能提供更好锚点\"\n      assigned_to: \"pending\"\n      status: \"open\"\n\n- id: \"R22-W5\"\n  summary: \"Token count 作为 incompleteness information-addition confound 代理过于粗糙，基于 incompleteness 的二级结论仍受 confound 影响\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1 提出（W5），R2 部分同意。Token count 无法捕获语义信息密度。但论文整体策略保守（已排除 incompleteness 报告 confound-free range）。问题在二级结论（最高系统性 nocuity 率 OR=2.61; 对 prompt 缓解最有抵抗力 −3.3pp n.s.）。\"\n  action_items:\n    - round: 22\n      action: \"对基于 incompleteness 的二级结论添加更强 caveat，或考虑语义复杂度指标替代 token count\"\n      assigned_to: \"pending\"\n      status: \"open\"\n\n- id: \"R22-W6\"\n  summary: \"残差方差（60.8%）的干预天花板讨论不够充分\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R2 提出（W2），R1 同意。Discussion §7 已提及但未明确框架化为干预天花板。R1 修正数字：残差是 60.8% 非 68.8%。\"\n  action_items:\n    - round: 22\n      action: \"Discussion 增加 2-3 句，明确量化干预上限的实际含义\"\n      assigned_to: \"pending\"\n      status: \"open\"\n\n- id: \"R22-M1\"\n  summary: \"生态效度缺口未量化——合成刺激与真实策略文档歧义的差距未知\"\n  category: framing\n  severity: minor\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1（W6），R2 同意。34.0pp 为上界但未量化与真实世界效应的预期差距。\"\n\n- id: \"R22-M2\"\n  summary: \"层级结构（linguistic vs specification）C3 未通过 Holm-Bonferroni 校正，但保留在分类法呈现中\"\n  category: framing\n  severity: minor\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1（W7），R2 同意。p=0.017 vs threshold 0.0125，已标注为 organizational convenience，但读者可能误解。\"\n\n- id: \"R22-M3\"\n  summary: \"人工 failure-mode 编码验证缺失（camera-ready 前需完成）\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1（W8），R2 同意。100 traces 人工验证在进行中但未完成。LLM 编码 LLM 失败的循环性风险。\"\n\n- id: \"R22-M4\"\n  summary: \"Table 2/Figure 2 中 incompleteness 应标注 confound status\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R2（W7），R1 同意。Table 2 展示原始 +49.2pp 但 confound 讨论在 §5.1 末段和 Appendix F，相隔较远。加脚注即可。\"\n\n- id: \"R22-M5\"\n  summary: \"Conclusion 偏短（约 5 句），可适当扩展\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R2（W6），R1 同意但认为 8 页限制下合理。建议增加干预天花板含义和分析逻辑链总结。\"\n\n# ============================================================\n# R21 ISSUES — ALL RESOLVED (from prior rounds)\n# ============================================================\n\n- id: \"R21-N1\"\n  summary: \"SESOI ±15pp 缺乏外部锚定，C2 mid-tier 在 ±10pp 下瓦解\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"§4.6 加 Lakens (2017) 两项原则性锚定; Intro partial ordering 加 ±15pp margin 限定; 无 clinical/financial 类比. Reviewer PASS.\"\n  resolution_round: 21\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R21-N2\"\n  summary: \"46% 系统性残差候选因素讨论深度不足\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Discussion 加候选因素 (conversation trajectory, task difficulty, policy structure); pp→% 单位统一.\"\n  resolution_round: 21\n  first_raised_round: 18\n  last_seen_round: 21\n\n- id: \"R21-N3\"\n  summary: \"Cross-judge type ranking ρ=0.09 严重削弱 C2 partial ordering\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"§5.2 加 judge-model pairing 解释 + pooled ρ≥0.71; Intro partial ordering 加 ±15pp 限定.\"\n  resolution_round: 21\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R21-N4\"\n  summary: \"Taxonomy 类型选择缺定量依据 + C3 inconclusive 未在 Intro 反映\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"§3 加三项 design criteria (attestation + minimal-pair + mutual exclusivity).\"\n  resolution_round: 21\n  first_raised_round: 18\n  last_seen_round: 21\n\n- id: \"R21-W1\"\n  summary: \"Error analysis LLM 编码循环性需人工验证\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Limitations Measurement 段加 camera-ready human validation 声明.\"\n  resolution_round: 21\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R21-W2\"\n  summary: \"DN 是 ambiguity collapse 场景迁移非概念创新\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"§6.2 主题句改为 agentic-context manifestation of ambiguity collapse.\"\n  resolution_round: 21\n  first_raised_round: 18\n  last_seen_round: 21\n\n- id: \"R21-W3\"\n  summary: \"Abstract 应突出 confound-free range\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"34.0pp headline 在前, confound-free range 紧随其后.\"\n  resolution_round: 21\n  first_raised_round: 19\n  last_seen_round: 21\n\n- id: \"R21-W4\"\n  summary: \"Human validation per-type 样本量不足\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"§4.4 加 pooled-only 限定 + per-type wide CI 警告.\"\n  resolution_round: 21\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R21-W5\"\n  summary: \"Temperature=0 跨 provider 确定性假设未讨论\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Limitations Scope 段加 cross-provider stochasticity + ICC 覆盖范围限定.\"\n  resolution_round: 21\n  first_raised_round: 21\n  last_seen_round: 21\n\n- id: \"R21-W6\"\n  summary: \"BibTeX key mou_ambigswe_2026 与 author 不匹配\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"全文替换 mou_ambigswe_2026 → vijayvargiya_ambigswe_2026.\"\n  resolution_round: 21\n  first_raised_round: 21\n  last_seen_round: 21\n\n- id: \"R21-M1\"\n  summary: \"Abstract 信息密度偏高 (5 个数字)\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"删除 NMI 具体值, 保留 order-of-magnitude; ≤4 核心数值.\"\n  resolution_round: 21\n\n- id: \"R21-M2\"\n  summary: \"Systematic nocuity 与 Berry & Kamsties 方向偏差\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"§6.3 加 divergent→convergent 方向反转说明.\"\n  resolution_round: 21\n\n- id: \"R21-M3\"\n  summary: \"NMI=0.23 绝对值 modest, 补 Cramér's V\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Discussion taxonomy 段补 Cramér's V=0.45.\"\n  resolution_round: 21\n\n- id: \"R20-N1\"\n  summary: \"17× definitional circularity\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"17× → order-of-magnitude; §6.1 区分 definitional vs empirical\"\n  resolution_round: 20\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R20-N2\"\n  summary: \"Missing Ambig-SWE\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Added citation in §2, §6.2, §9\"\n  resolution_round: 20\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R20-W9\"\n  summary: \"Bib fixes (duplicate + Anonymous + type)\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"All fixed\"\n  resolution_round: 20\n  first_raised_round: 20\n  last_seen_round: 20\n\n- id: \"R20-W11\"\n  summary: \"Abstract density\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Reduced from 7+ to ≤4 numbers across R20-R21\"\n  resolution_round: 21\n  first_raised_round: 20\n  last_seen_round: 21\n\n- id: \"R19-N1\"\n  summary: \"Ecological validity\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Synthetic conditions qualifier + Limitations paragraph\"\n  resolution_round: 19\n  first_raised_round: 19\n\n- id: \"R19-N2\"\n  summary: \"Behaviorally indistinguishable contradiction\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Reworded to comparable safety impact\"\n  resolution_round: 19\n  first_raised_round: 19\n\n- id: \"R19-N3\"\n  summary: \"Auth scope κ=0.385 claims\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Downgraded with caution caveats\"\n  resolution_round: 19\n  first_raised_round: 19\n\n- id: \"R18-N1\"\n  summary: \"C2 mid-tier ordering\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"C2 降为 secondary, robust extremes only\"\n  resolution_round: 18\n  first_raised_round: 18\n\n- id: \"R18-N2\"\n  summary: \"Judge-model confound\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Cross-family validation κ=0.717\"\n  resolution_round: 19\n  first_raised_round: 18\n\n- id: \"R17-N1\"\n  summary: \"30× MI ratio\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"30× → 17× → order-of-magnitude\"\n  resolution_round: 20\n  first_raised_round: 17"
  }
}
```

</details>

---


### Tool result

_source line 1968 · 2026-05-23T04:43:28.781713+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 10681}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1969 · 2026-05-23T04:46:12.553628+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 22 (Fresh Review)\n## Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\n**Venue**: EMNLP 2026 (ARR May cycle) | **审稿日期**: 2026-05-23\n\n---\n\n## Summary\n\n本文提出首个针对策略歧义对 LLM agent 安全影响的 matched-pair 因果研究。在 τ²-bench 上构建 300 对歧义/无歧义策略条款，跨五个前沿模型（GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3）和 2,997 episodes 评估六类歧义的影响。核心发现：歧义条款使违规率增加 34.0 pp（排除 confounded incompleteness 后 +18.7 至 +36.0 pp）；条款措辞解释 22.4% 方差而类型仅 0.4%；类型预测失败机制比预测违规率强一个数量级（NMI = 0.23 vs 0.01）。\n\n---\n\n## Strengths\n\n**S1. 严格的 matched-pair 因果设计。** 最小编辑条款对构建（§4.2, κ=0.95 标注一致性）配合 perturbation control（n=300, Δ=−0.67pp）建立了真正的因果推断，超越前人工作的相关性证据。Cross-judge 设计消除同模型自评偏差，matched-pair 结构使系统性 judge 偏差在处理效应（Δpp）中自动消除。[R1-S1, R2-S1]\n\n**S2. 多层次验证体系。** Type III SS 方差分解、排列检验（p<0.001）、ICC 复制（0.919）、七级 TOST 敏感性（Appendix A）、bootstrap 聚类（B=10,000）、三家族 cross-judge 验证（Fleiss' κ=0.717）、Holm-Bonferroni 校正——验证密度在同类工作中罕见。[R1-S5, R2-S2]\n\n**S3. 可操作的方差分解。** 条款措辞 22.4% >> 类型 0.4% 直接指导实践：条款级审计比类型级分类更有效。这比单纯报告\"歧义有害\"更进一步，具有工程可落地性。[R1-S2, R2-S3]\n\n**S4. Taxonomy 重构为诊断工具。** 类型预测失败机制（NMI=0.23, Cramér's V=0.45）比预测违规率（NMI=0.014）强一个数量级，将分类法从风险预测器重构为诊断工具——概念上的重要区分。三种失败机制（structural misparse, information gap-filling, boundary violation）与类型的映射提供了超越风险量化的诊断视角。[R1-S4, R2-S5]\n\n**S5. 跨模型、跨基准复制。** 5+2 个模型（含 Gemini 2.5 Flash, LLaMA 4 Scout）+ SOPBench 跨基准复制，效应方向在所有 7 个模型上一致。[R2-S4]\n\n**S6. 对局限性的坦诚处理。** Authorization scope 低 κ=0.385、cross-judge ρ=0.09、incompleteness confound、severity threshold 未预注册——透明度增强论文可信度。Taxonomy 主动定位为 experimental instrument。[R1-S3, R2-S6]\n\n**S7. 缓解实验闭环。** Type-specific prompt 实验（Appendix B）展示类型依赖的缓解效果（auth scope −18.0pp vs incompleteness −3.3pp n.s.），从诊断到干预形成闭环。[R1-S6, R2-S7]\n\n---\n\n## Weaknesses\n\n### Should-Fix（共识问题）\n\n**W1 [Should-Fix, Critical]. C4 model×type 交互可能是测量伪影。** C4 交互完全由 authorization scope 驱动（排除后 p=0.97, Appendix M）。该类型同时具有四个测量不稳定指标：最低 inter-judge κ（0.385）、最高 cross-judge 方差（41.6%–65.6%）、within-replication ICC≈0、跨 judge 组排名不一致的唯一驱动因素。虽已标注\"[Exploratory]\"，但 §5.3 的呈现规格（独立小节+专门图表）仍暗示实质性发现。建议：模拟 κ=0.385 噪声下交互检验假阳性率，或在正文明确降级 C4。[R1-W2, R2 全部同意]\n\n**W2 [Should-Fix]. SOPBench 复制效应压缩 63% 缺乏原则性归因。** τ²-bench +34.0pp → SOPBench +12.6pp，三个 post-hoc 解释（测量粒度、负向任务、结构差异）未量化各因素贡献。对于安全相关发现，3× 效应量差异值得更系统的归因。建议：在 τ²-bench 上以 constraint-level 重新分析，或原则性论证方向一致性的充分性。[R1-W1, R2 同意]\n\n**W3 [Should-Fix]. ICC 复制仅覆盖 OpenAI 家族。** ICC=0.919 和残差分解 ICC(1)=0.749 均在 OpenAI 内计算，但用于刻画所有五个模型的 60.8% 残差。跨 provider 随机性可能更高（不同 temperature=0 实现、MoE vs dense 架构差异）。建议：至少一个非 OpenAI 模型的小规模 ICC 复制，或明确标注适用范围。[R1-W3, R2 同意]\n\n**W4 [Should-Fix]. SESOI ±15pp 缺乏领域接地。** 两个论证标准（2× 测量噪声、缓解策略阈值）分别是精度论证和无经验支撑的判断。七级敏感性分析部分缓解。但 R2 补充 nuance：agent safety 新兴领域无先例标准，pilot study 阶段可接受。建议：明确承认 SESOI 是统计驱动的；讨论未来领域锚点。[R1-W4, R2 同意 with nuance]\n\n**W5 [Should-Fix]. Token count 作为 incompleteness confound 代理过于粗糙。** Token count 无法捕获语义信息密度。论文整体策略保守（已排除 incompleteness 报告 confound-free range），但基于 incompleteness 的二级结论（最高系统性 nocuity 率 OR=2.61; 对 prompt 缓解最有抵抗力 −3.3pp n.s.）仍受 confound 影响。建议：对这些二级结论添加更强 caveat。[R1-W5, R2 部分同意]\n\n**W6 [Should-Fix]. 残差方差干预天花板讨论不充分。** Discussion §7 已提及 clause-level auditing 为\"the largest actionable component\"，但未明确量化干预上限的实际含义：即使完美消除歧义，仍有 60.8% 违规变异来自其他因素。建议：增加 2-3 句框架化干预天花板。[R2-W2, R1 同意]\n\n### Minor（共识问题）\n\n**W7 [Minor]. 生态效度缺口未量化。** 34.0pp 标注为\"上界\"但未量化与真实策略文档歧义的预期差距。SOPBench +12.6pp 可作粗略下界参考但未在论文中建立此连接。[R1-W6, R2 同意]\n\n**W8 [Minor]. 层级结构（C3）未通过 Holm-Bonferroni 校正。** p=0.017 vs threshold 0.0125，已注释为\"organizational convenience\"，但读者可能误解两层结构为经验发现。[R1-W7, R2 同意]\n\n**W9 [Minor]. 人工 failure-mode 编码验证缺失。** 100 traces 人工验证在进行中但当前版本未完成。Failure mechanism 分析（§6）是重要贡献之一，LLM 编码 LLM 失败的循环性风险需 camera-ready 前解决。[R1-W8, R2 同意]\n\n**W10 [Minor]. Table 2/Figure 2 应标注 incompleteness confound。** Table 2 展示原始 +49.2pp 但 confound 讨论在 §5.1 末段和 Appendix F，相隔较远。加脚注即可。[R2-W7, R1 同意]\n\n**W11 [Minor]. Conclusion 偏短。** 约 5 句，建议扩展 1-2 句涵盖干预天花板含义和分析逻辑链。[R2-W6, R1 同意]\n\n### 不构成 Weakness 的 R2 关切（R1 成功反驳）\n\n- **Cross-judge ρ=0.09 已在正文 §5.2 明确报告**（R2 误称\"藏在 Appendix\"，R1 引用原文反驳）\n- **Abstract 信息密度**：因果研究报告效应量及边界条件为学术惯例，R1 反驳合理\n- **Taxonomy instrument 定位**：在 C3 未过校正、跨域 ρ=0.26 等限制下，instrument 定位是诚实且策略性正确的\n- **Limitations §9 Measurement 段已覆盖 cross-judge 测量问题的根因**\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键判断上达成共识 [AGREE]：\n\n1. **Soundness 4.0/5**：方法论严谨，主要 claims 有充分支撑\n2. **Overall 3.5 (Borderline Conference)**：方法论贡献实在但外部有效性不足\n3. **C4 交互分析不可靠**（W1）：最强共识点，R2 称 R1 的分析\"最精准\"\n4. **SOPBench 压缩需归因**（W2）\n5. **ICC 跨 provider 验证不足**（W3）\n6. **SESOI 统计驱动非领域驱动**（W4）\n7. **Incompleteness 二级结论需 caveat**（W5）\n8. **干预天花板需显式化**（W6）\n9. 所有 5 个 Minor 问题均达成共识\n\n## Reviewer Divergence\n\n| 维度 | R1 | R2 | 分歧根源 |\n|------|----|----|----------|\n| Excitement | 3.5/5 | 3.0/5 | R1 认为 matched-pair 因果设计在 agent safety 领域的首次应用构成显著方法论推进；R2 强调各组件增量性（taxonomy 是 Li et al. 子集重组，DN 是 ambiguity collapse 重命名）|\n\nR1 的 4 个 REBUT（R2-W1, W3, W4, W8）均有事实依据或合理论证，不构成未解决分歧。\n\n---\n\n## Questions for Authors\n\n**Q1.** 能否将 SOPBench 效应压缩分解为测量粒度 vs 领域差异 vs 结构差异？例如在 τ²-bench 上以 constraint-level 重新分析。[R1-Q1, R2 同意]\n\n**Q2.** 在模拟 κ=0.385（auth scope）vs κ=0.65+（其他类型）测量噪声下，C4 交互检验的期望假阳性率是多少？[R1-Q2, R2 同意]\n\n**Q3.** Auth scope ICC≈0 下 Figure 3 中 52pp 跨模型范围如何解释？建议在 Figure 3 中为 auth scope 添加低可靠性标注。[R1-Q3, R2 补充]\n\n**Q4.** 是否考虑过语义复杂度指标（如独立操作约束计数、BERTScore）替代 token count 控制 incompleteness confound？[R1-Q4, R2 补充]\n\n**Q5.** 跨域类型排名不一致（ρ=0.26）是否意味着 taxonomy 的诊断价值仅限于 type→mechanism 映射，实践者是否需要领域特定校准？[R1-Q5, R2 同意]\n\n**Q6.** 多条款歧义交互效应（如同一策略中同时存在 auth scope + incompleteness）是否考虑？[R2-Q5]\n\n**Q7.** 4.6% disambiguation awareness 各模型间差异如何？Claude（RLHF 对齐更强）是否显著高于 DeepSeek/Qwen3？[R2-Q3]\n\n**Q8.** Type-specific vs generic disambiguation prompt 的效果量对比是否可提供？这对部署指导更直接。[R2-Q4, R1 补充]\n\n---\n\n## Missing References\n\n无关键遗漏。Related work 覆盖充分（agent safety, NLP ambiguity, RE literature, psycholinguistics）。\n\n**可选补充**：\n- Byrt et al. (1993) κ 流行度悖论 —— 与 Appendix G coreferential κ=0.479 讨论直接相关 [R1 建议]\n- Kinniment et al. (2024) agent 自主性评估框架 [R2 可选]\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）**：未配置，本轮未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 10 info, 0 critical）。主要发现：\n\n**Warnings:**\n1. **Pages 4-6**：连续三页纯文本（Method §4 至 Results §5.2 开头），无 figure/table 穿插，建议用流程图或提前放置 Table 2 打破文字墙\n2. **Page 7**：Table 2 + Figure 2 + Figure 3 三个 display items 集中在同一页，与前三页纯文本形成强烈反差，建议将部分前移至 page 5-6 均衡视觉节奏\n3. **Pages 8-9**：Error Analysis/Discussion/Conclusion/Limitations 连续两页无 display item\n\n**Info 亮点：**\n- 正文共 4 个 display items / 8 页 = 0.5/页，对实证论文偏少（通常 5-8 个）\n- Figure 1 全宽实验概览图清晰但图内文字偏小\n- 未发现 margin 溢出、LaTeX 渲染错误、未解析引用 [?] 或排版问题\n- 格式合规：ACL template ✓, double-blind ✓, booktabs ✓, Limitations in main text ✓\n\n---\n\n## Overall Assessment\n\n### 维度评分\n\n| 维度 | 评分 | 说明 |\n|------|------|------|\n| Soundness | 4.0/5 | Matched-pair 设计和 perturbation control 建立严格因果推断。主要不足：auth scope 测量不可靠影响 C4；ICC 仅 OpenAI；SESOI 缺领域接地 |\n| Excitement | 3.0–3.5/5 | R1: 3.5（方法论首次应用有价值），R2: 3.0（各组件增量性）。圆桌判定：**3.25**，偏向 R1——matched-pair 因果设计在 agent safety 领域确实是方法论推进，但受限于两个客服领域和合成刺激 |\n| Reproducibility | 4.0/5 | 实验细节充分，代码数据承诺发布。扣分：依赖闭源 API，ICC 未跨 provider 验证 |\n\n### Overall: **3.5 — Borderline Conference**\n\n**Confidence**: 4/5（两位 Reviewer 独立得出相同结论，交叉验证增强可信度）\n\n### 总评\n\n方法论严谨的因果研究。Matched-pair 设计 + perturbation control 在 agent safety 领域首次建立了从策略歧义到安全违规的因果链，方差分解（clause 22.4% >> type 0.4%）提供了可操作洞见，failure mechanism 映射赋予 taxonomy 诊断价值。执行质量高于平均 submission，附录验证体系全面。\n\n主要不足：(1) C4 model×type 交互的唯一驱动类型（auth scope）测量不可靠，该发现可能是伪影；(2) SOPBench 跨基准复制效应压缩 63%，缺乏原则性归因；(3) 外部有效性受限（两个客服领域、合成刺激、仅前沿模型）；(4) 60.8% 残差方差限制了 clause-level auditing 的实际干预天花板。\n\n论文 Soundness 足以被 Findings 接收。是否进入 main conference 取决于 AC 对以下问题的判断：matched-pair 因果设计的首次应用 + 22.4%/0.4% 方差分解的可操作性是否达到 Conference 的 novelty bar。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Opening retail example 有效且具体，narrative flow 从 example → gap → method → results 连贯\n- Contribution (2) 中\"order of magnitude\"表述准确（NMI 16.8×，Appendix S）\n- Contribution 列表清晰，三项贡献层次分明\n\n### §2 Related Work\n- 覆盖全面：agent safety, ambiguity in NLP/RE, psycholinguistics, policy specification\n- ASPI tension（clarification-seeking → prompt injection）和 Ambig-SWE（interactive disambiguation）均已讨论\n- DRIP-R 的三点区分（因果性、安全违规、两层 taxonomy）清晰\n\n### §3 Taxonomy\n- 六类互斥性在实验目的下可接受\n- 三项 design criteria（attestation + minimal-pair + mutual exclusivity）为筛选提供了操作标准\n- 排除 ellipsis 和 pragmatic implicature 的理由充分\n- §3 末段\"Scope of ambiguity\"透明地讨论了 taxonomy 的包容性定义\n\n### §4 Method\n- Matched-pair 设计优雅，96% 初始标注一致率（κ=0.95）充分\n- Cross-judge 设计消除自评偏差\n- Perturbation control（n=300）有效排除表面文本变化\n- SESOI 论证需加强（见 W4）\n\n### §5 Results\n- C1 效应量强大（+34.0pp, OR=15.1）且统计显著（p<10^-105）\n- C2 partial ordering 框架合理：robust extremes + margin-dependent mid-tier\n- §5.2 关于 ρ=0.09 的 \"important qualification\" 透明且恰当\n- C4 需降级或补充测量噪声分析（见 W1）\n\n### §6 Analysis\n- 三种失败机制分类有诊断价值\n- Disambiguation neglect 量化（4.6%）有价值，术语定位诚实\n- Systematic nocuity（41.3% 收敛违规）是有趣发现\n- Failure mode coding 需人工验证（见 W9）\n\n### §7 Discussion\n- Differential nocuity 假设框架恰当\n- Taxonomy 作为诊断工具（NMI 0.23 vs 0.01）的论证有力\n- 干预天花板需更明确讨论（见 W6）\n\n### §8 Conclusion\n- 核心数字准确，confound-free range 限定恰当\n- 偏短，可扩展（见 W11）\n\n### §9 Limitations\n- 覆盖生态效度、范围、测量、confound、disambiguation channel——全面\n- Camera-ready human validation 承诺恰当\n\n### Appendix\n- 24 个 appendix 提供了全面的验证体系\n- Cross-judge 验证（Appendix W, Fleiss' κ=0.717）是重要补充\n- SOPBench 复制（Appendix V）需更系统的归因分析\n\n### 格式合规\n- 正文 ≤ 8 页 ✓ | Double-blind ✓ | ACL template (review mode) ✓\n- Limitations in main text ✓ | Booktabs ✓ | References format consistent ✓\n- 图表标题自解释 ✓ | 无排版错误 ✓",
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 22 (Fresh Review)\n## Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\n**Venue**: EMNLP 2026 (ARR May cycle) | **审稿日期**: 2026-05-23\n\n---\n\n## Summary\n\n本文提出首个针对策略歧义对 LLM agent 安全影响的 matched-pair 因果研究。在 τ²-bench 上构建 300 对歧义/无歧义策略条款，跨五个前沿模型（GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3）和 2,997 episodes 评估六类歧义的影响。核心发现：歧义条款使违规率增加 34.0 pp（排除 confounded incompleteness 后 +18.7 至 +36.0 pp）；条款措辞解释 22.4% 方差而类型仅 0.4%；类型预测失败机制比预测违规率强一个数量级（NMI = 0.23 vs 0.01）。\n\n---\n\n## Strengths\n\n**S1. 严格的 matched-pair 因果设计。** 最小编辑条款对构建（§4.2, κ=0.95 标注一致性）配合 perturbation control（n=300, Δ=−0.67pp）建立了真正的因果推断，超越前人工作的相关性证据。Cross-judge 设计消除同模型自评偏差，matched-pair 结构使系统性 judge 偏差在处理效应（Δpp）中自动消除。[R1-S1, R2-S1]\n\n**S2. 多层次验证体系。** Type III SS 方差分解、排列检验（p<0.001）、ICC 复制（0.919）、七级 TOST 敏感性（Appendix A）、bootstrap 聚类（B=10,000）、三家族 cross-judge 验证（Fleiss' κ=0.717）、Holm-Bonferroni 校正——验证密度在同类工作中罕见。[R1-S5, R2-S2]\n\n**S3. 可操作的方差分解。** 条款措辞 22.4% >> 类型 0.4% 直接指导实践：条款级审计比类型级分类更有效。这比单纯报告\"歧义有害\"更进一步，具有工程可落地性。[R1-S2, R2-S3]\n\n**S4. Taxonomy 重构为诊断工具。** 类型预测失败机制（NMI=0.23, Cramér's V=0.45）比预测违规率（NMI=0.014）强一个数量级，将分类法从风险预测器重构为诊断工具——概念上的重要区分。三种失败机制（structural misparse, information gap-filling, boundary violation）与类型的映射提供了超越风险量化的诊断视角。[R1-S4, R2-S5]\n\n**S5. 跨模型、跨基准复制。** 5+2 个模型（含 Gemini 2.5 Flash, LLaMA 4 Scout）+ SOPBench 跨基准复制，效应方向在所有 7 个模型上一致。[R2-S4]\n\n**S6. 对局限性的坦诚处理。** Authorization scope 低 κ=0.385、cross-judge ρ=0.09、incompleteness confound、severity threshold 未预注册——透明度增强论文可信度。Taxonomy 主动定位为 experimental instrument。[R1-S3, R2-S6]\n\n**S7. 缓解实验闭环。** Type-specific prompt 实验（Appendix B）展示类型依赖的缓解效果（auth scope −18.0pp vs incompleteness −3.3pp n.s.），从诊断到干预形成闭环。[R1-S6, R2-S7]\n\n---\n\n## Weaknesses\n\n### Should-Fix（共识问题）\n\n**W1 [Should-Fix, Critical]. C4 model×type 交互可能是测量伪影。** C4 交互完全由 authorization scope 驱动（排除后 p=0.97, Appendix M）。该类型同时具有四个测量不稳定指标：最低 inter-judge κ（0.385）、最高 cross-judge 方差（41.6%–65.6%）、within-replication ICC≈0、跨 judge 组排名不一致的唯一驱动因素。虽已标注\"[Exploratory]\"，但 §5.3 的呈现规格（独立小节+专门图表）仍暗示实质性发现。建议：模拟 κ=0.385 噪声下交互检验假阳性率，或在正文明确降级 C4。[R1-W2, R2 全部同意]\n\n**W2 [Should-Fix]. SOPBench 复制效应压缩 63% 缺乏原则性归因。** τ²-bench +34.0pp → SOPBench +12.6pp，三个 post-hoc 解释（测量粒度、负向任务、结构差异）未量化各因素贡献。对于安全相关发现，3× 效应量差异值得更系统的归因。建议：在 τ²-bench 上以 constraint-level 重新分析，或原则性论证方向一致性的充分性。[R1-W1, R2 同意]\n\n**W3 [Should-Fix]. ICC 复制仅覆盖 OpenAI 家族。** ICC=0.919 和残差分解 ICC(1)=0.749 均在 OpenAI 内计算，但用于刻画所有五个模型的 60.8% 残差。跨 provider 随机性可能更高（不同 temperature=0 实现、MoE vs dense 架构差异）。建议：至少一个非 OpenAI 模型的小规模 ICC 复制，或明确标注适用范围。[R1-W3, R2 同意]\n\n**W4 [Should-Fix]. SESOI ±15pp 缺乏领域接地。** 两个论证标准（2× 测量噪声、缓解策略阈值）分别是精度论证和无经验支撑的判断。七级敏感性分析部分缓解。但 R2 补充 nuance：agent safety 新兴领域无先例标准，pilot study 阶段可接受。建议：明确承认 SESOI 是统计驱动的；讨论未来领域锚点。[R1-W4, R2 同意 with nuance]\n\n**W5 [Should-Fix]. Token count 作为 incompleteness confound 代理过于粗糙。** Token count 无法捕获语义信息密度。论文整体策略保守（已排除 incompleteness 报告 confound-free range），但基于 incompleteness 的二级结论（最高系统性 nocuity 率 OR=2.61; 对 prompt 缓解最有抵抗力 −3.3pp n.s.）仍受 confound 影响。建议：对这些二级结论添加更强 caveat。[R1-W5, R2 部分同意]\n\n**W6 [Should-Fix]. 残差方差干预天花板讨论不充分。** Discussion §7 已提及 clause-level auditing 为\"the largest actionable component\"，但未明确量化干预上限的实际含义：即使完美消除歧义，仍有 60.8% 违规变异来自其他因素。建议：增加 2-3 句框架化干预天花板。[R2-W2, R1 同意]\n\n### Minor（共识问题）\n\n**W7 [Minor]. 生态效度缺口未量化。** 34.0pp 标注为\"上界\"但未量化与真实策略文档歧义的预期差距。SOPBench +12.6pp 可作粗略下界参考但未在论文中建立此连接。[R1-W6, R2 同意]\n\n**W8 [Minor]. 层级结构（C3）未通过 Holm-Bonferroni 校正。** p=0.017 vs threshold 0.0125，已注释为\"organizational convenience\"，但读者可能误解两层结构为经验发现。[R1-W7, R2 同意]\n\n**W9 [Minor]. 人工 failure-mode 编码验证缺失。** 100 traces 人工验证在进行中但当前版本未完成。Failure mechanism 分析（§6）是重要贡献之一，LLM 编码 LLM 失败的循环性风险需 camera-ready 前解决。[R1-W8, R2 同意]\n\n**W10 [Minor]. Table 2/Figure 2 应标注 incompleteness confound。** Table 2 展示原始 +49.2pp 但 confound 讨论在 §5.1 末段和 Appendix F，相隔较远。加脚注即可。[R2-W7, R1 同意]\n\n**W11 [Minor]. Conclusion 偏短。** 约 5 句，建议扩展 1-2 句涵盖干预天花板含义和分析逻辑链。[R2-W6, R1 同意]\n\n### 不构成 Weakness 的 R2 关切（R1 成功反驳）\n\n- **Cross-judge ρ=0.09 已在正文 §5.2 明确报告**（R2 误称\"藏在 Appendix\"，R1 引用原文反驳）\n- **Abstract 信息密度**：因果研究报告效应量及边界条件为学术惯例，R1 反驳合理\n- **Taxonomy instrument 定位**：在 C3 未过校正、跨域 ρ=0.26 等限制下，instrument 定位是诚实且策略性正确的\n- **Limitations §9 Measurement 段已覆盖 cross-judge 测量问题的根因**\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键判断上达成共识 [AGREE]：\n\n1. **Soundness 4.0/5**：方法论严谨，主要 claims 有充分支撑\n2. **Overall 3.5 (Borderline Conference)**：方法论贡献实在但外部有效性不足\n3. **C4 交互分析不可靠**（W1）：最强共识点，R2 称 R1 的分析\"最精准\"\n4. **SOPBench 压缩需归因**（W2）\n5. **ICC 跨 provider 验证不足**（W3）\n6. **SESOI 统计驱动非领域驱动**（W4）\n7. **Incompleteness 二级结论需 caveat**（W5）\n8. **干预天花板需显式化**（W6）\n9. 所有 5 个 Minor 问题均达成共识\n\n## Reviewer Divergence\n\n| 维度 | R1 | R2 | 分歧根源 |\n|------|----|----|----------|\n| Excitement | 3.5/5 | 3.0/5 | R1 认为 matched-pair 因果设计在 agent safety 领域的首次应用构成显著方法论推进；R2 强调各组件增量性（taxonomy 是 Li et al. 子集重组，DN 是 ambiguity collapse 重命名）|\n\nR1 的 4 个 REBUT（R2-W1, W3, W4, W8）均有事实依据或合理论证，不构成未解决分歧。\n\n---\n\n## Questions for Authors\n\n**Q1.** 能否将 SOPBench 效应压缩分解为测量粒度 vs 领域差异 vs 结构差异？例如在 τ²-bench 上以 constraint-level 重新分析。[R1-Q1, R2 同意]\n\n**Q2.** 在模拟 κ=0.385（auth scope）vs κ=0.65+（其他类型）测量噪声下，C4 交互检验的期望假阳性率是多少？[R1-Q2, R2 同意]\n\n**Q3.** Auth scope ICC≈0 下 Figure 3 中 52pp 跨模型范围如何解释？建议在 Figure 3 中为 auth scope 添加低可靠性标注。[R1-Q3, R2 补充]\n\n**Q4.** 是否考虑过语义复杂度指标（如独立操作约束计数、BERTScore）替代 token count 控制 incompleteness confound？[R1-Q4, R2 补充]\n\n**Q5.** 跨域类型排名不一致（ρ=0.26）是否意味着 taxonomy 的诊断价值仅限于 type→mechanism 映射，实践者是否需要领域特定校准？[R1-Q5, R2 同意]\n\n**Q6.** 多条款歧义交互效应（如同一策略中同时存在 auth scope + incompleteness）是否考虑？[R2-Q5]\n\n**Q7.** 4.6% disambiguation awareness 各模型间差异如何？Claude（RLHF 对齐更强）是否显著高于 DeepSeek/Qwen3？[R2-Q3]\n\n**Q8.** Type-specific vs generic disambiguation prompt 的效果量对比是否可提供？这对部署指导更直接。[R2-Q4, R1 补充]\n\n---\n\n## Missing References\n\n无关键遗漏。Related work 覆盖充分（agent safety, NLP ambiguity, RE literature, psycholinguistics）。\n\n**可选补充**：\n- Byrt et al. (1993) κ 流行度悖论 —— 与 Appendix G coreferential κ=0.479 讨论直接相关 [R1 建议]\n- Kinniment et al. (2024) agent 自主性评估框架 [R2 可选]\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）**：未配置，本轮未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 10 info, 0 critical）。主要发现：\n\n**Warnings:**\n1. **Pages 4-6**：连续三页纯文本（Method §4 至 Results §5.2 开头），无 figure/table 穿插，建议用流程图或提前放置 Table 2 打破文字墙\n2. **Page 7**：Table 2 + Figure 2 + Figure 3 三个 display items 集中在同一页，与前三页纯文本形成强烈反差，建议将部分前移至 page 5-6 均衡视觉节奏\n3. **Pages 8-9**：Error Analysis/Discussion/Conclusion/Limitations 连续两页无 display item\n\n**Info 亮点：**\n- 正文共 4 个 display items / 8 页 = 0.5/页，对实证论文偏少（通常 5-8 个）\n- Figure 1 全宽实验概览图清晰但图内文字偏小\n- 未发现 margin 溢出、LaTeX 渲染错误、未解析引用 [?] 或排版问题\n- 格式合规：ACL template ✓, double-blind ✓, booktabs ✓, Limitations in main text ✓\n\n---\n\n## Overall Assessment\n\n### 维度评分\n\n| 维度 | 评分 | 说明 |\n|------|------|------|\n| Soundness | 4.0/5 | Matched-pair 设计和 perturbation control 建立严格因果推断。主要不足：auth scope 测量不可靠影响 C4；ICC 仅 OpenAI；SESOI 缺领域接地 |\n| Excitement | 3.0–3.5/5 | R1: 3.5（方法论首次应用有价值），R2: 3.0（各组件增量性）。圆桌判定：**3.25**，偏向 R1——matched-pair 因果设计在 agent safety 领域确实是方法论推进，但受限于两个客服领域和合成刺激 |\n| Reproducibility | 4.0/5 | 实验细节充分，代码数据承诺发布。扣分：依赖闭源 API，ICC 未跨 provider 验证 |\n\n### Overall: **3.5 — Borderline Conference**\n\n**Confidence**: 4/5（两位 Reviewer 独立得出相同结论，交叉验证增强可信度）\n\n### 总评\n\n方法论严谨的因果研究。Matched-pair 设计 + perturbation control 在 agent safety 领域首次建立了从策略歧义到安全违规的因果链，方差分解（clause 22.4% >> type 0.4%）提供了可操作洞见，failure mechanism 映射赋予 taxonomy 诊断价值。执行质量高于平均 submission，附录验证体系全面。\n\n主要不足：(1) C4 model×type 交互的唯一驱动类型（auth scope）测量不可靠，该发现可能是伪影；(2) SOPBench 跨基准复制效应压缩 63%，缺乏原则性归因；(3) 外部有效性受限（两个客服领域、合成刺激、仅前沿模型）；(4) 60.8% 残差方差限制了 clause-level auditing 的实际干预天花板。\n\n论文 Soundness 足以被 Findings 接收。是否进入 main conference 取决于 AC 对以下问题的判断：matched-pair 因果设计的首次应用 + 22.4%/0.4% 方差分解的可操作性是否达到 Conference 的 novelty bar。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Opening retail example 有效且具体，narrative flow 从 example → gap → method → results 连贯\n- Contribution (2) 中\"order of magnitude\"表述准确（NMI 16.8×，Appendix S）\n- Contribution 列表清晰，三项贡献层次分明\n\n### §2 Related Work\n- 覆盖全面：agent safety, ambiguity in NLP/RE, psycholinguistics, policy specification\n- ASPI tension（clarification-seeking → prompt injection）和 Ambig-SWE（interactive disambiguation）均已讨论\n- DRIP-R 的三点区分（因果性、安全违规、两层 taxonomy）清晰\n\n### §3 Taxonomy\n- 六类互斥性在实验目的下可接受\n- 三项 design criteria（attestation + minimal-pair + mutual exclusivity）为筛选提供了操作标准\n- 排除 ellipsis 和 pragmatic implicature 的理由充分\n- §3 末段\"Scope of ambiguity\"透明地讨论了 taxonomy 的包容性定义\n\n### §4 Method\n- Matched-pair 设计优雅，96% 初始标注一致率（κ=0.95）充分\n- Cross-judge 设计消除自评偏差\n- Perturbation control（n=300）有效排除表面文本变化\n- SESOI 论证需加强（见 W4）\n\n### §5 Results\n- C1 效应量强大（+34.0pp, OR=15.1）且统计显著（p<10^-105）\n- C2 partial ordering 框架合理：robust extremes + margin-dependent mid-tier\n- §5.2 关于 ρ=0.09 的 \"important qualification\" 透明且恰当\n- C4 需降级或补充测量噪声分析（见 W1）\n\n### §6 Analysis\n- 三种失败机制分类有诊断价值\n- Disambiguation neglect 量化（4.6%）有价值，术语定位诚实\n- Systematic nocuity（41.3% 收敛违规）是有趣发现\n- Failure mode coding 需人工验证（见 W9）\n\n### §7 Discussion\n- Differential nocuity 假设框架恰当\n- Taxonomy 作为诊断工具（NMI 0.23 vs 0.01）的论证有力\n- 干预天花板需更明确讨论（见 W6）\n\n### §8 Conclusion\n- 核心数字准确，confound-free range 限定恰当\n- 偏短，可扩展（见 W11）\n\n### §9 Limitations\n- 覆盖生态效度、范围、测量、confound、disambiguation channel——全面\n- Camera-ready human validation 承诺恰当\n\n### Appendix\n- 24 个 appendix 提供了全面的验证体系\n- Cross-judge 验证（Appendix W, Fleiss' κ=0.717）是重要补充\n- SOPBench 复制（Appendix V）需更系统的归因分析\n\n### 格式合规\n- 正文 ≤ 8 页 ✓ | Double-blind ✓ | ACL template (review mode) ✓\n- Limitations in main text ✓ | Booktabs ✓ | References format consistent ✓\n- 图表标题自解释 ✓ | 无排版错误 ✓",
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 1970 · 2026-05-23T04:46:16.419474+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3865
}
```

</details>

---


### Assistant

_source line 1971 · 2026-05-23T04:46:26.354271+00:00_

Round 22 审稿完成，报告已投递至 Research Director。

**审稿结果摘要**：

- **Overall: 3.5 — Borderline Conference**（Soundness 4.0, Excitement 3.0–3.5, Reproducibility 4.0）
- **6 个 Should-Fix 共识问题**：C4 auth scope 测量伪影（critical）、SOPBench 63% 压缩归因、ICC 仅 OpenAI、SESOI 缺领域接地、incompleteness 二级结论 caveat、干预天花板显式化
- **5 个 Minor 共识问题**：生态效度量化、C3 层结构标注、人工 failure-mode 验证、Table 2 confound 脚注、Conclusion 扩展
- **视觉审查**：3 warnings（display items 分布不均：pp4-6 纯文字墙 vs p7 三图堆叠）
- **Issue Tracker**: 已同步更新 11 个 open issues

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 187

## Round 187

2 recorded events


### User

_source line 1972 · 2026-05-23T04:46:28.923536+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：

- Reviewer 2 的 W2（残差天花板）、W6（Conclusion 偏短）、W7（Table 2 confound 标注）合理同意
- W1（ρ=0.09 藏在 appendix）反驳——实际在 §5.2 正文已明确报告
- W3（Abstract 过密）、W4（taxonomy 定位）反驳——当前 framing 对因果研究论文合理
- Excitement 3.0 偏低，方法论从相关性→因果推断的推进值 3.5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1973 · 2026-05-23T04:46:41.174481+00:00_

Round 22 审稿已完成。报告已投递至 Research Director。

**最终结论**：

- **Overall: 3.5 (Borderline Conference)**，两位 Reviewer 独立一致
- **Soundness 4.0/5**（共识），**Excitement 3.0–3.5/5**（唯一分歧点）
- **1 个 Critical**：C4 model×type 交互可能是测量伪影（auth scope κ=0.385, ICC≈0，排除后 p=0.97）
- **5 个 Should-Fix**：SOPBench 63% 压缩归因、ICC 仅 OpenAI、SESOI 缺领域接地、incompleteness 二级结论 caveat、干预天花板显式化
- **5 个 Minor**：生态效度量化、C3 层级标注、人工 failure-mode 验证、Table 2 confound 脚注、Conclusion 扩展
- **格式合规全部通过**，视觉审查 3 warnings（display items 分布不均）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 188

## Round 188

58 recorded events


### User

_source line 1974 · 2026-05-23T05:16:51.293292+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1975 · 2026-05-23T05:16:56.975381+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1976 · 2026-05-23T05:16:56.975987+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1977 · 2026-05-23T05:17:02.002838+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,read_project_file,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,read_project_file,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1978 · 2026-05-23T05:17:02.103591+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1979 · 2026-05-23T05:17:05.315966+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1980 · 2026-05-23T05:17:05.366682+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1981 · 2026-05-23T05:17:08.028481+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1982 · 2026-05-23T05:17:09.583847+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1555
}
```

</details>

---


### Tool call

_source line 1983 · 2026-05-23T05:17:09.584382+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1984 · 2026-05-23T05:17:09.634939+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1985 · 2026-05-23T05:17:15.257735+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1986 · 2026-05-23T05:17:15.709840+00:00_

1	\begin{abstract}
2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. We present a matched-pair causal study on $\tau^2$-bench with 300 ambiguous/unambiguous clause pairs spanning a six-type taxonomy, evaluated across five models. Ambiguous clauses are consistently nocuous (i.e., harmful), increasing violation rates by 34.0 percentage points under controlled synthetic conditions ($+$18.7 to $+$36.0\,pp excluding the confounded incompleteness type). Clause wording explains 22.4\% of violation variance versus 0.4\% for type; however, type predicts failure \emph{mechanism} an order of magnitude more strongly than violation rate, establishing the taxonomy as a diagnostic tool. Error analysis reveals disambiguation neglect ($\leq$11\% awareness) and \emph{systematic nocuity}: over 40\% of clauses triggering model-convergent violations. These results, observed in customer-service policy domains under synthetic ambiguity injection, motivate clause-level policy auditing and type-targeted diagnosis for policy-governed deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1987 · 2026-05-23T05:17:15.760551+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1988 · 2026-05-23T05:17:16.212804+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 2002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1989 · 2026-05-23T05:17:16.213185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1990 · 2026-05-23T05:17:16.213454+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_l
…[truncated 4048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1991 · 2026-05-23T05:17:17.267498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 1992 · 2026-05-23T05:17:17.267905+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers (Table~\ref{tab:taxonomy}), selected from \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types) based on three design criteria: (1)~theoretical attestation in prior RE literature \citep{massey_ambiguity_re_2014,berry_kamsties_2004,drip_r_2026}, (2)~amenability to minimal-pair construction without altering clause semantics beyond the target ambiguity, and (3)~mutual exclusivity for unambiguous IV assignment. Types such as ellipsis and pragmatic implicature were excluded because they resist minimal-pair construction within the single-clause policy format.
7	
8	\begin{table}[t]
9	\centering
10	\footnotesize
11	\caption{Six-type ambiguity taxonomy. Disambiguation channel indicates the primary mechanism required to resolve the ambiguity.}
12	\label{tab:taxonomy}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}llll@{}}
15	\toprule
16	\textbf{Type} & \textbf{Layer} & \textbf{Definition} & \textbf{Disambig.\ Channel} \\
17	\midrule
18	Lexical & Ling. & Word/phrase admits multiple senses & Context \\
19	Scopal & Ling. & Quantifier/operator scope underdetermined & Bracketing \\
20	Coreferential & Ling. & Pronoun/NP referent is ambiguous & Resolution \\
21	Auth.\ Scope & Spec. & Permission boundary is vague & Boundary def. \\
22	Incompleteness & Spec. & Required information is absent & Content addition \\
23	Cond.\ Prec. & Spec. & Rules conflict under certain conditions & Priority rule \\
24	\bottomrule
25	\end{tabular}}%
26	\end{table}
27	
28	\paragraph{Linguistic layer.} These types operate at the syntactic or 
…[truncated 2646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1993 · 2026-05-23T05:17:17.669751+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1994 · 2026-05-23T05:17:18.122450+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300; Cohen's $\kappa = 0.95$ on six-type classification); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We
…[truncated 5335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1995 · 2026-05-23T05:17:18.123016+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1996 · 2026-05-23T05:17:18.626304+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around three analyses: the binary ambiguity effect (C1), the type partial ordering (C2, including the inconclusive layer effect C3), and the model$\times$type interaction (C4). C1 and C2 are primary claims; C4 is exploratory.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS avoids ordering dependence in our unbalanced design; logistic regression (Appendix~\ref{app:regression}) confirms concordant results (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}).} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (of which $\sim$15\% is run-to-run stochasticity and $\sim$46\% systematic-but-unmeasured factors, estimated from an OpenAI-family ICC replication; Appendix~\ref{app:residual}). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; controlling for token count changes no type's
…[truncated 7308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1997 · 2026-05-23T05:17:18.727136+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1998 · 2026-05-23T05:17:18.727595+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes (Gwet's AC$_1$ $= 0.62$, $\kappa = 0.52$ \citep{gwet_2014,cohen_1960}). Using LLMs to code LLM failures introduces circularity risk; however, mutual information between type (exogenous) and mechanism labels ($I(\text{type}; \text{mechanism}) = 0.41$ bits, $V = 0.45$; Appendix~\ref{app:type_mechanism}) provides structural evidence against this. Two of the six type--mechanism mappings reflect partial definitional affinity (authorization scope$\to$boundary violation, incompleteness$\to$gap-filling); the remaining four (e.g., scopal$\to$structural misparse, 82.7\% cross-model consistency) are empirically derived.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse}: the agent commits to an incorrect parse, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}. Dominates scopal (5/5), conditional precedence (4/5), and coreferential (3/5).
13	
14	\emph{Information gap-filling}: the agent fills missing information with plausible but incorrect defaults. Dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation}: the agent exceeds permission boundaries when authorization scope is underspecified; 69.2\% involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial). Dominates authorization scope exclusively (5/5).
17	
18	All dominant modes achieve $\geq$3/5 model consistency; scopal and authorization scope are unanimous (5/5).
19	
20	\begin{figure}[t]
21	\centering
22	\includegraphics[width=\columnwidth]{figures/fig
…[truncated 2077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1999 · 2026-05-23T05:17:19.080206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2000 · 2026-05-23T05:17:19.983986+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Our results support a \emph{differential nocuity} hypothesis \citep{berry_kamsties_2004,willis_nocuous_2008}: the binary effect is domain-robust ($p = 0.187$) but type-specific profiles require per-domain calibration ($\rho = 0.26$). Of the 60.8\% unexplained variance, $\sim$15\% is stochastic and $\sim$46\% systematic (ICC $= 0.749$; Appendix~\ref{app:residual}). In customer-service domains, clause-level auditing addresses the largest \emph{actionable} component (22.4\%) but not the majority of outcome variance. Candidate sources of the $\sim$46\% systematic residual include conversation trajectory complexity, task difficulty gradients, and latent policy structure beyond the clause level; conversation trajectory is the most readily measurable next target. Even perfect disambiguation would address at most the 22.4\% clause-wording component; the remaining 60.8\% reflects conversation-level and task-level factors beyond clause wording. Clause-level auditing is therefore a necessary but insufficient safeguard: it targets the largest single actionable component while leaving complementary factors---most immediately, conversation trajectory complexity---for separate mitigation.
6	
7	\paragraph{Taxonomy as diagnostic tool.}
8	Type membership explains only 0.4\% of violation variance versus 22.4\% for clause wording; however, it predicts failure \emph{mechanism} an order of magnitude more strongly than violation rate (NMI $= 0.23$ vs.\ $0.01$, Cram\'{e}r's $V = 0.45$; Appendix~\ref{app:type_mechanism}), validating the taxonomy as a diagnostic tool: each type maps to a dominant failure mechanism (\S\ref{sec:analysis}).
9	
10	\paragraph{Prompt-based mitigation.}
11	Prompt-based mitigation is type-dependent (effective for authorization scope and lexical but not incompleteness; Appendix~\ref{app:mitigation}), reinforcing policy-design over prompt-level fixes.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 2001 · 2026-05-23T05:17:20.034821+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2002 · 2026-05-23T05:17:20.487248+00:00_

1	\section{Conclusion}
2	
3	Under controlled synthetic conditions, policy ambiguity increases agent violations by 34.0\,pp ($+$18.7 to $+$36.0\,pp excluding the confounded incompleteness type). Clause wording explains 22.4\% of variance versus 0.4\% for type, while the taxonomy predicts failure mechanisms an order of magnitude better than violation rate. The type$\to$mechanism mapping (\S\ref{sec:analysis}) provides a diagnostic protocol: types producing structural misparse warrant syntactic rewriting, while gap-filling types require content addition. With $>$89\% disambiguation neglect and over 40\% convergent violations, clause-level auditing is critical for policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2003 · 2026-05-23T05:17:20.537985+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2004 · 2026-05-23T05:17:21.040340+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Ecological validity.} Our ambiguity pairs are synthetically constructed via templates (\S\ref{sec:method}), so the 34.0\,pp effect is an upper bound under controlled conditions; naturally occurring ambiguity in deployed policies may produce smaller effects. The SOPBench replication ($+$12.6\,pp), while directionally consistent, also uses researcher-constructed benchmarks. Neither study measures ambiguity prevalence in real-world policy documents; a dose-response study varying ambiguity density in production policies would help calibrate practical impact. As a rough lower bound, the SOPBench effect ($+$12.6\,pp) under more naturalistic conditions suggests the phenomenon persists at reduced magnitude, though measurement-grain differences preclude direct calibration (\S\ref{sec:results}).
5	
6	\paragraph{Scope.} We evaluate seven API-accessible models from six providers (Appendix~\ref{app:model_expansion}); smaller open-source models (7B--70B) may exhibit different vulnerability patterns. $\tau^2$-bench covers retail and airline customer service only---effects in other domains remain untested. Cross-domain consistency holds for the overall effect (C1, interaction $p = 0.19$) and model ranking ($\rho = 0.90$, $p = 0.037$), but type rankings vary across domains ($\rho = 0.26$, $p = 0.62$); conditional precedence in particular differs by 22\,pp between retail and airline, further motivating the partial-ordering framing. Different providers implement temperature$=$0 with varying determinism (strict argmax vs.\ near-deterministic sampling); our ICC replication (Appendix~\ref{app:residual}) covers only OpenAI models, and cross-provider stochasticity may affect reproducibility estimates. Consequently, the $\sim$15\%/$\sim$46\% stochastic--systematic decomposition within the residual is an OpenAI-family estimate and should not be assumed to generalize across provider architectures. Our matched-pair design requi
…[truncated 3288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2005 · 2026-05-23T05:17:21.040844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2006 · 2026-05-23T05:17:22.095573+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 37860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 2007 · 2026-05-23T05:17:22.095970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 2008 · 2026-05-23T05:17:22.246961+00:00_

1	@inproceedings{li_ambiguity_taxonomy_2024,
2	  title={A Taxonomy of Ambiguity Types for {NLP}},
3	  author={Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.},
4	  booktitle={Proceedings of EACL 2024},
5	  year={2024}
6	}
7	
8	@inproceedings{massey_ambiguity_re_2014,
9	  title={Identifying and Classifying Ambiguity for Regulatory Requirements},
10	  author={Massey, Aaron K. and Rutledge, Richard L. and Ant{\'o}n, Annie I. and Swire, Peter P.},
11	  booktitle={22nd IEEE International Requirements Engineering Conference (RE)},
12	  year={2014},
13	  doi={10.1109/RE.2014.6912250}
14	}
15	
16	@techreport{berry_kamsties_2004,
17	  title={From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook},
18	  author={Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.},
19	  institution={University of Waterloo},
20	  year={2004}
21	}
22	
23	@inproceedings{chantree_2006,
24	  title={Identifying Nocuous Ambiguities in Natural Language Requirements},
25	  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},
26	  booktitle={14th IEEE International Requirements Engineering Conference (RE)},
27	  year={2006}
28	}
29	
30	@incollection{wasow_ambiguity_2005,
31	  title={The Puzzle of Ambiguity},
32	  author={Wasow, Thomas and Perfors, Amy and Beaver, David},
33	  booktitle={Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe},
34	  publisher={CSLI Publications},
35	  year={2005}
36	}
37	
38	@article{kennedy_vagueness_2007,
39	  title={Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives},
40	  author={Kennedy, Christopher},
41	  journal={Linguistics and Philosophy},
42	  volume={30},
43	  number={1},
44	  pages={1--45},
45	  year={2007},
46	  doi={10.1007/s10988-006-9008-0}
47	}
48	
49	@article{willis_nocuous_2008,
50	  title={Automatic Identification of Nocuous Ambiguity},
51	  author={Willis, Alistair and Chantree, Francis and De Roeck
…[truncated 17467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2009 · 2026-05-23T05:17:22.247377+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2010 · 2026-05-23T05:17:22.347951+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2011 · 2026-05-23T05:17:29.124598+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 2012 · 2026-05-23T05:17:30.128581+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "review_issues.yaml",
  "max_chars": "20000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "review_issues.yaml",
    "max_chars": "20000"
  }
}
```

</details>

---


### Tool result

_source line 2013 · 2026-05-23T05:17:36.754444+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's information about EMNLP 2026 call for papers submission guidelines via ARR:

## Submission Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR Submission Process

Papers must be submitted, at latest,
…[truncated 1016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 7629
}
```

</details>

---


### Tool result

_source line 2014 · 2026-05-23T05:17:36.755052+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6626
}
```

</details>

---


### Tool call

_source line 2015 · 2026-05-23T05:17:40.118050+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 page limit format template double blind anonymity requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 page limit format template double blind anonymity requirements"
  }
}
```

</details>

---


### Tool call

_source line 2016 · 2026-05-23T05:17:41.022511+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 2017 · 2026-05-23T05:17:42.542318+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2018 · 2026-05-23T05:17:42.593235+00:00_

1	## Review Issues Tracker — policy_ambiguity_safety
2	## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Latest Round: 22
5	
6	# ============================================================
7	# R22 ISSUES — ALL RESOLVED
8	# ============================================================
9	
10	- id: "R22-W1"
11	  summary: "C4 model×type 交互完全由 authorization scope 驱动，该类型测量不可靠（κ=0.385, ICC≈0），C4 可能是测量伪影"
12	  category: method
13	  severity: critical
14	  status: resolved
15	  resolution: "Removed C4 subsection; compressed to 1 caveat paragraph explicitly framing C4 as possibly reflecting measurement instability. Four indicators cited inline (lowest κ, near-zero ICC, sole driver of ρ=0.09, interaction vanishes excluding auth scope p=0.97). Labeled 'suggestive only'. Figure 3 caption updated."
16	  resolution_round: 22
17	  first_raised_round: 22
18	  last_seen_round: 22
19	  mentions:
20	    - round: 22
21	      reviewers: [1, 2]
22	      note: "R1 提出（W2），R2 完全同意。四个独立指标同时指向测量不稳定：lowest κ, highest cross-judge variance, ICC≈0, C4 排除后 p=0.97。R2 称这是 R1 最强技术点。"
23	
24	- id: "R22-W2"
25	  summary: "SOPBench 复制效应压缩 63%（34.0pp→12.6pp），缺乏原则性归因"
26	  category: experiment
27	  severity: warning
28	  status: resolved
29	  resolution: "Added principled framing in §5.1 (directional consistency as primary criterion; effect-size calibration requires grain-matched measurement). Appendix SOPBench section expanded with structured attribution (3 factors: measurement grain, baseline rate compression, interaction depth)."
30	  resolution_round: 22
31	  first_raised_round: 22
32	  last_seen_round: 22
33	  mentions:
34	    - round: 22
35	      reviewers: [1, 2]
36	      note: "R1 提出（W1），R2 完全同意并升级认同度。三个 post-hoc 解释未量化各因素贡献。R1 建议在 τ²-bench 上以 constraint-level 重新分析。"
37	
38	- id: "R22-W3"
39	  summary: "ICC 复制仅覆盖 OpenAI 家族，但残差方差分解应用于所有模型"
40	  category: method
41	  severity: warning
42	  status: resolved
43	  resolu
…[truncated 12316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2019 · 2026-05-23T05:17:45.807329+00:00_

Web search results for query: "EMNLP 2026 page limit format template double blind anonymity requirements"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Submission Checklist for Original, First Time Submissions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/OriginalSubmissionChecklist"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the web search results, here's what I found about EMNLP 2026 submission requirements:

## Page Limits and Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

For the industry track specifically, the maximum is 6 pages for full-length industry track papers.

## Template

The official EMNLP 2026 LaTeX template uses ACL style files, is in two-column format with an 8-page limit for long papers, and is available through di
…[truncated 575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5689
}
```

</details>

---


### Tool result

_source line 2020 · 2026-05-23T05:17:47.616422+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format guidelines page limit"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on my search results, here are the key submission format guidelines and page limit requirements for ACL Rolling Review 2026:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

Upon acceptance, final versions of long papers will be given
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6593
}
```

</details>

---


### Tool call

_source line 2021 · 2026-05-23T05:18:03.978341+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2022 · 2026-05-23T05:18:04.229884+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2023 · 2026-05-23T05:18:07.894644+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2024 · 2026-05-23T05:18:07.945417+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2025 · 2026-05-23T05:18:29.926860+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 2026 · 2026-05-23T05:18:47.317358+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17390
}
```

</details>

---


### Tool call

_source line 2027 · 2026-05-23T05:18:47.620365+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, Long paper 正文 8 页 + unlimited references\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计页数\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `projects/policy_ambiguity_safety/artifacts/review_round_23/submitted.pdf`\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **实验设计**: matched-pair design 的有效性、300 clause pairs 的构建质量、annotator agreement (κ=0.95)\n2. **统计分析**: McNemar's test、TOST equivalence testing (±15pp SESOI)、Type III SS 方差分解、bootstrap clustering 的适用性和正确性\n3. **评估 pipeline**: cross-judge design (GPT-5.4 + GPT-4.1)、四级严重度量表、二值化阈值选择、cross-judge calibration (κ=0.653/κ_w=0.775)\n4. **控制实验**: perturbation control (n=300, Δ=-0.67pp)、ICC reproducibility (0.919)、information-addition confound for incompleteness\n5. **Confound 处理**: incompleteness 的 token count logistic regression、coreferential 作为 confound-free lower bound 的论证\n6. **Claim 与证据对齐**: C1-C4 每个 claim 是否有充分统计支撑、effect size 解读是否恰当\n7. **残差方差**: 60.8% residual 的 ICC 分解 (15% stochastic + 46% systematic) 是否仅基于 OpenAI family 的问题\n\n### 输出格式\n请按以下结构输出审稿意见：\n- **Summary** (2-3 句)\n- **Strengths** (逐条，S1, S2, ...)\n- **Weaknesses** (逐条，W1, W2, ...，标注 severity: critical/major/minor)\n- **Questions** (Q1, Q2, ...)\n- **Missing References** (如有)\n- **Overall Assessment** (评分 + 置信度)\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, Long paper 正文 8 页 + unlimited references\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计页数\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `projects/policy_ambiguity_safety/artifacts/review_round_23/submitted.pdf`\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **实验设计**: matched-pair design 的有效性、300 clause pairs 的构建质量、annotator agreement (κ=0.95)\n2. **统计分析**: McNemar's test、TOST equivalence testing (±15pp SESOI)、Type III SS 方差分解、bootstrap clustering 的适用性和正确性\n3. **评估 pipeline**: cross-judge design (GPT-5.4 + GPT-4.1)、四级严重度量表、二值化阈值选择、cross-judge calibration (κ=0.653/κ_w=0.775)\n4. **控制实验**: perturbation control (n=300, Δ=-0.67pp)、ICC reproducibility (0.919)、information-addition confound for incompleteness\n5. **Confound 处理**: incompleteness 的 token count logistic regression、coreferential 作为 confound-free lower bound 的论证\n6. **Claim 与证据对齐**: C1-C4 每个 claim 是否有充分统计支撑、effect size 解读是否恰当\n7. **残差方差**: 60.8% residual 的 ICC 分解 (15% stochastic + 46% systematic) 是否仅基于 OpenAI family 的问题\n\n### 输出格式\n请按以下结构输出审稿意见：\n- **Summary** (2-3 句)\n- **Strengths** (逐条，S1, S2, ...)\n- **Weaknesses** (逐条，W1, W2, ...，标注 severity: critical/major/minor)\n- **Questions** (Q1, Q2, ...)\n- **Missing References** (如有)\n- **Overall Assessment** (评分 + 置信度)\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
  }
}
```

</details>

---


### Tool result

_source line 2028 · 2026-05-23T05:19:02.292899+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14672
}
```

</details>

---


### Tool call

_source line 2029 · 2026-05-23T05:19:02.594145+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, Long paper 正文 8 页 + unlimited references\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计页数\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `projects/policy_ambiguity_safety/artifacts/review_round_23/submitted.pdf`\n\n### 你的审查侧重：新颖性/完整性\n\n请重点审查以下方面：\n\n1. **贡献新颖性**: 与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026)、MANTRA (2026) 等并发工作的区分度；matched-pair causal design 是否构成足够的方法论创新\n2. **Related work 覆盖**: 是否遗漏重要相关工作（特别是 2025-2026 agent safety / policy specification / ambiguity 方向的新工作）\n3. **Taxonomy 设计**: 6 type × 2 layer 的选择依据是否充分、type 选择标准（attestation + minimal-pair + mutual exclusivity）是否令人信服\n4. **Claim 校准**: 论文 claim 是否与证据强度匹配——特别是：\n   - \"34.0pp\" headline 是否充分注明 synthetic conditions + incompleteness confound\n   - \"order of magnitude\" (NMI 0.23 vs 0.01) 的表述是否过强\n   - partial ordering 的 claim 是否受 ρ=0.09 cross-judge ranking 影响\n5. **写作质量**: 叙事流畅度、信息密度、abstract 是否过载、conclusion 是否充分\n6. **格式合规**: 页数是否超限、匿名是否合规、Limitations 章节是否符合要求、参考文献格式\n7. **论文完整性**: 数据可用性声明、伦理考量（如需）、reproducibility 信息\n8. **Ecological validity**: synthetic ambiguity vs real-world policy ambiguity 的 gap 是否被充分 acknowledged\n\n### 输出格式\n请按以下结构输出审稿意见：\n- **Summary** (2-3 句)\n- **Strengths** (逐条，S1, S2, ...)\n- **Weaknesses** (逐条，W1, W2, ...，标注 severity: critical/major/minor)\n- **Questions** (Q1, Q2, ...)\n- **Missing References** (如有)\n- **Overall Assessment** (评分 + 置信度)\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, Long paper 正文 8 页 + unlimited references\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计页数\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `projects/policy_ambiguity_safety/artifacts/review_round_23/submitted.pdf`\n\n### 你的审查侧重：新颖性/完整性\n\n请重点审查以下方面：\n\n1. **贡献新颖性**: 与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026)、MANTRA (2026) 等并发工作的区分度；matched-pair causal design 是否构成足够的方法论创新\n2. **Related work 覆盖**: 是否遗漏重要相关工作（特别是 2025-2026 agent safety / policy specification / ambiguity 方向的新工作）\n3. **Taxonomy 设计**: 6 type × 2 layer 的选择依据是否充分、type 选择标准（attestation + minimal-pair + mutual exclusivity）是否令人信服\n4. **Claim 校准**: 论文 claim 是否与证据强度匹配——特别是：\n   - \"34.0pp\" headline 是否充分注明 synthetic conditions + incompleteness confound\n   - \"order of magnitude\" (NMI 0.23 vs 0.01) 的表述是否过强\n   - partial ordering 的 claim 是否受 ρ=0.09 cross-judge ranking 影响\n5. **写作质量**: 叙事流畅度、信息密度、abstract 是否过载、conclusion 是否充分\n6. **格式合规**: 页数是否超限、匿名是否合规、Limitations 章节是否符合要求、参考文献格式\n7. **论文完整性**: 数据可用性声明、伦理考量（如需）、reproducibility 信息\n8. **Ecological validity**: synthetic ambiguity vs real-world policy ambiguity 的 gap 是否被充分 acknowledged\n\n### 输出格式\n请按以下结构输出审稿意见：\n- **Summary** (2-3 句)\n- **Strengths** (逐条，S1, S2, ...)\n- **Weaknesses** (逐条，W1, W2, ...，标注 severity: critical/major/minor)\n- **Questions** (Q1, Q2, ...)\n- **Missing References** (如有)\n- **Overall Assessment** (评分 + 置信度)\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
  }
}
```

</details>

---


### Tool result

_source line 2030 · 2026-05-23T05:19:04.258211+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1664
}
```

</details>

---


### Assistant

_source line 2031 · 2026-05-23T05:19:10.563355+00:00_

已并行派发：
- **视觉审查 Agent**：已启动（fire-and-forget）
- **Reviewer 1**（方法严谨性）：已分配
- **Reviewer 2**（新颖性/完整性）：已分配

等待两位 Reviewer 返回 Round 1 独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 189

## Round 189

2 recorded events


### User

_source line 2032 · 2026-05-23T05:25:43.486952+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见（新颖性/完整性）

### Summary

本文在 τ²-bench 上构建 300 对 matched-pair 歧义/无歧义策略条款，通过六类型×两层分类体系评估五个模型，证明歧义条款在合成条件下使安全违规率增加 34.0 pp（排除 incompleteness confound 后为 18.7 pp），并发现条款措辞解释 22.4% 方差，而歧义类型仅解释 0.4%——但类型对失败机制的预测能力（NMI = 0.23）远强于对违规率的预测（NMI = 0.01）。这是一项方法论扎实的因果研究，matched-pair 设计在 agent safety 领域有新颖性，但生态效度和格式合规存在问题。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Matched-pair 因果设计严谨，统计方法恰当（TOST, Type III ANOVA, ICC, bootstrap clustering），但 incompleteness confound 削弱 headline claim，cross-judge ρ=0.09 质疑 type ranking 稳健性 |
| Excitement | 3.5/5 | 研究问题重要且 timely，matched-pair causal design 在 agent safety 领域是首次，但结论受限于合成歧义，实际部署指导价值有限 |
| Reproducibility | 4/5 | 数据和代码宣称将公开（Data and Code Availability, p10），实验设置详细（§4.1-4.4），参数完整（temperature=0, top_p=1, max_tokens=4096），统计检验充分报告 |
| Datasets | 3/5 | 300 matched clause pairs 有一定价值，但基于模板合成（§4.2），局限于 τ²-bench 两个 customer-service 场景（retail + airline），覆盖面较窄 |
| Software | N/A | 代码尚未发布 |
| Reviewer Confidence | 4/5 | 熟悉 agent safety evaluation 和 NLP 歧义研究，对因果推断方法论有较好把握 |

---

## Overall Assessment

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 方法论贡献扎实（matched-pair causal design 是首次用于 agent safety），但合成歧义的生态效度限制、incompleteness confound、以及正文超 8 页格式违规是影响接收的主要障碍。

---

## Strengths

**S1.** Matched-pair causal design 是本文最核心的方法论贡献。与 DRIP-R（观察性设计，使用真实歧义场景但无法隔离因果效应）和 MANTRA（SMT 形式化验证但不涉及歧义）相比，本文的 minimal-edit 配对设计能够在 clause level 建立歧义→违规的因果联系。这在 agent safety evaluation 中是首次，也是与并发工作的主要区分点（§2, Appendix L）。

**S2.** Variance decomposition 发现具有实用价值：条款措辞解释 22.4% 方差 vs 类型仅 0.4%（§5.1, Figure 2），这意味着 intervention 应针对具体条款措辞而非歧义类别。Type-mechanism mapping（§6.1, Figure 5）进一步将诊断建议落地到具体的 failure mode。

**S3.** 统计方法选择审慎。对 binary outcome 使用 McNemar's test，对 paired comparison 使用 TOST equivalence testing（Lakens, 2017），对 within-judge range 使用 Holm-Bonferroni correction，对 type ranking 使用 bootstrap 10,000 次重采样。ICC 用于跨模型一致性评估（ICC(3,1) = 0.74, p20）。这些选择均恰当。

**S4.** 多模型 + 跨架构评估增强 generalizability：主实验 5 个模型（GPT-3.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3），附录 E 追加 Gemini 2.5 Flash 和 LLaMA-4 Scout 两个 replication family。C1 binary effect 跨 7 个模型一致显著（Appendix E, Tables 7-8）。

**S5.** Error analysis 章节（§6）提供了超出纯 measurement 的洞察。Disambiguation neglect（§6.2）发现 overall awareness 仅 4.6%，且 Qwen3 和 DeepSeek 在全部 278 combined traces 中 awareness 为零——这对 agent deployment 设计有实际意义。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 正文超 8 页限制

- 具体位置：Page 9
- 问题：EMNLP 2026 long paper 正文严格限 8 页。当前 Discussion（§7）从 p8 延伸到 p9，Conclusion（§8）也在 p9 上半部分。Limitations 从 p9 中部开始。即使 Limitations 不计页数，正文（Abstract 到 Conclusion）仍约 8.4-8.5 页，超出限制。
- 为什么影响接收：这是 hard format constraint，可能导致 desk rejection。
- 建议修改方向：压缩 Discussion 或将部分内容移至 Appendix（例如 "Taxonomy as a diagnostic tool" 段落与 §6.1 有重叠）；Analysis（§6）也可考虑精简。

**N2** [critical] Incompleteness confound 在 headline claim 中不够显著

- 具体位置：Abstract line 4-5; §1 para 3; §5.1
- 问题：Abstract 说 "ambiguous clauses increase agent violations by 34.0 pp (+18.7 to +36.0 pp excluding the confounded incompleteness type)"——这个 caveat 放在括号里，且 "34.0 pp" 是读者首先看到的数字。但如 §6.3 所述，incompleteness 在结构上与其他五类不同（添加信息而非消解歧义）。Appendix F 的 confound-free analysis 显示排除 incompleteness 后效应范围是 18.7-36.0 pp，中位值远低于 34.0 pp。
- 为什么影响接收：如果 headline number 的很大一部分来自一个结构上有 confound 的类型，这削弱了论文的核心 claim 的可信度。审稿人会质疑真实的 "pure ambiguity" effect 到底有多大。
- 建议修改方向：(1) 在 abstract 中将 confound-free range（18.7-36.0 pp）作为主要数字，34.0 pp 作为包含全部类型的上界；或 (2) 在 abstract 中明确 "under synthetic conditions including an information-addition confound"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Cross-judge type ranking ρ = 0.09 削弱 C2 (Partial Ordering) claim

- 具体位置：§5.2, Appendix P
- 问题：C2 声称存在 "graded equivalence structure among five types"（§5.2），但跨 judge Spearman ρ = 0.09（p = 0.87, Appendix P）表明不同 judge 对类型排名几乎无一致性。论文将此归因于 authorization scope 的 rank reversal（GPT-4.1 rank 1 vs GPT-3.4 rank 6），但这恰恰说明 type ordering 高度依赖 judge identity，不是一个稳健的 finding。
- 建议：(1) 降低 C2 claim 的强度——从 "partial ordering" 改为 "model-dependent vulnerability profiles"；(2) 或移除 C2 作为独立 contribution，将其纳入 exploratory analysis。

**W2** [major] 合成歧义的生态效度（Ecological Validity）

- 具体位置：§4.2, Limitations (p9)
- 问题：所有 300 clause pairs 均通过模板合成（§4.2），由两位 annotators 生成后经 NLP 背景的第三人验证。SOPBench replication（Appendix V, +12.6 pp）提供了部分生态效度支持，但其评估方式不同（benchmark-specific assertion structure vs clause-level text changes），且 SOPBench 本身也是合成 benchmark。论文未提供任何来自真实企业策略文档的歧义案例。
- 建议：(1) 在 Discussion 中更明确地讨论 synthetic → real-world gap 的具体 threats（例如：真实歧义的上下文依赖性更强，可能被其他条款部分消解）；(2) 如有可能，补充少量真实策略文档中提取的歧义案例作为 case study。

**W3** [minor-major] NMI 0.23 vs 0.01 的 "order of magnitude" 表述

- 具体位置：§5.2 第2段, §8 Conclusion
- 问题：NMI 0.23 vs 0.01 确实是 "an order of magnitude" 的差异（数值上约 23 倍），但 NMI = 0.23 在绝对值上仍然是弱关联。论文用 "an order of magnitude better" 的措辞暗示了强预测力，但实际上这意味着 type 只解释了 mechanism 变异的约 23%。
- 建议：加上对 NMI 绝对值的解读——例如 "moderate association (NMI = 0.23)" vs "near-zero (NMI = 0.01)"，避免单纯依赖相对比较。

**W4** [minor] Abstract 信息过载

- 具体位置：Abstract
- 问题：Abstract 在约 150 词内包含 6+ 个定量结果（34.0 pp, 18.7, 22.4%, 0.4%, NMI 0.23 vs 0.01, 40%+），对初次阅读者认知负担过重。
- 建议：保留 2-3 个核心数字（binary effect, variance decomposition, type-mechanism NMI），其余放入 Introduction。

**W5** [minor] Disambiguation neglect 分析的推断边界

- 具体位置：§6.2
- 问题：§6.2 声称 agents "rarely recognize ambiguity"（overall awareness 4.6%），但测量方式是检查模型是否在推理中显式提及歧义。这混淆了两个不同的能力：(1) 能否检测到歧义（internal representation）；(2) 是否会在输出中显式标注歧义（surface behavior）。模型可能内部检测到歧义但选择默认解读而不显式标注。
- 建议：将 claim 从 "agents rarely recognize ambiguity" 修改为 "agents rarely surface ambiguity in their reasoning traces"，并讨论 internal detection 的可能性。

---

## 小问题（不影响接收）

- **M1**: Table 2 的 "Overall" 行汇总了所有类型包括 incompleteness——鉴于其 confound 状态，建议增加一行 "Overall (excl. Incomp.)" 或用脚注标注。
- **M2**: Figure 2 的 y 轴标签 "Proportion of variance (%)" 和柱形标注（如 "22.4%"）同时存在，略有冗余但不影响理解。
- **M3**: §4.3 提到 "five architecturally diverse models" 但其中 GPT-3.4 和 GPT-4.1 同属 OpenAI GPT 系列，"architecturally diverse" 的说法可稍微调整。
- **M4**: References 格式：部分 arXiv 引用缺少 submission date 或写法不统一（如有些有 "Submitted 2026-xx-xx" 有些没有）。

---

## Questions

**Q1**: 歧义条款注入点的选择标准是什么？§4.2 说 "we replace individual policy clauses"，但未说明如何选择 which clause to modify。注入位置是否会引入系统性偏差（例如：更早出现的条款 vs 后面的条款对模型行为影响不同）？

**Q2**: Human validation（§4.6）提到 inter-annotator agreement κ = 0.72，这是 Cohen's κ 还是 Fleiss's κ？对于 100 个 stratified episodes 的标注规模，请确认。

**Q3**: Incompleteness 在结构上与其他五类不同（§6.3），且 detection 最难（F1 = 0.34, Table 6）。是否考虑过将其从 taxonomy 中独立出来，作为单独的分析维度而非 six types 之一？这样可以消除 confound 问题，同时保留其作为重要现象的讨论。

**Q4**: Mitigation experiment（Appendix B, Table 4）中 type-specific disambiguation instructions 的效果差异很大（auth_scope −20.0 pp vs coreferential −2.0 pp）。这些 instructions 是如何生成的？instruction quality 本身是否是一个 confound？

**Q5**: Cross-domain analysis（Appendix U）提到 retail 和 airline 两个领域结果一致，但 τ²-bench 是否只有这两个领域？如果是，generalizability 到其他领域（如 healthcare, finance）仍然是开放问题。

---

## Missing References

1. **ATBench** (Li et al., 2026, arXiv:2604.02022)：trajectory-level agent safety benchmark，与本文的 trace-level 分析方法相关。
2. **Enhancing LLM Agent Safety via Causal Influence Prompting** (2026, arXiv:2507.00979)：使用 causal influence diagrams 增强 agent safety，与本文的因果方法论框架直接相关。
3. 本文的 Related Work 整体覆盖较好，已引用 DRIP-R、PolicyBank、MANTRA、OpenAgentSafety、SOPBench 等主要并发工作。Appendix L 的 DRIP-R 对比分析较为充分。

---

## 主要优势总结

- Matched-pair causal design 在 agent safety evaluation 中是首次，方法论贡献明确
- Variance decomposition（clause wording 22.4% vs type 0.4%）是 novel finding，对 intervention design 有实际指导意义
- 统计方法选择审慎（TOST, Type III ANOVA, ICC, bootstrap），报告充分
- 多模型 + replication families 增强 generalizability
- Error analysis（§6）超越纯 measurement，提供可操作的诊断框架
- 与并发工作的区分清晰（Appendix L）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2033 · 2026-05-23T05:25:50.611340+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 的审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 190

## Round 190

2 recorded events


### User

_source line 2034 · 2026-05-23T05:26:03.723900+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成，已提交至 Review Director。

核心判断：**Overall 3.5（Borderline Conference）**。

主要发现：
- **2 个 critical 问题**：正文超 8 页格式违规（Discussion+Conclusion 溢出到 p9）；incompleteness confound 在 headline claim "34.0 pp" 中未获足够显著标注（confound-free range 仅 18.7-36.0 pp）
- **5 个 should-fix 问题**：cross-judge ρ=0.09 削弱 type ordering claim；合成歧义生态效度不足；NMI "order of magnitude" 表述需绝对值语境化；abstract 信息过载；disambiguation neglect 的推断边界需收窄
- **主要优势**：matched-pair causal design 首次用于 agent safety（方法论新颖）；variance decomposition 发现（22.4% vs 0.4%）有实际指导意义；统计方法审慎；多模型+replication 增强泛化性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2035 · 2026-05-23T05:26:07.987784+00:00_

Reviewer 2 的意见已收到。等待 Reviewer 1 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 191

## Round 191

6 recorded events


### User

_source line 2036 · 2026-05-23T05:27:23.767969+00:00_

[Reviewer 1 审稿意见]:
## Round 1 审稿意见 — Reviewer 1（方法严谨性）

---

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: C1（二值歧义效应 +34.0 pp）方法论扎实、多重鲁棒性检验充分，可达 Conference 水平；但类型层面分析（C2–C4）受限于 authorization scope 的低可靠性（κ=0.385, ICC≈0）和跨 judge 类型排名近零相关（ρ=0.09），需要更谨慎的 claim 限定。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | C1 证据充分（McNemar、perturbation control、跨模型/跨基准复制）；C2 类型层面 claims 受 auth scope 可靠性和 TOST 边界选择影响；variance decomposition 仅限 OpenAI family |
| Excitement | 3.5/5 | 研究问题时新且重要（policy ambiguity → agent safety 的因果路径）；matched-pair 设计在该领域属首创；但局限于合成 benchmark，实际部署影响待验证 |
| Reproducibility | 4/5 | ICC=0.919、完整方法描述、跨基准复制（SOPBench）、跨架构复制（Gemini/LLaMA）；但 ICC 仅覆盖 OpenAI family |
| Confidence | 4/5 | 方法论审查在本人专业范围内；统计方法选择、实验设计、confound 处理均做了详细核查 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Authorization scope 类型的系统性不可靠，动摇 C2 和 C4 claims

- 具体位置：§4.4 cross-judge calibration; §5.2 C2; §5 C4 exploratory; Appendix P; Appendix X (per-type ICC)
- 问题：Authorization scope 在多个独立维度上表现出异常低的可靠性：
  - 跨 judge 二值一致性 κ=0.385（仅 fair agreement，其他类型 0.636–0.875）
  - Per-type ICC ≈ 0（Appendix X），意味着同一 clause×model cell 的结果本质上是随机的
  - 单独驱动跨 judge 组类型排名从 ρ=0.09 到排除后的 ρ=0.90（§5.2）
  - 单独驱动 C4 model×type interaction（排除后 p=0.97，Appendix N）
  - 跨模型方差 52 pp（12%–64%），远超其他类型
- 然而，论文在 Table 2 和主分析中对 authorization scope 的结果报告并无显著区分标记（仅在 Figure 3 caption 中提及 "interpret with caution"），在 C2 type partial ordering 讨论中仍将其归入 mid-tier cluster。
- 为什么影响接收：一个在多个可靠性指标上接近噪声的类型不应与高可靠类型等同处理。当前 framing 使读者可能将 auth scope 的类型排名视为与其他类型同等可信。
- 建议修改方向：(1) 在 Table 2 中对 auth scope 增加显著警告标注（不仅在 footnote）；(2) 在 C2 讨论中将 auth scope 明确标记为 "unreliable"，所有涉及 auth scope 的类型层面分析结果加 caveat；(3) 考虑在 sensitivity analysis 中系统性地报告 excluding auth scope 后的所有 C2 结论。

**N2** [critical] Residual variance decomposition（15% stochastic + 46% systematic）仅基于 OpenAI family，泛化性存疑

- 具体位置：§5.1 variance decomposition; Appendix X; §7 Discussion "Differential nocuity" paragraph; Limitations "Scope" paragraph
- 问题：60.8% residual 的内部分解（ICC(1)=0.749）基于 200 clause×model cells 的 5 次重复实验，但所有 cells 均来自 OpenAI 模型（GPT-5.4 judged by GPT-4.1）。不同训练范式（如 MoE vs. dense、open-source vs. proprietary）的 stochastic/systematic 比例可能显著不同。论文在 Limitations 中确实承认 "should not be assumed to generalize across provider architectures"，但在 §5.1 和 §7 的主文中，这一分解被作为核心分析结论呈现，而非附带 OpenAI-specific 的限定。
- 为什么影响接收：variance decomposition 是论文四个核心分析之一。如果 systematic residual 比例在非 OpenAI 模型上显著不同（例如 DeepSeek-V3 的 per-type ICC 结构可能完全不同），"~46% systematic-but-unmeasured" 的结论就不具备论文所暗示的普遍性。
- 建议修改方向：(1) 在 §5.1 主文中每次引用 residual 分解时都注明 "OpenAI-family estimate"；(2) 至少提供一个跨 provider ICC 的 proxy 度量（如 Claude 和 DeepSeek 的 between-run variance）；(3) 或将 Discussion 中的 "conversation trajectory" 等候选解释明确标注为 "hypotheses motivated by OpenAI-family data"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] TOST equivalence bound ±15pp 的 justification 不够严谨

- 具体位置：§4.6 Statistical Analysis; Appendix A (Table 3)
- 问题：±15pp SESOI 基于两个标准：(1) 超过 perturbation control CI 上界 6.67pp 的 2 倍以上；(2) 低于此 margin 的差异不值得区分 mitigation 策略。标准 (2) 本质上是一个 unfalsifiable 的主观判断。Sensitivity analysis（Table 3）显示，在 ±10pp 时仅 3/15 pairs 等价（mid-tier 仅 3/6），这意味着 ±15pp 的选择对 C2 cluster structure 结论有实质影响。论文将此呈现为 "satisfies two principled criteria (Lakens, 2017)"，但 Lakens (2017) 提供的是选择 SESOI 的框架，而非对 ±15pp 的背书。
- 建议：(1) 明确承认 ±15pp 是 pragmatic/conservative 选择而非 objectively principled；(2) 在 Table 3 sensitivity analysis 中增加讨论不同 margins 对结论的影响；(3) 考虑以 bootstrap clustering（margin-free）作为 C2 的主要证据。

**W2** [major] 跨 judge 组类型排名 ρ=0.09 的处理方式有 post-hoc 嫌疑

- 具体位置：§5.2 第 4 段; Appendix P
- 问题：论文报告跨 judge 组类型排名 ρ=0.09（p=0.87），然后通过排除 auth scope 获得 ρ=0.90（p=0.037），并以 three-family validation（ρ=0.71–0.89）佐证。虽然 auth scope 排除有独立理由（低 κ、高 variance），但在 6 个类型中排除 1 个后达到显著性，这一操作具有 post-hoc 特征。三家 judge validation 是更强的证据，但主文中 ρ=0.09 → "excluding it, ρ=0.90" 的叙述结构暗示了结论驱动的分析。
- 建议：(1) 将 three-family validation 结果提升到主文（目前仅在 Appendix W）作为 primary evidence；(2) 将排除 auth scope 的分析明确标记为 sensitivity check 而非主结论。

**W3** [major] Cross-judge calibration 样本量不足以支撑 per-type κ 估计

- 具体位置：§4.4; Appendix G (Table 9)
- 问题：Cross-judge calibration 在 100 个 episode 上进行（65% ambiguous），分到 6 个类型后每类仅约 17 个 episodes。Per-type κ 的置信区间未报告（相比之下，human-LLM agreement 的 Appendix G 报告了 bootstrap 95% CI）。κ=0.385 for auth scope 可能有极宽的 CI，使该估计的信息量有限。
- 建议：(1) 补充 per-type cross-judge κ 的 bootstrap CI；(2) 在主文中对 per-type κ 的 precision 加警告。

**W4** [minor] Token count 作为 incompleteness confound control 的粗糙性

- 具体位置：Appendix F; Appendix H
- 问题：Token count logistic regression 显示 OR=1.022/token（p=0.003），controlling 后 incompleteness 效应几乎不变（±0.1pp）。但 token count 是信息量的粗糙 proxy——同等长度的文本可能承载截然不同的信息密度。论文承认 "Token count is a coarse proxy for information content"，但未提供替代度量。Auth scope 的 token delta（+36.1 words）大于 incompleteness（+34.6 words），却有更低的违规率，这是有力的反证据，但仅作为附带观察而非系统性分析。
- 建议：补充至少一种 semantic-level 的信息量度量（如 sentence embedding similarity、information-theoretic measures）。

**W5** [minor] 主文可能超过 8 页限制

- 具体位置：Pages 8–9
- 问题：Section 7 Discussion 从 page 8 延伸到 page 9，Section 8 Conclusion 也在 page 9 上，然后才是 Limitations。按照 EMNLP 2026 的严格 8 页正文限制（Limitations 和 ethical considerations 不计入），numbered sections 1–8 似乎占据了约 8.3–8.5 页。
- 建议：压缩 Discussion（3 个 paragraph 可精简为 2 个）或将部分 Analysis 内容移入 Appendix。

---

## Questions（提给作者）

**Q1**: Perturbation control 的 CI 为 [-8.0, 6.67] pp（宽度 ~14.67 pp）。该 control 对 5pp 或 10pp 的 true perturbation effect 的统计功效（power）是多少？如果 power 较低，perturbation control 可能给出了虚假的安全感。

**Q2**: Type III SS variance decomposition 的完整模型公式是什么？是否包含 random effects？论文提到 condition×type interaction（4.1%），但完整的 model specification 未呈现。

**Q3**: Cross-judge calibration 中 per-type κ（特别是 auth scope 的 κ=0.385）的 bootstrap 95% CI 是多少？

**Q4**: ICC=0.919 仅基于 OpenAI family。是否计算过跨 provider 的 reproducibility 度量（如 GPT-5.4 vs Claude 对同一 clause 的结果一致性）？

**Q5**: Coreferential 作为 "confound-free lower bound" 的论证依赖于 "lexically identical variants"（information delta = 0）。但如果歧义解消完全依赖上下文信息，如何确保上下文本身不引入信息不对称？

**Q6**: NMI=0.23（type→mechanism）vs NMI=0.01（type→violation）——在 failure mechanism 分布高度不均衡的情况下（Table 14 confusion matrix 显示 structural misparse 和 gap-filling 占绝大多数），NMI 是否是合适的度量？

**Q7**: Bootstrap clustering 的 modal partition 仅在 34.3% 的 bootstrap 样本中出现（Appendix I），AU p-value=0.47。论文描述此为 "consistent with TOST"，但 34.3% 的频率和 AU=0.47 表明 cluster boundary 非常模糊。能否提供更高 k 值（如 k=4, 5）的 partition stability？

---

## Missing References

无关键缺失引用。建议考虑：
- Zheng et al. (2024) "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" 已引用（zheng_llm_judge_2024），但可补充 Ye et al. (2024) "FLASK: Fine-grained Language Model Evaluation" 作为 LLM-as-judge 方法论的对比。

---

## 主要优势

**S1**: **Matched-pair 因果设计严谨**。300 clause pairs 的配对设计有效控制 clause-level confounds。perturbation control（n=300, Δ=-0.67pp, CI containing zero）确认了对语义歧义的特异性。Holm-Bonferroni 在三个预注册测试族内的校正处理多重比较。

**S2**: **统计方法选择得当且全面**。McNemar's test（配对二值数据）、Fisher's exact（per-type 比较）、TOST equivalence（类型等价结构）、Type III SS（方差分解）、ICC（可重复性）、bootstrap clustering（无阈值聚类）——每种方法都适合对应分析。

**S3**: **多层次复制**。ICC=0.919 within OpenAI family；SOPBench 跨基准复制（+12.6pp directional consistency）；Gemini/LLaMA 跨架构复制（7 models, 6 providers）；cross-domain 一致性（retail vs airline, interaction p=0.19）。

**S4**: **Confound 处理多角度**。Incompleteness confound 通过 token count regression、exclusion analysis（confound-free range +18.7–+36.0pp）、coreferential 作为 information-delta=0 的 lower bound 三个独立角度控制。尽管 token count 是粗糙 proxy，多重证据链增强可信度。

**S5**: **高度透明的 limitation disclosure**。论文主动披露 ρ=0.09 cross-judge concordance、auth scope 的低 κ、OpenAI-only ICC decomposition、合成 benchmark 的生态效度局限——这种透明度在同行评审中值得肯定。

**S6**: **C1 core finding 非常稳健**。+34.0pp 效应跨 5 模型（main study）+ 2 模型（replication）+ SOPBench 均一致。排除 incompleteness 后仍有 +31.0pp（p < 10⁻⁷⁵）。排除任何单一类型均不影响 C1。Severity threshold robustness（moderate+ vs any-violation）确认方向一致。

---

## 格式与合规

- **Anonymity**: 符合 double-blind 要求（Anonymous ACL submission）
- **Limitations section**: 有，位于正文（非 appendix），覆盖 5 个方面，符合 EMNLP 2026 要求
- **页数**: 主文（Sections 1–8）疑似约 8.3–8.5 页，可能违反严格 8 页限制（见 W5）
- **References**: 格式一致，使用 acl_natbib.bst

---

## 总结

本文在因果设计和 C1 核心发现上方法论质量很高，perturbation control、多重复制和透明 limitation disclosure 令人印象深刻。主要顾虑集中在类型层面分析（C2–C4）：authorization scope 在 κ、ICC、cross-judge ranking 三个维度上均表现不可靠，却在主分析中未被充分区分；residual variance decomposition 仅基于 OpenAI family 但在主文中作为普遍结论呈现；TOST bounds 的选择对 cluster structure 结论有实质影响。如果 N1–N2 能妥善解决（主要是更准确的 claim qualification 而非新实验），论文可达 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2037 · 2026-05-23T05:28:16.802367+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每一条 Strength、Must-Fix、Should-Fix、Minor 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿意见（新颖性/完整性）\n\n### Summary\n\n本文在 τ²-bench 上构建 300 对 matched-pair 歧义/无歧义策略条款，通过六类型×两层分类体系评估五个模型，证明歧义条款在合成条件下使安全违规率增加 34.0 pp（排除 incompleteness confound 后为 18.7 pp），并发现条款措辞解释 22.4% 方差，而歧义类型仅解释 0.4%——但类型对失败机制的预测能力（NMI = 0.23）远强于对违规率的预测（NMI = 0.01）。这是一项方法论扎实的因果研究，matched-pair 设计在 agent safety 领域有新颖性，但生态效度和格式合规存在问题。\n\n### Overall Assessment\n**Overall**: 3.5 — Borderline Conference\n\n---\n\n### Strengths\n\n**S1.** Matched-pair causal design 是本文最核心的方法论贡献。与 DRIP-R（观察性设计）和 MANTRA（SMT 形式化验证但不涉及歧义）相比，本文的 minimal-edit 配对设计能够在 clause level 建立歧义→违规的因果联系。\n\n**S2.** Variance decomposition 发现具有实用价值：条款措辞解释 22.4% 方差 vs 类型仅 0.4%（§5.1, Figure 2），对 intervention design 有实际指导意义。Type-mechanism mapping（§6.1, Figure 5）进一步将诊断建议落地。\n\n**S3.** 统计方法选择审慎。McNemar's test、TOST equivalence testing（Lakens, 2017）、Holm-Bonferroni correction、bootstrap 10,000 次重采样、ICC 均恰当。\n\n**S4.** 多模型 + 跨架构评估增强 generalizability：主实验 5 个模型，附录 E 追加 Gemini 2.5 Flash 和 LLaMA-4 Scout。C1 跨 7 个模型一致显著。\n\n**S5.** Error analysis 章节（§6）提供超出纯 measurement 的洞察。Disambiguation neglect（§6.2）发现 overall awareness 仅 4.6%。\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] 正文超 8 页限制\n- Discussion（§7）从 p8 延伸到 p9，Conclusion（§8）也在 p9。正文（Abstract 到 Conclusion）约 8.4-8.5 页，超出限制。可能导致 desk rejection。\n\n**N2** [critical] Incompleteness confound 在 headline claim 中不够显著\n- Abstract 说 \"34.0 pp (+18.7 to +36.0 pp excluding the confounded incompleteness type)\"——caveat 放在括号里。Confound-free range 中位值远低于 34.0 pp。建议将 confound-free range 作为主要数字。\n\n---\n\n### Should-Fix 问题\n\n**W1** [major] Cross-judge type ranking ρ = 0.09 削弱 C2 claim\n- 跨 judge Spearman ρ = 0.09（p = 0.87）。排除 auth scope 后 ρ=0.90 具 post-hoc 特征。\n\n**W2** [major] 合成歧义的生态效度\n- 所有 300 clause pairs 均通过模板合成。SOPBench 也是合成 benchmark。未提供真实企业策略文档的歧义案例。\n\n**W3** [minor-major] NMI 0.23 vs 0.01 的 \"order of magnitude\" 表述\n- NMI = 0.23 绝对值仍是弱关联。建议加绝对值解读。\n\n**W4** [minor] Abstract 信息过载\n- 约 150 词内包含 6+ 个定量结果。建议保留 2-3 个核心数字。\n\n**W5** [minor] Disambiguation neglect 的推断边界\n- 混淆 internal detection 和 surface behavior。建议修改为 \"agents rarely surface ambiguity in their reasoning traces\"。\n\n---\n\n### 小问题\n- **M1**: Table 2 \"Overall\" 行建议增加 \"Overall (excl. Incomp.)\" 或用脚注标注。\n- **M2**: Figure 2 y轴标签和柱形标注略有冗余。\n- **M3**: §4.3 \"five architecturally diverse models\" 的说法可稍调整（GPT-5.4 和 GPT-4.1 同属 OpenAI）。\n- **M4**: References 格式部分 arXiv 引用写法不统一。\n\n---\n\n### Questions\n**Q1**: 歧义条款注入点的选择标准是什么？注入位置是否会引入系统性偏差？\n**Q2**: Human validation（§4.6）的 inter-annotator agreement κ = 0.72 是 Cohen's κ 还是 Fleiss's κ？\n**Q3**: 是否考虑过将 incompleteness 从 taxonomy 中独立出来？\n**Q4**: Mitigation experiment 的 instruction quality 本身是否是 confound？\n**Q5**: τ²-bench 是否只有 retail 和 airline 两个领域？\n\n---\n\n### Missing References\n1. ATBench (Li et al., 2026)\n2. Enhancing LLM Agent Safety via Causal Influence Prompting (2026)\n\n---\n\n请对以上每一条逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每一条 Strength、Must-Fix、Should-Fix、Minor 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿意见（新颖性/完整性）\n\n### Summary\n\n本文在 τ²-bench 上构建 300 对 matched-pair 歧义/无歧义策略条款，通过六类型×两层分类体系评估五个模型，证明歧义条款在合成条件下使安全违规率增加 34.0 pp（排除 incompleteness confound 后为 18.7 pp），并发现条款措辞解释 22.4% 方差，而歧义类型仅解释 0.4%——但类型对失败机制的预测能力（NMI = 0.23）远强于对违规率的预测（NMI = 0.01）。这是一项方法论扎实的因果研究，matched-pair 设计在 agent safety 领域有新颖性，但生态效度和格式合规存在问题。\n\n### Overall Assessment\n**Overall**: 3.5 — Borderline Conference\n\n---\n\n### Strengths\n\n**S1.** Matched-pair causal design 是本文最核心的方法论贡献。与 DRIP-R（观察性设计）和 MANTRA（SMT 形式化验证但不涉及歧义）相比，本文的 minimal-edit 配对设计能够在 clause level 建立歧义→违规的因果联系。\n\n**S2.** Variance decomposition 发现具有实用价值：条款措辞解释 22.4% 方差 vs 类型仅 0.4%（§5.1, Figure 2），对 intervention design 有实际指导意义。Type-mechanism mapping（§6.1, Figure 5）进一步将诊断建议落地。\n\n**S3.** 统计方法选择审慎。McNemar's test、TOST equivalence testing（Lakens, 2017）、Holm-Bonferroni correction、bootstrap 10,000 次重采样、ICC 均恰当。\n\n**S4.** 多模型 + 跨架构评估增强 generalizability：主实验 5 个模型，附录 E 追加 Gemini 2.5 Flash 和 LLaMA-4 Scout。C1 跨 7 个模型一致显著。\n\n**S5.** Error analysis 章节（§6）提供超出纯 measurement 的洞察。Disambiguation neglect（§6.2）发现 overall awareness 仅 4.6%。\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] 正文超 8 页限制\n- Discussion（§7）从 p8 延伸到 p9，Conclusion（§8）也在 p9。正文（Abstract 到 Conclusion）约 8.4-8.5 页，超出限制。可能导致 desk rejection。\n\n**N2** [critical] Incompleteness confound 在 headline claim 中不够显著\n- Abstract 说 \"34.0 pp (+18.7 to +36.0 pp excluding the confounded incompleteness type)\"——caveat 放在括号里。Confound-free range 中位值远低于 34.0 pp。建议将 confound-free range 作为主要数字。\n\n---\n\n### Should-Fix 问题\n\n**W1** [major] Cross-judge type ranking ρ = 0.09 削弱 C2 claim\n- 跨 judge Spearman ρ = 0.09（p = 0.87）。排除 auth scope 后 ρ=0.90 具 post-hoc 特征。\n\n**W2** [major] 合成歧义的生态效度\n- 所有 300 clause pairs 均通过模板合成。SOPBench 也是合成 benchmark。未提供真实企业策略文档的歧义案例。\n\n**W3** [minor-major] NMI 0.23 vs 0.01 的 \"order of magnitude\" 表述\n- NMI = 0.23 绝对值仍是弱关联。建议加绝对值解读。\n\n**W4** [minor] Abstract 信息过载\n- 约 150 词内包含 6+ 个定量结果。建议保留 2-3 个核心数字。\n\n**W5** [minor] Disambiguation neglect 的推断边界\n- 混淆 internal detection 和 surface behavior。建议修改为 \"agents rarely surface ambiguity in their reasoning traces\"。\n\n---\n\n### 小问题\n- **M1**: Table 2 \"Overall\" 行建议增加 \"Overall (excl. Incomp.)\" 或用脚注标注。\n- **M2**: Figure 2 y轴标签和柱形标注略有冗余。\n- **M3**: §4.3 \"five architecturally diverse models\" 的说法可稍调整（GPT-5.4 和 GPT-4.1 同属 OpenAI）。\n- **M4**: References 格式部分 arXiv 引用写法不统一。\n\n---\n\n### Questions\n**Q1**: 歧义条款注入点的选择标准是什么？注入位置是否会引入系统性偏差？\n**Q2**: Human validation（§4.6）的 inter-annotator agreement κ = 0.72 是 Cohen's κ 还是 Fleiss's κ？\n**Q3**: 是否考虑过将 incompleteness 从 taxonomy 中独立出来？\n**Q4**: Mitigation experiment 的 instruction quality 本身是否是 confound？\n**Q5**: τ²-bench 是否只有 retail 和 airline 两个领域？\n\n---\n\n### Missing References\n1. ATBench (Li et al., 2026)\n2. Enhancing LLM Agent Safety via Causal Influence Prompting (2026)\n\n---\n\n请对以上每一条逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2038 · 2026-05-23T05:28:49.527348+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 32724
}
```

</details>

---


### Tool call

_source line 2039 · 2026-05-23T05:28:49.678212+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每一条 Strength、Must-Fix、Should-Fix、Minor 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — Round 1 审稿意见（方法严谨性）\n\n### Overall\n**Overall**: 3.5 / 5（Borderline Conference）\n**一句话总结**: C1 方法论扎实、可达 Conference 水平；但 C2–C4 受 authorization scope 低可靠性和跨 judge 类型排名近零相关影响。\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] Authorization scope 类型的系统性不可靠，动摇 C2 和 C4 claims\n- κ=0.385（仅 fair）, per-type ICC ≈ 0, 单独驱动 ρ=0.09→0.90, 单独驱动 C4 interaction（排除后 p=0.97）, 跨模型方差 52pp\n- Table 2 和主分析中对 auth scope 无显著区分标记\n- 建议：Table 2 增加警告标注；C2 中将 auth scope 明确标记为 \"unreliable\"；系统性报告 excluding auth scope 后的 C2 结论\n\n**N2** [critical] Residual variance decomposition（15% stochastic + 46% systematic）仅基于 OpenAI family\n- ICC(1)=0.749 基于 200 cells，但均来自 OpenAI 模型\n- §5.1 和 §7 主文中作为核心结论呈现，未附 OpenAI-specific 限定\n- 建议：主文中每次引用时注明 \"OpenAI-family estimate\"；提供跨 provider ICC proxy\n\n---\n\n### Should-Fix 问题\n\n**W1** [major] TOST ±15pp justification 不够严谨\n- 标准 (2) 本质上是 unfalsifiable 主观判断\n- ±10pp 时仅 3/15 pairs 等价\n- 建议：承认 pragmatic 选择；bootstrap clustering 作为主要证据\n\n**W2** [major] 跨 judge 组类型排名 ρ=0.09 的处理有 post-hoc 嫌疑\n- 排除 1/6 类型后从 ρ=0.09 到 ρ=0.90\n- 建议：将 three-family validation 提升到主文；排除分析标记为 sensitivity check\n\n**W3** [major] Cross-judge calibration 样本量不足以支撑 per-type κ 估计\n- 100 episodes 分到 6 类型后每类约 17 个\n- Per-type κ 的 CI 未报告\n- 建议：补充 bootstrap CI；加 precision 警告\n\n**W4** [minor] Token count 作为 incompleteness confound control 的粗糙性\n- OR=1.022/token，但 token count 是粗糙 proxy\n- 建议：补充 semantic-level 信息量度量\n\n**W5** [minor] 主文可能超过 8 页限制\n- Discussion 从 p8 延伸到 p9\n- 建议：压缩 Discussion 或移部分 Analysis 到 Appendix\n\n---\n\n### Strengths\n\n**S1**: Matched-pair 因果设计严谨。perturbation control 确认语义歧义特异性。Holm-Bonferroni 在三个预注册测试族内校正。\n\n**S2**: 统计方法选择得当且全面。每种方法都适合对应分析。\n\n**S3**: 多层次复制。ICC=0.919；SOPBench 跨基准；Gemini/LLaMA 跨架构；cross-domain 一致性。\n\n**S4**: Confound 处理多角度。Token count regression、exclusion analysis、coreferential lower bound 三个独立角度。\n\n**S5**: 高度透明的 limitation disclosure。主动披露 ρ=0.09、auth scope 低 κ、OpenAI-only ICC 等。\n\n**S6**: C1 core finding 非常稳健。+34.0pp 跨 7 模型 + SOPBench 一致。排除任何单一类型均不影响 C1。\n\n---\n\n### Questions\n\n**Q1**: Perturbation control CI [-8.0, 6.67] pp 对 5pp 或 10pp true effect 的 power 是多少？\n**Q2**: Type III SS variance decomposition 的完整模型公式是什么？是否包含 random effects？\n**Q3**: Auth scope per-type κ=0.385 的 bootstrap 95% CI 是多少？\n**Q4**: 是否计算过跨 provider reproducibility（如 GPT-5.4 vs Claude）？\n**Q5**: Coreferential 作为 confound-free lower bound，如何确保上下文不引入信息不对称？\n**Q6**: NMI 在 failure mechanism 分布高度不均衡时是否是合适度量？\n**Q7**: Bootstrap clustering modal partition 仅 34.3%，AU=0.47，能否提供更高 k 值的 partition stability？\n\n---\n\n### Missing References\n- Ye et al. (2024) \"FLASK: Fine-grained Language Model Evaluation\" 作为 LLM-as-judge 方法论对比\n\n---\n\n请对以上每一条逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每一条 Strength、Must-Fix、Should-Fix、Minor 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — Round 1 审稿意见（方法严谨性）\n\n### Overall\n**Overall**: 3.5 / 5（Borderline Conference）\n**一句话总结**: C1 方法论扎实、可达 Conference 水平；但 C2–C4 受 authorization scope 低可靠性和跨 judge 类型排名近零相关影响。\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] Authorization scope 类型的系统性不可靠，动摇 C2 和 C4 claims\n- κ=0.385（仅 fair）, per-type ICC ≈ 0, 单独驱动 ρ=0.09→0.90, 单独驱动 C4 interaction（排除后 p=0.97）, 跨模型方差 52pp\n- Table 2 和主分析中对 auth scope 无显著区分标记\n- 建议：Table 2 增加警告标注；C2 中将 auth scope 明确标记为 \"unreliable\"；系统性报告 excluding auth scope 后的 C2 结论\n\n**N2** [critical] Residual variance decomposition（15% stochastic + 46% systematic）仅基于 OpenAI family\n- ICC(1)=0.749 基于 200 cells，但均来自 OpenAI 模型\n- §5.1 和 §7 主文中作为核心结论呈现，未附 OpenAI-specific 限定\n- 建议：主文中每次引用时注明 \"OpenAI-family estimate\"；提供跨 provider ICC proxy\n\n---\n\n### Should-Fix 问题\n\n**W1** [major] TOST ±15pp justification 不够严谨\n- 标准 (2) 本质上是 unfalsifiable 主观判断\n- ±10pp 时仅 3/15 pairs 等价\n- 建议：承认 pragmatic 选择；bootstrap clustering 作为主要证据\n\n**W2** [major] 跨 judge 组类型排名 ρ=0.09 的处理有 post-hoc 嫌疑\n- 排除 1/6 类型后从 ρ=0.09 到 ρ=0.90\n- 建议：将 three-family validation 提升到主文；排除分析标记为 sensitivity check\n\n**W3** [major] Cross-judge calibration 样本量不足以支撑 per-type κ 估计\n- 100 episodes 分到 6 类型后每类约 17 个\n- Per-type κ 的 CI 未报告\n- 建议：补充 bootstrap CI；加 precision 警告\n\n**W4** [minor] Token count 作为 incompleteness confound control 的粗糙性\n- OR=1.022/token，但 token count 是粗糙 proxy\n- 建议：补充 semantic-level 信息量度量\n\n**W5** [minor] 主文可能超过 8 页限制\n- Discussion 从 p8 延伸到 p9\n- 建议：压缩 Discussion 或移部分 Analysis 到 Appendix\n\n---\n\n### Strengths\n\n**S1**: Matched-pair 因果设计严谨。perturbation control 确认语义歧义特异性。Holm-Bonferroni 在三个预注册测试族内校正。\n\n**S2**: 统计方法选择得当且全面。每种方法都适合对应分析。\n\n**S3**: 多层次复制。ICC=0.919；SOPBench 跨基准；Gemini/LLaMA 跨架构；cross-domain 一致性。\n\n**S4**: Confound 处理多角度。Token count regression、exclusion analysis、coreferential lower bound 三个独立角度。\n\n**S5**: 高度透明的 limitation disclosure。主动披露 ρ=0.09、auth scope 低 κ、OpenAI-only ICC 等。\n\n**S6**: C1 core finding 非常稳健。+34.0pp 跨 7 模型 + SOPBench 一致。排除任何单一类型均不影响 C1。\n\n---\n\n### Questions\n\n**Q1**: Perturbation control CI [-8.0, 6.67] pp 对 5pp 或 10pp true effect 的 power 是多少？\n**Q2**: Type III SS variance decomposition 的完整模型公式是什么？是否包含 random effects？\n**Q3**: Auth scope per-type κ=0.385 的 bootstrap 95% CI 是多少？\n**Q4**: 是否计算过跨 provider reproducibility（如 GPT-5.4 vs Claude）？\n**Q5**: Coreferential 作为 confound-free lower bound，如何确保上下文不引入信息不对称？\n**Q6**: NMI 在 failure mechanism 分布高度不均衡时是否是合适度量？\n**Q7**: Bootstrap clustering modal partition 仅 34.3%，AU=0.47，能否提供更高 k 值的 partition stability？\n\n---\n\n### Missing References\n- Ye et al. (2024) \"FLASK: Fine-grained Language Model Evaluation\" 作为 LLM-as-judge 方法论对比\n\n---\n\n请对以上每一条逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2040 · 2026-05-23T05:28:51.141154+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1462
}
```

</details>

---


### Assistant

_source line 2041 · 2026-05-23T05:28:53.428570+00:00_

交叉分享已发送给两位 Reviewer。等待他们的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 192

## Round 192

2 recorded events


### User

_source line 2042 · 2026-05-23T05:28:55.986212+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5/5（Borderline Conference）

核心判断：
- **C1**（+34.0pp 二值效应）方法论扎实，跨 7 个模型和 2 个 benchmark 复制，是论文最强贡献
- **C2–C4** 类型层面分析受 authorization scope 系统性不可靠性（κ=0.385, ICC≈0, 单独驱动 ρ=0.09）拖累
- 两个 Must-Fix：(1) auth scope 需在主分析中更显著标注为不可靠；(2) residual variance decomposition 需在主文中限定为 OpenAI-family estimate
- 三个 Should-Fix：TOST ±15pp bound justification、ρ=0.09 post-hoc 排除叙述、cross-judge per-type κ 的 CI

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2043 · 2026-05-23T05:29:00.514958+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 193

## Round 193

2 recorded events


### User

_source line 2044 · 2026-05-23T05:30:48.894991+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Strengths

**[AGREE] R2-S1**: Matched-pair causal design 确实是核心方法论贡献。我在 R1-S1 中也给出了同样评价。与观察性设计相比，minimal-edit 配对在 clause level 的因果推断确实更可靠。

**[AGREE] R2-S2**: Variance decomposition 的实用价值我也认同（R1-S2）。不过我补充：这一分解的 residual 60.8% 的内部结构（15% stochastic + 46% systematic）仅基于 OpenAI family ICC，这一限定在我的 N2 中已标记为 critical。

**[AGREE] R2-S3**: 统计方法选择确实审慎，我的 R1-S2 给出了一致评价。

**[AGREE] R2-S4**: 跨架构评估的 generalizability 值得肯定。C1 跨 7 模型一致显著是论文最强的鲁棒性证据之一。

**[AGREE] R2-S5**: Error analysis 章节提供了超出纯 measurement 的洞察。但我对 "disambiguation neglect" 的推断边界有保留（见下 W5 回应）。

---

### Must-Fix

**[AGREE] R2-N1**: 正文超 8 页限制。我在 R1-W5 中也标记了这一问题（标为 minor，但 R2 标为 critical）。重新考虑后，我同意 R2 将此提升为 critical 的判断：EMNLP 2026 的 8 页限制是硬性要求，违反可能导致 desk rejection。Discussion（§7）三段 + Conclusion（§8）溢出至 page 9 是清晰可见的。建议压缩 Discussion 或将部分 §6 Analysis 内容移入 Appendix。

**[REBUT] R2-N2**: Incompleteness confound 在 headline claim 中的处理。R2 认为 "confound-free range 中位值远低于 34.0 pp"，但这一表述有误导性。需要区分两个数字：

1. **Confound-free range**（+18.7 to +36.0 pp）：这是五个非 incompleteness 类型各自的效应幅度范围。+18.7 pp 是 coreferential（最低类型）的效应，+36.0 pp 是 authorization scope 的效应。这不是 pooled effect，而是 per-type range。
2. **排除 incompleteness 后的 pooled effect**：§5.1 明确报告为 "+31.0 pp (95% CI [27.9, 34.1])"——与 +34.0 pp 仅差 3 pp。

因此，headline +34.0 pp 并未被 incompleteness confound 显著膨胀。排除 incompleteness 后的 pooled 效应（+31.0 pp）仍在 +34.0 pp 的 95% CI 内。Abstract 中的括号 caveat 已将 confound-free range 和 incompleteness exclusion 都呈现了。

**但我同意方向性建议**：Abstract 可以将 "+31.0 pp excluding incompleteness" 作为更保守的 headline 数字放在更显著位置，而非仅用括号标注 per-type range。这是 framing 问题而非 validity 问题——不应标为 critical。建议降级为 **should-fix**。

---

### Should-Fix

**[AGREE] R2-W1**: Cross-judge type ranking ρ=0.09 削弱 C2。这与我的 R1-W2 完全一致。排除 auth scope 后达到 ρ=0.90 的 post-hoc 特征是需要在主文中更谨慎处理的问题。不过我补充：论文确实提供了独立的 three-family validation（ρ=0.71–0.89, Appendix W），这部分不依赖 post-hoc exclusion。建议将 three-family validation 提升到主文。

**[AGREE] R2-W2**: 合成歧义的生态效度是合理担忧。论文在 Limitations "Ecological validity" 段承认了这一点，也提到 SOPBench replication（+12.6 pp）和 "dose-response study" 作为 future work。但我认为这是该研究设计的固有限制而非 must-fix——matched-pair causal design 本质上需要合成操控。真实企业策略的歧义分布无法进行配对控制。论文的 post-hoc realism validation（§4.2, "linguistic consistency with original τ²-bench policy text"）部分缓解了这一担忧。

**[REBUT] R2-W3**: NMI 0.23 vs 0.01 的 "order of magnitude" 表述。R2 认为 NMI=0.23 "绝对值仍是弱关联"。这需要区分两个问题：

1. **比较层面**：NMI 0.23 vs 0.01 确实是约 23 倍，超过 "an order of magnitude"。论文的 claim 是**相对比较**（"predicts failure mechanism an order of magnitude more strongly than violation rate"），而非声称 NMI=0.23 是强关联。
2. **绝对解读**：NMI=0.23 对应 Cramér's V=0.45（§7, Appendix S, Table 13），按 Cohen's conventions 属 medium-to-large effect。同时，Table 14 的 confusion matrix 显示每个类型都有一个 dominant failure mechanism（≥3/5 model consistency，§6.1），这提供了超越单一统计量的结构性证据。
3. **论文已有绝对值解读**：§7 "Taxonomy as diagnostic tool" 段同时报告了 NMI=0.23 和 Cramér's V=0.45，后者有明确的 effect size convention。

R2 的建议 "加绝对值解读" 实际上论文已经做了（通过 Cramér's V=0.45）。不过可以在主文中更明确地注明 NMI=0.23 的绝对水平（如 "moderate association in absolute terms"）。建议降级为 **minor**。

**[AGREE] R2-W4**: Abstract 信息过载。约 150 词内确实包含了过多定量结果。这是写作风格问题，不影响学术判断，但会影响可读性。同意 R2 的建议保留 2–3 个核心数字。

**[AGREE] R2-W5**: Disambiguation neglect 的推断边界。这是一个好 point。§6.2 定义 "disambiguation awareness versus surface adoption"，但测量的是 trace 中是否出现歧义识别的 surface signal，而非模型内部是否检测到歧义。论文引用 Vijayvargiya et al. (2026) 指出 "interactive disambiguation can recover substantial performance"，这暗示 neglect 是行为性的而非能力性的。R2 建议 "agents rarely surface ambiguity in their reasoning traces" 更精确，但论文已在 §6.2 最后一句（"the neglect we observe is behavioral rather than capacity-limited"）和 Limitations "Disambiguation channel" 段做了类似限定。建议在 §6.2 的首次定义处加入 "surface" 或 "externally expressed" 限定词。

---

### Minor

**[AGREE] R2-M1**: Table 2 增加 "Overall (excl. Incomp.)" 行。这与我的建议一致——incompleteness confound 的重要性需要在主结果表中更显著地体现。排除 incompleteness 后的 pooled effect（+31.0 pp）已在 §5.1 文本中报告，但放入 Table 2 会更直观。

**[AGREE] R2-M2**: Figure 2 标注冗余。这是纯视觉优化建议，合理。

**[AGREE] R2-M3**: "five architecturally diverse models" 表述。GPT-5.4 和 GPT-4.1 确实同属 OpenAI（虽然可能是不同架构代际），"four providers and two architecture families"（§4.3 原文）是更准确的说法。论文 §4.3 实际用的是 "spanning four providers and two architecture families"，R2 引用的 "five architecturally diverse" 可能出现在其他位置。不论如何，论文某处若有此表述，改为 "five models from four providers" 更准确。

**[AGREE] R2-M4**: References 格式。arXiv 引用写法不统一是排版问题，容易修复。

---

### Questions

**R2-Q1**: 歧义条款注入点选择标准。§4.2 描述了 template-based pipeline 和两名 annotator 的 review 流程，但确实未详细说明注入位置的选择策略（如是在 policy 开头、中间还是结尾；是否针对 high-stakes vs low-stakes clauses）。这是一个有效的方法论问题，注入位置可能影响 agent 的注意力分配。但论文的 matched-pair 设计控制了注入位置（同一 clause 的两个 variant 注入到同一位置），因此注入位置不会影响 **within-pair** 效应（C1），只可能影响 **across-type** 比较（C2）。

**R2-Q2**: Human validation κ。R2 引用 "§4.6 的 κ=0.72"，但论文实际报告在 §4.4（非 §4.6）：inter-annotator agreement κ=0.798, κ_w=0.762。这两个数字均为两名 annotator 之间的 Cohen's κ（论文未明确标注，但 two-annotator setting 下默认为 Cohen's κ）。R2 引用的数字和章节号均有误。

**R2-Q3**: Incompleteness 从 taxonomy 中独立出来。论文 §3 "Scope of 'ambiguity'" 段已讨论了这一点——incompleteness 严格来说不是 linguistic ambiguity 而是 information absence，但 "LLM agents process all six types identically" 是将其纳入统一 taxonomy 的理由。这是一个 design choice 而非错误。论文的 confound controls（Appendix F/H, §5.1 confound-free range）已对 incompleteness 做了充分的独立分析。

**R2-Q4**: Mitigation instruction quality 作为 confound。这是一个有效担忧。Appendix B 的 prompt template 对所有类型使用相同结构（"This policy clause may contain [type] ambiguity..."），只替换类型名。效果差异（auth scope -18.0 pp vs incompleteness -3.3 pp n.s.）可能反映类型本身的可干预性差异，也可能反映 instruction 对不同类型的匹配度差异。论文将此定位为 exploratory（Appendix B），未从中得出强 causal claim，这是恰当的。

**R2-Q5**: τ²-bench 领域。是的，τ²-bench 原始版本仅覆盖 retail 和 airline 两个 customer-service 领域（§4.1; Appendix U cross-domain analysis 明确列出 retail n=1,550 和 airline n=1,447）。Limitations "Scope" 段承认 "effects in other domains remain untested"。

---

### Missing References

**R2-Ref-1**: ATBench (Li et al., 2026)。需要确认这是否指论文已引用的 τ²-bench (Barnes et al., 2025) 或 SOPBench (Li et al., 2025)。如果是独立工作，确实可补充。

**R2-Ref-2**: "Enhancing LLM Agent Safety via Causal Influence Prompting (2026)"。如果是真实发表的工作，且涉及 causal 方法 + agent safety，确实与本文相关。但需验证该引用的真实性。

---

### 总结

与 R2 的主要共识：(1) 正文超页限制是必须修复的问题；(2) cross-judge ρ=0.09 削弱 C2；(3) disambiguation neglect 的推断边界需要更精确的表述。

与 R2 的主要分歧：(1) N2 不应为 critical——排除 incompleteness 后 pooled effect 为 +31.0 pp，headline +34.0 pp 并未被显著膨胀，建议降级为 should-fix（framing 问题）；(2) W3 中 NMI=0.23 的 "order of magnitude" 表述在比较层面是准确的，且论文已通过 Cramér's V=0.45 提供了绝对值解读，建议降级为 minor。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2045 · 2026-05-23T05:30:53.110012+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 194

## Round 194

2 recorded events


### User

_source line 2046 · 2026-05-23T05:30:56.127806+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Director。

与 R2 的核心共识：页数超限、cross-judge ρ=0.09、disambiguation neglect 推断边界。主要分歧：(1) incompleteness confound 不应为 critical——排除后 pooled effect 仅降 3pp 至 +31.0pp，是 framing 问题而非 validity 问题；(2) NMI "order of magnitude" 表述在比较层面准确，且已有 Cramér's V=0.45 作绝对值补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2047 · 2026-05-23T05:31:01.734743+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 195

## Round 195

10 recorded events


### User

_source line 2048 · 2026-05-23T05:31:03.239278+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 意见

---

### Must-Fix 回应

**[AGREE] R1-N1: Authorization scope 系统性不可靠**

同意这是本文最大的方法论隐患。我在自己的审稿意见中也独立指出了 ρ=0.09 的问题（R2-W1）。R1 补充的证据更加细致：

1. κ=0.385 是六类型中最低的（Table 9, Appendix G），且论文自述 per-type ICC ≈ 0（p20）——这意味着 auth scope 的违规率在模型间几乎无一致性。
2. 排除 auth scope 后 ρ 从 0.09 跳到 0.90，这不是 "sensitivity check" 而是说明 C2 的 partial ordering claim 完全取决于是否包含这一个类型。
3. R1 指出 C4 interaction 排除 auth scope 后 p=0.97——如果属实，这意味着 §7 中 "type-mechanism interaction" 作为 Discussion 核心论点之一，其统计基础同样依赖 auth scope。

补充发现：从 Figure 4（p7）可以看到 auth scope 的 violation rate 在 ambiguous conditions 下变化最大（约 52 pp across models），远超其他类型。Table 2 中 auth scope 的 overall violation rate 跨模型标准差也最高。论文在 Appendix P 和 Limitations 中确实提到了 auth scope 的不稳定性，但仅作为 passing remark，未在 C2/C4 的主文 claim 中作出相应调整。

**R1 的建议（Table 2 警告标注 + C2 中标记 unreliable + 报告 excluding auth scope 结论）是具体可操作的，我完全支持。**

---

**[AGREE with nuance] R1-N2: Variance decomposition 仅基于 OpenAI family**

同意核心关切，但需要区分两个层次：

1. **ICC(3,1) = 0.919 across all 5 main models**（§4.6）——这是全模型的一致性指标，not OpenAI-specific。说明 binary ambiguity effect (C1) 跨模型稳健。
2. **15% stochastic + 46% systematic 的 partition**——这确实来自 OpenAI family 的 ICC(1) replication（Appendix X, p19-20），因为只有 OpenAI 系列有足够的 within-family 变体来做 stochastic/systematic 分解。

R1 的批评对第 2 点完全成立：§5.1 和 §7 在呈现 "~15% stochastic" 时未加 OpenAI-specific 限定，读者会误认为这是跨架构的通用结论。但 R1 建议的 "提供跨 provider ICC proxy" 可能不可行——目前只有 OpenAI 有同族多模型（GPT-3.4 和 GPT-4.1），其他 provider 无法计算 within-family ICC。

**建议折中方案：主文每次引用 stochastic/systematic split 时注明 "estimated from an OpenAI-family replication"；补充 Table 7-8 (Appendix E) 中 Gemini 和 LLaMA 的 point estimate 作为定性一致性证据，但不做跨 provider ICC claim。**

---

### Should-Fix 回应

**[AGREE] R1-W1: TOST ±15pp justification**

同意 ±15pp 的选择有 pragmatic 成分。论文给出的两个标准（Lakens, 2017）中，standard (2)（"it exceeds a 2×, 95th-percentile severity-level divergence"）确实难以独立验证——R1 说得对，这本质上是用数据本身的分布来定义 equivalence margin，有 circular reasoning 风险。

但论文在 Appendix C 提供了 ±5pp 到 ±20pp 的 sensitivity analysis（Table 3），结果显示 switching to any violation yields consistent results。Bootstrap clustering（Appendix I）作为 non-parametric 替代方案也支持 type grouping 结构。

**支持 R1 建议：主文中承认 ±15pp 是 pragmatic 选择而非理论驱动；将 bootstrap clustering 提升为与 TOST 并列的主要证据。**

---

**[AGREE] R1-W2: ρ=0.09→0.90 的 post-hoc 嫌疑**

完全同意。我在 R2-W1 中也独立提出了同样的关切。排除 1/6 类型后相关性从近零到 0.90，这几乎是 "removing the inconvenient data point" 的教科书案例。即使论文给出了排除的理论理由（auth scope 的 rank reversal），这种操作在审稿中会被高度怀疑。

**补充建议：论文可以考虑用 robust rank correlation（如 Kendall's τ with breakdown point analysis）来报告 type ranking concordance，这类方法对单个 outlier 类型的敏感性有明确的量化。Appendix P 已报告了 Kendall's τ，但主文只用 Spearman ρ。**

---

**[AGREE] R1-W3: Per-type κ 样本量不足**

同意。100 episodes / 6 types ≈ 17 per type。对于 Cohen's κ 来说，n=17 的 95% CI 宽度通常在 ±0.2 到 ±0.3，这意味着 auth scope 的 κ=0.385 的真实 CI 可能跨越 fair → poor 或 fair → moderate 的边界。没有 CI，读者无法判断 per-type κ 差异是否统计显著。

**支持 R1 建议补充 bootstrap CI。这是一个 straightforward 的补充分析，不需要新数据。**

---

**[AGREE with minor reservation] R1-W4: Token count 作为 confound proxy 的粗糙性**

原则上同意 token count 是粗糙的信息量 proxy。但从实用角度看：

1. 论文使用 token count 的目的是控制 incompleteness 条款中 "information addition" 的 confound（Appendix F/H）。对于这个特定目的，token count 是 reasonable first approximation——更长的 unambiguous variant 通常包含更多信息。
2. R1 建议的 "semantic-level 信息量度量" 在实操中很难定义和计算。什么是一个 policy clause 的 semantic information content？没有公认的度量标准。

**建议：在论文中承认 token count 是 coarse proxy 并讨论其局限性，但不需要计算新的度量。如果 reviewer 坚持，可以补充 clause count 或 condition count 作为额外 proxy。**

---

**[AGREE] R1-W5: 正文超 8 页**

完全同意——这与我的 R2-N1 一致。我将其评为 critical 级别（可能导致 desk rejection），R1 评为 minor，我认为应该是 critical。EMNLP 2026 的 8 页限制是 hard constraint。

---

### Strengths 回应

**[AGREE] R1-S1 through R1-S6**: 全部同意。特别是：

- **S1** (matched-pair design): 与我的 R2-S1 一致。这确实是本文最核心的方法论贡献。
- **S5** (透明的 limitation disclosure): 这一点值得强调——论文主动披露了很多对自己不利的数据（ρ=0.09, auth scope 低 κ, OpenAI-only ICC），这在投稿论文中不常见，体现了学术诚信。但 R1 和我的共同观察是：disclosure ≠ adequate handling。论文承认了问题但未充分调整 claim 强度。
- **S6** (C1 稳健性): 完全同意。排除任何单一类型、任何单一模型，C1 均成立。这是论文最坚实的贡献。

---

### Questions 回应

**[AGREE] R1-Q1**: Perturbation control power analysis 是合理的追问。CI [-8.0, 6.67] pp 对 5pp true effect 的 power 可能不足。但考虑到 perturbation control 的目的是确认 non-ambiguity perturbations 不产生大效应（而非 detect 小效应），这个 CI 对排除 >8pp 的 confound 已足够。

**[AGREE] R1-Q2**: Type III SS 模型公式确实应该在正文或附录中明确报告。从 §5.1 上下文推断应该是 fixed-effects ANOVA（condition × type × model），但论文未写明是否包含 random effects 或 interaction terms。

**[AGREE] R1-Q3**: Auth scope κ=0.385 的 bootstrap CI——同 W3，这是必要的补充。

**[AGREE] R1-Q4**: 跨 provider reproducibility 是好问题。Appendix E 的 Gemini/LLaMA replication 提供了 point estimates，但未计算 cross-provider ICC。如 N2 讨论，within-family ICC 受限于可用模型数。

**[AGREE with nuance] R1-Q5**: Coreferential 作为 confound-free lower bound 的假设需要验证。但 coreferential ambiguity 的定义（"whose variants are lexically identical to their unambiguous counterparts," Appendix F, §6.3）意味着 token delta = 0，从而在 information-addition 维度上没有 confound。R1 问的 "上下文信息不对称" 可能指的是 pragmatic inference——但这恰恰是 ambiguity 本身的效应，不是 confound。

**[AGREE] R1-Q6**: NMI 在高度不均衡分布下的适用性。从 Figure 5 可以看到 failure mechanism 分布确实不均（structural misparse 和 boundary violation 占主导）。NMI 通过 normalization 部分缓解了 marginal 不均衡，但当某些 mechanism 类别频率极低时，estimation 不稳定。Cramér's V（论文在其他地方已使用）可能是更好的替代选择。

**[AGREE] R1-Q7**: Bootstrap clustering AU=0.47 和 modal partition 34.3% 确实表明 partition 不够稳定。论文在 Appendix I 中说 "the most frequent partition but not overwhelmingly stable"。如果更高 k 值能产生更稳定的 partition，这会改变 type grouping 的解读。

---

### Missing References 回应

**[REBUT] R1-Missing: FLASK (Ye et al., 2024)**

FLASK 是一个 fine-grained LLM evaluation framework，主要关注 LLM output quality 的多维度评估。本文使用的 dual-judge pipeline（§4.4）评估的是 binary violation outcome（violate or not），而非 output quality 的多维度打分。两者的 judge 设计目标不同：FLASK 为 quality assessment，本文为 compliance classification。更相关的 LLM-as-judge 参考是论文已引用的 Zheng et al. (2024)（automated pipeline validation）。

FLASK 作为 nice-to-have 引用是可以的，但不构成 missing reference——不引用不影响论文的技术完整性。

---

### 总结

与 R1 的评审意见高度一致。主要共识点：
1. **C1 是稳健的贡献**（两位 reviewer 均认可）
2. **Auth scope 不可靠性是核心方法论问题**（R1-N1 + R2-W1），需在 C2/C4 claim 中作出实质性调整
3. **正文超 8 页需修复**（R1-W5 + R2-N1）
4. **ρ=0.09→0.90 的排除分析有 post-hoc 嫌疑**（R1-W2 + R2-W1）

主要分歧：
1. **N2 严重程度**：R1 评为 critical，我认为是 major-with-nuance。ICC(3,1)=0.919 across all models 是 strong evidence，stochastic/systematic split 的 OpenAI-only 限制是 labeling issue 而非 validity threat。
2. **W5/页数问题严重程度**：R1 评为 minor，我评为 critical。8 页限制是 EMNLP 2026 的 hard constraint。
3. **FLASK 引用必要性**：R1 认为缺失，我认为不构成 missing reference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2049 · 2026-05-23T05:31:48.237111+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2050 · 2026-05-23T05:31:48.388264+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T05:18:33.476748+00:00\", \"completed_at\": \"2026-05-23T05:21:54.499020+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯 Title/Abstract/Introduction），Figure 1 出现在 page 2 顶部，属于可接受范围（前 3 页内）\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（Experimental Overview 三段式流水线图）是有效的视觉锚点，清晰传达 taxonomy → evaluation → cross-judge 的实验框架，与 title/abstract 一致\"}, {\"severity\": \"warning\", \"dimension\": \"pages 4-5\", \"message\": \"连续 2 页纯文本（Section 4 Method），无任何 display item 穿插。内容为实验设计和统计方法描述，尚可接受，但在 page 4 或 5 插入一个 method 示意图或 matched-pair 构造示例会改善阅读节奏\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"单页堆叠 3 个 display items（Table 2 全宽 + Figure 3 左栏 + Figure 4 右栏），密度过高，文字段落被压缩到极少，审稿人可能感到拥挤\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"最后一页（appendix 末页）内容仅占约 40% 页面，剩余大面积空白。因是 appendix 末尾，非主要问题\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-9\", \"message\": \"正文共 7 个 display items（Figure 1-5 + Table 1-2），约 0.78 个/页。对于实证为主的论文，密度合理偏紧凑\"}, {\"severity\": \"info\", \"dimension\": \"pages 12-19\", \"message\": \"Appendix 包含 Tables 3-17（15 个表），密度很高但 appendix 可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 和 Figure 4 尺寸偏小（各占约半栏高度），axis label 和 legend 字号接近可读下限。建议将两图合并为一个双面板 figure 并适当增大，或将其中一个移至下一页\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（Variance Decomposition 柱状图）清晰可读，caption 自包含，解释了虚线含义和阅读方式\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 5（Type-mechanism heatmap）颜色梯度清晰，单色渐变色盲友好，cell 内文字可读\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Table 1（Taxonomy）使用 booktabs 风格，列对齐良好，无竖线\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2（主结果表）全宽跨栏，最优值加粗，booktabs 风格，小数精度一致（1 位），格式规范\"}, {\"severity\": \"info\", \"di
…[truncated 1063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2051 · 2026-05-23T05:31:48.540066+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2052 · 2026-05-23T05:31:48.640894+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2053 · 2026-05-23T05:33:38.813476+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 23\n\n# ============================================================\n# R23 ISSUES — OPEN\n# ============================================================\n\n- id: \"R23-N1\"\n  summary: \"正文超 8 页限制（Discussion+Conclusion 溢出至 p9，约 8.4-8.5 页）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2 初评 critical（可能导致 desk rejection），R1 初评 minor 但交叉回应后同意升级为 critical。视觉审查 Agent 也独立确认 Conclusion 结束位置超过 page 8 底部。建议压缩 Discussion 或将部分 §6 Analysis 移入 Appendix。\"\n  action_items:\n    - round: 23\n      action: \"压缩正文至 8 页以内（Discussion 三段→两段，或将部分 Analysis 内容移入 Appendix）\"\n      assigned_to: \"Research Director\"\n      status: open\n\n- id: \"R23-N2\"\n  summary: \"Authorization scope 类型系统性不可靠（κ=0.385, ICC≈0, 单独驱动 ρ=0.09 和 C4 interaction），但在主分析中未充分标注\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1 提出（N1），R2 完全同意并补充 Figure 4 和 Table 2 证据。五个独立指标同时指向不可靠：lowest κ (0.385), per-type ICC≈0, 单独驱动 ρ=0.09→0.90, 单独驱动 C4 (排除后 p=0.97), 52pp 跨模型方差。论文在 Appendix 和 Limitations 中有 disclosure 但主文 claim 未调整。\"\n  action_items:\n    - round: 23\n      action: \"Table 2 对 auth scope 增加显著警告标注；C2 讨论中将 auth scope 标记为 unreliable；系统性报告 excluding auth scope 后的 C2 结论\"\n      assigned_to: \"Research Director\"\n      status: open\n\n- id: \"R23-W1\"\n  summary: \"Incompleteness confound 在 headline claim (34.0pp) 中的标注不够显著——framing 问题\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2 初评 critical，R1 以数据 rebut（排除 incompleteness 后 pooled effect +31.0pp，仅差 3pp），建议降级为 should-fix。分歧已充分表征：核心争议是 framing 而非 validity。建议在 Abstract 中将 +31.0pp (excl. incompleteness) 放在更显著位置。\"\n\n- id: \"R23-W2\"\n  summary: \"跨 judge 组类型排名 ρ=0.09→排除 auth scope 后 ρ=0.90 的 post-hoc 嫌疑\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1（W2）和 R2（W1）独立提出。three-family validation (ρ=0.71-0.89, Appendix W) 是更强证据但仅在 Appendix。建议将 three-family validation 提升到主文作为 primary evidence，排除分析标记为 sensitivity check。R2 补充建议用 robust rank correlation（如 Kendall's τ with breakdown point analysis）。\"\n\n- id: \"R23-W3\"\n  summary: \"Residual variance decomposition (15% stochastic + 46% systematic) 仅基于 OpenAI family，主文中未充分限定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1 提出（N2，评为 critical），R2 同意核心关切但认为是 labeling issue 而非 validity threat（ICC(3,1)=0.919 是全模型指标）。建议折中：主文每次引用 stochastic/systematic split 时注明 OpenAI-family estimate。\"\n\n- id: \"R23-W4\"\n  summary: \"TOST ±15pp SESOI 的 justification 有 pragmatic/circular 成分，需要更透明的承认\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1（W1）提出，R2 完全同意。标准 (2) 本质上是主观判断。±10pp 时仅 3/15 pairs 等价。建议承认 pragmatic 选择，将 bootstrap clustering 提升为与 TOST 并列的主要证据。\"\n\n- id: \"R23-W5\"\n  summary: \"Cross-judge calibration per-type κ 缺少 bootstrap CI（n≈17/type 不足以支撑 per-type 估计）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1（W3）提出，R2 完全同意。100 episodes / 6 types ≈ 17 per type，κ=0.385 的真实 CI 可能跨越 fair→poor 或 fair→moderate。补充 bootstrap CI 是 straightforward 分析。注：human-LLM agreement (Appendix G) 已有 bootstrap CI，cross-judge calibration 应对齐。\"\n\n- id: \"R23-W6\"\n  summary: \"合成歧义的生态效度——未提供真实企业策略文档的歧义案例\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2（W2）提出，R1 同意但指出这是 matched-pair design 的固有限制。SOPBench replication (+12.6pp) 提供部分支持但也是合成 benchmark。Limitations 已有 acknowledgment 但 Discussion 可更明确讨论 synthetic→real-world gap 的具体 threats。\"\n\n- id: \"R23-M1\"\n  summary: \"NMI 0.23 vs 0.01 的 order of magnitude 表述需要绝对值语境化\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2（W3）提出，R1 rebut（论文已有 Cramér's V=0.45 提供绝对值解读）。分歧：R2 认为主文应更明确注明 NMI=0.23 的绝对水平，R1 认为已足够。建议在主文补充 moderate association 限定词。\"\n\n- id: \"R23-M2\"\n  summary: \"Abstract 信息过载（约 150 词内 6+ 个定量结果）\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2（W4）提出，R1 同意。建议保留 2-3 个核心数字。\"\n\n- id: \"R23-M3\"\n  summary: \"Disambiguation neglect 推断边界需收窄——应区分 internal detection 和 surface behavior\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2（W5）提出，R1 同意方向但指出论文已在 §6.2 末句和 Limitations 做了类似限定（behavioral rather than capacity-limited）。建议在 §6.2 首次定义处加入 surface/externally expressed 限定词。\"\n\n- id: \"R23-M4\"\n  summary: \"Table 2 Overall 行应增加 Overall (excl. Incomp.) 或脚注标注\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2（M1）提出，R1 同意。排除 incompleteness 后 pooled effect (+31.0pp) 已在 §5.1 文本中报告，放入 Table 2 更直观。\"\n\n- id: \"R23-M5\"\n  summary: \"Token count 作为 incompleteness confound control 是粗糙 proxy\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1（W4）提出，R2 同意但认为实操中 semantic-level 度量难以定义。建议承认局限性但不需计算新度量。auth scope token delta (+36.1) > incompleteness (+34.6) 但违规率更低，是有力反证据。\"\n\n# ============================================================\n# R22 ISSUES — ALL RESOLVED (from prior round)\n# ============================================================\n\n- id: \"R22-W1\"\n  summary: \"C4 model×type 交互完全由 authorization scope 驱动，该类型测量不可靠（κ=0.385, ICC≈0），C4 可能是测量伪影\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Removed C4 subsection; compressed to 1 caveat paragraph explicitly framing C4 as possibly reflecting measurement instability.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1 提出（W2），R2 完全同意。\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23 两位 Reviewer 确认 C4 在当前版本中仍被标注为 exploratory/suggestive only（§5 C4 段）。但 R23-N2 指出 auth scope 的不可靠性标注在主分析中仍不够显著。\"\n\n- id: \"R22-W2\"\n  summary: \"SOPBench 复制效应压缩 63%（34.0pp→12.6pp），缺乏原则性归因\"\n  category: experiment\n  severity: warning\n  status: resolved\n  resolution: \"Added principled framing in §5.1 and structured attribution in Appendix SOPBench section.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-W3\"\n  summary: \"ICC 复制仅覆盖 OpenAI 家族，但残差方差分解应用于所有模型\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Added OpenAI-family qualifier in §5.1 and Limitations §Scope.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23 两位 Reviewer 认为当前限定仍不够——主文 §5.1 和 §7 引用 stochastic/systematic split 时仍未逐次注明 OpenAI-family estimate（R23-W3）。\"\n\n- id: \"R22-W4\"\n  summary: \"SESOI ±15pp 缺乏领域接地论证，为统计驱动而非领域驱动\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Added explicit acknowledgment in §4.6.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23 两位 Reviewer 认为当前 §4.6 的表述仍暗示 principled justification（引用 Lakens 2017），需更明确承认 pragmatic 选择（R23-W4）。\"\n\n- id: \"R22-W5\"\n  summary: \"Token count 作为 incompleteness information-addition confound 代理过于粗糙\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Confound caveat added to §6.3 and Limitations §Confounds.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-M5 重新提出，但降级为 minor（论文已有多角度 confound control）。\"\n\n- id: \"R22-W6\"\n  summary: \"残差方差（60.8%）的干预天花板讨论不够充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Added intervention ceiling paragraph in Discussion §7.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M1\"\n  summary: \"生态效度缺口未量化——合成刺激与真实策略文档歧义的差距未知\"\n  category: framing\n  severity: minor\n  status: resolved\n  resolution: \"Added dose-response study suggestion and SOPBench lower bound in Limitations.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W6 重新提出（warning 级别），认为 Limitations 已有 acknowledgment 但 Discussion 需更明确讨论 synthetic→real-world gap 的具体 threats。\"\n\n- id: \"R22-M2\"\n  summary: \"层级结构（linguistic vs specification）C3 未通过 Holm-Bonferroni 校正\"\n  category: framing\n  severity: minor\n  status: resolved\n  resolution: \"Already addressed: §5.2 explicitly states organizational convenience rather than empirical claim.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M3\"\n  summary: \"人工 failure-mode 编码验证缺失\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"Limitations §Measurement states validation underway.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M4\"\n  summary: \"Table 2/Figure 2 中 incompleteness 应标注 confound status\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added dagger marker and footnote in Table 2.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M5\"\n  summary: \"Conclusion 偏短\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added diagnostic protocol and disambiguation neglect summary.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 23\n\n# ============================================================\n# R23 ISSUES — OPEN\n# ============================================================\n\n- id: \"R23-N1\"\n  summary: \"正文超 8 页限制（Discussion+Conclusion 溢出至 p9，约 8.4-8.5 页）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2 初评 critical（可能导致 desk rejection），R1 初评 minor 但交叉回应后同意升级为 critical。视觉审查 Agent 也独立确认 Conclusion 结束位置超过 page 8 底部。建议压缩 Discussion 或将部分 §6 Analysis 移入 Appendix。\"\n  action_items:\n    - round: 23\n      action: \"压缩正文至 8 页以内（Discussion 三段→两段，或将部分 Analysis 内容移入 Appendix）\"\n      assigned_to: \"Research Director\"\n      status: open\n\n- id: \"R23-N2\"\n  summary: \"Authorization scope 类型系统性不可靠（κ=0.385, ICC≈0, 单独驱动 ρ=0.09 和 C4 interaction），但在主分析中未充分标注\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1 提出（N1），R2 完全同意并补充 Figure 4 和 Table 2 证据。五个独立指标同时指向不可靠：lowest κ (0.385), per-type ICC≈0, 单独驱动 ρ=0.09→0.90, 单独驱动 C4 (排除后 p=0.97), 52pp 跨模型方差。论文在 Appendix 和 Limitations 中有 disclosure 但主文 claim 未调整。\"\n  action_items:\n    - round: 23\n      action: \"Table 2 对 auth scope 增加显著警告标注；C2 讨论中将 auth scope 标记为 unreliable；系统性报告 excluding auth scope 后的 C2 结论\"\n      assigned_to: \"Research Director\"\n      status: open\n\n- id: \"R23-W1\"\n  summary: \"Incompleteness confound 在 headline claim (34.0pp) 中的标注不够显著——framing 问题\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2 初评 critical，R1 以数据 rebut（排除 incompleteness 后 pooled effect +31.0pp，仅差 3pp），建议降级为 should-fix。分歧已充分表征：核心争议是 framing 而非 validity。建议在 Abstract 中将 +31.0pp (excl. incompleteness) 放在更显著位置。\"\n\n- id: \"R23-W2\"\n  summary: \"跨 judge 组类型排名 ρ=0.09→排除 auth scope 后 ρ=0.90 的 post-hoc 嫌疑\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1（W2）和 R2（W1）独立提出。three-family validation (ρ=0.71-0.89, Appendix W) 是更强证据但仅在 Appendix。建议将 three-family validation 提升到主文作为 primary evidence，排除分析标记为 sensitivity check。R2 补充建议用 robust rank correlation（如 Kendall's τ with breakdown point analysis）。\"\n\n- id: \"R23-W3\"\n  summary: \"Residual variance decomposition (15% stochastic + 46% systematic) 仅基于 OpenAI family，主文中未充分限定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1 提出（N2，评为 critical），R2 同意核心关切但认为是 labeling issue 而非 validity threat（ICC(3,1)=0.919 是全模型指标）。建议折中：主文每次引用 stochastic/systematic split 时注明 OpenAI-family estimate。\"\n\n- id: \"R23-W4\"\n  summary: \"TOST ±15pp SESOI 的 justification 有 pragmatic/circular 成分，需要更透明的承认\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1（W1）提出，R2 完全同意。标准 (2) 本质上是主观判断。±10pp 时仅 3/15 pairs 等价。建议承认 pragmatic 选择，将 bootstrap clustering 提升为与 TOST 并列的主要证据。\"\n\n- id: \"R23-W5\"\n  summary: \"Cross-judge calibration per-type κ 缺少 bootstrap CI（n≈17/type 不足以支撑 per-type 估计）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1（W3）提出，R2 完全同意。100 episodes / 6 types ≈ 17 per type，κ=0.385 的真实 CI 可能跨越 fair→poor 或 fair→moderate。补充 bootstrap CI 是 straightforward 分析。注：human-LLM agreement (Appendix G) 已有 bootstrap CI，cross-judge calibration 应对齐。\"\n\n- id: \"R23-W6\"\n  summary: \"合成歧义的生态效度——未提供真实企业策略文档的歧义案例\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2（W2）提出，R1 同意但指出这是 matched-pair design 的固有限制。SOPBench replication (+12.6pp) 提供部分支持但也是合成 benchmark。Limitations 已有 acknowledgment 但 Discussion 可更明确讨论 synthetic→real-world gap 的具体 threats。\"\n\n- id: \"R23-M1\"\n  summary: \"NMI 0.23 vs 0.01 的 order of magnitude 表述需要绝对值语境化\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2（W3）提出，R1 rebut（论文已有 Cramér's V=0.45 提供绝对值解读）。分歧：R2 认为主文应更明确注明 NMI=0.23 的绝对水平，R1 认为已足够。建议在主文补充 moderate association 限定词。\"\n\n- id: \"R23-M2\"\n  summary: \"Abstract 信息过载（约 150 词内 6+ 个定量结果）\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2（W4）提出，R1 同意。建议保留 2-3 个核心数字。\"\n\n- id: \"R23-M3\"\n  summary: \"Disambiguation neglect 推断边界需收窄——应区分 internal detection 和 surface behavior\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2（W5）提出，R1 同意方向但指出论文已在 §6.2 末句和 Limitations 做了类似限定（behavioral rather than capacity-limited）。建议在 §6.2 首次定义处加入 surface/externally expressed 限定词。\"\n\n- id: \"R23-M4\"\n  summary: \"Table 2 Overall 行应增加 Overall (excl. Incomp.) 或脚注标注\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2（M1）提出，R1 同意。排除 incompleteness 后 pooled effect (+31.0pp) 已在 §5.1 文本中报告，放入 Table 2 更直观。\"\n\n- id: \"R23-M5\"\n  summary: \"Token count 作为 incompleteness confound control 是粗糙 proxy\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1（W4）提出，R2 同意但认为实操中 semantic-level 度量难以定义。建议承认局限性但不需计算新度量。auth scope token delta (+36.1) > incompleteness (+34.6) 但违规率更低，是有力反证据。\"\n\n# ============================================================\n# R22 ISSUES — ALL RESOLVED (from prior round)\n# ============================================================\n\n- id: \"R22-W1\"\n  summary: \"C4 model×type 交互完全由 authorization scope 驱动，该类型测量不可靠（κ=0.385, ICC≈0），C4 可能是测量伪影\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Removed C4 subsection; compressed to 1 caveat paragraph explicitly framing C4 as possibly reflecting measurement instability.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R1 提出（W2），R2 完全同意。\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23 两位 Reviewer 确认 C4 在当前版本中仍被标注为 exploratory/suggestive only（§5 C4 段）。但 R23-N2 指出 auth scope 的不可靠性标注在主分析中仍不够显著。\"\n\n- id: \"R22-W2\"\n  summary: \"SOPBench 复制效应压缩 63%（34.0pp→12.6pp），缺乏原则性归因\"\n  category: experiment\n  severity: warning\n  status: resolved\n  resolution: \"Added principled framing in §5.1 and structured attribution in Appendix SOPBench section.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-W3\"\n  summary: \"ICC 复制仅覆盖 OpenAI 家族，但残差方差分解应用于所有模型\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Added OpenAI-family qualifier in §5.1 and Limitations §Scope.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23 两位 Reviewer 认为当前限定仍不够——主文 §5.1 和 §7 引用 stochastic/systematic split 时仍未逐次注明 OpenAI-family estimate（R23-W3）。\"\n\n- id: \"R22-W4\"\n  summary: \"SESOI ±15pp 缺乏领域接地论证，为统计驱动而非领域驱动\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Added explicit acknowledgment in §4.6.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23 两位 Reviewer 认为当前 §4.6 的表述仍暗示 principled justification（引用 Lakens 2017），需更明确承认 pragmatic 选择（R23-W4）。\"\n\n- id: \"R22-W5\"\n  summary: \"Token count 作为 incompleteness information-addition confound 代理过于粗糙\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Confound caveat added to §6.3 and Limitations §Confounds.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-M5 重新提出，但降级为 minor（论文已有多角度 confound control）。\"\n\n- id: \"R22-W6\"\n  summary: \"残差方差（60.8%）的干预天花板讨论不够充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Added intervention ceiling paragraph in Discussion §7.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M1\"\n  summary: \"生态效度缺口未量化——合成刺激与真实策略文档歧义的差距未知\"\n  category: framing\n  severity: minor\n  status: resolved\n  resolution: \"Added dose-response study suggestion and SOPBench lower bound in Limitations.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W6 重新提出（warning 级别），认为 Limitations 已有 acknowledgment 但 Discussion 需更明确讨论 synthetic→real-world gap 的具体 threats。\"\n\n- id: \"R22-M2\"\n  summary: \"层级结构（linguistic vs specification）C3 未通过 Holm-Bonferroni 校正\"\n  category: framing\n  severity: minor\n  status: resolved\n  resolution: \"Already addressed: §5.2 explicitly states organizational convenience rather than empirical claim.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M3\"\n  summary: \"人工 failure-mode 编码验证缺失\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"Limitations §Measurement states validation underway.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M4\"\n  summary: \"Table 2/Figure 2 中 incompleteness 应标注 confound status\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added dagger marker and footnote in Table 2.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M5\"\n  summary: \"Conclusion 偏短\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added diagnostic protocol and disambiguation neglect summary.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22"
  }
}
```

</details>

---


### Tool result

_source line 2054 · 2026-05-23T05:33:38.914487+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 10245}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2055 · 2026-05-23T05:36:00.848970+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "# Round 23 审稿报告 — Policy Ambiguity Is Nocuous\n\n**Venue**: EMNLP 2026 via ARR May cycle | **Deadline**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文在 τ²-bench 上构建 300 对 matched-pair 歧义/无歧义策略条款，通过六类型×两层分类体系评估五个模型（附加两个 replication family），证明策略歧义在合成条件下使 LLM agent 安全违规率增加 34.0 pp（排除 confounded incompleteness 类型后 +18.7 至 +36.0 pp，pooled +31.0 pp）。方差分解发现条款措辞解释 22.4% 方差 vs 类型仅 0.4%，但类型对失败机制的预测能力远强于对违规率的预测（NMI = 0.23 vs 0.01）。这是一项方法论扎实的因果研究，C1 核心发现跨 7 个模型和 2 个 benchmark 稳健复制，但正文超页、authorization scope 类型不可靠性、以及生态效度限制是主要障碍。\n\n---\n\n## Strengths\n\n**S1. Matched-pair causal design 是首次用于 agent safety evaluation 的方法论贡献** [R1, R2 一致]\n与 DRIP-R（观察性设计）和 MANTRA（SMT 形式化验证）相比，minimal-edit 配对设计在 clause level 建立歧义→违规的因果联系。Perturbation control（n=300, Δ=-0.67pp, CI containing zero）确认语义歧义特异性。\n\n**S2. C1 核心发现极其稳健** [R1, R2 一致]\n+34.0pp 效应跨 5 主模型 + 2 replication families（7 models, 6 providers）一致显著。排除任何单一类型均不影响 C1。排除 incompleteness 后仍有 +31.0pp（p < 10⁻⁷⁵）。SOPBench 跨基准复制 (+12.6pp) 方向一致。Severity threshold robustness 确认。\n\n**S3. Variance decomposition 发现具有实用价值** [R1, R2 一致]\n条款措辞 22.4% vs 类型 0.4%——intervention 应针对具体条款而非歧义类别。Type-mechanism mapping（NMI=0.23, Cramér's V=0.45）将诊断建议落地到具体 failure mode。\n\n**S4. 统计方法选择审慎且全面** [R1, R2 一致]\nMcNemar's test、TOST equivalence、Type III SS、ICC、bootstrap clustering、Holm-Bonferroni 在三个预注册测试族内校正——每种方法适合对应分析。\n\n**S5. 高度透明的 limitation disclosure** [R1, R2 一致]\n论文主动披露 ρ=0.09 cross-judge concordance、auth scope 低 κ、OpenAI-only ICC decomposition 等对自己不利的数据。但 disclosure ≠ adequate handling——R1 和 R2 的共同观察是论文承认了问题但未充分调整 claim 强度。\n\n**S6. Error analysis 超越纯 measurement** [R2]\nDisambiguation neglect（overall awareness 仅 4.6%，Qwen3/DeepSeek 为零）和 systematic nocuity（41.3% convergent violations）对 agent deployment 设计有实际意义。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical] 正文超 8 页限制** [R1 + R2 共识]\nDiscussion（§7）从 p8 延伸到 p9，Conclusion（§8）也在 p9 上半部分。正文（Abstract 到 Conclusion）约 8.4-8.5 页，超出 EMNLP 2026 long paper 严格 8 页限制。视觉审查 Agent 独立确认。可能导致 desk rejection。\n→ 压缩 Discussion（三段→两段）或将部分 §6 Analysis 移入 Appendix。\n\n**N2 [critical] Authorization scope 类型系统性不可靠，动摇 C2/C4 claims** [R1 + R2 共识]\n五个独立指标同时指向不可靠：(1) κ=0.385（六类型最低）；(2) per-type ICC≈0；(3) 单独驱动跨 judge 组 ρ=0.09→排除后 0.90；(4) 单独驱动 C4 interaction（排除后 p=0.97）；(5) 52pp 跨模型方差。但 Table 2 和主分析中无显著区分标记。\n→ Table 2 增加警告标注；C2 中将 auth scope 标记为 unreliable；系统性报告 excluding auth scope 后的 C2 结论。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [major] Incompleteness confound 在 headline claim 中标注不够显著** [R2 提出, R1 部分 rebut]\nAbstract 中 \"34.0 pp (+18.7 to +36.0 pp excluding...)\" 将 confound-free range 置于括号内。R1 指出排除 incompleteness 后 pooled effect 为 +31.0pp（仅差 3pp），认为是 framing 问题而非 validity 问题。\n→ 建议在 Abstract 中将 +31.0pp (excl. incompleteness) 放在更显著位置。Table 2 增加 \"Overall (excl. Incomp.)\" 行。\n\n**W2 [major] ρ=0.09→0.90 的 post-hoc 排除叙述** [R1 + R2 共识]\n排除 1/6 类型后从 ρ=0.09 到 ρ=0.90——即使有理论理由，这在审稿中会被高度怀疑。Three-family validation（ρ=0.71–0.89, Appendix W）是更强且不依赖 post-hoc exclusion 的证据，但仅在 Appendix。\n→ 将 three-family validation 提升到主文作为 primary evidence；排除分析标记为 sensitivity check。\n\n**W3 [major] Residual variance decomposition 的 OpenAI-only 限制** [R1 提出, R2 同意 with nuance]\n15% stochastic + 46% systematic 来自 OpenAI family ICC(1) replication。§5.1 和 §7 在引用时未逐次注明。R2 指出 ICC(3,1)=0.919 是全模型指标（C1 稳健性不受影响），stochastic/systematic split 的 OpenAI-only 限制是 labeling issue。\n→ 主文每次引用 stochastic/systematic split 时注明 \"OpenAI-family estimate\"。\n\n**W4 [major] TOST ±15pp SESOI justification 有 pragmatic 成分** [R1 + R2 共识]\n标准 (2) 本质上是主观判断。±10pp 时仅 3/15 pairs 等价，SESOI 选择对 C2 cluster structure 结论有实质影响。\n→ 明确承认 pragmatic 选择而非 objectively principled；将 bootstrap clustering 提升为与 TOST 并列的主要证据。\n\n**W5 [major] Cross-judge per-type κ 缺少 bootstrap CI** [R1 + R2 共识]\n100 episodes / 6 types ≈ 17 per type。κ=0.385 for auth scope 可能有 ±0.2–0.3 的 CI。Human-LLM agreement (Appendix G) 已有 bootstrap CI，cross-judge calibration 应对齐。\n→ 补充 per-type cross-judge κ 的 bootstrap CI。\n\n**W6 [warning] 合成歧义的生态效度** [R2 提出, R1 同意但认为是固有限制]\n所有 300 clause pairs 均模板合成。SOPBench 也是合成 benchmark。未提供真实企业策略文档歧义案例。R1 指出 matched-pair design 本质上需要合成操控。\n→ Discussion 中更明确讨论 synthetic→real-world gap 的具体 threats（如真实歧义的上下文依赖性更强）。\n\n### Minor（不影响接收）\n\n**M1.** NMI=0.23 vs 0.01 的 \"order of magnitude\" 表述——比较层面准确（23×），但绝对值仍是 moderate association。建议补充 \"moderate association in absolute terms\" 限定。[R2 提出, R1 rebut; 降级 minor]\n\n**M2.** Abstract 信息过载——约 150 词内 6+ 个定量结果。建议保留 2-3 个核心数字。[R1 + R2 共识]\n\n**M3.** Disambiguation neglect 推断边界——应区分 internal detection 和 surface behavior。§6.2 首次定义处加入 \"surface\" 限定词。[R1 + R2 共识]\n\n**M4.** Table 2 \"Overall\" 行增加 \"Overall (excl. Incomp.)\" 或脚注。[R1 + R2 共识]\n\n**M5.** Token count 作为 confound proxy 粗糙——承认局限性即可，不需新度量。[R1 + R2 共识]\n\n**M6.** §4.3 \"five architecturally diverse models\" 表述——GPT-5.4 和 GPT-4.1 同属 OpenAI，改为 \"five models from four providers\"。[R2]\n\n**M7.** References 格式——部分 arXiv 引用 submission date 写法不统一。[R2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **C1 是稳健的、可达 Conference 水平的贡献**——matched-pair causal design + 跨 7 模型 + 跨 2 benchmark 复制\n2. **正文超 8 页是必须修复的硬性问题**——EMNLP 2026 desk rejection 风险\n3. **Authorization scope 不可靠性是核心方法论问题**——五个独立指标同时指向，需在 C2/C4 claim 中实质性调整\n4. **ρ=0.09→0.90 的排除分析有 post-hoc 嫌疑**——three-family validation 应提升到主文\n5. **TOST ±15pp 是 pragmatic 选择**——需更透明承认\n6. **论文透明度值得肯定**——但 disclosure ≠ adequate claim adjustment\n\n## Reviewer Divergence [REBUT]\n\n1. **Incompleteness confound severity**: R2 评 critical → R1 以数据 rebut（排除后 pooled +31.0pp，仅差 3pp）→ 共识降级为 should-fix (framing 问题)\n2. **Variance decomposition severity**: R1 评 critical → R2 认为是 labeling issue（ICC(3,1)=0.919 是全模型指标）→ 共识降级为 should-fix\n3. **NMI \"order of magnitude\" 表述**: R2 评 minor-major → R1 rebut（已有 Cramér's V=0.45）→ 降级 minor\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** Perturbation control CI [-8.0, 6.67] pp 对 5pp true effect 的统计功效是多少？[R1]\n**Q2.** Type III SS variance decomposition 的完整模型公式是什么？是否包含 random effects？[R1]\n**Q3.** Auth scope per-type cross-judge κ=0.385 的 bootstrap 95% CI 是多少？[R1, R2]\n**Q4.** 是否计算过跨 provider 的 reproducibility 度量？[R1]\n**Q5.** NMI 在 failure mechanism 分布高度不均衡时是否是合适度量？[R1]\n**Q6.** Bootstrap clustering modal partition 仅 34.3%（AU=0.47），更高 k 值的 partition stability 如何？[R1]\n**Q7.** 歧义条款注入点的选择标准是什么？注入位置是否引入系统性偏差？[R2]\n**Q8.** 是否考虑过将 incompleteness 从 taxonomy 中独立出来？[R2]\n**Q9.** Mitigation instruction quality 本身是否是 confound？[R2]\n\n---\n\n## Missing References\n\n- **Enhancing LLM Agent Safety via Causal Influence Prompting** (2026, arXiv:2507.00979)——causal 方法 + agent safety，与本文方法论框架直接相关 [R2 提出，需验证真实性]\n- 论文 Related Work 整体覆盖较好，已引用 DRIP-R、PolicyBank、MANTRA、OpenAgentSafety、SOPBench 等主要并发工作\n\n---\n\n## External Review\n\n**状态**: 未配置\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 已完成（0 critical, 2 warning, 18 info）\n\n关键发现：\n- **[warning] Pages 4-5**: 连续 2 页纯文本（§4 Method），无 display item 穿插。插入 method 示意图或 matched-pair 构造示例会改善阅读节奏。\n- **[warning] Page 7**: 单页堆叠 3 个 display items（Table 2 + Figure 3 + Figure 4），密度过高。建议将 Figure 3/4 合并为双面板或分散到相邻页。\n- **[info] Pages 1-9**: 正文约 7 个 display items（~0.78/页），密度合理偏紧凑。\n- **[info] Page 7**: Figure 3 和 Figure 4 尺寸偏小，axis label 字号接近可读下限。\n- **[info]** 正文（Sections 1-8）延伸至 page 9，**与两位 Reviewer 独立确认的超页问题一致**。\n- **[info]** 无内容溢出 margin、无 LaTeX 错误残留、无 [?] 未解析引用、无 section heading 孤悬。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**置信度**: 4/5（两位 Reviewer 独立给出相同评分，交叉回应后无变化）\n\n**理由**:\n- **C1 贡献可达 Conference 水平**：matched-pair causal design 在 agent safety 领域是首次；+34.0pp 效应（confound-free +31.0pp）跨 7 模型稳健复制；variance decomposition 和 type-mechanism mapping 有实用价值。\n- **阻碍升至 4.0 的因素**：(1) 正文超 8 页（desk rejection 风险）；(2) authorization scope 不可靠性未充分反映在 claim 中；(3) 类型层面分析（C2-C4）的 claim 强度与证据不完全匹配。\n- **如果 N1（页数）和 N2（auth scope 标注）能妥善解决**——这主要是 claim qualification 和排版压缩，不需要新实验——**论文可达 Conference (4.0) 水平**。\n\n**ARR 评分标准对照**: 3.5 = Borderline Conference，意味着论文有 Conference 水平的方法论贡献，但需要在格式合规和 claim 校准上做出修改才能被主会议接收。\n\n---\n\n## Detailed Comments（按章节）\n\n### Abstract\n- 信息密度偏高（6+ 个数字）；建议精简至 3 个核心数字\n- \"+34.0 pp (+18.7 to +36.0 pp excluding...)\" 的括号标注不够显著；建议将 +31.0pp (excl. incompleteness) 放在更显著位置\n- \"systematic nocuity: over 40% of clauses triggering model-convergent violations\" 是有效的 anchor point\n\n### §1 Introduction\n- Figure 1 placement（page 2 顶部）合理\n- Opening example（$200 退款场景）有效建立 motivation\n- Contribution (2) 的 \"order of magnitude\" 可加 \"moderate association\" 限定\n\n### §2 Related Work\n- 覆盖全面，已引用主要并发工作（DRIP-R, PolicyBank, AgentPex, MANTRA）\n- Appendix L 的 DRIP-R 对比分析充分\n\n### §3 Taxonomy\n- 六类型选择的三项 design criteria（attestation + minimal-pair + mutual exclusivity）有说服力\n- \"Scope of 'ambiguity'\" 段对 inclusive definition 的论证合理\n- C3 layer effect 已正确标注为 organizational convenience\n\n### §4 Method\n- Matched-pair design 严谨\n- Cross-judge calibration（§4.4）需补充 per-type κ 的 bootstrap CI\n- SESOI ±15pp（§4.6）需更透明承认 pragmatic 选择\n\n### §5 Results\n- C1 证据充分\n- C2 partial ordering 需更谨慎处理 auth scope\n- ρ=0.09 的主文呈现需调整——three-family validation 应提升为 primary evidence\n- C4 已正确标注为 exploratory/suggestive only\n\n### §6 Analysis\n- Type-mechanism mapping（§6.1）是有价值的 exploratory finding\n- Disambiguation neglect（§6.2）需在定义处加 \"surface\" 限定词\n- Systematic nocuity（§6.3）发现具有实际意义\n\n### §7 Discussion\n- 需要压缩（当前占用过多页面导致超限）\n- \"Taxonomy as diagnostic tool\" 段与 §6.1 有部分重叠\n- Intervention ceiling 讨论（22.4% vs 60.8% residual）已到位\n\n### §8 Conclusion\n- 长度适中\n- Confound-free range 已呈现\n\n### Limitations\n- 覆盖 5 个方面（ecological validity, scope, measurement, confounds, disambiguation channel）\n- 符合 EMNLP 2026 要求（不计入页数）\n- 透明度值得肯定\n\n### Appendix\n- 内容丰富（15+ 表，多项 supplementary analysis）\n- 格式统一（booktabs, 一致精度）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "report": "# Round 23 审稿报告 — Policy Ambiguity Is Nocuous\n\n**Venue**: EMNLP 2026 via ARR May cycle | **Deadline**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文在 τ²-bench 上构建 300 对 matched-pair 歧义/无歧义策略条款，通过六类型×两层分类体系评估五个模型（附加两个 replication family），证明策略歧义在合成条件下使 LLM agent 安全违规率增加 34.0 pp（排除 confounded incompleteness 类型后 +18.7 至 +36.0 pp，pooled +31.0 pp）。方差分解发现条款措辞解释 22.4% 方差 vs 类型仅 0.4%，但类型对失败机制的预测能力远强于对违规率的预测（NMI = 0.23 vs 0.01）。这是一项方法论扎实的因果研究，C1 核心发现跨 7 个模型和 2 个 benchmark 稳健复制，但正文超页、authorization scope 类型不可靠性、以及生态效度限制是主要障碍。\n\n---\n\n## Strengths\n\n**S1. Matched-pair causal design 是首次用于 agent safety evaluation 的方法论贡献** [R1, R2 一致]\n与 DRIP-R（观察性设计）和 MANTRA（SMT 形式化验证）相比，minimal-edit 配对设计在 clause level 建立歧义→违规的因果联系。Perturbation control（n=300, Δ=-0.67pp, CI containing zero）确认语义歧义特异性。\n\n**S2. C1 核心发现极其稳健** [R1, R2 一致]\n+34.0pp 效应跨 5 主模型 + 2 replication families（7 models, 6 providers）一致显著。排除任何单一类型均不影响 C1。排除 incompleteness 后仍有 +31.0pp（p < 10⁻⁷⁵）。SOPBench 跨基准复制 (+12.6pp) 方向一致。Severity threshold robustness 确认。\n\n**S3. Variance decomposition 发现具有实用价值** [R1, R2 一致]\n条款措辞 22.4% vs 类型 0.4%——intervention 应针对具体条款而非歧义类别。Type-mechanism mapping（NMI=0.23, Cramér's V=0.45）将诊断建议落地到具体 failure mode。\n\n**S4. 统计方法选择审慎且全面** [R1, R2 一致]\nMcNemar's test、TOST equivalence、Type III SS、ICC、bootstrap clustering、Holm-Bonferroni 在三个预注册测试族内校正——每种方法适合对应分析。\n\n**S5. 高度透明的 limitation disclosure** [R1, R2 一致]\n论文主动披露 ρ=0.09 cross-judge concordance、auth scope 低 κ、OpenAI-only ICC decomposition 等对自己不利的数据。但 disclosure ≠ adequate handling——R1 和 R2 的共同观察是论文承认了问题但未充分调整 claim 强度。\n\n**S6. Error analysis 超越纯 measurement** [R2]\nDisambiguation neglect（overall awareness 仅 4.6%，Qwen3/DeepSeek 为零）和 systematic nocuity（41.3% convergent violations）对 agent deployment 设计有实际意义。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical] 正文超 8 页限制** [R1 + R2 共识]\nDiscussion（§7）从 p8 延伸到 p9，Conclusion（§8）也在 p9 上半部分。正文（Abstract 到 Conclusion）约 8.4-8.5 页，超出 EMNLP 2026 long paper 严格 8 页限制。视觉审查 Agent 独立确认。可能导致 desk rejection。\n→ 压缩 Discussion（三段→两段）或将部分 §6 Analysis 移入 Appendix。\n\n**N2 [critical] Authorization scope 类型系统性不可靠，动摇 C2/C4 claims** [R1 + R2 共识]\n五个独立指标同时指向不可靠：(1) κ=0.385（六类型最低）；(2) per-type ICC≈0；(3) 单独驱动跨 judge 组 ρ=0.09→排除后 0.90；(4) 单独驱动 C4 interaction（排除后 p=0.97）；(5) 52pp 跨模型方差。但 Table 2 和主分析中无显著区分标记。\n→ Table 2 增加警告标注；C2 中将 auth scope 标记为 unreliable；系统性报告 excluding auth scope 后的 C2 结论。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [major] Incompleteness confound 在 headline claim 中标注不够显著** [R2 提出, R1 部分 rebut]\nAbstract 中 \"34.0 pp (+18.7 to +36.0 pp excluding...)\" 将 confound-free range 置于括号内。R1 指出排除 incompleteness 后 pooled effect 为 +31.0pp（仅差 3pp），认为是 framing 问题而非 validity 问题。\n→ 建议在 Abstract 中将 +31.0pp (excl. incompleteness) 放在更显著位置。Table 2 增加 \"Overall (excl. Incomp.)\" 行。\n\n**W2 [major] ρ=0.09→0.90 的 post-hoc 排除叙述** [R1 + R2 共识]\n排除 1/6 类型后从 ρ=0.09 到 ρ=0.90——即使有理论理由，这在审稿中会被高度怀疑。Three-family validation（ρ=0.71–0.89, Appendix W）是更强且不依赖 post-hoc exclusion 的证据，但仅在 Appendix。\n→ 将 three-family validation 提升到主文作为 primary evidence；排除分析标记为 sensitivity check。\n\n**W3 [major] Residual variance decomposition 的 OpenAI-only 限制** [R1 提出, R2 同意 with nuance]\n15% stochastic + 46% systematic 来自 OpenAI family ICC(1) replication。§5.1 和 §7 在引用时未逐次注明。R2 指出 ICC(3,1)=0.919 是全模型指标（C1 稳健性不受影响），stochastic/systematic split 的 OpenAI-only 限制是 labeling issue。\n→ 主文每次引用 stochastic/systematic split 时注明 \"OpenAI-family estimate\"。\n\n**W4 [major] TOST ±15pp SESOI justification 有 pragmatic 成分** [R1 + R2 共识]\n标准 (2) 本质上是主观判断。±10pp 时仅 3/15 pairs 等价，SESOI 选择对 C2 cluster structure 结论有实质影响。\n→ 明确承认 pragmatic 选择而非 objectively principled；将 bootstrap clustering 提升为与 TOST 并列的主要证据。\n\n**W5 [major] Cross-judge per-type κ 缺少 bootstrap CI** [R1 + R2 共识]\n100 episodes / 6 types ≈ 17 per type。κ=0.385 for auth scope 可能有 ±0.2–0.3 的 CI。Human-LLM agreement (Appendix G) 已有 bootstrap CI，cross-judge calibration 应对齐。\n→ 补充 per-type cross-judge κ 的 bootstrap CI。\n\n**W6 [warning] 合成歧义的生态效度** [R2 提出, R1 同意但认为是固有限制]\n所有 300 clause pairs 均模板合成。SOPBench 也是合成 benchmark。未提供真实企业策略文档歧义案例。R1 指出 matched-pair design 本质上需要合成操控。\n→ Discussion 中更明确讨论 synthetic→real-world gap 的具体 threats（如真实歧义的上下文依赖性更强）。\n\n### Minor（不影响接收）\n\n**M1.** NMI=0.23 vs 0.01 的 \"order of magnitude\" 表述——比较层面准确（23×），但绝对值仍是 moderate association。建议补充 \"moderate association in absolute terms\" 限定。[R2 提出, R1 rebut; 降级 minor]\n\n**M2.** Abstract 信息过载——约 150 词内 6+ 个定量结果。建议保留 2-3 个核心数字。[R1 + R2 共识]\n\n**M3.** Disambiguation neglect 推断边界——应区分 internal detection 和 surface behavior。§6.2 首次定义处加入 \"surface\" 限定词。[R1 + R2 共识]\n\n**M4.** Table 2 \"Overall\" 行增加 \"Overall (excl. Incomp.)\" 或脚注。[R1 + R2 共识]\n\n**M5.** Token count 作为 confound proxy 粗糙——承认局限性即可，不需新度量。[R1 + R2 共识]\n\n**M6.** §4.3 \"five architecturally diverse models\" 表述——GPT-5.4 和 GPT-4.1 同属 OpenAI，改为 \"five models from four providers\"。[R2]\n\n**M7.** References 格式——部分 arXiv 引用 submission date 写法不统一。[R2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **C1 是稳健的、可达 Conference 水平的贡献**——matched-pair causal design + 跨 7 模型 + 跨 2 benchmark 复制\n2. **正文超 8 页是必须修复的硬性问题**——EMNLP 2026 desk rejection 风险\n3. **Authorization scope 不可靠性是核心方法论问题**——五个独立指标同时指向，需在 C2/C4 claim 中实质性调整\n4. **ρ=0.09→0.90 的排除分析有 post-hoc 嫌疑**——three-family validation 应提升到主文\n5. **TOST ±15pp 是 pragmatic 选择**——需更透明承认\n6. **论文透明度值得肯定**——但 disclosure ≠ adequate claim adjustment\n\n## Reviewer Divergence [REBUT]\n\n1. **Incompleteness confound severity**: R2 评 critical → R1 以数据 rebut（排除后 pooled +31.0pp，仅差 3pp）→ 共识降级为 should-fix (framing 问题)\n2. **Variance decomposition severity**: R1 评 critical → R2 认为是 labeling issue（ICC(3,1)=0.919 是全模型指标）→ 共识降级为 should-fix\n3. **NMI \"order of magnitude\" 表述**: R2 评 minor-major → R1 rebut（已有 Cramér's V=0.45）→ 降级 minor\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** Perturbation control CI [-8.0, 6.67] pp 对 5pp true effect 的统计功效是多少？[R1]\n**Q2.** Type III SS variance decomposition 的完整模型公式是什么？是否包含 random effects？[R1]\n**Q3.** Auth scope per-type cross-judge κ=0.385 的 bootstrap 95% CI 是多少？[R1, R2]\n**Q4.** 是否计算过跨 provider 的 reproducibility 度量？[R1]\n**Q5.** NMI 在 failure mechanism 分布高度不均衡时是否是合适度量？[R1]\n**Q6.** Bootstrap clustering modal partition 仅 34.3%（AU=0.47），更高 k 值的 partition stability 如何？[R1]\n**Q7.** 歧义条款注入点的选择标准是什么？注入位置是否引入系统性偏差？[R2]\n**Q8.** 是否考虑过将 incompleteness 从 taxonomy 中独立出来？[R2]\n**Q9.** Mitigation instruction quality 本身是否是 confound？[R2]\n\n---\n\n## Missing References\n\n- **Enhancing LLM Agent Safety via Causal Influence Prompting** (2026, arXiv:2507.00979)——causal 方法 + agent safety，与本文方法论框架直接相关 [R2 提出，需验证真实性]\n- 论文 Related Work 整体覆盖较好，已引用 DRIP-R、PolicyBank、MANTRA、OpenAgentSafety、SOPBench 等主要并发工作\n\n---\n\n## External Review\n\n**状态**: 未配置\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 已完成（0 critical, 2 warning, 18 info）\n\n关键发现：\n- **[warning] Pages 4-5**: 连续 2 页纯文本（§4 Method），无 display item 穿插。插入 method 示意图或 matched-pair 构造示例会改善阅读节奏。\n- **[warning] Page 7**: 单页堆叠 3 个 display items（Table 2 + Figure 3 + Figure 4），密度过高。建议将 Figure 3/4 合并为双面板或分散到相邻页。\n- **[info] Pages 1-9**: 正文约 7 个 display items（~0.78/页），密度合理偏紧凑。\n- **[info] Page 7**: Figure 3 和 Figure 4 尺寸偏小，axis label 字号接近可读下限。\n- **[info]** 正文（Sections 1-8）延伸至 page 9，**与两位 Reviewer 独立确认的超页问题一致**。\n- **[info]** 无内容溢出 margin、无 LaTeX 错误残留、无 [?] 未解析引用、无 section heading 孤悬。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**置信度**: 4/5（两位 Reviewer 独立给出相同评分，交叉回应后无变化）\n\n**理由**:\n- **C1 贡献可达 Conference 水平**：matched-pair causal design 在 agent safety 领域是首次；+34.0pp 效应（confound-free +31.0pp）跨 7 模型稳健复制；variance decomposition 和 type-mechanism mapping 有实用价值。\n- **阻碍升至 4.0 的因素**：(1) 正文超 8 页（desk rejection 风险）；(2) authorization scope 不可靠性未充分反映在 claim 中；(3) 类型层面分析（C2-C4）的 claim 强度与证据不完全匹配。\n- **如果 N1（页数）和 N2（auth scope 标注）能妥善解决**——这主要是 claim qualification 和排版压缩，不需要新实验——**论文可达 Conference (4.0) 水平**。\n\n**ARR 评分标准对照**: 3.5 = Borderline Conference，意味着论文有 Conference 水平的方法论贡献，但需要在格式合规和 claim 校准上做出修改才能被主会议接收。\n\n---\n\n## Detailed Comments（按章节）\n\n### Abstract\n- 信息密度偏高（6+ 个数字）；建议精简至 3 个核心数字\n- \"+34.0 pp (+18.7 to +36.0 pp excluding...)\" 的括号标注不够显著；建议将 +31.0pp (excl. incompleteness) 放在更显著位置\n- \"systematic nocuity: over 40% of clauses triggering model-convergent violations\" 是有效的 anchor point\n\n### §1 Introduction\n- Figure 1 placement（page 2 顶部）合理\n- Opening example（$200 退款场景）有效建立 motivation\n- Contribution (2) 的 \"order of magnitude\" 可加 \"moderate association\" 限定\n\n### §2 Related Work\n- 覆盖全面，已引用主要并发工作（DRIP-R, PolicyBank, AgentPex, MANTRA）\n- Appendix L 的 DRIP-R 对比分析充分\n\n### §3 Taxonomy\n- 六类型选择的三项 design criteria（attestation + minimal-pair + mutual exclusivity）有说服力\n- \"Scope of 'ambiguity'\" 段对 inclusive definition 的论证合理\n- C3 layer effect 已正确标注为 organizational convenience\n\n### §4 Method\n- Matched-pair design 严谨\n- Cross-judge calibration（§4.4）需补充 per-type κ 的 bootstrap CI\n- SESOI ±15pp（§4.6）需更透明承认 pragmatic 选择\n\n### §5 Results\n- C1 证据充分\n- C2 partial ordering 需更谨慎处理 auth scope\n- ρ=0.09 的主文呈现需调整——three-family validation 应提升为 primary evidence\n- C4 已正确标注为 exploratory/suggestive only\n\n### §6 Analysis\n- Type-mechanism mapping（§6.1）是有价值的 exploratory finding\n- Disambiguation neglect（§6.2）需在定义处加 \"surface\" 限定词\n- Systematic nocuity（§6.3）发现具有实际意义\n\n### §7 Discussion\n- 需要压缩（当前占用过多页面导致超限）\n- \"Taxonomy as diagnostic tool\" 段与 §6.1 有部分重叠\n- Intervention ceiling 讨论（22.4% vs 60.8% residual）已到位\n\n### §8 Conclusion\n- 长度适中\n- Confound-free range 已呈现\n\n### Limitations\n- 覆盖 5 个方面（ecological validity, scope, measurement, confounds, disambiguation channel）\n- 符合 EMNLP 2026 要求（不计入页数）\n- 透明度值得肯定\n\n### Appendix\n- 内容丰富（15+ 表，多项 supplementary analysis）\n- 格式统一（booktabs, 一致精度）"
  }
}
```

</details>

---


### Tool result

_source line 2056 · 2026-05-23T05:36:05.012744+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4163
}
```

</details>

---


### Assistant

_source line 2057 · 2026-05-23T05:36:15.451914+00:00_

**Round 23 审稿报告已投递至 Research Director。**

审稿结果摘要：

- **Overall: 3.5（Borderline Conference）**，两位 Reviewer 独立评分一致，交叉回应后未变
- **2 个 critical**：正文超 8 页（desk rejection 风险）；authorization scope 类型系统性不可靠但主分析未充分标注
- **6 个 should-fix**：incompleteness confound framing、ρ=0.09 post-hoc 排除叙述、variance decomposition OpenAI-only 限定、TOST ±15pp pragmatic 成分、per-type κ 缺 CI、生态效度
- **7 个 minor**：NMI 绝对值语境化、abstract 信息密度、disambiguation neglect 推断边界等
- **核心判断**：C1 贡献可达 Conference 水平；若 N1（页数）和 N2（auth scope 标注）妥善解决——主要是 claim qualification 和排版压缩，不需要新实验——论文可达 4.0（Conference）

Review issues tracker 已同步更新（13 条 open issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 196

## Round 196

2 recorded events


### User

_source line 2058 · 2026-05-23T05:36:18.026487+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。主要结论：

- 与 R1 在 auth scope 不可靠性（N1）、ρ=0.09 post-hoc 排除（W2）、页数超限（W5）上高度一致
- 对 N2（variance decomposition OpenAI-only）同意关切但认为严重程度稍低——ICC(3,1)=0.919 跨全部模型是 strong evidence，OpenAI-only 是 labeling 问题
- 反驳 FLASK 作为 missing reference——该论文评估 output quality 多维度，与本文的 binary violation classification 目标不同
- 两位 reviewer 共识：C1 稳健可达 Conference 水平，但 C2/C4 需因 auth scope 问题实质性降级 claim

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2059 · 2026-05-23T05:36:33.411609+00:00_

审稿报告已投递至 Research Director。

**Round 23 审稿完成。**

最终评分：**3.5 — Borderline Conference**（两位 Reviewer 独立评分一致，交叉回应后未变化）

核心结论：
- **2 个 Must-Fix**：正文超 8 页（desk rejection 风险）；authorization scope 不可靠性需在 C2/C4 claim 中实质性标注
- **6 个 Should-Fix**：incompleteness confound framing、ρ=0.09 post-hoc 叙述、variance decomposition OpenAI-only 限定、TOST ±15pp pragmatic 承认、per-type κ 补 CI、生态效度讨论
- **7 个 Minor**：NMI 绝对值限定、abstract 精简、disambiguation neglect 推断边界、Table 2 excl. row 等
- **升级路径**：N1（页数）和 N2（auth scope 标注）主要是 claim qualification 和排版压缩，不需要新实验，解决后可达 **Conference (4.0)**

Review issues tracker 已同步更新（13 个 open issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 197

## Round 197

52 recorded events


### User

_source line 2060 · 2026-05-23T08:14:03.372084+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2061 · 2026-05-23T08:14:10.915421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2062 · 2026-05-23T08:14:10.968706+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 2063 · 2026-05-23T08:14:25.349348+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2064 · 2026-05-23T08:14:25.400103+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2065 · 2026-05-23T08:14:30.873124+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2066 · 2026-05-23T08:14:31.375550+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2067 · 2026-05-23T08:14:31.877927+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2068 · 2026-05-23T08:14:31.878331+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2069 · 2026-05-23T08:14:32.380505+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2070 · 2026-05-23T08:14:33.786193+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 2071 · 2026-05-23T08:14:34.289073+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2072 · 2026-05-23T08:14:34.640726+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\makeatletter
41	\newcommand{\extAlph}[1]{%
42	  \ifcase#1\or A\or B\or C\or D\or E\or F\or G\or H\or I\or J\or K\or L\or M\or N\or O\or P\or Q\or R\or S\or T\or U\or V\or W\or X\or Y\or Z\or AA\or AB\or AC\or AD\or AE\fi}
43	\renewcommand{\thesection}{\extAlph{\value{section}}}
44	\makeatother
45	\input{sections/appendix}
46	
47	\end{document}
48	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2073 · 2026-05-23T08:14:34.641043+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "review_issues.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 2074 · 2026-05-23T08:14:34.741618+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2075 · 2026-05-23T08:14:39.711335+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 2076 · 2026-05-23T08:14:40.615095+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2077 · 2026-05-23T08:14:40.615468+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2078 · 2026-05-23T08:14:42.472978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2079 · 2026-05-23T08:14:42.674119+00:00_

1	\begin{abstract}
2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. We present a matched-pair causal study on $\tau^2$-bench with 300 ambiguous/unambiguous clause pairs spanning a six-type taxonomy, evaluated across five models. Ambiguous clauses are consistently nocuous (i.e., harmful), increasing violation rates by 34.0 percentage points ($+$18.7 to $+$36.0\,pp in confound-free types). Clause wording explains 22.4\% of violation variance; however, type predicts failure \emph{mechanism} more strongly than violation rate, establishing the taxonomy as a diagnostic tool. Error analysis reveals disambiguation neglect and \emph{systematic nocuity}: models converge on identical policy violations with a systematic permissive bias (77\%). These results, observed in customer-service domains under controlled synthetic ambiguity, motivate clause-level policy auditing and type-targeted diagnosis for policy-governed deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2080 · 2026-05-23T08:14:42.674495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2081 · 2026-05-23T08:14:42.775248+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity---a pilot audit of 407 clauses from 24 production policy documents finds 55--87\% contain at least one ambiguity type (Appendix~\ref{app:prevalence})---a property studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[widt
…[truncated 2139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 2082 · 2026-05-23T08:14:45.987764+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here's what I found regarding EMNLP 2026 call for papers, ARR submission guidelines, and page limits:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

## Submission Deadline and Process

All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026. EMNLP 2026 will use ACL R
…[truncated 843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6276
}
```

</details>

---


### Tool call

_source line 2083 · 2026-05-23T08:14:55.675265+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May submission guidelines anonymity requirements formatting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May submission guidelines anonymity requirements formatting"
  }
}
```

</details>

---


### Tool call

_source line 2084 · 2026-05-23T08:14:57.332267+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2085 · 2026-05-23T08:14:58.186263+00:00_

1	## Review Issues Tracker — policy_ambiguity_safety
2	## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Latest Round: 23
5	
6	# ============================================================
7	# R23 ISSUES — ALL RESOLVED
8	# ============================================================
9	
10	- id: "R23-N1"
11	  summary: "正文超 8 页限制（Discussion+Conclusion 溢出至 p9，约 8.4-8.5 页）"
12	  category: format
13	  severity: critical
14	  status: resolved
15	  resolution: "§5.1 C1 compressed (perturbation→§4 ref, permutation 1-sentence). Discussion merged 3→2 ¶ then further trimmed. Conclusion compressed. Variance decomposition figure moved to Appendix. Visual verification: Conclusion ends on p8, Limitations starts p9."
16	  resolution_round: 23
17	  first_raised_round: 23
18	  last_seen_round: 23
19	
20	- id: "R23-N2"
21	  summary: "Authorization scope 类型系统性不可靠（κ=0.385, ICC≈0, 单独驱动 ρ=0.09 和 C4 interaction），但在主分析中未充分标注"
22	  category: method
23	  severity: critical
24	  status: resolved
25	  resolution: "Table 2: ‡ added to Auth Scope row + footnote ('Interpret with caution: lowest inter-judge agreement κ=0.385'). §5.2: excluding-auth-scope sentence added ('remaining five types preserve same partial ordering')."
26	  resolution_round: 23
27	  first_raised_round: 23
28	  last_seen_round: 23
29	
30	- id: "R23-W1"
31	  summary: "Incompleteness confound 在 headline claim (34.0pp) 中的标注不够显著——framing 问题 [复发×3: R21-W3→R22-M4→R23-W1]"
32	  category: framing
33	  severity: warning
34	  status: resolved
35	  resolution: "Abstract reframed: '+34.0pp (+18.7 to +36.0pp in confound-free types)'. Table 2 footnote added with excl-incomp pooled Δ=+31.0pp."
36	  resolution_round: 23
37	  first_raised_round: 21
38	  last_seen_round: 23
39	
40	- id: "R23-W2"
41	  summary: "跨 judge 组类型排名 ρ=0.09→排除 auth scope 后 ρ=0.90 的 post-hoc 嫌疑 [复发×2: R21-N3→R23-W2]"
42	  category: method
43	  severity: warning
44	  status: resolved
45	
…[truncated 8461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 2086 · 2026-05-23T08:14:58.186801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2087 · 2026-05-23T08:14:58.438482+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300; Cohen's $\kappa = 0.95$ on six-type classification); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We
…[truncated 5234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2088 · 2026-05-23T08:14:58.438884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2089 · 2026-05-23T08:14:58.489434+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around three analyses: the binary ambiguity effect (C1), the type partial ordering (C2, including the inconclusive layer effect C3), and the model$\times$type interaction (C4). C1 and C2 are primary claims; C4 is exploratory.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity (\S\ref{sec:method}). A Type III sum-of-squares decomposition\footnote{Type III SS avoids ordering dependence in our unbalanced design; logistic regression (Appendix~\ref{app:regression}) confirms concordant results (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}).} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (of which $\sim$15\% is stochastic and $\sim$46\% systematic, estimated from an OpenAI-family ICC replication; Appendix~\ref{app:residual}). A permutation test confirms the clause effect exceeds chance ($p < 0.001$; Appendix~\ref{app:clause_variance}). Individual clause wording---not type membership---drives clause-level variance. The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; controlling for token count changes no type's predicted effect by more than 0.1\,pp (Appendix~\ref{app:confound}). The confound-free range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope); excluding incompleteness entirely, the pooled effect is $+$31.0\,pp (95\% CI $[27.9, 34.1]$).
9	
10	Replication on two additional model families confirms the effect across seven models ($\Delta = +20.0$ to $+33.6$\,pp; 
…[truncated 6972 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2090 · 2026-05-23T08:15:05.322412+00:00_

Web search results for query: "ACL Rolling Review 2026 May submission guidelines anonymity requirements formatting"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/authors.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/authors.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

Based on the search results, here's a summary of the ACL Rolling Review 2026 May submission guidelines regarding anonymity requirements and formatting:

## Anonymity Requirements

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)…" must be avoided.

Suppl
…[truncated 1220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 9647
}
```

</details>

---


### Tool call

_source line 2091 · 2026-05-23T08:15:10.978391+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 2092 · 2026-05-23T08:15:14.705286+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes (Gwet's AC$_1$ $= 0.62$, $\kappa = 0.52$ \citep{gwet_2014,cohen_1960}). Using LLMs to code LLM failures introduces circularity risk; however, mutual information between type (exogenous) and mechanism labels ($I(\text{type}; \text{mechanism}) = 0.41$ bits, $V = 0.45$; Appendix~\ref{app:type_mechanism}) provides structural evidence against this. Two of the six type--mechanism mappings reflect partial definitional affinity (authorization scope$\to$boundary violation, incompleteness$\to$gap-filling); the remaining four (e.g., scopal$\to$structural misparse, 82.7\% cross-model consistency) are empirically derived.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse}: the agent commits to an incorrect parse, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}. Dominates scopal (5/5), conditional precedence (4/5), and coreferential (3/5).
13	
14	\emph{Information gap-filling}: the agent fills missing information with plausible but incorrect defaults. Dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation}: the agent exceeds permission boundaries when authorization scope is underspecified; 69.2\% involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial). Dominates authorization scope exclusively (5/5).
17	
18	All dominant modes achieve $\geq$3/5 model consistency; scopal and authorization scope are unanimous (5/5).
19	
20	\begin{figure}[t]
21	\centering
22	\includegraphics[width=\columnwidth]{figures/fig
…[truncated 2796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 3726
}
```

</details>

---


### Tool call

_source line 2093 · 2026-05-23T08:15:14.755875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2094 · 2026-05-23T08:15:14.756333+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity and intervention limits.}
5	Our results support a \emph{differential nocuity} hypothesis \citep{berry_kamsties_2004,willis_nocuous_2008}: the binary effect is domain-robust ($p = 0.187$) but type-specific profiles require per-domain calibration ($\rho = 0.26$). Of the 60.8\% unexplained variance, $\sim$15\% is stochastic and $\sim$46\% systematic (OpenAI-family estimate; ICC $= 0.749$; Appendix~\ref{app:residual}). Even perfect disambiguation would address at most 22.4\% of variance; prompt-based mitigation is type-dependent (Appendix~\ref{app:mitigation}), reinforcing policy-design over prompt-level fixes.
6	
7	\paragraph{Taxonomy as diagnostic tool.}
8	Type membership explains only 0.4\% of violation variance versus 22.4\% for clause wording; however, it predicts failure \emph{mechanism} an order of magnitude more strongly than violation rate (NMI $= 0.23$ vs.\ $0.01$, Cram\'{e}r's $V = 0.45$; Appendix~\ref{app:type_mechanism}), validating the taxonomy as a diagnostic tool (\S\ref{sec:analysis}).
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2095 · 2026-05-23T08:15:14.756604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool call

_source line 2096 · 2026-05-23T08:15:14.756782+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2097 · 2026-05-23T08:15:14.857378+00:00_

1	\section{Conclusion}
2	
3	Under controlled synthetic conditions, policy ambiguity increases agent violations by 34.0\,pp ($+$18.7 to $+$36.0\,pp in confound-free types). The taxonomy predicts failure mechanisms more strongly than violation rate, yielding type-targeted diagnostics (\S\ref{sec:analysis}). With $>$89\% disambiguation neglect and over 40\% convergent violations, clause-level policy auditing is critical for safe deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 2098 · 2026-05-23T08:15:14.857820+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our ambiguity pairs are synthetically constructed, so the 34.0\,pp effect is an upper bound; naturally occurring ambiguity may produce smaller effects (the SOPBench replication under more naturalistic conditions yields $+$12.6\,pp). We evaluate seven API-accessible models across two customer-service domains; smaller open-source models, other domains, and production policy documents with correlated ambiguities remain untested. Cross-judge agreement is substantial overall (Fleiss' $\kappa = 0.717$), but authorization scope shows lower reliability ($\kappa = 0.385$), reflecting inherent construct subjectivity (\S\ref{sec:results}); failure mode coding relies on LLM annotators ($\kappa = 0.52$), with human validation underway for camera-ready.
5	
6	\section*{Data and Code Availability}
7	The 300 clause pairs, evaluation pipeline, analysis scripts, and raw episode traces will be released upon publication at \url{https://github.com/anonymous/policy-ambiguity-safety}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2099 · 2026-05-23T08:15:20.743683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2100 · 2026-05-23T08:15:21.748393+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_l
…[truncated 4154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2101 · 2026-05-23T08:15:21.799247+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 2102 · 2026-05-23T08:15:22.201437+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers (Table~\ref{tab:taxonomy}), selected from \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types) based on three design criteria: (1)~theoretical attestation in prior RE literature \citep{massey_ambiguity_re_2014,berry_kamsties_2004,drip_r_2026}, (2)~amenability to minimal-pair construction without altering clause semantics beyond the target ambiguity, and (3)~mutual exclusivity for unambiguous IV assignment. Types such as ellipsis and pragmatic implicature were excluded because they resist minimal-pair construction within the single-clause policy format.
7	
8	\begin{table}[t]
9	\centering
10	\footnotesize
11	\caption{Six-type ambiguity taxonomy. Disambiguation channel indicates the primary mechanism required to resolve the ambiguity.}
12	\label{tab:taxonomy}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}llll@{}}
15	\toprule
16	\textbf{Type} & \textbf{Layer} & \textbf{Definition} & \textbf{Disambig.\ Channel} \\
17	\midrule
18	Lexical & Ling. & Word/phrase admits multiple senses & Context \\
19	Scopal & Ling. & Quantifier/operator scope underdetermined & Bracketing \\
20	Coreferential & Ling. & Pronoun/NP referent is ambiguous & Resolution \\
21	Auth.\ Scope & Spec. & Permission boundary is vague & Boundary def. \\
22	Incompleteness & Spec. & Required information is absent & Content addition \\
23	Cond.\ Prec. & Spec. & Rules conflict under certain conditions & Priority rule \\
24	\bottomrule
25	\end{tabular}}%
26	\end{table}
27	
28	\paragraph{Linguistic layer.} These types operate at the syntactic or 
…[truncated 2646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2103 · 2026-05-23T08:15:22.352601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2104 · 2026-05-23T08:15:22.705199+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 51608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2105 · 2026-05-23T08:16:06.725844+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- **标题**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n- **Venue**: EMNLP 2026 via ARR (Long Paper)\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板，正文 8 页限（不含 Limitations 和参考文献），double-blind 匿名\n- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_24/submitted.pdf`\n\n## 你的审查侧重\n\n1. **实验设计与因果推断**：matched-pair design 的内部效度，300 clause pairs 的构建质量和覆盖范围，perturbation control 和 reproducibility control 的充分性\n2. **统计分析**：McNemar's test、TOST equivalence、Type III SS variance decomposition、ICC 的使用是否恰当，多重比较校正是否充分，SESOI ±15pp 的 justification\n3. **评估管线可靠性**：cross-judge design 的偏差控制，human validation 的样本量和代表性，authorization scope 低 κ 对结论的影响\n4. **Controls 与 confounds**：incompleteness information-addition confound 的处理，token count 作为 proxy 的局限性，perturbation control 的覆盖面\n5. **可复现性**：模型选择的代表性（5+2 模型），ICC replication 仅限 OpenAI family 的范围限制，SOPBench 效应压缩的归因\n\n## 输出格式\n\n请按以下结构输出：\n```\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级）\n## Questions（需要作者澄清的问题）\n## Missing References（遗漏的重要相关工作）\n## Overall Assessment（评分 + 置信度 + 简要理由）\n```\n\n评分标准（ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n严格评审，不留情面。"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- **标题**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n- **Venue**: EMNLP 2026 via ARR (Long Paper)\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板，正文 8 页限（不含 Limitations 和参考文献），double-blind 匿名\n- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_24/submitted.pdf`\n\n## 你的审查侧重\n\n1. **实验设计与因果推断**：matched-pair design 的内部效度，300 clause pairs 的构建质量和覆盖范围，perturbation control 和 reproducibility control 的充分性\n2. **统计分析**：McNemar's test、TOST equivalence、Type III SS variance decomposition、ICC 的使用是否恰当，多重比较校正是否充分，SESOI ±15pp 的 justification\n3. **评估管线可靠性**：cross-judge design 的偏差控制，human validation 的样本量和代表性，authorization scope 低 κ 对结论的影响\n4. **Controls 与 confounds**：incompleteness information-addition confound 的处理，token count 作为 proxy 的局限性，perturbation control 的覆盖面\n5. **可复现性**：模型选择的代表性（5+2 模型），ICC replication 仅限 OpenAI family 的范围限制，SOPBench 效应压缩的归因\n\n## 输出格式\n\n请按以下结构输出：\n```\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级）\n## Questions（需要作者澄清的问题）\n## Missing References（遗漏的重要相关工作）\n## Overall Assessment（评分 + 置信度 + 简要理由）\n```\n\n评分标准（ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n严格评审，不留情面。"
  }
}
````

</details>

---


### Tool result

_source line 2106 · 2026-05-23T08:16:19.125928+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12400
}
```

</details>

---


### Tool call

_source line 2107 · 2026-05-23T08:16:19.979376+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- **标题**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n- **Venue**: EMNLP 2026 via ARR (Long Paper)\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板，正文 8 页限（不含 Limitations 和参考文献），double-blind 匿名\n- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_24/submitted.pdf`\n\n## 你的审查侧重\n\n1. **贡献新颖性**：与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等并发工作的差异化是否充分？matched-pair causal design 是否真正 novel？taxonomy 的 novelty vs. 已有 RE 分类体系？\n2. **Related Work 覆盖**：是否遗漏重要相关工作？尤其是 agent safety、policy specification、ambiguity detection 领域的最新工作（2025-2026）\n3. **Claims 与 Evidence 对齐**：C1-C4 的 claim 是否被实验充分支撑？variance decomposition 的叙事是否准确反映数据？\"order of magnitude\" 等措辞的精确性\n4. **写作质量**：Abstract 信息密度是否合理？叙事流畅度？术语一致性？图表的信息传达效率？\n5. **格式合规**：\n   - 正文是否在 8 页内（Limitations 不计入）\n   - 是否 double-blind（无作者信息泄露）\n   - ACL 模板使用是否正确\n   - 引用格式一致性\n   - Limitations section 是否存在且充分\n\n## 输出格式\n\n请按以下结构输出：\n```\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级）\n## Questions（需要作者澄清的问题）\n## Missing References（遗漏的重要相关工作）\n## Overall Assessment（评分 + 置信度 + 简要理由）\n```\n\n评分标准（ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n严格评审，不留情面。"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- **标题**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n- **Venue**: EMNLP 2026 via ARR (Long Paper)\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板，正文 8 页限（不含 Limitations 和参考文献），double-blind 匿名\n- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_24/submitted.pdf`\n\n## 你的审查侧重\n\n1. **贡献新颖性**：与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等并发工作的差异化是否充分？matched-pair causal design 是否真正 novel？taxonomy 的 novelty vs. 已有 RE 分类体系？\n2. **Related Work 覆盖**：是否遗漏重要相关工作？尤其是 agent safety、policy specification、ambiguity detection 领域的最新工作（2025-2026）\n3. **Claims 与 Evidence 对齐**：C1-C4 的 claim 是否被实验充分支撑？variance decomposition 的叙事是否准确反映数据？\"order of magnitude\" 等措辞的精确性\n4. **写作质量**：Abstract 信息密度是否合理？叙事流畅度？术语一致性？图表的信息传达效率？\n5. **格式合规**：\n   - 正文是否在 8 页内（Limitations 不计入）\n   - 是否 double-blind（无作者信息泄露）\n   - ACL 模板使用是否正确\n   - 引用格式一致性\n   - Limitations section 是否存在且充分\n\n## 输出格式\n\n请按以下结构输出：\n```\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级）\n## Questions（需要作者澄清的问题）\n## Missing References（遗漏的重要相关工作）\n## Overall Assessment（评分 + 置信度 + 简要理由）\n```\n\n评分标准（ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n严格评审，不留情面。"
  }
}
````

</details>

---


### Tool call

_source line 2108 · 2026-05-23T08:16:19.979781+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 2109 · 2026-05-23T08:16:21.351331+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1371
}
```

</details>

---


### Tool result

_source line 2110 · 2026-05-23T08:16:22.917243+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2937
}
```

</details>

---


### Assistant

_source line 2111 · 2026-05-23T08:16:31.305272+00:00_

Round 1 已启动：
- **Reviewer 1**（方法严谨性）：已分配，独立审稿中
- **Reviewer 2**（新颖性与完整性）：已分配，独立审稿中
- **视觉审查 Agent**：已派发，并行执行中

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 198

## Round 198

2 recorded events


### User

_source line 2112 · 2026-05-23T08:22:20.231893+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告（方法严谨性）

### 论文信息
- **标题**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety
- **Venue**: EMNLP 2026 via ARR (Long Paper)
- **格式检查**: 正文 8 页（pp.1-8），Limitations 在 p.9 不计入页限，References pp.9-10，Appendix pp.11-21。符合 ACL 8 页正文限制。Double-blind 匿名格式正确。

---

## Summary（2-3 句）

本文提出首个 matched-pair 因果研究，在 τ²-bench 上构造 300 组歧义/无歧义条款对（六类分类），评估五个模型在 2,997 个 episode 中的违规率变化。核心发现：歧义条款使违规率增加 34.0 pp（去混淆类型范围 +18.7 至 +36.0 pp），条款措辞解释 22.4% 方差而类型仅 0.4%，但类型对失败机制的预测能力比违规率高一个数量级（NMI = 0.23 vs. 0.01）。论文在实验控制和统计分析方面展现了较高的严谨性，但合成歧义的外部效度、incompleteness 的信息添加混淆、以及失败模式编码缺乏人工验证是主要顾虑。

---

## Strengths（逐条）

**S1. 实验设计严谨的 matched-pair causal design。** 300 clause pairs × 2 conditions × 5 models 的 matched-pair 设计是本文最大的方法论贡献。配对内比较有效隔离了歧义操作的因果效应，消除了条款内容的混淆。两名独立标注者的类型分配初始一致率 96%（κ = 0.95），确保了 IV 分配质量。（§4.2）

**S2. 全面且恰当的统计框架。** McNemar's test 用于配对二分结果、TOST equivalence testing 跨七个 margin 的敏感性分析（Table 3/Appendix A）、Type III SS 方差分解（避免不平衡设计中的排序依赖）、Holm-Bonferroni 多重比较校正——统计工具选择恰当且与研究设计匹配。Bootstrap clustering（B = 10,000）作为 margin-free 补充验证 TOST 结构，方法论上有冗余保障。（§4.6）

**S3. Perturbation control 建立因果特异性。** 300 episodes 的非歧义扰动（同义替换、条款重排）产生 Δ = −0.67 pp（95% CI 含零），有效排除了表面文本变化对结果的解释。worst-case CI bound (6.67 pp) 与主效应 (34.0 pp) 的差距为因果归因提供了定量下界。（§4.5）

**S4. 对方法论局限的异常坦诚。** 论文在 incompleteness 的信息添加混淆、authorization scope 的低 κ（0.385）、ICC 复制仅限 OpenAI 家族、合成刺激的上界性质等方面均主动披露并提供定量分析。多处提供 "excluding X" 的敏感性分析（排除 incompleteness 的 pooled Δ = 31.0 pp，排除 auth scope 的交互消失 p = 0.97），这在同类工作中是少见的。

**S5. Cross-judge validation 深入且多层次。** 三家族交叉验证（Fleiss' κ = 0.717），同家族偏差检验（Claude judge 对 Claude agent 更严格而非更宽松），McNemar's test 排除系统性检测偏差（p = 0.606）。Dual-judge calibration 的设计是合理的。（§4.4, Appendix R）

**S6. Variance decomposition 揭示非直觉发现。** Type III SS 分解显示条款措辞（22.4%）远超类型（0.4%）在解释违规方差中的作用，而类型预测失败机制（NMI = 0.23）比违规率（NMI = 0.01）高 16.8 倍——这一发现重构了分类法的价值定位，从风险预测工具转变为诊断工具。ICC 复制进一步将 60.8% 残差分解为 ~15% 随机 + ~46% 系统性，证明主效应不受随机噪声威胁。（§5.1, Appendix Z）

**S7. 模型覆盖面广。** 五个主研究模型（GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3）+ 两个复制模型（Gemini-2.5-Flash, LLaMA-4-Scout）覆盖六个提供商、两种架构家族（dense + MoE），增强了 C1 的跨架构泛化性。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] 合成歧义与自然歧义的效应差距未充分解释，威胁外部效度**
- 具体位置：§5.1, Appendix X (SOPBench), Limitations
- 问题：主研究效应 +34.0 pp 与 SOPBench 复制效应 +12.6 pp 之间存在 63% 的压缩（并且 SOPBench 上仅 3/5 模型达到统计显著，GPT-5.4 borderline p=0.052，DeepSeek 不显著 p=0.163）。论文将此归因于三个结构性差异（measurement grain、baseline rate compression、interaction depth），但这些归因是 post-hoc 的推测，没有实验分解。如果实际应用中效应大小接近 12.6 pp 而非 34.0 pp，论文的核心 framing（"nocuous"）和实践意义会被大幅削弱。
- 为什么影响接收：因果研究的价值最终取决于其外部效度。Abstract 和 Conclusion 中的 "34.0 pp" 数字在多大程度上代表真实世界效应，读者无法判断。
- 建议修改方向：(1) 在 Abstract/Conclusion 中明确标注 "under controlled synthetic conditions"（目前 Conclusion 已有但 Abstract 仅在文末提及 "customer-service domains under controlled synthetic ambiguity"，措辞可更突出）；(2) 将 SOPBench 的 12.6 pp 作为 lower bound 与 34.0 pp 的 upper bound 对比呈现，而非将其放入 Appendix 作为次要信息；(3) 定量分析三个归因因素中哪个贡献最大（例如通过仅改变 measurement grain 的控制实验）。

**N2 [critical] Incompleteness 的信息添加混淆控制不足以支撑因果主张**
- 具体位置：§5.1, Appendix F (confound analysis)
- 问题：Incompleteness 的无歧义变体必然添加新的策略内容（信息添加），而非仅解消已有歧义。论文用 token count 作为 proxy 控制混淆——logistic regression 显示 token delta 系数为正（β = +0.027, p = 0.003），即更长条款预测更多违规。论文将此解释为 "counter to the information-addition hypothesis"，但这一推理有误：更长的无歧义条款同时添加了更多限制性约束，可能导致代理因约束过多而违规（over-constraint violation），这与信息添加减少歧义的效应方向一致而非相反。Token count 是信息内容的粗糙代理（论文自身承认 "Token count is a coarse proxy"），无法区分"解消歧义的信息"和"增加约束复杂性的信息"。
- 此外，authorization scope 有最大的 token delta（+36.1 words）但低于 incompleteness 的违规率——论文将此作为 counter-evidence，但 auth scope 的低 κ（0.385）和极高跨模型方差（52 pp）使其作为参照物的可靠性本身成疑。
- 为什么影响接收：Incompleteness 是效应最大的类型（+49.2 pp），占总违规的最大比例。如果其效应部分由信息添加而非歧义解消驱动，则 C1 的 headline 数字和 C2 的类型排序均受影响。
- 建议修改方向：(1) 设计一个信息添加控制条件——在无歧义条款基础上添加等量的无关信息（irrelevant policy content），测量其效应是否与添加消歧信息的效应一致；(2) 使用语义相似度或 information-theoretic measures 替代 token count 作为信息内容的 proxy；(3) 至少在 headline 数字中报告 "confound-free range" 作为主要结论（当前已报告 +18.7 至 +36.0 pp，但 34.0 pp 的 pooled 数字仍是 Abstract 首选）。

**N3 [critical] 条款对构建过程不够透明，可复现性受限**
- 具体位置：§4.2
- 问题：300 clause pairs 通过 "template-based pipeline" 生成，但论文未描述：(1) 使用了多少模板？(2) 模板的结构是什么？(3) 模板如何确保覆盖每种歧义类型的内部多样性？(4) 标注过程中有多少候选对被筛除（rejection rate）？(5) "post-hoc realism validation" 的具体方法和结果（§4.2 仅一句带过）。Appendix V 的示例表仅展示每类型一个代表性对，无法评估类型内的变异程度。标注者的高一致率（κ = 0.95）可能反映歧义实例过于典型化，而非自然分布的良好覆盖。
- 为什么影响接收：条款对的构建质量是整个因果推断链条的起点。如果模板过于狭窄，50 对/类型可能无法代表每种歧义类型的全谱系，clause-level variance（22.4%）可能被低估。
- 建议修改方向：(1) 在 Appendix 中完整描述模板设计过程、筛选标准和淘汰率；(2) 展示每种类型 2-3 个 clause pair 的 diversity，覆盖高/中/低效应实例；(3) 描述 "post-hoc realism validation" 的具体协议和指标。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] 失败模式编码缺乏人工验证且可靠性仅为中等**
- 具体位置：§6, Limitations
- 问题：614 条违规 trace 的五类失败模式编码由 LLM 完成（Gwet's AC₁ = 0.62, κ = 0.52），仅为中等一致性。LLM 编码 LLM 失败引入循环性风险。论文用 type→mechanism 的互信息作为结构性证据反驳循环性——但这一论证仅表明类型和机制之间存在非平凡关联，不能排除 LLM coder 在分类机制时受到歧义类型标签泄漏的影响（如果 coder 的 prompt 中包含类型信息）。Limitations 中承认 "human validation underway for camera-ready"，但当前提交缺乏这一关键验证。
- 建议：(1) 明确说明 LLM coder 的 prompt 是否包含歧义类型信息（如果包含，循环性风险更大）；(2) 至少对 50-100 条 trace 进行人工失败模式编码作为验证；(3) 如果 camera-ready 前无法完成，应将 §6 的 claim 强度降低（当前 "three mechanistically distinct failure patterns" 的表述隐含了较强的确定性）。

**W2 [warning] SESOI ±15 pp 的 justification 是循环的**
- 具体位置：§4.6
- 问题：SESOI 设定为 ±15 pp，理由是 "it exceeds measurement noise (perturbation control upper CI: 6.67 pp) by >2×, and a per-type difference below this margin would not warrant distinct mitigation strategies." 第一条理由（>2× 噪声）是任意的（为何不是 3× 或 1.5×？）。第二条理由（不需要不同缓解策略）预设了对实际部署的了解，但无实证支撑——在高风险场景中，5 pp 的差异可能足以区分缓解优先级。论文确实提供了跨七个 margin 的敏感性分析（Table 3），这部分缓解了 SESOI 选择的影响，但 primary margin 的选择仍影响了 §5.2 中的叙述结构（哪些类型"等价"、哪些"分离"）。
- 建议：(1) 明确声明 ±15 pp 是 pragmatic 而非 principled 的选择；(2) 在 §5.2 正文中更突出地引用 Table 3 的 ±10 pp 和 ±12 pp 结果，使读者看到 mid-tier 结构在不同 margin 下的变化；(3) 讨论是否存在领域特定的 SESOI determination 方法。

**W3 [warning] ICC 复制仅限 OpenAI 家族，跨提供商可复现性未直接验证**
- 具体位置：§4.5, Appendix Z
- 问题：ICC 复制（0.919）基于 30 clause pairs × 2 models × 3 replicates，但两个模型均为 OpenAI 家族（GPT-5.4 和 GPT-4.1）。同家族模型可能共享训练数据和对齐方法，导致内部一致性被高估。论文用 "C1 consistency across all seven models" 间接支撑跨提供商稳定性，但 C1 是类型级效应，不等同于 clause-level reproducibility。Authorization scope 的 replication ICC ≈ 0（floor effect）进一步说明 ICC 的稳定性依赖于特定条件。
- 建议：(1) 明确标注 ICC 复制的范围限制（当前 §4.5 仅一句 "ICC is computed within the OpenAI family"）；(2) 讨论跨提供商 ICC 可能更低的含义；(3) 如果资源允许，对 1-2 个非 OpenAI 模型进行小规模 ICC 复制。

**W4 [warning] Human validation 样本量不足以支撑 per-type 可靠性推断**
- 具体位置：§4.4, Appendix I
- 问题：100 episodes 的人工验证产生 200 human-LLM rating pairs，但 per-type 仅 n ≈ 32-34。Coreferential 的 κ = 0.479 尽管 raw agreement 85%（prevalence paradox），authorization scope κ = 0.644——这些数值的 95% CI 极宽（coreferential: [0.00, 0.84]）。论文自身承认 "per-type estimates are imprecise" 和 "should not be interpreted as type-level reliability guarantees"，但正文中仍多次引用 per-type κ 作为论证依据（如 §5.2 对 auth scope κ = 0.385 的讨论）。
- 建议：(1) 增加 human validation 样本量至 per-type ≥ 50；(2) 在引用 per-type κ 时始终附带 CI；(3) 对 authorization scope 和 coreferential 进行专门的 reliability 研究。

**W5 [warning] Cross-domain type ranking 不一致削弱 C2 的泛化性**
- 具体位置：Appendix O
- 问题：跨零售和航空两个领域，per-type violation rate rankings 的 Spearman ρ = 0.26（p = 0.62），远未达到显著。Conditional precedence 跨域差异 22.0 pp（retail 26.7% vs airline 48.7%, Fisher p < 0.001）。这意味着 C2 的类型排序高度领域依赖，但 §7 仅一句提及 "type-specific profiles require per-domain calibration (ρ = 0.26)" 而未充分讨论其对 C2 结论的影响。
- 建议：(1) 在 §5.2 或 §7 中更显著地讨论 C2 的领域依赖性；(2) 在 Conclusion 中限定 C2 的适用范围（"within the customer-service domain" 而非暗示普遍性）。

**W6 [warning] Prevalence audit 用于 motivating research 但自身可靠性低**
- 具体位置：Introduction (§1), Appendix AA
- 问题：Introduction 引用 prevalence audit 的 "55-87% contain at least one ambiguity type" 来 motivate 研究。但该 audit 的 inter-annotator agreement 仅 κ = 0.295（fair），标注完全由 LLM 完成，Claude 标注 83.8% vs GPT 58.5%——差异巨大，且无人工验证（"human validation of a stratified 50-clause subset is planned for the camera-ready"）。用一个 κ = 0.295 的 pilot 来 motivate 一篇因果研究，方法论上不一致。
- 建议：(1) 在 Introduction 中引用时明确标注这是 "LLM-annotated pilot audit with fair inter-judge agreement (κ = 0.295)"；(2) 补充文献中已有的人工标注 ambiguity prevalence 数据作为补充。

### Minor 问题（不影响接收）

**M1.** §6.3 对 "nocuous" 术语的使用实际上 inverts 了 Berry & Kamsties (2004) 的原义（原义：不同 stakeholders 产生不同解释→divergent；本文：模型收敛到相同错误解释→convergent）。虽然 §6.3 有讨论这一反转，但建议在首次使用时（Abstract）即简要标注这一区别，避免熟悉 RE 文献的读者产生误解。

**M2.** 所有 API 调用使用 temperature = 0（§4.3），这是实验控制的合理选择，但生产环境通常使用 temperature > 0。应在 Limitations 中提及温度设置对结论泛化性的影响。

**M3.** §4.2 提到 "3 episodes lost to API errors in one Qwen3 batch"，从 3,000 到 2,997。虽然影响极小，但应说明这 3 个 episode 是否在特定条件/类型下，以排除 systematic missingness。

**M4.** Table 2 脚注中 ‡ 标记 authorization scope 的 "Lowest inter-judge agreement (κ = 0.385)"，但该 κ 来自 100 episodes 的 dual-judge calibration，per-type 仅 ~17 episodes。建议在脚注中标注样本量。

**M5.** Appendix 编号使用自定义 \extAlph 命令从 A 到 AE，但正文交叉引用使用混合记法（如 "Appendix R"、"Appendix AA"）。应检查所有 Appendix 引用的一致性。

---

## Questions（需要作者澄清的问题）

**Q1.** Template-based pipeline 使用了多少模板？每类型的模板数量是否相同？模板的设计是否经过 pilot testing 以确保歧义操作的生态效度？

**Q2.** SOPBench 复制中 GPT-5.4（p = 0.052）和 DeepSeek（p = 0.163）未达显著——如果扩大样本量（当前 n = 139 和 374），作者预期这些模型是否会达到显著？power analysis 是否支持 C1 在这些模型上的效应量足以在合理样本量下达到显著？

**Q3.** 失败模式编码的 LLM coder 的 prompt 是否包含了歧义类型标签？如果是，如何排除 coder 利用类型信息推断机制的可能性（即非独立编码）？

**Q4.** Cross-domain type ranking 的 ρ = 0.26 是否意味着 C2 的 partial ordering 仅在 pooled 水平上成立，而在单一领域内可能不成立？这对实际部署中的 "type-targeted diagnosis" 建议有何含义？

**Q5.** 22.4% 的 clause-level variance 的分布形态如何——是少数高效应条款驱动的右偏分布，还是连续分布？如果是前者，识别高风险条款的 surface features 是否比类型分类更有实践价值？（Appendix W 的 linguistic feature regression R² = 0.069 暗示 surface features 预测能力也很有限。）

**Q6.** Matched-pair OR = 15.1 来自 McNemar's test 的 discordant pairs（n = 580）。580/1497 = 38.7% 的 pairs 是 discordant 的——剩余 61.3% 的 concordant pairs 中，concordant-violation（两个条件都违规）和 concordant-no-violation 的比例分别是多少？高 concordant-violation 比例会暗示歧义不是唯一的违规驱动因素。

---

## Missing References（遗漏的重要相关工作）

1. **Lu et al., 2022** ("Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity") — 关于 LLM 对 prompt 表面特征的敏感性，与 clause wording 解释 22.4% 方差的发现相关。

2. **Kadavath et al., 2022** ("Language Models (Mostly) Know What They Know") — 关于 LLM 自我校准能力，与 disambiguation neglect（4.6% awareness）的发现直接相关。

3. **Anthropic's Constitutional AI (Bai et al., 2022)** 和 **RLHF 对齐文献** — 与 authorization scope 的跨模型差异（Claude 12% vs GPT-5.4 64%）反映 "differential safety training" 的讨论直接相关，但论文未引用任何具体的对齐训练方法论文。

---

## Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claim (C1, C2) 有充分统计支撑和适当控制，matched-pair 设计严谨。但 incompleteness 的信息添加混淆控制不够（仅 token count proxy），failure mode 编码缺人工验证（κ = 0.52），authorization scope 低 κ（0.385）影响部分分析。Per-type 分析受小样本 CI 限制。 |
| Excitement | 3.5/5 | 研究问题新颖且实践相关（policy ambiguity → agent safety 的首个因果研究）。Type → mechanism 的发现重构了分类法价值，有诊断工具潜力。但 synthetic-to-natural 效应差距（34 pp → 12.6 pp）和跨域类型排序不稳定（ρ = 0.26）限制了直接实践影响。 |
| Reproducibility | 3/5 | 承诺释放 300 clause pairs、pipeline 和 traces。但 template-based pipeline 描述不足，ICC 复制仅限 OpenAI 家族，coreferential 在复制和 mitigation 实验中均被排除。 |
| Confidence | 4/5 | 仔细阅读了全文和全部 Appendix，熟悉因果推断方法、LLM safety evaluation 和 ambiguity 相关文献。 |

### 评分
**Overall: 3.5 (Borderline Conference)**

**理由**: 本文在 research question 的新颖性（policy ambiguity 的首个因果研究）和方法论严谨性（matched-pair design + 全面的统计框架 + 多层控制）方面达到了会议水准。方差分解和 type→mechanism 的发现有实质贡献。但三个问题阻止了明确的 Conference 推荐：(1) 合成刺激的外部效度不确定（SOPBench 效应压缩 63%，且该复制中 2/5 模型不显著），(2) incompleteness 的信息添加混淆控制仅用 token count 这一粗糙 proxy，(3) failure mode taxonomy 缺乏人工验证（camera-ready 承诺不足以支撑当前 claim 强度）。如果作者能在 revision 中解决 N1-N3 中的至少两个（特别是 clause pair construction transparency 和 incompleteness confound 的更强控制），论文可升至 Conference 水准。当前状态适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2113 · 2026-05-23T08:22:29.661562+00:00_

Reviewer 1 已提交审稿意见（方法严谨性），评分 3.5 Borderline Conference。等待 Reviewer 2 的审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 199

## Round 199

2 recorded events


### User

_source line 2114 · 2026-05-23T08:22:37.524463+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.5 (Borderline Conference)**。

主要优势：matched-pair causal design 严谨、统计框架全面、perturbation control 有效、方法论局限的坦诚披露。

三个 Must-Fix 问题阻止了 Conference 推荐：
1. **合成→自然效应压缩 63%**（SOPBench 仅 +12.6 pp vs 主研究 +34.0 pp，且 2/5 模型不显著），外部效度存疑
2. **Incompleteness 的信息添加混淆控制不足**——token count 是粗糙 proxy，正系数的解释有逻辑漏洞
3. **条款对构建过程不透明**——template pipeline 未描述模板数量、结构和筛选率，可复现性受限

当前适合 Findings；解决 N1-N3 中至少两个可升至 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2115 · 2026-05-23T08:22:45.546352+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 200

## Round 200

6 recorded events


### User

_source line 2116 · 2026-05-23T08:23:33.927112+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性与完整性

**论文**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
**Venue**: EMNLP 2026 via ARR (Long Paper)

---

## Summary（2-3 句）

本文在 τ²-bench 上通过 300 对 matched-pair 子句（覆盖六类歧义类型、五个模型），建立了 policy 歧义与 LLM agent 安全违规之间的因果关系（+34.0 pp），并展示类型预测失败机制的能力远强于预测违规率（NMI = 0.23 vs 0.01）。工作方法论严谨，统计框架完整（TOST 等价检验、方差分解、扰动控制、交叉评判校准），但核心发现（歧义导致违规）的意外性有限，taxonomy 新颖性受制于对已有分类体系的子集选取，且关键类型（authorization scope、incompleteness）存在构念效度和混杂问题。

---

## Strengths（逐条）

**S1. 方法论严谨的因果设计**
Matched-pair 最小编辑设计（§4.2）是本文最大亮点。通过控制子句语义只改变歧义属性，配合扰动控制（Δ_perturb = -0.67 pp，含零；§4.5）和 ICC = 0.919 的复现性验证，因果推断链条完整度在该领域同类工作中罕见。相比 DRIP-R（仅关联性）和 PolicyBank（策略迭代优化），本文的实验设计具有明确的方法论优势。

**S2. 统计严谨性超出平均水准**
TOST 等价检验替代了主观聚类（Table 3, Appendix A），方差分解明确区分 clause identity (22.4%) vs type (0.4%) vs model (1.0%)，Holm-Bonferroni 校正用于多重比较，C3 层效应未通过校正后被诚实地标注为未通过（p=0.017 vs 阈值 0.0125）。这种统计自律值得肯定。

**S3. Error analysis 揭示的新现象有价值**
"Disambiguation neglect"（§6.2，总体 4.6% 意识率）和 "systematic nocuity"（§6.3，41.3% 多数模型收敛于相同错误解释，77% 倾向宽松方向）是有实质贡献的发现。特别是 nocuity 的方向反转（Berry & Kamsties 的 nocuous = 人类分歧，此处 = 模型收敛于错误）提供了对 LLM 特有的 agent safety 失败模式的深入理解。

**S4. 充分的复现与泛化验证**
7 个模型（5 main + Gemini-2.5-Flash, LLaMA-4-Scout）、SOPBench 跨基准复现（Appendix X）、三族交叉评判验证（Appendix G），覆盖面在同类工作中少见。

**S5. Related work 覆盖度好**
引用了所有主要并发工作（DRIP-R, PolicyBank, AgentPex, MANTRA），并在 §2 中明确定位差异。对心理语言学（Ferreira 2002, Frazier & Rayner 1982）和 RE 文献（Berry & Kamsties 2004, Massey 2014）的桥接也恰当。

---

## Weaknesses（按严重程度分级）

### Must-Fix 问题（影响接收决定）

**N1 [critical] 核心贡献的 novelty 需更诚实定位**
- 具体位置：§1 contributions list, Abstract
- 问题：Contribution (1) 宣称 "the first matched-pair causal study of policy ambiguity's safety impact"。Matched-pair 设计本身是心理语言学和 RE 领域的标准方法论（Ferreira 2002 已被引用），将其应用于 LLM agent policy 是直接的领域迁移（domain transfer），而非方法论创新。核心发现——歧义策略导致更多违规——方向上是可预测的（ambiguity → more errors 是先验合理的），真正有价值的是效应量化和类型分析。但当前 framing 将"首次"和"因果"作为主要卖点，overstates 了新颖性。
- 为什么影响接收：ARR Excitement 维度要求论文提供 surprising 或 non-obvious 的 insight。如果核心 message 是 "模糊政策导致更多违规"，reviewer 可能认为这验证了一个显而易见的假设。
- 建议修改方向：将 framing 从 "first causal study" 转向 "first quantification of the differential effect across ambiguity types + diagnostic taxonomy"。后者的 NMI = 0.23 vs 0.01 的发现更有价值且更不显然。

**N2 [critical] Taxonomy 新颖性不足，且层效应未得到统计支持**
- 具体位置：§3 Taxonomy, §5.2 (C3)
- 问题：六类 taxonomy 是从 Li et al. (2024) 的 11 类 NLP taxonomy 中选取 6 类，非原创分类体系。两层结构（linguistic/specification）是论文叙事的重要组成，但 C3 层效应未通过 Holm-Bonferroni 校正（p=0.017 vs 阈值 0.0125, §5.2）。这意味着"两层结构具有实证区分度"这一隐含 claim 缺乏统计支持。论文在 §5.2 末尾简短提及这一失败，但 §3 和 §1 的叙事仍然大量围绕两层结构展开，造成 framing 与 evidence 的落差。
- 为什么影响接收：Taxonomy 被列为关键贡献之一。如果层效应不显著，taxonomy 的结构性贡献仅剩六类分类本身（子集选取），难以支撑一个独立贡献。
- 建议修改方向：（a）在 §3 更明确地说明层划分是组织性的而非 empirically validated structural claim；（b）将 taxonomy 的贡献定位为"实验工具"而非"分类贡献"，这与 §2 中 "experimental instrument rather than a proposed classification standard" 的表述一致，但正文其他地方的 framing 不一致。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] Authorization scope 构念效度存疑**
- 具体位置：§4.4 (κ=0.385), §5.2 (ρ=0.09 cross-judge group ranking), §5.2 (C4 driven entirely by auth scope)
- 问题：Authorization scope 的评判者间一致性远低于其他类型（κ=0.385 vs 整体 κ=0.653），交叉评判组排序不一致（ρ=0.09, p=0.87），且是唯一驱动 C4 model×type 交互效应的类型（排除后 p=0.97）。这些证据综合表明 authorization scope 可能不是一个稳定的测量构念——不同评判者对"investigating an unauthorized request 是否构成 violation"存在根本分歧。论文在脚注和文本中承认了这些问题，但 authorization scope 仍以与其他类型平等的权重参与所有主分析（Table 2, Figure 2-3），且其 36.0 pp 的效应量是报告中的"confound-free"上界。
- 建议：在主分析中对 authorization scope 进行更系统的敏感性分析——报告排除 auth scope 后的 pooled Δ、方差分解、NMI 等核心数字。当前只在 C4 和 cross-judge ranking 中做了这个排除，但 C1 和 C2 的核心数字未报告排除后的版本。

**W2 [warning] Incompleteness 的混杂问题 framing 不够突出**
- 具体位置：§4.2, §5.1, Table 2 footnote
- 问题：Incompleteness 的歧义消解涉及信息添加（content addition），本质上是不同于其他五类的实验操纵——其他类型是最小编辑，而 incompleteness 需要添加新内容。这意味着 incompleteness 的 49.2 pp 效应量可能部分归因于信息量差异而非歧义本身。论文通过 token count 控制和 logistic regression（Appendix F）缓解了这一问题，但仅在脚注标记（Table 2 †），主文叙事仍频繁引用 49.2 pp 作为最大效应。在 Abstract 中，"34.0 percentage points" 包含了 incompleteness，而 confound-free range "+18.7 to +36.0 pp" 排除了它——这个关键区别在 Abstract 的一句话中被压缩处理，容易被忽略。
- 建议：Abstract 和 Conclusion 中应优先报告 confound-free 的 pooled effect (+31.0 pp, 排除 incompleteness)，将含 incompleteness 的 34.0 pp 作为上界补充。

**W3 [warning] SOPBench 跨基准复现效应量大幅缩小**
- 具体位置：§5.1, Appendix X
- 问题：SOPBench 复现仅显示 +12.6 pp（主实验的约 1/3），且仅 3/5 比较达到显著。论文将此定性为 "directional consistency"，但一个同样合理的解读是：合成构造的歧义子句在 τ²-bench 上严重膨胀了效应量，真实世界效应可能远小于 34.0 pp。§5.1 末尾的 caveat "effect-size calibration requires grain-matched measurement" 是重要的，但位于段落末尾容易被忽略。
- 建议：在 Discussion 中更正式地讨论效应量的生态效度（ecological validity）。当前 Limitations 提到 "34.0 pp is an upper bound"，但未将 SOPBench 的 12.6 pp 作为更现实的估计进行讨论。

**W4 [warning] 方差分解叙事偏重已解释部分**
- 具体位置：§5.1, §7
- 问题：方差分解显示 60.8% 为残差（~15% 随机 + ~46% 系统性），但正文叙事集中于已解释的 22.4%（clause wording）。"Even perfect disambiguation would address at most 22.4% of variance"（§7）是一个重要 caveat，但被包装为 intervention 的上限而非研究本身的解释力问题。如果 60.8% 的方差来自未建模的对话轨迹、用户模拟器行为、话题交互等因素，那么 clause-level 分析框架本身的解释范围是有限的。
- 建议：在 Discussion 中正面讨论 60.8% 残差的来源假说及其对论文 claims 解释范围的影响。

**W5 [warning] NMI 比较的方法论细节不够透明**
- 具体位置：§1, §7, Appendix
- 问题："Type predicts failure mechanism an order of magnitude better than violation rate (NMI = 0.23 vs 0.01)" 是论文的核心 claim 之一。但 NMI 的计算细节不在正文中：type→mechanism 是 6 categories × 5 mechanisms，而 type→violation 是 6 categories × 2 outcomes（binary）。两侧的变量粒度（cardinality）不对称——mechanism 有 5 类而 violation 只有 2 类——可能影响 NMI 值的可比性。虽然 NMI 理论上通过归一化处理了这一问题，但低 cardinality（binary outcome）下 NMI 的 effective range 更受限。
- 建议：在正文或 Appendix 中补充说明 NMI 计算的具体设置，并讨论 cardinality asymmetry 对比较的影响。或者补充一个 cardinality-symmetric 的替代指标（如将 violation rate 离散化为多个 bin 后重算 NMI）。

### Minor 问题（不影响接收）

**M1.** Abstract 信息密度过高：一个 abstract 中包含 8 个具体数字（34.0 pp, +18.7, +36.0, 22.4%, 0.4%, NMI=0.23, 0.01, 77%），影响可读性。建议精简到 3-4 个最核心的数字。

**M2.** C3 claims 结构：C1-C4 的编号暗示四个 claims，但 C3（层效应）未通过多重校正，C4 被标注为 exploratory。实际上只有 C1 和 C2 是 supported primary claims，建议在 §5 开头更明确地表述。

**M3.** Temperature = 0 的局限性：所有实验使用 temperature=0（§4.3），最大化确定性但可能不代表典型部署条件。Limitations 未提及这一点。

**M4.** Figure 1 概览图信息量可以更高：当前 Figure 1 主要展示 pipeline 流程，但未可视化关键设计选择（如 matched-pair 的最小编辑示例），空间利用可优化。

**M5.** "Nocuous" 一词在标题中使用可能对非 RE 背景读者不友好。虽然在正文中有充分解释（§1 第一段引入 Berry & Kamsties 2004），但标题是第一接触点。

---

## Questions（需要作者澄清）

**Q1.** SOPBench 的 +12.6 pp 仅为主效应的 37%。如果论文的核心 message 是 "policy ambiguity causes safety violations"，那么在更自然的条件下效应量缩小到约 1/3 这一事实如何影响论文的实际启示？

**Q2.** Authorization scope 排除后，C1 的 pooled Δ 和方差分解数字是否发生实质变化？当前只报告了排除 incompleteness 后的 pooled Δ = +31.0 pp（Table 2 脚注），但未报告排除 auth scope 后的数字。

**Q3.** NMI = 0.23（type→mechanism）中的 mechanism 编码使用 LLM annotator（κ=0.52, §6），这一较低的编码可靠性对 NMI 值有多大影响？如果使用 human coding 的 subsample，NMI 是否稳定？

**Q4.** "Systematic nocuity" 中 77% 的 permissive bias 是否可能反映训练数据中 customer-service 场景的固有偏向（agent 通常被训练为"帮助客户"）？如果在不同领域（如医疗、金融）中复现，permissive 方向是否会改变？

**Q5.** Disambiguation neglect (4.6%) 的分布高度集中于 GPT-4.1 和 Claude（10-11%），而 Qwen3 和 DeepSeek 为 0%。这是否反映了 safety training 差异而非歧义处理能力差异？

---

## Missing References（遗漏的重要相关工作）

1. **AgentSpec** (Wang et al., ICSE 2026) — 针对 LLM agent 的运行时规约执行框架，提供 DSL 定义安全约束并实时强制执行，是本文诊断框架的自然下游（从检测到预防）。应在 §2 Agent Safety Evaluation 段落中讨论。

2. **Agent Behavioral Contracts** (arXiv 2602.22302, 2026) — 形式化规约与运行时执行，与本文的 policy specification 视角互补。

3. **"Check Yourself Before You Wreck Yourself"** (arXiv 2510.16492, 2025) — 提出 selective quitting 作为 agent safety 机制，与本文发现的 disambiguation neglect（agents 不知何时退出）直接相关。

---

## Overall Assessment

**Overall**: 3.5 (Borderline Conference)

**Soundness**: 4/5 — 方法论设计严谨，统计框架完整，confounds 被诚实地报告。扣分点在于 authorization scope 构念效度和 NMI 比较的 cardinality 不对称。

**Excitement**: 3/5 — 核心发现（ambiguity → violations）方向上可预测；type-specific 诊断和 systematic nocuity 有价值但不足以达到 "exciting" 水平。Taxonomy 非原创构建。

**Reproducibility**: 4/5 — 数据和代码承诺发布，实验设置详细，ICC 复现验证充分。LLM 评判的可复现性受 API 版本影响。

**Confidence**: 4/5 — 仔细阅读了全文含 appendix，熟悉 RE 歧义文献、LLM agent safety 评估、因果推断方法论。

**一句话总结**: 方法论严谨的因果实验，但核心 insight 的 novelty 受限于验证了一个先验可预期的假设；taxonomy 的独立贡献不足以弥补 excitement 的缺口。如果能按 N1/N2 调整 framing——弱化 "first causal study" 卖点、强化 type-specific diagnostic 和 systematic nocuity 作为主贡献——评分可能升至 Conference (4.0)。

---

## 格式合规检查

- ✅ 正文 8 页（Sections 1-8 在第 8 页结束，Limitations 在第 9 页）
- ✅ Double-blind（标题页 "Anonymous ACL submission"，GitHub URL 使用 anonymous）
- ✅ ACL 模板使用正确
- ✅ Limitations section 存在且位于正文中（第 9 页），覆盖了合成数据、领域范围、评判一致性三个关键限制
- ✅ 引用格式基本一致（natbib 风格）
- ⚠️ 一处注意：Data and Code Availability 中的匿名 GitHub URL 格式正确，但需确保提交时未泄露真实身份

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2117 · 2026-05-23T08:24:22.455264+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Must-Fix 问题\n\n**N1 [critical] 合成歧义与自然歧义的效应差距未充分解释，威胁外部效度**\n主研究 +34.0 pp vs SOPBench +12.6 pp，63% 压缩，2/5 模型不显著。三个归因因素（measurement grain、baseline rate compression、interaction depth）是 post-hoc 推测，无实验分解。Abstract/Conclusion 中 \"34.0 pp\" 在多大程度上代表真实世界效应，读者无法判断。\n\n**N2 [critical] Incompleteness 的信息添加混淆控制不足以支撑因果主张**\nToken count 作为 proxy 控制混淆——logistic regression 的正系数 (β=+0.027) 的解释有逻辑漏洞：更长条款可能因约束过多而违规（over-constraint violation），方向与信息添加假设一致而非相反。Auth scope 有最大 token delta (+36.1) 但低 κ (0.385)，作为参照物不可靠。\n\n**N3 [critical] 条款对构建过程不够透明，可复现性受限**\n\"Template-based pipeline\" 未描述模板数量、结构、筛选率、rejection rate。\"Post-hoc realism validation\" 一句带过。标注者高一致率 (κ=0.95) 可能反映歧义实例过于典型化。\n\n### Should-Fix 问题\n\n**W1 [warning] 失败模式编码缺乏人工验证且可靠性仅为中等**\n614 条 trace 由 LLM 编码（Gwet's AC₁=0.62, κ=0.52），循环性风险。LLM coder 的 prompt 是否包含类型信息？\n\n**W2 [warning] SESOI ±15 pp 的 justification 是循环的**\n\">2× 噪声\"和\"不需要不同缓解策略\"两条理由均非 principled。\n\n**W3 [warning] ICC 复制仅限 OpenAI 家族**\n同家族模型共享训练数据，clause-level reproducibility 可能被高估。\n\n**W4 [warning] Human validation 样本量不足以支撑 per-type 可靠性推断**\nPer-type n≈32-34，coreferential κ=0.479 CI [0.00, 0.84]。\n\n**W5 [warning] Cross-domain type ranking 不一致削弱 C2 泛化性**\nρ=0.26 (p=0.62)，cond. prec. 跨域差异 22.0 pp。\n\n**W6 [warning] Prevalence audit 自身可靠性低**\nκ=0.295, Claude 83.8% vs GPT 58.5%，无人工验证。\n\n### Minor 问题\nM1. \"Nocuous\" 术语反转未在首次使用时标注\nM2. Temperature=0 的泛化性限制\nM3. 3 个 Qwen3 API error episodes 的 systematic missingness\nM4. Table 2 ‡ 脚注缺样本量\nM5. Appendix 交叉引用一致性\n\n### Questions\nQ1. 模板数量和设计？\nQ2. SOPBench 中 GPT-5.4/DeepSeek 的 power analysis？\nQ3. LLM coder prompt 是否含类型标签？\nQ4. ρ=0.26 对 type-targeted diagnosis 的实际含义？\nQ5. 22.4% clause-level variance 的分布形态？\nQ6. Concordant-violation vs concordant-no-violation 比例？\n\n### Missing References\n1. Lu et al. 2022 (prompt order sensitivity)\n2. Kadavath et al. 2022 (LLM self-calibration)\n3. Constitutional AI / RLHF alignment literature\n\n### Overall: 3.5 (Borderline Conference)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Must-Fix 问题\n\n**N1 [critical] 合成歧义与自然歧义的效应差距未充分解释，威胁外部效度**\n主研究 +34.0 pp vs SOPBench +12.6 pp，63% 压缩，2/5 模型不显著。三个归因因素（measurement grain、baseline rate compression、interaction depth）是 post-hoc 推测，无实验分解。Abstract/Conclusion 中 \"34.0 pp\" 在多大程度上代表真实世界效应，读者无法判断。\n\n**N2 [critical] Incompleteness 的信息添加混淆控制不足以支撑因果主张**\nToken count 作为 proxy 控制混淆——logistic regression 的正系数 (β=+0.027) 的解释有逻辑漏洞：更长条款可能因约束过多而违规（over-constraint violation），方向与信息添加假设一致而非相反。Auth scope 有最大 token delta (+36.1) 但低 κ (0.385)，作为参照物不可靠。\n\n**N3 [critical] 条款对构建过程不够透明，可复现性受限**\n\"Template-based pipeline\" 未描述模板数量、结构、筛选率、rejection rate。\"Post-hoc realism validation\" 一句带过。标注者高一致率 (κ=0.95) 可能反映歧义实例过于典型化。\n\n### Should-Fix 问题\n\n**W1 [warning] 失败模式编码缺乏人工验证且可靠性仅为中等**\n614 条 trace 由 LLM 编码（Gwet's AC₁=0.62, κ=0.52），循环性风险。LLM coder 的 prompt 是否包含类型信息？\n\n**W2 [warning] SESOI ±15 pp 的 justification 是循环的**\n\">2× 噪声\"和\"不需要不同缓解策略\"两条理由均非 principled。\n\n**W3 [warning] ICC 复制仅限 OpenAI 家族**\n同家族模型共享训练数据，clause-level reproducibility 可能被高估。\n\n**W4 [warning] Human validation 样本量不足以支撑 per-type 可靠性推断**\nPer-type n≈32-34，coreferential κ=0.479 CI [0.00, 0.84]。\n\n**W5 [warning] Cross-domain type ranking 不一致削弱 C2 泛化性**\nρ=0.26 (p=0.62)，cond. prec. 跨域差异 22.0 pp。\n\n**W6 [warning] Prevalence audit 自身可靠性低**\nκ=0.295, Claude 83.8% vs GPT 58.5%，无人工验证。\n\n### Minor 问题\nM1. \"Nocuous\" 术语反转未在首次使用时标注\nM2. Temperature=0 的泛化性限制\nM3. 3 个 Qwen3 API error episodes 的 systematic missingness\nM4. Table 2 ‡ 脚注缺样本量\nM5. Appendix 交叉引用一致性\n\n### Questions\nQ1. 模板数量和设计？\nQ2. SOPBench 中 GPT-5.4/DeepSeek 的 power analysis？\nQ3. LLM coder prompt 是否含类型标签？\nQ4. ρ=0.26 对 type-targeted diagnosis 的实际含义？\nQ5. 22.4% clause-level variance 的分布形态？\nQ6. Concordant-violation vs concordant-no-violation 比例？\n\n### Missing References\n1. Lu et al. 2022 (prompt order sensitivity)\n2. Kadavath et al. 2022 (LLM self-calibration)\n3. Constitutional AI / RLHF alignment literature\n\n### Overall: 3.5 (Borderline Conference)"
  }
}
```

</details>

---


### Tool result

_source line 2118 · 2026-05-23T08:24:48.066976+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25611
}
```

</details>

---


### Tool call

_source line 2119 · 2026-05-23T08:24:48.418675+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Must-Fix 问题\n\n**N1 [critical] 核心贡献的 novelty 需更诚实定位**\nContribution (1) \"the first matched-pair causal study\" — matched-pair 是心理语言学/RE 的标准方法，应用于 LLM agent policy 是领域迁移而非方法论创新。核心发现 \"ambiguity → more errors\" 方向上可预测。建议 framing 从 \"first causal study\" 转向 \"first quantification of differential effect + diagnostic taxonomy\"。\n\n**N2 [critical] Taxonomy 新颖性不足，且层效应未得到统计支持**\n六类 taxonomy 是 Li et al. (2024) 11 类的子集选取。C3 层效应未通过 Holm-Bonferroni (p=0.017 vs 阈值 0.0125)。§3 和 §1 的叙事围绕两层结构展开，但 evidence 不支持。建议将 taxonomy 定位为 \"experimental instrument\" 而非 \"classification contribution\"。\n\n### Should-Fix 问题\n\n**W1 [warning] Authorization scope 构念效度存疑**\nκ=0.385, ρ=0.09 cross-judge group ranking, C4 entirely driven by auth scope (排除后 p=0.97)。建议报告排除 auth scope 后的 C1 pooled Δ、方差分解、NMI。\n\n**W2 [warning] Incompleteness 混杂 framing 不够突出**\n49.2 pp 可能部分归因于信息量差异。Abstract 中 34.0 pp 包含 incompleteness 而 confound-free range 排除了它，这个区别在一句话中被压缩处理。建议 Abstract/Conclusion 优先报告 confound-free pooled effect (+31.0 pp)。\n\n**W3 [warning] SOPBench 效应量大幅缩小**\n+12.6 pp = 主实验 1/3。\"Directional consistency\" 的 framing 可能掩盖了效应量的实质性差异。建议在 Discussion 正式讨论生态效度。\n\n**W4 [warning] 方差分解叙事偏重已解释部分**\n60.8% 残差被包装为 intervention 上限而非研究解释力限制。\n\n**W5 [warning] NMI 比较的 cardinality 不对称**\nType→mechanism 是 6×5，type→violation 是 6×2。低 cardinality 下 NMI effective range 更受限。\n\n### Minor 问题\nM1. Abstract 信息密度过高（8 个数字）\nM2. C3/C4 编号暗示四个 supported claims，实际仅 C1/C2\nM3. Temperature=0 局限性\nM4. Figure 1 信息量可更高\nM5. \"Nocuous\" 在标题中对非 RE 读者不友好\n\n### Questions\nQ1. SOPBench 效应缩小对实际启示的影响？\nQ2. 排除 auth scope 后 C1 和方差分解数字？\nQ3. LLM 编码的低 κ 对 NMI 的影响？\nQ4. 77% permissive bias 是否是 customer-service domain artifact？\nQ5. Disambiguation neglect 的模型差异是 safety training 差异而非歧义处理能力差异？\n\n### Missing References\n1. AgentSpec (Wang et al., ICSE 2026) — agent runtime specification enforcement\n2. Agent Behavioral Contracts (arXiv 2602.22302, 2026) — formal specification + runtime enforcement\n3. \"Check Yourself Before You Wreck Yourself\" (arXiv 2510.16492, 2025) — selective quitting for agent safety\n\n### Overall: 3.5 (Borderline Conference)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Must-Fix 问题\n\n**N1 [critical] 核心贡献的 novelty 需更诚实定位**\nContribution (1) \"the first matched-pair causal study\" — matched-pair 是心理语言学/RE 的标准方法，应用于 LLM agent policy 是领域迁移而非方法论创新。核心发现 \"ambiguity → more errors\" 方向上可预测。建议 framing 从 \"first causal study\" 转向 \"first quantification of differential effect + diagnostic taxonomy\"。\n\n**N2 [critical] Taxonomy 新颖性不足，且层效应未得到统计支持**\n六类 taxonomy 是 Li et al. (2024) 11 类的子集选取。C3 层效应未通过 Holm-Bonferroni (p=0.017 vs 阈值 0.0125)。§3 和 §1 的叙事围绕两层结构展开，但 evidence 不支持。建议将 taxonomy 定位为 \"experimental instrument\" 而非 \"classification contribution\"。\n\n### Should-Fix 问题\n\n**W1 [warning] Authorization scope 构念效度存疑**\nκ=0.385, ρ=0.09 cross-judge group ranking, C4 entirely driven by auth scope (排除后 p=0.97)。建议报告排除 auth scope 后的 C1 pooled Δ、方差分解、NMI。\n\n**W2 [warning] Incompleteness 混杂 framing 不够突出**\n49.2 pp 可能部分归因于信息量差异。Abstract 中 34.0 pp 包含 incompleteness 而 confound-free range 排除了它，这个区别在一句话中被压缩处理。建议 Abstract/Conclusion 优先报告 confound-free pooled effect (+31.0 pp)。\n\n**W3 [warning] SOPBench 效应量大幅缩小**\n+12.6 pp = 主实验 1/3。\"Directional consistency\" 的 framing 可能掩盖了效应量的实质性差异。建议在 Discussion 正式讨论生态效度。\n\n**W4 [warning] 方差分解叙事偏重已解释部分**\n60.8% 残差被包装为 intervention 上限而非研究解释力限制。\n\n**W5 [warning] NMI 比较的 cardinality 不对称**\nType→mechanism 是 6×5，type→violation 是 6×2。低 cardinality 下 NMI effective range 更受限。\n\n### Minor 问题\nM1. Abstract 信息密度过高（8 个数字）\nM2. C3/C4 编号暗示四个 supported claims，实际仅 C1/C2\nM3. Temperature=0 局限性\nM4. Figure 1 信息量可更高\nM5. \"Nocuous\" 在标题中对非 RE 读者不友好\n\n### Questions\nQ1. SOPBench 效应缩小对实际启示的影响？\nQ2. 排除 auth scope 后 C1 和方差分解数字？\nQ3. LLM 编码的低 κ 对 NMI 的影响？\nQ4. 77% permissive bias 是否是 customer-service domain artifact？\nQ5. Disambiguation neglect 的模型差异是 safety training 差异而非歧义处理能力差异？\n\n### Missing References\n1. AgentSpec (Wang et al., ICSE 2026) — agent runtime specification enforcement\n2. Agent Behavioral Contracts (arXiv 2602.22302, 2026) — formal specification + runtime enforcement\n3. \"Check Yourself Before You Wreck Yourself\" (arXiv 2510.16492, 2025) — selective quitting for agent safety\n\n### Overall: 3.5 (Borderline Conference)"
  }
}
```

</details>

---


### Tool result

_source line 2120 · 2026-05-23T08:24:49.776762+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1358
}
```

</details>

---


### Assistant

_source line 2121 · 2026-05-23T08:24:53.124252+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 201

## Round 201

2 recorded events


### User

_source line 2122 · 2026-05-23T08:24:55.707204+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心评分：Overall 3.5 (Borderline Conference)**

主要判断依据：
- **方法论是本文最大优势**：matched-pair 因果设计、完整的统计框架（TOST、方差分解、扰动控制）、7 模型复现，soundness 给 4/5
- **Excitement 受限（3/5）**：核心发现"歧义导致违规"方向可预期；taxonomy 是已有 11 类体系的 6 类子集选取，且两层结构（C3）未通过统计校正
- **两个 Must-Fix**：(1) 需重新定位 novelty framing——从"首次因果研究"转向"首次量化类型差异+诊断 taxonomy"；(2) taxonomy 层效应不显著需在 framing 中诚实处理
- **五个 Should-Fix**：authorization scope 构念效度（κ=0.385）、incompleteness 混杂 framing、SOPBench 效应缩小 1/3 的生态效度讨论、60.8% 残差方差的讨论缺失、NMI cardinality 不对称

如果作者按建议调整 framing，评分有望升至 4.0 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2123 · 2026-05-23T08:25:00.076636+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 202

## Round 202

2 recorded events


### User

_source line 2124 · 2026-05-23T08:26:57.953420+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 合成歧义与自然歧义的效应差距（34.0 pp vs 12.6 pp）**

同意这是本文最重要的外部效度威胁。我在自己的审稿中将此列为 W3（Should-Fix）。R1 将其升级为 critical 是合理的——63% 的效应压缩（34.0→12.6 pp）不能仅用 "measurement grain" 和 "baseline rate compression" 等 post-hoc 归因来解释。

补充 R1 未提的一点：§5.1 中 "directional consistency across all models is the primary criterion" 这一 framing 将跨基准复现的标准从效应量一致性降格为方向一致性，是一种目标移动（goalpost shifting）。如果主 claim 是量化因果效应（"increases violation rates by 34.0 pp"），那么跨基准效应量的大幅缩小就不能被 "方向一致即可" 搪塞过去。

但我与 R1 在严重程度上有细微差异：我认为这更接近 Should-Fix 而非 Must-Fix，因为论文的 Limitations 已明确声明 "34.0 pp is an upper bound"（§Limitations），且 SOPBench 复现是 supplementary 验证，不是论文的核心分析平台。关键修改是调整 Abstract/Conclusion 中的 framing——将 confound-free pooled effect（+31.0 pp，排除 incompleteness）或 SOPBench 的 +12.6 pp 作为效应量范围呈现，而非仅报告 34.0 pp。

---

**[AGREE] R1-N2: Incompleteness 信息添加混淆控制不足**

同意（我的 W2 提出了同一问题但 R1 的批评更精确）。R1 指出 logistic regression 的正系数 β=+0.027 存在另一种解释——更长条款可能因约束过多导致 over-constraint violation——这一反事实解释在逻辑上成立。

不过，我对 R1 的批评力度有一点保留：§5.1 明确报告 "controlling for token count changes no type's predicted effect by more than 0.1 pp"。无论 β 的因果解释如何，0.1 pp 的实际影响是微不足道的。R1 的批评更多是对方法论透明度的要求，而非对结论的实质威胁。

真正的问题不在于 token count 控制，而在于 incompleteness 的实验操纵本质上不同——其他五类是语义重写（rewording），incompleteness 是信息删除/添加。这两种操纵的心理语言学机制不同，不应被同一个 "ambiguity effect" 统一度量。论文已部分承认这一点（报告了排除 incompleteness 的 pooled Δ = +31.0 pp），但 framing 不够突出。

---

**[REBUT] R1-N3: 条款对构建过程不够透明——严重程度过高**

部分同意透明度不足，但不同意将此列为 Must-Fix/Critical。

理由：
1. §4.2 已提供关键细节：template-based pipeline、两名 NLP 背景标注者、三项验证标准（单一歧义实例、不改变策略范围、自然性）、96% 初始一致率（287/300, κ=0.95）、13 个分歧通过讨论解决。
2. Data and Code Availability 承诺发布全部 300 对子句、评估 pipeline 和分析脚本——这是最终极的可复现性保证。
3. R1 担心 κ=0.95 "可能反映歧义实例过于典型化"——但高标注一致率是 controlled experiment 的设计目标，不是缺陷。matched-pair 设计本身就要求清晰的歧义操纵；如果标注者也无法一致判断歧义类型，实验效度才会受损。

我建议将此降级为 Should-Fix：在 camera-ready 中补充模板数量、筛选率、rejection criteria 的具体数字，并在 Appendix 中给出 5-10 个完整的 clause pair 示例（当前 Table 1 仅有类型定义，无完整示例）。实际上 Appendix S 已有部分示例（"Clause Pair Examples"），但应扩展。

---

### Should-Fix 问题

**[AGREE] R1-W1: LLM 失败模式编码的循环性风险**

同意。§6 提到 mutual information 作为循环性的间接证据（"mutual information between type (exogenous) and mechanism labels provides structural evidence against this"），但未直接回答 R1 的核心问题：**LLM coder 的 prompt 是否包含类型标签？** 如果 coder 知道每个 trace 对应的歧义类型，type→mechanism 的 NMI = 0.23 可能部分被 prompt 污染。这是我的 Q3 也追问的问题。

此外，§6 报告 Gwet's AC₁ = 0.62, κ = 0.52——两个一致性指标的差异（0.62 vs 0.52）暗示 prevalence bias 或 marginal distribution 不均。论文选择报告 AC₁ 作为主指标是合理的（AC₁ 对 prevalence bias 更鲁棒），但 §Limitations 中仅提及 "failure mode coding relies on LLM annotators (κ=0.52)"，选择性引用了较低的数字，造成了刻意保守的印象——或者说前后不一致。

---

**[AGREE] R1-W2: SESOI ±15 pp 的 justification 问题**

同意 justification 不够 principled。但我比 R1 温和：论文提供了 Table 3（TOST sensitivity across 7 margins, ±5 to ±20 pp），这实质上已经承认 ±15 pp 是一个特定选择。关键发现（incompleteness 和 coreferential 分离，mid-tier cluster）在 ±12 到 ±18 pp 范围内稳定。所以 SESOI 的具体值对结论的影响有限。

建议：在 §4.6 中明确 ±15 pp 是 pragmatic default 而非 principled threshold，并引导读者参考 Table 3 的 sensitivity analysis 作为主要证据。

---

**[AGREE] R1-W3: ICC 复制仅限 OpenAI 家族**

同意。§4.5 说 "ICC is computed within the OpenAI family"，又用 "cross-provider stability is supported by C1 consistency across all seven models" 来弥补，但 C1 consistency（方向一致）和 ICC（clause-level reproducibility）是不同层次的证据。同家族模型可能共享训练数据导致 clause-level response pattern 相似，从而膨胀 ICC。跨家族 ICC 未报告是一个真实缺口。

---

**[AGREE] R1-W4: Human validation per-type 样本量不足**

同意。论文自身已承认这一限制（§4.4 "per-type estimates (n≈32-34) have wide confidence intervals and should not be interpreted as type-level reliability guarantees"），但仍然在 §4.4 的 paragraph 标题中使用了 "Human validation" 这一全称，可能给读者过强的可靠性印象。

---

**[AGREE] R1-W5: Cross-domain type ranking ρ=0.26 削弱 C2 泛化性**

强烈同意。这是我审稿时未充分注意的一点。ρ=0.26（p=0.62）意味着 retail 和 airline 两个 domain 的类型排序几乎无关。如果 C2 的类型偏序在两个 customer-service 子域之间都不能泛化，那么论文对 "type-targeted diagnosis for policy-governed deployments"（Conclusion）的实际建议就缺乏根基。

结合我自己的 W1（authorization scope 构念效度存疑）：如果排除 auth scope，跨域 ρ 是否改善？论文在 §5.2 中报告排除 auth scope 后 cross-judge ρ 从 0.09 升至 0.90，但未报告排除 auth scope 后的跨域 ρ。这个数字对理解 C2 的泛化性至关重要。

---

**[REBUT] R1-W6: Prevalence audit 可靠性——严重程度应降低**

部分同意 κ=0.295 很低，但不同意这是一个 Should-Fix 级别的问题。Prevalence audit（Appendix AA）是一个补充性的 real-world grounding 分析，不是论文的核心实验。它的目的是说明 "policy ambiguity 在真实文档中普遍存在"（55-87%），为研究动机提供背景。即使完全删除这个 audit，论文的核心因果分析、方差分解和 error analysis 不受影响。

建议降级为 Minor：在 Appendix AA 中明确标注 κ=0.295 的低可靠性，并将 55-87% 的范围解读为 "初步估计" 而非确定结论。

---

### Minor 问题

**[AGREE] R1-M1:** "Nocuous" 术语的 Berry & Kamsties (2004) 含义 vs 本文的反转含义确实应在首次使用时标注。§1 第一段引入了 nocuous/innocuous 的原始含义，但 "nocuity inversion"（§6.3 的 systematic nocuity）的概念要到第 7 页才出现。读者在阅读标题和前几页时可能会按原始含义理解，产生误解。

**[AGREE] R1-M2:** Temperature=0 限制。同意，我也在 M3 中提到。

**[REBUT] R1-M3:** 3 个 Qwen3 API errors（3/3000 = 0.1%）不构成 systematic missingness 的风险。除非这 3 个 episode 在某个类型/条件中聚集，否则不影响任何结论。论文报告了总数（2,997 episodes），透明度足够。这个 concern 过度了。

**[AGREE] R1-M4:** Table 2 脚注 ‡ 确实应标注 auth scope 的 per-type calibration 样本量（n≈17）。

**[AGREE] R1-M5:** 未独立验证 appendix 交叉引用一致性，但如果存在不一致则应修复。

---

### Questions 回应

**R1-Q1（模板设计）：** 同意需要澄清。我在 N3 的 rebut 中已建议在 camera-ready 中补充细节。

**R1-Q2（SOPBench power analysis）：** 好问题。SOPBench 每模型样本量（n 未在正文中明确报告）可能不足以检测 12.6 pp 的效应。如果 underpowered，2/5 不显著可能是 Type II error 而非真实无效应。

**R1-Q3（LLM coder prompt 是否含类型标签）：** 关键问题，我完全同意需要作者明确回答。

**R1-Q4（ρ=0.26 的实际含义）：** 与 W5 一致。ρ=0.26 意味着 type-specific 建议不能在未经域内验证的情况下跨域推广。这直接影响论文 Conclusion 中 "type-targeted diagnosis" 的实用价值。

**R1-Q5（22.4% clause-level variance 的分布形态）：** 有意义的问题——如果少数高影响子句驱动了大部分 variance，"clause-level auditing" 的建议就更有操作性（先审高风险子句）。

**R1-Q6（Concordant-violation vs concordant-no-violation）：** 论文报告 41.3% 触发多数收敛违规、13.0% 全模型一致违规。但未报告多数收敛无违规的比例——这个比例对理解 "systematic nocuity" 的相对普遍性很重要。如果 80% 的子句在所有模型中都不引发违规，那么 41.3% 的收敛违规率（在总歧义子句中而非仅违规子句中的比例）会更有信息量。

---

### Missing References 回应

**[REBUT] Lu et al. 2022 (prompt order sensitivity):** 相关性有限。本文的 matched-pair 设计控制了 prompt 位置（子句在同一 policy document 中的同一位置被替换），order sensitivity 不是本研究的混杂因素。

**[AGREE] Kadavath et al. 2022 (self-calibration):** 同意。Kadavath et al. 关于 LLM 校准不确定性的能力直接关联 disambiguation neglect 发现（§6.2）——agent 不仅不表达不确定性，可能根本无法检测到自己处于歧义条件下。这为 "disambiguation neglect" 提供了更深层的理论解释。

**[REBUT] Constitutional AI / RLHF alignment literature:** 过于宽泛。论文已引用了 safety training 相关工作（§2 Agent Safety Evaluation 段），且 permissive attractor 的讨论（§6.3）隐含了 RLHF 对 helpfulness 的优化可能导致 permissive bias。如果 R1 能指出具体文献（如 Bai et al. 2022 的 helpful-harmless trade-off），建议会更 actionable。

---

### Overall Assessment 回应

R1 给出 3.5（Borderline Conference），与我的评分一致。我们在核心判断上高度趋同：方法论严谨但 novelty 不够突出，external validity 存疑。

两份审稿的主要分歧在于 N3（clause pair construction transparency）：R1 列为 Must-Fix，我认为 Should-Fix 更合适（数据承诺发布 + §4.2 已有关键信息）。其余主要问题（synthetic vs natural gap、incompleteness confound、auth scope validity）两份审稿独立发现了相同的关切。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2125 · 2026-05-23T08:27:03.722516+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 203

## Round 203

2 recorded events


### User

_source line 2126 · 2026-05-23T08:27:06.283785+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- R1 的 9 个 Weakness 中，我 **AGREE 7 个**（N1, N2, W1-W5），**REBUT 2 个**（N3 应降为 Should-Fix、W6 应降为 Minor）
- R1 的 5 个 Minor 中，AGREE 4 个、REBUT 1 个（M3，3/3000 API error 不构成 systematic missingness）
- R1 的 3 个 Missing References 中，AGREE 1 个（Kadavath 2022）、REBUT 2 个
- 两份审稿独立收敛于相同的核心关切：synthetic-natural 效应差距、incompleteness 混杂、authorization scope 构念效度
- 两份审稿评分一致：3.5 Borderline Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2127 · 2026-05-23T08:27:12.843559+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 204

## Round 204

10 recorded events


### User

_source line 2128 · 2026-05-23T08:27:14.347096+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 核心贡献的 novelty framing**

同意 R2 的判断。Matched-pair 本身是心理语言学和 RE 的成熟方法，"first matched-pair causal study" 的 novelty claim 本质上是领域迁移。"ambiguity → more errors" 方向上确实可预测——这类研究的价值在于量化 how much 和 which kind，而非 whether。

不过需要指出，论文在 §3 已经有部分自我限定："Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard"（§3, Scope of 'ambiguity' 段）。问题是这一定位没有贯穿到 §1 的 contributions 列表和 Abstract 中。R2 建议的 reframing 方向（"first quantification of differential effect + diagnostic taxonomy"）更准确地反映了实际贡献：(1) 量化了效应量级（+18.7 至 +36.0 pp confound-free range），(2) 发现 type 预测 mechanism（NMI = 0.23）远强于预测 violation rate（NMI = 0.01），后者是真正非平凡的发现。

**[AGREE] R2-N2: Taxonomy 新颖性和 C3 层效应**

完全同意。论文自身在 §5.2 已承认 C3 未通过 Holm-Bonferroni 校正（"p = 0.017, adjusted threshold 0.0125"），但 §3 的叙事仍围绕 "two layers—linguistic and specification" 展开，§1 的 Introduction 也强调 "six-type taxonomy organized into two layers"。C3 失败意味着两层结构在当前数据下是一个未得到支持的假设，论文不应在叙事中将其作为已确立的组织原则。

补充我自己的观察：两层结构的假设（linguistic ambiguity 可通过 tool responses / world knowledge 部分解消，specification ambiguity 无外部解消渠道）在 §3 末尾被提出（"We test this empirically"），但 C3 的失败恰恰意味着这个理论预测没有得到验证。§5.2 对此的处理是诚实的，但 §3 和 §1 需要同步更新叙事——将两层结构降格为描述性的组织框架而非经验性的 claim。

---

### Should-Fix 问题

**[AGREE] R2-W1: Authorization scope 构念效度**

强烈同意。这与我自己审稿中的观察一致。Authorization scope 在多个维度上是 outlier：
- 最低 inter-judge κ = 0.385（Table in §4.4; Appendix I）
- 近零 cross-judge-group type ranking（ρ = 0.09, Appendix L）
- 驱动全部 C4 interaction（排除后 p = 0.97, Appendix N）
- 最低 within-type ICC（0.29; replication ICC ≈ 0, Appendix Z）
- 最大跨模型方差（52 pp range, Figure 3）

论文已提供排除 auth scope 后 C4 消失的分析（Appendix N），以及排除后 cross-judge ρ = 0.90 (Appendix L)。但 R2 的要求很合理：应报告排除 auth scope 后的 C1 pooled Δ、方差分解、和 NMI。当前论文仅报告了排除 incompleteness 后的 C1（Appendix Q: Δ = 31.0 pp），但没有排除 auth scope 后的对应分析。这不需要新实验——只需对现有数据重新计算。

**[AGREE] R2-W2: Incompleteness 混杂 framing**

同意。这与我 N2 的核心观点一致。Abstract 中 "34.0 percentage points (+18.7 to +36.0 pp in confound-free types)" 在一句话中压缩了两个不同层次的信息：34.0 pp 包含 incompleteness，confound-free range 排除了它。一个更诚实的 framing 是将 confound-free pooled effect（+31.0 pp, 95% CI [27.9, 34.1], Appendix Q）作为 headline，将 34.0 pp 标注为 "including the incompleteness upper bound"。3 pp 的差距虽然不大，但 framing 的透明性本身是方法论严谨性的体现。

**[AGREE] R2-W3: SOPBench 效应量大幅缩小**

同意。这与我 N1 的核心观点一致。"Directional consistency" 是一个弱标准——五个模型都 > 0 只说明方向没反转，不能证明效应量级具有跨 benchmark 稳定性。更重要的是，SOPBench 上 2/5 模型不显著（GPT-5.4 p=0.052, DeepSeek p=0.163），这在 5 个模型中是 non-trivial 的失败率。论文的 structured attribution（measurement grain + baseline compression + interaction depth）虽然每个因素都合理，但三个因素同时作用且各自的贡献量无法分离，使归因本质上不可验证。

建议：在 Discussion 中增加一段正式讨论生态效度，将 "34.0 pp (synthetic τ²-bench) → 12.6 pp (more naturalistic SOPBench)" 框定为效应量的可能范围，而非将 SOPBench 结果放在 Appendix 中弱化其重要性。

**[PARTIALLY AGREE] R2-W4: 方差分解叙事偏重已解释部分**

部分同意。§7 的 framing "Even perfect disambiguation would address at most 22.4% of variance" 是一个有效的 intervention ceiling 论证——它告诉从业者即使完美消歧也只能解决 22.4% 的问题。但 R2 的观点也有道理：60.8% 的未解释方差意味着论文的模型对违规结果的预测力有限（Total $R^2 \approx 0.39$）。

不过，论文在 Appendix Z 中已经对残差进行了进一步分解（~15% stochastic + ~46% systematic，基于 ICC = 0.749），并且讨论了 86.5% 的 cell unanimity。这比大多数同类工作做得更多。建议在 §5.1 或 §7 正文中补充一句承认 60.8% 残差是当前模型解释力的限制，而不仅仅是 intervention ceiling。

**[AGREE] R2-W5: NMI cardinality 不对称**

这是 R2 审稿中最精准的技术点。同意。

Type→mechanism 是 6×5（最大可能 NMI 受限于 min(H(type), H(mechanism))），type→violation 是 6×2（二分结果的 H(violation) ≤ 1 bit，严重压缩了 MI 的上界）。即使 type 对 violation rate 有中等预测力，NMI 在低 cardinality target 下也会被压缩。论文报告的 "order of magnitude" 差异（0.23 vs 0.01）中，部分差异可能是 cardinality artifact 而非实质性差异。

论文确实也报告了 Cramér's V = 0.45（type→mechanism, Table in Appendix U）和 Cramér's V = 0.137（type→violation rate omnibus, §5.2），后者的比较更公平（V 不受 cardinality 影响的方式与 NMI 不同），但 V = 0.45 vs V = 0.137 的比值约为 3.3×，远小于 NMI 的 16.8×。建议正文中 (1) 承认 NMI 比较受 cardinality 不对称影响，(2) 以 Cramér's V 的比较作为补充或替代。

---

### Minor 问题

**[AGREE] R2-M1**: Abstract 信息密度确实过高。8 个数字在一段中密集出现（34.0 pp, +18.7, +36.0, 22.4%, 0.4%, 77%, NMI 暗示引用）。建议精简至 4-5 个核心数字。

**[AGREE] R2-M2**: C3/C4 的编号确实暗示四个同等级别的 claim，但 C3 未通过校正、C4 是 exploratory。建议在 §5 开头明确标注 claim 层级。论文已在 §5 首段提到 "C1 and C2 are primary claims; C4 is exploratory"，但 C3 的 inconclusive status 可以更突出。

**[AGREE] R2-M3**: Temperature=0 局限性。同我 M2。

**[REBUT] R2-M4**: Figure 1 的信息量问题。Figure 1 作为 overview figure 的功能是帮助读者快速理解实验流程——taxonomy → τ²-bench injection → cross-judge evaluation。在 8 页正文限制下，Figure 1 承担的是导航功能而非信息传达功能。如果增加更多细节（如每种类型的示例），可能反而降低可读性。这是审美判断而非方法论问题。

**[PARTIALLY AGREE] R2-M5**: "Nocuous" 对非 RE 读者的可读性。同我 M1。标题中使用确实可能降低可发现性，但该词是论文核心论点的精准术语（来自 Berry & Kamsties 2004）。建议保留标题但在 Abstract 首次使用时加入简短定义（当前已有 "i.e., harmful"）。

---

### Questions

**[AGREE] R2-Q1**: SOPBench 效应缩小对实际启示的影响。同我 N1。合成条件下 34.0 pp → 更自然条件下 12.6 pp 的 gap 对论文的 practical implications 段（如果有的话——当前 §7 讨论较短）需要更诚实的讨论。

**[AGREE] R2-Q2**: 排除 auth scope 后 C1 和方差分解。如上述 W1 回应，这只需对现有数据重新计算，不需要新实验。

**[AGREE] R2-Q3**: LLM 编码的低 κ 对 NMI 的影响。这是一个重要的关联点。如果 mechanism coding 的 reliability 只有 κ = 0.52，那么 type→mechanism 的 NMI = 0.23 实际上是在 noisy labels 上计算的——真实 NMI 可能更高（noise attenuation）或更低（systematic coding bias）。论文应讨论 measurement error 对 NMI estimates 的影响方向。

**[PARTIALLY AGREE] R2-Q4**: 77% permissive bias 是否是 customer-service domain artifact。这是一个合理的假设——customer service 领域可能固有地倾向 permissive 解释（customer satisfaction 压力）。但论文的跨域分析（Appendix O）显示 permissive bias 在 retail 和 airline 两个领域都成立（虽然论文未分域报告 permissive 比例）。如果两个领域的 permissive 比例一致，则 domain artifact 解释被弱化。但如果仅在 customer service 域内一致，泛化性仍存疑。建议作者在 rebuttal 中报告分域 permissive 比例。

**[PARTIALLY AGREE] R2-Q5**: Disambiguation neglect 的模型差异来源。R2 指出这可能是 safety training 差异而非 ambiguity processing 差异——有道理。GPT-4.1 和 Claude 的高 awareness（10-11%）可能反映其 safety training 中包含了 "when uncertain, ask" 的行为模式，而非更深层的歧义感知能力。但论文的数据无法区分这两个假设——需要 ablation 研究（如在无 safety system prompt 下测试）。论文 §6.2 的 framing "The absence reflects default behavior, not inability" 实际上与 R2 的观点兼容（引用 Vijayvargiya et al., 2026 关于 interactive disambiguation 的恢复能力）。建议在 §6.2 中增加一句明确讨论 safety training vs ambiguity processing 的混淆。

---

### Missing References

**[NO COMMENT]** R2 建议的三篇参考文献（AgentSpec ICSE 2026, Agent Behavioral Contracts arXiv 2602.22302, "Check Yourself Before You Wreck Yourself" arXiv 2510.16492）——作为 Reviewer 我无法独立验证这些引用的存在性和相关性。如果确实存在且相关，它们属于 agent runtime specification enforcement 方向，与本文的 policy specification analysis 互补但不重叠。建议作者在 revision 中自行检查并酌情引用。

---

### 综合评估

R2 的审稿质量高，多数意见与我的独立判断一致。我们在以下核心问题上达成共识：
1. **外部效度**是最大风险（SOPBench 63% 效应压缩）
2. **Incompleteness confound** 需要更突出的 framing
3. **Authorization scope** 的构念效度问题系统性地影响多个分析
4. **C3 层效应失败**但叙事未充分调整
5. **Failure mode coding** 缺人工验证

R2 提出的 NMI cardinality asymmetry（W5）是我遗漏的有价值的技术点。

我与 R2 的唯一实质性分歧在 Figure 1（M4）——我认为当前 overview figure 在页限下功能合理。

**维持我的评分：Overall 3.5 (Borderline Conference)**，与 R2 一致。论文的核心方法论框架（matched-pair design + variance decomposition + type→mechanism mapping）是扎实的，但外部效度和若干验证缺口将其限制在 Borderline Conference / strong Findings 区间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2129 · 2026-05-23T08:27:39.419629+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2130 · 2026-05-23T08:27:39.771387+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T08:16:22.520223+00:00\", \"completed_at\": \"2026-05-23T08:19:52.432532+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 4-6\", \"message\": \"连续三页纯文本（§4 Experimental Platform → §5.2 Type Partial Ordering），无任何 figure/table/equation 穿插。审稿人在方法-结果过渡段会感到视觉疲劳。建议在 page 5-6 区域插入一个结果摘要表或关键效应量的 forest plot，打破文本墙。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 3（Model × Type 热力图）尺寸偏小，挤在右栏顶部约 1/4 栏高。单元格数值和轴标签在正常阅读距离下可能难以辨认。建议改用 figure*（全宽）或适当增大纵向空间。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 2 和 Figure 3 均出现在第 8 页（Discussion/Conclusion 区域），但其数据首次讨论在第 5-6 页的 Results 章节。Float 位置与首次引用距离约 2-3 页，审稿人需要回翻查看。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主体正文共 5 个 display items（Figure 1, Table 1, Table 2, Figure 2, Figure 3）。对于一篇以实证因果分析为核心的论文，密度偏低（8 页建议 6-8 个）。Appendix 的表格非常丰富（Tables 3-22 + Figure 5），但主体部分的视觉密度对审稿人第一印象偏弱。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（实验流程概览图）作为第一个视觉锚点出现在第 2 页顶部，位置合理，三面板布局清晰传达了实验 pipeline（Taxonomy → Evaluation → Cross-Judge），为审稿人建立了良好的认知框架。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 使用 booktabs 风格，排版干净。最优结果有标注（M/L 标记）。表格放在 Results 区域，float 位置合理。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 的 bar chart 在左栏底部，垂直空间略紧凑，误差线标注清晰，但个别 type 标签可能因缩写而不够直观。\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Appendix 单页包含 4 个表格（Tables 4-7），排版紧凑但可读。对 appendix 材料来说可接受。\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Tables 13-16 四张表堆叠在一页，其中 Table 13（clause pair examples）文字较密。在 appendix 中可接受但略显拥挤。\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"Figure 5（方差分解 stacked bar chart）清晰美观，图例可读，颜色区分度好。是 appendix 中最有效的可视化。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \
…[truncated 302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2131 · 2026-05-23T08:27:39.771774+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2132 · 2026-05-23T08:27:39.872361+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2133 · 2026-05-23T08:30:45.402050+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 24\n\n# ============================================================\n# R24 ISSUES\n# ============================================================\n\n- id: \"R24-N1\"\n  summary: \"合成→自然效应压缩 63%（34.0pp→12.6pp SOPBench），外部效度未充分讨论，Abstract/Conclusion framing 偏乐观\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 列为 Must-Fix，R2 列为 Should-Fix 但 AGREE R1 判断合理。共识：SOPBench 2/5 模型不显著，'directional consistency' 是 goalpost shifting，三因素归因不可验证\"\n  action_items:\n    - round: 24\n      action: \"Discussion 增加生态效度正式段落；Abstract/Conclusion 呈现效应量范围（12.6-34.0pp）而非仅 34.0pp\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-N2\"\n  summary: \"Incompleteness 信息添加混淆控制不足——token count proxy 粗糙，正系数解释有逻辑漏洞；framing 中 confound-free range 不够突出\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R22-W5: token count proxy 粗糙\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W1: incompleteness confound 在 headline claim 标注不够——标记为 resolved 但本轮复发\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix: β=+0.027 的 over-constraint violation 替代解释成立；R2 AGREE 但认为 0.1pp 实际影响微小，核心问题是 framing 不够突出\"\n  action_items:\n    - round: 24\n      action: \"Abstract/Conclusion 优先报告 confound-free pooled Δ=+31.0pp，34.0pp 作为含 incompleteness 上界补充\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-N3\"\n  summary: \"核心贡献 novelty framing 不够诚实——'first matched-pair causal study' 是领域迁移而非方法论创新，'ambiguity→violations' 方向可预测\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix, R1 AGREE。共识：应从'first causal study'转向'first quantification of differential effect + diagnostic taxonomy'，NMI=0.23 vs 0.01 才是非平凡发现\"\n  action_items:\n    - round: 24\n      action: \"重写 §1 contributions list 和 Abstract，弱化 'first causal' 卖点，强化 type-specific diagnostic 和 systematic nocuity 作为主贡献\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-N4\"\n  summary: \"Taxonomy 两层结构（C3）未通过 Holm-Bonferroni 校正（p=0.017 vs 阈值 0.0125），但 §3 和 §1 叙事仍围绕两层展开\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix, R1 AGREE。共识：将两层结构降格为描述性组织框架，§3 和 §1 需同步更新叙事\"\n  action_items:\n    - round: 24\n      action: \"§3 明确两层划分是组织性的而非 empirically validated claim；§1 同步调整\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W1\"\n  summary: \"Authorization scope 构念效度系统性存疑（κ=0.385, ρ=0.09, ICC≈0, 驱动全部 C4），缺少排除 auth scope 后的 C1/方差分解/NMI 敏感性分析\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R22-W1: C4 完全由 auth scope 驱动\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-N2: auth scope 低 κ 标注——标记为 resolved 但本轮发现需要更系统的敏感性分析\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix, R1 强烈 AGREE。共识：需报告排除 auth scope 后的 C1 pooled Δ、方差分解、NMI——现有数据即可计算\"\n  action_items:\n    - round: 24\n      action: \"补充排除 auth scope 后的 C1 pooled Δ、方差分解、NMI 等核心数字\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W2\"\n  summary: \"条款对构建过程不够透明——template pipeline 未描述模板数量/结构/筛选率，post-hoc realism validation 一句带过\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 列为 Must-Fix，R2 REBUT 降为 Should-Fix（理由：数据承诺发布、§4.2 已有关键信息、高 κ=0.95 是设计目标不是缺陷）。共识：需补充但非 blocking\"\n  action_items:\n    - round: 24\n      action: \"Appendix 补充模板数量、筛选标准、rejection rate；扩展 clause pair 示例至每类型 2-3 个\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W3\"\n  summary: \"失败模式编码缺乏人工验证（LLM 编码 κ=0.52），循环性风险未排除——LLM coder prompt 是否含类型标签未说明\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1]\n      note: \"R23-M3: disambiguation neglect 推断边界需收窄——标记为 resolved\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix, R2 AGREE。共识：需明确 coder prompt 是否含类型信息，至少 50-100 条 trace 的人工验证\"\n  action_items:\n    - round: 24\n      action: \"明确 LLM coder prompt 设计；对 50-100 条 trace 进行人工失败模式编码验证\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W4\"\n  summary: \"SESOI ±15pp justification 不够 principled——'>2× 噪声'和'不需不同缓解策略'均非领域接地论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"首次提出\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W4: 标记为 resolved（替换为 pragmatic threshold）但本轮复发\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix, R2 AGREE 但认为 Table 3 sensitivity analysis 已缓解。共识：明确标注 pragmatic default，引导读者参考 Table 3\"\n  action_items:\n    - round: 24\n      action: \"§4.6 进一步明确 ±15pp 是 pragmatic default 而非 principled threshold；正文中更突出引用 Table 3 的 ±10/±12pp 结果\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W5\"\n  summary: \"ICC 复制仅限 OpenAI 家族，跨提供商 clause-level reproducibility 未直接验证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 22\n      reviewers: [1]\n      note: \"R22-W3: ICC 复制仅覆盖 OpenAI 家族——标记为 resolved\"\n    - round: 23\n      reviewers: [1]\n      note: \"R23-W3: OpenAI-family qualifier 不充分——标记为 resolved\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix, R2 AGREE。共识：需明确标注范围限制，讨论跨提供商 ICC 可能更低的含义\"\n  action_items:\n    - round: 24\n      action: \"讨论跨提供商 ICC 可能更低的含义，明确标注范围限制\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W6\"\n  summary: \"Human validation per-type 样本量不足（n≈32-34），CI 极宽（coreferential κ CI [0.00, 0.84]），但仍被引用作论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix, R2 AGREE。共识：增加样本量或在引用 per-type κ 时始终附 CI\"\n  action_items:\n    - round: 24\n      action: \"引用 per-type κ 时附带 CI；理想情况下增加 human validation 至 per-type ≥50\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W7\"\n  summary: \"Cross-domain type ranking ρ=0.26（p=0.62），C2 类型偏序高度领域依赖，'type-targeted diagnosis' 建议缺乏跨域根基\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix, R2 强烈 AGREE。共识：§5.2 或 §7 需显著讨论领域依赖性，Conclusion 限定适用范围\"\n  action_items:\n    - round: 24\n      action: \"§7 讨论 C2 领域依赖性；Conclusion 限定 type-targeted diagnosis 的适用范围（within customer-service domain）\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W8\"\n  summary: \"NMI 比较的 cardinality 不对称——type→mechanism (6×5) vs type→violation (6×2)，'order of magnitude' 表述可能含 artifact\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [2]\n      note: \"R2 Should-Fix, R1 AGREE 并补充 Cramér's V 比较（0.45 vs 0.137 = 3.3×，远小于 NMI 的 16.8×）\"\n  action_items:\n    - round: 24\n      action: \"正文承认 NMI 受 cardinality 不对称影响；以 Cramér's V（3.3× ratio）作为补充或替代'order of magnitude'表述\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W9\"\n  summary: \"方差分解叙事偏重已解释部分（22.4%），60.8% 残差被包装为 intervention ceiling 而非研究解释力限制\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [2]\n      note: \"R2 Should-Fix, R1 PARTIALLY AGREE（认为 Appendix Z 的 ICC 分解已足够，但正文可补充一句）\"\n  action_items:\n    - round: 24\n      action: \"§5.1 或 §7 补充一句承认 60.8% 残差是当前模型解释力的限制\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-M1\"\n  summary: \"Abstract 信息密度过高（8 个数字），影响可读性\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均提及，建议精简至 3-4 个核心数字\"\n\n- id: \"R24-M2\"\n  summary: \"'Nocuous' 术语反转（Berry & Kamsties 2004: divergent → 本文: convergent）未在首次使用时标注\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均同意需在 Abstract 首次使用时简要标注\"\n\n- id: \"R24-M3\"\n  summary: \"Temperature=0 对结论泛化性的影响未在 Limitations 中提及\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均同意需在 Limitations 补充\"\n\n- id: \"R24-M4\"\n  summary: \"C3/C4 编号暗示四个同等级别 claim，实际仅 C1/C2 是 supported primary claims\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"§5 开头应更明确标注 claim 层级\"\n\n- id: \"R24-M5\"\n  summary: \"Table 2 脚注 ‡ 标注 auth scope 低 κ 但未标注 per-type calibration 样本量（n≈17）\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 AGREE\"\n\n- id: \"R24-M6\"\n  summary: \"Prevalence audit（Appendix）κ=0.295，Introduction 引用时未标注低可靠性\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 列为 Should-Fix，R2 REBUT 降为 Minor（不影响核心分析）。共识：标注即可\"\n\n# ============================================================\n# R23 ISSUES — ALL RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R23-N1\"\n  summary: \"正文超 8 页限制（Discussion+Conclusion 溢出至 p9，约 8.4-8.5 页）\"\n  category: format\n  severity: critical\n  status: resolved\n  resolution: \"§5.1 C1 compressed (perturbation→§4 ref, permutation 1-sentence). Discussion merged 3→2 ¶ then further trimmed. Conclusion compressed. Variance decomposition figure moved to Appendix. Visual verification: Conclusion ends on p8, Limitations starts p9.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-N2\"\n  summary: \"Authorization scope 类型系统性不可靠（κ=0.385, ICC≈0, 单独驱动 ρ=0.09 和 C4 interaction），但在主分析中未充分标注\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Table 2: ‡ added to Auth Scope row + footnote ('Interpret with caution: lowest inter-judge agreement κ=0.385'). §5.2: excluding-auth-scope sentence added ('remaining five types preserve same partial ordering').\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R23-W1\"\n  summary: \"Incompleteness confound 在 headline claim (34.0pp) 中的标注不够显著——framing 问题 [复发×3: R21-W3→R22-M4→R23-W1]\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Abstract reframed: '+34.0pp (+18.7 to +36.0pp in confound-free types)'. Table 2 footnote added with excl-incomp pooled Δ=+31.0pp.\"\n  resolution_round: 23\n  first_raised_round: 21\n  last_seen_round: 24\n\n- id: \"R23-W2\"\n  summary: \"跨 judge 组类型排名 ρ=0.09→排除 auth scope 后 ρ=0.90 的 post-hoc 嫌疑 [复发×2: R21-N3→R23-W2]\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"§5.2 rewritten: three-family validation (ρ=0.71-0.89) now leads as primary evidence; ρ=0.09 exclusion framed as 'sensitivity check'.\"\n  resolution_round: 23\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: \"R23-W3\"\n  summary: \"Residual variance decomposition (15% stochastic + 46% systematic) 仅基于 OpenAI family，主文中未逐处限定 [复发×2: R22-W3→R23-W3]\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"OpenAI-family qualifier added in all three locations: §5.1 C1 paragraph, Figure caption (now in Appendix), and §7 Discussion.\"\n  resolution_round: 23\n  first_raised_round: 22\n  last_seen_round: 24\n\n- id: \"R23-W4\"\n  summary: \"TOST ±15pp SESOI 的 justification 有 pragmatic/circular 成分 [复发×4: R20→R21→R22→R23]\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Replaced 'satisfies two principled criteria (Lakens 2017)' with 'pragmatic threshold'. Removed Lakens from SESOI justification (kept at TOST method cite). Bootstrap cluster analysis promoted to parallel primary evidence. Verbose acknowledgment paragraph removed.\"\n  resolution_round: 23\n  first_raised_round: 20\n  last_seen_round: 24\n\n- id: \"R23-W5\"\n  summary: \"Cross-judge calibration per-type κ 缺少 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"§4.4 method.tex: added 'per-type estimates carry wide confidence intervals at n≈17 per type (Appendix)' qualifier. Appendix per_type_agreement table already has bootstrap CIs for human-LLM κ.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-W6\"\n  summary: \"合成歧义的生态效度——未提供真实企业策略文档的歧义案例 [复发×2: R22-M1→R23-W6，升级 warning]\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Discussion §7 ¶1: added synthetic→real-world gap threats sentence (correlated ambiguities, domain jargon, implicit organizational context).\"\n  resolution_round: 23\n  first_raised_round: 22\n  last_seen_round: 24\n\n- id: \"R23-M1\"\n  summary: \"NMI 0.23 vs 0.01 的 order of magnitude 表述需要绝对值语境化\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Discussion taxonomy paragraph: added '(moderate association: NMI = 0.23 vs. 0.01, Cramér's V = 0.45)'.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M2\"\n  summary: \"Abstract 信息过载（约 150 词内 6+ 个定量结果）\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Abstract trimmed to 3 core numbers (34.0pp, confound-free range, 22.4%). Removed OR, p-values, ≤11%, 40%, 0.4%.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R23-M3\"\n  summary: \"Disambiguation neglect 推断边界需收窄\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"§6.2 analysis.tex: added 'externally expressed' before 'disambiguation awareness'.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M4\"\n  summary: \"Table 2 Overall 行应增加 excl-incompleteness 汇总\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Table 2 footnote: 'Excluding incompleteness: pooled Δ=+31.0pp (95% CI [27.9, 34.1])'.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M5\"\n  summary: \"Token count 作为 incompleteness confound control 是粗糙 proxy\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"Confirmed: Limitations §Confounds already states 'Token-count difference...is an imperfect proxy for informational asymmetry; future work could employ semantic complexity metrics'.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M6\"\n  summary: \"§4.3 'five architecturally diverse models' 表述不准确\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Changed to 'five models from four providers spanning two architecture families' in method.tex §4.3.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M7\"\n  summary: \"References arXiv 引用格式不统一\"\n  category: format\n  severity: minor\n  status: resolved\n  resolution: \"Fixed 2 entries (lin_ask_to_clarify_2025, mu_can_llms_2023): @inproceedings→@article, booktitle→journal. All arXiv entries now use consistent @article format.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n# ============================================================\n# R22 ISSUES — ALL RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R22-W1\"\n  summary: \"C4 model×type 交互完全由 authorization scope 驱动，该类型测量不可靠（κ=0.385, ICC≈0），C4 可能是测量伪影\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Removed C4 subsection; compressed to 1 caveat paragraph explicitly framing C4 as possibly reflecting measurement instability.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n\n- id: \"R22-W2\"\n  summary: \"SOPBench 复制效应压缩 63%（34.0pp→12.6pp），缺乏原则性归因\"\n  category: experiment\n  severity: warning\n  status: resolved\n  resolution: \"Added principled framing in §5.1 and structured attribution in Appendix SOPBench section.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-W3\"\n  summary: \"ICC 复制仅覆盖 OpenAI 家族，但残差方差分解应用于所有模型\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Added OpenAI-family qualifier in §5.1 and Limitations §Scope. R23 found qualifier insufficient at some mentions — addressed in R23-W3.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n\n- id: \"R22-W4\"\n  summary: \"SESOI ±15pp 缺乏领域接地论证，为统计驱动而非领域驱动\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Added explicit acknowledgment in §4.6.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n\n- id: \"R22-W5\"\n  summary: \"Token count 作为 incompleteness information-addition confound 代理过于粗糙\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Confound caveat added to §6.3 and Limitations §Confounds.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n\n- id: \"R22-W6\"\n  summary: \"残差方差（60.8%）的干预天花板讨论不够充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Added intervention ceiling paragraph in Discussion §7.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M1\"\n  summary: \"生态效度缺口未量化\"\n  category: framing\n  severity: minor\n  status: resolved\n  resolution: \"Added dose-response study suggestion and SOPBench lower bound in Limitations. R23-W6 found Discussion needs more specific threats — addressed there.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n\n- id: \"R22-M2\"\n  summary: \"层级结构（C3）未通过 Holm-Bonferroni 校正\"\n  category: framing\n  severity: minor\n  status: resolved\n  resolution: \"Already addressed: §5.2 explicitly states organizational convenience.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M3\"\n  summary: \"人工 failure-mode 编码验证缺失\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"Limitations §Measurement states validation underway.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M4\"\n  summary: \"Table 2/Figure 2 中 incompleteness 应标注 confound status\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added dagger marker and footnote in Table 2.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M5\"\n  summary: \"Conclusion 偏短\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added diagnostic protocol and disambiguation neglect summary.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 24\n\n# ============================================================\n# R24 ISSUES\n# ============================================================\n\n- id: \"R24-N1\"\n  summary: \"合成→自然效应压缩 63%（34.0pp→12.6pp SOPBench），外部效度未充分讨论，Abstract/Conclusion framing 偏乐观\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 列为 Must-Fix，R2 列为 Should-Fix 但 AGREE R1 判断合理。共识：SOPBench 2/5 模型不显著，'directional consistency' 是 goalpost shifting，三因素归因不可验证\"\n  action_items:\n    - round: 24\n      action: \"Discussion 增加生态效度正式段落；Abstract/Conclusion 呈现效应量范围（12.6-34.0pp）而非仅 34.0pp\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-N2\"\n  summary: \"Incompleteness 信息添加混淆控制不足——token count proxy 粗糙，正系数解释有逻辑漏洞；framing 中 confound-free range 不够突出\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R22-W5: token count proxy 粗糙\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W1: incompleteness confound 在 headline claim 标注不够——标记为 resolved 但本轮复发\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix: β=+0.027 的 over-constraint violation 替代解释成立；R2 AGREE 但认为 0.1pp 实际影响微小，核心问题是 framing 不够突出\"\n  action_items:\n    - round: 24\n      action: \"Abstract/Conclusion 优先报告 confound-free pooled Δ=+31.0pp，34.0pp 作为含 incompleteness 上界补充\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-N3\"\n  summary: \"核心贡献 novelty framing 不够诚实——'first matched-pair causal study' 是领域迁移而非方法论创新，'ambiguity→violations' 方向可预测\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix, R1 AGREE。共识：应从'first causal study'转向'first quantification of differential effect + diagnostic taxonomy'，NMI=0.23 vs 0.01 才是非平凡发现\"\n  action_items:\n    - round: 24\n      action: \"重写 §1 contributions list 和 Abstract，弱化 'first causal' 卖点，强化 type-specific diagnostic 和 systematic nocuity 作为主贡献\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-N4\"\n  summary: \"Taxonomy 两层结构（C3）未通过 Holm-Bonferroni 校正（p=0.017 vs 阈值 0.0125），但 §3 和 §1 叙事仍围绕两层展开\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix, R1 AGREE。共识：将两层结构降格为描述性组织框架，§3 和 §1 需同步更新叙事\"\n  action_items:\n    - round: 24\n      action: \"§3 明确两层划分是组织性的而非 empirically validated claim；§1 同步调整\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W1\"\n  summary: \"Authorization scope 构念效度系统性存疑（κ=0.385, ρ=0.09, ICC≈0, 驱动全部 C4），缺少排除 auth scope 后的 C1/方差分解/NMI 敏感性分析\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R22-W1: C4 完全由 auth scope 驱动\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-N2: auth scope 低 κ 标注——标记为 resolved 但本轮发现需要更系统的敏感性分析\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix, R1 强烈 AGREE。共识：需报告排除 auth scope 后的 C1 pooled Δ、方差分解、NMI——现有数据即可计算\"\n  action_items:\n    - round: 24\n      action: \"补充排除 auth scope 后的 C1 pooled Δ、方差分解、NMI 等核心数字\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W2\"\n  summary: \"条款对构建过程不够透明——template pipeline 未描述模板数量/结构/筛选率，post-hoc realism validation 一句带过\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 列为 Must-Fix，R2 REBUT 降为 Should-Fix（理由：数据承诺发布、§4.2 已有关键信息、高 κ=0.95 是设计目标不是缺陷）。共识：需补充但非 blocking\"\n  action_items:\n    - round: 24\n      action: \"Appendix 补充模板数量、筛选标准、rejection rate；扩展 clause pair 示例至每类型 2-3 个\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W3\"\n  summary: \"失败模式编码缺乏人工验证（LLM 编码 κ=0.52），循环性风险未排除——LLM coder prompt 是否含类型标签未说明\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1]\n      note: \"R23-M3: disambiguation neglect 推断边界需收窄——标记为 resolved\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix, R2 AGREE。共识：需明确 coder prompt 是否含类型信息，至少 50-100 条 trace 的人工验证\"\n  action_items:\n    - round: 24\n      action: \"明确 LLM coder prompt 设计；对 50-100 条 trace 进行人工失败模式编码验证\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W4\"\n  summary: \"SESOI ±15pp justification 不够 principled——'>2× 噪声'和'不需不同缓解策略'均非领域接地论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"首次提出\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W4: 标记为 resolved（替换为 pragmatic threshold）但本轮复发\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix, R2 AGREE 但认为 Table 3 sensitivity analysis 已缓解。共识：明确标注 pragmatic default，引导读者参考 Table 3\"\n  action_items:\n    - round: 24\n      action: \"§4.6 进一步明确 ±15pp 是 pragmatic default 而非 principled threshold；正文中更突出引用 Table 3 的 ±10/±12pp 结果\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W5\"\n  summary: \"ICC 复制仅限 OpenAI 家族，跨提供商 clause-level reproducibility 未直接验证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 22\n      reviewers: [1]\n      note: \"R22-W3: ICC 复制仅覆盖 OpenAI 家族——标记为 resolved\"\n    - round: 23\n      reviewers: [1]\n      note: \"R23-W3: OpenAI-family qualifier 不充分——标记为 resolved\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix, R2 AGREE。共识：需明确标注范围限制，讨论跨提供商 ICC 可能更低的含义\"\n  action_items:\n    - round: 24\n      action: \"讨论跨提供商 ICC 可能更低的含义，明确标注范围限制\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W6\"\n  summary: \"Human validation per-type 样本量不足（n≈32-34），CI 极宽（coreferential κ CI [0.00, 0.84]），但仍被引用作论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix, R2 AGREE。共识：增加样本量或在引用 per-type κ 时始终附 CI\"\n  action_items:\n    - round: 24\n      action: \"引用 per-type κ 时附带 CI；理想情况下增加 human validation 至 per-type ≥50\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W7\"\n  summary: \"Cross-domain type ranking ρ=0.26（p=0.62），C2 类型偏序高度领域依赖，'type-targeted diagnosis' 建议缺乏跨域根基\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix, R2 强烈 AGREE。共识：§5.2 或 §7 需显著讨论领域依赖性，Conclusion 限定适用范围\"\n  action_items:\n    - round: 24\n      action: \"§7 讨论 C2 领域依赖性；Conclusion 限定 type-targeted diagnosis 的适用范围（within customer-service domain）\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W8\"\n  summary: \"NMI 比较的 cardinality 不对称——type→mechanism (6×5) vs type→violation (6×2)，'order of magnitude' 表述可能含 artifact\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [2]\n      note: \"R2 Should-Fix, R1 AGREE 并补充 Cramér's V 比较（0.45 vs 0.137 = 3.3×，远小于 NMI 的 16.8×）\"\n  action_items:\n    - round: 24\n      action: \"正文承认 NMI 受 cardinality 不对称影响；以 Cramér's V（3.3× ratio）作为补充或替代'order of magnitude'表述\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-W9\"\n  summary: \"方差分解叙事偏重已解释部分（22.4%），60.8% 残差被包装为 intervention ceiling 而非研究解释力限制\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [2]\n      note: \"R2 Should-Fix, R1 PARTIALLY AGREE（认为 Appendix Z 的 ICC 分解已足够，但正文可补充一句）\"\n  action_items:\n    - round: 24\n      action: \"§5.1 或 §7 补充一句承认 60.8% 残差是当前模型解释力的限制\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R24-M1\"\n  summary: \"Abstract 信息密度过高（8 个数字），影响可读性\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均提及，建议精简至 3-4 个核心数字\"\n\n- id: \"R24-M2\"\n  summary: \"'Nocuous' 术语反转（Berry & Kamsties 2004: divergent → 本文: convergent）未在首次使用时标注\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均同意需在 Abstract 首次使用时简要标注\"\n\n- id: \"R24-M3\"\n  summary: \"Temperature=0 对结论泛化性的影响未在 Limitations 中提及\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均同意需在 Limitations 补充\"\n\n- id: \"R24-M4\"\n  summary: \"C3/C4 编号暗示四个同等级别 claim，实际仅 C1/C2 是 supported primary claims\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"§5 开头应更明确标注 claim 层级\"\n\n- id: \"R24-M5\"\n  summary: \"Table 2 脚注 ‡ 标注 auth scope 低 κ 但未标注 per-type calibration 样本量（n≈17）\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 AGREE\"\n\n- id: \"R24-M6\"\n  summary: \"Prevalence audit（Appendix）κ=0.295，Introduction 引用时未标注低可靠性\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 列为 Should-Fix，R2 REBUT 降为 Minor（不影响核心分析）。共识：标注即可\"\n\n# ============================================================\n# R23 ISSUES — ALL RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R23-N1\"\n  summary: \"正文超 8 页限制（Discussion+Conclusion 溢出至 p9，约 8.4-8.5 页）\"\n  category: format\n  severity: critical\n  status: resolved\n  resolution: \"§5.1 C1 compressed (perturbation→§4 ref, permutation 1-sentence). Discussion merged 3→2 ¶ then further trimmed. Conclusion compressed. Variance decomposition figure moved to Appendix. Visual verification: Conclusion ends on p8, Limitations starts p9.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-N2\"\n  summary: \"Authorization scope 类型系统性不可靠（κ=0.385, ICC≈0, 单独驱动 ρ=0.09 和 C4 interaction），但在主分析中未充分标注\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Table 2: ‡ added to Auth Scope row + footnote ('Interpret with caution: lowest inter-judge agreement κ=0.385'). §5.2: excluding-auth-scope sentence added ('remaining five types preserve same partial ordering').\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R23-W1\"\n  summary: \"Incompleteness confound 在 headline claim (34.0pp) 中的标注不够显著——framing 问题 [复发×3: R21-W3→R22-M4→R23-W1]\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Abstract reframed: '+34.0pp (+18.7 to +36.0pp in confound-free types)'. Table 2 footnote added with excl-incomp pooled Δ=+31.0pp.\"\n  resolution_round: 23\n  first_raised_round: 21\n  last_seen_round: 24\n\n- id: \"R23-W2\"\n  summary: \"跨 judge 组类型排名 ρ=0.09→排除 auth scope 后 ρ=0.90 的 post-hoc 嫌疑 [复发×2: R21-N3→R23-W2]\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"§5.2 rewritten: three-family validation (ρ=0.71-0.89) now leads as primary evidence; ρ=0.09 exclusion framed as 'sensitivity check'.\"\n  resolution_round: 23\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: \"R23-W3\"\n  summary: \"Residual variance decomposition (15% stochastic + 46% systematic) 仅基于 OpenAI family，主文中未逐处限定 [复发×2: R22-W3→R23-W3]\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"OpenAI-family qualifier added in all three locations: §5.1 C1 paragraph, Figure caption (now in Appendix), and §7 Discussion.\"\n  resolution_round: 23\n  first_raised_round: 22\n  last_seen_round: 24\n\n- id: \"R23-W4\"\n  summary: \"TOST ±15pp SESOI 的 justification 有 pragmatic/circular 成分 [复发×4: R20→R21→R22→R23]\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Replaced 'satisfies two principled criteria (Lakens 2017)' with 'pragmatic threshold'. Removed Lakens from SESOI justification (kept at TOST method cite). Bootstrap cluster analysis promoted to parallel primary evidence. Verbose acknowledgment paragraph removed.\"\n  resolution_round: 23\n  first_raised_round: 20\n  last_seen_round: 24\n\n- id: \"R23-W5\"\n  summary: \"Cross-judge calibration per-type κ 缺少 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"§4.4 method.tex: added 'per-type estimates carry wide confidence intervals at n≈17 per type (Appendix)' qualifier. Appendix per_type_agreement table already has bootstrap CIs for human-LLM κ.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-W6\"\n  summary: \"合成歧义的生态效度——未提供真实企业策略文档的歧义案例 [复发×2: R22-M1→R23-W6，升级 warning]\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Discussion §7 ¶1: added synthetic→real-world gap threats sentence (correlated ambiguities, domain jargon, implicit organizational context).\"\n  resolution_round: 23\n  first_raised_round: 22\n  last_seen_round: 24\n\n- id: \"R23-M1\"\n  summary: \"NMI 0.23 vs 0.01 的 order of magnitude 表述需要绝对值语境化\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Discussion taxonomy paragraph: added '(moderate association: NMI = 0.23 vs. 0.01, Cramér's V = 0.45)'.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M2\"\n  summary: \"Abstract 信息过载（约 150 词内 6+ 个定量结果）\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Abstract trimmed to 3 core numbers (34.0pp, confound-free range, 22.4%). Removed OR, p-values, ≤11%, 40%, 0.4%.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R23-M3\"\n  summary: \"Disambiguation neglect 推断边界需收窄\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"§6.2 analysis.tex: added 'externally expressed' before 'disambiguation awareness'.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M4\"\n  summary: \"Table 2 Overall 行应增加 excl-incompleteness 汇总\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Table 2 footnote: 'Excluding incompleteness: pooled Δ=+31.0pp (95% CI [27.9, 34.1])'.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M5\"\n  summary: \"Token count 作为 incompleteness confound control 是粗糙 proxy\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"Confirmed: Limitations §Confounds already states 'Token-count difference...is an imperfect proxy for informational asymmetry; future work could employ semantic complexity metrics'.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M6\"\n  summary: \"§4.3 'five architecturally diverse models' 表述不准确\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Changed to 'five models from four providers spanning two architecture families' in method.tex §4.3.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M7\"\n  summary: \"References arXiv 引用格式不统一\"\n  category: format\n  severity: minor\n  status: resolved\n  resolution: \"Fixed 2 entries (lin_ask_to_clarify_2025, mu_can_llms_2023): @inproceedings→@article, booktitle→journal. All arXiv entries now use consistent @article format.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n# ============================================================\n# R22 ISSUES — ALL RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R22-W1\"\n  summary: \"C4 model×type 交互完全由 authorization scope 驱动，该类型测量不可靠（κ=0.385, ICC≈0），C4 可能是测量伪影\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Removed C4 subsection; compressed to 1 caveat paragraph explicitly framing C4 as possibly reflecting measurement instability.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n\n- id: \"R22-W2\"\n  summary: \"SOPBench 复制效应压缩 63%（34.0pp→12.6pp），缺乏原则性归因\"\n  category: experiment\n  severity: warning\n  status: resolved\n  resolution: \"Added principled framing in §5.1 and structured attribution in Appendix SOPBench section.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-W3\"\n  summary: \"ICC 复制仅覆盖 OpenAI 家族，但残差方差分解应用于所有模型\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Added OpenAI-family qualifier in §5.1 and Limitations §Scope. R23 found qualifier insufficient at some mentions — addressed in R23-W3.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n\n- id: \"R22-W4\"\n  summary: \"SESOI ±15pp 缺乏领域接地论证，为统计驱动而非领域驱动\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Added explicit acknowledgment in §4.6.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n\n- id: \"R22-W5\"\n  summary: \"Token count 作为 incompleteness information-addition confound 代理过于粗糙\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Confound caveat added to §6.3 and Limitations §Confounds.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n\n- id: \"R22-W6\"\n  summary: \"残差方差（60.8%）的干预天花板讨论不够充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Added intervention ceiling paragraph in Discussion §7.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M1\"\n  summary: \"生态效度缺口未量化\"\n  category: framing\n  severity: minor\n  status: resolved\n  resolution: \"Added dose-response study suggestion and SOPBench lower bound in Limitations. R23-W6 found Discussion needs more specific threats — addressed there.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 23\n\n- id: \"R22-M2\"\n  summary: \"层级结构（C3）未通过 Holm-Bonferroni 校正\"\n  category: framing\n  severity: minor\n  status: resolved\n  resolution: \"Already addressed: §5.2 explicitly states organizational convenience.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M3\"\n  summary: \"人工 failure-mode 编码验证缺失\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"Limitations §Measurement states validation underway.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M4\"\n  summary: \"Table 2/Figure 2 中 incompleteness 应标注 confound status\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added dagger marker and footnote in Table 2.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22\n\n- id: \"R22-M5\"\n  summary: \"Conclusion 偏短\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added diagnostic protocol and disambiguation neglect summary.\"\n  resolution_round: 22\n  first_raised_round: 22\n  last_seen_round: 22"
  }
}
```

</details>

---


### Tool result

_source line 2134 · 2026-05-23T08:30:45.503320+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 19205}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2135 · 2026-05-23T08:33:54.830362+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "report": "# Round 24 审稿报告\n\n**论文**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n**Venue**: EMNLP 2026 via ARR (Long Paper)\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）\n**审稿模式**: Fresh（重新审稿）\n**轮次**: Round 1, 1 轮收敛（交叉回应后无未解决矛盾）\n\n---\n\n## Summary\n\n本文在 τ²-bench 上通过 300 组 matched-pair 歧义/无歧义条款对（六类分类、五个模型、2,997 episodes），建立了 policy 歧义与 LLM agent 安全违规之间的因果关系（+34.0 pp，confound-free 范围 +18.7 至 +36.0 pp）。方差分解显示条款措辞解释 22.4% 的违规方差而类型仅 0.4%，但类型预测失败机制的能力远强于预测违规率（NMI = 0.23 vs 0.01）。Error analysis 发现 disambiguation neglect（4.6% awareness）和 systematic nocuity（77% permissive bias）。方法论严谨度在同类工作中突出，但外部效度存疑（SOPBench 效应压缩 63%）、novelty framing 偏强、taxonomy 层效应无统计支撑。\n\n---\n\n## Strengths\n\n**S1. Matched-pair 因果设计严谨 [R1, R2 共识]**\n300 clause pairs × 2 conditions × 5 models 的配对内比较有效隔离歧义操作的因果效应。两名标注者类型分配 κ = 0.95。Perturbation control（Δ = −0.67 pp, CI 含零）和 ICC = 0.919 复制验证完整。在该领域因果推断链条完整度罕见。\n\n**S2. 统计框架全面且自律 [R1, R2 共识]**\nMcNemar's test、TOST 等价检验（跨 7 个 margin 的敏感性分析）、Type III SS 方差分解、Holm-Bonferroni 校正、Bootstrap clustering（B=10,000）。C3 未通过校正后被诚实标注为 inconclusive。统计自律值得肯定。\n\n**S3. Error Analysis 揭示有价值的新现象 [R1, R2 共识]**\nDisambiguation neglect（4.6%）、systematic nocuity（41.3% 多数模型收敛于同一错误、77% permissive bias）是有实质贡献的发现。Nocuity 方向反转（Berry & Kamsties 2004 的 divergent → 本文的 convergent）提供了 LLM-specific 的失败模式理解。\n\n**S4. 复现与泛化验证充分 [R1, R2 共识]**\n7 个模型（5 main + 2 replication）覆盖 6 providers、2 架构家族。三族交叉评判验证（Fleiss' κ = 0.717）。SOPBench 跨基准复制。方法论局限的坦诚披露（incompleteness confound、auth scope 低 κ、ICC 范围限制）在同类工作中少见。\n\n**S5. Related Work 覆盖好 [R2]**\n引用了所有主要并发工作（DRIP-R, PolicyBank, AgentPex, MANTRA），对心理语言学和 RE 文献的桥接恰当。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical, R2 提出 R1 AGREE] Novelty framing 不够诚实**\nContribution (1) \"the first matched-pair causal study\" 本质上是将心理语言学/RE 的标准方法迁移到 LLM agent policy 领域，非方法论创新。核心发现\"ambiguity → more errors\"方向上可预测，真正有价值的是效应量化和 type→mechanism 的诊断发现（NMI = 0.23 vs 0.01）。§3 已有 \"experimental instrument rather than a proposed classification standard\" 的自我限定，但 §1 contributions 和 Abstract 未贯穿此定位。\n→ **建议**: 从 \"first causal study\" 转向 \"first quantification of differential effect + diagnostic taxonomy\" 作为核心卖点。\n\n**N2 [critical, R2 提出 R1 AGREE] Taxonomy 两层结构（C3）无统计支撑但叙事未调整**\n六类 taxonomy 是 Li et al. (2024) 11 类的子集选取，非原创分类体系。C3 层效应未通过 Holm-Bonferroni 校正（p=0.017 vs 阈值 0.0125），但 §3 和 §1 的叙事仍围绕 \"two layers—linguistic and specification\" 展开。§3 的理论预测（linguistic ambiguity 可部分通过 tool responses 解消）恰恰未得到验证。\n→ **建议**: 将两层结构降格为描述性组织框架，§3 和 §1 同步更新叙事。\n\n**N3 [critical, R1 提出 R2 AGREE 但认为接近 Should-Fix] 外部效度——合成→自然效应压缩 63%**\nτ²-bench 主实验 +34.0 pp vs SOPBench +12.6 pp，且 SOPBench 上 2/5 模型不显著（GPT-5.4 p=0.052, DeepSeek p=0.163）。三因素归因（measurement grain、baseline compression、interaction depth）是 post-hoc 推测，各自贡献量无法分离。§5.1 \"directional consistency across all models is the primary criterion\" 将标准从效应量一致性降格为方向一致性，是 goalpost shifting。Limitations 已声明 \"34.0 pp is an upper bound\"，但 Abstract/Conclusion 仍以 34.0 pp 为主要数字。\n→ **建议**: Discussion 增加生态效度正式段落；Abstract/Conclusion 呈现效应量范围（12.6-34.0 pp）。\n\n**N4 [critical, R1 提出 R2 AGREE] Incompleteness 信息添加混淆控制不足**\nIncompleteness 的实验操纵本质上不同于其他五类（信息删除/添加 vs 语义重写）。Token count 作为 proxy 控制混淆，logistic regression 正系数 β=+0.027 存在替代解释（over-constraint violation）。虽然 0.1 pp 的实际影响微小，但 framing 问题严重——Abstract 中 34.0 pp 包含 incompleteness 而 confound-free range（+18.7 至 +36.0 pp）排除了它，这个区别被压缩在一句话中。\n→ **建议**: Abstract/Conclusion 优先报告 confound-free pooled Δ = +31.0 pp（95% CI [27.9, 34.1]），34.0 pp 标注为含 incompleteness 上界。\n\n### Should-Fix（影响评分但非一票否决）\n\n**W1 [warning, R2 提出 R1 强烈 AGREE] Authorization scope 构念效度系统性存疑**\n多维度 outlier：最低 inter-judge κ = 0.385、cross-judge-group ρ = 0.09、驱动全部 C4（排除后 p=0.97）、最低 within-type ICC = 0.29、最大跨模型方差 52 pp。已有排除 auth scope 后 C4 消失和 cross-judge ρ = 0.90 的分析，但缺少排除后的 C1 pooled Δ、方差分解、NMI——仅需对现有数据重新计算。\n→ **建议**: 补充排除 auth scope 后的 C1、方差分解、NMI 敏感性分析。\n\n**W2 [warning, R1 提出 R2 REBUT 降级] 条款对构建过程不够透明**\nTemplate-based pipeline 未描述模板数量、结构、筛选率。Post-hoc realism validation 一句带过。R2 认为应降为 Should-Fix（数据承诺发布、§4.2 已有关键信息、高 κ 是设计目标）。两位 Reviewer 共识：需补充但非 blocking。\n→ **建议**: Appendix 补充模板设计细节和筛选率；扩展 clause pair 示例至每类型 2-3 个。\n\n**W3 [warning, R1 提出 R2 AGREE] 失败模式编码缺乏人工验证**\n614 条 trace 的 LLM 编码（Gwet's AC₁ = 0.62, κ = 0.52），循环性风险。LLM coder prompt 是否包含类型信息未说明。Limitations 中 \"human validation underway for camera-ready\" 不足以支撑当前 claim 强度。\n→ **建议**: 明确 coder prompt 设计；至少 50-100 条 trace 的人工验证。\n\n**W4 [warning, R1 提出 R2 AGREE] SESOI ±15 pp 的 justification 不够 principled**\n\">2× 噪声\"和\"不需不同缓解策略\"两条理由非领域接地。Table 3 sensitivity analysis 已部分缓解，但 ±15 pp 的选择仍影响 §5.2 叙事结构。\n→ **建议**: 明确标注 pragmatic default；正文更突出引用 Table 3 的 ±10/±12 pp 结果。\n\n**W5 [warning, R1 提出 R2 AGREE] ICC 复制仅限 OpenAI 家族**\n同家族模型可能共享训练数据导致 clause-level response pattern 相似，膨胀 ICC。C1 方向一致性不等同于 clause-level reproducibility。\n→ **建议**: 讨论跨提供商 ICC 可能更低的含义。\n\n**W6 [warning, R1 提出 R2 AGREE] Human validation per-type 样本量不足**\nPer-type n ≈ 32-34，CI 极宽（coreferential: [0.00, 0.84]）。论文自身承认 imprecise 但仍引用 per-type κ 作论证。\n→ **建议**: 引用 per-type κ 时附 CI；理想情况增加至 per-type ≥ 50。\n\n**W7 [warning, R1 提出 R2 强烈 AGREE] Cross-domain type ranking ρ = 0.26 削弱 C2 泛化性**\nRetail 和 airline 两个 customer-service 子域的类型排序几乎无关（p=0.62）。Cond. prec. 跨域差异 22.0 pp。Conclusion 中 \"type-targeted diagnosis for policy-governed deployments\" 的建议缺乏跨域根基。\n→ **建议**: §7 讨论领域依赖性；Conclusion 限定适用范围。\n\n**W8 [warning, R2 提出 R1 AGREE] NMI 比较的 cardinality 不对称**\nType→mechanism (6×5) vs type→violation (6×2)。Binary outcome 下 NMI 的 effective range 更受限，\"order of magnitude\"（16.8×）部分是 cardinality artifact。Cramér's V 比较（0.45 vs 0.137 = 3.3×）更公平但比值远小。\n→ **建议**: 承认 NMI 受 cardinality 影响；以 Cramér's V 补充或替代 \"order of magnitude\" 表述。\n\n**W9 [warning, R2 提出 R1 PARTIALLY AGREE] 方差分解叙事偏重已解释部分**\n60.8% 残差被包装为 intervention ceiling 而非研究解释力限制。Appendix Z 的 ICC 分解已有进一步分析，但正文未充分反映。\n→ **建议**: §5.1 或 §7 补充一句承认解释力限制。\n\n### Minor（不影响接收）\n\n**M1 [R1, R2]** Abstract 信息密度过高（8 个数字），建议精简至 3-4 个。\n**M2 [R1, R2]** \"Nocuous\" 术语反转未在首次使用（Abstract）时标注。\n**M3 [R1, R2]** Temperature=0 对泛化性的影响未在 Limitations 提及。\n**M4 [R1, R2]** C3/C4 编号暗示四个同等级 claim，应明确标注层级。\n**M5 [R1]** Table 2 脚注 ‡ 应标注 per-type 样本量（n≈17）。\n**M6 [R1→R2 降级]** Prevalence audit（Appendix）κ = 0.295，Introduction 引用时标注低可靠性。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下核心问题上达成完全共识：\n\n1. **外部效度是最大风险**：SOPBench 63% 效应压缩 + 2/5 模型不显著，合成条件下的 34.0 pp 不可直接推广\n2. **Incompleteness confound 的 framing 不够突出**：confound-free range 应作为 headline\n3. **Authorization scope 构念效度系统性存疑**：多维度 outlier，需补充排除后的敏感性分析\n4. **C3 层效应失败但叙事未同步调整**：两层结构应降格为组织性框架\n5. **失败模式编码缺人工验证**：camera-ready 承诺不够\n6. **Novelty framing 偏强**：应从 \"first causal study\" 转向 type-specific diagnostic\n7. **NMI cardinality asymmetry**：Cramér's V 比较更公平（3.3× vs 16.8×）\n8. **Cross-domain type ranking 不支持跨域泛化**：ρ = 0.26\n\n---\n\n## Reviewer Divergence\n\n两位 Reviewer 仅在严重程度上有分歧，无实质性矛盾：\n\n| Issue | R1 | R2 | 共识 |\n|-------|-----|-----|------|\n| 条款对构建透明度（N3/W2） | Must-Fix | Should-Fix | **Should-Fix**（R2 理由充分：数据将发布、§4.2 已有关键信息） |\n| Prevalence audit 可靠性（W6/M6） | Should-Fix | Minor | **Minor**（不影响核心分析） |\n| Figure 1 信息量（M4） | 合理 | 可优化 | **不列入**（审美判断，非方法论问题） |\n| 3 episodes API error（M3） | Minor | 无需关注 | **不列入**（0.1% 不构成 systematic missingness） |\n\n---\n\n## Questions（需作者澄清）\n\n**Q1 [R1, R2 共识]** SOPBench 效应缩小到 1/3 对论文实际启示（practical implications）的影响？如果真实世界效应接近 12.6 pp 而非 34.0 pp，\"nocuous\" framing 和 \"clause-level auditing\" 建议的力度如何调整？\n\n**Q2 [R2 提出 R1 AGREE]** 排除 authorization scope 后，C1 pooled Δ、方差分解、NMI 的具体数字？（现有数据即可计算）\n\n**Q3 [R1, R2 共识]** LLM failure mode coder 的 prompt 是否包含歧义类型标签？如果包含，NMI = 0.23 可能被 prompt 污染。如果不包含，请说明 prompt 设计。\n\n**Q4 [R1]** 22.4% clause-level variance 的分布形态——少数高效应条款驱动的右偏分布 vs 连续分布？LOO 最大 shift 1.4 pp 暗示无单一极端值，但 within-type CV 0.69-1.03 暗示高异质性。\n\n**Q5 [R2]** 77% permissive bias 是否是 customer-service domain artifact（agent 被训练为\"帮助客户\"）？跨域 permissive 比例分别是多少？\n\n**Q6 [R2]** Disambiguation neglect 的模型差异（GPT-4.1/Claude 10-11% vs Qwen3/DeepSeek 0%）反映 safety training 差异还是歧义处理能力差异？§6.2 \"default behavior, not inability\" 的 claim 能否被当前数据区分？\n\n**Q7 [R1]** Concordant-violation 和 concordant-no-violation 的比例分别是多少？（580/1497 discordant pairs 意味着 917 concordant pairs）\n\n---\n\n## Missing References\n\n**两位 Reviewer 共同推荐：**\n- Kadavath et al. 2022, \"Language Models (Mostly) Know What They Know\" — 与 disambiguation neglect 直接相关\n\n**R2 推荐（R1 未独立验证）：**\n- AgentSpec (Wang et al., ICSE 2026) — agent runtime specification enforcement\n- Agent Behavioral Contracts (arXiv 2602.22302, 2026) — formal specification + runtime enforcement\n- \"Check Yourself Before You Wreck Yourself\" (arXiv 2510.16492, 2025) — selective quitting for agent safety\n\n**R1 推荐（R2 部分 REBUT）：**\n- Kadavath et al. 2022 [R2 AGREE]\n- Lu et al. 2022, prompt order sensitivity [R2 REBUT: matched-pair 已控制位置]\n- Constitutional AI / RLHF literature [R2 REBUT: 过于宽泛]\n\n---\n\n## External Review\n\n**状态**: 未请求（项目配置未启用外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（3 warnings, 0 critical, 9 info）\n\n**Warnings:**\n1. **Pages 4-6 视觉疲劳**: 连续三页纯文本（§4 Method → §5.2 Results），无 figure/table/equation 穿插。建议在 page 5-6 插入结果摘要表或 forest plot 打破文本墙。\n2. **Page 8 Figure 3 尺寸偏小**: Model×Type 热力图挤在右栏约 1/4 栏高，单元格数值和轴标签在正常阅读距离下难以辨认。建议改用 figure*（全宽）或增大纵向空间。\n3. **Figure 2/3 Float 位置偏离引用**: 两个 figure 出现在 page 8（Discussion/Conclusion 区域），但首次引用在 page 5-6 的 Results。审稿人需回翻 2-3 页。\n\n**Info:**\n- 主体正文 5 个 display items（对 8 页实证论文偏低，建议 6-8 个）\n- Figure 1 位置合理（page 2 顶部）、Table 2 排版干净、Appendix 表格丰富\n- 正文精确卡在 8 页限制内，Limitations 在 page 9\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 4/5 | **3.75** — matched-pair 设计和统计框架严谨，但 incompleteness confound 控制不足、auth scope 构念效度存疑、failure mode 编码缺人工验证 |\n| Excitement | 3.5/5 | 3/5 | **3.25** — 核心发现方向可预测；type-specific diagnostic 和 systematic nocuity 有价值但 taxonomy 非原创；\"first causal study\" framing overstates novelty |\n| Reproducibility | 3/5 | 4/5 | **3.5** — 数据/代码承诺发布，但 template pipeline 描述不足、ICC 仅 OpenAI family |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**一句话总结**: 方法论严谨的因果实验（matched-pair + 全面统计框架 + 7 模型），核心方法论框架是扎实的。但四个问题限制了评分：(1) novelty framing 偏强（\"first causal study\" 是领域迁移而非创新），(2) 外部效度存疑（SOPBench 效应压缩 63%），(3) taxonomy 层效应无统计支撑但叙事未调整，(4) incompleteness confound 和 auth scope 构念效度的联合影响。\n\n**升分路径**: 如果作者 (a) 按 N1/N2 调整 framing（弱化 \"first causal\"、降格两层结构），(b) 按 N3 在 Discussion 正式讨论生态效度并调整 headline 数字，(c) 按 N4 调整 incompleteness framing——论文可升至 **4.0 Conference**。当前状态适合 **strong Findings**。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高（8 个数字），建议精简至 34.0 pp（或 confound-free 31.0 pp）、22.4% clause variance、NMI ratio\n- \"Nocuous\" 首次出现时加 \"(i.e., harmful)\" 已有，但 nocuity inversion（convergent vs divergent）未标注\n- Confound-free range 在句末容易被忽略，建议调整为 headline\n\n### §1 Introduction\n- Contribution (1) 的 \"first\" claim 需 reframe\n- Prevalence audit 引用（55-87%）应标注低可靠性（κ = 0.295）\n- Figure 1 位置合理但信息密度可优化\n\n### §3 Taxonomy\n- 两层结构的叙事需降格为组织性框架\n- \"We test this empirically\" 的预测未通过 → 应在 §5.2 的 C3 结果后增加 cross-reference\n\n### §4 Method\n- §4.2 template pipeline 需补充细节（模板数量、筛选率）\n- §4.3 temperature=0 的局限性应在 Limitations 补充\n- §4.4 human validation per-type 引用时附 CI\n- §4.6 SESOI ±15 pp 明确标注 pragmatic default\n\n### §5 Results\n- §5.1 C1: 34.0 pp 应标注为含 incompleteness 的上界；confound-free pooled Δ = 31.0 pp 应更突出\n- §5.1 variance decomposition: 补充 60.8% 残差作为解释力限制的一句话\n- §5.2 C2: cross-domain ρ = 0.26 的讨论应更显著\n- §5.2 NMI: \"order of magnitude\" 需补充 Cramér's V 作为 cardinality-robust 替代\n- C3/C4 的 claim 层级应在 §5 开头更明确标注\n\n### §6 Analysis\n- §6 failure mode: claim 强度应降低至与 κ = 0.52 匹配\n- §6.2 disambiguation neglect: safety training vs ambiguity processing 的混淆应讨论\n- §6.3 systematic nocuity: permissive bias 可能是 domain artifact，应在 Discussion 讨论\n\n### §7 Discussion\n- 增加生态效度正式段落（34.0 pp → 12.6 pp SOPBench）\n- C2 领域依赖性的讨论\n- 77% permissive bias 的跨域稳定性讨论\n\n### Limitations\n- 补充 temperature=0 的局限性\n- 加强 ICC 范围限制的讨论\n\n### Appendix\n- 扩展 clause pair examples（每类型 2-3 个）\n- Table 2 脚注标注 per-type 样本量\n\n### 格式\n- ✅ 正文 8 页，Limitations page 9（不计入页限）\n- ✅ Double-blind 匿名格式正确\n- ✅ ACL 模板使用正确\n- ✅ References natbib 风格\n- ⚠️ Data availability 中匿名 GitHub URL 需确保提交时未泄露身份"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "report": "# Round 24 审稿报告\n\n**论文**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n**Venue**: EMNLP 2026 via ARR (Long Paper)\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）\n**审稿模式**: Fresh（重新审稿）\n**轮次**: Round 1, 1 轮收敛（交叉回应后无未解决矛盾）\n\n---\n\n## Summary\n\n本文在 τ²-bench 上通过 300 组 matched-pair 歧义/无歧义条款对（六类分类、五个模型、2,997 episodes），建立了 policy 歧义与 LLM agent 安全违规之间的因果关系（+34.0 pp，confound-free 范围 +18.7 至 +36.0 pp）。方差分解显示条款措辞解释 22.4% 的违规方差而类型仅 0.4%，但类型预测失败机制的能力远强于预测违规率（NMI = 0.23 vs 0.01）。Error analysis 发现 disambiguation neglect（4.6% awareness）和 systematic nocuity（77% permissive bias）。方法论严谨度在同类工作中突出，但外部效度存疑（SOPBench 效应压缩 63%）、novelty framing 偏强、taxonomy 层效应无统计支撑。\n\n---\n\n## Strengths\n\n**S1. Matched-pair 因果设计严谨 [R1, R2 共识]**\n300 clause pairs × 2 conditions × 5 models 的配对内比较有效隔离歧义操作的因果效应。两名标注者类型分配 κ = 0.95。Perturbation control（Δ = −0.67 pp, CI 含零）和 ICC = 0.919 复制验证完整。在该领域因果推断链条完整度罕见。\n\n**S2. 统计框架全面且自律 [R1, R2 共识]**\nMcNemar's test、TOST 等价检验（跨 7 个 margin 的敏感性分析）、Type III SS 方差分解、Holm-Bonferroni 校正、Bootstrap clustering（B=10,000）。C3 未通过校正后被诚实标注为 inconclusive。统计自律值得肯定。\n\n**S3. Error Analysis 揭示有价值的新现象 [R1, R2 共识]**\nDisambiguation neglect（4.6%）、systematic nocuity（41.3% 多数模型收敛于同一错误、77% permissive bias）是有实质贡献的发现。Nocuity 方向反转（Berry & Kamsties 2004 的 divergent → 本文的 convergent）提供了 LLM-specific 的失败模式理解。\n\n**S4. 复现与泛化验证充分 [R1, R2 共识]**\n7 个模型（5 main + 2 replication）覆盖 6 providers、2 架构家族。三族交叉评判验证（Fleiss' κ = 0.717）。SOPBench 跨基准复制。方法论局限的坦诚披露（incompleteness confound、auth scope 低 κ、ICC 范围限制）在同类工作中少见。\n\n**S5. Related Work 覆盖好 [R2]**\n引用了所有主要并发工作（DRIP-R, PolicyBank, AgentPex, MANTRA），对心理语言学和 RE 文献的桥接恰当。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical, R2 提出 R1 AGREE] Novelty framing 不够诚实**\nContribution (1) \"the first matched-pair causal study\" 本质上是将心理语言学/RE 的标准方法迁移到 LLM agent policy 领域，非方法论创新。核心发现\"ambiguity → more errors\"方向上可预测，真正有价值的是效应量化和 type→mechanism 的诊断发现（NMI = 0.23 vs 0.01）。§3 已有 \"experimental instrument rather than a proposed classification standard\" 的自我限定，但 §1 contributions 和 Abstract 未贯穿此定位。\n→ **建议**: 从 \"first causal study\" 转向 \"first quantification of differential effect + diagnostic taxonomy\" 作为核心卖点。\n\n**N2 [critical, R2 提出 R1 AGREE] Taxonomy 两层结构（C3）无统计支撑但叙事未调整**\n六类 taxonomy 是 Li et al. (2024) 11 类的子集选取，非原创分类体系。C3 层效应未通过 Holm-Bonferroni 校正（p=0.017 vs 阈值 0.0125），但 §3 和 §1 的叙事仍围绕 \"two layers—linguistic and specification\" 展开。§3 的理论预测（linguistic ambiguity 可部分通过 tool responses 解消）恰恰未得到验证。\n→ **建议**: 将两层结构降格为描述性组织框架，§3 和 §1 同步更新叙事。\n\n**N3 [critical, R1 提出 R2 AGREE 但认为接近 Should-Fix] 外部效度——合成→自然效应压缩 63%**\nτ²-bench 主实验 +34.0 pp vs SOPBench +12.6 pp，且 SOPBench 上 2/5 模型不显著（GPT-5.4 p=0.052, DeepSeek p=0.163）。三因素归因（measurement grain、baseline compression、interaction depth）是 post-hoc 推测，各自贡献量无法分离。§5.1 \"directional consistency across all models is the primary criterion\" 将标准从效应量一致性降格为方向一致性，是 goalpost shifting。Limitations 已声明 \"34.0 pp is an upper bound\"，但 Abstract/Conclusion 仍以 34.0 pp 为主要数字。\n→ **建议**: Discussion 增加生态效度正式段落；Abstract/Conclusion 呈现效应量范围（12.6-34.0 pp）。\n\n**N4 [critical, R1 提出 R2 AGREE] Incompleteness 信息添加混淆控制不足**\nIncompleteness 的实验操纵本质上不同于其他五类（信息删除/添加 vs 语义重写）。Token count 作为 proxy 控制混淆，logistic regression 正系数 β=+0.027 存在替代解释（over-constraint violation）。虽然 0.1 pp 的实际影响微小，但 framing 问题严重——Abstract 中 34.0 pp 包含 incompleteness 而 confound-free range（+18.7 至 +36.0 pp）排除了它，这个区别被压缩在一句话中。\n→ **建议**: Abstract/Conclusion 优先报告 confound-free pooled Δ = +31.0 pp（95% CI [27.9, 34.1]），34.0 pp 标注为含 incompleteness 上界。\n\n### Should-Fix（影响评分但非一票否决）\n\n**W1 [warning, R2 提出 R1 强烈 AGREE] Authorization scope 构念效度系统性存疑**\n多维度 outlier：最低 inter-judge κ = 0.385、cross-judge-group ρ = 0.09、驱动全部 C4（排除后 p=0.97）、最低 within-type ICC = 0.29、最大跨模型方差 52 pp。已有排除 auth scope 后 C4 消失和 cross-judge ρ = 0.90 的分析，但缺少排除后的 C1 pooled Δ、方差分解、NMI——仅需对现有数据重新计算。\n→ **建议**: 补充排除 auth scope 后的 C1、方差分解、NMI 敏感性分析。\n\n**W2 [warning, R1 提出 R2 REBUT 降级] 条款对构建过程不够透明**\nTemplate-based pipeline 未描述模板数量、结构、筛选率。Post-hoc realism validation 一句带过。R2 认为应降为 Should-Fix（数据承诺发布、§4.2 已有关键信息、高 κ 是设计目标）。两位 Reviewer 共识：需补充但非 blocking。\n→ **建议**: Appendix 补充模板设计细节和筛选率；扩展 clause pair 示例至每类型 2-3 个。\n\n**W3 [warning, R1 提出 R2 AGREE] 失败模式编码缺乏人工验证**\n614 条 trace 的 LLM 编码（Gwet's AC₁ = 0.62, κ = 0.52），循环性风险。LLM coder prompt 是否包含类型信息未说明。Limitations 中 \"human validation underway for camera-ready\" 不足以支撑当前 claim 强度。\n→ **建议**: 明确 coder prompt 设计；至少 50-100 条 trace 的人工验证。\n\n**W4 [warning, R1 提出 R2 AGREE] SESOI ±15 pp 的 justification 不够 principled**\n\">2× 噪声\"和\"不需不同缓解策略\"两条理由非领域接地。Table 3 sensitivity analysis 已部分缓解，但 ±15 pp 的选择仍影响 §5.2 叙事结构。\n→ **建议**: 明确标注 pragmatic default；正文更突出引用 Table 3 的 ±10/±12 pp 结果。\n\n**W5 [warning, R1 提出 R2 AGREE] ICC 复制仅限 OpenAI 家族**\n同家族模型可能共享训练数据导致 clause-level response pattern 相似，膨胀 ICC。C1 方向一致性不等同于 clause-level reproducibility。\n→ **建议**: 讨论跨提供商 ICC 可能更低的含义。\n\n**W6 [warning, R1 提出 R2 AGREE] Human validation per-type 样本量不足**\nPer-type n ≈ 32-34，CI 极宽（coreferential: [0.00, 0.84]）。论文自身承认 imprecise 但仍引用 per-type κ 作论证。\n→ **建议**: 引用 per-type κ 时附 CI；理想情况增加至 per-type ≥ 50。\n\n**W7 [warning, R1 提出 R2 强烈 AGREE] Cross-domain type ranking ρ = 0.26 削弱 C2 泛化性**\nRetail 和 airline 两个 customer-service 子域的类型排序几乎无关（p=0.62）。Cond. prec. 跨域差异 22.0 pp。Conclusion 中 \"type-targeted diagnosis for policy-governed deployments\" 的建议缺乏跨域根基。\n→ **建议**: §7 讨论领域依赖性；Conclusion 限定适用范围。\n\n**W8 [warning, R2 提出 R1 AGREE] NMI 比较的 cardinality 不对称**\nType→mechanism (6×5) vs type→violation (6×2)。Binary outcome 下 NMI 的 effective range 更受限，\"order of magnitude\"（16.8×）部分是 cardinality artifact。Cramér's V 比较（0.45 vs 0.137 = 3.3×）更公平但比值远小。\n→ **建议**: 承认 NMI 受 cardinality 影响；以 Cramér's V 补充或替代 \"order of magnitude\" 表述。\n\n**W9 [warning, R2 提出 R1 PARTIALLY AGREE] 方差分解叙事偏重已解释部分**\n60.8% 残差被包装为 intervention ceiling 而非研究解释力限制。Appendix Z 的 ICC 分解已有进一步分析，但正文未充分反映。\n→ **建议**: §5.1 或 §7 补充一句承认解释力限制。\n\n### Minor（不影响接收）\n\n**M1 [R1, R2]** Abstract 信息密度过高（8 个数字），建议精简至 3-4 个。\n**M2 [R1, R2]** \"Nocuous\" 术语反转未在首次使用（Abstract）时标注。\n**M3 [R1, R2]** Temperature=0 对泛化性的影响未在 Limitations 提及。\n**M4 [R1, R2]** C3/C4 编号暗示四个同等级 claim，应明确标注层级。\n**M5 [R1]** Table 2 脚注 ‡ 应标注 per-type 样本量（n≈17）。\n**M6 [R1→R2 降级]** Prevalence audit（Appendix）κ = 0.295，Introduction 引用时标注低可靠性。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下核心问题上达成完全共识：\n\n1. **外部效度是最大风险**：SOPBench 63% 效应压缩 + 2/5 模型不显著，合成条件下的 34.0 pp 不可直接推广\n2. **Incompleteness confound 的 framing 不够突出**：confound-free range 应作为 headline\n3. **Authorization scope 构念效度系统性存疑**：多维度 outlier，需补充排除后的敏感性分析\n4. **C3 层效应失败但叙事未同步调整**：两层结构应降格为组织性框架\n5. **失败模式编码缺人工验证**：camera-ready 承诺不够\n6. **Novelty framing 偏强**：应从 \"first causal study\" 转向 type-specific diagnostic\n7. **NMI cardinality asymmetry**：Cramér's V 比较更公平（3.3× vs 16.8×）\n8. **Cross-domain type ranking 不支持跨域泛化**：ρ = 0.26\n\n---\n\n## Reviewer Divergence\n\n两位 Reviewer 仅在严重程度上有分歧，无实质性矛盾：\n\n| Issue | R1 | R2 | 共识 |\n|-------|-----|-----|------|\n| 条款对构建透明度（N3/W2） | Must-Fix | Should-Fix | **Should-Fix**（R2 理由充分：数据将发布、§4.2 已有关键信息） |\n| Prevalence audit 可靠性（W6/M6） | Should-Fix | Minor | **Minor**（不影响核心分析） |\n| Figure 1 信息量（M4） | 合理 | 可优化 | **不列入**（审美判断，非方法论问题） |\n| 3 episodes API error（M3） | Minor | 无需关注 | **不列入**（0.1% 不构成 systematic missingness） |\n\n---\n\n## Questions（需作者澄清）\n\n**Q1 [R1, R2 共识]** SOPBench 效应缩小到 1/3 对论文实际启示（practical implications）的影响？如果真实世界效应接近 12.6 pp 而非 34.0 pp，\"nocuous\" framing 和 \"clause-level auditing\" 建议的力度如何调整？\n\n**Q2 [R2 提出 R1 AGREE]** 排除 authorization scope 后，C1 pooled Δ、方差分解、NMI 的具体数字？（现有数据即可计算）\n\n**Q3 [R1, R2 共识]** LLM failure mode coder 的 prompt 是否包含歧义类型标签？如果包含，NMI = 0.23 可能被 prompt 污染。如果不包含，请说明 prompt 设计。\n\n**Q4 [R1]** 22.4% clause-level variance 的分布形态——少数高效应条款驱动的右偏分布 vs 连续分布？LOO 最大 shift 1.4 pp 暗示无单一极端值，但 within-type CV 0.69-1.03 暗示高异质性。\n\n**Q5 [R2]** 77% permissive bias 是否是 customer-service domain artifact（agent 被训练为\"帮助客户\"）？跨域 permissive 比例分别是多少？\n\n**Q6 [R2]** Disambiguation neglect 的模型差异（GPT-4.1/Claude 10-11% vs Qwen3/DeepSeek 0%）反映 safety training 差异还是歧义处理能力差异？§6.2 \"default behavior, not inability\" 的 claim 能否被当前数据区分？\n\n**Q7 [R1]** Concordant-violation 和 concordant-no-violation 的比例分别是多少？（580/1497 discordant pairs 意味着 917 concordant pairs）\n\n---\n\n## Missing References\n\n**两位 Reviewer 共同推荐：**\n- Kadavath et al. 2022, \"Language Models (Mostly) Know What They Know\" — 与 disambiguation neglect 直接相关\n\n**R2 推荐（R1 未独立验证）：**\n- AgentSpec (Wang et al., ICSE 2026) — agent runtime specification enforcement\n- Agent Behavioral Contracts (arXiv 2602.22302, 2026) — formal specification + runtime enforcement\n- \"Check Yourself Before You Wreck Yourself\" (arXiv 2510.16492, 2025) — selective quitting for agent safety\n\n**R1 推荐（R2 部分 REBUT）：**\n- Kadavath et al. 2022 [R2 AGREE]\n- Lu et al. 2022, prompt order sensitivity [R2 REBUT: matched-pair 已控制位置]\n- Constitutional AI / RLHF literature [R2 REBUT: 过于宽泛]\n\n---\n\n## External Review\n\n**状态**: 未请求（项目配置未启用外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（3 warnings, 0 critical, 9 info）\n\n**Warnings:**\n1. **Pages 4-6 视觉疲劳**: 连续三页纯文本（§4 Method → §5.2 Results），无 figure/table/equation 穿插。建议在 page 5-6 插入结果摘要表或 forest plot 打破文本墙。\n2. **Page 8 Figure 3 尺寸偏小**: Model×Type 热力图挤在右栏约 1/4 栏高，单元格数值和轴标签在正常阅读距离下难以辨认。建议改用 figure*（全宽）或增大纵向空间。\n3. **Figure 2/3 Float 位置偏离引用**: 两个 figure 出现在 page 8（Discussion/Conclusion 区域），但首次引用在 page 5-6 的 Results。审稿人需回翻 2-3 页。\n\n**Info:**\n- 主体正文 5 个 display items（对 8 页实证论文偏低，建议 6-8 个）\n- Figure 1 位置合理（page 2 顶部）、Table 2 排版干净、Appendix 表格丰富\n- 正文精确卡在 8 页限制内，Limitations 在 page 9\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 4/5 | **3.75** — matched-pair 设计和统计框架严谨，但 incompleteness confound 控制不足、auth scope 构念效度存疑、failure mode 编码缺人工验证 |\n| Excitement | 3.5/5 | 3/5 | **3.25** — 核心发现方向可预测；type-specific diagnostic 和 systematic nocuity 有价值但 taxonomy 非原创；\"first causal study\" framing overstates novelty |\n| Reproducibility | 3/5 | 4/5 | **3.5** — 数据/代码承诺发布，但 template pipeline 描述不足、ICC 仅 OpenAI family |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**一句话总结**: 方法论严谨的因果实验（matched-pair + 全面统计框架 + 7 模型），核心方法论框架是扎实的。但四个问题限制了评分：(1) novelty framing 偏强（\"first causal study\" 是领域迁移而非创新），(2) 外部效度存疑（SOPBench 效应压缩 63%），(3) taxonomy 层效应无统计支撑但叙事未调整，(4) incompleteness confound 和 auth scope 构念效度的联合影响。\n\n**升分路径**: 如果作者 (a) 按 N1/N2 调整 framing（弱化 \"first causal\"、降格两层结构），(b) 按 N3 在 Discussion 正式讨论生态效度并调整 headline 数字，(c) 按 N4 调整 incompleteness framing——论文可升至 **4.0 Conference**。当前状态适合 **strong Findings**。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高（8 个数字），建议精简至 34.0 pp（或 confound-free 31.0 pp）、22.4% clause variance、NMI ratio\n- \"Nocuous\" 首次出现时加 \"(i.e., harmful)\" 已有，但 nocuity inversion（convergent vs divergent）未标注\n- Confound-free range 在句末容易被忽略，建议调整为 headline\n\n### §1 Introduction\n- Contribution (1) 的 \"first\" claim 需 reframe\n- Prevalence audit 引用（55-87%）应标注低可靠性（κ = 0.295）\n- Figure 1 位置合理但信息密度可优化\n\n### §3 Taxonomy\n- 两层结构的叙事需降格为组织性框架\n- \"We test this empirically\" 的预测未通过 → 应在 §5.2 的 C3 结果后增加 cross-reference\n\n### §4 Method\n- §4.2 template pipeline 需补充细节（模板数量、筛选率）\n- §4.3 temperature=0 的局限性应在 Limitations 补充\n- §4.4 human validation per-type 引用时附 CI\n- §4.6 SESOI ±15 pp 明确标注 pragmatic default\n\n### §5 Results\n- §5.1 C1: 34.0 pp 应标注为含 incompleteness 的上界；confound-free pooled Δ = 31.0 pp 应更突出\n- §5.1 variance decomposition: 补充 60.8% 残差作为解释力限制的一句话\n- §5.2 C2: cross-domain ρ = 0.26 的讨论应更显著\n- §5.2 NMI: \"order of magnitude\" 需补充 Cramér's V 作为 cardinality-robust 替代\n- C3/C4 的 claim 层级应在 §5 开头更明确标注\n\n### §6 Analysis\n- §6 failure mode: claim 强度应降低至与 κ = 0.52 匹配\n- §6.2 disambiguation neglect: safety training vs ambiguity processing 的混淆应讨论\n- §6.3 systematic nocuity: permissive bias 可能是 domain artifact，应在 Discussion 讨论\n\n### §7 Discussion\n- 增加生态效度正式段落（34.0 pp → 12.6 pp SOPBench）\n- C2 领域依赖性的讨论\n- 77% permissive bias 的跨域稳定性讨论\n\n### Limitations\n- 补充 temperature=0 的局限性\n- 加强 ICC 范围限制的讨论\n\n### Appendix\n- 扩展 clause pair examples（每类型 2-3 个）\n- Table 2 脚注标注 per-type 样本量\n\n### 格式\n- ✅ 正文 8 页，Limitations page 9（不计入页限）\n- ✅ Double-blind 匿名格式正确\n- ✅ ACL 模板使用正确\n- ✅ References natbib 风格\n- ⚠️ Data availability 中匿名 GitHub URL 需确保提交时未泄露身份"
  }
}
```

</details>

---


### Tool result

_source line 2136 · 2026-05-23T08:33:59.098757+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4268
}
```

</details>

---


### Assistant

_source line 2137 · 2026-05-23T08:34:11.408836+00:00_

Round 24 审稿完成。

**审稿结果：Overall 3.5 (Borderline Conference / Strong Findings)**

审稿报告已投递至 Research Director。核心发现：

- **4 个 Must-Fix**：novelty framing 偏强、taxonomy C3 无统计支撑、外部效度（SOPBench 效应压缩 63%）、incompleteness confound framing
- **9 个 Should-Fix**：auth scope 构念效度、条款对透明度、失败模式编码缺人工验证、SESOI justification、ICC 范围、human validation 样本量、cross-domain 泛化、NMI cardinality、方差分解叙事
- **6 个 Minor**

两位 Reviewer 评分完全一致（均 3.5），交叉回应后核心问题高度收敛，无未解决矛盾。升分路径明确：调整 framing（N1/N2）+ 讨论生态效度（N3）+ 调整 headline 数字（N4）可升至 4.0 Conference。

Issue Tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 205

## Round 205

2 recorded events


### User

_source line 2138 · 2026-05-23T08:34:13.993564+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部意见的逐条交叉回应并提交给 Director。

核心结论：与 R2 在 5 个关键问题上达成共识（外部效度、incompleteness confound、auth scope 构念效度、C3 层效应、failure mode validation）。R2 的 NMI cardinality asymmetry (W5) 是我遗漏的有价值技术点，已表示同意。唯一实质性分歧在 Figure 1 的信息量（M4）。维持 Overall 3.5 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2139 · 2026-05-23T08:34:31.702755+00:00_

Round 24 审稿完成。

**最终结果：Overall 3.5 (Borderline Conference / Strong Findings)**

审稿报告已投递至 Research Director。两位 Reviewer 评分完全一致（3.5），交叉回应后在所有核心问题上达成共识，无未解决矛盾。

**4 个 Must-Fix（Critical）：**
1. Novelty framing 偏强——应从 "first causal study" 转向 "first quantification + diagnostic taxonomy"
2. Taxonomy 两层结构（C3）无统计支撑但叙事未调整
3. 外部效度——SOPBench 效应压缩 63%（34.0→12.6 pp），Abstract/Conclusion framing 偏乐观
4. Incompleteness confound framing 不够突出——confound-free Δ=31.0 pp 应作为 headline

**9 个 Should-Fix（Warning）：** auth scope 构念效度、条款对构建透明度、failure mode 人工验证、SESOI justification、ICC 范围、human validation 样本量、cross-domain ρ=0.26、NMI cardinality 不对称、方差分解叙事

**升分路径：** 调整 framing（N1/N2）+ 讨论生态效度（N3）+ 调整 headline 数字（N4）→ 可升至 4.0 Conference。

Issue Tracker 已同步更新（R24: 4 critical, 9 warning, 6 minor, 全部 open）。视觉审查已完成（3 warnings: pages 4-6 文本墙、Figure 3 偏小、Figure 2/3 float 偏离引用位置）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 206

## Round 206

56 recorded events


### User

_source line 2140 · 2026-05-23T09:27:48.659324+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2141 · 2026-05-23T09:27:54.177343+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2142 · 2026-05-23T09:27:54.228513+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2143 · 2026-05-23T09:28:02.966538+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2144 · 2026-05-23T09:28:03.017245+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2145 · 2026-05-23T09:28:06.430746+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2146 · 2026-05-23T09:28:06.481414+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2147 · 2026-05-23T09:28:10.245605+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2148 · 2026-05-23T09:28:10.296186+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2149 · 2026-05-23T09:28:26.431300+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2150 · 2026-05-23T09:28:27.385695+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2151 · 2026-05-23T09:28:27.436327+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2152 · 2026-05-23T09:28:28.942105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2153 · 2026-05-23T09:28:28.992795+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\makeatletter
41	\newcommand{\extAlph}[1]{%
42	  \ifcase#1\or A\or B\or C\or D\or E\or F\or G\or H\or I\or J\or K\or L\or M\or N\or O\or P\or Q\or R\or S\or T\or U\or V\or W\or X\or Y\or Z\or AA\or AB\or AC\or AD\or AE\fi}
43	\renewcommand{\thesection}{\extAlph{\value{section}}}
44	\makeatother
45	\input{sections/appendix}
46	
47	\end{document}
48	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2154 · 2026-05-23T09:28:28.993252+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2155 · 2026-05-23T09:28:36.226448+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"The 14th Joint Conference on Lexical and Computational Semantics | ACL Member Portal","url":"https://www.aclweb.org/portal/content/14th-joint-conference-lexical-and-computational-semantics"},{"title":"ACL Policy on Publication Ethics - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics"},{"title":"EACL 2026 - Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-call-system-demonstrations"}]

Based on the search results, here's what I found about ACL Rolling Review (ARR) 2026 submission guidelines and author instructions:

## Key Submission Guidelines

ACL Rolling Review (ARR) invites the submission of long and short papers on substantial, original, and unpublished research in all aspects of Computational Linguistics and Natural Language Processing.

## Paper Format and Templates

Paper submissions must use the official ACL style templates, which are available as an Overleaf template and can also be downloaded directly via https://aclrollingreview.org/cfp under 'Paper Submission Process, Criteria and Templates'. All 
…[truncated 917 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 8790
}
```

</details>

---


### Tool result

_source line 2156 · 2026-05-23T09:28:36.226986+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 7233
}
```

</details>

---


### Tool call

_source line 2157 · 2026-05-23T09:28:43.704893+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit long short paper requirements aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit long short paper requirements aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 2158 · 2026-05-23T09:28:44.711482+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers commitment deadline submission site:2026.emnlp.org OR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers commitment deadline submission site:2026.emnlp.org OR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2159 · 2026-05-23T09:28:46.518803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2160 · 2026-05-23T09:28:46.619580+00:00_

1	\begin{abstract}
2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. We present a matched-pair causal study on $\tau^2$-bench with 300 ambiguous/unambiguous clause pairs spanning a six-type taxonomy, evaluated across five models. Ambiguous clauses are consistently nocuous (harmful; inverting \citeauthor{berry_kamsties_2004}'s divergent interpretation to convergent error), increasing violation rates by 31.0 percentage points in confound-free types (34.0\,pp across all six types, with incompleteness subject to an information-addition confound). Clause wording explains 22.4\% of violation variance; however, type predicts failure \emph{mechanism} substantially more strongly than violation rate, establishing the taxonomy as a diagnostic tool. Error analysis reveals disambiguation neglect and \emph{systematic nocuity}: models converge on identical policy violations with a systematic permissive bias (77\%). These results, observed in customer-service domains under controlled synthetic ambiguity, motivate clause-level policy auditing and type-targeted diagnosis for policy-governed deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2161 · 2026-05-23T09:28:46.670290+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2162 · 2026-05-23T09:28:46.721422+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity---a pilot audit of 407 clauses from 24 production policy documents finds 55--87\% contain at least one ambiguity type (dual-judge $\kappa = 0.30$; range reflects union vs.\ intersection; Appendix~\ref{app:prevalence})---a property studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violati
…[truncated 2448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 2163 · 2026-05-23T09:28:49.783199+00:00_

Web search results for query: "EMNLP 2026 call for papers commitment deadline submission site:2026.emnlp.org OR site:aclweb.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Natural Language Processing | ACL Member Portal","url":"https://www.aclweb.org/portal/category/topics/natural-language-processing"},{"title":"Upcoming ACL-Sponsored Events | ACL Member Portal","url":"https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_submission_deadline_value&sort=asc"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information about EMNLP 2026 submission deadlines:

Papers that have received reviews and a meta-review from ARR (whether fr
…[truncated 830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5071
}
```

</details>

---


### Tool result

_source line 2164 · 2026-05-23T09:28:57.815212+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit long short paper requirements aclrollingreview.org"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on the search results, here is the information about ACL Rolling Review 2026 submission format requirements:

## Page Limits

Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices. Short papers may consist of up to 4 pages of content, plus unlimited references and appendices.

Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Formatting and Submission Requirements

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities must be avoided.

Appendices should come after the references in the submitted pdf, but do not count towards
…[truncated 699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 14110
}
```

</details>

---


### Tool call

_source line 2165 · 2026-05-23T09:29:05.597450+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2166 · 2026-05-23T09:29:05.898965+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_l
…[truncated 4154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2167 · 2026-05-23T09:29:05.899391+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 2168 · 2026-05-23T09:29:06.050304+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers (Table~\ref{tab:taxonomy}), selected from \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types) based on three design criteria: (1)~theoretical attestation in prior RE literature \citep{massey_ambiguity_re_2014,berry_kamsties_2004,drip_r_2026}, (2)~amenability to minimal-pair construction without altering clause semantics beyond the target ambiguity, and (3)~mutual exclusivity for unambiguous IV assignment. Types such as ellipsis and pragmatic implicature were excluded because they resist minimal-pair construction within the single-clause policy format.
7	
8	\begin{table}[t]
9	\centering
10	\footnotesize
11	\caption{Six-type ambiguity taxonomy. Disambiguation channel indicates the primary mechanism required to resolve the ambiguity.}
12	\label{tab:taxonomy}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}llll@{}}
15	\toprule
16	\textbf{Type} & \textbf{Layer} & \textbf{Definition} & \textbf{Disambig.\ Channel} \\
17	\midrule
18	Lexical & Ling. & Word/phrase admits multiple senses & Context \\
19	Scopal & Ling. & Quantifier/operator scope underdetermined & Bracketing \\
20	Coreferential & Ling. & Pronoun/NP referent is ambiguous & Resolution \\
21	Auth.\ Scope & Spec. & Permission boundary is vague & Boundary def. \\
22	Incompleteness & Spec. & Required information is absent & Content addition \\
23	Cond.\ Prec. & Spec. & Rules conflict under certain conditions & Priority rule \\
24	\bottomrule
25	\end{tabular}}%
26	\end{table}
27	
28	\paragraph{Linguistic layer.} These types operate at the syntactic or 
…[truncated 2784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2169 · 2026-05-23T09:29:06.402078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2170 · 2026-05-23T09:29:06.905563+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300; Cohen's $\kappa = 0.95$ on six-type classification); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We
…[truncated 4361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2171 · 2026-05-23T09:29:06.905898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2172 · 2026-05-23T09:29:07.307834+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around three analyses: the binary ambiguity effect (C1), the type partial ordering (C2, including the inconclusive layer effect C3), and the model$\times$type interaction (C4). C1 and C2 are primary supported claims; C3 (layer effect) is inconclusive; C4 (model$\times$type interaction) is exploratory.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity (\S\ref{sec:method}). A Type III sum-of-squares decomposition\footnote{Type III SS avoids ordering dependence in our unbalanced design; logistic regression (Appendix~\ref{app:regression}) confirms concordant results (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}).} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (of which $\sim$15\% is stochastic and $\sim$46\% systematic, estimated from an OpenAI-family ICC replication; Appendix~\ref{app:residual}). A permutation test confirms that clause wording---not type membership---drives this variance ($p < 0.001$; Appendix~\ref{app:clause_variance}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; controlling for token count changes no type's predicted effect by more than 0.1\,pp (Appendix~\ref{app:confound}). The confound-free range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope); excluding incompleteness entirely, the pooled effect is $+$31.0\,pp (95\% CI $[27.9, 34.1]$).
9	
10	Replication on two additional models confirms the effect across seven models ($\Delta = +2
…[truncated 5986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2173 · 2026-05-23T09:29:12.477676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 2174 · 2026-05-23T09:29:12.879560+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes (Gwet's AC$_1$ $= 0.62$, $\kappa = 0.52$ \citep{gwet_2014,cohen_1960}). The failure mode coder prompt receives the agent trajectory, policy clause, ground truth, and violation assessment, but does \emph{not} include the ambiguity type label; type is assigned programmatically post hoc. Using LLMs to code LLM failures introduces circularity risk; however, mutual information between type (exogenous) and mechanism labels ($I(\text{type}; \text{mechanism}) = 0.41$ bits, $V = 0.45$; Appendix~\ref{app:type_mechanism}) provides structural evidence against this. This association is computed from LLM-coded labels; human mechanism coding yields lower agreement ($\kappa = 0.15$; Appendix~\ref{app:human_validation}), so absolute NMI should be interpreted as an upper bound on the true type--mechanism association. The following failure mode patterns should therefore be interpreted as consistent LLM categorization tendencies rather than ground-truth mechanism assignments. Two of the six type--mechanism mappings reflect partial definitional affinity (authorization scope$\to$boundary violation, incompleteness$\to$gap-filling); the remaining four (e.g., scopal$\to$structural misparse, 82.7\% cross-model consistency) are empirically derived.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse}: the agent commits to an incorrect parse, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}. Dominates scopal (5/5), conditional precedence (4/5), and coreferential (3/5).
13	
14	\e
…[truncated 2537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2175 · 2026-05-23T09:29:12.879919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2176 · 2026-05-23T09:29:13.934122+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity and intervention limits.}
5	Our results support a \emph{differential nocuity} hypothesis \citep{berry_kamsties_2004,willis_nocuous_2008}: the binary effect is domain-robust ($p = 0.187$) but type-specific profiles require per-domain calibration: cross-domain type ranking is near chance ($\rho = 0.26$, $p = 0.62$), driven by conditional precedence ($\Delta = 22.0$\,pp retail vs.\ airline); deployment in other domains requires independent type-effect calibration. Of the 60.8\% unexplained variance, $\sim$15\% is stochastic and $\sim$46\% systematic (within-provider ICC $= 0.749$; cross-provider consistency supported by C1 replication across seven models; Appendix~\ref{app:residual}). The explained share (39.2\%) is comparable to behavioral research norms; the large systematic residual likely reflects clause$\times$context interactions invisible to type-level analysis, further supporting clause-level over type-level auditing as the actionable intervention. Even perfect disambiguation would address at most 22.4\% of variance; prompt-based mitigation is type-dependent (Appendix~\ref{app:mitigation}), reinforcing policy-design over prompt-level fixes.
6	
7	\paragraph{Taxonomy as diagnostic tool.}
8	Type membership explains only 0.4\% of violation variance versus 22.4\% for clause wording; however, it predicts failure \emph{mechanism} substantially more strongly than violation rate (Cram\'{e}r's $V = 0.45$ vs.\ $0.14$; Appendix~\ref{app:type_mechanism}), validating the taxonomy as a diagnostic tool (\S\ref{sec:analysis}).
9	
10	\paragraph{Ecological validity.}
11	Our synthetic design establishes causal mechanisms but overestimates naturalistic effect sizes. The SOPBench replication ($+$12.6\,pp under constraint-level measurement; Appendix~\ref{app:sopbench}) confirms directional consistency; absolute effect calibration requires grain-matched benchmarks.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 2177 · 2026-05-23T09:29:13.934511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2178 · 2026-05-23T09:29:14.135508+00:00_

1	\section{Conclusion}
2	
3	Under controlled synthetic conditions, policy ambiguity increases agent violations by 31.0\,pp in confound-free types (95\% CI $[27.9, 34.1]$); cross-benchmark evidence confirms directional consistency at reduced magnitude. The taxonomy predicts failure mechanisms substantially more strongly than violation rate (Cram\'{e}r's $V$), enabling type-targeted diagnostics within customer-service domains (\S\ref{sec:analysis}); cross-domain type rankings require per-domain calibration ($\rho = 0.26$). With $>$89\% disambiguation neglect and over 40\% convergent violations, clause-level policy auditing is essential for safe deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 2179 · 2026-05-23T09:29:14.135841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2180 · 2026-05-23T09:29:14.186230+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our ambiguity pairs are synthetically constructed, so the 34.0\,pp effect is an upper bound; the SOPBench replication ($+$12.6\,pp) provides a naturalistic lower bound. We evaluate seven API-accessible models across two customer-service domains at temperature $= 0$; other domains, smaller models, and stochastic sampling remain untested. Failure mode coding relies on LLM annotators ($\kappa = 0.52$; human $\kappa = 0.15$), though the coder prompt excludes ambiguity type labels, preventing type--mechanism contamination.
5	
6	\section*{Data and Code Availability}
7	The 300 clause pairs, evaluation pipeline, analysis scripts, and raw episode traces will be released upon publication at \url{https://github.com/anonymous/policy-ambiguity-safety}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2181 · 2026-05-23T09:29:21.162540+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2182 · 2026-05-23T09:29:21.615652+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 56648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2183 · 2026-05-23T09:29:21.616177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2184 · 2026-05-23T09:29:21.667462+00:00_

1	@inproceedings{li_ambiguity_taxonomy_2024,
2	  title={A Taxonomy of Ambiguity Types for {NLP}},
3	  author={Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.},
4	  booktitle={Proceedings of EACL 2024},
5	  year={2024}
6	}
7	
8	@inproceedings{massey_ambiguity_re_2014,
9	  title={Identifying and Classifying Ambiguity for Regulatory Requirements},
10	  author={Massey, Aaron K. and Rutledge, Richard L. and Ant{\'o}n, Annie I. and Swire, Peter P.},
11	  booktitle={22nd IEEE International Requirements Engineering Conference (RE)},
12	  year={2014},
13	  doi={10.1109/RE.2014.6912250}
14	}
15	
16	@techreport{berry_kamsties_2004,
17	  title={From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook},
18	  author={Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.},
19	  institution={University of Waterloo},
20	  year={2004}
21	}
22	
23	@inproceedings{chantree_2006,
24	  title={Identifying Nocuous Ambiguities in Natural Language Requirements},
25	  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},
26	  booktitle={14th IEEE International Requirements Engineering Conference (RE)},
27	  year={2006}
28	}
29	
30	@incollection{wasow_ambiguity_2005,
31	  title={The Puzzle of Ambiguity},
32	  author={Wasow, Thomas and Perfors, Amy and Beaver, David},
33	  booktitle={Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe},
34	  publisher={CSLI Publications},
35	  year={2005}
36	}
37	
38	@article{kennedy_vagueness_2007,
39	  title={Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives},
40	  author={Kennedy, Christopher},
41	  journal={Linguistics and Philosophy},
42	  volume={30},
43	  number={1},
44	  pages={1--45},
45	  year={2007},
46	  doi={10.1007/s10988-006-9008-0}
47	}
48	
49	@article{willis_nocuous_2008,
50	  title={Automatic Identification of Nocuous Ambiguity},
51	  author={Willis, Alistair and Chantree, Francis and De Roeck
…[truncated 1993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2185 · 2026-05-23T09:29:29.315363+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_25/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_25/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2186 · 2026-05-23T09:29:29.817539+00:00_

-rw-r--r-- 1 ubuntu ubuntu 529722 May 23 09:24 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_25/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2187 · 2026-05-23T09:29:29.968583+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2188 · 2026-05-23T09:29:30.019609+00:00_

## Review Issues Tracker — policy_ambiguity_safety
## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
## Venue: EMNLP 2026 via ARR May cycle
## Latest Round: 24

# ============================================================
# R24 ISSUES — IN PROGRESS
# ============================================================

- id: "R24-N1"
  summary: "Novelty framing 偏强——'first matched-pair causal study' 是领域迁移而非方法论创新"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 24
  last_seen_round: 24
  mentions:
    - round: 24
      reviewers: [1, 2]
      note: "R2 Must-Fix, R1 AGREE。共识：从'first causal study'转向'diagnostic taxonomy + systematic nocuity'作为核心卖点"
  action_items:
    - round: 24
      action: "双锚结构重写 §1 contributions：(1) causal study 作为基础, (2) diagnostic taxonomy 作为 intellectual headline, (3) disambiguation neglect + systematic nocuity"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R24-N2"
  summary: "Incompleteness confound framing 不够突出——confound-free range 应作为 headline [复发×4: R21→R24]"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 21
  last_seen_round: 24
  mentions:
    - round: 22
      reviewers: [1, 2]
      note: "R22-W5: token count proxy 粗糙"
    - round: 23
      reviewers: [1, 2]
      note: "R23-W1: 标记为 resolved 但本轮复发"
    - round: 24
      reviewers: [1, 2]
      note: "R1 Must-Fix: framing 核心问题; R2 AGREE 但认为 0.1pp 实际影响微小"
  action_items:
    - round: 24
      action: "Abstract lead with confound-free +31.0pp; 34.0pp 降为补充数字; Conclusion 同步"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R24-N3"
  summary: "SOPBench 63% 效应压缩——外部效度未充分讨论"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 24
  last_seen_round: 24
  mentions:
    - round: 24
      reviewers: [1, 2]
      note: "R1 Must-Fix, R2 AGREE。SOPBe
…[truncated 12219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2189 · 2026-05-23T09:29:55.167548+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 2190 · 2026-05-23T09:30:13.747479+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18579
}
```

</details>

---


### Tool call

_source line 2191 · 2026-05-23T09:30:14.506517+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性与实验设计**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（via ACL Rolling Review May cycle）\n- **投稿类别**: Long paper\n- **正文页数限制**: 8 页（不含 references 和 appendix）\n- **模板**: ACL 2026 template\n- **匿名规则**: Double-blind\n- **Limitations**: 必须在正文中包含，不计入页数限制\n- **截止日期**: 2026-05-25\n\n## 论文路径\n- LaTeX 源文件: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_25/submitted.pdf`\n\n## 你的审查侧重\n\n1. **因果推断设计**：matched-pair 设计是否真正建立因果关系？300 clause pairs × 5 models = 2,997 episodes 的样本量是否足够？合成歧义 vs. 自然歧义的生态效度？\n\n2. **统计分析**：McNemar's test、TOST equivalence testing (±15pp SESOI)、方差分解（Type III SS）、ICC 复制——这些统计方法是否正确应用？结论是否得到支持？特别关注：\n   - SESOI ±15pp 的 justification 是否充分\n   - 22.4% clause wording variance vs. 0.4% type variance 的解读\n   - 60.8% 残差方差的讨论\n   - ICC=0.919 仅在 OpenAI family 内计算\n\n3. **控制实验**：perturbation control (Δ=-0.67pp) 是否足以排除表面扰动？incompleteness 的 information-addition confound 处理是否充分？\n\n4. **评估 pipeline**：cross-judge 设计（GPT-5.4 评 3 个模型，GPT-4.1 评 2 个模型）——不对称设计是否引入偏差？human validation (n=100, κ=0.733) 是否足够？failure mode coding (LLM κ=0.52, human κ=0.15) 的可靠性？\n\n5. **复制与泛化**：7 模型复制、SOPBench 跨基准复制的说服力？跨领域 ρ=0.26 对 C2 泛化的影响？\n\n请输出完整审稿报告，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）、Questions、Missing References。",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性与实验设计**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（via ACL Rolling Review May cycle）\n- **投稿类别**: Long paper\n- **正文页数限制**: 8 页（不含 references 和 appendix）\n- **模板**: ACL 2026 template\n- **匿名规则**: Double-blind\n- **Limitations**: 必须在正文中包含，不计入页数限制\n- **截止日期**: 2026-05-25\n\n## 论文路径\n- LaTeX 源文件: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_25/submitted.pdf`\n\n## 你的审查侧重\n\n1. **因果推断设计**：matched-pair 设计是否真正建立因果关系？300 clause pairs × 5 models = 2,997 episodes 的样本量是否足够？合成歧义 vs. 自然歧义的生态效度？\n\n2. **统计分析**：McNemar's test、TOST equivalence testing (±15pp SESOI)、方差分解（Type III SS）、ICC 复制——这些统计方法是否正确应用？结论是否得到支持？特别关注：\n   - SESOI ±15pp 的 justification 是否充分\n   - 22.4% clause wording variance vs. 0.4% type variance 的解读\n   - 60.8% 残差方差的讨论\n   - ICC=0.919 仅在 OpenAI family 内计算\n\n3. **控制实验**：perturbation control (Δ=-0.67pp) 是否足以排除表面扰动？incompleteness 的 information-addition confound 处理是否充分？\n\n4. **评估 pipeline**：cross-judge 设计（GPT-5.4 评 3 个模型，GPT-4.1 评 2 个模型）——不对称设计是否引入偏差？human validation (n=100, κ=0.733) 是否足够？failure mode coding (LLM κ=0.52, human κ=0.15) 的可靠性？\n\n5. **复制与泛化**：7 模型复制、SOPBench 跨基准复制的说服力？跨领域 ρ=0.26 对 C2 泛化的影响？\n\n请输出完整审稿报告，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）、Questions、Missing References。",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 2192 · 2026-05-23T09:30:32.699827+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18193
}
```

</details>

---


### Tool call

_source line 2193 · 2026-05-23T09:30:33.052369+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性、完整性与写作质量**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（via ACL Rolling Review May cycle）\n- **投稿类别**: Long paper\n- **正文页数限制**: 8 页（不含 references 和 appendix）\n- **模板**: ACL 2026 template\n- **匿名规则**: Double-blind\n- **Limitations**: 必须在正文中包含，不计入页数限制\n- **截止日期**: 2026-05-25\n\n## 论文路径\n- LaTeX 源文件: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_25/submitted.pdf`\n\n## 你的审查侧重\n\n1. **新颖性与贡献定位**：\n   - 核心贡献是什么？\"first matched-pair causal study\" 是方法论创新还是领域迁移？\n   - Taxonomy 的价值：6 类歧义分类相对于 Li et al. 2024 的 11 类 taxonomy 有何增量？type 仅解释 0.4% variance 但预测 failure mechanism (Cramér's V=0.45)——这个 \"diagnostic tool\" 定位是否成立？\n   - Disambiguation neglect (4.6%) 和 systematic nocuity (41.3%) 是新发现还是已知现象的新标签？\n\n2. **Related Work 覆盖**：\n   - 与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等同期工作的对比是否充分？\n   - 是否遗漏重要相关工作？特别是 LLM 歧义处理、agent safety evaluation、policy specification 领域\n   - 对 Berry & Kamsties 2004 \"nocuous/innocuous\" 框架的扩展是否恰当？\n\n3. **Claim 校准**：\n   - Abstract/Introduction 中的 claim 强度是否与实际证据匹配？\n   - \"nocuous\" 一词的使用——convergent error vs. divergent interpretation，是否构成对 Berry & Kamsties 的合理扩展？\n   - 34.0pp 在合成条件下 vs. SOPBench 12.6pp——ecological validity 讨论是否充分？\n   - C3 (layer effect) inconclusive 但 taxonomy 仍按两层组织——这是否有问题？\n\n4. **写作质量**：\n   - 论文结构是否清晰？数字密度是否过高？\n   - 术语定义是否一致？特别是 \"ambiguity\" 的广义使用（含 vagueness、incompleteness、normative conflict）\n   - Limitations 是否充分且简洁（EMNLP 要求一小段，~3 个点）？\n\n5. **格式合规**：\n   - 正文是否在 8 页以内？\n   - 匿名化是否完整？有无 self-citation 泄露？\n   - Data/Code availability URL 是否匿名？\n   - References 格式是否一致？\n\n请输出完整审稿报告，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）、Questions、Missing References。",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性、完整性与写作质量**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（via ACL Rolling Review May cycle）\n- **投稿类别**: Long paper\n- **正文页数限制**: 8 页（不含 references 和 appendix）\n- **模板**: ACL 2026 template\n- **匿名规则**: Double-blind\n- **Limitations**: 必须在正文中包含，不计入页数限制\n- **截止日期**: 2026-05-25\n\n## 论文路径\n- LaTeX 源文件: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_25/submitted.pdf`\n\n## 你的审查侧重\n\n1. **新颖性与贡献定位**：\n   - 核心贡献是什么？\"first matched-pair causal study\" 是方法论创新还是领域迁移？\n   - Taxonomy 的价值：6 类歧义分类相对于 Li et al. 2024 的 11 类 taxonomy 有何增量？type 仅解释 0.4% variance 但预测 failure mechanism (Cramér's V=0.45)——这个 \"diagnostic tool\" 定位是否成立？\n   - Disambiguation neglect (4.6%) 和 systematic nocuity (41.3%) 是新发现还是已知现象的新标签？\n\n2. **Related Work 覆盖**：\n   - 与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等同期工作的对比是否充分？\n   - 是否遗漏重要相关工作？特别是 LLM 歧义处理、agent safety evaluation、policy specification 领域\n   - 对 Berry & Kamsties 2004 \"nocuous/innocuous\" 框架的扩展是否恰当？\n\n3. **Claim 校准**：\n   - Abstract/Introduction 中的 claim 强度是否与实际证据匹配？\n   - \"nocuous\" 一词的使用——convergent error vs. divergent interpretation，是否构成对 Berry & Kamsties 的合理扩展？\n   - 34.0pp 在合成条件下 vs. SOPBench 12.6pp——ecological validity 讨论是否充分？\n   - C3 (layer effect) inconclusive 但 taxonomy 仍按两层组织——这是否有问题？\n\n4. **写作质量**：\n   - 论文结构是否清晰？数字密度是否过高？\n   - 术语定义是否一致？特别是 \"ambiguity\" 的广义使用（含 vagueness、incompleteness、normative conflict）\n   - Limitations 是否充分且简洁（EMNLP 要求一小段，~3 个点）？\n\n5. **格式合规**：\n   - 正文是否在 8 页以内？\n   - 匿名化是否完整？有无 self-citation 泄露？\n   - Data/Code availability URL 是否匿名？\n   - References 格式是否一致？\n\n请输出完整审稿报告，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）、Questions、Missing References。",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 2194 · 2026-05-23T09:30:34.469294+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1416
}
```

</details>

---


### Assistant

_source line 2195 · 2026-05-23T09:30:44.413430+00:00_

Round 1 已启动：
- 视觉审查 Agent 已派发（与审稿并行）
- Reviewer 1（方法严谨性）已分配
- Reviewer 2（新颖性/完整性）已分配

等待两位 Reviewer 完成独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 207

## Round 207

2 recorded events


### User

_source line 2196 · 2026-05-23T09:37:03.171543+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告 — Round 1 (新颖性、完整性与写作质量)

**论文标题**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety
**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle)

---

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 一项实验设计扎实、claim 校准得当的因果研究，但核心新颖性主要是方法论的领域迁移而非概念创新，taxonomy 相对于 Li et al. (2024) 的增量贡献需要更强的论证，且"ambiguity"的广义使用可能引起 NLP 社区读者的困惑。

## 官方维度打分（ACL ARR Review Form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | Matched-pair 因果设计严谨，统计分析充分（permutation tests, ICC, bootstrap），claims 用 confound-free range 和置信区间恰当地 hedge；C3 inconclusive 也坦诚报告 |
| Excitement | 3 / 5 | 研究问题重要且及时，但核心贡献是已有方法（matched-pair design）在新领域（policy-agent safety）的应用，taxonomy 是对 Li et al. 的 condensation 而非全新构建；最有趣的 finding（type predicts mechanism but not rate）没有在 framing 中获得足够突出的位置 |
| Reproducibility | 4 / 5 | 代码承诺公开，clause pair 构建流程描述清晰（§4.2, Appendix S），统计方法完整；但 500 clause pair 中 annotator 协议细节（13 disagreements 如何 resolve）和 GPT-5.4 prompt 模板未在正文或 appendix 展示 |
| Confidence | 4 / 5 | 熟悉 NLP 歧义处理、agent safety evaluation 和因果推断方法 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Taxonomy 增量贡献论证不足——与 Li et al. (2024) 11-type taxonomy 的关系
- 具体位置：§3 Ambiguity Taxonomy（p3-4）, §1 Introduction（p1-2, contributions list）
- 问题：论文声称构建了一个 6-type, two-layer taxonomy，并说明设计基于三个标准：(1) RE 文献的理论动机，(2) matched-pair 构建的可行性，(3) 无歧义 IV 赋值的互斥性。但相对于 Li et al. (2024) 的 11-type NLP taxonomy（syntactic, semantic, pragmatic），论文仅用一句话解释了 condensation 逻辑（"selected from Li et al. (2024b)'s N.P. taxonomy (11 types) based on three design criteria"）。读者无法判断：哪 5 个 types 被排除？排除标准是理论的还是实验便利性驱动的？6 个保留的 types 是否覆盖了真实 policy documents 中最常见的歧义类型？Appendix AC 的 real-world policy audit（24 documents, 407 clauses）部分回答了这个问题，但该审计结果没有被用来论证 taxonomy 的覆盖度。
- 为什么影响接收：Taxonomy 是论文的三个核心贡献之一（C2, C3）。如果 taxonomy 仅是为实验便利性而裁剪的 subset，其作为"diagnostic tool"的普适性就大打折扣。
- 建议修改方向：(1) 在 §3 或 Appendix 中增加一个表格，明确列出 Li et al. 11 types → 本文 6 types 的映射和排除理由；(2) 用 Appendix AC 的 real-world distribution 数据论证 6 types 覆盖了实际 policy documents 中 >X% 的歧义实例。

**N2** [critical] "Ambiguity" 的广义使用与 NLP 社区标准定义的张力
- 具体位置：§3 第一段（p3, "Scope of 'ambiguity'"）, Abstract（p1）
- 问题：论文明确承认采用广义的"ambiguity"定义（"Our taxonomy uses ambiguity broadly to encompass policy features admitting multiple operationally distinct interpretations by an LLM agent"），将 incompleteness（缺失信息）、normative conflict（规则冲突）、vagueness（模糊性）都纳入"ambiguity"范畴。在 NLP/计算语言学传统中，ambiguity 严格指同一表达有多个合法解析（syntactic/semantic ambiguity），与 vagueness（边界模糊但单一解析）和 incompleteness（信息缺失）是不同概念。论文虽声明了这一选择，但仅用"because LLM agents process all six types identically—committing to a single interpretation without flagging uncertainty"来论证。这个论证不充分：LLM 处理方式相同不意味着语言学分类应该合并。
- 为什么影响接收：ACL/EMNLP 读者群包含大量语言学背景的审稿人。广义"ambiguity"可能被视为术语误用，削弱论文在该社区的可信度。更关键的是，incompleteness 类型（49.2pp effect）的效应量远高于其他类型，但其 confound（information addition, §4.5）使其难以与"歧义"效应区分——这恰恰说明 incompleteness 和真正的 ambiguity 在机制上不同。
- 建议修改方向：(1) 考虑使用更宽泛的上位术语如"policy specification defects"或"policy underspecification"作为总称，保留"ambiguity"给真正的多解析类型；(2) 至少在 §3 中增加一段讨论这一术语选择与 NLP 传统分类之间的关系。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] C3（layer effect）inconclusive 但 taxonomy 仍按 two-layer 组织——理论动机 vs 经验支撑的张力
- 具体位置：§5.2（p6）, §1 contributions（p2, "a two-layer taxonomy"）
- 问题：论文将 taxonomy 组织为 linguistic layer (lexical, scopal, cond. precedence) 和 specification layer (auth. scope, incompleteness, conferential)。但 C3 的检验结果是 inconclusive（"C3 (layer effect) is inconclusive"）——TOST 等价性检验在 ±15pp margin 下仅有两对通过，六对中四对残留差异显著。论文解释这是因为 within-layer heterogeneity（e.g., incompleteness 55.6% vs lexical 41.6%）。这意味着 two-layer 结构主要是理论借用（from RE literature, Berry & Kamsties），缺乏经验支撑。论文虽坦承了这一点，但在 contributions 列表和 abstract 中仍把"two-layer taxonomy"作为核心贡献展示，可能误导读者以为 layer 区分有经验依据。
- 建议：在 §3 开头明确声明 two-layer 结构是基于理论的组织框架（organizational framework），而非经验发现的层级效应。在 contributions 列表中调整 C3 的表述。

**W2** [warning] 合成条件 (34.0pp) vs SOPBench (12.6pp) 的 ecological validity gap 讨论不充分
- 具体位置：§8 Conclusion（p8）, Limitations（p9）, Appendix Z（p19）
- 问题：主实验在 τ²-bench 上用合成注入的 clause pairs 测试，effect size 为 34.0pp（confound-free ≥27.3pp）。SOPBench 复制实验仅获得 12.6pp 的效应。论文在 Conclusion 中报告了 SOPBench 数字作为"directional consistency"，但两个数字之间近 3 倍的差距没有被充分讨论。Appendix Z 列出了三个结构性差异（episode-level vs clause-level measurement, test-constraint vs policy-constraint boundaries, interaction effects），但正文中只用"directional consistency"一带而过。这个差距对论文的实践指导意义至关重要：如果真实世界的效应更接近 12.6pp 而非 34pp，干预的优先级判断会完全不同。
- 建议：在 §7 Discussion 或 §8 Conclusion 中用 2-3 句话正式讨论效应量差距的原因和对实践的影响。

**W3** [warning] "Nocuous" 术语的概念延伸过度
- 具体位置：Title, Abstract, §6.3（p8）
- 问题：Berry & Kamsties (2004) 定义 nocuous ambiguity 为"不同 stakeholder 对同一表述产生不同解释，导致有害后果"——核心是 divergent interpretation。本文的 §6.3 发现是"systematic nocuity"——models converge on the same wrong interpretation（convergent error）。论文在 §6.3 明确说"our agents exhibit convergent rather than divergent errors"，但标题仍用"Nocuous"来概括全文发现。将"所有模型收敛到同一个错误解释"称为"nocuous"是对 Berry & Kamsties 框架的重大概念转换，因为 convergent misinterpretation 和 divergent interpretation 在机制上完全不同：前者暗示 systematic bias in training data，后者暗示 genuine interpretive ambiguity。
- 建议：(1) 在 Abstract 或 §1 中更早、更明确地说明本文对"nocuous"的扩展定义；(2) 讨论这种扩展的合理性——为何 convergent error 也应称为"nocuous"而非使用不同术语。

**W4** [warning] Disambiguation neglect (4.6%) 的新颖性不清晰
- 具体位置：§6.2（p8）, Appendix V
- 问题：论文发现 agents 仅在 4.6% 的情况下尝试 disambiguate（请求澄清），并将其命名为"disambiguation neglect"。但 LLM 倾向于直接回答而非请求澄清是一个已知现象，在 Tamari et al. (2023)、Suri et al. (2025) 等文献中已有讨论。论文在 Related Work (§2, p2-3) 中引用了这些工作，但没有明确说明本文的 4.6% 发现相对于已知现象提供了什么增量贡献（例如：是否第一次在 policy compliance context 中量化？是否发现了 type-specific 的 clarification 率差异？）。
- 建议：在 §6.2 中增加 1-2 句话说明本文发现的具体增量。

**W5** [warning] 数字密度过高，叙事线索被淹没
- 具体位置：§5 Results, §6 Error Analysis（p5-8）
- 问题：正文 8 页中包含极高密度的统计数字：CI, p-values, OR, Cramér's V, NMI, TOST margins, LOO values, ICC 等。例如 §5.1 一个段落中包含了 41.0% vs 6.9%, OR=15.1, 95% CI [10.78, 21.17], p<10^-116, p<10^7, ±25.7 to +39.0pp, p<10^-15 等数字。虽然统计严谨性值得肯定，但这种密度使得非统计方法背景的读者难以提取核心 takeaway。
- 建议：考虑将部分详细数字移至 appendix（已有的 Table 3 sensitivity analysis 是好的实践），在正文中保留关键 effect sizes 和定性结论。

---

## 小问题（不影响接收）

**M1** Table 1（p3）的 "Disambig. Channel" 列中的描述过于简短（如"Lexical context"、"Quantifier hierarchy"），对不熟悉 RE 文献的读者可能不够直观。建议增加 1-2 个字的说明或在 caption 中补充。

**M2** Figure 2（p6）的 per-type effect sizes 使用 "(App)" 来标记上界，但正文中对"upper bound"的含义（incompleteness 的 information-addition confound）要到 §4.5 才解释。建议在 Figure 2 caption 中加一句说明。

**M3** Limitations section（p9）恰当且简洁（3 个要点：合成数据、有限模型集、未追踪 SOPBench），符合 EMNLP 要求。但第一个要点（"synthetically constructed"）与正文中的 ecological validity 讨论有少量重复。

**M4** References（p9-10）格式整体一致（ACL natbib），但部分 arXiv preprints 同时标注了 "arXiv preprint" 和 "Submitted YYYY.MM.DD"，建议统一格式。

---

## Questions for Authors

**Q1**: 关于 DRIP-R (Borakoty et al., 2026) 的映射——Appendix L 将 DRIP-R 的 5 个 RE ambiguity categories 映射到你们的 6-type taxonomy。但 DRIP-R 的核心 setup 是 "no single correct resolution"（真正的开放式歧义），而你们的 matched-pair design 预设了 ground truth（unambiguous version 是正确答案）。你们如何论证你们的 taxonomy 和发现可以推广到 DRIP-R 式的真实歧义场景？

**Q2**: Incompleteness type 贡献了最大的 effect size（49.2pp, Table 2）但同时有最强的 confound（information addition）。如果排除 incompleteness，剩余 5 types 的 pooled effect（confound-free 31.0pp）是否仍具有实践意义？换言之，如果 incompleteness 的效应主要来自"缺失信息"而非"歧义"，那么纯粹由歧义驱动的安全风险有多大？

**Q3**: Taxonomy-as-diagnostic-tool 的定位（§7, Cramér's V=0.45 for mechanism prediction vs 0.4% variance for rate prediction）是论文最有趣的发现之一。但 failure mechanism 的分类本身（structural misparse, info gap-filling, boundary violation）是否也是 post-hoc 的？如果是，type→mechanism 的关联是否存在 circular reasoning 风险？

**Q4**: 论文使用 5 个 models（2 closed + 3 open），但 Claude Sonnet 4.6 在 authorization scope violations 方面表现出明显异常（64% violation rate, Table 2）。这个异常是否影响了 pooled estimates？sensitivity analysis 是否排除了 Claude 后仍然稳健？

---

## Missing References / Related Work 覆盖评估

**已引用且充分**: Berry & Kamsties 2004, Li et al. 2024, τ²-bench (Barres et al. 2025), MANTRA (Anand et al. 2026), PolicyBank (Choi et al. 2026), SOPBench (Li et al. 2025), DRIP-R (Borakoty et al. 2026), SafeAgentBench, ShieldAgent.

**已引用但讨论不足**:
- DRIP-R (2026): 仅在 Appendix L 中做 category mapping，正文中缺乏对两种研究范式差异的讨论（matched-pair with ground truth vs. genuinely ambiguous scenarios）。作为最直接的同期竞争工作，至少应在 §2 Related Work 中用 2-3 句话对比核心方法论差异。

**可能遗漏**:
- Gao-Arch et al. (2026) "Ambiguity collapse in LLMs" (arXiv:2603.05890) — 论文已引用，但这篇工作的 "ambiguity collapse" 概念与本文的 "systematic nocuity"（convergent error）高度相关，值得在 §6.3 或 §7 Discussion 中对比讨论。

---

## 主要优势

**S1** Matched-pair 因果设计是该领域的方法论进步：通过控制 clause wording 的 minimal edits，实现了比观测研究更干净的因果推断。permutation control（perturbation effect ≈ -0.67pp, §4.5）有效排除了非歧义相关的 confound。

**S2** Claim 校准得当：论文系统性地使用 confound-free range（≥27.3pp）、upper bound 标记（incompleteness）、TOST 等价性检验，避免了 over-claiming。C3 inconclusive 被坦诚报告。这在该领域的论文中并不常见。

**S3** 多层次复制增强了可信度：5 models × 6 types × cross-judge validation（3 judges, ICC=0.749）+ SOPBench 跨 benchmark 复制 + 2 additional model families（Gemini, LLAMA）。

**S4** Type→mechanism 的发现（Cramér's V=0.45 vs type→rate 0.4%）是一个有价值的理论贡献：说明 taxonomy 的价值在于 failure diagnosis 而非 rate prediction，这为后续的 targeted mitigation 工作提供了 actionable framework。

**S5** Real-world policy audit（Appendix AC, 24 documents, 407 clauses）提供了 external validity 的初步证据，虽然规模有限。

---

## 格式合规检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文 ≤ 8 页 | ✓ | §1-§8 正好 8 页（p1-p8），Limitations 在 p9 |
| 匿名化 | ✓ | "Anonymous ACL submission"，代码 URL 用 anonymous placeholder |
| Limitations section | ✓ | 在正文中，简洁（~3 个要点），不在 appendix |
| Self-citation 泄露 | 未检测到 | 未发现明显的 self-identifying 引用模式 |
| References 格式 | 基本一致 | 少量 arXiv preprint 格式不统一（M4）|
| Data/Code availability | ✓ | 提供匿名 GitHub URL |
| ACL template | ✓ | 标准 ACL 2-column format |

---

## 总结

这是一篇实验设计扎实、统计分析严谨的实证研究，回答了一个重要且及时的问题。主要优势在于 matched-pair 因果设计、claim 的谨慎校准、以及 type→mechanism 的有价值发现。主要不足是 taxonomy 相对于 Li et al. 的增量贡献论证不够充分（N1），"ambiguity" 的广义使用可能引起 NLP 社区的术语争议（N2），以及合成条件与真实环境之间的效应量差距需要更深入的讨论（W2）。如果 N1 和 N2 得到充分回应（增加 mapping 表格、调整术语框架），论文可达到 Conference 水平。当前状态适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2197 · 2026-05-23T09:37:12.153311+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 208

## Round 208

2 recorded events


### User

_source line 2198 · 2026-05-23T09:37:25.689477+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**评分摘要**：Overall 3.5（Borderline Conference），Soundness 4/5，Excitement 3/5。

**核心判断**：实验设计扎实（matched-pair causal design + 多层复制），claim 校准得当，但两个 Must-Fix 问题可能影响接收——(N1) taxonomy 相对于 Li et al. 2024 的增量贡献论证不足，缺少 11→6 types 的映射和排除理由；(N2) "ambiguity" 广义使用（涵盖 incompleteness、normative conflict）与 NLP 社区的标准定义有张力，且 incompleteness 的 information-addition confound 恰恰说明它在机制上不同于真正的歧义。

另有 5 个 Should-Fix（C3 inconclusive vs two-layer framing、synthetic/SOPBench 效应量差距、"nocuous" 术语延伸、disambiguation neglect 新颖性、数字密度）和 4 个小问题。格式合规检查全部通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2199 · 2026-05-23T09:37:30.800441+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 209

## Round 209

6 recorded events
