---
round: 8
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-22T09:35:39.586114+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 9 审稿报告（Fresh Review）

**论文**: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性/实验设计/统计方法论; R2: 新颖性/完整性/Related Work/写作质量）
**交叉轮次**: 1 轮（Round 1 初审 + 交叉分享 + 收敛）

---

## Summary

本文提出 Controlled Style Decomposition (CSD) 框架，结合 NLI-gated content control、per-axis style decomposition 和 position-controlled pairwise comparison，量化 LLM judge 中的风格偏差。核心发现称为"Likert Blindspot"：Likert 评分系统性地遗漏 pairwise comparison 能检测到的风格偏差——在中等效应量时完全衰减（d → 0），在较强效应时衰减 >60%。实验跨 4 个 target judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、1 个负对照（Claude Sonnet 4）、3 个 benchmark、3 个 style axis 验证。GEE conditional decomposition 揭示 per-axis confound structure：verbosity style-dominated，formality conditional，register judge-dependent。

---

## Strengths

**S1. 实验设计多维度且严谨。** 4+1 judges × 3 benchmarks × 2+1 style axes × 7 种统计方法的交叉验证矩阵在 LLM evaluation 文献中罕见。Table 2 的 sensitivity hierarchy 呈现干净的 all-or-nothing 模式：所有 pairwise 方法显著，所有 Likert 方法不显著，极具说服力。[R1-S2, R2-S1, R2-S2, AGREE]

**S2. 负对照设计有效。** Claude Sonnet 4 在相同 pairwise 设计下 BT ≈ 54-56%，TOST 确认等价性。为其他 judge 的显著偏差提供了因果对比基础——证明偏差是 judge-specific 而非 format-induced。[R1-S4, AGREE]

**S3. 因果推断框架诚实定位。** §3.5 Design Rationale 明确 DAG 是 "design rationale, not a claim of perfect identification"，三个 operational assumptions 逐一列出并在附录中提供经验验证。[R1-S3, R2 partial REBUT on Title/Abstract language]

**S4. Per-axis confound structure 是独立有价值发现。** GEE conditional decomposition 揭示 verbosity = style-dominated（Style OR 8–13）、formality = conditional on originality、register = judge-dependent。对 LLM judge 用户有直接 actionable value。[R1-S5, R2-S3, AGREE]

**S5. Robustness 分析深度罕见。** Appendix A–Q 覆盖方向非对称性、NLI consistency filter、GEE diagnostics、rewriter independence、NLI threshold sweep (11 points)、direction-aware gate validation、Claude TOST、bootstrap attenuation、BT goodness-of-fit、100-point Likert、NLI gate ablation、rewriting artifact control。几乎回答了每个合理质疑。[R1-S5, R2-S4, AGREE]

**S6. Black-box 框架设计实用性强。** CSD 不需要 judge 内部访问，可 post-hoc 应用于任何 black-box judge。[R2-S5, AGREE]

---

## Weaknesses

### Must-Fix（需在 rebuttal/revision 中解决）

**MF1. NLI gate 作为 content preservation 唯一门控缺乏人工验证** [R1-N1 critical, R2-Q1 AGREE]
- CSD 因果推断完全依赖 NLI gate (DeBERTa-v3-large, τ=0.90) 保证 content 不变，但 NLI 模型存在系统性盲区（如对论证结构重组不敏感）。论文未报告任何 human evaluation of content preservation quality。
- GPT-4o cross-validation (92.1%/82.6% pass precision) 是 LLM-vs-LLM 验证，存在认识论循环——用同类工具验证测量工具。
- 如果 NLI gate 系统性放过某些 content 变化（如 formal 改写增加 hedging 改变 claim 强度），则观测到的"style bias"可能部分是 content bias 的伪装。
- **此问题自 Round 3 起持续 7 轮未解决。** 两位 Reviewer 共同指向：增加 human evaluation 是最大可 actionable 改进（50-100 pairs × 2-3 annotators）。
- **交叉共识**: 双方完全一致。

**MF2. Novelty framing 过于强势——核心发现是已知测量理论的实证确认** [R1-N2 critical, R2-N1 critical, AGREE]
- Thurstone (1927) Law of Comparative Judgment 已建立 pairwise > Likert 的灵敏度优势。论文在 §2 引用了这些文献并承认理论预测，但 Title/Abstract/Conclusion 中的 "reveal" 措辞将此包装为新发现。
- 更准确的定位：CSD 框架首次在 LLM judge 场景下系统量化了理论预测的灵敏度差距（severity spectrum 和 per-axis confound structure 是真正新发现）。
- **交叉共识**: 双方完全一致。建议从 "reveal" 转为 "quantify"；将 per-axis confound structure 提升为并列核心贡献。此问题自 Round 1 起持续未完全修正。

### Should-Fix（重要但非致命）

**SF1. Pairwise "检测" vs. "放大" 的核心解释性歧义** [R2-N2 critical → R1 REBUT 降为 warning]
- 替代解释：pairwise comparison 可能放大微小的、无关紧要的风格微偏好，Likert 的不显著才反映真实效应。
- 论文 §5.4 提供 6 项 amplification controls（NLI gate ablation、Claude 负对照、cross-axis BT variation、GEE artifact control、debiased prompting、cross-architecture replication），Jeong et al. (2025) Comparative Trap 也在讨论之中。
- R1 反驳核心论据：Claude 负对照在相同 pairwise 设计下无偏差，证明非 format-induced 放大。
- **分歧记录**: R2 定 critical（controls 只排除大规模放大，无法排除中等程度放大），R1 定 warning（负对照已充分缓解）。Director 判定 **Should-Fix**：Conclusion 语言应更谨慎（从 "reveal" 改为条件性表述），但论文已提供了合理的 bounding analysis。

**SF2. Style axis 覆盖面过窄** [R2-W1 warning, R1 AGREE direction]
- 仅 2 primary + 1 exploratory axes。LLM judge 已知风格偏差远不止这些（bullet-point vs. prose、hedging level 等）。"Per-axis confound structure" 这一分类法基于 3 个 axis 的泛化基础不足。
- 建议：限定为 "preliminary evidence of axis-dependent confound patterns"；在 Limitations 列出未覆盖轴。

**SF3. Claude TOST Δ=15pp margin 偏宽且覆盖不完整** [R1-W3 warning, R2 implied AGREE]
- Δ=15pp 接近 GPT-4o formality 的 BT 偏差（~13pp），意味着 Claude 可能存在高达 15pp 的 style preference 仍被判"无偏差"。Claude 仅覆盖 2/3 axes（无 register）。
- 建议三选一：(a) 增加 n 使 Δ=10pp 有功效；(b) reframe 为 "insufficient evidence for bias at Δ=15pp precision"；(c) 报告 minimum detectable Δ at 80% power。

**SF4. Evaluator-producer overlap 处理力度有限** [R1-W4 warning, R2-Q3 AGREE]
- Qwen3-32B 同时做 rewriter 和 judge。Cross-rewriter 验证（GPT-4o rewriter）显示 Style OR 下降 22%，但仅限 Qwen3-32B judge 验证。效应量有 ±20-25% rewriter-dependent 变异。
- 建议：显式承认 Blindspot 存在性 robust 但效应量精确值受 rewriter 影响。

**SF5. NLI gate 44% 拒绝率的选择偏差特征分析不足** [R2-W2 warning, R1 AGREE]
- Appendix B 的 4 个 surface covariates 可能不够全面。Filtered-in pairs 可能偏向内容更简单的文本。
- 建议补充对 filtered-out pairs 的语言复杂度对比分析。

**SF6. Style axis 之间的 cross-contamination 未直接测试** [R1-W2 warning, R2 implied AGREE]
- §3.5 假设(iii)（rewrite 不引入 target axis 外的系统性变化）未被经验验证。Table 5 GEE interaction test 只检验 Style×Originality 而非 cross-axis interaction。
- 建议：对每个 axis 改写样本测量其他 axis 的变化幅度。

### Minor

**M1. 100-point Likert 实验仅用单一 judge** [R2-W3, R1 AGREE]
- Appendix M 仅 Qwen3-32B，如果 GPT-4o 在 100-point scale 下 ATE 显著则结论不成立。建议增加至少 1 个 judge。

**M2. 因果语言张力** [R2-W4, R1 partial REBUT]
- §3.5 disclaimer 已足够明确。问题仅在 Title ("Controlled") 和 Abstract 的措辞选择暗示过强因果识别。建议在 Abstract 增加一句说明 "controlled" 指 experimentally controlled rewriting 而非 formal causal identification。

---

## Reviewer Consensus [AGREE]

1. **Novelty reframing 是最优先修改**：从 "我们发现了 Blindspot" 转为 "我们首次系统量化了已知测量理论效应在 LLM judge 场景下的严重程度 + 发现了 per-axis confound structure"。[R1-N2 × R2-N1]
2. **Human evaluation 是最大可 actionable 改进**：50-100 pairs × 2-3 annotators 的 content preservation 验证能同时解决 NLI gate 可信度和 detection vs. amplification 两个问题。[R1-N1 × R2-Q1]
3. **实验设计的严谨性是主要优势**：7 种统计方法 × 4+1 judges × 3 benchmarks 的矩阵在同领域罕见。[R1-S2 × R2-S1]
4. **Per-axis confound structure 应被提升为核心贡献**。[R1 cross × R2-N1]
5. **TOST Δ=15pp 偏宽**，Claude 负对照的 framing 需更谨慎。[R1-W3 × R2 implied]

## Reviewer Divergence [分歧]

1. **检测 vs. 放大的严重程度** [R2-N2 critical vs. R1 warning]：R2 认为这是核心解释性歧义，论证存在循环性，且 6 项 controls 仅排除大规模放大；R1 反驳负对照（Claude BT ≈ 54-56%）是最强反驳证据——若 pairwise 系统性放大则所有 judge 均应受影响。R1 进一步指出论证在操作层面（alignment pipeline 确实用 pairwise）不循环。Director 判定 Should-Fix 而非 critical：Conclusion 语言应谨慎化，但论文已提供合理 bounding。

---

## Questions（需作者回应）

Q1. NLI gate 的 false-pass rate 是否有人工验证数据？即使 50 pairs 的抽样也能大幅增强可信度。
Q2. Table 1 缺失单元格代表什么？选择哪些 judge×axis×benchmark 组合的理由是什么？
Q3. Bootstrap attenuation analysis (d = −0.017) 如何排除 Likert 和 pairwise 在 construct 层面的根本差异？
Q4. Formal 改写是否系统性改变了 verbosity 或 register？是否有定量 axis isolation 证据？
Q5. 选择 formality 和 verbosity 作为 primary axes 的先验理由是什么？
Q6. 是否有办法量化 pairwise 的放大倍数（amplification factor），而非仅定性 bounding？

---

## Missing References

- Simms, Zelazny, Williams & Bernstein (2019). *Psychological Assessment* — rating scale granularity 对 discriminability 的影响
- Polo et al. (2024). tinyBenchmarks — IRT 在 LLM 评估中的应用
- Kocmi & Federmann (2023). LLM judge bias across evaluation formats
- 建议验证 Stureborg et al. (2024) 在 references.bib 中的完整性

---

## External Review (Stanford Agentic Reviewer)

未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical / 2 warning / 4 info）：

- **[warning] P16**: 末页仅 3 条 reference，约 85% 空白；建议调整分页使末页填充更充分
- **[warning] P6**: 3 个 display items（Figure 3 + Table 2 + Figure 4）挤在同一页，Figure 3/4 图幅偏小，axis label 接近可读性下限；建议将 Table 2 或 Figure 4 移至 P7 分散密度
- **[info] P1-3**: 前 3 页中仅 P2 有 1 个 display item，视觉上偏"文字墙"
- **[info] P4**: Figure 2 因果 DAG 节点标签偏小，打印后可能需凑近看
- **[info] P6**: Figure 3 的 filled/open diamond marker 尺寸较小，灰度打印时 significance 区分度可能下降
- **[info] P13**: References 与 appendix 表格过渡区略拥挤

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 3.5/5 | 4/5 | 3.5-4 |
| Excitement | 3.5/5 | 3/5 | 3-3.5 |
| Reproducibility | 4/5 | 4/5 | 4 |
| Overall | 3.5 | 3.5 | **3.5** |
| Confidence | 4/5 | 4/5 | 4 |

**总评**: 实验工作扎实、统计分析充分、robustness 覆盖深入的 evaluation 方法论工作。核心发现（Likert 对 style bias 的结构性不敏感 + per-axis confound structure）对 NLP evaluation 社区有实用价值。但两个 Must-Fix 问题阻碍更高评分：(1) NLI gate 缺乏人工验证——这是因果推断链的最薄弱环节，且已持续 7 轮未解决；(2) Novelty framing 将已知测量理论效应的实证确认包装为新发现，需要重新定位。如果 rebuttal/revision 能增加 human evaluation 数据并 reframe novelty narrative，可上调至 4.0 (Conference)。

---

## Detailed Comments

### §1 Introduction
- Motivating example ("average height") 后已有 nuance acknowledgment ("formality preferences may partially reflect legitimate quality judgments")——这是合理的处理。
- "CSD reveals the Likert Blindspot" → 建议改为 "CSD quantifies the Likert Blindspot" 或 "CSD demonstrates"

### §2 Related Work
- 覆盖全面，Jeong et al. (2025) Comparative Trap 和 Tripathi et al. (2025) 均已引用。
- 建议补充 IRT 文献（Polo et al., 2024）以加强 measurement theory 背景。

### §3 Method
- §3.2 NLI gate 描述清晰，direction-aware strategy 有理论依据。
- §3.5 Design Rationale 的因果语言校准良好（"design rationale, not a claim of perfect identification"）。但 §3.1 "constitutes a binary intervention on a single style variable" 中 "intervention" 一词与 §3.5 的谨慎定位有张力。
- Figure 2 DAG 标注了 residual confounding dashed line——诚实且有效。

### §4 Experiments
- §4.1 Statistical framework 现在明确 "six tests—three target judges × two axes" + Gemini confirmatory + Appendix Q 8-test sensitivity analysis。比之前轮次的表述有显著改善。
- Table 1 footnote "Empty cells: untested benchmark–axis combinations" 存在但未说明选择理由。

### §5 Analysis
- §5.1 Likert Blindspot 的 head-to-head comparison with RATE 是有效的对比设计。
- §5.1 measurement attenuation vs. construct divergence 的讨论已有改善（引用 Tripathi et al. 2025），但 "Blindspot" 术语天然偏向 attenuation 解释。
- §5.2 GEE conditional decomposition 结果清晰，"style-dominated" 而非 "confound-free" 是正确术语选择。
- §5.4 六项 amplification controls 是对 Comparative Trap 的系统性回应。

### §6 Conclusion
- 简洁但可能过于简短（3 句话）。建议增加 practical implication 和 caveats。

### Limitations
- 覆盖了主要局限：quality-style confounding、evaluator-producer bias、validation methodology、scale design、per-axis independence、ecological validity。
- Limitations 写得坦诚且适当长度（约 3 个点，符合 EMNLP 要求）。
- 建议补充：style axis 之间的 potential interaction；将 measurement theory 背景作为 limitation 显式列出。

### 格式合规
- ✅ ACL template (`\usepackage[review]{acl}`)
- ✅ Double-blind (`\author{Anonymous}`)
- ✅ 正文 8 页合规
- ✅ Limitations section 存在
- ✅ References 不限页
- ⚠️ P6 display item 密度过高（视觉审查 warning）
