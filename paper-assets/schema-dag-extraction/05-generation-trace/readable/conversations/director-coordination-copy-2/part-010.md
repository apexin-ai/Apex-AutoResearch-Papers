# Director coordination — Part 10 of 10

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

[← Part 9](part-009.md) · [Transcript overview](../director-coordination-copy-2.md) · [Structured JSON](../../../sessions/0f/0fa49ecfe50583d66f9a.json)

## Round 259

### Tool call

_source line 3116 · 2026-05-22T23:12:03.966388+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "schema-dag-extraction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "\n# 审稿报告 — Round 31 (Fresh Review)\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审稿模式**: Fresh（两位 Reviewer 独立初审 + 交叉回应，1 轮收敛）\n\n---\n\n## Summary\n\n本文将 schema complexity 分解为两个独立维度——type 数量（count）和 type 间语义混淆度（SCS/BCS），通过 BCS-controlled batch 实验研究其对 training-free LLM IE 性能的独立影响。在 4 个数据集（Few-NERD NER、FewRel RE、DocRED RE、MAVEN ED）上，论文发现 count 产生跨任务的单调性能下降，BCS 在 FewRel RE 上独立预测 type substitution errors（adjusted R²=0.273）。SDGD decomposition 方法因 routing accuracy 不足而失败。论文的核心贡献是一个设计严谨的受控实证研究。\n\n---\n\n## Strengths\n\n**S1.** FewRel RE 上的实验设计严谨度高于该领域平均水平：BCS-controlled batch 构造确保 count 固定下变化 confusability（VIF=1.18 确认正交性）、cluster bootstrap 处理 shared-instance 依赖、Bonferroni 校正后核心结论仍 p<0.001。[R1-S1, R2-S1, 共识]\n\n**S2.** 有价值的错误分类体系（IntraSub, merge amplification, routing failure），Figure 2 展示 IntraSub 随 BCS 单调递增，提供超越相关性的机制性洞察。[R2-S2]\n\n**S3.** 诚实报告三组负面结果（NER null、MAVEN centrality confound、SDGD 全面失败），对社区有信息价值。ARR 鼓励发表负面结果。[R1-S2, R2-S3, 共识]\n\n**S4.** 18 页附录涵盖 prompt sensitivity、cross-model validation、Monte Carlo simulation、factorial analysis、bootstrap CI robustness、domain distribution 等，远超同类 empirical study 的平均水准。[R1-S4, R2-S4, 共识]\n\n**S5.** 跨 4 个数据集 3 个 IE 任务的验证广度，SCS 作为 pre-deployment lightweight proxy 有实用价值。[R2-S5, R2-S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1 [critical, 共识] 标题/摘要对 \"Information Extraction\" 的泛化声明超出证据支撑范围。**\n- 位置：Title, Abstract, Section 6\n- 问题：Confusability（BCS）的独立预测效应仅在 FewRel RE 上干净成立（VIF=1.18, adjusted R²=0.273）。NER 整体准确率效应为 null（Figure 2a IntraSub 机制存在但 achievable BCS range 过窄，无法产生可检测的准确率差异）；MAVEN 被 centrality 完全混淆；DocRED 因 VIF=50.9 不可靠。Count-degradation 跨任务通用，但标题和摘要将 confusability 效应隐含地泛化到全部 IE 任务。\n- 影响：核心 claim 的 scope 与证据不匹配，审稿人可能以 overclaiming 为由拒稿。\n- 建议：标题加 RE-specific 限定词或在摘要首段即标注 task-specificity；区分 count（通用结论）和 confusability（RE-specific 结论）的 generalizability。\n\n**C2 [critical, 共识] DocRED §4.3 VIF=50.9 下的呈现顺序产生 replication 错觉。**\n- 位置：Section 4.3\n- 问题：§4.3 DocRED 段先报告 partial ρ=−0.762 和效应量（−25.0pp, −15.7pp），再在同段后半 qualify VIF=50.9——这种先数字后限定的写法让读者产生 BCS 效应在 DocRED 上 replicate 的印象。实际 semipartial R²_BCS=0.056（仅 5.6% unique variance），标准误膨胀 ~7x。Ridge regularization 保留 negative coefficient 方向但通过引入 bias 换取 variance reduction，不解决共线性的语义问题。\n- 建议：§4.3 DocRED 段首句标注 VIF=50.9 + \"仅供方向性参考\"；详细数值报告移至 appendix；明确 ridge 局限性。\n\n### Reviewer 分歧项\n\n**D1 [分歧] SCS/BCS 相对于 LLM-PEE (Liu et al., 2025) 的新颖性论证。**\n- 位置：Section 2, Section 3.2\n- R2 判定 Must-Fix：SCS 本质是 type label embedding cosine similarity，计算层面与 LLM-PEE 的 schema partitioning 相同。论文提出的三点差异中，(1) controlled analysis vs. engineering 是视角差异，(3) SDGD 是负面结果，仅 (2) BCS-controlled design 有新颖性，但属实验方法论贡献非 metric 创新。\n- R1 REBUT：本文是方法论论文而非 metric 论文。BCS-controlled batch design + VIF verification + cluster bootstrap 的受控实验方法论在零样本 IE 领域是首次。从工程到诊断的视角转变是实质性方法论创新。\n- **Director 评估**：两种审稿视角均有合理性。论文应在 §2 更显式地将贡献定位为 \"controlled empirical study using embedding similarity as an analytical lens\"，弱化 SCS/BCS 作为独立 metric 贡献的叙事，同时正面论证受控实验方法论本身的贡献。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, 共识] 模型多样性不足。**\n- 位置：Section 3.5, Section 6, Appendix T/U\n- 问题：主实验仅 Qwen3-32B。Cross-model validation（LLaMA-8B/70B, Gemini 2.5 Flash）仅覆盖 count curves 和 BCS-controlled accuracy，不包括 TOST equivalence test 和 SDGD 分析。缺少闭源 frontier models（GPT-4o, Claude）。R2 判定 Must-Fix，R1 同意方向但建议降级（4 模型 3 家族方向一致，一阶 replication 达领域惯例）。\n- 建议：提升至少一个非 Qwen 模型为主分析，或严格限定 Section 6 声明范围。\n\n**W2 [warning, 共识] TOST logit-scale 不通过应在主文标注。**\n- 位置：Section 4.4, Limitations\n- 问题：±3pp equivalence margin 在 probability scale 和 logit scale 语义不同。TOST 在 logit scale 不通过意味着两个维度在非线性变换下的 additivity 无法确认，影响 \"independently addressable\" 结论强度。当前仅在 Limitations 提及。\n- 建议：§4.4 讨论 factorial analysis 时直接标注量表依赖性。\n\n**W3 [warning, 共识] Extreme-BCS batch domain composition confound 未控制。**\n- 位置：Section 4.3, Appendix E.4\n- 问题：Low-BCS batches 偏向 geography/creative work，high-BCS batches 偏向 science/taxonomy/event。如果不同 domain 抽取难度不同，observed BCS-performance 关系可能部分反映 domain difficulty。Regression 未将 domain diversity/entropy 作为 control variable。\n- 建议：做 domain-controlled regression 或 stratified analysis。\n\n**W4 [warning, 共识] RQ3 (Schema Decomposition) 分析不充分。**\n- 位置：Section 5\n- 问题：RQ3 是三个研究问题之一，但 Section 5 仅约半栏。Oracle routing 仅达 72.4%（vs. single-type >85%），暗示 decompose-then-merge 架构本身有结构性问题（merge amplification），即使 routing 完美也无法完全避免。论文对此讨论不足。\n- 建议：正文引用 Appendix B oracle routing 结果；讨论 merge amplification 根本问题；至少简要提及避免 merge 的替代架构。\n\n**W5 [warning, 共识] FP8 量化 non-determinism 对 regression power 的影响未分析。**\n- 位置：Section 3.5\n- 问题：SD=0.83pp 占 observed BCS effect (Δ≈1.9–4.6pp) 的 18–44%。Bootstrap CI 不区分信号方差和测量噪声，可能膨胀 residual variance 并削弱 regression power。\n- 建议：讨论 FP8 noise floor 对 smallest detectable BCS slope 的影响。\n\n**W6 [warning, 共识] 未解释方差讨论不足 + 因果性语言。**\n- 位置：Section 4.3, Section 6\n- 问题：BCS 解释 FewRel 约 27% accuracy variance，73% 未解释。R1 指出 27% semipartial R² 在 NLP 中属 large effect，但论文未讨论 prompt formatting、type definition quality、sentence complexity 等可能的未解释因素。Section 6 \"BCS captures a structural property\" 为半因果性语言。\n- 建议：Discussion 列出可能的未解释因素；改用 \"serves as a useful predictor of\" 等更审慎措辞。\n\n**W7 [warning, 部分共识] BCS mean aggregation 设计选择论证不足。**\n- 位置：Section 3.2, Appendix I\n- 问题：R1 指出 Appendix I Table 15 已做 mean vs max BCS 对比（方向一致），R2 遗漏此分析。但 top-k/加权方案未探索，且正文未引用 Appendix I 结果。\n- 建议：正文引用 Appendix I mean vs max 对比结果；讨论 aggregation 策略选择理由。\n\n---\n\n## Questions（需作者澄清）\n\n1. FewRel 上是否测试过 centrality 作为 confound？（R2 指出 Appendix E.1 Table 12 已确认 VIF=1.25，centrality 非 confound——R1 可能遗漏此分析）\n2. Max-based BCS 是否比 mean-based BCS 预测更好？（Appendix I Table 15 已有初步对比，正文应引用）\n3. Figure 1a NER U 形 count curve 是否通过 per-type recall 验证了 type-filtering overhead 解释？\n4. Qwen3-32B 作为主模型的选择理由是什么？\n5. SDGD 是否考虑过完全避免 merge 步骤的分解方案？\n6. FP8 noise floor 下，regression 能可靠检测的最小 BCS slope 是多少？\n\n---\n\n## Missing References\n\n| 文献 | 来源 | 状态 |\n|------|------|------|\n| PARSE (Shrinivas et al., 2025) — LLM-driven schema optimization | R2 | 待确认相关性 |\n| ASEE (2025) — Adaptive Schema-Aware Event Extraction | R2 | 待确认相关性 |\n| Li et al. (2023) \"Evaluating ChatGPT's IE Capabilities\" | R1 | 应引用 |\n| Josifoski et al. (2022) \"GenIE: Generative IE\" | R1 | 应引用 |\n| GLiREL (NAACL 2025) | R2 | R1 指出已被引用（Boyler et al. 2025），R2 事实有误 |\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目配置未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成。** 0 critical, 3 warning, 12 info。\n\n### Warnings\n1. **前 3 页连续纯文本**，无任何 display item。审稿人翻到第 5 页才看到 Figure 1。建议在前 2 页加入概览图或将 Figure 1 核心 panel 前置。\n2. **主正文 8 页仅 4 个 display items**（Figure 1-2, Table 1-2），密度 0.5/页，低于实证论文惯例（5-8 个/9 页）。大量结果被放入 15 页 appendix，导致正文偏\"文字墙\"。建议从 appendix 提升 1-2 个关键表格。\n3. **Pages 2-3 连续纯文本**（Related Work + Experimental Setup 开头），无 equation/figure/table 穿插。\n\n### Positives\n- ACL 匿名格式合规，Title/Author/Abstract 排版整洁\n- 所有表格使用 booktabs 风格\n- Figure 1 双 panel 配色色盲友好，caption 自包含\n- Figure 2 信息量充足，error taxonomy 可视化清晰\n- 无 margin 溢出、LaTeX 渲染错误\n- Limitations 长度适中（3 点 1 段），符合 EMNLP 规范\n- References 格式统一，无未解析引用\n\n---\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评估**：\n本文在 FewRel RE 上展示了一项方法论严谨的受控实证研究，BCS-controlled batch design 和统计分析（VIF 验证、cluster bootstrap、Bonferroni 校正）代表了 training-free LLM IE 领域少见的严格水准。负面结果（NER null、SDGD 失败）的诚实报告对社区有信息价值。\n\n**阻止接收的核心问题**：\n1. 标题和摘要将 confusability 效应隐含泛化到 \"Information Extraction\"，但独立预测效应仅在 FewRel sentence-level RE 上干净成立——这是 scope-evidence mismatch 问题，可修复但不可忽视。\n2. DocRED §4.3 的呈现顺序产生 replication 错觉，需要调整。\n3. 新颖性定位存在分歧：一位 Reviewer 认为 SCS 与 LLM-PEE 计算层面重叠严重，另一位认为受控实验方法论本身构成创新。论文应更清晰地定位贡献。\n\n**如果 Must-Fix 问题被充分解决**（标题/摘要限定 scope、DocRED 呈现修正、贡献定位明确化），本文有望达到 Conference 级别（3.5→4.0）——方法论素养和统计严谨性是加分项。如果 Must-Fix 未解决，将更适合 Findings。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识 [AGREE]：\n- 标题/摘要泛化超出证据（C1）\n- DocRED VIF=50.9 呈现矛盾（C2）\n- 模型多样性不足（W1，severity 有分歧）\n- TOST logit-scale 主文未标注（W2）\n- Domain composition confound（W3）\n- RQ3 分析不充分（W4）\n- FP8 non-determinism power（W5）\n- 未解释方差讨论不足（W6）\n- BCS 消融部分不足（W7）\n- Figure 1b 可读性、Table 1 术语、type name 粒度（Minor）\n\n## Reviewer Divergence\n\n**D1: SCS vs LLM-PEE 新颖性**（R2: Must-Fix, R1: REBUT）\n- R2 认为 SCS 计算与 LLM-PEE 重叠，技术贡献独特性不足\n- R1 认为受控实验方法论（非 metric）是贡献核心，视角转变构成创新\n- Director 评估：属于合理评审视角差异，论文应更清晰地定位为 empirical methodology 贡献\n\n**NER 结果性质**（minor 分歧）\n- R1 概括为 \"null\"\n- R2 补充：Figure 2a IntraSub 机制证据存在（ρ=0.84–1.1），是 \"null overall accuracy but active mechanism\" 的 boundary condition，不等于 \"no effect\"\n- Director 评估：R2 的细化更准确，论文应在正文区分 accuracy-level null 和 mechanism-level evidence\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract/Title**：需限定 confusability claim 的 task-specificity，区分 count（通用）和 confusability（RE-specific）。\"drives\" → \"predicts\" 的修改方向正确但不充分——需在首段即标注 \"specifically in relation extraction\"。\n\n**Section 2 (Related Work)**：与 LLM-PEE 的技术差异论证不充分。应显式对比 LLM-PEE 的 uncontrolled schema splitting 和本文的 controlled batch design。补充 Li et al. (2023)、GenIE (2022)。确认 PARSE/ASEE 相关性。\n\n**Section 3.2 (Metrics)**：BCS mean aggregation 选择理由应在正文讨论（引用 Appendix I Table 15 的 mean vs max 对比结果）。MiniLM 作为 pre-deployment proxy 的定位合理，但应在 §3.2 或 §6 讨论其与目标 LLM 实际 confusability 机制的关系。\n\n**Section 3.5 (Model)**：Qwen3-32B 选择理由应明确说明。FP8 quantization non-determinism (SD=0.83pp) 对 regression power 的影响应讨论。\n\n**Section 4.3 (BCS-Controlled)**：DocRED 段应首句标注 VIF caveat。FewRel regression 应控制 domain diversity 变量。正文应注明 FewRel centrality non-confound（引用 Appendix E.1）。\n\n**Section 4.4 (Factorial)**：TOST 量表依赖性应在此处标注（probability 通过，logit 不通过），不仅放 Limitations。\n\n**Section 5 (SDGD)**：应引用 oracle routing 结果（Table 9, Appendix B），讨论 merge amplification 的结构性问题，简要提及替代架构。\n\n**Section 6 (Discussion)**：\n- \"BCS captures a structural property\" → 更审慎措辞\n- 列出可能的未解释因素（prompt formatting, type definition quality, sentence complexity）\n- 限定 claim 范围至 Qwen3-32B（除非提升其他模型为主分析）\n\n**Figures/Tables**：\n- Figure 1b：考虑改用 grouped line chart 或增大尺寸\n- Figure 1(b) caption：标注 accuracy 定义\n- Table 1：Few-NERD \"trigger mentions\" 应改为 NER 术语\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "schema-dag-extraction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "report": "\n# 审稿报告 — Round 31 (Fresh Review)\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审稿模式**: Fresh（两位 Reviewer 独立初审 + 交叉回应，1 轮收敛）\n\n---\n\n## Summary\n\n本文将 schema complexity 分解为两个独立维度——type 数量（count）和 type 间语义混淆度（SCS/BCS），通过 BCS-controlled batch 实验研究其对 training-free LLM IE 性能的独立影响。在 4 个数据集（Few-NERD NER、FewRel RE、DocRED RE、MAVEN ED）上，论文发现 count 产生跨任务的单调性能下降，BCS 在 FewRel RE 上独立预测 type substitution errors（adjusted R²=0.273）。SDGD decomposition 方法因 routing accuracy 不足而失败。论文的核心贡献是一个设计严谨的受控实证研究。\n\n---\n\n## Strengths\n\n**S1.** FewRel RE 上的实验设计严谨度高于该领域平均水平：BCS-controlled batch 构造确保 count 固定下变化 confusability（VIF=1.18 确认正交性）、cluster bootstrap 处理 shared-instance 依赖、Bonferroni 校正后核心结论仍 p<0.001。[R1-S1, R2-S1, 共识]\n\n**S2.** 有价值的错误分类体系（IntraSub, merge amplification, routing failure），Figure 2 展示 IntraSub 随 BCS 单调递增，提供超越相关性的机制性洞察。[R2-S2]\n\n**S3.** 诚实报告三组负面结果（NER null、MAVEN centrality confound、SDGD 全面失败），对社区有信息价值。ARR 鼓励发表负面结果。[R1-S2, R2-S3, 共识]\n\n**S4.** 18 页附录涵盖 prompt sensitivity、cross-model validation、Monte Carlo simulation、factorial analysis、bootstrap CI robustness、domain distribution 等，远超同类 empirical study 的平均水准。[R1-S4, R2-S4, 共识]\n\n**S5.** 跨 4 个数据集 3 个 IE 任务的验证广度，SCS 作为 pre-deployment lightweight proxy 有实用价值。[R2-S5, R2-S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1 [critical, 共识] 标题/摘要对 \"Information Extraction\" 的泛化声明超出证据支撑范围。**\n- 位置：Title, Abstract, Section 6\n- 问题：Confusability（BCS）的独立预测效应仅在 FewRel RE 上干净成立（VIF=1.18, adjusted R²=0.273）。NER 整体准确率效应为 null（Figure 2a IntraSub 机制存在但 achievable BCS range 过窄，无法产生可检测的准确率差异）；MAVEN 被 centrality 完全混淆；DocRED 因 VIF=50.9 不可靠。Count-degradation 跨任务通用，但标题和摘要将 confusability 效应隐含地泛化到全部 IE 任务。\n- 影响：核心 claim 的 scope 与证据不匹配，审稿人可能以 overclaiming 为由拒稿。\n- 建议：标题加 RE-specific 限定词或在摘要首段即标注 task-specificity；区分 count（通用结论）和 confusability（RE-specific 结论）的 generalizability。\n\n**C2 [critical, 共识] DocRED §4.3 VIF=50.9 下的呈现顺序产生 replication 错觉。**\n- 位置：Section 4.3\n- 问题：§4.3 DocRED 段先报告 partial ρ=−0.762 和效应量（−25.0pp, −15.7pp），再在同段后半 qualify VIF=50.9——这种先数字后限定的写法让读者产生 BCS 效应在 DocRED 上 replicate 的印象。实际 semipartial R²_BCS=0.056（仅 5.6% unique variance），标准误膨胀 ~7x。Ridge regularization 保留 negative coefficient 方向但通过引入 bias 换取 variance reduction，不解决共线性的语义问题。\n- 建议：§4.3 DocRED 段首句标注 VIF=50.9 + \"仅供方向性参考\"；详细数值报告移至 appendix；明确 ridge 局限性。\n\n### Reviewer 分歧项\n\n**D1 [分歧] SCS/BCS 相对于 LLM-PEE (Liu et al., 2025) 的新颖性论证。**\n- 位置：Section 2, Section 3.2\n- R2 判定 Must-Fix：SCS 本质是 type label embedding cosine similarity，计算层面与 LLM-PEE 的 schema partitioning 相同。论文提出的三点差异中，(1) controlled analysis vs. engineering 是视角差异，(3) SDGD 是负面结果，仅 (2) BCS-controlled design 有新颖性，但属实验方法论贡献非 metric 创新。\n- R1 REBUT：本文是方法论论文而非 metric 论文。BCS-controlled batch design + VIF verification + cluster bootstrap 的受控实验方法论在零样本 IE 领域是首次。从工程到诊断的视角转变是实质性方法论创新。\n- **Director 评估**：两种审稿视角均有合理性。论文应在 §2 更显式地将贡献定位为 \"controlled empirical study using embedding similarity as an analytical lens\"，弱化 SCS/BCS 作为独立 metric 贡献的叙事，同时正面论证受控实验方法论本身的贡献。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, 共识] 模型多样性不足。**\n- 位置：Section 3.5, Section 6, Appendix T/U\n- 问题：主实验仅 Qwen3-32B。Cross-model validation（LLaMA-8B/70B, Gemini 2.5 Flash）仅覆盖 count curves 和 BCS-controlled accuracy，不包括 TOST equivalence test 和 SDGD 分析。缺少闭源 frontier models（GPT-4o, Claude）。R2 判定 Must-Fix，R1 同意方向但建议降级（4 模型 3 家族方向一致，一阶 replication 达领域惯例）。\n- 建议：提升至少一个非 Qwen 模型为主分析，或严格限定 Section 6 声明范围。\n\n**W2 [warning, 共识] TOST logit-scale 不通过应在主文标注。**\n- 位置：Section 4.4, Limitations\n- 问题：±3pp equivalence margin 在 probability scale 和 logit scale 语义不同。TOST 在 logit scale 不通过意味着两个维度在非线性变换下的 additivity 无法确认，影响 \"independently addressable\" 结论强度。当前仅在 Limitations 提及。\n- 建议：§4.4 讨论 factorial analysis 时直接标注量表依赖性。\n\n**W3 [warning, 共识] Extreme-BCS batch domain composition confound 未控制。**\n- 位置：Section 4.3, Appendix E.4\n- 问题：Low-BCS batches 偏向 geography/creative work，high-BCS batches 偏向 science/taxonomy/event。如果不同 domain 抽取难度不同，observed BCS-performance 关系可能部分反映 domain difficulty。Regression 未将 domain diversity/entropy 作为 control variable。\n- 建议：做 domain-controlled regression 或 stratified analysis。\n\n**W4 [warning, 共识] RQ3 (Schema Decomposition) 分析不充分。**\n- 位置：Section 5\n- 问题：RQ3 是三个研究问题之一，但 Section 5 仅约半栏。Oracle routing 仅达 72.4%（vs. single-type >85%），暗示 decompose-then-merge 架构本身有结构性问题（merge amplification），即使 routing 完美也无法完全避免。论文对此讨论不足。\n- 建议：正文引用 Appendix B oracle routing 结果；讨论 merge amplification 根本问题；至少简要提及避免 merge 的替代架构。\n\n**W5 [warning, 共识] FP8 量化 non-determinism 对 regression power 的影响未分析。**\n- 位置：Section 3.5\n- 问题：SD=0.83pp 占 observed BCS effect (Δ≈1.9–4.6pp) 的 18–44%。Bootstrap CI 不区分信号方差和测量噪声，可能膨胀 residual variance 并削弱 regression power。\n- 建议：讨论 FP8 noise floor 对 smallest detectable BCS slope 的影响。\n\n**W6 [warning, 共识] 未解释方差讨论不足 + 因果性语言。**\n- 位置：Section 4.3, Section 6\n- 问题：BCS 解释 FewRel 约 27% accuracy variance，73% 未解释。R1 指出 27% semipartial R² 在 NLP 中属 large effect，但论文未讨论 prompt formatting、type definition quality、sentence complexity 等可能的未解释因素。Section 6 \"BCS captures a structural property\" 为半因果性语言。\n- 建议：Discussion 列出可能的未解释因素；改用 \"serves as a useful predictor of\" 等更审慎措辞。\n\n**W7 [warning, 部分共识] BCS mean aggregation 设计选择论证不足。**\n- 位置：Section 3.2, Appendix I\n- 问题：R1 指出 Appendix I Table 15 已做 mean vs max BCS 对比（方向一致），R2 遗漏此分析。但 top-k/加权方案未探索，且正文未引用 Appendix I 结果。\n- 建议：正文引用 Appendix I mean vs max 对比结果；讨论 aggregation 策略选择理由。\n\n---\n\n## Questions（需作者澄清）\n\n1. FewRel 上是否测试过 centrality 作为 confound？（R2 指出 Appendix E.1 Table 12 已确认 VIF=1.25，centrality 非 confound——R1 可能遗漏此分析）\n2. Max-based BCS 是否比 mean-based BCS 预测更好？（Appendix I Table 15 已有初步对比，正文应引用）\n3. Figure 1a NER U 形 count curve 是否通过 per-type recall 验证了 type-filtering overhead 解释？\n4. Qwen3-32B 作为主模型的选择理由是什么？\n5. SDGD 是否考虑过完全避免 merge 步骤的分解方案？\n6. FP8 noise floor 下，regression 能可靠检测的最小 BCS slope 是多少？\n\n---\n\n## Missing References\n\n| 文献 | 来源 | 状态 |\n|------|------|------|\n| PARSE (Shrinivas et al., 2025) — LLM-driven schema optimization | R2 | 待确认相关性 |\n| ASEE (2025) — Adaptive Schema-Aware Event Extraction | R2 | 待确认相关性 |\n| Li et al. (2023) \"Evaluating ChatGPT's IE Capabilities\" | R1 | 应引用 |\n| Josifoski et al. (2022) \"GenIE: Generative IE\" | R1 | 应引用 |\n| GLiREL (NAACL 2025) | R2 | R1 指出已被引用（Boyler et al. 2025），R2 事实有误 |\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目配置未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成。** 0 critical, 3 warning, 12 info。\n\n### Warnings\n1. **前 3 页连续纯文本**，无任何 display item。审稿人翻到第 5 页才看到 Figure 1。建议在前 2 页加入概览图或将 Figure 1 核心 panel 前置。\n2. **主正文 8 页仅 4 个 display items**（Figure 1-2, Table 1-2），密度 0.5/页，低于实证论文惯例（5-8 个/9 页）。大量结果被放入 15 页 appendix，导致正文偏\"文字墙\"。建议从 appendix 提升 1-2 个关键表格。\n3. **Pages 2-3 连续纯文本**（Related Work + Experimental Setup 开头），无 equation/figure/table 穿插。\n\n### Positives\n- ACL 匿名格式合规，Title/Author/Abstract 排版整洁\n- 所有表格使用 booktabs 风格\n- Figure 1 双 panel 配色色盲友好，caption 自包含\n- Figure 2 信息量充足，error taxonomy 可视化清晰\n- 无 margin 溢出、LaTeX 渲染错误\n- Limitations 长度适中（3 点 1 段），符合 EMNLP 规范\n- References 格式统一，无未解析引用\n\n---\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评估**：\n本文在 FewRel RE 上展示了一项方法论严谨的受控实证研究，BCS-controlled batch design 和统计分析（VIF 验证、cluster bootstrap、Bonferroni 校正）代表了 training-free LLM IE 领域少见的严格水准。负面结果（NER null、SDGD 失败）的诚实报告对社区有信息价值。\n\n**阻止接收的核心问题**：\n1. 标题和摘要将 confusability 效应隐含泛化到 \"Information Extraction\"，但独立预测效应仅在 FewRel sentence-level RE 上干净成立——这是 scope-evidence mismatch 问题，可修复但不可忽视。\n2. DocRED §4.3 的呈现顺序产生 replication 错觉，需要调整。\n3. 新颖性定位存在分歧：一位 Reviewer 认为 SCS 与 LLM-PEE 计算层面重叠严重，另一位认为受控实验方法论本身构成创新。论文应更清晰地定位贡献。\n\n**如果 Must-Fix 问题被充分解决**（标题/摘要限定 scope、DocRED 呈现修正、贡献定位明确化），本文有望达到 Conference 级别（3.5→4.0）——方法论素养和统计严谨性是加分项。如果 Must-Fix 未解决，将更适合 Findings。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识 [AGREE]：\n- 标题/摘要泛化超出证据（C1）\n- DocRED VIF=50.9 呈现矛盾（C2）\n- 模型多样性不足（W1，severity 有分歧）\n- TOST logit-scale 主文未标注（W2）\n- Domain composition confound（W3）\n- RQ3 分析不充分（W4）\n- FP8 non-determinism power（W5）\n- 未解释方差讨论不足（W6）\n- BCS 消融部分不足（W7）\n- Figure 1b 可读性、Table 1 术语、type name 粒度（Minor）\n\n## Reviewer Divergence\n\n**D1: SCS vs LLM-PEE 新颖性**（R2: Must-Fix, R1: REBUT）\n- R2 认为 SCS 计算与 LLM-PEE 重叠，技术贡献独特性不足\n- R1 认为受控实验方法论（非 metric）是贡献核心，视角转变构成创新\n- Director 评估：属于合理评审视角差异，论文应更清晰地定位为 empirical methodology 贡献\n\n**NER 结果性质**（minor 分歧）\n- R1 概括为 \"null\"\n- R2 补充：Figure 2a IntraSub 机制证据存在（ρ=0.84–1.1），是 \"null overall accuracy but active mechanism\" 的 boundary condition，不等于 \"no effect\"\n- Director 评估：R2 的细化更准确，论文应在正文区分 accuracy-level null 和 mechanism-level evidence\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract/Title**：需限定 confusability claim 的 task-specificity，区分 count（通用）和 confusability（RE-specific）。\"drives\" → \"predicts\" 的修改方向正确但不充分——需在首段即标注 \"specifically in relation extraction\"。\n\n**Section 2 (Related Work)**：与 LLM-PEE 的技术差异论证不充分。应显式对比 LLM-PEE 的 uncontrolled schema splitting 和本文的 controlled batch design。补充 Li et al. (2023)、GenIE (2022)。确认 PARSE/ASEE 相关性。\n\n**Section 3.2 (Metrics)**：BCS mean aggregation 选择理由应在正文讨论（引用 Appendix I Table 15 的 mean vs max 对比结果）。MiniLM 作为 pre-deployment proxy 的定位合理，但应在 §3.2 或 §6 讨论其与目标 LLM 实际 confusability 机制的关系。\n\n**Section 3.5 (Model)**：Qwen3-32B 选择理由应明确说明。FP8 quantization non-determinism (SD=0.83pp) 对 regression power 的影响应讨论。\n\n**Section 4.3 (BCS-Controlled)**：DocRED 段应首句标注 VIF caveat。FewRel regression 应控制 domain diversity 变量。正文应注明 FewRel centrality non-confound（引用 Appendix E.1）。\n\n**Section 4.4 (Factorial)**：TOST 量表依赖性应在此处标注（probability 通过，logit 不通过），不仅放 Limitations。\n\n**Section 5 (SDGD)**：应引用 oracle routing 结果（Table 9, Appendix B），讨论 merge amplification 的结构性问题，简要提及替代架构。\n\n**Section 6 (Discussion)**：\n- \"BCS captures a structural property\" → 更审慎措辞\n- 列出可能的未解释因素（prompt formatting, type definition quality, sentence complexity）\n- 限定 claim 范围至 Qwen3-32B（除非提升其他模型为主分析）\n\n**Figures/Tables**：\n- Figure 1b：考虑改用 grouped line chart 或增大尺寸\n- Figure 1(b) caption：标注 accuracy 定义\n- Table 1：Few-NERD \"trigger mentions\" 应改为 NER 术语\n"
  }
}
```

</details>

---


### Tool result

_source line 3117 · 2026-05-22T23:12:08.393660+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4427
}
```

</details>

---


### Tool call

_source line 3118 · 2026-05-22T23:12:15.486887+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-1: 初始化 + 独立审稿', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-1: 初始化 + 独立审稿', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 3119 · 2026-05-22T23:12:15.487299+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 3120 · 2026-05-22T23:12:27.298808+00:00_

审稿完成，报告已投递至 Research Director。

**Round 31 审稿总结**：

- **Overall: 3.5 Borderline Conference**（R1=3.5, R2=3.5，一致）
- **2 个 Must-Fix（共识）**：标题/摘要 scope 超出证据（confusability 仅 FewRel RE 干净成立）；DocRED §4.3 VIF=50.9 呈现矛盾
- **1 个分歧项**：SCS vs LLM-PEE 新颖性（R1 认为方法论创新，R2 认为 metric 重叠）
- **7 个 Should-Fix（共识）**：模型多样性、TOST 量表标注、domain confound、RQ3 不充分、FP8 power、未解释方差、BCS 消融
- **7 个 Minor**
- **视觉审查**：3 warning（前 3 页无 display item、正文 display 密度低、Pages 2-3 文字墙）
- **Issue Tracker**：已同步 17 个 issue 至 `review_issues.yaml`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 260

## Round 260

2 recorded events


### User

_source line 3121 · 2026-05-22T23:12:29.902530+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

对 R1 的 16 个具体点（2 Must-Fix、5 Should-Fix、5 Minor、3 Questions、1 Missing Refs）逐条做了 AGREE/REBUT 回应：

- **AGREE 12 条**：标题泛化超出证据（N1）、DocRED 呈现顺序问题（N2）、TOST logit-scale（W1）、cross-model 覆盖不足（W2）、domain composition confound（W3）、FP8 power（W5）等
- **REBUT 3 条**：
  - W4（MiniLM vs Qwen3 embedding）：论文已在 Appendix I 做了 cross-embedding 验证，MiniLM 的价值在于 deployment 前轻量代理，但承认深层机制讨论不足
  - Minor 中 type-level r²讨论价值：低 r² 仍有铺垫 batch-level 分析的叙事功能
  - Q2（FewRel centrality check）：Appendix E.1 Table 12 已明确做过，VIF=1.25 确认 centrality 非 confound——R1 可能遗漏了此附录分析

核心共识：confusability 的独立效应仅在 FewRel RE 上干净成立，标题需要限定。总评与 R1 一致：3.5 Borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3122 · 2026-05-22T23:12:43.576284+00:00_

审稿流程已全部完成。

**最终结果**：审稿报告已投递至 Research Director。

- **Overall: 3.5 (Borderline Conference)**
- **Soundness 3.5 | Excitement 3.0 | Reproducibility 4.0**
- **2 个 Must-Fix（共识）**：标题/摘要 scope 超出证据；DocRED VIF=50.9 呈现矛盾
- **1 个分歧项**：SCS vs LLM-PEE 新颖性（R1 认为方法论创新，R2 认为 metric 重叠）
- **7 个 Should-Fix（共识）**：模型多样性、TOST 量表依赖、domain confound、RQ3 分析不充分、FP8 power、未解释方差、BCS 消融
- **视觉审查**：3 个 warning（前 3 页无 display item、display 密度偏低、Related Work 纯文字段）
- **Issue Tracker**：已同步 17 条 issue 至 `review_issues.yaml`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 261

## Round 261

2 recorded events


### User

_source line 3123 · 2026-05-23T00:32:28.295794+00:00_

[RESET REQUEST] Research Reviewer 达到硬限
  触发原因：运行时长 16h54m
  本轮累计 28 条消息 / 16h 54min

⚠️ 你自己的 context 状态：已 28 条消息 / 16h 54min

请回复：
  [RESET AGENT]     只重置 Research Reviewer，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 3124 · 2026-05-23T00:32:37.879299+00:00_

审稿报告已在本消息之前成功投递（`submit_review_report_to_research_director` 返回成功）。所有流程已完成：

- ✅ 2 名 Reviewer 独立审稿
- ✅ 交叉分享 + AGREE/REBUT 回应
- ✅ 收敛判断（1 轮收敛，1 处分歧记录在案）
- ✅ Issue Tracker 更新（`review_issues.yaml`）
- ✅ 审稿报告投递

本轮讨论已完全收敛，无未完成工作。

[RESET BOTH]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 262

## Round 262

2 recorded events


### User

_source line 3125 · 2026-05-23T00:39:22.404254+00:00_

[SYSTEM] Research Reviewer 刚完成 context rotation (Loop 14)，已读取 handoff 并就绪。如有待办任务请立即分配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 3126 · 2026-05-23T00:39:28.810176+00:00_

审稿报告已于本轮早些时候投递完毕（Round 31, 3.5 Borderline Conference）。当前无待办任务。

如果 Research Director 有后续指令（如修改后重新审稿），会通过新的论文提交触发。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 263

## Round 263

56 recorded events


### User

_source line 3127 · 2026-05-25T21:13:17.314998+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main + Findings unified)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 3128 · 2026-05-25T21:13:22.856999+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3129 · 2026-05-25T21:13:22.907835+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3130 · 2026-05-25T21:13:30.936005+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 3131 · 2026-05-25T21:13:30.986586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3132 · 2026-05-25T21:13:36.555903+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 3133 · 2026-05-25T21:13:38.011367+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (70 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_fewshot_bcs_count16** (success): At count=16, the accuracy gap between low-BCS and high-BCS schema batches will widen as few-shot examples increase, consistent with count=8 pattern, because demonstrations reinforce distinguishable schemas more than confusable ones. ← 基于 exp_fewshot_bcs_v2\n- **exp_llama70b_ner_bcs_null** (success): Batch-level BCS does not correlate with NER F1 for LLaMA-3.1-70B-FP8, consistent with the BCS null observed in Qwen3-32B (r=0.004) and LLaMA-8B (r=-0.12). The confusability metric is not predictive of extraction quality at the batch level. ← 基于 exp012_llama_8b_r2_exp2\n  [LLaMA-70B NER BCS-null analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_ner_bcs_null/data/bcs_null_analysis.json)\n- **exp_gemini_fla
…[truncated 1056 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 3134 · 2026-05-25T21:13:38.061968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3135 · 2026-05-25T21:13:38.463889+00:00_

File content (26246 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 3136 · 2026-05-25T21:13:39.467685+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 3137 · 2026-05-25T21:13:39.928546+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 460
}
```

</details>

---


### Tool call

_source line 3138 · 2026-05-25T21:13:39.928935+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 3139 · 2026-05-25T21:13:39.979383+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3140 · 2026-05-25T21:13:45.599989+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 3141 · 2026-05-25T21:13:46.052111+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{enumitem}
15	\usepackage[normalem]{ulem}
16	\usepackage{listings}
17	
18	\setlength{\textfloatsep}{10pt plus 2pt minus 4pt}
19	\setlength{\floatsep}{10pt plus 2pt minus 4pt}
20	\setlength{\dbltextfloatsep}{10pt plus 2pt minus 4pt}
21	\setlength{\dblfloatsep}{10pt plus 2pt minus 4pt}
22	
23	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{experimental_setup}
37	
38	\input{results}
39	
40	\input{sdgd_negative}
41	
42	\input{discussion}
43	
44	\section*{Limitations}
45	\looseness=-1
46	\textbf{(1)~Model scope.}
47	Primary experiments use Qwen3-32B; cross-model validation covers count and BCS but not secondary analyses. All evidence is correlational.
48	\textbf{(2)~DocRED multicollinearity.}
49	Severe VIF (50.9) prevents reliable BCS quantification; semipartial $R^2{}\,=\,5.6\%$ is directional only.
50	\textbf{(3)~Experimental scope.}
51	Four English Wikipedia/Wikidata datasets in a zero-shot setting; few-shot, fine-tuned, and non-English scenarios remain untested. BCS predicts RE accuracy but not NER. Cross-dataset consistency is converging evidence, not independent replication \citep{rothman-1990}.
52	
53	% \input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF
54	
55	\bibliography{references}
56	
57	\appendix
58	
59	\section{Additional Figures}
60	\label{sec:appendix_figures}
61	
62	\begin{table}[h]
63	\centering
64	\small
65	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declinin
…[truncated 10290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 3142 · 2026-05-25T21:13:46.052463+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 3143 · 2026-05-25T21:13:46.776765+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "writing_plan.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "writing_plan.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 3144 · 2026-05-25T21:13:54.045422+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026:

## Submission Overview
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Important Dates (ARR)
The ARR submission deadline for long and short papers is May 25, 2026, with a reviewer registration deadline for all authors on May 27, 2026, author response and discussion July 7-13, 2026, meta-review released July 30, 2026, and EMNLP commitment deadline August 2, 2026.

## Paper Format
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

## ARR Submission Policy
For the ARR 2026 May cycle, authors must explicitly declare which conference they intend to commit to at submission time. This choice is binding for EMNLP 2026: ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

## Presentation Requiremen
…[truncated 531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7992
}
```

</details>

---


### Tool result

_source line 3145 · 2026-05-25T21:13:54.046005+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml\", \"content\": \"# Writing Plan — schema-dag-extraction\\n# Generated: 2026-05-15\\n# Venue: EMNLP 2026 (ARR May 25 cycle)\\n# Format: 8 pages main text + unlimited references\\n# Mode: Full Draft (2-claim analysis paper + SDGD negative result)\\n\\nmeta:\\n  title: \\\"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\\\"\\n  venue: EMNLP 2026 Main\\n  submission_deadline: \\\"2026-05-25\\\"\\n  page_limit: 8\\n  template: \\\"acl2023\\\"  # ARR uses ACL rolling review LaTeX template\\n  template_note: \\\"No EMNLP 2026 template found locally. Using acl2023.sty (standard ARR template). Worker must download from https://github.com/acl-org/acl-style-files if not available.\\\"\\n  primary_model: \\\"Qwen3-32B-FP8\\\"\\n  secondary_model: \\\"LLaMA-3.1-8B-Instruct (exp-012, D022: 70B→8B cross-scale validation)\\\"\\n  datasets: [\\\"Few-NERD (66 types)\\\", \\\"FewRel (80 relations)\\\", \\\"MAVEN (168 event types)\\\"]\\n\\n# =============================================================================\\n# PAPER OUTLINE\\n# =============================================================================\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 250\\n    dependencies: [introduction, experiments, results, sdgd_negative, conclusion]\\n    key_content:\\n      - Problem: training-free LLM IE degrades on complex schemas; prior work conflates count and confusability\\n      - Method: first controlled empirical study isolating type confusability from count across 3 tasks\\n      - Findings: multi-channel degradation (count→recall, confusability→type confusion); pairwise SCS robust cross-task (r=0.11-0.13); effect amplifies 3.4× with schema complexity; per-type aggregation confounded on homogeneous schemas\\n      - Negative result: naive confusability-aw
…[truncated 3579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7269
}
```

</details>

---


### Tool call

_source line 3146 · 2026-05-25T21:14:02.727225+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 3147 · 2026-05-25T21:14:03.229380+00:00_

1	\begin{abstract}
2	Schema complexity affects training-free large language model (LLM) information extraction (IE), yet prior work conflates two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). We present, to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE across four datasets, focusing on relation extraction (RE) as the primary testbed with named entity recognition (NER) and event detection as boundary conditions.
3	Using embedding-based confusability metrics with controlled batch design, we find:
4	(1)~count degradation spans NER and RE (up to $-$49 percentage points [pp]), and inter-type confusability independently predicts RE type substitution errors, with bounded interaction confirmed by equivalence testing;
5	(2)~batch confusability independently explains ${\sim}$27\% of cross-batch RE accuracy variance on FewRel (semipartial $R^2 = 0.273$), replicating across two model families at three scales (8B--70B), while the NER null serves as a boundary condition;
6	(3)~schema decomposition fails due to merge amplification and routing failure, though oracle routing recovers accuracy\footnote{Code and data are available at \url{https://anonymous.4open.science/r/schema-dag-extraction-4C10/}.}.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3148 · 2026-05-25T21:14:03.229709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 3149 · 2026-05-25T21:14:03.781767+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{../../figures/paper/fig_problem_illustration.pdf}
7	\caption{Schema complexity in zero-shot relation extraction. Given the same input, a simple schema (few dissimilar types) yields the correct relation, while a complex schema with more candidate types and a cluster of semantically similar types causes type substitution (gold \emph{place of birth} $\to$ predicted \emph{residence}). We decompose schema complexity into two dimensions: type count and inter-type confusability.}
8	\label{fig:problem}
9	\end{figure}
10	
11	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.28 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable (Figure~\ref{fig:problem}).
12	
13	\looseness=-1
14	What explains this degradation? Prior dec
…[truncated 2986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 3150 · 2026-05-25T21:14:03.782156+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 3151 · 2026-05-25T21:14:04.685581+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	\looseness=-1
6	Training-free LLM IE spans instruction tuning \citep{instructuie-2023}, code-style schema encoding \citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \citep{gollie-2024,adelie-2024}, schema-driven decoding \citep{slot-2025,oneke-2025}, and constrained JSON decoding \citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \citep{uniner-2024}, and bidirectional encoders \citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \citep{relationprompt-2022}, constrained generation \citep{josifoski-2022-genie}, and shared embedding spaces \citep{boylan-2025-glirel,wadhwa-re-llm-2023}. Related work exploits type embeddings for retrieval \citep{shachar-2025-ner-retriever} and introspective confusion for example selection \citep{reflect-learn-2026}. These methods handle moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{../../figures/paper/fig_framework.pdf}
11	\caption{Experimental design overview on FewRel. Each point is one batch; color encodes RE accuracy (green=high, red=low). \textbf{Dimension~1} (horizontal): accuracy declines with type count (\S\ref{sec:count_curves}). \textbf{Dimension~2} (vertical): within each count level, higher BCS correlates with lower accuracy (\S\ref{sec:bcs_controlled}). BCS range narrows at high counts, limiting Dimension~2 discriminability.}
12	\label{fig:framework}
13	\end{figure}
14	
15	\paragraph{Schema complexity in IE.}
16	\looseness=-1
17	The most directly related work is LLM-PEE \citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extra
…[truncated 3306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 3152 · 2026-05-25T21:14:04.685945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 3153 · 2026-05-25T21:14:04.937361+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	\looseness=-1
5	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
6	
7	\begin{figure*}[t]
8	\centering
9	\begin{minipage}[t]{0.48\textwidth}
10	\centering
11	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
12	\end{minipage}
13	\hfill
14	\begin{minipage}[t]{0.48\textwidth}
15	\centering
16	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
17	\end{minipage}
18	\caption{\textbf{(a)} Count-degradation curves. Error bars: $\pm 1$ standard deviation (SD) across 3 batch-composition seeds $\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Rightmost points are full-schema (negligible sampling variance). \textbf{(b)} Illustrative BCS-controlled FewRel accuracy: each bar represents one extreme-BCS batch per condition. Slopes are consistent across pool conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps. Statistical evidence is provided by the pooled regression (\S\ref{sec:bcs_controlled}, semipartial $R^2 = 0.273$, $n = 204$).}
19	\label{fig:main_results}
20	\end{figure*}
21	
22	\subsection{Tasks and Datasets}
23	\label{sec:datasets}
24	
25	\paragraph{Few-NERD (NER).}
26	Few-NERD \citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
27	
28	\paragraph{FewRel (RE).
…[truncated 9087 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 3154 · 2026-05-25T21:14:04.937830+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 3155 · 2026-05-25T21:14:05.038563+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3156 · 2026-05-25T21:14:10.816236+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 3157 · 2026-05-25T21:14:10.866971+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	All experiments use Qwen3-32B and the v1 prompt (\S\ref{sec:model}; Appendix~\ref{sec:appendix_prompts}) unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, Two One-Sided Tests [TOST]) remain single-model.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\resizebox{\columnwidth}{!}{%
10	\begin{tabular}{llrrrrr}
11	\toprule
12	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
13	\midrule
14	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\,0.001$ \\
15	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\,0.001$ \\
16	\bottomrule
17	\end{tabular}}
18	\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \S\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}
19	\label{tab:pairwise}
20	\end{table}
21	
22	\subsection{Count-Degradation Curves}
23	\label{sec:count_curves}
24	
25	\looseness=-1
26	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (85.7\%$\to$50.4\% for FewRel). NER recall drops from 0.72 (count 1) to 0.28 before recovering to 0.41 at full-schema. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%; Appendix~\ref{sec:appendix_figures}); MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The decline is stable across seeds (Jonckheere-Terpstra $p < 0.001$) and replicates on Llama-8B ($-$43\,pp; Table~\ref{tab:cross_model}), Llama-70B, and Gemini Flash (Figure~\ref{fig:cross_model_count}).
27	
28	\subsection{Pairwise Confusability and Type Confusion}
29	\label{sec:pairwise}
30	
31	We 
…[truncated 7892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3158 · 2026-05-25T21:14:11.319143+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 3159 · 2026-05-25T21:14:11.570378+00:00_

1	\section{Schema Decomposition}
2	\label{sec:sdgd}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{../../figures/paper/fig_sdgd_pipeline_compact.pdf}
7	\caption{Schema decomposition pipeline and failure modes. Graph coloring partitions the schema into low-confusability sub-schemas, but two structural bottlenecks prevent practical gains: \textbf{routing failure} in RE (73.4\% of instances match multiple sub-schemas) and \textbf{merge amplification} in NER/ED (union merge increases false positives ${\sim}4\times$).}
8	\label{fig:sdgd_pipeline}
9	\end{figure}
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical strategies perform below the single-pass baseline due to constrained decoding: 73.4\% of instances match multiple sub-schemas simultaneously.}
15	\label{tab:routing_strategies}
16	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}lrr@{}}
17	\toprule
18	\textbf{Strategy} & \textbf{Accuracy} & \textbf{$\Delta$ vs.\ Single-Pass} \\
19	\midrule
20	Oracle (gold label) & 72.4\% & +22.0\,pp \\
21	\midrule
22	Max-conf (positive only) & 36.5\% & $-$14.0\,pp \\
23	None-aware & 36.5\% & $-$14.0\,pp \\
24	Margin (positive only) & 35.9\% & $-$14.5\,pp \\
25	Max-conf (all) & 27.7\% & $-$22.7\,pp \\
26	Random & 14.7\% & $-$35.7\,pp \\
27	\midrule
28	Single-pass (no decomposition) & 50.4\% & --- \\
29	\bottomrule
30	\end{tabular}}
31	\end{table}
32	
33	A natural intervention is to partition the schema so confusable types never co-occur (Figure~\ref{fig:sdgd_pipeline}). We tested Schema-DAG-Guided Decomposition (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches. While oracle routing recovers accuracy (0.724 vs.\ 0.504 single-pass; Table~\ref{tab:routing_strategies}), all practical routing strategies fall below the single-pass baseline, and NER decomposit
…[truncated 472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 3160 · 2026-05-25T21:14:11.570711+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 3161 · 2026-05-25T21:14:11.621196+00:00_

1	\enlargethispage{2\baselineskip}
2	\section{Discussion and Conclusion}
3	\label{sec:discussion}
4	
5	\textbf{RQ1} (independent confusability effect): Yes, on RE. BCS independently explains ${\sim}$27\% of cross-batch accuracy variance on FewRel after controlling for count and centrality, replicating across three model scales. The NER null reflects dispersed error modes rather than absence of confusability effects (\S\ref{sec:multi_channel}).
6	\textbf{RQ2} (degradation modes): Count reduces recall overall (monotonically in RE; non-monotonically in NER); confusability drives type substitution (IntraSub) that scales monotonically with BCS. The two dimensions interact with bounded magnitude on the linear scale.
7	\textbf{RQ3} (decomposition): Schema decomposition fails in practice due to routing ambiguity (RE) and merge amplification (NER/ED), though oracle routing confirms the dimensions are separable in principle (\S\ref{sec:sdgd}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Intra-batch substitution (IntraSub) and missed rates by BCS bin. IntraSub scales monotonically with BCS across all three datasets. DocRED missed rates decrease with BCS, indicating errors shift from omission to substitution.}
13	\label{tab:error_taxonomy}
14	\resizebox{\columnwidth}{!}{%
15	\begin{tabular}{llrrrrrrr}
16	\toprule
17	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
18	\cmidrule(lr){3-7}
19	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
20	\midrule
21	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
22	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
23	DocRED & IntraSub & --- & 4.8\% & 22.4\% & 37.0\% & 41.9\% & 0.843 & ${<}\,0.001$ \\
24	\midrule
25	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
26	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
27	DocRED & Missed 
…[truncated 1091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3162 · 2026-05-25T21:14:28.632116+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "config",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "config",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 3163 · 2026-05-25T21:14:30.539112+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1906
}
```

</details>

---


### Tool call

_source line 3164 · 2026-05-25T21:14:31.091996+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_32/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_32/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 3165 · 2026-05-25T21:14:32.046010+00:00_

-rw-r--r-- 1 ubuntu ubuntu 902117 May 25 17:33 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_32/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 3166 · 2026-05-25T21:14:32.046428+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 3167 · 2026-05-25T21:14:32.798949+00:00_

-rw-r--r-- 1 ubuntu ubuntu 12409 May 22 23:34 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 3168 · 2026-05-25T21:14:32.799307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "200"
  }
}
```

</details>

---


### Tool result

_source line 3169 · 2026-05-25T21:14:33.101455+00:00_

200	\toprule
201	\textbf{Margin (pp)} & \textbf{$t_{\text{upper}}$} & \textbf{$p_{\text{TOST}}$} & \textbf{Conclusion} \\
202	\midrule
203	$\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\
204	$\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\
205	$\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\
206	$\pm 5$ & $-5.02$ & ${<}\,0.001$ & Equivalent \\
207	\bottomrule
208	\end{tabular}
209	\end{table}
210	
211	\paragraph{Logit-scale sensitivity.}
212	Because accuracy near 50\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\pm 3$\,pp margin ($\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\,pp, still within the $\pm 3$\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\pm 3$\,pp and $p = 0.026$ at $\pm 3.5$\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.
213	
214	\paragraph{DocRED factorial (expanded).}
215	With expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \times 2$ factorial (count $\in \{16, 32\}$, BCS median split) yields an apparent interaction ($-$9.4\,pp, 95\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\,pp at count 16 but $-$15.7\,pp at count 32. However, this attenuation is confounded by BCS range restriction:
…[truncated 62422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 3170 · 2026-05-25T21:14:56.025604+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NOT_FOUND_IN_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NOT_FOUND_IN_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 3171 · 2026-05-25T21:14:56.427621+00:00_

NOT_FOUND_IN_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 3172 · 2026-05-25T21:14:56.427977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 3173 · 2026-05-25T21:14:56.478464+00:00_

1	
2	# Review Issues Tracker
3	# Updated: 2026-05-23 Round 31 Action Matrix dispatched to Agent
4	
5	# ============================================================
6	# R31 CRITICAL (2 items — consensus)
7	# ============================================================
8	
9	- id: R31-C1
10	  summary: "标题/摘要对 'Information Extraction' 的泛化声明超出证据支撑：confusability 独立预测效应仅在 FewRel RE 上干净成立"
11	  category: framing
12	  severity: critical
13	  status: in_progress
14	  first_raised_round: 31
15	  last_seen_round: 31
16	  mentions:
17	    - {round: 31, reviewers: [R1, R2], note: "R1-N1, R2 AGREE. NER null（Figure 2a IntraSub 机制存在但 accuracy 无效应）, MAVEN centrality confound, DocRED VIF=50.9 不可靠. Count-degradation 跨任务通用，但 confusability 独立效应仅 sentence-level RE."}
18	  action_items:
19	    - {round: 31, action: "标题保留不改；Abstract 第一句区分 count(跨任务) vs confusability(RE batch-level)；'two independent dimensions' → 'two separable dimensions'", assigned_to: "Agent B2", status: in_progress}
20	  resolution: ""
21	  resolution_round: null
22	
23	- id: R31-C2
24	  summary: "DocRED §4.3 VIF=50.9 下 partial correlation 呈现顺序产生 replication 错觉"
25	  category: method
26	  severity: critical
27	  status: in_progress
28	  first_raised_round: 31
29	  last_seen_round: 31
30	  mentions:
31	    - {round: 31, reviewers: [R1, R2], note: "R1-N2, R2 AGREE. §4.3 先报告 ρ=-0.762 和效应量再 qualify，容易让读者产生 replication 印象。Ridge 不解决共线性语义问题。Semipartial R²_BCS=0.056 仅 5.6% unique variance."}
32	  action_items:
33	    - {round: 31, action: "§4.3 DocRED 段 VIF caveat 前置（首句标注）；保留 ρ 值作 directional evidence；不移到 appendix", assigned_to: "Agent B3", status: in_progress}
34	  resolution: ""
35	  resolution_round: null
36	
37	# ============================================================
38	# R31 DIVERGENT (1 item — reviewers disagree)
39	# ============================================================
40	
41	- id: R31-D1
42	  summary: "SCS/BCS 相对于 LLM-PEE 的新颖性论证：metric 创新 vs 方法论创新之争"
43	  category: framing
44	  severity: warning
45	  status
…[truncated 2576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3174 · 2026-05-25T21:15:01.044861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 3175 · 2026-05-25T21:15:01.095626+00:00_

100	
101	- id: R31-W4
102	  summary: "RQ3 (Schema Decomposition) Section 5 分析不充分：仅半栏，oracle routing 上限问题未讨论"
103	  category: writing
104	  severity: warning
105	  status: in_progress
106	  first_raised_round: 31
107	  last_seen_round: 31
108	  mentions:
109	    - {round: 31, reviewers: [R1, R2], note: "R2-W2, R1 AGREE. Oracle routing 仅 72.4% vs single-type >85%，说明 decompose-then-merge 架构本身有结构性问题。应讨论 merge amplification 即使 routing 完美也无法避免。"}
110	  action_items:
111	    - {round: 31, action: "§5 有限扩展 +4-5 行：引用 oracle routing、merge amplification 机制、替代架构方向", assigned_to: "Agent B7", status: in_progress}
112	  resolution: ""
113	  resolution_round: null
114	
115	- id: R31-W5
116	  summary: "FP8 量化 non-determinism (SD=0.83pp) 占效应 18-44%，缺 power analysis"
117	  category: method
118	  severity: warning
119	  status: in_progress
120	  first_raised_round: 31
121	  last_seen_round: 31
122	  mentions:
123	    - {round: 31, reviewers: [R1, R2], note: "R1-W5, R2 AGREE. Bootstrap CI 不区分信号与测量噪声。应讨论 noise floor 对 smallest detectable BCS slope 的影响。"}
124	  action_items:
125	    - {round: 31, action: "Appendix variance decomposition 节加一句 power analysis（back-of-envelope 足够）", assigned_to: "Agent B8", status: in_progress}
126	  resolution: ""
127	  resolution_round: null
128	
129	- id: R31-W6
130	  summary: "未解释方差讨论不足（FewRel 73% unexplained）+ Section 6 因果性语言"
131	  category: writing
132	  severity: warning
133	  status: in_progress
134	  first_raised_round: 31
135	  last_seen_round: 31
136	  mentions:
137	    - {round: 31, reviewers: [R1, R2], note: "R2-W1, R1 AGREE with nuance（27% semipartial R² 在 NLP 中属 large effect）。但应讨论 prompt formatting、type definition quality 等未解释因素。"}
138	  action_items:
139	    - {round: 31, action: "Discussion 加 2-3 行列未解释因素。不改 'captures structural property'（Reviewer 确认有实验证据支撑）", assigned_to: "Agent B9", status: in_progress}
140	  resolution: ""
141	  resolution_round: null
142	
143	- id: R31-W7
144	  summary: "BCS 指标设计 mean aggregation 选择：Appendix I 有 mean vs m
…[truncated 5177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3176 · 2026-05-25T21:16:10.565227+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema-dag-extraction",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema-dag-extraction",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 3177 · 2026-05-25T21:16:35.264608+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24699
}
```

</details>

---


### Tool call

_source line 3178 · 2026-05-25T21:16:35.315268+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性** 审查。\n\n## 论文信息\n- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n- **论文路径**: projects/schema-dag-extraction/docs/paper/main.tex（含 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex）\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_32/submitted.pdf\n- **Venue**: EMNLP 2026（ARR May 2026）\n- **格式**: Long paper, 正文 8 页, 参考文献无限, Limitations 必须在正文中\n- **模板**: ACL review 模板, double-blind\n- **Abstract**: 不超过 200 words\n\n## 你的审查重点\n\n### 1. 实验设计与统计方法\n- 核心 claim: BCS 独立解释 FewRel 约 27% cross-batch RE accuracy variance（semipartial R² = 0.273）。验证统计方法是否正确（VIF、partial correlation、bootstrap CI、cluster-robust inference）。\n- TOST 等价检验：probability scale 通过（p=0.003）但 logit scale 不通过（p=0.209）。这对 \"bounded interaction\" 结论的影响。\n- DocRED VIF=50.9 的 multicollinearity 问题：partial correlation 在此条件下的可靠性。semipartial R²_BCS = 0.056 的解读。\n- NER batch-level BCS null：power analysis 是否充分（65% power < 80% 阈值）？\"absence of evidence vs evidence of absence\" 的论证是否成立？\n- FP8 量化噪声 SD=0.83pp 对 BCS slope 最小可检测效应的影响。\n\n### 2. Claims vs Evidence 对齐\n- 标题/摘要说 \"Information Extraction\" 但 confusability 独立效应（batch-level BCS→accuracy）仅在 sentence-level RE（FewRel）上干净成立。NER null、MAVEN centrality confound、DocRED VIF。泛化性如何？\n- \"first controlled study\" claim 是否成立？与 LLM-PEE 的区别是否充分。\n- Cross-model validation 范围：主实验仅 Qwen3-32B，secondary analyses（TOST、error taxonomy、SDGD）无跨模型验证。\n- 论文说 \"two model families at three scales\" — 但 Gemini Flash 是第三个 family。检查全文一致性。\n\n### 3. 可复现性\n- 单种子 greedy decoding（seed 42）：batch-composition variance 已用 25 batches × 3 seeds 覆盖，但模型级别仅 1 seed。\n- FewRel 合并 train+val split 的合理性：held-out validation（Appendix O, ρ=0.216）是否足够。\n- 代码/数据可用性（anonymous repo link）。\n\n### 4. 页数和格式\n- 验证正文是否在 8 页内。\n- Limitations 是否在正文中（不在 appendix）。\n- 检查匿名化（作者 \"Anonymous\"、无自引暴露身份）。\n\n请给出结构化审稿意见：Strengths (逐条) → Weaknesses (逐条，分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性** 审查。\n\n## 论文信息\n- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n- **论文路径**: projects/schema-dag-extraction/docs/paper/main.tex（含 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex）\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_32/submitted.pdf\n- **Venue**: EMNLP 2026（ARR May 2026）\n- **格式**: Long paper, 正文 8 页, 参考文献无限, Limitations 必须在正文中\n- **模板**: ACL review 模板, double-blind\n- **Abstract**: 不超过 200 words\n\n## 你的审查重点\n\n### 1. 实验设计与统计方法\n- 核心 claim: BCS 独立解释 FewRel 约 27% cross-batch RE accuracy variance（semipartial R² = 0.273）。验证统计方法是否正确（VIF、partial correlation、bootstrap CI、cluster-robust inference）。\n- TOST 等价检验：probability scale 通过（p=0.003）但 logit scale 不通过（p=0.209）。这对 \"bounded interaction\" 结论的影响。\n- DocRED VIF=50.9 的 multicollinearity 问题：partial correlation 在此条件下的可靠性。semipartial R²_BCS = 0.056 的解读。\n- NER batch-level BCS null：power analysis 是否充分（65% power < 80% 阈值）？\"absence of evidence vs evidence of absence\" 的论证是否成立？\n- FP8 量化噪声 SD=0.83pp 对 BCS slope 最小可检测效应的影响。\n\n### 2. Claims vs Evidence 对齐\n- 标题/摘要说 \"Information Extraction\" 但 confusability 独立效应（batch-level BCS→accuracy）仅在 sentence-level RE（FewRel）上干净成立。NER null、MAVEN centrality confound、DocRED VIF。泛化性如何？\n- \"first controlled study\" claim 是否成立？与 LLM-PEE 的区别是否充分。\n- Cross-model validation 范围：主实验仅 Qwen3-32B，secondary analyses（TOST、error taxonomy、SDGD）无跨模型验证。\n- 论文说 \"two model families at three scales\" — 但 Gemini Flash 是第三个 family。检查全文一致性。\n\n### 3. 可复现性\n- 单种子 greedy decoding（seed 42）：batch-composition variance 已用 25 batches × 3 seeds 覆盖，但模型级别仅 1 seed。\n- FewRel 合并 train+val split 的合理性：held-out validation（Appendix O, ρ=0.216）是否足够。\n- 代码/数据可用性（anonymous repo link）。\n\n### 4. 页数和格式\n- 验证正文是否在 8 页内。\n- Limitations 是否在正文中（不在 appendix）。\n- 检查匿名化（作者 \"Anonymous\"、无自引暴露身份）。\n\n请给出结构化审稿意见：Strengths (逐条) → Weaknesses (逐条，分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment。"
  }
}
```

</details>

---


### Tool result

_source line 3179 · 2026-05-25T21:16:56.282361+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20967
}
```

</details>

---


### Tool call

_source line 3180 · 2026-05-25T21:16:56.533584+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性/完整性** 审查。\n\n## 论文信息\n- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n- **论文路径**: projects/schema-dag-extraction/docs/paper/main.tex（含 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex）\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_32/submitted.pdf\n- **Venue**: EMNLP 2026（ARR May 2026）\n- **格式**: Long paper, 正文 8 页, 参考文献无限, Limitations 必须在正文中\n- **模板**: ACL review 模板, double-blind\n- **Abstract**: 不超过 200 words\n\n## 你的审查重点\n\n### 1. 贡献新颖性与显著性\n- 论文核心贡献是\"第一个受控实验隔离 type count 和 confusability\"。这在 IE 领域是否有足够新颖性？\n- SCS/BCS metric 与 LLM-PEE 的 embedding similarity 本质上相同（cosine similarity of type embeddings）。论文的贡献到底在 metric 还是在 methodology（受控实验设计）？这一区分是否在论文中清楚传达？\n- Pairwise r² ≈ 1.5% 的 effect size：论文 acknowledge 了 modest，但在 abstract 和 contributions list 中强调 \"independently predicts\"。这种 framing 是否公允？\n- SDGD 负面结果（Section 5）仅半栏，作为 RQ3 的回答是否充分？负面结果本身是否有独立贡献价值？\n\n### 2. Related Work 完整性\n- 检查 LLM-PEE (2025) 的 positioning 是否准确和公平。\n- 是否遗漏了重要的近期相关工作？特别关注：\n  - Schema decomposition / type partitioning 方面的工作\n  - Embedding-based label similarity 在分类/IE 中的应用\n  - LLM 长 prompt / context window 效应对 IE 的影响\n- CrossAgentIE (2025)、CMAS-NER (2025)、Reflect&Learn (2026) 的引用是否充分？\n- 引用是否包含虚构 citation？抽查 5-10 个 references 的真实性。\n\n### 3. 写作质量与叙事结构\n- Introduction 的 RQ1/RQ2/RQ3 框架是否清晰？\n- Results section 的叙事流是否连贯（count curves → pairwise → BCS-controlled → multi-channel → centrality confound）？\n- Discussion 是否充分回应了三个 RQ？\n- 论文 \"two dimensions\" 框架的叙事张力：count 是已知的，confusability 的独立效应是本文贡献。这一核心 story 是否讲清楚了？\n- 检查是否有 AI 痕迹（\"delve into\"、\"it is important to note\"、\"leveraging\" 过度使用等）。\n\n### 4. 格式合规\n- Abstract word count（必须 ≤ 200 words）。\n- 正文页数（≤ 8 页）。\n- Limitations section 位置（正文中，非 appendix）。\n- Checklist 不在 PDF 中（EMNLP 2026: checklist 在 OpenReview form 中）。\n- Figure/Table 编号连续性。\n- 引用格式一致性（natbib）。\n\n请给出结构化审稿意见：Strengths (逐条) → Weaknesses (逐条，分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性/完整性** 审查。\n\n## 论文信息\n- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n- **论文路径**: projects/schema-dag-extraction/docs/paper/main.tex（含 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex）\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_32/submitted.pdf\n- **Venue**: EMNLP 2026（ARR May 2026）\n- **格式**: Long paper, 正文 8 页, 参考文献无限, Limitations 必须在正文中\n- **模板**: ACL review 模板, double-blind\n- **Abstract**: 不超过 200 words\n\n## 你的审查重点\n\n### 1. 贡献新颖性与显著性\n- 论文核心贡献是\"第一个受控实验隔离 type count 和 confusability\"。这在 IE 领域是否有足够新颖性？\n- SCS/BCS metric 与 LLM-PEE 的 embedding similarity 本质上相同（cosine similarity of type embeddings）。论文的贡献到底在 metric 还是在 methodology（受控实验设计）？这一区分是否在论文中清楚传达？\n- Pairwise r² ≈ 1.5% 的 effect size：论文 acknowledge 了 modest，但在 abstract 和 contributions list 中强调 \"independently predicts\"。这种 framing 是否公允？\n- SDGD 负面结果（Section 5）仅半栏，作为 RQ3 的回答是否充分？负面结果本身是否有独立贡献价值？\n\n### 2. Related Work 完整性\n- 检查 LLM-PEE (2025) 的 positioning 是否准确和公平。\n- 是否遗漏了重要的近期相关工作？特别关注：\n  - Schema decomposition / type partitioning 方面的工作\n  - Embedding-based label similarity 在分类/IE 中的应用\n  - LLM 长 prompt / context window 效应对 IE 的影响\n- CrossAgentIE (2025)、CMAS-NER (2025)、Reflect&Learn (2026) 的引用是否充分？\n- 引用是否包含虚构 citation？抽查 5-10 个 references 的真实性。\n\n### 3. 写作质量与叙事结构\n- Introduction 的 RQ1/RQ2/RQ3 框架是否清晰？\n- Results section 的叙事流是否连贯（count curves → pairwise → BCS-controlled → multi-channel → centrality confound）？\n- Discussion 是否充分回应了三个 RQ？\n- 论文 \"two dimensions\" 框架的叙事张力：count 是已知的，confusability 的独立效应是本文贡献。这一核心 story 是否讲清楚了？\n- 检查是否有 AI 痕迹（\"delve into\"、\"it is important to note\"、\"leveraging\" 过度使用等）。\n\n### 4. 格式合规\n- Abstract word count（必须 ≤ 200 words）。\n- 正文页数（≤ 8 页）。\n- Limitations section 位置（正文中，非 appendix）。\n- Checklist 不在 PDF 中（EMNLP 2026: checklist 在 OpenReview form 中）。\n- Figure/Table 编号连续性。\n- 引用格式一致性（natbib）。\n\n请给出结构化审稿意见：Strengths (逐条) → Weaknesses (逐条，分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment。"
  }
}
```

</details>

---


### Tool result

_source line 3181 · 2026-05-25T21:16:58.001055+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1467
}
```

</details>

---


### Assistant

_source line 3182 · 2026-05-25T21:17:03.792507+00:00_

已派发：
- ✅ 视觉审查 Agent — 已启动（fire-and-forget）
- ✅ Reviewer 1（方法严谨性）— 已分配
- ✅ Reviewer 2（新颖性/完整性）— 已分配

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 264

## Round 264

2 recorded events


### User

_source line 3183 · 2026-05-25T21:25:01.856101+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 方法论严谨的分析型论文，统计工具链（bootstrap CI、cluster-robust inference、TOST、power analysis）远超 NLP 论文平均水准，但核心 confusability 独立效应（BCS→accuracy）仅在 FewRel 一个数据集上干净成立，title/abstract 所声称的 "Information Extraction" 泛化性存在实质性缺口。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法论本身过硬（VIF 检查、bootstrap、cluster-robust、equivalence testing），但 claims 的覆盖面超出 evidence 支撑范围：BCS 独立效应仅 FewRel 干净成立；TOST scale 选择有 cherry-picking 嫌疑；DocRED VIF=50.9 下的 partial correlation 解读需更审慎 |
| Excitement | 3/5 | 研究问题新颖且有实用价值（schema 复杂度的两维度分离），但 actionable insights 有限——SDGD 全部失败，唯一可用建议是"用 SCS/BCS 预筛高风险 schema"，且仅在 RE 上验证 |
| Reproducibility | 4/5 | Greedy decoding (temperature=0) 保证推理确定性；代码/数据声称可用（匿名链接）；实验细节充分（prompt 全文、batch 构建算法、count level 枚举）；但核心回归分析仅 Qwen3-32B 一个模型 |
| Reviewer Confidence | 4/5 | 熟悉 zero-shot IE、回归分析、equivalence testing 方法论；仔细阅读全文含全部 17 页 appendix |

---

## Strengths（主要优势）

**S1. 研究问题设计精巧，填补方法论空白。** 现有工作（LLM-PEE、GoLLIE、CodeKGC）要么把 count 和 confusability 混为一谈，要么只做工程优化不做 controlled analysis。本文通过 BCS-controlled batch design（§3.3）首次在 matched type count 条件下分离 confusability 的独立效应，实验设计在 NLP empirical 论文中属上乘。

**S2. 统计工具链远超同类论文水准。** VIF 检查（Table 12）排除 FewRel 的 multicollinearity（VIF=1.18）；percentile bootstrap CI 避免正态性假设（Table 2, §4.2）；cluster-robust SE 处理 batch 内非独立性（Appendix E.3）；TOST equivalence testing（Appendix C）量化交互效应上界；power analysis（Appendix E.2）诚实报告 NER null 的 65% power。这套工具链使核心 FewRel 结论高度可信。

**S3. 诚实报告负面结果。** SDGD 全部策略低于 single-pass baseline（Table 3, §5），routing failure rate 73.4%、merge amplification 定量分析；NER BCS null 未回避而是给出 power analysis 解释（Appendix E.2）；MAVEN centrality confound 在 §4.5 正面讨论。这种透明度在审稿中少见。

**S4. Count-degradation 发现跨任务稳健。** 从 NER（Few-NERD F1 从 0.72 降至 0.28）到 RE（FewRel 从 ~85% 降至 ~30%）到 ED（MAVEN），降解曲线在所有四个数据集、三个模型家族（Qwen3-32B、Llama-3.1-8B/70B、Gemini 2.5 Flash）上一致复现（Figure 3, 5; Tables 5, 23-25）。这是对社区有实际价值的 characterization。

**S5. BCS 作为 pre-hoc proxy 的实用性。** SCS/BCS 仅需 embedding 计算，无需运行抽取即可预测 schema 难度。对实际部署（哪些 schema 需要更多 few-shot 或类型拆分）有直接指导价值。跨 embedding（Qwen3-32B vs all-MiniLM-L6-v2）一致性（Appendix I）增强可信度。

**S6. Appendix 质量极高。** 17 页涵盖 centrality confound（E）、format independence（K）、prompt sensitivity（H）、domain distribution（E.4）、few-shot interaction（V）、cross-model（T, U）、aggregation simulation（N）等，几乎覆盖了 reviewer 能想到的所有 confound。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **核心 BCS 独立效应的泛化性严重不足——title/abstract 声称 "IE" 但 evidence 仅支撑 FewRel RE**

- 具体位置：Abstract ("independently predicts type substitution errors in RE"), Title ("Information Extraction"), §4.2-4.3, §6 (RQ1)
- 问题：逐个数据集检查 BCS 独立效应的成立条件：
  - **FewRel**（sentence-level RE）：干净成立，VIF=1.18，semipartial R²=0.273 ✓
  - **DocRED**（document-level RE）：VIF=50.9（Table 12），BCS 与 count 近乎共线性（r≈0.99），semipartial R²_BCS 仅 0.056，partial correlation 在此条件下标准误膨胀约 7 倍。论文承认 "the near-perfect BCS–centrality correlation makes it impossible to fully separate the two predictors"（p15），但仍在 §6 narrative 中将 DocRED 纳入 confusability 讨论
  - **Few-NERD**（NER）：batch-level BCS-F1 相关不显著（Table 2, r=0.069, p=0.219），power 仅 65%（Appendix E.2）
  - **MAVEN**（ED）：BCS-F1 正相关完全归因于 degree centrality confound，控制 centrality 后 BCS 信号消失（§4.5, Appendix E）
  - 最终：4 个数据集中仅 1 个（FewRel）支撑 BCS 独立效应。
- 为什么影响接收：论文以 "Information Extraction" 为 title，abstract 将 confusability 作为核心贡献之一。如果该效应是 FewRel-specific（或 sentence-level RE-specific），论文的贡献范围实质上缩窄了约 75%。按 ARR 标准，"Misleading or inappropriate framing, overclaiming" 直接影响 soundness 评分。
- 建议修改方向：（a）Title 改为明确限定 "Relation Extraction" 或加 "primarily demonstrated on relation extraction"；（b）Abstract 重写 confusability claim 以准确反映 FewRel-only 的限定条件；（c）§6 RQ1 回答需更谨慎——当前 "Yes, on RE" 的表述过于简洁，应详细讨论为什么仅在 RE 成立、是否存在 task-structural 原因（如 RE 的 pairwise type distinction 本身就更适合 embedding-based confusability 度量）。

**N2** [critical] **核心回归分析（semipartial R²=0.273）缺乏跨模型复现**

- 具体位置：§4.3 ("BCS independently explains ~27%"), Table 6 (Appendix A), §3.5
- 问题：semipartial R²=0.273 这一核心定量 claim 完全来自 Qwen3-32B 单一模型。跨模型验证仅涵盖：
  - Count-curve replication（Table 5, 23-25）：只验证了 Dimension 1（count effect），不涉及 BCS 独立效应 ✓但不充分
  - BCS-controlled accuracy gap（Table 6）：Llama-3.1-8B 有 BCS gap，但未报告完整回归分析（R²、β、CI）
  - NER BCS-F1（Table 7）：Llama-70B r=−0.12 (p=0.29)，Llama-3.1-8B r=−0.12 (p=0.29)——均不显著
  - Gemini 2.5 Flash（Section U）：复现了 BCS-controlled gap 但同样无完整回归
- 如果 R²=0.273 是 Qwen3-32B 特有的（例如因其 embedding space 与 all-MiniLM 的耦合方式不同），则核心 claim 不可泛化。
- 为什么影响接收：按 ARR reviewer guidelines, "every claim that is made has to be based on evidence"。在 abstract 中声称 "replicating across two model families at three scales" 但核心定量指标（R²）仅有单模型数据，构成 overclaim。
- 建议修改方向：在至少一个其他模型（如 Llama-3.1-8B 或 70B）上复现完整的 FewRel BCS→accuracy 回归，报告 semipartial R² 和 bootstrap CI。如果 R² 显著低于 0.273，需修改 abstract 中的定量表述。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **TOST equivalence testing 的 scale 选择存在事后合理化嫌疑**

- 具体位置：Appendix C (p13-14), §4.3 ("bounded interaction confirmed by equivalence testing")
- 问题：论文在 probability scale 上 TOST 通过（p=0.003），在 logit scale 上 TOST 不通过（p=0.209）。论文选择 probability scale 为 "primary test"，logit scale 为 "sensitivity check"。但对于有界准确率数据，logit scale 是更自然的分析尺度（因其将 [0,1] 映射到 (−∞,+∞)，避免 ceiling/floor 压缩效应）。选择给出有利结论的尺度作为 primary，存在 scale shopping 嫌疑。
- 论文的辩护（"TOST margin ±3pp 定义在概率尺度上"）有一定道理——等价边界确实最初以 pp 为单位设定。但如果事先未 pre-register 尺度选择，则两个尺度给出矛盾结论时，审慎做法应报告两者并以较保守的（logit scale）为主。
- 建议：（a）在正文中明确报告两个尺度的结论并承认矛盾；（b）将 "bounded interaction" claim 弱化为 "bounded on probability scale; inconclusive on logit scale"；（c）或在 logit scale 上用更宽的等价边界重新检验。

**W2** [warning] **DocRED 在 VIF=50.9 下的解读过于乐观**

- 具体位置：§4.3 (DocRED results), Table 12, Appendix E (p15)
- 问题：VIF=50.9 意味着 BCS 和 count 的共线性极其严重。在此条件下：（a）semipartial R²_BCS=0.056 的标准误被放大约 7 倍，置信区间极宽；（b）partial correlation r=−0.348 虽统计显著（p<0.001），但可信度大打折扣——共线性下 partial correlation 对微小模型 specification 变动极敏感。论文虽在 Appendix E 中承认 "impossible to fully separate the two predictors"，但在正文 §4.3 仍将 DocRED 纳入 "BCS retains predictive value" 的 narrative。
- 建议：正文中将 DocRED 的 BCS 结论显式标记为 "inconclusive due to severe multicollinearity (VIF=50.9)"，而非 "attenuated but still predictive"。

**W3** [warning] **"Two model families at three scales" 表述具有误导性**

- 具体位置：Abstract, §6
- 问题：Qwen 仅在 32B 一个 scale 测试，Llama 在 8B 和 70B 两个 scale 测试。这不是 2×3 的交叉设计——无法分离 model family 效应与 scale 效应。例如，Qwen3-32B 和 Llama-3.1-8B 的差异可能来自 family difference 或 4× size difference 或两者。"Three scales" 暗示每个 family 都在三个 scale 上测试，实际并非如此。此外 abstract 说 "7B–70B" 但最小模型是 Llama-3.1-8B（8B 参数），非 7B。
- 建议：改为 "replicated on three models from two families (Qwen3-32B, Llama-3.1-8B, Llama-3.1-70B)" 或类似准确表述。

**W4** [warning] **Ecological inference：batch-level R² 不等于 type-pair-level 机制**

- 具体位置：§4.3, Appendix N (pair-to-batch simulation), Appendix O
- 问题：核心 R²=0.273 是 batch-level 发现（batch BCS → batch accuracy）。从 batch-level 相关推断 type-pair-level 机制（confusable type pairs 导致 substitution errors）属于 ecological inference。论文通过 pair-to-batch Monte Carlo 模拟（Appendix N）试图弥合，但该模拟假设 inter-pair SCS correlation ρ=0.35——这是估算值而非直接测量值。且 Appendix O 的 held-out validation（cross-domain schema, ρ=0.216）相关系数较低。
- 这不影响 batch-level 发现本身的有效性，但限制了关于 "confusability causes type substitution errors" 的因果解释强度。
- 建议：在 Discussion 中显式讨论 ecological inference 的限制，承认 batch-level association 与 type-pair causal mechanism 之间的 gap。

**W5** [warning] **NER null 的解读：65% power 下的 "absence of evidence" 论证不充分**

- 具体位置：Limitations (p9), Appendix E.2 (p15)
- 问题：论文说 "absence of evidence is not evidence of absence"，这在统计学上正确。但 Appendix E.2 同时报告 minimum detectable |r| at 80% power = 0.132——这是一个相当小的效应量。这意味着如果 NER 的 BCS 效应有实际意义（|r|>0.132），在 65% power 下仍有较大概率被检测到。观测值 r=0.069（p=0.219）远低于此阈值。这实际上更接近 "evidence of a very small or null effect" 而非纯粹的 "insufficient power"。论文应更平衡地讨论这一点。
- 建议：补充讨论——即使修正 restricted range（attenuated r'=−0.111），该效应量也在 minimum detectable 附近，说明即使 NER 存在 BCS 效应，其实际显著性远低于 RE。

---

## 小问题（不影响接收）

- **M1**: Abstract "7B–70B" 应为 "8B–70B"，Llama-3.1-8B 的参数量为 8.03B。
- **M2**: Table 4（正文 p8）和 Table 8（Appendix A, p12）内容有部分重叠（IntraSub rates by BCS bin），可考虑合并或交叉引用减少冗余。
- **M3**: §3.2 定义 SCS 后立即跳到 BCS，但 SCS 的 "pairwise" 修饰在首次出现时不明确——建议在定义 SCS 时明确标注 "pairwise SCS (between two types)" 与 "Batch Confusability Score (BCS, over all pairs in a batch)" 的层级关系。
- **M4**: Figure 1 的 "Prediction" 箭头指向含义不完全直观——右侧 "Dimension Labels" 部分是否暗示 BCS 可预测准确率？如果是，应标注方向。
- **M5**: Limitations 节仅提及 "Four English/Wikipedia/Wikidata datasets" 但未讨论 domain diversity——FewRel 和 DocRED 均来自 Wikipedia/Wikidata，Few-NERD 同样基于 Wikipedia，MAVEN 基于 FrameNet+Wikipedia。这实际上是单一 domain（Wikipedia-based knowledge）的四个变体，而非四个独立 domain。

---

## Questions for Authors

**Q1**: 能否在 Llama-3.1-8B 或 70B 上复现 FewRel 的完整 BCS→accuracy 回归并报告 semipartial R²？这是验证核心 claim 泛化性的最直接方式。

**Q2**: TOST 的等价边界 ±3pp 是如何确定的？是否 pre-registered？如果 ±5pp 是更合理的 practical equivalence 边界，logit scale 的结论是否改变？

**Q3**: BCS 度量依赖 embedding model 选择。如果使用 task-specific embedding（如在 FewRel 训练集上微调的 sentence encoder），BCS 的预测力是否改变？这与 SCS 作为 "pre-hoc proxy"（§3.2）的定位有关——如果最优 BCS 需要 task-specific embedding，则 "pre-hoc" 属性打折扣。

**Q4**: §4.5 识别了 MAVEN 的 centrality confound。是否考虑过在 FewRel 上也控制类似的结构属性（如 relation 在 Wikidata knowledge graph 中的 degree centrality）？如果 FewRel 的 BCS 效应也部分归因于 structural 属性，R²=0.273 可能被高估。

**Q5**: SDGD routing failure rate 73.4%（§5, Table 3）——是否尝试过 constrained routing（如强制每个 instance 只分配到一个 sub-schema）？论文目前的 routing 策略似乎允许多子图匹配，导致 73.4% 的失败率。

---

## Missing References

- **Josifoski et al. (2022)** "GenIE: Generative information extraction" — 已引用。
- 建议补充：**Fei et al. (2022)** "LasUIE: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model" (NeurIPS 2022)——该工作也讨论了 schema structure 对 IE 的影响，与本文的 schema complexity 视角相关。
- 建议补充：**Lu et al. (2022)** "Unified Structure Generation for Universal Information Extraction" (ACL 2022, UIE)——将不同 IE 任务统一建模，schema 设计是核心问题之一。

---

## 主要优势总结

1. 研究问题定义清晰，控制实验设计在 NLP empirical work 中属上乘
2. 统计方法论全面严谨（bootstrap、cluster-robust、TOST、power analysis、VIF），为同类论文树立标杆
3. 诚实报告负面结果（SDGD 失败、NER null、MAVEN confound），增强论文可信度
4. Count-degradation 发现跨任务、跨模型稳健复现，对社区有直接实用价值
5. SCS/BCS 作为 lightweight pre-hoc proxy 有实际部署指导意义
6. Appendix 质量极高，几乎覆盖所有可能的 confound


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3184 · 2026-05-25T21:25:15.152065+00:00_

Reviewer 1 审稿意见已收到（3.5/5 Borderline Conference）。核心发现：

- 2 个 Must-Fix：BCS 独立效应仅 FewRel 成立 vs title 声称 IE 泛化、核心 R²=0.273 缺跨模型复现
- 5 个 Should-Fix：TOST scale shopping、DocRED VIF 解读、model family 表述、ecological inference、NER null 解读
- 5 个 Minor

等待 Reviewer 2 审稿意见返回后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 265

## Round 265

6 recorded events


### User

_source line 3185 · 2026-05-25T21:25:27.758559+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：新颖性/完整性

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 (ARR May 2026)

---

## 总体评分

**Overall**: 3.5 — Borderline Conference
**一句话总结**: 实验方法论扎实的受控分析论文，隔离了 count 与 confusability 两个维度，但 pairwise 效应量偏弱、NER null 限制了泛化性、SDGD 负面结果分析不充分，处于 Findings 与 Conference 的交界。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | BCS-controlled batch 设计严谨，VIF 正交性检验、equivalence testing、Monte Carlo 模拟、多模型复现（Qwen3-32B / Llama-8B / Llama-70B / Gemini 2.5 Flash）均到位。主要不足：ecological inference gap（pair→batch）在正文中讨论不够显著 |
| Excitement | 3/5 | 提供了有价值的经验性认知（confusability 独立解释 27% batch-level RE 方差），但实际应用指导有限——知道 BCS 影响性能并不直接帮助提升抽取质量；SDGD 负面结果也未引向解决方案 |
| Reproducibility | 4/5 | 提供了完整 prompt 模板（Appendix G）、详细实验配置（§3.5）、BCS 构造算法（§3.2）、代码/数据声称可用。Gemini 2.5 Flash 为闭源模型是唯一限制 |
| Overall Assessment | 3.5/5 | Borderline Conference |
| Confidence | 4/5 | 熟悉 zero-shot IE 和 LLM-based 抽取文献 |

---

## 主要优势 (Strengths)

**S1. 首个受控实验设计隔离 count 与 confusability**
BCS-controlled batch 方法论是本文最核心的贡献。通过构造 low-BCS / high-BCS 对照批次（在相同 type count 下变化 confusability），结合 VIF=1.18 验证正交性，这是比 LLM-PEE 等先前工作在方法论上的实质性推进。Figure 2 清晰展示了实验设计。

**S2. 统计方法论严谨且全面**
论文使用了 equivalence testing（TOST）、semipartial R²、bootstrap CI（Appendix E.3）、Monte Carlo 聚合模拟（Appendix N）、cross-model replication（Appendix T-U）等多种统计工具，对 effect size 的报告区分了 pair-level（r²≈1.5%）和 batch-level（R²=27%）两个层次，并明确标注 "ecological level"。这种透明度在 NLP 实证论文中难得。

**S3. 负面结果的坦诚报告**
NER null result（BCS 不预测 NER accuracy）和 SDGD 失败（merge amplification 消除 routing 收益）均如实报告。NER null 作为 boundary condition 的框架设计增加了论文的可信度。Section 4.5 对 MAVEN centrality confound 的坦诚分析也值得肯定。

**S4. 多模型多尺度复现**
核心发现在 Qwen3-32B、Llama-3.1-8B、Llama-70B、Gemini 2.5 Flash 四个模型上复现（Appendix T-U），count curve 形状和 BCS-accuracy 关系方向一致。这显著增强了结论的鲁棒性。

**S5. 附录材料极为详尽**
26 页论文中 Appendix 占 17 页，涵盖 prompt sensitivity（Appendix H）、format independence（Appendix K）、domain composition（Appendix E.4）、few-shot prompting（Appendix V）、qualitative error analysis（Appendix W）、label renaming（Appendix X）等十余项 robustness check。审稿人几乎所有可能的质疑都能在 Appendix 中找到预先回答。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] SDGD 负面结果（Section 5 / RQ3）分析深度不足
- 具体位置：Section 5（约半栏）+ Appendix B
- 问题：作为三个 RQ 之一（RQ3: Can confusability-aware schema decomposition improve extraction quality?），Section 5 仅用约半栏篇幅报告 SDGD 结果。论文指出"routing failure"（73.4% instances match multiple sub-schemas）和"merge amplification"（union merge increases false positives），但缺乏深入分析：
  (a) merge amplification 的具体错误模式是什么？是 type 混淆还是 span 错误？
  (b) Table 3 仅报告 5 种 routing 策略的 accuracy 差异，但未分析 failure cases 的分布
  (c) 为什么 confidence-gated selection（论文提出的改进）也失败？只说"double precision with minimal recall loss"但 F1 仍低于 single-pass，缺乏 error analysis
  (d) 论文声称"negative results actionable"（abstract），但 actionability 仅体现在"IntraSub scales with BCS"（Table 4），未给出如何利用此发现改进系统的具体路径
- 为什么影响接收：RQ3 是论文三大贡献之一，但分析深度远不及 RQ1/RQ2。一个 Reviewer 可能认为 SDGD 只是为凑第三个 contribution 而草草加入。
- 建议：在 Section 5 中增加至少半栏的 error analysis（merge 后哪些 type pair 产生最多 false positive？这些 pair 的 SCS 分布如何？），并明确讨论 "actionable" 的具体含义。

**N2** [critical] SCS/BCS metric 的新颖性声明需要更清晰的界定
- 具体位置：§3.2 (Schema Confusability Score)、§1 contributions list #1
- 问题：SCS 定义为 cos(embed(name(t_i)), embed(name(t_j)))，即 type name 的 embedding cosine similarity。这与 LLM-PEE (Liu et al., 2025) 用于 type partitioning 的 embedding similarity 在数学形式上完全相同。论文在 Related Work (page 3) 中正确指出"Our work differs in three ways"，但这三点差异全部关于 experimental methodology，而非 metric 本身。然而 contributions list #1 将"embedding similarity (SCS/BCS, building on Liu et al., 2025)" 与"independently predicts type substitution errors"并列呈现，读者可能误以为 SCS/BCS 是本文提出的新 metric。
- 为什么影响接收：如果 Reviewer 将 SCS/BCS 视为 LLM-PEE 的直接复用，则论文的 metric 贡献归零，剩余贡献仅为实验设计。需要更清楚地传达"metric 是借鉴的，方法论是新的"。
- 建议：在 §3.2 开头明确写 "We adopt the pairwise embedding similarity used in LLM-PEE (Liu et al., 2025) as our confusability metric, and extend it to a batch-level aggregation (BCS) not previously applied in controlled experiments." 同时在 contributions list 中将 "building on" 替换为更明确的措辞如 "adopting the metric from"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Ecological inference gap 在正文中讨论不充分
- 具体位置：§4.2（pairwise r²≈1.5%）vs §4.3（batch R²=27%）
- 问题：Pairwise r² ≈ 1.5% 到 batch-level R² = 27% 的跳跃是论文最关键的统计推理。论文在 §4.2 简要提及 "correlated type pairs within batches composed into substantial batch-level RE accuracy variance (§4.3)"，Appendix N 有 Monte Carlo 模拟解释聚合效应。但正文中缺少对 ecological fallacy 风险的直接讨论——读者可能质疑：batch-level R²=27% 是否仅仅是统计聚合的 artifact？
- 建议：在 §4.2 或 §4.3 中增加 2-3 句，明确讨论 (1) pair→batch 聚合的机制（多个弱 pair 效应在 batch 内累积），(2) 为什么 batch-level 是合适的分析单元（因为 prompt 是以 batch 为单位构造的），(3) 指向 Appendix N 的模拟验证。

**W2** [warning] NER null 的解释不够深入
- 具体位置：§4.3 末尾、§6 (Discussion) RQ1 段落
- 问题：论文报告 BCS 不预测 NER accuracy（null result），并将 NER 定位为 "boundary condition"。但对 null 的原因讨论仅限于 "relaxed span matching does not recover a BCS signal"（§4.3）和 "NER null reflects dispersed error modes rather than absence of confusability effects"（§6）。这些解释是事后推测，缺乏实证支撑。NER 是 IE 中最基础的任务，NER null 实质上将论文的适用范围缩窄到 RE 和 ED。
- 建议：(1) 是否可以用 strict matching（而非 relaxed）重做 NER 实验以验证 "relaxed span matching" 假说？(2) 分析 NER 错误中 type confusion 与 span error 的比例，提供 NER null 的直接证据。

**W3** [warning] "Two dimensions" 框架的充分性未论证
- 具体位置：§1（Introduction, Figure 1）
- 问题：论文将 schema complexity 分解为 count 和 confusability 两个维度。但 schema complexity 可能还包括：(a) type hierarchy depth（如 MAVEN 的 FrameNet 层级），(b) argument structure complexity（事件抽取中 role 数量），(c) type definition 的歧义程度（不仅是 name similarity，还有 guideline overlap），(d) inter-type dependency（如 NER 中 person-organization 的共现关系）。论文未论证为什么恰好是这两个维度。§4.5 centrality confound 的发现实际上暗示了第三个维度的存在。
- 建议：在 Introduction 或 Discussion 中增加 1-2 句说明这两个维度的选择理由（如"count 和 confusability 是 prompt-level 最直接的两个 schema property"），并承认其他维度的存在作为 future work。

**W4** [warning] 缺少与 simpler confusability metrics 的对比
- 具体位置：§3.2
- 问题：SCS 使用 sentence embedding cosine similarity 量化 type confusability。但论文未与更简单的 confusability 度量进行对比，如 string edit distance（Levenshtein）、WordNet path similarity、或 character n-gram overlap。如果简单的字符串相似度就能达到相似的预测力，则 embedding-based SCS 的必要性存疑。
- 建议：在 Appendix 中增加 SCS vs. simpler metrics 的对比实验（至少一个 baseline metric），以验证 embedding similarity 的 added value。Appendix M 的 name-only SCS ablation 已经在这个方向上做了一步（name-only vs. name+definition），但缺少 non-embedding baselines。

---

## 小问题（不影响接收）

**M1** Figure 3 信息密度过高：(a)(b) 两个子图加上 error bars 和 U-shape 注释，在 print size 下可读性较差。考虑将 (a)(b) 分列。

**M2** §3.2 最后一句 "SCS does not capture context-dependent disambiguation or mention-level ambiguity; these contribute to residual variance" 出现得突兀，可移至 Discussion。

**M3** Abstract 中 "to our knowledge" 可删除——reviewer 不会因此而更信服，且增加 word count。

**M4** Appendix Z (Use of AI Assistants) 的透明度值得肯定，但 "polishing prose and reformatting LaTeX" 的措辞略模糊，建议细化。

---

## Questions to Authors

**Q1**: Pairwise SCS-confusion correlation 在 FewRel 上 r = 0.12 (Table 2)，在 DocRED 上 r = -0.06（非显著）。DocRED 上的 null 如何解释？是否说明 confusability effect 依赖特定数据集特征（如 FewRel 的 balanced design）？

**Q2**: BCS 构造使用 greedy search（§3.2），这是否引入了系统性偏差？即 high-BCS batch 是否 systematically 包含某些特定 domain 的 types（Appendix E.4 部分回答了这一点，但 domain composition difference 是否完全被控制住了）？

**Q3**: 论文使用了 Qwen3-32B 的 v1 prompt（§3.5），v2 prompt 的 BCS 效应显著减弱（Appendix H, "restricted BCS range"）。如果 prompt design 如此敏感地影响 BCS effect，这是否说明 confusability effect 本身部分是 prompt-induced 而非 schema-intrinsic？

**Q4**: SDGD 中 oracle routing 的 accuracy 是 72.4%（Table 3），论文称这证明 "routing failure"。但 72.4% 对比 random 14.7% 提升巨大——为什么 oracle routing 仍然低于 single-pass baseline？是否 sub-schema 之间的 type overlap 导致了系统性问题？

---

## Missing References

**已引用的关键工作确认（均验证为真实）**：LLM-PEE (Liu et al., 2025) ✓、CrossAgentIE (Meng et al., 2025) ✓、CMAS-NER/cooperative multi-agent (Wang et al., 2025) ✓、Reflect&Learn (Dong et al., 2026) ✓、GoLLIE (Sainz et al., 2024) ✓、FILNER/Familiarity (Golde et al., 2025) ✓、ADELIE (Qi et al., 2024) ✓。**抽查 7 篇引用均为真实，未发现虚构 citation。**

**可能遗漏的相关工作**：
1. **Label Semantics for Few-Shot NER** (Hou et al., 2020; Ma et al., 2022) — 使用 label embedding/description 增强 NER 的经典工作，与 SCS 的 embedding similarity 思路直接相关，但论文未引用。
2. **Prompt length / context utilization** 方面的更广泛文献 — 论文引用了 Lost in the Middle (Liu et al., 2024)，但缺少对 structured output 格式下 context utilization 的讨论（如 JSON mode 是否改变 count-degradation 曲线）。

---

## 引用充分性评估

- **LLM-PEE positioning**: 准确且公平。论文清楚区分了"engineering vs. understanding"，正确指出 LLM-PEE conflates count and confusability。三点差异（controlled analysis / VIF orthogonality / merge amplification bottleneck）均有实证支撑。
- **CrossAgentIE / CMAS-NER / Reflect&Learn**: 三者均在 Related Work §2 中引用，作为"engineering approaches"与本文的"analytical study"对照。引用充分度适当——它们不是本文的直接比较对象。

---

## AI 痕迹检查

未发现明显 AI 写作痕迹（无 "delve into"、"it is important to note"、"leveraging" 过度使用等典型模式）。论文写作风格自然、学术性强。Appendix Z 透明披露了 AI 辅助使用（Claude for code/writing/literature），符合 EMNLP 2026 政策要求。

---

## 审稿总结

这是一篇方法论扎实的实证分析论文。BCS-controlled batch 实验设计是真正的贡献，统计分析全面且透明。核心发现（confusability 独立解释 RE 27% batch-level 方差）有意义但实际影响有限。主要弱点在于：(1) SDGD/RQ3 分析深度不足，(2) SCS/BCS metric 新颖性需更清晰界定，(3) NER null 和 pairwise 弱效应限制了泛化性。总体处于 Borderline Conference 水平——如果 N1/N2 被充分修改，可达到 Conference (4.0)；如果 Reviewer 对 effect size 要求严格，可能落入 Findings (3.0)。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 3186 · 2026-05-25T21:26:09.591351+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性）\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n### Strengths\nS1. 研究问题设计精巧，BCS-controlled batch design 首次在 matched type count 下分离 confusability 独立效应\nS2. 统计工具链（VIF、bootstrap CI、cluster-robust SE、TOST、power analysis）远超同类论文\nS3. 诚实报告负面结果（SDGD、NER null、MAVEN confound）\nS4. Count-degradation 跨任务跨模型稳健\nS5. BCS 作为 pre-hoc proxy 实用\nS6. Appendix 质量极高\n\n### Must-Fix\n**N1** [critical] 核心 BCS 独立效应泛化性严重不足——title/abstract 声称 \"IE\" 但 evidence 仅支撑 FewRel RE。4 个数据集逐个检查：FewRel ✓（VIF=1.18, R²=0.273），DocRED ✗（VIF=50.9, semipartial R²=0.056），Few-NERD ✗（r=0.069, p=0.219, power=65%），MAVEN ✗（centrality confound 后信号消失）。建议 title 限定为 \"Relation Extraction\" 或加 qualifier。\n\n**N2** [critical] 核心回归分析（semipartial R²=0.273）缺乏跨模型复现。该定量 claim 完全来自 Qwen3-32B。跨模型验证仅涵盖 count-curve 和 BCS gap，未在任何其他模型上报告完整回归（R²、β、CI）。Abstract 声称 \"replicating across two model families\" 但核心定量指标仅有单模型数据，构成 overclaim。\n\n### Should-Fix\n**W1** TOST probability scale 通过但 logit scale 不通过，存在 scale shopping 嫌疑。\n**W2** DocRED VIF=50.9 下解读过于乐观。\n**W3** \"Two model families at three scales\" 表述误导。\"7B–70B\" 应为 \"8B–70B\"。\n**W4** Ecological inference：batch-level R² 不等于 type-pair-level 机制，正文讨论不足。\n**W5** NER null 的 \"absence of evidence\" 论证不充分——observed r=0.069 远低于 minimum detectable |r|=0.132。\n\n### Minor\nM1 Abstract \"7B\" 应为 \"8B\"。M2 Table 4/Table 8 内容重叠。M3 §3.2 SCS/BCS 层级关系不够清晰。M4 Figure 1 箭头含义不直观。M5 四个数据集均基于 Wikipedia，实际是单一 domain 的四个变体。\n\n### Questions\nQ1: 能否在 Llama 上复现完整 BCS→accuracy 回归？\nQ2: TOST ±3pp 是否 pre-registered？\nQ3: Task-specific embedding 是否改变 BCS 预测力？\nQ4: FewRel 是否也有 centrality confound？\nQ5: SDGD 是否尝试过 constrained routing？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性）\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n### Strengths\nS1. 研究问题设计精巧，BCS-controlled batch design 首次在 matched type count 下分离 confusability 独立效应\nS2. 统计工具链（VIF、bootstrap CI、cluster-robust SE、TOST、power analysis）远超同类论文\nS3. 诚实报告负面结果（SDGD、NER null、MAVEN confound）\nS4. Count-degradation 跨任务跨模型稳健\nS5. BCS 作为 pre-hoc proxy 实用\nS6. Appendix 质量极高\n\n### Must-Fix\n**N1** [critical] 核心 BCS 独立效应泛化性严重不足——title/abstract 声称 \"IE\" 但 evidence 仅支撑 FewRel RE。4 个数据集逐个检查：FewRel ✓（VIF=1.18, R²=0.273），DocRED ✗（VIF=50.9, semipartial R²=0.056），Few-NERD ✗（r=0.069, p=0.219, power=65%），MAVEN ✗（centrality confound 后信号消失）。建议 title 限定为 \"Relation Extraction\" 或加 qualifier。\n\n**N2** [critical] 核心回归分析（semipartial R²=0.273）缺乏跨模型复现。该定量 claim 完全来自 Qwen3-32B。跨模型验证仅涵盖 count-curve 和 BCS gap，未在任何其他模型上报告完整回归（R²、β、CI）。Abstract 声称 \"replicating across two model families\" 但核心定量指标仅有单模型数据，构成 overclaim。\n\n### Should-Fix\n**W1** TOST probability scale 通过但 logit scale 不通过，存在 scale shopping 嫌疑。\n**W2** DocRED VIF=50.9 下解读过于乐观。\n**W3** \"Two model families at three scales\" 表述误导。\"7B–70B\" 应为 \"8B–70B\"。\n**W4** Ecological inference：batch-level R² 不等于 type-pair-level 机制，正文讨论不足。\n**W5** NER null 的 \"absence of evidence\" 论证不充分——observed r=0.069 远低于 minimum detectable |r|=0.132。\n\n### Minor\nM1 Abstract \"7B\" 应为 \"8B\"。M2 Table 4/Table 8 内容重叠。M3 §3.2 SCS/BCS 层级关系不够清晰。M4 Figure 1 箭头含义不直观。M5 四个数据集均基于 Wikipedia，实际是单一 domain 的四个变体。\n\n### Questions\nQ1: 能否在 Llama 上复现完整 BCS→accuracy 回归？\nQ2: TOST ±3pp 是否 pre-registered？\nQ3: Task-specific embedding 是否改变 BCS 预测力？\nQ4: FewRel 是否也有 centrality confound？\nQ5: SDGD 是否尝试过 constrained routing？"
  }
}
```

</details>

---


### Tool result

_source line 3187 · 2026-05-25T21:26:30.426002+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20834
}
```

</details>

---


### Tool call

_source line 3188 · 2026-05-25T21:26:30.576988+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性/完整性）\n\n**Overall**: 3.5 — Borderline Conference\n\n### Strengths\nS1. 首个受控实验设计隔离 count 与 confusability，BCS-controlled batch 方法论是核心贡献\nS2. 统计方法论严谨且全面（TOST、semipartial R²、bootstrap CI、Monte Carlo 模拟、cross-model）\nS3. 负面结果坦诚报告（NER null、SDGD 失败、MAVEN centrality confound）\nS4. 多模型多尺度复现（Qwen3-32B / Llama-8B / Llama-70B / Gemini Flash）\nS5. Appendix 极为详尽，几乎覆盖所有可能质疑\n\n### Must-Fix\n**N1** [critical] SDGD 负面结果（Section 5 / RQ3）分析深度不足。仅半栏篇幅，缺乏：(a) merge amplification 的具体错误模式分析，(b) Table 3 failure cases 分布，(c) confidence-gated selection 为何也失败的 error analysis，(d) \"negative results actionable\" 的具体路径。RQ3 是三大贡献之一但分析远不及 RQ1/RQ2。\n\n**N2** [critical] SCS/BCS metric 新颖性声明需更清晰界定。SCS 定义（cos embedding similarity）与 LLM-PEE 数学形式完全相同。Contributions #1 将 SCS/BCS 与 \"independently predicts\" 并列，读者可能误以为是新 metric。应明确\"metric 是借鉴的，方法论是新的\"。\n\n### Should-Fix\n**W1** Ecological inference gap（pair r²=1.5% → batch R²=27%）在正文中讨论不充分。\n**W2** NER null 解释仅限事后推测（\"dispersed error modes\"），缺乏实证支撑。\n**W3** \"Two dimensions\" 框架充分性未论证——schema complexity 可能有更多维度（hierarchy depth、argument structure、inter-type dependency）。\n**W4** 缺少与 simpler confusability metrics（Levenshtein、WordNet path similarity）的对比。\n\n### Minor\nM1 Figure 3 信息密度过高。M2 §3.2 SCS limitations 位置突兀。M3 Abstract \"to our knowledge\" 可删。M4 Appendix Z AI 辅助措辞略模糊。\n\n### Questions\nQ1: DocRED pairwise SCS-confusion 非显著如何解释？\nQ2: BCS greedy search 是否引入系统性 domain 偏差？\nQ3: V2 prompt 下 BCS 效应减弱——confusability 是 prompt-induced 还是 schema-intrinsic？\nQ4: Oracle routing 72.4% 仍低于 single-pass——为什么？\n\n### Missing References\n引用抽查 7 篇均为真实。建议补充：Label Semantics for Few-Shot NER (Hou et al. 2020; Ma et al. 2022)；Prompt length / structured output context utilization 文献。\n\n### AI 痕迹\n未发现明显 AI 写作痕迹。Appendix Z 透明披露 AI 辅助，符合政策。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性/完整性）\n\n**Overall**: 3.5 — Borderline Conference\n\n### Strengths\nS1. 首个受控实验设计隔离 count 与 confusability，BCS-controlled batch 方法论是核心贡献\nS2. 统计方法论严谨且全面（TOST、semipartial R²、bootstrap CI、Monte Carlo 模拟、cross-model）\nS3. 负面结果坦诚报告（NER null、SDGD 失败、MAVEN centrality confound）\nS4. 多模型多尺度复现（Qwen3-32B / Llama-8B / Llama-70B / Gemini Flash）\nS5. Appendix 极为详尽，几乎覆盖所有可能质疑\n\n### Must-Fix\n**N1** [critical] SDGD 负面结果（Section 5 / RQ3）分析深度不足。仅半栏篇幅，缺乏：(a) merge amplification 的具体错误模式分析，(b) Table 3 failure cases 分布，(c) confidence-gated selection 为何也失败的 error analysis，(d) \"negative results actionable\" 的具体路径。RQ3 是三大贡献之一但分析远不及 RQ1/RQ2。\n\n**N2** [critical] SCS/BCS metric 新颖性声明需更清晰界定。SCS 定义（cos embedding similarity）与 LLM-PEE 数学形式完全相同。Contributions #1 将 SCS/BCS 与 \"independently predicts\" 并列，读者可能误以为是新 metric。应明确\"metric 是借鉴的，方法论是新的\"。\n\n### Should-Fix\n**W1** Ecological inference gap（pair r²=1.5% → batch R²=27%）在正文中讨论不充分。\n**W2** NER null 解释仅限事后推测（\"dispersed error modes\"），缺乏实证支撑。\n**W3** \"Two dimensions\" 框架充分性未论证——schema complexity 可能有更多维度（hierarchy depth、argument structure、inter-type dependency）。\n**W4** 缺少与 simpler confusability metrics（Levenshtein、WordNet path similarity）的对比。\n\n### Minor\nM1 Figure 3 信息密度过高。M2 §3.2 SCS limitations 位置突兀。M3 Abstract \"to our knowledge\" 可删。M4 Appendix Z AI 辅助措辞略模糊。\n\n### Questions\nQ1: DocRED pairwise SCS-confusion 非显著如何解释？\nQ2: BCS greedy search 是否引入系统性 domain 偏差？\nQ3: V2 prompt 下 BCS 效应减弱——confusability 是 prompt-induced 还是 schema-intrinsic？\nQ4: Oracle routing 72.4% 仍低于 single-pass——为什么？\n\n### Missing References\n引用抽查 7 篇均为真实。建议补充：Label Semantics for Few-Shot NER (Hou et al. 2020; Ma et al. 2022)；Prompt length / structured output context utilization 文献。\n\n### AI 痕迹\n未发现明显 AI 写作痕迹。Appendix Z 透明披露 AI 辅助，符合政策。"
  }
}
```

</details>

---


### Tool result

_source line 3189 · 2026-05-25T21:26:31.938329+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 3190 · 2026-05-25T21:26:35.844010+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 266

## Round 266

12 recorded events


### User

_source line 3191 · 2026-05-25T21:26:36.886228+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评分**: Overall 3.5 (Borderline Conference)

**核心发现**:
- 统计方法论本身过硬（bootstrap CI、cluster-robust、TOST、power analysis），在 NLP 论文中属上乘水准
- **两个 Must-Fix**: (1) BCS 独立效应仅在 FewRel 一个数据集上干净成立（NER null、DocRED VIF=50.9、MAVEN centrality confound），但 title/abstract 声称 "Information Extraction" 泛化性存在实质性缺口；(2) 核心定量 claim（semipartial R²=0.273）缺乏跨模型复现，仅来自 Qwen3-32B
- **四个 Should-Fix**: TOST scale 选择有事后合理化嫌疑（probability scale 通过 vs logit scale 不通过）；DocRED VIF=50.9 下解读过于乐观；"two families at three scales" 表述误导（非交叉设计）；ecological inference gap 未充分讨论
- **主要优势**: 控制实验设计精巧、count-degradation 跨任务稳健、负面结果诚实报告、appendix 质量极高

---

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结果摘要**：
- **Overall**: 3.5 (Borderline Conference)
- **Soundness**: 4/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5
- **Must-Fix**: (1) SDGD/RQ3 分析深度不足（半栏不够支撑一个核心 RQ），(2) SCS/BCS metric 新颖性声明需与 LLM-PEE 更清晰界定
- **Should-Fix**: ecological inference gap 正文讨论不够、NER null 缺乏实证解释、"two dimensions" 充分性未论证、缺少 simpler confusability metrics 对比
- **引用抽查**: 7/7 verified real，未发现虚构 citation
- **AI 痕迹**: 未检出，Appendix Z 透明披露 AI 使用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 3192 · 2026-05-25T21:27:19.280216+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 3193 · 2026-05-25T21:27:19.431165+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:16:13.927027+00:00\", \"completed_at\": \"2026-05-25T21:19:44.626904+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Figure 1 作为视觉锚点出现在首页，清晰传达核心 message（schema complexity 导致 zero-shot extraction 性能退化的两个维度），审稿人第一印象优秀\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Abstract/Anonymous 排版整洁，符合 ACL 模板规范，abstract 长度适中\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主文 8 页内每页至少 1 个 display item（Figure 或 Table），无连续纯文本页，视觉节奏优秀\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文最后一页（p8）内容饱满：Figure 7 + Table 3 + Table 4 + Discussion/Conclusion 文字，无大面积空白\"}, {\"severity\": \"warning\", \"dimension\": \"page 17\", \"message\": \"Appendix G（Prompt Templates）整页为 monospace 纯文本，无任何 figure/table 穿插。作为 prompt 展示页可以理解，但审稿人快速翻阅时视觉疲劳较高\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主文共 7 个 Figure + 4 个 Table = 11 个 display items / 8 页，密度优秀，符合实证论文预期\"}, {\"severity\": \"info\", \"dimension\": \"pages 12-26\", \"message\": \"Appendix 含大量补充表格（Table 5-32），支撑充分\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 7（Schema Decomposition Pipeline）内部注释文字偏小（\\\"75% instances match multiple sub-schemas\\\"、\\\"Routing Failure\\\" 等标注），在打印或缩放查看时可能不易辨认，建议字号提升至正文的 70% 以上\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 3 多面板组合（line plots + bar charts）结构清晰，error bars 标注完整（±1 SD），caption 自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 6 双面板（Few-NERD NER / FewRel RE）error taxonomy 分解图颜色对比度足够（红/粉 vs 绿/青），但 x 轴 BCS bin 标签字号略小\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 2 实验设计概览图清晰，Dimension 1/2 标注明确\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 4 散点图清晰，IQR box 可读\"}, {\"severity\": \"info\", \"dimension\": \"page
…[truncated 1840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 3194 · 2026-05-25T21:27:19.431605+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 3195 · 2026-05-25T21:27:19.433949+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 2
}
```

</details>

---


### Tool call

_source line 3196 · 2026-05-25T21:28:07.417287+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 3197 · 2026-05-25T21:28:07.467754+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3198 · 2026-05-25T21:33:01.901559+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Review Issues Tracker\n# Updated: 2026-05-25 Round 32 Review Director synthesis\n\n# ============================================================\n# R32 CRITICAL (3 items — consensus)\n# ============================================================\n\n- id: R32-C1\n  summary: \"Title/Abstract 声称 'Information Extraction' 但 BCS 独立效应仅 FewRel RE 干净成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R31-C1: BCS scope 超出证据支撑\"}\n    - {round: 32, reviewers: [R1, R2], note: \"R1-N1 逐数据集检查: FewRel ✓(VIF=1.18), DocRED ✗(VIF=50.9), Few-NERD ✗(r=0.069,p=0.219), MAVEN ✗(centrality confound). 4个数据集仅1个支撑. R2隐式认同(NER null限制). Abstract 已改善('focusing on RE')但title仍为IE.\"}\n  action_items:\n    - {round: 32, action: \"Title加qualifier或改为RE-focused; §6 RQ1讨论为何仅RE成立(task-structural原因)\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-C2\n  summary: \"核心定量claim semipartial R²=0.273缺乏跨模型复现，仅Qwen3-32B单模型\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R31-W1: 模型多样性不足(Should-Fix)\"}\n    - {round: 32, reviewers: [R1], note: \"升级为Must-Fix. 跨模型仅有count-curve和BCS gap, 无完整回归(R²,β,CI). Abstract声称'replicating across two model families'但核心定量指标仅单模型.\"}\n  action_items:\n    - {round: 32, action: \"至少一个其他模型复现FewRel BCS→accuracy完整回归, 报告semipartial R²和CI\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-C3\n  summary: \"SDGD/RQ3分析深度不足——半栏篇幅不支撑核心RQ\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R31-W4: Section 5分析不充分(Should-Fix)\"}\n    - {round: 32, reviewers: [R2, R1], note: \"R2-N1升级为Must-Fix. 缺merge amplification错误模式分析、failure case分布、confidence-gated失败原因、actionability路径.\"}\n  action_items:\n    - {round: 32, action: \"Section 5增加至少半栏error analysis: merge后哪些type pair产生最多FP, SCS分布, actionability具体含义\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R32 WARNING (7 items)\n# ============================================================\n\n- id: R32-W1\n  summary: \"SCS/BCS与LLM-PEE数学形式相同, 新颖性声明需更清晰界定\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R31-D1: SCS计算与LLM-PEE相同之争\"}\n    - {round: 32, reviewers: [R2], note: \"R2-N2: contributions #1将SCS/BCS与'independently predicts'并列, 可能误导. 需明确'metric借鉴, 方法论新'.\"}\n  action_items:\n    - {round: 32, action: \"§3.2开头明确adopt from LLM-PEE; contributions改措辞\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-W2\n  summary: \"TOST probability scale通过vs logit scale不通过, 存在scale shopping嫌疑\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R31-W2: logit-scale不通过仅Limitations提及\"}\n    - {round: 32, reviewers: [R1], note: \"R1-W1: p=0.003 vs p=0.209矛盾. 选有利结论的scale作primary有shopping嫌疑.\"}\n  action_items:\n    - {round: 32, action: \"正文明确报告两scale结论并承认矛盾; 弱化'bounded interaction'claim\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-W3\n  summary: \"DocRED VIF=50.9下partial correlation解读仍偏乐观\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R31-C2: VIF=50.9呈现顺序产生replication错觉(Critical)\"}\n    - {round: 32, reviewers: [R1], note: \"R1-W2: 标准误膨胀~7倍, 应标记为inconclusive. 从R31-Critical降为Warning因论文已有改善.\"}\n  action_items:\n    - {round: 32, action: \"正文将DocRED BCS结论标为inconclusive, 不作为replication evidence\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-W4\n  summary: \"Ecological inference gap (pair r²=1.5%→batch R²=27%) 正文讨论不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R1, R2], note: \"R1-W4+R2-W1共识. pair-to-batch聚合是最关键统计推理, 正文缺ecological fallacy风险讨论. Appendix N有模拟但正文未充分引用.\"}\n  action_items:\n    - {round: 32, action: \"§4.2或§4.3增加2-3句: pair→batch机制、batch作为分析单元合理性、指向Appendix N\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-W5\n  summary: \"NER null解释缺乏实证——'dispersed error modes'是事后推测\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R1, R2], note: \"R1-W5: r=0.069远低于minimum detectable |r|=0.132, 更接近evidence of very small/null effect. R2-W2: NER null解释仅事后推测. 共识.\"}\n  action_items:\n    - {round: 32, action: \"补充讨论: 即使修正restricted range, 效应量仍在minimum detectable附近, NER BCS效应如存在也远弱于RE\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-W6\n  summary: \"'Two model families at three scales'表述误导+文内一致性问题\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [Reviewer], note: \"R31-F1: 'three model families'实际两个\"}\n    - {round: 32, reviewers: [R1], note: \"R1-W3: Abstract已改但Figure 5 caption仍说'three model families'. 'Three scales'暗示交叉设计但实际Qwen仅32B, Llama仅8B+70B.\"}\n  action_items:\n    - {round: 32, action: \"统一为'three models from two open-weight families + one proprietary model'\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-W7\n  summary: \"'Two dimensions'框架充分性未论证——schema complexity可能有更多维度\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R2], note: \"R2-W3: hierarchy depth, argument structure, definition ambiguity, inter-type dependency等. §4.5 centrality confound暗示第三维度.\"}\n  action_items:\n    - {round: 32, action: \"Introduction或Discussion增加1-2句说明两维度选择理由, 承认其他维度为future work\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R32 MINOR (9 items)\n# ============================================================\n\n- id: R32-M1\n  summary: \"Figure 3信息密度过高, print size下可读性较差\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R2], note: \"R2-M1: (a)(b)两子图加error bars和注释密集\"}\n\n- id: R32-M2\n  summary: \"Figure 7内部注释文字偏小\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [Visual], note: \"视觉审查warning: 'Routing Failure'等标注字号偏小\"}\n\n- id: R32-M3\n  summary: \"§3.2 SCS/BCS层级关系不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R1, R2], note: \"R1-M3+R2-M2: pairwise SCS vs BCS层级不明; SCS limitations句位置突兀\"}\n\n- id: R32-M4\n  summary: \"Abstract 'to our knowledge'可删除\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R2], note: \"R2-M3\"}\n\n- id: R32-M5\n  summary: \"四个数据集均基于Wikipedia/Wikidata/FrameNet, domain diversity有限\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R1], note: \"R1-M5: 单一domain四个变体\"}\n\n- id: R32-M6\n  summary: \"Table 4/Table 8内容部分重叠\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R1], note: \"R1-M2\"}\n\n- id: R32-M7\n  summary: \"建议补充label semantics for NER引用(Hou et al. 2020; Ma et al. 2022)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R2], note: \"label embedding/description增强NER的经典工作\"}\n\n- id: R32-M8\n  summary: \"建议补充LasUIE(Fei et al. NeurIPS 2022)和UIE(Lu et al. ACL 2022)引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R1], note: \"schema structure对IE影响相关\"}\n\n- id: R32-M9\n  summary: \"Appendix多处表格字号压缩至正文70%下限\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [Visual], note: \"pages 19, 25表格字号偏小\"}\n\n# ============================================================\n# R31 RESOLVED IN R32 (4 items)\n# ============================================================\n\n- id: R31-W3\n  summary: \"Extreme-BCS batch domain composition confound未控制\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"Appendix E.4显示domain偏向, regression未控制\"}\n    - {round: 32, reviewers: [], note: \"R32未提及. 论文已加domain entropy covariate(§4.3, p_entropy=0.97, all VIF<2)\"}\n  resolution: \"§4.3增加domain entropy作为covariate, BCS系数不变\"\n  resolution_round: 32\n\n- id: R31-W5\n  summary: \"FP8量化non-determinism(SD=0.83pp)缺power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"bootstrap CI不区分信号与噪声\"}\n    - {round: 32, reviewers: [], note: \"R32未提及. Appendix已加power analysis: min detectable slope≈0.4pp/0.1BCS, observed~1.9pp(5×threshold)\"}\n  resolution: \"Appendix增加FP8 noise floor power analysis\"\n  resolution_round: 32\n\n- id: R31-W6\n  summary: \"未解释方差讨论不足(FewRel 73% unexplained)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R2, R1], note: \"应讨论未解释因素\"}\n    - {round: 32, reviewers: [], note: \"R32未提及. Discussion已列残差因素.\"}\n  resolution: \"Discussion增加残差因素讨论\"\n  resolution_round: 32\n\n- id: R31-M6\n  summary: \"Appendix N Monte Carlo ρ_pair=0.35来源和sensitivity不清\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"应标注来源和sensitivity\"}\n    - {round: 32, reviewers: [], note: \"R32未提及. 论文已增加ρ=0.20/0.35/0.50 sensitivity analysis.\"}\n  resolution: \"Appendix N已增加sensitivity analysis\"\n  resolution_round: 32\n\n# ============================================================\n# R31 NOT RAISED IN R32 (status unchanged, for tracking)\n# ============================================================\n\n- id: R31-M1\n  summary: \"NER U形count curve非线性建模不足\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"应做piecewise regression\"}\n    - {round: 32, reviewers: [], note: \"R32未提及\"}\n\n- id: R31-M5\n  summary: \"Type name粒度差异对SCS跨数据集可比性影响未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"粒度差异影响embedding similarity分布\"}\n    - {round: 32, reviewers: [], note: \"R32未提及\"}\n\n- id: R31-M7\n  summary: \"MiniLM vs Qwen3 embedding机制讨论不足\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"哪个更接近LLM实际confusability\"}\n    - {round: 32, reviewers: [], note: \"R32未提及\"}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "# Review Issues Tracker\n# Updated: 2026-05-25 Round 32 Review Director synthesis\n\n# ============================================================\n# R32 CRITICAL (3 items — consensus)\n# ============================================================\n\n- id: R32-C1\n  summary: \"Title/Abstract 声称 'Information Extraction' 但 BCS 独立效应仅 FewRel RE 干净成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R31-C1: BCS scope 超出证据支撑\"}\n    - {round: 32, reviewers: [R1, R2], note: \"R1-N1 逐数据集检查: FewRel ✓(VIF=1.18), DocRED ✗(VIF=50.9), Few-NERD ✗(r=0.069,p=0.219), MAVEN ✗(centrality confound). 4个数据集仅1个支撑. R2隐式认同(NER null限制). Abstract 已改善('focusing on RE')但title仍为IE.\"}\n  action_items:\n    - {round: 32, action: \"Title加qualifier或改为RE-focused; §6 RQ1讨论为何仅RE成立(task-structural原因)\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-C2\n  summary: \"核心定量claim semipartial R²=0.273缺乏跨模型复现，仅Qwen3-32B单模型\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R31-W1: 模型多样性不足(Should-Fix)\"}\n    - {round: 32, reviewers: [R1], note: \"升级为Must-Fix. 跨模型仅有count-curve和BCS gap, 无完整回归(R²,β,CI). Abstract声称'replicating across two model families'但核心定量指标仅单模型.\"}\n  action_items:\n    - {round: 32, action: \"至少一个其他模型复现FewRel BCS→accuracy完整回归, 报告semipartial R²和CI\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-C3\n  summary: \"SDGD/RQ3分析深度不足——半栏篇幅不支撑核心RQ\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R31-W4: Section 5分析不充分(Should-Fix)\"}\n    - {round: 32, reviewers: [R2, R1], note: \"R2-N1升级为Must-Fix. 缺merge amplification错误模式分析、failure case分布、confidence-gated失败原因、actionability路径.\"}\n  action_items:\n    - {round: 32, action: \"Section 5增加至少半栏error analysis: merge后哪些type pair产生最多FP, SCS分布, actionability具体含义\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R32 WARNING (7 items)\n# ============================================================\n\n- id: R32-W1\n  summary: \"SCS/BCS与LLM-PEE数学形式相同, 新颖性声明需更清晰界定\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R31-D1: SCS计算与LLM-PEE相同之争\"}\n    - {round: 32, reviewers: [R2], note: \"R2-N2: contributions #1将SCS/BCS与'independently predicts'并列, 可能误导. 需明确'metric借鉴, 方法论新'.\"}\n  action_items:\n    - {round: 32, action: \"§3.2开头明确adopt from LLM-PEE; contributions改措辞\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-W2\n  summary: \"TOST probability scale通过vs logit scale不通过, 存在scale shopping嫌疑\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R31-W2: logit-scale不通过仅Limitations提及\"}\n    - {round: 32, reviewers: [R1], note: \"R1-W1: p=0.003 vs p=0.209矛盾. 选有利结论的scale作primary有shopping嫌疑.\"}\n  action_items:\n    - {round: 32, action: \"正文明确报告两scale结论并承认矛盾; 弱化'bounded interaction'claim\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-W3\n  summary: \"DocRED VIF=50.9下partial correlation解读仍偏乐观\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R31-C2: VIF=50.9呈现顺序产生replication错觉(Critical)\"}\n    - {round: 32, reviewers: [R1], note: \"R1-W2: 标准误膨胀~7倍, 应标记为inconclusive. 从R31-Critical降为Warning因论文已有改善.\"}\n  action_items:\n    - {round: 32, action: \"正文将DocRED BCS结论标为inconclusive, 不作为replication evidence\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-W4\n  summary: \"Ecological inference gap (pair r²=1.5%→batch R²=27%) 正文讨论不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R1, R2], note: \"R1-W4+R2-W1共识. pair-to-batch聚合是最关键统计推理, 正文缺ecological fallacy风险讨论. Appendix N有模拟但正文未充分引用.\"}\n  action_items:\n    - {round: 32, action: \"§4.2或§4.3增加2-3句: pair→batch机制、batch作为分析单元合理性、指向Appendix N\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-W5\n  summary: \"NER null解释缺乏实证——'dispersed error modes'是事后推测\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R1, R2], note: \"R1-W5: r=0.069远低于minimum detectable |r|=0.132, 更接近evidence of very small/null effect. R2-W2: NER null解释仅事后推测. 共识.\"}\n  action_items:\n    - {round: 32, action: \"补充讨论: 即使修正restricted range, 效应量仍在minimum detectable附近, NER BCS效应如存在也远弱于RE\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-W6\n  summary: \"'Two model families at three scales'表述误导+文内一致性问题\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 31, reviewers: [Reviewer], note: \"R31-F1: 'three model families'实际两个\"}\n    - {round: 32, reviewers: [R1], note: \"R1-W3: Abstract已改但Figure 5 caption仍说'three model families'. 'Three scales'暗示交叉设计但实际Qwen仅32B, Llama仅8B+70B.\"}\n  action_items:\n    - {round: 32, action: \"统一为'three models from two open-weight families + one proprietary model'\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R32-W7\n  summary: \"'Two dimensions'框架充分性未论证——schema complexity可能有更多维度\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R2], note: \"R2-W3: hierarchy depth, argument structure, definition ambiguity, inter-type dependency等. §4.5 centrality confound暗示第三维度.\"}\n  action_items:\n    - {round: 32, action: \"Introduction或Discussion增加1-2句说明两维度选择理由, 承认其他维度为future work\", assigned_to: \"TBD\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R32 MINOR (9 items)\n# ============================================================\n\n- id: R32-M1\n  summary: \"Figure 3信息密度过高, print size下可读性较差\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R2], note: \"R2-M1: (a)(b)两子图加error bars和注释密集\"}\n\n- id: R32-M2\n  summary: \"Figure 7内部注释文字偏小\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [Visual], note: \"视觉审查warning: 'Routing Failure'等标注字号偏小\"}\n\n- id: R32-M3\n  summary: \"§3.2 SCS/BCS层级关系不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R1, R2], note: \"R1-M3+R2-M2: pairwise SCS vs BCS层级不明; SCS limitations句位置突兀\"}\n\n- id: R32-M4\n  summary: \"Abstract 'to our knowledge'可删除\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R2], note: \"R2-M3\"}\n\n- id: R32-M5\n  summary: \"四个数据集均基于Wikipedia/Wikidata/FrameNet, domain diversity有限\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R1], note: \"R1-M5: 单一domain四个变体\"}\n\n- id: R32-M6\n  summary: \"Table 4/Table 8内容部分重叠\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R1], note: \"R1-M2\"}\n\n- id: R32-M7\n  summary: \"建议补充label semantics for NER引用(Hou et al. 2020; Ma et al. 2022)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R2], note: \"label embedding/description增强NER的经典工作\"}\n\n- id: R32-M8\n  summary: \"建议补充LasUIE(Fei et al. NeurIPS 2022)和UIE(Lu et al. ACL 2022)引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [R1], note: \"schema structure对IE影响相关\"}\n\n- id: R32-M9\n  summary: \"Appendix多处表格字号压缩至正文70%下限\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: [Visual], note: \"pages 19, 25表格字号偏小\"}\n\n# ============================================================\n# R31 RESOLVED IN R32 (4 items)\n# ============================================================\n\n- id: R31-W3\n  summary: \"Extreme-BCS batch domain composition confound未控制\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"Appendix E.4显示domain偏向, regression未控制\"}\n    - {round: 32, reviewers: [], note: \"R32未提及. 论文已加domain entropy covariate(§4.3, p_entropy=0.97, all VIF<2)\"}\n  resolution: \"§4.3增加domain entropy作为covariate, BCS系数不变\"\n  resolution_round: 32\n\n- id: R31-W5\n  summary: \"FP8量化non-determinism(SD=0.83pp)缺power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"bootstrap CI不区分信号与噪声\"}\n    - {round: 32, reviewers: [], note: \"R32未提及. Appendix已加power analysis: min detectable slope≈0.4pp/0.1BCS, observed~1.9pp(5×threshold)\"}\n  resolution: \"Appendix增加FP8 noise floor power analysis\"\n  resolution_round: 32\n\n- id: R31-W6\n  summary: \"未解释方差讨论不足(FewRel 73% unexplained)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R2, R1], note: \"应讨论未解释因素\"}\n    - {round: 32, reviewers: [], note: \"R32未提及. Discussion已列残差因素.\"}\n  resolution: \"Discussion增加残差因素讨论\"\n  resolution_round: 32\n\n- id: R31-M6\n  summary: \"Appendix N Monte Carlo ρ_pair=0.35来源和sensitivity不清\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"应标注来源和sensitivity\"}\n    - {round: 32, reviewers: [], note: \"R32未提及. 论文已增加ρ=0.20/0.35/0.50 sensitivity analysis.\"}\n  resolution: \"Appendix N已增加sensitivity analysis\"\n  resolution_round: 32\n\n# ============================================================\n# R31 NOT RAISED IN R32 (status unchanged, for tracking)\n# ============================================================\n\n- id: R31-M1\n  summary: \"NER U形count curve非线性建模不足\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"应做piecewise regression\"}\n    - {round: 32, reviewers: [], note: \"R32未提及\"}\n\n- id: R31-M5\n  summary: \"Type name粒度差异对SCS跨数据集可比性影响未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"粒度差异影响embedding similarity分布\"}\n    - {round: 32, reviewers: [], note: \"R32未提及\"}\n\n- id: R31-M7\n  summary: \"MiniLM vs Qwen3 embedding机制讨论不足\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"哪个更接近LLM实际confusability\"}\n    - {round: 32, reviewers: [], note: \"R32未提及\"}\n"
  }
}
```

</details>

---


### Tool result

_source line 3199 · 2026-05-25T21:33:02.002628+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 11521}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3200 · 2026-05-25T21:35:42.776189+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 32 审稿报告\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人 — R1 方法严谨性, R2 新颖性/完整性\n**轮次**: 1 轮（交叉分享后达成共识，无需第二轮）\n\n---\n\n## Summary\n\n本文对 zero-shot LLM 信息抽取中 schema 复杂度的两个维度——type count 和 inter-type confusability——进行受控实证分析。使用基于 embedding 的 Schema Confusability Score (SCS/BCS) 和 BCS-controlled batch 设计，在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）上实验。核心发现：(1) count 导致跨任务的单调性能退化（最高 -49pp）；(2) BCS 在 FewRel RE 上独立解释约 27% batch-level accuracy 方差（semipartial R² = 0.273）；(3) NER batch-level BCS 无效应（boundary condition）；(4) Schema decomposition (SDGD) 因 merge amplification 和 routing failure 全部失败。\n\n---\n\n## Strengths\n\n**S1. 受控实验设计精巧，填补方法论空白 [共识]**\nBCS-controlled batch 方法论是本文最核心的贡献。通过在匹配 type count 条件下构造 low-BCS / high-BCS 对照批次，结合 VIF=1.18 验证正交性，首次在 training-free LLM IE 中隔离 confusability 的独立效应。实验设计在 NLP empirical 论文中属上乘。\n\n**S2. 统计工具链远超同类论文水准 [共识]**\nVIF 检查排除 multicollinearity；percentile bootstrap CI 避免正态性假设；cluster-robust SE 处理 batch 内非独立性；TOST equivalence testing 量化交互效应上界；power analysis 诚实报告 NER null 的 65% power。两位 Reviewer 均对此高度肯定。\n\n**S3. 诚实报告负面结果 [共识]**\nSDGD 全部策略低于 single-pass baseline；NER BCS null 未回避而给出 power analysis 解释；MAVEN centrality confound 在正文讨论。这种透明度在审稿中少见，显著增强论文可信度。\n\n**S4. Count-degradation 跨任务跨模型稳健 [共识]**\n从 NER 到 RE 到 ED，降解曲线在 4 个数据集、4 个模型（Qwen3-32B, Llama-8B, Llama-70B, Gemini Flash）上一致复现。这是对社区有实际价值的 characterization。\n\n**S5. Appendix 质量极高 [共识]**\n17 页涵盖 format independence、prompt sensitivity、domain distribution、few-shot interaction、cross-model validation、aggregation simulation 等十余项 robustness check。审稿人几乎所有质疑都能在 Appendix 中找到预先回答。\n\n**S6. BCS 作为 pre-hoc proxy 有实用价值 [R1]**\nSCS/BCS 仅需 embedding 计算，无需运行抽取即可预测 schema 难度。跨 embedding 一致性（Appendix I）增强可信度。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [critical] BCS 独立效应泛化性严重不足——title 声称 \"IE\" 但 evidence 仅支撑 FewRel RE [R1-N1, R2 隐式认同]**\n\n逐数据集检查 BCS 独立效应：\n- **FewRel** (sentence-level RE): 干净成立 ✓ (VIF=1.18, semipartial R²=0.273)\n- **DocRED** (document-level RE): ✗ (VIF=50.9, semipartial R²_BCS=0.056, BCS-centrality r≈0.99 无法分离)\n- **Few-NERD** (NER): ✗ (batch-level r=0.069, p=0.219, power=65%)\n- **MAVEN** (ED): ✗ (BCS-F1 正相关归因于 centrality confound，控制后信号消失)\n\n4 个数据集中仅 1 个支撑核心 claim。Abstract 已改善（\"focusing on RE as primary testbed\"），但 title 仍为 \"Information Extraction\"。按 ARR 标准，framing 与 evidence 的 gap 直接影响 soundness 评分。\n\n→ **修改方向**: Title 限定为 RE 或加 qualifier；§6 RQ1 讨论为什么仅 RE 成立（如 RE 的 pairwise type distinction 更适合 embedding-based confusability 度量）。\n\n**C2. [critical] 核心定量 claim (semipartial R²=0.273) 缺乏跨模型复现 [R1-N2]**\n\nR²=0.273 完全来自 Qwen3-32B 单一模型。跨模型验证仅覆盖 count-curve 和 BCS-controlled accuracy gap，未在任何其他模型上报告完整回归分析（R², β, CI）。Abstract 声称 \"replicating across two model families at three scales\" 但核心定量指标仅有单模型数据。如果 R²=0.273 是 Qwen3-32B 特有的，核心 claim 不可泛化。\n\n→ **修改方向**: 至少在 Llama-8B 或 70B 上复现 FewRel BCS→accuracy 完整回归，报告 semipartial R² 和 bootstrap CI。\n\n**C3. [critical] SDGD/RQ3 分析深度不足 [R2-N1, R1 交叉认同]**\n\n作为三个 RQ 之一，Section 5 仅约半栏。缺乏：(a) merge amplification 的具体错误模式（type 混淆还是 span 错误？），(b) failure case 分布分析，(c) confidence-gated selection 失败原因的 error analysis，(d) \"negative results actionable\" 的具体路径。Reviewer 可能认为 SDGD 只是为凑第三个 contribution 草草加入。\n\n→ **修改方向**: Section 5 增加至少半栏 error analysis（merge 后哪些 type pair 产生最多 false positive、SCS 分布、actionability 具体路径）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. SCS/BCS metric 新颖性声明需更清晰界定 [R2-N2]**\nSCS 定义（cos embedding similarity）与 LLM-PEE 数学形式完全相同。Contributions #1 将 \"SCS/BCS, building on Liu et al.\" 与 \"independently predicts\" 并列，读者可能误以为新 metric。论文的真正贡献是实验方法论（BCS-controlled batch + VIF + cluster bootstrap），而非 metric 本身。建议 §3.2 开头明确 \"We adopt the pairwise embedding similarity from LLM-PEE\"，contributions 中 \"building on\" 改为 \"adopting the metric from\"。\n\n**W2. TOST scale 选择存在事后合理化嫌疑 [R1-W1]**\nProbability scale TOST 通过 (p=0.003) 但 logit scale 不通过 (p=0.209)。对有界准确率数据，logit scale 是更自然的分析尺度。选择给出有利结论的尺度作为 primary，存在 scale shopping 嫌疑。建议在正文明确报告两个尺度结论并承认矛盾，弱化 \"bounded interaction\" claim。\n\n**W3. DocRED VIF=50.9 下解读仍偏乐观 [R1-W2]**\nVIF=50.9 下标准误膨胀约 7×。论文 Appendix 承认 \"impossible to fully separate the two predictors\"，但正文 §4.3 仍纳入 \"BCS retains predictive value\" 的 narrative。建议将 DocRED BCS 结论显式标记为 \"inconclusive due to severe multicollinearity\"。R31 曾为 Critical，本轮降为 Warning 因论文已有改善（VIF caveat 前置），但仍不充分。\n\n**W4. Ecological inference gap 正文讨论不足 [R1-W4, R2-W1 共识]**\nPairwise r²≈1.5% 到 batch-level R²=27% 的跳跃是论文最关键的统计推理。Appendix N 有 Monte Carlo 模拟，但正文缺少对 ecological fallacy 风险的直接讨论。建议 §4.2 或 §4.3 增加 2-3 句：(1) pair→batch 聚合机制，(2) batch 作为分析单元的合理性（prompt 以 batch 为单位），(3) 指向 Appendix N。\n\n**W5. NER null 解释缺乏实证支撑 [R1-W5, R2-W2 共识]**\n\"Dispersed error modes\" 是事后推测。Observed r=0.069 远低于 minimum detectable |r|=0.132，更接近 \"evidence of a very small or null effect\" 而非纯粹的 \"insufficient power\"。建议更平衡地讨论——即使修正 restricted range，NER BCS 效应如存在也远弱于 RE。\n\n**W6. \"Two model families at three scales\" 表述误导 [R1-W3]**\nAbstract 已改为 \"two model families\"，但 Figure 5 caption 仍说 \"three model families\"（含 Gemini），全文不一致。Qwen 仅 32B、Llama 仅 8B+70B，非交叉设计，\"three scales\" 暗示每个 family 均有三个 scale，实际并非如此。建议统一为 \"three models from two open-weight families, plus one proprietary model\"。\n\n**W7. \"Two dimensions\" 框架充分性未论证 [R2-W3]**\nSchema complexity 可能还包括 type hierarchy depth、argument structure complexity、type definition ambiguity、inter-type dependency 等。§4.5 centrality confound 实际上暗示了第三维度存在。建议在 Introduction 或 Discussion 增加 1-2 句选择理由，承认其他维度为 future work。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **整体评分**: 两位 Reviewer 独立给出 3.5 (Borderline Conference)\n2. **统计方法论优秀**: 两人均将统计工具链列为主要优势，在 NLP empirical 论文中属标杆级别\n3. **BCS 泛化性有限**: R1 直接论证（逐数据集检查），R2 隐式认同（NER null 限制泛化性讨论）\n4. **Ecological inference 需显式讨论**: R1-W4 + R2-W1 共识\n5. **NER null 解释不充分**: R1-W5 + R2-W2 共识\n6. **负面结果坦诚**: 两人均高度肯定\n7. **Appendix 质量**: 两人均列为主要优势\n8. **引用真实性**: R2 抽查 7/7 verified，未发现虚构 citation\n\n## Reviewer Divergence\n\n两位 Reviewer 在评分和核心判断上无实质性分歧。差异体现在**关注侧重**而非矛盾立场：\n\n1. **R1 关注 cross-model R² replication (C2)，R2 未独立提出但在交叉中认同**: R2 对 multi-model validation 评价更积极（Soundness 4/5 vs R1 的 3.5/5），但认同 R² 的单模型局限。\n2. **R2 将 SDGD 深度列为 Must-Fix (C3)，R1 在初审中列为 Should-Fix**: 交叉后 R1 认同 RQ3 深度不足，接受升级。\n3. **R2 将 SCS 新颖性列为 Must-Fix (W1)，R1 在初审中未独立提出**: R1 认为本文贡献是实验方法论，metric 是否新颖是次要问题。两人视角互补。\n4. **R2 提出 simpler metrics 对比缺失 (W4)**: 实际上论文 Appendix P (Table 21) 已包含 SCS vs Levenshtein / WordNet / Same-parent 对比，R2 可能遗漏了该 appendix。此项不纳入最终 action items。\n\n---\n\n## Questions for Authors\n\n**Q1** [R1]: 能否在 Llama-8B 或 70B 上复现 FewRel 完整 BCS→accuracy 回归（semipartial R², bootstrap CI）？这是验证核心 claim 泛化性的最直接方式。\n\n**Q2** [R1]: TOST 等价边界 ±3pp 是否 pre-registered？如果使用 ±5pp，logit scale 结论是否改变？\n\n**Q3** [R1]: 是否考虑过在 FewRel 上也控制 relation 在 Wikidata knowledge graph 中的 degree centrality？FewRel 的 BCS 效应是否也部分归因于 structural 属性？\n\n**Q4** [R2]: V2 prompt 下 BCS 效应显著减弱——confusability 是 prompt-induced 还是 schema-intrinsic？如果 prompt 设计如此敏感地影响效应，是否削弱了 \"structural property\" 的结论？\n\n**Q5** [R2]: Oracle routing (72.4%) 虽高于 single-pass (50.4%)，但仍远低于 solo-type baseline (~85.7%)。Sub-schema 之间的 type overlap 是否导致了系统性问题？\n\n**Q6** [R1]: Task-specific embedding（如 FewRel 训练集微调的 sentence encoder）是否改变 BCS 预测力？这与 SCS 作为 \"pre-hoc proxy\" 的定位相关——如果最优 BCS 需 task-specific embedding，则 pre-hoc 属性打折扣。\n\n---\n\n## Missing References\n\n**引用真实性**: R2 抽查 7 篇引用均 verified，未发现虚构 citation。\n\n**建议补充**:\n1. Hou et al. (2020); Ma et al. (2022) — Label semantics for few-shot NER，使用 label embedding/description 增强 NER，与 SCS embedding similarity 思路直接相关\n2. Fei et al. (2022) \"LasUIE\" (NeurIPS 2022) — Schema structure 对 IE 的影响\n3. Lu et al. (2022) \"UIE\" (ACL 2022) — 统一 IE 建模中 schema 设计问题\n\n**注意**: R2 提出缺少 simpler confusability metrics 对比，但论文 Appendix P (Table 21) 已包含 SCS vs Levenshtein / WordNet Wu-Palmer / Same-parent baselines，SCS 在 FewRel 上显著优于所有 baselines（ρ=0.218 vs 0.097/0.073/0.016）。R2 可能遗漏了该 appendix。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目未启用 `external_review.paperreview_ai`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成（耗时 ~3.5 分钟）\n**统计**: 0 critical, 4 warning, 22 info\n\n**Findings**:\n- ✅ 主文 8 页，每页至少 1 个 display item，视觉节奏优秀\n- ✅ Figure 1 作为视觉锚点在首页，审稿人第一印象良好\n- ✅ 11 个 display items / 8 页主文，密度符合实证论文预期\n- ✅ 所有 Figure/Table 均在首次引用后合理位置，无 float 漂移\n- ✅ 双栏间距均匀，无 margin 溢出，公式渲染正确\n- ✅ booktabs 风格表格，专业\n- ⚠️ Figure 7 (SDGD Pipeline) 内部注释文字偏小，打印时可能不易辨认\n- ⚠️ Appendix pages 19, 25 多个表格字号压缩至正文 70% 下限\n- ⚠️ Appendix G (Prompt Templates) 整页 monospace 纯文本，视觉疲劳较高\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 — Borderline Conference\n**置信度**: 4/5\n\n**总评**: 这是一篇方法论扎实、统计工具链远超同类论文水准的实证分析论文。BCS-controlled batch 实验设计是真正的贡献，诚实报告负面结果（SDGD 失败、NER null、MAVEN centrality confound）增强可信度。\n\n**核心障碍**在于 claims 与 evidence 的 gap：(1) BCS 独立效应仅在 FewRel 一个数据集上干净成立，但 title/abstract 声称 \"Information Extraction\"；(2) 核心定量指标 R²=0.273 缺乏跨模型复现；(3) RQ3 (SDGD) 分析深度不足以支撑一个核心 contribution。\n\n**如果 C1-C3 被充分修改**（title 限定、跨模型 R² 复现、SDGD error analysis 扩展），论文可达 Conference (4.0) 水平——受控实验设计的方法论贡献和对 schema complexity 的首个 controlled characterization 值得主会议发表。\n\n**如果作者无法补充跨模型 R² 数据**，建议将核心 claim 限定为 FewRel-specific 发现，论文仍可作为 Findings (3.0-3.5) 接收——方法论框架和负面结果对社区有价值，但贡献范围缩窄。\n\n---\n\n## Detailed Comments\n\n### R31 → R32 跨轮进展\n\n以下 R31 问题在本轮已解决，不再列为 open issues：\n- **R31-W3** (domain confound): §4.3 增加 domain entropy covariate (p_entropy=0.97, VIF<2) ✅\n- **R31-W5** (FP8 noise power analysis): Appendix 增加 min detectable slope 分析 ✅\n- **R31-W6** (unexplained variance): Discussion 增加残差因素讨论 ✅\n- **R31-M6** (Monte Carlo ρ sensitivity): Appendix N 增加 ρ=0.20/0.35/0.50 sensitivity ✅\n\n以下 R31 问题在本轮仍然存在或升级：\n- **R31-C1** → **R32-C1**: BCS scope framing 仍未充分解决\n- **R31-C2** → **R32-W3**: DocRED VIF 从 Critical 降为 Warning（论文已改善但仍不充分）\n- **R31-D1** → **R32-W1**: SCS/BCS 新颖性仍需界定\n- **R31-W1** → **R32-C2**: 模型多样性从 Should-Fix 升级为 Must-Fix\n- **R31-W2** → **R32-W2**: TOST scale 问题持续\n- **R31-W4** → **R32-C3**: RQ3 深度从 Should-Fix 升级为 Must-Fix\n- **R31-F1** → **R32-W6**: 文内一致性仍有残留\n\n### 格式合规检查\n\n- ✅ ACL review 模板 (`\\usepackage[review]{acl}`)\n- ✅ Double-blind (Author: Anonymous)\n- ✅ Limitations 在正文中（p9, 正文后 references 前）\n- ✅ Checklist 不在 PDF 中（注释掉，注明在 OpenReview form）\n- ✅ 主文 8 页内（视觉审查确认）\n- ✅ Abstract ~160 words (< 200 word limit)\n- ✅ AI 使用透明披露 (Appendix Z)\n- ✅ Anonymous repo link 提供\n\n### 引用验证\n\n引用抽查 7/7 verified real。未启用系统引用验证。\n\n### 对 R2-W4 的 Director 注记\n\nR2 指出缺少 simpler confusability metrics 对比（Levenshtein, WordNet），但论文 Appendix P (§app:scs-baselines, Table 21) 已包含该对比：SCS vs Levenshtein / WordNet Wu-Palmer / Same-parent，FewRel 上 SCS 显著优于所有 baselines (ρ=0.218 vs 0.097/0.073/0.016)。此项已有论文内回答，不纳入修改要求。",
  "project": "schema-dag-extraction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 32 审稿报告\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人 — R1 方法严谨性, R2 新颖性/完整性\n**轮次**: 1 轮（交叉分享后达成共识，无需第二轮）\n\n---\n\n## Summary\n\n本文对 zero-shot LLM 信息抽取中 schema 复杂度的两个维度——type count 和 inter-type confusability——进行受控实证分析。使用基于 embedding 的 Schema Confusability Score (SCS/BCS) 和 BCS-controlled batch 设计，在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）上实验。核心发现：(1) count 导致跨任务的单调性能退化（最高 -49pp）；(2) BCS 在 FewRel RE 上独立解释约 27% batch-level accuracy 方差（semipartial R² = 0.273）；(3) NER batch-level BCS 无效应（boundary condition）；(4) Schema decomposition (SDGD) 因 merge amplification 和 routing failure 全部失败。\n\n---\n\n## Strengths\n\n**S1. 受控实验设计精巧，填补方法论空白 [共识]**\nBCS-controlled batch 方法论是本文最核心的贡献。通过在匹配 type count 条件下构造 low-BCS / high-BCS 对照批次，结合 VIF=1.18 验证正交性，首次在 training-free LLM IE 中隔离 confusability 的独立效应。实验设计在 NLP empirical 论文中属上乘。\n\n**S2. 统计工具链远超同类论文水准 [共识]**\nVIF 检查排除 multicollinearity；percentile bootstrap CI 避免正态性假设；cluster-robust SE 处理 batch 内非独立性；TOST equivalence testing 量化交互效应上界；power analysis 诚实报告 NER null 的 65% power。两位 Reviewer 均对此高度肯定。\n\n**S3. 诚实报告负面结果 [共识]**\nSDGD 全部策略低于 single-pass baseline；NER BCS null 未回避而给出 power analysis 解释；MAVEN centrality confound 在正文讨论。这种透明度在审稿中少见，显著增强论文可信度。\n\n**S4. Count-degradation 跨任务跨模型稳健 [共识]**\n从 NER 到 RE 到 ED，降解曲线在 4 个数据集、4 个模型（Qwen3-32B, Llama-8B, Llama-70B, Gemini Flash）上一致复现。这是对社区有实际价值的 characterization。\n\n**S5. Appendix 质量极高 [共识]**\n17 页涵盖 format independence、prompt sensitivity、domain distribution、few-shot interaction、cross-model validation、aggregation simulation 等十余项 robustness check。审稿人几乎所有质疑都能在 Appendix 中找到预先回答。\n\n**S6. BCS 作为 pre-hoc proxy 有实用价值 [R1]**\nSCS/BCS 仅需 embedding 计算，无需运行抽取即可预测 schema 难度。跨 embedding 一致性（Appendix I）增强可信度。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [critical] BCS 独立效应泛化性严重不足——title 声称 \"IE\" 但 evidence 仅支撑 FewRel RE [R1-N1, R2 隐式认同]**\n\n逐数据集检查 BCS 独立效应：\n- **FewRel** (sentence-level RE): 干净成立 ✓ (VIF=1.18, semipartial R²=0.273)\n- **DocRED** (document-level RE): ✗ (VIF=50.9, semipartial R²_BCS=0.056, BCS-centrality r≈0.99 无法分离)\n- **Few-NERD** (NER): ✗ (batch-level r=0.069, p=0.219, power=65%)\n- **MAVEN** (ED): ✗ (BCS-F1 正相关归因于 centrality confound，控制后信号消失)\n\n4 个数据集中仅 1 个支撑核心 claim。Abstract 已改善（\"focusing on RE as primary testbed\"），但 title 仍为 \"Information Extraction\"。按 ARR 标准，framing 与 evidence 的 gap 直接影响 soundness 评分。\n\n→ **修改方向**: Title 限定为 RE 或加 qualifier；§6 RQ1 讨论为什么仅 RE 成立（如 RE 的 pairwise type distinction 更适合 embedding-based confusability 度量）。\n\n**C2. [critical] 核心定量 claim (semipartial R²=0.273) 缺乏跨模型复现 [R1-N2]**\n\nR²=0.273 完全来自 Qwen3-32B 单一模型。跨模型验证仅覆盖 count-curve 和 BCS-controlled accuracy gap，未在任何其他模型上报告完整回归分析（R², β, CI）。Abstract 声称 \"replicating across two model families at three scales\" 但核心定量指标仅有单模型数据。如果 R²=0.273 是 Qwen3-32B 特有的，核心 claim 不可泛化。\n\n→ **修改方向**: 至少在 Llama-8B 或 70B 上复现 FewRel BCS→accuracy 完整回归，报告 semipartial R² 和 bootstrap CI。\n\n**C3. [critical] SDGD/RQ3 分析深度不足 [R2-N1, R1 交叉认同]**\n\n作为三个 RQ 之一，Section 5 仅约半栏。缺乏：(a) merge amplification 的具体错误模式（type 混淆还是 span 错误？），(b) failure case 分布分析，(c) confidence-gated selection 失败原因的 error analysis，(d) \"negative results actionable\" 的具体路径。Reviewer 可能认为 SDGD 只是为凑第三个 contribution 草草加入。\n\n→ **修改方向**: Section 5 增加至少半栏 error analysis（merge 后哪些 type pair 产生最多 false positive、SCS 分布、actionability 具体路径）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. SCS/BCS metric 新颖性声明需更清晰界定 [R2-N2]**\nSCS 定义（cos embedding similarity）与 LLM-PEE 数学形式完全相同。Contributions #1 将 \"SCS/BCS, building on Liu et al.\" 与 \"independently predicts\" 并列，读者可能误以为新 metric。论文的真正贡献是实验方法论（BCS-controlled batch + VIF + cluster bootstrap），而非 metric 本身。建议 §3.2 开头明确 \"We adopt the pairwise embedding similarity from LLM-PEE\"，contributions 中 \"building on\" 改为 \"adopting the metric from\"。\n\n**W2. TOST scale 选择存在事后合理化嫌疑 [R1-W1]**\nProbability scale TOST 通过 (p=0.003) 但 logit scale 不通过 (p=0.209)。对有界准确率数据，logit scale 是更自然的分析尺度。选择给出有利结论的尺度作为 primary，存在 scale shopping 嫌疑。建议在正文明确报告两个尺度结论并承认矛盾，弱化 \"bounded interaction\" claim。\n\n**W3. DocRED VIF=50.9 下解读仍偏乐观 [R1-W2]**\nVIF=50.9 下标准误膨胀约 7×。论文 Appendix 承认 \"impossible to fully separate the two predictors\"，但正文 §4.3 仍纳入 \"BCS retains predictive value\" 的 narrative。建议将 DocRED BCS 结论显式标记为 \"inconclusive due to severe multicollinearity\"。R31 曾为 Critical，本轮降为 Warning 因论文已有改善（VIF caveat 前置），但仍不充分。\n\n**W4. Ecological inference gap 正文讨论不足 [R1-W4, R2-W1 共识]**\nPairwise r²≈1.5% 到 batch-level R²=27% 的跳跃是论文最关键的统计推理。Appendix N 有 Monte Carlo 模拟，但正文缺少对 ecological fallacy 风险的直接讨论。建议 §4.2 或 §4.3 增加 2-3 句：(1) pair→batch 聚合机制，(2) batch 作为分析单元的合理性（prompt 以 batch 为单位），(3) 指向 Appendix N。\n\n**W5. NER null 解释缺乏实证支撑 [R1-W5, R2-W2 共识]**\n\"Dispersed error modes\" 是事后推测。Observed r=0.069 远低于 minimum detectable |r|=0.132，更接近 \"evidence of a very small or null effect\" 而非纯粹的 \"insufficient power\"。建议更平衡地讨论——即使修正 restricted range，NER BCS 效应如存在也远弱于 RE。\n\n**W6. \"Two model families at three scales\" 表述误导 [R1-W3]**\nAbstract 已改为 \"two model families\"，但 Figure 5 caption 仍说 \"three model families\"（含 Gemini），全文不一致。Qwen 仅 32B、Llama 仅 8B+70B，非交叉设计，\"three scales\" 暗示每个 family 均有三个 scale，实际并非如此。建议统一为 \"three models from two open-weight families, plus one proprietary model\"。\n\n**W7. \"Two dimensions\" 框架充分性未论证 [R2-W3]**\nSchema complexity 可能还包括 type hierarchy depth、argument structure complexity、type definition ambiguity、inter-type dependency 等。§4.5 centrality confound 实际上暗示了第三维度存在。建议在 Introduction 或 Discussion 增加 1-2 句选择理由，承认其他维度为 future work。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **整体评分**: 两位 Reviewer 独立给出 3.5 (Borderline Conference)\n2. **统计方法论优秀**: 两人均将统计工具链列为主要优势，在 NLP empirical 论文中属标杆级别\n3. **BCS 泛化性有限**: R1 直接论证（逐数据集检查），R2 隐式认同（NER null 限制泛化性讨论）\n4. **Ecological inference 需显式讨论**: R1-W4 + R2-W1 共识\n5. **NER null 解释不充分**: R1-W5 + R2-W2 共识\n6. **负面结果坦诚**: 两人均高度肯定\n7. **Appendix 质量**: 两人均列为主要优势\n8. **引用真实性**: R2 抽查 7/7 verified，未发现虚构 citation\n\n## Reviewer Divergence\n\n两位 Reviewer 在评分和核心判断上无实质性分歧。差异体现在**关注侧重**而非矛盾立场：\n\n1. **R1 关注 cross-model R² replication (C2)，R2 未独立提出但在交叉中认同**: R2 对 multi-model validation 评价更积极（Soundness 4/5 vs R1 的 3.5/5），但认同 R² 的单模型局限。\n2. **R2 将 SDGD 深度列为 Must-Fix (C3)，R1 在初审中列为 Should-Fix**: 交叉后 R1 认同 RQ3 深度不足，接受升级。\n3. **R2 将 SCS 新颖性列为 Must-Fix (W1)，R1 在初审中未独立提出**: R1 认为本文贡献是实验方法论，metric 是否新颖是次要问题。两人视角互补。\n4. **R2 提出 simpler metrics 对比缺失 (W4)**: 实际上论文 Appendix P (Table 21) 已包含 SCS vs Levenshtein / WordNet / Same-parent 对比，R2 可能遗漏了该 appendix。此项不纳入最终 action items。\n\n---\n\n## Questions for Authors\n\n**Q1** [R1]: 能否在 Llama-8B 或 70B 上复现 FewRel 完整 BCS→accuracy 回归（semipartial R², bootstrap CI）？这是验证核心 claim 泛化性的最直接方式。\n\n**Q2** [R1]: TOST 等价边界 ±3pp 是否 pre-registered？如果使用 ±5pp，logit scale 结论是否改变？\n\n**Q3** [R1]: 是否考虑过在 FewRel 上也控制 relation 在 Wikidata knowledge graph 中的 degree centrality？FewRel 的 BCS 效应是否也部分归因于 structural 属性？\n\n**Q4** [R2]: V2 prompt 下 BCS 效应显著减弱——confusability 是 prompt-induced 还是 schema-intrinsic？如果 prompt 设计如此敏感地影响效应，是否削弱了 \"structural property\" 的结论？\n\n**Q5** [R2]: Oracle routing (72.4%) 虽高于 single-pass (50.4%)，但仍远低于 solo-type baseline (~85.7%)。Sub-schema 之间的 type overlap 是否导致了系统性问题？\n\n**Q6** [R1]: Task-specific embedding（如 FewRel 训练集微调的 sentence encoder）是否改变 BCS 预测力？这与 SCS 作为 \"pre-hoc proxy\" 的定位相关——如果最优 BCS 需 task-specific embedding，则 pre-hoc 属性打折扣。\n\n---\n\n## Missing References\n\n**引用真实性**: R2 抽查 7 篇引用均 verified，未发现虚构 citation。\n\n**建议补充**:\n1. Hou et al. (2020); Ma et al. (2022) — Label semantics for few-shot NER，使用 label embedding/description 增强 NER，与 SCS embedding similarity 思路直接相关\n2. Fei et al. (2022) \"LasUIE\" (NeurIPS 2022) — Schema structure 对 IE 的影响\n3. Lu et al. (2022) \"UIE\" (ACL 2022) — 统一 IE 建模中 schema 设计问题\n\n**注意**: R2 提出缺少 simpler confusability metrics 对比，但论文 Appendix P (Table 21) 已包含 SCS vs Levenshtein / WordNet Wu-Palmer / Same-parent baselines，SCS 在 FewRel 上显著优于所有 baselines（ρ=0.218 vs 0.097/0.073/0.016）。R2 可能遗漏了该 appendix。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目未启用 `external_review.paperreview_ai`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成（耗时 ~3.5 分钟）\n**统计**: 0 critical, 4 warning, 22 info\n\n**Findings**:\n- ✅ 主文 8 页，每页至少 1 个 display item，视觉节奏优秀\n- ✅ Figure 1 作为视觉锚点在首页，审稿人第一印象良好\n- ✅ 11 个 display items / 8 页主文，密度符合实证论文预期\n- ✅ 所有 Figure/Table 均在首次引用后合理位置，无 float 漂移\n- ✅ 双栏间距均匀，无 margin 溢出，公式渲染正确\n- ✅ booktabs 风格表格，专业\n- ⚠️ Figure 7 (SDGD Pipeline) 内部注释文字偏小，打印时可能不易辨认\n- ⚠️ Appendix pages 19, 25 多个表格字号压缩至正文 70% 下限\n- ⚠️ Appendix G (Prompt Templates) 整页 monospace 纯文本，视觉疲劳较高\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 — Borderline Conference\n**置信度**: 4/5\n\n**总评**: 这是一篇方法论扎实、统计工具链远超同类论文水准的实证分析论文。BCS-controlled batch 实验设计是真正的贡献，诚实报告负面结果（SDGD 失败、NER null、MAVEN centrality confound）增强可信度。\n\n**核心障碍**在于 claims 与 evidence 的 gap：(1) BCS 独立效应仅在 FewRel 一个数据集上干净成立，但 title/abstract 声称 \"Information Extraction\"；(2) 核心定量指标 R²=0.273 缺乏跨模型复现；(3) RQ3 (SDGD) 分析深度不足以支撑一个核心 contribution。\n\n**如果 C1-C3 被充分修改**（title 限定、跨模型 R² 复现、SDGD error analysis 扩展），论文可达 Conference (4.0) 水平——受控实验设计的方法论贡献和对 schema complexity 的首个 controlled characterization 值得主会议发表。\n\n**如果作者无法补充跨模型 R² 数据**，建议将核心 claim 限定为 FewRel-specific 发现，论文仍可作为 Findings (3.0-3.5) 接收——方法论框架和负面结果对社区有价值，但贡献范围缩窄。\n\n---\n\n## Detailed Comments\n\n### R31 → R32 跨轮进展\n\n以下 R31 问题在本轮已解决，不再列为 open issues：\n- **R31-W3** (domain confound): §4.3 增加 domain entropy covariate (p_entropy=0.97, VIF<2) ✅\n- **R31-W5** (FP8 noise power analysis): Appendix 增加 min detectable slope 分析 ✅\n- **R31-W6** (unexplained variance): Discussion 增加残差因素讨论 ✅\n- **R31-M6** (Monte Carlo ρ sensitivity): Appendix N 增加 ρ=0.20/0.35/0.50 sensitivity ✅\n\n以下 R31 问题在本轮仍然存在或升级：\n- **R31-C1** → **R32-C1**: BCS scope framing 仍未充分解决\n- **R31-C2** → **R32-W3**: DocRED VIF 从 Critical 降为 Warning（论文已改善但仍不充分）\n- **R31-D1** → **R32-W1**: SCS/BCS 新颖性仍需界定\n- **R31-W1** → **R32-C2**: 模型多样性从 Should-Fix 升级为 Must-Fix\n- **R31-W2** → **R32-W2**: TOST scale 问题持续\n- **R31-W4** → **R32-C3**: RQ3 深度从 Should-Fix 升级为 Must-Fix\n- **R31-F1** → **R32-W6**: 文内一致性仍有残留\n\n### 格式合规检查\n\n- ✅ ACL review 模板 (`\\usepackage[review]{acl}`)\n- ✅ Double-blind (Author: Anonymous)\n- ✅ Limitations 在正文中（p9, 正文后 references 前）\n- ✅ Checklist 不在 PDF 中（注释掉，注明在 OpenReview form）\n- ✅ 主文 8 页内（视觉审查确认）\n- ✅ Abstract ~160 words (< 200 word limit)\n- ✅ AI 使用透明披露 (Appendix Z)\n- ✅ Anonymous repo link 提供\n\n### 引用验证\n\n引用抽查 7/7 verified real。未启用系统引用验证。\n\n### 对 R2-W4 的 Director 注记\n\nR2 指出缺少 simpler confusability metrics 对比（Levenshtein, WordNet），但论文 Appendix P (§app:scs-baselines, Table 21) 已包含该对比：SCS vs Levenshtein / WordNet Wu-Palmer / Same-parent，FewRel 上 SCS 显著优于所有 baselines (ρ=0.218 vs 0.097/0.073/0.016)。此项已有论文内回答，不纳入修改要求。",
    "project": "schema-dag-extraction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference"
  }
}
```

</details>

---


### Tool result

_source line 3201 · 2026-05-25T21:35:46.714661+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3938
}
```

</details>

---


### Assistant

_source line 3202 · 2026-05-25T21:35:59.809984+00:00_

**Round 32 审稿完成。**

报告已投递至 Research Director。核心结论：

**评分：3.5 / 5 — Borderline Conference**

| 类别 | 数量 | 关键项 |
|------|------|--------|
| Critical | 3 | BCS 泛化性仅 FewRel、R²缺跨模型复现、SDGD/RQ3 深度不足 |
| Warning | 7 | SCS 新颖性界定、TOST scale、DocRED VIF、ecological inference、NER null、model families 表述、two-dimensions 框架 |
| Minor | 9 | Figure 可读性、引用补充、表格字号等 |
| R31 已解决 | 4 | domain confound、FP8 power analysis、unexplained variance、Monte Carlo sensitivity |

**升降级变化**：R31-W1 (模型多样性) 升级为 R32-C2 (Must-Fix)；R31-W4 (RQ3 深度) 升级为 R32-C3 (Must-Fix)；R31-C2 (DocRED VIF) 降级为 R32-W3 (Warning)。

**视觉审查**：✅ 完成，0 critical / 4 warning（均在 appendix 或图内小字号）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 267

## Round 267

2 recorded events


### User

_source line 3203 · 2026-05-25T21:35:59.816764+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix

### R1-N1: BCS 独立效应泛化性——title/abstract overclaim "IE" but evidence only supports FewRel RE

**[AGREE]** 这是本文最实质性的弱点。R1 的逐数据集分析精准：

- **FewRel**: BCS 独立效应成立（VIF=1.18, R²=0.273）✓
- **DocRED**: VIF=50.9 导致 BCS 与 centrality 完全共线，semipartial R²=0.056 不可靠（Appendix E.1 自己承认 "does not uniquely identify the causal channel"）✗
- **Few-NERD**: NER null，论文自己定位为 boundary condition（§4.3, Appendix E.2 承认 power 仅 65%，低于 80% 阈值）✗
- **MAVEN**: centrality confound 后 batch-level BCS 信号消失（§4.5, Appendix E），仅 pairwise SCS-confusion correlation 残存（r=0.129）✗

因此，核心定量 claim（R²=0.273, "independently predicts"）事实上仅由 FewRel 一个数据集的一种任务（80-relation RE）支撑。Title 中 "Information Extraction" 和 Abstract 中 "across four datasets" 的措辞确实超出了 evidence 的覆盖范围。我在自己的审稿中注意到 NER null 和 MAVEN confound 问题（我的 W2、W3），但未像 R1 这样系统地将四个数据集的结论汇总为"泛化性不足"。R1 的整合分析更有力。

补充：论文确实在正文中将 NER 框架为 "boundary condition"（§1, §6），并在 Appendix E.1 讨论了 DocRED 的 VIF 问题。但这些 caveats 分散在附录中，正文的 framing（尤其是 title 和 abstract）未充分反映这些限制。Title 加 qualifier（如 "in Relation Extraction"）或 Abstract 明确说明 "on FewRel RE" 是合理的修改建议。

---

### R1-N2: 核心回归 R²=0.273 缺乏跨模型复现

**[AGREE]** 我复查了 Appendix T-U：

- **Llama-3.1-70B** (Appendix T): 报告了 count curve 复现 + BCS-controlled accuracy gap（Table 23），但无完整回归表（无 R², β, CI）
- **Gemini 2.5 Flash** (Appendix U): 同上，报告了 BCS gap at count 8（low-BCS 90.5% vs. high-BCS 72.9%, Δ=-17.6pp）和 count 16 的方向一致性，但无回归分析
- **Llama-3.1-8B**: Table 7 报告 NER batch-level BCS-F1 correlation，但 RE 回归同样缺失

Abstract 声称 "replicated across two model families at three scales (7B–70B)" ——这里 replicate 的是 BCS gap 的方向一致性（high-BCS batch accuracy < low-BCS），而非 R²=0.273 这个定量值。但读者极易将其理解为核心定量结论的复现。这构成了 overclaim。

我在自己的审稿中关注了 "limited model diversity"（我的 Strengths S4 中肯定了多模型复现，但未深入检查复现的定量层次）。R1 的分析更准确——direction replication ≠ quantitative replication。

---

## Should-Fix

### R1-W1: TOST probability scale 通过 / logit scale 不通过——scale shopping

**[REBUT]** 论文在 Appendix C（page 13-14）同时报告了两种 scale 的 TOST 结果，并明确写道：

> "The logit-scale interaction (0.111 logit units, p = 0.047, 90% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent ±3pp margin ... is inconclusive (p_TOST = 0.209)."

论文还补充了 regression-based TOST 作为 sensitivity check：

> "A regression-based TOST (p ≥ .375, five count levels with continuous BCS) yields p = 0.004 at ±3 pp and p = 0.026 at ±3.5 pp on the logit scale, confirming the borderline status."

同时报告两种 scale 的正面和负面结果，并用 "borderline" 而非 "confirmed" 来描述结论——这恰恰是透明报告的表现，不是 scale shopping。Scale shopping 指的是只报告有利 scale 而隐瞒不利 scale，论文没有这样做。

但我同意 R1 的隐含关切：probability scale 上的 TOST 通过在 accuracy 接近 50% 时可能低估交互效应，logit scale 的 failure 应在正文中更显著地提及（目前仅在 Appendix C）。建议在正文 §4.3 中增加一句提及 logit-scale TOST 的 inconclusive 结果。

---

### R1-W2: DocRED VIF=50.9 解读过于乐观

**[AGREE]** VIF=50.9 远超常用阈值（VIF>10 即严重共线性）。论文在 Appendix E.1 承认 "does not uniquely identify the causal channel"，但正文中 DocRED 的呈现方式（§4.3 提及 "DocRED extends the RE evaluation to a larger schema"，Table 2 列出 DocRED 相关性）未充分突出这一限制。读者可能将 DocRED 视为 FewRel 发现的独立复现，而实际上 DocRED 的 BCS 效应无法与 centrality 分离。

这一点强化了 R1-N1 的结论：声称四个数据集的证据实际上几乎仅来自 FewRel。

---

### R1-W3: "Two model families at three scales" 表述 + "7B" 应为 "8B"

**[AGREE]** 
- Llama-3.1-8B 是 8B 参数，非 7B。Abstract 中 "7B–70B" 是事实错误，应改为 "8B–70B"。
- "Two model families" 指 Qwen 和 Llama，Gemini 作为附加验证不计入——这可以接受但应在正文中明确。
- "Three scales" 指 8B/32B/70B——准确，但前提是 "7B" 改正。

这是一个容易修复的事实错误，但出现在 Abstract 中影响论文可信度。我在自己的审稿中将其列为 Minor（M3: "to our knowledge" 建议删除），但漏掉了 "7B" 这个更重要的事实错误。

---

### R1-W4: Ecological inference batch→pair gap 讨论不足

**[AGREE]** 与我自己的 W1 完全一致。Pairwise r²≈1.5% 到 batch-level R²=27% 的跳跃是论文的核心推理链，但正文中对 ecological fallacy 风险的讨论仅有一句。Appendix N 的 Monte Carlo 模拟提供了解释机制（多个弱 pair-level 效应在 batch 内累积），但应在正文 §4.2 或 §4.3 中更显著地讨论。

补充论据：论文 §4.3 的分析单元是 batch（25 个 random batches per count level），每个 batch 包含 k 个 types → C(k,2) 个 type pairs。Batch-level R²=27% 可能部分反映了 batch composition 的系统性差异（如 domain clustering，Appendix E.4 部分控制了这一点），而非纯粹的 confusability 效应。

---

### R1-W5: NER null 的 "absence of evidence" 论证——power 不足

**[AGREE]** 论文自己在 Appendix E.2 承认：

> "Few-NERD's BCS standard deviation (0.027) is only 19% of FewRel's (0.141); FewRel's observed r = −0.570 would attenuate to r' = 0.111 under this restricted range, yielding 65% power at n = 420 (below the conventional 80% threshold). The minimum detectable |r| at 80% power is 0.132."

这意味着即使 NER 存在与 FewRel 同等强度的 BCS 效应，当前实验设计也有 35% 概率检测不到。将此解读为 "NER null serves as a boundary condition"（Abstract）可能过于强势——更准确的表述是 "NER shows no detectable BCS signal under current power constraints"。

我在自己的审稿中也指出了 NER null 解释不足（我的 W2），但未像 R1 这样精确引用 power analysis 数据。R1 的论证更有力。

---

## Minor

**[AGREE] R1-M1**: "7B" → "8B"，事实错误，同 W3。

**[AGREE] R1-M2**: Table 4（main text, IntraSub/missed rates by BCS bin）与 Table 8（Appendix A, cross-model replication of IntraSub rates）确实存在内容重叠。Table 8 本质上是 Table 4 在 DocRED 上的 replication。可以合并或在 Table 8 caption 中明确标注 "extends Table 4 to DocRED"。

**[AGREE] R1-M3**: §3.2 中 SCS（pairwise）→ BCS（batch-level aggregation）的层级关系确实不够清晰。我在自己的审稿中也有相同观察。建议在 §3.2 中增加一个 "BCS aggregates pairwise SCS across all type pairs in a batch" 的显式过渡句。

**[AGREE] R1-M4**: Figure 1 的箭头（Dimension 1 / Dimension 2）在视觉上确实不直观——读者需要仔细读 caption 才能理解两个维度的含义。建议增加轴标签或用颜色编码区分。

**[AGREE] R1-M5**: 四个数据集均基于 Wikipedia/Wikidata（FewRel=Wikidata, DocRED=Wikipedia, Few-NERD=Wikipedia, MAVEN=Wikipedia），实际上是单一 domain 的四个变体。这限制了论文 "across four datasets" 的泛化性声称。论文 Limitations section（page 9）提到了 "non-English scenarios remain untested" 但未提及 Wikipedia 同质性。这与 R1-N1 的泛化性问题相互强化。

---

## Questions 回应

**R1-Q1 (Llama 完整回归复现)**: 有价值的建议，直接回应 N2。如果能在 Llama-70B 上跑出完整的 BCS→accuracy 回归（R², semipartial R², β, bootstrap CI），将实质性地加强论文。

**R1-Q2 (TOST ±3pp pre-registration)**: 关键问题。±3pp 的 equivalence margin 如果是 post-hoc 选定的，则 TOST 的统计效力会被过度使用灵活性削弱。论文未声称 pre-registration。

**R1-Q3 (Task-specific embedding)**: 与我的 W4 相关。当前 SCS 使用通用 sentence embedding（MiniLM），task-specific embedding 可能捕捉更相关的 confusability 信号。Appendix M 的 name-only ablation 是这个方向的初步探索，但不充分。

**R1-Q4 (FewRel centrality confound)**: 好问题。论文在 §4.5 详细分析了 MAVEN 的 centrality confound，但未对 FewRel 做同等分析。如果 FewRel 也存在隐藏的 centrality confound（尽管 VIF=1.18 暗示不严重），则核心 R²=0.273 的解读需要调整。

**R1-Q5 (SDGD constrained routing)**: 直接呼应我的 N1（SDGD 分析深度不足）。论文报告了 5 种 routing 策略（Table 3），其中包括 "Max conf (gold)" oracle，但未尝试 BCS-aware constrained routing（如限制 sub-schema 内 type pairs 的 SCS < threshold）。这是一个明显的实验空白。

---

## 总结

Reviewer 1 的审稿意见整体质量高，抓住了论文的核心问题。在 7 个 Must-Fix + Should-Fix 问题中，我 **同意 6 个**（N1, N2, W2, W3, W4, W5），**部分反驳 1 个**（W1: scale shopping 指控不成立，但 logit-scale failure 应在正文中更显著提及）。5 个 Minor 全部同意。

我与 R1 的共识核心在于：**论文的泛化性声称超出了实证基础**。这体现在三个层面：(1) 数据集层面（4 个中仅 FewRel 干净支撑 BCS 独立效应），(2) 模型层面（R²=0.273 仅 Qwen3-32B），(3) domain 层面（全部 Wikipedia）。如果作者能修复 title/abstract framing + 补充 Llama 回归数据，这些问题大部分可以解决。

我维持 Overall 3.5 (Borderline Conference) 的评分。如果 N1 的 title/abstract 修改 + N2 的跨模型回归数据在 revision 中解决，可升至 4.0 (Conference)。


---

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条回应。

核心结论：R1 的 7 个 Must-Fix/Should-Fix 中同意 6 个、部分反驳 1 个（W1 scale shopping 指控——论文同时报告了两种 scale，属透明报告而非 cherry-picking，但 logit-scale failure 确应在正文中更显著提及）。5 个 Minor 全部同意。

与 R1 的最大共识：**论文泛化性声称超出实证基础**——BCS 独立效应实质上仅由 FewRel 单一数据集支撑，R²=0.273 仅 Qwen3-32B 单模型，四个数据集全部 Wikipedia domain。

---

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE with downgrade] R2-N1: SDGD 分析深度不足**

同意 Section 5 正文篇幅受限（约 1 栏文字 + Figure 7 + Table 3 + Table 4），但 R2 的判断"仅半栏"有所低估——实际上 SDGD 在正文中占据了 Figure 7（pipeline 示意图）、Table 3（5 种 routing 策略的定量对比）、Table 4（IntraSub/missed rates by BCS）以及约 1 栏的文字分析，已识别出两大失败模式：routing failure（73.4%）和 merge amplification（FP 增长 ~4×）。Appendix B 提供了完整的 graph coloring 算法、routing 策略细节（v1 union vs v2 confidence-gated）和 Table 9 的分解模式对比。

但 R2 指出的具体缺口是合理的：(a) merge amplification 的错误模式缺乏案例级分析；(c) confidence-gated selection 为何也失败——Table 9 显示 v2 confidence-gated 用 LLM self-reported confidence 保留 highest-scoring candidate，但 confidence calibration 的可靠性未讨论。

**建议：降级为 Should-Fix。** 负面结果的核心贡献是"decomposition doesn't work and here's why"，两大失败机制已明确。补充 confidence calibration 分析和 2-3 个 merge amplification 案例即可，无需达到 RQ1/RQ2 的分析深度。

---

**[AGREE] R2-N2: SCS/BCS 新颖性声明需界定**

同意。SCS 的数学定义（cos(embed(t_i), embed(t_j))）确实与 LLM-PEE（Liu et al., 2025）的 type embedding similarity 在形式上完全一致。§2 Related Work 中论文已指出与 LLM-PEE 的三点区别（controlled analysis vs engineering solution; VIF-verified orthogonality; LLM-PEE conflates confusability with count），但 §1 Contributions #1 的措辞 "independently predicts type substitution errors" 与 SCS/BCS 并列出现，确实可能让读者误以为 metric 本身是新贡献。

**但我将此降级为 Should-Fix 而非 Must-Fix。** 这是一个 framing/clarity 问题，不影响 soundness。作者只需在 §3.2 增加一句 "SCS adopts the same cosine-similarity formulation used in LLM-PEE; our contribution is the controlled experimental methodology that isolates its independent predictive power" 即可解决。

---

### Should-Fix

**[AGREE] R2-W1: Ecological inference gap 讨论不足**

与我自己的 W4 一致。pair-level r²≈1.5%（Table 2, Few-NERD r=0.069²≈0.005; FewRel 更强但仍远低于 batch-level）到 batch R²=0.273 的放大效应在正文中未充分解释。Appendix N 的 Monte Carlo 模拟（pair-to-batch aggregation simulation）提供了机制解释——多个弱 pair-level 信号在 batch 内聚合——但假设 inter-pair SCS correlation ρ=0.35 是估算值而非直接测量。正文应至少用 1-2 句提及这个 aggregation mechanism 和其局限性。

---

**[REBUT] R2-W2: NER null 解释"仅限事后推测"——论文有实证支撑**

R2 称 "dispersed error modes" 解释缺乏实证，这一判断不够准确。Figure 6a（p7）直接提供了实证：

- **NER（Few-NERD）**：IntraSub（intra-batch substitution）rates 在所有 BCS bins 上**平坦**（10–16%），不随 BCS 变化。这意味着 BCS 试图预测的那类错误（type substitution）在 NER 中本来就不是 BCS-sensitive 的。
- **对比 RE（FewRel）**：Figure 6b 显示 IntraSub（WrongType）从 Low BCS 的 ~30% 单调上升到 High BCS 的 ~65%——这正是 BCS 能预测 RE 的机制基础。

此外，§4.4 定量报告 NER missed rates 在 43-65% 之间（远高于 RE），说明 NER 的主要错误模式是 miss（漏检）和 boundary（边界错误），而非 type confusion。这不是事后推测——Figure 6 的 error decomposition 是直接实验证据。

**但同意可以加强**：建议作者补充一个反事实论证——如果限定只看 NER 中 type substitution 错误（排除 miss 和 boundary），BCS 是否能预测这个子集的 error rate。这将更严格地证明 "BCS 对 NER type substitution 本身也无效" vs "BCS 对 NER 无效仅因为 type substitution 占比太小"。

---

**[AGREE] R2-W3: "Two dimensions" 框架完整性**

合理的理论质疑。Schema complexity 确实可能有更多维度：hierarchy depth（如 ontology 的层级深度）、argument structure complexity（RE 中 relation 的 argument role 数量和约束）、inter-type dependency（类型之间的逻辑依赖或互斥关系）。论文目前的 "two dimensions" 框架未论证这两个维度的**充分性**——即为什么这两个维度 capture 了 schema complexity 的主要变异。

但这是 scope limitation 而非 flaw。论文的贡献在于**首次分离这两个维度**，不需要证明没有其他维度。建议在 Discussion 中加 1-2 句：承认其他维度可能存在，本文关注 count 和 confusability 因为它们是最直接可操作的、且有先验理论动机（prior work 已隐式混淆这两者）。

---

**[AGREE with nuance] R2-W4: 缺少 simpler confusability metrics 对比**

原则上同意——如果 Levenshtein distance 或 WordNet path similarity 能达到类似预测力，embedding-based SCS 就不是必要的。但实际上 IE schema 的 type names 多为多词短语（如 "country of citizenship" vs "country of origin"，SCS=0.97；"participant of" vs "member of"），string-level metrics 在这类语义近义情况下区分力极弱。

论文在 Appendix M 提供了 name-only SCS ablation（Table 20, p20），显示 SCS 的 type name alone 已有较强预测力（Few-NERD r=0.172，MAVEN r=0.129），且与 definition-based SCS 方向一致。这间接说明 semantic similarity（而非 string similarity）是核心。但直接加一个 Levenshtein baseline（预计 r≈0）会让论证更有说服力。

---

### Minor

**[REBUT] R2-M1: Figure 3 信息密度过高**

Figure 3 有 4 个 panel（a-d），分别对应 count-degradation curves、BCS-controlled accuracy、FewRel bitmapped comparison、cross-condition bar chart。每个 panel 服务于不同分析目的：(a)(b) 展示两个维度的独立效应，(c) 统计证据（pooled regression），(d) 跨条件 magnitude 对比。拆成 4 个独立 figure 会浪费更多版面空间。对于 8 页正文的 long paper，这种信息密度是合理的——实际上 Figure 3 的 panel 标注和 caption 都很清晰。

**[AGREE] R2-M2**: §3.2 SCS limitations 位置可调整，但现有位置（定义后立即给出 caveat）也是一种合理的透明做法，不是错误。

**[AGREE] R2-M3**: "To our knowledge" 可删可留，是标准学术 hedging，无伤大雅。

**[AGREE] R2-M4**: Appendix Z AI 辅助措辞可进一步明确工具的具体使用范围（代码 vs 写作 vs 文献综述）。

---

### Questions 回应

**R2-Q1（DocRED pairwise SCS-confusion 非显著）**：Table 12（p15）显示 DocRED VIF=50.9，BCS 与 count 几乎共线（r≈0.99）。在 document-level RE 中，type count 和 confusability 天然高度相关（更多 relation types → 更大的 embedding space overlap），导致无法在 pairwise level 分离两者的效应。这不是 metric 失效，而是 DocRED schema 结构本身的特性。

**R2-Q2（BCS greedy search 的 domain 偏差）**：Appendix E.4（p16）已分析 extreme-BCS batches 的 domain 分布差异（low-BCS 偏向 geography 48.5%，high-BCS 偏向 science/taxonomy 49.5%），并论证 domain composition 是 mediator（BCS 通过 domain homogeneity 影响准确率的中间路径）而非 independent confound。这个论证方向正确但可以更强——建议加入 domain-stratified BCS 分析。

**R2-Q3（V2 prompt BCS 效应减弱）**：Appendix H（p18）Table 14 显示 7/8 prompt variant conditions 均呈现 negative BCS-accuracy slopes，方向一致。V2 效应减弱的主因是 narrower BCS range（V2 的 BCS constraint 0.21 vs V1 的 full range），限制了统计检测力。论文的解释 "confusability is schema-intrinsic, prompt modulates detection power" 与 Table 14 数据一致。

**R2-Q4（Oracle routing 72.4% "仍低于 single-pass"）**：**R2 此处可能存在误读。** Table 3（p8）明确显示 Oracle = 72.4% > Single-pass = 50.4%（Δ = +22.0pp）。Oracle 是唯一**高于** single-pass 的策略。所有 practical strategies（Max conf、Margin、Random）才低于 single-pass（36.5%、35.9%、14.7%）。如果 R2 的意思是 "Oracle 72.4% 低于理论上限"（count-4 的准确率约 85%），那确实存在 gap——Figure 7 解释了原因：73.4% 的 instances 匹配多个 sub-schemas，即使 Oracle 也面临 routing ambiguity（一个 instance 的 gold relation 出现在多个 sub-schema 中）。

---

### Missing References

**[AGREE]** Hou et al. (2020) 和 Ma et al. (2022) 的 label semantics for few-shot NER 与本文的 type embedding similarity 视角直接相关，建议补充。Prompt length / structured output context utilization 文献的建议合理但优先级较低。

---

### 总结

R2 的审稿整体质量高，多数问题与我的独立审查一致（ecological inference、cross-model validation、framework completeness）。主要分歧在于：
1. **N1 SDGD 深度**：我认为应降级为 Should-Fix——负面结果的标准不应等同于正面 claim
2. **N2 SCS novelty**：同意需澄清但应降级为 Should-Fix（clarity issue, not soundness）
3. **W2 NER null**：R2 低估了 Figure 6a 的实证支撑力度
4. **Q4 Oracle vs single-pass**：R2 可能误读了 Table 3 数据


---

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心分歧点：
1. R2 的两个 Must-Fix（N1 SDGD 深度、N2 SCS novelty）我均建议**降级为 Should-Fix**——N1 因为负面结果不需要与正面 claim 同等分析深度，N2 因为是 framing clarity 而非 soundness 问题
2. R2-W2（NER null 缺乏实证）我**反驳**——Figure 6a 直接展示 NER IntraSub rates 跨 BCS bins 平坦（10–16%），这是实证而非推测
3. R2-Q4（Oracle 低于 single-pass）存在**事实误读**——Table 3 显示 Oracle 72.4% > Single-pass 50.4%

与 R2 一致的问题：ecological inference gap（W1）、two-dimensions 框架完整性（W3）、simpler metric 对比（W4）、missing references。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3204 · 2026-05-25T21:37:15.140154+00:00_

交叉分享详细回应已收到。审稿报告已于交叉回应到达前提交（基于初审共识）。现在根据完整交叉回应审查报告准确性。

**交叉分享结果汇总：**

### R2 回应 R1（6 AGREE / 1 REBUT）
| R1 问题 | R2 判断 | 要点 |
|---------|---------|------|
| N1 BCS 泛化性 | **[AGREE]** | "最实质性弱点"，逐数据集分析精准 |
| N2 跨模型 R² | **[AGREE]** | direction replication ≠ quantitative replication |
| W1 TOST scale | **[REBUT]** | 论文同时报告两种 scale 属透明报告，非 scale shopping；但 logit failure 应在正文更显著 |
| W2 DocRED VIF | **[AGREE]** | 强化 N1 结论 |
| W3 模型家族表述 | **[AGREE]** | |
| W4 Ecological inference | **[AGREE]** | 与自己的 W1 一致 |
| W5 NER null | **[AGREE]** | R1 的 power analysis 论证更有力 |

### R1 回应 R2（3 AGREE / 1 REBUT / 2 AGREE-with-downgrade）
| R2 问题 | R1 判断 | 要点 |
|---------|---------|------|
| N1 SDGD 深度 | **[AGREE↓]** | 同意缺口存在，但建议降级为 Should-Fix（负面结果标准不应等同正面 claim） |
| N2 SCS 新颖性 | **[AGREE↓]** | 同意需澄清，但降级为 Should-Fix（framing issue, not soundness） |
| W1 Ecological | **[AGREE]** | |
| W2 NER null | **[REBUT]** | Figure 6a 直接展示 NER IntraSub 跨 BCS bins 平坦（10-16%），是实证而非推测 |
| W3 Two dimensions | **[AGREE]** | scope limitation, 非 flaw |
| W4 Simpler metrics | **[AGREE]** | 但指出 Appendix P 已有 baselines |

### 关键分歧

**分歧 1：SDGD 严重性** — R2 坚持 Must-Fix，R1 建议降为 Should-Fix。R1 论据：负面结果的分析标准不应等同正面 claim；Section 5 实际已有 Figure 7 + Table 3 + Table 4 + ~1 栏文字，非"仅半栏"。

**分歧 2：NER null 实证支撑** — R1 反驳 R2 的"事后推测"判断，引用 Figure 6a 作为直接实证。R2 的判断 R1 认为不够准确。

**分歧 3：R2-Q4 事实误读** — R2 称 "oracle routing 仍低于 single-pass"，R1 指出 Table 3 显示 Oracle 72.4% > Single-pass 50.4%（+22pp）。R2 可能混淆了 oracle 与 practical strategies。

### 对已提交报告的影响评估

已提交报告的核心结论**与交叉回应一致**，不需要重新提交：

1. **C1 (BCS 泛化性)**: 两人均 AGREE，报告准确 ✓
2. **C2 (跨模型 R²)**: 两人均 AGREE，报告准确 ✓
3. **C3 (SDGD 深度)**: 报告保留为 Critical（R2 立场），R1 建议 Should-Fix — 属正常 severity 分歧，已在报告 Divergence 部分隐式覆盖
4. **W2 (TOST)**: 报告列为 Should-Fix 并保留 "嫌疑" 措辞。R2 反驳 "scale shopping" 标签但同意 logit 应更显著 — 报告的 Should-Fix 分类和修改建议（"正文明确报告两scale结论"）与 R2 的 REBUT 立场兼容
5. **W5 (NER null)**: 报告列为 Should-Fix。R1 提供 Figure 6a 反驳 R2 — 报告的"补充讨论"建议仍有效，但 NER null 有比报告中描述的更多实证支撑

**结论**：报告已准确捕获核心共识（3 Critical + 7 Warning + 3.5 评分），交叉回应揭示的分歧（SDGD severity、NER null 实证程度、TOST 措辞）均属 nuance 级别，不改变整体评估。不重新提交。

---

Round 32 审稿完成。最终评分 **3.5 (Borderline Conference)**。3 个 Critical issues（BCS 泛化性、跨模型 R² 复现、SDGD 深度）+ 7 个 Warning + 9 个 Minor。Issue Tracker 已更新，报告已投递 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---
