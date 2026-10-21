# Reviewer 2 coordination — Part 2 of 6

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-2-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/09/09a3a079e15d5a0cc797.json)

## Round 13

### Tool call

_source line 468 · 2026-05-16T15:12:41.024348+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 1 审稿意见\n\n**论文**: \"Does Type Confusability Shape Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 Main Conference (ACL ARR May 2025 cycle)\n**审查侧重**: 新颖性、Framing、Related Work、完整性\n\n---\n\n## 1. Summary\n\n本文通过受控实验设计，将 training-free LLM IE 中的 schema-induced degradation 分解为两个通道：count-driven recall decline (Channel 1) 和 confusability-driven type substitution (Channel 2)。引入 Schema Confusability Score (SCS) 度量类型间语义重叠，在 NER/RE/ED 四个数据集上验证。主要发现包括：典型批次间 confusability 差异约 2.2pp，pairwise SCS 解释 1.3-1.7% 的混淆方差，以及 NER schema decomposition 因 merge amplification 失败。\n\n---\n\n## 2. Strengths\n\n- **S1**: 实验设计严谨——BCS-controlled experiments 有效隔离了 count 和 confusability 变量，within-pool analysis 控制了 pool composition confound，permutation test 验证了跨池 slope 一致性\n- **S2**: 负面结果的诚实报告——SDGD 在 NER 上的失败及原因分析（merge amplification）对社区有实际指导价值\n- **S3**: 统计方法全面——bootstrap CIs、TOST equivalence testing、cluster bootstrap、Monte Carlo simulation 验证 pair-to-batch aggregation，方法论素养高于平均水平\n- **S4**: MAVEN centrality confound 的识别和解决（§4.5 + Appendix D）展示了对 embedding space 结构问题的深入理解\n- **S5**: Limitations section 覆盖 7 项关键弱点 + multiple comparisons 讨论，自我批评充分\n- **S6**: 跨模型验证（Qwen3-32B + Llama-3.1-8B）和跨 prompt 验证（v1/v2）增强了结论鲁棒性\n\n---\n\n## 3. Weaknesses\n\n### **W1** [critical] 核心 novelty 有限：two-channel decomposition 近似 trivial\n\n\"更多类型导致 recall 下降\"已被 Li et al. (2023) 和 LLM-PEE (2025) 观察到；\"语义相似的类型容易混淆\"是 NLP 分类任务的常识性直觉。本文的贡献在于用 controlled design 量化这一直觉，但 decomposition 本身的概念 novelty 有限。\n\n**证据**: §2 Related Work 已承认 \"SCS shares its formal definition...with the partitioning criterion used in LLM-PEE\"。Contribution #1 称之为 \"controlled evidence for two degradation channels\"——这更像是 empirical confirmation 而非 conceptual advancement。\n\n**为什么影响接收**: EMNLP 要求 excitement/novelty 达到一定阈值。如果核心贡献是 \"用受控实验证实了一个广泛预期的直觉\"，excitement 打分将偏低。\n\n### **W2** [critical] Framing 过度强调 extreme-batch 结果，弱化 typical-batch 现实\n\nAbstract 第一个具体数据点是 \"quartile BCS gap is −5.3pp\"，而 \"typical random batches differ by ≈2.2pp\" 被放在后面。极端批次 31.2pp 出现在 Table ref 引用中。Introduction 的 finding (1) 以 \"up to 31.2pp under extreme-batch construction\" 结尾。\n\n**问题**: 对于实践者来说，真实工作负载中遇到的效应量是 ~2.2pp（约 7% of extreme-batch gap）。这个 magnitude 在许多应用场景中可能不具备实际意义。论文未讨论这 2.2pp 是否超过了 practitioners 的 noise tolerance。\n\n**建议**: Abstract 和 Introduction 应以 typical-batch magnitude 为主锚，将 extreme-batch 作为 \"upper bound under adversarial construction\" 的补充说明。\n\n### **W3** [critical] 非显著结果被不恰当地 frame 为正面贡献\n\nContribution #4: \"RE batch composition yields a directional +1.4pp gain (p≈0.19)\"。Abstract 也提到此结果。Conclusion 重复。\n\n**问题**: p=0.19 远未达到任何常规显著性阈值。将非显著结果列为 contribution 违反了学术写作规范。\"directional\" 这个修饰词不能将 n.s. 结果升格为 contribution。此外，graph coloring 方案在 15 个 random seeds 中仅排第 13——比大多数随机方案更差。\n\n**建议**: 将此结果从 contribution list 中移除，降级为 \"exploratory finding\" 或 \"null result consistent with narrow BCS margin\"。\n\n### **W4** [warning] \"Empirically separable channels\" 的证据不均衡\n\n- FewRel factorial TOST: p=0.003，支持 additive separability ✓\n- Few-NERD factorial: p=0.50，不支持 ✗\n- Few-NERD within-dataset 2×2: p_TOST=0.56，不支持 ✗\n\n三项检验中两项失败。论文在 §4.4 和 Appendix E 中解释为 \"power issue\"，但 Abstract 和 Introduction 仍以 \"empirically separable\" 为核心 framing，无突出 caveat。\n\n**建议**: \"separable\" 的声称应限定为 \"separable in RE (FewRel); evidence insufficient in NER\"。\n\n### **W5** [warning] Cross-model claim 省略 NER Channel 2 失败\n\nAbstract: \"Channel 1 replicates fully on Llama-3.1-8B; Channel 2 replicates on RE but shows floor effects on 8B NER\"——这一表述相对准确。但 Introduction finding (1) 和 Conclusion 中 \"replicate across model families\" 的措辞给读者的印象是两个 channel 都完整复现。\n\n**具体位置**: Conclusion 第一句 \"showed these channels are separable in RE and replicate across model families (Llama-3.1-8B: count r=0.725, confusability Δ=−27pp)\"——Δ=−27pp 是 RE 数据，但 \"replicate across model families\" 暗示全任务复现。\n\n### **W6** [warning] SCS 作为 metric 的增量贡献存疑\n\nSCS = cosine similarity of type name embeddings。§2 明确承认这与 LLM-PEE 的 partitioning criterion 形式相同。Name+definition ablation (Appendix G) 显示无系统性改进。Pairwise R² = 1.3-1.7%。\n\n**问题**: 如果 metric 与先行工作相同，且解释力仅 1.3-1.7%，将其命名为新 \"Score\" 并作为论文贡献之一是否过度包装？\n\n### **W7** [warning] FewRel 数据使用方式引入潜在 confound\n\n§3.1: \"we combine the training and validation splits to obtain the full 80-relation pool\"。FewRel 的 train 和 val splits 覆盖不同的 relation types。合并后 train-origin types 可能存在数据泄漏风险。\n\n论文在 Limitations item 7 讨论了 contamination 并用 train vs val accuracy 差异（-8.8pp, p=0.06）反驳，但这个 p=0.06 是 marginally significant，且方向（train < val）也可能反映 train-origin types 本身更难（更多长尾类型），而非无泄漏。\n\n### **W8** [warning] Abstract 数字密度过高，可读性差\n\nAbstract 包含: −5.3pp, [−7.4, −3.2], 2.2pp, R²=0.22-0.53, r²=1.3-1.7%, r=0.725, Δ=−27pp, slope=−0.71, R²=0.53, +29.8pp, +1.4pp, p≈0.19 等至少 12 个数字/区间。这严重超出了 abstract 的信息承载力，读者难以在首次阅读中形成清晰的 take-away message。\n\n---\n\n## 4. Questions for Authors\n\n**Q1**: Typical-batch 2.2pp 差异是否超过了下游应用的 noise tolerance？是否有 application scenario 分析表明这个 magnitude 具有实际意义？\n\n**Q2**: 既然 SCS 的 pairwise R² 仅 1.3-1.7%，且剩余方差来自 \"entity frequency, prompt position, mention ambiguity, and definition quality\"——为什么不将这些因素纳入 multivariate model？这是否意味着 SCS 的 practical utility 有限？\n\n**Q3**: RE 使用 oracle routing 评估 batch composition，但 oracle routing 需要 gold labels。实际部署中不可能使用 oracle routing，那么 RE 的 decomposition 结果对实践者的指导价值是什么？\n\n**Q4**: Few-NERD factorial p=0.50 的 power analysis——如果有足够 power，authors 预期交互效应的 direction 和 magnitude 是什么？是否做了 post-hoc power calculation？\n\n**Q5**: 为什么 NER 使用 Qwen3-32B hidden states 做 SCS embedding，而 RE/ED 使用 MiniLM？这种不一致是否影响跨任务结论的可比性？\n\n---\n\n## 5. Missing References\n\n**M1** [重要] **\"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\"** (2025, arXiv 2502.08436)——直接研究通过 label space reduction 改善 zero-shot LLM 分类，本质上是本文 Channel 1 (count-driven degradation) 的工程化解决方案。必须引用和区分。\n\n**M2** [重要] **\"Many-Shot In-Context Learning\"** (NeurIPS 2024)——证明 many-shot regime 下更多 context（包括更多 label examples）可以改善分类性能，提供了与 count-degradation 相反方向的证据（training-free 但有 demonstrations vs. 纯 zero-shot）。应讨论为什么 zero-shot setting 下 count-degradation 存在但 many-shot 下不一定。\n\n**M3** [建议] **Label confusion / class similarity 在传统 ML 中的文献**——如 inter-class similarity 对分类器性能的影响在 pre-LLM 时代已有广泛研究。应在 Related Work 中承认 confusability 作为 degradation factor 的发现不仅限于 LLM setting。\n\n**M4** [建议] SGD/SGD-X 的讨论深度不足——仅一句话提及，但 Schema-Guided Dialogue 中 intent/slot confusion 与 schema size 的关系是最直接的 parallel。Appendix H 有更多讨论但正文中过于简略。\n\n---\n\n## 6. Overall Assessment\n\n**Soundness**: 3.5/5 — 实验设计和统计方法论扎实，但部分 claim（separability 在 NER 上未证实、非显著结果作为 contribution）存在 overclaiming\n\n**Excitement**: 2.5/5 — 核心发现（\"类型多了 recall 下降，类型相似了容易混淆\"）概念上不令人惊讶；practical magnitude (2.2pp) 有限；SCS metric 与 LLM-PEE 形式相同；负面结果（SDGD 失败）有价值但不足以独立支撑论文\n\n**Overall**: 2.5/5 — **Borderline reject (leaning weak reject)**\n\n**置信度**: 4/5 — 我仔细阅读了论文的所有 section 和 appendix，对实验设计和统计方法有信心，但对 embedding/IE 领域的最新进展了解可能不完全\n\n**一句话总结**: 方法论严谨但核心发现的 novelty 和 practical impact 不足以支撑 EMNLP main conference 接收——typical-batch 效应量仅 2.2pp，SCS 与 LLM-PEE 形式相同，主要贡献是\"用受控实验确认了预期中的直觉\"。\n\n---\n\n## 7. Detailed Comments by Section\n\n### Abstract\n- 信息过载：12+ 数字/区间在 ~200 词内，建议精简至 3-4 个核心数字\n- \"the first study to formally isolate type confusability from type count\" 可能过强——LLM-PEE 虽然不以分析为目标，但其 embedding-based partitioning 隐式地利用了同样的 count-confusability 分离思想\n\n### §1 Introduction\n- Contribution #4 包含 p≈0.19 的非显著结果，不应列为 contribution\n- \"Two empirically separable channels\" 措辞应加限定词（\"in RE\"）\n- Finding (1) 将 extreme-batch 31.2pp 放在最显眼位置，给读者造成 effect size 大于实际 typical 值的印象\n\n### §2 Related Work\n- \"From Haystack to Needle\" (2025) 未引用——直接相关的 label space reduction 工作\n- Many-shot ICL (NeurIPS 2024) 未引用——在 many-shot regime 下 more labels 可能不 degrade\n- SGD/SGD-X 仅一句，应扩展讨论 intent confusion 与 schema size 的关系\n- ¶4 \"SCS novelty\" 段落坦承 SCS 形式上与 LLM-PEE criterion 相同——这种诚实值得赞赏，但也强化了 novelty 有限的印象\n\n### §3 Experimental Setup\n- FewRel train+val 合并的 rationale 清楚，但 contamination 讨论应更严格\n- 单 seed 评估（seed=42）且 \"variance across seeds is not quantified\"——对于 p≈0.19 级别的 marginal effects，seed sensitivity 是关键的 missing information\n- NER 用 Qwen3 embedding, RE/ED 用 MiniLM 的理由应更明确讨论\n\n### §4 Results\n- §4.3 Practical magnitude 段落写得好——坦诚 2.2pp 是 typical 效应\n- §4.4 Multi-channel: \"Channel 1\" 和 \"Channel 2\" 标签首次出现在 Introduction，这是好的\n- §4.5 Centrality confound 分析深入且有说服力\n\n### §5 SDGD\n- 负面结果的分析清晰有力\n- 但 \"merge amplification\" 在 span-level NER 中是一个相对 obvious 的 failure mode——任何 multi-pass extraction + union merge 都会面临此问题。Confidence gating 是最简单的 mitigation 但论文承认不解决问题——是否尝试了 NMS (non-maximum suppression)、span-level voting 等替代方案？\n\n### §6 Discussion\n- \"Why does embedding similarity predict LLM confusion?\" 段落提出了一个合理的假说但缺乏 mechanistic evidence（acknowledged in Limitations item 6）\n- Schema design implications 提出 3 个 mitigation strategies 但均为建议性的，无实验验证\n\n### Conclusion\n- 过于简短（~100 words），且再次将 \"+1.4pp (p≈0.19)\" 作为 positive finding 提及\n",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 1 审稿意见\n\n**论文**: \"Does Type Confusability Shape Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 Main Conference (ACL ARR May 2025 cycle)\n**审查侧重**: 新颖性、Framing、Related Work、完整性\n\n---\n\n## 1. Summary\n\n本文通过受控实验设计，将 training-free LLM IE 中的 schema-induced degradation 分解为两个通道：count-driven recall decline (Channel 1) 和 confusability-driven type substitution (Channel 2)。引入 Schema Confusability Score (SCS) 度量类型间语义重叠，在 NER/RE/ED 四个数据集上验证。主要发现包括：典型批次间 confusability 差异约 2.2pp，pairwise SCS 解释 1.3-1.7% 的混淆方差，以及 NER schema decomposition 因 merge amplification 失败。\n\n---\n\n## 2. Strengths\n\n- **S1**: 实验设计严谨——BCS-controlled experiments 有效隔离了 count 和 confusability 变量，within-pool analysis 控制了 pool composition confound，permutation test 验证了跨池 slope 一致性\n- **S2**: 负面结果的诚实报告——SDGD 在 NER 上的失败及原因分析（merge amplification）对社区有实际指导价值\n- **S3**: 统计方法全面——bootstrap CIs、TOST equivalence testing、cluster bootstrap、Monte Carlo simulation 验证 pair-to-batch aggregation，方法论素养高于平均水平\n- **S4**: MAVEN centrality confound 的识别和解决（§4.5 + Appendix D）展示了对 embedding space 结构问题的深入理解\n- **S5**: Limitations section 覆盖 7 项关键弱点 + multiple comparisons 讨论，自我批评充分\n- **S6**: 跨模型验证（Qwen3-32B + Llama-3.1-8B）和跨 prompt 验证（v1/v2）增强了结论鲁棒性\n\n---\n\n## 3. Weaknesses\n\n### **W1** [critical] 核心 novelty 有限：two-channel decomposition 近似 trivial\n\n\"更多类型导致 recall 下降\"已被 Li et al. (2023) 和 LLM-PEE (2025) 观察到；\"语义相似的类型容易混淆\"是 NLP 分类任务的常识性直觉。本文的贡献在于用 controlled design 量化这一直觉，但 decomposition 本身的概念 novelty 有限。\n\n**证据**: §2 Related Work 已承认 \"SCS shares its formal definition...with the partitioning criterion used in LLM-PEE\"。Contribution #1 称之为 \"controlled evidence for two degradation channels\"——这更像是 empirical confirmation 而非 conceptual advancement。\n\n**为什么影响接收**: EMNLP 要求 excitement/novelty 达到一定阈值。如果核心贡献是 \"用受控实验证实了一个广泛预期的直觉\"，excitement 打分将偏低。\n\n### **W2** [critical] Framing 过度强调 extreme-batch 结果，弱化 typical-batch 现实\n\nAbstract 第一个具体数据点是 \"quartile BCS gap is −5.3pp\"，而 \"typical random batches differ by ≈2.2pp\" 被放在后面。极端批次 31.2pp 出现在 Table ref 引用中。Introduction 的 finding (1) 以 \"up to 31.2pp under extreme-batch construction\" 结尾。\n\n**问题**: 对于实践者来说，真实工作负载中遇到的效应量是 ~2.2pp（约 7% of extreme-batch gap）。这个 magnitude 在许多应用场景中可能不具备实际意义。论文未讨论这 2.2pp 是否超过了 practitioners 的 noise tolerance。\n\n**建议**: Abstract 和 Introduction 应以 typical-batch magnitude 为主锚，将 extreme-batch 作为 \"upper bound under adversarial construction\" 的补充说明。\n\n### **W3** [critical] 非显著结果被不恰当地 frame 为正面贡献\n\nContribution #4: \"RE batch composition yields a directional +1.4pp gain (p≈0.19)\"。Abstract 也提到此结果。Conclusion 重复。\n\n**问题**: p=0.19 远未达到任何常规显著性阈值。将非显著结果列为 contribution 违反了学术写作规范。\"directional\" 这个修饰词不能将 n.s. 结果升格为 contribution。此外，graph coloring 方案在 15 个 random seeds 中仅排第 13——比大多数随机方案更差。\n\n**建议**: 将此结果从 contribution list 中移除，降级为 \"exploratory finding\" 或 \"null result consistent with narrow BCS margin\"。\n\n### **W4** [warning] \"Empirically separable channels\" 的证据不均衡\n\n- FewRel factorial TOST: p=0.003，支持 additive separability ✓\n- Few-NERD factorial: p=0.50，不支持 ✗\n- Few-NERD within-dataset 2×2: p_TOST=0.56，不支持 ✗\n\n三项检验中两项失败。论文在 §4.4 和 Appendix E 中解释为 \"power issue\"，但 Abstract 和 Introduction 仍以 \"empirically separable\" 为核心 framing，无突出 caveat。\n\n**建议**: \"separable\" 的声称应限定为 \"separable in RE (FewRel); evidence insufficient in NER\"。\n\n### **W5** [warning] Cross-model claim 省略 NER Channel 2 失败\n\nAbstract: \"Channel 1 replicates fully on Llama-3.1-8B; Channel 2 replicates on RE but shows floor effects on 8B NER\"——这一表述相对准确。但 Introduction finding (1) 和 Conclusion 中 \"replicate across model families\" 的措辞给读者的印象是两个 channel 都完整复现。\n\n**具体位置**: Conclusion 第一句 \"showed these channels are separable in RE and replicate across model families (Llama-3.1-8B: count r=0.725, confusability Δ=−27pp)\"——Δ=−27pp 是 RE 数据，但 \"replicate across model families\" 暗示全任务复现。\n\n### **W6** [warning] SCS 作为 metric 的增量贡献存疑\n\nSCS = cosine similarity of type name embeddings。§2 明确承认这与 LLM-PEE 的 partitioning criterion 形式相同。Name+definition ablation (Appendix G) 显示无系统性改进。Pairwise R² = 1.3-1.7%。\n\n**问题**: 如果 metric 与先行工作相同，且解释力仅 1.3-1.7%，将其命名为新 \"Score\" 并作为论文贡献之一是否过度包装？\n\n### **W7** [warning] FewRel 数据使用方式引入潜在 confound\n\n§3.1: \"we combine the training and validation splits to obtain the full 80-relation pool\"。FewRel 的 train 和 val splits 覆盖不同的 relation types。合并后 train-origin types 可能存在数据泄漏风险。\n\n论文在 Limitations item 7 讨论了 contamination 并用 train vs val accuracy 差异（-8.8pp, p=0.06）反驳，但这个 p=0.06 是 marginally significant，且方向（train < val）也可能反映 train-origin types 本身更难（更多长尾类型），而非无泄漏。\n\n### **W8** [warning] Abstract 数字密度过高，可读性差\n\nAbstract 包含: −5.3pp, [−7.4, −3.2], 2.2pp, R²=0.22-0.53, r²=1.3-1.7%, r=0.725, Δ=−27pp, slope=−0.71, R²=0.53, +29.8pp, +1.4pp, p≈0.19 等至少 12 个数字/区间。这严重超出了 abstract 的信息承载力，读者难以在首次阅读中形成清晰的 take-away message。\n\n---\n\n## 4. Questions for Authors\n\n**Q1**: Typical-batch 2.2pp 差异是否超过了下游应用的 noise tolerance？是否有 application scenario 分析表明这个 magnitude 具有实际意义？\n\n**Q2**: 既然 SCS 的 pairwise R² 仅 1.3-1.7%，且剩余方差来自 \"entity frequency, prompt position, mention ambiguity, and definition quality\"——为什么不将这些因素纳入 multivariate model？这是否意味着 SCS 的 practical utility 有限？\n\n**Q3**: RE 使用 oracle routing 评估 batch composition，但 oracle routing 需要 gold labels。实际部署中不可能使用 oracle routing，那么 RE 的 decomposition 结果对实践者的指导价值是什么？\n\n**Q4**: Few-NERD factorial p=0.50 的 power analysis——如果有足够 power，authors 预期交互效应的 direction 和 magnitude 是什么？是否做了 post-hoc power calculation？\n\n**Q5**: 为什么 NER 使用 Qwen3-32B hidden states 做 SCS embedding，而 RE/ED 使用 MiniLM？这种不一致是否影响跨任务结论的可比性？\n\n---\n\n## 5. Missing References\n\n**M1** [重要] **\"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\"** (2025, arXiv 2502.08436)——直接研究通过 label space reduction 改善 zero-shot LLM 分类，本质上是本文 Channel 1 (count-driven degradation) 的工程化解决方案。必须引用和区分。\n\n**M2** [重要] **\"Many-Shot In-Context Learning\"** (NeurIPS 2024)——证明 many-shot regime 下更多 context（包括更多 label examples）可以改善分类性能，提供了与 count-degradation 相反方向的证据（training-free 但有 demonstrations vs. 纯 zero-shot）。应讨论为什么 zero-shot setting 下 count-degradation 存在但 many-shot 下不一定。\n\n**M3** [建议] **Label confusion / class similarity 在传统 ML 中的文献**——如 inter-class similarity 对分类器性能的影响在 pre-LLM 时代已有广泛研究。应在 Related Work 中承认 confusability 作为 degradation factor 的发现不仅限于 LLM setting。\n\n**M4** [建议] SGD/SGD-X 的讨论深度不足——仅一句话提及，但 Schema-Guided Dialogue 中 intent/slot confusion 与 schema size 的关系是最直接的 parallel。Appendix H 有更多讨论但正文中过于简略。\n\n---\n\n## 6. Overall Assessment\n\n**Soundness**: 3.5/5 — 实验设计和统计方法论扎实，但部分 claim（separability 在 NER 上未证实、非显著结果作为 contribution）存在 overclaiming\n\n**Excitement**: 2.5/5 — 核心发现（\"类型多了 recall 下降，类型相似了容易混淆\"）概念上不令人惊讶；practical magnitude (2.2pp) 有限；SCS metric 与 LLM-PEE 形式相同；负面结果（SDGD 失败）有价值但不足以独立支撑论文\n\n**Overall**: 2.5/5 — **Borderline reject (leaning weak reject)**\n\n**置信度**: 4/5 — 我仔细阅读了论文的所有 section 和 appendix，对实验设计和统计方法有信心，但对 embedding/IE 领域的最新进展了解可能不完全\n\n**一句话总结**: 方法论严谨但核心发现的 novelty 和 practical impact 不足以支撑 EMNLP main conference 接收——typical-batch 效应量仅 2.2pp，SCS 与 LLM-PEE 形式相同，主要贡献是\"用受控实验确认了预期中的直觉\"。\n\n---\n\n## 7. Detailed Comments by Section\n\n### Abstract\n- 信息过载：12+ 数字/区间在 ~200 词内，建议精简至 3-4 个核心数字\n- \"the first study to formally isolate type confusability from type count\" 可能过强——LLM-PEE 虽然不以分析为目标，但其 embedding-based partitioning 隐式地利用了同样的 count-confusability 分离思想\n\n### §1 Introduction\n- Contribution #4 包含 p≈0.19 的非显著结果，不应列为 contribution\n- \"Two empirically separable channels\" 措辞应加限定词（\"in RE\"）\n- Finding (1) 将 extreme-batch 31.2pp 放在最显眼位置，给读者造成 effect size 大于实际 typical 值的印象\n\n### §2 Related Work\n- \"From Haystack to Needle\" (2025) 未引用——直接相关的 label space reduction 工作\n- Many-shot ICL (NeurIPS 2024) 未引用——在 many-shot regime 下 more labels 可能不 degrade\n- SGD/SGD-X 仅一句，应扩展讨论 intent confusion 与 schema size 的关系\n- ¶4 \"SCS novelty\" 段落坦承 SCS 形式上与 LLM-PEE criterion 相同——这种诚实值得赞赏，但也强化了 novelty 有限的印象\n\n### §3 Experimental Setup\n- FewRel train+val 合并的 rationale 清楚，但 contamination 讨论应更严格\n- 单 seed 评估（seed=42）且 \"variance across seeds is not quantified\"——对于 p≈0.19 级别的 marginal effects，seed sensitivity 是关键的 missing information\n- NER 用 Qwen3 embedding, RE/ED 用 MiniLM 的理由应更明确讨论\n\n### §4 Results\n- §4.3 Practical magnitude 段落写得好——坦诚 2.2pp 是 typical 效应\n- §4.4 Multi-channel: \"Channel 1\" 和 \"Channel 2\" 标签首次出现在 Introduction，这是好的\n- §4.5 Centrality confound 分析深入且有说服力\n\n### §5 SDGD\n- 负面结果的分析清晰有力\n- 但 \"merge amplification\" 在 span-level NER 中是一个相对 obvious 的 failure mode——任何 multi-pass extraction + union merge 都会面临此问题。Confidence gating 是最简单的 mitigation 但论文承认不解决问题——是否尝试了 NMS (non-maximum suppression)、span-level voting 等替代方案？\n\n### §6 Discussion\n- \"Why does embedding similarity predict LLM confusion?\" 段落提出了一个合理的假说但缺乏 mechanistic evidence（acknowledged in Limitations item 6）\n- Schema design implications 提出 3 个 mitigation strategies 但均为建议性的，无实验验证\n\n### Conclusion\n- 过于简短（~100 words），且再次将 \"+1.4pp (p≈0.19)\" 作为 positive finding 提及\n",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-16T15:12:45.295899+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4271
}
```

</details>

---


### Assistant

_source line 470 · 2026-05-16T15:12:51.717549+00:00_

审稿意见已提交给 Review Director。

核心判断：**Borderline reject (2.5/5)**。方法论严谨（统计设计优秀），但三个 critical 问题制约接收：
1. 核心 novelty 有限——"count↓recall, similarity↑confusion" 的分解概念上近似 trivial
2. Framing 偏差——extreme-batch 31.2pp 被过度突出，而 typical 效应仅 2.2pp
3. 非显著结果 (+1.4pp, p≈0.19) 被列为论文贡献

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 14

## Round 14

4 recorded events


### User

_source line 471 · 2026-05-16T15:15:54.577661+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每条 Weakness 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也请对 Strengths、Questions、Missing References 中你有不同看法的部分发表意见。

---

# Reviewer 1 — Round 1 审稿意见

**审查侧重**: 方法严谨性、实验设计、统计有效性

## 2. Strengths

**S1.** BCS-controlled 实验框架，within-pool 分析排除 pool composition 混淆，permutation test 验证跨 pool 斜率一致性（p=0.60）。
**S2.** 统计透明度高——主动报告 r²=1.3-1.7% 的微小效应，practical magnitude 区分极端 vs 典型 batch。
**S3.** 诚实的负面结果——SDGD 失败 + merge amplification 深入诊断。
**S4.** 多数据集、跨模型验证——MAVEN 异常的 centrality confound 处理方法学成熟。
**S5.** Pair-to-batch amplification Monte Carlo 模拟给出定量解释。

## 3. Weaknesses

**W1 [critical]** "两通道可分离"的统计证据不对称且不充分。
FewRel TOST p=0.003 支持，但 Few-NERD p=0.50 完全无法区分"无交互"和"检验力不足"。§5.4 自己说 NER 中 "coupled"，与"两通道可分离"的总体 claim 矛盾。如果可分离性仅在 RE（closed-set）上成立，generality 有限。
建议：(a) "empirically separable" 限定为 RE-specific；(b) NER 改为 "two channels identified, separability not confirmed"；(c) NER power analysis。

**W2 [critical]** Count curve 每个 level 仅 5 个 random batch，方差估计不可靠。
5 个 batch 的 mean 和 SE 估计不稳定。Figure 1a 是否有 error bar？count curve 是 Channel 1 核心证据，如果估计不稳定，Channel 1 的 claim 基础动摇。
建议：报告 batch 间 SD 或 CI；解释为什么 5 个 batch 足够。

**W3 [warning]** Pairwise r²=1.3-1.7% 的实际意义问题。
更关键的是 conditioning on non-zero confusion pairs 将 r² 提升到 7%，但后续讨论多次使用 7% 作为"真实效应大小"做 aggregation simulation，引入选择偏差。
建议：讨论 alternative confusability metrics。

**W4 [warning]** 不同数据集使用不同 embedding。
Few-NERD 用 Qwen3，FewRel/DocRED/MAVEN 用 MiniLM。跨数据集 r 值不可直接比较。Few-NERD 用模型自身 embedding 有循环论证风险。

**W5 [warning]** FewRel data contamination 未充分排除。
defense (−8.8pp, p=0.06) borderline non-significant。contamination 可能不 uniform。

**W6 [warning]** 31.2pp extreme-batch framing 误导风险。
Abstract/Intro 给读者第一印象是 31.2pp 的实际影响，但 typical 仅 2.2pp。

**W7 [info]** 单种子评估可靠性。
greedy decoding + seed=42，variance across seeds not quantified。

**W8 [info]** Bootstrap 参数不一致（B=10,000 vs B=1,000）。

## 4. Questions

Q1: Figure 1a error bar？batch 间方差多大？
Q2: Few-NERD 为什么选 Qwen3 而非 MiniLM？
Q3: Aggregation simulation ρ=0.35 从哪个数据集估得？对结果敏感吗？
Q4: Extreme batch 中具体 relation types？是否有 domain confound？
Q5: Per-type recall=0.586 > single-pass 0.368 → count curve recall 下降可能是 prompt length driven 而非 count-driven？
Q6: TOST margin ±3pp 依据？

## 5. Missing References
- Banerjee et al. (2025) "Benchmarking LLM-based Schema Extraction"
- Cohen (1988) / Lakens (2013) 关于 small effect size 实际意义
- Multiple testing correction 方法论（Perneger 1998, Rothman 1990）

## 6. Overall Assessment
**Findings acceptance (3/5)**，置信度 4/5
**核心问题**: 实验设计严谨但核心效应小（2.2pp typical），"两通道可分离" claim 在 NER 上缺乏统计支撑。建议 Findings paper 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-16T15:17:37.429773+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## 对 Strengths 的补充意见\n\nR1 的 S1-S5 评价准确，我完全同意。补充一点：S2（统计透明度）是本文最突出的优点之一——主动报告 r²=1.3-1.7% 并区分 extreme vs typical batch，在 NLP 论文中罕见。这种诚实同时也构成了论文的 weakness（效应量确实小），但不应因此低估 authors 的学术诚信。\n\n---\n\n## 对 Weaknesses 的逐条回应\n\n### R1-W1: \"两通道可分离\"的统计证据不对称\n\n[AGREE] R1-W1: 我在自己的审稿中将此列为 W4 [warning]。证据确实不均衡：\n- FewRel TOST p=0.003 ✓\n- Few-NERD factorial p=0.50 ✗\n- Few-NERD 2×2 TOST p=0.56 ✗\n\n§4.4 自己承认 NER 中 channels \"coupled\"，但 Abstract 和 Introduction 仍使用 \"empirically separable\" 作为全局 framing。R1 的建议（限定为 RE-specific + NER power analysis）完全合理。\n\n**补充**: 我认为更深层的问题是——NER 中 boundary ambiguity 和 type ambiguity 本质上不可分离（一个 span 被错误识别可能同时是 \"missed\" 和 \"substituted\"），所以 \"two separable channels\" 作为通用 claim 在 span-level tasks 上可能概念上就不成立，不仅是统计 power 问题。\n\n---\n\n### R1-W2: Count curve 每个 level 仅 5 个 random batch\n\n[REBUT] R1-W2: 这个担忧合理但 severity 可降为 warning 而非 critical，理由如下：\n\n1. **Count curve 的核心 claim 是 monotonic decline，不是精确估计每个点的均值。** 跨 4 个数据集（Few-NERD 7 levels、FewRel 7 levels、DocRED 7 levels、MAVEN 6 levels）的 monotonic pattern 构成强复现证据，单个点的 CI 宽度不影响 direction claim。\n\n2. **Cross-model replication (Table 4)**: Llama-3.1-8B 与 Qwen3-32B per-batch correlation r=0.725——如果 5 batches 的估计极不稳定，两个模型不可能产生这种 rank-order 一致性。\n\n3. **Solo baseline (count=1) 不依赖 batch sampling**: 每个 type 单独评估作为 ceiling，这是确定性的。从 ceiling 到 full-schema 的 decline 是 robust 的。\n\n4. **BCS-controlled experiments (§4.3) 使用 25-100 batches**——这些是 Channel 1 claim 的更强证据（within-pool n=100 random subsets）。\n\n**然而**: R1 关于 \"Figure 1a 是否有 error bar\" 的追问合理。如果 Figure 1a 没有 error bars/bands，这是一个 presentation gap。Authors 应补充 batch-level variance visualization。\n\n---\n\n### R1-W3: Pairwise r²=1.3-1.7% + conditioning bias\n\n[AGREE] R1-W3: conditioning on non-zero confusion pairs 将 r² 从 1.3-1.7% 提升到 7% 确实引入了选择偏差——只看 \"已经发生混淆\" 的 pairs 来估计 confusability 的解释力，排除了大量 SCS 高但未混淆的 pairs（可能因为 frequency 太低或 prompt 位置不利）。\n\n**然而**: Monte Carlo simulation (Appendix F) 用 7% 作为输入、输出 batch R²=0.219 匹配观测值 0.218——这个 external validation 说明 7% 在 aggregation model 中是 \"有效参数\"，即使它来自 conditioned sample。论文应更明确讨论这一点：7% 是 conditional effect size，not unconditional。\n\n**补充**: R1 建议讨论 alternative confusability metrics——我同意。论文 Limitations item 4 提到 \"label entropy or ontological depth may capture complementary dimensions\" 但未深入。考虑到 r²=1.3-1.7% 的 unconditional effect，是否存在更好的 pre-hoc proxy 是一个自然的 follow-up question。\n\n---\n\n### R1-W4: 不同数据集使用不同 embedding\n\n[AGREE] R1-W4: 我在自己的审稿中也提出了这个问题（Q5）。\n\n核心问题有二：\n1. **跨数据集 r 值不可比**: Few-NERD r=0.112 (Qwen3) vs MAVEN r=0.129 (MiniLM)——embedding space 不同，这两个 r 的比较无意义。\n2. **Few-NERD 循环论证**: 用 Qwen3（即 extraction model 本身）的 hidden states 做 SCS，然后测量 Qwen3 extraction 中的 confusion——predictor 和 outcome 来自同一模型的不同 passes，存在 shared representation bias。\n\n**但需注意**: §3.2 报告了 Qwen3 vs MiniLM cross-embedding sensitivity check，方向一致但 BCS range 更窄。论文选择 MiniLM 作为 RE/ED primary embedding 的理由（\"sentence-transformers are specifically trained for semantic similarity\"）是合理的。问题更多在于 Few-NERD 为什么不也用 MiniLM。\n\n---\n\n### R1-W5: FewRel data contamination\n\n[AGREE] R1-W5: 与我的 W7 一致。补充一点：\n\n论文的 contamination defense 有两个 argument：\n1. train-origin types accuracy lower (−8.8pp, p=0.06) — borderline n.s.\n2. monotonic count-dependent curve \"cannot be explained by uniform contamination\"\n\nArgument 2 更有说服力——如果模型记住了 FewRel 数据，performance 应在所有 conditions 提升，不会产生 monotonic decline。但 contamination 不一定 uniform（某些 relation 被记住更多），所以这也不是完全的 refutation。\n\n**Severity**: 我同意这是 warning 而非 critical——即使存在部分 contamination，degradation 的方向和 pattern 仍然成立。\n\n---\n\n### R1-W6: 31.2pp extreme-batch framing 误导\n\n[AGREE] R1-W6: 与我的 W2 [critical] 完全一致。\n\n补充数据：§4.3 Practical magnitude 报告 typical IQR=0.054 对应 2.2pp gap (CI: [0.4, 4.0])。CI 下界仅 0.4pp——在某些 random samples 中效应接近 zero。相比之下，31.2pp 来自人为构造的 extreme batches (maximally dissimilar vs maximally similar types from 80-relation pool)。\n\n这不仅是 framing 问题——如果 typical scenario 下效应为 0.4-4.0pp，那么 confusability 对实践者的指导价值（schema design implications）也相应受限。Discussion §6 的 3 个 mitigation strategies 在 typical 场景下可能 not worth the engineering effort。\n\n---\n\n### R1-W7: 单种子评估\n\n[REBUT] R1-W7: Severity 应为 negligible 而非 info，理由：\n\n论文使用 **greedy decoding (temperature=0)**——在 deterministic decoding 下，seed 仅影响 vLLM 的 CUDA kernel 数值误差传播（通常 <0.1% 差异）。这不是 sampling-based generation，所以 seed sensitivity 在原则上不是问题。\n\n唯一潜在 concern 是 vLLM 的 parallel execution 可能引入 non-determinism（GPU scheduling），但这对结论不构成威胁。\n\n---\n\n### R1-W8: Bootstrap 参数不一致\n\n[REBUT] R1-W8: §3.4 明确说明 \"pair-level CIs use standard percentile bootstrap (B=10,000); batch-level CIs use B=1,000 due to computational cost\"。\n\nB=1,000 对 batch-level percentile bootstrap 通常足够（standard practice），CI 精度在 ±0.5% 之内。这不是 methodological concern。\n\n---\n\n## 对 Questions 的补充意见\n\n**R1-Q5 是一个出色的问题**：per-type recall=0.586 > single-pass 0.368。如果 count-degradation 的真正 driver 是 prompt length（更多 type definitions = 更长 prompt = lost-in-the-middle 效应）而非 type count per se，那么 \"Channel 1 = count-driven\" 的 framing 需要修正为 \"Channel 1 = prompt-length-driven\"。\n\n论文引用了 lost-in-middle (Liu et al., 2024) 但未直接测试 prompt length vs count 的 confound——例如通过在 fixed count 下 padding prompt length 来分离两个因素。这是一个潜在的 confound that weakens Channel 1 的 mechanistic interpretation。\n\n**R1-Q6 关于 TOST margin ±3pp**：Appendix E 选 ±3pp 但未给出 justification。在 typical batch difference 仅 2.2pp 的 context 下，±3pp margin 相当宽松——如果 margin 设为 ±1pp，TOST 可能不通过。这是一个 analyst degrees of freedom 问题。\n\n---\n\n## 对 Missing References 的回应\n\n**Banerjee et al. (2025)**: 我未独立搜索到此文。如果确实存在且直接 benchmark LLM-based schema extraction，则应引用。但 R1 未提供完整引用信息，需要验证。\n\n**Cohen (1988) / Lakens (2013)**: [AGREE] 非常相关。论文反复讨论 \"modest effect size\" 和 \"practical magnitude\" 但未引用 small-effect-size 方法论文献。引用这些经典文献可以为 \"r²=1.3-1.7% is still meaningful\" 的论点提供框架支撑。\n\n**Multiple testing correction**: [REBUT] 论文 Limitations section 最后一段明确讨论了 multiple comparisons 策略（\"We do not apply family-wise correction across datasets, treating each as an independent replication\"），并引用了 independent replication 逻辑。Perneger (1998) 和 Rothman (1990) 实际上支持论文的 no-correction 策略（Rothman 著名地反对 Bonferroni），所以引用它们反而会强化论文立场。\n\n---\n\n## 对 Overall Assessment 的意见\n\nR1 给出 **Findings 3/5**。我的评分是 **Borderline reject 2.5/5**。\n\n差异来源：\n- R1 更看重方法论严谨性（确实优秀）；我更看重 novelty 和 practical impact\n- 我认为 \"SCS 与 LLM-PEE 形式相同\" + \"typical effect 2.2pp\" + \"NER decomposition 完全失败\" 三者叠加，使论文的 contribution 不足以支撑 main conference\n- R1 的 Findings track 建议合理——如果 novelty bar 降低，方法论质量足够\n\n**我的修正评分**: 如果 authors 能 (1) 将 \"separable\" 限定为 RE-specific，(2) 移除 p=0.19 结果的 contribution 定位，(3) 以 typical-batch 2.2pp 为主锚重写 framing——我愿意上调至 **weak accept for Findings** (3/5)。当前 framing 下维持 2.5/5。\n",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## 对 Strengths 的补充意见\n\nR1 的 S1-S5 评价准确，我完全同意。补充一点：S2（统计透明度）是本文最突出的优点之一——主动报告 r²=1.3-1.7% 并区分 extreme vs typical batch，在 NLP 论文中罕见。这种诚实同时也构成了论文的 weakness（效应量确实小），但不应因此低估 authors 的学术诚信。\n\n---\n\n## 对 Weaknesses 的逐条回应\n\n### R1-W1: \"两通道可分离\"的统计证据不对称\n\n[AGREE] R1-W1: 我在自己的审稿中将此列为 W4 [warning]。证据确实不均衡：\n- FewRel TOST p=0.003 ✓\n- Few-NERD factorial p=0.50 ✗\n- Few-NERD 2×2 TOST p=0.56 ✗\n\n§4.4 自己承认 NER 中 channels \"coupled\"，但 Abstract 和 Introduction 仍使用 \"empirically separable\" 作为全局 framing。R1 的建议（限定为 RE-specific + NER power analysis）完全合理。\n\n**补充**: 我认为更深层的问题是——NER 中 boundary ambiguity 和 type ambiguity 本质上不可分离（一个 span 被错误识别可能同时是 \"missed\" 和 \"substituted\"），所以 \"two separable channels\" 作为通用 claim 在 span-level tasks 上可能概念上就不成立，不仅是统计 power 问题。\n\n---\n\n### R1-W2: Count curve 每个 level 仅 5 个 random batch\n\n[REBUT] R1-W2: 这个担忧合理但 severity 可降为 warning 而非 critical，理由如下：\n\n1. **Count curve 的核心 claim 是 monotonic decline，不是精确估计每个点的均值。** 跨 4 个数据集（Few-NERD 7 levels、FewRel 7 levels、DocRED 7 levels、MAVEN 6 levels）的 monotonic pattern 构成强复现证据，单个点的 CI 宽度不影响 direction claim。\n\n2. **Cross-model replication (Table 4)**: Llama-3.1-8B 与 Qwen3-32B per-batch correlation r=0.725——如果 5 batches 的估计极不稳定，两个模型不可能产生这种 rank-order 一致性。\n\n3. **Solo baseline (count=1) 不依赖 batch sampling**: 每个 type 单独评估作为 ceiling，这是确定性的。从 ceiling 到 full-schema 的 decline 是 robust 的。\n\n4. **BCS-controlled experiments (§4.3) 使用 25-100 batches**——这些是 Channel 1 claim 的更强证据（within-pool n=100 random subsets）。\n\n**然而**: R1 关于 \"Figure 1a 是否有 error bar\" 的追问合理。如果 Figure 1a 没有 error bars/bands，这是一个 presentation gap。Authors 应补充 batch-level variance visualization。\n\n---\n\n### R1-W3: Pairwise r²=1.3-1.7% + conditioning bias\n\n[AGREE] R1-W3: conditioning on non-zero confusion pairs 将 r² 从 1.3-1.7% 提升到 7% 确实引入了选择偏差——只看 \"已经发生混淆\" 的 pairs 来估计 confusability 的解释力，排除了大量 SCS 高但未混淆的 pairs（可能因为 frequency 太低或 prompt 位置不利）。\n\n**然而**: Monte Carlo simulation (Appendix F) 用 7% 作为输入、输出 batch R²=0.219 匹配观测值 0.218——这个 external validation 说明 7% 在 aggregation model 中是 \"有效参数\"，即使它来自 conditioned sample。论文应更明确讨论这一点：7% 是 conditional effect size，not unconditional。\n\n**补充**: R1 建议讨论 alternative confusability metrics——我同意。论文 Limitations item 4 提到 \"label entropy or ontological depth may capture complementary dimensions\" 但未深入。考虑到 r²=1.3-1.7% 的 unconditional effect，是否存在更好的 pre-hoc proxy 是一个自然的 follow-up question。\n\n---\n\n### R1-W4: 不同数据集使用不同 embedding\n\n[AGREE] R1-W4: 我在自己的审稿中也提出了这个问题（Q5）。\n\n核心问题有二：\n1. **跨数据集 r 值不可比**: Few-NERD r=0.112 (Qwen3) vs MAVEN r=0.129 (MiniLM)——embedding space 不同，这两个 r 的比较无意义。\n2. **Few-NERD 循环论证**: 用 Qwen3（即 extraction model 本身）的 hidden states 做 SCS，然后测量 Qwen3 extraction 中的 confusion——predictor 和 outcome 来自同一模型的不同 passes，存在 shared representation bias。\n\n**但需注意**: §3.2 报告了 Qwen3 vs MiniLM cross-embedding sensitivity check，方向一致但 BCS range 更窄。论文选择 MiniLM 作为 RE/ED primary embedding 的理由（\"sentence-transformers are specifically trained for semantic similarity\"）是合理的。问题更多在于 Few-NERD 为什么不也用 MiniLM。\n\n---\n\n### R1-W5: FewRel data contamination\n\n[AGREE] R1-W5: 与我的 W7 一致。补充一点：\n\n论文的 contamination defense 有两个 argument：\n1. train-origin types accuracy lower (−8.8pp, p=0.06) — borderline n.s.\n2. monotonic count-dependent curve \"cannot be explained by uniform contamination\"\n\nArgument 2 更有说服力——如果模型记住了 FewRel 数据，performance 应在所有 conditions 提升，不会产生 monotonic decline。但 contamination 不一定 uniform（某些 relation 被记住更多），所以这也不是完全的 refutation。\n\n**Severity**: 我同意这是 warning 而非 critical——即使存在部分 contamination，degradation 的方向和 pattern 仍然成立。\n\n---\n\n### R1-W6: 31.2pp extreme-batch framing 误导\n\n[AGREE] R1-W6: 与我的 W2 [critical] 完全一致。\n\n补充数据：§4.3 Practical magnitude 报告 typical IQR=0.054 对应 2.2pp gap (CI: [0.4, 4.0])。CI 下界仅 0.4pp——在某些 random samples 中效应接近 zero。相比之下，31.2pp 来自人为构造的 extreme batches (maximally dissimilar vs maximally similar types from 80-relation pool)。\n\n这不仅是 framing 问题——如果 typical scenario 下效应为 0.4-4.0pp，那么 confusability 对实践者的指导价值（schema design implications）也相应受限。Discussion §6 的 3 个 mitigation strategies 在 typical 场景下可能 not worth the engineering effort。\n\n---\n\n### R1-W7: 单种子评估\n\n[REBUT] R1-W7: Severity 应为 negligible 而非 info，理由：\n\n论文使用 **greedy decoding (temperature=0)**——在 deterministic decoding 下，seed 仅影响 vLLM 的 CUDA kernel 数值误差传播（通常 <0.1% 差异）。这不是 sampling-based generation，所以 seed sensitivity 在原则上不是问题。\n\n唯一潜在 concern 是 vLLM 的 parallel execution 可能引入 non-determinism（GPU scheduling），但这对结论不构成威胁。\n\n---\n\n### R1-W8: Bootstrap 参数不一致\n\n[REBUT] R1-W8: §3.4 明确说明 \"pair-level CIs use standard percentile bootstrap (B=10,000); batch-level CIs use B=1,000 due to computational cost\"。\n\nB=1,000 对 batch-level percentile bootstrap 通常足够（standard practice），CI 精度在 ±0.5% 之内。这不是 methodological concern。\n\n---\n\n## 对 Questions 的补充意见\n\n**R1-Q5 是一个出色的问题**：per-type recall=0.586 > single-pass 0.368。如果 count-degradation 的真正 driver 是 prompt length（更多 type definitions = 更长 prompt = lost-in-the-middle 效应）而非 type count per se，那么 \"Channel 1 = count-driven\" 的 framing 需要修正为 \"Channel 1 = prompt-length-driven\"。\n\n论文引用了 lost-in-middle (Liu et al., 2024) 但未直接测试 prompt length vs count 的 confound——例如通过在 fixed count 下 padding prompt length 来分离两个因素。这是一个潜在的 confound that weakens Channel 1 的 mechanistic interpretation。\n\n**R1-Q6 关于 TOST margin ±3pp**：Appendix E 选 ±3pp 但未给出 justification。在 typical batch difference 仅 2.2pp 的 context 下，±3pp margin 相当宽松——如果 margin 设为 ±1pp，TOST 可能不通过。这是一个 analyst degrees of freedom 问题。\n\n---\n\n## 对 Missing References 的回应\n\n**Banerjee et al. (2025)**: 我未独立搜索到此文。如果确实存在且直接 benchmark LLM-based schema extraction，则应引用。但 R1 未提供完整引用信息，需要验证。\n\n**Cohen (1988) / Lakens (2013)**: [AGREE] 非常相关。论文反复讨论 \"modest effect size\" 和 \"practical magnitude\" 但未引用 small-effect-size 方法论文献。引用这些经典文献可以为 \"r²=1.3-1.7% is still meaningful\" 的论点提供框架支撑。\n\n**Multiple testing correction**: [REBUT] 论文 Limitations section 最后一段明确讨论了 multiple comparisons 策略（\"We do not apply family-wise correction across datasets, treating each as an independent replication\"），并引用了 independent replication 逻辑。Perneger (1998) 和 Rothman (1990) 实际上支持论文的 no-correction 策略（Rothman 著名地反对 Bonferroni），所以引用它们反而会强化论文立场。\n\n---\n\n## 对 Overall Assessment 的意见\n\nR1 给出 **Findings 3/5**。我的评分是 **Borderline reject 2.5/5**。\n\n差异来源：\n- R1 更看重方法论严谨性（确实优秀）；我更看重 novelty 和 practical impact\n- 我认为 \"SCS 与 LLM-PEE 形式相同\" + \"typical effect 2.2pp\" + \"NER decomposition 完全失败\" 三者叠加，使论文的 contribution 不足以支撑 main conference\n- R1 的 Findings track 建议合理——如果 novelty bar 降低，方法论质量足够\n\n**我的修正评分**: 如果 authors 能 (1) 将 \"separable\" 限定为 RE-specific，(2) 移除 p=0.19 结果的 contribution 定位，(3) 以 typical-batch 2.2pp 为主锚重写 framing——我愿意上调至 **weak accept for Findings** (3/5)。当前 framing 下维持 2.5/5。\n",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-16T15:17:41.305123+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3875
}
```

</details>

---


### Assistant

_source line 474 · 2026-05-16T15:17:50.943319+00:00_

已向 Review Director 提交对 Reviewer 1 的逐条回应。核心立场：

- **W1 (separability)**: AGREE — 与我自己的 W4 一致，NER 上无统计支撑
- **W2 (5 batches)**: REBUT — monotonic pattern 跨 4 数据集复现 + cross-model r=0.725，5 batches 不动摇 direction claim，但应补 error bars
- **W3 (r²=1.3-1.7%)**: AGREE — conditioning bias 存在，但 Monte Carlo 外部验证部分缓解
- **W4 (不同 embedding)**: AGREE — Few-NERD 用 Qwen3 有循环论证风险
- **W5 (contamination)**: AGREE — borderline defense
- **W6 (31.2pp framing)**: AGREE — 与我的 W2 一致
- **W7 (单种子)**: REBUT — greedy decoding 下 seed 不构成问题
- **W8 (bootstrap)**: REBUT — B=1,000 是 standard practice

整体评分差异：R1 给 Findings 3/5，我给 2.5/5，主要因为我对 novelty/impact 要求更高。如果修正 framing 问题，我愿上调至 Findings 3/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 15

## Round 15

62 recorded events


### User

_source line 475 · 2026-05-16T16:35:00.808661+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 相关工作完整性 + 整体贡献评估 + framing**。

## Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式**: ACL 2-column template, 8 页正文 + 无限参考文献/附录, double-blind
- **匿名规则**: 严格 double-blind

## 论文路径
`projects/schema-dag-extraction/docs/paper/main.tex`（含 \input 的子文件）

## 审查侧重

请从以下角度严格评审：

1. **新颖性评估**：
   - "Two-channel degradation" 是否为真正的 conceptual contribution 还是常识性直觉的 formalization？
   - SCS/BCS 与 LLM-PEE 的 embedding similarity 有何本质区别？
   - Controlled methodology 的方法论新颖性是否足以支撑 EMNLP main conference？

2. **Framing 和 claims 的合理性**：
   - Abstract 和 Introduction 的 headline 数字选择是否诚实反映 typical effect？
   - "First controlled study" 声称是否 overclaim？
   - RQ3（decomposition）的答案是 negative result — contributions 是否正确反映？
   - Contribution #4 中 "Diagnosis to mitigation" 措辞是否暗示正面结果？

3. **相关工作的完整性**：
   - Schema complexity 文献是否充分覆盖？
   - 是否遗漏近期 (2025-2026) 的重要工作？
   - LLM-PEE 对比是否公平？
   - Hierarchical classification / label confusion 在传统 ML 中有大量文献，是否充分引用？

4. **整体贡献 vs. venue 标准**：
   - 作为 empirical analysis paper，发现的深度和广度是否达到 EMNLP 2026 main conference 标准？
   - 对社区的实际影响和 actionable insights 是什么？
   - 负结果（SDGD failure, +1.4pp n.s.）是否有独立的发表价值？

请按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出审稿意见。Weaknesses 请按严重程度排序，每条给出具体 evidence 和建议修改方案。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-16T16:35:06.980827+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-16T16:35:07.032176+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-16T16:35:10.095638+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 479 · 2026-05-16T16:35:10.146404+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-16T16:35:12.354945+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-16T16:35:12.405541+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-16T16:35:17.494606+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-16T16:35:17.595435+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-16T16:35:21.962954+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 485 · 2026-05-16T16:35:22.064041+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-16T16:35:22.164781+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 487 · 2026-05-16T16:35:22.366004+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-16T16:35:22.468027+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 489 · 2026-05-16T16:35:22.468949+00:00_

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
17	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
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
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\text{TOST}} = 0.003$, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontologic
…[truncated 26937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool result

_source line 490 · 2026-05-16T16:35:22.469299+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 1
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-16T16:35:31.010581+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on my search results, I found comprehensive information about ACL Rolling Review 2026 reviewer guidelines, review forms, and evaluation criteria. Here's what I found:

## Reviewer Guidelines

The reviewer's main tasks are (1) checking the appropriateness of the submission
…[truncated 2276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9047
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-16T16:35:36.129889+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form scoring dimensions soundness excitement reproducibility 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form scoring dimensions soundness excitement reproducibility 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 493 · 2026-05-16T16:35:36.632393+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 494 · 2026-05-16T16:35:36.733283+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. We present the first controlled study isolating type confusability from type count in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets. We introduce the Schema Confusability Score (SCS) and two experimental paradigms: count curves (varying schema size while randomizing confusability) and BCS-controlled experiments (fixing size while varying confusability).
3	
4	We identify two degradation channels: count-driven recall decline and confusability-driven type substitution. In typical random batches, confusability accounts for ${\approx}\,2.2$\,pp accuracy difference; under quartile contrast the gap reaches $-5.3$\,pp, and batch-level BCS explains up to 53\% of cross-batch variance. The channels are cleanly separable in RE (TOST equivalence test, $p = 0.003$) but coupled in NER where boundary and type ambiguity interact. Effects are directionally consistent across prompt designs and model scales, though Channel~2 attenuates on smaller models. Schema decomposition via oracle routing recovers +29.8\,pp for RE, but confusability-aware grouping yields no significant improvement over random grouping (+1.4\,pp, $p \approx 0.19$, n.s.).
5	\end{abstract}
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 495 · 2026-05-16T16:35:37.084890+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 496 · 2026-05-16T16:35:37.587218+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	We present the first controlled study isolating type confusa
…[truncated 2686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 497 · 2026-05-16T16:35:37.587693+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 498 · 2026-05-16T16:35:38.039972+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting \cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms. Concurrently, \citet{haystack-to-needle-2025} redu
…[truncated 1932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-16T16:35:38.040441+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-16T16:35:38.542723+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\
…[truncated 7281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-16T16:35:38.543193+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-16T16:35:39.448364+00:00_

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
20	\caption{\textbf{(a)} Count-degradation curves across three tasks. Error bars show $\pm 1$\,SD across 5 random type batches per count level (omitted at count${}\,=\,1$ where each type is evaluated individually). NER recall and RE accuracy decline monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\%), FewRel accuracy from 85.7\% to 50.4\% ($-$35.3\,pp), and DocRED from 88.0\% to 38.7\% ($-$56\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.
25	
26	\subsection{Pairwise Confusability and Type Confusion}
27	\label{sec:pairwise}
28	
29	We test whether pairwise SCS predicts type-le
…[truncated 8919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-16T16:35:39.448912+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 504 · 2026-05-16T16:35:39.951212+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an adopted abbreviation for schema decomposition and grouping; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.
5	
6	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\,=\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\ref{tab:sdgd_results}, Appendix~\ref{sec:appendix_sdgd}).
7	
8	\paragraph{Merge amplification in NER.}
9	The core failure mechanism is \emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calib
…[truncated 4344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-16T16:35:39.951699+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 506 · 2026-05-16T16:35:40.153099+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1 extreme-batch gap; Appendix~\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}).
6	
7	\paragraph{Prompt length as mechanism.}
8	Count-driven degradation (Channel~1) may partly reflect prompt length increase: adding types mechanically lengthens the prompt, and per-type recall (0.586) substantially exceeds single-pass recall (0.368), consistent with lost-in-middle effects \cite{lost-in-middle-2024}. Disentangling count from prompt length would require fixed-count variable-length experiments, which we leave to future work.
9	
10	\paragraph{Why does embedding similarity predict LLM confusion?}
11	Type name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest (conditional $R^2 \approx 7\%$ among non-zero confusion pairs; unconditional $r^2 = 1.3$--$1.7\%$) but amplifies ${\sim}3\times$ at the batch level through inter-pair correlation (Appendix~\ref{app:aggregation-sim}), yielding batch-level $R^2$ of
…[truncated 1454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-16T16:35:40.203750+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-16T16:35:40.254543+00:00_

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
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}, vLLM \cite{vllm-2023}, and all-Mini
…[truncated 4435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-16T16:35:44.320981+00:00_

Web search results for query: "ACL Rolling Review review form scoring dimensions soundness excitement reproducibility 2025 2026"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) scoring dimensions for the review form in 2025-2026:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked
…[truncated 1838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8191
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-16T16:35:48.996024+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 511 · 2026-05-16T16:35:48.996371+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-16T16:35:50.502742+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-16T16:35:50.704613+00:00_

1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	% =============================================================================
6	% DIRECT COMPETITORS
7	% =============================================================================
8	
9	@inproceedings{llm-pee-2025,
10	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
11	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
12	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
13	    year      = {2025},
14	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
15	}
16	
17	@article{parse-2025,
18	    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
19	    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
20	    journal = {arXiv preprint arXiv:2510.08623},
21	    year    = {2025},
22	    url     = {https://arxiv.org/abs/2510.08623},
23	}
24	
25	@inproceedings{dee-2024,
26	    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},
27	    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},
28	    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},
29	    year      = {2024},
30	    url       = {https://arxiv.org/abs/2406.01045},
31	}
32	
33	@inproceedings{crossagentie-2025,
34	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
35	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},
36	    booktitle = {Findings of the Association for Computational Linguistics: ACL
…[truncated 21581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-16T16:35:50.755568+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-16T16:35:50.806547+00:00_

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
…[truncated 5190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-16T16:35:57.132485+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their exact scale (1-5 etc), and the description for each score level. I need the exact wording for soundness, excitement, overall assessment, reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their exact scale (1-5 etc), and the description for each score level. I need the exact wording for soundness, excitement, overall assessment, reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-16T16:36:04.725701+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully..."
- **4**: "Quite sure. I tried to check the important points carefully..."
- **3**: "Pretty sure, but there's a chance I missed something..."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed..."
- **1**: "Not my area, or paper is very hard to understand..."

## Soundness
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen..."
- **4**: "Strong: This study provides sufficient support for all claims..."
- **3**: "Acceptable: This study provides sufficient support for main claims..."
- **2**: "Poor: Some main claims are not sufficiently supported..."
- **1**: "Major Issues: This study is not yet sufficiently thorough..."

## Excitement
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others..."
- **4**: "Exciting: I would mention this paper to others..."
- **3**: "Interesting: I might mention some points..."
- **2**: "Potentially Interesting: this paper does not resonate with me..."
- **1**: "Not Exciting: this paper does not resonate with me..."

## Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: "Consider for Award" (top 2.5%)
- **4**: "Conference: I think this paper could be accepted..."
- **3**: "Findings: I think this paper could be accepted to Findings..."
- **2**: "Resubmit next cycle: substantial revisions needed..."
- **1**: "Do not resubmit: fully redone or not relevant..."

## Reproducibility
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results..."
- **3**: "They could reproduce with some difficulty..."
- **2**: "They would be hard pressed to reproduce..."
- **1**: "They would not be able to reproduce..."

## Datasets & Software
Scale: 1-5 each
- **5**: "Enabling: should affect research project choice
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7593
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-16T16:36:09.346091+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM information extraction schema complexity type confusion label space 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM information extraction schema complexity type confusion label space 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 519 · 2026-05-16T16:36:10.351318+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "zero-shot NER large label set type confusability hierarchical label confusion 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "zero-shot NER large label set type confusability hierarchical label confusion 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-16T16:36:11.004818+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "label confusion matrix embedding similarity prediction classification 2024 2025 NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "label confusion matrix embedding similarity prediction classification 2024 2025 NLP"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-16T16:36:16.779200+00:00_

Web search results for query: "zero-shot NER large label set type confusability hierarchical label confusion 2025 2026"

Links: [{"title":"Ensembling Prompting Strategies for Zero-Shot ...","url":"https://aclanthology.org/2025.emnlp-main.918.pdf"},{"title":"ZERONER: Fueling Zero-Shot Named Entity Recognition ...","url":"https://aclanthology.org/2025.findings-acl.805.pdf"},{"title":"Advancing Few-Shot Named Entity Recognition with Large Language Model","url":"https://www.mdpi.com/2076-3417/15/7/3838"},{"title":"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets | OpenReview","url":"https://openreview.net/forum?id=NEEtm5laNK1"},{"title":"[2302.02551] CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets","url":"https://arxiv.org/abs/2302.02551"},{"title":"Zero-shot learning in the presence of hierarchically coarsened labels","url":"https://eurekamag.com/research/101/175/101175343.php"},{"title":"Few-Shot and Zero-Shot Multi-Label Learning for Structured Label Spaces - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6375489/"},{"title":"GitHub - acmi-lab/CHILS: Code and results accompanying our paper titled CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets · GitHub","url":"https://github.com/acmi-lab/CHILS"},{"title":"Zero-Shot Learning in the Presence of Hierarchically Coarsened Labels","url":"https://openaccess.thecvf.com/content_CVPRW_2020/papers/w54/Samplawski_Zero-Shot_Learning_in_the_Presence_of_Hierarchically_Coarsened_Labels_CVPRW_2020_paper.pdf"},{"title":"Preserving Zero-shot Capability in Supervised Fine-tuning ...","url":"https://aclanthology.org/2025.findings-naacl.315.pdf"}]

I found several relevant research papers related to your query. Here's what the search returned:

**Recent Zero-Shot NER and Hierarchical Label Research (2025-2026):**

The paper "ZERONER: Fueling Zero-Shot Named Entity Recognition" was published in the Findings of ACL 2025 (July 27 - August 1, 2025), which directly addresses zero-sh
…[truncated 1242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6427
}
```

</details>

---


### Tool result

_source line 522 · 2026-05-16T16:36:17.792086+00:00_

Web search results for query: "LLM information extraction schema complexity type confusion label space 2025 2026"

Links: [{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"LLM Structured Output Benchmarks are Riddled with Mistakes","url":"https://cleanlab.ai/blog/structured-output-benchmark/"},{"title":"ScrapeGraphAI-100k: Dataset for Schema-Constrained LLM Generation","url":"https://arxiv.org/html/2602.15189"},{"title":"Structured data extraction from unstructured content using LLM schemas","url":"https://simonwillison.net/2025/Feb/28/llm-schemas/"},{"title":"Structured Outputs: Reliable Schema-Validated Data Extraction from Language Models - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/structured-outputs-schema-validated-data-extraction-language-models"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"LLMs for Structured Data Extraction from PDFs in 2026","url":"https://unstract.com/blog/comparing-approaches-for-using-llms-for-structured-data-extraction-from-pdfs/"},{"title":"Leveraging large language models for structured information extraction from pathology reports - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2153353925001075"},{"title":"LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models","url":"https://arxiv.org/html/2504.00752v1"}]

I've completed the web search for your query on LLM information extraction schema complexity, type confusion, and label space in 2025-2026. Here are the key findings:

## Schema Complexity and LLM Challenges

LLMs strugg
…[truncated 1578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8445
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-16T16:36:18.144038+00:00_

Web search results for query: "label confusion matrix embedding similarity prediction classification 2024 2025 NLP"

Links: [{"title":"Text Classification. Text Classification with Embeddings and… | by Ruma Sinha | Medium","url":"https://rumasinha.medium.com/text-classification-1e81c83c6f68"},{"title":"How to interpret a confusion matrix for a machine learning model","url":"https://www.evidentlyai.com/classification-metrics/confusion-matrix"},{"title":"Label Confusion Learning to Enhance Text Classiﬁcation Models","url":"https://www.atailab.cn/seminar2021Spring/pdf/AAAI_2021_Label%20Confusion%20Learning%20to%20Enhance%20Text%20Classification%20Models.pdf"},{"title":"How to Use Confusion Matrices to Debug NLP Models | by Sachin K Singh | Medium","url":"https://medium.com/@isachinkamal/how-to-use-confusion-matrices-to-debug-nlp-models-834c98cd5e76"},{"title":"Understanding the Confusion Matrix in Machine Learning - GeeksforGeeks","url":"https://www.geeksforgeeks.org/machine-learning/confusion-matrix-machine-learning/"},{"title":"Knowledge-Based Construction of Confusion Matrices for ...","url":"https://ceur-ws.org/Vol-2998/paper6.pdf"},{"title":"Semantic Similarity through Classification Confusion","url":"https://aclanthology.org/2025.naacl-long.299.pdf"},{"title":"MLMC: Interactive multi-label multi-classifier evaluation without confusion matrices","url":"https://arxiv.org/html/2501.14460v1"},{"title":"Interpretable Text Embeddings and Text Similarity ...","url":"https://aclanthology.org/2025.emnlp-main.1135.pdf"},{"title":"(PDF) Multi-label Classifier Performance Evaluation with Confusion Matrix","url":"https://www.researchgate.net/publication/342873309_Multi-label_Classifier_Performance_Evaluation_with_Confusion_Matrix"}]

I've performed a web search for your query and found several relevant results. Here's what I discovered about label confusion, embedding similarity, and classification in NLP from 2024-2025:

## Key Findings:

**Label Confusion Models in NLP:**
R
…[truncated 1545 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7139
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-16T16:36:21.757011+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"label semantic similarity\" \"classification confusion\" predict NLP ACL EMNLP 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"label semantic similarity\" \"classification confusion\" predict NLP ACL EMNLP 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 525 · 2026-05-16T16:36:22.309323+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CHiLS hierarchical label sets zero-shot classification confusion sibling classes 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CHiLS hierarchical label sets zero-shot classification confusion sibling classes 2023"
  }
}
```

</details>

---


### Tool result

_source line 526 · 2026-05-16T16:36:26.932461+00:00_

Web search results for query: "CHiLS hierarchical label sets zero-shot classification confusion sibling classes 2023"

Links: [{"title":"[2302.02551] CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets","url":"https://arxiv.org/abs/2302.02551"},{"title":"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets | OpenReview","url":"https://openreview.net/forum?id=NEEtm5laNK1"},{"title":"(PDF) CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets","url":"https://www.researchgate.net/publication/368305006_CHiLS_Zero-Shot_Image_Classification_with_Hierarchical_Label_Sets"},{"title":"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets","url":"https://arxiv.org/pdf/2302.02551"},{"title":"GitHub - acmi-lab/CHILS: Code and results accompanying our paper titled CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets · GitHub","url":"https://github.com/acmi-lab/CHILS"},{"title":"ICML Poster CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets","url":"https://icml.cc/virtual/2023/poster/24774"},{"title":"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets","url":"https://proceedings.mlr.press/v202/novack23a.html"},{"title":"ICLR CHiLS: Zero-shot Image Classification with Hierarchical Label Sets","url":"https://iclr.cc/virtual/2023/13793"},{"title":"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets | DeepAI","url":"https://deepai.org/publication/chils-zero-shot-image-classification-with-hierarchical-label-sets"},{"title":"CHILS: ZERO-SHOT IMAGE CLASSIFICATION WITH ...","url":"https://zacharynovack.github.io/CHiLS_preprint.pdf"}]

I found comprehensive information about CHiLS. Here's what the search results show:

## Overview

CHiLS (Classification with Hierarchical Label Sets) is an alternative strategy for zero-shot classification specifically designed for datasets with implicit semantic hierarchies.

## How CHiLS Works

CHiLS proceeds in three steps: (i) for each clas
…[truncated 1090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4623
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-16T16:36:27.786454+00:00_

Web search results for query: ""label semantic similarity" "classification confusion" predict NLP ACL EMNLP 2024 2025"

Links: [{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"Semantic Similarity through Classification Confusion","url":"https://aclanthology.org/2025.naacl-long.299.pdf"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-emnlp/"},{"title":"Logits Reranking via Semantic Labels for Hard Samples in ...","url":"https://aclanthology.org/2024.findings-emnlp.657.pdf"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"LLMs Can Also Do Well! Breaking Barriers in Semantic ...","url":"https://aclanthology.org/2025.findings-acl.1189.pdf"},{"title":"A Coarse-to-Fine Prototype Learning Approach for Multi- ...","url":"https://aclanthology.org/2024.findings-emnlp.140.pdf"},{"title":"Grounded Semantic Role Labelling from Synthetic Multimodal Data for Situated Robot Commands - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1212/"},{"title":"Semantic Role Labelling: A Systematic Review of Approaches, Challenges, and Trends for English and Indian Languages - Chakma - 2025 - Expert Systems - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/exsy.13838"},{"title":"Using similarity network analysis to improve text similarity calculations | Applied Network Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41109-025-00699-7"}]

Based on the search results, I found relevant research matching your query about label semantic similarity and classification confusion in NLP:

## Key Finding

A paper titled "Semantic Similarity through Classification Confusion" appears to directly address your research interests. This work is published in th
…[truncated 1171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6029
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-16T16:36:32.024617+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Semantic Similarity through Classification Confusion\" NAACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Semantic Similarity through Classification Confusion\" NAACL 2025"
  }
}
```

</details>

---


### Tool call

_source line 529 · 2026-05-16T16:36:32.476804+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "controlled experiment confound isolation NLP empirical study methodology EMNLP 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "controlled experiment confound isolation NLP empirical study methodology EMNLP 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 530 · 2026-05-16T16:36:37.446642+00:00_

Web search results for query: "controlled experiment confound isolation NLP empirical study methodology EMNLP 2024 2025"

Links: [{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing - EMNLP 2024","url":"https://2024.emnlp.org/"},{"title":"dblp: EMNLP","url":"https://dblp.org/db/conf/emnlp/index.html"},{"title":"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations - ACL Anthology","url":"https://aclanthology.org/volumes/2025.emnlp-demos/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track - ACL Anthology","url":"https://aclanthology.org/volumes/2025.emnlp-industry/"},{"title":"Empirical Methods in Natural Language Processing | ACL Member Portal","url":"https://www.aclweb.org/portal/emnlp"},{"title":"EMNLP 2025 The 2025 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2025.emnlp-tutorials.pdf"},{"title":"EMNLP: Empirical Methods in Natural Language Processing","url":"https://dl.acm.org/doi/proceedings/10.5555/1613715"},{"title":"Empirical Methods in Natural Language Processing (EMNLP) 2024 - Apple Machine Learning Research","url":"https://machinelearning.apple.com/updates/apple-at-emnlp-2024"},{"title":"EMNLP 2024 The 2024 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2024.findings-emnlp.0.pdf"}]

I found information about EMNLP 2024 and 2025 conferences. Here's what the search results show:

## EMNLP 2024 and 2025 Conferences

EMNLP 2024 was held November 12-16 in Miami, Florida, while EMNLP 2025 was held in Suzhou, China, November 4-9, 2025.

## Conference Coverage

The search results include proceedings and demonstrations from both conferences. EMNLP 2024 proceedings were published by the Association for Computational Linguisti
…[truncated 770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4969
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-16T16:36:43.471721+00:00_

Web search results for query: ""Semantic Similarity through Classification Confusion" NAACL 2025"

Links: [{"title":"Rethinking Word Similarity: Semantic Similarity through Classification Confusion - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.299/"},{"title":"Semantic Similarity through Classification Confusion","url":"https://aclanthology.org/2025.naacl-long.299.pdf"},{"title":"[2502.05704] Rethinking Word Similarity: Semantic Similarity through Classification Confusion","url":"https://arxiv.org/abs/2502.05704"},{"title":"[2502.05704v1] Rethinking Word Similarity: Semantic Similarity through Classification Confusion","url":"http://arxiv.org/abs/2502.05704v1"},{"title":"Rethinking Word Similarity: Semantic Similarity through Classification Confusion","url":"https://arxiv.org/html/2502.05704v1"},{"title":"Rethinking Word Similarity: Semantic Similarity through Classification Confusion | OpenReview","url":"https://openreview.net/forum?id=KmhVC7FKXN"},{"title":"Findings of the Association for Computational Linguistics:","url":"https://aclanthology.org/2025.findings-naacl.263.pdf"},{"title":"Understanding Conversational AI Philosophy, Ethics, and Social","url":"https://ubiquitypress.com/books/130/files/6a695d3d-40a3-4e2c-b09b-ce33a9985780.pdf"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"}]

I found the paper! Here's the information about "Semantic Similarity through Classification Confusion" from NAACL 2025:

## Paper Overview

The paper is titled "Rethinking Word Similarity: Semantic Similarity through Classification Confusion" and is authored by Kaitlyn Zhou, Haishan Gao, Sarah Li Chen, Dan Edelstein, Dan Jurafsky, and Chen Shani.

## Key Contribution

The authors propose a new measure of similarity called Word Confusion that reframes semantic similarity in terms of feature-based classification
…[truncated 1027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11447
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-16T16:36:48.293305+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 533 · 2026-05-16T16:37:54.107156+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 47, \"total_citations\": 72, \"unique_cited_keys\": 47, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 36, \"online_not_found\": 4, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"llm-pee-2025\", \"type\": \"inproceedings\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"authors\": \"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"parse-2025\", \"type\": \"article\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"authors\": \"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.08623\"}, {\"key\": \"dee-2024\", \"type\": \"inproceedings\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"authors\": \"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\"}, {\"key\": \"crossagentie-2025\", \"type\": \"inproceedings\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"authors\": \"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"cmas-ner-2025\", \"type\": \"inproceedings\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"auth
…[truncated 38055 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 65813
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-16T16:41:26.648459+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见（Round 1）\n\n**论文**: *Does Type Confusability Shape Schema-Induced Degradation in Training-Free LLM Information Extraction?*\n**审查侧重**: 新颖性 + 相关工作完整性 + 整体贡献评估 + Framing\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: 实验设计严谨、统计方法扎实的经验分析论文，但核心发现（语义相似的类型更容易混淆）缺乏惊喜感，pairwise effect size 极小（$r^2 = 1.3\\text{--}1.7\\%$），mitigation 实验为负结果，整体 novelty 和 actionable impact 不足以支撑 EMNLP main conference。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 控制变量设计合理，TOST/bootstrap CI/permutation test 规范；但 single-seed 评估、SCS 用提取模型自身 embedding（Few-NERD）、FewRel train+val 合并等削弱了部分 claim 稳健性 |\n| Excitement | 2.5 / 5 | 核心发现符合直觉、可预测性强；负结果（SDGD failure）虽有价值但未指出前进路径；pairwise r² 极小；practical impact 有限 |\n| Reproducibility | 4.0 / 5 | 数据集公开、模型开源、decoding 参数明确、承诺代码发布；扣分：single seed、未量化 seed variance |\n| Overall | 3.0 / 5 | 质量适合 Findings，不满足 main conference 的 novelty/excitement 门槛 |\n\n**Reviewer Confidence**: 4 / 5\n\n---\n\n## 主要优势\n\n1. **实验设计精巧**。Count curves + BCS-controlled 双范式有效解耦 schema size 和 confusability。Within-pool analysis（§5.3, Table 6）排除 pool composition 混淆，permutation test ($p = 0.60$) 令人信服。\n\n2. **负结果的诚实报告**。SDGD 全面失败（§6）的报告——特别是 merge amplification 机制的诊断——对社区有价值。\n\n3. **Centrality confound 分析**（§5.5, Appendix F）。发现 MAVEN 的 positive BCS-F1 相关是 centrality artifact 并通过 partial correlation 消除，是论文最有洞察力的部分。\n\n4. **统计方法规范**。TOST equivalence test、cluster bootstrap、Monte Carlo aggregation simulation 等，在 NLP empirical 论文中属于上乘。\n\n5. **四数据集三任务覆盖 + cross-model validation**。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **核心发现 novelty 不足：SCS 不是新指标，\"similar labels cause confusion\" 不是新发现**\n- 位置：§2 Related Work \"SCS novelty\" 段落；§3.2\n- SCS = pairwise cosine similarity = LLM-PEE 的 partitioning criterion（论文自己承认）\n- 核心结论对 IE 从业者而言是 common sense 级别直觉\n- Pairwise r² = 1.3-1.7% 意味着 SCS 只解释极小部分混淆 variance；Cohen (1988) 的 \"small effect\" 标准面向行为科学，在 engineering NLP 论文中此 bar 不够\n- \"Controlled factorial design\" 是标准方法论，应用到新 domain 不构成方法论创新\n- **建议**：挖掘更深发现——剩下 98.3% variance 由什么解释？或提出更有预测力的 confusion predictor（如 attention/logit-based measure）\n\n**N2** [critical] **Contribution #4 \"Diagnosis to mitigation\" framing 误导——mitigation 失败了**\n- 位置：§1 Contribution 4；§6\n- NER SDGD: F1 0.445→0.251 全面崩塌；RE graph-coloring: +1.4 pp n.s.；confidence gating 更差\n- \"Mitigation\" 暗示成功缓解，但 RQ3 答案是 negative\n- **建议**：改为 \"Schema decomposition reveals structural barriers\"，将 merge amplification 发现作为贡献点\n\n**N3** [critical] **Hierarchical classification / label confusion 文献覆盖严重不足**\n- 位置：§2 Related Work ¶3\n- 只引了 Deng et al. (2010) ImageNet。遗漏：\n  - Zhou et al. \"Semantic Similarity through Classification Confusion\" (NAACL 2025) — 概念上的逆问题\n  - Guo et al. \"Label Confusion Learning\" (AAAI 2021) — 用 label embedding similarity 构建 confusion distribution\n  - Novack et al. \"CHiLS\" (ICML 2023) — hierarchical label decomposition 解决 zero-shot sibling confusion\n  - ZERONER (ACL Findings 2025) — 近期 zero-shot NER\n  - HTC 文献中大量 sibling confusion 经验发现\n- 削弱了 \"first controlled study\" 声称的可信度\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] **Abstract/Introduction headline 数字 cherry-picking**\n- \"up to 53%\" 是 DocRED 最大值，FewRel 只有 22%。count curve 的 -42% decline 混合了 Channel 1+2\n- **建议**：报告 range（\"22-53%\"），以 typical effect (2.2 pp) 为主 headline\n\n**W2** [warning] **\"First controlled study\" 声称需 qualify**\n- LLM-PEE 的 partitioning 隐式控制了 confusability；传统 ML 中此类设计很常见\n- **建议**：改为 \"a systematic controlled study\"\n\n**W3** [warning] **Single-seed 评估削弱 claim 稳健性**\n- Batch sampling 是 random 的，但 seed variance 未量化\n- Extreme batches 每组只有 1 个（Table 7 注释承认了这一点），应在正文中 prominent 声明\n\n**W4** [warning] **LLM-PEE 对比不够公平和深入**\n- LLM-PEE 做 ED decomposition 获得正面结果，SDGD 失败——差异原因未讨论\n- 说 LLM-PEE \"conflates\" count 和 confusability 不够公允\n\n**W5** [warning] **RE 实验的 ecological validity**\n- FewRel train+val 合并、oracle routing、closed-set classification format 与实际 RE 任务差距较大\n- BCS-controlled RE 的 routing 策略不够清楚\n\n---\n\n## 小问题\n- SCS validation label 未被引用\n- Abstract 中 \"BCS slopes: p=0.60\" 首次出现缺乏上下文\n- Table 5 caption 的 v1/v2 选择逻辑未在正文解释\n- 引用验证显示 gliner2-2025、sclar-sensitivity-2024、json-schema-bench-2025、li2023evaluating 在 OpenAlex 中未精确匹配\n\n## 缺失引用\n- Zhou et al., NAACL 2025 — Semantic Similarity through Classification Confusion\n- Guo et al., AAAI 2021 — Label Confusion Learning\n- Novack et al., ICML 2023 — CHiLS\n- ZERONER, ACL Findings 2025",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见（Round 1）\n\n**论文**: *Does Type Confusability Shape Schema-Induced Degradation in Training-Free LLM Information Extraction?*\n**审查侧重**: 新颖性 + 相关工作完整性 + 整体贡献评估 + Framing\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: 实验设计严谨、统计方法扎实的经验分析论文，但核心发现（语义相似的类型更容易混淆）缺乏惊喜感，pairwise effect size 极小（$r^2 = 1.3\\text{--}1.7\\%$），mitigation 实验为负结果，整体 novelty 和 actionable impact 不足以支撑 EMNLP main conference。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 控制变量设计合理，TOST/bootstrap CI/permutation test 规范；但 single-seed 评估、SCS 用提取模型自身 embedding（Few-NERD）、FewRel train+val 合并等削弱了部分 claim 稳健性 |\n| Excitement | 2.5 / 5 | 核心发现符合直觉、可预测性强；负结果（SDGD failure）虽有价值但未指出前进路径；pairwise r² 极小；practical impact 有限 |\n| Reproducibility | 4.0 / 5 | 数据集公开、模型开源、decoding 参数明确、承诺代码发布；扣分：single seed、未量化 seed variance |\n| Overall | 3.0 / 5 | 质量适合 Findings，不满足 main conference 的 novelty/excitement 门槛 |\n\n**Reviewer Confidence**: 4 / 5\n\n---\n\n## 主要优势\n\n1. **实验设计精巧**。Count curves + BCS-controlled 双范式有效解耦 schema size 和 confusability。Within-pool analysis（§5.3, Table 6）排除 pool composition 混淆，permutation test ($p = 0.60$) 令人信服。\n\n2. **负结果的诚实报告**。SDGD 全面失败（§6）的报告——特别是 merge amplification 机制的诊断——对社区有价值。\n\n3. **Centrality confound 分析**（§5.5, Appendix F）。发现 MAVEN 的 positive BCS-F1 相关是 centrality artifact 并通过 partial correlation 消除，是论文最有洞察力的部分。\n\n4. **统计方法规范**。TOST equivalence test、cluster bootstrap、Monte Carlo aggregation simulation 等，在 NLP empirical 论文中属于上乘。\n\n5. **四数据集三任务覆盖 + cross-model validation**。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **核心发现 novelty 不足：SCS 不是新指标，\"similar labels cause confusion\" 不是新发现**\n- 位置：§2 Related Work \"SCS novelty\" 段落；§3.2\n- SCS = pairwise cosine similarity = LLM-PEE 的 partitioning criterion（论文自己承认）\n- 核心结论对 IE 从业者而言是 common sense 级别直觉\n- Pairwise r² = 1.3-1.7% 意味着 SCS 只解释极小部分混淆 variance；Cohen (1988) 的 \"small effect\" 标准面向行为科学，在 engineering NLP 论文中此 bar 不够\n- \"Controlled factorial design\" 是标准方法论，应用到新 domain 不构成方法论创新\n- **建议**：挖掘更深发现——剩下 98.3% variance 由什么解释？或提出更有预测力的 confusion predictor（如 attention/logit-based measure）\n\n**N2** [critical] **Contribution #4 \"Diagnosis to mitigation\" framing 误导——mitigation 失败了**\n- 位置：§1 Contribution 4；§6\n- NER SDGD: F1 0.445→0.251 全面崩塌；RE graph-coloring: +1.4 pp n.s.；confidence gating 更差\n- \"Mitigation\" 暗示成功缓解，但 RQ3 答案是 negative\n- **建议**：改为 \"Schema decomposition reveals structural barriers\"，将 merge amplification 发现作为贡献点\n\n**N3** [critical] **Hierarchical classification / label confusion 文献覆盖严重不足**\n- 位置：§2 Related Work ¶3\n- 只引了 Deng et al. (2010) ImageNet。遗漏：\n  - Zhou et al. \"Semantic Similarity through Classification Confusion\" (NAACL 2025) — 概念上的逆问题\n  - Guo et al. \"Label Confusion Learning\" (AAAI 2021) — 用 label embedding similarity 构建 confusion distribution\n  - Novack et al. \"CHiLS\" (ICML 2023) — hierarchical label decomposition 解决 zero-shot sibling confusion\n  - ZERONER (ACL Findings 2025) — 近期 zero-shot NER\n  - HTC 文献中大量 sibling confusion 经验发现\n- 削弱了 \"first controlled study\" 声称的可信度\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] **Abstract/Introduction headline 数字 cherry-picking**\n- \"up to 53%\" 是 DocRED 最大值，FewRel 只有 22%。count curve 的 -42% decline 混合了 Channel 1+2\n- **建议**：报告 range（\"22-53%\"），以 typical effect (2.2 pp) 为主 headline\n\n**W2** [warning] **\"First controlled study\" 声称需 qualify**\n- LLM-PEE 的 partitioning 隐式控制了 confusability；传统 ML 中此类设计很常见\n- **建议**：改为 \"a systematic controlled study\"\n\n**W3** [warning] **Single-seed 评估削弱 claim 稳健性**\n- Batch sampling 是 random 的，但 seed variance 未量化\n- Extreme batches 每组只有 1 个（Table 7 注释承认了这一点），应在正文中 prominent 声明\n\n**W4** [warning] **LLM-PEE 对比不够公平和深入**\n- LLM-PEE 做 ED decomposition 获得正面结果，SDGD 失败——差异原因未讨论\n- 说 LLM-PEE \"conflates\" count 和 confusability 不够公允\n\n**W5** [warning] **RE 实验的 ecological validity**\n- FewRel train+val 合并、oracle routing、closed-set classification format 与实际 RE 任务差距较大\n- BCS-controlled RE 的 routing 策略不够清楚\n\n---\n\n## 小问题\n- SCS validation label 未被引用\n- Abstract 中 \"BCS slopes: p=0.60\" 首次出现缺乏上下文\n- Table 5 caption 的 v1/v2 选择逻辑未在正文解释\n- 引用验证显示 gliner2-2025、sclar-sensitivity-2024、json-schema-bench-2025、li2023evaluating 在 OpenAlex 中未精确匹配\n\n## 缺失引用\n- Zhou et al., NAACL 2025 — Semantic Similarity through Classification Confusion\n- Guo et al., AAAI 2021 — Label Confusion Learning\n- Novack et al., ICML 2023 — CHiLS\n- ZERONER, ACL Findings 2025",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-16T16:41:30.568034+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3919
}
```

</details>

---


### Assistant

_source line 536 · 2026-05-16T16:41:36.300215+00:00_

审稿意见已提交给 Review Director。

总结：给出 **Overall 3.0 / 5 (Findings)**。三个 Must-Fix：(1) SCS 不是新指标、核心发现缺乏 novelty；(2) Contribution #4 "Diagnosis to mitigation" 包装误导负结果；(3) hierarchical classification / label confusion 文献覆盖严重不足。五个 Should-Fix：headline 数字 cherry-picking、"first" 优先权声称需弱化、single-seed 问题、LLM-PEE 对比不够深入、RE 实验的 ecological validity。识别 4 篇缺失引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 16

## Round 16

4 recorded events


### User

_source line 537 · 2026-05-16T16:42:13.802446+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也请对 R1 的 Strengths 和 Questions 给出你的看法。

---

## Reviewer 1 完整审稿意见

**Overall**: 3.5/5

**官方维度打分**:
| 维度 | 分数 |
|------|------|
| Soundness | 3/5 |
| Excitement | 3.5/5 |
| Reproducibility | 3.5/5 |
| Reviewer Confidence | 4/5 |

### Must-Fix

**N1** [critical] Factorial separability claim 建立在选择性测试上
- 三项检验中只有一项通过（FewRel full regression TOST p=0.003）
- Few-NERD 2×2 factorial: p=0.50（不显著）
- FewRel 2×2 factorial (n=54): p_TOST=0.56（不显著）
- "regression approach provides the stronger test" 是 post-hoc 辩护
- 典型的 garden of forking paths 问题
- 建议：abstract/conclusion 中 "cleanly separable" 改为限定性表述

**N2** [critical] 典型效应量（2.2pp）是否足以支撑核心论点？
- CI 下界仅 0.4pp，接近零实际意义
- 98.3-98.7% 的 type confusion variance 由其他因素解释
- extreme-batch gap (-31.2pp) 和 conditional r² (7%) 放大感知效应
- "batch-level BCS explains up to 53%" 来自 DocRED 极端条件
- 建议：重新定位为 "confusability is detectable but not the primary driver"

**N3** [critical] Conditioning on non-zero pairs 引入选择偏差
- unconditional r²=1.3% vs conditional r²=7%
- Monte Carlo simulation 使用 conditional R²=0.074 作为输入
- 用 unconditional r²=0.013 结果会大幅缩水
- 建议：用 unconditional r² 重新运行 simulation

### Should-Fix

**W1** Single-seed evaluation 无法量化推断不确定性
**W2** 跨数据集 embedding 不一致削弱可比性
**W3** Count curve 每 level 仅 5 batches，稳定性存疑
**W4** FewRel 合并 train+val splits 的方法论风险
**W5** TOST equivalence margin (±3pp) 的 justification 非标准

### Strengths
1. 问题设定精准且有价值
2. 高度诚实的负面结果报告
3. 分析深度出色
4. Limitations 质量极高
5. 跨任务一致性

### Questions
Q1: 用 unconditional r² 替代 conditional R² 作 simulation 输入，结果是多少？
Q2: 5 random batches per count level 的 batch-to-batch variance 有多大？
Q3: 如何保证 full regression 通过 TOST 不是 cherry-picking？
Q4: NER 的 positive BCS-F1 correlation 归因于 frequency confound——controlling BCS 是否间接 controlled frequency？

### Missing References
- Lakens (2017) "Equivalence Tests: A Practical Primer"
- Simmons et al. (2011) "False-Positive Psychology"
- Stefan et al. (2019) on SESOI determination

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-16T16:44:31.835056+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1（Round 1）\n\n### Must-Fix\n\n**[AGREE with qualification] R1-N1: Factorial separability \"cleanly separable\" overclaim**\n三项检验中一项通过（regression TOST p=0.003）两项 inconclusive（Few-NERD p=0.50, FewRel 2×2 p_TOST=0.56）。但这更接近 power difference 而非 cherry-picking：regression 用 69 batches × 5 count levels，2×2 只有 54 points × 2 levels。论文透明报告了全部结果（Appendix D）。建议改为 \"separable in RE under sufficient power; consistent but inconclusive at smaller samples\"。\n\n**[AGREE] R1-N2: 典型效应量 2.2pp 太小**\n与我的 R2-N1 完全一致。CI 下界 0.4pp，98.3% variance 未解释。Count effect (-42% to -56%) vs confusability typical effect (2.2pp) magnitude 差两个数量级，\"two-channel\" 对称 framing 不成立。同意改为 \"detectable but not primary driver\"。\n\n**[AGREE with nuance] R1-N3: Conditioning on non-zero pairs 引入 selection bias**\nConditional R²=7% vs unconditional r²=1.3% 的差距确实需要解释。但 Appendix I simulation 的目的是验证 aggregation math consistency，non-zero pairs 是 batch-level variance 的实际贡献者，所以 conditional R² 作为 input 有一定合理性。建议：用 unconditional r² 作为 lower bound 重新运行 simulation，明确讨论 discrepancy。\n\n### Should-Fix\n\n**[AGREE] R1-W1 (single-seed)**: 与我的 R2-W3 一致。\n**[REBUT partial] R1-W2 (embedding 不一致)**: 论文提供了 cross-check（MiniLM r=0.172 vs Qwen3 r=0.138, matrix correlation 0.894），方向一致。真正问题是 shared-representation bias，非 embedding 选择。\n**[AGREE] R1-W3 (5 batches per level)**: n=5 SD 估计不稳定。\n**[AGREE] R1-W4 (FewRel train+val merge)**: contamination p=0.06 marginal，不能排除。\n**[REBUT partial] R1-W5 (TOST ±3pp margin)**: Table 4 sensitivity analysis 显示 ±2pp 也 marginally equivalent (p=0.047)，interaction=0.47pp, 90% CI [-1.0, 2.0]pp，具体 margin 选择不 critical。但应引用 Lakens 2017。\n\n### Strengths 回应\n全部同意，特别是 S2（负面结果诚实）和 S4（Limitations 质量）。S5（跨任务一致性）部分同意——count channel 一致，confusability channel 实际上是 RE clean / NER coupled / MAVEN confounded 的不一致模式。\n\n### Questions 回应\nQ1 (unconditional simulation): 粗估 simulated batch R²≈0.039，远低于 observed 0.218。需要论文解释此 discrepancy。\nQ4 (NER frequency confound): 好问题。Few-NERD BCS-controlled 可能间接控制了 frequency。论文对 MAVEN 做了 centrality control 但未对 Few-NERD 做同样分析。\n\n### 评分差异\nR1 Overall 3.5 vs 我 3.0。差异在 Excitement（R1: 3.5, 我: 2.5）。R1 更看重方法论贡献，我更关注核心发现 novelty。3.0-3.5 差异合理，论文属 borderline Findings/Main。",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1（Round 1）\n\n### Must-Fix\n\n**[AGREE with qualification] R1-N1: Factorial separability \"cleanly separable\" overclaim**\n三项检验中一项通过（regression TOST p=0.003）两项 inconclusive（Few-NERD p=0.50, FewRel 2×2 p_TOST=0.56）。但这更接近 power difference 而非 cherry-picking：regression 用 69 batches × 5 count levels，2×2 只有 54 points × 2 levels。论文透明报告了全部结果（Appendix D）。建议改为 \"separable in RE under sufficient power; consistent but inconclusive at smaller samples\"。\n\n**[AGREE] R1-N2: 典型效应量 2.2pp 太小**\n与我的 R2-N1 完全一致。CI 下界 0.4pp，98.3% variance 未解释。Count effect (-42% to -56%) vs confusability typical effect (2.2pp) magnitude 差两个数量级，\"two-channel\" 对称 framing 不成立。同意改为 \"detectable but not primary driver\"。\n\n**[AGREE with nuance] R1-N3: Conditioning on non-zero pairs 引入 selection bias**\nConditional R²=7% vs unconditional r²=1.3% 的差距确实需要解释。但 Appendix I simulation 的目的是验证 aggregation math consistency，non-zero pairs 是 batch-level variance 的实际贡献者，所以 conditional R² 作为 input 有一定合理性。建议：用 unconditional r² 作为 lower bound 重新运行 simulation，明确讨论 discrepancy。\n\n### Should-Fix\n\n**[AGREE] R1-W1 (single-seed)**: 与我的 R2-W3 一致。\n**[REBUT partial] R1-W2 (embedding 不一致)**: 论文提供了 cross-check（MiniLM r=0.172 vs Qwen3 r=0.138, matrix correlation 0.894），方向一致。真正问题是 shared-representation bias，非 embedding 选择。\n**[AGREE] R1-W3 (5 batches per level)**: n=5 SD 估计不稳定。\n**[AGREE] R1-W4 (FewRel train+val merge)**: contamination p=0.06 marginal，不能排除。\n**[REBUT partial] R1-W5 (TOST ±3pp margin)**: Table 4 sensitivity analysis 显示 ±2pp 也 marginally equivalent (p=0.047)，interaction=0.47pp, 90% CI [-1.0, 2.0]pp，具体 margin 选择不 critical。但应引用 Lakens 2017。\n\n### Strengths 回应\n全部同意，特别是 S2（负面结果诚实）和 S4（Limitations 质量）。S5（跨任务一致性）部分同意——count channel 一致，confusability channel 实际上是 RE clean / NER coupled / MAVEN confounded 的不一致模式。\n\n### Questions 回应\nQ1 (unconditional simulation): 粗估 simulated batch R²≈0.039，远低于 observed 0.218。需要论文解释此 discrepancy。\nQ4 (NER frequency confound): 好问题。Few-NERD BCS-controlled 可能间接控制了 frequency。论文对 MAVEN 做了 centrality control 但未对 Few-NERD 做同样分析。\n\n### 评分差异\nR1 Overall 3.5 vs 我 3.0。差异在 Excitement（R1: 3.5, 我: 2.5）。R1 更看重方法论贡献，我更关注核心发现 novelty。3.0-3.5 差异合理，论文属 borderline Findings/Main。",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-16T16:44:35.700750+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3865
}
```

</details>

---


### Assistant

_source line 540 · 2026-05-16T16:44:41.965234+00:00_

交叉回应已提交。

总结：R1 的 3 条 Must-Fix 中我对 N2（effect size 太小）完全同意，N1（factorial selectivity）同意结论但认为 "cherry-picking" 定性偏重（更接近 power difference），N3（selection bias）同意需要补充 unconditional simulation 但 conditional R² 作为 aggregation input 有部分合理性。5 条 Should-Fix 中同意 3 条，对 embedding 不一致和 TOST margin 部分反驳。评分差异主要在 Excitement 维度——我对核心发现 novelty 的评价更低。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 17

## Round 17

34 recorded events


### User

_source line 541 · 2026-05-16T17:35:25.530479+00:00_

[Round 1 审稿请求]:
你负责**新颖性与完整性**审查。

## 论文信息
- 论文路径: `projects/schema-dag-extraction/docs/paper/main.tex`
- 目标 venue: EMNLP 2026 Main Conference
- 截止日期: 2026-05-25
- 格式: ACL 模板, 正文 8 页, double-blind
- 匿名规则: 完全匿名（作者信息、self-reference 不可暴露身份）

## 论文摘要
研究 training-free LLM IE 中 schema complexity 导致的性能下降。提出 Schema Confusability Score (SCS)，通过 count curves 和 BCS-controlled 实验分离 count-driven recall decline (Channel 1) 和 confusability-driven type substitution (Channel 2)。跨 4 个数据集 (Few-NERD, FewRel, DocRED, MAVEN) 和 2 个模型 (Qwen3-32B, Llama-3.1-8B)。发现 count 效应主导 (-49pp)，confusability 典型差距约 2.2pp；TOST 检验支持 RE 中 additive separability；NER decomposition 因 merge amplification 失败。

## 审查侧重
请重点评估以下方面：
1. **贡献新颖性**：SCS 与 LLM-PEE 使用相同形式的 pairwise cosine similarity——本文的贡献定位是否清晰？"two-channel decomposition" 是否构成足够的 conceptual contribution 还是仅为 empirical confirmation？
2. **Related work 覆盖**：是否遗漏重要相关工作？特别是 hierarchical classification 中 label confusion 的文献 (如 Deng et al. 2010, Zhou et al. 2025, Guo et al. 2021, Novack et al. 2023 CHiLS, ZERONER 2025)；"first controlled study" 声称是否准确？
3. **Framing 准确性**：Abstract/Intro 中 extreme-batch 31.2pp 与 typical 2.2pp 的比重是否恰当？Contribution #4 "decomposition" 的 framing 是否误导（NER F1 0.445→0.251, RE +1.4pp n.s.）？"cleanly separable channels" 的措辞是否被 NER coupling 和 failed factorial tests 动摇？
4. **写作质量与格式**：Abstract 数字密度是否过高？整体论证逻辑是否清晰？ACL checklist 是否完整？

请按 EMNLP 审稿标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Score (1-5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-16T17:35:32.650718+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-16T17:35:34.106248+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-16T17:35:34.106759+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 545 · 2026-05-16T17:35:34.157996+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-16T17:35:39.529199+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 547 · 2026-05-16T17:35:41.486512+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 548 · 2026-05-16T17:35:41.789287+00:00_

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
17	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
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
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\text{TOST}} = 0.003$, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontologic
…[truncated 28389 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 549 · 2026-05-16T17:35:41.789648+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 550 · 2026-05-16T17:35:46.158276+00:00_

Web search results for query: "EMNLP 2026 reviewer guidelines review form criteria"

Links: [{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"}]

I found information about EMNLP 2026 reviewer guidelines and review form criteria. Here's what I discovered:

## EMNLP 2026 Uses ACL Rolling Review (ARR)

EMNLP 2026 uses ACL Rolling Review (ARR) as a reviewing system, with final decisions made by the conference.

## Reviewer Guidelines and Requirements

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform reviews on time and in line with ARR requirements.

If reviewers feel qualified to review some aspects of the paper but not others, they should state in the review if they did not check some major parts, such as proofs, as this information is helpful for the Area Chair.

## Review Form Evaluati
…[truncated 727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6629
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-16T17:36:35.078104+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 53, \"total_citations\": 78, \"unique_cited_keys\": 53, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 41, \"online_not_found\": 5, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"llm-pee-2025\", \"type\": \"inproceedings\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"authors\": \"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"parse-2025\", \"type\": \"article\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"authors\": \"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.08623\"}, {\"key\": \"dee-2024\", \"type\": \"inproceedings\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"authors\": \"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\"}, {\"key\": \"crossagentie-2025\", \"type\": \"inproceedings\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"authors\": \"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"cmas-ner-2025\", \"type\": \"inproceedings\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"auth
…[truncated 42675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 53288
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-16T17:36:41.105101+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-16T17:36:41.556863+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. We present the first controlled study isolating type confusability from type count in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets. We introduce the Schema Confusability Score (SCS) and two experimental paradigms: count curves (varying schema size while randomizing confusability) and BCS-controlled experiments (fixing size while varying confusability).
3	
4	We identify two degradation channels: count-driven recall decline and confusability-driven type substitution. In typical random batches, confusability accounts for ${\approx}\,2.2$\,pp accuracy difference---markedly smaller than count effects (up to $-$49\,pp); under quartile contrast the gap reaches $-5.3$\,pp, and batch-level BCS explains up to 53\% of cross-batch variance. The channels are consistent with additive separability in RE (TOST equivalence test, $p = 0.003$; lower-powered $2 \times 2$ designs did not reach equivalence) but coupled in NER where boundary and type ambiguity interact. Effects are directionally consistent across prompt designs and model scales, though Channel~2 attenuates on smaller models. Schema decomposition via oracle routing recovers +29.8\,pp for RE, but confusability-aware grouping yields no significant improvement over random grouping (+1.4\,pp, $p \approx 0.19$, n.s.).
5	\end{abstract}
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-16T17:36:41.557236+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-16T17:36:42.612684+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	We present the first controlled study isolating type confusa
…[truncated 2729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-16T17:36:42.763642+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-16T17:36:42.764136+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting \cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms. Concurrently, \citet{haystack-to-needle-2025} redu
…[truncated 2350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-16T17:36:43.015149+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-16T17:36:43.517257+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\
…[truncated 7345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-16T17:36:43.517701+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-16T17:36:44.621946+00:00_

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
20	\caption{\textbf{(a)} Count-degradation curves across three tasks. Error bars show $\pm 1$\,SD across 5 random type batches per count level (omitted at count${}\,=\,1$ where each type is evaluated individually). NER recall and RE accuracy decline monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\%), FewRel accuracy from 85.7\% to 50.4\% ($-$35.3\,pp), and DocRED from 88.0\% to 38.7\% ($-$56\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty. Count curves (5 batches per level) establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments
…[truncated 9469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-16T17:36:44.722783+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-16T17:36:44.924037+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an adopted abbreviation for schema decomposition and grouping; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.
5	
6	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\,=\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\ref{tab:sdgd_results}, Appendix~\ref{sec:appendix_sdgd}).
7	
8	\paragraph{Merge amplification in NER.}
9	The core failure mechanism is \emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calib
…[truncated 4344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-16T17:36:44.974797+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-16T17:36:45.478095+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN) exhibit centrality confounding requiring pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across models, suggesting a task-inherent difficulty ceiling. RE's clean separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}). Cross-scale evidence (32B vs.\ 8B) shows Channel~2 attenuates on smaller models while Channel~1 replicates fully (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}).
6	
7	\paragraph{Prompt length as mechanism.}
8	Count-driven degradation may partly reflect prompt length: per-type recall (0.586) substantially exceeds single-pass (0.368), consistent with lost-in-middle effects \cite{lost-in-middle-2024}. Disentangling count from length requires fixed-count variable-length experiments.
9	
10	\paragraph{Why does embedding similarity predict LLM confusion?}
11	SCS captures semantic proximity in the representational space LLMs use for type resolution; high overlap causes substitution errors. The unconditional pair-level effect is modest ($r^2 = 1.3$--$1.7\%$), as ${\sim}89\%$ of pairs never produce mutual confusion; among the active-confusion subset, $R^2 \approx 7\%$ amplifies ${\sim}3\times$ at the batch level through inter-pair correlation (Appendix~\ref{app:aggregation-sim}), yielding batch-level $R^2$ of 22--53\%---sufficient for pre-hoc schema screening.
12	
13	\paragraph{Schema design implications.}
14	Typical confusability effects (2.2\,pp) are an order of magnitude smaller than count effects ($-$42\% to $-$56\%), so count reduction should be the first-line mitigation. For residual confusability, we sugg
…[truncated 877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-16T17:36:45.528799+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-16T17:36:46.533020+00:00_

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
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}, vLLM \cite{vllm-2023}, and all-Mini
…[truncated 4435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-16T17:36:47.788177+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their descriptions, and the scoring scale (1-5 or whatever scale is used). I need the exact names of each dimension and what each score level means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their descriptions, and the scoring scale (1-5 or whatever scale is used). I need the exact names of each dimension and what each score level means."
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-16T17:36:54.413624+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with half-point options: 4.5, 3.5, 2.5, 1.5)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all claims"
- **3**: "Acceptable: This study provides sufficient support for main claims"
- **2**: "Poor: Some main claims not sufficiently supported"
- **1**: "Major Issues: Not sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with half-point options)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points"
- **2**: "Potentially Interesting: does not resonate with me"
- **1**: "Not Exciting: does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with half-point options)
- **5**: Consider for Award
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce with some difficulty"
- **2**: "They would be hard pressed to reproduce"
- **1**: "They would not be able to reproduce"

## 6. **Datasets**
Scale: 1-5
- **5**: Enabling
- **4**: Useful
- **3**: Potentially useful
- **2**: Documentary
- **1**: 
…[truncated 414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6625
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-16T17:38:29.881167+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, how to assess novelty, soundness, significance, and any specific instructions about empirical papers, negative results, or framing standards."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, how to assess novelty, soundness, significance, and any specific instructions about empirical papers, negative results, or framing standards."
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-16T17:38:41.036346+00:00_

# ARR Reviewer Guidelines: Core Evaluation Framework

## What Reviewers Should Evaluate

ARR reviewers assess papers across three primary dimensions:

**Soundness**: Technical correctness and methodological rigor. Reviews must justify soundness scores with specific evidence from the paper text. Low scores require detailed explanation of identified flaws.

**Excitement**: Personal interest and relevance to the reviewer's work. This subjective dimension is separate from soundness assessment and need not include explicit justification.

**Overall Recommendation**: A composite judgment reflecting soundness, excitement, novelty, and potential impact—balancing technical quality with significance for the field.

## Assessing Novelty

The guidelines reject several problematic approaches to novelty evaluation:

- Findings that "seem obvious in retrospect" may still represent genuine contributions the community hasn't yet validated empirically
- Absence of precedent in literature doesn't disqualify work; novel contributions are often harder to publish
- Contribution type matters: reproductions, reimplementations, and analyses are in-scope and deserve fair evaluation
- Missing citations to prior work only constitute weaknesses if that work was published 3+ months before submission

## Soundness Standards

Sound papers demonstrate:

- Clear statement of assumptions and complete proofs (when applicable)
- Sufficient methodological detail for reproducibility
- Appropriate statistical significance assessment with confidence intervals or error bars
- Fair baseline comparisons with properly-tuned systems
- Honest representation of related work without misattribution

Papers with acknowledged limitations aren't automatically weak; limitations require separate justification as weaknesses.

## Significance Beyond SOTA

"State-of-the-art results neither necessary nor sufficient for scientific contribution." Reviewers should recognize value in:

- Efficiency improvements
- Interpretabili
…[truncated 1745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 11155
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-16T17:41:28.565879+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：新颖性与完整性审查\n\n### 总体评分\n**Overall**: 3 / 5 (Findings acceptance)\n**一句话总结**: 实验设计严谨、统计方法规范的经验性研究，但核心发现（count 主导、confusability 次要）符合直觉预期，SCS 指标与先前工作形式等价，\"two-channel decomposition\" 的概念贡献有限，practical implications 受限于极小的效应量和 decomposition 失败。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计方法论扎实；但 separability 声称仅在一种检验设计下成立，NER coupling 和 factorial 检验失败削弱了核心 claim |\n| Excitement | 2.5/5 | 研究问题有实际意义，但主要发现确认直觉，SCS 缺乏新颖性，实际效应量小（typical 2.2pp），decomposition 负面结果有价值但限制了影响力 |\n| Reproducibility | 4/5 | 实验细节充分，prompt 模板在 appendix 提供，代码承诺 acceptance 后释放 |\n| Confidence | 4/5 | 仔细检查了实验设计、统计方法和 framing |\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] SCS 与 LLM-PEE 形式等价，conceptual contribution 定位不清\n- 具体位置：§2 \"SCS novelty\" 段 + §1 Contribution #2\n- 问题：论文在 §2 坦承 SCS 与 LLM-PEE 的 pairwise cosine similarity 形式等价，但 Contribution #2 仍将 \"Pairwise confusability as predictor\" 列为独立贡献项，暗示 SCS 本身具有新颖性。BCS 只是 SCS 的算术均值聚合。\n- 为什么影响接收：如果核心 metric 与已有工作等价，论文必须清楚论证实验发现本身为何构成足够的 empirical contribution。当前 framing 在 \"metric novelty\" 和 \"framework novelty\" 之间摇摆不定。\n- 建议：将 SCS/BCS 降格为 experimental operationalization；Contribution #2 重新聚焦为实验设计层面的贡献。\n\n**N2** [critical] \"Two-channel decomposition\" 的 conceptual contribution 深度不足\n- 具体位置：§1 Contribution #1, §4.4, §6\n- 问题：两个 channel——count↑ recall↓、similar types → confusion——都是高度直觉化的观察。Deng et al. (2010)、Guo et al. (2021)、Zhou et al. (2025) 已在其他领域展示了类似机制。核心发现 \"count matters much more than confusability\"（typical 2.2pp vs -49pp）基本确认了已知直觉。\n- 为什么影响接收：purely confirmatory empirical work 通常需要更强的 surprising findings 或 practical implications 来支撑 EMNLP main conference。\n- 建议：将 surprising findings（merge amplification、centrality confound、NER coupling）提升为核心 contribution，将 \"two-channel\" 降级为 organizational framework。\n\n**N3** [critical] Contribution #4 (\"decomposition\") 的 framing 有误导性\n- 具体位置：§1 Contribution #4, §5, Table 5\n- 问题：NER decomposition 灾难性失败（F1 0.445→0.251）；RE confusability-aware grouping 无显著改善（+1.4pp, p≈0.19, rank 13/15）；Oracle routing +29.8pp 需 gold labels。将三个负面/不可实现的结果包装为 \"contribution\" 是过度 framing。\n- 建议：明确定位为 negative findings，讨论 merge amplification 是否是 truly novel finding。\n\n### Should-Fix 问题\n\n**W1** \"Cleanly separable channels\" 措辞与证据不一致\n- §4.4, §1 Contribution #1\n- 三个检验中只有一个（full-range regression TOST p=0.003）通过，2×2 factorial 和 Few-NERD factorial 均未达到 separability。\"Cleanly\" 是过强措辞。\n\n**W2** Abstract/Intro 中极端值与典型值的比重失衡\n- Introduction 用大量极端条件数字渲染降级严重性，但 typical BCS effect（2.2pp）在 intro 中未出现，读者在 intro 阶段会形成 \"confusability effect 很大\" 的错误印象。\n\n**W3** 效应量解释的 internal tension\n- pairwise r²=1.3-1.7% 到 batch-level R²=22-53% 的放大依赖于只看 \"active confusion pairs\"。但如果需要先知道哪些 pair 是 active 才能得到有意义的 R²，SCS 的 pre-hoc 价值受限。\n\n**W4** \"First controlled study\" 声称需要更精确的 scoping\n- 依赖于将 scope 限定得足够窄。建议改为 \"to our knowledge\" 并 acknowledge 先前工作在其他领域的 methodological precedent。\n\n**W5** 单模型为主、单种子评估的 generalizability 限制\n- Channel 2 在 8B NER 上由于 floor effects 未能复现，应从 Limitations 提升到 main text discussion。\n\n### 小问题\n- Abstract 数字密度偏高，建议精简至 3-4 个核心数字\n- §2 引用 behavioral science standards (Cohen 1988) 论证 r²=1.3-1.7% 不能直接迁移到 NLP feature engineering\n- \"training-free\" vs \"zero-shot\" 术语使用不够精确\n- 引用核查：53 条 bib entries 全部真实，无伪造引用\n\n### 主要优势\n- 实验设计的严谨性：双范式设计 + within-pool analysis + permutation test\n- 统计方法远超 NLP 论文平均水平：TOST、cluster bootstrap、aggregation simulation\n- Centrality confound 分析（§4.5）是 genuinely novel observation\n- Merge amplification 的系统诊断有信息量\n- Negative results 的诚实报告\n- 跨 4 个数据集、3 个 IE 任务的覆盖\n\n### Questions to Authors\n1. Typical 2.2pp gap 在实际 schema design 中如何 actionably 使用？\n2. Oracle routing +29.8pp 在无 gold labels 的 realistic 设置中是否有 pilot 结果？\n3. MiniLM 预测力强于 Qwen3 embeddings（r=0.172 vs 0.138），是否暗示外部 embedding 是更好的 confusability proxy？",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见：新颖性与完整性审查\n\n### 总体评分\n**Overall**: 3 / 5 (Findings acceptance)\n**一句话总结**: 实验设计严谨、统计方法规范的经验性研究，但核心发现（count 主导、confusability 次要）符合直觉预期，SCS 指标与先前工作形式等价，\"two-channel decomposition\" 的概念贡献有限，practical implications 受限于极小的效应量和 decomposition 失败。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计方法论扎实；但 separability 声称仅在一种检验设计下成立，NER coupling 和 factorial 检验失败削弱了核心 claim |\n| Excitement | 2.5/5 | 研究问题有实际意义，但主要发现确认直觉，SCS 缺乏新颖性，实际效应量小（typical 2.2pp），decomposition 负面结果有价值但限制了影响力 |\n| Reproducibility | 4/5 | 实验细节充分，prompt 模板在 appendix 提供，代码承诺 acceptance 后释放 |\n| Confidence | 4/5 | 仔细检查了实验设计、统计方法和 framing |\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] SCS 与 LLM-PEE 形式等价，conceptual contribution 定位不清\n- 具体位置：§2 \"SCS novelty\" 段 + §1 Contribution #2\n- 问题：论文在 §2 坦承 SCS 与 LLM-PEE 的 pairwise cosine similarity 形式等价，但 Contribution #2 仍将 \"Pairwise confusability as predictor\" 列为独立贡献项，暗示 SCS 本身具有新颖性。BCS 只是 SCS 的算术均值聚合。\n- 为什么影响接收：如果核心 metric 与已有工作等价，论文必须清楚论证实验发现本身为何构成足够的 empirical contribution。当前 framing 在 \"metric novelty\" 和 \"framework novelty\" 之间摇摆不定。\n- 建议：将 SCS/BCS 降格为 experimental operationalization；Contribution #2 重新聚焦为实验设计层面的贡献。\n\n**N2** [critical] \"Two-channel decomposition\" 的 conceptual contribution 深度不足\n- 具体位置：§1 Contribution #1, §4.4, §6\n- 问题：两个 channel——count↑ recall↓、similar types → confusion——都是高度直觉化的观察。Deng et al. (2010)、Guo et al. (2021)、Zhou et al. (2025) 已在其他领域展示了类似机制。核心发现 \"count matters much more than confusability\"（typical 2.2pp vs -49pp）基本确认了已知直觉。\n- 为什么影响接收：purely confirmatory empirical work 通常需要更强的 surprising findings 或 practical implications 来支撑 EMNLP main conference。\n- 建议：将 surprising findings（merge amplification、centrality confound、NER coupling）提升为核心 contribution，将 \"two-channel\" 降级为 organizational framework。\n\n**N3** [critical] Contribution #4 (\"decomposition\") 的 framing 有误导性\n- 具体位置：§1 Contribution #4, §5, Table 5\n- 问题：NER decomposition 灾难性失败（F1 0.445→0.251）；RE confusability-aware grouping 无显著改善（+1.4pp, p≈0.19, rank 13/15）；Oracle routing +29.8pp 需 gold labels。将三个负面/不可实现的结果包装为 \"contribution\" 是过度 framing。\n- 建议：明确定位为 negative findings，讨论 merge amplification 是否是 truly novel finding。\n\n### Should-Fix 问题\n\n**W1** \"Cleanly separable channels\" 措辞与证据不一致\n- §4.4, §1 Contribution #1\n- 三个检验中只有一个（full-range regression TOST p=0.003）通过，2×2 factorial 和 Few-NERD factorial 均未达到 separability。\"Cleanly\" 是过强措辞。\n\n**W2** Abstract/Intro 中极端值与典型值的比重失衡\n- Introduction 用大量极端条件数字渲染降级严重性，但 typical BCS effect（2.2pp）在 intro 中未出现，读者在 intro 阶段会形成 \"confusability effect 很大\" 的错误印象。\n\n**W3** 效应量解释的 internal tension\n- pairwise r²=1.3-1.7% 到 batch-level R²=22-53% 的放大依赖于只看 \"active confusion pairs\"。但如果需要先知道哪些 pair 是 active 才能得到有意义的 R²，SCS 的 pre-hoc 价值受限。\n\n**W4** \"First controlled study\" 声称需要更精确的 scoping\n- 依赖于将 scope 限定得足够窄。建议改为 \"to our knowledge\" 并 acknowledge 先前工作在其他领域的 methodological precedent。\n\n**W5** 单模型为主、单种子评估的 generalizability 限制\n- Channel 2 在 8B NER 上由于 floor effects 未能复现，应从 Limitations 提升到 main text discussion。\n\n### 小问题\n- Abstract 数字密度偏高，建议精简至 3-4 个核心数字\n- §2 引用 behavioral science standards (Cohen 1988) 论证 r²=1.3-1.7% 不能直接迁移到 NLP feature engineering\n- \"training-free\" vs \"zero-shot\" 术语使用不够精确\n- 引用核查：53 条 bib entries 全部真实，无伪造引用\n\n### 主要优势\n- 实验设计的严谨性：双范式设计 + within-pool analysis + permutation test\n- 统计方法远超 NLP 论文平均水平：TOST、cluster bootstrap、aggregation simulation\n- Centrality confound 分析（§4.5）是 genuinely novel observation\n- Merge amplification 的系统诊断有信息量\n- Negative results 的诚实报告\n- 跨 4 个数据集、3 个 IE 任务的覆盖\n\n### Questions to Authors\n1. Typical 2.2pp gap 在实际 schema design 中如何 actionably 使用？\n2. Oracle routing +29.8pp 在无 gold labels 的 realistic 设置中是否有 pilot 结果？\n3. MiniLM 预测力强于 Qwen3 embeddings（r=0.172 vs 0.138），是否暗示外部 embedding 是更好的 confusability proxy？",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-16T17:41:32.183227+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3617
}
```

</details>

---


### Assistant

_source line 574 · 2026-05-16T17:41:38.563065+00:00_

审稿意见已提交给 Review Director。

总结：本文是一篇实验设计严谨的经验性研究（统计方法尤其出色），但存在三个核心问题：(1) SCS 与 LLM-PEE 形式等价，贡献定位不清；(2) "two-channel decomposition" 主要确认直觉而非提供 surprising insights；(3) decomposition 实验全面失败却被 framed 为 positive contribution。建议定位为 Findings 而非 Main Conference。最值得保留的发现是 centrality confound 分析和 merge amplification 的系统诊断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 18

## Round 18

4 recorded events


### User

_source line 575 · 2026-05-16T17:42:16.432303+00:00_

[Round 1 审稿请求]:
## 交叉分享：以下是 Reviewer 1 的完整审稿意见

请逐条回应其 Must-Fix 和 Should-Fix ��题：对每条用 [AGREE] 同意并��明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

**Reviewer 1 Overall**: 3.0/5 (Findings acceptance)

### Must-Fix 问题

**N1** [critical] TOST equivalence margin (±3pp) 的合理性论证存在逻辑缺陷
- 论文用 prompt variation 引起的 ~25pp accuracy shift 作为 TOST margin 的锚点，但 prompt variation 是完全不同的变异来源。
- 关键问题：典型 confusability 效应本身仅 2.2pp，而 TOST margin 设为 ±3pp——equivalence test 实质上只在说 "interaction 小于 main effect 本身"。
- Sensitivity analysis 显示 ±2pp 时 p=0.047（borderline），±1pp 时 p=0.278（失败）。
- 建议弱化 "additive separability" 为 "interaction bounded below 2pp"。

**N2** [critical] Pair-level r²=1.3-1.7% 到 batch-level R²=22% 的聚合存在 conditioning bias
- Simulation 使用 conditional R²=7.4%（仅限 non-zero confusion pairs），论文自己承认 "conditioning on the dependent variable may inflate this"。
- 使用 unconditional r²=1.3% 时，模拟的 batch R² 仅 ~0.01——远低于观测值 0.218。
- 这是 circular reasoning：先筛选有 confusion 的 pairs，发现更高的 R²，再用这个 R² 去解释 batch-level 观测。

**N3** [critical] Single-seed evaluation 对核心 claims 的影响被低估
- vLLM FP8 量化推理可能有非确定性。
- Count curve 每 level 仅 5 batches，bootstrap CIs 不捕获 "如果抽另外 5 个 batches" 的方差。
- 1,000 evaluation instances 是 sampled 的，CIs 不覆盖不同 sample 的方差。

### Should-Fix 问题

**W1** FewRel train+val 合并的 contamination 风险
- p=0.06 非常接近显著；non-uniform contamination 未排除；DocRED (2019) 的 contamination 风险并非 trivially lower。

**W2** Channel 2 效应量在 typical 场景下极小，但 framing 偏重 extreme cases
- 在最现实场景（全 80 relations），自然 BCS 变异不足以检测效应 (p=0.76)。BCS 作为 "pre-hoc screening tool" 价值存疑。

**W3** NER text matching 可能混淆 boundary errors 与 type errors

**W4** MAVEN 反向结果削弱 generalizability
- 4 个数据集中 1 个完全相反，two-channel framework 在 same-domain schemas 上不 applicable。

**W5** Few-NERD 使用 extraction model 自身 embedding 的 shared-representation bias

---

请对以上每条给出 [AGREE] 或 [REBUT] 回应，引用论文具体内容支持你的判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-16T17:45:01.587045+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n### Must-Fix\n\n**[AGREE] R1-N1: TOST margin 逻辑缺陷** — 同意。用 prompt variation (~25pp) 锚定 TOST margin 不合逻辑，且 ±3pp > typical confusability main effect 2.2pp。但 sensitivity analysis (Table 9) 显示 interaction bounded below ~2pp (p=0.047)，data 本身不误，问题是 \"additive separability\" 措辞过强。与我的 W1 一致。\n\n**[AGREE with qualification] R1-N2: Conditioning bias** — conditioning on non-zero confusion pairs 确实有 bias，但 \"circular reasoning\" 定性过强。关键区别：batch-level R²=0.218 是直接观测（Table 6），不依赖 simulation。Simulation 是 explanatory model，非 evidence base。建议标注 Appendix F 为 illustrative model。\n\n**[REBUT] R1-N3: Single-seed evaluation** — (1) FP8 greedy decoding 的 non-determinism 在 argmax 层面极小，R1 未提供实际变异证据；(2) 5 batches/level 仅用于 trend direction，magnitude estimation 依赖 n=25-100 的 BCS-controlled experiments (§4.1)；(3) 跨 4 个数据集的 directional consistency 比单数据集 multi-seed 提供更强 robustness。降为 Should-Fix 更恰当。\n\n### Should-Fix\n\n**[AGREE] R1-W1** — p=0.06 不构成 strong evidence against contamination。\n**[AGREE] R1-W2** — 完全同意，与我的 W3 本质相同。Full 80-rel condition p=0.76 直接削弱 pre-hoc screening 声称。\n**[AGREE] R1-W3** — NER Missed 类别未分离 boundary error，影响 Channel 1 magnitude estimation。\n**[REBUT] R1-W4** — MAVEN 的 centrality confound 是 genuinely novel finding（§4.5, Appendix D partial correlation 控制后 p>0.2），pairwise SCS signal 仍显著 (r=0.129, p<0.001)。问题在 aggregation method 不在 framework。\n**[REBUT] R1-W5** — MiniLM cross-check 给出更强的 r (0.172 vs 0.138)，shared-representation bias 方向是 conservative。\n\n### 与我自己审稿意见的交集\nR1 和我在以下核心判断上一致：(1) typical effect size 过小限制 practical value；(2) separability/additive 声称 framing 过强；(3) overall 3/5 Findings 档位。主要分歧在 MAVEN 解读和 single-seed 严重程度上。",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n### Must-Fix\n\n**[AGREE] R1-N1: TOST margin 逻辑缺陷** — 同意。用 prompt variation (~25pp) 锚定 TOST margin 不合逻辑，且 ±3pp > typical confusability main effect 2.2pp。但 sensitivity analysis (Table 9) 显示 interaction bounded below ~2pp (p=0.047)，data 本身不误，问题是 \"additive separability\" 措辞过强。与我的 W1 一致。\n\n**[AGREE with qualification] R1-N2: Conditioning bias** — conditioning on non-zero confusion pairs 确实有 bias，但 \"circular reasoning\" 定性过强。关键区别：batch-level R²=0.218 是直接观测（Table 6），不依赖 simulation。Simulation 是 explanatory model，非 evidence base。建议标注 Appendix F 为 illustrative model。\n\n**[REBUT] R1-N3: Single-seed evaluation** — (1) FP8 greedy decoding 的 non-determinism 在 argmax 层面极小，R1 未提供实际变异证据；(2) 5 batches/level 仅用于 trend direction，magnitude estimation 依赖 n=25-100 的 BCS-controlled experiments (§4.1)；(3) 跨 4 个数据集的 directional consistency 比单数据集 multi-seed 提供更强 robustness。降为 Should-Fix 更恰当。\n\n### Should-Fix\n\n**[AGREE] R1-W1** — p=0.06 不构成 strong evidence against contamination。\n**[AGREE] R1-W2** — 完全同意，与我的 W3 本质相同。Full 80-rel condition p=0.76 直接削弱 pre-hoc screening 声称。\n**[AGREE] R1-W3** — NER Missed 类别未分离 boundary error，影响 Channel 1 magnitude estimation。\n**[REBUT] R1-W4** — MAVEN 的 centrality confound 是 genuinely novel finding（§4.5, Appendix D partial correlation 控制后 p>0.2），pairwise SCS signal 仍显著 (r=0.129, p<0.001)。问题在 aggregation method 不在 framework。\n**[REBUT] R1-W5** — MiniLM cross-check 给出更强的 r (0.172 vs 0.138)，shared-representation bias 方向是 conservative。\n\n### 与我自己审稿意见的交集\nR1 和我在以下核心判断上一致：(1) typical effect size 过小限制 practical value；(2) separability/additive 声称 framing 过强；(3) overall 3/5 Findings 档位。主要分歧在 MAVEN 解读和 single-seed 严重程度上。",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-16T17:45:05.781055+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4194
}
```

</details>

---


### Assistant

_source line 578 · 2026-05-16T17:45:09.740878+00:00_

交叉回应已提交。总结：对 R1 的 7 条意见中 AGREE 4 条（N1、W1、W2、W3）、AGREE with qualification 1 条（N2）、REBUT 2 条（N3、W4+W5）。我和 R1 在核心判断上高度一致——overall 3/5、typical effect size 限制 practical value、separability 声称 framing 过强。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 19

## Round 19

60 recorded events


### User

_source line 579 · 2026-05-17T07:34:29.971354+00:00_

[Round 10 审稿请求]:
## Round 10 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 贡献清晰度 + 写作质量 + 格式合规**

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
- **Deadline**: 2026-05-25
- **页数限制**: 8 页正文 + unlimited references; Limitations 不计页数
- **模板**: ACL style template, `\usepackage[review]{acl}`
- **匿名**: Double-blind

### 论文路径
- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`
- 补充材料: `projects/schema-dag-extraction/docs/paper/supplementary.tex`
- 各 section 文件: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`

### 审查重点

1. **新颖性评估**：
   - SCS/BCS 与 LLM-PEE 的 embedding similarity 形式相同——本文的增量贡献在哪里？
   - "Count dominates confusability by ~20×" 这个发现是否 non-obvious？
   - Two-channel decomposition 是否属于 EMNLP Main Conference 级别的贡献？
   - 负面结果（SDGD failure, routing failure）的贡献价值

2. **贡献清晰度**：
   - 4 条 Contributions 的表述是否清晰、准确、可验证
   - Abstract 和 Introduction 是否有效传达核心信息（30 秒审稿人测试）
   - 叙事主线是否一致：Abstract → Introduction → Method → Results → Discussion → Conclusion

3. **Related Work 定位**：
   - 与 LLM-PEE、UniNER、PARSE 等直接竞争者的区分是否充分
   - 引用覆盖度：是否遗漏重要相关工作（2024-2026 年 LLM IE 领域）
   - 自身定位：empirical confirmation paper vs. methodological contribution

4. **写作质量**：
   - AI 写作痕迹检查：em-dash (—)、-ing phrases、过度分段、transition word 堆砌
   - 专有名词首次出现是否有定义（SCS, BCS, SDGD, Channel 1/2）
   - 数字密度是否合理（Abstract 特别注意）
   - Figure/Table 信息密度和 caption 自包含性

5. **格式合规**：
   - 页数限制（8 页正文）
   - Limitations section 存在且不计入页数
   - Responsible NLP Research Checklist 是否完整
   - 匿名化：是否有泄露作者身份的信息
   - 引用格式一致性

请给出完整审稿意见，包含 Strengths, Weaknesses, Questions, Missing References, 和 Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-17T07:34:38.745940+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 581 · 2026-05-17T07:34:38.798034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-17T07:34:42.977599+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 583 · 2026-05-17T07:34:44.383457+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 584 · 2026-05-17T07:34:44.384028+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 585 · 2026-05-17T07:34:45.539997+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-17T07:34:45.841821+00:00_

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
17	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
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
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded interaction ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy
…[truncated 35271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-17T07:34:50.813103+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's information about ACL ARR reviewer guidelines, review form criteria, and scoring for 2025-2026:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the t
…[truncated 1477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7835
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-17T07:34:57.543558+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, scoring scales, and dimensions. Include all numbered scores and their descriptions for soundness, excitement/novelty, overall recommendation, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, scoring scales, and dimensions. Include all numbered scores and their descriptions for soundness, excitement/novelty, overall recommendation, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 589 · 2026-05-17T07:34:59.401185+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 590 · 2026-05-17T07:34:59.602271+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. To our knowledge, we present the first controlled study isolating type confusability from type count in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets. We introduce the Schema Confusability Score (SCS) and two experimental paradigms: count curves (varying schema size while randomizing confusability) and BCS-controlled experiments (fixing size while varying confusability).
3	
4	We identify two degradation channels: count-driven recall decline and confusability-driven type substitution. In typical random batches, confusability accounts for ${\approx}\,2.2$\,pp accuracy difference---markedly smaller than count effects ($-$49\,pp for document-level RE)---while batch-level BCS explains 22--53\% of cross-batch variance. The channels exhibit bounded interaction in RE (TOST $p = 0.003$ at $\pm 3$\,pp) but are coupled in NER where boundary and type ambiguity interact. Effects are directionally consistent across prompt designs and model scales, though Channel~2 attenuates on smaller models. Schema decomposition via oracle routing recovers substantial RE gains, but confusability-aware grouping yields no significant improvement over random.
5	\end{abstract}
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 591 · 2026-05-17T07:34:59.602627+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 592 · 2026-05-17T07:34:59.653136+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what 
…[truncated 3588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-17T07:35:04.370625+00:00_

# ACL Rolling Review Form: Evaluation Criteria

## Soundness Scale (1-5)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement/Novelty Scale (1-5)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make effort to attend."
- **3**: "Interesting: I might mention some points or attend if there's time."
- **2**: "Potentially Interesting: does not resonate with me, but might with others."
- **1**: "Not Exciting: does not resonate with me, and I don't think it would with others."

## Overall Assessment Scale (1-5)
- **5**: "Consider for Award: could be considered for outstanding paper award (top 2.5%)."
- **4**: "Conference: could be accepted to an ACL conference."
- **3**: "Findings: could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: needs substantial revisions."
- **1**: "Do not resubmit: has to be fully redone."

## Reviewer Confidence Scale (1-5)
- **5**: "Positive that my evaluation is correct; very familiar with related work."
- **4**: "Quite sure; unlikely to have missed something affecting ratings."
- **3**: "Pretty sure; chance I missed details or didn't check thoroughly."
- **2**: "Willing to defend; fairly likely I missed details or misunderstood points."
- **1**: "Not my area; evaluation is educated guess."

## Additional Dimensions
- **Reproducibility**: 1-5 scale assessing whether readers can reproduce results
- **Datasets Value**: 1-5 scale for released dataset utility
- **Software Value**: 1-5 scale for released software utility
- **Author Anonym
…[truncated 56 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6827
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-17T07:35:07.733159+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-17T07:35:08.185239+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Specifically, LLM-PEE employs union merge across sub-schema extractions, which our \S\ref{sec:sdgd} analysis shows causes precision to collapse from 0.56 to 0.21 in NER as false positives accumulate across passes; RE avoids this because closed-set classification does not require span reconciliation, explaining why LLM-PEE's decomposition succeeds for relation/event tasks but faces unresolved merge challenges on span-level extraction. Other approaches addre
…[truncated 2788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-17T07:35:08.185600+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-17T07:35:08.587470+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\
…[truncated 7383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-17T07:35:08.588032+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-17T07:35:08.638753+00:00_

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
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schem
…[truncated 10306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-17T07:35:14.109025+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-17T07:35:14.561108+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an adopted abbreviation for schema decomposition and grouping; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.
5	
6	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\,=\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\ref{tab:sdgd_results}, Appendix~\ref{sec:appendix_sdgd}).
7	
8	\paragraph{Merge amplification in NER.}
9	The core failure mechanism is \emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calib
…[truncated 5593 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-17T07:35:14.712113+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-17T07:35:14.813003+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across models, suggesting a difficulty ceiling. RE's separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}). Cross-scale evidence (32B vs.\ 8B) shows Channel~1 replicates fully while Channel~2 attenuates on smaller models, dropping to near-zero $R^2$ for NER on Llama-3.1-8B (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}). Count-driven degradation may partly reflect prompt length (per-type recall 0.586 vs.\ single-pass 0.368, consistent with lost-in-middle effects; \citealt{lost-in-middle-2024}).
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pair-level effect is modest ($r^2 = 1.3$--$1.7\%$, as ${\sim}89\%$ of pairs never produce mutual confusion); among active-confusion pairs, $R^2 \approx 7\%$ amplifies ${\sim}3\times$ at batch level (Appendix~\ref{app:aggregation-sim}), yielding $R^2$ of 22--53\%. The NER U-shape (\S\ref{sec:count_curves}) reflects a dual-task burden absent in RE: partial schemas require simultaneous span detection and type-membership filtering; at full-schema, filtering becomes vacuous and recall recovers, confirming task-specific mechanistic pathways.
9	
10	\section{Conclusion}
11	\label{sec:conclusion}
12	
13	Schema-induced degradation in training-free LLM extraction operates through two channels (count-driven recall decline, confusability-driven type confusion) with bounded interaction in RE but coupling in NER. Channel~1 replicates across scales; Channel~2 attenuates on s
…[truncated 49 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-17T07:35:14.863700+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-17T07:35:15.115447+00:00_

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
17	\title{Supplementary Material for: Schema-Induced Degradation\\in Training-Free LLM Information Extraction}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\appendix
25	
26	\section{Additional Figures}
27	\label{sec:appendix_figures}
28	
29	\begin{table}[h]
30	\centering
31	\small
32	\begin{tabular}{lrr}
33	\toprule
34	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
35	\midrule
36	1 & 0.702 & 0.640 \\
37	64 & 0.273 & 0.304 \\
38	\midrule
39	Decline & $-$43\,pp & $-$34\,pp \\
40	\bottomrule
41	\end{tabular}
42	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
43	\label{tab:cross_model}
44	\end{table}
45	
46	\begin{table}[h]
47	\centering
48	\small
49	\resizebox{\columnwidth}{!}{%
50	\begin{tabular}{crrrrrr}
51	\toprule
52	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
53	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
54	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
55	\midrule
56	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
57	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
58	\bottomrule
59	\end{tabular}}
60	\caption{Cross-model BCS-controlled FewRel accuracy. 
…[truncated 33287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-17T07:35:21.839162+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-17T07:35:22.291192+00:00_

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
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
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
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}, vLLM \cite{vllm-2023}, and a
…[truncated 4442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-17T07:35:22.743171+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "count"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-17T07:35:22.894209+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex:1

Found 1 total occurrence across 1 file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-17T07:35:23.496656+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "count"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-17T07:35:23.547345+00:00_

No matches found

Found 0 total occurrences across 0 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-17T07:35:28.619005+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-17T07:35:29.070971+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:15:Our centrality confound (\S\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \cite{cai-isotropy-clusters-2021}---explaining why MAVEN's single-ontology types conflate confusability with centrality.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:113:NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:116:NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:117:RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:127:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:177:Single-pass (no decomposition) & 50.4\% & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:225:\item \textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types tha
…[truncated 3969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-17T07:35:29.472760+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "head_limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "head_limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-17T07:35:29.523526+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:222:For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:304:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:400:\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\Delta r$ indicates no systematic benefit from including definitions.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex:75:Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex:111:Yes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex:13:Schema-induced degradation in training-free LLM extrac
…[truncated 3234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-17T07:35:37.354476+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "project": "schema-dag-extraction",
  "skip_online": "False"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "project": "schema-dag-extraction",
    "skip_online": "False"
  }
}
```

</details>

---


### Tool call

_source line 617 · 2026-05-17T07:35:37.555339+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-17T07:36:33.318652+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 53, \"total_citations\": 76, \"unique_cited_keys\": 52, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 41, \"online_not_found\": 5, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [\"lakens-2017-equivalence\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"llm-pee-2025\", \"type\": \"inproceedings\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"authors\": \"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"parse-2025\", \"type\": \"article\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"authors\": \"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.08623\"}, {\"key\": \"dee-2024\", \"type\": \"inproceedings\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"authors\": \"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\"}, {\"key\": \"crossagentie-2025\", \"type\": \"inproceedings\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"authors\": \"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"cmas-ner-2025\", \"type\": \"inproceedings\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named E
…[truncated 42497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 55964
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-17T07:36:33.321121+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 55765
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-17T07:36:39.494352+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1-4",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "1-4",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 621 · 2026-05-17T07:36:40.349755+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf 2>/dev/null | grep -i \"pages\"",
  "description": "Get PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf 2>/dev/null | grep -i \"pages\"",
    "description": "Get PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 622 · 2026-05-17T07:36:40.962995+00:00_

Error: result (2,848,987 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/add20d08-e3f3-434f-9d96-5ab81c489ce4/tool-results/mcp-agent-ml-research-pdf_to_images-1779003400767.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/add20d08-e3f3-434f-9d96-5ab81c489ce4/tool-results/mcp-agent-ml-research-pdf_to_images-1779003400767.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/add20d08-e3f3-434f-9d96-5ab81c489ce4/tool-results/mcp-agent-ml-research-pdf_to_images-1779003400767.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1468
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-17T07:36:41.063800+00:00_

Pages:           21

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 714
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-17T07:36:49.974145+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "7-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "7-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-17T07:36:51.259211+00:00_

Error: result (2,786,001 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/add20d08-e3f3-434f-9d96-5ab81c489ce4/tool-results/mcp-agent-ml-research-pdf_to_images-1779003411116.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/add20d08-e3f3-434f-9d96-5ab81c489ce4/tool-results/mcp-agent-ml-research-pdf_to_images-1779003411116.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/add20d08-e3f3-434f-9d96-5ab81c489ce4/tool-results/mcp-agent-ml-research-pdf_to_images-1779003411116.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1285
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-17T07:36:57.030697+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdftotext main.pdf - 2>/dev/null | grep -n \"Limitations\\|References\\|\\\\\\\\section\\|Appendix\\|^A \" | head -30",
  "description": "Find section boundaries in PDF text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdftotext main.pdf - 2>/dev/null | grep -n \"Limitations\\|References\\|\\\\\\\\section\\|Appendix\\|^A \" | head -30",
    "description": "Find section boundaries in PDF text"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-17T07:36:57.231997+00:00_

717:0.172, Qwen3 r = 0.138; Appendix I). SCS
720:accuracy (∆r: −0.023 to +0.035; Appendix L),
834:in Appendix G). Cross-model validation uses MetaLlama-3.1-8B-Instruct (Dubey et al., 2024). All
848:Unless otherwise noted, all experiments in this section use the v1 prompt (§3.5; full templates in Appendix G).
862:Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (§4.5). The
979:level (Appendix O). Formal trend analysis confirms
1119:vs. Qwen3 r = 0.138; Appendix), suggesting that
1132:in Appendix J). At 80 relations, extreme-batch
1182:pools (permutation p ≈ 0.60; Appendix K). The
1201:correlation structure; see Appendix M for the illustrative aggregation model).
1242:on 8B NER (Limitations, item 1).
1250:modulates magnitude but does not eliminate the effect (Appendix H). The BCS–accuracy correlation
1304:correlation vanishes (p > 0.2; Appendix E). The
1363:holds across four structurally distinct prompt variants at count 32 (all r < −0.47; Appendix H.1),
1390:±3 pp; Appendix C).
1435:A natural intervention against confusability-driven
1454:0.292, versus 0.445 for single-pass (Table 7, Appendix B).
1608:than confined to low-confidence predictions (Appendix B).
1658:Appendix B.1). The root cause is constrained decoding: the enum constraint forces the model to
1761:Limitations
1808:∼3× at batch level (Appendix M), yielding R2 of
1818:not reach significance (p = 0.50; Appendix C).
1821:Appendix C), and cross-pool slope consistency
1827:Appendix H). Cross-scale evidence (32B vs. 8B)
1923:as a covariate leaves the BCS partial effect unchanged (p = 0.245 for origin; Appendix N).
2056:Yes. The Limitations section (after §7) discusses single-model reliance, modest pairwise
2310:References
2391:A benchmark for robust generalization in schemaguided dialogue systems. In Proceedings of the AAAI
3373:A separate within-dataset 2 × 2 factorial on
3765:A trigger is the word or phrase that
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_
…[truncated 82 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-17T07:37:12.099664+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\\\\\enlargethispage",
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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\\\\\enlargethispage",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-17T07:37:12.652454+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-17T07:37:12.803497+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -c \"---\" abstract.tex introduction.tex related_work.tex experimental_setup.tex results.tex sdgd_negative.tex discussion.tex",
  "description": "Count em-dashes in main body tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -c \"---\" abstract.tex introduction.tex related_work.tex experimental_setup.tex results.tex sdgd_negative.tex discussion.tex",
    "description": "Count em-dashes in main body tex files"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-17T07:37:12.854128+00:00_

Exit code 2
grep: unrecognized option '---'
Usage: grep [OPTION]... PATTERNS [FILE]...
Try 'grep --help' for more information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-17T07:37:16.719429+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -c -- '---' abstract.tex introduction.tex related_work.tex experimental_setup.tex results.tex sdgd_negative.tex discussion.tex",
  "description": "Count LaTeX em-dashes in body files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -c -- '---' abstract.tex introduction.tex related_work.tex experimental_setup.tex results.tex sdgd_negative.tex discussion.tex",
    "description": "Count LaTeX em-dashes in body files"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-17T07:37:17.173743+00:00_

abstract.tex:1
introduction.tex:4
related_work.tex:4
experimental_setup.tex:2
results.tex:5
sdgd_negative.tex:3
discussion.tex:0
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-17T07:37:17.525514+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "enlargethispage",
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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "enlargethispage",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-17T07:37:17.629194+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex:19:\enlargethispage*{9\baselineskip}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-17T07:39:12.581573+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 10 审稿意见 — Reviewer 2（新颖性 + 贡献清晰度 + 写作质量 + 格式合规）\n\n## 总体评分\n**Overall**: 3/5 (Findings)\n**一句话总结**: 实验设计严谨的 empirical confirmation paper，但核心度量 SCS 与 LLM-PEE 形式相同、typical-batch 效应仅 2.2pp 的实际意义有限、且 negative results 占篇幅过大，削弱了作为 EMNLP Main 贡献的说服力。\n\n## 官方维度打分（ACL ARR Review Form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 实验设计 (stratified count vs. confusability) 严谨，统计方法（TOST, permutation, bootstrap CI）规范；但 MAVEN 数据集上信号消失、NER 方向反转需依赖复杂 confound 解释 |\n| Excitement | 2/5 | 主要发现是 \"count dominates confusability by ~20×\"，即 confusability 的实际影响很小（2.2pp）；SCS 与 LLM-PEE 的 metric 形式相同；negative results 有价值但无 actionable insight |\n| Reproducibility | 4/5 | 代码承诺释放，prompt 模板在 appendix，数据集公开，超参完整；但 supplementary 有 placeholder sections 未填 |\n| Overall | 3/5 | Findings 级别：贡献扎实但增量有限，适合 Findings track |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] SCS/BCS 与 LLM-PEE 的区分不够清晰，增量贡献需重新 framing\n- 具体位置：§2 Related Work (¶2 \"SCS novelty\")、§1 Introduction Contribution #2\n- 问题：论文在 §2 ¶4 明确承认 \"SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE\"。Contribution #2 声称 \"Pairwise embedding similarity predicts type confusion\"，但 LLM-PEE 已使用相同 metric 做 schema decomposition，隐含了相同假设。论文的真正增量是 controlled experimental design 证明了因果方向性，但这一点在 Abstract 和 Contribution list 中没有被清晰表达——读者会认为 SCS 本身是贡献。\n- 为什么影响接收：审稿人会质疑 \"what's new beyond LLM-PEE?\" 如果 framing 不够精确，这会被视为 incremental replication。\n- 建议修改方向：Contribution #2 应重写为 \"We provide the first controlled empirical evidence that pairwise embedding similarity causally predicts type confusion, isolating this from count effects\"，并在 Abstract 中明确 \"empirical validation under controlled conditions\" 而非暗示 metric 本身是新的。\n\n**N2** [critical] Typical-batch 效应仅 2.2pp——实际意义（practical significance）论证不足\n- 具体位置：§4.3 \"Practical magnitude\" (¶), Abstract (\"confusability accounts for ≈2.2pp accuracy difference---markedly smaller than count effects\")\n- 问题：2.2pp 在随机 batch 中的 typical confusability gap 是 statistically significant 但 practically marginal。论文诚实报告了这一数字，但同时声称 \"BCS explains 22--53% of cross-batch variance\" 和 \"quartile Δ = -5.3pp\"。这里有叙事张力：如果 confusability 的典型影响只有 2.2pp，为什么要花整篇论文隔离它？extreme-batch gap (31.2pp) 来自人为构造的极端条件，不反映真实部署场景。\n- 为什么影响接收：审稿人会问 \"so what?\" — 如果 count dominates by 20×，那么 practitioner 应该关注 schema size reduction，confusability 只是次要因素。这削弱了论文的 motivation。\n- 建议修改方向：强化 \"为什么了解 confusability channel 的存在本身有价值\"（如：在 count 固定时，BCS 可以预测 22-53% cross-batch variance，这对 schema design 有直接 actionable guidance）。或者 reframe 为：本文发现是 \"count is the bottleneck, not confusability\"，这本身是对 decomposition literature 的重要纠正。\n\n**N3** [critical] Negative results 占比过大但缺乏 constructive resolution\n- 具体位置：§5 全节 (SDGD failure + routing failure), Contribution #4\n- 问题：§5 用了约 1.5 页报告所有 decomposition 方法都失败：NER 因 merge amplification 失败，RE 因 routing 失败，confusability-aware grouping 比 random 仅好 1.4pp (n.s.)。这些 negative results 有价值，但论文没有提出任何 promising direction——Conclusion 只说 \"BCS enables pre-hoc screening\" 和 \"deployable routing as an open challenge\"。\n- 为什么影响接收：EMNLP Main 通常期待 negative results 伴随 insight on why things fail + at least one promising direction。当前只有 diagnosis 没有 prescription，读者读完会问 \"那我该怎么办？\"\n- 建议修改方向：(a) 减少 §5 篇幅（移部分到 appendix），为 Discussion 腾空间；(b) 在 Discussion 中提出 2-3 个具体的 future direction（如：free-form generation routing, calibrated confidence, schema-aware fine-tuning）并给出初步证据或分析。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 数字密度过高，30 秒可读性差\n- 具体位置：Abstract (abstract.tex)\n- 问题：Abstract 包含 \"≈2.2pp\"、\"−49pp\"、\"22--53%\"、\"TOST p = 0.003 at ±3pp\"、\"+29.8pp\"、\"+1.4pp (p ≈ 0.19)\" 等大量数字。审稿人在 30 秒内无法消化这些信息。TOST p-value 和 equivalence margin 出现在 abstract 中极不常见。\n- 建议：Abstract 保留 2-3 个关键数字，将统计细节留给正文。重点传达 \"what's the story\" 而非 \"what are the numbers\"。\n\n**W2** [warning] Introduction Contribution list 过于冗长且含未铺垫概念\n- 具体位置：§1 Introduction, Contribution items 1-4\n- 问题：每条 Contribution 都超过 3 行，且包含正文才解释的术语（TOST, merge amplification, oracle routing, constrained decoding）。Contribution #1 中 \"TOST p = 0.003 at ±3pp\" 在 Introduction 中出现但 TOST 方法到 §4.4/Appendix C 才解释。这违反 \"首次出现须定义\" 原则。\n- 建议：Contribution list 每条 1-2 行，技术细节留给对应 section。\n\n**W3** [warning] `\\enlargethispage*{9\\baselineskip}` 严重操纵页面布局\n- 具体位置：sdgd_negative.tex line 19\n- 问题：这个命令将某页扩展了约 9 行（≈1/4 页高度），严重偏离 ACL template 的标准页面设置。这在实质上等于多获得了 1/4 页空间。虽然不一定会 desk reject，但审稿人或 AC 可能注意到页面底部 margin 异常。\n- 建议：删除此命令，压缩正文到 8 页自然布局内。将部分 §5 内容移至 appendix。\n\n**W4** [warning] LaTeX em-dash (`---`) 使用频率偏高\n- 具体位置：正文 body 共 19 处 `---`（abstract 1, intro 4, related_work 4, setup 2, results 5, sdgd 3）\n- 问题：19 处 explanatory em-dash 在 8 页内是异常高频。多数用于插入解释性补充（如 \"highly confusable---types share a color\"、\"the within-pool slope is significant---but establishes that...\"），这是 AI 辅助写作的典型 pattern。人类学术写作通常用括号或拆分句子。\n- 建议：将至少 2/3 的 em-dash 替换为括号、逗号或独立句子。保留数学/范围用法的 en-dash。\n\n**W5** [warning] MAVEN 数据集结果方向相反，centrality confound 解释复杂\n- 具体位置：§4.5 Centrality Confound, Appendix E\n- 问题：MAVEN 上 per-type BCS-F1 显示 positive correlation（与假设相反），需要引入 centrality confound + partial correlation 才能解释。虽然分析本身合理，但这意味着论文的核心 claim \"BCS predicts degradation\" 在 4 个数据集中只有 2 个直接支持（FewRel, DocRED），1 个需要 pairwise 分析才有信号（Few-NERD batch level 是 positive），1 个方向反转需要 confound adjustment。\n- 建议：在 Introduction 或 Abstract 中更诚实地表述适用范围：\"cross-domain schemas\" 而非暗示普适性。\n\n**W6** [warning] Supplementary 有 placeholder sections 未完成\n- 具体位置：supplementary.tex lines 448-449, 455-456, 460-461\n- 问题：三处 \"[Placeholder: ... to be added.]\" 出现在 Appendix §L.1, §L.2, §L.3。提交未完成的 supplementary material 不专业。\n- 建议：投稿前填充或删除这些 section。\n\n## 小问题（不影响接收）\n- §1 footnote 2 中 anonymous review URL (`anonymous.4open.science/r/schema-dag-extraction`) 包含项目名 \"schema-dag-extraction\"，如果作者的 GitHub 有同名 repo 可能泄露身份\n- Orphan bib entry: `lakens-2017-equivalence` 在 .bib 中但从未被引用\n- §2 ¶1 \"These methods perform well with moderate schemas (4--20 types) but none investigates...\" 中 \"none investigates\" 是过强断言——LLM-PEE 正是研究 schema 规模的\n- Discussion/Conclusion 仅 ~12 行（2 段 + 3 句），与前文的分析深度不匹配，显得仓促\n\n## Missing References\n- **NuNER** (Bogdanov et al., 2024): zero-shot NER via instruction tuning on diverse schemas，直接相关\n- **Self-Improving LLM IE** (如 Zhang et al. 2024, \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\"): 自我改进策略可能缓解 confusability\n- **LLMaAA** (Zhang et al., 2024): LLM-as-annotator 范式下同样面临 schema scaling\n- 缺少 structured prediction 视角的引用（如 CRF-based label confusion, structured inference with label dependencies）\n\n## 主要优势\n- **实验设计出色**：stratified design 控制 count vs. confusability 是本文最强贡献，实验逻辑严密\n- **诚实报告 negative results**：SDGD 失败、routing 失败、practical magnitude 仅 2.2pp——这种透明度在 NLP 论文中罕见且有价值\n- **统计方法规范**：TOST equivalence testing、permutation tests、bootstrap CIs、variance decomposition——方法论素质高于平均水平\n- **Limitations section 非常详尽**：8 条 limitations + multiple comparisons discussion，展示了作者的学术严谨\n- **跨数据集/跨模型/跨 prompt 验证**：4 datasets × 2 models × 4+ prompt variants，robustness check 全面\n\n## 定位建议\n本文更适合定位为 **empirical analysis / negative result paper** 投 Findings track，而非 Main Conference。核心障碍是：(1) metric 非新；(2) 主要发现是 confusability 影响小；(3) 没有可用的 mitigation 方案。如果 reframe 为 \"decomposition literature 的 assumption 是错的，count 才是 bottleneck\"，并精简 negative results section 为更 concise 的诊断，可能更有竞争力。",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 10 审稿意见 — Reviewer 2（新颖性 + 贡献清晰度 + 写作质量 + 格式合规）\n\n## 总体评分\n**Overall**: 3/5 (Findings)\n**一句话总结**: 实验设计严谨的 empirical confirmation paper，但核心度量 SCS 与 LLM-PEE 形式相同、typical-batch 效应仅 2.2pp 的实际意义有限、且 negative results 占篇幅过大，削弱了作为 EMNLP Main 贡献的说服力。\n\n## 官方维度打分（ACL ARR Review Form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 实验设计 (stratified count vs. confusability) 严谨，统计方法（TOST, permutation, bootstrap CI）规范；但 MAVEN 数据集上信号消失、NER 方向反转需依赖复杂 confound 解释 |\n| Excitement | 2/5 | 主要发现是 \"count dominates confusability by ~20×\"，即 confusability 的实际影响很小（2.2pp）；SCS 与 LLM-PEE 的 metric 形式相同；negative results 有价值但无 actionable insight |\n| Reproducibility | 4/5 | 代码承诺释放，prompt 模板在 appendix，数据集公开，超参完整；但 supplementary 有 placeholder sections 未填 |\n| Overall | 3/5 | Findings 级别：贡献扎实但增量有限，适合 Findings track |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] SCS/BCS 与 LLM-PEE 的区分不够清晰，增量贡献需重新 framing\n- 具体位置：§2 Related Work (¶2 \"SCS novelty\")、§1 Introduction Contribution #2\n- 问题：论文在 §2 ¶4 明确承认 \"SCS shares its formal definition---pairwise cosine similarity of type name embeddings---with the partitioning criterion used in LLM-PEE\"。Contribution #2 声称 \"Pairwise embedding similarity predicts type confusion\"，但 LLM-PEE 已使用相同 metric 做 schema decomposition，隐含了相同假设。论文的真正增量是 controlled experimental design 证明了因果方向性，但这一点在 Abstract 和 Contribution list 中没有被清晰表达——读者会认为 SCS 本身是贡献。\n- 为什么影响接收：审稿人会质疑 \"what's new beyond LLM-PEE?\" 如果 framing 不够精确，这会被视为 incremental replication。\n- 建议修改方向：Contribution #2 应重写为 \"We provide the first controlled empirical evidence that pairwise embedding similarity causally predicts type confusion, isolating this from count effects\"，并在 Abstract 中明确 \"empirical validation under controlled conditions\" 而非暗示 metric 本身是新的。\n\n**N2** [critical] Typical-batch 效应仅 2.2pp——实际意义（practical significance）论证不足\n- 具体位置：§4.3 \"Practical magnitude\" (¶), Abstract (\"confusability accounts for ≈2.2pp accuracy difference---markedly smaller than count effects\")\n- 问题：2.2pp 在随机 batch 中的 typical confusability gap 是 statistically significant 但 practically marginal。论文诚实报告了这一数字，但同时声称 \"BCS explains 22--53% of cross-batch variance\" 和 \"quartile Δ = -5.3pp\"。这里有叙事张力：如果 confusability 的典型影响只有 2.2pp，为什么要花整篇论文隔离它？extreme-batch gap (31.2pp) 来自人为构造的极端条件，不反映真实部署场景。\n- 为什么影响接收：审稿人会问 \"so what?\" — 如果 count dominates by 20×，那么 practitioner 应该关注 schema size reduction，confusability 只是次要因素。这削弱了论文的 motivation。\n- 建议修改方向：强化 \"为什么了解 confusability channel 的存在本身有价值\"（如：在 count 固定时，BCS 可以预测 22-53% cross-batch variance，这对 schema design 有直接 actionable guidance）。或者 reframe 为：本文发现是 \"count is the bottleneck, not confusability\"，这本身是对 decomposition literature 的重要纠正。\n\n**N3** [critical] Negative results 占比过大但缺乏 constructive resolution\n- 具体位置：§5 全节 (SDGD failure + routing failure), Contribution #4\n- 问题：§5 用了约 1.5 页报告所有 decomposition 方法都失败：NER 因 merge amplification 失败，RE 因 routing 失败，confusability-aware grouping 比 random 仅好 1.4pp (n.s.)。这些 negative results 有价值，但论文没有提出任何 promising direction——Conclusion 只说 \"BCS enables pre-hoc screening\" 和 \"deployable routing as an open challenge\"。\n- 为什么影响接收：EMNLP Main 通常期待 negative results 伴随 insight on why things fail + at least one promising direction。当前只有 diagnosis 没有 prescription，读者读完会问 \"那我该怎么办？\"\n- 建议修改方向：(a) 减少 §5 篇幅（移部分到 appendix），为 Discussion 腾空间；(b) 在 Discussion 中提出 2-3 个具体的 future direction（如：free-form generation routing, calibrated confidence, schema-aware fine-tuning）并给出初步证据或分析。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 数字密度过高，30 秒可读性差\n- 具体位置：Abstract (abstract.tex)\n- 问题：Abstract 包含 \"≈2.2pp\"、\"−49pp\"、\"22--53%\"、\"TOST p = 0.003 at ±3pp\"、\"+29.8pp\"、\"+1.4pp (p ≈ 0.19)\" 等大量数字。审稿人在 30 秒内无法消化这些信息。TOST p-value 和 equivalence margin 出现在 abstract 中极不常见。\n- 建议：Abstract 保留 2-3 个关键数字，将统计细节留给正文。重点传达 \"what's the story\" 而非 \"what are the numbers\"。\n\n**W2** [warning] Introduction Contribution list 过于冗长且含未铺垫概念\n- 具体位置：§1 Introduction, Contribution items 1-4\n- 问题：每条 Contribution 都超过 3 行，且包含正文才解释的术语（TOST, merge amplification, oracle routing, constrained decoding）。Contribution #1 中 \"TOST p = 0.003 at ±3pp\" 在 Introduction 中出现但 TOST 方法到 §4.4/Appendix C 才解释。这违反 \"首次出现须定义\" 原则。\n- 建议：Contribution list 每条 1-2 行，技术细节留给对应 section。\n\n**W3** [warning] `\\enlargethispage*{9\\baselineskip}` 严重操纵页面布局\n- 具体位置：sdgd_negative.tex line 19\n- 问题：这个命令将某页扩展了约 9 行（≈1/4 页高度），严重偏离 ACL template 的标准页面设置。这在实质上等于多获得了 1/4 页空间。虽然不一定会 desk reject，但审稿人或 AC 可能注意到页面底部 margin 异常。\n- 建议：删除此命令，压缩正文到 8 页自然布局内。将部分 §5 内容移至 appendix。\n\n**W4** [warning] LaTeX em-dash (`---`) 使用频率偏高\n- 具体位置：正文 body 共 19 处 `---`（abstract 1, intro 4, related_work 4, setup 2, results 5, sdgd 3）\n- 问题：19 处 explanatory em-dash 在 8 页内是异常高频。多数用于插入解释性补充（如 \"highly confusable---types share a color\"、\"the within-pool slope is significant---but establishes that...\"），这是 AI 辅助写作的典型 pattern。人类学术写作通常用括号或拆分句子。\n- 建议：将至少 2/3 的 em-dash 替换为括号、逗号或独立句子。保留数学/范围用法的 en-dash。\n\n**W5** [warning] MAVEN 数据集结果方向相反，centrality confound 解释复杂\n- 具体位置：§4.5 Centrality Confound, Appendix E\n- 问题：MAVEN 上 per-type BCS-F1 显示 positive correlation（与假设相反），需要引入 centrality confound + partial correlation 才能解释。虽然分析本身合理，但这意味着论文的核心 claim \"BCS predicts degradation\" 在 4 个数据集中只有 2 个直接支持（FewRel, DocRED），1 个需要 pairwise 分析才有信号（Few-NERD batch level 是 positive），1 个方向反转需要 confound adjustment。\n- 建议：在 Introduction 或 Abstract 中更诚实地表述适用范围：\"cross-domain schemas\" 而非暗示普适性。\n\n**W6** [warning] Supplementary 有 placeholder sections 未完成\n- 具体位置：supplementary.tex lines 448-449, 455-456, 460-461\n- 问题：三处 \"[Placeholder: ... to be added.]\" 出现在 Appendix §L.1, §L.2, §L.3。提交未完成的 supplementary material 不专业。\n- 建议：投稿前填充或删除这些 section。\n\n## 小问题（不影响接收）\n- §1 footnote 2 中 anonymous review URL (`anonymous.4open.science/r/schema-dag-extraction`) 包含项目名 \"schema-dag-extraction\"，如果作者的 GitHub 有同名 repo 可能泄露身份\n- Orphan bib entry: `lakens-2017-equivalence` 在 .bib 中但从未被引用\n- §2 ¶1 \"These methods perform well with moderate schemas (4--20 types) but none investigates...\" 中 \"none investigates\" 是过强断言——LLM-PEE 正是研究 schema 规模的\n- Discussion/Conclusion 仅 ~12 行（2 段 + 3 句），与前文的分析深度不匹配，显得仓促\n\n## Missing References\n- **NuNER** (Bogdanov et al., 2024): zero-shot NER via instruction tuning on diverse schemas，直接相关\n- **Self-Improving LLM IE** (如 Zhang et al. 2024, \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\"): 自我改进策略可能缓解 confusability\n- **LLMaAA** (Zhang et al., 2024): LLM-as-annotator 范式下同样面临 schema scaling\n- 缺少 structured prediction 视角的引用（如 CRF-based label confusion, structured inference with label dependencies）\n\n## 主要优势\n- **实验设计出色**：stratified design 控制 count vs. confusability 是本文最强贡献，实验逻辑严密\n- **诚实报告 negative results**：SDGD 失败、routing 失败、practical magnitude 仅 2.2pp——这种透明度在 NLP 论文中罕见且有价值\n- **统计方法规范**：TOST equivalence testing、permutation tests、bootstrap CIs、variance decomposition——方法论素质高于平均水平\n- **Limitations section 非常详尽**：8 条 limitations + multiple comparisons discussion，展示了作者的学术严谨\n- **跨数据集/跨模型/跨 prompt 验证**：4 datasets × 2 models × 4+ prompt variants，robustness check 全面\n\n## 定位建议\n本文更适合定位为 **empirical analysis / negative result paper** 投 Findings track，而非 Main Conference。核心障碍是：(1) metric 非新；(2) 主要发现是 confusability 影响小；(3) 没有可用的 mitigation 方案。如果 reframe 为 \"decomposition literature 的 assumption 是错的，count 才是 bottleneck\"，并精简 negative results section 为更 concise 的诊断，可能更有竞争力。",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-17T07:39:16.397925+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3816
}
```

</details>

---


### Assistant

_source line 638 · 2026-05-17T07:39:35.701456+00:00_

Round 10 审稿意见已提交。

核心判断：**Overall 3/5 (Findings)**。三个 Must-Fix 问题：

1. **SCS 与 LLM-PEE 形式相同**，增量贡献的 framing 不清晰——需要明确论文贡献是 controlled experimental evidence 而非 metric 本身
2. **Typical-batch 效应仅 2.2pp**，practical significance 论证不足——需要解释为什么隔离一个占 1/20 的因素值得整篇论文
3. **Negative results 占比过大但无 constructive resolution**——SDGD 失败 + routing 失败用了 ~1.5 页但没有 promising direction

另有 6 个 Should-Fix（Abstract 数字堆砌、Contribution list 冗长、`\enlargethispage*{9\baselineskip}` 操纵页面、em-dash 高频、MAVEN 反向结果、supplementary placeholder 未完成）。

Sources:
- [ACL ARR Review Form](http://aclrollingreview.org/reviewform)
- [ACL ARR Reviewer Guidelines](http://aclrollingreview.org/reviewerguidelines)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 20

## Round 20

14 recorded events


### User

_source line 639 · 2026-05-17T07:40:04.306175+00:00_

[Round 10 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的意见。对每个要点：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 1 的完整审稿原文：

## 总体评分
**Overall**: 3.5/5（介于 Findings acceptance 和 Conference acceptance 之间）
**一句话总结**: 实验设计严谨、统计方法扎实，但核心效应量极小（pairwise r²=1.3-1.7%），聚合推理链条中存在条件化偏倚，且"两通道有界交互"的因果主张超出观察性证据所能支撑的范围。

## Must-Fix 问题

**N1** [critical] 条件化R²到batch R²的聚合推理链存在逻辑断裂
- §4.3 Practical magnitude + Appendix H
- 问题：论文核心叙事依赖从pairwise r²=1.3-1.7%（unconditional）→ conditional R²=7%（non-zero confusion pairs only）→ batch R²=22%的推理链。但unconditional simulation仅产出R²=0.044，远低于观测值0.218。论文用"BCS通过active confusable pairs的密度预测batch accuracy"来解释这个5倍gap，但这构成了对dependent variable的条件化。更关键的是，如果89%的type pairs从不产生mutual confusion，那BCS（mean over ALL pairs）理论上应该被这89%的噪声稀释——为何batch-level R²仍达22%？
- 建议：(1) 明确承认simulation是explanatory而非confirmatory；(2) 提供不依赖条件化的解释。

**N2** [critical] TOST equivalence margin（±3pp）的justification循环且对核心claim的支撑不足
- Appendix C, Table 5
- 问题：(1) Margin选择理由是"3pp interaction atop 2.2pp main effect = >130% amplification"，但为什么130%是临界值？(2) Table 5显示±1pp时TOST inconclusive（p=0.278），±2pp时仅marginal（p=0.047）。interaction可能达main effect的~50%。(3) 2×2 factorial（n=54）TOST p=0.56完全失败，Few-NERD factorial p=0.50也不显著。三个独立测试中两个失败。

**N3** [critical] 因果语言超出观察性证据的边界
- §4.4, §5 Discussion, Title ("Does Type Confusability Shape...")
- 问题：标题"shape"暗示因果，正文"driven"、"channels"、"bounded interaction"暗示mechanistic independence，但Limitations item 7自己承认"correlational evidence...does not establish interventional causality"。

## Should-Fix 问题

**W1** Multiple comparisons的Rothman (1990)立场应用过于宽松
**W2** Cross-seed variance decomposition暴露non-determinism（seed SD 2.7pp at count 16），与"greedy消除randomness"矛盾，且与2.2pp typical effect量级相当
**W3** MAVEN实质上不支持核心假设——4个数据集中只有2个直接支持BCS batch-level prediction
**W4** NER U-shape的mechanistic解释不充分

## 主要优势
1. 实验设计极为严谨（双paradigm factorial思想）
2. Confound identification透彻（centrality, frequency, pool composition, split-origin）
3. 负面结果honest reporting
4. 统计方法多元且适当
5. 效应量的honest contextualization
6. Cross-validation thorough

---

请逐条回应上述 Must-Fix (N1-N3) 和 Should-Fix (W1-W4) 中的每一项。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-17T07:40:52.354383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "60",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "60",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-17T07:40:52.756590+00:00_

60	
61	\paragraph{Within-pool controlled comparison.}
62	\label{sec:within_pool}
63	Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
64	
65	\paragraph{Practical magnitude.}
66	\label{sec:practical_magnitude}
67	For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0])---roughly 7\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). The 31.2\,pp figure reflects maximum BCS contrast, not the typical batch experience. Conditional pair-level $R^2 \approx 7\%$ among non-zero confusion pairs (vs.\ unconditional $r^2 = 1.3$--$1.7\%$ across all pairs; Table~\ref{tab:pairwise}; we note the conditioning inflates this estimate) aggregates to batch-level $R^2 \approx 22\%$ ($\sim$3$\times$ amplification, consistent with a Monte Carlo simulation accounting for inter-pair correlation structure; see Appendix~\ref{app:aggregation-sim} for the illustrative aggregation model).
68	
69	\paragraph{Cross-model validation.}
70	The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap. Both models converge to $\approx$51\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\S\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).
71	
72	\paragraph{Prompt sensitivity.}
73	Under the v2 prompt, the extreme-batch BCS gap is $-$2
…[truncated 2399 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-17T07:40:52.857486+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-17T07:40:52.908266+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. To our knowledge, we present the first controlled study isolating type confusability from type count in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets. We introduce the Schema Confusability Score (SCS) and two experimental paradigms: count curves (varying schema size while randomizing confusability) and BCS-controlled experiments (fixing size while varying confusability).
3	
4	We identify two degradation channels: count-driven recall decline and confusability-driven type substitution. In typical random batches, confusability accounts for ${\approx}\,2.2$\,pp accuracy difference---markedly smaller than count effects ($-$49\,pp for document-level RE)---while batch-level BCS explains 22--53\% of cross-batch variance. The channels exhibit bounded interaction in RE (TOST $p = 0.003$ at $\pm 3$\,pp) but are coupled in NER where boundary and type ambiguity interact. Effects are directionally consistent across prompt designs and model scales, though Channel~2 attenuates on smaller models. Schema decomposition via oracle routing recovers substantial RE gains, but confusability-aware grouping yields no significant improvement over random.
5	\end{abstract}
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-17T07:40:55.870815+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-17T07:40:55.921465+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what 
…[truncated 3588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-17T07:41:05.106224+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-17T07:41:05.307213+00:00_

1	% DEPRECATED — this file is no longer included in main.tex.
2	% The active conclusion is in discussion.tex (\input{discussion}).
3	% Kept for reference only; safe to delete.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-17T07:41:13.154999+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Limitations",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content",
  "-A": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Limitations",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "output_mode": "content",
    "-A": "80"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-17T07:41:13.205831+00:00_

38:\section*{Limitations}
39-\begin{enumerate}[leftmargin=*,itemsep=2pt]
40-\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41-
42-\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43-
44-\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded interaction ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.
45-
46-[Omitted long context line]
47-
48-\item \textbf{NER evaluation metric.} Our exact-match NER evaluation conflates boundary errors (partial span overlap) with type errors (correct span, wrong label). Relaxed matching may yield different confusability effect sizes, as boundary ambiguity may correlate with schema complexity independently of type similarity.
49-
50-\item \textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.
51-
52-\item \textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relations
…[truncated 5892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-17T07:42:56.801589+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE with nuance] R1-N1: 条件化 R² 到 batch R² 的聚合推理链**\n\nR1 的核心批评方向正确：从 unconditional r²=1.3-1.7% 跳到 conditional R²=7% 确实构成对 dependent variable 的条件化，且 unconditional simulation 仅产出 R²=0.044 vs 观测 0.218 的 5× gap 需要解释。\n\n但我注意到论文已经部分 hedge 了这一点：\n- §4.3 明确注明 \"we note the conditioning inflates this estimate\"\n- Appendix M 开头声明 \"It is not the evidence base for our claims---the observed batch-level R² = 0.218 is a direct empirical measurement independent of this simulation\"\n\n因此，batch-level R²=0.218 是直接观测值（OLS regression on 100 random 16-type batches, §4.3），不是从 pairwise 推导出来的。聚合链是 post-hoc explanatory model。R1 的质疑在于叙事暗示因果链条，但核心 claim（BCS 预测 batch accuracy with R²=0.22）有独立实证支撑。\n\n**对 R1 \"为什么 BCS mean over ALL pairs 没被 89% 噪声稀释\" 的补充观点**：高 mean-BCS batches 几何上必然包含更多 active confusable pairs（因为 mean 高意味着更多 pair 超过 confusion activation threshold）。这不是条件化，而是 BCS 作为 proxy 的机制解释——类比：平均气温预测降雪概率，不需要条件化于\"确实下雪的日子\"来解释为什么 mean temperature 有预测力。\n\n**结论**：同意叙事链条有误导性，但 batch R²=0.218 的实证基础独立成立。建议作者更明确区分 \"observational finding\" 与 \"post-hoc explanatory model\"。\n\n---\n\n**[REBUT] R1-N2: TOST equivalence margin 的 justification**\n\nR1 的表述 \"三个独立测试中两个失败\" 是对论文设计层级的误读。\n\n论文在 §4.4 (results.tex line 87) 明确写道：\n> \"The full-range regression (n = 69, five count levels) serves as the **primary** separability test; the 2 × 2 factorial (n = 54) as a **sensitivity check**.\"\n\nAppendix C (supplementary.tex line 150) 进一步解释：\n> \"The regression approach provides the stronger test by leveraging the full count range.\"\n\n实验层级：\n1. **Primary test**（full-range regression, n=69, 5 count levels）: interaction = 0.47pp, TOST p=0.003 at ±3pp → **PASSES**\n2. **Sensitivity check**（2×2 factorial, n=54）: TOST p=0.56 → power 不足（fewer count levels, narrower BCS contrast）\n3. **NER factorial**: p=0.50 → NER 中两 channel 本身就 coupled（论文承认 \"bounded interaction in RE but coupled in NER\"）\n\nR1 将 sensitivity check 的 non-significance 等同于 \"failure\" 是不恰当的——statistical test failing to reject ≠ evidence of absence，尤其在 known underpowered conditions 下。\n\n但 R1 关于 margin 选择循环性的批评有部分道理：为什么 130% amplification 是 \"materially alter practitioner decisions\" 的阈值？这确实是 judgment call，不是来自 external standard。Table 5 的 sensitivity analysis 显示 ±2pp 也 marginal equivalent (p=0.047)，说明结论对 margin 选择不敏感。\n\n**结论**：反驳 \"三测试两失败\" 的定性，但同意 margin justification 需要更透明的 external anchoring。\n\n---\n\n**[AGREE with qualification] R1-N3: 因果语言超出证据边界**\n\nR1 指出标题 \"shape\" 和正文 \"channels\"/\"driven\" 暗示因果，而 Limitations item 7 承认 correlational。这一张力确实存在。\n\n但需要注意：BCS-controlled experiments（§4.3）是 **quasi-experimental design**，不是纯观察研究。作者通过 constructing high/low BCS batches while holding count fixed 实现了对 confusability 的 deliberate manipulation。这比 observational correlation 更接近 interventional evidence——虽然不是 randomized controlled trial（因为 BCS 和 type identity/frequency 不能完全解耦），但 within-pool controlled comparison（§4.3, permutation p=0.60）控制了 pool composition confound。\n\nTitle \"Does Type Confusability Shape...\" 是 question form，比 assertion 弱。\"Channel\" terminology 暗示 mechanistic independence，但论文也明确说 NER 中两者 coupled。\n\n**结论**：同意因果语言应进一步软化（建议 \"predict\" 替代 \"driven\"；\"separable predictors\" 替代 \"channels\"），但反驳将此归类为纯观察研究——BCS-controlled design 具有 quasi-experimental 性质。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Multiple comparisons / Rothman stance**\n\n同意。Rothman (1990) 的 \"no correction needed for independent tests\" 适用于 conceptual replications，但论文内部有些 secondary analyses（如 per-prompt-variant correlations, Table in Appendix H.1）是 same-dataset multiple looks，不完全属于 independent replications。论文承认 \"core claims rest on effects reaching p < 0.001\"（Limitations），这是 pragmatic 但非 formal 的保护。\n\n---\n\n**[REBUT] R1-W2: Cross-seed variance 2.7pp vs typical effect 2.2pp**\n\nR1 的比较在量纲上不对等。\n\n根据 Appendix O (main.tex, Table at line 437-447)：\n- Count 16: Batch SD = 0.0626 (6.26pp), Seed SD = 0.0270 (2.70pp), Ratio = 5.4\n\n\"Seed SD = 2.70pp\" 是 3 个 seed 各自产生的 25-batch mean 的标准差。每个 seed 控制的是 **batch composition sampling**（哪些类型组合进同一个 batch），不是模型推理随机性。§3.5 明确说 \"single-seed evaluation with greedy decoding, which eliminates model-level randomness\"——模型推理用 temperature=0 + seed 42，确定性的。\n\n2.70pp seed SD 反映的是：从无限可能的 batch 组合中抽 25 个样本的 sampling variance of the estimator，不是模型 non-determinism。而 2.2pp 是 BCS IQR 对应的 expected accuracy gap（fixed quantity）。这两个数字比较不合理——前者是 estimator uncertainty，后者是 effect size。\n\n进一步证据：count 80 时 Seed SD = 0.88pp（Table row），此时只有一种 batch composition（全 schema），所有 variance 必须来自非 batch 来源——可能是 FP8 量化的微小 non-determinism 或 evaluation sample 的 bootstrap 差异。\n\n**但 R1 提出了一个有效的 implicit concern**：如果 seed SD = 2.7pp 反映 batch sampling noise，而 typical BCS effect = 2.2pp，那么在任意随机 25-batch 样本中，BCS 效应可能被 sampling noise 淹没——这确实限制了 practical detectability。论文的 95% CI [0.4, 4.0] for 2.2pp effect 暗示了这一点（CI 含 near-zero）。\n\n---\n\n**[AGREE] R1-W3: MAVEN 实质不支持核心假设**\n\n完全同意。我在自己的 W5 中已提出相同观点。4 个数据集中：\n- FewRel、DocRED：直接支持（negative BCS slope, significant）\n- Few-NERD batch-level：方向反转（positive r = +0.50/+0.58），需要 type-frequency confound 解释\n- MAVEN per-type：方向反转（positive ρ = +0.184/+0.208），需要 centrality confound 解释\n\n论文依赖 pairwise SCS-confusion correlation 来\"挽救\" Few-NERD 和 MAVEN，但 batch-level prediction（BCS → performance）才是 practitioner 关心的。在这个层面上只有 RE 数据集直接支持。\n\n---\n\n**[AGREE with nuance] R1-W4: NER U-shape mechanistic解释不充分**\n\n同意解释是 speculative。\"Dual-task burden: partial schemas require simultaneous span detection and type-membership filtering; at full-schema, filtering becomes vacuous and recall recovers\" (§6 Discussion) 是合理假设但未被实验验证。\n\n不过，supporting evidence 包括：\n- Per-type extraction recall = 0.586 vs single-pass = 0.368（Table 7, §5）：消除所有 type competition 后 recall 大幅恢复\n- Full-schema recall recovery (0.41 from plateau of 0.27)：当所有类型都在 prompt 中，模型不需要 \"filter membership\"\n- RE 无此 pattern（monotonic decline）：RE 是 closed-set classification，没有 span detection 负担\n\n这些 indirect evidence 使假设 plausible，但确实不构成 definitive mechanism proof。建议作者标注为 hypothesis 而非 established finding。",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE with nuance] R1-N1: 条件化 R² 到 batch R² 的聚合推理链**\n\nR1 的核心批评方向正确：从 unconditional r²=1.3-1.7% 跳到 conditional R²=7% 确实构成对 dependent variable 的条件化，且 unconditional simulation 仅产出 R²=0.044 vs 观测 0.218 的 5× gap 需要解释。\n\n但我注意到论文已经部分 hedge 了这一点：\n- §4.3 明确注明 \"we note the conditioning inflates this estimate\"\n- Appendix M 开头声明 \"It is not the evidence base for our claims---the observed batch-level R² = 0.218 is a direct empirical measurement independent of this simulation\"\n\n因此，batch-level R²=0.218 是直接观测值（OLS regression on 100 random 16-type batches, §4.3），不是从 pairwise 推导出来的。聚合链是 post-hoc explanatory model。R1 的质疑在于叙事暗示因果链条，但核心 claim（BCS 预测 batch accuracy with R²=0.22）有独立实证支撑。\n\n**对 R1 \"为什么 BCS mean over ALL pairs 没被 89% 噪声稀释\" 的补充观点**：高 mean-BCS batches 几何上必然包含更多 active confusable pairs（因为 mean 高意味着更多 pair 超过 confusion activation threshold）。这不是条件化，而是 BCS 作为 proxy 的机制解释——类比：平均气温预测降雪概率，不需要条件化于\"确实下雪的日子\"来解释为什么 mean temperature 有预测力。\n\n**结论**：同意叙事链条有误导性，但 batch R²=0.218 的实证基础独立成立。建议作者更明确区分 \"observational finding\" 与 \"post-hoc explanatory model\"。\n\n---\n\n**[REBUT] R1-N2: TOST equivalence margin 的 justification**\n\nR1 的表述 \"三个独立测试中两个失败\" 是对论文设计层级的误读。\n\n论文在 §4.4 (results.tex line 87) 明确写道：\n> \"The full-range regression (n = 69, five count levels) serves as the **primary** separability test; the 2 × 2 factorial (n = 54) as a **sensitivity check**.\"\n\nAppendix C (supplementary.tex line 150) 进一步解释：\n> \"The regression approach provides the stronger test by leveraging the full count range.\"\n\n实验层级：\n1. **Primary test**（full-range regression, n=69, 5 count levels）: interaction = 0.47pp, TOST p=0.003 at ±3pp → **PASSES**\n2. **Sensitivity check**（2×2 factorial, n=54）: TOST p=0.56 → power 不足（fewer count levels, narrower BCS contrast）\n3. **NER factorial**: p=0.50 → NER 中两 channel 本身就 coupled（论文承认 \"bounded interaction in RE but coupled in NER\"）\n\nR1 将 sensitivity check 的 non-significance 等同于 \"failure\" 是不恰当的——statistical test failing to reject ≠ evidence of absence，尤其在 known underpowered conditions 下。\n\n但 R1 关于 margin 选择循环性的批评有部分道理：为什么 130% amplification 是 \"materially alter practitioner decisions\" 的阈值？这确实是 judgment call，不是来自 external standard。Table 5 的 sensitivity analysis 显示 ±2pp 也 marginal equivalent (p=0.047)，说明结论对 margin 选择不敏感。\n\n**结论**：反驳 \"三测试两失败\" 的定性，但同意 margin justification 需要更透明的 external anchoring。\n\n---\n\n**[AGREE with qualification] R1-N3: 因果语言超出证据边界**\n\nR1 指出标题 \"shape\" 和正文 \"channels\"/\"driven\" 暗示因果，而 Limitations item 7 承认 correlational。这一张力确实存在。\n\n但需要注意：BCS-controlled experiments（§4.3）是 **quasi-experimental design**，不是纯观察研究。作者通过 constructing high/low BCS batches while holding count fixed 实现了对 confusability 的 deliberate manipulation。这比 observational correlation 更接近 interventional evidence——虽然不是 randomized controlled trial（因为 BCS 和 type identity/frequency 不能完全解耦），但 within-pool controlled comparison（§4.3, permutation p=0.60）控制了 pool composition confound。\n\nTitle \"Does Type Confusability Shape...\" 是 question form，比 assertion 弱。\"Channel\" terminology 暗示 mechanistic independence，但论文也明确说 NER 中两者 coupled。\n\n**结论**：同意因果语言应进一步软化（建议 \"predict\" 替代 \"driven\"；\"separable predictors\" 替代 \"channels\"），但反驳将此归类为纯观察研究——BCS-controlled design 具有 quasi-experimental 性质。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Multiple comparisons / Rothman stance**\n\n同意。Rothman (1990) 的 \"no correction needed for independent tests\" 适用于 conceptual replications，但论文内部有些 secondary analyses（如 per-prompt-variant correlations, Table in Appendix H.1）是 same-dataset multiple looks，不完全属于 independent replications。论文承认 \"core claims rest on effects reaching p < 0.001\"（Limitations），这是 pragmatic 但非 formal 的保护。\n\n---\n\n**[REBUT] R1-W2: Cross-seed variance 2.7pp vs typical effect 2.2pp**\n\nR1 的比较在量纲上不对等。\n\n根据 Appendix O (main.tex, Table at line 437-447)：\n- Count 16: Batch SD = 0.0626 (6.26pp), Seed SD = 0.0270 (2.70pp), Ratio = 5.4\n\n\"Seed SD = 2.70pp\" 是 3 个 seed 各自产生的 25-batch mean 的标准差。每个 seed 控制的是 **batch composition sampling**（哪些类型组合进同一个 batch），不是模型推理随机性。§3.5 明确说 \"single-seed evaluation with greedy decoding, which eliminates model-level randomness\"——模型推理用 temperature=0 + seed 42，确定性的。\n\n2.70pp seed SD 反映的是：从无限可能的 batch 组合中抽 25 个样本的 sampling variance of the estimator，不是模型 non-determinism。而 2.2pp 是 BCS IQR 对应的 expected accuracy gap（fixed quantity）。这两个数字比较不合理——前者是 estimator uncertainty，后者是 effect size。\n\n进一步证据：count 80 时 Seed SD = 0.88pp（Table row），此时只有一种 batch composition（全 schema），所有 variance 必须来自非 batch 来源——可能是 FP8 量化的微小 non-determinism 或 evaluation sample 的 bootstrap 差异。\n\n**但 R1 提出了一个有效的 implicit concern**：如果 seed SD = 2.7pp 反映 batch sampling noise，而 typical BCS effect = 2.2pp，那么在任意随机 25-batch 样本中，BCS 效应可能被 sampling noise 淹没——这确实限制了 practical detectability。论文的 95% CI [0.4, 4.0] for 2.2pp effect 暗示了这一点（CI 含 near-zero）。\n\n---\n\n**[AGREE] R1-W3: MAVEN 实质不支持核心假设**\n\n完全同意。我在自己的 W5 中已提出相同观点。4 个数据集中：\n- FewRel、DocRED：直接支持（negative BCS slope, significant）\n- Few-NERD batch-level：方向反转（positive r = +0.50/+0.58），需要 type-frequency confound 解释\n- MAVEN per-type：方向反转（positive ρ = +0.184/+0.208），需要 centrality confound 解释\n\n论文依赖 pairwise SCS-confusion correlation 来\"挽救\" Few-NERD 和 MAVEN，但 batch-level prediction（BCS → performance）才是 practitioner 关心的。在这个层面上只有 RE 数据集直接支持。\n\n---\n\n**[AGREE with nuance] R1-W4: NER U-shape mechanistic解释不充分**\n\n同意解释是 speculative。\"Dual-task burden: partial schemas require simultaneous span detection and type-membership filtering; at full-schema, filtering becomes vacuous and recall recovers\" (§6 Discussion) 是合理假设但未被实验验证。\n\n不过，supporting evidence 包括：\n- Per-type extraction recall = 0.586 vs single-pass = 0.368（Table 7, §5）：消除所有 type competition 后 recall 大幅恢复\n- Full-schema recall recovery (0.41 from plateau of 0.27)：当所有类型都在 prompt 中，模型不需要 \"filter membership\"\n- RE 无此 pattern（monotonic decline）：RE 是 closed-set classification，没有 span detection 负担\n\n这些 indirect evidence 使假设 plausible，但确实不构成 definitive mechanism proof。建议作者标注为 hypothesis 而非 established finding。",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-17T07:43:00.668896+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3867
}
```

</details>

---


### Assistant

_source line 652 · 2026-05-17T07:43:08.942630+00:00_

交叉回应已提交。总结：

- **N1** (聚合链): 部分同意叙事有误导性，但反驳核心——batch R²=0.218 是直接观测，不依赖条件化推导
- **N2** (TOST): 反驳"三测两败"的定性——论文明确区分 primary test (PASS) 和 sensitivity checks (underpowered)
- **N3** (因果语言): 同意应软化，但指出 BCS-controlled design 具有 quasi-experimental 性质，非纯观察
- **W1** (Multiple comparisons): 同意
- **W2** (Cross-seed variance): 反驳——2.7pp 是 batch sampling variance，不是 model non-determinism，与 2.2pp effect size 不可直接比较
- **W3** (MAVEN): 完全同意，与我自己 W5 一致
- **W4** (NER U-shape): 同意解释 speculative，但指出 indirect evidence 使其 plausible

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 21

## Round 21

64 recorded events


### User

_source line 653 · 2026-05-17T08:51:32.804187+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2（新颖性 + 写作完整性 + 格式合规）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
- **Deadline**: 2026-05-25
- **页数**: Long paper, 8 页正文 + 无限参考文献
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名**: Double-blind

### 论文路径
- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`
- 补充材料: `projects/schema-dag-extraction/docs/paper/supplementary.tex`
- 各章节: abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex

### 你的审查侧重

**核心任务**: 评估本文的新颖性定位、写作质量和格式合规性。

重点检查：
1. **Novelty & Contribution**:
   - SCS metric 与 LLM-PEE (2025) 的 partitioning criterion 形式相同——论文是否清楚界定了自己的增量（controlled validation vs metric novelty）
   - "首次 controlled study" 的声称是否有 sufficient qualification
   - Contribution list 是否准确反映实际贡献（不过度宣传、不遗漏）
   - 对于一篇 analysis paper（非提出新方法）：findings 是否足够 non-obvious/actionable 来支撑 Main Conference
2. **Related Work completeness**:
   - 是否覆盖所有 direct competitors（特别是 CROSSAGENTIE, LLM-PEE, PARSE, DEE-2024, ZeroNER）
   - 是否有遗漏的重要 related work（structured prediction perspective, label confusion in traditional ML, recent 2025-2026 schema decomposition work）
   - Positioning 是否清楚且公允
3. **写作质量**:
   - Abstract: 是否在 30 秒内传达 problem/method/result；数字密度是否过高
   - Introduction: 叙事线是否连贯；Contribution list 是否简洁（每条 1-2 行 vs 当前长度）
   - AI 写作痕迹: em-dash 使用频率、-ing phrases、过度分段、过渡词堆砌
   - 专有名词首次出现是否有定义
4. **格式合规**:
   - 页数是否 ≤ 8 页（编译验证）
   - 是否有 `\enlargethispage` 或其他 page geometry manipulation
   - Supplementary 是否有 placeholder/incomplete sections
   - 引用格式是否一致（natbib）
   - 图表 caption 是否 self-contained；表格精度是否统一

### 输出格式

请按以下结构输出审稿意见：
```
## Summary (2-3句)
## Strengths (逐条)
## Weaknesses (逐条，标注 [Critical/Warning/Minor])
## Questions (需要作者回答的)
## Missing References (如有)
## Overall Assessment (评分 + 置信度)
## Detailed Comments (逐节)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-17T08:51:42.310029+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-17T08:51:42.711941+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-17T08:51:42.762428+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-17T08:51:43.014105+00:00_

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
17	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
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
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded association ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entro
…[truncated 36215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-17T08:51:48.787426+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-17T08:51:49.844521+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. To our knowledge, we present the first controlled study isolating type confusability from type count in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets. We introduce the Schema Confusability Score (SCS) and two experimental paradigms: count curves (varying schema size while randomizing confusability) and BCS-controlled experiments (fixing size while varying confusability).
3	
4	We identify two degradation dimensions: count-related recall decline and confusability-related type substitution. In typical random batches, confusability accounts for ${\approx}\,2.2$\,pp accuracy difference, markedly smaller than count effects ($-$49\,pp for document-level RE), while batch-level BCS explains 22--53\% of cross-batch variance. The dimensions exhibit bounded association in RE but are coupled in NER where boundary and type ambiguity interact. Effects are directionally consistent across prompt designs and model scales, though Dimension~2 attenuates on smaller models. Schema decomposition via oracle routing recovers substantial RE gains, but confusability-aware grouping yields no significant improvement over random.
5	\end{abstract}
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-17T08:51:49.845000+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-17T08:51:50.397056+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accurac
…[truncated 3429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-17T08:51:50.598012+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-17T08:51:50.598464+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. Recent work also explores LLM-based data annotation for NER \cite{bogdanov2024nuner,zhang2023llmaaa} and self-improving zero-shot extraction \cite{xie2024selfimproving}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. Specifically, LLM-PEE employs union merge across sub-schema extractions, which our \S\ref{sec:sdgd} analysis shows causes precision to collapse from 0.56 to 0.21 in NER as false positives accumulate across passes; RE avoids this because closed-set classification does not require span reconci
…[truncated 2949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-17T08:51:50.849517+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-17T08:51:51.251629+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\
…[truncated 7414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-17T08:51:51.302435+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-17T08:51:52.205889+00:00_

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
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schem
…[truncated 10237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-17T08:51:52.206210+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-17T08:51:52.758377+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets causes precision to collapse (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}), confirming that type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!}{%
19	\beg
…[truncated 501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-17T08:51:52.809040+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-17T08:51:53.160804+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across models, suggesting a difficulty ceiling. RE's separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}). Cross-scale evidence (32B vs.\ 8B) shows Dimension~1 replicates fully while Dimension~2 attenuates on smaller models, dropping to near-zero $R^2$ for NER on Llama-3.1-8B (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}). Count-related degradation may partly reflect prompt length (per-type recall 0.586 vs.\ single-pass 0.368, consistent with lost-in-middle effects; \citealt{lost-in-middle-2024}).
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pair-level effect is modest ($r^2 = 1.3$--$1.7\%$, as ${\sim}89\%$ of pairs never produce mutual confusion); among active-confusion pairs, $R^2 \approx 7\%$ amplifies ${\sim}3\times$ at batch level (Appendix~\ref{app:aggregation-sim}), yielding $R^2$ of 22--53\%. We hypothesize that the NER U-shape (\S\ref{sec:count_curves}) reflects a dual-task burden absent in RE: partial schemas require simultaneous span detection and type-membership filtering; at full-schema, filtering becomes vacuous and recall recovers, confirming task-specific pathways.
9	
10	\section{Conclusion}
11	\label{sec:conclusion}
12	
13	Schema-induced degradation in training-free LLM extraction operates along two dimensions (count-related recall decline, confusability-related type confusion) with bounded association in RE but coupling in NER. Dimension~1 replicates across scales; Dimensio
…[truncated 68 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-17T08:51:53.211449+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-17T08:51:53.664180+00:00_

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
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
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
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}, vLLM \cite{vllm-2023}, a
…[truncated 4443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-17T08:51:53.714801+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-17T08:51:54.217514+00:00_

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
17	\title{Supplementary Material for: Schema-Induced Degradation\\in Training-Free LLM Information Extraction}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\appendix
25	
26	\section{Additional Figures}
27	\label{sec:appendix_figures}
28	
29	\begin{table}[h]
30	\centering
31	\small
32	\begin{tabular}{lrr}
33	\toprule
34	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
35	\midrule
36	1 & 0.702 & 0.640 \\
37	64 & 0.273 & 0.304 \\
38	\midrule
39	Decline & $-$43\,pp & $-$34\,pp \\
40	\bottomrule
41	\end{tabular}
42	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
43	\label{tab:cross_model}
44	\end{table}
45	
46	\begin{table}[h]
47	\centering
48	\small
49	\resizebox{\columnwidth}{!}{%
50	\begin{tabular}{crrrrrr}
51	\toprule
52	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
53	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
54	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
55	\midrule
56	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
57	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
58	\bottomrule
59	\end{tabular}}
60	\caption{Cross-model BCS-controlled FewRel accuracy. 
…[truncated 33588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-17T08:51:54.330268+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 677 · 2026-05-17T08:51:54.384056+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-17T08:52:03.901589+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 679 · 2026-05-17T08:52:04.805571+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ACL Rolling Review reviewer form dimensions soundness novelty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ACL Rolling Review reviewer form dimensions soundness novelty"
  }
}
```

</details>

---


### Tool result

_source line 680 · 2026-05-17T08:52:11.584611+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Here are the key findings from the ACL Rolling Review (ARR) 2025-2026 reviewer guidelines, review form, and scoring criteria:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text 
…[truncated 1347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7683
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-17T08:52:13.643271+00:00_

Web search results for query: "EMNLP 2026 ACL Rolling Review reviewer form dimensions soundness novelty"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"}]

Let me search more specifically for the review form dimensions to get the complete picture.

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclwe
…[truncated 2504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8837
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-17T08:52:17.207565+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 683 · 2026-05-17T08:52:17.560043+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-17T08:52:22.543579+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc), and descriptions of each score level. I need the exact scoring rubric for soundness, excitement, overall recommendation, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc), and descriptions of each score level. I need the exact scoring rubric for soundness, excitement, overall recommendation, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 685 · 2026-05-17T08:52:24.807043+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract all reviewer guidelines, especially: what constitutes a sound paper, how to evaluate novelty/excitement, what are the criteria for recommending accept vs reject, and any specific guidance on analysis papers (non-method papers). Also extract any guidance on how to handle papers with negative results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract all reviewer guidelines, especially: what constitutes a sound paper, how to evaluate novelty/excitement, what are the criteria for recommending accept vs reject, and any specific guidance on analysis papers (non-method papers). Also extract any guidance on how to handle papers with negative results."
  }
}
```

</details>

---


### Tool result

_source line 686 · 2026-05-17T08:52:29.024613+00:00_

# ACL Rolling Review Form Scoring Rubrics

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure...It's unlikely, though conceivable, that I missed something"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## Soundness
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others"

## Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5% papers)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle with substantial revisions
- **1**: Do not resubmit

## Reproducibility
Scale: 1-5
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce the results with some difficulty"
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "They would not be able to reproduce the results"

## Datasets & Software
Scale: 1-5 (identical for both)
- **5**: Enabling research direction changes
- **4**
…[truncated 124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6481
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-17T08:52:32.090069+00:00_

# ARR Reviewer Guidelines: Key Evaluation Criteria

## What Constitutes a Sound Paper

The guidelines emphasize that papers should demonstrate **technical soundness, proof validity, sound argumentation, and novelty**. Reviewers must assess whether authors present sufficient evidence for their claims. The soundness score specifically requires that low ratings be justified by concrete review content—vague assessments are considered violations of reviewer guidelines.

## Novelty and Excitement Evaluation

The guidelines distinguish between two separate dimensions:

**Novelty/Contribution**: Papers must address a clear knowledge gap. The guidelines note that "some findings may seem intuitive but haven't previously been tested empirically," so counterintuitive results don't inherently lack value.

**Excitement**: This is explicitly orthogonal to soundness. As stated, "low soundness scores without sufficient justification could reflect unconscious bias," while excitement reflects "personal taste" and requires no explicit justification.

## Accept vs. Reject Criteria

**Grounds for acceptance**: Papers recommended for publication must be "sufficiently sound and reproducible." The guidelines note that "improvements in efficiency...or creating a high-quality resource" may merit acceptance despite limited novelty if they demonstrate significant impact potential.

**Grounds for rejection or desk-rejection**:
- Hallucinated references or serious anonymity violations
- Missing limitations sections
- Egregious responsible NLP checklist violations
- Critical ethics issues requiring investigation

## Guidance on Negative Results

The guidelines explicitly encourage fair treatment of negative findings: "The bias towards publishing only positive results...contributes to hype. If something systematically does not work...the community needs to know about it." Negative results are legitimate contributions if properly framed and investigated.

## Analysis Papers (Non-Method)

The guideli
…[truncated 263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7283
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-17T08:52:41.232117+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-17T08:52:41.734314+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex:1:% DEPRECATED — this file is no longer included in main.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-17T08:52:42.236450+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-17T08:52:42.788951+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-17T08:52:43.190768+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\enlargethispage",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\enlargethispage",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-17T08:52:43.693430+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-17T08:52:44.798071+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-17T08:52:45.602431+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:222:For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:82:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex:183:For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-17T08:52:46.204522+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\geometry|\\\\setlength|\\\\addtolength.*margin|\\\\vspace\\*?\\{-",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\geometry|\\\\setlength|\\\\addtolength.*margin|\\\\vspace\\*?\\{-",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-17T08:52:46.505702+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/acl.sty:57:  \setlength{\linenumbersep}{1.6cm}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/acl.sty:106:\setlength\columnsep{0.6cm}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/acl.sty:108:\setlength\titlebox{11\baselineskip}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/acl.sty:173:      {\setlength{\rightmargin}{0.6cm}%
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/acl.sty:174:        \setlength{\leftmargin}{0.6cm}}%
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/acl.sty:209: {}{\setlength{\labelwidth}{0pt}\setlength{\leftmargin}{\parindent}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/acl.sty:210: \setlength{\itemindent}{-\parindent}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/acl.sty:226: {}{\setlength{\labelwidth}{0pt}\setlength{\leftmargin}{\parindent}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/acl.sty:227: \setlength{\itemindent}{-\parindent}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex:70:\vspace{-0.5em}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex:79:\vspace{-0.5em}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex:142:\vspace{-0.5em}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex:151:\vspace{-0.5em}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-17T08:52:46.506140+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-17T08:52:46.606899+00:00_

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
…[truncated 5190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-17T08:52:53.095238+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-17T08:52:53.347280+00:00_

1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	% =============================================================================
6	% DIRECT COMPETITORS
7	% =============================================================================
8	
9	@inproceedings{llm-pee-2025,
10	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
11	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
12	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
13	    year      = {2025},
14	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
15	}
16	
17	@inproceedings{parse-2025,
18	    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
19	    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
20	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
21	    year      = {2025},
22	    url       = {https://aclanthology.org/2025.emnlp-industry.184/},
23	}
24	
25	@inproceedings{dee-2024,
26	    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},
27	    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},
28	    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},
29	    year      = {2024},
30	    url       = {https://arxiv.org/abs/2406.01045},
31	}
32	
33	@inproceedings{crossagentie-2025,
34	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
35	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shux
…[truncated 26195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-17T08:52:59.076050+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper to check page count",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
    "description": "Compile LaTeX paper to check page count",
    "timeout": "60000"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-17T08:53:00.482452+00:00_

s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (20 pages, 439339 bytes).
Transcript written on main.log.
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-17T08:53:05.001173+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|page\" | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|page\" | tail -5",
  "description": "Run bibtex and recompile to get correct page count",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|page\" | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|page\" | tail -5",
    "description": "Run bibtex and recompile to get correct page count",
    "timeout": "120000"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-17T08:53:07.611335+00:00_

The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
Warning--can't use both volume and number fields in guo-2021-label-confusion
(There was 1 warning)
Output written on main.pdf (20 pages, 439339 bytes).
Output written on main.pdf (20 pages, 439339 bytes).
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 2610
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-17T08:53:14.996055+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -n \"\\\\[\" main.log | grep -i \"page\\|appendix\\|bibliography\\|checklist\" | head -20; echo \"---\"; grep \"Output written\" main.log",
  "description": "Check page distribution in compiled PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -n \"\\\\[\" main.log | grep -i \"page\\|appendix\\|bibliography\\|checklist\" | head -20; echo \"---\"; grep \"Output written\" main.log",
    "description": "Check page distribution in compiled PDF"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-17T08:53:15.096935+00:00_

grep: main.log: binary file matches
689:[8] (./checklist.tex [9]
---
Output written on main.pdf (20 pages, 439339 bytes).
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-17T08:53:18.513681+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && strings main.log | grep -E \"^\\[[0-9]\" | head -30",
  "description": "Extract page numbers from log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && strings main.log | grep -E \"^\\[[0-9]\" | head -30",
    "description": "Extract page numbers from log"
  }
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-17T08:53:18.615985+00:00_

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
[4]) (./results.tex
[8] (./checklist.tex [9]
[10] [11]
[12]
[13]
[14]
[16])
[17]
[18]
[19]
[20] (./main.aux)
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-17T08:53:22.133507+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 711 · 2026-05-17T08:53:22.133897+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-17T08:53:29.117474+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-17T08:53:33.331428+00:00_

Error: result (6,846,786 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/a11df890-62f8-4148-8571-584ff13b0154/tool-results/mcp-agent-ml-research-pdf_to_images-1779008012848.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/a11df890-62f8-4148-8571-584ff13b0154/tool-results/mcp-agent-ml-research-pdf_to_images-1779008012848.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/a11df890-62f8-4148-8571-584ff13b0154/tool-results/mcp-agent-ml-research-pdf_to_images-1779008012848.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4213
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-17T08:53:37.247035+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "7-9",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "7-9",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-17T08:53:38.189077+00:00_

Error: result (1,999,913 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/a11df890-62f8-4148-8571-584ff13b0154/tool-results/mcp-agent-ml-research-pdf_to_images-1779008018103.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/a11df890-62f8-4148-8571-584ff13b0154/tool-results/mcp-agent-ml-research-pdf_to_images-1779008018103.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/a11df890-62f8-4148-8571-584ff13b0154/tool-results/mcp-agent-ml-research-pdf_to_images-1779008018103.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 942
}
```

</details>

---


### Assistant

_source line 716 · 2026-05-17T08:58:50.580883+00:00_

API Error: Stream idle timeout - partial response received

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 22

## Round 22

8 recorded events


### User

_source line 717 · 2026-05-17T08:59:31.235818+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务（重发）— Reviewer 2（新颖性 + 写作完整性 + 格式合规）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
- **Deadline**: 2026-05-25
- **页数**: Long paper, 8 页正文 + 无限参考文献
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名**: Double-blind

### 论文路径
- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`
- 补充材料: `projects/schema-dag-extraction/docs/paper/supplementary.tex`
- 各章节: abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex

### 你的审查侧重

**核心任务**: 评估本文的新颖性定位、写作质量和格式合规性。

重点检查：
1. **Novelty & Contribution**:
   - SCS metric 与 LLM-PEE (2025) 的 partitioning criterion 形式相同——论文是否清楚界定了自己的增量（controlled validation vs metric novelty）
   - "首次 controlled study" 的声称是否有 sufficient qualification
   - Contribution list 是否准确反映实际贡献（不过度宣传、不遗漏）
   - 对于一篇 analysis paper（非提出新方法）：findings 是否足够 non-obvious/actionable 来支撑 Main Conference
2. **Related Work completeness**:
   - 是否覆盖所有 direct competitors（特别是 CROSSAGENTIE, LLM-PEE, PARSE, DEE-2024, ZeroNER）
   - 是否有遗漏的重要 related work（structured prediction perspective, label confusion in traditional ML, recent 2025-2026 schema decomposition work）
   - Positioning 是否清楚且公允
3. **写作质量**:
   - Abstract: 是否在 30 秒内传达 problem/method/result；数字密度是否过高
   - Introduction: 叙事线是否连贯；Contribution list 是否简洁（每条 1-2 行 vs 当前长度）
   - AI 写作痕迹: em-dash 使用频率、-ing phrases、过度分段、过渡词堆砌
   - 专有名词首次出现是否有定义
4. **格式合规**:
   - 页数是否 ≤ 8 页（编译验证）
   - 是否有 `\enlargethispage` 或其他 page geometry manipulation
   - Supplementary 是否有 placeholder/incomplete sections
   - 引用格式是否一致（natbib）
   - 图表 caption 是否 self-contained；表格精度是否统一

### 输出格式

请按以下结构输出审稿意见：
```
## Summary (2-3句)
## Strengths (逐条)
## Weaknesses (逐条，标注 [Critical/Warning/Minor])
## Questions (需要作者回答的)
## Missing References (如有)
## Overall Assessment (评分 + 置信度)
## Detailed Comments (逐节)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-17T09:01:03.040595+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && strings main.log | grep -E \"^\\[|\\.tex\\)\" | head -40",
  "description": "Check page breaks in compilation log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && strings main.log | grep -E \"^\\[|\\.tex\\)\" | head -40",
    "description": "Check page breaks in compilation log"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-17T09:01:03.243021+00:00_

[Loading MPS to PDF converter (version 2006.09.02).]
) (./abstract.tex)
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
[]\T1/ptm/m/n/10 (-20) Table 1: |Dataset statis-tics. BCS Range in-di-cates the
[4]) (./results.tex
) (./sdgd_negative.tex) (./discussion.tex [7 <../../figures/paper/fig_error_tax
[8] (./checklist.tex [9]
[]\T1/ptm/m/n/10.95 (+20) Yes. 
[][]3.3[][] de-scribes both ex-per-i-men-tal
[]\T1/ptm/m/n/10 (+20) Dhananjay Ashok and Zachary C. Lip-ton. 2023.
[10] [11]
[12]
[]\T1/ptm/m/n/10 (+20) Dong Zhao, Yadong Wang, Xi-ang Chen, Chenxi
[]\T1/ptm/m/n/10.95 (+20) Single-pass ex-trac-tion achieves F1=0.445
[13]
[14]
[16])
[17]
[18]
[][]4.3[][]), we com-pute
[19]
[] \OT1/cmr/m/n/10.95 = \OML/cmm/m/it/10.95 ^^L[] \OT1/cmr/m/n/10.95 + \OML/cmm
[]\T1/ptm/m/n/10.95 (+20) Pairwise SCS dis-tri-bu-tions do not dif-
[20] (./main.aux)
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-17T09:03:57.906051+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 721 · 2026-05-17T09:03:57.956620+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-17T09:05:29.544570+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿完成\n\n### 审查侧重：新颖性 + 写作完整性 + 格式合规\n\n---\n\n## Summary (2-3句)\n\n本文通过 stratified 实验设计，将 zero-shot LLM IE 中 schema 复杂度引起的性能退化分解为两个维度：type count（主导因素）和 type confusability（次要因素）。SCS/BCS 指标本身与 LLM-PEE (2025) 形式相同，论文的核心贡献是 controlled validation framework 而非新指标。研究方法论严谨，但 pairwise 效应量极小（r² = 1.3–1.7%），加上 schema decomposition 全面失败的负结果，使得 actionable takeaway 有限。\n\n---\n\n## Strengths (逐条)\n\n**S1. 方法论严谨性突出。** BCS-controlled 设计、within-pool 控制、permutation tests、TOST 等价检验、cross-seed variance decomposition、多种 robustness checks 构成了 NLP 实证研究的高水准范例。对 centrality confound 的识别和处理（§4.5、Appendix F）尤为精彩。\n\n**S2. 负结果的诊断价值高。** SDGD 失败的根因分析（merge amplification 导致 precision 崩塌；constrained decoding 消除 confidence signal 使 routing 失效）是 genuinely useful 的发现，可帮助社区避免重复踩坑。\n\n**S3. Confound 处理透明。** 论文主动识别并讨论了多个潜在混淆因素：type frequency、centrality、data contamination（FewRel train/val split）、prompt sensitivity、embedding anisotropy。Limitations 部分极为详尽（8项），体现高度学术诚实。\n\n**S4. 实验覆盖面合理。** 覆盖 NER/RE/ED 三任务、四数据集、两模型规模、多 prompt 变体，结论的 generalizability 得到一定支撑。\n\n**S5. Related Work positioning 诚实。** \"SCS novelty\" 段落明确承认与 LLM-PEE 形式相同，将自身贡献限定为 controlled validation。这种坦诚值得肯定。\n\n---\n\n## Weaknesses (逐条)\n\n**W1 [Critical] 核心效应量过小，practical significance 存疑。**\n- 具体位置：§4.2 Table 2, §4.3 \"Practical magnitude\" paragraph\n- 问题：Pairwise r² = 1.3–1.7%；typical-batch gap 仅 2.2 pp（95% CI [0.4, 4.0]）。论文试图通过 Cohen (1988) 的\"small but real\"标准和 batch-level amplification (R² = 0.22) 来辩护，但 2.2 pp 的 typical gap 在实际部署中几乎不可察觉。Extreme-batch gap（31.2 pp）虽大，但依赖人为极端化 BCS，real-world schema 不太可能出现如此极端的 composition。\n- 为什么影响接收：对于 analysis paper，findings 必须 non-obvious 或 actionable。\"Confusability 有 statistically significant 但 practically negligible 的影响\"这一结论，虽然方法论上严格，但对 practitioner 的指导价值有限。\n- 建议：需更强的论证说明何种场景下 2.2 pp 的 gap 具有实际意义，或者承认 main finding 实际上是\"count 才是瓶颈，confusability 可忽略\"。\n\n**W2 [Critical] Abstract 和 Introduction 信息过载，叙事不清晰。**\n- 具体位置：abstract.tex 全文，introduction.tex \"Our experiments yield five findings\" 段落\n- 问题：\n  - Abstract 在 ~170 words 内塞入\"2.2 pp\"、\"−49 pp\"、\"22–53%\"、\"+29.8 pp\"、\"TOST\"等密集数字和未定义术语。BCS 在 abstract 中首次出现时仅说\"BCS-controlled experiments\"，未展开为 Batch Confusability Score。\n  - Introduction 的\"五个发现\"段落是一个 ~100 词的单句，包含 5 个嵌套子句和大量括号注释，极难一次读懂。\n  - Contribution list 4 条各 2-3 行、内嵌具体数字和 section 引用，读起来像 result summary 而非 contribution statement。\n- 为什么影响接收：审稿人在 abstract/intro 阶段判断论文价值。当前密度会导致核心 message 被淹没。\n- 建议：(1) Abstract 删减数字到 2-3 个关键数据点；(2) 展开 BCS 缩写；(3) 将\"五个发现\"拆成 5 个独立短句；(4) Contribution list 每条压缩到 1 行。\n\n**W3 [Warning] Analysis paper 的 novelty bar 问题。**\n- 具体位置：§1 \"To our knowledge, we present the first controlled study...\"\n- 问题：核心 metric (SCS = cosine similarity of type embeddings) 非新，实验设计（stratified batching by similarity）属于标准实验方法论应用。论文的主要\"发现\"可总结为：(a) count 比 confusability 重要 ~20x（somewhat expected），(b) embedding similarity weakly predicts confusion（r² < 2%，量级上 not actionable），(c) decomposition 失败（useful but narrow）。对于 EMNLP Main Conference，通常期望 analysis paper 揭示 counter-intuitive findings 或提供 actionable design principles。\n- 为什么影响评分：Excitement 维度将受限。如果 reviewer 认为\"count dominates\"是 expected result，则贡献进一步缩水。\n- 建议：强化 non-obvious 发现的 framing（例如 merge amplification 机制、centrality confound 的 methodological contribution），将 paper narrative 从\"SCS predicts confusion\"转向\"why decomposition fails and what this means for the field\"。\n\n**W4 [Warning] NER 结果在 batch-level 与 pairwise-level 方向矛盾，解释不完全令人信服。**\n- 具体位置：§4.3 prompt sensitivity paragraph, Appendix H NER paragraph\n- 问题：NER batch-level BCS–F1 correlation 为正（r = +0.50 to +0.58），与 confusability hypothesis 预测的负方向相反。论文归因于 type-frequency confound，并依赖 pairwise analysis 作为\"primary evidence\"。但这意味着 BCS 在 NER 上不是一个 reliable pre-hoc predictor——方向都是错的。Contribution 3 声称\"BCS generalizes across RE tasks and schema sizes\"但添加了 caveat \"applicability to span-level tasks requires confound adjustment\"，这实质上限制了 BCS 的 generalizability 到仅 RE。\n- 为什么影响评分：Contribution 3 的 claim scope 与实际证据不匹配。\n- 建议：Contribution 3 应明确限定为 RE-specific finding，或提供 NER 上 confound-adjusted BCS 的结果。\n\n**W5 [Warning] Supplementary 与 main.tex Appendix 内容完全重复。**\n- 具体位置：main.tex (lines 63-462, \\appendix section) vs. supplementary.tex\n- 问题：main.tex 编译后 appendix 占 pages 10-20，supplementary.tex 是同一内容的独立编译版本。两者同时存在造成冗余且可能混淆 reviewers。\n- 建议：删除其中一份。建议保留 main.tex 内的 appendix，删除独立 supplementary.tex。\n\n**W6 [Minor] TOST 等价检验术语未展开定义。**\n- 具体位置：§4.4 \"TOST equivalence testing\"，Abstract\n- 问题：\"TOST\" (Two One-Sided Tests) 在正文首次出现时未展开。NLP 社区对此统计方法不一定熟悉。\n- 建议：正文首次使用时写\"Two One-Sided Tests (TOST) equivalence testing\"。\n\n**W7 [Minor] Contribution 措辞像 result summary 而非 contribution statement。**\n- 具体位置：introduction.tex L17-22\n- 问题：每条 Contribution 以 bold finding 开头（如\"Count dominates confusability by ~20× in typical batches\"），接着是具体实验数字。标准 contribution 写法应更 general。\n- 建议：将 Contribution list 改为方法论/框架层面的贡献描述，简洁到每条 1 行。\n\n**W8 [Minor] Discussion/Conclusion 过于简短。**\n- 具体位置：discussion.tex 全文（~14 行 + 2 句 conclusion）\n- 问题：对于 8 页 analysis paper，Discussion 是综合 findings 为 broader insights 的关键位置。当前不到 1/4 column。缺少：practitioner 的 actionable recommendations、与 training-based IE 的对比、metric 改进方向。\n- 建议：扩展 Discussion 到至少 1/2 column。\n\n---\n\n## Questions (需要作者回答的)\n\n**Q1.** Typical-batch gap 为 2.2 pp。在什么实际应用场景下，这个量级的 confusability effect 值得 schema designer 投入精力去优化？\n\n**Q2.** BCS 在 NER 上方向为正。如果对 type-frequency 做 partial correlation 控制后，batch-level BCS–F1 correlation 变为什么方向和量级？\n\n**Q3.** Table 5 显示 confusability-aware grouping 仅比 random +1.4 pp (n.s.)。是否做过 oracle routing + random grouping vs oracle routing + confusability-aware grouping 的 comparison？\n\n**Q4.** Contribution 2 使用\"predicts\"（\"embedding similarity predicts type confusion\"）。鉴于 Limitations §7 承认\"correlational evidence\"，是否应改为\"is correlated with\"？\n\n**Q5.** FewRel (2018) data contamination：Qwen3 technical report 是否有关于 pretraining data composition 的信息可直接排除？\n\n---\n\n## Missing References\n\n1. **Prompt-length confound**: Levy et al. (2024) \"Same Task, More Tokens\" — count 和 prompt length 完全 confounded，需加强 alternative explanation 讨论。\n2. **Extreme multi-label classification with label embeddings**: Bhatia et al. (2015) 等 — structured prediction 中 label similarity 影响分类的前例。\n3. **LLM iterative refinement**: GenRES (NAACL 2025), ULTRA (2025) 等近期 schema-aware extraction 工作。\n\n---\n\n## Overall Assessment\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 方法论严谨，统计处理规范，主要 claim 有充分支撑。NER batch-level 矛盾处理略弱 |\n| Excitement | 2.5/5 | Analysis paper 无新方法。核心发现 surprise factor 有限，effect size 过小 |\n| Reproducibility | 4.5/5 | 实验细节详尽，prompt templates 完整，承诺代码 release |\n| Clarity | 3/5 | 方法和结果写作清晰，但 Abstract/Introduction 过密影响 accessibility |\n\n**Overall Recommendation: 3/5 (Borderline)**\n\n**置信度: 4/5 (高)**\n\n**核心判断**：方法论严谨的 analysis paper，但 practical significance 与 novelty 的结合度不足以 strongly support Main Conference。Effect size 极小（typical gap 2.2 pp），SCS metric 非新，BCS 仅在 RE 上可靠，核心 insight（count dominates）somewhat expected。最强贡献（merge amplification 诊断、centrality confound）可能更适合 Findings track。\n\n---\n\n### 格式合规检查结果\n\n| 检查项 | 结果 |\n|--------|------|\n| 页数 ≤ 8 (正文) | ✓ 合规 — 编译确认 Sections 1-7 在 page 7-8 结束，Limitations 不计入 |\n| \\enlargethispage | ✓ 未使用 |\n| Page geometry manipulation | ✓ 仅 prompt_appendix.tex 中 \\vspace{-0.5em}（在 appendix，可接受） |\n| Anonymous (double-blind) | ✓ author = \"Anonymous\"，anonymous.4open.science URL |\n| \\usepackage[review]{acl} | ✓ 正确 |\n| Em-dash 使用 | ✓ 正文无解释性 em-dash（仅废弃文件 conclusion.tex 注释中有 1 处） |\n| 引用格式 (natbib) | ✓ 一致。bibtex warning: guo-2021 volume+number 冲突（minor） |\n| 图表 caption self-contained | ✓ Figure 1, Figure 2, 各 Table caption 均含足够上下文 |\n| 表格精度统一 | ✓ 各表内部统一 |\n| Supplementary 完整性 | ⚠️ 与 main appendix 完全重复，应删除一份 |",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿完成\n\n### 审查侧重：新颖性 + 写作完整性 + 格式合规\n\n---\n\n## Summary (2-3句)\n\n本文通过 stratified 实验设计，将 zero-shot LLM IE 中 schema 复杂度引起的性能退化分解为两个维度：type count（主导因素）和 type confusability（次要因素）。SCS/BCS 指标本身与 LLM-PEE (2025) 形式相同，论文的核心贡献是 controlled validation framework 而非新指标。研究方法论严谨，但 pairwise 效应量极小（r² = 1.3–1.7%），加上 schema decomposition 全面失败的负结果，使得 actionable takeaway 有限。\n\n---\n\n## Strengths (逐条)\n\n**S1. 方法论严谨性突出。** BCS-controlled 设计、within-pool 控制、permutation tests、TOST 等价检验、cross-seed variance decomposition、多种 robustness checks 构成了 NLP 实证研究的高水准范例。对 centrality confound 的识别和处理（§4.5、Appendix F）尤为精彩。\n\n**S2. 负结果的诊断价值高。** SDGD 失败的根因分析（merge amplification 导致 precision 崩塌；constrained decoding 消除 confidence signal 使 routing 失效）是 genuinely useful 的发现，可帮助社区避免重复踩坑。\n\n**S3. Confound 处理透明。** 论文主动识别并讨论了多个潜在混淆因素：type frequency、centrality、data contamination（FewRel train/val split）、prompt sensitivity、embedding anisotropy。Limitations 部分极为详尽（8项），体现高度学术诚实。\n\n**S4. 实验覆盖面合理。** 覆盖 NER/RE/ED 三任务、四数据集、两模型规模、多 prompt 变体，结论的 generalizability 得到一定支撑。\n\n**S5. Related Work positioning 诚实。** \"SCS novelty\" 段落明确承认与 LLM-PEE 形式相同，将自身贡献限定为 controlled validation。这种坦诚值得肯定。\n\n---\n\n## Weaknesses (逐条)\n\n**W1 [Critical] 核心效应量过小，practical significance 存疑。**\n- 具体位置：§4.2 Table 2, §4.3 \"Practical magnitude\" paragraph\n- 问题：Pairwise r² = 1.3–1.7%；typical-batch gap 仅 2.2 pp（95% CI [0.4, 4.0]）。论文试图通过 Cohen (1988) 的\"small but real\"标准和 batch-level amplification (R² = 0.22) 来辩护，但 2.2 pp 的 typical gap 在实际部署中几乎不可察觉。Extreme-batch gap（31.2 pp）虽大，但依赖人为极端化 BCS，real-world schema 不太可能出现如此极端的 composition。\n- 为什么影响接收：对于 analysis paper，findings 必须 non-obvious 或 actionable。\"Confusability 有 statistically significant 但 practically negligible 的影响\"这一结论，虽然方法论上严格，但对 practitioner 的指导价值有限。\n- 建议：需更强的论证说明何种场景下 2.2 pp 的 gap 具有实际意义，或者承认 main finding 实际上是\"count 才是瓶颈，confusability 可忽略\"。\n\n**W2 [Critical] Abstract 和 Introduction 信息过载，叙事不清晰。**\n- 具体位置：abstract.tex 全文，introduction.tex \"Our experiments yield five findings\" 段落\n- 问题：\n  - Abstract 在 ~170 words 内塞入\"2.2 pp\"、\"−49 pp\"、\"22–53%\"、\"+29.8 pp\"、\"TOST\"等密集数字和未定义术语。BCS 在 abstract 中首次出现时仅说\"BCS-controlled experiments\"，未展开为 Batch Confusability Score。\n  - Introduction 的\"五个发现\"段落是一个 ~100 词的单句，包含 5 个嵌套子句和大量括号注释，极难一次读懂。\n  - Contribution list 4 条各 2-3 行、内嵌具体数字和 section 引用，读起来像 result summary 而非 contribution statement。\n- 为什么影响接收：审稿人在 abstract/intro 阶段判断论文价值。当前密度会导致核心 message 被淹没。\n- 建议：(1) Abstract 删减数字到 2-3 个关键数据点；(2) 展开 BCS 缩写；(3) 将\"五个发现\"拆成 5 个独立短句；(4) Contribution list 每条压缩到 1 行。\n\n**W3 [Warning] Analysis paper 的 novelty bar 问题。**\n- 具体位置：§1 \"To our knowledge, we present the first controlled study...\"\n- 问题：核心 metric (SCS = cosine similarity of type embeddings) 非新，实验设计（stratified batching by similarity）属于标准实验方法论应用。论文的主要\"发现\"可总结为：(a) count 比 confusability 重要 ~20x（somewhat expected），(b) embedding similarity weakly predicts confusion（r² < 2%，量级上 not actionable），(c) decomposition 失败（useful but narrow）。对于 EMNLP Main Conference，通常期望 analysis paper 揭示 counter-intuitive findings 或提供 actionable design principles。\n- 为什么影响评分：Excitement 维度将受限。如果 reviewer 认为\"count dominates\"是 expected result，则贡献进一步缩水。\n- 建议：强化 non-obvious 发现的 framing（例如 merge amplification 机制、centrality confound 的 methodological contribution），将 paper narrative 从\"SCS predicts confusion\"转向\"why decomposition fails and what this means for the field\"。\n\n**W4 [Warning] NER 结果在 batch-level 与 pairwise-level 方向矛盾，解释不完全令人信服。**\n- 具体位置：§4.3 prompt sensitivity paragraph, Appendix H NER paragraph\n- 问题：NER batch-level BCS–F1 correlation 为正（r = +0.50 to +0.58），与 confusability hypothesis 预测的负方向相反。论文归因于 type-frequency confound，并依赖 pairwise analysis 作为\"primary evidence\"。但这意味着 BCS 在 NER 上不是一个 reliable pre-hoc predictor——方向都是错的。Contribution 3 声称\"BCS generalizes across RE tasks and schema sizes\"但添加了 caveat \"applicability to span-level tasks requires confound adjustment\"，这实质上限制了 BCS 的 generalizability 到仅 RE。\n- 为什么影响评分：Contribution 3 的 claim scope 与实际证据不匹配。\n- 建议：Contribution 3 应明确限定为 RE-specific finding，或提供 NER 上 confound-adjusted BCS 的结果。\n\n**W5 [Warning] Supplementary 与 main.tex Appendix 内容完全重复。**\n- 具体位置：main.tex (lines 63-462, \\appendix section) vs. supplementary.tex\n- 问题：main.tex 编译后 appendix 占 pages 10-20，supplementary.tex 是同一内容的独立编译版本。两者同时存在造成冗余且可能混淆 reviewers。\n- 建议：删除其中一份。建议保留 main.tex 内的 appendix，删除独立 supplementary.tex。\n\n**W6 [Minor] TOST 等价检验术语未展开定义。**\n- 具体位置：§4.4 \"TOST equivalence testing\"，Abstract\n- 问题：\"TOST\" (Two One-Sided Tests) 在正文首次出现时未展开。NLP 社区对此统计方法不一定熟悉。\n- 建议：正文首次使用时写\"Two One-Sided Tests (TOST) equivalence testing\"。\n\n**W7 [Minor] Contribution 措辞像 result summary 而非 contribution statement。**\n- 具体位置：introduction.tex L17-22\n- 问题：每条 Contribution 以 bold finding 开头（如\"Count dominates confusability by ~20× in typical batches\"），接着是具体实验数字。标准 contribution 写法应更 general。\n- 建议：将 Contribution list 改为方法论/框架层面的贡献描述，简洁到每条 1 行。\n\n**W8 [Minor] Discussion/Conclusion 过于简短。**\n- 具体位置：discussion.tex 全文（~14 行 + 2 句 conclusion）\n- 问题：对于 8 页 analysis paper，Discussion 是综合 findings 为 broader insights 的关键位置。当前不到 1/4 column。缺少：practitioner 的 actionable recommendations、与 training-based IE 的对比、metric 改进方向。\n- 建议：扩展 Discussion 到至少 1/2 column。\n\n---\n\n## Questions (需要作者回答的)\n\n**Q1.** Typical-batch gap 为 2.2 pp。在什么实际应用场景下，这个量级的 confusability effect 值得 schema designer 投入精力去优化？\n\n**Q2.** BCS 在 NER 上方向为正。如果对 type-frequency 做 partial correlation 控制后，batch-level BCS–F1 correlation 变为什么方向和量级？\n\n**Q3.** Table 5 显示 confusability-aware grouping 仅比 random +1.4 pp (n.s.)。是否做过 oracle routing + random grouping vs oracle routing + confusability-aware grouping 的 comparison？\n\n**Q4.** Contribution 2 使用\"predicts\"（\"embedding similarity predicts type confusion\"）。鉴于 Limitations §7 承认\"correlational evidence\"，是否应改为\"is correlated with\"？\n\n**Q5.** FewRel (2018) data contamination：Qwen3 technical report 是否有关于 pretraining data composition 的信息可直接排除？\n\n---\n\n## Missing References\n\n1. **Prompt-length confound**: Levy et al. (2024) \"Same Task, More Tokens\" — count 和 prompt length 完全 confounded，需加强 alternative explanation 讨论。\n2. **Extreme multi-label classification with label embeddings**: Bhatia et al. (2015) 等 — structured prediction 中 label similarity 影响分类的前例。\n3. **LLM iterative refinement**: GenRES (NAACL 2025), ULTRA (2025) 等近期 schema-aware extraction 工作。\n\n---\n\n## Overall Assessment\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 方法论严谨，统计处理规范，主要 claim 有充分支撑。NER batch-level 矛盾处理略弱 |\n| Excitement | 2.5/5 | Analysis paper 无新方法。核心发现 surprise factor 有限，effect size 过小 |\n| Reproducibility | 4.5/5 | 实验细节详尽，prompt templates 完整，承诺代码 release |\n| Clarity | 3/5 | 方法和结果写作清晰，但 Abstract/Introduction 过密影响 accessibility |\n\n**Overall Recommendation: 3/5 (Borderline)**\n\n**置信度: 4/5 (高)**\n\n**核心判断**：方法论严谨的 analysis paper，但 practical significance 与 novelty 的结合度不足以 strongly support Main Conference。Effect size 极小（typical gap 2.2 pp），SCS metric 非新，BCS 仅在 RE 上可靠，核心 insight（count dominates）somewhat expected。最强贡献（merge amplification 诊断、centrality confound）可能更适合 Findings track。\n\n---\n\n### 格式合规检查结果\n\n| 检查项 | 结果 |\n|--------|------|\n| 页数 ≤ 8 (正文) | ✓ 合规 — 编译确认 Sections 1-7 在 page 7-8 结束，Limitations 不计入 |\n| \\enlargethispage | ✓ 未使用 |\n| Page geometry manipulation | ✓ 仅 prompt_appendix.tex 中 \\vspace{-0.5em}（在 appendix，可接受） |\n| Anonymous (double-blind) | ✓ author = \"Anonymous\"，anonymous.4open.science URL |\n| \\usepackage[review]{acl} | ✓ 正确 |\n| Em-dash 使用 | ✓ 正文无解释性 em-dash（仅废弃文件 conclusion.tex 注释中有 1 处） |\n| 引用格式 (natbib) | ✓ 一致。bibtex warning: guo-2021 volume+number 冲突（minor） |\n| 图表 caption self-contained | ✓ Figure 1, Figure 2, 各 Table caption 均含足够上下文 |\n| 表格精度统一 | ✓ 各表内部统一 |\n| Supplementary 完整性 | ⚠️ 与 main appendix 完全重复，应删除一份 |",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-17T09:05:33.460593+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Assistant

_source line 724 · 2026-05-17T09:05:39.259560+00:00_

Round 1 审稿完成，已提交给 Review Director。

核心结论：**Borderline (3/5)**。方法论严谨（Soundness 4/5），但 excitement 受限（2.5/5）——效应量过小（typical gap 仅 2.2 pp）、SCS 非新指标、BCS 仅 RE 上可靠、核心 finding（count dominates）somewhat expected。最有价值的贡献是 merge amplification 诊断和 centrality confound 识别。建议作者 reframe narrative 以强化 non-obvious findings，或考虑 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 23

## Round 23

4 recorded events


### User

_source line 725 · 2026-05-17T09:06:34.762523+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1（方法严谨性 + 统计证据）的完整审稿原文。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注你与 R1 在以下问题上是否一致：
1. TOST margin 选择问题
2. Pair-to-batch aggregation 的 conditioning bias
3. NER Dimension 2 的 batch-level 证据方向
4. Effect size 的 practical significance

---

## Reviewer 1 完整审稿意见

### Weaknesses

**W1 [Critical] TOST equivalence margin (±3pp) 相对于 main effect (2.2pp) 过于宽松。**
- ±3pp margin 是 typical-batch main effect (2.2pp) 的 136%。即使交互达到 3pp（超过 main effect 本身），TOST 仍会判定"等价"。在 ±1pp，equivalence inconclusive (p=0.278)。论文自身承认 "a 3pp interaction atop the 2.2pp confusability main effect would represent >130% amplification"。
- Separability claim 是贡献 1 的核心。如果 interaction 可能达到 main effect 的 ~50%（±1pp inconclusive），则 "bounded association" 的强度被高估。

**W2 [Critical] Pair-to-batch R² 聚合依赖于 conditioning on non-zero confusion pairs。**
- Monte Carlo simulation 用 conditional R²=7%（仅限非零 confusion pairs，约占 11%）预测 batch R²=0.219，精确匹配观测值 0.218。但 unconditional R²=1.3% 时模拟仅产生 R²=0.044。
- 这是 post-hoc conditioning on the dependent variable：先选出实际产生 confusion 的 pairs，再衡量 SCS 对 confusion 量的预测力。
- 如果 SCS 的 unconditional 预测力只能解释 batch-level 4.4% variance（而非 22%），则 BCS 作为 "pre-hoc screening metric" 的实用价值被夸大。

**W3 [Critical] NER 的 Dimension 2 证据实质上弱于 RE，但 claim 未做充分区分。**
- NER batch-level BCS-F1 correlation 为正向 (r = +0.50 v1, +0.58 v2)，与 confusability hypothesis 预测方向相反。
- Pairwise r²=1.3% 的实际意义有限；batch-level（与部署相关的粒度）方向相反意味着 confusability 在 NER 中被 frequency 效应掩盖甚至逆转。
- 论文 title 和 abstract 泛化地讨论 "NER, RE, and event detection"，但 Dimension 2 的 practical relevance（batch-level）仅 RE 支持。

**W4 [Warning] Title 中的 "Shape" 超出证据支持的因果边界。**
- Correlational + quasi-experimental stratification 支持 "predict" 或 "associate with"，但不支持 "shape"。
- Limitations 明确承认 "does not establish interventional causality"。

**W5 [Warning] Cross-model validation 覆盖不足。**
- 仅 Qwen3-32B + Llama-3.1-8B。Dimension 2 在 8B NER 上 near-zero，无 proprietary model 验证。

**W6 [Warning] FewRel train+val split 合并的 contamination 风险处理。**
- Split-origin covariate analysis: p=0.06 接近 threshold；contaminated types 可能是 high-frequency Wikidata relations（也是 high-BCS），产生非均匀效应。

**W7 [Warning] 1000 instances 对 long-tail types 的充分性。**
- 低频 types 可能只有个位数 instances，pairwise confusion rate 估计极不稳定。

**W8 [Warning] Prompt variant analysis power 不足。**
- 每个 condition 仅 n=10 batches。Count 8 下所有 4 个 variant 均 non-significant。Count 32 有 2/4 达 p<0.05 但未 apply multiple comparison correction。

### Questions
- Q1: Within-pool quartile CI [-8.17, +0.38] 包含零——能否作为 Dimension 2 的证据？
- Q2: NER 是否尝试过 frequency-residualized BCS？
- Q3: Monte Carlo simulation 的参数估计是否 circular？
- Q4: FP8 + vLLM 的非确定性（seed SD at count 80 = 0.88pp）如何解释？
- Q5: TOST 是否在 raw accuracy scale 上计算（floor effects 可能压缩 interaction）？

### Overall: 3.5 (Borderline Conference / strong Findings)

---

请对以上每个 Weakness (W1-W8) 和 Questions (Q1-Q5) 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-17T09:08:57.587474+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: TOST margin ±3pp 相对于 main effect 过于宽松。**\n\n同意这是实质性问题。Typical-batch main effect 仅 2.2 pp，±3pp margin 允许 interaction 达 main effect 的 136% 仍判定\"等价\"。Appendix C Table 6 显示 ±1pp 时 inconclusive (p=0.278)，无法排除 interaction 达 main effect ~50%。这直接弱化 Contribution 1 的 \"two separable dimensions\" 叙事。与我的 W1（effect size 过小）相互加强：当 main effect 只有 2.2 pp 时，separability 的实践意义也随之削弱。\n\n---\n\n**[AGREE with nuance] R1-W2: Pair-to-batch conditioning bias。**\n\n同意 conditioning on non-zero confusion pairs 是 post-hoc selection。但有重要 nuance：论文 Appendix G 开头声明 \"It is not the evidence base for our claims; the observed batch-level R²=0.218 (§4.3) is a direct empirical measurement independent of this simulation.\" Batch-level R²=0.22 是直接测量，不依赖 simulation。\n\n真正问题在 framing：论文应更清楚区分（a）BCS 作为 batch-level descriptor 解释 22% variance（直接测量，valid）和（b）SCS 作为 pair-level pre-hoc predictor 仅解释 1.3% variance（practitioner 实际能用的值）。当前 narrative 倾向让 reader 记住 \"22%\" 而淡化 \"1.3%\"，构成 misleading framing。\n\n---\n\n**[AGREE] R1-W3: NER Dimension 2 证据弱于 RE，claim 未充分区分。**\n\n强烈同意，与我的 W4 完全一致。NER batch-level BCS–F1 方向为正（与 hypothesis 相反），MAVEN per-type BCS–F1 被 centrality confound 完全解释（Appendix F, partial r non-significant）。Dimension 2 在实际可用粒度（batch-level）上仅 FewRel + DocRED（同属 RE）支持。论文 title/abstract 给人 cross-task generalization 印象，但证据不支持。\n\n---\n\n**[AGREE] R1-W4: Title \"Shape\" 暗示因果性。**\n\n同意。虽 title 用问句形式提供缓冲，但论文内部多处使用 \"predicts\"（Contribution 2），结合 Limitations §7 承认 \"does not establish interventional causality\"，存在不匹配。建议改为 \"predict\" 或 \"associate with\"。与我的 Q4 一致。\n\n---\n\n**[AGREE with qualification] R1-W5: Cross-model validation 不足。**\n\n同意方向但 severity 略低。对 analysis paper，2 个不同 family + 不同 scale 提供 reasonable initial evidence。但缺少 proprietary model 验证是 gap，这些模型可能有不同的 type-resolution mechanism。论文 Limitations §1 已明确承认。\n\n---\n\n**[AGREE with qualification] R1-W6: FewRel contamination。**\n\n部分同意 concern valid，但论文 defense 是多线的（Appendix I）：BCS partial effect unchanged、monotonic curve、DocRED replication。Collectively reasonable defense，不构成 critical weakness。\n\n---\n\n**[AGREE] R1-W7: 1000 instances 对 long-tail types 充分性。**\n\n同意。Few-NERD 的 long-tail distribution 意味着某些 types 可能个位数 instances。Type-level cluster bootstrap CI（Table 2）部分 addresses 但不完全解决。\n\n---\n\n**[AGREE with nuance] R1-W8: Prompt variant power 不足。**\n\n同意 n=10 underpowered 且无 multiple comparison correction。但论文定位为 robustness check（非 primary evidence），4/4 方向一致是 informative。Count 8 全部 n.s. 的观察重要：confusability effect 可能仅 large schema 时 detectable，进一步限制 practical applicability。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1**: Within-pool quartile CI 确实包含零，但 regression slope p=0.027 显著。论文已有 caveat。\n\n**[AGREE] R1-Q2**: Frequency-residualized BCS for NER 是明显遗漏。MAVEN 有此分析（Appendix F）但 Few-NERD 没有。这是我的 W4/Q2 的核心。\n\n**[AGREE with nuance] R1-Q3**: Simulation 参数有 circularity 但论文声明 \"illustrative, not evidence base\"。删除 simulation 不影响 R²=0.218 直接测量。\n\n**[AGREE] R1-Q4**: Seed SD=0.88pp 在 greedy mode 下不应存在。\"Eliminates randomness\" 措辞应修正。\n\n**[AGREE] R1-Q5**: Floor effect (~51% at high-BCS) 可能压缩 interaction 空间，TOST 在 logit scale 上可能给出不同结论。Valid methodological concern。\n\n---\n\n### 与 R1 的核心分歧\n\n**一致点**：W1 (TOST), W3 (NER Dimension 2), W4 (causality), Q2 (frequency-residualized NER)\n\n**Severity 分歧**：R1 给 3.5，我给 3。我认为 novelty/excitement deficit（我的 W3）是比 statistical subtleties 更大的 acceptance barrier。论文的统计工作 above-average 严谨（我的 S1），但\"发现了一个 r²=1.3% 的 effect\"这个 story 本身的 Main Conference worthiness 是根本问题。R1 的统计质疑如果得到解决（更严格的 TOST、frequency-residualized NER BCS），可能提高 soundness score，但不改变 excitement 评估。",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: TOST margin ±3pp 相对于 main effect 过于宽松。**\n\n同意这是实质性问题。Typical-batch main effect 仅 2.2 pp，±3pp margin 允许 interaction 达 main effect 的 136% 仍判定\"等价\"。Appendix C Table 6 显示 ±1pp 时 inconclusive (p=0.278)，无法排除 interaction 达 main effect ~50%。这直接弱化 Contribution 1 的 \"two separable dimensions\" 叙事。与我的 W1（effect size 过小）相互加强：当 main effect 只有 2.2 pp 时，separability 的实践意义也随之削弱。\n\n---\n\n**[AGREE with nuance] R1-W2: Pair-to-batch conditioning bias。**\n\n同意 conditioning on non-zero confusion pairs 是 post-hoc selection。但有重要 nuance：论文 Appendix G 开头声明 \"It is not the evidence base for our claims; the observed batch-level R²=0.218 (§4.3) is a direct empirical measurement independent of this simulation.\" Batch-level R²=0.22 是直接测量，不依赖 simulation。\n\n真正问题在 framing：论文应更清楚区分（a）BCS 作为 batch-level descriptor 解释 22% variance（直接测量，valid）和（b）SCS 作为 pair-level pre-hoc predictor 仅解释 1.3% variance（practitioner 实际能用的值）。当前 narrative 倾向让 reader 记住 \"22%\" 而淡化 \"1.3%\"，构成 misleading framing。\n\n---\n\n**[AGREE] R1-W3: NER Dimension 2 证据弱于 RE，claim 未充分区分。**\n\n强烈同意，与我的 W4 完全一致。NER batch-level BCS–F1 方向为正（与 hypothesis 相反），MAVEN per-type BCS–F1 被 centrality confound 完全解释（Appendix F, partial r non-significant）。Dimension 2 在实际可用粒度（batch-level）上仅 FewRel + DocRED（同属 RE）支持。论文 title/abstract 给人 cross-task generalization 印象，但证据不支持。\n\n---\n\n**[AGREE] R1-W4: Title \"Shape\" 暗示因果性。**\n\n同意。虽 title 用问句形式提供缓冲，但论文内部多处使用 \"predicts\"（Contribution 2），结合 Limitations §7 承认 \"does not establish interventional causality\"，存在不匹配。建议改为 \"predict\" 或 \"associate with\"。与我的 Q4 一致。\n\n---\n\n**[AGREE with qualification] R1-W5: Cross-model validation 不足。**\n\n同意方向但 severity 略低。对 analysis paper，2 个不同 family + 不同 scale 提供 reasonable initial evidence。但缺少 proprietary model 验证是 gap，这些模型可能有不同的 type-resolution mechanism。论文 Limitations §1 已明确承认。\n\n---\n\n**[AGREE with qualification] R1-W6: FewRel contamination。**\n\n部分同意 concern valid，但论文 defense 是多线的（Appendix I）：BCS partial effect unchanged、monotonic curve、DocRED replication。Collectively reasonable defense，不构成 critical weakness。\n\n---\n\n**[AGREE] R1-W7: 1000 instances 对 long-tail types 充分性。**\n\n同意。Few-NERD 的 long-tail distribution 意味着某些 types 可能个位数 instances。Type-level cluster bootstrap CI（Table 2）部分 addresses 但不完全解决。\n\n---\n\n**[AGREE with nuance] R1-W8: Prompt variant power 不足。**\n\n同意 n=10 underpowered 且无 multiple comparison correction。但论文定位为 robustness check（非 primary evidence），4/4 方向一致是 informative。Count 8 全部 n.s. 的观察重要：confusability effect 可能仅 large schema 时 detectable，进一步限制 practical applicability。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1**: Within-pool quartile CI 确实包含零，但 regression slope p=0.027 显著。论文已有 caveat。\n\n**[AGREE] R1-Q2**: Frequency-residualized BCS for NER 是明显遗漏。MAVEN 有此分析（Appendix F）但 Few-NERD 没有。这是我的 W4/Q2 的核心。\n\n**[AGREE with nuance] R1-Q3**: Simulation 参数有 circularity 但论文声明 \"illustrative, not evidence base\"。删除 simulation 不影响 R²=0.218 直接测量。\n\n**[AGREE] R1-Q4**: Seed SD=0.88pp 在 greedy mode 下不应存在。\"Eliminates randomness\" 措辞应修正。\n\n**[AGREE] R1-Q5**: Floor effect (~51% at high-BCS) 可能压缩 interaction 空间，TOST 在 logit scale 上可能给出不同结论。Valid methodological concern。\n\n---\n\n### 与 R1 的核心分歧\n\n**一致点**：W1 (TOST), W3 (NER Dimension 2), W4 (causality), Q2 (frequency-residualized NER)\n\n**Severity 分歧**：R1 给 3.5，我给 3。我认为 novelty/excitement deficit（我的 W3）是比 statistical subtleties 更大的 acceptance barrier。论文的统计工作 above-average 严谨（我的 S1），但\"发现了一个 r²=1.3% 的 effect\"这个 story 本身的 Main Conference worthiness 是根本问题。R1 的统计质疑如果得到解决（更严格的 TOST、frequency-residualized NER BCS），可能提高 soundness score，但不改变 excitement 评估。",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-17T09:09:01.631163+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4043
}
```

</details>

---


### Assistant

_source line 728 · 2026-05-17T09:09:07.478225+00:00_

交叉回应已提交给 Review Director。

核心结论：与 R1 在 TOST margin、NER Dimension 2 方向矛盾、causality overclaim 三个关键问题上达成一致。主要分歧在 severity 评估——我认为 novelty/excitement deficit 是比统计细节更根本的 acceptance barrier，论文即使修复 R1 所有统计问题，"r²=1.3% effect" 的 story 仍难达 Main Conference 的 excitement threshold。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 24

## Round 24

50 recorded events


### User

_source line 729 · 2026-05-17T14:17:12.362902+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的侧重**：新颖性 + 叙事完整性 + 写作质量 + 引用覆盖

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式**: Long paper, 8 页正文, ACL `[review]` 模板, double-blind
- **附录**: 不计入页数限制，但必须双栏格式
- **必须包含**: Limitations section + Responsible NLP Research Checklist

### 论文路径
`projects/schema-dag-extraction/docs/paper/main.tex`（多文件结构，需读取 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）

### 论文概要
标题: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
这是一篇分析性论文，不提出新方法/新模型，而是通过控制实验揭示 training-free LLM IE 中 schema complexity 如何驱动性能下降。核心指标为 SCS（pairwise embedding similarity）和 BCS（batch-level aggregation）。包含跨 4 个数据集、3 个任务、3 个模型的广泛实验。负面结果：SDGD schema decomposition 失败。

### 审查重点
请重点审查以下方面，给出详细评估：

1. **新颖性评估**
   - SCS/BCS 本质上是 pairwise cosine similarity 的简单聚合——这是否有足够的新颖性？论文自身承认 SCS 与 LLM-PEE 的 partitioning criterion 形式相同。
   - "Controlled study isolating count from confusability" 的分析范式新颖性如何？
   - 负面结果（SDGD 失败）的贡献度如何？是否足以作为独立贡献点？
   - 对 EMNLP 2026 的贡献门槛评估：这篇论文更适合 Main 还是 Findings？

2. **叙事完整性**
   - Abstract → Introduction → Method → Results → Discussion 的故事线是否连贯？
   - "Two dimensions" framing 是否准确？NER 上 batch-level 无效果这一事实是否削弱了框架的普适性？
   - 论文的 contribution claim（Introduction 末尾的 4 条）是否都有充分支撑？
   - RQ1/RQ2/RQ3 的回答是否清晰且令人信服？

3. **写作质量**
   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段等）？
   - 术语定义是否清晰？首次出现是否有解释？
   - 段落过渡是否自然？
   - Abstract 是否在 150-250 words 内完成四个必答问题？

4. **Related Work 和引用覆盖**
   - Related Work 是否充分 positioning？与直接竞争者（LLM-PEE, PARSE, CrossAgentIE, DEE）的区分是否清晰？
   - 是否遗漏重要相关工作？特别关注 2025-2026 年的最新工作
   - 引用密度是否达到 EMNLP 标准？
   - SCS novelty paragraph 是否有效地回应了潜在的新颖性质疑？

5. **图表质量**
   - 图表信息密度是否足够？
   - Caption 是否自包含？
   - 数值精度是否统一？

请按照标准审稿报告格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Detailed Comments

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-17T14:17:21.339050+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-17T14:17:22.345032+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-17T14:17:22.345425+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 733 · 2026-05-17T14:17:22.395866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-17T14:17:26.110954+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 735 · 2026-05-17T14:17:26.613232+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 736 · 2026-05-17T14:17:27.115807+00:00_

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
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B and 70B-Instruct (FP8). Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded association ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity. The TOST equivalence test is estimated from BCS-controlled batches (counts 4--40) where BCS variation is sufficient; generalization to broader count ranges requires additional controlled experi
…[truncated 45008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 737 · 2026-05-17T14:17:27.116309+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 738 · 2026-05-17T14:17:27.470612+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets, and operationalize confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS, the mean pairwise embedding similarity within a type batch). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); at batch level, BCS explains 22--53\% of cross-batch accuracy variance in RE but not in NER, where the signal is absent despite significant pairwise effects. Schema decomposition fails in both tasks due to merge amplification (NER) and routing failure (RE), which points to structural barriers to confusability-aware extraction.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 739 · 2026-05-17T14:17:27.472142+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 740 · 2026-05-17T14:17:27.522788+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accurac
…[truncated 3022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-17T14:17:33.348054+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's information about ACL ARR 2025-2026 reviewer guidelines, review form, and scoring criteria:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide thre
…[truncated 1423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7237
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-17T14:17:38.619431+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 etc.), descriptions of each score level, and all questions reviewers must answer. Include soundness, excitement, overall assessment criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 etc.), descriptions of each score level, and all questions reviewers must answer. Include soundness, excitement, overall assessment criteria."
  }
}
```

</details>

---


### Tool call

_source line 743 · 2026-05-17T14:17:40.028093+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 744 · 2026-05-17T14:17:40.379906+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. Recent work also explores LLM-based data annotation for NER \cite{bogdanov2024nuner,zhang2023llmaaa} and self-improving zero-shot extraction \cite{xie2024selfimproving}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. Specifically, LLM-PEE employs union merge across sub-schema extractions, which our \S\ref{sec:sdgd} analysis shows is associated with precision collapsing from 0.56 to 0.21 in NER as false positives accumulate across passes; RE avoids this because closed-set classification does not require s
…[truncated 2960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 745 · 2026-05-17T14:17:40.530794+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 746 · 2026-05-17T14:17:40.782198+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound, making it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task i
…[truncated 7789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 747 · 2026-05-17T14:17:40.833271+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 748 · 2026-05-17T14:17:40.833797+00:00_

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
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schem
…[truncated 10558 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-17T14:17:45.209040+00:00_

# ACL Rolling Review Form - Complete Scoring Structure

## Primary Scoring Dimensions

### 1. Reviewer Confidence (1-5 Scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with careful checking; unlikely to have missed critical details
- **3**: Pretty sure, but may have missed elements; general familiarity without detailed verification
- **2**: Willing to defend evaluation, but likely missed details or uncertain about novelty
- **1**: "Not my area, or paper is very hard to understand"

### 2. Soundness (1-5 Scale with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong; sufficient support with optional extra experiments
- **3**: Acceptable; supports main claims with minor gaps
- **2**: Poor; main claims lack support with technical problems
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

### 3. Excitement (1-5 Scale with .5 increments)
Evaluates subjective appeal including innovation, impact, and relevance. Ranges from "Highly Exciting" (would recommend/attend) to "Not Exciting" (doesn't resonate with community).

### 4. Overall Assessment (1-5 Scale with .5 increments)
- **5**: Award consideration (top 2.5% papers)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Needs substantial revisions for next cycle
- **1**: Do not resubmit; irrelevant or requires complete redo

## Required Questions

**Narrative sections**: Paper summary, strengths, weaknesses, comments/suggestions, and best paper justification (if applicable)

**Further evaluation areas**: Limitations/societal impact, ethical concerns, ethics review necessity, reproducibility (1-5), dataset value (1-5), software value (1-5), and author identity knowledge (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6589
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-17T14:17:51.154401+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-17T14:17:51.606574+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapsing (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}), confirming that type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!
…[truncated 512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-17T14:17:51.657225+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-17T14:17:52.159426+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across models, suggesting a difficulty ceiling. RE's separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}). Cross-scale evidence (32B vs.\ 8B) shows Dimension~1 replicates fully while Dimension~2 attenuates on smaller models, dropping to near-zero $R^2$ for NER on Llama-3.1-8B (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}). Count-related degradation may partly reflect prompt length (per-type recall 0.586 vs.\ single-pass 0.368, consistent with lost-in-middle effects; \citealt{lost-in-middle-2024}; \citealt{levy-2024-same-task}).
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pair-level effect is modest ($r^2 = 1.3$--$1.7\%$, as ${\sim}89\%$ of pairs never produce mutual confusion); among active-confusion pairs, $R^2 \approx 7\%$ amplifies ${\sim}3\times$ at batch level (Appendix~\ref{app:aggregation-sim}), yielding $R^2$ of 22--53\%. For individual type pairs, SCS is therefore a weak predictor; other factors such as frequency, context diversity, and definition quality dominate. At the batch level, however, these pair-level effects aggregate to produce the observed $R^2$ of 22--53\% in RE, sufficient for practical schema-level screening. We hypothesize that the NER U-shape (\S\ref{sec:count_curves}) reflects a dual-task burden absent in RE: partial schemas require simultaneous span detection and type-membership filtering; at full-schema, filtering becomes vacuous and recall recovers, confirming 
…[truncated 2538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-17T14:17:52.159789+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-17T14:17:52.612102+00:00_

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
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
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
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{llama3
…[truncated 4519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-17T14:17:54.017621+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what constitutes a good review, how to assess soundness, excitement, and overall assessment. What are the criteria for each score level? What specific aspects should reviewers evaluate?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what constitutes a good review, how to assess soundness, excitement, and overall assessment. What are the criteria for each score level? What specific aspects should reviewers evaluate?"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-17T14:18:00.907726+00:00_

# ARR Reviewer Guidelines: Assessment Framework

## What Constitutes a Good Review

Strong reviews must be **specific, professional, and justified**. Rather than vague criticisms like "unclear" or "not novel," reviewers should identify exact issues: "Y and Z are missing from X's description" or cite specific related work.

Reviews should avoid common cognitive biases (listed as H1-H17) such as dismissing results as "obvious in retrospect" or requiring unnecessary additional experiments beyond what claims demand.

## Three-Score Assessment System

Starting February 2025, ARR uses three distinct scores:

### **Soundness**
Evaluates technical rigor and validity. The guideline emphasizes: *"low Soundness scores must be justified by the text of the review."* Reviewers should identify specific methodological flaws, incomplete proofs, or experimental design issues rather than subjective preferences.

### **Excitement**
Reflects personal interest orthogonal to soundness. A paper can be technically sound yet personally unexciting to a reviewer—this separation prevents subjective taste from contaminating technical assessment.

### **Overall Assessment**
A composite recommendation balancing soundness, excitement, novelty, and potential impact. Papers need not achieve SOTA status; contributions like efficiency improvements or high-quality resources merit consideration despite limited personal excitement.

## Key Evaluation Criteria

Reviewers should assess:

- **Appropriateness** to venue scope
- **Novelty** with proper citation support
- **Methodology soundness** (M1-M5 codes for common issues)
- **Experimental rigor** (R1-R5: statistical significance, appropriate claims scope, reproducibility details)
- **Ethics considerations** where applicable
- **Clarity** of research questions and contributions

## Tone and Professionalism

Reviews must maintain professional neutrality. The guidelines note: *"Write the review you would like to get yourself."* Sarcasm, dismissiveness, and 
…[truncated 86 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6890
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-17T14:18:06.506730+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-17T14:18:06.557453+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-17T14:18:07.060888+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 761 · 2026-05-17T14:21:44.923282+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 59, \"total_citations\": 81, \"unique_cited_keys\": 55, \"orphan_bib\": 4, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 47, \"online_not_found\": 4, \"online_mismatch\": 8}, \"cross_check\": {\"orphan_bib\": [\"levy-2024-same-task\", \"llm-calibration-survey-2024\", \"perneger-1998\", \"wellek2010testing\"], \"missing_bib\": [], \"orphan_count\": 4, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"llm-pee-2025\", \"type\": \"inproceedings\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"authors\": \"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"parse-2025\", \"type\": \"inproceedings\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"authors\": \"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"dee-2024\", \"type\": \"inproceedings\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"authors\": \"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\"}, {\"key\": \"crossagentie-2025\", \"type\": \"inproceedings\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"authors\": \"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"},
…[truncated 47334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 217862
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-17T14:22:26.819590+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-17T14:22:27.271778+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex:1:% DEPRECATED — this file is no longer included in main.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-17T14:22:27.824101+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-17T14:22:28.327253+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-17T14:22:28.930553+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-17T14:22:28.931038+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:225:For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:82:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-17T14:22:34.566338+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|It is worth noting|Notably,|delve|leverage|utilize|facilitate|a myriad|a plethora",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally|It is worth noting|Notably,|delve|leverage|utilize|facilitate|a myriad|a plethora",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 769 · 2026-05-17T14:22:35.470234+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:54:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:49:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-17T14:22:35.929137+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", highlighting| demonstrating| indicating| suggesting| showcasing| underscoring",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", highlighting| demonstrating| indicating| suggesting| showcasing| underscoring",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-17T14:22:36.082544+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:46:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:24:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:49:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:70:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:85:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-17T14:22:49.656767+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "zero-shot LLM information extraction schema complexity 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "zero-shot LLM information extraction schema complexity 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 773 · 2026-05-17T14:22:49.858000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "label confusion embedding similarity NER relation extraction LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "label confusion embedding similarity NER relation extraction LLM 2025"
  }
}
```

</details>

---


### Tool result

_source line 774 · 2026-05-17T14:22:57.237014+00:00_

Web search results for query: "label confusion embedding similarity NER relation extraction LLM 2025"

Links: [{"title":"Advancing Few-Shot Named Entity Recognition with Large Language Model","url":"https://www.mdpi.com/2076-3417/15/7/3838"},{"title":"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/html/2508.10036v1"},{"title":"Enhancing Discriminative Representation in Similar ...","url":"https://aclanthology.org/2025.naacl-long.123.pdf"},{"title":"Structured Semantic Information Helps Retrieve Better Examples for In-Context Learning in Few-Shot Relation Extraction","url":"https://arxiv.org/html/2601.20803"},{"title":"GitHub - bllin001/llm-entities-agreement: Analyzing and unifying entity extraction results from Large Language Models using Named Entity Recognition (NER) and cosine similarity techniques · GitHub","url":"https://github.com/bllin001/llm-entities-agreement"},{"title":"Learning a Universal Entity Taxonomy across Datasets and ...","url":"https://aclanthology.org/2025.coling-main.725.pdf"},{"title":"Leveraging large language models and embedding representations for enhanced word similarity computation | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-31102-1"},{"title":"From Text to Alpha: Can LLMs Track Evolving Signals in Corporate Disclosures?","url":"https://arxiv.org/html/2510.03195"},{"title":"Relation Extraction in Biomedical Abstracts with LLMs and ...","url":"https://arxiv.org/pdf/2509.19057"},{"title":"Generation-Augmented Retrieval: Rethinking the Role of ...","url":"https://aclanthology.org/2025.findings-emnlp.974.pdf"}]

Based on the search results, here are key findings related to label confusion, embedding similarity, NER, relation extraction, and LLMs in 2025:

## Few-Shot NER with Label Confusion

As the number of entity types grows, distinguishing fine-grained categories becomes more challenging, and implementing appropriate label scope filt
…[truncated 1137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7379
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-17T14:22:57.739060+00:00_

Web search results for query: "zero-shot LLM information extraction schema complexity 2025 2026"

Links: [{"title":"Applying an ontology-aware zero-shot LLM prompting approach for information extraction in Greek: the case of DIAVGEIA gov gr | Proceedings of the 28th Pan-Hellenic Conference on Progress in Computing and Informatics","url":"https://dl.acm.org/doi/10.1145/3716554.3716603"},{"title":"A Zero-Shot Framework for Low-Resource Relation Extraction via Distant Supervision and Large Language Models","url":"https://www.mdpi.com/2079-9292/14/3/593"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"LLM-based Zero-shot Triple Extraction for Automated Ontology Generation from Software Engineering Standards","url":"https://arxiv.org/html/2509.00140v2"},{"title":"LlmRe: A zero-shot entity relation extraction method based on the large language model | Proceedings of the 2023 7th International Conference on Electronic Information Technology and Computer Engineering","url":"https://dl.acm.org/doi/abs/10.1145/3650400.3650478"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"Zero-shot learning to extract assessment criteria and medical services from the preventive healthcare guidelines using large language models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11258407/"},{"title":"Zero-shot document-level biomedical relation extraction via scenario-based prompt design in two-stage with LLM - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1476927126001039"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"Introducing mCODEGPT as a zero-shot information extraction from clinical free text data tool for cancer 
…[truncated 1849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8082
}
```

</details>

---


### Tool call

_source line 776 · 2026-05-17T14:25:46.162282+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**侧重**: 新颖性 + 叙事完整性 + 写作质量 + 引用覆盖\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验设计严谨、统计方法规范的分析性研究，但核心指标无新颖性、\"两维度\"框架被 NER 空结果削弱、实际贡献门槛更适合 Findings 而非 Main。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验设计规范（BCS-controlled、TOST、cross-model），统计报告充分（bootstrap CI、permutation test），但NER batch-level null结果与\"两维度\"框架矛盾，MAVEN被有效排除使四数据集覆盖率虚高 |\n| **Excitement** | 2.5/5 | 核心发现（count > confusability, similar labels → more confusion）符合直觉且有先例，无意外洞察；负面结果有价值但不足以作为独立贡献；缺乏可操作的解决方案 |\n| **Reproducibility** | 4/5 | 实验参数详尽（seed、decoding config、batch sizes），承诺代码发布，prompt templates 完整公开 |\n| **Reviewer Confidence** | 4/5 | 仔细阅读全文含附录，熟悉 zero-shot IE 和相关统计方法 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心指标 SCS/BCS 无新颖性，分析范式产出符合直觉的结论\n\n- 具体位置：§3.2 SCS 定义，Related Work \"SCS novelty\" 段落\n- 问题：SCS = pairwise cosine similarity of type name embeddings。BCS = mean pairwise SCS。论文自身承认 SCS \"shares its formal definition\" with LLM-PEE 的 partitioning criterion。\"SCS novelty\" 段落试图将贡献重新定位为 \"controlled experimental framework rather than the metric\"，但框架产出的核心结论是：(a) 语义相似的标签更容易混淆——这在传统 ML 中有大量先例（论文已引 Deng 2010, Guo 2021, Zhou 2025），(b) 更多标签导致更差性能——这是 well-known 的。Controlled separation of count from confusability 是方法论贡献，但产出的 insight（\"count dominates, confusability is modest with r²=1.3–1.7%\"）对社区的增量知识有限。\n- 为什么影响接收：EMNLP Main 要求 sufficient novelty in method OR insight。此论文既无新方法，insight 也主要确认直觉而非挑战它。\n- 建议修改方向：(a) 增加 mechanistic analysis（attention/logit level）解释 WHY embedding similarity predicts confusion；或 (b) 展示 BCS-based schema optimization 的实际性能提升，让分析产出可操作的方案。\n\n**N2** [critical] \"两维度\"框架被 NER batch-level null 结果实质性削弱\n\n- 具体位置：§4.3 batch-level 结果、§4.4 Multi-Dimensional Degradation、§5 Discussion \"Task-dependent batch-level effects\"、Appendix G\n- 问题：论文核心叙事围绕 \"degradation operates along two dimensions\"。然而 Dimension 2（confusability → batch-level performance）仅在 RE 上成立。NER batch-level BCS 相关为 null（r ≈ 0, n=450, §4.4 和 Appendix G）。这意味着 \"two-dimensional\" framing 仅适用于论文研究的三个任务之一。标题问 \"How Does Schema Complexity Predict Performance\"，但对 NER 的回答本质上是 \"count matters, confusability doesn't (at batch level)\"。论文提供了假说（NER 错误以 missed entities 为主，§5），但未验证。\n- 为什么影响接收：中心 framing 过度承诺。审稿人会发现 \"two dimensions\" 仅适用于 RE 这一点，对论文可信度造成严重损害。\n- 建议修改方向：诚实地将论文重新定位为 \"BCS predicts RE accuracy with practical significance; NER presents a contrasting case where count dominates\"。或者验证关于 NER 的假说——例如，将 missed-entity errors 从 NER F1 中分离后观察是否出现 BCS signal。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Pairwise 效应量微弱，实际意义存疑\n\n- 具体位置：§4.2 Table 3, §4.3 \"Practical magnitude\"\n- 问题：Pairwise SCS 仅解释 1.3–1.7% 的 type confusion variance。Batch-level BCS 在 FewRel 上 R²=22%（DocRED 53%），更可观，但 typical-batch gap 仅 2.2 pp（§4.3），论文自述为 \"roughly 7% of the extreme-batch gap\"。论文引用 Cohen (1988) 的 \"small but real\" 框架为效应量辩护，但这一来自行为科学的标准直接套用到 NLP 部署场景需要更多论证。3–5 pp 的准确率差异在多数部署场景下不构成决策依据。\n- 建议：明确说明在什么部署条件下 2.2 pp 差距具有实际意义，或承认 BCS 更适合作为 screening heuristic 而非 strong predictor。\n\n**W2** [warning] FewRel 数据使用方式非标准\n\n- 具体位置：§3.1 FewRel 段落，Limitations 第 8 条\n- 问题：合并 FewRel training+validation splits 获得 80 types 是非标准用法。FewRel 原始设计为 few-shot meta-learning，train/val 对应不同的 relation sets。论文提供了 contamination checks（train-origin types 准确率更低而非更高, $-$8.8 pp, p=0.06），但 non-uniform contamination 更难排除。Appendix K 的 split-origin covariate 分析有效缓解了 batch-level 担忧，但 individual type-level contamination 仍可能影响 pairwise SCS-confusion 相关。\n- 建议：在正文中更显著地讨论这一设计选择。如果仅使用 16-type val split 的 controlled experiments 能复现主要发现，明确指出。\n\n**W3** [warning] MAVEN 结果实质被排除，四数据集覆盖率虚高\n\n- 具体位置：§4.5 Centrality Confound, Appendix E\n- 问题：MAVEN 是四个数据集之一，但 batch-level 结果因 centrality confounding 被 invalidate。虽然 pairwise SCS signal 幸存（r=0.129, p<0.001），MAVEN 不提供任何 usable batch-level evidence。因此 batch-level BCS claim 的有效数据集覆盖为：FewRel ✓, DocRED ✓, Few-NERD ✗ (null), MAVEN ✗ (confounded)。这意味着 BCS 的 batch-level predictive power 仅在 RE 任务上成立。\n- 建议：Abstract 和 Introduction 中 \"spanning NER, RE, and event detection across four datasets\" 的措辞应修改，区分 pairwise-level 和 batch-level findings 的覆盖范围。\n\n**W4** [warning] Contribution 3 本质上是 null result 的包装\n\n- 具体位置：Introduction Contribution list item 3\n- 问题：Contribution 3 声称 \"count-related recall decline generalizes across tasks, while batch-level confusability effects are specific to RE\"。后半句本质上是 NER 的 null result。将 null result 包装为 positive contribution 有误导性——需要明确区分 \"我们发现了 X\" 和 \"我们未能发现 X\"。\n- 建议：将 Contribution 3 改写为 \"We identify task-dependent limitations of batch-level confusability metrics: BCS predicts RE accuracy but fails to predict NER F1, revealing that...\"\n\n**W5** [warning] Introduction \"五个发现\" vs \"四条贡献\" 不对齐\n\n- 具体位置：Introduction lines 14–19（五个发现）vs lines 22–27（四条贡献）\n- 问题：五个 findings 和四条 contributions 之间没有清晰的映射关系。Finding (4)（centrality confound）和 Finding (5)（decomposition failure）映射到哪条 contribution？读者需要自行推断。\n- 建议：或者统一为相同数量的条目并建立对应关系，或者在 contribution list 中标注对应的 finding 编号。\n\n---\n\n## 小问题（不影响接收）\n\n- **Abstract 偏短**：约 130–140 words，低于 150–250 words 建议范围。可增加一句 practical implications。\n- **-ing 分词短语**：Results §4.1 \"indicating schema configuration rather than model-specific factors predicts difficulty\"；Discussion §5 \"suggesting a difficulty ceiling\"；§6 SDGD \"confirming that type separation recovers performance\"。频率中等，建议改写为完整句子。\n- **\"Notably\" 使用**：Results §4.2 line 49 \"Notably, the independent MiniLM embedding yields a stronger...\"——可直接删除 \"Notably\" 不影响表意。\n- **孤儿引用**：`llm-calibration-survey-2024`, `perneger-1998`, `wellek2010testing` 在 .bib 中但未被引用（`levy-2024-same-task` 在 discussion.tex 中使用了 `\\citealt`，verify_references 工具可能未检测到 `\\citealt` 命令）。应清理。\n- **DocRED count curve 仅引用未呈现**：§4.1 提到 \"DocRED replicates the monotonic RE pattern (88.0%→38.7%, −56%; Appendix)\" 但 Appendix 中未找到 DocRED 的 count curve table/figure，只有 DocRED 在 §4.3 的 BCS-controlled 结果。\n- **MAVEN ED 结果不充分**：MAVEN 作为 Event Detection 数据集被包含，但 ED 特有的分析（trigger identification vs. type classification 的交互）几乎没有展开。ED 的独立贡献有限。\n\n---\n\n## 引用覆盖评估\n\n**总体**：55 unique citations，对 EMNLP long paper 来说偏少但可接受。在线验证确认绝大多数引用真实存在。\n\n**可能遗漏的重要工作**：\n\n1. **Batch prompting**: Cheng et al. (2023) \"Batch Prompting: Efficient Inference with Large Language Model APIs\" — 论文的 count-curve 方法概念上与 batch prompting 相关，将多个 types 打包进一个 prompt 的做法应当讨论这一联系。\n2. **Universal entity taxonomy**: Fetahu et al. / Li et al. (COLING 2025) \"Learning a Universal Entity Taxonomy across Datasets\" — 直接涉及跨数据集的 entity type 语义关系。\n3. **Grammar-constrained decoding**: 论文大量使用 vLLM constrained decoding，但仅引用 JSONSchemaBench，未引用 Outlines (Willard & Louf, 2023) 或 SGLang 等实际实现的基础工作。考虑到 constrained decoding 对 RE routing failure 的关键作用（§6: \"constrained decoding forces confident predictions\"），这是重要的遗漏。\n4. **Prompt sensitivity beyond format**: Sclar (2024) 已引用但 Lu et al. (2022) \"Fantastically Ordered Prompts and Where to Find Them\" 关于 label ordering sensitivity 的工作未引——论文使用 alphabetical ordering，是否 ordering 本身影响 confusability 效应值得讨论。\n\n**SCS novelty 段落有效性**：位于 Related Work 末尾（§2 最后一个段落），策略位置正确。引用 Cohen (1988) 和 Lakens (2013) 为 effect size 辩护是合理的。但该段落更像是预防性辩护而非积极论证新颖性——它承认了问题但未真正解决新颖性质疑。\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：BCS-controlled experiments 正确隔离 confusability 与 count（§4.3），within-pool 分析控制 pool composition，cross-model 验证跨越三个模型家族，TOST equivalence testing 是 NLP 论文中罕见的统计规范。\n2. **诚实报告负面和空结果**：NER batch-level null, SDGD 失败, pairwise effect sizes 微弱——这种学术诚实在投稿论文中难得。\n3. **Confound 分析堪称典范**：MAVEN centrality confound（§4.5, Appendix E）从 confound identification 到 partial correlation 到 joint control 到 interpretation，逻辑完整。\n4. **Cross-model/cross-prompt robustness**：跨 Qwen3-32B, Llama-3.1-8B, Llama-3.1-70B 及四种 prompt variants 的复现为结论提供了可信度。\n5. **Limitations section 异常详尽**：8 条具体 limitations 带量化证据，属于高标准。\n\n---\n\n## 综合判断\n\n这是一篇方法论严谨的分析性论文，在实验设计和统计报告方面超过了多数 EMNLP 投稿。问题在于：(1) 核心指标无新意，(2) \"两维度\"框架仅在 RE 上完整成立，(3) insight 主要确认直觉而非挑战它，(4) 缺乏可操作的解决方案。SDGD 的负面结果有社区价值但作为独立贡献偏弱。综合来看，Soundness 较强但 Excitement 不足，建议定位 Findings 而非 Main。如果作者能回应 N1（增加 mechanistic analysis 或 practical solution）和 N2（诚实调整 framing），论文可升至 3.5。",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**侧重**: 新颖性 + 叙事完整性 + 写作质量 + 引用覆盖\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验设计严谨、统计方法规范的分析性研究，但核心指标无新颖性、\"两维度\"框架被 NER 空结果削弱、实际贡献门槛更适合 Findings 而非 Main。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验设计规范（BCS-controlled、TOST、cross-model），统计报告充分（bootstrap CI、permutation test），但NER batch-level null结果与\"两维度\"框架矛盾，MAVEN被有效排除使四数据集覆盖率虚高 |\n| **Excitement** | 2.5/5 | 核心发现（count > confusability, similar labels → more confusion）符合直觉且有先例，无意外洞察；负面结果有价值但不足以作为独立贡献；缺乏可操作的解决方案 |\n| **Reproducibility** | 4/5 | 实验参数详尽（seed、decoding config、batch sizes），承诺代码发布，prompt templates 完整公开 |\n| **Reviewer Confidence** | 4/5 | 仔细阅读全文含附录，熟悉 zero-shot IE 和相关统计方法 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心指标 SCS/BCS 无新颖性，分析范式产出符合直觉的结论\n\n- 具体位置：§3.2 SCS 定义，Related Work \"SCS novelty\" 段落\n- 问题：SCS = pairwise cosine similarity of type name embeddings。BCS = mean pairwise SCS。论文自身承认 SCS \"shares its formal definition\" with LLM-PEE 的 partitioning criterion。\"SCS novelty\" 段落试图将贡献重新定位为 \"controlled experimental framework rather than the metric\"，但框架产出的核心结论是：(a) 语义相似的标签更容易混淆——这在传统 ML 中有大量先例（论文已引 Deng 2010, Guo 2021, Zhou 2025），(b) 更多标签导致更差性能——这是 well-known 的。Controlled separation of count from confusability 是方法论贡献，但产出的 insight（\"count dominates, confusability is modest with r²=1.3–1.7%\"）对社区的增量知识有限。\n- 为什么影响接收：EMNLP Main 要求 sufficient novelty in method OR insight。此论文既无新方法，insight 也主要确认直觉而非挑战它。\n- 建议修改方向：(a) 增加 mechanistic analysis（attention/logit level）解释 WHY embedding similarity predicts confusion；或 (b) 展示 BCS-based schema optimization 的实际性能提升，让分析产出可操作的方案。\n\n**N2** [critical] \"两维度\"框架被 NER batch-level null 结果实质性削弱\n\n- 具体位置：§4.3 batch-level 结果、§4.4 Multi-Dimensional Degradation、§5 Discussion \"Task-dependent batch-level effects\"、Appendix G\n- 问题：论文核心叙事围绕 \"degradation operates along two dimensions\"。然而 Dimension 2（confusability → batch-level performance）仅在 RE 上成立。NER batch-level BCS 相关为 null（r ≈ 0, n=450, §4.4 和 Appendix G）。这意味着 \"two-dimensional\" framing 仅适用于论文研究的三个任务之一。标题问 \"How Does Schema Complexity Predict Performance\"，但对 NER 的回答本质上是 \"count matters, confusability doesn't (at batch level)\"。论文提供了假说（NER 错误以 missed entities 为主，§5），但未验证。\n- 为什么影响接收：中心 framing 过度承诺。审稿人会发现 \"two dimensions\" 仅适用于 RE 这一点，对论文可信度造成严重损害。\n- 建议修改方向：诚实地将论文重新定位为 \"BCS predicts RE accuracy with practical significance; NER presents a contrasting case where count dominates\"。或者验证关于 NER 的假说——例如，将 missed-entity errors 从 NER F1 中分离后观察是否出现 BCS signal。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Pairwise 效应量微弱，实际意义存疑\n\n- 具体位置：§4.2 Table 3, §4.3 \"Practical magnitude\"\n- 问题：Pairwise SCS 仅解释 1.3–1.7% 的 type confusion variance。Batch-level BCS 在 FewRel 上 R²=22%（DocRED 53%），更可观，但 typical-batch gap 仅 2.2 pp（§4.3），论文自述为 \"roughly 7% of the extreme-batch gap\"。论文引用 Cohen (1988) 的 \"small but real\" 框架为效应量辩护，但这一来自行为科学的标准直接套用到 NLP 部署场景需要更多论证。3–5 pp 的准确率差异在多数部署场景下不构成决策依据。\n- 建议：明确说明在什么部署条件下 2.2 pp 差距具有实际意义，或承认 BCS 更适合作为 screening heuristic 而非 strong predictor。\n\n**W2** [warning] FewRel 数据使用方式非标准\n\n- 具体位置：§3.1 FewRel 段落，Limitations 第 8 条\n- 问题：合并 FewRel training+validation splits 获得 80 types 是非标准用法。FewRel 原始设计为 few-shot meta-learning，train/val 对应不同的 relation sets。论文提供了 contamination checks（train-origin types 准确率更低而非更高, $-$8.8 pp, p=0.06），但 non-uniform contamination 更难排除。Appendix K 的 split-origin covariate 分析有效缓解了 batch-level 担忧，但 individual type-level contamination 仍可能影响 pairwise SCS-confusion 相关。\n- 建议：在正文中更显著地讨论这一设计选择。如果仅使用 16-type val split 的 controlled experiments 能复现主要发现，明确指出。\n\n**W3** [warning] MAVEN 结果实质被排除，四数据集覆盖率虚高\n\n- 具体位置：§4.5 Centrality Confound, Appendix E\n- 问题：MAVEN 是四个数据集之一，但 batch-level 结果因 centrality confounding 被 invalidate。虽然 pairwise SCS signal 幸存（r=0.129, p<0.001），MAVEN 不提供任何 usable batch-level evidence。因此 batch-level BCS claim 的有效数据集覆盖为：FewRel ✓, DocRED ✓, Few-NERD ✗ (null), MAVEN ✗ (confounded)。这意味着 BCS 的 batch-level predictive power 仅在 RE 任务上成立。\n- 建议：Abstract 和 Introduction 中 \"spanning NER, RE, and event detection across four datasets\" 的措辞应修改，区分 pairwise-level 和 batch-level findings 的覆盖范围。\n\n**W4** [warning] Contribution 3 本质上是 null result 的包装\n\n- 具体位置：Introduction Contribution list item 3\n- 问题：Contribution 3 声称 \"count-related recall decline generalizes across tasks, while batch-level confusability effects are specific to RE\"。后半句本质上是 NER 的 null result。将 null result 包装为 positive contribution 有误导性——需要明确区分 \"我们发现了 X\" 和 \"我们未能发现 X\"。\n- 建议：将 Contribution 3 改写为 \"We identify task-dependent limitations of batch-level confusability metrics: BCS predicts RE accuracy but fails to predict NER F1, revealing that...\"\n\n**W5** [warning] Introduction \"五个发现\" vs \"四条贡献\" 不对齐\n\n- 具体位置：Introduction lines 14–19（五个发现）vs lines 22–27（四条贡献）\n- 问题：五个 findings 和四条 contributions 之间没有清晰的映射关系。Finding (4)（centrality confound）和 Finding (5)（decomposition failure）映射到哪条 contribution？读者需要自行推断。\n- 建议：或者统一为相同数量的条目并建立对应关系，或者在 contribution list 中标注对应的 finding 编号。\n\n---\n\n## 小问题（不影响接收）\n\n- **Abstract 偏短**：约 130–140 words，低于 150–250 words 建议范围。可增加一句 practical implications。\n- **-ing 分词短语**：Results §4.1 \"indicating schema configuration rather than model-specific factors predicts difficulty\"；Discussion §5 \"suggesting a difficulty ceiling\"；§6 SDGD \"confirming that type separation recovers performance\"。频率中等，建议改写为完整句子。\n- **\"Notably\" 使用**：Results §4.2 line 49 \"Notably, the independent MiniLM embedding yields a stronger...\"——可直接删除 \"Notably\" 不影响表意。\n- **孤儿引用**：`llm-calibration-survey-2024`, `perneger-1998`, `wellek2010testing` 在 .bib 中但未被引用（`levy-2024-same-task` 在 discussion.tex 中使用了 `\\citealt`，verify_references 工具可能未检测到 `\\citealt` 命令）。应清理。\n- **DocRED count curve 仅引用未呈现**：§4.1 提到 \"DocRED replicates the monotonic RE pattern (88.0%→38.7%, −56%; Appendix)\" 但 Appendix 中未找到 DocRED 的 count curve table/figure，只有 DocRED 在 §4.3 的 BCS-controlled 结果。\n- **MAVEN ED 结果不充分**：MAVEN 作为 Event Detection 数据集被包含，但 ED 特有的分析（trigger identification vs. type classification 的交互）几乎没有展开。ED 的独立贡献有限。\n\n---\n\n## 引用覆盖评估\n\n**总体**：55 unique citations，对 EMNLP long paper 来说偏少但可接受。在线验证确认绝大多数引用真实存在。\n\n**可能遗漏的重要工作**：\n\n1. **Batch prompting**: Cheng et al. (2023) \"Batch Prompting: Efficient Inference with Large Language Model APIs\" — 论文的 count-curve 方法概念上与 batch prompting 相关，将多个 types 打包进一个 prompt 的做法应当讨论这一联系。\n2. **Universal entity taxonomy**: Fetahu et al. / Li et al. (COLING 2025) \"Learning a Universal Entity Taxonomy across Datasets\" — 直接涉及跨数据集的 entity type 语义关系。\n3. **Grammar-constrained decoding**: 论文大量使用 vLLM constrained decoding，但仅引用 JSONSchemaBench，未引用 Outlines (Willard & Louf, 2023) 或 SGLang 等实际实现的基础工作。考虑到 constrained decoding 对 RE routing failure 的关键作用（§6: \"constrained decoding forces confident predictions\"），这是重要的遗漏。\n4. **Prompt sensitivity beyond format**: Sclar (2024) 已引用但 Lu et al. (2022) \"Fantastically Ordered Prompts and Where to Find Them\" 关于 label ordering sensitivity 的工作未引——论文使用 alphabetical ordering，是否 ordering 本身影响 confusability 效应值得讨论。\n\n**SCS novelty 段落有效性**：位于 Related Work 末尾（§2 最后一个段落），策略位置正确。引用 Cohen (1988) 和 Lakens (2013) 为 effect size 辩护是合理的。但该段落更像是预防性辩护而非积极论证新颖性——它承认了问题但未真正解决新颖性质疑。\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：BCS-controlled experiments 正确隔离 confusability 与 count（§4.3），within-pool 分析控制 pool composition，cross-model 验证跨越三个模型家族，TOST equivalence testing 是 NLP 论文中罕见的统计规范。\n2. **诚实报告负面和空结果**：NER batch-level null, SDGD 失败, pairwise effect sizes 微弱——这种学术诚实在投稿论文中难得。\n3. **Confound 分析堪称典范**：MAVEN centrality confound（§4.5, Appendix E）从 confound identification 到 partial correlation 到 joint control 到 interpretation，逻辑完整。\n4. **Cross-model/cross-prompt robustness**：跨 Qwen3-32B, Llama-3.1-8B, Llama-3.1-70B 及四种 prompt variants 的复现为结论提供了可信度。\n5. **Limitations section 异常详尽**：8 条具体 limitations 带量化证据，属于高标准。\n\n---\n\n## 综合判断\n\n这是一篇方法论严谨的分析性论文，在实验设计和统计报告方面超过了多数 EMNLP 投稿。问题在于：(1) 核心指标无新意，(2) \"两维度\"框架仅在 RE 上完整成立，(3) insight 主要确认直觉而非挑战它，(4) 缺乏可操作的解决方案。SDGD 的负面结果有社区价值但作为独立贡献偏弱。综合来看，Soundness 较强但 Excitement 不足，建议定位 Findings 而非 Main。如果作者能回应 N1（增加 mechanistic analysis 或 practical solution）和 N2（诚实调整 framing），论文可升至 3.5。",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 777 · 2026-05-17T14:25:50.440061+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4277
}
```

</details>

---


### Assistant

_source line 778 · 2026-05-17T14:25:58.347181+00:00_

审稿报告已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。

主要问题：
1. **[N1 critical]** SCS/BCS 无新颖性，核心 insight 确认直觉而非挑战它
2. **[N2 critical]** "两维度"框架被 NER batch-level null result 实质性削弱——Dimension 2 仅在 RE 上成立
3. **[W1-W5]** 效应量微弱(r²=1.3-1.7%)、FewRel 非标准用法、MAVEN 实质被排除使覆盖率虚高、Contribution 3 包装 null result、五发现 vs 四贡献不对齐

优势：实验设计严谨（TOST、cross-model、within-pool control）、诚实报告负面结果、MAVEN centrality confound 分析堪称典范。

建议：Soundness 较强但 Excitement 不足，建议 Findings 而非 Main。如能增加 mechanistic analysis 或实际 solution 并调整 framing，可提升至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 25

## Round 25

60 recorded events


### User

_source line 779 · 2026-05-17T14:28:13.884101+00:00_

[Round 12 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 写作质量 + 格式合规**。这是 Round 12 审稿（论文经过多轮修订）。

## 投稿信息
- **Venue**: EMNLP 2026 Main Conference（通过 ACL Rolling Review May 2026 cycle 提交）
- **格式**: ACL 2023 模板, double-blind, 行号开启
- **正文页数限制**: 8 页（不含 references, limitations, ethics, appendix）
- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit（含 0.5 级增量）
- **论文路径**: `projects/schema-dag-extraction/docs/paper/main.tex`

## 你的审查侧重

### A. 新颖性与贡献（Excitement）
1. 核心 finding（count > confusability 20×, typical gap 仅 2.2pp）的新颖性评估——这些发现是否 trivially expected？
2. SCS/BCS metric 的增量贡献——论文是否已正确 frame 为 "controlled validation" 而非 metric novelty？
3. 负面结果（SDGD failure, merge amplification）的社区价值
4. 与同期工作的差异化定位

### B. 写作质量
1. **Abstract**: 是否精简到 2-3 核心数字？BCS 是否在 Abstract 内展开定义？是否仍像实验报告？
2. **Introduction**: "五发现"段是否已拆句？Contribution list 是否已改为方法论声明格式（1 行/条，无具体数字）？
3. **Discussion/Conclusion**: 是否扩展到至少 1/2 column？是否包含 practitioner recommendations、training-based IE 对比？
4. **AI 写作痕迹**: grep em-dash (—/–), -ing 尾句, 过度分段
5. **因果语言**: Title 是否仍含 "Shape"？正文 "driven"/"channels" 是否已替换为 "predict"/"associate with"?

### C. 格式合规
1. 正文 8 页限制
2. `\enlargethispage` 是否已删除
3. Supplementary 与 appendix 是否仍有重复
4. 引用格式、orphan bib entries
5. TOST 首次使用是否展开为 "Two One-Sided Tests (TOST)"

### D. 上轮遗留 Open Issues（重点检查修复状态）
**Critical (in_progress)**:
- R10-N1: 因果语言 ('driven', 'channels', 'shape') 超出证据边界
- R10-N2: Pair→batch 聚合推理链叙事误导 (unconditional R²=1.3% vs batch 22%)
- R10-N3: TOST ±3pp margin 的 external anchoring 不足
- R11-N1: NER Dimension 2 batch-level 方向相反 但 title/abstract 泛化为 cross-task
- R11-N2: 核心效应量过小 (2.2pp) practical significance 存疑

**Warning (in_progress)**:
- R10-W3: Abstract 数字密度过高
- R10-W4: Contribution list 过长
- R10-W5: BCS 'generalizes across tasks' overclaiming
- R10-W7: Supplementary 与 appendix 重复
- R11-W1: Discussion 过短
- R11-W2: TOST 术语未展开
- R11-W3: Prompt variant analysis 无 multiple comparison correction

请逐条检查这些 issue 的修复状态，并独立评估论文当前质量。按 ACL ARR review form 出具完整审稿报告（Soundness/Excitement/Reproducibility/Overall Assessment/Confidence + Must-Fix/Should-Fix/Minor）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-17T14:28:24.828023+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-17T14:28:25.381195+00:00_

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
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B and 70B-Instruct (FP8). Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded association ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity. The TOST equivalence test is estimated from BCS-controlled batches (counts 4--40) where BCS variation is sufficient; generalization to broader count ranges requires additional controlled experi
…[truncated 45008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-17T14:28:25.432799+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 783 · 2026-05-17T14:28:25.534996+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-17T14:28:32.062312+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-17T14:28:32.062785+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets, and operationalize confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS, the mean pairwise embedding similarity within a type batch). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); at batch level, BCS explains 22--53\% of cross-batch accuracy variance in RE but not in NER, where the signal is absent despite significant pairwise effects. Schema decomposition fails in both tasks due to merge amplification (NER) and routing failure (RE), which points to structural barriers to confusability-aware extraction.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-17T14:28:32.464794+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-17T14:28:32.967122+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accurac
…[truncated 3022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-17T14:28:33.017908+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-17T14:28:33.921829+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. Recent work also explores LLM-based data annotation for NER \cite{bogdanov2024nuner,zhang2023llmaaa} and self-improving zero-shot extraction \cite{xie2024selfimproving}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. Specifically, LLM-PEE employs union merge across sub-schema extractions, which our \S\ref{sec:sdgd} analysis shows is associated with precision collapsing from 0.56 to 0.21 in NER as false positives accumulate across passes; RE avoids this because closed-set classification does not require s
…[truncated 2960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-17T14:28:33.922297+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 791 · 2026-05-17T14:28:34.474915+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound, making it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task i
…[truncated 7789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-17T14:28:34.475294+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 793 · 2026-05-17T14:28:34.928318+00:00_

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
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schem
…[truncated 10558 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-17T14:28:34.928652+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-17T14:28:35.430758+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapsing (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}), confirming that type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!
…[truncated 512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-17T14:28:35.481372+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-17T14:28:35.883405+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across models, suggesting a difficulty ceiling. RE's separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}). Cross-scale evidence (32B vs.\ 8B) shows Dimension~1 replicates fully while Dimension~2 attenuates on smaller models, dropping to near-zero $R^2$ for NER on Llama-3.1-8B (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}). Count-related degradation may partly reflect prompt length (per-type recall 0.586 vs.\ single-pass 0.368, consistent with lost-in-middle effects; \citealt{lost-in-middle-2024}; \citealt{levy-2024-same-task}).
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pair-level effect is modest ($r^2 = 1.3$--$1.7\%$, as ${\sim}89\%$ of pairs never produce mutual confusion); among active-confusion pairs, $R^2 \approx 7\%$ amplifies ${\sim}3\times$ at batch level (Appendix~\ref{app:aggregation-sim}), yielding $R^2$ of 22--53\%. For individual type pairs, SCS is therefore a weak predictor; other factors such as frequency, context diversity, and definition quality dominate. At the batch level, however, these pair-level effects aggregate to produce the observed $R^2$ of 22--53\% in RE, sufficient for practical schema-level screening. We hypothesize that the NER U-shape (\S\ref{sec:count_curves}) reflects a dual-task burden absent in RE: partial schemas require simultaneous span detection and type-membership filtering; at full-schema, filtering becomes vacuous and recall recovers, confirming 
…[truncated 2538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-17T14:28:35.934147+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-17T14:28:36.235796+00:00_

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
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
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
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{llama3
…[truncated 4519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-17T14:28:36.236385+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-17T14:28:47.129871+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the web search results, here's information about ACL Rolling Review 2026 reviewer guidelines, review form, and criteria:

## Reviewer Guidelines

To preserve the merits of double-blind review, reviewers should not actively try to discover the identity of the authors an
…[truncated 2053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10893
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-17T14:28:51.349765+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 803 · 2026-05-17T14:28:51.400358+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-17T14:28:55.667656+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales (1-5 or whatever), and the description of each score level. I need the exact criteria for Soundness, Excitement/Novelty, Overall Assessment, Confidence, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales (1-5 or whatever), and the description of each score level. I need the exact criteria for Soundness, Excitement/Novelty, Overall Assessment, Confidence, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 805 · 2026-05-17T14:28:57.024411+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 806 · 2026-05-17T14:28:57.326009+00:00_

1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	% =============================================================================
6	% DIRECT COMPETITORS
7	% =============================================================================
8	
9	@inproceedings{llm-pee-2025,
10	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
11	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
12	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
13	    year      = {2025},
14	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
15	}
16	
17	@inproceedings{parse-2025,
18	    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
19	    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
20	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
21	    year      = {2025},
22	    url       = {https://aclanthology.org/2025.emnlp-industry.184/},
23	}
24	
25	@inproceedings{dee-2024,
26	    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},
27	    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},
28	    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},
29	    year      = {2024},
30	    url       = {https://arxiv.org/abs/2406.01045},
31	}
32	
33	@inproceedings{crossagentie-2025,
34	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
35	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shux
…[truncated 27103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-17T14:29:02.200146+00:00_

# ACL ARR Review Form Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## Soundness
Scale: 1-5 (with half-point increments)
- **5:** Study represents exceptional thoroughness for its category
- **4:** Adequate support provided; minor additional experiments optional
- **3:** Sufficient evidence for main claims; some points need refinement
- **2:** Major claims lack support; significant technical/methodological problems
- **1:** Insufficient depth or not relevant to computational linguistics

## Excitement
Scale: 1-5 (with half-point increments)
- **5:** "I would recommend this paper to others and/or attend its presentation"
- **4:** Would mention to colleagues; make effort to attend presentation
- **3:** Might discuss certain aspects if time permits
- **2:** Does not resonate personally; may appeal to broader community
- **1:** "Does not resonate with me...or others in the *ACL community"

## Overall Assessment
Scale: 1-5 (with half-point increments)
- **5:** Award consideration (top 2.5%)
- **4:** Conference acceptance
- **3:** Findings acceptance
- **2:** Resubmit after revisions next cycle
- **1:** Do not resubmit or lacks relevance

## Additional Dimensions

**Reproducibility:** 1-5 scale measuring ease of result reproduction

**Datasets/Software:** 1-5 scales assessing resource value to researchers

**Author Identity Knowledge:** 1-5 scale indicating anonymity status

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6532
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-17T14:29:10.639052+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-17T14:29:11.041284+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex:1:% DEPRECATED — this file is no longer included in main.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-17T14:29:11.593299+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-17T14:29:12.097296+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-17T14:29:12.549763+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\enlargethispage",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\enlargethispage",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-17T14:29:13.006651+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-17T14:29:14.011981+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "driven|channels",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "driven|channels",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-17T14:29:14.463743+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:276:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:424:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:502:Table~\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\,pp (70B) versus $-$30.1\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-driven decline) is directionally consistent across architectures for RE.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:504:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:508:In summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-driven decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:513:To test whether in-context demonstrations mitigate the BCS-driven confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \S\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\approx 0.36$; 
…[truncated 323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-17T14:29:15.467544+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-17T14:29:15.668582+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:225:For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:307:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:403:\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\Delta r$ indicates no systematic benefit from including definitions.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:424:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:531:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex:75:Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex:111:Yes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.
/home/ubuntu/.agent-ml-research-id
…[truncated 2656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-17T14:29:15.669000+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-17T14:29:15.719913+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 820 · 2026-05-17T14:29:27.437188+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "count-driven|BCS-driven|frequency-driven|confusability-driven",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "count-driven|BCS-driven|frequency-driven|confusability-driven",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-17T14:29:27.488048+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:424:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:502:Table~\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\,pp (70B) versus $-$30.1\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-driven decline) is directionally consistent across architectures for RE.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:504:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:508:In summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-driven decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:513:To test whether in-context demonstrations mitigate the BCS-driven confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \S\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\approx 0.36$; 25 high-BCS, mean $\approx 0.80$), drawn from the pre-constructed batch pool of \S\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/d
…[truncated 51 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-17T14:29:27.990238+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Two One-Sided|TOST",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Two One-Sided|TOST",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-17T14:29:28.040883+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:44:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:187:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:189:A $2 \times 2$ factorial sensitivity check on FewRel (count $\in \{8, 16\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\S\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:199:\textbf{Margin (pp)} & \textbf{$t_{\text{upper}}$} & \textbf{$p_{\text{TOST}}$} & \textbf{Conclusion} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:207:\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\,pp, 90\% CI [$-$1.0, 2.0]\,pp) is bounded below 2\,pp at marginal significance ($p = 0.047$), confirming that the $\pm 3$\,pp choice does not drive the equivalence conclusion. At $\pm 1$\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:212:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex:11:Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomp
…[truncated 760 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 824 · 2026-05-17T14:29:28.844509+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "shape|Shape",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "shape|Shape",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-17T14:29:28.895273+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:498:\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\to$80): $-$30.7\,pp (70B) vs.\ $-$30.1\,pp (32B). NER decline (count 2$\to$22): $-$7.1\,pp (70B) vs.\ $-$23.6\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:504:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:508:In summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-driven decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:20:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-17T14:29:29.197500+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\enlargethispage|\\\\newpage",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\enlargethispage|\\\\newpage",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-17T14:29:29.348534+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-17T14:29:30.252758+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "channels",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "channels",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-17T14:29:30.605028+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-17T14:32:41.870206+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "wellek|perneger|llm-calibration-survey",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "wellek|perneger|llm-calibration-survey",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-17T14:32:42.974396+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-17T14:32:43.194279+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex",
  "head_limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex",
    "head_limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-17T14:32:43.194881+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:15:Our centrality confound (\S\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \cite{cai-isotropy-clusters-2021}, explaining why MAVEN's single-ontology types conflate confusability with centrality.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:57:\paragraph{Multiple comparisons.} Cross-dataset comparisons (FewRel, DocRED, Few-NERD, MAVEN) serve as independent replications of the same hypothesis and do not require family-wise correction \citep{rothman-1990}. Within-dataset secondary analyses (e.g., quartile comparisons, slope sensitivity checks) involve multiple looks at the same data; we report individual $p$-values and note that core claims rest on effects reaching $p < 0.001$ \citep{dror-2018-significance}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:192:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:307:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:468:[Omitted long matching line]
/home/ubu
…[truncated 3707 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-17T14:33:21.105264+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 835 · 2026-05-17T14:33:21.155943+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-17T14:35:16.839198+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 12 审稿报告\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)\n**审查侧重**: 新颖性 + 写作质量 + 格式合规\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 方法论严谨、结果诚实的 controlled study，但核心效应量小（typical 2.2pp）、findings 可预期程度较高，达到 Findings 收录标准但 excitement 不足以进入主会议。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨（BCS-controlled stratification、TOST equivalence、cross-model/cross-prompt validation），但2×2 factorial和logit-scale TOST均 inconclusive；NER batch-level null result限制了 cross-task generalization |\n| Excitement | 2.5/5 | 核心发现（count > confusability 20×）有量化价值但非意外；SCS/BCS 非新指标；negative results 有社区价值但 practical utility 有限（BCS screening 仅改善 3-5pp） |\n| Reproducibility | 4/5 | 实验细节充分（decoding params、seed、batch构造协议、bootstrap参数），承诺开源，prompt templates 完整 |\n| Overall Assessment | 3.0/5 | Findings 级别 |\n| Confidence | 4/5 | 仔细阅读全文含附录，熟悉 zero-shot IE 和统计方法论 |\n\n---\n\n## 上轮 Open Issues 修复状态检查\n\n### Critical Issues\n\n**R10-N1: 因果语言 ('driven', 'channels', 'shape') 超出证据边界**\n→ **[MOSTLY FIXED]** Title 已改为 \"Predict\"（非 \"Shape\"）。正文主体（Introduction/Results/Discussion）未发现 \"channels\"，\"driven\" 仅出现在 Related Work 引用他人方法名称（\"Schema-Driven Decoding\"）中。但 Appendix 仍有残余：Appendix N（cross-model 70B）使用 \"count-driven decline\"（main.tex L502, L508），Appendix P（few-shot）使用 \"BCS-driven confusability effect\"（main.tex L513）。虽然 Limitations §7 明确声明 \"correlational evidence with controlled stratification\"，附录中的因果措辞仍与此声明不一致。**降级为 Should-Fix**。\n\n**R10-N2: Pair→batch 聚合推理链叙事误导**\n→ **[FIXED]** Discussion §6 第2段现在明确分层叙述：unconditional $r^2 = 1.3$-$1.7\\%$ → conditional $R^2 \\approx 7\\%$（non-zero pairs）→ batch $R^2 \\approx 22\\%$（~3× amplification）。Appendix I（Pair-to-Batch Aggregation Simulation）明确标注为 \"illustrative explanatory model\"，与 Practical magnitude 段的直接实证 $R^2 = 0.218$ 明确区分。叙事链条清晰，不再误导。\n\n**R10-N3: TOST ±3pp margin external anchoring**\n→ **[FIXED]** Appendix D（Equivalence margin justification）提供三重 anchoring：(1) Empirical: batch SD ≈ 4.6pp；(2) Practical: <3pp 低于 deployment threshold；(3) Statistical: 3pp ≈ 0.5×SD ≈ Cohen's $d$ 0.5。TOST sensitivity table（±1 到 ±5pp）展示 robustness。锚定充分。\n\n**R11-N1: NER Dimension 2 batch-level null/opposite 但 title/abstract 泛化为 cross-task**\n→ **[FIXED]** Title 使用宽泛的 \"Schema Complexity\"（涵盖 count + confusability），不单独宣称 confusability cross-task。Abstract 明确写 \"BCS explains 22–53% of cross-batch accuracy variance in RE **but not in NER**, where the signal is absent despite significant pairwise effects.\" Contribution 3 明确限定 \"batch-level confusability effects are specific to RE.\" Discussion 有专段 \"Task-dependent batch-level effects\" 分析原因。不再 overclaim。\n\n**R11-N2: 核心效应量过小 (2.2pp) practical significance 存疑**\n→ **[PARTIALLY ADDRESSED — 降级为 Should-Fix]** 论文多处透明报告：Abstract 写 \"≈2.2 pp in typical batches\"；Practical magnitude 段给出 CI [0.4, 4.0]pp；Discussion 给出 practitioner threshold（top-quartile BCS > 0.59 → 3-5pp）。Limitations item 2 承认 \"Pairwise SCS explains 1.3–1.7% of type confusion variance\"。但论文将 BCS 定位为 \"lightweight pre-hoc screen\"，而 3-5pp 的 screening 价值在实际部署中是否足以改变决策仍然存疑。此问题更多是 findings 本身的局限而非写作问题，因此降级为 Should-Fix。\n\n### Warning Issues\n\n**R10-W3: Abstract 数字密度过高**\n→ **[FIXED]** 当前 Abstract 仅保留 3 个核心数字（−49pp, 2.2pp, 22-53%），密度合理。\n\n**R10-W4: Contribution list 过长**\n→ **[FIXED]** 4 条贡献，每条 1-2 行，无嵌入数字，采用方法论声明格式（\"We conduct...\"/\"We validate...\"/\"We show...\"/\"We report...\"），引用对应 section。格式规范。\n\n**R10-W5: BCS 'generalizes across tasks' overclaiming**\n→ **[FIXED]** Contribution 3 明确限定 \"batch-level confusability effects are specific to RE\"。Discussion 明确 \"BCS is a useful pre-hoc screening tool for RE schema design but not for NER.\"\n\n**R10-W7: Supplementary 与 appendix 重复**\n→ **[FIXED]** 未发现独立 supplementary 文件；所有补充材料均在 Appendix（main.tex）中。无重复问题。\n\n**R11-W1: Discussion 过短**\n→ **[MOSTLY FIXED]** Discussion 现有 4 段实质内容：(1) Boundary conditions, (2) Why embedding similarity predicts confusion, (3) Task-dependent batch-level effects, (4) Practical implications。包含 practitioner recommendations（top-quartile BCS threshold, count reduction for NER）。但 training-based IE 对比仅一句话（\"fine-tuned models may learn type boundaries that reduce confusability effects\"），较单薄。Conclusion 仅 3 句，过于简短，缺少 future work 展望（SDGD future directions 段在 §5 而非 Conclusion 中）。\n\n**R11-W2: TOST 术语未展开**\n→ **[NOT FIXED]** Introduction L15 首次使用 \"TOST $p = 0.003$\"，未展开。展开出现在 Results §4.4：\"Two One-Sided Tests (TOST)\"。按 ACL 规范，首次出现必须展开。\n\n**R11-W3: Prompt variant analysis 无 multiple comparison correction**\n→ **[ADDRESSED]** Appendix G（Prompt Variants）明确解释不用 Bonferroni 的理由：\"assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal\"，引用 Rothman (1990)，并以 directional consistency（7/8 conditions negative）作为证据。理由合理。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Introduction \"五发现\"段 Finding (1) 仍过于密集\n- 具体位置：introduction.tex L15\n- 问题：Finding (1) 是一个 56 词的复合句，包含冒号、两个括号插入、分号、and/but 转折，一句话内塞入：两维度名称 + count magnitude + confusability magnitude + TOST结果 + NER coupling exception。读者需多次回读才能解析。Findings (2)-(5) 密度合理。\n- 为什么影响接收：Introduction 的前 30 秒阅读体验直接影响审稿人对论文的第一印象。Finding (1) 作为最核心的发现，可读性不佳会降低说服力。\n- 建议修改方向：拆为 2-3 句。第一句写两维度和主次关系；第二句写 TOST bounded association；第三句写 NER 的例外。同时在此处展开 TOST 首次缩写。\n\n**N2** [critical] Conclusion 过于简短（3 句话），缺少 future work 和 broader impact\n- 具体位置：discussion.tex L18-19\n- 问题：Conclusion 仅 3 句复述主要发现，无 future work 方向、无 broader implications、无与 training-based IE 的对比展望。SDGD future directions（coarse-to-fine、retrieval routing、calibrated generation）出现在 §5 而非 Conclusion，审稿人在结尾无法看到 forward-looking vision。\n- 为什么影响接收：Findings 论文的 Conclusion 需要让审稿人看到研究的延伸价值。当前 Conclusion 读起来像一个 TL;DR 而非一个有洞察的收尾。\n- 建议修改方向：扩展至 5-8 句，包含：(1) 核心发现总结（现有），(2) 与 training-based IE 的关系和对比（fine-tuning 是否消除 confusability effect？），(3) 主要 future directions 从 §5 移至此处或重述，(4) broader implication（schema design principles for any prompt-based label discrimination task）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] TOST 首次出现未展开\n- 具体位置：introduction.tex L15\n- 问题：TOST 在 Introduction 首次出现时写为 \"TOST $p = 0.003$\"，未展开为 \"Two One-Sided Tests (TOST)\"。展开在 results.tex L87（§4.4）才出现。\n- 建议：在 Introduction L15 首次使用处展开，或将 §4.4 的展开提前。\n\n**W2** [warning] Appendix 残余因果语言（\"count-driven\", \"BCS-driven\"）\n- 具体位置：main.tex L502, L508（Appendix N: cross-model 70B）, L513（Appendix P: few-shot）\n- 问题：\"count-driven decline\"、\"BCS-driven confusability effect\" 暗示因果关系，与 Limitations §7 的 \"correlational evidence\" 声明不一致。\n- 建议：替换为 \"count-related decline\"、\"BCS-associated confusability effect\"，与正文主体措辞一致。\n\n**W3** [warning] Practical significance 论证仍偏弱\n- 具体位置：Discussion §6 \"Practical implications\" 段\n- 问题：论文将 BCS 定位为 \"lightweight pre-hoc screen\"，但 typical gap 仅 2.2pp（CI 下界 0.4pp），top-quartile screening 仅改善 3-5pp。对于 RE deployment，这一水平的 screening 是否足以改变 schema design 决策？论文缺少与现有 schema optimization 方法（如 PARSE, LLM-PEE）在实际效果上的定量对比。\n- 建议：(1) 明确 3-5pp 在什么部署场景下有实际价值（如高精度需求场景 vs 一般场景）；(2) 讨论 BCS screening 相对于直接 few-shot augmentation 的成本效益。\n\n**W4** [warning] Training-based IE 对比仅一句话\n- 具体位置：discussion.tex L14 末尾\n- 问题：\"These results apply to the training-free setting; fine-tuned models may learn type boundaries that reduce confusability effects\" 是唯一一处 training-based IE 对比。审稿人会问：fine-tuned models 是否也受 schema complexity 影响？如果是，本文的发现范围更广；如果不是，需要解释为什么。\n- 建议：扩展 2-3 句，至少引用 supervised IE 中的 schema scaling 工作或提出合理推测。\n\n**W5** [warning] References.bib 有 3 个 orphan entries\n- 具体位置：references.bib\n- 问题：`wellek2010testing`、`perneger-1998`、`llm-calibration-survey-2024` 在所有 .tex 文件中均未被 \\cite。虽然 BibTeX 不会将未引用条目编入参考文献，但 orphan entries 暗示写作过程中删除了相关讨论但未清理 bib。\n- 建议：删除未引用条目，或在相关位置补充引用。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 中 \"spanning NER, RE, and event detection across four datasets\" 可以更精炼，\"across four datasets spanning NER, RE, and event detection\" 语序更自然。\n- Appendix 编号使用字母（A-P）但正文中引用时混用 \"Appendix~\\ref{}\" 和 \"Appendix\"，格式不完全统一。\n- Table 1 的 \"Embedding\" 列（Qwen3-32B vs MiniLM）信息重要但可能让读者困惑为什么不同数据集用不同 embedding；§3.1 有解释但 caption 中未提及原因。\n- Conclusion 中 \"BCS enables pre-hoc screening\" 是一个 fragment，不是完整句子。\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：BCS-controlled stratification、within-pool comparison、TOST equivalence testing、cross-model/cross-prompt/cross-seed validation 构成了 NLP 分析论文中少见的严密控制设计。Permutation test for slope equivalence ($p = 0.60$) 和 variance decomposition 是亮点。\n\n2. **结果报告诚实透明**：NER batch-level null result、SDGD failure、2×2 factorial inconclusive、logit-scale TOST inconclusive 等负面/不确定结果均如实报告，不做选择性强调。这在该领域不常见。\n\n3. **Negative results 有社区价值**：merge amplification（precision 0.56→0.21）和 routing failure 的诊断解释了为什么 decompose-then-merge pipelines 在 NER 上失败，为后续工作提供了明确的瓶颈定位。\n\n4. **Cross-validation 广度**：4 datasets × 3 tasks × 3 models × 4 prompt variants × 3 seeds，覆盖面远超同类工作。Centrality confound 在 MAVEN 上的发现和处理方式展示了良好的分析深度。\n\n5. **Statistical methodology 规范**：Bootstrap CI、permutation tests、TOST equivalence with sensitivity analysis、cluster-robust CIs、variance decomposition 等统计方法使用得当，大部分超过 NLP 论文的平均统计严谨度。\n\n---\n\n## 新颖性专项评估\n\n**核心发现的新颖性**：\n- \"Count > confusability by ~20×\" 的定量结论有信息量，但 count degradation 本身已被多项工作观察到（Li et al. 2023, LLM-PEE）。新增贡献在于 controlled isolation 和量化比较，这更接近 \"validation\" 而非 \"discovery\"。\n- SCS/BCS 的形式定义与 LLM-PEE 的 partitioning criterion 相同（论文自己在 Related Work 中承认）。贡献在框架而非指标本身。\n- Negative results（SDGD failure）是论文最具社区价值的部分，但主要是实验验证而非理论洞察。\n\n**与同期工作的差异化**：\n- 相比 LLM-PEE：分析 vs 工程，complementary 关系清晰\n- 相比 PARSE：schema optimization vs schema analysis，方向不同\n- 论文 positioning 为 \"controlled empirical study\" 而非 \"new method\" 是准确的\n\n**总体新颖性判断**：moderate。价值在于严谨的量化分析和诚实的 negative results，但不构成 conceptual breakthrough。适合 Findings。\n",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 12 审稿报告\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)\n**审查侧重**: 新颖性 + 写作质量 + 格式合规\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 方法论严谨、结果诚实的 controlled study，但核心效应量小（typical 2.2pp）、findings 可预期程度较高，达到 Findings 收录标准但 excitement 不足以进入主会议。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨（BCS-controlled stratification、TOST equivalence、cross-model/cross-prompt validation），但2×2 factorial和logit-scale TOST均 inconclusive；NER batch-level null result限制了 cross-task generalization |\n| Excitement | 2.5/5 | 核心发现（count > confusability 20×）有量化价值但非意外；SCS/BCS 非新指标；negative results 有社区价值但 practical utility 有限（BCS screening 仅改善 3-5pp） |\n| Reproducibility | 4/5 | 实验细节充分（decoding params、seed、batch构造协议、bootstrap参数），承诺开源，prompt templates 完整 |\n| Overall Assessment | 3.0/5 | Findings 级别 |\n| Confidence | 4/5 | 仔细阅读全文含附录，熟悉 zero-shot IE 和统计方法论 |\n\n---\n\n## 上轮 Open Issues 修复状态检查\n\n### Critical Issues\n\n**R10-N1: 因果语言 ('driven', 'channels', 'shape') 超出证据边界**\n→ **[MOSTLY FIXED]** Title 已改为 \"Predict\"（非 \"Shape\"）。正文主体（Introduction/Results/Discussion）未发现 \"channels\"，\"driven\" 仅出现在 Related Work 引用他人方法名称（\"Schema-Driven Decoding\"）中。但 Appendix 仍有残余：Appendix N（cross-model 70B）使用 \"count-driven decline\"（main.tex L502, L508），Appendix P（few-shot）使用 \"BCS-driven confusability effect\"（main.tex L513）。虽然 Limitations §7 明确声明 \"correlational evidence with controlled stratification\"，附录中的因果措辞仍与此声明不一致。**降级为 Should-Fix**。\n\n**R10-N2: Pair→batch 聚合推理链叙事误导**\n→ **[FIXED]** Discussion §6 第2段现在明确分层叙述：unconditional $r^2 = 1.3$-$1.7\\%$ → conditional $R^2 \\approx 7\\%$（non-zero pairs）→ batch $R^2 \\approx 22\\%$（~3× amplification）。Appendix I（Pair-to-Batch Aggregation Simulation）明确标注为 \"illustrative explanatory model\"，与 Practical magnitude 段的直接实证 $R^2 = 0.218$ 明确区分。叙事链条清晰，不再误导。\n\n**R10-N3: TOST ±3pp margin external anchoring**\n→ **[FIXED]** Appendix D（Equivalence margin justification）提供三重 anchoring：(1) Empirical: batch SD ≈ 4.6pp；(2) Practical: <3pp 低于 deployment threshold；(3) Statistical: 3pp ≈ 0.5×SD ≈ Cohen's $d$ 0.5。TOST sensitivity table（±1 到 ±5pp）展示 robustness。锚定充分。\n\n**R11-N1: NER Dimension 2 batch-level null/opposite 但 title/abstract 泛化为 cross-task**\n→ **[FIXED]** Title 使用宽泛的 \"Schema Complexity\"（涵盖 count + confusability），不单独宣称 confusability cross-task。Abstract 明确写 \"BCS explains 22–53% of cross-batch accuracy variance in RE **but not in NER**, where the signal is absent despite significant pairwise effects.\" Contribution 3 明确限定 \"batch-level confusability effects are specific to RE.\" Discussion 有专段 \"Task-dependent batch-level effects\" 分析原因。不再 overclaim。\n\n**R11-N2: 核心效应量过小 (2.2pp) practical significance 存疑**\n→ **[PARTIALLY ADDRESSED — 降级为 Should-Fix]** 论文多处透明报告：Abstract 写 \"≈2.2 pp in typical batches\"；Practical magnitude 段给出 CI [0.4, 4.0]pp；Discussion 给出 practitioner threshold（top-quartile BCS > 0.59 → 3-5pp）。Limitations item 2 承认 \"Pairwise SCS explains 1.3–1.7% of type confusion variance\"。但论文将 BCS 定位为 \"lightweight pre-hoc screen\"，而 3-5pp 的 screening 价值在实际部署中是否足以改变决策仍然存疑。此问题更多是 findings 本身的局限而非写作问题，因此降级为 Should-Fix。\n\n### Warning Issues\n\n**R10-W3: Abstract 数字密度过高**\n→ **[FIXED]** 当前 Abstract 仅保留 3 个核心数字（−49pp, 2.2pp, 22-53%），密度合理。\n\n**R10-W4: Contribution list 过长**\n→ **[FIXED]** 4 条贡献，每条 1-2 行，无嵌入数字，采用方法论声明格式（\"We conduct...\"/\"We validate...\"/\"We show...\"/\"We report...\"），引用对应 section。格式规范。\n\n**R10-W5: BCS 'generalizes across tasks' overclaiming**\n→ **[FIXED]** Contribution 3 明确限定 \"batch-level confusability effects are specific to RE\"。Discussion 明确 \"BCS is a useful pre-hoc screening tool for RE schema design but not for NER.\"\n\n**R10-W7: Supplementary 与 appendix 重复**\n→ **[FIXED]** 未发现独立 supplementary 文件；所有补充材料均在 Appendix（main.tex）中。无重复问题。\n\n**R11-W1: Discussion 过短**\n→ **[MOSTLY FIXED]** Discussion 现有 4 段实质内容：(1) Boundary conditions, (2) Why embedding similarity predicts confusion, (3) Task-dependent batch-level effects, (4) Practical implications。包含 practitioner recommendations（top-quartile BCS threshold, count reduction for NER）。但 training-based IE 对比仅一句话（\"fine-tuned models may learn type boundaries that reduce confusability effects\"），较单薄。Conclusion 仅 3 句，过于简短，缺少 future work 展望（SDGD future directions 段在 §5 而非 Conclusion 中）。\n\n**R11-W2: TOST 术语未展开**\n→ **[NOT FIXED]** Introduction L15 首次使用 \"TOST $p = 0.003$\"，未展开。展开出现在 Results §4.4：\"Two One-Sided Tests (TOST)\"。按 ACL 规范，首次出现必须展开。\n\n**R11-W3: Prompt variant analysis 无 multiple comparison correction**\n→ **[ADDRESSED]** Appendix G（Prompt Variants）明确解释不用 Bonferroni 的理由：\"assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal\"，引用 Rothman (1990)，并以 directional consistency（7/8 conditions negative）作为证据。理由合理。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Introduction \"五发现\"段 Finding (1) 仍过于密集\n- 具体位置：introduction.tex L15\n- 问题：Finding (1) 是一个 56 词的复合句，包含冒号、两个括号插入、分号、and/but 转折，一句话内塞入：两维度名称 + count magnitude + confusability magnitude + TOST结果 + NER coupling exception。读者需多次回读才能解析。Findings (2)-(5) 密度合理。\n- 为什么影响接收：Introduction 的前 30 秒阅读体验直接影响审稿人对论文的第一印象。Finding (1) 作为最核心的发现，可读性不佳会降低说服力。\n- 建议修改方向：拆为 2-3 句。第一句写两维度和主次关系；第二句写 TOST bounded association；第三句写 NER 的例外。同时在此处展开 TOST 首次缩写。\n\n**N2** [critical] Conclusion 过于简短（3 句话），缺少 future work 和 broader impact\n- 具体位置：discussion.tex L18-19\n- 问题：Conclusion 仅 3 句复述主要发现，无 future work 方向、无 broader implications、无与 training-based IE 的对比展望。SDGD future directions（coarse-to-fine、retrieval routing、calibrated generation）出现在 §5 而非 Conclusion，审稿人在结尾无法看到 forward-looking vision。\n- 为什么影响接收：Findings 论文的 Conclusion 需要让审稿人看到研究的延伸价值。当前 Conclusion 读起来像一个 TL;DR 而非一个有洞察的收尾。\n- 建议修改方向：扩展至 5-8 句，包含：(1) 核心发现总结（现有），(2) 与 training-based IE 的关系和对比（fine-tuning 是否消除 confusability effect？），(3) 主要 future directions 从 §5 移至此处或重述，(4) broader implication（schema design principles for any prompt-based label discrimination task）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] TOST 首次出现未展开\n- 具体位置：introduction.tex L15\n- 问题：TOST 在 Introduction 首次出现时写为 \"TOST $p = 0.003$\"，未展开为 \"Two One-Sided Tests (TOST)\"。展开在 results.tex L87（§4.4）才出现。\n- 建议：在 Introduction L15 首次使用处展开，或将 §4.4 的展开提前。\n\n**W2** [warning] Appendix 残余因果语言（\"count-driven\", \"BCS-driven\"）\n- 具体位置：main.tex L502, L508（Appendix N: cross-model 70B）, L513（Appendix P: few-shot）\n- 问题：\"count-driven decline\"、\"BCS-driven confusability effect\" 暗示因果关系，与 Limitations §7 的 \"correlational evidence\" 声明不一致。\n- 建议：替换为 \"count-related decline\"、\"BCS-associated confusability effect\"，与正文主体措辞一致。\n\n**W3** [warning] Practical significance 论证仍偏弱\n- 具体位置：Discussion §6 \"Practical implications\" 段\n- 问题：论文将 BCS 定位为 \"lightweight pre-hoc screen\"，但 typical gap 仅 2.2pp（CI 下界 0.4pp），top-quartile screening 仅改善 3-5pp。对于 RE deployment，这一水平的 screening 是否足以改变 schema design 决策？论文缺少与现有 schema optimization 方法（如 PARSE, LLM-PEE）在实际效果上的定量对比。\n- 建议：(1) 明确 3-5pp 在什么部署场景下有实际价值（如高精度需求场景 vs 一般场景）；(2) 讨论 BCS screening 相对于直接 few-shot augmentation 的成本效益。\n\n**W4** [warning] Training-based IE 对比仅一句话\n- 具体位置：discussion.tex L14 末尾\n- 问题：\"These results apply to the training-free setting; fine-tuned models may learn type boundaries that reduce confusability effects\" 是唯一一处 training-based IE 对比。审稿人会问：fine-tuned models 是否也受 schema complexity 影响？如果是，本文的发现范围更广；如果不是，需要解释为什么。\n- 建议：扩展 2-3 句，至少引用 supervised IE 中的 schema scaling 工作或提出合理推测。\n\n**W5** [warning] References.bib 有 3 个 orphan entries\n- 具体位置：references.bib\n- 问题：`wellek2010testing`、`perneger-1998`、`llm-calibration-survey-2024` 在所有 .tex 文件中均未被 \\cite。虽然 BibTeX 不会将未引用条目编入参考文献，但 orphan entries 暗示写作过程中删除了相关讨论但未清理 bib。\n- 建议：删除未引用条目，或在相关位置补充引用。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 中 \"spanning NER, RE, and event detection across four datasets\" 可以更精炼，\"across four datasets spanning NER, RE, and event detection\" 语序更自然。\n- Appendix 编号使用字母（A-P）但正文中引用时混用 \"Appendix~\\ref{}\" 和 \"Appendix\"，格式不完全统一。\n- Table 1 的 \"Embedding\" 列（Qwen3-32B vs MiniLM）信息重要但可能让读者困惑为什么不同数据集用不同 embedding；§3.1 有解释但 caption 中未提及原因。\n- Conclusion 中 \"BCS enables pre-hoc screening\" 是一个 fragment，不是完整句子。\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：BCS-controlled stratification、within-pool comparison、TOST equivalence testing、cross-model/cross-prompt/cross-seed validation 构成了 NLP 分析论文中少见的严密控制设计。Permutation test for slope equivalence ($p = 0.60$) 和 variance decomposition 是亮点。\n\n2. **结果报告诚实透明**：NER batch-level null result、SDGD failure、2×2 factorial inconclusive、logit-scale TOST inconclusive 等负面/不确定结果均如实报告，不做选择性强调。这在该领域不常见。\n\n3. **Negative results 有社区价值**：merge amplification（precision 0.56→0.21）和 routing failure 的诊断解释了为什么 decompose-then-merge pipelines 在 NER 上失败，为后续工作提供了明确的瓶颈定位。\n\n4. **Cross-validation 广度**：4 datasets × 3 tasks × 3 models × 4 prompt variants × 3 seeds，覆盖面远超同类工作。Centrality confound 在 MAVEN 上的发现和处理方式展示了良好的分析深度。\n\n5. **Statistical methodology 规范**：Bootstrap CI、permutation tests、TOST equivalence with sensitivity analysis、cluster-robust CIs、variance decomposition 等统计方法使用得当，大部分超过 NLP 论文的平均统计严谨度。\n\n---\n\n## 新颖性专项评估\n\n**核心发现的新颖性**：\n- \"Count > confusability by ~20×\" 的定量结论有信息量，但 count degradation 本身已被多项工作观察到（Li et al. 2023, LLM-PEE）。新增贡献在于 controlled isolation 和量化比较，这更接近 \"validation\" 而非 \"discovery\"。\n- SCS/BCS 的形式定义与 LLM-PEE 的 partitioning criterion 相同（论文自己在 Related Work 中承认）。贡献在框架而非指标本身。\n- Negative results（SDGD failure）是论文最具社区价值的部分，但主要是实验验证而非理论洞察。\n\n**与同期工作的差异化**：\n- 相比 LLM-PEE：分析 vs 工程，complementary 关系清晰\n- 相比 PARSE：schema optimization vs schema analysis，方向不同\n- 论文 positioning 为 \"controlled empirical study\" 而非 \"new method\" 是准确的\n\n**总体新颖性判断**：moderate。价值在于严谨的量化分析和诚实的 negative results，但不构成 conceptual breakthrough。适合 Findings。\n",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-17T14:35:20.872482+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4033
}
```

</details>

---


### Assistant

_source line 838 · 2026-05-17T14:35:29.212304+00:00_

Round 12 审稿报告已提交。

核心判断：**Overall 3.0（Findings 级别）**。论文经过多轮修订后在写作和技术严谨性上有明显进步，大部分 Critical issues 已修复。主要残留问题：

1. **Must-Fix**：Introduction Finding (1) 仍过密（单句56词含多层嵌套），Conclusion 仅3句缺少 future work
2. **Should-Fix**：TOST 首次出现未展开、Appendix 残余因果语言、practical significance 论证偏弱、training-based IE 对比单薄、3个 orphan bib entries
3. **新颖性**：核心发现（count > confusability 20×, typical gap 2.2pp）有量化价值但非意外；SCS/BCS 非新指标；negative results 是最具社区价值的部分。适合 Findings 但 excitement 不足主会议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 26

## Round 26

4 recorded events


### User

_source line 839 · 2026-05-17T14:35:30.589453+00:00_

[Round 12 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 1 审稿报告（方法严谨性 + 实验设计 + 统计分析）

### 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 实验设计和统计分析展现了高于平均水平的严谨性，但 "two dimensions" 的核心 claim 在 NER 上缺乏 batch-level 支撑，pairwise effect size 极小（$r^2 = 1.3\text{-}1.7\%$），confusability 维度的实际意义有待商榷。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨，但核心 claim 的证据在不同任务间不一致；TOST margin 选择可争议；pairwise effect size 极小 |
| Excitement | 3/5 | 问题有实践价值，但 confusability effect 太弱（typical-batch gap 仅 2.2pp），负面结果限制可操作性 |
| Reproducibility | 4/5 | 实验细节充分，prompt 模板完整，声明将发布代码 |
| Overall Assessment | 3.5 | 分析型论文质量中上，但 claim 与证据间存在张力 |
| Confidence | 4/5 | 仔细审查了实验设计和统计方法 |

### Must-Fix 问题（3 个 critical）

**N1** [critical] "Two Dimensions" Claim 跨任务一致性不足
- NER batch-level BCS 效果为零（$r \approx 0$, $n = 450$）
- MAVEN per-type BCS--F1 correlation 控制 centrality 后消失（$p > 0.2$）
- Dimension 2 实际只在 RE（FewRel + DocRED）的 closed-set format 下被 batch-level 验证
- 论文仍在 Abstract/Conclusion 中将其作为跨任务通用发现呈现 → overclaiming
- 建议：重新定位为 "task-specific effect"，调整 Abstract 和 Conclusion

**N2** [critical] Pairwise $r^2 = 1.3\text{-}1.7\%$ 的实际意义论证不充分
- typical-batch gap 仅 2.2pp（95% CI: [0.4, 4.0]），quartile gap 仅 3.9pp
- batch-level $R^2 = 22\%$ 的放大依赖 conditional estimate（only non-zero confusion pairs），unconditional 仅 4.4%
- 引用 behavioral research 标准（Cohen 1988）辩护 "small but real effects" 在 NLP engineering 场景需要更强论证
- 建议：区分 statistical vs practical significance，提供 engineering context

**N3** [critical] TOST Equivalence Margin 选择鲁棒性不足
- ±3pp margin 得到 $p = 0.003$，但 ±2pp 时 marginally equivalent（$p = 0.047$），±1pp inconclusive
- logit-scale TOST 也 inconclusive（$p = 0.209$）
- confusability main effect 仅 2.2pp，±3pp margin 已超过 main effect → "可忽略"的标准过于宽松
- 建议：降低对 separability 的 confidence，讨论 margin 相对于 main effect 的比例

### Should-Fix 问题（5 个 warning）

**W1** 多重比较：Appendix H cross-prompt analysis 中 8 个 correlated tests 在同一数据上不做 correction，仅以 "directional consistency" 辩护不够严谨
**W2** FewRel 合并 train+val splits 的正当化不充分；contamination risk 论证仅靠 n.s. p-value
**W3** Few-NERD long-tail distribution 的 type frequency confound 在 count-curve 中未控制
**W4** SCS 对 Few-NERD 使用 extraction model 自身的 embeddings，circularity 应在正文讨论
**W5** Cross-model validation 仅 3 个 open-weight models（2 个 families），无 proprietary model 验证

### 小问题
- S1: 4 个 orphan bib entries 需清理
- S2: U-shape rebound 的 "type-filtering overhead" 解释缺直接验证
- S3: Table 1 Embedding 列标注可能引起困惑
- S4: "bounded association" 缺乏操作性定义

### 主要优势
- 精心设计的控制实验（count-curve + BCS-controlled + within-pool analysis）
- 统计方法整体选择合理（TOST, permutation, bootstrap, variance decomposition）
- 诚实报告负面结果（SDGD failure, NER null, MAVEN confound）
- 广泛的 sensitivity analysis（4 种 prompt variants, 3 models, cross-embedding, TOST sensitivity）
- 异常详尽的 Limitations section（8 items + multiple comparisons paragraph）

### 格式合规
- 正文 8 页以内（Conclusion 在 page 8 底部结束），Limitations + Checklist 从 page 9 开始 ✓
- ACL review 模板，double-blind，行号开启 ✓
- 22 页总页数（含 Appendix）✓
- 引用格式基本正确，4 个 orphan 需清理

---

请逐条回应上述 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-17T14:37:33.117501+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n## Must-Fix 问题回应\n\n### [REBUT] R1-N1: \"Two Dimensions\" Claim 跨任务一致性不足\n\nR1 认为论文在 Abstract/Conclusion 中将 Dimension 2 作为 \"跨任务通用发现\" 呈现，构成 overclaiming。我认为这一批评**部分有道理但过度**。\n\n**反驳理由：**\n\n1. \"Two dimensions\" 在 pairwise 层面确实是 cross-task 的。Table 2（§4.2）报告 Few-NERD $r = 0.112$ ($p < 0.001$) 和 MAVEN $r = 0.129$ ($p < 0.001$)，pairwise SCS 在 NER 和 ED 上均显著。R1 仅关注 batch-level 效果而忽视了 pairwise 层面的跨任务一致性。\n\n2. Abstract 已明确限定：\"BCS explains 22–53% of cross-batch accuracy variance in RE **but not in NER**, where the signal is absent despite significant pairwise effects.\" 这不是 overclaiming，而是精确报告。\n\n3. Contribution 3（Introduction L25）明确写 \"batch-level confusability effects are specific to RE\"。Discussion §6 第3段专门讨论 \"Task-dependent batch-level effects\"。\n\n4. Conclusion 写 \"with bounded association in RE but coupling in NER\"，这同样是区分了任务差异。\n\n**部分同意点：** Conclusion 确实过于简短（仅3句），使得 task-specificity 的 nuance 被压缩。如果 Conclusion 扩展（我在自己的 N2 中也提出了这一点），可以更充分地阐述 \"pairwise cross-task, batch-level RE-specific\" 的分层结论。但当前 Abstract 和 Introduction 的表述并不构成 overclaiming。\n\n---\n\n### [AGREE] R1-N2: Pairwise $r^2 = 1.3$-$1.7\\%$ 实际意义论证不充分\n\n同意 practical significance 论证需要加强。Typical-batch gap 2.2pp（CI 下界 0.4pp）确实偏小，引用 behavioral research 标准（Cohen 1988）来辩护 NLP 工程场景下的实际意义不够有力。\n\n**但需要纠正 R1 的一个事实错误：** R1 称 \"batch-level $R^2 = 22\\%$ 的放大依赖 conditional estimate（only non-zero confusion pairs）\"。这不准确。$R^2 = 0.218$ 来自 §4.1 Practical magnitude 段的**直接回归**（\"Direct regression on 100 random 16-type batches from the 80-relation pool\"），是独立的经验测量值。Appendix I（Pair-to-Batch Aggregation Simulation）开篇明确声明 \"It is **not the evidence base** for our claims; the observed batch-level $R^2 = 0.218$ is a direct empirical measurement independent of this simulation.\" Conditional $R^2 \\approx 7\\%$ 仅用于事后解释 aggregation 机制，不参与核心 claim 的证据链。\n\n**同意的核心点：** 即使 $R^2 = 22\\%$ 是直接测量，2.2pp 的 typical gap 在实际部署中是否有 actionable value 确实需要更好的工程场景论证。论文应区分 \"statistically detectable\" 和 \"practically actionable\"。\n\n---\n\n### [AGREE] R1-N3: TOST Equivalence Margin 选择鲁棒性不足\n\n同意。这是论文统计论证中最薄弱的环节。\n\n**关键问题：** ±3pp margin 相对于 2.2pp main effect 的比例（136%）过大。论文自己在 Equivalence margin justification 段中写道 \"A 3pp interaction atop the 2.2pp confusability main effect would represent >130% amplification\"，实际上是在承认 ±3pp 允许 interaction 超过 main effect 本身。这削弱了 \"bounded association\" 的说服力。\n\n**补充证据：**\n- ±2pp 仅 marginally equivalent ($p = 0.047$)，这意味着在更保守的标准下 separability 不确定\n- Logit-scale TOST inconclusive ($p = 0.209$)，论文归因于 limited power 而非 large effect，但 power 不足本身就是问题\n- 2×2 factorial 也 inconclusive ($p_{TOST} = 0.56$)\n\n三项独立的 robustness check 均未能确认 separability，仅有 primary regression 的 ±3pp TOST 成功。论文应降低 \"bounded association\" 的 confidence level，措辞从 \"confirms bounded association\" 调整为 \"suggests bounded association under the primary specification\"。\n\n---\n\n## Should-Fix 问题回应\n\n### [REBUT] R1-W1: Cross-prompt analysis 多重比较\n\nR1 认为 8 个 correlated tests 仅以 \"directional consistency\" 辩护不够严谨。我认为论文的论证是合理的。\n\n**理由：**\n1. Appendix G 明确解释：Bonferroni 假设独立假设，对 correlated prompt variants testing the same underlying signal 是 inappropriate 的。这是统计学教科书级别的正确论断。\n2. 引用 Rothman (1990)（\"No Adjustments Are Needed for Multiple Comparisons\"）是 epidemiology 领域广泛接受的观点。\n3. Directional consistency（7/8 conditions negative）作为补充证据是合理的。论文没有声称所有 8 个条件都显著，而是论证 underlying signal 的方向一致性。\n4. 核心 claim 不依赖于 prompt variant analysis。主要 BCS 效果已在 §4.1 的 primary experiment 中 established（$p < 0.001$）。Prompt variant analysis 是 robustness check，不是 primary evidence。\n\n不过，论文可以额外报告 meta-analytic 合并效应（如 Fisher's method 或 random-effects meta-analysis）来更正式地量化 combined evidence。\n\n### [AGREE] R1-W2: FewRel 合并 train+val splits 的正当化\n\n部分同意。不过论文已提供了多层 contamination 论证，并非仅靠 n.s. p-value：\n\n- Train-origin accuracy **更低**（−8.8pp），方向相反于 contamination hypothesis（Limitations §4）\n- Monotonic count-degradation 无法被 uniform contamination 解释\n- BCS slope consistency（permutation $p = 0.60$）\n- Appendix L 的 covariate 分析：train-origin ratio 不显著（$p = 0.245$），BCS partial effect 不变\n- DocRED replication（$R^2 = 0.53$）提供 lower-contamination-risk 的独立验证\n\n这些论证组合是合理的。但 R1 提出的 \"正当化不充分\" 主要指 **为什么需要合并 train+val** 这一设计决策本身。论文在 §3.1 解释了原因（\"Since the validation split covers only 16 relations, we combine... to obtain the full 80-relation pool required for schema-scale experiments\"），但这个解释可以更突出。\n\n### [AGREE] R1-W3: Few-NERD type frequency confound\n\n同意这是一个有效的 concern。Few-NERD 的 long-tail 分布意味着较大的 batch 更可能包含低频 type，而低频 type 的 recall 本身更低，与 count 混淆。\n\n**缓解因素：**\n- FewRel（balanced design）是 BCS 分析的 primary dataset，已消除 frequency confound（§4.1 开头明确说明）\n- Appendix G（prompt sensitivity）发现 NER 的 batch-level BCS-frequency confound（$r(\\text{BCS}, \\text{freq}) = 0.53$），控制后 partial correlation 不显著\n- Count curves 用于建立 trend direction，不做精确 magnitude estimation（§4.1：\"magnitude estimation relies on the higher-powered BCS-controlled experiments\"）\n\n但 R1 说得对：正文 count-curve 段（§4.1）应明确 flag 这一 confound。当前的 mitigation 分散在 Appendix 中，正文读者可能遗漏。\n\n### [REBUT] R1-W4: SCS circularity（Few-NERD 用 extraction model embeddings）\n\n论文已在两处讨论此问题：\n\n1. **§3.1 正文**：\"a cross-embedding check confirms directional consistency (MiniLM $r = 0.172$, Qwen3 $r = 0.138$; Appendix)\"。关键发现：**独立 MiniLM embedding 的相关性反而更高**（0.172 > 0.138），说明 Qwen3 SCS 是 conservative estimate 而非 inflated。\n\n2. **Limitations item 4**：\"For Few-NERD, SCS is computed from the extraction model's own embeddings (Qwen3), creating a shared-representation dependency. MiniLM cross-check yields a conservative but directionally consistent estimate ($r = 0.172$ vs $r = 0.138$; confusion matrix correlation 0.894), suggesting the effect is not an artifact of shared representations.\"\n\n如果 circularity 导致 inflation，我们应该看到 Qwen3 $r$ > MiniLM $r$，但实际相反。论文已在正文和 Limitations 中均讨论了此问题，不只在 Limitations 中。R1 的 concern 已被论文现有分析回应。\n\n### [AGREE] R1-W5: Cross-model 仅 open-weight models\n\n同意这是一个合理的局限性。3 个 models（2 个 families）确实有限。\n\n不过：\n- Limitations item 1 已明确承认 \"Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified\"\n- 使用 open-weight models 是可复现性的需要（proprietary model 的 API 版本频繁变化，结果不可复现）\n- 3 个模型横跨 8B/32B/70B 三个 scale，已覆盖一定范围\n\n这更多是一个 **inherent limitation** 而非 **fixable flaw**。对于 Findings 级别的论文，当前的 model coverage 加上明确的 limitation 声明是可接受的。\n",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n## Must-Fix 问题回应\n\n### [REBUT] R1-N1: \"Two Dimensions\" Claim 跨任务一致性不足\n\nR1 认为论文在 Abstract/Conclusion 中将 Dimension 2 作为 \"跨任务通用发现\" 呈现，构成 overclaiming。我认为这一批评**部分有道理但过度**。\n\n**反驳理由：**\n\n1. \"Two dimensions\" 在 pairwise 层面确实是 cross-task 的。Table 2（§4.2）报告 Few-NERD $r = 0.112$ ($p < 0.001$) 和 MAVEN $r = 0.129$ ($p < 0.001$)，pairwise SCS 在 NER 和 ED 上均显著。R1 仅关注 batch-level 效果而忽视了 pairwise 层面的跨任务一致性。\n\n2. Abstract 已明确限定：\"BCS explains 22–53% of cross-batch accuracy variance in RE **but not in NER**, where the signal is absent despite significant pairwise effects.\" 这不是 overclaiming，而是精确报告。\n\n3. Contribution 3（Introduction L25）明确写 \"batch-level confusability effects are specific to RE\"。Discussion §6 第3段专门讨论 \"Task-dependent batch-level effects\"。\n\n4. Conclusion 写 \"with bounded association in RE but coupling in NER\"，这同样是区分了任务差异。\n\n**部分同意点：** Conclusion 确实过于简短（仅3句），使得 task-specificity 的 nuance 被压缩。如果 Conclusion 扩展（我在自己的 N2 中也提出了这一点），可以更充分地阐述 \"pairwise cross-task, batch-level RE-specific\" 的分层结论。但当前 Abstract 和 Introduction 的表述并不构成 overclaiming。\n\n---\n\n### [AGREE] R1-N2: Pairwise $r^2 = 1.3$-$1.7\\%$ 实际意义论证不充分\n\n同意 practical significance 论证需要加强。Typical-batch gap 2.2pp（CI 下界 0.4pp）确实偏小，引用 behavioral research 标准（Cohen 1988）来辩护 NLP 工程场景下的实际意义不够有力。\n\n**但需要纠正 R1 的一个事实错误：** R1 称 \"batch-level $R^2 = 22\\%$ 的放大依赖 conditional estimate（only non-zero confusion pairs）\"。这不准确。$R^2 = 0.218$ 来自 §4.1 Practical magnitude 段的**直接回归**（\"Direct regression on 100 random 16-type batches from the 80-relation pool\"），是独立的经验测量值。Appendix I（Pair-to-Batch Aggregation Simulation）开篇明确声明 \"It is **not the evidence base** for our claims; the observed batch-level $R^2 = 0.218$ is a direct empirical measurement independent of this simulation.\" Conditional $R^2 \\approx 7\\%$ 仅用于事后解释 aggregation 机制，不参与核心 claim 的证据链。\n\n**同意的核心点：** 即使 $R^2 = 22\\%$ 是直接测量，2.2pp 的 typical gap 在实际部署中是否有 actionable value 确实需要更好的工程场景论证。论文应区分 \"statistically detectable\" 和 \"practically actionable\"。\n\n---\n\n### [AGREE] R1-N3: TOST Equivalence Margin 选择鲁棒性不足\n\n同意。这是论文统计论证中最薄弱的环节。\n\n**关键问题：** ±3pp margin 相对于 2.2pp main effect 的比例（136%）过大。论文自己在 Equivalence margin justification 段中写道 \"A 3pp interaction atop the 2.2pp confusability main effect would represent >130% amplification\"，实际上是在承认 ±3pp 允许 interaction 超过 main effect 本身。这削弱了 \"bounded association\" 的说服力。\n\n**补充证据：**\n- ±2pp 仅 marginally equivalent ($p = 0.047$)，这意味着在更保守的标准下 separability 不确定\n- Logit-scale TOST inconclusive ($p = 0.209$)，论文归因于 limited power 而非 large effect，但 power 不足本身就是问题\n- 2×2 factorial 也 inconclusive ($p_{TOST} = 0.56$)\n\n三项独立的 robustness check 均未能确认 separability，仅有 primary regression 的 ±3pp TOST 成功。论文应降低 \"bounded association\" 的 confidence level，措辞从 \"confirms bounded association\" 调整为 \"suggests bounded association under the primary specification\"。\n\n---\n\n## Should-Fix 问题回应\n\n### [REBUT] R1-W1: Cross-prompt analysis 多重比较\n\nR1 认为 8 个 correlated tests 仅以 \"directional consistency\" 辩护不够严谨。我认为论文的论证是合理的。\n\n**理由：**\n1. Appendix G 明确解释：Bonferroni 假设独立假设，对 correlated prompt variants testing the same underlying signal 是 inappropriate 的。这是统计学教科书级别的正确论断。\n2. 引用 Rothman (1990)（\"No Adjustments Are Needed for Multiple Comparisons\"）是 epidemiology 领域广泛接受的观点。\n3. Directional consistency（7/8 conditions negative）作为补充证据是合理的。论文没有声称所有 8 个条件都显著，而是论证 underlying signal 的方向一致性。\n4. 核心 claim 不依赖于 prompt variant analysis。主要 BCS 效果已在 §4.1 的 primary experiment 中 established（$p < 0.001$）。Prompt variant analysis 是 robustness check，不是 primary evidence。\n\n不过，论文可以额外报告 meta-analytic 合并效应（如 Fisher's method 或 random-effects meta-analysis）来更正式地量化 combined evidence。\n\n### [AGREE] R1-W2: FewRel 合并 train+val splits 的正当化\n\n部分同意。不过论文已提供了多层 contamination 论证，并非仅靠 n.s. p-value：\n\n- Train-origin accuracy **更低**（−8.8pp），方向相反于 contamination hypothesis（Limitations §4）\n- Monotonic count-degradation 无法被 uniform contamination 解释\n- BCS slope consistency（permutation $p = 0.60$）\n- Appendix L 的 covariate 分析：train-origin ratio 不显著（$p = 0.245$），BCS partial effect 不变\n- DocRED replication（$R^2 = 0.53$）提供 lower-contamination-risk 的独立验证\n\n这些论证组合是合理的。但 R1 提出的 \"正当化不充分\" 主要指 **为什么需要合并 train+val** 这一设计决策本身。论文在 §3.1 解释了原因（\"Since the validation split covers only 16 relations, we combine... to obtain the full 80-relation pool required for schema-scale experiments\"），但这个解释可以更突出。\n\n### [AGREE] R1-W3: Few-NERD type frequency confound\n\n同意这是一个有效的 concern。Few-NERD 的 long-tail 分布意味着较大的 batch 更可能包含低频 type，而低频 type 的 recall 本身更低，与 count 混淆。\n\n**缓解因素：**\n- FewRel（balanced design）是 BCS 分析的 primary dataset，已消除 frequency confound（§4.1 开头明确说明）\n- Appendix G（prompt sensitivity）发现 NER 的 batch-level BCS-frequency confound（$r(\\text{BCS}, \\text{freq}) = 0.53$），控制后 partial correlation 不显著\n- Count curves 用于建立 trend direction，不做精确 magnitude estimation（§4.1：\"magnitude estimation relies on the higher-powered BCS-controlled experiments\"）\n\n但 R1 说得对：正文 count-curve 段（§4.1）应明确 flag 这一 confound。当前的 mitigation 分散在 Appendix 中，正文读者可能遗漏。\n\n### [REBUT] R1-W4: SCS circularity（Few-NERD 用 extraction model embeddings）\n\n论文已在两处讨论此问题：\n\n1. **§3.1 正文**：\"a cross-embedding check confirms directional consistency (MiniLM $r = 0.172$, Qwen3 $r = 0.138$; Appendix)\"。关键发现：**独立 MiniLM embedding 的相关性反而更高**（0.172 > 0.138），说明 Qwen3 SCS 是 conservative estimate 而非 inflated。\n\n2. **Limitations item 4**：\"For Few-NERD, SCS is computed from the extraction model's own embeddings (Qwen3), creating a shared-representation dependency. MiniLM cross-check yields a conservative but directionally consistent estimate ($r = 0.172$ vs $r = 0.138$; confusion matrix correlation 0.894), suggesting the effect is not an artifact of shared representations.\"\n\n如果 circularity 导致 inflation，我们应该看到 Qwen3 $r$ > MiniLM $r$，但实际相反。论文已在正文和 Limitations 中均讨论了此问题，不只在 Limitations 中。R1 的 concern 已被论文现有分析回应。\n\n### [AGREE] R1-W5: Cross-model 仅 open-weight models\n\n同意这是一个合理的局限性。3 个 models（2 个 families）确实有限。\n\n不过：\n- Limitations item 1 已明确承认 \"Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified\"\n- 使用 open-weight models 是可复现性的需要（proprietary model 的 API 版本频繁变化，结果不可复现）\n- 3 个模型横跨 8B/32B/70B 三个 scale，已覆盖一定范围\n\n这更多是一个 **inherent limitation** 而非 **fixable flaw**。对于 Findings 级别的论文，当前的 model coverage 加上明确的 limitation 声明是可接受的。\n",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-17T14:37:36.848500+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3730
}
```

</details>

---


### Assistant

_source line 842 · 2026-05-17T14:37:50.704475+00:00_

交叉回应已提交。总结：

- **R1-N1 (Two Dimensions overclaiming)**: [REBUT] — 论文 Abstract/Contribution/Discussion 已明确限定 batch-level BCS 为 RE-specific，pairwise SCS 确实 cross-task 显著。当前表述不构成 overclaiming，但 Conclusion 过短导致 nuance 被压缩。
- **R1-N2 (Practical significance)**: [AGREE] — 但纠正了一个事实错误：batch $R^2=22\%$ 是直接回归测量，非依赖 conditional estimate。
- **R1-N3 (TOST margin)**: [AGREE] — ±3pp 相对于 2.2pp main effect 的比例过大，三项 robustness check 均未确认 separability，应降低 confidence。
- **R1-W1 (Multiple comparison)**: [REBUT] — Bonferroni 对 correlated tests 不适用，Rothman 1990 引用合理，prompt variant analysis 是 robustness check 非 primary evidence。
- **R1-W2 (FewRel merge)**: [AGREE] — 多层论证已存在但可更突出。
- **R1-W3 (Frequency confound)**: [AGREE] — 正文 count-curve 段应 flag 此 confound。
- **R1-W4 (SCS circularity)**: [REBUT] — MiniLM cross-check $r$ 反而更高，已在正文 §3.1 和 Limitations 讨论。
- **R1-W5 (Open-weight only)**: [AGREE] — 合理局限性，已在 Limitations 声明，对 Findings 级别可接受。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 27

## Round 27

56 recorded events


### User

_source line 843 · 2026-05-18T02:57:27.776391+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 写作完整性 + 格式合规** 审查。

## Venue 信息
- **目标**: EMNLP 2026（通过 ARR May 2026 cycle）
- **截止**: 2026-05-25
- **格式**: Long paper, 8 页正文, ACL style template (`\usepackage[review]{acl}`), double-blind
- **Limitations section**: 必填，不计入页数
- **Responsible NLP Checklist**: 必填

## 论文路径
`projects/schema-dag-extraction/docs/paper/main.tex`（含 12 个 .tex 子文件：abstract, introduction, related_work, experimental_setup, results, sdgd_negative, discussion, checklist, prompt_appendix，以及 main.tex 中的 appendix sections）

## 论文概要
研究 training-free LLM IE 中 schema 复杂度如何预测性能。两维退化模型（count + confusability），SCS/BCS 指标，4 数据集，负面 SDGD 结果。

## 你的审查侧重

重点审查以下方面：

1. **新颖性评估**：
   - SCS 与 LLM-PEE 形式相同，增量贡献是否足够？
   - "controlled study" 的贡献层级：analysis paper vs method paper
   - 负面结果（SDGD 失败）的学术价值
   - 对 NLP 社区的 actionable insights 有多少？

2. **叙事逻辑和写作质量**：
   - Abstract 是否有效传达核心发现？（当前 ~130-140 words，偏短）
   - Introduction 的 findings-contributions 对齐（4 findings vs 4 contributions 是否映射清晰）
   - Discussion/Conclusion 是否充分？（历史反馈指出 Conclusion 仅 3 句，缺 future work）
   - 因果语言控制：Title 用 "Predict" 而非 "Shape"，正文是否一致？
   - AI 写作痕迹：em-dash、-ing phrases、过度分段

3. **Related Work 覆盖度**：
   - 直接竞争者覆盖：LLM-PEE, PARSE, DEE, CROSSAGENTIE 等是否充分定位
   - 是否遗漏重要相关工作？检查 constrained decoding (Willard & Louf 2023 Outlines) 引用
   - Orphan bib entries（wellek2010testing, perneger-1998, llm-calibration-survey-2024 是否存在）
   - 引用密度是否达到 EMNLP 水平

4. **格式合规**：
   - `\documentclass[11pt]{article}` + `\usepackage[review]{acl}` 是否正确
   - 正文是否在 8 页以内（需检查编译后页数）
   - Limitations section 位置和内容
   - Responsible NLP Checklist 完整性
   - 匿名化（作者信息、anonymous review link）
   - Figure/Table caption 自包含性
   - Reference 格式一致性

5. **Contribution framing**：
   - Contribution 3（task-dependent limitations of BCS）是否在包装 NER null result？
   - "首次 controlled study" 声明的限定是否充分？
   - Practical implications（BCS screening at threshold > 0.59）是否有足够支撑？

请输出完整审稿报告，格式：
- Summary (2-3 句)
- Strengths (逐条)
- Weaknesses (逐条，标注 severity: critical/major/minor)
- Questions for Authors
- Missing References
- Overall Assessment (用 EMNLP 2026 ARR 评分: 1-5 scale)
- Confidence (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-18T02:57:37.145240+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-18T02:57:37.145735+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-18T02:57:37.196107+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-18T02:57:37.447704+00:00_

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
…[truncated 48154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-18T02:57:44.430809+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-18T02:57:44.933166+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets, and operationalize confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS, the mean pairwise embedding similarity within a type batch). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); at batch level, BCS explains 22--53\% of cross-batch accuracy variance in RE but not in NER, where the signal is absent despite significant pairwise effects. Schema decomposition fails in both tasks due to merge amplification (NER) and routing failure (RE), which points to structural barriers to confusability-aware extraction.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-18T02:57:44.933616+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-18T02:57:45.387412+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accurac
…[truncated 3094 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-18T02:57:45.438018+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-18T02:57:45.890002+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. Recent work also explores LLM-based data annotation for NER \cite{bogdanov2024nuner,zhang2023llmaaa} and self-improving zero-shot extraction \cite{xie2024selfimproving}. Batch prompting \cite{cheng2023batch} processes multiple inputs per call for efficiency; our count-curve design similarly places multiple types in a single prompt but as an experimental variable rather than an efficiency technique. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. Specifically, LLM-PEE employs union mer
…[truncated 3529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-18T02:57:45.940650+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-18T02:57:46.442666+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound, making it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task i
…[truncated 7789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-18T02:57:46.443195+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-18T02:57:46.855170+00:00_

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
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schem
…[truncated 10874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 411
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-18T02:57:46.856010+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-18T02:57:47.308191+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapsing (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}), confirming that type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!
…[truncated 512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-18T02:57:47.308767+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-18T02:57:50.849389+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across models, suggesting a difficulty ceiling. RE's separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}). Cross-scale evidence (32B vs.\ 8B) shows Dimension~1 replicates fully while Dimension~2 attenuates on smaller models, dropping to near-zero $R^2$ for NER on Llama-3.1-8B (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}). Count-related degradation may partly reflect prompt length (per-type recall 0.586 vs.\ single-pass 0.368, consistent with lost-in-middle effects; \citealt{lost-in-middle-2024}; \citealt{levy-2024-same-task}).
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\% on Few-NERD, $r = 0.112$) because ${\sim}89\%$ of type pairs never produce mutual confusion; among the 11\% with nonzero confusion, conditional $R^2$ rises to 7\%. Correlated pair-level signals then aggregate at the batch level: a Monte Carlo simulation ($\rho_{\mathrm{SCS}} = 0.35$; Appendix~\ref{app:aggregation-sim}) predicts batch $R^2$ of 18--25\%, consistent with the observed 22--53\% in RE. SCS is thus a weak pair-level predictor but a practically useful batch-level screen. We hypothesize that the NER U-shape (\S\ref{sec:count_curves}) reflects a dual-task burden absent in RE: partial schemas require simultaneous span detection and type-membership filtering; at full-schema, filtering becomes vacuous and recall recovers, confirming task-specific pathways.
9	
10	\paragraph{Task-dependent 
…[truncated 2920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3540
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-18T02:57:51.051680+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-18T02:57:51.102482+00:00_

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
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
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
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{llama3
…[truncated 4519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-18T02:57:51.303639+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-18T02:57:51.404631+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-18T02:57:57.681748+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool call

_source line 867 · 2026-05-18T02:57:57.933060+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 868 · 2026-05-18T02:57:57.983625+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-18T02:57:58.084728+00:00_

1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	@article{gemini-team-2024,
6	  title     = {Gemini 1.5: Unlocking Multimodal Understanding Across Millions of Tokens of Context},
7	  author    = {{Gemini Team} and Georgiev, Petko and Lei, Ving Ian and Burnell, Ryan and Bai, Libin and Gulati, Anmol and Tanzer, Garrett and Vincent, Damien and Pan, Zhufeng and Wang, Shibo and others},
8	  journal   = {arXiv preprint arXiv:2403.05530},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2403.05530}
11	}
12	
13	@article{willard2023efficient,
14	  title     = {Efficient Guided Generation for Large Language Models},
15	  author    = {Willard, Brandon T. and Louf, R{\'e}mi},
16	  journal   = {arXiv preprint arXiv:2307.09702},
17	  year      = {2023},
18	  url       = {https://arxiv.org/abs/2307.09702}
19	}
20	
21	@inproceedings{cheng2023batch,
22	  title     = {Batch Prompting: Efficient Inference with Large Language Model {API}s},
23	  author    = {Cheng, Zhoujun and Kasai, Jungo and Yu, Tao},
24	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track},
25	  pages     = {792--810},
26	  year      = {2023},
27	  url       = {https://aclanthology.org/2023.emnlp-industry.74/},
28	  doi       = {10.18653/v1/2023.emnlp-industry.74}
29	}
30	
31	@inproceedings{lu2022fantastically,
32	  title     = {Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity},
33	  author    = {Lu, Yao and Bartolo, Max and Moore, Alastair and Riedel, Sebastian and Stenetorp, Pontus},
34	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
35	  pages     = {8086--8098},
36	  year      = {2022},
37	  url       = {https://aclanthology.org/2022.acl-long.556/},
38	  doi       = {10.18653/v1/2022.acl-long.556}
39	}
40	
41	@inproceedings{yan
…[truncated 28531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-18T02:58:02.458082+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"
  }
}
```

</details>

---


### Tool call

_source line 871 · 2026-05-18T02:58:05.420230+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "wellek2010testing|perneger-1998|llm-calibration-survey-2024",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "wellek2010testing|perneger-1998|llm-calibration-survey-2024",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 872 · 2026-05-18T02:58:05.822076+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 873 · 2026-05-18T02:58:06.223597+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—|–",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—|–",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 874 · 2026-05-18T02:58:06.274257+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex:1:% DEPRECATED — this file is no longer included in main.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-18T02:58:16.420774+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I found comprehensive information about the ACL Rolling Review (ARR) 2025-2026 reviewer guidelines. Here's what the current guidelines specify:

## Review Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness 
…[truncated 1494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 13962
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-18T02:58:19.501180+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 877 · 2026-05-18T02:58:19.501593+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-18T02:58:23.128919+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 879 · 2026-05-18T02:58:24.033010+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the full reviewer guidelines, especially the scoring criteria for soundness, excitement, overall assessment. What are the exact scale descriptions for each dimension?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the full reviewer guidelines, especially the scoring criteria for soundness, excitement, overall assessment. What are the exact scale descriptions for each dimension?"
  }
}
```

</details>

---


### Tool result

_source line 880 · 2026-05-18T02:58:29.257916+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite certain; unlikely to have missed critical details
- **3**: Reasonably confident; some details may have been overlooked
- **2**: Willing to defend evaluation; likely missed some aspects
- **1**: "Not my area, or paper is very hard to understand"

## Soundness
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong support for claims; additional experiments optional
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: Major technical/methodological problems present
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: Would mention to colleagues; effort to attend presentation
- **3**: Might mention points; attend if time permits
- **2**: May interest other community members
- **1**: "Not Exciting: this paper does not resonate with me"

## Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: Consider for outstanding paper award
- **4**: Suitable for conference acceptance
- **3**: Appropriate for Findings track
- **2**: Needs substantial revisions for next cycle
- **1**: Requires complete redoing or lacks relevance

## Additional Scored Dimensions
- **Reproducibility** (1-5 scale)
- **Dataset Value** (1-5 scale)
- **Software Value** (1-5 scale)
- **Author Identity Knowledge** (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6128
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-18T02:58:29.760052+00:00_

# ARR Reviewer Scoring Criteria

Based on the guidelines provided, ARR uses three scoring dimensions for reviews:

## 1. **Soundness**
The guidelines state that "soundness scores must be justified by the text of the review." Low soundness scores require explicit justification in the review content. This dimension assesses technical validity and methodological rigor.

## 2. **Excitement**
Described as a "separate _excitement_ score, which is orthogonal to the assessment of the soundness of the paper," this reflects personal interest and subjective preference. The guidelines note that reviewers may find work technically sound but personally uninteresting.

## 3. **Overall Assessment**
This is "an explicit recommendation for the outcome of this paper, if it were committed to an \*ACL venue." It serves as "a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."

## Important Distinction
The guidelines emphasize that "all papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible," yet a reviewer may recommend acceptance despite low personal excitement due to factors like impact potential or community value.

**Note:** The document does not provide explicit numerical scale descriptions (e.g., 1-5 ratings or specific anchor definitions) for any of these three dimensions. The emphasis is on justification and coherence between scores and review text rather than predetermined scale values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5727
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-18T02:58:37.443363+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "wellek2010testing|perneger-1998|llm-calibration-survey-2024",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "wellek2010testing|perneger-1998|llm-calibration-survey-2024",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-18T02:58:37.845193+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-18T02:58:38.297007+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "head_limit": "0"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-18T02:58:38.347808+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:15:Our centrality confound (\S\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \cite{cai-isotropy-clusters-2021}, explaining why MAVEN's single-ontology types conflate confusability with centrality.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:57:\paragraph{Multiple comparisons.} Cross-dataset comparisons (FewRel, DocRED, Few-NERD, MAVEN) serve as independent replications of the same hypothesis and do not require family-wise correction \citep{rothman-1990}. Within-dataset secondary analyses (e.g., quartile comparisons, slope sensitivity checks) involve multiple looks at the same data; we report individual $p$-values and note that core claims rest on effects reaching $p < 0.001$ \citep{dror-2018-significance}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:192:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:307:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:472:[Omitted long matching line]
/home/ubu
…[truncated 4209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-18T03:00:00.957193+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Gemini",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Gemini",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-18T03:00:01.913740+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:40:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:514:\section{Cross-Model Validation with Gemini 2.5 Flash (API)}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:517:We further validate Dimension~1 on a proprietary model, Gemini 2.5 Flash \citep{gemini-team-2024}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve experiment using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:524:\textbf{Count} & \textbf{Gemini Flash} & \textbf{Qwen3-32B} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:533:\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\rho = -1.0$ for both on counts 4--32).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:537:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex:19:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:70:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-18T03:00:02.672552+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "-ing,\"| -ing [a-z]|, demonstrating|, highlighting|, leveraging|, enabling|, facilitating|, indicating|, suggesting|, confirming|, providing",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "-ing,\"| -ing [a-z]|, demonstrating|, highlighting|, leveraging|, enabling|, facilitating|, indicating|, suggesting|, confirming|, providing",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 889 · 2026-05-18T03:00:02.724479+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:46:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:52:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:207:\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\,pp, 90\% CI [$-$1.0, 2.0]\,pp) is bounded below 2\,pp at marginal significance ($p = 0.047$), confirming that the $\pm 3$\,pp choice does not drive the equivalence conclusion. At $\pm 1$\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:258:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:442:Pairwise SCS distributions do not differ significantly between train-origin (64 types, mean\,=\,0.880) and val-origin (16 types, mean\,=\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$), confirming that the train/val split does not introduce systematic confusability bias.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:467:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:510:For the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\Delta = +10.9$\,pp, 95\% CI: [$+$3.0, $+$20.1]). The confidence interval excludes zero, confirming the confusability effect at the 70B scale.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:537:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea
…[truncated 2451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-18T03:00:19.906030+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.59",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.59",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-18T03:00:19.956619+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:201:$\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:510:For the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\Delta = +10.9$\,pp, 95\% CI: [$+$3.0, $+$20.1]). The confidence interval excludes zero, confirming the confusability effect at the 70B scale.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex:14:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-18T03:00:23.497344+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "offset": "13",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "offset": "13",
    "limit": "3"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-18T03:00:23.548364+00:00_

13	\paragraph{Practical implications.}
14	The bounded count$\times$confusability interaction (0.47\,pp, TOST $p = 0.003$) means practitioners scaling schema size need not worry about confusability amplification. For RE, BCS provides a pre-hoc screen: threshold $> 0.59$ identifies confusable pairs with expected accuracy differences of 3--5\,pp. For NER, count is the dominant predictor; reducing schema size per prompt is the primary lever. Few-shot demonstrations do not mitigate the confusability gap: under 5-shot prompting, the BCS penalty widens (+4.3\,pp, $p = 0.014$; Appendix~\ref{sec:appendix_fewshot_bcs}), confirming confusability as a structural schema property. These results apply to the training-free setting; fine-tuned models may learn type boundaries that reduce confusability effects.
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-18T03:00:36.006835+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
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

_source line 895 · 2026-05-18T03:00:36.058347+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-18T03:02:55.327326+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告：Round 1\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 via ACL ARR May 2026 cycle\n**审查侧重**: 新颖性 + 写作完整性 + 格式合规 + Related Work 覆盖度 + Contribution framing\n\n---\n\n## Summary\n\n本文对 training-free LLM IE 中 schema 复杂度如何预测性能退化进行了系统性的 controlled study，将退化分解为两个维度（type count 和 type confusability），提出 SCS/BCS 指标量化 confusability，并在四个数据集上验证。论文同时报告了 schema decomposition (SDGD) 的负面结果。这是一篇实验设计严谨的 analysis paper，但核心指标 SCS 与 LLM-PEE 形式相同，pairwise effect size 很小 (r² ≈ 1.3-1.7%)，practical implications 有限（BCS 仅对 RE 有效，对 NER 无 batch-level signal），这限制了论文的 excitement 和 actionable value。\n\n---\n\n## Strengths\n\n**S1. 实验设计严谨，控制变量到位。** BCS-controlled 实验通过固定 count 变化 BCS 来隔离 confusability 效应，within-pool 分析控制了 pool composition confound，TOST equivalence testing 形式化检验了两维度的 bounded association。这种 quasi-experimental 设计在 NLP 实证研究中不常见，值得肯定。\n\n**S2. 极其充分的 robustness checks。** 跨模型验证 (8B/32B/70B/Gemini)、跨 prompt 变体验证 (4 种 prompt)、跨数据集复制 (FewRel/DocRED/Few-NERD/MAVEN)、BCS aggregation sensitivity (mean vs max)、SCS embedding ablation (name-only vs name+def)、cross-seed variance decomposition。论文在 robustness 方面的投入远超多数 EMNLP 投稿。\n\n**S3. 负面结果的诚实报告。** SDGD 的失败分析（NER merge amplification、RE routing failure）具有实际价值，论文不仅报告了 SDGD 失败，还诊断了失败原因（precision collapse, constrained decoding 导致的 routing 不可靠），并诚实指出 confusability-aware grouping 仅比 random 好 +1.4pp (n.s.)。\n\n**S4. Limitations section 极为详尽。** 8 项具体限制 + 多重比较声明，涵盖 model coverage、effect size、factorial tests、metric scope、evaluation metric、causal mechanism、data contamination。这是我见过的最详尽的 Limitations 之一。\n\n**S5. NER/RE 退化模式的差异化分析有洞察力。** 发现 BCS 对 RE 有效但对 NER 无效、NER U-shape 与 RE monotonic decline 的对比、centrality confound 的识别和处理（§5.5, Appendix E），这些 task-dependent 发现确实有助于理解 LLM IE 的行为。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **SCS 与 LLM-PEE 形式相同，增量贡献的 framing 不够有说服力**\n- 具体位置：Related Work §SCS novelty 段落；Introduction Contribution 2\n- 问题：论文在 Related Work 中坦承 \"SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE\"，声称贡献在于 \"controlled experimental framework\" 而非指标本身。但这意味着论文的方法论贡献实质上是 (a) 一个 analysis framework + (b) 一组实验发现。对于 analysis paper，关键在于发现是否 surprising 和 actionable。然而：\n  - Pairwise r² = 1.3-1.7% 属于 \"small but real\" 范畴，论文自己引用 Cohen (1988) 承认这一点\n  - Typical-batch BCS gap 仅 ~2.2pp（§4.3 practical magnitude），这对于实际部署的指导意义有限\n  - BCS 对 NER 无 batch-level signal，使得 BCS 的实际适用范围缩小到 RE 和 ED\n- 为什么影响接收：审稿人会问 \"if I'm a practitioner, what do I do differently after reading this paper?\"。答案主要是 \"RE schema 设计时检查 BCS\"，但效果仅 3-5pp\n- 建议：更明确地论证 analysis paper 对社区的价值——例如，论文的发现是否推翻了某个广泛持有的假设？是否指明了未来 method paper 应该解决的瓶颈？当前的 framing 更像是 \"我们系统地验证了一个直觉\"，需要提升到 \"我们发现了一个之前不知道的机制\"\n\n**N2** [critical] **Contribution 3 本质上是包装 NER null result**\n- 具体位置：Introduction Contribution 3；§4.3 (BCS-controlled, NER 部分)；§5.4 (Discussion, task-dependent batch-level effects)\n- 问题：Contribution 3 声称 \"We identify task-dependent boundaries of batch-level confusability metrics: BCS predicts type substitution errors in RE but shows no batch-level signal in NER, highlighting the need for task-specific validation\"。这实质上是将 \"BCS 在 NER 上不 work\" 重新包装为一个贡献。虽然识别 metric 的适用边界确实有价值，但将其列为四大 contribution 之一会让审稿人质疑论文的贡献密度\n- 为什么影响接收：如果四个 contribution 中有一个是 null result 的 reframing，论文的核心贡献实际上只有三个\n- 建议：将 Contribution 3 合并到 Contribution 2 中作为 boundary condition，或将其降级为 finding 而非 contribution\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] **Gemini 2.5 Flash 引用错误**\n- 具体位置：main.tex line 517; references.bib `gemini-team-2024`\n- 问题：论文在多处引用 \"Gemini 2.5 Flash \\citep{gemini-team-2024}\"，但 bib 条目 `gemini-team-2024` 实际指向的是 \"Gemini 1.5: Unlocking Multimodal Understanding Across Millions of Tokens of Context\" (arXiv:2403.05530)。Gemini 2.5 Flash 是不同的模型/论文，应该引用正确的 technical report\n- 建议：替换为 Gemini 2.5 的正确引用（如果存在 tech report）或标注为 \"Gemini 2.5 Flash (Google, 2025)\" 不带具体 citation\n\n**W2** [major] **Conclusion 过短，缺 future work**\n- 具体位置：discussion.tex §7 (Conclusion)，共 1 段约 120 words\n- 问题：Conclusion 仅用一段话总结了所有发现，没有 future work 部分。虽然 §6 (SDGD) 末尾有三个 \"future directions\"（coarse-to-fine, retrieval routing, calibrated generation），但这些被嵌入在负面结果的讨论中，不够系统。一篇 8 页 EMNLP long paper 的 Conclusion 通常至少两段，包含 implications + limitations sketch + future directions\n- 建议：扩展 Conclusion 至 2-3 段，系统阐述 future work（如：fine-tuned model 是否消除 confusability effect？如何将 BCS 集成到 schema design pipeline？pairwise SCS 如何扩展到 hierarchical schemas？）\n\n**W3** [major] **Abstract 偏短且缺少 motivation/significance**\n- 具体位置：abstract.tex，约 140 words\n- 问题：Abstract 直接切入技术细节 (\"Training-free LLM information extraction degrades...\")，缺少对问题重要性的 framing。EMNLP long paper abstract 通常 150-250 words。当前 Abstract 没有回答 \"为什么这个问题重要\"，也没有提及 cross-model generalization 这一重要发现。一个不熟悉 LLM IE 的审稿人可能在前两句话后就失去兴趣\n- 建议：(1) 开头加一句关于 training-free LLM IE 快速增长的重要性; (2) 加入 cross-model 验证的一句话; (3) 扩充到 ~200 words\n\n**W4** [major] **BCS > 0.59 阈值缺乏系统推导**\n- 具体位置：Discussion §Practical implications\n- 问题：论文声称 \"BCS provides a pre-hoc screen: threshold > 0.59 identifies confusable pairs with expected accuracy differences of 3-5 pp\"，但正文中没有对这个 0.59 阈值进行 formal derivation（如 ROC analysis、threshold sensitivity curve、或 calibration 分析）。这个数字似乎来自实验数据，但读者无法 verify 其来源或了解其鲁棒性\n- 建议：(1) 在正文或 Appendix 中加入 threshold 的推导过程; (2) 报告不同 threshold 下的 precision-recall 或 accuracy gap; (3) 至少说明这个数字是如何从数据中得到的\n\n**W5** [minor] **Introduction 的 4 findings 与 4 contributions 映射不够清晰**\n- 具体位置：Introduction, findings (1)-(4) vs contributions (1)-(4)\n- 问题：Finding (3) \"Effects are consistent across schema sizes and granularities\" 是一个 robustness 声明，没有直接映射到任何一个 contribution。Finding (1) 和 Finding (2) 都部分映射到 Contribution 1 和 2，但边界不清。读者需要自行 reconstruct 对应关系\n- 建议：要么减少 findings 数量使之与 contributions 一一对应，要么在 contributions 列表中用 (§X) 引用明确标注每个 contribution 对应哪些 findings\n\n**W6** [minor] **部分 -ing participial phrases 残留**\n- 具体位置：\n  - Introduction Contribution 3: \"highlighting the need for task-specific validation\"\n  - Results §4.1: \"indicating schema configuration rather than model-specific factors predicts difficulty\"\n  - Results §4.3: \"confirming the confusability effect at the 70B scale\"\n  - Discussion: \"confirming confusability as a structural schema property\"\n  - 多处 caption 中 \"confirming that...\"\n- 问题：这些 -ing 尾缀短语是典型的 AI 写作标志（参见 CLAUDE.md 写作规范 §5.3）。正文中约有 10-15 处\n- 建议：将 -ing 短语改为独立句子或其他句式。例如：\"highlighting the need for...\" → \"This underscores the need for...\" 或直接删除\n\n**W7** [minor] **MAVEN 仅用 validation set 评估**\n- 具体位置：§3.1 MAVEN 段落\n- 问题：论文说 \"We use the validation set... for evaluation, as test set labels are not publicly available\"。这是常见做法但值得注意：validation set 可能在调试过程中被间接 \"looked at\"，尤其是在选择 prompt 版本或调整实验参数时。论文没有明确声明 validation set 是否在任何实验设计决策中被使用\n- 建议：加一句声明 MAVEN validation set 是否用于任何 hyperparameter 选择\n\n---\n\n## 小问题（不影响接收）\n\n1. **deprecated conclusion.tex 残留**: `conclusion.tex` 文件存在且包含注释 `% DEPRECATED — this file is no longer included in main.tex.`，应清理（不影响编译但不整洁）\n2. **Table 1 的 Embedding 列**: Few-NERD 用 Qwen3-32B 而其他三个用 MiniLM，但 §3.2 解释了原因。建议在 Table caption 中简要提及为什么使用不同的 embedding\n3. **RE prompt 没有 v1/v2 区分**: §3.4 说 \"RE uses only a v2-style prompt\"，但 SDGD 实验中 Table 3 (Appendix B) 提到 \"All modes use the v1 prompt\"。RE 是否有 v1 prompt？如果 RE 只有一个 prompt 版本，不应称其为 \"v2-style\"\n4. **FewRel train+val combination**: 合并 train 和 validation split 可能引入 heterogeneity，论文在 Appendix K 做了 split-origin analysis 控制这个 confound，但正文应更明确提到这个设计决策的潜在影响\n\n---\n\n## Questions for Authors\n\n**Q1**: BCS > 0.59 这个阈值是如何推导的？在不同数据集 (FewRel vs DocRED) 上是否一致？\n\n**Q2**: 论文声称 \"first controlled study isolating type confusability from type count\"。如果 LLM-PEE 已经在用 embedding similarity 做 partitioning（即隐式利用了 confusability 信息），那么本文的 \"controlled isolation\" 与 LLM-PEE 的 ablation study（如果存在的话）有何本质区别？\n\n**Q3**: NER 的 U-shape (count 22-44 plateau, count 66 recovery) 是一个 striking finding。论文假设 \"at full-schema, filtering becomes vacuous and recall recovers\"，但这个解释是否可以被直接验证——例如，通过检查 full-schema 条件下是否有更多 false positives（因为不需要 type filtering）？\n\n**Q4**: Pairwise SCS 在 NER 上显著 (r = 0.112, p < 0.001) 但 batch-level BCS 完全无效 (r ≈ 0)。论文的解释是 \"NER errors are dominated by missed entities\"。但如果 pairwise signal 存在，为什么 aggregation 不保留信号？是否存在 cancellation effect（某些 pairs 正相关而另一些负相关）？\n\n**Q5**: Few-shot 实验 (Appendix N) 发现 confusability gap 在 5-shot 下反而扩大 (+4.3pp)。论文推测 \"lost-in-middle effects from increased prompt length\"，但如果这是 prompt length 问题，为什么 low-BCS 在 1-shot 时最高 (0.754) 而在 5-shot 时下降 (0.715)？是否有其他解释？\n\n---\n\n## Missing References\n\n1. **Gemini 2.5 技术报告**: 当前引用 `gemini-team-2024` 指向 Gemini 1.5，需要替换为 Gemini 2.5 的正确引用\n2. **Constrained decoding 相关工作**: Willard & Louf (2023) 已引用 ✓。但论文大量使用 vLLM constrained decoding (json schema enforcement)，可能还应引用 guidance/outlines 框架的后续工作或 structured generation survey\n3. **Orphan entries 检查**: Director 提到的 `wellek2010testing`, `perneger-1998`, `llm-calibration-survey-2024` 均不存在于 references.bib 中——不存在 orphan entry 问题\n4. **引用密度**: ~45 条引用，对于 EMNLP long paper 偏少但可接受。建议补充 1-2 条关于 embedding similarity for label confusion 的 NLP 文献（如 Snell et al. Prototypical Networks 的 confusion-with-distance 分析）\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 备注 |\n|------|------|------|\n| `\\documentclass[11pt]{article}` | ✅ | main.tex line 1 |\n| `\\usepackage[review]{acl}` | ✅ | main.tex line 3 |\n| `\\author{Anonymous}` | ✅ | main.tex line 19 |\n| Anonymous review link | ✅ | Introduction footnote 2, anonymous.4open.science |\n| Limitations section | ✅ | 8 项 + multiple comparisons 段落，不计入页数 |\n| Responsible NLP Checklist | ✅ | 完整，所有 A/B/C/D/E 小节均已回答 |\n| 正文 ≤ 8 页 | ⚠️ 无法验证 | 未编译；7 个正文 section + 多个 table/figure，内容密集，可能接近但不确定是否超限 |\n| Em-dash 检查 | ✅ | 正文 .tex 无解释性 em-dash/en-dash |\n| Reference 格式 | ⚠️ | Gemini 引用错误（W1），其余格式一致 |\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 4/5 | 实验设计严谨，控制变量充分，robustness checks 极为详尽。扣分点：BCS 0.59 阈值无 formal derivation；logit-scale TOST 不一致但被诚实报告 |\n| **Excitement** | 2.5/5 | Analysis paper 的发现主要验证了直觉（larger/more similar schemas → worse performance）。SCS 与 LLM-PEE 相同。Effect size 很小。Practical implications 有限且仅适用于 RE |\n| **Reproducibility** | 4.5/5 | 代码承诺 release；prompt templates 完整附录；所有实验参数明确；使用开源模型 + 公开数据集 |\n| **Overall Assessment** | **3.0** | **Findings 级别**。方法论严谨、实验设计优秀、robustness 充分，但新颖性有限（SCS = LLM-PEE metric）、effect size modest、practical actionability 局限于 RE。适合 Findings track |\n\n## Confidence\n\n**4/5** — 我仔细阅读了论文全文（含所有 appendix）和 references.bib，熟悉 LLM IE 和 zero-shot extraction 的相关文献。对实验设计和统计方法的评估有较高信心。\n\n---\n\n## 主要优势总结\n\n- 实验设计的严谨性在 NLP 实证研究中属于上乘水平\n- Robustness checks 的广度和深度堪称典范\n- 负面结果的诚实报告和失败诊断对社区有价值\n- Limitations section 极为详尽，体现了高度的科学诚实性\n- Centrality confound 的识别和处理是一个有价值的方法论贡献\n\n## 核心关切\n\n论文的核心张力在于：实验做得非常好，但发现的东西不够 exciting。一个审稿人可以同时认为 \"this is very well done\" 和 \"this doesn't tell me something I didn't already suspect\"。如果作者能更好地 frame 哪些发现是 counter-intuitive（例如 NER U-shape、BCS 对 NER 无效、few-shot 反而扩大 gap），论文的 excitement 会提升。当前的 framing 过于 \"系统验证\"，不够 \"发现驱动\"。\n",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告：Round 1\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 via ACL ARR May 2026 cycle\n**审查侧重**: 新颖性 + 写作完整性 + 格式合规 + Related Work 覆盖度 + Contribution framing\n\n---\n\n## Summary\n\n本文对 training-free LLM IE 中 schema 复杂度如何预测性能退化进行了系统性的 controlled study，将退化分解为两个维度（type count 和 type confusability），提出 SCS/BCS 指标量化 confusability，并在四个数据集上验证。论文同时报告了 schema decomposition (SDGD) 的负面结果。这是一篇实验设计严谨的 analysis paper，但核心指标 SCS 与 LLM-PEE 形式相同，pairwise effect size 很小 (r² ≈ 1.3-1.7%)，practical implications 有限（BCS 仅对 RE 有效，对 NER 无 batch-level signal），这限制了论文的 excitement 和 actionable value。\n\n---\n\n## Strengths\n\n**S1. 实验设计严谨，控制变量到位。** BCS-controlled 实验通过固定 count 变化 BCS 来隔离 confusability 效应，within-pool 分析控制了 pool composition confound，TOST equivalence testing 形式化检验了两维度的 bounded association。这种 quasi-experimental 设计在 NLP 实证研究中不常见，值得肯定。\n\n**S2. 极其充分的 robustness checks。** 跨模型验证 (8B/32B/70B/Gemini)、跨 prompt 变体验证 (4 种 prompt)、跨数据集复制 (FewRel/DocRED/Few-NERD/MAVEN)、BCS aggregation sensitivity (mean vs max)、SCS embedding ablation (name-only vs name+def)、cross-seed variance decomposition。论文在 robustness 方面的投入远超多数 EMNLP 投稿。\n\n**S3. 负面结果的诚实报告。** SDGD 的失败分析（NER merge amplification、RE routing failure）具有实际价值，论文不仅报告了 SDGD 失败，还诊断了失败原因（precision collapse, constrained decoding 导致的 routing 不可靠），并诚实指出 confusability-aware grouping 仅比 random 好 +1.4pp (n.s.)。\n\n**S4. Limitations section 极为详尽。** 8 项具体限制 + 多重比较声明，涵盖 model coverage、effect size、factorial tests、metric scope、evaluation metric、causal mechanism、data contamination。这是我见过的最详尽的 Limitations 之一。\n\n**S5. NER/RE 退化模式的差异化分析有洞察力。** 发现 BCS 对 RE 有效但对 NER 无效、NER U-shape 与 RE monotonic decline 的对比、centrality confound 的识别和处理（§5.5, Appendix E），这些 task-dependent 发现确实有助于理解 LLM IE 的行为。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **SCS 与 LLM-PEE 形式相同，增量贡献的 framing 不够有说服力**\n- 具体位置：Related Work §SCS novelty 段落；Introduction Contribution 2\n- 问题：论文在 Related Work 中坦承 \"SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE\"，声称贡献在于 \"controlled experimental framework\" 而非指标本身。但这意味着论文的方法论贡献实质上是 (a) 一个 analysis framework + (b) 一组实验发现。对于 analysis paper，关键在于发现是否 surprising 和 actionable。然而：\n  - Pairwise r² = 1.3-1.7% 属于 \"small but real\" 范畴，论文自己引用 Cohen (1988) 承认这一点\n  - Typical-batch BCS gap 仅 ~2.2pp（§4.3 practical magnitude），这对于实际部署的指导意义有限\n  - BCS 对 NER 无 batch-level signal，使得 BCS 的实际适用范围缩小到 RE 和 ED\n- 为什么影响接收：审稿人会问 \"if I'm a practitioner, what do I do differently after reading this paper?\"。答案主要是 \"RE schema 设计时检查 BCS\"，但效果仅 3-5pp\n- 建议：更明确地论证 analysis paper 对社区的价值——例如，论文的发现是否推翻了某个广泛持有的假设？是否指明了未来 method paper 应该解决的瓶颈？当前的 framing 更像是 \"我们系统地验证了一个直觉\"，需要提升到 \"我们发现了一个之前不知道的机制\"\n\n**N2** [critical] **Contribution 3 本质上是包装 NER null result**\n- 具体位置：Introduction Contribution 3；§4.3 (BCS-controlled, NER 部分)；§5.4 (Discussion, task-dependent batch-level effects)\n- 问题：Contribution 3 声称 \"We identify task-dependent boundaries of batch-level confusability metrics: BCS predicts type substitution errors in RE but shows no batch-level signal in NER, highlighting the need for task-specific validation\"。这实质上是将 \"BCS 在 NER 上不 work\" 重新包装为一个贡献。虽然识别 metric 的适用边界确实有价值，但将其列为四大 contribution 之一会让审稿人质疑论文的贡献密度\n- 为什么影响接收：如果四个 contribution 中有一个是 null result 的 reframing，论文的核心贡献实际上只有三个\n- 建议：将 Contribution 3 合并到 Contribution 2 中作为 boundary condition，或将其降级为 finding 而非 contribution\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] **Gemini 2.5 Flash 引用错误**\n- 具体位置：main.tex line 517; references.bib `gemini-team-2024`\n- 问题：论文在多处引用 \"Gemini 2.5 Flash \\citep{gemini-team-2024}\"，但 bib 条目 `gemini-team-2024` 实际指向的是 \"Gemini 1.5: Unlocking Multimodal Understanding Across Millions of Tokens of Context\" (arXiv:2403.05530)。Gemini 2.5 Flash 是不同的模型/论文，应该引用正确的 technical report\n- 建议：替换为 Gemini 2.5 的正确引用（如果存在 tech report）或标注为 \"Gemini 2.5 Flash (Google, 2025)\" 不带具体 citation\n\n**W2** [major] **Conclusion 过短，缺 future work**\n- 具体位置：discussion.tex §7 (Conclusion)，共 1 段约 120 words\n- 问题：Conclusion 仅用一段话总结了所有发现，没有 future work 部分。虽然 §6 (SDGD) 末尾有三个 \"future directions\"（coarse-to-fine, retrieval routing, calibrated generation），但这些被嵌入在负面结果的讨论中，不够系统。一篇 8 页 EMNLP long paper 的 Conclusion 通常至少两段，包含 implications + limitations sketch + future directions\n- 建议：扩展 Conclusion 至 2-3 段，系统阐述 future work（如：fine-tuned model 是否消除 confusability effect？如何将 BCS 集成到 schema design pipeline？pairwise SCS 如何扩展到 hierarchical schemas？）\n\n**W3** [major] **Abstract 偏短且缺少 motivation/significance**\n- 具体位置：abstract.tex，约 140 words\n- 问题：Abstract 直接切入技术细节 (\"Training-free LLM information extraction degrades...\")，缺少对问题重要性的 framing。EMNLP long paper abstract 通常 150-250 words。当前 Abstract 没有回答 \"为什么这个问题重要\"，也没有提及 cross-model generalization 这一重要发现。一个不熟悉 LLM IE 的审稿人可能在前两句话后就失去兴趣\n- 建议：(1) 开头加一句关于 training-free LLM IE 快速增长的重要性; (2) 加入 cross-model 验证的一句话; (3) 扩充到 ~200 words\n\n**W4** [major] **BCS > 0.59 阈值缺乏系统推导**\n- 具体位置：Discussion §Practical implications\n- 问题：论文声称 \"BCS provides a pre-hoc screen: threshold > 0.59 identifies confusable pairs with expected accuracy differences of 3-5 pp\"，但正文中没有对这个 0.59 阈值进行 formal derivation（如 ROC analysis、threshold sensitivity curve、或 calibration 分析）。这个数字似乎来自实验数据，但读者无法 verify 其来源或了解其鲁棒性\n- 建议：(1) 在正文或 Appendix 中加入 threshold 的推导过程; (2) 报告不同 threshold 下的 precision-recall 或 accuracy gap; (3) 至少说明这个数字是如何从数据中得到的\n\n**W5** [minor] **Introduction 的 4 findings 与 4 contributions 映射不够清晰**\n- 具体位置：Introduction, findings (1)-(4) vs contributions (1)-(4)\n- 问题：Finding (3) \"Effects are consistent across schema sizes and granularities\" 是一个 robustness 声明，没有直接映射到任何一个 contribution。Finding (1) 和 Finding (2) 都部分映射到 Contribution 1 和 2，但边界不清。读者需要自行 reconstruct 对应关系\n- 建议：要么减少 findings 数量使之与 contributions 一一对应，要么在 contributions 列表中用 (§X) 引用明确标注每个 contribution 对应哪些 findings\n\n**W6** [minor] **部分 -ing participial phrases 残留**\n- 具体位置：\n  - Introduction Contribution 3: \"highlighting the need for task-specific validation\"\n  - Results §4.1: \"indicating schema configuration rather than model-specific factors predicts difficulty\"\n  - Results §4.3: \"confirming the confusability effect at the 70B scale\"\n  - Discussion: \"confirming confusability as a structural schema property\"\n  - 多处 caption 中 \"confirming that...\"\n- 问题：这些 -ing 尾缀短语是典型的 AI 写作标志（参见 CLAUDE.md 写作规范 §5.3）。正文中约有 10-15 处\n- 建议：将 -ing 短语改为独立句子或其他句式。例如：\"highlighting the need for...\" → \"This underscores the need for...\" 或直接删除\n\n**W7** [minor] **MAVEN 仅用 validation set 评估**\n- 具体位置：§3.1 MAVEN 段落\n- 问题：论文说 \"We use the validation set... for evaluation, as test set labels are not publicly available\"。这是常见做法但值得注意：validation set 可能在调试过程中被间接 \"looked at\"，尤其是在选择 prompt 版本或调整实验参数时。论文没有明确声明 validation set 是否在任何实验设计决策中被使用\n- 建议：加一句声明 MAVEN validation set 是否用于任何 hyperparameter 选择\n\n---\n\n## 小问题（不影响接收）\n\n1. **deprecated conclusion.tex 残留**: `conclusion.tex` 文件存在且包含注释 `% DEPRECATED — this file is no longer included in main.tex.`，应清理（不影响编译但不整洁）\n2. **Table 1 的 Embedding 列**: Few-NERD 用 Qwen3-32B 而其他三个用 MiniLM，但 §3.2 解释了原因。建议在 Table caption 中简要提及为什么使用不同的 embedding\n3. **RE prompt 没有 v1/v2 区分**: §3.4 说 \"RE uses only a v2-style prompt\"，但 SDGD 实验中 Table 3 (Appendix B) 提到 \"All modes use the v1 prompt\"。RE 是否有 v1 prompt？如果 RE 只有一个 prompt 版本，不应称其为 \"v2-style\"\n4. **FewRel train+val combination**: 合并 train 和 validation split 可能引入 heterogeneity，论文在 Appendix K 做了 split-origin analysis 控制这个 confound，但正文应更明确提到这个设计决策的潜在影响\n\n---\n\n## Questions for Authors\n\n**Q1**: BCS > 0.59 这个阈值是如何推导的？在不同数据集 (FewRel vs DocRED) 上是否一致？\n\n**Q2**: 论文声称 \"first controlled study isolating type confusability from type count\"。如果 LLM-PEE 已经在用 embedding similarity 做 partitioning（即隐式利用了 confusability 信息），那么本文的 \"controlled isolation\" 与 LLM-PEE 的 ablation study（如果存在的话）有何本质区别？\n\n**Q3**: NER 的 U-shape (count 22-44 plateau, count 66 recovery) 是一个 striking finding。论文假设 \"at full-schema, filtering becomes vacuous and recall recovers\"，但这个解释是否可以被直接验证——例如，通过检查 full-schema 条件下是否有更多 false positives（因为不需要 type filtering）？\n\n**Q4**: Pairwise SCS 在 NER 上显著 (r = 0.112, p < 0.001) 但 batch-level BCS 完全无效 (r ≈ 0)。论文的解释是 \"NER errors are dominated by missed entities\"。但如果 pairwise signal 存在，为什么 aggregation 不保留信号？是否存在 cancellation effect（某些 pairs 正相关而另一些负相关）？\n\n**Q5**: Few-shot 实验 (Appendix N) 发现 confusability gap 在 5-shot 下反而扩大 (+4.3pp)。论文推测 \"lost-in-middle effects from increased prompt length\"，但如果这是 prompt length 问题，为什么 low-BCS 在 1-shot 时最高 (0.754) 而在 5-shot 时下降 (0.715)？是否有其他解释？\n\n---\n\n## Missing References\n\n1. **Gemini 2.5 技术报告**: 当前引用 `gemini-team-2024` 指向 Gemini 1.5，需要替换为 Gemini 2.5 的正确引用\n2. **Constrained decoding 相关工作**: Willard & Louf (2023) 已引用 ✓。但论文大量使用 vLLM constrained decoding (json schema enforcement)，可能还应引用 guidance/outlines 框架的后续工作或 structured generation survey\n3. **Orphan entries 检查**: Director 提到的 `wellek2010testing`, `perneger-1998`, `llm-calibration-survey-2024` 均不存在于 references.bib 中——不存在 orphan entry 问题\n4. **引用密度**: ~45 条引用，对于 EMNLP long paper 偏少但可接受。建议补充 1-2 条关于 embedding similarity for label confusion 的 NLP 文献（如 Snell et al. Prototypical Networks 的 confusion-with-distance 分析）\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 备注 |\n|------|------|------|\n| `\\documentclass[11pt]{article}` | ✅ | main.tex line 1 |\n| `\\usepackage[review]{acl}` | ✅ | main.tex line 3 |\n| `\\author{Anonymous}` | ✅ | main.tex line 19 |\n| Anonymous review link | ✅ | Introduction footnote 2, anonymous.4open.science |\n| Limitations section | ✅ | 8 项 + multiple comparisons 段落，不计入页数 |\n| Responsible NLP Checklist | ✅ | 完整，所有 A/B/C/D/E 小节均已回答 |\n| 正文 ≤ 8 页 | ⚠️ 无法验证 | 未编译；7 个正文 section + 多个 table/figure，内容密集，可能接近但不确定是否超限 |\n| Em-dash 检查 | ✅ | 正文 .tex 无解释性 em-dash/en-dash |\n| Reference 格式 | ⚠️ | Gemini 引用错误（W1），其余格式一致 |\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 4/5 | 实验设计严谨，控制变量充分，robustness checks 极为详尽。扣分点：BCS 0.59 阈值无 formal derivation；logit-scale TOST 不一致但被诚实报告 |\n| **Excitement** | 2.5/5 | Analysis paper 的发现主要验证了直觉（larger/more similar schemas → worse performance）。SCS 与 LLM-PEE 相同。Effect size 很小。Practical implications 有限且仅适用于 RE |\n| **Reproducibility** | 4.5/5 | 代码承诺 release；prompt templates 完整附录；所有实验参数明确；使用开源模型 + 公开数据集 |\n| **Overall Assessment** | **3.0** | **Findings 级别**。方法论严谨、实验设计优秀、robustness 充分，但新颖性有限（SCS = LLM-PEE metric）、effect size modest、practical actionability 局限于 RE。适合 Findings track |\n\n## Confidence\n\n**4/5** — 我仔细阅读了论文全文（含所有 appendix）和 references.bib，熟悉 LLM IE 和 zero-shot extraction 的相关文献。对实验设计和统计方法的评估有较高信心。\n\n---\n\n## 主要优势总结\n\n- 实验设计的严谨性在 NLP 实证研究中属于上乘水平\n- Robustness checks 的广度和深度堪称典范\n- 负面结果的诚实报告和失败诊断对社区有价值\n- Limitations section 极为详尽，体现了高度的科学诚实性\n- Centrality confound 的识别和处理是一个有价值的方法论贡献\n\n## 核心关切\n\n论文的核心张力在于：实验做得非常好，但发现的东西不够 exciting。一个审稿人可以同时认为 \"this is very well done\" 和 \"this doesn't tell me something I didn't already suspect\"。如果作者能更好地 frame 哪些发现是 counter-intuitive（例如 NER U-shape、BCS 对 NER 无效、few-shot 反而扩大 gap），论文的 excitement 会提升。当前的 framing 过于 \"系统验证\"，不够 \"发现驱动\"。\n",
    "reviewer_id": "2",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-18T03:03:00.099052+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4771
}
```

</details>

---


### Assistant

_source line 898 · 2026-05-18T03:03:08.873295+00:00_

审稿报告已提交。

核心判断：**Overall 3.0 (Findings 级别)**。论文实验设计和 robustness 属上乘水平（Soundness 4/5），但新颖性受限于 SCS 与 LLM-PEE 指标形式相同、effect size modest (r² ≈ 1.3-1.7%, typical gap ~2.2pp)、practical implications 仅适用 RE（Excitement 2.5/5）。

关键问题：
- **N1** [critical]: SCS 增量贡献 framing 不够有力，发现主要是 "系统验证直觉" 而非 "发现新机制"
- **N2** [critical]: Contribution 3 本质是 NER null result 的 reframing
- **W1** [major]: Gemini 2.5 Flash 引用指向 Gemini 1.5 论文
- **W2** [major]: Conclusion 仅 1 段，缺 future work
- **W3** [major]: Abstract ~140 words 偏短，缺 motivation
- **W4** [major]: BCS > 0.59 阈值无 formal derivation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2"
}
```

</details>

---


## Round 28

## Round 28

14 recorded events


### User

_source line 899 · 2026-05-18T03:05:14.426905+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每一个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用具体 Section/Table/Figure）。

---

# Reviewer 1 完整审稿报告

**Overall Assessment: 3.5 (Borderline Conference)**
**Soundness: 3.5/5 | Excitement: 3/5 | Reproducibility: 4/5 | Confidence: 4/5**

## Strengths

**S1.** 精心设计的准实验控制。BCS-controlled 实验固定 count 变化 BCS，是真正的 quasi-experimental manipulation。

**S2.** 统计方法工具箱丰富且使用得当。TOST、bootstrap CIs、permutation test、cluster bootstrap、variance decomposition。

**S3.** 诚实且 informative 的负面结果。SDGD 失败不仅报告还系统诊断（merge amplification + routing failure）。Oracle routing +29.8pp 证明上限存在。

**S4.** 全面的敏感性分析。4 种 prompt variant、SCS ablation、BCS aggregation、logit-scale TOST、cross-seed decomposition。

**S5.** 跨模型验证覆盖度好。4 个模型跨 3 个架构族，Dimension 1 斜率几乎相同。

**S6.** MAVEN centrality confound 发现有方法论贡献价值。

**S7.** Limitations 透明度高。Data contamination 分析尤其充分。

## Weaknesses

**W1** [major] **Logit-scale TOST 不一致，削弱 "bounded association" 核心 claim。** Linear-scale TOST p=0.003 通过，但 logit-scale TOST p=0.209 inconclusive。交互项 logit-scale marginal significant (p=0.047)。选择 "primary scale" 看起来 outcome-driven。建议：(a) 正文明确报告 logit-scale 结果；(b) 考虑 mixed-effects logistic regression；(c) 或承认 separability 仅在 linear approximation 下成立。

**W2** [major] **Dimension 2 实际效应量小，framing 过度强调。** Typical gap 2.2pp (CI: [0.4, 4.0])。叙事频繁强调 extreme-batch gap (25-31pp)。BCS > 0.59 阈值缺少 precision/recall 分析。Title 说 "Predicts" 但 confusability 预测力 modest。Count 效应 (-49pp) 远大于 confusability (2.2pp)。建议：Abstract/Intro 前置 "count dominates"，提供 BCS 阈值 ROC 分析，强调方法论贡献。

**W3** [major] **NER batch-level null result 显著限制泛化性。** Batch-level BCS-F1 在 NER 为零 (r=0.004, n=450)。论文声称跨 NER/RE/ED，但 Dim 2 batch-level 仅对 RE 有效。NER U-shape "dual-task burden" 假设未经测试。MAVEN batch-level 未报告。建议：Title/Abstract 明确 BCS 的任务依赖性。

**W4** [major] **FewRel contamination 风险未完全排除。** Train-origin accuracy 差异 p=0.06 仅 suggestive。Non-uniform contamination 未被排除。DocRED 每个 count 仅 5 batches。建议：增加 DocRED batch 数量，或使用 contamination-free RE dataset。

**W5** [minor] Gemini 2.5 Flash 引用错误（bib 指向 Gemini 1.5）。

**W6** [minor] 多重比较处理不够一致（4 prompt × 2 count = 8 tests, 7/8 directional consistency 代替正式检验）。

**W7** [minor] FewRel RE 任务格式特殊性（closed-set classification with constrained decoding 非标准 RE）。

**W8** [minor] SCS 新颖性有限。§3.2 "We introduce" 给人新指标印象，但与 LLM-PEE 形式相同。

## Questions
Q1: 能否报告 mixed-effects logistic regression 结果？
Q2: Conditional r²=0.074 vs unconditional r²=0.013——selection on dependent variable 问题如何回应？
Q3: Count 80 natural BCS variation 太小 (IQR=0.033)——confusability 只在人工 partition 时 matter？
Q4: NER U-shape 能否通过 "dummy-padded schema" 实验验证？
Q5: Dimension 2 为何未在 Gemini 上测试？

## Missing References
1. Gemini 2.5 正确引用
2. Structured prediction calibration 文献
3. levy-2024-same-task 是否为 orphan entry

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-18T03:05:30.844938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "offset": "41",
  "limit": "16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "offset": "41",
    "limit": "16"
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-18T03:05:31.297430+00:00_

41	\subsection{Schema Confusability Score (SCS)}
42	\label{sec:scs}
43	
44	We introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
45	{\small
46	\[
47	\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
48	\]
49	}
50	
51	For a batch of types $B = \{t_1, \ldots, t_k\}$, the \textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:
52	\[
53	\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
54	\]
55	
56	We compute SCS with two embedding models: (1)~Qwen3-32B \cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. Few-NERD uses Qwen3 embeddings because its 66 fine-grained types include same-category pairs (e.g., ``person-artist'' vs.\ ``person-actor'') that MiniLM's 384-d space does not separate well; a cross-embedding check confirms directional consistency (MiniLM $r = 0.172$, Qwen3 $r = 0.138$; Appendix~\ref{sec:appendix_bcs_sensitivity}). SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\Delta r$: $-0.023$ to $+0.035$; Appendix~\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional co
…[truncated 173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-18T03:05:31.801035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "209",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "209",
    "limit": "6"
  }
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-18T03:05:32.256253+00:00_

209	\end{table}
210	
211	\paragraph{Logit-scale sensitivity.}
212	Because accuracy near 50\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\pm 3$\,pp margin ($\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\,pp, still within the $\pm 3$\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check.
213	
214	\section{Within-Pool CI Details}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 904 · 2026-05-18T03:05:32.508511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "60",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "60",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-18T03:05:32.559213+00:00_

60	
61	\paragraph{Within-pool controlled comparison.}
62	\label{sec:within_pool}
63	Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
64	
65	\paragraph{Practical magnitude.}
66	\label{sec:practical_magnitude}
67	Direct regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$), scaling to 53\% at DocRED 96-rel. The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0]), roughly 7\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). High mean-BCS batches contain more active confusable pairs, concentrating degradation. A post-hoc Monte Carlo simulation reproducing the observed ${\sim}3\times$ pair-to-batch amplification (conditional $R^2 \approx 7\%$ among non-zero confusion pairs to batch $R^2 \approx 22\%$; Appendix~\ref{app:aggregation-sim}) confirms this aggregation pattern.
68	
69	\paragraph{Cross-model validation.}
70	The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap. Both models converge to $\approx$51\% under high confusability regardless of count, while divergence is confined to the low-BCS regime, suggesting a task-inherent difficulty floor under high confusability (Table~\ref{tab:cross_model_bcs}). Dimension~1 replicates fully on Llama-3.1-8B (\S\ref{sec:count_curves}); Dimension~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1). Additional validation on Llama-3.1-70B-Instruct (FP8) and Gemini 2.5 Flash (API) confirms directional consistency across model scales and architecture families, including a p
…[truncated 862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-18T03:05:36.378650+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "levy-2024-same-task",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "levy-2024-same-task",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 907 · 2026-05-18T03:05:36.429393+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex:5:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-18T03:05:39.642614+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "offset": "4",
  "limit": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "offset": "4",
    "limit": "2"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-18T03:05:39.643057+00:00_

4	\paragraph{Boundary conditions.}
5	The decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across models, suggesting a difficulty ceiling. RE's separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}). Cross-scale evidence (32B vs.\ 8B) shows Dimension~1 replicates fully while Dimension~2 attenuates on smaller models, dropping to near-zero $R^2$ for NER on Llama-3.1-8B (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}). Count-related degradation may partly reflect prompt length (per-type recall 0.586 vs.\ single-pass 0.368, consistent with lost-in-middle effects; \citealt{lost-in-middle-2024}; \citealt{levy-2024-same-task}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---
