# Reviewer 1 coordination — Part 5 of 5

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../reviewer-1-coordination.md) · [Structured JSON](../../../sessions/a8/a8128143e1651a7a7a07.json)

## Round 57

### Tool result

_source line 2272 · 2026-05-23T12:39:15.882694+00:00_

# ARR Reviewer Guidelines: Key Instructions

## Core Focus Areas

Reviewers should prioritize:

1. **Technical Soundness**: Validate methodology, proof correctness, and argumentation quality
2. **Novelty Assessment**: Determine if work advances knowledge, avoiding hindsight bias that makes contributions seem "obvious"
3. **Appropriate Scoping**: Ensure claims match evidence presented, particularly for short papers
4. **Clarity**: Specify issues precisely rather than using vague language

## Novelty vs. Soundness Distinction

The guidelines emphasize these are separate concerns. A paper can be technically sound but personally uninteresting. Conversely, "SOTA results are neither necessary nor sufficient for a scientific contribution"—papers offering improvements in efficiency, interpretability, or fairness matter even without benchmark dominance.

## Major vs. Minor Issues

**Major issues** require justification that the problem prevents answering the stated research question. Common pitfalls misclassified as major weaknesses include:

- "Results seem obvious" (hindsight bias)
- "Method too simple" (simplicity is preferable)
- "Missing extra experiment X" (only needed if essential to claims)
- "Lacks recent baselines" (without specific, relevant models cited)

**Minor issues** belong in suggestions: clarification improvements, additional analyses, methodology alternatives.

## Scoring Dimensions (Starting February 2025)

**Soundness**: Technical validity and reproducibility. "Scores must be justified by review text"—low scores require identified faults.

**Excitement**: Personal interest, orthogonal to soundness. Reflects subjective taste without requiring explicit justification.

**Overall Recommendation**: Composite assessment balancing soundness, novelty, and potential impact across the field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6526
}
```

</details>

---


### Tool call

_source line 2273 · 2026-05-23T12:43:03.328069+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 研究问题新颖（递归合成文本的代际深度估计），实验覆盖面广且统计方法严谨，但 K*_empirical 的样本量稳定性存疑、实际过滤场景下各策略趋同削弱了实用价值、部分核心声明存在过度概括。\n\n## 官方维度打分（来自 ACL ARR review form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计检验体系完善（permutation test, bootstrap CI, Bonferroni correction），但 K*_empirical 在 5K→10K 时出现方向不一致的漂移（Table 28），θ=0.60 阈值敏感性使核心结论依赖单一操作点；DPI 理论动机使用合理但未过度声称 |\n| Excitement | 3.5/5 | \"代际深度估计\"是二元检测之外的新角度，\"one-wash laundering\"发现有概念价值；但 K*_empirical ≤ 2 意味着仅比二元分类多一层粒度，实际过滤场景（≤50% 污染）各策略无显著差异（Section 5），实用增量有限 |\n| Reproducibility | 4/5 | 超参数报告完整（Appendix Table 15），特征定义明确（Table 14），实验设置详尽；但代码和数据仅承诺\"upon acceptance\"发布 |\n| Confidence | 4/5 | 仔细阅读全文及全部附录，熟悉合成文本检测和数据污染相关工作 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] K*_empirical 估计在样本量变化时不稳定\n- 具体位置：Appendix B.11, Table 28 (p.18)\n- 问题：LLaMA-8B continuation 从 5K 样本的 K*_empirical=2 降至 10K 样本的 K*_empirical=1（1v2 AUC 从 >0.60 降至 0.5400）；同时 Gemma-2-2B 从 5K 的 K*_empirical=1 升至 10K 的 K*_empirical=2†。这表明在标准样本量（5K）下，部分配置的 K*_empirical 处于 θ 阈值的边际区域，估计结果对采样噪声敏感。\n- 为什么影响接收：论文主要结论 \"K*_empirical ≤ 2 across all 10 configurations\"（Abstract, Section 4.1）依赖于 5K 样本下的结果。如果 LLaMA-8B 在 10K 下实际为 K*_empirical=1，那么 \"6/10 configurations yield K*_empirical=2\" 这个数字需要修正。更根本地，如果 K*_empirical 随样本量双向漂移，读者无法判断哪个估计值是可靠的。\n- 建议修改方向：(a) 对所有 10 个配置统一在 10K 样本下报告结果，或论证 5K 足够（当前仅对 6 个配置做了 10K 验证）；(b) 对 K*_empirical 本身进行 bootstrap（不只是对 boundary AUC），量化 K*_empirical 的离散估计不确定性；(c) 将 Table 28 的发现从附录提升至正文讨论，而非只在附录中用脚注标记。\n\n**N2** [critical] 下游过滤实验在现实污染比例下各策略趋同，削弱实际应用价值\n- 具体位置：Section 5, Table 5 (p.7)\n- 问题：论文声称 K*_empirical=2 的一个重要实用推论是 \"binary filtering outperforms graduated alternatives\"（Abstract 第 6 句）。但 Table 5 显示：在污染比例 ≤50% 时，所有 6 种过滤策略（包括 no-filter）的 MMLU/HellaSwag 差异不显著（p > 0.12）。仅在 100% 合成数据这一极端设定下，binary 才显著优于 graduated（MMLU 降幅 -0.77 pp vs -1.53 pp）。\n- 为什么影响接收：100% 合成污染是不现实的场景。在现实应用场景下（论文自己也提到 \"real-world contamination ratios are typically lower\"），K*-guided filtering 的预测是空洞的——不是因为 binary 优于 graduated，而是因为所有方法等价（包括什么都不做）。这使得 Section 5 的 \"consistency check\" 无法有效区分 K*_empirical 框架是否真正提供了实际指导价值。\n- 建议修改方向：(a) 补充中等污染比例（10-30%）下更细粒度的 dose-response 实验，使用更大的评测集以提高统计功效；(b) 在 abstract/conclusion 中对过滤场景的声明加限定条件（如 \"at high contamination ratios\"）；(c) 讨论为什么在低污染率下所有方法趋同——是因为信号太弱，还是因为评测指标（MMLU/HellaSwag）对这种级别的数据质量差异不敏感。\n\n**N3** [critical] \"Generator-agnostic\" 声明范围过大\n- 具体位置：Abstract 第 5 句, Section 4.2 (p.5), Section 4.3 (p.5)\n- 问题：Abstract 声称 \"Generator-agnostic statistical features enable 80-92% cross-model transfer\"，但 Section 4.2 的跨模型迁移实验仅在 continuation-mode 模型间进行（Pythia, OLMo, Qwen-cont），且 Figure 4 的迁移矩阵排除了 rewrite mode。Section 4.3 明确指出 continuation-mode 和 rewrite-mode 的特征排序存在显著差异。这意味着 \"generator-agnostic\" 在严格意义上仅对 continuation-mode 成立，不涵盖 rewrite mode。\n- 为什么影响接收：这是 abstract 中三个核心贡献之一。Rewrite mode 是实际场景中常见的合成文本生成方式（如 paraphrasing, rewriting），将其排除在 \"generator-agnostic\" 声明之外会误导读者。\n- 建议修改方向：在 abstract 和 conclusion 中将 \"generator-agnostic\" 限定为 \"generator-agnostic within continuation-mode models\"，或补充 rewrite-mode 的跨模型迁移实验。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] θ=0.60 阈值选择的理论根基需加强\n- 具体位置：Section 3.1 (p.3), Figure 3 (p.6)\n- 问题：θ=0.60 基于 Cohen's h ≈ 0.20 的映射。但 Cohen's h 衡量的是两个比例之间的距离，将 AUC（一个概率积分）直接当作比例计算 h 值是一种简化，其有效性依赖于评分分布的假设（如正态性、等方差），而论文未验证这些假设。Figure 3 显示 K*_empirical 在 θ∈[0.55, 0.70] 范围内从 3 变到 1，核心结论高度依赖这个单一操作点。\n- 建议：(a) 验证 pairwise AUC 评分的分布形态，以论证 Cohen's h 映射的适用性；(b) 在正文中呈现 K*_empirical(θ) 的完整轮廓（目前 Figure 3 已有但未充分讨论），将 K*_empirical 定位为 θ 的函数而非固定常数。\n\n**W2** [warning] 缺少 13B+ 模型和 RLHF/DPO 对齐模型\n- 具体位置：Limitations (1), p.9\n- 问题：所有测试模型 ≤ 8B 参数。更大的模型（如 LLaMA-70B, Qwen-72B）可能产生更高质量的文本，使代际间差异更细微或更明显——方向不确定。RLHF/DPO 对齐模型的生成分布与 base/instruct 模型不同（PPO 优化可能引入特定的统计指纹），论文不覆盖这类模型限制了结论的外推性。\n- 建议：论文已在 Limitations 中提及，但应在 Discussion (Section 6) 中更深入地讨论模型规模对 K*_empirical 的可能影响方向，并引用 model collapse 文献中关于模型规模效应的发现。\n\n**W3** [warning] Qwen 在实验矩阵中的过度代表\n- 具体位置：Table 1 (p.4)\n- 问题：10 个配置中 4 个是 Qwen 变体（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B），占 40%。当论文声称 \"across all 10 configurations\" 时，如果 Qwen 的 4 个配置表现一致，这可能夸大了结论的独立性。\n- 建议：在正文中增加按架构族分组的结果呈现（如 \"across 6 architecture families\" 而非 \"across 10 configurations\"），使读者能区分独立架构族和同族变体。\n\n**W4** [warning] \"One-wash laundering\" 概念的精确性\n- 具体位置：Abstract 第 4 句, Section 6 (p.7-8)\n- 问题：K*_empirical=2 意味着 0v1 和 1v2 都可区分，仅 ≥2 深度不可区分。\"One-wash laundering\" 一词暗示一次生成即可消除检测信号，但实际上 0v1 检测 AUC > 0.90 仍然非常强。更精确地说，这是 \"depth-signal laundering\"（深度信号被洗掉）而非 \"detection-signal laundering\"（检测信号被洗掉）。虽然论文在 \"concentrates all exploitable signal at the human-vs.-machine boundary\" 这句话中做了限定，但 \"laundering\" 一词在广义理解上容易被误解为合成文本可通过一次转写逃避检测。\n- 建议：在 Section 6 首次使用 \"one-wash laundering\" 时增加一句明确澄清：二元检测（human vs. machine）不受影响（0v1 AUC 保持 >0.90），被 \"洗掉\" 的是深度区分信号（depth discrimination beyond the binary boundary）。\n\n**W5** [warning] Retrain-chain 讨论段落的表述不清\n- 具体位置：Section 6, \"Prompt-chain scope and retrain-chain gap\" (p.8)\n- 问题：这段文字在一个句子中同时提到了 K*_empirical=1 和 K*_empirical=7，以及 AUC 范围 0.485-0.903，但未清晰说明这些数值分别对应哪些配置。读者需要反复阅读才能理解 OLMo retrain chain 的 K*_empirical 与 Pythia/Qwen retrain chain 的 K*_empirical 有何不同。\n- 建议：分句说明每个架构族在 retrain-chain 下的 K*_empirical，或添加一个小表格。\n\n---\n\n## 小问题（不影响接收）\n\n- **Abstract 字数**：约 147 词，符合 ≤200 词要求。✓\n- **正文页数**：主体文本 8 页（含 Conclusion，不含 Limitations/Ethics/References），符合长文限制。✓\n- **Limitations section**：1 个，放在正文中（p.9），appendix 中没有额外的 limitations section。✓\n- **匿名合规**：作者为 \"Anonymous\"，未发现自引或 GitHub 链接等去匿名化泄露。✓\n- **破折号检查**：正文行文中未发现 em-dash（`---`），仅在表格占位符中使用。✓\n- **En-dash 用于数值范围**（如 1B–8B, 80–92%）：符合 LaTeX/ACL 排版规范。✓\n- Table 1 \"Config\" 列中模型缩写（如 \"Qwen-rw\" vs \"Qwen-cont\"）在首次出现时可增加一句简要说明，便于快速理解。\n- Eq. 1 中 K*_empirical 的定义要求所有 AUC_{j,j+1} > θ（从 j=1 到 j=k），如果中间某深度 AUC 非单调下降后又回升（论文在 Section 3.1 提到 AUC 非单调的可能性），K*_empirical 会低估真实可区分深度。论文已部分讨论，但可更明确说明这是保守估计的设计选择。\n\n---\n\n## 主要优势\n\n1. **研究问题新颖且有意义**：从二元检测（human vs. machine）扩展到有序深度估计，填补了文献空白。在训练数据污染日益严重的背景下，理解 \"生成了多少轮\" 是一个自然且重要的问题。\n\n2. **统计方法严谨全面**：permutation test（10,000 次）、bootstrap 95% CI、Bonferroni correction for 10 comparisons 的组合使用正确；θ 敏感性分析（Figure 3）和跨种子鲁棒性检查（Table 26）体现了方法论的严谨性。\n\n3. **实验覆盖面广**：6 个架构族、4 个领域、4 种解码策略、15 维统计特征，构成了一个系统性的实验矩阵。附录中的 29 张表格和大量消融实验展示了全面的 sensitivity analysis。\n\n4. **\"One-wash laundering\" 概念有解释力**：AUC 从 0v1（>0.90）急剧下降到 2v3（~0.55）的模式在多个配置中高度一致，这一经验规律本身就是有价值的发现，为数据筛选策略提供了实证基础。\n\n5. **跨模型迁移结果有实践意义**：continuation-mode 下 80-92% 的 accuracy retention 和 ρ > 0.90 的特征排序一致性，表明深度估计可在未知生成器上部署（尽管限于 continuation mode）。\n\n6. **下游验证实验（Section 5）**：将 K*_empirical 预测与实际过滤性能对接，提供了 falsifiable 的验证，这在分析型论文中不常见。\n\n---\n\n## 对作者的提问（Questions to Authors）\n\n1. Table 28 中 LLaMA-8B 从 5K→10K 的 K*_empirical 下降是否说明 5K 样本量对于某些配置不够充分？如果对所有 10 个配置统一使用 10K 样本，主要结论是否需要修改？\n\n2. 在现实污染比例（10-30%）下，是否有更敏感的下游评测指标（如 perplexity on held-out data, generation diversity metrics）能区分不同过滤策略的效果？\n\n3. Cross-model transfer 是否测试过 rewrite-mode→continuation-mode 的跨模式迁移？如果没有，作者认为此方向迁移的主要困难是什么？\n\n4. DeBERTa upper-bound probe（Table 29）在 arXiv 上将 K*_empirical 提升至 4。如果使用更强的特征提取器（如 GPT-2 perplexity features, semantic similarity features），K*_empirical 是否可能进一步提升？这是否暗示 15 维统计特征 substantially underestimates K*_theory？",
  "reviewer_id": "1",
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 研究问题新颖（递归合成文本的代际深度估计），实验覆盖面广且统计方法严谨，但 K*_empirical 的样本量稳定性存疑、实际过滤场景下各策略趋同削弱了实用价值、部分核心声明存在过度概括。\n\n## 官方维度打分（来自 ACL ARR review form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计检验体系完善（permutation test, bootstrap CI, Bonferroni correction），但 K*_empirical 在 5K→10K 时出现方向不一致的漂移（Table 28），θ=0.60 阈值敏感性使核心结论依赖单一操作点；DPI 理论动机使用合理但未过度声称 |\n| Excitement | 3.5/5 | \"代际深度估计\"是二元检测之外的新角度，\"one-wash laundering\"发现有概念价值；但 K*_empirical ≤ 2 意味着仅比二元分类多一层粒度，实际过滤场景（≤50% 污染）各策略无显著差异（Section 5），实用增量有限 |\n| Reproducibility | 4/5 | 超参数报告完整（Appendix Table 15），特征定义明确（Table 14），实验设置详尽；但代码和数据仅承诺\"upon acceptance\"发布 |\n| Confidence | 4/5 | 仔细阅读全文及全部附录，熟悉合成文本检测和数据污染相关工作 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] K*_empirical 估计在样本量变化时不稳定\n- 具体位置：Appendix B.11, Table 28 (p.18)\n- 问题：LLaMA-8B continuation 从 5K 样本的 K*_empirical=2 降至 10K 样本的 K*_empirical=1（1v2 AUC 从 >0.60 降至 0.5400）；同时 Gemma-2-2B 从 5K 的 K*_empirical=1 升至 10K 的 K*_empirical=2†。这表明在标准样本量（5K）下，部分配置的 K*_empirical 处于 θ 阈值的边际区域，估计结果对采样噪声敏感。\n- 为什么影响接收：论文主要结论 \"K*_empirical ≤ 2 across all 10 configurations\"（Abstract, Section 4.1）依赖于 5K 样本下的结果。如果 LLaMA-8B 在 10K 下实际为 K*_empirical=1，那么 \"6/10 configurations yield K*_empirical=2\" 这个数字需要修正。更根本地，如果 K*_empirical 随样本量双向漂移，读者无法判断哪个估计值是可靠的。\n- 建议修改方向：(a) 对所有 10 个配置统一在 10K 样本下报告结果，或论证 5K 足够（当前仅对 6 个配置做了 10K 验证）；(b) 对 K*_empirical 本身进行 bootstrap（不只是对 boundary AUC），量化 K*_empirical 的离散估计不确定性；(c) 将 Table 28 的发现从附录提升至正文讨论，而非只在附录中用脚注标记。\n\n**N2** [critical] 下游过滤实验在现实污染比例下各策略趋同，削弱实际应用价值\n- 具体位置：Section 5, Table 5 (p.7)\n- 问题：论文声称 K*_empirical=2 的一个重要实用推论是 \"binary filtering outperforms graduated alternatives\"（Abstract 第 6 句）。但 Table 5 显示：在污染比例 ≤50% 时，所有 6 种过滤策略（包括 no-filter）的 MMLU/HellaSwag 差异不显著（p > 0.12）。仅在 100% 合成数据这一极端设定下，binary 才显著优于 graduated（MMLU 降幅 -0.77 pp vs -1.53 pp）。\n- 为什么影响接收：100% 合成污染是不现实的场景。在现实应用场景下（论文自己也提到 \"real-world contamination ratios are typically lower\"），K*-guided filtering 的预测是空洞的——不是因为 binary 优于 graduated，而是因为所有方法等价（包括什么都不做）。这使得 Section 5 的 \"consistency check\" 无法有效区分 K*_empirical 框架是否真正提供了实际指导价值。\n- 建议修改方向：(a) 补充中等污染比例（10-30%）下更细粒度的 dose-response 实验，使用更大的评测集以提高统计功效；(b) 在 abstract/conclusion 中对过滤场景的声明加限定条件（如 \"at high contamination ratios\"）；(c) 讨论为什么在低污染率下所有方法趋同——是因为信号太弱，还是因为评测指标（MMLU/HellaSwag）对这种级别的数据质量差异不敏感。\n\n**N3** [critical] \"Generator-agnostic\" 声明范围过大\n- 具体位置：Abstract 第 5 句, Section 4.2 (p.5), Section 4.3 (p.5)\n- 问题：Abstract 声称 \"Generator-agnostic statistical features enable 80-92% cross-model transfer\"，但 Section 4.2 的跨模型迁移实验仅在 continuation-mode 模型间进行（Pythia, OLMo, Qwen-cont），且 Figure 4 的迁移矩阵排除了 rewrite mode。Section 4.3 明确指出 continuation-mode 和 rewrite-mode 的特征排序存在显著差异。这意味着 \"generator-agnostic\" 在严格意义上仅对 continuation-mode 成立，不涵盖 rewrite mode。\n- 为什么影响接收：这是 abstract 中三个核心贡献之一。Rewrite mode 是实际场景中常见的合成文本生成方式（如 paraphrasing, rewriting），将其排除在 \"generator-agnostic\" 声明之外会误导读者。\n- 建议修改方向：在 abstract 和 conclusion 中将 \"generator-agnostic\" 限定为 \"generator-agnostic within continuation-mode models\"，或补充 rewrite-mode 的跨模型迁移实验。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] θ=0.60 阈值选择的理论根基需加强\n- 具体位置：Section 3.1 (p.3), Figure 3 (p.6)\n- 问题：θ=0.60 基于 Cohen's h ≈ 0.20 的映射。但 Cohen's h 衡量的是两个比例之间的距离，将 AUC（一个概率积分）直接当作比例计算 h 值是一种简化，其有效性依赖于评分分布的假设（如正态性、等方差），而论文未验证这些假设。Figure 3 显示 K*_empirical 在 θ∈[0.55, 0.70] 范围内从 3 变到 1，核心结论高度依赖这个单一操作点。\n- 建议：(a) 验证 pairwise AUC 评分的分布形态，以论证 Cohen's h 映射的适用性；(b) 在正文中呈现 K*_empirical(θ) 的完整轮廓（目前 Figure 3 已有但未充分讨论），将 K*_empirical 定位为 θ 的函数而非固定常数。\n\n**W2** [warning] 缺少 13B+ 模型和 RLHF/DPO 对齐模型\n- 具体位置：Limitations (1), p.9\n- 问题：所有测试模型 ≤ 8B 参数。更大的模型（如 LLaMA-70B, Qwen-72B）可能产生更高质量的文本，使代际间差异更细微或更明显——方向不确定。RLHF/DPO 对齐模型的生成分布与 base/instruct 模型不同（PPO 优化可能引入特定的统计指纹），论文不覆盖这类模型限制了结论的外推性。\n- 建议：论文已在 Limitations 中提及，但应在 Discussion (Section 6) 中更深入地讨论模型规模对 K*_empirical 的可能影响方向，并引用 model collapse 文献中关于模型规模效应的发现。\n\n**W3** [warning] Qwen 在实验矩阵中的过度代表\n- 具体位置：Table 1 (p.4)\n- 问题：10 个配置中 4 个是 Qwen 变体（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B），占 40%。当论文声称 \"across all 10 configurations\" 时，如果 Qwen 的 4 个配置表现一致，这可能夸大了结论的独立性。\n- 建议：在正文中增加按架构族分组的结果呈现（如 \"across 6 architecture families\" 而非 \"across 10 configurations\"），使读者能区分独立架构族和同族变体。\n\n**W4** [warning] \"One-wash laundering\" 概念的精确性\n- 具体位置：Abstract 第 4 句, Section 6 (p.7-8)\n- 问题：K*_empirical=2 意味着 0v1 和 1v2 都可区分，仅 ≥2 深度不可区分。\"One-wash laundering\" 一词暗示一次生成即可消除检测信号，但实际上 0v1 检测 AUC > 0.90 仍然非常强。更精确地说，这是 \"depth-signal laundering\"（深度信号被洗掉）而非 \"detection-signal laundering\"（检测信号被洗掉）。虽然论文在 \"concentrates all exploitable signal at the human-vs.-machine boundary\" 这句话中做了限定，但 \"laundering\" 一词在广义理解上容易被误解为合成文本可通过一次转写逃避检测。\n- 建议：在 Section 6 首次使用 \"one-wash laundering\" 时增加一句明确澄清：二元检测（human vs. machine）不受影响（0v1 AUC 保持 >0.90），被 \"洗掉\" 的是深度区分信号（depth discrimination beyond the binary boundary）。\n\n**W5** [warning] Retrain-chain 讨论段落的表述不清\n- 具体位置：Section 6, \"Prompt-chain scope and retrain-chain gap\" (p.8)\n- 问题：这段文字在一个句子中同时提到了 K*_empirical=1 和 K*_empirical=7，以及 AUC 范围 0.485-0.903，但未清晰说明这些数值分别对应哪些配置。读者需要反复阅读才能理解 OLMo retrain chain 的 K*_empirical 与 Pythia/Qwen retrain chain 的 K*_empirical 有何不同。\n- 建议：分句说明每个架构族在 retrain-chain 下的 K*_empirical，或添加一个小表格。\n\n---\n\n## 小问题（不影响接收）\n\n- **Abstract 字数**：约 147 词，符合 ≤200 词要求。✓\n- **正文页数**：主体文本 8 页（含 Conclusion，不含 Limitations/Ethics/References），符合长文限制。✓\n- **Limitations section**：1 个，放在正文中（p.9），appendix 中没有额外的 limitations section。✓\n- **匿名合规**：作者为 \"Anonymous\"，未发现自引或 GitHub 链接等去匿名化泄露。✓\n- **破折号检查**：正文行文中未发现 em-dash（`---`），仅在表格占位符中使用。✓\n- **En-dash 用于数值范围**（如 1B–8B, 80–92%）：符合 LaTeX/ACL 排版规范。✓\n- Table 1 \"Config\" 列中模型缩写（如 \"Qwen-rw\" vs \"Qwen-cont\"）在首次出现时可增加一句简要说明，便于快速理解。\n- Eq. 1 中 K*_empirical 的定义要求所有 AUC_{j,j+1} > θ（从 j=1 到 j=k），如果中间某深度 AUC 非单调下降后又回升（论文在 Section 3.1 提到 AUC 非单调的可能性），K*_empirical 会低估真实可区分深度。论文已部分讨论，但可更明确说明这是保守估计的设计选择。\n\n---\n\n## 主要优势\n\n1. **研究问题新颖且有意义**：从二元检测（human vs. machine）扩展到有序深度估计，填补了文献空白。在训练数据污染日益严重的背景下，理解 \"生成了多少轮\" 是一个自然且重要的问题。\n\n2. **统计方法严谨全面**：permutation test（10,000 次）、bootstrap 95% CI、Bonferroni correction for 10 comparisons 的组合使用正确；θ 敏感性分析（Figure 3）和跨种子鲁棒性检查（Table 26）体现了方法论的严谨性。\n\n3. **实验覆盖面广**：6 个架构族、4 个领域、4 种解码策略、15 维统计特征，构成了一个系统性的实验矩阵。附录中的 29 张表格和大量消融实验展示了全面的 sensitivity analysis。\n\n4. **\"One-wash laundering\" 概念有解释力**：AUC 从 0v1（>0.90）急剧下降到 2v3（~0.55）的模式在多个配置中高度一致，这一经验规律本身就是有价值的发现，为数据筛选策略提供了实证基础。\n\n5. **跨模型迁移结果有实践意义**：continuation-mode 下 80-92% 的 accuracy retention 和 ρ > 0.90 的特征排序一致性，表明深度估计可在未知生成器上部署（尽管限于 continuation mode）。\n\n6. **下游验证实验（Section 5）**：将 K*_empirical 预测与实际过滤性能对接，提供了 falsifiable 的验证，这在分析型论文中不常见。\n\n---\n\n## 对作者的提问（Questions to Authors）\n\n1. Table 28 中 LLaMA-8B 从 5K→10K 的 K*_empirical 下降是否说明 5K 样本量对于某些配置不够充分？如果对所有 10 个配置统一使用 10K 样本，主要结论是否需要修改？\n\n2. 在现实污染比例（10-30%）下，是否有更敏感的下游评测指标（如 perplexity on held-out data, generation diversity metrics）能区分不同过滤策略的效果？\n\n3. Cross-model transfer 是否测试过 rewrite-mode→continuation-mode 的跨模式迁移？如果没有，作者认为此方向迁移的主要困难是什么？\n\n4. DeBERTa upper-bound probe（Table 29）在 arXiv 上将 K*_empirical 提升至 4。如果使用更强的特征提取器（如 GPT-2 perplexity features, semantic similarity features），K*_empirical 是否可能进一步提升？这是否暗示 15 维统计特征 substantially underestimates K*_theory？",
    "reviewer_id": "1",
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2274 · 2026-05-23T12:43:07.247973+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3919
}
```

</details>

---


### Assistant

_source line 2275 · 2026-05-23T12:43:21.808009+00:00_

审稿意见已提交给 Review Director。

**评分概要：**
- **Overall: 3.5 (Borderline Conference)**
- Soundness: 3.5/5, Excitement: 3.5/5, Reproducibility: 4/5

**3 个 Must-Fix 问题：**
1. **K\*\_empirical 样本量不稳定** — LLaMA-8B 在 5K→10K 时从 K\*=2 降至 K\*=1（Table 28），Gemma-2-2B 反向漂移，核心结论的可靠性受质疑
2. **下游过滤实验在现实污染比例下各策略趋同** — ≤50% 污染时所有方法无显著差异（p>0.12），100% 污染是不现实场景，削弱实用价值声明
3. **"Generator-agnostic" 声明过度** — 跨模型迁移仅在 continuation-mode 间验证，rewrite mode 被排除在外

**5 个 Should-Fix 问题：** θ=0.60 阈值理论根基、缺少 13B+/RLHF 模型、Qwen 过度代表（4/10）、"one-wash laundering" 术语精确性、retrain-chain 段落表述不清。

格式合规方面全部通过（abstract 147词、正文 8 页、Limitations 1 个在正文中、匿名合规、无破折号违规）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1"
}
```

</details>

---


## Round 58

## Round 58

18 recorded events


### User

_source line 2276 · 2026-05-23T12:44:14.503107+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿原文：

**Overall**: 3.5 (Borderline Conference)

### Must-Fix

**R2-N1** [critical] Related Work 遗漏 text watermarking 作为 depth tracking 的替代方案
- Section 2 和 Section 6 完全未讨论 text watermarking（Kirchenbauer et al., 2023; SynthID 等）。Watermarking 是工业界追踪合成文本 provenance 的主流方法，理论上可在每轮生成时嵌入标记实现精确 depth tracking。论文的 post-hoc 统计检测与 watermarking 的 proactive embedding 形成互补，但未提及这一对比。

**R2-N2** [critical] Dose-response 实验暴露实用性局限，但被埋在 Appendix
- Table 25 (Appendix B.8) 显示 10% 污染率下 no-filter MMLU (0.6009) 与 base model (0.6018) 差异仅 0.09pp，≤50% 污染率下所有 filtering 策略效果不显著。但 Introduction 动机叙述和 Section 5 使用 100% 合成数据。论文将 K*_empirical 与数据 curation 实际价值挂钩（contribution (c)），但 dose-response 证据表明这种挂钩在低污染率下不成立。

### Should-Fix

**R2-W1** K*_empirical 的阈值依赖性需要更透明的处理
- K*_empirical 的 "≤ 2" 取决于 θ=0.60。Figure 3 显示 θ 在 [0.55, 0.70] 范围内 K*_empirical 从 3 到 1。主文叙述给读者的印象是这是一个稳健结论。建议报告 K*_empirical 在 θ 区间上的行为。

**R2-W2** 方法论贡献定位不够清晰
- 15 个统计特征 + OBD LightGBM 均为现有技术直接应用。Contribution list 的呈现让读者可能误认为方法本身有创新。应更明确定位为 "empirical characterization using existing tools"。

**R2-W3** Abstract 中 "80-92% cross-model transfer" 缺少 continuation-mode 限定
- 这个数字仅适用于 continuation mode，rewrite mode 跨模型迁移仅 61-63%。

**R2-W4** 模型配置不平衡（Qwen 占 4/10）
- "across 6 architecture families" 的叙述给人均匀覆盖的印象，但 Qwen 贡献了 6/10 中的 4/6 个 K*_empirical=2 配置。

**R2-W5** "One-wash laundering" 与已知 model collapse 现象的关系界定不清
- model collapse 文献已建立递归生成中信息退化在早期最剧烈的认知。"One-wash laundering" 本质是同一现象的检测视角重述。

### 缺失引用
1. Kirchenbauer et al., 2023 "A Watermark for Large Language Models" ICML
2. Christ et al., 2024 "Undetectable Watermarks for Language Models"
3. SynthID / C2PA content credentials
4. 2025-2026 multi-class AI text detection 工作

### 小问题
1. Figure 4 文字过小
2. Table 2 密度过高
3. Section 4.4 Neural Probe 比较需更多 caveat
4. 未报告计算开销
5. 符号 K* vs K*_empirical 偶尔混用
6. Appendix B.8 dose-response 应提升至正文

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2277 · 2026-05-23T12:44:57.730059+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/submitted.pdf",
  "project": "gen-depth-contamination",
  "pages": "1-3",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/submitted.pdf",
    "project": "gen-depth-contamination",
    "pages": "1-3",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2278 · 2026-05-23T12:44:58.284203+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.9}], \"total_pages\": 18, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 2279 · 2026-05-23T12:45:02.248874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 2280 · 2026-05-23T12:45:03.102312+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 2281 · 2026-05-23T12:45:03.253961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 2282 · 2026-05-23T12:45:03.254422+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 2283 · 2026-05-23T12:45:04.312097+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---


### Tool result

_source line 2284 · 2026-05-23T12:45:04.315501+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1061
}
```

</details>

---


### Tool call

_source line 2285 · 2026-05-23T12:45:11.292964+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/submitted.pdf",
  "project": "gen-depth-contamination",
  "pages": "7-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/submitted.pdf",
    "project": "gen-depth-contamination",
    "pages": "7-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2286 · 2026-05-23T12:45:11.544314+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 536.8}], \"total_pages\": 18, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2287 · 2026-05-23T12:45:14.205259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 2288 · 2026-05-23T12:45:14.757963+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_29/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 2289 · 2026-05-23T12:45:14.809373+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool result

_source line 2290 · 2026-05-23T12:45:15.362575+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 2291 · 2026-05-23T12:47:05.039071+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: Related Work 遗漏 text watermarking**\n\nR2 将此定为 critical，我认为应降级为 Should-Fix。理由如下：\n\n1. **范式根本不同**：Watermarking 是 proactive embedding（生成时嵌入标记），本文是 post-hoc statistical detection（对已有文本做深度估计）。两者的应用前提完全不同——watermarking 要求控制生成过程，而本文面向的场景是从未知来源的语料中 post-hoc 判断深度。Section 2 的 Related Work 按功能分类（detection / curation / ordinal classification），watermarking 不属于其中任何一类。\n\n2. **不影响核心论证**：论文的 contribution 是测量 K*_empirical 这一经验边界，watermarking 的存在与否不影响 K*_empirical 的定义、测量方法或实验结论。\n\n3. **但确实值得提及**：作为 depth tracking 的替代范式，在 Section 2 或 Section 6 中用 1-2 句话说明 \"watermarking 可实现精确 depth tracking 但要求控制生成端，本文解决的是无法控制生成端时的 post-hoc 检测\" 是合理的补充。\n\n结论：应加一句定位说明，但不构成 Must-Fix。ARR reviewer guidelines 明确指出 \"missing extra experiment X\" 或遗漏引用在不影响 stated research question 时不应作为 major weakness。\n\n---\n\n**[AGREE] R2-N2: Dose-response 实验暴露实用性局限**\n\n我在 R1-N2 中提出了实质相同的问题。补充两点：\n\n1. **主文并非完全回避**：Section 5 (p.7) 明确写了 \"At realistic contamination ratios (≤50%), all filtering strategies converge (p > 0.12)\"，所以核心发现在正文中有体现，并非完全 \"buried\"。但 R2 说得对——具体的 dose-response 数据（Table 25）仅在 Appendix B.8，读者需要自己翻到附录才能看到 10%/30%/50% 的具体数值。\n\n2. **更关键的是 contribution (c) 的表述问题**：Abstract 第 6 句 (\"K*_empirical correctly predicts that binary filtering outperforms graduated alternatives for web text\") 在 100% 污染时成立，但在 ≤50% 时 prediction 是 vacuous（因为所有方法等价）。建议 abstract 中加限定 \"at high contamination ratios\" 或改为 \"K*_empirical correctly predicts the convergence of filtering strategies\"。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: θ 阈值依赖性需更透明处理**\n\n与我的 R1-W1 一致。补充：Figure 3 (p.6) 已经提供了 θ 敏感性曲线，但仅在右栏一小段文字中讨论。如果在 Section 4.1 首次报告 K*_empirical=2 时就附带一句 \"K*_empirical(θ) ranges from 3 (θ=0.55) to 1 (θ=0.70); we report results at the reference operating point θ=0.60\"，读者会立即获得正确的心理模型，而非在 6 页之后才看到 sensitivity analysis。\n\n---\n\n**[REBUT] R2-W2: 方法论贡献定位不够清晰**\n\n部分不同意。\n\n1. **K*_empirical 的形式化定义本身是概念贡献**：Eq. 1 定义的 K*_empirical = max{k ≥ 1 : AUC_{j,j+1} > θ, ∀1 ≤ j ≤ k} 将 \"递归合成文本的可区分深度\" 操作化为一个可测量的量，这在先前文献中没有对应概念。Model collapse 文献（Shumailov et al., 2024; Dohmatob et al., 2024）研究质量退化但不提供 \"在哪个深度停止可区分\" 的形式化度量。Binary detection 文献（Mitchell et al., 2023; Hans et al., 2024）停留在 0v1。\n\n2. **OBD + LightGBM 确实是 existing tools**：R2 说得对，15 个统计特征和 OBD-LightGBM 均为直接应用（Table 14, Table 15）。论文没有声称分类器本身是贡献。\n\n3. **Contribution list 的实际措辞**：Section 1 (p.1) 的三个贡献分别是 \"(a) Measuring the discrimination boundary\"、\"(b) Domain dependence\"、\"(c) Generator-agnostic cross-model transfer\"，均以 empirical finding 的形式呈现，没有声称 \"我们提出了一种新方法\"。所以我认为定位已经是 \"empirical characterization\"，R2 的担忧有一定道理但程度上论文已经做了合理的自我定位。\n\n---\n\n**[AGREE] R2-W3: Abstract 中 \"80-92% cross-model transfer\" 缺少 continuation-mode 限定**\n\n完全同意。这与我的 R1-N3 实质相同。Abstract 第 5 句不加限定地写 \"Generator-agnostic statistical features enable 80-92% cross-model transfer\" 会误导读者。rewrite mode 跨模型迁移仅 61-63%（Section 4.2, p.5），是一个显著不同的结论。\n\n---\n\n**[AGREE] R2-W4: 模型配置不平衡（Qwen 4/10）**\n\n同意，与我的 R1-W3 一致。补充：4 个 Qwen 配置（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B）之间有 systematic correlation（同一 tokenizer、相似的 pretraining data），它们在 K*_empirical 上的一致性不能等同于独立架构族的一致性。论文应在报告 \"6/10 yield K*_empirical=2\" 时同时说明 \"across 4/6 independent architecture families\"。\n\n---\n\n**[REBUT] R2-W5: \"One-wash laundering\" 与 model collapse 的关系**\n\n部分反驳。R2 认为 one-wash laundering \"本质是 model collapse 同一现象的检测视角重述\"，我认为这低估了两者的区别。\n\n1. **Prompt chain ≠ Retrain chain**：Model collapse 文献（Shumailov et al., 2024; Alemohammad et al., 2024）研究的是 retrain chains（每轮用前一轮的合成数据重新训练模型），而本文的 one-wash laundering 发生在 prompt chains（模型参数不变，仅递归生成文本）。Section 6 (p.8) 明确展示了这一区别：retrain chains 下 Pythia 和 Qwen 的 K*_empirical=7（6v7 AUC = 0.634-0.641 > θ），远高于 prompt chains 的 K*_empirical=2。\n\n2. **信息退化的机制不同**：Retrain chain 的信息退化来自模型参数的 cumulative adaptation（分布漂移），而 prompt chain 的信息退化来自 text-level 的统计特征均质化。前者在 depth 7 仍可区分，后者在 depth 2 就已饱和——这是定量上的巨大差异，说明不是\"同一现象\"。\n\n3. **R2 有道理的部分**：\"递归生成中信息退化在早期最剧烈\"这一定性认知确实在 model collapse 文献中已有。论文应在 Section 6 中更明确地说明 \"one-wash laundering is the prompt-chain analogue of early-stage degradation observed in retrain-chain model collapse, but the two phenomena differ quantitatively: K*_empirical=2 for prompt chains vs. K*_empirical=7 for retrain chains\"。\n\n---\n\n### 缺失引用\n\n**[AGREE]** Kirchenbauer et al., 2023 和 SynthID/C2PA：同 R2-N1 的回应，值得在 Related Work 中用 1-2 句提及作为替代范式。\n\n**[REBUT]** Christ et al., 2024 \"Undetectable Watermarks\"：这篇论文讨论的是理论上不可检测的 watermark 的存在性，与 depth estimation 的关联很弱。仅在讨论 watermarking 局限性时才相关。\n\n**[AGREE with caveat]** \"2025-2026 multi-class AI text detection 工作\"：R2 未给出具体引用。如果存在直接做 multi-class depth classification 的工作，确实应该引用。但据我所知，现有 multi-class 工作（如将文本分类为 GPT-4/Claude/LLaMA 等不同来源）是 generator attribution，而非 depth estimation。R2 应具体指出缺失的引用。\n\n---\n\n### 小问题\n\n1. **[AGREE] Figure 4 文字过小**：从 PDF 观察确认，热力图中的数字在打印时可能难以辨认。\n2. **[AGREE] Table 2 密度过高**：Table 2 (p.4) 包含 10 个配置 × 5 个深度对的 AUC 值和 CI，确实密集。但考虑到 8 页限制，压缩是可以理解的。建议将部分配置移至 appendix。\n3. **[REBUT] Section 4.4 Neural Probe 需更多 caveat**：Section 4.4 (p.5) 已经说明了 neural probe 的局限性——它使用 frozen encoder 的隐层表示，K*_empirical 的提升（从 2 到 3）仅在 Qwen 上出现，Pythia 仍为 K*_empirical=2。论文清楚地将 neural probe 定位为 \"upper bound exploration\"，caveat 已经足够。\n4. **[AGREE] 未报告计算开销**：特征提取和分类器训练的计算成本确实未报告。对于 reproducibility 来说应补充。\n5. **[REBUT] K* vs K*_empirical 混用**：从 LaTeX 源码看，论文定义了 `\\Kstar`（K*）和 `\\Kempirical`（K*_empirical）两个宏。K* 在标题和简写语境中指代 K*_empirical（因为 K*_theory 在论文中基本未使用），我未在正文中发现造成歧义的混用。如果 R2 能指出具体位置会更有说服力。\n6. **[AGREE]** Appendix B.8 dose-response 应在正文中更充分讨论：同 R2-N2，但正文 Section 5 已经有一句总结。\n\n---\n\n### 总结\n\nR2 和我（R1）在以下核心问题上达成共识：\n- **实用性局限**（dose-response 在低污染率下趋同）→ 两人均标记为 critical\n- **\"Generator-agnostic\" 过度声明**（需限定 continuation-mode）→ R2 为 W3，R1 为 N3\n- **θ 阈值敏感性**→ 两人均标记为 Should-Fix\n- **Qwen 过度代表**→ 两人均标记为 Should-Fix\n\n我与 R2 的主要分歧：\n- **Watermarking 缺失**：R2 标为 critical，我认为是 Should-Fix（不影响核心论证）\n- **方法论贡献定位**：R2 认为不清晰，我认为论文已合理自我定位为 empirical characterization\n- **One-wash vs model collapse**：R2 认为是重述，我认为 prompt-chain 和 retrain-chain 的定量差异（K*=2 vs K*=7）表明这是相关但不同的现象",
  "reviewer_id": "1",
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: Related Work 遗漏 text watermarking**\n\nR2 将此定为 critical，我认为应降级为 Should-Fix。理由如下：\n\n1. **范式根本不同**：Watermarking 是 proactive embedding（生成时嵌入标记），本文是 post-hoc statistical detection（对已有文本做深度估计）。两者的应用前提完全不同——watermarking 要求控制生成过程，而本文面向的场景是从未知来源的语料中 post-hoc 判断深度。Section 2 的 Related Work 按功能分类（detection / curation / ordinal classification），watermarking 不属于其中任何一类。\n\n2. **不影响核心论证**：论文的 contribution 是测量 K*_empirical 这一经验边界，watermarking 的存在与否不影响 K*_empirical 的定义、测量方法或实验结论。\n\n3. **但确实值得提及**：作为 depth tracking 的替代范式，在 Section 2 或 Section 6 中用 1-2 句话说明 \"watermarking 可实现精确 depth tracking 但要求控制生成端，本文解决的是无法控制生成端时的 post-hoc 检测\" 是合理的补充。\n\n结论：应加一句定位说明，但不构成 Must-Fix。ARR reviewer guidelines 明确指出 \"missing extra experiment X\" 或遗漏引用在不影响 stated research question 时不应作为 major weakness。\n\n---\n\n**[AGREE] R2-N2: Dose-response 实验暴露实用性局限**\n\n我在 R1-N2 中提出了实质相同的问题。补充两点：\n\n1. **主文并非完全回避**：Section 5 (p.7) 明确写了 \"At realistic contamination ratios (≤50%), all filtering strategies converge (p > 0.12)\"，所以核心发现在正文中有体现，并非完全 \"buried\"。但 R2 说得对——具体的 dose-response 数据（Table 25）仅在 Appendix B.8，读者需要自己翻到附录才能看到 10%/30%/50% 的具体数值。\n\n2. **更关键的是 contribution (c) 的表述问题**：Abstract 第 6 句 (\"K*_empirical correctly predicts that binary filtering outperforms graduated alternatives for web text\") 在 100% 污染时成立，但在 ≤50% 时 prediction 是 vacuous（因为所有方法等价）。建议 abstract 中加限定 \"at high contamination ratios\" 或改为 \"K*_empirical correctly predicts the convergence of filtering strategies\"。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: θ 阈值依赖性需更透明处理**\n\n与我的 R1-W1 一致。补充：Figure 3 (p.6) 已经提供了 θ 敏感性曲线，但仅在右栏一小段文字中讨论。如果在 Section 4.1 首次报告 K*_empirical=2 时就附带一句 \"K*_empirical(θ) ranges from 3 (θ=0.55) to 1 (θ=0.70); we report results at the reference operating point θ=0.60\"，读者会立即获得正确的心理模型，而非在 6 页之后才看到 sensitivity analysis。\n\n---\n\n**[REBUT] R2-W2: 方法论贡献定位不够清晰**\n\n部分不同意。\n\n1. **K*_empirical 的形式化定义本身是概念贡献**：Eq. 1 定义的 K*_empirical = max{k ≥ 1 : AUC_{j,j+1} > θ, ∀1 ≤ j ≤ k} 将 \"递归合成文本的可区分深度\" 操作化为一个可测量的量，这在先前文献中没有对应概念。Model collapse 文献（Shumailov et al., 2024; Dohmatob et al., 2024）研究质量退化但不提供 \"在哪个深度停止可区分\" 的形式化度量。Binary detection 文献（Mitchell et al., 2023; Hans et al., 2024）停留在 0v1。\n\n2. **OBD + LightGBM 确实是 existing tools**：R2 说得对，15 个统计特征和 OBD-LightGBM 均为直接应用（Table 14, Table 15）。论文没有声称分类器本身是贡献。\n\n3. **Contribution list 的实际措辞**：Section 1 (p.1) 的三个贡献分别是 \"(a) Measuring the discrimination boundary\"、\"(b) Domain dependence\"、\"(c) Generator-agnostic cross-model transfer\"，均以 empirical finding 的形式呈现，没有声称 \"我们提出了一种新方法\"。所以我认为定位已经是 \"empirical characterization\"，R2 的担忧有一定道理但程度上论文已经做了合理的自我定位。\n\n---\n\n**[AGREE] R2-W3: Abstract 中 \"80-92% cross-model transfer\" 缺少 continuation-mode 限定**\n\n完全同意。这与我的 R1-N3 实质相同。Abstract 第 5 句不加限定地写 \"Generator-agnostic statistical features enable 80-92% cross-model transfer\" 会误导读者。rewrite mode 跨模型迁移仅 61-63%（Section 4.2, p.5），是一个显著不同的结论。\n\n---\n\n**[AGREE] R2-W4: 模型配置不平衡（Qwen 4/10）**\n\n同意，与我的 R1-W3 一致。补充：4 个 Qwen 配置（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B）之间有 systematic correlation（同一 tokenizer、相似的 pretraining data），它们在 K*_empirical 上的一致性不能等同于独立架构族的一致性。论文应在报告 \"6/10 yield K*_empirical=2\" 时同时说明 \"across 4/6 independent architecture families\"。\n\n---\n\n**[REBUT] R2-W5: \"One-wash laundering\" 与 model collapse 的关系**\n\n部分反驳。R2 认为 one-wash laundering \"本质是 model collapse 同一现象的检测视角重述\"，我认为这低估了两者的区别。\n\n1. **Prompt chain ≠ Retrain chain**：Model collapse 文献（Shumailov et al., 2024; Alemohammad et al., 2024）研究的是 retrain chains（每轮用前一轮的合成数据重新训练模型），而本文的 one-wash laundering 发生在 prompt chains（模型参数不变，仅递归生成文本）。Section 6 (p.8) 明确展示了这一区别：retrain chains 下 Pythia 和 Qwen 的 K*_empirical=7（6v7 AUC = 0.634-0.641 > θ），远高于 prompt chains 的 K*_empirical=2。\n\n2. **信息退化的机制不同**：Retrain chain 的信息退化来自模型参数的 cumulative adaptation（分布漂移），而 prompt chain 的信息退化来自 text-level 的统计特征均质化。前者在 depth 7 仍可区分，后者在 depth 2 就已饱和——这是定量上的巨大差异，说明不是\"同一现象\"。\n\n3. **R2 有道理的部分**：\"递归生成中信息退化在早期最剧烈\"这一定性认知确实在 model collapse 文献中已有。论文应在 Section 6 中更明确地说明 \"one-wash laundering is the prompt-chain analogue of early-stage degradation observed in retrain-chain model collapse, but the two phenomena differ quantitatively: K*_empirical=2 for prompt chains vs. K*_empirical=7 for retrain chains\"。\n\n---\n\n### 缺失引用\n\n**[AGREE]** Kirchenbauer et al., 2023 和 SynthID/C2PA：同 R2-N1 的回应，值得在 Related Work 中用 1-2 句提及作为替代范式。\n\n**[REBUT]** Christ et al., 2024 \"Undetectable Watermarks\"：这篇论文讨论的是理论上不可检测的 watermark 的存在性，与 depth estimation 的关联很弱。仅在讨论 watermarking 局限性时才相关。\n\n**[AGREE with caveat]** \"2025-2026 multi-class AI text detection 工作\"：R2 未给出具体引用。如果存在直接做 multi-class depth classification 的工作，确实应该引用。但据我所知，现有 multi-class 工作（如将文本分类为 GPT-4/Claude/LLaMA 等不同来源）是 generator attribution，而非 depth estimation。R2 应具体指出缺失的引用。\n\n---\n\n### 小问题\n\n1. **[AGREE] Figure 4 文字过小**：从 PDF 观察确认，热力图中的数字在打印时可能难以辨认。\n2. **[AGREE] Table 2 密度过高**：Table 2 (p.4) 包含 10 个配置 × 5 个深度对的 AUC 值和 CI，确实密集。但考虑到 8 页限制，压缩是可以理解的。建议将部分配置移至 appendix。\n3. **[REBUT] Section 4.4 Neural Probe 需更多 caveat**：Section 4.4 (p.5) 已经说明了 neural probe 的局限性——它使用 frozen encoder 的隐层表示，K*_empirical 的提升（从 2 到 3）仅在 Qwen 上出现，Pythia 仍为 K*_empirical=2。论文清楚地将 neural probe 定位为 \"upper bound exploration\"，caveat 已经足够。\n4. **[AGREE] 未报告计算开销**：特征提取和分类器训练的计算成本确实未报告。对于 reproducibility 来说应补充。\n5. **[REBUT] K* vs K*_empirical 混用**：从 LaTeX 源码看，论文定义了 `\\Kstar`（K*）和 `\\Kempirical`（K*_empirical）两个宏。K* 在标题和简写语境中指代 K*_empirical（因为 K*_theory 在论文中基本未使用），我未在正文中发现造成歧义的混用。如果 R2 能指出具体位置会更有说服力。\n6. **[AGREE]** Appendix B.8 dose-response 应在正文中更充分讨论：同 R2-N2，但正文 Section 5 已经有一句总结。\n\n---\n\n### 总结\n\nR2 和我（R1）在以下核心问题上达成共识：\n- **实用性局限**（dose-response 在低污染率下趋同）→ 两人均标记为 critical\n- **\"Generator-agnostic\" 过度声明**（需限定 continuation-mode）→ R2 为 W3，R1 为 N3\n- **θ 阈值敏感性**→ 两人均标记为 Should-Fix\n- **Qwen 过度代表**→ 两人均标记为 Should-Fix\n\n我与 R2 的主要分歧：\n- **Watermarking 缺失**：R2 标为 critical，我认为是 Should-Fix（不影响核心论证）\n- **方法论贡献定位**：R2 认为不清晰，我认为论文已合理自我定位为 empirical characterization\n- **One-wash vs model collapse**：R2 认为是重述，我认为 prompt-chain 和 retrain-chain 的定量差异（K*=2 vs K*=7）表明这是相关但不同的现象",
    "reviewer_id": "1",
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2292 · 2026-05-23T12:47:08.860002+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3820
}
```

</details>

---


### Assistant

_source line 2293 · 2026-05-23T12:47:15.186600+00:00_

交叉回应已提交给 Review Director。

核心判断：R2 的 6 个 Should-Fix 中我同意 4 个（W1/W3/W4 + 小问题部分），反驳 2 个（W2 方法定位已合理、W5 one-wash 与 model collapse 有实质区别）。R2 的 2 个 Must-Fix 中，N2（dose-response 实用性）我完全同意，N1（watermarking 缺失）我认为应降级为 Should-Fix。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1"
}
```

</details>

---


## Round 59

## Round 59

74 recorded events


### User

_source line 2294 · 2026-05-25T21:16:37.303427+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查**方法严谨性 + 实验设计 + 统计有效性**。

## 投稿信息
- **Venue**: EMNLP 2026（通过 ARR 统一审稿）
- **类别**: Long Paper (Main Conference)
- **页数限制**: 正文 8 页，references 无限，Limitations 不计入页数
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind（作者标为 Anonymous）
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/submitted.pdf`

## 你的审查侧重

1. **方法论**:
   - K*_empirical 的定义是否数学严谨？Eq.1 的 max 算子假设是否成立？
   - DPI 到 AUC 单调递减的推理链是否有逻辑缺口？
   - OBD-LightGBM 分类器设计是否合理？与 ordinal logistic regression 的对比是否公平？
   - θ=0.60 阈值选择的合理性——是否为 post-hoc？敏感性分析是否充分？

2. **实验设计**:
   - 10 个配置中 Qwen 占 4 个——是否过度代表？按 family 去重后结论是否仍然成立？
   - 5K 样本量是否足够？Bootstrap 稳定性分析是否充分？
   - Cross-model transfer 仅限 continuation mode——声明范围是否过大？
   - Filtering 实验在 83% 污染下进行——在现实比例（≤50%）下效果是否消失？

3. **统计实践**:
   - Permutation test + Bonferroni 校正是否恰当？
   - Bootstrap CI 的计算方法和置信水平是否合理？
   - 边界情况（marginal cases）的处理是否诚实？
   - GroupKFold cross-validation 设计是否防止了数据泄漏？

4. **可复现性**:
   - 超参数是否完整报告？
   - 数据集描述是否足够？
   - 代码可用性声明是否存在？

请完整阅读论文（包括 appendix），给出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Overall Assessment (评分+置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2295 · 2026-05-25T21:16:47.640821+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2296 · 2026-05-25T21:16:47.741622+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2297 · 2026-05-25T21:16:51.915022+00:00_

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
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 2298 · 2026-05-25T21:16:52.969145+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/submitted.pdf",
  "pages": "1-10",
  "project": "gen-depth-contamination",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/submitted.pdf",
    "pages": "1-10",
    "project": "gen-depth-contamination",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2299 · 2026-05-25T21:17:00.882390+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Guidelines

All papers recommended for Findings or main conference are expected to be sound and reproducible. Area Chairs should mostly follow the soundness assessment of the reviewers when they are in agreement, and they can weigh in when ther
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8967
}
```

</details>

---


### Tool result

_source line 2300 · 2026-05-25T21:17:02.393991+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 449.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 551.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 623.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 417.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p9.png\", \"width\": 1
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9424
}
```

</details>

---


### Tool call

_source line 2301 · 2026-05-25T21:17:08.365812+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 2302 · 2026-05-25T21:17:08.921427+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 2303 · 2026-05-25T21:17:09.775672+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool result

_source line 2304 · 2026-05-25T21:17:09.776518+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 2305 · 2026-05-25T21:17:09.827039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 2306 · 2026-05-25T21:17:10.329329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 2307 · 2026-05-25T21:17:10.732599+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 2308 · 2026-05-25T21:17:10.733024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 2309 · 2026-05-25T21:17:11.336652+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool result

_source line 2310 · 2026-05-25T21:17:11.639176+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 2311 · 2026-05-25T21:17:18.536458+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 2312 · 2026-05-25T21:17:18.940444+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 2313 · 2026-05-25T21:17:18.991594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 2314 · 2026-05-25T21:17:19.895585+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 2315 · 2026-05-25T21:17:19.946938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 2316 · 2026-05-25T21:17:20.401956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 2317 · 2026-05-25T21:17:20.706650+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 759
}
```

</details>

---


### Tool call

_source line 2318 · 2026-05-25T21:17:20.707119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 2319 · 2026-05-25T21:17:21.362683+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool result

_source line 2320 · 2026-05-25T21:17:21.664671+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 2321 · 2026-05-25T21:17:29.345634+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/submitted.pdf",
  "pages": "11-18",
  "project": "gen-depth-contamination",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/submitted.pdf",
    "pages": "11-18",
    "project": "gen-depth-contamination",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2322 · 2026-05-25T21:17:30.554892+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 276.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 354.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 292.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 363.0}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.2}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.8}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.9}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 388.2}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/art
…[truncated 75 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1209
}
```

</details>

---


### Tool call

_source line 2323 · 2026-05-25T21:17:40.902980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 2324 · 2026-05-25T21:17:41.710347+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 2325 · 2026-05-25T21:17:41.710759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 2326 · 2026-05-25T21:17:42.170174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 2327 · 2026-05-25T21:17:42.676089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 2328 · 2026-05-25T21:17:43.086264+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1375
}
```

</details>

---


### Tool call

_source line 2329 · 2026-05-25T21:17:43.086870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 2330 · 2026-05-25T21:17:43.999294+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1829
}
```

</details>

---


### Tool result

_source line 2331 · 2026-05-25T21:17:44.355437+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1679
}
```

</details>

---


### Tool result

_source line 2332 · 2026-05-25T21:17:45.212904+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2126
}
```

</details>

---


### Tool call

_source line 2333 · 2026-05-25T21:17:51.684906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 2334 · 2026-05-25T21:17:52.138495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 2335 · 2026-05-25T21:17:52.746106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_30/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 2336 · 2026-05-25T21:17:54.161114+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2476
}
```

</details>

---


### Tool result

_source line 2337 · 2026-05-25T21:17:55.991591+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3853
}
```

</details>

---


### Tool result

_source line 2338 · 2026-05-25T21:17:56.046533+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3300
}
```

</details>

---


### Tool call

_source line 2339 · 2026-05-25T21:18:03.836419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2340 · 2026-05-25T21:18:03.938697+00:00_

1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{colortbl}
15	\usepackage{multirow}
16	\usepackage{enumitem}
17	\usepackage{subcaption}
18	\usepackage{placeins}
19	\usepackage{float}
20	
21	\newcommand{\Kstar}{{K^*}}
22	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
23	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
24	\newcommand{\auc}{\text{AUC}}
25	\newcommand{\jsd}{\text{JSD}}
26	
27	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
28	
29	\author{Anonymous}
30	
31	\begin{document}
32	\maketitle
33	
34	% === Abstract ===
35	\begin{abstract}
36	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
37	We measure a lower bound on the generational discrimination boundary, $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable).
38	Under prompt-chain generation across 10 model configurations (6 architecture families, 1B--8B), 4 source domains, and 4 decoding strategies, $\Kempirical \leq 2$ for all web text configurations ($\theta{=}0.60$); structured academic text (arXiv) reaches $\Kempirical{=}3$ across four independent architecture families.
39	Beyond two generation passes, web text becomes statistically indistinguishable across deeper generations, a \emph{one-wash laundering} effect that concentrates the dominant exploitable signal at the human-vs.-machine boundary.
40	Across continuation-mode generators, generator-agnostic statistical features enable 80--92\% cross-model transfer with scorer-invariant feature rankings ($\rho > 0.90$); depth estimation on corpora from unknown gen
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2341 · 2026-05-25T21:18:10.014993+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2342 · 2026-05-25T21:18:10.065650+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_pairwise_significance.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_filtering_main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_alpha_sweep.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2343 · 2026-05-25T21:18:14.832106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2344 · 2026-05-25T21:18:15.284191+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Corpus-level statistical features are fed to the OBD-LightGBM classifier for depth prediction. (Simplified notation; see Eq.~\ref{eq:kstar} for the formal $\Kempirical$ definition.)}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: mutual information with the seed text degrades monotonically.
17	Together with Markov chain convergence, this motivates the existence of a finite discrimination boundary where $\auc_{k-1,k}$ falls below a decision threshold, though AUC and mutual information are not formally equivalent; the actual saturation depth must therefore be measured empirically.
18	Pairwise AUC generally decreases with depth but may exhibit noise-level reversals (e.g., Pythia-1.4B 3v4 $\auc = 0.505$ vs.\ 4v5 $= 0.508$, a difference within bootstrap CI; Table~\ref{tab:kstar_ci_extended}), reinforcing that $\Kempirical$ is a measured quantity rather than a theoretical prediction.
19	
20	We define the operational lower bound:
21	{\small
22	\begin{equation}
23	  \Kempirical = \max\bigl\{k \!\geq\! 1 : \auc_{j-1,j} > \theta,\;\forall\, 1 \!\leq\! j \!\leq\! k\bigr\},
24	  \label{eq:kstar}
25	\end{equation}
26	}
27	which requires all pairs up to depth $k$ to exceed the threshold (the $\forall j$ constraint is naturally satisfied because $\auc_{k-1,k}$ decreases monotonically above $\thet
…[truncated 6051 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2345 · 2026-05-25T21:18:15.284707+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
  }
}
```

</details>

---


### Tool result

_source line 2346 · 2026-05-25T21:18:15.786819+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate on ten configurations spanning six families: Pythia-1.4B/6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite/continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B.
5	Unless noted, all experiments use the OBD-LightGBM classifier with 15 features (Section~\ref{sec:method}), 5{,}000 C4 texts per depth level (depths 0--5).
6	
7	%% ====================================================================
8	\subsection{The Discrimination Boundary}
9	\label{sec:kstar_boundary}
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
14	\caption{Pairwise $\auc$ decay across adjacent depth pairs (0v1, 1v2, \ldots, 4v5) for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\% CIs. Horizontal dashed line: $\theta = 0.60$.}
15	\label{fig:auc_decay}
16	\end{figure}
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
22	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
23	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
24	\label{tab:kstar_ci}
25	\resizebox{\textwidth}{!}{%
26	\begin{tabular}{lcccccccccc}
27	\toprule
28	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
29	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
30	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
31	\midrule
32	0v1 & .9956 & & .9722 & & .9861 & & .9971 & & .9644 & [.961,\,.967] \\
33	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6074 & [.598,\,.617]\rlap{$^*$} & .5001 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$
…[truncated 15516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2347 · 2026-05-25T21:18:15.837448+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
  }
}
```

</details>

---


### Tool result

_source line 2348 · 2026-05-25T21:18:15.888597+00:00_

1	\section{Consistency Check: $\Kstar$-Guided Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical = 2$ predicts that binary curation should suffice; we validate this under extreme contamination (${\sim}$83\% synthetic), not as an independent contribution (at realistic rates $\leq$50\%, differences $<$0.3\,pp; Appendix~\ref{sec:dose_response}).
5	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} (15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal}, and (vi)~\textbf{DSIR}~\citep{xie2023dsir}, fine-tuning Qwen2.5-1.5B-Instruct via LoRA (rank~8) for 3 epochs across 5 seeds~\cite{shumailov2024collapse, dohmatob2024model}.
6	
7	\begin{table}[t]
8	\centering
9	\small
10	\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Figure~\ref{fig:filtering_strategies}.}
11	\label{tab:tab_filtering_main}
12	\resizebox{\columnwidth}{!}{\input{tables/tab_filtering_main}}
13	\end{table}
14	
15	Binary-ours reduces the MMLU gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives; Table~\ref{tab:tab_filtering_main}, \ref{tab:pairwise_significance}).
16	The ordering is interpretable through $\Kempirical$: binary filtering exploits the strongest boundary (0v1), while graduated strategies assign weights based on near-random classifier outputs for depths $\geq 2$, injecting noise rather than useful signal.
17	Graduated filtering converges toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag ($p_{\text{corr}} = 1.00$) but remains worse on MMLU ($p_{\text{corr}} = 0.011$); DSIR is indistinguishable from no-filter
…[truncated 290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2349 · 2026-05-25T21:18:32.598999+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2350 · 2026-05-25T21:18:33.001444+00:00_

1	\appendix
2	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
3	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
4	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
5	\setlength{\abovecaptionskip}{4pt}
6	\setlength{\belowcaptionskip}{2pt}
7	\section{Supplementary Materials}
8	\label{sec:appendix}
9	
10	This appendix provides supplementary figures, detailed experimental tables, dataset statistics, and complete feature descriptions referenced in the main text.
11	
12	\paragraph{Feature ranking and cross-model consistency.}
13	Table~\ref{tab:top_features} reports per-model single-feature AUC rankings.
14	Surprisal derivative features (\texttt{surp\_d1\_std}, \texttt{surp\_d2\_std}) consistently rank among the top three across all continuation-mode models (Pythia, OLMo, Qwen-cont), with pairwise Spearman $\rho \geq 0.85$.
15	The rewrite-mode model (Qwen-rw) diverges by placing \texttt{freq\_entropy} first; this reflects a distributional shift that is lexical rather than surprisal-driven.
16	This scorer-invariant ranking supports the use of a fixed 15-dimensional feature set across generators without per-model feature selection.
17	
18	%%% Feature ranking table (moved from main text)
19	\begin{table}[!htbp]
20	\centering
21	\small
22	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
23	\label{tab:top_features}
24	\resizebox{\columnwidth}{!}{%
25	\begin{tabular}{cllll}
26	\toprule
27	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
28	\midrule
29	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
30	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
31	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\te
…[truncated 23638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2351 · 2026-05-25T21:18:33.002181+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
  }
}
```

</details>

---


### Tool result

_source line 2352 · 2026-05-25T21:18:33.254697+00:00_

1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	
6	The DPI guarantees a finite $\Ktheory$; for general web text, $\Kempirical \leq 2$ across all 10 configurations (1B--8B, 6 families), while structured domains (arXiv) yield $\Kempirical{=}3$, aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6862, 0.7037]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--92\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), which enables single-classifier deployment across generators.
12	Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
13	Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 89--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
14	
15	\begin{table}[h]
16	\centering
17	\caption{Cross-scorer validation. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1. OLMo arXiv cross-scorer confirms $\Kempirical{=}1$ ($p{=}0.510$, n.s.).}
18	\label{tab:crossscorer}
19	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
20	\end{table}
21	
22	\begin{table}[h]
23	\centering
24	\small
25	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values. DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs). Scorer is statistically significant but explains modest variance ($\eta^2_p{=}.192$) relative to Depth-Pair ($\eta^2_p{=}.998$), which supports near-scorer-independence of depth discrimination.}
26
…[truncated 24362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 2353 · 2026-05-25T21:18:43.640831+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2354 · 2026-05-25T21:18:43.641196+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\paragraph{One-wash laundering (web text).}
11	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
12	OBD achieves 94\% depth-0 recall but only 15--23\% for depths $\geq$2; frontier LLMs show 8--38\% ($p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}; per-depth breakdown in Table~\ref{tab:s3c_perdepth}), which supports a data-intrinsic interpretation.
13	Unlike model collapse~\cite{shumailov2024collapse}, one-wash laundering describes erasure of statistical fingerprints; quality may degrade further after features become indistinguishable.
14	
15	\begin{figure}[t]
16	\centering
17	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
18	\caption{MMLU accuracy under six filtering strategies (5 seeds, $\pm$1 std). Binary $\Kstar$ filtering (red) minimizes degradation; graduated weighting converges toward binary as $\alpha$ increases. Dashed line: no-filter baseline.}
19	\label{fig:filtering_strategies}
20	\end{figure}
21	
22	\paragraph{Boundary cases and representation dependence.}
23	Under Bonferroni correction (Table~\ref{tab:bonferroni_ci}), three of six $\Kempirical{=}2$ cases become marginal (CI lower 0.593--0.599), though $\Kempirical \leq 2$ holds across $\theta \in [0.59, 0.61]$ (Figure~\ref{fig:kstar_theta}).
24	$\Kempirical$ is representation-dependent: neural probes yield $\Kempirical^{\text{neural}} \in \{1,2,3\}$ (Table~\ref{tab:neural_probe_crossmodel}); a DeBERTa probe extends to $\Kempirical{=}4$ on arXiv (Table~\ref{tab:deberta_vs_obd}).
25	
26	\paragraph{Domain dependence and scope.}
27	arXiv yields $\Kempirical{=}3$ across four families (Figure~\ref{fig:jsd_decay}), drive
…[truncated 268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2355 · 2026-05-25T21:18:43.791961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2356 · 2026-05-25T21:18:43.842541+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across four lines of work: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}); membership inference~\cite{zawalski2026codec} addresses a different question; the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
11	No existing method estimates how many rounds of recursive generation a text has undergone.
12	
13	The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
14	We empirically measure a lower bound $\Kempirical$ on the discrimination boundary (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistic
…[truncated 1659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2357 · 2026-05-25T21:18:50.025462+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form 2025 2026 soundness excitement overall assessment scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form 2025 2026 soundness excitement overall assessment scoring dimensions"
  }
}
```

</details>

---


### Tool result

_source line 2358 · 2026-05-25T21:18:57.912066+00:00_

Web search results for query: "ACL Rolling Review review form 2025 2026 soundness excitement overall assessment scoring dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) review form for 2025-2026:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness
Soundness assesses whether the paper is sufficiently sound and thorough, clearly states scie
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7886
}
```

</details>

---


### Tool call

_source line 2359 · 2026-05-25T21:19:02.027573+00:00_

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
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
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

_source line 2360 · 2026-05-25T21:19:02.128494+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2361 · 2026-05-25T21:19:09.358003+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form scoring dimensions, their scale (1-5 or otherwise), and the description of each score level. I need the exact scoring criteria for: soundness, excitement, overall assessment, confidence, and any other dimensions. List every score option with its label."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form scoring dimensions, their scale (1-5 or otherwise), and the description of each score level. I need the exact scoring criteria for: soundness, excitement, overall assessment, confidence, and any other dimensions. List every score option with its label."
  }
}
```

</details>

---


### Tool result

_source line 2362 · 2026-05-25T21:19:19.542286+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
Scale: 1-5

- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
Scale: 1-5 (with half-point options: 4.5, 3.5, 2.5, 1.5)

- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
Scale: 1-5 (with half-point options: 4.5, 3.5, 2.5, 1.5)

- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

## Overall Assessment
Scale: 1-5 (with half-point options)

- **5**: Consider for Award (top 2.5% papers)
- **4.5**: Borderline Award
- **4**: Conference acceptance recommendation
- **3.5**: Borderline Conference
- **3**: Findings of the ACL acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## Reproducibility
Scale: 1-5

- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty
- **2**: Very difficult to reproduce
- **1**: Cannot reproduce re
…[truncated 459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 10184
}
```

</details>

---


### Tool call

_source line 2363 · 2026-05-25T21:22:22.521166+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what should reviewers focus on, what are the expectations for soundness and excitement scores, and any specific instructions about how to evaluate papers. Include any guidance about how soundness scores must be justified."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines: what should reviewers focus on, what are the expectations for soundness and excitement scores, and any specific instructions about how to evaluate papers. Include any guidance about how soundness scores must be justified."
  }
}
```

</details>

---


### Tool result

_source line 2364 · 2026-05-25T21:22:28.958123+00:00_

# Key ARR Reviewer Guidelines

## Core Focus Areas

Reviewers should concentrate on four main tasks:

1. **Allocate adequate time** for both reviewing and discussion periods
2. **Check assignments** for expertise fit and conflicts of interest
3. **Write substantive reviews** with specific feedback
4. **Engage with author responses** and update assessments accordingly

## Soundness and Excitement Scores

The guidance emphasizes critical distinctions between score types:

**Soundness scores** must be rigorously justified. As stated: "The soundness scores must be justified by the text of the review. If you give a low soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it."

**Excitement scores** operate independently from soundness, reflecting personal interest rather than technical quality. A paper can be technically sound yet personally unexciting, or vice versa.

**Overall assessment** combines soundness, excitement, novelty, and potential impact—the composite recommendation for venue placement.

## Writing Strong Reviews

Key expectations include:

- **Be specific** with concrete examples rather than vague criticisms
- **Avoid common reviewer biases** (listing 17 problematic heuristics like dismissing "surprising" results or demanding unnecessary experiments)
- **Maintain professional tone**, treating authors with respect and constructive intent
- **Read papers twice**: initial skim to adjust expectations, then in-depth evaluation

The guidelines stress that low scores require transparent justification to avoid unconscious bias influencing recommendations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6436
}
```

</details>

---


### Tool call

_source line 2365 · 2026-05-25T21:24:34.969067+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告\n\n**论文**: Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审查侧重**: 方法严谨性 + 实验设计 + 统计有效性\n\n---\n\n## Summary\n\n本文提出\"生成深度估计\"这一新问题：衡量文本经历了多少轮递归 LLM 生成。定义 K*_empirical 为相邻代际仍可区分的最大深度（AUC > θ=0.60），使用 15 维统计特征 + OBD-LightGBM 分类器。核心发现：对一般网络文本 K*_empirical ≤ 2（10 个模型配置、6 个架构族），arXiv 结构化文本 K*_empirical = 3。跨模型迁移保持 80-92% 准确率（continuation mode）。在 ~83% 污染下，K*_empirical 正确预测二元过滤优于渐进式策略。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 问题定义新颖、实验覆盖面广、统计实践较规范，但核心发现 K*=2 的统计显著性在 Bonferroni 校正下仅半数成立，Qwen 过度代表和 claim 范围过大拉低了可信度。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论总体合理，统计控制（permutation + Bonferroni + GroupKFold）规范；但 DPI→AUC 推理链有逻辑缺口，6 个 K*=2 配置中 3 个在 Bonferroni 校正下 marginal，核心 claim 的统计基础有脆弱性 |\n| Excitement | 3.5/5 | \"生成深度\"是一个全新的研究维度，\"one-wash laundering\" 发现对 model collapse 和数据治理领域有实际意义；但 K*≤2 本质上是个 negative result——说明深度估计在二元检测之上提供的增量有限 |\n| Reproducibility | 4/5 | 超参数完整报告（Table S6），特征定义齐全（Table S5），匿名代码/数据链接已提供，数据集构造描述充分 |\n| Confidence | 4/5 | 仔细阅读全文及全部附录，熟悉 machine-generated text detection 和 model collapse 相关工作 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] K*_empirical=2 的统计显著性在 Bonferroni 校正下仅半数成立\n\n- 具体位置：Section 4.1, Table 2, Appendix B.10 (Table 27)\n- 问题：论文声称\"K*_empirical=2 for 6/10 configurations\"（Abstract, Section 4.1），但 Table 27 (Bonferroni-corrected 99.5% CI) 显示 6 个 K*=2 配置中仅 3 个（Qwen-rw, Qwen-base, Qwen-7B）的 CI 下界超过 θ=0.60。Pythia-1.4B (0.593), Qwen-cont (0.598), LLaMA-8B (0.599) 三个配置的 CI 下界均低于 θ。这意味着在多重比较校正后，\"K*=2\"对这三个配置而言统计不显著。\n- 为什么影响接收：这是论文的核心 claim。如果仅 3/6 配置统计显著，且这 3 个全是 Qwen 变体，那 \"K*≤2 universally\" 的泛化性大幅削弱。论文在 Section 4.1 确实提及了这一点，但措辞是\"marginal\"而非直接承认不显著，且 Abstract/Introduction 的表述未反映这一限制。\n- 建议修改方向：(1) Abstract 和 Introduction 中将 \"6/10\" 改为按 family 去重的表述（如\"3 of 6 independent families achieve K*=2, with 3 additional Qwen-family variants\"）；(2) 明确区分\"statistically significant K*=2\"（3 configs）和\"point-estimate K*=2\"（6 configs）；(3) 考虑以 per-family 分析作为主要结论而非 per-configuration 计数。\n\n**N2** [critical] Qwen 过度代表导致 headline 数字膨胀\n\n- 具体位置：Table 1 (Section 3.3), Table 2 (Section 4.1), Abstract\n- 问题：10 个配置中 Qwen 占 4 个（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B），其他 5 个 family 各仅 1-2 个配置。6 个 K*=2 配置中 4 个是 Qwen 变体。按 family 去重：仅 3 个独立 family（Qwen, Pythia, LLaMA）在至少一个配置中达到 K*=2，而 Pythia 和 LLaMA 的 K*=2 在 Bonferroni 校正下均为 marginal。实际上只有 Qwen family 稳健地达到 K*=2。\n- 为什么影响接收：如果核心结论主要由一个 model family 驱动，泛化性主张不成立。Reviewer 和 reader 读到 \"6/10 configurations, 6 architecture families\" 时会认为这是跨 family 的 robust 结论，但实际不是。\n- 建议修改方向：(1) 主表和 Abstract 应以 per-family 结果为主体（如：\"K*=2 robustly holds for the Qwen family; Pythia and LLaMA reach K*=2 but with marginal significance; OLMo, Gemma, Mistral yield K*=1\"）；(2) 分析 Qwen 为何 consistently 产生更高 AUC——是 Qwen 的生成文本确实保留更多世代信号，还是存在 Qwen-specific artifact（Section 4.4 neural probe 已暗示后者的可能）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] DPI→AUC 单调递减的推理链有逻辑缺口\n\n- 具体位置：Section 3.1 (method.tex lines 16-18, 30)\n- 问题：论文用 DPI 论证 I(X; Y_1) ≥ I(X; Y_2) ≥ ...（seed 与各代的 MI 单调递减），然后以此 \"motivate\" AUC_{k-1,k} 随 k 递减的经验观察。但 DPI 关于 I(X; Y_k) 的单调性并不蕴含 I(Y_{k-1}; Y_k)（相邻代际的 MI）的单调性。论文衡量的是相邻代际的可区分性 AUC_{k-1,k}，这与 I(X; Y_k) 是不同的量。对齐次 Markov chain，I(Y_{k-1}; Y_k) 的行为取决于 mixing rate / convergence，非 DPI 直接推导。\n- 建议：明确说明 DPI 只保证 seed-to-generation MI 的单调性，而非 adjacent-pair discriminability。可引用 Markov chain mixing time 文献补充理论动机。当前 \"The DPI motivates the empirical observation\" 的措辞模糊了理论保证与经验观察的边界。\n\n**W2** [warning] θ=0.60 阈值的后验性问题\n\n- 具体位置：Section 3.1 (method.tex lines 34-40), Figure 3\n- 问题：θ=0.60 的选择基于 1v2 AUC cluster (0.607-0.696) 与 2v3 cluster (~0.54-0.59) 之间的 gap。这本质上是 post-hoc 的——先观察了 AUC 分布，再选择 θ 落在 gap 中。论文提供了两个独立 justification：(1) permutation null 95th percentile < 0.55, (2) sensitivity surface (Figure 3)。这些有帮助，但更理想的做法是基于 permutation null distribution 直接推导 θ（如取 null 的 99th percentile 作为 θ），或在独立 hold-out 配置上验证 θ。\n- 建议：(1) 承认 θ 的选择有 post-hoc 成分；(2) 报告基于 permutation null 直接推导的 θ 值（如 99th percentile of null），并与 θ=0.60 比较；(3) 或者在 held-out 配置（如 LLaMA, Mistral）上验证 θ=0.60 的有效性。\n\n**W3** [warning] Cross-model transfer claim 范围过大\n\n- 具体位置：Abstract (\"depth estimation on corpora from unknown generators requires no retraining\"), Section 4.2\n- 问题：Abstract 声称 \"depth estimation on corpora from unknown generators requires no retraining\"，但 (a) 迁移实验仅覆盖 continuation mode，rewrite mode 迁移仅 61-63%；(b) 迁移在 K*=1 的模型（OLMo, Gemma, Mistral）上无意义——因为这些模型本身只有 0v1 信号；(c) 有效的迁移仅在 Pythia↔OLMo↔Qwen-cont 三者之间验证。Abstract 的 claim 远超实际验证范围。\n- 建议：Abstract 中限定为 \"across continuation-mode generators with K*≥2\"，避免暗示 universal applicability。\n\n**W4** [warning] OBD vs. ordinal logistic regression 对比的公平性\n\n- 具体位置：Section 3.2 (method.tex line 72)\n- 问题：论文报告 OBD pairwise AUC 均值 0.6099 vs. ordinal logistic regression 0.4883。AUC < 0.50 意味着 ordinal regression 在部分 depth pair 上系统性反向预测，这暗示模型拟合可能有问题（如特征标准化、超参数选择）。论文解释为 \"collapsing predictions toward central depths\"，但 collapsing 应产生 AUC ≈ 0.50（随机水平），而非 < 0.50。均值 0.4883 < 0.50 需要更详细的解释——是哪些 depth pair 反转了？是否调参过？\n- 建议：报告 ordinal regression 各 depth pair 的 AUC 分解，解释 <0.50 的具体原因，并说明是否对 ordinal regression 做了合理的超参数调优以确保对比公平。\n\n**W5** [warning] Filtering 实验的实际意义有限\n\n- 具体位置：Section 5, Appendix B.8 (Table 25)\n- 问题：主实验在 ~83% 污染下进行，binary-ours 将 MMLU 降幅从 -1.53pp 减至 -0.77pp。但 Appendix B.8 显示在现实污染比例 (≤50%) 下，所有策略差异 <0.3pp，且所有策略下 MMLU 均高于 base model（无降幅可恢复）。这意味着 K*-guided filtering 仅在极端场景下有实际效果。论文将此定位为\"consistency check\"，但 Abstract 和 contributions 中的表述重量级很高，可能误导读者认为这是一个 practical contribution。\n- 建议：(1) Abstract 中更明确地限定 filtering 结论的适用范围；(2) 在 Section 5 开头直接说明 ≤50% 下效果消失，而非放在附录。\n\n**W6** [warning] Bootstrap CI 方法不一致\n\n- 具体位置：Table 27 (Appendix B.10) vs. Table 28 (Appendix B.11)\n- 问题：Table 27 使用 normal-approximation bootstrap CI（AUC ± 2.807 × σ_boot），Table 28 脚注提到 \"percentile\" CI。对于 AUC 接近边界（0.50-0.60 区间）的情形，bootstrap 分布可能偏斜，normal approximation 可能不准确。论文未统一说明全文使用的 CI 计算方法。\n- 建议：明确全文 CI 方法（建议统一用 percentile bootstrap），并对 boundary pair AUC 检查 bootstrap 分布的偏斜程度。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Eq.1 定义 K*_empirical = max{k ≥ 1 : ...}，当集合为空时（即 AUC_{0,1} < θ）定义未明确。虽然实验中所有 0v1 AUC > 0.92 故不会触发，但形式定义应处理此边界情况（如约定 K*_empirical = 0）。\n- **M2**: \"One-wash laundering\" 术语隐含故意洗白的含义，但论文描述的是自然发生的信息丢失现象。可考虑在首次使用时解释此术语为隐喻而非字面含义。\n- **M3**: Table 2 中 OLMo 的 1v2 AUC (0.5001) 和 2v3 AUC (0.4973) 以及 3v4 AUC (0.5034) 呈非单调——脚注 § 已标注。这个案例本身就说明 DPI→AUC 单调的论证不成立（回应 W1）。\n- **M4**: 论文提到 Pythia-6.9B 的 4v5 AUC 为 \"---\" (Table S2b)，标注 \"K*=1; 4v5 not required for boundary determination\"。但其 1v2 AUC = 0.5955 低于 θ=0.60，所以确实是 K*=1，不影响结论。只是标注不够直观。\n- **M5**: Abstract 中 \"structured academic text (arXiv) reaches K*_empirical=3 across four independent architecture families\" 应注明 OLMo 是例外（K*=1 across all domains）。否则读者可能以为全部 5 个测试 family 都是 K*=3。\n\n---\n\n## Questions for Authors\n\n1. 3 个 Bonferroni-marginal 的 K*=2 配置（Pythia-1.4B, Qwen-cont, LLaMA-8B）的 CI 下界分别为 0.593, 0.598, 0.599。如果采用 0.60 作为 CI 下界的判定标准（而非点估计），论文的核心结论会如何修改？\n2. Qwen family 在 K*=2 中的 dominant 表现是否可能源于 Qwen 架构/训练数据的特殊性而非普遍现象？Neural probe (Section 4.4) 中 Qwen 达到 K*_neural=3 而 Pythia 仅 K*_neural=2，是否暗示 Qwen 生成文本有特殊的 \"self-familiarity\" 信号？\n3. Ordinal logistic regression 的 pairwise AUC 均值 0.4883 低于随机水平(0.50)，能否提供各 depth pair 的分解？是否对 ordinal regression 做了超参数搜索？\n4. Cross-model transfer (Section 4.2) 仅覆盖 continuation mode。对于实际部署场景（互联网文本可能由 instruction-tuned 模型的 rewrite mode 生成），迁移失败（61-63%）是否限制了整个方法的实用性？\n\n---\n\n## 主要优势\n\n- **S1**: 问题定义新颖且重要——\"生成深度\"是一个此前未被研究的维度，对 model collapse、数据治理和 synthetic text detection 领域有明确意义。\n- **S2**: 实验覆盖面广——10 个模型配置、6 个架构族、4 个域、4 个解码策略，附带充分的消融实验（长度、seed、scorer、样本量）。\n- **S3**: 统计实践规范——permutation test + Bonferroni 校正、bootstrap CI、GroupKFold 防泄漏、self-BLEU 折内计算，多处主动标注 marginal cases。\n- **S4**: DeBERTa 上界实验（Appendix B.14）提供了有用的对比：15D 特征给出 lower bound，表征模型可将 K* 推至 4（arXiv），量化了 generator-agnostic 特征的代价。\n- **S5**: 对 retrain-chain vs. prompt-chain 的区分（Appendix B.7）澄清了本工作的定位：prompt-chain K* 度量的是文本固有的信息退化，不含训练循环效应。\n- **S6**: 可复现性好——超参数、特征定义、数据集构造、代码链接均已提供。",
  "reviewer_id": "1",
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告\n\n**论文**: Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审查侧重**: 方法严谨性 + 实验设计 + 统计有效性\n\n---\n\n## Summary\n\n本文提出\"生成深度估计\"这一新问题：衡量文本经历了多少轮递归 LLM 生成。定义 K*_empirical 为相邻代际仍可区分的最大深度（AUC > θ=0.60），使用 15 维统计特征 + OBD-LightGBM 分类器。核心发现：对一般网络文本 K*_empirical ≤ 2（10 个模型配置、6 个架构族），arXiv 结构化文本 K*_empirical = 3。跨模型迁移保持 80-92% 准确率（continuation mode）。在 ~83% 污染下，K*_empirical 正确预测二元过滤优于渐进式策略。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 问题定义新颖、实验覆盖面广、统计实践较规范，但核心发现 K*=2 的统计显著性在 Bonferroni 校正下仅半数成立，Qwen 过度代表和 claim 范围过大拉低了可信度。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论总体合理，统计控制（permutation + Bonferroni + GroupKFold）规范；但 DPI→AUC 推理链有逻辑缺口，6 个 K*=2 配置中 3 个在 Bonferroni 校正下 marginal，核心 claim 的统计基础有脆弱性 |\n| Excitement | 3.5/5 | \"生成深度\"是一个全新的研究维度，\"one-wash laundering\" 发现对 model collapse 和数据治理领域有实际意义；但 K*≤2 本质上是个 negative result——说明深度估计在二元检测之上提供的增量有限 |\n| Reproducibility | 4/5 | 超参数完整报告（Table S6），特征定义齐全（Table S5），匿名代码/数据链接已提供，数据集构造描述充分 |\n| Confidence | 4/5 | 仔细阅读全文及全部附录，熟悉 machine-generated text detection 和 model collapse 相关工作 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] K*_empirical=2 的统计显著性在 Bonferroni 校正下仅半数成立\n\n- 具体位置：Section 4.1, Table 2, Appendix B.10 (Table 27)\n- 问题：论文声称\"K*_empirical=2 for 6/10 configurations\"（Abstract, Section 4.1），但 Table 27 (Bonferroni-corrected 99.5% CI) 显示 6 个 K*=2 配置中仅 3 个（Qwen-rw, Qwen-base, Qwen-7B）的 CI 下界超过 θ=0.60。Pythia-1.4B (0.593), Qwen-cont (0.598), LLaMA-8B (0.599) 三个配置的 CI 下界均低于 θ。这意味着在多重比较校正后，\"K*=2\"对这三个配置而言统计不显著。\n- 为什么影响接收：这是论文的核心 claim。如果仅 3/6 配置统计显著，且这 3 个全是 Qwen 变体，那 \"K*≤2 universally\" 的泛化性大幅削弱。论文在 Section 4.1 确实提及了这一点，但措辞是\"marginal\"而非直接承认不显著，且 Abstract/Introduction 的表述未反映这一限制。\n- 建议修改方向：(1) Abstract 和 Introduction 中将 \"6/10\" 改为按 family 去重的表述（如\"3 of 6 independent families achieve K*=2, with 3 additional Qwen-family variants\"）；(2) 明确区分\"statistically significant K*=2\"（3 configs）和\"point-estimate K*=2\"（6 configs）；(3) 考虑以 per-family 分析作为主要结论而非 per-configuration 计数。\n\n**N2** [critical] Qwen 过度代表导致 headline 数字膨胀\n\n- 具体位置：Table 1 (Section 3.3), Table 2 (Section 4.1), Abstract\n- 问题：10 个配置中 Qwen 占 4 个（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B），其他 5 个 family 各仅 1-2 个配置。6 个 K*=2 配置中 4 个是 Qwen 变体。按 family 去重：仅 3 个独立 family（Qwen, Pythia, LLaMA）在至少一个配置中达到 K*=2，而 Pythia 和 LLaMA 的 K*=2 在 Bonferroni 校正下均为 marginal。实际上只有 Qwen family 稳健地达到 K*=2。\n- 为什么影响接收：如果核心结论主要由一个 model family 驱动，泛化性主张不成立。Reviewer 和 reader 读到 \"6/10 configurations, 6 architecture families\" 时会认为这是跨 family 的 robust 结论，但实际不是。\n- 建议修改方向：(1) 主表和 Abstract 应以 per-family 结果为主体（如：\"K*=2 robustly holds for the Qwen family; Pythia and LLaMA reach K*=2 but with marginal significance; OLMo, Gemma, Mistral yield K*=1\"）；(2) 分析 Qwen 为何 consistently 产生更高 AUC——是 Qwen 的生成文本确实保留更多世代信号，还是存在 Qwen-specific artifact（Section 4.4 neural probe 已暗示后者的可能）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] DPI→AUC 单调递减的推理链有逻辑缺口\n\n- 具体位置：Section 3.1 (method.tex lines 16-18, 30)\n- 问题：论文用 DPI 论证 I(X; Y_1) ≥ I(X; Y_2) ≥ ...（seed 与各代的 MI 单调递减），然后以此 \"motivate\" AUC_{k-1,k} 随 k 递减的经验观察。但 DPI 关于 I(X; Y_k) 的单调性并不蕴含 I(Y_{k-1}; Y_k)（相邻代际的 MI）的单调性。论文衡量的是相邻代际的可区分性 AUC_{k-1,k}，这与 I(X; Y_k) 是不同的量。对齐次 Markov chain，I(Y_{k-1}; Y_k) 的行为取决于 mixing rate / convergence，非 DPI 直接推导。\n- 建议：明确说明 DPI 只保证 seed-to-generation MI 的单调性，而非 adjacent-pair discriminability。可引用 Markov chain mixing time 文献补充理论动机。当前 \"The DPI motivates the empirical observation\" 的措辞模糊了理论保证与经验观察的边界。\n\n**W2** [warning] θ=0.60 阈值的后验性问题\n\n- 具体位置：Section 3.1 (method.tex lines 34-40), Figure 3\n- 问题：θ=0.60 的选择基于 1v2 AUC cluster (0.607-0.696) 与 2v3 cluster (~0.54-0.59) 之间的 gap。这本质上是 post-hoc 的——先观察了 AUC 分布，再选择 θ 落在 gap 中。论文提供了两个独立 justification：(1) permutation null 95th percentile < 0.55, (2) sensitivity surface (Figure 3)。这些有帮助，但更理想的做法是基于 permutation null distribution 直接推导 θ（如取 null 的 99th percentile 作为 θ），或在独立 hold-out 配置上验证 θ。\n- 建议：(1) 承认 θ 的选择有 post-hoc 成分；(2) 报告基于 permutation null 直接推导的 θ 值（如 99th percentile of null），并与 θ=0.60 比较；(3) 或者在 held-out 配置（如 LLaMA, Mistral）上验证 θ=0.60 的有效性。\n\n**W3** [warning] Cross-model transfer claim 范围过大\n\n- 具体位置：Abstract (\"depth estimation on corpora from unknown generators requires no retraining\"), Section 4.2\n- 问题：Abstract 声称 \"depth estimation on corpora from unknown generators requires no retraining\"，但 (a) 迁移实验仅覆盖 continuation mode，rewrite mode 迁移仅 61-63%；(b) 迁移在 K*=1 的模型（OLMo, Gemma, Mistral）上无意义——因为这些模型本身只有 0v1 信号；(c) 有效的迁移仅在 Pythia↔OLMo↔Qwen-cont 三者之间验证。Abstract 的 claim 远超实际验证范围。\n- 建议：Abstract 中限定为 \"across continuation-mode generators with K*≥2\"，避免暗示 universal applicability。\n\n**W4** [warning] OBD vs. ordinal logistic regression 对比的公平性\n\n- 具体位置：Section 3.2 (method.tex line 72)\n- 问题：论文报告 OBD pairwise AUC 均值 0.6099 vs. ordinal logistic regression 0.4883。AUC < 0.50 意味着 ordinal regression 在部分 depth pair 上系统性反向预测，这暗示模型拟合可能有问题（如特征标准化、超参数选择）。论文解释为 \"collapsing predictions toward central depths\"，但 collapsing 应产生 AUC ≈ 0.50（随机水平），而非 < 0.50。均值 0.4883 < 0.50 需要更详细的解释——是哪些 depth pair 反转了？是否调参过？\n- 建议：报告 ordinal regression 各 depth pair 的 AUC 分解，解释 <0.50 的具体原因，并说明是否对 ordinal regression 做了合理的超参数调优以确保对比公平。\n\n**W5** [warning] Filtering 实验的实际意义有限\n\n- 具体位置：Section 5, Appendix B.8 (Table 25)\n- 问题：主实验在 ~83% 污染下进行，binary-ours 将 MMLU 降幅从 -1.53pp 减至 -0.77pp。但 Appendix B.8 显示在现实污染比例 (≤50%) 下，所有策略差异 <0.3pp，且所有策略下 MMLU 均高于 base model（无降幅可恢复）。这意味着 K*-guided filtering 仅在极端场景下有实际效果。论文将此定位为\"consistency check\"，但 Abstract 和 contributions 中的表述重量级很高，可能误导读者认为这是一个 practical contribution。\n- 建议：(1) Abstract 中更明确地限定 filtering 结论的适用范围；(2) 在 Section 5 开头直接说明 ≤50% 下效果消失，而非放在附录。\n\n**W6** [warning] Bootstrap CI 方法不一致\n\n- 具体位置：Table 27 (Appendix B.10) vs. Table 28 (Appendix B.11)\n- 问题：Table 27 使用 normal-approximation bootstrap CI（AUC ± 2.807 × σ_boot），Table 28 脚注提到 \"percentile\" CI。对于 AUC 接近边界（0.50-0.60 区间）的情形，bootstrap 分布可能偏斜，normal approximation 可能不准确。论文未统一说明全文使用的 CI 计算方法。\n- 建议：明确全文 CI 方法（建议统一用 percentile bootstrap），并对 boundary pair AUC 检查 bootstrap 分布的偏斜程度。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Eq.1 定义 K*_empirical = max{k ≥ 1 : ...}，当集合为空时（即 AUC_{0,1} < θ）定义未明确。虽然实验中所有 0v1 AUC > 0.92 故不会触发，但形式定义应处理此边界情况（如约定 K*_empirical = 0）。\n- **M2**: \"One-wash laundering\" 术语隐含故意洗白的含义，但论文描述的是自然发生的信息丢失现象。可考虑在首次使用时解释此术语为隐喻而非字面含义。\n- **M3**: Table 2 中 OLMo 的 1v2 AUC (0.5001) 和 2v3 AUC (0.4973) 以及 3v4 AUC (0.5034) 呈非单调——脚注 § 已标注。这个案例本身就说明 DPI→AUC 单调的论证不成立（回应 W1）。\n- **M4**: 论文提到 Pythia-6.9B 的 4v5 AUC 为 \"---\" (Table S2b)，标注 \"K*=1; 4v5 not required for boundary determination\"。但其 1v2 AUC = 0.5955 低于 θ=0.60，所以确实是 K*=1，不影响结论。只是标注不够直观。\n- **M5**: Abstract 中 \"structured academic text (arXiv) reaches K*_empirical=3 across four independent architecture families\" 应注明 OLMo 是例外（K*=1 across all domains）。否则读者可能以为全部 5 个测试 family 都是 K*=3。\n\n---\n\n## Questions for Authors\n\n1. 3 个 Bonferroni-marginal 的 K*=2 配置（Pythia-1.4B, Qwen-cont, LLaMA-8B）的 CI 下界分别为 0.593, 0.598, 0.599。如果采用 0.60 作为 CI 下界的判定标准（而非点估计），论文的核心结论会如何修改？\n2. Qwen family 在 K*=2 中的 dominant 表现是否可能源于 Qwen 架构/训练数据的特殊性而非普遍现象？Neural probe (Section 4.4) 中 Qwen 达到 K*_neural=3 而 Pythia 仅 K*_neural=2，是否暗示 Qwen 生成文本有特殊的 \"self-familiarity\" 信号？\n3. Ordinal logistic regression 的 pairwise AUC 均值 0.4883 低于随机水平(0.50)，能否提供各 depth pair 的分解？是否对 ordinal regression 做了超参数搜索？\n4. Cross-model transfer (Section 4.2) 仅覆盖 continuation mode。对于实际部署场景（互联网文本可能由 instruction-tuned 模型的 rewrite mode 生成），迁移失败（61-63%）是否限制了整个方法的实用性？\n\n---\n\n## 主要优势\n\n- **S1**: 问题定义新颖且重要——\"生成深度\"是一个此前未被研究的维度，对 model collapse、数据治理和 synthetic text detection 领域有明确意义。\n- **S2**: 实验覆盖面广——10 个模型配置、6 个架构族、4 个域、4 个解码策略，附带充分的消融实验（长度、seed、scorer、样本量）。\n- **S3**: 统计实践规范——permutation test + Bonferroni 校正、bootstrap CI、GroupKFold 防泄漏、self-BLEU 折内计算，多处主动标注 marginal cases。\n- **S4**: DeBERTa 上界实验（Appendix B.14）提供了有用的对比：15D 特征给出 lower bound，表征模型可将 K* 推至 4（arXiv），量化了 generator-agnostic 特征的代价。\n- **S5**: 对 retrain-chain vs. prompt-chain 的区分（Appendix B.7）澄清了本工作的定位：prompt-chain K* 度量的是文本固有的信息退化，不含训练循环效应。\n- **S6**: 可复现性好——超参数、特征定义、数据集构造、代码链接均已提供。",
    "reviewer_id": "1",
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2366 · 2026-05-25T21:24:38.640360+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3671
}
```

</details>

---


### Assistant

_source line 2367 · 2026-05-25T21:24:48.341091+00:00_

审稿报告已提交给 Review Director。

总结：

- **Overall 3.5 (Borderline Conference)**，Soundness 3.5，Excitement 3.5
- **2 个 Must-Fix**：(1) K\*=2 的 Bonferroni 显著性仅半数成立（3/6 配置 marginal），核心 claim 统计基础脆弱；(2) Qwen 占 K\*=2 配置的 4/6，按 family 去重后结论大幅弱化
- **6 个 Should-Fix**：DPI→AUC 推理缺口、θ 后验性、transfer claim 过宽、OBD vs ordinal regression 对比公平性、filtering 实际意义有限、bootstrap CI 方法不一致
- **主要优势**：问题定义新颖、实验覆盖全面、统计实践规范、可复现性好

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1"
}
```

</details>

---


## Round 60

## Round 60

4 recorded events


### User

_source line 2368 · 2026-05-25T21:33:17.006596+00:00_

[Round 1 审稿请求]:
## 交叉分享：请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

特别关注两人评分差异（你 3.5 vs R2 3.0）的根源——R2 的核心降分理由是"贡献悖论"（K*≤2 使 depth estimation 退化为 binary detection），你是否认同这一判断？

---

## Reviewer 2 审稿报告（Round 1 — 新颖性/贡献/相关工作/写作质量）

---

### Paper Summary

本文定义了"generational depth estimation"问题：给定一篇文本，估计其经历了多少轮递归合成生成。作者提出 K*_empirical 作为"discrimination boundary"的下界——即分类器能可靠区分相邻深度的最大深度。通过 15 维统计特征 + OBD-LightGBM 分类器，在 10 种模型配置（6 个架构族，1B-8B）、4 个领域、4 种解码策略上实验。核心发现：web text 上 K*≤2（"one-wash laundering"现象），arXiv 上 K*=3，跨模型迁移保留 80-92% 准确率。在极端污染场景（~83% synthetic）下，K*=2 正确预测了 binary filtering 是最优策略。

---

### 总体评分

**Overall**: 3.0（Findings）
**一句话总结**: 问题定义有一定新意，实验覆盖全面，但核心发现 K*≤2 构成"贡献悖论"——depth estimation 框架的实际效用被还原为 binary detection，novelty 和 practical impact 不足以支撑 Main Conference。

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论合理，统计检验严谨（Bonferroni、bootstrap CI、permutation test），但 DPI 与 AUC 的关联是非正式的，θ=0.60 的选取有一定任意性 |
| Excitement | 3/5 | 问题时效性强，one-wash laundering 概念有趣，但 K*≤2 限制了框架的实际影响力，结论与 binary detection 高度重合 |
| Overall Assessment | 3.0/5 | Findings 水准：实证工作扎实但贡献显著性不足 |
| Confidence | 4/5 | model collapse 和 text detection 在我的专长范围内 |
| Reproducibility | 4/5 | 提供匿名代码/数据链接，超参数和实验设置在 appendix 中详述 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] 贡献悖论：K*≤2 使 depth estimation 框架退化为 binary detection

- 具体位置：Section 1（contributions），Section 5（filtering），Section 7（conclusion）
- 问题：论文的核心 framing 是"generational depth estimation"这一新问题，但主要实验发现 K*≤2（web text）意味着深度估计在实践中等价于二分类（human vs. machine）或最多三分类（depth 0/1/≥2）。Section 5 的 filtering 实验进一步证实 binary filtering 是最优策略，graduated weighting 没有额外收益——这与现有 binary detector（DivEye、Binoculars、Min-K++等）的实际功能完全一致。论文试图将 K*=2 本身作为贡献（"knowing the boundary matters"），但未充分论证：(a) 知道 K*=2 相比直接使用 binary detector 在实践中有何额外价值？(b) K*=2 这一结论对 data curation pipeline 的设计产生了哪些 binary detection 无法给出的指导？
- 为什么影响接收：如果 depth estimation 框架的实际产出等价于已有工作，novelty 和 practical contribution 将大打折扣。审稿人会质疑：为什么需要一个新框架来得出"用 binary 就够了"这一结论？
- 建议修改方向：(1) 在 Introduction 和 Discussion 中更坦诚地讨论这一悖论，明确区分 framework 的理论价值（characterization of information loss dynamics）和实践价值；(2) 更深入地讨论 K*>2 的场景（arXiv K*=3，neural probe K*=3-4，retrain-chain K*≥4），将这些作为框架价值的正面证据而非脚注；(3) 讨论在什么条件下（更强的特征、更大的模型、structured domains）depth estimation 可能变得 non-trivially useful。

**N2** [critical] 4/10 配置 K*=1 削弱了"K*≤2 universally holds"的主张

- 具体位置：Section 4.1（第45-47行，LaTeX experiments_c1.tex），Table 2（主文），Table 10（appendix）
- 问题：论文的核心声明是"K*≤2 holds universally for web text"（Abstract, Conclusion），但 4/10 配置（OLMo 全部配置、Gemma-2-2B、Mistral-7B、Pythia-6.9B 的部分配置）给出 K*=1，意味着这些模型甚至无法区分 depth 1 和 depth 2。论文将 OLMo K*=1 归因为该模型的特性（"sole exception"），但当 40% 的配置给出 K*=1 时，这不再是"exception"。论文对 K*=1 出现的原因缺乏系统性分析：是模型容量、训练数据、架构差异、还是 15D 特征集的局限？
- 为什么影响接收：如果 K*=1 和 K*=2 的分布接近 50/50，那么 K*=2 的"universal"声明需要更多 qualification。此外，K*=1 意味着连 binary depth distinction（depth 1 vs 2）都做不到，进一步削弱了 depth estimation 框架的适用性。
- 建议修改方向：(1) 明确报告 K*=1 和 K*=2 的比例，避免"universally K*≤2"的 overclaiming；(2) 增加对 K*=1 模型的特征分析（例如 OLMo 和 Pythia-6.9B 的 surprisal distribution 是否确实没有 depth-dependent shift）；(3) 讨论 K*=1 是特征集的局限（lower bound 太 loose）还是真实的信息论极限。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Text watermarking 作为 provenance tracking 替代方案的讨论严重不足

- 具体位置：Section 2（related_work.tex 第18-19行）
- 问题：Text watermarking（Kirchenbauer et al., 2023）是 generational provenance tracking 的直接竞争范式——如果生成器嵌入水印，则可以精确追踪生成深度，K*理论上可以无限延伸。论文仅用一句话提及 watermarking（"our work addresses the complementary post-hoc scenario where the generator is not controlled"），但没有讨论：(a) 在什么场景下 post-hoc 方法优于 proactive watermarking？(b) 随着 watermarking 技术普及，post-hoc depth estimation 的长期价值如何？(c) 是否有混合方案（部分水印 + post-hoc 检测）的可能性？
- 建议：在 Related Work 中增加 1-2 句讨论 watermarking 与 post-hoc detection 的互补性和各自适用条件。

**W2** [warning] θ=0.60 的阈值选取存在 circularity 风险

- 具体位置：Section 3.1（method.tex 第34-40行），Figure 3
- 问题：θ=0.60 的主要 justification 是"sits between the 1v2 AUC cluster (0.607-0.696) and the 2v3 cluster (0.55-0.59)"。但这意味着阈值是在观察到 AUC 分布后选择的，使其恰好将 K* 定在 2。这构成了一种弱 circularity：先看数据分布，再选阈值，再报告该阈值下的结论。虽然 Figure 3 的 sensitivity analysis 缓解了这一问题（K*=2 在 θ∈[0.59, 0.60] 范围内稳定），但 1pp 的稳定窗口并不宽裕。在 θ=0.61 时，Pythia-1.4B 已 drop 到 K*=1。
- 建议：(1) 承认 θ 是 post-hoc 选取的，或者提供 θ 的先验 justification（如基于随机分类器的 null distribution）；(2) 报告在多个 θ 值下的主要结论，而非仅在 θ=0.60 下。

**W3** [warning] Retrain-chain K*≥4 的声明缺乏方法论支撑

- 具体位置：Section 6（discussion.tex 第28行）
- 问题："Retrain-chain experiments yield K*≥4" 在正文中仅一句话提及，但没有描述实验方法、使用的模型、训练过程或统计检验。如果 retrain-chain 确实能达到 K*≥4，这将是本文框架最有价值的应用场景之一——它表明 depth estimation 在 retrain 设定下是 non-trivial 的。但目前这一声明是未经充分支撑的。
- 建议：(1) 在 appendix 中补充 retrain-chain 实验的完整方法和结果；(2) 或者删除这一声明，避免 unsupported claim。

**W4** [warning] 论文叙事密度过高，insight 深度不足

- 具体位置：整个 Section 4-5
- 问题：正文 8 页内塞入了 10 个模型配置、4 个领域、4 种解码策略、cross-model transfer、cross-scorer validation、neural probe、binary detector comparison、filtering experiment 等大量实验，每个实验的讨论空间极为有限。许多关键发现被压缩到 1-2 句话后立即指向 appendix table。例如 Section 4.3（Feature Ordering，7 行文字）和 Section 4.6（Binary Detector，4 行文字）。这导致论文读起来更像实验结果清单而非有深度的分析。
- 建议：考虑删减部分边缘实验（如 binary detector confidence 可移到 appendix），腾出空间对核心发现进行更深入的分析和讨论。

---

### 小问题（不影响接收）

- Introduction 第7行（introduction.tex line 7）一句话中有三层括号嵌套（retrain-chains 定义、prompt-chains 定义、appendix 引用），可读性差。建议拆成两句。
- Section 4.5 中 "Jensen--Shannon divergence" 使用 en-dash 连接双人名，虽然 LaTeX 排版上可接受，但在 NLP 社区更常见的写法是 "Jensen-Shannon"（hyphen）。
- Abstract word count: ~144 words，符合 200 words 限制。
- Limitations 部分：3 个点，简洁恰当，符合规范。
- 未发现正文行文中使用破折号（em-dash）的违规情况。所有 `---` 均出现在表格中作为缺失值标记。
- 匿名规则：作者标为 "Anonymous"，符合 double-blind 要求。
- 页数限制：正文（Section 1-7）在 8 页以内，Limitations 在第 9 页，符合 EMNLP 2026 格式要求。

---

### 主要优势

1. **问题定义有开拓性**：将 generational depth estimation 从模糊的直觉转化为可操作的度量（K*_empirical），为 model collapse 和 data contamination 研究提供了量化工具。DPI → discrimination boundary 的理论动机是自然的。

2. **实验覆盖面广且方法论严谨**：10 个模型配置、6 个架构族、4 个领域、4 种解码策略，辅以 Bonferroni 校正、bootstrap CI、permutation test、ANOVA，统计测试达到了高标准。Appendix 提供了充分的复现细节。

3. **"One-wash laundering"概念有传播价值**：将 K*=2 的发现包装为"一次清洗即不可追溯"的概念，对数据治理实践有直接的 messaging value——它告诉社区：一旦合成文本被再次用于生成，后续深度信息就丢失了。

4. **跨模型迁移（80-92%）是实用贡献**：15D generator-agnostic 特征集在 continuation mode 下的高迁移率（scorer-invariant feature ranking ρ>0.90）使得无需知道生成模型即可部署，这对实际数据审计有价值。

5. **K*-guided filtering 提供了 end-to-end 验证**：Section 5 的 filtering 实验将 K* 从描述性度量提升为有预测力的指标，展示了框架与下游任务的连接。

---

### 针对 Director 指定审查维度的总结判断

1. **新颖性与贡献**：中等。问题定义有新意，但 K*≤2 导致框架退化为 binary detection（贡献悖论）。One-wash laundering 是一个有价值的 empirical characterization，但不构成方法论突破。与 binary detection 的增量贡献需要更清晰的论证。

2. **相关工作**：基本完整，model collapse 和 detection 文献覆盖良好，但 watermarking 讨论过于薄弱。未发现 2025-2026 重大遗漏。

3. **写作质量**：整体清晰，叙事逻辑通顺，术语引入恰当。主要问题是信息密度过高导致 insight 深度不足。无破折号违规，abstract 字数合规，limitations 格式正确。

4. **整体定位**：更适合 Findings。论文的 ambition（depth estimation framework）与 conclusion（binary suffices）之间的张力是最大障碍。如果能更好地 frame K*>2 场景（arXiv、retrain-chain、neural probe）的价值，并深入讨论贡献悖论，有望提升到 Borderline Conference（3.5）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2369 · 2026-05-25T21:35:25.432737+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### 评分差异分析（R1: 3.5 vs R2: 3.0）\n\n核心分歧在于如何评估\"贡献悖论\"的杀伤力。R2 认为 K*≤2 使 depth estimation 退化为 binary detection，因此框架的 novelty 和 practical contribution 不足以支撑 Main Conference。我的判断是：K*≤2 作为 empirical characterization 本身有独立价值（它解释了 WHY binary suffices，而非仅仅重复 binary suffices 这一结论），且框架在 K*>2 场景（arXiv K*=3, retrain-chain K*≥4）中展示了 non-trivial 的扩展潜力。但我同意 R2 的核心批评有相当的合理性——论文确实未充分论证 depth framework 相比 binary detection 的增量实践价值。详见下方 N1 回应。\n\n---\n\n### Must-Fix 问题回应\n\n**[REBUT] R2-N1: 贡献悖论（K*≤2 使 framework 退化为 binary detection）**\n\nR2 的论点有道理但过于绝对。我的反驳基于三点：\n\n(1) **K*=2 是一个 characterization result，不等于 \"binary detection\"。** 论文的贡献不是\"提供一个新 detector\"，而是回答\"递归合成文本的统计可区分性在哪一代消失\"。这一问题此前无人定量回答。K*≤2 告诉我们信息损失集中在 0v1 边界——这解释了为什么 graduated strategies 不 work（Section 5, Table 5: graduated 在 depth≥2 上基于近随机分类器输出赋权，注入噪声而非信号）。现有 binary detector（DivEye, Binoculars）不提供这一解释，它们只输出 binary label。\n\n(2) **K*>2 场景证明框架有超越 binary 的适用性。** arXiv K*=3（Table 4, 4 个独立 family），neural probe K*_neural=3-4（Table 3），DeBERTa K*=4 on arXiv（Table in Appendix B.14），retrain-chain K*≥4（Appendix B.7）。这些场景下 depth estimation IS non-trivially useful。R2 建议将这些作为\"框架价值的正面证据而非脚注\"——我同意此建议，但不同意这些已有结果不足以支撑框架价值的判断。\n\n(3) **但 R2 的核心批评仍然成立：论文的 framing 确有张力。** Title 和 Abstract 强调 \"depth estimation\"，但 web text 的 actionable conclusion 确实是 \"use binary\"。论文需要更好地 frame：框架的理论贡献（characterization of information loss）vs. 实践贡献（对特定场景如 structured text 和 retrain-chain 的 non-binary depth estimation）。\n\n**结论**：R2-N1 是 valid 的 framing 问题，但不构成 reject 理由。合理的修改路径如 R2 所建议的(1)(2)(3)即可解决。这一张力不应将评分从 3.5 拉到 3.0——characterization results 在 NLP venues 有接收先例（如 model collapse 系列论文本身也是 characterization，Shumailov et al. 2024 被 Nature 接收）。\n\n---\n\n**[AGREE] R2-N2: 4/10 K*=1 削弱 \"universally K*≤2\" 主张**\n\n同意，但需要补充几点 nuance：\n\n(a) \"K*≤2 universally\" 这一表述在技术上是正确的——K*=1 ⊂ K*≤2。论文的 claim 是上界，不是等式。所有 10 个配置确实都满足 K*≤2。\n\n(b) 但 R2 的深层 concern 有道理：当 40% 配置 K*=1 时，\"depth estimation\" 这个词对这些模型而言毫无操作意义——甚至连 depth 1 vs 2 都区分不了。这确实削弱了框架的适用性主张。\n\n(c) 这与我自己的 N1/N2 相呼应——我指出的问题是 K*=2 配置中 Qwen 过度代表（4/6 K*=2 是 Qwen），以及 Bonferroni 校正下仅 3/6 显著。R2 从另一个角度（K*=1 的比例）得出类似结论：核心发现的 generalizability 不如论文所宣称的那么强。\n\n(d) R2 建议\"增加对 K*=1 模型的特征分析\"——这非常有价值。论文在 Section 4.5 (Cross-Domain) 对 OLMo 的 cross-scorer 验证（p=0.510, n.s.）表明 K*=1 对 OLMo 是 robust 的，但没有分析 WHY OLMo 生成的文本在 depth 1 vs 2 上就失去了可区分性。是 OLMo 的生成质量太低（collapse 太快）还是太高（统计特征太接近人类文本）？论文应该探讨。\n\n---\n\n### Should-Fix 问题回应\n\n**[AGREE] R2-W1: Watermarking 讨论不足**\n\n同意。Watermarking 是 generational provenance tracking 的直接对标方案。论文仅用一句\"complementary post-hoc scenario\"带过，这不够。至少应讨论：(a) post-hoc 方法的核心优势是不需要控制生成器，适用于已有的 uncontrolled synthetic text；(b) watermarking 在多轮递归生成下的鲁棒性也是 open question（recursive paraphrasing 可能 wash out watermarks，与 one-wash laundering 形成有趣的对比）。补充 1-2 句即可，不需要大篇幅。\n\n**[AGREE] R2-W2: θ=0.60 的 circularity**\n\n完全同意，与我自己的 W2 一致。θ 的选取确实是 post-hoc 的。R2 和我都认为 Figure 3 的 sensitivity analysis 部分缓解了这一问题，但 1pp 的稳定窗口（θ∈[0.59, 0.60]）并不宽裕。论文应承认 θ 的 post-hoc 性质，并报告基于 permutation null 的 principled threshold。\n\n**[REBUT] R2-W3: Retrain-chain K*≥4 声明缺乏方法论支撑**\n\n部分反驳。R2 说\"没有描述实验方法、使用的模型、训练过程\"，但 Appendix B.7（appendix_extended.tex lines 71-73）明确写道：\n\n> \"Retrain-chain validation (Pythia-1.4B LoRA, 5 generations) yields K*≥4 (1v2 AUC = 0.9484, 2v3 = 0.8888, 3v4 = 0.7982)\"\n\n这提供了：模型（Pythia-1.4B）、方法（LoRA fine-tuning）、代数（5 generations）、具体 AUC 数值（3 个 boundary pair）。虽然不够详尽（缺少 LoRA 超参数、训练数据量、CI 等），但不是\"未经支撑的 claim\"。R2 的\"或者删除这一声明\"建议过于极端——这是论文框架 beyond-binary 价值的关键证据。建议补充 LoRA 训练细节和 bootstrap CI，但无需删除。\n\n**[AGREE] R2-W4: 叙事密度过高，insight 深度不足**\n\n部分同意。Section 4 确实塞了太多实验，每个实验 1-2 句讨论就跳到下一个。特别是 Section 4.3（Feature Ordering，仅 7 行）和 Section 4.6（Binary Detector Confidence，4 行）。但我对修改建议有不同看法：R2 建议\"删减边缘实验\"，我更倾向于\"重组结构\"——将 binary detector confidence 和 feature ordering 移到 appendix，腾出空间深入讨论 core findings（K*=2 的 boundary dynamics、K*=1 vs K*=2 的模型差异、arXiv K*=3 的 implications）。实验的广度是 strength，不应砍掉，但应重新分配讨论篇幅。\n\n---\n\n### 小问题回应\n\n- **Introduction 括号嵌套**：[AGREE] 三层括号确实影响可读性。\n- **Jensen--Shannon vs Jensen-Shannon**：[REBUT] 微小排版偏好，en-dash 连双人名在数学/物理文献中是标准用法，NLP 社区两种写法均被接受，不构成问题。\n- **Abstract word count**：R2 统计约 144 words，但我重新核对 LaTeX 源文件（main.tex lines 36-42），实际 abstract 约 180-190 words（R2 可能统计有误——abstract 包含多个长句和技术术语）。无论如何，符合 200 words 限制。\n\n---\n\n### 对贡献悖论的最终判断\n\nR2 的\"贡献悖论\"是本轮审稿中最重要的争议点。我的最终立场：\n\n**R2 的诊断是准确的**——K*≤2 确实在 web text 上将 depth estimation 的实际效用拉近到 binary detection。这是论文必须正面回应的核心质疑。\n\n**但 R2 的处方（降至 Findings）可能过重**——理由如下：\n1. Characterization results 本身有独立价值。K*≤2 不是在 reinvent binary detection，而是在量化 WHY binary suffices——这是一个新的 empirical finding，不是已有结论的重复。\n2. 框架在 K*>2 场景中有 non-trivial 的应用（arXiv, retrain-chain, neural probe）。\n3. 实验的广度和统计严谨性在同类工作中属于上游水平。\n\n**综合评判**：如果论文能按 R2-N1 的建议(1)(2)(3)修改 framing（更坦诚地讨论悖论、强化 K*>2 场景的论述、明确区分理论与实践贡献），加上我 N1/N2 要求的 per-family 分析和 Bonferroni marginal 的更诚实表述，整体质量可以达到 Borderline Conference（3.5）。当前状态下，我维持 3.5 但理解 R2 给 3.0 的逻辑。\n\n**建议 Director**：R1 和 R2 在 Soundness 上一致（3.5），分歧主要在 Excitement/Overall。核心争议是\"characterization result 的贡献是否够 Main Conference\"——这更适合由 AC 在 meta-review 中基于 venue 的接收标准最终裁定。",
  "reviewer_id": "1",
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### 评分差异分析（R1: 3.5 vs R2: 3.0）\n\n核心分歧在于如何评估\"贡献悖论\"的杀伤力。R2 认为 K*≤2 使 depth estimation 退化为 binary detection，因此框架的 novelty 和 practical contribution 不足以支撑 Main Conference。我的判断是：K*≤2 作为 empirical characterization 本身有独立价值（它解释了 WHY binary suffices，而非仅仅重复 binary suffices 这一结论），且框架在 K*>2 场景（arXiv K*=3, retrain-chain K*≥4）中展示了 non-trivial 的扩展潜力。但我同意 R2 的核心批评有相当的合理性——论文确实未充分论证 depth framework 相比 binary detection 的增量实践价值。详见下方 N1 回应。\n\n---\n\n### Must-Fix 问题回应\n\n**[REBUT] R2-N1: 贡献悖论（K*≤2 使 framework 退化为 binary detection）**\n\nR2 的论点有道理但过于绝对。我的反驳基于三点：\n\n(1) **K*=2 是一个 characterization result，不等于 \"binary detection\"。** 论文的贡献不是\"提供一个新 detector\"，而是回答\"递归合成文本的统计可区分性在哪一代消失\"。这一问题此前无人定量回答。K*≤2 告诉我们信息损失集中在 0v1 边界——这解释了为什么 graduated strategies 不 work（Section 5, Table 5: graduated 在 depth≥2 上基于近随机分类器输出赋权，注入噪声而非信号）。现有 binary detector（DivEye, Binoculars）不提供这一解释，它们只输出 binary label。\n\n(2) **K*>2 场景证明框架有超越 binary 的适用性。** arXiv K*=3（Table 4, 4 个独立 family），neural probe K*_neural=3-4（Table 3），DeBERTa K*=4 on arXiv（Table in Appendix B.14），retrain-chain K*≥4（Appendix B.7）。这些场景下 depth estimation IS non-trivially useful。R2 建议将这些作为\"框架价值的正面证据而非脚注\"——我同意此建议，但不同意这些已有结果不足以支撑框架价值的判断。\n\n(3) **但 R2 的核心批评仍然成立：论文的 framing 确有张力。** Title 和 Abstract 强调 \"depth estimation\"，但 web text 的 actionable conclusion 确实是 \"use binary\"。论文需要更好地 frame：框架的理论贡献（characterization of information loss）vs. 实践贡献（对特定场景如 structured text 和 retrain-chain 的 non-binary depth estimation）。\n\n**结论**：R2-N1 是 valid 的 framing 问题，但不构成 reject 理由。合理的修改路径如 R2 所建议的(1)(2)(3)即可解决。这一张力不应将评分从 3.5 拉到 3.0——characterization results 在 NLP venues 有接收先例（如 model collapse 系列论文本身也是 characterization，Shumailov et al. 2024 被 Nature 接收）。\n\n---\n\n**[AGREE] R2-N2: 4/10 K*=1 削弱 \"universally K*≤2\" 主张**\n\n同意，但需要补充几点 nuance：\n\n(a) \"K*≤2 universally\" 这一表述在技术上是正确的——K*=1 ⊂ K*≤2。论文的 claim 是上界，不是等式。所有 10 个配置确实都满足 K*≤2。\n\n(b) 但 R2 的深层 concern 有道理：当 40% 配置 K*=1 时，\"depth estimation\" 这个词对这些模型而言毫无操作意义——甚至连 depth 1 vs 2 都区分不了。这确实削弱了框架的适用性主张。\n\n(c) 这与我自己的 N1/N2 相呼应——我指出的问题是 K*=2 配置中 Qwen 过度代表（4/6 K*=2 是 Qwen），以及 Bonferroni 校正下仅 3/6 显著。R2 从另一个角度（K*=1 的比例）得出类似结论：核心发现的 generalizability 不如论文所宣称的那么强。\n\n(d) R2 建议\"增加对 K*=1 模型的特征分析\"——这非常有价值。论文在 Section 4.5 (Cross-Domain) 对 OLMo 的 cross-scorer 验证（p=0.510, n.s.）表明 K*=1 对 OLMo 是 robust 的，但没有分析 WHY OLMo 生成的文本在 depth 1 vs 2 上就失去了可区分性。是 OLMo 的生成质量太低（collapse 太快）还是太高（统计特征太接近人类文本）？论文应该探讨。\n\n---\n\n### Should-Fix 问题回应\n\n**[AGREE] R2-W1: Watermarking 讨论不足**\n\n同意。Watermarking 是 generational provenance tracking 的直接对标方案。论文仅用一句\"complementary post-hoc scenario\"带过，这不够。至少应讨论：(a) post-hoc 方法的核心优势是不需要控制生成器，适用于已有的 uncontrolled synthetic text；(b) watermarking 在多轮递归生成下的鲁棒性也是 open question（recursive paraphrasing 可能 wash out watermarks，与 one-wash laundering 形成有趣的对比）。补充 1-2 句即可，不需要大篇幅。\n\n**[AGREE] R2-W2: θ=0.60 的 circularity**\n\n完全同意，与我自己的 W2 一致。θ 的选取确实是 post-hoc 的。R2 和我都认为 Figure 3 的 sensitivity analysis 部分缓解了这一问题，但 1pp 的稳定窗口（θ∈[0.59, 0.60]）并不宽裕。论文应承认 θ 的 post-hoc 性质，并报告基于 permutation null 的 principled threshold。\n\n**[REBUT] R2-W3: Retrain-chain K*≥4 声明缺乏方法论支撑**\n\n部分反驳。R2 说\"没有描述实验方法、使用的模型、训练过程\"，但 Appendix B.7（appendix_extended.tex lines 71-73）明确写道：\n\n> \"Retrain-chain validation (Pythia-1.4B LoRA, 5 generations) yields K*≥4 (1v2 AUC = 0.9484, 2v3 = 0.8888, 3v4 = 0.7982)\"\n\n这提供了：模型（Pythia-1.4B）、方法（LoRA fine-tuning）、代数（5 generations）、具体 AUC 数值（3 个 boundary pair）。虽然不够详尽（缺少 LoRA 超参数、训练数据量、CI 等），但不是\"未经支撑的 claim\"。R2 的\"或者删除这一声明\"建议过于极端——这是论文框架 beyond-binary 价值的关键证据。建议补充 LoRA 训练细节和 bootstrap CI，但无需删除。\n\n**[AGREE] R2-W4: 叙事密度过高，insight 深度不足**\n\n部分同意。Section 4 确实塞了太多实验，每个实验 1-2 句讨论就跳到下一个。特别是 Section 4.3（Feature Ordering，仅 7 行）和 Section 4.6（Binary Detector Confidence，4 行）。但我对修改建议有不同看法：R2 建议\"删减边缘实验\"，我更倾向于\"重组结构\"——将 binary detector confidence 和 feature ordering 移到 appendix，腾出空间深入讨论 core findings（K*=2 的 boundary dynamics、K*=1 vs K*=2 的模型差异、arXiv K*=3 的 implications）。实验的广度是 strength，不应砍掉，但应重新分配讨论篇幅。\n\n---\n\n### 小问题回应\n\n- **Introduction 括号嵌套**：[AGREE] 三层括号确实影响可读性。\n- **Jensen--Shannon vs Jensen-Shannon**：[REBUT] 微小排版偏好，en-dash 连双人名在数学/物理文献中是标准用法，NLP 社区两种写法均被接受，不构成问题。\n- **Abstract word count**：R2 统计约 144 words，但我重新核对 LaTeX 源文件（main.tex lines 36-42），实际 abstract 约 180-190 words（R2 可能统计有误——abstract 包含多个长句和技术术语）。无论如何，符合 200 words 限制。\n\n---\n\n### 对贡献悖论的最终判断\n\nR2 的\"贡献悖论\"是本轮审稿中最重要的争议点。我的最终立场：\n\n**R2 的诊断是准确的**——K*≤2 确实在 web text 上将 depth estimation 的实际效用拉近到 binary detection。这是论文必须正面回应的核心质疑。\n\n**但 R2 的处方（降至 Findings）可能过重**——理由如下：\n1. Characterization results 本身有独立价值。K*≤2 不是在 reinvent binary detection，而是在量化 WHY binary suffices——这是一个新的 empirical finding，不是已有结论的重复。\n2. 框架在 K*>2 场景中有 non-trivial 的应用（arXiv, retrain-chain, neural probe）。\n3. 实验的广度和统计严谨性在同类工作中属于上游水平。\n\n**综合评判**：如果论文能按 R2-N1 的建议(1)(2)(3)修改 framing（更坦诚地讨论悖论、强化 K*>2 场景的论述、明确区分理论与实践贡献），加上我 N1/N2 要求的 per-family 分析和 Bonferroni marginal 的更诚实表述，整体质量可以达到 Borderline Conference（3.5）。当前状态下，我维持 3.5 但理解 R2 给 3.0 的逻辑。\n\n**建议 Director**：R1 和 R2 在 Soundness 上一致（3.5），分歧主要在 Excitement/Overall。核心争议是\"characterization result 的贡献是否够 Main Conference\"——这更适合由 AC 在 meta-review 中基于 venue 的接收标准最终裁定。",
    "reviewer_id": "1",
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2370 · 2026-05-25T21:35:29.001142+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3568
}
```

</details>

---


### Assistant

_source line 2371 · 2026-05-25T21:35:36.534156+00:00_

交叉回应已提交给 Review Director。

核心结论：R2 的"贡献悖论"诊断准确（K*≤2 确实将 depth estimation 拉近 binary detection），但我认为 characterization result 本身有独立价值，且 K*>2 场景（arXiv/retrain-chain/neural probe）证明框架有 beyond-binary 的扩展潜力，降至 Findings 过重。两位 Reviewer 在 Soundness 上一致（3.5），分歧集中在 Excitement/Overall，建议 Director 关注"characterization result 是否够 Main Conference"这一判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1"
}
```

</details>

---
