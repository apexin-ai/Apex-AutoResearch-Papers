---
round: 29
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-22T04:30:34.833542+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 29 (Fresh Review)

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）
**轮次**: 1 轮独立审稿 + 1 轮交叉分享（共识达成，无需 Round 2）

---

## Summary

本文研究 schema 复杂度（类型数量 + 类型间混淆度）如何影响 training-free LLM 信息抽取性能。提出 SCS/BCS 两个 embedding-based 指标，通过 BCS-controlled batch design 在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）上隔离 count 和 confusability 两个维度。主要发现：(1) count 退化跨 4 数据集、4 模型一致；(2) BCS 解释 FewRel RE 上 ~22% 的跨 batch 准确率方差；(3) schema 分解因 merge amplification 和 routing failure 而失败。

---

## Strengths

**S1 [共识]**: BCS-controlled batch design（固定 count 变 BCS 隔离 confusability）是真正的方法论创新，可被后续研究复用。

**S2 [共识]**: 统计严谨度显著高于同类 NLP 实证工作——bootstrap CIs、TOST equivalence tests、power analysis、partial correlations、permutation tests、variance decomposition。

**S3 [共识]**: 对负面结果和 confounders 的报告达到罕见的透明度——NER batch-level null（3 模型一致）、MAVEN centrality confound、SDGD 失败均如实呈现并附带诊断分析。

**S4 [共识]**: Count 退化的实证基础极其扎实——4 数据集、3 任务、4 模型方向一致，效应量大（FewRel -36pp, DocRED -49pp）。

**S5 [共识]**: 19 页 Appendix 提供完整 prompt templates、cross-model validation、sensitivity analysis、confound controls，reproducibility 标准极高。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [Critical, R1+R2 AGREE]: BCS 度量的干净证据仅限 FewRel RE，但论文叙事暗示跨任务适用性。**

逐数据集审查：
- FewRel RE: R²=0.22, VIF=1.18 — **唯一 confound-free 证据**
- DocRED RE: VIF=50.9, BCS-centrality r=0.99, partial correlation 标准误膨胀 ~7x, 不可信
- MAVEN ED: controlling for centrality 后 BCS → non-significant (p>0.2)
- Few-NERD NER: batch-level null, 3 模型 × 2 prompts 一致

Abstract "inter-type confusability drives type substitution errors" 的泛化语气与证据不匹配。Count 退化的 4 数据集一致性与 BCS 的 FewRel 局限性形成鲜明对比。

**必须修改**: Abstract/Introduction 明确区分 count 退化（跨任务一致）和 BCS 效应（clean evidence 仅 FewRel RE）。考虑在补充 1 个 VIF 可控的新数据集上验证 BCS。

**W2 [Critical, R1+R2 AGREE]: DocRED VIF=50.9 的处理不充分。**

VIF=50.9 意味着 BCS 和 degree centrality 几乎完全线性相关，partial correlation 的 SE 膨胀 √50.9 ≈ 7.1 倍。在此条件下报告的 p<0.001 几乎不可解释。然而 §4.3 main text 仍呈现 DocRED R²=0.578，虽附注说明了 collinearity，但可能给粗读读者造成 "DocRED 效应更强" 的错误印象。

**必须修改**: Main text 明确标注 DocRED BCS 因 VIF=50.9 不可解释，不作为支持证据呈现。提供 ridge regression 或 PCA-based partial correlation 作为 robustness check。

### Should-Fix（影响评分）

**W3 [Major, R2 raised + R1 AGREE]: SCS/BCS 相对 LLM-PEE 技术新颖性有限。**

SCS = embedding cosine similarity，论文自认继承自 LLM-PEE。BCS 的 max 聚合技术含量有限。贡献定位为 "旧指标 + 新实验范式 + 实证发现"。如果 BCS 仅在 FewRel 有干净证据，novelty 和 evidence 同时偏弱。

**建议**: §3.2 更明确阐述 SCS/BCS 与 LLM-PEE 的技术差异。增强实证覆盖比修饰指标新颖性更有效。

**W4 [Major, R1 raised + R2 AGREE]: TOST 等价性检验结论依赖量表选择。**

- Probability scale ±3pp: TOST p=0.003 → equivalence
- Logit scale ±3pp: TOST inconclusive; interaction p=0.047 (边缘显著)

两个量表在关键 margin 给出相反结论。"Count 和 confusability independently addressable" 这一核心 claim 处于刀刃上。Logit scale 对 bounded metrics 通常更理论合理。

**建议**: 弱化为 "approximately additive on the probability scale within the observed range"。Main text 明确报告两个量表的结论差异。

**W5 [Major, R1 raised + R2 AGREE]: Abstract/Introduction 使用因果语言超出证据支撑。**

"Drives" 暗示因果关系。BCS-controlled design 是 quasi-experimental 但非 randomized intervention。§6 承认 "correlational evidence with controlled stratification"，与 abstract 中的 "drives" 矛盾。

**建议**: 将 "drives" 替换为 "predicts" 或 "is associated with"。

**W6 [Major, R1 raised + R2 partial REBUT]: Greedy batch 构造可能引入 domain concentration confound。**

High-BCS batches 倾向选择同一语义域的类型。FewRel 的 balanced design 和 cross-prompt validation 部分缓解，但不能排除 cluster-level domain difficulty 这一替代解释。

**建议**: 报告 extreme batches 的 type domain 分布。考虑 domain-matched batch construction 作为 robustness check。

**W7 [Major, R1 raised + R2 AGREE]: 共享 text instances 的 bootstrap CI 可能 anti-conservative。**

1000 个 text instances 跨所有 batches 共享。Instance-level cross-batch correlation 未被 batch-level bootstrap 处理。Appendix R 的 variance decomposition 部分缓解，但形式上 CI 可能偏窄。

**建议**: 提供 cluster-robust SE（cluster on text instance）或 split-sample bootstrap 作为 sensitivity check。

### Minor

**M1**: "First controlled study" claim 实质正确但需更精确措辞限定（"simultaneously isolating count and inter-type confusability as independent dimensions using embedding-based metrics and controlled batch design"）。[R2 raised, R1 partial REBUT — 同意限定措辞]

**M2**: NER null framing 偏向 "低 power" 解释，应同等考虑 "NER 任务特性"（span detection dominance over type classification）作为替代解释。Relaxed matching (Appendix) 仍 null 支持此解读。[R1+R2 AGREE]

**M3**: Discussion 缺少理论层面讨论——为什么 embedding similarity 能预测 LLM type confusion？[R1+R2 AGREE]

**M4**: §5 SDGD 应保留在正文（叙事弧需要）但需压缩，将算法细节移入 appendix。Cross-model validation 的关键表应提升到正文。[R1 keep + R2 demote → 共识: keep but compress]

**M5**: 多重比较无正式校正。核心 claims (p<0.001) 不受影响，但边缘结果（logit interaction p=0.047）在校正后可能 non-significant。[R1+R2 AGREE]

**M6**: 遗漏引用 3 篇: Zhang et al. AAAI 2026 (Reflect then Learn, introspective confusion), NER Retriever (Findings EMNLP 2025, type-aware embeddings), Show Less Instruct More (2024, definition quality for zero-shot NER)。[R2 identified, R1 agrees on 3/4]

---

## Reviewer Consensus [AGREE]

1. BCS 干净证据仅 FewRel RE，论文需明确限定适用范围
2. DocRED VIF=50.9 下的 partial correlation 不可信，不应作为支持证据
3. Count 退化故事跨 4 数据集 4 模型扎实，是 solid contribution
4. BCS-controlled batch design 是方法论创新
5. 统计严谨度和 appendix 质量显著高于同类工作
6. "Drives" 应替换为 "predicts"
7. TOST "independently addressable" claim 需弱化

## Reviewer Divergence [Partial disagreement]

1. **Domain concentration confound (W6)**: R1 认为需要严格验证；R2 认为 balanced design + cross-prompt 提供部分缓解但同意报告 domain 分布。**结论**: 建议作为 should-fix（报告 domain 分布），非 must-fix。

2. **SDGD section 定位 (M4)**: R2 建议降级为 appendix；R1 认为叙事弧需要保留。**结论**: 保留但压缩。

3. **"First controlled study" claim (M1)**: R2 认为 Chen et al./GoLLIE/Reflect 相关；R1 认为这些工作 scope 不同，claim 实质正确。**结论**: 措辞限定即可。

---

## Questions（需作者澄清）

Q1. 能否在一个 BCS-centrality VIF < 5 的新数据集上重复 BCS-controlled 实验？这是提升论文最直接的路径。

Q2. DocRED VIF=50.9 下报告的 partial correlation p<0.001 是否经过 variance inflation 调整？能否提供 ridge regression 结果？

Q3. High-BCS extreme batches 中的 relation types 是否集中在特定语义域（如 kinship, spatial）？

Q4. 跨 batch 共享 text instances 对 bootstrap CI 宽度的影响有多大？Split-sample bootstrap 结果如何？

Q5. NER batch-level null 在 3 模型 + 2 prompts + relaxed matching 上一致——作者是否认为这更可能反映 NER 任务特性而非 power 不足？

Q6. 如果 logit scale 上存在边缘显著的 count×BCS interaction (p=0.047)，"independently addressable" claim 是否需要根本性修改？

---

## Missing References

1. Zhang et al. "Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion" (AAAI 2026) — content uncertainty 与 type confusability 直接相关
2. "NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings" (Findings EMNLP 2025) — type-aware embeddings 方法论相关
3. "Show Less, Instruct More: Enriching Prompts with Definitions and Guidelines for Zero-Shot NER" (2024) — definition quality 影响 zero-shot NER

---

## External Review

**状态**: 未请求（项目未启用外部审稿）

---

## Visual Layout Check（非评分项）

视觉审查已完成（2026-05-22 04:14 → 04:18）。发现：

- **[Critical]** Appendix p.26: Table 28 仅占页面 1/4，下方 ~3/4 空白。应调整 float 位置消除空白。
- **[Warning]** pp.1-2: 前 2 页纯文本无 display item，建议 Introduction 末尾加概览 figure（方法流程图或核心发现 teaser）。
- **[Warning]** p.8: 正文末页压缩 4 个 section（4.4/4.5后半/5/6），Discussion 感觉草草收尾。
- **[Warning]** pp.5-8: 正文仅 4 个 display items（2 fig + 2 table），大量结果在 appendix。建议提升 1-2 个关键 appendix 表到正文。
- **[Info]** Figure 1(b) x 轴标签使用缩写（intA_type 等），不够直观。
- **[Info]** Figure 2 灰度打印下颜色区分度不足。
- **[Info]** 整体排版专业，无 LaTeX 渲染错误、margin 溢出或未解析引用。

---

## Overall Assessment

**评分**: 3.5 / 5 (Borderline Conference)

**EMNLP 2026 标准**: 3.5 = Borderline Conference（可被主会议接收的边缘）

**置信度**: 4/5（两位 Reviewer 均仔细阅读全文及全部 appendix，逐一核查统计方法论）

**理由**:

论文有两个明确的贡献维度：(1) Count 退化的系统性实证——4 数据集、4 模型一致，效应量大，是 solid contribution；(2) BCS-controlled batch design 是方法论创新。然而，BCS 作为 confusability predictor 的核心证据仅在 FewRel RE 上 confound-free（VIF=1.18），另外 3 个数据集均有严重问题（DocRED VIF=50.9 不可解释、MAVEN 归因于 centrality、NER null）。这使得论文的主要叙事——confusability 是独立退化维度——在泛化性上显著受限。

如果作者能在 rebuttal 中：(a) 补充 1 个 VIF 可控的新数据集 BCS-controlled 结果，或 (b) 对 DocRED 提供 ridge regression robustness check 证实 BCS 有独立贡献，或 (c) 将 claim scope 明确限定为 RE 并相应调整 title/abstract，评分可上调至 4.0 (Conference)。

当前状态建议 **Findings 接收**——统计严谨度和实验方法论质量足以接收，但泛化性不足以支撑 main conference。

---

## Detailed Comments（逐节）

**Abstract**: 信息密度可接受但 "drives" 需改为 "predicts"。SCS 的具体含义（pairwise cosine similarity between type-name embeddings）应在 abstract 中明确。

**§1 Introduction**: RQ 设置清晰。"First controlled study" claim 需限定。Contribution list 的第 2 点（task asymmetry）与第 1 点有较多重叠。

**§2 Related Work**: 覆盖面良好。缺 Zhang et al. AAAI 2026。"SCS novelty" 段的自我定位诚实但可能不够自信。

**§3 Experimental Setup**: 设计精良。Table 1 "BCS ranges not comparable across embedding models" 这一限制对结论的影响应展开讨论。

**§4 Results**: Count curves (§4.1) 扎实。BCS-controlled (§4.3) 的 FewRel 结果令人信服。DocRED 结果需 downgrade 呈现方式。TOST (§4.4) 需报告两个量表结论。NER null 需平衡解释。

**§5 SDGD**: 叙事逻辑合理但需压缩。Oracle routing insight (72.4% vs 50.4%) 有价值。

**§6 Discussion**: 过短。需添加 "why embedding similarity predicts LLM confusion" 的理论讨论。Practical implications 已改善但仍可更具体。

**Limitations**: 全面。Item 1 正确标注了单模型分析的范围。"Cannot distinguish" 表述正确但应同等权重讨论 "NER 任务特性" 替代解释。
