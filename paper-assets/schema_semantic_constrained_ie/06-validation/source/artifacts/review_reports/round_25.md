---
round: 25
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T10:49:48.801958+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 25 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**Target Venue**: EMNLP 2026 (ARR May cycle)
**Reviewers**: R1（方法严谨性+实验设计）、R2（新颖性+完整性+写作质量）
**轮次**: Round 1（fresh review，无上轮记忆）
**收敛**: 1 轮交叉后收敛，5 个完全共识问题，1 个分歧已解决

---

## Summary

OntoCoDec 提出将 IE 本体编译为两层 token-level 解码约束的框架：grammar layer 通过 XGrammar 保证 JSON 结构和词汇约束（Level 1: context-free），semantic layer 通过运行时 entity registry + dynamic logit masking 保证 domain/range 类型约束（Level 2: prefix-decidable with state）。核心理论贡献是 Proposition 1（pumping lemma 证明 domain/range 约束超出 CFG 表达能力）。实验覆盖 3 个 8B 模型族（Qwen3-8B, Llama-3.1-8B, Mistral-7B）× 2 个 RE 数据集（SciERC, DocRED），加 1 个 70B 单模型族验证（Llama-3.1-70B AWQ INT4）和 WikiEvents event extraction pilot（n=20）。在 zero-shot 和 LoRA fine-tuning 两种设置下，DR 违规几乎完全消除（fine-tuned ≤0.09%），但引入 CF 违规作为 trade-off。

---

## Strengths

**S1.** [共识] 实验设计极为扎实——本文最大亮点。五路 ablation on SciERC（Table 1: unconstrained / grammar-only / GCD-equiv / semantic-only / S1 / S2）清晰解剖了每层的独立与交互贡献。GCD-equiv 通过 vLLM `guided_json` 外部验证（Appendix S）增强可信度。跨模型验证（3 tokenizer families × 2 datasets）、fine-tuning composability（Table 2, Bonferroni-corrected CIs）、beam search sweep（k∈{1,2,4,8}）、downstream impact 分析（仅 0.49% blocked triples match gold labels）均展现了罕见的实验严谨性。

**S2.** [共识] 统计方法严谨。Bootstrap CI（10,000 iterations）、Bonferroni correction for multiple comparisons、Cohen's d effect sizes 的使用在 NLP 论文中不常见。per-configuration corrected p-values 的诚实报告（如 SciERC p_adj=1.00）值得肯定。

**S3.** [共识] Limitations 的透明度异常高。三段式 Limitations 覆盖 constraint scope / evaluation coverage / engineering considerations，主动报告了 CF trade-off、n=3 tightness 相关性不显著、WikiEvents n=20 统计效力不足、70B 单一模型族限制等。这种自我批评的态度显著提高了论文可信度。

**S4.** [共识] 工程完整性强。31 页 Appendix 覆盖了几乎所有可预见的质疑：causal tracing、cascade error analysis、order invariance、prompt sensitivity、document length effect、quantization robustness、sampling robustness。跨 3 个 tokenizer family 的 continuation masking 验证了 tokenizer-agnostic 设计。Grammar-first fallback 机制优先保证 JSON 结构完整性的设计哲学符合实际部署需求。

**S5.** [共识] 问题定义精准且有实际意义。论文清晰识别了 grammar-constrained decoding 的能力边界——无法执行跨字段 domain/range 类型约束——并给出了形式化论证。15-18% 的 baseline violation rate 证实了问题的实际严重性。

**S6.** [R2] 写作质量高。8 页正文在高信息密度下保持了良好的逻辑流；符号使用一致（DR/RV/ET/CF 始终如一）；Related Work 的三轴组织（constrained decoding / schema-aware IE / constraint enforcement in IE）清晰有效。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [Critical, 完全共识] **WikiEvents n=20 不足以支撑 "task generalization" contribution claim**
- §1 Contribution 2 将 WikiEvents pilot 列为贡献一部分："a preliminary n=20 event extraction pilot provides directional evidence of task generalization"。n=20, MDE≈±5.0pp 不构成 generalization 证据，属 feasibility demonstration 而非 validation。零样本 WikiEvents 评估（n=246, Table 47）验证了 EV/RoV 消除，有价值；但 fine-tuning composability 的 n=20 无法支撑有置信度的结论。
- **要求**: 从 Contribution 2 完全删除 WikiEvents 表述；§5.2 移至 Appendix 或正文仅保留 1 句 feasibility mention。

**MF2** [Critical, 完全共识] **GoLLIE 比较方法论不公平，但被用于定位论文差异化**
- Appendix S 对比 GoLLIE-7B zero-shot（5 predicted relations / 100 docs）vs. OntoCoDec LoRA+S1（~1100 predicted relations）。§6 引用此结论（"near-complete output suppression"）定位差异化，但实验条件不对等——GoLLIE 未在 SciERC 训练导致输出少，非方法内在差异。论文的"complementary"定位合理，但 Appendix S 的直接对比表支撑不了这个定位。
- **要求**: 删除 Appendix S 直接对比表，改为定性讨论；§6 删除或显著限定"near-complete output suppression"表述，并显著说明不可比原因。

### Should-Fix（影响评分但不一票否决）

**SF1** [Major, 完全共识] **κ-DR 相关性（n=3）在正文 §4 叙事权重过高**
- §4 "Constraint Tightness" 段为 κ 给出了独立定义式、三个 schema 的具体数值、p=0.138，Appendix 有独立 case study 和 Figure 3。叙事权重与 n=3 证据强度严重不匹配。κ 还是 confounded variable（entity type confusability 是 co-factor）。论文已标注"descriptive"但展示比重暗示 κ 有独立解释力。
- R1 初评 Critical，R2 交叉后建议降为 Major（因未列入 Contribution），Director 采纳 Major。
- **要求**: §4 Constraint Tightness 压缩为 1-2 句描述性观察，删除 p 值报告（n=3 的 p 值本身误导），详细分析移 Appendix。

**SF2** [Major, 完全共识] **Proposition 1 新颖性有限——formalizing known intuition**
- PDA 无法执行 random-access stack lookup 是形式语言理论基本知识。论文诚实称之为"formalizing a known intuition"（§1 C1），但仍列为三大贡献之首，§3 投入大量篇幅（proof sketch + engineering applicability + empirical observation）。Appendix O pumping lemma 证明正确但不深刻——构造了 copy-language 变体。Engineering applicability（DFA 6^17 states）比 Proposition 1 本身更有价值。
- **要求**: 降低 Proposition 1 展示权重——从 Contribution 首位降级，或将 engineering applicability 作为主要论述重心。

**SF3** [Major, 完全共识] **DR↔CF trade-off 在零样本场景下严重程度讨论不足**
- Zero-shot greedy S1: total violation 15.45%→10.83%（DR↓94% 但 CF 0.08%→9.90%），净降幅仅 30%。Abstract 突出 DR reduction 但 CF increase 叙事不对称。R2 补充：(1) Abstract 确实提及 zero-shot CF 可达 12%；(2) DR/CF 质性差异真实（DR 不可恢复 vs CF 可 post-hoc）；(3) 推荐配置 fine-tuned+beam 下 trade-off 很小。
- R1 初评 Critical，R2 交叉后提供 nuance 建议降为 Major，Director 采纳 Major。
- **要求**: Abstract framing 更对称地报告 DR reduction 和 CF increase；§7 Discussion 扩展 zero-shot CF 实际影响分析；明确推荐 beam k≥2 作为 zero-shot 部署配置。

**SF4** [Major, 完全共识] **70B 验证单一模型族但 Contribution 3 称"scale validation"**
- 所有 70B 实验仅 Llama-3.1-70B AWQ INT4，无 Qwen-72B/Mistral-Large，无 FP16 对比。Scale-dependent interaction（semantic-only 24%→84%）是否为 Llama-specific 未知。论文已标 "single-family" 但仍用"validation"一词。
- **要求**: Contribution 3 改"Preliminary 70B exploration"或"Single-model scale probe"，不用"validation"。

**SF5** [Major, R1 提出 R2 同意] **Scale-dependent layer interaction 缺乏因果解释**
- Semantic-only 在 8B 仅 24% DR reduction vs. 70B 达 84%，论文仅称"empirical observation"无因果解释。候选假设（vocabulary calibration / logit distribution / fallback 频率差异）均未讨论。现有数据（Appendix C fallback tracing）应可提供部分解释但未连接。
- **要求**: §3 或 §5 添加 1-2 句关于可能机制的讨论，至少分析 8B vs 70B semantic-only 下的 fallback 频率差异。

**SF6** [Major, R1 提出 R2 同意] **S1 vs S2 对比缺乏深入分析**
- S1 vs S2 差异未做统计检验。70B 下 S2 R-F1 降低 8.45pp 的具体原因未分析。S2 何时优于 S1 无指导。R2 注：S1/S2 是次要叙事，Major 但不影响接收。
- **要求**: 提供 S1 vs S2 paired bootstrap test；分析 70B S2 failure case；讨论 S2 推荐条件。

### Minor

**M1** [R1 提出 R2 rebut，R2 论点有效] Fine-tuning 仅验证 LoRA。R2 指出 full FT 已在 Appendix 验证，且 composability 机制上不依赖 fine-tuning 方法。Limitations 中 caveat 可适当加强。

---

## Reviewer Consensus（[AGREE] 标注）

以下问题两位 Reviewer 完全一致：

1. **WikiEvents n=20 从 Contribution 降级** — R1-W5 [Major] + R2-N1 [Critical]，R1 交叉 AGREE R2。升级为 Critical。
2. **GoLLIE 比较方法论不公平** — R2-N2 [Critical] + R1-W6 [Minor]，R1 交叉 AGREE R2 并补充 nuance。升级为 Critical。
3. **Proposition 1 新颖性有限** — R1-W1 [Major] + R2-W1 [Major]，双方交叉 AGREE。
4. **κ-DR 相关性叙事权重过高** — R1-N1 + R2-W4，双方交叉 AGREE。
5. **CF trade-off 讨论不足** — R1-N2 + R2-W3，双方交叉 AGREE（含 nuance）。
6. **70B 单一模型族 overclaim "validation"** — R2-W2 [Major]，R1 交叉 AGREE。
7. **Scale-dependent interaction 缺因果解释** — R1-W2 [Major]，R2 交叉 AGREE。
8. **S1 vs S2 分析不足** — R1-W4 [Major]，R2 交叉 AGREE。

## Reviewer Divergence（[REBUT] 标注）

**唯一分歧：LoRA-only composability**
- R1 认为仅验证 LoRA 是 Major 缺陷，composability claim 泛化性不足。
- R2 [REBUT]：Full fine-tuning 已在 Appendix 验证；composability 机制不依赖 fine-tuning 方法（runtime logit masking 对模型权重来源不可知）；不同 PEFT 方法改变权重不改变 logits 生成方式。
- **Director 裁定**：R2 的 rebut 有效。已验证两种 fine-tuning 方法（LoRA + full FT），且机制论证成立。降为 Minor，在 Limitations 加强 caveat 即可。

---

## Questions for Authors

**Q1.** Schema coverage gaps 占 fine-tuning residual DR 的 33%。当 training data 的 type pair 分布不覆盖所有合法 ontology pair 时，系统会 over-restrict。能否量化 SciERC 和 DocRED 的 schema 对 ground truth ontology 的覆盖率？是否考虑过基于 ontology hierarchy 构建 constraint？

**Q2.** Entity registry 的 first-seen semantics 在长文档中的行为如何？DocRED outlier 文档的 entity 数可达多少？registry 在 100+ entities 时是否有实测性能数据？

**Q3.** Continuation masking 对 morphologically similar types（如 Protein vs. Protein_Complex）的实际失败率？

**Q4.** 在 R-F1 仅 8-13% 的 zero-shot 设置中，violation reduction 的实际下游价值如何量化？

**Q5.** Proposition 1 是否已在其他文献中以类似形式出现过？与已有 cross-serial dependency 不可由 CFG 表达的结论的本质区别？

**Q6.** GoLLIE-7B 在 LoRA fine-tuning 后的 SciERC 表现如何？如果 GoLLIE fine-tuned 后输出量正常化但仍保持低 DR，则 OntoCoDec 的差异化需要重新评估。

**Q7.** Scale-dependent layer interaction（semantic-only 70B 84% vs. 8B 24%）是否有理论预期支持？70B 模型更好的 vocabulary calibration 是否解释了 semantic layer 的独立有效性？

---

## Missing References

论文对关键相关工作的覆盖充分。CRANE (Banerjee et al., 2025)、EnriCo (Zaratiana et al., 2024)、IterGen (Ugare et al., 2025)、SynCode、XGrammar、Outlines、SGLang、PICARD、KG-Trie、GoLLIE、KnowCoder、GCD、BoostCD 均已引用。

唯一建议：CRANE 仅在 Appendix B 讨论，但 S2 在 70B 下 R-F1 降低 8.45pp 与 CRANE 关于 constrained decoding 抑制 reasoning 的分析直接相关，应在主文 §3.4 或 §5 70B 段至少引用。

---

## External Review (Stanford Agentic Reviewer)

未配置。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时 ~4.5 分钟）

**Warnings (3)**:
1. 主文 8 页仅 3 个 display items（1 figure + 2 tables），对于实证型论文偏少（通常 5-8 个）。大量实验结果全部推入附录，审稿人在主文中缺乏足够的视觉锚点。建议将至少 1-2 个关键结果表或 ablation 图提至主文。
2. Method 段（§3.1-3.3）连续 2 页纯文本，无 figure/table/algorithm box 穿插。建议用 Algorithm 伪代码或流程图打断文字墙。
3. Related Work + Discussion/Conclusion 合占 1 页纯文本，无总结性图表辅助审稿人抓取核心 takeaway。

**Info (7)**:
- Table 35 红/绿对比对色盲用户不友好
- 末页内容填充约 60-65%
- Figure 1 内部标注文字偏小（约正文 60%）
- 多页附录堆叠 4 张表格，可考虑合并
- Table 1/2 格式专业（booktabs + 加粗最优值 + 小数位一致）✓
- Table 3 prompt 模板文字较小但可接受
- 附录 Figure 2/3/4 分辨率和轴标签清晰 ✓

---

## Overall Assessment

**Overall: 3.5 — Borderline Conference**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 4/5 | 3.75 |
| Excitement | 3/5 | 3/5 | 3.0 |
| Reproducibility | 4/5 | 4/5 | 4.0 |
| Confidence | 4/5 | 4/5 | 4.0 |
| **Overall** | **3.5** | **3.5** | **3.5** |

**判断依据**：论文解决了一个有实际意义的问题（LLM-based IE 中 15-18% 的本体违规率），提出了干净的两层架构，配有正确的理论证明和极其全面的消融实验。统计方法（bootstrap CI, Bonferroni, Cohen's d）在 NLP 论文中罕见且值得肯定。31 页 Appendix 和三段式 Limitations 的透明度是显著优势。

主要不足：(1) 核心技术新颖性中等——entity registry + dynamic masking 是现有 constrained decoding 的自然延伸，Proposition 1 是已知结论在 IE 场景的应用（Excitement 3/5）；(2) 两个关键实验证据有缺陷——WikiEvents n=20 不支撑 task generalization claim，GoLLIE 比较方法论不公平；(3) 零样本场景下 DR→CF trade-off 的净效果被叙事不对称地呈现。

**Findings vs. Conference 的关键判断维度**：论文的实验质量和透明度足以被 Findings 接收。是否能进入主会议取决于对"扎实的工程+实验贡献 vs. 有限的概念新颖性"的权衡。若 MF1（WikiEvents framing）和 MF2（GoLLIE 比较公平性）在 revision 中修复，且 SF2（Proposition 1 展示权重）和 SF3（CF trade-off 对称呈现）得到改善，评分有望上调至 3.5-4.0 区间。

---

## Detailed Comments

### §1 Introduction
- Contribution 1：Proposition 1 定位为"formalizing a known intuition"是诚实的，但列为首位贡献且 §3 篇幅过大，给人 substantial theoretical contribution 的印象。建议降级或重新排序。
- Contribution 2：WikiEvents 部分应完全删除。
- Contribution 3："Single-family scale validation"中"validation"应改为"exploration"或"probe"。
- "F1 41-47%"：Table 2 Qwen DocRED S1 R-F1=40.79%，低于 41%。修正为"R-F1 40-47%"。

### §3 Method
- Proposition 1 proof sketch 技术正确，但不深刻。Engineering applicability（DFA 6^17 states）比 Proposition 1 本身更 informative。
- §3.1 "100% preservation across all configurations"表述不清，建议改为"entity-before-relation ordering is maintained in all N documents across all configurations"。
- Continuation masking 设计合理，跨 3 个 tokenizer family 验证了 tokenizer-agnostic 性。

### §4 Constraint Composition
- Constraint Tightness 段落应压缩为 1-2 句。删除 p=0.138 报告（n=3 的 p 值本身误导）。κ 作为描述性工具仍有概念价值，但详细分析应在 Appendix。

### §5 Experiments
- 五路 ablation（Table 1）是论文最强的实验贡献。
- Cross-field violation analysis（§5.1）数据充分：cascade error 分解（7.3% cascade vs. 2.5× correct locks）是有力证据。
- Fine-tuning composability（Table 2）报告严谨。
- §5.2 WikiEvents：正文应压缩至 1 句或移至 Appendix。
- 70B results：scale-dependent interaction 需因果讨论；S2 在 70B 的降级应引用 CRANE。
- DocRED 使用 dev set 的说明应从 footnote 1 提升至 Setup 段正文。

### §6 Related Work
- 三轴组织有效。
- GoLLIE 段应删除或显著限定"near-complete output suppression"表述。
- CRANE 应在主文提及，不仅限于 Appendix B。

### §7 Discussion and Conclusion
- 目前约 0.5 页，过于压缩。需扩展：DR↔CF trade-off 实际影响、per-triple vs. global enforcement 路线图、schema evolution 考量。

### Limitations
- 三段式结构充分，覆盖面好。
- 建议加强 fine-tuning 方法泛化性的 caveat（不仅"other fine-tuning methods warrant further investigation"，应指出不同 PEFT 方法对 logit distribution 的影响可能不同）。
- 添加 schema evolution 对 empirical constraints 的影响讨论。

### Format Compliance (EMNLP 2026)
- ✅ 正文 8 页（§1-§7 在 pages 1-8）
- ✅ 匿名处理（Anonymous ACL submission，无身份泄露）
- ✅ Limitations section 存在且充分
- ✅ Ethics statement 存在
- ✅ References ACL natbib 格式
- ✅ \usepackage[review]{acl} 启用 review 模式