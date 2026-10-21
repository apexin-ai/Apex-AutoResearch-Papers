---
round: 2
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T06:58:57.688101+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 3 (Fresh)

**论文**: "Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families"
**Venue**: EMNLP 2026 via ARR May cycle (截止 2026-05-25)
**Reviewers**: R1 (方法严谨性, 3.5/5), R2 (新颖性与完整性, 3.5/5)
**Director Overall**: **3.0 / 5 (Findings)**

---

## Summary

本文研究不同类型的策略歧义如何影响 LLM agent 的安全违规率。采用 matched-pair 设计，在 τ²-bench（零售/航空客服场景）上构造 300 对歧义/无歧义条款，覆盖六类歧义（两层 taxonomy：linguistic 层 3 类 + specification 层 3 类），评估五个模型（GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3），共 2,997 episodes。提出四个 claims：C1（歧义普遍增加 34.0pp 违规率，OR=15.1），C2（三层类型层级，Cramér's V=0.137），C3（linguistic/specification 层级区分不显著，inconclusive），C4（模型×类型交互效应）。附带 perturbation control、error analysis（614 traces, 5 failure modes）、Ambiguity Blindness 量化（<11% awareness）和消歧指令缓解实验（1,256 episodes）。

---

## Strengths

**S1** [Consensus] **Matched-pair causal design 是方法论贡献**：perturbation control (Δ_perturb=3.33pp vs Δ_ambig=34.0pp) + TOST equivalence + variance decomposition + ICC reproducibility 的组合在 agent safety benchmarking 中几乎没有先例。论文的因果推断设计显著优于同期工作（DRIP-R: correlation only, PolicyBank: no matched design）。

**S2** [Consensus] **C1 和 C2 有压倒性统计支撑**：C1 (p < 10⁻¹⁰⁵, OR=15.1, bootstrap CI [31.2, 36.9]) 和 C2 (p = 3.6 × 10⁻⁵, V=0.137, power=0.993) 的证据强度远超审稿接受阈值。variance decomposition 发现 clause identity 解释 22.4% vs model identity 仅 1.0%，是重要的实践洞察。

**S3** [Consensus] **Authorization scope "canary type" 发现有独特实践价值**：Claude 12% vs GPT-5.4 64%（52pp 跨模型范围）直接揭示了不同 safety training 策略的差异化效果——但此结论受 cross-judge confound 影响（见 MF1）。

**S4** [Consensus] **Claim 层级透明**：C3 显式标记为 inconclusive，Holm-Bonferroni 校正后 C3 不通过。logistic regression 控制 token delta 后层级项翻转。这种方法论诚实度在该领域不常见。

**S5** [Consensus] **Error analysis 提供机制洞察**：三种机制模式（structural misparse, information gap-filling, boundary violation）跨越 specification/linguistic 层级边界，3/6 类型全模型一致、6/6 多数一致。Ambiguity Blindness 的量化 (<11% awareness, >88% surface adoption) 虽概念上不意外但首次在 agent safety context 中给出具体数字。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [Critical — Consensus] **Cross-judge confound 缺乏校准数据**

GPT-5.4 评判 Claude/Qwen3/DeepSeek；GPT-4.1 评判 GPT-5.4。Judge identity 与 model identity 完全混淆。论文最引人注目的发现——authorization scope Claude 12% vs GPT-5.4 64%（Table 1）——跨越 judge boundary（Claude 由 GPT-5.4 评判，GPT-5.4 由 GPT-4.1 评判）。无法区分 GPT-5.4 的 vulnerability profile 是模型特性还是 GPT-4.1 检测能力差异的 artifact。论文未提供任何 inter-judge calibration 数据。Within-judge analysis 仅能确认 C1 在两个子群中一致，无法量化 judge bias 方向和大小。

*R1-N3 和 R2-N2 独立识别；交叉后两人 AGREE。*

**要求**: (a) 在 ≥100 episodes 上做 human evaluation 建立 LLM-human agreement baseline；(b) 和/或让 GPT-5.4 和 GPT-4.1 同时评判同一批 traces 量化 judge bias；(c) 在 §4.4 正式讨论 confound 影响。

---

**MF2** [Critical — Consensus] **Human evaluation baseline 完全缺失**

核心指标（binary violation/no-violation + four-tier severity）的 2,997 episodes 全部由 LLM judge 产生，无任何 human-LLM agreement 数据。§4.2 的 clause pair 质量有双人审核，§6 的 failure mode 有 LLM-LLM agreement (AC₁=0.62, κ=0.52)——但论文最核心的违规判定缺乏人类校准。R-Judge (EMNLP 2024 Findings) 和 ToolEmu (ICLR 2024)——论文引用的同领域工作——均包含 human evaluation baseline。纯 LLM-as-judge 且无人类校准低于 EMNLP agent safety 的当前社区标准。

*R2-N3 提出为 Must-Fix；R1 交叉后从 W2 升级同意。*

**要求**: 对 ≥100 episodes（stratified by type × severity）做 human annotation，报告 human-LLM agreement (Cohen's κ)。

---

**MF3** [Critical — Consensus] **Incompleteness confound 未充分解决**

Incompleteness 的无歧义变体必然添加新的策略信息（边界条件、例外规则），而非仅消解歧义。这违反了 §4.2 matched-pair 设计的第二条质量标准（"eliminates that ambiguity without introducing new information that changes the policy's scope"）。Incompleteness 驱动了 C2 三层层级的顶层（53.6%）、Systematic Nocuity 的 24% universal convergence、以及 "universally dangerous" 的核心叙事。论文在 Limitations 中用 token delta logistic regression 处理（β→−0.10, p=0.384 after controlling token delta），但 token count 是信息内容的极粗糙代理。一条添加全新退货排除规则的条款，其信息增量远超同等 token 数量的词汇替换。排除 incompleteness 后，5-type omnibus p=0.079（不显著），三层层级可能坍缩为两层（auth scope vs coreferential 仍显著，p_adj=0.039）。

*R1-N2 提出为 Must-Fix；R2 交叉后从 W1 升级同意。*

**要求**: (a) 在 §5.2 报告结果处立即讨论 confound，不得仅放 Limitations；(b) 报告含/不含 incompleteness 两版 C2 分析；(c) 考虑将 incompleteness 重新定义为 "missing policy content"（与其他 5 类性质不同）；(d) camera-ready 中增加 information-addition control。

---

**MF4** [Critical — Consensus] **C4 (model×type interaction) 作为 primary claim 证据不足**

Model×type interaction 仅解释 2.9% 方差（η²=0.026）。R1 从统计角度指出效应量过小无法与 C1 (p < 10⁻¹⁰⁵) 和 C2 (V=0.137, p < 10⁻⁵) 并列为 primary claim。R2 从 framing 角度指出 Abstract "jointly determine" 暗示 model 和 type 贡献相当，与实际不符。

*Director 对 p 值分歧的裁决*：R1 声称 F(12)=1.97, p=0.075；论文报告 F(20)=1.97, p=0.006。正确 df = (5−1)(6−1) = 20，R1 使用了错误的 df。论文报告的 p=0.006 在给定 df 下是自洽的。**但两位 Reviewer 一致认为，无论 p 值如何，2.9% 的方差解释量不足以支撑 primary claim 地位。**

*R1-N1 和 R2-W5 从不同角度提出；交叉后两人 AGREE。*

**要求**: (a) 将 C4 降级为 exploratory（与 C3 同级）；(b) Abstract "jointly determine" → "type primarily determines severity, with a smaller but significant model×type interaction"；(c) §1 贡献列表中不再将 C4 与 C1/C2 并列。

---

### Should-Fix（影响评分但不一票否决）

**SF1** [Warning — Consensus] **TOST ±15pp margin 缺乏 domain-specific 依据**
七个 margin 的敏感性分析（Appendix A）是好做法，但 primary margin ±15pp 无理论论证。基线 ~30-40% 下 ±15pp 意味着 15-55% 均为 "等价"——过于宽松。Lakens (2017) 要求 SESOI (Smallest Effect Size of Interest) 论证。

**SF2** [Warning — Consensus] **Error analysis LLM 编码器未经人类验证**
Gwet's AC₁=0.62, Cohen's κ=0.52 为 LLM-LLM agreement，非 LLM-human。AC₁=0.62 处于 "substantial" 下界，minority failure modes 可靠性可能更低。§6.1-6.2 的 type-specific failure signatures 完全基于此。

**SF3** [Warning — Consensus with qualification] **Perturbation control 检验力有限**
n=120 (24/model), MDE≥15pp, CI [-5.0, 13.3]。Worst-case 下 surface perturbation 可解释 13.3/34.0 ≈ 39% 的主效应。C1 在任何合理假设下仍成立（残余效应 ≥20.7pp），但因果归因的精度受限。

**SF4** [Warning — Consensus] **ICC 子集代表性不明**
30/300 clause pairs (10%), 2/5 models (40%), ICC=0.919。未披露选择了哪 2 个模型。Cross-architecture reproducibility 声明受限。

**SF5** [Warning — Consensus] **Mitigation 结果被低估**
Table 3 (Appendix B) 包含高价值发现：DeepSeek 反向效果 (+2/+4 pp, 消歧指令反而增加违规)、Claude auth scope floor effect (Δ=0)、GPT-5.4 dramatic response (−40pp)。这些直接支撑 Differential Nocuity 的实践含义但被完全推入 appendix，§7 仅一句话提及。

**SF6** [Warning — Consensus] **Taxonomy framing 不精确**
§3 input taxonomy (6 types, curated from literature) 和 §6 output taxonomy (5 failure modes, empirically discovered) 使用相同术语 "taxonomy"，易混淆。§1 Contribution 3 应强调 failure mode taxonomy 为研究发现，非 input taxonomy。

**SF7** [Warning — Partial Consensus] **Related Work 遗漏**
- Hu et al. (2025) "Ambiguity in LLMs is a concept missing problem" — 与 §6.3 Ambiguity Blindness 直接相关 [两人同意]
- Cohen (1960) / Gwet (2014) 统计原始文献 — κ 和 AC₁ 的引用规范 [两人同意]
- DRIP-R 方法论对比不够详细 — 最直接的 concurrent work 应有更系统比较 [两人同意]
- OpenAgentSafety (ICLR 2026) — 如涉及 policy compliance 维度则值得一提 [R2 提出，R1 conditional agree]

**SF8** [Warning — R1 识别，R2 反驳，Director 裁决 R1 正确] **正文超过 8 页限制**
§7 Discussion 从 page 8 延续到 page 9，§8 Conclusion 完全在 page 9。视觉审查 Agent 独立确认："Discussion 从 page 8 延续到 page 9，Conclusion 在 page 9 中部"。EMNLP 2026 Long paper 正文（Abstract 到 Conclusion）严格 8 页。**R2 反驳不成立，论文超页。**

---

### Minor（不影响接收）

- M1: 引用 minor mismatches — Lassiter & Goodman (2017 vs 2015), Levy (2008 vs 2007), ferrari_defects_2018 first author Rosadini [R1/R2 均识别，无虚构引用]
- M2: Table 3 排除 coreferential 未解释原因
- M3: 标题 "LLM Agent Families" 仅覆盖 5 个模型，"families" 措辞略显夸大
- M4: "Nocuous" 对 EMNLP 读者可能不熟悉，首次使用时加释义
- M5: Figure 1 内文字偏小，打印可读性可能受影响
- M6: Figure 3 heatmap 建议改为 figure*（全宽）提升可读性

---

## Reviewer Consensus

两位 Reviewer 独立评审后在以下关键问题上达成完全共识：

| 问题 | R1 | R2 | 交叉后 |
|------|-----|-----|--------|
| Cross-judge confound | N3 (Must-Fix) | N2 (Must-Fix) | 双方 AGREE |
| Human eval baseline | W2 → 升级 | N3 (Must-Fix) | R1 升级同意 |
| Incompleteness confound | N2 (Must-Fix) | W1 → 升级 | R2 升级同意 |
| C4 降级 | N1 (Must-Fix) | W5 (Should-Fix) | 双方 AGREE (互补角度) |
| TOST margin | W1 | AGREE | 共识 |
| Error analysis validation | W2 | AGREE | 共识 |
| Perturbation power | W3 | AGREE w/ qualification | 基本共识 |
| ICC representativeness | W4 | AGREE | 共识 |
| Mitigation underexploited | — | W2 → R1 AGREE | 共识 |
| Taxonomy framing | — | W3 → R1 AGREE | 共识 |

---

## Reviewer Divergence

| 问题 | R1 | R2 | Director 裁决 |
|------|-----|-----|---------------|
| R2-N1: Abstract "500 pairs" | **REBUT** — 原文为 "300" | Must-Fix | **R1 正确，R2 事实前提错误，排除** |
| 页数合规 (R1-W5) | Should-Fix (超页) | **REBUT** — 合规 | **R1 正确，视觉审查确认超页** |
| C4 p-value | F(12)=1.97, p=0.075 | 论文 F(20)=1.97, p=0.006 自洽 | **R2 正确 (df=20)，但效应量结论一致** |
| Related work 引用量 | 33 条足够 | 33 条偏少 | **R1 正确，数量非评审标准** |

---

## Questions for Authors

1. 是否可行在 ~100 episodes 上做 dual-judge evaluation (GPT-5.4 + GPT-4.1 评判同一批 traces)？如果 GPT-4.1 对 GPT-5.4 系统性偏严/偏松，C4 中 GPT-5.4 的 vulnerability profile 结论如何修正？
2. 排除 incompleteness 后，remaining 5 types 的 between-type 差异是否仍显著？Authorization scope (41.6%) vs coreferential (31.6%) 的层级差异是否保持？
3. TOST primary margin ±15pp 的选择依据是什么？能否提供 domain-grounded SESOI 论证（如 "对策略合规而言，15pp 差异在部署中可接受/不可接受"）？
4. Table 3 中 DeepSeek 的反向效果（消歧指令反而增加违规 +2/+4 pp）有无机制解释？是否与其 zero disambiguation awareness 相关——不识别歧义的模型收到消歧指令时行为退化？
5. Perturbation control CI 上界 13.3pp 意味着最高 39% 的主效应可能来自 surface perturbation。扩大至 n=300 (MDE ~9pp) 是否能实质性收紧因果归因？

---

## Missing References

**需补充** [共识]:
- Hu et al. (2025) "Ambiguity in LLMs is a concept missing problem" — 与 §6.3 Ambiguity Blindness 直接相关
- Cohen, J. (1960) "A coefficient of agreement for nominal scales" — κ 原始文献
- Gwet, K.L. (2014) "Handbook of Inter-Rater Reliability" — AC₁ 原始文献

**建议考虑** [部分共识]:
- OpenAgentSafety (ICLR 2026) — 如涉及 policy compliance 维度
- Prompt sensitivity 文献 (e.g., EMNLP 2024 Findings) — 建立 perturbation control 与 prompt sensitivity 研究的联系

---

## External Review (Stanford Agentic Reviewer)

**状态: 已跳过 (skipped)**。外部审稿请求已发送但用户选择不提交。本报告仅基于内部两位 Reviewer 的圆桌审稿。

---

## Visual Layout Check（非评分项）

**状态: 已完成**。4 warnings, 6 info-level findings。

主要发现：
- **[Warning]** Pages 3–5 连续 3 页纯文本（Related Work → Taxonomy → Method），无 figure/table 打断。§3 Taxonomy 建议增加层级图或摘要表。
- **[Warning]** Pages 8–9 连续纯文本（Error Analysis 后半 + Discussion + Conclusion + Limitations），无视觉元素。
- **[Warning]** 末页（p.12）仅 ~35% 填充，底部大面积空白。
- **[Warning]** 主体 9 页仅 4 个 display items（3 figures + 1 table），密度偏低。建议增加 taxonomy 汇总表或 mitigation 可视化。
- **[Info]** Figure 1 内文字偏小；Figure 3 heatmap 建议改 figure*；Table 1 未对最优值加粗；主体正文确认延伸至第 9 页。

---

## Overall Assessment

### 评分: 3.0 / 5 (Findings)

### Rationale

**C1（+34.0 pp, OR=15.1）和 C2（V=0.137, 三层层级）有压倒性统计支撑**，matched-pair causal design + perturbation control 在 agent safety benchmarking 中构成方法论贡献。这些结果足以支撑 Findings 级别发表。

**但四个共识性 Must-Fix 问题共同阻碍 Conference 级别**：

1. **Cross-judge confound** 使所有涉及 GPT-5.4 的跨模型比较不可靠——而 C4 和 "canary type" 发现正是基于跨模型比较
2. **无 human evaluation baseline** 低于 EMNLP agent safety 社区当前标准（R-Judge/ToolEmu 均有）
3. **Incompleteness confound** 影响 C2 顶层和 "universally dangerous" 核心叙事——排除后三层可能坍缩为两层
4. **C4 仅解释 2.9% 方差**，不足以作为 primary claim 与 C1/C2 并列

**论文标题 "Differential Vulnerability Profiles Across LLM Agent Families" 的承诺本质上依赖 C4**——如果模型间差异不是 primary finding，标题承诺就无法兑现。

两位 Reviewer 均给出 **3.5 (Borderline Conference)**，并认为修复 Must-Fix 后可达 4.0。Director 综合评估后下调 0.5 至 **3.0 (Findings)**，理由：
- 标题承诺（differential profiles）与 C4 证据强度之间存在实质性 gap
- 缺乏 human evaluation 在 EMNLP venue 的严重性
- Cross-judge confound 影响论文最有辨识度的发现（auth scope canary type）

### 修订路径

**如果作者完成以下修订，预估可达 3.5–4.0（Borderline Conference → Conference）**：
- [ ] Human evaluation 校准数据（≥100 episodes, human-LLM κ）
- [ ] Inter-judge calibration 或 dual-judge subsample
- [ ] C4 降级为 exploratory，修改标题和 Abstract 措辞
- [ ] §5.2 正文中处理 incompleteness confound（含/不含两版 C2）
- [ ] 压缩正文至 8 页
- [ ] 补充 missing references (Hu et al. 2025, Cohen 1960, Gwet 2014)

**Confidence: 4/5**

---

## Detailed Comments

### §1 Introduction
- Opening anecdote ($200 loss from scopal ambiguity) 有效吸引读者
- "no existing study provides a causal, type-granularity mapping" 是准确的 gap statement
- Contribution 2 中 C4 不应与 C1/C2 并列——改为 "suggestive model-specific variation"
- Contribution 3 应区分 input taxonomy (curated) 和 failure mode taxonomy (discovered)

### §2 Related Work
- 三个交叉领域（CL ambiguity, RE, agent safety）覆盖良好，篇幅控制恰当
- DRIP-R 差异化讨论存在但方法论对比不够详细
- 缺 Hu et al. (2025)、Cohen (1960)、Gwet (2014)

### §3 Taxonomy
- 两层六类组织清晰，例子具体
- Wasow (2005) operational definition 和 vagueness 包含 (Kennedy 2007) 论证充分
- **缺视觉呈现**——taxonomy diagram 或 summary table 对读者理解至关重要

### §4 Method
- §4.2 matched-pair 设计是全文最强方法论贡献——三条质量标准、双人审核、迭代修正
- §4.4 cross-judge 设计：confound 应在此处正式讨论，不应推迟到 §8 Limitations
- §4.5 perturbation control：应正式承认 CI 上界 13.3pp 的残余不确定性
- §4.6 统计分析：Holm-Bonferroni 三个 family 清晰；C3 不通过校正 correctly noted

### §5 Results
- C1 (§5.1)：证据压倒性。Variance decomposition (clause 22.4% vs model 1.0%) 是重要洞察
- C2 (§5.2)：统计支撑强，但 incompleteness confound 讨论必须在此处而非仅在 Limitations
- C3 (§5.3)：inconclusive 定位诚实且论证充分
- C4 (§5.4)：within-judge analysis for auth scope (Claude/Qwen3/DeepSeek 同由 GPT-5.4 评判) 是亮点，但 GPT-5.4 自身数据跨 judge boundary；2.9% variance 不足以支撑 primary claim

### §6 Error Analysis
- 五种 failure mode 定义清晰，跨模型一致性 (3/6 unanimous, 6/6 majority) compelling
- 三种机制模式 (structural misparse, gap-filling, boundary violation) 提供 actionable insights
- Ambiguity Blindness operationalization 需补充细节（"disambiguation awareness" vs "surface adoption" 编码标准）
- LLM-only coding 无 human validation 是方法论缺口

### §7 Discussion
- "Differential Nocuity" 框架定位为 empirical regularity 而非 governing principle 更恰当
- "Canary type" for auth scope 是最有实践价值的发现——但需 cross-judge 排除 confound
- Practical implications 段过长——导致超页。Mitigation 结果（Appendix B）的精华应整合入此处

### §8 Conclusion
- 准确总结主要发现
- "22× more violation variance" 是有力的 takeaway
- 需压缩以确保落入 page 8

### Limitations
- 覆盖全面且诚实——model coverage, domain scope, synthetic ambiguity, cross-judge, failure mode reliability, incompleteness confound, severity threshold
- Cross-judge 讨论应前移至 §4.4
- Incompleteness regression 分析有信息量但不充分（token count ≠ information content）
- Realism validation (TTR, Flesch-Kincaid, KS tests) 是好做法