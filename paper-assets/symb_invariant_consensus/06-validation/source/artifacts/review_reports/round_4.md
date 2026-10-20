---
round: 4
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T15:17:11.662860+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — Round 6 (Fresh)

**论文**: "Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Fail in LLM Reasoning"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Deadline**: 2026-05-25 (ARR submission) / 2026-08-02 (EMNLP commitment)
**Reviewer 配置**: R1 (方法严谨性 + 实验设计 + 统计分析) / R2 (新颖性 + 相关工作完整性 + 格式合规)
**流程**: Round 1 独立审稿 → 交叉分享 ([AGREE]/[REBUT]) → 收敛 → 汇总

---

## Summary

论文提出 SICA（Symbolic Invariant Consensus Aggregation），从 K 条 CoT traces 中提取 FOL 约束并通过 Z3 加权 partial MAX-SAT 选择答案，系统评估其在 6 个模型（7B–32B）、3 个推理域、~1,250 unique instances 上的表现。核心发现为负面结果：自提取约束无法超越 SC 多数投票。论文提出 "Symbolic Mirage" 假说解释此失败，识别三个机制（Independence-Accuracy Trade-off, Symbolic Confirmation Bias, Process-Level Homogeneity），并通过 Oracle 控制和 DeBERTa 跨架构 PoC 论证外部验证信号是突破方向。

---

## Strengths

**S1: 系统性实验设计与精巧的 Oracle 控制。** [R1-S1/S2/S3, R2-S1, 共识]
6 个模型 × 3 域 × 3000+ 条件评估，22+ remediation strategies 全部失败，形成强有力的负面结论闭环。Oracle 控制（gold FOL → +29.90pp Mistral-7B, +14.22pp Qwen-14B, +11.50pp ProofWriter）精确分离了聚合机制与约束质量的因果关系，是全文最有说服力的实验。

**S2: Symbolic Confirmation Bias 的定量化有独立贡献价值。** [R1-S1, R2-S3, 共识]
Bias ratio 4.97×、94% 错误与 SC 重叠、跨 3 个模型族的一致性（Table 14）——这些定量指标超越了 "LLMs cannot self-correct" 的定性结论，为社区理解自验证失败的具体机制提供了可操作的诊断工具。

**S3: CJT + Effective-K 框架提供有价值的分析透镜。** [R2-S2, R1-S5]
将 Condorcet Jury Theorem 引入 LLM trace 分析，Effective-K 指标直观量化了"额外采样的边际收益递减"。跨 4 种聚合方法和 3 个模型族的 κ ≥ 0.40 ceiling（Table 3）支撑了 independence bottleneck 的普遍性。

**S4: 写作结构清晰，统计报告完整。** [R1-S6, R2-S5]
正文 8 页内容密度高，Contribution 列表精确对应后续 sections。McNemar exact test、bootstrap CI、power analysis（虽然结论不利于作者）的全面报告体现了统计诚实性。Limitations 段覆盖 scale/language/power/computation 各维度。

**S5: 跨架构 PoC 提供建设性出路。** [R1-S4, R2-S4]
DeBERTa NLI 在 ProofWriter 上 +3.50pp（p=0.013），打破 same-model ceiling，为论文从纯负面转向有条件的正面展望提供了实验支撑。

---

## Weaknesses

### Must-Fix

**W1: 统计功效严重不足，标题 "Fail" 过度断言。** [R1-W1(must-fix), R2-AGREE]
Power analysis（Appendix E）显示 observed power 仅 5.7%–20.6%，MDE 为 4.64–8.84pp。如果 SICA 真实效应为 1–2pp（对 reasoning benchmark 已属 meaningful），当前样本量根本无法检测到。标题 "Fail" 和 abstract "fail to surpass majority voting" 是 evidence of absence 的措辞，但统计证据仅支持 absence of evidence。
- **修复方案**: (1) 对 confirmatory conditions 运行 TOST equivalence test（margin ±2pp）——若 TOST 显著拒绝效应 ≥2pp 的假设，可有底气声称 "no practically meaningful improvement"；(2) 若 TOST 不显著，软化语言："...provide no detectable improvement at current sample sizes" 或 "...do not yield statistically significant gains"；(3) 标题改为 "Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning"。

**W2: 跨架构 PoC 多重比较未校正。** [R1-W2(must-fix), R2-AGREE]
DeBERTa 在 2 datasets × 3+ weight configurations 上测试。ProofWriter w=3 的 p=0.013 在 Bonferroni（6 comparisons, threshold 0.0083）下不再显著；仅 w=5 的 p<0.001 可能存活。论文未报告任何多重比较校正。
- **修复方案**: 报告 Bonferroni/BH 校正后 p 值，或明确标注 §6 为 exploratory analysis。以 ProofWriter w=5（p<0.001，校正后仍显著）为主要证据。

**W3: 核心发现与 self-correction/self-verification 文献的区分不足。** [R2-W1(must-fix), R1-partial-rebut]
"Symbolic Confirmation Bias" 本质上是 Huang et al. (2024) self-correction failure 和 Stechly et al. (2025) self-verification failure 在符号域的具体实例化。论文引用了这些工作但未充分论证其增量贡献。R1 部分反驳：认为定量框架（κ, Effective-K, BR）本身有价值；R2 坚持需要更清晰的区分。
- **修复方案**: 在 Introduction 或 §7 增加段落，明确对比 (a) Huang/Stechly 的定性结论 vs (b) 本文的定量贡献（Effective-K 框架、BR 指标作为诊断工具、process-level independence 发现形式验证也无法突破 confirmation bias）。

**W4: 关键相关工作缺失。** [R2-W2(must-fix), R1-AGREE]
- **CLOVER** (Ryu et al., ICLR 2025): compositional FOL translation + SAT verification，在 7 个逻辑推理 benchmark 上 SOTA。与 SICA pipeline 直接相关——为什么 compositional translation 有效而 self-extraction 失败？
- **VERGE** (arXiv 2601.20055): SMT solver iterative refinement
- **"Not All Votes Count! Programs as Verifiers"** (Xia et al., 2024): programs-as-verifiers 增强 SC
- **"Logical Soundness is not a Reliable Criterion..."** (arXiv 2604.04177): LLM formal logic 系统性失败 position paper
- **修复方案**: 在 §2 Neuro-symbolic reasoning 段落补充 CLOVER 和 VERGE，讨论 compositional translation vs free-form extraction 的对比。

### Should-Fix

**W5: CJT 框架应用不够严谨——Fleiss' κ 作为 ICC proxy 有统计学问题。** [R1-W3(should-fix), R2-Q3, 共识]
Fleiss' κ 是名义尺度一致性指标，与 Ladha (1992) 意义上的投票者相关系数统计含义不同。Kish (1965) design-effect 公式假设等相关结构（constant pairwise correlation），在 LLM traces 中未被验证。论文已添加 "qualitative proxy" 声明，但 K_eff 数值仍被大量用于定量推断。
- **修复方案**: (a) 补充 pairwise vote correlation 作为替代/交叉验证指标；(b) 或弱化 CJT 框架的定量角色至 conceptual motivation。

**W6: Bias ratio 报告不一致。** [R1-W4(should-fix)]
§5.2 报告 4.97× raw / 4.24× weighted，跨模型 "1.97×, 3.93×, 2.88×" raw——但 Table 14 中 weighted 数字为 2.14/3.05/2.86×。4.97× 的计算范围（哪个条件、pooled 还是单条件）不明确。
- **修复方案**: 在 §5.2 明确标注 4.97× 的计算条件和 raw/weighted 区别，Table 14 同时报告两种 ratio。

**W7: Type A/B/C failure mode 分类为 post-hoc 但呈现为理论框架。** [R1-W5(should-fix), R2-AGREE]
SC 准确率阈值（60%, 40%）无理论推导或 sensitivity 分析。
- **修复方案**: 明确标注为 post-hoc empirical taxonomy。

**W8: Process-Level Independence 的 TF-IDF cosine similarity 过于粗糙。** [R2-W3(should-fix), R1-Q3, 共识]
TF-IDF 只捕获 lexical overlap，无法区分语义相似但表述不同的推理路径。论文已声明 "lower bound"，但作为 Contribution 3 的核心方法论，需要更强的支撑。
- **修复方案**: 补充 sentence embedding（SimCSE/SBERT）对比验证，或在 Limitations 中更显著地讨论此限制。

**W9: Degeneration condition (Eq. 4) 推导不完备。** [R1-W6(should-fix)]
从 constraint coupling 到 score 退化为 majority voting 的推导缺少关键步骤——需假设 SAT 检查在退化 regime 下几乎不淘汰约束。
- **修复方案**: 补充退化条件下 constraint rejection rate 的经验证据，或标注 Eq. 4 为 approximate。

**W10: "Symbolic Mirage" 术语精确度。** [R2-W5(should-fix), R1-rebut]
"Mirage" 暗示约束方法论整体失效，但 Oracle 实验证明机制有效。R2 认为命名误导，R1 认为有教学价值但需 scoping。分歧点。
- **修复方案**: 保留术语但在首次出现时明确定义范围："self-extraction 产生的约束是 mirage，而非符号约束方法论本身"。

### Minor

**W11**: α=0.5 penalty weight 无 sensitivity analysis 或 justification。[R1-W7]
**W12**: GSM8K (n=30) / AIME (n=22) 在 Table 1 中与大样本条件并列，应加分区标注。[R1-W8]
**W13**: orphan bib entry `press2023compositionality`。[R1-W9, R2-W6]
**W14**: Reasoning models (o1, R1, QwQ) 未在 §2 作为独立类别讨论。[R2-W7]
**W15**: 部分 bib author name 与 OpenAlex 记录不一致，建议核实。[R2-W6]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识 [AGREE]：

1. **统计功效不足是核心缺陷**——标题/abstract 的 "Fail" 断言超出统计证据支撑，需要 TOST equivalence test 或措辞修正。
2. **跨架构 PoC 需要多重比较校正**——p=0.013 在 6+ comparisons 下不再显著。
3. **CJT/Fleiss' κ 框架的定量使用需要更严格的 justification**。
4. **TF-IDF 作为 process-level independence 指标过于粗糙**，需补充验证或加强 limitation 讨论。
5. **CLOVER 等关键引用缺失**需要补充。
6. **Oracle 控制是全文最强实验**，确认聚合机制有效。
7. **实验覆盖面广、统计报告诚实**是显著优势。

---

## Reviewer Divergence

**新颖性评估**（主要分歧）：
- **R2**（3.0/5 Excitement → 2.5）：核心发现可从 Huang (2024) + Stechly (2025) 合理预期，"Symbolic Confirmation Bias" 是已知结论在符号域的实例化。论文需更清晰论证定量工具的增量价值。
- **R1**（3.5/5 Excitement → 3.5）：虽然定性方向可预期，但 Effective-K 框架、BR 指标、process-level independence 的定量化是真正的新贡献，为社区提供了分析 self-verification 失败的可复用工具。
- **Director 判断**: R2 的新颖性担忧有理有据——一个 well-informed reader 确实可以从已有文献推断出 "self-extracted symbolic constraints will inherit model bias"。论文的增量价值在于定量化程度和实验规模，但这需要在论文中被显式论证。当前论文未充分做到这一点。

**"Symbolic Mirage" 术语**（次要分歧）：
- R2 认为术语 marketing-like 且误导（Oracle 证明机制有效）；R1 认为有教学价值。
- **Director 判断**: 术语可保留但需更精确的 scoping。

---

## Questions

**Q1** [R1]: Symbolic Mirage 假说 (Eq. 5) 的概率空间定义需要更精确——E_θ 的定义、条件化的 σ-algebra、"·" 的含义均不清楚。

**Q2** [R1]: K sensitivity 中 K=8 时 Δ≈+4.90pp 是否值得更深入分析？non-monotonicity 可能指向约束冗余度与 K 的关系。

**Q3** [R1]: T_ext=0.3 的选择依据？是否做过 extraction temperature sensitivity analysis？

**Q4** [R2]: QwQ-32B 在 Type A 条件下无 significant degradation——reasoning models 的 CoT 结构是否缓解 confirmation bias？

**Q5** [R2]: ProofWriter Oracle 的 gold constraints 如何构造？DSL 自动转换 vs 人工标注？

**Q6** [R1/R2]: 跨架构 PoC 为何仅在 FOLIO/ProofWriter 测试？是否尝试过其他外部信号源（不同 LLM family 作为 extractor, code execution verification）？

---

## Missing References

1. **CLOVER** (Ryu et al., ICLR 2025) — compositional FOL translation + SAT, SOTA on 7 benchmarks [R2, R1-agree, critical]
2. **VERGE** (arXiv 2601.20055) — SMT solver iterative refinement [R2]
3. **"Not All Votes Count! Programs as Verifiers"** (Xia et al., 2024) [R2]
4. **"Logical Soundness is not a Reliable Criterion..."** (arXiv 2604.04177, Apr 2025) — position paper [R2, possibly concurrent]
5. **Equivalence testing literature**: Lakens (2017) "Equivalence Tests: A Practical Primer" 或 Schuirmann (1987) [R1, 如果采用 TOST 修复方案]
6. **Amonkar et al. (2025)** — 已引用但 §2 讨论过浅，需更详细对比 [R1]

---

## External Review

**外部审稿（Stanford Agentic Reviewer）**: 未请求（项目配置中 `external_review.paperreview_ai.enabled` 未启用）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（1 critical, 3 warning, 20 info）。

**Critical**:
- **Page 20**: 仅顶部约 15% 有内容（Extended Limitations 末尾），>75% 为空白。审稿人翻到此页会有未完成/草率的印象。建议调整附录段落分布或将后续 Figures 前移填充。

**Warning**:
- **Pages 1-3**: 前 3 页无任何 display item（figure/table），第一个视觉锚点 Figure 1 直到 page 4 才出现。建议将 Figure 1 提前至 page 2-3。
- **Page 8**: Discussion + Conclusion 整页纯文本。建议将附录 Figure 4（intervention summary bar chart）提升至主文。
- **全文主文**: 仅 5 个 display items（2 figures + 3 tables），对实证论文偏低。Figure 4（22+ intervention 条形图）和 Figure 6（κ-accuracy scatter）是最佳提升候选。

**Info highlights**: 模板使用正确（`\usepackage[review]{acl}`），匿名合规（Author: Anonymous），行号显示正常，无 LaTeX 错误残留，无 margin overflow，引用无 [?] 未解析。公式渲染全部正确。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**Reviewer 分数**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)

**评分依据**:

论文在实验设计和分析深度上表现出色——6 个模型、22+ remediation strategies、Oracle 控制、3 个 testable predictions、process-level 分析，构成了一个完整且有说服力的研究叙事。Symbolic Confirmation Bias 的定量化（BR 4.97×, 94% overlap）和 Effective-K 框架本身有工具性价值。

然而，三个关键问题制约了论文达到 Conference（4.0）水平：

1. **统计推断基础不足**（R1-W1, 共识 Must-Fix）：标题和 abstract 的 "Fail" 断言是 evidence of absence 的措辞，但 observed power 5.7%–20.6% 仅支持 absence of evidence。这不是修饰性问题——这是论文核心 claim 的统计有效性问题。TOST equivalence test 是必要的补充。

2. **新颖性不够清晰**（R2-W1, 分歧但偏 R2）：核心发现——"自提取符号约束继承模型偏差"——可以从 Huang et al. (2024) self-correction failure 和 Stechly et al. (2025) self-verification failure 的已有结论合理预期。论文的增量在于定量化程度和实验规模，但这一增量价值未被显式论证。缺失 CLOVER 等关键引用进一步削弱了论文对 neuro-symbolic 领域的覆盖。

3. **跨架构 PoC 统计可靠性存疑**（R1-W2, 共识 Must-Fix）：作为论文唯一的正面实验结果，p=0.013 在多重比较校正后可能不再显著。

综合来看，论文具有 Findings 水平的贡献——实验扎实、分析有深度、负面结果有社区价值。若能解决上述三个关键问题（TOST test 或措辞修正 + 明确新颖性论证 + 多重比较校正），评分有望提升至 3.5 (Borderline Conference)。

**置信度**: 4/5

---

## Detailed Comments

### §1 Introduction
- 开篇 motivation 清晰："SC is hitting a ceiling" → CJT explains why → SICA attempts to break it → fails → Symbolic Mirage。
- Contributions 列表准确对应后续内容。
- 缺：需增加段落明确区分 Huang/Stechly 的定性结论与本文定量贡献。

### §2 Related Work
- 覆盖 4 个方向（SC extensions, neuro-symbolic, test-time compute, CJT/ensemble），结构完整。
- 缺：CLOVER (ICLR 2025)、VERGE、reasoning models 作为独立类别。
- Amonkar et al. (2025) 已引但讨论过浅。

### §3 Background & Setup
- SICA pipeline 形式化定义完整（Eq. 1-4, Figure 1, Algorithm 1-2）。
- Symbolic Mirage 假说（Eq. 5）有 3 个 testable predictions，结构化程度高。
- 问题：(a) Fleiss' κ → K_eff 映射的统计严谨性；(b) Eq. 4 degeneration condition 推导不完备；(c) Eq. 5 概率空间定义不精确。

### §4 Experiments
- Table 1 主结果表全面，Type A/B/C + Degenerate + Oracle 分组清晰。
- Oracle 控制是全文最强实验（+29.90pp, +14.22pp, +11.50pp）。
- 问题：(a) power 5.7%–20.6% 不支持 "fail" 结论；(b) GSM8K/AIME 小样本应更明确标注 exploratory。

### §5 Analysis
- §5.1 Effective-K 跨 15 条件一致。
- §5.2 Confirmation Bias 量化有力（BR 4.97×, 94% overlap）但数字报告需一致化。
- §5.3 Process-level independence 发现有独立价值但 TF-IDF 方法有限。
- §5.5 22+ remediation strategies 全部失败是强证据，但展示效率可优化（Figure 4 在附录中，应提升至主文）。

### §6 Cross-Architecture PoC
- 方向正确，ProofWriter +3.50pp (p=0.013) 是论文最重要的正面结果。
- 需多重比较校正。ProofWriter w=5 (p<0.001) 在校正后仍显著，应以此为 primary。
- Per-label 分析（DeBERTa 擅长 False, SC 擅长 Unknown）提供了互补性机制解释。

### §7 Discussion
- 三段结构（mechanism, broader implications, open questions）合理。
- Krogh/Brown ensemble diversity 文献连接和 Turpin CoT faithfulness 连接有价值。
- 缺：与 CLOVER 等 compositional translation 方法的对比讨论。

### §8 Conclusion
- 简洁覆盖主要发现。

### Limitations
- 全面覆盖 scale/language/power/computation，统计诚实性体现。
- Power analysis 放在附录而非 limitations 主段落中，建议将核心数据（power 5.7%–20.6%）在 limitations 段内显式提及。

### Appendix
- 内容充实（22 pages total），prompts、algorithms、case studies、ablations、power analysis、bootstrap CI 齐全。
- Page 20 空白需修复。
