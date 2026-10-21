---
round: 20
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T02:47:01.848681+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 20 审稿报告
## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
## Venue: EMNLP 2026 via ARR May cycle
## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)
## 审稿模式: Fresh (重新审稿)

---

## Summary

本文研究 LLM agent 在自然语言策略规范中遇到歧义时是否会产生安全违规。作者构建了 300 对匹配的歧义/非歧义 clause pairs，涵盖六类歧义分类（两层：语言层 + 规范层），在 τ²-bench 上评估五个模型（2,997 episodes）。核心发现：(1) 歧义在合成控制条件下增加 34.0pp 违规率（conditional OR=15.1）；(2) clause wording 解释 22.4% 方差（vs. type 仅 0.4%），但 type 预测 failure mechanism 的能力是预测违规率的 17 倍；(3) agent 对歧义的元认知意识极低（≤11%），41.3% 的歧义 clause 触发多模型趋同违规。

---

## Strengths

**S1 [共识]** 匹配对因果设计在 agent safety 领域属方法论创新——相比 DRIP-R 的关联性设计和 PolicyBank 的迭代优化，这是唯一提供因果证据的工作。300 clause pairs 的规模和匹配质量（κ=0.95）可信。

**S2 [共识]** 多层 robustness 堪称全面：perturbation control（n=300, Δ=-0.67pp, CI 含零）、cross-judge 三族验证（Fleiss' κ=0.717）、cross-benchmark 复现（SOPBench）、七模型跨架构复现（6 providers）。对 C1 的支撑层层递进。

**S3 [共识]** "clause wording drives risk, type predicts mechanism" 的双重分解是最有洞察力的发现。22.4% vs. 0.4% 的方差分解和 NMI 分析将 taxonomy 从分类标签转化为诊断工具，是有说服力的 reframing。

**S4 [共识]** Claims 校准诚实：C3 标注 inconclusive, C4 标注 exploratory；incompleteness confound 被充分讨论；authorization scope 的低可靠性被反复提示。统计方法选择与数据结构匹配（McNemar, TOST, Holm-Bonferroni, bootstrap cluster）。

**S5 [共识]** Appendix 深度可圈可点：19 个 appendix sections 覆盖了几乎所有可预见的 reviewer 质疑。Limitations 章节覆盖五个方面（生态效度、范围、测量、confound、disambiguation channel），坦诚且具体。

---

## Weaknesses

### Must-Fix 问题（两位 Reviewer 共识）

**N1 [critical, 共识]** Failure mode taxonomy 与 ambiguity taxonomy 的定义循环性

"Type predicts failure mechanism 17× more strongly than violation rate" 是 Abstract/Discussion/Conclusion 的核心卖点之一。但三种 failure mechanisms 与 ambiguity types 存在定义层面的高度重叠：
- Authorization scope → boundary violation（72/104 traces, 69%）：如果 authorization boundary 模糊，agent 越权就被编码为 "boundary violation"——这是同一现象的两种描述
- Incompleteness → information gap-filling（70/134 traces）：信息缺失时 agent 用默认值填充，编码为 gap-filling——这是 incompleteness 的直接语义后果

混淆矩阵（Table 14）显示映射并非完全 tautological（如 incompleteness 也有 43 structural misparse），但 MI 的绝对值被定义重叠抬高。此外，failure mode 编码使用 LLM 标注 LLM 失败（§6 自己承认 "introduces circularity risk"），编码者间一致性仅 moderate（Gwet's AC₁=0.62, κ=0.52）。论文的反驳——"MI between exogenous type and mechanism labels provides anti-circularity evidence"——在定义重叠面前说服力不足。

**要求修改**：(1) 区分哪些 type→mechanism 映射是定义驱动的（auth scope→boundary, incompleteness→gap-filling）vs. 经验发现的（scopal→structural misparse），分别报告 MI；(2) 弱化 "17×" 为定性表述（如 "substantially better"），不再使用精确倍数作为核心卖点；(3) 对至少 100 traces 进行人工 failure mode 编码验证，或在 Limitations 中明确标注为局限。

**N2 [critical, 共识]** 遗漏重要相关工作 Ambig-SWE (Mou et al., ICLR 2026)

Ambig-SWE (arXiv:2502.13069) 直接研究 agent 在 underspecified/ambiguous 指令下的行为，发现交互式 disambiguation 可将性能提升高达 74%。该论文区分了 ambiguity 和 underspecificity——与本文 linguistic/specification 两层分类直接对应。这是 2026 年 top venue 发表的最直接相关工作。

R1 补充：Ambig-SWE 的发现与本文 mitigation experiment（Appendix B）互补而非矛盾——本文证明 default settings 下存在 neglect，Ambig-SWE 证明 interactive 设置下可部分恢复。但不讨论这一对比会削弱 §6.2 和 Discussion 的说服力。

**要求修改**：在 §2 Related Work 引用 Ambig-SWE，在 §6.2 或 §7 Discussion 讨论 interactive vs. non-interactive 设置下 disambiguation 行为的差异，在 §9 Limitations "Disambiguation channel" 段引用 Ambig-SWE 作为对比证据。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning]** SESOI ±15pp 缺乏外部锚定——C2 mid-tier cluster 在 ±10pp 下瓦解（仅 3/6 pairs 等价，power=0.57）。R2 指出论文已有 Table 3 七 margin 敏感性 + bootstrap cluster analysis 作为 margin-free 补充，C2 表述已为 "robust extremes"。但 Abstract 中 "partial ordering" 未附 margin 条件，§4.6 操作性论证缺部署数据支撑。**建议**：Abstract 限定 margin 条件；§4.6 承认无行业标准 SESOI。

**W2 [warning]** Taxonomy 新颖性定位模糊——六类直接源自已有分类体系，排除 ellipsis/pragmatic implicature 缺乏量化依据。R1 指出论文已有定位（§3 "experimental instrument"、Appendix L DRIP-R 映射），核心贡献是 matched-pair evidence 而非 taxonomy 本身。**建议**：§3 增加类型选择的操作标准；明确声明 taxonomy 是实验 IV 的操作化。

**W3 [warning]** Cross-judge 分配非随机化——matched-pair 差异中 judge bias 抵消仅在 additive bias 假设下成立。Appendix W 三族验证仅覆盖 ambiguous condition，judge×condition 交互效应未排除。**建议**：补充 unambiguous condition 的 cross-judge 验证或在 Limitations 中标注此假设。

**W4 [warning]** Disambiguation neglect 与 ambiguity collapse 概念区分度不足——Liu et al. (2023) 和 Gur-Arieh et al. (2026) 已有 ambiguity collapse 概念。本文差异主要在 agentic context 的后果层面。**建议**：弱化 disambiguation neglect 作为独立概念的强调，定位为 ambiguity collapse 在 agentic context 下的后果验证。

**W5 [warning]** 生态效度量化差距——34.0pp (τ²-bench) vs. 12.6pp (SOPBench)，5 个模型中仅 3 个达到 individual significance。Abstract/Conclusion 以 34.0pp 为 headline，未讨论自然歧义 prevalence 作为 effect-to-impact 的 scaling factor。**建议**：Abstract 或 Conclusion 中提及 SOPBench 的 +12.6pp 作为 cross-benchmark reference；Limitations 讨论 prevalence 对实际影响的调节作用。

**W6 [warning]** Human validation per-type 样本量不足（n=32-34）——scopal κ CI=[0.00, 1.00] 几乎无信息量。正文 §4.4 的表述可能给 type-level reliability 过于乐观的印象。**建议**：正文更明确指出 human validation 仅支持 pooled 层面的 pipeline 可靠性。

**W7 [warning]** Perturbation control 仅测试 surface-level specificity——R2 指出 coreferential 类型（lexically identical, Δ=0）已提供天然的信息量控制，token count regression 方向与 information-addition 假设相反。但 token count 是粗糙代理。**建议**：Limitations 中明确指出 information-addition control 的缺失。

**W8 [warning]** Variance decomposition 中 clause-level vs. type-level auditing 的 actionability 讨论不足——22.4% clause identity 中 22.0% 是 within-type 变异，clause-level auditing 在大规模文档中可能不可行；type-level auditing 仅 0.4% 方差但更可操作。**建议**：Discussion 中区分两种审计策略的成本-收益。

**W9 [warning]** Bib 条目问题——yu_causal_2026 与 yu2026causal 重复条目；3 条 Anonymous 作者（disambiguation_cqa_survey_2025, atbench_2026, riskybench_2026）；tamkin_evaluating_2023 使用 @inproceedings 但 booktitle 为 arXiv。**要求修复**。

**W10 [warning]** 其他可能遗漏文献——Ambig-DS (arXiv:2605.09698), Active Task Disambiguation (arXiv:2502.04485), CAR-bench (arXiv:2601.22027)。**建议**：逐条审查并按相关性纳入。

**W11 [warning]** Abstract 信息密度过高——7+ 数值指标（34.0pp, OR=15.1, +18.7 to +36.0pp, 22.4% vs 0.4%, 17×, ≤11%, 41.3%）超出工作记忆容量。**建议**：精简至 3-4 个核心数值。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：

1. **Failure mode 定义循环是核心弱点** (N1)——17× claim 的可信度受定义重叠和 LLM 编码循环性影响
2. **Ambig-SWE 必须引用** (N2)——ICLR 2026 top venue，直接相关
3. **方法论质量高** (Soundness 4)——matched-pair 因果设计、多层 robustness、claims 校准诚实
4. **新颖性处于 borderline** (Excitement 3)——结果方向可预期，taxonomy 增量，disambiguation neglect 与已有概念重叠
5. **生态效度是主要限制**——合成歧义上界 + SOPBench replication 效力偏弱
6. **Abstract 数值密度过高**

## Reviewer Divergence

以下问题存在分歧（已在交叉回应中部分收敛）：

1. **R1-N2 → R2 部分反驳 [REBUT]**：R1 认为 SESOI ±15pp 缺乏外部锚定是 critical must-fix；R2 认为论文已有七 margin 敏感性分析 + margin-free bootstrap cluster，处理较充分，建议降级为 should-fix 并在 Abstract 附限定条件。**Director 判断**：采纳 R2 的降级建议，列为 W1 (should-fix)——论文的 Appendix A 和 §5.2 末尾已经提供了读者在任何阈值下评估 C2 的充分信息。

2. **R2-N2 → R1 反驳 [REBUT]**：R2 认为 taxonomy 新颖性不足是 critical must-fix；R1 认为论文已明确定位 taxonomy 为 experimental instrument，核心贡献是 matched-pair evidence。**Director 判断**：采纳 R1 的降级建议，列为 W2 (should-fix)——§3 和 Appendix L 的定位已经清晰，但可进一步明确类型选择的操作标准。

3. **R1-W3 → R2 部分反驳 [REBUT]**：R1 认为 perturbation control 的 construct validity 不足；R2 指出 coreferential 类型和 token count regression 已部分回应。**Director 判断**：列为 W7 (should-fix)，仅需在 Limitations 中补充一句。

---

## Questions

1. Failure mode 编码是否有人工验证子集？如果没有，是否可以在 camera-ready 前完成至少 100 traces 的人工编码？
2. 同批 annotators 是否既创建又验证了 clause pairs？如果是，如何排除 confirmation bias？
3. Authorization scope 的 per-type ICC ≈ 0 与其在 C4 中的 prominent role 如何调和？

---

## Missing References

1. **Ambig-SWE** (Mou et al., ICLR 2026, arXiv:2502.13069) — [Must-Fix] agent 在 ambiguous 指令下的行为，交互式 disambiguation
2. **Ambig-DS** (arXiv:2605.09698, 2025) — data-science agent 的 task-framing ambiguity
3. **Active Task Disambiguation with LLMs** (arXiv:2502.04485, 2025) — 主动 disambiguation 策略
4. **CAR-bench** (arXiv:2601.22027, 2026) — agent 不确定性下的一致性和 limit-awareness

---

## External Review

外部审稿：未请求（项目配置未启用）。

---

## Visual Layout Check

视觉审查：仍在进行中，本报告不等待。完成后会自动补发到 Group C。

---

## Overall Assessment

**Overall Score: 3.5 / 5 (Borderline Conference)**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Overall | 3.5 | 3.5 | **3.5** |
| Soundness | 4 | 4 | **4** |
| Excitement | 3 | 3 | **3** |
| Confidence | 4 | 4 | **4** |

**核心判断**：方法论执行到位（Soundness 4），matched-pair 因果设计、多层 robustness checks、诚实的 claims 校准在 agent safety 文献中属上乘。但存在两个关键弱点：(1) "17× diagnostic power" 的核心论证存在定义循环风险，需弱化表述并区分定义驱动 vs. 经验发现的 type→mechanism 映射；(2) 遗漏了 ICLR 2026 的直接相关工作 Ambig-SWE。新颖性处于 borderline——结果方向可预期，taxonomy 增量，disambiguation neglect 与已有概念重叠度高。

**接收条件**：如果作者能 (1) 弱化 17× 为定性表述并讨论定义循环，(2) 补充 Ambig-SWE 引用并讨论 interactive vs. non-interactive disambiguation，(3) 精简 Abstract 数值密度，(4) 修复 bib 条目问题，本文可达 Conference 水准（4.0）。

---

## Detailed Comments

### §1 Introduction
- Contribution (2) "variance decomposition...combined with mutual information analysis showing that type predicts failure mechanism 17× better" — 17× 需弱化（见 N1）
- 建议在 contribution 声明中更突出因果设计本身作为方法论贡献

### §2 Related Work
- 缺少 Ambig-SWE (ICLR 2026) — Must-Fix N2
- 可能遗漏 Ambig-DS, Active Task Disambiguation, CAR-bench — W10
- "Psycholinguistics of ambiguity processing" 段落可引用 Ambig-SWE 作为 interactive disambiguation evidence

### §3 Ambiguity Taxonomy
- 类型选择标准 ("frequency in operational policy documents") 缺乏量化数据支撑 — W2
- 建议增加一句明确声明 taxonomy 是实验 IV 的操作化而非分类标准

### §4 Method
- §4.2 同批 annotators 创建+验证的 confirmation bias 风险未讨论 — M2
- §4.4 Human validation per-type 不确定性在正文中传达不足 — W6
- §4.4 McNemar's test (9 vs 6 discordant pairs) 检验力有限
- §4.5 Perturbation control 测试 surface-level specificity，information-addition control 缺失 — W7
- §4.6 SESOI ±15pp 操作性论证缺部署数据支撑 — W1

### §5 Results
- §5.1 "Clause wording—not type membership—drives variance" 与 "significant type heterogeneity (χ²=28.02, V=0.137)" 的 juxtaposition 可加一句说明 V=0.137 对应 ~1.9% variance
- §5.2 C2 的 "partial ordering" 应在 Abstract 中附 margin 条件 — W1
- Abstract 中 "+18.7 to +36.0pp" 应限定为 type-level range

### §6 Error Analysis
- §6 Failure mode 定义循环性 — N1
- §6.2 Disambiguation neglect vs. ambiguity collapse 区分度 — W4

### §7 Discussion
- "clause-level auditing addresses the largest actionable component (22.4%)" — 需区分 clause-level vs. type-level auditing 的可行性 — W8
- 建议引用 Ambig-SWE 讨论 interactive disambiguation channel

### §9 Limitations
- "Disambiguation channel" 段应引用 Ambig-SWE 的 74% improvement 作为对比
- Information-addition control 缺失可增加一句

### References
- 修复重复条目 (yu_causal_2026 / yu2026causal)
- 核实 Anonymous 作者条目真实性
- tamkin_evaluating_2023 改为 @article 类型

### Appendix
- Appendix K (Table 14) 混淆矩阵支持但也暴露定义循环问题 — 建议在正文引用时明确标注哪些映射是 definitional vs. empirical
- Appendix W cross-judge 验证补充 unambiguous condition 会更完整 — W3