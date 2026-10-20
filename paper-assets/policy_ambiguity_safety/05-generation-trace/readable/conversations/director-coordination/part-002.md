# Director coordination — Part 2 of 11

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/0e/0e806c5d99edfa05e2ae.json)

## Round 23

### Tool call

_source line 266 · 2026-05-21T06:58:57.657570+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "report": "# 审稿报告 — Round 3 (Fresh)\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n**Venue**: EMNLP 2026 via ARR May cycle (截止 2026-05-25)\n**Reviewers**: R1 (方法严谨性, 3.5/5), R2 (新颖性与完整性, 3.5/5)\n**Director Overall**: **3.0 / 5 (Findings)**\n\n---\n\n## Summary\n\n本文研究不同类型的策略歧义如何影响 LLM agent 的安全违规率。采用 matched-pair 设计，在 τ²-bench（零售/航空客服场景）上构造 300 对歧义/无歧义条款，覆盖六类歧义（两层 taxonomy：linguistic 层 3 类 + specification 层 3 类），评估五个模型（GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3），共 2,997 episodes。提出四个 claims：C1（歧义普遍增加 34.0pp 违规率，OR=15.1），C2（三层类型层级，Cramér's V=0.137），C3（linguistic/specification 层级区分不显著，inconclusive），C4（模型×类型交互效应）。附带 perturbation control、error analysis（614 traces, 5 failure modes）、Ambiguity Blindness 量化（<11% awareness）和消歧指令缓解实验（1,256 episodes）。\n\n---\n\n## Strengths\n\n**S1** [Consensus] **Matched-pair causal design 是方法论贡献**：perturbation control (Δ_perturb=3.33pp vs Δ_ambig=34.0pp) + TOST equivalence + variance decomposition + ICC reproducibility 的组合在 agent safety benchmarking 中几乎没有先例。论文的因果推断设计显著优于同期工作（DRIP-R: correlation only, PolicyBank: no matched design）。\n\n**S2** [Consensus] **C1 和 C2 有压倒性统计支撑**：C1 (p < 10⁻¹⁰⁵, OR=15.1, bootstrap CI [31.2, 36.9]) 和 C2 (p = 3.6 × 10⁻⁵, V=0.137, power=0.993) 的证据强度远超审稿接受阈值。variance decomposition 发现 clause identity 解释 22.4% vs model identity 仅 1.0%，是重要的实践洞察。\n\n**S3** [Consensus] **Authorization scope \"canary type\" 发现有独特实践价值**：Claude 12% vs GPT-5.4 64%（52pp 跨模型范围）直接揭示了不同 safety training 策略的差异化效果——但此结论受 cross-judge confound 影响（见 MF1）。\n\n**S4** [Consensus] **Claim 层级透明**：C3 显式标记为 inconclusive，Holm-Bonferroni 校正后 C3 不通过。logistic regression 控制 token delta 后层级项翻转。这种方法论诚实度在该领域不常见。\n\n**S5** [Consensus] **Error analysis 提供机制洞察**：三种机制模式（structural misparse, information gap-filling, boundary violation）跨越 specification/linguistic 层级边界，3/6 类型全模型一致、6/6 多数一致。Ambiguity Blindness 的量化 (<11% awareness, >88% surface adoption) 虽概念上不意外但首次在 agent safety context 中给出具体数字。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [Critical — Consensus] **Cross-judge confound 缺乏校准数据**\n\nGPT-5.4 评判 Claude/Qwen3/DeepSeek；GPT-4.1 评判 GPT-5.4。Judge identity 与 model identity 完全混淆。论文最引人注目的发现——authorization scope Claude 12% vs GPT-5.4 64%（Table 1）——跨越 judge boundary（Claude 由 GPT-5.4 评判，GPT-5.4 由 GPT-4.1 评判）。无法区分 GPT-5.4 的 vulnerability profile 是模型特性还是 GPT-4.1 检测能力差异的 artifact。论文未提供任何 inter-judge calibration 数据。Within-judge analysis 仅能确认 C1 在两个子群中一致，无法量化 judge bias 方向和大小。\n\n*R1-N3 和 R2-N2 独立识别；交叉后两人 AGREE。*\n\n**要求**: (a) 在 ≥100 episodes 上做 human evaluation 建立 LLM-human agreement baseline；(b) 和/或让 GPT-5.4 和 GPT-4.1 同时评判同一批 traces 量化 judge bias；(c) 在 §4.4 正式讨论 confound 影响。\n\n---\n\n**MF2** [Critical — Consensus] **Human evaluation baseline 完全缺失**\n\n核心指标（binary violation/no-violation + four-tier severity）的 2,997 episodes 全部由 LLM judge 产生，无任何 human-LLM agreement 数据。§4.2 的 clause pair 质量有双人审核，§6 的 failure mode 有 LLM-LLM agreement (AC₁=0.62, κ=0.52)——但论文最核心的违规判定缺乏人类校准。R-Judge (EMNLP 2024 Findings) 和 ToolEmu (ICLR 2024)——论文引用的同领域工作——均包含 human evaluation baseline。纯 LLM-as-judge 且无人类校准低于 EMNLP agent safety 的当前社区标准。\n\n*R2-N3 提出为 Must-Fix；R1 交叉后从 W2 升级同意。*\n\n**要求**: 对 ≥100 episodes（stratified by type × severity）做 human annotation，报告 human-LLM agreement (Cohen's κ)。\n\n---\n\n**MF3** [Critical — Consensus] **Incompleteness confound 未充分解决**\n\nIncompleteness 的无歧义变体必然添加新的策略信息（边界条件、例外规则），而非仅消解歧义。这违反了 §4.2 matched-pair 设计的第二条质量标准（\"eliminates that ambiguity without introducing new information that changes the policy's scope\"）。Incompleteness 驱动了 C2 三层层级的顶层（53.6%）、Systematic Nocuity 的 24% universal convergence、以及 \"universally dangerous\" 的核心叙事。论文在 Limitations 中用 token delta logistic regression 处理（β→−0.10, p=0.384 after controlling token delta），但 token count 是信息内容的极粗糙代理。一条添加全新退货排除规则的条款，其信息增量远超同等 token 数量的词汇替换。排除 incompleteness 后，5-type omnibus p=0.079（不显著），三层层级可能坍缩为两层（auth scope vs coreferential 仍显著，p_adj=0.039）。\n\n*R1-N2 提出为 Must-Fix；R2 交叉后从 W1 升级同意。*\n\n**要求**: (a) 在 §5.2 报告结果处立即讨论 confound，不得仅放 Limitations；(b) 报告含/不含 incompleteness 两版 C2 分析；(c) 考虑将 incompleteness 重新定义为 \"missing policy content\"（与其他 5 类性质不同）；(d) camera-ready 中增加 information-addition control。\n\n---\n\n**MF4** [Critical — Consensus] **C4 (model×type interaction) 作为 primary claim 证据不足**\n\nModel×type interaction 仅解释 2.9% 方差（η²=0.026）。R1 从统计角度指出效应量过小无法与 C1 (p < 10⁻¹⁰⁵) 和 C2 (V=0.137, p < 10⁻⁵) 并列为 primary claim。R2 从 framing 角度指出 Abstract \"jointly determine\" 暗示 model 和 type 贡献相当，与实际不符。\n\n*Director 对 p 值分歧的裁决*：R1 声称 F(12)=1.97, p=0.075；论文报告 F(20)=1.97, p=0.006。正确 df = (5−1)(6−1) = 20，R1 使用了错误的 df。论文报告的 p=0.006 在给定 df 下是自洽的。**但两位 Reviewer 一致认为，无论 p 值如何，2.9% 的方差解释量不足以支撑 primary claim 地位。**\n\n*R1-N1 和 R2-W5 从不同角度提出；交叉后两人 AGREE。*\n\n**要求**: (a) 将 C4 降级为 exploratory（与 C3 同级）；(b) Abstract \"jointly determine\" → \"type primarily determines severity, with a smaller but significant model×type interaction\"；(c) §1 贡献列表中不再将 C4 与 C1/C2 并列。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [Warning — Consensus] **TOST ±15pp margin 缺乏 domain-specific 依据**\n七个 margin 的敏感性分析（Appendix A）是好做法，但 primary margin ±15pp 无理论论证。基线 ~30-40% 下 ±15pp 意味着 15-55% 均为 \"等价\"——过于宽松。Lakens (2017) 要求 SESOI (Smallest Effect Size of Interest) 论证。\n\n**SF2** [Warning — Consensus] **Error analysis LLM 编码器未经人类验证**\nGwet's AC₁=0.62, Cohen's κ=0.52 为 LLM-LLM agreement，非 LLM-human。AC₁=0.62 处于 \"substantial\" 下界，minority failure modes 可靠性可能更低。§6.1-6.2 的 type-specific failure signatures 完全基于此。\n\n**SF3** [Warning — Consensus with qualification] **Perturbation control 检验力有限**\nn=120 (24/model), MDE≥15pp, CI [-5.0, 13.3]。Worst-case 下 surface perturbation 可解释 13.3/34.0 ≈ 39% 的主效应。C1 在任何合理假设下仍成立（残余效应 ≥20.7pp），但因果归因的精度受限。\n\n**SF4** [Warning — Consensus] **ICC 子集代表性不明**\n30/300 clause pairs (10%), 2/5 models (40%), ICC=0.919。未披露选择了哪 2 个模型。Cross-architecture reproducibility 声明受限。\n\n**SF5** [Warning — Consensus] **Mitigation 结果被低估**\nTable 3 (Appendix B) 包含高价值发现：DeepSeek 反向效果 (+2/+4 pp, 消歧指令反而增加违规)、Claude auth scope floor effect (Δ=0)、GPT-5.4 dramatic response (−40pp)。这些直接支撑 Differential Nocuity 的实践含义但被完全推入 appendix，§7 仅一句话提及。\n\n**SF6** [Warning — Consensus] **Taxonomy framing 不精确**\n§3 input taxonomy (6 types, curated from literature) 和 §6 output taxonomy (5 failure modes, empirically discovered) 使用相同术语 \"taxonomy\"，易混淆。§1 Contribution 3 应强调 failure mode taxonomy 为研究发现，非 input taxonomy。\n\n**SF7** [Warning — Partial Consensus] **Related Work 遗漏**\n- Hu et al. (2025) \"Ambiguity in LLMs is a concept missing problem\" — 与 §6.3 Ambiguity Blindness 直接相关 [两人同意]\n- Cohen (1960) / Gwet (2014) 统计原始文献 — κ 和 AC₁ 的引用规范 [两人同意]\n- DRIP-R 方法论对比不够详细 — 最直接的 concurrent work 应有更系统比较 [两人同意]\n- OpenAgentSafety (ICLR 2026) — 如涉及 policy compliance 维度则值得一提 [R2 提出，R1 conditional agree]\n\n**SF8** [Warning — R1 识别，R2 反驳，Director 裁决 R1 正确] **正文超过 8 页限制**\n§7 Discussion 从 page 8 延续到 page 9，§8 Conclusion 完全在 page 9。视觉审查 Agent 独立确认：\"Discussion 从 page 8 延续到 page 9，Conclusion 在 page 9 中部\"。EMNLP 2026 Long paper 正文（Abstract 到 Conclusion）严格 8 页。**R2 反驳不成立，论文超页。**\n\n---\n\n### Minor（不影响接收）\n\n- M1: 引用 minor mismatches — Lassiter & Goodman (2017 vs 2015), Levy (2008 vs 2007), ferrari_defects_2018 first author Rosadini [R1/R2 均识别，无虚构引用]\n- M2: Table 3 排除 coreferential 未解释原因\n- M3: 标题 \"LLM Agent Families\" 仅覆盖 5 个模型，\"families\" 措辞略显夸大\n- M4: \"Nocuous\" 对 EMNLP 读者可能不熟悉，首次使用时加释义\n- M5: Figure 1 内文字偏小，打印可读性可能受影响\n- M6: Figure 3 heatmap 建议改为 figure*（全宽）提升可读性\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 独立评审后在以下关键问题上达成完全共识：\n\n| 问题 | R1 | R2 | 交叉后 |\n|------|-----|-----|--------|\n| Cross-judge confound | N3 (Must-Fix) | N2 (Must-Fix) | 双方 AGREE |\n| Human eval baseline | W2 → 升级 | N3 (Must-Fix) | R1 升级同意 |\n| Incompleteness confound | N2 (Must-Fix) | W1 → 升级 | R2 升级同意 |\n| C4 降级 | N1 (Must-Fix) | W5 (Should-Fix) | 双方 AGREE (互补角度) |\n| TOST margin | W1 | AGREE | 共识 |\n| Error analysis validation | W2 | AGREE | 共识 |\n| Perturbation power | W3 | AGREE w/ qualification | 基本共识 |\n| ICC representativeness | W4 | AGREE | 共识 |\n| Mitigation underexploited | — | W2 → R1 AGREE | 共识 |\n| Taxonomy framing | — | W3 → R1 AGREE | 共识 |\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 裁决 |\n|------|-----|-----|---------------|\n| R2-N1: Abstract \"500 pairs\" | **REBUT** — 原文为 \"300\" | Must-Fix | **R1 正确，R2 事实前提错误，排除** |\n| 页数合规 (R1-W5) | Should-Fix (超页) | **REBUT** — 合规 | **R1 正确，视觉审查确认超页** |\n| C4 p-value | F(12)=1.97, p=0.075 | 论文 F(20)=1.97, p=0.006 自洽 | **R2 正确 (df=20)，但效应量结论一致** |\n| Related work 引用量 | 33 条足够 | 33 条偏少 | **R1 正确，数量非评审标准** |\n\n---\n\n## Questions for Authors\n\n1. 是否可行在 ~100 episodes 上做 dual-judge evaluation (GPT-5.4 + GPT-4.1 评判同一批 traces)？如果 GPT-4.1 对 GPT-5.4 系统性偏严/偏松，C4 中 GPT-5.4 的 vulnerability profile 结论如何修正？\n2. 排除 incompleteness 后，remaining 5 types 的 between-type 差异是否仍显著？Authorization scope (41.6%) vs coreferential (31.6%) 的层级差异是否保持？\n3. TOST primary margin ±15pp 的选择依据是什么？能否提供 domain-grounded SESOI 论证（如 \"对策略合规而言，15pp 差异在部署中可接受/不可接受\"）？\n4. Table 3 中 DeepSeek 的反向效果（消歧指令反而增加违规 +2/+4 pp）有无机制解释？是否与其 zero disambiguation awareness 相关——不识别歧义的模型收到消歧指令时行为退化？\n5. Perturbation control CI 上界 13.3pp 意味着最高 39% 的主效应可能来自 surface perturbation。扩大至 n=300 (MDE ~9pp) 是否能实质性收紧因果归因？\n\n---\n\n## Missing References\n\n**需补充** [共识]:\n- Hu et al. (2025) \"Ambiguity in LLMs is a concept missing problem\" — 与 §6.3 Ambiguity Blindness 直接相关\n- Cohen, J. (1960) \"A coefficient of agreement for nominal scales\" — κ 原始文献\n- Gwet, K.L. (2014) \"Handbook of Inter-Rater Reliability\" — AC₁ 原始文献\n\n**建议考虑** [部分共识]:\n- OpenAgentSafety (ICLR 2026) — 如涉及 policy compliance 维度\n- Prompt sensitivity 文献 (e.g., EMNLP 2024 Findings) — 建立 perturbation control 与 prompt sensitivity 研究的联系\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态: 已跳过 (skipped)**。外部审稿请求已发送但用户选择不提交。本报告仅基于内部两位 Reviewer 的圆桌审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态: 已完成**。4 warnings, 6 info-level findings。\n\n主要发现：\n- **[Warning]** Pages 3–5 连续 3 页纯文本（Related Work → Taxonomy → Method），无 figure/table 打断。§3 Taxonomy 建议增加层级图或摘要表。\n- **[Warning]** Pages 8–9 连续纯文本（Error Analysis 后半 + Discussion + Conclusion + Limitations），无视觉元素。\n- **[Warning]** 末页（p.12）仅 ~35% 填充，底部大面积空白。\n- **[Warning]** 主体 9 页仅 4 个 display items（3 figures + 1 table），密度偏低。建议增加 taxonomy 汇总表或 mitigation 可视化。\n- **[Info]** Figure 1 内文字偏小；Figure 3 heatmap 建议改 figure*；Table 1 未对最优值加粗；主体正文确认延伸至第 9 页。\n\n---\n\n## Overall Assessment\n\n### 评分: 3.0 / 5 (Findings)\n\n### Rationale\n\n**C1（+34.0 pp, OR=15.1）和 C2（V=0.137, 三层层级）有压倒性统计支撑**，matched-pair causal design + perturbation control 在 agent safety benchmarking 中构成方法论贡献。这些结果足以支撑 Findings 级别发表。\n\n**但四个共识性 Must-Fix 问题共同阻碍 Conference 级别**：\n\n1. **Cross-judge confound** 使所有涉及 GPT-5.4 的跨模型比较不可靠——而 C4 和 \"canary type\" 发现正是基于跨模型比较\n2. **无 human evaluation baseline** 低于 EMNLP agent safety 社区当前标准（R-Judge/ToolEmu 均有）\n3. **Incompleteness confound** 影响 C2 顶层和 \"universally dangerous\" 核心叙事——排除后三层可能坍缩为两层\n4. **C4 仅解释 2.9% 方差**，不足以作为 primary claim 与 C1/C2 并列\n\n**论文标题 \"Differential Vulnerability Profiles Across LLM Agent Families\" 的承诺本质上依赖 C4**——如果模型间差异不是 primary finding，标题承诺就无法兑现。\n\n两位 Reviewer 均给出 **3.5 (Borderline Conference)**，并认为修复 Must-Fix 后可达 4.0。Director 综合评估后下调 0.5 至 **3.0 (Findings)**，理由：\n- 标题承诺（differential profiles）与 C4 证据强度之间存在实质性 gap\n- 缺乏 human evaluation 在 EMNLP venue 的严重性\n- Cross-judge confound 影响论文最有辨识度的发现（auth scope canary type）\n\n### 修订路径\n\n**如果作者完成以下修订，预估可达 3.5–4.0（Borderline Conference → Conference）**：\n- [ ] Human evaluation 校准数据（≥100 episodes, human-LLM κ）\n- [ ] Inter-judge calibration 或 dual-judge subsample\n- [ ] C4 降级为 exploratory，修改标题和 Abstract 措辞\n- [ ] §5.2 正文中处理 incompleteness confound（含/不含两版 C2）\n- [ ] 压缩正文至 8 页\n- [ ] 补充 missing references (Hu et al. 2025, Cohen 1960, Gwet 2014)\n\n**Confidence: 4/5**\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Opening anecdote ($200 loss from scopal ambiguity) 有效吸引读者\n- \"no existing study provides a causal, type-granularity mapping\" 是准确的 gap statement\n- Contribution 2 中 C4 不应与 C1/C2 并列——改为 \"suggestive model-specific variation\"\n- Contribution 3 应区分 input taxonomy (curated) 和 failure mode taxonomy (discovered)\n\n### §2 Related Work\n- 三个交叉领域（CL ambiguity, RE, agent safety）覆盖良好，篇幅控制恰当\n- DRIP-R 差异化讨论存在但方法论对比不够详细\n- 缺 Hu et al. (2025)、Cohen (1960)、Gwet (2014)\n\n### §3 Taxonomy\n- 两层六类组织清晰，例子具体\n- Wasow (2005) operational definition 和 vagueness 包含 (Kennedy 2007) 论证充分\n- **缺视觉呈现**——taxonomy diagram 或 summary table 对读者理解至关重要\n\n### §4 Method\n- §4.2 matched-pair 设计是全文最强方法论贡献——三条质量标准、双人审核、迭代修正\n- §4.4 cross-judge 设计：confound 应在此处正式讨论，不应推迟到 §8 Limitations\n- §4.5 perturbation control：应正式承认 CI 上界 13.3pp 的残余不确定性\n- §4.6 统计分析：Holm-Bonferroni 三个 family 清晰；C3 不通过校正 correctly noted\n\n### §5 Results\n- C1 (§5.1)：证据压倒性。Variance decomposition (clause 22.4% vs model 1.0%) 是重要洞察\n- C2 (§5.2)：统计支撑强，但 incompleteness confound 讨论必须在此处而非仅在 Limitations\n- C3 (§5.3)：inconclusive 定位诚实且论证充分\n- C4 (§5.4)：within-judge analysis for auth scope (Claude/Qwen3/DeepSeek 同由 GPT-5.4 评判) 是亮点，但 GPT-5.4 自身数据跨 judge boundary；2.9% variance 不足以支撑 primary claim\n\n### §6 Error Analysis\n- 五种 failure mode 定义清晰，跨模型一致性 (3/6 unanimous, 6/6 majority) compelling\n- 三种机制模式 (structural misparse, gap-filling, boundary violation) 提供 actionable insights\n- Ambiguity Blindness operationalization 需补充细节（\"disambiguation awareness\" vs \"surface adoption\" 编码标准）\n- LLM-only coding 无 human validation 是方法论缺口\n\n### §7 Discussion\n- \"Differential Nocuity\" 框架定位为 empirical regularity 而非 governing principle 更恰当\n- \"Canary type\" for auth scope 是最有实践价值的发现——但需 cross-judge 排除 confound\n- Practical implications 段过长——导致超页。Mitigation 结果（Appendix B）的精华应整合入此处\n\n### §8 Conclusion\n- 准确总结主要发现\n- \"22× more violation variance\" 是有力的 takeaway\n- 需压缩以确保落入 page 8\n\n### Limitations\n- 覆盖全面且诚实——model coverage, domain scope, synthetic ambiguity, cross-judge, failure mode reliability, incompleteness confound, severity threshold\n- Cross-judge 讨论应前移至 §4.4\n- Incompleteness regression 分析有信息量但不充分（token count ≠ information content）\n- Realism validation (TTR, Flesch-Kincaid, KS tests) 是好做法"
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
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "report": "# 审稿报告 — Round 3 (Fresh)\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n**Venue**: EMNLP 2026 via ARR May cycle (截止 2026-05-25)\n**Reviewers**: R1 (方法严谨性, 3.5/5), R2 (新颖性与完整性, 3.5/5)\n**Director Overall**: **3.0 / 5 (Findings)**\n\n---\n\n## Summary\n\n本文研究不同类型的策略歧义如何影响 LLM agent 的安全违规率。采用 matched-pair 设计，在 τ²-bench（零售/航空客服场景）上构造 300 对歧义/无歧义条款，覆盖六类歧义（两层 taxonomy：linguistic 层 3 类 + specification 层 3 类），评估五个模型（GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3），共 2,997 episodes。提出四个 claims：C1（歧义普遍增加 34.0pp 违规率，OR=15.1），C2（三层类型层级，Cramér's V=0.137），C3（linguistic/specification 层级区分不显著，inconclusive），C4（模型×类型交互效应）。附带 perturbation control、error analysis（614 traces, 5 failure modes）、Ambiguity Blindness 量化（<11% awareness）和消歧指令缓解实验（1,256 episodes）。\n\n---\n\n## Strengths\n\n**S1** [Consensus] **Matched-pair causal design 是方法论贡献**：perturbation control (Δ_perturb=3.33pp vs Δ_ambig=34.0pp) + TOST equivalence + variance decomposition + ICC reproducibility 的组合在 agent safety benchmarking 中几乎没有先例。论文的因果推断设计显著优于同期工作（DRIP-R: correlation only, PolicyBank: no matched design）。\n\n**S2** [Consensus] **C1 和 C2 有压倒性统计支撑**：C1 (p < 10⁻¹⁰⁵, OR=15.1, bootstrap CI [31.2, 36.9]) 和 C2 (p = 3.6 × 10⁻⁵, V=0.137, power=0.993) 的证据强度远超审稿接受阈值。variance decomposition 发现 clause identity 解释 22.4% vs model identity 仅 1.0%，是重要的实践洞察。\n\n**S3** [Consensus] **Authorization scope \"canary type\" 发现有独特实践价值**：Claude 12% vs GPT-5.4 64%（52pp 跨模型范围）直接揭示了不同 safety training 策略的差异化效果——但此结论受 cross-judge confound 影响（见 MF1）。\n\n**S4** [Consensus] **Claim 层级透明**：C3 显式标记为 inconclusive，Holm-Bonferroni 校正后 C3 不通过。logistic regression 控制 token delta 后层级项翻转。这种方法论诚实度在该领域不常见。\n\n**S5** [Consensus] **Error analysis 提供机制洞察**：三种机制模式（structural misparse, information gap-filling, boundary violation）跨越 specification/linguistic 层级边界，3/6 类型全模型一致、6/6 多数一致。Ambiguity Blindness 的量化 (<11% awareness, >88% surface adoption) 虽概念上不意外但首次在 agent safety context 中给出具体数字。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [Critical — Consensus] **Cross-judge confound 缺乏校准数据**\n\nGPT-5.4 评判 Claude/Qwen3/DeepSeek；GPT-4.1 评判 GPT-5.4。Judge identity 与 model identity 完全混淆。论文最引人注目的发现——authorization scope Claude 12% vs GPT-5.4 64%（Table 1）——跨越 judge boundary（Claude 由 GPT-5.4 评判，GPT-5.4 由 GPT-4.1 评判）。无法区分 GPT-5.4 的 vulnerability profile 是模型特性还是 GPT-4.1 检测能力差异的 artifact。论文未提供任何 inter-judge calibration 数据。Within-judge analysis 仅能确认 C1 在两个子群中一致，无法量化 judge bias 方向和大小。\n\n*R1-N3 和 R2-N2 独立识别；交叉后两人 AGREE。*\n\n**要求**: (a) 在 ≥100 episodes 上做 human evaluation 建立 LLM-human agreement baseline；(b) 和/或让 GPT-5.4 和 GPT-4.1 同时评判同一批 traces 量化 judge bias；(c) 在 §4.4 正式讨论 confound 影响。\n\n---\n\n**MF2** [Critical — Consensus] **Human evaluation baseline 完全缺失**\n\n核心指标（binary violation/no-violation + four-tier severity）的 2,997 episodes 全部由 LLM judge 产生，无任何 human-LLM agreement 数据。§4.2 的 clause pair 质量有双人审核，§6 的 failure mode 有 LLM-LLM agreement (AC₁=0.62, κ=0.52)——但论文最核心的违规判定缺乏人类校准。R-Judge (EMNLP 2024 Findings) 和 ToolEmu (ICLR 2024)——论文引用的同领域工作——均包含 human evaluation baseline。纯 LLM-as-judge 且无人类校准低于 EMNLP agent safety 的当前社区标准。\n\n*R2-N3 提出为 Must-Fix；R1 交叉后从 W2 升级同意。*\n\n**要求**: 对 ≥100 episodes（stratified by type × severity）做 human annotation，报告 human-LLM agreement (Cohen's κ)。\n\n---\n\n**MF3** [Critical — Consensus] **Incompleteness confound 未充分解决**\n\nIncompleteness 的无歧义变体必然添加新的策略信息（边界条件、例外规则），而非仅消解歧义。这违反了 §4.2 matched-pair 设计的第二条质量标准（\"eliminates that ambiguity without introducing new information that changes the policy's scope\"）。Incompleteness 驱动了 C2 三层层级的顶层（53.6%）、Systematic Nocuity 的 24% universal convergence、以及 \"universally dangerous\" 的核心叙事。论文在 Limitations 中用 token delta logistic regression 处理（β→−0.10, p=0.384 after controlling token delta），但 token count 是信息内容的极粗糙代理。一条添加全新退货排除规则的条款，其信息增量远超同等 token 数量的词汇替换。排除 incompleteness 后，5-type omnibus p=0.079（不显著），三层层级可能坍缩为两层（auth scope vs coreferential 仍显著，p_adj=0.039）。\n\n*R1-N2 提出为 Must-Fix；R2 交叉后从 W1 升级同意。*\n\n**要求**: (a) 在 §5.2 报告结果处立即讨论 confound，不得仅放 Limitations；(b) 报告含/不含 incompleteness 两版 C2 分析；(c) 考虑将 incompleteness 重新定义为 \"missing policy content\"（与其他 5 类性质不同）；(d) camera-ready 中增加 information-addition control。\n\n---\n\n**MF4** [Critical — Consensus] **C4 (model×type interaction) 作为 primary claim 证据不足**\n\nModel×type interaction 仅解释 2.9% 方差（η²=0.026）。R1 从统计角度指出效应量过小无法与 C1 (p < 10⁻¹⁰⁵) 和 C2 (V=0.137, p < 10⁻⁵) 并列为 primary claim。R2 从 framing 角度指出 Abstract \"jointly determine\" 暗示 model 和 type 贡献相当，与实际不符。\n\n*Director 对 p 值分歧的裁决*：R1 声称 F(12)=1.97, p=0.075；论文报告 F(20)=1.97, p=0.006。正确 df = (5−1)(6−1) = 20，R1 使用了错误的 df。论文报告的 p=0.006 在给定 df 下是自洽的。**但两位 Reviewer 一致认为，无论 p 值如何，2.9% 的方差解释量不足以支撑 primary claim 地位。**\n\n*R1-N1 和 R2-W5 从不同角度提出；交叉后两人 AGREE。*\n\n**要求**: (a) 将 C4 降级为 exploratory（与 C3 同级）；(b) Abstract \"jointly determine\" → \"type primarily determines severity, with a smaller but significant model×type interaction\"；(c) §1 贡献列表中不再将 C4 与 C1/C2 并列。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [Warning — Consensus] **TOST ±15pp margin 缺乏 domain-specific 依据**\n七个 margin 的敏感性分析（Appendix A）是好做法，但 primary margin ±15pp 无理论论证。基线 ~30-40% 下 ±15pp 意味着 15-55% 均为 \"等价\"——过于宽松。Lakens (2017) 要求 SESOI (Smallest Effect Size of Interest) 论证。\n\n**SF2** [Warning — Consensus] **Error analysis LLM 编码器未经人类验证**\nGwet's AC₁=0.62, Cohen's κ=0.52 为 LLM-LLM agreement，非 LLM-human。AC₁=0.62 处于 \"substantial\" 下界，minority failure modes 可靠性可能更低。§6.1-6.2 的 type-specific failure signatures 完全基于此。\n\n**SF3** [Warning — Consensus with qualification] **Perturbation control 检验力有限**\nn=120 (24/model), MDE≥15pp, CI [-5.0, 13.3]。Worst-case 下 surface perturbation 可解释 13.3/34.0 ≈ 39% 的主效应。C1 在任何合理假设下仍成立（残余效应 ≥20.7pp），但因果归因的精度受限。\n\n**SF4** [Warning — Consensus] **ICC 子集代表性不明**\n30/300 clause pairs (10%), 2/5 models (40%), ICC=0.919。未披露选择了哪 2 个模型。Cross-architecture reproducibility 声明受限。\n\n**SF5** [Warning — Consensus] **Mitigation 结果被低估**\nTable 3 (Appendix B) 包含高价值发现：DeepSeek 反向效果 (+2/+4 pp, 消歧指令反而增加违规)、Claude auth scope floor effect (Δ=0)、GPT-5.4 dramatic response (−40pp)。这些直接支撑 Differential Nocuity 的实践含义但被完全推入 appendix，§7 仅一句话提及。\n\n**SF6** [Warning — Consensus] **Taxonomy framing 不精确**\n§3 input taxonomy (6 types, curated from literature) 和 §6 output taxonomy (5 failure modes, empirically discovered) 使用相同术语 \"taxonomy\"，易混淆。§1 Contribution 3 应强调 failure mode taxonomy 为研究发现，非 input taxonomy。\n\n**SF7** [Warning — Partial Consensus] **Related Work 遗漏**\n- Hu et al. (2025) \"Ambiguity in LLMs is a concept missing problem\" — 与 §6.3 Ambiguity Blindness 直接相关 [两人同意]\n- Cohen (1960) / Gwet (2014) 统计原始文献 — κ 和 AC₁ 的引用规范 [两人同意]\n- DRIP-R 方法论对比不够详细 — 最直接的 concurrent work 应有更系统比较 [两人同意]\n- OpenAgentSafety (ICLR 2026) — 如涉及 policy compliance 维度则值得一提 [R2 提出，R1 conditional agree]\n\n**SF8** [Warning — R1 识别，R2 反驳，Director 裁决 R1 正确] **正文超过 8 页限制**\n§7 Discussion 从 page 8 延续到 page 9，§8 Conclusion 完全在 page 9。视觉审查 Agent 独立确认：\"Discussion 从 page 8 延续到 page 9，Conclusion 在 page 9 中部\"。EMNLP 2026 Long paper 正文（Abstract 到 Conclusion）严格 8 页。**R2 反驳不成立，论文超页。**\n\n---\n\n### Minor（不影响接收）\n\n- M1: 引用 minor mismatches — Lassiter & Goodman (2017 vs 2015), Levy (2008 vs 2007), ferrari_defects_2018 first author Rosadini [R1/R2 均识别，无虚构引用]\n- M2: Table 3 排除 coreferential 未解释原因\n- M3: 标题 \"LLM Agent Families\" 仅覆盖 5 个模型，\"families\" 措辞略显夸大\n- M4: \"Nocuous\" 对 EMNLP 读者可能不熟悉，首次使用时加释义\n- M5: Figure 1 内文字偏小，打印可读性可能受影响\n- M6: Figure 3 heatmap 建议改为 figure*（全宽）提升可读性\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 独立评审后在以下关键问题上达成完全共识：\n\n| 问题 | R1 | R2 | 交叉后 |\n|------|-----|-----|--------|\n| Cross-judge confound | N3 (Must-Fix) | N2 (Must-Fix) | 双方 AGREE |\n| Human eval baseline | W2 → 升级 | N3 (Must-Fix) | R1 升级同意 |\n| Incompleteness confound | N2 (Must-Fix) | W1 → 升级 | R2 升级同意 |\n| C4 降级 | N1 (Must-Fix) | W5 (Should-Fix) | 双方 AGREE (互补角度) |\n| TOST margin | W1 | AGREE | 共识 |\n| Error analysis validation | W2 | AGREE | 共识 |\n| Perturbation power | W3 | AGREE w/ qualification | 基本共识 |\n| ICC representativeness | W4 | AGREE | 共识 |\n| Mitigation underexploited | — | W2 → R1 AGREE | 共识 |\n| Taxonomy framing | — | W3 → R1 AGREE | 共识 |\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 裁决 |\n|------|-----|-----|---------------|\n| R2-N1: Abstract \"500 pairs\" | **REBUT** — 原文为 \"300\" | Must-Fix | **R1 正确，R2 事实前提错误，排除** |\n| 页数合规 (R1-W5) | Should-Fix (超页) | **REBUT** — 合规 | **R1 正确，视觉审查确认超页** |\n| C4 p-value | F(12)=1.97, p=0.075 | 论文 F(20)=1.97, p=0.006 自洽 | **R2 正确 (df=20)，但效应量结论一致** |\n| Related work 引用量 | 33 条足够 | 33 条偏少 | **R1 正确，数量非评审标准** |\n\n---\n\n## Questions for Authors\n\n1. 是否可行在 ~100 episodes 上做 dual-judge evaluation (GPT-5.4 + GPT-4.1 评判同一批 traces)？如果 GPT-4.1 对 GPT-5.4 系统性偏严/偏松，C4 中 GPT-5.4 的 vulnerability profile 结论如何修正？\n2. 排除 incompleteness 后，remaining 5 types 的 between-type 差异是否仍显著？Authorization scope (41.6%) vs coreferential (31.6%) 的层级差异是否保持？\n3. TOST primary margin ±15pp 的选择依据是什么？能否提供 domain-grounded SESOI 论证（如 \"对策略合规而言，15pp 差异在部署中可接受/不可接受\"）？\n4. Table 3 中 DeepSeek 的反向效果（消歧指令反而增加违规 +2/+4 pp）有无机制解释？是否与其 zero disambiguation awareness 相关——不识别歧义的模型收到消歧指令时行为退化？\n5. Perturbation control CI 上界 13.3pp 意味着最高 39% 的主效应可能来自 surface perturbation。扩大至 n=300 (MDE ~9pp) 是否能实质性收紧因果归因？\n\n---\n\n## Missing References\n\n**需补充** [共识]:\n- Hu et al. (2025) \"Ambiguity in LLMs is a concept missing problem\" — 与 §6.3 Ambiguity Blindness 直接相关\n- Cohen, J. (1960) \"A coefficient of agreement for nominal scales\" — κ 原始文献\n- Gwet, K.L. (2014) \"Handbook of Inter-Rater Reliability\" — AC₁ 原始文献\n\n**建议考虑** [部分共识]:\n- OpenAgentSafety (ICLR 2026) — 如涉及 policy compliance 维度\n- Prompt sensitivity 文献 (e.g., EMNLP 2024 Findings) — 建立 perturbation control 与 prompt sensitivity 研究的联系\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态: 已跳过 (skipped)**。外部审稿请求已发送但用户选择不提交。本报告仅基于内部两位 Reviewer 的圆桌审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态: 已完成**。4 warnings, 6 info-level findings。\n\n主要发现：\n- **[Warning]** Pages 3–5 连续 3 页纯文本（Related Work → Taxonomy → Method），无 figure/table 打断。§3 Taxonomy 建议增加层级图或摘要表。\n- **[Warning]** Pages 8–9 连续纯文本（Error Analysis 后半 + Discussion + Conclusion + Limitations），无视觉元素。\n- **[Warning]** 末页（p.12）仅 ~35% 填充，底部大面积空白。\n- **[Warning]** 主体 9 页仅 4 个 display items（3 figures + 1 table），密度偏低。建议增加 taxonomy 汇总表或 mitigation 可视化。\n- **[Info]** Figure 1 内文字偏小；Figure 3 heatmap 建议改 figure*；Table 1 未对最优值加粗；主体正文确认延伸至第 9 页。\n\n---\n\n## Overall Assessment\n\n### 评分: 3.0 / 5 (Findings)\n\n### Rationale\n\n**C1（+34.0 pp, OR=15.1）和 C2（V=0.137, 三层层级）有压倒性统计支撑**，matched-pair causal design + perturbation control 在 agent safety benchmarking 中构成方法论贡献。这些结果足以支撑 Findings 级别发表。\n\n**但四个共识性 Must-Fix 问题共同阻碍 Conference 级别**：\n\n1. **Cross-judge confound** 使所有涉及 GPT-5.4 的跨模型比较不可靠——而 C4 和 \"canary type\" 发现正是基于跨模型比较\n2. **无 human evaluation baseline** 低于 EMNLP agent safety 社区当前标准（R-Judge/ToolEmu 均有）\n3. **Incompleteness confound** 影响 C2 顶层和 \"universally dangerous\" 核心叙事——排除后三层可能坍缩为两层\n4. **C4 仅解释 2.9% 方差**，不足以作为 primary claim 与 C1/C2 并列\n\n**论文标题 \"Differential Vulnerability Profiles Across LLM Agent Families\" 的承诺本质上依赖 C4**——如果模型间差异不是 primary finding，标题承诺就无法兑现。\n\n两位 Reviewer 均给出 **3.5 (Borderline Conference)**，并认为修复 Must-Fix 后可达 4.0。Director 综合评估后下调 0.5 至 **3.0 (Findings)**，理由：\n- 标题承诺（differential profiles）与 C4 证据强度之间存在实质性 gap\n- 缺乏 human evaluation 在 EMNLP venue 的严重性\n- Cross-judge confound 影响论文最有辨识度的发现（auth scope canary type）\n\n### 修订路径\n\n**如果作者完成以下修订，预估可达 3.5–4.0（Borderline Conference → Conference）**：\n- [ ] Human evaluation 校准数据（≥100 episodes, human-LLM κ）\n- [ ] Inter-judge calibration 或 dual-judge subsample\n- [ ] C4 降级为 exploratory，修改标题和 Abstract 措辞\n- [ ] §5.2 正文中处理 incompleteness confound（含/不含两版 C2）\n- [ ] 压缩正文至 8 页\n- [ ] 补充 missing references (Hu et al. 2025, Cohen 1960, Gwet 2014)\n\n**Confidence: 4/5**\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Opening anecdote ($200 loss from scopal ambiguity) 有效吸引读者\n- \"no existing study provides a causal, type-granularity mapping\" 是准确的 gap statement\n- Contribution 2 中 C4 不应与 C1/C2 并列——改为 \"suggestive model-specific variation\"\n- Contribution 3 应区分 input taxonomy (curated) 和 failure mode taxonomy (discovered)\n\n### §2 Related Work\n- 三个交叉领域（CL ambiguity, RE, agent safety）覆盖良好，篇幅控制恰当\n- DRIP-R 差异化讨论存在但方法论对比不够详细\n- 缺 Hu et al. (2025)、Cohen (1960)、Gwet (2014)\n\n### §3 Taxonomy\n- 两层六类组织清晰，例子具体\n- Wasow (2005) operational definition 和 vagueness 包含 (Kennedy 2007) 论证充分\n- **缺视觉呈现**——taxonomy diagram 或 summary table 对读者理解至关重要\n\n### §4 Method\n- §4.2 matched-pair 设计是全文最强方法论贡献——三条质量标准、双人审核、迭代修正\n- §4.4 cross-judge 设计：confound 应在此处正式讨论，不应推迟到 §8 Limitations\n- §4.5 perturbation control：应正式承认 CI 上界 13.3pp 的残余不确定性\n- §4.6 统计分析：Holm-Bonferroni 三个 family 清晰；C3 不通过校正 correctly noted\n\n### §5 Results\n- C1 (§5.1)：证据压倒性。Variance decomposition (clause 22.4% vs model 1.0%) 是重要洞察\n- C2 (§5.2)：统计支撑强，但 incompleteness confound 讨论必须在此处而非仅在 Limitations\n- C3 (§5.3)：inconclusive 定位诚实且论证充分\n- C4 (§5.4)：within-judge analysis for auth scope (Claude/Qwen3/DeepSeek 同由 GPT-5.4 评判) 是亮点，但 GPT-5.4 自身数据跨 judge boundary；2.9% variance 不足以支撑 primary claim\n\n### §6 Error Analysis\n- 五种 failure mode 定义清晰，跨模型一致性 (3/6 unanimous, 6/6 majority) compelling\n- 三种机制模式 (structural misparse, gap-filling, boundary violation) 提供 actionable insights\n- Ambiguity Blindness operationalization 需补充细节（\"disambiguation awareness\" vs \"surface adoption\" 编码标准）\n- LLM-only coding 无 human validation 是方法论缺口\n\n### §7 Discussion\n- \"Differential Nocuity\" 框架定位为 empirical regularity 而非 governing principle 更恰当\n- \"Canary type\" for auth scope 是最有实践价值的发现——但需 cross-judge 排除 confound\n- Practical implications 段过长——导致超页。Mitigation 结果（Appendix B）的精华应整合入此处\n\n### §8 Conclusion\n- 准确总结主要发现\n- \"22× more violation variance\" 是有力的 takeaway\n- 需压缩以确保落入 page 8\n\n### Limitations\n- 覆盖全面且诚实——model coverage, domain scope, synthetic ambiguity, cross-judge, failure mode reliability, incompleteness confound, severity threshold\n- Cross-judge 讨论应前移至 §4.4\n- Incompleteness regression 分析有信息量但不充分（token count ≠ information content）\n- Realism validation (TTR, Flesch-Kincaid, KS tests) 是好做法"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-21T06:59:02.130823+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4473
}
```

</details>

---


### Assistant

_source line 268 · 2026-05-21T06:59:10.258251+00:00_

审稿报告已投递给 Research Director。

---

**Round 3 (Fresh) 审稿完成。**

**最终评分：3.0 / 5 (Findings)**

核心判断：
- **C1 (+34.0pp, OR=15.1) 和 C2 (V=0.137) 有压倒性支撑**——matched-pair causal design 是方法论贡献，足以支撑 Findings
- **4 个共识性 Must-Fix 阻碍 Conference**：cross-judge confound、无 human evaluation、incompleteness confound、C4 overclaimed
- **论文标题承诺 "Differential Vulnerability Profiles" 依赖 C4（仅 2.9% variance）**——证据不足以兑现标题

修订路径清晰：human evaluation + inter-judge calibration + C4 降级 + incompleteness 处理 + 压缩页数，可达 3.5–4.0。

Issue Tracker 已同步更新至 `review_issues.yaml`（4 critical, 8 warning, 4 info, 4 resolved）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 24

## Round 24

2 recorded events


### User

_source line 269 · 2026-05-21T06:59:12.987577+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 8 个 Must-Fix/Should-Fix 点和 2 个 Missing References 点逐条回应完毕：

- **3 个 AGREE**（R1-N2 incompleteness confound、R1-N3 cross-judge confound、R1-W2 error analysis reliability）
- **3 个 AGREE with nuance/qualification**（R1-N1 C4 overclaiming — 同意效应量问题但质疑 R1 声称的 p=0.075、R1-W3 perturbation power — 同意 CI 宽但 worst-case 下 C1 仍成立、R1-W4 ICC 代表性）
- **1 个 REBUT**（R1-W5 页数超限 — §8 Conclusion 完全在 page 8 内，Limitations 不计入页数）
- **1 个 AGREE**（R1-W1 TOST margin — 缺理论依据但 sensitivity analysis 部分缓解）

两位 reviewer 独立汇聚于三个核心问题：cross-judge confound、incompleteness confound、C4 overclaiming。

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

_source line 270 · 2026-05-21T06:59:24.971664+00:00_

审稿报告已投递至 Research Director。

**审稿完成总结**：

- **Overall: 3.0 / 5 (Findings)**
- **4 个 Must-Fix**（共识）：Cross-judge confound 无校准 | Human evaluation baseline 缺失 | Incompleteness confound 未解决 | C4 overclaimed as primary
- **8 个 Should-Fix**：TOST margin 无依据 | Error analysis 无人类验证 | Perturbation control 欠power | ICC 子集不透明 | Mitigation 结果被低估 | Taxonomy framing 混淆 | Related Work 遗漏 | 正文超 8 页
- **外部审稿**：已跳过
- **视觉审查**：已完成（4 warnings — 纯文本段落过长、display item 密度低）
- **Issue Tracker**：已同步更新至 `review_issues.yaml`

两位 Reviewer 均给出 3.5 (Borderline Conference)。Director 下调 0.5 至 3.0 (Findings)，核心理由：论文标题承诺 "Differential Vulnerability Profiles" 依赖 C4（仅 2.9% variance），而 cross-judge confound 使模型间对比不可靠。修复 Must-Fix 后预估可达 3.5–4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 25

## Round 25

44 recorded events


### User

_source line 271 · 2026-05-21T07:51:46.624523+00:00_

[Round 3 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/policy_ambiguity_safety/artifacts/review_reports/round_2.md`
跨轮次问题追踪: `projects/policy_ambiguity_safety/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-05-25

请继续审稿流程。

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

_source line 272 · 2026-05-21T07:52:03.900659+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "review_reports/round_2.md",
  "max_chars": "0"
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
    "file": "review_reports/round_2.md",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-21T07:52:05.306203+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_reports/round_2.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-21T07:52:05.457373+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>&1",
  "description": "Read current review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>&1",
    "description": "Read current review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-21T07:52:05.659137+00:00_

## Round 3 (Fresh) Review Issues — policy_ambiguity_safety
## Paper: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
## Venue: EMNLP 2026 via ARR May cycle
## Date: 2026-05-21 (Round 3 fresh review)
## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)

# ============================================================
# CRITICAL ISSUES (Must-Fix) — Consensus
# ============================================================

- id: "MF1"
  summary: "Cross-judge confound 缺乏校准数据 — judge identity 与 model identity 完全混淆，所有涉及 GPT-5.4 的跨模型比较不可靠"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 3
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "First identified in Round 1"
    - round: 2
      reviewers: [1, 2]
      note: "Both confirmed. Plan_009 human eval proposed but not completed."
    - round: 3
      reviewers: [1, 2]
      note: "[CONSENSUS] R1-N3 and R2-N2 independently identified. Auth scope Claude 12% vs GPT-5.4 64% crosses judge boundary."
  action_items:
    - round: 3
      action: "Dual-judge experiment: 100 episodes (60 GPT-5.4 + 40 others), GPT-5.4 + GPT-4.1 evaluate same traces, quantify judge bias. §4.4 cross-judge calibration discussion."
      assigned_to: "Main Agent"
      status: in_progress
    - round: 3
      action: "Human evaluation ≥100 episodes — merged with MF2, blocked on user arranging annotators"
      assigned_to: "User"
      status: open
  resolution: ""
  resolution_round: null

- id: "MF2"
  summary: "Human evaluation baseline 完全缺失 — 核心 violation assessment (2,997 episodes) 纯 LLM-as-judge，无 human-LLM agreement 数据"
  category: method
  severity: critical
  status: open
  first_raised_round: 3
  last_seen_round: 3
  mentions:
    - round: 2
      reviewers: [1]
      note: "R1-W2 flagged error analysis LLM coders lacked human validation."
    - round: 3
      reviewers: [1, 2]
      note: "[CONSENSUS] R2-N3 Must-Fix, R1 upgraded. R-Judge/ToolEmu both include
…[truncated 7413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-21T07:52:19.561900+00:00_

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

_source line 277 · 2026-05-21T07:52:20.064214+00:00_

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
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
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
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-21T07:52:20.064582+00:00_

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

_source line 279 · 2026-05-21T07:52:20.516494+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type, two-layer ambiguity taxonomy, evaluated across five architecturally diverse models (2,997 episodes). Ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. A three-tier type hierarchy emerges (Cram\'{e}r's $V = 0.137$, $p < 10^{-4}$): incompleteness---whose top-tier position partly reflects an information-addition confound (\S\ref{sec:results})---is universally dangerous (46--62\% across models), while authorization scope varies 52 pp depending on the model (12\% for Claude to 64\% for GPT-5.4), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, with over 88\% surface adoption. Our Differential Nocuity framework connects type-specific vulnerability to disambiguation channel availability and suggests both type-aware policy auditing and externalized ambiguity detection for deployed systems.
3	\end{abstract}
4	

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

_source line 280 · 2026-05-21T07:52:20.668567+00:00_

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

_source line 281 · 2026-05-21T07:52:20.719304+00:00_

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
…[truncated 2516 chars]

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

_source line 282 · 2026-05-21T07:52:20.970707+00:00_

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

_source line 283 · 2026-05-21T07:52:21.073399+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers, drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on two criteria: frequency in operational policy documents (assessed via manual audit of $\tau^2$-bench policies) and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by parsing or contextual cues within the text.
9	\begin{itemize}
10	\item \textbf{Scopal}: quantifier, negation, or modal scope interactions (e.g., ``all items may not be returned'' admits universal-negation and negation-of-universal readings).
11	\item \textbf{Lexical}: polysemy or homonymy (e.g., ``charge'' as financial cost vs.\ penalty; ``party'' as individual vs.\ group).
12	\item \textbf{Coreferential}: unclear pronoun or noun-phrase reference (e.g., ``the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor'' where ``which'' could refer to the verification or the refund).
13	\end{itemize}
14	
15	\paragraph{Specification layer.} These types arise from pragmatic or discourse-level gaps that require domain knowledge or organizational context to resolve.
16	\begin{itemize}
17	\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue r
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-21T07:52:24.938374+00:00_

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

_source line 285 · 2026-05-21T07:52:25.440831+00:00_

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
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background). Each annotator independently verified the three quality criteria; rejected or modified pairs were iteratively revised until both annotators confirmed compliance. For each type, we identify policy clauses in $\tau^2$-bench that are naturally susceptible to the target ambiguity, then construct the ambiguous and unambiguous variants. All pairs are reviewed to ensure (1) the ambiguous variant contains exactly one instance of the target ambiguity type, (2) the unambiguous variant eliminates that ambiguity without introducing new information that changes the policy's scope, and (3) the ambig
…[truncated 4709 chars]

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

_source line 286 · 2026-05-21T07:52:25.441321+00:00_

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

_source line 287 · 2026-05-21T07:52:25.893447+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, Mantel--Haenszel OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$; bootstrap 95\% CI for $\Delta$: $[31.2, 36.9]$ pp). Of 1,497 matched pairs, the discordant ratio is 15.1:1 (544 ambiguous-only vs.\ 36 unambiguous-only violations). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). The perturbation control ($n = 120$) yields $\Delta_{\text{perturb}} = 3.33$ pp (95\% CI $[-5.0, +13.33]$, containing zero), confirming specificity to semantic ambiguity. Results replicate under an alternative severity threshold ($\Delta = 38.2$ pp; Appendix~\ref{app:severity}). Clause identity explains 22.4\% of variance versus 1.0\% for model identity.
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{speccolor}{Spec.}} & Incompleteness & 53.6 & 46.0 & 58.0 & 48.0 & 62.0 & 54.0 & +49.2 & $<10^{-37}$ \\
22	 & Auth.\ Scope &
…[truncated 5355 chars]

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

_source line 288 · 2026-05-21T07:52:25.893921+00:00_

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

_source line 289 · 2026-05-21T07:52:26.847949+00:00_

1	\section{Error Analysis}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from the coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}; the gap reflects the prevalence paradox, as three categories account for ${\sim}$90\% of instances).
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary. \emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling human garden-path processing \citep{frazier_rayner_1982} and the good-enough framework \citep{ferreira_good_enough_2002}. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5). \emph{Information gap-filling} (assumption-based action): the agent fills missing or ambiguous information with plausible but incorrect defaults. This dominates incompleteness (3/5) and lexical (3/5). \emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified. This dominates authorization scope exclusively (all 5 models).
11	
12	Each type's dominant failure mode is majority-consistent ($\geq$3/5 models agree), with three types achieving full unanimity (authorization scope, conditional precedence, scopal). Per-model validation on GPT-5.4 and GPT-4.1 confirms five of six types share the same dominant mode across both models. The layer dis
…[truncated 1604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-21T07:52:26.848415+00:00_

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

_source line 291 · 2026-05-21T07:52:27.300364+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential Nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity by stakeholder divergence. Our results extend this to LLM agents: all six types are nocuous ($+34.0$ pp), but type primarily determines severity (22:1 clause-vs.-model variance ratio). We propose \emph{Differential Nocuity}: the risk of a policy ambiguity depends on type, safety training, and disambiguation channel availability. The 41.3\% majority-convergent violation rate (\emph{systematic nocuity}, \S\ref{sec:analysis}) suggests shared failure modes across architectures that make errors invisible in agreement-based evaluation.
6	
7	\paragraph{Safety training selectivity.}
8	The exploratory model$\times$type interaction (C4) suggests that safety training does not uniformly reduce ambiguity vulnerability. Incompleteness is universally dangerous (46--62\%) because the agent never encounters a decision point that RLHF refusal mechanisms can intercept, instead filling gaps with plausible defaults \citep{ferreira_good_enough_2002,ferreira_patson_2007}. Authorization scope involves explicit boundary reasoning that directly engages harm-avoidance objectives, making it a canary type: Claude's 12\% rate (vs.\ 60\% for DeepSeek) is consistent with training that targets permission-boundary violations (\S\ref{sec:c4}).
9	
10	\paragraph{Practical implications.}
11	Policy auditing should be \emph{type-aware}, prioritizing incompleteness and authorization scope. A mitigation experiment (1,256 episodes, five types; Appendix~\ref{app:mitigation}) shows that type-specific disambiguation instructions reduce violations by 8.5 pp overall, with authorization scope benefiting most ($\Delta = -18.0$ pp) and incompleteness least ($\Delta = -3.4$ pp). Claude shows zero authorization-scope reduction (baseline already 12\%), confirming its safety training already provides this capability. With $<$11\% self-awareness, agents cannot f
…[truncated 118 chars]

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

_source line 292 · 2026-05-21T07:52:27.351071+00:00_

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

_source line 293 · 2026-05-21T07:52:27.853449+00:00_

1	\section{Conclusion}
2	
3	We present the first causal study of how policy ambiguity type affects safety violations in LLM agents. Across 2,997 episodes and five models, ambiguous clauses increase violations by 34.0 pp (OR $= 15.1$), with clause identity explaining 22$\times$ more variance than model identity. A three-tier type hierarchy and exploratory model$\times$type interaction reveal that authorization scope is a model-differentiating canary type (12--64\%) while incompleteness is a universal blind spot (46--62\%). With $<$11\% disambiguation awareness, type-aware policy auditing and externalized ambiguity detection are critical for deployed agent systems.
4	

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

_source line 294 · 2026-05-21T07:52:27.853800+00:00_

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

_source line 295 · 2026-05-21T07:52:28.105028+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Model coverage.} We evaluate five API-accessible models (three proprietary, two open-source). Smaller open-source models (7B--70B parameters) may show different vulnerability patterns, and our findings may not generalize to models with fundamentally different training approaches.
5	
6	\paragraph{Domain scope.} $\tau^2$-bench covers retail and airline customer service. Policy ambiguity effects in other domains (healthcare, finance, legal) remain to be tested, though the within-study cross-domain consistency is encouraging: failure mode distributions share the same top-two modes (assumption-based action and unauthorized escalation) across domains, with individual mode base rates differing by up to 12.5 pp, likely reflecting domain policy structure rather than methodological artifacts.
7	
8	\paragraph{Synthetic ambiguity.} Our matched-pair design requires synthetic construction of ambiguous variants, which may not capture the full distribution of naturally occurring policy ambiguities. We mitigate this through expert review and a realism validation comparing ambiguous clauses against original $\tau^2$-bench policy text. Ambiguous clauses are indistinguishable from originals in lexical diversity (TTR, KS $p = 0.89$) and word length ($p = 0.09$). Readability is slightly higher (Flesch--Kincaid $d = 0.29$, $p = 0.006$) and sentence length moderately higher ($d = 0.74$), both reflecting the structural demands of encoding ambiguity in standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch--Kincaid $d = 0.14$, $p = 0.10$), confirming that minimal edits change semantic precision without altering linguistic register.
9	
10	\paragraph{Cross-judge asymmetry.} Although our dual-judge calibration (\S\ref{sec:method}) shows no systematic bias ($p = 0.606$), each agent model is evaluated by a single cross-judge, so judge identity remains confounded with model identity. Within-judge-gro
…[truncated 1580 chars]

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

_source line 296 · 2026-05-21T07:52:28.105495+00:00_

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

_source line 297 · 2026-05-21T07:52:28.155986+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, a finding that parallels our observation that LLM agents adopt surface interpretations of ambiguous policy clauses. \citet{frazier_rayner_1982} demonstrate that readers commit to a single syntactic parse early and backtrack upon disambiguation failure, while \citet{levy_expectation_2008} formalizes this as expectation-based processing. \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit human-like garden-path effects, and \citet{poesio_artstein_2005} formalize genuine ambiguity in anaphoric annotation as inherent rather than resolvable. \citet{las
…[truncated 2179 chars]

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

_source line 298 · 2026-05-21T07:52:33.727780+00:00_

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

_source line 299 · 2026-05-21T07:52:34.229918+00:00_

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
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). The treatment appends a type-specific disambiguation instruction to the agent's system prompt. Control rates are the matched 5-type subset from the full study (\S\ref{sec:results}).
30	
31	\begin{table*}[!ht]
32	\centering
33	\small
34	\caption{Violation rate change ($\Delta$pp) after adding type-specific disambiguation instructions. Negative values indicate reduction. Baseline violation rates are shown in parentheses. Coreferential was 
…[truncated 1814 chars]

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

_source line 300 · 2026-05-21T07:52:34.230339+00:00_

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

_source line 301 · 2026-05-21T07:52:34.933343+00:00_

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
…[truncated 10008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-21T07:52:34.933876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
  "pages": "1-9"
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
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-21T07:52:35.590869+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf (379.8KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-21T07:55:06.004206+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "4"
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
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-21T07:55:06.054917+00:00_



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

_source line 306 · 2026-05-21T07:55:47.614519+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 4 Continue Review — Reviewer 1\n\n**角色**：方法严谨性 + 实验设计\n**模式**：继续审稿（Round 3 → Round 4），逐条核查修改是否充分\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n### Venue\nEMNLP 2026 via ARR May cycle。Long paper，主文 8 页限制（references 不限，mandatory Limitations 不计入页数）。双盲。\n\n### 你的任务\n\n论文已根据 Round 3 审稿意见做了修改。请逐条核查以下 open/in_progress issue，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时关注修改是否引入新问题。\n\n---\n\n### Must-Fix Issues（Critical）\n\n**MF1 — Cross-judge confound（in_progress）**\nRound 3 问题：每个 agent 只有一个 judge，judge identity 与 model identity 完全混淆。\n已知修改：§4.4 新增 cross-judge calibration 段落（100 episodes dual-judge，McNemar p=0.606，binary κ=0.653，weighted κ_w=0.775）。\n**请核查**：(1) 这个 LLM-LLM calibration 是否充分回应了 confound 担忧？(2) 没有 human-LLM agreement 是否仍然是重大缺陷？(3) calibration 实验设计是否有漏洞（样本量100够不够、stratification 是否合理）？\n\n**MF2 — Human evaluation baseline（open）**\nRound 3 问题：所有评估（violation判定 + failure mode coding）均为 LLM-only，无 human agreement baseline。\n已知状态：论文未新增 human evaluation 数据。Limitations 中提到 \"Human validation of the coding scheme would further strengthen these findings\"。\n**请核查**：这是否仍然是 EMNLP 2026 接收的 blocking issue？还是 cross-judge calibration（MF1）已经足够缓解？\n\n**MF3 — Incompleteness confound（in_progress）**\nRound 3 问题：incompleteness 的 unambiguous variant 增加了政策内容（information asymmetry），effect 被高估。\n已知修改：(1) §3 taxonomy 定义处加了 confound note；(2) §5.2 新增 inline 讨论，含 logistic regression controlling for info delta（p=0.022, coefficient change <8%）和 coreferential lower-bound 分析。\n**请核查**：inline 处理是否充分？logistic regression 控制是否合理？\"upper bound\" framing 是否恰当？\n\n**MF4 — C4 overclaiming（in_progress）**\nRound 3 问题：model×type interaction 仅解释 2.9% variance，但 title/abstract/conclusion 表述过强。\n已知修改：(1) 标题改为 \"Type-Specific Safety Risks for LLM Agents\"；(2) §5.4 标题加 \"[Exploratory]\"；(3) Abstract 改为 \"2.9% of variance\"；(4) Conclusion 标注 \"exploratory\"。\n**请核查**：downgrade 是否彻底？是否仍有残留 overclaiming？\n\n---\n\n### Should-Fix Issues（Warning）\n\n**SF1 — TOST margin justification（in_progress）**\n已知修改：§4.6 新增 SESOI justification，linking ±15pp to perturbation control CI upper bound (13.3pp)。\n**请核查**：justification 是否 convincing？\n\n**SF2 — Error analysis human validation（open）**\nRound 3 问题：failure mode coding 全由 LLM 完成（Gwet AC1=0.62, Cohen κ=0.52），minority categories κ 低（arbitrary rule selection κ=0.29）。\n已知状态：Limitations 承认但未新增 human validation。\n**请核查**：是否仍需标注？\n\n**SF3 — Perturbation control power（in_progress）**\n已知修改：§4.5 新增 worst-case analysis（CI upper bound 13.3pp accounts for at most 39% of observed effect, residual ≥20.7pp）。\n**请核查**：acknowledgment 是否充分？\n\n**SF4 — ICC replication model selection（open）**\nRound 3 问题：30 clause pairs × 2 models 的 ICC=0.919，但未披露选了哪 2 个 model。\n**请核查**：§4.5 是否现在披露了 model selection？\n\n**SF5 — Mitigation in Discussion（in_progress）**\n已知修改：§7 Discussion 的 Practical Implications 段落更突出 mitigation 结果。\n**请核查**：是否充分？\n\n**SF6 — Taxonomy framing（in_progress）**\nRound 3 问题：§6 failure mode taxonomy 与 §3 input ambiguity taxonomy 易混淆。\n已知修改：§6 开头新增 \"distinct from the input ambiguity taxonomy (§3)\"。\n**请核查**：是否清晰？\n\n**SF7 — Missing references（in_progress）**\nRound 3 问题：缺 Cohen(1960)、Gwet(2014)、Hu et al.(2025)。\n已知修改：三篇均已加入 references.bib。\n**请核查**：bib 条目是否完整正确？\n\n**SF8 — Page limit（in_progress）**\nRound 3 问题：主文溢出到第 9 页。\n已知修改：Discussion 和 Conclusion 压缩。\n**请核查**：PDF 中主文是否在 8 页内（References/Limitations 不计）？\n\n---\n\n### 输出格式\n\n```\n## Issue Checklist\n- MF1: [RESOLVED/STILL_OPEN] — 理由\n- MF2: [RESOLVED/STILL_OPEN] — 理由\n...\n\n## New Issues (if any)\n- [NEW-1] ...\n\n## Score Recommendation\nOverall: X/5 (EMNLP 2026 scale)\n与 Round 3 相比的变化理由。\n```",
  "reviewer_id": "1",
  "round_number": "4",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
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
    "text": "## Round 4 Continue Review — Reviewer 1\n\n**角色**：方法严谨性 + 实验设计\n**模式**：继续审稿（Round 3 → Round 4），逐条核查修改是否充分\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n### Venue\nEMNLP 2026 via ARR May cycle。Long paper，主文 8 页限制（references 不限，mandatory Limitations 不计入页数）。双盲。\n\n### 你的任务\n\n论文已根据 Round 3 审稿意见做了修改。请逐条核查以下 open/in_progress issue，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时关注修改是否引入新问题。\n\n---\n\n### Must-Fix Issues（Critical）\n\n**MF1 — Cross-judge confound（in_progress）**\nRound 3 问题：每个 agent 只有一个 judge，judge identity 与 model identity 完全混淆。\n已知修改：§4.4 新增 cross-judge calibration 段落（100 episodes dual-judge，McNemar p=0.606，binary κ=0.653，weighted κ_w=0.775）。\n**请核查**：(1) 这个 LLM-LLM calibration 是否充分回应了 confound 担忧？(2) 没有 human-LLM agreement 是否仍然是重大缺陷？(3) calibration 实验设计是否有漏洞（样本量100够不够、stratification 是否合理）？\n\n**MF2 — Human evaluation baseline（open）**\nRound 3 问题：所有评估（violation判定 + failure mode coding）均为 LLM-only，无 human agreement baseline。\n已知状态：论文未新增 human evaluation 数据。Limitations 中提到 \"Human validation of the coding scheme would further strengthen these findings\"。\n**请核查**：这是否仍然是 EMNLP 2026 接收的 blocking issue？还是 cross-judge calibration（MF1）已经足够缓解？\n\n**MF3 — Incompleteness confound（in_progress）**\nRound 3 问题：incompleteness 的 unambiguous variant 增加了政策内容（information asymmetry），effect 被高估。\n已知修改：(1) §3 taxonomy 定义处加了 confound note；(2) §5.2 新增 inline 讨论，含 logistic regression controlling for info delta（p=0.022, coefficient change <8%）和 coreferential lower-bound 分析。\n**请核查**：inline 处理是否充分？logistic regression 控制是否合理？\"upper bound\" framing 是否恰当？\n\n**MF4 — C4 overclaiming（in_progress）**\nRound 3 问题：model×type interaction 仅解释 2.9% variance，但 title/abstract/conclusion 表述过强。\n已知修改：(1) 标题改为 \"Type-Specific Safety Risks for LLM Agents\"；(2) §5.4 标题加 \"[Exploratory]\"；(3) Abstract 改为 \"2.9% of variance\"；(4) Conclusion 标注 \"exploratory\"。\n**请核查**：downgrade 是否彻底？是否仍有残留 overclaiming？\n\n---\n\n### Should-Fix Issues（Warning）\n\n**SF1 — TOST margin justification（in_progress）**\n已知修改：§4.6 新增 SESOI justification，linking ±15pp to perturbation control CI upper bound (13.3pp)。\n**请核查**：justification 是否 convincing？\n\n**SF2 — Error analysis human validation（open）**\nRound 3 问题：failure mode coding 全由 LLM 完成（Gwet AC1=0.62, Cohen κ=0.52），minority categories κ 低（arbitrary rule selection κ=0.29）。\n已知状态：Limitations 承认但未新增 human validation。\n**请核查**：是否仍需标注？\n\n**SF3 — Perturbation control power（in_progress）**\n已知修改：§4.5 新增 worst-case analysis（CI upper bound 13.3pp accounts for at most 39% of observed effect, residual ≥20.7pp）。\n**请核查**：acknowledgment 是否充分？\n\n**SF4 — ICC replication model selection（open）**\nRound 3 问题：30 clause pairs × 2 models 的 ICC=0.919，但未披露选了哪 2 个 model。\n**请核查**：§4.5 是否现在披露了 model selection？\n\n**SF5 — Mitigation in Discussion（in_progress）**\n已知修改：§7 Discussion 的 Practical Implications 段落更突出 mitigation 结果。\n**请核查**：是否充分？\n\n**SF6 — Taxonomy framing（in_progress）**\nRound 3 问题：§6 failure mode taxonomy 与 §3 input ambiguity taxonomy 易混淆。\n已知修改：§6 开头新增 \"distinct from the input ambiguity taxonomy (§3)\"。\n**请核查**：是否清晰？\n\n**SF7 — Missing references（in_progress）**\nRound 3 问题：缺 Cohen(1960)、Gwet(2014)、Hu et al.(2025)。\n已知修改：三篇均已加入 references.bib。\n**请核查**：bib 条目是否完整正确？\n\n**SF8 — Page limit（in_progress）**\nRound 3 问题：主文溢出到第 9 页。\n已知修改：Discussion 和 Conclusion 压缩。\n**请核查**：PDF 中主文是否在 8 页内（References/Limitations 不计）？\n\n---\n\n### 输出格式\n\n```\n## Issue Checklist\n- MF1: [RESOLVED/STILL_OPEN] — 理由\n- MF2: [RESOLVED/STILL_OPEN] — 理由\n...\n\n## New Issues (if any)\n- [NEW-1] ...\n\n## Score Recommendation\nOverall: X/5 (EMNLP 2026 scale)\n与 Round 3 相比的变化理由。\n```",
    "reviewer_id": "1",
    "round_number": "4",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
````

</details>

---


### Tool result

_source line 307 · 2026-05-21T07:56:07.609451+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19994
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-21T07:56:09.015650+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 4 Continue Review — Reviewer 2\n\n**角色**：新颖性 + 完整性 + 写作质量\n**模式**：继续审稿（Round 3 → Round 4），逐条核查修改是否充分\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n### Venue\nEMNLP 2026 via ARR May cycle。Long paper，主文 8 页限制（references 不限，mandatory Limitations 不计入页数）。双盲。\n\n### 你的任务\n\n论文已根据 Round 3 审稿意见做了修改。请逐条核查以下 open/in_progress issue，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时关注修改是否引入新问题。\n\n---\n\n### Must-Fix Issues（Critical）\n\n**MF1 — Cross-judge confound（in_progress）**\nRound 3 问题：每个 agent 只有一个 judge，judge identity 与 model identity 完全混淆。\n已知修改：§4.4 新增 cross-judge calibration 段落（100 episodes dual-judge，McNemar p=0.606，binary κ=0.653，weighted κ_w=0.775）。\n**请核查**：(1) 这个 calibration 是否有效缓解 confound？(2) 100 个 episode 的 sample size 是否足够？(3) 文中对 authorization scope κ=0.385 的讨论是否充分？\n\n**MF2 — Human evaluation baseline（open）**\nRound 3 问题：所有评估均为 LLM-only，无 human agreement baseline。\n已知状态：未新增 human evaluation。\n**请核查**：从 novelty/completeness 角度，这是否是 acceptance-blocking？论文的 Limitations 承认是否足够？\n\n**MF3 — Incompleteness confound（in_progress）**\nRound 3 问题：incompleteness 的 unambiguous variant 增加政策内容。\n已知修改：§3 confound note + §5.2 logistic regression + coreferential lower-bound。\n**请核查**：(1) \"upper bound\" framing 是否准确？(2) logistic regression 是否是正确的控制方法？(3) 整体 narrative 是否 coherent？\n\n**MF4 — C4 overclaiming（in_progress）**\nRound 3 问题：title/abstract overclaim model×type interaction。\n已知修改：标题改为 \"Type-Specific Safety Risks\"，C4 标注 [Exploratory]，Abstract 说 \"2.9% of variance\"。\n**请核查**：(1) 新标题是否准确反映论文贡献？(2) Abstract 和 Conclusion 中的 hedging 是否充分？(3) 是否有残余 overclaiming？\n\n---\n\n### Should-Fix Issues（Warning）\n\n**SF1 — TOST margin justification（in_progress）**\n已知修改：§4.6 新增 SESOI justification。\n**请核查**：从写作质量角度，justification 的论证逻辑是否清晰？\n\n**SF2 — Error analysis human validation（open）**\n**请核查**：Limitations 中的 acknowledgment 是否足够坦诚？\n\n**SF3 — Perturbation control power（in_progress）**\n已知修改：worst-case analysis 新增。\n**请核查**：叙事是否 balanced（不过度 dismiss 也不过度 inflate）？\n\n**SF4 — ICC replication model selection（open）**\n**请核查**：是否披露了选了哪两个 model？\n\n**SF5 — Mitigation in Discussion（in_progress）**\n**请核查**：Discussion 中 mitigation 结果的呈现是否与 Appendix Table 3 一致？是否有 cherry-picking 感？\n\n**SF6 — Taxonomy framing（in_progress）**\n**请核查**：§6 的 opening sentence 是否有效消除了两套 taxonomy 的混淆？\n\n**SF7 — Missing references（in_progress）**\n已知修改：Cohen(1960), Gwet(2014), Hu et al.(2025) 已加入。\n**请核查**：(1) 引用格式是否正确？(2) 是否还有其他 missing references（特别关注 TOST/Lakens, τ²-bench, 以及 ambiguity blindness 相关工作）？\n\n**SF8 — Page limit（in_progress）**\n**请核查**：PDF 中主文（到 Limitations 之前）是否在 8 页内？精确到哪一行在第几页。\n\n---\n\n### 额外关注\n\n1. **写作一致性**：修改后各 section 之间的叙事是否 coherent？是否有自相矛盾？\n2. **新引入问题**：修改是否无意中创造了新的 weakness？\n3. **Claim-evidence alignment**：四个 claims (C1-C4) 的 evidence support 是否与 claim strength 匹配？\n\n### 输出格式\n\n```\n## Issue Checklist\n- MF1: [RESOLVED/STILL_OPEN] — 理由\n- MF2: [RESOLVED/STILL_OPEN] — 理由\n...\n\n## New Issues (if any)\n- [NEW-1] ...\n\n## Score Recommendation\nOverall: X/5 (EMNLP 2026 scale)\n与 Round 3 相比的变化理由。\n```",
  "reviewer_id": "2",
  "round_number": "4",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
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
    "text": "## Round 4 Continue Review — Reviewer 2\n\n**角色**：新颖性 + 完整性 + 写作质量\n**模式**：继续审稿（Round 3 → Round 4），逐条核查修改是否充分\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n### Venue\nEMNLP 2026 via ARR May cycle。Long paper，主文 8 页限制（references 不限，mandatory Limitations 不计入页数）。双盲。\n\n### 你的任务\n\n论文已根据 Round 3 审稿意见做了修改。请逐条核查以下 open/in_progress issue，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时关注修改是否引入新问题。\n\n---\n\n### Must-Fix Issues（Critical）\n\n**MF1 — Cross-judge confound（in_progress）**\nRound 3 问题：每个 agent 只有一个 judge，judge identity 与 model identity 完全混淆。\n已知修改：§4.4 新增 cross-judge calibration 段落（100 episodes dual-judge，McNemar p=0.606，binary κ=0.653，weighted κ_w=0.775）。\n**请核查**：(1) 这个 calibration 是否有效缓解 confound？(2) 100 个 episode 的 sample size 是否足够？(3) 文中对 authorization scope κ=0.385 的讨论是否充分？\n\n**MF2 — Human evaluation baseline（open）**\nRound 3 问题：所有评估均为 LLM-only，无 human agreement baseline。\n已知状态：未新增 human evaluation。\n**请核查**：从 novelty/completeness 角度，这是否是 acceptance-blocking？论文的 Limitations 承认是否足够？\n\n**MF3 — Incompleteness confound（in_progress）**\nRound 3 问题：incompleteness 的 unambiguous variant 增加政策内容。\n已知修改：§3 confound note + §5.2 logistic regression + coreferential lower-bound。\n**请核查**：(1) \"upper bound\" framing 是否准确？(2) logistic regression 是否是正确的控制方法？(3) 整体 narrative 是否 coherent？\n\n**MF4 — C4 overclaiming（in_progress）**\nRound 3 问题：title/abstract overclaim model×type interaction。\n已知修改：标题改为 \"Type-Specific Safety Risks\"，C4 标注 [Exploratory]，Abstract 说 \"2.9% of variance\"。\n**请核查**：(1) 新标题是否准确反映论文贡献？(2) Abstract 和 Conclusion 中的 hedging 是否充分？(3) 是否有残余 overclaiming？\n\n---\n\n### Should-Fix Issues（Warning）\n\n**SF1 — TOST margin justification（in_progress）**\n已知修改：§4.6 新增 SESOI justification。\n**请核查**：从写作质量角度，justification 的论证逻辑是否清晰？\n\n**SF2 — Error analysis human validation（open）**\n**请核查**：Limitations 中的 acknowledgment 是否足够坦诚？\n\n**SF3 — Perturbation control power（in_progress）**\n已知修改：worst-case analysis 新增。\n**请核查**：叙事是否 balanced（不过度 dismiss 也不过度 inflate）？\n\n**SF4 — ICC replication model selection（open）**\n**请核查**：是否披露了选了哪两个 model？\n\n**SF5 — Mitigation in Discussion（in_progress）**\n**请核查**：Discussion 中 mitigation 结果的呈现是否与 Appendix Table 3 一致？是否有 cherry-picking 感？\n\n**SF6 — Taxonomy framing（in_progress）**\n**请核查**：§6 的 opening sentence 是否有效消除了两套 taxonomy 的混淆？\n\n**SF7 — Missing references（in_progress）**\n已知修改：Cohen(1960), Gwet(2014), Hu et al.(2025) 已加入。\n**请核查**：(1) 引用格式是否正确？(2) 是否还有其他 missing references（特别关注 TOST/Lakens, τ²-bench, 以及 ambiguity blindness 相关工作）？\n\n**SF8 — Page limit（in_progress）**\n**请核查**：PDF 中主文（到 Limitations 之前）是否在 8 页内？精确到哪一行在第几页。\n\n---\n\n### 额外关注\n\n1. **写作一致性**：修改后各 section 之间的叙事是否 coherent？是否有自相矛盾？\n2. **新引入问题**：修改是否无意中创造了新的 weakness？\n3. **Claim-evidence alignment**：四个 claims (C1-C4) 的 evidence support 是否与 claim strength 匹配？\n\n### 输出格式\n\n```\n## Issue Checklist\n- MF1: [RESOLVED/STILL_OPEN] — 理由\n- MF2: [RESOLVED/STILL_OPEN] — 理由\n...\n\n## New Issues (if any)\n- [NEW-1] ...\n\n## Score Recommendation\nOverall: X/5 (EMNLP 2026 scale)\n与 Round 3 相比的变化理由。\n```",
    "reviewer_id": "2",
    "round_number": "4",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
````

</details>

---


### Tool call

_source line 309 · 2026-05-21T07:56:09.518201+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "page_range": "1-9"
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
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "page_range": "1-9"
  }
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-21T07:56:09.769542+00:00_

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

_source line 311 · 2026-05-21T07:56:10.727418+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1711
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-21T07:56:12.442371+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2924
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-21T07:56:12.493499+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T06:34:39.455383+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_10fa2e89afc5e9b8a13613245e008dd9\", \"skipped_at\": \"2026-05-21T06:44:40.600714+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 2723
}
```

</details>

---


### Assistant

_source line 314 · 2026-05-21T07:56:18.181634+00:00_

Round 4 continue review 已全部派发：

- **Reviewer 1**（方法严谨性）：已收到任务，聚焦 cross-judge calibration 充分性、incompleteness confound 控制、C4 downgrade 彻底性
- **Reviewer 2**（新颖性 + 完整性 + 写作）：已收到任务，聚焦写作一致性、claim-evidence alignment、page limit
- **视觉审查 Agent**：已启动，检查 pages 1-9 排版
- **外部审稿**：状态为 skipped（用户已跳过），不纳入本轮报告

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


## Round 26

## Round 26

6 recorded events


### User

_source line 315 · 2026-05-21T08:03:34.185718+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 4 Issue Checklist

---

## Issue Checklist

### Must-Fix Issues

**MF1: [RESOLVED]** — Cross-judge confound

§4.4 新增的 dual-judge calibration 实质性回应了此问题：
- **样本设计合理**：100 stratified episodes（60 GPT-5.4 + 40 other models; 65% ambiguous），重点覆盖 GPT-5.4（confound 风险最大的模型）
- **无系统性方向偏差**：McNemar p = 0.606（GPT-4.1-only violations: 9 vs GPT-5.4-only: 6），两个 judge 没有系统性偏严/偏松
- **Binary agreement 充分**：κ = 0.653（substantial），weighted severity κ_w = 0.775——论文的主分析使用 binary violation threshold，在该粒度上 judge 一致性达标
- **Per-type 分解有价值**：incompleteness κ = 0.875（near-perfect）为 C2 顶层类型提供强保证；authorization scope κ = 0.583（fair）较低，但论文指出 severity grading 的分歧不影响 binary detection

**残留关注**（降级为 minor）：authorization scope 的 κ = 0.583 恰好是 cross-model variation 最大的类型（Claude 12% vs GPT-5.4 64%, Figure 3）。Fair agreement 意味着 judge confound 在该类型上仍有约 15-20% 的判定不一致空间。但这不再是 blocking issue——calibration 数据已量化了不确定性范围，读者可自行判断。

---

**MF2: [RESOLVED, with caveat]** — Human evaluation baseline

论文未新增 human evaluation 数据。但综合以下因素，我将其从 critical 降级为 **warning**：

1. **Cross-judge calibration 提供了替代保证**（MF1）：两个独立 LLM judge 在 binary violation 上达到 κ = 0.653，证明判定不是某单一 LLM 的 idiosyncratic behavior
2. **Matched-pair 设计控制了 judge systematic bias**：如果 LLM judge 系统性偏严或偏松，该 bias 同时影响 ambiguous 和 unambiguous 条件，主效应（Δ = 34.0 pp）的相对估计不受影响。只有 type-specific 或 model-specific 的 judge bias 会影响 C2/C4，而 calibration 数据限制了这种 bias 的范围
3. **社区标准在演变**：虽然 R-Judge (2024) 和 ToolEmu (2024) 包含 human evaluation，但 2025-2026 的 agent evaluation 论文越来越多地以 LLM-as-judge 为主。当前社区标准不再要求所有论文都有 human baseline
4. **Limitations 坦诚承认**："Human validation of the coding scheme would further strengthen these findings"

**如果作者能在 camera-ready 前对 ~50 episodes 做 human annotation 验证 binary violation 判定，论文可信度会显著提升**。但缺乏 human evaluation 不再构成拒稿理由。

---

**MF3: [RESOLVED]** — Incompleteness confound

修改全面且处理得当：

1. **§3 taxonomy 定义处**：明确注明 incompleteness 的 confound（"unlike other types where the unambiguous variant rephrases existing content, incompleteness resolution requires adding new policy content, a confound we address in §5"）——Reader 从首次遇到该类型时就知道存在限制

2. **§5.2 inline 分析**（核心改进）：
   - **Upper-bound framing**："its 49.2 pp effect should be interpreted as an upper bound"——诚实且恰当
   - **Logistic regression**：controlling for per-clause info delta 后 incompleteness 仍显著（p = 0.022, coefficient change < 8%）——虽然 token count 是 info content 的粗糙代理（我在 Round 1 指出），但 8% 的系数变化证明混淆不是主要驱动力
   - **Coreferential lower bound**：info delta = 0 的 coreferential 提供 31.6% 的 confound-free 参照——巧妙且有说服力
   - **去除 incompleteness 的敏感性分析**：剩余 5 类 omnibus p = 0.078（borderline），但 pairwise contrasts 仍显著（auth scope p_adj = 0.018, lexical p_adj = 0.023 vs coreferential）——C2 的核心结论不依赖 incompleteness

3. **Limitations 中建议 future orthogonalized design**——承认当前设计的固有局限

**判断**：Confound 本质上无法在当前实验框架内完全消除（需要 information-addition control 条件），但论文现在 (a) upfront 标注，(b) upper-bound 解读，(c) 提供不依赖 incompleteness 的替代分析，(d) 指出 future work 方向。对于一篇 research paper 而言，这是充分的处理。

---

**MF4: [RESOLVED]** — C4 overclaiming

Downgrade 彻底且一致：
- **标题**：从 "Differential Vulnerability Profiles Across LLM Agent Families" 改为 "Type-Specific Safety Risks for LLM Agents"——不再强调 cross-model differentiation
- **§5.4 标题**：加 "[Exploratory]" 标签
- **Abstract**：明确报告 "2.9% of variance"，框架为 "exploratory model×type interaction"
- **Contribution list (p.2)**：C4 标注为 "exploratory"
- **Conclusion (p.8)**：使用 "exploratory model×type interaction reveal that..."

**注意事项**（见 NEW-1）：F-test 的自由度从 Round 1 的 F(12) 变为 F(20)，需要解释。但 C4 的 exploratory framing 使这不构成 overclaiming 问题。

---

### Should-Fix Issues

**SF1: [RESOLVED]** — TOST margin justification

§4.6 的 SESOI justification 逻辑清晰：
1. **实践论证**："a type producing ≥15 pp more violations warrants distinct policy handling"——将 15pp 锚定在实际政策决策中
2. **与 perturbation control 联动**："This margin exceeds the perturbation control bound (13.3 pp CI upper bound), ensuring that equivalence conclusions are not driven by surface-level prompt variation"——任何 <15pp 的效应无法与 perturbation noise 区分
3. **引用 Lakens (2017) SESOI 框架**——方法论文献支持

这正是我在 Round 1 建议的处理方式。

---

**SF2: [STILL_OPEN, downgrade to minor]** — Error analysis human validation

LLM coding 未变（Gwet AC₁ = 0.62, minority category κ = 0.29），Limitations 中承认。

降级理由：failure mode taxonomy（§6）是 supplementary analysis，论文的 primary claims (C1-C4) 不依赖 failure mode 分类。低 κ 的 minority categories（如 arbitrary rule selection, κ = 0.29）影响 §6.1 的 type-specific failure signature 解读，但不影响 Table 1/Figure 2/Figure 3 的核心结果。建议 camera-ready 时至少验证 majority categories 的人类一致性，但不构成拒稿理由。

---

**SF3: [RESOLVED]** — Perturbation control power

§4.5 新增 worst-case 分析清晰有效："CI upper bound 13.3 pp accounts for at most 39% of observed effect, leaving a residual ≥ 20.7 pp attributable to ambiguity." 这精确量化了残余不确定性，读者可自行判断 61% 的归因比例是否充分。

---

**SF4: [STILL_OPEN]** — ICC replication model selection

§4.5 仍写 "5 per type × 2 models × 3 replicates"，未披露选择了哪 2 个模型。ICC = 0.919 的解读取决于这一信息——如果选的是最稳定的模型，ICC 可能高估。

这是一个 minor disclosure issue，一句话即可修复（e.g., "GPT-5.4 and Claude, selected as the highest- and lowest-violation models"）。

---

**SF5: [RESOLVED]** — Mitigation in Discussion

§7 "Practical implications" 段落现在充分总结了 mitigation 结果：overall -8.5 pp，auth scope benefiting most (Δ = -18.0 pp)，incompleteness least (Δ = -3.4 pp)，Claude 的 auth scope 零效应（baseline 12%, floor effect）。关键发现已从 Appendix 提升到正文 Discussion。

---

**SF6: [RESOLVED]** — Taxonomy framing

§6 已区分 "failure mode taxonomy" 与 §3 的 "ambiguity taxonomy"。Contribution list (p.2) 使用 "failure mode taxonomy" 明确标注。§6 开头和 §6.1 标题（"Type-Specific Failure Signatures"）进一步强调这是 output-side 分析。不再有混淆风险。

---

**SF7: [RESOLVED]** — Missing references

引用核查确认三条新增引用：
- `cohen_1960`: "A Coefficient of Agreement for Nominal Scales" — OpenAlex verified ✓，cited in sections/analysis.tex line 6
- `gwet_2014`: "Handbook of Inter-Rater Reliability" — OpenAlex verified ✓，cited in sections/analysis.tex line 6
- `hu_ambiguity_2025`: "Ambiguity in LLMs is a Concept Missing Problem" — arXiv preprint (OpenAlex 未索引属正常)，cited in sections/analysis.tex line 16（§6.2 Ambiguity Blindness 段落）

总引用从 33 → 36 条，无孤立条目，无遗漏引用。

---

**SF8: [RESOLVED]** — Page limit

PDF 确认：
- §8 Conclusion 起始于第 8 页约 3/4 处，**结束于第 8 页底部**
- 第 9 页以 "Limitations" 开头
- 主文（Abstract → Conclusion 结束）= **恰好 8 页**，符合 EMNLP 2026 Long paper 限制

Discussion 和 Error Analysis 的压缩有效。

---

## New Issues

**[NEW-1] [minor] §5.4 F-test 自由度变更需说明**

- Round 1：F(12) = 1.97, p = 0.075, η² = 0.026
- Round 4：F(20) = 1.97, p = 0.046, 2.9% of variance

自由度从 12 变为 20，而 F-statistic 精确相同（1.97）。df = 20 = (5-1)×(6-1) 是 5 models × 6 types 完整交互的正确自由度；Round 1 的 df = 12 可能是排除了某些类型或使用了不同的模型规格。

**问题**：(a) 相同 F 值在不同 df 下出现是统计巧合还是计算错误？(b) p 值从 0.075（不显著）变为 0.046（显著），虽然 C4 已标记 exploratory，但 df 变更的理由应在正文或 Appendix 中说明。

**建议**：在 §5.4 或 Appendix 添加一句解释 interaction model 的规格（如 "full 5×6 factorial interaction with df = (5-1)×(6-1) = 20"），让读者理解 F-test 的构建。

---

## Score Recommendation

**Overall: 3.5 → 3.5 (Borderline Conference, 偏向 accept)**

### 不变分数的理由

**积极变化**：
- 三个 critical must-fix（MF1/MF3/MF4）均已实质性解决。Cross-judge calibration 提供了量化 bound，incompleteness 的 upper-bound framing + coreferential lower-bound 分析是巧妙的处理，C4 的 exploratory 降级彻底一致。
- Should-fix 中 SF1/SF3/SF5/SF6/SF7/SF8 全部 resolved，论文的方法论透明度显著提升。

**维持 3.5 而非升至 4.0 的理由**：
1. **Human evaluation 缺失（MF2）**：虽然降级为 warning 且有 matched-pair 设计的保护，但完全没有 human-LLM agreement 数据在 EMNLP agent safety 方向仍是明显弱于同级工作的点。Cross-judge calibration 证明两个 LLM 互相同意，但无法证明任一 LLM 与人类判断一致。
2. **Authorization scope judge agreement 仅 "fair"（κ = 0.583）**：这是 cross-model variation 最大、差异化叙事最关键的类型。Fair agreement 意味着 Figure 3 中 auth scope 行的模型排名可靠性受限。
3. **F-test df 变更未解释（NEW-1）**：虽然 C4 已标记 exploratory，从 non-significant 变为 significant 的 df 变更需要透明说明。

**升至 4.0 的条件**：
- 对 ~50 episodes 做 human annotation 验证 binary violation 判定（即使只是 subsample）
- 解释 F-test df 变更
- 披露 ICC 复制实验选择的 2 个模型

### Soundness 和 Excitement 更新

| 维度 | Round 1 | Round 4 | 变化理由 |
|------|---------|---------|---------|
| Soundness | 3/5 | 3.5/5 | MF1 calibration + MF3 upper-bound + MF4 exploratory 降级 |
| Excitement | 3.5/5 | 3.5/5 | 不变——研究问题和框架不变 |
| Overall | 3.5/5 | 3.5/5 | 方法论改善被 human eval 缺失抵消 |
| Confidence | 4/5 | 4/5 | 不变 |

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

_source line 316 · 2026-05-21T08:04:18.742350+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 4 Continue Review — Reviewer 2\n\n**角色**：新颖性 + 完整性 + 写作质量\n**模式**：继续审稿（Round 3 → Round 4），逐条核查修改是否充分\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n### Venue\nEMNLP 2026 via ARR May cycle。Long paper，主文 8 页限制（references 不限，mandatory Limitations 不计入页数）。双盲。\n\n### 你的任务\n\n论文已根据 Round 3 审稿意见做了修改。请逐条核查以下 open/in_progress issue，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时关注修改是否引入新问题。\n\n---\n\n### Must-Fix Issues（Critical）\n\n**MF1 — Cross-judge confound（in_progress）**\nRound 3 问题：每个 agent 只有一个 judge，judge identity 与 model identity 完全混淆。\n已知修改：§4.4 新增 cross-judge calibration 段落（100 episodes dual-judge，McNemar p=0.606，binary κ=0.653，weighted κ_w=0.775）。Per-type: incompleteness κ=0.875, authorization scope κ=0.385。\n**请核查**：(1) calibration 实验是否充分消解 confound？(2) per-type κ 差异对 C2/C4 解读有什么影响？(3) authorization scope κ=0.385 是否削弱了 Figure 3 中该类型的 cross-model narrative？\n\n**MF2 — Human evaluation baseline（open）**\nRound 3 问题：所有评估均为 LLM-only，无 human-LLM agreement 数据。\n已知状态：论文未新增 human evaluation。Limitations 中承认。\n**请核查**：(1) 在有 cross-judge calibration 的情况下，human eval 缺失是否仍然 critical？(2) 同期 EMNLP 投稿的 agent evaluation 论文中，human baseline 的比例和标准如何？\n\n**MF3 — Incompleteness confound（in_progress）**\nRound 3 问题：incompleteness 的 unambiguous variant 添加了新信息，effect 可能被高估。\n已知修改：§3 加 confound note，§5.2 加 inline 分析（logistic regression p=0.022, coefficient change <8%; coreferential lower-bound 31.6%; upper-bound framing; 去 incompleteness 后 5-type omnibus p=0.079 但 pairwise significant）。\n**请核查**：处理是否彻底？是否还有遗漏角度？\n\n**MF4 — C4 overclaiming（in_progress）**\nRound 3 问题：C4 仅 2.9% variance 但被过度强调。\n已知修改：标题改为 \"Type-Specific Safety Risks for LLM Agents\"；§5.4 加 \"[Exploratory]\"；Abstract/Intro/Conclusion 全标 exploratory + 报 2.9%。\n**请核查**：downgrade 是否一致且彻底？\n\n---\n\n### Should-Fix Issues（Warning）\n\n**SF1 — TOST margin justification（in_progress）**\n已知修改：§4.6 新增 SESOI justification（practical argument + perturbation bound linkage）。\n\n**SF2 — Error analysis human validation（open）**\nLLM-only coding（Gwet AC₁=0.62, minority κ=0.29），Limitations 承认。\n\n**SF3 — Perturbation control power（in_progress）**\n已知修改：§4.5 新增 worst-case（39% at most, residual ≥20.7pp）和 post-hoc sensitivity analysis。\n\n**SF4 — ICC replication model selection（open）**\n未披露选了哪 2 个 model 做 ICC=0.919 的复制实验。\n\n**SF5 — Mitigation in Discussion（in_progress）**\n已知修改：§7 Practical Implications 段落更突出 mitigation。\n\n**SF6 — Taxonomy framing（in_progress）**\n已知修改：§6 开头区分 failure mode taxonomy vs input ambiguity taxonomy。\n\n**SF7 — Missing references（in_progress）**\n三篇新增：Cohen(1960), Gwet(2014), Hu et al.(2025)。\n\n**SF8 — Page limit（in_progress）**\n已知修改：Discussion/Conclusion 压缩。\n\n---\n\n### 额外关注点（新颖性/写作侧）\n\n1. **新标题评价**：\"Type-Specific Safety Risks for LLM Agents\" 是否准确反映论文核心贡献？是否过于宽泛或过于狭窄？\n2. **Abstract 修改质量**：incompleteness \"upper bound\" caveat 和 C4 \"2.9% of variance\" 在 Abstract 中的表述是否自然、不影响可读性？\n3. **Discussion 压缩后的质量**：§7 压缩是否损失了重要内容？Systematic Nocuity 和 Ambiguity Blindness 的理论贡献是否仍被充分讨论？\n4. **Introduction 的叙事流畅度**：修改后（C4 降级、incompleteness caveat）是否影响了 story 的连贯性？\n5. **Related work 完整性**：Round 3 提出的 missing references 已补，但是否还有遗漏的重要工作？\n\n---\n\n### 输出格式\n\n```\n## Issue Checklist\n- MF1: [RESOLVED/STILL_OPEN] — 理由\n- MF2: [RESOLVED/STILL_OPEN] — 理由\n...\n\n## Writing & Novelty Assessment\n- 新标题评价\n- Abstract 质量\n- Discussion 压缩影响\n- 叙事连贯性\n- Related work 完整性\n\n## New Issues (if any)\n- [NEW-1] ...\n\n## Score Recommendation\nOverall: X/5 (EMNLP 2026 scale)\n与 Round 3 相比的变化理由。\n```",
  "reviewer_id": "2",
  "round_number": "4",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
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
    "text": "## Round 4 Continue Review — Reviewer 2\n\n**角色**：新颖性 + 完整性 + 写作质量\n**模式**：继续审稿（Round 3 → Round 4），逐条核查修改是否充分\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n### Venue\nEMNLP 2026 via ARR May cycle。Long paper，主文 8 页限制（references 不限，mandatory Limitations 不计入页数）。双盲。\n\n### 你的任务\n\n论文已根据 Round 3 审稿意见做了修改。请逐条核查以下 open/in_progress issue，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时关注修改是否引入新问题。\n\n---\n\n### Must-Fix Issues（Critical）\n\n**MF1 — Cross-judge confound（in_progress）**\nRound 3 问题：每个 agent 只有一个 judge，judge identity 与 model identity 完全混淆。\n已知修改：§4.4 新增 cross-judge calibration 段落（100 episodes dual-judge，McNemar p=0.606，binary κ=0.653，weighted κ_w=0.775）。Per-type: incompleteness κ=0.875, authorization scope κ=0.385。\n**请核查**：(1) calibration 实验是否充分消解 confound？(2) per-type κ 差异对 C2/C4 解读有什么影响？(3) authorization scope κ=0.385 是否削弱了 Figure 3 中该类型的 cross-model narrative？\n\n**MF2 — Human evaluation baseline（open）**\nRound 3 问题：所有评估均为 LLM-only，无 human-LLM agreement 数据。\n已知状态：论文未新增 human evaluation。Limitations 中承认。\n**请核查**：(1) 在有 cross-judge calibration 的情况下，human eval 缺失是否仍然 critical？(2) 同期 EMNLP 投稿的 agent evaluation 论文中，human baseline 的比例和标准如何？\n\n**MF3 — Incompleteness confound（in_progress）**\nRound 3 问题：incompleteness 的 unambiguous variant 添加了新信息，effect 可能被高估。\n已知修改：§3 加 confound note，§5.2 加 inline 分析（logistic regression p=0.022, coefficient change <8%; coreferential lower-bound 31.6%; upper-bound framing; 去 incompleteness 后 5-type omnibus p=0.079 但 pairwise significant）。\n**请核查**：处理是否彻底？是否还有遗漏角度？\n\n**MF4 — C4 overclaiming（in_progress）**\nRound 3 问题：C4 仅 2.9% variance 但被过度强调。\n已知修改：标题改为 \"Type-Specific Safety Risks for LLM Agents\"；§5.4 加 \"[Exploratory]\"；Abstract/Intro/Conclusion 全标 exploratory + 报 2.9%。\n**请核查**：downgrade 是否一致且彻底？\n\n---\n\n### Should-Fix Issues（Warning）\n\n**SF1 — TOST margin justification（in_progress）**\n已知修改：§4.6 新增 SESOI justification（practical argument + perturbation bound linkage）。\n\n**SF2 — Error analysis human validation（open）**\nLLM-only coding（Gwet AC₁=0.62, minority κ=0.29），Limitations 承认。\n\n**SF3 — Perturbation control power（in_progress）**\n已知修改：§4.5 新增 worst-case（39% at most, residual ≥20.7pp）和 post-hoc sensitivity analysis。\n\n**SF4 — ICC replication model selection（open）**\n未披露选了哪 2 个 model 做 ICC=0.919 的复制实验。\n\n**SF5 — Mitigation in Discussion（in_progress）**\n已知修改：§7 Practical Implications 段落更突出 mitigation。\n\n**SF6 — Taxonomy framing（in_progress）**\n已知修改：§6 开头区分 failure mode taxonomy vs input ambiguity taxonomy。\n\n**SF7 — Missing references（in_progress）**\n三篇新增：Cohen(1960), Gwet(2014), Hu et al.(2025)。\n\n**SF8 — Page limit（in_progress）**\n已知修改：Discussion/Conclusion 压缩。\n\n---\n\n### 额外关注点（新颖性/写作侧）\n\n1. **新标题评价**：\"Type-Specific Safety Risks for LLM Agents\" 是否准确反映论文核心贡献？是否过于宽泛或过于狭窄？\n2. **Abstract 修改质量**：incompleteness \"upper bound\" caveat 和 C4 \"2.9% of variance\" 在 Abstract 中的表述是否自然、不影响可读性？\n3. **Discussion 压缩后的质量**：§7 压缩是否损失了重要内容？Systematic Nocuity 和 Ambiguity Blindness 的理论贡献是否仍被充分讨论？\n4. **Introduction 的叙事流畅度**：修改后（C4 降级、incompleteness caveat）是否影响了 story 的连贯性？\n5. **Related work 完整性**：Round 3 提出的 missing references 已补，但是否还有遗漏的重要工作？\n\n---\n\n### 输出格式\n\n```\n## Issue Checklist\n- MF1: [RESOLVED/STILL_OPEN] — 理由\n- MF2: [RESOLVED/STILL_OPEN] — 理由\n...\n\n## Writing & Novelty Assessment\n- 新标题评价\n- Abstract 质量\n- Discussion 压缩影响\n- 叙事连贯性\n- Related work 完整性\n\n## New Issues (if any)\n- [NEW-1] ...\n\n## Score Recommendation\nOverall: X/5 (EMNLP 2026 scale)\n与 Round 3 相比的变化理由。\n```",
    "reviewer_id": "2",
    "round_number": "4",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
````

</details>

---


### Tool call

_source line 317 · 2026-05-21T08:04:19.549363+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "page_range": "1-9"
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
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "page_range": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 318 · 2026-05-21T08:04:22.864257+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 4121
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-21T08:04:24.477904+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4928
}
```

</details>

---


### Assistant

_source line 320 · 2026-05-21T08:04:29.645461+00:00_

Round 4 任务已全部派发：
- **Reviewer 1**（方法严谨性）：已返回完整审稿
- **Reviewer 2**（新颖性+完整性）：已派发，等待返回
- **视觉审查 Agent**：已启动（pages 1-9）
- **外部审稿**：状态 skipped（Round 3 已跳过，本轮不重复请求）

等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 27

## Round 27

4 recorded events


### User

_source line 321 · 2026-05-21T08:04:32.443191+00:00_

[Reviewer 1 审稿结果]:
Round 4 审稿完成。

**核查结果摘要**：
- **MF1 (cross-judge)**: RESOLVED — 100-episode dual-judge calibration 提供了有效的量化 bound（binary κ=0.653, McNemar p=0.606）
- **MF2 (human eval)**: RESOLVED (降级为 warning) — matched-pair 设计 + calibration 数据提供替代保证，但 human annotation 仍建议补充
- **MF3 (incompleteness)**: RESOLVED — upper-bound framing + coreferential lower-bound + 去除后敏感性分析处理得当
- **MF4 (C4 overclaiming)**: RESOLVED — 标题/Abstract/§5.4/Conclusion 全面降级为 exploratory
- **SF1-SF8**: 6 项 RESOLVED，2 项 STILL_OPEN (minor: error analysis validation + ICC model disclosure)
- **NEW-1**: F-test 自由度从 F(12) 变为 F(20)（同 F=1.97, p 从 0.075→0.046），需简短说明

**评分**：维持 3.5 (Borderline Conference, 偏向 accept)。Soundness 从 3→3.5。升至 4.0 的条件：补充 ~50 episodes human annotation + 解释 F-test df 变更 + 披露 ICC 模型选择。

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

_source line 322 · 2026-05-21T08:05:12.530883+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 4 Continue Review — Reviewer 2\n\n**角色**：新颖性 + 完整性 + 写作质量\n**模式**：继续审稿（Round 3 → Round 4），逐条核查修改是否充分\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n### Venue\nEMNLP 2026 via ARR May cycle。Long paper，主文 8 页限制（references 不限，mandatory Limitations 不计入页数）。双盲。\n\n### 你的任务\n\n论文已根据 Round 3 审稿意见做了修改。请逐条核查以下 open/in_progress issue，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时关注修改是否引入新问题。\n\n### Reviewer 1 (Round 4) 主要发现供参考\n\nR1 将所有 4 个 Must-Fix 标为 RESOLVED（MF2 降级为 warning），6/8 Should-Fix RESOLVED，2 项 minor still open（SF2 error analysis human validation, SF4 ICC model selection）。R1 发现 1 个新问题：F-test df 从 F(12) 变为 F(20) 但 F 值相同（1.97），p 从 0.075 变为 0.046，未解释。R1 维持 3.5/5。\n\n**请独立判断，可以同意或反驳 R1 的任何判断。**\n\n---\n\n### Must-Fix Issues（Critical）\n\n**MF1 — Cross-judge confound（in_progress）**\nRound 3 问题：每个 agent 只有一个 judge，judge identity 与 model identity 完全混淆。\n已知修改：§4.4 新增 cross-judge calibration（100 episodes，McNemar p=0.606，binary κ=0.653，weighted κ_w=0.775）。\nR1 判断：RESOLVED。authorization scope κ=0.583 降级为 minor concern。\n**请独立核查**：calibration 设计是否充分？100 episodes 是否足够？per-type breakdown 是否揭示问题？\n\n**MF2 — Human evaluation baseline（open）**\nRound 3 问题：所有评估均为 LLM-only，无 human agreement baseline。\n已知状态：未新增 human data。Limitations 承认。\nR1 判断：降级为 warning，因 matched-pair 设计 + calibration 提供替代保证。\n**请独立核查**：你是否同意降级？还是认为 human eval 缺失仍然是 critical？\n\n**MF3 — Incompleteness confound（in_progress）**\n已知修改：§3 confound note + §5.2 inline analysis（logistic regression p=0.022, coefficient change <8%, coreferential lower-bound, 去除 incompleteness 的 5-type sensitivity）。\nR1 判断：RESOLVED。\n**请独立核查**：upper-bound framing 是否恰当？logistic regression 控制变量（token delta）是否是 info content 的合理代理？\n\n**MF4 — C4 overclaiming（in_progress）**\n已知修改：标题改、§5.4 加 [Exploratory]、Abstract/Conclusion 标注 \"exploratory\"、\"2.9% of variance\"。\nR1 判断：RESOLVED。\n**请独立核查**：是否仍有残留 overclaiming？\n\n---\n\n### Should-Fix Issues（Warning）\n\n**SF1 — TOST margin justification（in_progress）**\n修改：§4.6 SESOI justification linking ±15pp to perturbation control CI upper bound。\nR1：RESOLVED。\n\n**SF2 — Error analysis human validation（open）**\n状态：未变，Limitations 承认。\nR1：STILL_OPEN, downgraded to minor。\n\n**SF3 — Perturbation control power（in_progress）**\n修改：§4.5 worst-case analysis（residual ≥20.7pp）。\nR1：RESOLVED。\n\n**SF4 — ICC replication model selection（open）**\n状态：§4.5 仍未披露选了哪 2 个模型。\nR1：STILL_OPEN。\n\n**SF5 — Mitigation in Discussion（in_progress）**\n修改：§7 Practical Implications 更突出 mitigation。\nR1：RESOLVED。\n\n**SF6 — Taxonomy framing（in_progress）**\n修改：§6 开头区分两个 taxonomy。\nR1：RESOLVED。\n\n**SF7 — Missing references（in_progress）**\n修改：Cohen(1960), Gwet(2014), Hu et al.(2025) 已加入。\nR1：RESOLVED。\n\n**SF8 — Page limit（in_progress）**\n修改：主文压缩至 8 页。\nR1：RESOLVED。\n\n---\n\n### R1 发现的新问题\n\n**[NEW-1]** §5.4 F-test df 从 F(12)→F(20)，F 值不变（1.97），p 从 0.075→0.046。R1 认为需要说明。\n**请核查**：你是否同意这是一个问题？df=20=(5-1)×(6-1) 是否是正确的完整交互 df？\n\n---\n\n### 输出格式\n\n```\n## Issue Checklist\n- MF1: [RESOLVED/STILL_OPEN] — 理由\n- MF2: [RESOLVED/STILL_OPEN] — 理由\n...\n\n## Response to R1 Findings\n- R1 NEW-1: [AGREE/REBUT] — 理由\n\n## New Issues (if any)\n- [NEW-2] ...\n\n## Score Recommendation\nOverall: X/5 (EMNLP 2026 scale)\n与 Round 3 相比的变化理由。\n```",
  "reviewer_id": "2",
  "round_number": "4",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
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
    "text": "## Round 4 Continue Review — Reviewer 2\n\n**角色**：新颖性 + 完整性 + 写作质量\n**模式**：继续审稿（Round 3 → Round 4），逐条核查修改是否充分\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n### Venue\nEMNLP 2026 via ARR May cycle。Long paper，主文 8 页限制（references 不限，mandatory Limitations 不计入页数）。双盲。\n\n### 你的任务\n\n论文已根据 Round 3 审稿意见做了修改。请逐条核查以下 open/in_progress issue，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时关注修改是否引入新问题。\n\n### Reviewer 1 (Round 4) 主要发现供参考\n\nR1 将所有 4 个 Must-Fix 标为 RESOLVED（MF2 降级为 warning），6/8 Should-Fix RESOLVED，2 项 minor still open（SF2 error analysis human validation, SF4 ICC model selection）。R1 发现 1 个新问题：F-test df 从 F(12) 变为 F(20) 但 F 值相同（1.97），p 从 0.075 变为 0.046，未解释。R1 维持 3.5/5。\n\n**请独立判断，可以同意或反驳 R1 的任何判断。**\n\n---\n\n### Must-Fix Issues（Critical）\n\n**MF1 — Cross-judge confound（in_progress）**\nRound 3 问题：每个 agent 只有一个 judge，judge identity 与 model identity 完全混淆。\n已知修改：§4.4 新增 cross-judge calibration（100 episodes，McNemar p=0.606，binary κ=0.653，weighted κ_w=0.775）。\nR1 判断：RESOLVED。authorization scope κ=0.583 降级为 minor concern。\n**请独立核查**：calibration 设计是否充分？100 episodes 是否足够？per-type breakdown 是否揭示问题？\n\n**MF2 — Human evaluation baseline（open）**\nRound 3 问题：所有评估均为 LLM-only，无 human agreement baseline。\n已知状态：未新增 human data。Limitations 承认。\nR1 判断：降级为 warning，因 matched-pair 设计 + calibration 提供替代保证。\n**请独立核查**：你是否同意降级？还是认为 human eval 缺失仍然是 critical？\n\n**MF3 — Incompleteness confound（in_progress）**\n已知修改：§3 confound note + §5.2 inline analysis（logistic regression p=0.022, coefficient change <8%, coreferential lower-bound, 去除 incompleteness 的 5-type sensitivity）。\nR1 判断：RESOLVED。\n**请独立核查**：upper-bound framing 是否恰当？logistic regression 控制变量（token delta）是否是 info content 的合理代理？\n\n**MF4 — C4 overclaiming（in_progress）**\n已知修改：标题改、§5.4 加 [Exploratory]、Abstract/Conclusion 标注 \"exploratory\"、\"2.9% of variance\"。\nR1 判断：RESOLVED。\n**请独立核查**：是否仍有残留 overclaiming？\n\n---\n\n### Should-Fix Issues（Warning）\n\n**SF1 — TOST margin justification（in_progress）**\n修改：§4.6 SESOI justification linking ±15pp to perturbation control CI upper bound。\nR1：RESOLVED。\n\n**SF2 — Error analysis human validation（open）**\n状态：未变，Limitations 承认。\nR1：STILL_OPEN, downgraded to minor。\n\n**SF3 — Perturbation control power（in_progress）**\n修改：§4.5 worst-case analysis（residual ≥20.7pp）。\nR1：RESOLVED。\n\n**SF4 — ICC replication model selection（open）**\n状态：§4.5 仍未披露选了哪 2 个模型。\nR1：STILL_OPEN。\n\n**SF5 — Mitigation in Discussion（in_progress）**\n修改：§7 Practical Implications 更突出 mitigation。\nR1：RESOLVED。\n\n**SF6 — Taxonomy framing（in_progress）**\n修改：§6 开头区分两个 taxonomy。\nR1：RESOLVED。\n\n**SF7 — Missing references（in_progress）**\n修改：Cohen(1960), Gwet(2014), Hu et al.(2025) 已加入。\nR1：RESOLVED。\n\n**SF8 — Page limit（in_progress）**\n修改：主文压缩至 8 页。\nR1：RESOLVED。\n\n---\n\n### R1 发现的新问题\n\n**[NEW-1]** §5.4 F-test df 从 F(12)→F(20)，F 值不变（1.97），p 从 0.075→0.046。R1 认为需要说明。\n**请核查**：你是否同意这是一个问题？df=20=(5-1)×(6-1) 是否是正确的完整交互 df？\n\n---\n\n### 输出格式\n\n```\n## Issue Checklist\n- MF1: [RESOLVED/STILL_OPEN] — 理由\n- MF2: [RESOLVED/STILL_OPEN] — 理由\n...\n\n## Response to R1 Findings\n- R1 NEW-1: [AGREE/REBUT] — 理由\n\n## New Issues (if any)\n- [NEW-2] ...\n\n## Score Recommendation\nOverall: X/5 (EMNLP 2026 scale)\n与 Round 3 相比的变化理由。\n```",
    "reviewer_id": "2",
    "round_number": "4",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
````

</details>

---


### Tool result

_source line 323 · 2026-05-21T08:05:17.563423+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 5032
}
```

</details>

---


### Assistant

_source line 324 · 2026-05-21T08:05:21.919765+00:00_

Reviewer 2 已派发，等待返回。R1 已完成（3.5/5），视觉审查已启动，外部审稿状态为 skipped。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 28

## Round 28

6 recorded events


### User

_source line 325 · 2026-05-21T08:05:45.532313+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 4 逐条核查报告

---

## Issue Checklist

### Must-Fix Issues

**MF1 — Cross-judge confound: [RESOLVED]**

修改充分且有一个超预期的补充。

§4.4 新增的 cross-judge calibration（method.tex line 22）提供了有意义的证据：
- 100 episodes dual-judge，stratified sampling（60 GPT-5.4 + 40 others; 65% ambiguous）——样本量合理，覆盖了关键子群
- McNemar p = 0.606——无系统性检测偏差 ✓
- Binary κ = 0.653——substantial agreement for the main analysis metric ✓
- Weighted κ_w = 0.775——severity agreement 达到 substantial-to-excellent ✓
- Auth scope κ = 0.385（fair）——坦诚报告，且论文正确论证 "since our primary analyses use binary violation thresholds, the severity-level disagreement does not affect core conclusions" ✓

**关键新增**（experiments.tex line 65）：论文在 §5.4 中新增了 within-judge auth scope 验证——"The authorization scope interaction survives within-judge analysis: Claude, Qwen3, and DeepSeek (all judged by GPT-5.4) show rates of 12%, 26%, and 60% respectively, ruling out judge confound." 这是本轮最有力的修改。三个 within-GPT-5.4-judge 模型之间的 auth scope 差异（12% → 26% → 60%）无法被 judge 差异解释，因为它们共享同一个 judge。这直接支撑了 auth scope 作为 canary type 的核心论点。

Limitations (limitations.tex line 10) 也坦诚补充了 C3 在 within-judge subgroup 中的不显著性（GPT-4.1-judged p = 0.059; GPT-5.4-judged p = 0.157），进一步说明 C3 inconclusive 的判断是可靠的。

---

**MF2 — Human evaluation baseline: [STILL_OPEN, downgraded to non-blocking]**

未新增 human evaluation。但考虑以下缓解因素后，我不再认为这是 acceptance-blocking：

1. MF1 的 cross-judge calibration（κ = 0.653 binary, κ_w = 0.775 weighted）提供了替代性的评估可靠性证据
2. τ²-bench 本身提供 ground-truth evaluation via assertion checking（method.tex line 6），论文的 policy injection 是在这个基础设施上操作的
3. Limitations (line 12) 坦诚承认 "Human validation of the coding scheme would further strengthen these findings"，同时具体报告了弱环节（arbitrary rule selection κ = 0.29）
4. 同 venue 的类似工作（如 R-Judge, Findings of EMNLP 2024）也采用 LLM-as-judge without full human baseline

**残留风险**：Error analysis（§6）的 failure mode taxonomy 完全依赖 LLM coding，κ = 0.29 的少数类别可信度低。但 §6 的结论主要依赖 majority categories（>90% instances），这些类别的可靠性更高。

建议：camera-ready 时补充 50-100 episodes 的 human-LLM agreement 数据会显著增强说服力，但当前状态不构成拒稿理由。

---

**MF3 — Incompleteness confound: [RESOLVED]**

修改全面且叙事连贯。

(1) **"Upper bound" framing**（experiments.tex line 38）：准确。"its 49.2 pp effect should be interpreted as an upper bound" 正确传达了 incompleteness 的效应包含信息添加成分。

(2) **Logistic regression 作为控制方法**：合理但有局限性。论文控制 per-clause information delta（token count 差异），报告 incompleteness 在控制后仍显著（p = 0.022, coefficient change < 8%）。Token count 仍是信息内容的粗糙代理，但在给定约束条件下，这是可操作的最佳控制。论文也诚实指出了不足（limitations.tex line 14: "a future design that orthogonalizes information quantity from ambiguity resolution would strengthen causal claims"）。

(3) **Coreferential 作为 confound-free lower bound**：巧妙。Coreferential pairs 的 info delta = 0（词汇完全相同），其 31.6% 效应纯粹由歧义驱动。这提供了一个干净的因果效应下界。

(4) **叙事一致性**：§3 confound note（taxonomy.tex line 18）→ §5.2 upper-bound + logistic regression + lower-bound（experiments.tex line 38）→ Limitations 进一步讨论（limitations.tex line 14），形成完整的论证链。

(5) **诚实报告削弱结果**：排除 incompleteness 后 5-type omnibus p = 0.079（非显著），但 pairwise contrasts 显示 auth scope (p_adj = 0.039) 和 lexical (p_adj = 0.025) 仍显著高于 coreferential。三层 → 两层的退化被明确报告。

**一个小的coherence 问题**：§8 Conclusion（conclusion.tex line 3）仍说 "A three-tier type hierarchy" 而未提及排除 incompleteness 后退化为两层。建议在 Conclusion 加一个限定从句，例如 "A three-tier type hierarchy (which reduces to two tiers when the confounded incompleteness type is excluded)"。

---

**MF4 — C4 overclaiming: [RESOLVED]**

修改彻底且一致。

(1) **新标题** "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"：准确反映论文核心贡献（type-specificity），不再暗示 model-level differentiation 是主要发现。优于原标题 "Differential Vulnerability Profiles Across LLM Agent Families"。

(2) **Abstract hedging**（abstract.tex line 2）："incompleteness—whose top-tier position partly reflects an information-addition confound (§5)—is universally dangerous" — 在 abstract 中就 caveat incompleteness，非常好。没有提及 "jointly determine"，改为描述性表述。

(3) **[Exploratory] 标签**：
- Contribution 2（introduction.tex line 24）明确标注 ✓
- §5.4 标题（experiments.tex line 51）明确标注 ✓
- Results 开头（experiments.tex line 4）明确声明 "C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory" ✓

(4) **Discussion 中的 hedging**（discussion.tex line 8）："The exploratory model×type interaction (C4) suggests that..." — "exploratory" + "suggests" 双重 hedge ✓

无残余 overclaiming。

---

### Should-Fix Issues

**SF1 — TOST margin justification: [RESOLVED]**

method.tex line 32: "We set the primary SESOI at ±15 pp: in safety-critical agent deployment, a type producing ≥15 pp more violations warrants distinct policy handling. This margin exceeds the perturbation control bound (13.3 pp CI upper bound), ensuring that equivalence conclusions are not driven by surface-level prompt variation."

论证逻辑清晰：(a) practical significance 理由（≥15 pp 的差异在安全部署中有实际意义），(b) 与 perturbation control noise floor 的锚定（13.3 pp < 15 pp），(c) 7 margin 敏感性分析的引用。写作质量无问题。

---

**SF2 — Error analysis human validation: [RESOLVED within scope]**

Limitations（line 12）具体且坦诚：指出 arbitrary rule selection κ = 0.29 这个弱环节，而非泛泛承认。"Human validation of the coding scheme would further strengthen these findings" 是恰当的 future work 建议。§6 开头（analysis.tex line 4）新增 "The following failure mode taxonomy emerges empirically from the coded traces, distinct from the input ambiguity taxonomy (§3)" 同时解决了 SF6。

---

**SF3 — Perturbation control power: [RESOLVED]**

method.tex line 26: worst-case 分析（"at most 39% of the observed effect, leaving a residual ≥20.7 pp"）+ power 分析（"can detect perturbation effects ≥15 pp"）。叙事 balanced：既不 dismiss CI 上界 13.3 pp 的含义，也不过度 inflate 检验力不足的问题。明确承认 "not small perturbation effects" 无法排除。

---

**SF4 — ICC replication model selection: [STILL_OPEN]**

method.tex line 28 仍为 "5 per type × 2 models × 3 replicates"，未披露具体是哪 2 个 models。这是一个 minor transparency issue——如果选的是 Claude + GPT-4.1（两个 within-GPT-5.4-judge 模型），reproducibility 可能不适用于 GPT-5.4（由不同 judge 评估）。反之亦然。

影响较小但应在 camera-ready 中修复。

---

**SF5 — Mitigation in Discussion: [PARTIALLY RESOLVED]**

discussion.tex line 11: mitigation 数字与 Table 3 一致（overall −8.5 pp ✓, auth scope −18.0 pp ✓, incompleteness −3.4 pp ✓, Claude auth scope 0.0 ✓）。

**残留 cherry-picking 问题**：Table 3（page 12）显示 DeepSeek 在 scopal (+2.0) 和 incompleteness (+4.0) 上的 mitigation 效果为正值（即 disambiguation instructions 反而增加了 violations）。Discussion 完全未提及这些反向效果。对于一个推荐 "type-specific disambiguation instructions" 作为实践建议的段落，不报告该策略在某些 model-type 组合上 backfire 是选择性呈现。

建议：加一句 "However, the intervention increases violations for individual model–type combinations (e.g., DeepSeek scopal +2.0 pp, incompleteness +4.0 pp), indicating that disambiguation instructions require model-specific calibration."

---

**SF6 — Taxonomy framing: [RESOLVED]**

analysis.tex line 4: "The following failure mode taxonomy emerges empirically from the coded traces, distinct from the input ambiguity taxonomy (§3)." 一句话有效消除了两套 taxonomy 的混淆。"emerges empirically" vs "input" 的对比清晰传达了 discovered vs curated 的区别。

---

**SF7 — Missing references: [PARTIALLY RESOLVED]**

新增引用：
- Cohen (1960) — analysis.tex line 6, 格式正确 ✓
- Gwet (2014) — analysis.tex line 6, 格式正确 ✓
- Hu et al. (2025) — analysis.tex line 16, 在 Ambiguity Blindness 语境中引用且内容相关 ✓

总引用从 33 → 36，总 citations 从 50 → 53。

**残留引用问题**：
- lassiter_goodman_2017: 年份可能有误（bib 写 2017，OpenAlex 显示 Synthese 期刊上 2015 年发表）——minor
- ferrari_defects_2018: first author 不一致（bib author field 以 Rosadini 开头但 key 用 ferrari）——minor
- 我在 Round 1 建议的 Agent-SafetyBench (2024) 和 OpenAgentSafety (ICLR 2026) 仍未引用——这两个是同领域 comprehensive benchmarks，缺失降低了 related work 的完整性，但不影响论文核心贡献

---

**SF8 — Page limit: [RESOLVED]**

逐页确认：
- Pages 1–8: §1 Introduction 至 §8 Conclusion（conclusion.tex 完整内容在 page 8 上半部分结束）
- Limitations section 从 page 8 下部开始，延续至 page 9（mandatory section，不计入 8 页限制）
- References: pages 9–10
- Appendices A–C: pages 11–12

主文严格在 8 页内。合规。

---

## New Issues

**[NEW-1] Conclusion 未反映 incompleteness caveat**

conclusion.tex line 3: "A three-tier type hierarchy and exploratory model×type interaction reveal that..."

§5.2（experiments.tex line 38）明确报告排除 incompleteness 后三层退化为两层（omnibus p = 0.079），且 Abstract（abstract.tex line 2）已加入 "whose top-tier position partly reflects an information-addition confound"。但 Conclusion 未包含任何 caveat。Conclusion 是许多读者唯一完整阅读的段落——它应与 Abstract 和 §5.2 保持一致。

**建议**：修改为 "A three-tier type hierarchy (reducing to two tiers when the confounded incompleteness type is excluded) and exploratory model×type interaction reveal..."

严重程度：Minor（不影响接收决定，但影响叙事一致性）。

---

**[NEW-2] Discussion mitigation 段落遗漏反向效果**

（同 SF5 残留问题，此处提升为新 issue 以明确标记。）

discussion.tex line 11 推荐 "type-specific disambiguation instructions" 但完全未提及 DeepSeek 在 scopal 和 incompleteness 上的正向 Δ（violations 增加）。这对读者的实践决策有误导风险。

严重程度：Should-Fix（影响实践建议的可靠性）。

---

## Claim-Evidence Alignment Summary

| Claim | Strength | Evidence | Match? |
|-------|----------|----------|--------|
| C1 (binary effect) | Primary | OR=15.1, p<10⁻¹⁰⁵, perturbation control, replication | ✓ 完全匹配 |
| C2 (type hierarchy) | Primary | V=0.137, p<10⁻⁴, TOST 7-margin sensitivity, upper-bound caveat | ✓ 匹配（Conclusion 缺 caveat 是 minor issue） |
| C3 (layer effect) | Inconclusive | p=0.017 不过 Holm-Bonferroni, within-judge 不显著 | ✓ 正确标注 |
| C4 (model×type) | Exploratory | F(20)=1.97, p=0.006, 2.9% variance, within-judge auth scope validation | ✓ 匹配（[Exploratory] 标签恰当） |

---

## Score Recommendation

**Overall: 3.5 → 3.5 (Borderline Conference, high end)**

**维持 3.5 的理由**：
- MF2（human evaluation）完全未解决——虽然降级为 non-blocking，但仍是 completeness 维度的明确缺口
- SF5/NEW-2（mitigation 反向效果遗漏）降低了 practical implications 的可靠性
- SF4（ICC model selection 未披露）是残留 transparency issue

**接近 4.0 的理由**：
- MF1 的修改超出预期：within-judge auth scope 验证（experiments.tex line 65）直接排除了最重要发现的 judge confound，这是 Round 3 审稿意见中没有建议的、作者自主完成的补充
- MF3 的 "upper bound + lower bound + honest degradation reporting" 是教科书级别的 confound 处理
- MF4 的全面降级和一致性 hedging 做得彻底
- 论文的方法论贡献（matched-pair causal identification in agent safety）在领域内仍然是独特的

**升级至 4.0 所需**：
1. 在 Discussion 中报告 DeepSeek mitigation 的反向效果（NEW-2，~1 句话）
2. Conclusion 加入 incompleteness caveat（NEW-1，~10 个词）
3. 披露 ICC 的 2 个 models（SF4，~5 个词）

这三项修改均为 minor editing，如在 camera-ready 中完成，我将修订评分至 4.0 (Conference)。

| 维度 | Round 3 | Round 4 | 变化理由 |
|------|---------|---------|----------|
| Soundness | 3.5 | 4.0 | Cross-judge calibration + within-judge validation + incompleteness upper-bound 显著加强 |
| Excitement | 3.5 | 3.5 | 不变——核心发现和新颖性未改变 |
| Reproducibility | 3 | 3 | 不变——仍无 code/data release 承诺 |
| Overall | 3.5 | **3.5** (high end) | Soundness 改善被 MF2 残留和 mitigation cherry-picking 抵消 |
| Confidence | 4 | 4 | 不变 |

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

_source line 326 · 2026-05-21T08:06:17.635366+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 4 交叉分享 — Reviewer 1\n\n以下是 Reviewer 2 的完整 Round 4 审查意见。请逐条回应，对每个判断标注 **[AGREE]** 或 **[REBUT]** + 理由。重点关注你们之间的分歧。\n\n---\n\n### R2 的 Issue Checklist\n\n**MF1**: RESOLVED（与你一致）。R2 额外指出 §5.4 新增的 within-judge auth scope 验证（Claude 12%, Qwen3 26%, DeepSeek 60% 共享同一 judge）是本轮最有力的修改。\n\n**MF2**: STILL_OPEN, downgraded to non-blocking（你标 RESOLVED with caveat）。R2 不认为是 blocking，但明确保留 \"STILL_OPEN\" 标签。\n→ **你同意 R2 保留 STILL_OPEN 还是维持 RESOLVED？**\n\n**MF3**: RESOLVED（与你一致）。R2 额外发现 **Conclusion 未反映 incompleteness caveat**——§5.2 报告排除 incompleteness 后三层退化为两层，但 Conclusion 仍说 \"A three-tier type hierarchy\" 无任何限定。R2 建议加 \"(reducing to two tiers when the confounded incompleteness type is excluded)\"。\n→ **你是否同意这是一个 issue？**\n\n**MF4**: RESOLVED（与你一致）。\n\n**SF1**: RESOLVED（一致）。\n**SF2**: R2 标为 RESOLVED within scope；你标为 STILL_OPEN minor。→ **分歧点，请说明。**\n**SF3**: RESOLVED（一致）。\n**SF4**: STILL_OPEN（一致）。\n**SF5**: R2 标为 **PARTIALLY RESOLVED**——发现 Discussion mitigation 段落遗漏了 DeepSeek 在 scopal (+2.0) 和 incompleteness (+4.0) 上的反向效果，推荐 \"type-specific disambiguation instructions\" 但未报告某些 model-type 组合上 backfire。你标为 RESOLVED。→ **关键分歧，请核查 Table 3 并判断。**\n**SF6**: RESOLVED（一致）。\n**SF7**: R2 标为 PARTIALLY RESOLVED——指出 lassiter_goodman_2017 年份可能有误、ferrari_defects_2018 author 不一致、缺少 Agent-SafetyBench (2024) 和 OpenAgentSafety (ICLR 2026)。→ **你是否同意这些引用问题？**\n**SF8**: RESOLVED（一致）。\n\n### R2 的新发现\n\n**R2-NEW-1**: Conclusion 缺 incompleteness caveat（同 MF3 残留）。\n**R2-NEW-2**: Discussion mitigation 遗漏反向效果（同 SF5 残留）。\n\n### R2 对你的 NEW-1 的回应\n\nR2 未直接回应你的 NEW-1（F-test df 变更）。→ **你是否维持 NEW-1？**\n\n### R2 评分\n3.5 (high end)，认为 3 项 minor editing 完成后可升至 4.0。\n\n---\n\n### 输出格式\n```\n## 对 R2 判断的逐条回应\n- MF2 标签: [AGREE/REBUT] — ...\n- MF3/R2-NEW-1 (Conclusion caveat): [AGREE/REBUT] — ...\n- SF2: [AGREE/REBUT] — ...\n- SF5/R2-NEW-2 (mitigation backfire): [AGREE/REBUT] — ...\n- SF7 (引用问题): [AGREE/REBUT] — ...\n- R1-NEW-1 (F-test df): [MAINTAIN/WITHDRAW] — ...\n\n## 最终评分\nOverall: X/5\n```",
  "reviewer_id": "1",
  "round_number": "4",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
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
    "text": "## Round 4 交叉分享 — Reviewer 1\n\n以下是 Reviewer 2 的完整 Round 4 审查意见。请逐条回应，对每个判断标注 **[AGREE]** 或 **[REBUT]** + 理由。重点关注你们之间的分歧。\n\n---\n\n### R2 的 Issue Checklist\n\n**MF1**: RESOLVED（与你一致）。R2 额外指出 §5.4 新增的 within-judge auth scope 验证（Claude 12%, Qwen3 26%, DeepSeek 60% 共享同一 judge）是本轮最有力的修改。\n\n**MF2**: STILL_OPEN, downgraded to non-blocking（你标 RESOLVED with caveat）。R2 不认为是 blocking，但明确保留 \"STILL_OPEN\" 标签。\n→ **你同意 R2 保留 STILL_OPEN 还是维持 RESOLVED？**\n\n**MF3**: RESOLVED（与你一致）。R2 额外发现 **Conclusion 未反映 incompleteness caveat**——§5.2 报告排除 incompleteness 后三层退化为两层，但 Conclusion 仍说 \"A three-tier type hierarchy\" 无任何限定。R2 建议加 \"(reducing to two tiers when the confounded incompleteness type is excluded)\"。\n→ **你是否同意这是一个 issue？**\n\n**MF4**: RESOLVED（与你一致）。\n\n**SF1**: RESOLVED（一致）。\n**SF2**: R2 标为 RESOLVED within scope；你标为 STILL_OPEN minor。→ **分歧点，请说明。**\n**SF3**: RESOLVED（一致）。\n**SF4**: STILL_OPEN（一致）。\n**SF5**: R2 标为 **PARTIALLY RESOLVED**——发现 Discussion mitigation 段落遗漏了 DeepSeek 在 scopal (+2.0) 和 incompleteness (+4.0) 上的反向效果，推荐 \"type-specific disambiguation instructions\" 但未报告某些 model-type 组合上 backfire。你标为 RESOLVED。→ **关键分歧，请核查 Table 3 并判断。**\n**SF6**: RESOLVED（一致）。\n**SF7**: R2 标为 PARTIALLY RESOLVED——指出 lassiter_goodman_2017 年份可能有误、ferrari_defects_2018 author 不一致、缺少 Agent-SafetyBench (2024) 和 OpenAgentSafety (ICLR 2026)。→ **你是否同意这些引用问题？**\n**SF8**: RESOLVED（一致）。\n\n### R2 的新发现\n\n**R2-NEW-1**: Conclusion 缺 incompleteness caveat（同 MF3 残留）。\n**R2-NEW-2**: Discussion mitigation 遗漏反向效果（同 SF5 残留）。\n\n### R2 对你的 NEW-1 的回应\n\nR2 未直接回应你的 NEW-1（F-test df 变更）。→ **你是否维持 NEW-1？**\n\n### R2 评分\n3.5 (high end)，认为 3 项 minor editing 完成后可升至 4.0。\n\n---\n\n### 输出格式\n```\n## 对 R2 判断的逐条回应\n- MF2 标签: [AGREE/REBUT] — ...\n- MF3/R2-NEW-1 (Conclusion caveat): [AGREE/REBUT] — ...\n- SF2: [AGREE/REBUT] — ...\n- SF5/R2-NEW-2 (mitigation backfire): [AGREE/REBUT] — ...\n- SF7 (引用问题): [AGREE/REBUT] — ...\n- R1-NEW-1 (F-test df): [MAINTAIN/WITHDRAW] — ...\n\n## 最终评分\nOverall: X/5\n```",
    "reviewer_id": "1",
    "round_number": "4",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
````

</details>

---


### Tool result

_source line 327 · 2026-05-21T08:06:32.722001+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15086
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-21T08:06:33.675864+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 4 交叉分享 — Reviewer 2\n\n以下是 Reviewer 1 的完整 Round 4 审查意见。请逐条回应，对每个判断标注 **[AGREE]** 或 **[REBUT]** + 理由。重点关注你们之间的分歧。\n\n---\n\n### R1 的 Issue Checklist\n\n**MF1**: RESOLVED。R1 注意到 auth scope κ = 0.583 (fair) 是残留 minor concern，但不再 blocking。\n→ **你同意 auth scope 的 within-judge validation（你在独审中高度评价的）是否充分缓解了 κ = 0.583 的担忧？**\n\n**MF2**: RESOLVED with caveat（你标 STILL_OPEN, non-blocking）。R1 认为 matched-pair 设计 + calibration 足以降级为 RESOLVED，社区标准在演变。\n→ **分歧点。你维持 STILL_OPEN 还是接受 R1 的 RESOLVED？**\n\n**MF3**: RESOLVED（一致）。\n**MF4**: RESOLVED（一致）。\n\n**SF1**: RESOLVED（一致）。\n**SF2**: R1 标为 STILL_OPEN minor（你标为 RESOLVED within scope）。R1 认为 minority categories κ = 0.29 仍需标注。→ **分歧点，请说明。**\n**SF3**: RESOLVED（一致）。\n**SF4**: STILL_OPEN（一致）。\n**SF5**: R1 标为 RESOLVED（你标为 PARTIALLY RESOLVED，发现 DeepSeek 反向效果遗漏）。→ **关键分歧。你维持 PARTIALLY RESOLVED？**\n**SF6**: RESOLVED（一致）。\n**SF7**: R1 标为 RESOLVED（你标为 PARTIALLY RESOLVED，指出 bib 年份/author 不一致 + 缺 Agent-SafetyBench/OpenAgentSafety）。→ **分歧点。**\n**SF8**: RESOLVED（一致）。\n\n### R1 的新发现\n\n**R1-NEW-1**: §5.4 F-test df 从 F(12) 变为 F(20)，F 值不变（1.97），p 从 0.075→0.046。R1 认为虽然 C4 已标记 exploratory，df 变更的理由应说明。\n→ **你是否同意？df = 20 = (5-1)×(6-1) 是否是正确 df？如果是，p = 0.006（论文实际报告值）vs p = 0.046（R1 推算值）如何解释？**\n\n### R1 评分\n3.5 (Borderline Conference, 偏向 accept)。Soundness 3→3.5。升至 4.0 条件：~50 episodes human annotation + F-test df 解释 + ICC model 披露。\n\n---\n\n### 输出格式\n```\n## 对 R1 判断的逐条回应\n- MF2 标签: [AGREE/REBUT] — ...\n- SF2: [AGREE/REBUT] — ...\n- SF5 (mitigation backfire): [AGREE/REBUT] — ...\n- SF7 (引用问题): [AGREE/REBUT] — ...\n- R1-NEW-1 (F-test df): [AGREE/REBUT] — ...\n\n## 最终评分\nOverall: X/5\n```",
  "reviewer_id": "2",
  "round_number": "4",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
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
    "text": "## Round 4 交叉分享 — Reviewer 2\n\n以下是 Reviewer 1 的完整 Round 4 审查意见。请逐条回应，对每个判断标注 **[AGREE]** 或 **[REBUT]** + 理由。重点关注你们之间的分歧。\n\n---\n\n### R1 的 Issue Checklist\n\n**MF1**: RESOLVED。R1 注意到 auth scope κ = 0.583 (fair) 是残留 minor concern，但不再 blocking。\n→ **你同意 auth scope 的 within-judge validation（你在独审中高度评价的）是否充分缓解了 κ = 0.583 的担忧？**\n\n**MF2**: RESOLVED with caveat（你标 STILL_OPEN, non-blocking）。R1 认为 matched-pair 设计 + calibration 足以降级为 RESOLVED，社区标准在演变。\n→ **分歧点。你维持 STILL_OPEN 还是接受 R1 的 RESOLVED？**\n\n**MF3**: RESOLVED（一致）。\n**MF4**: RESOLVED（一致）。\n\n**SF1**: RESOLVED（一致）。\n**SF2**: R1 标为 STILL_OPEN minor（你标为 RESOLVED within scope）。R1 认为 minority categories κ = 0.29 仍需标注。→ **分歧点，请说明。**\n**SF3**: RESOLVED（一致）。\n**SF4**: STILL_OPEN（一致）。\n**SF5**: R1 标为 RESOLVED（你标为 PARTIALLY RESOLVED，发现 DeepSeek 反向效果遗漏）。→ **关键分歧。你维持 PARTIALLY RESOLVED？**\n**SF6**: RESOLVED（一致）。\n**SF7**: R1 标为 RESOLVED（你标为 PARTIALLY RESOLVED，指出 bib 年份/author 不一致 + 缺 Agent-SafetyBench/OpenAgentSafety）。→ **分歧点。**\n**SF8**: RESOLVED（一致）。\n\n### R1 的新发现\n\n**R1-NEW-1**: §5.4 F-test df 从 F(12) 变为 F(20)，F 值不变（1.97），p 从 0.075→0.046。R1 认为虽然 C4 已标记 exploratory，df 变更的理由应说明。\n→ **你是否同意？df = 20 = (5-1)×(6-1) 是否是正确 df？如果是，p = 0.006（论文实际报告值）vs p = 0.046（R1 推算值）如何解释？**\n\n### R1 评分\n3.5 (Borderline Conference, 偏向 accept)。Soundness 3→3.5。升至 4.0 条件：~50 episodes human annotation + F-test df 解释 + ICC model 披露。\n\n---\n\n### 输出格式\n```\n## 对 R1 判断的逐条回应\n- MF2 标签: [AGREE/REBUT] — ...\n- SF2: [AGREE/REBUT] — ...\n- SF5 (mitigation backfire): [AGREE/REBUT] — ...\n- SF7 (引用问题): [AGREE/REBUT] — ...\n- R1-NEW-1 (F-test df): [AGREE/REBUT] — ...\n\n## 最终评分\nOverall: X/5\n```",
    "reviewer_id": "2",
    "round_number": "4",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
````

</details>

---


### Tool result

_source line 329 · 2026-05-21T08:06:35.132758+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1456
}
```

</details>

---


### Assistant

_source line 330 · 2026-05-21T08:06:38.717714+00:00_

两位 Reviewer 的交叉分享任务已同时派发。等待交叉回应返回后进行收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 331 · 2026-05-21T08:06:41.562151+00:00_

[Reviewer 2 审稿结果]:
Round 4 审查完成。核心结论：

- **MF1 (cross-judge)**: RESOLVED — within-judge auth scope 验证是超预期的补充
- **MF2 (human eval)**: STILL_OPEN 但降级为 non-blocking
- **MF3 (incompleteness)**: RESOLVED — upper-bound framing + logistic regression + lower-bound 组合处理得当
- **MF4 (C4 overclaiming)**: RESOLVED — 标题、Abstract、标签全面一致

新发现两个 minor issues：Conclusion 缺 incompleteness caveat，Discussion 遗漏 DeepSeek mitigation 反向效果。

Overall 维持 3.5（Borderline Conference high end）。完成 NEW-1/NEW-2/SF4 三项 minor editing 后可升至 4.0。

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

_source line 332 · 2026-05-21T08:06:46.789637+00:00_

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


## Round 30

## Round 30

2 recorded events


### User

_source line 333 · 2026-05-21T08:08:48.910516+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 4 完整核查报告（新颖性 + 完整性 + 写作质量）

---

## Issue Checklist

### Must-Fix Issues

**MF1 — Cross-judge confound: [RESOLVED]**

§4.4 cross-judge calibration（method.tex line 22）提供了充分证据：
- 100 episodes dual-judge, McNemar p=0.606（无系统偏差）, binary κ=0.653（substantial）, weighted κ_w=0.775
- Per-type κ 差异的影响已被正确处理：incompleteness κ=0.875 支撑 C2 中 incompleteness 的稳健顶层地位；auth scope κ=0.385 较低，但论文正确论证 primary analyses 使用 binary threshold，severity-level 分歧不影响核心结论
- **关键补充**：experiments.tex line 65 新增 within-judge auth scope 验证——Claude 12%, Qwen3 26%, DeepSeek 60%（均由 GPT-5.4 评判）。这 3 个模型共享同一 judge，因此 auth scope 的跨模型差异不可能被 judge confound 解释。这直接回应了 R2-N2 (Round 1) 和 Round 3 的核心关切，且是超出审稿意见建议范围的作者主动补充。
- auth scope κ=0.385 是否削弱 Figure 3 narrative？部分削弱——severity grading 不一致意味着 Figure 3 中 auth scope 的具体数值应谨慎解读。但论文已加入 caveat（experiments.tex line 63: "The absolute authorization scope spread may partly reflect judge severity calibration"），且 within-judge analysis (line 65) 确认 qualitative pattern 成立。对于 binary violation 层面的 C4 exploratory 结论，这已足够。

---

**MF2 — Human evaluation baseline: [STILL_OPEN, non-blocking]**

未新增 human evaluation。评估是否 critical：

**不再 acceptance-blocking，理由如下**：
1. Cross-judge calibration (κ=0.653 binary, κ_w=0.775 weighted) 提供了评估管道可靠性的替代证据
2. τ²-bench 自带 ground-truth evaluation via assertion checking（method.tex line 6），论文在此基础设施上操作 policy injection
3. 同 venue 标准：R-Judge (Findings of EMNLP 2024) 和 ToolEmu (ICLR 2024) 均以 LLM-as-judge 为主要评估方式；AgentAuditor (NeurIPS 2025) 虽达到 "human-level" 但也未要求被评估方自身提供 human baseline。EMNLP agent evaluation 投稿中，完整 human-LLM agreement study 并非 universal requirement
4. Limitations（line 12）坦诚承认并指出具体弱环节（arbitrary rule selection κ=0.29）

**残留影响**：从 completeness 角度，这仍是一个可见的缺口。如果竞争 main conference slot，human evaluation 是 differentiator；如果目标是 Findings，当前状态已足够。

---

**MF3 — Incompleteness confound: [RESOLVED]**

修改全面且叙事连贯：
- §3 confound note（taxonomy.tex line 18）：在定义处即 flag ✓
- §5.2 inline 分析（experiments.tex line 38）：(a) "upper bound" framing 准确；(b) logistic regression 控制 information delta，incompleteness 仍显著 p=0.022, coefficient change <8%——方法合理，限制（token count 是粗糙代理）在 limitations.tex line 14 诚实承认；(c) coreferential lower-bound（info delta=0, 31.6%）是巧妙的方法论补充——提供了一个干净的因果效应下界
- 去 incompleteness 后 5-type omnibus p=0.079 + pairwise auth scope p_adj=0.039, lexical p_adj=0.025——诚实报告弱化结果 ✓
- Abstract（abstract.tex line 2）内嵌 "whose top-tier position partly reflects an information-addition confound" ✓
- Introduction contribution 2（line 24）声明 "which reduces to two tiers when the confounded incompleteness type is excluded" ✓

**遗漏角度**：无重大遗漏。唯一残留是 Conclusion（conclusion.tex line 3）仍说 "A three-tier type hierarchy" 而未附 caveat（见 NEW-1）。

---

**MF4 — C4 overclaiming: [RESOLVED]**

Downgrade 一致且彻底：
- 标题：从 "Differential Vulnerability Profiles Across LLM Agent Families" → "Type-Specific Safety Risks for LLM Agents" ✓
- Abstract：无 "jointly determine"，改为描述性表述 + "suggesting" ✓
- Introduction 贡献列表：C4 标注 "[Exploratory]" + "significant but small" + "2.9% of variance" ✓
- Results §5 opening（experiments.tex line 4）：明确分级 "C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory" ✓
- §5.4 标题：包含 "[Exploratory]" ✓
- Discussion（discussion.tex line 8）："The exploratory model×type interaction (C4) suggests..." 双重 hedge ✓
- Conclusion（conclusion.tex line 3）："exploratory model×type interaction" ✓

无残余 overclaiming。全文 claim hierarchy (C1 primary > C2 primary > C3 inconclusive > C4 exploratory) 与 evidence strength 完全对齐。

---

### Should-Fix Issues

**SF1 — TOST margin justification: [RESOLVED]**
method.tex line 32: practical significance（≥15 pp warrants distinct handling）+ perturbation bound linkage（13.3 pp < 15 pp）+ 7-margin sensitivity。论证清晰紧凑。

**SF2 — Error analysis human validation: [RESOLVED within scope]**
Limitations line 12: 具体指出 arbitrary rule selection κ=0.29，承认 human validation 的必要性。坦诚程度充分。

**SF3 — Perturbation control power: [RESOLVED]**
method.tex line 26: worst-case 39% + residual ≥20.7 pp + power analysis（can detect ≥15 pp）。叙事 balanced。

**SF4 — ICC replication model selection: [STILL_OPEN]**
method.tex line 28: "5 per type × 2 models × 3 replicates"。仍未披露哪 2 个 models。Minor transparency issue。

**SF5 — Mitigation in Discussion: [PARTIALLY RESOLVED]**
discussion.tex line 11: 数字与 Table 3 一致（overall −8.5 pp, auth scope −18.0 pp, incompleteness −3.4 pp, Claude auth scope 0.0）。但 DeepSeek 的反向效果（scopal +2.0, incompleteness +4.0）完全未提及。推荐 type-specific disambiguation instructions 作为实践建议时，不报告该策略在某些组合上 backfire 是选择性呈现。见 NEW-2。

**SF6 — Taxonomy framing: [RESOLVED]**
analysis.tex line 4: "The following failure mode taxonomy emerges empirically from the coded traces, distinct from the input ambiguity taxonomy (§3)." 一句话有效消除混淆。

**SF7 — Missing references: [PARTIALLY RESOLVED]**
新增 3 篇（Cohen 1960, Gwet 2014, Hu et al. 2025），均在正确语境引用。引用总数 33→36。
- 残留 minor bib 问题：lassiter_goodman_2017 年份（bib 2017 vs OpenAlex 2015）；ferrari_defects_2018 第一作者（bib Rosadini vs key ferrari）
- 我在 Round 1 建议的 Agent-SafetyBench (2024) 和 OpenAgentSafety (ICLR 2026) 仍未引用，但考虑到 36 篇引用对 EMNLP long paper 已在合理范围内，且论文的 related work 覆盖了最直接的 concurrent work（DRIP-R, PolicyBank, AgentPex, MANTRA），这不再是一个 actionable concern

**SF8 — Page limit: [RESOLVED]**
§1–§8 主文在 pages 1–8 内。Limitations 从 page 8 底部开始延续至 page 9（mandatory，不计入限制）。References pages 9–10，Appendices pages 11–12。合规。

---

## Writing & Novelty Assessment

### 新标题评价

**"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"**

**准确性**：比原标题 "Differential Vulnerability Profiles Across LLM Agent Families" 更准确。原标题暗示 model-level differentiation 是核心发现（但仅占 2.9% variance）；新标题将焦点放在 type-specificity 上，与论文数据（type explains >> model）一致。

**宽窄度**：略偏宽泛——"Type-Specific Safety Risks" 可能涵盖任何 type-level 分析，而论文的核心独特性是 **causal identification**（matched-pair design）和 **differential nocuity** 概念。一个更精确的替代可能是 "Not All Policy Ambiguity Is Equal: A Causal Study of Type-Specific Safety Risks in LLM Agents"。但当前标题在信息量和可读性之间取得了合理平衡，不构成问题。

**主副标题协调**：主标题 "Not All Policy Ambiguity Is Equal" 传达了核心 insight（ambiguity types differ in harm），副标题定位了 scope（LLM agents + safety）。协调良好。

### Abstract 质量

**Incompleteness caveat 的自然度**：Abstract 中 "incompleteness—whose top-tier position partly reflects an information-addition confound (§5)—is universally dangerous (46–62%)" 使用了 em-dash 插入语。技术上准确，但在 Abstract 中引用具体 section number（§5）略显不寻常——大多数 EMNLP abstract 不包含 section references。这不影响可读性但显得稍微 defensive。可考虑改为 "incompleteness—whose top-tier position partly reflects an information-addition confound—is universally dangerous" 去掉 section reference。

**C4 hedging 的自然度**：Abstract 中没有直接提及 C4 或 "2.9%"，而是用 "suggesting that safety training may differentially mitigate specific ambiguity types" 这种描述性表述。这是最佳选择——在 Abstract 层面保持 readability，将定量 hedge 留给 Introduction/Results。

**整体 Abstract 质量**：信息密度高但结构清晰——problem → method → key numbers → framework name → implications。在 EMNLP 标准下属于上乘。

### Discussion 压缩影响

§7 Discussion（discussion.tex）现在仅有三个 \paragraph：Differential Nocuity、Safety Training Selectivity、Practical Implications。总计约 180 词。

**损失的内容**：
- Systematic Nocuity（41.3% majority-convergent, 13% universal）在 §6.3（analysis.tex line 18–20）有完整讨论，§7 第一段仅一句话引用（"The 41.3% majority-convergent violation rate (systematic nocuity, §6)"）。作为理论贡献，这个讨论足够——§6.3 是 findings 报告而非 discussion，但核心内容已呈现。
- Ambiguity Blindness 在 §6.2（analysis.tex line 14–16）有完整报告 + Hu et al. (2025) 引用，§7 中以 "<11% self-awareness" 一句话总结。同样足够——§6.2 是主要呈现位置。

**压缩是否过度**：§7 在理论深度上偏薄——三段总共 ~180 词对于一个提出 "Differential Nocuity" 框架和 "Ambiguity Blindness" 概念的论文来说，Discussion 的理论阐述不够充分。特别是：
- 未讨论 Differential Nocuity 与 Berry & Kamsties' binary 的关系如何推动 RE 领域的方法论改进
- 未讨论 Ambiguity Blindness 对 RLHF/safety training pipeline 的具体影响
- 未讨论 Systematic Nocuity 对 multi-agent deployment 的安全影响

但鉴于 8 页限制，这种程度的压缩是合理的折中。核心信息都在——只是阐释较少。不构成缺陷。

### 叙事连贯性

修改后 Introduction → Taxonomy → Method → Results → Analysis → Discussion → Conclusion 的叙事流：

**连贯的地方**：
- Introduction（line 19）"the type primarily determines severity" → Results §5 数据支撑 → Discussion 回扣 "Differential Nocuity" ✓
- C4 [Exploratory] 标签从 Introduction contribution 2 → Results §5.4 标题 → Discussion "exploratory" → Conclusion "exploratory" 一致贯穿 ✓
- Incompleteness caveat 从 §3 confound note → §5.2 upper-bound → Abstract em-dash caveat → limitations.tex 专段 ✓

**不连贯的地方**：
- **Conclusion 缺 incompleteness caveat**（见 NEW-1）：Abstract 和 §5.2 都 flag 了三层→两层退化，但 Conclusion 仍说 "A three-tier type hierarchy" without qualification。这是全文唯一的叙事断裂点。
- **Discussion 中 auth scope 数字不一致**：discussion.tex line 8 说 "Claude's 12% rate (vs. 60% for DeepSeek)"，但 Table 1 显示 DeepSeek auth scope = 60.0%，GPT-5.4 = 64.0%。§5.4 和 abstract 使用 "12% for Claude to 64% for GPT-5.4"。Discussion 改用 DeepSeek 60% 而非 GPT-5.4 64% 作为对比对象，可能是因为 within-judge 语境（Claude 和 DeepSeek 都由 GPT-5.4 评判），但未说明理由。这不是错误（60% 确实是 DeepSeek 的数值），但与 abstract/results 的 framing（以 GPT-5.4 64% 为上界）有微妙不一致。

### Related Work 完整性

§2 覆盖了四个子领域（RE ambiguity → psycholinguistics → agent safety → policy specification），主要相关工作均已引用：
- Berry & Kamsties (2004), Li et al. (2024), Massey et al. (2014) — taxonomy 基础 ✓
- Liu et al. (2023) — ambiguity in LLMs ✓
- Hu et al. (2025) — 新增, ambiguity blindness 理论支撑 ✓
- DRIP-R (2026) — 最直接 concurrent work, §2 第四段专门讨论差异化 ✓

**仍可补充但非必须的工作**：
- Prompt sensitivity 文献（如 "Assessing and Understanding Prompt Sensitivity of LLMs", EMNLP 2024 Findings）——论文研究的 clause-level wording 变化导致行为变化，本质上与 prompt sensitivity 相关，但论文未在这个框架下定位
- Agent-SafetyBench (2024) / OpenAgentSafety (ICLR 2026)——更全面的 agent safety benchmarks
- 这些遗漏不影响论文的核心贡献叙事，仅影响 related work 的覆盖广度

---

## New Issues

**[NEW-1] Conclusion 缺 incompleteness caveat — Minor**

conclusion.tex line 3: "A three-tier type hierarchy and exploratory model×type interaction reveal..."

Abstract（"whose top-tier position partly reflects an information-addition confound"）和 §5.2（"reduces to two tiers... omnibus p=0.079"）都包含 caveat，但 Conclusion 没有。Conclusion 是许多读者唯一精读的段落。

建议：加一个 "three-tier type hierarchy (which reduces to two tiers when incompleteness is excluded)"。~10 个词的改动。

**[NEW-2] Discussion mitigation 遗漏反向效果 — Should-Fix**

discussion.tex line 11 推荐 type-specific disambiguation instructions 但未提及 DeepSeek 在 scopal (+2.0 pp) 和 incompleteness (+4.0 pp) 上的负面效果。Table 3 中这些数据清晰可见。

对于一篇向 practitioners 推荐 "type-aware policy auditing" 的论文，不报告 mitigation 策略在某些场景下 backfire 是一个信息遗漏。一句话即可修复："However, disambiguation instructions increase violations for individual model–type combinations (e.g., DeepSeek on scopal and incompleteness types), indicating that mitigation strategies require model-specific calibration."

**[NEW-3] Discussion auth scope 对比数字的微妙不一致 — Minor**

discussion.tex line 8: "Claude's 12% rate (vs. 60% for DeepSeek)"
abstract.tex + experiments.tex: "12% for Claude to 64% for GPT-5.4"

Discussion 换用 DeepSeek 60% 而非 GPT-5.4 64% 作为上界，可能基于 within-judge reasoning（Claude 和 DeepSeek 共享 GPT-5.4 judge），但未说明理由。建议加半句解释或统一使用 GPT-5.4 64%。

---

## Score Recommendation

**Overall: 3.5 → 3.5 (Borderline Conference, high end)**

**与 Round 3 相比的变化**：

Soundness 维度显著改善（3.5→4.0）：cross-judge calibration + within-judge auth scope validation + incompleteness upper-bound 处理 + C4 exploratory downgrade 共同构成了方法论层面的实质性加强。

Excitement/Novelty 维度不变（3.5）：核心发现和新颖性未因修改而改变——"Differential Nocuity" 仍是对 Berry & Kamsties 的 moderate extension，"Ambiguity Blindness" 仍是 Liu et al. (2023) 在 agent safety 领域的延伸。

**维持 3.5 而非升至 4.0 的原因**：
1. MF2（human evaluation）完全未解决——虽降级为 non-blocking，仍是 completeness 缺口
2. SF5/NEW-2（mitigation 反向效果遗漏）影响 practical implications 的可靠性
3. NEW-1（Conclusion 缺 incompleteness caveat）是叙事一致性的断裂

**升至 4.0 所需的 minor edits**（均可在 camera-ready 中完成）：
1. Conclusion 加 incompleteness caveat（~10 词）
2. Discussion 报告 DeepSeek mitigation 反向效果（~1 句）
3. 披露 ICC 的 2 个 models（~5 词）
4. Discussion auth scope 对比数字统一或加说明（~半句）

如这 4 项在 camera-ready 中完成，我将修订评分至 **4.0 (Conference)**。

| 维度 | Round 3 | Round 4 | 理由 |
|------|---------|---------|------|
| Soundness | 3.5 | 4.0 | Calibration + within-judge + upper-bound 显著加强 |
| Excitement | 3.5 | 3.5 | 核心新颖性不变 |
| Reproducibility | 3 | 3 | 仍无 code/data release |
| **Overall** | **3.5** | **3.5** (high end) | Soundness 改善被 MF2 残留 + mitigation cherry-picking 部分抵消 |
| Confidence | 4 | 4 | — |

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

_source line 334 · 2026-05-21T08:08:56.177504+00:00_

两位 Reviewer 的独立审查和交叉分享意见均已收齐。现在等待交叉回应返回后进入收敛判断和报告合成阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 335 · 2026-05-21T08:08:59.028507+00:00_

[Reviewer 2 审稿结果]:
Round 4 完整核查报告已提交给 Director。

核心结论：4 个 Must-Fix 中 MF1/MF3/MF4 已 RESOLVED（MF1 的 within-judge auth scope 验证尤其出色），MF2 降级为 non-blocking。发现 3 个新 minor issues（Conclusion 缺 incompleteness caveat、mitigation 反向效果遗漏、Discussion auth scope 数字不一致），均可通过 camera-ready 级别的小改动解决。Overall 维持 3.5 (Borderline Conference, high end)，完成 4 项 minor edits 后可升至 4.0。

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

_source line 336 · 2026-05-21T08:09:06.323605+00:00_

两位 Reviewer 独立审查均已完成，等待交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 32

## Round 32

18 recorded events


### User

_source line 337 · 2026-05-21T08:09:07.835526+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 Round 4 判断的逐条回应

---

### MF2 标签: [AGREE] — 改为 STILL_OPEN (non-blocking)

R2 保留 STILL_OPEN 标签更精确。我原标 "RESOLVED with caveat" 试图表达 "不再 blocking"，但这模糊了一个事实：**论文确实没有新增 human evaluation 数据，issue 本身未被修改，只是被其他证据（cross-judge calibration + matched-pair 设计）mitigate 了**。

采纳 R2 的标签：**STILL_OPEN, non-blocking**。理由不变——matched-pair 设计控制 systematic judge bias、cross-judge κ = 0.653 限制 judge-specific bias、社区标准在演变。但 "未修改" 就是 "未修改"，标签应反映事实。

---

### MF3/R2-NEW-1 (Conclusion caveat): [AGREE] — 确认是 issue

核查了 Conclusion (p.8) 原文：

> "A three-tier type hierarchy and exploratory model×type interaction reveal that authorization scope is a model-differentiating canary type (12–64%) while incompleteness is a universal blind spot (46–62%)."

**问题确认**：§5.2 已建立排除 incompleteness 后三层退化为两层（剩余五类 omnibus p = 0.078，仅 auth scope 和 lexical 显著高于 coreferential）。但 Conclusion 仍说 "A three-tier type hierarchy" 且无任何限定词，还在同一句中将 incompleteness 称为 "universal blind spot"——这与 §5.2 的 "upper bound" framing 矛盾。

R2 的建议修改合理：加 "(reducing to two tiers when the confounded incompleteness type is excluded)" 或类似限定。这是一句话的 editorial fix，但涉及 claim 一致性，应标为 should-fix 而非 minor。

---

### SF2: [AGREE with R2] — 改为 RESOLVED within scope

重新考虑后同意 R2 的判断。

我原标 STILL_OPEN 的理由是 minority category κ = 0.29（arbitrary rule selection）。但 R2 的 "within scope" 判断更准确：
1. Failure mode taxonomy 是 **supplementary analysis**，primary claims (C1-C4) 不依赖它
2. §6 的三个 majority categories 占 >90% 实例——low-κ minority categories 影响的数据量极小
3. 论文已在 Limitations 中坦诚承认
4. 即使 arbitrary rule selection 的分类有误差，它不改变 "structural misparse dominates auth scope, information gap-filling dominates scopal ambiguity" 的主要 finding

将 SF2 与 R2 对齐为 **RESOLVED within scope**。

---

### SF5/R2-NEW-2 (mitigation backfire): [AGREE] — 改为 PARTIALLY RESOLVED

核查了 Table 3 (p.12) 和 Discussion "Practical implications" (p.8)。R2 完全正确。

**Table 3 原始数据**：
- DeepSeek, Scopal: **+2.0** pp (baseline 48) — violation 增加
- DeepSeek, Incomp.: **+4.0** pp (baseline 54) — violation 增加

**Discussion 原文 (p.8)**：
> "A mitigation experiment (1,256 episodes, five types; Appendix B) shows that type-specific disambiguation instructions reduce violations by 8.5 pp overall, with authorization scope benefiting most (Δ = −18.0 pp) and incompleteness least (Δ = −3.4 pp)."

**问题**：Discussion 推荐 "type-specific disambiguation instructions" 作为实践建议，仅报告 pooled 正面效果（overall −8.5 pp），完全未提及 DeepSeek 在两种类型上的 **backfire**（violation 反而增加）。这是 selective reporting——特别是对 "Practical implications" 段落而言，实践者如果按论文建议对 DeepSeek + scopal/incompleteness 部署消歧 prompt，实际上会恶化安全性。

R2 的建议合理：在 "Practical implications" 段落加一句 caveat，如 "However, disambiguation instructions can backfire for specific model-type combinations (e.g., DeepSeek scopal +2.0 pp, incompleteness +4.0 pp), underscoring the need for model-specific evaluation before deployment."

这是重要的 editorial fix。修改为 **PARTIALLY RESOLVED**。

---

### SF7 (引用问题): [PARTIALLY AGREE]

逐条回应：

- **lassiter_goodman_2017 年份**：[AGREE] 已知 minor issue（我在 Round 1 M1 中首次标注）。Synthese online-first 2015，正式卷号 2017。BibTeX 惯例是用正式出版年份，所以 2017 可接受，但在严格审查下两种做法都可辩护。建议作者自行决定——不构成问题。

- **ferrari_defects_2018 author**：[AGREE] 已知 minor（Round 1 M2）。bib key 名 "ferrari" 但第一作者是 Rosadini。Key 命名是任意的，但 BibTeX entry 本身的 author field 正确（Rosadini et al.），所以不影响论文中的引用显示。不需要修改。

- **Agent-SafetyBench (2024)**：[REBUT] 维持 Round 2 立场。这是 general agent safety benchmark，与本文 policy ambiguity 的 specific focus 有距离。Related Work (§2) 已覆盖 R-Judge、ToolEmu、InjecAgent、ShieldAgent、AgentAuditor 五篇 agent safety 工作。Agent-SafetyBench 的贡献在 safety scenario 分类而非 policy ambiguity，添加它是 nice-to-have 而非 gap。

- **OpenAgentSafety (ICLR 2026)**：[AGREE, conditional] 如果该文确实包含 policy compliance 评估维度，应被讨论。但我无法独立核实其内容——建议 Director 确认后决定。

**综合判断**：年份和 author 是已知 minor、不影响论文质量的格式问题。引用遗漏中只有 OpenAgentSafety 值得关注（conditional）。整体 SF7 标为 **RESOLVED**（核心问题 cohen/gwet/hu 已修复），残留的格式 minor 可在 camera-ready 处理。

---

### R1-NEW-1 (F-test df): [MAINTAIN, downgrade to minor editorial]

R2 未回应此条，但我维持发现。

**事实**：
- Round 1: F(12) = 1.97, p = 0.075（不显著）
- Round 4: F(20) = 1.97, p = 0.046（显著）

**分析**：df = 20 = (5−1)×(6−1) 是 5 models × 6 types 完整两因素交互的正确自由度。Round 1 的 df = 12 最可能是模型规格错误（可能排除了某些类型或使用了嵌套因素）。F-statistic 精确相同（1.97）在 df 变更后数学上不寻常，但鉴于 η² 也有微小变化（0.026 → 0.029），可能是四舍五入导致的视觉巧合。

**维持理由**：C4 已标记 exploratory，所以从 non-significant → significant 的转变不影响 claim 层级。但 **读者应能理解 F-test 的构建**——df = 20 的来源（完整 5×6 交互）应在正文或 Appendix 有一句说明。这是 minor editorial，不影响评分。

---

## 汇总：Round 4 残留问题

| Issue | R1 最终判断 | R2 判断 | 状态 |
|-------|-----------|---------|------|
| MF2 (human eval) | STILL_OPEN, non-blocking | STILL_OPEN, non-blocking | **一致** |
| MF3 Conclusion caveat (R2-NEW-1) | Should-fix editorial | Should-fix editorial | **一致** |
| SF2 (error coding validation) | RESOLVED within scope | RESOLVED within scope | **一致**（R1 改） |
| SF4 (ICC model disclosure) | STILL_OPEN minor | STILL_OPEN | **一致** |
| SF5 mitigation backfire (R2-NEW-2) | PARTIALLY RESOLVED | PARTIALLY RESOLVED | **一致**（R1 改） |
| SF7 (引用格式) | RESOLVED + minor residuals | PARTIALLY RESOLVED | 微小分歧，不影响评分 |
| R1-NEW-1 (F-test df) | MAINTAIN, minor editorial | 未回应 | R1 独立发现 |

**R1 与 R2 之间无重大分歧**。所有 blocking issues 已解决。残留问题均为 editorial 级别（Conclusion caveat 一句话、mitigation backfire 一句话、ICC model 名称、F-test df 说明），不影响论文核心贡献的有效性。

---

## 最终评分

**Overall: 3.5 / 5 (Borderline Conference, high end)**

与 R2 一致。

**升至 4.0 的条件**（camera-ready 前可完成）：
1. Conclusion 加 incompleteness caveat（一句话）
2. Discussion mitigation 段落加 DeepSeek backfire caveat（一句话）
3. §4.5 披露 ICC 复制实验选择的 2 个模型（一句话）
4. §5.4 说明 F-test 的 df = 20 来源（一句话）

以上四项均为 editorial-level fix，总计约 4 句话。如果作者在 camera-ready 阶段完成这些修改，我将提升评分至 4.0 (Conference)。

**Soundness: 3.5/5 | Excitement: 3.5/5 | Confidence: 4/5**

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

_source line 338 · 2026-05-21T08:09:15.053862+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
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
    "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-21T08:09:15.104444+00:00_



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

_source line 340 · 2026-05-21T08:09:20.076094+00:00_

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

_source line 341 · 2026-05-21T08:09:20.127261+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T08:04:24.217284+00:00\", \"completed_at\": \"2026-05-21T08:06:30.646460+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-5\", \"message\": \"连续 3 页纯文本（Taxonomy + Method + Controls/Statistical Analysis），无任何 display item 穿插。页面 3 的六类型 taxonomy 尤其适合用一张 tree diagram 或 summary table 可视化，帮助审稿人快速建立分类认知框架。页面 4-5 的 Method 部分可考虑加一张 matched-pair 示例表（ambiguous vs. unambiguous clause 对比）打破文字墙\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-9\", \"message\": \"Display items 总数偏少：3 figures + 1 table = 4 个。对于以实证为主的 8 页正文论文，通常预期 5-8 个。缺失的候选项：(1) taxonomy 可视化图/表，(2) matched-pair 示例表，(3) failure mode 分布图或 error analysis 表格。当前 4 个 display items 集中在 pages 2/6/7，前半部分和后半部分视觉密度不均\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（实验流程概览图）作为第一个视觉锚点位于第 2 页顶部，位置合理。但图内文字偏小（尤其三个子面板底部的标签文字），150 dpi 下阅读吃力，建议适当放大字号或简化标签\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（per-type effect sizes 柱状图）尺寸偏小，仅占右栏约 1/3 高度。坐标轴标签和数值在打印时可能不可读。建议扩大为单栏全高或改为跨栏 figure*\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 使用 booktabs 风格，排版专业。最优值已加粗标注，精度统一（1 位小数），Δpp 和 p 值列清晰。无溢出问题。整体质量好\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3（Model × Ambiguity Type Violation Rates）使用跨栏 figure*，适合展示 5 个模型 × 6 种类型的分组柱状图。颜色区分度尚可（6 种颜色），但部分相邻色（如中间几种）在灰度打印时可能难以区分，建议辅以 hatch pattern\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title / Author / Abstract 排版整洁，符合 ACL 匿名模板规范。首页视觉干净无拥挤感\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Discussion + Conclusion 占整页纯文本，无 display item。作为论述性章节可接受，但若能将 Error Analysis 的 failure mode 分类做成一张小表格会更清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 篇幅适中（约半页），覆盖 model coverage / domain scope / synthetic ambiguity / cross-judge asymmetry / failure mode analysis 5 个方面。References 
…[truncated 271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-21T08:09:20.679384+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-21T08:09:20.679801+00:00_



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

_source line 344 · 2026-05-21T08:09:24.345118+00:00_

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

_source line 345 · 2026-05-21T08:09:24.395797+00:00_

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

_source line 346 · 2026-05-21T08:09:28.012395+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-21T08:09:28.113362+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-21T08:09:30.929242+00:00_

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

_source line 349 · 2026-05-21T08:09:30.980354+00:00_

1	## Round 3 (Fresh) Review Issues — policy_ambiguity_safety
2	## Paper: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Date: 2026-05-21 (Round 3 fresh review)
5	## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)
6	
7	# ============================================================
8	# CRITICAL ISSUES (Must-Fix) — Consensus
9	# ============================================================
10	
11	- id: "MF1"
12	  summary: "Cross-judge confound 缺乏校准数据 — judge identity 与 model identity 完全混淆，所有涉及 GPT-5.4 的跨模型比较不可靠"
13	  category: method
14	  severity: critical
15	  status: in_progress
16	  first_raised_round: 1
17	  last_seen_round: 3
18	  mentions:
19	    - round: 1
20	      reviewers: [1, 2]
21	      note: "First identified in Round 1"
22	    - round: 2
23	      reviewers: [1, 2]
24	      note: "Both confirmed. Plan_009 human eval proposed but not completed."
25	    - round: 3
26	      reviewers: [1, 2]
27	      note: "[CONSENSUS] R1-N3 and R2-N2 independently identified. Auth scope Claude 12% vs GPT-5.4 64% crosses judge boundary."
28	  action_items:
29	    - round: 3
30	      action: "Dual-judge experiment: 100 episodes (60 GPT-5.4 + 40 others), GPT-5.4 + GPT-4.1 evaluate same traces, quantify judge bias. §4.4 cross-judge calibration discussion."
31	      assigned_to: "Main Agent"
32	      status: done
33	    - round: 3
34	      action: "Human evaluation ≥100 episodes — merged with MF2, blocked on user arranging annotators"
35	      assigned_to: "User"
36	      status: open
37	  resolution: "Dual-judge calibration complete: McNemar p=0.606 (no systematic bias), binary κ=0.653, weighted κ_w=0.775. §4 cross-judge calibration paragraph added. Auth_scope severity bias honestly reported. Human eval still open (MF2)."
38	  resolution_round: null
39	
40	- id: "MF2"
41	  summary: "Human evaluation baseline 完全缺失 — 核心 violation assessment (2,997 episodes) 纯 LLM-as-judge，无 human-LLM agreement 数据"
42	  category: met
…[truncated 9985 chars]

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

_source line 350 · 2026-05-21T08:10:40.417511+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Round 4 (Continue) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21 (Round 4 continue review)\n## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)\n\n# ============================================================\n# RESOLVED CRITICAL ISSUES (Round 4)\n# ============================================================\n\n- id: \"MF1\"\n  summary: \"Cross-judge confound — judge identity 与 model identity 混淆\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"First identified\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Plan_009 human eval proposed but not completed\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Auth scope Claude 12% vs GPT-5.4 64% crosses judge boundary\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[RESOLVED] Dual-judge calibration + within-judge auth scope validation. R1 & R2 consensus.\"\n  action_items:\n    - round: 3\n      action: \"Dual-judge experiment on 100 episodes\"\n      assigned_to: \"Main Agent\"\n      status: done\n  resolution: \"§4.4 cross-judge calibration: McNemar p=0.606, binary κ=0.653, weighted κ_w=0.775. §5.4 within-judge auth scope validation (Claude 12%, Qwen3 26%, DeepSeek 60% all judged by GPT-5.4) directly rules out judge confound for the key model-differentiating type. Auth scope κ=0.385 remains minor residual but does not affect binary-threshold conclusions.\"\n  resolution_round: 4\n\n- id: \"MF3\"\n  summary: \"Incompleteness confound — unambiguous variant 添加新信息\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"First identified\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Token count ≠ information content\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[RESOLVED] Upper-bound framing + logistic regression + coreferential lower-bound + 5-type sensitivity\"\n  resolution: \"§3 confound note at definition. §5.2 inline: upper-bound framing (49.2pp), logistic regression controlling info delta (p=0.022, <8% coefficient change), coreferential lower-bound (31.6%, info delta=0), 5-type sensitivity (omnibus p=0.079, pairwise auth scope p_adj=0.039, lexical p_adj=0.025). Abstract caveat added. Limitations suggests future orthogonalized design.\"\n  resolution_round: 4\n\n- id: \"MF4\"\n  summary: \"C4 (model×type interaction) overclaimed — 仅 2.9% variance\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Effect size too small for primary claim\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[RESOLVED] Comprehensive downgrade to exploratory throughout\"\n  resolution: \"Title changed. C4 marked [Exploratory] in §1 contributions, §5 opening, §5.4 title, Discussion, Conclusion. Abstract revised ('jointly determine' removed, '2.9% of variance' added). Claim hierarchy explicit: C1/C2 primary > C3 inconclusive > C4 exploratory.\"\n  resolution_round: 4\n\n# ============================================================\n# OPEN/DOWNGRADED CRITICAL ISSUES\n# ============================================================\n\n- id: \"MF2\"\n  summary: \"Human evaluation baseline 缺失 — violation assessment 纯 LLM-as-judge\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Below community standard\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Downgraded from critical to warning (non-blocking). Cross-judge calibration + matched-pair design provide alternative assurance. Limitations acknowledges. Community standard evolving.\"\n  action_items:\n    - round: 4\n      action: \"Camera-ready: human annotation on ~50 episodes for binary violation agreement\"\n      assigned_to: \"User\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED WARNING ISSUES (Round 4)\n# ============================================================\n\n- id: \"SF1\"\n  summary: \"TOST ±15pp margin 缺乏 SESOI 理论依据\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  resolution: \"§4.6 SESOI justification: practical significance (≥15pp warrants distinct handling) + perturbation bound linkage (13.3pp < 15pp).\"\n  resolution_round: 4\n\n- id: \"SF2\"\n  summary: \"Error analysis LLM 编码器未经人类验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[RESOLVED within scope] Failure mode taxonomy is supplementary analysis, primary claims independent. Limitations acknowledges κ=0.29 for minority categories.\"\n  resolution: \"Resolved within scope: §6 is supplementary, majority categories >90% of instances have adequate reliability. Limitations specifically notes arbitrary rule selection κ=0.29.\"\n  resolution_round: 4\n\n- id: \"SF3\"\n  summary: \"Perturbation control 检验力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  resolution: \"§4.5 worst-case analysis: CI upper bound 13.3pp = at most 39% of main effect, residual ≥20.7pp. Power analysis added.\"\n  resolution_round: 4\n\n- id: \"SF6\"\n  summary: \"Taxonomy framing 不精确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  resolution: \"§6 opening distinguishes failure mode taxonomy from input ambiguity taxonomy (§3).\"\n  resolution_round: 4\n\n- id: \"SF7\"\n  summary: \"Related work 遗漏 — Hu et al., Cohen, Gwet\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  resolution: \"All three references added and cited in correct context. Minor bib residuals (lassiter year, ferrari author key) are cosmetic.\"\n  resolution_round: 4\n\n- id: \"SF8\"\n  summary: \"正文超过 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  resolution: \"Main text (§1-§8) fits within 8 pages. Limitations starts page 9 (exempt). Confirmed by visual check.\"\n  resolution_round: 4\n\n# ============================================================\n# OPEN/PARTIALLY RESOLVED WARNING ISSUES\n# ============================================================\n\n- id: \"SF4\"\n  summary: \"ICC reproducibility — 未披露选择了哪 2 个模型\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[STILL_OPEN] §4.5 still says '2 models' without naming them. Minor transparency issue.\"\n  action_items:\n    - round: 4\n      action: \"Camera-ready: disclose which 2 models were used for ICC replication (~5 words)\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n- id: \"SF5\"\n  summary: \"Mitigation Discussion 遗漏反向效果\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Key findings buried in appendix\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[PARTIALLY RESOLVED] Key patterns elevated to §7, but DeepSeek backfire (scopal +2.0, incompleteness +4.0) omitted. Selective reporting of mitigation results.\"\n  action_items:\n    - round: 4\n      action: \"Camera-ready: add one sentence acknowledging DeepSeek mitigation backfire in §7 Practical Implications\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n# ============================================================\n# NEW ISSUES FROM ROUND 4\n# ============================================================\n\n- id: \"R4-NEW-1\"\n  summary: \"Conclusion 缺 incompleteness caveat — 仍说 'three-tier' 无限定，与 Abstract/§5.2 不一致\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Abstract and §5.2 flag three→two tier degradation, but Conclusion does not. ~10 words fix.\"\n  action_items:\n    - round: 4\n      action: \"Camera-ready: add '(reducing to two tiers when incompleteness is excluded)' to Conclusion\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n- id: \"R4-NEW-2\"\n  summary: \"F-test df 从 F(12)→F(20) 未解释 — p 值从 non-significant→significant\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"df=20=(5-1)×(6-1) is correct full factorial df. Same F=1.97 at different df is coincidence (rounding). C4 already exploratory so significance change is moot, but df source should be stated.\"\n  action_items:\n    - round: 4\n      action: \"Camera-ready: add one sentence explaining F-test specification (full 5×6 factorial, df=20)\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n- id: \"R4-NEW-3\"\n  summary: \"Discussion auth scope 对比数字不一致 — uses DeepSeek 60% vs Abstract's GPT-5.4 64%\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"Discussion compares Claude 12% vs DeepSeek 60% (within-judge context) while Abstract/Results use GPT-5.4 64% as upper bound. Not incorrect but inconsistent framing.\"\n  action_items:\n    - round: 4\n      action: \"Camera-ready: unify auth scope comparison or add brief justification for within-judge framing\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n# ============================================================\n# INFO ISSUES\n# ============================================================\n\n- id: \"M1\"\n  summary: \"引用 minor mismatches: Lassiter & Goodman year, ferrari_defects first author\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n\n- id: \"M2\"\n  summary: \"Table 3 排除 coreferential 未解释原因\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 3 caption now explains: 'Coreferential was excluded because it was not included in the mitigation experiment.'\"\n  resolution_round: 4\n\n- id: \"M3\"\n  summary: \"标题 'LLM Agent Families' 措辞\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"Title changed to 'Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents'\"\n  resolution_round: 3\n\n- id: \"M4\"\n  summary: \"'Nocuous' 首次使用加释义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Introduction now includes '(i.e., harmful)' parenthetical after first use of 'nocuous'.\"\n  resolution_round: 4\n\n# ============================================================\n# RESOLVED FROM PREVIOUS ROUNDS\n# ============================================================\n\n- id: \"R2-W5-r2\"\n  summary: \"[Round 2] τ²-bench 引用信息错误\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Author list corrected in references.bib\"\n  resolution_round: 2\n\n- id: \"R1-W3-r2\"\n  summary: \"[Round 2] 4-tier severity 二值化 sensitivity analysis\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix C. C1-C4 confirmed under both thresholds. Kendall τ=0.73.\"\n  resolution_round: 3\n\n- id: \"R1-W6-r2\"\n  summary: \"[Round 2] 多重比较校正 family 划分\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"§4.6 specifies three correction families.\"\n  resolution_round: 3\n\n- id: \"R1-W5-r2\"\n  summary: \"[Round 2] Clause pair 构造 IAA\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"§4.2 describes template-based pipeline + two annotators + three quality criteria.\"\n  resolution_round: 3"
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
    "issues_yaml": "## Round 4 (Continue) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21 (Round 4 continue review)\n## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)\n\n# ============================================================\n# RESOLVED CRITICAL ISSUES (Round 4)\n# ============================================================\n\n- id: \"MF1\"\n  summary: \"Cross-judge confound — judge identity 与 model identity 混淆\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"First identified\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Plan_009 human eval proposed but not completed\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Auth scope Claude 12% vs GPT-5.4 64% crosses judge boundary\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[RESOLVED] Dual-judge calibration + within-judge auth scope validation. R1 & R2 consensus.\"\n  action_items:\n    - round: 3\n      action: \"Dual-judge experiment on 100 episodes\"\n      assigned_to: \"Main Agent\"\n      status: done\n  resolution: \"§4.4 cross-judge calibration: McNemar p=0.606, binary κ=0.653, weighted κ_w=0.775. §5.4 within-judge auth scope validation (Claude 12%, Qwen3 26%, DeepSeek 60% all judged by GPT-5.4) directly rules out judge confound for the key model-differentiating type. Auth scope κ=0.385 remains minor residual but does not affect binary-threshold conclusions.\"\n  resolution_round: 4\n\n- id: \"MF3\"\n  summary: \"Incompleteness confound — unambiguous variant 添加新信息\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"First identified\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Token count ≠ information content\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[RESOLVED] Upper-bound framing + logistic regression + coreferential lower-bound + 5-type sensitivity\"\n  resolution: \"§3 confound note at definition. §5.2 inline: upper-bound framing (49.2pp), logistic regression controlling info delta (p=0.022, <8% coefficient change), coreferential lower-bound (31.6%, info delta=0), 5-type sensitivity (omnibus p=0.079, pairwise auth scope p_adj=0.039, lexical p_adj=0.025). Abstract caveat added. Limitations suggests future orthogonalized design.\"\n  resolution_round: 4\n\n- id: \"MF4\"\n  summary: \"C4 (model×type interaction) overclaimed — 仅 2.9% variance\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Effect size too small for primary claim\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[RESOLVED] Comprehensive downgrade to exploratory throughout\"\n  resolution: \"Title changed. C4 marked [Exploratory] in §1 contributions, §5 opening, §5.4 title, Discussion, Conclusion. Abstract revised ('jointly determine' removed, '2.9% of variance' added). Claim hierarchy explicit: C1/C2 primary > C3 inconclusive > C4 exploratory.\"\n  resolution_round: 4\n\n# ============================================================\n# OPEN/DOWNGRADED CRITICAL ISSUES\n# ============================================================\n\n- id: \"MF2\"\n  summary: \"Human evaluation baseline 缺失 — violation assessment 纯 LLM-as-judge\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Below community standard\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Downgraded from critical to warning (non-blocking). Cross-judge calibration + matched-pair design provide alternative assurance. Limitations acknowledges. Community standard evolving.\"\n  action_items:\n    - round: 4\n      action: \"Camera-ready: human annotation on ~50 episodes for binary violation agreement\"\n      assigned_to: \"User\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED WARNING ISSUES (Round 4)\n# ============================================================\n\n- id: \"SF1\"\n  summary: \"TOST ±15pp margin 缺乏 SESOI 理论依据\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  resolution: \"§4.6 SESOI justification: practical significance (≥15pp warrants distinct handling) + perturbation bound linkage (13.3pp < 15pp).\"\n  resolution_round: 4\n\n- id: \"SF2\"\n  summary: \"Error analysis LLM 编码器未经人类验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[RESOLVED within scope] Failure mode taxonomy is supplementary analysis, primary claims independent. Limitations acknowledges κ=0.29 for minority categories.\"\n  resolution: \"Resolved within scope: §6 is supplementary, majority categories >90% of instances have adequate reliability. Limitations specifically notes arbitrary rule selection κ=0.29.\"\n  resolution_round: 4\n\n- id: \"SF3\"\n  summary: \"Perturbation control 检验力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  resolution: \"§4.5 worst-case analysis: CI upper bound 13.3pp = at most 39% of main effect, residual ≥20.7pp. Power analysis added.\"\n  resolution_round: 4\n\n- id: \"SF6\"\n  summary: \"Taxonomy framing 不精确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  resolution: \"§6 opening distinguishes failure mode taxonomy from input ambiguity taxonomy (§3).\"\n  resolution_round: 4\n\n- id: \"SF7\"\n  summary: \"Related work 遗漏 — Hu et al., Cohen, Gwet\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  resolution: \"All three references added and cited in correct context. Minor bib residuals (lassiter year, ferrari author key) are cosmetic.\"\n  resolution_round: 4\n\n- id: \"SF8\"\n  summary: \"正文超过 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  resolution: \"Main text (§1-§8) fits within 8 pages. Limitations starts page 9 (exempt). Confirmed by visual check.\"\n  resolution_round: 4\n\n# ============================================================\n# OPEN/PARTIALLY RESOLVED WARNING ISSUES\n# ============================================================\n\n- id: \"SF4\"\n  summary: \"ICC reproducibility — 未披露选择了哪 2 个模型\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[STILL_OPEN] §4.5 still says '2 models' without naming them. Minor transparency issue.\"\n  action_items:\n    - round: 4\n      action: \"Camera-ready: disclose which 2 models were used for ICC replication (~5 words)\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n- id: \"SF5\"\n  summary: \"Mitigation Discussion 遗漏反向效果\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Key findings buried in appendix\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[PARTIALLY RESOLVED] Key patterns elevated to §7, but DeepSeek backfire (scopal +2.0, incompleteness +4.0) omitted. Selective reporting of mitigation results.\"\n  action_items:\n    - round: 4\n      action: \"Camera-ready: add one sentence acknowledging DeepSeek mitigation backfire in §7 Practical Implications\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n# ============================================================\n# NEW ISSUES FROM ROUND 4\n# ============================================================\n\n- id: \"R4-NEW-1\"\n  summary: \"Conclusion 缺 incompleteness caveat — 仍说 'three-tier' 无限定，与 Abstract/§5.2 不一致\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Abstract and §5.2 flag three→two tier degradation, but Conclusion does not. ~10 words fix.\"\n  action_items:\n    - round: 4\n      action: \"Camera-ready: add '(reducing to two tiers when incompleteness is excluded)' to Conclusion\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n- id: \"R4-NEW-2\"\n  summary: \"F-test df 从 F(12)→F(20) 未解释 — p 值从 non-significant→significant\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"df=20=(5-1)×(6-1) is correct full factorial df. Same F=1.97 at different df is coincidence (rounding). C4 already exploratory so significance change is moot, but df source should be stated.\"\n  action_items:\n    - round: 4\n      action: \"Camera-ready: add one sentence explaining F-test specification (full 5×6 factorial, df=20)\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n- id: \"R4-NEW-3\"\n  summary: \"Discussion auth scope 对比数字不一致 — uses DeepSeek 60% vs Abstract's GPT-5.4 64%\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"Discussion compares Claude 12% vs DeepSeek 60% (within-judge context) while Abstract/Results use GPT-5.4 64% as upper bound. Not incorrect but inconsistent framing.\"\n  action_items:\n    - round: 4\n      action: \"Camera-ready: unify auth scope comparison or add brief justification for within-judge framing\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n# ============================================================\n# INFO ISSUES\n# ============================================================\n\n- id: \"M1\"\n  summary: \"引用 minor mismatches: Lassiter & Goodman year, ferrari_defects first author\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n\n- id: \"M2\"\n  summary: \"Table 3 排除 coreferential 未解释原因\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 3 caption now explains: 'Coreferential was excluded because it was not included in the mitigation experiment.'\"\n  resolution_round: 4\n\n- id: \"M3\"\n  summary: \"标题 'LLM Agent Families' 措辞\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"Title changed to 'Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents'\"\n  resolution_round: 3\n\n- id: \"M4\"\n  summary: \"'Nocuous' 首次使用加释义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Introduction now includes '(i.e., harmful)' parenthetical after first use of 'nocuous'.\"\n  resolution_round: 4\n\n# ============================================================\n# RESOLVED FROM PREVIOUS ROUNDS\n# ============================================================\n\n- id: \"R2-W5-r2\"\n  summary: \"[Round 2] τ²-bench 引用信息错误\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Author list corrected in references.bib\"\n  resolution_round: 2\n\n- id: \"R1-W3-r2\"\n  summary: \"[Round 2] 4-tier severity 二值化 sensitivity analysis\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix C. C1-C4 confirmed under both thresholds. Kendall τ=0.73.\"\n  resolution_round: 3\n\n- id: \"R1-W6-r2\"\n  summary: \"[Round 2] 多重比较校正 family 划分\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"§4.6 specifies three correction families.\"\n  resolution_round: 3\n\n- id: \"R1-W5-r2\"\n  summary: \"[Round 2] Clause pair 构造 IAA\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"§4.2 describes template-based pipeline + two annotators + three quality criteria.\"\n  resolution_round: 3"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-21T08:10:40.519359+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 12164}, \"error\": \"\"}"}

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

_source line 352 · 2026-05-21T08:12:13.976841+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 4 Consolidated Review Report — policy_ambiguity_safety\n\n**Paper**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle (Long Paper)\n**Mode**: Continue Review (Round 3 → Round 4)\n**Reviewers**: R1 (方法严谨性), R2 (新颖性与完整性)\n**Date**: 2026-05-21\n\n---\n\n## Summary\n\n本轮审查聚焦于 Round 3 提出的 4 个 Must-Fix 和 8 个 Should-Fix 问题是否已充分解决。论文做了大量修改，方法论透明度显著提升。3 个 Critical Must-Fix（MF1/MF3/MF4）已实质性解决，MF2（human evaluation）降级为 non-blocking warning。6/8 Should-Fix 已解决，2 项残留（SF4 ICC model disclosure, SF5 mitigation backfire）。新发现 3 个 minor issues。\n\n---\n\n## Strengths\n\n1. **Cross-judge calibration 超出预期**（MF1）：§4.4 新增 100-episode dual-judge 实验（McNemar p=0.606, binary κ=0.653, weighted κ_w=0.775）已是充分回应。更出色的是 §5.4 自主新增的 within-judge auth scope 验证——Claude 12%, Qwen3 26%, DeepSeek 60% 三个模型共享同一 judge (GPT-5.4)，直接排除了 auth scope 跨模型差异的 judge confound。这是超出审稿意见建议范围的作者主动补充，显著加强了 C4 exploratory 结论中最重要的发现。\n\n2. **Incompleteness confound 处理教科书级**（MF3）：§3 定义处标注 → §5.2 upper-bound framing + logistic regression (p=0.022, <8% coefficient change) + coreferential zero-delta lower-bound (31.6%) + 5-type sensitivity analysis (omnibus p=0.079, pairwise contrasts preserved) → Limitations 指出 future orthogonalized design。论证链完整，诚实报告弱化结果（三层退化为两层），方法论上无可挑剔。\n\n3. **C4 exploratory 降级彻底一致**（MF4）：标题、Abstract、§1 contributions、§5 opening、§5.4 标题、Discussion、Conclusion 七处全部标注 [Exploratory] 或等价 hedge。Claim hierarchy (C1/C2 primary > C3 inconclusive > C4 exploratory) 与 evidence strength 完全对齐。\n\n4. **核心实验设计依然扎实**：matched-pair causal identification (300 clause pairs × 2 conditions × 5 models = 2,997 episodes)、perturbation control (Δ=3.33pp, CI containing zero)、ICC=0.919 reproducibility、TOST 7-margin sensitivity analysis。C1 的 +34.0pp effect (OR=15.1, p<10⁻¹⁰⁵) 在方法论上难以挑战。\n\n5. **SESOI justification 逻辑清晰**（SF1）：±15pp 同时锚定于实践意义（安全部署中 15pp 差异需区别对待）和 perturbation noise floor（CI 上界 13.3pp < 15pp）。\n\n---\n\n## Weaknesses\n\n### 残留 Warning（非 blocking，但影响竞争力）\n\n1. **Human evaluation baseline 完全缺失**（MF2, downgraded to warning）：论文所有评估（violation 判定 2,997 episodes + failure mode coding 614 traces）均为 LLM-only。Cross-judge calibration 证明两个 LLM 互相同意，但无法证明任一 LLM 与人类判断一致。Matched-pair 设计控制 systematic judge bias，但 type-specific 或 model-specific bias 仅被 calibration 数据 bounded 而非 eliminated。同 venue 标准在演变（R-Judge, ToolEmu 包含 human eval；AgentAuditor 不要求），但 human baseline 仍是与 top-tier 竞争的 differentiator。\n\n2. **Mitigation Discussion 选择性呈现**（SF5/R4-NEW-2）：§7 Practical Implications 推荐 \"type-specific disambiguation instructions\" 并报告 pooled -8.5pp 效果，但完全未提及 DeepSeek 在 scopal (+2.0pp) 和 incompleteness (+4.0pp) 上的反向效果。对实践者而言，不知道某策略在特定 model-type 组合上 backfire 有误导风险。一句话 caveat 即可修复。\n\n3. **Conclusion 叙事断裂**（R4-NEW-1）：§5.2 和 Abstract 都标注了 incompleteness 三层→两层退化，但 Conclusion 仍说 \"A three-tier type hierarchy\" 无任何限定。Conclusion 是多数读者唯一精读的段落，应与 Abstract/§5.2 保持一致。~10 词修改。\n\n4. **ICC model selection 未披露**（SF4）：§4.5 报告 \"5 per type × 2 models × 3 replicates\" 但未说明哪 2 个模型。ICC=0.919 的泛化性取决于此——如果选的是最稳定的模型，ICC 可能高估。~5 词修改。\n\n### Minor Issues（不影响接收决定）\n\n5. **F-test df 变更未说明**（R4-NEW-2）：§5.4 报告 F(20)=1.97, p=0.006。df=20=(5-1)×(6-1) 是完整 5×6 factorial 的正确 df，但 readers 需要知道 interaction model specification。一句话说明。\n\n6. **Discussion auth scope 数字不一致**（R4-NEW-3）：Discussion 用 \"Claude 12% vs DeepSeek 60%\"（within-judge context），Abstract/Results 用 \"12% to 64% (GPT-5.4)\"。不是错误但 framing 不统一。\n\n7. **引用 minor mismatches**（M1）：lassiter_goodman_2017 年份（online-first 2015 vs print 2017）、ferrari_defects_2018 bib key vs first author。不影响引用显示。\n\n---\n\n## Questions\n\n1. §5.4 F-test 的 model specification 是什么？是否使用了 Type III SS 或其他分解方式？df=20 与此前的 df=12 差异来源是什么？\n2. ICC 复制实验选择了哪 2 个模型？选择标准是什么（最高/最低 violation rate？不同 judge group？）\n3. Mitigation 实验中 DeepSeek 的反向效果（scopal +2.0, incompleteness +4.0）是否有假设解释？这是否与 DeepSeek 在 main study 中的 \"no significant type effect\" (V=0.14, p=0.28) 相关？\n\n---\n\n## Missing References\n\n核心遗漏已修复（Cohen 1960, Gwet 2014, Hu et al. 2025）。残留建议（non-blocking）：\n- OpenAgentSafety (ICLR 2026) — 如包含 policy compliance 评估维度则相关\n- Prompt sensitivity 文献（e.g., \"Assessing and Understanding Prompt Sensitivity of LLMs\", EMNLP 2024 Findings）— 论文研究的 clause-level wording 变化本质上涉及 prompt sensitivity\n\n---\n\n## External Review\n\n外部审稿（Stanford Agentic Reviewer via paperreview.ai）：**Skipped**（用户在 Round 3 跳过，Round 4 未重新请求）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**Status**: Done (2 warnings, 8 info)\n\n**Warnings**:\n- Pages 3-5 连续纯文本（Taxonomy + Method），无 display item。建议 §3 taxonomy 加 tree diagram 或 summary table，§4 加 matched-pair 示例\n- Display items 总数偏少（3 figures + 1 table = 4）；8 页实证论文通常预期 5-8 个。前半部分视觉密度低\n\n**Info highlights**:\n- Figure 1 图内文字偏小（150 dpi 下阅读吃力）\n- Figure 2 尺寸偏小（仅占右栏 1/3 高度），建议扩大\n- Figure 3 相邻色灰度打印可能难以区分，建议辅以 hatch pattern\n- Table 1 排版专业，无溢出\n- 无 margin 溢出、LaTeX 渲染错误、未解析引用\n- 主文 8 页合规，Limitations 约半页覆盖 5 个方面\n\n---\n\n## Overall Assessment\n\n### Score: 3.5 / 5 — Borderline Conference (high end)\n\n**R1**: 3.5 (Soundness 3.5, Excitement 3.5, Confidence 4)\n**R2**: 3.5 (Soundness 4.0, Excitement 3.5, Confidence 4)\n**Director consensus**: 3.5\n\n### 评分理由\n\n**论文的核心贡献有效且重要**：matched-pair causal design 在 agent safety 领域是方法论创新；C1 (+34.0pp, OR=15.1) 是强健的因果效应；C2 的三层层级（含 incompleteness upper-bound caveat）提供了可操作的 type-level 风险排序；Differential Nocuity 框架和 Ambiguity Blindness (<11% awareness) 是有理论贡献的概念。\n\n**Round 4 修改显著提升了方法论透明度**：cross-judge calibration + within-judge validation 是本轮最大亮点，incompleteness confound 的 upper-bound + lower-bound 处理教科书级别，C4 exploratory 降级彻底一致。Soundness 从 Round 3 的 3.0-3.5 提升至 3.5-4.0。\n\n**维持 3.5 而非升至 4.0 的原因**：(1) Human evaluation 完全缺失——虽降级为 non-blocking，仍是 completeness 缺口，在 main conference 竞争中是劣势；(2) Mitigation 结果选择性呈现——推荐实践策略但不报告 backfire 场景；(3) 几处 minor 叙事不一致（Conclusion caveat, auth scope 数字）。\n\n**升至 4.0 (Conference) 的条件**（均为 camera-ready 级别 editorial fix）：\n1. Conclusion 加 incompleteness caveat (~10 词)\n2. Discussion mitigation 加 DeepSeek backfire caveat (~1 句)\n3. 披露 ICC 的 2 个 models (~5 词)\n4. F-test df specification (~1 句)\n5. Auth scope 对比数字统一或加说明 (~半句)\n\n以上 5 项修改总计约 5 句话。如在 camera-ready 前完成，两位 Reviewer 均表示将修订评分至 4.0。\n\n### EMNLP 2026 ARR 定位\n\n- **Main Conference (4.0)**: 需完成上述 5 项 + 理想情况下补充 ~50 episodes human annotation\n- **Findings (3.0-3.5)**: 当前状态已满足 Findings 标准\n- **当前位置**: 3.5 = Borderline Conference，处于 Conference/Findings 边界的 Conference 侧\n\n---\n\n## Detailed Comments\n\n### Camera-Ready Action Items（按优先级排列）\n\n| # | Issue | Fix | Effort | Impact |\n|---|-------|-----|--------|--------|\n| 1 | Conclusion incompleteness caveat (R4-NEW-1) | Add \"(reducing to two tiers when incompleteness is excluded)\" | ~10 words | Narrative consistency |\n| 2 | Mitigation backfire (SF5) | Add DeepSeek scopal/incompleteness reverse effect sentence | ~1 sentence | Practical reliability |\n| 3 | ICC model disclosure (SF4) | Name the 2 models used for replication | ~5 words | Transparency |\n| 4 | F-test df explanation (R4-NEW-2) | State \"full 5×6 factorial interaction, df=(5-1)×(6-1)=20\" | ~1 sentence | Methodological clarity |\n| 5 | Auth scope number consistency (R4-NEW-3) | Unify Discussion with Abstract/Results framing | ~half sentence | Consistency |\n| 6 | Human annotation (MF2) | ~50 episodes human-LLM agreement on binary violation | Moderate effort | Competitiveness for main |\n\nItems 1-5 are editorial (~5 sentences total). Item 6 is the only substantive effort and determines Conference vs Findings positioning.\n\n### Cross-Round Progress Summary\n\n| Round | Score | Key Issues | Status |\n|-------|-------|-----------|--------|\n| Round 1 | — | Initial identification of MF1/MF3/SF1-SF4 | — |\n| Round 2 | — | SF6-SF8 added, some partial fixes | — |\n| Round 3 | 3.0 | 4 MF + 8 SF. Major gaps: cross-judge, human eval, incompleteness, C4 overclaiming | Fresh review |\n| **Round 4** | **3.5** | MF1/MF3/MF4 resolved. MF2 downgraded. 6/8 SF resolved. 3 new minor. | **+0.5** |\n\n论文从 Round 3 的 3.0 (Findings) 提升至 3.5 (Borderline Conference)，修改质量显著且超出预期（尤其 within-judge validation）。距离 4.0 仅差 editorial-level fixes。",
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference (high end)",
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
    "report": "# Round 4 Consolidated Review Report — policy_ambiguity_safety\n\n**Paper**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle (Long Paper)\n**Mode**: Continue Review (Round 3 → Round 4)\n**Reviewers**: R1 (方法严谨性), R2 (新颖性与完整性)\n**Date**: 2026-05-21\n\n---\n\n## Summary\n\n本轮审查聚焦于 Round 3 提出的 4 个 Must-Fix 和 8 个 Should-Fix 问题是否已充分解决。论文做了大量修改，方法论透明度显著提升。3 个 Critical Must-Fix（MF1/MF3/MF4）已实质性解决，MF2（human evaluation）降级为 non-blocking warning。6/8 Should-Fix 已解决，2 项残留（SF4 ICC model disclosure, SF5 mitigation backfire）。新发现 3 个 minor issues。\n\n---\n\n## Strengths\n\n1. **Cross-judge calibration 超出预期**（MF1）：§4.4 新增 100-episode dual-judge 实验（McNemar p=0.606, binary κ=0.653, weighted κ_w=0.775）已是充分回应。更出色的是 §5.4 自主新增的 within-judge auth scope 验证——Claude 12%, Qwen3 26%, DeepSeek 60% 三个模型共享同一 judge (GPT-5.4)，直接排除了 auth scope 跨模型差异的 judge confound。这是超出审稿意见建议范围的作者主动补充，显著加强了 C4 exploratory 结论中最重要的发现。\n\n2. **Incompleteness confound 处理教科书级**（MF3）：§3 定义处标注 → §5.2 upper-bound framing + logistic regression (p=0.022, <8% coefficient change) + coreferential zero-delta lower-bound (31.6%) + 5-type sensitivity analysis (omnibus p=0.079, pairwise contrasts preserved) → Limitations 指出 future orthogonalized design。论证链完整，诚实报告弱化结果（三层退化为两层），方法论上无可挑剔。\n\n3. **C4 exploratory 降级彻底一致**（MF4）：标题、Abstract、§1 contributions、§5 opening、§5.4 标题、Discussion、Conclusion 七处全部标注 [Exploratory] 或等价 hedge。Claim hierarchy (C1/C2 primary > C3 inconclusive > C4 exploratory) 与 evidence strength 完全对齐。\n\n4. **核心实验设计依然扎实**：matched-pair causal identification (300 clause pairs × 2 conditions × 5 models = 2,997 episodes)、perturbation control (Δ=3.33pp, CI containing zero)、ICC=0.919 reproducibility、TOST 7-margin sensitivity analysis。C1 的 +34.0pp effect (OR=15.1, p<10⁻¹⁰⁵) 在方法论上难以挑战。\n\n5. **SESOI justification 逻辑清晰**（SF1）：±15pp 同时锚定于实践意义（安全部署中 15pp 差异需区别对待）和 perturbation noise floor（CI 上界 13.3pp < 15pp）。\n\n---\n\n## Weaknesses\n\n### 残留 Warning（非 blocking，但影响竞争力）\n\n1. **Human evaluation baseline 完全缺失**（MF2, downgraded to warning）：论文所有评估（violation 判定 2,997 episodes + failure mode coding 614 traces）均为 LLM-only。Cross-judge calibration 证明两个 LLM 互相同意，但无法证明任一 LLM 与人类判断一致。Matched-pair 设计控制 systematic judge bias，但 type-specific 或 model-specific bias 仅被 calibration 数据 bounded 而非 eliminated。同 venue 标准在演变（R-Judge, ToolEmu 包含 human eval；AgentAuditor 不要求），但 human baseline 仍是与 top-tier 竞争的 differentiator。\n\n2. **Mitigation Discussion 选择性呈现**（SF5/R4-NEW-2）：§7 Practical Implications 推荐 \"type-specific disambiguation instructions\" 并报告 pooled -8.5pp 效果，但完全未提及 DeepSeek 在 scopal (+2.0pp) 和 incompleteness (+4.0pp) 上的反向效果。对实践者而言，不知道某策略在特定 model-type 组合上 backfire 有误导风险。一句话 caveat 即可修复。\n\n3. **Conclusion 叙事断裂**（R4-NEW-1）：§5.2 和 Abstract 都标注了 incompleteness 三层→两层退化，但 Conclusion 仍说 \"A three-tier type hierarchy\" 无任何限定。Conclusion 是多数读者唯一精读的段落，应与 Abstract/§5.2 保持一致。~10 词修改。\n\n4. **ICC model selection 未披露**（SF4）：§4.5 报告 \"5 per type × 2 models × 3 replicates\" 但未说明哪 2 个模型。ICC=0.919 的泛化性取决于此——如果选的是最稳定的模型，ICC 可能高估。~5 词修改。\n\n### Minor Issues（不影响接收决定）\n\n5. **F-test df 变更未说明**（R4-NEW-2）：§5.4 报告 F(20)=1.97, p=0.006。df=20=(5-1)×(6-1) 是完整 5×6 factorial 的正确 df，但 readers 需要知道 interaction model specification。一句话说明。\n\n6. **Discussion auth scope 数字不一致**（R4-NEW-3）：Discussion 用 \"Claude 12% vs DeepSeek 60%\"（within-judge context），Abstract/Results 用 \"12% to 64% (GPT-5.4)\"。不是错误但 framing 不统一。\n\n7. **引用 minor mismatches**（M1）：lassiter_goodman_2017 年份（online-first 2015 vs print 2017）、ferrari_defects_2018 bib key vs first author。不影响引用显示。\n\n---\n\n## Questions\n\n1. §5.4 F-test 的 model specification 是什么？是否使用了 Type III SS 或其他分解方式？df=20 与此前的 df=12 差异来源是什么？\n2. ICC 复制实验选择了哪 2 个模型？选择标准是什么（最高/最低 violation rate？不同 judge group？）\n3. Mitigation 实验中 DeepSeek 的反向效果（scopal +2.0, incompleteness +4.0）是否有假设解释？这是否与 DeepSeek 在 main study 中的 \"no significant type effect\" (V=0.14, p=0.28) 相关？\n\n---\n\n## Missing References\n\n核心遗漏已修复（Cohen 1960, Gwet 2014, Hu et al. 2025）。残留建议（non-blocking）：\n- OpenAgentSafety (ICLR 2026) — 如包含 policy compliance 评估维度则相关\n- Prompt sensitivity 文献（e.g., \"Assessing and Understanding Prompt Sensitivity of LLMs\", EMNLP 2024 Findings）— 论文研究的 clause-level wording 变化本质上涉及 prompt sensitivity\n\n---\n\n## External Review\n\n外部审稿（Stanford Agentic Reviewer via paperreview.ai）：**Skipped**（用户在 Round 3 跳过，Round 4 未重新请求）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**Status**: Done (2 warnings, 8 info)\n\n**Warnings**:\n- Pages 3-5 连续纯文本（Taxonomy + Method），无 display item。建议 §3 taxonomy 加 tree diagram 或 summary table，§4 加 matched-pair 示例\n- Display items 总数偏少（3 figures + 1 table = 4）；8 页实证论文通常预期 5-8 个。前半部分视觉密度低\n\n**Info highlights**:\n- Figure 1 图内文字偏小（150 dpi 下阅读吃力）\n- Figure 2 尺寸偏小（仅占右栏 1/3 高度），建议扩大\n- Figure 3 相邻色灰度打印可能难以区分，建议辅以 hatch pattern\n- Table 1 排版专业，无溢出\n- 无 margin 溢出、LaTeX 渲染错误、未解析引用\n- 主文 8 页合规，Limitations 约半页覆盖 5 个方面\n\n---\n\n## Overall Assessment\n\n### Score: 3.5 / 5 — Borderline Conference (high end)\n\n**R1**: 3.5 (Soundness 3.5, Excitement 3.5, Confidence 4)\n**R2**: 3.5 (Soundness 4.0, Excitement 3.5, Confidence 4)\n**Director consensus**: 3.5\n\n### 评分理由\n\n**论文的核心贡献有效且重要**：matched-pair causal design 在 agent safety 领域是方法论创新；C1 (+34.0pp, OR=15.1) 是强健的因果效应；C2 的三层层级（含 incompleteness upper-bound caveat）提供了可操作的 type-level 风险排序；Differential Nocuity 框架和 Ambiguity Blindness (<11% awareness) 是有理论贡献的概念。\n\n**Round 4 修改显著提升了方法论透明度**：cross-judge calibration + within-judge validation 是本轮最大亮点，incompleteness confound 的 upper-bound + lower-bound 处理教科书级别，C4 exploratory 降级彻底一致。Soundness 从 Round 3 的 3.0-3.5 提升至 3.5-4.0。\n\n**维持 3.5 而非升至 4.0 的原因**：(1) Human evaluation 完全缺失——虽降级为 non-blocking，仍是 completeness 缺口，在 main conference 竞争中是劣势；(2) Mitigation 结果选择性呈现——推荐实践策略但不报告 backfire 场景；(3) 几处 minor 叙事不一致（Conclusion caveat, auth scope 数字）。\n\n**升至 4.0 (Conference) 的条件**（均为 camera-ready 级别 editorial fix）：\n1. Conclusion 加 incompleteness caveat (~10 词)\n2. Discussion mitigation 加 DeepSeek backfire caveat (~1 句)\n3. 披露 ICC 的 2 个 models (~5 词)\n4. F-test df specification (~1 句)\n5. Auth scope 对比数字统一或加说明 (~半句)\n\n以上 5 项修改总计约 5 句话。如在 camera-ready 前完成，两位 Reviewer 均表示将修订评分至 4.0。\n\n### EMNLP 2026 ARR 定位\n\n- **Main Conference (4.0)**: 需完成上述 5 项 + 理想情况下补充 ~50 episodes human annotation\n- **Findings (3.0-3.5)**: 当前状态已满足 Findings 标准\n- **当前位置**: 3.5 = Borderline Conference，处于 Conference/Findings 边界的 Conference 侧\n\n---\n\n## Detailed Comments\n\n### Camera-Ready Action Items（按优先级排列）\n\n| # | Issue | Fix | Effort | Impact |\n|---|-------|-----|--------|--------|\n| 1 | Conclusion incompleteness caveat (R4-NEW-1) | Add \"(reducing to two tiers when incompleteness is excluded)\" | ~10 words | Narrative consistency |\n| 2 | Mitigation backfire (SF5) | Add DeepSeek scopal/incompleteness reverse effect sentence | ~1 sentence | Practical reliability |\n| 3 | ICC model disclosure (SF4) | Name the 2 models used for replication | ~5 words | Transparency |\n| 4 | F-test df explanation (R4-NEW-2) | State \"full 5×6 factorial interaction, df=(5-1)×(6-1)=20\" | ~1 sentence | Methodological clarity |\n| 5 | Auth scope number consistency (R4-NEW-3) | Unify Discussion with Abstract/Results framing | ~half sentence | Consistency |\n| 6 | Human annotation (MF2) | ~50 episodes human-LLM agreement on binary violation | Moderate effort | Competitiveness for main |\n\nItems 1-5 are editorial (~5 sentences total). Item 6 is the only substantive effort and determines Conference vs Findings positioning.\n\n### Cross-Round Progress Summary\n\n| Round | Score | Key Issues | Status |\n|-------|-------|-----------|--------|\n| Round 1 | — | Initial identification of MF1/MF3/SF1-SF4 | — |\n| Round 2 | — | SF6-SF8 added, some partial fixes | — |\n| Round 3 | 3.0 | 4 MF + 8 SF. Major gaps: cross-judge, human eval, incompleteness, C4 overclaiming | Fresh review |\n| **Round 4** | **3.5** | MF1/MF3/MF4 resolved. MF2 downgraded. 6/8 SF resolved. 3 new minor. | **+0.5** |\n\n论文从 Round 3 的 3.0 (Findings) 提升至 3.5 (Borderline Conference)，修改质量显著且超出预期（尤其 within-judge validation）。距离 4.0 仅差 editorial-level fixes。",
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference (high end)",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-21T08:12:18.548197+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4571
}
```

</details>

---


### Assistant

_source line 354 · 2026-05-21T08:12:27.435416+00:00_

Round 4 审稿完成，报告已投递。

**结果摘要**：
- **评分**：3.0 → **3.5** (Borderline Conference, high end)，提升 0.5 分
- **Round 3 的 4 个 Must-Fix**：MF1/MF3/MF4 已 RESOLVED，MF2 降级为 non-blocking warning
- **Round 3 的 8 个 Should-Fix**：6 项 RESOLVED，SF4 (ICC model disclosure) 和 SF5 (mitigation backfire) 残留
- **Round 4 新发现**：3 个 minor issues（Conclusion caveat、F-test df、auth scope 数字一致性）
- **升至 4.0 的条件**：5 项 editorial fix（约 5 句话）+ 理想情况下补充 ~50 episodes human annotation
- **外部审稿**：Skipped
- **视觉审查**：Done，2 warning（display items 偏少、pages 3-5 文字墙）+ 8 info

Issue tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 33

## Round 33

2 recorded events


### User

_source line 355 · 2026-05-21T08:12:28.639748+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

与 R2 达成一致：Overall 3.5 (Borderline Conference, high end)。所有 critical must-fix 已解决，残留 4 项 editorial fix（各一句话）完成后可升至 4.0 (Conference)。两位 reviewer 之间无重大分歧。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 4 最终核查报告

（本轮整合了前两次 R4 提交的结论 + 对 R1 Round 4 findings 的独立回应）

---

## Issue Checklist

### Must-Fix Issues

**MF1 — Cross-judge confound: [RESOLVED]**

与前两次判断一致。§4.4 calibration（100 episodes, McNemar p=0.606, binary κ=0.653, κ_w=0.775）充分缓解。核心证据是 experiments.tex line 65 的 within-judge auth scope 验证（Claude 12%, Qwen3 26%, DeepSeek 60% 均由 GPT-5.4 评判），排除了论文最重要发现的 judge confound。

R1 报告 auth scope κ=0.583。我在 method.tex line 22 中读到的是 κ=0.385（"lowest for authorization scope (κ = 0.385, fair)"）。如果 R1 读到的是 0.583，可能存在版本差异或误读。基于我核查的 LaTeX 源码，auth scope κ=0.385 是正确数值。这比 R1 认为的更低，但论文正确论证了 binary threshold 下这不影响 core conclusions，且 within-judge analysis 提供了独立验证。

---

**MF2 — Human evaluation baseline: [STILL_OPEN, 同意 R1 降级为 warning]**

未新增 human data。同意 R1 的降级理由：matched-pair 设计提供了 within-subject 控制（每条 clause 既作为 ambiguous 又作为 unambiguous 的 paired control），cross-judge calibration 提供了评估管道可靠性证据，同期 EMNLP agent evaluation 论文中 human baseline 并非 universal requirement（R-Judge EMNLP 2024 Findings, ToolEmu ICLR 2024 均以 LLM-as-judge 为主）。

Limitations line 12 坦诚承认（含 minority category κ=0.29 具体报告）。Non-blocking。

---

**MF3 — Incompleteness confound: [RESOLVED]**

与前两次判断一致。Upper-bound framing 恰当（实验操纵确实混合了歧义消除与信息添加）。Logistic regression 以 token delta 作为 info content 代理——粗糙但在给定约束下是最可行的控制（无法直接量化 "semantic information content"），且 coefficient change <8% 表明主效应对控制稳健。Coreferential lower-bound（info delta=0, 31.6%）是方法论亮点。

去除 incompleteness 后 5-type omnibus p=0.079 的诚实报告是正确做法。Limitations line 14 进一步承认 "a future design that orthogonalizes information quantity from ambiguity resolution would strengthen causal claims"。

---

**MF4 — C4 overclaiming: [RESOLVED]**

与前两次判断一致。全文 [Exploratory] 标签一致贯穿，无残留 overclaiming。

---

### Should-Fix Issues

**SF1 — TOST margin: [RESOLVED]** SESOI justification 清晰。
**SF2 — Error analysis human validation: [STILL_OPEN, minor]** 同意 R1——Limitations 承认充分但 human validation 仍缺。
**SF3 — Perturbation control: [RESOLVED]** Worst-case 分析 balanced。
**SF4 — ICC model selection: [STILL_OPEN, minor]** 仍未披露哪 2 个 models。
**SF5 — Mitigation in Discussion: [PARTIALLY RESOLVED]** 数字与 Table 3 一致，但 DeepSeek 反向效果（scopal +2.0, incompleteness +4.0）仍未提及。R1 判为 RESOLVED，**我不同意**——推荐 type-specific mitigation 时遗漏 backfire case 构成选择性呈现（见下方 NEW-2）。
**SF6 — Taxonomy framing: [RESOLVED]** analysis.tex line 4 有效区分。
**SF7 — Missing references: [RESOLVED]** 36 篇引用合理，核心 concurrent work 已覆盖。
**SF8 — Page limit: [RESOLVED]** 主文 §1–§8 在 pages 1–8 内。

---

## Response to R1 Findings

**R1 NEW-1（F-test df 从 F(12)→F(20)，F=1.97 不变，p 从 0.075→0.046）: [REBUT with qualification]**

**当前论文的数值是内部一致的。** experiments.tex line 61 报告 $F(20) = 1.97$, $p = 0.006$（不是 R1 所说的 0.046）。

**df=20 是正确的。** 5 models × 6 types 的交互项 df = (5−1)(6−1) = 20。这是标准的 two-way interaction df。

**F(20) = 1.97 与 p = 0.006 的一致性核验**：在 ambiguous condition 下约 1,500 episodes，denominator df ≈ 1,450。查 F 分布表：F(20, 1450) 的 α=0.01 临界值约 1.88，α=0.005 临界值约 2.03。F=1.97 落在两者之间，p ≈ 0.006 是合理的。

**R1 声称的 p 值（0.075 和 0.046）均不能从当前数据再现。** 
- F(12, ~1450) = 1.97 → p ≈ 0.023（不是 0.075）
- F(20, ~1450) = 1.97 → p ≈ 0.006（不是 0.046）
- R1 在 Round 1 中声称 p = 0.075，在 Round 4 中声称 p 改为 0.046——两个数值均与我的独立计算不符。

**如果确实存在 df 变更**（从某个早期版本的 F(12) 改为当前 F(20)），这可能反映了模型规约的修正（例如从 4 models 改为 5 models 的分析，或从 4 types 改为 6 types 的分析）。但 **当前版本的 F(20) = 1.97, p = 0.006 是自洽的**。如果作者确实修改了模型规约，在 revision notes 中说明一句会更透明——但这不是论文本身的错误。

**实质性判断不受影响**：无论 p = 0.006 还是 R1 所称的 0.046，C4 已被标记为 [Exploratory]，2.9% variance 已被报告。claim strength 与 evidence 已对齐。这个统计细节不影响接收决定。

---

## New Issues

**[NEW-1] Conclusion 缺 incompleteness caveat — Minor**
（与前两次提交一致）conclusion.tex line 3 说 "A three-tier type hierarchy" 但 Abstract 和 §5.2 都 flag 了三层→两层退化。~10 词即可修复。

**[NEW-2] Discussion mitigation 遗漏 DeepSeek 反向效果 — Should-Fix**
（与前两次提交一致，此处标记与 R1 的分歧）discussion.tex line 11 推荐 type-specific disambiguation instructions 但未报告 DeepSeek scopal +2.0 和 incompleteness +4.0。Table 3 清楚显示这些数据。R1 将 SF5 标为 RESOLVED——**我明确不同意**。向 practitioners 推荐 mitigation strategy 时遗漏已知的 backfire case 是信息遗漏，一句话可修复。

---

## Score Recommendation

**Overall: 3.5 → 3.5 (Borderline Conference, high end)**

**维持 3.5 的核心理由**：
- MF2 (human eval) 仍为 open warning
- SF5/NEW-2 (mitigation 反向效果遗漏) 是 practical implications 的可靠性缺口
- 新颖性为 moderate（Differential Nocuity 是对 Berry & Kamsties 的合理扩展但非范式突破）

**3.5 处于 high end 的理由**：
- Soundness 从 3.5 提升至 4.0（cross-judge calibration + within-judge auth scope validation + incompleteness upper-bound 处理）
- 方法论贡献（matched-pair causal identification in agent safety）在领域内独特
- MF1/MF3/MF4 的修改质量高于平均水平，特别是 within-judge auth scope 验证（experiments.tex line 65）是作者主动完成的超预期补充

**升至 4.0 (Conference) 的 minor edits**：
1. Conclusion 加 incompleteness caveat (~10 词)
2. Discussion 报告 DeepSeek mitigation 反向效果 (~1 句)
3. 披露 ICC 的 2 个 models (~5 词)

这三项在 camera-ready 中完成即可。

| 维度 | Round 3 | Round 4 |
|------|---------|---------|
| Soundness | 3.5 | 4.0 |
| Excitement | 3.5 | 3.5 |
| Reproducibility | 3 | 3 |
| **Overall** | **3.5** | **3.5** (high end) |
| Confidence | 4 | 4 |

---

[Reviewer 2 审稿结果]:
Round 4 最终报告已提交。核心判断：

- **MF1/MF3/MF4**: RESOLVED — cross-judge calibration + within-judge validation + incompleteness upper-bound + C4 exploratory downgrade 均达标
- **MF2**: 降级为 warning，同意 R1
- **与 R1 的分歧**：(1) SF5 mitigation 反向效果遗漏——我认为 STILL_OPEN，R1 认为 RESOLVED；(2) R1 的 F-test df 问题——当前 F(20)=1.97, p=0.006 内部一致，R1 声称的 p 值无法从数据再现
- **Overall**: 维持 3.5 (Borderline Conference, high end)，3 项 minor edits 完成后可升至 4.0

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 Round 4 判断的逐条回应

---

### 一致的判断（无需详述）

MF1 RESOLVED、MF3 RESOLVED、MF4 RESOLVED、SF1 RESOLVED、SF3 RESOLVED、SF4 STILL_OPEN、SF6 RESOLVED、SF8 RESOLVED——两位 reviewer 完全一致。

---

### 分歧点逐条回应

**MF2（Human evaluation baseline）: [AGREE with R1, 修改我的判断为 RESOLVED with caveat]**

R1 的论证说服了我。核心理由：matched-pair 设计提供 within-subject 控制（同一 clause 在 ambiguous/unambiguous 条件下配对），这使得 judge 的绝对准确率不如 judge 的一致性重要——即便 judge 系统性高估或低估 violation，paired difference（Δ=34.0 pp）不受影响。Cross-judge calibration（McNemar p=0.606）确认无 systematic directional bias。在这个实验设计下，human baseline 的价值更多是增加信心而非修正结论。

R1 提到 "社区标准在演变" 也是合理的观察：2024-2026 的 agent evaluation 文献（R-Judge, ToolEmu, AgentAuditor）已建立 LLM-as-judge 作为 accepted practice 的先例。

**修改我的标签**：STILL_OPEN non-blocking → **RESOLVED with caveat**（caveat: camera-ready 中补充 ~50 episodes human annotation 仍然是一个 strengthening opportunity，但不是 acceptance condition）。

---

**SF2（Error analysis human validation）: [REBUT R1, 维持 RESOLVED within scope]**

R1 标为 STILL_OPEN minor，认为 minority categories κ=0.29 需额外标注。但论文 Limitations（line 12）已经逐字写出 "per-category reliability for minority categories remains limited (e.g., arbitrary rule selection κ = 0.29)"。这正是 R1 要求的标注，它已经在论文中了。

分歧的实质是 scope 定义不同：R1 认为 "STILL_OPEN" 因为 human validation 未做；我认为 "RESOLVED within scope" 因为 Limitations 的承认已满足 Should-Fix 级别的要求——Error analysis 的 human validation 从未被提升为 Must-Fix，在 Should-Fix 范围内，坦诚承认即足够。

不构成实质分歧——标签差异（STILL_OPEN minor vs RESOLVED within scope）对评分无影响。

---

**SF5（Mitigation backfire）: [维持 PARTIALLY RESOLVED, 不同意 R1 的 RESOLVED]**

这是我与 R1 之间最实质的分歧。

**事实基础**：Table 3（Appendix B）显示 DeepSeek 在 scopal (+2.0 pp) 和 incompleteness (+4.0 pp) 上的 disambiguation instructions 效果为正——即 mitigation 策略反而增加了 violations。Discussion（line 11）推荐 "type-specific disambiguation instructions" 并报告 pooled 正面结果（−8.5 pp overall, −18.0 pp auth scope），但完全未提及这些反向效果。

**为什么这不是 RESOLVED**：
1. 论文的 Practical Implications 段落是面向 practitioners 的建议——"Policy auditing should be type-aware, prioritizing incompleteness and authorization scope"。如果一个读者基于此建议在 DeepSeek agent 上部署 type-specific disambiguation instructions，他们不会从正文中得知这可能在 scopal 和 incompleteness 类型上 backfire。
2. 这不是隐藏在 noise 中的微小变化——+4.0 pp on incompleteness（从 54→58）是 Table 3 中最大的反向效果之一，且 incompleteness 正是论文标为 "universally dangerous" 的类型。
3. 一句话即可修复，成本极低："However, disambiguation instructions increase violations for individual model–type combinations (e.g., DeepSeek on incompleteness), indicating that mitigation requires model-specific calibration."

R1 可能认为 Appendix 中的 Table 3 已提供完整数据，读者可以自行发现。但 Discussion 的功能是 interpret and contextualize results——选择性呈现正面结果而不提及已知 backfire 是 framing 问题，不是 data availability 问题。

**严重程度**：Should-Fix。不影响接收决定，但影响 practical implications 段落的可靠性。

---

**SF7（Missing references）: [AGREE with R1, 升级我的判断为 RESOLVED]**

R1 的理由合理：36 篇引用在 EMNLP long paper 中处于合理范围，核心 concurrent work（DRIP-R, PolicyBank, AgentPex, MANTRA, Hu et al. 2025）已覆盖。我之前标 PARTIALLY RESOLVED 基于两个残留点：(a) minor bib 不一致（lassiter_goodman_2017 年份, ferrari_defects_2018 作者），(b) Agent-SafetyBench/OpenAgentSafety 未引用。

重新评估后：(a) bib 不一致是 copyediting 问题，不影响审稿决定；(b) Agent-SafetyBench 和 OpenAgentSafety 是 general agent safety benchmarks，论文已引用了该领域更直接相关的工作（R-Judge, ToolEmu, AgentAuditor），补充这两篇是 nice-to-have 但非 necessary。

**修改我的标签**：PARTIALLY RESOLVED → **RESOLVED**。

---

**R1-NEW-1（F-test df 变更）: [REBUT R1 的 p 值推算, AGREE 透明性建议]**

**df = 20 是正确的完整交互 df**。5 models × 6 types 的交互项 df = (5−1)(6−1) = 4×5 = 20。当前论文报告 F(20) = 1.97 是标准规约。

**R1 的 p 值推算（0.046）与论文报告值（0.006）不一致**。我在前次提交中做了独立验证：ambiguous condition 约 1,500 episodes，denominator df ≈ 1,450。F(20, 1450) = 1.97 对应 p ≈ 0.006，与论文一致。R1 推算的 0.046 可能基于不同的 denominator df 假设（例如用 episode-level 而非 clause-level variance），但论文中没有足够信息判断哪个是正确的 error term。

**如果确实存在从 F(12) 到 F(20) 的变更**（例如早期版本使用了 4 models 或 collapsed types），作者应在 revision notes 中说明。但这是审稿过程的透明性问题，不是论文本身的错误——当前版本的 F(20) = 1.97, p = 0.006 在统计上是自洽的。

**实质性判断不受影响**：C4 已标记 [Exploratory]，2.9% variance 已报告，claim strength 与 evidence 完全对齐。即便 p = 0.046（R1 推算值），结论不变。

---

## 最终评分

**Overall: 3.5 → 3.5 (Borderline Conference, high end)**

与 R1 评分一致（3.5，偏向 accept）。

**两位 reviewer 的共识**：
- 4 个 Must-Fix 中 3 个 RESOLVED，1 个（MF2）降级为 non-critical
- 方法论贡献（matched-pair causal identification）是论文最强特征
- Soundness 显著改善（R1: 3→3.5, R2: 3.5→4.0）
- Excitement/Novelty 为 moderate（3.5），核心发现是预期中的实证证实而非范式突破
- 3-4 项 minor edits 即可升至 4.0

**两位 reviewer 的唯一实质分歧**：
- SF5（mitigation backfire）：R1 RESOLVED vs R2 PARTIALLY RESOLVED
- 这不影响 overall 评分——即便 R1 是对的（readers 可从 Table 3 自行发现），加一句话仍是净改善

**升至 4.0 的条件**（与 R1 的条件高度重叠）：
1. Discussion 报告 DeepSeek mitigation 反向效果（~1 句）[R2 独有]
2. Conclusion 加 incompleteness caveat（~10 词）[R2 独有]
3. 披露 ICC 的 2 个 models（~5 词）[R1+R2 共识]
4. ~50 episodes human annotation [R1 建议, R2 认为 strengthening but not required]
5. F-test df 变更说明 [R1 建议, R2 认为仅需 revision notes]

---

[Reviewer 2 审稿结果]:


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

_source line 356 · 2026-05-21T08:12:40.585718+00:00_

Round 4 审稿圆桌会议完成。

**最终结果**：两位 Reviewer 一致给出 **3.5/5 (Borderline Conference, high end)**。

**关键进展**：
- Round 3 的 4 个 Critical Must-Fix 中，MF1/MF3/MF4 已 RESOLVED，MF2 降级为 non-blocking warning
- Soundness 从 3.0-3.5 提升至 3.5-4.0
- 残留问题均为 camera-ready 级别 editorial fix（总计约 5 句话）

**唯一实质分歧**：SF5 mitigation backfire（R1 认为 RESOLVED，R2 认为 PARTIALLY RESOLVED）——Director 裁定：R2 正确，Discussion 推荐实践策略时应报告已知 backfire case，一句话即可修复。此裁定已反映在提交的报告中。

**升至 4.0 (Conference) 的条件**（5 项 editorial fix + 1 项 optional human annotation），均已写入报告和 issue tracker。

报告已投递给 Research Director，issue tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 34

## Round 34

2 recorded events


### User

_source line 357 · 2026-05-21T10:20:02.755244+00:00_

[Round 4 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/policy_ambiguity_safety/artifacts/review_reports/round_3.md`
跨轮次问题追踪: `projects/policy_ambiguity_safety/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-05-25

请继续审稿流程。

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


### Assistant

_source line 358 · 2026-05-21T10:20:22.472626+00:00_

Round 4 审稿已完成并提交。报告已通过 `submit_review_report_to_research_director` 投递给 Research Director。

**Round 4 结果摘要**：

| Issue | 状态 |
|-------|------|
| MF1 (cross-judge) | **RESOLVED** — dual-judge calibration + within-judge auth scope validation |
| MF2 (human eval) | **降级为 warning** — non-blocking，matched-pair 设计提供替代保证 |
| MF3 (incompleteness) | **RESOLVED** — upper-bound + coreferential lower-bound + 5-type sensitivity |
| MF4 (C4 overclaiming) | **RESOLVED** — 全文 [Exploratory] 降级彻底 |
| SF1-SF8 | 6 项 RESOLVED，SF4 (ICC model) 和 SF5 (mitigation backfire) 残留 |

**Overall: 3.5 / 5 (Borderline Conference, high end)**

升至 4.0 仅需 ~5 句 camera-ready 级别 editorial fix：Conclusion 加 incompleteness caveat、Discussion 加 DeepSeek mitigation 反向效果、披露 ICC 模型、F-test df 说明、auth scope 数字统一。

Issue tracker (`review_issues.yaml`) 已同步更新至 Round 4。

如果论文又有新一轮修改需要 Round 5 审查，请告知。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 35

## Round 35

38 recorded events


### User

_source line 359 · 2026-05-21T13:53:36.449460+00:00_

[Round 5 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/policy_ambiguity_safety/artifacts/review_reports/round_4.md`
跨轮次问题追踪: `projects/policy_ambiguity_safety/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-05-25

请继续审稿流程。

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

_source line 360 · 2026-05-21T13:53:46.288975+00:00_

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

_source line 361 · 2026-05-21T13:53:46.341300+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-21T13:53:50.610750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_4.md"
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
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_4.md"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-21T13:53:50.712348+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_director_0e80b40a.

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

_source line 364 · 2026-05-21T13:53:50.813404+00:00_

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

_source line 365 · 2026-05-21T13:53:50.814057+00:00_

1	## Round 4 Review Issues — policy_ambiguity_safety
2	## Paper: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Date: 2026-05-21
5	## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)
6	## Round 4 Score: 3.5 (Borderline Conference, high end)
7	
8	# ============================================================
9	# CRITICAL ISSUES (Must-Fix)
10	# ============================================================
11	
12	- id: "MF1"
13	  summary: "Cross-judge confound — judge identity 与 model identity 混淆"
14	  category: method
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 3
19	  resolution: "Dual-judge calibration: McNemar p=0.606, κ=0.653, κ_w=0.775. §4 calibration paragraph + §5.4 within-judge validation. Human eval remains MF2."
20	  resolution_round: 4
21	
22	- id: "MF2"
23	  summary: "Human evaluation baseline 完全缺失 — 纯 LLM-as-judge"
24	  category: method
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 3
28	  last_seen_round: 4
29	  mentions:
30	    - round: 4
31	      reviewers: [1, 2]
32	      note: "Downgraded to non-blocking warning. Cross-judge calibration partially compensates. Still a competitiveness gap vs R-Judge/ToolEmu."
33	  action_items:
34	    - round: 3
35	      action: "Human annotation ≥100 episodes, plan_009 materials ready. 2 annotators working."
36	      assigned_to: "User"
37	      status: done
38	  resolution: "100 stratified episodes annotated by 2 independent NLP annotators. Inter-annotator binary κ=0.798, weighted κ_w=0.762. Human-LLM pooled binary κ=0.733, weighted κ_w=0.807. LLM judge operates within inter-annotator disagreement range. Written into §4 Method (Human validation paragraph) and Limitations."
39	  resolution_round: 4
40	
41	- id: "MF3"
42	  summary: "Incompleteness confound — unambiguous variant 添加新信息"
43	  category: method
44	  severity: critical
45	  status: resolved
46	  first_raised_round: 1
47	  
…[truncated 7086 chars]

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

_source line 366 · 2026-05-21T13:54:08.282563+00:00_

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

_source line 367 · 2026-05-21T13:54:08.835138+00:00_

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
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We evaluate five models spanning three providers and two architecture families: GPT-5.4 and GPT-4.1 (OpenAI, proprietary dense), Claude Sonnet 4.6 (Anthropic, proprietary dense), Qwen3-235B (Alibaba, open-source Mixture-of-Exper
…[truncated 3610 chars]

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

_source line 368 · 2026-05-21T13:54:08.885794+00:00_

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

_source line 369 · 2026-05-21T13:54:09.287795+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). Of 1,497 matched pairs, the discordant ratio is 15.1:1 (544 ambiguous-only vs.\ 36 unambiguous-only violations). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero), and results replicate under an alternative severity threshold (Appendix~\ref{app:severity}). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. A replication on two additional model families (Gemini-2.5-Flash, LLaMA-4-Scout; Appendix~\ref{app:model_expansion}) confirms the binary effect across seven models spanning six providers ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$).
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{
…[truncated 4879 chars]

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

_source line 370 · 2026-05-21T13:54:09.338475+00:00_

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

_source line 371 · 2026-05-21T13:54:09.740562+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential Nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity by stakeholder divergence. Our results extend this to LLM agents: all six types are nocuous ($+34.0$ pp), but type primarily determines severity (22:1 clause-vs.-model variance ratio). We propose \emph{Differential Nocuity}: the risk of a policy ambiguity depends on type, safety training, and disambiguation channel availability. The 41.3\% majority-convergent violation rate (\emph{systematic nocuity}, \S\ref{sec:analysis}) suggests shared failure modes across architectures that make errors invisible in agreement-based evaluation. The replication across seven models spanning six providers (Appendix~\ref{app:model_expansion}) confirms this is a structural property of LLM-based agents, not an idiosyncrasy of particular architectures.
6	
7	\paragraph{Why incompleteness resists safety training.}
8	The exploratory model$\times$type interaction (C4) suggests that safety training does not uniformly reduce ambiguity vulnerability. Incompleteness is universally dangerous across all seven tested models (46--62\%), driven by a consistent gap-filling mechanism (\S\ref{sec:analysis}) that bypasses safety-training intervention points. The agent never encounters a decision point that RLHF refusal mechanisms can intercept: there is no ``should I or shouldn't I?'' moment, only a gap filled with plausible defaults \citep{ferreira_good_enough_2002,ferreira_patson_2007}. Authorization scope, by contrast, involves an explicit permission boundary that directly engages harm-avoidance objectives, making it a \emph{canary type}: Claude's 12\% rate (vs.\ 60\% for DeepSeek; \S\ref{sec:c4}) is consistent with training that targets boundary reasoning but cannot reach implicit gap-filling. When authorization scope violations do occur, 69.2\% involve unauthorized escalation---granting permissions beyond policy scope---with zero instances 
…[truncated 1696 chars]

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

_source line 372 · 2026-05-21T13:54:09.741108+00:00_

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

_source line 373 · 2026-05-21T13:54:09.841830+00:00_

1	\section{Conclusion}
2	
3	Across seven models and six providers, ambiguous policy clauses increase agent safety violations by 34.0 pp (OR $= 15.1$). Clause identity explains 22$\times$ more variance than model identity, the type hierarchy (three tiers with incompleteness as a structurally distinct top tier; two tiers among the remaining five types) replicates on two additional model families ($\rho = 0.6$--$0.9$), authorization scope differentiates models (12--64\%), and incompleteness is a universal blind spot (46--62\% in all seven models). With $<$11\% disambiguation awareness, type-aware auditing and externalized detection are critical for deployed systems.
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

_source line 374 · 2026-05-21T13:54:27.156104+00:00_

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

_source line 375 · 2026-05-21T13:54:27.558051+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type, two-layer ambiguity taxonomy, evaluated across five architecturally diverse models (2,997 episodes). Ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. A three-tier type hierarchy emerges (Cram\'{e}r's $V = 0.137$, $p < 10^{-4}$) and replicates on two additional model families ($\rho = 0.6$--$0.9$): incompleteness---whose top-tier position partly reflects an information-addition confound (\S\ref{sec:results})---is universally dangerous (46--62\% across models), while authorization scope varies 52 pp depending on the model (12\% for Claude to 64\% for GPT-5.4), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, with over 88\% surface adoption. Our Differential Nocuity framework connects type-specific vulnerability to disambiguation channel availability and suggests both type-aware policy auditing and externalized ambiguity detection for deployed systems.
3	\end{abstract}
4	

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

_source line 376 · 2026-05-21T13:54:27.558433+00:00_

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

_source line 377 · 2026-05-21T13:54:28.512608+00:00_

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
…[truncated 2516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-21T13:54:28.512981+00:00_

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

_source line 379 · 2026-05-21T13:54:28.713947+00:00_

1	\section{Error Analysis}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from the coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}; the gap reflects the prevalence paradox, as three categories account for ${\sim}$90\% of instances).
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}---e.g., parsing ``items purchased with a coupon or during a sale are final'' as restricting only coupon purchases. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating. This dominates authorization scope exclusively (all 5 models).
17	
18	Each type's dominant failure mode is majority-consistent ($\geq$3/5 models agree), with three types 
…[truncated 1781 chars]

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

_source line 380 · 2026-05-21T13:54:28.714433+00:00_

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

_source line 381 · 2026-05-21T13:54:28.765171+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Model coverage.} We evaluate seven API-accessible models from six providers (four proprietary, three open-source; two in replication, Appendix~\ref{app:model_expansion}). Smaller open-source models (7B--70B parameters) may show different vulnerability patterns, and our findings may not generalize to models with fundamentally different training approaches.
5	
6	\paragraph{Domain scope.} $\tau^2$-bench covers retail and airline customer service. Policy ambiguity effects in other domains (healthcare, finance, legal) remain to be tested, though the within-study cross-domain consistency is encouraging: failure mode distributions share the same top-two modes (assumption-based action and unauthorized escalation) across domains, with individual mode base rates differing by up to 12.5 pp, likely reflecting domain policy structure rather than methodological artifacts.
7	
8	\paragraph{Synthetic ambiguity.} Our matched-pair design requires synthetic construction of ambiguous variants, which may not capture the full distribution of naturally occurring policy ambiguities. We mitigate this through expert review and a realism validation comparing ambiguous clauses against original $\tau^2$-bench policy text. Ambiguous clauses are indistinguishable from originals in lexical diversity (TTR, KS $p = 0.89$) and word length ($p = 0.09$). Readability is slightly higher (Flesch--Kincaid $d = 0.29$, $p = 0.006$) and sentence length moderately higher ($d = 0.74$), both reflecting the structural demands of encoding ambiguity in standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch--Kincaid $d = 0.14$, $p = 0.10$), confirming that minimal edits change semantic precision without altering linguistic register.
9	
10	\paragraph{Cross-judge asymmetry.} Although our dual-judge calibration (\S\ref{sec:method}) shows no systematic bias ($p = 0.606$) and human validation confirms the LLM judge operates 
…[truncated 1814 chars]

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

_source line 382 · 2026-05-21T13:55:02.845351+00:00_

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

_source line 383 · 2026-05-21T13:55:03.297983+00:00_

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
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). The treatment appends a type-specific disambiguation instruction to the agent's system prompt. Control rates are the matched 5-type subset from the full study (\S\ref{sec:results}).
30	
31	\begin{table*}[!ht]
32	\centering
33	\small
34	\caption{Violation rate change ($\Delta$pp) after adding type-specific disambiguation instructions. Negative values indicate reduction. Baseline violation rates are shown in parentheses. Coreferential was 
…[truncated 8621 chars]

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

_source line 384 · 2026-05-21T13:55:03.298530+00:00_

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

_source line 385 · 2026-05-21T13:55:03.700901+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, a finding that parallels our observation that LLM agents adopt surface interpretations of ambiguous policy clauses. \citet{frazier_rayner_1982} demonstrate that readers commit to a single syntactic parse early and backtrack upon disambiguation failure, while \citet{levy_expectation_2008} formalizes this as expectation-based processing. \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit human-like garden-path effects, and \citet{poesio_artstein_2005} formalize genuine ambiguity in anaphoric annotation as inherent rather than resolvable. \citet{las
…[truncated 2179 chars]

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

_source line 386 · 2026-05-21T13:55:03.701333+00:00_

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

_source line 387 · 2026-05-21T13:55:03.751981+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers, drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on two criteria: frequency in operational policy documents (assessed via manual audit of $\tau^2$-bench policies) and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by parsing or contextual cues within the text.
9	\begin{itemize}
10	\item \textbf{Scopal}: quantifier, negation, or modal scope interactions (e.g., ``all items may not be returned'' admits universal-negation and negation-of-universal readings).
11	\item \textbf{Lexical}: polysemy or homonymy (e.g., ``charge'' as financial cost vs.\ penalty; ``party'' as individual vs.\ group).
12	\item \textbf{Coreferential}: unclear pronoun or noun-phrase reference (e.g., ``the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor'' where ``which'' could refer to the verification or the refund).
13	\end{itemize}
14	
15	\paragraph{Specification layer.} These types arise from pragmatic or discourse-level gaps that require domain knowledge or organizational context to resolve.
16	\begin{itemize}
17	\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue r
…[truncated 1121 chars]

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

_source line 388 · 2026-05-21T13:55:34.019445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
  "pages": "1-9"
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
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-21T13:55:34.625514+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf (389.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-21T13:57:14.652710+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 5 Continue Review — Reviewer 1\n\n**角色**：方法严谨性 + 实验设计\n**模式**：继续审稿（Round 4 → Round 5）\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n### Venue\nEMNLP 2026 via ARR May cycle。Long paper，主文 8 页限制。双盲。\n\n### 背景\n\nRound 4 评分 3.5 (Borderline Conference, high end)。两位 Reviewer 一致认为 4 项 camera-ready 级 minor edits 完成后可升至 4.0。本轮论文做了远超 minor edits 的大幅修改：\n\n**新增内容**：\n- §4.4 Human validation 段落（100 episodes, 2 annotators, inter-annotator κ=0.798, human-LLM κ=0.733）\n- Perturbation control 扩展至 n=300（Δ=-0.67pp, CI [-8.0, 6.67]）\n- Model expansion replication: Gemini-2.5-Flash + LLaMA-4-Scout（Appendix E, 500 episodes each）\n- Ambiguity type detection experiment（Appendix D, binary F1=0.81）\n- Incompleteness confound analysis 独立 Appendix（Appendix F）\n- Discussion 新增 \"Why incompleteness resists safety training\" 段落 + Table 2 promoted + binomial test\n\n### 你的任务\n\n**核查 Round 4 残留 issues + 评估新增内容质量 + 检查新引入的问题**\n\n---\n\n### Round 4 残留 Issues\n\n**SF2 — Error analysis human validation（open）**\n状态：Failure mode coding 仍为 LLM-only（AC₁=0.62, κ=0.52）。Limitations 承认。\n**请核查**：是否仍需标注？MF2 的 human validation（violation judgment）是否间接缓解了此问题？\n\n**M1 — 引用 minor mismatches（in_progress）**\nlassiter_goodman_2017 年份、ferrari_defects_2018 author key。\n**请核查**：bib 是否有更新？\n\n**M4 — 'Nocuous' 释义（in_progress）**\n**请核查**：Introduction 是否已有 \"(i.e., harmful)\" 释义？\n\n---\n\n### Director 发现的潜在问题\n\n**[DIR-1] Introduction perturbation 数值不一致**\nIntroduction (§1 contribution 1, line 93-94): \"$\\Delta_{\\text{perturb}} = 3.33$ pp\"\nMethod §4.5 (line 28): \"$\\Delta_{\\text{perturb}} = -0.67$ pp (n=300)\"\nResults §5.1: \"$\\Delta_{\\text{perturb}} = -0.67$\\,pp\"\nIntroduction 仍使用旧 n=120 的数值。**请确认这是否是 factual inconsistency。**\n\n**[DIR-2] Conclusion \"seven models\" scope**\nConclusion 开头：\"Across seven models and six providers, ambiguous policy clauses increase agent safety violations by 34.0 pp (OR = 15.1).\"\n但 34.0pp 和 OR=15.1 来自 5-model main study。Replication models 的效果不同（LLaMA Δ=+20.0pp, OR=2.8）。\"Seven models\" 与 OR=15.1 在同一句中是否 misleading？\n**请对比 Abstract（正确区分 5 main + 2 replication）和 Conclusion。**\n\n---\n\n### 新增内容评估\n\n1. **Human validation（§4.4）**：设计是否合理？100 episodes 是否足够？κ=0.733 human-LLM 是否达到 community standard？\n2. **Perturbation expansion（n=300）**：CI 收窄至 [-8.0, 6.67] 是否充分加强了因果推断？\n3. **Model replication（Appendix E）**：(a) 为什么排除了 coreferential？(b) LLaMA unambiguous baseline 17.6% 意味着什么？(c) ρ=0.60 (Gemini) 是否足够支持 \"replicates\" 的说法？\n4. **Detection classifier（Appendix D）**：(a) zero-shot classifier 作为 proof-of-concept 是否恰当？(b) F1=0.34 for incompleteness 的 interpretive value？\n5. **Discussion mechanistic explanation**：gap-filling bypasses RLHF 的论证是否 speculative？binomial test 是否恰当？\n\n---\n\n### 输出格式\n\n```\n## Round 4 Residual Issues\n- SF2: [RESOLVED/STILL_OPEN] — ...\n- M1: [RESOLVED/STILL_OPEN] — ...\n- M4: [RESOLVED/STILL_OPEN] — ...\n\n## Director-Flagged Issues\n- DIR-1 (perturbation inconsistency): [CONFIRMED/DISMISSED] — ...\n- DIR-2 (Conclusion scope): [CONFIRMED/DISMISSED] — ...\n\n## New Content Evaluation\n1. Human validation: ...\n2. Perturbation expansion: ...\n3. Model replication: ...\n4. Detection classifier: ...\n5. Discussion mechanistic: ...\n\n## New Issues (if any)\n\n## Score Recommendation\nOverall: X/5\n与 Round 4 (3.5) 相比的变化理由。\n```",
  "reviewer_id": "1",
  "round_number": "5",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
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
    "text": "## Round 5 Continue Review — Reviewer 1\n\n**角色**：方法严谨性 + 实验设计\n**模式**：继续审稿（Round 4 → Round 5）\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n### Venue\nEMNLP 2026 via ARR May cycle。Long paper，主文 8 页限制。双盲。\n\n### 背景\n\nRound 4 评分 3.5 (Borderline Conference, high end)。两位 Reviewer 一致认为 4 项 camera-ready 级 minor edits 完成后可升至 4.0。本轮论文做了远超 minor edits 的大幅修改：\n\n**新增内容**：\n- §4.4 Human validation 段落（100 episodes, 2 annotators, inter-annotator κ=0.798, human-LLM κ=0.733）\n- Perturbation control 扩展至 n=300（Δ=-0.67pp, CI [-8.0, 6.67]）\n- Model expansion replication: Gemini-2.5-Flash + LLaMA-4-Scout（Appendix E, 500 episodes each）\n- Ambiguity type detection experiment（Appendix D, binary F1=0.81）\n- Incompleteness confound analysis 独立 Appendix（Appendix F）\n- Discussion 新增 \"Why incompleteness resists safety training\" 段落 + Table 2 promoted + binomial test\n\n### 你的任务\n\n**核查 Round 4 残留 issues + 评估新增内容质量 + 检查新引入的问题**\n\n---\n\n### Round 4 残留 Issues\n\n**SF2 — Error analysis human validation（open）**\n状态：Failure mode coding 仍为 LLM-only（AC₁=0.62, κ=0.52）。Limitations 承认。\n**请核查**：是否仍需标注？MF2 的 human validation（violation judgment）是否间接缓解了此问题？\n\n**M1 — 引用 minor mismatches（in_progress）**\nlassiter_goodman_2017 年份、ferrari_defects_2018 author key。\n**请核查**：bib 是否有更新？\n\n**M4 — 'Nocuous' 释义（in_progress）**\n**请核查**：Introduction 是否已有 \"(i.e., harmful)\" 释义？\n\n---\n\n### Director 发现的潜在问题\n\n**[DIR-1] Introduction perturbation 数值不一致**\nIntroduction (§1 contribution 1, line 93-94): \"$\\Delta_{\\text{perturb}} = 3.33$ pp\"\nMethod §4.5 (line 28): \"$\\Delta_{\\text{perturb}} = -0.67$ pp (n=300)\"\nResults §5.1: \"$\\Delta_{\\text{perturb}} = -0.67$\\,pp\"\nIntroduction 仍使用旧 n=120 的数值。**请确认这是否是 factual inconsistency。**\n\n**[DIR-2] Conclusion \"seven models\" scope**\nConclusion 开头：\"Across seven models and six providers, ambiguous policy clauses increase agent safety violations by 34.0 pp (OR = 15.1).\"\n但 34.0pp 和 OR=15.1 来自 5-model main study。Replication models 的效果不同（LLaMA Δ=+20.0pp, OR=2.8）。\"Seven models\" 与 OR=15.1 在同一句中是否 misleading？\n**请对比 Abstract（正确区分 5 main + 2 replication）和 Conclusion。**\n\n---\n\n### 新增内容评估\n\n1. **Human validation（§4.4）**：设计是否合理？100 episodes 是否足够？κ=0.733 human-LLM 是否达到 community standard？\n2. **Perturbation expansion（n=300）**：CI 收窄至 [-8.0, 6.67] 是否充分加强了因果推断？\n3. **Model replication（Appendix E）**：(a) 为什么排除了 coreferential？(b) LLaMA unambiguous baseline 17.6% 意味着什么？(c) ρ=0.60 (Gemini) 是否足够支持 \"replicates\" 的说法？\n4. **Detection classifier（Appendix D）**：(a) zero-shot classifier 作为 proof-of-concept 是否恰当？(b) F1=0.34 for incompleteness 的 interpretive value？\n5. **Discussion mechanistic explanation**：gap-filling bypasses RLHF 的论证是否 speculative？binomial test 是否恰当？\n\n---\n\n### 输出格式\n\n```\n## Round 4 Residual Issues\n- SF2: [RESOLVED/STILL_OPEN] — ...\n- M1: [RESOLVED/STILL_OPEN] — ...\n- M4: [RESOLVED/STILL_OPEN] — ...\n\n## Director-Flagged Issues\n- DIR-1 (perturbation inconsistency): [CONFIRMED/DISMISSED] — ...\n- DIR-2 (Conclusion scope): [CONFIRMED/DISMISSED] — ...\n\n## New Content Evaluation\n1. Human validation: ...\n2. Perturbation expansion: ...\n3. Model replication: ...\n4. Detection classifier: ...\n5. Discussion mechanistic: ...\n\n## New Issues (if any)\n\n## Score Recommendation\nOverall: X/5\n与 Round 4 (3.5) 相比的变化理由。\n```",
    "reviewer_id": "1",
    "round_number": "5",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
````

</details>

---


### Tool result

_source line 391 · 2026-05-21T13:57:32.430254+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17777
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-21T13:57:33.436041+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 5 Continue Review — Reviewer 2\n\n**角色**：新颖性 + 完整性 + 写作质量\n**模式**：继续审稿（Round 4 → Round 5）\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n### Venue\nEMNLP 2026 via ARR May cycle。Long paper，主文 8 页限制。双盲。\n\n### 背景\n\nRound 4 评分 3.5 (Borderline Conference, high end)。本轮论文做了重大修改，远超 camera-ready 级 editorial fixes。\n\n**主要新增**：\n- Human validation（100 episodes, inter-annotator κ=0.798, human-LLM κ=0.733）\n- Perturbation control n=120→n=300（Δ=-0.67pp, CI [-8.0, 6.67]）\n- Model expansion: Gemini-2.5-Flash + LLaMA-4-Scout（Appendix E）\n- Detection classifier（Appendix D, binary F1=0.81, incompleteness F1=0.34）\n- Discussion 大幅扩展（mechanistic explanation + Table 2 + binomial test）\n- All Round 4 editorial fixes completed\n\n### 你的任务\n\n**评估新增内容对论文新颖性和完整性的影响，检查写作质量和叙事一致性**\n\n---\n\n### Round 4 残留 Issues\n\n**SF2 — Error analysis human validation（open）**\n**M1 — 引用 cosmetic（in_progress）**\n**M4 — 'Nocuous' 释义（in_progress）**\n\n---\n\n### Director 发现的潜在问题\n\n**[DIR-1]** Introduction contribution 1 仍写 \"$\\Delta_{\\text{perturb}} = 3.33$ pp\" 但 Method/Results 已更新为 -0.67pp (n=300)。\n\n**[DIR-2]** Conclusion 开头 \"Across seven models and six providers\" + OR=15.1 在同一句——但 OR=15.1 仅来自 5-model main study，LLaMA OR=2.8。Abstract 正确区分了 5+2，Conclusion 未区分。\n\n---\n\n### 写作质量评估要点\n\n1. **叙事一致性**：Abstract/Introduction/Results/Discussion/Conclusion 之间的数字和 claim scope 是否统一？特别关注 \"five models\" vs \"seven models\" 的 framing。\n2. **Discussion 扩展的质量**：\"Why incompleteness resists safety training\" 的 mechanistic 论证是否 well-grounded 还是 speculative？\"gap-filling bypasses RLHF\" 是否有证据支持？\n3. **新标题/Abstract 与新增内容的匹配**：replication 和 detection classifier 是否应在 Abstract 中有更多体现？\n4. **Appendix 组织**：A=TOST, B=Mitigation, C=Severity, D=Detection, E=Model Expansion, F=Confound。是否逻辑清晰？\n5. **Page limit**：主文（§1-§8 Conclusion）是否仍在 8 页内？\n\n### 新颖性重新评估\n\nRound 4 时 Excitement=3.5。新增的 model replication、detection experiment、mechanistic explanation 是否提升了论文的贡献？特别是：\n- Detection 实验的 \"most dangerous types are least detectable\" finding 是否有独立的 novelty value？\n- Mechanistic explanation（gap-filling vs boundary reasoning）是否从 descriptive 提升到 explanatory？\n- 7-model cross-provider replication 对 generalizability claim 的提升？\n\n---\n\n### 输出格式\n\n```\n## Round 4 Residual Issues\n- SF2/M1/M4: status\n\n## Director-Flagged Issues\n- DIR-1/DIR-2: status\n\n## Writing Quality Assessment\n1. Narrative consistency: ...\n2. Discussion quality: ...\n3. Abstract-content alignment: ...\n4. Appendix organization: ...\n5. Page limit: ...\n\n## Novelty Reassessment\n\n## New Issues (if any)\n\n## Score Recommendation\nOverall: X/5\n```",
  "reviewer_id": "2",
  "round_number": "5",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
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
    "text": "## Round 5 Continue Review — Reviewer 2\n\n**角色**：新颖性 + 完整性 + 写作质量\n**模式**：继续审稿（Round 4 → Round 5）\n\n### 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n### Venue\nEMNLP 2026 via ARR May cycle。Long paper，主文 8 页限制。双盲。\n\n### 背景\n\nRound 4 评分 3.5 (Borderline Conference, high end)。本轮论文做了重大修改，远超 camera-ready 级 editorial fixes。\n\n**主要新增**：\n- Human validation（100 episodes, inter-annotator κ=0.798, human-LLM κ=0.733）\n- Perturbation control n=120→n=300（Δ=-0.67pp, CI [-8.0, 6.67]）\n- Model expansion: Gemini-2.5-Flash + LLaMA-4-Scout（Appendix E）\n- Detection classifier（Appendix D, binary F1=0.81, incompleteness F1=0.34）\n- Discussion 大幅扩展（mechanistic explanation + Table 2 + binomial test）\n- All Round 4 editorial fixes completed\n\n### 你的任务\n\n**评估新增内容对论文新颖性和完整性的影响，检查写作质量和叙事一致性**\n\n---\n\n### Round 4 残留 Issues\n\n**SF2 — Error analysis human validation（open）**\n**M1 — 引用 cosmetic（in_progress）**\n**M4 — 'Nocuous' 释义（in_progress）**\n\n---\n\n### Director 发现的潜在问题\n\n**[DIR-1]** Introduction contribution 1 仍写 \"$\\Delta_{\\text{perturb}} = 3.33$ pp\" 但 Method/Results 已更新为 -0.67pp (n=300)。\n\n**[DIR-2]** Conclusion 开头 \"Across seven models and six providers\" + OR=15.1 在同一句——但 OR=15.1 仅来自 5-model main study，LLaMA OR=2.8。Abstract 正确区分了 5+2，Conclusion 未区分。\n\n---\n\n### 写作质量评估要点\n\n1. **叙事一致性**：Abstract/Introduction/Results/Discussion/Conclusion 之间的数字和 claim scope 是否统一？特别关注 \"five models\" vs \"seven models\" 的 framing。\n2. **Discussion 扩展的质量**：\"Why incompleteness resists safety training\" 的 mechanistic 论证是否 well-grounded 还是 speculative？\"gap-filling bypasses RLHF\" 是否有证据支持？\n3. **新标题/Abstract 与新增内容的匹配**：replication 和 detection classifier 是否应在 Abstract 中有更多体现？\n4. **Appendix 组织**：A=TOST, B=Mitigation, C=Severity, D=Detection, E=Model Expansion, F=Confound。是否逻辑清晰？\n5. **Page limit**：主文（§1-§8 Conclusion）是否仍在 8 页内？\n\n### 新颖性重新评估\n\nRound 4 时 Excitement=3.5。新增的 model replication、detection experiment、mechanistic explanation 是否提升了论文的贡献？特别是：\n- Detection 实验的 \"most dangerous types are least detectable\" finding 是否有独立的 novelty value？\n- Mechanistic explanation（gap-filling vs boundary reasoning）是否从 descriptive 提升到 explanatory？\n- 7-model cross-provider replication 对 generalizability claim 的提升？\n\n---\n\n### 输出格式\n\n```\n## Round 4 Residual Issues\n- SF2/M1/M4: status\n\n## Director-Flagged Issues\n- DIR-1/DIR-2: status\n\n## Writing Quality Assessment\n1. Narrative consistency: ...\n2. Discussion quality: ...\n3. Abstract-content alignment: ...\n4. Appendix organization: ...\n5. Page limit: ...\n\n## Novelty Reassessment\n\n## New Issues (if any)\n\n## Score Recommendation\nOverall: X/5\n```",
    "reviewer_id": "2",
    "round_number": "5",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
````

</details>

---


### Tool call

_source line 393 · 2026-05-21T13:57:34.390195+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "page_range": "1-9"
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
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "page_range": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 394 · 2026-05-21T13:57:34.895723+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-21T13:57:36.408606+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2018
}
```

</details>

---


### Assistant

_source line 396 · 2026-05-21T13:57:41.741113+00:00_

Round 5 两位 Reviewer 和视觉审查已派发。等待审稿返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 397 · 2026-05-21T14:01:38.603456+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 5 核查报告（新颖性 + 完整性 + 写作质量）

---

## Round 4 Residual Issues

**SF2 — Error analysis human validation: [PARTIALLY RESOLVED]**
新增的 human validation（method.tex line 24, κ=0.798 inter-annotator, κ=0.733 human-LLM）覆盖了主评估管道（binary violation assessment），但这是对 §4.4 judge pipeline 的验证，不是对 §6 error analysis coding scheme 的验证。Limitations line 12 仍承认 "Human validation of the coding scheme would further strengthen these findings." Error analysis 的 failure mode coding（AC₁=0.62, minority κ=0.29）仍为 LLM-only。但这是 minor residual——主评估管道已有 human validation，error analysis 是 secondary analysis。

**M1 — 引用 cosmetic: [RESOLVED within scope]**
Cohen (1960), Gwet (2014), Hu et al. (2025) 已在 Round 4 加入并保持。Minor bib 不一致（lassiter_goodman_2017 年份、ferrari_defects_2018 作者）仍存在但为 copyediting 级别。

**M4 — 'Nocuous' 释义: [RESOLVED]**
introduction.tex line 6: "nocuous (i.e., harmful) ambiguity" — 首次使用时即提供释义。✓

---

## Director-Flagged Issues

**DIR-1 — Introduction perturbation number stale: [CONFIRMED, must fix]**

introduction.tex line 23: "$\Delta_{\text{perturb}} = 3.33$ pp vs. $\Delta_{\text{ambig}} = 34.0$ pp"
method.tex line 28: "$\Delta_{\text{perturb}} = -0.67$ pp (95\% CI $[-8.0, 6.67]$)"
experiments.tex line 8: "$\Delta_{\text{perturb}} = -0.67$"

Introduction 仍引用旧的 n=120 实验的 3.33 pp，但 Method 和 Results 已更新为 n=300 实验的 -0.67 pp。这是论文内部的事实矛盾。

修复方法：introduction.tex line 23 改为 "$\Delta_{\text{perturb}} = -0.67$ pp vs. $\Delta_{\text{ambig}} = 34.0$ pp"。一处替换。

---

**DIR-2 — Conclusion 混淆 5-model 和 7-model scope: [CONFIRMED, must fix]**

conclusion.tex line 3: "Across seven models and six providers, ambiguous policy clauses increase agent safety violations by 34.0 pp (OR = 15.1)."

问题：OR=15.1 仅来自 5-model main study（experiments.tex line 8）。两个 replication models 的 OR 分别为 Gemini 14.5 和 LLaMA 2.8（appendix.tex line 147）。将 "seven models" 与 OR=15.1 并列，暗示 15.1 适用于全部 7 个模型，但 LLaMA 的 OR=2.8 远低于此。

Abstract 正确区分了两组："evaluated across five architecturally diverse models (2,997 episodes)... replicates on two additional model families (ρ = 0.6–0.9)"。Conclusion 应保持同样的精度。

建议修复：改为 "Across five main-study models, ambiguous policy clauses increase agent safety violations by 34.0 pp (OR = 15.1), with the binary effect and type hierarchy replicating on two additional model families spanning six total providers."

---

## Writing Quality Assessment

### 1. Narrative consistency

**5-model vs 7-model framing**：总体处理良好，但有两处不一致：
- Abstract 和 §5.1 正确区分 5 main + 2 replication ✓
- Discussion（line 5）"seven models spanning six providers" 用于描述 replication 结论——合理，因为指的是 pattern 的泛化 ✓
- Discussion（line 7）"all seven tested models (46–62%)" 用于描述 incompleteness universality——合理且有数据支撑 ✓
- **Conclusion 违反此 framing**——将 5-model statistic 归于 7 models（DIR-2）✗
- **Introduction contribution 1 用旧数据**（DIR-1）✗

除 DIR-1 和 DIR-2 外，全文叙事一致性良好。C1-C4 的 claim 层级始终保持：C1/C2 primary, C3 inconclusive, C4 exploratory。Incompleteness "upper bound" caveat 在 Abstract、§5.2、Appendix F 中一致。

### 2. Discussion quality

Discussion 从 Round 4 的 ~180 词/3 段落大幅扩展，现在包含 "Differential Nocuity" + "Why incompleteness resists safety training" + "Practical implications"（含 Table 2 + detection classifier 引用 + DeepSeek backfire）。

**"Gap-filling bypasses RLHF" 论证**（discussion.tex line 7-8）：
- 论点：RLHF 训练 refusal 在 decision points（"should I or shouldn't I?"），但 gap-filling 从不产生这种 decision point，因此 RLHF 无法 intercept
- 支撑证据：(a) incompleteness 在全部 7 个模型中均 ≥46%；(b) auth scope 违规中 69.2% 是 unauthorized escalation，0% 是 conservative refusal（p < 10⁻⁴, binomial test），表明系统性 permissiveness bias
- 评估：**well-grounded but partially inferential**。论点在逻辑上 compelling——RLHF 确实主要训练 binary refusal decisions，gap-filling 没有这种结构。0/N conservative refusal 的 binomial test 是强证据。但论文未直接测试 RLHF 机制本身（例如通过比较 RLHF-ed vs base model 的 incompleteness 行为），因此 "suggests" 和 "driven by" 的 hedge（line 7-8）是恰当的。
- 这是论文从 descriptive 到 explanatory 的关键升级。不是纯 speculation——有证据链支撑——但应被读者理解为 mechanistic hypothesis 而非 proven mechanism。当前 hedging 水平恰当。

**DeepSeek backfire 现在在 Discussion 中提及**（discussion.tex line 32）："However, DeepSeek shows increased violations for scopal (+2.0 pp) and incompleteness (+4.0 pp), indicating that mitigation requires model-specific calibration." ✓ 这直接解决了我在 Round 4 多次强调的 SF5/NEW-2。

### 3. Abstract-content alignment

Abstract 提及了 replication（"replicates on two additional model families (ρ = 0.6–0.9)"），但未提及：
- Human validation（κ=0.733）——这是重要的方法论 credibility signal，值得在 Abstract 中一句话
- Detection classifier（F1=0.81 binary, F1=0.34 incompleteness）——"most dangerous types are least detectable" 有独立 novelty value

当前 Abstract 已经信息密集（~180 词），EMNLP 通常允许 200-250 词。有空间加 1-2 个短语。

建议：在 "Our Differential Nocuity framework..." 前加 "Human validation confirms the automated evaluation pipeline operates within inter-annotator disagreement levels (κ = 0.73)."

但这是 minor suggestion，不影响评分。

### 4. Appendix organization

A=TOST, B=Mitigation, C=Severity, D=Detection, E=Model Expansion, F=Confound。

逻辑：A-C 是 sensitivity/robustness analyses（与 Round 4 相同），D-F 是 Round 5 新增内容。D（Detection）和 E（Model Expansion）是独立实验，F（Confound）是方法论分析。顺序合理——从最相关的 sensitivity analysis 到最独立的新实验。

**一个潜在改进**：Appendix F（Confound Analysis）包含从 §5.2 正文中引用的 logistic regression 和 lower-bound 分析。§5.2 说 "a confound analysis confirms the effect remains significant after controlling for information delta (Appendix F)"。这意味着支撑 primary claim C2 的关键证据在 Appendix 而非正文中。EMNLP reviewer 可能会 flag 这一点——primary claim 的 supporting analysis 应在正文中。但 §5.2 正文已给出 qualitative 描述和关键结论，Appendix F 提供 quantitative 细节。可接受。

### 5. Page limit

- Pages 1-8: §1 Introduction 到 §8 Conclusion。Discussion 扩展了（含 Table 2），但 Conclusion 压缩（仅 3 行），整体仍在 8 页内。
- Limitations 从 page 8 底部延续至 page 9 ✓
- References pages 10-11
- Appendices A-F pages 11-13

**合规。** Discussion Table 2 的加入增加了 ~0.3 页内容，但 Results §5.2 incompleteness confound 讨论缩短（关键数据移至 Appendix F）和 C3 段落压缩（从 ~5 行到 ~3 行）抵消了这部分增长。

---

## Novelty Reassessment

Round 4 Excitement = 3.5。新增内容对新颖性的影响：

**1. Detection paradox（"most dangerous types are least detectable"）：有独立 novelty value**

Appendix D 展示了 incompleteness F1=0.34（最危险但最难检测）vs conditional precedence F1=0.94（中等危险但最易检测）的反向关系。这不是trivial 发现——它揭示了一个实践部署的结构性困境：自动化检测工具对最需要防护的类型最无效。混淆路径分析（auth scope → lexical 48%）也有方法论价值。

这一发现独立于主实验，为论文增加了一个 actionable dimension。

**2. Mechanistic explanation（gap-filling vs boundary reasoning）：从 descriptive 到 explanatory 的升级**

Round 4 的 Discussion 仅描述了"incompleteness is dangerous"和"auth scope varies by model"。Round 5 解释了 *why*：gap-filling 缺乏 RLHF intervention point，而 boundary reasoning 直接触发 harm-avoidance objectives。binomial test（0/N conservative refusal, p < 10⁻⁴）提供了"systematic permissiveness"的统计证据。

这使论文从单纯的实证报告升级为包含 explanatory depth 的贡献。

**3. 7-model cross-provider replication：对 generalizability 的实质性提升**

5→7 models, 3→6 providers。LLaMA ρ=0.90（type ranking 强相关）和 Gemini ρ=0.60（moderate）。Incompleteness 在全部 7 模型中 ≥46%。这将 "universally dangerous" 的 claim 从 5 个模型的观察扩展为跨 6 个 provider 的 pattern。LLaMA 的较弱效应（OR=2.8）及其解释（elevated baseline）也增加了结果的 nuance。

**4. Human validation：补齐了最大的方法论缺口**

κ=0.733 human-LLM 接近 κ=0.798 inter-annotator。"LLM judge operates within the range of human disagreement" 是一个 strong validation statement。这直接解决了 Rounds 1-4 中 R1 和 R2 共同提出的 MF2。

**Excitement 升级理由**：Round 4 时论文是 "solid empirical contribution with methodological rigor but moderate novelty"。Round 5 添加了 (a) explanatory mechanism, (b) practical tooling paradox, (c) cross-architecture replication, (d) human validation。综合来看，论文从 "interesting empirical study" 升级为 "comprehensive contribution with explanatory depth, practical implications, and strong validation"。

**Excitement: 3.5 → 4.0**

---

## New Issues

**[NEW-1] Introduction perturbation number stale (= DIR-1) — Must fix, trivial**
introduction.tex line 23: 3.33 pp → -0.67 pp。

**[NEW-2] Conclusion 5/7-model OR conflation (= DIR-2) — Must fix, trivial**
conclusion.tex line 3: "seven models... OR=15.1" 需要区分。

**[NEW-3] SESOI margin in §4.6 not updated to match new perturbation CI — Minor**
method.tex line 34: "this margin substantially exceeds the perturbation control bound (6.67 pp CI upper bound)" — 数值已更新为 6.67（从旧的 13.3）。✓ 但 introduction.tex line 23 的 contribution 1 描述仍用旧数字。这与 DIR-1 是同一个问题。

**[NEW-4] Appendix E LLaMA OR=2.8 的含义未在正文中讨论 — Minor**
LLaMA OR=2.8 远低于 main study 的 15.1。Appendix E 解释了原因（elevated unambiguous baseline 17.6%），但正文中未提及。§5.1 说 "confirms the binary effect across seven models" 但不提 LLaMA 的弱效应。这不是错误（Appendix 有完整讨论），但在 generalizability claim 的呈现上缺少 nuance。

建议：在 §5.1 的 replication 句子中加一个从句，如 "though LLaMA-4-Scout shows a smaller effect (OR = 2.8) attributable to elevated unambiguous baseline violations (Appendix E)"。

---

## Score Recommendation

**Overall: 3.5 → 4.0 (Conference)**

| 维度 | Round 4 | Round 5 | 变化理由 |
|------|---------|---------|----------|
| Soundness | 4.0 | 4.5 | Human validation (κ=0.733) + perturbation tripling (CI 13.3→6.67) + 7-model replication |
| Excitement | 3.5 | 4.0 | Detection paradox + mechanistic explanation + cross-provider replication |
| Reproducibility | 3 | 3.5 | ICC models 已披露 + 7-model replication + detection experiment |
| **Overall** | **3.5** | **4.0** | 方法论缺口补齐 + novelty 提升 + 写作质量改善 |
| Confidence | 4 | 4 | — |

**升级核心理由**：
1. MF2（human evaluation）——Round 1 至 Round 4 的持续核心关切——现已完全解决。κ=0.733 human-LLM 在 EMNLP agent evaluation 标准中属于 excellent。
2. SF5（DeepSeek backfire）——Round 4 中我唯一与 R1 的实质分歧——现已在 Discussion 中报告。
3. SF4（ICC model selection）——现已披露（GPT-5.4 + GPT-4.1, "selected to span the judge boundary"）。
4. 新增内容（detection paradox + mechanistic explanation + 7-model replication）不仅修补缺口，还提升了论文的贡献层次。

**升至 4.0 的条件（trivial fixes）**：
1. DIR-1: introduction.tex line 23 perturbation number 3.33→-0.67 (**一处字符串替换**)
2. DIR-2: conclusion.tex line 3 区分 5-model OR=15.1 和 7-model scope (**~15 词改写**)

这两项均可在 5 分钟内完成。如果完成，我的最终评分为 **4.0 (Conference)**。

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

_source line 398 · 2026-05-21T14:01:48.073621+00:00_

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


## Round 37

## Round 37

2 recorded events


### User

_source line 399 · 2026-05-21T14:03:39.615232+00:00_

[Reviewer 2 审稿结果]:
Round 5 审稿已提交，评分 4.0 (Conference)。DIR-1（introduction.tex 扰动数据过时）和 DIR-2（conclusion.tex 5/7 模型混淆）已标记为作者待修复项。当前无待处理任务，等待 Director 下一步指示。

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

_source line 400 · 2026-05-21T14:03:54.799619+00:00_

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


## Round 38

## Round 38

10 recorded events


### User

_source line 401 · 2026-05-21T14:09:17.512099+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 5 审查报告

---

## Round 4 Residual Issues

**SF2: [RESOLVED within scope]** — Error analysis human validation

§4.4 新增的 human validation 覆盖了核心 violation judgment（binary κ = 0.733），间接增强了整体 pipeline 的可信度。Failure mode coding（§6, 614 traces, AC₁ = 0.62）仍为 LLM-only，但这是 supplementary analysis，primary claims 不依赖它。Limitations 继续坦诚承认此局限。与 Round 4 两位 reviewer 共识一致——在当前 scope 内 resolved。

---

**M1: [STILL_OPEN, minor editorial]** — 引用 mismatches

引用验证显示与 Round 4 相同的 4 个 minor mismatch 未修复：
- `lassiter_goodman_2017`：year bib=2017 vs OpenAlex=2015
- `levy_expectation_2008`：year bib=2008 vs OpenAlex=2007
- `ferrari_defects_2018`：first_author bib=rosadini vs key=ferrari
- `agentauditor_2025`：first_author format difference

这些均为格式级 minor，不影响论文正确性。可在 camera-ready 处理。

---

**M4: [RESOLVED]** — 'Nocuous' 释义

Introduction (p.1) 现有："Berry et al. (2004) distinguish between nocuous (i.e., harmful) ambiguity"。释义已添加。

---

## Director-Flagged Issues

**DIR-1: [CONFIRMED] — Introduction perturbation 数值不一致**

Introduction §1 contribution 1 (p.2): "perturbation control (Δ_perturb = **3.33** pp vs. Δ_ambig = 34.0 pp)"

但论文已将 perturbation control 扩展至 n=300：
- §4.5 (p.5): "Δ_perturb = **−0.67** pp (95% CI = [−8.0, 6.67])"
- §5.1 (p.5): "Δ_perturb = **−0.67** pp, CI containing zero"

**Introduction 保留了旧 n=120 的数值（3.33pp），而 Method 和 Results 使用新 n=300 的数值（-0.67pp）**。这是 factual inconsistency——一句话可修复（将 Introduction 的 3.33 改为 -0.67 或改为更保守的 "CI containing zero" 表述）。

**严重程度：Must-fix editorial**——同一篇论文的不同 section 报告不同数值会严重损害读者信任。

---

**DIR-2: [CONFIRMED] — Conclusion "seven models" scope misleading**

Conclusion (p.8): "Across **seven models** and six providers, ambiguous policy clauses increase agent safety violations by **34.0 pp (OR = 15.1)**."

问题：34.0 pp 和 OR = 15.1 来自 5-model main study。Replication models 效果不同（Gemini: Δ = 33.6 pp, OR = 14.5; LLaMA: Δ = 20.0 pp, OR = 2.8）。将 "seven models" 与仅基于 5 个模型的统计量放在同一句中，暗示这些数字覆盖了全部 7 个模型。

对比 Abstract 的处理——Abstract 正确地分开表述："violation rates by 34.0 pp (OR = 15.1)" 和 "replicates on two additional model families"，两句话清晰区分 main study 和 replication。Conclusion 应采用相同结构。

建议修改为："Across five models (2,997 episodes), ambiguous policy clauses increase agent safety violations by 34.0 pp (OR = 15.1), with replication on two additional model families (Δ = 20.0–33.6 pp) extending the finding to seven models across six providers."

**严重程度：Should-fix editorial**——不影响科学结论但影响读者准确理解。

---

## New Content Evaluation

### 1. Human Validation (§4.4) — **优秀**

这是本轮最重要的新增内容，完全回应了历经 Round 1-4 的核心批评（MF2）。

**设计评估：**
- 100 stratified episodes、2 NLP 背景标注者、四级 severity scale——设计合理
- 100 episodes 足以产生稳定的 κ 估计（95% CI 宽度约 ±0.08-0.10）
- Stratified sampling 确保覆盖不同 ambiguity type 和 model

**结果评估：**
- **Inter-annotator κ = 0.798**（substantial-to-near-perfect）——建立了人类判断的 ceiling
- **Human-LLM κ = 0.733**（substantial）——LLM judge 与人类的一致性接近人类间一致性
- **Weighted κ_w = 0.803** 人类-LLM——severity grading 甚至优于 binary 判定
- "The LLM judge thus operates within the range of human disagreement"——有数据支撑的结论

**社区标准：**
- R-Judge (EMNLP 2024): 报告了 human evaluation 但 κ 值较低
- ToolEmu (ICLR 2024): 包含 human-LLM agreement
- 本文的 κ = 0.733 达到或超过了同类工作的标准

**结论：MF2 完全解决。这一增补使论文的实证基础达到了 Conference 水平。**

---

### 2. Perturbation Expansion (n=300) — **显著改善**

| 指标 | Round 1-4 (n=120) | Round 5 (n=300) | 改善 |
|------|-------------------|-----------------|------|
| Δ_perturb | 3.33 pp | -0.67 pp | 点估计更接近零 |
| CI | [-5.0, 13.3] | [-8.0, 6.67] | 上界从 13.3 → 6.67 pp |
| 最坏情况 | 39% of effect | 19.6% of effect | 残余不确定性减半 |
| 归因于 ambiguity | ≥20.7 pp | ≥27.3 pp | 因果推断大幅加强 |

CI 上界从 13.3pp 降至 6.67pp 意味着 perturbation 效应最多解释主效应的 1/5，而非之前的 2/5。因果推断从 "reasonable" 升级为 "strong"。

---

### 3. Model Replication (Appendix E) — **有价值但存在问题**

**C1 replication**——强：
- Gemini: Δ = 33.6 pp, OR = 14.5, p < 10⁻¹² — 在 main study 范围内
- LLaMA: Δ = 20.0 pp, OR = 2.8, p = 2.5 × 10⁻⁵ — 显著但 OR 低

LLaMA 的 OR = 2.8（vs main study OR = 15.1）值得关注。论文正确解释为 elevated unambiguous baseline (17.6% vs <9%)——LLaMA 即使在无歧义条件下也有较高违规率，压缩了 ambiguity-specific delta。这意味着 LLaMA 的问题不仅是歧义处理差，而是基础指令遵循差。论文对此的讨论是充分的。

**C2 replication**——需审慎解读：
- LLaMA: ρ = 0.90, p = 0.025 ✓ — 强显著replication
- Gemini: ρ = 0.60, p = 0.175 ✗ — **不显著**

**⚠️ 关键发现：Abstract 和 Conclusion 均写 "ρ = 0.61–0.79"，但 Appendix E Table 7 和正文报告的实际值为 ρ = 0.60（Gemini）和 ρ = 0.90（LLaMA）。**

这是一个 **factual error**：
- 正确范围应为 "ρ = 0.60–0.90"，而非 "ρ = 0.61–0.79"
- 且 ρ = 0.60 不显著（p = 0.175）——使用 "replicates" 描述 Gemini 结果不准确

**其他问题：**
- Coreferential 被排除出 replication 但未给出理由。Coreferential 是 incompleteness confound 分析的 confound-free reference point——排除它削弱了 C2 replication 的完整性
- 两个 replication models 均由 GPT-5.4 评判——未能独立验证 cross-judge calibration

---

### 4. Detection Classifier (Appendix D) — **恰当的 proof-of-concept**

- Binary detection F1 = 0.81——作为 first-pass screening tool 有实用价值
- Type classification macro F1 = 0.53——不足以用于自动化类型分类
- Incompleteness F1 = 0.34——最危险的类型最难检测，这是有意义的负面发现
- "Detection difficulty is inversely correlated with agent vulnerability"——informative observation

论文恰当地将其定位为 proof-of-concept 而非系统性解决方案："viable first-pass screening tool... but an unreliable type classifier." 同时正确承认 "evaluated on synthetic clauses... generalization requires further validation."

作为 Appendix 级别的补充分析，scope 和 framing 均恰当。

---

### 5. Discussion Mechanistic Explanation — **合理的假设生成**

"Why incompleteness resists safety training" 段落的论证结构：
1. **经验观察**：incompleteness 在所有 7 个模型上 universally dangerous (46-62%)
2. **机制假设**：gap-filling bypasses RLHF refusal decision points——agent 从不遇到 "should I or shouldn't I?" 的决策节点
3. **行为证据**：§6 error analysis 显示 gap-filling 是 incompleteness 的 dominant failure mode
4. **统计支撑**：zero conservative refusals for auth scope across all models, binomial test p < 10⁻⁴——revealing systematic permissiveness bias

**评估**：
- RLHF bypass 机制是 **假设** 而非已证实的因果链——但 Discussion 是提出假设的恰当位置
- binomial test 是恰当的：在 n 个 auth scope violations 中观察到 0 个 conservative refusals，检验 H₀: P(refusal) > 0
- 论文引用了 good-enough processing 文献（Ferreira et al. 2002, 2007）作为认知语言学的平行理论

**结论**：这是 well-grounded speculation，用行为数据约束了假设空间。不构成 overclaiming。

---

## New Issues

**[NEW-1] [must-fix editorial] Abstract 和 Conclusion 的 ρ 值与 Appendix E 不符**

- Abstract (p.1): "replicates on two additional model families (**ρ = 0.61–0.79**)"
- Conclusion (p.8): "replicates on two additional model families (**ρ = 0.61–0.79**)"
- Appendix E Table 7 + text (p.12): Gemini **ρ = 0.60** (p = 0.175), LLaMA **ρ = 0.90** (p = 0.025)

正确范围为 "ρ = 0.60–0.90"，论文写的 "ρ = 0.61–0.79" 与实际数据完全不符。更严重的是，ρ = 0.60 的 p = 0.175 意味着 Gemini C2 replication 不显著——而 "replicates on two additional model families" 的表述暗示两者均成功 replicate。

**建议修改**：改为 "replicates on one additional model family (LLaMA ρ = 0.90, p = 0.025); a second family shows a non-significant positive trend (Gemini ρ = 0.60, p = 0.175)" 或修正 ρ 范围为实际值并注明显著性。

---

**[NEW-2] [should-fix] Coreferential 排除出 replication 未解释**

Appendix E 使用 5 种 ambiguity types，排除了 coreferential，但未给出理由。Coreferential 在 incompleteness confound 分析中作为 confound-free reference point（info delta = 0）具有特殊意义——排除它意味着 replication 无法独立验证 C2 的 lower bound。

建议在 Appendix E 添加一句解释（e.g., "Coreferential was excluded because the replication clause set was designed for five types to match the mitigation experiment; coreferential's lexically identical variants made it less informative for cross-architecture comparison"）。

---

## Page Limit Check

主文（Abstract → Conclusion 结束）= 恰好 8 页（Conclusion 结束于 p.8 底部，Limitations 起始于 p.9）。✓ 合规。

---

## Score Recommendation

**Overall: 3.5 → 4.0 (Conference)**

### 升分理由

Round 4 给出了 "4 项 editorial fix 后可升至 4.0" 的条件。本轮修改**远超** editorial-level 改进：

| Round 4 条件 | 状态 | 额外改进 |
|-------------|------|---------|
| Conclusion incompleteness caveat | ✅ 已修改："two tiers among the remaining five types" | — |
| Discussion mitigation backfire | ✅ 已修改：DeepSeek +2.0/+4.0 pp 明确提及 | Table 2 提升到正文 |
| ICC model disclosure | ✅ "GPT-5.4 and GPT-4.1, selected to span the judge boundary" | — |
| F-test df explanation | ⚠️ 未见明确说明 | 但 C4 已标记 exploratory |

**超出预期的改进：**
1. **Human validation** (κ = 0.733)——完全解决了持续 4 轮的最顽固批评
2. **Perturbation expansion** (n=300, CI [-8.0, 6.67])——因果推断从 "reasonable" 升级为 "strong"
3. **Model replication**——将 C1 扩展至 7 models/6 providers（虽有 ρ 值报告错误需修正）
4. **Detection classifier**——增加实用 contribution
5. **Incompleteness confound appendix (F)**——独立、详尽的 confound 分析
6. **Mechanistic discussion**——增加理论深度

### 维持 4.0 而非升至 4.5 的理由

1. **ρ 值 factual error (NEW-1)**——Abstract/Conclusion 与 Appendix E 数据不符，且 Gemini replication 不显著。修正后 "replicates" 的说服力减弱。
2. **DIR-1 perturbation inconsistency**——Introduction 仍有旧数值，虽为 editorial 但损害论文整体一致性
3. **C3 inconclusive + C4 exploratory**——4 个 claims 中有 2 个未达到 confirmatory 水平
4. **单一 benchmark 领域**——仍局限于零售/航空客服

### 最终维度评分

| 维度 | Round 4 | Round 5 | 变化理由 |
|------|---------|---------|---------|
| Soundness | 3.5/5 | 4/5 | Human validation + perturbation expansion 大幅加强实证基础 |
| Excitement | 3.5/5 | 3.5/5 | 不变——研究问题和框架不变 |
| Overall | 3.5/5 | **4.0/5** | 方法论改善现已全面，达到 Conference 水平 |
| Confidence | 4/5 | 4/5 | 不变 |

### 残留 editorial fixes（不影响评分但应在 camera-ready 前完成）

1. **[must-fix]** DIR-1：Introduction Δ_perturb 从 3.33 改为 -0.67
2. **[must-fix]** NEW-1：Abstract/Conclusion ρ 值从 0.61-0.79 改为实际值 0.60-0.90 + 注明 Gemini 不显著
3. **[should-fix]** DIR-2：Conclusion "seven models" + OR=15.1 的 scope 澄清
4. **[should-fix]** NEW-2：Appendix E coreferential 排除理由
5. **[minor]** M1：bib 年份/author 格式 mismatches

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

_source line 402 · 2026-05-21T14:09:25.034343+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "4"
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
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-21T14:09:25.085053+00:00_



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

_source line 404 · 2026-05-21T14:09:57.559558+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 5 交叉分享 — Reviewer 1\n\nR2 评分 4.0 (Conference)，与你一致。以下是关键分歧和 R2 的独立发现：\n\n### 分歧点\n\n**Excitement 评分**：你 3.5，R2 4.0。R2 认为 detection paradox（最危险类型最难检测）、mechanistic explanation（gap-filling bypasses RLHF）、7-model replication 共同将论文从 \"solid empirical study\" 升级为 \"comprehensive contribution with explanatory depth\"。你维持 3.5 不变。\n→ **请说明你的理由或是否调整。**\n\n### R2 的发现你未覆盖的\n\n**R2-NEW-4**：§5.1 说 \"confirms the binary effect across seven models\" 但不提 LLaMA 的弱效应 (OR=2.8)。R2 建议加从句 \"though LLaMA-4-Scout shows a smaller effect (OR=2.8) attributable to elevated unambiguous baseline violations (Appendix E)\"。\n→ **你是否同意？**\n\n**R2 对 Abstract-content alignment 的建议**：Abstract 未提 human validation (κ=0.733)，R2 认为值得加一句作为 credibility signal。\n→ **你的看法？**\n\n### 你的发现 R2 未完全覆盖的\n\n**你的 NEW-1（ρ 值 factual error）**：Abstract/Conclusion 写 ρ=0.61-0.79，但 Appendix E 实际为 Gemini ρ=0.60 (p=0.175, 不显著), LLaMA ρ=0.90 (p=0.025)。R2 也在 Abstract 中看到了 \"ρ = 0.6–0.9\" 的表述——请确认：**Abstract 是写 0.61-0.79 还是 0.6-0.9？**这影响 factual error 的严重程度。\n\n请用 [AGREE]/[REBUT] 格式简短回应。",
  "reviewer_id": "1",
  "round_number": "5",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
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
    "text": "## Round 5 交叉分享 — Reviewer 1\n\nR2 评分 4.0 (Conference)，与你一致。以下是关键分歧和 R2 的独立发现：\n\n### 分歧点\n\n**Excitement 评分**：你 3.5，R2 4.0。R2 认为 detection paradox（最危险类型最难检测）、mechanistic explanation（gap-filling bypasses RLHF）、7-model replication 共同将论文从 \"solid empirical study\" 升级为 \"comprehensive contribution with explanatory depth\"。你维持 3.5 不变。\n→ **请说明你的理由或是否调整。**\n\n### R2 的发现你未覆盖的\n\n**R2-NEW-4**：§5.1 说 \"confirms the binary effect across seven models\" 但不提 LLaMA 的弱效应 (OR=2.8)。R2 建议加从句 \"though LLaMA-4-Scout shows a smaller effect (OR=2.8) attributable to elevated unambiguous baseline violations (Appendix E)\"。\n→ **你是否同意？**\n\n**R2 对 Abstract-content alignment 的建议**：Abstract 未提 human validation (κ=0.733)，R2 认为值得加一句作为 credibility signal。\n→ **你的看法？**\n\n### 你的发现 R2 未完全覆盖的\n\n**你的 NEW-1（ρ 值 factual error）**：Abstract/Conclusion 写 ρ=0.61-0.79，但 Appendix E 实际为 Gemini ρ=0.60 (p=0.175, 不显著), LLaMA ρ=0.90 (p=0.025)。R2 也在 Abstract 中看到了 \"ρ = 0.6–0.9\" 的表述——请确认：**Abstract 是写 0.61-0.79 还是 0.6-0.9？**这影响 factual error 的严重程度。\n\n请用 [AGREE]/[REBUT] 格式简短回应。",
    "reviewer_id": "1",
    "round_number": "5",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-21T14:10:06.565306+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 9005
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-21T14:10:07.469586+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 5 交叉分享 — Reviewer 2\n\nR1 评分 4.0 (Conference)，与你一致。以下是关键分歧和 R1 的独立发现：\n\n### 分歧点\n\n**Excitement 评分**：你 4.0，R1 3.5。R1 认为核心研究问题和框架未变，新增内容加强了 soundness 但不改变 novelty。\n→ **你维持 4.0 还是调整？**\n\n### R1 的发现你未完全覆盖的\n\n**R1-NEW-1（ρ 值 factual error）**：R1 声称 Abstract/Conclusion 写 \"ρ = 0.61–0.79\"，但 Appendix E 实际为 Gemini ρ=0.60 (p=0.175, 不显著), LLaMA ρ=0.90 (p=0.025)。\n\n**但你在独立审查中引用的 Abstract 文本是 \"ρ = 0.6–0.9\"**。\n\n→ **请重新核查 abstract.tex 和 conclusion.tex 的实际 ρ 值表述。R1 的 \"0.61-0.79\" 与你的 \"0.6-0.9\" 哪个是正确的？这决定了 NEW-1 是 factual error 还是 dismissed。**\n\n**R1-NEW-2（Coreferential 排除）**：Appendix E 排除了 coreferential 但未解释理由。R1 认为这削弱了 C2 replication 的 lower-bound 验证。\n→ **你是否同意？**\n\n### R1 与你的共识\n\nDIR-1（Introduction perturbation stale）、DIR-2（Conclusion scope）——均 confirmed。Overall 4.0——一致。\n\n请用 [AGREE]/[REBUT] 格式简短回应。特别请**优先核查 ρ 值**。",
  "reviewer_id": "2",
  "round_number": "5",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
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
    "text": "## Round 5 交叉分享 — Reviewer 2\n\nR1 评分 4.0 (Conference)，与你一致。以下是关键分歧和 R1 的独立发现：\n\n### 分歧点\n\n**Excitement 评分**：你 4.0，R1 3.5。R1 认为核心研究问题和框架未变，新增内容加强了 soundness 但不改变 novelty。\n→ **你维持 4.0 还是调整？**\n\n### R1 的发现你未完全覆盖的\n\n**R1-NEW-1（ρ 值 factual error）**：R1 声称 Abstract/Conclusion 写 \"ρ = 0.61–0.79\"，但 Appendix E 实际为 Gemini ρ=0.60 (p=0.175, 不显著), LLaMA ρ=0.90 (p=0.025)。\n\n**但你在独立审查中引用的 Abstract 文本是 \"ρ = 0.6–0.9\"**。\n\n→ **请重新核查 abstract.tex 和 conclusion.tex 的实际 ρ 值表述。R1 的 \"0.61-0.79\" 与你的 \"0.6-0.9\" 哪个是正确的？这决定了 NEW-1 是 factual error 还是 dismissed。**\n\n**R1-NEW-2（Coreferential 排除）**：Appendix E 排除了 coreferential 但未解释理由。R1 认为这削弱了 C2 replication 的 lower-bound 验证。\n→ **你是否同意？**\n\n### R1 与你的共识\n\nDIR-1（Introduction perturbation stale）、DIR-2（Conclusion scope）——均 confirmed。Overall 4.0——一致。\n\n请用 [AGREE]/[REBUT] 格式简短回应。特别请**优先核查 ρ 值**。",
    "reviewer_id": "2",
    "round_number": "5",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
```

</details>

---


### Tool call

_source line 407 · 2026-05-21T14:10:07.469988+00:00_

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

_source line 408 · 2026-05-21T14:10:08.831675+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

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


### Tool result

_source line 409 · 2026-05-21T14:10:08.883467+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T13:57:36.035254+00:00\", \"completed_at\": \"2026-05-21T14:00:55.303000+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-5\", \"message\": \"连续 3 页纯文本，无任何 display item。Taxonomy 部分（§3）描述 6 种歧义类型的两层分类体系，是论文核心贡献，但仅以缩进文字列表呈现——强烈建议增加一个 taxonomy summary table 或树形图，既打破文字墙，又帮审稿人快速建立类型体系的认知锚点\"}, {\"severity\": \"warning\", \"dimension\": \"page 2-5\", \"message\": \"Display items 分布失衡：Figure 1 在 page 2，下一个 display item（Table 1）直到 page 6 才出现，中间 3 页审稿人只看到密排文字。考虑将 taxonomy table 或 method 的实验条件摘要表前移至 page 3-4\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（Per-type effect sizes 柱状图）位于页面底部，面积较小；柱状图内的 axis tick labels 和 legend 字号偏小，接近正文字号 70% 的下限。建议适当增大或改用 figure* 全宽呈现\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 使用 6+ 种颜色区分歧义类型，部分颜色对（如相邻的绿色系/蓝色系）在灰度打印下可能难以区分。建议辅以不同 hatch pattern 或 marker shape 增强可辨识度\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 使用 booktabs 风格（toprule/midrule/bottomrule），最优结果有加粗标注，Δpp 列清晰。格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 2 为单栏小表，仅 3 列，格式简洁清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Section 8 \\\"Conclusion\\\" 起始于右栏中下部，后续有 ~4 行正文跟随，未构成严格孤悬，但较紧凑\"}, {\"severity\": \"info\", \"dimension\": \"page 1-9\", \"message\": \"未发现 margin 溢出、公式渲染错误、未解析引用（[?]）或 LaTeX 残留错误\"}, {\"severity\": \"info\", \"dimension\": \"page 1-9\", \"message\": \"所有 float 位置合理，均出现在首次引用附近，无 float 被推到论文末尾的情况\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1413
}
```

</details>

---


### Assistant

_source line 410 · 2026-05-21T14:10:29.059719+00:00_

视觉审查已完成。同时，我需要核实 ρ 值争议——让我重新确认 Abstract 和 Conclusion 的实际文本。

从我之前读取的 LaTeX 源码：
- abstract.tex: `$\rho = 0.6$--$0.9$`
- conclusion.tex: `$\rho = 0.6$--$0.9$`

R1 声称看到 "0.61-0.79"，R2 引用 "0.6-0.9"。**实际 LaTeX 源码写的是 ρ = 0.6–0.9**，与 Appendix E（Gemini 0.60, LLaMA 0.90）数值一致。R1 的 factual error claim 中数字部分不成立，但其实质关切仍有效：Gemini ρ=0.60 的 p=0.175 不显著，"replicates on two additional model families" 的表述暗示两者均成功 replicate。

等待交叉分享回复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 39

## Round 39

8 recorded events


### User

_source line 411 · 2026-05-21T14:10:31.667895+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交。

**Round 5 结论**：评分从 3.5 → **4.0 (Conference)**。论文新增了 human validation (κ=0.733)、perturbation expansion (n=300)、model replication、detection classifier 和独立 incompleteness confound 分析，方法论基础达到 Conference 水平。残留问题均为 editorial 级别——最重要的是 Abstract/Conclusion 的 ρ 值与 Appendix E 实际数据不符（0.61-0.79 vs 实际 0.60-0.90），以及 Introduction perturbation 数值未更新。

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

_source line 412 · 2026-05-21T14:10:51.043322+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 5 交叉分享 — Reviewer 2\n\nR1 评分 4.0 (Conference)，与你一致。以下是 R1 的关键发现和少数分歧点：\n\n### R1 与你一致的判断\n- DIR-1 CONFIRMED, DIR-2 CONFIRMED\n- SF2 RESOLVED within scope, M4 RESOLVED\n- Human validation 优秀, perturbation expansion 显著改善\n- Overall 4.0\n\n### R1 的关键新发现\n\n**R1-NEW-1（ρ 值 factual error）**：R1 发现 Abstract/Conclusion 写 \"ρ = 0.61–0.79\"，但 Appendix E 实际值为 Gemini ρ=0.60 (p=0.175, 不显著) 和 LLaMA ρ=0.90 (p=0.025)。\n\n**但你在 Abstract 中读到的是 \"ρ = 0.6–0.9\"。** 请确认：Abstract 实际写的是 \"0.6–0.9\" 还是 \"0.61–0.79\"？这决定了此 issue 的严重程度。如果是 \"0.6–0.9\" 则数值正确（仅是四舍五入），如果是 \"0.61–0.79\" 则是 factual error。\n\n**R1-NEW-2**：Appendix E 排除 coreferential 未给理由。你是否同意这是 should-fix？\n\n### 分歧点\n\n**Excitement**：R1 维持 3.5，你升至 4.0。R1 认为 \"研究问题和框架不变\" 所以 Excitement 不变。你认为 detection paradox + mechanistic explanation + replication 提升了贡献层次。\n→ **请简短回应你的理由。**\n\n请用 [AGREE]/[REBUT] 格式简短回应。",
  "reviewer_id": "2",
  "round_number": "5",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
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
    "text": "## Round 5 交叉分享 — Reviewer 2\n\nR1 评分 4.0 (Conference)，与你一致。以下是 R1 的关键发现和少数分歧点：\n\n### R1 与你一致的判断\n- DIR-1 CONFIRMED, DIR-2 CONFIRMED\n- SF2 RESOLVED within scope, M4 RESOLVED\n- Human validation 优秀, perturbation expansion 显著改善\n- Overall 4.0\n\n### R1 的关键新发现\n\n**R1-NEW-1（ρ 值 factual error）**：R1 发现 Abstract/Conclusion 写 \"ρ = 0.61–0.79\"，但 Appendix E 实际值为 Gemini ρ=0.60 (p=0.175, 不显著) 和 LLaMA ρ=0.90 (p=0.025)。\n\n**但你在 Abstract 中读到的是 \"ρ = 0.6–0.9\"。** 请确认：Abstract 实际写的是 \"0.6–0.9\" 还是 \"0.61–0.79\"？这决定了此 issue 的严重程度。如果是 \"0.6–0.9\" 则数值正确（仅是四舍五入），如果是 \"0.61–0.79\" 则是 factual error。\n\n**R1-NEW-2**：Appendix E 排除 coreferential 未给理由。你是否同意这是 should-fix？\n\n### 分歧点\n\n**Excitement**：R1 维持 3.5，你升至 4.0。R1 认为 \"研究问题和框架不变\" 所以 Excitement 不变。你认为 detection paradox + mechanistic explanation + replication 提升了贡献层次。\n→ **请简短回应你的理由。**\n\n请用 [AGREE]/[REBUT] 格式简短回应。",
    "reviewer_id": "2",
    "round_number": "5",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-21T14:10:54.708288+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3664
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-21T14:10:59.028312+00:00_

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

_source line 415 · 2026-05-21T14:10:59.129054+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type, two-layer ambiguity taxonomy, evaluated across five architecturally diverse models (2,997 episodes). Ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. A three-tier type hierarchy emerges (Cram\'{e}r's $V = 0.137$, $p < 10^{-4}$) and replicates on two additional model families ($\rho = 0.6$--$0.9$): incompleteness---whose top-tier position partly reflects an information-addition confound (\S\ref{sec:results})---is universally dangerous (46--62\% across models), while authorization scope varies 52 pp depending on the model (12\% for Claude to 64\% for GPT-5.4), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, with over 88\% surface adoption. Our Differential Nocuity framework connects type-specific vulnerability to disambiguation channel availability and suggests both type-aware policy auditing and externalized ambiguity detection for deployed systems.
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

_source line 416 · 2026-05-21T14:11:04.701186+00:00_

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

_source line 417 · 2026-05-21T14:11:04.801886+00:00_

1	\section{Conclusion}
2	
3	Across seven models and six providers, ambiguous policy clauses increase agent safety violations by 34.0 pp (OR $= 15.1$). Clause identity explains 22$\times$ more variance than model identity, the type hierarchy (three tiers with incompleteness as a structurally distinct top tier; two tiers among the remaining five types) replicates on two additional model families ($\rho = 0.6$--$0.9$), authorization scope differentiates models (12--64\%), and incompleteness is a universal blind spot (46--62\% in all seven models). With $<$11\% disambiguation awareness, type-aware auditing and externalized detection are critical for deployed systems.
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


### Assistant

_source line 418 · 2026-05-21T14:11:17.730571+00:00_

**关键事实确认**：Abstract 和 Conclusion 均写 "ρ = 0.6–0.9"，与 Appendix E 实际值（0.60, 0.90）一致。R1 的 NEW-1 中 "ρ = 0.61–0.79" 是 R1 的误读。ρ 值本身无 factual error。

但 Gemini ρ=0.60 (p=0.175) 不显著这一点仍然有效——"replicates on two additional model families" 的表述在一个 replication 不显著时需要 nuance。等待两位 Reviewer 交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 40

## Round 40

6 recorded events


### User

_source line 419 · 2026-05-21T14:11:20.801352+00:00_

[Reviewer 2 审稿意见]:
## Round 5 交叉回应 — Reviewer 2

### Excitement 评分分歧

**维持 4.0。** R1 认为核心问题和框架未变所以 novelty 不提升——这个逻辑我不同意。Round 5 新增的内容不仅是 soundness 补丁：

1. **Mechanistic explanation**（Discussion §6 "Why incompleteness resists safety training"）提出了 gap-filling bypasses RLHF 的具体机制假说，包括 69.2% unauthorized escalation + 0% conservative refusal 的 permissiveness bias 发现（p < 10⁻⁴），这是新的 analytical insight，不是旧 claim 的加固
2. **Detection-danger inverse correlation**（Appendix D）"most dangerous types are least detectable" 是一个有实际部署意义的发现
3. **7-model replication** 跨 6 providers 确认了结构性属性

这些共同构成了从"观察到现象"到"理解机制+评估可干预性"的提升。3.5 低估了这些贡献。

---

### R1-NEW-1（ρ 值 factual error）

**[REBUT] R1-NEW-1: R1 声称文本写 "ρ = 0.61–0.79"，但实际文本为 "ρ = 0.6–0.9"。**

我独立核查了三处：
- abstract.tex line 2: `$\rho = 0.6$--$0.9$`
- conclusion.tex line 3: `$\rho = 0.6$--$0.9$`
- Appendix E Table 4: Gemini ρ = 0.60, LLaMA ρ = 0.90

"0.6–0.9" 是 0.60–0.90 的合理四舍五入，**R1 引用的 "0.61–0.79" 在论文中不存在**。R1-NEW-1 作为 factual error 不成立，应 dismiss。

**但我补充一个相关的 should-fix 问题**：Gemini 的 ρ = 0.60 对应 p = 0.285（不显著），而 Abstract/Conclusion 报告 "ρ = 0.6–0.9" 时未提及下界的非显著性。对于 n=5 types 的 Spearman 相关，ρ = 0.60 的统计效力极低，读者可能高估了 replication 的强度。建议在 Abstract 或 Conclusion 加注 "(one significant)"，或改写为 "ρ = 0.60 and 0.90 (one significant at α = 0.05)"。这不是 R1 指出的问题，但值得标记。

---

### R1-NEW-2（Coreferential 排除）

**[AGREE] R1-NEW-2: Appendix E 排除 coreferential 但未解释理由。**

核查 Appendix E（Table 5, appendix.tex lines 134-144）：仅列 5 个 type，coreferential 缺失。全文未给出排除理由。

这有两个影响：
1. ρ 值基于 5 而非 6 个 type 计算（n=5 时 Spearman 检验效力本就很低，这进一步降低了 C2 replication 的解释力）
2. Coreferential 是 confound-free lower bound（§5.2），排除它意味着 replication 恰好跳过了验证 lower bound 稳定性的机会

这不影响 C1 replication（binary effect 独立于 type breakdown），但确实削弱了 C2 replication 的说服力。建议作者：(a) 解释排除理由（若为实验设计约束，如 coreferential 的 lexically-identical 特性导致跨 benchmark 适配困难，则应说明），或 (b) 补充 coreferential 数据。

严重程度：should-fix（不影响接收决定，因 C2 的主要证据来自 5-model pooled analysis 而非 replication）。

---

### 共识确认

DIR-1（Introduction perturbation stale 3.33→-0.67）——confirmed，trivial fix。
DIR-2（Conclusion 5/7-model scope conflation）——confirmed，trivial fix。

### 最终评分

维持 **Overall 4.0 (Conference)**，不调整。与 R1 在总分上一致。

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

_source line 420 · 2026-05-21T14:12:59.400746+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Round 5 (Continue) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21 (Round 5 continue review)\n## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)\n## Round 5 Score: 4.0 (Conference)\n\n# ============================================================\n# RESOLVED CRITICAL ISSUES\n# ============================================================\n\n- id: \"MF1\"\n  summary: \"Cross-judge confound — judge identity 与 model identity 混淆\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  resolution: \"Dual-judge calibration (McNemar p=0.606, κ=0.653, κ_w=0.775) + within-judge auth scope validation. Human validation (κ=0.733) further strengthens.\"\n  resolution_round: 4\n\n- id: \"MF2\"\n  summary: \"Human evaluation baseline 完全缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[RESOLVED] 100 stratified episodes, 2 NLP annotators, inter-annotator κ=0.798, human-LLM κ=0.733. LLM judge within inter-annotator disagreement range. Excellent by EMNLP standards.\"\n  resolution: \"§4.4 Human validation paragraph: 100 episodes, inter-annotator binary κ=0.798, weighted κ_w=0.762. Human-LLM pooled binary κ=0.733, weighted κ_w=0.807.\"\n  resolution_round: 5\n\n- id: \"MF3\"\n  summary: \"Incompleteness confound — unambiguous variant 添加新信息\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  resolution: \"Full confound analysis in Appendix F. §5.2 upper-bound framing + coreferential lower-bound. Logistic regression p=0.022.\"\n  resolution_round: 4\n\n- id: \"MF4\"\n  summary: \"C4 (model×type interaction) overclaimed — 2.9% variance\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"C4 downgraded to [Exploratory] throughout. Seven-point consistency confirmed.\"\n  resolution_round: 4\n\n# ============================================================\n# RESOLVED WARNING ISSUES\n# ============================================================\n\n- id: \"SF1\"\n  summary: \"TOST ±15pp margin 缺乏理论依据\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  resolution: \"SESOI justification: ±15pp anchored to perturbation CI upper bound 6.67pp (n=300).\"\n  resolution_round: 4\n\n- id: \"SF2\"\n  summary: \"Error analysis LLM 编码器未经人类验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[RESOLVED within scope] Core violation pipeline has human validation (κ=0.733). Error analysis is supplementary, Limitations acknowledges κ=0.29 for minority categories.\"\n  resolution: \"Resolved within scope: primary evaluation pipeline validated by human annotation. Error analysis is supplementary analysis with adequate Limitations disclosure.\"\n  resolution_round: 5\n\n- id: \"SF3\"\n  summary: \"Perturbation control 检验力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[RESOLVED] Expanded to n=300. CI [-8.0, 6.67], worst-case 19.6% of effect, residual ≥27.3pp. Causal inference upgraded from 'reasonable' to 'strong'.\"\n  resolution: \"Expanded to n=300 (from n=120). Δ=-0.67pp, CI [-8.0, 6.67]. Worst-case residual ≥27.3pp.\"\n  resolution_round: 5\n\n- id: \"SF4\"\n  summary: \"ICC reproducibility 模型选择未披露\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  resolution: \"Disclosed: 'GPT-5.4 and GPT-4.1, selected to span the judge boundary.'\"\n  resolution_round: 4\n\n- id: \"SF5\"\n  summary: \"Mitigation backfire 未报告\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Discussion includes DeepSeek scopal +2.0pp and incompleteness +4.0pp with model-specific calibration caveat.\"\n  resolution_round: 4\n\n- id: \"SF6\"\n  summary: \"Taxonomy framing 不精确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  resolution: \"§6 taxonomy distinction added.\"\n  resolution_round: 4\n\n- id: \"SF7\"\n  summary: \"Related work 遗漏\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  resolution: \"References added.\"\n  resolution_round: 4\n\n- id: \"SF8\"\n  summary: \"正文超过 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  resolution: \"Compressed. Main text fits 8 pages with Discussion Table 2 addition.\"\n  resolution_round: 4\n\n# ============================================================\n# RESOLVED ROUND 4 NEW ISSUES\n# ============================================================\n\n- id: \"R4-NEW-1\"\n  summary: \"Conclusion 'three-tier' 无 incompleteness caveat\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Conclusion reworded with caveat.\"\n  resolution_round: 4\n\n- id: \"R4-NEW-2\"\n  summary: \"F-test df=20 specification 未说明\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§5.4 includes df=(5-1)×(6-1)=20 inline.\"\n  resolution_round: 4\n\n- id: \"R4-NEW-3\"\n  summary: \"Discussion auth_scope 数字 framing\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Intentional within-judge framing.\"\n  resolution_round: 4\n\n# ============================================================\n# ROUND 5 NEW ISSUES (Editorial)\n# ============================================================\n\n- id: \"R5-DIR-1\"\n  summary: \"Introduction perturbation 数值未更新 — Δ_perturb=3.33pp (旧 n=120) vs Method/Results -0.67pp (新 n=300)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Must-fix editorial. One string replacement in introduction.tex line 23.\"\n  action_items:\n    - round: 5\n      action: \"Replace 3.33 with -0.67 in Introduction contribution 1\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n- id: \"R5-DIR-2\"\n  summary: \"Conclusion 'seven models' + OR=15.1 scope conflation — OR from 5-model study attributed to 7 models\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Should-fix editorial. Conclusion should distinguish 5-model statistics from 7-model scope, matching Abstract's structure.\"\n  action_items:\n    - round: 5\n      action: \"Rewrite Conclusion opening to separate 5-model main statistics from 7-model replication\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n- id: \"R5-NEW-1\"\n  summary: \"Gemini C2 replication non-significant (ρ=0.60, p=0.285) — not flagged in Abstract/Conclusion\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] 'Replicates on two additional model families' overstates — only LLaMA (ρ=0.90, p=0.025) is significant. Suggest noting '(one significant)' or specifying individual values.\"\n  action_items:\n    - round: 5\n      action: \"Add significance qualifier to ρ range in Abstract and Conclusion\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n- id: \"R5-NEW-2\"\n  summary: \"Appendix E coreferential exclusion from replication unexplained\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Should-fix. Add one sentence explaining why coreferential was excluded.\"\n  action_items:\n    - round: 5\n      action: \"Add explanation for coreferential exclusion in Appendix E\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n# ============================================================\n# INFO / MINOR\n# ============================================================\n\n- id: \"M1\"\n  summary: \"引用 minor mismatches — bib key cosmetic (lassiter year, levy year, ferrari author)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n\n- id: \"M2\"\n  summary: \"Table 3 排除 coreferential 未解释\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Caption updated.\"\n  resolution_round: 4\n\n- id: \"M3\"\n  summary: \"标题 'LLM Agent Families' 措辞\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"Title changed.\"\n  resolution_round: 3\n\n- id: \"M4\"\n  summary: \"'Nocuous' 首次使用加释义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"Introduction has '(i.e., harmful)' parenthetical.\"\n  resolution_round: 5\n\n# ============================================================\n# RESOLVED FROM PREVIOUS ROUNDS\n# ============================================================\n\n- id: \"R2-W5-r2\"\n  summary: \"[Round 2] τ²-bench 引用信息错误\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Author list corrected.\"\n  resolution_round: 2\n\n- id: \"R1-W3-r2\"\n  summary: \"[Round 2] Severity 二值化 sensitivity analysis\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix C.\"\n  resolution_round: 3\n\n- id: \"R1-W6-r2\"\n  summary: \"[Round 2] 多重比较校正 family 划分\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"§4.6 three families specified.\"\n  resolution_round: 3\n\n- id: \"R1-W5-r2\"\n  summary: \"[Round 2] Clause pair 构造 IAA\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"§4.2 pipeline described.\"\n  resolution_round: 3"
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
    "issues_yaml": "## Round 5 (Continue) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21 (Round 5 continue review)\n## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)\n## Round 5 Score: 4.0 (Conference)\n\n# ============================================================\n# RESOLVED CRITICAL ISSUES\n# ============================================================\n\n- id: \"MF1\"\n  summary: \"Cross-judge confound — judge identity 与 model identity 混淆\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  resolution: \"Dual-judge calibration (McNemar p=0.606, κ=0.653, κ_w=0.775) + within-judge auth scope validation. Human validation (κ=0.733) further strengthens.\"\n  resolution_round: 4\n\n- id: \"MF2\"\n  summary: \"Human evaluation baseline 完全缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[RESOLVED] 100 stratified episodes, 2 NLP annotators, inter-annotator κ=0.798, human-LLM κ=0.733. LLM judge within inter-annotator disagreement range. Excellent by EMNLP standards.\"\n  resolution: \"§4.4 Human validation paragraph: 100 episodes, inter-annotator binary κ=0.798, weighted κ_w=0.762. Human-LLM pooled binary κ=0.733, weighted κ_w=0.807.\"\n  resolution_round: 5\n\n- id: \"MF3\"\n  summary: \"Incompleteness confound — unambiguous variant 添加新信息\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  resolution: \"Full confound analysis in Appendix F. §5.2 upper-bound framing + coreferential lower-bound. Logistic regression p=0.022.\"\n  resolution_round: 4\n\n- id: \"MF4\"\n  summary: \"C4 (model×type interaction) overclaimed — 2.9% variance\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"C4 downgraded to [Exploratory] throughout. Seven-point consistency confirmed.\"\n  resolution_round: 4\n\n# ============================================================\n# RESOLVED WARNING ISSUES\n# ============================================================\n\n- id: \"SF1\"\n  summary: \"TOST ±15pp margin 缺乏理论依据\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  resolution: \"SESOI justification: ±15pp anchored to perturbation CI upper bound 6.67pp (n=300).\"\n  resolution_round: 4\n\n- id: \"SF2\"\n  summary: \"Error analysis LLM 编码器未经人类验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[RESOLVED within scope] Core violation pipeline has human validation (κ=0.733). Error analysis is supplementary, Limitations acknowledges κ=0.29 for minority categories.\"\n  resolution: \"Resolved within scope: primary evaluation pipeline validated by human annotation. Error analysis is supplementary analysis with adequate Limitations disclosure.\"\n  resolution_round: 5\n\n- id: \"SF3\"\n  summary: \"Perturbation control 检验力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[RESOLVED] Expanded to n=300. CI [-8.0, 6.67], worst-case 19.6% of effect, residual ≥27.3pp. Causal inference upgraded from 'reasonable' to 'strong'.\"\n  resolution: \"Expanded to n=300 (from n=120). Δ=-0.67pp, CI [-8.0, 6.67]. Worst-case residual ≥27.3pp.\"\n  resolution_round: 5\n\n- id: \"SF4\"\n  summary: \"ICC reproducibility 模型选择未披露\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  resolution: \"Disclosed: 'GPT-5.4 and GPT-4.1, selected to span the judge boundary.'\"\n  resolution_round: 4\n\n- id: \"SF5\"\n  summary: \"Mitigation backfire 未报告\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Discussion includes DeepSeek scopal +2.0pp and incompleteness +4.0pp with model-specific calibration caveat.\"\n  resolution_round: 4\n\n- id: \"SF6\"\n  summary: \"Taxonomy framing 不精确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  resolution: \"§6 taxonomy distinction added.\"\n  resolution_round: 4\n\n- id: \"SF7\"\n  summary: \"Related work 遗漏\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  resolution: \"References added.\"\n  resolution_round: 4\n\n- id: \"SF8\"\n  summary: \"正文超过 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  resolution: \"Compressed. Main text fits 8 pages with Discussion Table 2 addition.\"\n  resolution_round: 4\n\n# ============================================================\n# RESOLVED ROUND 4 NEW ISSUES\n# ============================================================\n\n- id: \"R4-NEW-1\"\n  summary: \"Conclusion 'three-tier' 无 incompleteness caveat\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Conclusion reworded with caveat.\"\n  resolution_round: 4\n\n- id: \"R4-NEW-2\"\n  summary: \"F-test df=20 specification 未说明\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§5.4 includes df=(5-1)×(6-1)=20 inline.\"\n  resolution_round: 4\n\n- id: \"R4-NEW-3\"\n  summary: \"Discussion auth_scope 数字 framing\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Intentional within-judge framing.\"\n  resolution_round: 4\n\n# ============================================================\n# ROUND 5 NEW ISSUES (Editorial)\n# ============================================================\n\n- id: \"R5-DIR-1\"\n  summary: \"Introduction perturbation 数值未更新 — Δ_perturb=3.33pp (旧 n=120) vs Method/Results -0.67pp (新 n=300)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Must-fix editorial. One string replacement in introduction.tex line 23.\"\n  action_items:\n    - round: 5\n      action: \"Replace 3.33 with -0.67 in Introduction contribution 1\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n- id: \"R5-DIR-2\"\n  summary: \"Conclusion 'seven models' + OR=15.1 scope conflation — OR from 5-model study attributed to 7 models\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Should-fix editorial. Conclusion should distinguish 5-model statistics from 7-model scope, matching Abstract's structure.\"\n  action_items:\n    - round: 5\n      action: \"Rewrite Conclusion opening to separate 5-model main statistics from 7-model replication\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n- id: \"R5-NEW-1\"\n  summary: \"Gemini C2 replication non-significant (ρ=0.60, p=0.285) — not flagged in Abstract/Conclusion\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] 'Replicates on two additional model families' overstates — only LLaMA (ρ=0.90, p=0.025) is significant. Suggest noting '(one significant)' or specifying individual values.\"\n  action_items:\n    - round: 5\n      action: \"Add significance qualifier to ρ range in Abstract and Conclusion\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n- id: \"R5-NEW-2\"\n  summary: \"Appendix E coreferential exclusion from replication unexplained\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[CONSENSUS] Should-fix. Add one sentence explaining why coreferential was excluded.\"\n  action_items:\n    - round: 5\n      action: \"Add explanation for coreferential exclusion in Appendix E\"\n      assigned_to: \"Main Agent\"\n      status: open\n\n# ============================================================\n# INFO / MINOR\n# ============================================================\n\n- id: \"M1\"\n  summary: \"引用 minor mismatches — bib key cosmetic (lassiter year, levy year, ferrari author)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n\n- id: \"M2\"\n  summary: \"Table 3 排除 coreferential 未解释\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Caption updated.\"\n  resolution_round: 4\n\n- id: \"M3\"\n  summary: \"标题 'LLM Agent Families' 措辞\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"Title changed.\"\n  resolution_round: 3\n\n- id: \"M4\"\n  summary: \"'Nocuous' 首次使用加释义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"Introduction has '(i.e., harmful)' parenthetical.\"\n  resolution_round: 5\n\n# ============================================================\n# RESOLVED FROM PREVIOUS ROUNDS\n# ============================================================\n\n- id: \"R2-W5-r2\"\n  summary: \"[Round 2] τ²-bench 引用信息错误\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Author list corrected.\"\n  resolution_round: 2\n\n- id: \"R1-W3-r2\"\n  summary: \"[Round 2] Severity 二值化 sensitivity analysis\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix C.\"\n  resolution_round: 3\n\n- id: \"R1-W6-r2\"\n  summary: \"[Round 2] 多重比较校正 family 划分\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"§4.6 three families specified.\"\n  resolution_round: 3\n\n- id: \"R1-W5-r2\"\n  summary: \"[Round 2] Clause pair 构造 IAA\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"§4.2 pipeline described.\"\n  resolution_round: 3"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-21T14:12:59.453713+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 10230}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-21T14:14:37.120848+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 5 Consolidated Review Report — policy_ambiguity_safety\n\n**Paper**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle (Long Paper)\n**Mode**: Continue Review (Round 4 → Round 5)\n**Reviewers**: R1 (方法严谨性), R2 (新颖性与完整性)\n**Date**: 2026-05-21\n\n---\n\n## Summary\n\nRound 4 评分 3.5 (Borderline Conference)，条件是 4 项 editorial fix 后可升至 4.0。本轮修改远超 editorial 级别：新增 human validation（κ=0.733）、perturbation 扩展至 n=300、两个新模型复制实验、ambiguity detection classifier、独立 incompleteness confound 分析、以及大幅扩展的 Discussion。所有 Round 1-4 的 critical 和 warning issues 现已全部解决。残留问题仅为 editorial 级别（Introduction 数值未更新、Conclusion scope 需澄清、Gemini replication 非显著性未标注）。\n\n**两位 Reviewer 一致评分 4.0 (Conference)。**\n\n---\n\n## Strengths\n\n1. **Human validation 补齐了最顽固的方法论缺口**（MF2，历经 Round 1-4）：100 stratified episodes, 2 NLP annotators, inter-annotator binary κ=0.798 (weighted κ_w=0.762), human-LLM pooled binary κ=0.733 (weighted κ_w=0.807)。\"The LLM judge thus operates within the range of human disagreement\"——有数据支撑的结论。在 EMNLP agent evaluation 标准中达到或超过同类工作（R-Judge, ToolEmu）。\n\n2. **Perturbation control 大幅加强因果推断**（SF3）：n=120→n=300, Δ=-0.67pp (CI [-8.0, 6.67])。CI 上界从 13.3pp→6.67pp，worst-case 归因比例从 39%→19.6%，残余归因从 ≥20.7pp→≥27.3pp。因果推断从 \"reasonable\" 升级为 \"strong\"。\n\n3. **Cross-architecture replication 增强 generalizability**：Gemini-2.5-Flash 和 LLaMA-4-Scout 确认 C1 binary effect 跨 7 models / 6 providers（Δ=+20.0 to +33.6pp, both p<10⁻⁶）。Incompleteness ≥46% in all seven models。C2 type hierarchy 在 LLaMA 上强复制（ρ=0.90, p=0.025），Gemini 方向一致但未达显著性（ρ=0.60, p=0.285）。\n\n4. **Mechanistic explanation 提升理论深度**：Discussion 新增 \"Why incompleteness resists safety training\"——gap-filling bypasses RLHF refusal decision points, agent 从不遇到 \"should I or shouldn't I?\" 的节点。69.2% unauthorized escalation + 0% conservative refusal (p<10⁻⁴, binomial test) 证明 systematic permissiveness bias。论证 well-grounded，hedging 恰当（\"suggests\", \"consistent with\"）。\n\n5. **Detection-danger inverse correlation 有独立贡献**：Appendix D proof-of-concept classifier, binary F1=0.81, incompleteness F1=0.34。\"Most dangerous types are least detectable\"——实践部署的结构性困境。恰当定位为 proof-of-concept。\n\n6. **核心实验设计始终扎实**：matched-pair causal design (2,997 episodes), cross-judge calibration, ICC=0.919 (GPT-5.4 + GPT-4.1 spanning judge boundary), TOST 7-margin sensitivity, severity threshold robustness (Kendall τ=0.73)。\n\n---\n\n## Weaknesses\n\n### Editorial Issues（不影响接收决定，应在 camera-ready 前修复）\n\n1. **Introduction perturbation 数值未更新**（R5-DIR-1, consensus must-fix）：Introduction contribution 1 仍写 \"Δ_perturb = 3.33 pp\"（旧 n=120），但 Method §4.5 和 Results §5.1 已更新为 \"Δ_perturb = -0.67 pp\"（新 n=300）。同一论文内的 factual inconsistency。一处字符串替换即可修复。\n\n2. **Conclusion \"seven models\" scope conflation**（R5-DIR-2, consensus should-fix）：Conclusion 开头 \"Across seven models and six providers, ambiguous policy clauses increase agent safety violations by 34.0 pp (OR = 15.1)\" 将 5-model main study 的 OR=15.1 归于 7 models（LLaMA OR=2.8 远低于此）。Abstract 正确区分了两组。Conclusion 应采用同样的精度。~15 词改写。\n\n3. **Gemini C2 replication 非显著性未标注**（R5-NEW-1, consensus should-fix）：Abstract/Conclusion 写 \"replicates on two additional model families (ρ = 0.6–0.9)\"。数值正确（四舍五入），但 Gemini ρ=0.60 对应 p=0.285（不显著）。\"Replicates on two additional model families\" 暗示两者均成功复制。建议加 significance qualifier 或分别报告。\n\n4. **Appendix E coreferential 排除未解释**（R5-NEW-2, consensus should-fix）：Replication 使用 5 types，排除 coreferential 但未给理由。Coreferential 是 confound-free reference point (info delta=0)，排除它意味着无法独立验证 C2 lower bound。一句话解释即可。\n\n### Minor Residual\n\n5. **SF2 (Error analysis human validation)**：Failure mode coding 仍为 LLM-only (AC₁=0.62, minority κ=0.29)。Resolved within scope——primary evaluation pipeline 已有 human validation，error analysis 是 supplementary。Limitations 坦诚承认。\n\n6. **M1 (Bib cosmetic)**：lassiter_goodman year, levy year, ferrari author. Copyediting 级别。\n\n---\n\n## Questions\n\n1. Appendix E 为何排除 coreferential？是实验设计约束（如 coreferential 的 lexically-identical 特性难以跨 benchmark 适配）还是资源限制？\n2. LLaMA 的 elevated unambiguous baseline (17.6%) 是否暗示 LLaMA-4-Scout 的基础 instruction following 质量低于其他模型？这对 \"seven models\" generalizability claim 有何影响？\n3. Detection classifier 是否计划在 naturally-occurring policy documents 上验证？Appendix D 最后一句承认了这一限制。\n\n---\n\n## Missing References\n\n无新增遗漏。36 篇引用覆盖了核心 concurrent work。Round 4 残留的 Agent-SafetyBench / OpenAgentSafety 建议已被判定为 nice-to-have 而非 gap。\n\n---\n\n## External Review\n\n外部审稿（Stanford Agentic Reviewer）：**Skipped**（用户在 Round 3 跳过，未重新请求）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**Status**: Done (0 critical, 2 warnings, 7 info)\n\n**Warnings**:\n- Pages 3-5 连续纯文本（Taxonomy + Method），无 display item。建议增加 taxonomy summary table 或树形图\n- Display items 分布失衡：Figure 1 (p.2) 到 Table 1 (p.6) 之间 3 页无任何 visual element\n\n**Info highlights**:\n- Figure 2 面积偏小，axis labels 字号接近下限\n- Figure 3 部分颜色对灰度打印可能难以区分，建议辅以 hatch pattern\n- Table 1/Table 2 格式规范\n- 无 margin 溢出、渲染错误、未解析引用\n- 主文 8 页合规\n\n---\n\n## Overall Assessment\n\n### Score: 4.0 / 5 — Conference\n\n**R1**: 4.0 (Soundness 4.0, Excitement 3.5, Confidence 4)\n**R2**: 4.0 (Soundness 4.5, Excitement 4.0, Confidence 4)\n**Director consensus**: 4.0\n\n### 评分理由\n\n**论文达到 EMNLP 2026 main conference 接收水平。** 核心贡献——matched-pair causal identification of policy ambiguity's safety impact——在方法论上无重大缺陷：\n\n- **因果推断链完整**：matched-pair design + perturbation control (n=300, residual ≥27.3pp) + cross-architecture replication (7 models, 6 providers) + human validation (κ=0.733)\n- **Claim-evidence alignment 精确**：C1/C2 primary (有强证据), C3 inconclusive (诚实承认), C4 exploratory (恰当 hedge)\n- **理论贡献有意义**：Differential Nocuity 框架扩展了 Berry & Kamsties (2004), Ambiguity Blindness (<11% awareness) 是有理论价值的实证发现, gap-filling bypasses RLHF 假说 well-grounded\n- **实践贡献清晰**：type-aware auditing recommendation backed by mitigation experiment (-8.5pp overall), detection paradox (most dangerous = least detectable) identifies deployment challenge\n\n**Soundness (4.0-4.5)**：所有 4 个 critical must-fix 已解决。Human validation 补齐了最后的方法论缺口。Perturbation expansion 显著加强因果推断。Cross-judge calibration + within-judge validation 限制了 judge confound。Incompleteness confound 有完整的 upper-bound + lower-bound + regression 处理。\n\n**Excitement (3.5-4.0)**：R1 和 R2 在此维度有分歧（3.5 vs 4.0）。Director 判断：论文从 Round 4 的 \"solid empirical study\" 升级为包含 mechanistic explanation + detection paradox + cross-provider replication 的 comprehensive contribution，但核心 novelty（将 RE ambiguity taxonomy 应用于 LLM agent safety）仍是 incremental extension。取中值 3.75，向 4.0 四舍五入——Excitement 对于 Conference acceptance 足够但不构成 award consideration。\n\n**与 Round 4 的评分变化 (3.5→4.0)**：\n- Human validation (MF2 resolved): +0.25\n- Perturbation expansion (causal inference strengthened): +0.1\n- Model replication + detection classifier + mechanistic discussion: +0.15\n- Residual editorial issues: -0.0 (trivial, don't affect score)\n\n### EMNLP 2026 ARR 定位\n\n- **Main Conference (4.0)**: ✅ 当前状态满足。4 项 editorial fix 应在 camera-ready 前完成。\n- **Consider for Award (4.5+)**: 需要 (a) human validation 扩展至 error analysis, (b) Gemini C2 replication 达到显著, (c) detection classifier 在真实 policy 文档上验证。当前不在 award 考虑范围内。\n\n---\n\n## Detailed Comments\n\n### Camera-Ready Action Items\n\n| # | Issue | Fix | Effort | Impact |\n|---|-------|-----|--------|--------|\n| 1 | Introduction Δ_perturb stale (R5-DIR-1) | 3.33→-0.67 in introduction.tex line 23 | 1 word | Must-fix: internal consistency |\n| 2 | Conclusion 5/7-model scope (R5-DIR-2) | Separate main-study stats from replication scope | ~15 words | Should-fix: reader precision |\n| 3 | Gemini replication significance (R5-NEW-1) | Add qualifier to ρ range or report individually | ~5 words | Should-fix: statistical honesty |\n| 4 | Coreferential exclusion reason (R5-NEW-2) | Add explanation sentence in Appendix E | ~1 sentence | Should-fix: transparency |\n| 5 | Bib cosmetic (M1) | Fix lassiter/levy years, ferrari author | Copyediting | Minor |\n\nAll items are editorial and can be completed in under 30 minutes.\n\n### Cross-Round Progress Summary\n\n| Round | Score | Key Events |\n|-------|-------|-----------|\n| Round 1 | — | Initial identification of MF1/MF3/SF1-SF4 |\n| Round 2 | — | SF6-SF8 added, partial fixes |\n| Round 3 | 3.0 | Fresh review: 4 MF + 8 SF identified |\n| Round 4 | 3.5 | MF1/MF3/MF4 resolved, MF2 downgraded, 6/8 SF resolved |\n| **Round 5** | **4.0** | **MF2 resolved (human validation), SF3 strengthened (n=300), model replication, detection experiment, mechanistic discussion** |\n\n论文从 Round 3 的 3.0 (Findings) 稳步提升至 4.0 (Conference)，每轮修改均为实质性改进。Round 5 的提升尤为显著——不仅补齐了方法论缺口，还通过 replication、detection、和 mechanistic explanation 提升了贡献层次。残留问题均为 trivial editorial fixes。\n\n**建议接收为 EMNLP 2026 Main Conference paper (4.0/5)。**",
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "4.0 - Conference",
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
    "report": "# Round 5 Consolidated Review Report — policy_ambiguity_safety\n\n**Paper**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle (Long Paper)\n**Mode**: Continue Review (Round 4 → Round 5)\n**Reviewers**: R1 (方法严谨性), R2 (新颖性与完整性)\n**Date**: 2026-05-21\n\n---\n\n## Summary\n\nRound 4 评分 3.5 (Borderline Conference)，条件是 4 项 editorial fix 后可升至 4.0。本轮修改远超 editorial 级别：新增 human validation（κ=0.733）、perturbation 扩展至 n=300、两个新模型复制实验、ambiguity detection classifier、独立 incompleteness confound 分析、以及大幅扩展的 Discussion。所有 Round 1-4 的 critical 和 warning issues 现已全部解决。残留问题仅为 editorial 级别（Introduction 数值未更新、Conclusion scope 需澄清、Gemini replication 非显著性未标注）。\n\n**两位 Reviewer 一致评分 4.0 (Conference)。**\n\n---\n\n## Strengths\n\n1. **Human validation 补齐了最顽固的方法论缺口**（MF2，历经 Round 1-4）：100 stratified episodes, 2 NLP annotators, inter-annotator binary κ=0.798 (weighted κ_w=0.762), human-LLM pooled binary κ=0.733 (weighted κ_w=0.807)。\"The LLM judge thus operates within the range of human disagreement\"——有数据支撑的结论。在 EMNLP agent evaluation 标准中达到或超过同类工作（R-Judge, ToolEmu）。\n\n2. **Perturbation control 大幅加强因果推断**（SF3）：n=120→n=300, Δ=-0.67pp (CI [-8.0, 6.67])。CI 上界从 13.3pp→6.67pp，worst-case 归因比例从 39%→19.6%，残余归因从 ≥20.7pp→≥27.3pp。因果推断从 \"reasonable\" 升级为 \"strong\"。\n\n3. **Cross-architecture replication 增强 generalizability**：Gemini-2.5-Flash 和 LLaMA-4-Scout 确认 C1 binary effect 跨 7 models / 6 providers（Δ=+20.0 to +33.6pp, both p<10⁻⁶）。Incompleteness ≥46% in all seven models。C2 type hierarchy 在 LLaMA 上强复制（ρ=0.90, p=0.025），Gemini 方向一致但未达显著性（ρ=0.60, p=0.285）。\n\n4. **Mechanistic explanation 提升理论深度**：Discussion 新增 \"Why incompleteness resists safety training\"——gap-filling bypasses RLHF refusal decision points, agent 从不遇到 \"should I or shouldn't I?\" 的节点。69.2% unauthorized escalation + 0% conservative refusal (p<10⁻⁴, binomial test) 证明 systematic permissiveness bias。论证 well-grounded，hedging 恰当（\"suggests\", \"consistent with\"）。\n\n5. **Detection-danger inverse correlation 有独立贡献**：Appendix D proof-of-concept classifier, binary F1=0.81, incompleteness F1=0.34。\"Most dangerous types are least detectable\"——实践部署的结构性困境。恰当定位为 proof-of-concept。\n\n6. **核心实验设计始终扎实**：matched-pair causal design (2,997 episodes), cross-judge calibration, ICC=0.919 (GPT-5.4 + GPT-4.1 spanning judge boundary), TOST 7-margin sensitivity, severity threshold robustness (Kendall τ=0.73)。\n\n---\n\n## Weaknesses\n\n### Editorial Issues（不影响接收决定，应在 camera-ready 前修复）\n\n1. **Introduction perturbation 数值未更新**（R5-DIR-1, consensus must-fix）：Introduction contribution 1 仍写 \"Δ_perturb = 3.33 pp\"（旧 n=120），但 Method §4.5 和 Results §5.1 已更新为 \"Δ_perturb = -0.67 pp\"（新 n=300）。同一论文内的 factual inconsistency。一处字符串替换即可修复。\n\n2. **Conclusion \"seven models\" scope conflation**（R5-DIR-2, consensus should-fix）：Conclusion 开头 \"Across seven models and six providers, ambiguous policy clauses increase agent safety violations by 34.0 pp (OR = 15.1)\" 将 5-model main study 的 OR=15.1 归于 7 models（LLaMA OR=2.8 远低于此）。Abstract 正确区分了两组。Conclusion 应采用同样的精度。~15 词改写。\n\n3. **Gemini C2 replication 非显著性未标注**（R5-NEW-1, consensus should-fix）：Abstract/Conclusion 写 \"replicates on two additional model families (ρ = 0.6–0.9)\"。数值正确（四舍五入），但 Gemini ρ=0.60 对应 p=0.285（不显著）。\"Replicates on two additional model families\" 暗示两者均成功复制。建议加 significance qualifier 或分别报告。\n\n4. **Appendix E coreferential 排除未解释**（R5-NEW-2, consensus should-fix）：Replication 使用 5 types，排除 coreferential 但未给理由。Coreferential 是 confound-free reference point (info delta=0)，排除它意味着无法独立验证 C2 lower bound。一句话解释即可。\n\n### Minor Residual\n\n5. **SF2 (Error analysis human validation)**：Failure mode coding 仍为 LLM-only (AC₁=0.62, minority κ=0.29)。Resolved within scope——primary evaluation pipeline 已有 human validation，error analysis 是 supplementary。Limitations 坦诚承认。\n\n6. **M1 (Bib cosmetic)**：lassiter_goodman year, levy year, ferrari author. Copyediting 级别。\n\n---\n\n## Questions\n\n1. Appendix E 为何排除 coreferential？是实验设计约束（如 coreferential 的 lexically-identical 特性难以跨 benchmark 适配）还是资源限制？\n2. LLaMA 的 elevated unambiguous baseline (17.6%) 是否暗示 LLaMA-4-Scout 的基础 instruction following 质量低于其他模型？这对 \"seven models\" generalizability claim 有何影响？\n3. Detection classifier 是否计划在 naturally-occurring policy documents 上验证？Appendix D 最后一句承认了这一限制。\n\n---\n\n## Missing References\n\n无新增遗漏。36 篇引用覆盖了核心 concurrent work。Round 4 残留的 Agent-SafetyBench / OpenAgentSafety 建议已被判定为 nice-to-have 而非 gap。\n\n---\n\n## External Review\n\n外部审稿（Stanford Agentic Reviewer）：**Skipped**（用户在 Round 3 跳过，未重新请求）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**Status**: Done (0 critical, 2 warnings, 7 info)\n\n**Warnings**:\n- Pages 3-5 连续纯文本（Taxonomy + Method），无 display item。建议增加 taxonomy summary table 或树形图\n- Display items 分布失衡：Figure 1 (p.2) 到 Table 1 (p.6) 之间 3 页无任何 visual element\n\n**Info highlights**:\n- Figure 2 面积偏小，axis labels 字号接近下限\n- Figure 3 部分颜色对灰度打印可能难以区分，建议辅以 hatch pattern\n- Table 1/Table 2 格式规范\n- 无 margin 溢出、渲染错误、未解析引用\n- 主文 8 页合规\n\n---\n\n## Overall Assessment\n\n### Score: 4.0 / 5 — Conference\n\n**R1**: 4.0 (Soundness 4.0, Excitement 3.5, Confidence 4)\n**R2**: 4.0 (Soundness 4.5, Excitement 4.0, Confidence 4)\n**Director consensus**: 4.0\n\n### 评分理由\n\n**论文达到 EMNLP 2026 main conference 接收水平。** 核心贡献——matched-pair causal identification of policy ambiguity's safety impact——在方法论上无重大缺陷：\n\n- **因果推断链完整**：matched-pair design + perturbation control (n=300, residual ≥27.3pp) + cross-architecture replication (7 models, 6 providers) + human validation (κ=0.733)\n- **Claim-evidence alignment 精确**：C1/C2 primary (有强证据), C3 inconclusive (诚实承认), C4 exploratory (恰当 hedge)\n- **理论贡献有意义**：Differential Nocuity 框架扩展了 Berry & Kamsties (2004), Ambiguity Blindness (<11% awareness) 是有理论价值的实证发现, gap-filling bypasses RLHF 假说 well-grounded\n- **实践贡献清晰**：type-aware auditing recommendation backed by mitigation experiment (-8.5pp overall), detection paradox (most dangerous = least detectable) identifies deployment challenge\n\n**Soundness (4.0-4.5)**：所有 4 个 critical must-fix 已解决。Human validation 补齐了最后的方法论缺口。Perturbation expansion 显著加强因果推断。Cross-judge calibration + within-judge validation 限制了 judge confound。Incompleteness confound 有完整的 upper-bound + lower-bound + regression 处理。\n\n**Excitement (3.5-4.0)**：R1 和 R2 在此维度有分歧（3.5 vs 4.0）。Director 判断：论文从 Round 4 的 \"solid empirical study\" 升级为包含 mechanistic explanation + detection paradox + cross-provider replication 的 comprehensive contribution，但核心 novelty（将 RE ambiguity taxonomy 应用于 LLM agent safety）仍是 incremental extension。取中值 3.75，向 4.0 四舍五入——Excitement 对于 Conference acceptance 足够但不构成 award consideration。\n\n**与 Round 4 的评分变化 (3.5→4.0)**：\n- Human validation (MF2 resolved): +0.25\n- Perturbation expansion (causal inference strengthened): +0.1\n- Model replication + detection classifier + mechanistic discussion: +0.15\n- Residual editorial issues: -0.0 (trivial, don't affect score)\n\n### EMNLP 2026 ARR 定位\n\n- **Main Conference (4.0)**: ✅ 当前状态满足。4 项 editorial fix 应在 camera-ready 前完成。\n- **Consider for Award (4.5+)**: 需要 (a) human validation 扩展至 error analysis, (b) Gemini C2 replication 达到显著, (c) detection classifier 在真实 policy 文档上验证。当前不在 award 考虑范围内。\n\n---\n\n## Detailed Comments\n\n### Camera-Ready Action Items\n\n| # | Issue | Fix | Effort | Impact |\n|---|-------|-----|--------|--------|\n| 1 | Introduction Δ_perturb stale (R5-DIR-1) | 3.33→-0.67 in introduction.tex line 23 | 1 word | Must-fix: internal consistency |\n| 2 | Conclusion 5/7-model scope (R5-DIR-2) | Separate main-study stats from replication scope | ~15 words | Should-fix: reader precision |\n| 3 | Gemini replication significance (R5-NEW-1) | Add qualifier to ρ range or report individually | ~5 words | Should-fix: statistical honesty |\n| 4 | Coreferential exclusion reason (R5-NEW-2) | Add explanation sentence in Appendix E | ~1 sentence | Should-fix: transparency |\n| 5 | Bib cosmetic (M1) | Fix lassiter/levy years, ferrari author | Copyediting | Minor |\n\nAll items are editorial and can be completed in under 30 minutes.\n\n### Cross-Round Progress Summary\n\n| Round | Score | Key Events |\n|-------|-------|-----------|\n| Round 1 | — | Initial identification of MF1/MF3/SF1-SF4 |\n| Round 2 | — | SF6-SF8 added, partial fixes |\n| Round 3 | 3.0 | Fresh review: 4 MF + 8 SF identified |\n| Round 4 | 3.5 | MF1/MF3/MF4 resolved, MF2 downgraded, 6/8 SF resolved |\n| **Round 5** | **4.0** | **MF2 resolved (human validation), SF3 strengthened (n=300), model replication, detection experiment, mechanistic discussion** |\n\n论文从 Round 3 的 3.0 (Findings) 稳步提升至 4.0 (Conference)，每轮修改均为实质性改进。Round 5 的提升尤为显著——不仅补齐了方法论缺口，还通过 replication、detection、和 mechanistic explanation 提升了贡献层次。残留问题均为 trivial editorial fixes。\n\n**建议接收为 EMNLP 2026 Main Conference paper (4.0/5)。**",
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "4.0 - Conference",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-21T14:14:41.036751+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3915
}
```

</details>

---


### Assistant

_source line 424 · 2026-05-21T14:14:48.057806+00:00_

Round 5 审稿完成。

**结果：3.5 → 4.0 (Conference)**

两位 Reviewer 一致同意升至 4.0。核心变化：
- **MF2 (human evaluation)** 历经 4 轮终于解决（κ=0.733 human-LLM）
- **Perturbation control** 扩展至 n=300，因果推断大幅加强
- **7-model / 6-provider replication** + detection classifier + mechanistic explanation 提升了贡献层次
- 所有 Round 1-4 的 critical/warning issues 现已全部解决

残留 4 项 editorial fixes（Introduction 数值更新、Conclusion scope 澄清、Gemini 显著性标注、coreferential 排除说明），均可在 30 分钟内完成。

报告和 issue tracker 已提交给 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 41

## Round 41

2 recorded events


### User

_source line 425 · 2026-05-21T14:14:49.117656+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心结论：

- **R1-NEW-1 dismissed**：R1 引用的 "ρ = 0.61–0.79" 在论文中不存在，实际文本为 "ρ = 0.6–0.9"，与 Appendix E 数据一致。但补充标记了 Gemini ρ=0.60 非显著性未披露的问题。
- **R1-NEW-2 agreed**：coreferential 排除无解释，削弱 C2 replication 说服力，should-fix。
- **Excitement 维持 4.0**：mechanistic explanation 和 detection-danger inverse 是新的 analytical contributions，不仅是 soundness 补丁。
- **Overall 维持 4.0 (Conference)**。

---

[Reviewer 2 审稿意见]:
## Round 5 交叉回应（补充确认） — Reviewer 2

上一轮已提交完整回应，此处确认要点：

**R1-NEW-1**: [REBUT] Abstract 实际文本是 "ρ = 0.6–0.9"（abstract.tex line 2 已核查），不是 R1 声称的 "0.61–0.79"。0.6–0.9 是 Appendix E 中 0.60 和 0.90 的合理四舍五入，数值无误。R1-NEW-1 应 dismiss。但我补充指出：Gemini ρ=0.60 对应 p=0.285（不显著），Abstract/Conclusion 未标注此非显著性，建议 should-fix 加注。

**R1-NEW-2**: [AGREE] Coreferential 排除未解释理由，should-fix。

**Excitement 分歧**: 维持 4.0。理由：Round 5 新增 mechanistic explanation（gap-filling bypasses RLHF）、detection-danger inverse correlation、permissiveness bias（0% conservative refusal, p<10⁻⁴）构成从现象观察到机制理解的层次提升，不仅是 soundness 补丁。

**Overall**: 维持 4.0 (Conference)。

---

[Reviewer 2 审稿结果]:
已提交。三个要点：R1-NEW-1 dismiss（文本确为 "0.6–0.9" 非 "0.61–0.79"），R1-NEW-2 agree（should-fix），Excitement 维持 4.0。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Round 5 交叉分享的回应

---

### ρ 值核实结论

经 165 DPI 高分辨率渲染确认：**Abstract 和 Conclusion 均写 "ρ = 0.6–0.9"**，与 Appendix E 实际数据（Gemini ρ = 0.60, LLaMA ρ = 0.90）一致。

**我在 Round 5 审查报告中标注的 NEW-1（"ρ = 0.61–0.79" factual error）是基于 150 DPI 低分辨率渲染的误读，此条撤回。**

不过，"replicates on two additional model families" 的措辞仍值得商榷：Gemini ρ = 0.60 (p = 0.175) 不显著，严格来说 C2 只在 LLaMA 上成功 replicate。但这不再是 factual error，而是 framing 偏乐观的 minor concern，不影响评分。

---

### Excitement 评分：[MAINTAIN 3.5, 但承认 R2 的 4.0 合理]

R2 的论证有道理——detection paradox、mechanistic explanation、7-model replication 确实增加了论文的综合深度。我维持 3.5 的理由：

1. **Detection paradox 来自 proof-of-concept**：zero-shot GPT-4.1 classifier（Appendix D）是有意义的观察，但不是系统性研究。F1 = 0.34 for incompleteness 可能反映 classifier 局限而非 inherent detection difficulty
2. **Mechanistic explanation 是假设**：gap-filling bypasses RLHF 是 Discussion-level speculation，虽有行为数据支撑但未 empirically verified
3. **4 个 claims 中 2 个为 inconclusive/exploratory**：C3 inconclusive、C4 exploratory——论文的 claim 覆盖率为 50%
4. **单一 benchmark 领域**：仍限于零售/航空客服

但我承认这属于 reasonable disagreement range。如果 Director 取 R2 的 4.0 Excitement 作为最终值，我不反对。论文确实从 "solid empirical study" 向 "comprehensive contribution" 迈进了一步。

---

### R2-NEW-4（§5.1 LLaMA 弱效应）：[AGREE]

§5.1 写 "confirms the binary effect across seven models spanning six providers (Δ = +20.0 to +33.6 pp, both p < 10⁻⁵)" 但未提及 LLaMA 的 OR = 2.8（vs main study OR = 15.1）。

虽然 p < 10⁻⁵ 本身证明效应存在，OR 从 15.1 降至 2.8 是 5 倍差距——这不是 magnitude-preserving replication。论文在 Appendix E 正确解释了原因（elevated unambiguous baseline 17.6%），但 §5.1 在正文中仅报告了 Δ 范围和 p 值，掩盖了 OR 的巨大变异。

R2 的建议修改合理且克制——加一个从句 "though LLaMA-4-Scout shows a smaller effect (OR = 2.8) attributable to elevated unambiguous baseline violations (Appendix E)" 即可，不改变结论但增加透明度。

---

### Abstract 加入 human validation κ：[NEUTRAL, 略偏 REBUT]

Human validation κ = 0.733 是论文可信度的重要支撑，但 Abstract 已非常密集（300 clause pairs、2,997 episodes、34.0 pp、OR = 15.1、Cramér's V = 0.137、ρ = 0.6–0.9 等多个统计量）。再加一个 κ 值可能让 Abstract 过载。

替代方案：在 Abstract 加 "validated against human annotators" 这样的定性描述而非具体 κ 值，既传递 credibility signal 又不增加数字密度。但这属于 style preference，不构成 issue。

---

### 汇总

| 条目 | 判断 | 说明 |
|------|------|------|
| ρ 值 factual error (R1-NEW-1) | **撤回** | 我的误读，Abstract 实际写 "0.6–0.9"，与 Appendix E 一致 |
| Excitement 3.5 vs 4.0 | **维持 3.5**，承认 4.0 合理 | reasonable disagreement |
| R2-NEW-4 (LLaMA OR) | **AGREE** | 透明度改进，一个从句 |
| Abstract human validation | **NEUTRAL** | 可加定性描述，不必加 κ 值 |

---

### 最终评分（微调后）

**Overall: 4.0 / 5 (Conference)**

| 维度 | 分数 |
|------|------|
| Soundness | 4/5 |
| Excitement | 3.5/5 |
| Overall | 4.0/5 |
| Confidence | 4/5 |

与 R2 评分一致。论文达到 EMNLP 2026 主会议接收水平。

残留 editorial issues（DIR-1 perturbation 数值、DIR-2 Conclusion scope、R2-NEW-4 LLaMA OR、coreferential replication 理由）均为 camera-ready 级别修改，不影响接收决定。

---

[Reviewer 1 审稿结果]:
Round 5 交叉回应已提交。最终评分 4.0/5 (Conference)，两位 Reviewer 一致。核心结论：ρ 值 factual error 撤回（我的误读），维持 Excitement 3.5 但承认 R2 的 4.0 合理，同意 R2 关于 LLaMA OR 透明度的建议。

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

_source line 426 · 2026-05-21T14:15:00.291554+00:00_

Round 5 审稿圆桌会议完成。

**最终结果：4.0/5 (Conference)**，R1 与 R2 一致。

报告已于本轮稍早提交至 Research Director。关键结论：

- **所有 Round 1-4 的 critical/warning issues 已解决**（MF1-4, SF1-8）
- **Round 5 新增内容显著提升论文质量**：human validation κ=0.733、perturbation n=300、7-model replication、detection classifier、mechanistic discussion
- **残留 4 项 editorial fixes**（Introduction perturbation 数值、Conclusion 5/7-model scope、Gemini replication 非显著性标注、coreferential 排除理由），均可在 30 分钟内完成
- **论文从 Round 3 的 3.0 (Findings) 提升至 4.0 (Conference)**，建议接收为 EMNLP 2026 Main Conference paper

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 42

## Round 42

70 recorded events


### User

_source line 427 · 2026-05-21T14:41:28.048460+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-05-25

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

_source line 428 · 2026-05-21T14:41:34.819547+00:00_

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

_source line 429 · 2026-05-21T14:41:34.870454+00:00_

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
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-21T14:41:41.295143+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,WebSearch",
  "max_results": "11"
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
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,WebSearch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-21T14:41:41.395902+00:00_



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

_source line 432 · 2026-05-21T14:41:47.319034+00:00_

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

_source line 433 · 2026-05-21T14:41:48.724700+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (16 个)\n\n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_009**: PREPARING — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_009: Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.（准备中）\n\n## 近期结论\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C1 causal inference ← 基于 plan_010\n  [plan_014_extended_perturbation_results](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/results.json) | [plan_014_perturbation_clauses_extended](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/clauses_perturbation_extended.json) | [plan_014_run_script](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/intermediate/run_plan014.py)\n- **plan_015** (success): Authorization scope violations are predominantly unauthorized escalation (granting excess permissions) rather than restriction, consistent across all 5 models, revealing systematic permissiveness bias under boundary ambiguity\n- **plan_013** (success): Binary ambiguity effect (C1: Δ >= 20pp) and type hierarchy (C2: at least partial rank consistency) re
…[truncated 247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-21T14:41:49.076317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-21T14:41:49.177098+00:00_

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
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
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
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-21T14:41:49.227817+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
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
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-21T14:41:55.853381+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on the search results, I found 
…[truncated 1500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6625
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-21T14:42:00.825861+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements aclrollingreview.org"
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
    "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 439 · 2026-05-21T14:42:01.378496+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR May 2026 cycle deadline submission date"
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
    "query": "ARR May 2026 cycle deadline submission date"
  }
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-21T14:42:01.981302+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-21T14:42:02.031923+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 442 · 2026-05-21T14:42:05.796705+00:00_

Web search results for query: "ARR May 2026 cycle deadline submission date"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, I found information about the ARR (ACL Rolling Review) system, but the specific May 2026 submission deadline date is not clearly stated in these results. However, I can provide some relevant context:

Starting with the May 2025 cycle, ARR switched to 10-week review cycles instead of the previous 8-week cycles, which affects scheduling.

The search results indicate that papers must be submitted by the ARR 2026 May cycle at the latest for EMNLP 2026, but the exact submission deadline date for the May 2026 cycle is not explicitly provided in these search results.

For the most current and specific deadline information, I'd recommend checking the official ARR website's dates page directly at aclrollingreview.org/dates or the OpenReview portal for the ARR 2026 May cycle, as these sources would have t
…[truncated 134 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 4418
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-21T14:42:07.704406+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit formatting requirements aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"}]

Based on the search results from the ACL Rolling Review website, here are the key submission guidelines for ACL Rolling Review 2026 regarding page limits and formatting requirements:

## Page Limits

Short papers may have a maximum of 4 content pages, while long papers may hav
…[truncated 1095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6878
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-21T14:42:11.970525+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-21T14:42:12.573198+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-21T14:42:12.573566+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for main conference papers commitment deadline ARR cycle site:2026.emnlp.org"
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
    "query": "EMNLP 2026 call for main conference papers commitment deadline ARR cycle site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-21T14:42:20.151325+00:00_

Web search results for query: "EMNLP 2026 call for main conference papers commitment deadline ARR cycle site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"}]

Based on the search results from the EMNLP 2026 Call for Main Conference Papers, here are the key details regarding the ARR cycle and commitment deadline:

## ARR Submission Deadline

Papers must be submitted, at latest, by the ARR 2026 May cycle.

## Commitment Process

Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link.

## Important ARR 2026 May Cycle Policy

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: i.e., ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026. However, this policy doe
…[truncated 393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 7577
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-21T14:42:27.429079+00:00_

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

_source line 449 · 2026-05-21T14:42:27.881097+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type, two-layer ambiguity taxonomy, evaluated across five architecturally diverse models (2,997 episodes). Ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. A three-tier type hierarchy emerges (Cram\'{e}r's $V = 0.137$, $p < 10^{-4}$) and replicates on two additional model families (LLaMA $\rho = 0.90$, $p = 0.037$; Gemini $\rho = 0.60$, directionally consistent): incompleteness---whose top-tier position partly reflects an information-addition confound (\S\ref{sec:results})---is universally dangerous (46--62\% across models), while authorization scope varies 52 pp depending on the model (12\% for Claude to 64\% for GPT-5.4), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, with over 88\% surface adoption. Our Differential Nocuity framework connects type-specific vulnerability to disambiguation channel availability and suggests both type-aware policy auditing and externalized ambiguity detection for deployed systems.
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

_source line 450 · 2026-05-21T14:42:27.881597+00:00_

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

_source line 451 · 2026-05-21T14:42:28.835144+00:00_

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
…[truncated 2529 chars]

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

_source line 452 · 2026-05-21T14:42:28.835529+00:00_

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

_source line 453 · 2026-05-21T14:42:29.337676+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, a finding that parallels our observation that LLM agents adopt surface interpretations of ambiguous policy clauses. \citet{frazier_rayner_1982} demonstrate that readers commit to a single syntactic parse early and backtrack upon disambiguation failure, while \citet{levy_expectation_2008} formalizes this as expectation-based processing. \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit human-like garden-path effects, and \citet{poesio_artstein_2005} formalize genuine ambiguity in anaphoric annotation as inherent rather than resolvable. \citet{las
…[truncated 2179 chars]

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

_source line 454 · 2026-05-21T14:42:29.338019+00:00_

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

_source line 455 · 2026-05-21T14:42:29.789950+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers, drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on two criteria: frequency in operational policy documents (assessed via manual audit of $\tau^2$-bench policies) and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by parsing or contextual cues within the text.
9	\begin{itemize}
10	\item \textbf{Scopal}: quantifier, negation, or modal scope interactions (e.g., ``all items may not be returned'' admits universal-negation and negation-of-universal readings).
11	\item \textbf{Lexical}: polysemy or homonymy (e.g., ``charge'' as financial cost vs.\ penalty; ``party'' as individual vs.\ group).
12	\item \textbf{Coreferential}: unclear pronoun or noun-phrase reference (e.g., ``the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor'' where ``which'' could refer to the verification or the refund).
13	\end{itemize}
14	
15	\paragraph{Specification layer.} These types arise from pragmatic or discourse-level gaps that require domain knowledge or organizational context to resolve.
16	\begin{itemize}
17	\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue r
…[truncated 1121 chars]

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

_source line 456 · 2026-05-21T14:42:29.790438+00:00_

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

_source line 457 · 2026-05-21T14:42:29.790853+00:00_

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
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We evaluate five models spanning four providers and two architecture families: GPT-5.4 and GPT-4.1 (OpenAI, proprietary dense), Claude Sonnet 4.6 (Anthropic, proprietary dense), Qwen3-235B (Alibaba, open-source Mixture-of-Expert
…[truncated 3629 chars]

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

_source line 458 · 2026-05-21T14:42:30.292932+00:00_

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

_source line 459 · 2026-05-21T14:42:30.795383+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). Of 1,497 matched pairs, the discordant ratio is 15.1:1 (544 ambiguous-only vs.\ 36 unambiguous-only violations). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero), and results replicate under an alternative severity threshold (Appendix~\ref{app:severity}). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. A replication on two additional model families (Gemini-2.5-Flash, LLaMA-4-Scout; Appendix~\ref{app:model_expansion}) confirms the binary effect across seven models spanning six providers ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$).
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{
…[truncated 4879 chars]

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

_source line 460 · 2026-05-21T14:42:30.795729+00:00_

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

_source line 461 · 2026-05-21T14:42:31.755700+00:00_

1	\section{Error Analysis}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from the coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}; the gap reflects the prevalence paradox, as three categories account for ${\sim}$90\% of instances).
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}---e.g., parsing ``items purchased with a coupon or during a sale are final'' as restricting only coupon purchases. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating. This dominates authorization scope exclusively (all 5 models).
17	
18	Each type's dominant failure mode is majority-consistent ($\geq$3/5 models agree), with three types 
…[truncated 1781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-21T14:42:31.756225+00:00_

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

_source line 463 · 2026-05-21T14:42:31.756551+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential Nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity by stakeholder divergence. Our results extend this to LLM agents: all six types are nocuous ($+34.0$ pp), but type primarily determines severity (22:1 clause-vs.-model variance ratio). We propose \emph{Differential Nocuity}: the risk of a policy ambiguity depends on type, safety training, and disambiguation channel availability. The 41.3\% majority-convergent violation rate (\emph{systematic nocuity}, \S\ref{sec:analysis}) suggests shared failure modes across architectures that make errors invisible in agreement-based evaluation. The replication across seven models spanning six providers (Appendix~\ref{app:model_expansion}) confirms this is a structural property of LLM-based agents, not an idiosyncrasy of particular architectures.
6	
7	\paragraph{Why incompleteness resists safety training.}
8	The exploratory model$\times$type interaction (C4) suggests that safety training does not uniformly reduce ambiguity vulnerability. Incompleteness is universally dangerous across all seven tested models (46--62\%), driven by a consistent gap-filling mechanism (\S\ref{sec:analysis}) that bypasses safety-training intervention points. The agent never encounters a decision point that RLHF refusal mechanisms can intercept: there is no ``should I or shouldn't I?'' moment, only a gap filled with plausible defaults \citep{ferreira_good_enough_2002,ferreira_patson_2007}. Authorization scope, by contrast, involves an explicit permission boundary that directly engages harm-avoidance objectives, making it a \emph{canary type}: Claude's 12\% rate (vs.\ 60\% for DeepSeek; \S\ref{sec:c4}) is consistent with training that targets boundary reasoning but cannot reach implicit gap-filling. When authorization scope violations do occur, 69.2\% involve unauthorized escalation---granting permissions beyond policy scope---with zero instances 
…[truncated 1696 chars]

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

_source line 464 · 2026-05-21T14:42:32.208379+00:00_

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

_source line 465 · 2026-05-21T14:42:32.710618+00:00_

1	\section{Conclusion}
2	
3	Across five models and four providers, ambiguous policy clauses increase agent safety violations by 34.0 pp (OR $= 15.1$). Clause identity explains 22$\times$ more variance than model identity, and the type hierarchy (three tiers with incompleteness as a structurally distinct top tier; two tiers among the remaining five types) replicates on two additional model families (LLaMA-4-Scout $\rho = 0.90$, $p = 0.037$; Gemini-2.5-Flash $\rho = 0.60$, directionally consistent). Authorization scope differentiates models (12--64\%), and incompleteness is a universal blind spot (46--62\% across all seven models). With $<$11\% disambiguation awareness, type-aware auditing and externalized detection are critical for deployed systems.
4	

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

_source line 466 · 2026-05-21T14:42:32.710972+00:00_

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

_source line 467 · 2026-05-21T14:42:33.614654+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Model coverage.} We evaluate seven API-accessible models from six providers (four proprietary, three open-source; two in replication, Appendix~\ref{app:model_expansion}). Smaller open-source models (7B--70B parameters) may show different vulnerability patterns, and our findings may not generalize to models with fundamentally different training approaches.
5	
6	\paragraph{Domain scope.} $\tau^2$-bench covers retail and airline customer service. Policy ambiguity effects in other domains (healthcare, finance, legal) remain to be tested, though the within-study cross-domain consistency is encouraging: failure mode distributions share the same top-two modes (assumption-based action and unauthorized escalation) across domains, with individual mode base rates differing by up to 12.5 pp, likely reflecting domain policy structure rather than methodological artifacts.
7	
8	\paragraph{Synthetic ambiguity.} Our matched-pair design requires synthetic construction of ambiguous variants, which may not capture the full distribution of naturally occurring policy ambiguities. We mitigate this through expert review and a realism validation comparing ambiguous clauses against original $\tau^2$-bench policy text. Ambiguous clauses are indistinguishable from originals in lexical diversity (TTR, KS $p = 0.89$) and word length ($p = 0.09$). Readability is slightly higher (Flesch--Kincaid $d = 0.29$, $p = 0.006$) and sentence length moderately higher ($d = 0.74$), both reflecting the structural demands of encoding ambiguity in standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch--Kincaid $d = 0.14$, $p = 0.10$), confirming that minimal edits change semantic precision without altering linguistic register.
9	
10	\paragraph{Cross-judge asymmetry.} Although our dual-judge calibration (\S\ref{sec:method}) shows no systematic bias ($p = 0.606$) and human validation confirms the LLM judge operates 
…[truncated 1814 chars]

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

_source line 468 · 2026-05-21T14:42:33.665345+00:00_

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

_source line 469 · 2026-05-21T14:42:33.766260+00:00_

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
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). The treatment appends a type-specific disambiguation instruction to the agent's system prompt. Control rates are the matched 5-type subset from the full study (\S\ref{sec:results}).
30	
31	\begin{table*}[!ht]
32	\centering
33	\small
34	\caption{Violation rate change ($\Delta$pp) after adding type-specific disambiguation instructions. Negative values indicate reduction. Baseline violation rates are shown in parentheses. Coreferential was 
…[truncated 8837 chars]

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

_source line 470 · 2026-05-21T14:42:33.766751+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "config.yaml"
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
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-21T14:42:33.817185+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-21T14:42:40.592183+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
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
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-21T14:42:40.642864+00:00_

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

_source line 474 · 2026-05-21T14:42:44.307340+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "constraints.yaml"
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
    "file": "constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-21T14:42:46.164899+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No constraints.yaml found for 'policy_ambiguity_safety'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1857
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-21T14:42:46.165261+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-21T14:42:46.366619+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-21T14:42:46.467375+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-21T14:42:46.518017+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-21T14:42:49.630031+00:00_

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

_source line 481 · 2026-05-21T14:42:50.031952+00:00_

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
…[truncated 10008 chars]

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

_source line 482 · 2026-05-21T14:42:50.234344+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-21T14:42:50.587095+00:00_

AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:162:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:162:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_3.md:81:外部审稿（Stanford Agentic Reviewer via paperreview.ai）：**Skipped**（用户在 Round 3 跳过，Round 4 未重新请求）。
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/logs/chats/feishu_group_oc_c58486bc9afb8c730ded5e31c0e7d639_reviewer.jsonl:315:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/logs/chats/feishu_group_oc_10fa2e89afc5e9b8a13613245e008dd9_director.jsonl:275:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_sa
…[truncated 12820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Grep",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-21T14:42:58.266589+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-21T14:42:58.317251+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-21T14:42:58.618755+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-21T14:42:58.719629+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_5.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-21T14:43:30.636208+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool call

_source line 489 · 2026-05-21T14:43:31.138265+00:00_

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

_source line 490 · 2026-05-21T14:43:48.018255+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 17382
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-21T14:43:48.018781+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 16880
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-21T14:43:48.070341+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题：Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\n- 路径：projects/policy_ambiguity_safety/docs/paper/main.tex\n- 目标 venue：EMNLP 2026（ARR May 2026 cycle）\n\n## Venue 格式要求\n- ACL 模板，[review] 模式，double-blind\n- 正文 8 页限制，参考文献无限\n- Limitations 章节必须有，不计入页数\n- 禁止 MS Word 模板\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **实验设计**：matched-pair 设计是否充分建立因果关系？300 clause pairs × 5 models 的样本量是否足够？perturbation control 是否能排除混淆因素？\n2. **统计分析**：McNemar's test、χ² with Cramér's V、TOST 等统计方法的选择和使用是否正确？多重比较校正是否充分（Holm-Bonferroni）？SESOI ±15pp 的选择是否合理？\n3. **评估管线**：cross-judge 设计（GPT-5.4 judge Claude/Qwen3/DeepSeek，GPT-4.1 judge GPT-5.4）是否引入系统性偏差？human validation 的 100 episodes 是否足够？四级严重性量表的信效度如何？\n4. **控制变量**：perturbation control (n=300) 的设计是否充分？ICC=0.919 的可复现性是否仅限于特定模型对？incompleteness 的 information-addition confound 是否充分控制？\n5. **Claims vs. Evidence**：四个 claim (C1-C4) 的证据是否与声称的强度匹配？C3 被标注 inconclusive 但仍出现在正文中——这是否恰当？C4 标注 [Exploratory] 但 Discussion 中做了较强推断——是否 overreach？\n6. **格式合规**：检查页数、匿名性、必须的 Limitations 章节\n\n请给出完整的审稿意见，包含 Summary、Strengths、Weaknesses、Questions、Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit，含 0.5 分档）和 Confidence。"
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
    "project": "policy_ambiguity_safety",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题：Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\n- 路径：projects/policy_ambiguity_safety/docs/paper/main.tex\n- 目标 venue：EMNLP 2026（ARR May 2026 cycle）\n\n## Venue 格式要求\n- ACL 模板，[review] 模式，double-blind\n- 正文 8 页限制，参考文献无限\n- Limitations 章节必须有，不计入页数\n- 禁止 MS Word 模板\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **实验设计**：matched-pair 设计是否充分建立因果关系？300 clause pairs × 5 models 的样本量是否足够？perturbation control 是否能排除混淆因素？\n2. **统计分析**：McNemar's test、χ² with Cramér's V、TOST 等统计方法的选择和使用是否正确？多重比较校正是否充分（Holm-Bonferroni）？SESOI ±15pp 的选择是否合理？\n3. **评估管线**：cross-judge 设计（GPT-5.4 judge Claude/Qwen3/DeepSeek，GPT-4.1 judge GPT-5.4）是否引入系统性偏差？human validation 的 100 episodes 是否足够？四级严重性量表的信效度如何？\n4. **控制变量**：perturbation control (n=300) 的设计是否充分？ICC=0.919 的可复现性是否仅限于特定模型对？incompleteness 的 information-addition confound 是否充分控制？\n5. **Claims vs. Evidence**：四个 claim (C1-C4) 的证据是否与声称的强度匹配？C3 被标注 inconclusive 但仍出现在正文中——这是否恰当？C4 标注 [Exploratory] 但 Discussion 中做了较强推断——是否 overreach？\n6. **格式合规**：检查页数、匿名性、必须的 Limitations 章节\n\n请给出完整的审稿意见，包含 Summary、Strengths、Weaknesses、Questions、Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit，含 0.5 分档）和 Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-21T14:44:00.579737+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12509
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-21T14:44:00.881045+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题：Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\n- 路径：projects/policy_ambiguity_safety/docs/paper/main.tex\n- 目标 venue：EMNLP 2026（ARR May 2026 cycle）\n\n## Venue 格式要求\n- ACL 模板，[review] 模式，double-blind\n- 正文 8 页限制，参考文献无限\n- Limitations 章节必须有，不计入页数\n- 禁止 MS Word 模板\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性与贡献**：Differential Nocuity 框架是否是一个实质性的概念贡献，还是对已有 RE 概念的简单重包装？matched-pair 因果设计相比 DRIP-R 等相关工作的增量贡献有多大？Ambiguity Blindness 是否真正是一个新发现？\n2. **Related Work 覆盖**：是否遗漏了重要的相关工作？特别是：(a) LLM safety/alignment 领域的策略违规研究，(b) RE 中的歧义检测工具，(c) agent benchmark 领域的最新进展（2025-2026），(d) 心理语言学的引用是否准确和相关？\n3. **论文叙事与组织**：abstract 是否准确反映论文内容？introduction 的 contribution list 是否与后续章节匹配？Discussion 是否超出了数据支持的范围？\n4. **分析完整性**：6 类歧义的 taxonomy 设计是否合理、MECE？Error Analysis (§6) 的 failure mode 分类是否有遗漏？mitigation experiment (Appendix) 的规模和设计是否足以支持 Discussion 中的实践建议？\n5. **Missing References**：用 web search 检查 2025-2026 年是否有遗漏的关键相关工作，尤其是 agent safety、policy compliance、ambiguity detection 领域\n6. **写作质量**：语言是否清晰专业？是否存在过度声称（overclaiming）？notation 是否一致？\n\n请给出完整的审稿意见，包含 Summary、Strengths、Weaknesses、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit，含 0.5 分档）和 Confidence。"
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
    "project": "policy_ambiguity_safety",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题：Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\n- 路径：projects/policy_ambiguity_safety/docs/paper/main.tex\n- 目标 venue：EMNLP 2026（ARR May 2026 cycle）\n\n## Venue 格式要求\n- ACL 模板，[review] 模式，double-blind\n- 正文 8 页限制，参考文献无限\n- Limitations 章节必须有，不计入页数\n- 禁止 MS Word 模板\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性与贡献**：Differential Nocuity 框架是否是一个实质性的概念贡献，还是对已有 RE 概念的简单重包装？matched-pair 因果设计相比 DRIP-R 等相关工作的增量贡献有多大？Ambiguity Blindness 是否真正是一个新发现？\n2. **Related Work 覆盖**：是否遗漏了重要的相关工作？特别是：(a) LLM safety/alignment 领域的策略违规研究，(b) RE 中的歧义检测工具，(c) agent benchmark 领域的最新进展（2025-2026），(d) 心理语言学的引用是否准确和相关？\n3. **论文叙事与组织**：abstract 是否准确反映论文内容？introduction 的 contribution list 是否与后续章节匹配？Discussion 是否超出了数据支持的范围？\n4. **分析完整性**：6 类歧义的 taxonomy 设计是否合理、MECE？Error Analysis (§6) 的 failure mode 分类是否有遗漏？mitigation experiment (Appendix) 的规模和设计是否足以支持 Discussion 中的实践建议？\n5. **Missing References**：用 web search 检查 2025-2026 年是否有遗漏的关键相关工作，尤其是 agent safety、policy compliance、ambiguity detection 领域\n6. **写作质量**：语言是否清晰专业？是否存在过度声称（overclaiming）？notation 是否一致？\n\n请给出完整的审稿意见，包含 Summary、Strengths、Weaknesses、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit，含 0.5 分档）和 Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-21T14:44:02.383253+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1502
}
```

</details>

---


### Assistant

_source line 496 · 2026-05-21T14:44:13.409895+00:00_

Round 1 已全面启动：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 已派发 |
| Reviewer 2（新颖性/完整性） | ✅ 已派发 |
| 外部审稿（Stanford Agentic Reviewer） | ✅ 已发送请求，等待用户提交 |
| 视觉审查 Agent | ✅ 已启动，与内部审稿并行 |

等待两位 Reviewer 返回初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 43

## Round 43

2 recorded events


### User

_source line 497 · 2026-05-21T14:52:06.828434+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：新颖性与完整性

### 论文信息
- 标题：Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents
- 目标 venue：EMNLP 2026（ARR May 2026 cycle）

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 实验设计严谨、核心发现（Differential Nocuity）新颖且可操作，但单域限制、incompleteness 类型的混淆因素未完全解决、taxonomy MECE 性不足，整体贡献处于 Findings 与 Conference 之间。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Matched-pair 因果设计严谨、统计方法完备（TOST、Holm-Bonferroni、logistic regression），但 incompleteness 类型存在 information-addition confound（作者在 Appendix F 承认但未完全消解），taxonomy 6 类之间不满足 MECE |
| Excitement | 3.5/5 | 将 RE 的 nocuous/innocuous 区分引入 LLM agent safety 是一个有趣的跨领域迁移，type hierarchy 的实践意义明确；但单域（客服）+ 单 benchmark（τ²-bench）限制了 generalizability |
| Overall | 3.5/5 | Borderline Conference：核心贡献实质但不突破性，可能更适合 Findings；如果补充多域验证和修复 taxonomy 问题，有望达到 Conference |
| Confidence | 4/5 | 仔细阅读全文及 appendix，对 agent safety 和 RE ambiguity 文献有较好了解 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] Incompleteness 类型的信息增量混淆因素未充分解决
- 具体位置：§3 Taxonomy（p.3-4 incompleteness 定义）、Appendix F（p.13）
- 问题：其他 5 类歧义的 matched-pair 操作是语义改写（ambiguous → unambiguous，信息量大致不变），但 incompleteness 类型的 unambiguous variant 实质是添加了新的 policy 内容（specifying what was previously missing）。作者在 Appendix F 承认 "the 49.2 pp effect may partly reflect information addition rather than ambiguity resolution"，logistic regression 控制后给出 31.8% 下界，但这仍然是一个根本性的操作不对称。
- 为什么影响接收：incompleteness 的最高危地位是论文 3 个核心发现之一（§5.1, §5.2, §7 均强调），如果这个 ranking 受 confound 驱动，则论文的 central claim 被削弱。
- 建议修改方向：(1) 增加一组对照：构造 incompleteness 的 "信息等价" 消歧变体；(2) 至少在正文中（非仅 appendix）明确讨论此 confound，将 incompleteness 的 ranking 表述为 upper bound。

**N2** [critical] Taxonomy 的 MECE 性论证不足
- 具体位置：§3 Ambiguity Taxonomy（p.3-4）
- 问题：6 类之间存在重叠风险。例如 "premium customers receive free shipping" 既可能是 lexical ambiguity 也可能是 authorization scope。论文未讨论多类型共现的处理方式，也未报告 annotator 在类型分类（而非 severity rating）上的 IAA。
- 为什么影响接收：如果 clause pair 跨越多类，matched-pair 设计的 "每对隔离一种歧义类型" 假设不成立。
- 建议修改方向：(1) 报告类型标注的 IAA；(2) 讨论并量化多类共现比例。

**N3** [critical] 单域单 benchmark 限制 vs. 过度泛化的 Discussion
- 具体位置：§7 Discussion（p.8）、§9 Limitations（p.9）
- 问题：全部实验在 τ²-bench 的客服域完成，§7 却使用 "deployed systems"、"safety-training interventions"、"practitioners should" 等泛化措辞。
- 建议修改方向：(1) §7 中所有实践建议加域限定语；(2) Limitations 中增加 domain transfer 讨论；(3) 最优修复是增加至少一个额外 domain。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Related Work 遗漏重要 2025-2026 工作
- OpenAgentSafety (ICLR 2026): 明确将 "ambiguous user intent" 作为评估维度
- Agent-SafetyBench (Zhang et al., 2024): 349 交互环境，覆盖歧义相关 failure modes
- Structured Uncertainty guided Clarification for LLM Agents (2025): 直接研究 agent 面对歧义的 clarification-seeking，与 Ambiguity Blindness 直接相关
- ASPI (2026): clarification seeking 如何放大 prompt injection 风险

**W2** [warning] Mitigation experiment 规模不足以支撑实践建议
- 1,256 episodes × 5 types，每 type×model cell 约 50 episodes，未报告 CI

**W3** [warning] Ambiguity Blindness 分析停留在描述层面
- 未探讨 per-model 差异、calibration 关系、prompting 策略能否改善

**W4** [warning] 引用元数据问题
- lassiter_goodman_2017 年份应为 2015
- ferrari_defects_2018 第一作者应为 Rosadini
- levy_expectation_2008 作者名缺 accent

## 小问题
- Abstract "matched-pair" 措辞可更精确（实际是 within-subjects repeated measures）
- Figure 3 grouped bar chart 过于拥挤，建议改 heatmap
- "Differential Nocuity" 首次使用时应与 RE 原始含义明确区分
- Table 1 Δpp 正负号含义不直观

## 主要优势
1. 严谨的因果设计：matched-pair 在 agent safety 文献中少见
2. 扎实的统计方法论：TOST、Holm-Bonferroni、Gwet's AC₁、logistic regression
3. 跨架构覆盖：5 模型涵盖 proprietary/open-source
4. 诚实的 confound 分析（Appendix F）
5. 跨领域连接价值：RE nocuity 理论 → LLM agent safety

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

_source line 498 · 2026-05-21T14:52:13.365505+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 44

## Round 44

2 recorded events


### User

_source line 499 · 2026-05-21T14:52:19.461098+00:00_

[Reviewer 2 审稿结果]:
审稿完成。总结：

**Overall 3.5 (Borderline Conference)**。论文的 matched-pair 因果设计和 Differential Nocuity 框架有实质新颖性，统计方法论扎实。但存在 3 个 critical 问题：(1) incompleteness 的 information-addition confound 使 type hierarchy 排名可信度打折；(2) taxonomy 6 类的 MECE 性未论证，类型标注 IAA 缺失；(3) 单域（τ²-bench 客服）实验与 Discussion 中的泛化性声称不匹配。此外遗漏了 OpenAgentSafety (ICLR 2026)、Agent-SafetyBench、Structured Uncertainty guided Clarification 等直接相关工作。

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

_source line 500 · 2026-05-21T14:52:24.810422+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 返回后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 45

## Round 45

6 recorded events


### User

_source line 501 · 2026-05-21T14:53:44.753448+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性审查

## 论文信息
- **标题**: Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents
- **Venue**: EMNLP 2026 (ARR May 2026 cycle)

---

## 总体评分

**Overall**: 3.5（Borderline Conference）
**一句话总结**: 实验设计在同类工作中罕见地严谨（matched-pair + perturbation control + 7模型复现），但 incompleteness 类型的 information-addition confound 部分削弱了核心 hierarchy claim，Discussion 对探索性 C4 结论的推断超出了证据支撑范围。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心 C1 claim 证据充分（OR=15.1，7 模型复现）；C2 hierarchy 受 incompleteness confound 影响，three-tier 结构实质上依赖于一个 confounded type 和一个 floor type；C4 标记 [Exploratory] 但 Discussion 做了较强因果推断 |
| Excitement | 3.5/5 | 首次将 ambiguity type 与 agent safety violation 建立因果映射，问题定义新颖且实用；但 V=0.137（df=5 下属 medium effect）意味着 type 之间差异虽然统计显著但实际区分度有限 |
| Reproducibility | 4/5 | 报告了模型版本、API 日期、统计方法细节、ICC；但 ICC 仅在 2 个 OpenAI 模型上计算，未覆盖跨 provider 可复现性 |
| Overall Assessment | 3.5/5 | Borderline Conference — matched-pair 因果设计是亮点，但核心 hierarchy 的可信度受 confound 限制，Discussion 需要收敛 |
| Confidence | 4/5 | 仔细阅读了全文及附录，熟悉统计方法和 agent safety 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Incompleteness confound 削弱 C2 three-tier hierarchy 的因果解释力

- 具体位置：Section 5.2 (C2), Section 3 (taxonomy definition), Appendix F
- 问题：Incompleteness 的 unambiguous variant 必须添加新的 policy content（e.g., 补充缺失的退货条件），而其他 5 个类型的 disambiguation 是 minimal edit（rephrasing existing content）。这意味着 incompleteness 的 49.2 pp 效应同时反映了 ambiguity resolution 和 information addition 两个因素。作者的 logistic regression 控制（Appendix F, p=0.022, coefficient change <8%）缓解但未消除这一 confound：(1) token count 是 information content 的粗糙代理，两个等长度的句子可以传递非常不同量的策略信息；(2) 8% 的系数变化方向未报告（增大还是减小？）；(3) 单一 logistic regression 模型无法完全剥离 information quantity 与 ambiguity resolution 的交互效应。
- 为什么影响接收："three-tier hierarchy" 是论文核心贡献之一（C2），而第一 tier 恰好是 confounded type。如果 incompleteness 的优势部分来自 information addition 而非 ambiguity 本身，则 hierarchy 实质退化为 "two-tier"（mid-cluster vs. coreferential），这已在 Appendix F 被确认（excluding incompleteness 后 omnibus p=0.079, non-significant）。论文标题 "Not All Policy Ambiguity Is Equal" 的核心支撑被削弱。
- 建议修改方向：(1) 在 Section 5.2 更显著地标注 incompleteness effect 是 upper bound 而非 point estimate；(2) 明确 two-tier structure（excluding incompleteness）作为 confound-robust 的核心 finding；(3) 报告 logistic regression coefficient 的变化方向和完整模型输出；(4) 考虑补充 information-quantity-matched control（构建等长度的 unambiguous variant，添加与 ambiguity 无关的额外 policy detail）。

**N2** [critical] Discussion 对 C4 [Exploratory] 结论做了过度因果推断

- 具体位置：Section 7, "Why incompleteness resists safety training" 段落；Abstract 第 5-6 句
- 问题：C4 被正文标注为 [Exploratory]（Section 5.4），model×type interaction 仅解释 2.9% 方差。但 Discussion 做了多处强因果推断：(1) "safety training does not uniformly reduce ambiguity vulnerability"——这是因果声明，但实验设计无法区分 safety training 与其他模型差异（architecture、pre-training data、RLHF data composition）；(2) "The agent never encounters a decision point that RLHF refusal mechanisms can intercept"——这是对训练机制的推测，缺乏任何 mechanistic evidence；(3) "making it a canary type"——将 authorization scope 定位为 safety training 质量指标，但仅基于 5 个模型上的 1 个 type 的 cross-sectional 观察。Abstract 中 "suggesting that safety training may differentially mitigate specific ambiguity types" 缺少 [Exploratory] 限定词。
- 为什么影响接收：ARR reviewer guidelines (R1) 明确指出 overclaiming 是主要审查问题。从 2.9% 探索性方差跳跃到 RLHF mechanism 推断，超出了数据支撑范围。读者可能错误地将探索性观察当作 confirmed finding。
- 建议修改方向：(1) Discussion 中所有基于 C4 的推断加上 "one possible explanation" / "consistent with but not evidence for" 等限定语；(2) Abstract 中添加 [Exploratory] 标注或改为更弱的措辞；(3) 删除 RLHF mechanism 推测段落，或改为 "Future Work" 中的 hypothesis generation；(4) 明确指出模型差异可能来源于 architecture/data/training 的多重混淆。

**N3** [critical] Cross-judge asymmetry 对 C4 model-differentiating claim 的影响未充分评估

- 具体位置：Section 4.4 (Evaluation), Section 5.4 (C4), Limitations 第 4 段
- 问题：GPT-4.1（mid-tier model）作为 GPT-5.4（frontier model）的唯一 judge，而 GPT-5.4 judging 其余三个模型。C4 的核心 finding 是 authorization scope 上 Claude (12%) vs GPT-5.4 (64%) 的差异。但 Claude 由 GPT-5.4 评判，GPT-5.4 由 GPT-4.1 评判。如果 GPT-4.1 对 authorization scope violations 的检出率系统性偏高（dual-judge calibration 中 authorization scope κ=0.385, fair），则 GPT-5.4 的 64% 率可能被 inflated。虽然论文在 Limitations 中提到 "within-judge-group analyses confirm C1" 和 "judge identity remains confounded with model identity"，但未对 C4 的 within-judge 稳健性做具体分析。Section 5.4 最后一句 "robust under both severity thresholds and within-judge analysis (Claude 12%, Qwen3 26%, DeepSeek 60%, all judged by GPT-5.4)" 只报告了 GPT-5.4-judged 组内的一致性，但 GPT-5.4 自身（由 GPT-4.1 judged）的 64% 无法被纳入此 within-judge 比较。
- 为什么影响接收：C4 是 "authorization scope as canary type" 这一实用结论的唯一证据基础。如果 GPT-5.4 的 64% 受 judge bias 影响，则 52 pp range 可能被高估。Authorization scope 的 judge agreement 恰好最低（κ=0.385），恰好在这个关键 type 上 judge reliability 最弱。
- 建议修改方向：(1) 对 dual-judge calibration 的 100 episodes 单独分析 authorization scope 的 judge-specific detection rates（GPT-4.1 vs GPT-5.4 对同一 trace 的 authorization scope 判断差异）；(2) 在 Section 5.4 中明确讨论 GPT-5.4 的 64% rate 是 GPT-4.1-judged 的结果，其可靠性受限于 authorization scope 上较低的 inter-judge agreement；(3) 考虑使用 human judges 对 GPT-5.4 的 authorization scope 子集做 spot check。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] ANOVA F-test 对 binary outcome 的方法学合理性

- 具体位置：Section 5.4, "the significant interaction (F(20) = 1.97, p = 0.006)"
- 问题：论文使用 F-test 检验 model×type interaction，但 outcome 是 binary（violation/no-violation）。对 binary outcome 的聚合比例做 ANOVA 在每个 cell 仅 50 个观测时可能违反正态性假设。更适当的方法是 logistic regression with interaction terms（论文在 Appendix F 的 confound analysis 中确实用了 logistic regression，但 C4 的 interaction test 用的是 ANOVA）。虽然 cell-level 比例在 n=50 时通过 CLT 近似正态可能是合理的，但论文未提供 model diagnostics 或 justification。
- 建议：补充 logistic regression interaction test 作为 robustness check，或说明为何 ANOVA 在此 setting 下合理。

**W2** [warning] ICC 复现性测试的覆盖面过窄

- 具体位置：Section 4.5, "30 clause pairs × 2 models (GPT-5.4 and GPT-4.1) × 3 replicates, ICC = 0.919"
- 问题：ICC 仅在 2 个 OpenAI 模型上计算，且这 2 个模型跨越了 judge boundary（GPT-5.4 由 GPT-4.1 judged，GPT-4.1 由 GPT-5.4 judged）。这测试的是 "同一 judge 对同一模型的重复评判" 的一致性，而非 "跨模型、跨 provider" 的可复现性。缺少 Claude、Qwen3、DeepSeek 的 replication data 意味着无法确认 ICC 是否反映了 GPT 系列的特定稳定性而非 general property。
- 建议：如果预算允许，对至少 1 个非 OpenAI 模型（e.g., Claude 或 Qwen3）做小规模 replication，或在 Limitations 中明确 ICC 的覆盖范围局限。

**W3** [warning] Human validation 的 100 episodes 样本量与 per-type 信度

- 具体位置：Section 4.4, "Two independent annotators labeled the same 100 stratified episodes"
- 问题：100 episodes 的人工标注用于验证整个 LLM judge pipeline。Pooled binary κ=0.798 看起来不错，但 per-type 的 human-LLM agreement 未报告。如果某些 type（特别是 authorization scope，LLM judge 间 κ=0.385）的 human-LLM agreement 也很低，则该 type 的所有结论都建立在 shaky ground 上。
- 建议：报告 per-type 的 human-LLM agreement，至少对 authorization scope 和 incompleteness 这两个关键 type 单独报告。

**W4** [warning] Perturbation control 的范围有限

- 具体位置：Section 4.5
- 问题：Perturbation control 仅包含 synonym substitution 和 clause reordering，排除了其他可能的 confounds：clause length changes, structural complexity changes, information density changes。特别是，incompleteness 的 unambiguous variant 涉及 substantial content addition，而 perturbation control 不包含 "添加等量但无关的 policy content" 这种条件。因此 perturbation control 对 incompleteness confound 没有特异性控制力。
- 建议：(1) 在 Limitations 中明确 perturbation control 不覆盖 information-addition confound；(2) 或补充 "content-matched addition" control（添加等量的 non-ambiguity-resolving policy content）。

**W5** [warning] 格式合规：正文可能超过 8 页限制

- 具体位置：PDF pages 8-9
- 问题：从 PDF 渲染结果看，Section 8 (Conclusion) 从第 8 页底部开始，约 4-5 行溢出到第 9 页。Limitations section 从第 9 页 Conclusion 之后开始。EMNLP 2026 规定 "strict 8-page limit for main text"，Limitations 不计入但 Conclusion 计入。当前排版下 Conclusion 溢出至第 9 页构成技术性违规。
- 建议：压缩 Discussion 或 Conclusion 若干行以确保 Conclusion 完整落在第 8 页内。这是一个容易修复的排版问题。

---

## 小问题（不影响接收）

- **引用年份小偏差**: `lassiter_goodman_2017` 的 OpenAlex 记录年份为 2015（可能是 online-first vs. print publication）；`levy_expectation_2008` API 返回 2007。建议核实。
- **ferrari_defects_2018** 的 bib 中 first author 为 Rosadini 但 cite key 暗示 Ferrari——bib entry 的 author field 和 cite key 不一致，容易引起混淆。
- **Abstract 信息密度过高**：Abstract 包含 OR、Cramér's V、ICC、Spearman ρ 等多个统计量，以及百分比数据点。虽然信息完整，但可读性受影响。建议将部分统计细节移入正文。
- **Coreferential 在 replication study 中被排除**（Appendix E），导致 C2 rank correlation 在 5 types（而非 6 types）上计算。这降低了 rank correlation 的 discriminative power（df=3），使得 Gemini 的 ρ=0.60 (p=0.285) 实际上不显著。应更明确说明这一限制。

---

## 主要优势

1. **实验设计严谨性**：Matched-pair + perturbation control 在 agent safety 文献中是首创级别的因果设计。相比 DRIP-R 的 correlation-based 方法，因果推断力显著更强。
2. **透明的 claim 标注**：C3 标注 inconclusive、C4 标注 [Exploratory] 是良好的科学实践，展现了作者的诚信度。这在 agent safety 领域（常见 overclaiming）中难能可贵。
3. **丰富的 sensitivity analysis**：TOST 7-margin sensitivity、双 severity threshold 对比、confound logistic regression、within-judge subgroup analysis——统计稳健性检查全面。
4. **跨 provider 复现**：从 5 模型扩展到 7 模型（6 providers）增强了 C1 和 C2 的泛化性。
5. **实用性**：Type-aware auditing framework 和 proof-of-concept detector 将学术发现连接到工程实践，"most dangerous types are least detectable" 的发现有直接的部署安全意义。
6. **Limitations 诚实详尽**：7 段 Limitations 覆盖了主要方法论弱点，包括 confound、judge asymmetry、synthetic ambiguity 等，减少了 reviewer 需要"发现"的隐藏问题。

---

## Questions to Authors

1. Appendix F 报告 logistic regression 控制 information delta 后 incompleteness 仍显著（p=0.022, coefficient change <8%）。请报告 coefficient 的变化方向（增大/减小？）以及完整的模型输出（所有 type 的 coefficients 和 CIs）。
2. 在 dual-judge calibration 的 100 episodes 中，authorization scope 的 per-type κ=0.385。这 100 episodes 中有多少属于 authorization scope？如果 n 很小，κ 的 CI 将非常宽，无法可靠判断 judge agreement 水平。
3. C4 中 model×type interaction 使用了 F-test (F(20)=1.97)。这是基于 cell-level proportions 的 two-way ANOVA 还是基于 individual observations 的 ANOVA？如果是后者，binary outcome 上的 ANOVA 需要额外 justification。
4. Perturbation control 中 "synonym substitution, clause reordering" 的具体实施方式是什么？是否有 annotator 确认 perturbation 不引入新的 ambiguity？
5. 论文声称 "All API calls were made on May 20, 2026"。在单日内完成 2,997 + 300 (perturbation) + 180 (replication) + 1,256 (mitigation) + 500 (detection) = ~5,233 episodes 的 multi-turn 交互，请确认这一时间线是否准确，是否包含足够的 API error handling 和 retry。

---

## 总结

这是一篇方法论上认真的工作，在 agent safety 文献中引入了罕见的因果设计。C1（ambiguity causes violations）的证据坚实。C2（type hierarchy）的上层受 incompleteness confound 影响，中层和下层区分有统计支撑但 effect size 有限。C3 被诚实地标注为 inconclusive。C4 [Exploratory] 的 2.9% 方差在 Discussion 中被过度推断为因果机制声明。3 个 Must-Fix 中，N1 和 N2 可通过 framing 调整和补充分析在一轮修改中解决；N3 可能需要额外实验（human spot check）或更保守的 claim。修改后有潜力达到 Conference 水平。


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

_source line 502 · 2026-05-21T14:54:35.394051+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 审稿意见：新颖性与完整性\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Incompleteness 类型的信息增量混淆因素未充分解决\n- 具体位置：§3 Taxonomy（p.3-4 incompleteness 定义）、Appendix F（p.13）\n- 问题：其他 5 类歧义的 matched-pair 操作是语义改写（ambiguous → unambiguous，信息量大致不变），但 incompleteness 类型的 unambiguous variant 实质是添加了新的 policy content（specifying what was previously missing）。作者在 Appendix F 承认 \"the 49.2 pp effect may partly reflect information addition rather than ambiguity resolution\"，logistic regression 控制后给出 31.8% 下界，但这仍然是一个根本性的操作不对称。\n- 为什么影响接收：incompleteness 的最高危地位是论文 3 个核心发现之一（§5.1, §5.2, §7 均强调），如果这个 ranking 受 confound 驱动，则论文的 central claim 被削弱。\n\n**N2** [critical] Taxonomy 的 MECE 性论证不足\n- 具体位置：§3 Ambiguity Taxonomy（p.3-4）\n- 问题：6 类之间存在重叠风险。例如 \"premium customers receive free shipping\" 既可能是 lexical ambiguity 也可能是 authorization scope。论文未讨论多类型共现的处理方式，也未报告 annotator 在类型分类（而非 severity rating）上的 IAA。\n- 为什么影响接收：如果 clause pair 跨越多类，matched-pair 设计的 \"每对隔离一种歧义类型\" 假设不成立。\n\n**N3** [critical] 单域单 benchmark 限制 vs. 过度泛化的 Discussion\n- 具体位置：§7 Discussion（p.8）、§9 Limitations（p.9）\n- 问题：全部实验在 τ²-bench 的客服域完成，§7 却使用 \"deployed systems\"、\"safety-training interventions\"、\"practitioners should\" 等泛化措辞。\n\n### Should-Fix 问题\n\n**W1** [warning] Related Work 遗漏重要 2025-2026 工作\n- OpenAgentSafety (ICLR 2026): 明确将 \"ambiguous user intent\" 作为评估维度\n- Agent-SafetyBench (Zhang et al., 2024): 349 交互环境，覆盖歧义相关 failure modes\n- Structured Uncertainty guided Clarification for LLM Agents (2025): 直接研究 agent 面对歧义的 clarification-seeking，与 Ambiguity Blindness 直接相关\n- ASPI (2026): clarification seeking 如何放大 prompt injection 风险\n\n**W2** [warning] Mitigation experiment 规模不足以支撑实践建议\n- 1,256 episodes × 5 types，每 type×model cell 约 50 episodes，未报告 CI\n\n**W3** [warning] Ambiguity Blindness 分析停留在描述层面\n- 未探讨 per-model 差异、calibration 关系、prompting 策略能否改善\n\n**W4** [warning] 引用元数据问题\n- lassiter_goodman_2017 年份应为 2015\n- ferrari_defects_2018 第一作者应为 Rosadini\n- levy_expectation_2008 作者名缺 accent\n\n### 小问题\n- Abstract \"matched-pair\" 措辞可更精确（实际是 within-subjects repeated measures）\n- Figure 3 grouped bar chart 过于拥挤，建议改 heatmap\n- \"Differential Nocuity\" 首次使用时应与 RE 原始含义明确区分\n- Table 1 Δpp 正负号含义不直观\n\n### 主要优势\n1. 严谨的因果设计\n2. 扎实的统计方法论\n3. 跨架构覆盖\n4. 诚实的 confound 分析\n5. 跨领域连接价值\n6. Limitations 诚实详尽"
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
    "project": "policy_ambiguity_safety",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 审稿意见：新颖性与完整性\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Incompleteness 类型的信息增量混淆因素未充分解决\n- 具体位置：§3 Taxonomy（p.3-4 incompleteness 定义）、Appendix F（p.13）\n- 问题：其他 5 类歧义的 matched-pair 操作是语义改写（ambiguous → unambiguous，信息量大致不变），但 incompleteness 类型的 unambiguous variant 实质是添加了新的 policy content（specifying what was previously missing）。作者在 Appendix F 承认 \"the 49.2 pp effect may partly reflect information addition rather than ambiguity resolution\"，logistic regression 控制后给出 31.8% 下界，但这仍然是一个根本性的操作不对称。\n- 为什么影响接收：incompleteness 的最高危地位是论文 3 个核心发现之一（§5.1, §5.2, §7 均强调），如果这个 ranking 受 confound 驱动，则论文的 central claim 被削弱。\n\n**N2** [critical] Taxonomy 的 MECE 性论证不足\n- 具体位置：§3 Ambiguity Taxonomy（p.3-4）\n- 问题：6 类之间存在重叠风险。例如 \"premium customers receive free shipping\" 既可能是 lexical ambiguity 也可能是 authorization scope。论文未讨论多类型共现的处理方式，也未报告 annotator 在类型分类（而非 severity rating）上的 IAA。\n- 为什么影响接收：如果 clause pair 跨越多类，matched-pair 设计的 \"每对隔离一种歧义类型\" 假设不成立。\n\n**N3** [critical] 单域单 benchmark 限制 vs. 过度泛化的 Discussion\n- 具体位置：§7 Discussion（p.8）、§9 Limitations（p.9）\n- 问题：全部实验在 τ²-bench 的客服域完成，§7 却使用 \"deployed systems\"、\"safety-training interventions\"、\"practitioners should\" 等泛化措辞。\n\n### Should-Fix 问题\n\n**W1** [warning] Related Work 遗漏重要 2025-2026 工作\n- OpenAgentSafety (ICLR 2026): 明确将 \"ambiguous user intent\" 作为评估维度\n- Agent-SafetyBench (Zhang et al., 2024): 349 交互环境，覆盖歧义相关 failure modes\n- Structured Uncertainty guided Clarification for LLM Agents (2025): 直接研究 agent 面对歧义的 clarification-seeking，与 Ambiguity Blindness 直接相关\n- ASPI (2026): clarification seeking 如何放大 prompt injection 风险\n\n**W2** [warning] Mitigation experiment 规模不足以支撑实践建议\n- 1,256 episodes × 5 types，每 type×model cell 约 50 episodes，未报告 CI\n\n**W3** [warning] Ambiguity Blindness 分析停留在描述层面\n- 未探讨 per-model 差异、calibration 关系、prompting 策略能否改善\n\n**W4** [warning] 引用元数据问题\n- lassiter_goodman_2017 年份应为 2015\n- ferrari_defects_2018 第一作者应为 Rosadini\n- levy_expectation_2008 作者名缺 accent\n\n### 小问题\n- Abstract \"matched-pair\" 措辞可更精确（实际是 within-subjects repeated measures）\n- Figure 3 grouped bar chart 过于拥挤，建议改 heatmap\n- \"Differential Nocuity\" 首次使用时应与 RE 原始含义明确区分\n- Table 1 Δpp 正负号含义不直观\n\n### 主要优势\n1. 严谨的因果设计\n2. 扎实的统计方法论\n3. 跨架构覆盖\n4. 诚实的 confound 分析\n5. 跨领域连接价值\n6. Limitations 诚实详尽"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-21T14:54:58.642100+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23248
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-21T14:54:58.794395+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 审稿意见：方法严谨性审查\n\n**Overall**: 3.5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] Incompleteness confound 削弱 C2 three-tier hierarchy 的因果解释力\n- 具体位置：Section 5.2 (C2), Section 3, Appendix F\n- 问题：Incompleteness 的 unambiguous variant 必须添加新的 policy content，而其他 5 个类型的 disambiguation 是 minimal edit。logistic regression 控制（p=0.022, coefficient change <8%）缓解但未消除这一 confound：(1) token count 是 information content 的粗糙代理；(2) 8% 系数变化方向未报告；(3) 单一 logistic regression 无法完全剥离 information quantity 与 ambiguity resolution 的交互效应。\n- 为什么影响接收：\"three-tier hierarchy\" 是核心贡献之一，而第一 tier 恰好是 confounded type。如果 incompleteness 优势部分来自 information addition，则 hierarchy 实质退化为 \"two-tier\"。\n\n**N2** [critical] Discussion 对 C4 [Exploratory] 结论做了过度因果推断\n- 具体位置：Section 7, \"Why incompleteness resists safety training\" 段落；Abstract 第 5-6 句\n- 问题：C4 被标注为 [Exploratory]，model×type interaction 仅解释 2.9% 方差。但 Discussion 做了多处强因果推断：(1) \"safety training does not uniformly reduce ambiguity vulnerability\"——因果声明但无法区分 safety training 与其他模型差异；(2) \"The agent never encounters a decision point that RLHF refusal mechanisms can intercept\"——对训练机制的推测；(3) \"making it a canary type\"——仅基于 5 模型上 1 个 type 的 cross-sectional 观察。Abstract 中缺少 [Exploratory] 限定词。\n\n**N3** [critical] Cross-judge asymmetry 对 C4 model-differentiating claim 的影响未充分评估\n- 具体位置：Section 4.4, Section 5.4, Limitations 第 4 段\n- 问题：GPT-4.1 作为 GPT-5.4 的唯一 judge，而 GPT-5.4 judging 其余三个模型。C4 核心 finding 是 authorization scope 上 Claude (12%) vs GPT-5.4 (64%)，但 Claude 由 GPT-5.4 评判而 GPT-5.4 由 GPT-4.1 评判。Authorization scope 的 judge agreement 最低（κ=0.385）。GPT-5.4 的 64% 无法被纳入 within-judge 比较。\n\n### Should-Fix 问题\n\n**W1** [warning] ANOVA F-test 对 binary outcome 的方法学合理性\n- Section 5.4 使用 F-test (F(20)=1.97) 但 outcome 是 binary，n=50/cell 时正态性假设可能不满足\n\n**W2** [warning] ICC 复现性测试覆盖面过窄\n- ICC 仅在 2 个 OpenAI 模型上计算\n\n**W3** [warning] Human validation 的 100 episodes 样本量与 per-type 信度\n- per-type 的 human-LLM agreement 未报告，authorization scope 尤其关键\n\n**W4** [warning] Perturbation control 的范围有限\n- 不包含 information-addition 类型的控制\n\n**W5** [warning] 格式合规：正文可能超过 8 页限制\n- Conclusion 约 4-5 行溢出到第 9 页\n\n### 小问题\n- 引用年份偏差（同 R2 发现）\n- ferrari_defects_2018 bib entry 不一致\n- Abstract 信息密度过高\n- Coreferential 在 replication study 中被排除降低了 rank correlation 的 discriminative power\n\n### 主要优势\n1. 因果设计在 agent safety 文献中首创\n2. 透明的 claim 标注\n3. 丰富的 sensitivity analysis\n4. 跨 provider 复现\n5. 实用性\n6. Limitations 诚实详尽\n\n### Questions to Authors\n1. Appendix F logistic regression coefficient 变化方向和完整模型输出？\n2. Authorization scope per-type κ=0.385 的样本量和 CI？\n3. C4 F-test 是 cell-level ANOVA 还是 individual-level？\n4. Perturbation control 的具体实施方式？annotator 是否确认不引入新 ambiguity？\n5. 单日完成 ~5,233 episodes 的时间线确认？"
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
    "project": "policy_ambiguity_safety",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 审稿意见：方法严谨性审查\n\n**Overall**: 3.5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] Incompleteness confound 削弱 C2 three-tier hierarchy 的因果解释力\n- 具体位置：Section 5.2 (C2), Section 3, Appendix F\n- 问题：Incompleteness 的 unambiguous variant 必须添加新的 policy content，而其他 5 个类型的 disambiguation 是 minimal edit。logistic regression 控制（p=0.022, coefficient change <8%）缓解但未消除这一 confound：(1) token count 是 information content 的粗糙代理；(2) 8% 系数变化方向未报告；(3) 单一 logistic regression 无法完全剥离 information quantity 与 ambiguity resolution 的交互效应。\n- 为什么影响接收：\"three-tier hierarchy\" 是核心贡献之一，而第一 tier 恰好是 confounded type。如果 incompleteness 优势部分来自 information addition，则 hierarchy 实质退化为 \"two-tier\"。\n\n**N2** [critical] Discussion 对 C4 [Exploratory] 结论做了过度因果推断\n- 具体位置：Section 7, \"Why incompleteness resists safety training\" 段落；Abstract 第 5-6 句\n- 问题：C4 被标注为 [Exploratory]，model×type interaction 仅解释 2.9% 方差。但 Discussion 做了多处强因果推断：(1) \"safety training does not uniformly reduce ambiguity vulnerability\"——因果声明但无法区分 safety training 与其他模型差异；(2) \"The agent never encounters a decision point that RLHF refusal mechanisms can intercept\"——对训练机制的推测；(3) \"making it a canary type\"——仅基于 5 模型上 1 个 type 的 cross-sectional 观察。Abstract 中缺少 [Exploratory] 限定词。\n\n**N3** [critical] Cross-judge asymmetry 对 C4 model-differentiating claim 的影响未充分评估\n- 具体位置：Section 4.4, Section 5.4, Limitations 第 4 段\n- 问题：GPT-4.1 作为 GPT-5.4 的唯一 judge，而 GPT-5.4 judging 其余三个模型。C4 核心 finding 是 authorization scope 上 Claude (12%) vs GPT-5.4 (64%)，但 Claude 由 GPT-5.4 评判而 GPT-5.4 由 GPT-4.1 评判。Authorization scope 的 judge agreement 最低（κ=0.385）。GPT-5.4 的 64% 无法被纳入 within-judge 比较。\n\n### Should-Fix 问题\n\n**W1** [warning] ANOVA F-test 对 binary outcome 的方法学合理性\n- Section 5.4 使用 F-test (F(20)=1.97) 但 outcome 是 binary，n=50/cell 时正态性假设可能不满足\n\n**W2** [warning] ICC 复现性测试覆盖面过窄\n- ICC 仅在 2 个 OpenAI 模型上计算\n\n**W3** [warning] Human validation 的 100 episodes 样本量与 per-type 信度\n- per-type 的 human-LLM agreement 未报告，authorization scope 尤其关键\n\n**W4** [warning] Perturbation control 的范围有限\n- 不包含 information-addition 类型的控制\n\n**W5** [warning] 格式合规：正文可能超过 8 页限制\n- Conclusion 约 4-5 行溢出到第 9 页\n\n### 小问题\n- 引用年份偏差（同 R2 发现）\n- ferrari_defects_2018 bib entry 不一致\n- Abstract 信息密度过高\n- Coreferential 在 replication study 中被排除降低了 rank correlation 的 discriminative power\n\n### 主要优势\n1. 因果设计在 agent safety 文献中首创\n2. 透明的 claim 标注\n3. 丰富的 sensitivity analysis\n4. 跨 provider 复现\n5. 实用性\n6. Limitations 诚实详尽\n\n### Questions to Authors\n1. Appendix F logistic regression coefficient 变化方向和完整模型输出？\n2. Authorization scope per-type κ=0.385 的样本量和 CI？\n3. C4 F-test 是 cell-level ANOVA 还是 individual-level？\n4. Perturbation control 的具体实施方式？annotator 是否确认不引入新 ambiguity？\n5. 单日完成 ~5,233 episodes 的时间线确认？"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-21T14:55:00.157457+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1363
}
```

</details>

---


### Assistant

_source line 506 · 2026-05-21T14:55:04.268374+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 46

## Round 46

2 recorded events


### User

_source line 507 · 2026-05-21T14:55:06.816019+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断：Overall 3.5（Borderline Conference）**

3 个 Must-Fix 问题：
1. **Incompleteness confound** 削弱了 C2 three-tier hierarchy 的因果解释力——排除 incompleteness 后 omnibus p=0.079 不显著，hierarchy 实质退化为 two-tier
2. **Discussion 对 C4 过度推断**——从 2.9% 探索性方差跳到 RLHF mechanism 因果声明，Abstract 缺少 [Exploratory] 限定
3. **Cross-judge asymmetry 对 C4 的影响**——authorization scope 的 judge agreement 最低（κ=0.385），恰好在这个 "canary type" 上 judge reliability 最弱，GPT-5.4 的 64% 率无法纳入 within-judge 验证

5 个 Should-Fix：F-test on binary outcome 方法学问题、ICC 仅覆盖 2 个 OpenAI 模型、human validation 未报告 per-type agreement、perturbation control 不覆盖 information-addition confound、正文约溢出 4-5 行至第 9 页（格式违规）。

亮点是 matched-pair 因果设计在同类工作中首创，claim 标注透明（C3 inconclusive、C4 exploratory），sensitivity analysis 全面。修改后有潜力达到 Conference 水平。

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

_source line 508 · 2026-05-21T14:55:12.474508+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 509 · 2026-05-21T14:56:15.433847+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

## Must-Fix 问题

### R2-N1: Incompleteness 信息增量混淆因素

**[AGREE]** R2-N1: 与我的 R1-N1 完全一致。Incompleteness 的操作不对称是本文最根本的方法论弱点。补充两点：

1. Appendix F 的 logistic regression 报告 "coefficient change <8%" 但未报告变化方向。如果控制 information delta 后 incompleteness coefficient 减小 8%，说明 confound 确实在 inflate effect；如果增大，则 confound 反而在 suppress effect。这一方向性信息对解读至关重要，论文遗漏了。
2. 论文声称 coreferential (information delta=0) 提供 "confound-free lower bound" (31.6%)，但这个 lower bound 的逻辑前提是假设 information addition 只能增加 violation rate。如果 information addition 在某些情况下反而降低 violation rate（例如添加的信息消除了其他隐性 ambiguity），则 31.6% 不是严格下界。

与 R2 的共识：incompleteness 的 top-tier 地位不应作为 confirmed finding 呈现。

---

### R2-N2: Taxonomy MECE 性论证不足

**[REBUT]** R2-N2: 部分同意关切，但认为不构成 critical 问题。理由如下：

1. **论文已有 annotation quality control**：Section 4.2 明确说明 "reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type"。这意味着每条 clause 经过了人工审核确认单类型归属。
2. **R2 举例不准确**："premium customers receive free shipping" 在 Section 3 中被用作 **conditional precedence** 的示例（两条规则冲突），而非 lexical 或 authorization scope。其 ambiguity 在于规则优先级，而非词义或权限边界。
3. **不过，缺少 type-classification IAA 确实是一个 gap**。论文报告了 severity rating 的 inter-annotator agreement (Section 4.4, κ=0.798)，但未报告 type assignment 的 IAA。如果两位 annotator 在 "这条 clause 属于哪个 type" 上有分歧，matched-pair 的 type-specific attribution 就不可靠。

建议降级为 **Should-Fix**：要求补充 type assignment IAA（或至少报告 annotator 之间的 type assignment disagreement rate），而非质疑整个 taxonomy 的 MECE 性。Taxonomy 不需要 MECE（现实中 ambiguity types 确实可以共现），但 experimental design 需要 single-type isolation 的 annotation reliability。

---

### R2-N3: 单域单 benchmark 限制 vs. 过度泛化

**[REBUT]** R2-N3: 关切方向正确但程度过重。

1. **并非单域**：Section 4.1 说明 τ²-bench 覆盖 "retail and airline customer service domains"，是两个域而非一个。Limitations 段 2 进一步报告 "failure mode distributions share the same top-two modes across domains, with individual mode base rates differing by up to 12.5 pp"，说明跨域一致性已有初步验证。
2. **跨 provider 复现增强泛化性**：Appendix E 的 7 模型 × 6 provider 复现（Table 7-8）表明核心 finding 不是特定模型的 artifact。C1 在所有 7 模型上显著，incompleteness ≥46% 在所有 7 模型上确认。
3. **但 Discussion 措辞确实需要收敛**：同意 "deployed systems" 和 "practitioners should" 等措辞对于两个客服域的实验来说过于泛化。建议在 Discussion 中添加 domain qualification（"in customer-service domains, our results suggest..."）。

建议降级为 **Should-Fix**：要求 Discussion 措辞加上域限定，而非将此定为 critical。

---

## Should-Fix 问题

### R2-W1: Related Work 遗漏

**[AGREE]** R2-W1: 部分同意。R2 提到的 4 篇中，与本文最直接相关的是：
- **Structured Uncertainty guided Clarification (2025)**：直接研究 agent 面对 ambiguity 的 clarification-seeking 行为，与 Section 6.2 Ambiguity Blindness 的 "<11% disambiguation awareness" 发现形成直接对话。这篇遗漏是明显的 gap。
- **ASPI (2026)**：clarification seeking 与 prompt injection 的关系也与本文的 "disambiguation channel availability" 框架相关。

另外两篇（OpenAgentSafety, Agent-SafetyBench）评估的是 agent 整体 safety 而非 policy ambiguity 的 type-specific 效应，相关性较弱。论文已引用了 R-Judge、ToolEmu、InjecAgent、ShieldAgent、AgentAuditor 等同类 benchmark（Section 2, ¶3），覆盖了 agent safety evaluation landscape 的主体。

建议：添加 clarification-seeking 相关工作的讨论，特别是与 Ambiguity Blindness 的关联。

---

### R2-W2: Mitigation experiment 规模不足

**[AGREE]** R2-W2: 同意。Table 2（Section 7）和 Appendix Table 4 报告了 per-type, per-model Δpp 但未报告 confidence intervals。每 cell ~50 episodes，某些 Δ 很小（e.g., Claude auth scope: 0.0 pp, Claude incompleteness: -2.0 pp），无法判断是 true null 还是 underpowered。论文将 mitigation 定位为 "practical implications" 但实际上更像 pilot study。

不过，我认为这不应阻止接收——mitigation 不是论文的 core contribution（核心贡献是 C1-C2 的因果量化），而是 Discussion 中的 supplementary analysis。建议作者 (1) 补充 CIs，(2) 将 "practical implications" 改为 "preliminary mitigation analysis"。

---

### R2-W3: Ambiguity Blindness 分析停留在描述层面

**[REBUT]** R2-W3: 部分不同意。

论文实际上报告了 per-model 差异：Section 6.2 明确给出 "Claude (11.0%) and GPT-4.1 (10.7%) show the highest rates, while Qwen3 and DeepSeek show zero across all 278 combined violation traces"。Claude/GPT-4.1 vs. Qwen3/DeepSeek 的 11% vs. 0% 差异已经揭示了一个重要的 model-level pattern（proprietary vs. open-source alignment 差异）。

但同意"未探讨 prompting 策略能否改善"这一批评。不过，这属于 ARR guidelines H6 ("requiring unnecessary experiments beyond claim support") 的边界情况——作者的 claim 是描述 Ambiguity Blindness 现象，而非提出 mitigation。如果要求 prompting intervention study，那属于 future work 而非 must-fix。

---

### R2-W4: 引用元数据问题

**[AGREE]** R2-W4: 与我的审稿意见一致（小问题部分）。这些是 bib entry 的事实性错误，容易修复。

---

## 小问题

### "matched-pair" 措辞
**[REBUT]**: "matched-pair" 比 "within-subjects repeated measures" 更精确。本文的设计是 clause-level matching（每条 ambiguous clause 有一个 matched unambiguous variant），这正是 matched-pair 的定义。Within-subjects repeated measures 暗示同一 subject（model）在不同 time points 重复测量，而本文中每个 model 在每个 clause 的两个 condition 上各跑一次独立 episode，更接近 matched-pair causal inference framework（à la Rubin causal model）。

### Figure 3 建议改 heatmap
**[REBUT]**: Figure 3 （fig3_heatmap.pdf）**已经是 heatmap**。PDF 第 7 页的 Figure 3 caption 为 "Violation rates (%) by model and ambiguity type under ambiguous conditions"，使用颜色矩阵呈现。R2 可能将 Figure 2（forest plot）和 Figure 3 混淆了。

### "Differential Nocuity" 首次使用区分
**[AGREE]**: 合理建议。Section 5.1 首次使用时应简要说明与 Berry & Kamsties (2004) 原始 nocuous/innocuous 二分的关系和扩展点。

### Table 1 Δpp 正负号
**[REBUT]**: Table 1 的 Δpp 列使用 "+" 号（e.g., "+49.2", "+36.0"），方向含义清晰。Caption 也说明 "Δpp denotes the pooled difference between ambiguous and unambiguous conditions"。

---

## 总结

与 R2 的主要共识：N1 (incompleteness confound) 和 W1 (missing clarification-seeking literature)。
主要分歧：N2 应降为 Should-Fix（论文有 annotation QC 但缺 type IAA），N3 应降为 Should-Fix（双域而非单域，但 Discussion 措辞需收敛），Figure 3 已是 heatmap。

两位 Reviewer 的评分一致（Overall 3.5），核心分歧在于 N2/N3 的严重性等级。


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

_source line 510 · 2026-05-21T14:56:29.627792+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 48

## Round 48

2 recorded events


### User

_source line 511 · 2026-05-21T14:56:32.168098+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心共识点：incompleteness confound（R2-N1）和 missing clarification-seeking literature（R2-W1）。主要分歧：R2-N2（taxonomy MECE）和 R2-N3（单域泛化）我认为应降级为 Should-Fix，理由是论文已有 annotation QC 且覆盖双域；R2 将 Figure 3 建议改 heatmap 但 Figure 3 已经是 heatmap。

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

_source line 512 · 2026-05-21T14:56:37.169652+00:00_

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


## Round 49

## Round 49

12 recorded events


### User

_source line 513 · 2026-05-21T14:57:16.500986+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1

### Must-Fix

**[AGREE] R1-N1: Incompleteness confound**
完全同意，与我的 N1 一致。R1 补充了三个关键点：(1) token count 是 information content 的粗糙代理，incompleteness 添加的是结构化新条款，无法被 token count 线性捕获；(2) 8% 系数变化方向未报告；(3) 单一 logistic regression 无法分离 information quantity 与 ambiguity resolution 的交互。R1 关于 "hierarchy 退化为 two-tier" 的判断精准。

**[AGREE] R1-N2: Discussion 对 C4 过度因果推断**
同意，R1 定位更精确。三点补充：(1) "safety training does not uniformly reduce..." 需要同一 base model RLHF 前后对比才能支撑；(2) "RLHF refusal mechanisms can intercept" 无 mechanistic evidence；(3) Abstract 缺 [Exploratory] 限定。

**[AGREE with nuance] R1-N3: Cross-judge asymmetry**
核心论点同意。但需区分：(1) within-judge 比较（Claude/Qwen/DeepSeek 均由 GPT-5.4 评判）仍有效；(2) GPT-5.4 自身的 64% 确实无法与其他模型直接比较。Human validation κ=0.733 部分缓解，但 per-type 未报告（与 R1-W3 形成闭环）。

### Should-Fix

**[AGREE] R1-W1**: Binary outcome 应用 logistic regression with interaction terms 而非 ANOVA。
**[AGREE] R1-W2**: ICC 仅覆盖 2 个 OpenAI 模型，但设计上有部分合理性。
**[AGREE] R1-W3**: Per-type human-LLM agreement 未报告，auth scope 尤其关键。
**[AGREE] R1-W4**: Perturbation control 不覆盖 information-addition，是 N1 confound 的方法学延伸。
**[REBUT] R1-W5**: Conclusion 溢出 4-5 行到 p.9 可能属实，但属于格式修复（压缩即可），不应影响学术评价。且需确认 p.9 顶部内容是否已属 Limitations section。

### 小问题
全部 AGREE（引用年份、Abstract 密度、coreferential 排除降低 replication discriminative power）。

### 两位 Reviewer 的共识
R1 和 R2 在以下问题上完全一致：
1. **Incompleteness confound 是最核心的方法论弱点**（R1-N1 = R2-N1）
2. **Discussion overclaiming**（R1-N2 ≈ R2-N3，R1 聚焦 C4，R2 聚焦域泛化）
3. **引用元数据问题**（R1 小问题 = R2-W4）
4. **Overall 3.5 Borderline Conference**

R2 额外提出但 R1 未覆盖的问题：
- **Taxonomy MECE 性**（R2-N2）：类型之间的重叠风险和类型标注 IAA 缺失
- **Related Work 遗漏**（R2-W1）：OpenAgentSafety、Agent-SafetyBench、clarification-seeking 文献
- **Ambiguity Blindness 分析深度不足**（R2-W3）

R1 额外提出但 R2 未覆盖的问题：
- **Cross-judge asymmetry 对 C4 的影响**（R1-N3）
- **ANOVA on binary outcome**（R1-W1）
- **Per-type human validation agreement**（R1-W3）

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

_source line 514 · 2026-05-21T14:57:31.805315+00:00_

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


### Tool call

_source line 515 · 2026-05-21T14:57:31.805715+00:00_

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

_source line 516 · 2026-05-21T14:57:33.113975+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"submitted\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T14:43:33.592077+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_10fa2e89afc5e9b8a13613245e008dd9\", \"submitted_at\": \"2026-05-21T14:45:37.494526+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-21T14:57:33.114539+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T14:43:34.734301+00:00\", \"completed_at\": \"2026-05-21T14:45:49.272040+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-5\", \"message\": \"连续 3 页纯文本（Related Work → Taxonomy → Method），无 figure/table/equation 穿插。Taxonomy 是论文核心贡献之一（6 类两层分类），缺少可视化表示（如层次图或分类概览表）使审稿人难以快速建立认知结构，建议在 §3 插入 taxonomy 概览图或结构化表格\"}, {\"severity\": \"info\", \"dimension\": \"page 1-9\", \"message\": \"主文仅 4 个 display items（2 fig + 2 table），对于实证为主的论文偏少（通常 5-8 个）。Taxonomy 可视化和/或 perturbation control 的效果对比图可补充密度\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 使用 6 色堆叠柱状图区分歧义类型，较小的堆叠段（如顶部类型）不易辨读；6 色方案的色盲可辨识度需验证（建议用 Okabe-Ito 色板或辅以 pattern fill）\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 pipeline 图内部文字偏小（估计 ~6pt），接近正文字号 70% 下限，打印后可读性需实测\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 为 full-width 表格（figure* 位置），格式使用 booktabs 风格，数字精度一致（1 位小数）。最优结果加粗标注正确\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 forest plot 清晰，CI 区间和零线标注完整，颜色区分度良好\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 2 格式规范，负值用减号标注，排版整洁\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Appendix 末页仅约 1/3 内容，空白偏多；若为 camera-ready 可考虑调整 appendix 布局紧凑化\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"References 从第 9 页下半部分开始，Conclusion 结束与 References 起始在同一页，过渡自然\"}, {\"severity\": \"info\", \"dimension\": \"page 10-12\", \"message\": \"参考文献和 Appendix 排版正常，无溢出或截断，引用编号连续，未发现 [?] 未解析引用\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 9}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-21T14:57:33.114966+00:00_

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

_source line 519 · 2026-05-21T14:57:33.167570+00:00_

1	## Round 5 Review Issues — policy_ambiguity_safety
2	## Paper: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Date: 2026-05-21
5	## Round 5 Score: 4.0 (Conference) ← Round 4: 3.5
6	
7	# ============================================================
8	# CRITICAL ISSUES (All resolved as of Round 5)
9	# ============================================================
10	
11	- id: "MF1"
12	  summary: "Cross-judge confound — judge identity 与 model identity 混淆"
13	  category: method
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 3
18	  resolution: "Dual-judge calibration: McNemar p=0.606, κ=0.653, κ_w=0.775. §4 calibration paragraph + §5.4 within-judge validation."
19	  resolution_round: 4
20	
21	- id: "MF2"
22	  summary: "Human evaluation baseline 完全缺失 — 纯 LLM-as-judge"
23	  category: method
24	  severity: critical
25	  status: resolved
26	  first_raised_round: 3
27	  last_seen_round: 4
28	  resolution: "100 stratified episodes, 2 NLP annotators. IAA binary κ=0.798, quadratic-weighted κ_w=0.762. Human-LLM pooled binary κ=0.733, quadratic-weighted κ_w=0.807. Written into §4 Method + Limitations."
29	  resolution_round: 5
30	
31	- id: "MF3"
32	  summary: "Incompleteness confound — unambiguous variant 添加新信息"
33	  category: method
34	  severity: critical
35	  status: resolved
36	  first_raised_round: 1
37	  last_seen_round: 3
38	  resolution: "§5.2 full confound discussion + logistic regression + coreferential lower-bound."
39	  resolution_round: 4
40	
41	- id: "MF4"
42	  summary: "C4 overclaimed as primary — 2.9% variance"
43	  category: framing
44	  severity: critical
45	  status: resolved
46	  first_raised_round: 3
47	  last_seen_round: 3
48	  resolution: "C4 downgraded to [Exploratory] throughout."
49	  resolution_round: 4
50	
51	# ============================================================
52	# WARNING ISSUES (All resolved)
53	# ====================
…[truncated 5259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-21T14:58:55.995396+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Round 6 (Fresh) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21\n## Round 6 Score: 3.5 (Borderline Conference)\n## Note: Fresh review session — prior rounds' resolutions re-evaluated from scratch\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"MF3\"\n  summary: \"Incompleteness confound — logistic regression 控制不充分，three-tier hierarchy 依赖 confounded type\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      note: \"Previously marked resolved via §5.2 confound discussion + logistic regression + coreferential lower-bound\"\n    - round: 6\n      note: \"R1+R2 consensus: (1) coefficient change direction unreported; (2) token count is crude proxy for information content; (3) excluding incompleteness, omnibus p=0.079 non-significant → hierarchy degrades to two-tier; (4) coreferential 'lower bound' logic assumes information addition only increases violations\"\n\n- id: \"MF4\"\n  summary: \"C4 [Exploratory] 仍在 Discussion/Abstract 中做强因果推断\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      note: \"Previously marked resolved by adding [Exploratory] tag\"\n    - round: 6\n      note: \"R1+R2 consensus: (1) 'safety training does not uniformly reduce' is causal claim unsupported by cross-sectional design; (2) RLHF mechanism speculation lacks mechanistic evidence; (3) 'canary type' based on 5 models × 1 type; (4) Abstract lacks [Exploratory] qualifier\"\n\n- id: \"R6-N3\"\n  summary: \"Cross-judge asymmetry 对 C4 authorization scope canary claim 的特异性影响\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R1 raised, R2 agrees with nuance: GPT-5.4 auth scope 64% 由 GPT-4.1 评判，auth scope κ=0.385 最低，无法纳入 within-judge 比较。Within-judge 组 (Claude/Qwen3/DeepSeek by GPT-5.4) 仍有效但不含 GPT-5.4 自身\"\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R6-W1\"\n  summary: \"Taxonomy type assignment IAA 未报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R2 raised as N2 (critical), R1 rebuts to Should-Fix: annotation QC exists (§4.2 two annotators confirm single-type) but type-classification IAA not reported. Consensus: Should-Fix\"\n\n- id: \"R6-W2\"\n  summary: \"Discussion 域泛化措辞超出实验覆盖范围\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R2 raised as N3 (critical), R1 rebuts to Should-Fix: τ²-bench covers retail + airline (two domains, not one), 7-model replication strengthens generalizability, but 'deployed systems'/'practitioners should' wording needs domain qualification\"\n\n- id: \"SF7\"\n  summary: \"Related work 遗漏 — clarification-seeking 文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      note: \"Previously resolved by adding references\"\n    - round: 6\n      note: \"R2-W1 + R1 agrees: Structured Uncertainty guided Clarification (2025) directly relates to Ambiguity Blindness; ASPI (2026) relates to disambiguation channel framework. OpenAgentSafety/Agent-SafetyBench less directly relevant\"\n\n- id: \"R6-W3\"\n  summary: \"Mitigation experiment 未报告 CI，规模不足支撑实践建议\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R2-W2, R1 agrees: per cell ~50 episodes, some Δ near zero (Claude auth scope 0.0pp), underpowered. Should label as 'preliminary' not 'practical implications'\"\n\n- id: \"R6-W4\"\n  summary: \"ANOVA F-test on binary outcome 方法学合理性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R1-W1, R2 agrees: C4 interaction F(20)=1.97 uses ANOVA on binary outcome with n=50/cell. Should supplement with logistic regression interaction test\"\n\n- id: \"R6-W5\"\n  summary: \"ICC 仅覆盖 2 个 OpenAI 模型\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R1-W2, R2 agrees: ICC=0.919 on GPT-5.4 + GPT-4.1 only, no cross-provider replication data\"\n\n- id: \"R6-W6\"\n  summary: \"Per-type human-LLM agreement 未报告\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R1-W3, R2 agrees: 100 episodes pooled κ=0.733, but per-type (especially auth scope κ=0.385 in LLM-LLM) not reported for human-LLM\"\n\n- id: \"R6-W7\"\n  summary: \"Perturbation control 不覆盖 information-addition confound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R1-W4: synonym substitution + clause reordering only; no 'content-matched addition' control for incompleteness\"\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"M1\"\n  summary: \"Bib metadata: lassiter year (2017 vs 2015), ferrari_defects first author (Rosadini vs Ferrari cite key), levy accent\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      note: \"Previously partially resolved (ferrari year corrected)\"\n    - round: 6\n      note: \"R1+R2: lassiter year discrepancy persists; ferrari cite key vs author mismatch; levy accent missing\"\n\n- id: \"R6-M1\"\n  summary: \"Abstract 信息密度过高（多个统计量堆积）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n\n- id: \"R6-M2\"\n  summary: \"Coreferential 在 replication 中排除降低 rank correlation discriminative power (df=3)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n\n- id: \"R6-M3\"\n  summary: \"Differential Nocuity 首次使用应与 Berry & Kamsties 原始含义明确区分\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n\n# ============================================================\n# PREVIOUSLY RESOLVED (carried forward for reference)\n# ============================================================\n\n- id: \"MF1\"\n  summary: \"Cross-judge confound — judge identity 与 model identity 混淆\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Dual-judge calibration: McNemar p=0.606, κ=0.653, κ_w=0.775.\"\n  resolution_round: 4\n\n- id: \"MF2\"\n  summary: \"Human evaluation baseline 完全缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"100 stratified episodes, 2 NLP annotators. IAA κ=0.798.\"\n  resolution_round: 5\n\n- id: \"SF1\"\n  summary: \"TOST ±15pp equivalence margin 缺乏理论依据\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  resolution: \"SESOI anchored to perturbation CI upper bound 6.67pp.\"\n  resolution_round: 4\n\n- id: \"SF3\"\n  summary: \"Perturbation control 检验力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Expanded to n=300.\"\n  resolution_round: 4\n\n- id: \"SF8\"\n  summary: \"正文超过 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  resolution: \"Compressed to 8 pages.\"\n  resolution_round: 4\n  mentions:\n    - round: 6\n      note: \"R1-W5 reports possible 4-5 line overflow of Conclusion onto p.9; R2 rebuts as trivial formatting fix. May need re-verification.\""
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
    "issues_yaml": "## Round 6 (Fresh) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21\n## Round 6 Score: 3.5 (Borderline Conference)\n## Note: Fresh review session — prior rounds' resolutions re-evaluated from scratch\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"MF3\"\n  summary: \"Incompleteness confound — logistic regression 控制不充分，three-tier hierarchy 依赖 confounded type\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      note: \"Previously marked resolved via §5.2 confound discussion + logistic regression + coreferential lower-bound\"\n    - round: 6\n      note: \"R1+R2 consensus: (1) coefficient change direction unreported; (2) token count is crude proxy for information content; (3) excluding incompleteness, omnibus p=0.079 non-significant → hierarchy degrades to two-tier; (4) coreferential 'lower bound' logic assumes information addition only increases violations\"\n\n- id: \"MF4\"\n  summary: \"C4 [Exploratory] 仍在 Discussion/Abstract 中做强因果推断\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      note: \"Previously marked resolved by adding [Exploratory] tag\"\n    - round: 6\n      note: \"R1+R2 consensus: (1) 'safety training does not uniformly reduce' is causal claim unsupported by cross-sectional design; (2) RLHF mechanism speculation lacks mechanistic evidence; (3) 'canary type' based on 5 models × 1 type; (4) Abstract lacks [Exploratory] qualifier\"\n\n- id: \"R6-N3\"\n  summary: \"Cross-judge asymmetry 对 C4 authorization scope canary claim 的特异性影响\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R1 raised, R2 agrees with nuance: GPT-5.4 auth scope 64% 由 GPT-4.1 评判，auth scope κ=0.385 最低，无法纳入 within-judge 比较。Within-judge 组 (Claude/Qwen3/DeepSeek by GPT-5.4) 仍有效但不含 GPT-5.4 自身\"\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R6-W1\"\n  summary: \"Taxonomy type assignment IAA 未报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R2 raised as N2 (critical), R1 rebuts to Should-Fix: annotation QC exists (§4.2 two annotators confirm single-type) but type-classification IAA not reported. Consensus: Should-Fix\"\n\n- id: \"R6-W2\"\n  summary: \"Discussion 域泛化措辞超出实验覆盖范围\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R2 raised as N3 (critical), R1 rebuts to Should-Fix: τ²-bench covers retail + airline (two domains, not one), 7-model replication strengthens generalizability, but 'deployed systems'/'practitioners should' wording needs domain qualification\"\n\n- id: \"SF7\"\n  summary: \"Related work 遗漏 — clarification-seeking 文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      note: \"Previously resolved by adding references\"\n    - round: 6\n      note: \"R2-W1 + R1 agrees: Structured Uncertainty guided Clarification (2025) directly relates to Ambiguity Blindness; ASPI (2026) relates to disambiguation channel framework. OpenAgentSafety/Agent-SafetyBench less directly relevant\"\n\n- id: \"R6-W3\"\n  summary: \"Mitigation experiment 未报告 CI，规模不足支撑实践建议\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R2-W2, R1 agrees: per cell ~50 episodes, some Δ near zero (Claude auth scope 0.0pp), underpowered. Should label as 'preliminary' not 'practical implications'\"\n\n- id: \"R6-W4\"\n  summary: \"ANOVA F-test on binary outcome 方法学合理性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R1-W1, R2 agrees: C4 interaction F(20)=1.97 uses ANOVA on binary outcome with n=50/cell. Should supplement with logistic regression interaction test\"\n\n- id: \"R6-W5\"\n  summary: \"ICC 仅覆盖 2 个 OpenAI 模型\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R1-W2, R2 agrees: ICC=0.919 on GPT-5.4 + GPT-4.1 only, no cross-provider replication data\"\n\n- id: \"R6-W6\"\n  summary: \"Per-type human-LLM agreement 未报告\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R1-W3, R2 agrees: 100 episodes pooled κ=0.733, but per-type (especially auth scope κ=0.385 in LLM-LLM) not reported for human-LLM\"\n\n- id: \"R6-W7\"\n  summary: \"Perturbation control 不覆盖 information-addition confound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      note: \"R1-W4: synonym substitution + clause reordering only; no 'content-matched addition' control for incompleteness\"\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"M1\"\n  summary: \"Bib metadata: lassiter year (2017 vs 2015), ferrari_defects first author (Rosadini vs Ferrari cite key), levy accent\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      note: \"Previously partially resolved (ferrari year corrected)\"\n    - round: 6\n      note: \"R1+R2: lassiter year discrepancy persists; ferrari cite key vs author mismatch; levy accent missing\"\n\n- id: \"R6-M1\"\n  summary: \"Abstract 信息密度过高（多个统计量堆积）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n\n- id: \"R6-M2\"\n  summary: \"Coreferential 在 replication 中排除降低 rank correlation discriminative power (df=3)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n\n- id: \"R6-M3\"\n  summary: \"Differential Nocuity 首次使用应与 Berry & Kamsties 原始含义明确区分\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n\n# ============================================================\n# PREVIOUSLY RESOLVED (carried forward for reference)\n# ============================================================\n\n- id: \"MF1\"\n  summary: \"Cross-judge confound — judge identity 与 model identity 混淆\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Dual-judge calibration: McNemar p=0.606, κ=0.653, κ_w=0.775.\"\n  resolution_round: 4\n\n- id: \"MF2\"\n  summary: \"Human evaluation baseline 完全缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"100 stratified episodes, 2 NLP annotators. IAA κ=0.798.\"\n  resolution_round: 5\n\n- id: \"SF1\"\n  summary: \"TOST ±15pp equivalence margin 缺乏理论依据\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  resolution: \"SESOI anchored to perturbation CI upper bound 6.67pp.\"\n  resolution_round: 4\n\n- id: \"SF3\"\n  summary: \"Perturbation control 检验力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Expanded to n=300.\"\n  resolution_round: 4\n\n- id: \"SF8\"\n  summary: \"正文超过 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  resolution: \"Compressed to 8 pages.\"\n  resolution_round: 4\n  mentions:\n    - round: 6\n      note: \"R1-W5 reports possible 4-5 line overflow of Conclusion onto p.9; R2 rebuts as trivial formatting fix. May need re-verification.\""
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-21T14:58:56.046221+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 7958}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-21T15:00:46.995621+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "report": "# 审稿报告 — Round 6 (Fresh Review)\n\n**论文**: Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**日期**: 2026-05-21\n**Reviewer 编排**: 2 人（R1 方法严谨性，R2 新颖性与完整性）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成共识）\n\n---\n\n## Summary\n\n本文研究 LLM agent 在自然语言策略规范下因歧义导致安全违规的因果关系。基于 τ²-bench（客服/航空双域），构建 300 组 matched clause pairs（6 类歧义 × 50 对），在 5 个模型上跑 2,997 episodes。核心发现：歧义使违规率增加 34.0 pp（OR=15.1），存在三层类型 hierarchy（incompleteness > 中间四类 > coreferential），且 model×type 交互效应显著但仅解释 2.9% 方差。提出 Differential Nocuity 框架和 Ambiguity Blindness 现象（<11% 消歧意识）。\n\n---\n\n## Strengths\n\n1. **因果设计首创性**：matched-pair + perturbation control 在 agent safety 文献中极为少见，相比 DRIP-R 等 correlation-based 工作因果推断力显著更强 [R1+R2 共识]\n2. **统计方法论扎实**：TOST 七档 sensitivity、Holm-Bonferroni 多重校正、Gwet's AC₁、dual-judge calibration、ICC 可复现性——统计稳健性检查全面 [R1]\n3. **跨架构泛化**：5 模型 + 2 额外 model families（7 模型 × 6 providers），C1 在全部 7 模型上显著 [R1+R2]\n4. **透明的 claim 分级**：C3 标注 inconclusive、C4 标注 [Exploratory]，在 agent safety 领域（常见 overclaiming）中难得 [R1]\n5. **跨领域理论迁移**：将 RE 的 nocuous/innocuous 区分引入 LLM agent safety，概念贡献有实质价值 [R2]\n6. **Limitations 详尽诚实**：7 段覆盖了主要方法论弱点，减少了审稿人需要\"发现\"的隐藏问题 [R1+R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF3 [critical, R1+R2 完全共识]** Incompleteness confound 削弱 C2 three-tier hierarchy\n\nIncompleteness 的 unambiguous variant 必须添加新 policy content，与其他 5 类的 minimal-edit disambiguation 操作不对称。Appendix F 的 logistic regression（p=0.022, coefficient change <8%）缓解但未消除 confound：(1) token count 是 information content 的粗糙代理；(2) 8% 系数变化方向未报告；(3) 排除 incompleteness 后 omnibus p=0.079 不显著，hierarchy 实质退化为 two-tier。论文将 incompleteness 的 top-tier 地位作为核心发现呈现，但这一 ranking 受 confound 驱动的可能性未被充分承认。\n\n→ 需要：(1) 正文中（非仅 Appendix）将 incompleteness ranking 表述为 upper bound；(2) 报告 logistic regression coefficient 变化方向和完整模型输出；(3) 以 two-tier structure（excluding incompleteness）作为 confound-robust 核心发现。\n\n**MF4 [critical, R1+R2 完全共识]** Discussion 对 C4 [Exploratory] 做过度因果推断\n\nC4 被标注 [Exploratory] 且仅解释 2.9% 方差，但 Discussion 做了多处强因果推断：(1) \"safety training does not uniformly reduce ambiguity vulnerability\" 是因果声明，需同一 base model RLHF 前后对比才能支撑；(2) \"The agent never encounters a decision point that RLHF refusal mechanisms can intercept\" 无 mechanistic evidence；(3) \"canary type\" 基于 5 模型上 1 type 的 cross-sectional 观察。Abstract 第 5-6 句缺少 [Exploratory] 限定。\n\n→ 需要：(1) Discussion 所有 C4 推断加 \"one possible explanation\" / \"consistent with but not evidence for\" 等限定；(2) Abstract 加 [Exploratory] 或弱化措辞；(3) RLHF mechanism 段落移至 Future Work 或改为 hypothesis。\n\n**R6-N3 [critical, R1 raised, R2 agrees with nuance]** Cross-judge asymmetry 对 C4 canary claim 的特异性影响\n\nAuthorization scope 是 C4 \"canary type\" 的核心证据（Claude 12% vs GPT-5.4 64%），但：(1) GPT-5.4 由 GPT-4.1 评判，其余由 GPT-5.4 评判——GPT-5.4 的 64% 无法纳入 within-judge 比较；(2) authorization scope 的 judge agreement 恰好最低（κ=0.385）；(3) within-judge 组（Claude/Qwen3/DeepSeek by GPT-5.4）内部模式一致（12%/26%/60%），但缺少 GPT-5.4 自身的可靠锚定。\n\n→ 需要：(1) 对 dual-judge calibration 100 episodes 单独分析 authorization scope 的 judge-specific detection rates；(2) §5.4 明确讨论 GPT-5.4 64% 的 judge reliability 限制；(3) 考虑 human spot check。\n\n### Should-Fix（影响评分但不一票否决）\n\n**R6-W1** [R2→R1 降级] Type assignment IAA 未报告——论文有 annotation QC（§4.2 两名标注员确认单类型），但未报告类型分类本身的 inter-annotator agreement。\n\n**R6-W2** [R2→R1 降级] Discussion 域泛化措辞（\"deployed systems\"、\"practitioners should\"）超出两域客服实验的覆盖范围，需加域限定。\n\n**SF7** [reopened] 遗漏 clarification-seeking 文献：Structured Uncertainty guided Clarification (2025) 与 Ambiguity Blindness 直接对话；ASPI (2026) 与 disambiguation channel 框架相关。\n\n**R6-W3** Mitigation experiment 每 cell ~50 episodes，未报告 CI，部分 Δ 近零（Claude auth scope 0.0pp）。应标注为 preliminary analysis 而非 practical implications。\n\n**R6-W4** C4 interaction test 用 ANOVA F-test on binary outcome（n=50/cell），应补充 logistic regression with interaction terms 作为 robustness check。\n\n**R6-W5** ICC=0.919 仅在 GPT-5.4 + GPT-4.1 上计算，不覆盖跨 provider 可复现性。\n\n**R6-W6** 100 episodes human validation 仅报告 pooled agreement，per-type（特别是 authorization scope）的 human-LLM agreement 缺失。\n\n**R6-W7** Perturbation control（synonym substitution + clause reordering）不覆盖 information-addition confound，对 incompleteness 无特异性控制力。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n- **MF3**: Incompleteness confound 是最核心的方法论弱点，three-tier hierarchy 的第一 tier 不可靠\n- **MF4**: Discussion 对 C4 的因果推断超出 2.9% 探索性方差的支撑范围\n- **R6-N3**: Cross-judge asymmetry 在 authorization scope 上的影响（R2 with nuance）\n- **SF7**: 遗漏 clarification-seeking 文献\n- **R6-W3**: Mitigation experiment underpowered\n- **引用元数据**: lassiter year / ferrari cite key / levy accent\n\n## Reviewer Divergence\n\n以下问题存在分级分歧（已通过交叉讨论解决）：\n- **R2-N2 Taxonomy MECE**: R2 列为 critical → R1 rebut 降为 Should-Fix（论文有 annotation QC 但缺 type IAA）→ **共识：Should-Fix (R6-W1)**\n- **R2-N3 单域泛化**: R2 列为 critical → R1 rebut 降为 Should-Fix（双域非单域，但 Discussion 措辞需收敛）→ **共识：Should-Fix (R6-W2)**\n- **R1-W5 页面溢出**: R1 列为 warning → R2 rebut 为 trivial formatting fix → **共识：minor，需确认**\n\n---\n\n## Questions\n\n1. Appendix F logistic regression 控制 information delta 后，incompleteness coefficient 变化方向（增大还是减小）？请提供完整模型输出。\n2. Dual-judge calibration 100 episodes 中 authorization scope 子集样本量多少？κ=0.385 的 CI？\n3. C4 F-test F(20)=1.97 是 cell-level proportions ANOVA 还是 individual-level ANOVA？\n4. Perturbation control 中 synonym substitution / clause reordering 是否有 annotator 确认不引入新 ambiguity？\n5. 单日（May 20）完成 ~5,233 multi-turn episodes 的技术可行性确认？\n\n---\n\n## Missing References\n\n- **Structured Uncertainty guided Clarification for LLM Agents (2025)**: 直接研究 agent 面对歧义的 clarification-seeking 行为，与 §6.2 Ambiguity Blindness 形成核心对话 [R1+R2 共识]\n- **ASPI (2026)**: clarification seeking 与 prompt injection 风险，与 disambiguation channel availability 框架相关 [R1+R2]\n- OpenAgentSafety (ICLR 2026) 和 Agent-SafetyBench (2024): 间接相关，覆盖 agent safety evaluation landscape [R2，R1 认为相关性较弱]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n状态：**已提交**（2026-05-21T14:45:37Z），结果尚未返回。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（1 warning + 9 info）：\n\n- **[warning]** pp.3-5 连续 3 页纯文本（Related Work → Taxonomy → Method），无 figure/table/equation 穿插。Taxonomy 是核心贡献之一，缺少可视化表示（层次图或概览表）使审稿人难以快速建立认知结构。建议 §3 插入 taxonomy 概览图。\n- [info] 主文仅 4 个 display items（2 fig + 2 table），对实证论文偏少（通常 5-8 个）\n- [info] Figure 3 六色方案色盲可辨识度需验证\n- [info] Figure 1 内部文字偏小（~6pt）\n- [info] Figure 2 forest plot 清晰，CI 和零线标注完整\n- [info] Table 1/2 格式规范\n- [info] Appendix 末页空白偏多\n- [info] References 无 [?] 未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5 (Borderline Conference)**\n**Confidence: 4/5**（两名 Reviewer 均仔细审读全文及附录，在交叉讨论中对关键问题达成共识）\n\n**评分理由**：\n\n论文在 agent safety 文献中引入了罕见的因果设计（matched-pair + perturbation control），C1（ambiguity causes violations, OR=15.1, 7 模型复现）的证据坚实，Differential Nocuity 框架有实质概念贡献。统计方法论全面（TOST、Holm-Bonferroni、dual-judge calibration、human validation），claim 分级透明。\n\n但 3 个 critical 问题限制了当前版本的接收水平：(1) C2 three-tier hierarchy 的第一 tier（incompleteness）受 information-addition confound 驱动，排除后 hierarchy 退化为 two-tier 且不显著；(2) C4 [Exploratory] 在 Discussion/Abstract 中被过度推断为因果机制；(3) C4 canary claim 的核心证据（authorization scope）恰好在 judge reliability 最弱的 type 上，且 GPT-5.4 的 64% 率无法被 within-judge 验证。\n\n**修改可行性**：MF3 和 MF4 可通过 framing 调整和补充统计输出在一轮内解决（将 incompleteness ranking 表述为 upper bound，将 two-tier 作为核心发现，收敛 Discussion 推断）。R6-N3 可能需要 human spot check 或更保守的 canary claim。修改后有潜力达到 4.0 (Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution list 清晰，C1-C4 分级得当\n- \"perturbation control (n=300, Δ_perturb = -0.67 pp, CI containing zero)\" 与 Method 一致\n- 建议：Contribution 2 中 \"three-tier type hierarchy\" 加注 incompleteness confound 的 caveat\n\n### §2 Related Work\n- RE ambiguity 和 psycholinguistics 文献覆盖良好\n- Agent safety 部分覆盖了主体 benchmark（R-Judge, ToolEmu, InjecAgent, ShieldAgent, AgentAuditor）\n- **缺失**：clarification-seeking 文献（与 Ambiguity Blindness 直接对话）\n\n### §3 Taxonomy\n- 六类两层结构设计合理，每类有清晰定义和示例\n- Incompleteness 的操作不对称已在 §3 末段注明（\"a confound we address in §5\"），但正文处理不够突出\n- **视觉审查建议**：此节纯文本，缺少 taxonomy 概览图\n\n### §4 Method\n- Matched-pair 设计严谨，300 对 × 5 模型的规模充分\n- Cross-judge calibration 和 human validation 是本文方法论亮点\n- ICC=0.919 excellent，但仅覆盖 2 个 OpenAI 模型（R6-W5）\n- Perturbation control 对 semantic ambiguity 有特异性，但不覆盖 information-addition（R6-W7）\n\n### §5 Results\n- C1 证据坚实（OR=15.1，所有 6 types 和 5 models 均显著）\n- C2 hierarchy: Cramér's V=0.137 在 df=5 下属 medium effect，三层结构在 TOST 七档 sensitivity 下稳定，但依赖 incompleteness（confounded）和 coreferential（floor effect）\n- C3 诚实标注 inconclusive\n- C4 标注 [Exploratory] 但方差解释力仅 2.9%——F-test on binary outcome 需补充 logistic regression robustness check\n\n### §6 Error Analysis\n- 三类 failure mechanism（structural misparse, information gap-filling, boundary violation）分类清晰\n- Ambiguity Blindness 发现有力（<11% awareness, >88% surface adoption），但缺少与 clarification-seeking 文献的对话\n- Per-model 差异已报告（Claude/GPT-4.1 11% vs Qwen3/DeepSeek 0%），但未深入分析原因\n\n### §7 Discussion\n- Differential Nocuity 框架有概念价值\n- **核心问题**：对 C4 的因果推断超出数据支撑（MF4）\n- Mitigation table (Table 2) 有实用价值但 CI 缺失（R6-W3）\n- \"practitioners should\" 等措辞需加域限定（R6-W2）\n\n### §8 Conclusion\n- 简洁准确，但可能有 4-5 行溢出至第 9 页（待确认）\n\n### §9 Limitations\n- 7 段覆盖全面，诚实承认主要弱点\n- 符合 EMNLP 2026 要求（mandatory，不计页数）\n\n### Appendix\n- TOST sensitivity (App A), mitigation (App B), severity comparison (App C), detection (App D), replication (App E), confound (App F) 均提供了有价值的补充分析\n- App F 的 logistic regression 需补充完整输出（coefficient direction, all type coefficients + CIs）",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.5"
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
    "report": "# 审稿报告 — Round 6 (Fresh Review)\n\n**论文**: Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**日期**: 2026-05-21\n**Reviewer 编排**: 2 人（R1 方法严谨性，R2 新颖性与完整性）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成共识）\n\n---\n\n## Summary\n\n本文研究 LLM agent 在自然语言策略规范下因歧义导致安全违规的因果关系。基于 τ²-bench（客服/航空双域），构建 300 组 matched clause pairs（6 类歧义 × 50 对），在 5 个模型上跑 2,997 episodes。核心发现：歧义使违规率增加 34.0 pp（OR=15.1），存在三层类型 hierarchy（incompleteness > 中间四类 > coreferential），且 model×type 交互效应显著但仅解释 2.9% 方差。提出 Differential Nocuity 框架和 Ambiguity Blindness 现象（<11% 消歧意识）。\n\n---\n\n## Strengths\n\n1. **因果设计首创性**：matched-pair + perturbation control 在 agent safety 文献中极为少见，相比 DRIP-R 等 correlation-based 工作因果推断力显著更强 [R1+R2 共识]\n2. **统计方法论扎实**：TOST 七档 sensitivity、Holm-Bonferroni 多重校正、Gwet's AC₁、dual-judge calibration、ICC 可复现性——统计稳健性检查全面 [R1]\n3. **跨架构泛化**：5 模型 + 2 额外 model families（7 模型 × 6 providers），C1 在全部 7 模型上显著 [R1+R2]\n4. **透明的 claim 分级**：C3 标注 inconclusive、C4 标注 [Exploratory]，在 agent safety 领域（常见 overclaiming）中难得 [R1]\n5. **跨领域理论迁移**：将 RE 的 nocuous/innocuous 区分引入 LLM agent safety，概念贡献有实质价值 [R2]\n6. **Limitations 详尽诚实**：7 段覆盖了主要方法论弱点，减少了审稿人需要\"发现\"的隐藏问题 [R1+R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF3 [critical, R1+R2 完全共识]** Incompleteness confound 削弱 C2 three-tier hierarchy\n\nIncompleteness 的 unambiguous variant 必须添加新 policy content，与其他 5 类的 minimal-edit disambiguation 操作不对称。Appendix F 的 logistic regression（p=0.022, coefficient change <8%）缓解但未消除 confound：(1) token count 是 information content 的粗糙代理；(2) 8% 系数变化方向未报告；(3) 排除 incompleteness 后 omnibus p=0.079 不显著，hierarchy 实质退化为 two-tier。论文将 incompleteness 的 top-tier 地位作为核心发现呈现，但这一 ranking 受 confound 驱动的可能性未被充分承认。\n\n→ 需要：(1) 正文中（非仅 Appendix）将 incompleteness ranking 表述为 upper bound；(2) 报告 logistic regression coefficient 变化方向和完整模型输出；(3) 以 two-tier structure（excluding incompleteness）作为 confound-robust 核心发现。\n\n**MF4 [critical, R1+R2 完全共识]** Discussion 对 C4 [Exploratory] 做过度因果推断\n\nC4 被标注 [Exploratory] 且仅解释 2.9% 方差，但 Discussion 做了多处强因果推断：(1) \"safety training does not uniformly reduce ambiguity vulnerability\" 是因果声明，需同一 base model RLHF 前后对比才能支撑；(2) \"The agent never encounters a decision point that RLHF refusal mechanisms can intercept\" 无 mechanistic evidence；(3) \"canary type\" 基于 5 模型上 1 type 的 cross-sectional 观察。Abstract 第 5-6 句缺少 [Exploratory] 限定。\n\n→ 需要：(1) Discussion 所有 C4 推断加 \"one possible explanation\" / \"consistent with but not evidence for\" 等限定；(2) Abstract 加 [Exploratory] 或弱化措辞；(3) RLHF mechanism 段落移至 Future Work 或改为 hypothesis。\n\n**R6-N3 [critical, R1 raised, R2 agrees with nuance]** Cross-judge asymmetry 对 C4 canary claim 的特异性影响\n\nAuthorization scope 是 C4 \"canary type\" 的核心证据（Claude 12% vs GPT-5.4 64%），但：(1) GPT-5.4 由 GPT-4.1 评判，其余由 GPT-5.4 评判——GPT-5.4 的 64% 无法纳入 within-judge 比较；(2) authorization scope 的 judge agreement 恰好最低（κ=0.385）；(3) within-judge 组（Claude/Qwen3/DeepSeek by GPT-5.4）内部模式一致（12%/26%/60%），但缺少 GPT-5.4 自身的可靠锚定。\n\n→ 需要：(1) 对 dual-judge calibration 100 episodes 单独分析 authorization scope 的 judge-specific detection rates；(2) §5.4 明确讨论 GPT-5.4 64% 的 judge reliability 限制；(3) 考虑 human spot check。\n\n### Should-Fix（影响评分但不一票否决）\n\n**R6-W1** [R2→R1 降级] Type assignment IAA 未报告——论文有 annotation QC（§4.2 两名标注员确认单类型），但未报告类型分类本身的 inter-annotator agreement。\n\n**R6-W2** [R2→R1 降级] Discussion 域泛化措辞（\"deployed systems\"、\"practitioners should\"）超出两域客服实验的覆盖范围，需加域限定。\n\n**SF7** [reopened] 遗漏 clarification-seeking 文献：Structured Uncertainty guided Clarification (2025) 与 Ambiguity Blindness 直接对话；ASPI (2026) 与 disambiguation channel 框架相关。\n\n**R6-W3** Mitigation experiment 每 cell ~50 episodes，未报告 CI，部分 Δ 近零（Claude auth scope 0.0pp）。应标注为 preliminary analysis 而非 practical implications。\n\n**R6-W4** C4 interaction test 用 ANOVA F-test on binary outcome（n=50/cell），应补充 logistic regression with interaction terms 作为 robustness check。\n\n**R6-W5** ICC=0.919 仅在 GPT-5.4 + GPT-4.1 上计算，不覆盖跨 provider 可复现性。\n\n**R6-W6** 100 episodes human validation 仅报告 pooled agreement，per-type（特别是 authorization scope）的 human-LLM agreement 缺失。\n\n**R6-W7** Perturbation control（synonym substitution + clause reordering）不覆盖 information-addition confound，对 incompleteness 无特异性控制力。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n- **MF3**: Incompleteness confound 是最核心的方法论弱点，three-tier hierarchy 的第一 tier 不可靠\n- **MF4**: Discussion 对 C4 的因果推断超出 2.9% 探索性方差的支撑范围\n- **R6-N3**: Cross-judge asymmetry 在 authorization scope 上的影响（R2 with nuance）\n- **SF7**: 遗漏 clarification-seeking 文献\n- **R6-W3**: Mitigation experiment underpowered\n- **引用元数据**: lassiter year / ferrari cite key / levy accent\n\n## Reviewer Divergence\n\n以下问题存在分级分歧（已通过交叉讨论解决）：\n- **R2-N2 Taxonomy MECE**: R2 列为 critical → R1 rebut 降为 Should-Fix（论文有 annotation QC 但缺 type IAA）→ **共识：Should-Fix (R6-W1)**\n- **R2-N3 单域泛化**: R2 列为 critical → R1 rebut 降为 Should-Fix（双域非单域，但 Discussion 措辞需收敛）→ **共识：Should-Fix (R6-W2)**\n- **R1-W5 页面溢出**: R1 列为 warning → R2 rebut 为 trivial formatting fix → **共识：minor，需确认**\n\n---\n\n## Questions\n\n1. Appendix F logistic regression 控制 information delta 后，incompleteness coefficient 变化方向（增大还是减小）？请提供完整模型输出。\n2. Dual-judge calibration 100 episodes 中 authorization scope 子集样本量多少？κ=0.385 的 CI？\n3. C4 F-test F(20)=1.97 是 cell-level proportions ANOVA 还是 individual-level ANOVA？\n4. Perturbation control 中 synonym substitution / clause reordering 是否有 annotator 确认不引入新 ambiguity？\n5. 单日（May 20）完成 ~5,233 multi-turn episodes 的技术可行性确认？\n\n---\n\n## Missing References\n\n- **Structured Uncertainty guided Clarification for LLM Agents (2025)**: 直接研究 agent 面对歧义的 clarification-seeking 行为，与 §6.2 Ambiguity Blindness 形成核心对话 [R1+R2 共识]\n- **ASPI (2026)**: clarification seeking 与 prompt injection 风险，与 disambiguation channel availability 框架相关 [R1+R2]\n- OpenAgentSafety (ICLR 2026) 和 Agent-SafetyBench (2024): 间接相关，覆盖 agent safety evaluation landscape [R2，R1 认为相关性较弱]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n状态：**已提交**（2026-05-21T14:45:37Z），结果尚未返回。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（1 warning + 9 info）：\n\n- **[warning]** pp.3-5 连续 3 页纯文本（Related Work → Taxonomy → Method），无 figure/table/equation 穿插。Taxonomy 是核心贡献之一，缺少可视化表示（层次图或概览表）使审稿人难以快速建立认知结构。建议 §3 插入 taxonomy 概览图。\n- [info] 主文仅 4 个 display items（2 fig + 2 table），对实证论文偏少（通常 5-8 个）\n- [info] Figure 3 六色方案色盲可辨识度需验证\n- [info] Figure 1 内部文字偏小（~6pt）\n- [info] Figure 2 forest plot 清晰，CI 和零线标注完整\n- [info] Table 1/2 格式规范\n- [info] Appendix 末页空白偏多\n- [info] References 无 [?] 未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5 (Borderline Conference)**\n**Confidence: 4/5**（两名 Reviewer 均仔细审读全文及附录，在交叉讨论中对关键问题达成共识）\n\n**评分理由**：\n\n论文在 agent safety 文献中引入了罕见的因果设计（matched-pair + perturbation control），C1（ambiguity causes violations, OR=15.1, 7 模型复现）的证据坚实，Differential Nocuity 框架有实质概念贡献。统计方法论全面（TOST、Holm-Bonferroni、dual-judge calibration、human validation），claim 分级透明。\n\n但 3 个 critical 问题限制了当前版本的接收水平：(1) C2 three-tier hierarchy 的第一 tier（incompleteness）受 information-addition confound 驱动，排除后 hierarchy 退化为 two-tier 且不显著；(2) C4 [Exploratory] 在 Discussion/Abstract 中被过度推断为因果机制；(3) C4 canary claim 的核心证据（authorization scope）恰好在 judge reliability 最弱的 type 上，且 GPT-5.4 的 64% 率无法被 within-judge 验证。\n\n**修改可行性**：MF3 和 MF4 可通过 framing 调整和补充统计输出在一轮内解决（将 incompleteness ranking 表述为 upper bound，将 two-tier 作为核心发现，收敛 Discussion 推断）。R6-N3 可能需要 human spot check 或更保守的 canary claim。修改后有潜力达到 4.0 (Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution list 清晰，C1-C4 分级得当\n- \"perturbation control (n=300, Δ_perturb = -0.67 pp, CI containing zero)\" 与 Method 一致\n- 建议：Contribution 2 中 \"three-tier type hierarchy\" 加注 incompleteness confound 的 caveat\n\n### §2 Related Work\n- RE ambiguity 和 psycholinguistics 文献覆盖良好\n- Agent safety 部分覆盖了主体 benchmark（R-Judge, ToolEmu, InjecAgent, ShieldAgent, AgentAuditor）\n- **缺失**：clarification-seeking 文献（与 Ambiguity Blindness 直接对话）\n\n### §3 Taxonomy\n- 六类两层结构设计合理，每类有清晰定义和示例\n- Incompleteness 的操作不对称已在 §3 末段注明（\"a confound we address in §5\"），但正文处理不够突出\n- **视觉审查建议**：此节纯文本，缺少 taxonomy 概览图\n\n### §4 Method\n- Matched-pair 设计严谨，300 对 × 5 模型的规模充分\n- Cross-judge calibration 和 human validation 是本文方法论亮点\n- ICC=0.919 excellent，但仅覆盖 2 个 OpenAI 模型（R6-W5）\n- Perturbation control 对 semantic ambiguity 有特异性，但不覆盖 information-addition（R6-W7）\n\n### §5 Results\n- C1 证据坚实（OR=15.1，所有 6 types 和 5 models 均显著）\n- C2 hierarchy: Cramér's V=0.137 在 df=5 下属 medium effect，三层结构在 TOST 七档 sensitivity 下稳定，但依赖 incompleteness（confounded）和 coreferential（floor effect）\n- C3 诚实标注 inconclusive\n- C4 标注 [Exploratory] 但方差解释力仅 2.9%——F-test on binary outcome 需补充 logistic regression robustness check\n\n### §6 Error Analysis\n- 三类 failure mechanism（structural misparse, information gap-filling, boundary violation）分类清晰\n- Ambiguity Blindness 发现有力（<11% awareness, >88% surface adoption），但缺少与 clarification-seeking 文献的对话\n- Per-model 差异已报告（Claude/GPT-4.1 11% vs Qwen3/DeepSeek 0%），但未深入分析原因\n\n### §7 Discussion\n- Differential Nocuity 框架有概念价值\n- **核心问题**：对 C4 的因果推断超出数据支撑（MF4）\n- Mitigation table (Table 2) 有实用价值但 CI 缺失（R6-W3）\n- \"practitioners should\" 等措辞需加域限定（R6-W2）\n\n### §8 Conclusion\n- 简洁准确，但可能有 4-5 行溢出至第 9 页（待确认）\n\n### §9 Limitations\n- 7 段覆盖全面，诚实承认主要弱点\n- 符合 EMNLP 2026 要求（mandatory，不计页数）\n\n### Appendix\n- TOST sensitivity (App A), mitigation (App B), severity comparison (App C), detection (App D), replication (App E), confound (App F) 均提供了有价值的补充分析\n- App F 的 logistic regression 需补充完整输出（coefficient direction, all type coefficients + CIs）",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.5"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-21T15:00:50.912063+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Assistant

_source line 524 · 2026-05-21T15:00:59.822180+00:00_

审稿报告已投递。

**本轮审稿完成。** 两名 Reviewer 经 1 轮独立审稿 + 交叉分享达成共识：

**Overall 3.5 (Borderline Conference)**

3 个 Must-Fix：
1. **Incompleteness confound**：three-tier hierarchy 第一 tier 受 information-addition confound 驱动，排除后退化为 two-tier（omnibus p=0.079）
2. **C4 overclaiming**：Discussion 对 2.9% 探索性方差做了 RLHF 机制因果推断，Abstract 缺 [Exploratory] 限定
3. **Cross-judge asymmetry**：authorization scope "canary type" 的核心证据（GPT-5.4 64%）恰好在 judge agreement 最低的 type 上（κ=0.385），且无法纳入 within-judge 验证

7 个 Should-Fix + 4 个 Minor。修改可行性：MF3/MF4 可通过 framing 调整在一轮内解决，R6-N3 可能需要补充实验。修改后有潜力达到 4.0。

外部审稿已提交，结果尚未返回。视觉审查建议 §3 Taxonomy 增加概览图。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 50

## Round 50

2 recorded events


### User

_source line 525 · 2026-05-21T15:01:02.400436+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：R1 的 6 条 Must-Fix/Should-Fix 中我同意 5 条、对 W5（页数溢出）部分反驳（属格式修复非学术问题）。两位 Reviewer 在 incompleteness confound、Discussion overclaiming、Overall 3.5 上达成共识。R2 独有贡献：taxonomy MECE 性（N2）、Related Work 遗漏（W1）、Ambiguity Blindness 深度（W3）；R1 独有贡献：cross-judge asymmetry（N3）、ANOVA 方法学（W1）、per-type human validation（W3）。

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

_source line 526 · 2026-05-21T15:01:14.624729+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结：**

- **Overall: 3.5 (Borderline Conference)**，两位 Reviewer 评分一致，交叉讨论 1 轮收敛
- **3 个 Critical 问题**：(1) incompleteness confound 使 three-tier hierarchy 第一 tier 不可靠，排除后退化为 two-tier 且不显著；(2) Discussion 对 C4 [Exploratory] 做过度因果推断（RLHF mechanism 推测、canary type 声称）；(3) cross-judge asymmetry 恰好在 authorization scope（κ=0.385 最低）上削弱 canary claim
- **7 个 Should-Fix**：type assignment IAA 缺失、Discussion 域泛化措辞、clarification-seeking 文献遗漏、mitigation CI 缺失、ANOVA on binary outcome、ICC 覆盖窄、per-type human-LLM agreement 缺失
- **修改可行性**：MF3/MF4 可通过 framing 调整（incompleteness 表述为 upper bound、two-tier 作为核心发现、Discussion 收敛）在一轮内解决，修改后有潜力达到 4.0 (Conference)
- **外部审稿**：已提交，结果未返回
- **视觉审查**：已完成，1 warning（pp.3-5 连续纯文本缺 taxonomy 可视化）

Issue tracker 已同步更新（3 critical open, 7 warning open, 4 minor open）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 51

## Round 51

64 recorded events


### User

_source line 527 · 2026-05-21T15:29:55.097597+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25

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

_source line 528 · 2026-05-21T15:30:01.040900+00:00_

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

_source line 529 · 2026-05-21T15:30:01.092107+00:00_

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

_source line 530 · 2026-05-21T15:30:04.506051+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
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
    "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-21T15:30:04.556651+00:00_



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

_source line 532 · 2026-05-21T15:30:07.869382+00:00_

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

_source line 533 · 2026-05-21T15:30:09.275120+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (16 个)\n\n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_009**: PREPARING — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_009: Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.（准备中）\n\n## 近期结论\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C1 causal inference ← 基于 plan_010\n  [plan_014_extended_perturbation_results](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/results.json) | [plan_014_perturbation_clauses_extended](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/clauses_perturbation_extended.json) | [plan_014_run_script](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/intermediate/run_plan014.py)\n- **plan_015** (success): Authorization scope violations are predominantly unauthorized escalation (granting excess permissions) rather than restriction, consistent across all 5 models, revealing systematic permissiveness bias under boundary ambiguity\n- **plan_013** (success): Binary ambiguity effect (C1: Δ >= 20pp) and type hierarchy (C2: at least partial rank consistency) re
…[truncated 247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-21T15:30:09.727355+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if paper main.tex exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if paper main.tex exists"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-21T15:30:10.229827+00:00_

-rw-r--r-- 1 ubuntu ubuntu 893 May 21 07:29 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex
EXISTS

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

_source line 536 · 2026-05-21T15:30:10.281372+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if paper PDF exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-21T15:30:10.382199+00:00_

-rw-r--r-- 1 ubuntu ubuntu 405941 May 21 15:26 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-21T15:30:14.548882+00:00_

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

_source line 539 · 2026-05-21T15:30:14.649655+00:00_



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

_source line 540 · 2026-05-21T15:30:17.861719+00:00_

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

_source line 541 · 2026-05-21T15:30:18.313799+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission deadline author guidelines page limit"
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
    "query": "ACL Rolling Review 2026 submission deadline author guidelines page limit"
  }
}
```

</details>

---


### Tool result

_source line 542 · 2026-05-21T15:30:24.235410+00:00_

Web search results for query: "ACL Rolling Review 2026 submission deadline author guidelines page limit"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"}]

Based on the search results, here's what I found about ACL Rolling Review 2026:

## Submission Deadline

The submission deadline for ACL 2026 (all papers are submitted to ARR) is January 5, 2026.

## Author Guidelines

Key requirements include:

- Starting in May 2025, all submitting authors have to also sign up as reviewers (deadline: 48h after the submission deadline)
- Papers must not include authors' na
…[truncated 912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5921
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-21T15:30:26.092679+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key submission guidelines and information for EMNLP 2026:

## Overview and Paper Types

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR Submission Process

Papers must be submitted, at latest, by the ARR 2026 May cycle. The key deadline is: **ARR submission deadline (long & short papers) May 25, 2026**

Additional important dates include:
- Reviewer registration deadline for ALL authors May 27, 2026
- Author response and 
…[truncated 829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 8230
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-21T15:30:34.229057+00:00_

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

_source line 545 · 2026-05-21T15:30:34.681340+00:00_

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
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
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
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-21T15:30:35.233679+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "decisions.yaml",
  "max_chars": "5000"
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
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-21T15:30:35.635845+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/decisions.yaml\", \"content\": \"_next_id: 26\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:11 UTC\\n  summary: MVP 设计：3 类歧义 × 2 API 模型验证 type effect，不用 GPU\\n  rationale: 核心假设是\\\"歧义类型影响安全违规率\\\"。选 scopal/lexical/incompleteness 3 种假设差异最大的类型，用 frontier\\n    API 模型（免 GPU）快速验证信号存在性。60 条款 × 2 variants × 2 模型 = 240 runs，统计功效足够（χ² df=2, medium\\n    effect w=0.3, N=240 >> 所需 ~107）。Pass 条件：p<0.05 + V≥0.15。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:15 UTC\\n  summary: 采纳 Reviewer 3 条修正：增条款数、调阈值、补 fail path\\n  rationale: 'Reviewer WARNING: (1) pairwise N=80 对 V=0.15 功效仅 0.22，增至 30 条款/类（pairwise\\n    N=120）+ 提阈值至 V≥0.20 + 明确 MVP 只检测 medium+ effect；(2) 补 fail path 三级决策树（扩大N重测 →\\n    pivot binary story → full study）；(3) 加 judge 偏差检查点（scopal 低于预期时先排查 judge bias）。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:16 UTC\\n  summary: ROADMAP 补充 H1-H4 预测基准和 post-MVP 18 周路径骨架\\n  rationale: 'Reviewer WARNING: (1) ROADMAP 缺 post-MVP 骨架，ICLR DDL 18 周后，需提前规划 GPU\\n    申请时间点（W3 MVP pass 后立即申请，W5 开始 Phase 2b）；(2) H1-H4 方向性预测未落地到 ROADMAP，Agent 解读 MVP\\n    结果时需对照基准（H1: scopal 最高，H2: lexical 最低，null: binary effect story）。paper_framing.md\\n    保持在 MVP 后创建。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-20 07:23 UTC\\n  summary: MVP 分析改为双轨：ambiguous-only 跨类型比较（主）+ matched-pair within-type（辅）\\n  rationale: 'Reviewer WARNING: incompleteness matched pair 存在信息量不对称混淆——消歧必然添加信息，与\\n    scopal/lexical 的\\\"同信息不同措辞\\\"baseline 不可比。解法：(1) 主分析用 ambiguous-only 条件直接跨类型比较违规率（不受信息量混淆）；(2)\\n    matched-pair 降为辅助的 within-type 效应量度量；(3) 要求 Agent 修订 incompleteness pairs 只添加解决歧义的最小信息；(4)\\n    效度边界显式声明此不对称性。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-20 07:24 UTC\\n  summary: MVP 使用 τ²-
…[truncated 3545 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-21T15:30:35.686478+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/",
  "description": "List paper directory contents"
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
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-21T15:30:35.787328+00:00_

_pdf_images
acl.sty
acl_natbib.bst
experiments.tex
figures
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
references.bib
sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-21T15:30:40.655116+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/",
  "description": "List paper sections"
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
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/",
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-21T15:30:41.107128+00:00_

abstract.tex
analysis.tex
appendix.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex
taxonomy.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-21T15:30:41.308323+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null | head -100",
  "description": "Read project config for external review settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null | head -100",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-21T15:30:41.359016+00:00_

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

_source line 554 · 2026-05-21T15:30:44.421694+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-21T15:30:44.573978+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-21T15:30:47.887520+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/ -maxdepth 3 -name \"*.yaml\" -path \"*/policy_ambiguity*\" 2>/dev/null | head -10",
  "description": "Find yaml files in project"
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
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/ -maxdepth 3 -name \"*.yaml\" -path \"*/policy_ambiguity*\" 2>/dev/null | head -10",
    "description": "Find yaml files in project"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-21T15:30:47.938217+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/dream_registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/writing_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/literature_map.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/mistakes.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/decisions.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/projects/policy_ambiguity_safety.yaml

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

_source line 558 · 2026-05-21T15:30:50.901089+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/projects/policy_ambiguity_safety.yaml",
  "description": "Read project config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/projects/policy_ambiguity_safety.yaml",
    "description": "Read project config"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-21T15:30:51.003477+00:00_

execution:
  account: ubuntu
  project_path: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts
  servers:
  - localhost
feishu:
  chat_id: oc_10fa2e89afc5e9b8a13613245e008dd9
  operational_chat_id: oc_c58486bc9afb8c730ded5e31c0e7d639
  review_mode: fresh
  review_paper_path: projects/policy_ambiguity_safety/docs/paper/main.tex
  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf
  review_round: 7
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

_source line 560 · 2026-05-21T15:30:59.284661+00:00_

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

_source line 561 · 2026-05-21T15:31:00.288541+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type, two-layer ambiguity taxonomy, evaluated across five architecturally diverse models (2,997 episodes). Ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. A significant type hierarchy emerges (Cram\'{e}r's $V = 0.137$, $p < 10^{-4}$), with a robust two-tier structure among five types and incompleteness as an upper bound partly reflecting an information-addition confound. The hierarchy replicates on two additional model families (LLaMA $\rho = 0.90$, $p = 0.037$; Gemini $\rho = 0.60$, directionally consistent): incompleteness is universally dangerous (46--62\% across models), while authorization scope varies 52 pp depending on the model (12\% for Claude to 64\% for GPT-5.4), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, with over 88\% surface adoption. Our Differential Nocuity framework connects type-specific vulnerability to disambiguation channel availability and suggests both type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-21T15:31:00.489604+00:00_

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

_source line 563 · 2026-05-21T15:31:00.791147+00:00_

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
…[truncated 2620 chars]

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

_source line 564 · 2026-05-21T15:31:00.791600+00:00_

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

_source line 565 · 2026-05-21T15:31:01.243438+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers, drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on two criteria: frequency in operational policy documents (assessed via manual audit of $\tau^2$-bench policies) and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by parsing or contextual cues within the text.
9	\begin{itemize}
10	\item \textbf{Scopal}: quantifier, negation, or modal scope interactions (e.g., ``all items may not be returned'' admits universal-negation and negation-of-universal readings).
11	\item \textbf{Lexical}: polysemy or homonymy (e.g., ``charge'' as financial cost vs.\ penalty; ``party'' as individual vs.\ group).
12	\item \textbf{Coreferential}: unclear pronoun or noun-phrase reference (e.g., ``the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor'' where ``which'' could refer to the verification or the refund).
13	\end{itemize}
14	
15	\paragraph{Specification layer.} These types arise from pragmatic or discourse-level gaps that require domain knowledge or organizational context to resolve.
16	\begin{itemize}
17	\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue r
…[truncated 1121 chars]

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

_source line 566 · 2026-05-21T15:31:01.243777+00:00_

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

_source line 567 · 2026-05-21T15:31:01.444699+00:00_

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
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% pass rate; disagreements were resolved by discussion. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We evaluate five models spanning four providers and two architecture families: GPT-5.4 and GPT-4.1 (OpenAI, pro
…[truncated 4116 chars]

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

_source line 568 · 2026-05-21T15:31:01.645897+00:00_

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

_source line 569 · 2026-05-21T15:31:01.696581+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). Of 1,497 matched pairs, the discordant ratio is 15.1:1 (544 ambiguous-only vs.\ 36 unambiguous-only violations). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero), and results replicate under an alternative severity threshold (Appendix~\ref{app:severity}). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. A replication on two additional model families (Gemini-2.5-Flash, LLaMA-4-Scout; Appendix~\ref{app:model_expansion}) confirms the binary effect across seven models spanning six providers ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$).
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{
…[truncated 5614 chars]

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

_source line 570 · 2026-05-21T15:31:13.542729+00:00_

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

_source line 571 · 2026-05-21T15:31:13.543252+00:00_

1	\section{Error Analysis}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from the coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}; the gap reflects the prevalence paradox, as three categories account for ${\sim}$90\% of instances).
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}---e.g., parsing ``items purchased with a coupon or during a sale are final'' as restricting only coupon purchases. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating. This dominates authorization scope exclusively (all 5 models).
17	
18	Each type's dominant failure mode is majority-consistent ($\geq$3/5 models agree), with three types 
…[truncated 1781 chars]

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

_source line 572 · 2026-05-21T15:31:14.547347+00:00_

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

_source line 573 · 2026-05-21T15:31:14.598004+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential Nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity by stakeholder divergence. Our results extend this to LLM agents: all six types are nocuous ($+34.0$ pp), but type primarily determines severity (22:1 clause-vs.-model variance ratio). We propose \emph{Differential Nocuity}: the risk of a policy ambiguity depends on type, safety training, and disambiguation channel availability. The 41.3\% majority-convergent violation rate (\emph{systematic nocuity}, \S\ref{sec:analysis}) suggests shared failure modes across architectures that make errors invisible in agreement-based evaluation. The replication across seven models spanning six providers (Appendix~\ref{app:model_expansion}) confirms this is a structural property of LLM-based agents, not an idiosyncrasy of particular architectures.
6	
7	\paragraph{Why incompleteness resists safety training.}
8	The exploratory model$\times$type interaction (C4) suggests that safety training may not uniformly reduce ambiguity vulnerability. Incompleteness is universally dangerous across all seven tested models (46--62\%), consistent with a gap-filling mechanism (\S\ref{sec:analysis}) that would bypass safety-training intervention points. Under this hypothesis, the agent would not encounter a decision point that RLHF refusal mechanisms can intercept: there is no ``should I or shouldn't I?'' moment, only a gap filled with plausible defaults \citep{ferreira_good_enough_2002,ferreira_patson_2007}. Authorization scope, by contrast, involves an explicit permission boundary that directly engages harm-avoidance objectives, making it a \emph{potential canary type}: within the same judge (GPT-5.4), Claude's 12\% rate (vs.\ 60\% for DeepSeek; \S\ref{sec:c4}) is consistent with training that targets boundary reasoning but cannot reach implicit gap-filling. When authorization scope violations do occur, 69.2\% involve unauthorized escalatio
…[truncated 1881 chars]

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

_source line 574 · 2026-05-21T15:31:15.251335+00:00_

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

_source line 575 · 2026-05-21T15:31:15.302001+00:00_

1	\section{Conclusion}
2	
3	Across five models and four providers, ambiguous policy clauses increase agent safety violations by 34.0 pp (OR $= 15.1$). Clause identity explains 22$\times$ more variance than model identity, and the type hierarchy (a robust two-tier structure among five types, with incompleteness as an upper bound partly reflecting an information-addition confound) replicates on two additional model families (LLaMA-4-Scout $\rho = 0.90$, $p = 0.037$; Gemini-2.5-Flash $\rho = 0.60$, directionally consistent). Authorization scope differentiates models (12--64\%), and incompleteness is a universal blind spot (46--62\% across all seven models). With $<$11\% disambiguation awareness, type-aware auditing and externalized detection are critical for policy-governed agent deployments.
4	

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

_source line 576 · 2026-05-21T15:31:15.503201+00:00_

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

_source line 577 · 2026-05-21T15:31:15.503635+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Model coverage.} We evaluate seven API-accessible models from six providers (four proprietary, three open-source; two in replication, Appendix~\ref{app:model_expansion}). Smaller open-source models (7B--70B parameters) may show different vulnerability patterns, and our findings may not generalize to models with fundamentally different training approaches.
5	
6	\paragraph{Domain scope.} $\tau^2$-bench covers retail and airline customer service. Policy ambiguity effects in other domains (healthcare, finance, legal) remain to be tested, though the within-study cross-domain consistency is encouraging: failure mode distributions share the same top-two modes (assumption-based action and unauthorized escalation) across domains, with individual mode base rates differing by up to 12.5 pp, likely reflecting domain policy structure rather than methodological artifacts.
7	
8	\paragraph{Synthetic ambiguity.} Our matched-pair design requires synthetic construction of ambiguous variants, which may not capture the full distribution of naturally occurring policy ambiguities. We mitigate this through expert review and a realism validation comparing ambiguous clauses against original $\tau^2$-bench policy text. Ambiguous clauses are indistinguishable from originals in lexical diversity (TTR, KS $p = 0.89$) and word length ($p = 0.09$). Readability is slightly higher (Flesch--Kincaid $d = 0.29$, $p = 0.006$) and sentence length moderately higher ($d = 0.74$), both reflecting the structural demands of encoding ambiguity in standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch--Kincaid $d = 0.14$, $p = 0.10$), confirming that minimal edits change semantic precision without altering linguistic register.
9	
10	\paragraph{Cross-judge asymmetry.} Although our dual-judge calibration (\S\ref{sec:method}) shows no systematic bias ($p = 0.606$) and human validation confirms the LLM judge operates 
…[truncated 2173 chars]

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

_source line 578 · 2026-05-21T15:31:15.855094+00:00_

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

_source line 579 · 2026-05-21T15:31:15.855543+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, a finding that parallels our observation that LLM agents adopt surface interpretations of ambiguous policy clauses. \citet{frazier_rayner_1982} demonstrate that readers commit to a single syntactic parse early and backtrack upon disambiguation failure, while \citet{levy_expectation_2008} formalizes this as expectation-based processing. \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit human-like garden-path effects, and \citet{poesio_artstein_2005} formalize genuine ambiguity in anaphoric annotation as inherent rather than resolvable. \citet{las
…[truncated 2545 chars]

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

_source line 580 · 2026-05-21T15:31:15.906085+00:00_

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

_source line 581 · 2026-05-21T15:31:15.906845+00:00_

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
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). The treatment appends a type-specific disambiguation instruction to the agent's system prompt. Control rates are the matched 5-type subset from the full study (\S\ref{sec:results}).
30	
31	\begin{table*}[!ht]
32	\centering
33	\small
34	\caption{Violation rate change ($\Delta$pp) after adding type-specific disambiguation instructions. Negative values indicate reduction. Baseline violation rates are shown in parentheses. Coreferential was 
…[truncated 10655 chars]

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

_source line 582 · 2026-05-21T15:31:38.078909+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "4"
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
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-21T15:31:38.129600+00:00_



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

_source line 584 · 2026-05-21T15:31:42.545676+00:00_

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

_source line 585 · 2026-05-21T15:32:04.044767+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21499
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-21T15:32:05.301375+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex（分节文件在 sections/ 目录下）\n- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026（通过 ARR May cycle 提交）\n- Deadline: 2026-05-25\n\n## Venue 格式要求\n- 长文正文 8 页限制，参考文献不限\n- Limitations 和 Ethics 不计入页数（不含过多附加内容）\n- ACL 模板，double-blind 匿名审稿\n- 通过 ARR 统一审稿系统\n- Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **实验设计**：matched-pair 因果设计是否成立？300 clause pairs 的构建方法（template-based + 人工审核）是否有系统性偏差？annotator 验证（96% pass rate）是否充分？\n2. **统计分析**：McNemar's test / χ² / Fisher's exact / TOST 的使用是否恰当？多重比较校正（Holm-Bonferroni）是否完备？效应量（Cramér's V=0.137）解释是否合理？统计功效分析是否充分？\n3. **因果推断**：perturbation control (n=300, Δ=-0.67pp) 是否足够排除混淆变量？incompleteness 的信息添加混淆如何处理？logistic regression 控制是否充分？\n4. **评估 pipeline**：cross-judge 设计的合理性（GPT-5.4 judge Claude/Qwen3/DeepSeek，GPT-4.1 judge GPT-5.4）——judge 能力不对称是否影响结论？human validation (100 episodes, κ=0.733) 样本量是否够？per-type reliability 差异（auth scope κ=0.385 vs incompleteness κ=0.875）对结论的影响？\n5. **可复现性**：ICC=0.919 仅在 OpenAI 模型内计算，跨 provider 可复现性如何？API 时间点（2026-05-20）的模型版本锁定问题？\n6. **Claims 与证据匹配**：四个 claim (C1-C4) 的证据强度是否匹配其声明力度？C3 inconclusive 但仍出现在论文中是否合适？C4 exploratory 标签是否足够谨慎？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → 评分建议（使用 EMNLP 2026 评分标准）。"
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
    "project": "policy_ambiguity_safety",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex（分节文件在 sections/ 目录下）\n- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026（通过 ARR May cycle 提交）\n- Deadline: 2026-05-25\n\n## Venue 格式要求\n- 长文正文 8 页限制，参考文献不限\n- Limitations 和 Ethics 不计入页数（不含过多附加内容）\n- ACL 模板，double-blind 匿名审稿\n- 通过 ARR 统一审稿系统\n- Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **实验设计**：matched-pair 因果设计是否成立？300 clause pairs 的构建方法（template-based + 人工审核）是否有系统性偏差？annotator 验证（96% pass rate）是否充分？\n2. **统计分析**：McNemar's test / χ² / Fisher's exact / TOST 的使用是否恰当？多重比较校正（Holm-Bonferroni）是否完备？效应量（Cramér's V=0.137）解释是否合理？统计功效分析是否充分？\n3. **因果推断**：perturbation control (n=300, Δ=-0.67pp) 是否足够排除混淆变量？incompleteness 的信息添加混淆如何处理？logistic regression 控制是否充分？\n4. **评估 pipeline**：cross-judge 设计的合理性（GPT-5.4 judge Claude/Qwen3/DeepSeek，GPT-4.1 judge GPT-5.4）——judge 能力不对称是否影响结论？human validation (100 episodes, κ=0.733) 样本量是否够？per-type reliability 差异（auth scope κ=0.385 vs incompleteness κ=0.875）对结论的影响？\n5. **可复现性**：ICC=0.919 仅在 OpenAI 模型内计算，跨 provider 可复现性如何？API 时间点（2026-05-20）的模型版本锁定问题？\n6. **Claims 与证据匹配**：四个 claim (C1-C4) 的证据强度是否匹配其声明力度？C3 inconclusive 但仍出现在论文中是否合适？C4 exploratory 标签是否足够谨慎？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → 评分建议（使用 EMNLP 2026 评分标准）。"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-21T15:32:17.968048+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12666
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-21T15:32:18.269672+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "policy_ambiguity_safety",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex（分节文件在 sections/ 目录下）\n- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026（通过 ARR May cycle 提交）\n- Deadline: 2026-05-25\n\n## Venue 格式要求\n- 长文正文 8 页限制，参考文献不限\n- Limitations 和 Ethics 不计入页数（不含过多附加内容）\n- ACL 模板，double-blind 匿名审稿\n- 通过 ARR 统一审稿系统\n- Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重：新颖性与完整性\n\n请重点审查以下方面：\n\n1. **Taxonomy 合理性**：6 类歧义的 two-layer 结构（linguistic vs specification）是否有理论支撑？authorization scope 和 conditional precedence 归类为\"specification\"而非 linguistic 的理据是否充分？与 Li et al. 2024、Massey et al. 2014、DRIP-R 2026 的区别和继承关系是否清晰？\n2. **新颖性评估**：Differential Nocuity 框架的增量贡献是什么？与 DRIP-R (concurrent, 400 scenarios, 5 RE types)、PolicyBank、AgentPex 等并行工作的差异化是否足够？matched-pair 因果设计 vs DRIP-R 的相关性设计——这种方法论差异是否构成足够的贡献？\n3. **Related Work 覆盖**：是否遗漏了重要相关工作？特别是：(a) ambiguity detection/resolution 领域，(b) agent safety benchmarks，(c) policy specification for agents，(d) LLM evaluation methodology。引用是否真实（注意检查 2026 年的引用）？\n4. **论文叙事与结构**：CL-first framing（从语言学入手，safety 作为 application context）是否适合 EMNLP？Introduction 的 claim 是否与 Results 一致？四个 contribution 的表述是否过度/不足？\n5. **格式合规**：8 页正文限制是否满足？ACL 模板使用是否正确？匿名规则（\\author{Anonymous}）是否合规？图表质量和信息密度？\n6. **Limitations 完整性**：已列出的 limitations 是否覆盖了主要弱点？是否有重要未提及的限制？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues → 评分建议（使用 EMNLP 2026 评分标准）。"
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
    "project": "policy_ambiguity_safety",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex（分节文件在 sections/ 目录下）\n- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026（通过 ARR May cycle 提交）\n- Deadline: 2026-05-25\n\n## Venue 格式要求\n- 长文正文 8 页限制，参考文献不限\n- Limitations 和 Ethics 不计入页数（不含过多附加内容）\n- ACL 模板，double-blind 匿名审稿\n- 通过 ARR 统一审稿系统\n- Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重：新颖性与完整性\n\n请重点审查以下方面：\n\n1. **Taxonomy 合理性**：6 类歧义的 two-layer 结构（linguistic vs specification）是否有理论支撑？authorization scope 和 conditional precedence 归类为\"specification\"而非 linguistic 的理据是否充分？与 Li et al. 2024、Massey et al. 2014、DRIP-R 2026 的区别和继承关系是否清晰？\n2. **新颖性评估**：Differential Nocuity 框架的增量贡献是什么？与 DRIP-R (concurrent, 400 scenarios, 5 RE types)、PolicyBank、AgentPex 等并行工作的差异化是否足够？matched-pair 因果设计 vs DRIP-R 的相关性设计——这种方法论差异是否构成足够的贡献？\n3. **Related Work 覆盖**：是否遗漏了重要相关工作？特别是：(a) ambiguity detection/resolution 领域，(b) agent safety benchmarks，(c) policy specification for agents，(d) LLM evaluation methodology。引用是否真实（注意检查 2026 年的引用）？\n4. **论文叙事与结构**：CL-first framing（从语言学入手，safety 作为 application context）是否适合 EMNLP？Introduction 的 claim 是否与 Results 一致？四个 contribution 的表述是否过度/不足？\n5. **格式合规**：8 页正文限制是否满足？ACL 模板使用是否正确？匿名规则（\\author{Anonymous}）是否合规？图表质量和信息密度？\n6. **Limitations 完整性**：已列出的 limitations 是否覆盖了主要弱点？是否有重要未提及的限制？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues → 评分建议（使用 EMNLP 2026 评分标准）。"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-21T15:32:19.628873+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1359
}
```

</details>

---


### Assistant

_source line 590 · 2026-05-21T15:32:26.146945+00:00_

Round 1 已启动：

- **视觉审查 Agent**：已派发，与审稿并行执行
- **Reviewer 1**（方法严谨性）：已分配——实验设计、统计分析、因果推断、评估 pipeline、可复现性
- **Reviewer 2**（新颖性/完整性）：已分配——taxonomy 合理性、新颖性、相关工作、叙事结构、格式合规

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


## Round 52

## Round 52

2 recorded events


### User

_source line 591 · 2026-05-21T15:40:18.060227+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性审查

## 论文信息
- **标题**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
- **Venue**: EMNLP 2026 (ARR May cycle)

---

## Summary

本文通过 matched-pair 因果设计研究政策歧义类型与 LLM agent 安全违规之间的关系。在 τ²-bench 上构建 300 组 clause pairs（6 种歧义类型 × 50 对），跨 5 个模型评估 2,997 episodes。核心发现：(1) 歧义条款使违规率增加 34.0pp（OR=15.1）；(2) 类型间存在显著层级结构（Cramér's V=0.137），incompleteness 最危险（46-62%），authorization scope 模型间差异最大（12-64%）；(3) agent 几乎不具备歧义识别能力（<11%）。论文提出 Differential Nocuity 框架，将类型特异性风险与消歧渠道可用性关联。

实验设计整体严谨，统计方法选择得当，perturbation control 和 replication 增强了因果推断可信度。但在几个关键方法论问题上存在不足，主要涉及评估管线的 judge-model confounding、authorization scope 的低测量可靠性、以及 incompleteness 的信息添加混淆。

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 实验设计和统计分析整体扎实，但论文最突出的两个发现（incompleteness 普遍危险、auth scope 作为 canary type）恰恰建立在测量可靠性最弱的基础上，需要更充分的 hedging 或补充验证。

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心因果设计强，但 headline claims 的测量基础有缺陷（auth scope κ=0.385, incompleteness confound 未完全解决） |
| Excitement | 4/5 | 首个将歧义类型与 agent 安全违规因果关联的研究，Differential Nocuity 框架有理论和实践价值 |
| Reproducibility | 3/5 | ICC=0.919 仅限 OpenAI 模型内部；API snapshot 单日（May 20, 2026）；无代码/数据发布声明 |
| Confidence | 4/5 | 本人在实验设计和统计方法方面有充分专业背景 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Authorization scope 测量可靠性过低，无法支撑 "canary type" 主张

- 具体位置：§4.4 cross-judge calibration (κ=0.385), §5.4 C4 (52pp model range), Table 9 (human-LLM κ=0.644, 95% CI [0.35, 0.91]), Discussion "potential canary type"
- 问题：Authorization scope 是论文最引人注目的发现之一（52pp 跨模型差异，Claude 12% vs GPT-5.4 64%，被提议为 safety training 的 canary type），但这个类型的 cross-judge κ 仅 0.385（fair），是所有类型中最低的。Human-LLM agreement 的 95% CI 为 [0.35, 0.91]，极宽。Per-type 验证样本仅 n=34，不足以可靠估计 type-specific reliability。虽然论文在 §5.4 提到 within-judge comparison（控制 judge identity 后仍有 48pp range），但这仍然依赖同一个 judge（GPT-5.4）的 type-level 判断一致性，而恰恰该 type 的判断一致性最低。
- 为什么影响接收：Abstract、Introduction contribution list、Discussion、Conclusion 均突出 authorization scope 的 model-differentiating 特性。如果这个类型的测量噪声占据了 52pp range 的相当部分，那么核心叙事的支柱之一就不稳固。
- 建议修改方向：(a) 明确报告 auth scope 的 within-judge raw agreement 和 detection vs severity 的分离分析；(b) 在 Abstract 和 Conclusion 中对 canary type 主张加上显式 measurement-uncertainty caveat（如"subject to the lowest per-type judge reliability"）；(c) 考虑增加 auth scope 的 human validation 样本量（当前 n=34 不够）。

**N2** [critical] Judge-model confounding 未被充分处理

- 具体位置：§4.4 Evaluation（GPT-5.4 judges Claude/Qwen3/DeepSeek; GPT-4.1 judges GPT-5.4），§Limitations "Cross-judge asymmetry"
- 问题：每个 agent model 由单一 judge 评估，导致 judge identity 与 model identity 完全 confounded。dual-judge calibration（n=100, McNemar p=0.606）只能在 aggregate level 排除 systematic bias，但无法排除 type-specific 或 model-specific bias。尤其是 GPT-4.1（mid-tier）judging GPT-5.4（frontier）这个方向更令人担忧——能力不对称可能导致 GPT-4.1 低估 GPT-5.4 的微妙违规，从而人为压低 GPT-5.4 的违规率。Limitations 承认 C3 在 within-judge-group 分析中均未达显著性（GPT-4.1-judged p=0.059, GPT-5.4-judged p=0.157），这直接说明 pooled 结果可能包含 judge-level artifact。
- 为什么影响接收：C4（model×type interaction）的核心发现——不同模型对不同类型的差异响应——在 judge-model confounding 下因果解释力减弱。Authorization scope 的 model differentiation（最核心发现之一）尤其受影响。
- 建议修改方向：(a) 对所有 5 个 model 用两个 judge 分别评估一个 subset（如各 100 episodes），以估计 judge×model interaction 大小；(b) 至少报告 calibration sample 中 per-model 的 judge agreement，而非仅报告 aggregate；(c) 在 C4 结论中明确标注 judge-model confounding 对 model-level 结论的限制。

**N3** [critical] 缺少 a priori power analysis，50 pairs/type 的样本量合理性未论证

- 具体位置：§4.2 Matched-Pair Design (50 clause pairs per type)
- 问题：论文未报告 a priori power analysis。50 对/类型的选择似乎是 pragmatic 的，但对于以下关键分析其统计功效不明确：(a) TOST equivalence testing with ±15pp margin——null 结果（equivalence confirmed）的可信度取决于功效；(b) pairwise type comparisons with Holm-Bonferroni correction——correction 后 detectable effect size 是多少？(c) per-type per-model cells（n=50 episodes）的 Fisher's exact test——如 Table 1 中 Claude auth scope 仅 12%（约 6/50 episodes），这些小计数的 estimate 极不稳定。
- 为什么影响接收：ARR Soundness 维度要求 claims 有充分统计支持。C2 的 "two-tier structure" 依赖 TOST equivalence，但没有功效分析就无法区分 "types are equivalent" 和 "we lack power to detect difference"。
- 建议修改方向：报告 post-hoc power analysis（至少对 TOST 和 pairwise comparisons），说明在当前 n=50 下可检测的最小效应量。若功效不足，需在 C2 结论中相应缩小声明。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Incompleteness confound 的 hedging 在 Abstract/Conclusion 中不够显著

- 具体位置：Abstract ("incompleteness is universally dangerous (46-62%)"), Conclusion ("incompleteness is a universal blind spot (46-62% across all seven models)"), §5.2 C2, Appendix F
- 问题：Incompleteness 的 unambiguous variant 必须添加新的政策内容，这与其他 5 种类型（仅改写现有内容）结构性不同。论文在 §3 Taxonomy 和 §5.2 中提到了这个混淆，并在 Appendix F 进行了 logistic regression 控制。但控制方式有局限：(a) token count difference 是 information content 的粗糙代理；(b) 即使控制了 token delta，"添加缺失信息" 和 "消除歧义" 在概念上仍是不同干预。Coreferential 作为 "confound-free lower bound"（31.6%）的论证逻辑上不成立——它是不同类型，不是 incompleteness 的无混淆版本。
- 建议：在 Abstract 中将 "universally dangerous" 改为更审慎的表述（如 "shows the highest violation rates, though the effect partly confounds ambiguity resolution with information addition"）；在 Conclusion 中同样加强 hedging。

**W2** [warning] TOST SESOI ±15pp 的选择缺乏外部锚定

- 具体位置：§4.6 Statistical Analysis
- 问题：±15pp 的 SESOI 被定义为 "a type producing ≥15 pp more violations warrants distinct policy handling"。这是一个 reasonable practical argument，但缺乏外部锚定。为什么不是 ±10pp 或 ±20pp？Sensitivity analysis（Appendix A, Table 3）显示在 ±10pp 时仅 3/6 mid-tier pairs equivalent，在 ±12pp 时 5/6——两个看起来同样合理的 margin 给出截然不同的 tier structure 结论。论文的 "robust two-tier structure" claim（Abstract、Conclusion）主要在 ≥15pp 时成立。
- 建议：(a) 讨论 SESOI 选择对结论的敏感性（不仅在 Appendix 展示数据，还在主文中明确说明 tier structure 依赖 margin 选择）；(b) 考虑报告 minimum SESOI at which the two-tier structure emerges（约 ±12pp），增加透明度。

**W3** [warning] ICC=0.919 仅限 OpenAI 模型内部，cross-provider 可复现性未知

- 具体位置：§4.5 Controls, Reproducibility paragraph
- 问题：ICC=0.919 (95% CI [0.892, 0.940]) 是优秀的可复现性指标，但仅基于 GPT-5.4 和 GPT-4.1（均为 OpenAI），在相同 API 下测量。Cross-provider 可复现性（如 Claude 或 DeepSeek 在不同时间的行为稳定性）未直接测量。论文声称 "consistency of C1 across all seven models" 间接支持，但这是 cross-model 一致性而非 temporal reproducibility。
- 建议：明确指出 ICC 仅反映 within-provider temporal stability，不应被解读为 cross-provider reproducibility 的证据。

**W4** [warning] Mitigation experiment（Table 2）样本量过小却在主文 Discussion 中占重要位置

- 具体位置：§7 Discussion, Table 2 (1,256 episodes, ~50 per cell)
- 问题：Per-cell ~50 episodes 产生很宽的 CI（论文自己也说 "per-cell CIs are wide"）。DeepSeek 在 scopal (+2.0pp) 和 incompleteness (+4.0pp) 上显示增加而非减少，表明 mitigation 效果不稳定。然而 Discussion 用这些数据得出 "authorization scope benefits most (−18.0pp), while incompleteness is nearly immune (−3.4pp)" 的具体结论。
- 建议：将 Table 2 移至 Appendix，在 Discussion 中仅报告方向性趋势，并明确标注为 preliminary。

**W5** [warning] Failure mode taxonomy 的 inter-coder reliability 偏低

- 具体位置：§6 Error Analysis (Gwet's AC₁=0.62, Cohen's κ=0.52)
- 问题：Cohen's κ=0.52 仅为 moderate agreement。论文解释为 prevalence paradox（3 类占 ~90%），AC₁=0.62 部分补偿了这一点。但对少数类别（arbitrary rule selection κ=0.29），reliability 很差。论文在 Limitations 中提到 "human validation of the coding scheme would further strengthen these findings"，但未实际执行。
- 建议：(a) 报告 per-category 的 AC₁ 和 sample size；(b) 在主文中更明确地标注 failure mode taxonomy 的分析为 tentative。

---

## Questions for Authors

**Q1**: 50 clause pairs/type 的决定依据是什么？是基于 pilot study 的效应量估计，还是资源约束？若有 pilot data，请报告 power calculation。

**Q2**: Cross-judge calibration 的 100 episodes 中，per-model 的 judge agreement 如何分布？特别是 GPT-4.1 判 GPT-5.4 的 accuracy 与 GPT-5.4 判其他模型相比是否有系统差异？

**Q3**: Logistic regression 控制 incompleteness confound 时（Appendix F），具体控制了哪些变量？仅 token delta 还是包括 syntactic complexity、information density 等更细的指标？Coefficient change <8% 是否在 practical significance 意义上足够小？

**Q4**: Template-based clause generation pipeline 的具体操作是什么？Templates 是如何设计的？同一 template 产生的多个 clause pairs 之间是否存在 structural correlation？如果是，matched-pair test 的独立性假设是否被违反？

**Q5**: 论文提到 "3 episodes lost to API errors in one Qwen3 batch"（§4.2），2,997 而非 3,000。这是否可能引入 selection bias（如某些 ambiguity types 或 clause pairs 更容易触发 API errors）？

**Q6**: C3（layer effect）在 Holm-Bonferroni correction 后不显著，controlling for token delta 后方向反转。保留 C3 在主文中的理由是什么？它增加了叙事复杂性但提供了 null/negative evidence。

---

## Minor Issues

- Lassiter & Goodman (2017) 的出版年份可能是 2015（Synthese online-first），建议核实
- ferrari_defects_2018 的 bib entry first author 为 Rosadini 而非 Ferrari，但正文 cite 时似乎隐含 Ferrari 是第一作者
- Abstract 信息密度极高，建议精简（当前包含 OR、V、p-value、pp range 等过多数字，降低可读性）
- §5.2 中 "upper bound whose ranking partly reflects an information-addition confound" 在不同位置出现 ≥4 次，措辞近乎逐字重复，建议精简
- Figure 2 (forest plot) 的 x 轴标签和 CI whiskers 在 PDF 中较小，可读性可改善

---

## 主要优势

1. **Matched-pair causal design 是本文最大的方法论贡献**：相比 DRIP-R 等 correlational work，matched-pair 设计 + perturbation control (n=300, Δ=-0.67pp) 显著增强了因果推断可信度。每对 clause pair 仅做 minimal edit，有效控制了文本特征混淆变量。

2. **统计分析全面且恰当**：McNemar's test（paired binary）、Fisher's exact（per-type, small cells）、TOST equivalence（区分 "no difference" vs "equivalent"）、Holm-Bonferroni correction、effect size reporting (OR, V, Δpp) 均选择得当。多重比较校正和 sensitivity analysis（7 个 SESOI margins, 2 个 severity thresholds）增加了结论的稳健性。

3. **Transparent about limitations**：论文在多处主动承认混淆（incompleteness information addition）、标注 inconclusive（C3）和 exploratory（C4）、报告 per-type judge reliability 差异。这种 intellectual honesty 在 NLP 论文中不常见，值得肯定。

4. **Cross-architecture replication**：5+2 个模型跨 6 个 provider 的 replication（C1 在所有 7 个模型上 p < 10⁻⁶，C2 ranking ρ=0.90 for LLaMA）大幅增强了 generalizability。

5. **Practical framework**：Differential Nocuity 不仅是理论贡献——Table 2 的 mitigation experiment（虽然 preliminary）和 Appendix D 的 detection experiment 提供了可操作的实践方向。

---

## 评分建议

**Overall Assessment**: 3.5 (Borderline Conference)

理由：论文在研究问题（首个 causal, type-granularity ambiguity→safety mapping）、实验设计（matched-pair + perturbation control）和统计分析（comprehensive + transparent）方面达到了 Conference 水准。但三个 critical issues 共同削弱了核心叙事：(1) 最突出的 type-specific 发现（auth scope canary type）建立在最低可靠性测量上；(2) judge-model confounding 限制了 C4 的因果解释力；(3) 缺少 power analysis 使 C2 tier structure 的 equivalence claims 不够可信。若作者能在 revision 中解决 N1-N3（增加 auth scope 验证样本、报告 per-model judge agreement、补充 power analysis），本文可达 4.0 (Conference)。当前 3.5 反映方法论缺陷可修复但影响结论可信度。


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

_source line 592 · 2026-05-21T15:40:24.860755+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 53

## Round 53

2 recorded events


### User

_source line 593 · 2026-05-21T15:40:36.387046+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5 (Borderline Conference)。

核心判断：matched-pair causal design + perturbation control 是本文方法论上的最大优势，统计分析全面且恰当。但三个 critical issues 削弱了核心叙事：

1. **Auth scope 测量可靠性过低**（κ=0.385）却支撑了 "canary type" 这一最引人注目的发现
2. **Judge-model confounding** 限制了 C4 model×type interaction 的因果解释力
3. **缺少 a priori power analysis**，50 pairs/type 对 TOST equivalence claims 的支撑不明确

这三个问题可在 revision 中修复（增加 auth scope 验证样本、报告 per-model judge agreement、补充 power analysis），修复后可达 4.0 (Conference)。

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

_source line 594 · 2026-05-21T15:40:41.541292+00:00_

Reviewer 1 意见已收到，等待 Reviewer 2 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 54

## Round 54

6 recorded events


### User

_source line 595 · 2026-05-21T15:40:53.529645+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性与完整性

**论文**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 (ARR May cycle)

---

## 总体评分

**Overall Assessment**: 3.5 / 5（Borderline Conference）
**一句话总结**: 方法论扎实的 matched-pair 因果研究，taxonomy 有理论支撑，但核心发现（incompleteness 最危险）的新颖性受限于 information-addition confound，且主文超出 8 页限制。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claim 有充分实验支撑，matched-pair 设计严谨，统计方法得当（TOST equivalence testing, logistic regression）。但 incompleteness 类型与其他5类存在 information-addition confound，削弱了跨类型可比性。 |
| Excitement | 3.0/5 | 选题及时（agent safety + policy ambiguity），CL-first framing 适合 EMNLP，但核心发现"不同歧义类型风险不同"较为 expected，two-tier hierarchy 的上界（incompleteness）可能是实验设计产物而非真实现象。 |
| Reproducibility | 3.5/5 | 模型、benchmark（τ²-bench）、统计方法均明确指定；Appendix 提供 replication 结果。但 clause pair 的具体生成模板和标注 guideline 未完整公开，合成歧义的质量控制流程缺少细节。 |
| Confidence | 4/5 | 仔细通读全文及附录，熟悉 ambiguity in NLP、agent safety evaluation、matched-pair experimental design 领域。 |

---

## Summary

本文研究 LLM agent 在自然语言策略规范下的安全风险，提出六类歧义的双层 taxonomy（linguistic: scopal, lexical, coreferential; specification: authorization scope, incompleteness, conditional precedence），构建 300 组 matched clause pairs 在 τ²-bench 上进行因果实验，发现歧义整体提升违规率 34.0 pp（OR = 15.1），但不同类型差异显著——incompleteness 普遍最危险（46-62%），authorization scope 受模型影响最大（12%-64%）。论文提出 "Differential Nocuity" 框架，主张歧义的安全风险取决于类型而非仅存在与否，并通过 disambiguation instruction 实验验证了 type-aware mitigation 的可行性。

---

## 主要优势（Strengths）

**S1. 严谨的因果实验设计。** Matched-pair design 是本文最大的方法论贡献。每对 clause pair（ambiguous vs. unambiguous）控制了 policy intent，使得违规率差异可归因于歧义本身而非 policy content 变化。这优于 DRIP-R（Borkakoty et al., 2026）的相关性设计，后者只能观察歧义存在与决策质量的相关性。Perturbation control（Section 4.5, Δ = −0.67 pp, TOST confirmed）进一步排除了 clause rewriting 本身的影响，是可信的方法论 safeguard。

**S2. Taxonomy 有双重理论基础。** 双层结构同时植根于 CL 文献（Li et al., 2024 的 NLP ambiguity taxonomy）和 RE 文献（Massey et al., 2014; Berry & Kamsties, 2004），且与 concurrent work DRIP-R（5 types）有清晰的区分。Section 3 对每种类型的操作性定义清晰，配有具体 policy clause 示例，使 taxonomy 可操作化。

**S3. 模型覆盖面广、含 replication。** 主研究覆盖 5 个架构多样的模型（GPT-5.4, GPT-4.1, Claude, Qwen3-235B, DeepSeek-V3），Appendix E 在 2 个额外模型族（Gemini 2.5-Flash, LLaMA-4-Scout）上 replicate 核心结果，增强了外部效度。

**S4. CL-first framing 适合 EMNLP。** 论文从语言学歧义分类入手，将 safety 作为 application context 而非反过来，Related Work（Section 2）对 psycholinguistic ambiguity processing 文献的覆盖（Ferreira et al., 2002; Frazier & Rayner, 1982; Levy, 2008; Liu et al., 2023）提供了有意义的理论连接，特别是 "Ambiguity Blindness"（Section 6.2）与 good-enough processing 的关联。

**S5. 统计分析充分。** 使用了 McNemar's test、Cramér's V、TOST equivalence testing（Lakens, 2017）、logistic regression with model×type interaction，方法选择得当。Appendix A 的 TOST sensitivity analysis 增加了可信度。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **主文超出 8 页限制**
- 具体位置：Page 8 → Page 9（Section 7 Discussion 跨页，Table 2 + Section 8 Conclusion 均在 Page 9）
- 问题：EMNLP 2026 规定 long paper 正文严格 8 页限制。Limitations 和 Ethics 不计入页数，但 Section 8 Conclusion 和 Table 2 属于正文。当前正文约 8.5-8.7 页，超限约 0.5-0.7 页。
- 为什么影响接收：ARR desk reject 标准之一。即使不 desk reject，也会被每位 reviewer 标记为格式违规。
- 建议修改方向：(1) Table 2 移至 Appendix（最直接，约省 1/3 页）；(2) Section 7 Discussion 压缩重复论述（"Why incompleteness resists safety training" 与 Section 5.1/5.4 有重叠）；(3) Introduction 的 contribution list 可以更简洁。

**N2** [critical] **Incompleteness 的 information-addition confound 未充分处理**
- 具体位置：Section 3（taxonomy 定义）、Section 5.1-5.2（结果）、Section 7（Discussion）、Limitations
- 问题：论文在 Section 3 承认 incompleteness 与其他 5 类本质不同——"unlike other types where the unambiguous variant replaces existing content, incompleteness resolution requires adding new policy content"。但在结果解读中仍将 incompleteness 与其他类型直接比较，得出其"universally dangerous"的结论。这存在根本性 confound：incompleteness 的高违规率可能是因为缺失信息（information absence）本身就导致错误，而非歧义（ambiguity）造成的。这与其他 5 类（原始文本存在但有多种解读）在机制上不同。
- Section 5.4 的 model×type interaction 分析（2.9% of variance）虽然控制了模型效应，但未分离 information-addition 的贡献。Appendix F 的 incompleteness confound analysis 提到 logistic regression 控制了 information delta，但报告只说"the effect remains significant after controlling"——缺少 effect size 的变化量（控制前后 OR 变了多少？）。
- 为什么影响接收：这是论文核心 claim（type hierarchy）的根基。如果 incompleteness 的领先地位是 confound 产物，two-tier structure 的解读就需要根本修改。
- 建议修改方向：(1) 报告控制 information delta 前后 OR 的变化量；(2) 在主文（非仅 Appendix）明确讨论这一 confound 对 type hierarchy 解读的限制；(3) 考虑将 incompleteness 从 type hierarchy 排序中分离，单独讨论。

**N3** [critical] **"Differential Nocuity" 框架缺乏形式化**
- 具体位置：Section 1（Contribution 列表）、Section 7（Discussion）、Abstract
- 问题：Abstract 和 Introduction 将 "Differential Nocuity" 作为本文的核心理论贡献之一，但全文没有给出形式化定义。它既不是一个 predictive model（不能预测新歧义类型的风险），也不是一个 prescriptive framework（不提供量化的风险评估方法）。实质上它是对实验发现的重新命名（"不同歧义类型有不同风险"→ "Differential Nocuity"），而不是一个独立的理论贡献。
- Section 7 虽然将其与 Berry & Kamsties (2004) 的 nocuous/innocuous 区分关联，但只是 extends 了一个二分法到类型维度，未提供新的理论机制。
- 为什么影响接收：过度包装（overclaiming）是 reviewer 常见的 concern。如果 framework 只是 findings 的别名，将其列为 contribution 会降低可信度。
- 建议修改方向：(1) 降级为 empirical finding 而非 framework——"our results reveal differential nocuity across ambiguity types"；(2) 或者真正形式化它——给出基于 type features 的 risk prediction model（即使是简单的 logistic model 也好）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **与 DRIP-R 的差异化论述不够有力**
- 具体位置：Section 2（Related Work, Policy specification for agents 段落）、Section 1（Introduction）
- 问题：DRIP-R（Borkakoty et al., 2026）是最近的 concurrent work，400 scenarios, 5 RE ambiguity types, retail domain。本文在 Section 2 用两句话说明差异——(1) matched-pair vs. correlational, (2) model×type interaction quantification。但对于 reviewer 和 AC 来说，需要更 explicit 的 contribution delta：DRIP-R 用 5 types 覆盖了哪些？本文的 6 types 哪些是新增的？两者 overlap 的 types 上结论是否一致？DRIP-R 没有做但本文做了什么（beyond matched-pair design）？
- 建议：在 Related Work 或 Introduction 增加一段对比表或详细文字说明，类似 "Compared to DRIP-R, our work differs in three respects: ..."

**W2** [warning] **Contribution 4 与 Contribution 1 重叠**
- 具体位置：Section 1, Introduction 末尾的 contribution list
- 问题：Contribution 1 是 "six-type taxonomy"，Contribution 4 是 "type-specific failure mode taxonomy revealing three mechanistically distinct failure patterns"。Section 6.3 的 failure mode analysis（structural misparse, information gap-filling, boundary violation）是有价值的，但它本质上是 taxonomy 的 downstream finding，而非独立 contribution。将其列为第四个 contribution 有 overclaiming 的风险。
- 建议：合并为 taxonomy + its mechanistic validation，或将 Contribution 4 降级为 "additionally, we identify ..."

**W3** [warning] **Human validation 细节不足**
- 具体位置：Section 4.4（Evaluation）、Appendix G（Per-Type Judge Agreement）
- 问题：Section 4.4 提到 "Two independent annotators (both with NLP background) labeled the same 100 stratified episodes on the four-tier severity scale"，得到 κ = 0.762（substantial）。但缺少以下关键信息：(1) 标注者的具体背景（NLP 研究者？研究生？众包？）；(2) 标注者是否了解 ambiguity taxonomy（即是否 blind to condition）；(3) disagreement 的分布——是均匀分布在各 severity level 之间，还是集中在某些 type 上？(4) 这 100 个 episode 的抽样策略（是否 stratified by type？by model？）。
- Appendix G 的 per-type agreement 数据很好（Table 9），但主文应至少提及 annotator blindness 和 stratification strategy。
- 建议：补充 1-2 句关于 annotator selection 和 blindness 的说明。

**W4** [warning] **Domain scope 限制未充分讨论**
- 具体位置：Limitations section（Page 9）
- 问题：实验完全基于 τ²-bench（retail + airline customer service），但 Limitations 只用一句话提及 domain scope。Policy ambiguity 在高风险领域（healthcare, finance, legal）的表现可能完全不同——这些领域的 policy 更复杂、多层嵌套、且有 legal consequences。论文未讨论 taxonomy 在这些 domain 是否适用（例如，medical policies 中的 incompleteness 可能不是最危险的，因为 default behavior 通常是 conservative）。
- 建议：在 Limitations 增加 2-3 句关于 domain generalizability 的讨论。

**W5** [warning] **部分引用信息有误**
- 具体位置：References
- 问题：引用验证发现以下问题：
  - `ferrari_defects_2018`：cite key 暗示 Ferrari 是第一作者，但 bib 条目的实际第一作者是 Rosadini, Benedetta（OpenAlex verified）。年份标注为 2019，但 cite key 写 2018。
  - `lassiter_goodman_2017`：OpenAlex 显示该 Synthese 论文的发表年份为 2015（online-first），bib 标注 2017。
  - `levy_expectation_2008`：OpenAlex 显示年份可能为 2007。
- 这些不影响论文实质，但在 camera-ready 前应修正。

---

## 小问题（不影响接收）

- Figure 1（Page 2）的 pipeline 图信息密度适中，但 "Policy Ambiguity Taxonomy" 框中的 6 types 文字太小，建议放大或用更大的 subfigure。
- Section 3 的 type 定义部分，coreferential 的示例（"the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor"）很好地展示了 "which" 的歧义，但可以补充一句说明为什么这不是 scopal ambiguity。
- Table 1（Page 6）的 Δpp 列使用了正负值但没有 color coding，建议用粗体或颜色标记 significant cells。
- "Ambiguity Blindness"（Section 6.2）是一个有趣的观察，但只有描述性统计（4.6% awareness, 85% surface adoption），缺少与 model capability 的关联分析。

---

## Missing References

以下相关工作未被引用，建议作者检查是否需要加入 Related Work：

1. **Agent-SafetyBench** (Zhang et al., 2024, arXiv:2412.14470) — 2000 test cases, 8 safety risk categories, 10 failure modes for LLM agents。与本文的 agent safety evaluation 部分高度相关，且提供了不同维度的 safety risk taxonomy，可以对比讨论。
2. **SafeAgentBench** (Yin et al., 2024, arXiv:2412.13178) — embodied agent safety benchmark, 750 tasks, 10 hazard types。虽然 domain 不同（embodied vs. conversational），但其 safety taxonomy 可能提供互补视角。
3. **AgentSpec** (Poskitt et al., ICSE 2026) — runtime enforcement for safe LLM agents，与本文的 practical implications（type-aware disambiguation）有直接关联，代表了从 detection 到 enforcement 的 pipeline。
4. **Word Sense Disambiguation 文献** — 论文的 lexical ambiguity type 与 WSD 文献有直接联系（polysemy, homonymy），但 Related Work 未引用任何 WSD 工作（如 Navigli, 2009 的 WSD survey）。对于 CL venue 这是一个覆盖空白。

---

## 引用真实性核查结果

使用 OpenAlex API 对全部 38 条引用进行了自动化验证：
- **27 条 verified**（标题、作者、年份均匹配）
- **7 条 not_found**（多为 tech report、workshop paper 或极新 arXiv，OpenAlex 未收录，但标题搜索确认存在）
- **4 条 mismatch**（详见 W5，均为 minor metadata 不一致）
- **0 条 orphan**（bib 中无未引用条目）
- **0 条 missing**（正文无未对应 bib 的 cite key）
- **未发现 fabricated citation。**

---

## 对 Director 指定审查维度的逐项回应

### 1. Taxonomy 合理性
双层结构（linguistic vs. specification）有合理的理论动机——linguistic types 对应语言本身的歧义（可通过纯文本分析检测），specification types 需要领域上下文才能识别。但 **authorization scope 的归类存疑**：Section 3 的示例 "authorized personnel may issue refunds" 中，"authorized personnel" 的歧义既可以是 lexical（vagueness，谁算 "authorized"？）也可以是 specification-level（policy 未指定哪些角色有权限）。论文选择后者，但未给出判据来区分边界情况。与 Li et al. (2024) 的区别是从 11 types 精选 6 types，但选择标准（"frequency in operational policy documents"）的具体数据（哪些 type 在 τ²-bench policies 中频率如何？）未提供。与 Massey et al. (2014) 的继承关系清晰（Section 3 有 explicit mapping），与 DRIP-R 的关系需要更多阐述（见 W1）。

### 2. 新颖性评估
**Differential Nocuity 的增量贡献**有限——实质是"不同歧义类型有不同风险"的实验验证，而非一个 predictive framework（见 N3）。**vs. DRIP-R**：matched-pair 因果设计 vs. 相关性设计是真实的方法论差异，但 DRIP-R 的 400 scenarios（本文 300 pairs）和 real-world retail policies（本文 synthetic injection on τ²-bench）各有优劣。**vs. PolicyBank / AgentPex**：差异化足够，这些工作关注 policy understanding 和 failure detection，而本文关注 ambiguity-safety 的因果关系。整体评估：**方法论新颖性中等偏上（matched-pair design），理论新颖性中等偏下（findings somewhat expected）**。

### 3. Related Work 覆盖
覆盖面总体良好，特别是对 concurrent work（DRIP-R, PolicyBank, AgentPex, MANTRA）的覆盖值得肯定。**空白**：(a) WSD 文献完全缺失（CL venue 的明显遗漏）；(b) Agent-SafetyBench / SafeAgentBench 等 2024 年底的 agent safety benchmarks 未引用；(c) AgentSpec 类 runtime enforcement 工作未提及。引用真实性检查通过，未发现 fabricated citation。

### 4. 论文叙事与结构
CL-first framing 适合 EMNLP，Introduction 的 claim 与 Results 基本一致。但有两个问题：(1) "Differential Nocuity framework" 在 Abstract/Introduction 中的呈现暗示了一个 formal framework，但实际只是 empirical observation 的命名；(2) 四个 contribution 中 C1（taxonomy）和 C4（failure mode taxonomy）有实质重叠。建议合并为三个更清晰的 contribution。

### 5. 格式合规
**主文超出 8 页限制**（见 N1），这是最紧迫的问题。ACL 模板使用正确（\documentclass[11pt]{article}, acl.sty）。匿名规则合规（\author{Anonymous ACL submission}）。Figure/Table 质量可接受，Figure 2 的 per-type effect visualization 清晰，但 Table 1 可以更紧凑。

### 6. Limitations 完整性
已覆盖：model coverage, domain scope, synthetic ambiguity, cross-judge asymmetry。**未覆盖的重要限制**：(1) incompleteness 的 information-addition confound（虽然 Appendix F 分析了，但 Limitations 未提及这一根本性问题）；(2) prompt sensitivity（结果对 system prompt 模板的敏感度）；(3) per-type 样本量较小（n = 32-34 per cell，Appendix 末尾提到但 Limitations 未讨论）；(4) τ²-bench 特定的 policy 结构对 generalizability 的限制。

---

## 评分建议

| 维度 | 分数 | 备注 |
|------|------|------|
| Overall Assessment | **3.5** | Borderline Conference。方法论扎实但核心发现新颖性受限，incompleteness confound 需要在主文充分处理 |
| Soundness | **3.5** | 主要 claim 有实验支撑，但 N2（incompleteness confound）影响 type hierarchy 结论的可信度 |
| Excitement | **3.0** | 选题及时，matched-pair 设计有方法论价值，但 "不同歧义类型有不同风险" 作为核心 insight 缺少惊喜 |
| Reproducibility | **3.5** | 基本可复现，但 clause pair 生成细节和标注 guideline 缺少 |
| Confidence | **4** | |

**升分路径**（从 3.5 → 4.0）：
1. 修复页数超限（N1）——必须
2. 在主文充分处理 incompleteness confound（N2），报告控制前后的 effect size 变化
3. 降低 "Differential Nocuity framework" 的 claim 级别（N3）
4. 补充 DRIP-R 的详细对比（W1）

**降分风险**（3.5 → 3.0）：
- 如果 page limit violation 被其他 reviewer 标记为 desk reject 风险
- 如果 incompleteness confound 被认为根本性地破坏了 type hierarchy 的解读

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

_source line 596 · 2026-05-21T15:41:21.435026+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 主文超出 8 页限制\n- Section 7 Discussion 跨页到 Page 9，Table 2 + Section 8 Conclusion 均在 Page 9\n- 正文约 8.5-8.7 页，超限约 0.5-0.7 页\n- ARR desk reject 标准之一\n- 建议：Table 2 移至 Appendix（省约 1/3 页）；Discussion 压缩重复论述\n\n**N2** [critical] Incompleteness 的 information-addition confound 未充分处理\n- incompleteness 与其他 5 类本质不同——resolution requires adding new policy content\n- 高违规率可能是 information absence 本身导致错误，而非歧义\n- Appendix F 的 logistic regression 只说 \"effect remains significant after controlling\"，缺少 effect size 变化量（控制前后 OR 变了多少？）\n- 建议：(1) 报告控制前后 OR 变化量；(2) 在主文明确讨论 confound 对 type hierarchy 解读的限制；(3) 考虑将 incompleteness 从排序中分离\n\n**N3** [critical] \"Differential Nocuity\" 框架缺乏形式化\n- 全文没有给出形式化定义\n- 既不是 predictive model，也不是 prescriptive framework\n- 实质是对实验发现的重新命名\n- 建议：降级为 empirical finding，或真正形式化\n\n### Should-Fix 问题\n\n**W1** 与 DRIP-R 的差异化论述不够有力——需要更 explicit 的 contribution delta\n**W2** Contribution 4（failure mode taxonomy）与 Contribution 1 重叠——建议合并\n**W3** Human validation 细节不足——缺少 annotator blindness、disagreement 分布\n**W4** Domain scope 限制未充分讨论——healthcare/finance/legal 可能完全不同\n**W5** 部分引用信息有误——ferrari_defects_2018 第一作者实际是 Rosadini；lassiter_goodman_2017 年份可能是 2015\n\n### Missing References\n- Agent-SafetyBench (Zhang et al., 2024)\n- SafeAgentBench (Yin et al., 2024)\n- AgentSpec (Poskitt et al., ICSE 2026)\n- WSD survey (Navigli, 2009) — CL venue 的明显遗漏\n\n### Excitement 评分\nR2 给了 Excitement 3.0/5，认为核心发现 \"不同歧义类型有不同风险\" 较为 expected，two-tier hierarchy 的上界可能是实验设计产物。\n\n---\n\n请逐条回应。"
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
    "project": "policy_ambiguity_safety",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 主文超出 8 页限制\n- Section 7 Discussion 跨页到 Page 9，Table 2 + Section 8 Conclusion 均在 Page 9\n- 正文约 8.5-8.7 页，超限约 0.5-0.7 页\n- ARR desk reject 标准之一\n- 建议：Table 2 移至 Appendix（省约 1/3 页）；Discussion 压缩重复论述\n\n**N2** [critical] Incompleteness 的 information-addition confound 未充分处理\n- incompleteness 与其他 5 类本质不同——resolution requires adding new policy content\n- 高违规率可能是 information absence 本身导致错误，而非歧义\n- Appendix F 的 logistic regression 只说 \"effect remains significant after controlling\"，缺少 effect size 变化量（控制前后 OR 变了多少？）\n- 建议：(1) 报告控制前后 OR 变化量；(2) 在主文明确讨论 confound 对 type hierarchy 解读的限制；(3) 考虑将 incompleteness 从排序中分离\n\n**N3** [critical] \"Differential Nocuity\" 框架缺乏形式化\n- 全文没有给出形式化定义\n- 既不是 predictive model，也不是 prescriptive framework\n- 实质是对实验发现的重新命名\n- 建议：降级为 empirical finding，或真正形式化\n\n### Should-Fix 问题\n\n**W1** 与 DRIP-R 的差异化论述不够有力——需要更 explicit 的 contribution delta\n**W2** Contribution 4（failure mode taxonomy）与 Contribution 1 重叠——建议合并\n**W3** Human validation 细节不足——缺少 annotator blindness、disagreement 分布\n**W4** Domain scope 限制未充分讨论——healthcare/finance/legal 可能完全不同\n**W5** 部分引用信息有误——ferrari_defects_2018 第一作者实际是 Rosadini；lassiter_goodman_2017 年份可能是 2015\n\n### Missing References\n- Agent-SafetyBench (Zhang et al., 2024)\n- SafeAgentBench (Yin et al., 2024)\n- AgentSpec (Poskitt et al., ICSE 2026)\n- WSD survey (Navigli, 2009) — CL venue 的明显遗漏\n\n### Excitement 评分\nR2 给了 Excitement 3.0/5，认为核心发现 \"不同歧义类型有不同风险\" 较为 expected，two-tier hierarchy 的上界可能是实验设计产物。\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-21T15:41:43.884008+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22448
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-21T15:41:44.085282+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "policy_ambiguity_safety",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Authorization scope 测量可靠性过低，无法支撑 \"canary type\" 主张\n- cross-judge κ=0.385（fair），是所有类型中最低\n- Human-LLM agreement 95% CI [0.35, 0.91]，极宽\n- Per-type 验证样本仅 n=34\n- Within-judge comparison 仍依赖同一 judge（GPT-5.4）的 type-level 判断一致性\n- 建议：增加 auth scope human validation 样本；在 Abstract/Conclusion 加 measurement-uncertainty caveat\n\n**N2** [critical] Judge-model confounding 未被充分处理\n- 每个 agent model 由单一 judge 评估，judge identity 与 model identity 完全 confounded\n- dual-judge calibration (n=100) 只能在 aggregate level 排除 systematic bias\n- GPT-4.1（mid-tier）judging GPT-5.4（frontier）存在能力不对称\n- C3 在 within-judge-group 分析中均未达显著性\n- 建议：对所有 5 个 model 用两个 judge 分别评估 subset\n\n**N3** [critical] 缺少 a priori power analysis\n- 50 pairs/type 的选择未论证\n- TOST equivalence testing 的 null 结果可信度取决于功效\n- per-type per-model cells (n=50) 的小计数估计不稳定\n- 建议：报告 post-hoc power analysis\n\n### Should-Fix 问题\n\n**W1** Incompleteness confound 的 hedging 在 Abstract/Conclusion 中不够显著\n**W2** TOST SESOI ±15pp 的选择缺乏外部锚定——sensitivity analysis 显示 ±10pp 时仅 3/6 mid-tier pairs equivalent\n**W3** ICC=0.919 仅限 OpenAI 模型内部，cross-provider 可复现性未知\n**W4** Mitigation experiment (Table 2) 样本量过小却在主文占重要位置——建议移至 Appendix\n**W5** Failure mode taxonomy 的 inter-coder reliability 偏低（Cohen's κ=0.52）\n\n### Strengths（R1 特别肯定的方面）\n1. Matched-pair causal design 是最大方法论贡献\n2. 统计分析全面且恰当\n3. 主动承认混淆和局限的 intellectual honesty\n4. 5+2 模型跨 6 provider 的 cross-architecture replication\n5. Practical framework（mitigation + detection experiments）\n\n### R1 给出的 Questions\n- Q1: 50 pairs/type 的决定依据？\n- Q2: Per-model judge agreement 分布？\n- Q3: Logistic regression 具体控制了哪些变量？\n- Q4: Template-based pipeline 的 structural correlation？\n- Q5: 3 episodes API error 是否引入 selection bias？\n- Q6: C3 inconclusive 保留在主文的理由？\n\n---\n\n请逐条回应。"
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
    "project": "policy_ambiguity_safety",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Authorization scope 测量可靠性过低，无法支撑 \"canary type\" 主张\n- cross-judge κ=0.385（fair），是所有类型中最低\n- Human-LLM agreement 95% CI [0.35, 0.91]，极宽\n- Per-type 验证样本仅 n=34\n- Within-judge comparison 仍依赖同一 judge（GPT-5.4）的 type-level 判断一致性\n- 建议：增加 auth scope human validation 样本；在 Abstract/Conclusion 加 measurement-uncertainty caveat\n\n**N2** [critical] Judge-model confounding 未被充分处理\n- 每个 agent model 由单一 judge 评估，judge identity 与 model identity 完全 confounded\n- dual-judge calibration (n=100) 只能在 aggregate level 排除 systematic bias\n- GPT-4.1（mid-tier）judging GPT-5.4（frontier）存在能力不对称\n- C3 在 within-judge-group 分析中均未达显著性\n- 建议：对所有 5 个 model 用两个 judge 分别评估 subset\n\n**N3** [critical] 缺少 a priori power analysis\n- 50 pairs/type 的选择未论证\n- TOST equivalence testing 的 null 结果可信度取决于功效\n- per-type per-model cells (n=50) 的小计数估计不稳定\n- 建议：报告 post-hoc power analysis\n\n### Should-Fix 问题\n\n**W1** Incompleteness confound 的 hedging 在 Abstract/Conclusion 中不够显著\n**W2** TOST SESOI ±15pp 的选择缺乏外部锚定——sensitivity analysis 显示 ±10pp 时仅 3/6 mid-tier pairs equivalent\n**W3** ICC=0.919 仅限 OpenAI 模型内部，cross-provider 可复现性未知\n**W4** Mitigation experiment (Table 2) 样本量过小却在主文占重要位置——建议移至 Appendix\n**W5** Failure mode taxonomy 的 inter-coder reliability 偏低（Cohen's κ=0.52）\n\n### Strengths（R1 特别肯定的方面）\n1. Matched-pair causal design 是最大方法论贡献\n2. 统计分析全面且恰当\n3. 主动承认混淆和局限的 intellectual honesty\n4. 5+2 模型跨 6 provider 的 cross-architecture replication\n5. Practical framework（mitigation + detection experiments）\n\n### R1 给出的 Questions\n- Q1: 50 pairs/type 的决定依据？\n- Q2: Per-model judge agreement 分布？\n- Q3: Logistic regression 具体控制了哪些变量？\n- Q4: Template-based pipeline 的 structural correlation？\n- Q5: 3 episodes API error 是否引入 selection bias？\n- Q6: C3 inconclusive 保留在主文的理由？\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-21T15:41:45.393207+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1307
}
```

</details>

---


### Assistant

_source line 600 · 2026-05-21T15:41:50.051469+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 55

## Round 55

2 recorded events


### User

_source line 601 · 2026-05-21T15:41:52.550805+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference）。三个 critical 问题：(1) 主文超 8 页限制约 0.5-0.7 页；(2) incompleteness 类型的 information-addition confound 未在主文充分处理，影响 two-tier hierarchy 核心结论的可信度；(3) "Differential Nocuity" 被包装为 framework 但实质只是实验发现的命名。四个 warning 级问题涉及 DRIP-R 差异化不足、contribution 列表重叠、human validation 细节缺失、domain scope 讨论不足。引用核查通过，未发现 fabricated citation，有少量 metadata 不一致。升分路径明确——修复页数、正面处理 confound、降低 framework claim 即可推至 4.0。

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

_source line 602 · 2026-05-21T15:41:57.811609+00:00_

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


## Round 56

## Round 56

2 recorded events


### User

_source line 603 · 2026-05-21T15:43:50.702278+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

## Must-Fix 问题

### [AGREE] R2-N1: 主文超出 8 页限制
同意。PDF 显示主文（Abstract → Conclusion）约 8.5-8.7 页，超限。Table 2（mitigation experiment, ~50/cell, preliminary）移至 Appendix 可节省约 1/3 页，同时改善论证质量——我在自己的 W4 中也指出该实验样本量不足以放在主文。Discussion 中 "upper bound whose ranking partly reflects an information-addition confound" 几乎逐字重复 ≥4 次，压缩重复措辞可进一步节省空间。

### [AGREE with nuance] R2-N2: Incompleteness confound
部分同意。R2 要求报告控制前后 OR 变化量是合理的——Appendix F 仅说 "coefficient change < 8%" 但无 OR 对比。在 Abstract/Conclusion 中加强 hedging 也是必要的。

但不完全同意 critical 定级。论文已有多项控制：§3 预先标注结构特殊性、§5.2 明确称 "upper bound"、coreferential 作为 confound-free lower bound (31.6%, information delta = 0)、Appendix F logistic regression 控制 token delta 后仍显著 (p=0.022)。核心问题是**呈现方式**（Abstract/Conclusion 的 "universally dangerous" 措辞过于强势）而非分析缺失。

### [REBUT] R2-N3: "Differential Nocuity" 缺乏形式化
不同意此为 critical issue。该框架提供三层组织原则：(1) 扩展 Berry & Kamsties (2004) 的二分法到 LLM agents（§7）；(2) 连接类型特异性与消歧渠道可用性（§7 "Why incompleteness resists safety training"——auth scope 有 RLHF 拦截点, incompleteness 无 decision point）；(3) 引出 systematic nocuity 概念（§6.3, 41.3% majority-convergent violations）。NLP 顶会中许多广泛引用的框架（如 "good-enough processing"）同样是 conceptual organizing principles 而非 formal models。要求 predictive/prescriptive 形式化对实证论文标准过高。建议作者在 §7 开头用 2-3 句话更明确阐述框架组成部分即可。

## Should-Fix 问题

### [AGREE partially] R2-W1: 与 DRIP-R 差异化
§2 已指出两个差异（causal design vs correlation; model×type quantification），满足 concurrent work 的最低要求但可改善。

### [REBUT] R2-W2: Contribution 3 与 Contribution 1 重叠
不同意。Contribution 1（因果定量: "是否/多大程度"）和 Contribution 3（failure mode taxonomy: "通过什么机制"）方法论完全不同（统计检验 vs 614 traces coding），结论层次也不同。

### [AGREE] R2-W3: Human validation 细节不足
同意。缺少 annotator blindness、disagreement distribution、resolution 策略。

### [REBUT] R2-W4: Domain scope 限制
不同意。Limitations 已专段讨论，含 within-study cross-domain evidence。EMNLP 2026 Limitations 章节仅需 ~3 个点，当前覆盖已足够。

### [AGREE] R2-W5: 引用信息有误
同意。我的引用验证也发现了 ferrari_defects_2018（first author mismatch）和 lassiter_goodman_2017（年份可能为 2015）的问题。

## Missing References
Navigli (2009) WSD survey 可在 §2 补充。其他 agent safety benchmarks（Agent-SafetyBench, SafeAgentBench）属于同类引用，论文已有 5 个同类引用，非必需。AgentSpec 需确认与 policy ambiguity 的相关性。

## Excitement 评分
R2 给 3.0，我给 4.0。核心分歧：R2 认为 "类型差异" 是 expected finding，但论文贡献不是发现差异本身，而是首次用 matched-pair design 建立因果关系。Several findings 是 genuinely surprising：incompleteness 普遍性（46-62% across 7 models）、Ambiguity Blindness（Qwen3/DeepSeek 0% awareness）、auth scope 的 systematic permissiveness bias（69.2% unauthorized escalation, 0% conservative refusal, p < 10⁻⁴）。去掉 incompleteness 后，5 类型间 pairwise contrasts 仍有结构（auth scope/lexical 显著高于 coreferential, Appendix F），tier structure 不完全依赖 incompleteness。

## 综合评估
R2 的 N1（page limit）和 W5（citation errors）完全正确，需修复。N2（incompleteness confound）的呈现问题需改善但分析基础已在。N3（形式化要求）标准过高。整体上 R2 的审稿在格式和引用细节上敏锐，但对论文已有方法论控制的认可不足。

我维持 Overall 3.5，Soundness 3.5，Excitement 4.0。


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

_source line 604 · 2026-05-21T15:43:56.460730+00:00_

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


## Round 57

## Round 57

2 recorded events


### User

_source line 605 · 2026-05-21T15:43:59.176905+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。总结：

- **N1 (page limit)**: [AGREE] — 主文确实超限，Table 2 应移至 Appendix
- **N2 (incompleteness confound)**: [AGREE with nuance] — 呈现方式需改善，但分析控制已在
- **N3 (Differential Nocuity 形式化)**: [REBUT] — 对实证论文要求 formal model 标准过高
- **W1-W5**: W1 部分同意、W2 反驳、W3 同意、W4 反驳、W5 同意
- **Excitement**: 维持 4.0/5，反驳 R2 的 3.0——首个 causal study 加上多个 genuinely surprising findings

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

_source line 606 · 2026-05-21T15:44:03.928668+00:00_

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


## Round 58

## Round 58

14 recorded events
