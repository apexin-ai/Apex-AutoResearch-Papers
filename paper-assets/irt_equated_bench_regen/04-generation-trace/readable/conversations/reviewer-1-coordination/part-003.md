# Reviewer 1 coordination — Part 3 of 3

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../reviewer-1-coordination.md) · [Structured JSON](../../../sessions/f4/f44f4d47dd150062eb07.json)

## Round 32

### Assistant

_source line 982 · 2026-05-22T16:32:31.744300+00:00_

审稿意见已提交给 Review Director。

总结：我以 **Overall 3.0 (Findings)** 评分，识别了 4 个 Major 问题：

1. **DEFF 校正内部张力**（13.5% vs 29.2% 两倍差距，论证不充分）
2. **Graduated de-duplication 方法未定义**（三种收敛校正之一从未被正式描述）
3. **半合成 binary flipping 过度简化**（ΔTPR 的推广性存疑）
4. **因果模糊性与论文定位的张力**（difficulty-direction interaction 更符合能力演化而非污染）

主要优势在于 cross-subject matching 的 ΔFPR = 0 保证、ground truth 元批判、以及研究规模。适合 Findings 但定量结论精度不足以支撑主会议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 33

## Round 33

4 recorded events


### User

_source line 983 · 2026-05-22T16:37:50.653790+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每条 Weakness 和 Question，使用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 审稿意见：新颖性与完整性

## Summary

本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于六个 METABENCH 基准（5,227 模型 × 12,508 MMLU 题目为主），检测 2023 与 2024 模型队列之间的时序测量不稳定性。主要发现：(1) 经非独立性校正后约 27–29% 的 MMLU 题目表现出大幅时序 DIF；(2) web-overlap 污染标签与 DIF 标记近乎独立（Jaccard = 0.206）；(3) 跨科目匹配的半合成验证框架实现 ΔFPR = 0。论文建议对 LLM 基准进行常规 DIF 审计。

## Strengths

**S1** 规模与严谨性令人印象深刻。分析覆盖 5,227 个模型和 12,508 个 MMLU 题目，跨 5 个额外基准验证（共 27,125 题）。多重鲁棒性检验（随机分割、能力匹配、族内比较、DEFF 校正、cluster bootstrap）提供了全面的不确定性量化。三种独立的非独立性校正方法（simple-mean DEFF 29.2%、graduated de-duplication 29.1%、cluster bootstrap 下界 26.7%）收敛于 ≈27–29%，令人信服。

**S2** 跨科目匹配的半合成验证框架设计精良（Section 3.4）。单科目注入下 ΔFPR = 0 的理论保证是干净的方法论性质，多科目注入的退化分析（Table 6：k=10 时 ΔFPR = 0.047±0.022）信息量丰富。将 purified subtest matching 适配到 LLM 多科目场景是合理的方法论延伸。

**S3** 全局暴露（global exposure）与差异功能（differential functioning）的概念区分（Figure 1）清晰有力。虽然这一区分在 DIF 文献中已存在，但将其应用于 LLM 污染检测的辩论中是有价值的概念贡献。

**S4** Limitations 部分诚实且全面。对因果模糊性、MH-DIF 仅检测均匀 DIF 的局限、GSM1K 样本量限制均有坦诚讨论。特别是承认 difficulty–direction interaction (ρ = −0.597) "与技能习得更一致，而非污染"，这种学术诚实值得肯定。

**S5** 下游影响分析（Section 4.6）增加了实际价值：DIF 标记的题目集中了区分性信号（z = −8 to −49 vs. random removal），揭示了一个重要张力——移除不稳定题目反而会降低基准质量。这是一个值得社区关注的发现。

**S6** 跨基准复制（Table 3：6 个基准，C% 从 17.9% 到 31.3%）增强了发现的泛化性。知识/推理型基准比程序型基准 DIF 更高的模式（26.9–31.3% vs. 17.9–18.9%）具有描述性价值。

## Weaknesses

**W1 [Major] 因果模糊性削弱了论文的实际意义。**

- 具体位置：Section 5.1, Limitations
- 问题：论文检测到时序 DIF 但无法区分三种机制：污染、能力演化、训练方法变化。Discussion (Section 5.1) 承认这一点，甚至认为 difficulty–direction pattern (ρ = −0.597) "more consistent with skill acquisition than contamination"。如果观察到的 DIF 主要反映的是模型的合法能力进化，则论文在污染文献中的定位和"ground truth meta-critique"的 framing 都失去力度。
- 为什么影响接收：论文需要更明确地回答：temporal DIF 是需要修复的问题还是对模型能力变化的合法测量？当前的模糊处理让读者无法判断这项工作的 actionability。Section 5.2 的 DIF Audit Protocol 建议（Monitor/Flag/Act）在没有因果区分的前提下缺乏操作依据——如果 27% 的 DIF 中大部分是能力进化，那么在 C% ≥ 25% 时切换到 stable-item rankings（Act 级别）可能会系统性地低估 2024 模型的真实进步。
- 建议修改方向：(a) 将论文明确定位为 psychometric audit（中立描述性分析），弱化污染相关叙事；或 (b) 设计更有针对性的分析来分离因果来源（如利用已知训练数据组成不同的模型子集，或比较 base model vs. instruction-tuned 的 DIF 差异来隔离 post-training 效应）。

**W2 [Major] "Ground truth meta-critique"（Contribution 1）存在循环论证。**

- 具体位置：Section 4.3, Introduction Contribution 1
- 问题：论文在 Figure 1 中定义了 global exposure 和 differential functioning 的概念区分，然后在 Section 4.3 中实证展示两者不相关（Jaccard = 0.206），最后将此称为"category error in prevailing validation methodology"。但这在逻辑上近乎同义反复：作者自己定义的两个不同概念被验证为确实不同，这不是对任何一种方法的批判，而是对两者测量不同事物的确认。Enrichment ratio = 0.964 (95% CI [0.94, 1.02]) 甚至略低于 1.0，说明 DIF-C 题目中 web-contaminated 的比例反而稍低，进一步表明两者正交。
- 为什么影响接收：将 Contribution 1 框架为"meta-critique"暗示先前方法有错误，但实际上先前方法（web-overlap 检测）和本文方法（DIF 检测）各自测量不同的东西，两者都可以是正确的。这种过度包装削弱了论文的可信度。
- 建议修改方向：将 Contribution 1 重新框架为"empirical demonstration that global exposure and differential functioning are orthogonal constructs"，避免使用"meta-critique"和"category error"等暗示先前方法有误的措辞。

**W3 [Major] 方法论新颖性有限。**

- 具体位置：Section 2 (Related Work), Section 3
- 问题：论文明确声明"We do not modify the MH procedure"（Section 2）。跨科目匹配是已有 purified subtest matching 的适配（Swaminathan and Rogers, 1990; Nandakumar, 1993）。主要贡献是将标准教育测量方法大规模应用于新领域（LLM 基准），而非方法论创新。
- 为什么影响接收：对于 EMNLP 主会议论文，仅应用现有方法（无论规模多大）可能不足以满足新颖性要求。论文没有针对 LLM 特有挑战（如模型族内依赖、多维度结构、能力分布双峰性）开发新的 DIF 方法。DEFF 校正和 cluster bootstrap 是标准统计方法的直接应用。
- 建议修改方向：(a) 开发 LLM-specific 的 DIF 方法（例如利用模型族谱结构的层次化 DIF、结合 IRT 参数的因果 DIF 分解）；或 (b) 更强调实证发现的新颖性和实际影响，承认方法论贡献是应用层面的。

**W4 [Minor] Framing 在两种不兼容叙事间摇摆。**

- 具体位置：Title vs. Introduction vs. Discussion
- 问题：标题和论文大部分内容将此框架为"measurement instability"（中立、心理测量学），但 Introduction 的第一个贡献是针对污染标签的"ground truth meta-critique"，大量文本讨论 contamination detection。Discussion (Section 5.1) 又转向"可能是能力进化"。读者会困惑：这是 (a) 基准时序稳定性的心理测量学审计，还是 (b) 污染检测方法论的批判？这是两篇不同的论文，应用不同的评价标准。

**W5 [Minor] 核心估计 ≈27–29% 的不确定性未被充分讨论。**

- 具体位置：Section 4.2, Appendix D
- 问题：Cluster bootstrap CI 为 [26.7%, 53.2%]，上界几乎是点估计的两倍。DEFF 校正范围为 13.5%–29.2%，取决于 $\bar{m}$ 估计器的选择——跨越 2× 因子。论文将 weighted-mean DEFF (13.5%) 称为"unrealistic"（Section 4.2），理由是有效 cluster size $\bar{m}$=254 意味着每个 family member "functionally identical"。但 weighted-mean $\bar{m}$ 是 survey methodology 中的标准方法（Kish, 1965），反映随机抽样模型所经历的实际聚类效应。在仅约 30 个 families 的情况下，ICC 估计的方差很大，进一步增加不确定性。读者很难判断真实 C% 是 13.5% 还是 29.2%。

**W6 [Minor] MMLU 题目质量问题处理不充分。**

- 具体位置：Section 5.1
- 问题：MMLU 已知存在大量问题题目（错误、歧义选项、过时内容）。论文引用 Gema et al. (2024) 的专家标注错误，报告 enrichment = 1.10× (95% CI [0.92, 1.27], p = 0.23)。但：(a) CI 上界 1.27 意味着 DIF-C 题目中错误题比例可能高出 27%；(b) Gema et al. 的错误标注仅覆盖部分质量问题；(c) DIF 可能部分反映不同代际模型对歧义题目的差异敏感度，这不会被错误标注捕获。用不显著的 p = 0.23 来"rule out"题目质量缺陷是 absence of evidence ≠ evidence of absence。

**W7 [Minor] GSM1K 探索性分析 (N=33) 统计功效不足。**

- 具体位置：Section 4.7, Appendix Figure 5
- 问题：N=33 时，单个 influential point 即可改变相关性的显著性和方向。虽然 leave-one-out 分析确认单个移除后 r 仍显著 (r ∈ [−0.54, −0.37])，且移除三个 Cook's D 异常值后 r = −0.38 (p = 0.036)，但 p = 0.036 在 N=30 下并不稳健。此外，在 appendix 中以完整 figure 和详细分析呈现赋予了这个探索性结果过多权重。
- 建议：要么大幅扩展样本量，要么将其缩减为一段简短提及。

**W8 [Nitpick] 页面格式存在激进操作。**

- 具体位置：discussion.tex 第 3 行 `\enlargethispage*{14\baselineskip}`；conclusion.tex 第 1 行 `\vspace{-12pt}`
- 问题：14 baselines 在 11pt 字体下约增加 2.5 英寸的页面高度，可能导致文本侵入下边距。结合 Conclusion 前的 −12pt vspace，说明论文在 8 页限制下非常紧张。虽然此类格式操作在 ARR 提交中常见，但 14\baselineskip 的幅度异常大。

**W9 [Nitpick] Abstract 和 Title 的范围暗示与实际分析不完全匹配。**

- 具体位置：Abstract, Title
- 问题：Abstract 提到"six METABENCH benchmarks (5,227 models, 27,125 items)"，但 5,227 是 MMLU 的模型数（GSM8K 用 6,702 个模型，见 Appendix E Table 9）。非 MMLU 基准仅占一个小节（Section 4.7）和一张表（Table 3）。论文的贡献范围主要是 MMLU，abstract 的表述可能让读者高估了分析的均匀覆盖度。

## Questions

**Q1**: Difficulty–direction interaction (ρ = −0.597) 被解读为"与技能习得更一致"。但如果简单题目因更常见于公开语料而在两个队列中均被"均匀污染"（产生 DIF-A 而非 DIF-C），而复杂题目因稀缺性更易产生差异化污染，这同样能解释该模式。能否排除这种替代解释？

**Q2**: DEFF 估计假设族内 ICC 恒定。但 fine-tune 和 merge 模型与 base model variants 的 ICC 可能差异很大。DEFF 估计对异常值家族（如 Mistral 547 个模型，占 ref cohort 51%）的敏感度如何？

**Q3**: Section 5.2 建议"≥500 模型累积时进行 MH-DIF 审计"。这个阈值的依据是什么？Power analysis（Section 4.1）显示 N ≥ 80/cohort 即可。500 是总模型数还是每队列？

**Q4**: Growing Pains (Habba et al., 2026) 使用 IRT calibration 选择 anchor items。其选择的 anchor items 与本文的 DIF-A（stable）题目实际重叠如何？是否有实证比较？

**Q5**: 6 个月窗口分析得到 C% = 34.35%（Section 4.7），高于完整年度对比的 31.3%。这似乎违反直觉——更短的时间窗口应该产生更少的 DIF。能否解释？是否因为短窗口内模型队列组成更极端（如集中在特定家族）？

## Missing References

1. **MMLU-Pro** (Wang et al., 2024): MMLU 的强化版本，设计上对污染更鲁棒。在讨论 MMLU 脆弱性和潜在补救策略时直接相关，目前未被引用。

2. **Polo et al. (2024), "tinyBenchmarks"** — 已引用，但论文可加强与 IRT-based item selection 方法（如 TinyBenchmarks 选择的子集）的 DIF 特征对比讨论。

3. 论文引用了 Suk and Lyu (2026) 的因果 DIF 框架但未充分利用——考虑到 W1 中的因果模糊性问题，更深入地讨论因果 DIF 方法论将增强论文。

## Overall Assessment

**Overall**: 3.5 (Borderline Conference)
**Confidence**: 4/5

**一句话总评**: 大规模、方法严谨的实证研究，但核心方法无创新（直接应用 1988 年的 MH-DIF）、因果解释缺失、且 framing 在心理测量审计与污染批判之间摇摆不定，削弱了贡献的清晰度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 984 · 2026-05-22T16:39:46.190928+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n## Weaknesses 回应\n\n**[AGREE] R2-W1: 因果模糊性削弱实际意义**\n\n同意，且我在自己的 W4 中提出了高度一致的关切。补充两点：\n\n(1) R2 指出 Section 5.2 的 DIF Audit Protocol 在无因果区分的前提下缺乏操作依据——这比我的批评更具体、更有力。如果 27% DIF 的主体是能力演化，Act 级别（C% ≥ 25% 切换到 stable-item rankings）会系统性低估 2024 模型进步，这确实是一个实践危害。\n\n(2) R2 建议 \"利用已知训练数据组成不同的模型子集来分离因果\" 是可行的方向。例如，比较 base model 与其 instruction-tuned 变体的 DIF 差异可以隔离 post-training 效应（两者共享预训练数据但 post-training 不同）。论文有 Within-family 比较（Llama-2 vs Llama-3, Table 1: C% = 61.3%），但未沿此方向做因果分离。\n\n**[REBUT] R2-W2: Ground truth meta-critique 循环论证**\n\n部分不同意。R2 的论证是：论文定义了两个不同概念，然后验证它们不同，这是同义反复。但论文的贡献不仅是抽象概念区分，而是具体的**实证发现**：先前多项污染检测工作（Section 2, Related Work 中引用的 Shi et al. 2024, Dekoninck et al. 2024 等）使用 Li et al. (2024) 的 web-overlap 标签作为 ground truth 来评估检测器性能。论文证明这些标签与 DIF 正交（Jaccard = 0.206, enrichment = 0.964, Section 4.3），这意味着：用 web-overlap 标签验证的检测器可能在检测 differential functioning 方面完全无信息量。这是一个有实操意义的发现，不是纯概念层面的同义反复。\n\n但我同意 R2 的措辞建议：\"meta-critique\" 和 \"category error\" 的措辞确实过强。更准确的框架是 \"empirical demonstration that these labels measure a different construct\"，而不是暗示先前方法有 \"错误\"——两种方法测量不同的东西，各有其合理用途。\n\n**[AGREE] R2-W3: 方法论新颖性有限**\n\n同意论文的方法论贡献主要在应用层面。论文自己承认 \"We do not modify the MH procedure\"（Section 2）。Cross-subject matching 是对 purified subtest matching（Swaminathan & Rogers, 1990; Nandakumar, 1993）的适配，DEFF 校正和 cluster bootstrap 是标准统计方法。\n\n但我对 R2 的严重程度评估有保留：EMNLP 接收大量以 empirical contribution 为主的论文，将标准方法大规模应用于新领域并产生重要实证发现（如 DIF 与 web-overlap 正交、6 个基准的跨基准复现），在我看来可以达到 Findings 的新颖性门槛，尽管对主会议确实偏弱。关键问题不在于方法是否新颖，而在于实证发现是否可靠——而这回到了 W1（因果模糊性）和我的 W1（DEFF 张力）的讨论。\n\n**[AGREE] R2-W4: Framing 摇摆**\n\n完全同意。我在自己的 W4 中从略有不同的角度提出了同一问题。论文在 \"psychometric audit\"（标题、Section 5.1 承认因果模糊性）和 \"contamination critique\"（Introduction Contribution 1、大量污染检测文献讨论）之间确实不一致。这两种叙事需要不同的评价标准，混合呈现让读者无法定位论文的核心贡献。\n\n**[AGREE] R2-W5: 核心估计不确定性**\n\n同意，且与我的 W1 高度一致。R2 补充了一个我未充分强调的重要观点：weighted-mean m̄ 是 survey methodology 的标准方法（Kish, 1965），论文将其视为 \"unrealistic\" 需要更强的论证。Cluster bootstrap CI [26.7%, 53.2%] 的上界 53.2% 几乎是下界的两倍——这个不确定性范围本身就说明定量结论的精度不足。\n\n**[AGREE] R2-W6: MMLU 题目质量处理不充分**\n\n同意。R2 正确指出 CI 上界 1.27 意味着高达 27% 的 enrichment 与数据兼容，且 Gema et al. 的错误标注仅覆盖部分质量问题。\"Absence of evidence ≠ evidence of absence\" 是准确的方法论批评。论文用不显著的 p 值来 \"rule out\" item quality defects 在逻辑上不严密。\n\n不过，我认为此问题对核心结论的威胁有限：即使 DIF-C 题目中存在 27% 的错误率偏高，这仍然意味着绝大多数 DIF-C 题目不是由错误驱动的。这更多是 framing 问题（不应说 \"ruled out\"）而非实质性威胁。\n\n**[AGREE] R2-W7: GSM1K N=33**\n\n同意。论文在 Limitations 中承认 \"limited statistical power and is exploratory\"，但 Appendix 中以完整 Figure 和详细 Cook's D 分析呈现赋予了过多权重。应缩减为正文中一句话的提及或完全移入补充材料。\n\n**[AGREE] R2-W8: 页面格式激进**\n\n同意。`\\enlargethispage*{14\\baselineskip}` 在 11pt acl 模板下约增加 2.3-2.5 英寸——这确实异常激进，可能导致文本侵入下边距。结合 `\\vspace{-12pt}` 和正文中多处 `\\looseness=-1`，论文显然在 8 页限制下极度紧张。这可能导致 Area Chair 格式审查时被标记。\n\n**[AGREE] R2-W9: Abstract 范围暗示**\n\n同意。Abstract 提到 \"six METABENCH benchmarks (5,227 models, 27,125 items)\" 暗示均匀覆盖，但非 MMLU 基准仅在 Section 4.7 一个小节和 Table 3 中处理，无独立的 DEFF 校正或半合成验证。5,227 是 MMLU 的模型数，GSM8K 实际用 6,702 模型（Appendix E, Table 9），这一差异在 Abstract 中被掩盖。\n\n## Questions 回应\n\n**[AGREE] R2-Q1: Difficulty-direction interaction 的替代解释**\n\n这是一个我未考虑到的有力替代解释。R2 提出：简单题目因更常见于公开语料而在两个队列中均被\"均匀污染\"（产生 DIF-A），复杂题目因稀缺性更易产生差异化污染（产生 DIF-C）。这一机制同样能解释 ρ = -0.597 的 difficulty-direction pattern，且与污染假说兼容而非能力演化。论文需要提供证据排除（或至少讨论）这一替代解释。可以通过检查 Li et al. 标签中的 web-overlap 覆盖率是否按难度分层来间接测试。\n\n**[AGREE] R2-Q2: DEFF 对异常家族的敏感度**\n\n与我的 W7 一致。Mistral（547 模型，占 ref cohort 51%）对 ICC 估计和 DEFF 的影响应当被量化。\n\n**[AGREE] R2-Q3: 500 模型阈值依据**\n\nR2 准确指出 power analysis 显示 N ≥ 80/cohort 即可，但 Section 5.2 建议 \"≥500 模型累积时\"。这个 500 是 ad hoc 的——论文未解释为什么不是 160（80×2 cohorts）或 1000。阈值建议需要更明确的统计依据。\n\n**[REBUT] R2-Q4: Growing Pains anchor items 重叠**\n\n这是一个有趣的研究问题，但我认为不应作为本文的 weakness。Growing Pains (Habba et al., 2026) 是并行工作，使用不同方法（IRT calibration）选择 anchor items。论文已在 Related Work (Section 2) 中引用了该工作并说明本文 \"complements concurrent work on anchor-item calibration\"。要求与并行工作进行实证比较超出了合理范围。\n\n**[AGREE] R2-Q5: 6 个月窗口 C% = 34.35% 高于年度对比**\n\n这确实违反直觉。R2 的猜测（短窗口内模型队列组成更极端）是合理的——6 个月窗口可能导致队列被特定家族主导，从而放大家族特异性 DIF。论文应解释这一现象，或至少将其作为 DEFF/家族效应的证据讨论。\n\n## Missing References 回应\n\n**[AGREE] MMLU-Pro**: Wang et al. (2024) 的 MMLU-Pro 确实直接相关——作为 MMLU 的强化版本，讨论 MMLU 的脆弱性时应当引用。\n\n**[REBUT] Suk and Lyu (2026) 利用不足**: 论文已在 Section 5.1 引用 Suk and Lyu (2026) 并明确指出 \"observational DIF alone cannot separate contamination from capability evolution\"。在无法获取训练数据的前提下，更深入地应用因果 DIF 方法论是不现实的——因果 DIF 需要因果模型假设和更多数据（如反事实情境），论文的 observational setting 不支持。\n\n## Overall Assessment 回应\n\nR2 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于对方法论新颖性的权重：\n\n- R2 将 W3（方法论无创新）列为 Major，但仍给 3.5。我认为 W3 的严重性取决于实证发现的可靠性——如果定量结论可靠，\"大规模应用现有方法产生重要发现\" 可以达到 Findings 甚至 Borderline Conference。\n- 我给出 3.0 的主要原因是 DEFF 内部张力（我的 W1，R2 的 W5）和 graduated de-duplication 未定义（我的 W2）共同削弱了核心定量结论（27-29%）的可信度。如果这个数字不可靠，论文的大部分实证贡献都受影响。\n- R2 未提及 graduated de-duplication 未定义的问题（我的 W2），这是一个重要遗漏。作为三种收敛方法之一，该方法在论文中从未被正式描述，这是严重的可复现性缺陷。\n\n综合两份审稿意见，我认为论文在 Findings 和 Borderline Conference 之间，倾向 Findings（3.0-3.5）。核心阻碍主会议录用的问题是：(1) 因果模糊性 + framing 不一致（R1-W4, R2-W1, R2-W4）；(2) 定量结论精度不足（R1-W1, R2-W5）；(3) 方法论新颖性有限（R2-W3）。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n## Weaknesses 回应\n\n**[AGREE] R2-W1: 因果模糊性削弱实际意义**\n\n同意，且我在自己的 W4 中提出了高度一致的关切。补充两点：\n\n(1) R2 指出 Section 5.2 的 DIF Audit Protocol 在无因果区分的前提下缺乏操作依据——这比我的批评更具体、更有力。如果 27% DIF 的主体是能力演化，Act 级别（C% ≥ 25% 切换到 stable-item rankings）会系统性低估 2024 模型进步，这确实是一个实践危害。\n\n(2) R2 建议 \"利用已知训练数据组成不同的模型子集来分离因果\" 是可行的方向。例如，比较 base model 与其 instruction-tuned 变体的 DIF 差异可以隔离 post-training 效应（两者共享预训练数据但 post-training 不同）。论文有 Within-family 比较（Llama-2 vs Llama-3, Table 1: C% = 61.3%），但未沿此方向做因果分离。\n\n**[REBUT] R2-W2: Ground truth meta-critique 循环论证**\n\n部分不同意。R2 的论证是：论文定义了两个不同概念，然后验证它们不同，这是同义反复。但论文的贡献不仅是抽象概念区分，而是具体的**实证发现**：先前多项污染检测工作（Section 2, Related Work 中引用的 Shi et al. 2024, Dekoninck et al. 2024 等）使用 Li et al. (2024) 的 web-overlap 标签作为 ground truth 来评估检测器性能。论文证明这些标签与 DIF 正交（Jaccard = 0.206, enrichment = 0.964, Section 4.3），这意味着：用 web-overlap 标签验证的检测器可能在检测 differential functioning 方面完全无信息量。这是一个有实操意义的发现，不是纯概念层面的同义反复。\n\n但我同意 R2 的措辞建议：\"meta-critique\" 和 \"category error\" 的措辞确实过强。更准确的框架是 \"empirical demonstration that these labels measure a different construct\"，而不是暗示先前方法有 \"错误\"——两种方法测量不同的东西，各有其合理用途。\n\n**[AGREE] R2-W3: 方法论新颖性有限**\n\n同意论文的方法论贡献主要在应用层面。论文自己承认 \"We do not modify the MH procedure\"（Section 2）。Cross-subject matching 是对 purified subtest matching（Swaminathan & Rogers, 1990; Nandakumar, 1993）的适配，DEFF 校正和 cluster bootstrap 是标准统计方法。\n\n但我对 R2 的严重程度评估有保留：EMNLP 接收大量以 empirical contribution 为主的论文，将标准方法大规模应用于新领域并产生重要实证发现（如 DIF 与 web-overlap 正交、6 个基准的跨基准复现），在我看来可以达到 Findings 的新颖性门槛，尽管对主会议确实偏弱。关键问题不在于方法是否新颖，而在于实证发现是否可靠——而这回到了 W1（因果模糊性）和我的 W1（DEFF 张力）的讨论。\n\n**[AGREE] R2-W4: Framing 摇摆**\n\n完全同意。我在自己的 W4 中从略有不同的角度提出了同一问题。论文在 \"psychometric audit\"（标题、Section 5.1 承认因果模糊性）和 \"contamination critique\"（Introduction Contribution 1、大量污染检测文献讨论）之间确实不一致。这两种叙事需要不同的评价标准，混合呈现让读者无法定位论文的核心贡献。\n\n**[AGREE] R2-W5: 核心估计不确定性**\n\n同意，且与我的 W1 高度一致。R2 补充了一个我未充分强调的重要观点：weighted-mean m̄ 是 survey methodology 的标准方法（Kish, 1965），论文将其视为 \"unrealistic\" 需要更强的论证。Cluster bootstrap CI [26.7%, 53.2%] 的上界 53.2% 几乎是下界的两倍——这个不确定性范围本身就说明定量结论的精度不足。\n\n**[AGREE] R2-W6: MMLU 题目质量处理不充分**\n\n同意。R2 正确指出 CI 上界 1.27 意味着高达 27% 的 enrichment 与数据兼容，且 Gema et al. 的错误标注仅覆盖部分质量问题。\"Absence of evidence ≠ evidence of absence\" 是准确的方法论批评。论文用不显著的 p 值来 \"rule out\" item quality defects 在逻辑上不严密。\n\n不过，我认为此问题对核心结论的威胁有限：即使 DIF-C 题目中存在 27% 的错误率偏高，这仍然意味着绝大多数 DIF-C 题目不是由错误驱动的。这更多是 framing 问题（不应说 \"ruled out\"）而非实质性威胁。\n\n**[AGREE] R2-W7: GSM1K N=33**\n\n同意。论文在 Limitations 中承认 \"limited statistical power and is exploratory\"，但 Appendix 中以完整 Figure 和详细 Cook's D 分析呈现赋予了过多权重。应缩减为正文中一句话的提及或完全移入补充材料。\n\n**[AGREE] R2-W8: 页面格式激进**\n\n同意。`\\enlargethispage*{14\\baselineskip}` 在 11pt acl 模板下约增加 2.3-2.5 英寸——这确实异常激进，可能导致文本侵入下边距。结合 `\\vspace{-12pt}` 和正文中多处 `\\looseness=-1`，论文显然在 8 页限制下极度紧张。这可能导致 Area Chair 格式审查时被标记。\n\n**[AGREE] R2-W9: Abstract 范围暗示**\n\n同意。Abstract 提到 \"six METABENCH benchmarks (5,227 models, 27,125 items)\" 暗示均匀覆盖，但非 MMLU 基准仅在 Section 4.7 一个小节和 Table 3 中处理，无独立的 DEFF 校正或半合成验证。5,227 是 MMLU 的模型数，GSM8K 实际用 6,702 模型（Appendix E, Table 9），这一差异在 Abstract 中被掩盖。\n\n## Questions 回应\n\n**[AGREE] R2-Q1: Difficulty-direction interaction 的替代解释**\n\n这是一个我未考虑到的有力替代解释。R2 提出：简单题目因更常见于公开语料而在两个队列中均被\"均匀污染\"（产生 DIF-A），复杂题目因稀缺性更易产生差异化污染（产生 DIF-C）。这一机制同样能解释 ρ = -0.597 的 difficulty-direction pattern，且与污染假说兼容而非能力演化。论文需要提供证据排除（或至少讨论）这一替代解释。可以通过检查 Li et al. 标签中的 web-overlap 覆盖率是否按难度分层来间接测试。\n\n**[AGREE] R2-Q2: DEFF 对异常家族的敏感度**\n\n与我的 W7 一致。Mistral（547 模型，占 ref cohort 51%）对 ICC 估计和 DEFF 的影响应当被量化。\n\n**[AGREE] R2-Q3: 500 模型阈值依据**\n\nR2 准确指出 power analysis 显示 N ≥ 80/cohort 即可，但 Section 5.2 建议 \"≥500 模型累积时\"。这个 500 是 ad hoc 的——论文未解释为什么不是 160（80×2 cohorts）或 1000。阈值建议需要更明确的统计依据。\n\n**[REBUT] R2-Q4: Growing Pains anchor items 重叠**\n\n这是一个有趣的研究问题，但我认为不应作为本文的 weakness。Growing Pains (Habba et al., 2026) 是并行工作，使用不同方法（IRT calibration）选择 anchor items。论文已在 Related Work (Section 2) 中引用了该工作并说明本文 \"complements concurrent work on anchor-item calibration\"。要求与并行工作进行实证比较超出了合理范围。\n\n**[AGREE] R2-Q5: 6 个月窗口 C% = 34.35% 高于年度对比**\n\n这确实违反直觉。R2 的猜测（短窗口内模型队列组成更极端）是合理的——6 个月窗口可能导致队列被特定家族主导，从而放大家族特异性 DIF。论文应解释这一现象，或至少将其作为 DEFF/家族效应的证据讨论。\n\n## Missing References 回应\n\n**[AGREE] MMLU-Pro**: Wang et al. (2024) 的 MMLU-Pro 确实直接相关——作为 MMLU 的强化版本，讨论 MMLU 的脆弱性时应当引用。\n\n**[REBUT] Suk and Lyu (2026) 利用不足**: 论文已在 Section 5.1 引用 Suk and Lyu (2026) 并明确指出 \"observational DIF alone cannot separate contamination from capability evolution\"。在无法获取训练数据的前提下，更深入地应用因果 DIF 方法论是不现实的——因果 DIF 需要因果模型假设和更多数据（如反事实情境），论文的 observational setting 不支持。\n\n## Overall Assessment 回应\n\nR2 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于对方法论新颖性的权重：\n\n- R2 将 W3（方法论无创新）列为 Major，但仍给 3.5。我认为 W3 的严重性取决于实证发现的可靠性——如果定量结论可靠，\"大规模应用现有方法产生重要发现\" 可以达到 Findings 甚至 Borderline Conference。\n- 我给出 3.0 的主要原因是 DEFF 内部张力（我的 W1，R2 的 W5）和 graduated de-duplication 未定义（我的 W2）共同削弱了核心定量结论（27-29%）的可信度。如果这个数字不可靠，论文的大部分实证贡献都受影响。\n- R2 未提及 graduated de-duplication 未定义的问题（我的 W2），这是一个重要遗漏。作为三种收敛方法之一，该方法在论文中从未被正式描述，这是严重的可复现性缺陷。\n\n综合两份审稿意见，我认为论文在 Findings 和 Borderline Conference 之间，倾向 Findings（3.0-3.5）。核心阻碍主会议录用的问题是：(1) 因果模糊性 + framing 不一致（R1-W4, R2-W1, R2-W4）；(2) 定量结论精度不足（R1-W1, R2-W5）；(3) 方法论新颖性有限（R2-W3）。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-22T16:39:51.517750+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5326
}
```

</details>

---


### Assistant

_source line 986 · 2026-05-22T16:40:00.802768+00:00_

已提交对 Reviewer 2 全部意见的逐条回应。主要判断：

- **8/9 条 Weakness 同意**（W1因果模糊性、W3新颖性有限、W4-W9），仅对 W2（ground truth meta-critique 循环论证）部分反驳——论文的实证发现（web-overlap 标签与 DIF 正交）有实操意义，不是纯概念层面的同义反复，但 "meta-critique" 措辞确实过强。
- **4/5 条 Question 同意**，仅对 Q4（与 Growing Pains anchor items 比较）反驳——这超出了对并行工作的合理要求。
- 综合评分：两份审稿意见在因果模糊性、DEFF 张力、framing 不一致三个核心问题上高度一致，论文适合 Findings 收录（3.0-3.5 区间）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 34

## Round 34

50 recorded events


### User

_source line 987 · 2026-05-23T05:52:53.458147+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）

### Venue 信息
- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 提交）
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页 + 无限参考文献；Limitations 章节不计入页数
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind（作者信息不可出现在论文中）
- **附录**: 允许，审稿人可选择性参考

### 论文文件
- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf`

### 你的审查侧重

**方法严谨性 + 实验设计**。重点评估：

1. **MH-DIF 方法论**: MH procedure 的应用是否正确？ETS C 分类阈值选择是否合理？Cross-subject matching 策略的理论基础是否充分？ΔFPR=0 的 guarantee 是否成立？
2. **Semi-synthetic 验证框架**: Binary response flipping 是否过于简化？Injection framework 的 ecological validity 如何？Dose-response 曲线是否令人信服？
3. **统计控制**: DEFF 校正方法是否恰当？Simple-mean vs weighted-mean 的选择依据？Family-level cluster bootstrap 的设计？Leave-one-family-out 分析是否充分？
4. **实验设计**: 时间队列划分（2023 vs 2024）是否合理？Matched-ability 分析是否足以排除 ability confound？Cross-benchmark replication 的验证力度？
5. **数据质量**: METABENCH 数据的可靠性？Web-overlap labels 作为外部参照的适当性？
6. **因果推断**: 论文是否恰当地区分了 DIF 检测（what）与因果归因（why）？Base-vs-instruct decomposition 的推断边界？
7. **局限性讨论**: Limitations 是否充分覆盖了方法论的已知弱点？

### 输出格式
请按以下结构撰写审稿意见：
- **Summary** (2-3 句)
- **Strengths** (逐条，S1/S2/...)
- **Weaknesses** (逐条，W-M1/W-M2/... 表示方法类; W-E1/W-E2/... 表示实验类; W-S1/W-S2/... 表示统计类)
  - 每条标注严重程度: [Must-Fix] / [Should-Fix] / [Minor]
- **Questions** (Q1/Q2/...)
- **Missing References** (如有)
- **Overall Assessment**: 评分 + 置信度
  - 评分标准 (ARR): 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit

请严格、客观、不留情面地评审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-23T05:53:03.917094+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-23T05:53:04.017887+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-23T05:53:07.982605+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 991 · 2026-05-23T05:53:10.545195+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf",
  "pages": "1-10",
  "project": "irt_equated_bench_regen",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf",
    "pages": "1-10",
    "project": "irt_equated_bench_regen",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 992 · 2026-05-23T05:53:14.316975+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about the ACL Rolling Review 2026 reviewer guidelines, review form, and criteria:

## Reviewer Guidelines

Reviewers are asked to read the paper to get an initial impression, search for related work, and note any major sections they did not check (such as proofs). Reviewers are provided with a checklist to flag problems that others may have missed.

## Review Standards and Criteria

Papers should be treated as submissions to ACL when evaluating them. For Findings track papers, the 
…[truncated 858 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6334
}
```

</details>

---


### Tool result

_source line 993 · 2026-05-23T05:53:16.480902+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 555.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 575.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p9.png\", \"width\": 1
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5935
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-23T05:53:23.058977+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all dimensions, rating scales, and criteria. Include every field name, its scale (e.g., 1-5), and the description of each rating level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all dimensions, rating scales, and criteria. Include every field name, its scale (e.g., 1-5), and the description of each rating level."
  }
}
```

</details>

---


### Tool call

_source line 995 · 2026-05-23T05:53:24.114097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-23T05:53:24.517908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-23T05:53:25.422400+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool result

_source line 998 · 2026-05-23T05:53:25.423817+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 999 · 2026-05-23T05:53:25.424290+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-23T05:53:25.978687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-23T05:53:26.331424+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-23T05:53:26.335126+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-23T05:53:26.844963+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 866
}
```

</details>

---


### Tool result

_source line 1004 · 2026-05-23T05:53:27.247831+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 912
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-23T05:53:30.561098+00:00_

# ACL Rolling Review Form - Complete Structure

## Primary Review Dimensions

**Paper Summary**
Free-form assessment of paper topic and content clarity.

**Summary of Strengths**
Open-ended evaluation of reasons for publication, including "novel and useful methodology, insightful empirical results."

**Summary of Weaknesses**
Numbered concerns about correctness, impact, or clarity that authors can address individually.

**Comments/Suggestions/Typos**
Additional improvement suggestions beyond main weaknesses.

## Numerical Rating Scales

**Reviewer Confidence** (1-5)
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure" with minimal risk of error
- 3: "Pretty sure" but details unchecked
- 2: "Willing to defend" but likely missed elements
- 1: "Not my area" or incomprehensible

**Soundness** (1-5 with half-points)
- 5: "Most thorough" for its type
- 4: "Sufficient support" for claims
- 3: "Acceptable" with minor gaps
- 2: "Major technical/methodological problems"
- 1: Insufficient for publication

**Excitement** (1-5 with half-points)
- 5: "Highly Exciting" recommendation
- 4: Notable enough to mention
- 3: "Interesting" if time permits
- 2: May resonate with others
- 1: Not aligned with NLP community

**Overall Assessment** (1-5 with half-points)
- 5: Award consideration (top 2.5%)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Needs substantial revision
- 1: Do not resubmit

## Additional Evaluation Areas

**Limitations and Societal Impact**
Open assessment of discussed limitations and potential harms to marginalized populations.

**Ethical Concerns**
Evaluation against "ACL code of ethics" and author submissions.

**Needs Ethics Review**
Determination if special committee review required.

**Reproducibility** (1-5)
- 5: Results easily reproducible
- 1: Results irreproducible

**Datasets** (1-5)
Value ranging from "Enabling" to "No usable datasets."

**Software** (1-5)
Value assessment similar to datasets scale.

**Author Identity Knowledge** (1-
…[truncated 38 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7502
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-23T05:53:39.801048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1007 · 2026-05-23T05:53:40.153933+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-23T05:53:41.211488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-23T05:53:41.515402+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1714
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-23T05:53:41.515857+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-23T05:53:42.923467+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2769
}
```

</details>

---


### Tool result

_source line 1012 · 2026-05-23T05:53:42.924441+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1712
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-23T05:53:42.925145+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-23T05:53:43.075912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-23T05:53:43.980611+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-23T05:53:43.981088+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf",
  "pages": "11-17",
  "project": "irt_equated_bench_regen",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf",
    "pages": "11-17",
    "project": "irt_equated_bench_regen",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1017 · 2026-05-23T05:53:44.836470+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 586.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 416.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 425.8}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 94.7}], \"total_pages\": 17, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1018 · 2026-05-23T05:53:51.471566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1019 · 2026-05-23T05:53:52.028188+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-23T05:53:53.282004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-23T05:53:53.536627+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2065
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-23T05:53:53.537117+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 1023 · 2026-05-23T05:53:53.940483+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1024 · 2026-05-23T05:53:54.800629+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2772
}
```

</details>

---


### Tool call

_source line 1025 · 2026-05-23T05:53:54.801135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-23T05:53:55.103241+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-23T05:53:55.155846+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 1028 · 2026-05-23T05:53:55.409615+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2127
}
```

</details>

---


### Tool result

_source line 1029 · 2026-05-23T05:53:55.563503+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2026
}
```

</details>

---


### Tool result

_source line 1030 · 2026-05-23T05:53:56.016028+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2075
}
```

</details>

---


### Tool result

_source line 1031 · 2026-05-23T05:53:56.070240+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1269
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-23T05:59:56.510238+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form. For each numerical field (Soundness, Excitement, Overall Assessment, Reproducibility, etc.), list EVERY rating level with its exact description. I need the full text of each level, not just summaries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form. For each numerical field (Soundness, Excitement, Overall Assessment, Reproducibility, etc.), list EVERY rating level with its exact description. I need the full text of each level, not just summaries."
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-23T06:00:07.457867+00:00_

# ACL Rolling Review Form - Complete Rating Scales

## Reviewer Confidence
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings."
- **3:** "Pretty sure, but there's a chance I missed something. Although I have a good feel for this area in general, I did not carefully check the paper's details, e.g., the math or experimental design."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details, didn't understand some central points, or can't be sure about the novelty of the work."
- **1:** "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

## Soundness
- **5:** "Excellent: This study is one of the most thorough I have seen, given its type."
- **4:** "Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential."
- **3:** "Acceptable: This study provides sufficient support for its main claims. Some minor points may need extra support or details."
- **2:** "Poor: Some of the main claims are not sufficiently supported. There are major technical/methodological problems."
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL."

## Excitement
- **5:** "Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference."
- **4:** "Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference."
- **3:** "Interesting: I might mention some points of this paper to others and/or attend its presentation if there's time."
- **2:** "Potentially Interesting: this paper does not resonate with me, but it might with others in the *ACL community."
- **1:** "Not Exciting: this paper
…[truncated 3378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 10947
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-23T06:02:46.537032+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n---\n\n### Summary\n\n本文将教育测量领域的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 方法引入 LLM benchmark 评估，在 METABENCH 数据上（5,227 模型 × 12,508 MMLU items）检测 2023 与 2024 模型队列之间的 temporal measurement instability。核心发现是 27–29% 的 MMLU items（经非独立性校正后）表现出显著的 temporal DIF，但该不稳定性不影响模型排名（ρ ≥ 0.997）。论文引入了 cross-subject matching（ΔFPR = 0 guarantee）、DEFF clustering 校正、semi-synthetic injection 验证框架等方法贡献。总体而言，这是一篇有实质创新的跨学科论文，方法论基础扎实，但在若干关键环节的 claim scoping 和验证充分性上存在改进空间。\n\n---\n\n### Strengths\n\n**S1. 真正的跨学科方法创新。** MH-DIF 在教育测量领域已有数十年积累，但将其系统性地引入 LLM benchmark 评估是新颖的。论文不是简单套用，而是针对 LLM 特有问题做了有意义的方法适配：cross-subject matching 解决了 multi-domain benchmark 中 matching variable 被污染的问题（Section 3.4），DEFF 校正处理了模型家族非独立性（Section C），这些都是 non-trivial 的方法贡献。\n\n**S2. 规模与覆盖面令人印象深刻。** 5,227 个模型 × 12,508 items 的分析规模远超此前 IRT/DIF 在 NLP 领域的应用。跨六个 benchmark 的 replication（Table 3, Figure 6）增加了结果可信度。\n\n**S3. 多层 convergent evidence 设计。** 论文构建了完整的证据链：semi-synthetic injection → Monte Carlo power analysis → structural controls（matched-ability、leave-one-family-out）→ cross-benchmark replication → downstream impact analysis（ranking preservation）。这种多层验证在 NLP 实证论文中并不常见。\n\n**S4. Global exposure 与 differential functioning 的概念区分。** Section 4.3 中 DIF flags 与 web-overlap labels 的正交性结果（Jaccard = 0.206, ψ = 0.012, OR = 1.05 [0.96, 1.15]）以及 Figure 1 的概念图，清晰地建立了 DIF 检测与传统 contamination detection 的理论区别。这对领域的概念框架有贡献。\n\n**S5. Downstream impact 分析提供了实用视角。** Section 4.6 中 ρ ≥ 0.997 的 ranking preservation 以及 Figure 6 中 DIF-ordered vs random removal 的对比，将统计发现转化为可操作的 benchmark 维护建议。\n\n**S6. DEFF 校正的 size-stratified 分析（Appendix C）很扎实。** 对不同家族规模的 ICC 分层分析（Table 9）以及对 simple-mean vs weighted-mean 选择的论证，展示了对 survey statistics 方法论的深入理解。\n\n---\n\n### Weaknesses\n\n#### 方法类\n\n**W-M1 [Should-Fix]: Semi-synthetic 验证框架的 ecological validity 不足。**\n- 具体位置：Section 3.4, Figure 2\n- 问题：Binary response flipping 模型假设 contamination 以均匀概率 p 将错误回答翻转为正确回答。这是最简化的 contamination 模型。真实的 contamination 模式远更复杂：(a) memorization 可能改变 response distribution 而非确定性地修正答案；(b) contamination rate 与 item properties（difficulty、web exposure frequency）可能相关，而非均匀分布；(c) 随机选取 20% items 作为 \"contaminated set\" 不反映真实 contamination 的 subject-dependent 结构。论文展示了清晰的 dose-response 曲线（Figure 2, ΔTPR 从 0.40 到 0.95），但这仅验证了方法对这种特定简化模型的敏感性。Section 4.3 的 null result（DIF 与 web-overlap 正交）可以被解读为 MH-DIF 检测到的并非 contamination，而是其他形式的 temporal change（capability evolution、training methodology shifts）——这一 alternative interpretation 在论文中讨论不足。\n- 建议：增加至少一种更 realistic 的 contamination model（例如 difficulty-dependent injection rate、subject-correlated contamination），或更显式地讨论 ecological validity 的局限。\n\n**W-M2 [Should-Fix]: ΔFPR = 0 guarantee 的 scope 在 abstract 和 Section 1 中被过度表述。**\n- 具体位置：Abstract (\"cross-subject matching (ΔFPR = 0 guarantee)\"), Section 1 第2个贡献点, Section 3.4 Remark\n- 问题：ΔFPR = 0 guarantee 仅在 single-subject contamination 下成立（Section 3.4 Remark 明确说明）。但 abstract 和 introduction 均未限定此条件。Section 4.5 和 Table 7 的 multi-subject injection 实验表明，当 contamination 扩展到 k=10 个 subjects（18% of domains）时，ΔFPR 升至 0.047 ± 0.022。在现实场景中，training data contamination 极可能跨越多个 subjects，使得 ΔFPR = 0 guarantee 的实际适用范围有限。更关键的是，Table 7 显示 k=10 时 ΔFPR = 0.047 而 k=20 时 ΔFPR 降至 ~0.009，这种非单调模式表明当 contamination 足够 pervasive 时，cross-subject matching 可能将 contamination signal 归一化，导致方法在最需要的场景下失灵。\n- 建议：在 abstract 和 Section 1 中明确 \"under single-subject contamination\" 条件；在 Section 5 中讨论 pervasive contamination 场景下的失灵风险。\n\n**W-M3 [Should-Fix]: 验证目标（contamination detection）与应用 claim（measurement instability）之间存在张力。**\n- 具体位置：Section 3.4 vs Section 4.3 vs Section 5.1\n- 问题：Semi-synthetic 验证框架注入的是 contamination（response flipping），验证的是 MH-DIF 作为 contamination detector 的能力。但 real-world 应用中，Section 4.3 表明 DIF flags 与 web-overlap contamination labels 正交，Section 5.1 将 DIF 定位为检测更广义的 \"measurement instability\"（包括 contamination、capability evolution、training methodology shifts 三种不可区分的机制）。这意味着：方法为 X 做了验证，但 claim 检测到了 Y。如果 DIF 主要检测的是 capability evolution 而非 contamination，那么 semi-synthetic injection 验证就不能直接支持 real-world findings 的解读。\n- 建议：(a) 增加非 contamination 来源的 measurement instability 验证（如 ability-distribution shift injection），或 (b) 在 Discussion 中更显式地承认这一解释性 gap。\n\n**W-M4 [Minor]: K=5 stratification 的敏感性分析范围有限。**\n- 具体位置：Table 5, Section 4.1 footnote\n- 问题：K=3 vs K=5 对比（Table 5）显示结果稳健，但 K 的范围过窄。在 5,227 个 examinees 的情况下（远超教育测量的典型样本量），应该测试 K=10 或连续匹配（logistic regression DIF），以排除 coarse stratification 导致的 residual confounding。\n- 建议：补充 K=10 或 continuous matching 的敏感性分析。\n\n#### 实验类\n\n**W-E1 [Should-Fix]: 2023 vs 2024 cohort 比较中的 temporal confound 未完全解决。**\n- 具体位置：Section 3.3, Section 4.2, Section 4.7\n- 问题：temporal 队列划分同时 confound 了多个变量：contamination 程度、architecture 演化（2024 instruct/chat 模型比例更高）、capability scaling、training methodology（RLHF/DPO 普及）。Base-vs-instruct decomposition（Section 4.7）部分解决了 model type confound，但 decomposition 本身将 model type 与 temporal effect 再次混淆（2024 inherently 有更多 instruct models）。Matched-ability 分析（Section 4.4, matched quintiles）控制了 ability level，但未控制 architecture/training methodology 的 confound。论文在 Section 5.1 列出三个 non-exclusive mechanisms 但无法 decompose 各自贡献。\n- 建议：承认这一根本性局限；或设计 within-period 对比（例如同时期的 base vs instruct）来分离机制。\n\n**W-E2 [Minor]: Item-Property Predictive Analysis（Appendix F）结果对 contamination 叙事构成挑战。**\n- 具体位置：Appendix F, Section 5.2\n- 问题：用 item properties（difficulty、discrimination、vocabulary metrics、web-overlap labels）预测 DIF susceptibility 的 logistic regression 仅达 AUC ≈ 0.60，接近随机水平。Web-overlap labels 的 SHAP 贡献 < 0.015。如果已知的 item properties 几乎无法预测哪些 items 会出现 DIF，这引发两个问题：(a) DIF 是否部分捕捉了 noise 而非 systematic signal？(b) 如果无法事前预测 DIF items，Section 5.2 推荐的 \"DIF Audit Protocol\" 的实用价值几何？\n- 建议：在 Discussion 中显式讨论 low predictability 的含义及其对 practical monitoring 的影响。\n\n**W-E3 [Minor]: Half-year granularity 分析（Appendix D）的解读方向值得商榷。**\n- 具体位置：Appendix D\n- 问题：6 个月粒度切分得到 C% = 34.1%，高于全年切分的 31.3%。论文解释为更极化的 cohort composition。但 alternative interpretation 是方法对 cohort composition artifacts 敏感——更小、更异质的组产生更多 DIF flags。这对主要发现的稳定性构成concern。\n- 建议：测试多个时间切点的 C% 稳定性，而非仅展示一个半年切分。\n\n#### 统计类\n\n**W-S1 [Should-Fix]: Simple-mean vs weighted-mean DEFF 的分歧实质性地影响 headline result。**\n- 具体位置：Appendix C, Table 2 (referenced in Section C)\n- 问题：Simple-mean DEFF（n̄ = 62.8）给出 corrected C% = 29.2%；weighted-mean DEFF（n̄_w = 214.5, Kish 1965）给出 corrected C% = 13.5%。两种方法的结果相差约 2 倍。论文以 within-family similarity 不随家族规模增长（ρ_s = −0.009, p = 0.96）为由选择 simple-mean。但 Kish effective cluster size 是 survey statistics 的标准方法；论文的论证是 \"weighted-mean over-corrects\"，但这本身是一个需要证明的 claim，而非给定事实。13.5% 和 29.2% 对应完全不同的 narrative：\"约三成 items 不稳定\" vs \"约一成 items 不稳定\"。\n- 建议：(a) 在正文中同时报告两个估计及其解读差异，而非仅在 Appendix 中讨论；(b) 提供更强的 statistical evidence 支持 simple-mean 的选择（如 simulation study 比较两种校正在已知 DIF rate 下的 coverage）。\n\n**W-S2 [Minor]: Power analysis 依赖已承认 poor fit 的 2PL 参数。**\n- 具体位置：Section 4.1, Appendix A\n- 问题：论文承认 MMLU response matrix 对 unidimensional 2PL model fit 差（\"expected for a 57-subject multidimensional benchmark\"），但 Monte Carlo power analysis 仍使用 2PL 参数。虽然 MH-DIF 本身不依赖 IRT model fit，但 power analysis 的 TPR bounds（0.68–0.80）可靠性受影响。\n- 建议：说明 2PL misfit 对 power estimates 的可能影响方向。\n\n---\n\n### Questions\n\n**Q1:** Cross-subject matching 中，对 within-MMLU DIF 分析，matching variable 具体是什么？是其余 56 个 subjects 的 total score 之和吗？如果是，这个 variable 被 item 数量多的 subjects（如 STEM 类）主导，是否引入隐式权重偏差？\n\n**Q2:** Table 7 显示 multi-subject injection 的 ΔFPR 在 k=10 时为 0.047 但 k=20 时降至 ~0.009。这种非单调模式的原因是什么？如果 pervasive contamination 导致 ΔFPR 降低，这是否意味着方法在 widespread contamination 下会 fail silently？\n\n**Q3:** Abstract 报告 \"27,828 items across all six\" benchmarks。但根据 Figure 6 中各 benchmark 的 N 值（818 + 1,173 + 1,267 + 1,320 + 10,042 + 12,508 = 27,128），总数为 27,128 而非 27,828。请核实。\n\n**Q4:** Leave-one-family-out 分析（Section 4.4）仅移除 non-dominant families（≤15% of cohort）。如果移除 dominant families（Mistral、Llama-3），temporal C% 是否会发生实质变化？这些 mega-families 驱动了 DEFF correction，如果同时驱动了 DIF detection，结果的 robustness 就存疑。\n\n**Q5:** 论文区分了 DIF detection（what）和 causal attribution（why），这是好的实践。但 Section 5.1 最后一段和 Section 4.7 的 base-vs-instruct decomposition 实际上进入了 causal territory，声称提供了 \"positive evidence for mechanisms separation\"。在无法 experimentally isolate mechanisms 的观测研究中，这一 claim 的证据力度如何？\n\n**Q6:** METABENCH 数据中是否有 model quality filtering？Open LLM Leaderboard 上存在大量低质量提交（duplicate models、intentionally overfitting models）。如果未过滤，这些 noise models 是否可能人为膨胀 DIF rates？\n\n---\n\n### Missing References\n\n论文的引用覆盖总体充分。一个可能有价值的补充：\n- Polo et al. (2024) \"TinyBenchmarks\" 在 References 中已有引用但在 Related Work 讨论 IRT-based item selection 时可以更深入地对比方法差异。\n- 未发现明显遗漏的关键文献。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论基础（MH-DIF）扎实，cross-subject matching 理论清晰；但 semi-synthetic validation 的 ecological validity 有限，DEFF 校正方法选择产生 2× 结果分歧，ΔFPR=0 guarantee 的适用范围被过度表述 |\n| Excitement | 3.5/5 | 跨学科方法创新，将成熟的 psychometric 工具引入 LLM 评估；但 validation/application 的 interpretive gap 和 low item-property predictability（AUC ≈ 0.60）限制了实际影响力 |\n| Reproducibility | 4/5 | METABENCH 数据公开，MH procedure 定义清晰，匿名代码仓库可用。DEFF 校正和 semi-synthetic framework 的实现细节充分 |\n| Reviewer Confidence | 4/5 | 我熟悉 DIF 方法论、IRT 在 NLP 中的应用、以及 benchmark contamination 检测文献。仔细检查了核心方法和实验设计 |\n\n---\n\n### Overall Assessment\n\n**Overall: 3.5 (Borderline Conference)**\n\n**一句话总结：** 一篇有实质跨学科创新的论文——将 MH-DIF 引入 LLM benchmark 评估并提出了有意义的方法适配——但 semi-synthetic validation 的 ecological validity 不足、ΔFPR=0 guarantee 的适用范围过度表述、以及 DEFF 校正方法选择导致 headline result 产生 2 倍分歧，这些问题共同削弱了核心 claims 的可靠性。论文的 conceptual contribution（global exposure vs differential functioning 的区分）是重要的，但需要更强的实证支撑来匹配其 ambition。\n\n**升/降分关键：** 若能 (a) 增加一种更 realistic 的 contamination model 验证、(b) 在 abstract/intro 中准确限定 ΔFPR=0 guarantee 的条件、(c) 在正文中更透明地讨论 DEFF 方法选择对结果的影响，可上调至 4.0。\n\n---\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n---\n\n### Summary\n\n本文将教育测量领域的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 方法引入 LLM benchmark 评估，在 METABENCH 数据上（5,227 模型 × 12,508 MMLU items）检测 2023 与 2024 模型队列之间的 temporal measurement instability。核心发现是 27–29% 的 MMLU items（经非独立性校正后）表现出显著的 temporal DIF，但该不稳定性不影响模型排名（ρ ≥ 0.997）。论文引入了 cross-subject matching（ΔFPR = 0 guarantee）、DEFF clustering 校正、semi-synthetic injection 验证框架等方法贡献。总体而言，这是一篇有实质创新的跨学科论文，方法论基础扎实，但在若干关键环节的 claim scoping 和验证充分性上存在改进空间。\n\n---\n\n### Strengths\n\n**S1. 真正的跨学科方法创新。** MH-DIF 在教育测量领域已有数十年积累，但将其系统性地引入 LLM benchmark 评估是新颖的。论文不是简单套用，而是针对 LLM 特有问题做了有意义的方法适配：cross-subject matching 解决了 multi-domain benchmark 中 matching variable 被污染的问题（Section 3.4），DEFF 校正处理了模型家族非独立性（Section C），这些都是 non-trivial 的方法贡献。\n\n**S2. 规模与覆盖面令人印象深刻。** 5,227 个模型 × 12,508 items 的分析规模远超此前 IRT/DIF 在 NLP 领域的应用。跨六个 benchmark 的 replication（Table 3, Figure 6）增加了结果可信度。\n\n**S3. 多层 convergent evidence 设计。** 论文构建了完整的证据链：semi-synthetic injection → Monte Carlo power analysis → structural controls（matched-ability、leave-one-family-out）→ cross-benchmark replication → downstream impact analysis（ranking preservation）。这种多层验证在 NLP 实证论文中并不常见。\n\n**S4. Global exposure 与 differential functioning 的概念区分。** Section 4.3 中 DIF flags 与 web-overlap labels 的正交性结果（Jaccard = 0.206, ψ = 0.012, OR = 1.05 [0.96, 1.15]）以及 Figure 1 的概念图，清晰地建立了 DIF 检测与传统 contamination detection 的理论区别。这对领域的概念框架有贡献。\n\n**S5. Downstream impact 分析提供了实用视角。** Section 4.6 中 ρ ≥ 0.997 的 ranking preservation 以及 Figure 6 中 DIF-ordered vs random removal 的对比，将统计发现转化为可操作的 benchmark 维护建议。\n\n**S6. DEFF 校正的 size-stratified 分析（Appendix C）很扎实。** 对不同家族规模的 ICC 分层分析（Table 9）以及对 simple-mean vs weighted-mean 选择的论证，展示了对 survey statistics 方法论的深入理解。\n\n---\n\n### Weaknesses\n\n#### 方法类\n\n**W-M1 [Should-Fix]: Semi-synthetic 验证框架的 ecological validity 不足。**\n- 具体位置：Section 3.4, Figure 2\n- 问题：Binary response flipping 模型假设 contamination 以均匀概率 p 将错误回答翻转为正确回答。这是最简化的 contamination 模型。真实的 contamination 模式远更复杂：(a) memorization 可能改变 response distribution 而非确定性地修正答案；(b) contamination rate 与 item properties（difficulty、web exposure frequency）可能相关，而非均匀分布；(c) 随机选取 20% items 作为 \"contaminated set\" 不反映真实 contamination 的 subject-dependent 结构。论文展示了清晰的 dose-response 曲线（Figure 2, ΔTPR 从 0.40 到 0.95），但这仅验证了方法对这种特定简化模型的敏感性。Section 4.3 的 null result（DIF 与 web-overlap 正交）可以被解读为 MH-DIF 检测到的并非 contamination，而是其他形式的 temporal change（capability evolution、training methodology shifts）——这一 alternative interpretation 在论文中讨论不足。\n- 建议：增加至少一种更 realistic 的 contamination model（例如 difficulty-dependent injection rate、subject-correlated contamination），或更显式地讨论 ecological validity 的局限。\n\n**W-M2 [Should-Fix]: ΔFPR = 0 guarantee 的 scope 在 abstract 和 Section 1 中被过度表述。**\n- 具体位置：Abstract (\"cross-subject matching (ΔFPR = 0 guarantee)\"), Section 1 第2个贡献点, Section 3.4 Remark\n- 问题：ΔFPR = 0 guarantee 仅在 single-subject contamination 下成立（Section 3.4 Remark 明确说明）。但 abstract 和 introduction 均未限定此条件。Section 4.5 和 Table 7 的 multi-subject injection 实验表明，当 contamination 扩展到 k=10 个 subjects（18% of domains）时，ΔFPR 升至 0.047 ± 0.022。在现实场景中，training data contamination 极可能跨越多个 subjects，使得 ΔFPR = 0 guarantee 的实际适用范围有限。更关键的是，Table 7 显示 k=10 时 ΔFPR = 0.047 而 k=20 时 ΔFPR 降至 ~0.009，这种非单调模式表明当 contamination 足够 pervasive 时，cross-subject matching 可能将 contamination signal 归一化，导致方法在最需要的场景下失灵。\n- 建议：在 abstract 和 Section 1 中明确 \"under single-subject contamination\" 条件；在 Section 5 中讨论 pervasive contamination 场景下的失灵风险。\n\n**W-M3 [Should-Fix]: 验证目标（contamination detection）与应用 claim（measurement instability）之间存在张力。**\n- 具体位置：Section 3.4 vs Section 4.3 vs Section 5.1\n- 问题：Semi-synthetic 验证框架注入的是 contamination（response flipping），验证的是 MH-DIF 作为 contamination detector 的能力。但 real-world 应用中，Section 4.3 表明 DIF flags 与 web-overlap contamination labels 正交，Section 5.1 将 DIF 定位为检测更广义的 \"measurement instability\"（包括 contamination、capability evolution、training methodology shifts 三种不可区分的机制）。这意味着：方法为 X 做了验证，但 claim 检测到了 Y。如果 DIF 主要检测的是 capability evolution 而非 contamination，那么 semi-synthetic injection 验证就不能直接支持 real-world findings 的解读。\n- 建议：(a) 增加非 contamination 来源的 measurement instability 验证（如 ability-distribution shift injection），或 (b) 在 Discussion 中更显式地承认这一解释性 gap。\n\n**W-M4 [Minor]: K=5 stratification 的敏感性分析范围有限。**\n- 具体位置：Table 5, Section 4.1 footnote\n- 问题：K=3 vs K=5 对比（Table 5）显示结果稳健，但 K 的范围过窄。在 5,227 个 examinees 的情况下（远超教育测量的典型样本量），应该测试 K=10 或连续匹配（logistic regression DIF），以排除 coarse stratification 导致的 residual confounding。\n- 建议：补充 K=10 或 continuous matching 的敏感性分析。\n\n#### 实验类\n\n**W-E1 [Should-Fix]: 2023 vs 2024 cohort 比较中的 temporal confound 未完全解决。**\n- 具体位置：Section 3.3, Section 4.2, Section 4.7\n- 问题：temporal 队列划分同时 confound 了多个变量：contamination 程度、architecture 演化（2024 instruct/chat 模型比例更高）、capability scaling、training methodology（RLHF/DPO 普及）。Base-vs-instruct decomposition（Section 4.7）部分解决了 model type confound，但 decomposition 本身将 model type 与 temporal effect 再次混淆（2024 inherently 有更多 instruct models）。Matched-ability 分析（Section 4.4, matched quintiles）控制了 ability level，但未控制 architecture/training methodology 的 confound。论文在 Section 5.1 列出三个 non-exclusive mechanisms 但无法 decompose 各自贡献。\n- 建议：承认这一根本性局限；或设计 within-period 对比（例如同时期的 base vs instruct）来分离机制。\n\n**W-E2 [Minor]: Item-Property Predictive Analysis（Appendix F）结果对 contamination 叙事构成挑战。**\n- 具体位置：Appendix F, Section 5.2\n- 问题：用 item properties（difficulty、discrimination、vocabulary metrics、web-overlap labels）预测 DIF susceptibility 的 logistic regression 仅达 AUC ≈ 0.60，接近随机水平。Web-overlap labels 的 SHAP 贡献 < 0.015。如果已知的 item properties 几乎无法预测哪些 items 会出现 DIF，这引发两个问题：(a) DIF 是否部分捕捉了 noise 而非 systematic signal？(b) 如果无法事前预测 DIF items，Section 5.2 推荐的 \"DIF Audit Protocol\" 的实用价值几何？\n- 建议：在 Discussion 中显式讨论 low predictability 的含义及其对 practical monitoring 的影响。\n\n**W-E3 [Minor]: Half-year granularity 分析（Appendix D）的解读方向值得商榷。**\n- 具体位置：Appendix D\n- 问题：6 个月粒度切分得到 C% = 34.1%，高于全年切分的 31.3%。论文解释为更极化的 cohort composition。但 alternative interpretation 是方法对 cohort composition artifacts 敏感——更小、更异质的组产生更多 DIF flags。这对主要发现的稳定性构成concern。\n- 建议：测试多个时间切点的 C% 稳定性，而非仅展示一个半年切分。\n\n#### 统计类\n\n**W-S1 [Should-Fix]: Simple-mean vs weighted-mean DEFF 的分歧实质性地影响 headline result。**\n- 具体位置：Appendix C, Table 2 (referenced in Section C)\n- 问题：Simple-mean DEFF（n̄ = 62.8）给出 corrected C% = 29.2%；weighted-mean DEFF（n̄_w = 214.5, Kish 1965）给出 corrected C% = 13.5%。两种方法的结果相差约 2 倍。论文以 within-family similarity 不随家族规模增长（ρ_s = −0.009, p = 0.96）为由选择 simple-mean。但 Kish effective cluster size 是 survey statistics 的标准方法；论文的论证是 \"weighted-mean over-corrects\"，但这本身是一个需要证明的 claim，而非给定事实。13.5% 和 29.2% 对应完全不同的 narrative：\"约三成 items 不稳定\" vs \"约一成 items 不稳定\"。\n- 建议：(a) 在正文中同时报告两个估计及其解读差异，而非仅在 Appendix 中讨论；(b) 提供更强的 statistical evidence 支持 simple-mean 的选择（如 simulation study 比较两种校正在已知 DIF rate 下的 coverage）。\n\n**W-S2 [Minor]: Power analysis 依赖已承认 poor fit 的 2PL 参数。**\n- 具体位置：Section 4.1, Appendix A\n- 问题：论文承认 MMLU response matrix 对 unidimensional 2PL model fit 差（\"expected for a 57-subject multidimensional benchmark\"），但 Monte Carlo power analysis 仍使用 2PL 参数。虽然 MH-DIF 本身不依赖 IRT model fit，但 power analysis 的 TPR bounds（0.68–0.80）可靠性受影响。\n- 建议：说明 2PL misfit 对 power estimates 的可能影响方向。\n\n---\n\n### Questions\n\n**Q1:** Cross-subject matching 中，对 within-MMLU DIF 分析，matching variable 具体是什么？是其余 56 个 subjects 的 total score 之和吗？如果是，这个 variable 被 item 数量多的 subjects（如 STEM 类）主导，是否引入隐式权重偏差？\n\n**Q2:** Table 7 显示 multi-subject injection 的 ΔFPR 在 k=10 时为 0.047 但 k=20 时降至 ~0.009。这种非单调模式的原因是什么？如果 pervasive contamination 导致 ΔFPR 降低，这是否意味着方法在 widespread contamination 下会 fail silently？\n\n**Q3:** Abstract 报告 \"27,828 items across all six\" benchmarks。但根据 Figure 6 中各 benchmark 的 N 值（818 + 1,173 + 1,267 + 1,320 + 10,042 + 12,508 = 27,128），总数为 27,128 而非 27,828。请核实。\n\n**Q4:** Leave-one-family-out 分析（Section 4.4）仅移除 non-dominant families（≤15% of cohort）。如果移除 dominant families（Mistral、Llama-3），temporal C% 是否会发生实质变化？这些 mega-families 驱动了 DEFF correction，如果同时驱动了 DIF detection，结果的 robustness 就存疑。\n\n**Q5:** 论文区分了 DIF detection（what）和 causal attribution（why），这是好的实践。但 Section 5.1 最后一段和 Section 4.7 的 base-vs-instruct decomposition 实际上进入了 causal territory，声称提供了 \"positive evidence for mechanisms separation\"。在无法 experimentally isolate mechanisms 的观测研究中，这一 claim 的证据力度如何？\n\n**Q6:** METABENCH 数据中是否有 model quality filtering？Open LLM Leaderboard 上存在大量低质量提交（duplicate models、intentionally overfitting models）。如果未过滤，这些 noise models 是否可能人为膨胀 DIF rates？\n\n---\n\n### Missing References\n\n论文的引用覆盖总体充分。一个可能有价值的补充：\n- Polo et al. (2024) \"TinyBenchmarks\" 在 References 中已有引用但在 Related Work 讨论 IRT-based item selection 时可以更深入地对比方法差异。\n- 未发现明显遗漏的关键文献。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论基础（MH-DIF）扎实，cross-subject matching 理论清晰；但 semi-synthetic validation 的 ecological validity 有限，DEFF 校正方法选择产生 2× 结果分歧，ΔFPR=0 guarantee 的适用范围被过度表述 |\n| Excitement | 3.5/5 | 跨学科方法创新，将成熟的 psychometric 工具引入 LLM 评估；但 validation/application 的 interpretive gap 和 low item-property predictability（AUC ≈ 0.60）限制了实际影响力 |\n| Reproducibility | 4/5 | METABENCH 数据公开，MH procedure 定义清晰，匿名代码仓库可用。DEFF 校正和 semi-synthetic framework 的实现细节充分 |\n| Reviewer Confidence | 4/5 | 我熟悉 DIF 方法论、IRT 在 NLP 中的应用、以及 benchmark contamination 检测文献。仔细检查了核心方法和实验设计 |\n\n---\n\n### Overall Assessment\n\n**Overall: 3.5 (Borderline Conference)**\n\n**一句话总结：** 一篇有实质跨学科创新的论文——将 MH-DIF 引入 LLM benchmark 评估并提出了有意义的方法适配——但 semi-synthetic validation 的 ecological validity 不足、ΔFPR=0 guarantee 的适用范围过度表述、以及 DEFF 校正方法选择导致 headline result 产生 2 倍分歧，这些问题共同削弱了核心 claims 的可靠性。论文的 conceptual contribution（global exposure vs differential functioning 的区分）是重要的，但需要更强的实证支撑来匹配其 ambition。\n\n**升/降分关键：** 若能 (a) 增加一种更 realistic 的 contamination model 验证、(b) 在 abstract/intro 中准确限定 ΔFPR=0 guarantee 的条件、(c) 在正文中更透明地讨论 DEFF 方法选择对结果的影响，可上调至 4.0。\n\n---\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-23T06:02:50.455279+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3918
}
```

</details>

---


### Assistant

_source line 1036 · 2026-05-23T06:02:58.985249+00:00_

审稿意见已提交给 Review Director。

评审结论：**Overall 3.5 (Borderline Conference)**。

核心判断：跨学科方法创新有实质价值（MH-DIF + cross-subject matching + DEFF correction），但三个 Should-Fix 级别问题需要解决：
1. Semi-synthetic validation 的 ecological validity 不足（binary response flipping 过于简化）
2. ΔFPR=0 guarantee 在 abstract 中未限定为 single-subject contamination
3. Simple-mean vs weighted-mean DEFF 产生 29.2% vs 13.5% 的 2× 分歧，方法选择对 headline result 影响过大

若能修订 claim scoping 并补充更 realistic 的 validation，可上调至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 35

## Round 35

2 recorded events


### User

_source line 1037 · 2026-05-23T06:03:59.502285+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 — Round 1 审稿意见

### Summary

本文将教育测量学中的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，使用 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items），发现 2023 与 2024 模型群组间约 27–29% 的 MMLU 题目存在时序 DIF（ETS Category C），且该信号与 web-overlap 污染标签近乎正交（Jaccard = 0.206）。论文提出 cross-subject matching 策略控制假阳率，通过半合成注入验证检测力，并在 6 个 METABENCH benchmark 上复现了结果。

### Weaknesses

**W-N1 [Should-Fix]** 方法论新颖性有限——核心是已有方法的领域迁移

论文的核心方法（MH-DIF + ETS 分类）是 1988 年提出的标准教育测量技术，作者在 Section 2 明确承认 "We do not modify the MH procedure; our contribution is the application context." 三个 claimed contributions 中：
- "Orthogonal constructs" 是经验发现而非方法创新；
- "Temporal DIF audit framework" 是现有技术的组合（cross-subject matching 在 DIF 文献中有先例，Nandakumar 1993; Donoghue 1993）；
- "Temporal measurement instability at scale" 是规模而非新颖性。

论文的适配工作（cross-subject matching、DEFF 校正）是工程性的而非方法论性的。对于 EMNLP 主会议，期望看到更强的方法论贡献或至少某种分析方法的显著扩展。

**W-N2 [Must-Fix]** 无法归因 DIF 机制严重限制实际价值

论文反复承认 DIF 只能检测 "that" 而非 "why"（Abstract, Section 5.1, Limitations），并列举三种可能机制（differential contamination, capability evolution, training methodology shifts），但未提供任何方法区分它们。Section 5.1 的混合机制分析（Appendix A, Mixed-mechanism injection）表明半合成模拟无法匹配 instruct 模型的观测模式（simulated ρ_instruct = -0.302 vs. observed -0.079），进一步暴露了归因困难。

这导致核心实用困境：如果 benchmark 维护者发现 C% = 31%，但不知道这代表污染、能力进化还是训练方法变化，该采取什么行动？Section 5.2 的 Monitor/Flag/Act 协议基于 C% 阈值给出行动建议，但在机制不明的情况下，"Act" 层面的"stable-item rankings"可能移除的恰恰是反映合法能力变化的 items。

**W-C1 [Should-Fix]** 结论段过于简略，未能收束论证

Section 6 Conclusion 仅有一句话。缺少：(1) 关键发现的综合讨论；(2) 研究局限性的简述；(3) 未来方向。这一段的极端简短（配合 `\vspace{-28pt}`）是空间不足的明显症状。

**W-C2 [Should-Fix]** DIF 百分比的不确定性范围过宽，核心结论模糊

论文的 headline number 是 31.3%，但经过不同校正方法后，范围从 13.5%（weighted-mean DEFF）到 53.2%（cluster bootstrap 上界）。4× 的范围使得核心结论难以评估。

**W-F1 [Must-Fix]** `\enlargethispage` 使用极度激进，涉嫌违反页数限制精神

`discussion.tex:3` 使用 `\enlargethispage*{10\baselineskip}`——即在 Discussion 页面增加约 10 行文本空间（≈ 1.7 英寸 / 4.3 厘米）。`experiments.tex:46` 另有 `\enlargethispage*{4\baselineskip}`。此外还有多处负 vspace。综合效果是在名义上 8 页的限制内塞入了约 9 页的内容。

**W-W1 [Should-Fix]** 论文过于 notation-heavy，可读性受损

**W-W2 [Minor]** 术语一致性 — "measurement instability" 和 "temporal DIF" 交替使用

### Questions

**Q1.** 从 benchmark 维护者的角度，DIF 审计提供了什么 contamination detection 和常规 benchmark analysis 无法提供的独特价值？

**Q2.** Within-family (Llama-2 vs. 3) 的 C% = 61.3%，远高于 Temporal 的 31.3%。这是否说明 DIF 主要反映的是 model architecture/training 差异而非 benchmark integrity 问题？

**Q3.** k=20 时 ΔFPR = 0.069 相对于 DEFF-adjusted 的 13.5% 下界就是 50% 的相对误差，如何确保结论的稳健性？

**Q4.** 是否考虑过 logistic regression DIF 或 SIBTEST 作为方法论比较？

**Q5.** Figure 1 概念示意图在空间紧张时是否值得？

### Missing References
1. Multi-group CFA / alignment methods（Millsap & Olivera-Aguilar 2012; Asparouhov & Muthén 2014）
2. Dataset shift / concept drift 文献（Quinonero-Candela et al. 2009）

### Overall Assessment
**3.5 — Borderline Conference**
Soundness 4/5, Excitement 3/5, Reproducibility 5/5

---

请逐条回应上述 Weaknesses 和 Questions，特别关注你作为方法/实验审稿人的视角是否支持或反对 Reviewer 2 的判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1038 · 2026-05-23T06:06:25.120809+00:00_

逐条回应 Reviewer 2 的审稿意见。

---

**[REBUT] W-N1: 方法论新颖性有限**

R2 的论述有两处不准确。第一，R2 引用 Nandakumar (1993) 和 Donoghue (1993) 作为 cross-subject matching 的先例，但这些工作讨论的是 **purified subtest matching**（在同一测试内剔除 studied items 后用剩余 items 匹配），而非论文提出的 **cross-benchmark matching**（用完全不同 benchmark 的 total score 作为 matching variable）。后者在 LLM multi-domain evaluation 的语境下是新的适配，因为它解决了 LLM benchmarks 中跨 subject contamination 同时发生的问题——这在教育测量中不存在类似的大规模情境。第二，DEFF 校正（Appendix C）针对 model family 结构的 size-stratified ICC 分析不是 "工程性" 工作；它需要建立 LLM model families 的 clustering 特性（Table 9 的 ICC 随 family size 递减），这是领域特有的实证发现。

但 R2 的核心判断——论文的贡献以应用和实证为主而非方法论突破——我认为是正确的。对于 EMNLP，应用性贡献是完全可以接收的，问题在于应用的 insights 是否足够 compelling。这取决于 W-N2 中机制归因问题的严重程度。

---

**[REBUT] W-N2: 无法归因 DIF 机制（R2 标注 Must-Fix，我认为 Should-Fix）**

R2 将此标为 Must-Fix，理由是不知道机制就无法采取行动。我认为这过度要求了。

教育测量中 DIF 的标准用途恰好是 **diagnostic without attribution**：ETS 的实际操作流程（Zieky, 2006）是先检测 DIF items、再由 subject-matter experts 判断 mechanism 和 action——而非要求统计方法本身提供因果解释。论文在 Section 5.2 提出的 Monitor/Flag/Act protocol 正是遵循了这一范式。R2 担忧 "stable-item rankings 可能移除反映合法能力变化的 items"，但论文已在 Section 4.6 中明确说明：ρ ≥ 0.997 表明移除 C items 几乎不改变排名（Figure 6），因此 practical harm 极低。

Section 5.1 的混合机制分析（simulated ρ_instruct = −0.302 vs. observed −0.079）确实显示 semi-synthetic framework 无法完全复现 real-world 模式，但这恰恰是论文诚实报告局限性的体现，而非应被惩罚的缺陷。

我在自己的 W-M3 中也指出了 validation/application 之间的张力，但归因困难本身不应是 Must-Fix——这是所有观测性 DIF 研究的固有局限。Should-Fix：要求论文在 Discussion 中更清晰地界定 DIF 审计的决策边界即可。

---

**[AGREE] W-C1: Conclusion 过于简略**

同意。Section 6 Conclusion 极度简短（实际上就是一句话加上 `\vspace{-28pt}`），在空间约束下可以理解，但作为独立的审稿意见，确实缺少对核心发现的综合收束。不过严重程度为 Minor 而非 Should-Fix，因为 Section 5 Discussion 已承担了大部分 conclusion 功能。

---

**[REBUT] W-C2: DIF 百分比不确定性范围过宽（4×）**

R2 将范围表述为 "13.5% 到 53.2%（4× range）"，这一 framing 有误导性。53.2% 是 cluster bootstrap CI 的 **上界**，不是 point estimate；13.5% 是 weighted-mean DEFF 的保守下界。论文的两个 convergent point estimates 是 simple-mean DEFF（29.2%）和 cluster bootstrap lower bound（26.7%），两者的一致性很高（Section C, Appendix）。

更准确的不确定性范围应是：point estimate 27–29%，conservative lower bound 13.5%。这是 ~2× 范围而非 4×。我在自己的 W-S1 中也指出了 simple-mean vs weighted-mean 的 2× 分歧，但论文在 Section H 中提供了 evidence（ρ_s = −0.009, p = 0.96：within-family similarity 不随 family size 增长）支持 simple-mean 的选择。R2 将上界和下界混合呈现为 "范围" 是不恰当的。

---

**[AGREE] W-F1: \enlargethispage 使用激进**

同意这是一个值得关注的格式问题。`\enlargethispage*{10\baselineskip}` 在 Discussion 页面增加约 10 行空间（~4.3cm），效果相当显著。结合 experiments.tex 中的 `\enlargethispage*{4\baselineskip}` 和多处负 vspace，实际内容密度确实超出了标准 8 页格式允许的范围。

但我不会标为 Must-Fix，而是 Should-Fix。原因：(a) `\enlargethispage` 是 LaTeX 的合法命令，许多被接收的 ACL 论文使用了类似技巧；(b) 最终判定权在 AC 和 program chairs，reviewer 可以 flag 但不应以此作为 reject 理由；(c) 如果 Discussion 缩减导致论文无法回应 R2 自己的 W-N2（机制讨论不足），那就陷入矛盾。建议作者压缩部分内容至 Appendix，但不应作为 acceptance-blocking issue。

---

**[REBUT] W-W1: 论文过于 notation-heavy**

不同意。论文涉及 MH 统计量（公式 1-2）、ETS C 分类阈值、DEFF 校正、cross-subject matching 的形式化——这些都需要 precise notation 来避免歧义。对于一篇方法论导向的论文，Section 3 的 notation density 在 ACL/EMNLP 的 measurement/evaluation track 中是正常水平。如果减少 notation，反而可能损害 reproducibility（R2 自己给了 Reproducibility 5/5）。

---

**[AGREE] W-W2: 术语一致性**

同意，Minor 级别。"Temporal DIF" 是具体的统计发现，"measurement instability" 是更广义的概念。两者并非不一致，但论文应在首次引入时明确定义二者关系（例如 "we use temporal measurement instability to refer to the phenomenon, and temporal DIF as its statistical operationalization"）。

---

### Questions 回应

**[REBUT] Q1: DIF 审计的独特价值**

R2 的问题隐含假设——如果 DIF 与 contamination detection 提供类似信息就没有价值。但 Section 4.3 恰恰表明两者 **正交**（Jaccard = 0.206, OR = 1.05）。DIF 提供的独特价值是：识别 measurement properties 跨时间变化的 items，不论原因是否为 contamination。这在 benchmark 维护中的直接应用是：当 C% 升高时，benchmark 维护者知道需要审查哪些 items，即使不知道 root cause。常规 benchmark analysis（accuracy tracking）无法定位到 item level；contamination detection 只覆盖 web-exposed items。

---

**[AGREE] Q2: Within-family C% = 61.3% 的含义**

这是一个很好的观察。Within-family DIF（Llama-2 vs Llama-3）的 C% = 61.3% 远高于 temporal DIF 的 31.3%，强烈暗示 DIF 主要捕捉的是 model architecture/training paradigm 差异，而非 benchmark 本身的 integrity 问题。这与我的 W-M3（validation/application 张力）和 W-E1（temporal confound）一致：如果 family-level capability shifts 产生更强的 DIF signal，那么 temporal DIF 中的相当比例可能同样反映 capability evolution 而非 contamination。论文应更显式地讨论这一发现对 contamination 叙事的影响。

---

**[REBUT] Q3: k=20 ΔFPR 与 DEFF 下界的比值**

R2 引用 k=20 时 ΔFPR = 0.069，但据我对 Table 7 和正文（Section 4.5）的阅读，k=20 的 ΔFPR 约为 0.009 ± 0.018，而非 0.069。ΔFPR = 0.047 ± 0.022 是 k=10 的数值。如果 R2 的数字来源有误，那么 "50% 相对误差" 的计算也不成立。即使取 k=10 的 0.047，相对于 simple-mean DEFF adjusted C% 29.2%，相对误差约 16%，这是更合理的 concern 范围。建议 R2 核实数字来源。

---

**[AGREE] Q4: 方法论比较（logistic regression DIF / SIBTEST）**

同意。我在自己的 Q1 中也提出了 continuous matching（logistic regression DIF）的建议。在 5,227 个 examinees 的规模下，logistic regression DIF 可以避免 K-stratification 的信息损失，SIBTEST 可以检测 non-uniform DIF。至少应作为 sensitivity check 呈现。

---

**[REBUT] Q5: Figure 1 的空间价值**

不同意。Figure 1 以视觉方式清晰建立了 global contamination vs differential contamination 的概念区分，这是论文的核心 conceptual contribution（也是 S4 的基础）。对于跨学科读者（NLP 研究者不熟悉 DIF 概念），这张概念图的教学价值大于它占用的空间。在空间压力下，压缩 Section 3.1/3.2 的文字描述比移除 Figure 1 更合理。

---

### Missing References 回应

**[AGREE]** Multi-group CFA / measurement invariance alignment methods（Millsap & Olivera-Aguilar 2012; Asparouhov & Muthén 2014）确实是相关文献，论文在 Related Work 讨论 measurement invariance 时（Section 2，MIMIC models 段落）可以补充引用。

**[REBUT]** Dataset shift / concept drift（Quinonero-Candela et al. 2009）与 DIF 的关联较弱。DIF 是 item-level analysis，dataset shift 是 distribution-level analysis。两者在不同粒度上操作，引用关联性有限。

---

### 总结

R2 的 6 条 Weaknesses 中，我同意 3 条（W-C1 同意但降级为 Minor、W-F1 同意但降级为 Should-Fix、W-W2 同意 Minor），反驳 3 条（W-N1 部分反驳、W-N2 反驳 Must-Fix 定级但同意 Should-Fix、W-C2 反驳 4× framing）。R2 的 Questions 中 Q2 是最有洞察力的——within-family C% = 61.3% 对论文的 contamination narrative 构成真正挑战。

R2 给出 3.5 (Borderline Conference)，与我的评分一致。我认为 R2 的 Excitement 3/5 偏低——跨学科方法引入本身有价值，即使核心方法是已有技术。Soundness 4/5 偏高——考虑到 DEFF 分歧和 ecological validity 问题，3.5 更合适。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 36

## Round 36

48 recorded events


### User

_source line 1039 · 2026-05-23T07:56:56.176287+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）

### Venue 信息
- **目标 venue**: EMNLP 2026（通过 ACL Rolling Review 投稿）
- **页数限制**: 正文 ≤ 8 页，参考文献无限制，Limitations 不计入页数
- **模板**: ACL 格式（`\usepackage[review]{acl}`）
- **匿名规则**: double-blind
- **附录**: 允许，不计入页数

### 论文文件
- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/submitted.pdf`
- 各章节在 `paper/sections/` 目录下

### 你的审查侧重

**核心任务：评估方法论严谨性、实验设计合理性、统计分析正确性。**

请重点审查以下方面：

1. **MH-DIF 方法应用**：
   - MH procedure 在 LLM benchmark 场景下的适用性假设是否成立？
   - Cross-subject matching 的 ΔFPR=0 claim 是否严谨？边界条件（k subjects）讨论是否充分？
   - ETS C 分类的双阈值（效应量+显著性）在 N=5,227 下几乎自动满足显著性，这对结果的影响是否充分讨论？

2. **DEFF 非独立性校正**：
   - Simple-mean vs weighted-mean DEFF 的选择论证是否有说服力？
   - 27-29% vs 13.5% 的范围呈现是否透明、合理？
   - Family structure 的处理（graduated de-duplication、LOFO）是否充分？

3. **Semi-synthetic 验证框架**：
   - Binary response flipping 作为 injection model 的 ecological validity
   - Dose-response 曲线的解释力
   - Difficulty-dependent injection 的结果解读

4. **控制实验和敏感性分析**：
   - Random split, ability-quintile, matched-ability 控制是否充分排除替代解释？
   - Temporal confound（2023 vs 2024 同时 confound architecture/training/capability）的处理
   - Within-family (Llama-2 vs 3) 分析的逻辑

5. **Cross-benchmark 复制**：
   - 6 个 METABENCH benchmark 结果的一致性和差异性解释
   - GSM1K 探索性分析的权重是否恰当

6. **统计报告**：
   - 置信区间、效应量、p值的报告是否完整规范？
   - 多重比较问题的处理
   - Bootstrap CI 的合理性

请按以下格式输出审稿意见：
- **Summary**（2-3句概述论文）
- **Strengths**（逐条，标注 S1, S2, ...）
- **Weaknesses**（逐条，标注 W-M1 方法, W-E1 实验, W-S1 统计等，并标明 Must-Fix / Should-Fix / Minor）
- **Questions**（需要作者澄清的问题）
- **Missing References**（遗漏的重要相关工作）
- **Overall Assessment**（评分 + 置信度）

评分标准（ARR/EMNLP 2026）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-23T07:57:03.461942+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-23T07:57:03.713470+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1042 · 2026-05-23T07:57:07.996908+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1043 · 2026-05-23T07:57:10.259752+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1044 · 2026-05-23T07:57:15.033277+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about the ACL Rolling Review 2026 reviewer guidelines, review form, and criteria:

## Reviewer Guidelines

The recommended workflow is to (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. If you feel qualified to review some aspects of the paper but not others (e.g. experimental results but not the formal proofs), please state in the review if you did not check some major parts, such as proofs, 
…[truncated 1037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7036
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-23T07:57:17.448073+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 582.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 551.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p9.png\", \"width\": 1
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7188
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-23T07:57:25.145445+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. I need every field name, its scale (e.g. 1-5), and the description of each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. I need every field name, its scale (e.g. 1-5), and the description of each score level."
  }
}
```

</details>

---


### Tool call

_source line 1047 · 2026-05-23T07:57:26.100471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-23T07:57:26.655183+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-23T07:57:27.567084+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1466
}
```

</details>

---


### Tool result

_source line 1050 · 2026-05-23T07:57:27.572571+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 917
}
```

</details>

---


### Tool call

_source line 1051 · 2026-05-23T07:57:27.573052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-23T07:57:28.175719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-23T07:57:28.528657+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1054 · 2026-05-23T07:57:28.679820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1055 · 2026-05-23T07:57:28.932940+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool result

_source line 1056 · 2026-05-23T07:57:29.539216+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool result

_source line 1057 · 2026-05-23T07:57:33.406366+00:00_

# ACL Rolling Review Form - Complete Structure

## Core Review Dimensions

**1. Paper Summary**
- Open-ended field for describing paper content and identifying misunderstandings

**2. Summary of Strengths**
- Open-ended field for publication-worthy contributions

**3. Summary of Weaknesses**
- Open-ended field; numbered concerns encouraged for author responses

**4. Comments/Suggestions/Typos**
- Open-ended field for improvement suggestions

## Scored Dimensions

**5. Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct...familiar with related work"
- 4: "Quite sure...unlikely, though conceivable, I missed something"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend...fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

**6. Soundness** (1-5 scale, with .5 increments)
- 5: "Excellent: one of the most thorough"
- 4: "Strong: sufficient support for claims"
- 3: "Acceptable: sufficient support for main claims"
- 2: "Poor: main claims not sufficiently supported"
- 1: "Major Issues: not sufficiently thorough"

**7. Excitement** (1-5 scale, with .5 increments)
- 5: "Highly Exciting: would recommend widely"
- 4: "Exciting: would mention to others"
- 3: "Interesting: might mention to others"
- 2: "Potentially Interesting: doesn't resonate personally"
- 1: "Not Exciting: unlikely resonates with community"

**8. Overall Assessment** (1-5 scale, with .5 increments)
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

**9. Best Paper Justification**
- Required if rating 5 or 4.5

## Additional Sections

**10. Limitations and Societal Impact** (open-ended)

**11. Ethical Concerns** (open-ended)

**12. Needs Ethics Review** (yes/no with explanation)

**13. Reproducibility** (1-5 scale)
- 5: Easy reproduction
- 4: Mostly reproducible
- 3: Reproducible with difficulty
- 2: Hard to reproduce
- 1: Ca
…[truncated 455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8260
}
```

</details>

---


### Tool call

_source line 1058 · 2026-05-23T07:57:42.097987+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1059 · 2026-05-23T07:57:42.602884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1060 · 2026-05-23T07:57:43.459133+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool result

_source line 1061 · 2026-05-23T07:57:43.460834+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-23T07:57:43.461391+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1063 · 2026-05-23T07:57:43.967935+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1064 · 2026-05-23T07:57:44.471778+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool call

_source line 1065 · 2026-05-23T07:57:44.573888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1066 · 2026-05-23T07:57:44.727717+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 759
}
```

</details>

---


### Tool result

_source line 1067 · 2026-05-23T07:57:45.331413+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-23T07:57:52.662900+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-17",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-17",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-23T07:57:53.772538+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 586.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 483.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.1}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 440.1}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 296.2}], \"total_pages\": 17, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-23T07:57:59.244906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1071 · 2026-05-23T07:58:00.201640+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-23T07:58:00.352690+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 1073 · 2026-05-23T07:58:00.654889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-23T07:58:01.160096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-23T07:58:02.117334+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1764
}
```

</details>

---


### Tool result

_source line 1076 · 2026-05-23T07:58:02.118755+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1463
}
```

</details>

---


### Tool call

_source line 1077 · 2026-05-23T07:58:02.119168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1078 · 2026-05-23T07:58:02.623191+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1463
}
```

</details>

---


### Tool call

_source line 1079 · 2026-05-23T07:58:02.623652+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1080 · 2026-05-23T07:58:03.027989+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 1081 · 2026-05-23T07:58:03.028529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1082 · 2026-05-23T07:58:03.582250+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool result

_source line 1083 · 2026-05-23T07:58:03.685506+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 1084 · 2026-05-23T08:02:51.542874+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿意见 — Round 1\n\n**论文**：Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n\n---\n\n### Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM 基准评测，在 METABENCH 数据集（5,227 模型 × 12,508 MMLU items）上发现约 27-29%（经非独立性校正后）的 items 在 2023 vs 2024 模型 cohort 间表现出显著的时序 DIF。论文进一步证明 DIF 标记与 web-overlap 污染标签在统计上正交（Jaccard ≈ 0.206，κ = 0.012），并通过 semi-synthetic 注入框架验证了 MH-DIF 的检测能力。论文将发现定位为「测量不稳定性」而非「污染检测」，提出 DIF 审计作为基准评测的心理测量学预筛工具。\n\n---\n\n### Strengths\n\n**S1. 规模与系统性**：5,227 模型 × 12,508 items 的全矩阵分析在 LLM 评测领域属罕见规模。五种 cohort 设计（temporal、ability-quintile、matched-ability、within-family、random split）构成了严谨的控制体系（Table 1, Table 2）。\n\n**S2. 非独立性校正框架扎实**：认识到 LLM model families 违反独立性假设并提出 DEFF 校正是重要的方法论贡献。同时提供 simple-mean DEFF 和 family-level cluster bootstrap 两个独立校正路径，且两者收敛于相近区间（26.7%-29.2%），增强了结果可信度（Section 4.2, Appendix E）。\n\n**S3. Cross-subject matching 的 FPR 保证**：Section 3.4 对单科目污染场景下 ΔFPR = 0 的构造性证明是精巧的——用不同 benchmark 的总分作为 matching variable 从根本上隔离了被测科目的污染信号。这一设计在 LLM 评测中具有独立价值。\n\n**S4. DIF 与 web-overlap 的正交性发现**：κ = 0.012、OR = 1.05、Jaccard 在 permutation null 区间内（Section 4.3），统计支撑充分。这一发现对理解 benchmark 质量问题的多维性具有概念性贡献——global exposure 和 differential functioning 确实捕捉了不同现象。\n\n**S5. 跨 benchmark 复制**：六个 METABENCH benchmark 均表现出时序 DIF（Table 3），增强了结论的普适性。GSM8K 的探索性分析（Section 4.7, Appendix F）恰当地标注为描述性分析。\n\n**S6. 下游影响分析有实践价值**：Figure 4 展示 DIF-ordered 移除对模型排名的影响（flip rate 33.6%），Table 2 的 matched-ability 控制（C% = 28.35%）排除了纯能力差异解释，这些分析将方法论发现与实际评测决策相连接。\n\n**S7. 机制分析（Appendix B）虽为探索性但有深度**：排除论证、difficulty-direction interaction、mixed-injection 分析展示了认真的因果推理尝试，即使最终未能完全区分机制。\n\n---\n\n### Weaknesses\n\n**W-M1 [Must-Fix] 时序混淆是论文最大的解释性缺口**\n\n- **位置**：Section 5.1, Section 3.3, Appendix B\n- **问题**：2023 vs 2024 model cohort 在架构（Transformer variants）、训练范式（SFT/RLHF/DPO 演进）、数据规模、能力水平上同时变化。论文将 DIF 定义为「items function differently across cohorts」（Section 5.1），但在 LLM 场景下，不同代模型对不同 item 类型展现不同能力 profile 是 **预期行为**——这与教育测量中同一课程体系下不同人群的 DIF（预期为零）有本质区别。\n- **具体地说**：Section 5.1 报告 base models 在难题上提升（ρ = −0.570）而 instruct models 在易题上提升（ρ near-zero gradient），但这可能完全反映了合法的训练方法论进步（如 RLHF 对易题的 ceiling effect 提升），而非测量的不稳定性。论文的 Appendix B 排除分析列出三种机制但承认无法区分。\n- **为什么影响接收**：核心 claim「27-29% of items exhibit temporal measurement instability」的可解释性取决于是否能将 legitimate capability evolution 与 genuine measurement dysfunction 区分开。如果无法区分，DIF rate 作为 benchmark 质量指标的实践价值存疑。\n- **建议**：(a) 明确讨论「在 LLM 场景下什么样的 DIF 是预期的、可接受的」——可以借鉴 Camilli and Shepard (1994) 对 impact vs bias 的区分；(b) 考虑引入 item-level covariates（如 item difficulty, discrimination, subject domain）作为 DIF 的解释变量，区分可解释的 DIF（由 item 特征预测）和残余 DIF；(c) 更审慎地限定 claim——将「measurement instability」改为「differential item functioning across model generations」，让读者自行判断这是否构成 instability。\n\n**W-M2 [Should-Fix] DEFF 估计范围过宽，首选估计的论证不够充分**\n\n- **位置**：Section 4.2, Appendix E\n- **问题**：Simple-mean DEFF（n̄ = 62.8）给出调整后 C% = 29.2%，weighted-mean DEFF（n̄ reflecting effective cluster size）给出 C% = 13.5%。两者相差 2 倍以上。论文以「within-family similarity is flat across family sizes (r_s = −0.03)」为由偏好 simple-mean，但这一论证存在逻辑缺口：\n  - r_s = −0.03 说明 ICC 不随 family size 变化，但这不意味着应该用 simple-mean。在 survey methodology 中，当 clusters 大小不等时，weighted-mean 更能反映随机抽取一个 unit 所经历的实际 design effect（Kish, 1965）。\n  - 更关键的是，论文的 50 个 families 中大 families（Llama-3 n=308, Mistral n=547 等）贡献了大部分 models。一个从 5,227 models 中随机抽取的 model 更可能来自大 family，因此 weighted-mean 可能更合适。\n- **为什么影响评分**：13.5% vs 29.2% 的差距直接影响读者对 benchmark 质量问题严重程度的判断。\n- **建议**：(a) 展示 DEFF 敏感性分析（如移除最大 2-3 个 families 后的变化）；(b) 在正文中并列呈现两个估计，而非将 13.5% 降级为 footnote-level 的「lower bound」；(c) 讨论在什么条件下各估计更合适。\n\n**W-M3 [Should-Fix] Semi-synthetic 注入模型的生态效度有限**\n\n- **位置**：Section 3.4, Section 4.5, Figure 2\n- **问题**：Binary response flipping（以 exploitation rate p 随机翻转正确答案为错误）是对真实污染的粗糙近似。真实污染通过 memorization 表现——模型在 seen items 上的正确率系统性提升，而非随机翻转。这意味着：\n  - 真实污染产生的 DIF pattern 是单向的（只提升正确率），而 random flipping 是双向的\n  - 真实污染与 item difficulty 相关（易题 ceiling effect 限制了提升空间），而 uniform flipping 忽略了这一点\n  - Difficulty-dependent injection（Appendix B, Scheme D）部分解决了这个问题，但仍是 injection 而非 memorization\n- **论文在 Limitations 中承认了这一点**，但 Section 4.5 标题「Semi-Synthetic Framework Validation」暗示了比实际更强的验证。\n- **建议**：(a) 将 Section 4.5 定位为「detection power under a simplified injection model」而非 framework validation；(b) 讨论 monotonic injection（只允许 0→1 翻转）的结果是否不同；(c) 引用或讨论更现实的 contamination simulation 方法（如基于 n-gram overlap 的注入）。\n\n**W-E1 [Should-Fix] ETS C 分类阈值在 N=5,227 下的适用性未讨论**\n\n- **位置**：Section 3.2\n- **问题**：ETS C 分类要求 |Δ_MH| ≥ 1.5 **且** p < 0.05。论文正确指出在 N=5,227 下显著性几乎自动满足（Section 3.2: \"statistical significance (p < 0.05) is nearly automatically satisfied for any |Δ_MH| ≥ 1.5\"），这意味着分类实质上仅由效应量驱动。但 |Δ_MH| ≥ 1.5 这一阈值来自教育测量（通常 N 在数百到数千范围），在 N=5,227 的 LLM 场景下是否仍然合适？\n  - 较大的 N 意味着更精确的 Δ_MH 估计，从而更多 items 可能恰好越过阈值\n  - 论文虽然用了 DEFF 校正来调整 N，但 DEFF 校正的是 χ² 统计量而非效应量估计本身\n- **建议**：讨论 |Δ_MH| ≥ 1.5 在不同 N 下的含义是否一致，或考虑使用 bootstrapped 效应量 CI 是否包含 0 作为替代判据。\n\n**W-E2 [Should-Fix] Within-family 分析的 generalizability**\n\n- **位置**：Section 4.4 (倒数第二段), Table 2\n- **问题**：Within-family 分析主要依赖 Llama-2 vs Llama-3（N=161 vs N=308）和 Mistral 系列。但这两个 family 的代际变化特别大（Llama-2→3 涉及训练数据扩大 7 倍 + 架构改进）。用这样大跨度的代际变化来论证「DIF captures structured item-level change beyond ability differences」可能过度推断——在更小代际差异的 family 内（如 Llama-3 → Llama-3.1），DIF 信号是否仍然存在？\n- **建议**：如 METABENCH 中有更细粒度的代际变化（如 Llama-3 → Llama-3.1 → Llama-3.2），展示 within-family DIF 随代际距离的变化趋势。\n\n**W-S1 [Should-Fix] 关键统计量缺少不确定性度量**\n\n- **位置**：全文多处\n- **问题**：\n  - DEFF 估计（3.87 和 12.79）未报告 CI 或标准误——这些是关键的校正参数\n  - Appendix E Table 9 报告了 tier-stratified DEFF 但缺少 tier 之间的统计检验\n  - Jaccard = 0.206 报告了 permutation null 区间但未报告 bootstrap CI\n  - 机制分析（Appendix B）中的 logistic regression OR（如 OR = 1.73 for difficulty-model-type interaction）未报告 CI\n- **建议**：为 DEFF、Jaccard、以及 Appendix B 的 OR 添加 95% CI。\n\n**W-S2 [Minor] 多重比较处理的透明度**\n\n- **位置**：Section 4.2, Appendix A.2\n- **问题**：论文提到使用 BH correction（Section 4.2），但 Appendix A.2 的 random-split sanity check 使用了「α_rf = 0.05」且未提到多重比较校正。此外，Appendix B 的 logistic regression 报告了多个 p 值但未明确是否经过校正。应在一处统一说明多重比较策略。\n- **建议**：在 Method 或 Appendix 中添加一段统一说明所有 p 值的多重比较处理方式。\n\n**W-M4 [Minor] 「Measurement instability」概念的操作化定义不够明确**\n\n- **位置**：Title, Abstract, Section 5.1\n- **问题**：论文标题使用「temporal measurement instability」，但 Section 5.1 又说「DIF detects that items function differently across cohorts, not why」。在教育测量中，measurement invariance 有明确的操作化定义（如 IRT 参数跨组等价）。论文实际检测的是 MH-DIF（一种 observed-score 方法），但用了「measurement instability」这一更强的概念标签。MH-DIF 检测到的可能是 item-level functioning 差异而非真正的 measurement property 退化。\n- **建议**：在 Section 3 开头明确定义本文中「measurement instability」的操作化含义=「statistically significant and practically meaningful DIF as classified by ETS C criteria」。\n\n---\n\n### Questions for Authors\n\n**Q1**：在 matched-ability 控制中（Table 2, C% = 28.35%），如何确保 matching 的质量？Matching 是 exact matching 还是 propensity score matching？剩余的能力差异有多大？\n\n**Q2**：论文报告 Jaccard = 0.206 在 permutation null (0.203, 0.222] 内（Section 4.3），但 Table 1 的 Enrichment 列显示 temporal DIF 的 enrichment ratio = 1.0。如果 web-overlap items 中有部分确实受到污染并导致 DIF，这个信号是否被 73.8% 的非 web-overlap coverage 稀释了？\n\n**Q3**：DEFF 校正后 C% 从 31.3% 降至 29.2%（simple-mean）——降幅只有 2 个百分点。这是否说明 family structure 对 DIF 检测的实际影响很小？如果是这样，为什么 weighted-mean 给出的 13.5% 差异如此大？\n\n**Q4**：Appendix H 的 item-property predictive analysis 使用了 17 个 features 做 logistic regression/LightGBM，ROC = 0.603/0.039。这个接近 chance 的预测能力意味着 DIF 标记几乎不可预测——这是支持还是反对 DIF 作为 measurement quality indicator 的论点？\n\n**Q5**：Cross-benchmark validation（Table 3）显示不同 benchmark 的 temporal C% 差异较大（MMLU 31.3% vs HellaSwag 17.9%）。这种差异是否与 benchmark 的 item 特征（如 item format, difficulty distribution）系统性相关？\n\n---\n\n### Missing References\n\n1. **Camilli, G., & Shepard, L. A. (1994). Methods for Identifying Biased Test Items.** — 这是 DIF 领域的经典教科书，区分了 impact（合法能力差异）和 bias（测量偏差），对本文的解释框架直接相关。论文引用了 Holland & Thayer (1988) 等早期工作但遗漏了这一关键理论基础。\n\n2. **Penfield, R. D., & Camilli, G. (2007). Differential item functioning and item bias.** In Handbook of Statistics. — 系统综述 DIF 方法论，包括 MH 方法的局限性讨论。论文引了 Penfield and Camilli (2007) 于 page 3（作为 comprehensive review），但如果确实引用了则此条取消。\n\n3. **Wainer, H. (1993). Differential Testlet Functioning.** — 讨论了 testlet（item bundle）对 DIF 检测的影响，与本文的 family structure（model clusters）问题有类似的非独立性挑战。\n\n4. **Suk, Y., & Wiejon, Y. (2026). Rethinking differential item functioning from a causal inference perspective.** — 论文引用列表第 11 页显示已引用此文（\"Forthcoming\"），确认已包含。\n\n---\n\n### Overall Assessment\n\n**Overall**: **3.5 — Borderline Conference**\n\n**一句话总结**：方法论框架扎实、规模令人印象深刻，但时序混淆的不可解性和 DEFF 估计的宽范围削弱了核心 claim 的可解释性和实践价值。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | MH-DIF 应用正确，DEFF 校正和 cross-subject matching 设计精巧，但时序混淆未解决，DEFF 范围（13.5-29.2%）过宽 |\n| Excitement | 3.5/5 | 将心理测量学方法引入 LLM 评测的方向有价值，DIF-contamination 正交性发现 novel，但实践 actionability 受限 |\n| Reproducibility | 4/5 | 数据来自公开的 METABENCH，分析代码注释可用（footnote 1），方法描述详细 |\n| Reviewer Confidence | 4/5 | 熟悉 DIF 方法论和 LLM 评测文献，对 survey sampling（DEFF）的细节理解一般 |\n\n**评分依据**：论文在方法论上达到了 conference 水准（S1-S3 的系统性、S4 的正交性发现、S5 的跨 benchmark 复制），但 W-M1（时序混淆）是影响核心 claim 可解释性的根本问题。如果作者能更审慎地限定 claim（从 \"measurement instability\" 退到 \"temporal DIF\"），并更透明地处理 DEFF 估计范围（W-M2），论文可以达到 4 (Conference)。当前状态介于 Conference 和 Findings 之间。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿意见 — Round 1\n\n**论文**：Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n\n---\n\n### Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM 基准评测，在 METABENCH 数据集（5,227 模型 × 12,508 MMLU items）上发现约 27-29%（经非独立性校正后）的 items 在 2023 vs 2024 模型 cohort 间表现出显著的时序 DIF。论文进一步证明 DIF 标记与 web-overlap 污染标签在统计上正交（Jaccard ≈ 0.206，κ = 0.012），并通过 semi-synthetic 注入框架验证了 MH-DIF 的检测能力。论文将发现定位为「测量不稳定性」而非「污染检测」，提出 DIF 审计作为基准评测的心理测量学预筛工具。\n\n---\n\n### Strengths\n\n**S1. 规模与系统性**：5,227 模型 × 12,508 items 的全矩阵分析在 LLM 评测领域属罕见规模。五种 cohort 设计（temporal、ability-quintile、matched-ability、within-family、random split）构成了严谨的控制体系（Table 1, Table 2）。\n\n**S2. 非独立性校正框架扎实**：认识到 LLM model families 违反独立性假设并提出 DEFF 校正是重要的方法论贡献。同时提供 simple-mean DEFF 和 family-level cluster bootstrap 两个独立校正路径，且两者收敛于相近区间（26.7%-29.2%），增强了结果可信度（Section 4.2, Appendix E）。\n\n**S3. Cross-subject matching 的 FPR 保证**：Section 3.4 对单科目污染场景下 ΔFPR = 0 的构造性证明是精巧的——用不同 benchmark 的总分作为 matching variable 从根本上隔离了被测科目的污染信号。这一设计在 LLM 评测中具有独立价值。\n\n**S4. DIF 与 web-overlap 的正交性发现**：κ = 0.012、OR = 1.05、Jaccard 在 permutation null 区间内（Section 4.3），统计支撑充分。这一发现对理解 benchmark 质量问题的多维性具有概念性贡献——global exposure 和 differential functioning 确实捕捉了不同现象。\n\n**S5. 跨 benchmark 复制**：六个 METABENCH benchmark 均表现出时序 DIF（Table 3），增强了结论的普适性。GSM8K 的探索性分析（Section 4.7, Appendix F）恰当地标注为描述性分析。\n\n**S6. 下游影响分析有实践价值**：Figure 4 展示 DIF-ordered 移除对模型排名的影响（flip rate 33.6%），Table 2 的 matched-ability 控制（C% = 28.35%）排除了纯能力差异解释，这些分析将方法论发现与实际评测决策相连接。\n\n**S7. 机制分析（Appendix B）虽为探索性但有深度**：排除论证、difficulty-direction interaction、mixed-injection 分析展示了认真的因果推理尝试，即使最终未能完全区分机制。\n\n---\n\n### Weaknesses\n\n**W-M1 [Must-Fix] 时序混淆是论文最大的解释性缺口**\n\n- **位置**：Section 5.1, Section 3.3, Appendix B\n- **问题**：2023 vs 2024 model cohort 在架构（Transformer variants）、训练范式（SFT/RLHF/DPO 演进）、数据规模、能力水平上同时变化。论文将 DIF 定义为「items function differently across cohorts」（Section 5.1），但在 LLM 场景下，不同代模型对不同 item 类型展现不同能力 profile 是 **预期行为**——这与教育测量中同一课程体系下不同人群的 DIF（预期为零）有本质区别。\n- **具体地说**：Section 5.1 报告 base models 在难题上提升（ρ = −0.570）而 instruct models 在易题上提升（ρ near-zero gradient），但这可能完全反映了合法的训练方法论进步（如 RLHF 对易题的 ceiling effect 提升），而非测量的不稳定性。论文的 Appendix B 排除分析列出三种机制但承认无法区分。\n- **为什么影响接收**：核心 claim「27-29% of items exhibit temporal measurement instability」的可解释性取决于是否能将 legitimate capability evolution 与 genuine measurement dysfunction 区分开。如果无法区分，DIF rate 作为 benchmark 质量指标的实践价值存疑。\n- **建议**：(a) 明确讨论「在 LLM 场景下什么样的 DIF 是预期的、可接受的」——可以借鉴 Camilli and Shepard (1994) 对 impact vs bias 的区分；(b) 考虑引入 item-level covariates（如 item difficulty, discrimination, subject domain）作为 DIF 的解释变量，区分可解释的 DIF（由 item 特征预测）和残余 DIF；(c) 更审慎地限定 claim——将「measurement instability」改为「differential item functioning across model generations」，让读者自行判断这是否构成 instability。\n\n**W-M2 [Should-Fix] DEFF 估计范围过宽，首选估计的论证不够充分**\n\n- **位置**：Section 4.2, Appendix E\n- **问题**：Simple-mean DEFF（n̄ = 62.8）给出调整后 C% = 29.2%，weighted-mean DEFF（n̄ reflecting effective cluster size）给出 C% = 13.5%。两者相差 2 倍以上。论文以「within-family similarity is flat across family sizes (r_s = −0.03)」为由偏好 simple-mean，但这一论证存在逻辑缺口：\n  - r_s = −0.03 说明 ICC 不随 family size 变化，但这不意味着应该用 simple-mean。在 survey methodology 中，当 clusters 大小不等时，weighted-mean 更能反映随机抽取一个 unit 所经历的实际 design effect（Kish, 1965）。\n  - 更关键的是，论文的 50 个 families 中大 families（Llama-3 n=308, Mistral n=547 等）贡献了大部分 models。一个从 5,227 models 中随机抽取的 model 更可能来自大 family，因此 weighted-mean 可能更合适。\n- **为什么影响评分**：13.5% vs 29.2% 的差距直接影响读者对 benchmark 质量问题严重程度的判断。\n- **建议**：(a) 展示 DEFF 敏感性分析（如移除最大 2-3 个 families 后的变化）；(b) 在正文中并列呈现两个估计，而非将 13.5% 降级为 footnote-level 的「lower bound」；(c) 讨论在什么条件下各估计更合适。\n\n**W-M3 [Should-Fix] Semi-synthetic 注入模型的生态效度有限**\n\n- **位置**：Section 3.4, Section 4.5, Figure 2\n- **问题**：Binary response flipping（以 exploitation rate p 随机翻转正确答案为错误）是对真实污染的粗糙近似。真实污染通过 memorization 表现——模型在 seen items 上的正确率系统性提升，而非随机翻转。这意味着：\n  - 真实污染产生的 DIF pattern 是单向的（只提升正确率），而 random flipping 是双向的\n  - 真实污染与 item difficulty 相关（易题 ceiling effect 限制了提升空间），而 uniform flipping 忽略了这一点\n  - Difficulty-dependent injection（Appendix B, Scheme D）部分解决了这个问题，但仍是 injection 而非 memorization\n- **论文在 Limitations 中承认了这一点**，但 Section 4.5 标题「Semi-Synthetic Framework Validation」暗示了比实际更强的验证。\n- **建议**：(a) 将 Section 4.5 定位为「detection power under a simplified injection model」而非 framework validation；(b) 讨论 monotonic injection（只允许 0→1 翻转）的结果是否不同；(c) 引用或讨论更现实的 contamination simulation 方法（如基于 n-gram overlap 的注入）。\n\n**W-E1 [Should-Fix] ETS C 分类阈值在 N=5,227 下的适用性未讨论**\n\n- **位置**：Section 3.2\n- **问题**：ETS C 分类要求 |Δ_MH| ≥ 1.5 **且** p < 0.05。论文正确指出在 N=5,227 下显著性几乎自动满足（Section 3.2: \"statistical significance (p < 0.05) is nearly automatically satisfied for any |Δ_MH| ≥ 1.5\"），这意味着分类实质上仅由效应量驱动。但 |Δ_MH| ≥ 1.5 这一阈值来自教育测量（通常 N 在数百到数千范围），在 N=5,227 的 LLM 场景下是否仍然合适？\n  - 较大的 N 意味着更精确的 Δ_MH 估计，从而更多 items 可能恰好越过阈值\n  - 论文虽然用了 DEFF 校正来调整 N，但 DEFF 校正的是 χ² 统计量而非效应量估计本身\n- **建议**：讨论 |Δ_MH| ≥ 1.5 在不同 N 下的含义是否一致，或考虑使用 bootstrapped 效应量 CI 是否包含 0 作为替代判据。\n\n**W-E2 [Should-Fix] Within-family 分析的 generalizability**\n\n- **位置**：Section 4.4 (倒数第二段), Table 2\n- **问题**：Within-family 分析主要依赖 Llama-2 vs Llama-3（N=161 vs N=308）和 Mistral 系列。但这两个 family 的代际变化特别大（Llama-2→3 涉及训练数据扩大 7 倍 + 架构改进）。用这样大跨度的代际变化来论证「DIF captures structured item-level change beyond ability differences」可能过度推断——在更小代际差异的 family 内（如 Llama-3 → Llama-3.1），DIF 信号是否仍然存在？\n- **建议**：如 METABENCH 中有更细粒度的代际变化（如 Llama-3 → Llama-3.1 → Llama-3.2），展示 within-family DIF 随代际距离的变化趋势。\n\n**W-S1 [Should-Fix] 关键统计量缺少不确定性度量**\n\n- **位置**：全文多处\n- **问题**：\n  - DEFF 估计（3.87 和 12.79）未报告 CI 或标准误——这些是关键的校正参数\n  - Appendix E Table 9 报告了 tier-stratified DEFF 但缺少 tier 之间的统计检验\n  - Jaccard = 0.206 报告了 permutation null 区间但未报告 bootstrap CI\n  - 机制分析（Appendix B）中的 logistic regression OR（如 OR = 1.73 for difficulty-model-type interaction）未报告 CI\n- **建议**：为 DEFF、Jaccard、以及 Appendix B 的 OR 添加 95% CI。\n\n**W-S2 [Minor] 多重比较处理的透明度**\n\n- **位置**：Section 4.2, Appendix A.2\n- **问题**：论文提到使用 BH correction（Section 4.2），但 Appendix A.2 的 random-split sanity check 使用了「α_rf = 0.05」且未提到多重比较校正。此外，Appendix B 的 logistic regression 报告了多个 p 值但未明确是否经过校正。应在一处统一说明多重比较策略。\n- **建议**：在 Method 或 Appendix 中添加一段统一说明所有 p 值的多重比较处理方式。\n\n**W-M4 [Minor] 「Measurement instability」概念的操作化定义不够明确**\n\n- **位置**：Title, Abstract, Section 5.1\n- **问题**：论文标题使用「temporal measurement instability」，但 Section 5.1 又说「DIF detects that items function differently across cohorts, not why」。在教育测量中，measurement invariance 有明确的操作化定义（如 IRT 参数跨组等价）。论文实际检测的是 MH-DIF（一种 observed-score 方法），但用了「measurement instability」这一更强的概念标签。MH-DIF 检测到的可能是 item-level functioning 差异而非真正的 measurement property 退化。\n- **建议**：在 Section 3 开头明确定义本文中「measurement instability」的操作化含义=「statistically significant and practically meaningful DIF as classified by ETS C criteria」。\n\n---\n\n### Questions for Authors\n\n**Q1**：在 matched-ability 控制中（Table 2, C% = 28.35%），如何确保 matching 的质量？Matching 是 exact matching 还是 propensity score matching？剩余的能力差异有多大？\n\n**Q2**：论文报告 Jaccard = 0.206 在 permutation null (0.203, 0.222] 内（Section 4.3），但 Table 1 的 Enrichment 列显示 temporal DIF 的 enrichment ratio = 1.0。如果 web-overlap items 中有部分确实受到污染并导致 DIF，这个信号是否被 73.8% 的非 web-overlap coverage 稀释了？\n\n**Q3**：DEFF 校正后 C% 从 31.3% 降至 29.2%（simple-mean）——降幅只有 2 个百分点。这是否说明 family structure 对 DIF 检测的实际影响很小？如果是这样，为什么 weighted-mean 给出的 13.5% 差异如此大？\n\n**Q4**：Appendix H 的 item-property predictive analysis 使用了 17 个 features 做 logistic regression/LightGBM，ROC = 0.603/0.039。这个接近 chance 的预测能力意味着 DIF 标记几乎不可预测——这是支持还是反对 DIF 作为 measurement quality indicator 的论点？\n\n**Q5**：Cross-benchmark validation（Table 3）显示不同 benchmark 的 temporal C% 差异较大（MMLU 31.3% vs HellaSwag 17.9%）。这种差异是否与 benchmark 的 item 特征（如 item format, difficulty distribution）系统性相关？\n\n---\n\n### Missing References\n\n1. **Camilli, G., & Shepard, L. A. (1994). Methods for Identifying Biased Test Items.** — 这是 DIF 领域的经典教科书，区分了 impact（合法能力差异）和 bias（测量偏差），对本文的解释框架直接相关。论文引用了 Holland & Thayer (1988) 等早期工作但遗漏了这一关键理论基础。\n\n2. **Penfield, R. D., & Camilli, G. (2007). Differential item functioning and item bias.** In Handbook of Statistics. — 系统综述 DIF 方法论，包括 MH 方法的局限性讨论。论文引了 Penfield and Camilli (2007) 于 page 3（作为 comprehensive review），但如果确实引用了则此条取消。\n\n3. **Wainer, H. (1993). Differential Testlet Functioning.** — 讨论了 testlet（item bundle）对 DIF 检测的影响，与本文的 family structure（model clusters）问题有类似的非独立性挑战。\n\n4. **Suk, Y., & Wiejon, Y. (2026). Rethinking differential item functioning from a causal inference perspective.** — 论文引用列表第 11 页显示已引用此文（\"Forthcoming\"），确认已包含。\n\n---\n\n### Overall Assessment\n\n**Overall**: **3.5 — Borderline Conference**\n\n**一句话总结**：方法论框架扎实、规模令人印象深刻，但时序混淆的不可解性和 DEFF 估计的宽范围削弱了核心 claim 的可解释性和实践价值。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | MH-DIF 应用正确，DEFF 校正和 cross-subject matching 设计精巧，但时序混淆未解决，DEFF 范围（13.5-29.2%）过宽 |\n| Excitement | 3.5/5 | 将心理测量学方法引入 LLM 评测的方向有价值，DIF-contamination 正交性发现 novel，但实践 actionability 受限 |\n| Reproducibility | 4/5 | 数据来自公开的 METABENCH，分析代码注释可用（footnote 1），方法描述详细 |\n| Reviewer Confidence | 4/5 | 熟悉 DIF 方法论和 LLM 评测文献，对 survey sampling（DEFF）的细节理解一般 |\n\n**评分依据**：论文在方法论上达到了 conference 水准（S1-S3 的系统性、S4 的正交性发现、S5 的跨 benchmark 复制），但 W-M1（时序混淆）是影响核心 claim 可解释性的根本问题。如果作者能更审慎地限定 claim（从 \"measurement instability\" 退到 \"temporal DIF\"），并更透明地处理 DEFF 估计范围（W-M2），论文可以达到 4 (Conference)。当前状态介于 Conference 和 Findings 之间。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1085 · 2026-05-23T08:02:55.358850+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Assistant

_source line 1086 · 2026-05-23T08:03:05.591072+00:00_

审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference）。

核心判断：
- **方法论框架扎实**——MH-DIF 应用正确，DEFF 校正和 cross-subject matching 是有独立价值的贡献
- **最大问题是时序混淆（W-M1）**——2023→2024 cohort 变化太多（架构/训练/数据/能力），无法区分 legitimate capability evolution 和 genuine measurement instability
- **DEFF 估计范围过宽（W-M2）**——simple-mean 给出 29.2%、weighted-mean 给出 13.5%，2 倍差距下论文偏好高估值的论证不充分
- **Semi-synthetic 注入模型生态效度有限（W-M3）**——random flipping ≠ memorization-based contamination

提出了 5 个需要作者澄清的问题和 3 条潜在遗漏引用。如果作者能审慎限定 claim 并更透明处理 DEFF 范围，论文可达 Conference (4.0)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 37

## Round 37

8 recorded events


### User

_source line 1087 · 2026-05-23T08:05:45.299735+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的意见。对每一条：
- **[AGREE]**：同意并说明理由
- **[REBUT]**：反驳并引用具体的 Section/Table/Figure 作为证据

特别关注与你自己审稿意见的差异和重叠。

---

以下是 Reviewer 2 的完整审稿原文：

### Strengths
S1: 分析规模和严谨性令人印象深刻。5,227 个模型 × 12,508 题目是目前已知最大规模的 DIF 分析。鲁棒性检验极其全面。
S2: Global exposure vs. differential functioning 二维框架有实际价值。正交性的实证证据充分且可信。
S3: 半合成验证框架设计良好。Cross-subject matching 保证 ΔFPR = 0 的理论分析简洁优雅。
S4: 六个基准的跨基准复现增强了可信度。
S5: base-vs-instruct 反转是论文最有洞察力的发现（χ² = 562.7）。
S6: 诚实展示局限性。

### Must-Fix 问题

**W-F1 [critical]: "Temporal measurement instability" 的 framing 存在根本性张力**
论文将 DIF 定义为 "temporal measurement instability"，但 "instability" 暗示基准测试存在缺陷。然而论文同时展示了：(a) 聚合排名几乎不受影响（ρ ≈ 0.997）；(b) DIF-flagged 题目集中了最高区分度信号；(c) DIF 可能反映真实能力演化。如果 DIF 反映的是真实 capability evolution，那么所谓 "instability" 恰恰是基准测试正常工作的表现。建议将 "instability" 替换为更中性术语，或更强力论证为什么即使来源于 capability evolution 它仍构成 "instability"。

**W-F2 [critical]: DIF 无法区分 contamination / capability evolution / composition shift——实践含义讨论不够充分**
论文承认 DIF "detects what, not why" 但直接跳到规范性建议 "benchmarks need psychometric monitoring"。这个跳跃缺乏逻辑支撑：若是 contamination 应移除 flagged 题目；若是 capability evolution，移除它们会损害基准质量；若是 composition shift，问题在 cohort 定义。Section 5.2 的 audit protocol 没有讨论在不同机制假设下行动后果截然不同。建议按不同机制场景分别讨论行动含义。

**W-C1 [critical]: \enlargethispage 使用过于激进，可能实质性违反 8 页限制**
experiments.tex 的 `\enlargethispage*{4\baselineskip}` + discussion.tex 的 `\enlargethispage*{6\baselineskip}` 共增加约 10 行空间。6\baselineskip 极为激进，page 8 异常密集。还有 15 处 `\looseness=-1/-2`。建议控制 \enlargethispage 在 ≤2\baselineskip 以内。

### Should-Fix 问题

**W-N1 [warning]: 核心方法是 1988 年的标准 MH-DIF，方法论新颖性有限**
贡献定位为 "methodological and empirical" 但实际上是 "application of existing methodology to a new domain"。

**W-N2 [warning]: "两个维度" 框架的新颖性被高估——正交性可能是预期结果而非发现**
Web-overlap 标签（global, 与模型无关）和 DIF（differential, 与模型相关）概念上就测量不同的东西，因此正交性是概念上预期的。

**W-F3 [warning]: 缺少 base-vs-instruct composition shift 的直接控制**
2023 和 2024 cohort 中 base/instruct 比例可能不同。论文做了 ability matching 但没做 model-type-stratified temporal DIF。建议补充。

**W-W1 [warning]: 术语不一致**
"measurement instability", "temporal DIF", "temporal comparability" 等术语交替使用。

**W-W2 [warning]: Conclusion 过于简短**
仅 4 句话，未讨论 practical implications 和 future directions。

**W-W3 [warning]: Abstract 信息密度过高**
数字堆叠，非 psychometrics 读者难以消化。

### Questions
Q1: 2023/2024 cohort 中 base/instruct 比例？是否做过 model-type-stratified temporal DIF？
Q2: Section 5.1 的 base N=1,409、instruct N=478 与 temporal cohort N=1,887 的关系？
Q3: Maeda (2025) 是否属于将 DIF 应用于 LLM 评估的先例？
Q4: Growing Pains anchor items 与本文 stable items 的重叠度？
Q5: DIF audit 后具体应采取什么行动？不同机制下后果如何？

### Missing References
1. Population composition 在 DIF 分析中的影响文献
2. LLM evaluation 中 fairness-oriented DIF 工作
3. Suk and Weiss (2026) 值得更详细讨论

### Overall: 3.5 — Borderline Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1088 · 2026-05-23T08:06:11.509369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1089 · 2026-05-23T08:06:12.112265+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1090 · 2026-05-23T08:06:12.266437+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool result

_source line 1091 · 2026-05-23T08:06:12.973060+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-23T08:07:49.520263+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 交叉回应 — 针对 Reviewer 2 的审稿意见\n\n---\n\n### Strengths 部分\n\n对 R2 的 S1-S6 无异议，与我自己的评估一致。\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-W-F1: \"Temporal measurement instability\" framing 的根本性张力**\n\n强烈同意。这与我的 W-M1 高度重叠，且 R2 的论证角度更尖锐：论文自身提供的证据（ρ ≈ 0.997 的聚合排名稳定性 + DIF items 集中最高区分度信号）实际上在反驳 \"instability\" 的负面含义。我的 W-M1 从时序混淆角度切入，R2 从论文内部证据矛盾切入——两条独立路径指向同一结论：「measurement instability」这一 framing 缺乏充分论证。\n\n补充一点 R2 未提到的：Section 5.1 的 base-vs-instruct difficulty gradient reversal（χ² = 562.7, p < 10⁻¹²⁴）本身就是一个极有价值的发现，但论文将其归类在 \"instability\" 叙事下反而削弱了它的意义。如果改为 \"structured differential functioning reflecting training paradigm evolution\"，同一发现会有更清晰的理论定位。\n\n**[AGREE] R2-W-F2: DIF 无法区分机制——实践含义讨论不足**\n\n同意核心论点。R2 指出 Section 5.2 的 audit protocol 在不同机制假设下行动后果截然不同——这一批评精准。具体而言，Section 5.2 建议 \"MH-DIF audits when ever ≥500 models accumulate\"（page 8），但若 DIF 反映的是 legitimate capability evolution，这种审计会系统性地标记高质量题目为 \"不稳定\"，反而损害 benchmark 质量。\n\n不过我要补充一个 nuance：论文在 Section 4.6 展示了 DIF-ordered removal 导致 33.6% 的排名反转（page 8, Figure 4），这至少说明 DIF 信号对实践决策有影响，不论底层机制如何。问题不在于 DIF 是否有信号，而在于论文直接从 \"有信号\" 跳到 \"需要监控\" 而未讨论 \"信号意味着什么\"。\n\n**[REBUT] R2-W-C1: \\enlargethispage 使用可能违反页数限制**\n\n不完全同意将此列为 critical。从 PDF 渲染结果看：\n- 主文（§1-§6 Conclusion）终止于第 8 页底部\n- Limitations 从第 9 页开始\n- EMNLP 2026 规则明确 Limitations 不计入 8 页限制\n\nPage 8 确实比其他页面更密集，但就我在 PDF 中所见，正文内容在视觉上仍在第 8 页之内。`\\enlargethispage` 和 `\\looseness` 是 LaTeX 排版的常见技巧，绝大多数顶会投稿都使用——只要最终渲染结果不超过页数限制即可。除非 PC 明确禁止这些命令（ARR CFP 和 reviewer guidelines 中我未找到此类禁令），我认为这属于 **Should-Fix** 而非 **Critical**。\n\n但我同意 R2 的观察：page 8 的信息密度异常高——Discussion + Conclusion 压缩在不到一页内，这影响了可读性。建议作者考虑精简 Section 4 中的冗余内容以给 Discussion 留出空间，而不是通过排版技巧挤压。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W-N1: 核心方法是 1988 年的标准 MH-DIF，方法论新颖性有限**\n\n部分不同意。MH-DIF 本身确实是 1988 年的方法，但论文的方法论贡献不在 MH 本身，而在三个适配：\n1. **DEFF 非独立性校正**（Section 4.2, Appendix E）——将 survey sampling 的 design effect 概念引入 LLM DIF 分析，处理 model family 结构，这在 DIF 文献中不常见\n2. **Cross-subject matching 的 FPR 保证**（Section 3.4）——利用多科目结构实现理论上的零 FPR，这是对 MH 方法在多维 benchmark 场景下的非平凡扩展\n3. **Semi-synthetic validation pipeline**（Section 3.4, 4.5）——将 dose-response 验证框架与 DIF 结合\n\n将论文定位为 \"application of existing methodology\" 过于苛刻。更准确的说法是 \"methodological adaptation with domain-specific innovations\"。当然，论文确实应该在 Introduction 中更明确地区分「采用已有方法」和「本文的方法论贡献」。\n\n**[AGREE] R2-W-N2: 正交性可能是概念上预期的结果**\n\n同意这一观察。Web-overlap（static, model-agnostic）和 DIF（dynamic, model-dependent）在概念上就测量不同维度，因此低 Jaccard 是预期而非惊喜。但我认为这并不完全削弱其贡献价值——概念预期和实证确认之间有差距。许多\"概念上预期\"的结果在实证中被推翻（如 benchmark contamination detection methods 之间的低一致性，见 Balloccu et al., 2024）。论文的实证确认（κ = 0.012, OR = 1.05, permutation test p = 0.88）将直觉上的预期转化为有统计支撑的事实，仍有增量贡献。\n\n建议作者在论文中 acknowledge 这一预期性，将贡献定位从 \"surprising discovery\" 调整为 \"empirical confirmation of a theoretically expected but previously unverified distinction\"。\n\n**[AGREE] R2-W-F3: 缺少 base-vs-instruct composition shift 的直接控制**\n\n同意，这是我审稿中遗漏的一个重要控制。2023→2024 cohort 中 base/instruct 比例变化可能是 DIF 信号的混淆源。论文做了 matched-ability 控制（Table 2, C% = 28.35%）但 ability matching 不等同于 model-type matching。\n\n具体而言：如果 2024 cohort 中 instruct models 比例显著高于 2023，而 instruct models 在易题上系统性表现不同（Section 5.1 已证明），那么观察到的 temporal DIF 可能部分归因于 cohort composition shift 而非 item-level measurement change。\n\n这个控制应该很容易补充：对 base models 和 instruct models 分别做 temporal DIF 分析，比较两个 subgroup 的 C% 是否一致。\n\n**[AGREE] R2-W-W1: 术语不一致**\n\n同意。这与我的 W-M4 重叠。\"measurement instability\"、\"temporal DIF\"、\"temporal comparability\"、\"differential functioning\" 在论文中交替使用但含义不完全相同。建议统一术语体系。\n\n**[AGREE] R2-W-W2: Conclusion 过于简短**\n\n同意。从 PDF page 8 可见，Section 6 Conclusion 仅约 4 句话，未讨论 practical implications、limitations of the audit protocol、或 future directions。这与论文的规模和深度不匹配。这可能正是 W-C1 所提排版挤压的后果——Discussion 和 Conclusion 被压缩以适应页数限制。\n\n**[AGREE] R2-W-W3: Abstract 信息密度过高**\n\n同意。Abstract 包含至少 8 个具体数字（5,227; 27,125; 31.3%; 27-29%; 0.206; 13.5%; 0.997; 562.7），对非 psychometrics 背景读者确实难以消化。建议减少数字、增加 narrative clarity。\n\n---\n\n### Questions 部分\n\n**R2-Q1 (base/instruct 比例 + model-type-stratified DIF)**：支持这一问题。与 W-F3 直接相关，是关键缺失控制。\n\n**R2-Q2 (Section 5.1 的 N 与 temporal cohort N 的关系)**：合理的技术性澄清问题。\n\n**R2-Q3 (Maeda 2025 是否为先例)**：有价值的先例确认问题。论文引用了 Maeda (2025) 但未详细讨论其方法和发现——如果 Maeda 已经将 DIF 应用于 LLM 评估，论文应明确说明与 Maeda 的差异（规模、方法适配、发现）。\n\n**R2-Q4 (Growing Pains anchor items 与 stable items 重叠度)**：有趣但非关键。Growing Pains (Habba et al., 2026) 使用 IRT calibration 识别 anchor items，本文使用 DIF 识别 unstable items——两种方法的 complementarity 值得讨论但不影响接收决定。\n\n**R2-Q5 (DIF audit 后的具体行动)**：与 W-F2 直接相关，是核心问题。\n\n---\n\n### Missing References 部分\n\nR2 指出的三类文献（population composition 对 DIF 的影响、LLM fairness-oriented DIF、Suk and Weiss 2026 详细讨论）均有道理，但均不构成关键遗漏。其中 Suk and Weiss (2026) 论文已引用（References page 11），只是讨论不够深入。\n\n---\n\n### 总结：R1 与 R2 的共识与分歧\n\n**核心共识**（两位 reviewer 独立得出）：\n1. **Framing 问题**：「measurement instability」的 claim 缺乏充分论证，temporal confound 未解决（R1-W-M1 ≈ R2-W-F1 ≈ R2-W-F2）\n2. **规模和方法论系统性是主要优势**\n3. **DIF-contamination 正交性有贡献但可能被高估**\n4. **Overall 3.5, Borderline Conference**\n\n**主要分歧**：\n1. **\\enlargethispage 严重性**：R2 列为 critical，R1 认为是 should-fix（排版技巧 vs 页数违规的界限）\n2. **方法论新颖性**：R2 认为有限（W-N1），R1 认为 DEFF/cross-subject matching/semi-synthetic 三个适配具有独立贡献\n3. **DEFF 估计范围**：R1 将此列为独立的 should-fix 问题（W-M2），R2 未专门讨论\n\n**建议 AC**：核心问题集中在 framing 和 interpretability——如果作者能在 revision 中 (a) 退回到更中性的 claim、(b) 补充 model-type-stratified 控制、(c) 分机制讨论 practical implications，论文可以达到 Conference 水平。当前版本 3.5 是合理评分。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 交叉回应 — 针对 Reviewer 2 的审稿意见\n\n---\n\n### Strengths 部分\n\n对 R2 的 S1-S6 无异议，与我自己的评估一致。\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-W-F1: \"Temporal measurement instability\" framing 的根本性张力**\n\n强烈同意。这与我的 W-M1 高度重叠，且 R2 的论证角度更尖锐：论文自身提供的证据（ρ ≈ 0.997 的聚合排名稳定性 + DIF items 集中最高区分度信号）实际上在反驳 \"instability\" 的负面含义。我的 W-M1 从时序混淆角度切入，R2 从论文内部证据矛盾切入——两条独立路径指向同一结论：「measurement instability」这一 framing 缺乏充分论证。\n\n补充一点 R2 未提到的：Section 5.1 的 base-vs-instruct difficulty gradient reversal（χ² = 562.7, p < 10⁻¹²⁴）本身就是一个极有价值的发现，但论文将其归类在 \"instability\" 叙事下反而削弱了它的意义。如果改为 \"structured differential functioning reflecting training paradigm evolution\"，同一发现会有更清晰的理论定位。\n\n**[AGREE] R2-W-F2: DIF 无法区分机制——实践含义讨论不足**\n\n同意核心论点。R2 指出 Section 5.2 的 audit protocol 在不同机制假设下行动后果截然不同——这一批评精准。具体而言，Section 5.2 建议 \"MH-DIF audits when ever ≥500 models accumulate\"（page 8），但若 DIF 反映的是 legitimate capability evolution，这种审计会系统性地标记高质量题目为 \"不稳定\"，反而损害 benchmark 质量。\n\n不过我要补充一个 nuance：论文在 Section 4.6 展示了 DIF-ordered removal 导致 33.6% 的排名反转（page 8, Figure 4），这至少说明 DIF 信号对实践决策有影响，不论底层机制如何。问题不在于 DIF 是否有信号，而在于论文直接从 \"有信号\" 跳到 \"需要监控\" 而未讨论 \"信号意味着什么\"。\n\n**[REBUT] R2-W-C1: \\enlargethispage 使用可能违反页数限制**\n\n不完全同意将此列为 critical。从 PDF 渲染结果看：\n- 主文（§1-§6 Conclusion）终止于第 8 页底部\n- Limitations 从第 9 页开始\n- EMNLP 2026 规则明确 Limitations 不计入 8 页限制\n\nPage 8 确实比其他页面更密集，但就我在 PDF 中所见，正文内容在视觉上仍在第 8 页之内。`\\enlargethispage` 和 `\\looseness` 是 LaTeX 排版的常见技巧，绝大多数顶会投稿都使用——只要最终渲染结果不超过页数限制即可。除非 PC 明确禁止这些命令（ARR CFP 和 reviewer guidelines 中我未找到此类禁令），我认为这属于 **Should-Fix** 而非 **Critical**。\n\n但我同意 R2 的观察：page 8 的信息密度异常高——Discussion + Conclusion 压缩在不到一页内，这影响了可读性。建议作者考虑精简 Section 4 中的冗余内容以给 Discussion 留出空间，而不是通过排版技巧挤压。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W-N1: 核心方法是 1988 年的标准 MH-DIF，方法论新颖性有限**\n\n部分不同意。MH-DIF 本身确实是 1988 年的方法，但论文的方法论贡献不在 MH 本身，而在三个适配：\n1. **DEFF 非独立性校正**（Section 4.2, Appendix E）——将 survey sampling 的 design effect 概念引入 LLM DIF 分析，处理 model family 结构，这在 DIF 文献中不常见\n2. **Cross-subject matching 的 FPR 保证**（Section 3.4）——利用多科目结构实现理论上的零 FPR，这是对 MH 方法在多维 benchmark 场景下的非平凡扩展\n3. **Semi-synthetic validation pipeline**（Section 3.4, 4.5）——将 dose-response 验证框架与 DIF 结合\n\n将论文定位为 \"application of existing methodology\" 过于苛刻。更准确的说法是 \"methodological adaptation with domain-specific innovations\"。当然，论文确实应该在 Introduction 中更明确地区分「采用已有方法」和「本文的方法论贡献」。\n\n**[AGREE] R2-W-N2: 正交性可能是概念上预期的结果**\n\n同意这一观察。Web-overlap（static, model-agnostic）和 DIF（dynamic, model-dependent）在概念上就测量不同维度，因此低 Jaccard 是预期而非惊喜。但我认为这并不完全削弱其贡献价值——概念预期和实证确认之间有差距。许多\"概念上预期\"的结果在实证中被推翻（如 benchmark contamination detection methods 之间的低一致性，见 Balloccu et al., 2024）。论文的实证确认（κ = 0.012, OR = 1.05, permutation test p = 0.88）将直觉上的预期转化为有统计支撑的事实，仍有增量贡献。\n\n建议作者在论文中 acknowledge 这一预期性，将贡献定位从 \"surprising discovery\" 调整为 \"empirical confirmation of a theoretically expected but previously unverified distinction\"。\n\n**[AGREE] R2-W-F3: 缺少 base-vs-instruct composition shift 的直接控制**\n\n同意，这是我审稿中遗漏的一个重要控制。2023→2024 cohort 中 base/instruct 比例变化可能是 DIF 信号的混淆源。论文做了 matched-ability 控制（Table 2, C% = 28.35%）但 ability matching 不等同于 model-type matching。\n\n具体而言：如果 2024 cohort 中 instruct models 比例显著高于 2023，而 instruct models 在易题上系统性表现不同（Section 5.1 已证明），那么观察到的 temporal DIF 可能部分归因于 cohort composition shift 而非 item-level measurement change。\n\n这个控制应该很容易补充：对 base models 和 instruct models 分别做 temporal DIF 分析，比较两个 subgroup 的 C% 是否一致。\n\n**[AGREE] R2-W-W1: 术语不一致**\n\n同意。这与我的 W-M4 重叠。\"measurement instability\"、\"temporal DIF\"、\"temporal comparability\"、\"differential functioning\" 在论文中交替使用但含义不完全相同。建议统一术语体系。\n\n**[AGREE] R2-W-W2: Conclusion 过于简短**\n\n同意。从 PDF page 8 可见，Section 6 Conclusion 仅约 4 句话，未讨论 practical implications、limitations of the audit protocol、或 future directions。这与论文的规模和深度不匹配。这可能正是 W-C1 所提排版挤压的后果——Discussion 和 Conclusion 被压缩以适应页数限制。\n\n**[AGREE] R2-W-W3: Abstract 信息密度过高**\n\n同意。Abstract 包含至少 8 个具体数字（5,227; 27,125; 31.3%; 27-29%; 0.206; 13.5%; 0.997; 562.7），对非 psychometrics 背景读者确实难以消化。建议减少数字、增加 narrative clarity。\n\n---\n\n### Questions 部分\n\n**R2-Q1 (base/instruct 比例 + model-type-stratified DIF)**：支持这一问题。与 W-F3 直接相关，是关键缺失控制。\n\n**R2-Q2 (Section 5.1 的 N 与 temporal cohort N 的关系)**：合理的技术性澄清问题。\n\n**R2-Q3 (Maeda 2025 是否为先例)**：有价值的先例确认问题。论文引用了 Maeda (2025) 但未详细讨论其方法和发现——如果 Maeda 已经将 DIF 应用于 LLM 评估，论文应明确说明与 Maeda 的差异（规模、方法适配、发现）。\n\n**R2-Q4 (Growing Pains anchor items 与 stable items 重叠度)**：有趣但非关键。Growing Pains (Habba et al., 2026) 使用 IRT calibration 识别 anchor items，本文使用 DIF 识别 unstable items——两种方法的 complementarity 值得讨论但不影响接收决定。\n\n**R2-Q5 (DIF audit 后的具体行动)**：与 W-F2 直接相关，是核心问题。\n\n---\n\n### Missing References 部分\n\nR2 指出的三类文献（population composition 对 DIF 的影响、LLM fairness-oriented DIF、Suk and Weiss 2026 详细讨论）均有道理，但均不构成关键遗漏。其中 Suk and Weiss (2026) 论文已引用（References page 11），只是讨论不够深入。\n\n---\n\n### 总结：R1 与 R2 的共识与分歧\n\n**核心共识**（两位 reviewer 独立得出）：\n1. **Framing 问题**：「measurement instability」的 claim 缺乏充分论证，temporal confound 未解决（R1-W-M1 ≈ R2-W-F1 ≈ R2-W-F2）\n2. **规模和方法论系统性是主要优势**\n3. **DIF-contamination 正交性有贡献但可能被高估**\n4. **Overall 3.5, Borderline Conference**\n\n**主要分歧**：\n1. **\\enlargethispage 严重性**：R2 列为 critical，R1 认为是 should-fix（排版技巧 vs 页数违规的界限）\n2. **方法论新颖性**：R2 认为有限（W-N1），R1 认为 DEFF/cross-subject matching/semi-synthetic 三个适配具有独立贡献\n3. **DEFF 估计范围**：R1 将此列为独立的 should-fix 问题（W-M2），R2 未专门讨论\n\n**建议 AC**：核心问题集中在 framing 和 interpretability——如果作者能在 revision 中 (a) 退回到更中性的 claim、(b) 补充 model-type-stratified 控制、(c) 分机制讨论 practical implications，论文可以达到 Conference 水平。当前版本 3.5 是合理评分。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1093 · 2026-05-23T08:07:53.335678+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Assistant

_source line 1094 · 2026-05-23T08:08:02.357175+00:00_

交叉回应已提交。主要结论：

- 与 R2 在核心问题上高度一致（framing 张力、temporal confound、术语不一致），独立得出相同的 3.5 评分
- 对 R2 的 3 个 critical 中 2 个表示同意（W-F1、W-F2），对 \enlargethispage 问题（W-C1）降级为 should-fix
- 反驳了 R2 对方法论新颖性的低估——DEFF 校正、cross-subject matching、semi-synthetic validation 是非平凡适配
- 补充支持了 R2 提出的 base/instruct composition shift 控制缺失（W-F3），这是我原始审稿遗漏的

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 1095 · 2026-05-23T08:08:03.583874+00:00_

[Round 1 审稿请求]:
提醒：请提交你对 Reviewer 2 审稿意见的交叉回应（[AGREE]/[REBUT]）。如果你已经完成分析，请直接输出交叉回应结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1096 · 2026-05-23T08:08:10.588233+00:00_

已在上一轮提交。交叉回应已通过 `review_reviewer_post_to_director` 发送给 Director，包含对 R2 全部意见的逐条 [AGREE]/[REBUT] 回应及 R1-R2 共识与分歧总结。无需重复提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 39

## Round 39

62 recorded events


### User

_source line 1097 · 2026-05-23T09:10:50.544610+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 方向的审稿。

## Venue 信息
- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)
- **类型**: Long paper
- **页数限制**: 8 页正文 + 无限参考文献；Limitations section 不计入页数
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind
- **附录**: 允许，不计入页数，审稿人可选择性阅读

## 论文信息
- **标题**: "Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"
- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`
- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/submitted.pdf`

## 你的审查侧重

请重点审查以下方面：

### 1. MH-DIF 方法论的适用性
- Mantel-Haenszel DIF 从 educational testing 迁移到 LLM benchmark 的合理性
- LLM 作为 "examinees" 是否满足 MH-DIF 的基本假设（local independence, unidimensionality）
- K=5 quintile stratification 的选择是否合理
- 论文如何处理 LLM-specific 的违反假设情况（model family non-independence, bimodal distributions）

### 2. Semi-synthetic 验证框架
- Uniform binary response flipping 作为注入策略的局限性——是否高估了检测能力
- ΔFPR=0 的 "constructive guarantee" 是否过度声称
- Cross-subject matching 的有效性和边界条件（multi-subject contamination 的退化）
- 是否有其他更现实的注入模型应该被考虑

### 3. 统计控制和 robustness
- DEFF 校正的两种估计（simple-mean vs weighted-mean）差异巨大（29.2% vs 13.5%），论文如何 justify 选择
- Family-level cluster bootstrap 95% CI [26.7%, 53.2%] 极宽，说明什么
- 多重比较校正（BH-FDR 仅移除 3/3918 items）——是否因 N=5227 导致 p-value inflation
- Graduated de-duplication 实验的解读是否合理
- LOFO 分析显示 Mistral/Llama-3 移除后 C% 显著下降——论文对此的解释是否充分

### 4. 实验设计
- 5 个 cohort designs 的选择和覆盖是否充分
- Cross-benchmark validation (6 benchmarks) 的说服力
- GSM1K correlation (r=-0.478, N=33) 的 exploratory 分析是否 overinterpreted
- Downstream impact 分析（ρ≈0.997 但个别模型 ±800 rank displacement）的实际意义
- Within-family DIF (Llama-2 vs Llama-3, C%=59.2%) 是否与 temporal DIF 可比

### 5. 论文格式
- 是否符合 8 页正文限制
- 匿名性是否满足 double-blind 要求
- 图表是否清晰、引用是否完整

请按 ARR 审稿标准给出结构化审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (评分 1-5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1098 · 2026-05-23T09:11:02.924136+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search ARR review form",
  "prompt": "Use WebSearch to find the official ACL Rolling Review (ARR) reviewer guidelines and review form criteria for 2025-2026. I need the exact scoring dimensions and their scales (e.g., soundness, excitement, overall assessment, confidence, etc.). Search for:\n1. \"ACL Rolling Review reviewer guidelines 2026\"\n2. \"ARR review form criteria dimensions\"\n3. \"aclrollingreview.org reviewer guidelines\"\n\nReport the exact dimensions, their scales, and any descriptions of what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Search ARR review form",
    "prompt": "Use WebSearch to find the official ACL Rolling Review (ARR) reviewer guidelines and review form criteria for 2025-2026. I need the exact scoring dimensions and their scales (e.g., soundness, excitement, overall assessment, confidence, etc.). Search for:\n1. \"ACL Rolling Review reviewer guidelines 2026\"\n2. \"ARR review form criteria dimensions\"\n3. \"aclrollingreview.org reviewer guidelines\"\n\nReport the exact dimensions, their scales, and any descriptions of what each score means."
  }
}
```

</details>

---


### Tool call

_source line 1099 · 2026-05-23T09:11:03.577279+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1100 · 2026-05-23T09:11:03.778286+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1101 · 2026-05-23T09:11:04.330733+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer guidelines 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer guidelines 2026"
  }
}
```

</details>

---


### Tool call

_source line 1102 · 2026-05-23T09:11:04.531756+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 1103 · 2026-05-23T09:11:04.532194+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclrollingreview.org reviewer guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclrollingreview.org reviewer guidelines"
  }
}
```

</details>

---


### Tool result

_source line 1104 · 2026-05-23T09:11:11.321226+00:00_

Web search results for query: "aclrollingreview.org reviewer guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"},{"title":"aclrollingreview/acguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/acguidelines.md"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"}]

Based on the web search results, I found information about the ARR (ACL Rolling Review) reviewer guidelines. Here's what I found:

## ARR Reviewer Guidelines Overview

ARR developed detailed guidelines and suggestions for each step of the review process, including a list of common problems in both reviews 
…[truncated 1110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6789
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-23T09:11:13.736113+00:00_

Web search results for query: "ARR review form criteria dimensions"

Links: [{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"}]

Based on the search results, here's information about the ARR (ACL Rolling Review) review form criteria:

## Review Form Criteria for ARR

For Findings papers, the main criteria are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.

## Key Evaluation Dimensions

The review form asks reviewers to address several key dimensions:

1. **Paper Summary**: Reviewers should describe what the paper is about to help action editors and area chairs understand the topic and highlight any possible misunderstandings.

2. **Reasons to Publish**: Reviewers should explain the major reasons to publish the paper at a selective *ACL venue, which could include novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related li
…[truncated 693 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9204
}
```

</details>

---


### Tool result

_source line 1106 · 2026-05-23T09:11:14.037738+00:00_

Web search results for query: "ACL Rolling Review reviewer guidelines 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the web search results, here's information about the ACL Rolling Review Reviewer Guidelines for 2026:

## Key Reviewer Guidelines

**Anonymity and Author Identity:**
Reviewers for *ACL conferences and TACL should be instructed not to actively try to discover the identity of the authors and not to let any suspicion or knowledge of author identity affect their judgment of the paper. This should not prevent them from searching for 
…[truncated 1590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9707
}
```

</details>

---


### Tool call

_source line 1107 · 2026-05-23T09:11:16.218941+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "What are the exact scoring dimensions, scales, and descriptions for reviewer ratings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "What are the exact scoring dimensions, scales, and descriptions for reviewer ratings?"
  }
}
```

</details>

---


### Tool call

_source line 1108 · 2026-05-23T09:11:16.319610+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "What are the exact scoring dimensions, scales, rating definitions, and evaluation criteria?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "What are the exact scoring dimensions, scales, rating definitions, and evaluation criteria?"
  }
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-23T09:11:21.494228+00:00_

# ACL Rolling Review: Scoring Dimensions and Scales

## Primary Rating Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: Willing to defend evaluation, but likely missed details
- 1: "Not my area, or paper is very hard to understand"

**Soundness** (1-5 scale with .5 increments)
- 5: "Excellent: This study is one of the most thorough"
- 4: "Strong: This study provides sufficient support"
- 3: "Acceptable: This study provides sufficient support for its main claims"
- 2: "Poor: Some of the main claims are not sufficiently supported"
- 1: "Major Issues: This study is not yet sufficiently thorough"

**Excitement** (1-5 scale with .5 increments)
- 5: "Highly Exciting: I would recommend this paper"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points"
- 2: "Potentially Interesting"
- 1: "Not Exciting"

**Overall Assessment** (1-5 scale with .5 increments)
- 5: "Consider for Award"
- 4: "Conference"
- 3: "Findings"
- 2: "Resubmit next cycle"
- 1: "Do not resubmit"

## Secondary Dimensions

Reproducibility, Datasets, Software, and Author Identity Recognition each use 1-5 scales with specific criteria.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5275
}
```

</details>

---


### Tool result

_source line 1110 · 2026-05-23T09:11:21.696160+00:00_

# ARR Reviewer Scoring Dimensions

Based on the guidelines, ARR reviewers provide **three scores** starting February 2025:

1. **Soundness** - "must be justified by the text of the review." Low soundness scores require explicit justification; vague assessments indicate the review doesn't faithfully explain the recommendation.

2. **Excitement** - A subjective measure reflecting personal interest, "orthogonal to the assessment of the soundness of the paper." This captures reviewer preference independent of technical quality.

3. **Overall Recommendation** - "an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue." This composite score reflects soundness, excitement, novelty, and impact considerations.

The guidelines emphasize that papers recommended for main conferences and Findings must be "sufficiently sound and reproducible," though reviewers may recommend acceptance for papers they find technically sound but personally unexciting, particularly if the work has significant practical impact.

The document does not specify numerical scales (e.g., 1-5 ratings) or detailed rubrics for each dimension—those details appear to be in the separate ARR review form documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5376
}
```

</details>

---


### Tool call

_source line 1111 · 2026-05-23T09:11:23.620631+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md",
  "prompt": "What are the exact scoring dimensions, scales, and descriptions for each rating level?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md",
    "prompt": "What are the exact scoring dimensions, scales, and descriptions for each rating level?"
  }
}
```

</details>

---


### Tool result

_source line 1112 · 2026-05-23T09:11:32.260346+00:00_

# ARR Review Scoring Dimensions

Based on the reviewer guidelines, starting February 2025, ARR reviewers provide **three scores**:

1. **Soundness** - Technical quality and validity of the research
2. **Excitement** - Personal interest in the topic (orthogonal to soundness)
3. **Overall Assessment** - Final recommendation for acceptance

However, the document does not provide the specific rating scales, numerical ranges, or detailed descriptions for each rating level. It only states that "soundness scores must be justified by the text of the review" and that excitement scores "reflect our personal taste, and so do not necessarily come with explicit reasons."

The guidelines emphasize that "All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible," but specific score definitions (e.g., 1-5 scale descriptions) are not detailed in this document. You would need to consult the [ARR review form documentation](https://aclrollingreview.org/reviewform) referenced in the FAQ section for complete scoring rubrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8639
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-23T09:11:37.884179+00:00_

Excellent! I now have comprehensive information about the ACL Rolling Review scoring dimensions. Here's the complete report:

## ACL Rolling Review (ARR) Scoring Dimensions - 2025-2026

Based on the official ARR reviewer guidelines and review form documentation, here are the exact scoring dimensions and their scales:

### **PRIMARY SCORING DIMENSIONS (All 1-5 scale with .5 increments)**

1. **Soundness** - Technical quality and validity of the research
   - 5: "Excellent: This study is one of the most thorough"
   - 4: "Strong: This study provides sufficient support"
   - 3: "Acceptable: This study provides sufficient support for its main claims"
   - 2: "Poor: Some of the main claims are not sufficiently supported"
   - 1: "Major Issues: This study is not yet sufficiently thorough"

2. **Excitement** - Personal interest and enthusiasm for the work
   - 5: "Highly Exciting: I would recommend this paper"
   - 4: "Exciting: I would mention this paper to others"
   - 3: "Interesting: I might mention some points"
   - 2: "Potentially Interesting"
   - 1: "Not Exciting"

3. **Overall Assessment** - Final recommendation for paper acceptance
   - 5: "Consider for Award"
   - 4: "Conference"
   - 3: "Findings"
   - 2: "Resubmit next cycle"
   - 1: "Do not resubmit"

### **SECONDARY DIMENSION**

4. **Reviewer Confidence** (1-5 scale)
   - 5: "Positive that my evaluation is correct"
   - 4: "Quite sure"
   - 3: "Pretty sure, but there's a chance I missed something"
   - 2: "Willing to defend evaluation, but likely missed details"
   - 1: "Not my area, or paper is very hard to understand"

### **ADDITIONAL EVALUATION CATEGORIES**
Reviewers also evaluate:
- **Reproducibility**
- **Datasets**
- **Software**
- **Author Identity Recognition**
(Each using 1-5 scales with specific criteria)

### **Key Guidelines (Effective February 2025)**
- Soundness scores "must be justified by the text of the review"
- Excitement is intentionally orthogonal to soundness—a reviewer can find a pape
…[truncated 557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 34960
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-23T09:11:43.459056+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1115 · 2026-05-23T09:11:45.768775+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 589.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 536.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p9.png\", \"width\": 1
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2309
}
```

</details>

---


### Tool call

_source line 1116 · 2026-05-23T09:11:50.141459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1117 · 2026-05-23T09:11:50.595953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1118 · 2026-05-23T09:11:51.098902+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 1119 · 2026-05-23T09:11:51.099329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1120 · 2026-05-23T09:11:51.957166+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool call

_source line 1121 · 2026-05-23T09:11:51.957623+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1122 · 2026-05-23T09:11:52.465692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1366
}
```

</details>

---


### Tool call

_source line 1123 · 2026-05-23T09:11:52.466140+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1124 · 2026-05-23T09:11:52.919347+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 1125 · 2026-05-23T09:11:52.919805+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1126 · 2026-05-23T09:11:53.827899+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-23T09:11:53.829867+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-23T09:11:53.830152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1129 · 2026-05-23T09:11:54.332202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1130 · 2026-05-23T09:11:54.784888+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1131 · 2026-05-23T09:11:54.785339+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1132 · 2026-05-23T09:11:55.440222+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1108
}
```

</details>

---


### Tool call

_source line 1133 · 2026-05-23T09:11:55.440681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1134 · 2026-05-23T09:11:55.595537+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 810
}
```

</details>

---


### Tool result

_source line 1135 · 2026-05-23T09:11:56.149573+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 708
}
```

</details>

---


### Tool call

_source line 1136 · 2026-05-23T09:12:05.344188+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1137 · 2026-05-23T09:12:06.349057+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 483.7}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.9}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 420.7}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.0}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 223.9}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/art
…[truncated 75 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-23T09:12:09.416893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1139 · 2026-05-23T09:12:09.918798+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1140 · 2026-05-23T09:12:10.824917+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool result

_source line 1141 · 2026-05-23T09:12:10.826135+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1142 · 2026-05-23T09:12:10.826474+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1143 · 2026-05-23T09:12:11.329583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1144 · 2026-05-23T09:12:11.836658+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool call

_source line 1145 · 2026-05-23T09:12:11.837127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1146 · 2026-05-23T09:12:12.743596+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---


### Tool call

_source line 1147 · 2026-05-23T09:12:12.744041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1148 · 2026-05-23T09:12:13.196766+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool result

_source line 1149 · 2026-05-23T09:12:13.201930+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 1150 · 2026-05-23T09:12:13.203840+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 1151 · 2026-05-23T09:12:13.758467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1152 · 2026-05-23T09:12:13.861516+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 657
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-23T09:12:14.214686+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 1154 · 2026-05-23T09:14:15.405598+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1155 · 2026-05-23T09:14:15.442113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 36
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-23T09:16:22.172025+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n### Summary\n\n本文将教育测量中的 Mantel-Haenszel 差异项目功能（MH-DIF）分析应用于 LLM benchmark 评估，对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）进行大规模时序审计。核心发现是 2023 与 2024 模型队列间约 27–31% 的 MMLU 题目表现出时序 DIF（即题目测量属性随时间漂移），且此信号与 web-overlap 污染标签经验上正交（Jaccard ≈ 0.206）。论文提出 cross-subject matching 策略处理多学科污染、用 semi-synthetic injection 验证检测能力、并在 6 个 benchmark 上做了交叉验证。最终建议将 MH-DIF 作为 benchmark 常规审计工具。\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5（Borderline Conference）\n**一句话总结**: 重要且新颖的跨学科贡献，将心理测量学的 DIF 框架以大规模方式引入 LLM 评估，但核心统计量（DEFF 校正后的 C%）存在 2 倍估计分歧未充分 justify，semi-synthetic 验证与真实污染模式的差距削弱了检测能力标定的可信度。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 方法论框架严谨、诊断检查全面，但 DEFF 两种估计量差异悬殊（29.2% vs 13.5%）且选择理由不充分；IRT 假设违反的影响量化不足 |\n| Excitement | 4 / 5 | 问题重要且及时，规模令人印象深刻（5,227 模型），cross-subject matching 是对 DIF 方法的实质性改编，实践建议可操作 |\n| Reproducibility | 4 / 5 | 提供匿名化代码链接，数据基于公开 METABENCH，方法描述详尽；但 semi-synthetic injection 的部分实现细节需参考附录 |\n| Confidence | 4 / 5 | 我熟悉 DIF/IRT 方法论和 LLM 评估文献，对本审查有较高信心 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] DEFF 校正的两种估计量差异悬殊，论文选择理由不充分\n\n- 具体位置：Section 4.2, Appendix D, Appendix I (Table 12)\n- 问题：Simple-mean DEFF 给出 adjusted C% = 29.2%，weighted-mean DEFF 给出 adjusted C% = 13.5%——二者相差超过 2 倍。论文以 simple-mean 为主要报告值（Section 4.2: \"the conservative weighted-mean DEFF... converge on ≈27–29%\"），但 Appendix I 的模拟显示 weighted-mean 在大家族低 ICC 条件下更准确（\"the simple-mean estimate better captures the average inflation per family under these conditions\"）。问题在于：（1）weighted-mean 是统计学中更标准的处理方式（按样本量加权），论文将非标准选择作为 primary 报告但缺乏充分的理论论证；（2）读者面对 \"13.5% vs 29.2%\" 的差异，无法判断真实 C% 究竟在什么水平；（3）cluster bootstrap 95% CI [26.7%, 53.2%] 极宽（跨度 26.5pp），进一步加剧了不确定性，但论文未在正文充分讨论这一宽度的含义。\n- 为什么影响接收：论文的核心 claim（\"≈27–29% of MMLU items exhibit temporal DIF\"）直接依赖此选择。如果 weighted-mean 才是更合理的估计，核心发现缩减至 13.5%——仍然有意义，但 narrative 和结论强度需要显著调整。\n- 建议修改方向：（1）在正文 Section 4.2 明确报告两种估计量及其差异，而非将 weighted-mean 仅放在附录；（2）论证为何 simple-mean 更适合本场景（或承认不确定性并以区间而非点估计作为主要结论）；（3）对 cluster bootstrap CI 的宽度做实质性讨论——什么驱动了这一不确定性？是 family 结构还是 cohort 划分？\n\n**N2** [critical] Semi-synthetic 验证使用的 uniform binary flipping 与真实污染模式差距过大，检测能力标定可信度受限\n\n- 具体位置：Section 3.4, Section 4.1, Figure 2, Limitations\n- 问题：Semi-synthetic injection 采用 uniform binary response flipping（以固定概率 ρ 将正确答案翻转为错误）。但真实的 benchmark 污染表现为：（a）使题目变容易而非随机翻转方向；（b）效应大小因题目难度而异（简单题 ceiling effect，困难题收益更大）；（c）与模型能力交互（高能力模型可能已经答对，污染无额外效应）。论文将 uniform flipping 定位为 \"worst-case injection model\" 和 \"upper-bound estimate\"（Limitations, p.8），但这一定位本身有问题——uniform flipping 不一定是 worst-case，而可能是 easiest-to-detect case，因为它产生的信号比真实污染更均匀、更容易被 MH 统计量捕获。\n- 为什么影响接收：Figure 2 的 dose-response 曲线（TPR vs ρ）是论文标定 MH-DIF 检测能力的核心证据。如果 uniform flipping 使检测偏容易，则 TPR 被高估，论文关于 \"MH-DIF 在 ρ > 0.3 时具有足够检测力\" 的结论不可靠。同时，ΔFPR = 0 的 \"constructive guarantee\" 虽然在数学上成立（cross-subject matching 的结构性质），但仅限于 injection 不影响 matching variable 的前提——如果真实污染是 multi-subject 的（论文 Table 7 已示 k=20 时 ΔFPR 升至 0.047），这一保证就退化了。\n- 建议修改方向：（1）增加至少一种更现实的注入模型（如 difficulty-dependent flipping：难题翻转概率高于简单题）并比较 TPR；（2）将 \"worst-case\" 改为 \"stylized\"/\"simplified\"，准确描述其性质；（3）在正文（非仅 Limitations）讨论 uniform flipping 假设对检测力标定的影响方向。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] ETS 效应量阈值（|Δ_MH| ≥ 1.5）为人类考生设计，直接移植到 LLM 的合理性未论证\n\n- 具体位置：Section 3.2, Appendix A.2\n- 问题：ETS 分类标准（A/B/C categories）基于 |Δ_MH| 阈值，这些阈值源自教育测试中数十年的经验校准，反映人类考生群体中 \"educationally meaningful\" 的 DIF 大小。LLM 群体的方差结构完全不同——5,227 个模型的能力分布可能比人类考生更异质（bimodal: base vs instruct）或更同质（同家族内），DIF 效应量的 \"meaningful\" 标准也应不同。论文直接采用 |Δ_MH| ≥ 1.5 作为 Category C 阈值但未讨论这一移植是否合理。Appendix A.2 的 threshold sensitivity 分析显示结论在 |Δ_MH| ∈ {1.0, 1.5, 2.0, 2.5} 范围内稳健，这是有用的，但不等于论证了 1.5 在 LLM 语境下的适切性。\n- 建议：增加一段讨论 ETS 阈值在 LLM 语境下的适切性，或用 data-driven 方法（如 permutation-based null distribution）确定 LLM-specific 阈值，并与 ETS 标准比较。\n\n**W2** [warning] N=5,227 模型导致 MH chi-squared 检验统计功效过高，p-value 近乎全部显著\n\n- 具体位置：Section 3.2, Section 4.2\n- 问题：MH chi-squared 的统计功效随样本量增大。N=5,227 时，即便极小的 DIF 效应也会达到统计显著（p < 0.05）。论文报告 BH-FDR 仅移除 3/3918 items——这恰恰说明几乎所有 p-value 都极小，统计显著性已失去区分力。虽然 ETS 分类引入了效应量阈值（|Δ_MH| ≥ 1.5）作为实质性过滤，但 ETS C 分类同时要求 p < 0.05（Section 3.2），在 N=5,227 下这一条件几乎自动满足，等同于仅用效应量筛选。\n- 建议：讨论 N=5,227 下统计功效的行为，说明 ETS 分类中 p < 0.05 条件在此规模下的实际角色；考虑是否需要更严格的效应量阈值来补偿。\n\n**W3** [warning] Within-family DIF（Llama-2 vs Llama-3, C%=59.2%）与 temporal DIF 的可比性存疑\n\n- 具体位置：Section 3.3 (Cohort 3), Appendix N, Table 14\n- 问题：Within-family cohort 比较 Llama-2（N=161）vs Llama-3（N=308），但这两代模型在架构、规模、训练数据上存在根本差异。观察到的 C%=59.2% 可能反映的是架构/能力代际差异而非 temporal DIF——两者在此设计中完全混淆。论文在 Appendix N 将其定位为 \"confirming that temporal DIF is not an artifact of comparing different architectures\"，但逻辑上恰恰相反：within-family 比较中 C% 更高可能表明 DIF 信号部分来自架构差异而非时间效应。\n- 建议：重新框架化 within-family 分析的解释——它不能 confirm temporal DIF 不是架构伪迹，而是说明 DIF 在 within-family 比较中更强，可能因为架构差异叠加了时间效应。或者提供 within-architecture same-generation 的比较作为对照。\n\n**W4** [warning] GSM1K 相关性分析（r = -0.478, N = 33）作为验证证据偏弱且存在过度解读风险\n\n- 具体位置：Section 4.7, Appendix F, Figure 5\n- 问题：论文将 GSM1K contamination gap 与 DIF ranking advantage 的负相关作为 \"independently confirming the DIF-contamination orthogonality\" 的证据（Section 4.7: \"SNAP > 0.012, independently confirming the DIF-contamination orthogonality\"）。但（1）N=33 极小，r=-0.478 的 95% CI 包含较弱的效应量；（2）33 个模型是 GSM1K 数据集中可用模型的全集还是子集？如果是子集，选择偏差需讨论；（3）相关方向（负相关）的因果解释不明确——为什么 DIF ranking advantage 高的模型反而 contamination gap 低？论文虽标注 \"exploratory\"（Figure 5 caption），但在 Section 4.7 正文中用 \"confirms\" 语气呈现。\n- 建议：统一 exploratory 定位，避免在正文用 \"confirms\"/\"confirming\" 表述；报告 r 的 confidence interval；讨论样本代表性。\n\n**W5** [warning] Local independence 违反的定量影响未充分评估\n\n- 具体位置：Section 4.5, Appendix A.1\n- 问题：Appendix A.1 报告了 Yen's Q3 诊断，发现 within-subject 和 cross-subject item pairs 存在 elevated residual correlations（|Q3| > 0.20 的比例较高）。但论文未将这些 Q3 违反与 DIF detection rate 的 inflation 做定量关联。DEFF 校正处理的是 family-level clustering（模型间非独立性），而 Q3 反映的是 item-level local dependence（题目间非独立性）——这是两个不同层面的非独立性问题，DEFF 不能替代对 Q3 的处理。\n- 建议：量化 item-level local dependence 对 MH-DIF 检测率的具体影响。例如，通过模拟 Q3 水平不同的数据，评估 local dependence 对 false DIF detection rate 的贡献。或至少讨论为什么 family-level DEFF 校正足以同时处理 item-level local dependence。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 3.2: \"K = 5 equiprobable strata (quintile-based binning) following ETS recommended practice\" — 引用了 Donoghue and Allen (1993) 和 Clauser and Mazor (1998)，但这些引用针对的是人类考试场景。建议增加一句说明 K=5 在 LLM 设置下的适切性（如 LLM 能力分布可能需要不同的 K 值）。\n\n- Table 1: \"Dashes (–) indicate comparisons where Li et al. labels are not available\" — 但表中 CV enrichment 列的 dash 含义应明确区分 \"不适用\" 与 \"数据缺失\"。\n\n- Figure 1 caption 较长（约 8 行），建议精简，将细节移入正文。\n\n- Limitations 段落提到 \"The MH χ² test assumes independent examinees; LLM model families violate this assumption\"，但此处的 \"independent examinees\" 容易与 local independence 混淆——实际指的是 examinees 之间的独立性（即模型间非独立性），建议措辞更精确。\n\n- 论文脚注 1 提供了匿名代码链接，满足 double-blind 要求。\n\n---\n\n## 主要优势\n\n1. **问题的重要性和及时性**：LLM benchmark 分数的跨时间可比性是一个被广泛假设但很少被系统验证的问题。论文以 5,227 个模型的规模进行定量审计，填补了重要的方法论空白。\n\n2. **Cross-subject matching 是对经典 DIF 的实质性创新**：论文识别出 LLM multi-domain benchmark 中 matching variable 会被污染的问题，并提出用其他学科的总分作为 matching variable——这不是简单套用教育测量方法，而是有针对性的方法论适配，包括 ΔFPR = 0 的结构性保证（在单学科注入条件下）。\n\n3. **多层次 robustness 检查**：graduated de-duplication（Table 2 系列）、LOFO（Table 8）、random split 负对照、cross-benchmark 验证（Table 3, 6 个 benchmark）、within-architecture 分析（Table 14）——这些检查覆盖了统计功效、家族结构、benchmark 特异性等多个维度的 confound。\n\n4. **\"两维度\" 框架的概念贡献**：将 global exposure（web-overlap）和 differential functioning（DIF）区分为互补的正交维度（Section 5.1, Figure 1），为 benchmark integrity 的讨论提供了新的概念结构。实证上 Jaccard ≈ 0.206 和 association tests 的 near-independence（OR = 1.01, Section 4.3）支持这一区分。\n\n5. **写作质量**：论文在 8 页内清晰呈现了复杂的方法论框架，Figure 1 的 ICC 双图对照直观有效，附录组织有序提供了详尽的补充分析。\n\n---\n\n**总结**：这是一篇有实质贡献的跨学科论文，将心理测量学方法成功引入 LLM 评估领域。核心发现（temporal DIF 广泛存在）在多个 robustness check 下成立。主要顾虑集中在两点：（1）DEFF 校正的估计量选择显著影响核心数字但未充分论证；（2）semi-synthetic 验证的注入模型过于理想化，限制了检测能力标定的外部效度。这两个问题可在修订中解决，不构成根本性缺陷。建议 Borderline Conference，倾向积极——如果作者能在修订中澄清 DEFF 选择并增加更现实的注入模型比较，本文可达到 Conference 水准。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n### Summary\n\n本文将教育测量中的 Mantel-Haenszel 差异项目功能（MH-DIF）分析应用于 LLM benchmark 评估，对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）进行大规模时序审计。核心发现是 2023 与 2024 模型队列间约 27–31% 的 MMLU 题目表现出时序 DIF（即题目测量属性随时间漂移），且此信号与 web-overlap 污染标签经验上正交（Jaccard ≈ 0.206）。论文提出 cross-subject matching 策略处理多学科污染、用 semi-synthetic injection 验证检测能力、并在 6 个 benchmark 上做了交叉验证。最终建议将 MH-DIF 作为 benchmark 常规审计工具。\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5（Borderline Conference）\n**一句话总结**: 重要且新颖的跨学科贡献，将心理测量学的 DIF 框架以大规模方式引入 LLM 评估，但核心统计量（DEFF 校正后的 C%）存在 2 倍估计分歧未充分 justify，semi-synthetic 验证与真实污染模式的差距削弱了检测能力标定的可信度。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 方法论框架严谨、诊断检查全面，但 DEFF 两种估计量差异悬殊（29.2% vs 13.5%）且选择理由不充分；IRT 假设违反的影响量化不足 |\n| Excitement | 4 / 5 | 问题重要且及时，规模令人印象深刻（5,227 模型），cross-subject matching 是对 DIF 方法的实质性改编，实践建议可操作 |\n| Reproducibility | 4 / 5 | 提供匿名化代码链接，数据基于公开 METABENCH，方法描述详尽；但 semi-synthetic injection 的部分实现细节需参考附录 |\n| Confidence | 4 / 5 | 我熟悉 DIF/IRT 方法论和 LLM 评估文献，对本审查有较高信心 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] DEFF 校正的两种估计量差异悬殊，论文选择理由不充分\n\n- 具体位置：Section 4.2, Appendix D, Appendix I (Table 12)\n- 问题：Simple-mean DEFF 给出 adjusted C% = 29.2%，weighted-mean DEFF 给出 adjusted C% = 13.5%——二者相差超过 2 倍。论文以 simple-mean 为主要报告值（Section 4.2: \"the conservative weighted-mean DEFF... converge on ≈27–29%\"），但 Appendix I 的模拟显示 weighted-mean 在大家族低 ICC 条件下更准确（\"the simple-mean estimate better captures the average inflation per family under these conditions\"）。问题在于：（1）weighted-mean 是统计学中更标准的处理方式（按样本量加权），论文将非标准选择作为 primary 报告但缺乏充分的理论论证；（2）读者面对 \"13.5% vs 29.2%\" 的差异，无法判断真实 C% 究竟在什么水平；（3）cluster bootstrap 95% CI [26.7%, 53.2%] 极宽（跨度 26.5pp），进一步加剧了不确定性，但论文未在正文充分讨论这一宽度的含义。\n- 为什么影响接收：论文的核心 claim（\"≈27–29% of MMLU items exhibit temporal DIF\"）直接依赖此选择。如果 weighted-mean 才是更合理的估计，核心发现缩减至 13.5%——仍然有意义，但 narrative 和结论强度需要显著调整。\n- 建议修改方向：（1）在正文 Section 4.2 明确报告两种估计量及其差异，而非将 weighted-mean 仅放在附录；（2）论证为何 simple-mean 更适合本场景（或承认不确定性并以区间而非点估计作为主要结论）；（3）对 cluster bootstrap CI 的宽度做实质性讨论——什么驱动了这一不确定性？是 family 结构还是 cohort 划分？\n\n**N2** [critical] Semi-synthetic 验证使用的 uniform binary flipping 与真实污染模式差距过大，检测能力标定可信度受限\n\n- 具体位置：Section 3.4, Section 4.1, Figure 2, Limitations\n- 问题：Semi-synthetic injection 采用 uniform binary response flipping（以固定概率 ρ 将正确答案翻转为错误）。但真实的 benchmark 污染表现为：（a）使题目变容易而非随机翻转方向；（b）效应大小因题目难度而异（简单题 ceiling effect，困难题收益更大）；（c）与模型能力交互（高能力模型可能已经答对，污染无额外效应）。论文将 uniform flipping 定位为 \"worst-case injection model\" 和 \"upper-bound estimate\"（Limitations, p.8），但这一定位本身有问题——uniform flipping 不一定是 worst-case，而可能是 easiest-to-detect case，因为它产生的信号比真实污染更均匀、更容易被 MH 统计量捕获。\n- 为什么影响接收：Figure 2 的 dose-response 曲线（TPR vs ρ）是论文标定 MH-DIF 检测能力的核心证据。如果 uniform flipping 使检测偏容易，则 TPR 被高估，论文关于 \"MH-DIF 在 ρ > 0.3 时具有足够检测力\" 的结论不可靠。同时，ΔFPR = 0 的 \"constructive guarantee\" 虽然在数学上成立（cross-subject matching 的结构性质），但仅限于 injection 不影响 matching variable 的前提——如果真实污染是 multi-subject 的（论文 Table 7 已示 k=20 时 ΔFPR 升至 0.047），这一保证就退化了。\n- 建议修改方向：（1）增加至少一种更现实的注入模型（如 difficulty-dependent flipping：难题翻转概率高于简单题）并比较 TPR；（2）将 \"worst-case\" 改为 \"stylized\"/\"simplified\"，准确描述其性质；（3）在正文（非仅 Limitations）讨论 uniform flipping 假设对检测力标定的影响方向。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] ETS 效应量阈值（|Δ_MH| ≥ 1.5）为人类考生设计，直接移植到 LLM 的合理性未论证\n\n- 具体位置：Section 3.2, Appendix A.2\n- 问题：ETS 分类标准（A/B/C categories）基于 |Δ_MH| 阈值，这些阈值源自教育测试中数十年的经验校准，反映人类考生群体中 \"educationally meaningful\" 的 DIF 大小。LLM 群体的方差结构完全不同——5,227 个模型的能力分布可能比人类考生更异质（bimodal: base vs instruct）或更同质（同家族内），DIF 效应量的 \"meaningful\" 标准也应不同。论文直接采用 |Δ_MH| ≥ 1.5 作为 Category C 阈值但未讨论这一移植是否合理。Appendix A.2 的 threshold sensitivity 分析显示结论在 |Δ_MH| ∈ {1.0, 1.5, 2.0, 2.5} 范围内稳健，这是有用的，但不等于论证了 1.5 在 LLM 语境下的适切性。\n- 建议：增加一段讨论 ETS 阈值在 LLM 语境下的适切性，或用 data-driven 方法（如 permutation-based null distribution）确定 LLM-specific 阈值，并与 ETS 标准比较。\n\n**W2** [warning] N=5,227 模型导致 MH chi-squared 检验统计功效过高，p-value 近乎全部显著\n\n- 具体位置：Section 3.2, Section 4.2\n- 问题：MH chi-squared 的统计功效随样本量增大。N=5,227 时，即便极小的 DIF 效应也会达到统计显著（p < 0.05）。论文报告 BH-FDR 仅移除 3/3918 items——这恰恰说明几乎所有 p-value 都极小，统计显著性已失去区分力。虽然 ETS 分类引入了效应量阈值（|Δ_MH| ≥ 1.5）作为实质性过滤，但 ETS C 分类同时要求 p < 0.05（Section 3.2），在 N=5,227 下这一条件几乎自动满足，等同于仅用效应量筛选。\n- 建议：讨论 N=5,227 下统计功效的行为，说明 ETS 分类中 p < 0.05 条件在此规模下的实际角色；考虑是否需要更严格的效应量阈值来补偿。\n\n**W3** [warning] Within-family DIF（Llama-2 vs Llama-3, C%=59.2%）与 temporal DIF 的可比性存疑\n\n- 具体位置：Section 3.3 (Cohort 3), Appendix N, Table 14\n- 问题：Within-family cohort 比较 Llama-2（N=161）vs Llama-3（N=308），但这两代模型在架构、规模、训练数据上存在根本差异。观察到的 C%=59.2% 可能反映的是架构/能力代际差异而非 temporal DIF——两者在此设计中完全混淆。论文在 Appendix N 将其定位为 \"confirming that temporal DIF is not an artifact of comparing different architectures\"，但逻辑上恰恰相反：within-family 比较中 C% 更高可能表明 DIF 信号部分来自架构差异而非时间效应。\n- 建议：重新框架化 within-family 分析的解释——它不能 confirm temporal DIF 不是架构伪迹，而是说明 DIF 在 within-family 比较中更强，可能因为架构差异叠加了时间效应。或者提供 within-architecture same-generation 的比较作为对照。\n\n**W4** [warning] GSM1K 相关性分析（r = -0.478, N = 33）作为验证证据偏弱且存在过度解读风险\n\n- 具体位置：Section 4.7, Appendix F, Figure 5\n- 问题：论文将 GSM1K contamination gap 与 DIF ranking advantage 的负相关作为 \"independently confirming the DIF-contamination orthogonality\" 的证据（Section 4.7: \"SNAP > 0.012, independently confirming the DIF-contamination orthogonality\"）。但（1）N=33 极小，r=-0.478 的 95% CI 包含较弱的效应量；（2）33 个模型是 GSM1K 数据集中可用模型的全集还是子集？如果是子集，选择偏差需讨论；（3）相关方向（负相关）的因果解释不明确——为什么 DIF ranking advantage 高的模型反而 contamination gap 低？论文虽标注 \"exploratory\"（Figure 5 caption），但在 Section 4.7 正文中用 \"confirms\" 语气呈现。\n- 建议：统一 exploratory 定位，避免在正文用 \"confirms\"/\"confirming\" 表述；报告 r 的 confidence interval；讨论样本代表性。\n\n**W5** [warning] Local independence 违反的定量影响未充分评估\n\n- 具体位置：Section 4.5, Appendix A.1\n- 问题：Appendix A.1 报告了 Yen's Q3 诊断，发现 within-subject 和 cross-subject item pairs 存在 elevated residual correlations（|Q3| > 0.20 的比例较高）。但论文未将这些 Q3 违反与 DIF detection rate 的 inflation 做定量关联。DEFF 校正处理的是 family-level clustering（模型间非独立性），而 Q3 反映的是 item-level local dependence（题目间非独立性）——这是两个不同层面的非独立性问题，DEFF 不能替代对 Q3 的处理。\n- 建议：量化 item-level local dependence 对 MH-DIF 检测率的具体影响。例如，通过模拟 Q3 水平不同的数据，评估 local dependence 对 false DIF detection rate 的贡献。或至少讨论为什么 family-level DEFF 校正足以同时处理 item-level local dependence。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 3.2: \"K = 5 equiprobable strata (quintile-based binning) following ETS recommended practice\" — 引用了 Donoghue and Allen (1993) 和 Clauser and Mazor (1998)，但这些引用针对的是人类考试场景。建议增加一句说明 K=5 在 LLM 设置下的适切性（如 LLM 能力分布可能需要不同的 K 值）。\n\n- Table 1: \"Dashes (–) indicate comparisons where Li et al. labels are not available\" — 但表中 CV enrichment 列的 dash 含义应明确区分 \"不适用\" 与 \"数据缺失\"。\n\n- Figure 1 caption 较长（约 8 行），建议精简，将细节移入正文。\n\n- Limitations 段落提到 \"The MH χ² test assumes independent examinees; LLM model families violate this assumption\"，但此处的 \"independent examinees\" 容易与 local independence 混淆——实际指的是 examinees 之间的独立性（即模型间非独立性），建议措辞更精确。\n\n- 论文脚注 1 提供了匿名代码链接，满足 double-blind 要求。\n\n---\n\n## 主要优势\n\n1. **问题的重要性和及时性**：LLM benchmark 分数的跨时间可比性是一个被广泛假设但很少被系统验证的问题。论文以 5,227 个模型的规模进行定量审计，填补了重要的方法论空白。\n\n2. **Cross-subject matching 是对经典 DIF 的实质性创新**：论文识别出 LLM multi-domain benchmark 中 matching variable 会被污染的问题，并提出用其他学科的总分作为 matching variable——这不是简单套用教育测量方法，而是有针对性的方法论适配，包括 ΔFPR = 0 的结构性保证（在单学科注入条件下）。\n\n3. **多层次 robustness 检查**：graduated de-duplication（Table 2 系列）、LOFO（Table 8）、random split 负对照、cross-benchmark 验证（Table 3, 6 个 benchmark）、within-architecture 分析（Table 14）——这些检查覆盖了统计功效、家族结构、benchmark 特异性等多个维度的 confound。\n\n4. **\"两维度\" 框架的概念贡献**：将 global exposure（web-overlap）和 differential functioning（DIF）区分为互补的正交维度（Section 5.1, Figure 1），为 benchmark integrity 的讨论提供了新的概念结构。实证上 Jaccard ≈ 0.206 和 association tests 的 near-independence（OR = 1.01, Section 4.3）支持这一区分。\n\n5. **写作质量**：论文在 8 页内清晰呈现了复杂的方法论框架，Figure 1 的 ICC 双图对照直观有效，附录组织有序提供了详尽的补充分析。\n\n---\n\n**总结**：这是一篇有实质贡献的跨学科论文，将心理测量学方法成功引入 LLM 评估领域。核心发现（temporal DIF 广泛存在）在多个 robustness check 下成立。主要顾虑集中在两点：（1）DEFF 校正的估计量选择显著影响核心数字但未充分论证；（2）semi-synthetic 验证的注入模型过于理想化，限制了检测能力标定的外部效度。这两个问题可在修订中解决，不构成根本性缺陷。建议 Borderline Conference，倾向积极——如果作者能在修订中澄清 DEFF 选择并增加更现实的注入模型比较，本文可达到 Conference 水准。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1157 · 2026-05-23T09:16:26.037169+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3865
}
```

</details>

---


### Assistant

_source line 1158 · 2026-05-23T09:16:36.675499+00:00_

审稿意见已提交给 Review Director。

核心评判：**Overall 3.5 / 5（Borderline Conference）**。

两个 Must-Fix：
1. **DEFF 校正分歧**——simple-mean（29.2%）vs weighted-mean（13.5%）差异 2 倍，直接影响核心 claim 的数字基础，选择理由不充分
2. **Semi-synthetic 验证的注入模型过于理想化**——uniform binary flipping 可能是 easiest-to-detect 而非 worst-case，检测力标定的外部效度受限

五个 Should-Fix：ETS 阈值移植合理性未论证、N=5227 下 p-value 失去区分力、within-family DIF 与架构差异混淆、GSM1K 相关性过度解读、local independence 违反的定量影响缺失。

总体判断：实质性跨学科贡献，核心发现在多个 robustness check 下成立，但两个关键统计选择需要在修订中澄清。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 40

## Round 40

4 recorded events


### User

_source line 1159 · 2026-05-23T09:22:24.310377+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见（新颖性 + 完整性 + Related Work）

**Overall**: 3.5 / 5（Borderline Conference）

### Must-Fix

**N1** [critical] 方法论贡献被过度声称（Overclaiming of framework contribution）
- Cross-subject matching 是 purified subtest matching 的直接适配，DEFF correction 是调查方法学标准技术，semi-synthetic validation 使用最简单的模拟方式。论文在 Section 2 说"We do not modify the MH procedure"，与 Introduction 中将 framework 列为独立贡献（Contribution 3）矛盾。建议将论文定位为"大规模实证研究 + 标准方法的领域适配"。

**N2** [critical] "两维度"贡献的新颖性存疑
- Global exposure 和 differential functioning 在定义层面就是不同维度。一个项目可以全局暴露高但无 DIF，反之亦然。因此它们的低相关（Jaccard=0.206）是从构念定义可预期的结果，而非令人惊讶的实证发现。将预期结果包装为"发现"削弱可信度。

### Should-Fix

**W1** 遗漏 concurrent work：CoDeC（ICLR 2026）。

**W2** 半合成验证的生态效度不足——真实的污染效应远比 uniform binary flipping 复杂（部分记忆、格式特定优势、能力依赖的差异性）。

**W3** 可操作性缺口——DIF 是 mechanism-agnostic 的，但论文推荐"mechanism-conditional responses"，实践者如何判断应该 remove 还是 annotate？

**W4** 非 MMLU 基准的分析深度不足——除 MMLU 外的 5 个基准仅在 Table 3 中各占一行数据，无结构分析。

**W5** 标题中"5,227 Models"可能产生误导——核心时序分析仅用 1,887 个模型。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1160 · 2026-05-23T09:24:15.143789+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE with nuance] R2-N1: 方法论贡献被过度声称**\n\nR2 指出 cross-subject matching 是 purified subtest matching 的直接适配、DEFF 是标准调查方法学、semi-synthetic validation 是最简模拟——这些判断在技术层面成立。Section 2 (p.3) 明确写道 \"We do not modify the MH procedure; our contribution is in the application context and the empirical findings it reveals\"，但 Introduction 的 Contribution 3 又将 \"Temporal DIF audit framework\" 列为独立贡献——这两处表述确实存在张力。\n\n但我认为 R2 的批评略显过度。Cross-subject matching 虽源自 purified subtest matching，但其在 LLM multi-domain benchmark 中的具体实现——用其他学科总分作为 matching variable 以隔离单学科污染——有其特定的方法论考量，特别是 Section 3.4 证明的 ΔFPR = 0 结构性保证（在单学科注入条件下）。这不是\"拿来就用\"，而是需要论证 matching variable 在新语境下的有效性。\n\n**建议**：将 Contribution 3 重新表述为\"标准 DIF 方法在 LLM 评估中的系统性适配与大规模实证验证\"，而非暗示方法论创新。这样既承认了技术上的非原创性，也保留了应用层面的贡献。\n\n---\n\n**[REBUT] R2-N2: \"两维度\"贡献的新颖性存疑**\n\nR2 认为 global exposure 和 differential functioning 在定义层面就是不同维度，因此低相关是可预期的结果。我不完全同意。\n\nR2 的论点在心理测量学视角下是成立的——\"暴露\"和\"功能差异\"当然是可分离的概念。但在 NLP 社区的实际研究实践中，这一区分并未被广泛认识。现有的 contamination detection 文献（如 Li et al., 2024b 的 web-overlap；Shi et al., 2024 的 Min-K%++）隐含地假设\"被污染的题目 = 测量失真的题目\"。论文的实证贡献在于用大规模数据 **量化了** 这一预期中的关联实际上有多弱：Jaccard ≈ 0.206（Section 4.3），OR = 1.01（Section 4.3: \"Association tests confirm near-independence\"），DIF-C rates 对 web-contaminated 和 non-contaminated items 几乎相同（30.7% vs 另一组，差异极小）。\n\n关键证据在 Figure 1（p.2）的 ICC 对照图：左图（global contamination）显示暴露本身不产生 DIF，而右图（differential contamination）才产生 DIF。这一视觉展示将概念区分转化为了可观察的经验模式。\n\n不过，我同意论文的 framing 可以改进——将\"两维度\"从\"surprising discovery\"调整为\"empirical quantification of a theoretically expected but previously unverified distinction\"会更准确。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: 遗漏 concurrent work CoDeC (ICLR 2026)**\n\n如果 CoDeC 确实是 ICLR 2026 发表的 contamination detection 相关工作，且在本文投稿前已公开（如 arXiv），则应在 Section 2 的 Related Work 中讨论。concurrent work 的遗漏是一个合理的完整性问题。但需核实 CoDeC 的具体发表时间线——如果在本文投稿后才公开，则不构成遗漏。\n\n---\n\n**[AGREE] R2-W2: 半合成验证的生态效度不足**\n\n这与我自己的 N2 一致。Uniform binary flipping 是最简的注入模型，真实污染涉及部分记忆、格式特定优势、能力依赖效应。我在自己的审稿中已将此列为 Must-Fix，要求增加至少一种更现实的注入模型（如 difficulty-dependent flipping）。两位 reviewer 的一致意见增强了此修改请求的权重。\n\n---\n\n**[AGREE with nuance] R2-W3: 可操作性缺口**\n\nR2 的观察有道理——论文 Section 5.2 推荐 \"mechanism-conditional responses\"（remove, annotate, or retain），但未给出判断标准。对于实践者来说，检测到 DIF 后的 next step 不明确。\n\n但我认为这一批评应适度。DIF 分析本质上是诊断工具，不是处方——正如医学检测发现异常后需要后续临床判断。论文的贡献在于提供诊断能力，不必须解决所有下游决策问题。Section 5.2 已引用了 Kolen and Brennan (2014) 和 Habba et al. (2026) 作为 equating adjustments 的参考方向。\n\n**建议**：在 Section 5.2 增加 1-2 句具体的决策启发式（如 \"items with |Δ_MH| > 2.0 and concurrent web-overlap flags should be prioritized for removal\"），但不要求完整的 decision framework。\n\n---\n\n**[REBUT] R2-W4: 非 MMLU 基准的分析深度不足**\n\nR2 批评除 MMLU 外的 5 个 benchmark 仅在 Table 3 各占一行。但我认为这一设计是合理的：\n\n1. MMLU 是最大的 benchmark（12,508 items, 5,227 models），也是 METABENCH 中结构最复杂的（57 subjects），因此作为 primary analysis 对象是自然的选择。\n2. Table 3 的 cross-benchmark 分析目的是 **replication**，不是独立的 deep dive。6 个 benchmark 的 C% 一致性（17.9%–31.3%，knowledge-intensive consistently > procedural）已足以支撑泛化性。\n3. 论文在 Appendix F 进一步提供了 cross-benchmark 细节。\n4. 8 页正文限制下，将篇幅分配给 MMLU 的深度分析而非广度铺开是合理的取舍。\n\n如果要求每个 benchmark 都做 LOFO、DEFF、within-family 等完整分析，论文会变成 6 篇论文的合集。Cross-benchmark 作为 robustness check 而非独立贡献，Table 3 的深度已足够。\n\n---\n\n**[REBUT] R2-W5: 标题中 \"5,227 Models\" 可能产生误导**\n\n论文 Section 3.1 (p.4) 明确定义：\"The primary dataset is the METABENCH response matrix... which records binary outcomes (1 = correct, 0 = incorrect) for 5,227 models evaluated on 12,508 MMLU items.\" 所有 5,227 个模型都参与了 response matrix 的构建和 DIF 分析的不同层面：\n\n- Temporal cohort (N=1,887) 是核心时序分析\n- Ability-quartile cohort 使用全部模型\n- Within-family, Within-subject, Random-split cohorts 使用不同子集\n- DEFF 估计（Appendix D）使用全部 5,227 模型的 family 结构\n\n标题说 \"A Large-Scale Psychometric Audit of 5,227 Models\" 描述的是审计范围（response matrix 的规模），而非暗示所有分析都使用全部 5,227 个模型。Section 3.3 (p.5) 清楚列出了每个 cohort 的具体 N 值。读者不会被误导。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE with nuance] R2-N1: 方法论贡献被过度声称**\n\nR2 指出 cross-subject matching 是 purified subtest matching 的直接适配、DEFF 是标准调查方法学、semi-synthetic validation 是最简模拟——这些判断在技术层面成立。Section 2 (p.3) 明确写道 \"We do not modify the MH procedure; our contribution is in the application context and the empirical findings it reveals\"，但 Introduction 的 Contribution 3 又将 \"Temporal DIF audit framework\" 列为独立贡献——这两处表述确实存在张力。\n\n但我认为 R2 的批评略显过度。Cross-subject matching 虽源自 purified subtest matching，但其在 LLM multi-domain benchmark 中的具体实现——用其他学科总分作为 matching variable 以隔离单学科污染——有其特定的方法论考量，特别是 Section 3.4 证明的 ΔFPR = 0 结构性保证（在单学科注入条件下）。这不是\"拿来就用\"，而是需要论证 matching variable 在新语境下的有效性。\n\n**建议**：将 Contribution 3 重新表述为\"标准 DIF 方法在 LLM 评估中的系统性适配与大规模实证验证\"，而非暗示方法论创新。这样既承认了技术上的非原创性，也保留了应用层面的贡献。\n\n---\n\n**[REBUT] R2-N2: \"两维度\"贡献的新颖性存疑**\n\nR2 认为 global exposure 和 differential functioning 在定义层面就是不同维度，因此低相关是可预期的结果。我不完全同意。\n\nR2 的论点在心理测量学视角下是成立的——\"暴露\"和\"功能差异\"当然是可分离的概念。但在 NLP 社区的实际研究实践中，这一区分并未被广泛认识。现有的 contamination detection 文献（如 Li et al., 2024b 的 web-overlap；Shi et al., 2024 的 Min-K%++）隐含地假设\"被污染的题目 = 测量失真的题目\"。论文的实证贡献在于用大规模数据 **量化了** 这一预期中的关联实际上有多弱：Jaccard ≈ 0.206（Section 4.3），OR = 1.01（Section 4.3: \"Association tests confirm near-independence\"），DIF-C rates 对 web-contaminated 和 non-contaminated items 几乎相同（30.7% vs 另一组，差异极小）。\n\n关键证据在 Figure 1（p.2）的 ICC 对照图：左图（global contamination）显示暴露本身不产生 DIF，而右图（differential contamination）才产生 DIF。这一视觉展示将概念区分转化为了可观察的经验模式。\n\n不过，我同意论文的 framing 可以改进——将\"两维度\"从\"surprising discovery\"调整为\"empirical quantification of a theoretically expected but previously unverified distinction\"会更准确。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: 遗漏 concurrent work CoDeC (ICLR 2026)**\n\n如果 CoDeC 确实是 ICLR 2026 发表的 contamination detection 相关工作，且在本文投稿前已公开（如 arXiv），则应在 Section 2 的 Related Work 中讨论。concurrent work 的遗漏是一个合理的完整性问题。但需核实 CoDeC 的具体发表时间线——如果在本文投稿后才公开，则不构成遗漏。\n\n---\n\n**[AGREE] R2-W2: 半合成验证的生态效度不足**\n\n这与我自己的 N2 一致。Uniform binary flipping 是最简的注入模型，真实污染涉及部分记忆、格式特定优势、能力依赖效应。我在自己的审稿中已将此列为 Must-Fix，要求增加至少一种更现实的注入模型（如 difficulty-dependent flipping）。两位 reviewer 的一致意见增强了此修改请求的权重。\n\n---\n\n**[AGREE with nuance] R2-W3: 可操作性缺口**\n\nR2 的观察有道理——论文 Section 5.2 推荐 \"mechanism-conditional responses\"（remove, annotate, or retain），但未给出判断标准。对于实践者来说，检测到 DIF 后的 next step 不明确。\n\n但我认为这一批评应适度。DIF 分析本质上是诊断工具，不是处方——正如医学检测发现异常后需要后续临床判断。论文的贡献在于提供诊断能力，不必须解决所有下游决策问题。Section 5.2 已引用了 Kolen and Brennan (2014) 和 Habba et al. (2026) 作为 equating adjustments 的参考方向。\n\n**建议**：在 Section 5.2 增加 1-2 句具体的决策启发式（如 \"items with |Δ_MH| > 2.0 and concurrent web-overlap flags should be prioritized for removal\"），但不要求完整的 decision framework。\n\n---\n\n**[REBUT] R2-W4: 非 MMLU 基准的分析深度不足**\n\nR2 批评除 MMLU 外的 5 个 benchmark 仅在 Table 3 各占一行。但我认为这一设计是合理的：\n\n1. MMLU 是最大的 benchmark（12,508 items, 5,227 models），也是 METABENCH 中结构最复杂的（57 subjects），因此作为 primary analysis 对象是自然的选择。\n2. Table 3 的 cross-benchmark 分析目的是 **replication**，不是独立的 deep dive。6 个 benchmark 的 C% 一致性（17.9%–31.3%，knowledge-intensive consistently > procedural）已足以支撑泛化性。\n3. 论文在 Appendix F 进一步提供了 cross-benchmark 细节。\n4. 8 页正文限制下，将篇幅分配给 MMLU 的深度分析而非广度铺开是合理的取舍。\n\n如果要求每个 benchmark 都做 LOFO、DEFF、within-family 等完整分析，论文会变成 6 篇论文的合集。Cross-benchmark 作为 robustness check 而非独立贡献，Table 3 的深度已足够。\n\n---\n\n**[REBUT] R2-W5: 标题中 \"5,227 Models\" 可能产生误导**\n\n论文 Section 3.1 (p.4) 明确定义：\"The primary dataset is the METABENCH response matrix... which records binary outcomes (1 = correct, 0 = incorrect) for 5,227 models evaluated on 12,508 MMLU items.\" 所有 5,227 个模型都参与了 response matrix 的构建和 DIF 分析的不同层面：\n\n- Temporal cohort (N=1,887) 是核心时序分析\n- Ability-quartile cohort 使用全部模型\n- Within-family, Within-subject, Random-split cohorts 使用不同子集\n- DEFF 估计（Appendix D）使用全部 5,227 模型的 family 结构\n\n标题说 \"A Large-Scale Psychometric Audit of 5,227 Models\" 描述的是审计范围（response matrix 的规模），而非暗示所有分析都使用全部 5,227 个模型。Section 3.3 (p.5) 清楚列出了每个 cohort 的具体 N 值。读者不会被误导。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-23T09:24:19.032523+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3888
}
```

</details>

---


### Assistant

_source line 1162 · 2026-05-23T09:24:31.129586+00:00_

已提交对 Reviewer 2 的逐条回应。总结：

- **R2-N1**（方法贡献过度声称）：[AGREE with nuance] — 技术组件确非原创，但 cross-subject matching 的 LLM 适配有实质考量，建议调整 framing 而非否定贡献
- **R2-N2**（两维度新颖性）：[REBUT] — 概念区分在心理测量学中不新，但在 NLP 社区中未被量化验证，Figure 1 的经验证据有独立价值
- **R2-W1**（遗漏 CoDeC）：[AGREE]，需核实时间线
- **R2-W2**（半合成生态效度）：[AGREE]，与我的 N2 一致
- **R2-W3**（可操作性缺口）：[AGREE with nuance]，DIF 本质是诊断工具，增加简要启发式即可
- **R2-W4**（非 MMLU 深度不足）：[REBUT]，cross-benchmark 作为 replication check 而非独立贡献，当前深度合理
- **R2-W5**（标题误导）：[REBUT]，5,227 描述审计范围，各 cohort N 值在正文清楚列出

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 41

## Round 41

56 recorded events


### User

_source line 1163 · 2026-05-23T10:19:20.832617+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查方法严谨性和统计有效性。

## 审稿任务

**论文**: "Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"
**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`
**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf`
**目标 Venue**: EMNLP 2026 (via ARR)
**格式要求**: Long paper, 8 页正文限制, ACL 模板, double-blind, mandatory Limitations section（不计入页数）, 无限引用

## 你的审查侧重

**方法严谨性 + 统计有效性**，重点关注：

1. **MH-DIF 方法论适用性**: MH-DIF 从教育测量迁移到 LLM 评估的统计假设是否成立？ETS 阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 的合理性。N=5,227 下 p-value 的统计功效和区分力。
2. **DEFF 校正**: simple-mean (29.2%) vs weighted-mean (13.5%) 两种估计量差异 2 倍，论文是否充分解释了选择偏好和偏差来源？Simulation study (App I) 是否足够有说服力？
3. **Semi-synthetic 验证框架**: uniform binary flipping 是否是 easiest-to-detect 而非 worst-case？ΔTPR 的外部效度。difficulty-dependent injection 是否充分缓解了这个concern？
4. **Cross-subject matching**: ΔFPR=0 guarantee 的条件和限制。k≤5 限制在实践中的合理性。matching variable contamination 在多域污染场景下的表现。
5. **控制实验充分性**: random split、ability-quintile、nearest-neighbor matching、composition control 是否完全排除了混淆因素？base/instruct composition shift (11.8pp gap) 的 residual confound。
6. **Local independence**: Yen's Q3 显示 11.3% item pairs 存在局部依赖，permutation simulation 的 FPR 膨胀估计 (<0.001pp) 是否可信？
7. **Multiple testing**: 论文声称 ETS C 的双重阈值提供了隐式控制，BH-FDR 仅移除 3/3,918 items。这个论证在 N=5,227 的超大样本下是否成立？

请按 ARR 标准输出完整审稿报告，包含 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Must-Fix / Should-Fix / Minor）、Questions、Missing References。最后给出 Overall Assessment 评分（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）和置信度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1164 · 2026-05-23T10:19:27.876445+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1165 · 2026-05-23T10:19:27.927051+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1166 · 2026-05-23T10:19:37.473229+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1167 · 2026-05-23T10:19:40.096443+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1168 · 2026-05-23T10:19:44.927973+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what I found:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consid
…[truncated 1277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7454
}
```

</details>

---


### Tool result

_source line 1169 · 2026-05-23T10:19:47.139865+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 584.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p9.png\", \"width\": 1
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7043
}
```

</details>

---


### Tool call

_source line 1170 · 2026-05-23T10:19:53.062208+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, all scoring dimensions and their scales, and any specific instructions for reviewers. Include all numbered fields, their descriptions, and rating scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, all scoring dimensions and their scales, and any specific instructions for reviewers. Include all numbered fields, their descriptions, and rating scales."
  }
}
```

</details>

---


### Tool call

_source line 1171 · 2026-05-23T10:19:54.219042+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1172 · 2026-05-23T10:19:54.673972+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1173 · 2026-05-23T10:19:55.479135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1174 · 2026-05-23T10:19:56.036345+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1817
}
```

</details>

---


### Tool call

_source line 1175 · 2026-05-23T10:19:56.036808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1176 · 2026-05-23T10:19:56.746327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1177 · 2026-05-23T10:19:56.797679+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2123
}
```

</details>

---


### Tool result

_source line 1178 · 2026-05-23T10:19:58.208976+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2729
}
```

</details>

---


### Tool result

_source line 1179 · 2026-05-23T10:19:58.513209+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2476
}
```

</details>

---


### Tool result

_source line 1180 · 2026-05-23T10:19:58.671406+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1925
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-23T10:20:02.947589+00:00_

# ACL Rolling Review Form: Complete Criteria and Scales

## Core Review Dimensions

**1. Paper Summary**
Reviewers describe paper content to highlight potential misunderstandings.

**2. Summary of Strengths**
Identify major publication reasons, including "novel and useful methodology, insightful empirical results or theoretical analysis."

**3. Summary of Weaknesses**
List numbered concerns about correctness, impact, clarity, or other factors affecting publication priority.

**4. Comments/Suggestions/Typos**
Additional improvement recommendations beyond addressing main concerns.

## Quantitative Rating Scales

**Reviewer Confidence** (1-5)
- 5 = Positive evaluation is correct; very careful reading
- 4 = Quite sure; important points checked carefully
- 3 = Pretty sure; general familiarity but details not thoroughly verified
- 2 = Willing to defend evaluation; likely missed some details
- 1 = Outside expertise area or paper very difficult to understand

**Soundness** (1-5, with half-point increments)
- 5 = "one of the most thorough I have seen, given its type"
- 4 = Strong; sufficient support with minor experiments optional
- 3 = Acceptable; supports main claims with minor gaps
- 2 = Poor; main claims insufficiently supported
- 1 = Major issues; not sufficiently thorough for publication

**Excitement** (1-5, with half-point increments)
- 5 = Highly exciting; recommend to others
- 4 = Exciting; mention to colleagues
- 3 = Interesting; might mention or attend presentation
- 2 = Potentially interesting to some community members
- 1 = Not exciting; irrelevant to computational linguistics

**Overall Assessment** (1-5, with half-point increments)
- 5 = Consider for award (top 2.5% papers)
- 4.5 = Borderline award
- 4 = Conference acceptance
- 3.5 = Borderline conference
- 3 = Findings acceptance
- 2.5 = Borderline findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

## Additional Evaluation Dimensions

**Limitations and Societal Impact
…[truncated 1240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9885
}
```

</details>

---


### Tool call

_source line 1182 · 2026-05-23T10:20:11.895925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1183 · 2026-05-23T10:20:12.701391+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 1184 · 2026-05-23T10:20:12.852643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1185 · 2026-05-23T10:20:13.207493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1186 · 2026-05-23T10:20:14.272414+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1419
}
```

</details>

---


### Tool result

_source line 1187 · 2026-05-23T10:20:14.375471+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1167
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-23T10:20:14.375963+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1189 · 2026-05-23T10:20:14.427917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1190 · 2026-05-23T10:20:15.486540+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-23T10:20:15.537928+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-23T10:20:22.475864+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-23T10:20:24.182108+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 583.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.2}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 420.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.8}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 337.3}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/art
…[truncated 75 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1706
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-23T10:20:37.490987+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-23T10:20:38.095420+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 1196 · 2026-05-23T10:20:38.146124+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1197 · 2026-05-23T10:20:38.900668+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-23T10:20:38.901197+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1199 · 2026-05-23T10:20:39.403615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1200 · 2026-05-23T10:20:39.856626+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1201 · 2026-05-23T10:20:39.857104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1202 · 2026-05-23T10:20:40.764570+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1360
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-23T10:20:40.765691+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-23T10:20:40.768198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-23T10:20:41.224963+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 1206 · 2026-05-23T10:20:41.225453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 1207 · 2026-05-23T10:20:41.777824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1208 · 2026-05-23T10:20:41.980204+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool result

_source line 1209 · 2026-05-23T10:20:42.182788+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-23T10:25:46.151613+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what reviewers should focus on, what constitutes a good review, how to assess papers, and any specific dos and don'ts. Include guidance on soundness, novelty, clarity, and significance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines: what reviewers should focus on, what constitutes a good review, how to assess papers, and any specific dos and don'ts. Include guidance on soundness, novelty, clarity, and significance."
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-23T10:25:55.088519+00:00_

# ARR Reviewer Guidelines: Key Focus Areas

## Core Reviewing Principles

**Read Strategically**: Reviewers should read papers twice—first for understanding the research question and methodology, then in-depth for technical evaluation. This prevents hindsight bias and confirmation bias from tainting initial assessments.

**Be Specific and Justified**: Generic criticisms undermine review quality. Rather than stating "X is unclear," identify precisely what information is missing. All scores must be supported by explicit evidence in the review text.

**Maintain Professional Tone**: Reviews should be collegial and constructive. The guidelines note that "Write the review you would like to get yourself," emphasizing that dismissive or sarcastic language damages the peer review ecosystem.

## What Makes a Strong Review

**Soundness Assessment**:
- Verify technical correctness and validity of arguments
- Check methodology appropriateness for stated claims
- Evaluate whether evidence actually supports conclusions
- Assess reproducibility details and experimental design

**Novelty and Contribution**:
- Determine if work advances knowledge rather than repeating known results
- Require specific citations when claiming lack of novelty (3+ months prior publication)
- Recognize that various contribution types—resources, analyses, reproductions—deserve fair evaluation

**Clarity and Presentation**:
- Ensure research questions are clearly articulated
- Verify that key details appear in main text, not just appendices
- Check for hallucinated references and citation accuracy

## Critical Dos and Don'ts

**Avoid These Common Reviewer Mistakes**:
- Treating negative results as weaknesses (they provide valuable knowledge)
- Dismissing work for methodological simplicity (simpler solutions are preferable)
- Requiring comparisons to closed-source models unless directly relevant to claims
- Listing acknowledged limitations as rejection reasons
- Expecting experiments beyond what claims requi
…[truncated 927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8936
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-23T10:28:22.225173+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿报告\n\n**论文**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**审查侧重**: 方法严谨性 + 统计有效性\n**Venue**: EMNLP 2026 (via ARR)\n\n---\n\n## Paper Summary\n\n本文将教育测量中成熟的 Mantel-Haenszel 差异项目功能分析 (MH-DIF) 迁移至 LLM benchmark 评估领域，基于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items）审计 2023 与 2024 模型队列间的分数可比性。核心发现：17.9–31.5% 的 items 在 ETS Category C 阈值（|Δ_MH| ≥ 1.5）下展现 temporal DIF。论文提出三项方法学适配：(a) cross-subject matching 防止 contamination 污染 matching variable；(b) DEFF 校正处理模型家族内非独立性；(c) semi-synthetic injection 验证框架。主要结论：DIF flags 与 global exposure labels 近似独立（Jaccard ≈ 0.206），DIF-corrected scores 平均偏移 ±2.12pp，raw benchmark scores 跨时间队列不可直接比较。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 方法论框架扎实、实证规模空前，但 ETS 阈值从人类考试直接移植到 LLM 缺乏领域内标定、DEFF 两种估计量 2 倍差距削弱了定量结论的精度，综合来看是一篇有实质贡献但关键校准环节需要补强的工作。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 方法论框架从教育测量迁移整体合理，5 种 cohort 设计提供三角验证，但 ETS 阈值缺乏 LLM 领域特定标定，DEFF 估计量不确定性大，multiple testing 论证在超大样本下有循环论证问题 |\n| Excitement | 3.5 / 5 | 重要且及时的问题——benchmark 分数跨时间可比性直接影响社区对模型进步的理解；cross-subject matching 是真正的方法学贡献；但 \"分数不可比\" 这一定性结论对实践者而言可能并不意外 |\n| Reproducibility | 4 / 5 | 代码可用，数据公开（METABENCH），方法描述详尽含参数（K=5 strata、ETS 阈值、bootstrap 细节）；Appendix 覆盖了绝大多数实现细节 |\n| Overall Assessment | 3.5 / 5 | Borderline Conference——定性发现稳健、方法学有贡献，但定量精度（阈值校准、DEFF 不确定性）需加强方可达到 Conference 水准 |\n\n**Reviewer Confidence**: 4 / 5（统计方法论和心理测量领域有充分经验，仔细阅读了全文含全部 Appendix）\n\n---\n\n## Strengths\n\n**S1. 重要且及时的研究问题。** LLM benchmark 分数跨时间可比性是社区追踪模型进步的基础假设。本文以实证而非轶事方式证明 ~27–29% 的 items 存在 temporal DIF，直接影响 leaderboard 解读。这不是 \"contamination detection\"——而是一个更根本的 measurement invariance 问题。\n\n**S2. 原则性的方法论框架。** MH-DIF 是教育测量中最成熟的 DIF 检测方法之一，其非参数特性（仅需二值响应和分组标签，无需模型内部信息）恰好适配 LLM 评估场景。方法选择有充分理论依据，不是简单的工具套用。\n\n**S3. 空前的实证规模与系统性控制。** 5,227 模型 × 12,508 items 是目前同类研究中最大规模的审计。五种 cohort 设计（temporal, ability-quintile, within-family, within-subject, random split）提供了真正的三角验证。Random split 基线 C% = 0.18%（Section 4.1）确认方法在零假设下几乎无 false positive，为后续结论提供了坚实的参照基准。\n\n**S4. Cross-subject matching 是实质性的方法学贡献。** 单域 contamination 下 ΔFPR = 0 的理论保证（Section 3.4）推导清晰且正确：将被测 subject 排除出 matching variable，从构造上阻断了 contamination 信号泄漏。这解决了将 DIF 应用于 LLM benchmark 时一个真实且此前未被解决的方法学难题。实证验证（Table 7）也支持这一保证在小 k 下成立。\n\n**S5. 对估计量不确定性的透明度。** 论文诚实报告了 simple-mean DEFF（29.2%）与 weighted-mean DEFF（13.5%）之间 ~2.2× 的差距（Section 4.2），而非 cherry-pick 一个。Appendix I 的 simulation study 为偏好 simple-mean 提供了有原则的依据，同时承认不确定性。\n\n**S6. 实用价值。** Section 5.2 提供了具体可操作的审计协议（MH-DIF pre-screening, N ≥ 500, cross-subject matching, k ≤ 5 阈值），直接可被 benchmark 维护者采用。\n\n**S7. 跨 benchmark 复制。** 分析扩展到全部 6 个 METABENCH benchmarks（Table 3）并在 GSM8K 上复制（Section 4.7），增强了泛化性声称。所有 6 个 benchmark 的 C% 均高于随机基线（Table 3 shows 20.7%–48.4%），定性结论一致。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1 [critical] ETS 阈值从人类考试直接移植到 LLM 缺乏领域内校准**\n- 具体位置：Section 3.2, Appendix A.2\n- 问题：论文直接采用 ETS Category C 阈值（|Δ_MH| ≥ 1.5）并引用其在教育测试中的标准地位。然而在教育场景中，DIF 率通常为 5–15%（Clauser and Mazor, 1998）；本文发现 17.9–31.5%，高出 2–6 倍。这一显著差异可能意味着：(a) LLM benchmark 确实存在严重的 measurement instability，或 (b) 该阈值对 LLM 领域过于宽松，因为 LLM 的 item-response 模式与人类考生在结构上不同。\n  \n  Appendix A.2 的阈值敏感性分析（|Δ_MH| ∈ {1.0, 1.5, 2.0, 2.5}）显示定性稳健性，这有帮助。但论文始终未建立：在 LLM 评估中，|Δ_MH| = 1.5 对应的 odds ratio (~2.7:1) 是否构成\"实质性显著\"的 measurement difference。当\"考生\"是 LLM 而非人类学生时，同一 effect size 可能有完全不同的实际含义。\n\n- 为什么影响接收：论文的核心量化声称（\"17.9–31.5% items exhibit temporal DIF\"）完全依赖于这个阈值。如果阈值不恰当，所有下游分析（DEFF 校正、cross-benchmark 比较、审计协议建议）的数值精度都受影响。\n- 建议修改方向：提供 LLM 领域内的实证锚定——例如，展示 |Δ_MH| ≥ 1.5 的 items 与 |Δ_MH| < 1.5 的 items 在模型排名上产生显著不同的结果（rank displacement analysis）。或者，使用数据驱动方法（如 random split 下 |Δ_MH| 分布的 95th percentile）建立 LLM-specific threshold，与 ETS 1.5 比较。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] DEFF 校正的 2× 不确定性削弱了 headline 定量精度**\n- 具体位置：Section 4.2, Appendix I\n- 问题：Simple-mean DEFF（29.2%，cluster bootstrap CI 26.7%）与 weighted-mean DEFF（13.5%）相差 ~2.2 倍。论文通过 Appendix I 的 simulation 论证了 simple-mean 的偏好，但该 simulation 仅测试了 4 种特定的 family-structure 场景，且 simple-mean 的优势依赖于 ICC 与 family size 的负相关关系——这一经验关系可能随 benchmark 和时间变化。\n  \n  论文 headline claim \"17.9–31.5% of items exhibit temporal DIF\" 横跨了这个范围。读者无法区分 \"~18% items have DIF\" 和 \"~31% items have DIF\"——二者的实践含义差异巨大。\n\n- 建议：(1) 在 abstract 和 introduction 中更突出地报告校正后范围，而非仅在 Section 4.2 讨论；(2) 给出在什么条件下（family 数量、size 分布、ICC 范围）应使用哪种估计量的指导；(3) 考虑报告一个 conservative \"robust\" 估计，如两种估计量的区间并集。\n\n**W2 [warning] Multiple testing 论证在超大样本下存在循环逻辑**\n- 具体位置：Section 3.2, Appendix A\n- 问题：论文声称 ETS C 的双重阈值（|Δ_MH| ≥ 1.5 AND p < 0.05）提供了\"隐式\"多重检验控制，并以 BH-FDR 仅移除 3/3,918 items 为证。但论文自身承认：\"At N ≥ 5,227, significance (p ≈ 0.03) is nearly automatically satisfied for any |Δ_MH| ≥ 1.5\"（Section 3.2）。这意味着：\n  (a) p-value 阈值是空洞的——它从不 bind；\n  (b) 分类完全由 effect size 决定；\n  (c) 对本身已极小的 p-values 施加 BH-FDR 自然几乎无变化。\n  \n  论证是循环的：展示一个校正在未校正值已极端时没有效果，不能证明分类是良好校准的。\n\n- 建议：明确承认在此 N 下分类本质上是纯 effect-size 准则，并在实质性而非统计性基础上论证 effect-size 阈值的合理性（与 N1 建议联动）。\n\n**W3 [warning] Semi-synthetic validation 使用 stylized injection 可能高估检测能力**\n- 具体位置：Section 3.4, Figure 2, Appendix G\n- 问题：主要验证（Section 3.4）使用 uniform binary flipping：选择 ETS A items 并以均匀概率 p 将 incorrect 翻转为 correct。这是检测的\"最佳情况\"——真实 contamination 产生渐变的、difficulty-dependent 的、部分的效应。\n  \n  Appendix G 的 difficulty-dependent injection 部分缓解了这一顾虑，但揭示了一个重要缺口：injection 无法匹配 instruct 模型观察到的 near-zero direction-reversal pattern（残差 gap 13×）。论文将此解读为 \"instruct-model DIF 至少部分由非 contamination 机制驱动\"——这是合理的解读，但同时意味着 semi-synthetic 框架无法完整复制真实 DIF 模式。\n\n- 建议：在 main text 中更明确地说明 ΔTPR 应被解读为检测能力的 upper bound 而非 point estimate。考虑增加更具挑战性的 injection scheme（如 graded injection with noise, model-capability-dependent injection rates）以测试 robustness。\n\n**W4 [warning] Base/instruct composition confound 未完全排除**\n- 具体位置：Section 5.1, Appendix O, Appendix P\n- 问题：论文报告 11.8pp 的 composition gap。Appendix O 显示 base 和 instruct 模型各自独立展现 DIF（Table 15），但方向分布差异大（base: 61.1% reference-favoring, ρ = −0.528; instruct: 65.6% focal-favoring, ρ = −0.079）。这意味着 temporal DIF profile 是两种不同模式的加权混合，且混合权重在队列间发生了偏移。虽然各子群 DIF 幅度可能持续，但聚合 C% 仍可能被 composition shift 部分膨胀。\n  \n  Section C（Appendix）的 composition control 显示仅 −1.0pp 的 residual shift，令人安心但基于有限协变量的 matching。\n\n- 建议：报告 composition-matched temporal C%（在 base/instruct 比例对齐后的 DIF 率），并讨论 residual confounding 的 magnitude bound。\n\n---\n\n## 小问题（不影响接收）\n\n**M1.** Local dependence 影响可能被低估。Yen's Q3 显示 11.3% within-subject item pairs |Q3| > 0.20（Section A.1），但 permutation simulation 估计 FPR inflation < 0.001pp。这一估计在直觉上偏低：虽然 permutation test 在零假设（无 DIF）下有效，但在备择假设下（真实 DIF 存在），LD 可能导致 subject 内 DIF 信号相关，使表面独立的 DIF-flagged items 数量高估。建议报告 within-subject DIF clustering 程度或讨论有效独立 DIF 信号数。\n\n**M2.** Cross-benchmark 分析较薄。Table 3 报告了 6 个 benchmarks 的 C% 和相关性，但缺少深度分析——例如，是否同一 model families 在所有 benchmarks 上驱动 DIF？Item-level DIF profiles 是否跨 benchmark 相关？\n\n**M3.** GSM8K 复制（Section 4.7）描述过于简略。应报告使用了多少 items/models，以及 GSM8K 的 DIF 模式与 MMLU 的异同。\n\n**M4.** 论文在 Section 3.2 提到 \"At N ≥ 5,227\"，但 temporal comparison 实际使用 N_ref = 1,080, N_focal = 807（Section 3.3），总计 1,887 而非 5,227。应澄清 MH test 中使用的有效 N。\n\n**M5.** Figure 1 的 \"left\" vs \"right\" 两个子图区分需要更清晰的标注——当前 caption 中\"Left: global contamination produces no DIF\" 和 \"Right: differential contamination produces DIF\" 在小字体下不够醒目。\n\n---\n\n## Questions for Authors\n\n**Q1.** 能否提供证据表明 |Δ_MH| = 1.5 在 LLM 场景下产生有意义的不同的模型排名？例如，仅移除 |Δ_MH| ≥ 1.5 items vs. |Δ_MH| ≥ 1.0 或 ≥ 2.0 后，平均 rank displacement 分别是多少？\n\n**Q2.** DEFF simulation（Appendix I）假设了特定的 ICC-family-size 关系。如果 within-family ICC 在不同 family size 间大致恒定（而非负相关），simple-mean 的偏好是否仍然成立？\n\n**Q3.** Permutation simulation 报告 LD 导致 FPR inflation < 0.001pp。运行了多少 permutations？该估计的 standard error 是多少？鉴于 11.3% item pairs 显示 |Q3| > 0.20，能否提供直觉解释为何 FPR 影响如此之小？\n\n**Q4.** Difficulty-direction interaction（Appendix B）显示显著的 difficulty × model-type interaction（t = 1.56, OR = 4.75, p < 10⁻⁸）。仅此 interaction 能解释多大比例的 observed temporal DIF？是否存在这样的可能：difficulty-dependent capability improvements（无需任何 contamination）即可产生类似幅度的 DIF？\n\n**Q5.** K=5 strata 的选择依据 ETS 推荐实践。是否测试了 K=3 或 K=10 对 DIF 检测率的影响？Appendix J 提到了 K=3 和 K=5 的比较，但 main text 中未讨论。\n\n---\n\n## Missing References\n\n- Martinková, P., & Drabinová, A. (2018). \"ShinyItemAnalysis for teaching psychometrics and to enforce routine analysis of educational tests.\" *The R Journal* — 提供了替代 DIF 检测工具，与本文方法可作比较。\n- Chalmers, R.P. (2012). \"mirt: A multidimensional item response theory package for the R environment.\" *Journal of Statistical Software* — 论文提到 multidimensionality 但未引用主要 MIRT 软件/方法论文献。\n- 论文引用了 Polo et al. (2024) tinyBenchmarks，但可进一步讨论 IRT-based benchmark compression 与 DIF-aware item selection 的关系。\n\n---\n\n## 总结\n\n本文在一个重要问题上做出了实质性贡献：通过大规模心理测量审计揭示 LLM benchmark 分数的 temporal incomparability。方法论框架从教育测量迁移整体合理，cross-subject matching 是真正的创新，实证规模空前。主要不足集中在校准层面：ETS 阈值的 LLM 适用性缺乏领域内验证（N1），DEFF 校正的不确定性范围过大（W1），multiple testing 论证在大样本下需要重新框定（W2）。这些问题影响定量精度但不动摇定性结论（temporal DIF 以非平凡比例存在）。如果作者能补充 threshold 的 LLM-specific 校准，论文可上升到 Conference 水平。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿报告\n\n**论文**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**审查侧重**: 方法严谨性 + 统计有效性\n**Venue**: EMNLP 2026 (via ARR)\n\n---\n\n## Paper Summary\n\n本文将教育测量中成熟的 Mantel-Haenszel 差异项目功能分析 (MH-DIF) 迁移至 LLM benchmark 评估领域，基于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items）审计 2023 与 2024 模型队列间的分数可比性。核心发现：17.9–31.5% 的 items 在 ETS Category C 阈值（|Δ_MH| ≥ 1.5）下展现 temporal DIF。论文提出三项方法学适配：(a) cross-subject matching 防止 contamination 污染 matching variable；(b) DEFF 校正处理模型家族内非独立性；(c) semi-synthetic injection 验证框架。主要结论：DIF flags 与 global exposure labels 近似独立（Jaccard ≈ 0.206），DIF-corrected scores 平均偏移 ±2.12pp，raw benchmark scores 跨时间队列不可直接比较。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 方法论框架扎实、实证规模空前，但 ETS 阈值从人类考试直接移植到 LLM 缺乏领域内标定、DEFF 两种估计量 2 倍差距削弱了定量结论的精度，综合来看是一篇有实质贡献但关键校准环节需要补强的工作。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 方法论框架从教育测量迁移整体合理，5 种 cohort 设计提供三角验证，但 ETS 阈值缺乏 LLM 领域特定标定，DEFF 估计量不确定性大，multiple testing 论证在超大样本下有循环论证问题 |\n| Excitement | 3.5 / 5 | 重要且及时的问题——benchmark 分数跨时间可比性直接影响社区对模型进步的理解；cross-subject matching 是真正的方法学贡献；但 \"分数不可比\" 这一定性结论对实践者而言可能并不意外 |\n| Reproducibility | 4 / 5 | 代码可用，数据公开（METABENCH），方法描述详尽含参数（K=5 strata、ETS 阈值、bootstrap 细节）；Appendix 覆盖了绝大多数实现细节 |\n| Overall Assessment | 3.5 / 5 | Borderline Conference——定性发现稳健、方法学有贡献，但定量精度（阈值校准、DEFF 不确定性）需加强方可达到 Conference 水准 |\n\n**Reviewer Confidence**: 4 / 5（统计方法论和心理测量领域有充分经验，仔细阅读了全文含全部 Appendix）\n\n---\n\n## Strengths\n\n**S1. 重要且及时的研究问题。** LLM benchmark 分数跨时间可比性是社区追踪模型进步的基础假设。本文以实证而非轶事方式证明 ~27–29% 的 items 存在 temporal DIF，直接影响 leaderboard 解读。这不是 \"contamination detection\"——而是一个更根本的 measurement invariance 问题。\n\n**S2. 原则性的方法论框架。** MH-DIF 是教育测量中最成熟的 DIF 检测方法之一，其非参数特性（仅需二值响应和分组标签，无需模型内部信息）恰好适配 LLM 评估场景。方法选择有充分理论依据，不是简单的工具套用。\n\n**S3. 空前的实证规模与系统性控制。** 5,227 模型 × 12,508 items 是目前同类研究中最大规模的审计。五种 cohort 设计（temporal, ability-quintile, within-family, within-subject, random split）提供了真正的三角验证。Random split 基线 C% = 0.18%（Section 4.1）确认方法在零假设下几乎无 false positive，为后续结论提供了坚实的参照基准。\n\n**S4. Cross-subject matching 是实质性的方法学贡献。** 单域 contamination 下 ΔFPR = 0 的理论保证（Section 3.4）推导清晰且正确：将被测 subject 排除出 matching variable，从构造上阻断了 contamination 信号泄漏。这解决了将 DIF 应用于 LLM benchmark 时一个真实且此前未被解决的方法学难题。实证验证（Table 7）也支持这一保证在小 k 下成立。\n\n**S5. 对估计量不确定性的透明度。** 论文诚实报告了 simple-mean DEFF（29.2%）与 weighted-mean DEFF（13.5%）之间 ~2.2× 的差距（Section 4.2），而非 cherry-pick 一个。Appendix I 的 simulation study 为偏好 simple-mean 提供了有原则的依据，同时承认不确定性。\n\n**S6. 实用价值。** Section 5.2 提供了具体可操作的审计协议（MH-DIF pre-screening, N ≥ 500, cross-subject matching, k ≤ 5 阈值），直接可被 benchmark 维护者采用。\n\n**S7. 跨 benchmark 复制。** 分析扩展到全部 6 个 METABENCH benchmarks（Table 3）并在 GSM8K 上复制（Section 4.7），增强了泛化性声称。所有 6 个 benchmark 的 C% 均高于随机基线（Table 3 shows 20.7%–48.4%），定性结论一致。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1 [critical] ETS 阈值从人类考试直接移植到 LLM 缺乏领域内校准**\n- 具体位置：Section 3.2, Appendix A.2\n- 问题：论文直接采用 ETS Category C 阈值（|Δ_MH| ≥ 1.5）并引用其在教育测试中的标准地位。然而在教育场景中，DIF 率通常为 5–15%（Clauser and Mazor, 1998）；本文发现 17.9–31.5%，高出 2–6 倍。这一显著差异可能意味着：(a) LLM benchmark 确实存在严重的 measurement instability，或 (b) 该阈值对 LLM 领域过于宽松，因为 LLM 的 item-response 模式与人类考生在结构上不同。\n  \n  Appendix A.2 的阈值敏感性分析（|Δ_MH| ∈ {1.0, 1.5, 2.0, 2.5}）显示定性稳健性，这有帮助。但论文始终未建立：在 LLM 评估中，|Δ_MH| = 1.5 对应的 odds ratio (~2.7:1) 是否构成\"实质性显著\"的 measurement difference。当\"考生\"是 LLM 而非人类学生时，同一 effect size 可能有完全不同的实际含义。\n\n- 为什么影响接收：论文的核心量化声称（\"17.9–31.5% items exhibit temporal DIF\"）完全依赖于这个阈值。如果阈值不恰当，所有下游分析（DEFF 校正、cross-benchmark 比较、审计协议建议）的数值精度都受影响。\n- 建议修改方向：提供 LLM 领域内的实证锚定——例如，展示 |Δ_MH| ≥ 1.5 的 items 与 |Δ_MH| < 1.5 的 items 在模型排名上产生显著不同的结果（rank displacement analysis）。或者，使用数据驱动方法（如 random split 下 |Δ_MH| 分布的 95th percentile）建立 LLM-specific threshold，与 ETS 1.5 比较。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] DEFF 校正的 2× 不确定性削弱了 headline 定量精度**\n- 具体位置：Section 4.2, Appendix I\n- 问题：Simple-mean DEFF（29.2%，cluster bootstrap CI 26.7%）与 weighted-mean DEFF（13.5%）相差 ~2.2 倍。论文通过 Appendix I 的 simulation 论证了 simple-mean 的偏好，但该 simulation 仅测试了 4 种特定的 family-structure 场景，且 simple-mean 的优势依赖于 ICC 与 family size 的负相关关系——这一经验关系可能随 benchmark 和时间变化。\n  \n  论文 headline claim \"17.9–31.5% of items exhibit temporal DIF\" 横跨了这个范围。读者无法区分 \"~18% items have DIF\" 和 \"~31% items have DIF\"——二者的实践含义差异巨大。\n\n- 建议：(1) 在 abstract 和 introduction 中更突出地报告校正后范围，而非仅在 Section 4.2 讨论；(2) 给出在什么条件下（family 数量、size 分布、ICC 范围）应使用哪种估计量的指导；(3) 考虑报告一个 conservative \"robust\" 估计，如两种估计量的区间并集。\n\n**W2 [warning] Multiple testing 论证在超大样本下存在循环逻辑**\n- 具体位置：Section 3.2, Appendix A\n- 问题：论文声称 ETS C 的双重阈值（|Δ_MH| ≥ 1.5 AND p < 0.05）提供了\"隐式\"多重检验控制，并以 BH-FDR 仅移除 3/3,918 items 为证。但论文自身承认：\"At N ≥ 5,227, significance (p ≈ 0.03) is nearly automatically satisfied for any |Δ_MH| ≥ 1.5\"（Section 3.2）。这意味着：\n  (a) p-value 阈值是空洞的——它从不 bind；\n  (b) 分类完全由 effect size 决定；\n  (c) 对本身已极小的 p-values 施加 BH-FDR 自然几乎无变化。\n  \n  论证是循环的：展示一个校正在未校正值已极端时没有效果，不能证明分类是良好校准的。\n\n- 建议：明确承认在此 N 下分类本质上是纯 effect-size 准则，并在实质性而非统计性基础上论证 effect-size 阈值的合理性（与 N1 建议联动）。\n\n**W3 [warning] Semi-synthetic validation 使用 stylized injection 可能高估检测能力**\n- 具体位置：Section 3.4, Figure 2, Appendix G\n- 问题：主要验证（Section 3.4）使用 uniform binary flipping：选择 ETS A items 并以均匀概率 p 将 incorrect 翻转为 correct。这是检测的\"最佳情况\"——真实 contamination 产生渐变的、difficulty-dependent 的、部分的效应。\n  \n  Appendix G 的 difficulty-dependent injection 部分缓解了这一顾虑，但揭示了一个重要缺口：injection 无法匹配 instruct 模型观察到的 near-zero direction-reversal pattern（残差 gap 13×）。论文将此解读为 \"instruct-model DIF 至少部分由非 contamination 机制驱动\"——这是合理的解读，但同时意味着 semi-synthetic 框架无法完整复制真实 DIF 模式。\n\n- 建议：在 main text 中更明确地说明 ΔTPR 应被解读为检测能力的 upper bound 而非 point estimate。考虑增加更具挑战性的 injection scheme（如 graded injection with noise, model-capability-dependent injection rates）以测试 robustness。\n\n**W4 [warning] Base/instruct composition confound 未完全排除**\n- 具体位置：Section 5.1, Appendix O, Appendix P\n- 问题：论文报告 11.8pp 的 composition gap。Appendix O 显示 base 和 instruct 模型各自独立展现 DIF（Table 15），但方向分布差异大（base: 61.1% reference-favoring, ρ = −0.528; instruct: 65.6% focal-favoring, ρ = −0.079）。这意味着 temporal DIF profile 是两种不同模式的加权混合，且混合权重在队列间发生了偏移。虽然各子群 DIF 幅度可能持续，但聚合 C% 仍可能被 composition shift 部分膨胀。\n  \n  Section C（Appendix）的 composition control 显示仅 −1.0pp 的 residual shift，令人安心但基于有限协变量的 matching。\n\n- 建议：报告 composition-matched temporal C%（在 base/instruct 比例对齐后的 DIF 率），并讨论 residual confounding 的 magnitude bound。\n\n---\n\n## 小问题（不影响接收）\n\n**M1.** Local dependence 影响可能被低估。Yen's Q3 显示 11.3% within-subject item pairs |Q3| > 0.20（Section A.1），但 permutation simulation 估计 FPR inflation < 0.001pp。这一估计在直觉上偏低：虽然 permutation test 在零假设（无 DIF）下有效，但在备择假设下（真实 DIF 存在），LD 可能导致 subject 内 DIF 信号相关，使表面独立的 DIF-flagged items 数量高估。建议报告 within-subject DIF clustering 程度或讨论有效独立 DIF 信号数。\n\n**M2.** Cross-benchmark 分析较薄。Table 3 报告了 6 个 benchmarks 的 C% 和相关性，但缺少深度分析——例如，是否同一 model families 在所有 benchmarks 上驱动 DIF？Item-level DIF profiles 是否跨 benchmark 相关？\n\n**M3.** GSM8K 复制（Section 4.7）描述过于简略。应报告使用了多少 items/models，以及 GSM8K 的 DIF 模式与 MMLU 的异同。\n\n**M4.** 论文在 Section 3.2 提到 \"At N ≥ 5,227\"，但 temporal comparison 实际使用 N_ref = 1,080, N_focal = 807（Section 3.3），总计 1,887 而非 5,227。应澄清 MH test 中使用的有效 N。\n\n**M5.** Figure 1 的 \"left\" vs \"right\" 两个子图区分需要更清晰的标注——当前 caption 中\"Left: global contamination produces no DIF\" 和 \"Right: differential contamination produces DIF\" 在小字体下不够醒目。\n\n---\n\n## Questions for Authors\n\n**Q1.** 能否提供证据表明 |Δ_MH| = 1.5 在 LLM 场景下产生有意义的不同的模型排名？例如，仅移除 |Δ_MH| ≥ 1.5 items vs. |Δ_MH| ≥ 1.0 或 ≥ 2.0 后，平均 rank displacement 分别是多少？\n\n**Q2.** DEFF simulation（Appendix I）假设了特定的 ICC-family-size 关系。如果 within-family ICC 在不同 family size 间大致恒定（而非负相关），simple-mean 的偏好是否仍然成立？\n\n**Q3.** Permutation simulation 报告 LD 导致 FPR inflation < 0.001pp。运行了多少 permutations？该估计的 standard error 是多少？鉴于 11.3% item pairs 显示 |Q3| > 0.20，能否提供直觉解释为何 FPR 影响如此之小？\n\n**Q4.** Difficulty-direction interaction（Appendix B）显示显著的 difficulty × model-type interaction（t = 1.56, OR = 4.75, p < 10⁻⁸）。仅此 interaction 能解释多大比例的 observed temporal DIF？是否存在这样的可能：difficulty-dependent capability improvements（无需任何 contamination）即可产生类似幅度的 DIF？\n\n**Q5.** K=5 strata 的选择依据 ETS 推荐实践。是否测试了 K=3 或 K=10 对 DIF 检测率的影响？Appendix J 提到了 K=3 和 K=5 的比较，但 main text 中未讨论。\n\n---\n\n## Missing References\n\n- Martinková, P., & Drabinová, A. (2018). \"ShinyItemAnalysis for teaching psychometrics and to enforce routine analysis of educational tests.\" *The R Journal* — 提供了替代 DIF 检测工具，与本文方法可作比较。\n- Chalmers, R.P. (2012). \"mirt: A multidimensional item response theory package for the R environment.\" *Journal of Statistical Software* — 论文提到 multidimensionality 但未引用主要 MIRT 软件/方法论文献。\n- 论文引用了 Polo et al. (2024) tinyBenchmarks，但可进一步讨论 IRT-based benchmark compression 与 DIF-aware item selection 的关系。\n\n---\n\n## 总结\n\n本文在一个重要问题上做出了实质性贡献：通过大规模心理测量审计揭示 LLM benchmark 分数的 temporal incomparability。方法论框架从教育测量迁移整体合理，cross-subject matching 是真正的创新，实证规模空前。主要不足集中在校准层面：ETS 阈值的 LLM 适用性缺乏领域内验证（N1），DEFF 校正的不确定性范围过大（W1），multiple testing 论证在大样本下需要重新框定（W2）。这些问题影响定量精度但不动摇定性结论（temporal DIF 以非平凡比例存在）。如果作者能补充 threshold 的 LLM-specific 校准，论文可上升到 Conference 水平。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1213 · 2026-05-23T10:28:26.210225+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3985
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-23T10:28:35.507533+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-23T10:28:35.658960+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1216 · 2026-05-23T10:28:40.529257+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-23T10:28:40.630233+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 1218 · 2026-05-23T10:28:55.586114+00:00_

Reviewer 1 审稿完成。

**评分**: Overall 3.5/5 (Borderline Conference), Soundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5, Confidence 4/5。

**核心判断**: 定性结论稳健（temporal DIF 以非平凡比例存在），方法学有实质贡献（cross-subject matching），但定量精度受三个关键校准问题制约：

1. **N1 [Must-Fix]**: ETS |Δ_MH| ≥ 1.5 阈值从人类考试直接移植到 LLM，缺乏领域内标定——教育测试 DIF 率 5–15%，本文 17.9–31.5%，差异 2–6×，未排除阈值过于宽松的可能
2. **W1–W4 [Should-Fix]**: DEFF 两种估计量差 2.2×（29.2% vs 13.5%）；multiple testing 论证在 N≈5,227 下本质循环；semi-synthetic validation 用最易检测的 uniform flipping；base/instruct composition confound 未完全排除
3. **M1–M5 [Minor]**: local dependence FPR inflation 估计 <0.001pp 偏低、cross-benchmark 分析较薄等

报告已通过 `review_reviewer_post_to_director` 提交至 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 42

## Round 42

20 recorded events


### User

_source line 1219 · 2026-05-23T10:29:08.562449+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿报告

**Overall**: 3.5 (Borderline Conference)

### Must-Fix

**N1** [critical] Contribution 1 的贡献度声称需要重新校准
- 全局暴露（global exposure）和差异功能（differential functioning）在定义上就是不同的构念。将其低相关性（Jaccard ≈ 0.206）提升为三大贡献之首存在过度声称风险。EMNLP reviewer 可能将此视为"在大规模数据上确认了显而易见的事实"。

**N2** [critical] Contribution 3 ("three methodological adaptations") 与 "We do not modify the core MH statistic" 之间的张力
- (a) Cross-subject matching 属于标准实践中的实施决策；(b) DEFF correction 直接借用自 survey methodology；(c) Semi-synthetic validation 是验证策略，不是方法论贡献。称之为 "methodological adaptations" 过度拉升了新颖性。

### Should-Fix

**W1** [warning] §5.2 审计协议中的机制推断超出方法能力
- DIF 本身是 mechanism-agnostic 的，但 §5.2 建议 "DIF on web-clean items suggests capability shift"——这是 ad hoc 推断。

**W2** [warning] Discussion 停留在结果层面，缺乏深层 insight
- §5.1 本质上是额外实验结果；§5.2 缺乏对 temporal DIF 成因和对 LLM 评测生态系统性影响的讨论。

**W3** [warning] Abstract 信息密度过高
- 单段内包含 15+ 个数值，影响可读性。

**W4** [warning] Limitations section 覆盖面偏窄
- 未讨论对 MMLU 式多选题以外基准的泛化性、模型发布日期与训练数据截止时间不对齐、Li et al. web-overlap 标签本身的局限性。

### Minor

**M1** 术语不一致: "temporal score incomparability" vs measurement non-invariance
**M2** `\enlargethispage*{4\baselineskip}` 潜在格式违规
**M3** ±2.12pp 偏移在排名差异置信区间内还是外？
**M4** Figure 1 右图 y 轴应标注条件概率

### Missing References
1. Adaptive Testing for LLM Evaluation (arxiv 2511.04689)
2. JE-IRT (arxiv 2509.22888)
3. Confident Rankings with Fewer Items (arxiv 2601.13885)
4. When Benchmarks Leak: Inference-Time Decontamination (arxiv 2601.19334)

### Questions
Q1. 不同学科的 DIF enrichment ratio 差异的驱动因素？
Q2. 更粗粒度定义 "family" 后 C% 如何变化？
Q3. 是否考虑过与题目难度相关的注入方案？
Q4. DIF-flagged items 是否应被排除出 Growing Pains 的 anchor sets？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1220 · 2026-05-23T10:30:01.778658+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-2,6-8,14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-2,6-8,14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1221 · 2026-05-23T10:30:02.833373+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.2}], \"total_pages\": 18, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-23T10:30:06.551670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-23T10:30:07.456601+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1224 · 2026-05-23T10:30:07.458982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1225 · 2026-05-23T10:30:07.960820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1226 · 2026-05-23T10:30:08.464163+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 1227 · 2026-05-23T10:30:08.464631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1228 · 2026-05-23T10:30:09.369224+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-23T10:30:09.371090+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1230 · 2026-05-23T10:30:09.372005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1231 · 2026-05-23T10:30:09.674245+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1232 · 2026-05-23T10:30:10.379323+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool result

_source line 1233 · 2026-05-23T10:30:10.583598+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-23T10:32:26.443151+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: Contribution 1（global exposure vs. DIF 独立性）的贡献度**\n\nR2 认为 global exposure 和 differential functioning\"定义上就是不同构念\"，因此低 Jaccard（≈ 0.206）只是在\"确认显而易见的事实\"。我不完全同意。\n\n**证据与理由：**\n1. 定义上不同 ≠ 经验上必然独立。contamination detection 文献的隐含假设恰恰是：global exposure（item 出现在训练数据中）会导致 differential functioning（模型在该 item 上表现异常）。MinK++ (Shi et al., 2024)、Time Travel (Golchin and Surdescu, 2024) 等方法正是基于这一假设运作的。如果二者真的\"显而易见地独立\"，这些方法的理论基础就需要重新审视。\n2. 论文提供了具体的定量证据：Jaccard ≈ 0.206, Enrichment ratio ≈ 1.0（Section 4.3, Figure 1），permutation null (Jaccard = 0.206, p = 0.88)。这不是重述定义，而是对一个被广泛默认成立的假设的实证否证。\n3. 同时，Abstract 明确指出 \"aggregate rankings are robust (ρ ≈ 0.997), but absolute scores are not directly comparable\"——即 global exposure 不影响排名但 DIF 影响绝对分数。这一区分在先前文献中没有被系统建立。\n\n**部分同意点：** 我同意将此作为\"三大贡献之首\"的位置可以商榷——它更适合作为背景性的 empirical observation 来激发后续方法学贡献，而非独立的 headline contribution。建议作者调整 Introduction 中三个 contribution 的排序和权重表述。\n\n---\n\n**[REBUT] R2-N2: \"Three methodological adaptations\" 的新颖性**\n\nR2 认为三项适配均不构成方法论贡献：(a) cross-subject matching 是\"实施决策\"，(b) DEFF 借用 survey methodology，(c) semi-synthetic validation 是验证策略。我对 (a) 强烈反驳，对 (b)(c) 部分同意。\n\n**对 (a) Cross-subject matching 的反驳：**\n- 这不是标准实施决策。教育测量中 MH-DIF 的标准做法是使用 within-test total score 作为 matching variable（Holland and Thayer, 1988; Donoghue and Allen, 1993）。论文的创新在于：当 matching variable 本身可能被 contamination 污染时（benchmark 的 total score 包含了被 contaminate 的 items），使用 cross-subject total score 排除被测 subject，从构造上保证 ΔFPR = 0（Section 3.4，含形式化推导）。\n- 这一保证是 formal result，不是 engineering choice。Section 3.4 给出了严格证明：single-subject injection 下，被测 subject 的 items 不进入 matching variable，因此注入不影响 matching，ΔFPR = 0 by construction。\n- Table 7（Section 4.5）的实证验证进一步支持：single-subject injection 下 ΔFPR = 0.000（所有 MMLU subjects），而 within-subject matching 下 ΔFPR 则显著膨胀（+0.186）。这不是\"显然的实施选择\"——它解决了将 DIF 应用到 contaminated benchmarks 时一个此前未被形式化的 matching variable corruption 问题。\n\n**对 (b) DEFF correction 的部分同意：**\n- R2 说得对，DEFF 概念源自 survey methodology（Kish, 1965）。但将其适配到 LLM model-family 结构需要非平凡的工作：计算 family-level ICC、处理 heterogeneous family sizes、在 Appendix I 中通过 simulation 比较 simple-mean vs. weighted-mean 估计量。称之为\"adaptation\"而非\"original contribution\"更准确。\n\n**对 (c) Semi-synthetic validation 的同意：**\n- 我同意 semi-synthetic injection 更接近 validation strategy 而非 methodological contribution。论文用 \"validation\" 一词本身是准确的，但将其列为三大\"methodological adaptations\"之一确实拉升了新颖性声称。\n\n**建议：** 论文可将 (a) cross-subject matching 单独突出为主要方法学贡献（含 formal guarantee），将 (b)(c) 降级为\"supporting methodological choices\"或\"complementary validation\"。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: §5.2 审计协议中的 mechanism inference**\n\nR2 指出\"DIF on web-clean items suggests capability shift\"超出了 DIF 方法的能力边界。我同意这一批评。\n\nDIF by design 是 mechanism-agnostic 的（论文自身在 Limitations 中承认这一点）。虽然 §5.2 使用了 \"suggests\" 而非 \"proves\" 的措辞，但在审计协议这种规范性建议中，即便是\"suggests\"也可能被误读为因果推断。\n\n**补充意见：** 论文可改为更保守的表述，如：\"DIF on web-clean items is inconsistent with contamination as the sole mechanism\"——这是 MH-DIF 结合 web-overlap labels 可以支持的排除性推理，不需要正面声称是\"capability shift\"。\n\n---\n\n**[AGREE] R2-W2: Discussion 缺乏深层 insight（部分同意）**\n\n§5.1 确实更像是附加的实验分析（base/instruct 分层、model family profiles、difficulty-direction interaction）而非对 temporal DIF 成因的深层讨论。我部分同意。\n\n**但有两点需要补充：**\n1. 论文的核心贡献是 empirical audit 而非 mechanistic explanation。在 8 页限制下，合理的选择是将 Discussion 聚焦在最直接可操作的内容（审计协议），而非对缺乏数据支撑的因果机制进行推测。\n2. §5.1 中 base/instruct 方向差异（base: 61.1% reference-favoring, ρ = −0.528; instruct: 65.6% focal-favoring, ρ = −0.079, Section 5.1/Appendix O）不仅是结果报告——它提供了 structured signal 的证据，表明 DIF 不是随机噪声而是与训练方法论相关的系统性模式。这超越了简单的结果重述。\n\n---\n\n**[AGREE] R2-W3: Abstract 信息密度过高**\n\n同意。15+ 个数值在单段 abstract 中确实影响可读性。这是可以在 revision 中轻松改善的表达问题。\n\n---\n\n**[REBUT] R2-W4: Limitations 覆盖面偏窄（部分反驳）**\n\nR2 认为应补充：(1) 对 MMLU 式 MCQ 以外基准的泛化性，(2) 模型发布日期与训练数据截止不对齐，(3) Li et al. web-overlap 标签自身局限性。\n\n**反驳理由：**\n1. 关于泛化性：论文在 Section 4.7 已在 GSM8K（数学问题，非传统 MCQ）上完成了 cross-benchmark 复制，且 Table 3 报告了 6 个 METABENCH benchmarks 的 DIF 率（20.7%–48.4%），涵盖了不同题型。Limitations 中不需要重复讨论已有实证覆盖的问题。\n2. 关于 web-overlap 标签局限性：论文的核心发现恰恰是 DIF flags 与 web-overlap labels 近似独立（Jaccard ≈ 0.206），因此 web-overlap labels 的局限性主要影响 Section 4.3 的 ground truth comparison，而不影响论文的主要 DIF 分析。\n\n**同意点：** 模型发布日期与训练数据截止不对齐是一个值得在 Limitations 中提及的有效关切——temporal cohort 按 release date 划分，但模型的训练数据可能跨越了这些边界。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1:** 术语一致性是合理的要求。\"temporal score incomparability\" 和 \"measurement non-invariance\" 应在首次出现时明确对应关系。\n\n**[AGREE] R2-M2:** `\\enlargethispage*{4\\baselineskip}` 确实是潜在的格式风险。虽然 ACL 模板没有明确禁止此命令，但如果它导致正文页面实际内容超出标准行数，可能被 reviewer/AC 标记。我在首轮审稿中未检查 LaTeX 源码层面的格式合规性，这是一个有价值的补充。\n\n**[AGREE] R2-M3:** ±2.12pp 偏移是否在排名差异的置信区间内——这是一个好问题。论文报告了 DIF-corrected scores 的 rank displacement（Section 4.6: \"Among the 200 most displaced models (top 3.8%), 33.6% of pairwise rankings reverse\"），但未将 ±2.12pp 与排名不确定性的 baseline（如 bootstrap confidence interval of rank）进行比较。如果 ±2.12pp 落在 typical ranking noise 范围内，DIF correction 的实际价值会被削弱。\n\n**[AGREE] R2-M4:** Figure 1 右图 y 轴标注条件概率是合理的改进建议。\n\n---\n\n### Missing References\n\nR2 提出的 4 篇论文（Adaptive Testing for LLM Evaluation, JE-IRT, Confident Rankings with Fewer Items, When Benchmarks Leak）如果确实存在且相关，是合理的补充。但我无法当场验证这些 arXiv ID 的真实性——建议 Director 确认后转达给作者。其中 \"Adaptive Testing for LLM Evaluation\" 和 \"JE-IRT\" 可能与论文的 IRT 方法论直接相关，值得优先考虑。\n\n---\n\n### Questions\n\n**[对 R2-Q1 的回应]** Subject-level DIF enrichment ratio 差异：Table 6（Domain-level Cohen's d）和 Table 1 提供了部分 subject-level 数据。论文指出 knowledge-grounding benchmarks 的 C% 高于 procedural ones（Table 3: HellaSwag 17.9% vs. MMLU 31.5%），暗示知识密集型 items 更易受 temporal DIF 影响。但详细的 subject-level 驱动因素分析确实缺失。\n\n**[对 R2-Q2 的回应]** 更粗粒度的 family 定义：Appendix D（Size-stratified DEFF）和 Appendix H（LOFO robustness）提供了相关信息。Table 9 按 tier（<10, 10-50, 50-200, >200 members）分析了 ICC 和 DEFF。粗粒度 family 定义可能降低 ICC（因家族内异质性增加），进而减小 DEFF correction，但论文没有直接测试这一变体。这是一个有价值的 robustness check。\n\n**[对 R2-Q3 的回应]** Difficulty-dependent injection：已在 Appendix G 中覆盖（mixed-mechanism injection, Scheme D and E）。论文发现 difficulty-dependent injection 能复制 overall DIF direction gradient 但不能复制 instruct-model 的 near-zero reversal。这部分回答了 Q3。\n\n**[对 R2-Q4 的回应]** DIF-flagged items 与 Growing Pains anchor sets：这是一个好的应用建议，值得在 Discussion 中提及。Growing Pains（Habba et al., 2026）使用 IRT calibration 建立 anchor items for equating——如果这些 anchor items 存在 temporal DIF，equating 的有效性会受影响。\n\n---\n\n### 总结\n\nR2 的审稿侧重 novelty framing 和 presentation，与我（R1）侧重 statistical methodology 形成互补。我在 N2(a) 上强烈反驳——cross-subject matching 是 formal contribution 而非 implementation decision。在 N1 上部分反驳——global-vs-differential independence 不是定义上显然的。在 W1-W3 上基本同意。我认为 R2 的 overall 3.5 评分合理，但 N2 中对 cross-subject matching 新颖性的低估可能导致了过于保守的评价。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: Contribution 1（global exposure vs. DIF 独立性）的贡献度**\n\nR2 认为 global exposure 和 differential functioning\"定义上就是不同构念\"，因此低 Jaccard（≈ 0.206）只是在\"确认显而易见的事实\"。我不完全同意。\n\n**证据与理由：**\n1. 定义上不同 ≠ 经验上必然独立。contamination detection 文献的隐含假设恰恰是：global exposure（item 出现在训练数据中）会导致 differential functioning（模型在该 item 上表现异常）。MinK++ (Shi et al., 2024)、Time Travel (Golchin and Surdescu, 2024) 等方法正是基于这一假设运作的。如果二者真的\"显而易见地独立\"，这些方法的理论基础就需要重新审视。\n2. 论文提供了具体的定量证据：Jaccard ≈ 0.206, Enrichment ratio ≈ 1.0（Section 4.3, Figure 1），permutation null (Jaccard = 0.206, p = 0.88)。这不是重述定义，而是对一个被广泛默认成立的假设的实证否证。\n3. 同时，Abstract 明确指出 \"aggregate rankings are robust (ρ ≈ 0.997), but absolute scores are not directly comparable\"——即 global exposure 不影响排名但 DIF 影响绝对分数。这一区分在先前文献中没有被系统建立。\n\n**部分同意点：** 我同意将此作为\"三大贡献之首\"的位置可以商榷——它更适合作为背景性的 empirical observation 来激发后续方法学贡献，而非独立的 headline contribution。建议作者调整 Introduction 中三个 contribution 的排序和权重表述。\n\n---\n\n**[REBUT] R2-N2: \"Three methodological adaptations\" 的新颖性**\n\nR2 认为三项适配均不构成方法论贡献：(a) cross-subject matching 是\"实施决策\"，(b) DEFF 借用 survey methodology，(c) semi-synthetic validation 是验证策略。我对 (a) 强烈反驳，对 (b)(c) 部分同意。\n\n**对 (a) Cross-subject matching 的反驳：**\n- 这不是标准实施决策。教育测量中 MH-DIF 的标准做法是使用 within-test total score 作为 matching variable（Holland and Thayer, 1988; Donoghue and Allen, 1993）。论文的创新在于：当 matching variable 本身可能被 contamination 污染时（benchmark 的 total score 包含了被 contaminate 的 items），使用 cross-subject total score 排除被测 subject，从构造上保证 ΔFPR = 0（Section 3.4，含形式化推导）。\n- 这一保证是 formal result，不是 engineering choice。Section 3.4 给出了严格证明：single-subject injection 下，被测 subject 的 items 不进入 matching variable，因此注入不影响 matching，ΔFPR = 0 by construction。\n- Table 7（Section 4.5）的实证验证进一步支持：single-subject injection 下 ΔFPR = 0.000（所有 MMLU subjects），而 within-subject matching 下 ΔFPR 则显著膨胀（+0.186）。这不是\"显然的实施选择\"——它解决了将 DIF 应用到 contaminated benchmarks 时一个此前未被形式化的 matching variable corruption 问题。\n\n**对 (b) DEFF correction 的部分同意：**\n- R2 说得对，DEFF 概念源自 survey methodology（Kish, 1965）。但将其适配到 LLM model-family 结构需要非平凡的工作：计算 family-level ICC、处理 heterogeneous family sizes、在 Appendix I 中通过 simulation 比较 simple-mean vs. weighted-mean 估计量。称之为\"adaptation\"而非\"original contribution\"更准确。\n\n**对 (c) Semi-synthetic validation 的同意：**\n- 我同意 semi-synthetic injection 更接近 validation strategy 而非 methodological contribution。论文用 \"validation\" 一词本身是准确的，但将其列为三大\"methodological adaptations\"之一确实拉升了新颖性声称。\n\n**建议：** 论文可将 (a) cross-subject matching 单独突出为主要方法学贡献（含 formal guarantee），将 (b)(c) 降级为\"supporting methodological choices\"或\"complementary validation\"。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: §5.2 审计协议中的 mechanism inference**\n\nR2 指出\"DIF on web-clean items suggests capability shift\"超出了 DIF 方法的能力边界。我同意这一批评。\n\nDIF by design 是 mechanism-agnostic 的（论文自身在 Limitations 中承认这一点）。虽然 §5.2 使用了 \"suggests\" 而非 \"proves\" 的措辞，但在审计协议这种规范性建议中，即便是\"suggests\"也可能被误读为因果推断。\n\n**补充意见：** 论文可改为更保守的表述，如：\"DIF on web-clean items is inconsistent with contamination as the sole mechanism\"——这是 MH-DIF 结合 web-overlap labels 可以支持的排除性推理，不需要正面声称是\"capability shift\"。\n\n---\n\n**[AGREE] R2-W2: Discussion 缺乏深层 insight（部分同意）**\n\n§5.1 确实更像是附加的实验分析（base/instruct 分层、model family profiles、difficulty-direction interaction）而非对 temporal DIF 成因的深层讨论。我部分同意。\n\n**但有两点需要补充：**\n1. 论文的核心贡献是 empirical audit 而非 mechanistic explanation。在 8 页限制下，合理的选择是将 Discussion 聚焦在最直接可操作的内容（审计协议），而非对缺乏数据支撑的因果机制进行推测。\n2. §5.1 中 base/instruct 方向差异（base: 61.1% reference-favoring, ρ = −0.528; instruct: 65.6% focal-favoring, ρ = −0.079, Section 5.1/Appendix O）不仅是结果报告——它提供了 structured signal 的证据，表明 DIF 不是随机噪声而是与训练方法论相关的系统性模式。这超越了简单的结果重述。\n\n---\n\n**[AGREE] R2-W3: Abstract 信息密度过高**\n\n同意。15+ 个数值在单段 abstract 中确实影响可读性。这是可以在 revision 中轻松改善的表达问题。\n\n---\n\n**[REBUT] R2-W4: Limitations 覆盖面偏窄（部分反驳）**\n\nR2 认为应补充：(1) 对 MMLU 式 MCQ 以外基准的泛化性，(2) 模型发布日期与训练数据截止不对齐，(3) Li et al. web-overlap 标签自身局限性。\n\n**反驳理由：**\n1. 关于泛化性：论文在 Section 4.7 已在 GSM8K（数学问题，非传统 MCQ）上完成了 cross-benchmark 复制，且 Table 3 报告了 6 个 METABENCH benchmarks 的 DIF 率（20.7%–48.4%），涵盖了不同题型。Limitations 中不需要重复讨论已有实证覆盖的问题。\n2. 关于 web-overlap 标签局限性：论文的核心发现恰恰是 DIF flags 与 web-overlap labels 近似独立（Jaccard ≈ 0.206），因此 web-overlap labels 的局限性主要影响 Section 4.3 的 ground truth comparison，而不影响论文的主要 DIF 分析。\n\n**同意点：** 模型发布日期与训练数据截止不对齐是一个值得在 Limitations 中提及的有效关切——temporal cohort 按 release date 划分，但模型的训练数据可能跨越了这些边界。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1:** 术语一致性是合理的要求。\"temporal score incomparability\" 和 \"measurement non-invariance\" 应在首次出现时明确对应关系。\n\n**[AGREE] R2-M2:** `\\enlargethispage*{4\\baselineskip}` 确实是潜在的格式风险。虽然 ACL 模板没有明确禁止此命令，但如果它导致正文页面实际内容超出标准行数，可能被 reviewer/AC 标记。我在首轮审稿中未检查 LaTeX 源码层面的格式合规性，这是一个有价值的补充。\n\n**[AGREE] R2-M3:** ±2.12pp 偏移是否在排名差异的置信区间内——这是一个好问题。论文报告了 DIF-corrected scores 的 rank displacement（Section 4.6: \"Among the 200 most displaced models (top 3.8%), 33.6% of pairwise rankings reverse\"），但未将 ±2.12pp 与排名不确定性的 baseline（如 bootstrap confidence interval of rank）进行比较。如果 ±2.12pp 落在 typical ranking noise 范围内，DIF correction 的实际价值会被削弱。\n\n**[AGREE] R2-M4:** Figure 1 右图 y 轴标注条件概率是合理的改进建议。\n\n---\n\n### Missing References\n\nR2 提出的 4 篇论文（Adaptive Testing for LLM Evaluation, JE-IRT, Confident Rankings with Fewer Items, When Benchmarks Leak）如果确实存在且相关，是合理的补充。但我无法当场验证这些 arXiv ID 的真实性——建议 Director 确认后转达给作者。其中 \"Adaptive Testing for LLM Evaluation\" 和 \"JE-IRT\" 可能与论文的 IRT 方法论直接相关，值得优先考虑。\n\n---\n\n### Questions\n\n**[对 R2-Q1 的回应]** Subject-level DIF enrichment ratio 差异：Table 6（Domain-level Cohen's d）和 Table 1 提供了部分 subject-level 数据。论文指出 knowledge-grounding benchmarks 的 C% 高于 procedural ones（Table 3: HellaSwag 17.9% vs. MMLU 31.5%），暗示知识密集型 items 更易受 temporal DIF 影响。但详细的 subject-level 驱动因素分析确实缺失。\n\n**[对 R2-Q2 的回应]** 更粗粒度的 family 定义：Appendix D（Size-stratified DEFF）和 Appendix H（LOFO robustness）提供了相关信息。Table 9 按 tier（<10, 10-50, 50-200, >200 members）分析了 ICC 和 DEFF。粗粒度 family 定义可能降低 ICC（因家族内异质性增加），进而减小 DEFF correction，但论文没有直接测试这一变体。这是一个有价值的 robustness check。\n\n**[对 R2-Q3 的回应]** Difficulty-dependent injection：已在 Appendix G 中覆盖（mixed-mechanism injection, Scheme D and E）。论文发现 difficulty-dependent injection 能复制 overall DIF direction gradient 但不能复制 instruct-model 的 near-zero reversal。这部分回答了 Q3。\n\n**[对 R2-Q4 的回应]** DIF-flagged items 与 Growing Pains anchor sets：这是一个好的应用建议，值得在 Discussion 中提及。Growing Pains（Habba et al., 2026）使用 IRT calibration 建立 anchor items for equating——如果这些 anchor items 存在 temporal DIF，equating 的有效性会受影响。\n\n---\n\n### 总结\n\nR2 的审稿侧重 novelty framing 和 presentation，与我（R1）侧重 statistical methodology 形成互补。我在 N2(a) 上强烈反驳——cross-subject matching 是 formal contribution 而非 implementation decision。在 N1 上部分反驳——global-vs-differential independence 不是定义上显然的。在 W1-W3 上基本同意。我认为 R2 的 overall 3.5 评分合理，但 N2 中对 cross-subject matching 新颖性的低估可能导致了过于保守的评价。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-23T10:32:30.513076+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4069
}
```

</details>

---


### Tool call

_source line 1236 · 2026-05-23T10:32:50.254850+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1237 · 2026-05-23T10:32:50.356883+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 102
}
```

</details>

---


### Assistant

_source line 1238 · 2026-05-23T10:33:03.890879+00:00_

交叉回应已提交。总结：

- **N1**（global vs. DIF 独立性）：[REBUT] — 定义上不同≠经验上独立，contamination 文献隐含了二者相关的假设，实证否证不是"显而易见"。但同意其作为 Contribution #1 的位置可调整。
- **N2**（三项适配新颖性）：对 (a) cross-subject matching [REBUT]——有 formal ΔFPR=0 guarantee，不是 implementation decision；对 (b) DEFF 和 (c) semi-synthetic 部分 [AGREE]。
- **W1–W3**：基本 [AGREE]，§5.2 的 mechanism inference 超出 DIF 能力、Discussion 可更深、Abstract 过密。
- **W4**（Limitations 窄）：部分 [REBUT]——GSM8K 复制和 Table 3 已覆盖泛化性，但 release date vs. training cutoff 不对齐值得补充。
- **Minor M1–M4**：全部 [AGREE]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 43

## Round 43

100 recorded events


### User

_source line 1239 · 2026-05-23T11:25:10.421610+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。

## Venue 信息
- **EMNLP 2026** Long Paper via ACL Rolling Review (ARR)
- 正文 8 页限制，参考文献无限制
- Limitations 章节必须有，不计页数
- ACL 模板，double-blind
- Deadline: 2026-05-25
- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit

## 论文文件
- LaTeX: `projects/irt_equated_bench_regen/paper/main.tex`（入口文件，各章节在 `sections/` 目录）
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/submitted.pdf`

## 你的审查侧重

请重点评估以下维度：

1. **DIF 方法论适用性**：MH-DIF 从教育测量迁移到 LLM 评估的合理性。ETS 阈值（|Δ_MH| ≥ 1.5）的 LLM 适切性——论文是否提供了充分的 empirical calibration？随机分割基线是否足以建立 null distribution？
2. **统计控制充分性**：DEFF 校正两种估计量（simple-mean 29.2% vs weighted-mean 13.5%）的选择是否合理？推荐 simple-mean 作为 primary estimate 的论证是否充分？非独立性处理是否到位？
3. **Semi-synthetic validation**：uniform binary flipping 的 ecological validity。ΔTPR 标为 detection-power upper bound 是否充分？difficulty-dependent injection 是否弥补了 uniform 的局限？
4. **Cross-subject matching**：ΔFPR=0 的 formal guarantee 在什么条件下成立？k≤5 的限定是否充分讨论？当 k>5 时 graceful degradation 的论证是否严谨？
5. **实验设计**：temporal cohort 划分（2023 vs 2024）的合理性；ability confound 的控制（matched-ability quintile, NN matching）；cross-benchmark replication 的说服力
6. **Ground truth analysis**：DIF 与 web-overlap labels 的正交性论证逻辑是否自洽？enrichment≈1.0 的解释是否 convincing？
7. **Downstream impact**：ρ≈0.997 的 ranking preservation 与 ±800 rank displacement 的张力如何解读？DIF-corrected scoring 的实际意义

请按 ARR 审稿标准出具完整审稿意见，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment（含评分和置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1240 · 2026-05-23T11:25:21.167122+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search ARR review form",
  "prompt": "Search the web for the official ACL Rolling Review (ARR) review form and reviewer guidelines for 2025-2026. I need the exact scoring dimensions, their scales, and descriptions. Search for:\n1. \"ACL Rolling Review review form 2025\" or \"ARR review form criteria\"\n2. \"ACL ARR reviewer guidelines scoring dimensions\"\n\nReturn the complete list of scoring dimensions with their scales and what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Search ARR review form",
    "prompt": "Search the web for the official ACL Rolling Review (ARR) review form and reviewer guidelines for 2025-2026. I need the exact scoring dimensions, their scales, and descriptions. Search for:\n1. \"ACL Rolling Review review form 2025\" or \"ARR review form criteria\"\n2. \"ACL ARR reviewer guidelines scoring dimensions\"\n\nReturn the complete list of scoring dimensions with their scales and what each score means."
  }
}
```

</details>

---


### Tool call

_source line 1241 · 2026-05-23T11:25:21.770366+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/",
  "description": "List review round artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/",
    "description": "List review round artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1242 · 2026-05-23T11:25:21.922471+00:00_

_pdf_images
submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1243 · 2026-05-23T11:25:22.374424+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form 2025 ARR review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form 2025 ARR review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1244 · 2026-05-23T11:25:22.526176+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR reviewer guidelines scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR reviewer guidelines scoring dimensions"
  }
}
```

</details>

---


### Tool result

_source line 1245 · 2026-05-23T11:25:28.629392+00:00_

Web search results for query: "ACL ARR reviewer guidelines scoring dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR reviewer guidelines scoring dimensions:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

These three scoring dimensions represent the current evaluation framework for ARR (ACL Rolling Review) submissions. The guidelines emphasize that published research should at least be technically sound and appropriately scoped.

The search results show that ARR developed detailed guidelines and suggestions for each step of the process, including a list of common problems in both reviews and NLP paper
…[truncated 506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6103
}
```

</details>

---


### Tool result

_source line 1246 · 2026-05-23T11:25:29.787165+00:00_

Web search results for query: "ACL Rolling Review review form 2025 ARR review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL ARR 2025 July | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FJuly"}]

I found information about the ACL Rolling Review (ARR) 2025 review form and criteria. Here are the key details:

## ARR 2025 Review Form - Reviewer Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text 
…[truncated 1355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7412
}
```

</details>

---


### Tool call

_source line 1247 · 2026-05-23T11:25:31.346962+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "What are the scoring dimensions, scales, and descriptions for reviewer scores?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "What are the scoring dimensions, scales, and descriptions for reviewer scores?"
  }
}
```

</details>

---


### Tool call

_source line 1248 · 2026-05-23T11:25:31.699904+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "What are the complete scoring dimensions with their scales and what each score means?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "What are the complete scoring dimensions with their scales and what each score means?"
  }
}
```

</details>

---


### Tool result

_source line 1249 · 2026-05-23T11:25:36.485236+00:00_

# ARR Reviewer Scoring Dimensions

Based on the guidelines provided, ARR uses **three scoring dimensions** as of February 2025:

1. **Soundness** - Assesses technical validity and rigor. The guidelines state that "soundness scores must be justified by the text of the review." Low scores require explicit evidence of flaws.

2. **Excitement** - Reflects personal interest independent of quality. The document notes this is "orthogonal to the assessment of the soundness of the paper" and represents subjective preferences rather than objective merit.

3. **Overall Recommendation** - A composite score indicating whether the paper merits acceptance at an ACL venue. This balances "soundness, excitement, and also other factors like novelty and impact."

The guidelines emphasize that papers must be "sufficiently sound and reproducible" for main conference consideration, though reviewers may rate papers as acceptable despite low personal excitement if they have significant impact potential.

**Note:** The document does not specify exact numerical scales (e.g., 1-5 or 1-10) for these dimensions, only describing their conceptual meanings and relationships.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4785
}
```

</details>

---


### Tool result

_source line 1250 · 2026-05-23T11:25:36.889911+00:00_

# ACL Rolling Review Scoring Dimensions

The review form includes five main scoring dimensions:

## 1. **Reviewer Confidence** (1-5 scale)
Ranges from "Not my area, or paper is very hard to understand" (1) to "Positive that my evaluation is correct" (5).

## 2. **Soundness** (1-5 scale)
Evaluates whether the study is "sufficiently sound and thorough" with claims adequately supported. Ranges from "Major Issues" (1) to "Excellent" (5).

## 3. **Excitement** (1-5 scale)
A subjective measure of how transformational or impactful the paper is, from "Not Exciting" (1) to "Highly Exciting" (5).

## 4. **Overall Assessment** (1-5 scale)
The primary recommendation dimension spanning from "Do not resubmit" (1) through intermediate categories like "Findings" and "Conference" to "Consider for Award" (5).

## 5. **Reproducibility** (1-5 scale)
Assesses whether readers could replicate results, from "would not be able to reproduce" (1) to "could easily reproduce" (5).

Additional dimensions rate **Datasets** and **Software** quality (1-5 scales), plus **Author Identity** knowledge (1-5 scale).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5542
}
```

</details>

---


### Tool call

_source line 1251 · 2026-05-23T11:25:38.447074+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md",
  "prompt": "What are the complete scoring dimensions with their scales and exact descriptions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md",
    "prompt": "What are the complete scoring dimensions with their scales and exact descriptions?"
  }
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-23T11:25:38.701868+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md",
  "prompt": "What are the review form criteria and scoring dimensions for 2025?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md",
    "prompt": "What are the review form criteria and scoring dimensions for 2025?"
  }
}
```

</details>

---


### Tool result

_source line 1253 · 2026-05-23T11:25:41.976843+00:00_

# Review Form Criteria for 2025

Based on the provided content, the document does not explicitly detail the specific scoring dimensions or criteria used in the 2025 review form. 

The page notes that "Here is the current version of the review form" and provides a link to it, but the actual form criteria are not included in this Call for Papers document. The document does mention that review forms are "re-assessed and updated periodically," but specific scoring rubrics or evaluation dimensions for 2025 are not outlined here.

To find the detailed review criteria, you would need to consult the actual review form linked on the ARR website rather than this call for papers document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 3274
}
```

</details>

---


### Tool result

_source line 1254 · 2026-05-23T11:25:43.286887+00:00_

# ARR Reviewer Scoring Dimensions

Based on the guidelines, reviewers provide **three scores**:

1. **Soundness** - "The _soundness_ scores must be justified by the text of the review." Low scores require explicit justification; papers must be technically sound for acceptance.

2. **Excitement** - Reflects personal interest independent of soundness. The guidelines note this is "orthogonal to the assessment of the soundness of the paper" and "do not necessarily come with explicit reasons."

3. **Overall Assessment** - "An explicit recommendation for the outcome of this paper, if it were committed to an \*ACL venue." This composite score balances soundness, excitement, novelty, and potential impact.

The document does not specify exact numerical scales for these dimensions. It emphasizes that soundness and overall assessment scores must align with review content, while excitement captures subjective preference separate from technical evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4839
}
```

</details>

---


### Tool call

_source line 1255 · 2026-05-23T11:25:44.694099+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR review form soundness excitement overall recommendation 1-5 scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR review form soundness excitement overall recommendation 1-5 scale"
  }
}
```

</details>

---


### Tool call

_source line 1256 · 2026-05-23T11:25:44.895517+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" reviewer confidence reproducibility scoring 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" reviewer confidence reproducibility scoring 2025"
  }
}
```

</details>

---


### Tool result

_source line 1257 · 2026-05-23T11:25:50.777780+00:00_

Web search results for query: ""ACL Rolling Review" reviewer confidence reproducibility scoring 2025"

Links: [{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Can LLM feedback enhance review quality? A randomized study of 20K   reviews at ICLR 2025","url":"https://arxiv.org/pdf/2504.09737"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

I found relevant information about the ACL Rolling Review (ARR) scoring system for 2025. Here are the key findings:

## Reviewer Scoring Changes in 2025

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness and Reproducibility Requirements

Soundness scores must be justified by the text of the review. Additionally, low reproducibility scores should be justified. 

All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible.

## Separation of Soundness and Excitement

The new scoring framework distinguishes between objective assessment and personal preference. Excitement is a separate score that is orthogonal to the assessm
…[truncated 445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5882
}
```

</details>

---


### Tool result

_source line 1258 · 2026-05-23T11:25:51.179959+00:00_

Web search results for query: "ARR review form soundness excitement overall recommendation 1-5 scale"

Links: [{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"}]

Based on the search results, here's information about the ARR review form with soundness, excitement, and overall recommendation on 1-5 scales:

## Overview

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Scale

The soundness scale includes ratings such as 5 = Excellent (one of the most thorough studies), 4 = Strong (sufficient support for all claims), and 3 = Acceptable (sufficient support for main claims). The soundness scores must be justified by the text of the review.

## Excitement Scale

The excitement scale includes 5 = Highly Exciting (would recommend or attend presentation), and 4 = Exciting (would mention to others or make effort to attend). Excitement scores reflect personal taste and do not necessarily come with explicit reasons.

## Overall Recommendation

The Overall assessment score is an explicit recommendation for the outcome of the paper if committed to an ACL venue, reflecting assessment of soundness, e
…[truncated 321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6485
}
```

</details>

---


### Tool call

_source line 1259 · 2026-05-23T11:25:55.101071+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "List all scoring dimensions with their 1-5 scales and what each number means"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "List all scoring dimensions with their 1-5 scales and what each number means"
  }
}
```

</details>

---


### Tool result

_source line 1260 · 2026-05-23T11:26:00.122562+00:00_

# ACL Rolling Review Scoring Dimensions

## 1. Reviewer Confidence
**Scale: 1-5**
- **5**: Positive evaluation is correct; careful reading with familiarity of related work
- **4**: Quite sure; important points checked carefully
- **3**: Pretty sure; general area knowledge but details not verified
- **2**: Willing to defend evaluation; likely missed some details or novelty assessment uncertain
- **1**: Outside expertise area or paper very difficult to understand

## 2. Soundness
**Scale: 1-5 (with half-point increments)**
- **5**: "one of the most thorough" studies of its type
- **4**: Provides sufficient support for claims; minor additions optional
- **3**: Adequate support for main claims; some minor details need reinforcement
- **2**: Main claims lack sufficient support; major technical/methodological problems
- **1**: Insufficient rigor for publication or lacks relevance to ACL

## 3. Excitement
**Scale: 1-5 (with half-point increments)**
- **5**: Highly engaging; would recommend or attend presentation
- **4**: Compelling; would mention to colleagues or attend presentation
- **3**: Noteworthy; might discuss some points or attend if available
- **2**: Potentially interesting to some in the community
- **1**: Not engaging; unlikely to resonate with the ACL community

## 4. Overall Assessment
**Scale: 1-5 (with half-point increments)**
- **5**: Award consideration candidate
- **4**: Conference acceptance recommended
- **3**: Findings acceptance suitable
- **2**: Needs substantial revisions by next cycle
- **1**: Requires major overhaul or lacks ACL relevance

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5021
}
```

</details>

---


### Tool call

_source line 1261 · 2026-05-23T11:26:02.081502+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "List all scoring dimensions including reproducibility, datasets, software, and author identity with their scales"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "List all scoring dimensions including reproducibility, datasets, software, and author identity with their scales"
  }
}
```

</details>

---


### Tool result

_source line 1262 · 2026-05-23T11:26:06.952404+00:00_

# ARR Review Scoring Dimensions

Based on the ARR Reviewer Guidelines, the primary scoring dimensions are:

## Main Scoring Dimensions

**Soundness** - Assesses technical validity and correctness of the research methodology

**Excitement** - Reflects personal interest and subjective assessment of the work's appeal

**Overall Recommendation** - Composite score recommending acceptance, rejection, or other outcomes

## Related Assessment Areas

The guidelines reference a **reproducibility score**, though detailed scale information isn't explicitly provided. Reviewers evaluate whether "enough details/code is provided for reproducibility."

The document notes that reviewers indicate their **confidence level** in assessments, and can specify knowledge of author identity.

## Important Context

The guidelines emphasize that "soundness scores must be justified by the text of the review." The overall recommendation should reflect "soundness, excitement, and also other factors like novelty and impact."

Notably, the document does not present a traditional multi-dimensional rubric with numbered scales (e.g., 1-5 ratings across multiple criteria). Instead, it focuses on three primary scores with supporting justifications in review text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4870
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-23T11:26:12.732727+00:00_

## Summary: ACL Rolling Review (ARR) 2025-2026 Scoring Dimensions

Based on the official ACL Rolling Review materials, here are the complete scoring dimensions with their scales and descriptions:

### **Primary Scoring Dimensions (3 Scores Required)**

#### 1. **Soundness** (1-5 scale, half-point increments allowed)
- **5**: One of the most thorough studies of its type
- **4**: Provides sufficient support for claims; minor additions optional
- **3**: Adequate support for main claims; some minor details need reinforcement
- **2**: Main claims lack sufficient support; major technical/methodological problems
- **1**: Insufficient rigor for publication or lacks relevance to ACL
- **Key Requirement**: Soundness scores MUST be justified by the text of the review

#### 2. **Excitement** (1-5 scale, half-point increments allowed)
- **5**: Highly engaging; would recommend or attend presentation
- **4**: Compelling; would mention to colleagues or attend presentation
- **3**: Noteworthy; might discuss some points or attend if available
- **2**: Potentially interesting to some in the community
- **1**: Not engaging; unlikely to resonate with the ACL community
- **Key Characteristic**: Subjective and orthogonal to soundness assessment; does not necessarily require explicit justification

#### 3. **Overall Assessment/Recommendation** (1-5 scale, half-point increments allowed)
- **5**: Award consideration candidate
- **4**: Conference acceptance recommended
- **3**: Findings acceptance suitable
- **2**: Needs substantial revisions by next cycle
- **1**: Requires major overhaul or lacks ACL relevance
- **Basis**: Composite score reflecting soundness, excitement, and other factors like novelty and impact

### **Secondary Scoring Dimensions**

#### 4. **Reviewer Confidence** (1-5 scale)
- **5**: Positive evaluation is correct; careful reading with familiarity of related work
- **4**: Quite sure; important points checked carefully
- **3**: Pretty sure; general area knowledge but detai
…[truncated 992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 51565
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-23T11:26:17.057625+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1265 · 2026-05-23T11:26:17.108346+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-23T11:26:24.849167+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1267 · 2026-05-23T11:26:25.050437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 1268 · 2026-05-23T11:26:25.152048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool call

_source line 1269 · 2026-05-23T11:26:25.153577+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1270 · 2026-05-23T11:26:26.308382+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 570.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p9.png\", \"width\": 1
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1459
}
```

</details>

---


### Tool result

_source line 1271 · 2026-05-23T11:26:26.308836+00:00_

1	\begin{abstract}
2	LLM benchmark scores are compared across model generations, yet whether individual items measure the same construct over time is rarely tested. We apply differential item functioning (DIF) analysis from educational measurement to six METABENCH benchmarks (5,227 models), validated through a semi-synthetic injection framework with cross-subject matching. Between 2023 and 2024 model cohorts, 17.9--31.3\% of items exhibit large temporal DIF (${\approx}$27--29\% for MMLU after non-independence corrections; conservative bound 13.5\%; random-split baseline 0.62\%). Web-overlap contamination labels are near-independent of DIF flags: global exposure and differential functioning are complementary diagnostic dimensions. Temporal DIF does not threaten aggregate rankings ($\rho \approx 0.997$) but reveals structured item-level change---base and instruct models exhibit opposite DIF patterns---and shifts DIF-corrected scores by ${+}2.12$\,pp on average. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1258
}
```

</details>

---


### Tool result

_source line 1272 · 2026-05-23T11:26:26.309104+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \emph{measurement invariance} to denote the property that test items function identically across groups~\citep{meredith1993invariance}, \emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \emph{temporal score incomparability} (measurement non-invariance across temporal cohorts, manifesting as score incomparability) as the empirical phenomenon when DIF is detected---scores are not directly comparable across cohorts because item measurement properties differ systematically, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.62\% under a random-split control. Aggregate rankings are robust ($\rho \approx 0.997$), but absolute scores are not directly comparable: DIF-corrected scoring shifts accuracy by ${+}2.12$\,pp on average, with individual models displaced by up to 849 rank positions. The incomparability is diagnostic, revealing which capability dimensions shift across model generations.
5	
6	Existing approaches to benchmark integrity focus on \emph{global exposure}---whether items appear in training corpora---through membership inference~\citep{shi2024mink} and performance-based detection~\citep{deko
…[truncated 3074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1157
}
```

</details>

---


### Tool result

_source line 1273 · 2026-05-23T11:26:26.309405+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh,magis2010difr} detects DIF by stratify
…[truncated 9039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 1274 · 2026-05-23T11:26:31.384871+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1275 · 2026-05-23T11:26:31.837409+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	A Monte Carlo power analysis (1,000 replications) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80 and AUC of 0.93--0.94 for $|\Delta_{\mathrm{MH}}| \geq 1.4$ (\Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold; power varies with item discrimination (TPR 0.40--0.95 across $a = 0.5$--$2.0$; \Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal DIF: 31\% of Items Exhibit Differential Functioning}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.4\%, 38.1\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$, upper bound driven by mega-family over-representation; \Cref{app:uncertainty}). Two DEFF estimators bound the non-independence effect in parallel: simple-mean DEFF (29.2\%) and cluster bootstrap (26.7\%) converge on ${\approx}$27--29\%, while the conservative weighted-mean DEFF yields 13.5\%---still ${\approx}22\times$ the random baseline (\Cref{app:deff,app:deff_simulation}). We recommend simple-mean DEFF as the primary estimate: it converges with the cluster bootstrap and DEFF simulation, while weighted-mean DEFF over-corrects by down-weighting large families with systematically lower ICC. Under 100 random permutations within the 2023 c
…[truncated 10755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-23T11:26:31.837875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-23T11:26:32.805957+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Temporal DIF as Structured Signal}
5	\label{sec:disc_temporal}
6	
7	\looseness=-1
8	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}---and this is by design. Stratifying by model type reveals opposite patterns: base models ($N{=}1{,}409$) are 60.1\% reference-favoring ($\rho = -0.570$), while instruct models ($N{=}478$) are 65.6\% focal-favoring ($\rho = -0.079$; $\chi^2 = 562.7$, $p < 10^{-124}$). Following the impact-bias framework~\citep{camilli1994methods}, this reversal reflects structured item-level bias rather than uniform group impact, validating DIF as a mechanism-agnostic diagnostic (\Cref{app:mechanism_discussion}).
9	
10	\looseness=-1
11	Composition downsampling ($\Delta = 1.08$\,pp), base-only (32.1\%), and instruct-only (36.5\%) temporal analyses independently confirm DIF is not an artifact of cohort structure (\Cref{app:composition_control,app:baseinst_temporal,app:within_arch}). These findings have immediate implications for leaderboard maintenance: temporal DIF means the same score carries different meaning across model generations, motivating periodic psychometric audits alongside score reporting.
12	
13	\looseness=-1
14	Three features distinguish LLM temporal DIF from educational settings: (1)~the observed C\% (${\approx}$27--29\%) substantially exceeds typical educational DIF rates~\citep{clauser1998dif}; (2)~DIF flags and web-overlap labels are near-independent (Jaccard $= 0.206$), unlike educational settings where DIF correlates with construct-irrelevant variance; (3)~model families introduce non-independence (design effect) absent in human testing, necessitating DEFF correction (\Cref{app:deff}).
15	
16	\subsection{Recommended DIF Audit Protocol}
17	\label{sec:disc_protocol}
18	
19	\looseness=-1
20	Item-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \Cref{app:predictive}), precluding pre-screening. We recommend MH-DIF
…[truncated 603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 968
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-23T11:26:32.806344+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1279 · 2026-05-23T11:26:33.308575+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues and \citet{oren2024proving} prove contamination through exchangeability tests. Performance-based detectors identify contamination through statistical anomalies \citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique,deng2024investigating} in-context learning effects~\citep{zawalski2026codec}, or inference-time decontamination~\citep{chai2026benchmarksleak}. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introd
…[truncated 4571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-23T11:26:33.309083+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1281 · 2026-05-23T11:26:33.561088+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-2
5	Across six METABENCH benchmarks, 17.9--31.3\% of items exhibit temporal DIF across 2023--2024 model cohorts (${\approx}$27--29\% for MMLU; conservative bound: 13.5\%), while aggregate rankings remain preserved ($\rho \approx 0.997$). Global exposure and differential functioning are complementary diagnostic dimensions (Jaccard $= 0.206$), confirmed by opposite base-vs-instruct DIF patterns ($\chi^2 = 562.7$). DIF-corrected scoring shifts accuracy by ${+}2.12$\,pp on average, with rank displacements exceeding ${\pm}500$. Mechanism-conditional DIF audit should complement contamination screening as standard practice~\citep{habba2026growingpains}.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1282 · 2026-05-23T11:26:33.561587+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1283 · 2026-05-23T11:26:33.612970+00:00_

1	\section*{Limitations}
2	
3	\looseness=-1
4	Three primary limitations apply. (1)~The semi-synthetic framework uses uniform binary response flipping, a stylized injection model; reported $\Delta\mathrm{TPR}$ values may overestimate detection power, and detection power under realistic contamination patterns (partial memorization, format-specific advantages) is untested. The framework detects \emph{that} items function differently but not \emph{why}---a deliberate design choice that limits immediate actionability; follow-up expert review is needed to determine whether flagged items should be retired or retained. (2)~The MH $\chi^2$ test assumes independent examinees; LLM model families violate this assumption. Three convergent corrections (${\approx}$27--29\%) and family-level cluster bootstrap (95\% CI: $[26.7\%, 53.2\%]$) bound the impact, but the extreme relatedness of some families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in educational settings~\citep{french2010hierarchical}. (3)~Cross-subject matching assumes contamination affects a minority of domains; $\Delta\mathrm{FPR}$ rises to 0.069 when contamination spans ${\geq}20$ subjects. Although composition control experiments show a small residual shift ($\Delta = 1.08$\,pp; \Cref{app:composition_control}), base/instruct ratio changes between cohorts remain a potential confound that cannot be fully eliminated without single-architecture longitudinal data. Temporal cohorts defined by calendar year provide coarse granularity, and generalizability to open-ended or partial-credit benchmarks is untested. Multidimensional DIF~\citep{ackerman1992didmf} may arise when MMLU's 57 subjects span distinct latent dimensions; cross-subject matching mitigates between-domain multidimensionality but not within-domain violations. IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric. Additionally, model release dates need not align with training-data cu
…[truncated 144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1284 · 2026-05-23T11:26:41.752602+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1285 · 2026-05-23T11:26:42.155900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1286 · 2026-05-23T11:26:43.110532+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 1287 · 2026-05-23T11:26:43.111759+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-23T11:26:43.162378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1289 · 2026-05-23T11:26:43.664902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1290 · 2026-05-23T11:26:44.071643+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 1291 · 2026-05-23T11:26:44.072474+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1292 · 2026-05-23T11:26:45.029620+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1364
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-23T11:26:45.030910+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-23T11:26:45.031257+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1295 · 2026-05-23T11:26:45.534099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1296 · 2026-05-23T11:26:45.938772+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1297 · 2026-05-23T11:26:45.939227+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1298 · 2026-05-23T11:26:46.039864+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1299 · 2026-05-23T11:26:46.241791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 707
}
```

</details>

---


### Tool call

_source line 1300 · 2026-05-23T11:26:59.746868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1301 · 2026-05-23T11:26:59.747223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1302 · 2026-05-23T11:26:59.747391+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1303 · 2026-05-23T11:26:59.747524+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1304 · 2026-05-23T11:26:59.797918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-23T11:26:59.848491+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1306 · 2026-05-23T11:27:04.018112+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "8-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "8-14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1307 · 2026-05-23T11:27:04.921806+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 563.8}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.4}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 562.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 559.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.6}], \"total_pages\": 18, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1308 · 2026-05-23T11:27:07.180553+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1309 · 2026-05-23T11:27:08.085269+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1310 · 2026-05-23T11:27:08.085864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1311 · 2026-05-23T11:27:08.588282+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1312 · 2026-05-23T11:27:09.093993+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 1313 · 2026-05-23T11:27:09.094444+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1314 · 2026-05-23T11:27:10.000600+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool result

_source line 1315 · 2026-05-23T11:27:10.001441+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1316 · 2026-05-23T11:27:10.152301+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 1317 · 2026-05-23T11:27:10.304285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1318 · 2026-05-23T11:27:11.059118+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool result

_source line 1319 · 2026-05-23T11:27:11.260910+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-23T11:27:17.991784+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "14-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "14-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1321 · 2026-05-23T11:27:18.445909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1322 · 2026-05-23T11:27:18.697541+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.8}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.0}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 381.3}], \"total_pages\": 18, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 705
}
```

</details>

---


### Tool result

_source line 1323 · 2026-05-23T11:27:18.999893+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 30324 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1324 · 2026-05-23T11:27:26.429834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1325 · 2026-05-23T11:27:27.436488+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-23T11:27:28.190024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1327 · 2026-05-23T11:27:28.894735+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 1328 · 2026-05-23T11:27:29.246610+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-23T11:27:29.701380+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1330 · 2026-05-23T11:27:30.105874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-23T11:27:31.515583+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool call

_source line 1332 · 2026-05-23T11:27:32.586341+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1333 · 2026-05-23T11:27:32.989115+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-23T11:28:54.186273+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1335 · 2026-05-23T11:28:54.337794+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1336 · 2026-05-23T11:31:05.249518+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿意见：方法严谨性 + 实验有效性\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel 差异项目功能（DIF）分析迁移到 LLM 基准评测领域，在 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）上发现 2023 与 2024 模型群组之间约 27–29% 的题目存在显著时序 DIF（保守下界 13.5%），远超随机基线（0.62%）。论文提出跨学科匹配（cross-subject matching）策略并给出 ΔFPR=0 的形式化保证，通过半合成注入框架验证检测能力，并在六个 METABENCH 基准上复现。核心发现是 DIF 标记与 web-overlap 污染标签近乎正交（Jaccard=0.206），base 与 instruct 模型呈现相反的 DIF 方向模式。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 将 DIF 引入 LLM 评测是新颖且及时的贡献，实验控制详尽，但 DEFF 估计量选择的论证不够严密、半合成验证的生态效度有限、以及\"检测到 DIF 之后怎么办\"的可操作性不足，使本文处于 Conference 与 Findings 的边界。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论总体严谨，多重控制（随机分割、能力匹配、LOFO、跨基准复现）令人信服；但 DEFF 双估计量差距达 2× 且选择论证有循环性，k>5 时 ΔFPR 保证退化，半合成注入生态效度有限 |\n| Excitement | 3.5/5 | 将心理测量学的 DIF 方法引入 LLM 评测是新颖的跨学科贡献，正交性发现有理论价值；但 DIF 只能检测\"what\"不能回答\"why\"，实际可操作性受限，ρ≈0.997 削弱了实践紧迫性 |\n| Overall Assessment | 3.5/5 | Borderline Conference — 贡献真实但关键方法选择需要更严谨的论证 |\n\n**Confidence**: 4/5 — 对 DIF 方法论和 IRT 在 NLP 中的应用有深入了解，仔细核查了统计论证。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] DEFF 估计量选择的论证存在循环性，且对核心结论影响巨大\n\n- 具体位置：§4.2、§D (App DEFF)、Table 12 (App L: DEFF Simulation)\n- 问题：论文给出两种 DEFF 估计量——simple-mean（C%=29.2%）和 weighted-mean（C%=13.5%），差距达 2.16×。论文推荐 simple-mean 为 primary estimate，理由是\"它与 cluster bootstrap 和 DEFF simulation 收敛\"。但 DEFF simulation（Table 12）的模拟场景本身使用了\"size-dependent ICC matching empirical observations\"——即用观测到的 ICC-size 反相关模式来构造模拟，再用模拟结果论证 simple-mean 更好，形成循环论证。此外，weighted-mean DEFF（Kish, 1965）是 survey sampling 文献中处理不等概率抽样的标准方法，论文将其降格为\"conservative extreme\"但未充分讨论在什么样本结构下 weighted-mean 是更合适的选择。13.5% 仍远超基线，但如果 weighted-mean 是正确的估计量，论文的 headline number（~27-29%）将被大幅下修，叙事的 framing 需要重新调整。\n- 为什么影响接收：论文的核心 claim 是\"~27-29% of items exhibit temporal DIF\"。如果 DEFF 选择改变，这个 headline number 可能需要修改为\"13.5-29.2%\"的区间表述，而非将 simple-mean 作为点估计推荐。\n- 建议修改方向：(1) 明确区分模拟研究的设计假设与待验证的假设，打破循环性；(2) 考虑采用区间表述（如\"13.5-29.2%, with convergent evidence supporting the upper range\"）而非推荐单一估计量；(3) 补充分析：如果使用 weighted-mean DEFF，论文的所有下游分析（排名影响、分数修正）如何变化。\n\n**N2** [critical] 半合成验证框架的生态效度不足，ΔTPR 作为\"detection-power upper bound\"的声称不严密\n\n- 具体位置：§3.4、§4.5、Limitations §(1)\n- 问题：半合成注入使用 uniform binary flipping（将 focal group 的错误回答以固定概率翻转为正确），论文将报告的 ΔTPR 标记为\"detection-power upper bound\"。但这个上界声称缺乏严格论证：(a) 如果真实污染集中在特定难度范围的题目上（如只影响中等难度题目），DIF 信号可能比 uniform flipping 更强而非更弱；(b) difficulty-dependent injection（§4.5）确实产生了较低的 ΔTPR（0.41 vs 0.51），但这只验证了一种特定的非均匀模式，不能穷举所有可能的注入模式；(c) 论文未讨论 partial memorization（模型只记住答案的关键线索而非完整内容）会产生什么样的 DIF 信号——这是现实中最常见的\"污染\"模式。\n- 为什么影响接收：半合成验证是论文方法有效性的关键支撑。如果 ΔTPR 不是真正的上界，那么论文对检测能力的表述需要降级，这影响读者对方法可靠性的判断。\n- 建议修改方向：(1) 将\"upper bound\"改为\"reference point under stylized uniform injection\"；(2) 补充至少一种更接近现实的注入模式（如 partial-credit flipping：只将 focal group 的回答从最不可能的错误选项翻转到正确答案，模拟部分记忆）；(3) 讨论在什么条件下真实污染可能产生比 uniform flipping 更强的 DIF 信号。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] k>5 时 ΔFPR 保证退化的影响未被充分量化\n\n- 具体位置：§3.4 Remark、§4.5、Table 7\n- 问题：跨学科匹配的 ΔFPR=0 保证仅对 single-subject contamination（k≤5）成立。当 k=20（18% of domains）时 ΔFPR 上升至 0.069±0.018。论文在 §4.5 最后一句提到\"worst-case ΔFPR at k=20 (0.069) represents up to 50% of the 13.5% lower bound\"，这意味着如果污染广泛分布且 weighted-mean DEFF 是正确估计，FPR 通胀可能吃掉保守估计的近一半。但论文未系统讨论：在现实场景中，MMLU 57 个学科中有多少可能同时受到污染？如果模型在预训练中接触了大量公开数据，污染可能同时影响多数学科。\n- 建议：(1) 提供关于\"现实中 k 的合理范围\"的论证——例如从 web-overlap 标签分布推断跨学科污染的经验分布；(2) 给出 ΔFPR 对 C% 估计的敏感性分析（如果 7pp 的 FPR 通胀全部转化为 false C flags，adjusted C% 从 X 降至 Y）。\n\n**W2** [warning] DIF 与 web-overlap 正交性的解读存在替代解释\n\n- 具体位置：§4.3、§5.1、Figure 1\n- 问题：enrichment≈1.0（DIF-C 在 web-contaminated 和 web-clean 题目中的比率几乎相同）被解读为\"两个诊断维度互补\"。但还有一个更简单的替代解释：DIF 可能根本不在测量任何与污染相关的东西。如果 DIF 主要反映的是能力演化（capability evolution）或训练方法差异（RLHF/instruction tuning），那么与污染标签正交是自然的——但这削弱了论文将 DIF 定位为\"complementary contamination diagnostic\"的叙事。论文在 §5.1 和 Appendix B 提供了 base/instruct 方向反转和难度-方向交互作为机制证据，但 Appendix B 的 mixed-mechanism injection 未能匹配 instruct 模型的 ρ（模拟 -0.302 vs 观测 -0.079），作者自己也承认\"instruct-model DIF is at least partially driven by non-contamination mechanisms\"。\n- 建议：(1) 更明确地将 DIF 定位为\"measurement instability diagnostic\"而非暗示它与污染互补——正交性发现说明它们是不同的东西，而非互补的工具；(2) 在 Discussion 中更充分地讨论\"DIF 主要反映能力演化而非污染\"这一可能性的含义。\n\n**W3** [warning] ρ≈0.997 的排名保持与 ±800 rank displacement 之间的张力未充分解析\n\n- 具体位置：§4.6、Appendix K\n- 问题：论文同时报告了 ρ≈0.997（几乎完美的排名相关）和 ±800 的极端位移。Appendix K 的分析表明 reversal 集中在 Δrank<50 的\"统计平局\"模型对中（reversal rate 35.2%），>1000 时为 0%。但这个模式是任何噪声源（包括随机移除 31% 的题目）都会产生的。论文报告了 DIF-ordered removal 比 random removal 更快降低 ρ（Figure 6, z=-8 to -49），但未直接报告：随机移除同等数量题目后的 rank displacement 分布是什么？如果随机移除 31% 的题目也产生 ±500 的位移，那么 DIF-specific 的 downstream impact 就大幅缩水。\n- 建议：补充随机移除 31% 题目后的 rank displacement 分布作为基线对比（mean Δ、99th percentile、±800 对应的百分位数），以量化 DIF-specific 的增量影响。\n\n**W4** [warning] 时序群组定义的粒度问题\n\n- 具体位置：§3.3、Limitations\n- 问题：以日历年（2023 vs 2024）划分群组是粗粒度的。模型发布日期 ≠ 训练数据截止日期。2024 年初发布的模型很可能主要使用 2023 年之前的数据训练。论文在 Appendix E 报告了半年度粒度（C%=34.4%），但这进一步模糊而非澄清了信号的时间结构。更重要的是，如果 DIF 主要由训练方法的代际变化（如 RLHF 的普及）驱动，那么\"时序\"标签可能是误导性的——本质上是方法论差异而非时间差异。\n- 建议：(1) 在正文中更明确地讨论 release date vs training cutoff 的混淆；(2) 考虑按训练方法论（base/instruct/RLHF）而非时间划分群组作为补充分析——论文已在 Appendix O-P 提供了 base-only 和 instruct-only 的时序 DIF，这些结果（均 >32%）支持 DIF 不完全由 composition shift 驱动，应在正文中更突出地呈现。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.2 中 ΔFPR=0 的陈述格式为\"Remark\"而非正式的 Proposition/Theorem，但论文在多处将其称为\"formal guarantee\"。建议统一：要么升级为 Proposition 并给出完整证明，要么降低\"formal guarantee\"的措辞。\n- Figure 1 的 ICC 示意图（global vs differential contamination）概念清晰，但右图假设\"only that cohort was disproportionately exposed\"——这是 differential contamination 的定义而非经验发现，存在循环性。Caption 应更明确地标注这是 schematic/definitional illustration。\n- Table 1 的 Within-family (Llama-2 vs 3) C%=61.3% 在能力匹配后收敛到 ~28-29%（Appendix C），这个信息很重要但在正文中不够突出。未经匹配的 61.3% 可能误导读者以为 within-family DIF 远高于 temporal DIF。\n- §4.7 GSM1K 相关性分析（r=-0.478, N=33）过于初步，作为正式结果放在正文中分量不足。建议移至 Appendix 或更明确地标记为 exploratory。\n- Limitations 中提到\"generalizability to open-ended or partial-credit benchmarks is untested\"，但 GSM8K（open-ended）已在 §4.7 中测试且结果一致（C%=18.9%）。这里的表述需要修正——应更精确地说\"partial-credit and free-form generation benchmarks are untested\"。\n\n---\n\n## 主要优势\n\n1. **跨学科方法创新**: 首次将 MH-DIF 系统性地应用于 LLM 基准评测，规模空前（5,227 模型），填补了教育测量和 LLM 评测之间的方法论空白。\n2. **实验控制的深度和广度**: 随机分割基线、能力匹配（NN matching）、LOFO 稳健性、graduated de-duplication、within-architecture 分析、composition control、跨基准复现——每一个潜在混淆变量都被系统地检验和排除。这种控制水平在 LLM 评测领域罕见。\n3. **跨学科匹配的创新**: 将教育测量中的 purified subtest matching 改造为 LLM 多学科设置的 cross-subject matching，并提供形式化的 ΔFPR=0 保证（在 k≤5 条件下），是对方法论的实质性贡献。\n4. **正交性发现的理论价值**: DIF 与 web-overlap 标签的近乎独立性（Jaccard=0.206, φ=0.012）是一个非平凡的经验发现，表明现有的全局污染检测和项目功能差异是不同的维度，具有重要的概念意义。\n5. **Base/instruct 方向反转**: χ²=562.7 的 base/instruct 方向反转提供了强有力的机制分离证据，表明 DIF 反映的是结构化的项目级变化而非均匀的群组效应。\n6. **写作质量**: 论文组织清晰，术语定义严谨（measurement invariance / DIF / temporal score incomparability 的三重区分），附录详实。\n\n---\n\n## Missing References\n\n- Embretson, S.E. & Reise, S.P. (2000). *Item Response Theory for Psychologists*. 作为 IRT 基础参考，论文大量使用 IRT 概念但未引用此经典教材。\n- Suk, Y. & Ryu, W. (2026). *Rethinking differential item functioning from a causal inference perspective*. 论文在 Appendix B 引用了此文（bibkey: suk2026rethinking），但在正文 Discussion 中讨论 DIF 的因果解释局限时未引用——考虑到 DIF\"测 what 不测 why\"是论文的核心局限之一，这篇因果推断视角的 DIF 文献应在正文中讨论。\n- Martinková, P. & Drabinová, A. (2018). *ShinyItemAnalysis for teaching psychometrics and to enforce routine analysis of educational tests*. 作为 DIF 分析的实用工具参考。\n\n---\n\n## Questions for Authors\n\n1. 如果使用 weighted-mean DEFF（C%=13.5%）重新计算所有下游分析（排名影响、分数修正、rank displacement），结果会发生什么定性变化？\n2. 在 web-overlap 标签覆盖的 9,229 个题目中，跨学科的污染分布是什么样的？有多少学科有 >50% 的题目被标记为 web-contaminated？这能帮助约束\"现实中 k 的合理范围\"。\n3. 论文是否考虑过使用 confirmatory DIF 方法（如 IRT-LR 或 MIMIC 模型）作为 MH-DIF 的交叉验证？非均匀 DIF 检测（§4.4: 17.7% additional items）暗示 MH 可能遗漏了重要信号。\n4. Base-only temporal DIF（32.1%）和 instruct-only temporal DIF（36.5%）之间的差异是否在统计上显著？如果 instruct 模型的 DIF 率更高，这对\"DIF 反映能力演化 vs 污染\"的机制讨论有什么含义？\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿意见：方法严谨性 + 实验有效性\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel 差异项目功能（DIF）分析迁移到 LLM 基准评测领域，在 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）上发现 2023 与 2024 模型群组之间约 27–29% 的题目存在显著时序 DIF（保守下界 13.5%），远超随机基线（0.62%）。论文提出跨学科匹配（cross-subject matching）策略并给出 ΔFPR=0 的形式化保证，通过半合成注入框架验证检测能力，并在六个 METABENCH 基准上复现。核心发现是 DIF 标记与 web-overlap 污染标签近乎正交（Jaccard=0.206），base 与 instruct 模型呈现相反的 DIF 方向模式。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 将 DIF 引入 LLM 评测是新颖且及时的贡献，实验控制详尽，但 DEFF 估计量选择的论证不够严密、半合成验证的生态效度有限、以及\"检测到 DIF 之后怎么办\"的可操作性不足，使本文处于 Conference 与 Findings 的边界。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论总体严谨，多重控制（随机分割、能力匹配、LOFO、跨基准复现）令人信服；但 DEFF 双估计量差距达 2× 且选择论证有循环性，k>5 时 ΔFPR 保证退化，半合成注入生态效度有限 |\n| Excitement | 3.5/5 | 将心理测量学的 DIF 方法引入 LLM 评测是新颖的跨学科贡献，正交性发现有理论价值；但 DIF 只能检测\"what\"不能回答\"why\"，实际可操作性受限，ρ≈0.997 削弱了实践紧迫性 |\n| Overall Assessment | 3.5/5 | Borderline Conference — 贡献真实但关键方法选择需要更严谨的论证 |\n\n**Confidence**: 4/5 — 对 DIF 方法论和 IRT 在 NLP 中的应用有深入了解，仔细核查了统计论证。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] DEFF 估计量选择的论证存在循环性，且对核心结论影响巨大\n\n- 具体位置：§4.2、§D (App DEFF)、Table 12 (App L: DEFF Simulation)\n- 问题：论文给出两种 DEFF 估计量——simple-mean（C%=29.2%）和 weighted-mean（C%=13.5%），差距达 2.16×。论文推荐 simple-mean 为 primary estimate，理由是\"它与 cluster bootstrap 和 DEFF simulation 收敛\"。但 DEFF simulation（Table 12）的模拟场景本身使用了\"size-dependent ICC matching empirical observations\"——即用观测到的 ICC-size 反相关模式来构造模拟，再用模拟结果论证 simple-mean 更好，形成循环论证。此外，weighted-mean DEFF（Kish, 1965）是 survey sampling 文献中处理不等概率抽样的标准方法，论文将其降格为\"conservative extreme\"但未充分讨论在什么样本结构下 weighted-mean 是更合适的选择。13.5% 仍远超基线，但如果 weighted-mean 是正确的估计量，论文的 headline number（~27-29%）将被大幅下修，叙事的 framing 需要重新调整。\n- 为什么影响接收：论文的核心 claim 是\"~27-29% of items exhibit temporal DIF\"。如果 DEFF 选择改变，这个 headline number 可能需要修改为\"13.5-29.2%\"的区间表述，而非将 simple-mean 作为点估计推荐。\n- 建议修改方向：(1) 明确区分模拟研究的设计假设与待验证的假设，打破循环性；(2) 考虑采用区间表述（如\"13.5-29.2%, with convergent evidence supporting the upper range\"）而非推荐单一估计量；(3) 补充分析：如果使用 weighted-mean DEFF，论文的所有下游分析（排名影响、分数修正）如何变化。\n\n**N2** [critical] 半合成验证框架的生态效度不足，ΔTPR 作为\"detection-power upper bound\"的声称不严密\n\n- 具体位置：§3.4、§4.5、Limitations §(1)\n- 问题：半合成注入使用 uniform binary flipping（将 focal group 的错误回答以固定概率翻转为正确），论文将报告的 ΔTPR 标记为\"detection-power upper bound\"。但这个上界声称缺乏严格论证：(a) 如果真实污染集中在特定难度范围的题目上（如只影响中等难度题目），DIF 信号可能比 uniform flipping 更强而非更弱；(b) difficulty-dependent injection（§4.5）确实产生了较低的 ΔTPR（0.41 vs 0.51），但这只验证了一种特定的非均匀模式，不能穷举所有可能的注入模式；(c) 论文未讨论 partial memorization（模型只记住答案的关键线索而非完整内容）会产生什么样的 DIF 信号——这是现实中最常见的\"污染\"模式。\n- 为什么影响接收：半合成验证是论文方法有效性的关键支撑。如果 ΔTPR 不是真正的上界，那么论文对检测能力的表述需要降级，这影响读者对方法可靠性的判断。\n- 建议修改方向：(1) 将\"upper bound\"改为\"reference point under stylized uniform injection\"；(2) 补充至少一种更接近现实的注入模式（如 partial-credit flipping：只将 focal group 的回答从最不可能的错误选项翻转到正确答案，模拟部分记忆）；(3) 讨论在什么条件下真实污染可能产生比 uniform flipping 更强的 DIF 信号。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] k>5 时 ΔFPR 保证退化的影响未被充分量化\n\n- 具体位置：§3.4 Remark、§4.5、Table 7\n- 问题：跨学科匹配的 ΔFPR=0 保证仅对 single-subject contamination（k≤5）成立。当 k=20（18% of domains）时 ΔFPR 上升至 0.069±0.018。论文在 §4.5 最后一句提到\"worst-case ΔFPR at k=20 (0.069) represents up to 50% of the 13.5% lower bound\"，这意味着如果污染广泛分布且 weighted-mean DEFF 是正确估计，FPR 通胀可能吃掉保守估计的近一半。但论文未系统讨论：在现实场景中，MMLU 57 个学科中有多少可能同时受到污染？如果模型在预训练中接触了大量公开数据，污染可能同时影响多数学科。\n- 建议：(1) 提供关于\"现实中 k 的合理范围\"的论证——例如从 web-overlap 标签分布推断跨学科污染的经验分布；(2) 给出 ΔFPR 对 C% 估计的敏感性分析（如果 7pp 的 FPR 通胀全部转化为 false C flags，adjusted C% 从 X 降至 Y）。\n\n**W2** [warning] DIF 与 web-overlap 正交性的解读存在替代解释\n\n- 具体位置：§4.3、§5.1、Figure 1\n- 问题：enrichment≈1.0（DIF-C 在 web-contaminated 和 web-clean 题目中的比率几乎相同）被解读为\"两个诊断维度互补\"。但还有一个更简单的替代解释：DIF 可能根本不在测量任何与污染相关的东西。如果 DIF 主要反映的是能力演化（capability evolution）或训练方法差异（RLHF/instruction tuning），那么与污染标签正交是自然的——但这削弱了论文将 DIF 定位为\"complementary contamination diagnostic\"的叙事。论文在 §5.1 和 Appendix B 提供了 base/instruct 方向反转和难度-方向交互作为机制证据，但 Appendix B 的 mixed-mechanism injection 未能匹配 instruct 模型的 ρ（模拟 -0.302 vs 观测 -0.079），作者自己也承认\"instruct-model DIF is at least partially driven by non-contamination mechanisms\"。\n- 建议：(1) 更明确地将 DIF 定位为\"measurement instability diagnostic\"而非暗示它与污染互补——正交性发现说明它们是不同的东西，而非互补的工具；(2) 在 Discussion 中更充分地讨论\"DIF 主要反映能力演化而非污染\"这一可能性的含义。\n\n**W3** [warning] ρ≈0.997 的排名保持与 ±800 rank displacement 之间的张力未充分解析\n\n- 具体位置：§4.6、Appendix K\n- 问题：论文同时报告了 ρ≈0.997（几乎完美的排名相关）和 ±800 的极端位移。Appendix K 的分析表明 reversal 集中在 Δrank<50 的\"统计平局\"模型对中（reversal rate 35.2%），>1000 时为 0%。但这个模式是任何噪声源（包括随机移除 31% 的题目）都会产生的。论文报告了 DIF-ordered removal 比 random removal 更快降低 ρ（Figure 6, z=-8 to -49），但未直接报告：随机移除同等数量题目后的 rank displacement 分布是什么？如果随机移除 31% 的题目也产生 ±500 的位移，那么 DIF-specific 的 downstream impact 就大幅缩水。\n- 建议：补充随机移除 31% 题目后的 rank displacement 分布作为基线对比（mean Δ、99th percentile、±800 对应的百分位数），以量化 DIF-specific 的增量影响。\n\n**W4** [warning] 时序群组定义的粒度问题\n\n- 具体位置：§3.3、Limitations\n- 问题：以日历年（2023 vs 2024）划分群组是粗粒度的。模型发布日期 ≠ 训练数据截止日期。2024 年初发布的模型很可能主要使用 2023 年之前的数据训练。论文在 Appendix E 报告了半年度粒度（C%=34.4%），但这进一步模糊而非澄清了信号的时间结构。更重要的是，如果 DIF 主要由训练方法的代际变化（如 RLHF 的普及）驱动，那么\"时序\"标签可能是误导性的——本质上是方法论差异而非时间差异。\n- 建议：(1) 在正文中更明确地讨论 release date vs training cutoff 的混淆；(2) 考虑按训练方法论（base/instruct/RLHF）而非时间划分群组作为补充分析——论文已在 Appendix O-P 提供了 base-only 和 instruct-only 的时序 DIF，这些结果（均 >32%）支持 DIF 不完全由 composition shift 驱动，应在正文中更突出地呈现。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.2 中 ΔFPR=0 的陈述格式为\"Remark\"而非正式的 Proposition/Theorem，但论文在多处将其称为\"formal guarantee\"。建议统一：要么升级为 Proposition 并给出完整证明，要么降低\"formal guarantee\"的措辞。\n- Figure 1 的 ICC 示意图（global vs differential contamination）概念清晰，但右图假设\"only that cohort was disproportionately exposed\"——这是 differential contamination 的定义而非经验发现，存在循环性。Caption 应更明确地标注这是 schematic/definitional illustration。\n- Table 1 的 Within-family (Llama-2 vs 3) C%=61.3% 在能力匹配后收敛到 ~28-29%（Appendix C），这个信息很重要但在正文中不够突出。未经匹配的 61.3% 可能误导读者以为 within-family DIF 远高于 temporal DIF。\n- §4.7 GSM1K 相关性分析（r=-0.478, N=33）过于初步，作为正式结果放在正文中分量不足。建议移至 Appendix 或更明确地标记为 exploratory。\n- Limitations 中提到\"generalizability to open-ended or partial-credit benchmarks is untested\"，但 GSM8K（open-ended）已在 §4.7 中测试且结果一致（C%=18.9%）。这里的表述需要修正——应更精确地说\"partial-credit and free-form generation benchmarks are untested\"。\n\n---\n\n## 主要优势\n\n1. **跨学科方法创新**: 首次将 MH-DIF 系统性地应用于 LLM 基准评测，规模空前（5,227 模型），填补了教育测量和 LLM 评测之间的方法论空白。\n2. **实验控制的深度和广度**: 随机分割基线、能力匹配（NN matching）、LOFO 稳健性、graduated de-duplication、within-architecture 分析、composition control、跨基准复现——每一个潜在混淆变量都被系统地检验和排除。这种控制水平在 LLM 评测领域罕见。\n3. **跨学科匹配的创新**: 将教育测量中的 purified subtest matching 改造为 LLM 多学科设置的 cross-subject matching，并提供形式化的 ΔFPR=0 保证（在 k≤5 条件下），是对方法论的实质性贡献。\n4. **正交性发现的理论价值**: DIF 与 web-overlap 标签的近乎独立性（Jaccard=0.206, φ=0.012）是一个非平凡的经验发现，表明现有的全局污染检测和项目功能差异是不同的维度，具有重要的概念意义。\n5. **Base/instruct 方向反转**: χ²=562.7 的 base/instruct 方向反转提供了强有力的机制分离证据，表明 DIF 反映的是结构化的项目级变化而非均匀的群组效应。\n6. **写作质量**: 论文组织清晰，术语定义严谨（measurement invariance / DIF / temporal score incomparability 的三重区分），附录详实。\n\n---\n\n## Missing References\n\n- Embretson, S.E. & Reise, S.P. (2000). *Item Response Theory for Psychologists*. 作为 IRT 基础参考，论文大量使用 IRT 概念但未引用此经典教材。\n- Suk, Y. & Ryu, W. (2026). *Rethinking differential item functioning from a causal inference perspective*. 论文在 Appendix B 引用了此文（bibkey: suk2026rethinking），但在正文 Discussion 中讨论 DIF 的因果解释局限时未引用——考虑到 DIF\"测 what 不测 why\"是论文的核心局限之一，这篇因果推断视角的 DIF 文献应在正文中讨论。\n- Martinková, P. & Drabinová, A. (2018). *ShinyItemAnalysis for teaching psychometrics and to enforce routine analysis of educational tests*. 作为 DIF 分析的实用工具参考。\n\n---\n\n## Questions for Authors\n\n1. 如果使用 weighted-mean DEFF（C%=13.5%）重新计算所有下游分析（排名影响、分数修正、rank displacement），结果会发生什么定性变化？\n2. 在 web-overlap 标签覆盖的 9,229 个题目中，跨学科的污染分布是什么样的？有多少学科有 >50% 的题目被标记为 web-contaminated？这能帮助约束\"现实中 k 的合理范围\"。\n3. 论文是否考虑过使用 confirmatory DIF 方法（如 IRT-LR 或 MIMIC 模型）作为 MH-DIF 的交叉验证？非均匀 DIF 检测（§4.4: 17.7% additional items）暗示 MH 可能遗漏了重要信号。\n4. Base-only temporal DIF（32.1%）和 instruct-only temporal DIF（36.5%）之间的差异是否在统计上显著？如果 instruct 模型的 DIF 率更高，这对\"DIF 反映能力演化 vs 污染\"的机制讨论有什么含义？\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-23T11:31:09.773171+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4523
}
```

</details>

---


### Assistant

_source line 1338 · 2026-05-23T11:31:22.188821+00:00_

审稿意见已提交给 Review Director。

**评分摘要**:
- **Overall**: 3.5 (Borderline Conference)
- **Soundness**: 3.5/5
- **Excitement**: 3.5/5
- **Confidence**: 4/5

**2 个 Must-Fix 问题**:
1. DEFF 估计量选择（simple-mean vs weighted-mean，差距 2×）的论证存在循环性——DEFF simulation 用观测到的 ICC-size 模式构造模拟，再用模拟结果论证 simple-mean 更好
2. 半合成验证的 ΔTPR "upper bound" 声称不严密——uniform flipping 不是检测能力的真正上界

**4 个 Should-Fix 问题**:
1. k>5 时 ΔFPR 保证退化的实际影响未量化
2. DIF-contamination 正交性有替代解释（DIF 可能根本不测量污染相关的东西）
3. ρ≈0.997 与 ±800 rank displacement 的张力需要随机移除基线对比
4. 日历年群组定义的粒度和"时序"标签可能是误导性的

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 44

## Round 44

4 recorded events


### User

_source line 1339 · 2026-05-23T11:32:13.832804+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（引用具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

### Must-Fix 问题

**N1** [critical] Mechanism-agnostic 定位与实验设计存在系统性矛盾
- 论文反复声称采取 mechanism-agnostic 立场（Abstract: "without implying degradation or attributing cause"），但实验设计大量围绕 contamination 展开：Section 3.4 注入 contamination、Section 4.3 对比 web-overlap labels、Section 4.5 标题 "Detection Power under Controlled Injection"、Appendix B "Mechanism Analysis"。
- 构成叙事上的自我矛盾：一方面声称不归因，另一方面整个验证体系建立在 contamination 假设之上。

**N2** [critical] Semi-synthetic validation 仅覆盖 uniform injection，与真实 contamination 模式脱节
- 主文的 detection power 数字（TPR 0.68-0.94, AUC 0.93-0.94）基于 uniform injection，可能高估真实场景。
- Difficulty-dependent injection (ΔTPR=0.41 vs uniform 0.51) 在 Appendix B，未在主文充分呈现。

**N3** [critical] 与 Growing Pains (Habba et al., 2026) 的差异化不充分
- Growing Pains 的 anchor item selection 本质上包含 DIF 筛选。论文仅一句话区分，未深入讨论方法论层面差异。
- "to our knowledge, no prior work applies DIF to benchmark temporal comparability" 可能不成立。

### Should-Fix 问题

**W1** MH 方法选择缺乏与替代方法的充分比较（SIBTEST、logistic regression DIF 等）
**W2** 时间粒度选择（年度 cohort）未经论证
**W3** Abstract 信息过载（≥8 个定量发现）
**W4** Jaccard ≈ 0.206 被表述为 "near-independent" 不够精确
**W5** DEFF 校正依赖 IRT 参数但模型拟合不佳

### Overall: 3.5 (Borderline Conference)
### Soundness: 4/5, Excitement: 3/5

---

请逐条回应上述问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-23T11:33:47.283967+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: Mechanism-agnostic 定位与实验设计的\"系统性矛盾\"**\n\nR2 的观察有一定表面合理性，但将其定性为\"系统性矛盾\"过重。论文的逻辑结构是：\n\n1. **核心 DIF 分析本身是 mechanism-agnostic 的**：MH-DIF 仅测试\"题目在两个群组间的功能是否不同\"，不假设任何特定机制。§3.2 的定义、§4.2 的时序 DIF 结果、§4.4 的结构分析——这些核心结果完全不依赖于 contamination 假设。\n\n2. **Semi-synthetic injection 使用 contamination 作为验证工具，而非作为理论前提**：任何检测方法都需要 ground truth 来校准检测能力。Contamination injection 提供了一个可控的、有明确 ground truth 的测试环境。论文在 §3.4 明确说明\"To evaluate whether MH-DIF can detect differential contamination *when it is present*\"——这是验证条件句，不是因果归因。\n\n3. **§4.3 的正交性分析恰恰支持 mechanism-agnostic 立场**：如果论文的叙事建立在 contamination 假设之上，那么与 web-overlap 标签的正交性（enrichment≈1.0）将是负面结果。但论文将其解读为正面发现——DIF 和 contamination labels 是\"complementary diagnostic dimensions\"——这正说明 DIF 不预设 contamination 作为唯一或主要机制。\n\n4. **Appendix B \"Mechanism Analysis\"** 标题确实可能引起误解，但内容是 *exclusion arguments*（排除能力混淆、domain-level improvement、item quality defects 等替代解释），这是标准的科学推理，不构成因果归因。\n\n真正的问题不在于\"矛盾\"，而在于 **叙事框架需要更清晰**：论文应更明确地区分\"DIF 作为诊断工具\"和\"contamination 作为验证手段\"。但这是 framing 问题，不是方法论缺陷。\n\n---\n\n**[AGREE] R2-N2: Semi-synthetic validation 的生态效度有限**\n\n同意。我在自己的审稿意见 N2 中提出了几乎完全一致的关切。补充两点：\n\n1. 论文确实在 Appendix B 提供了 difficulty-dependent injection（ΔTPR=0.41 vs uniform 0.51），但这一更接近现实的结果被放在附录中，主文的检测能力数字（TPR 0.68-0.94）基于 uniform injection，可能给读者造成过于乐观的印象。\n\n2. 更重要的是，如我在 N2 中指出的，\"upper bound\"声称缺乏严格论证——存在特定注入模式（如集中在中等难度题目）可能产生比 uniform 更强 DIF 信号的情况。\n\n建议作者将 difficulty-dependent injection 的结果提升到主文，并将 ΔTPR 标记为\"reference point\"而非\"upper bound\"。\n\n---\n\n**[REBUT] R2-N3: 与 Growing Pains 的差异化不充分**\n\nR2 声称\"Growing Pains 的 anchor item selection 本质上包含 DIF 筛选\"且论文的 novelty claim \"可能不成立\"，但这混淆了两个层面的区别：\n\n1. **方法论差异**：Growing Pains 使用 IRT fixed-parameter calibration（FPC），通过参数化模型（2PL/3PL）检测参数漂移。MH-DIF 是非参数方法，不假设特定 IRT 模型形式。论文在 Appendix A 明确报告\"MMLU response matrix shows poor fit to a unidimensional 2PL model\"——这意味着 FPC 的参数化假设在 MMLU 上可能不成立，而 MH-DIF 不受此限制。这是实质性的方法论差异，不是表面区分。\n\n2. **诊断 vs 矫正的功能定位**：Growing Pains 的目标是 *equating*（跨时间的分数可比性校正），其 anchor item selection 是达成 equating 的工具性步骤。本文的目标是 *diagnosis*（识别哪些题目、多大比例、什么模式出现功能差异），并提供定量严重程度分级（ETS A/B/C）。论文在 §2 Related Work 中明确指出：\"While Growing Pains prescribes how to equate scores after instability is detected, our work diagnoses *which* items exhibit instability and quantifies its magnitude.\"\n\n3. **\"no prior work applies DIF to benchmark temporal comparability\"**：这里的关键词是\"DIF\"——一个有明确定义的心理测量学程序（MH 统计量 + ETS 分类）。FPC 中的参数漂移检测虽然在广义上也检测\"项目不稳定性\"，但它不是 DIF 分析。这个 novelty claim 在严格意义上是成立的。\n\n建议作者在正文中补充 1-2 句话明确对比方法论差异（非参数 vs 参数化、诊断 vs 矫正），但不需要大幅改写。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: MH 方法选择缺乏与替代方法的比较**\n\n论文实际上已提供了多个层面的方法比较：\n\n- §4.4 使用 logistic regression DIF 检测非均匀 DIF，发现额外 17.7% 的题目（union 47%）——这既是对 MH 的补充，也证明了 MH 的保守性（仅检测 uniform DIF）。\n- §4.4 的 IRT θ-conditioning 作为 sensitivity check（r(θ, total score)=0.9986, C%=0.312），验证了 total-score matching 的充分性。\n- §2 Related Work 系统列举了 SIBTEST、Lord's χ²、Raju area method 等替代方法。\n\nMH 是教育测量中使用最广泛的 DIF 方法（论文引用了 Clauser and Mazor 1998 的综述），其选择不需要额外论证。大规模比较所有 DIF 方法超出了本文的范围——本文的贡献是将 DIF 引入 LLM 评测，而非开发新的 DIF 方法。\n\n---\n\n**[AGREE] R2-W2: 时间粒度选择未经论证**\n\n同意，我在 W4 中提出了类似关切。补充：Appendix E 的半年度分析（C%=34.4%）和 Appendix P 的 base-only/instruct-only 分析都提供了有价值的粒度信息，但正文未充分整合。建议作者在 §3.3 或 §5.1 中增加一段讨论 release date vs training cutoff 的混淆以及粒度选择的依据。\n\n---\n\n**[AGREE] R2-W3: Abstract 信息过载**\n\n同意这是一个 presentation issue。Abstract 确实压缩了过多定量发现（C% 范围、DEFF 校正值、Jaccard、φ、ρ、pp 偏移等）。建议精简到 4-5 个核心数字。但这不影响技术评估。\n\n---\n\n**[REBUT] R2-W4: Jaccard≈0.206 作为 \"near-independent\" 不精确**\n\nR2 的关切源于对 Jaccard 指标的误读。论文的\"near-independence\"声称并非仅基于 Jaccard，而是基于一组互补的统计量：\n\n- **φ = 0.012**：Phi 系数是二元变量间关联性的标准度量，0.012 在任何标准下都是 negligible association。\n- **OR = 1.05 [0.96, 1.15]**：95% CI 包含 1.0，无法拒绝独立性。\n- **Permutation null for Jaccard: [0.203, 0.222]**，观测值 0.206 落在 null distribution 内（§4.3: \"within permutation null\"）。\n- **p = 0.88**：关联性检验的 p 值远高于任何显著性阈值。\n\nJaccard=0.206 反映的是两组标记各自覆盖率的 base rate，不是关联强度。给定 ~31% 的 DIF-C rate 和 ~X% 的 web-contamination rate，即使两个标记完全独立，Jaccard 也不会为零。论文提供的 permutation null 正是控制了这一点。\"Near-independent\"在 φ=0.012 + OR CI 包含 1.0 + permutation test 的支持下是充分合理的。\n\n---\n\n**[REBUT] R2-W5: DEFF 校正依赖 IRT 参数但模型拟合不佳**\n\n这是一个事实性错误。DEFF 校正与 IRT 模型参数无关：\n\n- DEFF 使用的是 **ICC（intra-class correlation）**，即组内相关系数——这是一个从原始响应矩阵直接计算的非参数统计量，与 IRT 的 Item Characteristic Curve (ICC) 是完全不同的概念。\n- §D (Appendix DEFF) 定义：DEFF_i = 1 + (m̄ - 1) · ICC_i，其中 ICC_i 是 item i 在 30 个家族上的 one-way random-effects ICC。\n- 论文在 Limitations 中明确指出：\"IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric.\"\n\nR2 可能混淆了 ICC (intra-class correlation) 和 ICC (Item Characteristic Curve)。DEFF 校正完全是非参数的，不受 IRT 模型拟合质量的影响。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: Mechanism-agnostic 定位与实验设计的\"系统性矛盾\"**\n\nR2 的观察有一定表面合理性，但将其定性为\"系统性矛盾\"过重。论文的逻辑结构是：\n\n1. **核心 DIF 分析本身是 mechanism-agnostic 的**：MH-DIF 仅测试\"题目在两个群组间的功能是否不同\"，不假设任何特定机制。§3.2 的定义、§4.2 的时序 DIF 结果、§4.4 的结构分析——这些核心结果完全不依赖于 contamination 假设。\n\n2. **Semi-synthetic injection 使用 contamination 作为验证工具，而非作为理论前提**：任何检测方法都需要 ground truth 来校准检测能力。Contamination injection 提供了一个可控的、有明确 ground truth 的测试环境。论文在 §3.4 明确说明\"To evaluate whether MH-DIF can detect differential contamination *when it is present*\"——这是验证条件句，不是因果归因。\n\n3. **§4.3 的正交性分析恰恰支持 mechanism-agnostic 立场**：如果论文的叙事建立在 contamination 假设之上，那么与 web-overlap 标签的正交性（enrichment≈1.0）将是负面结果。但论文将其解读为正面发现——DIF 和 contamination labels 是\"complementary diagnostic dimensions\"——这正说明 DIF 不预设 contamination 作为唯一或主要机制。\n\n4. **Appendix B \"Mechanism Analysis\"** 标题确实可能引起误解，但内容是 *exclusion arguments*（排除能力混淆、domain-level improvement、item quality defects 等替代解释），这是标准的科学推理，不构成因果归因。\n\n真正的问题不在于\"矛盾\"，而在于 **叙事框架需要更清晰**：论文应更明确地区分\"DIF 作为诊断工具\"和\"contamination 作为验证手段\"。但这是 framing 问题，不是方法论缺陷。\n\n---\n\n**[AGREE] R2-N2: Semi-synthetic validation 的生态效度有限**\n\n同意。我在自己的审稿意见 N2 中提出了几乎完全一致的关切。补充两点：\n\n1. 论文确实在 Appendix B 提供了 difficulty-dependent injection（ΔTPR=0.41 vs uniform 0.51），但这一更接近现实的结果被放在附录中，主文的检测能力数字（TPR 0.68-0.94）基于 uniform injection，可能给读者造成过于乐观的印象。\n\n2. 更重要的是，如我在 N2 中指出的，\"upper bound\"声称缺乏严格论证——存在特定注入模式（如集中在中等难度题目）可能产生比 uniform 更强 DIF 信号的情况。\n\n建议作者将 difficulty-dependent injection 的结果提升到主文，并将 ΔTPR 标记为\"reference point\"而非\"upper bound\"。\n\n---\n\n**[REBUT] R2-N3: 与 Growing Pains 的差异化不充分**\n\nR2 声称\"Growing Pains 的 anchor item selection 本质上包含 DIF 筛选\"且论文的 novelty claim \"可能不成立\"，但这混淆了两个层面的区别：\n\n1. **方法论差异**：Growing Pains 使用 IRT fixed-parameter calibration（FPC），通过参数化模型（2PL/3PL）检测参数漂移。MH-DIF 是非参数方法，不假设特定 IRT 模型形式。论文在 Appendix A 明确报告\"MMLU response matrix shows poor fit to a unidimensional 2PL model\"——这意味着 FPC 的参数化假设在 MMLU 上可能不成立，而 MH-DIF 不受此限制。这是实质性的方法论差异，不是表面区分。\n\n2. **诊断 vs 矫正的功能定位**：Growing Pains 的目标是 *equating*（跨时间的分数可比性校正），其 anchor item selection 是达成 equating 的工具性步骤。本文的目标是 *diagnosis*（识别哪些题目、多大比例、什么模式出现功能差异），并提供定量严重程度分级（ETS A/B/C）。论文在 §2 Related Work 中明确指出：\"While Growing Pains prescribes how to equate scores after instability is detected, our work diagnoses *which* items exhibit instability and quantifies its magnitude.\"\n\n3. **\"no prior work applies DIF to benchmark temporal comparability\"**：这里的关键词是\"DIF\"——一个有明确定义的心理测量学程序（MH 统计量 + ETS 分类）。FPC 中的参数漂移检测虽然在广义上也检测\"项目不稳定性\"，但它不是 DIF 分析。这个 novelty claim 在严格意义上是成立的。\n\n建议作者在正文中补充 1-2 句话明确对比方法论差异（非参数 vs 参数化、诊断 vs 矫正），但不需要大幅改写。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: MH 方法选择缺乏与替代方法的比较**\n\n论文实际上已提供了多个层面的方法比较：\n\n- §4.4 使用 logistic regression DIF 检测非均匀 DIF，发现额外 17.7% 的题目（union 47%）——这既是对 MH 的补充，也证明了 MH 的保守性（仅检测 uniform DIF）。\n- §4.4 的 IRT θ-conditioning 作为 sensitivity check（r(θ, total score)=0.9986, C%=0.312），验证了 total-score matching 的充分性。\n- §2 Related Work 系统列举了 SIBTEST、Lord's χ²、Raju area method 等替代方法。\n\nMH 是教育测量中使用最广泛的 DIF 方法（论文引用了 Clauser and Mazor 1998 的综述），其选择不需要额外论证。大规模比较所有 DIF 方法超出了本文的范围——本文的贡献是将 DIF 引入 LLM 评测，而非开发新的 DIF 方法。\n\n---\n\n**[AGREE] R2-W2: 时间粒度选择未经论证**\n\n同意，我在 W4 中提出了类似关切。补充：Appendix E 的半年度分析（C%=34.4%）和 Appendix P 的 base-only/instruct-only 分析都提供了有价值的粒度信息，但正文未充分整合。建议作者在 §3.3 或 §5.1 中增加一段讨论 release date vs training cutoff 的混淆以及粒度选择的依据。\n\n---\n\n**[AGREE] R2-W3: Abstract 信息过载**\n\n同意这是一个 presentation issue。Abstract 确实压缩了过多定量发现（C% 范围、DEFF 校正值、Jaccard、φ、ρ、pp 偏移等）。建议精简到 4-5 个核心数字。但这不影响技术评估。\n\n---\n\n**[REBUT] R2-W4: Jaccard≈0.206 作为 \"near-independent\" 不精确**\n\nR2 的关切源于对 Jaccard 指标的误读。论文的\"near-independence\"声称并非仅基于 Jaccard，而是基于一组互补的统计量：\n\n- **φ = 0.012**：Phi 系数是二元变量间关联性的标准度量，0.012 在任何标准下都是 negligible association。\n- **OR = 1.05 [0.96, 1.15]**：95% CI 包含 1.0，无法拒绝独立性。\n- **Permutation null for Jaccard: [0.203, 0.222]**，观测值 0.206 落在 null distribution 内（§4.3: \"within permutation null\"）。\n- **p = 0.88**：关联性检验的 p 值远高于任何显著性阈值。\n\nJaccard=0.206 反映的是两组标记各自覆盖率的 base rate，不是关联强度。给定 ~31% 的 DIF-C rate 和 ~X% 的 web-contamination rate，即使两个标记完全独立，Jaccard 也不会为零。论文提供的 permutation null 正是控制了这一点。\"Near-independent\"在 φ=0.012 + OR CI 包含 1.0 + permutation test 的支持下是充分合理的。\n\n---\n\n**[REBUT] R2-W5: DEFF 校正依赖 IRT 参数但模型拟合不佳**\n\n这是一个事实性错误。DEFF 校正与 IRT 模型参数无关：\n\n- DEFF 使用的是 **ICC（intra-class correlation）**，即组内相关系数——这是一个从原始响应矩阵直接计算的非参数统计量，与 IRT 的 Item Characteristic Curve (ICC) 是完全不同的概念。\n- §D (Appendix DEFF) 定义：DEFF_i = 1 + (m̄ - 1) · ICC_i，其中 ICC_i 是 item i 在 30 个家族上的 one-way random-effects ICC。\n- 论文在 Limitations 中明确指出：\"IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric.\"\n\nR2 可能混淆了 ICC (intra-class correlation) 和 ICC (Item Characteristic Curve)。DEFF 校正完全是非参数的，不受 IRT 模型拟合质量的影响。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-23T11:33:51.002188+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3718
}
```

</details>

---


### Assistant

_source line 1342 · 2026-05-23T11:34:00.686112+00:00_

已提交对 Reviewer 2 的逐条回应。

总结：
- **R2-N1**（mechanism-agnostic 矛盾）：[REBUT]——contamination 是验证工具而非理论前提，正交性发现恰好支持 mechanism-agnostic 立场，但 framing 可更清晰
- **R2-N2**（semi-synthetic 生态效度）：[AGREE]——与我自己的 N2 一致
- **R2-N3**（Growing Pains 差异化）：[REBUT]——非参数 vs 参数化、诊断 vs 矫正是实质性差异，novelty claim 成立
- **R2-W1**（方法比较）：[REBUT]——论文已含 logistic regression DIF 和 θ-conditioning
- **R2-W2**（时间粒度）：[AGREE]——与我的 W4 一致
- **R2-W3**（Abstract 过载）：[AGREE]——presentation issue
- **R2-W4**（Jaccard 解读）：[REBUT]——φ=0.012 + OR CI 含 1.0 + permutation test 充分支持 near-independence
- **R2-W5**（DEFF 依赖 IRT）：[REBUT]——事实性错误，ICC (intra-class correlation) ≠ ICC (Item Characteristic Curve)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 45

## Round 45

58 recorded events


### User

_source line 1343 · 2026-05-23T13:59:01.124164+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

## 投稿信息
- **Venue**: EMNLP 2026 (Long Paper, via ARR)
- **Deadline**: 2026-05-25
- **页数限制**: 正文 8 页，参考文献不限，Limitations 不计入页数
- **模板**: ACL (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind
- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`
- **PDF路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/submitted.pdf`

## 论文概述
"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"——将教育测量中的 DIF (Differential Item Functioning) 分析应用于 METABENCH 的 5,227 个 LLM 模型，发现 17.9-31.3% 的 benchmark items 在 2023-2024 cohort 之间表现出 temporal DIF，而 DIF 信号与 web-overlap contamination labels 近乎独立 (Jaccard=0.206)。

## 你的审查侧重

请重点审查以下方面：

1. **MH-DIF 方法的统计严谨性**
   - ETS 阈值（从人类考生校准）直接用于 LLM 是否合理？论文用 random-split P99=1.45 做了经验校准，是否充分？
   - K=5 quintile stratification 的选择是否有充分论证？
   - 多重检验问题：12,508 items 的 multiple testing，ETS dual threshold 是否足够控制 FPR？

2. **DEFF 校正的有效性**
   - Simple-mean vs weighted-mean DEFF 差距 2.16×（29.2% vs 13.5%）。论文给出区间表述，但区间本身是否可靠？
   - Cluster bootstrap CI [26.7%, 53.2%] 排除了 13.5%，论证是否循环？
   - ICC 估计依赖 family 定义，family 边界的敏感性分析是否充分？

3. **Semi-synthetic 注入框架**
   - Uniform binary flipping 的 ecological validity——partial memorization 场景下检测力是否被高估？
   - Cross-subject matching ΔFPR=0 保证在 k≤5 时成立，但 k>5 退化的实际影响？
   - Difficulty-dependent injection (ΔTPR≈0.41 vs 0.51) 是否充分表征了真实场景？

4. **因果推断的边界**
   - Mechanism-agnostic 定位是否一致贯穿全文？有无地方暗示因果关系？
   - Base/instruct direction reversal (χ²=562.7) 的解释力——是否排除了 cohort composition confound？
   - DIF-contamination orthogonality 的两种解释是否平衡呈现？

5. **实验设计与数据**
   - METABENCH 数据集的代表性——全部来自 Open LLM Leaderboard，是否存在 selection bias？
   - Calendar-year cohort boundary 的粗糙性——release date ≠ training cutoff
   - 99.98% decoder-only 的 architecture homogeneity 是否限制了 generalizability？

请按照标准审稿格式输出：Summary → Strengths → Weaknesses (按 severity 排序) → Questions → Missing References → Overall Assessment (含置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1344 · 2026-05-23T13:59:10.628434+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1345 · 2026-05-23T13:59:10.679077+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1346 · 2026-05-23T13:59:14.396836+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1347 · 2026-05-23T13:59:15.452060+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer form dimensions scoring rubric 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer form dimensions scoring rubric 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1348 · 2026-05-23T13:59:17.815949+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/submitted.pdf",
  "pages": "1-10",
  "project": "irt_equated_bench_regen",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/submitted.pdf",
    "pages": "1-10",
    "project": "irt_equated_bench_regen",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1349 · 2026-05-23T13:59:21.387839+00:00_

Web search results for query: "ACL Rolling Review reviewer form dimensions scoring rubric 2025 2026"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"}]

Based on the search results, here is information about the ACL Rolling Review (ARR) reviewer form and scoring rubric for 2025-2026:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overal
…[truncated 1175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5935
}
```

</details>

---


### Tool result

_source line 1350 · 2026-05-23T13:59:22.142948+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also
…[truncated 1365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7746
}
```

</details>

---


### Tool result

_source line 1351 · 2026-05-23T13:59:24.358660+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 586.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p9.png\", \"width\": 1
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6542
}
```

</details>

---


### Tool call

_source line 1352 · 2026-05-23T13:59:33.700080+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all dimensions, scoring scales, descriptions for each score level, and any instructions for reviewers. Include soundness, excitement, overall assessment scales with all possible values."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all dimensions, scoring scales, descriptions for each score level, and any instructions for reviewers. Include soundness, excitement, overall assessment scales with all possible values."
  }
}
```

</details>

---


### Tool call

_source line 1353 · 2026-05-23T13:59:35.076661+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should focus on, how to evaluate soundness, excitement, reproducibility, ethics, limitations. Include any specific instructions about how to write reviews, what constitutes a good review, and scoring guidance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: what reviewers should focus on, how to evaluate soundness, excitement, reproducibility, ethics, limitations. Include any specific instructions about how to write reviews, what constitutes a good review, and scoring guidance."
  }
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-23T13:59:35.933894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1355 · 2026-05-23T13:59:36.436912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1356 · 2026-05-23T13:59:36.943555+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 1357 · 2026-05-23T13:59:36.947170+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1358 · 2026-05-23T13:59:37.853161+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1416
}
```

</details>

---


### Tool result

_source line 1359 · 2026-05-23T13:59:37.855021+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1360 · 2026-05-23T13:59:37.855416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1361 · 2026-05-23T13:59:38.359589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1362 · 2026-05-23T13:59:38.767793+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 1363 · 2026-05-23T13:59:38.768304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1364 · 2026-05-23T13:59:39.777331+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1417
}
```

</details>

---


### Tool call

_source line 1365 · 2026-05-23T13:59:39.778956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-23T13:59:40.132596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1367 · 2026-05-23T13:59:40.688239+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1919
}
```

</details>

---


### Tool result

_source line 1368 · 2026-05-23T13:59:41.392045+00:00_

# ACL Rolling Review Form - Complete Structure

## Core Review Dimensions

**1. Paper Summary**
Brief description of paper topic and content for action editors and area chairs.

**2. Summary of Strengths**
Focus on reasons for publication: "novel and useful methodology, insightful empirical results or theoretical analysis, clear organization."

**3. Summary of Weaknesses**
Numbered concerns including correctness, impact, clarity, and exposition quality.

**4. Comments/Suggestions/Typos**
Additional improvement suggestions beyond main concerns.

## Scoring Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: Positive evaluation; very careful reading and familiar with related work
- 4: Quite sure; important points checked carefully
- 3: Pretty sure; general area knowledge but limited detailed verification
- 2: Willing to defend but likely missed details or novelty assessment
- 1: Outside expertise area or paper very difficult to understand

**Soundness** (1-5 with half-points)
- 5: Excellent; thorough study for its type
- 4: Strong; sufficient support for claims
- 3: Acceptable; main claims supported with minor gaps
- 2: Poor; main claims insufficiently supported
- 1: Major issues; not publication-ready

**Excitement** (1-5 with half-points)
Subjective assessment of innovation, impact, and relevance potential.
- 5: Highly exciting; would recommend widely
- 4: Exciting; would mention to others
- 3: Interesting; might mention selectively
- 2: Potentially interesting to some community members
- 1: Not exciting; limited relevance to ACL community

**Overall Assessment** (1-5 with half-points)
- 5: Award consideration (top 2.5%)
- 4: Conference acceptance
- 3: Accept to Findings track
- 2: Resubmit next cycle
- 1: Do not resubmit

## Additional Evaluation Areas

- **Best Paper Justification**: Required for award/borderline-award recommendations
- **Limitations and Societal Impact**: Assessment of author disclosure regarding potential harms
- **Ethical Concerns**: Review ag
…[truncated 355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7691
}
```

</details>

---


### Tool result

_source line 1369 · 2026-05-23T13:59:41.444396+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1665
}
```

</details>

---


### Tool result

_source line 1370 · 2026-05-23T13:59:41.646097+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1513
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-23T13:59:53.473191+00:00_

# ARR Reviewer Guidelines Summary

## Core Review Tasks

Reviewers complete four main tasks:
1. **Allocate time** for reviewing and discussion periods
2. **Check assignments** for expertise, conflicts of interest, and desk-rejection criteria
3. **Write a strong review** with sound methodology assessment
4. **Update after author response** and engage in discussion

## Writing a Strong Review

### Reading Strategy
Read papers twice: first a skim to adjust expectations without looking at results, then in-depth evaluation. "Hindsight bias may make things seem obvious in retrospect" and confirmation bias can distort judgment. Search for related work *after* forming initial impressions to avoid discovering author identities.

### Specificity Requirements
Reviews must be concrete. Rather than stating "missing relevant references," specify which ones. Instead of "X is not clear," explain what information about X is absent. This allows area chairs to understand concerns without reading the full paper.

### Avoiding Common Reviewer Mistakes
Watch for these problematic patterns:

- Dismissing work as "unsurprising" when findings haven't been empirically tested
- Rejecting papers for lacking novelty without providing references to similar work
- Demanding SOTA results when papers contribute through other dimensions (efficiency, interpretability, fairness)
- Criticizing negative results, which serve important scientific functions
- Labeling methods "too simple" when simplicity aids real-world deployment
- Requesting experiments beyond what claims require

### NLP-Specific Issues to Flag

**Methodology concerns:**
- LLM evaluators used without validation in that specific context
- Insufficient reproducibility details or unclear code/data availability
- Undisclosed data quality problems
- Unmotivated selection of models or benchmarks
- Incomplete proofs or unstated assumptions

**Results issues:**
- Inappropriate statistics or p-hacking
- Claims exceeding what evidence supports
- 
…[truncated 3794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 18396
}
```

</details>

---


### Tool call

_source line 1372 · 2026-05-23T14:00:00.249313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1373 · 2026-05-23T14:00:01.724523+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1475
}
```

</details>

---


### Tool call

_source line 1374 · 2026-05-23T14:00:01.775905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-23T14:00:02.732579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-23T14:00:02.833486+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/submitted.pdf",
  "pages": "11-18",
  "project": "irt_equated_bench_regen",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/submitted.pdf",
    "pages": "11-18",
    "project": "irt_equated_bench_regen",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1377 · 2026-05-23T14:00:04.341562+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 574.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 567.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 446.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.1}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 430.8}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 434.7}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/art
…[truncated 75 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1508
}
```

</details>

---


### Tool call

_source line 1378 · 2026-05-23T14:00:07.511925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1379 · 2026-05-23T14:00:08.067212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1380 · 2026-05-23T14:00:08.921954+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-23T14:00:08.922994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-23T14:00:09.023797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1383 · 2026-05-23T14:00:09.425865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1384 · 2026-05-23T14:00:09.930674+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1385 · 2026-05-23T14:00:09.931142+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1386 · 2026-05-23T14:00:10.787321+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-23T14:00:10.788577+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 1388 · 2026-05-23T14:00:10.788996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1389 · 2026-05-23T14:00:11.291694+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1390 · 2026-05-23T14:00:11.797239+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool result

_source line 1391 · 2026-05-23T14:00:11.801387+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 509
}
```

</details>

---


### Tool call

_source line 1392 · 2026-05-23T14:00:11.801908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1393 · 2026-05-23T14:00:12.405631+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1394 · 2026-05-23T14:07:55.846216+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 方法严谨性审查报告\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 将 MH-DIF 应用于 5,227 LLMs 的大规模 psychometric audit 方法论基本可靠，cross-subject matching 是有价值的方法论贡献，但 DEFF 校正的 2.16× 不确定性范围、半合成注入框架的生态效度不足、以及缺少 DIF 文献中 impact/bias 关键区分是三个影响接收决定的方法论缺陷。\n\n## 官方维度打分（ACL ARR review form, Feb 2025+）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | MH-DIF 应用正确，cross-subject matching 有方法论贡献，但 DEFF 估计范围过宽（13.5%–29.2%）且半合成验证生态效度不足 |\n| Excitement | 3.5/5 | DIF 与 contamination 近正交（Jaccard=0.206）的发现有重要意义，但实践可操作性尚需更多论证 |\n| Reproducibility | 4/5 | 使用公开数据集 METABENCH，方法描述详尽，代码脚本声明可用 |\n| Confidence | 4/5 | 对统计方法论和 psychometrics 有充分了解，仔细阅读了正文和全部 18 页附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] DEFF 校正产生 2.16× 估计范围，论文未提供充分的分辨依据\n- 具体位置：Section D (Appendix, p.15)；正文 Section 4.2 (p.6) 报告 \"13.5–29.2%\"\n- 问题：Simple-mean DEFF (3.58) 给出 C% = 29.2%，weighted-mean DEFF (12.29) 给出 C% = 13.5%——差距超过 2 倍。论文将两者作为 \"bracket\" 呈现，但未提供在此区间内定位的原则性依据。Cluster bootstrap 95% CI [26.7%, 53.2%] 被用来排除 13.5% 下界，但 bootstrap 仅对约 30 个 family 重采样（其中 Mistral n=547、Llama-3 n=315 占据主导），有效独立重采样单元极少。论文自己也承认 \"extreme bootstrap upper bound (53.2%) is driven by extreme bootstrap resamples that over-represent Mistral or Llama-3\"（p.16），这意味着 bootstrap 分布受少数 mega-family 驱动，推断可靠性存疑。\n- 为什么影响接收：论文核心定量发现是 \"17.9–31.3% of items exhibit temporal DIF\"（Abstract, Conclusion 均引用此数字）。如果实际值接近 13.5%（weighted-mean），DIF 的规模和实践影响将大幅缩水，\"Correct\" 步骤移除的 item 数量和 rescoring 幅度也会显著不同。\n- 建议修改方向：(1) 对 family 定义进行 sensitivity analysis——用更细粒度的分组（如 fine-tune chain、base model version）和更粗粒度的分组分别估计 DEFF，展示 C% 对 family 粒度的敏感性曲线；(2) 报告 block bootstrap with varying block size 或 jackknife-after-bootstrap 结果，评估 cluster bootstrap CI 本身的稳定性；(3) 如果无法缩窄区间，至少应在正文 Discussion 中充分讨论这一不确定性的实践含义，而非仅在 Appendix D 中处理。\n\n**N2** [critical] 半合成注入框架使用 uniform binary flipping，检测力估计可能被系统性高估\n- 具体位置：Section 3.4 (p.5)；Section 4.5 (p.7)；Limitations (p.9)\n- 问题：注入框架将 \"contamination\" 操作化为二元翻转（incorrect → correct），产生最大化的 per-item DIF effect size。现实中 contamination 更可能表现为 graded probability shift（partial memorization：模型对见过的题目正确率从 0.4 提高到 0.7，而非从 0 跳到 1）。论文报告的 ΔTPR = 0.371（MMLU，Section 4.5）代表 binary-flip 下的 best-case 检测力。虽然 Scheme D（difficulty-dependent injection）展示了 ΔTPR 从 0.51 降至约 0.41，但这仍是 binary flipping 的变体（仅 injection rate 随 difficulty 变化），未测试 graded probability shift 场景。Limitations（p.9）正确承认了这一点但未量化影响。\n- 为什么影响接收：论文第二个核心贡献（cross-subject matching with constructive ΔFPR=0 guarantee）和实践建议（Section 5.2 Monitor/Triage/Correct 协议）的可行性都取决于有足够的检测力。如果 graded injection 下 ΔTPR 降至 0.1–0.2 级别，审计框架的实际可用性将大打折扣。\n- 建议修改方向：(1) 增加 graded injection scheme：将 p(correct) 从 baseline 提升 Δp ∈ {0.1, 0.2, 0.3}，而非 binary flip，报告不同 Δp 下的 ΔTPR 曲线和 \"minimum detectable probability shift\"；(2) 若实验资源不足，至少用数学推导估计 graded shift 对 MH odds ratio 的影响幅度，提供 analytical bound。\n\n**N3** [critical] 缺少 DIF 文献中的 \"impact vs. bias\" 关键区分，威胁 \"Correct\" 步骤的方法论基础\n- 具体位置：Section 5.2 (p.8)；Section M (p.18, score inflation analysis)\n- 问题：DIF 文献（Camilli & Shepard, 1994; Zumbo, 1999; Penfield & Camilli, 2007）明确区分 DIF（统计发现：能力匹配后 item 在组间表现不同）和 item bias（实质性判断：差异由 construct-irrelevant 因素导致）。DIF 是 bias 的必要但非充分条件。如果 2024 models 在特定推理能力上有真实进步，导致特定 items 上的 performance shift，这属于 \"impact\"（construct-relevant differential functioning），移除这些 items 反而会降低 benchmark 对真实能力差异的敏感度。论文的 \"Correct\" 步骤（Section 5.2）直接建议 \"removing ETS C items and rescoring\"，Section M 报告 \"+2.12 pp\" score shift，但未区分 impact-driven vs. bias-driven DIF items。论文自己在 Section B (Appendix) 承认 \"capability evolution\" 是三个可能机制之一——如果部分 DIF 确实由 capability evolution 驱动，indiscriminate removal 在方法论上不成立。\n- 为什么影响接收：这不仅是讨论层面的缺失，而是论文方法论框架的内在一致性问题。一方面声称 \"mechanism-agnostic\"，另一方面建议无差别移除 DIF items——两者逻辑冲突。\n- 建议修改方向：(1) 在 Section 5.2 引入 impact/bias 区分，讨论 Triage 步骤应如何 operationalize（例如：DIF 方向与 domain-specific ability gain 一致时可能是 impact，与 web-overlap 一致时更可能是 bias）；(2) 在 Section M 中分别报告 impact-candidate 和 bias-candidate items 的 rescoring 效应；(3) 引用 DIF 文献中的标准做法：DIF detection → expert content review → bias determination → removal decision，而非跳过中间步骤。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Calendar-year cohort boundary 过于粗糙\n- 具体位置：Section 3.3 (p.5)；Limitations (p.9)\n- 问题：以 calendar year（2023 vs 2024）划分 cohort，但 release date ≠ training data cutoff。2024 年初发布的模型可能使用 2022 年的训练数据。Appendix（p.16）的 half-year granularity 分析（31.3% annual vs 34.1% half-year）仅提供了有限额外信息。\n- 建议：(1) 对有 training cutoff 元数据的子集进行 sensitivity analysis；(2) 报告 quarterly cohort 的 C% 趋势以验证 temporal monotonicity。\n\n**W2** [warning] Cross-subject matching ΔFPR=0 保证在高覆盖率 contamination 下的退化未充分讨论\n- 具体位置：Section 4.5 (p.7)；Table 7\n- 问题：ΔFPR=0 保证仅在 k≤5 科目同时被 contaminate 时严格成立。k=10 时 ΔFPR=0.012–0.018，k=20 时 ΔFPR=0.062。论文正文称 \"worst-case multi-subject inflation (~7 pp) cannot account for the observed 31% C% rate\"，但此论证将 worst-case per-item FPR 与 aggregate C% 对比，未考虑在 \"realistic web contamination coverage\"（可能影响 30+ 科目）下的累积效应。\n- 建议：模拟在 k=30（~53% 科目）甚至 k=50 时的 ΔFPR，并讨论是否改变定性结论。\n\n**W3** [warning] Mechanism-agnostic 定位与 contamination-heavy 叙事存在张力\n- 具体位置：Section 1 (p.1-2)；Section 4.3 (p.6-7)；Section 5.1 (p.8)；Figure 1\n- 问题：论文明确宣称 \"mechanism-agnostic\"（Section 5.1: \"Temporal DIF detects that items function differently across cohorts, not why\"），但叙事结构大量围绕 contamination 展开：Related Work 以 \"Contamination Detection\" 开篇，Figure 1 左图标注 \"global contamination\"，Section 4.3 整节做 DIF-contamination 对比。这种张力可能让读者误读为 \"DIF 是更好的 contamination detector\"，与论文实际贡献（measurement invariance diagnostic）不一致。\n- 建议：将 contamination 对比重新框定为 \"discriminant validity evidence\"（证明 DIF 度量的构念不同于 contamination），而非暗示两者在同一维度上竞争。\n\n**W4** [warning] METABENCH 数据的 selection bias 未充分讨论\n- 具体位置：Section 3.1 (p.4)\n- 问题：所有 5,227 模型来自 Open LLM Leaderboard，存在自选择偏差（只有主动提交的模型被收录）、teaching-to-the-test 效应（Leaderboard 公开后可能诱导针对性训练）、以及 family-level over-representation（某些 family 大量提交微调变体）。DEFF 校正处理了非独立性，但 selection bias 本身未讨论。\n- 建议：在 Limitations 中讨论 Leaderboard selection bias 的方向和预期影响。\n\n---\n\n## 小问题（不影响接收）\n- Abstract \"≤22% benchmarks show above-baseline DIF flags\" 表述模糊，建议用 \"5 of 6 benchmarks\" 或具体比例\n- Table 3 (p.8) HellaSwag 的 Enrichment 标 \"–\"，原因是 Li et al. (2024b) 未覆盖——建议脚注说明\n- Figure 2 (p.7) y 轴标签 \"True Positive Rate (Power)\" 建议统一用 \"Detection Power (TPR)\" 以匹配正文术语\n\n---\n\n## Questions for Authors\n1. 如果用 graded probability injection（Δp=0.2 而非 binary flip），ΔTPR 预期会下降到什么水平？是否做过任何 pilot 实验或 analytical estimation？\n2. DEFF 的 family 定义是如何确定的？是否考虑过用 model card 中的 base model 字段构建更细粒度的 fine-tune chain 谱系？如果用 50 个 sub-family 而非 30 个 family，DEFF 会如何变化？\n3. Section M 中移除 DIF-C items 后 score shift = +2.12 pp——这意味着 2024 cohort 在 DIF-corrected 后得分更高。但如果 contamination 是主要机制，我们预期移除 contaminated items 后 2024 得分应该下降。论文如何调和这一方向性矛盾？\n4. 论文是否能区分 \"legitimately harder items for 2024 models\"（因为 training methodology shift 导致某些能力退化）和 \"construct-irrelevant DIF\"？如果不能，\"Correct\" 步骤的实践建议是否过于简化？\n\n---\n\n## Missing References\n- Camilli, G. & Shepard, L. A. (1994). *Methods for Identifying Biased Test Items*. Sage. ——DIF 与 item bias 的经典区分框架\n- Penfield, R. D. & Camilli, G. (2007). Differential item functioning and item bias. In *Handbook of Statistics* (Vol. 26). ——impact vs. bias 的方法论框架\n- （论文已引用 Millsap 2011、Zumbo 1999，但未利用其中的 impact/bias 区分来支撑 Section 5.2 的实践建议）\n\n---\n\n## 主要优势\n- **S1 规模与系统性**：5,227 模型 × 12,508 items 的全量 psychometric audit，据我所知是 LLM 评估领域最大规模的此类分析\n- **S2 Cross-subject matching 是真正的方法论贡献**：ΔFPR=0 的构造性保证（k≤5）为 DIF 在多科目 benchmark 上的应用提供了可靠的 FPR 控制，这是对标准 MH-DIF 流程的有价值扩展\n- **S3 DIF ⊥ contamination 的发现有重要理论意义**：Jaccard=0.206 表明这两种 diagnostic 维度近正交，挑战了将 item-level anomaly 简单归因于 contamination 的普遍直觉\n- **S4 内部一致性控制设计得当**：random-split baseline (0.62% C%)、ability-quintile check (2.9%)、half-year granularity、composition control（Appendix P：30.25% vs 31.3%，仅 1.08 pp 差异）构成多层次 null-hypothesis 校验\n- **S5 Base/instruct 方向反转 (χ²=562.7) 提供 mechanism separation 的强证据**：base models 60.1% reference-favoring vs instruct models 69.6% focal-favoring，有效排除了 DIF 纯粹由单一机制驱动的假设",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 方法严谨性审查报告\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 将 MH-DIF 应用于 5,227 LLMs 的大规模 psychometric audit 方法论基本可靠，cross-subject matching 是有价值的方法论贡献，但 DEFF 校正的 2.16× 不确定性范围、半合成注入框架的生态效度不足、以及缺少 DIF 文献中 impact/bias 关键区分是三个影响接收决定的方法论缺陷。\n\n## 官方维度打分（ACL ARR review form, Feb 2025+）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | MH-DIF 应用正确，cross-subject matching 有方法论贡献，但 DEFF 估计范围过宽（13.5%–29.2%）且半合成验证生态效度不足 |\n| Excitement | 3.5/5 | DIF 与 contamination 近正交（Jaccard=0.206）的发现有重要意义，但实践可操作性尚需更多论证 |\n| Reproducibility | 4/5 | 使用公开数据集 METABENCH，方法描述详尽，代码脚本声明可用 |\n| Confidence | 4/5 | 对统计方法论和 psychometrics 有充分了解，仔细阅读了正文和全部 18 页附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] DEFF 校正产生 2.16× 估计范围，论文未提供充分的分辨依据\n- 具体位置：Section D (Appendix, p.15)；正文 Section 4.2 (p.6) 报告 \"13.5–29.2%\"\n- 问题：Simple-mean DEFF (3.58) 给出 C% = 29.2%，weighted-mean DEFF (12.29) 给出 C% = 13.5%——差距超过 2 倍。论文将两者作为 \"bracket\" 呈现，但未提供在此区间内定位的原则性依据。Cluster bootstrap 95% CI [26.7%, 53.2%] 被用来排除 13.5% 下界，但 bootstrap 仅对约 30 个 family 重采样（其中 Mistral n=547、Llama-3 n=315 占据主导），有效独立重采样单元极少。论文自己也承认 \"extreme bootstrap upper bound (53.2%) is driven by extreme bootstrap resamples that over-represent Mistral or Llama-3\"（p.16），这意味着 bootstrap 分布受少数 mega-family 驱动，推断可靠性存疑。\n- 为什么影响接收：论文核心定量发现是 \"17.9–31.3% of items exhibit temporal DIF\"（Abstract, Conclusion 均引用此数字）。如果实际值接近 13.5%（weighted-mean），DIF 的规模和实践影响将大幅缩水，\"Correct\" 步骤移除的 item 数量和 rescoring 幅度也会显著不同。\n- 建议修改方向：(1) 对 family 定义进行 sensitivity analysis——用更细粒度的分组（如 fine-tune chain、base model version）和更粗粒度的分组分别估计 DEFF，展示 C% 对 family 粒度的敏感性曲线；(2) 报告 block bootstrap with varying block size 或 jackknife-after-bootstrap 结果，评估 cluster bootstrap CI 本身的稳定性；(3) 如果无法缩窄区间，至少应在正文 Discussion 中充分讨论这一不确定性的实践含义，而非仅在 Appendix D 中处理。\n\n**N2** [critical] 半合成注入框架使用 uniform binary flipping，检测力估计可能被系统性高估\n- 具体位置：Section 3.4 (p.5)；Section 4.5 (p.7)；Limitations (p.9)\n- 问题：注入框架将 \"contamination\" 操作化为二元翻转（incorrect → correct），产生最大化的 per-item DIF effect size。现实中 contamination 更可能表现为 graded probability shift（partial memorization：模型对见过的题目正确率从 0.4 提高到 0.7，而非从 0 跳到 1）。论文报告的 ΔTPR = 0.371（MMLU，Section 4.5）代表 binary-flip 下的 best-case 检测力。虽然 Scheme D（difficulty-dependent injection）展示了 ΔTPR 从 0.51 降至约 0.41，但这仍是 binary flipping 的变体（仅 injection rate 随 difficulty 变化），未测试 graded probability shift 场景。Limitations（p.9）正确承认了这一点但未量化影响。\n- 为什么影响接收：论文第二个核心贡献（cross-subject matching with constructive ΔFPR=0 guarantee）和实践建议（Section 5.2 Monitor/Triage/Correct 协议）的可行性都取决于有足够的检测力。如果 graded injection 下 ΔTPR 降至 0.1–0.2 级别，审计框架的实际可用性将大打折扣。\n- 建议修改方向：(1) 增加 graded injection scheme：将 p(correct) 从 baseline 提升 Δp ∈ {0.1, 0.2, 0.3}，而非 binary flip，报告不同 Δp 下的 ΔTPR 曲线和 \"minimum detectable probability shift\"；(2) 若实验资源不足，至少用数学推导估计 graded shift 对 MH odds ratio 的影响幅度，提供 analytical bound。\n\n**N3** [critical] 缺少 DIF 文献中的 \"impact vs. bias\" 关键区分，威胁 \"Correct\" 步骤的方法论基础\n- 具体位置：Section 5.2 (p.8)；Section M (p.18, score inflation analysis)\n- 问题：DIF 文献（Camilli & Shepard, 1994; Zumbo, 1999; Penfield & Camilli, 2007）明确区分 DIF（统计发现：能力匹配后 item 在组间表现不同）和 item bias（实质性判断：差异由 construct-irrelevant 因素导致）。DIF 是 bias 的必要但非充分条件。如果 2024 models 在特定推理能力上有真实进步，导致特定 items 上的 performance shift，这属于 \"impact\"（construct-relevant differential functioning），移除这些 items 反而会降低 benchmark 对真实能力差异的敏感度。论文的 \"Correct\" 步骤（Section 5.2）直接建议 \"removing ETS C items and rescoring\"，Section M 报告 \"+2.12 pp\" score shift，但未区分 impact-driven vs. bias-driven DIF items。论文自己在 Section B (Appendix) 承认 \"capability evolution\" 是三个可能机制之一——如果部分 DIF 确实由 capability evolution 驱动，indiscriminate removal 在方法论上不成立。\n- 为什么影响接收：这不仅是讨论层面的缺失，而是论文方法论框架的内在一致性问题。一方面声称 \"mechanism-agnostic\"，另一方面建议无差别移除 DIF items——两者逻辑冲突。\n- 建议修改方向：(1) 在 Section 5.2 引入 impact/bias 区分，讨论 Triage 步骤应如何 operationalize（例如：DIF 方向与 domain-specific ability gain 一致时可能是 impact，与 web-overlap 一致时更可能是 bias）；(2) 在 Section M 中分别报告 impact-candidate 和 bias-candidate items 的 rescoring 效应；(3) 引用 DIF 文献中的标准做法：DIF detection → expert content review → bias determination → removal decision，而非跳过中间步骤。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Calendar-year cohort boundary 过于粗糙\n- 具体位置：Section 3.3 (p.5)；Limitations (p.9)\n- 问题：以 calendar year（2023 vs 2024）划分 cohort，但 release date ≠ training data cutoff。2024 年初发布的模型可能使用 2022 年的训练数据。Appendix（p.16）的 half-year granularity 分析（31.3% annual vs 34.1% half-year）仅提供了有限额外信息。\n- 建议：(1) 对有 training cutoff 元数据的子集进行 sensitivity analysis；(2) 报告 quarterly cohort 的 C% 趋势以验证 temporal monotonicity。\n\n**W2** [warning] Cross-subject matching ΔFPR=0 保证在高覆盖率 contamination 下的退化未充分讨论\n- 具体位置：Section 4.5 (p.7)；Table 7\n- 问题：ΔFPR=0 保证仅在 k≤5 科目同时被 contaminate 时严格成立。k=10 时 ΔFPR=0.012–0.018，k=20 时 ΔFPR=0.062。论文正文称 \"worst-case multi-subject inflation (~7 pp) cannot account for the observed 31% C% rate\"，但此论证将 worst-case per-item FPR 与 aggregate C% 对比，未考虑在 \"realistic web contamination coverage\"（可能影响 30+ 科目）下的累积效应。\n- 建议：模拟在 k=30（~53% 科目）甚至 k=50 时的 ΔFPR，并讨论是否改变定性结论。\n\n**W3** [warning] Mechanism-agnostic 定位与 contamination-heavy 叙事存在张力\n- 具体位置：Section 1 (p.1-2)；Section 4.3 (p.6-7)；Section 5.1 (p.8)；Figure 1\n- 问题：论文明确宣称 \"mechanism-agnostic\"（Section 5.1: \"Temporal DIF detects that items function differently across cohorts, not why\"），但叙事结构大量围绕 contamination 展开：Related Work 以 \"Contamination Detection\" 开篇，Figure 1 左图标注 \"global contamination\"，Section 4.3 整节做 DIF-contamination 对比。这种张力可能让读者误读为 \"DIF 是更好的 contamination detector\"，与论文实际贡献（measurement invariance diagnostic）不一致。\n- 建议：将 contamination 对比重新框定为 \"discriminant validity evidence\"（证明 DIF 度量的构念不同于 contamination），而非暗示两者在同一维度上竞争。\n\n**W4** [warning] METABENCH 数据的 selection bias 未充分讨论\n- 具体位置：Section 3.1 (p.4)\n- 问题：所有 5,227 模型来自 Open LLM Leaderboard，存在自选择偏差（只有主动提交的模型被收录）、teaching-to-the-test 效应（Leaderboard 公开后可能诱导针对性训练）、以及 family-level over-representation（某些 family 大量提交微调变体）。DEFF 校正处理了非独立性，但 selection bias 本身未讨论。\n- 建议：在 Limitations 中讨论 Leaderboard selection bias 的方向和预期影响。\n\n---\n\n## 小问题（不影响接收）\n- Abstract \"≤22% benchmarks show above-baseline DIF flags\" 表述模糊，建议用 \"5 of 6 benchmarks\" 或具体比例\n- Table 3 (p.8) HellaSwag 的 Enrichment 标 \"–\"，原因是 Li et al. (2024b) 未覆盖——建议脚注说明\n- Figure 2 (p.7) y 轴标签 \"True Positive Rate (Power)\" 建议统一用 \"Detection Power (TPR)\" 以匹配正文术语\n\n---\n\n## Questions for Authors\n1. 如果用 graded probability injection（Δp=0.2 而非 binary flip），ΔTPR 预期会下降到什么水平？是否做过任何 pilot 实验或 analytical estimation？\n2. DEFF 的 family 定义是如何确定的？是否考虑过用 model card 中的 base model 字段构建更细粒度的 fine-tune chain 谱系？如果用 50 个 sub-family 而非 30 个 family，DEFF 会如何变化？\n3. Section M 中移除 DIF-C items 后 score shift = +2.12 pp——这意味着 2024 cohort 在 DIF-corrected 后得分更高。但如果 contamination 是主要机制，我们预期移除 contaminated items 后 2024 得分应该下降。论文如何调和这一方向性矛盾？\n4. 论文是否能区分 \"legitimately harder items for 2024 models\"（因为 training methodology shift 导致某些能力退化）和 \"construct-irrelevant DIF\"？如果不能，\"Correct\" 步骤的实践建议是否过于简化？\n\n---\n\n## Missing References\n- Camilli, G. & Shepard, L. A. (1994). *Methods for Identifying Biased Test Items*. Sage. ——DIF 与 item bias 的经典区分框架\n- Penfield, R. D. & Camilli, G. (2007). Differential item functioning and item bias. In *Handbook of Statistics* (Vol. 26). ——impact vs. bias 的方法论框架\n- （论文已引用 Millsap 2011、Zumbo 1999，但未利用其中的 impact/bias 区分来支撑 Section 5.2 的实践建议）\n\n---\n\n## 主要优势\n- **S1 规模与系统性**：5,227 模型 × 12,508 items 的全量 psychometric audit，据我所知是 LLM 评估领域最大规模的此类分析\n- **S2 Cross-subject matching 是真正的方法论贡献**：ΔFPR=0 的构造性保证（k≤5）为 DIF 在多科目 benchmark 上的应用提供了可靠的 FPR 控制，这是对标准 MH-DIF 流程的有价值扩展\n- **S3 DIF ⊥ contamination 的发现有重要理论意义**：Jaccard=0.206 表明这两种 diagnostic 维度近正交，挑战了将 item-level anomaly 简单归因于 contamination 的普遍直觉\n- **S4 内部一致性控制设计得当**：random-split baseline (0.62% C%)、ability-quintile check (2.9%)、half-year granularity、composition control（Appendix P：30.25% vs 31.3%，仅 1.08 pp 差异）构成多层次 null-hypothesis 校验\n- **S5 Base/instruct 方向反转 (χ²=562.7) 提供 mechanism separation 的强证据**：base models 60.1% reference-favoring vs instruct models 69.6% focal-favoring，有效排除了 DIF 纯粹由单一机制驱动的假设",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-23T14:07:59.710374+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3864
}
```

</details>

---


### Tool call

_source line 1396 · 2026-05-23T14:08:03.648929+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-23T14:08:03.649374+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-23T14:08:07.567373+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1399 · 2026-05-23T14:08:07.668924+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 101
}
```

</details>

---


### Assistant

_source line 1400 · 2026-05-23T14:08:21.266926+00:00_

审稿报告已提交给 Review Director。

核心结论：**Overall 3.5 (Borderline Conference)**。三个 Must-Fix 问题：(1) DEFF 校正的 2.16× 估计范围（13.5% vs 29.2%）缺乏分辨依据；(2) 半合成注入用 binary flipping 而非 graded probability shift，检测力估计可能被系统性高估；(3) 缺少 DIF 文献中 impact/bias 的经典区分，导致 "Correct" 步骤（无差别移除 DIF items）与 mechanism-agnostic 定位之间存在逻辑冲突。四个 Should-Fix：calendar-year cohort 粒度粗糙、cross-subject matching 在高覆盖率下退化、contamination-heavy 叙事与 mechanism-agnostic 定位的张力、METABENCH selection bias 未讨论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 46

## Round 46

4 recorded events


### User

_source line 1401 · 2026-05-23T14:08:57.691754+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 — Round 1 审稿报告（新颖性与完整性）

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 大规模实证发现有价值（temporal DIF 与 contamination 近乎正交），但核心方法是 off-the-shelf MH-DIF 的直接搬运，方法论创新不足以稳进主会。

## Must-Fix 问题

**N1** [critical] 核心方法论新颖性不足——MH-DIF 是 40 年前的标准方法的直接应用
- Section 3.2 的方法描述本质上是教科书内容——K=5 等频分层、对数 odds ratio、ETS A/B/C 分类标准均原封不动。
- 第一点贡献（temporal DIF at scale）是实证发现而非方法创新；第二点（cross-subject matching）是 purified subtest matching 的直接推广；第三点（audit protocol）是组合既有步骤。
- 建议：(a) 更清晰论证 ΔFPR=0 的技术挑战和理论保证；(b) 讨论 4 个 LLM-specific challenges 构成真正的方法适配贡献；(c) 增加与 logistic regression DIF 的比较。

**N2** [critical] "DIF 与 contamination 近乎独立"的核心发现依赖质量存疑的 proxy
- Web-overlap labels 来自 Li et al. (2024b)，仅检测 items 是否在公开网络语料中出现——非常粗糙的 contamination proxy。
- (1) Web-overlap ≠ 实际训练数据包含；(2) 许多 contamination 来源不会被 web-overlap 捕获；(3) Li et al. labels 覆盖率仅 73.8%。
- Jaccard ≈ 0.20 可能仅反映 web-overlap labels 的低质量，而非 DIF 与真正 contamination 的独立性。
- 建议：使用多种 contamination 指标交叉验证；将结论软化为 "DIF is independent of web-overlap based contamination labels"。

## Should-Fix 问题

**W1** [warning] ETS 阈值从人类测试群体直接迁移到 LLM，缺乏校准验证
- LLM 没有 guessing behavior，能力维度可能高度多维。
- 建议通过 simulation 验证 ETS 阈值在 LLM response matrix 下的 Type I error 和 power。

**W2** [warning] 与 Growing Pains (Habba et al., 2026) 的差异化论证不够深入
- 差异化主要停留在方法层面（MH-DIF vs. fixed-parameter calibration），缺少在相同数据/相同 items 上的直接比较。
- 建议在附录中加入交叉比较。

**W3** [warning] "Temporal" framing 可能过窄——实际检测到的是 cohort-based DIF
- 2023 vs. 2024 cohorts 不仅在时间上不同，还在架构、数据规模、训练方法上系统性不同。
- 建议在 Discussion 中更明确讨论 temporal confounding。

**W4** [warning] 因果性过度暗示
- Abstract "because item measurement properties differ systematically" 隐含因果判断。
- DIF 只能说明 "items function differently after conditioning on total score"。

**W5** [warning] Score correction 的实际影响展示不充分
- Section 4.6 仅半页篇幅，未区分 ranking reversal 发生在 top-10 还是 mid-tier。
- 建议扩展或加入 case study。

## 主要优势
1. 规模与覆盖度出色（5,227 models × 12,508 items）
2. Semi-synthetic validation 设计精巧
3. 多层验证架构可信
4. DEFF correction 处理 family dependence 得当
5. 附录内容丰富

## 缺失的重要参考文献
1. Test security / item exposure 文献（Hau & Chang, 2001; Way, 1998）
2. Polytomous DIF 方法（French & Miller, 1996）
3. Benchmark dynamics 中 item banking 和 equating 的文献
4. Multi-group CFA / MIMIC models for MI testing

---

请逐条回应 R2 的每个 Must-Fix 和 Should-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1402 · 2026-05-23T14:10:38.761019+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: 核心方法论新颖性不足——MH-DIF 是 off-the-shelf 的直接搬运**\n\nR2 的批评部分成立但整体过度。需要区分三个层次：\n\n(1) MH-DIF 本身确实是标准方法——这点没有争议。但论文的方法论贡献不在于 MH-DIF 本身，而在于**将其适配到 LLM evaluation 的特殊结构**。Section 3.2（p.4-5）明确列出 4 个 LLM-specific challenges：local independence violation（模型不是独立考生）、permutation simulation 验证（1,000 replications, Section 4.1）、fine-tuned variants within model families 造成 family structure、MMLU 57-subject 多维结构。这些不是教科书内容——教科书处理的是人类考生的 i.i.d. 假设，不涉及 family-level DEFF 校正（Section D）。\n\n(2) Cross-subject matching 不是 purified subtest matching 的\"直接推广\"。标准 purified subtest matching（Swaminathan & Rogers, 1990）从同一测试中剔除 DIF 嫌疑 items 后用剩余 items 做 matching variable。论文的 cross-subject matching（Section 3.4, p.5）完全使用**不同科目**的总分做 matching variable，并给出了 **constructive ΔFPR=0 guarantee**（单科目 contamination 下 matching variable 不包含任何 contaminated item 的信号）。这一保证的证明（p.5 \"Remark\"段落）依赖于 LLM benchmark 的 multi-subject 结构——这是人类教育测试中没有对应物的特殊构造。\n\n(3) 我同意 R2 关于增加 logistic regression DIF 比较的建议——这确实能强化方法论贡献。但**缺少比较不等于 MH-DIF 应用无新颖性**。\n\n**结论**：R2 的新颖性批评适用于 Section 3.2 的 MH-DIF 核心步骤描述，但不适用于 cross-subject matching、DEFF 校正、和 LLM-specific 适配工作。建议作者在 Introduction 中更清晰地区分\"borrowed methodology\"和\"novel adaptations\"，但不应要求以此为由拒稿。\n\n---\n\n**[AGREE] R2-N2: \"DIF 与 contamination 近乎独立\"依赖质量存疑的 proxy**\n\n这是 R2 最有力的批评，我完全同意。\n\nWeb-overlap labels（Li et al., 2024b）检测的是 items 是否在公开网络语料中出现——这与\"模型训练数据是否包含该 item\"之间存在大量 gap。论文 Section 4.3（p.6-7）自己报告覆盖率为 73.8%（9,229 of 12,508 items），且 web-overlap 只是 contamination 的一个 noisy proxy。Jaccard = 0.206 可能反映的是：(a) DIF 与真实 contamination 确实独立（论文的解释），或 (b) web-overlap labels 噪声太大导致与任何信号的关联都很低。论文未排除解释 (b)。\n\nSection 5.1（p.8）呈现了两种解释（\"DIF captures a broader signal\" vs. \"DIF and contamination detection measure distinct constructs\"），但在 Abstract 和 Conclusion 中的措辞更接近单一解释。Abstract 的 \"Web-overlap contamination labels are near-independent of DIF flags\" 虽然事实正确，但暗示的含义（DIF 检测的不是 contamination）取决于 labels 的质量。\n\nR2 建议将结论软化为 \"DIF is independent of web-overlap based contamination labels\" 是合理的。我进一步建议：**应在 Section 4.3 中报告 web-overlap labels 自身的 test-retest reliability 或与其他 contamination 指标的交叉验证**，否则读者无法判断低 Jaccard 是信号还是噪声。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: ETS 阈值从人类测试群体直接迁移到 LLM，缺乏校准验证**\n\n同意。我在自己的审查中也关注了这一问题。论文的 random-split P99=1.45（Section A.2, p.12-13）提供了 empirical calibration——在 2023 cohort 内部随机分割时，99th percentile of |Δ_MH| 恰好略低于 ETS C threshold 1.5，说明阈值在 LLM response matrix 下近似合理。但这只是 necessary condition（null distribution 下不超过阈值），不是 sufficient condition（阈值在 LLM-specific effect size 分布下是否提供 optimal sensitivity-specificity tradeoff）。\n\nR2 建议通过 simulation 验证 Type I error 和 power 是合理的——论文 Section 4.1 的 Monte Carlo power analysis（Table 4-5）已部分完成了这一工作，但未将其明确框定为\"ETS 阈值在 LLM 下的校准验证\"。建议作者在正文中更明确地连接 Section 4.1 的 power 结果与 ETS 阈值的适用性论证。\n\n---\n\n**[AGREE] R2-W2: 与 Growing Pains 的差异化论证不够深入**\n\n同意，但优先级不高。Growing Pains（Habba et al., 2026）使用 fixed-parameter IRT calibration 检测 temporal instability，与 MH-DIF 是不同的技术路径。Section 2（p.3）提到两者的方法差异，但缺乏在相同 data slice 上的直接比较。作为一个 should-fix 合理，但在 8 页正文空间限制下，附录中的交叉比较可能更可行。\n\n---\n\n**[AGREE] R2-W3: \"Temporal\" framing 可能过窄——实际是 cohort-based DIF**\n\n同意。我在自己的 W1 中提出了相同的关切。2023 vs 2024 cohorts 在时间、架构偏好、训练方法、数据规模等维度上同时变化，\"temporal\" 标签暗示时间是主要变量，但实际驱动 DIF 的可能是 cohort composition（例如 2024 instruct models 比例更高）。论文 Appendix P（p.18）的 composition control 分析（balanced C%=30.25% vs raw 31.3%）部分回应了这一关切，但仅控制了 base/instruct 比例，未控制其他 cohort 差异（如平均模型大小、主流架构从 Llama-2 到 Llama-3 的迁移）。\n\n建议作者在 Section 5.1 讨论中明确承认 \"temporal\" 是 \"cohort-based\" 的简写，并讨论未控制的 confounders。\n\n---\n\n**[REBUT] R2-W4: Abstract 中 \"because\" 构成因果性过度暗示**\n\nR2 引用的具体句子是 Abstract 中的 \"scores are not directly comparable across cohorts because item measurement properties differ systematically\"。我认为这**不构成因果过度暗示**。\n\n这里的 \"because\" 解释的是**为什么 scores 不可比**（因为 item properties 不同），而非**为什么 item properties 不同**（因为 contamination / capability evolution / methodology shift）。DIF 的存在**在定义上**意味着 measurement properties 在组间不同——这是 DIF 的 definition，不是因果推断。说 \"scores are incomparable because items function differently\" 等价于说 \"measurement invariance is violated, therefore scores are not on a common scale\"——这是 psychometrics 中的标准推论链，不涉及 DIF 成因的因果判断。\n\n我在自己的 W3 中确实指出论文在 mechanism-agnostic 定位和 contamination-heavy 叙事之间存在张力，但 R2 所 cite 的这个具体句子不是 problematic 的例子。\n\n---\n\n**[AGREE] R2-W5: Score correction 的实际影响展示不充分**\n\n部分同意，但我认为问题比 R2 描述的更深。R2 关注的是展示不充分（未区分 ranking reversal 的位置），这确实是一个 presentation issue。但更根本的问题是我在 N3 中指出的：**Score correction 缺少 impact/bias 区分作为方法论基础**。在没有区分 impact-driven 和 bias-driven DIF items 的情况下，即使展示了更详细的 ranking reversal，也无法判断 correction 是改善了还是损害了 benchmark 的测量质量。\n\n建议将 R2 的 \"展示不足\" 和我的 \"impact/bias 缺失\" 合并处理：先建立 conceptual foundation（哪些 DIF items 应该被移除），再展示移除后的实际影响。\n\n---\n\n### 缺失参考文献\n\n**[REBUT] Polytomous DIF 方法（French & Miller, 1996）**：MMLU 是 4 选 1 多选题，论文使用 binary scoring（correct=1, incorrect=0），polytomous DIF 方法不适用。这不是缺失。\n\n**[AGREE] Test security / item exposure 文献**：Hau & Chang (2001) 等 item exposure control 文献与 benchmark maintenance 高度相关，建议在 Section 5.2 audit protocol 讨论中引用。\n\n**[REBUT] Multi-group CFA / MIMIC models**：论文 Section 2（p.3）已引用 MIMIC models 文献并解释了选择 MH-DIF 而非 parametric MI testing 的理由（MH-DIF 是非参数方法，不依赖 IRT model fit，而 MMLU response matrix 对 uni-dimensional 2PL fit 较差——Section A.1, p.13）。multi-group CFA 要求可接受的 model fit 作为前提，在 57-subject MMLU 上不现实。这个选择有充分的方法论理由。\n\n**[AGREE] Benchmark dynamics 中的 item banking/equating 文献**：这与 Section 5.2 的 audit protocol 直接相关——DIF detection → item banking → equated scoring 是教育测量的标准流程。引用 equating 文献能强化 Section 5.2 的实践建议。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: 核心方法论新颖性不足——MH-DIF 是 off-the-shelf 的直接搬运**\n\nR2 的批评部分成立但整体过度。需要区分三个层次：\n\n(1) MH-DIF 本身确实是标准方法——这点没有争议。但论文的方法论贡献不在于 MH-DIF 本身，而在于**将其适配到 LLM evaluation 的特殊结构**。Section 3.2（p.4-5）明确列出 4 个 LLM-specific challenges：local independence violation（模型不是独立考生）、permutation simulation 验证（1,000 replications, Section 4.1）、fine-tuned variants within model families 造成 family structure、MMLU 57-subject 多维结构。这些不是教科书内容——教科书处理的是人类考生的 i.i.d. 假设，不涉及 family-level DEFF 校正（Section D）。\n\n(2) Cross-subject matching 不是 purified subtest matching 的\"直接推广\"。标准 purified subtest matching（Swaminathan & Rogers, 1990）从同一测试中剔除 DIF 嫌疑 items 后用剩余 items 做 matching variable。论文的 cross-subject matching（Section 3.4, p.5）完全使用**不同科目**的总分做 matching variable，并给出了 **constructive ΔFPR=0 guarantee**（单科目 contamination 下 matching variable 不包含任何 contaminated item 的信号）。这一保证的证明（p.5 \"Remark\"段落）依赖于 LLM benchmark 的 multi-subject 结构——这是人类教育测试中没有对应物的特殊构造。\n\n(3) 我同意 R2 关于增加 logistic regression DIF 比较的建议——这确实能强化方法论贡献。但**缺少比较不等于 MH-DIF 应用无新颖性**。\n\n**结论**：R2 的新颖性批评适用于 Section 3.2 的 MH-DIF 核心步骤描述，但不适用于 cross-subject matching、DEFF 校正、和 LLM-specific 适配工作。建议作者在 Introduction 中更清晰地区分\"borrowed methodology\"和\"novel adaptations\"，但不应要求以此为由拒稿。\n\n---\n\n**[AGREE] R2-N2: \"DIF 与 contamination 近乎独立\"依赖质量存疑的 proxy**\n\n这是 R2 最有力的批评，我完全同意。\n\nWeb-overlap labels（Li et al., 2024b）检测的是 items 是否在公开网络语料中出现——这与\"模型训练数据是否包含该 item\"之间存在大量 gap。论文 Section 4.3（p.6-7）自己报告覆盖率为 73.8%（9,229 of 12,508 items），且 web-overlap 只是 contamination 的一个 noisy proxy。Jaccard = 0.206 可能反映的是：(a) DIF 与真实 contamination 确实独立（论文的解释），或 (b) web-overlap labels 噪声太大导致与任何信号的关联都很低。论文未排除解释 (b)。\n\nSection 5.1（p.8）呈现了两种解释（\"DIF captures a broader signal\" vs. \"DIF and contamination detection measure distinct constructs\"），但在 Abstract 和 Conclusion 中的措辞更接近单一解释。Abstract 的 \"Web-overlap contamination labels are near-independent of DIF flags\" 虽然事实正确，但暗示的含义（DIF 检测的不是 contamination）取决于 labels 的质量。\n\nR2 建议将结论软化为 \"DIF is independent of web-overlap based contamination labels\" 是合理的。我进一步建议：**应在 Section 4.3 中报告 web-overlap labels 自身的 test-retest reliability 或与其他 contamination 指标的交叉验证**，否则读者无法判断低 Jaccard 是信号还是噪声。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: ETS 阈值从人类测试群体直接迁移到 LLM，缺乏校准验证**\n\n同意。我在自己的审查中也关注了这一问题。论文的 random-split P99=1.45（Section A.2, p.12-13）提供了 empirical calibration——在 2023 cohort 内部随机分割时，99th percentile of |Δ_MH| 恰好略低于 ETS C threshold 1.5，说明阈值在 LLM response matrix 下近似合理。但这只是 necessary condition（null distribution 下不超过阈值），不是 sufficient condition（阈值在 LLM-specific effect size 分布下是否提供 optimal sensitivity-specificity tradeoff）。\n\nR2 建议通过 simulation 验证 Type I error 和 power 是合理的——论文 Section 4.1 的 Monte Carlo power analysis（Table 4-5）已部分完成了这一工作，但未将其明确框定为\"ETS 阈值在 LLM 下的校准验证\"。建议作者在正文中更明确地连接 Section 4.1 的 power 结果与 ETS 阈值的适用性论证。\n\n---\n\n**[AGREE] R2-W2: 与 Growing Pains 的差异化论证不够深入**\n\n同意，但优先级不高。Growing Pains（Habba et al., 2026）使用 fixed-parameter IRT calibration 检测 temporal instability，与 MH-DIF 是不同的技术路径。Section 2（p.3）提到两者的方法差异，但缺乏在相同 data slice 上的直接比较。作为一个 should-fix 合理，但在 8 页正文空间限制下，附录中的交叉比较可能更可行。\n\n---\n\n**[AGREE] R2-W3: \"Temporal\" framing 可能过窄——实际是 cohort-based DIF**\n\n同意。我在自己的 W1 中提出了相同的关切。2023 vs 2024 cohorts 在时间、架构偏好、训练方法、数据规模等维度上同时变化，\"temporal\" 标签暗示时间是主要变量，但实际驱动 DIF 的可能是 cohort composition（例如 2024 instruct models 比例更高）。论文 Appendix P（p.18）的 composition control 分析（balanced C%=30.25% vs raw 31.3%）部分回应了这一关切，但仅控制了 base/instruct 比例，未控制其他 cohort 差异（如平均模型大小、主流架构从 Llama-2 到 Llama-3 的迁移）。\n\n建议作者在 Section 5.1 讨论中明确承认 \"temporal\" 是 \"cohort-based\" 的简写，并讨论未控制的 confounders。\n\n---\n\n**[REBUT] R2-W4: Abstract 中 \"because\" 构成因果性过度暗示**\n\nR2 引用的具体句子是 Abstract 中的 \"scores are not directly comparable across cohorts because item measurement properties differ systematically\"。我认为这**不构成因果过度暗示**。\n\n这里的 \"because\" 解释的是**为什么 scores 不可比**（因为 item properties 不同），而非**为什么 item properties 不同**（因为 contamination / capability evolution / methodology shift）。DIF 的存在**在定义上**意味着 measurement properties 在组间不同——这是 DIF 的 definition，不是因果推断。说 \"scores are incomparable because items function differently\" 等价于说 \"measurement invariance is violated, therefore scores are not on a common scale\"——这是 psychometrics 中的标准推论链，不涉及 DIF 成因的因果判断。\n\n我在自己的 W3 中确实指出论文在 mechanism-agnostic 定位和 contamination-heavy 叙事之间存在张力，但 R2 所 cite 的这个具体句子不是 problematic 的例子。\n\n---\n\n**[AGREE] R2-W5: Score correction 的实际影响展示不充分**\n\n部分同意，但我认为问题比 R2 描述的更深。R2 关注的是展示不充分（未区分 ranking reversal 的位置），这确实是一个 presentation issue。但更根本的问题是我在 N3 中指出的：**Score correction 缺少 impact/bias 区分作为方法论基础**。在没有区分 impact-driven 和 bias-driven DIF items 的情况下，即使展示了更详细的 ranking reversal，也无法判断 correction 是改善了还是损害了 benchmark 的测量质量。\n\n建议将 R2 的 \"展示不足\" 和我的 \"impact/bias 缺失\" 合并处理：先建立 conceptual foundation（哪些 DIF items 应该被移除），再展示移除后的实际影响。\n\n---\n\n### 缺失参考文献\n\n**[REBUT] Polytomous DIF 方法（French & Miller, 1996）**：MMLU 是 4 选 1 多选题，论文使用 binary scoring（correct=1, incorrect=0），polytomous DIF 方法不适用。这不是缺失。\n\n**[AGREE] Test security / item exposure 文献**：Hau & Chang (2001) 等 item exposure control 文献与 benchmark maintenance 高度相关，建议在 Section 5.2 audit protocol 讨论中引用。\n\n**[REBUT] Multi-group CFA / MIMIC models**：论文 Section 2（p.3）已引用 MIMIC models 文献并解释了选择 MH-DIF 而非 parametric MI testing 的理由（MH-DIF 是非参数方法，不依赖 IRT model fit，而 MMLU response matrix 对 uni-dimensional 2PL fit 较差——Section A.1, p.13）。multi-group CFA 要求可接受的 model fit 作为前提，在 57-subject MMLU 上不现实。这个选择有充分的方法论理由。\n\n**[AGREE] Benchmark dynamics 中的 item banking/equating 文献**：这与 Section 5.2 的 audit protocol 直接相关——DIF detection → item banking → equated scoring 是教育测量的标准流程。引用 equating 文献能强化 Section 5.2 的实践建议。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-23T14:10:42.829914+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4068
}
```

</details>

---


### Assistant

_source line 1404 · 2026-05-23T14:10:54.683563+00:00_

已提交对 Reviewer 2 的逐条回应。总结：

- **N1 (新颖性不足)**：[REBUT] — cross-subject matching 的 ΔFPR=0 保证和 DEFF 校正是 LLM-specific 的真正方法论贡献，不是教科书内容的直接搬运
- **N2 (contamination proxy 质量)**：[AGREE] — web-overlap labels 噪声可能解释低 Jaccard，论文需软化结论
- **W1 (ETS 阈值迁移)**：[AGREE] — random-split P99 是必要但非充分的校准
- **W2 (Growing Pains 对比)**：[AGREE] — 但优先级不高
- **W3 (temporal vs cohort-based)**：[AGREE] — 与我的 W1 一致
- **W4 (因果暗示)**：[REBUT] — Abstract 中的 "because" 解释的是不可比性的原因（DIF 的定义），非 DIF 成因的因果判断
- **W5 (score correction 展示)**：[AGREE] — 但更根本的问题是缺少 impact/bias 区分（我的 N3）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 47

## Round 47

48 recorded events


### User

_source line 1405 · 2026-05-25T21:17:08.517867+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1：方法严谨性 + 实验有效性

### Venue 信息
- **目标会议**: EMNLP 2026 (通过 ACL Rolling Review 提交)
- **Deadline**: 2026-05-25 (ARR May cycle)
- **页数限制**: 正文 8 页 + references 无限制；Limitations 不计入页数
- **模板**: ACL style template (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind review
- **附录规则**: 允许，可供 reviewer 参考但不强制阅读

### 论文文件
- LaTeX 源码: `projects/irt_equated_bench_regen/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）
- PDF: `projects/irt_equated_bench_regen/artifacts/review_round_19/submitted.pdf`

### 你的审查侧重

**方法严谨性 + 实验有效性**。你需要重点审查：

1. **MH-DIF 方法论**：
   - MH 检验在 LLM 设定下的适用性（独立性假设违反、非参数 vs 参数方法选择）
   - ETS 阈值从人类考生迁移到 LLM 的合理性及校准
   - $K=5$ quintile stratification 的选择依据
   - 多重比较处理（为何不做 FDR/FWER correction 作为主方法）

2. **Semi-synthetic 注入框架**：
   - Uniform binary flipping 的现实性——是否高估检测力
   - Cross-subject matching 的 $\Delta\mathrm{FPR}=0$ 声明的严谨性
   - $k \leq 5$ 的保证边界在更大 $k$ 下如何退化
   - Injection 实验设计是否充分验证了方法的检测能力

3. **统计声明**：
   - DEFF 校正：simple-mean (29.2%) vs weighted-mean (13.5%) 的 2.16× 差距——论文如何处理这一不确定性
   - 31.3% C% 的置信区间和 bootstrap 方法
   - Random-split baseline 0.62% 的可靠性
   - Power analysis 参数选择（$\bar{a}=1.2$, $\bar{b}=-0.84$）

4. **控制实验**：
   - Ability-quintile C%=2.9% 是否充分排除了能力差异混淆
   - Leave-one-family-out (LOFO) 分析的充分性
   - 1:1 nearest-neighbor matching 的设计
   - Within-family (Llama-2 vs Llama-3) C%=61.3% 的解释

5. **因果推断与机制**：
   - "near-independent of web-overlap labels" (Jaccard=0.206, φ=0.012) 的推断强度
   - Base vs instruct 反向模式 (χ²=562.7) 的解释是否过强
   - DIF 检测的是 "differential functioning" 还是 "impact"——论文是否充分区分

### 输出格式

请按以下结构输出审稿意见：

```
## Summary
[2-3 句论文概述]

## Strengths
[逐条列出优点，标注 S1, S2, ...]

## Weaknesses
[逐条列出缺点，标注 W1, W2, ...，按严重性排序]
每条包含：问题描述 + 具体证据（cite Section/Table/Figure）+ 建议

## Questions
[需要作者回答的问题，标注 Q1, Q2, ...]

## Missing References
[遗漏的重要相关工作]

## Minor Issues
[格式、typo、表述等小问题]

## Overall Assessment
评分（1-5，参考 ARR 标准）+ 置信度（1-5）+ 简要理由
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1406 · 2026-05-25T21:17:22.614045+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search ARR reviewer guidelines",
  "subagent_type": "Explore",
  "prompt": "Search the web for \"ACL Rolling Review reviewer guidelines 2026\" and \"ARR review form criteria dimensions\". I need to find the official review form dimensions and scoring criteria used by ACL Rolling Review (ARR) for EMNLP 2026 submissions. Look for:\n1. The official review form fields and their scoring scales\n2. Definitions of each dimension (soundness, excitement, reproducibility, etc.)\n3. Any specific instructions for reviewers\n\nTry these searches and report back what you find. Use WebSearch and WebFetch tools.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Search ARR reviewer guidelines",
    "subagent_type": "Explore",
    "prompt": "Search the web for \"ACL Rolling Review reviewer guidelines 2026\" and \"ARR review form criteria dimensions\". I need to find the official review form dimensions and scoring criteria used by ACL Rolling Review (ARR) for EMNLP 2026 submissions. Look for:\n1. The official review form fields and their scoring scales\n2. Definitions of each dimension (soundness, excitement, reproducibility, etc.)\n3. Any specific instructions for reviewers\n\nTry these searches and report back what you find. Use WebSearch and WebFetch tools.",
    "run_in_background": "True"
  }
}
```

</details>

---


### Tool result

_source line 1407 · 2026-05-25T21:17:22.664794+00:00_

Async agent launched successfully.
agentId: a63bd4eaa07246b9c (internal ID - do not mention to user. Use SendMessage with to: 'a63bd4eaa07246b9c' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen--claude-sessions-review-reviewer-1-e2787213/594acef4-9c68-429d-983f-bbf0bdfc50e5/tasks/a63bd4eaa07246b9c.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1408 · 2026-05-25T21:17:25.729486+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1409 · 2026-05-25T21:17:25.830408+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1410 · 2026-05-25T21:17:32.935991+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1411 · 2026-05-25T21:17:33.842089+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1412 · 2026-05-25T21:17:34.244220+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 739.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 432.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.9}], \"total_pages\": 16, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_ro
…[truncated 59 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool result

_source line 1413 · 2026-05-25T21:17:34.244639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-25T21:17:37.463928+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1415 · 2026-05-25T21:17:38.418548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1416 · 2026-05-25T21:17:38.419020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1417 · 2026-05-25T21:17:38.971551+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1418 · 2026-05-25T21:17:39.375063+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1419 · 2026-05-25T21:17:39.375495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1420 · 2026-05-25T21:17:39.829476+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool result

_source line 1421 · 2026-05-25T21:17:40.232382+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 1422 · 2026-05-25T21:17:44.749672+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1423 · 2026-05-25T21:17:45.705660+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1424 · 2026-05-25T21:17:45.706159+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1425 · 2026-05-25T21:17:46.208464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1426 · 2026-05-25T21:17:46.562866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 1427 · 2026-05-25T21:17:46.563331+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1428 · 2026-05-25T21:17:47.117849+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool result

_source line 1429 · 2026-05-25T21:17:47.369694+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 1430 · 2026-05-25T21:17:54.502618+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "9-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "9-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1431 · 2026-05-25T21:17:55.557458+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 574.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 550.9}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 475.1}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 418.8}], \"total_pages\": 16, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artif
…[truncated 73 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 1432 · 2026-05-25T21:17:58.470049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1433 · 2026-05-25T21:17:58.972305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1434 · 2026-05-25T21:17:59.877733+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool result

_source line 1435 · 2026-05-25T21:17:59.878506+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1436 · 2026-05-25T21:17:59.929051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1437 · 2026-05-25T21:18:00.283072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1438 · 2026-05-25T21:18:00.535866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---


### Tool result

_source line 1439 · 2026-05-25T21:18:01.090931+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 1440 · 2026-05-25T21:18:06.121039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1441 · 2026-05-25T21:18:06.573890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1442 · 2026-05-25T21:18:07.528503+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-25T21:18:07.529654+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1444 · 2026-05-25T21:18:07.531131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1445 · 2026-05-25T21:18:07.884998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1446 · 2026-05-25T21:18:08.137235+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---


### Tool result

_source line 1447 · 2026-05-25T21:18:08.946259+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1061
}
```

</details>

---


### Tool call

_source line 1448 · 2026-05-25T21:20:06.679111+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1449 · 2026-05-25T21:20:06.779991+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1450 · 2026-05-25T21:22:19.954985+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Summary\n\n本文将教育测量学中的 Mantel-Haenszel 差异项目功能 (MH-DIF) 分析引入 LLM 基准测试的时序可比性检验。基于 METABENCH 响应矩阵 (5,227 模型 × 12,508 MMLU 题目)，对比 2023 与 2024 模型队列，发现 31.3% 的题目呈现大效应 DIF（ETS C 类）。论文开发了基于跨学科匹配 (cross-subject matching) 的半合成注入验证框架，并提出 Monitor/Triage/Correct 审计协议。\n\n## Strengths\n\n**S1. 问题定位精准且重要。** 基准测试的时序可比性在 LLM 评估社区被广泛讨论但缺乏严格量化工具。将心理测量学的 measurement invariance 框架引入 LLM 评估是一个自然但尚未被充分探索的方向，填补了 Growing Pains (Habba et al., 2026) 等工作在诊断粒度上的空白。\n\n**S2. 实验规模与复制性出色。** 5,227 模型、12,508 题目、6 个基准测试的规模在同类工作中罕见。核心发现 (17.9–31.3% C%) 在 TruthfulQA、ARC、HellaSwag、WinoGrande、GSM8K 上均复制成功 (Section 4.7, Table 2)，显著增强了结论的可信度。\n\n**S3. Cross-subject matching 设计巧妙。** 利用非目标学科总分作为匹配变量，在单学科注入下 ΔFPR=0 的构造性保证 (Section 3.4, Remark) 是方法论上的亮点。Figure 5 清晰展示了 cross-subject vs within-subject 匹配在 FPR 控制上的差异，令人信服。\n\n**S4. 控制实验层次丰富。** 能力分位匹配 (C%=2.9% within-cohort, Table 5)、LOFO 家族分析 (Table 8)、随机拆分基线 (0.62%)、IRT θ-conditioning (r=0.9986) 等多层控制从不同角度排除了混淆因素。Section C 的 Simpson's paradox 分析 (logistic regression with DIF-C as dependent variable) 也有力证明了 DIF 信号并非仅由能力差异或题目难度驱动。\n\n**S5. 诊断与行动协议的实用价值。** Section 5.2 提出的 Monitor/Triage/Correct 框架不仅是方法展示，还给出了具体可操作的基准维护建议，增加了论文的实际影响力。\n\n**S6. Figure 1 管线图信息量大。** 四步管线 (response matrix → stratification → MH-DIF → ETS classification) 配合 C%=29.2% 和 stable-item ρ=0.997 的汇总统计，读者可快速把握方法全貌。\n\n## Weaknesses\n\n**W1. [Critical] 标题数字 (31.3%) 未经 DEFF 校正，且校正后区间极宽 (13.5%–29.2%)。** 论文的核心 claim 是 \"~29% of items exhibit large temporal DIF\"（Abstract, Section 4.2），但这是未经设计效应 (DEFF) 校正的 raw C%。Section D 和 Table 10 显示：简单均值 DEFF 校正后 C%=29.2%，加权均值 DEFF 校正后仅 C%=13.5%，两者相差 2.16 倍。Cluster bootstrap 上界为 53.2%，校正后收敛至 ~27–29%，但这仍依赖于 simple-mean estimator 的选择。论文在 Section 4.2 将此范围表述为 \"bracketing C% at 13.5–29.2%\"，但 abstract 和 introduction 的措辞 (\"31% of items\") 强烈暗示了更高端的估计。对于一篇以量化审计为核心贡献的论文，这一不确定性应在 abstract 中明确标注，而非在附录中讨论。\n- **具体位置**: Abstract (\"31% of items\"), Section 4.2, Appendix D (Table 10)\n- **为什么影响接收**: 核心量化 claim 的可信区间横跨 2× 范围，削弱了论文的主要贡献\n\n**W2. [Critical] 半合成注入使用均匀二值翻转 (uniform binary flipping)，可能高估检测力。** Section 3.4 将 \"contaminated\" 项以 20% 均匀概率翻转为正确。现实中的 contamination 效应高度异质：记忆化可能导致某些题目接近天花板、某些仅有微小提升，且不同模型受影响程度不同。Appendix B 的混合机制注入 (Scheme D: difficulty-dependent for base, uniform for instruct) 仅测试了一种替代模式，且仍假设所有被注入题目受到相同强度影响。论文在 Limitations 中承认 \"uniform binary response flipping; realistic contamination...would produce weaker DIF signals\"，但未量化此高估的程度。\n- **具体位置**: Section 3.4 (\"flip incorrect→correct at exploration rate ε\"), Appendix B, Limitations point (1)\n- **建议**: 至少补充一组 graded injection 实验（如 ε 按题目难度衰减、或按模型能力衰减），报告检测力的下降幅度\n\n**W3. [Major] IRT 模型拟合差与参数化 power analysis 之间的张力。** Section A.2 (p11) 明确指出 \"the MMLU response matrix shows poor fit to a one-dimensional 2PL model...This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions.\" 但 Table 3 的 power analysis 恰恰使用了 2PL 参数 (ā=1.2, various b̄) 来生成模拟数据并估计 TPR。如果真实数据不符合 2PL，那么基于 2PL 模拟的 power 估计的外部效度存疑。论文需要更明确地讨论这一张力：为什么 2PL power analysis 的结论仍可迁移到 non-2PL 的真实数据？\n- **具体位置**: Section A.2 (\"IRT model fit\" paragraph), Table 3\n- **建议**: 补充基于 empirical item parameters (而非假设的 2PL) 的 resampling-based power analysis，或明确讨论 2PL misfit 对 power 估计的影响方向\n\n**W4. [Major] Cross-subject ΔFPR=0 保证在多学科污染下退化，且退化速度未充分表征。** Section 3.4 的 Remark 证明单学科注入下 ΔFPR=0，但当 k > 5 个学科同时被污染时，匹配变量 M_i^{-x} 本身被污染。Table 7 (p13) 报告 k=30-50 时 ΔFPR 达到 0.36-0.46。但论文缺少对中间区域 (k=5-15, 更现实的部分污染场景) 的系统表征。此外，MMLU 覆盖 57 个学科，k ≤ 5 的保证仅覆盖不到 9% 的学科，实际应用中污染可能跨越更多学科。\n- **具体位置**: Section 3.4 (Remark), Table 7 (p13)\n- **建议**: 补充 k=5,8,10,15,20 的 ΔFPR 曲线，明确 \"安全区\" 的实际范围\n\n**W5. [Major] ETS 阈值从人类考生迁移到 LLM 的合理性缺乏讨论。** ETS 的 A/B/C 分类 (|Δ_MH| < 1.0 / 1.0–1.5 / ≥ 1.5) 是基于人类教育测试群体校准的效应量标准 (Section 3.2 引用 Donoghue & Allen, 1993; Clauser & Mazor, 1998)。LLM 与人类在 item-person 交互模式上有本质差异：(1) LLM 没有真正的 \"ability\" latent trait，总分仅是聚合正确率；(2) 5,227 个 \"考生\" 中存在大量高度同质的模型（同架构不同 checkpoint），inflating sample size 但不增加独立信息。论文在 Section A.2 做了 threshold sensitivity 分析 (Table 3)，表明定性结论不依赖特定阈值，但未讨论阈值本身在 LLM 语境下的 substantive meaning（即 |Δ_MH|=1.5 对 LLM 意味着什么实际差异）。\n- **具体位置**: Section 3.2 (ETS classification), Section A.2 (threshold sensitivity)\n- **建议**: 添加一段讨论 ETS 阈值在 LLM 设定下的实质含义，或提供 data-driven 的阈值校准\n\n**W6. [Moderate] 多重比较校正未作为主方法。** 12,508 个项目同时进行假设检验，即使 per-item α=0.05，预期假阳性也有 ~625 个。论文使用 ETS classification（基于效应量而非 p-value）作为主要分类方法，并在 Section A.2 提到 BH-FDR 校正作为 robustness check (α=0.05)。但 ETS 分类本身也包含显著性条件 (p < 0.05 for Category C)，此 p-value 门槛未做多重校正。Random-split baseline 0.62% 提供了经验性 null 分布，但这是在 random group assignment 下的 FPR，并非在 \"no DIF\" null 下的 FPR。\n- **具体位置**: Section 3.2 (Eq. 1-2), Section A.2 (\"Multiple testing\" paragraph)\n- **建议**: 报告 BH-FDR 校正后的 C% 变化，或更明确地论证 ETS classification 的效应量门槛为什么使 multiple testing correction 不必要\n\n**W7. [Moderate] \"近独立于 web-overlap labels\" 的推断强度。** Section 4.3 报告 DIF flags 与 web-overlap labels 的 Jaccard=0.206, φ=0.012, p=0.88。论文将此解读为两个信号 \"near-independent\"。但 Jaccard=0.206 意味着约 20% 的重叠，且 web-overlap labels 本身的覆盖率和准确性存疑 (论文也承认 \"web-overlap labels are a proxy for training-set membership...this near-independence could partly reflect noise\")。φ=0.012 的低相关更可能反映 web-overlap labels 的噪声而非 DIF 的独立性。这一分析的结论强度被过度解读了——正确的表述应是 \"DIF flags 与现有 web-overlap labels 不一致\"，而非 \"DIF 检测的是不同于 contamination 的信号\"。\n- **具体位置**: Section 4.3, Figure 2 (right panel caption)\n- **建议**: 弱化 \"complementary diagnostic dimensions\" 的措辞，承认 web-overlap labels 的噪声可能驱动低相关\n\n**W8. [Moderate] Base vs instruct 反向模式 (χ²=562.7) 的机制解释。** Section 4.3 (也见 Appendix O) 报告 base 模型倾向 reference-favoring (64.1%) 而 instruct 模型倾向 focal-favoring (65.6%)。论文将此归因于 \"structured capability shifts\" 和 \"composition shift as the primary driver\"。但 base 和 instruct 模型在处理 multiple-choice items 时有系统性差异（如 instruction following, output format），这些差异可能产生 DIF-like 的 artifacts，并非真正的 \"differential item functioning\"。论文未充分区分 DIF (item-level bias) 与 impact (group-level ability difference) 在 base vs instruct 比较中的含义。\n- **具体位置**: Section 4.3 (\"base and instruct models exhibit opposite DIF directions, χ²=562.7\"), Appendix O\n- **建议**: 讨论 base/instruct 的 format sensitivity 作为替代解释\n\n## Questions\n\n**Q1.** Abstract 和 Introduction 使用 \"31% of items\" 作为核心数字，但 DEFF 校正后下界为 13.5%。作者是否考虑在 abstract 中报告校正后的区间而非原始值？为什么选择 simple-mean DEFF 而非 weighted-mean 作为更保守的估计？\n\n**Q2.** Power analysis (Table 3) 基于 2PL 参数生成模拟数据，但论文承认 MMLU 对 2PL 拟合差。作者能否提供基于实际 item parameters 的 bootstrap power analysis，以验证 parametric power estimates 的外部效度？\n\n**Q3.** Cross-subject matching 的 ΔFPR=0 保证在 k ≤ 5 时成立。在更现实的 k=8-15 污染场景下（如一个 training corpus 覆盖多个 STEM 学科），ΔFPR 的退化曲线是什么形状？Table 7 仅报告了 k=20,30,40,50 的离散点。\n\n**Q4.** 时间分割点选择 (2023 vs 2024) 对 C% 有多大影响？如果改用 calendar-year boundaries 以外的分割（如按 MMLU release date 之前/之后），结果是否稳健？论文在 Section 4.2 提到 \"Calendar-year boundaries are coarse; half-yearly comparison C% = 34.1%\"——这一更高的 C% 是否暗示时间粒度越细 DIF 越大？\n\n**Q5.** 5,227 个模型中有大量来自同一架构家族的变体（如 Llama 系列有 N=547, Mistral N=308）。这些高度同质的模型是否 inflate 了 MH 统计量的显著性？DEFF 校正是否充分处理了这种 within-family correlation？\n\n**Q6.** Ability-quintile 控制 (Table 5) 显示 C% 未显著下降，但 within-subject DIF 仅在 5 个代表性学科上测试。如果在全部 57 个学科上执行 within-subject DIF，结果是否一致？\n\n**Q7.** Section H 的 item-property predictive analysis (logistic regression + LightGBM) 得到 AUROC ≈ 0.60，表明题目特征对 DIF susceptibility 的预测力很弱。这是否意味着 DIF 主要由模型端因素（而非题目端因素）驱动？这对 \"Monitor/Triage/Correct\" 协议中基于题目属性的预筛选有何影响？\n\n## Missing References\n\n1. **Computerized Adaptive Testing (CAT) for LLMs**: 近期有工作将 CAT 引入 LLM 评估 (如 Zhuang et al., 2023, \"Efficiently Measuring the Cognitive Ability of LLMs\")，这与本文的 item-level analysis 相关但未被引用。\n\n2. **Test security / item exposure literature**: 教育测量学中关于 item exposure 和 test security 的文献（如 van der Linden & Veldkamp, 2007）与 benchmark contamination 有直接对应关系。\n\n3. **Recent IRT-based LLM evaluation**: Polo et al. (2024) \"tinyBenchmarks\" 被引用，但 Vania et al. (2021, \"Comparing Test Sets with Item Response Theory\") 等更早的 NLP+IRT 工作可能也相关。\n\n## Minor Issues\n\n- **M1.** Figure 3 的 x 轴标签 \"Δ_MH\" 的下标 \"MH\" 在图中字体较小，建议放大。\n- **M2.** Table 1 (p7) 的 \"Enrichment\" 列缺少 HellaSwag 和部分基准的数据（标 \"–\"），应说明原因。\n- **M3.** Section 4.1 提到 \"1,000 replications\" 但未报告 seed 或 random number generator。\n- **M4.** Appendix 标签从 A 到 Q (17 个)，总量较大。考虑合并部分相关性强的 appendix 以提高可读性。\n- **M5.** Abstract 第一句 \"Every leaderboard comparison assumes that benchmark items measure the same construct across model generations\" 略显绝对——部分排行榜 (如 Chatbot Arena) 使用 ELO 而非固定题目。\n\n## Overall Assessment\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 3/5 — 方法论框架合理，但 DEFF 校正后核心数字的 2× 不确定性 (13.5%–29.2%) 以及 2PL power analysis 与模型拟合差之间的张力削弱了量化 claims 的可信度。半合成注入的均匀翻转假设可能高估检测力。\n**Excitement**: 3.5/5 — 将 MH-DIF 引入 LLM 评估是一个有价值的方法论贡献，问题重要且及时。但论文更偏向诊断工具展示而非深层机制发现，excitement 受限。\n**Reproducibility**: 4/5 — 代码和数据公开（脚注 1），附录详尽，但 power analysis 的具体实现细节（random seed, simulation code）未完全提供。\n**Confidence**: 4/5 — 我熟悉 DIF 方法论和 LLM 评估文献，仔细阅读了全文和附录。\n\n**简要理由**: 论文选题好、规模大、控制实验多层次，但核心量化 claim 的不确定性 (DEFF 13.5%–29.2%) 在 abstract/intro 中被淡化，半合成注入的 uniform flipping 假设可能高估检测力，且论文未充分解决 ETS 阈值从人类教育测试迁移到 LLM 的 substantive meaning 问题。如果作者能 (1) 在 abstract 中坦诚报告 DEFF 校正后的区间，(2) 补充 graded injection 实验，(3) 更明确讨论 IRT misfit 对 power analysis 的影响，论文将达到 Conference 水平 (4.0)。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Summary\n\n本文将教育测量学中的 Mantel-Haenszel 差异项目功能 (MH-DIF) 分析引入 LLM 基准测试的时序可比性检验。基于 METABENCH 响应矩阵 (5,227 模型 × 12,508 MMLU 题目)，对比 2023 与 2024 模型队列，发现 31.3% 的题目呈现大效应 DIF（ETS C 类）。论文开发了基于跨学科匹配 (cross-subject matching) 的半合成注入验证框架，并提出 Monitor/Triage/Correct 审计协议。\n\n## Strengths\n\n**S1. 问题定位精准且重要。** 基准测试的时序可比性在 LLM 评估社区被广泛讨论但缺乏严格量化工具。将心理测量学的 measurement invariance 框架引入 LLM 评估是一个自然但尚未被充分探索的方向，填补了 Growing Pains (Habba et al., 2026) 等工作在诊断粒度上的空白。\n\n**S2. 实验规模与复制性出色。** 5,227 模型、12,508 题目、6 个基准测试的规模在同类工作中罕见。核心发现 (17.9–31.3% C%) 在 TruthfulQA、ARC、HellaSwag、WinoGrande、GSM8K 上均复制成功 (Section 4.7, Table 2)，显著增强了结论的可信度。\n\n**S3. Cross-subject matching 设计巧妙。** 利用非目标学科总分作为匹配变量，在单学科注入下 ΔFPR=0 的构造性保证 (Section 3.4, Remark) 是方法论上的亮点。Figure 5 清晰展示了 cross-subject vs within-subject 匹配在 FPR 控制上的差异，令人信服。\n\n**S4. 控制实验层次丰富。** 能力分位匹配 (C%=2.9% within-cohort, Table 5)、LOFO 家族分析 (Table 8)、随机拆分基线 (0.62%)、IRT θ-conditioning (r=0.9986) 等多层控制从不同角度排除了混淆因素。Section C 的 Simpson's paradox 分析 (logistic regression with DIF-C as dependent variable) 也有力证明了 DIF 信号并非仅由能力差异或题目难度驱动。\n\n**S5. 诊断与行动协议的实用价值。** Section 5.2 提出的 Monitor/Triage/Correct 框架不仅是方法展示，还给出了具体可操作的基准维护建议，增加了论文的实际影响力。\n\n**S6. Figure 1 管线图信息量大。** 四步管线 (response matrix → stratification → MH-DIF → ETS classification) 配合 C%=29.2% 和 stable-item ρ=0.997 的汇总统计，读者可快速把握方法全貌。\n\n## Weaknesses\n\n**W1. [Critical] 标题数字 (31.3%) 未经 DEFF 校正，且校正后区间极宽 (13.5%–29.2%)。** 论文的核心 claim 是 \"~29% of items exhibit large temporal DIF\"（Abstract, Section 4.2），但这是未经设计效应 (DEFF) 校正的 raw C%。Section D 和 Table 10 显示：简单均值 DEFF 校正后 C%=29.2%，加权均值 DEFF 校正后仅 C%=13.5%，两者相差 2.16 倍。Cluster bootstrap 上界为 53.2%，校正后收敛至 ~27–29%，但这仍依赖于 simple-mean estimator 的选择。论文在 Section 4.2 将此范围表述为 \"bracketing C% at 13.5–29.2%\"，但 abstract 和 introduction 的措辞 (\"31% of items\") 强烈暗示了更高端的估计。对于一篇以量化审计为核心贡献的论文，这一不确定性应在 abstract 中明确标注，而非在附录中讨论。\n- **具体位置**: Abstract (\"31% of items\"), Section 4.2, Appendix D (Table 10)\n- **为什么影响接收**: 核心量化 claim 的可信区间横跨 2× 范围，削弱了论文的主要贡献\n\n**W2. [Critical] 半合成注入使用均匀二值翻转 (uniform binary flipping)，可能高估检测力。** Section 3.4 将 \"contaminated\" 项以 20% 均匀概率翻转为正确。现实中的 contamination 效应高度异质：记忆化可能导致某些题目接近天花板、某些仅有微小提升，且不同模型受影响程度不同。Appendix B 的混合机制注入 (Scheme D: difficulty-dependent for base, uniform for instruct) 仅测试了一种替代模式，且仍假设所有被注入题目受到相同强度影响。论文在 Limitations 中承认 \"uniform binary response flipping; realistic contamination...would produce weaker DIF signals\"，但未量化此高估的程度。\n- **具体位置**: Section 3.4 (\"flip incorrect→correct at exploration rate ε\"), Appendix B, Limitations point (1)\n- **建议**: 至少补充一组 graded injection 实验（如 ε 按题目难度衰减、或按模型能力衰减），报告检测力的下降幅度\n\n**W3. [Major] IRT 模型拟合差与参数化 power analysis 之间的张力。** Section A.2 (p11) 明确指出 \"the MMLU response matrix shows poor fit to a one-dimensional 2PL model...This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions.\" 但 Table 3 的 power analysis 恰恰使用了 2PL 参数 (ā=1.2, various b̄) 来生成模拟数据并估计 TPR。如果真实数据不符合 2PL，那么基于 2PL 模拟的 power 估计的外部效度存疑。论文需要更明确地讨论这一张力：为什么 2PL power analysis 的结论仍可迁移到 non-2PL 的真实数据？\n- **具体位置**: Section A.2 (\"IRT model fit\" paragraph), Table 3\n- **建议**: 补充基于 empirical item parameters (而非假设的 2PL) 的 resampling-based power analysis，或明确讨论 2PL misfit 对 power 估计的影响方向\n\n**W4. [Major] Cross-subject ΔFPR=0 保证在多学科污染下退化，且退化速度未充分表征。** Section 3.4 的 Remark 证明单学科注入下 ΔFPR=0，但当 k > 5 个学科同时被污染时，匹配变量 M_i^{-x} 本身被污染。Table 7 (p13) 报告 k=30-50 时 ΔFPR 达到 0.36-0.46。但论文缺少对中间区域 (k=5-15, 更现实的部分污染场景) 的系统表征。此外，MMLU 覆盖 57 个学科，k ≤ 5 的保证仅覆盖不到 9% 的学科，实际应用中污染可能跨越更多学科。\n- **具体位置**: Section 3.4 (Remark), Table 7 (p13)\n- **建议**: 补充 k=5,8,10,15,20 的 ΔFPR 曲线，明确 \"安全区\" 的实际范围\n\n**W5. [Major] ETS 阈值从人类考生迁移到 LLM 的合理性缺乏讨论。** ETS 的 A/B/C 分类 (|Δ_MH| < 1.0 / 1.0–1.5 / ≥ 1.5) 是基于人类教育测试群体校准的效应量标准 (Section 3.2 引用 Donoghue & Allen, 1993; Clauser & Mazor, 1998)。LLM 与人类在 item-person 交互模式上有本质差异：(1) LLM 没有真正的 \"ability\" latent trait，总分仅是聚合正确率；(2) 5,227 个 \"考生\" 中存在大量高度同质的模型（同架构不同 checkpoint），inflating sample size 但不增加独立信息。论文在 Section A.2 做了 threshold sensitivity 分析 (Table 3)，表明定性结论不依赖特定阈值，但未讨论阈值本身在 LLM 语境下的 substantive meaning（即 |Δ_MH|=1.5 对 LLM 意味着什么实际差异）。\n- **具体位置**: Section 3.2 (ETS classification), Section A.2 (threshold sensitivity)\n- **建议**: 添加一段讨论 ETS 阈值在 LLM 设定下的实质含义，或提供 data-driven 的阈值校准\n\n**W6. [Moderate] 多重比较校正未作为主方法。** 12,508 个项目同时进行假设检验，即使 per-item α=0.05，预期假阳性也有 ~625 个。论文使用 ETS classification（基于效应量而非 p-value）作为主要分类方法，并在 Section A.2 提到 BH-FDR 校正作为 robustness check (α=0.05)。但 ETS 分类本身也包含显著性条件 (p < 0.05 for Category C)，此 p-value 门槛未做多重校正。Random-split baseline 0.62% 提供了经验性 null 分布，但这是在 random group assignment 下的 FPR，并非在 \"no DIF\" null 下的 FPR。\n- **具体位置**: Section 3.2 (Eq. 1-2), Section A.2 (\"Multiple testing\" paragraph)\n- **建议**: 报告 BH-FDR 校正后的 C% 变化，或更明确地论证 ETS classification 的效应量门槛为什么使 multiple testing correction 不必要\n\n**W7. [Moderate] \"近独立于 web-overlap labels\" 的推断强度。** Section 4.3 报告 DIF flags 与 web-overlap labels 的 Jaccard=0.206, φ=0.012, p=0.88。论文将此解读为两个信号 \"near-independent\"。但 Jaccard=0.206 意味着约 20% 的重叠，且 web-overlap labels 本身的覆盖率和准确性存疑 (论文也承认 \"web-overlap labels are a proxy for training-set membership...this near-independence could partly reflect noise\")。φ=0.012 的低相关更可能反映 web-overlap labels 的噪声而非 DIF 的独立性。这一分析的结论强度被过度解读了——正确的表述应是 \"DIF flags 与现有 web-overlap labels 不一致\"，而非 \"DIF 检测的是不同于 contamination 的信号\"。\n- **具体位置**: Section 4.3, Figure 2 (right panel caption)\n- **建议**: 弱化 \"complementary diagnostic dimensions\" 的措辞，承认 web-overlap labels 的噪声可能驱动低相关\n\n**W8. [Moderate] Base vs instruct 反向模式 (χ²=562.7) 的机制解释。** Section 4.3 (也见 Appendix O) 报告 base 模型倾向 reference-favoring (64.1%) 而 instruct 模型倾向 focal-favoring (65.6%)。论文将此归因于 \"structured capability shifts\" 和 \"composition shift as the primary driver\"。但 base 和 instruct 模型在处理 multiple-choice items 时有系统性差异（如 instruction following, output format），这些差异可能产生 DIF-like 的 artifacts，并非真正的 \"differential item functioning\"。论文未充分区分 DIF (item-level bias) 与 impact (group-level ability difference) 在 base vs instruct 比较中的含义。\n- **具体位置**: Section 4.3 (\"base and instruct models exhibit opposite DIF directions, χ²=562.7\"), Appendix O\n- **建议**: 讨论 base/instruct 的 format sensitivity 作为替代解释\n\n## Questions\n\n**Q1.** Abstract 和 Introduction 使用 \"31% of items\" 作为核心数字，但 DEFF 校正后下界为 13.5%。作者是否考虑在 abstract 中报告校正后的区间而非原始值？为什么选择 simple-mean DEFF 而非 weighted-mean 作为更保守的估计？\n\n**Q2.** Power analysis (Table 3) 基于 2PL 参数生成模拟数据，但论文承认 MMLU 对 2PL 拟合差。作者能否提供基于实际 item parameters 的 bootstrap power analysis，以验证 parametric power estimates 的外部效度？\n\n**Q3.** Cross-subject matching 的 ΔFPR=0 保证在 k ≤ 5 时成立。在更现实的 k=8-15 污染场景下（如一个 training corpus 覆盖多个 STEM 学科），ΔFPR 的退化曲线是什么形状？Table 7 仅报告了 k=20,30,40,50 的离散点。\n\n**Q4.** 时间分割点选择 (2023 vs 2024) 对 C% 有多大影响？如果改用 calendar-year boundaries 以外的分割（如按 MMLU release date 之前/之后），结果是否稳健？论文在 Section 4.2 提到 \"Calendar-year boundaries are coarse; half-yearly comparison C% = 34.1%\"——这一更高的 C% 是否暗示时间粒度越细 DIF 越大？\n\n**Q5.** 5,227 个模型中有大量来自同一架构家族的变体（如 Llama 系列有 N=547, Mistral N=308）。这些高度同质的模型是否 inflate 了 MH 统计量的显著性？DEFF 校正是否充分处理了这种 within-family correlation？\n\n**Q6.** Ability-quintile 控制 (Table 5) 显示 C% 未显著下降，但 within-subject DIF 仅在 5 个代表性学科上测试。如果在全部 57 个学科上执行 within-subject DIF，结果是否一致？\n\n**Q7.** Section H 的 item-property predictive analysis (logistic regression + LightGBM) 得到 AUROC ≈ 0.60，表明题目特征对 DIF susceptibility 的预测力很弱。这是否意味着 DIF 主要由模型端因素（而非题目端因素）驱动？这对 \"Monitor/Triage/Correct\" 协议中基于题目属性的预筛选有何影响？\n\n## Missing References\n\n1. **Computerized Adaptive Testing (CAT) for LLMs**: 近期有工作将 CAT 引入 LLM 评估 (如 Zhuang et al., 2023, \"Efficiently Measuring the Cognitive Ability of LLMs\")，这与本文的 item-level analysis 相关但未被引用。\n\n2. **Test security / item exposure literature**: 教育测量学中关于 item exposure 和 test security 的文献（如 van der Linden & Veldkamp, 2007）与 benchmark contamination 有直接对应关系。\n\n3. **Recent IRT-based LLM evaluation**: Polo et al. (2024) \"tinyBenchmarks\" 被引用，但 Vania et al. (2021, \"Comparing Test Sets with Item Response Theory\") 等更早的 NLP+IRT 工作可能也相关。\n\n## Minor Issues\n\n- **M1.** Figure 3 的 x 轴标签 \"Δ_MH\" 的下标 \"MH\" 在图中字体较小，建议放大。\n- **M2.** Table 1 (p7) 的 \"Enrichment\" 列缺少 HellaSwag 和部分基准的数据（标 \"–\"），应说明原因。\n- **M3.** Section 4.1 提到 \"1,000 replications\" 但未报告 seed 或 random number generator。\n- **M4.** Appendix 标签从 A 到 Q (17 个)，总量较大。考虑合并部分相关性强的 appendix 以提高可读性。\n- **M5.** Abstract 第一句 \"Every leaderboard comparison assumes that benchmark items measure the same construct across model generations\" 略显绝对——部分排行榜 (如 Chatbot Arena) 使用 ELO 而非固定题目。\n\n## Overall Assessment\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 3/5 — 方法论框架合理，但 DEFF 校正后核心数字的 2× 不确定性 (13.5%–29.2%) 以及 2PL power analysis 与模型拟合差之间的张力削弱了量化 claims 的可信度。半合成注入的均匀翻转假设可能高估检测力。\n**Excitement**: 3.5/5 — 将 MH-DIF 引入 LLM 评估是一个有价值的方法论贡献，问题重要且及时。但论文更偏向诊断工具展示而非深层机制发现，excitement 受限。\n**Reproducibility**: 4/5 — 代码和数据公开（脚注 1），附录详尽，但 power analysis 的具体实现细节（random seed, simulation code）未完全提供。\n**Confidence**: 4/5 — 我熟悉 DIF 方法论和 LLM 评估文献，仔细阅读了全文和附录。\n\n**简要理由**: 论文选题好、规模大、控制实验多层次，但核心量化 claim 的不确定性 (DEFF 13.5%–29.2%) 在 abstract/intro 中被淡化，半合成注入的 uniform flipping 假设可能高估检测力，且论文未充分解决 ETS 阈值从人类教育测试迁移到 LLM 的 substantive meaning 问题。如果作者能 (1) 在 abstract 中坦诚报告 DEFF 校正后的区间，(2) 补充 graded injection 实验，(3) 更明确讨论 IRT misfit 对 power analysis 的影响，论文将达到 Conference 水平 (4.0)。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1451 · 2026-05-25T21:22:30.506079+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 10551
}
```

</details>

---


### Assistant

_source line 1452 · 2026-05-25T21:22:41.102531+00:00_

审稿意见已提交给 Review Director。

**审稿完成摘要**：

- **Overall**: 3.5 (Borderline Conference)
- **核心优势**: 问题定位精准、规模大 (5,227 models × 12,508 items × 6 benchmarks)、cross-subject matching 设计巧妙、控制实验层次丰富
- **主要问题**:
  - **W1 [Critical]**: 标题数字 31.3% 未经 DEFF 校正，校正后区间 13.5%–29.2% 横跨 2× 
  - **W2 [Critical]**: 均匀二值翻转注入可能高估检测力
  - **W3 [Major]**: 2PL power analysis 与 IRT 模型拟合差之间的张力
  - **W4 [Major]**: Cross-subject ΔFPR=0 保证在多学科污染 (k>5) 下退化
  - **W5 [Major]**: ETS 阈值从人类迁移到 LLM 缺乏实质含义讨论
- **提升路径**: 在 abstract 中坦诚报告 DEFF 区间、补充 graded injection 实验、讨论 IRT misfit 影响，可达 4.0 (Conference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 48

## Round 48

4 recorded events


### User

_source line 1453 · 2026-05-25T21:25:53.025466+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Weakness 和 Question：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）
  
---

## Reviewer 2 原文

### Strengths

**S1. 大规模、系统性的实证分析。** 5,227 个模型 × 12,508 个题目的分析规模令人印象深刻，在六个基准上复现增强了可信度。

**S2. 多层次验证设计严谨。** 五种 cohort 对比 + DEFF 校正 + cluster bootstrap + LOFO 分析 + 多阈值敏感性检验。Random split 的 0.62% C% 与 temporal 的 31.3% 形成 50× 对比。

**S3. Cross-subject matching 的 ΔFPR = 0 保证有理论和实证价值。**

**S4. DIF vs. contamination 的区分具有概念洞察力。** Figure 2 通过 ICC 曲线清晰展示了 global exposure 与 differential functioning 的区别。

**S5. 对 NLP 读者的心理测量概念解释充分。**

**S6. Base-vs-instruct 方向反转是有价值的发现。**

### Weaknesses

**W1. [Critical] 标题"Score Incomparability"与核心发现之间存在根本性叙事张力。** 标题暗示分数不可比较，但核心发现是 ρ ≈ 0.997——排名几乎完美保持。如果 31% 的题目有 DIF 但排名不变，那么"incomparability"这一措辞是否过度？论文实际展示的是 item-level instability with aggregate robustness，但标题设置的期望与实际发现不匹配。Introduction 中 "The result is sobering" 的措辞进一步放大了不匹配。

**W2. [Critical] 方法论新颖性有限——核心方法均为已知技术的直接应用。** MH-DIF (1988)、ETS A/B/C 分类、cross-subject matching (purified subtest matching 1990)、DEFF 校正 (1992)。论文的四个 LLM-specific challenges 的解决方案都是现有方法，没有提出针对 LLM 特殊性的新统计方法。

**W3. [Major] C% 的不确定性范围过大（13.5%–31.3%）。** 2.3× 的范围。Cluster bootstrap 依赖于 family 定义的合理性。如果真实 C% 接近 13.5%，论文的许多结论需要显著弱化。

**W4. [Major] "Mechanism-agnostic"定位与论文内容之间存在紧张关系。** 大量篇幅用于 contamination 分析，但声称 mechanism-agnostic。如果 DIF 真的是 mechanism-agnostic，为什么验证框架完全基于 contamination？

**W5. [Major] 缺少对 DIF 在 LLM 场景下概念合法性的深入讨论。** 2023 vs. 2024 模型不是同一总体的人口学子群，而是技术上根本不同的系统。κ = 0.80 意味着 20% 的 DIF 项目可能是多维性伪影。

**W6. [Minor] 三个 contribution 的权重不均衡。** Contribution 3（audit protocol）在 Section 5.2 中仅占半段，没有部署验证。

### Questions

**Q1.** 既然 ρ ≈ 0.997，能否更精确地量化 temporal DIF 的实际危害？在什么场景下 practitioner 会因忽略 temporal DIF 而做出错误决策？

**Q2.** 2023 vs 2024 calendar-year boundary 混合了多种变化源。是否考虑过更细粒度的时间划分？DIF 信号是逐渐积累还是存在突变点？

**Q3.** Base-vs-instruct 方向反转可能部分反映 RLHF/instruction tuning 对答题策略的系统性改变。如何区分"训练方法改变了模型的合法能力剖面"与"训练方法导致了 item 测量特性的扭曲"？

**Q4.** 当 DIF 由非 contamination 因素（如全局训练方法变化）驱动时，cross-subject matching 的行为如何？

### Missing References

**M1.** Rodriguez et al. (2021) "Evaluation Examples Are Not Equally Informative" (ACL 2021) — IRT 应用于 NLP 评估的奠基性工作。
**M2.** Polo et al. (2024) "tinyBenchmarks" (ICML 2024)。
**M3.** 2025 年 PSN-IRT 后续工作或 "Lost in Benchmarks?" 等最新 IRT+LLM 工作。

---

请对以上每个 Weakness (W1-W6) 和 Questions (Q1-Q4) 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1454 · 2026-05-25T21:27:50.605577+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1: 标题 \"Score Incomparability\" 与 ρ ≈ 0.997 的叙事张力。**\n同意这是论文最突出的叙事问题。论文的核心发现实际上是 *item-level instability with aggregate robustness*——31% 的题目有大效应 DIF，但聚合排名几乎不变 (Table 2: ρ ≈ 0.997, flip rate ≈ 0.062)。标题 \"Score Incomparability\" 设定了远超实际发现的期望。不过需要补充两点细微之处：(1) Section 4.6 和 Figure 6 表明 DIF-ordered item removal 比 random removal 更快降低排名一致性，说明 DIF 题目确实携带了结构化的不稳定信息；(2) 个别模型可移动多达 2,561 个排名位置（Section 4.6）。但我同意，aggregate-level 的近乎完美保持使 \"incomparability\" 一词失当。更准确的标题可能是 \"Temporal Item-Level Instability\" 或 \"Differential Item Functioning\"。\n\n**[REBUT] R2-W2: 方法论新颖性有限。**\n部分反驳。R2 正确指出核心统计方法 (MH-DIF, ETS, DEFF) 均非原创，但忽略了论文的方法论贡献不在于新统计量，而在于：(1) **Cross-subject matching** 虽源自 purified subtest matching (Swaminathan & Rogers, 1990)，但将其适配到 LLM multi-domain benchmark 设定下并推导出 ΔFPR=0 的构造性保证 (Section 3.4, Remark) 是非平凡的设计创新；(2) **Semi-synthetic injection framework** 将 contamination 建模为可控的 dose-response 实验（Figure 4），这在 DIF 文献中没有先例；(3) Section 5 系统性地识别了四个 LLM-specific challenges（local independence violation, within-family correlation, bimodal ability, multidimensionality）并给出了对应的方法论应对。对于 EMNLP 而言，方法论贡献不必是全新统计量——将成熟方法严谨地适配到新领域并通过大规模实证验证其有效性，本身就是有价值的贡献。当然，我同意论文应更清晰地标注哪些是已知方法、哪些是本文的适配创新。\n\n**[AGREE] R2-W3: C% 不确定性范围过大 (13.5%–31.3%)。**\n完全同意，这与我自己的 W1 一致。补充一点：这一不确定性的核心来源是 DEFF estimator 的选择——simple-mean vs weighted-mean（Section D, Table 10）。Weighted-mean DEFF 对 mega-families（如 Llama, Mistral）赋予过高权重可能导致 over-correction（Appendix D 讨论了这一点），但论文未提供判断两个 estimator 哪个更合适的独立证据。Cluster bootstrap CI [29.27%, 37.81%] 排除了 weighted-mean 的 13.5%，但 bootstrap 本身依赖于 family 定义的合理性（Appendix I: 30 families with ≥2 members）。我建议作者至少在 abstract 中报告校正后区间而非仅报告 raw 31.3%。\n\n**[AGREE] R2-W4: \"Mechanism-agnostic\" 定位与 contamination-focused 验证的张力。**\n同意这是一个重要的内部一致性问题。论文在 Section 5.1 声称 \"Temporal DIF detects *that* items function differently...not *why*\"，但 (1) 验证框架 (Section 3.4) 完全基于 contamination injection；(2) Section 4.3 花大量篇幅比较 DIF flags 与 web-overlap labels；(3) Discussion (Section 5.2) 建议基于 DIF 结果进行 contamination-motivated 的 item removal。如果方法真正 mechanism-agnostic，至少应包含一个非 contamination 来源的 DIF 验证（例如，模拟 \"training methodology shift\" 导致的 DIF，或利用已知的 format change 事件）。在此之前，\"mechanism-agnostic\" 的定位缺乏验证支撑。\n\n**[REBUT] R2-W5: DIF 在 LLM 场景下的概念合法性。**\n部分反驳。R2 正确指出 2023 vs 2024 模型不是 \"同一总体的人口学子群\"，但这并不使 DIF 分析无效——DIF 的核心问题是 \"controlling for overall ability, do items function differently across groups?\"，这一问题对任何可比较的两个群体都有意义，不限于人口学子群。教育测量中 DIF 也常用于跨时间群体 (如不同年份考生)，与本文设定类似。关于 κ=0.80 和多维性伪影：论文在 Section A.1 讨论了 Yen's Q3 diagnostic（11.3% of within-subject item pairs exceed Q3 ≥ 0.20），并通过 cross-subject matching 部分缓解了多维性问题（不同学科视为不同维度）。不过我同意论文应更深入讨论 \"LLM 的 total score 是否是一个有意义的 conditioning variable\"——这与我自己的 W5 (ETS 阈值迁移) 相关。\n\n**[AGREE] R2-W6: Contribution 3 (audit protocol) 权重不足。**\n同意。Section 5.2 的 Monitor/Triage/Correct 协议仅占半段，没有具体的实施案例、部署成本分析或用户研究。作为声明的三大贡献之一，这一部分显得单薄。建议要么降级为 \"future direction\"，要么扩展为独立 subsection 并提供至少一个模拟部署场景。\n\n---\n\n### Questions 回应\n\n**[AGREE] R2-Q1: 能否量化 temporal DIF 的实际危害？**\n同意这是论文缺失的关键信息。ρ ≈ 0.997 表明聚合排名几乎不受影响，那么 temporal DIF 的实际危害是什么？论文应提供具体场景：例如，(1) 哪些特定模型在 DIF item removal 前后排名变化最大？(2) 如果 practitioner 使用某个学科子集（而非全部 MMLU）评估模型，DIF 的影响是否被放大？(3) Figure 6 的 ranking degradation 在哪个 removal threshold 开始产生实质性影响？没有这些信息，读者难以判断 31% (或 13.5%) 的 DIF 率是否构成实际问题。\n\n**[AGREE] R2-Q2: 时间划分粒度的影响。**\n同意。论文报告 half-yearly C%=34.1% (Section 4.2)，高于 annual 31.3%。这一现象有两种解释：(1) 更细粒度捕获了更多真实的时序变化；(2) 更小的 cohort size 增加了统计噪声。论文未区分这两种可能性。此外，是否存在 \"突变点\" (change point)——例如某个特定时间窗口 DIF 突然增加——可以通过 rolling-window MH-DIF 分析来检验。这也与我自己的 Q4 相关。\n\n**[AGREE] R2-Q3: Base vs instruct 反转的解释。**\n完全同意，这与我自己的 W8 一致。RLHF/instruction tuning 系统性地改变了模型与 multiple-choice items 的交互方式（如输出格式偏好、refusal behavior、calibration 变化），这些都是 \"legitimate ability profile change\" 而非 item-level bias。论文的 χ²=562.7 (Section 4.3) 确认了方向反转的统计显著性，但未提供 DIF vs. impact 的分离证据。一个可能的测试：在 base-only 或 instruct-only 子群内进行 temporal DIF 分析，如果 DIF pattern 在子群内保持一致，则支持 item-level bias 解释；如果消失，则支持 composition shift 解释。论文在 Appendix O 分别报告了 base-only 和 instruct-only 的 temporal DIF (Table 15)，这部分应被提升到主文以回应此质疑。\n\n**[REBUT] R2-Q4: Non-contamination DIF 下 cross-subject matching 的行为。**\n部分反驳。R2 问 \"当 DIF 由全局训练方法变化驱动时 cross-subject matching 的行为如何\"——这个问题的前提需要澄清。Cross-subject matching 的设计目标是防止匹配变量被目标学科的 DIF 信号污染，而非区分 DIF 的来源。如果全局训练方法变化（如 RLHF）同时影响所有学科，cross-subject matching 仍然有效：它使用非目标学科的总分作为匹配变量，只要匹配变量能有效反映 \"ability\"（而非被污染），DIF 检测就有效。问题在于：当所有学科都受影响时，匹配变量本身反映了 \"post-method-change ability\"，而非 \"pure ability\"，这可能导致 cross-subject matching 低估 DIF（因为匹配变量已吸收了部分变化）。但这是 conservative bias（低估而非高估），不会导致 false positive inflation。所以 cross-subject matching 在 non-contamination DIF 场景下仍然是安全的，只是可能 under-powered。\n\n---\n\n### Missing References 回应\n\n**[AGREE] R2-M1: Rodriguez et al. (2021).** 同意，这是 IRT+NLP 评估的重要早期工作，应被引用。\n\n**[REBUT] R2-M2: Polo et al. (2024) \"tinyBenchmarks\".** 论文引用了 Polo et al. (Zhu et al., 2026) \"Benchmark health index\" (p10)。如果 R2 指的是另一篇 Polo et al. 2024 ICML 工作，需要确认具体引用。但 tinyBenchmarks 的 IRT 方法与本文的 DIF 分析在技术路线上差异较大（IRT 参数估计 vs. 非参数 DIF 检测），引用的必要性可讨论。\n\n**[AGREE] R2-M3: 最新 IRT+LLM 工作。** 同意，领域发展迅速，论文应确保引用最新的相关工作。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1: 标题 \"Score Incomparability\" 与 ρ ≈ 0.997 的叙事张力。**\n同意这是论文最突出的叙事问题。论文的核心发现实际上是 *item-level instability with aggregate robustness*——31% 的题目有大效应 DIF，但聚合排名几乎不变 (Table 2: ρ ≈ 0.997, flip rate ≈ 0.062)。标题 \"Score Incomparability\" 设定了远超实际发现的期望。不过需要补充两点细微之处：(1) Section 4.6 和 Figure 6 表明 DIF-ordered item removal 比 random removal 更快降低排名一致性，说明 DIF 题目确实携带了结构化的不稳定信息；(2) 个别模型可移动多达 2,561 个排名位置（Section 4.6）。但我同意，aggregate-level 的近乎完美保持使 \"incomparability\" 一词失当。更准确的标题可能是 \"Temporal Item-Level Instability\" 或 \"Differential Item Functioning\"。\n\n**[REBUT] R2-W2: 方法论新颖性有限。**\n部分反驳。R2 正确指出核心统计方法 (MH-DIF, ETS, DEFF) 均非原创，但忽略了论文的方法论贡献不在于新统计量，而在于：(1) **Cross-subject matching** 虽源自 purified subtest matching (Swaminathan & Rogers, 1990)，但将其适配到 LLM multi-domain benchmark 设定下并推导出 ΔFPR=0 的构造性保证 (Section 3.4, Remark) 是非平凡的设计创新；(2) **Semi-synthetic injection framework** 将 contamination 建模为可控的 dose-response 实验（Figure 4），这在 DIF 文献中没有先例；(3) Section 5 系统性地识别了四个 LLM-specific challenges（local independence violation, within-family correlation, bimodal ability, multidimensionality）并给出了对应的方法论应对。对于 EMNLP 而言，方法论贡献不必是全新统计量——将成熟方法严谨地适配到新领域并通过大规模实证验证其有效性，本身就是有价值的贡献。当然，我同意论文应更清晰地标注哪些是已知方法、哪些是本文的适配创新。\n\n**[AGREE] R2-W3: C% 不确定性范围过大 (13.5%–31.3%)。**\n完全同意，这与我自己的 W1 一致。补充一点：这一不确定性的核心来源是 DEFF estimator 的选择——simple-mean vs weighted-mean（Section D, Table 10）。Weighted-mean DEFF 对 mega-families（如 Llama, Mistral）赋予过高权重可能导致 over-correction（Appendix D 讨论了这一点），但论文未提供判断两个 estimator 哪个更合适的独立证据。Cluster bootstrap CI [29.27%, 37.81%] 排除了 weighted-mean 的 13.5%，但 bootstrap 本身依赖于 family 定义的合理性（Appendix I: 30 families with ≥2 members）。我建议作者至少在 abstract 中报告校正后区间而非仅报告 raw 31.3%。\n\n**[AGREE] R2-W4: \"Mechanism-agnostic\" 定位与 contamination-focused 验证的张力。**\n同意这是一个重要的内部一致性问题。论文在 Section 5.1 声称 \"Temporal DIF detects *that* items function differently...not *why*\"，但 (1) 验证框架 (Section 3.4) 完全基于 contamination injection；(2) Section 4.3 花大量篇幅比较 DIF flags 与 web-overlap labels；(3) Discussion (Section 5.2) 建议基于 DIF 结果进行 contamination-motivated 的 item removal。如果方法真正 mechanism-agnostic，至少应包含一个非 contamination 来源的 DIF 验证（例如，模拟 \"training methodology shift\" 导致的 DIF，或利用已知的 format change 事件）。在此之前，\"mechanism-agnostic\" 的定位缺乏验证支撑。\n\n**[REBUT] R2-W5: DIF 在 LLM 场景下的概念合法性。**\n部分反驳。R2 正确指出 2023 vs 2024 模型不是 \"同一总体的人口学子群\"，但这并不使 DIF 分析无效——DIF 的核心问题是 \"controlling for overall ability, do items function differently across groups?\"，这一问题对任何可比较的两个群体都有意义，不限于人口学子群。教育测量中 DIF 也常用于跨时间群体 (如不同年份考生)，与本文设定类似。关于 κ=0.80 和多维性伪影：论文在 Section A.1 讨论了 Yen's Q3 diagnostic（11.3% of within-subject item pairs exceed Q3 ≥ 0.20），并通过 cross-subject matching 部分缓解了多维性问题（不同学科视为不同维度）。不过我同意论文应更深入讨论 \"LLM 的 total score 是否是一个有意义的 conditioning variable\"——这与我自己的 W5 (ETS 阈值迁移) 相关。\n\n**[AGREE] R2-W6: Contribution 3 (audit protocol) 权重不足。**\n同意。Section 5.2 的 Monitor/Triage/Correct 协议仅占半段，没有具体的实施案例、部署成本分析或用户研究。作为声明的三大贡献之一，这一部分显得单薄。建议要么降级为 \"future direction\"，要么扩展为独立 subsection 并提供至少一个模拟部署场景。\n\n---\n\n### Questions 回应\n\n**[AGREE] R2-Q1: 能否量化 temporal DIF 的实际危害？**\n同意这是论文缺失的关键信息。ρ ≈ 0.997 表明聚合排名几乎不受影响，那么 temporal DIF 的实际危害是什么？论文应提供具体场景：例如，(1) 哪些特定模型在 DIF item removal 前后排名变化最大？(2) 如果 practitioner 使用某个学科子集（而非全部 MMLU）评估模型，DIF 的影响是否被放大？(3) Figure 6 的 ranking degradation 在哪个 removal threshold 开始产生实质性影响？没有这些信息，读者难以判断 31% (或 13.5%) 的 DIF 率是否构成实际问题。\n\n**[AGREE] R2-Q2: 时间划分粒度的影响。**\n同意。论文报告 half-yearly C%=34.1% (Section 4.2)，高于 annual 31.3%。这一现象有两种解释：(1) 更细粒度捕获了更多真实的时序变化；(2) 更小的 cohort size 增加了统计噪声。论文未区分这两种可能性。此外，是否存在 \"突变点\" (change point)——例如某个特定时间窗口 DIF 突然增加——可以通过 rolling-window MH-DIF 分析来检验。这也与我自己的 Q4 相关。\n\n**[AGREE] R2-Q3: Base vs instruct 反转的解释。**\n完全同意，这与我自己的 W8 一致。RLHF/instruction tuning 系统性地改变了模型与 multiple-choice items 的交互方式（如输出格式偏好、refusal behavior、calibration 变化），这些都是 \"legitimate ability profile change\" 而非 item-level bias。论文的 χ²=562.7 (Section 4.3) 确认了方向反转的统计显著性，但未提供 DIF vs. impact 的分离证据。一个可能的测试：在 base-only 或 instruct-only 子群内进行 temporal DIF 分析，如果 DIF pattern 在子群内保持一致，则支持 item-level bias 解释；如果消失，则支持 composition shift 解释。论文在 Appendix O 分别报告了 base-only 和 instruct-only 的 temporal DIF (Table 15)，这部分应被提升到主文以回应此质疑。\n\n**[REBUT] R2-Q4: Non-contamination DIF 下 cross-subject matching 的行为。**\n部分反驳。R2 问 \"当 DIF 由全局训练方法变化驱动时 cross-subject matching 的行为如何\"——这个问题的前提需要澄清。Cross-subject matching 的设计目标是防止匹配变量被目标学科的 DIF 信号污染，而非区分 DIF 的来源。如果全局训练方法变化（如 RLHF）同时影响所有学科，cross-subject matching 仍然有效：它使用非目标学科的总分作为匹配变量，只要匹配变量能有效反映 \"ability\"（而非被污染），DIF 检测就有效。问题在于：当所有学科都受影响时，匹配变量本身反映了 \"post-method-change ability\"，而非 \"pure ability\"，这可能导致 cross-subject matching 低估 DIF（因为匹配变量已吸收了部分变化）。但这是 conservative bias（低估而非高估），不会导致 false positive inflation。所以 cross-subject matching 在 non-contamination DIF 场景下仍然是安全的，只是可能 under-powered。\n\n---\n\n### Missing References 回应\n\n**[AGREE] R2-M1: Rodriguez et al. (2021).** 同意，这是 IRT+NLP 评估的重要早期工作，应被引用。\n\n**[REBUT] R2-M2: Polo et al. (2024) \"tinyBenchmarks\".** 论文引用了 Polo et al. (Zhu et al., 2026) \"Benchmark health index\" (p10)。如果 R2 指的是另一篇 Polo et al. 2024 ICML 工作，需要确认具体引用。但 tinyBenchmarks 的 IRT 方法与本文的 DIF 分析在技术路线上差异较大（IRT 参数估计 vs. 非参数 DIF 检测），引用的必要性可讨论。\n\n**[AGREE] R2-M3: 最新 IRT+LLM 工作。** 同意，领域发展迅速，论文应确保引用最新的相关工作。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-25T21:27:54.272360+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3666
}
```

</details>

---


### Assistant

_source line 1456 · 2026-05-25T21:27:59.738027+00:00_

交叉回应已提交。对 R2 的 6 个 Weaknesses：W1/W3/W4/W6 完全同意，W2/W5 部分反驳（cross-subject matching 适配和 DIF 概念合法性有辩护空间）。对 4 个 Questions：Q1/Q2/Q3 同意需要作者回应，Q4 部分反驳（cross-subject matching 在 non-contamination DIF 下仍安全，只是可能 under-powered）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---
