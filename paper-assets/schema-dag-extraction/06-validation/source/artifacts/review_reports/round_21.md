---
round: 21
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-19T12:02:25.076706+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 21 Consolidated Review Report
## "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Target Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewers**: R1 (method rigor), R2 (novelty + writing)
**Review Mode**: Fresh (independent full review)

---

## Summary

本文研究 schema 复杂度（类型数量和类型间混淆度）如何影响 zero-shot LLM 信息抽取性能。作者提出二维退化模型：Dimension 1（类型数量增加导致 recall 下降）和 Dimension 2（类型混淆度 BCS 预测 type substitution 错误）。使用 Schema Confusability Score（SCS，借鉴自 LLM-PEE）和 Batch Confusability Score（BCS）作为度量，在 4 个数据集（Few-NERD、FewRel、DocRED、MAVEN）上对 Qwen3-32B 进行系统实验，并用 Llama-3.1-70B/8B 和 Gemini 2.5 Flash 做跨模型验证。论文还报告了 SDGD（Schema-DAG-Guided Decomposition）的负面结果。

论文方法论总体扎实，BCS-controlled stratified 实验设计有方法论贡献，负面结果（SDGD）的诚实报告值得肯定。但核心 claim 的 scope 与 evidence 之间存在系统性错位，多项统计检验功效不足，且 confusability 效应的实际规模（typical ~2pp）限制了实用价值。

---

## Strengths

**S1. 系统性实验设计（双方共识）**
BCS-controlled stratified 实验框架是本文的核心方法论贡献。固定类型数量、仅变化 BCS 来隔离混淆度效应，这一设计在 schema complexity 研究中具有方法论价值，可为后续工作复用。

**S2. 负面结果的诚实报告（双方共识）**
§6 SDGD 负面结果（graph coloring 仅 +1.4pp n.s.，oracle routing +29.8pp 但 practical routing 全部低于 baseline）的完整报告，对社区有真正的信息价值。Merge amplification 和 routing failure 的分析帮助后续研究避免同类陷阱。

**S3. 跨模型一致性验证（双方共识）**
Dimension 1（count curve）在 4 个模型（含 Gemini 2.5 Flash API 模型）上 slope 一致性通过 permutation test 验证，增加了 count-degradation 发现的可信度。

**S4. 统计严谨性意识（R1 首提，R2 部分同意）**
Bootstrap CI、TOST equivalence testing、permutation slope comparison 等统计方法的使用显示作者具备统计素养。虽然具体执行有问题（见 Weaknesses），但方法论意识本身是正面的。

**S5. Centrality confound 识别（R1 首提，R2 同意有方法论价值）**
在 MAVEN 同域 schema 上识别 per-type BCS 与 centrality 混淆的问题，展示了实验分析的自觉性。

**S6. 写作质量总体良好（R2 首提）**
论文结构清晰，narrative 连贯，几乎无 AI 写作痕迹（em-dash 已清理），Limitations section 内容充实。

---

## Weaknesses

### Critical

**W1. TOST ±3pp margin 存在循环论证，bounded interaction 证据不足 [R1-W1, R2 同意]**
TOST equivalence testing 的 ±3pp margin 来源于 batch-level 标准差，而 batch SD 本身部分由 BCS 驱动，构成循环论证。更严重的是，4 组 TOST 检验中仅 1 组（FewRel sentence-level, linear scale）拒绝了非等价假设；其余 3 组均 inconclusive（logit p=0.209, DocRED p=0.77, NER p=0.50）。论文在 Intro/Conclusion 中已限定 scope 为 "sentence-level RE"，但 TOST margin 的理论基础仍然薄弱。

**W2. DocRED R²=53% 来自 n=35 不稳定估计，Abstract headline 误导 [R1-W2, R2 完全同意]**
Abstract 使用 "22-53%" 作为 BCS 解释力 range 的 headline，但上界 53% 来自 DocRED 仅 35 个观测点的 bootstrap，CI [0.27, 0.73] 极宽。将统计功效最弱的 dataset 的最高点估计作为 headline upper bound，会给读者造成远超实际的印象。DocRED factorial TOST 也完全 inconclusive (p=0.77)。

**W3. Dimension 2 缺乏 proprietary model batch-level 验证，claim scope 过宽 [R1-W3, R2 同意]**
Abstract "effects replicate across model scales and families" 未区分 pairwise SCS（schema-structural，不依赖 constrained decoding）和 batch-level BCS（依赖 forced-choice format）。Gemini 验证仅覆盖 Dimension 1 count curves；Dimension 2 的 batch-level BCS 效应未在 API 模型上验证。

**W4. SCS 指标借用自 LLM-PEE，novelty framing 不清晰 [R2-W1, R1 同意]**
SCS 与 LLM-PEE 的 partitioning criterion 形式上相同。Contribution 1 虽已改为 "Building on... prior work"，但论文整体 framing 仍可能让读者误以为 SCS 是本文创新。真正的 novelty 在 BCS-controlled stratified experimental framework，而非度量本身。

**W5. Typical effect size ~2pp，实用价值有限 [R2-W3, R1 完全同意]**
自然 schema sampling 下，BCS 变异产生的 typical effect 仅约 2pp（IQR=0.054）。80-relation 自然 pool 内 BCS slope 为 +0.221, p=0.76（不显著）。Abstract/Intro 引用的 25-31pp extreme-batch 差异来自人为构造的极端分组，不代表 realistic 场景。论文的价值更多在理论理解而非实际干预指导。

### Warning

**W6. NER Dimension 2 batch-level 为 null [R2-W4, R1 完全同意]**
NER 的 BCS batch-level 效应 r≈0（n=450），Dimension 2 仅在 RE forced-choice 任务上成立。Title "Information Extraction" 过于宽泛，暗示所有 IE 子任务均适用。

**W7. Embedding 选择不一致 [R2-W6, R1 同意]**
Few-NERD 使用 Qwen3 embedding，其余使用 MiniLM。论文自身数据显示 MiniLM 在 Few-NERD 上 r=0.172 > Qwen3 r=0.138，反驳了选择 Qwen3 的理由。应统一使用 MiniLM 作为主 embedding。

**W8. NER U-shape dual-task burden 假说缺乏直接验证 [R1-W5, R2 同意]**
Count 22-44→66 的 NER recovery 被解释为 "dual-task burden reduction"，但这是 post-hoc 假说，缺乏控制实验（如 "extract ALL then filter"）的直接验证。70B 上复现增加可信度但不等于验证。

**W9. 无有效干预方案 [R1-W6, R2 部分同意]**
Confusability 可检测但不可干预：graph coloring +1.4pp n.s.，renaming 降低准确率，few-shot 扩大 gap。论文价值定位应从 "prediction + intervention" 转向 "diagnostic understanding"。

**W10. Renaming 实验支持 conceptual overlap 替代解读，削弱 SCS construct validity [R1-W7, R2 高度同意]**
SCS 基于 name embedding similarity，但 renaming 失败（甚至降低准确率）表明类型混淆可能由概念重叠而非 label surface similarity 驱动。SCS 可能是 downstream proxy 而非 root cause metric。R2 评价此为"本轮最有力的理论质疑之一"。

**W11. MAVEN ED 贡献有限 [R2-W5, R1 部分同意]**
MAVEN 仅提供 pairwise 验证和 centrality confound 识别，batch-level 无 positive evidence。不应与 NER/RE 并列为等价贡献。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识：

1. **TOST margin 基础薄弱**（R21-C1）：3/4 条件 inconclusive，margin 选择缺乏独立 principled basis
2. **DocRED R²=53% 不应作为 headline**（R21-C2）：n=35, CI 过宽
3. **Dim2 proprietary gap**（R21-C3）：batch-level BCS 未在 API 模型验证
4. **SCS novelty 需重新 frame**（R21-C4）：指标借用，创新在实验设计
5. **Typical effect ~2pp**（R21-C5）：extreme-batch 数字不代表 realistic 场景
6. **NER Dim2 batch-level null**（R21-W1）：title 过宽
7. **Embedding 不一致**（R21-W2）：MiniLM 实际更优
8. **NER U-shape 未验证**（R21-W3）：post-hoc 假说
9. **无有效干预**（R21-W4）：诊断 > 干预
10. **Renaming 支持替代解读**（R21-W5）：conceptual overlap vs label surface similarity

---

## Reviewer Divergence

**Title "Predict" 是否应修改**（R21-D1）：
- R2：Must-Fix。论文仅 correlational evidence，"predict" 暗示因果或 actionable prediction。
- R1：REBUT。"Predict" 在统计回归语境中是标准用语（"X predicts Y" = "X is a statistical predictor of Y"），论文明确使用 "predictive relationship" 而非因果语言。
- **Director 判断**：R1 的 REBUT 有理。"Predict" 在定量社会科学和统计学中是标准回归术语，不暗示因果。但建议作者在 rebuttal 中准备防御，因为部分审稿人可能持 R2 立场。此项不降分。

---

## Questions for Authors

**Q1**（R1）：TOST margin 如果改用 ±2pp 或 ±5pp，哪些条件的结论会翻转？Table 4 sensitivity 是否覆盖了这些边界？

**Q2**（R1）：NER U-shape 是否可以通过 "extract ALL entities then filter by type" 的控制实验来验证 dual-task burden 假说？

**Q3**（R2）：80-relation natural pool 内 BCS slope 不显著（p=0.76），是否意味着 Dim2 在 realistic full-schema 部署中不可检测？

**Q4**（R2）：Gemini count-64 仅 11/25 batches 完成，dropped batches 的 BCS 分布是否与 completed 有系统偏差？

**Q5**（R1）：70B BCS validation 使用了哪个 pool？CI 较宽是否因为样本量不足？

---

## Missing References

- Josifoski et al. (2022) "GenIE: Generative Information Extraction" (NAACL 2022) — constrained generation for IE, 与本文 constrained decoding 方法直接相关

---

## External Review

**外部审稿：未配置**。项目未启用 external_review（paperreview.ai），本轮无外部审稿意见。

---

## Overall Assessment

**Overall Score: 3.0 — Findings（可被 Findings 接收）**

**Soundness: 3.5** — 实验设计有方法论价值，统计方法选择合理，但 TOST 执行有缺陷（3/4 inconclusive），DocRED n=35 不稳定，embedding 选择不一致。

**Excitement: 2.5** — Dimension 1 是 well-known 的 schema-size degradation 的系统验证（incremental），Dimension 2 的 batch-level 效应仅在 RE forced-choice 成立且 typical effect ~2pp，无有效干预方案。SDGD 负面结果有信息价值但本身不构成足够的 novelty。

**Confidence: 4.0** — 两位 Reviewer 独立给出相同评分，交叉分享后在所有 critical issue 上达成共识。

### 评分理由

**支持 Findings 的因素**：
- BCS-controlled stratified 实验设计是可复用的方法论贡献
- SDGD 负面结果对社区有真实信息价值
- 4 个数据集、4 个模型的系统性验证工作量大
- 统计方法论意识好（虽然执行有缺陷）
- 写作质量良好，结构清晰

**阻止 Conference (4.0) 的因素**：
- Typical effect size ~2pp 限制了实用 impact
- Dimension 2 batch-level 仅在 RE forced-choice 成立（NER null, ED confounded），title/abstract 过度概括
- SCS 指标非原创，真正 novelty（实验框架）的 framing 不清晰
- 5 项 critical issue 中 3 项涉及 claim scope 与 evidence 错位
- 无有效干预方案（所有尝试均失败或不显著）

**不降至 2.5 (Borderline Findings) 的因素**：
- 实验设计本身扎实，非方法错误而是 framing 问题
- 多数 critical issue 可通过 scope 限定和 reframing 在 revision 中解决
- 负面结果的贡献是真实的

### Rebuttal 建议关注点

如果作者 rebuttal，审稿人最关注以下问题的回应：
1. TOST margin 的独立 justification（R21-C1）
2. Abstract/headline 数字的 recalibration（R21-C2, C5）
3. Dim2 scope 限定（R21-C3, W1）
4. SCS novelty 的诚实 repositioning（R21-C4）

---

## Detailed Comments

### 格式合规性
- ✅ ACL 2023 模板，`[review]` 选项
- ✅ 匿名化（`\author{Anonymous}`）
- ✅ 正文 8 页
- ✅ Limitations section 存在且充实
- ✅ Responsible NLP Checklist 完整填写
- ✅ 附录双栏格式
- ✅ 无 em-dash AI 写作痕迹
- ⚠️ -ing 分词短语残留（Abstract/Results 中 "revealing...", "establishing..."）
- ⚠️ P-value 报告格式不一致（p<0.001 vs p<10^{-35}）

### 按 Section 的具体意见

**Abstract**: 数据密度过高。建议精简到 2-3 个关键数字，删除 "22-53%" upper bound，限定 "effects replicate" 的 scope。

**Introduction**: Finding 陈述中的统计限定词（TOST, inconclusive）对非统计学读者有认知负担，但删除会导致 overstatement。建议保留但简化措辞。Contribution 1 需明确 SCS 来源。

**§3 Experimental Setup**: Embedding 选择 justification 需修正（§3.2 选择 Qwen3 for Few-NERD 但 MiniLM 效果更好）。

**§4 Results**: DocRED R² 需标注 CI 和 n；80-rel natural pool 不显著结果需在正文（而非仅 appendix）讨论。

**§5 SDGD**: 这是论文最有信息价值的 section，建议保留完整篇幅。

**§7 Discussion**: 需更诚实 frame 实践意义（诊断 > 干预）；需讨论 conceptual overlap vs label surface similarity。

**Limitations**: 已较充实，建议补充 typical effect size ~2pp 的实践意义讨论和 NER Dim2 null 的限制。