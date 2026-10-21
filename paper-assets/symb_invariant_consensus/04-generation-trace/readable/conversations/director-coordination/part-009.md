# Director coordination — Part 9 of 9

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

[← Part 8](part-008.md) · [Transcript overview](../director-coordination.md) · [Structured JSON](../../../sessions/bd/bdd0e6c8e8a0a8a81e76.json)

## Round 182

### Tool call

_source line 2562 · 2026-05-25T21:31:07.221066+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 23 审稿报告（Fresh Review）\n\n**项目**: symb_invariant_consensus\n**Venue**: EMNLP 2026 (ARR)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+Related Work）\n**圆桌轮次**: 1 轮（两位 Reviewer 独立初审 + 交叉分享后达成共识，无需额外轮次）\n\n---\n\n## Summary\n\n本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM chain-of-thought traces 中提取 FOL 约束并用 Z3 求解 weighted partial MAX-SAT 以选答案。核心发现为负面结果：自提取约束系统性地确认多数投票结果（symbolic confirmation bias, SCB），SICA 在退化条件下归约为多数投票。论文在 9 个模型（7B 到 frontier）、4 个 benchmark 上验证了这一现象，测试了 27 种 training-free 补救策略均失败，提出三项诊断指标（C₀, K_eff, BR），并展示跨架构 NLI verifier 可部分突破瓶颈。\n\n---\n\n## Strengths\n\n**S1.** 实验方法论的高标准远超同类工作——McNemar 检验 + Benjamini-Hochberg 校正 + TOST 等价检验 + bootstrap CI + 显式功效分析 + 多种子复制的组合在 NLP 论文中罕见。[R1, R2 共识]\n\n**S2.** 27 种 training-free 补救策略的系统测试是有价值的负面证据，independence-accuracy trade-off 的发现防止社区重复探索已证明无效的方向。[R1, R2 共识]\n\n**S3.** Observation 1（Argmax Preservation）将经验发现提升为可验证的形式化命题，推导在给定前提下正确。[R2 Soundness 4/5]\n\n**S4.** 诊断框架（C₀, K_eff, BR）从 K=12 pilot run 即可计算，具有实际应用价值。[R1, R2 共识]\n\n**S5.** 22 页附录的消融和敏感性分析展示了全面的 due diligence（prompt templates、case studies、per-subtype 分析、CV 直方图等），大幅增强可复现性。[R1, R2 共识]\n\n**S6.** Limitations 坦诚，Discussion 不过度声称——exploratory vs. confirmatory 的区分、统计功效不足的报告均体现良好学术诚信。[R1, R2 共识]\n\n**S7.** 跨架构 NLI escape 虽然初步，但提供了正确的研究方向（structural independence > model capability）。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [R1-N1 + R2 共识] Observation 1 在 SICA 的 source-attribution scoring 设计下近乎同义反复**\n- σ(c,a) 完全基于约束的来源 trace（provenance）而非逻辑内容。在 variable isolation 导致跨 trace 约束无法交叉引用的情况下（56.4% 跨答案约束对共享零个 Z3 变量），这一退化是 scoring 设计的直接后果而非关于 self-extraction 的 surprising discovery。\n- 论文未讨论基于内容的评分替代方案（如变量名规范化后用 Z3 检查逻辑蕴含），也未解释为何不可行。\n- 当前表述让读者误以为这是关于 self-extraction 范式的深层发现，但它高度依赖于 source-attribution scoring 这一特定设计选择。\n- **修改要求**: (1) 讨论 content-based scoring 替代方案并解释为何不可行（即使是负面结果也有价值）；(2) 讨论变量规范化/标准化是否能打破 variable isolation；(3) 调整 Observation 1 的 framing 以反映其对 SICA 设计的依赖性。\n\n**MF2. [R2-N1 + R1 共识] 核心发现新颖性有限——\"post-hoc self-extraction inherits generation bias\" 较可预期**\n- SCB 的核心机制（自提取约束来自产生答案的同一 trace，继承生成模型的分布先验）可从已有文献合理预期：Huang et al. (2024) 证明 LLM 无法通过自身反馈自纠正推理，Kamoi et al. (2024) 系统总结了 intrinsic self-correction 的失败模式。\n- Observation 1 的代数推导在给定条件下较为直接。真正有价值的是经验发现退化在实践中普遍发生（9 个模型、BR 1.66-4.97x），但这一贡献的定位不够清晰。\n- **修改要求**: (1) 更明确地与 Huang/Kamoi 区分——强调 SCB 的独特之处在于\"formal solver 也无法修复偏差\"这一更强结论；(2) 论证为什么社区之前没有预见到这个结果（如 SatLM/LogicLM 的成功是否给了社区错误的乐观预期）。\n\n**MF3. [R2-N2] Benchmark 范围过窄，claim 范围暗示 generality 但不支持**\n- 主要评估仅用 FOLIO (n=204) 和 ProofWriter (n=600)，两个相对小型的英文逻辑推理数据集。GSM8K/AIME 仅作退化区域探针（n≤30）。\n- Abstract/Introduction 的 claim 范围（\"natural extension...we show this is a symbolic mirage\"）暗示 generality，但实验仅覆盖模板化演绎推理。代码生成（约束=单元测试）、数学推理（更丰富约束语言）、非演绎推理等场景完全未涉及。\n- **修改要求**: (1) Abstract/Intro 限定 claim 为\"logical reasoning benchmarks under zero-shot extraction\"；(2) 增加至少一个非逻辑推理 benchmark 的完整评估，或在 Limitations 中更显著地讨论此限制。\n\n**MF4. [R1-N2 + R2-W1 共识] Cross-architecture escape 的 capability-gap pattern (n=6) 作为三大贡献之一证据不足**\n- ρ=1.0, p=0.003 仅基于 n=6 个 generator-verifier 对。6 个数据点的完美 Spearman 相关对微小扰动不稳健。虽标注为\"exploratory\"，但列为 Contribution 3 且在 Discussion 中推导 test-time compute scaling 的 implications。\n- 附录 W 扩展到 15 conditions（10 survive BH correction），但主文的 n=6 framing 过于突出。\n- **修改要求**: (1) 降级为 observation 而非 contribution；(2) 在主文中引用附录 W 的 15-condition 扩展；(3) 对基于 n=6 推导的 implications 加更多 hedging。\n\n### Should-Fix（影响评分）\n\n**SF1. [R1-W1] 结构独立性与外部监督信号的归因混淆**\n- NLI verifiers 均在 MultiNLI 上 fine-tuned，提供了外部监督信号。跨模型 LLM 投票（也具有结构独立性但无 NLI 训练信号）并不奏效。关键因素是 structural independence + task-relevant supervised signal 的组合，而非仅前者。Discussion 中\"without task-specific training\"的表述值得商榷（MultiNLI 与逻辑推理任务高度相关）。\n- **建议**: 明确 escape 需要两个条件。\n\n**SF2. [R1-W2] 统计功效不足以支撑等价性声明**\n- MDE 在 80% power 下为 4.6-4.8 pp，典型 |Δ| ≤ 2 pp。11 个条件中仅 4 个通过 TOST。\"no condition shows a significant positive effect\" 的 framing 可能暗示比统计证据支持的更强结论。\n- **建议**: 区分\"no significant effect detected\"与\"SICA is equivalent to SC\"。\n\n**SF3. [R1-W3] \"Symbolic Confirmation Bias\" 命名可能有误导性**\n- 论文自身的排列检验确认 BR 反映 trace-count geometry 而非 extraction bias。约束并非 actively biased，而是 not independently informative。\n- **建议**: 在首次引入术语时明确区分实际机制与认知确认偏见。\n\n**SF4. [R1-W4] Variable normalization 作为最直接修复方案未被测试**\n- 27 种策略中无一直接尝试变量名规范化。如果映射到统一命名空间，Z3 可进行跨 trace 约束推理。\n- **建议**: 讨论为何不可行或列为 future work。\n\n**SF5. [R2-W2 + R21-W6 复现] Related Work 缺少 test-time compute scaling 范式讨论**\n- 未涉及 o1/o3、DeepSeek-R1 通过内部推理链实现推理提升的范式转变。Discussion 提到 PRM 但仅一句，Related Work 缺失这条线。\n- **建议**: §2 增加 reasoning model 讨论。\n\n**SF6. [R2-W3] 约束提取质量过浅，可能限制结论适用性**\n- 99% 为命题级别，仅 1% 使用真量词。系统 prompt 限制约束为单一比较表达式。更丰富的约束语言是否会改变 SCB 未被讨论。\n- **建议**: 讨论约束浅层性是设计选择还是模型能力限制。\n\n**SF7. [R2-W4] 部分近期相关工作缺失**\n- \"Neurosymbolic Language Reasoning as SMT\" (2026)、\"Adaptive LLM-Symbolic Reasoning\" (EACL 2026)、DeepSeek-R1/o1/o3、PRM 文献在 Related Work 中的覆盖。\n\n**SF8. [R1-W5] Confirmatory vs exploratory 条件划分标准不透明**\n- m=6 confirmatory 条件的选择标准未在正文中明确说明。\n\n**SF9. [R2-W5] Observation 1 在\"近退化\"条件下的适用性 gap**\n- 精确退化与近退化之间的理论 gap 未被讨论。BR 从 1.0 到接近 1.0 的行为变化是连续的还是存在相变？\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成共识 [AGREE]：\n\n1. **核心 insight 可预测性较高**: R1 认为在理解 variable isolation 后 Observation 1 近乎同义反复；R2 认为 SCB 可从已有 self-correction failure 文献预期。两者角度不同但结论一致——核心发现的 surprising factor 有限。\n2. **n=6 capability-gap pattern 作为贡献不足**: 两位 Reviewer 一致认为应降级为 observation。\n3. **实验方法论高质量**: 统计方法的使用远超同类工作，值得推广。\n4. **27 种策略的负面证据有社区价值**。\n5. **Limitations 报告坦诚**。\n\n## Reviewer Divergence\n\n无重大分歧。两位 Reviewer 的关切互补而非矛盾：\n- R1 侧重方法论循环性（Observation 1 的设计依赖性、variable normalization 缺失）\n- R2 侧重外部效度（benchmark 范围、novelty 定位、related work 覆盖）\n\n---\n\n## Questions\n\n**Q1** [R2]: 如果用不同（可能更强）的模型做约束提取（而非自提取），但保持相同架构，SCB 是否改变？Table 2 显示跨架构 NLI 逃逸有效，但跨模型同架构的约束提取未被测试。\n\n**Q2** [R2]: 温度 T=0.7 用于所有实验。SCB 对温度有多敏感？Appendix L.2 仅在 Mistral-7B 上测试了温度敏感性。\n\n**Q3** [R2]: 诊断框架的阈值（BR>2, K_eff>1.30, ProcessSim>0.6）是否数据集依赖？是从评估数据本身导出的吗？\n\n**Q4** [R2]: 27 种补救策略是 27 种独立策略还是部分组合？\n\n**Q5** [R1]: Eq. 2 的 argmax over S 与 Algorithm 1 的 iterative soft-clause removal 是否存在全局最优性 gap？\n\n**Q6** [R1]: Eq. 1 中 K_eff 公式引用 Ladha (1992)，但具体公式形式是否来自 Ladha 原文？\n\n---\n\n## Missing References\n\n1. **Neurosymbolic Language Reasoning as Satisfiability Modulo Theory (2026)** — 直接使用 SMT 做 LLM+symbolic 推理，与 Z3 MAX-SAT 方案高度相关 [R2]\n2. **Adaptive LLM-Symbolic Reasoning via Dynamic Logical (EACL 2026)** — 自动选择符号语言的元提示框架 [R2]\n3. **DeepSeek-R1 (2025) / OpenAI o1/o3** — test-time reasoning scaling 代表工作，在 Related Work 中需更充分讨论 [R2]\n4. **Process Reward Models 文献** — Discussion 提到但 Related Work 未覆盖 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（0 critical, 2 warnings, 23 info）\n\n**关键发现**:\n- 主文 8 页，display items 分布合理：9 个 display items / 8 页 ≈ 1.1/页，密度优秀\n- Figure 1 在 page 2 顶部，Title-Abstract-Figure 1 讲同一个故事，一致性好\n- 所有表格使用 booktabs 风格，格式统一\n- 所有 float 出现在首次引用附近，无漂移\n- 颜色方案基本一致，公式渲染正确\n\n**Warnings**:\n1. Page 30（Appendix 末页，AI Assistants 声明）仅占约 25%，~75% 空白。建议合并到前一页\n2. Figure 7 (p.17, appendix) 信息密度极高，策略名称字号较小。建议确认 ≥ 7pt\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**置信度: 4/5** — 两位 Reviewer 均仔细阅读全文 30 页，熟悉 self-consistency、neuro-symbolic reasoning、统计检验方法和 ensemble diversity 文献。\n\n**评分依据**:\n\n这是一篇实验方法论严谨、统计分析全面的负面结果论文。核心贡献（SCB 的发现和形式化、27 种策略的系统排除、诊断框架）对 neuro-symbolic reasoning 社区有直接指导意义。\n\n然而，四个 Must-Fix 问题制约了当前版本的接收前景：\n\n1. **Observation 1 的论证循环性**（MF1）：核心理论贡献在 source-attribution scoring 设计下近乎同义反复，且未讨论内容基础评分替代方案，削弱了 intellectual contribution。\n\n2. **核心发现的新颖性**（MF2）：SCB 可从已有 self-correction failure 文献合理预期，论文需要更清晰地定位其独特贡献。\n\n3. **Benchmark 范围**（MF3）：claim 暗示 generality 但仅覆盖英文逻辑推理，需收窄 claim 或扩展评估。\n\n4. **n=6 capability-gap pattern**（MF4）：作为三大贡献之一证据不足，应降级。\n\n如果 MF1-MF4 得到充分解决（特别是 MF1 的内容基础评分讨论和 MF2 的 novelty 重新定位），论文有潜力达到 Conference (4.0) 水平。当前版本更适合 Findings (3.0-3.5)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"symbolic mirage\" 作为隐喻尚可但技术论文中略显随意，建议正式定义或改用更精确术语\n- Contribution 3 的 framing（\"Cross-architecture escape\"）应反映 n=6 的初步性质\n\n### §3 Method\n- Eq. 2 (MAX-SAT objective) 的 argmax formulation 与 Algorithm 1 的实际实现有微妙差异，建议在正文中注明\n- K_eff 公式（Eq. 1）对 Ladha (1992) 的引用准确性需确认\n\n### §4 Experiments\n- Table 1 caption 中 ≤2pp 灰色带的解读可能被误读为显著性而非等价性\n- Figure 2 中 circled points 标注\"significant (p < .05)\"但未标注是否经 BH 校正后仍然显著\n- 9 个模型的 BR 数据在 Table 2 中给出，但仅 6 个模型有完整 SICA 精度对比。Abstract 中\"nine models\"表述准确（指 BR）但可能引起误解\n\n### §5 Analysis\n- §5.1 首次引入 SCB 术语时应明确区分实际机制（trace-count geometry）与认知确认偏见\n- §5.2 应增加对 variable normalization/canonicalization 的讨论\n- §5.4 应明确 escape 需要 structural independence + task-relevant capability 两个条件\n\n### §6 Discussion\n- \"our NLI escape instantiates this principle without task-specific training\" 需修正——MultiNLI 与逻辑推理任务高度相关\n- 基于 n=6 pattern 推导的 test-time compute implications 需更多 hedging\n\n### Limitations\n- 内容坦诚，覆盖了关键限制（模型规模、英文、逻辑推理、indirect controls）\n- 建议增加：benchmark 范围限制对 claim generality 的影响",
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 23 审稿报告（Fresh Review）\n\n**项目**: symb_invariant_consensus\n**Venue**: EMNLP 2026 (ARR)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+Related Work）\n**圆桌轮次**: 1 轮（两位 Reviewer 独立初审 + 交叉分享后达成共识，无需额外轮次）\n\n---\n\n## Summary\n\n本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM chain-of-thought traces 中提取 FOL 约束并用 Z3 求解 weighted partial MAX-SAT 以选答案。核心发现为负面结果：自提取约束系统性地确认多数投票结果（symbolic confirmation bias, SCB），SICA 在退化条件下归约为多数投票。论文在 9 个模型（7B 到 frontier）、4 个 benchmark 上验证了这一现象，测试了 27 种 training-free 补救策略均失败，提出三项诊断指标（C₀, K_eff, BR），并展示跨架构 NLI verifier 可部分突破瓶颈。\n\n---\n\n## Strengths\n\n**S1.** 实验方法论的高标准远超同类工作——McNemar 检验 + Benjamini-Hochberg 校正 + TOST 等价检验 + bootstrap CI + 显式功效分析 + 多种子复制的组合在 NLP 论文中罕见。[R1, R2 共识]\n\n**S2.** 27 种 training-free 补救策略的系统测试是有价值的负面证据，independence-accuracy trade-off 的发现防止社区重复探索已证明无效的方向。[R1, R2 共识]\n\n**S3.** Observation 1（Argmax Preservation）将经验发现提升为可验证的形式化命题，推导在给定前提下正确。[R2 Soundness 4/5]\n\n**S4.** 诊断框架（C₀, K_eff, BR）从 K=12 pilot run 即可计算，具有实际应用价值。[R1, R2 共识]\n\n**S5.** 22 页附录的消融和敏感性分析展示了全面的 due diligence（prompt templates、case studies、per-subtype 分析、CV 直方图等），大幅增强可复现性。[R1, R2 共识]\n\n**S6.** Limitations 坦诚，Discussion 不过度声称——exploratory vs. confirmatory 的区分、统计功效不足的报告均体现良好学术诚信。[R1, R2 共识]\n\n**S7.** 跨架构 NLI escape 虽然初步，但提供了正确的研究方向（structural independence > model capability）。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [R1-N1 + R2 共识] Observation 1 在 SICA 的 source-attribution scoring 设计下近乎同义反复**\n- σ(c,a) 完全基于约束的来源 trace（provenance）而非逻辑内容。在 variable isolation 导致跨 trace 约束无法交叉引用的情况下（56.4% 跨答案约束对共享零个 Z3 变量），这一退化是 scoring 设计的直接后果而非关于 self-extraction 的 surprising discovery。\n- 论文未讨论基于内容的评分替代方案（如变量名规范化后用 Z3 检查逻辑蕴含），也未解释为何不可行。\n- 当前表述让读者误以为这是关于 self-extraction 范式的深层发现，但它高度依赖于 source-attribution scoring 这一特定设计选择。\n- **修改要求**: (1) 讨论 content-based scoring 替代方案并解释为何不可行（即使是负面结果也有价值）；(2) 讨论变量规范化/标准化是否能打破 variable isolation；(3) 调整 Observation 1 的 framing 以反映其对 SICA 设计的依赖性。\n\n**MF2. [R2-N1 + R1 共识] 核心发现新颖性有限——\"post-hoc self-extraction inherits generation bias\" 较可预期**\n- SCB 的核心机制（自提取约束来自产生答案的同一 trace，继承生成模型的分布先验）可从已有文献合理预期：Huang et al. (2024) 证明 LLM 无法通过自身反馈自纠正推理，Kamoi et al. (2024) 系统总结了 intrinsic self-correction 的失败模式。\n- Observation 1 的代数推导在给定条件下较为直接。真正有价值的是经验发现退化在实践中普遍发生（9 个模型、BR 1.66-4.97x），但这一贡献的定位不够清晰。\n- **修改要求**: (1) 更明确地与 Huang/Kamoi 区分——强调 SCB 的独特之处在于\"formal solver 也无法修复偏差\"这一更强结论；(2) 论证为什么社区之前没有预见到这个结果（如 SatLM/LogicLM 的成功是否给了社区错误的乐观预期）。\n\n**MF3. [R2-N2] Benchmark 范围过窄，claim 范围暗示 generality 但不支持**\n- 主要评估仅用 FOLIO (n=204) 和 ProofWriter (n=600)，两个相对小型的英文逻辑推理数据集。GSM8K/AIME 仅作退化区域探针（n≤30）。\n- Abstract/Introduction 的 claim 范围（\"natural extension...we show this is a symbolic mirage\"）暗示 generality，但实验仅覆盖模板化演绎推理。代码生成（约束=单元测试）、数学推理（更丰富约束语言）、非演绎推理等场景完全未涉及。\n- **修改要求**: (1) Abstract/Intro 限定 claim 为\"logical reasoning benchmarks under zero-shot extraction\"；(2) 增加至少一个非逻辑推理 benchmark 的完整评估，或在 Limitations 中更显著地讨论此限制。\n\n**MF4. [R1-N2 + R2-W1 共识] Cross-architecture escape 的 capability-gap pattern (n=6) 作为三大贡献之一证据不足**\n- ρ=1.0, p=0.003 仅基于 n=6 个 generator-verifier 对。6 个数据点的完美 Spearman 相关对微小扰动不稳健。虽标注为\"exploratory\"，但列为 Contribution 3 且在 Discussion 中推导 test-time compute scaling 的 implications。\n- 附录 W 扩展到 15 conditions（10 survive BH correction），但主文的 n=6 framing 过于突出。\n- **修改要求**: (1) 降级为 observation 而非 contribution；(2) 在主文中引用附录 W 的 15-condition 扩展；(3) 对基于 n=6 推导的 implications 加更多 hedging。\n\n### Should-Fix（影响评分）\n\n**SF1. [R1-W1] 结构独立性与外部监督信号的归因混淆**\n- NLI verifiers 均在 MultiNLI 上 fine-tuned，提供了外部监督信号。跨模型 LLM 投票（也具有结构独立性但无 NLI 训练信号）并不奏效。关键因素是 structural independence + task-relevant supervised signal 的组合，而非仅前者。Discussion 中\"without task-specific training\"的表述值得商榷（MultiNLI 与逻辑推理任务高度相关）。\n- **建议**: 明确 escape 需要两个条件。\n\n**SF2. [R1-W2] 统计功效不足以支撑等价性声明**\n- MDE 在 80% power 下为 4.6-4.8 pp，典型 |Δ| ≤ 2 pp。11 个条件中仅 4 个通过 TOST。\"no condition shows a significant positive effect\" 的 framing 可能暗示比统计证据支持的更强结论。\n- **建议**: 区分\"no significant effect detected\"与\"SICA is equivalent to SC\"。\n\n**SF3. [R1-W3] \"Symbolic Confirmation Bias\" 命名可能有误导性**\n- 论文自身的排列检验确认 BR 反映 trace-count geometry 而非 extraction bias。约束并非 actively biased，而是 not independently informative。\n- **建议**: 在首次引入术语时明确区分实际机制与认知确认偏见。\n\n**SF4. [R1-W4] Variable normalization 作为最直接修复方案未被测试**\n- 27 种策略中无一直接尝试变量名规范化。如果映射到统一命名空间，Z3 可进行跨 trace 约束推理。\n- **建议**: 讨论为何不可行或列为 future work。\n\n**SF5. [R2-W2 + R21-W6 复现] Related Work 缺少 test-time compute scaling 范式讨论**\n- 未涉及 o1/o3、DeepSeek-R1 通过内部推理链实现推理提升的范式转变。Discussion 提到 PRM 但仅一句，Related Work 缺失这条线。\n- **建议**: §2 增加 reasoning model 讨论。\n\n**SF6. [R2-W3] 约束提取质量过浅，可能限制结论适用性**\n- 99% 为命题级别，仅 1% 使用真量词。系统 prompt 限制约束为单一比较表达式。更丰富的约束语言是否会改变 SCB 未被讨论。\n- **建议**: 讨论约束浅层性是设计选择还是模型能力限制。\n\n**SF7. [R2-W4] 部分近期相关工作缺失**\n- \"Neurosymbolic Language Reasoning as SMT\" (2026)、\"Adaptive LLM-Symbolic Reasoning\" (EACL 2026)、DeepSeek-R1/o1/o3、PRM 文献在 Related Work 中的覆盖。\n\n**SF8. [R1-W5] Confirmatory vs exploratory 条件划分标准不透明**\n- m=6 confirmatory 条件的选择标准未在正文中明确说明。\n\n**SF9. [R2-W5] Observation 1 在\"近退化\"条件下的适用性 gap**\n- 精确退化与近退化之间的理论 gap 未被讨论。BR 从 1.0 到接近 1.0 的行为变化是连续的还是存在相变？\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成共识 [AGREE]：\n\n1. **核心 insight 可预测性较高**: R1 认为在理解 variable isolation 后 Observation 1 近乎同义反复；R2 认为 SCB 可从已有 self-correction failure 文献预期。两者角度不同但结论一致——核心发现的 surprising factor 有限。\n2. **n=6 capability-gap pattern 作为贡献不足**: 两位 Reviewer 一致认为应降级为 observation。\n3. **实验方法论高质量**: 统计方法的使用远超同类工作，值得推广。\n4. **27 种策略的负面证据有社区价值**。\n5. **Limitations 报告坦诚**。\n\n## Reviewer Divergence\n\n无重大分歧。两位 Reviewer 的关切互补而非矛盾：\n- R1 侧重方法论循环性（Observation 1 的设计依赖性、variable normalization 缺失）\n- R2 侧重外部效度（benchmark 范围、novelty 定位、related work 覆盖）\n\n---\n\n## Questions\n\n**Q1** [R2]: 如果用不同（可能更强）的模型做约束提取（而非自提取），但保持相同架构，SCB 是否改变？Table 2 显示跨架构 NLI 逃逸有效，但跨模型同架构的约束提取未被测试。\n\n**Q2** [R2]: 温度 T=0.7 用于所有实验。SCB 对温度有多敏感？Appendix L.2 仅在 Mistral-7B 上测试了温度敏感性。\n\n**Q3** [R2]: 诊断框架的阈值（BR>2, K_eff>1.30, ProcessSim>0.6）是否数据集依赖？是从评估数据本身导出的吗？\n\n**Q4** [R2]: 27 种补救策略是 27 种独立策略还是部分组合？\n\n**Q5** [R1]: Eq. 2 的 argmax over S 与 Algorithm 1 的 iterative soft-clause removal 是否存在全局最优性 gap？\n\n**Q6** [R1]: Eq. 1 中 K_eff 公式引用 Ladha (1992)，但具体公式形式是否来自 Ladha 原文？\n\n---\n\n## Missing References\n\n1. **Neurosymbolic Language Reasoning as Satisfiability Modulo Theory (2026)** — 直接使用 SMT 做 LLM+symbolic 推理，与 Z3 MAX-SAT 方案高度相关 [R2]\n2. **Adaptive LLM-Symbolic Reasoning via Dynamic Logical (EACL 2026)** — 自动选择符号语言的元提示框架 [R2]\n3. **DeepSeek-R1 (2025) / OpenAI o1/o3** — test-time reasoning scaling 代表工作，在 Related Work 中需更充分讨论 [R2]\n4. **Process Reward Models 文献** — Discussion 提到但 Related Work 未覆盖 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（0 critical, 2 warnings, 23 info）\n\n**关键发现**:\n- 主文 8 页，display items 分布合理：9 个 display items / 8 页 ≈ 1.1/页，密度优秀\n- Figure 1 在 page 2 顶部，Title-Abstract-Figure 1 讲同一个故事，一致性好\n- 所有表格使用 booktabs 风格，格式统一\n- 所有 float 出现在首次引用附近，无漂移\n- 颜色方案基本一致，公式渲染正确\n\n**Warnings**:\n1. Page 30（Appendix 末页，AI Assistants 声明）仅占约 25%，~75% 空白。建议合并到前一页\n2. Figure 7 (p.17, appendix) 信息密度极高，策略名称字号较小。建议确认 ≥ 7pt\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**置信度: 4/5** — 两位 Reviewer 均仔细阅读全文 30 页，熟悉 self-consistency、neuro-symbolic reasoning、统计检验方法和 ensemble diversity 文献。\n\n**评分依据**:\n\n这是一篇实验方法论严谨、统计分析全面的负面结果论文。核心贡献（SCB 的发现和形式化、27 种策略的系统排除、诊断框架）对 neuro-symbolic reasoning 社区有直接指导意义。\n\n然而，四个 Must-Fix 问题制约了当前版本的接收前景：\n\n1. **Observation 1 的论证循环性**（MF1）：核心理论贡献在 source-attribution scoring 设计下近乎同义反复，且未讨论内容基础评分替代方案，削弱了 intellectual contribution。\n\n2. **核心发现的新颖性**（MF2）：SCB 可从已有 self-correction failure 文献合理预期，论文需要更清晰地定位其独特贡献。\n\n3. **Benchmark 范围**（MF3）：claim 暗示 generality 但仅覆盖英文逻辑推理，需收窄 claim 或扩展评估。\n\n4. **n=6 capability-gap pattern**（MF4）：作为三大贡献之一证据不足，应降级。\n\n如果 MF1-MF4 得到充分解决（特别是 MF1 的内容基础评分讨论和 MF2 的 novelty 重新定位），论文有潜力达到 Conference (4.0) 水平。当前版本更适合 Findings (3.0-3.5)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"symbolic mirage\" 作为隐喻尚可但技术论文中略显随意，建议正式定义或改用更精确术语\n- Contribution 3 的 framing（\"Cross-architecture escape\"）应反映 n=6 的初步性质\n\n### §3 Method\n- Eq. 2 (MAX-SAT objective) 的 argmax formulation 与 Algorithm 1 的实际实现有微妙差异，建议在正文中注明\n- K_eff 公式（Eq. 1）对 Ladha (1992) 的引用准确性需确认\n\n### §4 Experiments\n- Table 1 caption 中 ≤2pp 灰色带的解读可能被误读为显著性而非等价性\n- Figure 2 中 circled points 标注\"significant (p < .05)\"但未标注是否经 BH 校正后仍然显著\n- 9 个模型的 BR 数据在 Table 2 中给出，但仅 6 个模型有完整 SICA 精度对比。Abstract 中\"nine models\"表述准确（指 BR）但可能引起误解\n\n### §5 Analysis\n- §5.1 首次引入 SCB 术语时应明确区分实际机制（trace-count geometry）与认知确认偏见\n- §5.2 应增加对 variable normalization/canonicalization 的讨论\n- §5.4 应明确 escape 需要 structural independence + task-relevant capability 两个条件\n\n### §6 Discussion\n- \"our NLI escape instantiates this principle without task-specific training\" 需修正——MultiNLI 与逻辑推理任务高度相关\n- 基于 n=6 pattern 推导的 test-time compute implications 需更多 hedging\n\n### Limitations\n- 内容坦诚，覆盖了关键限制（模型规模、英文、逻辑推理、indirect controls）\n- 建议增加：benchmark 范围限制对 claim generality 的影响",
    "project": "symb_invariant_consensus",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 2563 · 2026-05-25T21:31:11.641982+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4420
}
```

</details>

---


### Assistant

_source line 2564 · 2026-05-25T21:31:20.275943+00:00_

审稿报告已投递。

**Round 23 审稿完成**：

- **Overall: 3.5 — Borderline Conference**
- **4 个 Must-Fix**: Observation 1 论证循环性、核心发现新颖性有限、Benchmark 范围过窄、n=6 capability-gap 作为贡献不足
- **9 个 Should-Fix**: 结构独立性归因混淆、统计功效不足、SCB 命名误导、variable normalization 缺失、test-time scaling 讨论缺失、约束提取过浅、近期相关工作缺失、confirmatory/exploratory 划分不透明、近退化适用性 gap
- **视觉审查**: 已完成，排版质量良好（0 critical, 2 minor warnings）
- **Issue Tracker**: 已同步更新（新增 10 个 open issues）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 183

## Round 183

4 recorded events


### User

_source line 2565 · 2026-05-25T21:31:20.285228+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### R1-N1: Observation 1 在 SICA 设计选择下近乎同义反复

**[AGREE]** R1 的技术论证成立且比我的 N1 更精准。

R1 指出 source-attribution scoring σ(c,a)=1 iff c 来自产生 a 的 trace 是**设计选择**，而非关于 self-extraction 的发现。结合 §5.2 报告的 variable isolation（56.4% 的跨答案约束共享零个 Z3 变量），退化是这一评分设计在变量隔离条件下的直接代数后果。

我对论文的补充观察：

1. §3 (p.3, Eq. 2) 的 deduplication 规则按 "syntactic equivalence (global average deduplication ratio: 46.0%)" 去重，但未按**语义等价**去重。两条来自不同 trace 的约束可能语义相同但变量名不同（如 `x > 0` vs `y > 0` 表达同一实体），Z3 将它们视为独立命题。这进一步强化了 R1 的论点——不是 extraction 有偏差，而是 scoring+dedup 机制无法跨 trace 聚合语义等价的约束。

2. 论文在 §5.2 自己承认 "The root cause is variable isolation"，但 Observation 1 在 §5.1 的定位仍然是 "self-extracted constraints systematically align with the model's majority answer" 这一听起来更广泛的结论。建议重新定位为：**在当前 provenance-based scoring 下，变量隔离导致 SICA 退化为多数投票**——并明确讨论 content-based scoring 替代方案（如基于约束语义嵌入的跨 trace 匹配）为何未被采用或不可行。

3. 但 R1 说"近乎同义反复"略有过度——Observation 1 的经验贡献在于证明退化条件**在实践中普遍成立**（Table 2: 所有 9 个模型的 BR ≈ 1，Δ(pp) 范围 -1.05 到 +0.00），这不是从设计可直接推出的（理论上约束 COULD 跨 trace 共享变量）。

**结论**：同意论文需要 (a) 将 Observation 1 明确限定为 SICA 特定设计的分析结论，(b) 讨论 content-based scoring 替代方案。

---

### R1-N2: Cross-architecture escape 的 capability-gap pattern 基于 n=6

**[AGREE]** 完全同意。

Table 3 (p.7) 展示 3 个 NLI 架构 × 若干 generator 条件。Figure 5 (p.8) 的 Spearman ρ=1.0 基于 n=6 generator-verifier 对。无论 p=0.003 多显著，n=6 的完美 rank correlation 对任何单点扰动都不稳健——移除任一数据点后 ρ 可能大幅下降。

论文将 cross-architecture escape 列为三大贡献之一（§1, p.1: "cross-architecture verification escapes the bottleneck"），但证据强度与 claim 强度不匹配。我的审稿意见 W1 也指出了这一不对称（负面发现: 9 模型 × 4 benchmark 的全面实验 vs. 正面发现: 3 NLI 架构 × 1 dataset）。

建议：降级为 "preliminary observation" 而非 "contribution"，或补充更多 generator-verifier 对（如在 FOLIO 上重复实验）。

---

### R1-W1: 结构独立性与外部监督信号的混淆

**[AGREE]** R1 的论证有力且我在初审中未充分识别。

关键反事实证据在 Appendix O (p.20)——cross-model confirmation bias 分析显示 Mistral-7B 从其他模型 trace 提取 FOL 仍然展现 SCB。这意味着**跨模型 LLM 约束提取**（具有结构独立性但无 NLI 监督信号）不能打破瓶颈。同时 NLI verifier（结构独立性 + MultiNLI fine-tuning）能打破瓶颈。

这直接挑战了论文 §5.4 的结论 "structural independence, not model-specific properties, drives the effect"。更准确的归因应该是 **structural independence + task-relevant supervised signal** 的组合。NLI verifier 不仅架构不同，更关键的是它们在 NLI 任务上有独立的监督训练信号，这提供了真正独立于 generator 的判断依据。

论文应当设计一个控制实验来分离这两个因素——例如用未经 NLI fine-tuning 的 DeBERTa base 做 verifier，看是否仍有 escape 效果。

---

### R1-W2: 统计功效不足以支撑等价性声明

**[AGREE]**，但补充 bootstrap CI 提供了部分缓解。

R1 正确指出 MDE = 4.6-4.8pp（Table 6, Appendix D, p.14）而 typical |Δ| ≤ 2pp，意味着实验无法可靠检测 2pp 的正面效应。11 个条件中仅 4 个通过 TOST 等价检验。

但论文还报告了 bootstrap 95% CI（Table 7, Appendix E, p.14）——所有三个 confirmatory 条件的 CI 均包含零，最宽区间为 LLaMA-8B FOLIO [-5.88, +0.98]。虽然 CI 宽度本身反映了功效不足，但所有 CI 的上界均 < 1pp（最有利条件 Qwen2.5-14B 为 [-1.12, +1.62]），这限制了可能被遗漏的正面效应的大小。

**建议**：论文应将 "no condition shows a significant positive effect" 改为更审慎的表述，如 "we find no evidence of positive effect, though our power to detect effects below ~4.6pp is limited; bootstrap CIs are consistent with effects between -5.9pp and +1.6pp"。

---

### R1-W3: "Symbolic Confirmation Bias" 命名可能有误导性

**[AGREE]** R1 的分析精确。

论文自己的排列检验（§5.1, "A permutation test confirms BR reflects trace-count geometry, not extraction bias"）已经承认 BR 反映的是 trace-count 几何而非提取偏差。§5.2 进一步确认根本原因是 variable isolation 导致约束无法跨 trace 交互——约束并非 actively biased toward the majority answer，而是 structurally non-independent from the traces that produced them。

"Confirmation bias" 在认知科学中指**主动偏向已有信念的倾向**（积极寻找确认性证据、忽略反驳性证据）。但论文描述的现象更接近**信息冗余**：约束没有提供超越 trace 来源的独立信息。"Symbolic redundancy" 或 "symbolic non-independence" 确实更准确地描述了这一机制。

不过我理解作者选择 "confirmation bias" 的修辞动机——它更 catchy 且直觉上传达了 "约束确认已有答案" 的核心现象。建议在正文中更明确地区分现象（constraints confirm the majority）和机制（non-independence/redundancy），避免暗示约束存在主动偏向。

---

### R1-W4: Variable isolation 的最直接修复（变量规范化）未被测试

**[AGREE]** 这是 27 种补救策略中最显眼的缺失。

论文在 §5.2 (p.7) 明确诊断 "The root cause is variable isolation: each trace generates constraints with its own variable names; Z3 treats identically-intended propositions from different traces as unrelated symbols." Appendix K (p.17) 进一步量化了这一问题——56.4% 的跨答案约束共享零个 Z3 变量。

既然变量隔离被确认为根本原因，最直接的修复应该是**跨 trace 变量名规范化**——将所有 trace 的变量映射到统一命名空间（例如通过 prompt 指定固定变量名方案，或通过 LLM 后处理进行变量对齐）。Figure 7 (p.17) 列出的 27 种策略中没有一种直接尝试这一方向。

我理解变量规范化并非 trivial——不同 trace 可能对同一实体使用不同概念化（如 "is_mammal(x)" vs "animal_type(x)='mammal'"），语义对齐本身需要额外推理。但至少应该测试**最简单的版本**：在提取 prompt 中强制指定固定变量名方案（如 "use variable names x1, x2, ... for entities in the order they appear"）。这比论文测试的许多策略（如 contrastive prompting、multi-temperature）更直接地针对已确认的根本原因。

---

### R1-W5: Confirmatory vs. exploratory 条件的划分标准不够清晰

**[AGREE]** 论文确实未在正文中清晰说明 m=6 confirmatory 条件的选择标准。

Appendix D (Table 6, p.14) 提到 "grouped conditions with n ≥ 200"，从 Table 1 的 8 个条件中排除了 n 较小的条件。但：
1. n ≥ 200 的阈值来源不明——为什么不是 n ≥ 100 或 n ≥ 300？
2. 主文 §4.2 (p.5) 说 "Two confirmatory conditions show significant degradation after Benjamin-Hochberg (BH) FDR control"，但未列出哪些条件是 confirmatory set。
3. 这种选择在 power analysis 之前还是之后做出的？如果先看了结果再划分 confirmatory/exploratory，存在 post-hoc rationalization 风险。

建议在正文中明确：(1) confirmatory 条件的精确列表，(2) 划分标准及其理由，(3) 划分是否在看到结果之前预注册。

---

### 综合评估

R1 的审稿意见整体质量高，技术深度超过我的初审。特别是 N1（Observation 1 的设计依赖性）和 W1（结构独立性 vs 监督信号混淆）是我未充分识别的重要问题。这两个问题共同指向论文在因果归因上的不精确——将设计选择的后果归因为范式性发现，将组合效应归因为单一因素。

基于 R1 的意见，我维持我的总体评分 **3.5 (Borderline Conference)**，但对 Soundness 的评分从 4 下调至 **3.5/5**——N1 和 W1 揭示的因果归因问题属于方法论不足（Observation 1 的 claim 范围过宽、cross-architecture escape 的因果分离不充分），影响了论文核心结论的可信度。

修订后的打分：
| 维度 | 分数 | 变化原因 |
|------|------|----------|
| Soundness | 3.5/5 | R1-N1 揭示 Observation 1 的设计依赖性 + R1-W1 的因果混淆 |
| Excitement | 3/5 | 不变 |
| Overall | 3.5 | 不变，但 Soundness 下调使得 borderline 偏下 |


---

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### N1: 核心发现新颖性有限——"post-hoc extraction inherits bias" 较为可预期

[AGREE] R2-Issue-N1（部分同意，但对"证据不足以支撑接收"的隐含结论持保留）

R2 指出 Observation 1 的代数推导在给定前提下较为直接，这与我自己的 N1 一致（我认为 Observation 1 在 SICA 的 source-attribution scoring 设计下近乎同义反复）。R2 正确引用了 Huang et al. (2024) 和 Kamoi et al. (2024) 作为先验知识。

但我认为 R2 低估了三个方面的贡献：
1. **机制的具体化**：论文提供了 M→T→(A,C) 因果结构（Figure 3）和 variable isolation 的具体机制（§5.2: "56.4% share zero Z3 variables"），这比 Huang et al. 的一般性结论 "LLMs cannot self-correct" 更有操作意义。论文 Related Work §2 明确讨论了与这些工作的关系，并指出 SCB 与 CoT-level confirmation bias (Turpin et al. 2023, Wan et al. 2025) 机制不同。
2. **经验广度**：9 个模型 × 4 个基准 × 27 种修复策略的系统性覆盖在该子领域无先例。
3. **实用诊断工具**：C₀/K_eff/BR 三诊断指标（§5.3）是直接可用的实践指导，这超越了"发现问题"的层面。

R2 说 "真正有价值的是经验发现…但这一贡献的定位不够清晰" ——我同意这个 repositioning 建议。论文应将重心从理论贡献（Observation 1）转向经验发现和诊断框架。

ARR reviewer guidelines (H1) 明确指出 "results appearing obvious retrospectively doesn't mean the community already knows them empirically"。在 neuro-symbolic reasoning 文献中，LogicLM (Pan et al. 2023)、LINC (Olausson et al. 2023)、SatLM (Ye et al. 2024) 均假设形式化约束提供独立信号——本文的系统性反证有发表价值。

**结论**：同意 framing 需要调整，但不同意贡献不足以支撑发表。

---

### N2: Benchmark 范围过窄，generalizability 存疑

[AGREE] R2-Issue-N2（部分同意，但认为 critical 定级过高）

R2 指出主要评估集中在 FOLIO 和 ProofWriter（模板化逻辑推理），这是事实。但有几个缓解因素：

1. **Best-case argument**：论文 Limitations 明确指出 "FOLIO and ProofWriter represent a best-case for symbolic verification, and the observed bias ratios likely represent a lower bound on SCB in less structured domains." 如果在约束提取最自然的任务上都失败，在结构化更弱的任务上更不可能成功。
2. **已有额外覆盖**：StrategyQA (n=200) 和 LogiQA (n=200) 不是模板化逻辑推理——StrategyQA 是开放域常识推理，LogiQA 是考试题。GSM8K/AIME 是数学推理（虽然 C₀ < 5% 导致退化）。
3. **Variable isolation 的普遍性**：§5.2 识别的根本原因（不同 trace 使用不同变量名）不依赖于特定 benchmark——只要 LLM 以自然语言思考然后提取形式约束，这一问题就存在。

但我同意 R2 提出的两个重要场景确实未被覆盖：
- **代码生成**（约束 = 单元测试）：这是一个根本不同的范式，单元测试可以被执行而非仅做可满足性检查，可能不受 variable isolation 影响。
- **数学推理**（更丰富的约束语言）：GSM8K 仅 n=30 且 C₀ < 5%，不足以评估 SCB 在数学场景的表现。

**结论**：benchmark 范围确实有限，但 best-case argument 和 variable isolation 的普遍性部分缓解了这一问题。建议降级为 should-fix。

---

### W1: 跨架构逃逸的正面贡献与负面发现不对称

[AGREE] R2-Issue-W1

完全同意。这与我自己的 N2 高度一致。负面发现有 9 模型 × 4 benchmark 支撑，但正面 escape 主要基于 ProofWriter (n=600) 上的 3 个 NLI 架构，且 capability-gap pattern 仅 n=6 数据点（ρ=1.0, p=0.003）。

补充一个 R2 未提及的具体问题：Table 3 (§5.4) 显示 combo gain 随 generator capability 单调递减（Mistral-7B: +6.67 pp → Qwen3-14B: +0.50 pp）。对于 frontier 模型（SC ≥ 85%），NLI combo 几乎无意义。论文在 §5.4 末尾承认 "Fine-tuning extends gains to generators with SC up to ~72%"——但这意味着 escape 仅对弱到中等模型有效，进一步限制了其实用价值。

论文的 Discussion 中基于这 n=6 pattern 推导 test-time compute scaling 的 implications 显得过于冒进。

---

### W2: Related Work 缺少 test-time compute scaling 范式讨论

[REBUT] R2-Issue-W2

R2 的这一批评部分不准确。查看 Related Work §2 的 "Verification and test-time scaling" 段落：
- **DeepSeek-R1**：已引用 "extended reasoning (Guo et al., 2025)" 即 DeepSeek-R1 论文
- **QwQ**：已引用 "(Qwen Team, 2024)"
- **o3**：Table 2 (§5.1) 实际测试了 o3 的 SCB（BR=1.66），且在 experiments §4.1 明确列出
- **PRM**：Related Work §2 引用了 Lightman et al. 2024, Wang et al. 2024 (Math-Shepherd), Cobbe et al. 2021
- **RL-based self-verification**：引用了 Zeng et al. 2025 (S2R)

论文还在 Related Work 末尾对比了 SICA 和 PRM/ORM 的 failure modes："SICA's bottleneck is extraction fidelity, whereas PRM/ORM's is reward model generalization."

R2 可能期望更深入的 paradigm-level 讨论（为什么 o1/R1 的 learned verification 成功而 self-extraction 失败），这确实可以加强论文。但 "缺失" 的定性不准确——这些工作已被引用和讨论。

---

### W3: 约束提取质量过浅，可能限制了结论的适用性

[AGREE] R2-Issue-W3（部分同意）

R2 正确指出 99.0% 的约束为命题级别（§3, method.tex L55），且 extraction prompt 限制 z3_formula 为单一比较表达式（Appendix A, 数学 prompt 的 "each z3_formula must be exactly ONE comparison"）。这是一个合理的设计关注。

但我认为更丰富的约束语言**不太可能**改变核心结论，原因是：
1. **Variable isolation 不依赖于约束复杂度**：即使提取带量词的一阶逻辑约束，每个 trace 仍使用自己的变量名。更复杂的约束反而可能加剧 variable isolation（更多变量 → 更难跨 trace 对齐）。
2. **经验证据**：逻辑 prompt（Appendix A）允许 Implies, And, Or, Not 等复杂操作符，不限制为单一比较。只有数学 prompt 有 "exactly ONE comparison" 限制。FOLIO 上的约束使用了 Implies 和 And 等复合结构，仍然表现出 SCB。
3. **Z3 rejection rate 极低**（3.4%），说明即使是复合约束也几乎都通过了可满足性检查——这正是退化的核心。

不过，R2 提出了一个论文应当讨论的 interesting question：如果约束被设计为**跨 trace 可比较的**格式（如统一本体），SCB 是否会改变？这与我自己的 W4（variable normalization）一致。

---

### W4: 部分近期相关工作缺失

[REBUT] R2-Issue-W4（部分反驳）

逐条检查：
- **DeepSeek-R1/o1/o3**：如上 W2 回应所述，DeepSeek-R1 (Guo et al., 2025)、QwQ、o3 均已被引用或测试。
- **Process Reward Models**：Related Work §2 已引用 Lightman et al. 2024, Wang et al. 2024, Cobbe et al. 2021。
- **"Neurosymbolic Language Reasoning as Satisfiability Modulo Theory" (2026)**：无法验证此引用是否真实存在。如果存在，应当补充。
- **"Adaptive LLM-Symbolic Reasoning via Dynamic Logical" (EACL 2026)**：Related Work §2 已引用 "Xu et al. 2026 (DyLoS)"，标题为 "Adaptive LLM-Symbolic reasoning via dynamic logical solver construction"——这很可能就是 R2 所指的论文。如果是同一篇，则 R2 的批评不成立。

**结论**：R2 列出的 4 类缺失引用中，至少 3 类已被覆盖。建议 R2 核实后再确认。

---

### W5: Observation 1 在 "近退化" 条件下的适用性

[AGREE] R2-Issue-W5

这是一个有价值的理论问题。Observation 1 形式化了 |C\| ≈ 0 的精确退化，但实际条件是连续的。论文提供了部分经验证据但未做形式化分析：

1. **三区域分类**（§5.3, Figure 2）显示 SICA Δ 与 SC 基线的关系呈现三段结构（Type C / intermediate / Type A），暗示**非相变**的连续过渡。
2. **Entropy decomposition**（Appendix M）显示低熵问题（majority ≥ 9/12）上 Δ ≈ 0 pp，高熵问题上效应方向取决于 SC regime——这提供了连续性的经验证据。
3. **α 消融**（Table 11, p.16）显示 SICA 与 count-only aggregation 在 ≥ 99% 问题上一致，BR 从 4.97（自提取）到 ~1.0（近退化边界）是连续的。

但 R2 正确指出论文缺少对**过渡区间行为**的形式化刻画。在 intermediate regime (SC 50-60%) 中，SICA 显示正向趋势但不显著——这恰好是 "近退化" 的有趣区域。是否存在某个 |C\|/|C| 阈值，超过该阈值 SICA 开始提供真正的纠错信号？这个问题值得在 Discussion 或 Appendix 中讨论。


---

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **N1 [AGREE]**: Observation 1 的退化确实依赖于 provenance-based scoring 的设计选择 + 变量隔离，但经验发现退化普遍成立仍有增量贡献。建议重新限定 claim 范围。
- **N2 [AGREE]**: n=6 的完美 Spearman 相关不稳健，正面贡献的证据强度不足。
- **W1 [AGREE]**: NLI escape 可能由 structural independence + supervised signal 共同驱动，Appendix O 的跨模型 LLM 实验支持这一判断。
- **W2 [AGREE]**: 功效不足，但 bootstrap CI 提供部分缓解。建议更审慎的表述。
- **W3 [AGREE]**: "confirmation bias" 暗示主动偏向，实际机制更接近 non-independence/redundancy。
- **W4 [AGREE]**: 变量规范化是最直接针对根本原因的修复方案，27 种策略中缺失。
- **W5 [AGREE]**: confirmatory 条件划分标准需要在正文中明确说明。

基于 R1 的洞察，我将 Soundness 从 4 下调至 3.5，Overall 维持 3.5。

---

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部 7 个问题的逐条回应。总结：

- **N1**（新颖性有限）：[AGREE] 同意 framing 需调整，但认为经验贡献和诊断框架仍有发表价值
- **N2**（benchmark 窄）：[AGREE] 部分同意，但 best-case argument 和 variable isolation 的普遍性是有效缓解因素，建议降级为 should-fix
- **W1**（正负不对称）：[AGREE] 完全同意，与我自己的 N2 一致
- **W2**（缺 test-time scaling 讨论）：[REBUT] DeepSeek-R1/QwQ/o3/PRM 均已被引用或测试，R2 批评部分不准确
- **W3**（约束浅）：[AGREE] 部分同意设计关注，但 variable isolation 不依赖约束复杂度
- **W4**（缺引用）：[REBUT] 4 类中至少 3 类已被覆盖，DyLoS 可能就是 R2 所指论文
- **W5**（近退化适用性）：[AGREE] 有价值的理论问题，论文确实缺少过渡区间的形式化刻画

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2566 · 2026-05-25T21:34:29.929158+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 23 审稿报告（Fresh Review）— 交叉分享后修订版\n\n**项目**: symb_invariant_consensus\n**Venue**: EMNLP 2026 (ARR)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+Related Work）\n**圆桌轮次**: 1 轮（独立初审 + 交叉分享，达成共识）\n**交叉分享完成度**: R1 和 R2 均完成逐条 [AGREE]/[REBUT] 回应\n\n---\n\n## Summary\n\n本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM chain-of-thought traces 中提取 FOL 约束并用 Z3 求解 weighted partial MAX-SAT 以选答案。核心发现为负面结果：自提取约束系统性地确认多数投票结果（symbolic confirmation bias, SCB），SICA 在退化条件下归约为多数投票。论文在 9 个模型（7B 到 frontier）、4 个 benchmark 上验证了这一现象，测试了 27 种 training-free 补救策略均失败，提出三项诊断指标（C₀, K_eff, BR），并展示跨架构 NLI verifier 可部分突破瓶颈。\n\n---\n\n## Strengths\n\n**S1.** 实验方法论的高标准远超同类工作——McNemar + BH correction + TOST 等价检验 + bootstrap CI + 功效分析 + 多种子复制在 NLP 论文中罕见。[R1, R2 共识]\n\n**S2.** 27 种 training-free 补救策略的系统测试是有价值的负面证据，independence-accuracy trade-off 防止社区重复探索已证明无效的方向。[R1, R2 共识]\n\n**S3.** Observation 1（Argmax Preservation）将经验发现提升为可验证的形式化命题，推导在给定前提下正确。[R2 初审 Soundness 4/5]\n\n**S4.** 诊断框架（C₀, K_eff, BR）从 K=12 pilot run 即可计算，具有实际应用价值。[R1, R2 共识]\n\n**S5.** 22 页附录的消融和敏感性分析（prompt templates、case studies、per-subtype 分析、CV 直方图等）大幅增强可复现性。[R1, R2 共识]\n\n**S6.** Limitations 坦诚，Discussion 不过度声称——exploratory vs. confirmatory 的区分、统计功效不足的报告体现良好学术诚信。[R1, R2 共识]\n\n**S7.** 跨架构 NLI escape 虽初步，但指向正确的研究方向。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [R1-N1 + R2 AGREE] Observation 1 在 SICA 的 source-attribution scoring 设计下近乎同义反复**\n- σ(c,a) 完全基于约束的来源 trace（provenance）而非逻辑内容。在 variable isolation 导致跨 trace 约束无法交叉引用的情况下（§5.2: 56.4% 跨答案约束共享零个 Z3 变量），退化是 scoring 设计的直接后果而非关于 self-extraction 的 surprising discovery。\n- R2 补充：syntactic deduplication（46%）未按语义等价去重。两条来自不同 trace 的约束可能语义相同但变量名不同，Z3 将它们视为独立命题。\n- R2 修正：论文经验发现退化条件在实践中普遍成立（9 模型、BR 1.66-4.97x）仍有增量贡献，但 Observation 1 的 claim 范围需收窄。\n- **修改要求**: (1) 将 Observation 1 明确限定为 SICA 特定设计（provenance-based scoring + variable isolation）的分析结论；(2) 讨论 content-based scoring 替代方案（如语义嵌入跨 trace 匹配、变量规范化）并解释为何不可行；(3) 重新定位经验发现（退化在实践中普遍发生）为核心贡献。\n\n**MF2. [R2-N1 + R1 AGREE] 核心发现新颖性有限——但经验贡献和诊断框架仍有价值**\n- SCB 核心机制可从 Huang et al. (2024) / Kamoi et al. (2024) 合理预期。\n- R1 同意 framing 需调整，但指出三方面增量：(a) M→T→(A,C) 因果结构和 variable isolation 的具体机制比一般性\"self-correction fails\"更有操作意义；(b) 9 模型 × 4 基准 × 27 策略的经验广度在该子领域无先例；(c) 诊断工具 C₀/K_eff/BR 是直接可用的实践指导。\n- R1 引用 ARR H1 规则：\"results appearing obvious retrospectively doesn't mean the community already knows them empirically\"。LogicLM/LINC/SatLM 均假设形式化约束提供独立信号，本文的系统性反证有发表价值。\n- **修改要求**: (1) 将重心从理论贡献（Observation 1）转向经验发现和诊断框架；(2) 论证为什么 SatLM/LogicLM 的成功给了社区错误的乐观预期，从而凸显本文的反直觉价值。\n\n**MF3. [R2-N2 + R1 部分 AGREE] Benchmark 范围有限，claim 需收窄**\n- 主要评估仅 FOLIO (n=204) + ProofWriter (n=600)。R1 提出缓解因素：(a) best-case argument（最适合约束提取的任务上都失败）；(b) StrategyQA/LogiQA 非模板化逻辑推理；(c) variable isolation 不依赖特定 benchmark。\n- 但 R1 也同意代码生成（约束=可执行单元测试）和数学推理（完整 GSM8K 评估）确实未覆盖。\n- R1 建议降级为 should-fix，考虑到 best-case argument 的有效性。\n- **修改要求**: (1) Abstract/Intro 限定 claim 为\"logical reasoning benchmarks under zero-shot extraction\"；(2) 在 Limitations 中更显著地讨论代码生成和数学推理场景。\n\n**MF4. [R1-N2 + R2 AGREE] Cross-architecture escape 的 capability-gap pattern (n=6) 作为三大贡献之一证据不足**\n- ρ=1.0, p=0.003 仅基于 n=6 对，对单点扰动不稳健。R2 补充：Table 3 显示 combo gain 随 generator capability 单调递减（Mistral-7B +6.67 → Qwen3-14B +0.50 pp），对 frontier 模型几乎无意义。\n- **修改要求**: (1) 降级为 observation 而非 contribution；(2) 主文引用附录 W 的 15-condition 扩展；(3) 对基于 n=6 的 implications 加更多 hedging。\n\n### Should-Fix（影响评分）\n\n**SF1. [R1-W1 + R2 AGREE] 结构独立性与外部监督信号的归因混淆**\n- NLI verifiers 在 MultiNLI 上 fine-tuned。跨模型 LLM 投票（也有结构独立性但无 NLI 信号）不奏效（Appendix O）。关键因素是 structural independence + task-relevant supervised signal 的组合。\n- Discussion 中\"without task-specific training\"表述不准确（MultiNLI 与逻辑推理高度相关）。\n- **建议**: 明确 escape 需要两个条件，设计控制实验分离两个因素（如用未 fine-tuned 的 DeBERTa base 做 verifier）。\n\n**SF2. [R1-W2 + R2 AGREE] 统计功效不足以支撑等价性声明**\n- MDE 4.6-4.8 pp，典型 |Δ| ≤ 2 pp。仅 4/11 通过 TOST。R2 补充 bootstrap CI 提供部分缓解（最有利条件上界 < +1.62 pp）。\n- **建议**: 将\"no condition shows significant positive effect\"改为更审慎表述，如\"we find no evidence of positive effect, though power to detect effects below ~4.6pp is limited\"。\n\n**SF3. [R1-W3 + R2 AGREE] \"Symbolic Confirmation Bias\" 命名可能有误导性**\n- 排列检验确认 BR 反映 trace-count geometry。约束非 actively biased 而是 not independently informative。R2 理解修辞动机但建议在正文中明确区分现象（constraints confirm majority）和机制（non-independence/redundancy）。\n- **建议**: 首次引入术语时明确区分。\n\n**SF4. [R1-W4 + R2 AGREE] Variable normalization 未被测试——27 种策略中最显眼的缺失**\n- R2 认同这是直接针对已确认根本原因的修复方案。最简单版本：在提取 prompt 中强制固定变量名方案。\n- **建议**: 至少测试 prompt-level 变量规范化，或解释为何不可行。\n\n**SF5. [R2-W2，R1 REBUT 后修正] Test-time compute scaling 范式讨论深度不足（非缺失）**\n- R1 核实后指出 DeepSeek-R1 (Guo et al. 2025)、QwQ (Qwen 2024)、o3（Table 2 实测 SCB）、PRM 文献（Lightman/Wang/Cobbe）均已被引用或测试。R2 的\"缺失\"定性不准确。\n- 实际问题是**讨论深度**不足：为什么 o1/R1 的 learned verification 成功而 self-extraction 失败，可以更充分地在 Discussion 中展开。\n- **建议**: 在 Discussion 中增加 paradigm-level 对比。\n\n**SF6. [R2-W3 + R1 部分 AGREE] 约束提取质量过浅**\n- R1 认为更丰富约束语言不太可能改变核心结论（variable isolation 不依赖约束复杂度），且逻辑 prompt 实际允许 Implies/And/Or 复合结构。但与 SF4 一致，如果约束被设计为跨 trace 可比较的格式（统一本体），SCB 可能改变。\n- **建议**: 讨论约束浅层性是设计选择还是模型能力限制。\n\n**SF7. [R2-W4，R1 REBUT 后修正] 近期相关工作覆盖——大部分已到位**\n- R1 核实：DeepSeek-R1/QwQ/o3/PRM 均已引用或测试；DyLoS (Xu et al. 2026) 可能就是 R2 所指的 EACL 2026 论文。\n- 仅\"Neurosymbolic Language Reasoning as SMT (2026)\"待确认是否真实存在。\n- **建议**: 如 SMT 论文确实存在，补充引用。\n\n**SF8. [R1-W5 + R2 AGREE] Confirmatory vs exploratory 划分标准不透明**\n- m=6 confirmatory 条件的选择标准（n ≥ 200 阈值来源、是否预注册）未在正文明确说明。\n- **建议**: 在 §4.1 或 §4.2 明确列出 confirmatory 条件及划分标准。\n\n**SF9. [R2-W5 + R1 AGREE] Observation 1 在\"近退化\"条件下的适用性 gap**\n- R1 提供了经验证据（三区域分类、entropy decomposition、α 消融）支持连续过渡而非相变。但缺少对过渡区间行为的形式化刻画——intermediate regime (SC 50-60%) 是否存在某个 |C\\|/|C| 阈值使 SICA 开始提供纠错信号？\n- **建议**: 在 Discussion 或 Appendix 中讨论过渡区间行为。\n\n---\n\n## Reviewer Consensus [交叉分享后]\n\n两位 Reviewer 在以下关键问题上达成完全共识 [AGREE]：\n\n1. **Observation 1 的设计依赖性**: 退化是 source-attribution scoring + variable isolation 的直接后果，Observation 1 的 claim 范围过宽。[R1-N1 + R2 AGREE]\n2. **核心 insight 可预测性较高**: 但经验贡献（9 模型 × 27 策略）和诊断框架仍有发表价值。[R2-N1 + R1 AGREE with nuance]\n3. **n=6 capability-gap pattern 作为贡献不足**: 应降级为 observation。[R1-N2 + R2 AGREE]\n4. **结构独立性 vs 监督信号混淆**: Escape 需要两个条件。[R1-W1 + R2 AGREE]\n5. **统计功效不足**: bootstrap CI 部分缓解，但表述需更审慎。[R1-W2 + R2 AGREE]\n6. **SCB 命名有误导性**: 实际机制是 non-independence，非 cognitive bias。[R1-W3 + R2 AGREE]\n7. **Variable normalization 缺失**: 最直接的修复方案未测试。[R1-W4 + R2 AGREE]\n8. **Confirmatory 划分不透明**: 需明确标准。[R1-W5 + R2 AGREE]\n9. **近退化适用性 gap**: 缺少过渡区间形式化。[R2-W5 + R1 AGREE]\n\n## Reviewer Divergence [已解决]\n\nR1 对 R2 的两个 REBUT 均基于事实核实，双方已无未解决矛盾：\n1. **R2-W2（缺 test-time scaling 讨论）→ R1 REBUT**: 相关工作已引用，问题是讨论深度而非缺失。\n2. **R2-W4（缺近期引用）→ R1 REBUT**: 4 类中至少 3 类已覆盖。\n\n---\n\n## Questions\n\n**Q1** [R2]: 跨模型同架构的约束提取（非自提取）是否改变 SCB？\n\n**Q2** [R2]: SCB 对提取温度有多敏感？Appendix 仅在 Mistral-7B 上测试。\n\n**Q3** [R2]: 诊断框架阈值是否数据集依赖？\n\n**Q4** [R2]: 27 种策略是独立策略还是部分组合？\n\n**Q5** [R1]: Eq. 2 的 argmax formulation 与 Algorithm 1 实现是否存在全局最优性 gap？\n\n**Q6** [R1]: K_eff 公式引用 Ladha (1992) 的准确性？\n\n---\n\n## Missing References\n\n1. **\"Neurosymbolic Language Reasoning as SMT\" (2026)** — 待确认是否真实存在。如存在，与 Z3 MAX-SAT 方案高度相关。[R2 提出，R1 未能确认]\n\n注：R2 初审列出的其他 3 类\"缺失\"引用（DeepSeek-R1/o1/o3、PRM、EACL 2026 DyLoS）经 R1 核实后确认**已被论文引用或测试**。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（0 critical, 2 warnings, 23 info）\n\n主要发现：\n- 主文 8 页，9 个 display items / 8 页 ≈ 1.1/页，密度优秀\n- Figure 1 在 page 2 顶部，Title-Abstract-Figure 1 一致性好\n- 所有表格 booktabs 风格，float 无漂移，颜色方案一致\n\nWarnings：\n1. Page 30（Appendix 末页 AI Assistants 声明）仅占 ~25%，建议合并到前一页\n2. Figure 7 (p.17, appendix) 策略名称字号较小，建议 ≥ 7pt\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**R1**: 3.5（Soundness 3.5, Excitement 3）\n**R2**: 3.5（Soundness 3.5↓from 4, Excitement 3）\n**Director**: 3.5\n\n**置信度: 4/5**\n\n**评分依据**:\n\n这是一篇实验方法论严谨、统计分析全面的负面结果论文。核心贡献对 neuro-symbolic reasoning 社区有直接指导意义。\n\n四个 Must-Fix 问题制约当前版本：\n\n1. **MF1: Observation 1 的论证循环性** — 核心理论贡献在 source-attribution scoring + variable isolation 设计下近乎同义反复。需收窄 claim 范围并讨论替代方案。\n\n2. **MF2: 核心发现的新颖性定位** — 需将重心从理论贡献转向经验发现和诊断框架，并论证为何 SatLM/LogicLM 的成功给了社区错误预期。\n\n3. **MF3: Benchmark 范围** — claim 暗示 generality 但仅覆盖英文逻辑推理。best-case argument 有效但需在 claim 中反映。\n\n4. **MF4: n=6 capability-gap pattern** — 作为 Contribution 3 证据不足，应降级。\n\n**可行修改路径**:\n- MF1: 增加 content-based scoring / variable normalization 的讨论和实验（~1-2 周）\n- MF2: 重新定位 framing（~2-3 天）\n- MF3: 收窄 claim + 增强 Limitations 讨论（~1 天）\n- MF4: 降级 + 引用附录扩展结果（~1 天）\n\n如果 MF1-MF4 充分解决（特别是 MF1 的替代方案讨论），论文有潜力达到 Conference (4.0)。当前版本更适合 Findings (3.0-3.5)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"symbolic mirage\" 作为隐喻可保留但建议在正文中正式定义\n- Contribution 3 应反映 n=6 的初步性质（\"preliminary observation\" 而非 \"contribution\"）\n\n### §3 Method\n- Eq. 2 与 Algorithm 1 的 gap 应在正文注明\n- K_eff 公式对 Ladha (1992) 的引用准确性需确认\n- 应讨论 content-based scoring 替代方案和 variable normalization\n\n### §4 Experiments\n- Table 1 caption 中灰色带可能被误读为显著性\n- Figure 2 的 circled points 应标注是否经 BH 校正\n- \"nine models\" 的 BR 和完整评估的 distinction 应更清晰\n\n### §5 Analysis\n- §5.1: SCB 术语首次引入时区分实际机制（trace-count geometry）与认知确认偏见\n- §5.2: 增加 variable normalization 讨论\n- §5.4: 明确 escape 需要 structural independence + supervised signal 两个条件\n- §5.4: \"without task-specific training\" 需修正\n\n### §6 Discussion\n- 基于 n=6 pattern 推导的 implications 需更多 hedging\n- 增加 learned verification (o1/R1) vs self-extraction 的 paradigm-level 对比\n\n### Limitations\n- 增加 benchmark 范围限制对 claim generality 的影响\n- 增加 variable normalization 未被测试的讨论",
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 23 审稿报告（Fresh Review）— 交叉分享后修订版\n\n**项目**: symb_invariant_consensus\n**Venue**: EMNLP 2026 (ARR)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+Related Work）\n**圆桌轮次**: 1 轮（独立初审 + 交叉分享，达成共识）\n**交叉分享完成度**: R1 和 R2 均完成逐条 [AGREE]/[REBUT] 回应\n\n---\n\n## Summary\n\n本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM chain-of-thought traces 中提取 FOL 约束并用 Z3 求解 weighted partial MAX-SAT 以选答案。核心发现为负面结果：自提取约束系统性地确认多数投票结果（symbolic confirmation bias, SCB），SICA 在退化条件下归约为多数投票。论文在 9 个模型（7B 到 frontier）、4 个 benchmark 上验证了这一现象，测试了 27 种 training-free 补救策略均失败，提出三项诊断指标（C₀, K_eff, BR），并展示跨架构 NLI verifier 可部分突破瓶颈。\n\n---\n\n## Strengths\n\n**S1.** 实验方法论的高标准远超同类工作——McNemar + BH correction + TOST 等价检验 + bootstrap CI + 功效分析 + 多种子复制在 NLP 论文中罕见。[R1, R2 共识]\n\n**S2.** 27 种 training-free 补救策略的系统测试是有价值的负面证据，independence-accuracy trade-off 防止社区重复探索已证明无效的方向。[R1, R2 共识]\n\n**S3.** Observation 1（Argmax Preservation）将经验发现提升为可验证的形式化命题，推导在给定前提下正确。[R2 初审 Soundness 4/5]\n\n**S4.** 诊断框架（C₀, K_eff, BR）从 K=12 pilot run 即可计算，具有实际应用价值。[R1, R2 共识]\n\n**S5.** 22 页附录的消融和敏感性分析（prompt templates、case studies、per-subtype 分析、CV 直方图等）大幅增强可复现性。[R1, R2 共识]\n\n**S6.** Limitations 坦诚，Discussion 不过度声称——exploratory vs. confirmatory 的区分、统计功效不足的报告体现良好学术诚信。[R1, R2 共识]\n\n**S7.** 跨架构 NLI escape 虽初步，但指向正确的研究方向。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [R1-N1 + R2 AGREE] Observation 1 在 SICA 的 source-attribution scoring 设计下近乎同义反复**\n- σ(c,a) 完全基于约束的来源 trace（provenance）而非逻辑内容。在 variable isolation 导致跨 trace 约束无法交叉引用的情况下（§5.2: 56.4% 跨答案约束共享零个 Z3 变量），退化是 scoring 设计的直接后果而非关于 self-extraction 的 surprising discovery。\n- R2 补充：syntactic deduplication（46%）未按语义等价去重。两条来自不同 trace 的约束可能语义相同但变量名不同，Z3 将它们视为独立命题。\n- R2 修正：论文经验发现退化条件在实践中普遍成立（9 模型、BR 1.66-4.97x）仍有增量贡献，但 Observation 1 的 claim 范围需收窄。\n- **修改要求**: (1) 将 Observation 1 明确限定为 SICA 特定设计（provenance-based scoring + variable isolation）的分析结论；(2) 讨论 content-based scoring 替代方案（如语义嵌入跨 trace 匹配、变量规范化）并解释为何不可行；(3) 重新定位经验发现（退化在实践中普遍发生）为核心贡献。\n\n**MF2. [R2-N1 + R1 AGREE] 核心发现新颖性有限——但经验贡献和诊断框架仍有价值**\n- SCB 核心机制可从 Huang et al. (2024) / Kamoi et al. (2024) 合理预期。\n- R1 同意 framing 需调整，但指出三方面增量：(a) M→T→(A,C) 因果结构和 variable isolation 的具体机制比一般性\"self-correction fails\"更有操作意义；(b) 9 模型 × 4 基准 × 27 策略的经验广度在该子领域无先例；(c) 诊断工具 C₀/K_eff/BR 是直接可用的实践指导。\n- R1 引用 ARR H1 规则：\"results appearing obvious retrospectively doesn't mean the community already knows them empirically\"。LogicLM/LINC/SatLM 均假设形式化约束提供独立信号，本文的系统性反证有发表价值。\n- **修改要求**: (1) 将重心从理论贡献（Observation 1）转向经验发现和诊断框架；(2) 论证为什么 SatLM/LogicLM 的成功给了社区错误的乐观预期，从而凸显本文的反直觉价值。\n\n**MF3. [R2-N2 + R1 部分 AGREE] Benchmark 范围有限，claim 需收窄**\n- 主要评估仅 FOLIO (n=204) + ProofWriter (n=600)。R1 提出缓解因素：(a) best-case argument（最适合约束提取的任务上都失败）；(b) StrategyQA/LogiQA 非模板化逻辑推理；(c) variable isolation 不依赖特定 benchmark。\n- 但 R1 也同意代码生成（约束=可执行单元测试）和数学推理（完整 GSM8K 评估）确实未覆盖。\n- R1 建议降级为 should-fix，考虑到 best-case argument 的有效性。\n- **修改要求**: (1) Abstract/Intro 限定 claim 为\"logical reasoning benchmarks under zero-shot extraction\"；(2) 在 Limitations 中更显著地讨论代码生成和数学推理场景。\n\n**MF4. [R1-N2 + R2 AGREE] Cross-architecture escape 的 capability-gap pattern (n=6) 作为三大贡献之一证据不足**\n- ρ=1.0, p=0.003 仅基于 n=6 对，对单点扰动不稳健。R2 补充：Table 3 显示 combo gain 随 generator capability 单调递减（Mistral-7B +6.67 → Qwen3-14B +0.50 pp），对 frontier 模型几乎无意义。\n- **修改要求**: (1) 降级为 observation 而非 contribution；(2) 主文引用附录 W 的 15-condition 扩展；(3) 对基于 n=6 的 implications 加更多 hedging。\n\n### Should-Fix（影响评分）\n\n**SF1. [R1-W1 + R2 AGREE] 结构独立性与外部监督信号的归因混淆**\n- NLI verifiers 在 MultiNLI 上 fine-tuned。跨模型 LLM 投票（也有结构独立性但无 NLI 信号）不奏效（Appendix O）。关键因素是 structural independence + task-relevant supervised signal 的组合。\n- Discussion 中\"without task-specific training\"表述不准确（MultiNLI 与逻辑推理高度相关）。\n- **建议**: 明确 escape 需要两个条件，设计控制实验分离两个因素（如用未 fine-tuned 的 DeBERTa base 做 verifier）。\n\n**SF2. [R1-W2 + R2 AGREE] 统计功效不足以支撑等价性声明**\n- MDE 4.6-4.8 pp，典型 |Δ| ≤ 2 pp。仅 4/11 通过 TOST。R2 补充 bootstrap CI 提供部分缓解（最有利条件上界 < +1.62 pp）。\n- **建议**: 将\"no condition shows significant positive effect\"改为更审慎表述，如\"we find no evidence of positive effect, though power to detect effects below ~4.6pp is limited\"。\n\n**SF3. [R1-W3 + R2 AGREE] \"Symbolic Confirmation Bias\" 命名可能有误导性**\n- 排列检验确认 BR 反映 trace-count geometry。约束非 actively biased 而是 not independently informative。R2 理解修辞动机但建议在正文中明确区分现象（constraints confirm majority）和机制（non-independence/redundancy）。\n- **建议**: 首次引入术语时明确区分。\n\n**SF4. [R1-W4 + R2 AGREE] Variable normalization 未被测试——27 种策略中最显眼的缺失**\n- R2 认同这是直接针对已确认根本原因的修复方案。最简单版本：在提取 prompt 中强制固定变量名方案。\n- **建议**: 至少测试 prompt-level 变量规范化，或解释为何不可行。\n\n**SF5. [R2-W2，R1 REBUT 后修正] Test-time compute scaling 范式讨论深度不足（非缺失）**\n- R1 核实后指出 DeepSeek-R1 (Guo et al. 2025)、QwQ (Qwen 2024)、o3（Table 2 实测 SCB）、PRM 文献（Lightman/Wang/Cobbe）均已被引用或测试。R2 的\"缺失\"定性不准确。\n- 实际问题是**讨论深度**不足：为什么 o1/R1 的 learned verification 成功而 self-extraction 失败，可以更充分地在 Discussion 中展开。\n- **建议**: 在 Discussion 中增加 paradigm-level 对比。\n\n**SF6. [R2-W3 + R1 部分 AGREE] 约束提取质量过浅**\n- R1 认为更丰富约束语言不太可能改变核心结论（variable isolation 不依赖约束复杂度），且逻辑 prompt 实际允许 Implies/And/Or 复合结构。但与 SF4 一致，如果约束被设计为跨 trace 可比较的格式（统一本体），SCB 可能改变。\n- **建议**: 讨论约束浅层性是设计选择还是模型能力限制。\n\n**SF7. [R2-W4，R1 REBUT 后修正] 近期相关工作覆盖——大部分已到位**\n- R1 核实：DeepSeek-R1/QwQ/o3/PRM 均已引用或测试；DyLoS (Xu et al. 2026) 可能就是 R2 所指的 EACL 2026 论文。\n- 仅\"Neurosymbolic Language Reasoning as SMT (2026)\"待确认是否真实存在。\n- **建议**: 如 SMT 论文确实存在，补充引用。\n\n**SF8. [R1-W5 + R2 AGREE] Confirmatory vs exploratory 划分标准不透明**\n- m=6 confirmatory 条件的选择标准（n ≥ 200 阈值来源、是否预注册）未在正文明确说明。\n- **建议**: 在 §4.1 或 §4.2 明确列出 confirmatory 条件及划分标准。\n\n**SF9. [R2-W5 + R1 AGREE] Observation 1 在\"近退化\"条件下的适用性 gap**\n- R1 提供了经验证据（三区域分类、entropy decomposition、α 消融）支持连续过渡而非相变。但缺少对过渡区间行为的形式化刻画——intermediate regime (SC 50-60%) 是否存在某个 |C\\|/|C| 阈值使 SICA 开始提供纠错信号？\n- **建议**: 在 Discussion 或 Appendix 中讨论过渡区间行为。\n\n---\n\n## Reviewer Consensus [交叉分享后]\n\n两位 Reviewer 在以下关键问题上达成完全共识 [AGREE]：\n\n1. **Observation 1 的设计依赖性**: 退化是 source-attribution scoring + variable isolation 的直接后果，Observation 1 的 claim 范围过宽。[R1-N1 + R2 AGREE]\n2. **核心 insight 可预测性较高**: 但经验贡献（9 模型 × 27 策略）和诊断框架仍有发表价值。[R2-N1 + R1 AGREE with nuance]\n3. **n=6 capability-gap pattern 作为贡献不足**: 应降级为 observation。[R1-N2 + R2 AGREE]\n4. **结构独立性 vs 监督信号混淆**: Escape 需要两个条件。[R1-W1 + R2 AGREE]\n5. **统计功效不足**: bootstrap CI 部分缓解，但表述需更审慎。[R1-W2 + R2 AGREE]\n6. **SCB 命名有误导性**: 实际机制是 non-independence，非 cognitive bias。[R1-W3 + R2 AGREE]\n7. **Variable normalization 缺失**: 最直接的修复方案未测试。[R1-W4 + R2 AGREE]\n8. **Confirmatory 划分不透明**: 需明确标准。[R1-W5 + R2 AGREE]\n9. **近退化适用性 gap**: 缺少过渡区间形式化。[R2-W5 + R1 AGREE]\n\n## Reviewer Divergence [已解决]\n\nR1 对 R2 的两个 REBUT 均基于事实核实，双方已无未解决矛盾：\n1. **R2-W2（缺 test-time scaling 讨论）→ R1 REBUT**: 相关工作已引用，问题是讨论深度而非缺失。\n2. **R2-W4（缺近期引用）→ R1 REBUT**: 4 类中至少 3 类已覆盖。\n\n---\n\n## Questions\n\n**Q1** [R2]: 跨模型同架构的约束提取（非自提取）是否改变 SCB？\n\n**Q2** [R2]: SCB 对提取温度有多敏感？Appendix 仅在 Mistral-7B 上测试。\n\n**Q3** [R2]: 诊断框架阈值是否数据集依赖？\n\n**Q4** [R2]: 27 种策略是独立策略还是部分组合？\n\n**Q5** [R1]: Eq. 2 的 argmax formulation 与 Algorithm 1 实现是否存在全局最优性 gap？\n\n**Q6** [R1]: K_eff 公式引用 Ladha (1992) 的准确性？\n\n---\n\n## Missing References\n\n1. **\"Neurosymbolic Language Reasoning as SMT\" (2026)** — 待确认是否真实存在。如存在，与 Z3 MAX-SAT 方案高度相关。[R2 提出，R1 未能确认]\n\n注：R2 初审列出的其他 3 类\"缺失\"引用（DeepSeek-R1/o1/o3、PRM、EACL 2026 DyLoS）经 R1 核实后确认**已被论文引用或测试**。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（0 critical, 2 warnings, 23 info）\n\n主要发现：\n- 主文 8 页，9 个 display items / 8 页 ≈ 1.1/页，密度优秀\n- Figure 1 在 page 2 顶部，Title-Abstract-Figure 1 一致性好\n- 所有表格 booktabs 风格，float 无漂移，颜色方案一致\n\nWarnings：\n1. Page 30（Appendix 末页 AI Assistants 声明）仅占 ~25%，建议合并到前一页\n2. Figure 7 (p.17, appendix) 策略名称字号较小，建议 ≥ 7pt\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**R1**: 3.5（Soundness 3.5, Excitement 3）\n**R2**: 3.5（Soundness 3.5↓from 4, Excitement 3）\n**Director**: 3.5\n\n**置信度: 4/5**\n\n**评分依据**:\n\n这是一篇实验方法论严谨、统计分析全面的负面结果论文。核心贡献对 neuro-symbolic reasoning 社区有直接指导意义。\n\n四个 Must-Fix 问题制约当前版本：\n\n1. **MF1: Observation 1 的论证循环性** — 核心理论贡献在 source-attribution scoring + variable isolation 设计下近乎同义反复。需收窄 claim 范围并讨论替代方案。\n\n2. **MF2: 核心发现的新颖性定位** — 需将重心从理论贡献转向经验发现和诊断框架，并论证为何 SatLM/LogicLM 的成功给了社区错误预期。\n\n3. **MF3: Benchmark 范围** — claim 暗示 generality 但仅覆盖英文逻辑推理。best-case argument 有效但需在 claim 中反映。\n\n4. **MF4: n=6 capability-gap pattern** — 作为 Contribution 3 证据不足，应降级。\n\n**可行修改路径**:\n- MF1: 增加 content-based scoring / variable normalization 的讨论和实验（~1-2 周）\n- MF2: 重新定位 framing（~2-3 天）\n- MF3: 收窄 claim + 增强 Limitations 讨论（~1 天）\n- MF4: 降级 + 引用附录扩展结果（~1 天）\n\n如果 MF1-MF4 充分解决（特别是 MF1 的替代方案讨论），论文有潜力达到 Conference (4.0)。当前版本更适合 Findings (3.0-3.5)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"symbolic mirage\" 作为隐喻可保留但建议在正文中正式定义\n- Contribution 3 应反映 n=6 的初步性质（\"preliminary observation\" 而非 \"contribution\"）\n\n### §3 Method\n- Eq. 2 与 Algorithm 1 的 gap 应在正文注明\n- K_eff 公式对 Ladha (1992) 的引用准确性需确认\n- 应讨论 content-based scoring 替代方案和 variable normalization\n\n### §4 Experiments\n- Table 1 caption 中灰色带可能被误读为显著性\n- Figure 2 的 circled points 应标注是否经 BH 校正\n- \"nine models\" 的 BR 和完整评估的 distinction 应更清晰\n\n### §5 Analysis\n- §5.1: SCB 术语首次引入时区分实际机制（trace-count geometry）与认知确认偏见\n- §5.2: 增加 variable normalization 讨论\n- §5.4: 明确 escape 需要 structural independence + supervised signal 两个条件\n- §5.4: \"without task-specific training\" 需修正\n\n### §6 Discussion\n- 基于 n=6 pattern 推导的 implications 需更多 hedging\n- 增加 learned verification (o1/R1) vs self-extraction 的 paradigm-level 对比\n\n### Limitations\n- 增加 benchmark 范围限制对 claim generality 的影响\n- 增加 variable normalization 未被测试的讨论",
    "project": "symb_invariant_consensus",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 2567 · 2026-05-25T21:34:33.829243+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3900
}
```

</details>

---


### Assistant

_source line 2568 · 2026-05-25T21:34:45.959345+00:00_

审稿报告已更新并重新投递（含交叉分享后的完整 [AGREE]/[REBUT] 共识记录和 factual corrections）。

**Round 23 审稿完成总结**：

- **Overall: 3.5（Borderline Conference）**，R1 和 R2 一致
- **4 个 Must-Fix**: Observation 1 设计依赖性、核心新颖性定位、Benchmark 范围、n=6 capability-gap 证据不足
- **9 个 Should-Fix**: 归因混淆、统计功效、命名误导、变量规范化缺失、讨论深度、约束浅层性、划分标准、近退化适用性等
- **交叉分享 9/11 问题完全共识**，2 个分歧由 R1 factual REBUT 解决
- **视觉审查**: 0 critical, 2 warnings（末页空白、Figure 7 字号）
- **可行修改路径**: MF1 的替代方案讨论 + MF2 的 framing 调整是关键突破点，完成后有潜力达到 Conference (4.0)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---
