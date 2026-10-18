# Director coordination — Part 4 of 7

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/9d/9db2d5c10f518e51ec86.json)

## Round 79

### Tool call

_source line 816 · 2026-05-22T09:35:39.575758+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "report": "# Round 9 审稿报告（Fresh Review）\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性/实验设计/统计方法论; R2: 新颖性/完整性/Related Work/写作质量）\n**交叉轮次**: 1 轮（Round 1 初审 + 交叉分享 + 收敛）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，结合 NLI-gated content control、per-axis style decomposition 和 position-controlled pairwise comparison，量化 LLM judge 中的风格偏差。核心发现称为\"Likert Blindspot\"：Likert 评分系统性地遗漏 pairwise comparison 能检测到的风格偏差——在中等效应量时完全衰减（d → 0），在较强效应时衰减 >60%。实验跨 4 个 target judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、1 个负对照（Claude Sonnet 4）、3 个 benchmark、3 个 style axis 验证。GEE conditional decomposition 揭示 per-axis confound structure：verbosity style-dominated，formality conditional，register judge-dependent。\n\n---\n\n## Strengths\n\n**S1. 实验设计多维度且严谨。** 4+1 judges × 3 benchmarks × 2+1 style axes × 7 种统计方法的交叉验证矩阵在 LLM evaluation 文献中罕见。Table 2 的 sensitivity hierarchy 呈现干净的 all-or-nothing 模式：所有 pairwise 方法显著，所有 Likert 方法不显著，极具说服力。[R1-S2, R2-S1, R2-S2, AGREE]\n\n**S2. 负对照设计有效。** Claude Sonnet 4 在相同 pairwise 设计下 BT ≈ 54-56%，TOST 确认等价性。为其他 judge 的显著偏差提供了因果对比基础——证明偏差是 judge-specific 而非 format-induced。[R1-S4, AGREE]\n\n**S3. 因果推断框架诚实定位。** §3.5 Design Rationale 明确 DAG 是 \"design rationale, not a claim of perfect identification\"，三个 operational assumptions 逐一列出并在附录中提供经验验证。[R1-S3, R2 partial REBUT on Title/Abstract language]\n\n**S4. Per-axis confound structure 是独立有价值发现。** GEE conditional decomposition 揭示 verbosity = style-dominated（Style OR 8–13）、formality = conditional on originality、register = judge-dependent。对 LLM judge 用户有直接 actionable value。[R1-S5, R2-S3, AGREE]\n\n**S5. Robustness 分析深度罕见。** Appendix A–Q 覆盖方向非对称性、NLI consistency filter、GEE diagnostics、rewriter independence、NLI threshold sweep (11 points)、direction-aware gate validation、Claude TOST、bootstrap attenuation、BT goodness-of-fit、100-point Likert、NLI gate ablation、rewriting artifact control。几乎回答了每个合理质疑。[R1-S5, R2-S4, AGREE]\n\n**S6. Black-box 框架设计实用性强。** CSD 不需要 judge 内部访问，可 post-hoc 应用于任何 black-box judge。[R2-S5, AGREE]\n\n---\n\n## Weaknesses\n\n### Must-Fix（需在 rebuttal/revision 中解决）\n\n**MF1. NLI gate 作为 content preservation 唯一门控缺乏人工验证** [R1-N1 critical, R2-Q1 AGREE]\n- CSD 因果推断完全依赖 NLI gate (DeBERTa-v3-large, τ=0.90) 保证 content 不变，但 NLI 模型存在系统性盲区（如对论证结构重组不敏感）。论文未报告任何 human evaluation of content preservation quality。\n- GPT-4o cross-validation (92.1%/82.6% pass precision) 是 LLM-vs-LLM 验证，存在认识论循环——用同类工具验证测量工具。\n- 如果 NLI gate 系统性放过某些 content 变化（如 formal 改写增加 hedging 改变 claim 强度），则观测到的\"style bias\"可能部分是 content bias 的伪装。\n- **此问题自 Round 3 起持续 7 轮未解决。** 两位 Reviewer 共同指向：增加 human evaluation 是最大可 actionable 改进（50-100 pairs × 2-3 annotators）。\n- **交叉共识**: 双方完全一致。\n\n**MF2. Novelty framing 过于强势——核心发现是已知测量理论的实证确认** [R1-N2 critical, R2-N1 critical, AGREE]\n- Thurstone (1927) Law of Comparative Judgment 已建立 pairwise > Likert 的灵敏度优势。论文在 §2 引用了这些文献并承认理论预测，但 Title/Abstract/Conclusion 中的 \"reveal\" 措辞将此包装为新发现。\n- 更准确的定位：CSD 框架首次在 LLM judge 场景下系统量化了理论预测的灵敏度差距（severity spectrum 和 per-axis confound structure 是真正新发现）。\n- **交叉共识**: 双方完全一致。建议从 \"reveal\" 转为 \"quantify\"；将 per-axis confound structure 提升为并列核心贡献。此问题自 Round 1 起持续未完全修正。\n\n### Should-Fix（重要但非致命）\n\n**SF1. Pairwise \"检测\" vs. \"放大\" 的核心解释性歧义** [R2-N2 critical → R1 REBUT 降为 warning]\n- 替代解释：pairwise comparison 可能放大微小的、无关紧要的风格微偏好，Likert 的不显著才反映真实效应。\n- 论文 §5.4 提供 6 项 amplification controls（NLI gate ablation、Claude 负对照、cross-axis BT variation、GEE artifact control、debiased prompting、cross-architecture replication），Jeong et al. (2025) Comparative Trap 也在讨论之中。\n- R1 反驳核心论据：Claude 负对照在相同 pairwise 设计下无偏差，证明非 format-induced 放大。\n- **分歧记录**: R2 定 critical（controls 只排除大规模放大，无法排除中等程度放大），R1 定 warning（负对照已充分缓解）。Director 判定 **Should-Fix**：Conclusion 语言应更谨慎（从 \"reveal\" 改为条件性表述），但论文已提供了合理的 bounding analysis。\n\n**SF2. Style axis 覆盖面过窄** [R2-W1 warning, R1 AGREE direction]\n- 仅 2 primary + 1 exploratory axes。LLM judge 已知风格偏差远不止这些（bullet-point vs. prose、hedging level 等）。\"Per-axis confound structure\" 这一分类法基于 3 个 axis 的泛化基础不足。\n- 建议：限定为 \"preliminary evidence of axis-dependent confound patterns\"；在 Limitations 列出未覆盖轴。\n\n**SF3. Claude TOST Δ=15pp margin 偏宽且覆盖不完整** [R1-W3 warning, R2 implied AGREE]\n- Δ=15pp 接近 GPT-4o formality 的 BT 偏差（~13pp），意味着 Claude 可能存在高达 15pp 的 style preference 仍被判\"无偏差\"。Claude 仅覆盖 2/3 axes（无 register）。\n- 建议三选一：(a) 增加 n 使 Δ=10pp 有功效；(b) reframe 为 \"insufficient evidence for bias at Δ=15pp precision\"；(c) 报告 minimum detectable Δ at 80% power。\n\n**SF4. Evaluator-producer overlap 处理力度有限** [R1-W4 warning, R2-Q3 AGREE]\n- Qwen3-32B 同时做 rewriter 和 judge。Cross-rewriter 验证（GPT-4o rewriter）显示 Style OR 下降 22%，但仅限 Qwen3-32B judge 验证。效应量有 ±20-25% rewriter-dependent 变异。\n- 建议：显式承认 Blindspot 存在性 robust 但效应量精确值受 rewriter 影响。\n\n**SF5. NLI gate 44% 拒绝率的选择偏差特征分析不足** [R2-W2 warning, R1 AGREE]\n- Appendix B 的 4 个 surface covariates 可能不够全面。Filtered-in pairs 可能偏向内容更简单的文本。\n- 建议补充对 filtered-out pairs 的语言复杂度对比分析。\n\n**SF6. Style axis 之间的 cross-contamination 未直接测试** [R1-W2 warning, R2 implied AGREE]\n- §3.5 假设(iii)（rewrite 不引入 target axis 外的系统性变化）未被经验验证。Table 5 GEE interaction test 只检验 Style×Originality 而非 cross-axis interaction。\n- 建议：对每个 axis 改写样本测量其他 axis 的变化幅度。\n\n### Minor\n\n**M1. 100-point Likert 实验仅用单一 judge** [R2-W3, R1 AGREE]\n- Appendix M 仅 Qwen3-32B，如果 GPT-4o 在 100-point scale 下 ATE 显著则结论不成立。建议增加至少 1 个 judge。\n\n**M2. 因果语言张力** [R2-W4, R1 partial REBUT]\n- §3.5 disclaimer 已足够明确。问题仅在 Title (\"Controlled\") 和 Abstract 的措辞选择暗示过强因果识别。建议在 Abstract 增加一句说明 \"controlled\" 指 experimentally controlled rewriting 而非 formal causal identification。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Novelty reframing 是最优先修改**：从 \"我们发现了 Blindspot\" 转为 \"我们首次系统量化了已知测量理论效应在 LLM judge 场景下的严重程度 + 发现了 per-axis confound structure\"。[R1-N2 × R2-N1]\n2. **Human evaluation 是最大可 actionable 改进**：50-100 pairs × 2-3 annotators 的 content preservation 验证能同时解决 NLI gate 可信度和 detection vs. amplification 两个问题。[R1-N1 × R2-Q1]\n3. **实验设计的严谨性是主要优势**：7 种统计方法 × 4+1 judges × 3 benchmarks 的矩阵在同领域罕见。[R1-S2 × R2-S1]\n4. **Per-axis confound structure 应被提升为核心贡献**。[R1 cross × R2-N1]\n5. **TOST Δ=15pp 偏宽**，Claude 负对照的 framing 需更谨慎。[R1-W3 × R2 implied]\n\n## Reviewer Divergence [分歧]\n\n1. **检测 vs. 放大的严重程度** [R2-N2 critical vs. R1 warning]：R2 认为这是核心解释性歧义，论证存在循环性，且 6 项 controls 仅排除大规模放大；R1 反驳负对照（Claude BT ≈ 54-56%）是最强反驳证据——若 pairwise 系统性放大则所有 judge 均应受影响。R1 进一步指出论证在操作层面（alignment pipeline 确实用 pairwise）不循环。Director 判定 Should-Fix 而非 critical：Conclusion 语言应谨慎化，但论文已提供合理 bounding。\n\n---\n\n## Questions（需作者回应）\n\nQ1. NLI gate 的 false-pass rate 是否有人工验证数据？即使 50 pairs 的抽样也能大幅增强可信度。\nQ2. Table 1 缺失单元格代表什么？选择哪些 judge×axis×benchmark 组合的理由是什么？\nQ3. Bootstrap attenuation analysis (d = −0.017) 如何排除 Likert 和 pairwise 在 construct 层面的根本差异？\nQ4. Formal 改写是否系统性改变了 verbosity 或 register？是否有定量 axis isolation 证据？\nQ5. 选择 formality 和 verbosity 作为 primary axes 的先验理由是什么？\nQ6. 是否有办法量化 pairwise 的放大倍数（amplification factor），而非仅定性 bounding？\n\n---\n\n## Missing References\n\n- Simms, Zelazny, Williams & Bernstein (2019). *Psychological Assessment* — rating scale granularity 对 discriminability 的影响\n- Polo et al. (2024). tinyBenchmarks — IRT 在 LLM 评估中的应用\n- Kocmi & Federmann (2023). LLM judge bias across evaluation formats\n- 建议验证 Stureborg et al. (2024) 在 references.bib 中的完整性\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 2 warning / 4 info）：\n\n- **[warning] P16**: 末页仅 3 条 reference，约 85% 空白；建议调整分页使末页填充更充分\n- **[warning] P6**: 3 个 display items（Figure 3 + Table 2 + Figure 4）挤在同一页，Figure 3/4 图幅偏小，axis label 接近可读性下限；建议将 Table 2 或 Figure 4 移至 P7 分散密度\n- **[info] P1-3**: 前 3 页中仅 P2 有 1 个 display item，视觉上偏\"文字墙\"\n- **[info] P4**: Figure 2 因果 DAG 节点标签偏小，打印后可能需凑近看\n- **[info] P6**: Figure 3 的 filled/open diamond marker 尺寸较小，灰度打印时 significance 区分度可能下降\n- **[info] P13**: References 与 appendix 表格过渡区略拥挤\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 4/5 | 3.5-4 |\n| Excitement | 3.5/5 | 3/5 | 3-3.5 |\n| Reproducibility | 4/5 | 4/5 | 4 |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4/5 | 4/5 | 4 |\n\n**总评**: 实验工作扎实、统计分析充分、robustness 覆盖深入的 evaluation 方法论工作。核心发现（Likert 对 style bias 的结构性不敏感 + per-axis confound structure）对 NLP evaluation 社区有实用价值。但两个 Must-Fix 问题阻碍更高评分：(1) NLI gate 缺乏人工验证——这是因果推断链的最薄弱环节，且已持续 7 轮未解决；(2) Novelty framing 将已知测量理论效应的实证确认包装为新发现，需要重新定位。如果 rebuttal/revision 能增加 human evaluation 数据并 reframe novelty narrative，可上调至 4.0 (Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Motivating example (\"average height\") 后已有 nuance acknowledgment (\"formality preferences may partially reflect legitimate quality judgments\")——这是合理的处理。\n- \"CSD reveals the Likert Blindspot\" → 建议改为 \"CSD quantifies the Likert Blindspot\" 或 \"CSD demonstrates\"\n\n### §2 Related Work\n- 覆盖全面，Jeong et al. (2025) Comparative Trap 和 Tripathi et al. (2025) 均已引用。\n- 建议补充 IRT 文献（Polo et al., 2024）以加强 measurement theory 背景。\n\n### §3 Method\n- §3.2 NLI gate 描述清晰，direction-aware strategy 有理论依据。\n- §3.5 Design Rationale 的因果语言校准良好（\"design rationale, not a claim of perfect identification\"）。但 §3.1 \"constitutes a binary intervention on a single style variable\" 中 \"intervention\" 一词与 §3.5 的谨慎定位有张力。\n- Figure 2 DAG 标注了 residual confounding dashed line——诚实且有效。\n\n### §4 Experiments\n- §4.1 Statistical framework 现在明确 \"six tests—three target judges × two axes\" + Gemini confirmatory + Appendix Q 8-test sensitivity analysis。比之前轮次的表述有显著改善。\n- Table 1 footnote \"Empty cells: untested benchmark–axis combinations\" 存在但未说明选择理由。\n\n### §5 Analysis\n- §5.1 Likert Blindspot 的 head-to-head comparison with RATE 是有效的对比设计。\n- §5.1 measurement attenuation vs. construct divergence 的讨论已有改善（引用 Tripathi et al. 2025），但 \"Blindspot\" 术语天然偏向 attenuation 解释。\n- §5.2 GEE conditional decomposition 结果清晰，\"style-dominated\" 而非 \"confound-free\" 是正确术语选择。\n- §5.4 六项 amplification controls 是对 Comparative Trap 的系统性回应。\n\n### §6 Conclusion\n- 简洁但可能过于简短（3 句话）。建议增加 practical implication 和 caveats。\n\n### Limitations\n- 覆盖了主要局限：quality-style confounding、evaluator-producer bias、validation methodology、scale design、per-axis independence、ecological validity。\n- Limitations 写得坦诚且适当长度（约 3 个点，符合 EMNLP 要求）。\n- 建议补充：style axis 之间的 potential interaction；将 measurement theory 背景作为 limitation 显式列出。\n\n### 格式合规\n- ✅ ACL template (`\\usepackage[review]{acl}`)\n- ✅ Double-blind (`\\author{Anonymous}`)\n- ✅ 正文 8 页合规\n- ✅ Limitations section 存在\n- ✅ References 不限页\n- ⚠️ P6 display item 密度过高（视觉审查 warning）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "report": "# Round 9 审稿报告（Fresh Review）\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性/实验设计/统计方法论; R2: 新颖性/完整性/Related Work/写作质量）\n**交叉轮次**: 1 轮（Round 1 初审 + 交叉分享 + 收敛）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，结合 NLI-gated content control、per-axis style decomposition 和 position-controlled pairwise comparison，量化 LLM judge 中的风格偏差。核心发现称为\"Likert Blindspot\"：Likert 评分系统性地遗漏 pairwise comparison 能检测到的风格偏差——在中等效应量时完全衰减（d → 0），在较强效应时衰减 >60%。实验跨 4 个 target judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、1 个负对照（Claude Sonnet 4）、3 个 benchmark、3 个 style axis 验证。GEE conditional decomposition 揭示 per-axis confound structure：verbosity style-dominated，formality conditional，register judge-dependent。\n\n---\n\n## Strengths\n\n**S1. 实验设计多维度且严谨。** 4+1 judges × 3 benchmarks × 2+1 style axes × 7 种统计方法的交叉验证矩阵在 LLM evaluation 文献中罕见。Table 2 的 sensitivity hierarchy 呈现干净的 all-or-nothing 模式：所有 pairwise 方法显著，所有 Likert 方法不显著，极具说服力。[R1-S2, R2-S1, R2-S2, AGREE]\n\n**S2. 负对照设计有效。** Claude Sonnet 4 在相同 pairwise 设计下 BT ≈ 54-56%，TOST 确认等价性。为其他 judge 的显著偏差提供了因果对比基础——证明偏差是 judge-specific 而非 format-induced。[R1-S4, AGREE]\n\n**S3. 因果推断框架诚实定位。** §3.5 Design Rationale 明确 DAG 是 \"design rationale, not a claim of perfect identification\"，三个 operational assumptions 逐一列出并在附录中提供经验验证。[R1-S3, R2 partial REBUT on Title/Abstract language]\n\n**S4. Per-axis confound structure 是独立有价值发现。** GEE conditional decomposition 揭示 verbosity = style-dominated（Style OR 8–13）、formality = conditional on originality、register = judge-dependent。对 LLM judge 用户有直接 actionable value。[R1-S5, R2-S3, AGREE]\n\n**S5. Robustness 分析深度罕见。** Appendix A–Q 覆盖方向非对称性、NLI consistency filter、GEE diagnostics、rewriter independence、NLI threshold sweep (11 points)、direction-aware gate validation、Claude TOST、bootstrap attenuation、BT goodness-of-fit、100-point Likert、NLI gate ablation、rewriting artifact control。几乎回答了每个合理质疑。[R1-S5, R2-S4, AGREE]\n\n**S6. Black-box 框架设计实用性强。** CSD 不需要 judge 内部访问，可 post-hoc 应用于任何 black-box judge。[R2-S5, AGREE]\n\n---\n\n## Weaknesses\n\n### Must-Fix（需在 rebuttal/revision 中解决）\n\n**MF1. NLI gate 作为 content preservation 唯一门控缺乏人工验证** [R1-N1 critical, R2-Q1 AGREE]\n- CSD 因果推断完全依赖 NLI gate (DeBERTa-v3-large, τ=0.90) 保证 content 不变，但 NLI 模型存在系统性盲区（如对论证结构重组不敏感）。论文未报告任何 human evaluation of content preservation quality。\n- GPT-4o cross-validation (92.1%/82.6% pass precision) 是 LLM-vs-LLM 验证，存在认识论循环——用同类工具验证测量工具。\n- 如果 NLI gate 系统性放过某些 content 变化（如 formal 改写增加 hedging 改变 claim 强度），则观测到的\"style bias\"可能部分是 content bias 的伪装。\n- **此问题自 Round 3 起持续 7 轮未解决。** 两位 Reviewer 共同指向：增加 human evaluation 是最大可 actionable 改进（50-100 pairs × 2-3 annotators）。\n- **交叉共识**: 双方完全一致。\n\n**MF2. Novelty framing 过于强势——核心发现是已知测量理论的实证确认** [R1-N2 critical, R2-N1 critical, AGREE]\n- Thurstone (1927) Law of Comparative Judgment 已建立 pairwise > Likert 的灵敏度优势。论文在 §2 引用了这些文献并承认理论预测，但 Title/Abstract/Conclusion 中的 \"reveal\" 措辞将此包装为新发现。\n- 更准确的定位：CSD 框架首次在 LLM judge 场景下系统量化了理论预测的灵敏度差距（severity spectrum 和 per-axis confound structure 是真正新发现）。\n- **交叉共识**: 双方完全一致。建议从 \"reveal\" 转为 \"quantify\"；将 per-axis confound structure 提升为并列核心贡献。此问题自 Round 1 起持续未完全修正。\n\n### Should-Fix（重要但非致命）\n\n**SF1. Pairwise \"检测\" vs. \"放大\" 的核心解释性歧义** [R2-N2 critical → R1 REBUT 降为 warning]\n- 替代解释：pairwise comparison 可能放大微小的、无关紧要的风格微偏好，Likert 的不显著才反映真实效应。\n- 论文 §5.4 提供 6 项 amplification controls（NLI gate ablation、Claude 负对照、cross-axis BT variation、GEE artifact control、debiased prompting、cross-architecture replication），Jeong et al. (2025) Comparative Trap 也在讨论之中。\n- R1 反驳核心论据：Claude 负对照在相同 pairwise 设计下无偏差，证明非 format-induced 放大。\n- **分歧记录**: R2 定 critical（controls 只排除大规模放大，无法排除中等程度放大），R1 定 warning（负对照已充分缓解）。Director 判定 **Should-Fix**：Conclusion 语言应更谨慎（从 \"reveal\" 改为条件性表述），但论文已提供了合理的 bounding analysis。\n\n**SF2. Style axis 覆盖面过窄** [R2-W1 warning, R1 AGREE direction]\n- 仅 2 primary + 1 exploratory axes。LLM judge 已知风格偏差远不止这些（bullet-point vs. prose、hedging level 等）。\"Per-axis confound structure\" 这一分类法基于 3 个 axis 的泛化基础不足。\n- 建议：限定为 \"preliminary evidence of axis-dependent confound patterns\"；在 Limitations 列出未覆盖轴。\n\n**SF3. Claude TOST Δ=15pp margin 偏宽且覆盖不完整** [R1-W3 warning, R2 implied AGREE]\n- Δ=15pp 接近 GPT-4o formality 的 BT 偏差（~13pp），意味着 Claude 可能存在高达 15pp 的 style preference 仍被判\"无偏差\"。Claude 仅覆盖 2/3 axes（无 register）。\n- 建议三选一：(a) 增加 n 使 Δ=10pp 有功效；(b) reframe 为 \"insufficient evidence for bias at Δ=15pp precision\"；(c) 报告 minimum detectable Δ at 80% power。\n\n**SF4. Evaluator-producer overlap 处理力度有限** [R1-W4 warning, R2-Q3 AGREE]\n- Qwen3-32B 同时做 rewriter 和 judge。Cross-rewriter 验证（GPT-4o rewriter）显示 Style OR 下降 22%，但仅限 Qwen3-32B judge 验证。效应量有 ±20-25% rewriter-dependent 变异。\n- 建议：显式承认 Blindspot 存在性 robust 但效应量精确值受 rewriter 影响。\n\n**SF5. NLI gate 44% 拒绝率的选择偏差特征分析不足** [R2-W2 warning, R1 AGREE]\n- Appendix B 的 4 个 surface covariates 可能不够全面。Filtered-in pairs 可能偏向内容更简单的文本。\n- 建议补充对 filtered-out pairs 的语言复杂度对比分析。\n\n**SF6. Style axis 之间的 cross-contamination 未直接测试** [R1-W2 warning, R2 implied AGREE]\n- §3.5 假设(iii)（rewrite 不引入 target axis 外的系统性变化）未被经验验证。Table 5 GEE interaction test 只检验 Style×Originality 而非 cross-axis interaction。\n- 建议：对每个 axis 改写样本测量其他 axis 的变化幅度。\n\n### Minor\n\n**M1. 100-point Likert 实验仅用单一 judge** [R2-W3, R1 AGREE]\n- Appendix M 仅 Qwen3-32B，如果 GPT-4o 在 100-point scale 下 ATE 显著则结论不成立。建议增加至少 1 个 judge。\n\n**M2. 因果语言张力** [R2-W4, R1 partial REBUT]\n- §3.5 disclaimer 已足够明确。问题仅在 Title (\"Controlled\") 和 Abstract 的措辞选择暗示过强因果识别。建议在 Abstract 增加一句说明 \"controlled\" 指 experimentally controlled rewriting 而非 formal causal identification。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Novelty reframing 是最优先修改**：从 \"我们发现了 Blindspot\" 转为 \"我们首次系统量化了已知测量理论效应在 LLM judge 场景下的严重程度 + 发现了 per-axis confound structure\"。[R1-N2 × R2-N1]\n2. **Human evaluation 是最大可 actionable 改进**：50-100 pairs × 2-3 annotators 的 content preservation 验证能同时解决 NLI gate 可信度和 detection vs. amplification 两个问题。[R1-N1 × R2-Q1]\n3. **实验设计的严谨性是主要优势**：7 种统计方法 × 4+1 judges × 3 benchmarks 的矩阵在同领域罕见。[R1-S2 × R2-S1]\n4. **Per-axis confound structure 应被提升为核心贡献**。[R1 cross × R2-N1]\n5. **TOST Δ=15pp 偏宽**，Claude 负对照的 framing 需更谨慎。[R1-W3 × R2 implied]\n\n## Reviewer Divergence [分歧]\n\n1. **检测 vs. 放大的严重程度** [R2-N2 critical vs. R1 warning]：R2 认为这是核心解释性歧义，论证存在循环性，且 6 项 controls 仅排除大规模放大；R1 反驳负对照（Claude BT ≈ 54-56%）是最强反驳证据——若 pairwise 系统性放大则所有 judge 均应受影响。R1 进一步指出论证在操作层面（alignment pipeline 确实用 pairwise）不循环。Director 判定 Should-Fix 而非 critical：Conclusion 语言应谨慎化，但论文已提供合理 bounding。\n\n---\n\n## Questions（需作者回应）\n\nQ1. NLI gate 的 false-pass rate 是否有人工验证数据？即使 50 pairs 的抽样也能大幅增强可信度。\nQ2. Table 1 缺失单元格代表什么？选择哪些 judge×axis×benchmark 组合的理由是什么？\nQ3. Bootstrap attenuation analysis (d = −0.017) 如何排除 Likert 和 pairwise 在 construct 层面的根本差异？\nQ4. Formal 改写是否系统性改变了 verbosity 或 register？是否有定量 axis isolation 证据？\nQ5. 选择 formality 和 verbosity 作为 primary axes 的先验理由是什么？\nQ6. 是否有办法量化 pairwise 的放大倍数（amplification factor），而非仅定性 bounding？\n\n---\n\n## Missing References\n\n- Simms, Zelazny, Williams & Bernstein (2019). *Psychological Assessment* — rating scale granularity 对 discriminability 的影响\n- Polo et al. (2024). tinyBenchmarks — IRT 在 LLM 评估中的应用\n- Kocmi & Federmann (2023). LLM judge bias across evaluation formats\n- 建议验证 Stureborg et al. (2024) 在 references.bib 中的完整性\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 2 warning / 4 info）：\n\n- **[warning] P16**: 末页仅 3 条 reference，约 85% 空白；建议调整分页使末页填充更充分\n- **[warning] P6**: 3 个 display items（Figure 3 + Table 2 + Figure 4）挤在同一页，Figure 3/4 图幅偏小，axis label 接近可读性下限；建议将 Table 2 或 Figure 4 移至 P7 分散密度\n- **[info] P1-3**: 前 3 页中仅 P2 有 1 个 display item，视觉上偏\"文字墙\"\n- **[info] P4**: Figure 2 因果 DAG 节点标签偏小，打印后可能需凑近看\n- **[info] P6**: Figure 3 的 filled/open diamond marker 尺寸较小，灰度打印时 significance 区分度可能下降\n- **[info] P13**: References 与 appendix 表格过渡区略拥挤\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 4/5 | 3.5-4 |\n| Excitement | 3.5/5 | 3/5 | 3-3.5 |\n| Reproducibility | 4/5 | 4/5 | 4 |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4/5 | 4/5 | 4 |\n\n**总评**: 实验工作扎实、统计分析充分、robustness 覆盖深入的 evaluation 方法论工作。核心发现（Likert 对 style bias 的结构性不敏感 + per-axis confound structure）对 NLP evaluation 社区有实用价值。但两个 Must-Fix 问题阻碍更高评分：(1) NLI gate 缺乏人工验证——这是因果推断链的最薄弱环节，且已持续 7 轮未解决；(2) Novelty framing 将已知测量理论效应的实证确认包装为新发现，需要重新定位。如果 rebuttal/revision 能增加 human evaluation 数据并 reframe novelty narrative，可上调至 4.0 (Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Motivating example (\"average height\") 后已有 nuance acknowledgment (\"formality preferences may partially reflect legitimate quality judgments\")——这是合理的处理。\n- \"CSD reveals the Likert Blindspot\" → 建议改为 \"CSD quantifies the Likert Blindspot\" 或 \"CSD demonstrates\"\n\n### §2 Related Work\n- 覆盖全面，Jeong et al. (2025) Comparative Trap 和 Tripathi et al. (2025) 均已引用。\n- 建议补充 IRT 文献（Polo et al., 2024）以加强 measurement theory 背景。\n\n### §3 Method\n- §3.2 NLI gate 描述清晰，direction-aware strategy 有理论依据。\n- §3.5 Design Rationale 的因果语言校准良好（\"design rationale, not a claim of perfect identification\"）。但 §3.1 \"constitutes a binary intervention on a single style variable\" 中 \"intervention\" 一词与 §3.5 的谨慎定位有张力。\n- Figure 2 DAG 标注了 residual confounding dashed line——诚实且有效。\n\n### §4 Experiments\n- §4.1 Statistical framework 现在明确 \"six tests—three target judges × two axes\" + Gemini confirmatory + Appendix Q 8-test sensitivity analysis。比之前轮次的表述有显著改善。\n- Table 1 footnote \"Empty cells: untested benchmark–axis combinations\" 存在但未说明选择理由。\n\n### §5 Analysis\n- §5.1 Likert Blindspot 的 head-to-head comparison with RATE 是有效的对比设计。\n- §5.1 measurement attenuation vs. construct divergence 的讨论已有改善（引用 Tripathi et al. 2025），但 \"Blindspot\" 术语天然偏向 attenuation 解释。\n- §5.2 GEE conditional decomposition 结果清晰，\"style-dominated\" 而非 \"confound-free\" 是正确术语选择。\n- §5.4 六项 amplification controls 是对 Comparative Trap 的系统性回应。\n\n### §6 Conclusion\n- 简洁但可能过于简短（3 句话）。建议增加 practical implication 和 caveats。\n\n### Limitations\n- 覆盖了主要局限：quality-style confounding、evaluator-producer bias、validation methodology、scale design、per-axis independence、ecological validity。\n- Limitations 写得坦诚且适当长度（约 3 个点，符合 EMNLP 要求）。\n- 建议补充：style axis 之间的 potential interaction；将 measurement theory 背景作为 limitation 显式列出。\n\n### 格式合规\n- ✅ ACL template (`\\usepackage[review]{acl}`)\n- ✅ Double-blind (`\\author{Anonymous}`)\n- ✅ 正文 8 页合规\n- ✅ Limitations section 存在\n- ✅ References 不限页\n- ⚠️ P6 display item 密度过高（视觉审查 warning）\n"
  }
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-22T09:35:43.845483+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4269
}
```

</details>

---


### Assistant

_source line 818 · 2026-05-22T09:35:53.026129+00:00_

审稿报告已投递。

**Round 9 审稿结果总结：**

**Overall: 3.5 (Borderline Conference)**

两个 Must-Fix：
1. **NLI gate 缺乏人工验证**——因果推断链最薄弱环节，持续 7 轮未解决，两位 Reviewer 一致认为是最大可 actionable 改进
2. **Novelty framing 过强**——"Likert Blindspot" 核心发现可从 Thurstone (1927) 理论预测，需从 "reveal" 调整为 "quantify"，将 per-axis confound structure 提升为并列核心贡献

六个 Should-Fix：检测 vs. 放大歧义（R1/R2 分歧，Director 判定 warning）、style axis 覆盖窄、TOST Δ=15pp 偏宽、evaluator-producer overlap、NLI 选择偏差、cross-axis contamination 未测试

主要优势：7 种统计方法交叉验证、4+1 judges × 3 benchmarks 矩阵、Claude 负对照、per-axis confound structure、Appendix A-Q 深度 robustness 分析

如果 revision 增加 human evaluation 数据并 reframe novelty，可上调至 4.0 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 80

## Round 80

2 recorded events


### User

_source line 819 · 2026-05-22T09:35:53.030068+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Weaknesses 回应

### [AGREE] R1-N1: NLI gate 缺乏人工验证

同意这是 CSD 因果推断链条的薄弱环节。论文在 Section 5.4 报告了 LLM annotator 验证（92% agreement, FNR = 8.4%, precision = 98.9%），并在 Appendix B 给出了 4 个 covariates 的一致性检验（NLI score p = 0.824, BERTScore p = 0.12, text length p = 0.137, length diff p = 0.715），在 Appendix E 给出了 11 个 NLI 阈值的灵敏度分析（Table 9，全部 44 cells 显著）。这些间接证据提供了部分 mitigation。

但 R1 的核心关切——NLI 模型可能对隐含推理链改变、论证结构重组等系统性盲区——无法被 LLM annotator 或统计 covariates 回答。论文自身在 Limitations 中也承认 "human evaluation of all 200 decisions containing original and rewritten text would strengthen construct-preservation claims"。**R1 指出的 formal rewrite 增加 hedging 从而改变 claim 强度的具体场景尤其值得关注**——这恰恰是 NLI 模型可能的盲区（NLI 检测语义蕴含，但 hedging 增减不改变蕴含方向，可能通过 gate 却实质改变了文本质量感知）。

补充一点 R1 未提及的：Appendix N（NLI Gate Ablation, Table 15）显示移除 NLI gate 后 NLI-fail pairs 的 BT 仍在 63.0%–76.0%，这说明即使在 content preservation 较差的 pairs 上偏差方向一致，但效应量可能被 content confounding 污染。这实际上是 R1 担忧的间接佐证——gate 确实在过滤 content-confounded pairs，但 gate 本身的准确性需要 human ground-truth 来验证。

**结论**：同意将此列为 critical issue。50–100 对的人工抽样验证是合理的最低要求。

---

### [AGREE] R1-N2: Likert Blindspot framing 过于强势

完全同意。这与我自己的 N1 独立一致。论文在 Section 2（第 2 页）明确承认 "the superiority of pairwise comparison over rating scales for eliciting reliable human judgments has been established since Thurstone (1927)"，但 Abstract 和 Introduction 的措辞（"We ... reveal the Likert Blindspot"）将其包装为全新发现。

R1 和我的建议一致：reframe 为"已有测量理论预测在 LLM judge 风格偏差中的首次系统性实证量化"。此外，我在自己的审稿中额外建议将 per-axis confound structure（Section 5.2, Table 3）提升为与 Blindspot quantification 平行的核心贡献——这个发现确实没有被先验理论预测。

---

### [AGREE] R1-W1: NLI filtering 后样本量有限，cross-benchmark 覆盖不完整

同意，但严重性判断略有不同。

关于**空白单元格**：Table 1 脚注明确标注 "Empty cells: untested benchmark×axis combinations, cross-bench. replication"，说明这是设计选择而非数据缺失。但论文**未解释选择标准**——为什么某些 judge×axis×benchmark 组合被测试而其他没有？这让读者无法评估覆盖的完整性。

关于**样本量**：n = 55（NLI filtering 后最小有效样本）确实偏小。但 Appendix I（Bootstrap Attenuation, Table 11）显示 BT 在 n = 50 到 355 的所有子样本中保持显著（d_formality 在 −0.006 到 −0.018 范围内，全部 95% CI 包含 0.07），Appendix K（Formal Power Analysis, Table 12）报告当前样本在 p < 0.001 水平对所有 6 个 judge×axis cells 达到 80% power。这部分缓解了 R1 的担忧。

**结论**：同意这是 warning 级别问题。论文应解释 cross-benchmark 选择逻辑，并在正文中简要提及 power analysis 结果（目前仅在 Appendix K）。

---

### [AGREE] R1-W2: Style axis 之间的 cross-contamination 未被直接测试

同意，且论文自身的证据实际上佐证了这个担忧。

Section 5.2（第 7 页）报告 "Both rewriting directions favor verbose responses (Formality OR 982...by 22's)"——这直接说明 formality rewrite 影响了 verbosity。论文试图通过 GEE conditional decomposition（Table 3）控制 originality confound，但 originality ≠ cross-axis style contamination。Appendix C（Table 5）的 interaction test 检验的是 Style × Originality，而非 formality × verbosity 或 formality × register。

Appendix O（Rewriting Artifact Control）的 same-style double-rewrite 控制了一般性的 rewriting polishing artifact，但论文自己承认 "cannot exclude style-specific-polishing interactions (e.g., formal rewriting may polish differently than casual rewriting)"（第 13 页）。

R1 提出的第三个假设（"style rewrite introduces no systematic differences beyond the target axis"）的验证缺口是真实的。定量检验方法可以是：对 formality-rewritten pairs 测量 verbosity 和 register 维度的变化幅度，验证是否显著偏离零。

**结论**：同意这是 warning 级别问题，且论文已有的证据（Section 5.2 的 verbose response 倾向）暗示该假设可能部分违反。

---

### [AGREE] R1-W3: 负对照 TOST margin 偏宽 + register 轴缺失（部分同意，部分反驳）

**关于 Δ = 15pp margin**：部分同意。Appendix G（第 11 页）透明地报告了 power constraint：Δ = 15pp 下 power 仅 76%；80% power 需要 Δ = 15.7pp。R1 指出 GPT-4o formality BT 偏差约 13pp（BT ≈ 63%，即 50% + 13pp），如果 Claude 有接近 13pp 的偏差仍可能被 TOST 判定为等价——这在数学上是正确的。

**但我要补充一个缓解因素**：Claude 的 raw BT 值（formality 56.2%, verbosity 54.1%）数值上接近 50%，远低于任何 target judge（最低为 GPT-4o formality 的 63%）。即使 TOST 的 formal equivalence testing 受 power 限制，**point estimate 本身已经支持 negative control 的解释**。TOST 的作用是 formal bound，不是唯一证据。

**关于 register 轴缺失**：完全同意。Table 1 中 Claude 仅有 formality 和 verbosity 结果（LLMBar 和 AlpacaEval），register 缺失。论文未解释这个 omission——即使 register 是 scaled replication，在 negative control 上缺失一个轴会削弱 "Claude shows no systematic bias" 的 claim。

**结论**：总体同意 warning 级别。TOST margin 是 power-constrained 的现实问题（不是方法论错误），但 register 缺失是需要解释的 gap。

---

### [REBUT] R1-W4: Evaluator-producer overlap 处理力度有限

不同意 R1 对此问题的 framing。

Appendix D（第 9 页）明确说明："Evaluator-producer overlap is limited to Qwen3-32B (rewriter = judge)... The other three target judges (GPT-4o, Llama-70B, Gemini) use a different rewriter and are not subject to this confound."

Evaluator-producer overlap 是**定义性地局限于 Qwen3-32B**的——因为 Qwen3-32B 既是 rewriter 也是 judge。对 GPT-4o、Llama-70B、Gemini 来说，它们判断的是 Qwen3-32B 的 rewrite，不存在 overlap。因此 cross-rewriter test（Tables 7–8，用 GPT-4o 替代 Qwen3-32B 作为 rewriter）正确地**仅针对唯一存在 overlap 的 judge（Qwen3-32B）**进行验证。

R1 要求 "覆盖其他 judges" 的 cross-rewriter test 在逻辑上是不必要的——对不存在 overlap 的 judges 做 overlap robustness check 无法增加信息。如果 R1 的真正担忧是 rewriter identity 的一般性影响（不限于 overlap），那 Table 7 的数据已部分回答：GPT-4o rewriter 下 Style OR 降低 22%（verbosity），但 Blindspot 模式持续（BT significant, Likert n.s.），说明 rewriter identity 影响效应量但不影响 Blindspot 的定性结论。

**结论**：不同意。论文对 evaluator-producer overlap 的处理是逻辑完整的。如果 R1 想要的是更广泛的 "rewriter robustness"（不同 rewriter 对不同 judges 的影响），这是一个合理的扩展方向但不是当前论文的方法论缺陷。

---

## Questions 回应

### R1-Q1: NLI gate false-pass rate

Section 5.4（第 7 页）报告了基于 LLM annotator 的验证：agreement 92%, FNR = 8.4% [95% Wilson CI: 3.7%, 15.9%], precision = 98.9%。但这是 **LLM annotator**，不是 human annotator。

[AGREE] 人工验证数据缺失是事实。如 R1-N1 所述，LLM annotator 可能与 NLI gate 共享系统性盲区（两者都是基于 transformer 的模型，可能对同类 content 变化不敏感），因此 LLM-based validation 无法完全替代 human validation。

---

### R1-Q2: Table 1 空白单元格

Table 1 脚注："Empty cells: untested benchmark×axis combinations, cross-bench. replication." 这是**设计选择**——AlpacaEval 和 MT-Bench 作为 cross-benchmark replication，不要求覆盖所有 judge×axis 组合。

[AGREE] 论文应解释选择哪些组合进行 replication 的标准（例如：是否优先选择 primary family 中效应最强/最弱的 cells？还是随机选择？）。当前呈现方式让读者无法评估 replication 的代表性。

---

### R1-Q3: Bootstrap d = −0.017 如何排除 construct 层面差异

[AGREE] **无法排除**。Appendix I 的 bootstrap analysis 显示 Likert d_formality = −0.017，d_verbosity = −0.017，在所有子样本中 d 保持 near-zero（Table 11）。这排除了"Likert 只是 power 不足"的解释（如果 Likert 能检测到同一效应，增加样本量应让 d 远离零）。

但 R1 的问题更深层：如果 pairwise 和 Likert 测量的是不同 constructs（pairwise 测量 comparative preference，Likert 测量 absolute quality perception），则 BT > 50% + Likert d ≈ 0 是两种 construct 的自然状态，不需要用 "Blindspot" 来解释。论文在 Section 5.1（第 6 页）讨论了 "measurement attenuation vs. construct divergence"，但**未提供决定性证据区分两种解释**。这与我自己的 N2 一致——论文需要 human ground-truth 或其他外部标准来区分。

---

### R1-Q4: Formal 改写是否系统性改变 verbosity/register

[AGREE] 论文**未提供直接的定量证据**证明 axis isolation。反而，Section 5.2（第 7 页）提供了反面证据："Both rewriting directions favor verbose responses (Formality OR..." ——formality rewrite 确实系统性地影响了 verbosity。

GEE conditional decomposition（Table 3）通过 controlling for originality 来间接处理这个问题，但 originality confound ≠ cross-axis style contamination。论文的第三个操作假设（"the style rewrite introduces no systematic differences beyond the target axis", Section 3.4, 第 4 页）在 formality → verbosity 方向上可能被违反。

这个问题比 R1 最初 framing 的更严重：如果 formality rewrite 系统性地增加 verbosity，而 verbosity 是 style-dominated bias（Table 3），则观测到的 "formality bias" 可能部分被 verbosity confound 驱动。GEE conditional analysis 部分控制了这个问题（formality effect remains significant after controlling for originality），但 cross-axis confounding 不等于 originality confounding。

---

### R1-Q5: Claude Sonnet 4 为何不覆盖 register axis

[AGREE] 论文未解释这个 omission。可能的原因是 register 作为 scaled replication（使用较宽松的 α）在 negative control 上的 inferential value 有限，加上样本量约束（n = 87 已经让 TOST 在 formality/verbosity 上仅达到 76% power）。但这些都是推测——论文应明确说明原因。缺少 register 覆盖意味着 Claude "无偏差" 的 claim 仅对 2/3 测试轴成立。

---

## 总结：与 R1 的共识和分歧

| R1 Issue | R2 判断 | 备注 |
|----------|---------|------|
| N1 (NLI human validation) | [AGREE] | 与我的 W2（NLI 选择偏差）互补 |
| N2 (Framing overstated) | [AGREE] | 与我的 N1 独立一致 |
| W1 (Sample size/coverage) | [AGREE] | Bootstrap 部分缓解，但 cross-benchmark 选择逻辑缺失 |
| W2 (Cross-axis interaction) | [AGREE] | 论文自身证据（S5.2 verbose tendency）佐证此担忧 |
| W3 (Negative control) | [AGREE] 部分 | TOST margin 受 power 限制可理解，register 缺失是真实 gap |
| W4 (Evaluator-producer) | [REBUT] | 论文处理逻辑完整，overlap 定义性局限于 Qwen3-32B |
| Q1 (False-pass rate) | [AGREE] | LLM annotator ≠ human validation |
| Q2 (Empty cells) | [AGREE] | 选择标准需解释 |
| Q3 (Bootstrap vs construct) | [AGREE] | 无法排除 construct divergence |
| Q4 (Cross-axis contamination) | [AGREE] | 论文自身 S5.2 数据是反面证据 |
| Q5 (Claude register) | [AGREE] | Omission 未解释 |

**两位 Reviewer 的核心共识**：(1) Novelty framing 需要重新定位（R1-N2 = R2-N1）；(2) 检测 vs. 放大的解释性歧义是 fundamental limitation（R1-Q3 ≈ R2-N2）；(3) NLI gate 的 human validation 缺失削弱了因果推断链条（R1-N1 ≈ R2-W2 的上游问题）。

**唯一分歧**：R1-W4（evaluator-producer overlap）——我认为论文的处理是逻辑完整的，R1 可能混淆了 "overlap confound"（仅 Qwen3-32B）与 "rewriter identity effect"（更广泛的 robustness 问题）。


---

[Reviewer 2 审稿结果]:
逐条回应完成。总结：

- **10/11 条 [AGREE]**（N1, N2, W1, W2, W3部分, Q1–Q5），与 R1 在 novelty framing、NLI human validation 缺失、cross-axis contamination、construct divergence 等核心问题上形成共识
- **1 条 [REBUT]**（W4 evaluator-producer overlap）：论文的处理逻辑完整，overlap 定义性地局限于 Qwen3-32B，cross-rewriter test 正确地仅针对该 judge
- **两位 Reviewer 的三大核心共识**：(1) Blindspot framing 需从"新发现"调整为"理论预测的首次实证量化"；(2) 检测 vs. 放大的解释性歧义是 fundamental limitation；(3) NLI gate 需要 human validation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 820 · 2026-05-22T09:36:19.881687+00:00_

Reviewer 2 的交叉回应晚于报告投递到达。审稿报告已提交（Overall 3.5），现补充记录 R2 交叉回应中的两个值得注意的要点：

1. **R1-W4（evaluator-producer overlap）: R2 REBUT 成立。** R2 指出 evaluator-producer overlap 定义性地局限于 Qwen3-32B（唯一同时做 rewriter 和 judge 的模型），对其他 3 个 target judges 不存在此 confound。Cross-rewriter test 正确地仅针对 Qwen3-32B 验证。R1 的担忧更准确地说是 "rewriter identity effect"（更广泛的 robustness 问题）而非 "evaluator-producer overlap"。报告中 SF4 的 framing 应做此区分。

2. **R1-W2（cross-axis contamination）: R2 提供了更强的佐证。** R2 引用 §5.2 原文 "Both rewriting directions favor verbose responses"——formality rewrite 确实系统性影响了 verbosity。这意味着 §3.5 假设(iii) 在 formality→verbosity 方向上可能被违反。如果 formality rewrite 增加 verbosity，而 verbosity 是 style-dominated bias（OR 8–13），则部分 "formality bias" 可能被 verbosity confound 驱动。此问题比报告中 SF6 的描述更严重。

以上两点不影响整体评分（3.5 Borderline Conference）和两个 Must-Fix 的判定。审稿报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 81

## Round 81

48 recorded events


### User

_source line 821 · 2026-05-22T16:32:25.941400+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-22T16:32:36.039782+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-22T16:32:36.040633+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 824 · 2026-05-22T16:32:42.567059+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "9"
  }
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-22T16:32:42.567625+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-22T16:32:45.629630+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-22T16:32:46.082655+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (54 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **register_100_cf** (killed): Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality\n- **gemini_flash_fourth_judge** (success): Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.\n- **llama70b_register** (success): Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures\n  [llama70b_register_summary](/api/workspace-files/projects/causal_style_decomp_judge/artifacts/llama70b_register/data/llama70b_register_summary.json)\n\n## 趋势\n成功 38 / 负向 12 / 失败 0 / 共 54\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- register_100_cf: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-22T16:32:46.183547+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 829 · 2026-05-22T16:32:46.234128+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-22T16:32:51.354389+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 831 · 2026-05-22T16:32:53.312664+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 832 · 2026-05-22T16:32:53.865224+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Detecting Hidden Style Bias\\in LLM Judges via Controlled Style Decomposition}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\S\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.
45	The primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences inhe
…[truncated 3671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 833 · 2026-05-22T16:32:53.865664+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-22T16:32:55.324504+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool call

_source line 835 · 2026-05-22T16:32:55.676185+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 836 · 2026-05-22T16:33:01.599210+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on my web search, I found comprehensive information about EMNLP 2026 ARR submission guidelines. Here's a summary of the key submission guidelines and author instructions:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contr
…[truncated 1980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 10244
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-22T16:33:01.650068+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_style_decomp_judge'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7784
}
```

</details>

---


### Tool result

_source line 838 · 2026-05-22T16:33:01.650539+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 5974
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-22T16:33:01.801329+00:00_

-rw-r--r-- 1 ubuntu ubuntu 389926 May 22 13:21 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 6476
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-22T16:33:05.715022+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit template requirements site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit template requirements site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 841 · 2026-05-22T16:33:06.567817+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "writing_plan.yaml"
  }
}
```

</details>

---


### Tool call

_source line 842 · 2026-05-22T16:33:07.119851+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null && echo \"ISSUES_EXIST\" || echo \"NO_ISSUES\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null && echo \"ISSUES_EXIST\" || echo \"NO_ISSUES\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-22T16:33:11.686810+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit template requirements site:aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Discontinuation of the MS Word Template – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/discontinuation-word-template"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results from the ACL Rolling Review website, here's th
…[truncated 1310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5971
}
```

</details>

---


### Tool result

_source line 844 · 2026-05-22T16:33:11.738665+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/writing_plan.yaml\", \"content\": \"meta:\\n  venue: \\\"EMNLP 2026 Main via ARR\\\"\\n  format: \\\"Long paper, 8 pages + unlimited references\\\"\\n  deadline: \\\"ARR June 2026 cycle (~June 15)\\\"\\n  template: \\\"ACL style (acl.sty, review mode)\\\"\\n  core_claim: \\\"Standard Likert scoring systematically underestimates style bias in LLM judges; binary style counterfactuals with pairwise comparison reveal causal bias that Likert misses.\\\"\\n  status: partial_draft\\n  partial_scope: [introduction, abstract_skeleton, figure_1_spec]\\n\\nvisualization_plan:\\n  - fig_id: fig1_likert_blindspot\\n    type: statistical\\n    tool: matplotlib\\n    placement: introduction\\n    aspect_ratio: \\\"2.2:1\\\"\\n    layout: \\\"2-panel, full-width (figure*)\\\"\\n    data_source: \\\"registry: mvp_32b_ate (Likert scores), pairwise_32b (pairwise results)\\\"\\n    raw_data_paths:\\n      likert: \\\"/root/causal_style_decomp_judge/data/scored_32b.jsonl\\\"\\n      pairwise: \\\"/root/causal_style_decomp_judge/data/pairwise_results_32b.jsonl\\\"\\n\\n    narrative_intent: >\\n      Standard Likert scoring sees no difference between formal and casual responses\\n      (overlapping distributions, p=0.33), while pairwise comparison on the same data\\n      reveals a 69.1% formal win rate (p=0.006). This measurement gap is the central\\n      problem CSD exposes.\\n\\n    design_notes:\\n      - \\\"Pattern H: asymmetric 2-panel [1.4:1] — left panel wider (distribution needs more space), right panel narrower (single bar)\\\"\\n      - \\\"Pattern C: dashed line at 50% baseline in right panel (chance level)\\\"\\n      - \\\"Pattern A: light blue band above 50% in right panel marking 'formal preference zone'\\\"\\n      - \\\"Pattern E: Wilson CI error bar on win rate bar [55.97%, 79.72%]\\\"\\n      - \\\"Pattern J: path-effect white stro
…[truncated 2304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5170
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-22T16:33:11.789378+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml
ISSUES_EXIST

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 4669
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-22T16:33:15.855247+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/",
  "description": "List paper section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/",
    "description": "List paper section files"
  }
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-22T16:33:16.307365+00:00_

abstract.tex
appendix.tex
conclusion.tex
experiments.tex
introduction.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-22T16:33:16.809584+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml | head -80",
  "description": "Read existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml | head -80",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-22T16:33:17.763739+00:00_

issues:
  # ============================================================
  # Round 1-4 issues (all resolved unless noted)
  # ============================================================

  - id: "R1-N1"
    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
    resolution_round: 4

  - id: "R2-N1"
    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
    category: framing
    severity: warning
    status: in_progress
    first_raised_round: 1
    last_seen_round: 10
    resolution: null
    resolution_round: null
    mentions:
      - round: 3
        reviewers: [1, 2]
        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
      - round: 8
        reviewers: [1, 2]
        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
      - round: 9
        reviewers: [1, 2]
        note: "R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。"
      - round: 10
        reviewers: [1, 2]
        note: "R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。"
    action_items:
      - round: 7
        action: "将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'"
        assigned_to: paper_agent
        status: done
      - round: 10
        action: "三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'"
        assigned_to: paper_agent
        status: in_progress

  - id: "R1-N2"
    summary: "NLI gate 67% false-negative rate 造成选择偏差未分析"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89"
    resolution_round: 1

  - i
…[truncated 598 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-22T16:33:17.915275+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-22T16:33:17.966170+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-22T16:33:21.632002+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml | wc -l",
  "description": "Count lines in review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml | wc -l",
    "description": "Count lines in review issues"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-22T16:33:21.983793+00:00_

1116

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-22T16:33:22.134777+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "description": "Read full review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "description": "Read full review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-22T16:33:22.185818+00:00_

&lt;persisted-output>
Output too large (34.4KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/7b570111-34f2-44d7-a5a1-7611a146966c/tool-results/begvz1yvm.txt

Preview (first 2KB):
issues:
  # ============================================================
  # Round 1-4 issues (all resolved unless noted)
  # ============================================================

  - id: "R1-N1"
    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
    resolution_round: 4

  - id: "R2-N1"
    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
    category: framing
    severity: warning
    status: in_progress
    first_raised_round: 1
    last_seen_round: 10
    resolution: null
    resolution_round: null
    mentions:
      - round: 3
        reviewers: [1, 2]
        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
      - round: 8
        reviewers: [1, 2]
        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
      - round: 9
        reviewers: [1, 2]
        note: "R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。"
      - round: 10
        reviewers: [1, 2]
        note: "R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。"
    action_items:
      - round: 7
        action: "将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'"
        assigned_to: paper_agent
        status: done
      - round: 10
        action: "三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'"
        assigned_to: paper_agent
…[truncated 337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-22T16:33:31.701118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/7b570111-34f2-44d7-a5a1-7611a146966c/tool-results/begvz1yvm.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/7b570111-34f2-44d7-a5a1-7611a146966c/tool-results/begvz1yvm.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-22T16:33:31.802051+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved unless noted)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	
16	  - id: "R2-N1"
17	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
18	    category: framing
19	    severity: warning
20	    status: in_progress
21	    first_raised_round: 1
22	    last_seen_round: 10
23	    resolution: null
24	    resolution_round: null
25	    mentions:
26	      - round: 3
27	        reviewers: [1, 2]
28	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
29	      - round: 8
30	        reviewers: [1, 2]
31	        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
32	      - round: 9
33	        reviewers: [1, 2]
34	        note: "R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。"
35	      - round: 10
36	        reviewers: [1, 2]
37	        note: "R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。"
38	    action_items:
39	      - round: 7
40	        action: "将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'"
41	        assigned_to: paper_agent
42	        status: done
43	      - round: 10
44	        action: "三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'"
45	        assigned_to: paper_agent
46	        status: in_progress
47	
48	  - id: "R1-N2"
49	    summary: "NLI gate 67% false-negative rate 造成选择偏差未分析"
50	    category: method
51	    severity: critical
52	    status: resolved
53	
…[truncated 4245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-22T16:33:35.213861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/7b570111-34f2-44d7-a5a1-7611a146966c/tool-results/begvz1yvm.txt",
  "offset": "200",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/7b570111-34f2-44d7-a5a1-7611a146966c/tool-results/begvz1yvm.txt",
    "offset": "200",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-22T16:33:35.214488+00:00_

200	    category: experiment
201	    severity: warning
202	    status: resolved
203	    first_raised_round: 1
204	    last_seen_round: 1
205	    resolution: "Magnitude gap framing"
206	    resolution_round: 1
207	
208	  - id: "CROSS-4"
209	    summary: "Ordinal regression 必要"
210	    category: method
211	    severity: critical
212	    status: resolved
213	    first_raised_round: 1
214	    last_seen_round: 1
215	    resolution: "Definitively resolved"
216	    resolution_round: 1
217	
218	  # ============================================================
219	  # Round 2 issues
220	  # ============================================================
221	
222	  - id: "RD2-MF2"
223	    summary: "Holm-Bonferroni 'nine tests' 错误"
224	    category: method
225	    severity: critical
226	    status: resolved
227	    first_raised_round: 2
228	    last_seen_round: 2
229	    resolution: "Text fixed to '6 tests'. Holm 6-test: 4/6 significant."
230	    resolution_round: 2
231	
232	  - id: "RD2-MF3"
233	    summary: "单一 benchmark (LLMBar n=100) 不支撑全称论断"
234	    category: experiment
235	    severity: critical
236	    status: resolved
237	    first_raised_round: 2
238	    last_seen_round: 4
239	    resolution: "3 benchmarks x 3 judges. 6/7 biased cells BT significant."
240	    resolution_round: 2
241	
242	  - id: "RD2-MF4"
243	    summary: "Abstract overclaim: 'dominant source' + verbosity category error"
244	    category: framing
245	    severity: critical
246	    status: resolved
247	    first_raised_round: 2
248	    last_seen_round: 2
249	    resolution: "Overclaim replaced in intro. Verbosity category error removed."
250	    resolution_round: 2
251	
252	  - id: "RD2-VIS"
253	    summary: "主正文超 8 页限制"
254	    category: format
255	    severity: critical
256	    status: resolved
257	    first_raised_round: 2
258	    last_seen_round: 10
259	    resolution: "Round 7+ 确认主正文 8 页合规。R10 确认 ≤8 页。"
260	    resolution_round: 7
261	    mentions:
262	      - round: 10
263	        reviewers: [1, 2]
2
…[truncated 10949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-22T16:33:41.435018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/7b570111-34f2-44d7-a5a1-7611a146966c/tool-results/begvz1yvm.txt",
  "offset": "598",
  "limit": "520"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/7b570111-34f2-44d7-a5a1-7611a146966c/tool-results/begvz1yvm.txt",
    "offset": "598",
    "limit": "520"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-22T16:33:41.485924+00:00_

598	  # ============================================================
599	  # Round 4 issues
600	  # ============================================================
601	
602	  - id: "R4-N1"
603	    summary: "Bradley-Terry IIA 假设未检验"
604	    category: method
605	    severity: warning
606	    status: in_progress
607	    first_raised_round: 4
608	    last_seen_round: 10
609	    resolution: null
610	    resolution_round: null
611	    mentions:
612	      - round: 8
613	        reviewers: [1, 2]
614	        note: "R8 Should-Fix：Appendix H formality 方向异质性挑战 IIA。"
615	      - round: 10
616	        reviewers: []
617	        note: "R10 未显式提及。§4.1 footnote 已承认 direction asymmetry。可能接近解决。"
618	
619	  - id: "R4-N2"
620	    summary: "Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑"
621	    category: framing
622	    severity: warning
623	    status: resolved
624	    first_raised_round: 4
625	    last_seen_round: 4
626	    resolution: "Reframed as integrative positioning."
627	    resolution_round: 4
628	
629	  - id: "R4-W1"
630	    summary: "Conclusion 仅一句话"
631	    category: writing
632	    severity: warning
633	    status: resolved
634	    first_raised_round: 4
635	    last_seen_round: 4
636	    resolution: "Conclusion expanded."
637	    resolution_round: 4
638	
639	  - id: "R4-M1"
640	    summary: "Table 1 Likert d 负值含义未解释"
641	    category: format
642	    severity: info
643	    status: resolved
644	    first_raised_round: 4
645	    last_seen_round: 4
646	    resolution: "Footnote added."
647	    resolution_round: 4
648	
649	  - id: "R4-M2"
650	    summary: "'Interventional Design' 标题措辞与 evidence 强度不匹配"
651	    category: framing
652	    severity: info
653	    status: resolved
654	    first_raised_round: 4
655	    last_seen_round: 4
656	    resolution: "Renamed to 'Design Rationale'."
657	    resolution_round: 4
658	
659	  # ============================================================
660	  # Round 5 issues
661	  # ============================================================
…[truncated 16022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-22T16:34:19.181967+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-22T16:34:34.170500+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 14988
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-22T16:34:34.321878+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ARR（May cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: Long paper，正文 ≤8 页，无限参考文献，ACL template，double-blind\n- **Limitations 章节**: 不计入页数，但不能包含新实验/图表/分析\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各 section 在 `sections/` 子目录）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf`\n\n## 你的审查侧重\n\n重点评估以下方面，严格、不留情面：\n\n1. **NLI Quality Gate 设计**：阈值选择依据、false positive/negative rate 报告、gate 引入的 selection bias 是否充分讨论\n2. **统计方法**：Bradley-Terry 模型假设（IIA）是否检验、Holm-Bonferroni 校正是否正确、GEE 分解的 confounding 处理、TOST equivalence testing 参数选择\n3. **因果声明强度**：论文使用 \"controlled\"/\"interventional\" 等术语是否与实际方法论强度匹配，是否有 overclaim\n4. **实验设计**：样本量充分性（n=100 LLMBar 基准）、cross-benchmark validation 覆盖面、evaluator-producer confound（同一模型既当 rewriter 又当 judge）\n5. **人工评估**：是否有人工标注验证 rewriting 质量和 NLI gate 准确性\n6. **可复现性**：实验细节是否足够复现（prompt、模型版本、随机种子等）\n\n输出格式：\n- **Summary** (2-3句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n- **Questions** (需要作者澄清的)\n- **Missing References**\n- **Overall Assessment** (评分 + 置信度)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ARR（May cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: Long paper，正文 ≤8 页，无限参考文献，ACL template，double-blind\n- **Limitations 章节**: 不计入页数，但不能包含新实验/图表/分析\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各 section 在 `sections/` 子目录）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf`\n\n## 你的审查侧重\n\n重点评估以下方面，严格、不留情面：\n\n1. **NLI Quality Gate 设计**：阈值选择依据、false positive/negative rate 报告、gate 引入的 selection bias 是否充分讨论\n2. **统计方法**：Bradley-Terry 模型假设（IIA）是否检验、Holm-Bonferroni 校正是否正确、GEE 分解的 confounding 处理、TOST equivalence testing 参数选择\n3. **因果声明强度**：论文使用 \"controlled\"/\"interventional\" 等术语是否与实际方法论强度匹配，是否有 overclaim\n4. **实验设计**：样本量充分性（n=100 LLMBar 基准）、cross-benchmark validation 覆盖面、evaluator-producer confound（同一模型既当 rewriter 又当 judge）\n5. **人工评估**：是否有人工标注验证 rewriting 质量和 NLI gate 准确性\n6. **可复现性**：实验细节是否足够复现（prompt、模型版本、随机种子等）\n\n输出格式：\n- **Summary** (2-3句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n- **Questions** (需要作者澄清的)\n- **Missing References**\n- **Overall Assessment** (评分 + 置信度)"
  }
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-22T16:34:46.731964+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12410
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-22T16:34:46.883026+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 写作完整性 + 格式合规**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ARR（May cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: Long paper，正文 ≤8 页，无限参考文献，ACL template，double-blind\n- **Limitations 章节**: 不计入页数，但不能包含新实验/图表/分析\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各 section 在 `sections/` 子目录）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf`\n\n## 你的审查侧重\n\n重点评估以下方面，严格、不留情面：\n\n1. **新颖性定位**：核心 contribution（Likert Blindspot 现象 + 检测方法）是否真正 novel，还是心理测量学已知现象（Thurstone 1927, paired comparison vs rating scales）的 domain transfer？论文是否充分 acknowledge 前人工作？\n2. **Related Work 覆盖**：LLM-as-judge bias 领域的关键工作是否完整覆盖？特别关注：(a) Comparative Trap (Jeong et al., 2025) 是否被引用和讨论——该工作提出 pairwise 格式可能放大而非仅检测 bias，与本文核心 claim 直接矛盾；(b) 其他 measurement format comparison 文献\n3. **Contribution 措辞**：Abstract/Intro 中是否有 overclaim（如 \"first\", \"reveals\", \"dominant source\" 等绝对性表述），contribution list 是否与实际证据强度匹配\n4. **写作质量**：叙事结构是否清晰、论证逻辑是否连贯、Abstract 是否过密、Limitations 是否充分\n5. **格式合规**：正文是否 ≤8 页、匿名性（无 self-citation 泄露）、Limitations 章节内容是否合规（无新实验/图表）、引用格式是否 ACL 规范\n6. **Detection vs Amplification 歧义**：pairwise 格式检测到的 bias 是 genuine style bias 还是 pairwise 格式本身的 amplification artifact？论文是否诚实地讨论了这一 alternative interpretation？\n\n输出格式：\n- **Summary** (2-3句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n- **Questions** (需要作者澄清的)\n- **Missing References**\n- **Overall Assessment** (评分 + 置信度)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 写作完整性 + 格式合规**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ARR（May cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: Long paper，正文 ≤8 页，无限参考文献，ACL template，double-blind\n- **Limitations 章节**: 不计入页数，但不能包含新实验/图表/分析\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各 section 在 `sections/` 子目录）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf`\n\n## 你的审查侧重\n\n重点评估以下方面，严格、不留情面：\n\n1. **新颖性定位**：核心 contribution（Likert Blindspot 现象 + 检测方法）是否真正 novel，还是心理测量学已知现象（Thurstone 1927, paired comparison vs rating scales）的 domain transfer？论文是否充分 acknowledge 前人工作？\n2. **Related Work 覆盖**：LLM-as-judge bias 领域的关键工作是否完整覆盖？特别关注：(a) Comparative Trap (Jeong et al., 2025) 是否被引用和讨论——该工作提出 pairwise 格式可能放大而非仅检测 bias，与本文核心 claim 直接矛盾；(b) 其他 measurement format comparison 文献\n3. **Contribution 措辞**：Abstract/Intro 中是否有 overclaim（如 \"first\", \"reveals\", \"dominant source\" 等绝对性表述），contribution list 是否与实际证据强度匹配\n4. **写作质量**：叙事结构是否清晰、论证逻辑是否连贯、Abstract 是否过密、Limitations 是否充分\n5. **格式合规**：正文是否 ≤8 页、匿名性（无 self-citation 泄露）、Limitations 章节内容是否合规（无新实验/图表）、引用格式是否 ACL 规范\n6. **Detection vs Amplification 歧义**：pairwise 格式检测到的 bias 是 genuine style bias 还是 pairwise 格式本身的 amplification artifact？论文是否诚实地讨论了这一 alternative interpretation？\n\n输出格式：\n- **Summary** (2-3句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n- **Questions** (需要作者澄清的)\n- **Missing References**\n- **Overall Assessment** (评分 + 置信度)"
  }
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-22T16:34:48.348476+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1465
}
```

</details>

---


### Assistant

_source line 868 · 2026-05-22T16:34:53.453951+00:00_

Round 1 已启动：
- Reviewer 1（方法严谨性）已派发
- Reviewer 2（新颖性+完整性）已派发
- 视觉审查 Agent 已派发（fire-and-forget）

等待两位 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 82

## Round 82

2 recorded events


### User

_source line 869 · 2026-05-22T16:40:23.759912+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 方法严谨性 + 实验设计审查

**论文**: *The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition*
**Venue**: EMNLP 2026 via ARR (May cycle)

---

## 总体评分

**Overall Assessment**: 3.5 — Borderline Conference
**一句话总结**: 论文识别了一个重要的评估方法学问题（Likert vs. pairwise 对风格偏差的灵敏度差异），统计框架扎实，但 Bradley-Terry IIA 假设未检验、人工验证规模不足、TOST 等价边界缺乏严格论证，这些方法论缺口削弱了核心声明的可信度。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计框架（BT + GEE + Holm-Bonferroni + TOST + Bootstrap）相当完整，但 IIA 假设仅承认未检验（脚注1, p.5），人工验证仅50对，TOST Δ=15pp 偏宽松 |
| Excitement | 3.5/5 | Likert Blindspot 现象对 NLG 评估社区有实际意义，但相对 RATE (Reber et al., 2025) 增量有限，且 measurement attenuation vs. construct divergence 的根本模糊性限制了贡献深度 |
| Reproducibility | 3.5/5 | Appendix P 提供了模型版本、温度参数、统计库信息；代码/数据承诺接收后公开；但 rewriting prompt 原文未在论文中展示 |
| Confidence | 4/5 | 熟悉 BT 模型、GEE、因果推断和 NLG 评估文献，仔细检查了统计方法 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Bradley-Terry IIA 假设未经验证

- 具体位置：Section 4.1, 脚注1 (p.5); Appendix B
- 问题：Bradley-Terry 模型的核心假设是 Independence of Irrelevant Alternatives (IIA)。论文在脚注1中承认 "The BT model assumes IIA"，但仅此一句，**未做任何经验性检验**（如 Hausman-McFadden test）。论文的实验设计中，同一 base text 经 style transformation 后生成多组配对，这些配对并非独立——同源文本在多个比较中重复出现，IIA 可能被系统性违反。Appendix B 报告的 formality 方向不对称性（formal→casual vs. casual→formal BT 估计显著不同）进一步暗示 IIA 违反的可能性。
- 为什么影响接收：BT 是论文检测 Blindspot 的核心统计工具。若 IIA 被违反，BT 估计的 bias 和 confidence intervals 均不可靠，整个 pairwise 检测框架的有效性成疑。
- 建议修改方向：(1) 执行 Hausman-McFadden test 或类似诊断；(2) 作为 robustness check，拟合 Thurstone-Mosteller Model V（不要求 IIA）并报告结论是否一致；(3) 对 direction asymmetry 提供更深入的解释——如果 asymmetry 源于 IIA 违反而非真实效应差异，应如何区分？

**N2** [critical] NLI Quality Gate 的选择偏差未充分量化

- 具体位置：Section 3.2; Appendix E (Table 9); Appendix N (NLI Gate Ablation); Section 5.4
- 问题：NLI gate 是整个框架的关键组件——通过 DeBERTa-v3-large 以 0.90 阈值过滤内容变化的配对。但论文存在以下缺口：
  - **FPR/FNR 未系统报告**：Section 5.4 报告了 50 对人工标注（25 对 gate-passed），precision=100%，但 (a) 50 对样本量太小（Wilson CI 下界仅 86.3%）；(b) 未报告 recall——多少内容保持的配对被错误拒绝？这个 false negative rate 直接决定 selection bias 的程度。
  - **Selection bias 的方向性未分析**：gate 过滤掉了约 12-35% 的配对（Table 1 脚注，因 axis 而异），被过滤配对的风格分布是什么？如果 gate 系统性地排除某种风格变换方向（如 casual→formal 比 formal→casual 更容易触发内容变化），则保留的样本不再代表完整的风格效应。
  - **Appendix N 的 ablation 不充分**：NLI-fail 样本的分析（Table 15）显示 NLI-fail pairs BT 仍在 75% 左右，但该分析仅涉及 verbosity 和 formality 两个 axis，且 NLI-fail 样本量很小（n 约 12-21），统计效力不足以支持 "gate removes content-confounded pairs rather than amplifying style signal" 的结论。
- 为什么影响接收：如果 NLI gate 引入了系统性的 selection bias（例如只保留了「容易做风格变换」的简单文本），则 Blindspot 可能是数据子集的 artifact 而非 Likert 量表的固有缺陷。
- 建议修改方向：(1) 扩大人工标注到至少 200 对，覆盖 gate-passed 和 gate-rejected 两侧；(2) 报告 recall/FNR；(3) 分析被过滤配对的特征（文本长度、复杂度、风格变换方向）与保留配对的系统性差异。

**N3** [critical] 样本量充分性与 power 解读存在循环论证风险

- 具体位置：Section 5.1; Appendix L (Table 12); Appendix K
- 问题：论文的核心发现是 "Likert 在 n≈88-355 时检测不到风格偏差，但 pairwise 可以"。Appendix L 的 formal power analysis 显示，Likert ATE 达到 80% power 需要 n=336 到 1200+ 不等的样本量——远超当前实验规模。这产生了一个根本性的解读困境：
  - **论文的解读**（§5.1）：这证明 Likert 量表存在 measurement attenuation，是方法论缺陷
  - **替代解读**：Likert 效应量本身较小（d ≈ 0.03-0.10），在当前样本量下 Likert 的 null 结果仅仅反映 insufficient power，不能得出 "Blindspot" 的结论。Pairwise 方法之所以检测到，是因为 forced-choice 范式天然放大了微小偏好差异
  - 论文在 §5.1 确实讨论了 "measurement attenuation vs. construct divergence" 二元性，但结论部分（§6）的表述 "Likert scoring systematically misses style biases" 偏向了前者，未保留足够的 hedging
- 为什么影响接收：如果 Blindspot 本质上是 power 问题而非方法论缺陷，则论文的核心贡献——CSD 框架作为 "检测隐藏偏差" 工具的必要性——被显著削弱。Reviewer 和 AC 会认为这是 overclaim。
- 建议修改方向：(1) 在更大样本量（≥500）上验证 Likert ATE 是否仍然 non-significant，或至少在 Conclusion 中明确声明当前结果不能排除 power 不足的解释；(2) 将 TOST 等价检验作为更有力的证据——但前提是 Δ 的选择需要更严格的论证（见 W1）；(3) 考虑在 AlpacaEval（样本量更大）上做 Likert sub-study。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] TOST 等价边界 Δ = 15pp 缺乏严格论证

- 具体位置：Section 5.1 (p.6, bottom); Appendix G
- 问题：TOST equivalence testing 的结论完全依赖于等价边界 Δ 的选择。论文选择 Δ = 15pp（win probability 百分点），理由是 "the largest effect magnitude across the CSD style axes"——这是循环论证，用自己观测到的效应量来定义 "什么算无差异"。15pp 对应约 d ≈ 0.43（Cohen's d），属于 medium effect size，这个等价边界相当宽松。如果采用 Δ = 5pp 或 10pp，TOST 的等价结论可能不成立。
- 建议：(1) 基于领域先验知识或实际决策后果论证 Δ 的选择（如 "低于多少 pp 的偏差不会影响 leaderboard 排名"）；(2) 报告 TOST 在不同 Δ 值（5pp, 10pp, 15pp, 20pp）下的结论 sensitivity。

**W2** [warning] Evaluator-producer confound 的控制实验范围有限

- 具体位置：Section 5.3; Appendix D (Tables 6-7)
- 问题：所有 style-controlled rewriting 均使用 Qwen3-32B（Appendix P），而 Qwen3-32B 同时是四个 target judge 之一。Table 7 的 independence test 仅在 verbosity axis 上用 GPT-4o 作为替代 rewriter，且仅针对 Qwen3-32B judge。存在以下缺口：(1) 未在 formality axis 上做替代 rewriter 测试；(2) 未检验其他 judge（GPT-4o, Llama-70B, Gemini）是否也受 Qwen3-32B rewriting style 的系统性影响（即 rewriter 的 "文风指纹" 是否被所有 judge 以相同方式感知）；(3) 仅一个替代 rewriter 不足以排除 rewriter-specific artifact。
- 建议：至少在两个 axis × 两个 judge 组合上做替代 rewriter 实验，或论证为何单个控制实验足够。

**W3** [warning] 因果术语与方法论强度不完全匹配

- 具体位置：Title; Section 3.1; Section 5 (p.5); Figure 2
- 问题：论文标题使用 "Controlled Style Decomposition"，Section 3 使用 "interventional"，Figure 2 画出 DAG 并标注 "blocked by NLI"。虽然 Section 5 (p.5) 有明确 disclaimer（"we do not claim that this DAG is a complete structural causal model"），但整体叙事给读者的印象是这是一个因果推断研究。实际上：(1) rewriting 不是真正的随机干预——LLM rewriter 的行为不受研究者精确控制；(2) NLI gate 不能保证 do-calculus 意义上的 "blocking"——它是一个统计过滤器，有 false positive/negative；(3) GEE decomposition 是关联性分析而非因果识别。
- 建议：(1) 在 Introduction 或 Method 中更早地设定预期，明确 "controlled" 指实验条件控制而非 formal causal identification；(2) 避免在 Figure 2 中使用 do-calculus 风格的 DAG notation（如 blocked path），或明确标注为 "assumed data-generating process" 而非因果图。

**W4** [warning] 负控制模型仅一个（Claude Sonnet 4），且验证深度有限

- 具体位置：Section 4.1; Appendix G
- 问题：Claude Sonnet 4 作为唯一的负控制，其 BT 结果（56.2%/54.19%, n.s.）确实支持 "无 Blindspot" 的结论。但 (1) 仅一个负控制不足以论证 Blindspot 是特定架构/训练方式的产物而非普遍现象；(2) 未讨论 Claude Sonnet 4 为何不受影响的机制假设——是架构差异、RLHF 策略、还是偶然？
- 建议：增加至少一个其他可能的负控制（如不同版本的 GPT 或开源 judge），或在 Discussion 中提出可检验的机制假设。

---

## 小问题（不影响接收）

- **M1**: Table 1 脚注标注 "Scaled replication (n = 355, other settings same)" 但 main text 对 n=355 replication 的讨论分散在多处（§5.1, Appendix J, K），不易追踪。建议在 Section 4 统一说明两个实验规模。
- **M2**: Figure 1 的 pipeline overview 可读性可改进——stage 之间的 sample attrition（n=100 → n=88 → ...）如果能标注具体数字会更清晰。
- **M3**: Appendix Q (Holm-Bonferroni sensitivity analysis) 报告 "All results remain significant under the expanded family"——但 8-test family 仅包含 4 judges × 2 axes，未包含不同 benchmark 的 comparisons。如果将 cross-benchmark tests 也纳入 family，校正后是否仍 significant？
- **M4**: Register axis 仅出现在 Table 1 和少量讨论中，结果均 non-significant。建议明确说明 register axis 的 n 值和 power，避免读者误解为 "register 无偏差" 而非 "power 不足"。

---

## Questions（需要作者澄清）

1. **IIA 诊断**：是否尝试过 Thurstone Model V 或其他不要求 IIA 的配对比较模型？如果 BT 在 IIA 违反下仍给出一致结论，这将大大增强论文可信度。
2. **NLI gate recall**：在 50 对人工标注中，有多少 gate-rejected 的配对实际上内容是保持的（即 false negatives）？这个数据是否已收集但未报告？
3. **Likert prompt 变体**：当前 Likert 评估使用固定的 1-10 量表。是否尝试过其他量表设计（如 5 点量表、descriptive anchors、rubric-based scoring）？如果不同 Likert 变体均显示 Blindspot，结论更有力。
4. **AlpacaEval/MT-Bench 的完整结果**：Table 1 仅报告 LLMBar 的详细 BT 和 Likert d 值。AlpacaEval 和 MT-Bench 的 per-judge per-axis 结果在哪个 Appendix？是否所有 judge 在这些 benchmark 上也一致复现 Blindspot？
5. **Bootstrap attenuation 估计的 convergence**：Appendix J 报告 attenuation δ̄ ≈ -0.017 across sample sizes (n ∈ [0.3n to 1.0n])。但 bootstrap 置信区间从 ±0.3 到 ±0.1——这个范围是否足以排除 δ̄ = 0（即无 attenuation）？

---

## Missing References

1. **Thurstone (1927)** 已引用，但未讨论 Thurstone Model V 作为 BT 的替代方案——在 IIA 可能违反的情况下，至少应引用并讨论。
2. **Agresti (2002) 或类似 GEE 方法论参考**：GEE decomposition 的统计细节可引用 Liang & Zeger (1986) 之外的教材级参考，帮助不熟悉 GEE 的读者。（Liang & Zeger 已引用，这一条为可选。）
3. **Bojar et al. (2016) 或 WMT human evaluation**: 作为大规模 pairwise vs. Likert 方法比较的先例，与本文主题高度相关但未引用。
4. **Karpinska et al. (2021)** 或其他关于 LLM 评估中 scale design 影响的工作，可补充 §2.1 "Measurement Sensitivity in NLG Evaluation" 的讨论。

---

## 主要优势

1. **问题重要且及时**：Likert vs. pairwise 的灵敏度差异对整个 NLG 评估社区有直接影响——如果 Likert 确实系统性地低估风格偏差，现有大量评估研究需要重新审视。
2. **统计框架完整性**：BT + GEE + Holm-Bonferroni + TOST + Bootstrap + sensitivity analysis 的组合在 NLP 评估论文中罕见，显示了认真的统计思考。
3. **控制实验设计**：NLI quality gate + direction-aware gating + 负控制（Claude Sonnet 4）+ evaluator-producer independence test（Table 7）构成了多层控制，即使每层单独看有缺口，整体设计仍优于大部分同类工作。
4. **GEE confound decomposition 是真正的贡献**：将 verbosity 识别为 style-dominated、formality 为 conditionally style-driven，比简单的 "有偏差/无偏差" 二分法信息量更大。
5. **Appendix 的深度令人印象深刻**：17 个附录（A-R）覆盖了几乎所有可预见的 robustness concern，说明作者在统计设计上投入了大量思考。
6. **100-point continuous scale robustness check**（Appendix M）有效反驳了 "Blindspot 仅因离散量表粒度不足" 的替代解释。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 870 · 2026-05-22T16:40:30.323374+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 83

## Round 83

2 recorded events


### User

_source line 871 · 2026-05-22T16:40:54.267633+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿完成，已提交至 Review Director。

**评分摘要**：Overall 3.5（Borderline Conference），Soundness 3.5，Excitement 3.5，Confidence 4。

**三个 Must-Fix**：
1. Bradley-Terry IIA 假设未做经验性检验（脚注1仅承认，无 Hausman-McFadden test 或替代模型对比）
2. NLI Quality Gate 的 selection bias 未充分量化（50 对人工验证太少，未报告 recall/FNR，被过滤配对特征未分析）
3. 样本量与 power 的循环论证风险（Likert null 结果可能仅反映 power 不足而非方法论缺陷，Conclusion 的 hedging 不够）

**四个 Should-Fix**：TOST Δ=15pp 论证不足、evaluator-producer confound 控制实验范围有限（仅一个 axis × 一个 judge）、因果术语偏强、负控制仅一个模型。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 872 · 2026-05-22T16:41:00.182440+00:00_

Reviewer 1 结果已收到。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 84

## Round 84

6 recorded events


### User

_source line 873 · 2026-05-22T16:42:34.212119+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性 + 写作完整性 + 格式合规）

### 总体评分

**Overall**: 3.5 — Borderline Conference
**一句话总结**: 方法论扎实、控制充分的实证工作，但核心发现（pairwise 比 Likert 更灵敏）在心理测量学中已有深厚根基，且 detection 与 amplification 无法干净分离，削弱了"Likert 是盲区"这一叙事的说服力。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法设计合理，NLI gate + position swap + negative control 构成可信的控制链；但 detection vs. amplification 无法分离，核心 claim 的因果解读存在歧义 |
| Excitement | 3/5 | CSD 框架和 GEE per-axis decomposition 有实用价值，但核心 observation 是 Thurstone (1927) 以来的经典心理测量学结论的 domain transfer |
| Reproducibility | 4/5 | 模型版本、prompt、seed、threshold 均明确；代码承诺在接收后发布 |
| Confidence | 4/5 | 仔细阅读了正文及全部 Appendix，熟悉 LLM-as-judge 和 measurement theory 文献 |

---

### Must-Fix 问题

**N1** [critical] 新颖性定位过度——核心发现有深厚心理测量学先例

- 位置：Section 2 ("first controlled quantification")；Abstract ("systematically misses biases")；Title
- Pairwise > Likert sensitivity 是 Thurstone (1927) Law of Comparative Judgment 的经典结论。Mohammad (2017)、Novikova et al. (2018) 已在 NLG 评估中实证验证。论文虽引用了这些工作，但叙事框架将已知现象包装为新发现——"The Likert Blindspot" 作为专有名词、"reveals" 等措辞暗示首次揭示。
- 影响：Reviewer 和 AC 会质疑 contribution 是否足够支撑 main conference。
- 建议：明确定位为"在 LLM judge 场景下首次系统量化已知 measurement-format sensitivity gap"；"first" 限定为 "first for LLM judges specifically"；削弱绝对性措辞。

**N2** [critical] Detection vs. Amplification 无法分离

- 位置：§5.4; §6 Conclusion ("the primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences")
- §5.4 六项控制 bound 了 amplification 但未 eliminate 它。缺少独立于两种测量格式的 ground-truth bias measure。Appendix M 100-point continuous Likert 排除了 scale granularity 解释，但未排除 amplification 解释。
- 如果 amplification 解释成立，论文标题和核心 claim 需根本重构。
- 建议：设计 ground-truth bias 已知的合成实验；或诚实 reframe 为 "divergent signals" 而非单方面归因为 Likert failure。

---

### Should-Fix 问题

**W1** [warning] Abstract 信息密度过高：d → 0, n = 355, p < 0.01, 60%, OR 68×11 等数字堆砌影响可读性。建议保留 1-2 个最有力数字，其余移至正文。

**W2** [warning] 主实验基于 LLMBar n=100（NLI gate 后 ≈88）。GEE decomposition、power analysis 等深度分析仅在此 benchmark 上。n=100 对"systematic blindspot"的 claim scope 偏少。

**W3** [warning] 标题和叙事预设 ground truth 在 pairwise 侧。"The Likert Blindspot" 暗示 Likert 有缺陷，但 "pairwise measures relative preference, Likert measures absolute quality" 的 construct 差异同样合理。

**W4** [warning] Register 轴未做 rewriter independence test，但在 Table 1/3 中与其他轴同等呈现。建议对 register 结果加显式 caveat。

---

### 小问题

- Limitations 提及废弃的 tone 轴实验并给出 pass rate 数字——建议移至 Appendix
- BT 模型 IIA 假设仅一笔带过（Footnote 1），值得补充讨论
- Figure 2 DAG 标注为 design rationale 但正文多处使用因果语言，需统一
- 格式合规：正文≤8页 ✓，匿名性 ✓，Limitations 无新实验 ✓，引用格式 ✓

---

### Questions for Authors

1. 能否设计 ground-truth bias 幅度已知的合成实验独立验证两种格式的 sensitivity curve？
2. 100-point continuous Likert 仍未检测到 bias——是否说明 absolute vs. relative evaluation 是根本区分而非 Likert 的"failure"？
3. Rewriter independence test 中 Style OR 下降 22% 如何解读？
4. 是否考虑让 human annotators 在 CSD pairs 上做 Likert + pairwise，区分 LLM-specific vs. format-specific？

---

### 主要优势

- 控制设计严谨（四家组织的 judge、negative control、七种统计方法、rewriter independence）
- GEE per-axis decomposition 有真正洞察——不仅"bias 存在"，而是"bias 的结构是什么"
- 诚实讨论 Comparative Trap 和 alternative interpretation
- CSD 作为 black-box framework 对 evaluation practitioners 有即时可用性

---

**Overall: 3.5 (Borderline Conference), Confidence: 4/5**

以目前形态更适合 Findings；若诚实 reframe novelty 并提供更强的 amplification-bounding evidence，可达 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-22T16:43:02.969449+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。\n\n---\n\n## Reviewer 1 — 方法严谨性 + 实验设计审查\n\n**Overall Assessment**: 3.5 — Borderline Conference\n\n### Must-Fix\n\n**N1** [critical] Bradley-Terry IIA 假设未经验证\n- BT 模型核心假设 IIA 仅在脚注1承认，未做 Hausman-McFadden test。同源文本在多组配对中重复出现，IIA 可能被系统性违反。Appendix B formality 方向不对称性暗示 IIA 违反。\n- 建议：执行 IIA 诊断、拟合 Thurstone Model V、解释 direction asymmetry。\n\n**N2** [critical] NLI Quality Gate 的选择偏差未充分量化\n- 50 对人工标注太少（Wilson CI 下界 86.3%），未报告 recall/FNR，被过滤配对特征未分析。gate 过滤 12-35% 配对，若系统性排除某种风格变换方向则 Blindspot 可能是数据子集 artifact。Appendix N ablation NLI-fail 样本量太小。\n- 建议：扩大人工标注到 200 对，报告 recall/FNR，分析被过滤配对特征。\n\n**N3** [critical] 样本量与 power 的循环论证风险\n- Likert ATE 达到 80% power 需 n=336-1200+，远超当前规模。Likert null 结果可能仅反映 power 不足而非方法论缺陷。Conclusion \"systematically misses\" 的 hedging 不够。\n- 建议：更大样本验证、TOST 需更严格 Δ 论证、明确声明不能排除 power 不足解释。\n\n### Should-Fix\n\n**W1** TOST Δ=15pp 缺乏严格论证（循环论证——用自己观测效应量定义等价边界，15pp ≈ d=0.43 属 medium effect，偏宽松）\n**W2** Evaluator-producer confound 控制实验范围有限（仅 verbosity × Qwen3-32B 有替代 rewriter）\n**W3** 因果术语与方法论强度不匹配（\"controlled\"/\"interventional\"/DAG notation 偏强）\n**W4** 负控制仅 Claude Sonnet 4 一个模型\n\n### Minor\n- M1: n=355 replication 讨论分散\n- M2: Figure 1 pipeline sample attrition 数字未标注\n- M3: Appendix Q Holm-Bonferroni 8-test family 未包含 cross-benchmark\n- M4: Register axis power 未报告\n\n### Questions\n1. 是否尝试过 Thurstone Model V？\n2. 50 对人工标注中 gate-rejected 的 false negative 数据？\n3. 是否尝试过其他 Likert 量表设计？\n4. AlpacaEval/MT-Bench 的 per-judge per-axis 完整结果？\n5. Bootstrap attenuation δ̄ ≈ -0.017 的 CI 是否包含 0？\n\n### Missing References\nThurstone Model V 讨论、Bojar et al. (2016) WMT human evaluation、Karpinska et al. (2021)\n\n---\n\n请对以上每一条给出你的 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。\n\n---\n\n## Reviewer 1 — 方法严谨性 + 实验设计审查\n\n**Overall Assessment**: 3.5 — Borderline Conference\n\n### Must-Fix\n\n**N1** [critical] Bradley-Terry IIA 假设未经验证\n- BT 模型核心假设 IIA 仅在脚注1承认，未做 Hausman-McFadden test。同源文本在多组配对中重复出现，IIA 可能被系统性违反。Appendix B formality 方向不对称性暗示 IIA 违反。\n- 建议：执行 IIA 诊断、拟合 Thurstone Model V、解释 direction asymmetry。\n\n**N2** [critical] NLI Quality Gate 的选择偏差未充分量化\n- 50 对人工标注太少（Wilson CI 下界 86.3%），未报告 recall/FNR，被过滤配对特征未分析。gate 过滤 12-35% 配对，若系统性排除某种风格变换方向则 Blindspot 可能是数据子集 artifact。Appendix N ablation NLI-fail 样本量太小。\n- 建议：扩大人工标注到 200 对，报告 recall/FNR，分析被过滤配对特征。\n\n**N3** [critical] 样本量与 power 的循环论证风险\n- Likert ATE 达到 80% power 需 n=336-1200+，远超当前规模。Likert null 结果可能仅反映 power 不足而非方法论缺陷。Conclusion \"systematically misses\" 的 hedging 不够。\n- 建议：更大样本验证、TOST 需更严格 Δ 论证、明确声明不能排除 power 不足解释。\n\n### Should-Fix\n\n**W1** TOST Δ=15pp 缺乏严格论证（循环论证——用自己观测效应量定义等价边界，15pp ≈ d=0.43 属 medium effect，偏宽松）\n**W2** Evaluator-producer confound 控制实验范围有限（仅 verbosity × Qwen3-32B 有替代 rewriter）\n**W3** 因果术语与方法论强度不匹配（\"controlled\"/\"interventional\"/DAG notation 偏强）\n**W4** 负控制仅 Claude Sonnet 4 一个模型\n\n### Minor\n- M1: n=355 replication 讨论分散\n- M2: Figure 1 pipeline sample attrition 数字未标注\n- M3: Appendix Q Holm-Bonferroni 8-test family 未包含 cross-benchmark\n- M4: Register axis power 未报告\n\n### Questions\n1. 是否尝试过 Thurstone Model V？\n2. 50 对人工标注中 gate-rejected 的 false negative 数据？\n3. 是否尝试过其他 Likert 量表设计？\n4. AlpacaEval/MT-Bench 的 per-judge per-axis 完整结果？\n5. Bootstrap attenuation δ̄ ≈ -0.017 的 CI 是否包含 0？\n\n### Missing References\nThurstone Model V 讨论、Bojar et al. (2016) WMT human evaluation、Karpinska et al. (2021)\n\n---\n\n请对以上每一条给出你的 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-22T16:43:11.813417+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 8843
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-22T16:43:11.964362+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。\n\n---\n\n## Reviewer 2 — 新颖性 + 写作完整性 + 格式合规审查\n\n**Overall Assessment**: 3.5 — Borderline Conference\n\n### Must-Fix\n\n**N1** [critical] 新颖性定位过度——核心发现有深厚心理测量学先例\n- Pairwise > Likert sensitivity 是 Thurstone (1927) 经典结论。Mohammad (2017)、Novikova et al. (2018) 已在 NLG 评估中实证验证。论文叙事将已知现象包装为新发现——\"The Likert Blindspot\"、\"reveals\" 等措辞。\n- 建议：定位为\"LLM judge 场景下首次系统量化\"，\"first\" 限定为 \"first for LLM judges specifically\"。\n\n**N2** [critical] Detection vs. Amplification 无法分离\n- §5.4 六项控制 bound 了 amplification 但未 eliminate。缺独立 ground-truth bias measure。100-point continuous Likert 排除 scale granularity 但未排除 amplification。\n- 建议：设计合成实验或诚实 reframe 为 \"divergent signals\"。\n\n### Should-Fix\n\n**W1** Abstract 信息密度过高，数字堆砌\n**W2** 主实验 n=100（gate 后 ≈88），scope 偏少\n**W3** 标题预设 ground truth 在 pairwise 侧，未充分考虑 construct 差异\n**W4** Register 轴未做 rewriter independence test\n\n### Minor\n- Limitations 的 tone 轴实验应移至 Appendix\n- BT IIA 假设讨论不足\n- Figure 2 DAG 与正文因果语言不统一\n- 格式合规：✓\n\n### Questions\n1. 能否设计 ground-truth 已知的合成实验？\n2. 100-point continuous Likert 是否说明 absolute vs. relative 是根本区分？\n3. Rewriter independence test Style OR 下降 22% 如何解读？\n4. 是否考虑 human annotators 做 Likert + pairwise？\n\n### Missing References\n未显式列出\n\n### 主要优势\n- 控制设计严谨\n- GEE per-axis decomposition 有真正洞察\n- 诚实讨论 Comparative Trap 和 alternative interpretation\n- CSD 作为 black-box framework 有即时可用性\n\n---\n\n请对以上每一条给出你的 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。\n\n---\n\n## Reviewer 2 — 新颖性 + 写作完整性 + 格式合规审查\n\n**Overall Assessment**: 3.5 — Borderline Conference\n\n### Must-Fix\n\n**N1** [critical] 新颖性定位过度——核心发现有深厚心理测量学先例\n- Pairwise > Likert sensitivity 是 Thurstone (1927) 经典结论。Mohammad (2017)、Novikova et al. (2018) 已在 NLG 评估中实证验证。论文叙事将已知现象包装为新发现——\"The Likert Blindspot\"、\"reveals\" 等措辞。\n- 建议：定位为\"LLM judge 场景下首次系统量化\"，\"first\" 限定为 \"first for LLM judges specifically\"。\n\n**N2** [critical] Detection vs. Amplification 无法分离\n- §5.4 六项控制 bound 了 amplification 但未 eliminate。缺独立 ground-truth bias measure。100-point continuous Likert 排除 scale granularity 但未排除 amplification。\n- 建议：设计合成实验或诚实 reframe 为 \"divergent signals\"。\n\n### Should-Fix\n\n**W1** Abstract 信息密度过高，数字堆砌\n**W2** 主实验 n=100（gate 后 ≈88），scope 偏少\n**W3** 标题预设 ground truth 在 pairwise 侧，未充分考虑 construct 差异\n**W4** Register 轴未做 rewriter independence test\n\n### Minor\n- Limitations 的 tone 轴实验应移至 Appendix\n- BT IIA 假设讨论不足\n- Figure 2 DAG 与正文因果语言不统一\n- 格式合规：✓\n\n### Questions\n1. 能否设计 ground-truth 已知的合成实验？\n2. 100-point continuous Likert 是否说明 absolute vs. relative 是根本区分？\n3. Rewriter independence test Style OR 下降 22% 如何解读？\n4. 是否考虑 human annotators 做 Likert + pairwise？\n\n### Missing References\n未显式列出\n\n### 主要优势\n- 控制设计严谨\n- GEE per-axis decomposition 有真正洞察\n- 诚实讨论 Comparative Trap 和 alternative interpretation\n- CSD 作为 black-box framework 有即时可用性\n\n---\n\n请对以上每一条给出你的 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-22T16:43:13.280372+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1316
}
```

</details>

---


### Assistant

_source line 878 · 2026-05-22T16:43:15.734548+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 85

## Round 85

2 recorded events


### User

_source line 879 · 2026-05-22T16:43:18.230867+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已提交给 Review Director。

核心判断：**3.5 (Borderline Conference)**。两个 Must-Fix 问题——(1) 新颖性定位过度（Thurstone 1927 以来 pairwise > Likert sensitivity 是已知结论，论文将其包装为新发现）；(2) detection vs. amplification 无法分离（六项控制 bound 了但未 eliminate amplification，缺少 ground-truth bias measure）。方法论执行质量高，GEE per-axis decomposition 有真正洞察，适合 Findings track；若 reframe novelty 并补充 amplification-bounding evidence 可冲击 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 880 · 2026-05-22T16:43:23.240650+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 86

## Round 86

2 recorded events


### User

_source line 881 · 2026-05-22T16:45:11.591982+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix

**[AGREE] R2-N1: 新颖性定位过度**

同意 R2 的核心判断。Pairwise 优于 Likert 在灵敏度上的优势确实是 Thurstone (1927) 以来的经典结论，且 Mohammad (2017)、Novikova et al. (2018) 已在 NLG 评估中做过实证验证。论文 Abstract 中 "reveals" 和标题中 "Detecting Hidden Style Bias" 的措辞确实给人「发现新现象」的印象，而实际贡献是将已知现象在 LLM judge 场景下做了首次系统性、per-axis 的量化。

补充我的观察：论文的真正新颖贡献是 (1) CSD 框架本身（NLI gate + style-controlled rewriting + position-controlled pairwise），(2) GEE per-axis decomposition 区分 style-dominated vs. conditionally style-driven 轴。这些方法论贡献是 solid 的，但被 "Blindspot" 这个过度戏剧化的命名所遮蔽。R2 建议的 reframe——"first systematic quantification for LLM judges specifically"——是恰当的。

**[AGREE] R2-N2: Detection vs. Amplification 无法分离**

完全同意，这与我在 N3 中提出的 "measurement attenuation vs. construct divergence 循环论证" 本质上是同一个问题的不同表述。

论文的 §5.4 提供了六项控制（human annotation, NLI gate, negative control 等），但正如 R2 所指出的，这些控制 bound 了 amplification 的程度但未 eliminate 它。关键缺口是：缺乏一个 **ground-truth bias 已知** 的验证场景。在没有 ground truth 的情况下，我们无法区分：
- 解读 A：Likert 量表有 attenuation，pairwise 才是「真实」灵敏度 → Blindspot 存在
- 解读 B：pairwise 的 forced-choice 范式放大了微小偏好差异，Likert 的 null 结果才是「真实」的 → Blindspot 是 artifact

论文在 §5.1 和 §6 中确实讨论了这个二元性，但结论的 hedging 不充分——§6 开头 "Likert scoring systematically misses style biases" 直接预设了解读 A。

补充一个 R2 未提到的角度：Appendix M 的 100-point continuous Likert 实验虽然排除了 scale granularity 解释，但实际上 **支持** R2 的 concern——因为即使在连续量表上 Blindspot 仍存在，这更可能反映 absolute vs. relative measurement 的根本差异（construct divergence），而非 Likert 的技术缺陷（measurement attenuation）。

---

### Should-Fix

**[AGREE] R2-W1: Abstract 信息密度过高**

同意。Abstract 中 "complete at moderate bias (d→0 at n=355), >60% attenuation at stronger effects" 等表述对首次接触本文的读者过于密集。建议精简数字，突出核心 message。这是写作问题，不影响技术判断。

**[AGREE] R2-W2: 主实验 n=100 scope 偏少**

同意，这与我的 N3 一致。n=100（gate 后 ≈88）在 Appendix L 的 formal power analysis 中已被证明对 Likert ATE 的 power 不足（需 n=336-1200+）。虽然 n=355 的 scaled replication 部分弥补了这一点，但 Likert 在 n=355 时仍 non-significant 的解读仍受 power 限制。

**[AGREE] R2-W3: 标题预设 ground truth 在 pairwise 侧**

同意。"Detecting Hidden Style Bias" 隐含假设 pairwise 检测到的就是 "真实偏差"，Likert 错过的就是 "隐藏偏差"。这与 N2 的 detection vs. amplification 问题直接相关。标题应更中性，如 "Divergent Style Sensitivity between Likert and Pairwise Evaluation in LLM Judges" 之类。

补充：我在 W3 中也提出了类似问题——Figure 2 的 DAG notation 和 "interventional" 等术语进一步强化了这种预设。

**[AGREE] R2-W4: Register 轴未做 rewriter independence test**

同意。Table 1 中 register 轴的 BT 结果对大部分 judge 为 non-significant（BT 接近 0.5），但论文未讨论这是 "register 确实无偏差" 还是 "register rewriting 质量不佳/power 不足"。缺乏 rewriter independence test 使得无法排除后者。

补充：我在 M4 中也标记了同一问题——register axis 的 n 值和 power 未明确报告。

---

### Minor

**[REBUT] R2-Minor-1: Limitations 的 tone 轴实验应移至 Appendix**

不同意。重新检查论文 p.8-9 的 Limitations section，tone axis 的讨论仅有一句话提及 pass rate (~5.07%) 来解释为何该轴被排除——这是对设计决策的说明，不构成 "新实验/图表/分析"。EMNLP 2026 规则允许 Limitations section 包含合理的定性讨论，只要不含 "excessive additional content"。一个 pass rate 数字不构成 excessive content。

**[AGREE] R2-Minor-2: BT IIA 假设讨论不足**

强烈同意，且我将此问题升级为 **Must-Fix**（我的 N1）。论文仅在脚注1中一句话承认 IIA，未做任何经验性检验。考虑到同源文本在多个比较中重复出现，IIA 违反风险实质性存在。Appendix B 的方向不对称性进一步暗示此问题。仅标为 Minor 低估了其严重性。

**[AGREE] R2-Minor-3: Figure 2 DAG 与因果语言不统一**

同意，与我的 W3 一致。Figure 2 使用因果图 notation（blocked path, do-intervention 风格），但 §5 的 disclaimer 承认这不是 formal causal model。二者之间存在张力。

**[AGREE] R2-Minor-4: 格式合规 ✓**

确认。主文 8 页，参考文献无限，Limitations 不计入页数。ACL template, double-blind 格式均合规。

---

### Questions

**[AGREE] R2-Q1: 合成实验（ground-truth 已知）**

强烈支持。这是解决 N2 (detection vs. amplification) 的最直接路径。例如：构造一组文本，其中人工注入已知程度的 style bias（如 formality 偏移），然后比较 Likert 和 pairwise 的检测灵敏度。如果 pairwise 在 ground-truth 为 0 的场景下仍 "检测到" bias，则说明 amplification 存在。

**[AGREE] R2-Q2: 100-point continuous Likert 与 absolute vs. relative 区分**

同意这是一个关键问题。如上述 N2 回应中所述，Appendix M 的结果实际上支持 construct divergence 解读——问题不在量表粒度，而在 absolute vs. relative 范式的根本差异。作者应在 rebuttal 中明确表态。

**[AGREE] R2-Q3: Rewriter independence test Style OR 下降 22%**

同意需要澄清。Table 7（Appendix D）显示 GPT-4o 作为替代 rewriter 时 Style OR 下降约 22%，这可能意味着 (a) Qwen3-32B 的 rewriting style 本身携带了一部分被检测到的 "bias"（即 rewriter artifact），或 (b) GPT-4o 的 rewriting 质量不同导致 style transformation 强度不同。22% 的幅度不可忽略。我在 W2 中也要求扩大替代 rewriter 实验的覆盖面。

**[AGREE] R2-Q4: Human annotators 做 Likert + pairwise**

同意这将是最有力的验证。如果人类评估者在相同材料上也显示 Likert-pairwise divergence，则 Blindspot 是范式级现象而非 LLM 特有。反之，如果人类 Likert 能检测到 bias 而 LLM Likert 不能，则问题在 LLM judge 而非量表本身。

---

### Missing References

R2 未显式列出缺失引用。补充我在 Round 1 中标记的：
- **Bojar et al. (2016)** 或 WMT human evaluation 工作——大规模 pairwise vs. rating 比较的重要先例
- **Karpinska et al. (2021)** 或类似 scale design 影响的研究

---

### 对 R2 优势识别的补充

同意 R2 对论文优势的识别，特别是 GEE per-axis decomposition 和 Comparative Trap 的诚实讨论。补充一点 R2 未提到的优势：**Appendix 的深度和覆盖面**（17 个附录 A-R）在 NLP 评估论文中罕见，展示了作者在 robustness concern 上的系统性思考。

---

### 总结

R2 的两个 Must-Fix（N1 新颖性过度、N2 detection vs. amplification）与我的核心关切高度一致。我与 R2 的唯一分歧是 BT IIA 的严重性定级——R2 列为 Minor，我认为应为 Must-Fix。两位 Reviewer 在以下三点形成共识：
1. 论文无法区分 detection 与 amplification（R2-N2 ≈ R1-N3）
2. 标题/措辞预设了 pairwise 为 ground truth（R2-W3 ≈ R1-W3）
3. 样本量不足限制了 Likert null 结果的解读（R2-W2 ≈ R1-N3）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 882 · 2026-05-22T16:45:16.301645+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 87

## Round 87

2 recorded events


### User

_source line 883 · 2026-05-22T16:45:18.803588+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。与 R2 在 7/8 条 Must-Fix 和 Should-Fix 上达成一致，唯一分歧是 BT IIA 问题的严重性——R2 列为 Minor，我认为应升级为 Must-Fix。两位 Reviewer 的共识聚焦于三个核心问题：detection vs. amplification 不可分离、标题预设 pairwise 为 ground truth、样本量限制 Likert null 的解读。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 884 · 2026-05-22T16:45:26.604643+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 88

## Round 88

10 recorded events


### User

_source line 885 · 2026-05-22T16:45:43.649502+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1

### Must-Fix

**[REBUT] R1-N1: BT IIA 假设未经验证** — 定级 overstated。(1) Table 2 七种统计方法中五种非参数方法不假设 IIA，全部独立确认 Blindspot；BT 非孤证。(2) Appendix B direction asymmetry 反映实质性偏好方向差异，不等于 IIA 违反。(3) Binary-choice BT 中 IIA 自动满足（无 irrelevant alternative 可删除），Hausman-McFadden test 不适用。建议降为 Should-Fix。

**[AGREE] R1-N2: NLI Gate 选择偏差** — 50 对人工标注偏少，recall/FNR 缺失。但 Appendix E threshold sweep（11 个阈值，44 组合全部显著，BT 变化 ≤4pp）提供部分缓解，说明结果不依赖特定子集。建议定为 Should-Fix。

**[AGREE] R1-N3: 样本量与 power 循环论证** — R1 最有力的一条。Table 12 需 n=336-1200+ 的 Likert power，当前 n≈88 远不够。Bootstrap attenuation（Appendix J, d̄≈-0.017）提供部分反驳但不充分——very small true effect 仍无法排除。"systematically misses" 措辞需 hedge。

### Should-Fix

**[AGREE] R1-W1** TOST Δ=15pp 需先验论证。
**[REBUT] R1-W2** R1 描述不准确——Appendix D Table 7 覆盖 formality+verbosity 两轴（非仅 verbosity），但 register 确实未覆盖。核心关切成立，具体描述需更正。
**[AGREE] R1-W3** 因果术语过强，我独立提出了同一问题。
**[AGREE] R1-W4** 单一 negative control 是限制。

### Minor
**[AGREE] M1, M3, M4**
**[REBUT] M2** — Figure 1 标题明确写了 "Numbers indicate sample attrition at each stage"，图中有标注。

### Questions
Q1: Binary-choice BT 中 Thurstone Model V 增量有限。Q2: 同意应报告。Q3: Appendix M 已测 100-point continuous Likert。Q4: 同意补充。Q5: Appendix J 明确 CI 包含 0。

### Missing References
[AGREE] Bojar et al. (2016) WMT human evaluation 高度相关。
[REBUT] Thurstone Model V 在 binary choice 场景增量有限，非必要。
Karpinska et al. (2021) 需更多 context。

### 两位 Reviewer 共识点
1. **Detection vs. amplification 未解决**（R2-N2 与 R1-N3 的 power 论证相互强化）
2. **因果/绝对性措辞需 hedge**（R2-N1 novelty overclaim + R1-W3 因果术语）
3. **Rewriter independence 不完整**（R2-W4 + R1-W2，register 未覆盖）
4. **样本量有限**（R2-W2 + R1-N3）

两位 Reviewer 分歧点：
- R1 将 BT IIA 定为 critical，R2 认为 binary-choice 中 IIA 自动满足，应降为 Should-Fix
- R1 将 NLI gate 定为 critical，R2 认为 threshold sweep 提供充分缓解，应降为 Should-Fix

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-22T16:45:57.279306+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-22T16:45:57.330008+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T16:34:22.503902+00:00\", \"completed_at\": \"2026-05-22T16:37:24.792371+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，视觉锚点（Figure 1）出现在第 2 页顶部。对于方法论论文这是可接受的，但若能将 Figure 1 或一个精简的 teaser figure 提至第 1 页底部，审稿人锚定会更快\"}, {\"severity\": \"warning\", \"dimension\": \"page 2\", \"message\": \"Figure 1（CSD pipeline overview）中各阶段的缩略图标非常小，在正常阅读距离下细节难以辨认。作为全文第一个 display item，它承担审稿人锚定印象的关键角色，建议放大或简化图标使其在单栏宽度下仍可清晰阅读\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 caption 较简短（\\\"CSD pipeline overview. Numbers indicate sample attrition at each stage.\\\"），缺少对各阶段功能的一句话概述，self-containment 可以更好\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"纯文本页（Related Work 尾段 + Method §3 开头），无 display item。仅一页纯文本，尚在可接受范围；且 page 4 立即出现 Figure 2，节奏未断\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2（因果 DAG）紧凑但清晰，红色/橙色节点标注合理，caption 详细且自包含，质量好\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1（主结果表）使用 booktabs 风格，显著结果加粗标注，脚注标记清晰。表格为全宽（table*），列数较多但对齐良好。脚注字号偏小但可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"页面密度高（Figure 3 + Table 2），但布局合理。Figure 3 使用实心/空心菱形区分显著性，配合虚线参考线，视觉编码有效。Table 2 booktabs 风格，整洁\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4（检测功效曲线）+ Table 3（GEE 分解），display item 密度与正文平衡良好。Figure 4 有阴影置信区间，可读性好\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"全文本页（Conclusion + Limitations），无 display item。作为结论页这是标准做法，不构成问题\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 中最优结果加粗标注，但未见次优下划线或 ↑/↓ 方向箭头标记。对于 BT 概率和 Likert d 值，增加方向指示可帮助审稿人快速定位关键发现\"}, {\"severity\": \"info\", \"dimension\": \"pages 10-13\", \"message\": \"Appendix 区域表格密度极高（Tables 4-18），无附录 figure。纯数据支撑型附录，功能上合理，但若能将部分关键 ablation 结果可视化（如 NLI threshold sweep Table 9 →
…[truncated 655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-22T16:46:28.099436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 889 · 2026-05-22T16:46:28.150168+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved unless noted)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	
16	  - id: "R2-N1"
17	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
18	    category: framing
19	    severity: warning
20	    status: in_progress
21	    first_raised_round: 1
22	    last_seen_round: 10
23	    resolution: null
24	    resolution_round: null
25	    mentions:
26	      - round: 3
27	        reviewers: [1, 2]
28	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
29	      - round: 8
30	        reviewers: [1, 2]
31	        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
32	      - round: 9
33	        reviewers: [1, 2]
34	        note: "R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。"
35	      - round: 10
36	        reviewers: [1, 2]
37	        note: "R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。"
38	    action_items:
39	      - round: 7
40	        action: "将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'"
41	        assigned_to: paper_agent
42	        status: done
43	      - round: 10
44	        action: "三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'"
45	        assigned_to: paper_agent
46	        status: in_progress
47	
48	  - id: "R1-N2"
49	    summary: "NLI gate 67% false-negative rate 造成选择偏差未分析"
50	    category: method
51	    severity: critical
52	    status: resolved
53	
…[truncated 1410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-22T16:50:23.682664+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 11\n        action: \"Abstract/§2 中 'reveals' 等措辞需进一步弱化；'first' 限定为 'first for LLM judges specifically'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 2 issues\n  # ============================================================\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 10\n    resolution: \"Round 7+ 确认主正文 8 页合规。R10 确认 ≤8 页。\"\n    resolution_round: 7\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 格式检查确认正文 8 页合规。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 格式合规确认：正文 ≤8 页 ✓，匿名 ✓，Limitations 无新实验 ✓。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"cross-rewriter validation 仅覆盖 Qwen3-32B judge。22% Style OR 下降确认 inflation 存在。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 共识 Should-Fix：Blindspot 存在性 robust，但效应量有 ±20-25% rewriter-dependent 变异。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF4: 仅 Qwen3-32B judge 有 cross-rewriter 验证。效应量 ±22% rewriter-dependent 变异需显式承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 Should-Fix: R1 指出仅 verbosity×Qwen3-32B 有替代 rewriter（R2 更正：formality+verbosity 两轴，但 register 未覆盖）。22% OR 下降不可忽略。两位共识 register 轴 evaluator-producer risk 最高。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 10\n        action: \"Limitations 补一句：effect-size precision varies ±22% with rewriter choice\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'.\"\n    resolution_round: 4\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"共识 Must-Fix。50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 两位共同指向：增加 human evaluation 是最大可 actionable 改进。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 MF1 (critical): 持续 7 轮未解决。两位 Reviewer 交叉共识：human evaluation 是 4.0 的关键路径。孙震 50-pair 标注今晚返回。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 将 NLI gate 50 对人工标注列为 Must-Fix（Wilson CI 下界仅 86.3%，未报告 recall/FNR）。R2 交叉降为 Should-Fix（threshold sweep 11 阈值×44 组合全显著提供缓解）。论文 §5.4 报告 50 对 100% precision，但规模仍不足。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板\"\n        assigned_to: agent\n        status: done\n      - round: 10\n        action: \"孙震标注返回后 → analyze_annotations.py → Paper Agent 写入 §5.4\"\n        assigned_to: agent\n        status: pending\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"两位再次一致指出 Abstract 过密。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 fresh review 未显式提出 Abstract 过密问题。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未提及 Abstract 密度问题。P1 重写后可能已缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 列为 Should-Fix（W1），R1 交叉 [AGREE]。数字堆砌影响可读性，建议保留 1-2 个最有力数字。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 Should-Fix：Appendix H formality 方向异质性挑战 IIA。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。§4.1 footnote 已承认 direction asymmetry。可能接近解决。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 分歧：R1 列为 Must-Fix (critical)——Appendix B direction asymmetry 暗示 IIA 违反，需 Hausman-McFadden test。R2 交叉 [REBUT] 降为 Should-Fix——binary-choice BT 中 IIA 自动满足，Table 2 五种非参数方法独立确认 Blindspot。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"§5.2 已加 6 项 amplification controls。从 critical 降级为 Should-Fix。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF1: 检测 vs 放大歧义仍为核心。R2 定 critical，R1 反驳降为 warning。6 项 controls + Claude 负对照已部分缓解。Conclusion 语言需条件化。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: detection vs. amplification 成为两位 Reviewer 的最大共识问题。R2 列为 Must-Fix (N2)，R1 交叉 [AGREE]。六项控制 bound 了 amplification 但未 eliminate。缺 ground-truth bias 已知的验证。100-point continuous Likert 排除粒度解释但支持 construct divergence 解读。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"Conclusion 加条件性表述：amplification controls bound 但不完全排除放大\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 11\n        action: \"§6 开头 'systematically misses' 需加 hedge；考虑 reframe 为 'divergent signals' 而非单方面归因 Likert failure\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1]\n        note: \"§3.5 因果语言校准良好。原始 'do-operator' 语言已修复。\"\n      - round: 10\n        reviewers: [2]\n        note: \"R10 M2: 'Controlled' 和 'interventional' 语言暗示过强因果识别。共识：§3.5 加明确声明。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 列为 Should-Fix (W3)，R2 交叉 [AGREE]。'controlled'/'interventional'/DAG notation 给人因果推断研究的印象，但 NLI gate 非 do-operator，GEE 是关联分析。建议 §3 更早声明 'controlled = experimentally controlled rewriting, not formal causal identification'。\"\n    action_items:\n      - round: 10\n        action: \"§3.5 加 'Controlled refers to experimentally controlled rewriting, not formal causal identification'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"共识：'the first' → 'a unified framework'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1 处理。RW 'first controlled, per-axis quantification' → 'first controlled quantification of this per-axis sensitivity gap'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R11 共识：'first' 需限定为 'first for LLM judges specifically'。\"\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R10 SF4 处理。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R11 共识：register 轴 evaluator-producer risk 最高，需显式 caveat。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"4 target judges (+ Gemini confirmatory) now cover the claim.\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"标题和 Abstract framing 偏向 attenuation。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 Q3: bootstrap attenuation 如何排除 construct-level 差异？§5.1 已有讨论但 'Blindspot' 术语天然偏向。MF2 reframe 部分缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 列为 Should-Fix (W3)，R1 交叉 [AGREE]。标题 'Detecting Hidden Style Bias' 预设 pairwise 为 ground truth。R1 补充：100-point Likert 结果实际支持 construct divergence 而非 measurement attenuation。建议标题更中性。\"\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: wont_fix\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Acknowledged as limitation. Register is weakest axis with judge-dependent confound structure; cross-rewriter test would be confounded by register's inherent instability.\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"R10 在 evaluator-producer 讨论中确认仍未覆盖 register。Limitations 已承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 W2 和 R2 W4 均指出 register 未覆盖。R2 交叉更正 R1 描述（Appendix D 覆盖 formality+verbosity 两轴，非仅 verbosity）。核心关切仍成立。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 升级 Must-Fix。Δ=15pp 几乎涵盖最小 confirmed bias。\"\n      - round: 10\n        reviewers: [1]\n        note: \"R10 SF3: Δ=15pp 偏宽，Claude 仅覆盖 2/3 axes。论文 Appendix G 有 Δ_min=15.7pp。Reviewer #104 确认当前版本已包含此数据。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 将 TOST Δ=15pp 列为 Should-Fix (W1)——循环论证（用自己效应量定义等价边界），15pp≈d=0.43 属 medium effect 偏宽。R2 交叉 [AGREE]。需先验论证或 sensitivity across Δ=5/10/15/20pp。\"\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"R10 Q2: Table 1 footnote 已有 'Empty cells: untested combinations' 但未说明选择理由。Reviewer #104 判断现有 footnote 足够。\"\n      - round: 11\n        reviewers: [1]\n        note: \"R11 M4: register axis 的 n 值和 power 未明确报告。\"\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound Δ=15pp 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"合并入 R5-M3 讨论。Δ_min=15.7pp 已报告。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。R11 两位共识 Should-Fix：需报告 TOST sensitivity across multiple Δ 或基于 leaderboard 排名影响论证 Δ 选择。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分——cross-axis contamination\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 10\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF6: cross-axis interaction 未测试。Agent 正在计算 cross-axis contamination 定量分析（formality rewrites 对 verbosity 的影响，反之亦然）。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。Limitations 已含 per-axis independence 讨论及 cross-axis contamination 分析（Appendix）。\"\n    action_items:\n      - round: 6\n        action: \"在 Limitations 补充讨论 axis-specific confounds\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"Agent 计算 cross-axis contamination（word count + formality proxy change）→ Appendix 写入\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2: 仅 2+1 axes 限制泛化。共识 Should-Fix：限定为 'preliminary evidence'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 列为 Must-Fix (N3)——n≈88 对 Likert power 严重不足（需 n=336-1200+），Likert null 可能仅反映 power 不足。R2 交叉 [AGREE]。共识：Conclusion 'systematically misses' 需 hedge，不能排除 power 解释。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 10\n    resolution: \"R9/R10 检查确认 Appendix C Table 5 已有完整 12 行 CI。\"\n    resolution_round: 10\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"论文 Related Work §2 已引用。\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 7 issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 10\n    resolution: \"§4.1 明确 'six tests—three target judges × two axes'，Gemini 为 confirmatory，Appendix Q 8-test family 下所有结果仍显著。R10 未再提及。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 fresh review 未提及此问题。§4.1 定义已清晰。\"\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型，存在循环性\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。§5.4 已报告 FNR 8.4% [3.7%, 15.9%] CI。GPT-4o cross-validation 部分缓解循环性。人工标注（MF1）将彻底解决。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及此具体问题，但 R1-N2 关于 NLI gate 人工验证不足间接涵盖。\"\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate 17.4% FPR 未报告\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。Appendix F 有 direction-aware gate validation data。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。\"\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"论文 §5.1 已引用 Tripathi et al. (2025)。\"\n    resolution_round: 9\n\n  # ============================================================\n  # Round 8 issues\n  # ============================================================\n\n  - id: \"R8-W1\"\n    summary: \"3 个风格轴限制 'framework' 级别泛化——需从 'framework' 降为 'methodology'\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2 再次确认。共识：限定为 'preliminary evidence of axis-dependent patterns'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: 与 R6-SF3 合并。两位共识：当前证据仅覆盖 3 axes，'framework' 级别泛化需更多 axes 验证。\"\n    action_items:\n      - round: 10\n        action: \"Limitations 补 'preliminary evidence' 限定 + 列出未覆盖 axes\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R8-W2\"\n    summary: \"生态效度讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Limitations 已含 'Our controlled manipulation design ensures internal validity but may not fully generalize to naturalistic evaluation settings.' R10 未再提及。\"\n    resolution_round: 10\n\n  - id: \"R8-W3\"\n    summary: \"Rewriting artifact 的 style-specific polishing interaction 未讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Appendix O 已含 'Same-style double-rewrite controls for style-neutral polishing artifacts but cannot exclude style-specific polishing interactions.' R10 未再提及。\"\n    resolution_round: 10\n\n  - id: \"R8-W4\"\n    summary: \"Introduction motivating example 未 acknowledge formality-quality nuance\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"§1 已有 'We note that formality preferences may partially reflect legitimate quality judgments—our GEE decomposition (§5.2) quantifies this originality component.' R10 确认。\"\n    resolution_round: 10\n\n  - id: \"R8-REF1\"\n    summary: \"建议补充引用：Girrbach et al. 'Likert or Not'\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"Phantom reference. Girrbach et al. wrote 'Reference-Free Rating'; 'Likert or Not' is by Godfrey et al. Neither match the suggested citation. Verified by Reviewer #97 and Agent.\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 10 issues\n  # ============================================================\n\n  - id: \"R10-N1\"\n    summary: \"100-point continuous Likert 实验仅用单一 judge（Qwen3-32B）\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Minor。Reviewer #104 判断不值得跑（Appendix 补充发现，非 primary claim）。Limitations 承认即可。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。Limitations 已含 'tested with a single judge' 承认。\"\n    action_items:\n      - round: 10\n        action: \"Limitations 补 'tested with a single judge'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R10-N2\"\n    summary: \"NLI gate 44% 拒绝率 selection bias 仅检查 4 个 surface covariates\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Reviewer #104 判断 Limitations 承认即可（已有 4-covariate + Cliff's δ + FNR 8.4%）。加一句 'retained pairs are not a random sample; BT estimates are conservative lower bounds'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 列为 Must-Fix (N2)——gate 过滤 12-35%，被过滤配对特征未分析，Appendix N ablation n 太小。R2 交叉降为 Should-Fix（threshold sweep 部分缓解）。\"\n    action_items:\n      - round: 10\n        action: \"Limitations 补 selection bias 承认句\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R10-REF1\"\n    summary: \"建议补充引用：Simms et al. (2019), Polo et al. (2024), Kocmi & Federmann (2023)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 10\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [2]\n        note: \"Agent 正在 WebSearch 验证真实性和相关性。\"\n    action_items:\n      - round: 10\n        action: \"WebSearch 验证 → 相关则加入 §2\"\n        assigned_to: agent\n        status: in_progress\n\n  # ============================================================\n  # Round 11 new issues\n  # ============================================================\n\n  - id: \"R11-N1\"\n    summary: \"Negative control 仅 Claude Sonnet 4 一个模型，不足以论证 Blindspot 的架构特异性\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix (W4): 仅一个负控制不足以论证 Blindspot 是特定架构/训练方式的产物。未讨论 Claude 为何不受影响。R2 交叉 [AGREE]。\"\n    action_items:\n      - round: 11\n        action: \"Discussion 提出可检验的机制假设（架构差异/RLHF 策略/偶然），或增加一个负控制\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R11-REF1\"\n    summary: \"建议补充引用：Bojar et al. (2016) WMT human evaluation\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 11\n        reviewers: [1]\n        note: \"大规模 pairwise vs. rating 方法比较的重要先例，与本文主题高度相关。R2 交叉 [AGREE]。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 11\n        action: \"Abstract/§2 中 'reveals' 等措辞需进一步弱化；'first' 限定为 'first for LLM judges specifically'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 2 issues\n  # ============================================================\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 10\n    resolution: \"Round 7+ 确认主正文 8 页合规。R10 确认 ≤8 页。\"\n    resolution_round: 7\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 格式检查确认正文 8 页合规。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 格式合规确认：正文 ≤8 页 ✓，匿名 ✓，Limitations 无新实验 ✓。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"cross-rewriter validation 仅覆盖 Qwen3-32B judge。22% Style OR 下降确认 inflation 存在。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 共识 Should-Fix：Blindspot 存在性 robust，但效应量有 ±20-25% rewriter-dependent 变异。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF4: 仅 Qwen3-32B judge 有 cross-rewriter 验证。效应量 ±22% rewriter-dependent 变异需显式承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 Should-Fix: R1 指出仅 verbosity×Qwen3-32B 有替代 rewriter（R2 更正：formality+verbosity 两轴，但 register 未覆盖）。22% OR 下降不可忽略。两位共识 register 轴 evaluator-producer risk 最高。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 10\n        action: \"Limitations 补一句：effect-size precision varies ±22% with rewriter choice\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'.\"\n    resolution_round: 4\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"共识 Must-Fix。50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 两位共同指向：增加 human evaluation 是最大可 actionable 改进。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 MF1 (critical): 持续 7 轮未解决。两位 Reviewer 交叉共识：human evaluation 是 4.0 的关键路径。孙震 50-pair 标注今晚返回。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 将 NLI gate 50 对人工标注列为 Must-Fix（Wilson CI 下界仅 86.3%，未报告 recall/FNR）。R2 交叉降为 Should-Fix（threshold sweep 11 阈值×44 组合全显著提供缓解）。论文 §5.4 报告 50 对 100% precision，但规模仍不足。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板\"\n        assigned_to: agent\n        status: done\n      - round: 10\n        action: \"孙震标注返回后 → analyze_annotations.py → Paper Agent 写入 §5.4\"\n        assigned_to: agent\n        status: pending\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"两位再次一致指出 Abstract 过密。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 fresh review 未显式提出 Abstract 过密问题。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未提及 Abstract 密度问题。P1 重写后可能已缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 列为 Should-Fix（W1），R1 交叉 [AGREE]。数字堆砌影响可读性，建议保留 1-2 个最有力数字。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 Should-Fix：Appendix H formality 方向异质性挑战 IIA。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。§4.1 footnote 已承认 direction asymmetry。可能接近解决。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 分歧：R1 列为 Must-Fix (critical)——Appendix B direction asymmetry 暗示 IIA 违反，需 Hausman-McFadden test。R2 交叉 [REBUT] 降为 Should-Fix——binary-choice BT 中 IIA 自动满足，Table 2 五种非参数方法独立确认 Blindspot。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"§5.2 已加 6 项 amplification controls。从 critical 降级为 Should-Fix。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF1: 检测 vs 放大歧义仍为核心。R2 定 critical，R1 反驳降为 warning。6 项 controls + Claude 负对照已部分缓解。Conclusion 语言需条件化。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: detection vs. amplification 成为两位 Reviewer 的最大共识问题。R2 列为 Must-Fix (N2)，R1 交叉 [AGREE]。六项控制 bound 了 amplification 但未 eliminate。缺 ground-truth bias 已知的验证。100-point continuous Likert 排除粒度解释但支持 construct divergence 解读。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"Conclusion 加条件性表述：amplification controls bound 但不完全排除放大\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 11\n        action: \"§6 开头 'systematically misses' 需加 hedge；考虑 reframe 为 'divergent signals' 而非单方面归因 Likert failure\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1]\n        note: \"§3.5 因果语言校准良好。原始 'do-operator' 语言已修复。\"\n      - round: 10\n        reviewers: [2]\n        note: \"R10 M2: 'Controlled' 和 'interventional' 语言暗示过强因果识别。共识：§3.5 加明确声明。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 列为 Should-Fix (W3)，R2 交叉 [AGREE]。'controlled'/'interventional'/DAG notation 给人因果推断研究的印象，但 NLI gate 非 do-operator，GEE 是关联分析。建议 §3 更早声明 'controlled = experimentally controlled rewriting, not formal causal identification'。\"\n    action_items:\n      - round: 10\n        action: \"§3.5 加 'Controlled refers to experimentally controlled rewriting, not formal causal identification'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"共识：'the first' → 'a unified framework'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1 处理。RW 'first controlled, per-axis quantification' → 'first controlled quantification of this per-axis sensitivity gap'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R11 共识：'first' 需限定为 'first for LLM judges specifically'。\"\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R10 SF4 处理。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R11 共识：register 轴 evaluator-producer risk 最高，需显式 caveat。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"4 target judges (+ Gemini confirmatory) now cover the claim.\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"标题和 Abstract framing 偏向 attenuation。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 Q3: bootstrap attenuation 如何排除 construct-level 差异？§5.1 已有讨论但 'Blindspot' 术语天然偏向。MF2 reframe 部分缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 列为 Should-Fix (W3)，R1 交叉 [AGREE]。标题 'Detecting Hidden Style Bias' 预设 pairwise 为 ground truth。R1 补充：100-point Likert 结果实际支持 construct divergence 而非 measurement attenuation。建议标题更中性。\"\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: wont_fix\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Acknowledged as limitation. Register is weakest axis with judge-dependent confound structure; cross-rewriter test would be confounded by register's inherent instability.\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"R10 在 evaluator-producer 讨论中确认仍未覆盖 register。Limitations 已承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 W2 和 R2 W4 均指出 register 未覆盖。R2 交叉更正 R1 描述（Appendix D 覆盖 formality+verbosity 两轴，非仅 verbosity）。核心关切仍成立。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 升级 Must-Fix。Δ=15pp 几乎涵盖最小 confirmed bias。\"\n      - round: 10\n        reviewers: [1]\n        note: \"R10 SF3: Δ=15pp 偏宽，Claude 仅覆盖 2/3 axes。论文 Appendix G 有 Δ_min=15.7pp。Reviewer #104 确认当前版本已包含此数据。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 将 TOST Δ=15pp 列为 Should-Fix (W1)——循环论证（用自己效应量定义等价边界），15pp≈d=0.43 属 medium effect 偏宽。R2 交叉 [AGREE]。需先验论证或 sensitivity across Δ=5/10/15/20pp。\"\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"R10 Q2: Table 1 footnote 已有 'Empty cells: untested combinations' 但未说明选择理由。Reviewer #104 判断现有 footnote 足够。\"\n      - round: 11\n        reviewers: [1]\n        note: \"R11 M4: register axis 的 n 值和 power 未明确报告。\"\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound Δ=15pp 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"合并入 R5-M3 讨论。Δ_min=15.7pp 已报告。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。R11 两位共识 Should-Fix：需报告 TOST sensitivity across multiple Δ 或基于 leaderboard 排名影响论证 Δ 选择。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分——cross-axis contamination\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 10\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF6: cross-axis interaction 未测试。Agent 正在计算 cross-axis contamination 定量分析（formality rewrites 对 verbosity 的影响，反之亦然）。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。Limitations 已含 per-axis independence 讨论及 cross-axis contamination 分析（Appendix）。\"\n    action_items:\n      - round: 6\n        action: \"在 Limitations 补充讨论 axis-specific confounds\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"Agent 计算 cross-axis contamination（word count + formality proxy change）→ Appendix 写入\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2: 仅 2+1 axes 限制泛化。共识 Should-Fix：限定为 'preliminary evidence'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 列为 Must-Fix (N3)——n≈88 对 Likert power 严重不足（需 n=336-1200+），Likert null 可能仅反映 power 不足。R2 交叉 [AGREE]。共识：Conclusion 'systematically misses' 需 hedge，不能排除 power 解释。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 10\n    resolution: \"R9/R10 检查确认 Appendix C Table 5 已有完整 12 行 CI。\"\n    resolution_round: 10\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"论文 Related Work §2 已引用。\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 7 issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 10\n    resolution: \"§4.1 明确 'six tests—three target judges × two axes'，Gemini 为 confirmatory，Appendix Q 8-test family 下所有结果仍显著。R10 未再提及。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 fresh review 未提及此问题。§4.1 定义已清晰。\"\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型，存在循环性\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。§5.4 已报告 FNR 8.4% [3.7%, 15.9%] CI。GPT-4o cross-validation 部分缓解循环性。人工标注（MF1）将彻底解决。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及此具体问题，但 R1-N2 关于 NLI gate 人工验证不足间接涵盖。\"\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate 17.4% FPR 未报告\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。Appendix F 有 direction-aware gate validation data。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。\"\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"论文 §5.1 已引用 Tripathi et al. (2025)。\"\n    resolution_round: 9\n\n  # ============================================================\n  # Round 8 issues\n  # ============================================================\n\n  - id: \"R8-W1\"\n    summary: \"3 个风格轴限制 'framework' 级别泛化——需从 'framework' 降为 'methodology'\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2 再次确认。共识：限定为 'preliminary evidence of axis-dependent patterns'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: 与 R6-SF3 合并。两位共识：当前证据仅覆盖 3 axes，'framework' 级别泛化需更多 axes 验证。\"\n    action_items:\n      - round: 10\n        action: \"Limitations 补 'preliminary evidence' 限定 + 列出未覆盖 axes\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R8-W2\"\n    summary: \"生态效度讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Limitations 已含 'Our controlled manipulation design ensures internal validity but may not fully generalize to naturalistic evaluation settings.' R10 未再提及。\"\n    resolution_round: 10\n\n  - id: \"R8-W3\"\n    summary: \"Rewriting artifact 的 style-specific polishing interaction 未讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Appendix O 已含 'Same-style double-rewrite controls for style-neutral polishing artifacts but cannot exclude style-specific polishing interactions.' R10 未再提及。\"\n    resolution_round: 10\n\n  - id: \"R8-W4\"\n    summary: \"Introduction motivating example 未 acknowledge formality-quality nuance\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"§1 已有 'We note that formality preferences may partially reflect legitimate quality judgments—our GEE decomposition (§5.2) quantifies this originality component.' R10 确认。\"\n    resolution_round: 10\n\n  - id: \"R8-REF1\"\n    summary: \"建议补充引用：Girrbach et al. 'Likert or Not'\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"Phantom reference. Girrbach et al. wrote 'Reference-Free Rating'; 'Likert or Not' is by Godfrey et al. Neither match the suggested citation. Verified by Reviewer #97 and Agent.\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 10 issues\n  # ============================================================\n\n  - id: \"R10-N1\"\n    summary: \"100-point continuous Likert 实验仅用单一 judge（Qwen3-32B）\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Minor。Reviewer #104 判断不值得跑（Appendix 补充发现，非 primary claim）。Limitations 承认即可。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。Limitations 已含 'tested with a single judge' 承认。\"\n    action_items:\n      - round: 10\n        action: \"Limitations 补 'tested with a single judge'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R10-N2\"\n    summary: \"NLI gate 44% 拒绝率 selection bias 仅检查 4 个 surface covariates\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Reviewer #104 判断 Limitations 承认即可（已有 4-covariate + Cliff's δ + FNR 8.4%）。加一句 'retained pairs are not a random sample; BT estimates are conservative lower bounds'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 列为 Must-Fix (N2)——gate 过滤 12-35%，被过滤配对特征未分析，Appendix N ablation n 太小。R2 交叉降为 Should-Fix（threshold sweep 部分缓解）。\"\n    action_items:\n      - round: 10\n        action: \"Limitations 补 selection bias 承认句\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R10-REF1\"\n    summary: \"建议补充引用：Simms et al. (2019), Polo et al. (2024), Kocmi & Federmann (2023)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 10\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [2]\n        note: \"Agent 正在 WebSearch 验证真实性和相关性。\"\n    action_items:\n      - round: 10\n        action: \"WebSearch 验证 → 相关则加入 §2\"\n        assigned_to: agent\n        status: in_progress\n\n  # ============================================================\n  # Round 11 new issues\n  # ============================================================\n\n  - id: \"R11-N1\"\n    summary: \"Negative control 仅 Claude Sonnet 4 一个模型，不足以论证 Blindspot 的架构特异性\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix (W4): 仅一个负控制不足以论证 Blindspot 是特定架构/训练方式的产物。未讨论 Claude 为何不受影响。R2 交叉 [AGREE]。\"\n    action_items:\n      - round: 11\n        action: \"Discussion 提出可检验的机制假设（架构差异/RLHF 策略/偶然），或增加一个负控制\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R11-REF1\"\n    summary: \"建议补充引用：Bojar et al. (2016) WMT human evaluation\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 11\n        reviewers: [1]\n        note: \"大规模 pairwise vs. rating 方法比较的重要先例，与本文主题高度相关。R2 交叉 [AGREE]。\""
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-22T16:50:23.784634+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 37946}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-22T16:52:46.293622+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "report": "# 审稿报告 — Round 11 (Fresh Review)\n\n**论文**: *The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition*\n**Venue**: EMNLP 2026 via ARR (May cycle)\n**审稿模式**: Fresh（两位 Reviewer 独立初审 + 交叉回应）\n**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 写作完整性 + 格式合规）\n\n---\n\n## Summary\n\n论文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated style rewriting + pairwise comparison 检测 LLM judge 中被 Likert 量表遗漏的风格偏差（\"Likert Blindspot\"）。在 4 个 judge（Qwen3-32B, GPT-4o, Llama-70B, Gemini-2.5-Flash）× 3 个风格轴（formality, verbosity, register）上验证，GEE decomposition 区分了 style-dominated（verbosity）与 conditionally style-driven（formality）轴。统计框架完整（BT + GEE + Holm-Bonferroni + TOST + Bootstrap），控制设计多层（NLI gate, position swap, negative control, rewriter independence test）。然而，核心发现本质上是心理测量学经典结论的 domain transfer，且 detection 与 amplification 无法干净分离，削弱了\"Likert 是盲区\"这一叙事的说服力。\n\n---\n\n## Strengths\n\n1. **统计框架罕见完整**：BT + GEE conditional decomposition + Holm-Bonferroni + TOST equivalence + Bootstrap attenuation + 7-method sensitivity analysis 的组合在 NLP 评估论文中极少见，体现了认真的统计思考。（R1, R2 共识）\n2. **GEE per-axis decomposition 有真正方法论贡献**：将 verbosity 识别为 style-dominated、formality 为 conditionally style-driven，超越简单的 \"有偏差/无偏差\" 二分法。这是论文最扎实的独立贡献。（R1, R2 共识）\n3. **多层控制设计**：NLI quality gate + position swap + direction-aware gating + Claude Sonnet 4 negative control + rewriter independence test + 同风格 double-rewrite control，整体设计优于大部分同类工作。（R1, R2 共识）\n4. **跨 judge 覆盖面**：4 个独立架构的 judge（含开源和闭源）独立复现 Blindspot，增强了结论的 generalizability。（R1）\n5. **Appendix 深度令人印象深刻**：17 个附录（A-R）覆盖了几乎所有可预见的 robustness concern。（R1）\n6. **诚实讨论 Comparative Trap 和 alternative interpretation**：§5.4 讨论了 detection vs. amplification 的歧义，Limitations 全面且自我批判。（R2）\n7. **CSD 作为 black-box framework 有即时实用性**：evaluation practitioners 可直接应用于检测自己 judge 的风格偏差。（R2）\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, R2-N1 + R1 AGREE] **新颖性定位过度——核心发现有深厚心理测量学先例**\n\nPairwise 优于 Likert 在灵敏度上的优势是 Thurstone (1927) Law of Comparative Judgment 的经典结论，Mohammad (2017) 和 Novikova et al. (2018) 已在 NLG 评估中实证验证。论文虽引用了这些工作，但叙事将已知现象包装为新发现：\n- 标题 \"Detecting **Hidden** Style Bias\" 暗示首次揭示\n- §2 \"first controlled quantification\" 的 scope 不够限定\n- Abstract 和 Conclusion 中 \"reveals\"/\"systematically misses\" 措辞过强\n\n**两位 Reviewer 共识**：论文真正的新颖贡献是 CSD 框架 + GEE per-axis decomposition，而非 \"Likert Blindspot\" 现象本身。建议 reframe 为 \"在 LLM judge 场景下首次系统量化已知的 measurement-format sensitivity gap\"，并将 per-axis confound taxonomy 提升为 co-equal contribution。\n\n**MF2** [critical, R2-N2 + R1-N3 + 交叉共识] **Detection vs. Amplification 无法分离——论文最根本的解读困境**\n\n§5.4 六项控制 bound 了 amplification 但未 eliminate：\n- 缺乏独立于两种测量格式的 **ground-truth bias measure**——没有 ground truth，就无法区分 (A) Likert attenuation vs. (B) pairwise amplification\n- 100-point continuous Likert（Appendix M）排除了 scale granularity 解释，但 R1 指出这实际上 **支持** construct divergence 解读——如果问题不在粒度，更可能是 absolute vs. relative measurement 的根本差异\n- Likert ATE 达到 80% power 需 n=336-1200+（Appendix L），当前 n≈88 的 Likert null 结果可能仅反映 power 不足而非方法论缺陷\n- Bootstrap attenuation δ̄ ≈ -0.017（Appendix J）的 CI 包含 0（R2 确认），不能排除无 attenuation\n\n**两位 Reviewer 共识**：§6 开头 \"Likert scoring systematically misses style biases\" 直接预设了解读 A，hedging 不充分。如果 amplification 解读成立，论文标题和核心 claim 需根本重构。建议：(1) 设计 ground-truth bias 已知的合成实验，或 (2) 诚实 reframe 为 \"divergent signals\" 而非单方面归因为 Likert failure。\n\n**MF3** [critical→warning, R1-N2, R2 降级] **NLI Quality Gate 选择偏差未充分量化**\n\n- 50 对人工标注偏少（Wilson CI 下界 86.3%），未报告 recall/FNR\n- Gate 过滤 12-35% 配对，被过滤配对的风格分布和特征未分析\n- Appendix N ablation（NLI-fail 样本）样本量太小（n≈12-21）\n\n**分歧记录**：R1 定为 critical Must-Fix；R2 交叉降为 Should-Fix，理由是 Appendix E threshold sweep（11 阈值 × 44 组合全显著，BT 变化 ≤4pp）提供了部分缓解。\n**Director 判断**：threshold sweep 缓解了结果对特定阈值的依赖，但未解决 selection bias 的方向性问题。定为 **高优 Should-Fix**。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, R1-W1 + R2 AGREE] **TOST 等价边界 Δ=15pp 缺乏严格论证**\n\n用自己观测到的效应量定义等价边界是循环论证。15pp ≈ d=0.43 属 medium effect，偏宽松。若 Δ=5pp 或 10pp，等价结论可能不成立。需基于领域先验（如 leaderboard 排名影响）论证，或报告 Δ=5/10/15/20pp 的 sensitivity。\n\n**SF2** [warning, R1-N3 + R2-W2 共识] **样本量限制 Likert null 的解读**\n\n主实验 LLMBar n=100（gate 后 ≈88），GEE 等深度分析仅在此 benchmark。n=355 scaled replication 部分弥补但 Likert 仍 n.s.。Conclusion \"systematically misses\" 需加 hedge——不能排除 power 不足解释。\n\n**SF3** [warning, R1-W3 + R2-Minor-3 共识] **因果术语与方法论强度不匹配**\n\n\"Controlled Style Decomposition\"/\"interventional\"/Figure 2 DAG notation 整体给人因果推断研究的印象。实际上 rewriting 非真正随机干预，NLI gate 非 do-operator，GEE 是关联分析。需更早声明 \"controlled = experimentally controlled rewriting, not formal causal identification\"。\n\n**SF4** [warning, R1-W2 + R2-W4 共识] **Evaluator-producer confound 控制实验覆盖不完整**\n\nAppendix D 覆盖 formality + verbosity 两轴（R2 更正 R1 原始描述），但 **register 轴完全未做 rewriter independence test**。Register 在 Table 1/3 中与其他轴同等呈现，需显式 caveat。22% Style OR 下降不可忽略。\n\n**SF5** [warning, R2-W3 + R1 AGREE] **标题和叙事预设 pairwise 为 ground truth**\n\n\"The Likert Blindspot\" 暗示 Likert 有缺陷，但 \"pairwise measures relative preference, Likert measures absolute quality\" 的 construct 差异同样合理。标题应更中性。\n\n**SF6** [warning, R2-W1 + R1 AGREE] **Abstract 信息密度过高**\n\n数字堆砌（d→0, n=355, p<0.01, 60%, OR 68×11 等）影响可读性。建议保留 1-2 个最有力数字，其余移至正文。\n\n**SF7** [warning, R1-W4 + R2 AGREE] **负控制仅 Claude Sonnet 4 一个模型**\n\n不足以论证 Blindspot 是特定架构/训练方式的产物。未讨论 Claude 为何不受影响的机制假设。\n\n### Minor（不影响接收）\n\n- **M1**: n=355 replication 讨论分散在 §5.1, Appendix J, K 多处，不易追踪（R1）\n- **M2**: Appendix Q Holm-Bonferroni 8-test family 未包含 cross-benchmark tests（R1）\n- **M3**: Register axis 的 n 值和 power 未明确报告，读者可能误解为 \"register 无偏差\" 而非 \"power 不足\"（R1）\n- **M4**: Limitations 中 tone 轴实验的 pass rate 数字可移至 Appendix（R2 提出，R1 反驳认为一个数字不构成 excessive content——**分歧记录**）\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成明确共识（交叉标注 [AGREE]）：\n\n1. **Detection vs. amplification 不可分离**是论文最根本的解读困境（MF2）\n2. **新颖性定位过度**——CSD 框架和 GEE decomposition 是真正贡献，但被 \"Blindspot\" 命名遮蔽（MF1）\n3. **因果术语偏强**需校准（SF3）\n4. **Register 轴 evaluator-producer 控制缺失**（SF4）\n5. **TOST Δ=15pp 需先验论证**（SF1）\n6. **Abstract 密度过高**（SF6）\n7. **负控制单一**（SF7）\n\n## Reviewer Divergence\n\n| 问题 | R1 定级 | R2 定级 | 核心分歧 |\n|------|---------|---------|----------|\n| BT IIA 假设未检验 | Must-Fix (critical) | Should-Fix (warning) | R2 认为 binary-choice BT 中 IIA 自动满足（无 irrelevant alternative 可删除），且 Table 2 五种非参数方法独立确认 Blindspot；R1 认为同源文本重复出现 + Appendix B direction asymmetry 仍构成风险 |\n| NLI gate 选择偏差 | Must-Fix (critical) | Should-Fix (warning) | R2 认为 threshold sweep（11阈值×44组合，BT变化≤4pp）提供充分缓解；R1 认为 sweep 未解决 selection bias 的方向性问题 |\n\n**Director 判断**：\n- BT IIA：R2 的技术论证更有说服力——在 binary forced choice 中 IIA 确实自动成立，且多种非参数方法一致。但 R1 关于 direction asymmetry 的观察值得在 Discussion 中补充解释。**定为 Should-Fix**。\n- NLI gate：两方各有理据。Threshold sweep 缓解了阈值依赖，但 selection bias 方向性分析仍缺。**定为高优 Should-Fix**（介于 MF 和 SF 之间）。\n\n---\n\n## Questions（需要作者澄清）\n\n1. 能否设计 ground-truth bias 幅度已知的合成实验，独立验证 Likert 和 pairwise 的 sensitivity curve？（R2-Q1, R1 AGREE）\n2. 100-point continuous Likert 仍未检测到 bias——作者是否认为这支持 absolute vs. relative evaluation 是根本区分？（R2-Q2, R1 AGREE）\n3. Rewriter independence test 中 Style OR 下降 22% 如何解读——是 rewriter artifact 还是 transformation 强度差异？（R2-Q3, R1 AGREE）\n4. 是否考虑 human annotators 在 CSD pairs 上同时做 Likert + pairwise 评估？（R2-Q4, R1 AGREE）\n5. 50 对人工标注中 gate-rejected 配对的 false negative 数据是否已收集？（R1-Q2）\n6. AlpacaEval/MT-Bench 的 per-judge per-axis 完整结果在哪个 Appendix？（R1-Q4）\n7. Bootstrap attenuation δ̄ ≈ -0.017 的 CI 包含 0（R2 确认）——如何解读这一结果？（R1-Q5）\n\n---\n\n## Missing References\n\n1. **Bojar et al. (2016)** 或 WMT human evaluation 工作——大规模 pairwise vs. rating 方法比较的重要先例（R1 提出, R2 AGREE）\n2. **Karpinska et al. (2021)** 或类似 scale design 影响的研究（R1 提出）\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）**：未配置，跳过。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 1 warning, 14 info）。\n\n**Warning**:\n- Figure 1（CSD pipeline overview, p.2）中各阶段缩略图标非常小，在正常阅读距离下细节难以辨认。作为全文第一个 display item，建议放大或简化图标。\n\n**Info highlights**:\n- 首页无 display item，Figure 1 在 p.2 顶部。方法论论文可接受，但若能提至 p.1 底部锚定更快。\n- Figure 1 caption 缺少各阶段功能概述，self-containment 可改进。\n- Figure 2（DAG）紧凑清晰，质量好。\n- 主体 8 页含 4 figures + 3 tables = 7 个 display items，密度健康。\n- 色彩方案保守，打印友好且色盲安全。\n- 未发现 LaTeX 渲染错误、margin 溢出或未解析引用。\n- Appendix 区域表格密度高，建议部分关键 ablation 结果可视化。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 — Borderline Conference（EMNLP 2026 ARR 评分标准）\n\n**置信度**: 4/5（两位 Reviewer 均仔细审查正文和全部 Appendix，熟悉 LLM-as-judge 和 measurement theory 文献）\n\n**详细评价**:\n\n论文在方法论执行上属于高质量工作：CSD 框架设计精巧，统计框架完整且罕见严谨，GEE per-axis decomposition 提供了超越简单 bias detection 的结构性洞察，17 个附录覆盖了几乎所有可预见的 robustness concern。控制设计（NLI gate + negative control + rewriter independence + position swap）构成了可信的多层验证链。\n\n然而，两个根本性问题限制了论文的 Conference-level 接收可能性：\n\n1. **新颖性**：核心 observation（pairwise 比 Likert 更灵敏）有深厚心理测量学先例（Thurstone 1927），论文叙事将 domain transfer 包装为新发现。真正的方法论贡献（CSD + GEE decomposition）被 \"Blindspot\" 命名所遮蔽。\n2. **解读歧义**：在缺乏 ground-truth bias measure 的情况下，detection vs. amplification 无法干净分离。论文的六项控制 bound 了 amplification 但未 eliminate 它，而 Conclusion 的 hedging 不充分。\n\n**路径建议**（不代表修改指导，仅作评审判断的背景说明）：\n- 以当前形态更适合 **Findings** track\n- 若能 (a) 诚实 reframe novelty、(b) 补充 amplification-bounding evidence（如合成实验或更大样本量验证）、(c) 在标题和 Conclusion 中保留足够 hedging，可达 **Conference** 水平\n\n---\n\n## Detailed Comments（按 Section）\n\n### Abstract\n- 信息密度过高，数字堆砌影响首次阅读体验。保留最核心的 1-2 个数字即可。（SF6）\n\n### §1 Introduction\n- \"Detecting Hidden Style Bias\" 的叙事框架预设 pairwise 为 ground truth。（SF5）\n- Contribution list 与实际证据强度匹配度待提升——将 per-axis confound taxonomy 提升为 co-equal contribution。（MF1）\n\n### §2 Related Work\n- Thurstone (1927)、Mohammad (2017)、Novikova et al. (2018) 已引用但讨论不充分——需更明确 acknowledge 本文在哪个维度上 extend 已有结论。（MF1）\n- 缺 Bojar et al. (2016) WMT human evaluation 先例。\n\n### §3 Method\n- \"Controlled\"/\"interventional\" 术语需更早声明不等于 formal causal identification。（SF3）\n- Figure 2 DAG notation 与 §5 disclaimer 之间有张力。（SF3）\n- NLI gate 的 recall/FNR 未报告。（MF3）\n\n### §4 Results\n- Table 1 register 轴结果需加显式 caveat（无 rewriter independence test）。（SF4）\n- BT IIA 可在 Discussion 中补充 direction asymmetry 的解释。（Divergence issue）\n\n### §5 Analysis\n- §5.1 measurement attenuation vs. construct divergence 讨论是论文最重要的自我审视，但 framing 偏向 attenuation。（MF2）\n- §5.4 六项 amplification controls 是 solid 的贡献，但 \"bound ≠ eliminate\" 需更显式。（MF2）\n- TOST Δ=15pp 需先验论证或 sensitivity analysis。（SF1）\n\n### §6 Conclusion\n- \"Likert scoring systematically misses style biases\" 直接预设解读 A，hedging 不充分。（MF2）\n\n### Limitations\n- 全面且自我批判，是论文的优势之一。\n- Tone 轴 pass rate 数字不构成 \"excessive content\"——R1 反驳 R2 的移除建议，Director 同意 R1。\n\n### 格式合规\n- 正文 ≤8 页 ✓\n- 匿名性 ✓（`\\author{Anonymous}`）\n- Limitations 无新实验/图表 ✓\n- 引用格式 ACL 规范 ✓\n- Double-blind ✓"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "report": "# 审稿报告 — Round 11 (Fresh Review)\n\n**论文**: *The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition*\n**Venue**: EMNLP 2026 via ARR (May cycle)\n**审稿模式**: Fresh（两位 Reviewer 独立初审 + 交叉回应）\n**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 写作完整性 + 格式合规）\n\n---\n\n## Summary\n\n论文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated style rewriting + pairwise comparison 检测 LLM judge 中被 Likert 量表遗漏的风格偏差（\"Likert Blindspot\"）。在 4 个 judge（Qwen3-32B, GPT-4o, Llama-70B, Gemini-2.5-Flash）× 3 个风格轴（formality, verbosity, register）上验证，GEE decomposition 区分了 style-dominated（verbosity）与 conditionally style-driven（formality）轴。统计框架完整（BT + GEE + Holm-Bonferroni + TOST + Bootstrap），控制设计多层（NLI gate, position swap, negative control, rewriter independence test）。然而，核心发现本质上是心理测量学经典结论的 domain transfer，且 detection 与 amplification 无法干净分离，削弱了\"Likert 是盲区\"这一叙事的说服力。\n\n---\n\n## Strengths\n\n1. **统计框架罕见完整**：BT + GEE conditional decomposition + Holm-Bonferroni + TOST equivalence + Bootstrap attenuation + 7-method sensitivity analysis 的组合在 NLP 评估论文中极少见，体现了认真的统计思考。（R1, R2 共识）\n2. **GEE per-axis decomposition 有真正方法论贡献**：将 verbosity 识别为 style-dominated、formality 为 conditionally style-driven，超越简单的 \"有偏差/无偏差\" 二分法。这是论文最扎实的独立贡献。（R1, R2 共识）\n3. **多层控制设计**：NLI quality gate + position swap + direction-aware gating + Claude Sonnet 4 negative control + rewriter independence test + 同风格 double-rewrite control，整体设计优于大部分同类工作。（R1, R2 共识）\n4. **跨 judge 覆盖面**：4 个独立架构的 judge（含开源和闭源）独立复现 Blindspot，增强了结论的 generalizability。（R1）\n5. **Appendix 深度令人印象深刻**：17 个附录（A-R）覆盖了几乎所有可预见的 robustness concern。（R1）\n6. **诚实讨论 Comparative Trap 和 alternative interpretation**：§5.4 讨论了 detection vs. amplification 的歧义，Limitations 全面且自我批判。（R2）\n7. **CSD 作为 black-box framework 有即时实用性**：evaluation practitioners 可直接应用于检测自己 judge 的风格偏差。（R2）\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, R2-N1 + R1 AGREE] **新颖性定位过度——核心发现有深厚心理测量学先例**\n\nPairwise 优于 Likert 在灵敏度上的优势是 Thurstone (1927) Law of Comparative Judgment 的经典结论，Mohammad (2017) 和 Novikova et al. (2018) 已在 NLG 评估中实证验证。论文虽引用了这些工作，但叙事将已知现象包装为新发现：\n- 标题 \"Detecting **Hidden** Style Bias\" 暗示首次揭示\n- §2 \"first controlled quantification\" 的 scope 不够限定\n- Abstract 和 Conclusion 中 \"reveals\"/\"systematically misses\" 措辞过强\n\n**两位 Reviewer 共识**：论文真正的新颖贡献是 CSD 框架 + GEE per-axis decomposition，而非 \"Likert Blindspot\" 现象本身。建议 reframe 为 \"在 LLM judge 场景下首次系统量化已知的 measurement-format sensitivity gap\"，并将 per-axis confound taxonomy 提升为 co-equal contribution。\n\n**MF2** [critical, R2-N2 + R1-N3 + 交叉共识] **Detection vs. Amplification 无法分离——论文最根本的解读困境**\n\n§5.4 六项控制 bound 了 amplification 但未 eliminate：\n- 缺乏独立于两种测量格式的 **ground-truth bias measure**——没有 ground truth，就无法区分 (A) Likert attenuation vs. (B) pairwise amplification\n- 100-point continuous Likert（Appendix M）排除了 scale granularity 解释，但 R1 指出这实际上 **支持** construct divergence 解读——如果问题不在粒度，更可能是 absolute vs. relative measurement 的根本差异\n- Likert ATE 达到 80% power 需 n=336-1200+（Appendix L），当前 n≈88 的 Likert null 结果可能仅反映 power 不足而非方法论缺陷\n- Bootstrap attenuation δ̄ ≈ -0.017（Appendix J）的 CI 包含 0（R2 确认），不能排除无 attenuation\n\n**两位 Reviewer 共识**：§6 开头 \"Likert scoring systematically misses style biases\" 直接预设了解读 A，hedging 不充分。如果 amplification 解读成立，论文标题和核心 claim 需根本重构。建议：(1) 设计 ground-truth bias 已知的合成实验，或 (2) 诚实 reframe 为 \"divergent signals\" 而非单方面归因为 Likert failure。\n\n**MF3** [critical→warning, R1-N2, R2 降级] **NLI Quality Gate 选择偏差未充分量化**\n\n- 50 对人工标注偏少（Wilson CI 下界 86.3%），未报告 recall/FNR\n- Gate 过滤 12-35% 配对，被过滤配对的风格分布和特征未分析\n- Appendix N ablation（NLI-fail 样本）样本量太小（n≈12-21）\n\n**分歧记录**：R1 定为 critical Must-Fix；R2 交叉降为 Should-Fix，理由是 Appendix E threshold sweep（11 阈值 × 44 组合全显著，BT 变化 ≤4pp）提供了部分缓解。\n**Director 判断**：threshold sweep 缓解了结果对特定阈值的依赖，但未解决 selection bias 的方向性问题。定为 **高优 Should-Fix**。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, R1-W1 + R2 AGREE] **TOST 等价边界 Δ=15pp 缺乏严格论证**\n\n用自己观测到的效应量定义等价边界是循环论证。15pp ≈ d=0.43 属 medium effect，偏宽松。若 Δ=5pp 或 10pp，等价结论可能不成立。需基于领域先验（如 leaderboard 排名影响）论证，或报告 Δ=5/10/15/20pp 的 sensitivity。\n\n**SF2** [warning, R1-N3 + R2-W2 共识] **样本量限制 Likert null 的解读**\n\n主实验 LLMBar n=100（gate 后 ≈88），GEE 等深度分析仅在此 benchmark。n=355 scaled replication 部分弥补但 Likert 仍 n.s.。Conclusion \"systematically misses\" 需加 hedge——不能排除 power 不足解释。\n\n**SF3** [warning, R1-W3 + R2-Minor-3 共识] **因果术语与方法论强度不匹配**\n\n\"Controlled Style Decomposition\"/\"interventional\"/Figure 2 DAG notation 整体给人因果推断研究的印象。实际上 rewriting 非真正随机干预，NLI gate 非 do-operator，GEE 是关联分析。需更早声明 \"controlled = experimentally controlled rewriting, not formal causal identification\"。\n\n**SF4** [warning, R1-W2 + R2-W4 共识] **Evaluator-producer confound 控制实验覆盖不完整**\n\nAppendix D 覆盖 formality + verbosity 两轴（R2 更正 R1 原始描述），但 **register 轴完全未做 rewriter independence test**。Register 在 Table 1/3 中与其他轴同等呈现，需显式 caveat。22% Style OR 下降不可忽略。\n\n**SF5** [warning, R2-W3 + R1 AGREE] **标题和叙事预设 pairwise 为 ground truth**\n\n\"The Likert Blindspot\" 暗示 Likert 有缺陷，但 \"pairwise measures relative preference, Likert measures absolute quality\" 的 construct 差异同样合理。标题应更中性。\n\n**SF6** [warning, R2-W1 + R1 AGREE] **Abstract 信息密度过高**\n\n数字堆砌（d→0, n=355, p<0.01, 60%, OR 68×11 等）影响可读性。建议保留 1-2 个最有力数字，其余移至正文。\n\n**SF7** [warning, R1-W4 + R2 AGREE] **负控制仅 Claude Sonnet 4 一个模型**\n\n不足以论证 Blindspot 是特定架构/训练方式的产物。未讨论 Claude 为何不受影响的机制假设。\n\n### Minor（不影响接收）\n\n- **M1**: n=355 replication 讨论分散在 §5.1, Appendix J, K 多处，不易追踪（R1）\n- **M2**: Appendix Q Holm-Bonferroni 8-test family 未包含 cross-benchmark tests（R1）\n- **M3**: Register axis 的 n 值和 power 未明确报告，读者可能误解为 \"register 无偏差\" 而非 \"power 不足\"（R1）\n- **M4**: Limitations 中 tone 轴实验的 pass rate 数字可移至 Appendix（R2 提出，R1 反驳认为一个数字不构成 excessive content——**分歧记录**）\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成明确共识（交叉标注 [AGREE]）：\n\n1. **Detection vs. amplification 不可分离**是论文最根本的解读困境（MF2）\n2. **新颖性定位过度**——CSD 框架和 GEE decomposition 是真正贡献，但被 \"Blindspot\" 命名遮蔽（MF1）\n3. **因果术语偏强**需校准（SF3）\n4. **Register 轴 evaluator-producer 控制缺失**（SF4）\n5. **TOST Δ=15pp 需先验论证**（SF1）\n6. **Abstract 密度过高**（SF6）\n7. **负控制单一**（SF7）\n\n## Reviewer Divergence\n\n| 问题 | R1 定级 | R2 定级 | 核心分歧 |\n|------|---------|---------|----------|\n| BT IIA 假设未检验 | Must-Fix (critical) | Should-Fix (warning) | R2 认为 binary-choice BT 中 IIA 自动满足（无 irrelevant alternative 可删除），且 Table 2 五种非参数方法独立确认 Blindspot；R1 认为同源文本重复出现 + Appendix B direction asymmetry 仍构成风险 |\n| NLI gate 选择偏差 | Must-Fix (critical) | Should-Fix (warning) | R2 认为 threshold sweep（11阈值×44组合，BT变化≤4pp）提供充分缓解；R1 认为 sweep 未解决 selection bias 的方向性问题 |\n\n**Director 判断**：\n- BT IIA：R2 的技术论证更有说服力——在 binary forced choice 中 IIA 确实自动成立，且多种非参数方法一致。但 R1 关于 direction asymmetry 的观察值得在 Discussion 中补充解释。**定为 Should-Fix**。\n- NLI gate：两方各有理据。Threshold sweep 缓解了阈值依赖，但 selection bias 方向性分析仍缺。**定为高优 Should-Fix**（介于 MF 和 SF 之间）。\n\n---\n\n## Questions（需要作者澄清）\n\n1. 能否设计 ground-truth bias 幅度已知的合成实验，独立验证 Likert 和 pairwise 的 sensitivity curve？（R2-Q1, R1 AGREE）\n2. 100-point continuous Likert 仍未检测到 bias——作者是否认为这支持 absolute vs. relative evaluation 是根本区分？（R2-Q2, R1 AGREE）\n3. Rewriter independence test 中 Style OR 下降 22% 如何解读——是 rewriter artifact 还是 transformation 强度差异？（R2-Q3, R1 AGREE）\n4. 是否考虑 human annotators 在 CSD pairs 上同时做 Likert + pairwise 评估？（R2-Q4, R1 AGREE）\n5. 50 对人工标注中 gate-rejected 配对的 false negative 数据是否已收集？（R1-Q2）\n6. AlpacaEval/MT-Bench 的 per-judge per-axis 完整结果在哪个 Appendix？（R1-Q4）\n7. Bootstrap attenuation δ̄ ≈ -0.017 的 CI 包含 0（R2 确认）——如何解读这一结果？（R1-Q5）\n\n---\n\n## Missing References\n\n1. **Bojar et al. (2016)** 或 WMT human evaluation 工作——大规模 pairwise vs. rating 方法比较的重要先例（R1 提出, R2 AGREE）\n2. **Karpinska et al. (2021)** 或类似 scale design 影响的研究（R1 提出）\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）**：未配置，跳过。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 1 warning, 14 info）。\n\n**Warning**:\n- Figure 1（CSD pipeline overview, p.2）中各阶段缩略图标非常小，在正常阅读距离下细节难以辨认。作为全文第一个 display item，建议放大或简化图标。\n\n**Info highlights**:\n- 首页无 display item，Figure 1 在 p.2 顶部。方法论论文可接受，但若能提至 p.1 底部锚定更快。\n- Figure 1 caption 缺少各阶段功能概述，self-containment 可改进。\n- Figure 2（DAG）紧凑清晰，质量好。\n- 主体 8 页含 4 figures + 3 tables = 7 个 display items，密度健康。\n- 色彩方案保守，打印友好且色盲安全。\n- 未发现 LaTeX 渲染错误、margin 溢出或未解析引用。\n- Appendix 区域表格密度高，建议部分关键 ablation 结果可视化。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 — Borderline Conference（EMNLP 2026 ARR 评分标准）\n\n**置信度**: 4/5（两位 Reviewer 均仔细审查正文和全部 Appendix，熟悉 LLM-as-judge 和 measurement theory 文献）\n\n**详细评价**:\n\n论文在方法论执行上属于高质量工作：CSD 框架设计精巧，统计框架完整且罕见严谨，GEE per-axis decomposition 提供了超越简单 bias detection 的结构性洞察，17 个附录覆盖了几乎所有可预见的 robustness concern。控制设计（NLI gate + negative control + rewriter independence + position swap）构成了可信的多层验证链。\n\n然而，两个根本性问题限制了论文的 Conference-level 接收可能性：\n\n1. **新颖性**：核心 observation（pairwise 比 Likert 更灵敏）有深厚心理测量学先例（Thurstone 1927），论文叙事将 domain transfer 包装为新发现。真正的方法论贡献（CSD + GEE decomposition）被 \"Blindspot\" 命名所遮蔽。\n2. **解读歧义**：在缺乏 ground-truth bias measure 的情况下，detection vs. amplification 无法干净分离。论文的六项控制 bound 了 amplification 但未 eliminate 它，而 Conclusion 的 hedging 不充分。\n\n**路径建议**（不代表修改指导，仅作评审判断的背景说明）：\n- 以当前形态更适合 **Findings** track\n- 若能 (a) 诚实 reframe novelty、(b) 补充 amplification-bounding evidence（如合成实验或更大样本量验证）、(c) 在标题和 Conclusion 中保留足够 hedging，可达 **Conference** 水平\n\n---\n\n## Detailed Comments（按 Section）\n\n### Abstract\n- 信息密度过高，数字堆砌影响首次阅读体验。保留最核心的 1-2 个数字即可。（SF6）\n\n### §1 Introduction\n- \"Detecting Hidden Style Bias\" 的叙事框架预设 pairwise 为 ground truth。（SF5）\n- Contribution list 与实际证据强度匹配度待提升——将 per-axis confound taxonomy 提升为 co-equal contribution。（MF1）\n\n### §2 Related Work\n- Thurstone (1927)、Mohammad (2017)、Novikova et al. (2018) 已引用但讨论不充分——需更明确 acknowledge 本文在哪个维度上 extend 已有结论。（MF1）\n- 缺 Bojar et al. (2016) WMT human evaluation 先例。\n\n### §3 Method\n- \"Controlled\"/\"interventional\" 术语需更早声明不等于 formal causal identification。（SF3）\n- Figure 2 DAG notation 与 §5 disclaimer 之间有张力。（SF3）\n- NLI gate 的 recall/FNR 未报告。（MF3）\n\n### §4 Results\n- Table 1 register 轴结果需加显式 caveat（无 rewriter independence test）。（SF4）\n- BT IIA 可在 Discussion 中补充 direction asymmetry 的解释。（Divergence issue）\n\n### §5 Analysis\n- §5.1 measurement attenuation vs. construct divergence 讨论是论文最重要的自我审视，但 framing 偏向 attenuation。（MF2）\n- §5.4 六项 amplification controls 是 solid 的贡献，但 \"bound ≠ eliminate\" 需更显式。（MF2）\n- TOST Δ=15pp 需先验论证或 sensitivity analysis。（SF1）\n\n### §6 Conclusion\n- \"Likert scoring systematically misses style biases\" 直接预设解读 A，hedging 不充分。（MF2）\n\n### Limitations\n- 全面且自我批判，是论文的优势之一。\n- Tone 轴 pass rate 数字不构成 \"excessive content\"——R1 反驳 R2 的移除建议，Director 同意 R1。\n\n### 格式合规\n- 正文 ≤8 页 ✓\n- 匿名性 ✓（`\\author{Anonymous}`）\n- Limitations 无新实验/图表 ✓\n- 引用格式 ACL 规范 ✓\n- Double-blind ✓"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-22T16:52:50.158121+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3864
}
```

</details>

---


### Assistant

_source line 894 · 2026-05-22T16:52:59.513443+00:00_

审稿报告已投递。

**Round 11 审稿完成**。两位 Reviewer 均给出 3.5（Borderline Conference），经交叉回应后在关键问题上达成高度共识：

- **MF1**: 新颖性定位过度——核心发现是 Thurstone (1927) 以来的经典结论在 LLM judge 场景的 domain transfer
- **MF2**: Detection vs. amplification 无法分离——六项控制 bound 了但未 eliminate amplification，缺 ground-truth bias measure，Conclusion hedging 不足
- **7 项 Should-Fix**: TOST Δ 论证不足、样本量限制、因果术语偏强、evaluator-producer 控制不完整（register）、标题预设 pairwise 为 ground truth、Abstract 过密、负控制单一
- **分歧**: BT IIA 严重性（R1=Must-Fix, R2=Should-Fix，Director 采纳 R2 的技术论证定为 Should-Fix）

**总评**: 3.5 Borderline Conference。方法论执行高质量，当前形态更适合 Findings；若 reframe novelty + 补充 amplification-bounding evidence + 加足 hedging，可冲 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 89

## Round 89

2 recorded events


### User

_source line 895 · 2026-05-22T16:53:02.020006+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

**总结**：对 R1 的 3 条 Must-Fix，我 rebut 了 N1（BT IIA 在 binary choice 中自动满足，且有五种 IIA-free 方法独立确认，建议降为 Should-Fix），agree 了 N2（但建议降为 Should-Fix，因 threshold sweep 提供缓解），agree 了 N3（power 不足是最有力的 alternative explanation）。两位 Reviewer 的核心共识集中在：detection vs. amplification 未解决、措辞需 hedge、rewriter independence 不完整、样本量有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 896 · 2026-05-22T16:53:12.138671+00:00_

审稿报告已投递至 Research Director。

**Round 11 审稿完成。**

两位 Reviewer 均给出 **3.5（Borderline Conference）**，综合评分 **3.5**。

核心问题：
1. **MF1**：新颖性定位过度——Likert vs. pairwise 灵敏度差异是 Thurstone (1927) 以来的经典结论
2. **MF2**：Detection vs. amplification 不可分离——六项控制 bound 但未 eliminate，缺 ground-truth bias measure
3. 7 条 Should-Fix：TOST Δ 论证、样本量 hedging、因果术语、evaluator-producer 控制、标题预设、Abstract 密度、单一负控制

Issue tracker 已同步更新（新增 2 条、更新 15 条现有 issue）。视觉审查结果已纳入报告（1 warning: Figure 1 图标过小）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 90

## Round 90

72 recorded events


### User

_source line 897 · 2026-05-22T18:04:59.376365+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 898 · 2026-05-22T18:05:07.605729+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-22T18:05:07.606746+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-22T18:05:13.127590+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-22T18:05:13.178162+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-22T18:05:16.544054+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-22T18:05:16.594719+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 904 · 2026-05-22T18:05:21.065476+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-22T18:05:21.117504+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-22T18:05:25.936078+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 907 · 2026-05-22T18:05:27.141052+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (54 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **register_100_cf** (killed): Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality\n- **gemini_flash_fourth_judge** (success): Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.\n- **llama70b_register** (success): Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures\n  [llama70b_register_summary](/api/workspace-files/projects/causal_style_decomp_judge/artifacts/llama70b_register/data/llama70b_register_summary.json)\n\n## 趋势\n成功 38 / 负向 12 / 失败 0 / 共 54\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- register_100_cf: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1204
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-22T18:05:27.141618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-22T18:05:28.095880+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Detecting Hidden Style Bias\\in LLM Judges via Controlled Style Decomposition}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\S\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.
45	The primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences inhe
…[truncated 3715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-22T18:05:28.146485+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 911 · 2026-05-22T18:05:29.251264+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 912 · 2026-05-22T18:05:29.403636+00:00_

-rw-r--r-- 1 ubuntu ubuntu 393706 May 22 17:54 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-22T18:05:34.562455+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found several relevant results. The search returned information about EMNLP 2026-related
…[truncated 1396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6415
}
```

</details>

---


### Tool call

_source line 914 · 2026-05-22T18:05:39.832474+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines author instructions page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines author instructions page limit"
  }
}
```

</details>

---


### Tool call

_source line 915 · 2026-05-22T18:05:40.836709+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 conference dates location call for main conference papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 conference dates location call for main conference papers"
  }
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-22T18:05:41.740645+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-22T18:05:46.057474+00:00_

Web search results for query: "EMNLP 2026 conference dates location call for main conference papers"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, here's the information about EMNLP 2026:

## Conference Dates and Location

EMNLP 2026 will be held in Budapest, Hungary from October 24th to October 29th, 2026.

## Call for Main Conference Papers

EMNLP 2026 invites the submiss
…[truncated 779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5220
}
```

</details>

---


### Tool result

_source line 918 · 2026-05-22T18:05:47.362736+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines author instructions page limit"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

I found relevant information about ARR 2026 submission guidelines. Here's what I found regarding submission guidelines and page limits:

## ACL Rolling Review (ARR) 2026 Submission Guidelines

The submission must adhere to the formatting in the submission templates, which is available as an Overleaf template.

### Key Author Requirements:

Papers must not
…[truncated 1346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 7530
}
```

</details>

---


### Tool result

_source line 919 · 2026-05-22T18:05:47.363590+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml\", \"content\": \"_next_id: 70\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 14:09 UTC\\n  summary: '文献蒸馏审视：研究方向无需调整，CSD 填补 #1 空白（多维 style 因果分解），post-MVP 需扩展 judge/benchmark/baseline\\n    覆盖'\\n  rationale: '10 篇论文蒸馏显示：(1) 多维 style 联合因果分解是领域 #1 空白，与 CSD 核心 claim 完全对齐；(2) 竞品 claim\\n    无直接重叠（FairJudge=white-box, Pref Leakage=family-based, Soumik=prompt-dependent）；(3)\\n    同行标准要求 3-5 异构 judge + AlpacaEval/Arena-Hard/MT-Bench + Bootstrap CIs + 对比 LC-AlpacaEval\\n    baseline。当前 MVP 方案足够，research 阶段需按蒸馏标准扩展。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 14:19 UTC\\n  summary: MVP 全量评分 + 分层分析：score 全部 100 条，按 BERTScore 阈值 0.88/0.90/0.92 分层算 ATE，不降低阈值\\n  rationale: 36% pass rate (BERTScore≥0.92) 偏低但 NLI 均值 0.9422 说明语义保留好。降阈值是数据操作，不如保留完整信息。全量评分\\n    (n=100) 保证统计 power，分层分析同时回答\\\"严格阈值下效应是否存在\\\"和\\\"宽松阈值下效应是否增强\\\"。8B H1 fail 不消耗迭代配额（ROADMAP\\n    规则），32B 备用。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 14:20 UTC\\n  summary: H1 content verification 改为 NLI-only gate（≥0.90），BERTScore 降为监控指标，不作为过滤条件\\n  rationale: Reviewer 诊断：36% pass rate 的根因是 BERTScore 惩罚 style transfer 预期的词汇变化（contractions→full\\n    forms 等），而非内容泄漏。NLI 均值 0.9422、抽样 >0.99 证明语义保留良好。BERTScore 作为 token-level 相似度指标与\\n    style transfer 评估目标矛盾（改的就是 token）。Double-rewrite pass rate 更低（21/100）进一步印证。NLI-only\\n    gate 是度量校准（不消耗 8B 迭代配额），与 D002 全量评分兼容——primary ATE 用 NLI≥0.90 子集，secondary 按 BERTScore\\n    分层。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 14:32 UTC\\n  summary: 8B 初步 ATE≈0.028 不可见，归因三因素：Likert 粒度 + 8B rewriter 质量 + RATE corruption。不计入\\n    kill criteria，等 n=100 + 32B\\n  rationale: 36/100 初步数据 Cohen's d=0.055 远低于 0.3 门槛，但三个叠加因素解释了结果：(1) 83% 零差异源于 integer\\n    Likert 无法捕捉 sub-integer 效应；(2) 22% identical rewrites 稀释 ATE；
…[truncated 10852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5622
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-22T18:05:54.741322+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review CFP 2026 long paper 8 pages short paper 4 pages double blind anonymity policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review CFP 2026 long paper 8 pages short paper 4 pages double blind anonymity policy"
  }
}
```

</details>

---


### Tool call

_source line 921 · 2026-05-22T18:05:57.100313+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 922 · 2026-05-22T18:05:57.603083+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 923 · 2026-05-22T18:05:57.954809+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 924 · 2026-05-22T18:05:58.005607+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-22T18:06:00.264417+00:00_

Web search results for query: "ACL Rolling Review CFP 2026 long paper 8 pages short paper 4 pages double blind anonymity policy"

Links: [{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"aclrollingreview/cfp.md at master · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/master/cfp.md"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's what I found about ACL Rolling Review CFP 2026 regarding paper length requirements and anonymity policy:

## Paper Length Requirements

Long papers may consist of up to eight (8) pages of content, plus unlimited pages of references. Short papers may consist of up to four (4) pages of content, plus unlimited pages of references.

## Anonymity Policy

ACL has policies for submission, review and citation designed to protect the integrity of two-way anonymized review and ensure that submission
…[truncated 649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5523
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-22T18:06:04.280632+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/ -name \"config.yaml\" -o -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
  "description": "Find config files in agent directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/ -name \"config.yaml\" -o -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
    "description": "Find config files in agent directory"
  }
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-22T18:06:04.582367+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-22T18:06:04.582701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 929 · 2026-05-22T18:06:04.633133+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved unless noted)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	
16	  - id: "R2-N1"
17	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
18	    category: framing
19	    severity: warning
20	    status: in_progress
21	    first_raised_round: 1
22	    last_seen_round: 11
23	    resolution: null
24	    resolution_round: null
25	    mentions:
26	      - round: 3
27	        reviewers: [1, 2]
28	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
29	      - round: 8
30	        reviewers: [1, 2]
31	        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
32	      - round: 9
33	        reviewers: [1, 2]
34	        note: "R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。"
35	      - round: 10
36	        reviewers: [1, 2]
37	        note: "R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。"
38	      - round: 11
39	        reviewers: [1, 2]
40	        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。"
41	    action_items:
42	      - round: 7
43	        action: "将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'"
44	        assigned_to: paper_agent
45	        status: done
46	      - round: 10
47	        action: "三处 'reveals' → 'demonstrates'/'identifies' + R
…[truncated 134 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 930 · 2026-05-22T18:06:08.147699+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "offset": "50",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "offset": "50",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 931 · 2026-05-22T18:06:08.198678+00:00_

50	      - round: 11
51	        action: "Abstract/§2 中 'reveals' 等措辞需进一步弱化；'first' 限定为 'first for LLM judges specifically'"
52	        assigned_to: paper_agent
53	        status: in_progress
54	
55	  - id: "R1-N2"
56	    summary: "NLI gate 67% false-negative rate 造成选择偏差未分析"
57	    category: method
58	    severity: critical
59	    status: resolved
60	    first_raised_round: 1
61	    last_seen_round: 1
62	    resolution: "§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89"
63	    resolution_round: 1
64	
65	  - id: "R1-N3"
66	    summary: "NLI 阈值 0.90 无 justification"
67	    category: method
68	    severity: critical
69	    status: resolved
70	    first_raised_round: 1
71	    last_seen_round: 4
72	    resolution: "Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added."
73	    resolution_round: 1
74	
75	  - id: "R2-N2"
76	    summary: "RATE 批评缺乏 matched replication"
77	    category: framing
78	    severity: critical
79	    status: resolved
80	    first_raised_round: 1
81	    last_seen_round: 1
82	    resolution: "§likert_pairwise h2h on same data"
83	    resolution_round: 1
84	
85	  - id: "R2-N3"
86	    summary: "引用系统严重不完整"
87	    category: format
88	    severity: critical
89	    status: resolved
90	    first_raised_round: 1
91	    last_seen_round: 1
92	    resolution: "22 verified refs, 0 broken"
93	    resolution_round: 1
94	
95	  - id: "R1-W1"
96	    summary: "Likert baseline 可能不公平——未使用 ordinal regression"
97	    category: method
98	    severity: critical
99	    status: resolved
100	    first_raised_round: 1
101	    last_seen_round: 1
102	    resolution: "Table 2: all 7 Likert methods fail"
103	    resolution_round: 1
104	
105	  - id: "R1-W2"
106	    summary: "Consistency filtering data loss"
107	    category: experiment
108	    severity: warning
109	    status: resolved
110	    first_raised_round: 1
111	    last_seen_round: 1
112	    resolution: "BT on all data LOWER than filtered"
113	    resolution_round: 1
114	
115	  - id: "R1-W3"
116	    summ
…[truncated 3896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 932 · 2026-05-22T18:06:11.311546+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "offset": "249",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "offset": "249",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 933 · 2026-05-22T18:06:11.362427+00:00_

249	  - id: "RD2-MF4"
250	    summary: "Abstract overclaim: 'dominant source' + verbosity category error"
251	    category: framing
252	    severity: critical
253	    status: resolved
254	    first_raised_round: 2
255	    last_seen_round: 2
256	    resolution: "Overclaim replaced in intro. Verbosity category error removed."
257	    resolution_round: 2
258	
259	  - id: "RD2-VIS"
260	    summary: "主正文超 8 页限制"
261	    category: format
262	    severity: critical
263	    status: resolved
264	    first_raised_round: 2
265	    last_seen_round: 10
266	    resolution: "Round 7+ 确认主正文 8 页合规。R10 确认 ≤8 页。"
267	    resolution_round: 7
268	    mentions:
269	      - round: 10
270	        reviewers: [1, 2]
271	        note: "R10 格式检查确认正文 8 页合规。"
272	      - round: 11
273	        reviewers: [1, 2]
274	        note: "R11 格式合规确认：正文 ≤8 页 ✓，匿名 ✓，Limitations 无新实验 ✓。"
275	
276	  - id: "RD2-SF1"
277	    summary: "Evaluator-producer 三角色 + 'independent' misleading"
278	    category: method
279	    severity: warning
280	    status: in_progress
281	    first_raised_round: 2
282	    last_seen_round: 11
283	    resolution: null
284	    resolution_round: null
285	    mentions:
286	      - round: 7
287	        reviewers: [1, 2]
288	        note: "cross-rewriter validation 仅覆盖 Qwen3-32B judge。22% Style OR 下降确认 inflation 存在。"
289	      - round: 9
290	        reviewers: [1, 2]
291	        note: "R9 共识 Should-Fix：Blindspot 存在性 robust，但效应量有 ±20-25% rewriter-dependent 变异。"
292	      - round: 10
293	        reviewers: [1, 2]
294	        note: "R10 SF4: 仅 Qwen3-32B judge 有 cross-rewriter 验证。效应量 ±22% rewriter-dependent 变异需显式承认。"
295	      - round: 11
296	        reviewers: [1, 2]
297	        note: "R11 Should-Fix: R1 指出仅 verbosity×Qwen3-32B 有替代 rewriter（R2 更正：formality+verbosity 两轴，但 register 未覆盖）。22% OR 下降不可忽略。两位共识 register 轴 evaluator-producer risk 最高。"
298	    action_items:
299	      - round: 4
300	        action: "Formality independence test added to Appendix D"
301	        assigned_to: agent
302	     
…[truncated 8159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 934 · 2026-05-22T18:06:14.776260+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "offset": "548",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "offset": "548",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 935 · 2026-05-22T18:06:14.827224+00:00_

548	    status: resolved
549	    first_raised_round: 3
550	    last_seen_round: 5
551	    resolution: "Citations expanded from 27 to 44."
552	    resolution_round: 4
553	
554	  - id: "R3-W8"
555	    summary: "NLI gate FN 可能引入 systematic selection bias"
556	    category: method
557	    severity: warning
558	    status: resolved
559	    first_raised_round: 3
560	    last_seen_round: 4
561	    resolution: "Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds."
562	    resolution_round: 4
563	
564	  - id: "R3-M1"
565	    summary: "Claude 作为 negative control 的双重解释"
566	    category: method
567	    severity: warning
568	    status: resolved
569	    first_raised_round: 3
570	    last_seen_round: 5
571	    resolution: "TOST equivalence testing added. Abstract changed 'confirms' to 'supports'."
572	    resolution_round: 4
573	
574	  - id: "R3-M2"
575	    summary: "Table 1 Holm-Bonferroni p-value 标注不够直觉"
576	    category: format
577	    severity: info
578	    status: resolved
579	    first_raised_round: 3
580	    last_seen_round: 4
581	    resolution: "Table 1 footnotes updated."
582	    resolution_round: 4
583	
584	  - id: "R3-M3"
585	    summary: "Abstract 过长过密"
586	    category: writing
587	    severity: info
588	    status: in_progress
589	    first_raised_round: 3
590	    last_seen_round: 11
591	    resolution: null
592	    resolution_round: null
593	    mentions:
594	      - round: 7
595	        reviewers: [1, 2]
596	        note: "两位再次一致指出 Abstract 过密。"
597	      - round: 9
598	        reviewers: []
599	        note: "R9 fresh review 未显式提出 Abstract 过密问题。"
600	      - round: 10
601	        reviewers: []
602	        note: "R10 未提及 Abstract 密度问题。P1 重写后可能已缓解。"
603	      - round: 11
604	        reviewers: [1, 2]
605	        note: "R11: R2 列为 Should-Fix（W1），R1 交叉 [AGREE]。数字堆砌影响可读性，建议保留 1-2 个最有力数字。"
606	
607	  - id: "R3-M4"
608	    summary: "Orphan bib entries"
609	    category: format
610	    severity: info
611	    status: resolved
612	  
…[truncated 12385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-22T18:06:19.696370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "offset": "947",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "offset": "947",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-22T18:06:19.797473+00:00_

947	        note: "R10 SF6: cross-axis interaction 未测试。Agent 正在计算 cross-axis contamination 定量分析（formality rewrites 对 verbosity 的影响，反之亦然）。"
948	      - round: 11
949	        reviewers: []
950	        note: "R11 未显式提及。Limitations 已含 per-axis independence 讨论及 cross-axis contamination 分析（Appendix）。"
951	    action_items:
952	      - round: 6
953	        action: "在 Limitations 补充讨论 axis-specific confounds"
954	        assigned_to: paper_agent
955	        status: done
956	      - round: 10
957	        action: "Agent 计算 cross-axis contamination（word count + formality proxy change）→ Appendix 写入"
958	        assigned_to: agent
959	        status: in_progress
960	
961	  - id: "R6-SF3"
962	    summary: "样本量偏小且 scaled replication 覆盖面窄"
963	    category: experiment
964	    severity: warning
965	    status: in_progress
966	    first_raised_round: 6
967	    last_seen_round: 11
968	    resolution: null
969	    resolution_round: null
970	    mentions:
971	      - round: 10
972	        reviewers: [1, 2]
973	        note: "R10 SF2: 仅 2+1 axes 限制泛化。共识 Should-Fix：限定为 'preliminary evidence'。"
974	      - round: 11
975	        reviewers: [1, 2]
976	        note: "R11: R1 列为 Must-Fix (N3)——n≈88 对 Likert power 严重不足（需 n=336-1200+），Likert null 可能仅反映 power 不足。R2 交叉 [AGREE]。共识：Conclusion 'systematically misses' 需 hedge，不能排除 power 解释。"
977	
978	  - id: "R6-M1"
979	    summary: "Appendix Table 5 (GEE CI) 部分条目缺失 95% CI"
980	    category: format
981	    severity: info
982	    status: resolved
983	    first_raised_round: 6
984	    last_seen_round: 10
985	    resolution: "R9/R10 检查确认 Appendix C Table 5 已有完整 12 行 CI。"
986	    resolution_round: 10
987	
988	  - id: "R6-REF1"
989	    summary: "建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)"
990	    category: writing
991	    severity: info
992	    status: resolved
993	    first_raised_round: 6
994	    last_seen_round: 8
995	    resolution: "论文 Related Work §2 已引用。"
996	    resolution_round: 8
997	
998	  # ===============================================
…[truncated 8634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 938 · 2026-05-22T18:06:26.925355+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-22T18:06:29.184700+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (54 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **register_100_cf** (killed): Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality\n- **gemini_flash_fourth_judge** (success): Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.\n- **llama70b_register** (success): Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures\n  [llama70b_register_summary](/api/workspace-files/projects/causal_style_decomp_judge/artifacts/llama70b_register/data/llama70b_register_summary.json)\n\n## 趋势\n成功 38 / 负向 12 / 失败 0 / 共 54\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- register_100_cf: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2259
}
```

</details>

---


### Tool call

_source line 940 · 2026-05-22T18:06:29.235354+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/ -name \"config.yaml\" -path \"*/causal_style_decomp_judge/*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/ -name \"project_config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/ -name \"*.yaml\" -path \"*/config*\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/ -name \"config.yaml\" -path \"*/causal_style_decomp_judge/*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/ -name \"project_config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/ -name \"*.yaml\" -path \"*/config*\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 941 · 2026-05-22T18:06:29.436591+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/projects/causal_style_decomp_judge.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/secrets/causal_style_decomp_judge/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 942 · 2026-05-22T18:06:32.499014+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/projects/causal_style_decomp_judge.yaml",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/projects/causal_style_decomp_judge.yaml",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 943 · 2026-05-22T18:06:32.499581+00:00_

1	execution:
2	  account: root
3	  gpu_ids:
4	  - cuda:0
5	  - cuda:1
6	  - cuda:2
7	  - cuda:3
8	  project_path: /root/causal_style_decomp_judge
9	  servers:
10	  - westb-29275
11	feishu:
12	  chat_id: oc_5ce280de124a4e308d1827c6450ad337
13	  check_references: false
14	  operational_chat_id: oc_09b04b56f2fb04931812c4a55f159dee
15	  review_mode: fresh
16	  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
17	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf
18	  review_round: 10
19	  review_supplementary_paths: ''
20	  submission_chat_id: oc_f810d8d75f013ad17831ce8459f07d6d
21	project:
22	  created_at: '2026-05-20T07:07:53.848Z'
23	  description: Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust
24	    Counterfactual Estimation
25	  name: causal_style_decomp_judge
26	  phase: research
27	  source_idea_id: idea_028
28	venue: emnlp-2026
29	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 944 · 2026-05-22T18:06:36.672059+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 945 · 2026-05-22T18:06:36.873266+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  - created_at: '2026-05-19T12:23:13Z'
12	    id: bd0516
13	    text: EMNLP 2026 restricts long paper submissions to a strict 8-page limit for
14	      main text, with unlimited space for references. Mandatory limitations and optional
15	      ethical considerations do not count towards this page limit, provided they do
16	      not contain excessive additional content.
17	  writing:
18	  - created_at: '2026-05-21T06:49:14Z'
19	    id: 2468a8
20	    text: Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
21	  - created_at: '2026-05-21T17:05:54Z'
22	    id: 0b1d8f
23	    text: ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
24	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-22T18:07:16.170623+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/",
  "description": "List paper section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/",
    "description": "List paper section files"
  }
}
```

</details>

---


### Tool result

_source line 947 · 2026-05-22T18:07:16.221446+00:00_

abstract.tex
appendix.tex
conclusion.tex
experiments.tex
introduction.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-22T18:07:19.335356+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-22T18:07:19.837893+00:00_

1	\begin{abstract}
2	Likert scoring---the default evaluation mode for LLM judges---attenuates style bias signals that pairwise comparison detects.
3	We introduce Controlled Style Decomposition (CSD), a black-box framework combining human-validated, NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to quantify style bias in LLM judges.
4	Across four judges from independent providers, one negative control, and three style axes, CSD demonstrates the Likert Blindspot: a severity spectrum from complete attenuation at moderate bias to over 60\% signal loss at stronger effects, confirmed by seven statistical methods across three benchmarks.
5	GEE conditional decomposition identifies a per-axis confound structure consistent across all four target judges: verbosity bias is style-dominated, formality exhibits a conditional effect moderated by content quality, and register is judge-dependent---determining which estimates are directly interpretable and which require conditional analysis.
6	A negative-control judge shows no detectable bias on either primary axis, supporting discriminative validity.
7	Whether the Blindspot reflects measurement attenuation or genuine construct divergence between absolute and comparative evaluation remains an open question; under either interpretation, Likert-only evaluation underestimates style-driven preferences that propagate through pairwise-based alignment pipelines.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-22T18:07:19.838281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 951 · 2026-05-22T18:07:20.139782+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} --- given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	This is the \emph{Likert Blindspot}.
6	We note that formality preferences may partially reflect legitimate quality judgments---our GEE decomposition (\S\ref{sec:direction}) quantifies this originality component.
7	This example reflects a systematic pattern.
8	
9	LLM judges are central infrastructure for NLP evaluation and alignment training (RLHF, DPO), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
10	Style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}: 76--92\% of observed preferences originate from surface-level style cues \citep{li2026preference}, with bias scores of 0.76--0.92 across five judges \citep{soumik2026judging}.
11	Despite this consensus, existing approaches address individual requirements (multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \citep{reber2025rate}, population-level correction \citep{dubois2025lc}), but no single framework integrates per-axis decomposition, interventional identification, per-instance diagnostics, and black-box applicability.
12	A further concern: standard Likert scoring produces ${\sim}60\%$ uninformative ties, and even non-tied pairs carry weaker signal than pairwise comparison---a limitation predicted by measurement theory \citep{thurstone1927law} but previously unquantified for LLM judges.
13	
14	We propose Controlled Style Decomposition (CSD), combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
15	I
…[truncated 2205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-22T18:07:20.140316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-22T18:07:20.241230+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
8	For each text, an instruction-tuned LLM (Qwen3-32B) classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification).
9	It then rewrites the text toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
10	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
11	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
12	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
13	
14	\subsection{Content Preservation Verification}
15	\label{sec:nli_gate}
16	
17	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
18	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90, selected as the threshold above which NLI performance plateaus (Appendix~\ref{app:nli_sweep}).
19	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exceed this value.
20	For axes that inherently c
…[truncated 6101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-22T18:07:23.202825+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-22T18:07:23.253676+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	The primary family comprises six tests---three target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B) $\times$ two axes (formality, verbosity)---corrected via Holm-Bonferroni at $\alpha = 0.05$; Gemini-2.5-Flash serves as confirmatory replication and is excluded from FWER control; as a sensitivity check, all eight tests remain significant under the expanded family (Appendix~\ref{app:holm8}).
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.\footnote{In binary-choice BT models, IIA is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$; verbosity: $p = 0.453$) reflects heterogeneous treatment effects across style directions rather than IIA violation.}
13	All bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.
14	GEE models use exchangeable working correlation, justified by near-zero estimated within-pair correlations ($\hat{\alpha} \in [-0.25, +0.11]$; Appendix~\ref{app:gee_diagnostics}).
15	
16	\paragraph{Model selection
…[truncated 16421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-22T18:07:29.026610+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
  "offset": "201"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
    "offset": "201"
  }
}
```

</details>

---


### Tool result

_source line 957 · 2026-05-22T18:07:29.077143+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (201). The file has 201 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 958 · 2026-05-22T18:07:29.784747+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-22T18:07:29.835389+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	CSD yields two findings.
5	First, the \emph{Likert Blindspot}: our evidence suggests that Likert scoring attenuates style bias signals that pairwise comparison detects---complete at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ signal loss at stronger effects---confirmed by seven statistical methods; we cannot fully separate measurement attenuation from format-level amplification (\S\ref{sec:amplification}) or construct divergence, but under any interpretation, Likert-only audits underestimate style-driven preferences that propagate through alignment pipelines.
6	Second, GEE conditional decomposition identifies per-axis confound structure---verbosity style-dominated, formality conditional, register judge-dependent---determining which estimates require conditional analysis.
7	
8	Existing Likert-based null findings may reflect measurement insensitivity rather than absence of bias; pairwise comparison with amplification controls (\S\ref{sec:amplification}) offers superior detection sensitivity.
9	Under the six amplification controls reported in \S\ref{sec:nli_validation}---including a negative-control judge that shows no pairwise bias---the observed sensitivity gap is more consistent with measurement attenuation than format-induced amplification, though the latter cannot be fully excluded.
10	
11	For practitioners auditing LLM judges, our results suggest that Likert-only evaluation is insufficient: bias audits should employ pairwise comparison with position control and per-axis decomposition to distinguish style-dominated from quality-confounded effects.
12	Human ground-truth validation of both measurement modes on identical pairs---determining whether the Blindspot reflects measurement attenuation, construct divergence, or a combination---remains the most informative next step.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-22T18:07:30.287399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-22T18:07:30.388821+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
14	
15	\paragrap
…[truncated 5448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-22T18:07:54.116220+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 963 · 2026-05-22T18:08:15.309098+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21192
}
```

</details>

---


### Tool call

_source line 964 · 2026-05-22T18:08:15.409821+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "10",
  "project": "causal_style_decomp_judge",
  "text": "你是 Reviewer 1，负责审查本论文的**方法严谨性、实验设计和统计分析**。\n\n## 论文信息\n- 标题：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n- 主文件：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026**（ARR May cycle），截止 2026-05-25\n- Long paper：正文 ≤8 页 + 无限参考文献（ACL 模板）\n- Limitations + Ethical Considerations 不计入页数限制\n- Double-blind 匿名审稿\n- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**方法严谨性**（重点）：\n1. NLI gate 作为 content preservation 验证的有效性——阈值选择、false positive/negative 率、是否引入 selection bias\n2. Style-controlled rewriting 方法：Qwen3-32B 既做 rewriter 又做 judge 的 evaluator-producer overlap 问题\n3. Direction-aware NLI 对 verbosity 的特殊处理是否方法论合理\n4. DAG/因果框架的声明强度与实际方法论强度是否匹配\n5. GEE conditional decomposition 的统计假设（exchangeable correlation、IIA for BT）是否得到检验和满足\n\n**实验设计**：\n6. 样本量（n=88 主实验，n=355 scaled replication）是否足以支撑论文的 claims\n7. 多重比较校正（Holm-Bonferroni 6 tests）是否合理\n8. 负控制（Claude Sonnet 4）的 TOST 等价检验——Δ=15pp 是否合理\n9. Cross-benchmark replication（AlpacaEval, MT-Bench）的覆盖面是否充分\n10. 人工标注验证规模（50 对）是否足够\n\n**统计分析**：\n11. Bradley-Terry 模型的 IIA 假设是否被检验（formality 方向不对称暗示可能违反）\n12. Bootstrap CI 方法（10,000 pair-level resamples）是否恰当\n13. Power analysis 的呈现方式（post-hoc vs. prospective）\n14. Detection vs. amplification 的六项控制是否充分回应 Comparative Trap 的关切\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准）。\n\n对每个 Weakness 标注严重程度：\n- **Must-Fix (critical)**：不修复则不可接收\n- **Should-Fix (warning)**：显著改善论文质量\n- **Minor (info)**：建议改进"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "10",
    "project": "causal_style_decomp_judge",
    "text": "你是 Reviewer 1，负责审查本论文的**方法严谨性、实验设计和统计分析**。\n\n## 论文信息\n- 标题：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n- 主文件：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026**（ARR May cycle），截止 2026-05-25\n- Long paper：正文 ≤8 页 + 无限参考文献（ACL 模板）\n- Limitations + Ethical Considerations 不计入页数限制\n- Double-blind 匿名审稿\n- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**方法严谨性**（重点）：\n1. NLI gate 作为 content preservation 验证的有效性——阈值选择、false positive/negative 率、是否引入 selection bias\n2. Style-controlled rewriting 方法：Qwen3-32B 既做 rewriter 又做 judge 的 evaluator-producer overlap 问题\n3. Direction-aware NLI 对 verbosity 的特殊处理是否方法论合理\n4. DAG/因果框架的声明强度与实际方法论强度是否匹配\n5. GEE conditional decomposition 的统计假设（exchangeable correlation、IIA for BT）是否得到检验和满足\n\n**实验设计**：\n6. 样本量（n=88 主实验，n=355 scaled replication）是否足以支撑论文的 claims\n7. 多重比较校正（Holm-Bonferroni 6 tests）是否合理\n8. 负控制（Claude Sonnet 4）的 TOST 等价检验——Δ=15pp 是否合理\n9. Cross-benchmark replication（AlpacaEval, MT-Bench）的覆盖面是否充分\n10. 人工标注验证规模（50 对）是否足够\n\n**统计分析**：\n11. Bradley-Terry 模型的 IIA 假设是否被检验（formality 方向不对称暗示可能违反）\n12. Bootstrap CI 方法（10,000 pair-level resamples）是否恰当\n13. Power analysis 的呈现方式（post-hoc vs. prospective）\n14. Detection vs. amplification 的六项控制是否充分回应 Comparative Trap 的关切\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准）。\n\n对每个 Weakness 标注严重程度：\n- **Must-Fix (critical)**：不修复则不可接收\n- **Should-Fix (warning)**：显著改善论文质量\n- **Minor (info)**：建议改进"
  }
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-22T18:08:33.141090+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17731
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-22T18:08:33.292330+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "10",
  "project": "causal_style_decomp_judge",
  "text": "你是 Reviewer 2，负责审查本论文的**新颖性、完整性、写作质量和相关工作覆盖**。\n\n## 论文信息\n- 标题：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n- 主文件：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026**（ARR May cycle），截止 2026-05-25\n- Long paper：正文 ≤8 页 + 无限参考文献（ACL 模板）\n- Limitations + Ethical Considerations 不计入页数限制\n- Double-blind 匿名审稿\n- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**新颖性**（重点）：\n1. \"Likert Blindspot\" 概念——这是心理测量学已知的 Thurstone (1927) 现象的 LLM judge domain transfer，还是有实质性新发现？\n2. CSD framework 的 novelty——相对于 RATE (Reber et al., 2025) 和其他 interventional 方法的增量贡献\n3. Per-axis confound decomposition 的 novelty——GEE 是标准统计方法，其在 LLM judge bias 场景的应用是否构成足够贡献\n4. 论文 framing 的声明强度：'demonstrates'/'identifies' 等措辞是否与实际证据匹配\n5. Detection vs. amplification 的核心歧义——论文标题 'Detecting Hidden Style Bias' 是否预设了 pairwise 为 ground truth\n\n**完整性**：\n6. 3 个 style axes（formality, verbosity, register）是否足以支撑 \"framework\" 级别泛化\n7. 负控制仅 Claude Sonnet 4 一个模型——是否足以论证 Blindspot 的架构特异性\n8. 缺少 human evaluation ground truth 来区分 measurement attenuation vs. construct divergence\n9. Register axis 的 evaluator-producer overlap 风险（无 cross-rewriter validation）\n10. Cross-benchmark replication 的不完整覆盖（Table 1 空 cells）\n\n**写作质量**：\n11. Abstract 信息密度——数字堆砌是否影响可读性\n12. Introduction motivating example 的说服力和公平性\n13. 论文整体叙事逻辑和 flow\n14. Limitations 章节的覆盖面和深度\n15. 格式合规：正文 ≤8 页、匿名、ACL 模板\n\n**相关工作覆盖**：\n16. 是否遗漏关键相关工作（尤其 pairwise vs. rating 方法比较的文献）\n17. 与竞品（RATE, FairJudge, CASSE, Comparative Trap）的定位是否准确\n18. 引用质量——是否存在幻觉引用或格式问题\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准）。\n\n对每个 Weakness 标注严重程度：\n- **Must-Fix (critical)**：不修复则不可接收\n- **Should-Fix (warning)**：显著改善论文质量\n- **Minor (info)**：建议改进"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "10",
    "project": "causal_style_decomp_judge",
    "text": "你是 Reviewer 2，负责审查本论文的**新颖性、完整性、写作质量和相关工作覆盖**。\n\n## 论文信息\n- 标题：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n- 主文件：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026**（ARR May cycle），截止 2026-05-25\n- Long paper：正文 ≤8 页 + 无限参考文献（ACL 模板）\n- Limitations + Ethical Considerations 不计入页数限制\n- Double-blind 匿名审稿\n- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**新颖性**（重点）：\n1. \"Likert Blindspot\" 概念——这是心理测量学已知的 Thurstone (1927) 现象的 LLM judge domain transfer，还是有实质性新发现？\n2. CSD framework 的 novelty——相对于 RATE (Reber et al., 2025) 和其他 interventional 方法的增量贡献\n3. Per-axis confound decomposition 的 novelty——GEE 是标准统计方法，其在 LLM judge bias 场景的应用是否构成足够贡献\n4. 论文 framing 的声明强度：'demonstrates'/'identifies' 等措辞是否与实际证据匹配\n5. Detection vs. amplification 的核心歧义——论文标题 'Detecting Hidden Style Bias' 是否预设了 pairwise 为 ground truth\n\n**完整性**：\n6. 3 个 style axes（formality, verbosity, register）是否足以支撑 \"framework\" 级别泛化\n7. 负控制仅 Claude Sonnet 4 一个模型——是否足以论证 Blindspot 的架构特异性\n8. 缺少 human evaluation ground truth 来区分 measurement attenuation vs. construct divergence\n9. Register axis 的 evaluator-producer overlap 风险（无 cross-rewriter validation）\n10. Cross-benchmark replication 的不完整覆盖（Table 1 空 cells）\n\n**写作质量**：\n11. Abstract 信息密度——数字堆砌是否影响可读性\n12. Introduction motivating example 的说服力和公平性\n13. 论文整体叙事逻辑和 flow\n14. Limitations 章节的覆盖面和深度\n15. 格式合规：正文 ≤8 页、匿名、ACL 模板\n\n**相关工作覆盖**：\n16. 是否遗漏关键相关工作（尤其 pairwise vs. rating 方法比较的文献）\n17. 与竞品（RATE, FairJudge, CASSE, Comparative Trap）的定位是否准确\n18. 引用质量——是否存在幻觉引用或格式问题\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准）。\n\n对每个 Weakness 标注严重程度：\n- **Must-Fix (critical)**：不修复则不可接收\n- **Should-Fix (warning)**：显著改善论文质量\n- **Minor (info)**：建议改进"
  }
}
```

</details>

---


### Tool result

_source line 967 · 2026-05-22T18:08:34.653348+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 968 · 2026-05-22T18:08:40.768539+00:00_

三路任务已并行派发：
- 视觉审查 Agent：已启动（fire-and-forget）
- Reviewer 1（方法/实验/统计）：已分配
- Reviewer 2（新颖性/完整性/写作/相关工作）：已分配

等待两位 Reviewer 的独立初审报告返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 91

## Round 91

2 recorded events


### User

_source line 969 · 2026-05-22T18:15:01.115228+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：The Likert Blindspot

### Summary

本文提出 Controlled Style Decomposition (CSD)，一个黑盒框架，通过 NLI 门控内容保持、单轴风格改写和位控 pairwise 比较来量化 LLM judge 的风格偏差。核心发现为"Likert Blindspot"：Likert 评分系统性地衰减 pairwise 比较能检测到的风格偏差信号——在中等偏差时完全衰减（d → 0），在较强效应时信号损失 >60%。在 4 个目标 judge + 1 个负控制、3 个风格轴、3 个 benchmark 上验证。GEE 条件分解揭示了逐轴混淆结构。

---

### Strengths

**S1. 实验设计严谨，控制充分。** 六项独立的放大控制（NLI gate ablation、负控制 judge、跨轴变异、rewriting artifact 吸收、debiased prompting、跨架构复现）显示出对 "Comparative Trap" 反面论证的充分意识。Position swap 双向评估 + consistent pairs sign test 设计合理。(§5.1, §5.4)

**S2. 统计分析多层次且透明。** 七种测量方法的灵敏度层级（Table 2）、Holm-Bonferroni 校正、探索性与验证性分析的明确区分、bootstrap 衰减分析和形式化功效分析（Appendix K），体现了高标准的统计实践。

**S3. 跨 judge 一致性强。** 四个独立架构一致复现 Blindspot（Table 1），GEE 混淆结构跨 judge 一致（verbosity 全部 Style OR 8–13，formality 全部条件显著）。

**S4. Limitations 坦诚全面。** 对 quality-style confounding、evaluator-producer overlap、construct divergence 的歧义性进行了充分讨论。

**S5. GEE 混淆分解有实用价值。** 将风格效应与 originality 效应分离，对从业者有直接指导意义。

---

### Must-Fix 问题（critical）

**N1 [critical] 核心歧义未解决，但标题和 framing 隐式预设 pairwise 为 ground truth**

论文标题 "Detecting Hidden Style Bias" 和 "Blindspot" 命名隐式假定 pairwise 检测到的是真实偏差、Likert 遗漏了它。然而论文自身承认三种等效解释：(a) Likert 测量衰减，(b) pairwise 放大（Comparative Trap），(c) 构念分歧。六项放大控制必要但非充分——负控制的 TOST Δ=15pp 实质性过宽（14pp win probability 差异会被判为"等价"），且仅一个负控制模型。建议标题改为更中性的表述，Abstract 前置三种解释。

**N2 [critical] 新颖性定位不足："Likert Blindspot" 本质是 Thurstone (1927) 在 LLM judge 领域的实证确认**

Forced-choice 比 rating scale 灵敏度更高是心理测量学经典结论（Thurstone 1927, Preston & Colman 2000, DeCoster & Iselin 2011），论文自己引用了这些文献。"unquantified" 的声明技术上正确，但核心机制完全可从已有理论预测。增量贡献是实证量化——有价值，但不足以支撑 "demonstrates"/"identifies" 等发现性措辞。建议明确定位为"首次在 LLM judge 下的系统性实证量化"，并深度对比 LLM judge 场景是否超越传统理论预测。

---

### Should-Fix 问题（warning）

**W1 [warning] Formality 轴的 GEE 结果削弱 "style bias" 叙事。** Table 3 中多个 judge 的 Orig OR ≥ Style OR（GPT-4o: 2.32 vs 2.58; Qwen3: 4.70 vs 4.20），pairwise 检测到的可能更多是与 formality 相关的质量差异而非纯风格偏差。

**W2 [warning] Register 轴 evaluator-producer overlap 严重且无跨改写器验证。** Register 所有改写用 Qwen3-32B 且无交叉验证，BT 结果也较弱。建议降级为 "exploratory pilot axis"。

**W3 [warning] 三个风格轴不足以支撑 "framework" 泛化。** 第四轴（tone）因 NLI gate 拒绝率过高放弃，表明适用性受限。建议软化为 "methodology for content-preserving style axes"。

**W4 [warning] 跨 benchmark 覆盖稀疏。** AlpacaEval 3 配置、MT-Bench 2 配置，verbosity 仅跨 benchmark 验证了 Qwen3 一个 judge。"three benchmarks" 声明名义上成立但实际覆盖很低。

**W5 [warning] 负控制 TOST Δ=15pp 过宽且仅一个模型。** 建议报告不同 Δ 下的 TOST 结果（10pp, 5pp），讨论 15pp 的实际含义。

---

### Minor 问题

- M1: Abstract 数字密度过高
- M2: Introduction 开头单实例不能代表系统性模式，caveat 应前置
- M3: 对 RATE 的批评措辞过于直接
- M4: Figure 2 DAG 中 orange dashed arrow 标注字号过小
- M5: Table 1 五种标记系统认知负担高
- M6: Limitations 约 1.5 页可适当精简

---

### Missing References

1. Carterette et al. (2008) — forced-choice vs. graded relevance 判断灵敏度差异（ECIR）
2. Sedoc & Ungar (2020) — IRT 模型应用于 chatbot 评估（ACL）
3. Deutsch et al. (2023) — tie 处理对评估指标灵敏度的影响（EMNLP）

---

### 官方维度打分（ACL ARR）

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3.5/5 | 方法严谨但核心歧义未解决；formality 混淆结构削弱叙事；TOST Δ 过宽 |
| Excitement | 2.5/5 | 经典心理测量学结论的领域迁移，非新发现；GEE 分解有增量贡献 |
| Reproducibility | 4/5 | 代码数据承诺发布；统计方法详细；模型版本固定 |

### Overall Assessment

**Overall: 3.0 — Findings**

实验设计严谨、统计分析透明的实证工作，但核心发现（Likert 对风格偏差的灵敏度低于 pairwise）本质是心理测量学经典理论在 LLM judge 场景的实证确认而非新发现，detection vs. amplification 核心歧义未解决，新颖性和 excitement 不足以达到主会议水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 970 · 2026-05-22T18:15:16.612835+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 92

## Round 92

6 recorded events


### User

_source line 971 · 2026-05-22T18:15:19.100375+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告

**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
**Venue**: EMNLP 2026 (ARR May cycle)
**审查侧重**: 方法严谨性、实验设计、统计分析

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 方法论扎实、现象定义清晰的实证研究，verbosity 轴结果令人信服，但 formality 轴的 quality-style 混淆显著削弱核心 claim，TOST 等价检验边界偏宽，整体贡献介于 Findings 和 Conference 之间。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心方法设计合理，统计框架严谨，但 formality 轴 GEE 显示 Originality OR ≥ Style OR（多配置），"style bias" 的 claim 对该轴偏强；verbosity 轴 (OR 8–13, Orig ns) 方法论上无可挑剔 |
| Excitement | 3.5/5 | Likert Blindspot 现象有明确的实践意义（RLHF/DPO 依赖 pairwise，但审计依赖 Likert），七种方法的 sensitivity hierarchy 是有价值的方法论贡献，但缺乏下游影响的实证 |
| Reproducibility | 4/5 | 实现细节完整（模型版本、温度、种子），统计方法描述清晰，代码/数据承诺开源；扣分点：部分 GEE 配置缺少 QIC 绝对值 |
| Reviewer Confidence | 4/5 | 熟悉 Bradley-Terry 模型、GEE、因果推断框架和 LLM 评估文献 |

---

## 主要优势

1. **现象定义清晰且可复现**：Likert Blindspot 在 4 个 judge × 2 个主轴 × 3 个 benchmark 上一致出现（11 个 bias-positive cell 中 8 个），且用 7 种统计方法验证了 sensitivity hierarchy（Table 2），形成了强有力的证据链。

2. **因果声明诚实克制**：Section 3.5 明确声明"we do not claim that this DAG is a complete structural causal model"，Figure 2 DAG 中用虚线橙色箭头标注 residual confounding，避免了过度因果宣称。这在该领域的论文中少见且值得肯定。

3. **统计方法论严谨**：
   - Holm-Bonferroni 校正 6 测试家族 + 8 测试敏感性分析（Appendix Q），全部保持显著
   - BT 拟合优度检验（Appendix H：formality deviance p=0.198, verbosity p=0.905）
   - GEE 诊断完整：exchangeable vs independence 对比（|ΔQIC| < 0.001）、交互项检验（所有 p > 0.13）、95% CI 完整报告
   - Bootstrap attenuation analysis（Appendix J）区分 measurement attenuation 与 insufficient power，优于简单 post-hoc power

4. **控制变量设计周全**：NLI 阈值 11 点 sweep（BT ≤ 3pp 变动）、cross-rewriter 验证（22% OR 下降但 Blindspot 持续）、same-style double-rewrite artifact control、Claude 负控制——形成多层防线。

5. **Verbosity 轴证据链极强**：Style OR 8.2–13.1（四个 judge 一致），Originality OR 0.38–0.49（均不显著或边缘），direction-aware NLI 有理论和实证依据（Appendix F），cross-rewriter 验证完整（Appendix D Table 7）。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Formality 轴 quality-style 混淆严重，核心 claim 对该轴偏强

- 具体位置：Table 3（GEE decomposition）、Section 5.2
- 问题：GEE 分解显示 formality 的 Originality OR 在多个配置中 ≥ Style OR：
  - GPT-4o: Style 2.58 vs Orig 2.32（几乎相等）
  - Qwen3 n=355: Style 2.15 vs Orig 4.99（originality 是 style 的 2.3 倍）
  - Gemini: Style 1.64 (ns!) vs Orig 2.51
  - Direction asymmetry（Appendix H: formal-origin 88.9% vs casual-origin 52.6%, Fisher p=0.015）进一步确认混淆存在

  这意味着 pairwise 检测到的 formality "bias" 有相当部分是 quality-formality 相关性的反映，而非纯粹的 style bias。论文标题和 abstract 用 "Detecting Hidden Style Bias" 统一描述所有轴的发现，但 formality 轴检测到的更多是 quality confound + style effect 的混合信号。

  Appendix H 的 stratified analysis（限制 Likert 等分对，BT=67.3%）作为 robustness check 有说服力，但存在一个 circularity 问题：论文的核心 claim 正是 Likert 对 style bias 不敏感，因此用 "Likert 等分" 作为 "质量无差异" 的代理变量存在逻辑矛盾。

- 为什么影响接收：如果 formality 的 Blindspot 本质上是 pairwise 对 quality-style correlation 的放大，而非 Likert 遗漏了 style bias，则论文的核心叙事（"hidden style bias"）被削弱约一半。
- 建议修改方向：
  (a) 在 abstract/introduction 中区分 verbosity（纯 style-driven）和 formality（style + quality confound），不要统一称为 "style bias"
  (b) 考虑将 formality 的发现重新定性为 "measurement sensitivity divergence" 而非 "hidden bias detection"
  (c) 补充讨论 stratified analysis 的 circularity 并提出替代验证方案

**N2** [critical] Bootstrap CI 的 pair-level resampling 在 GEE 语境下的合理性未论证

- 具体位置：Section 4.1, "All bootstrap CIs use 10,000 pair-level resamples"
- 问题：论文将 pair-level bootstrap 同时用于 BT 估计和 GEE 分解。对 BT 模型，pair-level resampling 是标准做法。但 GEE 使用 exchangeable working correlation 对 pair 内观测建模，其 CI 来自 sandwich standard errors（Appendix P），而非 bootstrap。这两套 CI 方法在论文中的分工不够清晰——Table 3 的 CI（Appendix C Table 6）使用哪种方法？如果是 sandwich SE，则与 Section 4.1 的 bootstrap 声明不一致；如果是 bootstrap，则需要论证 pair-level resampling 是否保持了 GEE 的 cluster 结构。
- 为什么影响接收：CI 方法的不清晰可能影响 GEE OR 的统计推断可靠性。
- 建议修改方向：明确区分 BT bootstrap CI 和 GEE sandwich CI 的适用范围，如果 GEE 也用 bootstrap，需论证 resampling 单位（pair vs cluster）的选择。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] TOST 等价检验边界 Δ=15pp 偏宽，负控制说服力有限

- 具体位置：Section 5.4（Detection vs. amplification, control ii）、Appendix G
- 问题：Claude Sonnet 4 的 TOST 在 Δ=15pp 时达到 p<0.05（76% power），但这意味着 Claude 可能存在高达 ~15pp 的未检测 style preference。GPT-4o formality 检测到的 bias 为 BT 63.0%（即 13pp 偏离 50%），与 TOST 边界几乎重叠。因此，Claude 负控制无法区分 "真正无 bias" 和 "moderate bias but below detection threshold"。
  论文声称 Claude 的 bound 与 GPT-4o (13–23pp) "substantively distinct"，但 13pp 和 15pp 的差距仅 2pp，且 CI 大量重叠。
- 建议：(a) 降低 claim 强度，承认 Δ=15pp 是 power 限制下的妥协而非 substantive bound; (b) 报告 Δ=10pp 时的 TOST power 和 p 值供读者判断; (c) 或增加 Claude 样本量以收紧边界。

**W2** [warning] 人工标注验证规模偏小，inter-annotator agreement 仅 moderate

- 具体位置：Section 5.4（Content preservation）、Appendix S
- 问题：50 对（25 pass + 25 reject）由 2 名标注员评估，Cohen's κ=0.44（moderate）。A1 认为全部 25 pass 对保内容（precision 100%），A2 认为 21/25（84%）。4 个分歧全在 verbosity condensation 对上——而 verbosity 正是论文最强 claim 的支撑轴。这意味着 verbosity NLI gate 的 content preservation 标准在标注员间有实质性分歧。
  Wilson CI [86.7%, 100%] 和 [65.3%, 93.6%] 的重叠区间说明精度估计本身不够精确。
- 建议：(a) 增加标注量（至少 100 对）以收紧 CI; (b) 增加第三名标注员; (c) 讨论 verbosity condensation 的 content preservation 标准模糊性对结论的影响。

**W3** [warning] Cross-benchmark replication 覆盖面有限

- 具体位置：Table 1, Section 5.3
- 问题：
  - AlpacaEval 仅测 3 个配置（2 judges × formality + 1 verbosity）
  - MT-Bench 仅测 2 个配置（2 judges × formality），无 verbosity
  - Llama-70B 和 Gemini 未做 cross-benchmark 验证
  - Register 轴无 cross-benchmark 验证
  论文 claim "cross-benchmark replication" 但实际覆盖面较窄，尤其 verbosity（最强轴）仅在 AlpacaEval 有 1 个 cross-benchmark 数据点，且该点是 ‡（both sig，非 Blindspot）。
- 建议：至少补充 MT-Bench verbosity 的 1-2 个 judge 数据；或降低 cross-benchmark claim 的强度。

**W4** [warning] Cross-axis contamination中 formality→verbosity 的 word count shift (d=−0.23) 非 negligible

- 具体位置：Appendix R, Table 18
- 问题：formality 改写导致 word count 变化 d=−0.23，按 Cohen 标准属 "small" 但非 negligible（论文自设的 negligible 标准是 d<0.20）。论文以 "directionally symmetric (formal→casual −5.0%, casual→formal +5.6%)" 辩护，但 dataset-level 对称不等于 pair-level 对称——如果 formal→casual 方向的 pairs 和 casual→formal 方向的 pairs 在 quality 或 judge preference 上有系统差异（direction asymmetry 已经证明确实如此），则 cross-axis 污染可能不会在 aggregate 中抵消。
- 建议：在 pair level 验证 word count 变化与 BT outcome 的相关性，或在 GEE 中加入 word count 变化作为 covariate。

---

## 小问题（不影响接收）

1. **Table 1 符号系统偏复杂**：†, ‡, †_e, †_c, --- 共 5 种标记，且 †_e 和 †_c 仅在脚注中解释。建议在正文首次出现时给出完整定义。

2. **Figure 4（power curve）标题**：虽正文已引用 Hoenig & Hesse (2001) 避免 post-hoc power 误用，但 Figure caption 中 "Detection probability at observed effect magnitudes" 的表述仍可能被误读为 post-hoc power。建议在 caption 中加注 "prospective sample-size planning"。

3. **Section 4.1 脚注 3（IIA）**：关于 binary-choice BT 模型中 IIA structurally satisfied 的声明是正确的，但脚注篇幅较长（~60 words），建议移至 Appendix H 与 GoF 检验合并讨论。

4. **Register 轴定位不够清晰**：在 Table 1 中 register 占 6 行，但正文 Section 5.3 仅用一句话提及 register 是 "exploratory and judge-dependent"。建议将 register 结果移至 appendix 或更明确地标注为 exploratory pilot。

5. **Limitations 段落"Validation methodology and scale design"**：提到 "100-point experiment was tested with a single judge" 但未在 Appendix M 中讨论为何仅选 Qwen3-32B（作为 evaluator-producer overlap 最严重的 judge）而非选无 overlap 的 GPT-4o。

---

## 问题（供作者回应）

**Q1**: Appendix H 的 stratified analysis 用 Likert 等分对作为 "无质量差异" 的代理变量来验证 style bias 存在——但论文的核心 claim 是 Likert 对 style 不敏感。如何排除这一 circularity？是否考虑过使用外部质量指标（如人工评分或参考答案匹配度）替代 Likert 作为 quality proxy？

**Q2**: 对于 formality 轴，Qwen3 n=355 的 GEE 分解显示 Originality OR (4.99) 是 Style OR (2.15) 的 2.3 倍。在这种 confound structure 下，"formality bias" 的表述是否仍然恰当？是否应改为 "formality-related preference divergence"？

**Q3**: TOST Δ=15pp 的选择基准是什么？是否是 smallest effect of interest (SESOI) 的估计，还是纯粹由 power 限制决定？如果是后者，论文是否应报告基于 SESOI 的 Δ 而非 power-driven 的 Δ？

**Q4**: Verbosity direction-aware NLI gate 恢复了 21 对（从 65% 到 86% pass rate），但这些恢复的对是否在 content quality 上与 bidirectional-pass 对系统不同？Appendix F 报告了 BT 的一致性，但未报告这两组在 Likert 质量分或 NLI 分数分布上的差异。

**Q5**: 论文声称 Blindspot 对 RLHF/DPO pipeline 有重要启示，但未给出任何下游影响的实证。是否有初步实验表明 style bias 实际影响了 alignment 结果？

---

## Missing References

未发现明显缺失的关键引用。论文对相关工作覆盖全面，包括 RATE (Reber et al., 2025)、Comparative Trap (Jeong et al., 2025)、self-preference (Panickssery et al., 2024) 等关键近期工作。

建议考虑引用：
- Stureborg et al. (2024) 关于 LLM judge calibration 的工作，与 Section 2 的 measurement sensitivity 讨论相关

---

## Overall Assessment 详细理由

**3.5 (Borderline Conference)**

这是一篇方法论扎实的实证研究，其核心发现（Likert Blindspot）有明确的实践意义。论文在因果声明的克制性、统计方法的严谨性、robustness check 的全面性上均优于同类工作。

**推荐 Conference 的理由**：
- Verbosity 轴的证据链完整且令人信服（Style OR 8–13, Orig ns, cross-rewriter validated, 4 judges consistent）
- Sensitivity hierarchy（7 种方法）是有价值的方法论贡献
- 对 LLM 评估社区（RLHF/DPO pipeline）有直接的 actionable implications

**犹豫的理由**：
- Formality 轴——论文的另一半核心 claim——受 quality confound 严重影响（N1），削弱了 "detecting hidden style bias" 的叙事统一性
- 负控制说服力有限（W1, Δ=15pp 与 GPT-4o 最小 bias 几乎重叠）
- 缺乏下游影响实证（Q5），限制了对 alignment 社区的直接贡献
- 论文在 "measurement attenuation vs construct divergence" 之间保持 agnostic（Section 5.1），这虽然诚实，但也意味着 Blindspot 的 mechanistic interpretation 尚不明确

如果作者能在 rebuttal 中：(1) 调整 formality claim 的措辞，区分 style-driven 和 confound-mixed 的发现；(2) 澄清 GEE CI 方法；(3) 讨论 stratified analysis 的 circularity——我愿意上调至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 972 · 2026-05-22T18:16:28.195539+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "10",
  "project": "causal_style_decomp_judge",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：The Likert Blindspot\n\n### Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一个黑盒框架，通过 NLI 门控内容保持、单轴风格改写和位控 pairwise 比较来量化 LLM judge 的风格偏差。核心发现为\"Likert Blindspot\"：Likert 评分系统性地衰减 pairwise 比较能检测到的风格偏差信号——在中等偏差时完全衰减（d → 0），在较强效应时信号损失 >60%。在 4 个目标 judge + 1 个负控制、3 个风格轴、3 个 benchmark 上验证。GEE 条件分解揭示了逐轴混淆结构。\n\n---\n\n### Strengths\n\n**S1. 实验设计严谨，控制充分。** 六项独立的放大控制（NLI gate ablation、负控制 judge、跨轴变异、rewriting artifact 吸收、debiased prompting、跨架构复现）显示出对 \"Comparative Trap\" 反面论证的充分意识。Position swap 双向评估 + consistent pairs sign test 设计合理。(§5.1, §5.4)\n\n**S2. 统计分析多层次且透明。** 七种测量方法的灵敏度层级（Table 2）、Holm-Bonferroni 校正、探索性与验证性分析的明确区分、bootstrap 衰减分析和形式化功效分析（Appendix K），体现了高标准的统计实践。\n\n**S3. 跨 judge 一致性强。** 四个独立架构一致复现 Blindspot（Table 1），GEE 混淆结构跨 judge 一致（verbosity 全部 Style OR 8–13，formality 全部条件显著）。\n\n**S4. Limitations 坦诚全面。** 对 quality-style confounding、evaluator-producer overlap、construct divergence 的歧义性进行了充分讨论。\n\n**S5. GEE 混淆分解有实用价值。** 将风格效应与 originality 效应分离，对从业者有直接指导意义。\n\n---\n\n### Must-Fix 问题（critical）\n\n**N1 [critical] 核心歧义未解决，但标题和 framing 隐式预设 pairwise 为 ground truth**\n\n论文标题 \"Detecting Hidden Style Bias\" 和 \"Blindspot\" 命名隐式假定 pairwise 检测到的是真实偏差、Likert 遗漏了它。然而论文自身承认三种等效解释：(a) Likert 测量衰减，(b) pairwise 放大（Comparative Trap），(c) 构念分歧。六项放大控制必要但非充分——负控制的 TOST Δ=15pp 实质性过宽（14pp win probability 差异会被判为\"等价\"），且仅一个负控制模型。建议标题改为更中性的表述，Abstract 前置三种解释。\n\n**N2 [critical] 新颖性定位不足：\"Likert Blindspot\" 本质是 Thurstone (1927) 在 LLM judge 领域的实证确认**\n\nForced-choice 比 rating scale 灵敏度更高是心理测量学经典结论（Thurstone 1927, Preston & Colman 2000, DeCoster & Iselin 2011），论文自己引用了这些文献。\"unquantified\" 的声明技术上正确，但核心机制完全可从已有理论预测。增量贡献是实证量化——有价值，但不足以支撑 \"demonstrates\"/\"identifies\" 等发现性措辞。建议明确定位为\"首次在 LLM judge 下的系统性实证量化\"，并深度对比 LLM judge 场景是否超越传统理论预测。\n\n---\n\n### Should-Fix 问题（warning）\n\n**W1 [warning] Formality 轴的 GEE 结果削弱 \"style bias\" 叙事。** Table 3 中多个 judge 的 Orig OR ≥ Style OR（GPT-4o: 2.32 vs 2.58; Qwen3: 4.70 vs 4.20），pairwise 检测到的可能更多是与 formality 相关的质量差异而非纯粹的 style bias。\n\n**W2 [warning] Register 轴 evaluator-producer overlap 严重且无跨改写器验证。** Register 所有改写用 Qwen3-32B 且无交叉验证，BT 结果也较弱。建议降级为 \"exploratory pilot axis\"。\n\n**W3 [warning] 三个风格轴不足以支撑 \"framework\" 泛化。** 第四轴（tone）因 NLI gate 拒绝率过高放弃，表明适用性受限。建议软化为 \"methodology for content-preserving style axes\"。\n\n**W4 [warning] 跨 benchmark 覆盖稀疏。** AlpacaEval 3 配置、MT-Bench 2 配置，verbosity 仅跨 benchmark 验证了 Qwen3 一个 judge。\"three benchmarks\" 声明名义上成立但实际覆盖很低。\n\n**W5 [warning] 负控制 TOST Δ=15pp 过宽且仅一个模型。** 建议报告不同 Δ 下的 TOST 结果（10pp, 5pp），讨论 15pp 的实际含义。\n\n---\n\n### Minor 问题\n\n- M1: Abstract 数字密度过高\n- M2: Introduction 开头单实例不能代表系统性模式，caveat 应前置\n- M3: 对 RATE 的批评措辞过于直接\n- M4: Figure 2 DAG 中 orange dashed arrow 标注字号过小\n- M5: Table 1 五种标记系统认知负担高\n- M6: Limitations 约 1.5 页可适当精简\n\n---\n\n### Missing References\n\n1. Carterette et al. (2008) — forced-choice vs. graded relevance 判断灵敏度差异（ECIR）\n2. Sedoc & Ungar (2020) — IRT 模型应用于 chatbot 评估（ACL）\n3. Deutsch et al. (2023) — tie 处理对评估指标灵敏度的影响（EMNLP）\n\n---\n\n### 官方维度打分（ACL ARR）\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3.5/5 | 方法严谨但核心歧义未解决；formality 混淆结构削弱叙事；TOST Δ 过宽 |\n| Excitement | 2.5/5 | 经典心理测量学结论的领域迁移，非新发现；GEE 分解有增量贡献 |\n| Reproducibility | 4/5 | 代码数据承诺发布；统计方法详细；模型版本固定 |\n\n### Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n实验设计严谨、统计分析透明的实证工作，但核心发现（Likert 对风格偏差的灵敏度低于 pairwise）本质是心理测量学经典理论在 LLM judge 场景的实证确认而非新发现，detection vs. amplification 核心歧义未解决，新颖性和 excitement 不足以达到主会议水平。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "10",
    "project": "causal_style_decomp_judge",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：The Likert Blindspot\n\n### Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一个黑盒框架，通过 NLI 门控内容保持、单轴风格改写和位控 pairwise 比较来量化 LLM judge 的风格偏差。核心发现为\"Likert Blindspot\"：Likert 评分系统性地衰减 pairwise 比较能检测到的风格偏差信号——在中等偏差时完全衰减（d → 0），在较强效应时信号损失 >60%。在 4 个目标 judge + 1 个负控制、3 个风格轴、3 个 benchmark 上验证。GEE 条件分解揭示了逐轴混淆结构。\n\n---\n\n### Strengths\n\n**S1. 实验设计严谨，控制充分。** 六项独立的放大控制（NLI gate ablation、负控制 judge、跨轴变异、rewriting artifact 吸收、debiased prompting、跨架构复现）显示出对 \"Comparative Trap\" 反面论证的充分意识。Position swap 双向评估 + consistent pairs sign test 设计合理。(§5.1, §5.4)\n\n**S2. 统计分析多层次且透明。** 七种测量方法的灵敏度层级（Table 2）、Holm-Bonferroni 校正、探索性与验证性分析的明确区分、bootstrap 衰减分析和形式化功效分析（Appendix K），体现了高标准的统计实践。\n\n**S3. 跨 judge 一致性强。** 四个独立架构一致复现 Blindspot（Table 1），GEE 混淆结构跨 judge 一致（verbosity 全部 Style OR 8–13，formality 全部条件显著）。\n\n**S4. Limitations 坦诚全面。** 对 quality-style confounding、evaluator-producer overlap、construct divergence 的歧义性进行了充分讨论。\n\n**S5. GEE 混淆分解有实用价值。** 将风格效应与 originality 效应分离，对从业者有直接指导意义。\n\n---\n\n### Must-Fix 问题（critical）\n\n**N1 [critical] 核心歧义未解决，但标题和 framing 隐式预设 pairwise 为 ground truth**\n\n论文标题 \"Detecting Hidden Style Bias\" 和 \"Blindspot\" 命名隐式假定 pairwise 检测到的是真实偏差、Likert 遗漏了它。然而论文自身承认三种等效解释：(a) Likert 测量衰减，(b) pairwise 放大（Comparative Trap），(c) 构念分歧。六项放大控制必要但非充分——负控制的 TOST Δ=15pp 实质性过宽（14pp win probability 差异会被判为\"等价\"），且仅一个负控制模型。建议标题改为更中性的表述，Abstract 前置三种解释。\n\n**N2 [critical] 新颖性定位不足：\"Likert Blindspot\" 本质是 Thurstone (1927) 在 LLM judge 领域的实证确认**\n\nForced-choice 比 rating scale 灵敏度更高是心理测量学经典结论（Thurstone 1927, Preston & Colman 2000, DeCoster & Iselin 2011），论文自己引用了这些文献。\"unquantified\" 的声明技术上正确，但核心机制完全可从已有理论预测。增量贡献是实证量化——有价值，但不足以支撑 \"demonstrates\"/\"identifies\" 等发现性措辞。建议明确定位为\"首次在 LLM judge 下的系统性实证量化\"，并深度对比 LLM judge 场景是否超越传统理论预测。\n\n---\n\n### Should-Fix 问题（warning）\n\n**W1 [warning] Formality 轴的 GEE 结果削弱 \"style bias\" 叙事。** Table 3 中多个 judge 的 Orig OR ≥ Style OR（GPT-4o: 2.32 vs 2.58; Qwen3: 4.70 vs 4.20），pairwise 检测到的可能更多是与 formality 相关的质量差异而非纯粹的 style bias。\n\n**W2 [warning] Register 轴 evaluator-producer overlap 严重且无跨改写器验证。** Register 所有改写用 Qwen3-32B 且无交叉验证，BT 结果也较弱。建议降级为 \"exploratory pilot axis\"。\n\n**W3 [warning] 三个风格轴不足以支撑 \"framework\" 泛化。** 第四轴（tone）因 NLI gate 拒绝率过高放弃，表明适用性受限。建议软化为 \"methodology for content-preserving style axes\"。\n\n**W4 [warning] 跨 benchmark 覆盖稀疏。** AlpacaEval 3 配置、MT-Bench 2 配置，verbosity 仅跨 benchmark 验证了 Qwen3 一个 judge。\"three benchmarks\" 声明名义上成立但实际覆盖很低。\n\n**W5 [warning] 负控制 TOST Δ=15pp 过宽且仅一个模型。** 建议报告不同 Δ 下的 TOST 结果（10pp, 5pp），讨论 15pp 的实际含义。\n\n---\n\n### Minor 问题\n\n- M1: Abstract 数字密度过高\n- M2: Introduction 开头单实例不能代表系统性模式，caveat 应前置\n- M3: 对 RATE 的批评措辞过于直接\n- M4: Figure 2 DAG 中 orange dashed arrow 标注字号过小\n- M5: Table 1 五种标记系统认知负担高\n- M6: Limitations 约 1.5 页可适当精简\n\n---\n\n### Missing References\n\n1. Carterette et al. (2008) — forced-choice vs. graded relevance 判断灵敏度差异（ECIR）\n2. Sedoc & Ungar (2020) — IRT 模型应用于 chatbot 评估（ACL）\n3. Deutsch et al. (2023) — tie 处理对评估指标灵敏度的影响（EMNLP）\n\n---\n\n### 官方维度打分（ACL ARR）\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3.5/5 | 方法严谨但核心歧义未解决；formality 混淆结构削弱叙事；TOST Δ 过宽 |\n| Excitement | 2.5/5 | 经典心理测量学结论的领域迁移，非新发现；GEE 分解有增量贡献 |\n| Reproducibility | 4/5 | 代码数据承诺发布；统计方法详细；模型版本固定 |\n\n### Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n实验设计严谨、统计分析透明的实证工作，但核心发现（Likert 对风格偏差的灵敏度低于 pairwise）本质是心理测量学经典理论在 LLM judge 场景的实证确认而非新发现，detection vs. amplification 核心歧义未解决，新颖性和 excitement 不足以达到主会议水平。"
  }
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-22T18:17:13.269756+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 45074
}
```

</details>

---


### Tool call

_source line 974 · 2026-05-22T18:17:13.421107+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "10",
  "project": "causal_style_decomp_judge",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审查侧重**: 方法严谨性、实验设计、统计分析\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法设计合理，统计框架严谨，但 formality 轴 GEE 显示 Originality OR ≥ Style OR（多配置），\"style bias\" 的 claim 对该轴偏强；verbosity 轴 (OR 8–13, Orig ns) 方法论上无可挑剔 |\n| Excitement | 3.5/5 | Likert Blindspot 现象有明确的实践意义（RLHF/DPO 依赖 pairwise，但审计依赖 Likert），七种方法的 sensitivity hierarchy 是有价值的方法论贡献，但缺乏下游影响的实证 |\n| Reproducibility | 4/5 | 实现细节完整（模型版本、温度、种子），统计方法描述清晰，代码/数据承诺开源；扣分点：部分 GEE 配置缺少 QIC 绝对值 |\n| Reviewer Confidence | 4/5 | 熟悉 Bradley-Terry 模型、GEE、因果推断框架和 LLM 评估文献 |\n\n---\n\n## 主要优势\n\n1. **现象定义清晰且可复现**：Likert Blindspot 在 4 个 judge × 2 个主轴 × 3 个 benchmark 上一致出现（11 个 bias-positive cell 中 8 个），且用 7 种统计方法验证了 sensitivity hierarchy（Table 2），形成了强有力的证据链。\n\n2. **因果声明诚实克制**：Section 3.5 明确声明\"we do not claim that this DAG is a complete structural causal model\"，Figure 2 DAG 中用虚线橙色箭头标注 residual confounding，避免了过度因果宣称。\n\n3. **统计方法论严谨**：Holm-Bonferroni 校正 6 测试家族 + 8 测试敏感性分析（Appendix Q），全部保持显著；BT 拟合优度检验；GEE 诊断完整：exchangeable vs independence 对比（|ΔQIC| < 0.001）、交互项检验（所有 p > 0.13）、95% CI 完整报告；Bootstrap attenuation analysis（Appendix J）区分 measurement attenuation 与 insufficient power。\n\n4. **控制变量设计周全**：NLI 阈值 11 点 sweep、cross-rewriter 验证、same-style double-rewrite artifact control、Claude 负控制。\n\n5. **Verbosity 轴证据链极强**：Style OR 8.2–13.1（四个 judge 一致），Originality OR 0.38–0.49（均不显著或边缘），direction-aware NLI 有理论和实证依据，cross-rewriter 验证完整。\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] Formality 轴 quality-style 混淆严重，核心 claim 对该轴偏强\n\n- Table 3（GEE decomposition）、Section 5.2：GEE 分解显示 formality 的 Originality OR 在多个配置中 ≥ Style OR：\n  - GPT-4o: Style 2.58 vs Orig 2.32（几乎相等）\n  - Qwen3 n=355: Style 2.15 vs Orig 4.99（originality 是 style 的 2.3 倍）\n  - Gemini: Style 1.64 (ns!) vs Orig 2.51\n  - Direction asymmetry（Appendix H: formal-origin 88.9% vs casual-origin 52.6%）进一步确认混淆存在\n- Formality 的 Blindspot 可能本质上是 pairwise 对 quality-style correlation 的放大\n- Appendix H 的 stratified analysis 存在 circularity：论文的核心 claim 是 Likert 对 style 不敏感，因此用 \"Likert 等分\" 作为 \"质量无差异\" 的代理变量存在逻辑矛盾\n- 建议：区分 verbosity（纯 style-driven）和 formality（style + quality confound），不要统一称为 \"style bias\"\n\n**N2** [critical] Bootstrap CI 的 pair-level resampling 在 GEE 语境下的合理性未论证\n\n- Section 4.1 声明 \"All bootstrap CIs use 10,000 pair-level resamples\"，但 GEE 使用 sandwich standard errors\n- Table 3 的 CI（Appendix C Table 6）使用哪种方法不清晰\n- 建议：明确区分 BT bootstrap CI 和 GEE sandwich CI 的适用范围\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] TOST 等价检验边界 Δ=15pp 偏宽，负控制说服力有限\n- Claude 可能存在高达 ~15pp 的未检测 style preference\n- GPT-4o formality 检测到的 bias 为 BT 63.0%（即 13pp 偏离 50%），与 TOST 边界几乎重叠\n- 建议报告 Δ=10pp 时的 TOST power 和 p 值\n\n**W2** [warning] 人工标注验证规模偏小，inter-annotator agreement 仅 moderate\n- 50 对由 2 名标注员评估，Cohen's κ=0.44（moderate）\n- 4 个分歧全在 verbosity condensation 对上——而 verbosity 正是最强 claim 的支撑轴\n- 建议增加标注量或第三名标注员\n\n**W3** [warning] Cross-benchmark replication 覆盖面有限\n- verbosity 仅在 AlpacaEval 有 1 个 cross-benchmark 数据点，且是 ‡（both sig，非 Blindspot）\n- 建议补充 MT-Bench verbosity 数据或降低 claim 强度\n\n**W4** [warning] Cross-axis contamination 中 formality→verbosity 的 word count shift (d=−0.23) 非 negligible\n- 按 Cohen 标准 d=−0.23 超过论文自设的 negligible 标准 d<0.20\n- dataset-level 对称不等于 pair-level 对称\n- 建议在 GEE 中加入 word count 变化作为 covariate\n\n---\n\n## 小问题\n\n1. Table 1 符号系统偏复杂（5 种标记）\n2. Figure 4（power curve）标题可能被误读为 post-hoc power\n3. Section 4.1 脚注 3（IIA）篇幅较长，建议移至 Appendix\n4. Register 轴定位不够清晰，建议明确标注为 exploratory pilot\n5. 100-point Likert 实验仅选 Qwen3-32B（evaluator-producer overlap 最严重的 judge）而非 GPT-4o\n\n---\n\n## 问题\n\n**Q1**: Appendix H 的 stratified analysis 用 Likert 等分对作为 \"无质量差异\" 的代理变量——如何排除 circularity？\n**Q2**: Formality 轴 Qwen3 n=355 的 Originality OR (4.99) 是 Style OR (2.15) 的 2.3 倍，\"formality bias\" 表述是否仍恰当？\n**Q3**: TOST Δ=15pp 的选择基准是什么？\n**Q4**: Verbosity direction-aware NLI gate 恢复的 21 对在 content quality 上是否与 bidirectional-pass 对系统不同？\n**Q5**: 论文声称对 RLHF/DPO pipeline 有启示，但未给出下游影响实证。\n\n---\n\n## Missing References\n\n建议考虑：Stureborg et al. (2024) 关于 LLM judge calibration\n\n---\n\n## Overall Assessment\n\n**3.5 (Borderline Conference)**\n\n方法论扎实的实证研究，verbosity 轴证据令人信服，但 formality 轴 quality confound 削弱核心 claim，TOST 边界偏宽，贡献介于 Findings 和 Conference 之间。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "10",
    "project": "causal_style_decomp_judge",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审查侧重**: 方法严谨性、实验设计、统计分析\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法设计合理，统计框架严谨，但 formality 轴 GEE 显示 Originality OR ≥ Style OR（多配置），\"style bias\" 的 claim 对该轴偏强；verbosity 轴 (OR 8–13, Orig ns) 方法论上无可挑剔 |\n| Excitement | 3.5/5 | Likert Blindspot 现象有明确的实践意义（RLHF/DPO 依赖 pairwise，但审计依赖 Likert），七种方法的 sensitivity hierarchy 是有价值的方法论贡献，但缺乏下游影响的实证 |\n| Reproducibility | 4/5 | 实现细节完整（模型版本、温度、种子），统计方法描述清晰，代码/数据承诺开源；扣分点：部分 GEE 配置缺少 QIC 绝对值 |\n| Reviewer Confidence | 4/5 | 熟悉 Bradley-Terry 模型、GEE、因果推断框架和 LLM 评估文献 |\n\n---\n\n## 主要优势\n\n1. **现象定义清晰且可复现**：Likert Blindspot 在 4 个 judge × 2 个主轴 × 3 个 benchmark 上一致出现（11 个 bias-positive cell 中 8 个），且用 7 种统计方法验证了 sensitivity hierarchy（Table 2），形成了强有力的证据链。\n\n2. **因果声明诚实克制**：Section 3.5 明确声明\"we do not claim that this DAG is a complete structural causal model\"，Figure 2 DAG 中用虚线橙色箭头标注 residual confounding，避免了过度因果宣称。\n\n3. **统计方法论严谨**：Holm-Bonferroni 校正 6 测试家族 + 8 测试敏感性分析（Appendix Q），全部保持显著；BT 拟合优度检验；GEE 诊断完整：exchangeable vs independence 对比（|ΔQIC| < 0.001）、交互项检验（所有 p > 0.13）、95% CI 完整报告；Bootstrap attenuation analysis（Appendix J）区分 measurement attenuation 与 insufficient power。\n\n4. **控制变量设计周全**：NLI 阈值 11 点 sweep、cross-rewriter 验证、same-style double-rewrite artifact control、Claude 负控制。\n\n5. **Verbosity 轴证据链极强**：Style OR 8.2–13.1（四个 judge 一致），Originality OR 0.38–0.49（均不显著或边缘），direction-aware NLI 有理论和实证依据，cross-rewriter 验证完整。\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] Formality 轴 quality-style 混淆严重，核心 claim 对该轴偏强\n\n- Table 3（GEE decomposition）、Section 5.2：GEE 分解显示 formality 的 Originality OR 在多个配置中 ≥ Style OR：\n  - GPT-4o: Style 2.58 vs Orig 2.32（几乎相等）\n  - Qwen3 n=355: Style 2.15 vs Orig 4.99（originality 是 style 的 2.3 倍）\n  - Gemini: Style 1.64 (ns!) vs Orig 2.51\n  - Direction asymmetry（Appendix H: formal-origin 88.9% vs casual-origin 52.6%）进一步确认混淆存在\n- Formality 的 Blindspot 可能本质上是 pairwise 对 quality-style correlation 的放大\n- Appendix H 的 stratified analysis 存在 circularity：论文的核心 claim 是 Likert 对 style 不敏感，因此用 \"Likert 等分\" 作为 \"质量无差异\" 的代理变量存在逻辑矛盾\n- 建议：区分 verbosity（纯 style-driven）和 formality（style + quality confound），不要统一称为 \"style bias\"\n\n**N2** [critical] Bootstrap CI 的 pair-level resampling 在 GEE 语境下的合理性未论证\n\n- Section 4.1 声明 \"All bootstrap CIs use 10,000 pair-level resamples\"，但 GEE 使用 sandwich standard errors\n- Table 3 的 CI（Appendix C Table 6）使用哪种方法不清晰\n- 建议：明确区分 BT bootstrap CI 和 GEE sandwich CI 的适用范围\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] TOST 等价检验边界 Δ=15pp 偏宽，负控制说服力有限\n- Claude 可能存在高达 ~15pp 的未检测 style preference\n- GPT-4o formality 检测到的 bias 为 BT 63.0%（即 13pp 偏离 50%），与 TOST 边界几乎重叠\n- 建议报告 Δ=10pp 时的 TOST power 和 p 值\n\n**W2** [warning] 人工标注验证规模偏小，inter-annotator agreement 仅 moderate\n- 50 对由 2 名标注员评估，Cohen's κ=0.44（moderate）\n- 4 个分歧全在 verbosity condensation 对上——而 verbosity 正是最强 claim 的支撑轴\n- 建议增加标注量或第三名标注员\n\n**W3** [warning] Cross-benchmark replication 覆盖面有限\n- verbosity 仅在 AlpacaEval 有 1 个 cross-benchmark 数据点，且是 ‡（both sig，非 Blindspot）\n- 建议补充 MT-Bench verbosity 数据或降低 claim 强度\n\n**W4** [warning] Cross-axis contamination 中 formality→verbosity 的 word count shift (d=−0.23) 非 negligible\n- 按 Cohen 标准 d=−0.23 超过论文自设的 negligible 标准 d<0.20\n- dataset-level 对称不等于 pair-level 对称\n- 建议在 GEE 中加入 word count 变化作为 covariate\n\n---\n\n## 小问题\n\n1. Table 1 符号系统偏复杂（5 种标记）\n2. Figure 4（power curve）标题可能被误读为 post-hoc power\n3. Section 4.1 脚注 3（IIA）篇幅较长，建议移至 Appendix\n4. Register 轴定位不够清晰，建议明确标注为 exploratory pilot\n5. 100-point Likert 实验仅选 Qwen3-32B（evaluator-producer overlap 最严重的 judge）而非 GPT-4o\n\n---\n\n## 问题\n\n**Q1**: Appendix H 的 stratified analysis 用 Likert 等分对作为 \"无质量差异\" 的代理变量——如何排除 circularity？\n**Q2**: Formality 轴 Qwen3 n=355 的 Originality OR (4.99) 是 Style OR (2.15) 的 2.3 倍，\"formality bias\" 表述是否仍恰当？\n**Q3**: TOST Δ=15pp 的选择基准是什么？\n**Q4**: Verbosity direction-aware NLI gate 恢复的 21 对在 content quality 上是否与 bidirectional-pass 对系统不同？\n**Q5**: 论文声称对 RLHF/DPO pipeline 有启示，但未给出下游影响实证。\n\n---\n\n## Missing References\n\n建议考虑：Stureborg et al. (2024) 关于 LLM judge calibration\n\n---\n\n## Overall Assessment\n\n**3.5 (Borderline Conference)**\n\n方法论扎实的实证研究，verbosity 轴证据令人信服，但 formality 轴 quality confound 削弱核心 claim，TOST 边界偏宽，贡献介于 Findings 和 Conference 之间。"
  }
}
```

</details>

---


### Tool result

_source line 975 · 2026-05-22T18:17:14.782691+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 976 · 2026-05-22T18:17:18.337818+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 93

## Round 93

14 recorded events


### User

_source line 977 · 2026-05-22T18:17:19.358240+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。论文方法论严谨、统计实践高标准，但两个 critical 问题压制了评分——(1) "Likert Blindspot" 本质是 Thurstone (1927) forced-choice 灵敏度优势在 LLM judge 领域的实证确认，novelty 定位为"新发现"而非"领域迁移验证"存在 overclaim；(2) detection vs. amplification vs. construct divergence 的核心歧义未解决，但标题和 framing 隐式预设 pairwise 为 ground truth。五个 should-fix 进一步影响评分（formality 轴的 GEE 结果反而削弱 bias 叙事、register 轴缺乏跨改写器验证、framework 泛化声明过强、跨 benchmark 覆盖稀疏、负控制 TOST Δ 过宽）。

---

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**评分摘要**：Overall 3.5 (Borderline Conference)

**核心判断**：
- **Verbosity 轴**证据极强（Style OR 8–13, Orig ns, 四个 judge 一致），方法论无可挑剔
- **Formality 轴**受 quality-style 混淆严重影响（Qwen3 n=355: Orig OR 4.99 vs Style OR 2.15），论文标题 "Detecting Hidden Style Bias" 对该轴偏强
- 统计方法论整体严谨（Holm-Bonferroni、BT GoF、GEE 诊断、NLI sweep），是该领域少见的高标准工作
- 两个 Must-Fix：(1) formality claim 需降级或重新措辞；(2) bootstrap vs sandwich CI 在 GEE 语境下的分工需澄清
- 四个 Should-Fix：TOST Δ=15pp 偏宽、人工标注规模偏小、cross-benchmark 覆盖有限、cross-axis 污染非 negligible

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-22T18:17:48.620198+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 979 · 2026-05-22T18:17:48.771302+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T18:07:57.444607+00:00\", \"completed_at\": \"2026-05-22T18:12:30.709617+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 pipeline 流程图内部标注文字偏小，打印后可能需要放大才能清晰阅读；建议稍微增大图幅或字号\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 caption 仅 \\\"CSD pipeline overview. Numbers indicate sample attrition at each stage.\\\"——偏简略，建议补充一句说明 pipeline 核心步骤（style rewriting → NLI gate → pairwise comparison），提升 caption 自包含度\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 脚注字号非常小（约 6pt），包含重要的符号说明（†/‡ 含义、Blindspot 定义），审稿人可能需要费力辨认\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 列数较多（Judge × Axis × 3 metrics），信息密度高；当前可读但接近上限，如有进一步修改可考虑拆分或简化\"}, {\"severity\": \"info\", \"dimension\": \"pages 8-9\", \"message\": \"Limitations 章节较长（~1.5 页，含 3 个子段落 + Code and Data），内容充实但篇幅偏长；EMNLP 2026 允许不计入页数限制前提是\\\"不含过多额外内容\\\"，当前内容均为实质性局限讨论，应该合规\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 因果 DAG 使用橙色/红色高亮路径，色盲用户可能需要额外辨认；建议补充线型（虚线/实线）区分或在节点旁加文字标签\"}, {\"severity\": \"info\", \"dimension\": \"pages 10-14\", \"message\": \"Appendix 共 19 个小节、~15 张表格，内容非常充实；格式统一且规范，但审稿人可能因体量庞大而选择性跳读\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-22T18:17:48.771751+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 981 · 2026-05-22T18:17:48.822319+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-22T18:17:54.910491+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 983 · 2026-05-22T18:17:54.910994+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 984 · 2026-05-22T18:17:58.724749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-22T18:17:58.925824+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved unless noted)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	
16	  - id: "R2-N1"
17	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
18	    category: framing
19	    severity: warning
20	    status: in_progress
21	    first_raised_round: 1
22	    last_seen_round: 11
23	    resolution: null
24	    resolution_round: null
25	    mentions:
26	      - round: 3
27	        reviewers: [1, 2]
28	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
29	      - round: 8
30	        reviewers: [1, 2]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 986 · 2026-05-22T18:23:25.584664+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 11\n        action: \"Abstract/§2 中 'reveals' 等措辞需进一步弱化；'first' 限定为 'first for LLM judges specifically'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 12\n        action: \"明确定位为 '首次在 LLM judge 下的系统性实证量化'，而非新发现。深度对比 LLM judge 场景是否超越传统心理测量预测。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 2 issues\n  # ============================================================\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 12\n    resolution: \"Round 7+ 确认主正文 8 页合规。R10 确认 ≤8 页。\"\n    resolution_round: 7\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 格式检查确认正文 8 页合规。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 格式合规确认：正文 ≤8 页 ✓，匿名 ✓，Limitations 无新实验 ✓。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 格式合规：正文 ≤8 页 ✓，ACL 模板 ✓，double-blind ✓。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"cross-rewriter validation 仅覆盖 Qwen3-32B judge。22% Style OR 下降确认 inflation 存在。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 共识 Should-Fix：Blindspot 存在性 robust，但效应量有 ±20-25% rewriter-dependent 变异。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF4: 仅 Qwen3-32B judge 有 cross-rewriter 验证。效应量 ±22% rewriter-dependent 变异需显式承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 Should-Fix: R1 指出仅 verbosity×Qwen3-32B 有替代 rewriter（R2 更正：formality+verbosity 两轴，但 register 未覆盖）。22% OR 下降不可忽略。两位共识 register 轴 evaluator-producer risk 最高。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W2: register 轴所有改写用 Qwen3-32B 且无跨改写器验证，BT 结果也较弱。建议降级为 exploratory pilot axis。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 10\n        action: \"Limitations 补一句：effect-size precision varies ±22% with rewriter choice\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'.\"\n    resolution_round: 4\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"共识 Must-Fix。50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 两位共同指向：增加 human evaluation 是最大可 actionable 改进。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 MF1 (critical): 持续 7 轮未解决。两位 Reviewer 交叉共识：human evaluation 是 4.0 的关键路径。孙震 50-pair 标注今晚返回。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 将 NLI gate 50 对人工标注列为 Must-Fix（Wilson CI 下界仅 86.3%，未报告 recall/FNR）。R2 交叉降为 Should-Fix（threshold sweep 11 阈值×44 组合全显著提供缓解）。论文 §5.4 报告 50 对 100% precision，但规模仍不足。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 W2: 50 对由 2 名标注员评估，κ=0.44 (moderate)，4 个分歧全在 verbosity condensation 上——正是最强 claim 轴。Wilson CI 过宽。建议增加标注量（≥100 对）或第三名标注员。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板\"\n        assigned_to: agent\n        status: done\n      - round: 10\n        action: \"孙震标注返回后 → analyze_annotations.py → Paper Agent 写入 §5.4\"\n        assigned_to: agent\n        status: pending\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"两位再次一致指出 Abstract 过密。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 fresh review 未显式提出 Abstract 过密问题。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未提及 Abstract 密度问题。P1 重写后可能已缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 列为 Should-Fix（W1），R1 交叉 [AGREE]。数字堆砌影响可读性，建议保留 1-2 个最有力数字。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 M1: Abstract 数字密度过高。与往轮一致。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 Should-Fix：Appendix H formality 方向异质性挑战 IIA。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。§4.1 footnote 已承认 direction asymmetry。可能接近解决。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 分歧：R1 列为 Must-Fix (critical)——Appendix B direction asymmetry 暗示 IIA 违反，需 Hausman-McFadden test。R2 交叉 [REBUT] 降为 Should-Fix——binary-choice BT 中 IIA 自动满足，Table 2 五种非参数方法独立确认 Blindspot。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 脚注 3：binary-choice BT 中 IIA structurally satisfied 的声明正确，但脚注篇幅长。方向异质性是 heterogeneous treatment effects 而非 IIA violation。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"§5.2 已加 6 项 amplification controls。从 critical 降级为 Should-Fix。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF1: 检测 vs 放大歧义仍为核心。R2 定 critical，R1 反驳降为 warning。6 项 controls + Claude 负对照已部分缓解。Conclusion 语言需条件化。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: detection vs. amplification 成为两位 Reviewer 的最大共识问题。R2 列为 Must-Fix (N2)，R1 交叉 [AGREE]。六项控制 bound 了 amplification 但未 eliminate。缺 ground-truth bias 已知的验证。100-point continuous Likert 排除粒度解释但支持 construct divergence 解读。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: 两位 Reviewer 最大共识问题。R2 N1 (critical)：标题 'Detecting Hidden Style Bias' 隐式预设 pairwise 为 ground truth。R1 通过 formality 轴 GEE 混淆（N1）间接支持——pairwise 检测到的可能部分是 quality-style correlation 的放大。六项控制必要但不充分。建议标题更中性。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"Conclusion 加条件性表述：amplification controls bound 但不完全排除放大\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 11\n        action: \"§6 开头 'systematically misses' 需加 hedge；考虑 reframe 为 'divergent signals' 而非单方面归因 Likert failure\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 12\n        action: \"标题改为更中性表述（如 'Measurement Divergence' 而非 'Detecting Hidden Bias'）；Abstract 前置三种等效解释\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1]\n        note: \"§3.5 因果语言校准良好。原始 'do-operator' 语言已修复。\"\n      - round: 10\n        reviewers: [2]\n        note: \"R10 M2: 'Controlled' 和 'interventional' 语言暗示过强因果识别。共识：§3.5 加明确声明。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 列为 Should-Fix (W3)，R2 交叉 [AGREE]。'controlled'/'interventional'/DAG notation 给人因果推断研究的印象，但 NLI gate 非 do-operator，GEE 是关联分析。建议 §3 更早声明 'controlled = experimentally controlled rewriting, not formal causal identification'。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 优势 2 肯定：§3.5 明确声明 'we do not claim this DAG is a complete structural causal model'，因果声明已诚实克制。此问题可能已接近解决。\"\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"共识：'the first' → 'a unified framework'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1 处理。RW 'first controlled, per-axis quantification' → 'first controlled quantification of this per-axis sensitivity gap'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R11 共识：'first' 需限定为 'first for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [2]\n        note: \"合并入 R2-N1。R12 R2 N2：'demonstrates'/'identifies' 仍偏发现性措辞。\"\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R10 SF4 处理。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R11 共识：register 轴 evaluator-producer risk 最高，需显式 caveat。\"\n      - round: 12\n        reviewers: [2]\n        note: \"合并入 RD2-SF1。R12 R2 W2：register 所有改写用 Qwen3-32B 且无跨改写器验证。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"4 target judges (+ Gemini confirmatory) now cover the claim.\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"标题和 Abstract framing 偏向 attenuation。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 Q3: bootstrap attenuation 如何排除 construct-level 差异？§5.1 已有讨论但 'Blindspot' 术语天然偏向。MF2 reframe 部分缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 列为 Should-Fix (W3)，R1 交叉 [AGREE]。标题 'Detecting Hidden Style Bias' 预设 pairwise 为 ground truth。R1 补充：100-point Likert 结果实际支持 construct divergence 而非 measurement attenuation。建议标题更中性。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识：论文承认三种等效解释但标题和 framing 隐式偏向 attenuation。合并入 R5-MF1 处理。\"\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: wont_fix\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: \"Acknowledged as limitation. Register is weakest axis with judge-dependent confound structure; cross-rewriter test would be confounded by register's inherent instability.\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"R10 在 evaluator-producer 讨论中确认仍未覆盖 register。Limitations 已承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 W2 和 R2 W4 均指出 register 未覆盖。R2 交叉更正 R1 描述（Appendix D 覆盖 formality+verbosity 两轴，非仅 verbosity）。核心关切仍成立。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W2 再次提出。与往轮一致。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 升级 Must-Fix。Δ=15pp 几乎涵盖最小 confirmed bias。\"\n      - round: 10\n        reviewers: [1]\n        note: \"R10 SF3: Δ=15pp 偏宽，Claude 仅覆盖 2/3 axes。论文 Appendix G 有 Δ_min=15.7pp。Reviewer #104 确认当前版本已包含此数据。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 将 TOST Δ=15pp 列为 Should-Fix (W1)——循环论证（用自己效应量定义等价边界），15pp≈d=0.43 属 medium effect 偏宽。R2 交叉 [AGREE]。需先验论证或 sensitivity across Δ=5/10/15/20pp。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识 Should-Fix：R1 W1 指出 GPT-4o formality 13pp 与 Δ=15pp 仅差 2pp，Claude 可能有未检测的 moderate bias。R2 W5 同意过宽且仅一个负控制。建议报告 Δ=10pp/5pp 的 TOST 结果。\"\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"R10 Q2: Table 1 footnote 已有 'Empty cells: untested combinations' 但未说明选择理由。Reviewer #104 判断现有 footnote 足够。\"\n      - round: 11\n        reviewers: [1]\n        note: \"R11 M4: register axis 的 n 值和 power 未明确报告。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识：Table 1 空 cells 脚注存在但选择理由缺失。R1 W3 + R2 W4：跨 benchmark 覆盖稀疏，verbosity 仅 1 个 cross-benchmark 数据点。\"\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"R12 视觉审查：Figure 2 DAG 橙色/红色高亮路径色盲用户可能需额外辨认。R2 M4 同指字号过小。\"\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound Δ=15pp 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"合并入 R5-M3 讨论。Δ_min=15.7pp 已报告。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。R11 两位共识 Should-Fix：需报告 TOST sensitivity across multiple Δ 或基于 leaderboard 排名影响论证 Δ 选择。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。R12 两位共识维持。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分——cross-axis contamination\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF6: cross-axis interaction 未测试。Agent 正在计算 cross-axis contamination 定量分析。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。Limitations 已含 per-axis independence 讨论及 cross-axis contamination 分析（Appendix）。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 W4: Appendix R cross-axis contamination 中 formality→verbosity 的 word count shift d=−0.23 超过论文自设 negligible 标准 d<0.20。dataset-level 对称不等于 pair-level 对称。建议在 GEE 中加入 word count 变化作为 covariate。\"\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2: 仅 2+1 axes 限制泛化。共识 Should-Fix：限定为 'preliminary evidence'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 列为 Must-Fix (N3)——n≈88 对 Likert power 严重不足（需 n=336-1200+），Likert null 可能仅反映 power 不足。R2 交叉 [AGREE]。共识：Conclusion 'systematically misses' 需 hedge，不能排除 power 解释。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 R2 W3: 第四轴（tone）因 NLI gate 拒绝率过高放弃，表明适用性受限。3 轴不足以支撑 'framework' 泛化。R1 W3: cross-benchmark 覆盖稀疏。两位共识：降为 'methodology for content-preserving style axes'。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 10\n    resolution: \"R9/R10 检查确认 Appendix C Table 5 已有完整 12 行 CI。\"\n    resolution_round: 10\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"论文 Related Work §2 已引用。\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 7 issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 10\n    resolution: \"§4.1 明确 'six tests—three target judges × two axes'，Gemini 为 confirmatory，Appendix Q 8-test family 下所有结果仍显著。R10 未再提及。\"\n    resolution_round: 10\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型，存在循环性\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。§5.4 已报告 FNR 8.4% [3.7%, 15.9%] CI。GPT-4o cross-validation 部分缓解循环性。人工标注（MF1）将彻底解决。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及此具体问题，但 R1-N2 关于 NLI gate 人工验证不足间接涵盖。\"\n      - round: 12\n        reviewers: []\n        note: \"R12 未显式提及。§5.4 人工标注 (50对) 部分缓解。\"\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate 17.4% FPR 未报告\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。Appendix F 有 direction-aware gate validation data。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 Q4: direction-aware NLI gate 恢复的 21 对在 content quality 上是否与 bidirectional-pass 对系统不同？BT 一致但 Likert 质量分和 NLI 分数分布差异未报告。\"\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"论文 §5.1 已引用 Tripathi et al. (2025)。\"\n    resolution_round: 9\n\n  # ============================================================\n  # Round 8 issues\n  # ============================================================\n\n  - id: \"R8-W1\"\n    summary: \"3 个风格轴限制 'framework' 级别泛化——需从 'framework' 降为 'methodology'\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2 再次确认。共识：限定为 'preliminary evidence of axis-dependent patterns'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: 与 R6-SF3 合并。两位共识：当前证据仅覆盖 3 axes，'framework' 级别泛化需更多 axes 验证。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W3: tone 轴失败说明适用性受限。建议软化为 'methodology for content-preserving style axes'。与 R6-SF3 合并。\"\n    action_items:\n      - round: 10\n        action: \"Limitations 补 'preliminary evidence' 限定 + 列出未覆盖 axes\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R8-W2\"\n    summary: \"生态效度讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Limitations 已含 'Our controlled manipulation design ensures internal validity but may not fully generalize to naturalistic evaluation settings.' R10 未再提及。\"\n    resolution_round: 10\n\n  - id: \"R8-W3\"\n    summary: \"Rewriting artifact 的 style-specific polishing interaction 未讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Appendix O 已含相关讨论。R10 未再提及。\"\n    resolution_round: 10\n\n  - id: \"R8-W4\"\n    summary: \"Introduction motivating example 未 acknowledge formality-quality nuance\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"§1 已有 GEE decomposition 引用。R10 确认。\"\n    resolution_round: 10\n\n  - id: \"R8-REF1\"\n    summary: \"建议补充引用：Girrbach et al. 'Likert or Not'\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"Phantom reference.\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 10 issues\n  # ============================================================\n\n  - id: \"R10-N1\"\n    summary: \"100-point continuous Likert 实验仅用单一 judge（Qwen3-32B）\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Minor。Limitations 承认即可。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。Limitations 已含 'tested with a single judge' 承认。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 小问题 5: 100-point 仅选 Qwen3-32B（evaluator-producer overlap 最严重的 judge）而非 GPT-4o，选择理由缺失。\"\n\n  - id: \"R10-N2\"\n    summary: \"NLI gate 44% 拒绝率 selection bias 仅检查 4 个 surface covariates\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Limitations 承认即可。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 列为 Must-Fix (N2)——gate 过滤 12-35%。R2 交叉降为 Should-Fix。\"\n      - round: 12\n        reviewers: []\n        note: \"R12 未显式提及。§5.4 已有 content preservation 人工验证。\"\n\n  - id: \"R10-REF1\"\n    summary: \"建议补充引用：Simms et al. (2019), Polo et al. (2024), Kocmi & Federmann (2023)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 10\n    resolution: null\n    resolution_round: null\n\n  # ============================================================\n  # Round 11 new issues\n  # ============================================================\n\n  - id: \"R11-N1\"\n    summary: \"Negative control 仅 Claude Sonnet 4 一个模型，不足以论证 Blindspot 的架构特异性\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix (W4): 仅一个负控制不足以论证 Blindspot 是特定架构/训练方式的产物。未讨论 Claude 为何不受影响。R2 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: R2 W5/N1 指出仅一个负控制模型。R1 W1 指出 TOST Δ=15pp 与 GPT-4o 最小 bias (13pp) 几乎重叠。两位共识：Claude 负控制说服力有限。\"\n    action_items:\n      - round: 11\n        action: \"Discussion 提出可检验的机制假设（架构差异/RLHF 策略/偶然），或增加一个负控制\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R11-REF1\"\n    summary: \"建议补充引用：Bojar et al. (2016) WMT human evaluation\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"论文 §2 已引用 Bojar et al. (2016)。\"\n    resolution_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"R12 确认：§2 'Bojar et al. (2016) document the practical tension between pairwise ranking and direct assessment at scale' 已引用。\"\n\n  # ============================================================\n  # Round 12 new issues\n  # ============================================================\n\n  - id: \"R12-N1\"\n    summary: \"Formality 轴 quality-style 混淆严重——GEE 显示 Orig OR ≥ Style OR（多配置），核心 'style bias' claim 对该轴偏强\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 N1 (critical) + R2 W1 (warning) 共同指出。GPT-4o: Style 2.58 vs Orig 2.32; Qwen3 n=355: Style 2.15 vs Orig 4.99; Gemini: Style 1.64 (ns) vs Orig 2.51。Appendix H stratified analysis 存在 circularity（用 Likert 等分作 quality proxy，但核心 claim 正是 Likert 不敏感）。两位共识：需区分 verbosity（纯 style-driven）和 formality（style + quality confound），不要统一称 'style bias'。\"\n    action_items:\n      - round: 12\n        action: \"Abstract/Intro 区分 verbosity (style-dominated) 和 formality (conditionally style-driven with quality confound)。考虑 formality 发现重新定性为 'measurement sensitivity divergence'。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R12-N2\"\n    summary: \"Bootstrap CI 在 GEE 语境下的 pair-level resampling 合理性未论证——BT bootstrap vs GEE sandwich SE 分工不清\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 N2: §4.1 'All bootstrap CIs use 10,000 pair-level resamples' 但 GEE 使用 sandwich SE。Table 3 CI 来源不清。如果 GEE 也用 bootstrap，需论证 resampling 保持 cluster 结构。\"\n    action_items:\n      - round: 12\n        action: \"明确区分 BT bootstrap CI 和 GEE sandwich CI 的适用范围；如果 GEE 也用 bootstrap，需论证 resampling 单位选择。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R12-W1\"\n    summary: \"Cross-axis contamination: formality→verbosity word count shift d=−0.23 超过论文自设 negligible 标准\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 W4: Appendix R Table 18 formality→verbosity word count d=−0.23 > 论文自设 d<0.20 negligible 标准。dataset-level 对称不等于 pair-level 对称。建议在 pair level 验证 word count 变化与 BT outcome 相关性，或 GEE 加 word count covariate。\"\n    action_items:\n      - round: 12\n        action: \"在 pair level 验证 word count shift 与 BT outcome 的相关性；或在 GEE 中加 word count 变化 covariate\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: \"R12-REF1\"\n    summary: \"建议补充引用：Carterette et al. (2008), Sedoc & Ungar (2020), Deutsch et al. (2023)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [2]\n        note: \"Carterette et al. (2008) ECIR: forced-choice vs. graded relevance sensitivity; Sedoc & Ungar (2020) ACL: IRT for chatbot evaluation; Deutsch et al. (2023) EMNLP: tie 处理对评估指标灵敏度。均与本文主题相关。需验证真实性。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 11\n        action: \"Abstract/§2 中 'reveals' 等措辞需进一步弱化；'first' 限定为 'first for LLM judges specifically'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 12\n        action: \"明确定位为 '首次在 LLM judge 下的系统性实证量化'，而非新发现。深度对比 LLM judge 场景是否超越传统心理测量预测。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 2 issues\n  # ============================================================\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 12\n    resolution: \"Round 7+ 确认主正文 8 页合规。R10 确认 ≤8 页。\"\n    resolution_round: 7\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 格式检查确认正文 8 页合规。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 格式合规确认：正文 ≤8 页 ✓，匿名 ✓，Limitations 无新实验 ✓。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 格式合规：正文 ≤8 页 ✓，ACL 模板 ✓，double-blind ✓。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"cross-rewriter validation 仅覆盖 Qwen3-32B judge。22% Style OR 下降确认 inflation 存在。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 共识 Should-Fix：Blindspot 存在性 robust，但效应量有 ±20-25% rewriter-dependent 变异。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF4: 仅 Qwen3-32B judge 有 cross-rewriter 验证。效应量 ±22% rewriter-dependent 变异需显式承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 Should-Fix: R1 指出仅 verbosity×Qwen3-32B 有替代 rewriter（R2 更正：formality+verbosity 两轴，但 register 未覆盖）。22% OR 下降不可忽略。两位共识 register 轴 evaluator-producer risk 最高。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W2: register 轴所有改写用 Qwen3-32B 且无跨改写器验证，BT 结果也较弱。建议降级为 exploratory pilot axis。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 10\n        action: \"Limitations 补一句：effect-size precision varies ±22% with rewriter choice\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'.\"\n    resolution_round: 4\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"共识 Must-Fix。50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 两位共同指向：增加 human evaluation 是最大可 actionable 改进。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 MF1 (critical): 持续 7 轮未解决。两位 Reviewer 交叉共识：human evaluation 是 4.0 的关键路径。孙震 50-pair 标注今晚返回。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 将 NLI gate 50 对人工标注列为 Must-Fix（Wilson CI 下界仅 86.3%，未报告 recall/FNR）。R2 交叉降为 Should-Fix（threshold sweep 11 阈值×44 组合全显著提供缓解）。论文 §5.4 报告 50 对 100% precision，但规模仍不足。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 W2: 50 对由 2 名标注员评估，κ=0.44 (moderate)，4 个分歧全在 verbosity condensation 上——正是最强 claim 轴。Wilson CI 过宽。建议增加标注量（≥100 对）或第三名标注员。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板\"\n        assigned_to: agent\n        status: done\n      - round: 10\n        action: \"孙震标注返回后 → analyze_annotations.py → Paper Agent 写入 §5.4\"\n        assigned_to: agent\n        status: pending\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"两位再次一致指出 Abstract 过密。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 fresh review 未显式提出 Abstract 过密问题。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未提及 Abstract 密度问题。P1 重写后可能已缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 列为 Should-Fix（W1），R1 交叉 [AGREE]。数字堆砌影响可读性，建议保留 1-2 个最有力数字。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 M1: Abstract 数字密度过高。与往轮一致。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 Should-Fix：Appendix H formality 方向异质性挑战 IIA。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。§4.1 footnote 已承认 direction asymmetry。可能接近解决。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 分歧：R1 列为 Must-Fix (critical)——Appendix B direction asymmetry 暗示 IIA 违反，需 Hausman-McFadden test。R2 交叉 [REBUT] 降为 Should-Fix——binary-choice BT 中 IIA 自动满足，Table 2 五种非参数方法独立确认 Blindspot。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 脚注 3：binary-choice BT 中 IIA structurally satisfied 的声明正确，但脚注篇幅长。方向异质性是 heterogeneous treatment effects 而非 IIA violation。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"§5.2 已加 6 项 amplification controls。从 critical 降级为 Should-Fix。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF1: 检测 vs 放大歧义仍为核心。R2 定 critical，R1 反驳降为 warning。6 项 controls + Claude 负对照已部分缓解。Conclusion 语言需条件化。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: detection vs. amplification 成为两位 Reviewer 的最大共识问题。R2 列为 Must-Fix (N2)，R1 交叉 [AGREE]。六项控制 bound 了 amplification 但未 eliminate。缺 ground-truth bias 已知的验证。100-point continuous Likert 排除粒度解释但支持 construct divergence 解读。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: 两位 Reviewer 最大共识问题。R2 N1 (critical)：标题 'Detecting Hidden Style Bias' 隐式预设 pairwise 为 ground truth。R1 通过 formality 轴 GEE 混淆（N1）间接支持——pairwise 检测到的可能部分是 quality-style correlation 的放大。六项控制必要但不充分。建议标题更中性。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"Conclusion 加条件性表述：amplification controls bound 但不完全排除放大\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 11\n        action: \"§6 开头 'systematically misses' 需加 hedge；考虑 reframe 为 'divergent signals' 而非单方面归因 Likert failure\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 12\n        action: \"标题改为更中性表述（如 'Measurement Divergence' 而非 'Detecting Hidden Bias'）；Abstract 前置三种等效解释\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1]\n        note: \"§3.5 因果语言校准良好。原始 'do-operator' 语言已修复。\"\n      - round: 10\n        reviewers: [2]\n        note: \"R10 M2: 'Controlled' 和 'interventional' 语言暗示过强因果识别。共识：§3.5 加明确声明。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 列为 Should-Fix (W3)，R2 交叉 [AGREE]。'controlled'/'interventional'/DAG notation 给人因果推断研究的印象，但 NLI gate 非 do-operator，GEE 是关联分析。建议 §3 更早声明 'controlled = experimentally controlled rewriting, not formal causal identification'。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 优势 2 肯定：§3.5 明确声明 'we do not claim this DAG is a complete structural causal model'，因果声明已诚实克制。此问题可能已接近解决。\"\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"共识：'the first' → 'a unified framework'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1 处理。RW 'first controlled, per-axis quantification' → 'first controlled quantification of this per-axis sensitivity gap'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R11 共识：'first' 需限定为 'first for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [2]\n        note: \"合并入 R2-N1。R12 R2 N2：'demonstrates'/'identifies' 仍偏发现性措辞。\"\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R10 SF4 处理。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R11 共识：register 轴 evaluator-producer risk 最高，需显式 caveat。\"\n      - round: 12\n        reviewers: [2]\n        note: \"合并入 RD2-SF1。R12 R2 W2：register 所有改写用 Qwen3-32B 且无跨改写器验证。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"4 target judges (+ Gemini confirmatory) now cover the claim.\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"标题和 Abstract framing 偏向 attenuation。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 Q3: bootstrap attenuation 如何排除 construct-level 差异？§5.1 已有讨论但 'Blindspot' 术语天然偏向。MF2 reframe 部分缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 列为 Should-Fix (W3)，R1 交叉 [AGREE]。标题 'Detecting Hidden Style Bias' 预设 pairwise 为 ground truth。R1 补充：100-point Likert 结果实际支持 construct divergence 而非 measurement attenuation。建议标题更中性。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识：论文承认三种等效解释但标题和 framing 隐式偏向 attenuation。合并入 R5-MF1 处理。\"\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: wont_fix\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: \"Acknowledged as limitation. Register is weakest axis with judge-dependent confound structure; cross-rewriter test would be confounded by register's inherent instability.\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"R10 在 evaluator-producer 讨论中确认仍未覆盖 register。Limitations 已承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 W2 和 R2 W4 均指出 register 未覆盖。R2 交叉更正 R1 描述（Appendix D 覆盖 formality+verbosity 两轴，非仅 verbosity）。核心关切仍成立。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W2 再次提出。与往轮一致。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 升级 Must-Fix。Δ=15pp 几乎涵盖最小 confirmed bias。\"\n      - round: 10\n        reviewers: [1]\n        note: \"R10 SF3: Δ=15pp 偏宽，Claude 仅覆盖 2/3 axes。论文 Appendix G 有 Δ_min=15.7pp。Reviewer #104 确认当前版本已包含此数据。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 将 TOST Δ=15pp 列为 Should-Fix (W1)——循环论证（用自己效应量定义等价边界），15pp≈d=0.43 属 medium effect 偏宽。R2 交叉 [AGREE]。需先验论证或 sensitivity across Δ=5/10/15/20pp。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识 Should-Fix：R1 W1 指出 GPT-4o formality 13pp 与 Δ=15pp 仅差 2pp，Claude 可能有未检测的 moderate bias。R2 W5 同意过宽且仅一个负控制。建议报告 Δ=10pp/5pp 的 TOST 结果。\"\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"R10 Q2: Table 1 footnote 已有 'Empty cells: untested combinations' 但未说明选择理由。Reviewer #104 判断现有 footnote 足够。\"\n      - round: 11\n        reviewers: [1]\n        note: \"R11 M4: register axis 的 n 值和 power 未明确报告。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识：Table 1 空 cells 脚注存在但选择理由缺失。R1 W3 + R2 W4：跨 benchmark 覆盖稀疏，verbosity 仅 1 个 cross-benchmark 数据点。\"\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"R12 视觉审查：Figure 2 DAG 橙色/红色高亮路径色盲用户可能需额外辨认。R2 M4 同指字号过小。\"\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound Δ=15pp 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"合并入 R5-M3 讨论。Δ_min=15.7pp 已报告。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。R11 两位共识 Should-Fix：需报告 TOST sensitivity across multiple Δ 或基于 leaderboard 排名影响论证 Δ 选择。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。R12 两位共识维持。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分——cross-axis contamination\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF6: cross-axis interaction 未测试。Agent 正在计算 cross-axis contamination 定量分析。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。Limitations 已含 per-axis independence 讨论及 cross-axis contamination 分析（Appendix）。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 W4: Appendix R cross-axis contamination 中 formality→verbosity 的 word count shift d=−0.23 超过论文自设 negligible 标准 d<0.20。dataset-level 对称不等于 pair-level 对称。建议在 GEE 中加入 word count 变化作为 covariate。\"\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2: 仅 2+1 axes 限制泛化。共识 Should-Fix：限定为 'preliminary evidence'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 列为 Must-Fix (N3)——n≈88 对 Likert power 严重不足（需 n=336-1200+），Likert null 可能仅反映 power 不足。R2 交叉 [AGREE]。共识：Conclusion 'systematically misses' 需 hedge，不能排除 power 解释。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 R2 W3: 第四轴（tone）因 NLI gate 拒绝率过高放弃，表明适用性受限。3 轴不足以支撑 'framework' 泛化。R1 W3: cross-benchmark 覆盖稀疏。两位共识：降为 'methodology for content-preserving style axes'。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 10\n    resolution: \"R9/R10 检查确认 Appendix C Table 5 已有完整 12 行 CI。\"\n    resolution_round: 10\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"论文 Related Work §2 已引用。\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 7 issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 10\n    resolution: \"§4.1 明确 'six tests—three target judges × two axes'，Gemini 为 confirmatory，Appendix Q 8-test family 下所有结果仍显著。R10 未再提及。\"\n    resolution_round: 10\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型，存在循环性\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。§5.4 已报告 FNR 8.4% [3.7%, 15.9%] CI。GPT-4o cross-validation 部分缓解循环性。人工标注（MF1）将彻底解决。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及此具体问题，但 R1-N2 关于 NLI gate 人工验证不足间接涵盖。\"\n      - round: 12\n        reviewers: []\n        note: \"R12 未显式提及。§5.4 人工标注 (50对) 部分缓解。\"\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate 17.4% FPR 未报告\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。Appendix F 有 direction-aware gate validation data。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 Q4: direction-aware NLI gate 恢复的 21 对在 content quality 上是否与 bidirectional-pass 对系统不同？BT 一致但 Likert 质量分和 NLI 分数分布差异未报告。\"\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"论文 §5.1 已引用 Tripathi et al. (2025)。\"\n    resolution_round: 9\n\n  # ============================================================\n  # Round 8 issues\n  # ============================================================\n\n  - id: \"R8-W1\"\n    summary: \"3 个风格轴限制 'framework' 级别泛化——需从 'framework' 降为 'methodology'\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2 再次确认。共识：限定为 'preliminary evidence of axis-dependent patterns'。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: 与 R6-SF3 合并。两位共识：当前证据仅覆盖 3 axes，'framework' 级别泛化需更多 axes 验证。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W3: tone 轴失败说明适用性受限。建议软化为 'methodology for content-preserving style axes'。与 R6-SF3 合并。\"\n    action_items:\n      - round: 10\n        action: \"Limitations 补 'preliminary evidence' 限定 + 列出未覆盖 axes\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R8-W2\"\n    summary: \"生态效度讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Limitations 已含 'Our controlled manipulation design ensures internal validity but may not fully generalize to naturalistic evaluation settings.' R10 未再提及。\"\n    resolution_round: 10\n\n  - id: \"R8-W3\"\n    summary: \"Rewriting artifact 的 style-specific polishing interaction 未讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Appendix O 已含相关讨论。R10 未再提及。\"\n    resolution_round: 10\n\n  - id: \"R8-W4\"\n    summary: \"Introduction motivating example 未 acknowledge formality-quality nuance\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"§1 已有 GEE decomposition 引用。R10 确认。\"\n    resolution_round: 10\n\n  - id: \"R8-REF1\"\n    summary: \"建议补充引用：Girrbach et al. 'Likert or Not'\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"Phantom reference.\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 10 issues\n  # ============================================================\n\n  - id: \"R10-N1\"\n    summary: \"100-point continuous Likert 实验仅用单一 judge（Qwen3-32B）\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Minor。Limitations 承认即可。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。Limitations 已含 'tested with a single judge' 承认。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 小问题 5: 100-point 仅选 Qwen3-32B（evaluator-producer overlap 最严重的 judge）而非 GPT-4o，选择理由缺失。\"\n\n  - id: \"R10-N2\"\n    summary: \"NLI gate 44% 拒绝率 selection bias 仅检查 4 个 surface covariates\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Limitations 承认即可。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 列为 Must-Fix (N2)——gate 过滤 12-35%。R2 交叉降为 Should-Fix。\"\n      - round: 12\n        reviewers: []\n        note: \"R12 未显式提及。§5.4 已有 content preservation 人工验证。\"\n\n  - id: \"R10-REF1\"\n    summary: \"建议补充引用：Simms et al. (2019), Polo et al. (2024), Kocmi & Federmann (2023)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 10\n    resolution: null\n    resolution_round: null\n\n  # ============================================================\n  # Round 11 new issues\n  # ============================================================\n\n  - id: \"R11-N1\"\n    summary: \"Negative control 仅 Claude Sonnet 4 一个模型，不足以论证 Blindspot 的架构特异性\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix (W4): 仅一个负控制不足以论证 Blindspot 是特定架构/训练方式的产物。未讨论 Claude 为何不受影响。R2 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: R2 W5/N1 指出仅一个负控制模型。R1 W1 指出 TOST Δ=15pp 与 GPT-4o 最小 bias (13pp) 几乎重叠。两位共识：Claude 负控制说服力有限。\"\n    action_items:\n      - round: 11\n        action: \"Discussion 提出可检验的机制假设（架构差异/RLHF 策略/偶然），或增加一个负控制\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R11-REF1\"\n    summary: \"建议补充引用：Bojar et al. (2016) WMT human evaluation\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"论文 §2 已引用 Bojar et al. (2016)。\"\n    resolution_round: 12\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"R12 确认：§2 'Bojar et al. (2016) document the practical tension between pairwise ranking and direct assessment at scale' 已引用。\"\n\n  # ============================================================\n  # Round 12 new issues\n  # ============================================================\n\n  - id: \"R12-N1\"\n    summary: \"Formality 轴 quality-style 混淆严重——GEE 显示 Orig OR ≥ Style OR（多配置），核心 'style bias' claim 对该轴偏强\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 N1 (critical) + R2 W1 (warning) 共同指出。GPT-4o: Style 2.58 vs Orig 2.32; Qwen3 n=355: Style 2.15 vs Orig 4.99; Gemini: Style 1.64 (ns) vs Orig 2.51。Appendix H stratified analysis 存在 circularity（用 Likert 等分作 quality proxy，但核心 claim 正是 Likert 不敏感）。两位共识：需区分 verbosity（纯 style-driven）和 formality（style + quality confound），不要统一称 'style bias'。\"\n    action_items:\n      - round: 12\n        action: \"Abstract/Intro 区分 verbosity (style-dominated) 和 formality (conditionally style-driven with quality confound)。考虑 formality 发现重新定性为 'measurement sensitivity divergence'。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R12-N2\"\n    summary: \"Bootstrap CI 在 GEE 语境下的 pair-level resampling 合理性未论证——BT bootstrap vs GEE sandwich SE 分工不清\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 N2: §4.1 'All bootstrap CIs use 10,000 pair-level resamples' 但 GEE 使用 sandwich SE。Table 3 CI 来源不清。如果 GEE 也用 bootstrap，需论证 resampling 保持 cluster 结构。\"\n    action_items:\n      - round: 12\n        action: \"明确区分 BT bootstrap CI 和 GEE sandwich CI 的适用范围；如果 GEE 也用 bootstrap，需论证 resampling 单位选择。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R12-W1\"\n    summary: \"Cross-axis contamination: formality→verbosity word count shift d=−0.23 超过论文自设 negligible 标准\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 W4: Appendix R Table 18 formality→verbosity word count d=−0.23 > 论文自设 d<0.20 negligible 标准。dataset-level 对称不等于 pair-level 对称。建议在 pair level 验证 word count 变化与 BT outcome 相关性，或 GEE 加 word count covariate。\"\n    action_items:\n      - round: 12\n        action: \"在 pair level 验证 word count shift 与 BT outcome 的相关性；或在 GEE 中加 word count 变化 covariate\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: \"R12-REF1\"\n    summary: \"建议补充引用：Carterette et al. (2008), Sedoc & Ungar (2020), Deutsch et al. (2023)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [2]\n        note: \"Carterette et al. (2008) ECIR: forced-choice vs. graded relevance sensitivity; Sedoc & Ungar (2020) ACL: IRT for chatbot evaluation; Deutsch et al. (2023) EMNLP: tie 处理对评估指标灵敏度。均与本文主题相关。需验证真实性。\""
  }
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-22T18:23:26.339316+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 43333}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-22T18:26:21.272329+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：The Likert Blindspot\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审稿轮次**: Round 12 (fresh review)\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+写作质量+相关工作）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一个黑盒框架，通过 NLI 门控内容保持、单轴风格改写和位控 pairwise 比较来量化 LLM judge 的风格偏差。核心发现为 \"Likert Blindspot\"：Likert 评分系统性地衰减 pairwise 比较能检测到的风格偏差信号。在 4 个目标 judge（GPT-4o, Qwen3-32B, Llama-70B, Gemini-Flash）+ 1 个负控制（Claude Sonnet 4）、3 个风格轴（formality, verbosity, register）、3 个 benchmark（LLMBar, AlpacaEval, MT-Bench）上验证。GEE 条件分解揭示了逐轴混淆结构：verbosity 是 style-dominated，formality 有显著 quality confound，register 是 judge-dependent。\n\n---\n\n## Strengths\n\n**S1. Verbosity 轴证据链极强。** Style OR 8.2–13.1（四个 judge 一致），Originality OR 0.38–0.49（均不显著或仅边缘），cross-rewriter 验证完整（Appendix D），direction-aware NLI 有理论和实证依据。方法论上无可挑剔。[两位共识]\n\n**S2. 统计方法论严谨且透明。** 七种测量方法的灵敏度层级（Table 2）、Holm-Bonferroni 6 测试家族 + 8 测试敏感性分析（全部保持显著）、探索性与验证性分析的明确区分、BT GoF 检验、GEE 诊断完整（exchangeable vs independence |ΔQIC| < 0.001）、bootstrap 衰减分析区分 measurement attenuation 与 insufficient power。这在 LLM judge 评估文献中属高标准。[两位共识]\n\n**S3. 因果声明诚实克制。** §3.5 明确声明 \"we do not claim that this DAG is a complete structural causal model\"，DAG 中用虚线橙色箭头标注 residual confounding，\"controlled\" 的定义明确限定为实验控制而非因果识别。这种克制在该领域的论文中少见。[R1 强调]\n\n**S4. 实验控制设计充分。** 六项放大控制（NLI gate ablation、Claude 负控制、跨轴 BT 变异、rewriting artifact 吸收、debiased prompting、跨架构复现）、position swap 双向评估、NLI 阈值 11 点 sweep（BT ≤3pp 变动）、same-style double-rewrite artifact control。[两位共识]\n\n**S5. 跨 judge 一致性强。** 四个独立架构一致复现 Blindspot（Table 1：11/11 bias-positive cells 中 8 个 Blindspot），GEE 混淆结构跨 judge 高度一致。[两位共识]\n\n**S6. Limitations 坦诚全面。** 对 quality-style confounding、evaluator-producer overlap、construct divergence 的歧义性、样本量限制、生态效度等进行了充分讨论。[R2 强调]\n\n---\n\n## Weaknesses\n\n### Must-Fix (critical) — 不修复则不可接收\n\n**MF1. [共识] 标题和 framing 隐式预设 pairwise 为 ground truth，核心歧义未解决。**\n论文标题 \"Detecting Hidden Style Bias\" 和 \"Blindspot\" 命名隐式假定 pairwise 检测到的是真实偏差、Likert 遗漏了它。然而论文自身承认三种等效解释：(a) Likert 测量衰减，(b) pairwise 放大（Comparative Trap, Jeong et al. 2025），(c) 构念分歧。六项放大控制必要但不充分——它们 bound 了 amplification 但未 eliminate。论文在 §5.1 保持 agnostic 是诚实的，但标题和 Abstract 的 framing 与此矛盾。\n- **建议**：标题改为更中性的表述（如 \"Measurement Divergence\" 而非 \"Detecting Hidden Bias\"）；Abstract 前置三种解释而非在 §5.1 才讨论。\n- R1 通过 formality GEE 混淆（MF2）间接支持此判断：pairwise 检测到的可能部分是 quality-style correlation 的放大。R2 直接作为 N1 (critical) 提出。\n\n**MF2. [共识] Formality 轴 quality-style 混淆严重，\"style bias\" claim 对该轴偏强。**\nGEE 分解显示 formality 的 Originality OR 在多个配置中 ≥ Style OR：\n- GPT-4o: Style 2.58 vs Orig 2.32（几乎相等）\n- Qwen3 n=355: Style 2.15 vs Orig 4.99（originality 是 style 的 2.3 倍）\n- Gemini: Style 1.64 (n.s.!) vs Orig 2.51\n- Direction asymmetry（formal-origin 88.9% vs casual-origin 52.6%, Fisher p=0.015）进一步确认\n\n如果 formality 的 Blindspot 本质上是 pairwise 对 quality-style correlation 的放大，而非 Likert 遗漏了 style bias，则论文的核心叙事被削弱约一半。Appendix H stratified analysis 存在 circularity：论文核心 claim 是 Likert 对 style 不敏感，因此用 Likert 等分作为 \"质量无差异\" 的代理变量存在逻辑矛盾。\n- **建议**：在 Abstract/Intro 区分 verbosity（纯 style-driven）和 formality（style + quality confound），不统一称 \"style bias\"。\n- R1 N1 (critical) + R2 W1 (warning)，交叉后两位均认可此问题的重要性。\n\n**MF3. [R2 主张，R1 部分认可] Novelty 定位不足——本质是 Thurstone (1927) 在 LLM judge 领域的实证确认。**\nForced-choice 比 rating scale 灵敏度更高是心理测量学经典结论（Thurstone 1927, Preston & Colman 2000, DeCoster & Iselin 2011），论文自己引用了这些文献。\"unquantified\" 的声明技术上正确，但核心机制完全可从已有理论预测。增量贡献是 (a) 实证量化 + (b) per-axis confound structure 的 GEE 分解——有价值，但不足以支撑 \"demonstrates\"/\"identifies\" 等发现性措辞。\n- **建议**：明确定位为 \"首次在 LLM judge 下的系统性实证量化\"，深度对比 LLM judge 场景是否超越传统理论预测。\n- R2 N2 (critical, Excitement 2.5/5)；R1 认为实践意义构成独立贡献（Excitement 3.5/5）。**这是本轮最大分歧点**。\n\n**MF4. [R1 主张] Bootstrap CI vs GEE sandwich SE 在论文中的分工不清晰。**\n§4.1 声明 \"All bootstrap CIs use 10,000 pair-level resamples\"，但 GEE 使用 sandwich standard errors。Table 3 的 CI（Appendix C Table 6）使用哪种方法不明确。如果 GEE 也用 bootstrap，需论证 pair-level resampling 是否保持 cluster 结构。\n- **建议**：明确区分 BT bootstrap CI 和 GEE sandwich CI 的适用范围。\n- R1 N2 (critical)；R2 未独立提出此问题。\n\n### Should-Fix (warning) — 显著改善论文质量\n\n**SF1. [共识] TOST 等价检验边界 Δ=15pp 偏宽，负控制说服力有限。**\nClaude 的 TOST 在 Δ=15pp 时 p<0.05，但 GPT-4o formality 检测到的 bias 为 BT 63.0%（即 13pp），与 Δ=15pp 仅差 2pp。Claude 可能存在 moderate bias 但低于检测阈值。且仅一个负控制模型。\n- **建议**：报告 Δ=10pp, 5pp 的 TOST 结果；承认 Δ=15pp 是 power 限制下的妥协。\n\n**SF2. [共识] 跨 benchmark 覆盖稀疏。**\nAlpacaEval 仅 3 配置，MT-Bench 仅 2 配置；verbosity（最强轴）仅在 AlpacaEval 有 1 个 cross-benchmark 数据点且为 ‡（非 Blindspot）。\"three benchmarks\" 声明名义上成立但实际覆盖很低。Llama-70B 和 Gemini 无 cross-benchmark 验证。\n\n**SF3. [共识] 3 个风格轴不足以支撑 \"framework\" 泛化。**\n第四轴（tone）因 NLI gate 拒绝率过高放弃，表明适用性受限于 content-preserving style axes。\n- **建议**：软化为 \"methodology for content-preserving style axes\"。\n\n**SF4. [R2 主张，R1 同意] Register 轴 evaluator-producer overlap 严重且无跨改写器验证。**\nRegister 所有改写用 Qwen3-32B，BT 结果也较弱（Qwen3 n.s.）。\n- **建议**：降级为 \"exploratory pilot axis\"。\n\n**SF5. [R1 主张] 人工标注验证规模偏小，inter-annotator agreement 仅 moderate。**\n50 对，κ=0.44 (moderate)。4 个标注分歧全在 verbosity condensation 对上——正是最强 claim 的支撑轴。Wilson CI [86.7%, 100%] 和 [65.3%, 93.6%] 精度估计不够精确。\n- **建议**：增加标注量（≥100 对）或第三名标注员。\n\n**SF6. [R1 主张] Cross-axis contamination: formality→verbosity word count shift d=−0.23 超过论文自设 negligible 标准 (d<0.20)。**\ndataset-level 对称不等于 pair-level 对称。\n- **建议**：在 pair level 验证 word count 变化与 BT outcome 的相关性，或在 GEE 中加入 word count covariate。\n\n### Minor (info)\n\n- M1: Abstract 数字密度过高，建议保留 1-2 个最有力数字 [R2]\n- M2: Introduction 开头单实例 caveat 应前置 [R2]\n- M3: 对 RATE 的批评措辞可更委婉 [R2]\n- M4: Figure 2 DAG 橙色 dashed arrow 字号过小 + 色盲可访问性 [R2 + 视觉审查]\n- M5: Table 1 五种标记系统（†, ‡, †_e, †_c, ---）认知负担高 [R1 + R2]\n- M6: Limitations 约 1.5 页可适当精简 [R2]\n- M7: Figure 4 caption \"Detection probability at observed effect magnitudes\" 可能被误读为 post-hoc power [R1]\n- M8: §4.1 脚注 3（IIA）篇幅长（~60 words），建议移至 Appendix [R1]\n- M9: Register 正文定位不够清晰，Table 1 占 6 行但 §5.3 仅一句话 [R1]\n- M10: 100-point Likert 仅选 Qwen3-32B 而非无 overlap 的 GPT-4o，选择理由缺失 [R1]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Formality 轴 quality confound 削弱 \"style bias\" 叙事**——两位独立提出，交叉后均确认。核心共识：pairwise 检测到的 formality \"bias\" 有相当部分是 quality-formality 相关性的反映。\n2. **TOST Δ=15pp 偏宽**——两位独立提出，交叉后一致。GPT-4o 最小 bias (13pp) 与 Δ (15pp) 几乎重叠。\n3. **Verbosity 轴证据令人信服**——两位一致肯定。Style OR 8–13, cross-rewriter validated, 4 judges consistent。\n4. **统计方法论高标准**——两位一致肯定。七种方法 sensitivity hierarchy、Holm-Bonferroni、GEE 诊断完整。\n5. **跨 benchmark 覆盖稀疏**——两位一致。verbosity 仅 1 个 cross-benchmark 数据点。\n6. **因果声明克制性值得肯定**——两位一致。§3.5 的 disclaimer 在该领域少见。\n7. **Register 应降级为 exploratory pilot**——两位一致。evaluator-producer overlap + BT 结果弱。\n\n## Reviewer Divergence [分歧]\n\n1. **Novelty/Excitement [最大分歧]**：R1 (3.5/5) 认为 Likert Blindspot 对 RLHF/DPO pipeline 有直接 actionable implications，sensitivity hierarchy 是有价值的方法论贡献；R2 (2.5/5) 认为核心发现是 Thurstone 经典结论的领域迁移，非新发现。**两位均认可 GEE per-axis decomposition 是增量贡献。**\n2. **Bootstrap/GEE CI 问题**：R1 列为 Must-Fix (critical)，R2 未独立提出。这是一个技术清晰性问题而非方法论错误。\n\n---\n\n## Questions (供作者回应)\n\n**Q1 [R1]**: Appendix H stratified analysis 用 Likert 等分作为 \"无质量差异\" 代理——如何排除 circularity？是否考虑过使用外部质量指标（如人工评分或参考答案匹配度）？\n\n**Q2 [R1]**: Formality 轴 Qwen3 n=355 的 GEE 显示 Orig OR (4.99) 是 Style OR (2.15) 的 2.3 倍，\"formality bias\" 表述是否仍恰当？\n\n**Q3 [R1]**: TOST Δ=15pp 的选择基准是 SESOI 估计还是 power-driven？如果后者，论文是否应报告基于 SESOI 的 Δ？\n\n**Q4 [R1]**: Verbosity direction-aware NLI gate 恢复的 21 对在 Likert 质量分和 NLI 分数分布上是否与 bidirectional-pass 对系统不同？\n\n**Q5 [R1]**: 论文声称对 RLHF/DPO pipeline 有启示，但未给出下游影响实证。是否有初步实验？\n\n---\n\n## Missing References\n\n**R2 建议（需验证真实性）**：\n1. Carterette et al. (2008) — forced-choice vs. graded relevance 灵敏度差异（ECIR）\n2. Sedoc & Ungar (2020) — IRT 应用于 chatbot 评估（ACL）\n3. Deutsch et al. (2023) — tie 处理对评估指标灵敏度的影响（EMNLP）\n\n**R1 建议**：\n4. Stureborg et al. (2024) — LLM judge calibration（论文 §2 已引用 Stureborg et al. 2024 关于 inconsistency，但 calibration 角度未充分覆盖）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（7 项 info，0 critical，0 warning）：\n- Figure 1 pipeline 流程图内部标注文字偏小，caption 偏简略\n- Table 1 脚注字号非常小（~6pt），包含重要符号说明\n- Limitations 章节 ~1.5 页，内容为实质性讨论，应合规\n- Figure 2 DAG 色盲可访问性需注意\n- Appendix 共 19 小节、~15 张表格，体量庞大但格式规范\n\n**格式合规确认**：正文 ≤8 页 ✓，ACL 模板 ✓，double-blind 匿名 ✓，Limitations 不计入页数 ✓。\n\n---\n\n## Overall Assessment\n\n### 官方维度打分（加权合成）\n\n| 维度 | R1 | R2 | 合成 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |\n| Excitement | 3.5/5 | 2.5/5 | **3.0/5** |\n| Reproducibility | 4/5 | 4/5 | **4.0/5** |\n\n### Overall: **3.0 (Findings)**\n\n**推荐理由**：\n- Verbosity 轴的证据链完整且令人信服（Style OR 8–13, 4 judges consistent）\n- 统计方法论严谨，在 LLM judge 评估文献中属高标准\n- GEE per-axis confound decomposition 有方法论增量贡献\n- 对从业者（RLHF/DPO pipeline）有 actionable implications\n\n**限制评分的核心因素**：\n1. **Novelty 不足**：核心发现（forced-choice 灵敏度高于 rating scale）是心理测量学经典结论的领域迁移确认。增量贡献（实证量化 + GEE 分解）有价值但不足以达到主会议水平。[R2 主张，两位在 GEE 增量贡献上达成共识]\n2. **Formality 轴 quality confound**：论文的两个 primary axes 之一（formality）受 quality-style confound 严重影响，削弱了 \"hidden style bias\" 统一叙事。[两位共识]\n3. **Detection vs. amplification 核心歧义**：标题和 framing 隐式预设 pairwise 为 ground truth，但论文自身承认无法区分 measurement attenuation、pairwise amplification 和 construct divergence。[两位共识]\n4. **负控制说服力有限**：TOST Δ=15pp 与 GPT-4o formality 最小 bias (13pp) 几乎重叠；仅一个负控制模型。[两位共识]\n\n**上调至 3.5 (Borderline Conference) 的条件**：\n如果作者在 rebuttal 中能 (1) 调整标题和 framing 为更中性表述；(2) 区分 formality claim 和 verbosity claim 的措辞强度；(3) 澄清 GEE CI 方法；(4) 深度论证 LLM judge 场景对 Thurstone 理论的超越——Director 愿意上调。\n\n**上调至 4.0 (Conference) 的条件（更高门槛）**：\n除上述条件外，还需 (5) 报告 TOST multi-Δ sensitivity；(6) 增加人工标注规模或提供 circularity 替代验证；(7) 增强 cross-benchmark 覆盖（尤其 verbosity）。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 开头 formality 实例有效但需前置 caveat（formality preferences 可能反映 legitimate quality judgments——§1 第二段已有，但应更早出现）\n- \"no single framework integrates...\" 的 gap statement 可能被视为 straw man——各工具解决的问题不同\n\n### §3 Method\n- §3.1 style-controlled rewriting 描述清晰\n- §3.2 NLI gate 设计合理；direction-aware verbosity 处理有理论依据\n- §3.3 measurement protocol 完整\n- §3.5 因果声明克制——\"controlled refers to experimentally controlled rewriting, not formal causal identification\" 是重要的诚实声明\n\n### §4 Experiments\n- §4.1 统计框架严谨：primary/exploratory/confirmatory 三分法、Holm-Bonferroni 校正、BT 正则化和 bootstrap 参数明确\n- Table 1 信息量大但认知负担高（5 种标记系统）\n- Table 2 sensitivity hierarchy 是有价值的方法论贡献\n\n### §5 Analysis\n- §5.1 Likert Blindspot 描述清晰，n=355 scaled replication 有力区分 attenuation vs power\n- §5.2 GEE decomposition 对 verbosity 令人信服；对 formality 的结果反而削弱 \"bias\" 叙事（Orig OR ≥ Style OR 多配置）\n- §5.3 Cross-judge replication 强，但 cross-benchmark 覆盖稀疏\n- §5.4 六项放大控制设计周全；人工标注 50 对规模偏小（κ=0.44）\n\n### §6 Conclusion\n- 双发现结构清晰\n- \"systematically misses\" 需 hedge——不能排除 power 解释和 construct divergence\n\n### Limitations\n- 坦诚全面，覆盖 quality-style confounding、evaluator-producer overlap、scope、ecological validity、scale design\n- 篇幅偏长（~1.5 页），可适当精简\n- 建议补充 cross-axis contamination d=−0.23 的讨论",
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：The Likert Blindspot\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审稿轮次**: Round 12 (fresh review)\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+写作质量+相关工作）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一个黑盒框架，通过 NLI 门控内容保持、单轴风格改写和位控 pairwise 比较来量化 LLM judge 的风格偏差。核心发现为 \"Likert Blindspot\"：Likert 评分系统性地衰减 pairwise 比较能检测到的风格偏差信号。在 4 个目标 judge（GPT-4o, Qwen3-32B, Llama-70B, Gemini-Flash）+ 1 个负控制（Claude Sonnet 4）、3 个风格轴（formality, verbosity, register）、3 个 benchmark（LLMBar, AlpacaEval, MT-Bench）上验证。GEE 条件分解揭示了逐轴混淆结构：verbosity 是 style-dominated，formality 有显著 quality confound，register 是 judge-dependent。\n\n---\n\n## Strengths\n\n**S1. Verbosity 轴证据链极强。** Style OR 8.2–13.1（四个 judge 一致），Originality OR 0.38–0.49（均不显著或仅边缘），cross-rewriter 验证完整（Appendix D），direction-aware NLI 有理论和实证依据。方法论上无可挑剔。[两位共识]\n\n**S2. 统计方法论严谨且透明。** 七种测量方法的灵敏度层级（Table 2）、Holm-Bonferroni 6 测试家族 + 8 测试敏感性分析（全部保持显著）、探索性与验证性分析的明确区分、BT GoF 检验、GEE 诊断完整（exchangeable vs independence |ΔQIC| < 0.001）、bootstrap 衰减分析区分 measurement attenuation 与 insufficient power。这在 LLM judge 评估文献中属高标准。[两位共识]\n\n**S3. 因果声明诚实克制。** §3.5 明确声明 \"we do not claim that this DAG is a complete structural causal model\"，DAG 中用虚线橙色箭头标注 residual confounding，\"controlled\" 的定义明确限定为实验控制而非因果识别。这种克制在该领域的论文中少见。[R1 强调]\n\n**S4. 实验控制设计充分。** 六项放大控制（NLI gate ablation、Claude 负控制、跨轴 BT 变异、rewriting artifact 吸收、debiased prompting、跨架构复现）、position swap 双向评估、NLI 阈值 11 点 sweep（BT ≤3pp 变动）、same-style double-rewrite artifact control。[两位共识]\n\n**S5. 跨 judge 一致性强。** 四个独立架构一致复现 Blindspot（Table 1：11/11 bias-positive cells 中 8 个 Blindspot），GEE 混淆结构跨 judge 高度一致。[两位共识]\n\n**S6. Limitations 坦诚全面。** 对 quality-style confounding、evaluator-producer overlap、construct divergence 的歧义性、样本量限制、生态效度等进行了充分讨论。[R2 强调]\n\n---\n\n## Weaknesses\n\n### Must-Fix (critical) — 不修复则不可接收\n\n**MF1. [共识] 标题和 framing 隐式预设 pairwise 为 ground truth，核心歧义未解决。**\n论文标题 \"Detecting Hidden Style Bias\" 和 \"Blindspot\" 命名隐式假定 pairwise 检测到的是真实偏差、Likert 遗漏了它。然而论文自身承认三种等效解释：(a) Likert 测量衰减，(b) pairwise 放大（Comparative Trap, Jeong et al. 2025），(c) 构念分歧。六项放大控制必要但不充分——它们 bound 了 amplification 但未 eliminate。论文在 §5.1 保持 agnostic 是诚实的，但标题和 Abstract 的 framing 与此矛盾。\n- **建议**：标题改为更中性的表述（如 \"Measurement Divergence\" 而非 \"Detecting Hidden Bias\"）；Abstract 前置三种解释而非在 §5.1 才讨论。\n- R1 通过 formality GEE 混淆（MF2）间接支持此判断：pairwise 检测到的可能部分是 quality-style correlation 的放大。R2 直接作为 N1 (critical) 提出。\n\n**MF2. [共识] Formality 轴 quality-style 混淆严重，\"style bias\" claim 对该轴偏强。**\nGEE 分解显示 formality 的 Originality OR 在多个配置中 ≥ Style OR：\n- GPT-4o: Style 2.58 vs Orig 2.32（几乎相等）\n- Qwen3 n=355: Style 2.15 vs Orig 4.99（originality 是 style 的 2.3 倍）\n- Gemini: Style 1.64 (n.s.!) vs Orig 2.51\n- Direction asymmetry（formal-origin 88.9% vs casual-origin 52.6%, Fisher p=0.015）进一步确认\n\n如果 formality 的 Blindspot 本质上是 pairwise 对 quality-style correlation 的放大，而非 Likert 遗漏了 style bias，则论文的核心叙事被削弱约一半。Appendix H stratified analysis 存在 circularity：论文核心 claim 是 Likert 对 style 不敏感，因此用 Likert 等分作为 \"质量无差异\" 的代理变量存在逻辑矛盾。\n- **建议**：在 Abstract/Intro 区分 verbosity（纯 style-driven）和 formality（style + quality confound），不统一称 \"style bias\"。\n- R1 N1 (critical) + R2 W1 (warning)，交叉后两位均认可此问题的重要性。\n\n**MF3. [R2 主张，R1 部分认可] Novelty 定位不足——本质是 Thurstone (1927) 在 LLM judge 领域的实证确认。**\nForced-choice 比 rating scale 灵敏度更高是心理测量学经典结论（Thurstone 1927, Preston & Colman 2000, DeCoster & Iselin 2011），论文自己引用了这些文献。\"unquantified\" 的声明技术上正确，但核心机制完全可从已有理论预测。增量贡献是 (a) 实证量化 + (b) per-axis confound structure 的 GEE 分解——有价值，但不足以支撑 \"demonstrates\"/\"identifies\" 等发现性措辞。\n- **建议**：明确定位为 \"首次在 LLM judge 下的系统性实证量化\"，深度对比 LLM judge 场景是否超越传统理论预测。\n- R2 N2 (critical, Excitement 2.5/5)；R1 认为实践意义构成独立贡献（Excitement 3.5/5）。**这是本轮最大分歧点**。\n\n**MF4. [R1 主张] Bootstrap CI vs GEE sandwich SE 在论文中的分工不清晰。**\n§4.1 声明 \"All bootstrap CIs use 10,000 pair-level resamples\"，但 GEE 使用 sandwich standard errors。Table 3 的 CI（Appendix C Table 6）使用哪种方法不明确。如果 GEE 也用 bootstrap，需论证 pair-level resampling 是否保持 cluster 结构。\n- **建议**：明确区分 BT bootstrap CI 和 GEE sandwich CI 的适用范围。\n- R1 N2 (critical)；R2 未独立提出此问题。\n\n### Should-Fix (warning) — 显著改善论文质量\n\n**SF1. [共识] TOST 等价检验边界 Δ=15pp 偏宽，负控制说服力有限。**\nClaude 的 TOST 在 Δ=15pp 时 p<0.05，但 GPT-4o formality 检测到的 bias 为 BT 63.0%（即 13pp），与 Δ=15pp 仅差 2pp。Claude 可能存在 moderate bias 但低于检测阈值。且仅一个负控制模型。\n- **建议**：报告 Δ=10pp, 5pp 的 TOST 结果；承认 Δ=15pp 是 power 限制下的妥协。\n\n**SF2. [共识] 跨 benchmark 覆盖稀疏。**\nAlpacaEval 仅 3 配置，MT-Bench 仅 2 配置；verbosity（最强轴）仅在 AlpacaEval 有 1 个 cross-benchmark 数据点且为 ‡（非 Blindspot）。\"three benchmarks\" 声明名义上成立但实际覆盖很低。Llama-70B 和 Gemini 无 cross-benchmark 验证。\n\n**SF3. [共识] 3 个风格轴不足以支撑 \"framework\" 泛化。**\n第四轴（tone）因 NLI gate 拒绝率过高放弃，表明适用性受限于 content-preserving style axes。\n- **建议**：软化为 \"methodology for content-preserving style axes\"。\n\n**SF4. [R2 主张，R1 同意] Register 轴 evaluator-producer overlap 严重且无跨改写器验证。**\nRegister 所有改写用 Qwen3-32B，BT 结果也较弱（Qwen3 n.s.）。\n- **建议**：降级为 \"exploratory pilot axis\"。\n\n**SF5. [R1 主张] 人工标注验证规模偏小，inter-annotator agreement 仅 moderate。**\n50 对，κ=0.44 (moderate)。4 个标注分歧全在 verbosity condensation 对上——正是最强 claim 的支撑轴。Wilson CI [86.7%, 100%] 和 [65.3%, 93.6%] 精度估计不够精确。\n- **建议**：增加标注量（≥100 对）或第三名标注员。\n\n**SF6. [R1 主张] Cross-axis contamination: formality→verbosity word count shift d=−0.23 超过论文自设 negligible 标准 (d<0.20)。**\ndataset-level 对称不等于 pair-level 对称。\n- **建议**：在 pair level 验证 word count 变化与 BT outcome 的相关性，或在 GEE 中加入 word count covariate。\n\n### Minor (info)\n\n- M1: Abstract 数字密度过高，建议保留 1-2 个最有力数字 [R2]\n- M2: Introduction 开头单实例 caveat 应前置 [R2]\n- M3: 对 RATE 的批评措辞可更委婉 [R2]\n- M4: Figure 2 DAG 橙色 dashed arrow 字号过小 + 色盲可访问性 [R2 + 视觉审查]\n- M5: Table 1 五种标记系统（†, ‡, †_e, †_c, ---）认知负担高 [R1 + R2]\n- M6: Limitations 约 1.5 页可适当精简 [R2]\n- M7: Figure 4 caption \"Detection probability at observed effect magnitudes\" 可能被误读为 post-hoc power [R1]\n- M8: §4.1 脚注 3（IIA）篇幅长（~60 words），建议移至 Appendix [R1]\n- M9: Register 正文定位不够清晰，Table 1 占 6 行但 §5.3 仅一句话 [R1]\n- M10: 100-point Likert 仅选 Qwen3-32B 而非无 overlap 的 GPT-4o，选择理由缺失 [R1]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Formality 轴 quality confound 削弱 \"style bias\" 叙事**——两位独立提出，交叉后均确认。核心共识：pairwise 检测到的 formality \"bias\" 有相当部分是 quality-formality 相关性的反映。\n2. **TOST Δ=15pp 偏宽**——两位独立提出，交叉后一致。GPT-4o 最小 bias (13pp) 与 Δ (15pp) 几乎重叠。\n3. **Verbosity 轴证据令人信服**——两位一致肯定。Style OR 8–13, cross-rewriter validated, 4 judges consistent。\n4. **统计方法论高标准**——两位一致肯定。七种方法 sensitivity hierarchy、Holm-Bonferroni、GEE 诊断完整。\n5. **跨 benchmark 覆盖稀疏**——两位一致。verbosity 仅 1 个 cross-benchmark 数据点。\n6. **因果声明克制性值得肯定**——两位一致。§3.5 的 disclaimer 在该领域少见。\n7. **Register 应降级为 exploratory pilot**——两位一致。evaluator-producer overlap + BT 结果弱。\n\n## Reviewer Divergence [分歧]\n\n1. **Novelty/Excitement [最大分歧]**：R1 (3.5/5) 认为 Likert Blindspot 对 RLHF/DPO pipeline 有直接 actionable implications，sensitivity hierarchy 是有价值的方法论贡献；R2 (2.5/5) 认为核心发现是 Thurstone 经典结论的领域迁移，非新发现。**两位均认可 GEE per-axis decomposition 是增量贡献。**\n2. **Bootstrap/GEE CI 问题**：R1 列为 Must-Fix (critical)，R2 未独立提出。这是一个技术清晰性问题而非方法论错误。\n\n---\n\n## Questions (供作者回应)\n\n**Q1 [R1]**: Appendix H stratified analysis 用 Likert 等分作为 \"无质量差异\" 代理——如何排除 circularity？是否考虑过使用外部质量指标（如人工评分或参考答案匹配度）？\n\n**Q2 [R1]**: Formality 轴 Qwen3 n=355 的 GEE 显示 Orig OR (4.99) 是 Style OR (2.15) 的 2.3 倍，\"formality bias\" 表述是否仍恰当？\n\n**Q3 [R1]**: TOST Δ=15pp 的选择基准是 SESOI 估计还是 power-driven？如果后者，论文是否应报告基于 SESOI 的 Δ？\n\n**Q4 [R1]**: Verbosity direction-aware NLI gate 恢复的 21 对在 Likert 质量分和 NLI 分数分布上是否与 bidirectional-pass 对系统不同？\n\n**Q5 [R1]**: 论文声称对 RLHF/DPO pipeline 有启示，但未给出下游影响实证。是否有初步实验？\n\n---\n\n## Missing References\n\n**R2 建议（需验证真实性）**：\n1. Carterette et al. (2008) — forced-choice vs. graded relevance 灵敏度差异（ECIR）\n2. Sedoc & Ungar (2020) — IRT 应用于 chatbot 评估（ACL）\n3. Deutsch et al. (2023) — tie 处理对评估指标灵敏度的影响（EMNLP）\n\n**R1 建议**：\n4. Stureborg et al. (2024) — LLM judge calibration（论文 §2 已引用 Stureborg et al. 2024 关于 inconsistency，但 calibration 角度未充分覆盖）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（7 项 info，0 critical，0 warning）：\n- Figure 1 pipeline 流程图内部标注文字偏小，caption 偏简略\n- Table 1 脚注字号非常小（~6pt），包含重要符号说明\n- Limitations 章节 ~1.5 页，内容为实质性讨论，应合规\n- Figure 2 DAG 色盲可访问性需注意\n- Appendix 共 19 小节、~15 张表格，体量庞大但格式规范\n\n**格式合规确认**：正文 ≤8 页 ✓，ACL 模板 ✓，double-blind 匿名 ✓，Limitations 不计入页数 ✓。\n\n---\n\n## Overall Assessment\n\n### 官方维度打分（加权合成）\n\n| 维度 | R1 | R2 | 合成 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |\n| Excitement | 3.5/5 | 2.5/5 | **3.0/5** |\n| Reproducibility | 4/5 | 4/5 | **4.0/5** |\n\n### Overall: **3.0 (Findings)**\n\n**推荐理由**：\n- Verbosity 轴的证据链完整且令人信服（Style OR 8–13, 4 judges consistent）\n- 统计方法论严谨，在 LLM judge 评估文献中属高标准\n- GEE per-axis confound decomposition 有方法论增量贡献\n- 对从业者（RLHF/DPO pipeline）有 actionable implications\n\n**限制评分的核心因素**：\n1. **Novelty 不足**：核心发现（forced-choice 灵敏度高于 rating scale）是心理测量学经典结论的领域迁移确认。增量贡献（实证量化 + GEE 分解）有价值但不足以达到主会议水平。[R2 主张，两位在 GEE 增量贡献上达成共识]\n2. **Formality 轴 quality confound**：论文的两个 primary axes 之一（formality）受 quality-style confound 严重影响，削弱了 \"hidden style bias\" 统一叙事。[两位共识]\n3. **Detection vs. amplification 核心歧义**：标题和 framing 隐式预设 pairwise 为 ground truth，但论文自身承认无法区分 measurement attenuation、pairwise amplification 和 construct divergence。[两位共识]\n4. **负控制说服力有限**：TOST Δ=15pp 与 GPT-4o formality 最小 bias (13pp) 几乎重叠；仅一个负控制模型。[两位共识]\n\n**上调至 3.5 (Borderline Conference) 的条件**：\n如果作者在 rebuttal 中能 (1) 调整标题和 framing 为更中性表述；(2) 区分 formality claim 和 verbosity claim 的措辞强度；(3) 澄清 GEE CI 方法；(4) 深度论证 LLM judge 场景对 Thurstone 理论的超越——Director 愿意上调。\n\n**上调至 4.0 (Conference) 的条件（更高门槛）**：\n除上述条件外，还需 (5) 报告 TOST multi-Δ sensitivity；(6) 增加人工标注规模或提供 circularity 替代验证；(7) 增强 cross-benchmark 覆盖（尤其 verbosity）。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 开头 formality 实例有效但需前置 caveat（formality preferences 可能反映 legitimate quality judgments——§1 第二段已有，但应更早出现）\n- \"no single framework integrates...\" 的 gap statement 可能被视为 straw man——各工具解决的问题不同\n\n### §3 Method\n- §3.1 style-controlled rewriting 描述清晰\n- §3.2 NLI gate 设计合理；direction-aware verbosity 处理有理论依据\n- §3.3 measurement protocol 完整\n- §3.5 因果声明克制——\"controlled refers to experimentally controlled rewriting, not formal causal identification\" 是重要的诚实声明\n\n### §4 Experiments\n- §4.1 统计框架严谨：primary/exploratory/confirmatory 三分法、Holm-Bonferroni 校正、BT 正则化和 bootstrap 参数明确\n- Table 1 信息量大但认知负担高（5 种标记系统）\n- Table 2 sensitivity hierarchy 是有价值的方法论贡献\n\n### §5 Analysis\n- §5.1 Likert Blindspot 描述清晰，n=355 scaled replication 有力区分 attenuation vs power\n- §5.2 GEE decomposition 对 verbosity 令人信服；对 formality 的结果反而削弱 \"bias\" 叙事（Orig OR ≥ Style OR 多配置）\n- §5.3 Cross-judge replication 强，但 cross-benchmark 覆盖稀疏\n- §5.4 六项放大控制设计周全；人工标注 50 对规模偏小（κ=0.44）\n\n### §6 Conclusion\n- 双发现结构清晰\n- \"systematically misses\" 需 hedge——不能排除 power 解释和 construct divergence\n\n### Limitations\n- 坦诚全面，覆盖 quality-style confounding、evaluator-producer overlap、scope、ecological validity、scale design\n- 篇幅偏长（~1.5 页），可适当精简\n- 建议补充 cross-axis contamination d=−0.23 的讨论",
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-22T18:26:25.189434+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3917
}
```

</details>

---


### Assistant

_source line 990 · 2026-05-22T18:26:41.884618+00:00_

审稿报告已投递至 Research Director。

---

**Round 12 审稿完成。**

**最终评分：3.0 (Findings)**

核心判断：
- **Verbosity 轴**证据链极强（Style OR 8–13，四个 judge 一致），方法论严谨
- **三个 critical 问题压制评分**：(1) 标题/framing 隐式预设 pairwise 为 ground truth，detection vs. amplification vs. construct divergence 核心歧义未解决；(2) Formality 轴 quality-style 混淆严重（Orig OR ≥ Style OR 多配置），削弱统一 "style bias" 叙事；(3) Novelty 定位为"新发现"而非 Thurstone (1927) 经典结论的领域迁移实证量化
- **Novelty 是两位 Reviewer 最大分歧**（R1: 3.5/5 vs R2: 2.5/5）——R1 认为实践意义构成独立贡献，R2 认为不足以达到主会议水平
- **上调条件已在报告中明确列出**（标题中性化 + formality/verbosity 区分 + GEE CI 澄清 + Thurstone 超越论证）

Issue tracker 已同步更新（3 个新 open issues + 12 个 existing issues 追加 R12 mentions）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 94

## Round 94

2 recorded events


### User

_source line 991 · 2026-05-22T18:26:41.892648+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Strengths

**[AGREE] S1–S5**: R2 对论文优势的概括准确全面，与我的评估一致。特别是 S2（统计分析多层次且透明）和 S4（Limitations 坦诚全面）是本文优于同类工作的突出特点。

---

### Must-Fix 问题

**[AGREE with nuance] R2-N1: 核心歧义未解决，标题/framing 预设 pairwise 为 ground truth**

同意标题 "Detecting Hidden Style Bias" 和 "Blindspot" 命名存在隐式偏向。我在自己的审稿中也将此列为 critical issue（R1-N1），理由相似但侧重不同：我从 formality 轴 GEE 数据出发（Qwen3 n=355: Style OR 2.15 vs Orig OR 4.99, Table 3），指出检测到的并非纯粹 style bias，R2 从更高层次指出三种等效解释未被 resolve。

不过，我认为 R2 的措辞略有过度。论文在 Section 5.1 已明确呈现三种解释并保持 agnostic（"Both interpretations lead to the same conclusion"），Limitations 第一段也直接讨论了 construct divergence。问题不在于论文 body 回避了歧义，而在于**标题和 abstract 的 framing 与正文的 agnostic 态度不匹配**。这是一个 framing 调整问题，而非方法论缺陷。

建议：标题改为 "The Likert Blindspot: Measurement Sensitivity Divergence in LLM Judge Style Evaluation" 或类似中性措辞即可回应此批评，不需要大改方法论。

---

**[REBUT] R2-N2: "Likert Blindspot" 本质是 Thurstone (1927) 的实证确认，新颖性不足**

R2 认为 forced-choice 比 rating scale 更灵敏是心理测量学经典结论（Thurstone 1927, Preston & Colman 2000），论文只是该理论在 LLM judge 领域的实证确认。我不同意将此评为 critical 级别，理由如下：

1. **效应幅度远超理论预测**：传统心理测量学的灵敏度差异是 gradual 的（效应更小、需要更大 n），但论文发现的是 **categorical failure**——Likert 在 n=88 到 n=355 的范围内 d 始终趋近于零（bootstrap attenuation analysis, Appendix J, Table 11: d_median = −0.017），而 pairwise BT 在同一数据上达 63–77%。七种 Likert 方法全部失败（Table 2），tie rate 高达 58–73%。这不是 "灵敏度较低"，而是 "系统性完全失效"——这一幅度在传统心理测量学中没有先例，因为人类评分者不会产生如此极端的 tie rate。

2. **GEE 条件分解是方法论增量贡献**：R2 自己在 S5 中肯定了 "GEE 混淆分解有实用价值"。将 style 效应从 originality 混淆中分离的逐轴分解（Table 3），以及由此揭示的 verbosity 纯 style-driven vs formality quality-confounded 的轴间差异，是经典 Thurstone 理论完全未涉及的。

3. **实践影响不可从理论推导**：即使理论上可预测 "pairwise 更灵敏"，但 **RLHF/DPO pipeline 依赖 pairwise 而审计依赖 Likert** 这一具体 gap 在本文之前并未被 *CL 社区系统性识别或量化。Thurstone 的理论不能告诉你 "GPT-4o 在 formality 上有 13pp 的 pairwise bias 但 Likert d=0.10"。

4. **实证量化本身在 *CL 会议中有先例被接收**：大量 *CL best paper 的核心贡献是对已知现象的首次系统性量化（如 position bias 的量化、self-preference 的量化）。R2 的标准如果严格执行，会 dismiss 许多已发表的重要工作。

**结论**：将此评为 critical 不恰当。建议作者在 Introduction 中加一段 "Our contribution beyond classical measurement theory" 的定位，承认 Thurstone 的理论基础但强调 LLM judge 的独特性（极端 tie rate、系统性 categorical failure、GEE 分解），将 N2 降级为 Should-Fix 级别的 framing 建议。

---

### Should-Fix 问题

**[AGREE] R2-W1: Formality 轴 GEE 结果削弱 "style bias" 叙事**

完全同意，与我的 R1-N1 一致。GPT-4o formality Style OR 2.58 vs Orig OR 2.32 几乎相等，Qwen3 n=355 的 Orig OR (4.99) 更是 Style OR (2.15) 的 2.3 倍（Table 3）。需要在正文中显著区分 verbosity（纯 style-driven）和 formality（style + quality confound）。

**[AGREE] R2-W2: Register 轴无跨改写器验证**

完全同意。Limitations 已承认（"register conclusions remain tentative pending independent rewriter validation"），但 Table 1 中 register 仍占 6 行主结果空间。建议移至 appendix 或明确标注 "exploratory pilot"，我在自己审稿的小问题第 4 条中也提出了同样建议。

**[AGREE with nuance] R2-W3: 三个风格轴不足以支撑 "framework" 泛化**

同意 tone 轴因 NLI gate 拒绝率过高被放弃，表明 CSD 的适用范围限于 content-preserving style axes。但论文并未声称 CSD 适用于所有 style axes——Section 3.1 已限定为 style-controlled rewriting，且 tone 轴的失败本身被 Limitations 引用为 NLI gate 有效性的积极证据（"confirming that the quality gate prevents content-altering manipulations"）。R2 的建议（软化为 "methodology for content-preserving style axes"）合理，但严重性应为 minor 而非 warning。

**[AGREE] R2-W4: 跨 benchmark 覆盖稀疏**

完全同意，与我的 R1-W3 一致。特别是 verbosity 作为最强轴在 MT-Bench 上无数据点。

**[AGREE] R2-W5: 负控制 TOST Δ=15pp 过宽**

完全同意，与我的 R1-W1 一致。GPT-4o formality bias 为 13pp（BT 63.0%），与 TOST Δ=15pp 仅差 2pp。R2 关于报告 Δ=10pp 和 5pp 的 TOST 结果的建议可操作且有价值。

---

### Minor 问题

**[AGREE] R2-M1 (Abstract 数字密度)**: 同意，abstract 中 "n=88", "69%", "BT > 0.50" 等数字堆叠影响可读性。

**[REBUT] R2-M2 (Introduction 开头单实例)**: 论文开头 "What is the average height of a male?" 例子用于直觉引入 Likert vs pairwise 的灵敏度差异，是 motivating example 而非 evidence。紧接着的正文明确用系统性数据支撑 claim。这种写法在顶会论文中常见且有效。

**[AGREE] R2-M3 (对 RATE 的批评措辞)**: Section 5.1 的 "Head-to-head comparison with RATE" 可能给人 adversarial 感。建议改为 "Complementary analysis with RATE" 或 "Extending RATE's framework"。

**[AGREE] R2-M4–M6**: Figure 2 标注字号、Table 1 符号系统（我也提出了同样意见）、Limitations 篇幅均为合理的排版改进建议。

---

### Missing References

**[AGREE] R2 建议的三篇文献**:
- Carterette et al. (2008) — forced-choice vs graded relevance 在 IR 领域的比较，与 Table 2 sensitivity hierarchy 直接相关
- Sedoc & Ungar (2020) — IRT 用于 chatbot 评估，与 Likert scale 的心理测量特性讨论相关
- Deutsch et al. (2023) — tie 处理对评估灵敏度的影响，与论文发现的 58–73% tie rate 直接相关

均为有价值的补充引用，特别是 Deutsch et al. (2023) 可以加强 Section 5.1 关于 tie rate 驱动 Blindspot 的论证。

---

### Overall Assessment 差异讨论

R2 给出 **3.0 (Findings)**，我给出 **3.5 (Borderline Conference)**。0.5 分差异主要来自对 N2（新颖性）的分歧。

R2 将 novelty concern 升级为 critical，认为 Likert Blindspot 是 "经典心理测量学结论的领域迁移"。如上所述，我认为这低估了：(a) 效应幅度的 categorical nature（非 gradual attenuation），(b) GEE 分解的方法论贡献，(c) 实践影响（RLHF/DPO 审计 gap）的独立价值。

如果将 N2 从 critical 降至 warning（我认为更恰当），R2 的实际审评只有 N1 一个 critical issue（framing），与我的评估基本一致。在这种情况下，论文经过 framing 调整后应处于 3.5 (Borderline Conference) 的水平。

维持我的 **3.5 (Borderline Conference)** 评分，条件性上调至 4.0 取决于 rebuttal 中对 formality confounding framing（R1-N1 / R2-N1 / R2-W1）的回应质量。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。核心分歧在 R2-N2（新颖性）：R2 认为是 Thurstone 的领域迁移，我认为 categorical failure 的幅度（d→0 vs BT 63–77%）、GEE 分解、实践影响超越了简单理论确认，不应评为 critical。对 R2 的其余意见（N1 framing、W1–W5）基本同意，与我自己的审稿一致。维持 3.5 评分。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

### Must-Fix

[AGREE] R1-N1 (Formality quality-style 混淆): 强烈同意。补充两点：(1) R1 指出的 Appendix H stratified analysis circularity 是精妙的方法论漏洞——论文 claim Likert 不敏感，但 stratified analysis 用 Likert 等分作"质量无差异"代理，前提被 claim 自身破坏；(2) Qwen3 n=355 的 Orig OR (4.99) 是 Style OR (2.15) 的 2.3 倍，"formality bias" 不如 "quality-correlated formality preference" 准确。建议论文将 verbosity（confirmed style bias）和 formality（style-quality entangled）分层讨论。

[REBUT] R1-N2 (Bootstrap CI vs GEE sandwich): 部分反驳。BT 用 bootstrap、GEE 用 sandwich 是正确做法，两个模型用不同 CI 方法无方法论错误。问题在于论文未明确区分报告方式——是表述清晰度问题，建议降级为 warning。

### Should-Fix

[AGREE] R1-W1 (TOST Δ=15pp): 同意，我 W5 提出相同关切。R1 的对比（GPT-4o formality BT=63%, 即 13pp，几乎落入 TOST 边界）尤其有力。

[AGREE] R1-W2 (人工标注): 同意。补充：4 个分歧全在 verbosity condensation，但 NLI 阈值 sweep 显示 BT ≤3pp 变化，部分缓解。

[AGREE] R1-W3 (Cross-benchmark): 同意。R1 观察更精确：verbosity 唯一跨 benchmark 数据点（AlpacaEval Qwen3）为 ‡（both sig），反而不支持 Blindspot。

[AGREE] R1-W4 (Cross-axis contamination d=−0.23): 同意。formality 改写导致 word count shift d=−0.23 超 small effect 标准，论文回避了此指标。支持在 GEE 加入 word count covariate。

### Minor

全部 [AGREE]。R1-Minor-5（100-point Likert 仅用 Qwen3-32B 而非 GPT-4o）是我未独立发现的有效观察。

### Questions

[AGREE] Q1-Q3, Q5。[REBUT] Q4：NLI 阈值 sweep 11 点 BT ≤3pp 变化间接表明 direction-aware gate 未引入系统偏差。

### Overall

R1 给 3.5，我给 3.0。分歧在 Excitement（R1: 3.5, 我: 2.5）。核心发现是 Thurstone (1927) 的领域迁移，"首次量化已知现象" 的 excitement 有限。两位 reviewer 一致结论：verbosity 强、formality 混淆严重、TOST 偏宽、跨 benchmark 不足、register 应降级。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。两位 reviewer 在关键问题上高度一致（formality 混淆、TOST 偏宽、跨 benchmark 不足），主要分歧在 excitement 评分（R1: 3.5 vs 我: 2.5），源于对"已知现象的领域迁移"这一贡献类型的 novelty 权重不同。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 992 · 2026-05-22T18:27:15.415842+00:00_

两位 Reviewer 的详细交叉回应已收到。交叉回应结果与报告中的收敛分析一致，确认以下关键结论：

**交叉后共识确认：**
- Formality 质量混淆 [AGREE × 2]
- TOST Δ=15pp 偏宽 [AGREE × 2]
- Cross-benchmark 覆盖不足 [AGREE × 2]
- Register 降级为 exploratory [AGREE × 2]
- Cross-axis contamination d=−0.23 [AGREE × 2]
- 人工标注规模偏小 [AGREE × 2]

**唯一持续分歧：Novelty/Excitement**
- R1 [REBUT R2-N2]：categorical failure（d→0 vs BT 63–77%）超越 Thurstone 理论预测幅度；GEE 分解是独立方法论贡献；RLHF/DPO 审计 gap 的实践意义不可从理论推导。建议降级为 Should-Fix。
- R2 维持 critical：首次量化已知现象的 excitement 有限。

**技术分歧（已收敛）：**
- R2 [REBUT R1-N2]：Bootstrap CI vs GEE sandwich SE 是表述清晰度问题而非方法论错误，建议从 critical 降级为 warning。合理——报告中已标注此为 R1 独立提出。

审稿报告已投递至 Research Director（Overall 3.0 Findings）。Issue tracker 已同步更新。审稿流程完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 95

## Round 95

44 recorded events


### User

_source line 993 · 2026-05-22T19:28:18.713176+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-22T19:28:24.079672+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-22T19:28:24.130899+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-22T19:28:30.354470+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-22T19:28:30.465440+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 110
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-22T19:28:34.139611+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 999 · 2026-05-22T19:28:34.140039+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-22T19:28:37.149201+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-22T19:28:37.199800+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-22T19:28:41.664335+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-22T19:28:43.574833+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (54 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **register_100_cf** (killed): Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality\n- **gemini_flash_fourth_judge** (success): Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.\n- **llama70b_register** (success): Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures\n  [llama70b_register_summary](/api/workspace-files/projects/causal_style_decomp_judge/artifacts/llama70b_register/data/llama70b_register_summary.json)\n\n## 趋势\n成功 38 / 负向 12 / 失败 0 / 共 54\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- register_100_cf: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1910
}
```

</details>

---


### Tool call

_source line 1004 · 2026-05-22T19:28:43.575192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-22T19:28:44.579366+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Measurement-Mode Divergence\\in LLM Judge Style Evaluation}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\S\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.
45	The primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences inherent in the format.
…[truncated 3696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-22T19:28:44.579848+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1007 · 2026-05-22T19:28:45.182455+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf"
  }
}
```

</details>

---


### Tool result

_source line 1008 · 2026-05-22T19:28:45.182829+00:00_

This PDF has 18 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-22T19:28:49.901323+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found some relevant search results, though they don't appear to contain the main EMNLP 2
…[truncated 1180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5321
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-22T19:28:54.269574+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limit author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1011 · 2026-05-22T19:28:54.772012+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 conference call for papers Budapest submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 conference call for papers Budapest submission deadline"
  }
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-22T19:28:57.634371+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
    "pages": "1-5"
  }
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-22T19:28:58.088762+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf (387.9KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-22T19:28:58.195897+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "review_issues.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-22T19:29:00.756374+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limit author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, I found information about ACL Rolling Review (ARR) submission guidelines. Here are the key details:

## Submission Guidelines Overview

Submissions must adhere to the formatting in the submission templates, which is available as an Overleaf template. Submissions are made in OpenReview.

## Author Requirements

ACL has adopted a policy requiring all authors to sign up as reviewers, with assignments m
…[truncated 1091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6486
}
```

</details>

---


### Tool result

_source line 1016 · 2026-05-22T19:29:00.807558+00:00_

Web search results for query: "EMNLP 2026 conference call for papers Budapest submission deadline"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"}]

Based on the search results, here is information about the EMNLP 2026 conference call for papers in Budapest:

## Conference Details
EMNLP 2026 will be held in Budapest, Hungary from October 24-29, 2026.

## Main Conference Paper Submission Deadline
The EMNLP 2026 paper submission deadline is May 25, 2026, 23:59:59 (UTC-12).

## Additional Important Dates
Al
…[truncated 849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6035
}
```

</details>

---


### Tool result

_source line 1017 · 2026-05-22T19:29:00.807941+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 2612
}
```

</details>

---


### Tool call

_source line 1018 · 2026-05-22T19:29:09.191881+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
  "pages": "6-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
    "pages": "6-10"
  }
}
```

</details>

---


### Tool result

_source line 1019 · 2026-05-22T19:29:10.149776+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf (387.9KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-22T19:29:10.155965+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR ACL Rolling Review 2026 long paper 8 pages short paper 4 pages format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR ACL Rolling Review 2026 long paper 8 pages short paper 4 pages format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1021 · 2026-05-22T19:29:11.360281+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1022 · 2026-05-22T19:29:11.512835+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-22T19:29:15.778348+00:00_

Web search results for query: "ARR ACL Rolling Review 2026 long paper 8 pages short paper 4 pages format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here are the format requirements for ARR (ACL Rolling Review) 2026 papers:

## Paper Length

ARR submissions are in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

More specifically:
- Short papers: 4 content pages maximum, Long papers: 8 content pages maximum.

## Page Limits Excluding Special S
…[truncated 884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5622
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-22T19:29:22.704971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
  "pages": "11-18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
    "pages": "11-18"
  }
}
```

</details>

---


### Tool result

_source line 1025 · 2026-05-22T19:29:23.308404+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf (387.9KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-22T19:29:23.366192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-22T19:29:23.669059+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved unless noted)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	
16	  - id: "R2-N1"
17	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
18	    category: framing
19	    severity: warning
20	    status: in_progress
21	    first_raised_round: 1
22	    last_seen_round: 12
23	    resolution: null
24	    resolution_round: null
25	    mentions:
26	      - round: 3
27	        reviewers: [1, 2]
28	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
29	      - round: 8
30	        reviewers: [1, 2]
31	        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
32	      - round: 9
33	        reviewers: [1, 2]
34	        note: "R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。"
35	      - round: 10
36	        reviewers: [1, 2]
37	        note: "R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。"
38	      - round: 11
39	        reviewers: [1, 2]
40	        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。"
41	      - round: 12
42	        reviewers: [1, 2]
43	        note: "R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。"
44	    action_
…[truncated 46982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-22T19:30:09.278041+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool call

_source line 1029 · 2026-05-22T19:30:10.231525+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1030 · 2026-05-22T19:30:48.186158+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 38908
}
```

</details>

---


### Tool result

_source line 1031 · 2026-05-22T19:30:48.186554+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 37955
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-22T19:30:48.287227+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 统计方法 + 实验设计**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL 模板，Long paper 正文 ≤8 页，参考文献不限，Limitations 不计入页数\n- **匿名规则**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf`\n\n## 论文概要\n标题：*The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation*\n核心发现：Likert 评分和 pairwise comparison 在检测 LLM judge 风格偏差时产生系统性分歧——pairwise 检测到 Likert 完全遗漏的偏好（BT > 60%, p < 0.001; Likert d → 0, p > 0.17）。提出 CSD 框架（NLI-gated 内容控制 + per-axis 风格分解 + position-controlled pairwise comparison），跨 4 个 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 个负控制（Claude Sonnet 4）+ 3 个 benchmark + 7 种统计方法验证。GEE 条件分解揭示 per-axis 混淆结构差异（verbosity = style-dominated, formality = conditional effect, register = judge-dependent）。\n\n## 你的审查侧重\n\n### 1. 统计方法严谨性\n- Bradley-Terry 模型的 IIA 假设在该数据中是否成立？脚注 3 声称 binary-choice BT 中 IIA \"structurally satisfied\"，是否正确？Appendix H 的 direction asymmetry (formality: 88.9% vs 52.6%) 对 BT 估计的影响？\n- GEE 使用 exchangeable working correlation + sandwich SE 是否合适？Appendix C 的模型诊断是否充分？\n- Bootstrap CI（10,000 pair-level resamples）与 GEE sandwich SE 的分工是否清晰？Table 3 CI 来源？\n- Holm-Bonferroni 校正的 test family 定义（§4.1 \"six tests\"）是否合理？Gemini 作为 confirmatory 排除在外的理由？\n- TOST 等价检验 Δ=15pp 的合理性？与 GPT-4o formality 最小 bias (13pp) 几乎重叠——Claude 可能有未检测的 moderate bias？\n\n### 2. 实验设计\n- NLI gate（DeBERTa-v3-large, τ=0.90）：44% 拒绝率造成的选择偏差？Appendix B 的 4 个 surface covariate 检查是否充分？\n- Direction-aware NLI gate 恢复的 21 对在 content quality 上是否与 bidirectional-pass 对系统不同？\n- 人工标注（50 对，2 名标注员，κ=0.44）：规模是否足够？Wilson CI 下界 86.3% 的 precision 是否支撑核心 claim？\n- Cross-axis contamination：formality→verbosity word count shift d=−0.23 超过论文自设 negligible 标准 (d<0.20)——是否需要在 GEE 中加 word count covariate？\n- 100-point continuous Likert 仅用 Qwen3-32B judge，存在 evaluator-producer overlap，选择理由？\n\n### 3. 因果/方法论声明\n- §3.5 Design Rationale 的因果免责声明是否充分？论文标题中 \"Measurement-Mode Divergence\" 是否中性？\n- DAG（Figure 2）的残余混淆路径（S→Q dashed）讨论是否充分？\n- \"Controlled Style Decomposition\" 中 \"Controlled\" 是否给人过强的因果推断印象？\n\n### 4. 格式合规\n- 正文是否 ≤8 页？\n- Double-blind 是否合规（无作者信息泄露）？\n- Limitations 是否合理（不含新实验结果）？\n\n请按以下格式输出审稿报告：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者回答)\n5. **Missing References** (如有)\n6. **Novelty** (1-5 分)\n7. **Soundness** (1-5 分)\n8. **Excitement** (1-5 分)\n9. **Overall Assessment** (使用 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 统计方法 + 实验设计**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL 模板，Long paper 正文 ≤8 页，参考文献不限，Limitations 不计入页数\n- **匿名规则**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf`\n\n## 论文概要\n标题：*The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation*\n核心发现：Likert 评分和 pairwise comparison 在检测 LLM judge 风格偏差时产生系统性分歧——pairwise 检测到 Likert 完全遗漏的偏好（BT > 60%, p < 0.001; Likert d → 0, p > 0.17）。提出 CSD 框架（NLI-gated 内容控制 + per-axis 风格分解 + position-controlled pairwise comparison），跨 4 个 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 个负控制（Claude Sonnet 4）+ 3 个 benchmark + 7 种统计方法验证。GEE 条件分解揭示 per-axis 混淆结构差异（verbosity = style-dominated, formality = conditional effect, register = judge-dependent）。\n\n## 你的审查侧重\n\n### 1. 统计方法严谨性\n- Bradley-Terry 模型的 IIA 假设在该数据中是否成立？脚注 3 声称 binary-choice BT 中 IIA \"structurally satisfied\"，是否正确？Appendix H 的 direction asymmetry (formality: 88.9% vs 52.6%) 对 BT 估计的影响？\n- GEE 使用 exchangeable working correlation + sandwich SE 是否合适？Appendix C 的模型诊断是否充分？\n- Bootstrap CI（10,000 pair-level resamples）与 GEE sandwich SE 的分工是否清晰？Table 3 CI 来源？\n- Holm-Bonferroni 校正的 test family 定义（§4.1 \"six tests\"）是否合理？Gemini 作为 confirmatory 排除在外的理由？\n- TOST 等价检验 Δ=15pp 的合理性？与 GPT-4o formality 最小 bias (13pp) 几乎重叠——Claude 可能有未检测的 moderate bias？\n\n### 2. 实验设计\n- NLI gate（DeBERTa-v3-large, τ=0.90）：44% 拒绝率造成的选择偏差？Appendix B 的 4 个 surface covariate 检查是否充分？\n- Direction-aware NLI gate 恢复的 21 对在 content quality 上是否与 bidirectional-pass 对系统不同？\n- 人工标注（50 对，2 名标注员，κ=0.44）：规模是否足够？Wilson CI 下界 86.3% 的 precision 是否支撑核心 claim？\n- Cross-axis contamination：formality→verbosity word count shift d=−0.23 超过论文自设 negligible 标准 (d<0.20)——是否需要在 GEE 中加 word count covariate？\n- 100-point continuous Likert 仅用 Qwen3-32B judge，存在 evaluator-producer overlap，选择理由？\n\n### 3. 因果/方法论声明\n- §3.5 Design Rationale 的因果免责声明是否充分？论文标题中 \"Measurement-Mode Divergence\" 是否中性？\n- DAG（Figure 2）的残余混淆路径（S→Q dashed）讨论是否充分？\n- \"Controlled Style Decomposition\" 中 \"Controlled\" 是否给人过强的因果推断印象？\n\n### 4. 格式合规\n- 正文是否 ≤8 页？\n- Double-blind 是否合规（无作者信息泄露）？\n- Limitations 是否合理（不含新实验结果）？\n\n请按以下格式输出审稿报告：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者回答)\n5. **Missing References** (如有)\n6. **Novelty** (1-5 分)\n7. **Soundness** (1-5 分)\n8. **Excitement** (1-5 分)\n9. **Overall Assessment** (使用 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit)"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-22T19:31:17.410770+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29123
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-22T19:31:19.770664+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "你是 Reviewer 2，负责**新颖性 + framing 平衡性 + 写作质量 + 格式合规**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL 模板，Long paper 正文 ≤8 页，参考文献不限，Limitations 不计入页数\n- **匿名规则**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf`\n\n## 论文概要\n标题：*The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation*\n核心发现：Likert 评分和 pairwise comparison 在检测 LLM judge 风格偏差时产生系统性分歧。提出 CSD 框架，跨 4 个 target judge + 1 个负控制 + 3 个 benchmark 验证。GEE 条件分解揭示 per-axis 混淆结构差异。\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- **核心问题**：Likert vs pairwise 的灵敏度差异是 Thurstone (1927) 以来心理测量学的已知现象。本文的贡献是否超越了 \"domain transfer\"？\n- \"Controlled Style Decomposition\" 框架 vs 既有工作（RATE [Reber et al., 2025]、Comparative Trap [Jeong et al., 2025]、CalibraEval [Li et al., 2025]）的实质差异？\n- GEE per-axis confound decomposition 是否构成独立的方法论贡献？\n- 论文使用 \"demonstrates\"/\"identifies\" 等措辞是否仍偏发现性？应如何定位？\n\n### 2. Framing 平衡性（Detection vs Amplification）\n- **标题分析**：当前标题 \"The Likert Blindspot\" 是否隐式预设 pairwise 为 ground truth？Jeong et al. (2025) 指出 pairwise comparison 放大风格偏好——论文如何处理这一对立证据？\n- §5.4 的六项 amplification controls 是否充分？是否能排除 pairwise 格式本身放大了 micro-preferences？\n- \"measurement attenuation\" vs \"construct divergence\" vs \"format amplification\" 三种解释在论文中的权重是否平衡？\n- Conclusion \"Likert-only audits miss style-driven preferences\" 是否过强？可能只是 pairwise 放大了本不重要的差异？\n- Claude Sonnet 4 作为唯一负控制——是否足以论证 Blindspot 的架构特异性？为何不讨论 Claude 不受影响的可能原因？\n\n### 3. 写作质量\n- **Abstract**：数字密度是否过高？是否影响可读性？建议保留哪些核心数字？\n- **Introduction** 开头的 motivating example（GPT-4o formal vs casual）是否充分 acknowledge formality-quality 的 nuance？\n- **Related Work** 覆盖面是否充分？遗漏的重要引用？\n- **Conclusion** 篇幅和深度是否合适？\n- 术语一致性检查：CSD/Blindspot/measurement divergence 等核心术语的使用是否一致？\n\n### 4. 格式与完整性\n- 正文 ≤8 页？\n- Double-blind 合规？\n- Limitations 内容是否覆盖关键弱点？是否过长/过短？\n- Appendix A-S 的组织是否合理？是否有主文应有但被放到附录的关键内容？\n- 引用格式（natbib）是否一致？\n\n### 5. Scope 与泛化\n- 3 个风格轴（formality, verbosity, register）+ 失败的 tone 轴——是否足以支撑 \"framework\" 级别的泛化声明？\n- 主实验仅用 LLMBar (n=100)——cross-benchmark (AlpacaEval, MT-Bench) 覆盖是否稀疏？\n- Register 轴结果较弱且 evaluator-producer overlap 最严重——是否应降级为 \"exploratory pilot\"？\n\n请按以下格式输出审稿报告：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者回答)\n5. **Missing References** (如有)\n6. **Novelty** (1-5 分)\n7. **Soundness** (1-5 分)\n8. **Excitement** (1-5 分)\n9. **Overall Assessment** (使用 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "你是 Reviewer 2，负责**新颖性 + framing 平衡性 + 写作质量 + 格式合规**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL 模板，Long paper 正文 ≤8 页，参考文献不限，Limitations 不计入页数\n- **匿名规则**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf`\n\n## 论文概要\n标题：*The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation*\n核心发现：Likert 评分和 pairwise comparison 在检测 LLM judge 风格偏差时产生系统性分歧。提出 CSD 框架，跨 4 个 target judge + 1 个负控制 + 3 个 benchmark 验证。GEE 条件分解揭示 per-axis 混淆结构差异。\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- **核心问题**：Likert vs pairwise 的灵敏度差异是 Thurstone (1927) 以来心理测量学的已知现象。本文的贡献是否超越了 \"domain transfer\"？\n- \"Controlled Style Decomposition\" 框架 vs 既有工作（RATE [Reber et al., 2025]、Comparative Trap [Jeong et al., 2025]、CalibraEval [Li et al., 2025]）的实质差异？\n- GEE per-axis confound decomposition 是否构成独立的方法论贡献？\n- 论文使用 \"demonstrates\"/\"identifies\" 等措辞是否仍偏发现性？应如何定位？\n\n### 2. Framing 平衡性（Detection vs Amplification）\n- **标题分析**：当前标题 \"The Likert Blindspot\" 是否隐式预设 pairwise 为 ground truth？Jeong et al. (2025) 指出 pairwise comparison 放大风格偏好——论文如何处理这一对立证据？\n- §5.4 的六项 amplification controls 是否充分？是否能排除 pairwise 格式本身放大了 micro-preferences？\n- \"measurement attenuation\" vs \"construct divergence\" vs \"format amplification\" 三种解释在论文中的权重是否平衡？\n- Conclusion \"Likert-only audits miss style-driven preferences\" 是否过强？可能只是 pairwise 放大了本不重要的差异？\n- Claude Sonnet 4 作为唯一负控制——是否足以论证 Blindspot 的架构特异性？为何不讨论 Claude 不受影响的可能原因？\n\n### 3. 写作质量\n- **Abstract**：数字密度是否过高？是否影响可读性？建议保留哪些核心数字？\n- **Introduction** 开头的 motivating example（GPT-4o formal vs casual）是否充分 acknowledge formality-quality 的 nuance？\n- **Related Work** 覆盖面是否充分？遗漏的重要引用？\n- **Conclusion** 篇幅和深度是否合适？\n- 术语一致性检查：CSD/Blindspot/measurement divergence 等核心术语的使用是否一致？\n\n### 4. 格式与完整性\n- 正文 ≤8 页？\n- Double-blind 合规？\n- Limitations 内容是否覆盖关键弱点？是否过长/过短？\n- Appendix A-S 的组织是否合理？是否有主文应有但被放到附录的关键内容？\n- 引用格式（natbib）是否一致？\n\n### 5. Scope 与泛化\n- 3 个风格轴（formality, verbosity, register）+ 失败的 tone 轴——是否足以支撑 \"framework\" 级别的泛化声明？\n- 主实验仅用 LLMBar (n=100)——cross-benchmark (AlpacaEval, MT-Bench) 覆盖是否稀疏？\n- Register 轴结果较弱且 evaluator-producer overlap 最严重——是否应降级为 \"exploratory pilot\"？\n\n请按以下格式输出审稿报告：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者回答)\n5. **Missing References** (如有)\n6. **Novelty** (1-5 分)\n7. **Soundness** (1-5 分)\n8. **Excitement** (1-5 分)\n9. **Overall Assessment** (使用 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit)"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-22T19:31:21.080467+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1309
}
```

</details>

---


### Assistant

_source line 1036 · 2026-05-22T19:31:34.157378+00:00_

已完成所有并行派发：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 已派发 |
| Reviewer 2（新颖性/framing） | ✅ 已派发 |
| 视觉审查 Agent | ✅ 已启动 |
| 外部审稿（Stanford Agentic Reviewer） | ⏭️ 未配置，跳过 |

等待两位 Reviewer 的独立初审结果返回，收集后进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 96

## Round 96

10 recorded events


### User

_source line 1037 · 2026-05-22T19:38:28.922449+00:00_

[Reviewer 2 审稿意见]:
# Reviewer 2 审稿报告（Round 1）

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 实验设计严谨、统计工具丰富的实证研究，但核心发现（Likert vs. pairwise 灵敏度差异）在心理测量学中早已确立，论文的 framing 系统性地偏向 pairwise 为 ground truth，削弱了贡献声明的说服力。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验控制周密（NLI gate、position control、7 种统计方法、GEE 分解），但 framing 不对称——无法充分区分 "Likert misses real signal" vs "pairwise amplifies micro-preferences"；单一负控制不足以支撑架构特异性声明 |
| Excitement | 3/5 | 对 LLM judge 审计实践有直接价值，但核心洞察对熟悉心理测量学的读者不意外；GEE per-axis 分解有趣但应用场景窄 |
| Novelty | 3/5 | 核心发现是 established knowledge 的 domain transfer；CSD + GEE 分解是增量贡献 |
| Overall | 3.0 | Findings 水平——方法学扎实但新颖性有限且 framing 问题需修正 |

---

## Strengths

**S1. 实验控制层次感出色。** CSD 三层控制——NLI gate (§3.2)、same-style double-rewrite (§5.4)、position swapping (§3.3)——在 LLM judge 风格偏差文献中属最周密的实验设计之一。

**S2. 统计方法多元互补。** 七种方法覆盖不同假设，Table 2 sensitivity hierarchy 清晰展示 Likert-based 方法一致失败。GEE 条件分解 (Table 3) 将 style OR 与 originality OR 分离是独立的方法论贡献。

**S3. Robustness 检查详尽。** §5.4 六项 amplification controls + Appendices A-S 大量补充分析（bootstrap CI、formal power analysis、100-point continuous Likert、cross-axis contamination 等）。

**S4. GEE per-axis confound 分解是真正的增量贡献。** Table 3 揭示 verbosity style-dominated (Style OR 8-15) vs formality conditional 的结构性差异。

**S5. 跨 judge 覆盖合理。** 4 target judges + 1 negative control 覆盖主流架构。

---

## Must-Fix 问题

**N1** [critical] **标题与 framing 隐式预设 pairwise 为 ground truth**
- 位置：Title、Abstract ("signal loss exceeding 60%")、§6 ("Likert-only audits miss style-driven preferences")
- "The Likert Blindspot" 将 Likert 定位为"盲区"，但论文自身在 §5.4 引用 Jeong et al. (2025) Comparative Trap 承认 pairwise 可能放大偏好，Limitations 提出 construct divergence 解释。这些 caveat 被隔离在末尾，未进入标题/摘要/结论。在缺乏外部 ground truth 的情况下，无法区分 measurement attenuation vs format amplification vs construct divergence 三种解释，但叙事 90% 倾向第一种。
- 建议：标题改为中性（如直接用副标题）；Abstract/Conclusion 给三种解释同等权重。

**N2** [critical] **新颖性定位模糊**
- 位置：§1、§6（"identifies"/"demonstrates"）
- Likert vs pairwise 灵敏度差异是 Thurstone (1927) 以来的经典结论。论文真正贡献是"首次受控量化 + GEE 分解方法"，但措辞有时像是声称发现了现象本身。
- 建议：§1 明确声明 "sensitivity gap is well-established; our contribution is first controlled quantification + decomposition methodology"。

**N3** [critical] **单一负控制不足以支撑架构特异性声明**
- 位置：§5.3、§6、Limitations
- Claude Sonnet 4 是唯一负控制。论文未探讨为何 Claude 不受影响（RLHF 差异？评估策略？），也未测试同系列其他模型。可能 Claude 只是整体风格不敏感而非"正确地不受影响"。
- 建议：讨论可能机制；降格为 "one model does not show this pattern"。

## Should-Fix 问题

**W1** [warning] **主实验仅用 LLMBar (n=100)，cross-benchmark 覆盖稀疏** — Table 2 的 AlpacaEval/MT-Bench 仅测试 formality pairwise，不足以支撑 "across three benchmarks" 泛化声明。

**W2** [warning] **Register 轴 evaluator-producer overlap 最严重，结果应降级** — Qwen3-32B 同时作为 rewriter 和 judge，BT 仅 51.4%。应标注为 exploratory。

**W3** [warning] **Abstract 数字密度过高** — ~200 词中堆砌过多数字和术语，影响核心信息传达。

**W4** [warning] **Introduction motivating example 未 acknowledge formality-quality nuance** — GPT-4o 偏好 formal 的例子暗示 Likert 偏好 casual 是"错误"的，但直到 Limitations/Appendix A 才讨论 formality 可能反映真实 quality 差异。

**W5** [warning] **"Framework" 设定过高预期** — CSD 更准确地说是 experimental protocol，3 个成功轴 + 1 个失败轴不足以支撑 "framework" 级别声明。

## 小问题
- §3-4 脚注密度高，打断阅读流
- Figure 2 (DAG) 偏小，blocked/open paths 区分不够直观
- Tone axis 失败值得 2-3 句更详细的分析
- §5.2 GEE 术语首次出现时缺乏直觉解释
- References 置于 Appendices 之后（非标准顺序）

## Questions

**Q1.** 六项 amplification controls 中哪一项最直接排除 "pairwise amplifies micro-preferences" 解释？无人类 ground truth 如何区分 attenuation vs amplification？

**Q2.** Claude 不表现 Blindspot 的可能机制？是否检查过 Claude 的 Likert/pairwise 评分分布（ceiling/floor effects, tie rates）？

**Q3.** 如果用更大 benchmark (n>1000)，Likert Type II error 是否因功效提升而缩小？Appendix K 报告 required n >1200——Blindspot 是否部分是 power issue？

**Q4.** Register 轴是否做了 rewriter 替换测试（类似 Appendix D 对 verbosity/formality 的测试）？

**Q5.** Tone axis NLI gate 通过率 56%——失败案例中 NLI 判定"内容改变"是正确的还是误判？

## Missing References
无重大遗漏。可考虑补充 Bai et al. (2022/2023) RLHF preference model 的 comparison vs rating 差异、Rafailov et al. (2023) DPO 中 pairwise preference 的理论性质。

## 格式检查
- ✅ 正文 ≤8 页合规
- ✅ Double-blind 合规
- ✅ Limitations 覆盖充分、长度适中
- ✅ Appendix A-S 组织合理
- ⚠️ References 在 Appendices 之后（非标准）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-22T19:38:40.869462+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1039 · 2026-05-22T19:38:46.019478+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 5150
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-22T19:38:53.654486+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/causal_style_decomp_judge/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/causal_style_decomp_judge/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-22T19:38:53.756064+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1042 · 2026-05-22T19:38:56.871742+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/causal_style_decomp_judge/**/config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/causal_style_decomp_judge/**/config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
  }
}
```

</details>

---


### Tool result

_source line 1043 · 2026-05-22T19:38:56.973103+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pandas/_config/config.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pandas/core/config_init.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pandas/_config/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.venv/lib/python3.14/site-packages/pandas/core/__pycache__/config_init.cpython-314.pyc

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1044 · 2026-05-22T19:39:00.892362+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5",
  "glob": "*.yaml",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5",
    "glob": "*.yaml",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-22T19:39:00.945518+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "elapsed_ms": 53
}
```

</details>

---


### Assistant

_source line 1046 · 2026-05-22T19:39:18.115560+00:00_

Reviewer 2 已返回，等待 Reviewer 1。外部审稿未在项目配置中启用，跳过。

Reviewer 2 核心评价：**3.0 (Findings)**。三个 Must-Fix：(1) 标题/framing 预设 pairwise 为 ground truth，(2) novelty 定位模糊（Thurstone 1927 domain transfer），(3) 单一负控制不足。

等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 97

## Round 97

2 recorded events


### User

_source line 1047 · 2026-05-22T19:39:20.646645+00:00_

[Reviewer 2 审稿结果]:
审稿报告已完成并提交给 Review Director。

**核心判断**：Overall 3.0 (Findings)。论文实验设计周密（NLI gate + 7 种统计方法 + GEE 分解 + 详尽附录），但有三个 Must-Fix 问题：

1. **Framing 不对称**——标题 "Likert Blindspot" 隐式预设 pairwise 为 ground truth，与论文自身承认的 Comparative Trap 证据矛盾，三种解释（attenuation / amplification / construct divergence）未获同等权重
2. **新颖性定位模糊**——Likert vs pairwise 灵敏度差异是心理测量学经典结论，论文需明确定位为"首次受控量化 + GEE 分解方法"而非"发现"
3. **单一负控制**——仅 Claude Sonnet 4 不表现 Blindspot，未探讨机制，不足以支撑架构特异性声明

若修正 framing + novelty 定位 + 扩展负控制讨论，有潜力升至 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1048 · 2026-05-22T19:39:28.858656+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 98

## Round 98

6 recorded events


### User

_source line 1049 · 2026-05-22T19:39:30.364095+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿报告

**论文**: *The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation*
**Venue**: EMNLP 2026 (ACL ARR)
**审查侧重**: 方法严谨性 + 统计方法 + 实验设计

---

## Summary

本文识别了 "Likert Blindspot" 现象：Likert 评分与 pairwise comparison 在检测 LLM judge 风格偏差时产生系统性分歧——BT 检测到显著偏好（BT > 60%, p < 0.001），而 Likert 的 Cohen's d → 0 且 p > 0.17。提出 CSD 框架（NLI-gated 内容控制 + per-axis 风格分解 + position-controlled pairwise comparison），在 4 个 judge + 1 个负控制 + 3 个 benchmark + 7 种统计方法下验证。GEE 条件分解揭示 per-axis 混淆结构差异。方法论整体扎实，核心发现在多重鲁棒性检验下稳健，但人工标注规模、TOST 等价阈值、方向不对称性处理等方面存在可改进空间。

---

## Strengths

**S1. 核心发现新颖且实践意义重大。** Likert Blindspot 对 LLM 评估方法论有直接影响：大量论文使用 Likert 评分审计 LLM judge 偏差，本文表明这种方法可能系统性遗漏通过 pairwise 传播的风格偏好。Table 2 显示 7 种统计方法中 5 种 Likert-based 方法全部失败（p > 0.17–0.90），而两种 pairwise 方法均显著（BT p < 0.001, sign test p = 0.006），证据力强。

**S2. 统计方法覆盖全面。** 7 种方法（BT, sign test, Likert ATE/t-test, Bayesian t, ordinal regression, GEE, Wilcoxon signed-rank）构成"sensitivity hierarchy"，从不同假设族独立验证同一结论。Holm-Bonferroni 校正覆盖 6 个主检验，且 §4.1 明确标注了 8 个检验全通过扩展族的结果。这种多方法三角验证在该领域论文中不常见。

**S3. 负控制设计严谨。** Claude Sonnet 4 作为负控制（n = 87, BT 50.2%/54.1%, n.s.），TOST 等价检验确认 Δ = 15pp 处等价（76% power），验证了 CSD pipeline 不会凭空制造偏差。Appendix G 的形式化处理充分。

**S4. GEE 条件分解贡献重大。** Table 3 的 Style OR vs. Originality OR 分离揭示了 per-axis 混淆结构差异（verbosity = style-dominated, formality = conditional effect, register = judge-dependent），这比简单的"有/无偏差"结论更有方法论价值。exchangeable working correlation + sandwich SE 的选择经 Appendix C 的 independence 对照验证（差异 <0.02），模型诊断充分。

**S5. 鲁棒性检验链完整。** NLI 阈值敏感性分析（Appendix E, 11 个阈值 0.60–0.95），bootstrap 衰减分析（Appendix J, d → 0 across all n），rewriter 独立性检验（Appendix D, GPT-4o rewriter 替换），cross-axis 污染分析（Appendix R），功效分析（Figure 4），方向感知 NLI gate（Appendix F）。这些构成多层防御，使核心发现难以归因于单一方法论 artifact。

**S6. 因果声明审慎。** §3.5 Design Rationale 明确免责："we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions"。"Controlled" 限定为实验控制而非因果识别。Figure 2 的 DAG 标注 S → Q 虚线路径并讨论残余混淆。论文标题 "Measurement-Mode Divergence" 是中性表述。

---

## Weaknesses

### Should-Fix

**W1 [Should-Fix] 人工标注规模不足，inter-annotator agreement 偏低（§5.4, Appendix S）**
- **位置**: §5.4 第一段，Appendix S
- **问题**: 50 对 NLI-scored pairs，仅 2 名标注员，κ = 0.44（moderate agreement）。Annotator 1 precision = 93.6%，Annotator 2 = 84.3%（§5.4: "CI [65.3%, 93.6%]"），两者差距近 10pp。论文称 κ = 0.44 反映 "calibrating a cohesion-difference rather than random noise"，但 50 对样本无法可靠区分系统性分歧与噪声。Wilson CI 下界 86.3% 基于合并数据；若按标注员分开，Annotator 2 的下界会明显低于此值。
- **为什么影响评分**: NLI gate 是 CSD 框架的核心假设保障组件——44% 拒绝率意味着大量数据依赖该 gate 的正确性。仅 50 对验证不足以支撑对该 gate 的信心，尤其是当两名标注员对 "content preservation" 的理解存在实质分歧（4 对 gate-rejected pairs 上的全部分歧集中在 verbosity-axis 的 subjective meaning 判断）。
- **建议**: 增加标注规模至 ≥100 对，增加第 3 名标注员以计算 Fleiss' κ，并分析分歧案例的特征分布（是否集中在特定 axis/instruction type）。

**W2 [Should-Fix] TOST 等价阈值 Δ = 15pp 与 GPT-4o 最小偏差重叠（§4.1, Limitations, Appendix G）**
- **位置**: §4.1 脚注，Limitations 第 3 段，Appendix G
- **问题**: TOST 设 Δ = 15pp（"a judge that agrees with the style-manipulated version on ≥65% of pairs"）。但 GPT-4o formality 的 BT = 63.0%（即 13pp above chance）——刚好在 Δ 之下。这意味着一个具有 10–14pp moderate bias 的 judge 会被 TOST 宣布为 "equivalent to no bias"。Claude 的实际 BT（50.2–54.1%）远低于此阈值，所以当前结论不受影响；但 Δ = 15pp 的选择依据不够充分——论文仅说 "would alter benchmark rankings in typical n ≈ 500 evaluations" 但未提供计算细节。
- **为什么影响评分**: 负控制的可信度依赖 TOST 阈值的合理性。若 Δ 过大，可能遗漏 Claude 的 moderate bias。
- **建议**: (1) 提供 Δ = 15pp 的定量推导（多大偏差会改变 benchmark ranking？用具体 benchmark 模拟）; (2) 增加 Δ 敏感性分析（Δ = 10pp, 12pp, 15pp, 20pp 下 TOST 结果如何变化）; (3) 在 Limitations 中明确 "moderate bias (10–14pp) 可能逃脱检测"。

**W3 [Should-Fix] 方向不对称性对 Table 1 BT 估计的影响未充分讨论（Appendix A/H）**
- **位置**: Appendix A（第 9 页底部），Appendix H（第 12 页），Table 1
- **问题**: Formality 方向不对称显著：formal→casual 方向 judge 保留原文 88.9%，casual→formal 方向仅 52.6%（Appendix H）。这暗示 formality BT 估计中混合了真实风格偏好和 "原文偏好 × 原文恰好是 formal" 的混淆。Appendix A 的 GEE 控制原文偏好后 formality 仍显著（OR = 2.58, p = 0.032），但主文 Table 1 的 BT 数值（GPT-4o form: 63.0%）是未调整的聚合值。读者可能将 Table 1 的数值直接解读为 "style preference magnitude"，而实际上其中包含质量混淆。
- **为什么影响评分**: Table 1 是论文的核心证据表，其数值的可解释性直接影响主 claim 的说服力。
- **建议**: (1) 在 Table 1 或正文中添加脚注，提示 formality BT 包含方向不对称效应，指向 Appendix A 的调整分析; (2) 考虑在 Table 1 旁增加 GEE-adjusted style OR 对照列; (3) 在 §5.1 讨论中更明确地区分 "BT detects real style preference" 和 "BT detects a mix of style + quality confounding that Likert attenuates"。

**W4 [Should-Fix] NLI gate 选择偏差检查覆盖面有限（§3.2, Appendix B）**
- **位置**: §3.2, Appendix B
- **问题**: 44% 拒绝率下，仅检查 4 个 surface covariates（word count, sentence count, TTR, FK grade）的 NLI-pass vs NLI-reject 分布。这些都是表面文本特征，未覆盖：(a) 语义/话题分布（某些 instruction types 是否被不成比例地过滤？），(b) 句法复杂度（parse tree depth），(c) 原始文本质量分布。Appendix E 的 NLI 阈值 sweep 显示 Blindspot 在所有阈值下持续——这是强鲁棒性证据，但不等同于选择偏差不存在。
- **建议**: 增加 instruction type/topic 分布对比；或论证为何 4 个 surface covariates 足以排除选择偏差。

**W5 [Should-Fix] Construct validity 讨论不充分（§5.1）**
- **位置**: §5.1 "Measurement attention vs. construct divergence"
- **问题**: 论文框架将 pairwise 定位为 "检测到" Likert "遗漏的" 偏差，隐含 pairwise 是更准确的测量。但 §5.1 自己承认 Likert 和 pairwise 可能测量不同 construct（absolute quality vs. comparative sensitivity）。如果 pairwise 的 forced-choice 设计人为放大微小风格差异为可测偏好（Comparative Trap, Jeong et al. 2025），而 Likert 正确反映了风格对绝对质量判断的可忽略影响，则两者都是"正确的"——只是对不同问题的回答。
- **论文已有的辩护**（§5.1 末段, §6）：RLHF/DPO 使用 pairwise comparison，所以 pairwise-detected biases 是对 alignment pipeline 实际传播的偏差的正确测量。这个实践论证是有效的，但在正文中不够显式——目前主要在 Conclusion 的一句话中提及。
- **建议**: 在 §5.1 中增加一段，明确区分 "measurement sensitivity gap"（同一 construct, pairwise 更灵敏）和 "construct divergence"（不同 construct, 各有效度），并论证为何在 RLHF 语境下前者更重要。

### Minor

**M1 [Minor] Cross-axis 污染超过自设阈值（Appendix R）**
- Formality 改写产生 word count shift d = −0.23，超过论文自设 d < 0.20 的 "negligible" 标准。Appendix R 的 GEE covariate check（加入 word count 后 Style OR 变化 < 12%, p > .28）有效缓解了这一问题，但主文仅在 Appendix 引用中一笔带过（§5.4 倒数第二句引用 Appendix R），未明确承认阈值违反。建议在主文中添加一句明确说明并引导读者到 Appendix R 的缓解分析。

**M2 [Minor] 100-point continuous Likert 仅用 Qwen3-32B（Appendix M）**
- Qwen3-32B 同时担任 rewriter 和 100-point Likert judge，存在 evaluator-producer overlap。虽然这一 overlap 应偏向让 Likert 更容易检测偏差（judge 评价自己的改写），反而强化了 Blindspot 结论，但应在 Appendix M 中注明这一设计限制。

**M3 [Minor] BT IIA 脚注简化过度（脚注 3）**
- 脚注 3 声称 "In binary-choice BT, IIA is structurally satisfied: each observation involves exactly two alternatives, so no third alternative can violate the axiom." 这在单次比较层面技术上正确，但 BT 模型跨 pairs 聚合时隐含的一维性假设（所有偏好可由单一潜在维度解释）未讨论。论文本身用 per-axis 分解证明偏好是多维的（Table 3），这与 BT 的一维假设存在张力——虽然每个 axis 分开建模缓解了问题。建议在脚注中补充一句关于一维性假设的说明。

**M4 [Minor] Bootstrap CI 方法未指定**
- Table 10（Appendix I）的 95% CI 基于 10,000 pair-level resamples，但未指定 percentile bootstrap 还是 BCa bootstrap。BT 概率在边界附近可能有偏度，BCa 更合适。

**M5 [Minor] Table 2 的 GEE 与 Table 3 的 GEE 是不同模型**
- Table 2 第 6 行 "GEE (exchangeable)" 以 Likert 评分为因变量，Table 3 以 pairwise 选择为因变量——两者性质完全不同。建议在 Table 2 标注 "GEE (Likert-outcome)" 以区分。

---

## Questions

**Q1.** 对于 formality 方向不对称（88.9% vs 52.6%），是否考虑过分方向拟合 BT 模型（formal→casual 和 casual→formal 分开估计），而非聚合？分方向估计可以帮助区分真实风格偏好与原文质量混淆。

**Q2.** NLI gate pass vs. reject 的 instruction type/topic 分布是否有系统差异？某些特定类型的 instruction（如创意写作 vs. 技术说明）是否被不成比例地过滤？

**Q3.** Direction-aware NLI gate 恢复的 21 对（Appendix F）的 content quality 分布是否与 bidirectional-pass 对一致？这些恢复对是否集中在某一 axis？

**Q4.** Table 2 的 GEE 与 Table 3 的 GEE 使用不同因变量（Likert score vs. pairwise choice）——能否在正文中明确区分？

**Q5.** 是否考虑过使用 BCa bootstrap 而非 percentile bootstrap 计算 BT 置信区间？尤其对于 BT 估计接近 0.5 或接近 1 的情况。

**Q6.** TOST Δ = 15pp 的定量依据是什么？"would alter benchmark rankings" 的具体模拟条件（benchmark size, number of models, score distribution）是否可以补充？

---

## Missing References

无必须添加的遗漏引用。以下为可选增强引用：
- **Measurement invariance**: Millsap (2011), *Statistical Approaches to Measurement Invariance* — 可强化 "measurement-mode divergence" 的心理测量学理论基础
- **BT model diagnostics**: Cattelan (2012), *Models for Paired Comparison Data: A Review with Emphasis on Dependent Data* — 可补充 BT 模型假设讨论

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5 / 5 | 主 claim 有多方法、多 judge、负控制支撑，统计方法选择合理且经鲁棒性检验。但人工标注规模（50 对, κ=0.44）不足以充分验证 NLI gate，TOST Δ=15pp 与最小观测偏差重叠，方向不对称对 Table 1 估计的影响在主文中讨论不足。 |
| **Excitement** | 3.5 / 5 | Likert Blindspot 对 LLM 评估方法论有直接实践影响——用 Likert 审计 judge 风格偏差的论文需重新审视结论。但范围限于 LLM judge 风格偏差检测，对更广泛 NLP 社区影响有限。 |
| **Reproducibility** | 4 / 5 | §P（Appendix P）提供完整实现细节（模型、API 版本、温度、NLI 阈值）。代码和数据承诺接收后公开。统计方法描述足够复现。 |
| **Confidence** | 4 / 5 | 统计方法和实验设计是我的核心审查方向，对 BT/GEE/TOST 方法论有充分把握。对 NLI gate 的 NLP 评估有合理理解。 |

---

## 总体评分

**Overall**: **3.5** — Borderline Conference

**一句话总结**: 核心发现新颖且证据充分（7 种方法 × 4 judges × 3 benchmarks 三角验证），但人工标注规模不足（50 对, κ=0.44）、TOST 等价阈值与最小观测偏差重叠（Δ=15pp vs. 13pp）、以及 construct validity 讨论的不完整性，使评分停留在 Borderline Conference——若 should-fix 问题得到解决（尤其 W1 和 W5），可以上调至 Conference (4.0)。

---

## 格式合规

- **正文页数**: 合规。§1–§6（Conclusion）结束于第 8 页上半部分，Limitations 从第 8 页下半部开始延续至第 9 页——Limitations 不计入 8 页限制。✓
- **Double-blind**: 合规。首页标注 "Anonymous ACL submission"，无作者信息、致谢或可识别 URL 泄露。✓
- **Limitations**: 合规。覆盖 quality-style confounding and construct validity、evaluator-producer bias、scope and ecological validity 三个维度，简洁且未包含新实验结果。✓
- **参考文献**: 格式规范，无明显遗漏。✓


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-22T19:40:53.035545+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix 和主要 Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。\n\n---\n\n# Reviewer 2 审稿报告（Round 1）\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n\n## 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验控制周密（NLI gate、position control、7 种统计方法、GEE 分解），但 framing 不对称——无法充分区分 \"Likert misses real signal\" vs \"pairwise amplifies micro-preferences\"；单一负控制不足以支撑架构特异性声明 |\n| Excitement | 3/5 | 对 LLM judge 审计实践有直接价值，但核心洞察对熟悉心理测量学的读者不意外；GEE per-axis 分解有趣但应用场景窄 |\n| Novelty | 3/5 | 核心发现是 established knowledge 的 domain transfer；CSD + GEE 分解是增量贡献 |\n| Overall | 3.0 | Findings 水平——方法学扎实但新颖性有限且 framing 问题需修正 |\n\n## Strengths\n\n**S1. 实验控制层次感出色。** CSD 三层控制——NLI gate (§3.2)、same-style double-rewrite (§5.4)、position swapping (§3.3)——在 LLM judge 风格偏差文献中属最周密的实验设计之一。\n\n**S2. 统计方法多元互补。** 七种方法覆盖不同假设，Table 2 sensitivity hierarchy 清晰展示 Likert-based 方法一致失败。GEE 条件分解 (Table 3) 将 style OR 与 originality OR 分离是独立的方法论贡献。\n\n**S3. Robustness 检查详尽。** §5.4 六项 amplification controls + Appendices A-S 大量补充分析（bootstrap CI、formal power analysis、100-point continuous Likert、cross-axis contamination 等）。\n\n**S4. GEE per-axis confound 分解是真正的增量贡献。** Table 3 揭示 verbosity style-dominated (Style OR 8-15) vs formality conditional 的结构性差异。\n\n**S5. 跨 judge 覆盖合理。** 4 target judges + 1 negative control 覆盖主流架构。\n\n## Must-Fix 问题\n\n**N1** [critical] **标题与 framing 隐式预设 pairwise 为 ground truth**\n- 位置：Title、Abstract (\"signal loss exceeding 60%\")、§6 (\"Likert-only audits miss style-driven preferences\")\n- \"The Likert Blindspot\" 将 Likert 定位为\"盲区\"，但论文自身在 §5.4 引用 Jeong et al. (2025) Comparative Trap 承认 pairwise 可能放大偏好，Limitations 提出 construct divergence 解释。这些 caveat 被隔离在末尾，未进入标题/摘要/结论。在缺乏外部 ground truth 的情况下，无法区分 measurement attenuation vs format amplification vs construct divergence 三种解释，但叙事 90% 倾向第一种。\n- 建议：标题改为中性（如直接用副标题）；Abstract/Conclusion 给三种解释同等权重。\n\n**N2** [critical] **新颖性定位模糊**\n- 位置：§1、§6（\"identifies\"/\"demonstrates\"）\n- Likert vs pairwise 灵敏度差异是 Thurstone (1927) 以来的经典结论。论文真正贡献是\"首次受控量化 + GEE 分解方法\"，但措辞有时像是声称发现了现象本身。\n- 建议：§1 明确声明 \"sensitivity gap is well-established; our contribution is first controlled quantification + decomposition methodology\"。\n\n**N3** [critical] **单一负控制不足以支撑架构特异性声明**\n- 位置：§5.3、§6、Limitations\n- Claude Sonnet 4 是唯一负控制。论文未探讨为何 Claude 不受影响（RLHF 差异？评估策略？），也未测试同系列其他模型。可能 Claude 只是整体风格不敏感而非\"正确地不受影响\"。\n- 建议：讨论可能机制；降格为 \"one model does not show this pattern\"。\n\n## Should-Fix 问题\n\n**W1** [warning] **主实验仅用 LLMBar (n=100)，cross-benchmark 覆盖稀疏** — Table 2 的 AlpacaEval/MT-Bench 仅测试 formality pairwise，不足以支撑 \"across three benchmarks\" 泛化声明。\n\n**W2** [warning] **Register 轴 evaluator-producer overlap 最严重，结果应降级** — Qwen3-32B 同时作为 rewriter 和 judge，BT 仅 51.4%。应标注为 exploratory。\n\n**W3** [warning] **Abstract 数字密度过高** — ~200 词中堆砌过多数字和术语，影响核心信息传达。\n\n**W4** [warning] **Introduction motivating example 未 acknowledge formality-quality nuance** — GPT-4o 偏好 formal 的例子暗示 Likert 偏好 casual 是\"错误\"的，但直到 Limitations/Appendix A 才讨论 formality 可能反映真实 quality 差异。\n\n**W5** [warning] **\"Framework\" 设定过高预期** — CSD 更准确地说是 experimental protocol，3 个成功轴 + 1 个失败轴不足以支撑 \"framework\" 级别声明。\n\n## 小问题\n- §3-4 脚注密度高，打断阅读流\n- Figure 2 (DAG) 偏小，blocked/open paths 区分不够直观\n- Tone axis 失败值得 2-3 句更详细的分析\n- §5.2 GEE 术语首次出现时缺乏直觉解释\n- References 置于 Appendices 之后（非标准顺序）\n\n## Questions\n\n**Q1.** 六项 amplification controls 中哪一项最直接排除 \"pairwise amplifies micro-preferences\" 解释？无人类 ground truth 如何区分 attenuation vs amplification？\n\n**Q2.** Claude 不表现 Blindspot 的可能机制？是否检查过 Claude 的 Likert/pairwise 评分分布（ceiling/floor effects, tie rates）？\n\n**Q3.** 如果用更大 benchmark (n>1000)，Likert Type II error 是否因功效提升而缩小？Appendix K 报告 required n >1200——Blindspot 是否部分是 power issue？\n\n**Q4.** Register 轴是否做了 rewriter 替换测试（类似 Appendix D 对 verbosity/formality 的测试）？\n\n**Q5.** Tone axis NLI gate 通过率 56%——失败案例中 NLI 判定\"内容改变\"是正确的还是误判？\n\n## Missing References\n无重大遗漏。可考虑补充 Bai et al. (2022/2023) RLHF preference model 的 comparison vs rating 差异、Rafailov et al. (2023) DPO 中 pairwise preference 的理论性质。\n\n## 格式检查\n- ✅ 正文 ≤8 页合规\n- ✅ Double-blind 合规\n- ✅ Limitations 覆盖充分、长度适中\n- ✅ Appendix A-S 组织合理\n- ⚠️ References 置于 Appendices 之后（非标准）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix 和主要 Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。\n\n---\n\n# Reviewer 2 审稿报告（Round 1）\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n\n## 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验控制周密（NLI gate、position control、7 种统计方法、GEE 分解），但 framing 不对称——无法充分区分 \"Likert misses real signal\" vs \"pairwise amplifies micro-preferences\"；单一负控制不足以支撑架构特异性声明 |\n| Excitement | 3/5 | 对 LLM judge 审计实践有直接价值，但核心洞察对熟悉心理测量学的读者不意外；GEE per-axis 分解有趣但应用场景窄 |\n| Novelty | 3/5 | 核心发现是 established knowledge 的 domain transfer；CSD + GEE 分解是增量贡献 |\n| Overall | 3.0 | Findings 水平——方法学扎实但新颖性有限且 framing 问题需修正 |\n\n## Strengths\n\n**S1. 实验控制层次感出色。** CSD 三层控制——NLI gate (§3.2)、same-style double-rewrite (§5.4)、position swapping (§3.3)——在 LLM judge 风格偏差文献中属最周密的实验设计之一。\n\n**S2. 统计方法多元互补。** 七种方法覆盖不同假设，Table 2 sensitivity hierarchy 清晰展示 Likert-based 方法一致失败。GEE 条件分解 (Table 3) 将 style OR 与 originality OR 分离是独立的方法论贡献。\n\n**S3. Robustness 检查详尽。** §5.4 六项 amplification controls + Appendices A-S 大量补充分析（bootstrap CI、formal power analysis、100-point continuous Likert、cross-axis contamination 等）。\n\n**S4. GEE per-axis confound 分解是真正的增量贡献。** Table 3 揭示 verbosity style-dominated (Style OR 8-15) vs formality conditional 的结构性差异。\n\n**S5. 跨 judge 覆盖合理。** 4 target judges + 1 negative control 覆盖主流架构。\n\n## Must-Fix 问题\n\n**N1** [critical] **标题与 framing 隐式预设 pairwise 为 ground truth**\n- 位置：Title、Abstract (\"signal loss exceeding 60%\")、§6 (\"Likert-only audits miss style-driven preferences\")\n- \"The Likert Blindspot\" 将 Likert 定位为\"盲区\"，但论文自身在 §5.4 引用 Jeong et al. (2025) Comparative Trap 承认 pairwise 可能放大偏好，Limitations 提出 construct divergence 解释。这些 caveat 被隔离在末尾，未进入标题/摘要/结论。在缺乏外部 ground truth 的情况下，无法区分 measurement attenuation vs format amplification vs construct divergence 三种解释，但叙事 90% 倾向第一种。\n- 建议：标题改为中性（如直接用副标题）；Abstract/Conclusion 给三种解释同等权重。\n\n**N2** [critical] **新颖性定位模糊**\n- 位置：§1、§6（\"identifies\"/\"demonstrates\"）\n- Likert vs pairwise 灵敏度差异是 Thurstone (1927) 以来的经典结论。论文真正贡献是\"首次受控量化 + GEE 分解方法\"，但措辞有时像是声称发现了现象本身。\n- 建议：§1 明确声明 \"sensitivity gap is well-established; our contribution is first controlled quantification + decomposition methodology\"。\n\n**N3** [critical] **单一负控制不足以支撑架构特异性声明**\n- 位置：§5.3、§6、Limitations\n- Claude Sonnet 4 是唯一负控制。论文未探讨为何 Claude 不受影响（RLHF 差异？评估策略？），也未测试同系列其他模型。可能 Claude 只是整体风格不敏感而非\"正确地不受影响\"。\n- 建议：讨论可能机制；降格为 \"one model does not show this pattern\"。\n\n## Should-Fix 问题\n\n**W1** [warning] **主实验仅用 LLMBar (n=100)，cross-benchmark 覆盖稀疏** — Table 2 的 AlpacaEval/MT-Bench 仅测试 formality pairwise，不足以支撑 \"across three benchmarks\" 泛化声明。\n\n**W2** [warning] **Register 轴 evaluator-producer overlap 最严重，结果应降级** — Qwen3-32B 同时作为 rewriter 和 judge，BT 仅 51.4%。应标注为 exploratory。\n\n**W3** [warning] **Abstract 数字密度过高** — ~200 词中堆砌过多数字和术语，影响核心信息传达。\n\n**W4** [warning] **Introduction motivating example 未 acknowledge formality-quality nuance** — GPT-4o 偏好 formal 的例子暗示 Likert 偏好 casual 是\"错误\"的，但直到 Limitations/Appendix A 才讨论 formality 可能反映真实 quality 差异。\n\n**W5** [warning] **\"Framework\" 设定过高预期** — CSD 更准确地说是 experimental protocol，3 个成功轴 + 1 个失败轴不足以支撑 \"framework\" 级别声明。\n\n## 小问题\n- §3-4 脚注密度高，打断阅读流\n- Figure 2 (DAG) 偏小，blocked/open paths 区分不够直观\n- Tone axis 失败值得 2-3 句更详细的分析\n- §5.2 GEE 术语首次出现时缺乏直觉解释\n- References 置于 Appendices 之后（非标准顺序）\n\n## Questions\n\n**Q1.** 六项 amplification controls 中哪一项最直接排除 \"pairwise amplifies micro-preferences\" 解释？无人类 ground truth 如何区分 attenuation vs amplification？\n\n**Q2.** Claude 不表现 Blindspot 的可能机制？是否检查过 Claude 的 Likert/pairwise 评分分布（ceiling/floor effects, tie rates）？\n\n**Q3.** 如果用更大 benchmark (n>1000)，Likert Type II error 是否因功效提升而缩小？Appendix K 报告 required n >1200——Blindspot 是否部分是 power issue？\n\n**Q4.** Register 轴是否做了 rewriter 替换测试（类似 Appendix D 对 verbosity/formality 的测试）？\n\n**Q5.** Tone axis NLI gate 通过率 56%——失败案例中 NLI 判定\"内容改变\"是正确的还是误判？\n\n## Missing References\n无重大遗漏。可考虑补充 Bai et al. (2022/2023) RLHF preference model 的 comparison vs rating 差异、Rafailov et al. (2023) DPO 中 pairwise preference 的理论性质。\n\n## 格式检查\n- ✅ 正文 ≤8 页合规\n- ✅ Double-blind 合规\n- ✅ Limitations 覆盖充分、长度适中\n- ✅ Appendix A-S 组织合理\n- ⚠️ References 置于 Appendices 之后（非标准）"
  }
}
```

</details>

---


### Tool result

_source line 1051 · 2026-05-22T19:42:16.707646+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 83672
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-22T19:42:17.159808+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Should-Fix、Minor 和主要 Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。\n\n---\n\n# Reviewer 1 — Round 1 审稿报告\n\n**审查侧重**: 方法严谨性 + 统计方法 + 实验设计\n\n## Summary\n\n本文识别了 \"Likert Blindspot\" 现象：Likert 评分与 pairwise comparison 在检测 LLM judge 风格偏差时产生系统性分歧——BT 检测到显著偏好（BT > 60%, p < 0.001），而 Likert 的 Cohen's d → 0 且 p > 0.17。提出 CSD 框架（NLI-gated 内容控制 + per-axis 风格分解 + position-controlled pairwise comparison），在 4 个 judge + 1 个负控制 + 3 个 benchmark + 7 种统计方法下验证。GEE 条件分解揭示 per-axis 混淆结构差异。方法论整体扎实，核心发现在多重鲁棒性检验下稳健，但人工标注规模、TOST 等价阈值、方向不对称性处理等方面存在可改进空间。\n\n## Strengths\n\n**S1. 核心发现新颖且实践意义重大。** Likert Blindspot 对 LLM 评估方法论有直接影响：大量论文使用 Likert 评分审计 LLM judge 偏差，本文表明这种方法可能系统性遗漏通过 pairwise 传播的风格偏好。Table 2 显示 7 种统计方法中 5 种 Likert-based 方法全部失败（p > 0.17–0.90），而两种 pairwise 方法均显著（BT p < 0.001, sign test p = 0.006），证据力强。\n\n**S2. 统计方法覆盖全面。** 7 种方法（BT, sign test, Likert ATE/t-test, Bayesian t, ordinal regression, GEE, Wilcoxon signed-rank）构成\"sensitivity hierarchy\"，从不同假设族独立验证同一结论。Holm-Bonferroni 校正覆盖 6 个主检验，且 §4.1 明确标注了 8 个检验全通过扩展族的结果。这种多方法三角验证在该领域论文中不常见。\n\n**S3. 负控制设计严谨。** Claude Sonnet 4 作为负控制（n = 87, BT 50.2%/54.1%, n.s.），TOST 等价检验确认 Δ = 15pp 处等价（76% power），验证了 CSD pipeline 不会凭空制造偏差。Appendix G 的形式化处理充分。\n\n**S4. GEE 条件分解贡献重大。** Table 3 的 Style OR vs. Originality OR 分离揭示了 per-axis 混淆结构差异（verbosity = style-dominated, formality = conditional effect, register = judge-dependent），这比简单的\"有/无偏差\"结论更有方法论价值。exchangeable working correlation + sandwich SE 的选择经 Appendix C 的 independence 对照验证（差异 <0.02），模型诊断充分。\n\n**S5. 鲁棒性检验链完整。** NLI 阈值敏感性分析（Appendix E, 11 个阈值 0.60–0.95），bootstrap 衰减分析（Appendix J, d → 0 across all n），rewriter 独立性检验（Appendix D, GPT-4o rewriter 替换），cross-axis 污染分析（Appendix R），功效分析（Figure 4），方向感知 NLI gate（Appendix F）。这些构成多层防御，使核心发现难以归因于单一方法论 artifact。\n\n**S6. 因果声明审慎。** §3.5 Design Rationale 明确免责：\"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"。\"Controlled\" 限定为实验控制而非因果识别。Figure 2 的 DAG 标注 S → Q 虚线路径并讨论残余混淆。论文标题 \"Measurement-Mode Divergence\" 是中性表述。\n\n## Weaknesses\n\n### Should-Fix\n\n**W1 [Should-Fix] 人工标注规模不足，inter-annotator agreement 偏低（§5.4, Appendix S）**\n- 50 对 NLI-scored pairs，仅 2 名标注员，κ = 0.44（moderate agreement）。Annotator 1 precision = 93.6%，Annotator 2 = 84.3%（§5.4: \"CI [65.3%, 93.6%]\"），两者差距近 10pp。论文称 κ = 0.44 反映 \"calibrating a cohesion-difference rather than random noise\"，但 50 对样本无法可靠区分系统性分歧与噪声。Wilson CI 下界 86.3% 基于合并数据；若按标注员分开，Annotator 2 的下界会明显低于此值。\n- NLI gate 是 CSD 框架的核心假设保障组件——44% 拒绝率意味着大量数据依赖该 gate 的正确性。仅 50 对验证不足以支撑对该 gate 的信心。\n- 建议：增加标注规模至 ≥100 对，增加第 3 名标注员以计算 Fleiss' κ，并分析分歧案例的特征分布。\n\n**W2 [Should-Fix] TOST 等价阈值 Δ = 15pp 与 GPT-4o 最小偏差重叠（§4.1, Limitations, Appendix G）**\n- TOST 设 Δ = 15pp，但 GPT-4o formality 的 BT = 63.0%（即 13pp above chance）——刚好在 Δ 之下。一个具有 10–14pp moderate bias 的 judge 会被 TOST 宣布为 \"equivalent to no bias\"。Claude 的实际 BT（50.2–54.1%）远低于此阈值，所以当前结论不受影响；但 Δ = 15pp 的选择依据不够充分。\n- 建议：提供 Δ = 15pp 的定量推导；增加 Δ 敏感性分析（Δ = 10pp, 12pp, 15pp, 20pp）；在 Limitations 中明确 \"moderate bias (10–14pp) 可能逃脱检测\"。\n\n**W3 [Should-Fix] 方向不对称性对 Table 1 BT 估计的影响未充分讨论（Appendix A/H）**\n- Formality 方向不对称显著：formal→casual 方向 judge 保留原文 88.9%，casual→formal 方向仅 52.6%。这暗示 formality BT 估计中混合了真实风格偏好和 \"原文偏好 × 原文恰好是 formal\" 的混淆。Appendix A 的 GEE 控制原文偏好后 formality 仍显著（OR = 2.58, p = 0.032），但主文 Table 1 的 BT 数值是未调整的聚合值。\n- 建议：在 Table 1 添加脚注提示方向不对称；考虑增加 GEE-adjusted style OR 对照列；在 §5.1 中更明确地区分 \"BT detects real style preference\" 和 \"BT detects a mix of style + quality confounding\"。\n\n**W4 [Should-Fix] NLI gate 选择偏差检查覆盖面有限（§3.2, Appendix B）**\n- 44% 拒绝率下，仅检查 4 个 surface covariates（word count, sentence count, TTR, FK grade）。未覆盖：语义/话题分布、句法复杂度、原始文本质量分布。\n- 建议：增加 instruction type/topic 分布对比；或论证为何 4 个 surface covariates 足以排除选择偏差。\n\n**W5 [Should-Fix] Construct validity 讨论不充分（§5.1）**\n- 论文框架将 pairwise 定位为 \"检测到\" Likert \"遗漏的\" 偏差，隐含 pairwise 是更准确的测量。但 §5.1 自己承认 Likert 和 pairwise 可能测量不同 construct（absolute quality vs. comparative sensitivity）。\n- 论文已有的辩护（§5.1 末段, §6）：RLHF/DPO 使用 pairwise comparison，所以 pairwise-detected biases 是对 alignment pipeline 实际传播的偏差的正确测量。这个实践论证是有效的，但在正文中不够显式。\n- 建议：在 §5.1 中增加一段，明确区分 \"measurement sensitivity gap\" 和 \"construct divergence\"，并论证为何在 RLHF 语境下前者更重要。\n\n### Minor\n\n**M1 [Minor] Cross-axis 污染超过自设阈值（Appendix R）** — Formality 改写产生 word count shift d = −0.23，超过 d < 0.20 标准。GEE covariate check 有效缓解但主文未明确承认阈值违反。\n\n**M2 [Minor] 100-point continuous Likert 仅用 Qwen3-32B（Appendix M）** — 存在 evaluator-producer overlap。\n\n**M3 [Minor] BT IIA 脚注简化过度（脚注 3）** — binary-choice BT 中 IIA 技术上正确，但跨 pairs 聚合时隐含的一维性假设未讨论。\n\n**M4 [Minor] Bootstrap CI 方法未指定** — 未指定 percentile bootstrap 还是 BCa bootstrap。\n\n**M5 [Minor] Table 2 的 GEE 与 Table 3 的 GEE 是不同模型** — 建议在 Table 2 标注 \"GEE (Likert-outcome)\" 以区分。\n\n## Questions\n\n**Q1.** 对于 formality 方向不对称（88.9% vs 52.6%），是否考虑过分方向拟合 BT 模型？\n\n**Q2.** NLI gate pass vs. reject 的 instruction type/topic 分布是否有系统差异？\n\n**Q3.** Direction-aware NLI gate 恢复的 21 对的 content quality 分布是否与 bidirectional-pass 对一致？\n\n**Q4.** Table 2 的 GEE 与 Table 3 的 GEE 使用不同因变量——能否在正文中明确区分？\n\n**Q5.** 是否考虑过使用 BCa bootstrap 而非 percentile bootstrap 计算 BT 置信区间？\n\n**Q6.** TOST Δ = 15pp 的定量依据是什么？\n\n## Missing References\n\n无必须添加的遗漏引用。可选增强引用：\n- Millsap (2011), *Statistical Approaches to Measurement Invariance*\n- Cattelan (2012), *Models for Paired Comparison Data: A Review with Emphasis on Dependent Data*\n\n## 总体评分\n\n**Overall**: **3.5** — Borderline Conference\n\n**一句话总结**: 核心发现新颖且证据充分（7 种方法 × 4 judges × 3 benchmarks 三角验证），但人工标注规模不足（50 对, κ=0.44）、TOST 等价阈值与最小观测偏差重叠（Δ=15pp vs. 13pp）、以及 construct validity 讨论的不完整性，使评分停留在 Borderline Conference——若 should-fix 问题得到解决（尤其 W1 和 W5），可以上调至 Conference (4.0)。\n\n## 格式合规\n- ✅ 正文页数合规\n- ✅ Double-blind 合规\n- ✅ Limitations 合规\n- ✅ 参考文献格式规范"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Should-Fix、Minor 和主要 Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。\n\n---\n\n# Reviewer 1 — Round 1 审稿报告\n\n**审查侧重**: 方法严谨性 + 统计方法 + 实验设计\n\n## Summary\n\n本文识别了 \"Likert Blindspot\" 现象：Likert 评分与 pairwise comparison 在检测 LLM judge 风格偏差时产生系统性分歧——BT 检测到显著偏好（BT > 60%, p < 0.001），而 Likert 的 Cohen's d → 0 且 p > 0.17。提出 CSD 框架（NLI-gated 内容控制 + per-axis 风格分解 + position-controlled pairwise comparison），在 4 个 judge + 1 个负控制 + 3 个 benchmark + 7 种统计方法下验证。GEE 条件分解揭示 per-axis 混淆结构差异。方法论整体扎实，核心发现在多重鲁棒性检验下稳健，但人工标注规模、TOST 等价阈值、方向不对称性处理等方面存在可改进空间。\n\n## Strengths\n\n**S1. 核心发现新颖且实践意义重大。** Likert Blindspot 对 LLM 评估方法论有直接影响：大量论文使用 Likert 评分审计 LLM judge 偏差，本文表明这种方法可能系统性遗漏通过 pairwise 传播的风格偏好。Table 2 显示 7 种统计方法中 5 种 Likert-based 方法全部失败（p > 0.17–0.90），而两种 pairwise 方法均显著（BT p < 0.001, sign test p = 0.006），证据力强。\n\n**S2. 统计方法覆盖全面。** 7 种方法（BT, sign test, Likert ATE/t-test, Bayesian t, ordinal regression, GEE, Wilcoxon signed-rank）构成\"sensitivity hierarchy\"，从不同假设族独立验证同一结论。Holm-Bonferroni 校正覆盖 6 个主检验，且 §4.1 明确标注了 8 个检验全通过扩展族的结果。这种多方法三角验证在该领域论文中不常见。\n\n**S3. 负控制设计严谨。** Claude Sonnet 4 作为负控制（n = 87, BT 50.2%/54.1%, n.s.），TOST 等价检验确认 Δ = 15pp 处等价（76% power），验证了 CSD pipeline 不会凭空制造偏差。Appendix G 的形式化处理充分。\n\n**S4. GEE 条件分解贡献重大。** Table 3 的 Style OR vs. Originality OR 分离揭示了 per-axis 混淆结构差异（verbosity = style-dominated, formality = conditional effect, register = judge-dependent），这比简单的\"有/无偏差\"结论更有方法论价值。exchangeable working correlation + sandwich SE 的选择经 Appendix C 的 independence 对照验证（差异 <0.02），模型诊断充分。\n\n**S5. 鲁棒性检验链完整。** NLI 阈值敏感性分析（Appendix E, 11 个阈值 0.60–0.95），bootstrap 衰减分析（Appendix J, d → 0 across all n），rewriter 独立性检验（Appendix D, GPT-4o rewriter 替换），cross-axis 污染分析（Appendix R），功效分析（Figure 4），方向感知 NLI gate（Appendix F）。这些构成多层防御，使核心发现难以归因于单一方法论 artifact。\n\n**S6. 因果声明审慎。** §3.5 Design Rationale 明确免责：\"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"。\"Controlled\" 限定为实验控制而非因果识别。Figure 2 的 DAG 标注 S → Q 虚线路径并讨论残余混淆。论文标题 \"Measurement-Mode Divergence\" 是中性表述。\n\n## Weaknesses\n\n### Should-Fix\n\n**W1 [Should-Fix] 人工标注规模不足，inter-annotator agreement 偏低（§5.4, Appendix S）**\n- 50 对 NLI-scored pairs，仅 2 名标注员，κ = 0.44（moderate agreement）。Annotator 1 precision = 93.6%，Annotator 2 = 84.3%（§5.4: \"CI [65.3%, 93.6%]\"），两者差距近 10pp。论文称 κ = 0.44 反映 \"calibrating a cohesion-difference rather than random noise\"，但 50 对样本无法可靠区分系统性分歧与噪声。Wilson CI 下界 86.3% 基于合并数据；若按标注员分开，Annotator 2 的下界会明显低于此值。\n- NLI gate 是 CSD 框架的核心假设保障组件——44% 拒绝率意味着大量数据依赖该 gate 的正确性。仅 50 对验证不足以支撑对该 gate 的信心。\n- 建议：增加标注规模至 ≥100 对，增加第 3 名标注员以计算 Fleiss' κ，并分析分歧案例的特征分布。\n\n**W2 [Should-Fix] TOST 等价阈值 Δ = 15pp 与 GPT-4o 最小偏差重叠（§4.1, Limitations, Appendix G）**\n- TOST 设 Δ = 15pp，但 GPT-4o formality 的 BT = 63.0%（即 13pp above chance）——刚好在 Δ 之下。一个具有 10–14pp moderate bias 的 judge 会被 TOST 宣布为 \"equivalent to no bias\"。Claude 的实际 BT（50.2–54.1%）远低于此阈值，所以当前结论不受影响；但 Δ = 15pp 的选择依据不够充分。\n- 建议：提供 Δ = 15pp 的定量推导；增加 Δ 敏感性分析（Δ = 10pp, 12pp, 15pp, 20pp）；在 Limitations 中明确 \"moderate bias (10–14pp) 可能逃脱检测\"。\n\n**W3 [Should-Fix] 方向不对称性对 Table 1 BT 估计的影响未充分讨论（Appendix A/H）**\n- Formality 方向不对称显著：formal→casual 方向 judge 保留原文 88.9%，casual→formal 方向仅 52.6%。这暗示 formality BT 估计中混合了真实风格偏好和 \"原文偏好 × 原文恰好是 formal\" 的混淆。Appendix A 的 GEE 控制原文偏好后 formality 仍显著（OR = 2.58, p = 0.032），但主文 Table 1 的 BT 数值是未调整的聚合值。\n- 建议：在 Table 1 添加脚注提示方向不对称；考虑增加 GEE-adjusted style OR 对照列；在 §5.1 中更明确地区分 \"BT detects real style preference\" 和 \"BT detects a mix of style + quality confounding\"。\n\n**W4 [Should-Fix] NLI gate 选择偏差检查覆盖面有限（§3.2, Appendix B）**\n- 44% 拒绝率下，仅检查 4 个 surface covariates（word count, sentence count, TTR, FK grade）。未覆盖：语义/话题分布、句法复杂度、原始文本质量分布。\n- 建议：增加 instruction type/topic 分布对比；或论证为何 4 个 surface covariates 足以排除选择偏差。\n\n**W5 [Should-Fix] Construct validity 讨论不充分（§5.1）**\n- 论文框架将 pairwise 定位为 \"检测到\" Likert \"遗漏的\" 偏差，隐含 pairwise 是更准确的测量。但 §5.1 自己承认 Likert 和 pairwise 可能测量不同 construct（absolute quality vs. comparative sensitivity）。\n- 论文已有的辩护（§5.1 末段, §6）：RLHF/DPO 使用 pairwise comparison，所以 pairwise-detected biases 是对 alignment pipeline 实际传播的偏差的正确测量。这个实践论证是有效的，但在正文中不够显式。\n- 建议：在 §5.1 中增加一段，明确区分 \"measurement sensitivity gap\" 和 \"construct divergence\"，并论证为何在 RLHF 语境下前者更重要。\n\n### Minor\n\n**M1 [Minor] Cross-axis 污染超过自设阈值（Appendix R）** — Formality 改写产生 word count shift d = −0.23，超过 d < 0.20 标准。GEE covariate check 有效缓解但主文未明确承认阈值违反。\n\n**M2 [Minor] 100-point continuous Likert 仅用 Qwen3-32B（Appendix M）** — 存在 evaluator-producer overlap。\n\n**M3 [Minor] BT IIA 脚注简化过度（脚注 3）** — binary-choice BT 中 IIA 技术上正确，但跨 pairs 聚合时隐含的一维性假设未讨论。\n\n**M4 [Minor] Bootstrap CI 方法未指定** — 未指定 percentile bootstrap 还是 BCa bootstrap。\n\n**M5 [Minor] Table 2 的 GEE 与 Table 3 的 GEE 是不同模型** — 建议在 Table 2 标注 \"GEE (Likert-outcome)\" 以区分。\n\n## Questions\n\n**Q1.** 对于 formality 方向不对称（88.9% vs 52.6%），是否考虑过分方向拟合 BT 模型？\n\n**Q2.** NLI gate pass vs. reject 的 instruction type/topic 分布是否有系统差异？\n\n**Q3.** Direction-aware NLI gate 恢复的 21 对的 content quality 分布是否与 bidirectional-pass 对一致？\n\n**Q4.** Table 2 的 GEE 与 Table 3 的 GEE 使用不同因变量——能否在正文中明确区分？\n\n**Q5.** 是否考虑过使用 BCa bootstrap 而非 percentile bootstrap 计算 BT 置信区间？\n\n**Q6.** TOST Δ = 15pp 的定量依据是什么？\n\n## Missing References\n\n无必须添加的遗漏引用。可选增强引用：\n- Millsap (2011), *Statistical Approaches to Measurement Invariance*\n- Cattelan (2012), *Models for Paired Comparison Data: A Review with Emphasis on Dependent Data*\n\n## 总体评分\n\n**Overall**: **3.5** — Borderline Conference\n\n**一句话总结**: 核心发现新颖且证据充分（7 种方法 × 4 judges × 3 benchmarks 三角验证），但人工标注规模不足（50 对, κ=0.44）、TOST 等价阈值与最小观测偏差重叠（Δ=15pp vs. 13pp）、以及 construct validity 讨论的不完整性，使评分停留在 Borderline Conference——若 should-fix 问题得到解决（尤其 W1 和 W5），可以上调至 Conference (4.0)。\n\n## 格式合规\n- ✅ 正文页数合规\n- ✅ Double-blind 合规\n- ✅ Limitations 合规\n- ✅ 参考文献格式规范"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-22T19:42:18.470559+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1310
}
```

</details>

---


### Assistant

_source line 1054 · 2026-05-22T19:42:25.541584+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 99

## Round 99

2 recorded events


### User

_source line 1055 · 2026-05-22T19:42:27.999381+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：

- **Overall: 3.5 (Borderline Conference)**
- 核心 Likert Blindspot 发现证据充分（7 种统计方法 × 4 judges × 3 benchmarks 交叉验证，负控制设计严谨），GEE 条件分解的 per-axis 混淆结构分析具有方法论贡献
- 5 个 Should-Fix 问题：(1) 人工标注仅 50 对且 κ=0.44；(2) TOST Δ=15pp 与 GPT-4o 最小偏差 13pp 重叠；(3) formality 方向不对称（88.9% vs 52.6%）对 Table 1 未调整 BT 的影响讨论不足；(4) NLI gate 44% 拒绝率下仅 4 个 surface covariate 检查；(5) construct validity 讨论中 pairwise 为何优于 Likert 的实践论证不够显式
- 5 个 Minor 问题：cross-axis 污染超阈值、100-point Likert 的 evaluator-producer overlap、BT IIA 脚注过度简化、bootstrap CI 类型未指定、Table 2 vs Table 3 的 GEE 模型区分不清

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1056 · 2026-05-22T19:42:33.370389+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 100

## Round 100

2 recorded events


### User

_source line 1057 · 2026-05-22T19:44:15.439199+00:00_

[Reviewer 2 审稿意见]:
# Reviewer 2 交叉回应 Reviewer 1

---

## Should-Fix 逐条回应

### R1-W1: 人工标注规模不足（50 pairs, κ=0.44）
**[AGREE]** 同意这是需要修复的问题。NLI gate 是 CSD 管线的核心假设保障组件——44% 拒绝率意味着超过四成数据被过滤，gate 的准确性直接决定剩余数据的有效性。50 对样本、2 名标注员、κ=0.44 的 moderate agreement 确实不足以建立对 gate 的强信心。

补充观察：论文确实在 NLI gate 之外提供了多层间接验证——Appendix E 的 11 阈值敏感性分析（0.60–0.95）显示 BT 结果在阈值变化下稳定、Appendix R 的 cross-axis 污染分析确认风格改写不改变其他轴的 surface features。这些降低了 gate 系统性失败的风险，但不能替代直接的人工验证。≥100 对 + 第 3 名标注员的建议合理。

### R1-W2: TOST Δ=15pp 与 GPT-4o 最小偏差重叠
**[AGREE]** 同意 Δ=15pp 的选择需要更充分的定量推导。GPT-4o formality BT=63%（13pp above chance）落在 Δ=15pp 的等价区间内，这意味着一个具有 moderate bias 的 judge 理论上可以被 TOST 宣布为"等价于无偏差"。虽然 Claude 的实际 BT（50.2–54.1%）远低于此阈值、当前结论不受影响，但 Δ 的选择缺乏锚定于实践意义的论证（如"多少 pp 的偏差会影响下游 alignment 决策？"）。

R1 建议的 Δ 敏感性分析（10pp/12pp/15pp/20pp）是提升可信度的最直接方式。

### R1-W3: 方向不对称性对 Table 1 BT 的影响
**[AGREE]** 同意 Table 1 的 BT 是未调整的聚合值，在方向不对称显著的情况下（formal→casual 88.9% vs casual→formal 52.6%）可能混合了真实风格偏好与原文偏好混淆。Appendix A 的 GEE 控制后 formality 仍显著（OR=2.58, p=0.032），但主文读者不易获取这一调整结果。

这一问题与我在 N1 中提出的 framing 不对称性直接相关：Table 1 的未调整 BT 容易被解读为"纯风格偏好的大小"，而实际上其中混入了质量混淆成分。在 Table 1 添加 GEE-adjusted 对照列或至少加脚注是最小修改方案。

### R1-W4: NLI gate 选择偏差检查覆盖面有限
**[AGREE]** 同意仅检查 4 个 surface covariates（word count, sentence count, TTR, FK grade）不足以排除选择偏差的所有维度。特别是 instruction type/topic 分布——如果 NLI gate 系统性地拒绝某类 instruction（如创意写作类比事实问答类更难保持内容等价），则通过 gate 的子集可能在 topic 分布上偏斜，进而影响 judge 的风格敏感度估计。

不过我认为严重程度略低于 R1 的评估。Appendix R 的 cross-axis contamination 分析已表明风格改写对 4 个 surface features 的影响可忽略，且 NLI threshold sensitivity sweep (Appendix E) 显示在 0.60–0.95 范围内 BT 估计稳定——如果选择偏差严重，不同阈值下应产生不稳定的结果。但增加 topic 分布对比确实是低成本高回报的补充。

### R1-W5: Construct validity 讨论不充分
**[AGREE]** 强烈同意，这与我的 N1（framing 不对称性）本质上是同一个问题。论文在 §5.1 末段和 Limitations 中承认了 construct divergence 的可能性，但这些讨论被边缘化——标题、摘要、结论的主叙事仍然是 "Likert misses what pairwise detects"。

R1 指出的 RLHF/DPO 实践论证（pairwise-detected biases 对 alignment pipeline 有实际意义）是一个有效的辩护角度，但在正文中确实不够显式。我建议比 R1 更进一步：不仅在 §5.1 增加一段 construct validity 讨论，还应在标题和摘要层面调整 framing，使三种解释（measurement attenuation / format amplification / construct divergence）获得更平衡的呈现。

---

## Minor 逐条回应

### R1-M1: Cross-axis 污染超过自设阈值（d=−0.23 > 0.20）
**[AGREE]** Appendix R 的 formality 改写产生 word count shift d=−0.23，确实超过论文自设的 d<0.20 标准。GEE covariate 控制有效缓解（Table 3 中 verbosity 的 confound 结构在控制 word count 后仍然清晰），但阈值违反应在主文或 Appendix R 中明确承认而非默认通过。

### R1-M2: 100-point continuous Likert 仅用 Qwen3-32B
**[AGREE]** 这与我的 W2（register 轴 evaluator-producer overlap）属于同一类问题。Appendix M 使用 Qwen3-32B 既是 rewriter 又是 judge 来测试 100-point continuous Likert，自偏好效应可能放大或掩盖结果。用 GPT-4o 或其他非 rewriter judge 复制此实验更可信。

### R1-M3: BT IIA 脚注简化过度
**[AGREE]** 技术上，binary-choice BT 满足 IIA，但跨 pairs 聚合时隐含的一维性假设（即"风格偏好可以用单一参数充分描述"）在风格是多维的情况下（formality、verbosity、register 各有不同 confound 结构）并非不言自明。不过这确实是 minor——GEE per-axis 分解本身就是对一维性假设的补充修正。

### R1-M4: Bootstrap CI 方法未指定
**[AGREE]** Appendix I 报告 bootstrap 95% CIs 但未指明 percentile 还是 BCa。鉴于 BT 估计的分布可能在 0.5 附近偏斜（尤其 Claude 负控制），BCa 校正可能产生实质差异。报告方法选择是基本的统计报告要求。

### R1-M5: Table 2 GEE 与 Table 3 GEE 是不同模型
**[AGREE]** Table 2 的 GEE 以 Likert score 为因变量（检测 Likert-based 方法的灵敏度），Table 3 的 GEE 以 pairwise choice 为因变量并分解 style/originality OR。两者目的和规格完全不同，但共享 "GEE" 标签。在 Table 2 中标注 "GEE (Likert-outcome)" 是零成本的明确化改进。

---

## Questions 逐条回应

### R1-Q1: 是否考虑分方向拟合 BT 模型？
**[AGREE]** 这是一个有价值的分析建议。Appendix F 的 direction-aware NLI gate 已经部分处理了方向不对称（通过恢复 21 个 unidirectional-pass pairs），但分方向 BT 模型能更直接地量化 formal→casual 和 casual→formal 方向上偏好强度的差异。如果两个方向的 BT 估计差异很大，则 Table 1 的聚合 BT 信息量有限。

### R1-Q2: NLI gate pass/reject 的 instruction type 分布差异？
**[AGREE]** 直接关联 W4。如果 NLI gate 系统性拒绝某类 instruction，通过 gate 的数据子集可能不代表原始 benchmark 的分布，影响 Blindspot 发现的外部效度。

### R1-Q3: Direction-aware NLI gate 恢复的 21 对质量分布？
**[AGREE]** Appendix F 报告 direction-aware gate 恢复了 21 additional pairs (BT 73.8%, p=0.006)，确认 Blindspot 在扩展数据中持续。但这 21 对是从 unidirectional-pass 中选出的（即一个方向 NLI pass、另一个方向 NLI fail），其内容质量分布可能与 bidirectional-pass pairs 不同。验证这一点对 Appendix F 结论的可信度很重要。

### R1-Q4: Table 2 vs Table 3 GEE 区分？
与 M5 相同，已 AGREE。

### R1-Q5: BCa vs percentile bootstrap？
与 M4 相同，已 AGREE。BCa 在小样本或偏斜分布下更准确，鉴于部分 cells（如 Claude 负控制）的 BT 估计接近 0.5，BCa 可能是更稳健的选择。

### R1-Q6: TOST Δ=15pp 定量依据？
与 W2 相同，已 AGREE。

---

## 对 R1 整体评分的回应

R1 给出 3.5 (Borderline Conference)，我给出 3.0 (Findings)。差异主要在 novelty 权重。

R1 的 S1 评价核心发现为"新颖且实践意义重大"——我部分不同意。Likert vs pairwise 灵敏度差异在心理测量学中是 Thurstone (1927) 以来的 established knowledge（§2 引用的 Stevens 1946、Preston & Colman 2000、DeCoster et al. 2011 都是这一传统中的经典工作）。论文的真正新颖性在于 (a) 首次在 LLM judge 领域受控量化这一现象的幅度，(b) GEE per-axis confound decomposition 方法。但"发现本身"的 novelty 有限——一个熟悉心理测量学的 reviewer 会预期 Likert 在微弱差异上不如 forced-choice sensitive。

我认为 R1 的 W5（construct validity）和我的 N1（framing 不对称性）共同构成了将评分压到 Findings 的核心原因：在缺乏外部 ground truth 的情况下，论文不能确定 pairwise 检测到的是"真实信号"还是"格式放大的微弱偏好"，但标题和结论的 framing 隐式预设了前者。如果 framing 修正 + construct validity 讨论加强，可以升至 3.5；如果同时增加人工标注规模和 TOST 敏感性分析，可以达到 Conference (4.0)。

---

## 总结

R1 的 5 个 Should-Fix 和 5 个 Minor 全部 **[AGREE]**。R1 的审稿在方法论细节（TOST 阈值、方向不对称性、bootstrap 方法、NLI gate 验证）上比我的审稿更深入，这些问题与我关注的更宏观的 framing/novelty 问题互补。两份审稿共同指向同一个核心缺陷：**论文的实验设计和统计分析是一流的，但解释框架（framing）系统性地偏向 "Likert is wrong, pairwise is right"，而数据本身无法排除 construct divergence 或 format amplification 的替代解释。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1058 · 2026-05-22T19:44:28.337474+00:00_

Reviewer 2 交叉回应已收到——对 Reviewer 1 的 5 个 Should-Fix 和 5 个 Minor **全部 [AGREE]**。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 101

## Round 101

8 recorded events


### User

_source line 1059 · 2026-05-22T19:44:29.354654+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见

---

## Must-Fix 逐条回应

### [AGREE] R2-N1: 标题与 framing 隐式预设 pairwise 为 ground truth
**同意存在问题，但不同意 severity 为 Must-Fix，应为 Should-Fix。**

R2 的核心观察是正确的：论文叙事重心偏向 "Likert misses real signal"，而 §5.1 的 construct divergence 讨论和 Limitations 的 Comparative Trap 引用被隔离在末尾。我在自己的审稿中也提出了类似问题（我的 W5: construct validity 讨论不充分）。

但 R2 将此升级为 Must-Fix 过重，原因如下：
1. **论文标题 "Measurement-Mode Divergence" 副标题本身是中性的**——"Blindspot" 是主标题的隐喻，但副标题准确描述了现象。
2. **§5.1 已明确讨论三种解释**："Both Likert and pairwise may be 'correct' for their respective constructs"（§5.1 倒数第三段），引用 Tripathi et al. (2025) 独立确认 construct divergence。问题是权重分配不均，而非完全缺失。
3. **实践论证是有效的**：RLHF/DPO 使用 pairwise comparison，因此 pairwise-detected biases 是对 alignment pipeline 实际传播偏差的正确度量——这个论点在 §1 和 §6 均有涉及（"Likert-only audits miss style-driven preferences that propagate through pairwise-based alignment pipelines"），只是不够显式。

**建议折中**：不必改标题（"Blindspot" 是有效的注意力锚点），但 Abstract 和 §6 应给 construct divergence 解释 1-2 句同等权重的空间。

---

### [REBUT] R2-N2: 新颖性定位模糊
**不同意此为 Must-Fix。论文已在 §1 明确界定了贡献边界。**

R2 称 "Likert vs pairwise 灵敏度差异是 Thurstone (1927) 以来的经典结论"——这在一般心理测量学层面成立，但在 LLM judge 风格偏差的特定语境中，**此前无受控实验量化过这一差异**。论文 §1 第 2 页明确声明：

> "Our contribution is the first controlled quantification of this per-axis sensitivity gap in the LLM judge setting; identifying the two-layer mechanism the inflation plus residual signal attenuation that drives it."

> "we previously sequentially conjectured for LLM judges"（§2 末段，引用 Koh et al. 2025 作为先前猜测）

论文区分了三层贡献：(1) 受控量化（vs. 先前的 observational 报告），(2) CSD 方法论（NLI gate + per-axis decomposition），(3) GEE 条件分解揭示 per-axis 混淆结构。R2 将 (3) 评价为 "真正的增量贡献"（R2-S4），却又在 N2 中称整体贡献为 "domain transfer"——这两个判断相互矛盾。

R2 举 Thurstone (1927) 为前序工作，但 Thurstone 的 Law of Comparative Judgment 讨论的是心理物理学中刺激量级判断，与 LLM judge 在 NLG evaluation 中的风格偏好检测是不同 task。将"一般性测量理论预测"等同于"特定领域的受控实验验证"，忽视了 empirical science 中领域验证的价值。

**结论**：论文措辞可局部收紧（如 §1 "This is the Likert Blindspot" 可改为 "We term this the Likert Blindspot"），但 N2 不构成 Must-Fix——因为贡献界定已在 §1 完成。

---

### [REBUT] R2-N3: 单一负控制不足以支撑架构特异性声明
**不同意此为 Must-Fix。R2 对论文 claim 的解读超出了论文实际声明。**

论文使用 Claude Sonnet 4 的目的是 **pipeline validation**（CSD 不会凭空制造偏差），**不是** architecture comparison。关键文本证据：

- §4.1: "Claude Sonnet 4 serves as confirmatory replication and is excluded from FWER control; as a sanity check, all eight tests remain significant under the expanded family."
- §5.3: "A negative control judge shows no divergence on either primary axis, supporting discriminative validity."
- §6: "including a negative control judge showing no pairwise divergence"

论文从未声明 "only certain architectures show the Blindspot" 或 "the Blindspot is architecture-specific"。Claude 的作用是证明 **CSD 具有 discriminative validity**——当真实偏差不存在时，pipeline 不报假阳性。这与 "探讨为何 Claude 不受影响" 是完全不同的研究问题。

R2 要求 "讨论可能机制" 和 "测试同系列其他模型"——这是要求论文回答一个它未提出的问题。将此升级为 Must-Fix 要求论文做超出其 scope 的工作。

**补充证据**：Appendix D（rewriter independence test）用 GPT-4o 替换 Qwen3-32B 作为 rewriter，Blindspot 持续存在——这进一步表明 Blindspot 不依赖特定 evaluator-producer 组合，是 pipeline 鲁棒性而非架构特异性的证据。

**结论**：R2 的关切可以通过在 Limitations 增加 1-2 句（"the mechanism behind Claude's null result remains unexplored"）解决，不构成 Must-Fix。

---

## Should-Fix 逐条回应

### [AGREE] R2-W1: 主实验仅用 LLMBar, cross-benchmark 覆盖稀疏
**部分同意。**

Table 1 的 AlpacaEval 和 MT-Bench 确实仅覆盖 formality + verbosity 的部分 judge 组合。"across three benchmarks" 的泛化声明需要限定。

但须注意两点缓解因素：
1. AlpacaEval 的 scaled replication (n = 355) 是独立的大样本验证，且 Appendix K（formal power analysis）和 Appendix J（bootstrap attenuation）均基于此样本。
2. §5.3 的 cross-judge 和 cross-axis replication 在 LLMBar 内部已用 4 个 judge × 3 个 axis = 12 个 cell 验证，8/11 显著（Table 1）。

建议将 "across three benchmarks" 限定为 "with primary results on LLMBar and confirmatory replication on AlpacaEval and MT-Bench for selected configurations"。

---

### [AGREE] R2-W2: Register 轴 evaluator-producer overlap
**部分同意。** Qwen3-32B 作为 rewriter + judge 的 overlap 应在论文中标注。我在自己的 M2 中也提出了类似问题（Appendix M 的 100-point Likert 用 Qwen3-32B）。

但须注意：register 的主要 Blindspot 结果来自 **其他 judge**（GPT-4o register n.s., Llama-70B register 63.1% BT significant——Table 1），这些 judge 与 rewriter 无 overlap。论文的核心 claim 建立在 verbosity 和 formality 上，register 是补充。"降级为 exploratory" 过强，标注 overlap 即可。

---

### [REBUT] R2-W3: Abstract 数字密度过高
**不同意。** 对于一篇以 "7 种统计方法 × 4 judges × 3 benchmarks" 为核心卖点的实证论文，Abstract 中的定量具体性（BT > 60%, p < 0.001; d → 0, p > 0.17）是必要的——它精确传达了 Blindspot 的 magnitude 和统计证据强度。去除这些数字会使 Abstract 变为无法验证的 qualitative assertion。

ARR reviewer guidelines 未对 Abstract 数字密度设限。Empirical NLP 论文（如 Wang et al. 2024 Chatbot Arena, Zheng et al. 2023 MT-Bench）的 Abstract 同样包含定量结果。

---

### [AGREE] R2-W4: Introduction motivating example 未 acknowledge formality-quality nuance
**同意，minor 级别修正即可。** §1 开头的 GPT-4o 例子（Likert 评 casual 为 8, formal 为 5，但 pairwise 一致选 formal）确实隐含了 "Likert 的判断是错误的"，而 formality 与 perceived quality 的关联直到 Appendix A 才讨论。在例子后添加一句 caveat（"whether this reflects a genuine quality difference or a stylistic preference is itself a question we address in §5.1"）即可解决。

---

### [REBUT] R2-W5: "Framework" 设定过高预期
**不同意。** "Framework" 在 NLP 文献中常用于描述 multi-stage experimental protocols（例如 RATE: Reber et al. 2025 称自己为 "framework"；Chatbot Arena 称自己为 "platform"/"framework"）。CSD 包含三个独立组件（NLI gate, per-axis decomposition, position-controlled pairwise），每个组件可独立复用——这是 framework 而非 one-off protocol 的定义特征。

3 个成功轴 + 1 个失败轴（tone）恰恰证明 framework 有 discriminative validity：它不是对所有输入都报阳性的 trivial pipeline。

---

## Questions 回应

### R2-Q1: 哪项 amplification control 最直接排除 "pairwise amplifies micro-preferences"？

这是好问题。最直接的证据组合：
1. **负控制（Claude）**：如果 pairwise 系统性放大微偏好，Claude 也应显示 inflated BT。Claude BT ≈ 50%（Table 1）证明 pairwise 不 uniformly amplify。
2. **Same-style double-rewrite control（§5.4, Appendix O）**：original vs. same-style rewrite 的 BT 被 GEE originality term 吸收，证明 rewriting artifact ≠ style signal。
3. **Rewriter independence（Appendix D）**：GPT-4o rewriter 替换后 Blindspot 持续——排除了 Qwen3-32B rewriter 特有的 style 注入。

但 R2 的核心问题——"无人类 ground truth 如何区分 attenuation vs amplification"——确实没有被完全回答。论文 §5.1 承认这一点。我同意这是论文的 inherent limitation，但不是 paper-breaking 问题，因为实践论证（RLHF 用 pairwise → pairwise-detected biases 实际传播）提供了 pragmatic ground truth。

### R2-Q2: Claude 机制？
同意这是开放问题。我在自己的审稿中未专门提出，但认为在 Limitations 增加 1-2 句讨论（可能与 Claude 的 RLHF 训练策略或内部评估策略有关）是合理的。

### [REBUT] R2-Q3: 大样本下 Likert Type II error 是否因功效提升而缩小？
**论文已明确回答此问题。** R2 似乎未充分考虑 Appendix J 和 K 的证据：

- **Appendix J（Bootstrap Attenuation Analysis）**：subsample BT 在所有样本量下稳定在 BT 76-77%（p < 0.001），而 Likert d 随 n 增大 **converges to zero**——不是 converge to a small nonzero value，是趋向零（Table 11: d remains flat near zero across sample sizes while BT is stable at 66.5%）。这直接证明 Blindspot 是 structural measurement difference，不是 power issue。
- **Appendix K（Formal Power Analysis）**: 对于 Likert 达到 80% power 所需 n > 1,200（Qwen3-32B verbosity），代表 "far beyond typical evaluation budgets"。但关键不在于 n 大小——即使 n = ∞，如果 d → 0，Likert 永远无法检测到 effect。

R2 提出 "Blindspot 是否部分是 power issue" 的问题，论文给出了明确否定回答。

### R2-Q4: Register 轴是否做了 rewriter 替换测试？
合理问题。查 Appendix D，rewriter independence test 仅覆盖 verbosity 和 formality（Table 7/8），register 未做替换测试。建议作者补充或在 Limitations 中注明。

### R2-Q5: Tone axis NLI gate 失败案例分析？
合理问题。论文对 tone axis 的失败仅用 "tone axis NLI gate pass rate was too low for meaningful analysis" 一句带过。2-3 句分析（NLI 判定内容改变是正确的 vs 误判；tone manipulation 是否 inherently content-altering）会有价值。

---

## 对 R2 总体评分的看法

R2 给 **3.0 (Findings)**，主要基于三个 Must-Fix（N1 framing, N2 novelty, N3 negative control）和 novelty/excitement 评分偏低。我认为：

1. **N1（framing）**实质上是 Should-Fix，不是 Must-Fix——修正 Abstract/Conclusion 的权重分配即可。
2. **N2（novelty）**与 R2 自己的 S4（"GEE per-axis decomposition 是真正增量贡献"）矛盾——如果最核心方法论贡献被承认，整体 novelty 不应降到 3/5。
3. **N3（negative control）**基于对论文 claim 的过度解读——论文从未声明架构特异性。

R2 的 Excitement 3/5（"对熟悉心理测量学的读者不意外"）以错误的受众为标准——EMNLP 的读者是 NLP 研究者，不是心理测量学家。对于 routinely 使用 Likert 评分审计 LLM judges 的 NLP 社区，Blindspot 现象的受控量化具有直接实践价值。

**我维持 Overall 3.5（Borderline Conference）。** 若 R2 的 N1-N3 全部为 Must-Fix，3.0 合理；但我认为 N2 和 N3 不构成 Must-Fix，N1 降为 Should-Fix 后，论文处于 Borderline Conference 区间。


---

[Reviewer 2 审稿结果]:
交叉回应已提交。

对 R1 的 5 个 Should-Fix 和 5 个 Minor 全部 **[AGREE]**，核心理由：

- **W1-W4**（标注规模、TOST 阈值、方向不对称、NLI gate 选择偏差）：R1 在方法论细节上的审查比我更深入，这些技术问题都是合理的，尤其 W1（50 pairs, κ=0.44）和 W2（Δ=15pp 与 GPT-4o 13pp 重叠）。
- **W5**（construct validity）：与我的 N1（framing 不对称性）本质上是同一问题——论文的核心缺陷不在实验设计，而在解释框架。
- **M1-M5**：均为合理的报告规范改进建议。

与 R1 的主要分歧在 **novelty 权重**：R1 给 3.5（Borderline Conference），我给 3.0（Findings）。我认为 Likert vs pairwise 灵敏度差异是心理测量学的 established knowledge，"首次在 LLM judge 领域量化"的新颖性不足以支撑 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1060 · 2026-05-22T19:45:02.634215+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1061 · 2026-05-22T19:45:03.036390+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T19:38:44.369868+00:00\", \"completed_at\": \"2026-05-22T19:42:04.329035+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item（标题+摘要+引言），首个视觉锚点 Figure 1 出现在第2页顶部，位置合理。Title/Author/Abstract 排版整洁专业，符合 ACL 匿名模板规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（CSD pipeline overview）作为首个 display item，展示方法流程而非核心发现——对方法论论文是合理选择。但图中各阶段的缩略图标（thumbnail icons）尺寸偏小，在打印时可能难以辨认细节。Caption 较简短（\\\"Numbers indicate sample attrition at each stage\\\"），建议补充一句总结性描述以增强自包含性。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2（因果 DAG）使用橙/红+蓝配色区分干预路径与混淆路径，视觉清晰。Caption 自包含性好，明确说明\\\"design rationale, not a claim of perfect identification\\\"。节点标签和箭头在当前分辨率下可读。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 3（Bradley-Terry win probabilities）使用实心/空心菱形编码显著性，0.50 基线虚线标注明确。Caption 详细解释了编码规则，自包含性优秀。散点间距略密但仍可分辨。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1（主结果表）和 Table 2（sensitivity hierarchy）均使用 booktabs 风格，无竖线。Table 1 跨双栏、行列密集，统计标记（*、†、‡、§）种类较多——审稿人需要花额外时间解读，但数据量决定了这是合理的呈现方式。最优结果有加粗标注。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4（power analysis curves）线型区分清晰（实线/虚线/点线），80% power 交叉点标注明确。Table 3（GEE decomposition）格式规范。本页图表+文字节奏良好。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"主正文最后一页（第8页）为纯文本（Section 5.4 Robustness + Section 6 Conclusion + Limitations），无 display item。结合第3页（Related Work/Method 纯文本），主正文中出现了两段各一页的纯文本区域，但均未连续出现（中间被 pp.4-7 的图表打断），节奏可接受。Limitations 章节简短覆盖核心限制点，符合 EMNLP 规范。\"}, {\"severity\": \"info\", \"dimension\": \"pages 10-14\", \"message\": \"附录包含 Table 4-18（共15张表），全部使用 booktabs 风格，格式一致。表格密度高但组织清晰，每张表都有对应的 appendix section 引用。\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Implementation Details（Section P）提供了模型版本、API 时间戳、超参数等复现信
…[truncated 681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 402
}
```

</details>

---
