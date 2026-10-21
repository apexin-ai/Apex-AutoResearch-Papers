# Reviewer 1 coordination — Part 3 of 5

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../reviewer-1-coordination.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/d1/d148805112ce41231b9b.json)

## Round 29

### User

_source line 865 · 2026-05-18T04:24:40.454619+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2（新颖性/完整性）的完整审稿意见。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 2 的审稿意见

**Overall**: 3.0 (Findings)

**Strengths**:
[S1] 实验设计严谨：受控实验方法论是最大亮点
[S2] 全面的 Limitations 讨论
[S3] 跨任务对比揭示的任务不对称性有洞察价值
[S4] 负面结果的报告有价值
[S5] 可复现性高

**Weaknesses**:

**[W1] [major] SCS/BCS 指标新颖性不足，与 LLM-PEE 的差异化不清晰**
- SCS 本质上就是 type name embedding 的 pairwise cosine similarity，非常标准
- Abstract/Contribution #1-2 以 SCS/BCS 为核心卖点，但 Related Work 承认与 LLM-PEE 形式相同
- 增量论证偏弱：LLM-PEE 的 partitioning 基于相同原理，只是实验验证深度不同

**[W2] [major] Confusability 效应量过小，实际意义存疑**
- 典型 batch gap 仅 ~2.2pp，extreme-batch 对比 ~25pp
- Count 效应高达 −49pp，相比之下 confusability 效应极小
- 论文用大量篇幅分析 ~2pp 效应，practical significance 不足
- "Practical implications" 段仅声称 3-5pp 关联，不是因果

**[W3] [major] 因果语言与证据等级不匹配**
- "schema-induced degradation"、"count-related recall decline"、"BCS explains 22-53%"
- 实际证据是 correlational + controlled stratification，非 interventional
- Limitations #7 承认 no interventional causality，但 Abstract/Introduction 未反映
- 建议 "associated with" 替代 "explains"；"schema-induced" → "schema-associated"

**[W4] [major] SDGD 负面结果分析深度不足**
- Section 5 仅约 1 column 正文 + Table 3
- merge amplification 机制描述简短，无 k 值与 amplification 定量分析
- routing failure 仅报告 oracle 上界，无失败案例分析
- Future directions 均未验证
- 作为 claimed contribution 深度不够

**[W5] [minor] NER batch-level null result 作为独立 Contribution (#3) 有膨胀之嫌**
- 本质是主实验 sub-finding，不是方法论或框架层面的独立贡献
- 建议并入 Contribution #2

**[W6] [minor] MAVEN centrality confound 削弱广度声称**
- MAVEN 不参与主分析框架，核心发现实际只在 3 个数据集成立

**[W7] [minor] "First controlled study" 声称需要更谨慎限定**
- LLM-PEE 和 PARSE 隐式涉及 confusability 影响
- "First" 声称容易引发反感

**[W8] [minor] Cross-model validation 规模有限**
- 仅 3 个 architecture family，Gemini 不在主分析中

**Questions**:
[Q1] Name-only vs name+definition SCS: 为什么 definition embedding 没帮助？是否说明 SCS 捕获的是 name-level 表面相似度？
[Q2] BCS 在 NER 上为 null 是否说明 BCS 本身不适用于 NER（因 error mode 根本不同），而非 confusability 在 NER 中不存在？
[Q3] BCS-Controlled batch 构建如何保证不是 trivially easy vs trivially hard 的对比？
[Q4] Oracle routing 在 RE 上恢复 +29.8pp 但 practical routing 全部低于 single-pass——这是否说明 SDGD 本身不适用于 RE？
[Q5] Abstract 中 "Few-shot demonstrations do not reduce the gap" 的 "the gap" 指代不明。

**Missing References**: GoLLIE (Sainz et al., ICLR 2024); Schema as Parameterized Tools for Universal IE (2025)

---

请逐条给出你的 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-18T04:26:53.654545+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: SCS/BCS 指标新颖性不足**\n\n同意 R2 的核心判断。论文自身在 Related Work §2 最后一段（\"SCS novelty\"）已明确承认\"SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE\"，并声明\"Our contribution is not the metric itself but the controlled experimental framework\"。然而 Abstract 和 Contribution #2 的措辞（\"We validate that pairwise embedding similarity predicts type confusion\"）仍以 SCS/BCS 为核心卖点，与 Related Work 中的自我定位不一致。建议在 Contribution 列表中将重心从 metric 本身转移到 experimental framework 和 findings 上。\n\n不过，需要补充的是：LLM-PEE 使用 embedding similarity 做 partitioning 工程，但没有做 controlled experiments 来验证 confusability 是否独立于 count 预测 degradation。论文的增量不在指标本身，而在 BCS-controlled 实验范式（固定 count 变化 BCS，§3.3 Experiment 2）和 within-pool 分析（Table 6）。这个方法论增量是实质性的，但论文的 framing 未能突出这一点。\n\n**[PARTIALLY AGREE] R2-W2: Confusability 效应量过小**\n\n部分同意。R2 指出 typical-batch gap 仅 2.2pp（§5.3, CI [0.4, 4.0]），相比 count 效应的 -49pp 确实很小，实际意义有限。这与我在 N2 中的 concern 一致。\n\n但我认为 R2 的论述忽略了两点：(1) 本文是 analytical study 而非 engineering paper——目标是 characterize degradation 的成因而非提供大幅度改进方案。小但 real 的效应在分析性研究中是可接受的 contribution（ACL ARR reviewer guidelines 明确反对 H5: \"treating SOTA achievement as necessary\"）。(2) Batch-level R²=0.22 意味着在 schema design 时 BCS 是一个 non-trivial predictor，即使 typical gap 小，对大规模部署（数万次抽取）来说累积效应可能有意义。\n\nR2 的合理建议是论文应更坦诚地在 Abstract/Introduction 中呈现 typical-batch magnitude（2.2pp），而非以 extreme-batch 数字（25-31pp）为主导叙事。这点我在 N2 中已独立提出。\n\n**[PARTIALLY AGREE] R2-W3: 因果语言与证据不匹配**\n\n部分同意。R2 区分了两类用语：\n- \"BCS explains 22-53% of variance\"：这是标准回归术语（R² 字面意思就是 \"variance explained\"），在统计学中不暗示因果关系。R2 建议改为 \"associated with\" 会使语言不够精确——R² 就是 \"explained variance\"。**此处 REBUT。**\n- \"schema-induced degradation\"（title 和全文多次出现）：这确实暗示因果方向。论文的证据是 correlational + controlled stratification，不是 interventional。Limitations §7 承认 \"The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway\"。但 title 和 Abstract 未反映这个 qualification。**此处 AGREE。**\n\n建议：title 中的 \"schema-induced\" 可弱化为 \"schema-associated\" 或保持 \"schema complexity\" 的 predictive framing（当前 title \"How Does Schema Complexity Predict Performance\" 实际上已经是 predictive 而非 causal 的措辞，比正文中的 \"schema-induced\" 更准确）。正文中 \"schema-induced degradation\" 改为 \"schema-associated degradation\" 更准确。\n\n**[PARTIALLY AGREE] R2-W4: SDGD 负面结果分析深度不足**\n\n部分同意 R2 的观察但不同意严重程度判断。\n\n同意：(1) merge amplification 的 quantitative analysis 确实不足——论文仅报告了 precision 从 0.563→0.210 的整体下降，但没有分析 k 值（decomposition passes 数量）与 false positive 增长的定量关系。如果 merge amplification 随 k 线性增长 vs 超线性增长，对 future mitigation 策略的指导完全不同。(2) Routing failure 仅报告了 5 种 strategy 的 accuracy（Table 7），没有 error analysis（哪些 instances 被错误路由？是 BCS 最高的 sub-schema 间的 confusion 还是 uniform failure？）。\n\n反驳严重程度：作为 Contribution #4 的负面结果，§6 + Appendix B/C 的深度在 NLP 论文中已属充分。负面结果的价值在于 (a) 证明 naive decomposition 不 work，(b) 诊断出 bottleneck（merge vs routing），(c) 量化 upper bound（oracle +29.8pp）。R2 要求的 k-value analysis 和 failure case analysis 是 reasonable suggestions 但不构成 rejection-level concern。\n\n**[REBUT] R2-W5: NER batch-level null result 不应作为独立 Contribution**\n\n不同意。Contribution #3 不仅仅是\"NER 上 BCS 不 work\"这个 null result，而是揭示了一个结构性的 task asymmetry：pairwise SCS-confusion correlation 在 NER 上显著（r=0.112, p<0.001, Table 2），但这个 signal 在 batch level 消失（r≈0, n=450, §5.3）。这个\"pairwise signal exists but doesn't aggregate\"的现象有独立的分析价值，它的解释（missed entities 43-65% overwhelm type substitution signal, §5.4 和 Figure 3）揭示了 NER 和 RE 的 error mode 根本差异。\n\n如果把这个并入 Contribution #2，会弱化\"BCS 的 task-dependent applicability\"这个 finding——这对想使用 BCS 做 schema design 的 practitioners 是重要的边界信息。\n\n**[AGREE] R2-W6: MAVEN centrality confound 削弱广度声称**\n\n同意。MAVEN 的 per-type/batch-level BCS 分析因 centrality confound 实际不可用（§5.5），仅 pairwise SCS-confusion 仍显著（r=0.129, Table 2）。论文声称\"four datasets\"但 MAVEN 的参与度明显弱于其他三个。我在审稿中未单独提出此问题，但 R2 的观察准确。\n\n建议在 Contribution 措辞中将\"four datasets\"改为\"three primary datasets (Few-NERD, FewRel, DocRED) with supplementary evidence from MAVEN\"，更准确地反映 MAVEN 的角色。\n\n**[REBUT] R2-W7: \"First controlled study\" 声称需更谨慎限定**\n\n不同意。论文的 claim 是 \"first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE\"（§1），不是 \"first study of confusability\"。R2 提到 LLM-PEE 和 PARSE \"隐式涉及 confusability 影响\"，但：\n- LLM-PEE（§2, Related Work）使用 embedding similarity 做 partitioning，但没有 controlled experiments 隔离 count 和 confusability。它的实验是 engineering evaluation（decomposition 后性能是否提升），不是 analytical isolation。\n- PARSE 优化 schema definitions，更不涉及 confusability 的 controlled analysis。\n\n\"First controlled study isolating X from Y\" 是一个 sufficiently qualified claim，因为它限定了方法（controlled isolation via stratified design）和范围（zero-shot LLM IE）。当然，如果有已发表工作确实做了同样的 controlled isolation，这个 claim 就不成立——但 R2 未给出这样的 counterexample。\n\n**[AGREE] R2-W8: Cross-model validation 规模有限**\n\n同意，与我的 W3 一致。3 个 architecture family（Qwen3, LLaMA, Gemini）对于 \"fundamental property of in-context learning\" 的 claim 不足。Gemini 仅验证 Dimension 1，Dimension 2 在 proprietary models 上完全未验证。\n\n---\n\n### Questions 逐条回应\n\n**[Q1] Name-only vs definition SCS**\n\nR2 的推测有道理但论文提供了 partial evidence against。Appendix §G Table 8 显示 matrix correlation 0.66-0.89，说明 name-only 和 name+definition SCS 高度一致。论文解释（§3.2）是 MAVEN/FewRel prompts 本身就只使用 type names，所以 name-only SCS 直接匹配 model input。只有 Few-NERD 的 prompts 包含 definitions。但 R2 的更深层问题——SCS 是否只 capture surface-level name similarity 而非 semantic confusability——是 valid concern，可以通过 random-label experiments 来测试。\n\n**[Q2] BCS 不适用于 NER**\n\nR2 的解读与论文一致。§5.4 和 Discussion 明确指出 NER errors dominated by missed entities (43-65%)，batch-level confusability 被 boundary detection failures 淹没。论文的结论确实是\"BCS 不适用于 NER batch-level prediction\"（不是\"confusability 在 NER 中不存在\"），因为 pairwise SCS-confusion 仍然显著（Table 2, r=0.112）。R2 的表述准确。\n\n**[Q3] BCS-Controlled batch 的 trivially easy/hard 问题**\n\n论文在 Appendix §M 提供了明确回答：variance decomposition 显示 BCS unique R²=0.259 (36.8%), composition unique R²=0.298 (42.3%), shared R²=0.147 (20.9%)，VIF=1.06，r(BCS, difficulty)=-0.21。这表明 BCS 和 type difficulty 近乎正交，extreme-batch 对比不是 trivially easy vs hard。Within-pool 分析（Table 6）进一步控制了 pool composition。我认为这个问题论文已充分 address。\n\n**[Q4] SDGD 不适用于 RE**\n\nR2 的解读本质上正确，这也是论文的结论（§6: \"all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema\"）。但论文的 framing 是\"routing failure\"而非\"SDGD 不适用于 RE\"——前者暗示 routing 可以改进，后者暗示 fundamental limitation。考虑到 constrained decoding 消除了 calibration signal（none-rate 仅 20-40%），这更像是 constrained decoding 的问题而非 SDGD 的 inherent limitation。\n\n**[Q5] Abstract 中 \"the gap\" 指代不明**\n\n同意。Abstract 中 \"Few-shot demonstrations do not reduce the gap (+4.3pp under 5-shot)\" 的 \"the gap\" 指 BCS gap（低 BCS vs 高 BCS accuracy 差异），但 Abstract 前文讨论的是 count-related decline 和 confusability-related substitution 两种 gap，读者无法确定指哪个。应改为 \"Few-shot demonstrations do not reduce the confusability gap\" 或类似更明确的表述。\n\n---\n\n### Missing References\n\n**GoLLIE (Sainz et al., ICLR 2024)**：已在 references.bib 中引用（gollie-2024），且在 Related Work §2 第一段被引用。R2 可能遗漏了这个引用。\n\n**\"Schema as Parameterized Tools for Universal IE\"**：不确定 R2 指的是哪篇具体论文。如果是指 OneKE (Luo et al., 2025) 或类似的 schema-as-tools 框架，论文已引用 oneke-2025。如果是另一篇 2025 年论文，需要 R2 提供具体 citation 以核实。\n\n---\n\n### 总体评估\n\nR2 给出 Overall 3.0 (Findings)。我认为 R2 的评分偏低。R2 的核心 concerns 可归纳为：(1) SCS 新颖性（valid but the novelty is in the experimental framework, not the metric）；(2) 效应量小（valid concern about framing but acceptable for an analytical study）；(3) 因果语言（partially valid, mostly a writing fix）；(4) SDGD 深度（valid suggestion but not rejection-level）。\n\n这些问题大多可通过 revision 修复（reframing claims, weakening causal language, adding DocRED CI），不构成 fundamental methodological flaws。我维持 3.5 (Borderline Conference) 的评分——论文的实验设计精巧度和统计严谨性在 NLP 领域中突出，但 framing/overclaim 问题拉低了整体印象。\n",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: SCS/BCS 指标新颖性不足**\n\n同意 R2 的核心判断。论文自身在 Related Work §2 最后一段（\"SCS novelty\"）已明确承认\"SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE\"，并声明\"Our contribution is not the metric itself but the controlled experimental framework\"。然而 Abstract 和 Contribution #2 的措辞（\"We validate that pairwise embedding similarity predicts type confusion\"）仍以 SCS/BCS 为核心卖点，与 Related Work 中的自我定位不一致。建议在 Contribution 列表中将重心从 metric 本身转移到 experimental framework 和 findings 上。\n\n不过，需要补充的是：LLM-PEE 使用 embedding similarity 做 partitioning 工程，但没有做 controlled experiments 来验证 confusability 是否独立于 count 预测 degradation。论文的增量不在指标本身，而在 BCS-controlled 实验范式（固定 count 变化 BCS，§3.3 Experiment 2）和 within-pool 分析（Table 6）。这个方法论增量是实质性的，但论文的 framing 未能突出这一点。\n\n**[PARTIALLY AGREE] R2-W2: Confusability 效应量过小**\n\n部分同意。R2 指出 typical-batch gap 仅 2.2pp（§5.3, CI [0.4, 4.0]），相比 count 效应的 -49pp 确实很小，实际意义有限。这与我在 N2 中的 concern 一致。\n\n但我认为 R2 的论述忽略了两点：(1) 本文是 analytical study 而非 engineering paper——目标是 characterize degradation 的成因而非提供大幅度改进方案。小但 real 的效应在分析性研究中是可接受的 contribution（ACL ARR reviewer guidelines 明确反对 H5: \"treating SOTA achievement as necessary\"）。(2) Batch-level R²=0.22 意味着在 schema design 时 BCS 是一个 non-trivial predictor，即使 typical gap 小，对大规模部署（数万次抽取）来说累积效应可能有意义。\n\nR2 的合理建议是论文应更坦诚地在 Abstract/Introduction 中呈现 typical-batch magnitude（2.2pp），而非以 extreme-batch 数字（25-31pp）为主导叙事。这点我在 N2 中已独立提出。\n\n**[PARTIALLY AGREE] R2-W3: 因果语言与证据不匹配**\n\n部分同意。R2 区分了两类用语：\n- \"BCS explains 22-53% of variance\"：这是标准回归术语（R² 字面意思就是 \"variance explained\"），在统计学中不暗示因果关系。R2 建议改为 \"associated with\" 会使语言不够精确——R² 就是 \"explained variance\"。**此处 REBUT。**\n- \"schema-induced degradation\"（title 和全文多次出现）：这确实暗示因果方向。论文的证据是 correlational + controlled stratification，不是 interventional。Limitations §7 承认 \"The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway\"。但 title 和 Abstract 未反映这个 qualification。**此处 AGREE。**\n\n建议：title 中的 \"schema-induced\" 可弱化为 \"schema-associated\" 或保持 \"schema complexity\" 的 predictive framing（当前 title \"How Does Schema Complexity Predict Performance\" 实际上已经是 predictive 而非 causal 的措辞，比正文中的 \"schema-induced\" 更准确）。正文中 \"schema-induced degradation\" 改为 \"schema-associated degradation\" 更准确。\n\n**[PARTIALLY AGREE] R2-W4: SDGD 负面结果分析深度不足**\n\n部分同意 R2 的观察但不同意严重程度判断。\n\n同意：(1) merge amplification 的 quantitative analysis 确实不足——论文仅报告了 precision 从 0.563→0.210 的整体下降，但没有分析 k 值（decomposition passes 数量）与 false positive 增长的定量关系。如果 merge amplification 随 k 线性增长 vs 超线性增长，对 future mitigation 策略的指导完全不同。(2) Routing failure 仅报告了 5 种 strategy 的 accuracy（Table 7），没有 error analysis（哪些 instances 被错误路由？是 BCS 最高的 sub-schema 间的 confusion 还是 uniform failure？）。\n\n反驳严重程度：作为 Contribution #4 的负面结果，§6 + Appendix B/C 的深度在 NLP 论文中已属充分。负面结果的价值在于 (a) 证明 naive decomposition 不 work，(b) 诊断出 bottleneck（merge vs routing），(c) 量化 upper bound（oracle +29.8pp）。R2 要求的 k-value analysis 和 failure case analysis 是 reasonable suggestions 但不构成 rejection-level concern。\n\n**[REBUT] R2-W5: NER batch-level null result 不应作为独立 Contribution**\n\n不同意。Contribution #3 不仅仅是\"NER 上 BCS 不 work\"这个 null result，而是揭示了一个结构性的 task asymmetry：pairwise SCS-confusion correlation 在 NER 上显著（r=0.112, p<0.001, Table 2），但这个 signal 在 batch level 消失（r≈0, n=450, §5.3）。这个\"pairwise signal exists but doesn't aggregate\"的现象有独立的分析价值，它的解释（missed entities 43-65% overwhelm type substitution signal, §5.4 和 Figure 3）揭示了 NER 和 RE 的 error mode 根本差异。\n\n如果把这个并入 Contribution #2，会弱化\"BCS 的 task-dependent applicability\"这个 finding——这对想使用 BCS 做 schema design 的 practitioners 是重要的边界信息。\n\n**[AGREE] R2-W6: MAVEN centrality confound 削弱广度声称**\n\n同意。MAVEN 的 per-type/batch-level BCS 分析因 centrality confound 实际不可用（§5.5），仅 pairwise SCS-confusion 仍显著（r=0.129, Table 2）。论文声称\"four datasets\"但 MAVEN 的参与度明显弱于其他三个。我在审稿中未单独提出此问题，但 R2 的观察准确。\n\n建议在 Contribution 措辞中将\"four datasets\"改为\"three primary datasets (Few-NERD, FewRel, DocRED) with supplementary evidence from MAVEN\"，更准确地反映 MAVEN 的角色。\n\n**[REBUT] R2-W7: \"First controlled study\" 声称需更谨慎限定**\n\n不同意。论文的 claim 是 \"first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE\"（§1），不是 \"first study of confusability\"。R2 提到 LLM-PEE 和 PARSE \"隐式涉及 confusability 影响\"，但：\n- LLM-PEE（§2, Related Work）使用 embedding similarity 做 partitioning，但没有 controlled experiments 隔离 count 和 confusability。它的实验是 engineering evaluation（decomposition 后性能是否提升），不是 analytical isolation。\n- PARSE 优化 schema definitions，更不涉及 confusability 的 controlled analysis。\n\n\"First controlled study isolating X from Y\" 是一个 sufficiently qualified claim，因为它限定了方法（controlled isolation via stratified design）和范围（zero-shot LLM IE）。当然，如果有已发表工作确实做了同样的 controlled isolation，这个 claim 就不成立——但 R2 未给出这样的 counterexample。\n\n**[AGREE] R2-W8: Cross-model validation 规模有限**\n\n同意，与我的 W3 一致。3 个 architecture family（Qwen3, LLaMA, Gemini）对于 \"fundamental property of in-context learning\" 的 claim 不足。Gemini 仅验证 Dimension 1，Dimension 2 在 proprietary models 上完全未验证。\n\n---\n\n### Questions 逐条回应\n\n**[Q1] Name-only vs definition SCS**\n\nR2 的推测有道理但论文提供了 partial evidence against。Appendix §G Table 8 显示 matrix correlation 0.66-0.89，说明 name-only 和 name+definition SCS 高度一致。论文解释（§3.2）是 MAVEN/FewRel prompts 本身就只使用 type names，所以 name-only SCS 直接匹配 model input。只有 Few-NERD 的 prompts 包含 definitions。但 R2 的更深层问题——SCS 是否只 capture surface-level name similarity 而非 semantic confusability——是 valid concern，可以通过 random-label experiments 来测试。\n\n**[Q2] BCS 不适用于 NER**\n\nR2 的解读与论文一致。§5.4 和 Discussion 明确指出 NER errors dominated by missed entities (43-65%)，batch-level confusability 被 boundary detection failures 淹没。论文的结论确实是\"BCS 不适用于 NER batch-level prediction\"（不是\"confusability 在 NER 中不存在\"），因为 pairwise SCS-confusion 仍然显著（Table 2, r=0.112）。R2 的表述准确。\n\n**[Q3] BCS-Controlled batch 的 trivially easy/hard 问题**\n\n论文在 Appendix §M 提供了明确回答：variance decomposition 显示 BCS unique R²=0.259 (36.8%), composition unique R²=0.298 (42.3%), shared R²=0.147 (20.9%)，VIF=1.06，r(BCS, difficulty)=-0.21。这表明 BCS 和 type difficulty 近乎正交，extreme-batch 对比不是 trivially easy vs hard。Within-pool 分析（Table 6）进一步控制了 pool composition。我认为这个问题论文已充分 address。\n\n**[Q4] SDGD 不适用于 RE**\n\nR2 的解读本质上正确，这也是论文的结论（§6: \"all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema\"）。但论文的 framing 是\"routing failure\"而非\"SDGD 不适用于 RE\"——前者暗示 routing 可以改进，后者暗示 fundamental limitation。考虑到 constrained decoding 消除了 calibration signal（none-rate 仅 20-40%），这更像是 constrained decoding 的问题而非 SDGD 的 inherent limitation。\n\n**[Q5] Abstract 中 \"the gap\" 指代不明**\n\n同意。Abstract 中 \"Few-shot demonstrations do not reduce the gap (+4.3pp under 5-shot)\" 的 \"the gap\" 指 BCS gap（低 BCS vs 高 BCS accuracy 差异），但 Abstract 前文讨论的是 count-related decline 和 confusability-related substitution 两种 gap，读者无法确定指哪个。应改为 \"Few-shot demonstrations do not reduce the confusability gap\" 或类似更明确的表述。\n\n---\n\n### Missing References\n\n**GoLLIE (Sainz et al., ICLR 2024)**：已在 references.bib 中引用（gollie-2024），且在 Related Work §2 第一段被引用。R2 可能遗漏了这个引用。\n\n**\"Schema as Parameterized Tools for Universal IE\"**：不确定 R2 指的是哪篇具体论文。如果是指 OneKE (Luo et al., 2025) 或类似的 schema-as-tools 框架，论文已引用 oneke-2025。如果是另一篇 2025 年论文，需要 R2 提供具体 citation 以核实。\n\n---\n\n### 总体评估\n\nR2 给出 Overall 3.0 (Findings)。我认为 R2 的评分偏低。R2 的核心 concerns 可归纳为：(1) SCS 新颖性（valid but the novelty is in the experimental framework, not the metric）；(2) 效应量小（valid concern about framing but acceptable for an analytical study）；(3) 因果语言（partially valid, mostly a writing fix）；(4) SDGD 深度（valid suggestion but not rejection-level）。\n\n这些问题大多可通过 revision 修复（reframing claims, weakening causal language, adding DocRED CI），不构成 fundamental methodological flaws。我维持 3.5 (Borderline Conference) 的评分——论文的实验设计精巧度和统计严谨性在 NLP 领域中突出，但 framing/overclaim 问题拉低了整体印象。\n",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-18T04:26:57.824887+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4170
}
```

</details>

---


### Assistant

_source line 868 · 2026-05-18T04:27:08.963541+00:00_

交叉回应已提交。

总结：对 R2 的 8 条 Weaknesses，我的回应分布为：
- **AGREE**: W1 (SCS 新颖性)、W6 (MAVEN 广度)、W8 (cross-model 有限)
- **PARTIALLY AGREE**: W2 (效应量 framing)、W3 (因果语言)、W4 (SDGD 深度)
- **REBUT**: W5 (NER null 作为独立 Contribution 有独立分析价值)、W7 ("First controlled study" 限定足够)

核心分歧在 Overall 评分：R2 给 3.0 (Findings)，我维持 3.5 (Borderline Conference)。R2 的主要 concerns 多为 framing/writing 问题，可通过 revision 修复，不构成 fundamental methodological flaws。论文的实验设计和统计严谨性是实质性优势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 30

## Round 30

42 recorded events


### User

_source line 869 · 2026-05-18T05:25:12.046636+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计论证**。

## 论文信息
- **标题**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
- **论文路径**: `projects/schema-dag-extraction/docs/paper/main.tex`（含 \input 的 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）
- **目标 venue**: EMNLP 2026 via ARR May 2026 cycle
- **截止日期**: 2026-05-25
- **格式**: ACL 模板 long paper, 正文 ≤ 8 页 (不含 references + Limitations), double-blind, Limitations section 必填
- **匿名**: double-blind (论文 \author{Anonymous})

## 你的审查侧重

**核心关注**:
1. **统计方法论**: TOST equivalence testing (±3pp margin) 的合理性; linear vs logit scale 选择; 等价检验 power 是否充分; 多重比较处理
2. **实验设计**: BCS-controlled 实验的 confound 控制; count curve 设计; within-pool vs independent pool 对比的有效性; 样本量 (n=25 vs n=5) 对结论的影响
3. **效应量与实际意义**: pairwise r²=1.3-1.7% 和 typical batch gap 2.2pp 的 practical significance; 22-53% R² claim 的稳健性 (尤其 DocRED n=25 的 53%)
4. **跨模型验证**: 3 个模型 family 是否充分支撑 generalizability claim; Dimension 2 仅在 open-weight RE 验证的局限
5. **因果语言**: Title "Predict" vs 正文中是否有残余因果措辞 ("induced", "driven", "shape" 等)
6. **SDGD 负面结果**: merge amplification 和 routing failure 的诊断深度

**交付物**: 完整审稿报告, 含 Summary (2-3 句), Strengths (逐条), Weaknesses (逐条, severity 标注 critical/major/minor), Questions, Missing References, Overall Assessment (用 ARR/EMNLP 评分标准 1-5 分)。

严格、客观、不留情面。你是评审人, 不是投稿人的盟友。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-18T05:25:18.893787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-18T05:25:19.196283+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-18T05:25:19.247066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 873 · 2026-05-18T05:25:19.600277+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 (count-associated decline) has been validated on a proprietary model (Gemini 2.5 Flash, $\rho = -0.900$, $p = 0.037$; Appendix~\ref{sec:appendix_cross_model_gemini}); Dimension~2 (confusability-associated type substitution) has been verified only on open-weight models. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded association ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rat
…[truncated 48827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-18T05:25:25.385633+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-18T05:25:25.738387+00:00_

1	\begin{abstract}
2	As large language models are increasingly deployed for information extraction without task-specific training, understanding how schema design affects extraction quality becomes critical for reliable deployment. Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors across NER, RE, and event detection on four datasets and operationalize confusability via the Schema Confusability Score (SCS) and its batch-level aggregation (BCS). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp, document-level RE at full schema) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); BCS explains 22--53\% of cross-batch RE accuracy variance but not NER, where boundary detection failures overwhelm the signal. Few-shot demonstrations do not reduce the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). These patterns replicate across model scales (8B to 70B) and architecture families (Qwen, LLaMA, Gemini), which suggests schema-associated degradation is consistent across tested model families rather than a model-specific artifact.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-18T05:25:25.789026+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-18T05:25:26.341502+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accur
…[truncated 3254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-18T05:25:26.392222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 879 · 2026-05-18T05:25:26.693998+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting 
…[truncated 3002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-18T05:25:26.694457+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-18T05:25:27.250539+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate th
…[truncated 8143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 556
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-18T05:25:27.251054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-18T05:25:27.653434+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\pm 1$\,SD across 3 seeds (42, 123, 456) $\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), ; schema configu
…[truncated 11051 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-18T05:25:27.653828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-18T05:25:28.106577+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapsing (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation thus recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation \citep{jagannatha2020calibrating} to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\re
…[truncated 535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-18T05:25:28.107542+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-18T05:25:28.560327+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED slope $-$0.71, adjusted $R^2 = 0.51$, 95\% CI [0.27, 0.73]) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%) because ${\sim}89\%$ of type pairs never confuse; among the 11\% with nonzero confusion, conditional $R^2$ rises to 7\%. Correlated pair-level signals aggregate at batch level: a Monte Carlo simulation (Appendix~\ref{app:aggregation-sim}) predicts batch $R^2$ of 18--25\%, consistent with the observed 22--53\% in RE. SCS is thus a weak pair-level predictor but a useful batch-level screen.
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific: BCS explains 22--53\% of cross-batch accuracy variance in RE but shows no correlation with NER F1 ($r \approx 0$, $n = 450$). RE's constrained decoding (enum constraint over valid type labels) channels all errors into type substitution (IntraSub scales with BCS; \S\ref{sec:multi_channel}), so batch confusability directly predicts accuracy. NER uses unconstrained generation, where errors scatter across missed entities (43--65\%), boundary misalignment, and hallucinated types, diluting the pairwise signal at batch level.
12	
13	\paragraph{Practical implications.}
14	The bounded count$\times$confusability interaction (0.47\,pp, TOST $p = 0.003$) implies no confusability amplification at scale. For RE, upper-SCS-quartile type pairs show 3--5\,pp accuracy diff
…[truncated 1309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-18T05:25:28.560797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 889 · 2026-05-18T05:25:29.114133+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{lla
…[truncated 4522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-18T05:25:29.114509+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-18T05:25:29.165116+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-18T05:25:34.341508+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
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

_source line 893 · 2026-05-18T05:25:34.342486+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-18T05:25:35.649705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-18T05:25:36.153185+00:00_

1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	@article{gemini-2025,
6	  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},
7	  author    = {Comanici, Gheorghe and others},
8	  journal   = {arXiv preprint arXiv:2507.06261},
9	  year      = {2025},
10	  url       = {https://arxiv.org/abs/2507.06261}
11	}
12	
13	@inproceedings{snell2017prototypical,
14	  title     = {Prototypical Networks for Few-shot Learning},
15	  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},
16	  booktitle = {Advances in Neural Information Processing Systems},
17	  volume    = {30},
18	  year      = {2017}
19	}
20	
21	@inproceedings{muller2019when,
22	  title     = {When Does Label Smoothing Help?},
23	  author    = {M{\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},
24	  booktitle = {Advances in Neural Information Processing Systems},
25	  volume    = {32},
26	  year      = {2019}
27	}
28	
29	@inproceedings{peterson2019human,
30	  title     = {Human Uncertainty Makes Classification More Robust},
31	  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},
32	  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},
33	  pages     = {9617--9626},
34	  year      = {2019}
35	}
36	
37	@inproceedings{jagannatha2020calibrating,
38	  title     = {Calibrating Structured Output Predictors for Natural Language Processing},
39	  author    = {Jagannatha, Abhyuday and Yu, Hong},
40	  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
41	  pages     = {2078--2092},
42	  year      = {2020}
43	}
44	
45	@article{willard2023efficient,
46	  title     = {Efficient Guided Generation for Large Language Models},
47	  author    = {Willard, Brandon T. and Louf, R{\'e}mi},
48	  journal   = {arXiv preprint arXiv:2307.09702}
…[truncated 29746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-18T05:25:40.543639+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines dimensions"
  }
}
```

</details>

---


### Tool call

_source line 897 · 2026-05-18T05:25:41.298430+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer form soundness excitement overall assessment 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer form soundness excitement overall assessment 2025"
  }
}
```

</details>

---


### Tool result

_source line 898 · 2026-05-18T05:25:47.730138+00:00_

Web search results for query: "ACL Rolling Review reviewer form soundness excitement overall assessment 2025"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/acguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/acguidelines.md"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) reviewer form and its scoring components:

## ACL Rolling Review S
…[truncated 1293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6431
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-18T05:25:47.931669+00:00_

Web search results for query: "ACL ARR review form criteria 2025 2026 reviewer guidelines dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I found information about ACL ARR review form criteria for 2025-2026. Here are the key details about the reviewer guidelines and evaluation dimensions:

## R
…[truncated 1442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7388
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-18T05:25:55.623536+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-18T05:25:55.774710+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-18T05:26:00.602099+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 etc.), descriptions of each score level, and any other required fields. I need the exact wording for Soundness, Excitement, Overall Assessment, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 etc.), descriptions of each score level, and any other required fields. I need the exact wording for Soundness, Excitement, Overall Assessment, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 903 · 2026-05-18T05:26:02.012025+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, scoring criteria, what constitutes a good review, any specific instructions about soundness, novelty, reproducibility, confidence scores, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, scoring criteria, what constitutes a good review, any specific instructions about soundness, novelty, reproducibility, confidence scores, etc."
  }
}
```

</details>

---


### Tool result

_source line 904 · 2026-05-18T05:26:07.789453+00:00_

# ARR Review Form - Scoring Dimensions

## 1. Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure. I tried to check the important points carefully"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

## 2. Soundness
**Scale: 1-5 (with 0.5 increments)**
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all of its claims"
- 3: "Acceptable: This study provides sufficient support for its main claims"
- 2: "Poor: Some of the main claims are not sufficiently supported"
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. Excitement
**Scale: 1-5 (with 0.5 increments)**
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points of this paper to others"
- 2: "Potentially Interesting: this paper does not resonate with me"
- 1: "Not Exciting: this paper does not resonate with me"

## 4. Overall Assessment
**Scale: 1-5 (with 0.5 increments)**
- 5: "Consider for Award: outstanding paper award consideration"
- 4: "Conference: could be accepted to an ACL conference"
- 3: "Findings: could be accepted to Findings of the ACL"
- 2: "Resubmit next cycle: needs substantial revisions"
- 1: "Do not resubmit: fully redone or not relevant"

## 5. Reproducibility
**Scale: 1-5**
- 5: "They could easily reproduce the results"
- 4: "They could mostly reproduce the results"
- 3: "They could reproduce with some difficulty"
- 2: "They would be hard pressed to reproduce"
- 1: "They would not be able to reproduce"

## 6. Datasets & Software Value
**Scale: 1-5** (identical scales for both)
- 5: "Enabling: should affect research project choices"
- 4: "
…[truncated 395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7187
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-18T05:26:15.531640+00:00_

# ARR Reviewer Guidelines Summary

## Core Review Tasks

Reviewers must complete four main tasks:

1. **Allocate time** for reviewing and discussion periods
2. **Check assignments** for expertise fit and conflicts of interest
3. **Write a strong review** following specific standards
4. **Update assessments** based on author responses

## What Reviewers Should Evaluate

### Soundness Assessment
Reviewers evaluate technical correctness, validity of arguments, and methodological rigor. The soundness score "must be justified by the text of the review."

### Key Evaluation Areas
- **Clarity**: Research questions and contributions should be "sufficiently clear what knowledge gap the authors are addressing"
- **Methodology**: Technical soundness, appropriate methodology selection, and valid argumentation
- **Reproducibility**: Sufficient detail for replicating experiments, including hyperparameter information
- **Novelty**: Whether contributions are genuinely new, though "novel methods tend to be harder to publish"
- **Experimental validity**: Sound statistical analysis, appropriate claim scoping, and fair baseline comparisons

## Scoring Criteria (As of February 2025)

ARR uses **three distinct scores**:

1. **Soundness**: Technical and methodological validity
2. **Excitement**: Personal interest level (orthogonal to soundness)
3. **Overall Recommendation**: Composite assessment for venue suitability

## What Constitutes a Strong Review

### Specificity Requirement (I1)
Reviews must be concrete. Instead of "paper lacks relevant references," specify: "paper misses references X, Y, Z."

### Professional Tone (I4)
Reviews should be "professional and neutral, if not kind." Sarcastic or dismissive language is discouraged, recognizing reviewers' power over authors' careers.

### Two-Pass Reading Strategy

**Skim-reading**: Assess research question, methodology scope, and claim appropriateness without examining results yet.

**In-depth reading**: Evaluate evidence, technical sou
…[truncated 2252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 13519
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-18T05:27:17.944508+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
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

_source line 907 · 2026-05-18T05:27:18.046032+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-18T05:29:40.701058+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿报告：方法严谨性 + 实验设计 + 统计论证\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 via ARR May 2026\n**审查侧重**: 统计方法论、实验设计、效应量与实际意义、跨模型验证、因果语言、SDGD 负面结果\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**一句话总结**: 一篇严谨的实证分析论文，实验设计精细、负面结果诚实，但核心贡献受限于效应量的实际意义偏弱，且 logit-scale 等价检验的不确定性削弱了\"bounded association\"这一关键 claim 的稳健性。\n\n---\n\n## 官方维度打分（来自 ARR Review Form, Feb 2025 onwards）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5 / 5 | 主要 claim 有充分支撑，但 logit-scale TOST 不确定性（p=0.209）与线性 scale 选择的 framing 偏差构成方法论弱点；部分核心数字（DocRED R²=0.53）CI 极宽 |\n| **Excitement** | 3 / 5 | 对 training-free IE 的 failure mode 提供了有价值的系统化理解，但 actionability 有限（2.2pp typical gap 难以驱动实际 schema 设计决策），负面 SDGD 结果有意义但缺乏替代方案 |\n| **Reproducibility** | 4 / 5 | 实验细节充分（decoding 参数、seed、batch 构造协议均有说明），prompt 模板完整给出，代码承诺 release；但 FewRel train+val 合并的具体 sampling 细节和 BCS batch 构造算法需要代码才能完全复现 |\n| **Confidence** | 4 / 5 | 统计方法论和实验设计是我的核心专长，我仔细检查了论文的所有统计 claim |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Logit-scale TOST 不确定性被低估，\"bounded association\" claim 需要重新表述\n\n- 具体位置：§5.4 Multi-Dimensional Degradation, Appendix §F (Factorial Analysis)\n- 问题：论文的核心 claim 之一是 count 和 confusability 在 RE 上具有\"bounded association\"（TOST p=0.003 at ±3pp）。然而 Appendix 明确报告 logit-scale interaction 为 0.111 logit units（p=0.047, marginally significant），logit-scale TOST inconclusive（p=0.209）。论文选择 linear scale 作为\"primary test\"并将 logit 分析降级为 sensitivity check，但这一选择本身就有利于作者的结论。在 accuracy 接近 50%（high-BCS batches 的 floor 就在 ~51%）时，linear scale 压缩 interaction effects 是已知的统计特性。论文虽然承认了这一点（\"accuracy near 50% compresses interaction effects on the linear scale\"），但随后仍以 linear-scale 结论为主导叙事。\n- 为什么影响接收：如果 logit scale 上 interaction 是 marginally significant，那么 Dimension 1 和 Dimension 2 的独立性在 RE 上就不是\"bounded\"而是\"inconclusive\"，这直接影响 §5.4 的\"two independent dimensions\"框架和 Discussion 中\"no confusability amplification at scale\"的实践建议。\n- 建议修改方向：（1）正文中（不仅是 Appendix）报告 logit-scale 结果，将 bounded association claim 降级为\"bounded under linear specification, inconclusive under logit\"；（2）承认 scale 选择是一个分析自由度；（3）或者增加样本量（n=69 对于 TOST 偏低）以提供更有力的检验。\n\n**N2** [critical] DocRED R²=0.53 的 claim 稳健性不足\n\n- 具体位置：§5.3 BCS-Controlled Experiments, Appendix §I (BCS-Controlled Detailed Results)\n- 问题：论文多处引用\"BCS explains 22-53% of cross-batch RE accuracy variance\"（Abstract, §1 Introduction contribution 2, §5.3, §7 Discussion），其中 53% 来自 DocRED count=16 的 n=35 batches OLS 回归。Appendix 报告 adjusted R²=0.511，Fisher z CI=[0.27, 0.73]。这个 CI 跨度 46 个百分点，意味着真实 R² 可能低至 27%（与 FewRel 的 22% 相近）或高至 73%。用 n=35 的 point estimate 0.53 作为范围上界（\"22-53%\"）在叙事中反复出现，给读者一种 BCS 解释力可达一半以上的印象，但实际不确定性极大。\n- 为什么影响接收：这是论文 contribution 2 的核心数字之一，如果审稿人注意到 CI 宽度，会质疑 claim 的 precision。\n- 建议修改方向：（1）正文中报告 CI（不只在 Appendix）；（2）将\"22-53%\"改为更保守的表述，如\"22% on FewRel (n=100), up to 53% on DocRED (n=35, CI [0.27, 0.73])\"，让读者自行判断；（3）或增加 DocRED 的 batch 数量以缩窄 CI。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] 缺乏 formal power analysis\n\n- 具体位置：§3.3 Experimental Design, Appendix §F (Factorial)\n- 问题：论文多处承认 power 不足（2×2 factorial p_TOST=0.56 \"due to limited power\"; 80-relation full condition n=25 \"underpowered\"；NER BCS batch-level r≈0 可能因 boundary errors 淹没信号也可能因 power 不足），但从未报告事前或事后 power analysis。TOST 检验的 power 直接取决于样本量和效应量；n=69 的 TOST 对 ±3pp margin 的 power 是多少？如果 power 不足 80%，则 equivalence conclusion 本身就不可靠。\n- 建议：报告 TOST 的 post-hoc power（或 sensitivity analysis 给出在当前 n 下可探测的最小等价 margin）；对 NER 的 null batch-level result，报告在当前 n=450 下可探测的最小 effect size。\n\n**W2** [major] Pairwise r²=1.3-1.7% 的实际意义论证薄弱\n\n- 具体位置：§5.2 Pairwise Confusability (Table 2), §6.2 Related Work (SCS novelty paragraph)\n- 问题：论文将 r²=1.3-1.7% 援引 Cohen (1988) 称为\"small but real\"，并论证其在 batch-level 聚合后放大到 R²=22%。Cohen 的分类本身在心理学界已有争议（Funder & Ozer, 2019），且 Cohen 本人警告不应机械套用。更关键的是：论文从 unconditional r²=1.3% 到 conditional r²=7%（只看非零混淆对）再到 batch R²=22% 的链条，虽然 Monte Carlo 模拟验证了数学一致性，但这依赖于 inter-pair SCS correlation ρ=0.35 的估计，该估计的 uncertainty 未被讨论。如果 ρ 偏低（如 0.20），simulated batch R² 会显著低于 22%。\n- 建议：（1）报告 ρ=0.35 的 CI；（2）在 simulation 中做 ρ 的 sensitivity analysis；（3）弱化\"小效应聚合为大效应\"的叙事语气，让数据更中立地说话。\n\n**W3** [major] 单 seed 实验设计对绝对值 claim 的限制\n\n- 具体位置：§3.5 Model and Inference\n- 问题：主实验使用 greedy decoding (temperature=0, seed=42)，论文论证 inter-seed variance 小（SD=0.88pp at count 80, Appendix §K）。但 cross-seed analysis 仅在 FewRel count curves 上做了 3 seeds（§5.1），BCS-controlled experiments、DocRED、MAVEN、cross-model validation 均为单 seed。论文报告的绝对数字（如 extreme-batch gap 31.2pp, BCS slope -0.509）的 uncertainty 因此被低估——bootstrap CI 只捕获了 batch composition variance，没有捕获 seed variance。\n- 建议：至少对核心 BCS-controlled RE 实验跑 3 seeds 并报告 seed-level variance，或在 Limitations 中明确说明单 seed 设计对绝对值估计的影响。\n\n**W4** [major] Dimension 2 跨模型验证不充分\n\n- 具体位置：Appendix §L (Cross-Model 70B), §M (Cross-Model Gemini), Limitations item 1\n- 问题：Dimension 1（count decline）在 4 个模型上验证（Qwen3-32B, Llama-8B, Llama-70B, Gemini Flash），但 Dimension 2（BCS-controlled confusability）仅在 Qwen3-32B（主模型）和 Llama-8B（Table A2 的 cross-model BCS）上有完整验证，Llama-70B 只有 count=16 的一个 BCS gap 数据点（§L），Gemini 没有 Dimension 2 数据。论文 Abstract 和 Conclusion 的措辞\"patterns replicate across model scales (8B to 70B) and architecture families (Qwen, LLaMA, Gemini)\"暗示两个 dimension 均已验证，但实际上 Dimension 2 的跨架构证据仅限于两个 open-weight 模型。\n- 建议：Abstract/Conclusion 中区分两个 dimension 的验证范围；或补充 Llama-70B 和 Gemini 的 BCS-controlled 实验。\n\n**W5** [moderate] TOST ±3pp margin 的 justification 存在循环论证风险\n\n- 具体位置：Appendix §F \"Equivalence margin justification\"\n- 问题：三个 anchor 中，\"Empirical\" anchor 基于\"typical random-batch confusability variation produces 2-5pp accuracy differences (batch SD ≈ 4.6pp at count 32)\"，即用数据本身的变异性来定义等价 margin。\"Statistical\" anchor 将 3pp 等价于 0.5×batch SD ≈ Cohen's d=0.5，但 Cohen's d=0.5 是 \"medium effect\" 的门槛，用它来定义\"negligible interaction\"逻辑上说不通（medium effect 怎么能算 negligible？）。论文随后补充\"A 3pp interaction atop the 2.2pp confusability main effect would represent >130% amplification\"，这个论证更有说服力，应该作为主要 justification。\n- 建议：重组 margin justification，以 130% amplification 论证为主线，弱化 Cohen's d=0.5 的类比（或正确引用 d=0.5 意味着 medium 而非 small effect）。\n\n**W6** [moderate] NER 评估指标的局限性影响 Dimension 2 的 NER null result 解读\n\n- 具体位置：Limitations item 5, §5.4\n- 问题：论文使用 exact-match NER 评估，但 Limitations item 5 承认这\"conflates boundary errors with type errors\"。如果 NER 的 batch-level BCS null result（r≈0）部分因为 exact-match 将 type confusion 和 boundary errors 混在一起，那么更宽松的匹配标准可能会揭示 NER 也存在 batch-level confusability signal。这使得\"BCS explains RE but not NER\"这一 task asymmetry claim 的确定性降低。\n- 建议：补充 relaxed-match（如 type-only 或 partial-span）NER 评估下的 BCS--F1 相关性，或将 task asymmetry claim 表述为\"under exact-match evaluation\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 2 只报告了 Few-NERD 和 MAVEN 的 pairwise correlation，FewRel 的 r=0.187 在 §3.4 提及但未入表（caption 解释了原因），建议统一呈现或在 table caption 中加入 FewRel 数字。\n- **M2**: Appendix §F 中\"Logit-scale sensitivity\"段落用\"logit-transformed accuracy\"但未给出 logit 变换的具体公式（log(p/(1-p))），对非统计背景读者不友好。\n- **M3**: §5.1 中\"plateauing across counts 22-44 before partial recovery at full-schema (0.41)\"——这个 U-shaped NER 曲线的解释（\"elimination of type-filtering overhead\"）缺乏实验证据支持，更像是猜测。\n- **M4**: Gemini count 64 基于 13/25 batches（Table A8），partial data 的 Spearman ρ 可信度打折扣，建议删除或标注更显著。\n- **M5**: Appendix §J 的 aggregation simulation 声称\"not the evidence base for our claims\"，但正文 §5.3 和 §7 均引用了 \"~3× pair-to-batch amplification\" 这一 simulation 结果来解释 R² 的 scaling——如果 simulation 不是证据，就不应在论证链中使用。\n- **M6**: Few-NERD 使用 Qwen3 自身的 embedding 计算 SCS（§3.3），存在 shared-representation dependency。虽然 MiniLM cross-check 结果一致（r=0.172 vs 0.138），但 Qwen3 embedding 产生更低的 r 反而削弱了 SCS 的解释力，这一 counterintuitive 结果值得讨论。\n- **M7**: References 中 Gemini 2025 的 arXiv ID 是 2507.06261——这个 ID 对应 2025 年 7 月的论文，但论文投稿日期是 2026 年 5 月 ARR cycle，时间线上没问题，但请确认引用的正确性（arXiv 2507 = 2025 July）。\n\n---\n\n## 主要优势\n\n1. **实验设计精细且系统化**：Count curves + BCS-controlled 的双范式设计有效隔离了 count 和 confusability 两个因素（§3.3）。Within-pool analysis（从 80-relation pool 抽取 16-relation subsets）控制了 pool composition confound（Table 5），permutation test p=0.60 有说服力。\n\n2. **统计严谨性高于同类工作**：使用 TOST 等价检验（而非仅靠 NHST 的 non-significance）、bootstrap CI、cluster bootstrap、permutation tests、variance decomposition。Rothman (1990) 关于多重比较的引用虽有争议但有理论依据。TOST sensitivity analysis across margins（Table A4）和 logit-scale sensitivity check 均体现了审慎态度。\n\n3. **负面结果的诊断深度出色**：SDGD failure 不仅报告了\"不 work\"，还诊断了 merge amplification（precision collapse 0.563→0.210）和 routing failure（constrained decoding 导致 73.4% instances 在 3-5 个 sub-schemas 同时获得 positive predictions），并区分了 NER（merge 问题）和 RE（routing 问题）的不同 failure mode（§6, Appendix §E）。\n\n4. **Centrality confound 的发现和处理（§5.5）**：MAVEN 上 BCS-F1 正相关的发现、centrality confound 的诊断、partial correlation 控制后效应消失（p>0.2），以及\"mean BCS 只适用于 cross-domain schemas\"的结论，是一个有价值的方法论贡献。\n\n5. **Limitations 极为坦诚**：8 条 Limitations + Multiple comparisons 讨论，涵盖了几乎所有我能想到的弱点（包括 causal mechanism、data contamination、NER metric、RE format specificity）。这在 NLP 论文中不常见。\n\n6. **多层 robustness check**：Cross-model (4 models)、cross-prompt (4 variants, Table A6)、cross-embedding (MiniLM vs Qwen3, Appendix §H)、cross-seed (3 seeds, Appendix §K)、cross-dataset (FewRel→DocRED replication)。\n\n---\n\n## Questions for Authors\n\nQ1: TOST 在 n=69 下对 ±3pp margin 的 statistical power 是多少？如果 power < 0.8，equivalence conclusion 的可信度如何？\n\nQ2: Aggregation simulation（Appendix §J）中 inter-pair SCS correlation ρ=0.35 的估计方法是什么？其 CI 是多少？如果 ρ=0.20，simulated batch R² 大约是多少？\n\nQ3: 论文是否尝试过在 NER 上使用 type-only matching（忽略 boundary）来检测 batch-level confusability signal？如果没有，这是否是一个值得做的实验？\n\nQ4: Few-NERD U-shaped count curve 的 partial recovery（count 66, recall=0.41 vs count 22-44 plateau ~0.27）有没有更具体的解释？\"elimination of type-filtering overhead\"是什么机制？\n\nQ5: Oracle routing 在 RE 上恢复了 +29.8pp（Table 6），但所有 practical routing strategies 都 fail。作者是否尝试过 embedding-based routing（用 SCS 将 test instance 路由到最相关的 sub-schema）而非 confidence-based routing？\n\n---\n\n## Missing References\n\n- Funder & Ozer (2019), \"Evaluating Effect Size in Psychological Research: Sense and Nonsense\"——关于 Cohen's effect size 分类的批判性讨论，与 §6.2 的 \"small but real\" claim 相关。\n- Wellek (2010), \"Testing Statistical Hypotheses of Equivalence and Noninferiority\"——TOST 方法论的权威教材，比 Lakens (2017) 更 comprehensive。\n- Schuirmann (1987), \"A comparison of the Two One-Sided Tests Procedure...\"——TOST 的原始论文，论文只引用了 Lakens (2017) 的 primer。\n- 关于 constrained decoding 对 calibration 影响的文献（论文 §6 中 routing failure 归因于 constrained decoding 消除了 confidence signal，但缺乏这方面的 citation）。\n\n---\n\n## 格式合规检查\n\n- ✅ ACL 模板 `\\usepackage[review]{acl}`\n- ✅ `\\author{Anonymous}`（double-blind）\n- ✅ Limitations section 在正文末尾（References 之前）\n- ✅ Responsible NLP Research Checklist 完整\n- ⚠️ 页数限制需编译确认（正文内容较多，§1-§7 + Limitations + Checklist，可能接近或超过 8 页）\n- ✅ 行号已启用（review option）\n\n---\n\n## 总结\n\n这是一篇高于平均水平的实证分析论文。实验设计的 sophistication（BCS-controlled, within-pool, TOST, variance decomposition）和负面结果的诊断深度值得肯定。主要 concern 是：（1）logit-scale TOST inconclusive 结果削弱了 core claim 的稳健性但论文 framing 偏向有利结论；（2）R²=22-53% 的上界 CI 极宽；（3）typical effect size（2.2pp）的 practical actionability 有限。如果作者能在 rebuttal 中（a）报告 TOST power analysis，（b）正文中报告 DocRED R² 的 CI，（c）明确区分 Dimension 2 的跨模型验证范围，我会考虑上调至 4。\n",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿报告：方法严谨性 + 实验设计 + 统计论证\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 via ARR May 2026\n**审查侧重**: 统计方法论、实验设计、效应量与实际意义、跨模型验证、因果语言、SDGD 负面结果\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**一句话总结**: 一篇严谨的实证分析论文，实验设计精细、负面结果诚实，但核心贡献受限于效应量的实际意义偏弱，且 logit-scale 等价检验的不确定性削弱了\"bounded association\"这一关键 claim 的稳健性。\n\n---\n\n## 官方维度打分（来自 ARR Review Form, Feb 2025 onwards）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5 / 5 | 主要 claim 有充分支撑，但 logit-scale TOST 不确定性（p=0.209）与线性 scale 选择的 framing 偏差构成方法论弱点；部分核心数字（DocRED R²=0.53）CI 极宽 |\n| **Excitement** | 3 / 5 | 对 training-free IE 的 failure mode 提供了有价值的系统化理解，但 actionability 有限（2.2pp typical gap 难以驱动实际 schema 设计决策），负面 SDGD 结果有意义但缺乏替代方案 |\n| **Reproducibility** | 4 / 5 | 实验细节充分（decoding 参数、seed、batch 构造协议均有说明），prompt 模板完整给出，代码承诺 release；但 FewRel train+val 合并的具体 sampling 细节和 BCS batch 构造算法需要代码才能完全复现 |\n| **Confidence** | 4 / 5 | 统计方法论和实验设计是我的核心专长，我仔细检查了论文的所有统计 claim |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Logit-scale TOST 不确定性被低估，\"bounded association\" claim 需要重新表述\n\n- 具体位置：§5.4 Multi-Dimensional Degradation, Appendix §F (Factorial Analysis)\n- 问题：论文的核心 claim 之一是 count 和 confusability 在 RE 上具有\"bounded association\"（TOST p=0.003 at ±3pp）。然而 Appendix 明确报告 logit-scale interaction 为 0.111 logit units（p=0.047, marginally significant），logit-scale TOST inconclusive（p=0.209）。论文选择 linear scale 作为\"primary test\"并将 logit 分析降级为 sensitivity check，但这一选择本身就有利于作者的结论。在 accuracy 接近 50%（high-BCS batches 的 floor 就在 ~51%）时，linear scale 压缩 interaction effects 是已知的统计特性。论文虽然承认了这一点（\"accuracy near 50% compresses interaction effects on the linear scale\"），但随后仍以 linear-scale 结论为主导叙事。\n- 为什么影响接收：如果 logit scale 上 interaction 是 marginally significant，那么 Dimension 1 和 Dimension 2 的独立性在 RE 上就不是\"bounded\"而是\"inconclusive\"，这直接影响 §5.4 的\"two independent dimensions\"框架和 Discussion 中\"no confusability amplification at scale\"的实践建议。\n- 建议修改方向：（1）正文中（不仅是 Appendix）报告 logit-scale 结果，将 bounded association claim 降级为\"bounded under linear specification, inconclusive under logit\"；（2）承认 scale 选择是一个分析自由度；（3）或者增加样本量（n=69 对于 TOST 偏低）以提供更有力的检验。\n\n**N2** [critical] DocRED R²=0.53 的 claim 稳健性不足\n\n- 具体位置：§5.3 BCS-Controlled Experiments, Appendix §I (BCS-Controlled Detailed Results)\n- 问题：论文多处引用\"BCS explains 22-53% of cross-batch RE accuracy variance\"（Abstract, §1 Introduction contribution 2, §5.3, §7 Discussion），其中 53% 来自 DocRED count=16 的 n=35 batches OLS 回归。Appendix 报告 adjusted R²=0.511，Fisher z CI=[0.27, 0.73]。这个 CI 跨度 46 个百分点，意味着真实 R² 可能低至 27%（与 FewRel 的 22% 相近）或高至 73%。用 n=35 的 point estimate 0.53 作为范围上界（\"22-53%\"）在叙事中反复出现，给读者一种 BCS 解释力可达一半以上的印象，但实际不确定性极大。\n- 为什么影响接收：这是论文 contribution 2 的核心数字之一，如果审稿人注意到 CI 宽度，会质疑 claim 的 precision。\n- 建议修改方向：（1）正文中报告 CI（不只在 Appendix）；（2）将\"22-53%\"改为更保守的表述，如\"22% on FewRel (n=100), up to 53% on DocRED (n=35, CI [0.27, 0.73])\"，让读者自行判断；（3）或增加 DocRED 的 batch 数量以缩窄 CI。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] 缺乏 formal power analysis\n\n- 具体位置：§3.3 Experimental Design, Appendix §F (Factorial)\n- 问题：论文多处承认 power 不足（2×2 factorial p_TOST=0.56 \"due to limited power\"; 80-relation full condition n=25 \"underpowered\"；NER BCS batch-level r≈0 可能因 boundary errors 淹没信号也可能因 power 不足），但从未报告事前或事后 power analysis。TOST 检验的 power 直接取决于样本量和效应量；n=69 的 TOST 对 ±3pp margin 的 power 是多少？如果 power 不足 80%，则 equivalence conclusion 本身就不可靠。\n- 建议：报告 TOST 的 post-hoc power（或 sensitivity analysis 给出在当前 n 下可探测的最小等价 margin）；对 NER 的 null batch-level result，报告在当前 n=450 下可探测的最小 effect size。\n\n**W2** [major] Pairwise r²=1.3-1.7% 的实际意义论证薄弱\n\n- 具体位置：§5.2 Pairwise Confusability (Table 2), §6.2 Related Work (SCS novelty paragraph)\n- 问题：论文将 r²=1.3-1.7% 援引 Cohen (1988) 称为\"small but real\"，并论证其在 batch-level 聚合后放大到 R²=22%。Cohen 的分类本身在心理学界已有争议（Funder & Ozer, 2019），且 Cohen 本人警告不应机械套用。更关键的是：论文从 unconditional r²=1.3% 到 conditional r²=7%（只看非零混淆对）再到 batch R²=22% 的链条，虽然 Monte Carlo 模拟验证了数学一致性，但这依赖于 inter-pair SCS correlation ρ=0.35 的估计，该估计的 uncertainty 未被讨论。如果 ρ 偏低（如 0.20），simulated batch R² 会显著低于 22%。\n- 建议：（1）报告 ρ=0.35 的 CI；（2）在 simulation 中做 ρ 的 sensitivity analysis；（3）弱化\"小效应聚合为大效应\"的叙事语气，让数据更中立地说话。\n\n**W3** [major] 单 seed 实验设计对绝对值 claim 的限制\n\n- 具体位置：§3.5 Model and Inference\n- 问题：主实验使用 greedy decoding (temperature=0, seed=42)，论文论证 inter-seed variance 小（SD=0.88pp at count 80, Appendix §K）。但 cross-seed analysis 仅在 FewRel count curves 上做了 3 seeds（§5.1），BCS-controlled experiments、DocRED、MAVEN、cross-model validation 均为单 seed。论文报告的绝对数字（如 extreme-batch gap 31.2pp, BCS slope -0.509）的 uncertainty 因此被低估——bootstrap CI 只捕获了 batch composition variance，没有捕获 seed variance。\n- 建议：至少对核心 BCS-controlled RE 实验跑 3 seeds 并报告 seed-level variance，或在 Limitations 中明确说明单 seed 设计对绝对值估计的影响。\n\n**W4** [major] Dimension 2 跨模型验证不充分\n\n- 具体位置：Appendix §L (Cross-Model 70B), §M (Cross-Model Gemini), Limitations item 1\n- 问题：Dimension 1（count decline）在 4 个模型上验证（Qwen3-32B, Llama-8B, Llama-70B, Gemini Flash），但 Dimension 2（BCS-controlled confusability）仅在 Qwen3-32B（主模型）和 Llama-8B（Table A2 的 cross-model BCS）上有完整验证，Llama-70B 只有 count=16 的一个 BCS gap 数据点（§L），Gemini 没有 Dimension 2 数据。论文 Abstract 和 Conclusion 的措辞\"patterns replicate across model scales (8B to 70B) and architecture families (Qwen, LLaMA, Gemini)\"暗示两个 dimension 均已验证，但实际上 Dimension 2 的跨架构证据仅限于两个 open-weight 模型。\n- 建议：Abstract/Conclusion 中区分两个 dimension 的验证范围；或补充 Llama-70B 和 Gemini 的 BCS-controlled 实验。\n\n**W5** [moderate] TOST ±3pp margin 的 justification 存在循环论证风险\n\n- 具体位置：Appendix §F \"Equivalence margin justification\"\n- 问题：三个 anchor 中，\"Empirical\" anchor 基于\"typical random-batch confusability variation produces 2-5pp accuracy differences (batch SD ≈ 4.6pp at count 32)\"，即用数据本身的变异性来定义等价 margin。\"Statistical\" anchor 将 3pp 等价于 0.5×batch SD ≈ Cohen's d=0.5，但 Cohen's d=0.5 是 \"medium effect\" 的门槛，用它来定义\"negligible interaction\"逻辑上说不通（medium effect 怎么能算 negligible？）。论文随后补充\"A 3pp interaction atop the 2.2pp confusability main effect would represent >130% amplification\"，这个论证更有说服力，应该作为主要 justification。\n- 建议：重组 margin justification，以 130% amplification 论证为主线，弱化 Cohen's d=0.5 的类比（或正确引用 d=0.5 意味着 medium 而非 small effect）。\n\n**W6** [moderate] NER 评估指标的局限性影响 Dimension 2 的 NER null result 解读\n\n- 具体位置：Limitations item 5, §5.4\n- 问题：论文使用 exact-match NER 评估，但 Limitations item 5 承认这\"conflates boundary errors with type errors\"。如果 NER 的 batch-level BCS null result（r≈0）部分因为 exact-match 将 type confusion 和 boundary errors 混在一起，那么更宽松的匹配标准可能会揭示 NER 也存在 batch-level confusability signal。这使得\"BCS explains RE but not NER\"这一 task asymmetry claim 的确定性降低。\n- 建议：补充 relaxed-match（如 type-only 或 partial-span）NER 评估下的 BCS--F1 相关性，或将 task asymmetry claim 表述为\"under exact-match evaluation\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 2 只报告了 Few-NERD 和 MAVEN 的 pairwise correlation，FewRel 的 r=0.187 在 §3.4 提及但未入表（caption 解释了原因），建议统一呈现或在 table caption 中加入 FewRel 数字。\n- **M2**: Appendix §F 中\"Logit-scale sensitivity\"段落用\"logit-transformed accuracy\"但未给出 logit 变换的具体公式（log(p/(1-p))），对非统计背景读者不友好。\n- **M3**: §5.1 中\"plateauing across counts 22-44 before partial recovery at full-schema (0.41)\"——这个 U-shaped NER 曲线的解释（\"elimination of type-filtering overhead\"）缺乏实验证据支持，更像是猜测。\n- **M4**: Gemini count 64 基于 13/25 batches（Table A8），partial data 的 Spearman ρ 可信度打折扣，建议删除或标注更显著。\n- **M5**: Appendix §J 的 aggregation simulation 声称\"not the evidence base for our claims\"，但正文 §5.3 和 §7 均引用了 \"~3× pair-to-batch amplification\" 这一 simulation 结果来解释 R² 的 scaling——如果 simulation 不是证据，就不应在论证链中使用。\n- **M6**: Few-NERD 使用 Qwen3 自身的 embedding 计算 SCS（§3.3），存在 shared-representation dependency。虽然 MiniLM cross-check 结果一致（r=0.172 vs 0.138），但 Qwen3 embedding 产生更低的 r 反而削弱了 SCS 的解释力，这一 counterintuitive 结果值得讨论。\n- **M7**: References 中 Gemini 2025 的 arXiv ID 是 2507.06261——这个 ID 对应 2025 年 7 月的论文，但论文投稿日期是 2026 年 5 月 ARR cycle，时间线上没问题，但请确认引用的正确性（arXiv 2507 = 2025 July）。\n\n---\n\n## 主要优势\n\n1. **实验设计精细且系统化**：Count curves + BCS-controlled 的双范式设计有效隔离了 count 和 confusability 两个因素（§3.3）。Within-pool analysis（从 80-relation pool 抽取 16-relation subsets）控制了 pool composition confound（Table 5），permutation test p=0.60 有说服力。\n\n2. **统计严谨性高于同类工作**：使用 TOST 等价检验（而非仅靠 NHST 的 non-significance）、bootstrap CI、cluster bootstrap、permutation tests、variance decomposition。Rothman (1990) 关于多重比较的引用虽有争议但有理论依据。TOST sensitivity analysis across margins（Table A4）和 logit-scale sensitivity check 均体现了审慎态度。\n\n3. **负面结果的诊断深度出色**：SDGD failure 不仅报告了\"不 work\"，还诊断了 merge amplification（precision collapse 0.563→0.210）和 routing failure（constrained decoding 导致 73.4% instances 在 3-5 个 sub-schemas 同时获得 positive predictions），并区分了 NER（merge 问题）和 RE（routing 问题）的不同 failure mode（§6, Appendix §E）。\n\n4. **Centrality confound 的发现和处理（§5.5）**：MAVEN 上 BCS-F1 正相关的发现、centrality confound 的诊断、partial correlation 控制后效应消失（p>0.2），以及\"mean BCS 只适用于 cross-domain schemas\"的结论，是一个有价值的方法论贡献。\n\n5. **Limitations 极为坦诚**：8 条 Limitations + Multiple comparisons 讨论，涵盖了几乎所有我能想到的弱点（包括 causal mechanism、data contamination、NER metric、RE format specificity）。这在 NLP 论文中不常见。\n\n6. **多层 robustness check**：Cross-model (4 models)、cross-prompt (4 variants, Table A6)、cross-embedding (MiniLM vs Qwen3, Appendix §H)、cross-seed (3 seeds, Appendix §K)、cross-dataset (FewRel→DocRED replication)。\n\n---\n\n## Questions for Authors\n\nQ1: TOST 在 n=69 下对 ±3pp margin 的 statistical power 是多少？如果 power < 0.8，equivalence conclusion 的可信度如何？\n\nQ2: Aggregation simulation（Appendix §J）中 inter-pair SCS correlation ρ=0.35 的估计方法是什么？其 CI 是多少？如果 ρ=0.20，simulated batch R² 大约是多少？\n\nQ3: 论文是否尝试过在 NER 上使用 type-only matching（忽略 boundary）来检测 batch-level confusability signal？如果没有，这是否是一个值得做的实验？\n\nQ4: Few-NERD U-shaped count curve 的 partial recovery（count 66, recall=0.41 vs count 22-44 plateau ~0.27）有没有更具体的解释？\"elimination of type-filtering overhead\"是什么机制？\n\nQ5: Oracle routing 在 RE 上恢复了 +29.8pp（Table 6），但所有 practical routing strategies 都 fail。作者是否尝试过 embedding-based routing（用 SCS 将 test instance 路由到最相关的 sub-schema）而非 confidence-based routing？\n\n---\n\n## Missing References\n\n- Funder & Ozer (2019), \"Evaluating Effect Size in Psychological Research: Sense and Nonsense\"——关于 Cohen's effect size 分类的批判性讨论，与 §6.2 的 \"small but real\" claim 相关。\n- Wellek (2010), \"Testing Statistical Hypotheses of Equivalence and Noninferiority\"——TOST 方法论的权威教材，比 Lakens (2017) 更 comprehensive。\n- Schuirmann (1987), \"A comparison of the Two One-Sided Tests Procedure...\"——TOST 的原始论文，论文只引用了 Lakens (2017) 的 primer。\n- 关于 constrained decoding 对 calibration 影响的文献（论文 §6 中 routing failure 归因于 constrained decoding 消除了 confidence signal，但缺乏这方面的 citation）。\n\n---\n\n## 格式合规检查\n\n- ✅ ACL 模板 `\\usepackage[review]{acl}`\n- ✅ `\\author{Anonymous}`（double-blind）\n- ✅ Limitations section 在正文末尾（References 之前）\n- ✅ Responsible NLP Research Checklist 完整\n- ⚠️ 页数限制需编译确认（正文内容较多，§1-§7 + Limitations + Checklist，可能接近或超过 8 页）\n- ✅ 行号已启用（review option）\n\n---\n\n## 总结\n\n这是一篇高于平均水平的实证分析论文。实验设计的 sophistication（BCS-controlled, within-pool, TOST, variance decomposition）和负面结果的诊断深度值得肯定。主要 concern 是：（1）logit-scale TOST inconclusive 结果削弱了 core claim 的稳健性但论文 framing 偏向有利结论；（2）R²=22-53% 的上界 CI 极宽；（3）typical effect size（2.2pp）的 practical actionability 有限。如果作者能在 rebuttal 中（a）报告 TOST power analysis，（b）正文中报告 DocRED R² 的 CI，（c）明确区分 Dimension 2 的跨模型验证范围，我会考虑上调至 4。\n",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-18T05:29:44.880107+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4179
}
```

</details>

---


### Assistant

_source line 910 · 2026-05-18T05:29:55.961476+00:00_

审稿报告已提交给 Review Director。

核心评判：**Overall 3.5（Borderline Conference）**。

主要发现：

**2 个 Must-Fix 问题**：
1. Logit-scale TOST inconclusive (p=0.209) 与论文主导叙事的 linear-scale "bounded association" 存在矛盾，scale 选择构成分析自由度，需在正文中透明报告
2. DocRED R²=0.53 的 CI 极宽 [0.27, 0.73]，"22-53%" 这一反复使用的 claim 上界不够稳健

**6 个 Should-Fix 问题**涉及：缺乏 formal power analysis、pairwise r²=1.3% 实际意义的论证链薄弱（ρ=0.35 估计未报 CI）、单 seed 设计对绝对值 claim 的限制、Dimension 2 跨模型验证不充分（Abstract/Conclusion 措辞暗示全面验证但实际仅 2 个 open-weight 模型）、TOST margin justification 中 Cohen's d=0.5 类比有误（medium≠negligible）、NER exact-match 指标可能掩盖 batch-level confusability signal。

**主要优势**：实验设计精细（BCS-controlled + within-pool 控制 confound）、统计严谨性高于同类工作、SDGD 负面结果诊断深度出色、centrality confound 处理有方法论价值、Limitations 极其坦诚。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 31

## Round 31

12 recorded events


### User

_source line 911 · 2026-05-18T05:33:01.320426+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6) 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿报告

**Overall Assessment**: 3.0 / 5 (Findings)

### Must-Fix 问题

**N1** [critical] SCS/BCS 无独立新颖性，"first controlled study" claim 需要更严格 qualify
- SCS 就是 pairwise cosine similarity of type name embeddings，论文自己承认与 LLM-PEE 形式相同 (§2)。BCS 是其 mean aggregation。metric 无增量，新颖性完全在 experimental framework 和 findings。但 Abstract/Contribution 措辞 ("operationalize confusability via SCS") 暗示 SCS 本身是贡献。

**N2** [critical] Confusability effect size 在典型条件下非常小（2.2pp），Abstract framing 有 cherry-picking 嫌疑
- Abstract 领衔数字 "−49pp" 来自 DocRED 全 schema 极端条件（Dimension 1），typical-batch BCS gap 仅 2.2pp。极端 batch 的 25–31pp gap 来自刻意构造的 extreme-BCS batches。Abstract 不体现 practical magnitude。

**N3** [critical] NER 和 ED 结果本质上是 null result，削弱 "three tasks, four datasets" 的 generality claim
- BCS 对 NER F1 batch-level r≈0 (n=450)。MAVEN per-type BCS 被 centrality confound 完全解释。Pairwise SCS 在 NER 上 r=0.112 (r²=1.3%)。标题无限定词暗示跨任务通用性，但 confusability strong story 仅在 RE 成立。

### Should-Fix 问题

**W1** [major] MAVEN 参与度极低，不支撑 "event detection" 和 "four datasets" claim
**W2** [major] Logit-scale TOST inconclusive 削弱 bounded-association 核心 claim
**W3** [major] Single-seed (seed=42) 实验，effect size 与 seed variance 可比 (seed SD=2.7pp at count 16 vs typical gap 2.2pp)
**W4** [minor-major] Abstract "up to −49pp" 混淆了 Dimension 1 和 Dimension 2
**W5** [minor] 缺失相关工作：DLiSC 和 SPT
**W6** [minor] 5 个 orphan bib entries

### 主要优势
实验设计严谨、统计方法高于平均、cross-model validation 充分、负面结果诚实、Limitations 模范级别、写作质量高（无 AI 痕迹）

### 总结判断
推荐 Findings (3.0)。Soundness 3.5 但 Excitement 2.5。强结果集中在 RE，NER/ED 基本 null results，SCS/BCS metric 无新颖性，typical effect size 2.2pp practical significance 有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-18T05:33:50.520372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-18T05:33:50.621319+00:00_

1	\begin{abstract}
2	As large language models are increasingly deployed for information extraction without task-specific training, understanding how schema design affects extraction quality becomes critical for reliable deployment. Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors across NER, RE, and event detection on four datasets and operationalize confusability via the Schema Confusability Score (SCS) and its batch-level aggregation (BCS). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp, document-level RE at full schema) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); BCS explains 22--53\% of cross-batch RE accuracy variance but not NER, where boundary detection failures overwhelm the signal. Few-shot demonstrations do not reduce the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). These patterns replicate across model scales (8B to 70B) and architecture families (Qwen, LLaMA, Gemini), which suggests schema-associated degradation is consistent across tested model families rather than a model-specific artifact.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 914 · 2026-05-18T05:33:53.883712+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "offset": "13",
  "limit": "14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "offset": "13",
    "limit": "14"
  }
}
```

</details>

---


### Tool result

_source line 915 · 2026-05-18T05:33:54.336082+00:00_

13	
14	Our experiments yield four findings:
15	(1)~Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) and confusability-related type substitution (typical-batch gap ${\approx}\,2.2$\,pp), with count as the dominant factor (\S\ref{sec:count_curves}, \S\ref{sec:multi_channel}). The two dimensions exhibit bounded association in RE (Two One-Sided Tests [TOST] equivalence, $p = 0.003$ at $\pm 3$\,pp) but are coupled in NER.
16	(2)~Pairwise SCS predicts type confusion across NER, RE, and ED ($r = 0.112$--$0.129$; \S\ref{sec:pairwise}); at batch level, BCS predicts accuracy in RE ($R^2 = 0.22$--$0.53$; \S\ref{sec:bcs_controlled}) but not in NER (batch-level $r \approx 0$, n.s.); per-type aggregation is confounded by centrality on homogeneous schemas (\S\ref{sec:centrality_confound}).
17	(3)~Effects are consistent across schema sizes (BCS slopes: $p = 0.60$; DocRED: $R^2 = 0.53$), prompt designs, and model families (\S\ref{sec:bcs_controlled}).
18	(4)~Schema decomposition fails due to merge amplification in NER; RE confusability-aware grouping yields no significant improvement over random (+1.4\,pp, $p \approx 0.19$, n.s.) despite oracle routing that recovers +29.8\,pp (\S\ref{sec:sdgd}).
19	
20	Our contributions are:
21	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
22	    \item We conduct the first controlled study that isolates count and confusability effects on training-free LLM IE performance across four datasets and three tasks (\S\ref{sec:count_curves}, \S\ref{sec:bcs_controlled}).
23	    \item We validate that pairwise embedding similarity predicts type confusion and show that weak pair-level signals ($r = 0.11$--$0.19$) amplify to batch-level predictive power ($R^2 = 0.22$--$0.53$) through correlated aggregation (\S\ref{sec:pairwise}, \S\ref{sec:bcs_controlled}).
24	    \item We discover a task asymmetry: BCS explains 22--53\% of RE accuracy variance through type substitution, yet shows no batch-l
…[truncated 351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-18T05:33:54.436963+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "56",
  "limit": "18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "56",
    "limit": "18"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-18T05:33:54.437377+00:00_

56	In BCS-controlled FewRel subsets, the high-BCS quartile shows $\Delta=-5.3$\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\,=\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\,pp at count 8, $-$31.8\,pp at count 16) and confirms monotonic decline.
57	
58	\paragraph{Document-level RE (DocRED).}
59	The effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\,pp at count 16 (slope $= -0.713$, $\rho = -0.661$, $p < 0.001$) and $-$17.6\,pp at count 32 (slope $= -0.690$, $\rho = -0.509$, $p = 0.002$). BCS explains 44--53\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.
60	
61	\paragraph{Within-pool controlled comparison.}
62	\label{sec:within_pool}
63	Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
64	
65	\paragraph{Practical magnitude.}
66	\label{sec:practical_magnitude}
67	Direct regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$), scaling to 53\% at DocRED 96-rel. The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0]), roughly 7\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% 
…[truncated 2032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-18T05:33:58.906015+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "bogdanov2024nuner|xie2024selfimproving|zhang2023llmaaa|cheng2023batch|levy-2024-same-task",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "bogdanov2024nuner|xie2024selfimproving|zhang2023llmaaa|cheng2023batch|levy-2024-same-task",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 919 · 2026-05-18T05:33:58.956578+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-18T05:35:20.158114+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 交叉回应 Reviewer 2 审稿意见\n\n---\n\n## Must-Fix 问题\n\n**[AGREE with qualification] R2-N1: SCS/BCS 无独立新颖性**\n\n同意 SCS 在形式上就是 pairwise cosine similarity，论文 §2 \"SCS novelty\" 段落自己承认了这一点（\"SCS shares its formal definition ... with the partitioning criterion used in LLM-PEE\"）。Contribution list item 2 的措辞 \"We validate that pairwise embedding similarity predicts type confusion\" 实际上比 Abstract 的 \"operationalize confusability via SCS\" 更准确。\n\n但我要补充一个 nuance：§2 末尾的论述 \"Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation\" 是一个合理的 positioning。给已有 metric 命名（SCS/BCS）以便论文内部一致引用是写作上的实用选择，不算 overclaim。问题在于 Abstract 的 \"operationalize\" 一词暗示了 SCS 是本文引入的操作化方式，建议改为 \"quantify confusability using pairwise embedding similarity (SCS)\" 或类似措辞以降低新颖性暗示。\n\n**[REBUT partially] R2-N2: Abstract framing 有 cherry-picking 嫌疑**\n\nR2 称 Abstract 领衔 -49pp 造成误导。我认为这一批评部分成立但整体过重。\n\n证据：Abstract 原文为 \"Degradation operates along two dimensions: count-related recall decline (up to −49pp, document-level RE at full schema) dominates confusability-related type substitution (≈2.2pp in typical batches)\"。这一句明确做了三件事：（1）将 -49pp 归于 Dimension 1（count），不是 confusability；（2）用 \"dominates\" 正确传达了两个 dimension 的相对重要性；（3）紧随其后报告了 typical-batch 2.2pp。Abstract 还补充了 \"BCS explains 22-53% of cross-batch RE accuracy variance but not NER\"，明确说了 NER null。\n\nR2 的核心合理关切是：读者的注意力会被 -49pp 吸引，忽略 2.2pp 才是 confusability 的 practical magnitude。这是 framing 偏好问题，不是 factual misrepresentation。我的建议是在 Abstract 中更突出 2.2pp 的实际含义（如加入\"below deployment-relevant thresholds\"的表述），而非删除 -49pp（它准确反映了 Dimension 1 的严重性）。\n\n但我同意 R2 的一个隐含批评：Introduction (§1) 的 findings summary 反复强调极端 batch gap（\"extreme-batch construction amplifies this to −31.2pp\"）而将 2.2pp practical magnitude 放在 §5.3 的一个 paragraph 中，叙事重心确实偏向了戏剧性数字。\n\n**[AGREE substantially] R2-N3: NER 和 ED 本质是 null result，削弱 generality claim**\n\n这是 R2 审稿意见中最有力的一条。\n\n证据：\n- NER batch-level BCS--F1: r≈0, n=450, §5.3 prompt sensitivity\n- MAVEN per-type BCS--F1: 正相关被 centrality confound 完全解释，partial correlation p>0.2, Appendix §G\n- NER pairwise SCS: r=0.112, r²=1.3%, Table 2\n- 论文标题 \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\" 无任务限定\n\n然而我要区分两个层面：\n1. **Dimension 1（count decline）**: 跨任务成立。NER recall 0.72→~0.27（§5.1），MAVEN 有 count-dependent 变化（虽然方向受 centrality confound 影响）。这不是 null result。\n2. **Dimension 2（confusability）**: 仅 RE 在 batch-level 成立。NER pairwise signal 存在但极弱且不聚合到 batch level。MAVEN pairwise signal 存在但 batch/per-type aggregation 被 confound。ED 本质上只有 supplementary 角色。\n\n论文 Contribution 3 将此称为 \"task asymmetry\"（\"BCS explains 22-53% of RE accuracy variance ... yet shows no batch-level signal in NER\"），这是诚实的。但 R2 正确指出标题和 \"three tasks, four datasets\" 的 framing 给读者造成了 confusability 跨任务通用的错误期待。\n\n建议：标题加入 RE-specific 限定，或在 Abstract 中更前置地说明 confusability 的强效应限于 RE。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: MAVEN 参与度极低**\n\n同意。MAVEN 的有效贡献仅限于：（1）pairwise SCS--confusion r=0.129, Table 2；（2）centrality confound 的发现（§5.5, Appendix §G），这本身是一个方法论贡献但不是 IE 实验贡献。Count curve 使用了仅 5 batches/level（§3.3 脚注），且未被正文图表充分展示。MAVEN 更适合 positioned as a case study for centrality confound，而非第四个平等的评估数据集。将 \"four datasets\" 改为 \"three primary datasets + one supplementary case study\" 更准确。\n\n**[AGREE] R2-W2: Logit-scale TOST inconclusive**\n\n与我的 N1 一致。Logit-scale interaction marginally significant（p=0.047），TOST inconclusive（p=0.209）。论文选择 linear scale 作为 primary specification 有利于结论。这是两位 reviewer 的共识 critical issue。\n\n**[AGREE with nuance] R2-W3: Seed SD vs typical BCS gap**\n\nR2 指出 FewRel count=16 的 seed SD=2.7pp（Appendix Table A10）vs typical BCS gap 2.2pp，量级可比。这个比较有启发性但需要 nuance：\n- Seed SD=2.7pp 反映的是 3 个 seeds 的 per-seed mean accuracy 的标准差，sample size 仅 n=3。这个估计本身非常不稳定。\n- 2.2pp 的 typical BCS gap 来自 100 random batches 的回归（§5.3），是 within-seed 的 BCS-attributable 效应。\n- 这两个数字的 measurement 层级不同（between-seed variance vs within-seed regression），直接比较有概念上的问题。\n\n但 R2 的核心 point 成立：如果换一个 seed，2.2pp 的 gap 估计可能波动到比如 0pp 或 5pp，这说明 practical magnitude claim 的 precision 被单 seed 设计限制了。这与我的 W3 一致。\n\n**[REBUT partially] R2-W4: Abstract \"-49pp\" 混淆 Dimension 1 和 2**\n\nAbstract 明确标注 \"-49pp, document-level RE at full schema\" 为 \"count-related recall decline\"，并以 \"dominates\" 连接 \"confusability-related type substitution (≈2.2pp)\"。两个 dimension 在语法上是 parallel 结构中的独立成分，没有混淆。不过我同意 R2 的隐含批评：对不仔细阅读的读者，-49pp 的数字冲击力可能遮盖结构化区分。这是 minor presentation issue，不是 factual error。\n\n**[CANNOT ASSESS] R2-W5: 缺失 DLiSC 和 SPT**\n\nR2 未提供 DLiSC 和 SPT 的完整引用信息（全称、作者、年份、venue）。如果 R2 能提供具体文献信息，我可以评估其相关性。在此之前无法判断。\n\n**[AGREE] R2-W6: Orphan bib entries**\n\n经确认，references.bib 中至少 5 个条目在任何 .tex 文件中未被引用：bogdanov2024nuner、xie2024selfimproving、zhang2023llmaaa、cheng2023batch、levy-2024-same-task。这是格式问题，应在提交前清理。\n\n---\n\n## 对 R2 Overall Assessment 的评论\n\nR2 给出 Soundness 3.5 / Excitement 2.5 / Overall 3.0 (Findings)。\n\n我同意 Soundness 3.5 的判断（与我一致）。对于 Excitement，R2 给 2.5 理由是\"强结果集中在 RE，NER/ED 基本 null results，SCS/BCS 无新颖性，typical effect size 2.2pp practical significance 有限\"。\n\n我对 Excitement 给 3.0 而非 2.5，原因如下：\n1. **Task asymmetry 本身是一个有价值的发现**（Contribution 3）。BCS predicts RE but not NER 不仅是 null result，而是揭示了 constrained decoding vs unconstrained generation 的 error channeling 差异（§7 Discussion），这对理解 training-free IE 的 failure modes 有实质价值。\n2. **Centrality confound 的发现和诊断**（§5.5）对后续使用 embedding-based metrics 做 IE 研究的人有方法论指导意义。\n3. **SDGD 负面结果的诊断深度**（merge amplification + routing failure）比简单报告 \"decomposition doesn't work\" 有更高的信息价值。\n\n但我理解 R2 的 perspective：如果把论文定位为 \"confusability predicts IE degradation\" 的正面故事，那确实 excitement 有限（因为强效应仅 RE，且 practical gap 2.2pp）。如果定位为 \"understanding failure modes of training-free IE\" 的分析性论文，excitement 更高。\n\n我的 Overall 3.5 vs R2 的 3.0，差距主要在对负面结果价值的判断上。\n\n---\n\n## R1-R2 共识总结\n\n两位 Reviewer 达成共识的 critical/major issues：\n1. **Logit-scale TOST inconclusive**（R1-N1, R2-W2）: bounded association claim 需重新表述\n2. **NER/ED generality 被 overclaim**（R1-W4 部分, R2-N3）: confusability 的强故事限于 RE\n3. **Single-seed 对 practical magnitude 的限制**（R1-W3, R2-W3）\n4. **DocRED R²=0.53 的 CI 极宽**（R1-N2）: R2 未直接提及但其 N2 的 practical significance 批评隐含了对这一数字稳健性的怀疑\n\n两位 Reviewer 意见分歧：\n- **SCS novelty**（R2-N1）：R2 将此列为 critical，我认为是 moderate presentation issue（论文已在 §2 self-qualify）\n- **Abstract framing**（R2-N2）：R2 认为 cherry-picking，我认为 Abstract 在事实上做了正确的 Dim1/Dim2 区分，但叙事重心确实偏向戏剧性数字\n",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 交叉回应 Reviewer 2 审稿意见\n\n---\n\n## Must-Fix 问题\n\n**[AGREE with qualification] R2-N1: SCS/BCS 无独立新颖性**\n\n同意 SCS 在形式上就是 pairwise cosine similarity，论文 §2 \"SCS novelty\" 段落自己承认了这一点（\"SCS shares its formal definition ... with the partitioning criterion used in LLM-PEE\"）。Contribution list item 2 的措辞 \"We validate that pairwise embedding similarity predicts type confusion\" 实际上比 Abstract 的 \"operationalize confusability via SCS\" 更准确。\n\n但我要补充一个 nuance：§2 末尾的论述 \"Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation\" 是一个合理的 positioning。给已有 metric 命名（SCS/BCS）以便论文内部一致引用是写作上的实用选择，不算 overclaim。问题在于 Abstract 的 \"operationalize\" 一词暗示了 SCS 是本文引入的操作化方式，建议改为 \"quantify confusability using pairwise embedding similarity (SCS)\" 或类似措辞以降低新颖性暗示。\n\n**[REBUT partially] R2-N2: Abstract framing 有 cherry-picking 嫌疑**\n\nR2 称 Abstract 领衔 -49pp 造成误导。我认为这一批评部分成立但整体过重。\n\n证据：Abstract 原文为 \"Degradation operates along two dimensions: count-related recall decline (up to −49pp, document-level RE at full schema) dominates confusability-related type substitution (≈2.2pp in typical batches)\"。这一句明确做了三件事：（1）将 -49pp 归于 Dimension 1（count），不是 confusability；（2）用 \"dominates\" 正确传达了两个 dimension 的相对重要性；（3）紧随其后报告了 typical-batch 2.2pp。Abstract 还补充了 \"BCS explains 22-53% of cross-batch RE accuracy variance but not NER\"，明确说了 NER null。\n\nR2 的核心合理关切是：读者的注意力会被 -49pp 吸引，忽略 2.2pp 才是 confusability 的 practical magnitude。这是 framing 偏好问题，不是 factual misrepresentation。我的建议是在 Abstract 中更突出 2.2pp 的实际含义（如加入\"below deployment-relevant thresholds\"的表述），而非删除 -49pp（它准确反映了 Dimension 1 的严重性）。\n\n但我同意 R2 的一个隐含批评：Introduction (§1) 的 findings summary 反复强调极端 batch gap（\"extreme-batch construction amplifies this to −31.2pp\"）而将 2.2pp practical magnitude 放在 §5.3 的一个 paragraph 中，叙事重心确实偏向了戏剧性数字。\n\n**[AGREE substantially] R2-N3: NER 和 ED 本质是 null result，削弱 generality claim**\n\n这是 R2 审稿意见中最有力的一条。\n\n证据：\n- NER batch-level BCS--F1: r≈0, n=450, §5.3 prompt sensitivity\n- MAVEN per-type BCS--F1: 正相关被 centrality confound 完全解释，partial correlation p>0.2, Appendix §G\n- NER pairwise SCS: r=0.112, r²=1.3%, Table 2\n- 论文标题 \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\" 无任务限定\n\n然而我要区分两个层面：\n1. **Dimension 1（count decline）**: 跨任务成立。NER recall 0.72→~0.27（§5.1），MAVEN 有 count-dependent 变化（虽然方向受 centrality confound 影响）。这不是 null result。\n2. **Dimension 2（confusability）**: 仅 RE 在 batch-level 成立。NER pairwise signal 存在但极弱且不聚合到 batch level。MAVEN pairwise signal 存在但 batch/per-type aggregation 被 confound。ED 本质上只有 supplementary 角色。\n\n论文 Contribution 3 将此称为 \"task asymmetry\"（\"BCS explains 22-53% of RE accuracy variance ... yet shows no batch-level signal in NER\"），这是诚实的。但 R2 正确指出标题和 \"three tasks, four datasets\" 的 framing 给读者造成了 confusability 跨任务通用的错误期待。\n\n建议：标题加入 RE-specific 限定，或在 Abstract 中更前置地说明 confusability 的强效应限于 RE。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: MAVEN 参与度极低**\n\n同意。MAVEN 的有效贡献仅限于：（1）pairwise SCS--confusion r=0.129, Table 2；（2）centrality confound 的发现（§5.5, Appendix §G），这本身是一个方法论贡献但不是 IE 实验贡献。Count curve 使用了仅 5 batches/level（§3.3 脚注），且未被正文图表充分展示。MAVEN 更适合 positioned as a case study for centrality confound，而非第四个平等的评估数据集。将 \"four datasets\" 改为 \"three primary datasets + one supplementary case study\" 更准确。\n\n**[AGREE] R2-W2: Logit-scale TOST inconclusive**\n\n与我的 N1 一致。Logit-scale interaction marginally significant（p=0.047），TOST inconclusive（p=0.209）。论文选择 linear scale 作为 primary specification 有利于结论。这是两位 reviewer 的共识 critical issue。\n\n**[AGREE with nuance] R2-W3: Seed SD vs typical BCS gap**\n\nR2 指出 FewRel count=16 的 seed SD=2.7pp（Appendix Table A10）vs typical BCS gap 2.2pp，量级可比。这个比较有启发性但需要 nuance：\n- Seed SD=2.7pp 反映的是 3 个 seeds 的 per-seed mean accuracy 的标准差，sample size 仅 n=3。这个估计本身非常不稳定。\n- 2.2pp 的 typical BCS gap 来自 100 random batches 的回归（§5.3），是 within-seed 的 BCS-attributable 效应。\n- 这两个数字的 measurement 层级不同（between-seed variance vs within-seed regression），直接比较有概念上的问题。\n\n但 R2 的核心 point 成立：如果换一个 seed，2.2pp 的 gap 估计可能波动到比如 0pp 或 5pp，这说明 practical magnitude claim 的 precision 被单 seed 设计限制了。这与我的 W3 一致。\n\n**[REBUT partially] R2-W4: Abstract \"-49pp\" 混淆 Dimension 1 和 2**\n\nAbstract 明确标注 \"-49pp, document-level RE at full schema\" 为 \"count-related recall decline\"，并以 \"dominates\" 连接 \"confusability-related type substitution (≈2.2pp)\"。两个 dimension 在语法上是 parallel 结构中的独立成分，没有混淆。不过我同意 R2 的隐含批评：对不仔细阅读的读者，-49pp 的数字冲击力可能遮盖结构化区分。这是 minor presentation issue，不是 factual error。\n\n**[CANNOT ASSESS] R2-W5: 缺失 DLiSC 和 SPT**\n\nR2 未提供 DLiSC 和 SPT 的完整引用信息（全称、作者、年份、venue）。如果 R2 能提供具体文献信息，我可以评估其相关性。在此之前无法判断。\n\n**[AGREE] R2-W6: Orphan bib entries**\n\n经确认，references.bib 中至少 5 个条目在任何 .tex 文件中未被引用：bogdanov2024nuner、xie2024selfimproving、zhang2023llmaaa、cheng2023batch、levy-2024-same-task。这是格式问题，应在提交前清理。\n\n---\n\n## 对 R2 Overall Assessment 的评论\n\nR2 给出 Soundness 3.5 / Excitement 2.5 / Overall 3.0 (Findings)。\n\n我同意 Soundness 3.5 的判断（与我一致）。对于 Excitement，R2 给 2.5 理由是\"强结果集中在 RE，NER/ED 基本 null results，SCS/BCS 无新颖性，typical effect size 2.2pp practical significance 有限\"。\n\n我对 Excitement 给 3.0 而非 2.5，原因如下：\n1. **Task asymmetry 本身是一个有价值的发现**（Contribution 3）。BCS predicts RE but not NER 不仅是 null result，而是揭示了 constrained decoding vs unconstrained generation 的 error channeling 差异（§7 Discussion），这对理解 training-free IE 的 failure modes 有实质价值。\n2. **Centrality confound 的发现和诊断**（§5.5）对后续使用 embedding-based metrics 做 IE 研究的人有方法论指导意义。\n3. **SDGD 负面结果的诊断深度**（merge amplification + routing failure）比简单报告 \"decomposition doesn't work\" 有更高的信息价值。\n\n但我理解 R2 的 perspective：如果把论文定位为 \"confusability predicts IE degradation\" 的正面故事，那确实 excitement 有限（因为强效应仅 RE，且 practical gap 2.2pp）。如果定位为 \"understanding failure modes of training-free IE\" 的分析性论文，excitement 更高。\n\n我的 Overall 3.5 vs R2 的 3.0，差距主要在对负面结果价值的判断上。\n\n---\n\n## R1-R2 共识总结\n\n两位 Reviewer 达成共识的 critical/major issues：\n1. **Logit-scale TOST inconclusive**（R1-N1, R2-W2）: bounded association claim 需重新表述\n2. **NER/ED generality 被 overclaim**（R1-W4 部分, R2-N3）: confusability 的强故事限于 RE\n3. **Single-seed 对 practical magnitude 的限制**（R1-W3, R2-W3）\n4. **DocRED R²=0.53 的 CI 极宽**（R1-N2）: R2 未直接提及但其 N2 的 practical significance 批评隐含了对这一数字稳健性的怀疑\n\n两位 Reviewer 意见分歧：\n- **SCS novelty**（R2-N1）：R2 将此列为 critical，我认为是 moderate presentation issue（论文已在 §2 self-qualify）\n- **Abstract framing**（R2-N2）：R2 认为 cherry-picking，我认为 Abstract 在事实上做了正确的 Dim1/Dim2 区分，但叙事重心确实偏向戏剧性数字\n",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 921 · 2026-05-18T05:35:24.171346+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4013
}
```

</details>

---


### Assistant

_source line 922 · 2026-05-18T05:35:32.428116+00:00_

交叉回应已提交。

总结：
- **R2-N1 (SCS novelty)**: 部分同意，SCS 形式无新颖性，但 "operationalize" 措辞修改即可解决
- **R2-N2 (Abstract cherry-picking)**: 部分反驳，Abstract 已明确区分 Dim1/Dim2 并报告 2.2pp，但叙事重心确实偏向戏剧性数字
- **R2-N3 (NER/ED null results)**: 实质同意，这是 R2 最有力的批评，confusability 强故事仅限 RE，标题和 framing 应加限定
- **R2-W1-W6**: W1(MAVEN)同意, W2(logit TOST)同意(与我的N1一致), W3(seed SD)有nuance地同意, W4(Abstract混淆)部分反驳, W5(DLiSC/SPT)缺信息无法评估, W6(orphan bib)确认存在

两位 Reviewer 的共识 critical issues: logit-scale TOST 不确定性、NER/ED generality overclaim、single-seed 限制。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 32

## Round 32

48 recorded events


### User

_source line 923 · 2026-05-18T07:04:30.862768+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Round 1, Reviewer 1

**你的审查侧重: 方法严谨性 + 实验设计 + 统计分析**

### 论文信息
- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
- **路径**: `projects/schema-dag-extraction/docs/paper/main.tex`（含附录；各章节为独立 .tex 文件在同一目录）
- **目标 venue**: EMNLP 2026 via ARR May 2026
- **截止日期**: 2026-05-25
- **类型**: Long paper

### Venue 格式要求
- 正文 ≤ 8 页（不含 Limitations、参考文献、附录）
- 模板: ACL style `\usepackage[review]{acl}`
- Double-blind 匿名
- Limitations section 必须存在（不计页数）
- Responsible NLP checklist 必须填写
- 附录不计页数但关键贡献必须在正文中
- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

### 你的审查重点

请重点评估以下方面：

1. **SCS/BCS 指标设计的合理性**: 
   - 用 embedding cosine similarity 量化 type confusability 是否有充分理论依据？
   - 选择 MiniLM vs Qwen3 做 embedding 的决策是否合理？两者结果不一致时如何处理？
   - BCS 作为 pairwise SCS 的均值聚合是否丢失了重要信息？

2. **实验设计与控制**:
   - BCS-controlled 实验是否真正隔离了 confusability？是否存在未控制的混杂变量？
   - Count curve 实验的 batch 采样策略是否引入偏差？
   - 跨模型验证的充分性（Qwen3-32B 为主，Llama 8B/70B、Gemini Flash 为辅）
   - 单 seed（seed=42）+ greedy decoding 是否足够？

3. **统计分析严谨性**:
   - TOST 等价性检验的 margin 选择（±3pp）是否合理？
   - Pairwise r²=1.3-1.7% 的效应量是否过小？"small but real" 的论证是否令人信服？
   - Bootstrap CI 的使用是否恰当？样本量是否足够？
   - 多重比较的处理方式（声称无需 family-wise correction）是否合理？

4. **负面结果的呈现**:
   - SDGD 失败的诊断是否充分？
   - Schema intervention 实验 inconclusive 的归因是否合理？
   - Few-shot 未能缓解 confusability 的结论是否过强？

5. **因果推断声明**:
   - 论文声称 "correlational evidence with controlled stratification"——控制变量设计是否支持因果方向的推断？
   - "confusability predicts type confusion" 的因果方向证据是否充分？

请按以下格式输出审稿意见：
```
## Summary（2-3句）
## Strengths（逐条）
## Weaknesses（逐条，标注 [CRITICAL] / [MAJOR] / [MINOR]）
## Questions（需要作者澄清的问题）
## Missing References（如有）
## Overall Assessment（评分 + 置信度 1-5）
## Detailed Comments（逐节）
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-18T07:04:37.454551+00:00_

called Skill

<details open><summary>🔧 Tool call — Skill</summary>

```json
{
  "skill": "review-reviewer-session-start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Skill",
  "tool_args": {
    "skill": "review-reviewer-session-start"
  }
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-18T07:04:37.505299+00:00_

&lt;tool_use_error>Unknown skill: review-reviewer-session-start&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Skill",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-18T07:04:40.871573+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-18T07:04:42.075818+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1204
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-18T07:04:42.076309+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 929 · 2026-05-18T07:04:42.127036+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 930 · 2026-05-18T07:04:48.654342+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 931 · 2026-05-18T07:04:48.856032+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 932 · 2026-05-18T07:04:48.907164+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 933 · 2026-05-18T07:04:48.907680+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 934 · 2026-05-18T07:04:49.008409+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 935 · 2026-05-18T07:04:56.140661+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I've found comprehensive information about ACL ARR reviewer guidelines for 2025-2026. Here's a summary of the key information:

## Reviewer Scores (2025 onwards)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justifie
…[truncated 1235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7486
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-18T07:05:01.012254+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other fields."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other fields."
  }
}
```

</details>

---


### Tool call

_source line 937 · 2026-05-18T07:05:01.515620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 938 · 2026-05-18T07:05:02.421269+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 (count-associated decline) has been validated on a proprietary model (Gemini 2.5 Flash, $\rho = -0.900$, $p = 0.037$; Appendix~\ref{sec:appendix_cross_model_gemini}); Dimension~2 (confusability-associated type substitution) has been verified only on open-weight models. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). A FewRel factorial with TOST equivalence testing is consistent with bounded association under the primary linear specification ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp); however, the logit-scale TOST is inconclusive ($p = 0.209$). At $n =
…[truncated 49913 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 939 · 2026-05-18T07:05:02.421832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 940 · 2026-05-18T07:05:02.472539+00:00_

1	\begin{abstract}
2	As large language models are increasingly deployed for information extraction without task-specific training, understanding how schema design affects extraction quality becomes critical for reliable deployment. Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors across NER, RE, and event detection on four datasets and quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation (BCS). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp, document-level RE at full schema) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); BCS explains 22--53\% of cross-batch RE accuracy variance but not NER, where boundary detection failures overwhelm the signal (confusability operates at the pair level across tasks but aggregates to batch-level predictive power only in RE). Few-shot demonstrations do not reduce the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Count-related decline (Dimension~1) replicates across model scales (8B to 70B) and architecture families including Gemini 2.5 Flash; confusability effects (Dimension~2) are verified on open-weight models (Qwen, LLaMA).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 941 · 2026-05-18T07:05:02.523155+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 942 · 2026-05-18T07:05:02.573910+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
…[truncated 3260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 943 · 2026-05-18T07:05:08.046388+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with unlikely but conceivable oversights
- **3**: Pretty sure but possibly missed details
- **2**: Willing to defend evaluation but likely missed some details
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: Excellent thoroughness for paper type
- **4**: Strong support for claims; extra experiments optional
- **3**: Acceptable support for main claims with minor gaps
- **2**: Poor; main claims lack sufficient support
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: Would mention paper to others or attend presentation
- **3**: Might mention points or attend if time permits
- **2**: Potentially interesting despite lacking personal resonance
- **1**: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance recommended
- **3**: Findings track acceptance
- **2**: Needs substantial revisions for next cycle
- **1**: "Do not resubmit: This paper has to be fully redone"

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty
- **2**: "Hard pressed to reproduce the results"
- **1**: Cannot reproduce

## 6. **Datasets & Software**
Scale: 1-5 (separate dimensions)
- **5**: Enabling value for future projects
- **4**: Useful for ongoing work
- **3**: Potentially useful
- **2**: Documentary value only
- **1**: No usable materials submitted

## 7. 
…[truncated 235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7034
}
```

</details>

---


### Tool call

_source line 944 · 2026-05-18T07:05:12.717194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 945 · 2026-05-18T07:05:13.018772+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting 
…[truncated 3068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-18T07:05:13.171426+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 947 · 2026-05-18T07:05:13.523916+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate th
…[truncated 8143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-18T07:05:13.674832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-18T07:05:13.675537+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\pm 1$\,SD across 3 seeds (42, 123, 456) $\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}); schema configura
…[truncated 10981 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-18T07:05:20.006121+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 951 · 2026-05-18T07:05:20.312428+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapse (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation thus recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation \citep{jagannatha2020calibrating} to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\resi
…[truncated 533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 306
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-18T07:05:20.313021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-18T07:05:20.514314+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED slope $-$0.71, adjusted $R^2 = 0.51$, 95\% CI [0.27, 0.73]) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%); conditional on nonzero confusion (${\sim}11\%$ of pairs), $R^2$ rises to 7\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\% (Monte Carlo simulation, Appendix~\ref{app:aggregation-sim}), consistent with the observed 22--53\% in RE.
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific ($R^2 = 0.22$--$0.53$ vs.\ $r \approx 0$ for NER, $n = 450$). RE's constrained decoding (enum constraint) channels all errors into type substitution, so batch confusability directly predicts accuracy; these effect sizes may represent upper bounds specific to the constrained-classification format. NER uses unconstrained generation, where errors scatter across missed entities (43--65\%), boundary misalignment, and hallucinated types, diluting the pairwise signal. We hypothesize the NER U-shape (\S\ref{sec:count_curves}) reflects a dual-task burden: partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers.
12	
13	\paragraph{Practical implications.}
14	The bounded count$\times$confusability interaction (0.47\,pp, TOST $p = 0.003$) implies no confusability amplification at scale. For RE, upper-SCS-quartile
…[truncated 1277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-18T07:05:20.514797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-18T07:05:20.565356+00:00_

1	% DEPRECATED — this file is no longer included in main.tex.
2	% The active conclusion is in discussion.tex (\input{discussion}).
3	% Kept for reference only; safe to delete.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-18T07:05:24.584627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 957 · 2026-05-18T07:05:25.089476+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{lla
…[truncated 4522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 958 · 2026-05-18T07:05:25.090020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
  }
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-18T07:05:25.291548+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	
11	\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	All supplementary material is included in the appendix of the main paper.
19	
20	\end{document}
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-18T07:05:25.294105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-18T07:05:25.346345+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-18T07:05:31.274869+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool call

_source line 963 · 2026-05-18T07:05:32.933569+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, including what reviewers should focus on, how to evaluate soundness and excitement, and any specific guidance on empirical papers, negative results, and statistical methodology."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, including what reviewers should focus on, how to evaluate soundness and excitement, and any specific guidance on empirical papers, negative results, and statistical methodology."
  }
}
```

</details>

---


### Tool result

_source line 964 · 2026-05-18T07:06:12.693877+00:00_

&lt;persisted-output>
Output too large (51.6KB). Full output saved to: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/003126a2-b03b-4f2d-ba1a-7cbaf8acf877/tool-results/toolu_01SDtzf6ZJs7gZJBPnmpQyzR.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 63, \"total_citations\": 89, \"unique_cited_keys\": 63, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 49, \"online_not_found\": 4, \"online_mismatch\": 10}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"schuirmann-1987-tost\", \"type\": \"article\", \"title\": \"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioava...\", \"authors\": \"Schuirmann, Donald J.\", \"year\": \"1987\", \"venue\": \"Journal of Pharmacokinetics and Biopharmaceutics\"}, {\"key\": \"gemini-2025\", \"type\": \"article\", \"title\": \"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\", \"authors\": \"Comanici, Gheorghe and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2507.06261\"}, {\"key\": \"snell2017prototypical\", \"type\": \"inproceedings\", \"title\": \"Prototypical Networks for Few-shot Learning\", \"authors\": \"Snell, Jake and Swersky, Kevin and Zemel, Richard\", \"year\": \"2017\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"muller2019when\", \"type\": \"inproceedings\", \"title\": \"When Does Label Smoothing Help?\", \"authors\": \"M\\\\\\\"uller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.\", \"year\": \"2019\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"peterson2019human\", \"type\": \"inproceedings\", \"title\": \"Human Uncertainty Makes C
…[truncated 371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 41419
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-18T07:06:19.928885+00:00_

# ARR Reviewer Guidelines: Core Principles

## What Reviewers Should Focus On

The guidelines emphasize four primary tasks:

1. **Allocate adequate time** for both reviewing and discussion phases
2. **Check assignment suitability** by verifying expertise, conflicts of interest, and anonymity concerns
3. **Write substantive reviews** with specific, actionable feedback
4. **Engage in post-response discussion** to acknowledge author clarifications

## Evaluating Soundness and Excitement

Starting February 2025, reviewers provide three distinct scores:

**Soundness:** "The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

**Excitement:** Represents personal interest independent of technical quality. Authors note that "low soundness scores without sufficient justification could be reliance on some unconscious bias."

**Overall Assessment:** A composite recommendation reflecting soundness, excitement, novelty, and potential impact. Papers can merit acceptance even if personally unexciting, particularly resource papers or efficiency improvements benefiting specific communities.

## Guidance on Empirical Papers and Negative Results

Reviewers should recognize that "The bias towards publishing only positive results is a known problem in many fields." Negative results deserve fair evaluation if the community needs knowledge about what systematically fails.

For empirical work, the guidelines flag common problematic heuristics: dismissing results as "unsurprising," expecting SOTA performance, or demanding additional experiments beyond what supports the paper's specific claims.

## Statistical Methodology

Papers should ideally include "appropriate information about their statistical significance (error bars, confidence intervals, statistical significance tests), details about how this was computed." Issues warrantin
…[truncated 156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 46995
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-18T07:06:23.818632+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/003126a2-b03b-4f2d-ba1a-7cbaf8acf877/tool-results/toolu_01SDtzf6ZJs7gZJBPnmpQyzR.txt",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/003126a2-b03b-4f2d-ba1a-7cbaf8acf877/tool-results/toolu_01SDtzf6ZJs7gZJBPnmpQyzR.txt",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 967 · 2026-05-18T07:06:24.185083+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 63, \"total_citations\": 89, \"unique_cited_keys\": 63, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 49, \"online_not_found\": 4, \"online_mismatch\": 10}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"schuirmann-1987-tost\", \"type\": \"article\", \"title\": \"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioava...\", \"authors\": \"Schuirmann, Donald J.\", \"year\": \"1987\", \"venue\": \"Journal of Pharmacokinetics and Biopharmaceutics\"}, {\"key\": \"gemini-2025\", \"type\": \"article\", \"title\": \"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\", \"authors\": \"Comanici, Gheorghe and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2507.06261\"}, {\"key\": \"snell2017prototypical\", \"type\": \"inproceedings\", \"title\": \"Prototypical Networks for Few-shot Learning\", \"authors\": \"Snell, Jake and Swersky, Kevin and Zemel, Richard\", \"year\": \"2017\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"muller2019when\", \"type\": \"inproceedings\", \"title\": \"When Does Label Smoothing Help?\", \"authors\": \"M\\\\\\\"uller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.\", \"year\": \"2019\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"peterson2019human\", \"type\": \"inproceedings\", \"title\": \"Human Uncertainty Makes Classification More Robust\", \"authors\": \"Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russ...\", \"year\": \"2019\", \"venue\": \"Proceedings of the IEEE/CVF International Conference on Computer Vision\"}, {\"key\": \"jagannatha2020calibrating\", \"type\": \"inproceedings\", \"title\": \"Calibrating Structured
…[truncated 50811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 366
}
```

</details>

---


### Tool call

_source line 968 · 2026-05-18T07:10:09.143215+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿意见 — Round 1\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n---\n\n## Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度对性能的影响，将退化分解为两个维度：类型数量（count）和类型语义相似度（confusability），提出 SCS/BCS 指标量化后者，并在 4 个数据集、3 个任务上进行控制实验。核心发现是：count 是主导退化因素；confusability 在 RE 的 batch 级有显著预测力（R²=0.22-0.53），但在 NER 的 batch 级无信号；schema 分解策略（SDGD）因 merge amplification 和 routing failure 而失败。实验方法学严谨，负面结果报告诚实，统计分析全面。主要局限是强结果局限于 RE 的 constrained classification 格式，泛化性受限，且核心度量 SCS 的实际效应量较小（pairwise r²=1.3-1.7%）。\n\n---\n\n## Strengths\n\n**S1. 实验设计精细且控制充分。** BCS-controlled 实验通过固定 count 变化 BCS，是合理的准实验设计。Within-pool 分析（从 80-relation pool 抽 16-relation 子集）有效控制了 pool composition confound，permutation test（p=0.60）增强了因果推断力。FewRel 的平衡设计（每类 700 实例）自然排除了 type frequency 混杂。整体设计远超该领域平均水平。\n\n**S2. 负面结果的诚实与深入报告。** SDGD 失败的诊断（merge amplification 导致精确率崩塌 0.563→0.210；routing failure 下所有非 oracle 策略低于 single-pass baseline）、NER batch 级 null result（r≈0, n=450）、few-shot 无法缓解 confusability gap（+4.3pp）、schema renaming intervention inconclusive——这些负面结果的价值不亚于正面发现，对社区有重要参考意义。\n\n**S3. 全面的稳健性检验。** 跨模型（Qwen3-32B, Llama-8B/70B, Gemini Flash）、跨 prompt 设计（4 种 variants）、跨 embedding（MiniLM vs Qwen3）、cross-seed variance decomposition、BCS aggregation sensitivity（mean vs max）、split-origin covariate analysis——几乎每个核心 claim 都有至少一个独立的稳健性检验，这在 NLP 实证研究中不常见。\n\n**S4. 统计方法学的使用高于 NLP 社区平均水准。** TOST 等价性检验、bootstrap CIs（percentile method, B=10,000）、cluster bootstrap、Jonckheere-Terpstra 趋势检验、partial correlation 控制 centrality confound、permutation tests for slope comparison——方法选择总体恰当。TOST sensitivity analysis（Table 6, Appendix §A3）展示了不同 margin 下的结论变化，这种透明度值得肯定。\n\n**S5. Limitations section 是我见过的同类论文中最详尽的。** 10 条 limitations 加一段 multiple comparisons 讨论，每条都有量化支撑（如 logit-scale power analysis、minimum detectable effect 计算）。这种自我批判的深度增强了论文整体可信度。\n\n---\n\n## Weaknesses\n\n**N1 [CRITICAL] — 强结果限于 RE constrained classification 格式，BCS 的 batch 级预测力对 NER 为零，论文标题和 abstract 的泛化暗示过强。**\n\n- 具体位置：Abstract 第 1 句、Introduction §1 title、§5.1 count curves、§5.3 BCS-controlled、§5.4 multi-channel\n- 问题：BCS 解释 RE 22-53% 的 cross-batch accuracy variance，但在 NER 上 r≈0（n=450, §5.4），MAVEN 因 centrality confound 需要剔除（§5.5）。三个 task 中只有 RE（且是 constrained enum classification）给出了强 batch-level 信号。论文标题 \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\" 暗示了跨任务的泛化结论，但实际上标题应更精确地限定为 RE 或 constrained classification。Discussion §7 承认 \"RE-specific\" 和 \"upper bounds specific to the constrained-classification format\"，但这个 caveat 在 abstract 和 introduction 中不够突出。\n- 为什么影响接收：如果 BCS 的预测力仅限于 closed-set constrained classification（这实际上是一个比较狭窄的 IE setting），那么论文对 \"schema complexity in LLM IE\" 的广泛声明就缺乏支撑。审稿人可能质疑：在更常见的 open-ended generative IE 中，这些发现还成立吗？\n- 建议修改方向：（a）Abstract 和 Introduction 更明确地 scope：BCS 的 batch-level 预测力目前仅在 constrained RE classification 中得到验证；（b）考虑在标题中加入限定词，或在 abstract 首段更早提及 task asymmetry。\n\n**N2 [CRITICAL] — TOST 等价性检验的 ±3pp margin 超过了 typical-batch 主效应（2.2pp），在概念上削弱了 \"bounded association\" 的声明。**\n\n- 具体位置：§5.4 multi-channel（TOST p=0.003 at ±3pp）、Appendix §A3（margin justification 和 sensitivity analysis）、Limitations item 3\n- 问题：Typical-batch BCS gap 仅 2.2pp（§5.3 practical magnitude），但 TOST 的等价 margin 设为 ±3pp。这意味着一个 3pp 的交互效应（比主效应大 36%）仍会被视为 \"equivalent to zero\"。论文自己也承认（Appendix §A3）：\"A 3pp interaction atop the 2.2pp main effect would represent >130% amplification, fundamentally changing whether confusability warrants mitigation.\" 但随即用 \"the interaction is bounded below that\" 来论证。\n- 技术问题：（a）在 ±2pp margin 下，TOST 仅 marginally equivalent（p=0.047）；在 ±1pp 下 inconclusive（p=0.278）。如果研究者关心的是 \"interaction 是否达到主效应的一半\"（即 1.1pp），当前数据无法回答这个问题。（b）Logit-scale TOST inconclusive（p=0.209），论文以 \"insufficient power\" 解释，但这正是问题所在：当 accuracy 接近 50% 时 linear scale 压缩效应，logit scale 更适合 bounded data，inconclusive 结果不应被轻视。\n- 为什么影响接收：\"bounded association\" 是论文核心 claim 之一（Introduction finding (1)），支撑了 \"count 和 confusability 可分离\" 的叙事。如果 margin 选择使这个声明变得 trivially true（因为 margin > main effect），那么 separability claim 的说服力大打折扣。\n- 建议修改方向：（a）明确报告 \"在 ±2pp margin（主效应大小）下 equivalence 仅 marginal\"；（b）承认 logit-scale 结果的重要性，将其与 linear-scale 结果并列讨论而非降为 sensitivity check；（c）将 \"bounded association\" 的声明弱化为 \"bounded below ±3pp\" 并讨论 what-if at smaller margins。\n\n**W1 [MAJOR] — SCS 缺乏与简单 baseline 指标的对比，无法判断 embedding similarity 是否优于 trivial 的 confusability 度量。**\n\n- 具体位置：§3.2 SCS definition、§2 related work \"SCS novelty\" paragraph\n- 问题：SCS = cosine similarity of type name embeddings。但论文没有与更简单的 confusability proxy 对比：（a）字符串编辑距离或子串重叠（如 \"person-artist\" vs \"person-actor\" 共享 \"person-\" 前缀）；（b）WordNet/Wikidata ontological distance；（c）type hierarchy path length（Few-NERD 有 8 coarse categories，同 category 下的 types 是否天然更 confusable？）。如果一个简单的 \"same parent category\" 二元变量就能解释类似比例的 confusion variance，那么 SCS 的贡献就很有限。\n- 为什么影响评分：SCS 是论文的核心贡献之一（Contribution 2）。如果不与 baseline 度量对比，审稿人无法评估 SCS 的增量价值。Related work 承认 SCS 与 LLM-PEE 的 partitioning criterion 共享定义，但仍声称贡献在于 \"controlled experimental framework\"。如果 framework 本身用任何 confusability proxy 都能得到类似结论，那么 SCS 作为独立贡献就被削弱。\n- 建议修改方向：加入至少 2 个 baseline confusability metrics（如 string overlap + ontological distance）与 SCS 在 pairwise confusion prediction 上的对比。\n\n**W2 [MAJOR] — 16-relation BCS-controlled 实验在关键条件下仅有 single extreme batch per BCS level，缺乏置信区间。**\n\n- 具体位置：Table 4（Appendix §A7 = Table ~\\ref{tab:bcs_controlled}）caption: \"The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.\"\n- 问题：16-relation 的 extreme-batch gap（-9.1pp at count 8）基于单个 low-BCS batch 和单个 high-BCS batch 的比较，没有置信区间。这意味着这个 gap 可能部分源自该特定 batch 组合的偶然因素（如特定 type 的 intrinsic difficulty）。虽然 80-relation 条件有 CI（[17.7, 42.7]），但 16-relation 条件是文中 \"controlled comparison\" 的重要组成部分。\n- 建议：要么增加 16-relation 条件的 replications，要么在正文明确标注此条件为 pilot/illustrative。\n\n**W3 [MAJOR] — FewRel 使用 train+val 合并数据，且对数据污染的论证虽然充分但非决定性。**\n\n- 具体位置：§3.1 FewRel paragraph、Limitations item 9、Appendix §A9\n- 问题：FewRel (2018) 是被广泛使用的数据集，很可能在 Qwen3 和 Llama 的预训练数据中出现。论文合并 train 和 val splits 以获得 80 种 relation（§3.1），这意味着大部分 types 来自 train split。Limitations item 9 的反驳论证（train-origin 准确率反而更低、monotonic decline 与 uniform contamination 矛盾、DocRED replication）合理但非决定性：contamination 可能是 non-uniform 的，某些 relation types 可能比其他更频繁出现在预训练数据中，而这种 non-uniform contamination 的效应难以与 confusability 效应完全分离。\n- 建议：考虑加入一个更新的、contamination 风险更低的 RE 数据集，或报告 FewRel 上的 perplexity/memorization 检测结果。\n\n**W4 [MAJOR] — Pairwise r²=1.3-1.7% 的 \"small but real\" 论证依赖跨学科类比（behavioral research），在 NLP 语境下说服力不足。**\n\n- 具体位置：§2 \"SCS novelty\" paragraph、Table 2、§5.2\n- 问题：论文引用 Cohen (1988) 和 Lakens (2013) 来论证 1.3-1.7% 的 r² 是 \"small but real\"。但（a）behavioral science 中 r²=1-2% 的 individual-difference predictors 通常在大样本（N>1000）上反复复制，而本文 pairwise analysis 的 n 为 1,953 和 11,026 pairs——不算大，尤其考虑到 pair 之间不独立（共享 type 的 pairs 相关）；（b）在 NLP/ML 语境下，一个 predictor 只解释 1.3% 的 variance 通常不足以支撑实际应用价值。论文自己也承认 \"entity frequency, prompt position, mention ambiguity, and definition quality\" 等因素解释剩余 variance，但没有量化它们各自的贡献。\n- 建议：（a）加入这些 confounders 的偏相关分析以展示 SCS 的 unique contribution；（b）或者弱化 pairwise r² 的解释，更多强调 batch-level R² 作为主证据。\n\n**W5 [MINOR] — Few-shot 实验的 \"confusability gap widens\" 结论可能过强。**\n\n- 具体位置：Appendix §A13 Table 11、§5.4 引用\n- 问题：0-shot gap = +18.5pp, 1-shot = +20.0pp, 5-shot = +22.8pp。论文声称 gap \"widens\"（bootstrap p=0.014）。但（a）1-shot high-BCS accuracy (+5.6pp) 比 0-shot 显著提升，说明 few-shot 在高 confusability 下也有用；（b）5-shot high-BCS accuracy 反而下降（-1.0pp vs 0-shot），可能是 prompt length 效应（lost-in-middle）而非 confusability 本身；（c）widening 的 p=0.014 是对 0-shot vs 5-shot gap 差异的 bootstrap test，但只有 3 个 data points（0/1/5-shot），趋势检验的统计力有限。\n- 建议：弱化结论为 \"few-shot 未能 *缩小* confusability gap\"，而非强调 \"widening\"。\n\n**W6 [MINOR] — NER 的 U-shape 解释（\"dual-task burden\"）是 post-hoc 推测，缺乏直接证据。**\n\n- 具体位置：Discussion §7 \"Task-dependent effects\"、§5.1\n- 问题：NER recall 在中间 count 水平下降后在 full-schema 恢复（U-shape），论文解释为 \"partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers.\" 这是一个合理的假设，但没有直接实验验证（如控制 type-filtering overhead 的实验）。\n- 建议：标注为 hypothesis 而非 explanation。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** BCS-controlled 实验中 \"extreme batches\" 的构造方法是什么？是通过优化搜索（如 greedy selection of most/least similar types）还是随机采样后筛选？如果是优化搜索，extreme batches 可能在 type difficulty 上也不平衡（如最相似的 types 恰好也是最难的 types）。Appendix §A12 的 BCS-composition independence analysis 部分回答了这个问题（VIF=1.06），但仅针对 mean type difficulty，是否还有其他 confounders？\n\n**Q2.** RE 使用 constrained decoding（enum constraint），这意味着模型被强制从候选 types 中选择一个。在这种设置下，所有 non-none errors 都必然是 intra-batch substitution。这是否过度放大了 confusability 的 apparent effect？如果使用 unconstrained decoding（模型可以生成不在候选列表中的 type），confusability effect 是否会减弱？\n\n**Q3.** §5.5 Centrality confound 分析显示 MAVEN 的 raw positive BCS-F1 correlation 完全归因于 centrality confounders。在控制 centrality 后，BCS-F1 correlation 消失（p>0.2）。Few-NERD 是否也做了相同的 centrality control？如果做了，结果如何？\n\n**Q4.** 论文声称 \"confusability predicts type confusion\"（因果方向），但 SCS 作为一个 pre-hoc proxy 只建立了相关性。schema renaming intervention 虽然尝试了因果验证但 inconclusive（Limitations item 8）。除了 renaming，是否考虑过其他 intervention（如 adding disambiguating definitions to confusable type pairs）？\n\n**Q5.** DocRED 的 batch 数量（5 per count level）远少于 FewRel（25）。DocRED 的 R²=0.53（高于 FewRel 的 0.218）是否可能被小样本膨胀？Adjusted R² 在 Appendix 中报告（0.511），但 n=35 的 OLS regression with one predictor 的 CI 仍然很宽（[0.27, 0.73]）。\n\n---\n\n## Missing References\n\n未发现重大缺失。引用覆盖了直接相关方法、baseline、benchmark、理论基础和统计方法。引用核查显示 63 条 bib entries 无 orphan 或 missing，49 条在线验证通过。建议补充：\n\n1. 关于 constrained decoding 对 error distribution 的影响：Tam et al. (2024) \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on LLM Performance\" 讨论了 format constraints 如何改变模型行为，与 §7 中 constrained decoding 限制 error channel 的讨论相关。\n2. 关于 embedding-based label similarity 在 zero-shot classification 中的应用：Yin et al. (2019) \"Benchmarking Zero-shot Text Classification\" 使用 label embedding similarity 作为 zero-shot classification 的基础，与 SCS 的概念基础相关。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 — Borderline Conference\n\n**Confidence**: 4/5 — Quite sure; I read the paper carefully and am familiar with both the IE methods and the statistical methodology used.\n\n**一句话总结**: 方法学严谨、负面结果诚实、robustness 检验全面的高质量实证研究，但核心发现（BCS batch-level 预测力）限于 constrained RE classification，泛化性不足以支撑论文标题暗示的广泛 claim；TOST margin 选择和 pairwise effect size 的解释需要加强。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计精良，统计方法选择恰当。但 TOST margin > main effect 削弱 separability claim；logit-scale 结果 inconclusive 未获足够重视；NER/MAVEN 的 null results 缩窄了 claim scope。 |\n| Excitement | 3/5 | 研究问题实际且重要（schema complexity 如何影响 LLM IE），但（a）核心发现局限于 RE constrained classification；（b）SDGD 失败意味着没有 actionable mitigation；（c）pairwise effect 极小。作为分析性工作有价值，但缺乏 exciting 的 takeaway。 |\n| Reproducibility | 4/5 | 代码承诺 release upon acceptance；实验参数详尽（seed, temperature, vLLM version, GPU spec）；prompt templates 完整提供；统计方法有引用。唯一不足是部分 batch construction algorithm 细节（如 extreme batch selection procedure）未完全明确。 |\n| Overall | 3.5/5 | Borderline Conference。方法学质量高、负面结果有价值、robustness 全面。但 generality 局限（RE-only batch-level signal）、TOST margin 问题、缺少 SCS baseline 对比，使得 contribution 的影响力有限。如能解决 N1（scope 表述）和 N2（TOST margin discussion），以及 W1（SCS baseline），可达 Conference。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 论文标题和 abstract 的 scope 与实际发现不匹配\n- 具体位置：标题、Abstract、Introduction §1 contributions (2)-(3)\n- 问题：标题暗示 \"schema complexity predicts performance in LLM IE\" 的通用结论，但 BCS 的 batch-level 预测力仅在 RE constrained classification 中成立；NER batch-level 为 null，MAVEN 需要 centrality adjustment。三任务中仅一个给出强 batch-level signal。\n- 为什么影响接收：scope 过宽的声明是审稿人最常见的 rejection 理由之一。\n- 建议：限定 scope（如 \"under constrained classification\"），或在 abstract/intro 更早更突出地呈现 task asymmetry。\n\n**N2** [critical] TOST margin 选择使 \"bounded association\" claim 变得 trivially satisfiable\n- 具体位置：§5.4、Appendix §A3\n- 问题：±3pp margin 超过 typical main effect（2.2pp），±1pp 下 inconclusive，logit-scale inconclusive。\n- 为什么影响接收：\"dimensions exhibit bounded association\" 是核心叙事支柱。\n- 建议：重新讨论 margin 与 main effect 的关系，给 logit-scale 结果更大权重。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] SCS 缺乏与简单 baseline metrics 的对比\n- 具体位置：§3.2、§2 \"SCS novelty\"\n- 建议：加入 string overlap / ontological distance baselines\n\n**W2** [warning] 16-relation BCS-controlled 条件仅 single batch per extreme, 无 CI\n- 具体位置：Table 4 caption\n- 建议：增加 replications 或标注为 pilot\n\n**W3** [warning] FewRel 数据污染风险的论证合理但非决定性\n- 具体位置：Limitations item 9\n- 建议：补充 contamination detection 或更新数据集 replication\n\n**W4** [warning] Pairwise r²=1.3-1.7% 的 \"small but real\" 论证需加强\n- 具体位置：§2 \"SCS novelty\"、Table 2\n- 建议：加入 confounders 的偏相关分析\n\n## 小问题（不影响接收）\n\n- W5: Few-shot \"widens\" 结论稍强，建议弱化为 \"does not reduce\"\n- W6: NER U-shape \"dual-task burden\" 解释标注为 hypothesis\n- DocRED 和 MAVEN batch 数量少（5 vs 25），power 分析不充分\n- Table 2 caption 中 \"FewRel (r=0.187; §3.2) is excluded as RE's per-instance format precludes direct comparison of confusion rates\"——这个排除的理由不够清楚，建议展开解释\n- Appendix 数量很多（13 sections），部分可精简\n\n## 主要优势\n\n- 控制实验设计精良（BCS-controlled + within-pool + cross-model + cross-prompt），远超同领域平均\n- 负面结果（SDGD 失败、NER batch-level null、few-shot 无效、intervention inconclusive）的诚实报告具有独立学术价值\n- 统计方法学（TOST、bootstrap CI、partial correlation、permutation test）使用恰当且透明\n- Limitations section 的深度和自我批判性是 gold standard\n- Centrality confound 的诊断和处理（§5.5 + Appendix §A5）展示了优秀的分析素养\n",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿意见 — Round 1\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n---\n\n## Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度对性能的影响，将退化分解为两个维度：类型数量（count）和类型语义相似度（confusability），提出 SCS/BCS 指标量化后者，并在 4 个数据集、3 个任务上进行控制实验。核心发现是：count 是主导退化因素；confusability 在 RE 的 batch 级有显著预测力（R²=0.22-0.53），但在 NER 的 batch 级无信号；schema 分解策略（SDGD）因 merge amplification 和 routing failure 而失败。实验方法学严谨，负面结果报告诚实，统计分析全面。主要局限是强结果局限于 RE 的 constrained classification 格式，泛化性受限，且核心度量 SCS 的实际效应量较小（pairwise r²=1.3-1.7%）。\n\n---\n\n## Strengths\n\n**S1. 实验设计精细且控制充分。** BCS-controlled 实验通过固定 count 变化 BCS，是合理的准实验设计。Within-pool 分析（从 80-relation pool 抽 16-relation 子集）有效控制了 pool composition confound，permutation test（p=0.60）增强了因果推断力。FewRel 的平衡设计（每类 700 实例）自然排除了 type frequency 混杂。整体设计远超该领域平均水平。\n\n**S2. 负面结果的诚实与深入报告。** SDGD 失败的诊断（merge amplification 导致精确率崩塌 0.563→0.210；routing failure 下所有非 oracle 策略低于 single-pass baseline）、NER batch 级 null result（r≈0, n=450）、few-shot 无法缓解 confusability gap（+4.3pp）、schema renaming intervention inconclusive——这些负面结果的价值不亚于正面发现，对社区有重要参考意义。\n\n**S3. 全面的稳健性检验。** 跨模型（Qwen3-32B, Llama-8B/70B, Gemini Flash）、跨 prompt 设计（4 种 variants）、跨 embedding（MiniLM vs Qwen3）、cross-seed variance decomposition、BCS aggregation sensitivity（mean vs max）、split-origin covariate analysis——几乎每个核心 claim 都有至少一个独立的稳健性检验，这在 NLP 实证研究中不常见。\n\n**S4. 统计方法学的使用高于 NLP 社区平均水准。** TOST 等价性检验、bootstrap CIs（percentile method, B=10,000）、cluster bootstrap、Jonckheere-Terpstra 趋势检验、partial correlation 控制 centrality confound、permutation tests for slope comparison——方法选择总体恰当。TOST sensitivity analysis（Table 6, Appendix §A3）展示了不同 margin 下的结论变化，这种透明度值得肯定。\n\n**S5. Limitations section 是我见过的同类论文中最详尽的。** 10 条 limitations 加一段 multiple comparisons 讨论，每条都有量化支撑（如 logit-scale power analysis、minimum detectable effect 计算）。这种自我批判的深度增强了论文整体可信度。\n\n---\n\n## Weaknesses\n\n**N1 [CRITICAL] — 强结果限于 RE constrained classification 格式，BCS 的 batch 级预测力对 NER 为零，论文标题和 abstract 的泛化暗示过强。**\n\n- 具体位置：Abstract 第 1 句、Introduction §1 title、§5.1 count curves、§5.3 BCS-controlled、§5.4 multi-channel\n- 问题：BCS 解释 RE 22-53% 的 cross-batch accuracy variance，但在 NER 上 r≈0（n=450, §5.4），MAVEN 因 centrality confound 需要剔除（§5.5）。三个 task 中只有 RE（且是 constrained enum classification）给出了强 batch-level 信号。论文标题 \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\" 暗示了跨任务的泛化结论，但实际上标题应更精确地限定为 RE 或 constrained classification。Discussion §7 承认 \"RE-specific\" 和 \"upper bounds specific to the constrained-classification format\"，但这个 caveat 在 abstract 和 introduction 中不够突出。\n- 为什么影响接收：如果 BCS 的预测力仅限于 closed-set constrained classification（这实际上是一个比较狭窄的 IE setting），那么论文对 \"schema complexity in LLM IE\" 的广泛声明就缺乏支撑。审稿人可能质疑：在更常见的 open-ended generative IE 中，这些发现还成立吗？\n- 建议修改方向：（a）Abstract 和 Introduction 更明确地 scope：BCS 的 batch-level 预测力目前仅在 constrained RE classification 中得到验证；（b）考虑在标题中加入限定词，或在 abstract 首段更早提及 task asymmetry。\n\n**N2 [CRITICAL] — TOST 等价性检验的 ±3pp margin 超过了 typical-batch 主效应（2.2pp），在概念上削弱了 \"bounded association\" 的声明。**\n\n- 具体位置：§5.4 multi-channel（TOST p=0.003 at ±3pp）、Appendix §A3（margin justification 和 sensitivity analysis）、Limitations item 3\n- 问题：Typical-batch BCS gap 仅 2.2pp（§5.3 practical magnitude），但 TOST 的等价 margin 设为 ±3pp。这意味着一个 3pp 的交互效应（比主效应大 36%）仍会被视为 \"equivalent to zero\"。论文自己也承认（Appendix §A3）：\"A 3pp interaction atop the 2.2pp main effect would represent >130% amplification, fundamentally changing whether confusability warrants mitigation.\" 但随即用 \"the interaction is bounded below that\" 来论证。\n- 技术问题：（a）在 ±2pp margin 下，TOST 仅 marginally equivalent（p=0.047）；在 ±1pp 下 inconclusive（p=0.278）。如果研究者关心的是 \"interaction 是否达到主效应的一半\"（即 1.1pp），当前数据无法回答这个问题。（b）Logit-scale TOST inconclusive（p=0.209），论文以 \"insufficient power\" 解释，但这正是问题所在：当 accuracy 接近 50% 时 linear scale 压缩效应，logit scale 更适合 bounded data，inconclusive 结果不应被轻视。\n- 为什么影响接收：\"bounded association\" 是论文核心 claim 之一（Introduction finding (1)），支撑了 \"count 和 confusability 可分离\" 的叙事。如果 margin 选择使这个声明变得 trivially true（因为 margin > main effect），那么 separability claim 的说服力大打折扣。\n- 建议修改方向：（a）明确报告 \"在 ±2pp margin（主效应大小）下 equivalence 仅 marginal\"；（b）承认 logit-scale 结果的重要性，将其与 linear-scale 结果并列讨论而非降为 sensitivity check；（c）将 \"bounded association\" 的声明弱化为 \"bounded below ±3pp\" 并讨论 what-if at smaller margins。\n\n**W1 [MAJOR] — SCS 缺乏与简单 baseline 指标的对比，无法判断 embedding similarity 是否优于 trivial 的 confusability 度量。**\n\n- 具体位置：§3.2 SCS definition、§2 related work \"SCS novelty\" paragraph\n- 问题：SCS = cosine similarity of type name embeddings。但论文没有与更简单的 confusability proxy 对比：（a）字符串编辑距离或子串重叠（如 \"person-artist\" vs \"person-actor\" 共享 \"person-\" 前缀）；（b）WordNet/Wikidata ontological distance；（c）type hierarchy path length（Few-NERD 有 8 coarse categories，同 category 下的 types 是否天然更 confusable？）。如果一个简单的 \"same parent category\" 二元变量就能解释类似比例的 confusion variance，那么 SCS 的贡献就很有限。\n- 为什么影响评分：SCS 是论文的核心贡献之一（Contribution 2）。如果不与 baseline 度量对比，审稿人无法评估 SCS 的增量价值。Related work 承认 SCS 与 LLM-PEE 的 partitioning criterion 共享定义，但仍声称贡献在于 \"controlled experimental framework\"。如果 framework 本身用任何 confusability proxy 都能得到类似结论，那么 SCS 作为独立贡献就被削弱。\n- 建议修改方向：加入至少 2 个 baseline confusability metrics（如 string overlap + ontological distance）与 SCS 在 pairwise confusion prediction 上的对比。\n\n**W2 [MAJOR] — 16-relation BCS-controlled 实验在关键条件下仅有 single extreme batch per BCS level，缺乏置信区间。**\n\n- 具体位置：Table 4（Appendix §A7 = Table ~\\ref{tab:bcs_controlled}）caption: \"The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.\"\n- 问题：16-relation 的 extreme-batch gap（-9.1pp at count 8）基于单个 low-BCS batch 和单个 high-BCS batch 的比较，没有置信区间。这意味着这个 gap 可能部分源自该特定 batch 组合的偶然因素（如特定 type 的 intrinsic difficulty）。虽然 80-relation 条件有 CI（[17.7, 42.7]），但 16-relation 条件是文中 \"controlled comparison\" 的重要组成部分。\n- 建议：要么增加 16-relation 条件的 replications，要么在正文明确标注此条件为 pilot/illustrative。\n\n**W3 [MAJOR] — FewRel 使用 train+val 合并数据，且对数据污染的论证虽然充分但非决定性。**\n\n- 具体位置：§3.1 FewRel paragraph、Limitations item 9、Appendix §A9\n- 问题：FewRel (2018) 是被广泛使用的数据集，很可能在 Qwen3 和 Llama 的预训练数据中出现。论文合并 train 和 val splits 以获得 80 种 relation（§3.1），这意味着大部分 types 来自 train split。Limitations item 9 的反驳论证（train-origin 准确率反而更低、monotonic decline 与 uniform contamination 矛盾、DocRED replication）合理但非决定性：contamination 可能是 non-uniform 的，某些 relation types 可能比其他更频繁出现在预训练数据中，而这种 non-uniform contamination 的效应难以与 confusability 效应完全分离。\n- 建议：考虑加入一个更新的、contamination 风险更低的 RE 数据集，或报告 FewRel 上的 perplexity/memorization 检测结果。\n\n**W4 [MAJOR] — Pairwise r²=1.3-1.7% 的 \"small but real\" 论证依赖跨学科类比（behavioral research），在 NLP 语境下说服力不足。**\n\n- 具体位置：§2 \"SCS novelty\" paragraph、Table 2、§5.2\n- 问题：论文引用 Cohen (1988) 和 Lakens (2013) 来论证 1.3-1.7% 的 r² 是 \"small but real\"。但（a）behavioral science 中 r²=1-2% 的 individual-difference predictors 通常在大样本（N>1000）上反复复制，而本文 pairwise analysis 的 n 为 1,953 和 11,026 pairs——不算大，尤其考虑到 pair 之间不独立（共享 type 的 pairs 相关）；（b）在 NLP/ML 语境下，一个 predictor 只解释 1.3% 的 variance 通常不足以支撑实际应用价值。论文自己也承认 \"entity frequency, prompt position, mention ambiguity, and definition quality\" 等因素解释剩余 variance，但没有量化它们各自的贡献。\n- 建议：（a）加入这些 confounders 的偏相关分析以展示 SCS 的 unique contribution；（b）或者弱化 pairwise r² 的解释，更多强调 batch-level R² 作为主证据。\n\n**W5 [MINOR] — Few-shot 实验的 \"confusability gap widens\" 结论可能过强。**\n\n- 具体位置：Appendix §A13 Table 11、§5.4 引用\n- 问题：0-shot gap = +18.5pp, 1-shot = +20.0pp, 5-shot = +22.8pp。论文声称 gap \"widens\"（bootstrap p=0.014）。但（a）1-shot high-BCS accuracy (+5.6pp) 比 0-shot 显著提升，说明 few-shot 在高 confusability 下也有用；（b）5-shot high-BCS accuracy 反而下降（-1.0pp vs 0-shot），可能是 prompt length 效应（lost-in-middle）而非 confusability 本身；（c）widening 的 p=0.014 是对 0-shot vs 5-shot gap 差异的 bootstrap test，但只有 3 个 data points（0/1/5-shot），趋势检验的统计力有限。\n- 建议：弱化结论为 \"few-shot 未能 *缩小* confusability gap\"，而非强调 \"widening\"。\n\n**W6 [MINOR] — NER 的 U-shape 解释（\"dual-task burden\"）是 post-hoc 推测，缺乏直接证据。**\n\n- 具体位置：Discussion §7 \"Task-dependent effects\"、§5.1\n- 问题：NER recall 在中间 count 水平下降后在 full-schema 恢复（U-shape），论文解释为 \"partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers.\" 这是一个合理的假设，但没有直接实验验证（如控制 type-filtering overhead 的实验）。\n- 建议：标注为 hypothesis 而非 explanation。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** BCS-controlled 实验中 \"extreme batches\" 的构造方法是什么？是通过优化搜索（如 greedy selection of most/least similar types）还是随机采样后筛选？如果是优化搜索，extreme batches 可能在 type difficulty 上也不平衡（如最相似的 types 恰好也是最难的 types）。Appendix §A12 的 BCS-composition independence analysis 部分回答了这个问题（VIF=1.06），但仅针对 mean type difficulty，是否还有其他 confounders？\n\n**Q2.** RE 使用 constrained decoding（enum constraint），这意味着模型被强制从候选 types 中选择一个。在这种设置下，所有 non-none errors 都必然是 intra-batch substitution。这是否过度放大了 confusability 的 apparent effect？如果使用 unconstrained decoding（模型可以生成不在候选列表中的 type），confusability effect 是否会减弱？\n\n**Q3.** §5.5 Centrality confound 分析显示 MAVEN 的 raw positive BCS-F1 correlation 完全归因于 centrality confounders。在控制 centrality 后，BCS-F1 correlation 消失（p>0.2）。Few-NERD 是否也做了相同的 centrality control？如果做了，结果如何？\n\n**Q4.** 论文声称 \"confusability predicts type confusion\"（因果方向），但 SCS 作为一个 pre-hoc proxy 只建立了相关性。schema renaming intervention 虽然尝试了因果验证但 inconclusive（Limitations item 8）。除了 renaming，是否考虑过其他 intervention（如 adding disambiguating definitions to confusable type pairs）？\n\n**Q5.** DocRED 的 batch 数量（5 per count level）远少于 FewRel（25）。DocRED 的 R²=0.53（高于 FewRel 的 0.218）是否可能被小样本膨胀？Adjusted R² 在 Appendix 中报告（0.511），但 n=35 的 OLS regression with one predictor 的 CI 仍然很宽（[0.27, 0.73]）。\n\n---\n\n## Missing References\n\n未发现重大缺失。引用覆盖了直接相关方法、baseline、benchmark、理论基础和统计方法。引用核查显示 63 条 bib entries 无 orphan 或 missing，49 条在线验证通过。建议补充：\n\n1. 关于 constrained decoding 对 error distribution 的影响：Tam et al. (2024) \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on LLM Performance\" 讨论了 format constraints 如何改变模型行为，与 §7 中 constrained decoding 限制 error channel 的讨论相关。\n2. 关于 embedding-based label similarity 在 zero-shot classification 中的应用：Yin et al. (2019) \"Benchmarking Zero-shot Text Classification\" 使用 label embedding similarity 作为 zero-shot classification 的基础，与 SCS 的概念基础相关。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 — Borderline Conference\n\n**Confidence**: 4/5 — Quite sure; I read the paper carefully and am familiar with both the IE methods and the statistical methodology used.\n\n**一句话总结**: 方法学严谨、负面结果诚实、robustness 检验全面的高质量实证研究，但核心发现（BCS batch-level 预测力）限于 constrained RE classification，泛化性不足以支撑论文标题暗示的广泛 claim；TOST margin 选择和 pairwise effect size 的解释需要加强。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计精良，统计方法选择恰当。但 TOST margin > main effect 削弱 separability claim；logit-scale 结果 inconclusive 未获足够重视；NER/MAVEN 的 null results 缩窄了 claim scope。 |\n| Excitement | 3/5 | 研究问题实际且重要（schema complexity 如何影响 LLM IE），但（a）核心发现局限于 RE constrained classification；（b）SDGD 失败意味着没有 actionable mitigation；（c）pairwise effect 极小。作为分析性工作有价值，但缺乏 exciting 的 takeaway。 |\n| Reproducibility | 4/5 | 代码承诺 release upon acceptance；实验参数详尽（seed, temperature, vLLM version, GPU spec）；prompt templates 完整提供；统计方法有引用。唯一不足是部分 batch construction algorithm 细节（如 extreme batch selection procedure）未完全明确。 |\n| Overall | 3.5/5 | Borderline Conference。方法学质量高、负面结果有价值、robustness 全面。但 generality 局限（RE-only batch-level signal）、TOST margin 问题、缺少 SCS baseline 对比，使得 contribution 的影响力有限。如能解决 N1（scope 表述）和 N2（TOST margin discussion），以及 W1（SCS baseline），可达 Conference。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 论文标题和 abstract 的 scope 与实际发现不匹配\n- 具体位置：标题、Abstract、Introduction §1 contributions (2)-(3)\n- 问题：标题暗示 \"schema complexity predicts performance in LLM IE\" 的通用结论，但 BCS 的 batch-level 预测力仅在 RE constrained classification 中成立；NER batch-level 为 null，MAVEN 需要 centrality adjustment。三任务中仅一个给出强 batch-level signal。\n- 为什么影响接收：scope 过宽的声明是审稿人最常见的 rejection 理由之一。\n- 建议：限定 scope（如 \"under constrained classification\"），或在 abstract/intro 更早更突出地呈现 task asymmetry。\n\n**N2** [critical] TOST margin 选择使 \"bounded association\" claim 变得 trivially satisfiable\n- 具体位置：§5.4、Appendix §A3\n- 问题：±3pp margin 超过 typical main effect（2.2pp），±1pp 下 inconclusive，logit-scale inconclusive。\n- 为什么影响接收：\"dimensions exhibit bounded association\" 是核心叙事支柱。\n- 建议：重新讨论 margin 与 main effect 的关系，给 logit-scale 结果更大权重。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] SCS 缺乏与简单 baseline metrics 的对比\n- 具体位置：§3.2、§2 \"SCS novelty\"\n- 建议：加入 string overlap / ontological distance baselines\n\n**W2** [warning] 16-relation BCS-controlled 条件仅 single batch per extreme, 无 CI\n- 具体位置：Table 4 caption\n- 建议：增加 replications 或标注为 pilot\n\n**W3** [warning] FewRel 数据污染风险的论证合理但非决定性\n- 具体位置：Limitations item 9\n- 建议：补充 contamination detection 或更新数据集 replication\n\n**W4** [warning] Pairwise r²=1.3-1.7% 的 \"small but real\" 论证需加强\n- 具体位置：§2 \"SCS novelty\"、Table 2\n- 建议：加入 confounders 的偏相关分析\n\n## 小问题（不影响接收）\n\n- W5: Few-shot \"widens\" 结论稍强，建议弱化为 \"does not reduce\"\n- W6: NER U-shape \"dual-task burden\" 解释标注为 hypothesis\n- DocRED 和 MAVEN batch 数量少（5 vs 25），power 分析不充分\n- Table 2 caption 中 \"FewRel (r=0.187; §3.2) is excluded as RE's per-instance format precludes direct comparison of confusion rates\"——这个排除的理由不够清楚，建议展开解释\n- Appendix 数量很多（13 sections），部分可精简\n\n## 主要优势\n\n- 控制实验设计精良（BCS-controlled + within-pool + cross-model + cross-prompt），远超同领域平均\n- 负面结果（SDGD 失败、NER batch-level null、few-shot 无效、intervention inconclusive）的诚实报告具有独立学术价值\n- 统计方法学（TOST、bootstrap CI、partial correlation、permutation test）使用恰当且透明\n- Limitations section 的深度和自我批判性是 gold standard\n- Centrality confound 的诊断和处理（§5.5 + Appendix §A5）展示了优秀的分析素养\n",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 969 · 2026-05-18T07:10:13.667370+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4524
}
```

</details>

---


### Assistant

_source line 970 · 2026-05-18T07:10:20.999857+00:00_

审稿意见已提交给 Review Director。

**审稿结论：Overall 3.5 (Borderline Conference)**

核心判断：
- **2 个 critical issues**: (1) 标题/abstract scope 过宽，BCS batch-level 预测力仅在 RE constrained classification 成立，NER 为 null；(2) TOST ±3pp margin 超过典型主效应 2.2pp，"bounded association" claim 被削弱
- **4 个 major issues**: SCS 缺 baseline 对比、16-rel 条件仅 single batch、FewRel 污染论证非决定性、pairwise r²=1.3% 的 "small but real" 论证跨学科类比不足
- **主要优势**: 实验设计精良、负面结果诚实、统计方法学全面、Limitations 极为详尽

如作者能解决 scope 表述、TOST margin 讨论、SCS baseline 对比，评分可提升至 Conference (4.0)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 33

## Round 33

14 recorded events


### User

_source line 971 · 2026-05-18T07:11:45.936114+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 — Round 1 审稿意见

**侧重**: 新颖性 + Related Work 覆盖 + 写作质量 + 格式合规

### Summary
本文通过控制实验将 training-free LLM IE 的 schema 复杂度退化分解为两个维度：type count（数量）和 type confusability（混淆性），在 4 个数据集、3 个任务、多个模型上验证。核心发现是：count 导致 recall 下降（已知现象），confusability 导致 type substitution（新观察但效应量小，典型场景仅 2.2 pp），schema decomposition 因 merge amplification 和 routing failure 而失败。论文方法论严谨，但实质性新洞察有限，核心贡献偏向对预期现象的确认（confirmatory）而非发现。

### Weaknesses

**W1. [CRITICAL] 核心新颖性不足——confusability 维度的效应量过小，难以支撑论文的主要贡献叙事**
- Pairwise SCS–confusion correlation: r²=1.3–1.7%（Table 2）
- 典型 batch 场景下 BCS quartile gap 仅 2.2 pp（§4.3, 95% CI [0.4, 4.0]）
- BCS 在 NER 上 batch-level 完全无信号（r≈0, n=450, §4.4）
- Per-type 分析在 MAVEN 上被 centrality confound 完全解释掉
- 论文多次展示 extreme-batch gaps（-31.2 pp），但这些是人为构造的极端条件，不代表实际部署场景
- 对于 EMNLP 顶会，r²=1.3% 的 predictor + NER 上无效的 finding，贡献度是否足以接收需要认真考量

**W2. [CRITICAL] "First controlled study" claim 过度宣称**
- LLM-PEE 已使用完全相同的 metric（type embedding cosine similarity）进行 schema partitioning
- PARSE 优化 schema definitions 来减少 type confusion——隐含了 confusability 维度的操纵
- Haystack-to-Needle 通过 iterative label space reduction 直接解决 label space size 导致的退化
- "Controlled study"是 methodology contribution，不是 finding contribution
- 建议改为"the first study that explicitly disentangles..."

**W3. [MAJOR] 论文定位模糊——empirical analysis paper 的接收标准未被充分满足**
- Finding 1（count 导致退化）：Li et al. (2023) 已观察到，不是新发现
- Finding 2（confusability 导致 type substitution）：领域知识就能预测到
- Finding 3（跨模型一致）：属于 robustness check
- Finding 4（SDGD 失败）：最有价值但是负面结果
- 未充分回答"为什么理解这个问题比解决这个问题更重要"
- Discussion §practical implications 仅两句话

**W4. [MAJOR] Abstract 过度压缩，信息密度超过可读阈值**
- SCS、BCS、SDGD 等缩写和大量数字在一段中
- 嵌套括号注释在 Abstract 中不合适
- 建议减少数字到 2-3 个关键的

**W5. [MAJOR] Introduction findings 段过密**
- 每条 finding 包含统计量（TOST p-value、R² 精确值等）
- 这些属于 Results，不属于 Introduction

**W6. [MAJOR] Task asymmetry 削弱 generalizability claim**
- RE: BCS works, R²=0.22–0.53
- NER: batch-level BCS 无效
- ED (MAVEN): centrality confound
- 不是"across three tasks"的一致发现，而是"primarily an RE finding"

**W7. [MINOR] Related Work 缺少 label bias/label length bias 文献**

**W8. [MINOR] "Notably" 用法（results.tex:49）是 AI 写作标志**

**W9. [MINOR] Contribution 3 的 claim 边界——task asymmetry 可能由 evaluation format 驱动**

### Questions
Q1. BCS 在 RE 上的高 R² 是否由 constrained decoding 人为放大？
Q2. FewRel train+val 合并是否改变了 val-origin types 的"熟悉度"特征？
Q3. NER 的 U-shape rebound 为什么 RE 没有类似现象？
Q4. 1-shot 在 high-BCS 上提升 +5.6pp，5-shot 反而降回，是否是 prompt length artifact？

### Missing References
1. Fei et al. "Quantifying and Mitigating Label Bias in LLMs" (NAACL 2024)
2. "Mitigating Label Length Bias in Large Language Models" (2025)
3. Zhao et al. "Label-Guided In-Context Learning for Named Entity Recognition" (2025)

### Overall Assessment
**3.0 (Findings)**, Confidence 4/5
Soundness 4.0, Excitement 2.5, Reproducibility 4.5

---

请逐条回应上述 Weaknesses（W1-W9）、Questions（Q1-Q4）和 Missing References，标注 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 972 · 2026-05-18T07:12:24.463801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-18T07:12:25.095060+00:00_

1	\begin{abstract}
2	As large language models are increasingly deployed for information extraction without task-specific training, understanding how schema design affects extraction quality becomes critical for reliable deployment. Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors across NER, RE, and event detection on four datasets and quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation (BCS). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp, document-level RE at full schema) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); BCS explains 22--53\% of cross-batch RE accuracy variance but not NER, where boundary detection failures overwhelm the signal (confusability operates at the pair level across tasks but aggregates to batch-level predictive power only in RE). Few-shot demonstrations do not reduce the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Count-related decline (Dimension~1) replicates across model scales (8B to 70B) and architecture families including Gemini 2.5 Flash; confusability effects (Dimension~2) are verified on open-weight models (Qwen, LLaMA).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 631
}
```

</details>

---


### Tool call

_source line 974 · 2026-05-18T07:12:25.095522+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "offset": "13",
  "limit": "14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "offset": "13",
    "limit": "14"
  }
}
```

</details>

---


### Tool result

_source line 975 · 2026-05-18T07:12:25.354676+00:00_

13	
14	Our experiments yield four findings:
15	(1)~Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) and confusability-related type substitution (typical-batch gap ${\approx}\,2.2$\,pp), with count as the dominant factor (\S\ref{sec:count_curves}, \S\ref{sec:multi_channel}). The two dimensions exhibit bounded association in RE (Two One-Sided Tests [TOST] equivalence, $p = 0.003$ at $\pm 3$\,pp) but are coupled in NER.
16	(2)~Pairwise SCS predicts type confusion across NER, RE, and ED ($r = 0.112$--$0.129$; \S\ref{sec:pairwise}); at batch level, BCS predicts accuracy in RE ($R^2 = 0.22$--$0.53$; \S\ref{sec:bcs_controlled}) but not in NER (batch-level $r \approx 0$, n.s.); per-type aggregation is confounded by centrality on homogeneous schemas (\S\ref{sec:centrality_confound}).
17	(3)~Effects are consistent across schema sizes (BCS slopes: $p = 0.60$; DocRED: $R^2 = 0.53$, 95\% CI [0.27, 0.73], $n = 35$), prompt designs, and model families (\S\ref{sec:bcs_controlled}).
18	(4)~Schema decomposition fails due to merge amplification in NER; RE confusability-aware grouping yields no significant improvement over random (+1.4\,pp, $p \approx 0.19$, n.s.) despite oracle routing that recovers +29.8\,pp (\S\ref{sec:sdgd}).
19	
20	Our contributions are:
21	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
22	    \item We conduct the first controlled study that isolates count and confusability effects on training-free LLM IE performance across four datasets and three tasks (\S\ref{sec:count_curves}, \S\ref{sec:bcs_controlled}).
23	    \item We validate that pairwise embedding similarity predicts type confusion and show that weak pair-level signals ($r = 0.11$--$0.19$) amplify to batch-level predictive power ($R^2 = 0.22$--$0.53$) through correlated aggregation (\S\ref{sec:pairwise}, \S\ref{sec:bcs_controlled}).
24	    \item We discover a task asymmetry: BCS explains 22--53\% of RE accuracy variance through type su
…[truncated 383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 259
}
```

</details>

---


### Tool call

_source line 976 · 2026-05-18T07:12:25.506445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "46",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "46",
    "limit": "8"
  }
}
```

</details>

---


### Tool result

_source line 977 · 2026-05-18T07:12:25.609572+00:00_

46	
47	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\rho = 0.144\text{--}0.227$ across all pairs, strengthening to $\rho = 0.27\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).
48	
49	The remaining variance likely reflects entity frequency, prompt position \cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\,pp under typical batching (\S\ref{sec:practical_magnitude}). Notably, the independent MiniLM embedding yields a \emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\ Qwen3 $r = 0.138$; Appendix), which indicates that shared-representation bias is conservative rather than inflationary.
50	
51	\subsection{BCS-Controlled Experiments}
52	\label{sec:bcs_controlled}
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-18T07:12:29.330749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "offset": "11",
  "limit": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "offset": "11",
    "limit": "7"
  }
}
```

</details>

---


### Tool result

_source line 979 · 2026-05-18T07:12:29.833747+00:00_

11	
12	\paragraph{SCS novelty.} SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE~\cite{llm-pee-2025} for schema decomposition. The use of embedding distance for type discrimination has parallels in metric learning \citep{snell2017prototypical}. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\%$) is consistent with standards for individual-difference predictors in behavioral research \citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \citep{lakens-2013-effect-size}.
13	
14	\paragraph{Embedding anisotropy.}
15	Our centrality confound (\S\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \cite{cai-isotropy-clusters-2021}, explaining why MAVEN's single-ontology types conflate confusability with centrality.
16	
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-18T07:12:29.935234+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "offset": "12",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "offset": "12",
    "limit": "8"
  }
}
```

</details>

---


### Tool result

_source line 981 · 2026-05-18T07:12:29.986019+00:00_

12	
13	\paragraph{Practical implications.}
14	The bounded count$\times$confusability interaction (0.47\,pp, TOST $p = 0.003$) implies no confusability amplification at scale. For RE, upper-SCS-quartile type pairs show 3--5\,pp accuracy differences; for NER, count reduction is the primary lever.
15	
16	\section{Conclusion}
17	\label{sec:conclusion}
18	
19	Schema-associated degradation in training-free LLM extraction operates along two dimensions (count-related recall decline, confusability-related type substitution) with bounded association in RE but coupling in NER. Count-related decline replicates across model scales (8B--70B) and architecture families including Gemini 2.5 Flash; confusability effects are verified on open-weight models and are structural rather than a prompting deficit (+4.3\,pp penalty under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE); BCS enables pre-hoc RE screening but not NER. Our findings characterize the training-free regime; fine-tuned models may learn type boundaries that mitigate confusability effects, though count-related decline likely persists as a schema-structural constraint. Future work should pursue interventional SCS validation, extend confusability analysis to generative IE formats, and develop merge-aware partitioning algorithms. More broadly, the two-dimensional framework may generalize to any task where LLMs discriminate among a prompt-specified label inventory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-18T07:14:16.355984+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 审稿意见\n\n---\n\n### Weaknesses 逐条回应\n\n---\n\n**[AGREE] R2-W1: 核心新颖性不足，confusability 维度效应量过小**\n\n同意这是论文面临的最大挑战，但需要区分两个层次：\n\n（1）**Pairwise r²=1.3-1.7% 确实很小**，R2 的批评合理。论文用 behavioral science 类比（Cohen 1988）来辩护，但这种跨学科类比在 NLP 语境下说服力有限（我在 R1-W4 中也指出了这一点）。\n\n（2）**但 batch-level R²=0.22-0.53 是实质性的**。R2 的描述侧重 pairwise r²，未充分区分 pair-level 和 batch-level 的差异。论文的核心证据不是 pairwise r²=1.3%，而是 batch-level R²=0.218（FewRel, §5.3 practical magnitude）和 R²=0.525（DocRED, §5.3 document-level RE）。一个 predictor 解释 22-53% 的 cross-batch variance 是有实际意义的。R2 聚焦 extreme-batch gap（-31.2pp）来批评\"人为构造\"是对的，但论文自己在 §5.3 已经给出了 typical-batch magnitude（2.2pp, quartile gap 3.9-5.3pp），这种区分是诚实的。\n\n（3）**NER batch-level null 和 MAVEN centrality confound 确实严重缩窄了 claim scope**——这与我的 R1-N1 一致。三个 task 中只有 RE 给出强 batch-level signal，论文标题的泛化暗示过强。\n\n总体判断：R2 的批评方向正确，但部分论证过度（忽视了 batch-level R²）。效应量小不一定意味着贡献不足——问题在于 scope 过宽（我的 N1）而非 effect 本身。\n\n---\n\n**[REBUT] R2-W2: \"First controlled study\" claim 过度宣称**\n\nR2 的论证存在类比不精确：\n\n（1）**LLM-PEE 使用 embedding cosine similarity 做 partitioning，不是做 controlled analysis**。论文在 Related Work §2 \"SCS novelty\" 段明确承认：\"SCS shares its formal definition...with the partitioning criterion used in LLM-PEE.\" 但 LLM-PEE 的目标是工程优化（partition schema to improve extraction），没有固定 count 变化 confusability 的控制实验，也没有隔离两个维度的 factorial 分析。使用同一个 metric 做不同的事（engineering vs. controlled analysis）是合法的区分。\n\n（2）**PARSE 优化 schema definitions 并不等于隔离 confusability**。PARSE 的目标是让 definitions 更清晰以提升抽取质量，这是一个 end-to-end 的工程干预，没有控制 count 或量化 confusability 的独立贡献。\"隐含了 confusability 维度的操纵\" 是过度引申。\n\n（3）**Haystack-to-Needle 做 label space reduction**，其效果同时包含 count reduction 和 confusability reduction，正是论文批评的 \"conflation\" 问题（Introduction §1 第 6 行）。\n\n（4）R2 自己也承认 \"Controlled study 是 methodology contribution, 不是 finding contribution\"——那么这恰恰支持论文的 claim：prior work 做的是 engineering，本文做的是 controlled analysis。这两者的区分是成立的。\n\n**但我同意措辞可以更精确**：\"first controlled study that explicitly disentangles...\" 确实比 \"first controlled study isolating...\" 更准确，R2 的建议合理。\n\n---\n\n**[AGREE] R2-W3: 论文定位模糊，empirical analysis paper 的接收标准未充分满足**\n\n这是一个合理的结构性批评：\n\n（1）R2 对四个 findings 的分类准确：Finding 1 是 confirmatory，Finding 2 效应小且 NER 无效，Finding 3 是 robustness check，Finding 4 是 negative result。作为 empirical analysis paper，论文需要回答 \"so what\"——理解问题比解决问题更重要的前提是理解本身带来 actionable insight。\n\n（2）**Discussion §7 practical implications 确实过薄**——仅两句话（\"For RE, upper-SCS-quartile type pairs show 3-5pp accuracy differences; for NER, count reduction is the primary lever\"）。对于一篇 analysis paper，应该提供更具体的 schema design guidelines：什么 BCS 阈值下需要注意？如何在 schema 设计阶段使用 SCS 筛选？这些内容完全可以从现有数据推导。\n\n（3）但我不同意 \"Finding 2 领域知识就能预测到\" 的说法。直觉上 \"similar types are harder to distinguish\" 是 trivially true，但（a）效应量有多大？（b）pair-level 如何传导到 batch-level？（c）NER 为什么不 work？这些都不是 \"领域知识\" 能回答的。科学研究的价值不仅在于发现 unexpected 的东西，也在于量化 expected 的东西。\n\n---\n\n**[AGREE] R2-W4: Abstract 过度压缩**\n\n完全同意。Abstract 在约 180 words 内塞入了 SCS、BCS、SDGD 三个缩写和至少 8 个数值（-49pp, 2.2pp, 22-53%, r≈0, +4.3pp, 8B, 70B 等），加上嵌套括号注释（\"confusability operates at the pair level across tasks but aggregates to batch-level predictive power only in RE\"），信息密度超过了 abstract 应有的可读性水平。按照 paper-writing norms §2.1 的标准：\"最多引用 2-3 个关键数字，要服务于 claim\"，当前 abstract 严重超标。\n\n---\n\n**[AGREE] R2-W5: Introduction findings 段统计量过密**\n\n同意。Introduction §1 的 findings (1)-(4) 包含了 TOST p-value、R² 精确值（0.22-0.53）、CI（[0.27, 0.73]）、n=35、+1.4pp p≈0.19 等大量统计细节。这些属于 Results/Methods，不属于 Introduction。Introduction 应传达 findings 的定性结论和方向，统计证据放在 Results 中即可。这在 ACL/EMNLP 的写作规范中是常见要求。\n\n---\n\n**[AGREE] R2-W6: Task asymmetry 削弱 generalizability claim**\n\n完全同意，这与我的 R1-N1 一致。论文的发现实质上是：\n- RE（constrained classification）: BCS batch-level 有效\n- NER（unconstrained generation）: BCS batch-level 无效\n- ED/MAVEN: centrality confound 导致 reversed sign\n\n这不是 \"across three tasks\" 的一致发现，而是 \"primarily an RE finding with a diagnostic explanation for why it doesn't work on NER\"。论文在 Discussion §7 和 Conclusion §8 确实提到了 \"RE-specific\" 和 \"format dependency\"，但 abstract 和 title 的 framing 没有充分反映这一限制。\n\n---\n\n**[AGREE] R2-W7: 缺少 label bias/label length bias 文献**\n\n部分同意。Label bias（模型对某些 label tokens 的 prior preference）确实可能是一个未被控制的 confound。如果某些 type names 恰好包含高频 tokens，模型可能偏向预测这些 types，而这种 bias 可能与 SCS（embedding similarity）相关。论文在 §5.2 讨论了 \"remaining variance\" 的来源（entity frequency, prompt position, mention ambiguity, definition quality），但没有提到 label token bias。不过，FewRel 的 constrained decoding（enum constraint）在一定程度上缓解了 label token bias（因为模型被强制从候选列表中选择），所以这个 confound 在 RE 实验中可能不是主要问题。NER 实验中更可能受影响，但 NER batch-level 本身就是 null result。\n\n建议补充引用但不需要作为 major weakness。\n\n---\n\n**[AGREE] R2-W8: \"Notably\" 用法是 AI 写作标志**\n\n同意，results.tex:49 \"Notably, the independent MiniLM embedding yields a stronger...\" 中的 \"Notably\" 是 AI 写作的常见标志。按照 paper-writing norms §5.2：\"避免 'It is worth noting that...' / 'Notably, ...'——直接写要说的内容。\" 应改为直接陈述。\n\n这是一个 trivial fix，不影响评分。\n\n---\n\n**[AGREE] R2-W9: Task asymmetry 可能由 evaluation format 驱动**\n\n同意，且论文自己也在 Discussion §7 承认了这一点：\"RE's constrained decoding (enum constraint) channels all errors into type substitution, so batch confusability directly predicts accuracy; these effect sizes may represent upper bounds specific to the constrained-classification format.\" 这与我的 R1 review 中 Q2 的问题一致：constrained decoding 是否人为放大了 BCS 的 apparent effect。\n\n如果 BCS 的预测力本质上是 \"在 closed-set forced choice 中，语义相似的选项更容易被混淆\"，那么这更接近一个已知的心理学/认知科学结论的 LLM 验证，而非新发现。\n\n---\n\n### Questions 逐条回应\n\n---\n\n**[AGREE] R2-Q1: BCS 在 RE 上的高 R² 是否由 constrained decoding 人为放大？**\n\n完全同意这是关键问题。Constrained decoding 将所有 non-none errors 强制导向 intra-batch substitution，这意味着 BCS 的预测对象（type confusion）本身被实验设计放大了。如果使用 unconstrained decoding，模型可能产生不在候选列表中的 type，那么 BCS 的解释力可能大幅下降。论文需要在 unconstrained decoding 条件下复制 BCS 实验以验证 robustness。这也是我在 R1 review 中 Q2 提出的问题。\n\n---\n\n**[REBUT] R2-Q2: FewRel train+val 合并是否改变了 val-origin types 的\"熟悉度\"特征？**\n\n论文在 Appendix §A9（Split-Origin Covariate Analysis）已经直接回答了这个问题。核心证据：\n- BCS partial effect 在控制 train-origin ratio 后不变（β_BCS = -0.416 vs -0.412 without covariate）\n- Train-origin ratio 本身不显著（β_origin = -0.057, p=0.245, ΔR²=0.005）\n- Train-origin 和 val-origin types 的 SCS 分布无显著差异（Mann-Whitney p=0.754, Cohen's d=0.081）\n\n这些分析已经充分控制了\"熟悉度\"差异对 BCS-accuracy 关系的可能影响。R2 的问题合理但已被论文回答。\n\n---\n\n**[AGREE] R2-Q3: NER 的 U-shape rebound 为什么 RE 没有类似现象？**\n\n合理问题。论文的 post-hoc 解释（Discussion §7：\"partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers\"）缺乏直接验证。我在 R1-W6 中也指出了这一点。RE 没有 U-shape 因为 RE 是 closed-set classification（不存在 \"type-filtering overhead\"），这个解释方向合理但属于 hypothesis。\n\n---\n\n**[AGREE] R2-Q4: 1-shot 在 high-BCS 上 +5.6pp，5-shot 反而降回，是否是 prompt length artifact？**\n\n同意，论文自己也引用了 lost-in-middle（Appendix §A13 最后一段），但只是作为一句附带提及。三个 data points（0/1/5-shot）不足以区分 confusability-specific 效应和 prompt length artifact。我在 R1-W5 中指出了相同问题。\n\n---\n\n### Missing References 逐条回应\n\n---\n\n**[AGREE] Fei et al. \"Quantifying and Mitigating Label Bias in LLMs\" (NAACL 2024)**\n\n部分同意。Label bias 是一个潜在 confound，如果 LLM 对某些 label tokens 有 prior preference，这可能与 embedding similarity 相关（高频词的 embeddings 往往更接近 cluster center）。但 constrained decoding 部分缓解了这个问题。建议在 Related Work 中提及但非 critical gap。\n\n---\n\n**[REBUT] \"Mitigating Label Length Bias in Large Language Models\" (2025)**\n\nLabel length bias 在本文设置中的影响有限：（1）RE 使用 constrained decoding + enum constraint，模型被强制选择一个 relation type，label length 不影响生成概率；（2）NER batch-level 本身是 null result；（3）SCS 基于 embedding similarity，不直接受 label length 影响。可以作为 minor addition 但不应被视为 major gap。\n\n---\n\n**[AGREE] Zhao et al. \"Label-Guided In-Context Learning for NER\" (2025)**\n\n与论文的 few-shot 实验（Appendix §A13）相关。论文发现 few-shot 无法缓解 confusability gap，而 label-guided ICL 可能提供一种 alternative in-context approach。建议在 Related Work 或 Discussion future directions 中提及。\n\n---\n\n### 对 R2 Overall Assessment（3.0 Findings）的回应\n\nR2 给出 3.0（Findings track），我给出 3.5（Borderline Conference）。差异主要在对两个问题的判断：\n\n**我认为 R2 过度低估了负面结果的价值**。SDGD 的系统性失败诊断（merge amplification + routing failure）对 decompose-then-merge paradigm 有广泛的 cautionary implication，ARR reviewer guidelines 也明确强调 negative results 应获得公平评价。Finding 4 不仅是 \"negative result\"，还有 diagnostic depth（precision collapse 的机制分析、oracle routing 的 headroom quantification）。\n\n**但我同意 R2 对 excitement 的评价（2.5/5）**。论文缺乏 actionable takeaway：知道 BCS 预测 RE accuracy variance 之后能做什么？SDGD 失败了，practical implications 仅两句话。一篇 analysis paper 如果不能 bridge understanding to action，其影响力确实有限。\n\n**综合判断**：我维持 3.5 而非下调至 3.0，因为方法学质量和 robustness 检验的深度值得认可，且 NLP 社区需要更多这样的 controlled empirical work（即使结果不 exciting）。但如果作者不能解决 scope 问题（R1-N1/R2-W6）和 practical implications 的薄弱（R2-W3），3.0 也是合理的评分。\n",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 审稿意见\n\n---\n\n### Weaknesses 逐条回应\n\n---\n\n**[AGREE] R2-W1: 核心新颖性不足，confusability 维度效应量过小**\n\n同意这是论文面临的最大挑战，但需要区分两个层次：\n\n（1）**Pairwise r²=1.3-1.7% 确实很小**，R2 的批评合理。论文用 behavioral science 类比（Cohen 1988）来辩护，但这种跨学科类比在 NLP 语境下说服力有限（我在 R1-W4 中也指出了这一点）。\n\n（2）**但 batch-level R²=0.22-0.53 是实质性的**。R2 的描述侧重 pairwise r²，未充分区分 pair-level 和 batch-level 的差异。论文的核心证据不是 pairwise r²=1.3%，而是 batch-level R²=0.218（FewRel, §5.3 practical magnitude）和 R²=0.525（DocRED, §5.3 document-level RE）。一个 predictor 解释 22-53% 的 cross-batch variance 是有实际意义的。R2 聚焦 extreme-batch gap（-31.2pp）来批评\"人为构造\"是对的，但论文自己在 §5.3 已经给出了 typical-batch magnitude（2.2pp, quartile gap 3.9-5.3pp），这种区分是诚实的。\n\n（3）**NER batch-level null 和 MAVEN centrality confound 确实严重缩窄了 claim scope**——这与我的 R1-N1 一致。三个 task 中只有 RE 给出强 batch-level signal，论文标题的泛化暗示过强。\n\n总体判断：R2 的批评方向正确，但部分论证过度（忽视了 batch-level R²）。效应量小不一定意味着贡献不足——问题在于 scope 过宽（我的 N1）而非 effect 本身。\n\n---\n\n**[REBUT] R2-W2: \"First controlled study\" claim 过度宣称**\n\nR2 的论证存在类比不精确：\n\n（1）**LLM-PEE 使用 embedding cosine similarity 做 partitioning，不是做 controlled analysis**。论文在 Related Work §2 \"SCS novelty\" 段明确承认：\"SCS shares its formal definition...with the partitioning criterion used in LLM-PEE.\" 但 LLM-PEE 的目标是工程优化（partition schema to improve extraction），没有固定 count 变化 confusability 的控制实验，也没有隔离两个维度的 factorial 分析。使用同一个 metric 做不同的事（engineering vs. controlled analysis）是合法的区分。\n\n（2）**PARSE 优化 schema definitions 并不等于隔离 confusability**。PARSE 的目标是让 definitions 更清晰以提升抽取质量，这是一个 end-to-end 的工程干预，没有控制 count 或量化 confusability 的独立贡献。\"隐含了 confusability 维度的操纵\" 是过度引申。\n\n（3）**Haystack-to-Needle 做 label space reduction**，其效果同时包含 count reduction 和 confusability reduction，正是论文批评的 \"conflation\" 问题（Introduction §1 第 6 行）。\n\n（4）R2 自己也承认 \"Controlled study 是 methodology contribution, 不是 finding contribution\"——那么这恰恰支持论文的 claim：prior work 做的是 engineering，本文做的是 controlled analysis。这两者的区分是成立的。\n\n**但我同意措辞可以更精确**：\"first controlled study that explicitly disentangles...\" 确实比 \"first controlled study isolating...\" 更准确，R2 的建议合理。\n\n---\n\n**[AGREE] R2-W3: 论文定位模糊，empirical analysis paper 的接收标准未充分满足**\n\n这是一个合理的结构性批评：\n\n（1）R2 对四个 findings 的分类准确：Finding 1 是 confirmatory，Finding 2 效应小且 NER 无效，Finding 3 是 robustness check，Finding 4 是 negative result。作为 empirical analysis paper，论文需要回答 \"so what\"——理解问题比解决问题更重要的前提是理解本身带来 actionable insight。\n\n（2）**Discussion §7 practical implications 确实过薄**——仅两句话（\"For RE, upper-SCS-quartile type pairs show 3-5pp accuracy differences; for NER, count reduction is the primary lever\"）。对于一篇 analysis paper，应该提供更具体的 schema design guidelines：什么 BCS 阈值下需要注意？如何在 schema 设计阶段使用 SCS 筛选？这些内容完全可以从现有数据推导。\n\n（3）但我不同意 \"Finding 2 领域知识就能预测到\" 的说法。直觉上 \"similar types are harder to distinguish\" 是 trivially true，但（a）效应量有多大？（b）pair-level 如何传导到 batch-level？（c）NER 为什么不 work？这些都不是 \"领域知识\" 能回答的。科学研究的价值不仅在于发现 unexpected 的东西，也在于量化 expected 的东西。\n\n---\n\n**[AGREE] R2-W4: Abstract 过度压缩**\n\n完全同意。Abstract 在约 180 words 内塞入了 SCS、BCS、SDGD 三个缩写和至少 8 个数值（-49pp, 2.2pp, 22-53%, r≈0, +4.3pp, 8B, 70B 等），加上嵌套括号注释（\"confusability operates at the pair level across tasks but aggregates to batch-level predictive power only in RE\"），信息密度超过了 abstract 应有的可读性水平。按照 paper-writing norms §2.1 的标准：\"最多引用 2-3 个关键数字，要服务于 claim\"，当前 abstract 严重超标。\n\n---\n\n**[AGREE] R2-W5: Introduction findings 段统计量过密**\n\n同意。Introduction §1 的 findings (1)-(4) 包含了 TOST p-value、R² 精确值（0.22-0.53）、CI（[0.27, 0.73]）、n=35、+1.4pp p≈0.19 等大量统计细节。这些属于 Results/Methods，不属于 Introduction。Introduction 应传达 findings 的定性结论和方向，统计证据放在 Results 中即可。这在 ACL/EMNLP 的写作规范中是常见要求。\n\n---\n\n**[AGREE] R2-W6: Task asymmetry 削弱 generalizability claim**\n\n完全同意，这与我的 R1-N1 一致。论文的发现实质上是：\n- RE（constrained classification）: BCS batch-level 有效\n- NER（unconstrained generation）: BCS batch-level 无效\n- ED/MAVEN: centrality confound 导致 reversed sign\n\n这不是 \"across three tasks\" 的一致发现，而是 \"primarily an RE finding with a diagnostic explanation for why it doesn't work on NER\"。论文在 Discussion §7 和 Conclusion §8 确实提到了 \"RE-specific\" 和 \"format dependency\"，但 abstract 和 title 的 framing 没有充分反映这一限制。\n\n---\n\n**[AGREE] R2-W7: 缺少 label bias/label length bias 文献**\n\n部分同意。Label bias（模型对某些 label tokens 的 prior preference）确实可能是一个未被控制的 confound。如果某些 type names 恰好包含高频 tokens，模型可能偏向预测这些 types，而这种 bias 可能与 SCS（embedding similarity）相关。论文在 §5.2 讨论了 \"remaining variance\" 的来源（entity frequency, prompt position, mention ambiguity, definition quality），但没有提到 label token bias。不过，FewRel 的 constrained decoding（enum constraint）在一定程度上缓解了 label token bias（因为模型被强制从候选列表中选择），所以这个 confound 在 RE 实验中可能不是主要问题。NER 实验中更可能受影响，但 NER batch-level 本身就是 null result。\n\n建议补充引用但不需要作为 major weakness。\n\n---\n\n**[AGREE] R2-W8: \"Notably\" 用法是 AI 写作标志**\n\n同意，results.tex:49 \"Notably, the independent MiniLM embedding yields a stronger...\" 中的 \"Notably\" 是 AI 写作的常见标志。按照 paper-writing norms §5.2：\"避免 'It is worth noting that...' / 'Notably, ...'——直接写要说的内容。\" 应改为直接陈述。\n\n这是一个 trivial fix，不影响评分。\n\n---\n\n**[AGREE] R2-W9: Task asymmetry 可能由 evaluation format 驱动**\n\n同意，且论文自己也在 Discussion §7 承认了这一点：\"RE's constrained decoding (enum constraint) channels all errors into type substitution, so batch confusability directly predicts accuracy; these effect sizes may represent upper bounds specific to the constrained-classification format.\" 这与我的 R1 review 中 Q2 的问题一致：constrained decoding 是否人为放大了 BCS 的 apparent effect。\n\n如果 BCS 的预测力本质上是 \"在 closed-set forced choice 中，语义相似的选项更容易被混淆\"，那么这更接近一个已知的心理学/认知科学结论的 LLM 验证，而非新发现。\n\n---\n\n### Questions 逐条回应\n\n---\n\n**[AGREE] R2-Q1: BCS 在 RE 上的高 R² 是否由 constrained decoding 人为放大？**\n\n完全同意这是关键问题。Constrained decoding 将所有 non-none errors 强制导向 intra-batch substitution，这意味着 BCS 的预测对象（type confusion）本身被实验设计放大了。如果使用 unconstrained decoding，模型可能产生不在候选列表中的 type，那么 BCS 的解释力可能大幅下降。论文需要在 unconstrained decoding 条件下复制 BCS 实验以验证 robustness。这也是我在 R1 review 中 Q2 提出的问题。\n\n---\n\n**[REBUT] R2-Q2: FewRel train+val 合并是否改变了 val-origin types 的\"熟悉度\"特征？**\n\n论文在 Appendix §A9（Split-Origin Covariate Analysis）已经直接回答了这个问题。核心证据：\n- BCS partial effect 在控制 train-origin ratio 后不变（β_BCS = -0.416 vs -0.412 without covariate）\n- Train-origin ratio 本身不显著（β_origin = -0.057, p=0.245, ΔR²=0.005）\n- Train-origin 和 val-origin types 的 SCS 分布无显著差异（Mann-Whitney p=0.754, Cohen's d=0.081）\n\n这些分析已经充分控制了\"熟悉度\"差异对 BCS-accuracy 关系的可能影响。R2 的问题合理但已被论文回答。\n\n---\n\n**[AGREE] R2-Q3: NER 的 U-shape rebound 为什么 RE 没有类似现象？**\n\n合理问题。论文的 post-hoc 解释（Discussion §7：\"partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers\"）缺乏直接验证。我在 R1-W6 中也指出了这一点。RE 没有 U-shape 因为 RE 是 closed-set classification（不存在 \"type-filtering overhead\"），这个解释方向合理但属于 hypothesis。\n\n---\n\n**[AGREE] R2-Q4: 1-shot 在 high-BCS 上 +5.6pp，5-shot 反而降回，是否是 prompt length artifact？**\n\n同意，论文自己也引用了 lost-in-middle（Appendix §A13 最后一段），但只是作为一句附带提及。三个 data points（0/1/5-shot）不足以区分 confusability-specific 效应和 prompt length artifact。我在 R1-W5 中指出了相同问题。\n\n---\n\n### Missing References 逐条回应\n\n---\n\n**[AGREE] Fei et al. \"Quantifying and Mitigating Label Bias in LLMs\" (NAACL 2024)**\n\n部分同意。Label bias 是一个潜在 confound，如果 LLM 对某些 label tokens 有 prior preference，这可能与 embedding similarity 相关（高频词的 embeddings 往往更接近 cluster center）。但 constrained decoding 部分缓解了这个问题。建议在 Related Work 中提及但非 critical gap。\n\n---\n\n**[REBUT] \"Mitigating Label Length Bias in Large Language Models\" (2025)**\n\nLabel length bias 在本文设置中的影响有限：（1）RE 使用 constrained decoding + enum constraint，模型被强制选择一个 relation type，label length 不影响生成概率；（2）NER batch-level 本身是 null result；（3）SCS 基于 embedding similarity，不直接受 label length 影响。可以作为 minor addition 但不应被视为 major gap。\n\n---\n\n**[AGREE] Zhao et al. \"Label-Guided In-Context Learning for NER\" (2025)**\n\n与论文的 few-shot 实验（Appendix §A13）相关。论文发现 few-shot 无法缓解 confusability gap，而 label-guided ICL 可能提供一种 alternative in-context approach。建议在 Related Work 或 Discussion future directions 中提及。\n\n---\n\n### 对 R2 Overall Assessment（3.0 Findings）的回应\n\nR2 给出 3.0（Findings track），我给出 3.5（Borderline Conference）。差异主要在对两个问题的判断：\n\n**我认为 R2 过度低估了负面结果的价值**。SDGD 的系统性失败诊断（merge amplification + routing failure）对 decompose-then-merge paradigm 有广泛的 cautionary implication，ARR reviewer guidelines 也明确强调 negative results 应获得公平评价。Finding 4 不仅是 \"negative result\"，还有 diagnostic depth（precision collapse 的机制分析、oracle routing 的 headroom quantification）。\n\n**但我同意 R2 对 excitement 的评价（2.5/5）**。论文缺乏 actionable takeaway：知道 BCS 预测 RE accuracy variance 之后能做什么？SDGD 失败了，practical implications 仅两句话。一篇 analysis paper 如果不能 bridge understanding to action，其影响力确实有限。\n\n**综合判断**：我维持 3.5 而非下调至 3.0，因为方法学质量和 robustness 检验的深度值得认可，且 NLP 社区需要更多这样的 controlled empirical work（即使结果不 exciting）。但如果作者不能解决 scope 问题（R1-N1/R2-W6）和 practical implications 的薄弱（R2-W3），3.0 也是合理的评分。\n",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 983 · 2026-05-18T07:14:20.829201+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4473
}
```

</details>

---


### Assistant

_source line 984 · 2026-05-18T07:14:28.684749+00:00_

交叉回应已提交。总结：

- **W1-W9 中 7 条 AGREE，1 条 REBUT（W2），1 条部分 AGREE**
- **Q1-Q4 中 3 条 AGREE，1 条 REBUT（Q2，论文 Appendix §A9 已回答）**
- **Missing References 中 2 条 AGREE，1 条 REBUT（label length bias 在 constrained decoding 下影响有限）**

核心共识：R2 和我在 scope 过宽（task asymmetry）、practical implications 不足、abstract/intro 信息密度过高这三个问题上完全一致。主要分歧在于：我认为 R2 对 "first controlled study" claim 的批评过度（LLM-PEE 做 engineering 和本文做 controlled analysis 是合法区分），且过度低估了 batch-level R²=0.22-0.53 和 negative results 的独立价值。我维持 3.5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 34

## Round 34

46 recorded events


### User

_source line 985 · 2026-05-18T08:15:25.237326+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）

### Venue 信息
- **目标**: EMNLP 2026（ARR May 2026 cycle）
- **Deadline**: 2026-05-25
- **格式**: Long paper, 8 页正文 + 无限参考文献, ACL style template (`\usepackage[review]{acl}`)
- **匿名**: Double-blind
- **附录**: 允许，参与审稿
- **评分标准**: 5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit

### 论文路径
`projects/schema-dag-extraction/docs/paper/main.tex`（含 \input 的各章节 .tex 文件）

### 你的审查侧重
**方法严谨性 + 实验设计**。重点审查：

1. **统计方法合理性**: SCS/BCS 定义、TOST 等价检验的 margin 选择（±3pp vs main effect 2.2pp）、logit-scale 分析、bootstrap CI 方法
2. **实验控制设计**: BCS-controlled 实验的内部效度、within-pool 控制的充分性、cross-model 验证的覆盖度
3. **效应量与实际意义**: pairwise r²=1.3-1.7% 的解释、batch-level R²=0.22-0.53 的可靠性、typical-batch 2.2pp gap 的实际部署意义
4. **因果推断边界**: 论文声称从 correlational 到 quasi-experimental 的推断链条是否清晰、语言是否过强
5. **Negative result 完整性**: SDGD 失败的诊断是否充分、替代方案讨论是否合理
6. **数据污染论证**: FewRel (2018) 预训练污染的排除论证是否充分
7. **Constrained decoding 对 BCS-accuracy 关系的影响**: enum constraint 是否人为放大了 RE 的 confusability 效应

### 历史审稿 Open Issues（供参考，需检查是否已修复）

**Critical**:
- R16-N1: Scope 过宽 — title/abstract 暗示跨任务泛化, 但 BCS batch-level 预测力仅限 RE
- R16-N2: TOST ±3pp margin > typical main effect 2.2pp, 'bounded association' claim 削弱; logit-scale inconclusive
- R16-N3: 效应量报告 framing 偏误 — extreme-batch gaps 前置, typical 2.2pp 后置

**Warning**:
- R16-W1: SCS 缺乏与简单 baseline metrics 对比（string overlap, ontological distance, same-parent category）
- R16-W6: 16-relation BCS-controlled 条件仅 single extreme batch, 无 CI
- R16-W7: Pairwise r²=1.3-1.7% 的 'small but real' 论证依赖跨学科类比
- R16-W8: Constrained decoding 可能人为放大 BCS 的 RE 效应

**Info**:
- R16-m1: Few-shot 'confusability gap widens' 结论过强
- R16-m5: FewRel 数据污染论证合理但非决定性

请按 ARR 审稿标准出具完整审稿报告，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment（含评分和置信度）/ Detailed Comments。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 986 · 2026-05-18T08:15:35.686968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-18T08:15:35.737942+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-18T08:15:39.582301+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-18T08:15:39.632955+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-18T08:15:43.170209+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-18T08:15:43.221365+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 992 · 2026-05-18T08:15:52.875013+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 993 · 2026-05-18T08:15:53.328229+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 (count-associated decline) has been validated on a proprietary model (Gemini 2.5 Flash, $\rho = -0.900$, $p = 0.037$; Appendix~\ref{sec:appendix_cross_model_gemini}); Dimension~2 (confusability-associated type substitution) has been verified only on open-weight models. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). A FewRel factorial with TOST equivalence testing is consistent with bounded association under the primary linear specification ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp); however, the logit-scale TOST is inconclusive ($p = 0.209$). At $n =
…[truncated 50034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-18T08:15:55.185819+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-18T08:15:55.537547+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-18T08:16:01.220952+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-18T08:16:01.279713+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 58
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-18T08:16:04.815644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-18T08:16:05.268122+00:00_

1	\begin{abstract}
2	As large language models are increasingly deployed for information extraction without task-specific training, understanding how schema design affects extraction quality becomes critical for reliable deployment. Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). To our knowledge, we present the first controlled study isolating these factors across NER, RE, and event detection on four datasets and quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation (BCS). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp, document-level RE at full schema) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); BCS explains 22--53\% of cross-batch RE accuracy variance but not NER, where boundary detection failures overwhelm the signal. Confusability operates at the pair level across all three tasks but aggregates to batch-level predictive power only in RE. Few-shot demonstrations do not reduce the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Count-related decline (Dimension~1) replicates across model scales (8B to 70B) and architecture families including Gemini 2.5 Flash; confusability effects (Dimension~2) are verified on open-weight models (Qwen, LLaMA), identifying confusability as a schema-structural constraint on training-free extraction.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-18T08:16:05.319702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-18T08:16:05.872539+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
…[truncated 3228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-18T08:16:05.873001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-18T08:16:05.873287+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting 
…[truncated 3156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1004 · 2026-05-18T08:16:06.174707+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-18T08:16:06.677675+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate th
…[truncated 8151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-18T08:16:06.678079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-18T08:16:07.079946+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\pm 1$\,SD across 3 seeds (42, 123, 456) $\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}); schema configura
…[truncated 10972 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-18T08:16:07.080331+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-18T08:16:08.033599+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapse (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation thus recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation \citep{jagannatha2020calibrating} to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\resi
…[truncated 533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-18T08:16:08.184513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-18T08:16:08.536173+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED slope $-$0.71, adjusted $R^2 = 0.51$, 95\% CI [0.27, 0.73]) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%); conditional on nonzero confusion (${\sim}11\%$ of pairs), $R^2$ rises to 7\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\% (Monte Carlo simulation, Appendix~\ref{app:aggregation-sim}), consistent with observed RE values.
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific ($R^2 = 0.22$--$0.53$ vs.\ $r \approx 0$ for NER, $n = 450$). Because RE uses constrained decoding that channels all errors into type substitution \cite{tam-2024-let-me-speak}, batch confusability directly predicts accuracy; these effect sizes likely represent upper bounds, and confusability effects may be weaker under unconstrained generation. NER's unconstrained generation scatters errors across missed entities (43--65\%), boundary misalignment, and hallucinated types, diluting the signal. We hypothesize the NER U-shape (\S\ref{sec:count_curves}) reflects a dual-task burden: partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers.
12	
13	\paragraph{Practical implications.}
14	The bounded count$\times$confusability interaction (0.47\,pp, TOST $p = 0.003$) implies no confusability amplification at scale. For 
…[truncated 967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-18T08:16:08.536529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-18T08:16:08.938894+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{lla
…[truncated 4608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-18T08:16:08.939287+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines"
  }
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-18T08:16:16.219903+00:00_

Web search results for query: "ACL ARR review form criteria 2025 2026 reviewer guidelines"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I found comprehensive information about ACL ARR review form criteria and reviewer guidelines for 2025-2026. Here are the key findings:

## Review Scoring Criteria (Febr
…[truncated 1532 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7280
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-18T08:16:22.459962+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (numeric range), and descriptions of each score level. Also extract any guidelines about what constitutes a good review, required sections, and evaluation criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (numeric range), and descriptions of each score level. Also extract any guidelines about what constitutes a good review, required sections, and evaluation criteria."
  }
}
```

</details>

---


### Tool call

_source line 1017 · 2026-05-18T08:16:23.516469+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, how to score papers, what constitutes good/bad reviews, criteria for soundness, excitement, and overall assessment. Include all scoring rubrics and their descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, how to score papers, what constitutes good/bad reviews, criteria for soundness, excitement, and overall assessment. Include all scoring rubrics and their descriptions."
  }
}
```

</details>

---


### Tool result

_source line 1018 · 2026-05-18T08:16:30.139599+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Core Scoring Dimensions

### 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

### 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

### 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

### 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Accept to Findings
- **2**: Resubmit next cycle with substantial revisions
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

### 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be able to reproduce the resul
…[truncated 820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7679
}
```

</details>

---


### Tool result

_source line 1019 · 2026-05-18T08:16:35.765290+00:00_

# ARR Reviewer Guidelines: Evaluation Criteria and Scoring

## Core Evaluation Dimensions

ARR uses three scoring categories:

**Soundness**: Technical correctness and validity of the work. Per guidelines: "low soundness scores must be justified by the text of the review." If you assign a low soundness rating without identifying major flaws, your review lacks coherence.

**Excitement**: Personal interest in the research topic. This subjective dimension is separate from soundness assessment and reflects individual preferences rather than objective quality judgments.

**Overall Assessment**: A composite recommendation for paper outcomes at *ACL venues, integrating soundness, excitement, novelty, and potential impact considerations.

## What Reviewers Should Evaluate

### Technical Soundness
- Validity of methodology and experimental design
- Correctness of formal proofs or theoretical claims
- Appropriateness of statistical analyses and significance testing
- Reproducibility: sufficient detail for others to replicate results

### Contribution Quality
- Clarity of research questions and knowledge gaps addressed
- Novelty relative to prior published work (3+ months before deadline)
- Scope appropriateness to CFP requirements
- Impact potential for the field

### Presentation Standards
- Clarity of writing and technical exposition
- Proper citation of related work
- Appropriate acknowledgment of limitations
- Professional, neutral tone in reviews

## Characteristics of Strong Reviews

**Specificity (I1)**: Avoid vague critiques. Replace "missing relevant references" with "missing XYZ citations." Specify line numbers and exact issues rather than general complaints.

**Professional Tone (I4)**: Reviews must be constructive and kind. Sarcastic or insulting language damages the peer review system and contributes to academic stress without advancing scientific discourse.

**Score Alignment (I3)**: Numerical ratings must correspond to review content. Unexplained low scores sig
…[truncated 2156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 12248
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-18T08:16:44.064953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-18T08:16:44.216237+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-18T08:16:44.216766+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-18T08:16:44.269050+00:00_

1	% DEPRECATED — this file is no longer included in main.tex.
2	% The active conclusion is in discussion.tex (\input{discussion}).
3	% Kept for reference only; safe to delete.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-18T08:18:19.261242+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1025 · 2026-05-18T08:19:28.380590+00:00_

&lt;persisted-output>
Output too large (53.3KB). Full output saved to: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/b0817902-f7a7-4bf1-843f-83defa8d6e0d/tool-results/toolu_0115GBaN2aVyEqYKz7MUv1JT.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 65, \"total_citations\": 91, \"unique_cited_keys\": 65, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 51, \"online_not_found\": 4, \"online_mismatch\": 10}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"tam-2024-let-me-speak\", \"type\": \"inproceedings\", \"title\": \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\", \"authors\": \"Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yin-2019-zero-shot-bench\", \"type\": \"inproceedings\", \"title\": \"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\", \"authors\": \"Yin, Wenpeng and Hay, Jamaal and Roth, Dan\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"schuirmann-1987-tost\", \"type\": \"article\", \"title\": \"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioava...\", \"authors\": \"Schuirmann, Donald J.\", \"year\": \"1987\", \"venue\": \"Journal of Pharmacokinetics and Biopharmaceutics\"}, {\"key\": \"gemini-2025\", \"type\": \"article\", \"title\": \"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\", \"authors\"
…[truncated 371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 69119
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-18T08:19:32.716319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/b0817902-f7a7-4bf1-843f-83defa8d6e0d/tool-results/toolu_0115GBaN2aVyEqYKz7MUv1JT.txt",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/b0817902-f7a7-4bf1-843f-83defa8d6e0d/tool-results/toolu_0115GBaN2aVyEqYKz7MUv1JT.txt",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-18T08:19:33.019404+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 65, \"total_citations\": 91, \"unique_cited_keys\": 65, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 51, \"online_not_found\": 4, \"online_mismatch\": 10}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"tam-2024-let-me-speak\", \"type\": \"inproceedings\", \"title\": \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\", \"authors\": \"Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yin-2019-zero-shot-bench\", \"type\": \"inproceedings\", \"title\": \"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\", \"authors\": \"Yin, Wenpeng and Hay, Jamaal and Roth, Dan\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"schuirmann-1987-tost\", \"type\": \"article\", \"title\": \"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioava...\", \"authors\": \"Schuirmann, Donald J.\", \"year\": \"1987\", \"venue\": \"Journal of Pharmacokinetics and Biopharmaceutics\"}, {\"key\": \"gemini-2025\", \"type\": \"article\", \"title\": \"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\", \"authors\": \"Comanici, Gheorghe and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2507.06261\"}, {\"key\": \"snell2017prototypical\", \"type\": \"inproceedings\", \"title\": \"Prototypical Networks for Few-shot Learning\", \"authors\": \"Snell, Jake and Swersky, Kevin and Zemel, Richard\", \"year\": \"2017\", \"venue\": \"Advances in 
…[truncated 52575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-18T08:22:23.355344+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — Round 1 审稿报告\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## Paper Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度如何影响抽取性能。作者将 schema 复杂度分解为两个维度：类型数量（count）和类型间语义混淆度（confusability），提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 量化后者。在 Few-NERD、FewRel、DocRED、MAVEN 四个数据集上，通过 count curve 和 BCS-controlled 两类实验，发现：(1) count 导致 recall 下降是主导因素；(2) BCS 可预测 RE 的 batch-level accuracy variance（R²=0.22–0.53）但对 NER 无效；(3) Schema 分解因 merge amplification（NER）和 routing failure（RE）而失败。cross-model 验证覆盖 8B–70B 及 Gemini 2.5 Flash。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n**一句话总结**: 实验设计严谨、统计方法成熟、负面结果报告诚实，但核心发现（BCS 预测力）局限于 RE 任务，scope claim 与实际证据存在张力，TOST 等价检验 margin 选择存在结构性问题。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 方法论总体扎实，TOST margin 和 logit-scale 问题坦诚报告但未解决；claim 语言偶尔偏强 |\n| **Excitement** | 3/5 | 分析视角新颖（controlled isolation of count vs. confusability），但 practical impact 受限于 negative decomposition result 和 modest effect sizes |\n| **Reproducibility** | 4/5 | 实验细节充分（prompt templates、seed、decoding params），代码承诺 release；唯一缺失是 batch 构造的具体算法伪代码 |\n| **Confidence** | 4/5 | 本人熟悉 LLM IE、统计方法论、zero-shot evaluation 相关工作 |\n\n---\n\n## Summary of Strengths\n\n**S1. 实验控制设计出色。** BCS-controlled 实验通过固定 count 变化 BCS，在 FewRel 的 balanced design 下消除了 type frequency confound。within-pool analysis（从 80-relation pool 采样 16-relation subsets）进一步控制了 pool composition confound，permutation test (p=0.60) 证实 slope 一致性。这种层层递进的控制设计在 NLP 实证研究中罕见。\n\n**S2. 统计方法论成熟。** TOST 等价检验、bootstrap CI、permutation test、cluster bootstrap、variance decomposition 等方法的运用在 NLP 论文中属于高水准。特别是 TOST sensitivity analysis（Table in Appendix §sec:appendix_factorial）提供了不同 margin 下的完整结果，使读者可以自行判断 equivalence 的稳健性。\n\n**S3. 负面结果报告诚实且有诊断价值。** SDGD 分解失败不仅报告了结果，还提供了 merge amplification 和 routing failure 的机制诊断。NER batch-level null result（r≈0, n=450）被坦诚报告而非隐藏。MAVEN centrality confound 的发现和处理（partial correlation 控制 log frequency + degree centrality）展示了科学严谨性。\n\n**S4. Cross-model 验证覆盖面广。** 从 8B (Llama-3.1-8B) 到 32B (Qwen3) 到 70B (Llama-3.1-70B-FP8) 到 proprietary (Gemini 2.5 Flash)，Dimension 1 在所有模型上复现。Dimension 2 在 open-weight 模型上验证。RE count curve 在 70B 上与 32B 几乎完全匹配（-30.7pp vs -30.1pp）。\n\n**S5. Robustness checks 全面。** Cross-prompt validation（4 种 prompt variants, Table in Appendix §sec:appendix_prompt_variants）、cross-seed variance decomposition（Table in Appendix app:variance-decomposition）、BCS aggregation sensitivity（mean vs max, Table in Appendix §sec:appendix_bcs_sensitivity）、SCS embedding ablation（name-only vs name+def, Table in Appendix app:scs-ablation）。每一项都增强了核心发现的可信度。\n\n---\n\n## Summary of Weaknesses (Must-Fix)\n\n**N1** [critical] **TOST ±3pp margin 超过 typical main effect 2.2pp，\"bounded association\" claim 的可信度受损**\n\n- 具体位置：§5.4 Multi-Dimensional Degradation; Appendix §sec:appendix_factorial (Table TOST sensitivity)\n- 问题：Typical-batch confusability gap 为 2.2pp (§5.3 Practical magnitude)。TOST 等价检验使用 ±3pp margin，超过主效应本身。Appendix TOST sensitivity table 显示：在 ±1pp margin 下等价检验 inconclusive (p=0.278)，即无法排除 interaction 达到主效应 ~50% 的可能性。logit-scale TOST 同样 inconclusive (p=0.209)。主文中使用 \"bounded association\" (§5.4) 和 \"bounded count×confusability interaction\" (§7 Discussion) 的措辞暗示 interaction 可以忽略，但实际上 ±1pp 等价检验的失败意味着 interaction 可能在实际上相当显著（相对于 2.2pp 主效应）。\n- 为什么影响接收：这是论文的一个核心 claim——两个维度近似可分。如果 interaction 可能达到主效应的 50%，则 \"bounded\" 的实际含义需要重新讨论。\n- 建议修改方向：(1) 在主文 §5.4 中明确报告 ±1pp 和 ±2pp 的 TOST 结果，而非仅在 Appendix 中展示；(2) 将 \"bounded association\" 改为更谨慎的措辞，如 \"the interaction is bounded below the ±3pp margin but may approach half the main effect magnitude\"；(3) 讨论 n=69 的 power 限制对 interaction 检测的影响。\n\n**N2** [critical] **Title/Abstract 的 scope 暗示跨任务通用性，但 BCS 的 batch-level 预测力仅限 RE**\n\n- 具体位置：Title \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"; Abstract line 1-2; §1 Introduction contributions\n- 问题：Title 使用 \"Information Extraction\"（通用）而非 \"Relation Extraction\"。BCS 在 batch-level 对 NER 无预测力（r≈0, n=450, §5.4），对 MAVEN ED 有 centrality confound（§5.5），仅在 RE（FewRel R²=0.22, DocRED R²=0.53）上有效。虽然 pairwise SCS 在三个任务上都显著，但 batch-level BCS 是论文的核心 metric——它才是可用于 schema design 的 practical tool。Abstract 确实提到 \"BCS explains 22-53% of cross-batch RE accuracy variance but not NER\"，但这个关键限定出现在 Abstract 中间，而 Title 仍暗示通用性。\n- 为什么影响接收：审稿人（和读者）会根据 title/abstract 判断 contribution scope。如果核心 metric 仅对一个任务类型有效，论文的 impact 评估会打折扣。\n- 建议修改方向：(1) Title 可改为更精确的表述，如 \"Schema Confusability Predicts Type Substitution in Training-Free LLM Relation Extraction: A Controlled Study\" 或保留当前 title 但在 Abstract 第一句就明确 task-specific 结论；(2) 在 Introduction 的 contribution 列表中将 task asymmetry 提升为核心贡献之一（目前是 contribution 3，位置偏后）。\n\n**N3** [critical] **Constrained decoding 对 BCS-accuracy 关系的影响未被充分 disentangle**\n\n- 具体位置：§7 Discussion \"Task-dependent effects and format dependency\"; Appendix §sec:appendix_prompts (RE prompt)\n- 问题：RE 使用 enum constraint 强制模型在候选 relation 中选择一个（包括 \"none\"）。在 closed-set classification 下，所有 non-none errors 都必然是 intra-batch type substitution，这在结构上保证了 BCS 与 error rate 的关联。论文 §7 承认 \"these effect sizes likely represent upper bounds\"，但这个承认远远不够——constrained decoding 不仅是 upper bound 的问题，它可能是 BCS-accuracy relationship 成立的必要条件。NER（无 enum constraint）的 batch-level null result (r≈0) 恰好与此一致：当 errors 可以散布到 missed entities、boundary errors、hallucinated types 时，BCS 失去预测力。\n- 为什么影响接收：如果 BCS 的 RE 预测力主要源于 constrained decoding 的 error channeling effect 而非 confusability 本身，则 SCS/BCS 作为 \"schema design metric\" 的价值受到质疑——它只在 enum classification 格式下有效。\n- 建议修改方向：(1) 增加一组 RE 实验：移除 enum constraint，使用 free-form generation，观察 BCS-accuracy 关系是否保持；(2) 如果无法增加实验，应在主文 §5.3 或 §7 中明确将 constrained decoding 列为 boundary condition，而非仅在 Discussion 中以 \"upper bound\" 一笔带过；(3) 讨论 NER 的 batch-level null 是否可以用同一逻辑解释（error channeling hypothesis）。\n\n---\n\n## Summary of Weaknesses (Should-Fix)\n\n**W1** [warning] **SCS 缺乏与简单 baseline metrics 的实证对比**\n\n- 具体位置：§4.2 SCS 定义; Limitations item 5; §3 Related Work \"SCS novelty\" paragraph\n- 问题：SCS 使用 embedding cosine similarity 量化类型混淆度。Limitations item 5 承认 \"whether simpler measures (e.g., string overlap, WordNet path distance) achieve comparable predictive power remains open\"。但这不应该是 open question——它应该在论文中被回答。如果 string overlap 或 same-parent category indicator 的预测力与 SCS 相当，则 SCS 的 contribution 会减弱（虽然不影响实验设计的贡献）。SCS embedding ablation (Appendix app:scs-ablation) 比较了 name-only vs. name+definition，但这只是 embedding input 变体，不是 metric 类型的对比。\n- 建议：增加 Table 对比 SCS、string edit distance、WordNet path distance、same-parent indicator 在 pairwise confusion prediction 上的 r 值。\n\n**W2** [warning] **FewRel 合并 train+val splits 的方法论影响未被充分讨论**\n\n- 具体位置：§4.1 Datasets \"FewRel\" paragraph\n- 问题：FewRel 原始设计中 train split (64 relations) 和 val split (16 relations) 是独立的。论文合并二者以获得 80 relations，但这些 relations 可能有不同的特征分布。Appendix app:split-origin 的 covariate analysis 显示 train-origin ratio 不显著 (p=0.245)，这在一定程度上缓解了 concern。但 held-out validation (Appendix app:scs-heldout-validation) 仅在 120 个 val-origin pairs 上验证了 SCS-confusion 关系（ρ=0.216），样本量较小。更重要的是，train-origin relations 的 accuracy 系统性低于 val-origin (-8.8pp, p=0.06)——虽然这与 contamination hypothesis 相反，但 p=0.06 处于边界，且样本量不平衡 (64 vs 16 types) 可能限制了检测力。\n- 建议：在主文中简要提及 split 合并的 rationale 和 covariate 结果，而非仅放在 Appendix 和 Limitations。\n\n**W3** [warning] **DocRED R²=0.53 基于 n=35 batches，CI 很宽**\n\n- 具体位置：§5.3 \"Document-level RE (DocRED)\"; Appendix app:bcs-controlled-table\n- 问题：DocRED count-16 的 R²=0.525 (adjusted 0.511) 基于 n=35 batches (5 high-BCS + 5 low-BCS + 25 random)。Fisher z CI: [0.27, 0.73]。这个 CI 跨度为 0.46，意味着真实解释力可能仅 27%，也可能高达 73%。主文中 \"BCS explains 22-53% of cross-batch RE accuracy variance\" 中的 53% 使用了点估计，但这个点估计的不确定性很大。\n- 建议：在主文中报告 DocRED R² 时附带 CI，或至少注明 n=35 的 sample size limitation。\n\n**W4** [warning] **Pair-to-batch aggregation simulation 是 post-hoc 的，参数来自同一数据**\n\n- 具体位置：Appendix app:aggregation-sim\n- 问题：Monte Carlo simulation 使用的 inter-pair SCS correlation (ρ=0.35) 和 conditional R²=0.074 都估计自同一 FewRel 实验数据。Appendix 正确标注其为 \"illustrative\" 且 \"the observed batch R²=0.218 is the primary evidence\"，但 §7 Discussion 中 \"Correlated aggregation amplifies this to batch-level R² of 18-25% (Monte Carlo simulation)\" 的表述可能让读者误以为这是独立验证。\n- 建议：在 §7 中加一句 \"the simulation uses parameters estimated from the same data and serves as a consistency check rather than independent evidence\"。\n\n**W5** [warning] **16-relation BCS-controlled 条件仅 single extreme batch, 无 CI**\n\n- 具体位置：Appendix Table app:bcs-controlled-table; §5.3\n- 问题：16-relation pilot condition 使用 n=1 extreme batch per BCS level。Table 中 CI 列为 \"---\"。虽然 80-relation condition 有完整 CI，但 16-relation 结果仍出现在主文 Figure 1b 和正文讨论中，缺乏不确定性量化可能误导读者。\n- 建议：在主文提及 16-relation 结果时注明 \"based on a single extreme batch; no CI available\"。\n\n**W6** [warning] **Few-shot 实验 \"confusability gap widens\" 的因果推断语言偏强**\n\n- 具体位置：Appendix §sec:appendix_fewshot_bcs; Abstract \"Few-shot demonstrations do not reduce the confusability gap (+4.3pp under 5-shot)\"\n- 问题：从 0-shot 到 5-shot，BCS gap 从 +18.5pp 增至 +22.8pp (bootstrap p=0.014)。但 low-BCS 的 non-monotonic pattern (0.682→0.754→0.715) 暗示 prompt length / lost-in-middle effect 可能是 confounding factor，而非 confusability 本身变得更严重。论文脚注提到 lost-in-middle，但 Abstract 和 Conclusion 中 \"+4.3pp under 5-shot\" 的表述暗示 confusability 是原因，而实际上 prompt length confound 同样可能解释这个 widening。\n- 建议：在 Abstract 或 Conclusion 中使用更谨慎的措辞，如 \"the gap does not narrow (and may widen) under 5-shot\"。\n\n---\n\n## Questions to Authors\n\n**Q1.** §5.3 Practical magnitude 报告 typical BCS gap 为 2.2pp (95% CI: [0.4, 4.0])。CI 下限接近零。如何解释这一点——在 IQR BCS span 下，confusability 的 practical significance 是否真的成立？\n\n**Q2.** NER 的 batch-level BCS null (r≈0, n=450) 是否可能是 evaluation metric confound（exact match 同时计入 boundary 和 type errors）导致？如果使用 relaxed matching（span overlap 即可），BCS-F1 correlation 是否可能恢复？\n\n**Q3.** RE 实验是否有移除 constrained decoding 的 ablation？如果在 free-form generation 下 BCS-accuracy 关系消失，论文的核心 claim 是否需要重新 scope？\n\n**Q4.** SCS 使用 MiniLM 或 Qwen3 embeddings。是否测试过使用 task-specific embeddings（如在 confusion matrix 上训练的 metric）？如果 SCS 的目的是 pre-hoc proxy，embedding 选择的 sensitivity 需要更多讨论。\n\n**Q5.** MAVEN centrality confound 在控制后 BCS-F1 correlation 消失 (p>0.2)。这是否意味着对于 same-domain schemas（现实中很常见，如 biomedical ontologies），BCS 完全不可用？论文的 practical implications 应如何适用于这类 schemas？\n\n---\n\n## Missing References\n\n引用覆盖总体充分（65 条引用，无虚假引用）。以下可考虑补充：\n\n- **Unconstrained vs. constrained decoding 对 IE 的影响**: 论文引用了 Tam et al. (2024) 和 JSON-Schema-Bench (2025)，但缺少直接比较 constrained vs. free-form decoding 对 classification accuracy 影响的实证工作。\n- **Label space reduction 相关**: Vandemoortele et al. (2025) 已引用，但 label embedding clustering 用于 schema simplification 的其他工作可能有遗漏。\n- **Effect size reporting in NLP**: 除 Dror et al. (2018) 外，可引用 Card et al. (2020) \"With Little Power Comes Great Responsibility\" 关于 NLP 实验中 effect size 和 power 分析的讨论。\n\n---\n\n## 小问题（不影响接收）\n\n- m1. Abstract 中 \"To our knowledge, we present the first controlled study\" 的 \"To our knowledge\" 修饰 \"present\" 语法不自然。建议改为 \"We present, to our knowledge, the first controlled study\" 或 \"This is, to our knowledge, the first controlled study\"。\n- m2. §4.1 FewRel paragraph: \"Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\" 这里 \"classify the relation\" 准确说应该是从 candidate set 中分类，可加 \"from the candidate set\"。\n- m3. Limitations item 3 (main.tex line 44): 这是全文最长的 limitation item，可读性差。建议拆分 TOST 讨论和 logit-scale 讨论为两个独立 items。\n- m4. Table cross-referencing: 正文 §5.3 提到 \"full data in Appendix Table\" 但有些引用不够 specific（如 \"Table~\\ref{tab:bcs_controlled}\" 在正文和附录中都有）。\n\n---\n\n## 主要优势总结\n\n1. **Controlled experimental design** 达到 NLP 实证研究的高标准，within-pool analysis 是亮点\n2. **统计方法论的成熟运用** 超越多数 NLP 论文——TOST、bootstrap、permutation test、variance decomposition 的组合使用\n3. **负面结果（SDGD 失败、NER null）的诚实报告** 有科学价值，诊断深入\n4. **Cross-model validation 覆盖面广**，从 8B 到 proprietary model\n5. **Centrality confound 的发现** 对 embedding-based schema analysis 有方法论贡献\n\n---\n\n## Limitations and Societal Impact\n\nLimitations 部分（9 条 + 1 段 multiple comparisons）非常详尽，属于我审过的 NLP 论文中最坦诚的 limitations 之一。每条都有量化数据支撑而非空泛声明。Societal impact 标记为 N/A 是合理的——这是纯分析研究。\n\n---\n\n## 最终评估\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5 |\n| Excitement | 3.0 |\n| Overall Assessment | **3.5** (Borderline Conference) |\n| Confidence | 4 |\n| Reproducibility | 4 |\n\n**升分条件**: 如果作者在 rebuttal 中 (1) 提供 unconstrained decoding 的 RE ablation 数据证明 BCS 关系不依赖 enum constraint，(2) 调整 TOST margin 讨论的 framing 使主文更透明，(3) 提供 SCS vs simple baselines 的对比数据，Overall 可升至 4.0 (Conference)。\n\n**降分风险**: 如果 unconstrained decoding 下 BCS-accuracy 关系消失，核心贡献会降级为 \"constrained decoding 下的 error channeling analysis\"，Overall 可能降至 3.0 (Findings)。\n\n---\n\n## 历史 Open Issues 追踪\n\n| Issue | Status | 评估 |\n|-------|--------|------|\n| R16-N1 (Scope 过宽) | **部分修复** | Abstract/Introduction 现在明确 NER null 和 task asymmetry，但 Title 仍暗示通用性。见 N2。 |\n| R16-N2 (TOST margin) | **部分修复** | 增加了 logit-scale analysis 和 sensitivity table，透明度提升，但结构性问题（margin > main effect）不变。见 N1。 |\n| R16-N3 (Effect size framing) | **已修复** | 2.2pp typical-batch figure 出现在 Abstract、Introduction、§5.3 dedicated paragraph。Extreme-batch results 有清晰标注。 |\n| R16-W1 (SCS vs simple baselines) | **未修复** | 仅在 Limitations 中承认为 open question。见 W1。 |\n| R16-W6 (16-rel single batch) | **已确认** | Table 中标注 \"---\" for CI，caption 解释原因。Limitation 已知但仍存在。见 W5。 |\n| R16-W7 (r²=1.3-1.7% framing) | **部分修复** | 增加了 aggregation simulation 和 BCS independence analysis (Appendix app:bcs-composition)。跨学科类比仍在使用但更加节制。 |\n| R16-W8 (Constrained decoding) | **部分修复** | §7 Discussion 现在明确承认 \"upper bound\"。但未提供 ablation 实验。见 N3。 |\n| R16-m1 (Few-shot conclusion) | **已修复** | 脚注解释了跨实验比较的不适当性，bootstrap p-value 提供了统计支撑。 |\n| R16-m5 (FewRel contamination) | **已修复** | Split-origin covariate analysis、held-out validation、DocRED replication 提供了充分的多角度论证。 |\n",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Round 1 审稿报告\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## Paper Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度如何影响抽取性能。作者将 schema 复杂度分解为两个维度：类型数量（count）和类型间语义混淆度（confusability），提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 量化后者。在 Few-NERD、FewRel、DocRED、MAVEN 四个数据集上，通过 count curve 和 BCS-controlled 两类实验，发现：(1) count 导致 recall 下降是主导因素；(2) BCS 可预测 RE 的 batch-level accuracy variance（R²=0.22–0.53）但对 NER 无效；(3) Schema 分解因 merge amplification（NER）和 routing failure（RE）而失败。cross-model 验证覆盖 8B–70B 及 Gemini 2.5 Flash。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n**一句话总结**: 实验设计严谨、统计方法成熟、负面结果报告诚实，但核心发现（BCS 预测力）局限于 RE 任务，scope claim 与实际证据存在张力，TOST 等价检验 margin 选择存在结构性问题。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 方法论总体扎实，TOST margin 和 logit-scale 问题坦诚报告但未解决；claim 语言偶尔偏强 |\n| **Excitement** | 3/5 | 分析视角新颖（controlled isolation of count vs. confusability），但 practical impact 受限于 negative decomposition result 和 modest effect sizes |\n| **Reproducibility** | 4/5 | 实验细节充分（prompt templates、seed、decoding params），代码承诺 release；唯一缺失是 batch 构造的具体算法伪代码 |\n| **Confidence** | 4/5 | 本人熟悉 LLM IE、统计方法论、zero-shot evaluation 相关工作 |\n\n---\n\n## Summary of Strengths\n\n**S1. 实验控制设计出色。** BCS-controlled 实验通过固定 count 变化 BCS，在 FewRel 的 balanced design 下消除了 type frequency confound。within-pool analysis（从 80-relation pool 采样 16-relation subsets）进一步控制了 pool composition confound，permutation test (p=0.60) 证实 slope 一致性。这种层层递进的控制设计在 NLP 实证研究中罕见。\n\n**S2. 统计方法论成熟。** TOST 等价检验、bootstrap CI、permutation test、cluster bootstrap、variance decomposition 等方法的运用在 NLP 论文中属于高水准。特别是 TOST sensitivity analysis（Table in Appendix §sec:appendix_factorial）提供了不同 margin 下的完整结果，使读者可以自行判断 equivalence 的稳健性。\n\n**S3. 负面结果报告诚实且有诊断价值。** SDGD 分解失败不仅报告了结果，还提供了 merge amplification 和 routing failure 的机制诊断。NER batch-level null result（r≈0, n=450）被坦诚报告而非隐藏。MAVEN centrality confound 的发现和处理（partial correlation 控制 log frequency + degree centrality）展示了科学严谨性。\n\n**S4. Cross-model 验证覆盖面广。** 从 8B (Llama-3.1-8B) 到 32B (Qwen3) 到 70B (Llama-3.1-70B-FP8) 到 proprietary (Gemini 2.5 Flash)，Dimension 1 在所有模型上复现。Dimension 2 在 open-weight 模型上验证。RE count curve 在 70B 上与 32B 几乎完全匹配（-30.7pp vs -30.1pp）。\n\n**S5. Robustness checks 全面。** Cross-prompt validation（4 种 prompt variants, Table in Appendix §sec:appendix_prompt_variants）、cross-seed variance decomposition（Table in Appendix app:variance-decomposition）、BCS aggregation sensitivity（mean vs max, Table in Appendix §sec:appendix_bcs_sensitivity）、SCS embedding ablation（name-only vs name+def, Table in Appendix app:scs-ablation）。每一项都增强了核心发现的可信度。\n\n---\n\n## Summary of Weaknesses (Must-Fix)\n\n**N1** [critical] **TOST ±3pp margin 超过 typical main effect 2.2pp，\"bounded association\" claim 的可信度受损**\n\n- 具体位置：§5.4 Multi-Dimensional Degradation; Appendix §sec:appendix_factorial (Table TOST sensitivity)\n- 问题：Typical-batch confusability gap 为 2.2pp (§5.3 Practical magnitude)。TOST 等价检验使用 ±3pp margin，超过主效应本身。Appendix TOST sensitivity table 显示：在 ±1pp margin 下等价检验 inconclusive (p=0.278)，即无法排除 interaction 达到主效应 ~50% 的可能性。logit-scale TOST 同样 inconclusive (p=0.209)。主文中使用 \"bounded association\" (§5.4) 和 \"bounded count×confusability interaction\" (§7 Discussion) 的措辞暗示 interaction 可以忽略，但实际上 ±1pp 等价检验的失败意味着 interaction 可能在实际上相当显著（相对于 2.2pp 主效应）。\n- 为什么影响接收：这是论文的一个核心 claim——两个维度近似可分。如果 interaction 可能达到主效应的 50%，则 \"bounded\" 的实际含义需要重新讨论。\n- 建议修改方向：(1) 在主文 §5.4 中明确报告 ±1pp 和 ±2pp 的 TOST 结果，而非仅在 Appendix 中展示；(2) 将 \"bounded association\" 改为更谨慎的措辞，如 \"the interaction is bounded below the ±3pp margin but may approach half the main effect magnitude\"；(3) 讨论 n=69 的 power 限制对 interaction 检测的影响。\n\n**N2** [critical] **Title/Abstract 的 scope 暗示跨任务通用性，但 BCS 的 batch-level 预测力仅限 RE**\n\n- 具体位置：Title \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"; Abstract line 1-2; §1 Introduction contributions\n- 问题：Title 使用 \"Information Extraction\"（通用）而非 \"Relation Extraction\"。BCS 在 batch-level 对 NER 无预测力（r≈0, n=450, §5.4），对 MAVEN ED 有 centrality confound（§5.5），仅在 RE（FewRel R²=0.22, DocRED R²=0.53）上有效。虽然 pairwise SCS 在三个任务上都显著，但 batch-level BCS 是论文的核心 metric——它才是可用于 schema design 的 practical tool。Abstract 确实提到 \"BCS explains 22-53% of cross-batch RE accuracy variance but not NER\"，但这个关键限定出现在 Abstract 中间，而 Title 仍暗示通用性。\n- 为什么影响接收：审稿人（和读者）会根据 title/abstract 判断 contribution scope。如果核心 metric 仅对一个任务类型有效，论文的 impact 评估会打折扣。\n- 建议修改方向：(1) Title 可改为更精确的表述，如 \"Schema Confusability Predicts Type Substitution in Training-Free LLM Relation Extraction: A Controlled Study\" 或保留当前 title 但在 Abstract 第一句就明确 task-specific 结论；(2) 在 Introduction 的 contribution 列表中将 task asymmetry 提升为核心贡献之一（目前是 contribution 3，位置偏后）。\n\n**N3** [critical] **Constrained decoding 对 BCS-accuracy 关系的影响未被充分 disentangle**\n\n- 具体位置：§7 Discussion \"Task-dependent effects and format dependency\"; Appendix §sec:appendix_prompts (RE prompt)\n- 问题：RE 使用 enum constraint 强制模型在候选 relation 中选择一个（包括 \"none\"）。在 closed-set classification 下，所有 non-none errors 都必然是 intra-batch type substitution，这在结构上保证了 BCS 与 error rate 的关联。论文 §7 承认 \"these effect sizes likely represent upper bounds\"，但这个承认远远不够——constrained decoding 不仅是 upper bound 的问题，它可能是 BCS-accuracy relationship 成立的必要条件。NER（无 enum constraint）的 batch-level null result (r≈0) 恰好与此一致：当 errors 可以散布到 missed entities、boundary errors、hallucinated types 时，BCS 失去预测力。\n- 为什么影响接收：如果 BCS 的 RE 预测力主要源于 constrained decoding 的 error channeling effect 而非 confusability 本身，则 SCS/BCS 作为 \"schema design metric\" 的价值受到质疑——它只在 enum classification 格式下有效。\n- 建议修改方向：(1) 增加一组 RE 实验：移除 enum constraint，使用 free-form generation，观察 BCS-accuracy 关系是否保持；(2) 如果无法增加实验，应在主文 §5.3 或 §7 中明确将 constrained decoding 列为 boundary condition，而非仅在 Discussion 中以 \"upper bound\" 一笔带过；(3) 讨论 NER 的 batch-level null 是否可以用同一逻辑解释（error channeling hypothesis）。\n\n---\n\n## Summary of Weaknesses (Should-Fix)\n\n**W1** [warning] **SCS 缺乏与简单 baseline metrics 的实证对比**\n\n- 具体位置：§4.2 SCS 定义; Limitations item 5; §3 Related Work \"SCS novelty\" paragraph\n- 问题：SCS 使用 embedding cosine similarity 量化类型混淆度。Limitations item 5 承认 \"whether simpler measures (e.g., string overlap, WordNet path distance) achieve comparable predictive power remains open\"。但这不应该是 open question——它应该在论文中被回答。如果 string overlap 或 same-parent category indicator 的预测力与 SCS 相当，则 SCS 的 contribution 会减弱（虽然不影响实验设计的贡献）。SCS embedding ablation (Appendix app:scs-ablation) 比较了 name-only vs. name+definition，但这只是 embedding input 变体，不是 metric 类型的对比。\n- 建议：增加 Table 对比 SCS、string edit distance、WordNet path distance、same-parent indicator 在 pairwise confusion prediction 上的 r 值。\n\n**W2** [warning] **FewRel 合并 train+val splits 的方法论影响未被充分讨论**\n\n- 具体位置：§4.1 Datasets \"FewRel\" paragraph\n- 问题：FewRel 原始设计中 train split (64 relations) 和 val split (16 relations) 是独立的。论文合并二者以获得 80 relations，但这些 relations 可能有不同的特征分布。Appendix app:split-origin 的 covariate analysis 显示 train-origin ratio 不显著 (p=0.245)，这在一定程度上缓解了 concern。但 held-out validation (Appendix app:scs-heldout-validation) 仅在 120 个 val-origin pairs 上验证了 SCS-confusion 关系（ρ=0.216），样本量较小。更重要的是，train-origin relations 的 accuracy 系统性低于 val-origin (-8.8pp, p=0.06)——虽然这与 contamination hypothesis 相反，但 p=0.06 处于边界，且样本量不平衡 (64 vs 16 types) 可能限制了检测力。\n- 建议：在主文中简要提及 split 合并的 rationale 和 covariate 结果，而非仅放在 Appendix 和 Limitations。\n\n**W3** [warning] **DocRED R²=0.53 基于 n=35 batches，CI 很宽**\n\n- 具体位置：§5.3 \"Document-level RE (DocRED)\"; Appendix app:bcs-controlled-table\n- 问题：DocRED count-16 的 R²=0.525 (adjusted 0.511) 基于 n=35 batches (5 high-BCS + 5 low-BCS + 25 random)。Fisher z CI: [0.27, 0.73]。这个 CI 跨度为 0.46，意味着真实解释力可能仅 27%，也可能高达 73%。主文中 \"BCS explains 22-53% of cross-batch RE accuracy variance\" 中的 53% 使用了点估计，但这个点估计的不确定性很大。\n- 建议：在主文中报告 DocRED R² 时附带 CI，或至少注明 n=35 的 sample size limitation。\n\n**W4** [warning] **Pair-to-batch aggregation simulation 是 post-hoc 的，参数来自同一数据**\n\n- 具体位置：Appendix app:aggregation-sim\n- 问题：Monte Carlo simulation 使用的 inter-pair SCS correlation (ρ=0.35) 和 conditional R²=0.074 都估计自同一 FewRel 实验数据。Appendix 正确标注其为 \"illustrative\" 且 \"the observed batch R²=0.218 is the primary evidence\"，但 §7 Discussion 中 \"Correlated aggregation amplifies this to batch-level R² of 18-25% (Monte Carlo simulation)\" 的表述可能让读者误以为这是独立验证。\n- 建议：在 §7 中加一句 \"the simulation uses parameters estimated from the same data and serves as a consistency check rather than independent evidence\"。\n\n**W5** [warning] **16-relation BCS-controlled 条件仅 single extreme batch, 无 CI**\n\n- 具体位置：Appendix Table app:bcs-controlled-table; §5.3\n- 问题：16-relation pilot condition 使用 n=1 extreme batch per BCS level。Table 中 CI 列为 \"---\"。虽然 80-relation condition 有完整 CI，但 16-relation 结果仍出现在主文 Figure 1b 和正文讨论中，缺乏不确定性量化可能误导读者。\n- 建议：在主文提及 16-relation 结果时注明 \"based on a single extreme batch; no CI available\"。\n\n**W6** [warning] **Few-shot 实验 \"confusability gap widens\" 的因果推断语言偏强**\n\n- 具体位置：Appendix §sec:appendix_fewshot_bcs; Abstract \"Few-shot demonstrations do not reduce the confusability gap (+4.3pp under 5-shot)\"\n- 问题：从 0-shot 到 5-shot，BCS gap 从 +18.5pp 增至 +22.8pp (bootstrap p=0.014)。但 low-BCS 的 non-monotonic pattern (0.682→0.754→0.715) 暗示 prompt length / lost-in-middle effect 可能是 confounding factor，而非 confusability 本身变得更严重。论文脚注提到 lost-in-middle，但 Abstract 和 Conclusion 中 \"+4.3pp under 5-shot\" 的表述暗示 confusability 是原因，而实际上 prompt length confound 同样可能解释这个 widening。\n- 建议：在 Abstract 或 Conclusion 中使用更谨慎的措辞，如 \"the gap does not narrow (and may widen) under 5-shot\"。\n\n---\n\n## Questions to Authors\n\n**Q1.** §5.3 Practical magnitude 报告 typical BCS gap 为 2.2pp (95% CI: [0.4, 4.0])。CI 下限接近零。如何解释这一点——在 IQR BCS span 下，confusability 的 practical significance 是否真的成立？\n\n**Q2.** NER 的 batch-level BCS null (r≈0, n=450) 是否可能是 evaluation metric confound（exact match 同时计入 boundary 和 type errors）导致？如果使用 relaxed matching（span overlap 即可），BCS-F1 correlation 是否可能恢复？\n\n**Q3.** RE 实验是否有移除 constrained decoding 的 ablation？如果在 free-form generation 下 BCS-accuracy 关系消失，论文的核心 claim 是否需要重新 scope？\n\n**Q4.** SCS 使用 MiniLM 或 Qwen3 embeddings。是否测试过使用 task-specific embeddings（如在 confusion matrix 上训练的 metric）？如果 SCS 的目的是 pre-hoc proxy，embedding 选择的 sensitivity 需要更多讨论。\n\n**Q5.** MAVEN centrality confound 在控制后 BCS-F1 correlation 消失 (p>0.2)。这是否意味着对于 same-domain schemas（现实中很常见，如 biomedical ontologies），BCS 完全不可用？论文的 practical implications 应如何适用于这类 schemas？\n\n---\n\n## Missing References\n\n引用覆盖总体充分（65 条引用，无虚假引用）。以下可考虑补充：\n\n- **Unconstrained vs. constrained decoding 对 IE 的影响**: 论文引用了 Tam et al. (2024) 和 JSON-Schema-Bench (2025)，但缺少直接比较 constrained vs. free-form decoding 对 classification accuracy 影响的实证工作。\n- **Label space reduction 相关**: Vandemoortele et al. (2025) 已引用，但 label embedding clustering 用于 schema simplification 的其他工作可能有遗漏。\n- **Effect size reporting in NLP**: 除 Dror et al. (2018) 外，可引用 Card et al. (2020) \"With Little Power Comes Great Responsibility\" 关于 NLP 实验中 effect size 和 power 分析的讨论。\n\n---\n\n## 小问题（不影响接收）\n\n- m1. Abstract 中 \"To our knowledge, we present the first controlled study\" 的 \"To our knowledge\" 修饰 \"present\" 语法不自然。建议改为 \"We present, to our knowledge, the first controlled study\" 或 \"This is, to our knowledge, the first controlled study\"。\n- m2. §4.1 FewRel paragraph: \"Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\" 这里 \"classify the relation\" 准确说应该是从 candidate set 中分类，可加 \"from the candidate set\"。\n- m3. Limitations item 3 (main.tex line 44): 这是全文最长的 limitation item，可读性差。建议拆分 TOST 讨论和 logit-scale 讨论为两个独立 items。\n- m4. Table cross-referencing: 正文 §5.3 提到 \"full data in Appendix Table\" 但有些引用不够 specific（如 \"Table~\\ref{tab:bcs_controlled}\" 在正文和附录中都有）。\n\n---\n\n## 主要优势总结\n\n1. **Controlled experimental design** 达到 NLP 实证研究的高标准，within-pool analysis 是亮点\n2. **统计方法论的成熟运用** 超越多数 NLP 论文——TOST、bootstrap、permutation test、variance decomposition 的组合使用\n3. **负面结果（SDGD 失败、NER null）的诚实报告** 有科学价值，诊断深入\n4. **Cross-model validation 覆盖面广**，从 8B 到 proprietary model\n5. **Centrality confound 的发现** 对 embedding-based schema analysis 有方法论贡献\n\n---\n\n## Limitations and Societal Impact\n\nLimitations 部分（9 条 + 1 段 multiple comparisons）非常详尽，属于我审过的 NLP 论文中最坦诚的 limitations 之一。每条都有量化数据支撑而非空泛声明。Societal impact 标记为 N/A 是合理的——这是纯分析研究。\n\n---\n\n## 最终评估\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5 |\n| Excitement | 3.0 |\n| Overall Assessment | **3.5** (Borderline Conference) |\n| Confidence | 4 |\n| Reproducibility | 4 |\n\n**升分条件**: 如果作者在 rebuttal 中 (1) 提供 unconstrained decoding 的 RE ablation 数据证明 BCS 关系不依赖 enum constraint，(2) 调整 TOST margin 讨论的 framing 使主文更透明，(3) 提供 SCS vs simple baselines 的对比数据，Overall 可升至 4.0 (Conference)。\n\n**降分风险**: 如果 unconstrained decoding 下 BCS-accuracy 关系消失，核心贡献会降级为 \"constrained decoding 下的 error channeling analysis\"，Overall 可能降至 3.0 (Findings)。\n\n---\n\n## 历史 Open Issues 追踪\n\n| Issue | Status | 评估 |\n|-------|--------|------|\n| R16-N1 (Scope 过宽) | **部分修复** | Abstract/Introduction 现在明确 NER null 和 task asymmetry，但 Title 仍暗示通用性。见 N2。 |\n| R16-N2 (TOST margin) | **部分修复** | 增加了 logit-scale analysis 和 sensitivity table，透明度提升，但结构性问题（margin > main effect）不变。见 N1。 |\n| R16-N3 (Effect size framing) | **已修复** | 2.2pp typical-batch figure 出现在 Abstract、Introduction、§5.3 dedicated paragraph。Extreme-batch results 有清晰标注。 |\n| R16-W1 (SCS vs simple baselines) | **未修复** | 仅在 Limitations 中承认为 open question。见 W1。 |\n| R16-W6 (16-rel single batch) | **已确认** | Table 中标注 \"---\" for CI，caption 解释原因。Limitation 已知但仍存在。见 W5。 |\n| R16-W7 (r²=1.3-1.7% framing) | **部分修复** | 增加了 aggregation simulation 和 BCS independence analysis (Appendix app:bcs-composition)。跨学科类比仍在使用但更加节制。 |\n| R16-W8 (Constrained decoding) | **部分修复** | §7 Discussion 现在明确承认 \"upper bound\"。但未提供 ablation 实验。见 N3。 |\n| R16-m1 (Few-shot conclusion) | **已修复** | 脚注解释了跨实验比较的不适当性，bootstrap p-value 提供了统计支撑。 |\n| R16-m5 (FewRel contamination) | **已修复** | Split-origin covariate analysis、held-out validation、DocRED replication 提供了充分的多角度论证。 |\n",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1029 · 2026-05-18T08:22:28.030713+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4675
}
```

</details>

---


### Assistant

_source line 1030 · 2026-05-18T08:22:38.485769+00:00_

审稿报告已提交给 Review Director。

核心评分：**Overall 3.5 (Borderline Conference)**，Soundness 3.5，Excitement 3.0。

提出了 3 个 Must-Fix 问题：
1. **TOST ±3pp margin 超过 typical main effect 2.2pp** — ±1pp 等价检验 inconclusive，"bounded association" 措辞偏强
2. **Scope claim 与 evidence 张力** — Title 暗示跨任务通用性，但 BCS batch-level 预测力仅限 RE
3. **Constrained decoding 未被 disentangle** — enum constraint 可能是 BCS-accuracy 关系成立的必要条件，缺 free-form generation ablation

6 个 Should-Fix：SCS 缺少简单 baseline 对比、FewRel train+val 合并讨论不足、DocRED R² 基于 n=35 CI 很宽、aggregation simulation 是 post-hoc、16-rel 单 batch 无 CI、few-shot "gap widens" 因果语言偏强。

升分条件：提供 unconstrained decoding ablation + 调整 TOST framing + SCS baseline 对比即可升至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 35

## Round 35

4 recorded events


### User

_source line 1031 · 2026-05-18T08:32:05.016325+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应 Reviewer 2 的每个 Must-Fix、Should-Fix 和 Question。对每条使用：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注你们评分的差异：你给 3.5 (Borderline Conference)，R2 给 3.0 (Findings)。请在回应结束后说明是否调整你的评分。

---

以下是 Reviewer 2 的完整审稿原文：

### Overall: 3.0 (Findings), Soundness 3.5, Excitement 2.5

### Must-Fix:

**N1** [critical] 标题/摘要 scope 与实际发现不匹配——BCS 预测力仅限 RE
- 标题问 "How Does Schema Complexity Predict Performance in Training-Free LLM IE"，暗示跨任务普适性。但 BCS 的批次级预测力仅在 RE 上成立（R²=0.22-0.53），NER 批次级相关 r≈0（n=150, §4.3-4.4），MAVEN 因 centrality confound 需单独处理（§4.5）。

**N2** [critical] SCS/BCS 指标新颖性不足——与 LLM-PEE 的 partitioning criterion 形式完全相同
- 论文自己承认 SCS 与 LLM-PEE metric 形式相同。Contribution 2 表述容易被读为指标层面新贡献。当核心度量没有 novelty 时，论文价值完全依赖实验设计的 rigor 和 findings 的 insight depth。

**N3** [critical] Practical implications 不足——"So what?" 问题未充分回答
- Discussion 实际建议仅两条：(1) RE 中 pre-screen 上五分位 SCS（3-5pp 收益）；(2) NER 中减少候选类型数（trivially known）。Schema decomposition 被证明失败。Empirical analysis paper 不能提供 actionable insights 其价值会被质疑。

### Should-Fix:

**W1** Abstract 信息密度过高——未定义缩写 + 数字堆砌（~195 words, 8+ 数值, BCS 未展开全称）

**W2** Introduction findings 段编号跳跃——(1) 直接跳到 (3)，(2) 缺失

**W3** "r = 0.1-1.7" 疑似笔误——Pearson r 范围 [-1, 1]，应为 "r = 0.11-0.19"

**W4** 补充材料标题与主文标题不一致——supplementary 仍用旧标题 "Schema-Induced Degradation"

**W5** "First controlled study" claim 仍有 overclaim 风险——LLM-PEE 也有 similarity-based 分组比较

**W6** TOST 逻辑刻度结果不确定——logit-scale p=0.209，论文仅放在 Appendix

### Minor:
- m1: 附录 3 处 -ing 分词短语结尾
- m2: Table 1 caption 星号注释不清晰
- m3: vLLM v0.20.2 版本号可能笔误
- m4: Contribution 3 "task asymmetry" 可能由 evaluation format 驱动
- m5: 4 条 bib entry 在 OpenAlex 未找到（索引问题非 fake）

### Questions:
1. BCS-accuracy 关系是否本质上是 constrained-decoding format 的产物？
2. Typical-batch gap 2.2pp 在实际部署中是否 meaningful？
3. Schema decomposition 方向本身不可行还是 routing 方法不够好？
4. SCS embedding 选择依赖先验知识，削弱 pre-hoc proxy 实用性？

### Missing References:
- Fei et al. 2024 (event extraction 评测)
- Gillick et al. 2014 (fine-grained entity typing)
- Levy et al. 2024 "Same Task, More Tokens" (已在 references 但正文未引用)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-18T08:33:40.400701+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见\n\n---\n\n## Must-Fix 逐条回应\n\n**[AGREE] R2-N1: 标题/摘要 scope 与实际发现不匹配**\n\n同意，这与我的 N2 完全一致。补充两点：\n\n1. R2 引用的 NER n=150 应为 n=450（§5.3 prompt sensitivity 段落和 Appendix §sec:appendix_prompt_sensitivity 明确报告 \"pooling across three seeds and all count levels (n=450)\"）。数据本身更强化了 null result 的可靠性——n=450 的 null 比 n=150 的 null 更有说服力，反而加重了 scope mismatch 的问题。\n2. 我想强调一个 R2 未提的细节：pairwise SCS 在三个任务上均显著（Few-NERD r=0.112, MAVEN r=0.129, FewRel r=0.187; Table 2），这是论文真正跨任务的发现。问题在于从 pairwise 到 batch-level 的 aggregation 仅在 RE 上成功。Title 如果修改为聚焦 \"pairwise confusability predicts type confusion across tasks; batch-level prediction is task-dependent\" 的叙事，scope 问题可以解决而不缩小实际贡献。\n\n**[REBUT] R2-N2: SCS/BCS 指标新颖性不足**\n\nR2 的批评有道理但过于严厉。论文 §3 Related Work \"SCS novelty\" 段落已经明确承认 \"SCS shares its formal definition with the partitioning criterion used in LLM-PEE\"，并将 contribution 定位在 \"controlled experimental framework\" 而非 metric 本身。关键区别：\n\n1. **LLM-PEE 用 embedding similarity 做工程（schema partitioning），本文用它做科学（controlled measurement）**。这是工具与理论的区别——温度计不是新发明，但用它做 controlled experiment 证明发烧与感染的 dose-response relationship 仍是科学贡献。\n2. Contribution 2 的原文是 \"We validate that pairwise embedding similarity predicts type confusion and show that weak pair-level signals (r=0.11-0.19) amplify to batch-level predictive power (R²=0.22-0.53) through correlated aggregation\"（§1 Introduction）。这里的 contribution 是 validation + aggregation mechanism，不是 metric 本身。\n3. 但我同意 R2 的隐含建议：Contribution 2 的措辞可以更清晰地与 LLM-PEE 区分，避免读者误读为 metric novelty claim。\n\n**[AGREE with qualification] R2-N3: Practical implications 不足**\n\n部分同意。R2 的 \"So what?\" 问题是合理的，但评估应区分两类贡献：\n\n1. **诊断贡献 vs. 解决方案贡献**。论文定位为诊断研究（§1 \"we conduct controlled analysis to understand why extraction degrades\"），而非提出解决方案。诊断的价值在于 (a) 解释为什么 LLM-PEE 等分解方法的 gain 有限（merge amplification 才是瓶颈而非 partitioning quality），(b) 为未来工作指明方向（coarse-to-fine pipelines, retrieval-based routing, calibrated generation; §6 SDGD \"Future directions\"）。\n2. **但 R2 对 practical advice 的批评是准确的**：NER 中 \"减少候选类型数\" 确实是 trivially known；RE 中 \"pre-screen 上四分位 SCS\" 的 3-5pp 收益在实际部署中边际效用有限。\n3. 我认为这不应是 \"critical\" 级别——ARR reviewer guidelines (H5) 明确指出不应要求 SOTA results 当论文 claim 的是不同类型的 contribution；(H6) 指出不应惩罚 negative results。论文的 SDGD 失败诊断本身有方法论价值。但如果 R2 认为 excitement 因此不足 (2.5)，这个主观评分是合理的。\n\n---\n\n## Should-Fix 逐条回应\n\n**[AGREE] R2-W1: Abstract 信息密度过高**\n\n同意。Abstract 约 195 words 包含 8+ 数值（-49pp, 2.2pp, 22-53%, +4.3pp 等）和未定义缩写（BCS 在 Abstract 中首次出现时未展开全称——仅有 \"its batch-level aggregation (BCS)\" 作为括号注释，但 SCS 和 BCS 的含义需要更多 context）。按照 ARR 标准，审稿人应在 30 秒内从 Abstract 判断论文价值——当前密度可能阻碍这一目标。\n\n**[REBUT] R2-W2: Introduction findings 段编号跳跃**\n\n我重新检查了 Introduction（introduction.tex lines 14-18）。编号为 (1)(2)(3)(4)，对应四个 findings。没有发现跳跃。R2 可能看到了编译渲染后的某个版本差异，或者将 contribution list（也是 1-4）与 findings list 混淆。需要 R2 clarify 具体是哪一行。\n\n**[REBUT] R2-W3: \"r = 0.1-1.7\" 疑似笔误**\n\nR2 说 \"r = 0.1-1.7\" 疑似笔误。我检查了全文——没有找到 \"r = 0.1-1.7\" 这个表述。论文中出现的是：\n- \"r = 0.112-0.129\"（Table 2, pairwise SCS-confusion correlation）\n- \"r² = 1.3-1.7%\"（§5.2, 即 r²=0.013-0.017）\n- \"r = 0.11-0.19\"（§1 Introduction, Contribution 2）\n\nR2 可能将 \"r²=1.3-1.7%\" 误读为 \"r=0.1-1.7\"。如果是这样，原文没有笔误。\n\n**[AGREE] R2-W4: 补充材料标题不一致**\n\n未验证 supplementary.tex 内容（信息隔离下我无法确认是否有独立 supplementary 文件），但如果存在旧标题，应统一。\n\n**[REBUT] R2-W5: \"First controlled study\" overclaim**\n\nR2 认为 LLM-PEE 也有 similarity-based 分组比较，因此 \"first controlled study\" overclaim。但论文 §3 已明确区分：\"LLM-PEE conflates count and confusability\"——LLM-PEE 按 similarity 分组时同时改变了 batch size 和 batch confusability，无法 isolate 哪个因素导致变化。本文的 BCS-controlled 实验（固定 count、变化 BCS）是真正的 controlled isolation。\"First controlled study isolating type confusability from type count via stratified design\" 这个 claim 在我看来是准确的，前提是 \"controlled\" 明确指 stratified/quasi-experimental design 而非简单的分组比较。\n\n**[AGREE] R2-W6: TOST logit-scale 结果仅在 Appendix**\n\n与我的 N1 一致。logit-scale TOST (p=0.209) inconclusive 是一个重要 caveat，应在主文 §5.4 中报告而非仅在 Appendix。\n\n---\n\n## Questions 回应\n\n**R2-Q1: BCS-accuracy 关系是否本质上是 constrained-decoding format 的产物？**\n\n这与我的 N3 完全一致。我在 N3 中已详细论述：enum constraint 将所有 non-none errors 强制导入 type substitution channel，结构性地保证了 BCS-error rate 的关联。NER 的 batch-level null 与此一致——当 errors 可散布到 missed entities、boundary errors、hallucinated types 时，BCS 失去预测力。论文需要 unconstrained decoding ablation 来 disentangle。\n\n**R2-Q2: Typical-batch gap 2.2pp 是否 meaningful？**\n\n这也是我的 Q1。补充一点定量分析：2.2pp gap 的 95% CI 为 [0.4, 4.0]（§5.3），下限仅 0.4pp。在 RE accuracy ~70% 的 baseline 下，2.2pp 相当于 3% relative change。对于 deployment-critical 场景（如 biomedical RE），即使 3% 也可能有意义；但论文未提供 domain-specific significance 的讨论。\n\n**R2-Q3: Schema decomposition 方向本身不可行还是 routing 方法不够好？**\n\n论文证据指向两者皆有：NER 的 merge amplification 是结构性的（precision collapse 0.563→0.210, §6），不依赖 routing 方法；RE 的 oracle routing 恢复 +29.8pp（Table 3），证明 decomposition 在 RE 上原则可行，但 practical routing 全部低于 single-pass baseline（Table in Appendix §sec:appendix_routing）。论文 §6 \"Future directions\" 提出了三个具体方向。我认为论文的诊断是充分的。\n\n**R2-Q4: SCS embedding 选择依赖先验知识？**\n\n部分同意。论文对 Few-NERD 使用 Qwen3 embeddings 是因为 \"MiniLM's 384-d space does not separate well\"（§4.2），这确实需要先验知识判断。但 cross-embedding check（MiniLM r=0.172 vs Qwen3 r=0.138, Appendix app:scs-ablation）和四种 prompt variants 的 directional consistency 提供了 robustness evidence。更大的问题是我的 W1：缺乏与真正简单的 baselines（string overlap, WordNet）的对比。\n\n---\n\n## Missing References 回应\n\n**[AGREE]** Fei et al. 2024 和 Gillick et al. 2014 确实相关。Levy et al. 2024 \"Same Task, More Tokens\" 如果在 bib 中但未在正文引用，属于 orphan entry——但引用验证工具显示 orphan_bib = 0，R2 可能需要 double-check 这个 claim。\n\n---\n\n## Minor Issues 回应\n\n- **[AGREE] m1**: -ing 分词结尾确实应修改。\n- **[AGREE] m2**: Table 1 caption 注释可更清晰。\n- **[REBUT] m3**: vLLM v0.20.2——vLLM 版本号是 0.x.y 格式而非 x.y.z，v0.20.2 是 2025 年的合理版本号（vLLM 迭代快），不太可能是笔误。\n- **[AGREE] m4**: Contribution 3 \"task asymmetry\" 确实可能主要由 evaluation format 驱动（constrained decoding vs free-form）而非 task 本质差异。这与我的 N3 呼应。\n- **[AGREE] m5**: 4 条 bib entry 在 OpenAlex 未找到是索引覆盖问题（gemini-2025 太新, dror-2018 和 sclar-2024 是已知论文, li2023evaluating 是 arXiv preprint），非虚假引用。\n\n---\n\n## 评分差异分析与是否调整\n\nR2 给 Overall 3.0 (Findings)，我给 3.5 (Borderline Conference)。差异主要来自：\n\n| 维度 | R1 (我) | R2 | 差异原因 |\n|------|---------|-----|----------|\n| Soundness | 3.5 | 3.5 | 一致 |\n| Excitement | 3.0 | 2.5 | R2 认为 practical impact 不足，我给了诊断研究更多 credit |\n| Overall | 3.5 | 3.0 | 主要由 Excitement 差异驱动 |\n\nR2 的 N3 (\"So what?\" 问题) 是我之前考虑但未列为 critical 的。重新审视后：\n\n- R2 的 Excitement 2.5 偏低——ARR guidelines H6 明确不应惩罚 negative results，且 SDGD 失败诊断有方法论价值。\n- 但 R2 对 practical implications 的批评确实有力——论文的 actionable takeaways 确实薄弱。\n- N2（SCS novelty）我部分反驳了，但 R2 的 concern 确实存在：如果 metric 无 novelty，实验设计和 findings 必须足够强才能支撑论文。\n\n**我的最终评分调整**：\n\n维持 **Overall 3.5 (Borderline Conference)**，不调整。理由：\n\n1. 实验设计的 rigor（within-pool control, permutation tests, TOST, variance decomposition）在 NLP 论文中确实突出，值得 conference-level recognition。\n2. 诊断贡献（merge amplification 是 decomposition 的真正瓶颈、NER vs RE 的 task asymmetry 解释、centrality confound 识别）对后续工作有实质指导意义。\n3. 但如果 N1（TOST margin）和 N3（constrained decoding ablation）在 rebuttal 中未得到充分回应，我会准备降至 3.0。\n\n关键升/降条件不变：unconstrained decoding ablation 是决定性实验。\n",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见\n\n---\n\n## Must-Fix 逐条回应\n\n**[AGREE] R2-N1: 标题/摘要 scope 与实际发现不匹配**\n\n同意，这与我的 N2 完全一致。补充两点：\n\n1. R2 引用的 NER n=150 应为 n=450（§5.3 prompt sensitivity 段落和 Appendix §sec:appendix_prompt_sensitivity 明确报告 \"pooling across three seeds and all count levels (n=450)\"）。数据本身更强化了 null result 的可靠性——n=450 的 null 比 n=150 的 null 更有说服力，反而加重了 scope mismatch 的问题。\n2. 我想强调一个 R2 未提的细节：pairwise SCS 在三个任务上均显著（Few-NERD r=0.112, MAVEN r=0.129, FewRel r=0.187; Table 2），这是论文真正跨任务的发现。问题在于从 pairwise 到 batch-level 的 aggregation 仅在 RE 上成功。Title 如果修改为聚焦 \"pairwise confusability predicts type confusion across tasks; batch-level prediction is task-dependent\" 的叙事，scope 问题可以解决而不缩小实际贡献。\n\n**[REBUT] R2-N2: SCS/BCS 指标新颖性不足**\n\nR2 的批评有道理但过于严厉。论文 §3 Related Work \"SCS novelty\" 段落已经明确承认 \"SCS shares its formal definition with the partitioning criterion used in LLM-PEE\"，并将 contribution 定位在 \"controlled experimental framework\" 而非 metric 本身。关键区别：\n\n1. **LLM-PEE 用 embedding similarity 做工程（schema partitioning），本文用它做科学（controlled measurement）**。这是工具与理论的区别——温度计不是新发明，但用它做 controlled experiment 证明发烧与感染的 dose-response relationship 仍是科学贡献。\n2. Contribution 2 的原文是 \"We validate that pairwise embedding similarity predicts type confusion and show that weak pair-level signals (r=0.11-0.19) amplify to batch-level predictive power (R²=0.22-0.53) through correlated aggregation\"（§1 Introduction）。这里的 contribution 是 validation + aggregation mechanism，不是 metric 本身。\n3. 但我同意 R2 的隐含建议：Contribution 2 的措辞可以更清晰地与 LLM-PEE 区分，避免读者误读为 metric novelty claim。\n\n**[AGREE with qualification] R2-N3: Practical implications 不足**\n\n部分同意。R2 的 \"So what?\" 问题是合理的，但评估应区分两类贡献：\n\n1. **诊断贡献 vs. 解决方案贡献**。论文定位为诊断研究（§1 \"we conduct controlled analysis to understand why extraction degrades\"），而非提出解决方案。诊断的价值在于 (a) 解释为什么 LLM-PEE 等分解方法的 gain 有限（merge amplification 才是瓶颈而非 partitioning quality），(b) 为未来工作指明方向（coarse-to-fine pipelines, retrieval-based routing, calibrated generation; §6 SDGD \"Future directions\"）。\n2. **但 R2 对 practical advice 的批评是准确的**：NER 中 \"减少候选类型数\" 确实是 trivially known；RE 中 \"pre-screen 上四分位 SCS\" 的 3-5pp 收益在实际部署中边际效用有限。\n3. 我认为这不应是 \"critical\" 级别——ARR reviewer guidelines (H5) 明确指出不应要求 SOTA results 当论文 claim 的是不同类型的 contribution；(H6) 指出不应惩罚 negative results。论文的 SDGD 失败诊断本身有方法论价值。但如果 R2 认为 excitement 因此不足 (2.5)，这个主观评分是合理的。\n\n---\n\n## Should-Fix 逐条回应\n\n**[AGREE] R2-W1: Abstract 信息密度过高**\n\n同意。Abstract 约 195 words 包含 8+ 数值（-49pp, 2.2pp, 22-53%, +4.3pp 等）和未定义缩写（BCS 在 Abstract 中首次出现时未展开全称——仅有 \"its batch-level aggregation (BCS)\" 作为括号注释，但 SCS 和 BCS 的含义需要更多 context）。按照 ARR 标准，审稿人应在 30 秒内从 Abstract 判断论文价值——当前密度可能阻碍这一目标。\n\n**[REBUT] R2-W2: Introduction findings 段编号跳跃**\n\n我重新检查了 Introduction（introduction.tex lines 14-18）。编号为 (1)(2)(3)(4)，对应四个 findings。没有发现跳跃。R2 可能看到了编译渲染后的某个版本差异，或者将 contribution list（也是 1-4）与 findings list 混淆。需要 R2 clarify 具体是哪一行。\n\n**[REBUT] R2-W3: \"r = 0.1-1.7\" 疑似笔误**\n\nR2 说 \"r = 0.1-1.7\" 疑似笔误。我检查了全文——没有找到 \"r = 0.1-1.7\" 这个表述。论文中出现的是：\n- \"r = 0.112-0.129\"（Table 2, pairwise SCS-confusion correlation）\n- \"r² = 1.3-1.7%\"（§5.2, 即 r²=0.013-0.017）\n- \"r = 0.11-0.19\"（§1 Introduction, Contribution 2）\n\nR2 可能将 \"r²=1.3-1.7%\" 误读为 \"r=0.1-1.7\"。如果是这样，原文没有笔误。\n\n**[AGREE] R2-W4: 补充材料标题不一致**\n\n未验证 supplementary.tex 内容（信息隔离下我无法确认是否有独立 supplementary 文件），但如果存在旧标题，应统一。\n\n**[REBUT] R2-W5: \"First controlled study\" overclaim**\n\nR2 认为 LLM-PEE 也有 similarity-based 分组比较，因此 \"first controlled study\" overclaim。但论文 §3 已明确区分：\"LLM-PEE conflates count and confusability\"——LLM-PEE 按 similarity 分组时同时改变了 batch size 和 batch confusability，无法 isolate 哪个因素导致变化。本文的 BCS-controlled 实验（固定 count、变化 BCS）是真正的 controlled isolation。\"First controlled study isolating type confusability from type count via stratified design\" 这个 claim 在我看来是准确的，前提是 \"controlled\" 明确指 stratified/quasi-experimental design 而非简单的分组比较。\n\n**[AGREE] R2-W6: TOST logit-scale 结果仅在 Appendix**\n\n与我的 N1 一致。logit-scale TOST (p=0.209) inconclusive 是一个重要 caveat，应在主文 §5.4 中报告而非仅在 Appendix。\n\n---\n\n## Questions 回应\n\n**R2-Q1: BCS-accuracy 关系是否本质上是 constrained-decoding format 的产物？**\n\n这与我的 N3 完全一致。我在 N3 中已详细论述：enum constraint 将所有 non-none errors 强制导入 type substitution channel，结构性地保证了 BCS-error rate 的关联。NER 的 batch-level null 与此一致——当 errors 可散布到 missed entities、boundary errors、hallucinated types 时，BCS 失去预测力。论文需要 unconstrained decoding ablation 来 disentangle。\n\n**R2-Q2: Typical-batch gap 2.2pp 是否 meaningful？**\n\n这也是我的 Q1。补充一点定量分析：2.2pp gap 的 95% CI 为 [0.4, 4.0]（§5.3），下限仅 0.4pp。在 RE accuracy ~70% 的 baseline 下，2.2pp 相当于 3% relative change。对于 deployment-critical 场景（如 biomedical RE），即使 3% 也可能有意义；但论文未提供 domain-specific significance 的讨论。\n\n**R2-Q3: Schema decomposition 方向本身不可行还是 routing 方法不够好？**\n\n论文证据指向两者皆有：NER 的 merge amplification 是结构性的（precision collapse 0.563→0.210, §6），不依赖 routing 方法；RE 的 oracle routing 恢复 +29.8pp（Table 3），证明 decomposition 在 RE 上原则可行，但 practical routing 全部低于 single-pass baseline（Table in Appendix §sec:appendix_routing）。论文 §6 \"Future directions\" 提出了三个具体方向。我认为论文的诊断是充分的。\n\n**R2-Q4: SCS embedding 选择依赖先验知识？**\n\n部分同意。论文对 Few-NERD 使用 Qwen3 embeddings 是因为 \"MiniLM's 384-d space does not separate well\"（§4.2），这确实需要先验知识判断。但 cross-embedding check（MiniLM r=0.172 vs Qwen3 r=0.138, Appendix app:scs-ablation）和四种 prompt variants 的 directional consistency 提供了 robustness evidence。更大的问题是我的 W1：缺乏与真正简单的 baselines（string overlap, WordNet）的对比。\n\n---\n\n## Missing References 回应\n\n**[AGREE]** Fei et al. 2024 和 Gillick et al. 2014 确实相关。Levy et al. 2024 \"Same Task, More Tokens\" 如果在 bib 中但未在正文引用，属于 orphan entry——但引用验证工具显示 orphan_bib = 0，R2 可能需要 double-check 这个 claim。\n\n---\n\n## Minor Issues 回应\n\n- **[AGREE] m1**: -ing 分词结尾确实应修改。\n- **[AGREE] m2**: Table 1 caption 注释可更清晰。\n- **[REBUT] m3**: vLLM v0.20.2——vLLM 版本号是 0.x.y 格式而非 x.y.z，v0.20.2 是 2025 年的合理版本号（vLLM 迭代快），不太可能是笔误。\n- **[AGREE] m4**: Contribution 3 \"task asymmetry\" 确实可能主要由 evaluation format 驱动（constrained decoding vs free-form）而非 task 本质差异。这与我的 N3 呼应。\n- **[AGREE] m5**: 4 条 bib entry 在 OpenAlex 未找到是索引覆盖问题（gemini-2025 太新, dror-2018 和 sclar-2024 是已知论文, li2023evaluating 是 arXiv preprint），非虚假引用。\n\n---\n\n## 评分差异分析与是否调整\n\nR2 给 Overall 3.0 (Findings)，我给 3.5 (Borderline Conference)。差异主要来自：\n\n| 维度 | R1 (我) | R2 | 差异原因 |\n|------|---------|-----|----------|\n| Soundness | 3.5 | 3.5 | 一致 |\n| Excitement | 3.0 | 2.5 | R2 认为 practical impact 不足，我给了诊断研究更多 credit |\n| Overall | 3.5 | 3.0 | 主要由 Excitement 差异驱动 |\n\nR2 的 N3 (\"So what?\" 问题) 是我之前考虑但未列为 critical 的。重新审视后：\n\n- R2 的 Excitement 2.5 偏低——ARR guidelines H6 明确不应惩罚 negative results，且 SDGD 失败诊断有方法论价值。\n- 但 R2 对 practical implications 的批评确实有力——论文的 actionable takeaways 确实薄弱。\n- N2（SCS novelty）我部分反驳了，但 R2 的 concern 确实存在：如果 metric 无 novelty，实验设计和 findings 必须足够强才能支撑论文。\n\n**我的最终评分调整**：\n\n维持 **Overall 3.5 (Borderline Conference)**，不调整。理由：\n\n1. 实验设计的 rigor（within-pool control, permutation tests, TOST, variance decomposition）在 NLP 论文中确实突出，值得 conference-level recognition。\n2. 诊断贡献（merge amplification 是 decomposition 的真正瓶颈、NER vs RE 的 task asymmetry 解释、centrality confound 识别）对后续工作有实质指导意义。\n3. 但如果 N1（TOST margin）和 N3（constrained decoding ablation）在 rebuttal 中未得到充分回应，我会准备降至 3.0。\n\n关键升/降条件不变：unconstrained decoding ablation 是决定性实验。\n",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-18T08:33:44.763749+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4363
}
```

</details>

---


### Assistant

_source line 1034 · 2026-05-18T08:33:51.868392+00:00_

交叉回应已提交。

总结：对 R2 的 9 条意见中，我 [AGREE] 4 条（N1 scope mismatch、W1 abstract 密度、W4 标题不一致、W6 logit-scale 位置），[REBUT] 4 条（N2 SCS novelty、W2 编号跳跃、W3 笔误、W5 first study claim），[AGREE with qualification] 1 条（N3 practical implications——诊断研究不应被要求提供 actionable solutions，但 advice 确实薄弱）。维持 Overall 3.5 不调整，关键分歧在于对诊断研究价值的权重差异。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 36

## Round 36

68 recorded events


### User

_source line 1035 · 2026-05-18T09:13:20.580775+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性与实验设计**。

## 论文信息
- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
- **论文路径**: `projects/schema-dag-extraction/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, supplementary.tex）
- **目标 venue**: EMNLP 2026（ARR May 25 cycle）
- **投稿类别**: Findings
- **截止日期**: 2026-05-25

## Venue 格式要求
- Long paper: 8页正文，Short paper: 4页正文；Limitations/Ethics 不计入
- 模板: ACL 格式 `\usepackage[review]{acl}`
- 匿名规则: Double-blind
- 引用格式: natbib

## 你的审查侧重

请重点评估以下方面：

1. **统计方法学**：
   - SCS/BCS 指标定义的合理性（embedding cosine similarity 作为 confusability proxy）
   - 实验设计（Count Curves + BCS-Controlled）是否真正隔离了 count 与 confusability 两个因素
   - TOST 等价性检验的使用是否恰当（margin 选择、power analysis）
   - 效应量解读（pairwise r²=1.3-1.7%，batch-level R²=22-53%）是否过度或合理
   - 单种子评估 + greedy decoding 的局限性

2. **实验设计与控制**：
   - BCS-controlled 实验的 confound 控制是否充分（除 BCS 外还有什么未控制的？）
   - FewRel train+val 合并使用的合理性（数据泄露风险？）
   - Cross-model validation 的充分性（Dimension 2 未在 proprietary model 上验证）
   - MAVEN centrality confound 的处理是否令人信服

3. **Negative Result (SDGD)**：
   - Merge amplification 的诊断是否严谨
   - Oracle routing 实验的设计是否合理
   - 从 negative result 中提取的 insight 是否有价值

4. **结论的可靠性**：
   - Claims 与 evidence 的对应关系是否严密
   - 是否存在过度推断（correlational → causal language）
   - Limitations 是否充分覆盖了关键弱点

请按照以下格式输出审稿意见：

```
## Summary（2-3句概述论文）

## Strengths（逐条列出）

## Weaknesses（逐条列出，按严重程度排序：Must-Fix > Should-Fix > Nice-to-Have）

## Questions（需要作者回答的问题）

## Missing References（遗漏的重要相关工作）

## Minor Issues（拼写、格式等）

## Overall Assessment（评分 + 置信度 + 简要理由）
```

评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-18T09:13:29.829286+00:00_

called Skill

<details open><summary>🔧 Tool call — Skill</summary>

```json
{
  "skill": "review-reviewer-session-start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Skill",
  "tool_args": {
    "skill": "review-reviewer-session-start"
  }
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-18T09:13:29.829632+00:00_

&lt;tool_use_error>Unknown skill: review-reviewer-session-start&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Skill",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-18T09:13:33.798027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1039 · 2026-05-18T09:13:34.099830+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-18T09:13:34.100276+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/schema-dag-extraction/docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-18T09:13:34.150764+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1042 · 2026-05-18T09:13:37.028044+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 1043 · 2026-05-18T09:13:37.453253+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 425
}
```

</details>

---


### Tool call

_source line 1044 · 2026-05-18T09:13:37.604565+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-18T09:13:37.655329+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.fls
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.fdb_latexmk
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.bbl
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.blg
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.out
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.aux
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p14.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/supplementary_p1.png
/
…[truncated 4751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-18T09:13:42.276827+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1047 · 2026-05-18T09:13:42.579911+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 (count-associated decline) has been validated on a proprietary model (Gemini 2.5 Flash, $\rho = -0.900$, $p = 0.037$; Appendix~\ref{sec:appendix_cross_model_gemini}); Dimension~2 (confusability-associated type substitution) has been verified only on open-weight models. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). A FewRel factorial with TOST equivalence testing is consistent with bounded association under the primary linear specification ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp); however, the logit-scale TOST is inconclusive ($p = 0.209$). At $n =
…[truncated 52026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-18T09:13:42.580422+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-18T09:13:42.732220+00:00_

1	\begin{abstract}
2	As large language models are increasingly deployed for information extraction without task-specific training, understanding how schema design affects extraction quality becomes critical for reliable deployment. Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets and quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution (modest in typical batches); BCS explains 22--53\% of cross-batch RE accuracy variance but shows no batch-level signal for NER, where boundary detection failures overwhelm the confusability signal. Confusability operates at the pair level across all three tasks but aggregates to batch-level predictive power only in RE under constrained decoding. Few-shot demonstrations do not reduce the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Count-related decline (Dimension~1) replicates across model scales (8B to 70B) and architecture families including Gemini 2.5 Flash; confusability effects (Dimension~2) are verified on open-weight models (Qwen, LLaMA), identifying confusability as a schema-structural constraint on training-free extraction.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-18T09:13:43.083960+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1051 · 2026-05-18T09:13:43.586376+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
…[truncated 3119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-18T09:13:43.586887+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-18T09:13:43.988830+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and fine-grained entity typing \cite{gillick-2014-entity-typing}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decompositi
…[truncated 3218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1054 · 2026-05-18T09:13:44.039524+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 1055 · 2026-05-18T09:13:44.542295+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate th
…[truncated 8151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1056 · 2026-05-18T09:13:44.542816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1057 · 2026-05-18T09:13:44.593497+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\pm 1$\,SD across 3 seeds (42, 123, 456) $\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}); schema configura
…[truncated 11235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1058 · 2026-05-18T09:13:50.383131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 1059 · 2026-05-18T09:13:50.807673+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapse (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation thus recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation \citep{jagannatha2020calibrating} to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\resi
…[truncated 533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 424
}
```

</details>

---


### Tool call

_source line 1060 · 2026-05-18T09:13:50.808386+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1061 · 2026-05-18T09:13:51.265814+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED slope $-$0.71, adjusted $R^2 = 0.51$, $n = 35$; 95\% CI [0.27, 0.73]) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%); conditional on nonzero confusion (${\sim}11\%$ of pairs), $R^2$ rises to 7\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\% (Monte Carlo simulation with parameters derived from the observed data; this simulation serves as an internal consistency check rather than independent evidence; Appendix~\ref{app:aggregation-sim}), consistent with observed RE values.
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific ($R^2 = 0.22$--$0.53$ vs.\ $r \approx 0$ for NER, $n = 450$). Because RE uses constrained decoding that channels all errors into type substitution \cite{tam-2024-let-me-speak}, BCS--accuracy prediction may depend on this error channeling: constrained decoding is a boundary condition for our batch-level findings \cite{schall-2025-hidden-cost}. Under unconstrained generation, errors may scatter across formats (missed entities, boundary shifts, hallucinated types), diluting the BCS signal as observed in NER. This error channeling hypothesis unifies the RE--NER asymmetry: constrained decoding concentrates errors into type substitution (where BCS is predictive), while unconstrained decoding distributes errors across multiple failure modes (where BCS loses s
…[truncated 1947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-18T09:13:51.316638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-18T09:13:51.417466+00:00_

1	% DEPRECATED — this file is no longer included in main.tex.
2	% The active conclusion is in discussion.tex (\input{discussion}).
3	% Kept for reference only; safe to delete.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-18T09:13:51.819681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-18T09:13:51.920697+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{lla
…[truncated 4608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1066 · 2026-05-18T09:13:52.272503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
  }
}
```

</details>

---


### Tool result

_source line 1067 · 2026-05-18T09:13:52.373362+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	
11	\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	All supplementary material is included in the appendix of the main paper.
19	
20	\end{document}
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-18T09:13:57.745565+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-18T09:13:57.946925+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-18T09:13:57.947441+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1071 · 2026-05-18T09:13:57.998189+00:00_

1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	@inproceedings{tam-2024-let-me-speak,
6	  title     = {Let Me Speak Freely? {A} Study on the Impact of Format Restrictions on Performance of Large Language Models},
7	  author    = {Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hung-yi and Chen, Yun-Nung},
8	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2408.02442}
11	}
12	
13	@inproceedings{yin-2019-zero-shot-bench,
14	  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},
15	  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},
16	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
17	  pages     = {3914--3923},
18	  year      = {2019},
19	  url       = {https://arxiv.org/abs/1909.00161}
20	}
21	
22	@article{schuirmann-1987-tost,
23	  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},
24	  author    = {Schuirmann, Donald J.},
25	  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},
26	  volume    = {15},
27	  number    = {6},
28	  pages     = {657--680},
29	  year      = {1987},
30	  doi       = {10.1007/BF01068419}
31	}
32	
33	@article{gemini-2025,
34	  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},
35	  author    = {Comanici, Gheorghe and others},
36	  journal   = {arXiv preprint arXiv:2507.06261},
37	  year      = {2025},
38	  url       = {https://arxiv.org/abs/2507.06261}
39	}
40	
41	@inproceedings{snell2017prototypical,
42	  title     = {Prototypical Networks for Few-shot Learning},
43	  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard
…[truncated 8365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-18T09:14:02.172418+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
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

_source line 1073 · 2026-05-18T09:14:02.223400+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-18T09:14:05.589311+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring dimensions"
  }
}
```

</details>

---


### Tool call

_source line 1075 · 2026-05-18T09:14:06.091776+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission guidelines reviewer instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission guidelines reviewer instructions"
  }
}
```

</details>

---


### Tool result

_source line 1076 · 2026-05-18T09:14:13.186938+00:00_

Web search results for query: "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"}]

Based on the search results, I've found relevant information about the ACL Rolling Review (ARR) review form criteria and reviewer guidelines for the 2025-2026 period.

## ARR Review Form Scoring Dimensions (2025-2026)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, 
…[truncated 1419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7597
}
```

</details>

---


### Tool result

_source line 1077 · 2026-05-18T09:14:16.405698+00:00_

Web search results for query: "EMNLP 2026 ARR submission guidelines reviewer instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"}]

Based on the search results, I found information about EMNLP 2026 ARR submission guidelines and reviewer instructions:

## Key Submission Guidelines:

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Authors submit articles to ARR, where submissions receive reviews and meta-reviews from ARR reviewers and action editors; then authors commit their reviewed articles to a publication venue (e.g., EMNLP 2026), where Senior Area Chairs and Program Chairs make acceptance decisions from the ARR reviews and meta-reviews.

## Important P
…[truncated 1224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10313
}
```

</details>

---


### Tool call

_source line 1078 · 2026-05-18T09:14:19.925485+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1079 · 2026-05-18T09:14:20.026401+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1080 · 2026-05-18T09:14:24.198400+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc), and descriptions of each score level. I need the exact criteria for Soundness, Excitement, Overall Assessment, Confidence, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc), and descriptions of each score level. I need the exact criteria for Soundness, Excitement, Overall Assessment, Confidence, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 1081 · 2026-05-18T09:14:25.054031+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines. I need all scoring criteria, what each score means, guidance on how to evaluate papers, and any specific instructions about what reviewers should focus on."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines. I need all scoring criteria, what each score means, guidance on how to evaluate papers, and any specific instructions about what reviewers should focus on."
  }
}
```

</details>

---


### Tool result

_source line 1082 · 2026-05-18T09:14:32.535510+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
**Scale: 1-5**
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## Soundness
**Scale: 1-5 (with .5 increments)**
- **5:** "Excellent: This study is one of the most thorough I have seen, given its type."
- **4:** "Strong: This study provides sufficient support for all of its claims."
- **3:** "Acceptable: This study provides sufficient support for its main claims."
- **2:** "Poor: Some of the main claims are not sufficiently supported."
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
**Scale: 1-5 (with .5 increments)**
- **5:** "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4:** "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3:** "Interesting: I might mention some points of this paper to others."
- **2:** "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1:** "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment
**Scale: 1-5 (with .5 increments)**
- **5:** "Consider for Award: Could be considered for an outstanding paper award."
- **4:** "Conference: Could be accepted to an *ACL conference."
- **3:** "Findings: Could be accepted to the Findings of the ACL."
- **2:** "Resubmit next cycle: Needs substantial revisions."
- **1:** "Do not resubmit: Has to be fully redone or is not relevant."

## Reproducibility
**Scale: 1-5**
- **5:** "They could easily reproduce the results."
- **4:** "They coul
…[truncated 877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8337
}
```

</details>

---


### Tool result

_source line 1083 · 2026-05-18T09:14:33.792161+00:00_

# ARR Reviewer Guidelines Summary

## Scoring System (Starting February 2025)

ARR reviewers provide three distinct scores:

1. **Soundness**: Technical validity and methodological rigor. "The _soundness_ scores must be justified by the text of the review." Low soundness ratings require explicit justification in your written comments.

2. **Excitement**: Personal interest level. This is subjective and "do not necessarily come with explicit reasons." A paper can be sound but personally uninteresting.

3. **Overall Assessment**: Explicit recommendation reflecting soundness, excitement, novelty, and impact combined. Papers for main venues must be "sufficiently sound and reproducible."

## Core Evaluation Tasks

**Task 1: Calendar Management**
Block time for reviewing, discussion periods, and updates. Factor in paper reading, writing ~0.5 pages of review, and spreading work across days.

**Task 2: Assignment Verification**
- Confirm expertise matches the paper's methodology
- Check for author identity knowledge (disclose if discovered)
- Verify no academic conflicts of interest

**Task 3: Write Strong Reviews**
- Read twice: skim first to assess expectations, then in-depth for evaluation
- Be specific with criticisms, avoiding vague complaints
- Check reviews against 17 common heuristic problems (H1-H17)
- Watch for 15 common NLP paper issues (M1-M5, T1-T2, R1-R5, G1-G5)
- Ensure tone remains professional and constructive

**Task 4: Engage in Discussion**
Acknowledge author responses and update assessments based on clarifications. "If you find that at least some of your concerns were sufficiently addressed, please update the scores."

## Key Guidance Principles

**What Constitutes Valid Criticism:**
- Missing specific references published 3+ months before deadline
- Named methodological flaws with concrete examples
- Lack of required comparisons to relevant, published baselines

**What to Avoid (Common Mistakes):**
Dismissing papers as "unsurprising," "too simple," lack
…[truncated 334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8738
}
```

</details>

---


### Tool call

_source line 1084 · 2026-05-18T09:16:05.623916+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1085 · 2026-05-18T09:16:06.580888+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-18T09:16:06.581352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1087 · 2026-05-18T09:16:07.084041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1088 · 2026-05-18T09:16:07.387047+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1089 · 2026-05-18T09:16:07.644746+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1063
}
```

</details>

---


### Tool result

_source line 1090 · 2026-05-18T09:16:08.500434+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1416
}
```

</details>

---


### Tool result

_source line 1091 · 2026-05-18T09:16:08.753397+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1366
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-18T09:16:12.642770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1093 · 2026-05-18T09:16:13.201371+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1094 · 2026-05-18T09:16:13.705067+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1062
}
```

</details>

---


### Tool call

_source line 1095 · 2026-05-18T09:16:13.705483+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1096 · 2026-05-18T09:16:14.312202+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool result

_source line 1097 · 2026-05-18T09:16:14.865537+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1160
}
```

</details>

---


### Tool call

_source line 1098 · 2026-05-18T09:16:22.523953+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
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

_source line 1099 · 2026-05-18T09:16:22.576040+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1100 · 2026-05-18T09:19:06.395344+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性与实验设计\n\n### Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度如何预测性能退化，将退化分解为两个维度：type 数量（count）和 type 间语义相似度（confusability）。通过 SCS/BCS 指标量化 confusability，在 FewRel、DocRED、Few-NERD、MAVEN 四个数据集上进行 count curve 和 BCS-controlled 实验。核心发现：count 导致 recall 下降（主效应），confusability 导致 type substitution（RE 中 BCS 解释 22-53% batch 间 accuracy 方差，NER 无 batch 级信号）。Schema decomposition（SDGD）因 merge amplification（NER）和 routing failure（RE）而失败。\n\n### Strengths\n\n**S1. 实验设计的方法论贡献显著。** 将 count 与 confusability 两个因素通过 BCS-controlled 实验隔离，是一个干净的准实验设计。固定 type 数量而仅变动 BCS 的做法（§3.3 Experiment 2）在 IE 领域尚属首次，研究问题清晰，RQ1-RQ3 层层递进。\n\n**S2. 统计方法异常严谨（在 NLP 论文中）。** 使用 TOST 等价性检验评估 count×BCS 交互效应、permutation test 比较跨 pool 斜率一致性、bootstrap CI（B=10,000 pair-level; B=1,000 batch-level）、variance decomposition 区分 batch 与 seed 方差。这种统计严谨性在 NLP 实证研究中不多见。TOST sensitivity analysis（Appendix Table 5）在多个 margin 上报告结果，而非仅挑最有利的。\n\n**S3. 透明的 negative results 报告。** SDGD 失败的诊断（merge amplification 导致 precision collapse 0.563→0.210; routing failure 因 constrained decoding 迫使每个 sub-schema 产生 confident predictions）具有独立价值。Oracle routing 实验（Table 3: 0.802 vs single-pass 0.504）清晰定位了瓶颈在 routing 而非 partitioning。\n\n**S4. 跨模型验证覆盖面广。** Dimension 1 在 Qwen3-32B、Llama-3.1-8B/70B、Gemini 2.5 Flash（proprietary）上均得到验证，RE count curve 斜率近乎一致（70B: -30.7pp vs 32B: -30.1pp, Table 9）。跨架构一致性增强了 count 退化的可信度。\n\n**S5. Limitations 异常全面。** 10 条 limitations 预先回应了大部分潜在批评（单种子、logit-scale TOST inconclusive、causal mechanism、unconstrained decoding ablation 缺失等）。Multiple comparisons 段落引用 Rothman (1990) 论证跨数据集比较属于 independent replications 不需 family-wise correction，方法论上合理。\n\n**S6. Confound 控制意识强。** MAVEN centrality confound（§4.5）的处理特别出色：识别到 positive raw correlation 异常→诊断 embedding collapse→partial correlation 控制 log frequency + degree centrality→正相关消失。FewRel split-origin covariate analysis（Appendix I）同样严谨。\n\n---\n\n### Weaknesses（按严重程度排序）\n\n#### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] Pairwise effect size 极小（r²=1.3-1.7%），pair-to-batch aggregation 的逻辑链依赖事后模拟而非独立验证。**\n- 具体位置：Table 2, §4.2, Appendix F (aggregation simulation)\n- 问题：SCS 作为 confusability 的核心 proxy，仅解释 1.3-1.7% 的 pairwise type confusion 方差。论文引用 behavioral research 标准（Cohen 1988; Lakens 2013）论证此为\"small but real\"，但类比不完全成立：behavioral research 中 individual-difference predictors 面对的是人类行为的高噪声，而此处 predictor（SCS）和 outcome（type confusion）均来自同一 LLM 系统，理论上应有更强的对应关系。\n- Batch-level R²=22% 的核心跳跃依赖 Appendix F 的 Monte Carlo simulation（conditional R²=7% among non-zero pairs → batch R² ≈ 22%）。但该模拟使用从观测数据估计的参数（inter-pair SCS correlation ρ=0.35），本质是 post-hoc curve fitting 而非独立预测。模拟\"match\"观测值不构成独立证据，论文自身也承认（\"this simulation serves as an internal consistency check rather than independent evidence\"），但 Discussion §6 仍以此解释 batch-level R² 的来源。\n- 为什么影响接收：如果 pairwise 效应本身微弱，batch-level 效应的可靠性就完全依赖于聚合机制。论文需要更清晰地论证为什么 1.3% 的 pairwise 信号足以支撑\"confusability as a schema-structural constraint\"这一核心 claim。\n- 建议修改方向：(1) 在 §4.2 中直接讨论 conditional vs unconditional R² 的区别及其含义，而非仅在 appendix 中提及；(2) 用 held-out batch prediction 验证 aggregation（即用一部分 batches 拟合 BCS→accuracy 模型，在另一部分上测试），而非依赖 simulation match。\n\n**N2 [critical] \"Two separable dimensions\"的 claim 依赖 TOST margin 选择，logit-scale 检验不支持等价性。**\n- 具体位置：§4.4, Appendix C (Table 5, logit-scale paragraph)\n- 问题：论文的核心框架是 count 和 confusability 是\"两个可分离维度\"。支撑这一 claim 的 TOST 等价性检验在 ±3pp margin 下显著（p=0.003），但在 ±1pp 下 inconclusive（p=0.278），且 logit-scale TOST 在等效 ±3pp margin 下也 inconclusive（p=0.209）。论文虽然透明报告了这些结果，但在 abstract 和 introduction 中仍使用\"bounded association\"这一较强表述。\n- 交互效应点估计 0.47pp 确实很小，但 90% CI 为 [-1.0, 2.0]pp（linear scale），上界达到主效应（2.2pp）的 91%。这意味着在最坏情况下，交互效应可能接近主效应本身的量级。\n- logit-scale interaction 为 0.111 logit (p=0.047)，实际上是 marginally significant 而非 null。论文将此定位为\"sensitivity check\"并保留 linear-scale 作为 primary test，但在 accuracy 接近 50% 时 linear scale 会压缩交互效应，logit scale 才是更合适的模型。\n- 为什么影响接收：如果 count × confusability 交互不可忽略，\"两个独立维度\"的框架就需要修改为\"两个部分耦合的维度\"，这会影响论文的核心叙事。\n- 建议修改方向：(1) 在正文中承认 logit-scale 结果为 marginally significant，而非仅在 appendix 中作为 sensitivity check 淡化；(2) 将 \"separable dimensions\" 措辞改为更审慎的表述如 \"largely additive with bounded interaction\"；(3) 增加样本量（更多 count levels 或 batches）以获得足够 power 来 resolve logit-scale 的不确定性。\n\n**N3 [critical] BCS batch-level 效应仅对 RE + constrained decoding 成立，但论文标题和 abstract 暗示普适性。**\n- 具体位置：Title, Abstract, §4.3-4.4, Discussion §6\n- 问题：论文标题\"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"暗示对 IE 的普适性。但实际上：\n  - NER：batch-level BCS-F1 correlation 为 null（r≈0, n=450, §4.4），仅 pairwise 效应显著但极弱（r²=1.3%）\n  - ED (MAVEN)：batch-level 出现 positive correlation（方向相反），归因于 centrality confound，控制后效应消失\n  - RE：batch-level 效应仅在 constrained decoding 下验证（Limitations item 9 承认未测试 unconstrained decoding）\n- Discussion §6 的\"error channeling hypothesis\"（constrained decoding 将所有错误集中到 type substitution，因此 BCS 仅在此条件下有 predictive power）是一个合理的事后解释，但也意味着 BCS 的适用范围远比论文 framing 暗示的窄。\n- 为什么影响接收：论文的核心贡献（BCS 作为 schema complexity 的 predictive metric）如果仅适用于 RE + constrained decoding，其实际影响力大幅缩减。审稿人和读者可能基于标题/abstract 期待一个跨任务的通用框架。\n- 建议修改方向：(1) 标题和 abstract 应更精确地界定 BCS 效应的适用范围（如\"...with task-dependent structure\"已在 conclusion 中出现，但 abstract 首句给出的印象仍是普适的）；(2) 至少对 RE 进行一个 unconstrained decoding ablation，以验证 error channeling hypothesis；(3) 如果 BCS 效应确实是 format-dependent 的，在 contribution 列表中明确这一限定。\n\n#### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] FewRel train+val 合并的合理性论证充分，但 80-type pool 的 BCS 结果可能受 pool composition 影响。**\n- 具体位置：§3.1 (FewRel paragraph), Appendix I (Split-Origin Covariate Analysis)\n- 问题：FewRel 合并 64 train-origin + 16 val-origin types。Appendix I 的 covariate analysis 证明 BCS partial effect 不受 split-origin 影响（β_origin = -0.057, p=0.245）。但 train-origin types 准确率数值上低 8.8pp（p=0.06, marginal），且 16 个 val-origin types 仅占 20%。在 extreme-batch 构造中，如果 high-BCS batches 系统性地富集了某一 origin 的 types（如 train-origin types 之间更相似），可能引入 subtle confound。\n- 建议：报告 extreme high-BCS 和 low-BCS batches 中 train/val origin 比例的分布，以排除 compositional confound。\n\n**W2 [warning] Dimension 2 在 proprietary model 上未验证，跨模型证据不对称。**\n- 具体位置：Limitations item 1, Appendix G (70B), Appendix H (Gemini)\n- 问题：Dimension 1（count decline）在 4 个模型上验证，包括 proprietary（Gemini）。Dimension 2（confusability）仅在 open-weight 模型上验证：Qwen3-32B（primary）、Llama-8B（floor effects on NER）、Llama-70B（仅 FewRel count 16 一个条件）。论文将 confusability 定位为\"structural constraint\"，但缺乏 proprietary model 上的 BCS-controlled 验证。\n- 建议：至少在 Gemini 上复现一个 BCS-controlled 条件（如 FewRel count 8, 25 low + 25 high batches），或在 Discussion 中更明确地将 Dimension 2 的 generalizability 标记为 open question。\n\n**W3 [warning] 单种子评估限制 BCS-controlled 实验的 precision estimation。**\n- 具体位置：§3.5, Limitations item 4, Appendix J (variance decomposition)\n- 问题：BCS-controlled 实验使用单种子（seed 42）+ greedy decoding。Appendix J 的 variance decomposition 证明 batch 间方差远大于 seed 间方差（5-474×），论证了 batch composition 是主要变异来源。但这个分析是在 count curve 实验上做的，而非 BCS-controlled 实验本身。BCS-controlled 实验的 extreme batches 是精心构造的（非随机），其 seed 敏感性可能与随机 batches 不同。\n- 建议：对 BCS-controlled 的 key result（如 FewRel 80-rel extreme-batch gap）补充 2-3 个种子的复现，或至少说明 greedy decoding 下的 variance decomposition 结论可以推广到 extreme batches。\n\n**W4 [warning] Typical-batch 效应量（2.2pp）的实际意义有限。**\n- 具体位置：§4.3 (Practical magnitude paragraph)\n- 问题：Extreme-batch gap（31.2pp）占据了叙事的主导位置，但 typical batches（random sampling）下 BCS 带来的 expected accuracy gap 仅 2.2pp（95% CI: [0.4, 4.0]）。在 Discussion §6 的 practical implications 中，论文建议 practitioners \"pre-screen type pairs in the upper SCS quartile\"以识别 3-5pp 的准确率风险。这个量级在很多应用场景中可能不值得额外的 schema 分析开销。\n- 建议：在 Discussion 中更坦诚地讨论 typical-batch 效应量是否达到实际部署中的 actionable 阈值，而非主要用 extreme-batch 结果来 frame practical implications。\n\n**W5 [warning] NER U-shape rebound 的机制解释缺乏直接证据。**\n- 具体位置：§4.1 (count curves), Discussion §6 (\"dual-task burden\" hypothesis)\n- 问题：NER recall 在中间 count（22-44）出现谷底后在 full-schema（66 types）处 recovery（0.27→0.41）。论文假设这是因为\"at full schema, type-membership filtering becomes vacuous and recall recovers\"。但这个假设没有直接实验验证——例如，在接近 full-schema 的 count（如 50、55、60 types）上测试以确认 recovery trajectory，或对比有/无 type filtering 的 ablation。\n- 建议：承认 U-shape 机制仍属假设性质，或补充中间 count 的数据点。\n\n**W6 [warning] Confusability-aware grouping 相对 random 无显著优势（+1.4pp, p≈0.19），削弱 BCS 的实践价值。**\n- 具体位置：Table 3 (batch_composition), §5 (RE: oracle routing)\n- 问题：即使在 oracle routing 下（消除 routing failure），confusability-aware grouping（graph coloring）仅比 random batching 高 1.4pp（0.802 vs 0.788±0.018, p≈0.19）。这意味着即使知道哪些 types 容易混淆，刻意分开它们也不能带来统计显著的改善。这与\"BCS predicts 22-53% of variance\"的发现形成张力：如果 BCS 能解释如此多的方差，为什么 BCS-aware grouping 不能改善结果？\n- 建议：需要在 §5 或 Discussion 中解释这一矛盾。可能的解释：graph coloring 降低了 mean BCS 但未充分降低 max BCS（最具混淆性的 pair 可能仍在同一 batch），或 random batching 本身已产生足够的 BCS 分散。\n\n---\n\n### Questions（需要作者回答）\n\n**Q1.** 为什么不对 RE 进行 unconstrained decoding ablation？这是验证 \"error channeling hypothesis\" 最直接的实验，且应比添加新模型更容易实现。如果 BCS-accuracy association 在 unconstrained decoding 下消失，论文的 batch-level 发现将被限定为 constrained-decoding-specific，这需要在 framing 中明确反映。\n\n**Q2.** Appendix F 的 aggregation simulation 使用 inter-pair SCS correlation ρ=0.35（estimated from pairs sharing a common type）。这个估计的标准误是多少？如果 ρ 的真实值显著偏离 0.35，simulation 输出的 batch R² 会如何变化？论文报告了 ρ=0.20 时 batch R²≈0.22（仍 match），但没有给出 ρ 估计本身的 uncertainty。\n\n**Q3.** Few-NERD 使用 Qwen3 embeddings 计算 SCS，而 FewRel/DocRED/MAVEN 使用 MiniLM。论文解释（§3.2）是因为 MiniLM 384-d 空间对 Few-NERD 的同类细粒度 types 区分不够。但如果 SCS 旨在作为一个 \"lightweight pre-hoc proxy\"，embedding 选择不应依赖于对任务特性的先验知识。这是否构成一个 overfitting-to-the-metric 的风险？\n\n**Q4.** Table 2 中 FewRel 的 pairwise SCS-confusion correlation（r=0.187）是在 §3.2 SCS validation 段落中报告的，但 Table 2 本身将其排除，理由是\"RE's per-instance format precludes direct comparison of confusion rates\"。能否更清楚地解释这个不一致？\n\n**Q5.** NER 的 exact-match evaluation（Limitations item 6）conflates boundary errors 和 type errors。论文是否尝试过 relaxed matching（如 partial span overlap）？如果 relaxed matching 下 pairwise SCS-confusion correlation 增强，这将强化 confusability 假说在 NER 上的证据。\n\n---\n\n### Missing References\n\n1. **Schick & Schütze (2021), \"Exploiting Cloze-Questions for Few-Shot Text Classification and Natural Language Inference\"** — 论文讨论了 label word 选择对 prompt-based classification 的影响，与 type confusability 高度相关但未被引用。\n2. **Hu et al. (2022), \"Knowledgeable Prompt-tuning\"** — label verbalization 与 type embedding similarity 的关系。\n3. **Wei et al. (2023), \"Zero-Shot Information Extraction via Chatting with ChatGPT\"** — 与 Li et al. (2023) 类似的 ChatGPT IE 评估，可能包含 schema size 相关观察。\n4. **Ma et al. (2023), \"Large Language Model Is Not a Good Few-Shot Information Extractor, but a Good Reranker for Hard Samples!\"** — 讨论 LLM IE 的局限性，与本文主题直接相关。\n\n---\n\n### Minor Issues\n\n1. Abstract 第一句 \"As large language models are increasingly deployed for information extraction without task-specific training\" 稍显 generic，建议从具体问题切入。\n2. §3.2 \"For Few-NERD, SCS is computed from the extraction model's own embeddings (Qwen3), which creates a shared-representation dependency\" — 这一重要 caveat 被放在 Limitations item 5 中而非正文方法论部分，应在 §3.2 中更显著地讨论。\n3. Table 1 的 BCS Range 列跨数据集不可直接比较（使用不同 embeddings），但 caption 未明确说明。\n4. Figure 1(b) 的 y 轴标签应标注单位（accuracy %）。\n5. 正文第8页 Table 3 caption 使用 \"$^\\dagger$Mean ± SD across 15 random seeds\"，但正文说 SDGD 使用 seed 42 进行主实验——15 random seeds 仅用于 random batching baseline，这一区分不够清晰。\n\n---\n\n### Overall Assessment\n\n## 总体评分\n**Overall**: 3.5（Borderline Conference）\n**一句话总结**: 方法论严谨的实证分析论文，提出了有价值的 count vs confusability 分解框架，但核心 confusability 效应在 typical batches 下量级有限（2.2pp），且 batch-level predictive power 仅限于 RE + constrained decoding，限制了框架的普适性和实践影响力。\n\n## 官方维度打分（来自 ACL ARR review form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法严谨（TOST、permutation test、bootstrap CI），但核心\"separable dimensions\" claim 在 logit-scale 上 inconclusive，pairwise effect size 极小（r²=1.3%），batch-level 效应范围窄（仅 RE + constrained decoding）。所有 claims 的支撑方向正确但强度不均匀。 |\n| Excitement | 3.0/5 | 研究问题有价值（首次隔离 count vs confusability），negative results 有诊断意义。但 typical-batch 效应量有限（2.2pp），无可行的 mitigation 方案（SDGD 失败），实践指导较弱。框架适用范围窄于标题暗示。 |\n| Reproducibility | 4/5 | 实验细节充分（decoding parameters、seed、batch 构造方法、prompt templates 均完整公开）。代码承诺在接收后释放。单 GPU 推理，计算成本可控（~72 GPU-hours）。唯一的扣分点是单种子评估。 |\n| Overall Assessment | 3.5/5 | 方法论贡献（BCS-controlled 实验设计 + 统计分析框架）达到 Conference 水平，但 empirical impact 因效应量有限和适用范围窄而更接近 Findings。如果作者能补充 unconstrained decoding ablation 并修正 framing 的普适性暗示，可上调至 4.0。 |\n| Confidence | 4/5 | 仔细阅读全文及所有 appendix，熟悉 IE、statistical methodology、和 LLM prompting 相关文献。对 TOST equivalence testing 和 effect size interpretation 有专业判断力。 |\n\n### 主要优势（总结）\n- 首次在 zero-shot LLM IE 中通过 controlled stratification 隔离 count 与 confusability\n- 统计分析框架（TOST、permutation tests、variance decomposition）在 NLP 实证研究中属于高水准\n- Negative results（SDGD 失败）的诊断具有独立参考价值\n- 跨模型验证（4 models including proprietary）增强 Dimension 1 的可信度\n- Limitations section 的全面性和诚实度值得肯定",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性与实验设计\n\n### Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度如何预测性能退化，将退化分解为两个维度：type 数量（count）和 type 间语义相似度（confusability）。通过 SCS/BCS 指标量化 confusability，在 FewRel、DocRED、Few-NERD、MAVEN 四个数据集上进行 count curve 和 BCS-controlled 实验。核心发现：count 导致 recall 下降（主效应），confusability 导致 type substitution（RE 中 BCS 解释 22-53% batch 间 accuracy 方差，NER 无 batch 级信号）。Schema decomposition（SDGD）因 merge amplification（NER）和 routing failure（RE）而失败。\n\n### Strengths\n\n**S1. 实验设计的方法论贡献显著。** 将 count 与 confusability 两个因素通过 BCS-controlled 实验隔离，是一个干净的准实验设计。固定 type 数量而仅变动 BCS 的做法（§3.3 Experiment 2）在 IE 领域尚属首次，研究问题清晰，RQ1-RQ3 层层递进。\n\n**S2. 统计方法异常严谨（在 NLP 论文中）。** 使用 TOST 等价性检验评估 count×BCS 交互效应、permutation test 比较跨 pool 斜率一致性、bootstrap CI（B=10,000 pair-level; B=1,000 batch-level）、variance decomposition 区分 batch 与 seed 方差。这种统计严谨性在 NLP 实证研究中不多见。TOST sensitivity analysis（Appendix Table 5）在多个 margin 上报告结果，而非仅挑最有利的。\n\n**S3. 透明的 negative results 报告。** SDGD 失败的诊断（merge amplification 导致 precision collapse 0.563→0.210; routing failure 因 constrained decoding 迫使每个 sub-schema 产生 confident predictions）具有独立价值。Oracle routing 实验（Table 3: 0.802 vs single-pass 0.504）清晰定位了瓶颈在 routing 而非 partitioning。\n\n**S4. 跨模型验证覆盖面广。** Dimension 1 在 Qwen3-32B、Llama-3.1-8B/70B、Gemini 2.5 Flash（proprietary）上均得到验证，RE count curve 斜率近乎一致（70B: -30.7pp vs 32B: -30.1pp, Table 9）。跨架构一致性增强了 count 退化的可信度。\n\n**S5. Limitations 异常全面。** 10 条 limitations 预先回应了大部分潜在批评（单种子、logit-scale TOST inconclusive、causal mechanism、unconstrained decoding ablation 缺失等）。Multiple comparisons 段落引用 Rothman (1990) 论证跨数据集比较属于 independent replications 不需 family-wise correction，方法论上合理。\n\n**S6. Confound 控制意识强。** MAVEN centrality confound（§4.5）的处理特别出色：识别到 positive raw correlation 异常→诊断 embedding collapse→partial correlation 控制 log frequency + degree centrality→正相关消失。FewRel split-origin covariate analysis（Appendix I）同样严谨。\n\n---\n\n### Weaknesses（按严重程度排序）\n\n#### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] Pairwise effect size 极小（r²=1.3-1.7%），pair-to-batch aggregation 的逻辑链依赖事后模拟而非独立验证。**\n- 具体位置：Table 2, §4.2, Appendix F (aggregation simulation)\n- 问题：SCS 作为 confusability 的核心 proxy，仅解释 1.3-1.7% 的 pairwise type confusion 方差。论文引用 behavioral research 标准（Cohen 1988; Lakens 2013）论证此为\"small but real\"，但类比不完全成立：behavioral research 中 individual-difference predictors 面对的是人类行为的高噪声，而此处 predictor（SCS）和 outcome（type confusion）均来自同一 LLM 系统，理论上应有更强的对应关系。\n- Batch-level R²=22% 的核心跳跃依赖 Appendix F 的 Monte Carlo simulation（conditional R²=7% among non-zero pairs → batch R² ≈ 22%）。但该模拟使用从观测数据估计的参数（inter-pair SCS correlation ρ=0.35），本质是 post-hoc curve fitting 而非独立预测。模拟\"match\"观测值不构成独立证据，论文自身也承认（\"this simulation serves as an internal consistency check rather than independent evidence\"），但 Discussion §6 仍以此解释 batch-level R² 的来源。\n- 为什么影响接收：如果 pairwise 效应本身微弱，batch-level 效应的可靠性就完全依赖于聚合机制。论文需要更清晰地论证为什么 1.3% 的 pairwise 信号足以支撑\"confusability as a schema-structural constraint\"这一核心 claim。\n- 建议修改方向：(1) 在 §4.2 中直接讨论 conditional vs unconditional R² 的区别及其含义，而非仅在 appendix 中提及；(2) 用 held-out batch prediction 验证 aggregation（即用一部分 batches 拟合 BCS→accuracy 模型，在另一部分上测试），而非依赖 simulation match。\n\n**N2 [critical] \"Two separable dimensions\"的 claim 依赖 TOST margin 选择，logit-scale 检验不支持等价性。**\n- 具体位置：§4.4, Appendix C (Table 5, logit-scale paragraph)\n- 问题：论文的核心框架是 count 和 confusability 是\"两个可分离维度\"。支撑这一 claim 的 TOST 等价性检验在 ±3pp margin 下显著（p=0.003），但在 ±1pp 下 inconclusive（p=0.278），且 logit-scale TOST 在等效 ±3pp margin 下也 inconclusive（p=0.209）。论文虽然透明报告了这些结果，但在 abstract 和 introduction 中仍使用\"bounded association\"这一较强表述。\n- 交互效应点估计 0.47pp 确实很小，但 90% CI 为 [-1.0, 2.0]pp（linear scale），上界达到主效应（2.2pp）的 91%。这意味着在最坏情况下，交互效应可能接近主效应本身的量级。\n- logit-scale interaction 为 0.111 logit (p=0.047)，实际上是 marginally significant 而非 null。论文将此定位为\"sensitivity check\"并保留 linear-scale 作为 primary test，但在 accuracy 接近 50% 时 linear scale 会压缩交互效应，logit scale 才是更合适的模型。\n- 为什么影响接收：如果 count × confusability 交互不可忽略，\"两个独立维度\"的框架就需要修改为\"两个部分耦合的维度\"，这会影响论文的核心叙事。\n- 建议修改方向：(1) 在正文中承认 logit-scale 结果为 marginally significant，而非仅在 appendix 中作为 sensitivity check 淡化；(2) 将 \"separable dimensions\" 措辞改为更审慎的表述如 \"largely additive with bounded interaction\"；(3) 增加样本量（更多 count levels 或 batches）以获得足够 power 来 resolve logit-scale 的不确定性。\n\n**N3 [critical] BCS batch-level 效应仅对 RE + constrained decoding 成立，但论文标题和 abstract 暗示普适性。**\n- 具体位置：Title, Abstract, §4.3-4.4, Discussion §6\n- 问题：论文标题\"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"暗示对 IE 的普适性。但实际上：\n  - NER：batch-level BCS-F1 correlation 为 null（r≈0, n=450, §4.4），仅 pairwise 效应显著但极弱（r²=1.3%）\n  - ED (MAVEN)：batch-level 出现 positive correlation（方向相反），归因于 centrality confound，控制后效应消失\n  - RE：batch-level 效应仅在 constrained decoding 下验证（Limitations item 9 承认未测试 unconstrained decoding）\n- Discussion §6 的\"error channeling hypothesis\"（constrained decoding 将所有错误集中到 type substitution，因此 BCS 仅在此条件下有 predictive power）是一个合理的事后解释，但也意味着 BCS 的适用范围远比论文 framing 暗示的窄。\n- 为什么影响接收：论文的核心贡献（BCS 作为 schema complexity 的 predictive metric）如果仅适用于 RE + constrained decoding，其实际影响力大幅缩减。审稿人和读者可能基于标题/abstract 期待一个跨任务的通用框架。\n- 建议修改方向：(1) 标题和 abstract 应更精确地界定 BCS 效应的适用范围（如\"...with task-dependent structure\"已在 conclusion 中出现，但 abstract 首句给出的印象仍是普适的）；(2) 至少对 RE 进行一个 unconstrained decoding ablation，以验证 error channeling hypothesis；(3) 如果 BCS 效应确实是 format-dependent 的，在 contribution 列表中明确这一限定。\n\n#### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] FewRel train+val 合并的合理性论证充分，但 80-type pool 的 BCS 结果可能受 pool composition 影响。**\n- 具体位置：§3.1 (FewRel paragraph), Appendix I (Split-Origin Covariate Analysis)\n- 问题：FewRel 合并 64 train-origin + 16 val-origin types。Appendix I 的 covariate analysis 证明 BCS partial effect 不受 split-origin 影响（β_origin = -0.057, p=0.245）。但 train-origin types 准确率数值上低 8.8pp（p=0.06, marginal），且 16 个 val-origin types 仅占 20%。在 extreme-batch 构造中，如果 high-BCS batches 系统性地富集了某一 origin 的 types（如 train-origin types 之间更相似），可能引入 subtle confound。\n- 建议：报告 extreme high-BCS 和 low-BCS batches 中 train/val origin 比例的分布，以排除 compositional confound。\n\n**W2 [warning] Dimension 2 在 proprietary model 上未验证，跨模型证据不对称。**\n- 具体位置：Limitations item 1, Appendix G (70B), Appendix H (Gemini)\n- 问题：Dimension 1（count decline）在 4 个模型上验证，包括 proprietary（Gemini）。Dimension 2（confusability）仅在 open-weight 模型上验证：Qwen3-32B（primary）、Llama-8B（floor effects on NER）、Llama-70B（仅 FewRel count 16 一个条件）。论文将 confusability 定位为\"structural constraint\"，但缺乏 proprietary model 上的 BCS-controlled 验证。\n- 建议：至少在 Gemini 上复现一个 BCS-controlled 条件（如 FewRel count 8, 25 low + 25 high batches），或在 Discussion 中更明确地将 Dimension 2 的 generalizability 标记为 open question。\n\n**W3 [warning] 单种子评估限制 BCS-controlled 实验的 precision estimation。**\n- 具体位置：§3.5, Limitations item 4, Appendix J (variance decomposition)\n- 问题：BCS-controlled 实验使用单种子（seed 42）+ greedy decoding。Appendix J 的 variance decomposition 证明 batch 间方差远大于 seed 间方差（5-474×），论证了 batch composition 是主要变异来源。但这个分析是在 count curve 实验上做的，而非 BCS-controlled 实验本身。BCS-controlled 实验的 extreme batches 是精心构造的（非随机），其 seed 敏感性可能与随机 batches 不同。\n- 建议：对 BCS-controlled 的 key result（如 FewRel 80-rel extreme-batch gap）补充 2-3 个种子的复现，或至少说明 greedy decoding 下的 variance decomposition 结论可以推广到 extreme batches。\n\n**W4 [warning] Typical-batch 效应量（2.2pp）的实际意义有限。**\n- 具体位置：§4.3 (Practical magnitude paragraph)\n- 问题：Extreme-batch gap（31.2pp）占据了叙事的主导位置，但 typical batches（random sampling）下 BCS 带来的 expected accuracy gap 仅 2.2pp（95% CI: [0.4, 4.0]）。在 Discussion §6 的 practical implications 中，论文建议 practitioners \"pre-screen type pairs in the upper SCS quartile\"以识别 3-5pp 的准确率风险。这个量级在很多应用场景中可能不值得额外的 schema 分析开销。\n- 建议：在 Discussion 中更坦诚地讨论 typical-batch 效应量是否达到实际部署中的 actionable 阈值，而非主要用 extreme-batch 结果来 frame practical implications。\n\n**W5 [warning] NER U-shape rebound 的机制解释缺乏直接证据。**\n- 具体位置：§4.1 (count curves), Discussion §6 (\"dual-task burden\" hypothesis)\n- 问题：NER recall 在中间 count（22-44）出现谷底后在 full-schema（66 types）处 recovery（0.27→0.41）。论文假设这是因为\"at full schema, type-membership filtering becomes vacuous and recall recovers\"。但这个假设没有直接实验验证——例如，在接近 full-schema 的 count（如 50、55、60 types）上测试以确认 recovery trajectory，或对比有/无 type filtering 的 ablation。\n- 建议：承认 U-shape 机制仍属假设性质，或补充中间 count 的数据点。\n\n**W6 [warning] Confusability-aware grouping 相对 random 无显著优势（+1.4pp, p≈0.19），削弱 BCS 的实践价值。**\n- 具体位置：Table 3 (batch_composition), §5 (RE: oracle routing)\n- 问题：即使在 oracle routing 下（消除 routing failure），confusability-aware grouping（graph coloring）仅比 random batching 高 1.4pp（0.802 vs 0.788±0.018, p≈0.19）。这意味着即使知道哪些 types 容易混淆，刻意分开它们也不能带来统计显著的改善。这与\"BCS predicts 22-53% of variance\"的发现形成张力：如果 BCS 能解释如此多的方差，为什么 BCS-aware grouping 不能改善结果？\n- 建议：需要在 §5 或 Discussion 中解释这一矛盾。可能的解释：graph coloring 降低了 mean BCS 但未充分降低 max BCS（最具混淆性的 pair 可能仍在同一 batch），或 random batching 本身已产生足够的 BCS 分散。\n\n---\n\n### Questions（需要作者回答）\n\n**Q1.** 为什么不对 RE 进行 unconstrained decoding ablation？这是验证 \"error channeling hypothesis\" 最直接的实验，且应比添加新模型更容易实现。如果 BCS-accuracy association 在 unconstrained decoding 下消失，论文的 batch-level 发现将被限定为 constrained-decoding-specific，这需要在 framing 中明确反映。\n\n**Q2.** Appendix F 的 aggregation simulation 使用 inter-pair SCS correlation ρ=0.35（estimated from pairs sharing a common type）。这个估计的标准误是多少？如果 ρ 的真实值显著偏离 0.35，simulation 输出的 batch R² 会如何变化？论文报告了 ρ=0.20 时 batch R²≈0.22（仍 match），但没有给出 ρ 估计本身的 uncertainty。\n\n**Q3.** Few-NERD 使用 Qwen3 embeddings 计算 SCS，而 FewRel/DocRED/MAVEN 使用 MiniLM。论文解释（§3.2）是因为 MiniLM 384-d 空间对 Few-NERD 的同类细粒度 types 区分不够。但如果 SCS 旨在作为一个 \"lightweight pre-hoc proxy\"，embedding 选择不应依赖于对任务特性的先验知识。这是否构成一个 overfitting-to-the-metric 的风险？\n\n**Q4.** Table 2 中 FewRel 的 pairwise SCS-confusion correlation（r=0.187）是在 §3.2 SCS validation 段落中报告的，但 Table 2 本身将其排除，理由是\"RE's per-instance format precludes direct comparison of confusion rates\"。能否更清楚地解释这个不一致？\n\n**Q5.** NER 的 exact-match evaluation（Limitations item 6）conflates boundary errors 和 type errors。论文是否尝试过 relaxed matching（如 partial span overlap）？如果 relaxed matching 下 pairwise SCS-confusion correlation 增强，这将强化 confusability 假说在 NER 上的证据。\n\n---\n\n### Missing References\n\n1. **Schick & Schütze (2021), \"Exploiting Cloze-Questions for Few-Shot Text Classification and Natural Language Inference\"** — 论文讨论了 label word 选择对 prompt-based classification 的影响，与 type confusability 高度相关但未被引用。\n2. **Hu et al. (2022), \"Knowledgeable Prompt-tuning\"** — label verbalization 与 type embedding similarity 的关系。\n3. **Wei et al. (2023), \"Zero-Shot Information Extraction via Chatting with ChatGPT\"** — 与 Li et al. (2023) 类似的 ChatGPT IE 评估，可能包含 schema size 相关观察。\n4. **Ma et al. (2023), \"Large Language Model Is Not a Good Few-Shot Information Extractor, but a Good Reranker for Hard Samples!\"** — 讨论 LLM IE 的局限性，与本文主题直接相关。\n\n---\n\n### Minor Issues\n\n1. Abstract 第一句 \"As large language models are increasingly deployed for information extraction without task-specific training\" 稍显 generic，建议从具体问题切入。\n2. §3.2 \"For Few-NERD, SCS is computed from the extraction model's own embeddings (Qwen3), which creates a shared-representation dependency\" — 这一重要 caveat 被放在 Limitations item 5 中而非正文方法论部分，应在 §3.2 中更显著地讨论。\n3. Table 1 的 BCS Range 列跨数据集不可直接比较（使用不同 embeddings），但 caption 未明确说明。\n4. Figure 1(b) 的 y 轴标签应标注单位（accuracy %）。\n5. 正文第8页 Table 3 caption 使用 \"$^\\dagger$Mean ± SD across 15 random seeds\"，但正文说 SDGD 使用 seed 42 进行主实验——15 random seeds 仅用于 random batching baseline，这一区分不够清晰。\n\n---\n\n### Overall Assessment\n\n## 总体评分\n**Overall**: 3.5（Borderline Conference）\n**一句话总结**: 方法论严谨的实证分析论文，提出了有价值的 count vs confusability 分解框架，但核心 confusability 效应在 typical batches 下量级有限（2.2pp），且 batch-level predictive power 仅限于 RE + constrained decoding，限制了框架的普适性和实践影响力。\n\n## 官方维度打分（来自 ACL ARR review form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法严谨（TOST、permutation test、bootstrap CI），但核心\"separable dimensions\" claim 在 logit-scale 上 inconclusive，pairwise effect size 极小（r²=1.3%），batch-level 效应范围窄（仅 RE + constrained decoding）。所有 claims 的支撑方向正确但强度不均匀。 |\n| Excitement | 3.0/5 | 研究问题有价值（首次隔离 count vs confusability），negative results 有诊断意义。但 typical-batch 效应量有限（2.2pp），无可行的 mitigation 方案（SDGD 失败），实践指导较弱。框架适用范围窄于标题暗示。 |\n| Reproducibility | 4/5 | 实验细节充分（decoding parameters、seed、batch 构造方法、prompt templates 均完整公开）。代码承诺在接收后释放。单 GPU 推理，计算成本可控（~72 GPU-hours）。唯一的扣分点是单种子评估。 |\n| Overall Assessment | 3.5/5 | 方法论贡献（BCS-controlled 实验设计 + 统计分析框架）达到 Conference 水平，但 empirical impact 因效应量有限和适用范围窄而更接近 Findings。如果作者能补充 unconstrained decoding ablation 并修正 framing 的普适性暗示，可上调至 4.0。 |\n| Confidence | 4/5 | 仔细阅读全文及所有 appendix，熟悉 IE、statistical methodology、和 LLM prompting 相关文献。对 TOST equivalence testing 和 effect size interpretation 有专业判断力。 |\n\n### 主要优势（总结）\n- 首次在 zero-shot LLM IE 中通过 controlled stratification 隔离 count 与 confusability\n- 统计分析框架（TOST、permutation tests、variance decomposition）在 NLP 实证研究中属于高水准\n- Negative results（SDGD 失败）的诊断具有独立参考价值\n- 跨模型验证（4 models including proprietary）增强 Dimension 1 的可信度\n- Limitations section 的全面性和诚实度值得肯定",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1101 · 2026-05-18T09:19:11.186177+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4790
}
```

</details>

---


### Assistant

_source line 1102 · 2026-05-18T09:19:21.792905+00:00_

审稿意见已提交给 Review Director。

总结：

**Overall: 3.5 (Borderline Conference)**

三个 Must-Fix 问题：
1. **Pairwise effect size 极小**（r²=1.3-1.7%），pair-to-batch aggregation 依赖事后模拟而非独立验证
2. **"Two separable dimensions" claim 依赖 TOST margin 选择**，logit-scale TOST inconclusive (p=0.209)，linear-scale CI 上界接近主效应量级
3. **BCS batch-level 效应仅对 RE + constrained decoding 成立**，但标题/abstract framing 暗示跨任务普适性

六个 Should-Fix 问题涉及：FewRel pool composition、Dimension 2 未在 proprietary model 验证、单种子评估、typical-batch 效应量有限（2.2pp）、NER U-shape 机制缺乏直接证据、confusability-aware grouping 无显著优势。

统计方法论本身严谨（TOST、permutation test、bootstrap CI、variance decomposition），是论文的主要优势。Negative results 的诊断（merge amplification, routing failure）具有独立价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 37

## Round 37

14 recorded events


### User

_source line 1103 · 2026-05-18T09:23:17.944903+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Questions 和 Missing References 也请给出你的判断。

---

# Reviewer 2 审稿意见：新颖性、完整性与写作质量

## Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度对性能的影响，将退化分解为两个维度：type count（维度1）和 type confusability（维度2）。通过 SCS/BCS 指标量化 confusability，在 4 个数据集、3 个任务上进行控制实验，发现 count 是主导因素，confusability 在 RE 任务中可解释 22-53% 的 batch 间准确率方差，但在 NER 中无 batch 级信号。Schema 分解因 merge amplification（NER）和 routing failure（RE）而失败。

本文是一项扎实的实证分析研究，实验设计严谨、limitations 诚实透彻，但在新颖性和可操作性方面存在不足。

## Must-Fix 问题

**N1** [critical] Abstract 信息过载，读起来像实验日志而非 compelling story
- Abstract 约 217 词，塞入了过多技术细节——"BCS explains 22-53% of cross-batch RE accuracy variance but shows no batch-level signal for NER, where boundary detection failures overwhelm the confusability signal"——这种句子在 abstract 中过于细碎。审稿人 30 秒内难以抓住核心价值。Abstract 试图覆盖所有发现（count decline、BCS for RE、NER null result、few-shot、SDGD failure、cross-model），导致每个点都只有半句话，没有一个点讲清楚。
- 建议修改方向：聚焦 1-2 个最强发现（如 RE 中 BCS 的解释力 + SDGD 的结构性失败），删减枝节数据点，用一句话清楚传达 "so what"。

**N2** [critical] 核心新颖性主张需更诚实的定位
- 论文声称 "the first controlled study isolating count and confusability"（§1），但核心指标 SCS 与 LLM-PEE 的 embedding similarity 形式完全相同（论文自己在 §2 "SCS novelty" 段承认），BCS 只是 mean aggregation。论文的真正贡献是 experimental methodology（controlled batching, TOST equivalence testing），而非指标本身。但 Contribution 2 的表述 "we repurpose it as a predictive metric and show..." 暗示了指标层面的创新。
- 此外，"two-dimensional degradation" 框架本质上是对已知现象（更多类型更难、相似类型易混淆）的系统化命名。Li et al. (2023) 已观察到 count-dependent degradation，LLM-PEE (2025) 已使用 embedding similarity 做 schema partitioning。
- 建议修改方向：将 novelty claim 明确锚定在 "experimental methodology" 而非 "metric/framework"。

**N3** [critical] RE 结论对 constrained decoding 的依赖是重大边界条件，但论文正文未充分强调
- 论文最强的发现（BCS explains 22-53% of RE variance）依赖于 RE 使用 constrained decoding（enum constraint）。NER 也使用了 constrained decoding（JSON schema with enum types）但 BCS 在 NER 上无 batch 级信号。这说明 constrained decoding 是必要条件但非充分条件——真正的条件是 "closed-set classification format"（RE 的特殊格式），而非 constrained decoding 本身。
- 建议修改方向：更精确地区分 "constrained decoding" 和 "closed-set classification format" 对 BCS 预测力的贡献。

## Should-Fix 问题

**W1** [warning] Pairwise effect size ($r^2 = 1.3\text{-}1.7\%$) 的解释过于乐观
**W2** [warning] 不同数据集使用不同 embedding 引入不必要的变量
**W3** [warning] Introduction 的 Contribution 3 将 NER null result framed 为 contribution
**W4** [warning] MAVEN 的角色定位模糊
**W5** [warning] 页数可能超限

## Questions

**Q1**: BCS 在 NER 上的 batch-level null result 是否意味着 confusability framework 对 NER 缺乏实用价值？
**Q2**: 真正的 boundary condition 是 constrained decoding 还是 closed-set single-label classification format？
**Q3**: 为什么不直接使用 validation-only 的 16 个 relation 作为 primary experiment？
**Q4**: Few-shot 实验中 prompt length 是否被控制？
**Q5**: "Cross-seed variance decomposition" 的意义是什么？

## Missing References

1. Chen et al. (2026), "Understanding LLM Performance Degradation in Multi-Instance Processing" (arXiv:2603.22608)
2. Chroma Research (2025-2026), "Context Rot"
3. Schall & de Melo (2025) 已引用但讨论不足

## Overall Assessment
**Overall**: 3.0（Findings）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-18T09:23:57.258168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-18T09:23:57.609904+00:00_

1	\begin{abstract}
2	As large language models are increasingly deployed for information extraction without task-specific training, understanding how schema design affects extraction quality becomes critical for reliable deployment. Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets and quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution (modest in typical batches); BCS explains 22--53\% of cross-batch RE accuracy variance but shows no batch-level signal for NER, where boundary detection failures overwhelm the confusability signal. Confusability operates at the pair level across all three tasks but aggregates to batch-level predictive power only in RE under constrained decoding. Few-shot demonstrations do not reduce the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Count-related decline (Dimension~1) replicates across model scales (8B to 70B) and architecture families including Gemini 2.5 Flash; confusability effects (Dimension~2) are verified on open-weight models (Qwen, LLaMA), identifying confusability as a schema-structural constraint on training-free extraction.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1106 · 2026-05-18T09:23:58.112177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "offset": "14",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "offset": "14",
    "limit": "12"
  }
}
```

</details>

---


### Tool result

_source line 1107 · 2026-05-18T09:23:58.313518+00:00_

14	Our experiments yield four findings:
15	(1)~Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) and confusability-related type substitution (modest in typical batches), with count as the dominant factor (\S\ref{sec:count_curves}, \S\ref{sec:multi_channel}). The two dimensions are consistent with bounded association under a $\pm 3$\,pp margin in RE (marginally at $\pm 2$\,pp; logit-scale inconclusive) but are coupled in NER.
16	(2)~Pairwise SCS predicts type confusion across NER, RE, and ED (\S\ref{sec:pairwise}); at batch level, BCS predicts accuracy in RE (\S\ref{sec:bcs_controlled}) but not in NER; per-type aggregation is confounded by centrality on homogeneous schemas (\S\ref{sec:centrality_confound}).
17	(3)~Effects are consistent across schema sizes, prompt designs, and model families (\S\ref{sec:bcs_controlled}).
18	(4)~Schema decomposition fails due to merge amplification in NER; RE confusability-aware grouping yields no significant improvement over random despite oracle routing that recovers substantial accuracy (\S\ref{sec:sdgd}).
19	
20	Our contributions are:
21	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
22	    \item We conduct the first controlled study that isolates count and confusability effects on training-free LLM IE performance across four datasets and three tasks (\S\ref{sec:count_curves}, \S\ref{sec:bcs_controlled}).
23	    \item Building on the embedding-similarity criterion used for schema partitioning in prior work \cite{llm-pee-2025}, we repurpose it as a predictive metric and show through controlled experiments that BCS explains 22--53\% of cross-batch RE accuracy variance (\S\ref{sec:pairwise}, \S\ref{sec:bcs_controlled}).
24	    \item We document a task asymmetry: BCS explains 22--53\% of RE accuracy variance through type substitution, yet shows no batch-level signal in NER despite significant pairwise effects (\S\ref{sec:bcs_controlled}, \S\ref{sec:multi_channel}).

…[truncated 219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1108 · 2026-05-18T09:23:58.364195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-18T09:23:58.414902+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED slope $-$0.71, adjusted $R^2 = 0.51$, $n = 35$; 95\% CI [0.27, 0.73]) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%); conditional on nonzero confusion (${\sim}11\%$ of pairs), $R^2$ rises to 7\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\% (Monte Carlo simulation with parameters derived from the observed data; this simulation serves as an internal consistency check rather than independent evidence; Appendix~\ref{app:aggregation-sim}), consistent with observed RE values.
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific ($R^2 = 0.22$--$0.53$ vs.\ $r \approx 0$ for NER, $n = 450$). Because RE uses constrained decoding that channels all errors into type substitution \cite{tam-2024-let-me-speak}, BCS--accuracy prediction may depend on this error channeling: constrained decoding is a boundary condition for our batch-level findings \cite{schall-2025-hidden-cost}. Under unconstrained generation, errors may scatter across formats (missed entities, boundary shifts, hallucinated types), diluting the BCS signal as observed in NER. This error channeling hypothesis unifies the RE--NER asymmetry: constrained decoding concentrates errors into type substitution (where BCS is predictive), while unconstrained decoding distributes errors across multiple failure modes (where BCS loses s
…[truncated 1947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-18T09:24:03.292019+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1111 · 2026-05-18T09:24:03.543067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1112 · 2026-05-18T09:24:04.296904+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-18T09:24:04.498877+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-18T09:26:35.370823+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE with downgrade] R2-N1: Abstract 信息过载**\n\n同意 Abstract 试图覆盖过多发现（count decline、BCS for RE、NER null、few-shot、SDGD failure、cross-model），导致核心 \"so what\" 被淹没。但我将此定位为 **should-fix 而非 must-fix**。理由：\n\n1. Abstract 217 词在 150-250 词范围内，信息密度高但未超限。\n2. 对于一篇多任务、多数据集的实证分析论文，结果的复杂性（RE vs NER 不对称、negative results）天然要求更多 nuance。过度简化反而可能误导读者（如只报告 RE 的 22-53% R² 而不提 NER null result 会夸大普适性）。\n3. 核心问题不是信息量，而是叙事结构——应先给出 high-level takeaway（\"schema complexity predicts degradation through two partially separable dimensions, but the predictive structure is task-dependent\"），再选择性展开 1-2 个最强证据。\n\n总结：同意需要改写，但严重度降为 should-fix。\n\n---\n\n**[PARTIALLY AGREE] R2-N2: 核心新颖性主张需更诚实的定位**\n\n同意 SCS 指标本身与 LLM-PEE 的 embedding similarity 形式完全相同，论文自己在 §2 \"SCS novelty\" 段也承认了这一点（\"SCS shares its formal definition with the partitioning criterion used in LLM-PEE\"）。Contribution 2 的 \"we repurpose it as a predictive metric\" 表述确实暗示了指标层面的创新，需要调整措辞。\n\n但我 **rebut** R2 对框架贡献的低估：\n\n1. **从 engineering tool 到 analytical instrument 的转变不是 trivial 的**。LLM-PEE 将 embedding similarity 作为 partitioning heuristic（工程手段），本文将其转化为 predictive metric 并通过 controlled experiments 量化其解释力（R²=22-53%）和边界条件（RE yes, NER no, same-domain schemas confounded）。这个转变需要 BCS-controlled experimental design、TOST equivalence testing、within-pool analysis 等全套方法论，而非简单的 metric reuse。\n2. **\"两个维度\"不只是命名已知现象**。Li et al. (2023) 观察到 count-dependent degradation 但未分离 confusability；LLM-PEE 使用 embedding similarity 做 partitioning 但从未量化 confusability 对 accuracy 的独立预测力。本文的核心发现——\"count 和 confusability 在 RE 中是 largely additive 的\"（TOST p=0.003 at ±3pp）以及\"NER 中两者耦合\"——是 prior work 未曾建立的定量结论。\n3. 但 R2 对 Contribution 2 措辞的批评是对的。建议改为：\"Building on the embedding-similarity criterion used for schema partitioning in prior work, we design controlled experiments that quantify its predictive relationship with extraction degradation...\"\n\n总结：同意 Contribution 2 措辞需修改，但框架层面的 experimental methodology 贡献是真实的，不应被低估。\n\n---\n\n**[AGREE with refinement] R2-N3: constrained decoding vs closed-set classification format 的区分**\n\n这是 R2 最锐利的观察。我完全同意 \"constrained decoding\" 不是正确的 boundary condition 描述。\n\n关键证据：NER **也使用** constrained decoding（JSON schema with enum types, §3.5 / Appendix K prompt templates），但 BCS 在 NER 上无 batch-level signal（r≈0, n=450, §4.4）。因此 constrained decoding 是 necessary but not sufficient condition。真正的区分是：\n\n- **RE**: closed-set single-label classification → 所有非 \"none\" 错误 必然是 intra-batch type substitution → BCS 直接预测 error rate\n- **NER**: open-set span extraction + type assignment → 错误分散在 boundary errors、missed entities、spurious entities、type substitution 多个模式 → BCS 仅预测其中 type substitution 子集，被其他 error modes 稀释\n\n论文的 Discussion §6 已经有类似分析（\"constrained decoding concentrates errors into type substitution\"），但术语 \"constrained decoding\" 不精确。RE 的 error channeling 来自 **classification format**（必须在给定选项中选一个），而非 constrained decoding 本身（NER 的 constrained decoding 约束的是 JSON 格式，不是 label 选择的排他性）。\n\n但我将此评为 **should-fix 而非 must-fix**，因为论文已经识别了正确的机制（error channeling），只是术语使用不够精确。修改 Discussion §6 的措辞即可解决。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Pairwise effect size 解释过于乐观**\n\n完全同意。我在自己的 N1 中也将此标记为 critical issue。r²=1.3-1.7% 用 behavioral research 标准来 justify 是类比不当——LLM 系统中 predictor 和 outcome 共享同一模型，理论上应有更强的对应关系。\n\n---\n\n**[PARTIALLY AGREE] R2-W2: 不同数据集使用不同 embedding**\n\n同意这引入了一个不必要的变量，我在自己的 Q3 中也提出了相同问题。但论文提供了技术理由（§3.2: MiniLM 384-d 对 Few-NERD 同类细粒度 types 区分不够）和 cross-embedding check（MiniLM r=0.172 vs Qwen3 r=0.138, confusion matrix correlation 0.894）。问题在于：如果 SCS 旨在作为 \"lightweight pre-hoc proxy\"（§3.2），embedding 选择不应需要对数据集特性的先验知识，这损害了 proxy 的通用性。\n\n建议：在 §3.2 中统一报告两种 embedding 的结果（至少对所有数据集都报告 MiniLM 结果），以 MiniLM 作为 primary，Qwen3 作为 sensitivity check。\n\n---\n\n**[REBUT] R2-W3: Introduction Contribution 3 将 NER null result framed 为 contribution**\n\n不同意 R2 的批评。Task asymmetry（RE: BCS 解释 22-53% variance vs NER: null batch-level signal despite significant pairwise effects）是本文最有价值的发现之一，原因：\n\n1. **对实践有直接指导意义**：告诉 NER practitioners 不要浪费时间在 confusability-aware batching 上，而应聚焦 count reduction（Discussion §6: \"reducing the number of candidate types per prompt is the primary lever\"）。\n2. **揭示了 task format 与 schema complexity 的交互**：这个发现推动了 \"error channeling hypothesis\"（Discussion §6），解释了为什么同一 metric 在不同 task 上表现不同，这是对 IE 领域的理论贡献。\n3. **Null results 在 controlled studies 中是 informative 的**：如果论文只报告 RE 的 positive results 而省略 NER 的 null results，反而会误导读者高估 BCS 的普适性。\n\nContribution 3 的 framing 合理——\"documenting a task asymmetry\" 不同于 \"documenting a failure\"。\n\n---\n\n**[PARTIALLY AGREE] R2-W4: MAVEN 的角色定位模糊**\n\n同意 MAVEN 在论文中的角色不够清晰。其 batch-level 结果为 positive（方向相反）→ 控制 confounders 后消失 → 主要贡献是 (1) pairwise analysis（Table 2: r=0.129, p<0.001）和 (2) centrality confound 的方法论案例（§4.5, Appendix D）。建议在 §3.1 MAVEN 描述中更明确地定位其为 \"supplementary dataset primarily for pairwise analysis and centrality confound demonstration\"。\n\n实际上论文已经在 §3.1 最后一句说了 \"MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level\"，但这个定位可以更早、更显著地出现。\n\n---\n\n**[AGREE] R2-W5: 页数可能超限**\n\n从 PDF 渲染来看，§7 Conclusion 出现在第 9 页上方，而 ACL Long Paper 正文限制为 8 页（Limitations/Ethics/References 不计入）。如果 Conclusion 确实在第 9 页，则超限。但 Conclusion 仅一段（约 5 行），通过压缩 Discussion 或 Results 中的冗余文字即可修复。这是一个 formatting issue，不影响科学内容。\n\n---\n\n### Questions 回应\n\n**R2-Q1: BCS 对 NER 是否缺乏实用价值？**\n\n是的，在 batch-level 上 BCS 对 NER 无预测价值。但论文已在 Discussion §6 给出替代实践建议（count reduction: ≤12 types/prompt），且 pairwise SCS 仍有诊断价值（识别容易混淆的 type pairs）。R2 的问题实际上是在问论文的 scope 是否过宽——我认为跨任务比较本身就是贡献（见我对 W3 的 rebut）。\n\n**R2-Q2: 真正的 boundary condition 是 constrained decoding 还是 closed-set classification format？**\n\n同意 R2，是后者。见我对 N3 的详细回应。\n\n**R2-Q3: 为什么不直接使用 16 val-only relations？**\n\n因为 16 types 的 BCS range 太窄，无法检测 confusability 效应。论文已展示：在 80-rel pool 中，full 80-type condition 的 BCS IQR 仅 0.033，导致 slope 不可解释（Table 4: slope=+0.221, p=0.76）。16 types 虽然有更宽的 BCS range（因为是 subset sampling），但 pool 仅 16 types 限制了 extreme-batch 构造的 BCS contrast（16-rel extreme gap 仅 -9.1pp vs 80-rel pool 的 -31.2pp, Appendix E Table 7）。合并 train+val 获得 80-type pool 是获取足够统计 power 的必要手段，且 split-origin covariate analysis（Appendix I）排除了 confound。R2 的建议不可行。\n\n**R2-Q4: Few-shot prompt length 是否被控制？**\n\n合理问题。Appendix L（§Few-Shot, Table 12）的 few-shot 实验在 count 8 上进行，每个 target type 采样 few-shot examples。1-shot 和 5-shot 下 prompt 长度差异较大，可能引入 lost-in-middle 效应。论文在 Appendix L 末尾提到了这一点（\"non-monotonic low-BCS pattern may reflect lost-in-middle effects from increased prompt length\"），但未做严格控制。这是一个 fair criticism。\n\n**R2-Q5: Cross-seed variance decomposition 的意义？**\n\nR2 似乎质疑这个分析的价值。我认为它是论文单种子设计的关键 justification：batch variance >> seed variance (5-474×) 证明 batch composition 是 primary variance source，使得单种子评估在捕获主要效应时是充分的。这直接回应了\"为什么不用多种子\"的自然质疑。\n\n---\n\n### Missing References 回应\n\n1. **Chen et al. (2026) \"Understanding LLM Performance Degradation in Multi-Instance Processing\"**: 如果该论文研究 LLM 在处理多实例时的性能退化，与本文的 count-dependent degradation 直接相关，应该引用。但需要确认该论文是否在 submission deadline 前 3 个月已公开（ARR reviewer guidelines 要求引用必须在 deadline 前 3 个月发表）。arXiv:2603.22608 的编号格式暗示 2026 年 3 月，而 ARR May 2025 cycle 的 deadline 是 2026-05-25，所以应该满足时间要求。**同意引用**（如果该论文确实存在且相关）。\n\n2. **Chroma Research \"Context Rot\"**: 不确定这是否为正式学术出版物。如果只是 blog post 或 technical report，在 *ACL venue 中引用不太合适。**需要确认出处**。\n\n3. **Schall & de Melo (2025)**: 已在论文中引用（\\cite{schall-2025-hidden-cost}，出现在 Discussion §6）。R2 认为讨论不足，我 partially agree——该论文关于 constrained decoding 隐性成本的发现直接支撑了本文的 error channeling hypothesis，值得在 Discussion 中多一句话的引用。\n\n---\n\n### 对 R2 Overall Assessment（3.0 Findings）的回应\n\nR2 给 3.0，我给 3.5。分歧主要在于：\n\n1. **新颖性评估**：R2 认为核心指标与 LLM-PEE 相同，框架是对已知现象的命名。我认为 experimental methodology（BCS-controlled design + TOST equivalence + within-pool analysis）构成实质方法论贡献，超越了 metric reuse 和 phenomenon naming。\n2. **NER null result 的价值**：R2 似乎不认为 task asymmetry 是 contribution。我认为这是论文最具 insight 的发现之一，推动了 error channeling hypothesis。\n3. **实践影响**：R2 认为无可行 mitigation 方案（SDGD 失败）削弱了论文价值。我认为 diagnostic 价值（knowing where and why things fail）对 Findings 而言已足够，尤其是论文给出了具体的实践建议（RE: SCS quartile screening; NER: ≤12 types/prompt）。\n\nR2 提出的写作和 framing 问题（N1 abstract, N2 novelty positioning, N3 constrained decoding terminology）均为 fixable issues，不应决定 accept/reject。\n\n我维持 **3.5（Borderline Conference）** 的评分。论文的方法论严谨性和 negative result 诊断价值使其超出 3.0（Findings）水平，但 R2 指出的 framing 和 scope 问题合理地限制了向 4.0 的上调。",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE with downgrade] R2-N1: Abstract 信息过载**\n\n同意 Abstract 试图覆盖过多发现（count decline、BCS for RE、NER null、few-shot、SDGD failure、cross-model），导致核心 \"so what\" 被淹没。但我将此定位为 **should-fix 而非 must-fix**。理由：\n\n1. Abstract 217 词在 150-250 词范围内，信息密度高但未超限。\n2. 对于一篇多任务、多数据集的实证分析论文，结果的复杂性（RE vs NER 不对称、negative results）天然要求更多 nuance。过度简化反而可能误导读者（如只报告 RE 的 22-53% R² 而不提 NER null result 会夸大普适性）。\n3. 核心问题不是信息量，而是叙事结构——应先给出 high-level takeaway（\"schema complexity predicts degradation through two partially separable dimensions, but the predictive structure is task-dependent\"），再选择性展开 1-2 个最强证据。\n\n总结：同意需要改写，但严重度降为 should-fix。\n\n---\n\n**[PARTIALLY AGREE] R2-N2: 核心新颖性主张需更诚实的定位**\n\n同意 SCS 指标本身与 LLM-PEE 的 embedding similarity 形式完全相同，论文自己在 §2 \"SCS novelty\" 段也承认了这一点（\"SCS shares its formal definition with the partitioning criterion used in LLM-PEE\"）。Contribution 2 的 \"we repurpose it as a predictive metric\" 表述确实暗示了指标层面的创新，需要调整措辞。\n\n但我 **rebut** R2 对框架贡献的低估：\n\n1. **从 engineering tool 到 analytical instrument 的转变不是 trivial 的**。LLM-PEE 将 embedding similarity 作为 partitioning heuristic（工程手段），本文将其转化为 predictive metric 并通过 controlled experiments 量化其解释力（R²=22-53%）和边界条件（RE yes, NER no, same-domain schemas confounded）。这个转变需要 BCS-controlled experimental design、TOST equivalence testing、within-pool analysis 等全套方法论，而非简单的 metric reuse。\n2. **\"两个维度\"不只是命名已知现象**。Li et al. (2023) 观察到 count-dependent degradation 但未分离 confusability；LLM-PEE 使用 embedding similarity 做 partitioning 但从未量化 confusability 对 accuracy 的独立预测力。本文的核心发现——\"count 和 confusability 在 RE 中是 largely additive 的\"（TOST p=0.003 at ±3pp）以及\"NER 中两者耦合\"——是 prior work 未曾建立的定量结论。\n3. 但 R2 对 Contribution 2 措辞的批评是对的。建议改为：\"Building on the embedding-similarity criterion used for schema partitioning in prior work, we design controlled experiments that quantify its predictive relationship with extraction degradation...\"\n\n总结：同意 Contribution 2 措辞需修改，但框架层面的 experimental methodology 贡献是真实的，不应被低估。\n\n---\n\n**[AGREE with refinement] R2-N3: constrained decoding vs closed-set classification format 的区分**\n\n这是 R2 最锐利的观察。我完全同意 \"constrained decoding\" 不是正确的 boundary condition 描述。\n\n关键证据：NER **也使用** constrained decoding（JSON schema with enum types, §3.5 / Appendix K prompt templates），但 BCS 在 NER 上无 batch-level signal（r≈0, n=450, §4.4）。因此 constrained decoding 是 necessary but not sufficient condition。真正的区分是：\n\n- **RE**: closed-set single-label classification → 所有非 \"none\" 错误 必然是 intra-batch type substitution → BCS 直接预测 error rate\n- **NER**: open-set span extraction + type assignment → 错误分散在 boundary errors、missed entities、spurious entities、type substitution 多个模式 → BCS 仅预测其中 type substitution 子集，被其他 error modes 稀释\n\n论文的 Discussion §6 已经有类似分析（\"constrained decoding concentrates errors into type substitution\"），但术语 \"constrained decoding\" 不精确。RE 的 error channeling 来自 **classification format**（必须在给定选项中选一个），而非 constrained decoding 本身（NER 的 constrained decoding 约束的是 JSON 格式，不是 label 选择的排他性）。\n\n但我将此评为 **should-fix 而非 must-fix**，因为论文已经识别了正确的机制（error channeling），只是术语使用不够精确。修改 Discussion §6 的措辞即可解决。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Pairwise effect size 解释过于乐观**\n\n完全同意。我在自己的 N1 中也将此标记为 critical issue。r²=1.3-1.7% 用 behavioral research 标准来 justify 是类比不当——LLM 系统中 predictor 和 outcome 共享同一模型，理论上应有更强的对应关系。\n\n---\n\n**[PARTIALLY AGREE] R2-W2: 不同数据集使用不同 embedding**\n\n同意这引入了一个不必要的变量，我在自己的 Q3 中也提出了相同问题。但论文提供了技术理由（§3.2: MiniLM 384-d 对 Few-NERD 同类细粒度 types 区分不够）和 cross-embedding check（MiniLM r=0.172 vs Qwen3 r=0.138, confusion matrix correlation 0.894）。问题在于：如果 SCS 旨在作为 \"lightweight pre-hoc proxy\"（§3.2），embedding 选择不应需要对数据集特性的先验知识，这损害了 proxy 的通用性。\n\n建议：在 §3.2 中统一报告两种 embedding 的结果（至少对所有数据集都报告 MiniLM 结果），以 MiniLM 作为 primary，Qwen3 作为 sensitivity check。\n\n---\n\n**[REBUT] R2-W3: Introduction Contribution 3 将 NER null result framed 为 contribution**\n\n不同意 R2 的批评。Task asymmetry（RE: BCS 解释 22-53% variance vs NER: null batch-level signal despite significant pairwise effects）是本文最有价值的发现之一，原因：\n\n1. **对实践有直接指导意义**：告诉 NER practitioners 不要浪费时间在 confusability-aware batching 上，而应聚焦 count reduction（Discussion §6: \"reducing the number of candidate types per prompt is the primary lever\"）。\n2. **揭示了 task format 与 schema complexity 的交互**：这个发现推动了 \"error channeling hypothesis\"（Discussion §6），解释了为什么同一 metric 在不同 task 上表现不同，这是对 IE 领域的理论贡献。\n3. **Null results 在 controlled studies 中是 informative 的**：如果论文只报告 RE 的 positive results 而省略 NER 的 null results，反而会误导读者高估 BCS 的普适性。\n\nContribution 3 的 framing 合理——\"documenting a task asymmetry\" 不同于 \"documenting a failure\"。\n\n---\n\n**[PARTIALLY AGREE] R2-W4: MAVEN 的角色定位模糊**\n\n同意 MAVEN 在论文中的角色不够清晰。其 batch-level 结果为 positive（方向相反）→ 控制 confounders 后消失 → 主要贡献是 (1) pairwise analysis（Table 2: r=0.129, p<0.001）和 (2) centrality confound 的方法论案例（§4.5, Appendix D）。建议在 §3.1 MAVEN 描述中更明确地定位其为 \"supplementary dataset primarily for pairwise analysis and centrality confound demonstration\"。\n\n实际上论文已经在 §3.1 最后一句说了 \"MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level\"，但这个定位可以更早、更显著地出现。\n\n---\n\n**[AGREE] R2-W5: 页数可能超限**\n\n从 PDF 渲染来看，§7 Conclusion 出现在第 9 页上方，而 ACL Long Paper 正文限制为 8 页（Limitations/Ethics/References 不计入）。如果 Conclusion 确实在第 9 页，则超限。但 Conclusion 仅一段（约 5 行），通过压缩 Discussion 或 Results 中的冗余文字即可修复。这是一个 formatting issue，不影响科学内容。\n\n---\n\n### Questions 回应\n\n**R2-Q1: BCS 对 NER 是否缺乏实用价值？**\n\n是的，在 batch-level 上 BCS 对 NER 无预测价值。但论文已在 Discussion §6 给出替代实践建议（count reduction: ≤12 types/prompt），且 pairwise SCS 仍有诊断价值（识别容易混淆的 type pairs）。R2 的问题实际上是在问论文的 scope 是否过宽——我认为跨任务比较本身就是贡献（见我对 W3 的 rebut）。\n\n**R2-Q2: 真正的 boundary condition 是 constrained decoding 还是 closed-set classification format？**\n\n同意 R2，是后者。见我对 N3 的详细回应。\n\n**R2-Q3: 为什么不直接使用 16 val-only relations？**\n\n因为 16 types 的 BCS range 太窄，无法检测 confusability 效应。论文已展示：在 80-rel pool 中，full 80-type condition 的 BCS IQR 仅 0.033，导致 slope 不可解释（Table 4: slope=+0.221, p=0.76）。16 types 虽然有更宽的 BCS range（因为是 subset sampling），但 pool 仅 16 types 限制了 extreme-batch 构造的 BCS contrast（16-rel extreme gap 仅 -9.1pp vs 80-rel pool 的 -31.2pp, Appendix E Table 7）。合并 train+val 获得 80-type pool 是获取足够统计 power 的必要手段，且 split-origin covariate analysis（Appendix I）排除了 confound。R2 的建议不可行。\n\n**R2-Q4: Few-shot prompt length 是否被控制？**\n\n合理问题。Appendix L（§Few-Shot, Table 12）的 few-shot 实验在 count 8 上进行，每个 target type 采样 few-shot examples。1-shot 和 5-shot 下 prompt 长度差异较大，可能引入 lost-in-middle 效应。论文在 Appendix L 末尾提到了这一点（\"non-monotonic low-BCS pattern may reflect lost-in-middle effects from increased prompt length\"），但未做严格控制。这是一个 fair criticism。\n\n**R2-Q5: Cross-seed variance decomposition 的意义？**\n\nR2 似乎质疑这个分析的价值。我认为它是论文单种子设计的关键 justification：batch variance >> seed variance (5-474×) 证明 batch composition 是 primary variance source，使得单种子评估在捕获主要效应时是充分的。这直接回应了\"为什么不用多种子\"的自然质疑。\n\n---\n\n### Missing References 回应\n\n1. **Chen et al. (2026) \"Understanding LLM Performance Degradation in Multi-Instance Processing\"**: 如果该论文研究 LLM 在处理多实例时的性能退化，与本文的 count-dependent degradation 直接相关，应该引用。但需要确认该论文是否在 submission deadline 前 3 个月已公开（ARR reviewer guidelines 要求引用必须在 deadline 前 3 个月发表）。arXiv:2603.22608 的编号格式暗示 2026 年 3 月，而 ARR May 2025 cycle 的 deadline 是 2026-05-25，所以应该满足时间要求。**同意引用**（如果该论文确实存在且相关）。\n\n2. **Chroma Research \"Context Rot\"**: 不确定这是否为正式学术出版物。如果只是 blog post 或 technical report，在 *ACL venue 中引用不太合适。**需要确认出处**。\n\n3. **Schall & de Melo (2025)**: 已在论文中引用（\\cite{schall-2025-hidden-cost}，出现在 Discussion §6）。R2 认为讨论不足，我 partially agree——该论文关于 constrained decoding 隐性成本的发现直接支撑了本文的 error channeling hypothesis，值得在 Discussion 中多一句话的引用。\n\n---\n\n### 对 R2 Overall Assessment（3.0 Findings）的回应\n\nR2 给 3.0，我给 3.5。分歧主要在于：\n\n1. **新颖性评估**：R2 认为核心指标与 LLM-PEE 相同，框架是对已知现象的命名。我认为 experimental methodology（BCS-controlled design + TOST equivalence + within-pool analysis）构成实质方法论贡献，超越了 metric reuse 和 phenomenon naming。\n2. **NER null result 的价值**：R2 似乎不认为 task asymmetry 是 contribution。我认为这是论文最具 insight 的发现之一，推动了 error channeling hypothesis。\n3. **实践影响**：R2 认为无可行 mitigation 方案（SDGD 失败）削弱了论文价值。我认为 diagnostic 价值（knowing where and why things fail）对 Findings 而言已足够，尤其是论文给出了具体的实践建议（RE: SCS quartile screening; NER: ≤12 types/prompt）。\n\nR2 提出的写作和 framing 问题（N1 abstract, N2 novelty positioning, N3 constrained decoding terminology）均为 fixable issues，不应决定 accept/reject。\n\n我维持 **3.5（Borderline Conference）** 的评分。论文的方法论严谨性和 negative result 诊断价值使其超出 3.0（Findings）水平，但 R2 指出的 framing 和 scope 问题合理地限制了向 4.0 的上调。",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1115 · 2026-05-18T09:26:39.901672+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4530
}
```

</details>

---


### Assistant

_source line 1116 · 2026-05-18T09:26:48.473922+00:00_

交叉回应已提交。总结：

**与 R2 的主要分歧点：**
- R2-N2（新颖性）：我认为 experimental methodology 贡献被 R2 低估，但同意 Contribution 2 措辞需修改
- R2-W3（NER null result 作为 contribution）：我 rebut——task asymmetry 是本文最有 insight 的发现之一
- R2 Overall 3.0 vs 我的 3.5：分歧在于方法论贡献和 negative result 诊断价值的权重

**与 R2 的主要共识：**
- N1（abstract 信息过载）：同意需改写，但降级为 should-fix
- N3（constrained decoding vs closed-set format）：完全同意这个区分，是 R2 最锐利的观察
- W1（pairwise effect size 解释乐观）：与我自己的 N1 一致
- W2（不同 embeddings）：与我的 Q3 一致
- W5（页数超限）：从 PDF 渲染确认 Conclusion 在第9页，需修复

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 38

## Round 38

38 recorded events


### User

_source line 1117 · 2026-05-18T09:57:13.970952+00:00_

[Round 1 审稿请求]:
你是 Round 19 Reviewer 1。审查侧重：**方法严谨性 + 实验设计 + R18 修复验证**。

## Venue 信息
- **目标**: EMNLP 2026 via ARR (May 25 cycle), Findings
- **格式**: ACL 模板, Long paper 8 页正文（不含 Limitations/Ethics/References）, double-blind
- **评分标准**: 5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit

## 论文路径
`projects/schema-dag-extraction/docs/paper/main.tex`（含 \input 的所有 section 文件）

## 论文概要
研究 training-free LLM IE 中 schema 复杂度如何预测性能退化，将退化分解为 count (Dim 1) 和 confusability (Dim 2) 两个维度。提出 SCS/BCS 量化 confusability，在 FewRel/DocRED/Few-NERD/MAVEN 上实验。BCS 在 RE 上解释 22-53% batch 间方差，NER 上无 batch 级信号。Schema decomposition (SDGD) 失败。

## R18 Open/In-Progress Issues（重点核查是否已修复）

### Critical
1. **R18-N1**: BCS batch-level 仅限 RE forced-choice classification format，非 constrained decoding。NER 也用 constrained decoding (JSON enum) 但无信号。→ 检查全文是否已精确区分 forced-choice classification format vs constrained decoding。
2. **R18-N2**: "Two separable dimensions" 在 logit-scale 上 inconclusive。→ 检查全文是否统一改为 "largely additive with bounded interaction"。
3. **R18-N3**: Contribution 2 暗示 metric innovation。→ 检查是否已改为 methodology contribution。

### Warning
4. **R18-W2**: Pairwise r²=1.3-1.7% 引用 Cohen (1988) 套用到 LLM 系统需额外论证。
5. **R18-W5**: Dimension 2 未在 proprietary model (Gemini) 上验证。Limitations 是否说明。
6. **R18-W7**: BCS-aware grouping 无显著优势 (+1.4pp)。SDGD section 是否加了 "marginal BCS reduction" 解释。
7. **R17-W3**: Typical-batch 2.2pp 实际意义有限。Practical implications 是否更坦诚。

## 你的审查重点

1. **R18 修复验证**: 逐条检查上述 issues 的修复质量，标记 [FIXED]、[PARTIALLY FIXED]、[NOT FIXED]
2. **实验设计严谨性**: BCS-controlled 设计、TOST equivalence、within-pool analysis、cross-model validation 的方法论质量
3. **统计分析**: effect sizes、CI、p-values 的解释是否恰当；logit-scale TOST 在正文中是否被提及
4. **因果 vs 相关性语言**: 全文是否避免了超出证据的因果表述
5. **新问题**: 是否有修改引入的新问题

## 输出格式
按以下结构输出审稿意见：
```
## R18 修复验证
[逐条 FIXED/PARTIALLY FIXED/NOT FIXED + 简要说明]

## Strengths (逐条)
## Weaknesses (逐条, 标 critical/warning/info)
## Questions
## Missing References
## Scores
- Soundness: X/5
- Excitement: X/5
- Reproducibility: X/5
- Overall: X (用 EMNLP 2026 评分标准)
- Confidence: X/5
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1118 · 2026-05-18T09:57:22.677522+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1119 · 2026-05-18T09:57:23.079970+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 (count-associated decline) has been validated on a proprietary model (Gemini 2.5 Flash, $\rho = -0.900$, $p = 0.037$; Appendix~\ref{sec:appendix_cross_model_gemini}); Dimension~2 (confusability-associated type substitution) has been verified only on open-weight models. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). A FewRel factorial with TOST equivalence testing is consistent with bounded interaction under the primary linear specification ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp); however, the logit-scale TOST is inconclusive ($p = 0.209$). At $n =
…[truncated 52682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1120 · 2026-05-18T09:57:25.088465+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find all tex input files",
  "prompt": "Find all .tex files under /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/. I need both the file paths and to understand the structure. Use glob to find all .tex files, then read main.tex to find all \\input commands to understand the paper structure. Report the full list of file paths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find all tex input files",
    "prompt": "Find all .tex files under /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/. I need both the file paths and to understand the structure. Use glob to find all .tex files, then read main.tex to find all \\input commands to understand the paper structure. Report the full list of file paths."
  }
}
```

</details>

---


### Tool call

_source line 1121 · 2026-05-18T09:57:25.189407+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1122 · 2026-05-18T09:57:25.240209+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1123 · 2026-05-18T09:57:26.647226+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 1124 · 2026-05-18T09:57:26.647561+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1125 · 2026-05-18T09:57:28.254320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1126 · 2026-05-18T09:57:28.556609+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 (count-associated decline) has been validated on a proprietary model (Gemini 2.5 Flash, $\rho = -0.900$, $p = 0.037$; Appendix~\ref{sec:appendix_cross_model_gemini}); Dimension~2 (confusability-associated type substitution) has been verified only on open-weight models. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). A FewRel factorial with TOST equivalence testing is consistent with bounded interaction under the primary linear specification ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp); however, the logit-scale TOST is inconclusive ($p = 0.209$). At $n =
…[truncated 52682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-18T09:57:35.409133+00:00_

Perfect! I've found all the .tex files and examined the main.tex file to understand the paper structure. Here's my complete report:

## Full List of .tex Files in the Paper Directory

**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/`

1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex` (main file)
2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex`
3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex`
4. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex`
5. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex`
6. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex`
7. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex`
8. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex`
9. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex`
10. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex`
11. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex`

## Paper Structure Based on main.tex \input Commands

The main.tex file includes the following documents in order:

1. **abstract.tex** - Paper abstract
2. **introduction.tex** - Introduction section
3. **related_work.tex** - Related work section
4. **experimental_setup.tex** - Experimental setup section
5. **results.tex** - Results section
6. **sdgd_negative.tex** - Schema-Guided Decomposition negative results section
7. **discussion.tex** - Discussion se
…[truncated 667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 10320
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-18T09:57:40.330476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-18T09:57:40.832952+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets. We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two largely additive dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution. BCS explains 22--53\% of cross-batch RE accuracy variance under RE's forced-choice format but shows no batch-level signal for NER, where errors scatter across missed entities and boundary failures. Few-shot demonstrations widen the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Confusability is a schema-structural property: effects replicate across model scales and families, and persist under varied prompt designs.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1130 · 2026-05-18T09:57:40.833304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1131 · 2026-05-18T09:57:41.336935+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
…[truncated 3119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1132 · 2026-05-18T09:57:41.337314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1133 · 2026-05-18T09:57:41.789267+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and fine-grained entity typing \cite{gillick-2014-entity-typing}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. \citet{wei-2023-chatie} reformulate zero-shot IE as multi-turn QA with ChatGPT but do not analyze schema-size effects.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definit
…[truncated 3641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1134 · 2026-05-18T09:57:41.789637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 1135 · 2026-05-18T09:57:42.293897+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate th
…[truncated 8243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 1136 · 2026-05-18T09:57:42.294369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1137 · 2026-05-18T09:57:42.797213+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\pm 1$\,SD across 3 seeds (42, 123, 456) $\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}); schema configura
…[truncated 11235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-18T09:57:42.797707+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 1139 · 2026-05-18T09:57:43.701535+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapse (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.): graph coloring achieves only marginal mean BCS reduction (0.559$\to$0.552), insufficient to produce detectable accuracy improvement. All practical routing strategies fall below the single-pass baseline (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Promising avenues include coarse-to-fine pipelines, retrieval-based routing, and calibrated generation \citep{jagannatha2020calibrating} to recover confidence signals.
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-18T09:57:43.802249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1141 · 2026-05-18T09:57:43.903092+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED slope $-$0.71, adjusted $R^2 = 0.51$, $n = 35$; 95\% CI [0.27, 0.73]) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%); conditional on nonzero confusion (${\sim}11\%$ of pairs), $R^2$ rises to 7\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\% (Monte Carlo simulation with parameters derived from the observed data; this simulation serves as an internal consistency check rather than independent evidence; Appendix~\ref{app:aggregation-sim}), consistent with observed RE values.
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific ($R^2 = 0.22$--$0.53$ vs.\ $r \approx 0$ for NER, $n = 450$). RE uses a forced-choice classification format where each instance maps to exactly one relation type; all non-null errors are necessarily type substitutions \cite{tam-2024-let-me-speak}, which makes BCS predictive. NER, despite also using constrained decoding on the type enum, produces multi-span output where errors scatter across missed entities, boundary misalignment, and type confusion, diluting the BCS signal. This format asymmetry is a boundary condition for our batch-level findings \cite{schall-2025-hidden-cost}: BCS predicts accuracy when task format channels errors into type substitution, but loses signal when errors distribute across multiple failure modes. We hypothesize the NER U-s
…[truncated 1468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1142 · 2026-05-18T09:57:43.903609+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 1143 · 2026-05-18T09:57:51.691321+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the web search results, here's information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified 
…[truncated 1207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7787
}
```

</details>

---


### Tool call

_source line 1144 · 2026-05-18T09:57:58.066744+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring dimensions, their scales, and descriptions. I need every field: soundness, excitement, overall assessment, confidence, reproducibility, and any other dimensions with their exact scale descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring dimensions, their scales, and descriptions. I need every field: soundness, excitement, overall assessment, confidence, reproducibility, and any other dimensions with their exact scale descriptions."
  }
}
```

</details>

---


### Tool call

_source line 1145 · 2026-05-18T09:57:59.473034+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including: what reviewers should look for, how to evaluate soundness, excitement, methodology, experiments, and any specific guidance on scoring. Include all criteria and scoring rubrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including: what reviewers should look for, how to evaluate soundness, excitement, methodology, experiments, and any specific guidance on scoring. Include all criteria and scoring rubrics."
  }
}
```

</details>

---


### Tool result

_source line 1146 · 2026-05-18T09:58:05.582948+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: Quite sure with careful checking; unlikely but possible missed details
- 3: Pretty sure; may have missed specifics despite general familiarity
- 2: Willing to defend evaluation; fairly likely some details missed
- 1: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- 5: Excellent; "one of the most thorough I have seen"
- 4: Strong; sufficient support with optional additional experiments
- 3: Acceptable; supports main claims with minor gaps
- 2: Poor; main claims lack sufficient support; major technical problems
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- 5: Highly exciting; would recommend to others
- 4: Exciting; "would mention this paper to others"
- 3: Interesting; might discuss selectively
- 2: Potentially interesting but doesn't resonate personally
- 1: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5: Consider for Award (top 2.5%)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- 5: Results easily reproducible
- 4: Mostly reproducible with minor variations possible
- 3: Reproducible with difficulty; underspecified parameters
- 2: Very difficult; unavailable data or insufficient details
- 1: "would not be able to reproduce the results"

## 6. **Datasets** (if applicable)
Scale: 1-5
- 5: Enabling; affects research project selection
- 4: Useful for ongoing work
- 3: Potentially useful
- 2: Documentary value
- 1: No usable datasets

## 7. **Software** (if applicable)

…[truncated 388 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7516
}
```

</details>

---


### Tool result

_source line 1147 · 2026-05-18T09:58:11.104110+00:00_

# ARR Reviewer Guidelines Summary

## Core Responsibilities

Reviewers must complete four main tasks: (1) allocate review time, (2) verify assignment suitability, (3) write substantive reviews, and (4) engage with author responses.

## Evaluation Framework

### Three-Score System (as of February 2025)

**Soundness**: Technical quality and validity. Scores must be justified by review text. Low soundness requires explicit fault identification.

**Excitement**: Personal interest level, independent from soundness assessment. Subjective preferences belong here rather than factual criticism.

**Overall Recommendation**: Composite judgment reflecting soundness, excitement, novelty, and potential impact—orthogonal concepts that shouldn't be conflated.

## What to Evaluate

### Methodology Assessment (M-codes)

- **M1**: LLM evaluators require validation in their specific context
- **M2**: Reproducibility demands sufficient detail, hyperparameters, and code availability plans
- **M3**: Data quality issues must be disclosed if discovered
- **M4**: Model/benchmark selection needs clear justification aligned with claims
- **M5**: Formal proofs require completeness; assumptions must be explicit

### Experimental Results (R-codes)

- **R1**: Statistics and data presentation; detection of p-hacking or prompt engineering bias
- **R2**: Claims must match evaluation scope (benchmark ≠ general capability)
- **R3**: Speculations must be labeled as such, not conclusions
- **R4**: Avoid overclaiming beyond evidence
- **R5**: Statistical significance testing with confidence intervals preferred

### General Issues (G-codes)

- **G1**: Research questions and contributions must be explicitly stated
- **G2**: Methodological choices shouldn't rely on unsound precedents
- **G3**: Related work must fairly represent prior contributions
- **G4**: Key terms require clear definitions
- **G5**: Citations must accurately represent cited work

## Common Reviewer Biases to Avoid (H-codes)

Reviewers sho
…[truncated 1898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 11631
}
```

</details>

---


### Tool call

_source line 1148 · 2026-05-18T09:59:41.149036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 1149 · 2026-05-18T09:59:41.250002+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{lla
…[truncated 4608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1150 · 2026-05-18T09:59:46.574755+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
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

_source line 1151 · 2026-05-18T09:59:46.625365+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-18T10:01:27.621150+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Round 19 Reviewer 1 审稿意见\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**审查侧重**: 方法严谨性 + 实验设计 + R18 修复验证\n\n---\n\n## R18 修复验证\n\n**R18-N1 [FIXED]**: forced-choice classification format vs constrained decoding 区分。\n全文已精确区分。Abstract 写 \"under RE's forced-choice format\"；Discussion §6 明确对比 \"RE uses a forced-choice classification format...NER, despite also using constrained decoding on the type enum\"；Limitations item 9 写 \"BCS batch-level prediction is demonstrated only under RE's forced-choice classification format\"；Conclusion 写 \"under forced-choice classification\"。术语使用一致且准确。\n\n**R18-N2 [FIXED]**: \"two separable dimensions\" → \"largely additive with bounded interaction\"。\nAbstract/Introduction/Conclusion 统一使用 \"largely additive dimensions\"。Introduction Finding (1) 明确写 \"logit-scale inconclusive\"。Results §4.4 报告 TOST 三个 margin 水平 (±3pp p=0.003, ±2pp p=0.047, ±1pp p=0.278) 及 logit-scale TOST (p=0.209)。NER 的 coupling 在 Introduction 和 Conclusion 中均被提及。\n\n**R18-N3 [FIXED]**: Contribution 2 从 metric innovation 改为 methodology contribution。\nContribution 2 现在写 \"Building on the embedding-similarity criterion used for schema partitioning in prior work, we design controlled experiments that isolate confusability from count\"。Related Work SCS novelty 段进一步澄清 \"Our contribution is not the metric itself but the controlled experimental framework\"。Framing 正确。\n\n**R18-W2 [PARTIALLY FIXED]**: Cohen (1988) 套用到 LLM 系统。\nRelated Work 现在加了 hedging: \"thresholds for 'practically meaningful' may differ in LLM systems where aggregation amplifies small per-instance biases\"。承认了标准不可直接迁移，但仍然以 behavioral research 的 \"small but real\" 框架作为锚定。建议进一步：要么找到 NLP/LLM 领域有 effect size 解读先例的文献，要么明确说明这是 tentative analogy。\n\n**R18-W5 [FIXED]**: Dimension 2 未在 proprietary model 上验证。\nLimitations item 1 明确写 \"Dimension 2 has been verified only on open-weight models\"。Appendix §H (Gemini) 结尾也写 \"cross-architecture Dimension 2 validation remains for future work\"。\n\n**R18-W7 [FIXED]**: BCS-aware grouping +1.4pp 无显著优势的解释。\nSDGD §5 现在写 \"graph coloring achieves only marginal mean BCS reduction (0.559→0.552), insufficient to produce detectable accuracy improvement\"。因果链清晰：BCS 降幅太小 → 精度差异不显著。\n\n**R17-W3 [PARTIALLY FIXED]**: Typical-batch 2.2pp 实际意义有限。\nResults §4.3 transparent 报告了 2.2pp (95% CI [0.4, 4.0]) 和 \"roughly 7% of the extreme-batch gap\"。Discussion practical implications 段承认 \"3-5pp expected impact\" 并加了 \"diagnostic guidelines derived from correlational evidence; practitioners should validate on their specific schema\"。但 Abstract 和 Introduction 的叙事仍侧重 extreme-batch 数字 (31.2pp, -49pp) 而非 typical-batch 的 modest effect，读者可能高估实际影响。\n\n---\n\n## Strengths\n\n**S1. 实验设计严谨，控制变量到位。**\nBCS-controlled 设计在固定 count 的前提下变化 confusability，是该研究问题的正确方法论选择。Within-pool analysis (§4.3, Table 5) 用 80-pool 内采样 16-relation 子集排除 pool composition confound，permutation test p=0.60 证实 slope consistency。FewRel 的 balanced design (700 instances/type) 消除了 type frequency confound。这些控制在 training-free IE 文献中是少见的。\n\n**S2. 统计分析全面且透明。**\nTOST equivalence testing 用三个 margin 水平报告 (Table 8)，logit-scale sensitivity 单独报告且承认 inconclusive，bootstrap CIs 区分了 pair-level (B=10,000) 和 batch-level (B=1,000)，variance decomposition (Appendix Table 11) 量化了 batch vs seed 方差比。这种统计透明度在 NLP 实证论文中罕见。\n\n**S3. 负面结果的诚实报告。**\nSDGD 失败、NER batch-level null、MAVEN centrality confound、logit-scale inconclusive、few-shot widening gap 均被如实报告并分析原因。这增强了正面结果的可信度。\n\n**S4. 跨模型验证覆盖面广。**\nQwen3-32B (primary) + Llama-3.1-8B + 70B (FP8) + Gemini 2.5 Flash (API)，覆盖 open-weight 和 proprietary、8B-70B+ 规模。Dimension 1 在所有模型上复现；Dimension 2 在 RE 上跨 8B/32B/70B 复现。\n\n**S5. Robustness checks 充分。**\nPrompt variants (4 种, Appendix Table 10)、BCS aggregation (mean vs max, Appendix Table 7)、embedding ablation (name vs name+def, Appendix Table 12)、SCS baselines (Levenshtein, WordNet, same-parent, Appendix Table 14)、held-out validation (16 val-origin types, Appendix §K)、split-origin covariate (Appendix §L)。每个 potential confound 都有对应的控制分析。\n\n---\n\n## Weaknesses\n\n**N1 [warning] TOST margin 选择与 main effect 的关系需更多论证。**\n- 具体位置: §4.4, Appendix §C\n- 问题: ±3pp TOST margin 的 empirical anchor 是 \"typical random-batch confusability variation produces 2-5pp accuracy differences\"，但 typical-batch confusability main effect 本身仅 2.2pp。用 ±3pp margin 证明 interaction bounded 意味着 interaction 可以高达 main effect 的 136% (3/2.2) 而仍被认为 \"bounded\"。±2pp 是 marginal (p=0.047)，±1pp inconclusive。在 logit scale 上也 inconclusive (p=0.209)。\n- \"largely additive\" 的 claim 实质上是: interaction 在 linear scale 上 bounded below 2-3pp, 但无法排除 interaction 接近甚至超过 main effect 的 magnitude。这使 \"largely additive\" 的表述偏乐观。\n- 建议: Abstract 中 \"two largely additive dimensions\" 应加限定词，如 \"under RE's forced-choice format on the linear scale\"；或将 hedging 从 Appendix 提到正文。\n\n**N2 [warning] Abstract/Introduction 的叙事偏重 extreme-batch 数字，淡化 typical-batch modest effect。**\n- 具体位置: Abstract, §1\n- 问题: Abstract 写 \"BCS explains 22-53% of cross-batch RE accuracy variance\"，Introduction 列 \"-31.2pp\" extreme-batch gap 和 \"3.9-5.3pp quartile gaps\"。但 typical batching 下的 expected gap 仅 2.2pp (CI [0.4, 4.0])，且 NER 上 batch-level signal 为零。读者从 Abstract/Introduction 获得的 impression 与 typical real-world impact 之间有落差。\n- 建议: Abstract 中加一句 typical-batch magnitude（如 \"though typical batches yield modest 2.2pp gaps\"），使核心 message 更 calibrated。\n\n**N3 [warning] NER batch-level null 削弱了 \"two-dimensional\" 框架的普适性。**\n- 具体位置: §4.3, §4.4, §6\n- 问题: 论文的核心 framing 是 \"two-dimensional degradation\"（count + confusability）。但 Dimension 2 在 batch level 仅对 RE 有效，NER 上 r≈0 (n=450)。论文解释这是因为 NER 的 error 分散在 missed entities 和 boundary failures 上，但这意味着 \"two-dimensional\" 框架对 NER 仅在 pairwise level 成立（r²=1.3%），batch-level 没有 actionable signal。\n- 对于 EMNLP 读者来说，NER 是比 RE classification 更 mainstream 的 IE task。框架对 NER batch-level 无预测力是一个 significant boundary condition。\n- 建议: 论文已经在多处承认了这一点（Discussion, Limitations），但 title 和 abstract 的 framing 仍暗示 two-dimensional decomposition 是 general 的。\n\n**N4 [info] Monte Carlo simulation 的 evidential status 需要更清晰。**\n- 具体位置: Appendix §I\n- 问题: 论文正确地将 simulation 标注为 \"illustrative explanatory model\" 和 \"internal consistency check\"。但 Discussion §6 引用 \"Monte Carlo simulation with parameters derived from the observed data\" 时，尽管加了 caveat，仍可能给人 independent corroboration 的印象。Simulation 用 conditional R²=7%（仅 non-zero confusion pairs）匹配 observed batch R²=0.218，但 unconditional R²=1.3% 只能产生 simulated batch R²=0.044。这个 ~5× gap 的解释（89% zero-confusion pairs dilution）虽合理，但 conditioning on the outcome variable 是一个 methodological concern。\n- 建议: 正文引用 simulation 时删去具体数字，仅保留 \"post-hoc simulation confirms the aggregation pattern is consistent\"。\n\n**N5 [info] Few-shot 实验中 5-shot low-BCS 回落的解释不够充分。**\n- 具体位置: Appendix §N, Table 15\n- 问题: 1-shot low-BCS = 0.754, 5-shot low-BCS = 0.715 (-3.9pp)。论文归因于 \"lost-in-middle effects from increased prompt length\"，但这只是推测，未做控制实验验证。如果 low-BCS 在 5-shot 下回落是 prompt length effect，那 high-BCS 5-shot 也应受类似影响——但 high-BCS 从 0.554 (1-shot) 降到 0.488 (5-shot) 的降幅 (-6.6pp) 更大。两组不对称的降幅可能有 confusability-specific 的解释，而非仅仅是 prompt length。\n- 建议: 承认 non-monotonic pattern 的解释是 speculative。\n\n**N6 [info] Prompt variant analysis 的 multiple comparison 处理。**\n- 具体位置: Appendix §G, Table 10\n- 问题: 8 个 tests (4 variants × 2 count levels) 在同一 dataset 上进行。论文不做 Bonferroni，理由是 \"correlated prompt variants testing the same underlying signal\" (citing Rothman 1990)。Rothman (1990) 讨论的是 independent replications across different populations，而这里是 same dataset + same batches + different prompts，相关性方向是 positive (同一 batch 在不同 prompt 下的 accuracy 正相关)。Positive correlation 会 inflate directional consistency 而 deflate individual p-values。7/8 directional consistency 在 positively correlated tests 下的 evidential value 低于独立情况。\n- 建议: 加一句说明 positive correlation 对 directional consistency 的影响。\n\n---\n\n## Questions\n\n**Q1.** Table 2 (pairwise correlation) 排除了 FewRel，理由是 \"RE's per-instance format precludes direct comparison of confusion rates\"。但 §3.2 validation paragraph 和 Appendix Table 14 都报告了 FewRel 的 pairwise SCS-confusion ρ=0.218/0.187。这两个说法是否矛盾？如果 FewRel 可以计算 pairwise confusion，为什么 Table 2 排除它？\n\n**Q2.** Variance decomposition (Appendix Table 11) 中 count=16 的 seed SD (0.027) 显著高于其他 count levels (0.010-0.019 range)。这个异常值是否影响了 count=16 BCS-controlled 实验的结论？\n\n**Q3.** BCS independence analysis (Appendix §M) 报告 BCS unique R²=0.259, composition unique R²=0.298, shared=0.147。Shared variance 占 20.9%，这意味着 BCS 和 type difficulty 不是完全正交的。在 BCS-controlled 实验中，是否控制了 mean type difficulty？\n\n---\n\n## Missing References\n\n- 无明显遗漏。Related work 覆盖了 training-free IE、schema decomposition、constrained decoding、label confusion 等主要方向。引用密度符合 ACL venue 标准。\n\n---\n\n## Scores\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨，统计分析全面透明；但 \"largely additive\" 在 logit scale 上 inconclusive，TOST margin 选择与 main effect magnitude 的关系需论证，NER batch-level null 削弱框架普适性 |\n| Excitement | 2.5/5 | 分析框架有价值（controlled isolation of count vs confusability），但 typical-batch effect modest (2.2pp)，NER 无 batch-level signal，schema decomposition 失败，practical takeaway 有限 |\n| Reproducibility | 4/5 | 详细的实验描述（decoding params, seed, batch sizes, bootstrap params），code promised upon acceptance，prompt templates in appendix；单 GPU 可复现 |\n| Overall | 3.0 (Findings) | 方法论严谨的实证研究，controlled experimental design 在 training-free IE 文献中是有价值的贡献。但 practical impact limited (2.2pp typical), NER batch-level null, schema decomposition failure, 以及 \"largely additive\" claim 的 logit-scale caveat 限制了 excitement。适合 Findings。 |\n| Confidence | 4/5 | 仔细阅读了全文和 appendix，熟悉实验方法论和统计检验 |\n",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Round 19 Reviewer 1 审稿意见\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**审查侧重**: 方法严谨性 + 实验设计 + R18 修复验证\n\n---\n\n## R18 修复验证\n\n**R18-N1 [FIXED]**: forced-choice classification format vs constrained decoding 区分。\n全文已精确区分。Abstract 写 \"under RE's forced-choice format\"；Discussion §6 明确对比 \"RE uses a forced-choice classification format...NER, despite also using constrained decoding on the type enum\"；Limitations item 9 写 \"BCS batch-level prediction is demonstrated only under RE's forced-choice classification format\"；Conclusion 写 \"under forced-choice classification\"。术语使用一致且准确。\n\n**R18-N2 [FIXED]**: \"two separable dimensions\" → \"largely additive with bounded interaction\"。\nAbstract/Introduction/Conclusion 统一使用 \"largely additive dimensions\"。Introduction Finding (1) 明确写 \"logit-scale inconclusive\"。Results §4.4 报告 TOST 三个 margin 水平 (±3pp p=0.003, ±2pp p=0.047, ±1pp p=0.278) 及 logit-scale TOST (p=0.209)。NER 的 coupling 在 Introduction 和 Conclusion 中均被提及。\n\n**R18-N3 [FIXED]**: Contribution 2 从 metric innovation 改为 methodology contribution。\nContribution 2 现在写 \"Building on the embedding-similarity criterion used for schema partitioning in prior work, we design controlled experiments that isolate confusability from count\"。Related Work SCS novelty 段进一步澄清 \"Our contribution is not the metric itself but the controlled experimental framework\"。Framing 正确。\n\n**R18-W2 [PARTIALLY FIXED]**: Cohen (1988) 套用到 LLM 系统。\nRelated Work 现在加了 hedging: \"thresholds for 'practically meaningful' may differ in LLM systems where aggregation amplifies small per-instance biases\"。承认了标准不可直接迁移，但仍然以 behavioral research 的 \"small but real\" 框架作为锚定。建议进一步：要么找到 NLP/LLM 领域有 effect size 解读先例的文献，要么明确说明这是 tentative analogy。\n\n**R18-W5 [FIXED]**: Dimension 2 未在 proprietary model 上验证。\nLimitations item 1 明确写 \"Dimension 2 has been verified only on open-weight models\"。Appendix §H (Gemini) 结尾也写 \"cross-architecture Dimension 2 validation remains for future work\"。\n\n**R18-W7 [FIXED]**: BCS-aware grouping +1.4pp 无显著优势的解释。\nSDGD §5 现在写 \"graph coloring achieves only marginal mean BCS reduction (0.559→0.552), insufficient to produce detectable accuracy improvement\"。因果链清晰：BCS 降幅太小 → 精度差异不显著。\n\n**R17-W3 [PARTIALLY FIXED]**: Typical-batch 2.2pp 实际意义有限。\nResults §4.3 transparent 报告了 2.2pp (95% CI [0.4, 4.0]) 和 \"roughly 7% of the extreme-batch gap\"。Discussion practical implications 段承认 \"3-5pp expected impact\" 并加了 \"diagnostic guidelines derived from correlational evidence; practitioners should validate on their specific schema\"。但 Abstract 和 Introduction 的叙事仍侧重 extreme-batch 数字 (31.2pp, -49pp) 而非 typical-batch 的 modest effect，读者可能高估实际影响。\n\n---\n\n## Strengths\n\n**S1. 实验设计严谨，控制变量到位。**\nBCS-controlled 设计在固定 count 的前提下变化 confusability，是该研究问题的正确方法论选择。Within-pool analysis (§4.3, Table 5) 用 80-pool 内采样 16-relation 子集排除 pool composition confound，permutation test p=0.60 证实 slope consistency。FewRel 的 balanced design (700 instances/type) 消除了 type frequency confound。这些控制在 training-free IE 文献中是少见的。\n\n**S2. 统计分析全面且透明。**\nTOST equivalence testing 用三个 margin 水平报告 (Table 8)，logit-scale sensitivity 单独报告且承认 inconclusive，bootstrap CIs 区分了 pair-level (B=10,000) 和 batch-level (B=1,000)，variance decomposition (Appendix Table 11) 量化了 batch vs seed 方差比。这种统计透明度在 NLP 实证论文中罕见。\n\n**S3. 负面结果的诚实报告。**\nSDGD 失败、NER batch-level null、MAVEN centrality confound、logit-scale inconclusive、few-shot widening gap 均被如实报告并分析原因。这增强了正面结果的可信度。\n\n**S4. 跨模型验证覆盖面广。**\nQwen3-32B (primary) + Llama-3.1-8B + 70B (FP8) + Gemini 2.5 Flash (API)，覆盖 open-weight 和 proprietary、8B-70B+ 规模。Dimension 1 在所有模型上复现；Dimension 2 在 RE 上跨 8B/32B/70B 复现。\n\n**S5. Robustness checks 充分。**\nPrompt variants (4 种, Appendix Table 10)、BCS aggregation (mean vs max, Appendix Table 7)、embedding ablation (name vs name+def, Appendix Table 12)、SCS baselines (Levenshtein, WordNet, same-parent, Appendix Table 14)、held-out validation (16 val-origin types, Appendix §K)、split-origin covariate (Appendix §L)。每个 potential confound 都有对应的控制分析。\n\n---\n\n## Weaknesses\n\n**N1 [warning] TOST margin 选择与 main effect 的关系需更多论证。**\n- 具体位置: §4.4, Appendix §C\n- 问题: ±3pp TOST margin 的 empirical anchor 是 \"typical random-batch confusability variation produces 2-5pp accuracy differences\"，但 typical-batch confusability main effect 本身仅 2.2pp。用 ±3pp margin 证明 interaction bounded 意味着 interaction 可以高达 main effect 的 136% (3/2.2) 而仍被认为 \"bounded\"。±2pp 是 marginal (p=0.047)，±1pp inconclusive。在 logit scale 上也 inconclusive (p=0.209)。\n- \"largely additive\" 的 claim 实质上是: interaction 在 linear scale 上 bounded below 2-3pp, 但无法排除 interaction 接近甚至超过 main effect 的 magnitude。这使 \"largely additive\" 的表述偏乐观。\n- 建议: Abstract 中 \"two largely additive dimensions\" 应加限定词，如 \"under RE's forced-choice format on the linear scale\"；或将 hedging 从 Appendix 提到正文。\n\n**N2 [warning] Abstract/Introduction 的叙事偏重 extreme-batch 数字，淡化 typical-batch modest effect。**\n- 具体位置: Abstract, §1\n- 问题: Abstract 写 \"BCS explains 22-53% of cross-batch RE accuracy variance\"，Introduction 列 \"-31.2pp\" extreme-batch gap 和 \"3.9-5.3pp quartile gaps\"。但 typical batching 下的 expected gap 仅 2.2pp (CI [0.4, 4.0])，且 NER 上 batch-level signal 为零。读者从 Abstract/Introduction 获得的 impression 与 typical real-world impact 之间有落差。\n- 建议: Abstract 中加一句 typical-batch magnitude（如 \"though typical batches yield modest 2.2pp gaps\"），使核心 message 更 calibrated。\n\n**N3 [warning] NER batch-level null 削弱了 \"two-dimensional\" 框架的普适性。**\n- 具体位置: §4.3, §4.4, §6\n- 问题: 论文的核心 framing 是 \"two-dimensional degradation\"（count + confusability）。但 Dimension 2 在 batch level 仅对 RE 有效，NER 上 r≈0 (n=450)。论文解释这是因为 NER 的 error 分散在 missed entities 和 boundary failures 上，但这意味着 \"two-dimensional\" 框架对 NER 仅在 pairwise level 成立（r²=1.3%），batch-level 没有 actionable signal。\n- 对于 EMNLP 读者来说，NER 是比 RE classification 更 mainstream 的 IE task。框架对 NER batch-level 无预测力是一个 significant boundary condition。\n- 建议: 论文已经在多处承认了这一点（Discussion, Limitations），但 title 和 abstract 的 framing 仍暗示 two-dimensional decomposition 是 general 的。\n\n**N4 [info] Monte Carlo simulation 的 evidential status 需要更清晰。**\n- 具体位置: Appendix §I\n- 问题: 论文正确地将 simulation 标注为 \"illustrative explanatory model\" 和 \"internal consistency check\"。但 Discussion §6 引用 \"Monte Carlo simulation with parameters derived from the observed data\" 时，尽管加了 caveat，仍可能给人 independent corroboration 的印象。Simulation 用 conditional R²=7%（仅 non-zero confusion pairs）匹配 observed batch R²=0.218，但 unconditional R²=1.3% 只能产生 simulated batch R²=0.044。这个 ~5× gap 的解释（89% zero-confusion pairs dilution）虽合理，但 conditioning on the outcome variable 是一个 methodological concern。\n- 建议: 正文引用 simulation 时删去具体数字，仅保留 \"post-hoc simulation confirms the aggregation pattern is consistent\"。\n\n**N5 [info] Few-shot 实验中 5-shot low-BCS 回落的解释不够充分。**\n- 具体位置: Appendix §N, Table 15\n- 问题: 1-shot low-BCS = 0.754, 5-shot low-BCS = 0.715 (-3.9pp)。论文归因于 \"lost-in-middle effects from increased prompt length\"，但这只是推测，未做控制实验验证。如果 low-BCS 在 5-shot 下回落是 prompt length effect，那 high-BCS 5-shot 也应受类似影响——但 high-BCS 从 0.554 (1-shot) 降到 0.488 (5-shot) 的降幅 (-6.6pp) 更大。两组不对称的降幅可能有 confusability-specific 的解释，而非仅仅是 prompt length。\n- 建议: 承认 non-monotonic pattern 的解释是 speculative。\n\n**N6 [info] Prompt variant analysis 的 multiple comparison 处理。**\n- 具体位置: Appendix §G, Table 10\n- 问题: 8 个 tests (4 variants × 2 count levels) 在同一 dataset 上进行。论文不做 Bonferroni，理由是 \"correlated prompt variants testing the same underlying signal\" (citing Rothman 1990)。Rothman (1990) 讨论的是 independent replications across different populations，而这里是 same dataset + same batches + different prompts，相关性方向是 positive (同一 batch 在不同 prompt 下的 accuracy 正相关)。Positive correlation 会 inflate directional consistency 而 deflate individual p-values。7/8 directional consistency 在 positively correlated tests 下的 evidential value 低于独立情况。\n- 建议: 加一句说明 positive correlation 对 directional consistency 的影响。\n\n---\n\n## Questions\n\n**Q1.** Table 2 (pairwise correlation) 排除了 FewRel，理由是 \"RE's per-instance format precludes direct comparison of confusion rates\"。但 §3.2 validation paragraph 和 Appendix Table 14 都报告了 FewRel 的 pairwise SCS-confusion ρ=0.218/0.187。这两个说法是否矛盾？如果 FewRel 可以计算 pairwise confusion，为什么 Table 2 排除它？\n\n**Q2.** Variance decomposition (Appendix Table 11) 中 count=16 的 seed SD (0.027) 显著高于其他 count levels (0.010-0.019 range)。这个异常值是否影响了 count=16 BCS-controlled 实验的结论？\n\n**Q3.** BCS independence analysis (Appendix §M) 报告 BCS unique R²=0.259, composition unique R²=0.298, shared=0.147。Shared variance 占 20.9%，这意味着 BCS 和 type difficulty 不是完全正交的。在 BCS-controlled 实验中，是否控制了 mean type difficulty？\n\n---\n\n## Missing References\n\n- 无明显遗漏。Related work 覆盖了 training-free IE、schema decomposition、constrained decoding、label confusion 等主要方向。引用密度符合 ACL venue 标准。\n\n---\n\n## Scores\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨，统计分析全面透明；但 \"largely additive\" 在 logit scale 上 inconclusive，TOST margin 选择与 main effect magnitude 的关系需论证，NER batch-level null 削弱框架普适性 |\n| Excitement | 2.5/5 | 分析框架有价值（controlled isolation of count vs confusability），但 typical-batch effect modest (2.2pp)，NER 无 batch-level signal，schema decomposition 失败，practical takeaway 有限 |\n| Reproducibility | 4/5 | 详细的实验描述（decoding params, seed, batch sizes, bootstrap params），code promised upon acceptance，prompt templates in appendix；单 GPU 可复现 |\n| Overall | 3.0 (Findings) | 方法论严谨的实证研究，controlled experimental design 在 training-free IE 文献中是有价值的贡献。但 practical impact limited (2.2pp typical), NER batch-level null, schema decomposition failure, 以及 \"largely additive\" claim 的 logit-scale caveat 限制了 excitement。适合 Findings。 |\n| Confidence | 4/5 | 仔细阅读了全文和 appendix，熟悉实验方法论和统计检验 |\n",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-18T10:01:32.193752+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4572
}
```

</details>

---


### Assistant

_source line 1154 · 2026-05-18T10:01:41.531674+00:00_

审稿意见已提交给 Review Director。

总结：

- **R18 修复验证**: N1/N2/N3/W5/W7 均 FIXED；W2/W3 PARTIALLY FIXED（Cohen 1988 analogy 仍需补充 LLM 领域先例；Abstract 叙事仍偏重 extreme-batch 数字）
- **Overall: 3.0 (Findings)**。方法论严谨（BCS-controlled design, within-pool analysis, TOST equivalence, 跨模型验证），统计透明度在 NLP 实证论文中罕见。主要限制：typical-batch effect 仅 2.2pp，NER 无 batch-level signal，"largely additive" 在 logit scale 上 inconclusive，schema decomposition 全面失败。
- 新提出 6 个 issues（2 warning, 4 info），3 个 questions。无 critical-level 新问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 39

## Round 39

4 recorded events


### User

_source line 1155 · 2026-05-18T10:03:41.319489+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

### R18 修复验证

| Issue | Status | 说明 |
|-------|--------|------|
| R18-N1 (boundary condition → forced-choice) | **[FIXED]** | "Forced-choice classification format" 贯穿 Abstract/Discussion/Conclusion/Limitations |
| R18-N2 (separable → largely additive) | **[FIXED]** | 统一为 "largely additive with bounded interaction"，TOST 分析含 logit-scale caveat |
| R18-N3 (metric → methodology contribution) | **[FIXED]** | Contribution 2 明确 "Building on...LLM-PEE...we design controlled experiments" |
| R18-W1 (Abstract ~180 words) | **[FIXED]** | ~156 words，结构清晰 |
| R18-W8 (正文超 8 页) | **[CANNOT VERIFY]** | 无法编译，估算 borderline 8-9 页 |
| R18-m-refs (Chen 2026, Wei 2023) | **[FIXED]** | 两篇均已 cite 且引用验证通过 |
| R17-W3 (diagnostic > engineering value) | **[PARTIALLY FIXED]** | Discussion 末尾 "diagnostic guidelines derived from correlational evidence"，但全文 framing 仍偏乐观 |

### Strengths
- S1: 实验设计严谨（BCS-controlled stratification, TOST, permutation test, bootstrap CI, within-pool 控制）
- S2: 跨模型验证充分（4 模型含 proprietary Gemini）
- S3: SDGD 负面结果诚实报告，对社区有警示意义
- S4: Limitations 10 项覆盖全面，含 power 分析自我披露
- S5: 70 篇引用，positioning 清晰

### Weaknesses
- **N1 [critical]**: 核心发现 novelty 有限——"more types = worse" 和 "similar types confuse" 概念上非 surprising；SCS 形式同 LLM-PEE；controlled experimental methodology 技术上非 novel。作为纯 analytical study，知识增量需足够大但效应量 modest
- **N2 [critical]**: Confusability 效应量小且 task-specific——pairwise r²=1.3-1.7%；NER batch-level 完全 null (n=450)；RE 发现依赖 forced-choice format 边界条件。Title/framing 暗示普适性但实际高度 task-specific
- **W1 [warning]**: 核心分析集中在 FewRel 一个数据集
- **W2 [warning]**: NER U-shape 现象缺乏实验证据解释
- **W3 [warning]**: "First controlled study" claim 可能过强

### Questions
- Q1: FewRel train-origin types 为何反而 accuracy 低 8.8pp？
- Q2: 16-rel condition 使用 single extreme batch 是否可能是 outlier？
- Q3: TOST ±1pp inconclusive 意味着 interaction 可能达 main effect 91%，"largely additive" framing 是否过强？

### Missing References
引用验证：70 bib / 97 citations / 0 orphan / 0 missing / 0 fabricated。建议补充 Guidance (Zheng et al., 2023) 和 Lyu et al. (2024)。

### Scores
- Soundness: 4/5
- Excitement: 2.5/5
- Reproducibility: 4/5
- Overall: 2.5 (Borderline Findings)
- Confidence: 4/5

### 一句话总结
实验执行出色的 analytical study，但核心发现（count dominates + confusability modest & RE-specific）的 novelty 和 impact 对 Findings 而言 borderline——知识增量受限于 modest effect sizes、NER batch-level null、和 SDGD 失败后缺乏 actionable alternative。

---

请逐条回应 R2 的 Weaknesses (N1, N2, W1, W2, W3)、Questions (Q1-Q3) 和 Missing References。对你自己的 issues 如果 R2 的审稿改变了你的判断也请说明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-18T10:05:21.265138+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# R1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## R18 修复验证\n\nR2 的修复验证与 R1 判断高度一致，仅就两项补充意见：\n\n**R18-W8 (正文页数)**: [AGREE] R2-W8: 我同样无法编译验证。从 section 数量和内容密度估算，8 页 borderline 是合理判断。这是一个需要作者确认的 formatting 问题。\n\n**R17-W3 (diagnostic > engineering)**: [AGREE] R2-R17-W3: 与我的 N2 一致。Discussion 末尾的 hedging 到位，但 Abstract/Introduction 的叙事仍偏重 extreme-batch 数字（-31.2pp, -49pp），对 typical-batch 2.2pp 的 modest effect 着墨不足。\n\n---\n\n## Weaknesses 逐条回应\n\n**[AGREE] R2-N1 (novelty 有限)**:\n同意 novelty 是本文的主要弱点。\"More types = worse\" 在 Li et al. (2023)、LLM-PEE (2025) 中已有定性观察；\"similar types confuse\" 在 hierarchical classification (Deng et al., 2010 ImageNet) 和 label confusion (Guo et al., 2021) 中有先例。SCS 形式同 LLM-PEE 的 partitioning criterion（Related Work §2 SCS novelty 段已承认）。论文的 novelty 在于 controlled experimental methodology，但 R2 的判断\"技术上非 novel\"有道理——BCS-controlled stratification 本质上是 observational study with quasi-experimental manipulation，不是新方法。\n\n不过我对 R2 的 framing 有一个 nuance 补充：虽然概念不 surprising，但在 training-free IE 文献中，此前没有人量化过 count vs confusability 的相对贡献，也没有人发现 NER batch-level null 这个 task asymmetry。这些 empirical findings 在 Findings track 中是 acceptable 的 knowledge increment，即使 conceptual novelty 有限。\n\n**[AGREE] R2-N2 (effect size small & task-specific)**:\n与我的 N2 和 N3 一致。具体证据：\n- Pairwise r²=1.3-1.7% (Table 2)\n- NER batch-level r≈0, n=450 (§4.3, §4.4)\n- Typical-batch gap 2.2pp, CI [0.4, 4.0] (§4.3 practical magnitude)\n- Dimension 2 batch-level signal 仅在 RE forced-choice format 下成立 (Discussion §6)\n\nTitle \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\" 确实暗示了对 IE 的普适性，但 Dimension 2 的 batch-level 预测力仅限 RE classification format。R2 的 \"task-specific\" 判断准确。\n\n**[PARTIALLY REBUT] R2-W1 (核心分析集中 FewRel 一个数据集)**:\nR2 的担忧有道理，但需要区分维度：\n- **Dimension 1 (count curves)**: 在 FewRel、DocRED、Few-NERD、MAVEN 四个数据集上均有复现（Figure 1a, §4.1），不是 single-dataset。\n- **Dimension 2 (BCS-controlled)**: FewRel 是 primary dataset，但 DocRED 独立复现了 BCS-accuracy slopes（slope=-0.713, R²=0.525 at count 16, R²=0.443 at count 32; §4.3 Document-level RE 段）。两个 RE 数据集（80 vs 96 types, sentence vs document level）的一致性构成有意义的 replication。\n- **Pairwise SCS**: 在 Few-NERD (r=0.112)、FewRel (r=0.187)、MAVEN (r=0.129) 三个数据集上均显著 (Table 2, §3.2)。\n\n真正的 single-dataset 问题在于：BCS-controlled 的 detailed analysis（within-pool, factorial, aggregation simulation）全部基于 FewRel。DocRED 的 BCS 分析相对简略（n=35 batches, 无 within-pool 控制）。\n\n**[AGREE] R2-W2 (NER U-shape 缺乏实验证据)**:\nDiscussion §6 提出的 \"dual-task burden\" 假说（partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers）是合理的机制假说，但完全是 speculative——没有控制实验验证。论文没有设计实验区分 U-shape 的 three possible explanations：(1) type-membership filtering overhead, (2) prompt length effect, (3) instruction complexity。Cross-model replication of U-shape（Table 9, 70B 和 Qwen3 均在 count 22→44 处 rebound）增加了现象的可信度，但不解释机制。R2 的 concern 成立。\n\n**[PARTIALLY REBUT] R2-W3 (\"first controlled study\" claim 过强)**:\n这取决于 \"controlled\" 的定义。论文的 claim 是 \"first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE, spanning NER, RE, and event detection\" (§1)。关键限定词是 \"isolating...via stratified design\"。\n- LLM-PEE (2025) 用 embedding similarity 做 schema partitioning，但没有 fix count + vary BCS 的 controlled comparison。\n- Li et al. (2023) 观察 count-dependent degradation，但不分离 confusability。\n- 其他 decomposition 工作（UniNER, PARSE 等）都是 engineering solutions，不做 controlled factor isolation。\n\n因此 \"first controlled study\" 在字面意义上可能成立，但 \"controlled\" 在这里指 quasi-experimental stratification，不是 randomized intervention。论文在 Limitations item 8 已承认 \"correlational evidence with controlled stratification\" 而非 \"interventional causality\"。Claim 不算过强，但可以更 precise 地写 \"first quasi-experimental study\"。\n\n---\n\n## Questions 逐条回应\n\n**[AGREE with nuance] R2-Q1 (FewRel train-origin accuracy 低 8.8pp)**:\n合理的问题。Appendix §L 报告 train-origin ratio 不显著（β=-0.057, p=0.245），BCS partial effect unchanged。但 -8.8pp (p=0.06) 的 borderline significance 确实值得讨论。论文在 Limitations item 10 把它归入 data contamination 讨论，认为 \"opposite to the contamination hypothesis\"（contamination 应使 train-origin accuracy 更高）。一个可能的解释是 train-split types 在 Wikidata 中 inherently 更难（被选入 training set 可能因为它们对 few-shot learning 更有挑战性），但论文未验证。R2 的问题合理但不影响核心结论（Appendix §L covariate analysis 已控制）。\n\n**[AGREE] R2-Q2 (16-rel single extreme batch = outlier risk)**:\n与论文自身的 caveat 一致。Appendix Table 8 caption 明确写 \"The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches\"。论文将 16-rel 作为 pilot condition，主要证据来自 80-rel pool 的 n=25/group 设计。R2 的 concern 成立但论文已 acknowledge。\n\n**[AGREE] R2-Q3 (TOST ±1pp inconclusive → interaction 可能达 main effect 91%)**:\n与我的 N1 一致。Interaction 的 90% CI 上界 2.0pp / main effect 2.2pp = 91%。这使 \"largely additive\" 在严格统计意义上站不住——数据不能排除 interaction 接近 main effect 的可能。论文的 defense 是 point estimate 很小 (0.47pp)，但 CI 宽度反映了 insufficient power。在 logit scale 上 TOST 也 inconclusive (p=0.209, Appendix §C)。\n\n不过我补充一个 nuance：cross-pool slope consistency (permutation p=0.60, Table 5) 提供了间接证据——如果 count×BCS interaction 很大，不同 count pool 的 BCS slope 应该不一致。这不是 formal equivalence test，但 directionally supportive。\n\n---\n\n## Missing References\n\n**[PARTIALLY AGREE] R2 建议补充 Guidance (Zheng et al., 2023) 和 Lyu et al. (2024)**:\n- Zheng et al. (2023) 如果是 LLM-as-judge/evaluation guidance 方向，与本文的 schema complexity 主题相关性有限。如果是 label guidance 方向，可能值得在 Related Work 中提及。需要作者确认具体是哪篇。\n- Lyu et al. (2024) 同理，需要确认具体论文。R2 未提供 full citation，无法判断相关性。\n- 论文现有 70 篇引用覆盖面已较完整。\n\n---\n\n## R2 审稿对 R1 判断的影响\n\nR2 的 N1 (novelty) 和 N2 (task-specificity) 是我同意的 concerns，但对 Overall 评分的影响我与 R2 有分歧：\n\n- R2 给 Overall 2.5 (Borderline Findings)，理由是 \"知识增量受限于 modest effect sizes、NER batch-level null、SDGD 失败后缺乏 actionable alternative\"。\n- 我维持 Overall 3.0 (Findings)。理由：(1) 论文的价值不在 engineering solution 而在 diagnostic framework——quantifying 了此前仅被定性观察的现象；(2) NER batch-level null 本身是一个有价值的 negative finding（task format determines whether confusability is batch-level predictive）；(3) SDGD 失败的诊断（merge amplification, routing failure）对未来 decomposition 工作有指导意义；(4) 统计透明度（TOST, logit-scale caveat, power analysis）在 NLP 实证论文中罕见，值得鼓励。\n\n这些 negative/modest results 如果被认为 \"not enough for Findings\"，会产生 publication bias 激励——只有 effect size 大且 positive 的结果才能发表。ARR reviewer guidelines H6 明确指出 \"negative findings\" 不应被自动降低评价。\n\n**最终判断**: R2 的审稿加强了我对 novelty 和 framing 问题的 concern，但不改变我的 Overall 3.0。论文需要在 Abstract/Introduction 中更 calibrated 地呈现 typical-batch effect size 和 task-specificity boundary condition。\n",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# R1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## R18 修复验证\n\nR2 的修复验证与 R1 判断高度一致，仅就两项补充意见：\n\n**R18-W8 (正文页数)**: [AGREE] R2-W8: 我同样无法编译验证。从 section 数量和内容密度估算，8 页 borderline 是合理判断。这是一个需要作者确认的 formatting 问题。\n\n**R17-W3 (diagnostic > engineering)**: [AGREE] R2-R17-W3: 与我的 N2 一致。Discussion 末尾的 hedging 到位，但 Abstract/Introduction 的叙事仍偏重 extreme-batch 数字（-31.2pp, -49pp），对 typical-batch 2.2pp 的 modest effect 着墨不足。\n\n---\n\n## Weaknesses 逐条回应\n\n**[AGREE] R2-N1 (novelty 有限)**:\n同意 novelty 是本文的主要弱点。\"More types = worse\" 在 Li et al. (2023)、LLM-PEE (2025) 中已有定性观察；\"similar types confuse\" 在 hierarchical classification (Deng et al., 2010 ImageNet) 和 label confusion (Guo et al., 2021) 中有先例。SCS 形式同 LLM-PEE 的 partitioning criterion（Related Work §2 SCS novelty 段已承认）。论文的 novelty 在于 controlled experimental methodology，但 R2 的判断\"技术上非 novel\"有道理——BCS-controlled stratification 本质上是 observational study with quasi-experimental manipulation，不是新方法。\n\n不过我对 R2 的 framing 有一个 nuance 补充：虽然概念不 surprising，但在 training-free IE 文献中，此前没有人量化过 count vs confusability 的相对贡献，也没有人发现 NER batch-level null 这个 task asymmetry。这些 empirical findings 在 Findings track 中是 acceptable 的 knowledge increment，即使 conceptual novelty 有限。\n\n**[AGREE] R2-N2 (effect size small & task-specific)**:\n与我的 N2 和 N3 一致。具体证据：\n- Pairwise r²=1.3-1.7% (Table 2)\n- NER batch-level r≈0, n=450 (§4.3, §4.4)\n- Typical-batch gap 2.2pp, CI [0.4, 4.0] (§4.3 practical magnitude)\n- Dimension 2 batch-level signal 仅在 RE forced-choice format 下成立 (Discussion §6)\n\nTitle \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\" 确实暗示了对 IE 的普适性，但 Dimension 2 的 batch-level 预测力仅限 RE classification format。R2 的 \"task-specific\" 判断准确。\n\n**[PARTIALLY REBUT] R2-W1 (核心分析集中 FewRel 一个数据集)**:\nR2 的担忧有道理，但需要区分维度：\n- **Dimension 1 (count curves)**: 在 FewRel、DocRED、Few-NERD、MAVEN 四个数据集上均有复现（Figure 1a, §4.1），不是 single-dataset。\n- **Dimension 2 (BCS-controlled)**: FewRel 是 primary dataset，但 DocRED 独立复现了 BCS-accuracy slopes（slope=-0.713, R²=0.525 at count 16, R²=0.443 at count 32; §4.3 Document-level RE 段）。两个 RE 数据集（80 vs 96 types, sentence vs document level）的一致性构成有意义的 replication。\n- **Pairwise SCS**: 在 Few-NERD (r=0.112)、FewRel (r=0.187)、MAVEN (r=0.129) 三个数据集上均显著 (Table 2, §3.2)。\n\n真正的 single-dataset 问题在于：BCS-controlled 的 detailed analysis（within-pool, factorial, aggregation simulation）全部基于 FewRel。DocRED 的 BCS 分析相对简略（n=35 batches, 无 within-pool 控制）。\n\n**[AGREE] R2-W2 (NER U-shape 缺乏实验证据)**:\nDiscussion §6 提出的 \"dual-task burden\" 假说（partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers）是合理的机制假说，但完全是 speculative——没有控制实验验证。论文没有设计实验区分 U-shape 的 three possible explanations：(1) type-membership filtering overhead, (2) prompt length effect, (3) instruction complexity。Cross-model replication of U-shape（Table 9, 70B 和 Qwen3 均在 count 22→44 处 rebound）增加了现象的可信度，但不解释机制。R2 的 concern 成立。\n\n**[PARTIALLY REBUT] R2-W3 (\"first controlled study\" claim 过强)**:\n这取决于 \"controlled\" 的定义。论文的 claim 是 \"first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE, spanning NER, RE, and event detection\" (§1)。关键限定词是 \"isolating...via stratified design\"。\n- LLM-PEE (2025) 用 embedding similarity 做 schema partitioning，但没有 fix count + vary BCS 的 controlled comparison。\n- Li et al. (2023) 观察 count-dependent degradation，但不分离 confusability。\n- 其他 decomposition 工作（UniNER, PARSE 等）都是 engineering solutions，不做 controlled factor isolation。\n\n因此 \"first controlled study\" 在字面意义上可能成立，但 \"controlled\" 在这里指 quasi-experimental stratification，不是 randomized intervention。论文在 Limitations item 8 已承认 \"correlational evidence with controlled stratification\" 而非 \"interventional causality\"。Claim 不算过强，但可以更 precise 地写 \"first quasi-experimental study\"。\n\n---\n\n## Questions 逐条回应\n\n**[AGREE with nuance] R2-Q1 (FewRel train-origin accuracy 低 8.8pp)**:\n合理的问题。Appendix §L 报告 train-origin ratio 不显著（β=-0.057, p=0.245），BCS partial effect unchanged。但 -8.8pp (p=0.06) 的 borderline significance 确实值得讨论。论文在 Limitations item 10 把它归入 data contamination 讨论，认为 \"opposite to the contamination hypothesis\"（contamination 应使 train-origin accuracy 更高）。一个可能的解释是 train-split types 在 Wikidata 中 inherently 更难（被选入 training set 可能因为它们对 few-shot learning 更有挑战性），但论文未验证。R2 的问题合理但不影响核心结论（Appendix §L covariate analysis 已控制）。\n\n**[AGREE] R2-Q2 (16-rel single extreme batch = outlier risk)**:\n与论文自身的 caveat 一致。Appendix Table 8 caption 明确写 \"The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches\"。论文将 16-rel 作为 pilot condition，主要证据来自 80-rel pool 的 n=25/group 设计。R2 的 concern 成立但论文已 acknowledge。\n\n**[AGREE] R2-Q3 (TOST ±1pp inconclusive → interaction 可能达 main effect 91%)**:\n与我的 N1 一致。Interaction 的 90% CI 上界 2.0pp / main effect 2.2pp = 91%。这使 \"largely additive\" 在严格统计意义上站不住——数据不能排除 interaction 接近 main effect 的可能。论文的 defense 是 point estimate 很小 (0.47pp)，但 CI 宽度反映了 insufficient power。在 logit scale 上 TOST 也 inconclusive (p=0.209, Appendix §C)。\n\n不过我补充一个 nuance：cross-pool slope consistency (permutation p=0.60, Table 5) 提供了间接证据——如果 count×BCS interaction 很大，不同 count pool 的 BCS slope 应该不一致。这不是 formal equivalence test，但 directionally supportive。\n\n---\n\n## Missing References\n\n**[PARTIALLY AGREE] R2 建议补充 Guidance (Zheng et al., 2023) 和 Lyu et al. (2024)**:\n- Zheng et al. (2023) 如果是 LLM-as-judge/evaluation guidance 方向，与本文的 schema complexity 主题相关性有限。如果是 label guidance 方向，可能值得在 Related Work 中提及。需要作者确认具体是哪篇。\n- Lyu et al. (2024) 同理，需要确认具体论文。R2 未提供 full citation，无法判断相关性。\n- 论文现有 70 篇引用覆盖面已较完整。\n\n---\n\n## R2 审稿对 R1 判断的影响\n\nR2 的 N1 (novelty) 和 N2 (task-specificity) 是我同意的 concerns，但对 Overall 评分的影响我与 R2 有分歧：\n\n- R2 给 Overall 2.5 (Borderline Findings)，理由是 \"知识增量受限于 modest effect sizes、NER batch-level null、SDGD 失败后缺乏 actionable alternative\"。\n- 我维持 Overall 3.0 (Findings)。理由：(1) 论文的价值不在 engineering solution 而在 diagnostic framework——quantifying 了此前仅被定性观察的现象；(2) NER batch-level null 本身是一个有价值的 negative finding（task format determines whether confusability is batch-level predictive）；(3) SDGD 失败的诊断（merge amplification, routing failure）对未来 decomposition 工作有指导意义；(4) 统计透明度（TOST, logit-scale caveat, power analysis）在 NLP 实证论文中罕见，值得鼓励。\n\n这些 negative/modest results 如果被认为 \"not enough for Findings\"，会产生 publication bias 激励——只有 effect size 大且 positive 的结果才能发表。ARR reviewer guidelines H6 明确指出 \"negative findings\" 不应被自动降低评价。\n\n**最终判断**: R2 的审稿加强了我对 novelty 和 framing 问题的 concern，但不改变我的 Overall 3.0。论文需要在 Abstract/Introduction 中更 calibrated 地呈现 typical-batch effect size 和 task-specificity boundary condition。\n",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1157 · 2026-05-18T10:05:25.485228+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4220
}
```

</details>

---


### Assistant

_source line 1158 · 2026-05-18T10:05:32.913179+00:00_

已提交对 Reviewer 2 的逐条回应。核心立场：

- **N1 (novelty)** 和 **N2 (task-specificity)**: 同意这是主要弱点，但 controlled methodology + negative findings 在 Findings track 仍有价值
- **W1 (single dataset)**: 部分反驳——DocRED 独立复现了 BCS slopes，Dimension 1 跨四个数据集复现
- **W2 (U-shape)**: 同意，假说缺实验验证
- **W3 (first controlled study)**: 部分反驳，claim 在字面意义上成立但可写 "quasi-experimental"
- **Q3 (TOST ±1pp)**: 同意，与我的 N1 一致，"largely additive" 偏乐观

维持 Overall 3.0 (Findings)，未因 R2 的 2.5 改变评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 40

## Round 40

42 recorded events


### User

_source line 1159 · 2026-05-19T04:30:17.607521+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）

### Venue 信息
- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）
- **截止日期**: 2026-05-25
- **页数限制**: Long paper, 正文 ≤ 8 页 + 无限参考文献页 + appendix 不计页数
- **模板**: ACL official style, `\usepackage[review]{acl}`
- **匿名规则**: Double-blind
- **Limitations section**: 必须有，不计入页数
- **Checklist**: Responsible NLP Research Checklist 必须认真填写
- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

### 论文路径
- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`
- 各章节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`, `checklist.tex`, `prompt_appendix.tex`
- 参考文献: `references.bib`

### 你的审查侧重

**方法严谨性 + 实验设计 + 统计分析**。具体关注：

1. **实验设计合理性**：
   - Count curves 和 BCS-controlled 两种实验范式是否能有效分离 count 和 confusability 两个维度？
   - 样本量是否充足（FewRel 25 batches, DocRED 5 batches）？
   - TOST equivalence test 的 margin 选择（±3pp）是否合理？是否有 p-hacking 风险？

2. **统计分析严谨性**：
   - Pairwise r²=1.3-1.7% 的效应量解读是否恰当？引用 Cohen (1988) behavioral research 标准是否适用于 LLM 系统？
   - Bootstrap CI、permutation test、TOST 的使用是否正确？
   - 多重比较问题：引用 Rothman (1990) 拒绝校正是否合理？
   - "Largely additive" 的 claim 在 logit-scale inconclusive 的情况下是否 overstate？

3. **跨模型/跨数据集验证**：
   - Qwen3-32B → Llama-3.1-8B/70B → Gemini 2.5 Flash 的 cross-model 验证是否充分？
   - Dimension 2 仅在 open-weight 模型上验证，是否是重大局限？
   - DocRED 复现是否充分支撑 claim？

4. **Negative results 的论证**：
   - SDGD decomposition failure 的归因（merge amplification, routing failure）是否 convincing？
   - Oracle routing +29.8pp 但 practical routing 全部 below baseline — 这是否说明 schema decomposition 本身有价值但 routing 是瓶颈？

5. **混淆变量控制**：
   - FewRel train/val split-origin 控制是否充分？
   - MAVEN centrality confound 的处理是否合理？
   - BCS independence from type composition (Appendix) 的 variance decomposition 是否令人信服？

请按 ARR 审稿标准输出完整审稿报告，包含：Summary, Strengths, Weaknesses (逐条编号, 标注 severity: Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 置信度), Detailed Comments。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1160 · 2026-05-19T04:30:26.783804+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-19T04:30:27.286566+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-19T04:30:27.287016+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-19T04:30:28.192981+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 has been validated across all four models including a proprietary one; Dimension~2 has been verified only on open-weight models and was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded under the linear specification (TOST $p = 0.003$ at $\pm 3$\,pp on FewRel; DocRED inconclusive, Appendix~\ref{sec:appendix_factorial}) but inconclusive on the logit scale ($p = 0.209$). BCS-controlled experiments use a single seed with greedy decoding; the residual SD of 0.88\,pp (Appendix~\ref{app:variance-decomposition}) supports robustness but precise magnitudes may vary.
43	
44	\item \textbf{Task format dependency.} BCS batch-level prediction is demonstrated only under RE's forced-choice classification format. An unconstrained decoding ablation ($n = 25$) confirms
…[truncated 56981 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1164 · 2026-05-19T04:30:28.396218+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1165 · 2026-05-19T04:30:28.497073+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1166 · 2026-05-19T04:30:34.672411+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1167 · 2026-05-19T04:30:35.074959+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets. We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two largely additive dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution, though typical batches yield modest ${\sim}$2\,pp gaps. BCS explains 22--53\% of cross-batch RE accuracy variance under RE's forced-choice format but shows no batch-level signal for NER, where errors scatter across missed entities and boundary failures. Few-shot demonstrations widen the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Pairwise confusability is a schema-structural property: effects replicate across model scales and families, and persist under varied prompt designs.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1168 · 2026-05-19T04:30:35.076935+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1169 · 2026-05-19T04:30:35.334297+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
…[truncated 3157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 257
}
```

</details>

---


### Tool call

_source line 1170 · 2026-05-19T04:30:35.493012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1171 · 2026-05-19T04:30:36.557205+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and fine-grained entity typing \cite{gillick-2014-entity-typing}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. \citet{wei-2023-chatie} reformulate zero-shot IE as multi-turn QA with ChatGPT but do not analyze schema-size effects.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definit
…[truncated 3188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1064
}
```

</details>

---


### Tool call

_source line 1172 · 2026-05-19T04:30:36.557698+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 1173 · 2026-05-19T04:30:37.060469+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate th
…[truncated 7648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1174 · 2026-05-19T04:30:37.060941+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1175 · 2026-05-19T04:30:37.514383+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure*}[t]
10	\centering
11	\begin{minipage}[t]{0.48\textwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\textwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves. Error bars: $\pm 1$\,SD across 3 seeds $\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Hollow markers: full-schema (no sampling variance). \textbf{(b)} BCS-controlled FewRel accuracy. Slopes are consistent across the independent and within-pool 16-relation conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps.}
21	\label{fig:main_results}
22	\end{figure*}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $
…[truncated 9450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1176 · 2026-05-19T04:30:37.565124+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 1177 · 2026-05-19T04:30:38.018436+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapse (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.): graph coloring achieves only marginal mean BCS reduction (0.559$\to$0.552), insufficient to produce detectable accuracy improvement. All practical routing strategies fall below the single-pass baseline (Appendix~\ref{sec:appendix_routing}).
11	
12	Promising avenues include coarse-to-fine pipelines and retrieval-based routing.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1178 · 2026-05-19T04:30:38.018932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1179 · 2026-05-19T04:30:38.778332+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED $R^2 = 0.51$) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%); conditional on nonzero confusion, $R^2$ rises to 7\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\% (Monte Carlo simulation; Appendix~\ref{app:aggregation-sim}), consistent with observed RE values.
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific ($R^2 = 0.22$--$0.53$ vs.\ $r \approx 0$ for NER, $n = 450$). RE uses forced-choice classification where all non-null errors are type substitutions \cite{tam-2024-let-me-speak}, making BCS predictive. NER produces multi-span output where errors scatter across missed entities, boundary misalignment, and type confusion, diluting the BCS signal \cite{schall-2025-hidden-cost}. The NER U-shape (\S\ref{sec:count_curves}) likely reflects a dual-task burden: partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers. An unconstrained decoding ablation ($n = 25$) confirms format dependency: removing the JSON enum constraint eliminates the BCS--accuracy correlation ($\rho = -0.14$, $p = 0.49$) while OOV remains near zero (0.08\%), showing that constrained decoding channels all errors into type substitution.
12	
13	\paragraph{Practical implications.}
14	For RE, pre-screening type pairs in th
…[truncated 1551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 759
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-19T04:30:38.778883+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-19T04:30:55.012263+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on my search, I found relevant information about ACL Rolling Review (ARR) guidelines for 2025-2026. Here's what I discovered:

## Reviewer Guidelines and Key Requirements

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

## Review Form and Assessment Process

After the author response period, ACs can report both great and irresponsible reviews via a new form on reviews or by listing the great/irresponsible reviewers in the meta-review form.

## Scoring and Review Standards

The program c
…[truncated 1007 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 16233
}
```

</details>

---


### Tool call

_source line 1182 · 2026-05-19T04:31:00.840485+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form dimensions/criteria and their scoring scales. I need: all numbered scoring dimensions (like soundness, excitement/novelty, clarity, etc.), their scale descriptions (1-5 or similar), and any specific guidance on how to score each dimension. Also extract any guidance on overall assessment scoring."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form dimensions/criteria and their scoring scales. I need: all numbered scoring dimensions (like soundness, excitement/novelty, clarity, etc.), their scale descriptions (1-5 or similar), and any specific guidance on how to score each dimension. Also extract any guidance on overall assessment scoring."
  }
}
```

</details>

---


### Tool call

_source line 1183 · 2026-05-19T04:31:02.654340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 1184 · 2026-05-19T04:31:03.057054+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{lla
…[truncated 4608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1185 · 2026-05-19T04:31:03.057538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1186 · 2026-05-19T04:31:03.209025+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1187 · 2026-05-19T04:31:03.209550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1188 · 2026-05-19T04:31:03.512367+00:00_

1	@inproceedings{tam-2024-let-me-speak,
2	  title     = {Let Me Speak Freely? {A} Study on the Impact of Format Restrictions on Performance of Large Language Models},
3	  author    = {Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hung-yi and Chen, Yun-Nung},
4	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track},
5	  year      = {2024},
6	  url       = {https://arxiv.org/abs/2408.02442}
7	}
8	
9	@inproceedings{yin-2019-zero-shot-bench,
10	  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},
11	  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},
12	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
13	  pages     = {3914--3923},
14	  year      = {2019},
15	  url       = {https://arxiv.org/abs/1909.00161}
16	}
17	
18	@article{schuirmann-1987-tost,
19	  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},
20	  author    = {Schuirmann, Donald J.},
21	  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},
22	  volume    = {15},
23	  number    = {6},
24	  pages     = {657--680},
25	  year      = {1987},
26	  doi       = {10.1007/BF01068419}
27	}
28	
29	@article{gemini-2025,
30	  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},
31	  author    = {Comanici, Gheorghe and others},
32	  journal   = {arXiv preprint arXiv:2507.06261},
33	  year      = {2025},
34	  url       = {https://arxiv.org/abs/2507.06261}
35	}
36	
37	@inproceedings{snell2017prototypical,
38	  title     = {Prototypical Networks for Few-shot Learning},
39	  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},
40	  booktitle = {Advances in Neural Information Processing Systems},
41	  volume    = {30},
42	  year      = {2017}
43	}
44	
4
…[truncated 31894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 1189 · 2026-05-19T04:31:13.082117+00:00_

# ARR Review Form Dimensions and Scoring

Based on the guidelines provided, ARR uses a **three-score system** as of February 2025:

## Scoring Dimensions

**1. Soundness**
- Measures technical validity and methodological rigor
- "Must be justified by the text of the review" - low scores require explicit fault identification
- Papers committed to venues must demonstrate sufficient soundness

**2. Excitement**
- Reflects personal interest and subjective appeal
- "Orthogonal to soundness assessment" - independent from technical evaluation
- Captures individual reviewer taste rather than objective quality

**3. Overall Assessment**
- Explicit recommendation for venue outcome (main conference, findings, or rejection)
- Composite score balancing soundness, excitement, novelty, and potential impact
- All accepted papers must meet soundness standards, but personal excitement varies

## Key Guidance

The instructions emphasize that excitement and soundness operate independently: "a paper sound but not personally interesting" warrants separate scoring. The overall assessment represents the recommendation if the paper were submitted to an *ACL venue.

**Specific scoring scales and numerical ranges are not detailed** in the provided content. The guidelines focus on *justification requirements* rather than numerical rubrics, emphasizing that "low reproducibility scores should be justified."

The form itself is referenced but not fully reproduced in these guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 12241
}
```

</details>

---


### Tool call

_source line 1190 · 2026-05-19T04:31:21.591329+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form 2025 soundness excitement overall assessment scoring scale 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form 2025 soundness excitement overall assessment scoring scale 1-5"
  }
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-19T04:31:31.004134+00:00_

Web search results for query: "ACL Rolling Review review form 2025 soundness excitement overall assessment scoring scale 1-5"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

Based on the search results, I found detailed information about the ACL Rolling Review 2025 form and scoring scales:

## Scoring Scale Overview

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Scoring (1-5 Scale)

5 = Excellent: This study is one of the most thorough I have seen, given its type. 4 = Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential. 3 = Acceptable: This study provides sufficient support for its main claims.

The form also specifies that soundness evaluates whether the paper is sufficiently sound and thorough, and whether it clearly states scientific claims and provides adequate support for them.

## Excitement Scoring (1-5 Scale)

5 = Highly Exc
…[truncated 718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9412
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-19T04:31:35.743992+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact numerical scales, and descriptions for each score level. I need every dimension (soundness, excitement, overall assessment, reproducibility, etc.), the full 1-5 scale descriptions for each, and any other form fields like confidence, limitations addressed, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact numerical scales, and descriptions for each score level. I need every dimension (soundness, excitement, overall assessment, reproducibility, etc.), the full 1-5 scale descriptions for each, and any other form fields like confidence, limitations addressed, etc."
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-19T04:31:45.211989+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. Reviewer Confidence
Scale: 1-5
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## 2. Soundness
Scale: 1-5 (with .5 increments)
- **5:** "Excellent: This study is one of the most thorough I have seen, given its type."
- **4:** "Strong: This study provides sufficient support for all of its claims."
- **3:** "Acceptable: This study provides sufficient support for its main claims."
- **2:** "Poor: Some of the main claims are not sufficiently supported."
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement
Scale: 1-5 (with .5 increments)
- **5:** "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4:** "Exciting: I would mention this paper to others."
- **3:** "Interesting: I might mention some points of this paper to others."
- **2:** "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1:** "Not Exciting: this paper does not resonate with me."

## 4. Overall Assessment
Scale: 1-5 (with .5 increments)
- **5:** "Consider for Award: up to top 2.5% papers"
- **4.5:** "Borderline Award"
- **4:** "Conference: could be accepted to an ACL conference"
- **3.5:** "Borderline Conference"
- **3:** "Findings: could be accepted to Findings of the ACL"
- **2.5:** "Borderline Findings"
- **2:** "Resubmit next cycle: needs substantial revisions"
- **1.5:** "Resubmit after next cycle: needs substantial revisions"
- **1:** "Do not resubmit"

## 5. Reproducibility
Scale: 1-5
- **5:** "They could easily reproduce the results."
- *
…[truncated 1833 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9467
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-19T04:32:41.810788+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-19T04:33:37.718195+00:00_

&lt;persisted-output>
Output too large (57.1KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/d1eaf3a3-f3ef-495b-9858-bc28ffbd1401/tool-results/toolu_015bun1d9uNeR1focnVuytay.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 70, \"total_citations\": 96, \"unique_cited_keys\": 69, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 55, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"jagannatha2020calibrating\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"tam-2024-let-me-speak\", \"type\": \"inproceedings\", \"title\": \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\", \"authors\": \"Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yin-2019-zero-shot-bench\", \"type\": \"inproceedings\", \"title\": \"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\", \"authors\": \"Yin, Wenpeng and Hay, Jamaal and Roth, Dan\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"schuirmann-1987-tost\", \"type\": \"article\", \"title\": \"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioava...\", \"authors\": \"Schuirmann, Donald J.\", \"year\": \"1987\", \"venue\": \"Journal of Pharmacokinetics and Biopharmaceutics\"}, {\"key\": \"gemini-2025\", \"type\": \"article\", \"title\": \"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long C
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 55907
}
```

</details>

---


### Tool call

_source line 1196 · 2026-05-19T04:33:41.686952+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/d1eaf3a3-f3ef-495b-9858-bc28ffbd1401/tool-results/toolu_015bun1d9uNeR1focnVuytay.txt",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/d1eaf3a3-f3ef-495b-9858-bc28ffbd1401/tool-results/toolu_015bun1d9uNeR1focnVuytay.txt",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1197 · 2026-05-19T04:33:41.989690+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 70, \"total_citations\": 96, \"unique_cited_keys\": 69, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 55, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"jagannatha2020calibrating\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"tam-2024-let-me-speak\", \"type\": \"inproceedings\", \"title\": \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\", \"authors\": \"Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yin-2019-zero-shot-bench\", \"type\": \"inproceedings\", \"title\": \"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\", \"authors\": \"Yin, Wenpeng and Hay, Jamaal and Roth, Dan\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"schuirmann-1987-tost\", \"type\": \"article\", \"title\": \"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioava...\", \"authors\": \"Schuirmann, Donald J.\", \"year\": \"1987\", \"venue\": \"Journal of Pharmacokinetics and Biopharmaceutics\"}, {\"key\": \"gemini-2025\", \"type\": \"article\", \"title\": \"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\", \"authors\": \"Comanici, Gheorghe and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2507.06261\"}, {\"key\": \"snell2017prototypical\", \"type\": \"inproceedings\", \"title\": \"Prototypical Networks for Few-shot Learning\", \"authors\": \"Snell, Jake and Swersky, Kevin and Zemel, Richard\", \"year\": \"2017
…[truncated 56510 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-19T04:36:49.951122+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿报告 — Round 1\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 (via ARR May 2026 cycle)\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n---\n\n## Paper Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度导致的性能退化问题，提出将退化分解为两个维度：type count（维度1）和 type confusability（维度2）。作者定义了 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 来量化 type 间语义混淆度，在 Few-NERD (NER)、FewRel (RE)、DocRED (doc-RE)、MAVEN (ED) 四个数据集上进行了 count curves 和 BCS-controlled 两种实验范式的系统评估。主要发现：(1) 两个维度\"大致可加\"（在 sentence-level RE 上）；(2) BCS 能解释 RE 22-53% 的跨 batch 准确率方差，但对 NER 无 batch-level 信号；(3) schema 分解因 merge amplification (NER) 和 routing failure (RE) 而失败。Cross-model 验证覆盖 Qwen3-32B、Llama-8B/70B、Gemini 2.5 Flash。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n**Confidence**: 4 (Quite sure. I tried to check the important points carefully.)\n**一句话总结**: 实验设计严谨、统计处理透明度高于 NLP 论文平均水准，但 \"largely additive\" 的核心 claim 在 logit scale 和 DocRED 上站不住脚，pairwise 效应量极小（r²=1.3-1.7%），且所有实际干预方向（分解、重命名、few-shot）均失败，实际可操作价值有限。\n\n---\n\n## 官方维度打分（来自 ARR Review Form，2025年2月更新版）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨，统计工具使用恰当（TOST、permutation test、bootstrap CI），但核心 claim \"largely additive\" overclaim，且多个条件下 TOST inconclusive |\n| Excitement | 3.0/5 | 分析框架有新意（首次系统分离 count vs confusability），但实际可操作建议有限，所有干预方向均失败 |\n| Reproducibility | 4/5 | 实验细节充分（model版本、decoding参数、prompt模板、seed），代码承诺 acceptance 后释放 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"Largely additive\" claim 在多个条件下不成立，属于 overclaim\n\n- 具体位置：Abstract（\"two largely additive dimensions\"）、§5（\"bounded interaction\"）、§7 Conclusion（\"two largely additive dimensions\"）\n- 问题：论文声称 count 和 confusability 两个维度\"大致可加\"。然而：\n  - **FewRel logit-scale**: interaction 0.111 logit, p=0.047（marginally significant），TOST inconclusive（p=0.209）。论文在 Appendix D 承认这一点，但 Abstract 和 Conclusion 未加此限定。\n  - **DocRED**: interaction +5.7pp，95% CI [-1.6, 13.0]，TOST at ±3pp p=0.77，完全无法建立 equivalence。论文限定为\"sentence-level RE\"，但 Abstract 和 Conclusion 中\"largely additive\"未加 task/scale 限定词。\n  - **NER**: factorial test inconclusive（p=0.50），无法分离两维度。\n  - **FewRel 2×2 factorial**: 也 inconclusive（p=0.56）。\n  - 实际上，\"largely additive\"仅由 FewRel 69-batch full-range regression 在 linear scale 上支撑（TOST p=0.003 at ±3pp），这是一个单数据集、单 scale 的结论。\n- 为什么影响接收：这是论文的核心 framing 之一，贯穿 Abstract/Introduction/Conclusion。如果只在 sentence-level RE 的 linear scale 上成立，就不应作为论文的主要标题级 claim。\n- 建议修改方向：(1) Abstract 和 Conclusion 中将 \"largely additive\" 限定为 \"bounded interaction under linear specification in sentence-level RE\"；(2) 明确承认在 DocRED 和 logit scale 上 additivity 不成立；(3) 或者重新 frame 为 \"two separable dimensions\"（不做 additivity claim）。\n\n**N2** [critical] Pairwise r²=1.3-1.7% 的效应量解读不够审慎，Cohen (1988) behavioral research 标准对 LLM 系统的适用性未论证\n\n- 具体位置：§4.2 Table 2、§2 Related Work（\"consistent with individual-difference predictors in behavioral research\"）、Limitations item 2\n- 问题：\n  - r²=1.3-1.7% 意味着 SCS 仅解释 type confusion 方差的 1.3-1.7%，剩余 >98% 由其他因素决定。\n  - 论文引用 Cohen (1988) 和 Lakens (2013) 的 behavioral research 标准来为小效应量辩护。但 Cohen 的标准是为心理学个体差异研究设计的，其中 r=0.1（r²=1%）被认为\"small but meaningful\"是因为在真实人群中的可检测效应有实际意义。LLM 系统是确定性的（greedy decoding），变量可控程度远高于行为研究，没有理由直接套用这个标准。\n  - 论文的 aggregation simulation（Appendix H）展示了 pair→batch 3x amplification，这比直接引用 Cohen 更有说服力，但模拟本身依赖 conditional r²=7%（只看非零混淆对），而非 unconditional 1.3%。\n- 为什么影响接收：如果 SCS 作为 confusability 的代理指标只解释 1.3% 方差，那 \"confusability predicts type confusion\" 这个 claim 的实际意义需要更谨慎的论述。审稿人可能质疑：是 SCS 本身不是好指标，还是 confusability 本身不是重要因素？\n- 建议修改方向：(1) 不引用 Cohen 的行为研究标准，改为直接用 batch-level R²=22-53% 作为主要证据，pairwise 作为补充；(2) 讨论为什么 pairwise 效应小但 batch-level 效应大（已有 aggregation simulation，但应提到正文而非仅 appendix）；(3) 讨论 SCS 作为代理指标的局限性（可能需要更精细的 confusability 指标，如基于 in-context confusion matrix 的指标）。\n\n**N3** [critical] BCS 对 NER 无 batch-level 信号，削弱 \"two-dimensional\" 框架的通用性\n\n- 具体位置：§4.3（\"BCS shows no batch-level signal for NER\"）、§5（\"NER batch-level BCS shows no predictive signal\"）、Discussion（\"RE-specific\"）\n- 问题：\n  - 论文提出的是一个跨任务的 \"two-dimensional degradation\" 框架（Abstract: \"across NER, RE, and event detection\"）。\n  - 但实际结果显示：Dimension 2 (confusability) 的 batch-level 效应**仅在 RE 的 forced-choice format 下有效**。NER r≈0（n=450），NER factorial inconclusive，MAVEN 有 centrality confound。\n  - 论文在 Discussion 中诊断了原因（forced-choice vs multi-span，RE 的 constrained decoding 把所有 error 都导向 type substitution），这个解释合理。但问题是：如果 BCS 只在 RE 有效，那 \"two-dimensional\" 是 RE 的特性还是 IE 的通用属性？\n  - Abstract 开头写 \"across NER, RE, and event detection\"，给人印象是三个任务都验证了两个维度。但实际上 NER 只验证了 Dimension 1（count curve）和 pairwise level 的 SCS，batch-level BCS 完全不工作。\n- 为什么影响接收：论文的贡献声明可能误导读者。如果一个 reviewer 只看 Abstract 和 Introduction，会认为两个维度在三个任务上都成立。\n- 建议修改方向：Abstract 和 Introduction 中明确标注 BCS batch-level 预测仅限 RE forced-choice format；将 \"across NER, RE, and ED\" 改为更精确的表述；或者将 NER 的 pairwise evidence 和 RE 的 batch-level evidence 分开表述。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] TOST equivalence margin ±3pp 的选择虽有 justification 但不够保守\n\n- 具体位置：Appendix D（§ Equivalence margin justification）、Table 6\n- 问题：\n  - ±3pp margin 在 ±2pp 时仅 marginally equivalent（p=0.047），±1pp inconclusive（p=0.278）。\n  - 论文称 3pp ≈ 0.5×batch SD，相当于 Cohen's d=0.5（medium effect）。但这里的 equivalence testing 是要证明 interaction **小**，用 \"medium effect\" 作为 bound 实际上是说 \"interaction 不超过中等效应\"，这并不令人信服——理想的 additivity claim 应该在更小的 margin 下成立。\n  - 论文的 sensitivity analysis（Table 6）是一个加分项，但恰恰展示了 ±1pp 下 inconclusive，说明精确的 additivity 无法建立。\n  - 此外，interaction 的 point estimate 是 0.47pp，但 90% CI 是 [-1.0, 2.0]。CI 上界 2.0pp 在 main effect 只有 2.2pp 的情况下，意味着 interaction 可能接近 main effect 大小——这不是\"可忽略\"的交互。\n- 建议：正文中应更明确地讨论 equivalence bound 的选择对结论的影响；将 \"largely additive\" 弱化为 \"bounded interaction at the ±3pp level\"。\n\n**W2** [warning] 引用 Rothman (1990) 拒绝多重比较校正的理由不够充分\n\n- 具体位置：Limitations 段落（\"Multiple comparisons\"）、Appendix G（prompt variants）\n- 问题：\n  - Rothman (1990) 的立场在统计学界有争议。该论文是流行病学语境下写的，核心观点是\"每个假设独立评估\"，但前提是每个比较都有独立的科学理由。\n  - 论文的 cross-dataset 比较确实可以视为独立复制，这部分引用 Rothman 是合理的。\n  - 但 Appendix G 的 cross-prompt-variant 分析（4 variants × 2 counts = 8 comparisons），论文用\"directional consistency（7/8 negative）\"来论证而非校正 p-value。这8个比较并非独立假设——它们测试的是同一个底层效应在不同 prompt 下的表现。在 count=8 时 4 个 variant 都不显著，count=32 时只有 2/4 显著（p=0.043, 0.009），这更像是 power 问题而非 robust evidence。\n  - 同时，核心分析中 p<0.001 的结果确实不需要多重比较校正（不会因校正而翻转），但边缘显著的二级分析（如 logit interaction p=0.047, 2pp TOST p=0.047）需要更谨慎解读。\n- 建议：对 cross-dataset 复制保留 Rothman 论证；对 within-study 二级分析（prompt variants, marginal results）加注 caveat。\n\n**W3** [warning] DocRED 样本量（5 batches per count level）过小，power 不足\n\n- 具体位置：§3.3（\"5 for DocRED and MAVEN\"）、§4.3（DocRED BCS results）\n- 问题：\n  - FewRel 使用 25 batches per count level，DocRED 和 MAVEN 仅 5 batches。论文在脚注中解释了原因（higher per-batch evaluation cost），但 5 batches 的 count curve 统计 power 极低。\n  - DocRED BCS-controlled 实验使用 n=35（5 high + 5 low + 25 random），这个样本量尚可。但 count curve 的 5 batches 无法提供可靠的趋势估计。\n  - DocRED 的 factorial interaction +5.7pp 的宽 CI [-1.6, 13.0] 很可能部分归因于样本量不足。\n- 建议：如果计算资源允许，增加 DocRED count curve batches 至少到 15；如果不可行，明确讨论 5-batch count curve 的 power limitation。\n\n**W4** [warning] Dimension 2 未在 proprietary model 上验证，cross-model 验证存在缺口\n\n- 具体位置：Appendix M（Gemini 2.5 Flash）、Limitations item 1\n- 问题：\n  - Dimension 1 跨模型验证充分（Qwen3-32B, Llama-8B, Llama-70B, Gemini 2.5 Flash），但 Dimension 2（BCS-controlled）仅在 open-weight 模型上验证。\n  - Gemini count-64 仅基于 11/25 batches（\"partial\"），论文未解释为什么部分数据缺失（API rate limit? 费用?）。\n  - Llama-70B 的 BCS 验证仅在 count=16 进行（单个 count level），不如 Qwen3 的多 count level 验证全面。\n  - 论文在 Limitations 中承认了 proprietary model 缺口，但鉴于 proprietary model 在实际应用中更常被使用，这是一个重要的外部有效性问题。\n- 建议：解释 Gemini partial data 的原因；如果有条件，补充 Gemini 在至少一个 count level 的 BCS-controlled 实验；明确标注这是 future work 而非已验证。\n\n**W5** [warning] Negative results (SDGD) 的归因分析虽有诊断但缺少解决方向的验证\n\n- 具体位置：§6（SDGD）、Appendix B（SDGD Full Protocol）、Appendix C（Routing Strategies）\n- 问题：\n  - Oracle routing +29.8pp 但所有 practical routing 均 below baseline。这说明**如果 routing 能解决**，schema decomposition 是有价值的。\n  - 论文诊断了两个 failure mode：merge amplification (NER) 和 routing failure (RE)。对 merge amplification 的分析清晰（precision collapse + recall bounded）。\n  - 但对 routing failure 的分析不够深入：为什么 \"73.4% of instances receive positive predictions from 3-5 sub-schemas simultaneously\"？这是 constrained decoding (enum constraint) 强制产生 positive prediction 的结果，论文也指出了 none-rate 只有 20-40%。但这意味着**问题不在于 schema decomposition 本身，而在于 constrained decoding 与 decomposition 的交互**。如果允许 \"none\" 有更高概率（如调整 prior），routing 可能改善。\n  - 论文最后一句 \"Promising avenues include coarse-to-fine pipelines and retrieval-based routing\" 过于简略。\n- 建议：讨论 constrained decoding 与 routing failure 的交互关系；考虑是否有简单的 ablation（如去掉 enum constraint 后的 routing performance）来验证归因。\n\n**W6** [warning] FewRel train/val split-origin 控制可以更强\n\n- 具体位置：Appendix I（Split-Origin Covariate Analysis）、Limitations item 5\n- 问题：\n  - FewRel 组合了 64 train-split 和 16 val-split types，train-origin types 准确率低 8.8pp（p=0.06，marginally nonsignificant）。\n  - 论文用 covariate analysis 展示 BCS 效应控制 split-origin 后不变（β_BCS unchanged），这是一个好的控制。\n  - 但核心问题是：为什么不直接在 16 个 val-origin types 上做独立验证？论文在 Appendix F 报告了 held-out validation（SCS-confusion ρ=0.216, p=0.018 on 120 val-only pairs），这比 covariate analysis 更有说服力，但埋在 Appendix 深处。\n  - 此外，FewRel (2018) 确实有 data contamination 风险。虽然 train-origin types 反而准确率更低（与 contamination 假设相反），但这个 argument 不完全令人信服——contamination 可能以更复杂的方式影响（如改变 type 间 confusion pattern 而非整体准确率）。\n- 建议：将 held-out validation 结果提到正文（即使简短提及）；对 contamination 的讨论更加 nuanced。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: references.bib 中 `jagannatha2020calibrating` 未被引用（orphan entry）。\n- **M2**: Table 1 的 Embedding 列显示 Few-NERD 用 Qwen3-32B 而其他用 MiniLM，但 BCS Range 注明 \"ranges are not comparable across embedding models\"。这意味着跨数据集的 BCS range 比较（如 FewRel 0.42-0.97 vs MAVEN 0.87-0.97）无意义，但论文某些地方隐含了这种比较（如 DocRED \"wider confusability range\"）。\n- **M3**: Appendix M (Gemini) 的 count-64 标注 \"partial (11/25 batches)\" 但未解释原因。\n- **M4**: 论文在 §3.4 提到 \"v1 requests character offsets\" 且 \"96.5% of predicted offsets were hallucinated\"，这是一个有趣的附带发现但未被充分讨论——如果 v1 的 offset hallucination 率如此高，为什么仍然报告 v1 结果？（虽然评估用的是 text matching 而非 offset matching，但这暗示 v1 格式可能以其他方式影响提取质量。）\n- **M5**: Limitations §3 提到 unconstrained decoding ablation (n=25) 消除了 BCS-accuracy 相关，但只在 Discussion 中简要提及。建议将此作为 format dependency 的正式 finding。\n\n---\n\n## 主要优势\n\n1. **实验设计精良**: Count curves + BCS-controlled 两种范式的组合设计巧妙，有效分离了 count 和 confusability。within-pool 控制（从 80-rel pool 抽 16-rel subsets）排除了 pool composition confound。FewRel 的 balanced design 自然消除了 type frequency confound。\n2. **统计处理透明度高**: 使用 TOST equivalence testing（而非仅看 null result）、bootstrap CI、permutation test、cluster bootstrap，并在 Appendix 中报告了多个 sensitivity analysis（TOST margin sweep、logit-scale、BCS aggregation method）。在 NLP 论文中这个统计严谨程度明显高于平均。\n3. **诚实报告 negative results**: SDGD 失败和 label renaming 实验均如实报告，且有合理的 failure mode 诊断。MAVEN centrality confound 的发现和处理也展现了方法论上的严谨。\n4. **Cross-model validation 范围广**: 4 个模型（Qwen3-32B, Llama-8B, Llama-70B, Gemini 2.5 Flash），覆盖不同 scale 和 family，Dimension 1 的 cross-model 证据令人信服。\n5. **Appendix 信息量大**: 14 个 Appendix 节提供了大量 sensitivity analysis、alternative specifications、和 robustness checks，审稿人可以深入验证每个 claim。\n\n---\n\n## Missing References\n\n- 未发现严重缺漏。Related Work 覆盖了直接相关方法（LLM-PEE, PARSE, UniNER 等）、baseline 论文（FewRel, Few-NERD, DocRED, MAVEN）、评测框架、和统计方法论参考。引用量级（~70 entries）与顶会长文一致。\n- 可以考虑添加：(1) 关于 LLM calibration 与 constrained decoding 交互的工作（与 routing failure 分析相关）；(2) 关于 equivalence testing 在 ML 中应用的更新文献（Lakens 之外）。\n\n---\n\n## Detailed Comments\n\n### 关于实验设计合理性\n\n1. **Count curves + BCS-controlled 的双范式设计**：这是本文方法论上的核心创新。Count curves 展示 trend direction，BCS-controlled 实验量化 confusability 独立效应。设计合理，两个范式互补。\n\n2. **样本量**: FewRel 的 25 batches/count level 对于 regression analysis 足够（n=69 for full-range, n=100 for within-pool）。DocRED 的 5 batches/count level 明显不足（已在 W3 中标注）。BCS-controlled 的 extreme batch design（1 low + 1 high + 25 random）在 16-rel pilot 中 power 有限（acknowledged by authors），80-rel 条件下 power 充足。\n\n3. **Greedy decoding single seed**: 论文用 greedy decoding (temp=0, seed 42) 减少随机性，Appendix N 的 variance decomposition 支持 batch composition 是主要方差来源（>5x intra-batch vs inter-seed）。这是合理的设计选择，但 seed=42 是一个特定选择，few-shot 实验中 example selection 的随机性未被控制。\n\n### 关于统计分析严谨性\n\n4. **TOST 的使用**: 概念上正确（equivalence testing 而非 null hypothesis testing），但 margin 选择（±3pp）的 justification 依赖 Cohen's d=0.5 analogy，而这个 analogy 未被充分论证（N2）。Sensitivity analysis（Table 6）是加分项。\n\n5. **Bootstrap CI**: 使用 percentile bootstrap (B=10,000 for pairs, B=1,000 for batches) 是 standard practice。Cluster bootstrap for type-level dependencies (Table 2) 是正确的。\n\n6. **Conditioning on nonzero confusion pairs**: 论文报告 conditional r²=7% 时诚实标注了 \"conditioning on the dependent variable may inflate this\"。但 aggregation simulation 使用 conditional r²（而非 unconditional）来 match 观测到的 batch-level R²=0.218，说明 conditional model 是更好的解释——论文应该更清楚地说明为什么 conditional 在这里是合理的（因为 89% 的 type pairs 永远不会互相混淆，只有语义近邻才 \"active\"）。\n\n### 关于跨模型/跨数据集验证\n\n7. **Dimension 1 cross-model**: Qwen3→Llama-8B（Few-NERD -43pp, per-batch r=0.725）、Qwen3→Llama-70B（RE slope near-identical: -30.7 vs -30.1pp）、Qwen3→Gemini（monotonic decline, ρ=-1.0 for count 4-32）。证据充分。\n\n8. **Dimension 2 cross-model**: Llama-8B BCS gap 77-87% of Qwen3（Table A2）；Llama-70B Δ=+10.9pp（CI excludes zero）。但未在 Gemini 上验证——这是一个 gap（W4）。\n\n### 关于 Negative Results\n\n9. **SDGD failure 归因合理但不完整**: merge amplification 的诊断清晰（precision 0.563→0.210，recall 有限提升）。routing failure 归因于 constrained decoding 迫使 positive prediction 也合理。但缺少一个关键实验：在 RE 上去掉 enum constraint 后 routing 是否改善？论文的 unconstrained ablation（§7）只检查了 BCS-accuracy correlation 是否消失，未检查 routing performance。\n\n10. **Oracle routing +29.8pp vs practical routing all below baseline**: 这个 gap 提示 schema decomposition 的理论上限很高，瓶颈完全在 routing。论文应该更强调这一点——这对 future work 方向有重大指导意义。\n\n---\n\n## Overall Assessment 理由\n\n本文是一篇扎实的实证分析论文，在实验设计和统计处理上明显优于大多数 NLP 论文。two-dimensional decomposition 框架有概念价值，negative results（SDGD failure, renaming failure）对社区有参考意义。\n\n但有三个问题拉低评分：(1) \"largely additive\" 作为核心 claim 仅在 sentence-level RE linear scale 上成立，overclaim 明显；(2) BCS batch-level 效应仅在 RE forced-choice format 下有效，框架的通用性有限；(3) pairwise 效应量极小（r²≈1.5%），所有实际干预（分解、重命名、few-shot）均失败，论文的 practical impact 很弱。\n\n如果 N1（overclaim）和 N3（通用性限定）得到修复，论文的诚实度和分析质量足以支持 Findings 接收。以目前的 framing 看，Borderline Conference (3.5) 是我的评分，如果 overclaim 不修，可能降至 3.0 (Findings)。\n",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿报告 — Round 1\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 (via ARR May 2026 cycle)\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n---\n\n## Paper Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度导致的性能退化问题，提出将退化分解为两个维度：type count（维度1）和 type confusability（维度2）。作者定义了 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 来量化 type 间语义混淆度，在 Few-NERD (NER)、FewRel (RE)、DocRED (doc-RE)、MAVEN (ED) 四个数据集上进行了 count curves 和 BCS-controlled 两种实验范式的系统评估。主要发现：(1) 两个维度\"大致可加\"（在 sentence-level RE 上）；(2) BCS 能解释 RE 22-53% 的跨 batch 准确率方差，但对 NER 无 batch-level 信号；(3) schema 分解因 merge amplification (NER) 和 routing failure (RE) 而失败。Cross-model 验证覆盖 Qwen3-32B、Llama-8B/70B、Gemini 2.5 Flash。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n**Confidence**: 4 (Quite sure. I tried to check the important points carefully.)\n**一句话总结**: 实验设计严谨、统计处理透明度高于 NLP 论文平均水准，但 \"largely additive\" 的核心 claim 在 logit scale 和 DocRED 上站不住脚，pairwise 效应量极小（r²=1.3-1.7%），且所有实际干预方向（分解、重命名、few-shot）均失败，实际可操作价值有限。\n\n---\n\n## 官方维度打分（来自 ARR Review Form，2025年2月更新版）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨，统计工具使用恰当（TOST、permutation test、bootstrap CI），但核心 claim \"largely additive\" overclaim，且多个条件下 TOST inconclusive |\n| Excitement | 3.0/5 | 分析框架有新意（首次系统分离 count vs confusability），但实际可操作建议有限，所有干预方向均失败 |\n| Reproducibility | 4/5 | 实验细节充分（model版本、decoding参数、prompt模板、seed），代码承诺 acceptance 后释放 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"Largely additive\" claim 在多个条件下不成立，属于 overclaim\n\n- 具体位置：Abstract（\"two largely additive dimensions\"）、§5（\"bounded interaction\"）、§7 Conclusion（\"two largely additive dimensions\"）\n- 问题：论文声称 count 和 confusability 两个维度\"大致可加\"。然而：\n  - **FewRel logit-scale**: interaction 0.111 logit, p=0.047（marginally significant），TOST inconclusive（p=0.209）。论文在 Appendix D 承认这一点，但 Abstract 和 Conclusion 未加此限定。\n  - **DocRED**: interaction +5.7pp，95% CI [-1.6, 13.0]，TOST at ±3pp p=0.77，完全无法建立 equivalence。论文限定为\"sentence-level RE\"，但 Abstract 和 Conclusion 中\"largely additive\"未加 task/scale 限定词。\n  - **NER**: factorial test inconclusive（p=0.50），无法分离两维度。\n  - **FewRel 2×2 factorial**: 也 inconclusive（p=0.56）。\n  - 实际上，\"largely additive\"仅由 FewRel 69-batch full-range regression 在 linear scale 上支撑（TOST p=0.003 at ±3pp），这是一个单数据集、单 scale 的结论。\n- 为什么影响接收：这是论文的核心 framing 之一，贯穿 Abstract/Introduction/Conclusion。如果只在 sentence-level RE 的 linear scale 上成立，就不应作为论文的主要标题级 claim。\n- 建议修改方向：(1) Abstract 和 Conclusion 中将 \"largely additive\" 限定为 \"bounded interaction under linear specification in sentence-level RE\"；(2) 明确承认在 DocRED 和 logit scale 上 additivity 不成立；(3) 或者重新 frame 为 \"two separable dimensions\"（不做 additivity claim）。\n\n**N2** [critical] Pairwise r²=1.3-1.7% 的效应量解读不够审慎，Cohen (1988) behavioral research 标准对 LLM 系统的适用性未论证\n\n- 具体位置：§4.2 Table 2、§2 Related Work（\"consistent with individual-difference predictors in behavioral research\"）、Limitations item 2\n- 问题：\n  - r²=1.3-1.7% 意味着 SCS 仅解释 type confusion 方差的 1.3-1.7%，剩余 >98% 由其他因素决定。\n  - 论文引用 Cohen (1988) 和 Lakens (2013) 的 behavioral research 标准来为小效应量辩护。但 Cohen 的标准是为心理学个体差异研究设计的，其中 r=0.1（r²=1%）被认为\"small but meaningful\"是因为在真实人群中的可检测效应有实际意义。LLM 系统是确定性的（greedy decoding），变量可控程度远高于行为研究，没有理由直接套用这个标准。\n  - 论文的 aggregation simulation（Appendix H）展示了 pair→batch 3x amplification，这比直接引用 Cohen 更有说服力，但模拟本身依赖 conditional r²=7%（只看非零混淆对），而非 unconditional 1.3%。\n- 为什么影响接收：如果 SCS 作为 confusability 的代理指标只解释 1.3% 方差，那 \"confusability predicts type confusion\" 这个 claim 的实际意义需要更谨慎的论述。审稿人可能质疑：是 SCS 本身不是好指标，还是 confusability 本身不是重要因素？\n- 建议修改方向：(1) 不引用 Cohen 的行为研究标准，改为直接用 batch-level R²=22-53% 作为主要证据，pairwise 作为补充；(2) 讨论为什么 pairwise 效应小但 batch-level 效应大（已有 aggregation simulation，但应提到正文而非仅 appendix）；(3) 讨论 SCS 作为代理指标的局限性（可能需要更精细的 confusability 指标，如基于 in-context confusion matrix 的指标）。\n\n**N3** [critical] BCS 对 NER 无 batch-level 信号，削弱 \"two-dimensional\" 框架的通用性\n\n- 具体位置：§4.3（\"BCS shows no batch-level signal for NER\"）、§5（\"NER batch-level BCS shows no predictive signal\"）、Discussion（\"RE-specific\"）\n- 问题：\n  - 论文提出的是一个跨任务的 \"two-dimensional degradation\" 框架（Abstract: \"across NER, RE, and event detection\"）。\n  - 但实际结果显示：Dimension 2 (confusability) 的 batch-level 效应**仅在 RE 的 forced-choice format 下有效**。NER r≈0（n=450），NER factorial inconclusive，MAVEN 有 centrality confound。\n  - 论文在 Discussion 中诊断了原因（forced-choice vs multi-span，RE 的 constrained decoding 把所有 error 都导向 type substitution），这个解释合理。但问题是：如果 BCS 只在 RE 有效，那 \"two-dimensional\" 是 RE 的特性还是 IE 的通用属性？\n  - Abstract 开头写 \"across NER, RE, and event detection\"，给人印象是三个任务都验证了两个维度。但实际上 NER 只验证了 Dimension 1（count curve）和 pairwise level 的 SCS，batch-level BCS 完全不工作。\n- 为什么影响接收：论文的贡献声明可能误导读者。如果一个 reviewer 只看 Abstract 和 Introduction，会认为两个维度在三个任务上都成立。\n- 建议修改方向：Abstract 和 Introduction 中明确标注 BCS batch-level 预测仅限 RE forced-choice format；将 \"across NER, RE, and ED\" 改为更精确的表述；或者将 NER 的 pairwise evidence 和 RE 的 batch-level evidence 分开表述。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] TOST equivalence margin ±3pp 的选择虽有 justification 但不够保守\n\n- 具体位置：Appendix D（§ Equivalence margin justification）、Table 6\n- 问题：\n  - ±3pp margin 在 ±2pp 时仅 marginally equivalent（p=0.047），±1pp inconclusive（p=0.278）。\n  - 论文称 3pp ≈ 0.5×batch SD，相当于 Cohen's d=0.5（medium effect）。但这里的 equivalence testing 是要证明 interaction **小**，用 \"medium effect\" 作为 bound 实际上是说 \"interaction 不超过中等效应\"，这并不令人信服——理想的 additivity claim 应该在更小的 margin 下成立。\n  - 论文的 sensitivity analysis（Table 6）是一个加分项，但恰恰展示了 ±1pp 下 inconclusive，说明精确的 additivity 无法建立。\n  - 此外，interaction 的 point estimate 是 0.47pp，但 90% CI 是 [-1.0, 2.0]。CI 上界 2.0pp 在 main effect 只有 2.2pp 的情况下，意味着 interaction 可能接近 main effect 大小——这不是\"可忽略\"的交互。\n- 建议：正文中应更明确地讨论 equivalence bound 的选择对结论的影响；将 \"largely additive\" 弱化为 \"bounded interaction at the ±3pp level\"。\n\n**W2** [warning] 引用 Rothman (1990) 拒绝多重比较校正的理由不够充分\n\n- 具体位置：Limitations 段落（\"Multiple comparisons\"）、Appendix G（prompt variants）\n- 问题：\n  - Rothman (1990) 的立场在统计学界有争议。该论文是流行病学语境下写的，核心观点是\"每个假设独立评估\"，但前提是每个比较都有独立的科学理由。\n  - 论文的 cross-dataset 比较确实可以视为独立复制，这部分引用 Rothman 是合理的。\n  - 但 Appendix G 的 cross-prompt-variant 分析（4 variants × 2 counts = 8 comparisons），论文用\"directional consistency（7/8 negative）\"来论证而非校正 p-value。这8个比较并非独立假设——它们测试的是同一个底层效应在不同 prompt 下的表现。在 count=8 时 4 个 variant 都不显著，count=32 时只有 2/4 显著（p=0.043, 0.009），这更像是 power 问题而非 robust evidence。\n  - 同时，核心分析中 p<0.001 的结果确实不需要多重比较校正（不会因校正而翻转），但边缘显著的二级分析（如 logit interaction p=0.047, 2pp TOST p=0.047）需要更谨慎解读。\n- 建议：对 cross-dataset 复制保留 Rothman 论证；对 within-study 二级分析（prompt variants, marginal results）加注 caveat。\n\n**W3** [warning] DocRED 样本量（5 batches per count level）过小，power 不足\n\n- 具体位置：§3.3（\"5 for DocRED and MAVEN\"）、§4.3（DocRED BCS results）\n- 问题：\n  - FewRel 使用 25 batches per count level，DocRED 和 MAVEN 仅 5 batches。论文在脚注中解释了原因（higher per-batch evaluation cost），但 5 batches 的 count curve 统计 power 极低。\n  - DocRED BCS-controlled 实验使用 n=35（5 high + 5 low + 25 random），这个样本量尚可。但 count curve 的 5 batches 无法提供可靠的趋势估计。\n  - DocRED 的 factorial interaction +5.7pp 的宽 CI [-1.6, 13.0] 很可能部分归因于样本量不足。\n- 建议：如果计算资源允许，增加 DocRED count curve batches 至少到 15；如果不可行，明确讨论 5-batch count curve 的 power limitation。\n\n**W4** [warning] Dimension 2 未在 proprietary model 上验证，cross-model 验证存在缺口\n\n- 具体位置：Appendix M（Gemini 2.5 Flash）、Limitations item 1\n- 问题：\n  - Dimension 1 跨模型验证充分（Qwen3-32B, Llama-8B, Llama-70B, Gemini 2.5 Flash），但 Dimension 2（BCS-controlled）仅在 open-weight 模型上验证。\n  - Gemini count-64 仅基于 11/25 batches（\"partial\"），论文未解释为什么部分数据缺失（API rate limit? 费用?）。\n  - Llama-70B 的 BCS 验证仅在 count=16 进行（单个 count level），不如 Qwen3 的多 count level 验证全面。\n  - 论文在 Limitations 中承认了 proprietary model 缺口，但鉴于 proprietary model 在实际应用中更常被使用，这是一个重要的外部有效性问题。\n- 建议：解释 Gemini partial data 的原因；如果有条件，补充 Gemini 在至少一个 count level 的 BCS-controlled 实验；明确标注这是 future work 而非已验证。\n\n**W5** [warning] Negative results (SDGD) 的归因分析虽有诊断但缺少解决方向的验证\n\n- 具体位置：§6（SDGD）、Appendix B（SDGD Full Protocol）、Appendix C（Routing Strategies）\n- 问题：\n  - Oracle routing +29.8pp 但所有 practical routing 均 below baseline。这说明**如果 routing 能解决**，schema decomposition 是有价值的。\n  - 论文诊断了两个 failure mode：merge amplification (NER) 和 routing failure (RE)。对 merge amplification 的分析清晰（precision collapse + recall bounded）。\n  - 但对 routing failure 的分析不够深入：为什么 \"73.4% of instances receive positive predictions from 3-5 sub-schemas simultaneously\"？这是 constrained decoding (enum constraint) 强制产生 positive prediction 的结果，论文也指出了 none-rate 只有 20-40%。但这意味着**问题不在于 schema decomposition 本身，而在于 constrained decoding 与 decomposition 的交互**。如果允许 \"none\" 有更高概率（如调整 prior），routing 可能改善。\n  - 论文最后一句 \"Promising avenues include coarse-to-fine pipelines and retrieval-based routing\" 过于简略。\n- 建议：讨论 constrained decoding 与 routing failure 的交互关系；考虑是否有简单的 ablation（如去掉 enum constraint 后的 routing performance）来验证归因。\n\n**W6** [warning] FewRel train/val split-origin 控制可以更强\n\n- 具体位置：Appendix I（Split-Origin Covariate Analysis）、Limitations item 5\n- 问题：\n  - FewRel 组合了 64 train-split 和 16 val-split types，train-origin types 准确率低 8.8pp（p=0.06，marginally nonsignificant）。\n  - 论文用 covariate analysis 展示 BCS 效应控制 split-origin 后不变（β_BCS unchanged），这是一个好的控制。\n  - 但核心问题是：为什么不直接在 16 个 val-origin types 上做独立验证？论文在 Appendix F 报告了 held-out validation（SCS-confusion ρ=0.216, p=0.018 on 120 val-only pairs），这比 covariate analysis 更有说服力，但埋在 Appendix 深处。\n  - 此外，FewRel (2018) 确实有 data contamination 风险。虽然 train-origin types 反而准确率更低（与 contamination 假设相反），但这个 argument 不完全令人信服——contamination 可能以更复杂的方式影响（如改变 type 间 confusion pattern 而非整体准确率）。\n- 建议：将 held-out validation 结果提到正文（即使简短提及）；对 contamination 的讨论更加 nuanced。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: references.bib 中 `jagannatha2020calibrating` 未被引用（orphan entry）。\n- **M2**: Table 1 的 Embedding 列显示 Few-NERD 用 Qwen3-32B 而其他用 MiniLM，但 BCS Range 注明 \"ranges are not comparable across embedding models\"。这意味着跨数据集的 BCS range 比较（如 FewRel 0.42-0.97 vs MAVEN 0.87-0.97）无意义，但论文某些地方隐含了这种比较（如 DocRED \"wider confusability range\"）。\n- **M3**: Appendix M (Gemini) 的 count-64 标注 \"partial (11/25 batches)\" 但未解释原因。\n- **M4**: 论文在 §3.4 提到 \"v1 requests character offsets\" 且 \"96.5% of predicted offsets were hallucinated\"，这是一个有趣的附带发现但未被充分讨论——如果 v1 的 offset hallucination 率如此高，为什么仍然报告 v1 结果？（虽然评估用的是 text matching 而非 offset matching，但这暗示 v1 格式可能以其他方式影响提取质量。）\n- **M5**: Limitations §3 提到 unconstrained decoding ablation (n=25) 消除了 BCS-accuracy 相关，但只在 Discussion 中简要提及。建议将此作为 format dependency 的正式 finding。\n\n---\n\n## 主要优势\n\n1. **实验设计精良**: Count curves + BCS-controlled 两种范式的组合设计巧妙，有效分离了 count 和 confusability。within-pool 控制（从 80-rel pool 抽 16-rel subsets）排除了 pool composition confound。FewRel 的 balanced design 自然消除了 type frequency confound。\n2. **统计处理透明度高**: 使用 TOST equivalence testing（而非仅看 null result）、bootstrap CI、permutation test、cluster bootstrap，并在 Appendix 中报告了多个 sensitivity analysis（TOST margin sweep、logit-scale、BCS aggregation method）。在 NLP 论文中这个统计严谨程度明显高于平均。\n3. **诚实报告 negative results**: SDGD 失败和 label renaming 实验均如实报告，且有合理的 failure mode 诊断。MAVEN centrality confound 的发现和处理也展现了方法论上的严谨。\n4. **Cross-model validation 范围广**: 4 个模型（Qwen3-32B, Llama-8B, Llama-70B, Gemini 2.5 Flash），覆盖不同 scale 和 family，Dimension 1 的 cross-model 证据令人信服。\n5. **Appendix 信息量大**: 14 个 Appendix 节提供了大量 sensitivity analysis、alternative specifications、和 robustness checks，审稿人可以深入验证每个 claim。\n\n---\n\n## Missing References\n\n- 未发现严重缺漏。Related Work 覆盖了直接相关方法（LLM-PEE, PARSE, UniNER 等）、baseline 论文（FewRel, Few-NERD, DocRED, MAVEN）、评测框架、和统计方法论参考。引用量级（~70 entries）与顶会长文一致。\n- 可以考虑添加：(1) 关于 LLM calibration 与 constrained decoding 交互的工作（与 routing failure 分析相关）；(2) 关于 equivalence testing 在 ML 中应用的更新文献（Lakens 之外）。\n\n---\n\n## Detailed Comments\n\n### 关于实验设计合理性\n\n1. **Count curves + BCS-controlled 的双范式设计**：这是本文方法论上的核心创新。Count curves 展示 trend direction，BCS-controlled 实验量化 confusability 独立效应。设计合理，两个范式互补。\n\n2. **样本量**: FewRel 的 25 batches/count level 对于 regression analysis 足够（n=69 for full-range, n=100 for within-pool）。DocRED 的 5 batches/count level 明显不足（已在 W3 中标注）。BCS-controlled 的 extreme batch design（1 low + 1 high + 25 random）在 16-rel pilot 中 power 有限（acknowledged by authors），80-rel 条件下 power 充足。\n\n3. **Greedy decoding single seed**: 论文用 greedy decoding (temp=0, seed 42) 减少随机性，Appendix N 的 variance decomposition 支持 batch composition 是主要方差来源（>5x intra-batch vs inter-seed）。这是合理的设计选择，但 seed=42 是一个特定选择，few-shot 实验中 example selection 的随机性未被控制。\n\n### 关于统计分析严谨性\n\n4. **TOST 的使用**: 概念上正确（equivalence testing 而非 null hypothesis testing），但 margin 选择（±3pp）的 justification 依赖 Cohen's d=0.5 analogy，而这个 analogy 未被充分论证（N2）。Sensitivity analysis（Table 6）是加分项。\n\n5. **Bootstrap CI**: 使用 percentile bootstrap (B=10,000 for pairs, B=1,000 for batches) 是 standard practice。Cluster bootstrap for type-level dependencies (Table 2) 是正确的。\n\n6. **Conditioning on nonzero confusion pairs**: 论文报告 conditional r²=7% 时诚实标注了 \"conditioning on the dependent variable may inflate this\"。但 aggregation simulation 使用 conditional r²（而非 unconditional）来 match 观测到的 batch-level R²=0.218，说明 conditional model 是更好的解释——论文应该更清楚地说明为什么 conditional 在这里是合理的（因为 89% 的 type pairs 永远不会互相混淆，只有语义近邻才 \"active\"）。\n\n### 关于跨模型/跨数据集验证\n\n7. **Dimension 1 cross-model**: Qwen3→Llama-8B（Few-NERD -43pp, per-batch r=0.725）、Qwen3→Llama-70B（RE slope near-identical: -30.7 vs -30.1pp）、Qwen3→Gemini（monotonic decline, ρ=-1.0 for count 4-32）。证据充分。\n\n8. **Dimension 2 cross-model**: Llama-8B BCS gap 77-87% of Qwen3（Table A2）；Llama-70B Δ=+10.9pp（CI excludes zero）。但未在 Gemini 上验证——这是一个 gap（W4）。\n\n### 关于 Negative Results\n\n9. **SDGD failure 归因合理但不完整**: merge amplification 的诊断清晰（precision 0.563→0.210，recall 有限提升）。routing failure 归因于 constrained decoding 迫使 positive prediction 也合理。但缺少一个关键实验：在 RE 上去掉 enum constraint 后 routing 是否改善？论文的 unconstrained ablation（§7）只检查了 BCS-accuracy correlation 是否消失，未检查 routing performance。\n\n10. **Oracle routing +29.8pp vs practical routing all below baseline**: 这个 gap 提示 schema decomposition 的理论上限很高，瓶颈完全在 routing。论文应该更强调这一点——这对 future work 方向有重大指导意义。\n\n---\n\n## Overall Assessment 理由\n\n本文是一篇扎实的实证分析论文，在实验设计和统计处理上明显优于大多数 NLP 论文。two-dimensional decomposition 框架有概念价值，negative results（SDGD failure, renaming failure）对社区有参考意义。\n\n但有三个问题拉低评分：(1) \"largely additive\" 作为核心 claim 仅在 sentence-level RE linear scale 上成立，overclaim 明显；(2) BCS batch-level 效应仅在 RE forced-choice format 下有效，框架的通用性有限；(3) pairwise 效应量极小（r²≈1.5%），所有实际干预（分解、重命名、few-shot）均失败，论文的 practical impact 很弱。\n\n如果 N1（overclaim）和 N3（通用性限定）得到修复，论文的诚实度和分析质量足以支持 Findings 接收。以目前的 framing 看，Borderline Conference (3.5) 是我的评分，如果 overclaim 不修，可能降至 3.0 (Findings)。\n",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1199 · 2026-05-19T04:36:54.777616+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4826
}
```

</details>

---


### Assistant

_source line 1200 · 2026-05-19T04:37:05.965031+00:00_

审稿报告已提交给 Review Director。

**总结**：

- **Overall**: 3.5 (Borderline Conference)
- **Soundness**: 3.5/5 | **Excitement**: 3.0/5 | **Reproducibility**: 4/5
- **3 个 Must-Fix**：(1) "largely additive" overclaim（仅在 sentence-level RE linear scale 成立），(2) pairwise r²=1.3-1.7% 效应量解读引用 Cohen behavioral research 标准不当，(3) BCS 对 NER 无 batch-level 信号，削弱 "two-dimensional" 框架通用性
- **6 个 Should-Fix**：TOST margin 不够保守、Rothman 多重比较论证不完整、DocRED 5 batches power 不足、Dimension 2 未在 proprietary model 验证、SDGD routing failure 分析不完整、split-origin 控制可更强
- **主要优势**：实验设计精良（双范式分离 count/confusability）、统计透明度高（TOST + bootstrap + sensitivity analysis）、诚实报告 negative results、cross-model 验证范围广

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 41

## Round 41

36 recorded events


### User

_source line 1201 · 2026-05-19T04:38:03.558182+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：请对 Reviewer 2 的审稿意见逐条回应

以下是 Reviewer 2 的完整审稿意见。请逐条回应：
- **[AGREE]**：同意并简要说明理由
- **[REBUT]**：反驳并提供证据（引用论文具体 Section/Table/Figure）

特别关注 R2 提出但你未提出的问题（R2-N1 Title "Predict", R2-N3 SCS novelty, R2-W2 renaming experiment, R2-W3 CrossAgentIE）以及你们评分差异的原因（你 3.5 vs R2 3.0）。

---

## Reviewer 2 完整审稿原文

**Overall Assessment**: 3.0 — Findings
**Soundness**: 3.5 | **Excitement**: 2.5 | **Confidence**: 4 | **Reproducibility**: 4

### Must-Fix:

**R2-N1** [critical] Title "Predict" 与实际 correlational evidence 不匹配
- Title 使用 "How Does Schema Complexity **Predict** Performance"，暗示因果预测力
- Limitations item 4 承认仅 correlational evidence
- Renaming 实验直接反驳朴素因果链（降低 SCS 反而降低准确率 3-9pp）
- Logit-scale TOST inconclusive (p=0.209)
- 建议改为 "Relate to" / "Affect" / "Shape"

**R2-N2** [critical] "Two-dimensional" framework 在 NER 上部分失效但 framing 未充分体现
- NER batch-level BCS 完全无预测信号 (r≈0, n=450)
- "Additive" 仅在 FewRel sentence-level RE linear scale 成立
- DocRED TOST 不成立 (p=0.77); NER factorial inconclusive (p=0.50); logit-scale inconclusive (p=0.209)
- Abstract 和 Introduction 未充分限定这些边界条件

**R2-N3** [critical] SCS 无新颖性，"controlled framework" 作为贡献的论证不足
- SCS = LLM-PEE 的 partitioning criterion（论文自己承认）
- "controlled experimental framework" 是自然的实验设计选择，并非方法论创新
- 核心发现（count dominates, similar types confuse more）直觉上不意外
- 效应量有限（~2pp typical, r²≈1.5% pairwise）
- 无可行缓解方案（SDGD失败/renaming反向/few-shot加剧）
- 建议：更深入对比 LLM-PEE merge 策略差异；强化 negative result actionable value；增加至少一个可行缓解实验

### Should-Fix:

**R2-W1** TOST ±3pp margin 选择值得质疑（与你的 W1 重叠）

**R2-W2** Renaming 实验削弱 SCS 实用价值但讨论不足
- SCS 实用价值依赖"降低 SCS 可以降低混淆"，renaming 证明相反
- §6 Practical implications 建议 "flag type pairs with SCS>0.85 for definition refinement" 但 renaming 说明这可能适得其反

**R2-W3** CrossAgentIE (ACL 2025 Findings) 对比不充分
- Cross-type debate 与 confusability 分析直接相关
- 论文仅在括号中列出，未讨论其 debate 机制是否本质上处理 type confusability

**R2-W4** FewRel train/val split 混合使用的合理性（与你的 W6 重叠）

**R2-W5** 论文定位为 "analytical/empirical study" 是否适合 EMNLP main track

### Minor: M1 orphan bib entry, M2 Abstract 信息密度, M3 Gemini 引用格式, M4 Table 1 caption, M5 SCS name-only vs prompt content 不一致, M6 bib accuracy

### Missing References:
1. Dubey et al. (2018) "Pairwise Confusion for Fine-Grained Visual Classification" (ECCV)
2. Collier et al. (2021) "Exploiting Class Similarity for ML with Confidence Labels"

---

请逐条回应 R2 的每个 Must-Fix、Should-Fix 和 Missing References。对于你的评分（3.5）与 R2（3.0）的差异，请说明你是否调整评分或维持不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-19T04:38:21.131996+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
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

_source line 1203 · 2026-05-19T04:38:21.182791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-19T04:38:24.900161+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-19T04:38:25.001073+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 has been validated across all four models including a proprietary one; Dimension~2 has been verified only on open-weight models and was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded under the linear specification (TOST $p = 0.003$ at $\pm 3$\,pp on FewRel; DocRED inconclusive, Appendix~\ref{sec:appendix_factorial}) but inconclusive on the logit scale ($p = 0.209$). BCS-controlled experiments use a single seed with greedy decoding; the residual SD of 0.88\,pp (Appendix~\ref{app:variance-decomposition}) supports robustness but precise magnitudes may vary.
43	
44	\item \textbf{Task format dependency.} BCS batch-level prediction is demonstrated only under RE's forced-choice classification format. An unconstrained decoding ablation ($n = 25$) confirms
…[truncated 3445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1206 · 2026-05-19T04:38:28.515806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1207 · 2026-05-19T04:38:28.767429+00:00_

100	\resizebox{\columnwidth}{!}{%
101	\begin{tabular}{llrrrrrrr}
102	\toprule
103	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
104	\cmidrule(lr){3-7}
105	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
106	\midrule
107	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
108	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
109	\midrule
110	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
111	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
112	\bottomrule
113	\end{tabular}}
114	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
115	\label{tab:error_taxonomy}
116	\end{table}
117	
118	\section{SDGD Full Protocol and Results}
119	\label{sec:appendix_sdgd}
120	
121	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
122	
123	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194,
…[truncated 16666 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1208 · 2026-05-19T04:38:28.767791+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1209 · 2026-05-19T04:38:28.818379+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-19T04:38:31.680165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-19T04:38:32.084523+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets. We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two largely additive dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution, though typical batches yield modest ${\sim}$2\,pp gaps. BCS explains 22--53\% of cross-batch RE accuracy variance under RE's forced-choice format but shows no batch-level signal for NER, where errors scatter across missed entities and boundary failures. Few-shot demonstrations widen the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Pairwise confusability is a schema-structural property: effects replicate across model scales and families, and persist under varied prompt designs.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-19T04:38:32.085000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1213 · 2026-05-19T04:38:32.487566+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
…[truncated 3157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-19T04:38:32.488167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-19T04:38:32.848085+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED $R^2 = 0.51$) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%); conditional on nonzero confusion, $R^2$ rises to 7\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\% (Monte Carlo simulation; Appendix~\ref{app:aggregation-sim}), consistent with observed RE values.
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific ($R^2 = 0.22$--$0.53$ vs.\ $r \approx 0$ for NER, $n = 450$). RE uses forced-choice classification where all non-null errors are type substitutions \cite{tam-2024-let-me-speak}, making BCS predictive. NER produces multi-span output where errors scatter across missed entities, boundary misalignment, and type confusion, diluting the BCS signal \cite{schall-2025-hidden-cost}. The NER U-shape (\S\ref{sec:count_curves}) likely reflects a dual-task burden: partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers. An unconstrained decoding ablation ($n = 25$) confirms format dependency: removing the JSON enum constraint eliminates the BCS--accuracy correlation ($\rho = -0.14$, $p = 0.49$) while OOV remains near zero (0.08\%), showing that constrained decoding channels all errors into type substitution.
12	
13	\paragraph{Practical implications.}
14	For RE, pre-screening type pairs in th
…[truncated 1551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 359
}
```

</details>

---


### Tool call

_source line 1216 · 2026-05-19T04:38:32.848613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-19T04:38:32.899668+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure*}[t]
10	\centering
11	\begin{minipage}[t]{0.48\textwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\textwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves. Error bars: $\pm 1$\,SD across 3 seeds $\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Hollow markers: full-schema (no sampling variance). \textbf{(b)} BCS-controlled FewRel accuracy. Slopes are consistent across the independent and within-pool 16-relation conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps.}
21	\label{fig:main_results}
22	\end{figure*}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $
…[truncated 9450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-19T04:38:36.717362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1219 · 2026-05-19T04:38:37.822801+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and fine-grained entity typing \cite{gillick-2014-entity-typing}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. \citet{wei-2023-chatie} reformulate zero-shot IE as multi-turn QA with ChatGPT but do not analyze schema-size effects.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definit
…[truncated 3188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool call

_source line 1220 · 2026-05-19T04:38:37.823340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 1221 · 2026-05-19T04:38:38.178322+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapse (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.): graph coloring achieves only marginal mean BCS reduction (0.559$\to$0.552), insufficient to produce detectable accuracy improvement. All practical routing strategies fall below the single-pass baseline (Appendix~\ref{sec:appendix_routing}).
11	
12	Promising avenues include coarse-to-fine pipelines and retrieval-based routing.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-19T04:38:38.178778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---
