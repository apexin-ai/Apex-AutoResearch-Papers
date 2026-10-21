---
round: 8
review_mode: fresh
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-19T06:38:21.186793+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 8 (Fresh Review)

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成共识）

---

## Summary

本文提出 OntoCoDec，将 IE ontology schema 编译为两层 token-level 解码约束：grammar 层（XGrammar CFG）保证 JSON 结构和词汇有效性，semantic 层通过有状态 entity registry 和动态 logit masking 在生成时强制 domain/range type 约束。在 SciERC、DocRED（RE）和 WikiEvents（EE）上跨 4 个模型（Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.1-70B）评估。核心结果：与 LoRA fine-tuning 组合后 DR ≤ 0.20% 且 R-F1 波动 < 0.6pp（R-F1 40-46 部署级质量）；zero-shot 下 DR 降低 42-99%，cross-task 泛化到 EE 无需架构修改。

---

## Strengths

**S1. 问题定义清晰、有实际价值。** 系统量化了 LLM-based IE 中的 ontological type violations（SciERC 15.37%, DocRED 18.46%），并证明 fine-tuning 后仍有 1-2% 残留。四类 violation 分类体系（DR/RV/ET/CF）完整覆盖。[共识]

**S2. Two-layer enabling dependency 有充分实验支撑。** Semantic-only 仅降 DR 24%，加 grammar 层后达 94%（Table 1）。这不仅是设计选择，而是经验验证的架构需求，ablation 定量拆解有独立价值。[共识]

**S3. Fine-tuning composability 是最强贡献。** LoRA + S1 在 SciERC/DocRED 上 DR ≤ 0.20%, R-F1 ±0.6pp, CF ≤ 1.18%（Table 2）。在 deployment-grade 质量（R-F1 40-46）下近乎无损消除 type violations，有真实实用价值。[共识]

**S4. 实验覆盖面异常全面。** 3 数据集 × 4 模型（含 70B）× 多 decoding 策略（greedy/beam/sampling）× zero-shot 和 fine-tuned × 四向 ablation。Beam search 在 fine-tuned SciERC 上消除所有四类 violation（Appendix F）。Cross-task 泛化到 EE（WikiEvents, 56 event types, 80 roles）无需架构修改。[共识]

**S5. 对 limitations 的处理诚实透明。** CF↔DR trade-off 通过专门 fallback ablation 分析（Appendix B, Table 5），CF 分布的 Generic↔X 归因（Table 6）有说服力。论文没有隐藏 CF 上升事实。[共识]

**S6. 可复现性极佳。** 完整 LoRA 超参（Appendix G）、prompts（Appendix A）、硬件规格、软件版本、experiment IDs 均提供。承诺 acceptance 后开源。[共识, R2 给 5/5]

**S7. Pair-based sequential masking 的 non-rectangularity 分析。** §4 证明独立 domain/range 检查会过度放行 33-37% 虚假 type pairs（SciERC 0/7, DocRED 23/96 relations 是矩形），justifies sequential enforcement。[R1]

---

## Weaknesses

### Must-Fix（2 条）

**W1 [Must-Fix] Dual-factor 统计声明过强（n=4, p≈0.058）。** [R8-MF1, 共识]
§4 正文使用 "predicts the cross-dataset results"，§1 Contribution #1 使用 "rates are driven by constraint tightness rather than ontology scale"。R²=0.886 基于仅 4 个数据点（df=2, p≈0.058 不显著），Spearman ρ=-0.77 基于 n=6（低于 α=0.05 临界值 ~0.886）。Appendix 承认 "descriptive rather than confirmatory"，但主文措辞仍为因果性。此外，SciERC/DocRED baseline DR 相近（15.37% vs 18.46%）不能排除巧合。WikiEvents 有 245 个约束，完全可以计算 κ 并验证。
**修复建议**: (1) 降级主文措辞为 "correlates with" / "is associated with"；(2) 在 WikiEvents 上验证 κ 的预测力；(3) §1 C1 弱化 causal claim。

**W2 [Must-Fix] WikiEvents fine-tuning composability 仅 20 文档评估。** [R8-MF2, 共识]
§5.4 fine-tuning 段承认 "wide confidence intervals at this sample size"，但 Abstract 和 §1 C3 宣称 "Fine-tuning composability extends to EE" 没有任何 qualification。Trigger F1 shift -5.4pp 可能纯粹是噪声。Zero-shot EE 使用 246 个文档但 fine-tuning 仅 20 个，不对称未解释。
**修复建议**: (1) 扩展到 100+ 文档，或 (2) 在 Abstract/C3 中加上 "preliminary" / "on a small test set" 的 qualification 并报告 CI/p-value。

### Should-Fix（9 条）

**W3 [Should-Fix] 缺少与 schema-aware IE baseline 的直接实验对比。** [R8-SF1, R1 主张, R2 部分同意]
无 GoLLIE/KnowCoder/BoostCD/GCD 的实验数据。GCD 有隐式对比（Table 1 grammar-only = GCD ceiling, §5.1: "the ceiling of grammar-based decoding"），但应显式标注。论文声称与 training-based 方法互补（§6），但缺乏实验验证。
**修复建议**: (1) Table 1 grammar-only 行加注 "equivalent to GCD"；(2) 如有资源，在 GoLLIE + OntoCoDec 上验证互补性。

**W4 [Should-Fix] Abstract "DR drops by 42-99%" 可能误导。** [R8-SF2, 共识]
42% 对应 Mistral DocRED（57.42%→33.20%，仍残留 33% violations），论文自身定义为 "boundary condition"。混合报告给读者的印象偏向 99% 端。Abstract 整体信息密度过高（~15 个数字，~250 words 上限区域）。
**修复建议**: (1) 分开报告 calibrated models (76-99%) 和 boundary condition (42%)；(2) 精简 Abstract 到 3-4 个关键数字。

**W5 [Should-Fix] EE fine-tuned CF 率未报告。** [R8-SF3, 共识]
§5.4 报告 RoV→0% 和 AC≤0.8%，但遗漏 CF。Zero-shot EE 下 CF 高达 15-21%（Table 4），fine-tuning 后 CF 是否降低是关键问题。遗漏让人怀疑结果不理想。
**修复建议**: 补充 EE fine-tuned CF 数据。

**W6 [Should-Fix] DocRED beam search 仅 50 文档子集。** [R8-SF4, R1 主张, R2 认为 Minor]
SciERC beam search 使用完整 551 文档（确认），但 DocRED 仅 50 个匹配文档。50 docs 上 DR→0% 的 95% CI 上界约 5.8%（Clopper-Pearson）。方法论上 matched design 是合理的，但统计功效有限。
**修复建议**: 如有计算资源，扩展到 200+ 文档。

**W7 [Should-Fix] 约束表基于频率统计而非完整 ontology schema，设计决策未解释。** [R8-SF5, 共识]
Appendix B residual DR error analysis 指出 33% 残留来自 "schema coverage gaps"。SciERC/DocRED 均有完整 ontology 定义，为什么用 frequency-based 近似而非完整 schema？如果使用完整 schema 可消除这部分残留。
**修复建议**: 解释工程决策原因；如可行，使用完整 ontology schema 并报告改进。

**W8 [Should-Fix] Appendix Extended Related Work 中 AI 写作痕迹密集。** [R8-SF6, 共识]
-ing 分词短语结尾（", establishing...", ", demonstrating...", ", enabling..."）在 Appendix B 出现 10+ 次，", confirming" 模式在各附录中出现 14 次。正文相对干净，但附录在 ARR 审稿范围内。此问题在 R5-R7 中曾反复出现和修复，本轮在附录中再次复发。
**修复建议**: 全文 grep `", establishing"`, `", demonstrating"`, `", enabling"`, `", confirming"` 并逐一改写。

**W9 [Should-Fix] Zero-shot 主导叙事但 fine-tuning composability 才是最强结果。** [R8-SF7, R2 主张, R1 部分同意]
§5.1-5.4 主要内容是 zero-shot 结果（R-F1 2-8%），fine-tuning composability 作为补充段落出现。Zero-shot 下 total violation burden (DR+CF) 从 15.45% 降到 10.83%（SciERC），净减少仅 ~30%，远不如 "94% DR reduction" 标题数字。R1 反驳 DR 和 CF 不等权（DR=triple 不可用，CF=individually valid），但同意 presentation 应调整。
**修复建议**: 重构叙事以 fine-tuning composability 为主线，zero-shot 作为 robustness/generalization 补充。

### Minor（5 条）

**W10 [Minor] Contribution #3 和 #4 高度重叠。** [R8-M1]
均关于 constraint behavior across settings。建议合并为一条关于 composability 和 trade-off 分析的贡献。

**W11 [Minor] Table 3 Grammar-only 行 R-F1/E-F1 标粗叙事矛盾。** [R8-M2]
Caption "best per column" 技术正确，但 Full S1 才是推荐配置。视觉上可能误导。

**W12 [Minor] Bib 重复条目。** [R8-M3]
grammar_aligned_2024 和 park2024grammar 指向同一篇论文（Park et al., Grammar-Aligned Decoding, NeurIPS 2024）。不影响 PDF 输出但应清理。

**W13 [Minor] Limitations section 格式需改善。** [R8-M4]
当前是一个连续密集段落（~10 个 limitation points），需分成 3-4 个带标题的子段（如 Constraint Scope, Evaluation Coverage, Scalability）。

**W14 [Minor] Roth & Yih (2004) 应移入正文 §6。** [R8-M5]
IE 中 hard type constraints 的奠基性工作，当前仅在 Appendix B 讨论。

---

## Reviewer Consensus

以下问题两位 Reviewer 独立发现并达成 [AGREE] 共识：

1. **Dual-factor 统计声明过强** (R1-W1 = R2-W2): 两人均认为 n=4/6 不足以支撑 causal language，需降级措辞。
2. **WikiEvents FT 20 文档过小** (R1-W2 = R2-W5): 两人均认为 EE composability claim 统计支撑不足。
3. **Abstract "42-99%" 可能误导** (R1-W4 ⊂ R2-W6): 两人均认为 boundary condition 与 calibrated models 混合报告不当。
4. **EE fine-tuned CF 未报告** (R1-W5, R2 同意): 遗漏关键指标。
5. **AI 写作痕迹** (R2-W4, R1 同意): 附录需系统清理。
6. **约束表 coverage gap 未解释** (R1-W7, R2 同意): 设计决策需说明。

---

## Reviewer Divergence

1. **DR+CF 净变化解读**: R2 认为 zero-shot total burden 仅降 ~30%，R1 反驳 DR 和 CF 不等权（DR=triple 不可用，CF=individually valid, globally inconsistent）。**Director 判断**: R1 的区分有道理——DR 使 triple 完全不可用，CF 下每个 triple 仍有局部正确性。但 R2 的批评也合理：从下游应用角度（如 KG 构建），CF 同样需要解决。两者观点应在报告中并存。

2. **Abstract 数字密度**: R2 认为堆砌（~15 个数字），R1 认为问题在叙事结构而非数字数量。**Director 判断**: 两者不矛盾——减少数字并重构叙事是同一解决方案的两面。

3. **Novelty 严重程度**: R2 列为 Should-Fix（核心机制非新），R1 认为弱项但 ablation 有独立价值。**Director 判断**: 技术新颖性确实有限，但 IE-specific adaptations（dynamic registry, non-rectangular pair-based masking）和全面的实证验证提供了足够的增量。这是 "solid engineering + thorough evaluation" 类论文，而非 "algorithmic breakthrough" 类论文。EMNLP 对这类工作有一定接纳度。

---

## Questions

**Q1.** CF↔DR trade-off 的量化：在 zero-shot 下，total violation burden (DR+CF) 的净变化是多少？能否提供包含 DR 和 CF 的 Pareto 分析？[R2]

**Q2.** WikiEvents fine-tuning 为什么只在 20 文档上评估？是数据集 split 限制还是计算限制？[R1, R2]

**Q3.** 能否设想 single integrated layer 直接在 type-bearing positions 同时强制 vocabulary 和 domain/range constraints？与两层方案的 trade-off 是什么？[R2]

**Q4.** Constraint tightness (κ) 在 WikiEvents EE setting 中是否有类似预测力？论文未报告 WikiEvents 的 κ 值。[R2]

**Q5.** 如果使用完整 ontology schema（而非 frequency-based）构建约束表，能否消除 33% 的 coverage gap 残留？[R1, R2]

**Q6.** Full fine-tuning（非 LoRA）的结果如何？Appendix 提到 "untuned learning rate underperforms LoRA"——如果调优 LR，结果是否不同？[R1]

---

## Missing References

引用数量（~56 条）符合 EMNLP 长文标准。以下可选补充：
- **Hokamp & Liu (2017)**: Lexically Constrained Decoding — constrained decoding 早期基础 [R2]
- **DEGREE (Hsu et al., 2022)**: prompt-based event extraction，与 WikiEvents 评估相关 [R2]
- **Roth & Yih (2004)**: 建议从 Appendix 移入正文 §6 [R2]

---

## External Review (Stanford Agentic Reviewer)

外部审稿未配置（`external_review.paperreview_ai.enabled` 未在项目配置中找到），本轮未请求外部审稿。

---

## Overall Assessment

**Overall: 3.5 (Borderline Conference)**

**评分分布**: R1 = 3.5, R2 = 3.5（完全一致）

**置信度**: 4/5（两位 Reviewer 均熟悉 constrained decoding 和 information extraction 领域）

### 评分理由

**技术执行**: 论文技术上 sound，两层约束架构形式化清晰，ablation 设计全面，composability with fine-tuning 是有真实实用价值的结果（DR ≤0.20%, F1 neutral at R-F1 40-46）。可复现性接近完美。

**技术新颖性**: 核心 type→mask 范式在 code domain 已有充分先例（PICARD, Synchromesh, PLDI 2025）。IE-specific adaptations（dynamic entity registry, pair-based sequential masking, non-rectangular type signatures）是真实的工程贡献，但属于范式迁移而非算法创新。这是本文最大弱点。

**统计严谨性**: Dual-factor pattern 的因果性声明（n=4, p≈0.058）和 EE composability claim（n=20）的统计支撑不足。这两个问题可修复但需要严肃对待。

**叙事结构**: Zero-shot 主导叙事但 fine-tuning composability 才是最强结果。Abstract 信息密度过高。CF trade-off 使 zero-shot 故事远不如标题数字那样有说服力（total burden 仅降 ~30%）。

**写作质量**: 正文相对干净，但 Appendix 中 AI 写作痕迹密集（-ing phrases, ", confirming" pattern），可能影响审稿人信任。

### ARR 评分参照

按 EMNLP 2026 ARR 标准：3.5 = Borderline Conference。论文处于 Findings 和 Main Conference 之间。

### 提升路径（3.5 → 4.0 Conference 的条件）

1. **[Must-Fix]** 降级 dual-factor causal claims 或在 WikiEvents 上验证 κ
2. **[Must-Fix]** 扩大 WikiEvents FT test set 或显著弱化 EE composability claim
3. **[High Impact]** 重构叙事以 fine-tuning composability 为主线
4. **[High Impact]** 精简 Abstract（3-4 个关键数字）、分开报告 calibrated/boundary
5. **[Hygiene]** 清除 Appendix AI 写作痕迹
6. **[Nice-to-have]** 显式标注 GCD baseline、补充 EE fine-tuned CF

---

## Detailed Comments

### §1 Introduction
- C1 "driven by constraint tightness" 措辞过强，改为 "correlated with"
- C3 和 C4 高度重叠，建议合并为一条
- C3 EE composability claim 需加 qualification（"preliminary, on a 20-document test set"）

### §2 Background
- 形式化清晰，constraint tightness 定义合理
- "prefix-decidable" 的论证有说服力

### §3 Method
- Two-layer architecture 设计合理，enabling dependency 的 ablation 支撑充分
- Continuation masking 处理多 tokenizer 是有价值的工程贡献
- Grammar-first fallback 的 rationale 清楚（结构完整性 > type 正确性）

### §4 Constraint Composition
- Non-rectangularity 分析（0/7 SciERC, 23/96 DocRED 矩形）有说服力
- Dual-factor "predicts" 必须降级（见 W1）
- Composability with fine-tuning 段是最强内容，不应埋在 §4 末尾

### §5 Experiments
- Five-way ablation（Table 1）设计全面
- DocRED grammar-only DR 上升至 26.17% 是 insightful observation（暴露潜在 type 不兼容性）
- Cross-model 验证（3 models × 2 datasets）覆盖面广
- WikiEvents EE 泛化令人印象深刻（EV/RoV→0%，Entity F1: 0→12-18%）
- WikiEvents FT 20 文档是最薄弱环节（见 W2）
- 70B 结果（DR→0% on both datasets）进一步验证 cross-scale generalizability
- Beam search 在 fine-tuned SciERC 消除所有 violations 是强结果

### §6 Related Work
- 正文 Related Work 过于压缩（~半页），核心 positioning 依赖 Appendix
- 建议将 Roth & Yih (2004) 和 code-domain 区分从 Appendix 移入正文
- Appendix Extended Related Work 全面但 AI 写作痕迹需清理

### §7 Discussion and Conclusion
- 过度压缩（~6 行），对于一篇有丰富实验结论的论文，discussion 部分太薄
- CF "open challenge" 的表述诚实但缺乏具体路线图

### Limitations
- 内容实质性好（多个方面：CF, coverage gap, scalability, zero-shot scope, beam search, full FT）
- 格式需改善：一个密集段落 → 3-4 个带标题的子段

### Ethics Statement
- 存在且合适，无问题

### 格式合规
- ✅ ACL style template（`\usepackage[review]{acl}`）
- ✅ Anonymous（`\author{Anonymous ACL submission}`）
- ✅ Limitations section 存在且实质性
- ✅ Ethics Statement 存在
- ⚠️ 需确认正文 ≤8 页（未能编译 PDF 验证）
- ⚠️ Bib 重复条目需清理