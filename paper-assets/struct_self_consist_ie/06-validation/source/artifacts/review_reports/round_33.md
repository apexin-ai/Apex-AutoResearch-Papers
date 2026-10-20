---
round: 33
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T08:21:56.027588+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER

**项目**: struct_self_consist_ie
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿轮次**: Round 33 (fresh)
**Reviewer**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作质量)
**日期**: 2026-05-22

---

## Summary

本文系统性研究 test-time compute scaling（self-consistency）在 NER 任务上的失败原因。作者提出"correlation-selection gap"概念——QE 信号在 population level 能有效预测输出质量（Spearman ρ 达 0.45，AUROC 达 0.82），但 instance-level 选择几乎无效（多数数据集 <1 pp）。通过四阶段诊断级联（degeneracy → oracle headroom → LP compression → selection alignment α→0）定位失败机制。Entity-level construction 在 Few-NERD 上获得 +1.40 pp（Holm p_adj=0.006），但在其他数据集上效果有限或无效。实验覆盖 4 个 NER 数据集、4 个模型家族（3B–72B + GPT-5.5）、RE 和 SQL 扩展。

---

## Strengths

**S1. 重要且诚实的 negative result。** 系统性证明 self-consistency 在 NER 上失败并诊断失败原因，填补了 test-time scaling 文献在结构化预测方面的空白。论文坦诚报告 entity construction 在 CoNLL 无效、SciERC 增益微弱，诚实度在当前 NLP 文献中突出。[R1, R2 共识]

**S2. 出色的统计严谨性。** 57 项统计检验完整枚举（Table 12 Holm-Bonferroni）、paired bootstrap CI、permutation test、TOST 等效性检验、post-hoc power analysis（Table 58）。这种透明度在同类工作中罕见，直接回应了 ARR guidelines 中 R1（inappropriate statistics）和 R5（missing significance）的关切。[R1, R2 共识]

**S3. Correlation-selection gap 概念清晰且有迁移价值。** "QE 信号 population-level 有效但 instance-level 失效"的解耦不仅适用于 NER，对任何 set-valued structured output 的 test-time scaling 都有启示。Figure 1 直观传达核心洞见。[R1, R2 共识]

**S4. 实验覆盖全面。** 9 种聚合方法、5 种 QE 信号、temperature/N-scaling/cross-model/cross-dataset 鲁棒性分析、RE 和 SQL 扩展、4 个模型家族（Qwen3-8B/4B/14B、LLaMA-3.1-8B、Qwen2.5-72B zero-shot、GPT-5.5 zero-shot）、DeBERTa-v3 encoder verifier、47 页附录。[R1, R2 共识]

**S5. MBR 理论联系。** Proposition 1 和 Proposition 2 将 entity-level 聚合与 MBR decoding 理论框架对接，为实验发现提供形式化基础。[R1, R2 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

无。经交叉讨论，R1 和 R2 各自提出的 Must-Fix 问题均被对方提供了有效反驳或降级至 Should-Fix：
- R1-N1（θ_crit 过拟合）：R2 指出 θ_crit 来自 Corollary 1 理论推导而非 post-hoc fitting，16 个配置是验证而非拟合来源。→ **降级为 Should-Fix**
- R1-N2（binding constraint 叙事矛盾）：R2 指出论文原文明确写 "α→0, not degeneracy alone, is the binding constraint"，R1 的批评基于对摘要的部分误读。→ **降级为 Minor**
- R1-N3（entity construction 证据不足）：双方 AGREE 证据有限，但 R2 指出 construction 非核心贡献（占 ~0.5 页），论文已自我限定。→ **维持 Should-Fix**
- R2-N1（实验 setup 位置）：R1 指出 Section 2.3 已提供关键参数，这是 presentation 问题非技术缺陷。→ **降级为 Should-Fix**
- R2-N2（模型多样性不足）：R1 提供详细反驳——论文实际覆盖 4 个模型家族、3B–72B 跨度、开源/闭源、fine-tuned/zero-shot、decoder/encoder（DeBERTa）。R2 的"仅 2 个 8B 模型"描述不准确。→ **降级为 Should-Fix（主文应更显著 highlight 跨规模结果）**

### Should-Fix（影响评分但不一票否决）

**SF1. Entity construction 证据有限，需降低叙事权重。** [R1-N3, R2-W1 | 双方共识]
- 阈值 k per-dataset 优化，无部署策略
- Holm-Bonferroni 全局校正后 p_adj=0.055（边缘），多数 construction 结果不显著
- CoNLL 无增益，SciERC 增益微弱
- 与 Xie et al. (2023) entity voting 的差异阐述不充分
- **建议**：将 construction 定位为探索性结果而非核心贡献；增加与 Xie et al. 的显式对比

**SF2. "Diagnostic Framework" 定位需澄清。** [R2-W3 | 双方部分同意]
- 标题包装为 "framework" 但更接近分析方法论贡献
- 每一步需要 task-specific 判断，其他研究者难以直接"运行"该 cascade
- **建议**：在 Section 1 contributions 中显式区分 (1) diagnostic methodology, (2) formal characterization, (3) empirical findings

**SF3. Related Work (Section 8) 过于压缩。** [R2-W6 | 双方共识]
- ~15 行对横跨 SC/MBR/NER aggregation/uncertainty estimation 的论文不足
- MBR for structured NLP、LLM calibration、Yao et al. (2026)/Yun et al. (2025) concurrent works 讨论不充分
- **建议**：扩展至 20–25 行，从 Appendix ae (Table 66) 提炼关键对比点

**SF4. 实验 setup 位置可优化。** [R2-N1 | R1 降级]
- 完整训练细节（LoRA 配置、constrained decoding 等）到 Section 7.1 才出现
- **建议**：在 Section 2 末尾增加 1–2 段实验概览，保留 Section 7.1 为完整参考

**SF5. θ_crit=0.70 阈值需 sensitivity 分析。** [R1-N1 | R2 降级]
- 理论基础（Corollary 1）sound，但缺 held-out validation 和 sensitivity sweep
- **建议**：报告 θ∈[0.65, 0.75] 的敏感性；在 RE/SQL 配置上验证

**SF6. RE 和 SQL 扩展覆盖有限。** [R1-W4, R2 | 双方共识]
- RE 仅 SciERC RE (n=397, 40% zero-F1)，SQL 仅类比讨论
- **建议**：补充 1 个 RE 数据集或弱化 "across NER and RE" 泛化声明

**SF7. 模型多样性在主文中呈现不足。** [R2-N2 | R1 反驳后降级]
- 论文实际覆盖广泛（4 家族、3B–72B、GPT-5.5、DeBERTa），但主文对 72B/GPT-5.5/DeBERTa 的讨论偏简略，多数结果在附录中
- **建议**：在 Section 7 或 Section 9 更显著地 highlight 跨规模/跨类型的一致性发现

---

## Reviewer Consensus [AGREE]

1. **Correlation-selection gap 是一个有价值的新概念**，对社区理解 self-consistency 在结构化预测上的局限性有实质贡献
2. **统计方法论在同类工作中属上乘**，57 项检验完整枚举的透明度值得肯定
3. **Entity construction 作为 prescriptive contribution 证据有限**，但论文已诚实自我限定
4. **Related Work 需要扩展**
5. **RE/SQL 扩展覆盖不足以支撑泛化声明**
6. **论文对 negative results 的呈现诚实且充分**

## Reviewer Divergence [REBUT]

1. **θ_crit 的性质**：R1 认为 post-hoc fitting 风险高（Must-Fix），R2 反驳有理论推导支撑（Should-Fix）。**Director 判定：Should-Fix**——Corollary 1 提供了理论基础，但缺 sensitivity 分析。
2. **"Binding constraint" 叙事**：R1 认为摘要 misleading（Must-Fix），R2 指出原文已明确 "α→0, not degeneracy alone"（Minor）。**Director 判定：Minor**——论文叙事基本准确，R1 的批评部分基于误读，但摘要措辞可微调使 signal alignment 的瓶颈地位更突出。
3. **模型多样性**：R2 认为"仅 2 个 8B 模型"（Must-Fix），R1 提供详细反驳列出 4 个家族 + 完整跨度。**Director 判定：Should-Fix**——覆盖存在但主文呈现不足。
4. **9 节结构**：R2 认为过于碎片化，R1 认为各节各回答一个独立诊断问题，简洁是优点。**Director 判定：不构成显著弱点**——诊断级联结构有其逻辑。
5. **"reliably predict" 措辞**：R2 认为 ρ=0.45 不够"reliable"，R1 反驳 ρ²≠variance explained（Spearman vs Pearson）且 AUROC=0.82 支撑该表述。**Director 判定：Minor 措辞调整**——"effectively predict" 或 "meaningfully predict" 更安全。

---

## Questions（需作者澄清）

1. θ_crit=0.70 在 θ∈[0.65, 0.75] 范围内是否改变 Table 31 的结论？
2. Entity construction 阈值 k 在无标注验证数据的实际场景中如何选择？
3. GPT-5.5 的 10.1% parse failure 排除后，是否系统性偏移了 correlation-selection gap 估计？
4. 论文是否计划补充更多 RE 数据集以支撑泛化声明？

---

## Missing References

1. **Entity-level aggregation 先驱工作**：Xie et al. (2023) entity voting 需在 Section 6.1 做显式对比
2. **MBR for structured NLP 更广泛文献**：Eikema et al. (2025) 之外的结构化输出 MBR 应用
3. **LLM calibration 综述**：论文使用 ECE（Appendix c）但未在 Related Work 讨论 calibration 领域

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical / 3 warning / 27 info）。

**Warnings:**
1. **Pages 1–2 纯文本**：前 2 页为 Abstract + Introduction 连续文字，Figure 1 直到 page 3 才出现。建议考虑将 Figure 1 提前或加入 teaser figure。
2. **Pages 8–9 纯文本**：Related Work + Discussion + Limitations + Ethics 连续无 display item，阅读体验略单调。
3. **Page 24 大面积空白**：Appendix 文本末页仅 ~25% 填充，page break 控制不佳。

**Positive:**
- 主文 8 display items / 8 pages，密度合理
- 所有 float 位置合理，无漂移
- 公式渲染全部正确
- 无 margin 溢出
- 符合 EMNLP 2026 8 页限制
- Figure 1 色彩对比存在轻微色盲友好性问题（红-绿），建议改用 Okabe-Ito 色板

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

**置信度: 4/5**

**理由：**

这是一篇扎实的诊断分析工作。"Correlation-selection gap"概念清晰且有迁移价值，统计严谨度在 NLP 论文中属上乘，negative results 的诚实呈现值得肯定。实验覆盖面广（4 个 NER 数据集、4 个模型家族、3B–72B 跨度、9 种方法）。

但论文的核心局限在于 prescriptive contribution 薄弱：entity-level construction 仅在 Few-NERD 上有明确正向效果（+1.40 pp, Holm p_adj=0.006），CoNLL 无增益，SciERC 增益微弱且未通过多重校正。这使论文本质上是一篇 negative result + 诊断分析工作，方法论增量有限。Related Work 过于压缩（~15 行），"framework"定位与实际分析贡献之间存在张力。

**无 Must-Fix 级别的技术缺陷**——经交叉讨论，所有 critical 问题均被降级或解决。7 个 Should-Fix 问题（entity construction 定位、framework 澄清、Related Work 扩展、实验 setup 前置、θ_crit sensitivity、RE/SQL 覆盖、模型多样性呈现）均可在修改周期内解决。

当前状态下 Findings 是安全着陆点。若能解决 SF1（entity construction 重新定位）、SF3（Related Work 扩展）和 SF7（主文 highlight 跨规模结果），可提升至 Conference 水平。

---

## Detailed Comments

### Section 1 (Introduction)
- "α→0, not degeneracy alone, is the binding constraint" 措辞基本准确但可更精确——建议改为 "near-zero selection alignment (α→0), jointly with degeneracy, constitutes the binding constraint"
- Contributions 列表应显式区分 diagnostic methodology / formal characterization / empirical findings 三类贡献

### Section 2 (Diagnostic Framework)
- 建议在 Section 2 末尾增加 1–2 段实验概览（数据集、模型、N、T 的概要）
- "capability ceiling" 定义清晰，但与 "correlation-selection gap" 的关系可更显式说明

### Section 3 (Self-Verification)
- ESJ AUROC=0.512 是重要的 negative finding，呈现简洁有效
- Hidden-state probe 的 LODO transfer 下降（0.56–0.67）是关键发现，支持 dataset-specific 结论

### Section 4 (Single-Signal Selection)
- Table 1 和 Figure 2 有效传达 gap
- "Diagnostic cascade" 四阶段逻辑清晰，但阶段间交互（R²<0）应在主文更显著呈现

### Section 5 (Adaptive Methods)
- Table 2 的 9 方法综述是有价值的参考
- Cross-model ensemble (+0.42 pp) 作为唯一 unconditional positive result，可在讨论中更突出

### Section 6 (Theory)
- Proposition 1 形式化了直观观察——作为诊断工具有价值但不构成独立理论贡献
- θ_crit=0.70 需 sensitivity 分析（θ∈[0.65, 0.75]）

### Section 7 (Experiments)
- 7.1 Experimental Setup 应前置或在 Section 2 提供概览
- 7.3 Few-NERD cross-dataset contrast 是论文亮点，LP selection +1.39 pp (p<0.001) 是最强正向结果
- 7.5 Prescriptive Results 应降低叙事权重，明确为探索性结果

### Section 8 (Related Work)
- 需要从 ~15 行扩展至 20–25 行
- 补充 MBR for structured NLP、LLM calibration 讨论
- 将 Yao/Yun concurrent works 的讨论从 Introduction 深化到 Related Work

### Section 9 (Discussion)
- 过于简短（约 5 行），建议扩展讨论 practical implications 和 future directions

### Limitations
- 覆盖面广且诚实，篇幅适中，符合 EMNLP 2026 规范

### Appendix
- 47 页附录详尽程度在同类工作中罕见，统计枚举透明度出色
- Table 66 (differentiation matrix) 应在主文 Section 8 中引用
- Appendix af (Anticipated Objections) 内容有用但可能给 reviewer 留下防御性印象