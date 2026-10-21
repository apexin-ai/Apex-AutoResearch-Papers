---
round: 14
overall_score: 3.0 (Findings)
timestamp: 2026-05-18T04:34:15.028606+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 14 审稿报告 — schema-dag-extraction

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性），1 轮独立审稿 + 1 轮交叉回应
**审稿模式**: Fresh（重新审稿，无历史轮次记忆）

---

## Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度对性能的影响，将退化分解为两个维度：type count（数量导致 recall 下降，最高 −49pp）和 confusability（语义相似度导致 type substitution，典型 batch 约 2.2pp）。通过 SCS/BCS 指标量化 confusability，在 NER (Few-NERD)、RE (FewRel/DocRED)、ED (MAVEN) 上进行受控实验。BCS 在 RE 上解释 22-53% 跨 batch 精度方差但在 NER 上无 batch 级信号；schema 分解因 merge amplification 和 routing failure 而失败。

---

## Strengths

**[S1] 实验设计精巧，count/confusability 隔离方法有方法论贡献** [共识]
BCS-controlled 实验（固定 count 变化 BCS）有效隔离两个维度，within-pool 分析进一步控制 pool composition confound（permutation p=0.60）。这个设计范式对后续 schema complexity 研究有参考价值。

**[S2] 统计分析在 NLP 领域中异常全面** [共识]
TOST equivalence testing、permutation tests、bootstrap CIs（pair-level B=10,000）、cluster bootstrap、Jonckheere-Terpstra trend test、variance decomposition、partial correlation。多层次 robustness checks（4 种 prompt variants、2 种 embeddings、name-only vs name+definition ablation、cross-seed decomposition）系统性覆盖 potential confounds。

**[S3] 负面结果诚实且有诊断深度** [共识]
SDGD 失败不是简单的"不 work"报告，而是诊断了 merge amplification（NER, precision 0.563→0.210）和 routing failure（RE）两种不同机制，并量化了 oracle upper bound (+29.8pp)。NER batch-level null result 也未被掩盖。

**[S4] Limitations section 详尽** [共识]
8 条 limitations + multiple comparisons 讨论，覆盖 model coverage、effect size、factorial interaction、causal mechanism、data contamination 等。在 NLP 论文中属于极少见的自我审视深度。

**[S5] 跨任务不对称性发现有洞察价值** [共识]
NER 和 RE 对 confusability 的响应模式截然不同（RE 有 batch 级信号，NER 没有），boundary detection failure 的解释有说服力。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[N1] "BCS explains 22-53% of cross-batch variance" claim 范围过宽且 DocRED R² 稳定性未验证** [R1 critical, R2 AGREE]
- 53% 来自 DocRED 仅 n=25 batches，未报告 adjusted R² 和 bootstrap CI，小样本 R² 天然上偏
- NER batch-level R²≈0，但 Abstract "22-53%" 的区间表述暗示跨任务 generality
- 22% R² 对应 typical-batch gap 仅 2.2pp (CI [0.4, 4.0])，presentation 暗示 strong predictive power 但实际 accuracy difference 很小
- **要求**: (1) 报告 DocRED R² 的 adjusted R² 和 bootstrap CI; (2) Abstract/Introduction 明确限定为 "RE accuracy variance"; (3) 讨论 R²=0.22 对应 2.2pp 的 practical significance

**[N2] TOST linear/logit scale 不一致性未充分解决** [R1 critical→R2 降级为 major; 最终评定: major-to-critical]
- Linear-scale TOST p=0.003 (equivalence) vs logit-scale TOST p=0.209 (inconclusive)
- 高 BCS batch accuracy 集中在 ~51%，接近 50% 时 linear scale 系统性压缩 interaction effects，logit scale 是更合适的分析尺度
- Logit-scale 90% CI 上界 (0.203) 超过 equivalence bound (0.156)，不是 "limited power" 能解释的
- Linear-scale 作为 primary test 缺乏 a priori justification
- R2 观点: bounded association 是 supporting claim 非核心，双维度主效应不受影响，因此 severity 应为 major
- **要求**: (1) 提供 logit-scale formal power analysis; (2) 或弱化 claim 为 "bounded under primary linear specification; inconclusive on logit scale"; (3) 讨论 scale choice rationale

### Should-Fix（影响评分）

**[W1] SCS/BCS 指标新颖性不足，与 LLM-PEE 差异化不清晰** [R2 major, R1 AGREE]
- SCS = pairwise cosine similarity of type name embeddings，与 LLM-PEE partitioning criterion 形式相同
- Abstract/Contribution #1-2 以 SCS/BCS 为核心卖点，与 Related Work 中自我定位（"contribution is not the metric itself"）不一致
- 实际增量在于 BCS-controlled 实验范式（experimental framework），而非 metric 本身
- **要求**: Contribution 措辞从 metric-centric 转向 framework-centric; §3.2 "We introduce" → "We operationalize"

**[W2] Confusability 效应量过小 (~2pp)，extreme-batch 叙事权重过高** [R2 major, R1 PARTIALLY AGREE]
- Typical-batch gap 2.2pp vs extreme-batch 25-31pp；count 效应 −49pp
- Introduction/Results 叙事偏向 extreme-batch 数字，typical gap 被弱化
- R1 辩护：analytical study 中 small but real effect 可接受；R2 认为需更有力论证 practical significance
- **共识**: 不构成 rejection 理由，但 Abstract/Introduction 应前置 typical-batch magnitude，extreme-batch 仅作对比锚点

**[W3] 因果语言残余** [R2 major (partial), R1 PARTIALLY AGREE]
- "schema-induced degradation" 全文多处出现，超出 correlational + controlled stratification 证据
- Title "predict" 合适，但正文 "schema-induced" 应改 "schema-associated"
- R² "explains" 在统计学中不暗示因果（R1 REBUT R2），但 "schema-induced" 确实超越
- Appendix 残余 "count-driven" / "BCS-driven" 未清理
- **要求**: 全文 grep "schema-induced" 替换; Appendix 因果语言清零

**[W4] 跨模型 generality claim 超出证据** [R1 major, R2 AGREE]
- "fundamental property of in-context learning" 仅验证了 3 families (Qwen/LLaMA/Gemini)
- Dimension 2 仅在 open-weight RE 上充分验证，Gemini 仅验证 Dimension 1
- 无 closed-source frontier model (GPT-4/Claude) 的 Dimension 2 验证
- **要求**: 弱化为 "consistent across tested model families, suggesting but not establishing generality"

**[W5] FewRel constrained decoding 格式特殊性讨论不足** [R1 major, R2 AGREE with nuance]
- Constrained decoding 消除 calibration signal，confusability 效应可能被 forced-choice 放大
- Limitations item 6 仅一句话，正文讨论不足
- R2 nuance: constrained decoding 对 RE closed-set classification 合理；NER unconstrained 结果提供自然对照
- **共识**: 不需重做实验，但正文需讨论 constrained decoding 对 effect size 的影响

**[W6] SDGD 分析深度不足** [R2 major, R1 PARTIALLY AGREE]
- Merge amplification 无 k 值与 FP 增长的定量分析
- Routing failure 无 error case analysis
- R1 认为作为负面结果深度已可接受，但补充分析是 reasonable suggestion
- **共识**: minor-to-major; 作为 Contribution #4 需更深入分析

### 小问题

- **[m1]** MAVEN 应降级为 supplementary dataset——"four datasets" 声称中 MAVEN 参与度弱 [R2-W6, R1 AGREE]
- **[m2]** Abstract "up to −49pp" 来自 DocRED 非主实验，有 cherry-picking 最大数字嫌疑 [R1]
- **[m3]** Abstract "the gap" 指代不明——应改为 "the confusability gap" [R2-Q5, R1 AGREE]
- **[m4]** Introduction Finding (1) 过于密集（56 词复合句）[R12-N1 遗留]
- **[m5]** TOST 术语首次出现未展开 [R11-W2 遗留]
- **[m6]** Introduction findings vs contributions 数量不对齐 [R12-W4 遗留]
- **[m7]** DocRED/MAVEN 5 batches vs FewRel/Few-NERD 25 batches 不对称未解释 [R1-W7]
- **[m8]** Conclusion 偏短，缺 future work 和 broader implications [R11-W1 遗留]
- **[m9]** NER U-shape "dual-task burden" 解释标注为 hypothesis [R10-m2 遗留]

---

## Reviewer Consensus [AGREE]

1. **实验设计是本文最大优势** — 双 Reviewer 独立认定 BCS-controlled 实验范式有方法论价值
2. **"22-53% variance" 需限定为 RE-specific** — NER batch-level R²=0 不应被 Abstract 的 framing 掩盖
3. **跨模型 generality claim 过强** — "fundamental property of in-context learning" 需弱化
4. **SCS/BCS 增量在 experimental framework 而非 metric** — Contribution 需 reframe
5. **因果语言需继续清理** — "schema-induced" → "schema-associated"
6. **Typical-batch 2.2pp 应前置于叙事** — extreme-batch 数字仅作对比锚点
7. **Constrained decoding 边界条件需在正文讨论** — 不仅限 Limitations 一句话
8. **Limitations section 和负面结果报告是罕见优点** — 学术诚信值得肯定

## Reviewer Divergence [REBUT]

1. **TOST 严重程度**: R1 评 critical（动摇核心 claim），R2 评 major（supporting analysis 非核心支柱）。**Director 判定**: major-to-critical——bounded association 不是唯一核心 claim，但作为论文框架的关键组件，其不确定性需要在正文中 prominently 呈现。
2. **NER Contribution #3 独立性**: R1 认为 task-dependent diagnosis 有独立分析价值（pairwise signal 存在但不 aggregate 的现象值得独立报告）；R2 认为应并入 Contribution #2。**Director 判定**: 保留为独立 contribution 但需改 framing——强调诊断性发现。
3. **"First controlled study" 声称**: R1 认为限定足够（qualified by "to our knowledge" + specific scope）；R2 认为 LLM-PEE 和 PARSE 已隐式涉及。**Director 判定**: 当前限定可接受，无需进一步修改。
4. **R1-W5 Shared-representation dependency**: R2 有效反驳——MiniLM 是 primary embedding（§3.2 明确说明），非 Qwen3。R1 的 "circular dependency" 前提部分有误。**Director 判定**: 此 weakness 降级为 info——MiniLM 与 Qwen3 是独立模型，不构成 circular dependency；confusion matrix correlation=0.894 更可能反映 confusability 是 schema 内在属性。

---

## Questions（需作者澄清）

1. DocRED R²=0.525 (count 16) 的 adjusted R² 和 bootstrap CI 是多少？n=25 上的稳定性如何？
2. FewRel pairwise SCS-confusion r=0.187（§3.2）的计算方法与 Table 2 有何不同？为什么 FewRel 被排除在 Table 2 之外？
3. BCS-Controlled batch 构建如何控制 type difficulty 之外的因素（即 low-BCS ≠ trivially easy, high-BCS ≠ trivially hard）？
4. Name-only SCS vs name+definition SCS 差异极小（Δr: −0.023 to +0.035）——这是否说明 SCS 捕获的是 name-level 表面相似度而非深层 semantic confusability？
5. NER U-shape 在 RE 中不存在的原因？"Dual-task burden" 解释是否有额外证据支持？

---

## Missing References

R1 和 R2 共同建议补充：
1. Structured prediction calibration (Kuleshov & Liang 2015)
2. Label embedding trees for hierarchical label space reduction (Bengio et al. 2010)
3. KG relation schema complexity (Bordes et al. 2013 relation cardinality 分析)
4. Label smoothing exploits inter-class similarity (Müller et al. 2019) — 已在 Related Work 引用
5. GoLLIE (Sainz et al., ICLR 2024) — R2 提出但 R1 确认已引用 (gollie-2024)

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**评分理由**:

论文的实验设计和统计分析在 NLP empirical study 中属于上乘水平，count/confusability 隔离的方法论有参考价值，负面结果报告诚实。然而：

1. **Novelty 受限**: SCS/BCS 是标准 cosine similarity，与 LLM-PEE 形式相同；核心发现"count 远比 confusability 重要"在直觉上可预期
2. **Effect size 小**: Confusability 的 typical-batch 效应仅 2.2pp，practical significance 有限
3. **Claims 需收窄**: "22-53% variance" 需限定为 RE-specific + 报告 DocRED CI；"fundamental property of in-context learning" 超出 3-family 证据；TOST bounded association 在 logit scale 上 inconclusive
4. **分析深度**: SDGD 负面结果和 constrained decoding 边界条件的讨论有提升空间

作为 **Findings 论文**是合适的——方法论扎实，发现有参考价值，对 schema design practitioners 和后续研究者提供了有意义的 characterization。但 **excitement 和 novelty 不足以支撑主会议接收**——核心 confusability 效应太小，SCS 指标无增量，且主要 claim 需显著收窄。

**Confidence: 4/5** — 两位 Reviewer 均仔细阅读全文及附录，熟悉 zero-shot IE、equivalence testing 和 schema complexity 文献。

---

## Rebuttal 建议重点

如果作者进行 rebuttal/revision，以下是最能影响评分的修改：
1. 报告 DocRED R² 的 bootstrap CI 并在 Abstract 限定为 "RE"（N1，可立即执行）
2. 提供 logit-scale power analysis 或弱化 bounded association claim（N2，可立即执行）
3. Contribution 重心从 SCS metric 转向 experimental framework（W1，revision 可修复）
4. 正文讨论 constrained decoding 对 RE effect size 的影响（W5，revision 可修复）
5. "fundamental property" → "consistent across tested families"（W4，一句话修改）

上述 1-2 如能充分回应，评分可能上调至 3.5 (Borderline Conference)。

---

## 维度评分汇总

| 维度 | R1 | R2 | 加权 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 2.5 | 2.75 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.0 | **3.0** |

Overall 取偏保守值（3.0）：Excitement 分歧（R1=3.0 vs R2=2.5）和 Novelty 评判（R2 更严格且有理有据）倾向于 Findings 而非 Borderline Conference。
