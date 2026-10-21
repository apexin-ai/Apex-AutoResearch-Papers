---
round: 31
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T23:12:03.984116+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — Round 31 (Fresh Review)

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 (ARR May 2026)
**审稿模式**: Fresh（两位 Reviewer 独立初审 + 交叉回应，1 轮收敛）

---

## Summary

本文将 schema complexity 分解为两个独立维度——type 数量（count）和 type 间语义混淆度（SCS/BCS），通过 BCS-controlled batch 实验研究其对 training-free LLM IE 性能的独立影响。在 4 个数据集（Few-NERD NER、FewRel RE、DocRED RE、MAVEN ED）上，论文发现 count 产生跨任务的单调性能下降，BCS 在 FewRel RE 上独立预测 type substitution errors（adjusted R²=0.273）。SDGD decomposition 方法因 routing accuracy 不足而失败。论文的核心贡献是一个设计严谨的受控实证研究。

---

## Strengths

**S1.** FewRel RE 上的实验设计严谨度高于该领域平均水平：BCS-controlled batch 构造确保 count 固定下变化 confusability（VIF=1.18 确认正交性）、cluster bootstrap 处理 shared-instance 依赖、Bonferroni 校正后核心结论仍 p<0.001。[R1-S1, R2-S1, 共识]

**S2.** 有价值的错误分类体系（IntraSub, merge amplification, routing failure），Figure 2 展示 IntraSub 随 BCS 单调递增，提供超越相关性的机制性洞察。[R2-S2]

**S3.** 诚实报告三组负面结果（NER null、MAVEN centrality confound、SDGD 全面失败），对社区有信息价值。ARR 鼓励发表负面结果。[R1-S2, R2-S3, 共识]

**S4.** 18 页附录涵盖 prompt sensitivity、cross-model validation、Monte Carlo simulation、factorial analysis、bootstrap CI robustness、domain distribution 等，远超同类 empirical study 的平均水准。[R1-S4, R2-S4, 共识]

**S5.** 跨 4 个数据集 3 个 IE 任务的验证广度，SCS 作为 pre-deployment lightweight proxy 有实用价值。[R2-S5, R2-S6]

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1 [critical, 共识] 标题/摘要对 "Information Extraction" 的泛化声明超出证据支撑范围。**
- 位置：Title, Abstract, Section 6
- 问题：Confusability（BCS）的独立预测效应仅在 FewRel RE 上干净成立（VIF=1.18, adjusted R²=0.273）。NER 整体准确率效应为 null（Figure 2a IntraSub 机制存在但 achievable BCS range 过窄，无法产生可检测的准确率差异）；MAVEN 被 centrality 完全混淆；DocRED 因 VIF=50.9 不可靠。Count-degradation 跨任务通用，但标题和摘要将 confusability 效应隐含地泛化到全部 IE 任务。
- 影响：核心 claim 的 scope 与证据不匹配，审稿人可能以 overclaiming 为由拒稿。
- 建议：标题加 RE-specific 限定词或在摘要首段即标注 task-specificity；区分 count（通用结论）和 confusability（RE-specific 结论）的 generalizability。

**C2 [critical, 共识] DocRED §4.3 VIF=50.9 下的呈现顺序产生 replication 错觉。**
- 位置：Section 4.3
- 问题：§4.3 DocRED 段先报告 partial ρ=−0.762 和效应量（−25.0pp, −15.7pp），再在同段后半 qualify VIF=50.9——这种先数字后限定的写法让读者产生 BCS 效应在 DocRED 上 replicate 的印象。实际 semipartial R²_BCS=0.056（仅 5.6% unique variance），标准误膨胀 ~7x。Ridge regularization 保留 negative coefficient 方向但通过引入 bias 换取 variance reduction，不解决共线性的语义问题。
- 建议：§4.3 DocRED 段首句标注 VIF=50.9 + "仅供方向性参考"；详细数值报告移至 appendix；明确 ridge 局限性。

### Reviewer 分歧项

**D1 [分歧] SCS/BCS 相对于 LLM-PEE (Liu et al., 2025) 的新颖性论证。**
- 位置：Section 2, Section 3.2
- R2 判定 Must-Fix：SCS 本质是 type label embedding cosine similarity，计算层面与 LLM-PEE 的 schema partitioning 相同。论文提出的三点差异中，(1) controlled analysis vs. engineering 是视角差异，(3) SDGD 是负面结果，仅 (2) BCS-controlled design 有新颖性，但属实验方法论贡献非 metric 创新。
- R1 REBUT：本文是方法论论文而非 metric 论文。BCS-controlled batch design + VIF verification + cluster bootstrap 的受控实验方法论在零样本 IE 领域是首次。从工程到诊断的视角转变是实质性方法论创新。
- **Director 评估**：两种审稿视角均有合理性。论文应在 §2 更显式地将贡献定位为 "controlled empirical study using embedding similarity as an analytical lens"，弱化 SCS/BCS 作为独立 metric 贡献的叙事，同时正面论证受控实验方法论本身的贡献。

### Should-Fix（影响评分但不一票否决）

**W1 [warning, 共识] 模型多样性不足。**
- 位置：Section 3.5, Section 6, Appendix T/U
- 问题：主实验仅 Qwen3-32B。Cross-model validation（LLaMA-8B/70B, Gemini 2.5 Flash）仅覆盖 count curves 和 BCS-controlled accuracy，不包括 TOST equivalence test 和 SDGD 分析。缺少闭源 frontier models（GPT-4o, Claude）。R2 判定 Must-Fix，R1 同意方向但建议降级（4 模型 3 家族方向一致，一阶 replication 达领域惯例）。
- 建议：提升至少一个非 Qwen 模型为主分析，或严格限定 Section 6 声明范围。

**W2 [warning, 共识] TOST logit-scale 不通过应在主文标注。**
- 位置：Section 4.4, Limitations
- 问题：±3pp equivalence margin 在 probability scale 和 logit scale 语义不同。TOST 在 logit scale 不通过意味着两个维度在非线性变换下的 additivity 无法确认，影响 "independently addressable" 结论强度。当前仅在 Limitations 提及。
- 建议：§4.4 讨论 factorial analysis 时直接标注量表依赖性。

**W3 [warning, 共识] Extreme-BCS batch domain composition confound 未控制。**
- 位置：Section 4.3, Appendix E.4
- 问题：Low-BCS batches 偏向 geography/creative work，high-BCS batches 偏向 science/taxonomy/event。如果不同 domain 抽取难度不同，observed BCS-performance 关系可能部分反映 domain difficulty。Regression 未将 domain diversity/entropy 作为 control variable。
- 建议：做 domain-controlled regression 或 stratified analysis。

**W4 [warning, 共识] RQ3 (Schema Decomposition) 分析不充分。**
- 位置：Section 5
- 问题：RQ3 是三个研究问题之一，但 Section 5 仅约半栏。Oracle routing 仅达 72.4%（vs. single-type >85%），暗示 decompose-then-merge 架构本身有结构性问题（merge amplification），即使 routing 完美也无法完全避免。论文对此讨论不足。
- 建议：正文引用 Appendix B oracle routing 结果；讨论 merge amplification 根本问题；至少简要提及避免 merge 的替代架构。

**W5 [warning, 共识] FP8 量化 non-determinism 对 regression power 的影响未分析。**
- 位置：Section 3.5
- 问题：SD=0.83pp 占 observed BCS effect (Δ≈1.9–4.6pp) 的 18–44%。Bootstrap CI 不区分信号方差和测量噪声，可能膨胀 residual variance 并削弱 regression power。
- 建议：讨论 FP8 noise floor 对 smallest detectable BCS slope 的影响。

**W6 [warning, 共识] 未解释方差讨论不足 + 因果性语言。**
- 位置：Section 4.3, Section 6
- 问题：BCS 解释 FewRel 约 27% accuracy variance，73% 未解释。R1 指出 27% semipartial R² 在 NLP 中属 large effect，但论文未讨论 prompt formatting、type definition quality、sentence complexity 等可能的未解释因素。Section 6 "BCS captures a structural property" 为半因果性语言。
- 建议：Discussion 列出可能的未解释因素；改用 "serves as a useful predictor of" 等更审慎措辞。

**W7 [warning, 部分共识] BCS mean aggregation 设计选择论证不足。**
- 位置：Section 3.2, Appendix I
- 问题：R1 指出 Appendix I Table 15 已做 mean vs max BCS 对比（方向一致），R2 遗漏此分析。但 top-k/加权方案未探索，且正文未引用 Appendix I 结果。
- 建议：正文引用 Appendix I mean vs max 对比结果；讨论 aggregation 策略选择理由。

---

## Questions（需作者澄清）

1. FewRel 上是否测试过 centrality 作为 confound？（R2 指出 Appendix E.1 Table 12 已确认 VIF=1.25，centrality 非 confound——R1 可能遗漏此分析）
2. Max-based BCS 是否比 mean-based BCS 预测更好？（Appendix I Table 15 已有初步对比，正文应引用）
3. Figure 1a NER U 形 count curve 是否通过 per-type recall 验证了 type-filtering overhead 解释？
4. Qwen3-32B 作为主模型的选择理由是什么？
5. SDGD 是否考虑过完全避免 merge 步骤的分解方案？
6. FP8 noise floor 下，regression 能可靠检测的最小 BCS slope 是多少？

---

## Missing References

| 文献 | 来源 | 状态 |
|------|------|------|
| PARSE (Shrinivas et al., 2025) — LLM-driven schema optimization | R2 | 待确认相关性 |
| ASEE (2025) — Adaptive Schema-Aware Event Extraction | R2 | 待确认相关性 |
| Li et al. (2023) "Evaluating ChatGPT's IE Capabilities" | R1 | 应引用 |
| Josifoski et al. (2022) "GenIE: Generative IE" | R1 | 应引用 |
| GLiREL (NAACL 2025) | R2 | R1 指出已被引用（Boyler et al. 2025），R2 事实有误 |

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 项目配置未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态：已完成。** 0 critical, 3 warning, 12 info。

### Warnings
1. **前 3 页连续纯文本**，无任何 display item。审稿人翻到第 5 页才看到 Figure 1。建议在前 2 页加入概览图或将 Figure 1 核心 panel 前置。
2. **主正文 8 页仅 4 个 display items**（Figure 1-2, Table 1-2），密度 0.5/页，低于实证论文惯例（5-8 个/9 页）。大量结果被放入 15 页 appendix，导致正文偏"文字墙"。建议从 appendix 提升 1-2 个关键表格。
3. **Pages 2-3 连续纯文本**（Related Work + Experimental Setup 开头），无 equation/figure/table 穿插。

### Positives
- ACL 匿名格式合规，Title/Author/Abstract 排版整洁
- 所有表格使用 booktabs 风格
- Figure 1 双 panel 配色色盲友好，caption 自包含
- Figure 2 信息量充足，error taxonomy 可视化清晰
- 无 margin 溢出、LaTeX 渲染错误
- Limitations 长度适中（3 点 1 段），符合 EMNLP 规范
- References 格式统一，无未解析引用

---

## Overall Assessment

**评分：3.5 — Borderline Conference**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |
| Excitement | 3/5 | 3/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**综合评估**：
本文在 FewRel RE 上展示了一项方法论严谨的受控实证研究，BCS-controlled batch design 和统计分析（VIF 验证、cluster bootstrap、Bonferroni 校正）代表了 training-free LLM IE 领域少见的严格水准。负面结果（NER null、SDGD 失败）的诚实报告对社区有信息价值。

**阻止接收的核心问题**：
1. 标题和摘要将 confusability 效应隐含泛化到 "Information Extraction"，但独立预测效应仅在 FewRel sentence-level RE 上干净成立——这是 scope-evidence mismatch 问题，可修复但不可忽视。
2. DocRED §4.3 的呈现顺序产生 replication 错觉，需要调整。
3. 新颖性定位存在分歧：一位 Reviewer 认为 SCS 与 LLM-PEE 计算层面重叠严重，另一位认为受控实验方法论本身构成创新。论文应更清晰地定位贡献。

**如果 Must-Fix 问题被充分解决**（标题/摘要限定 scope、DocRED 呈现修正、贡献定位明确化），本文有望达到 Conference 级别（3.5→4.0）——方法论素养和统计严谨性是加分项。如果 Must-Fix 未解决，将更适合 Findings。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识 [AGREE]：
- 标题/摘要泛化超出证据（C1）
- DocRED VIF=50.9 呈现矛盾（C2）
- 模型多样性不足（W1，severity 有分歧）
- TOST logit-scale 主文未标注（W2）
- Domain composition confound（W3）
- RQ3 分析不充分（W4）
- FP8 non-determinism power（W5）
- 未解释方差讨论不足（W6）
- BCS 消融部分不足（W7）
- Figure 1b 可读性、Table 1 术语、type name 粒度（Minor）

## Reviewer Divergence

**D1: SCS vs LLM-PEE 新颖性**（R2: Must-Fix, R1: REBUT）
- R2 认为 SCS 计算与 LLM-PEE 重叠，技术贡献独特性不足
- R1 认为受控实验方法论（非 metric）是贡献核心，视角转变构成创新
- Director 评估：属于合理评审视角差异，论文应更清晰地定位为 empirical methodology 贡献

**NER 结果性质**（minor 分歧）
- R1 概括为 "null"
- R2 补充：Figure 2a IntraSub 机制证据存在（ρ=0.84–1.1），是 "null overall accuracy but active mechanism" 的 boundary condition，不等于 "no effect"
- Director 评估：R2 的细化更准确，论文应在正文区分 accuracy-level null 和 mechanism-level evidence

---

## Detailed Comments

### Section-by-Section

**Abstract/Title**：需限定 confusability claim 的 task-specificity，区分 count（通用）和 confusability（RE-specific）。"drives" → "predicts" 的修改方向正确但不充分——需在首段即标注 "specifically in relation extraction"。

**Section 2 (Related Work)**：与 LLM-PEE 的技术差异论证不充分。应显式对比 LLM-PEE 的 uncontrolled schema splitting 和本文的 controlled batch design。补充 Li et al. (2023)、GenIE (2022)。确认 PARSE/ASEE 相关性。

**Section 3.2 (Metrics)**：BCS mean aggregation 选择理由应在正文讨论（引用 Appendix I Table 15 的 mean vs max 对比结果）。MiniLM 作为 pre-deployment proxy 的定位合理，但应在 §3.2 或 §6 讨论其与目标 LLM 实际 confusability 机制的关系。

**Section 3.5 (Model)**：Qwen3-32B 选择理由应明确说明。FP8 quantization non-determinism (SD=0.83pp) 对 regression power 的影响应讨论。

**Section 4.3 (BCS-Controlled)**：DocRED 段应首句标注 VIF caveat。FewRel regression 应控制 domain diversity 变量。正文应注明 FewRel centrality non-confound（引用 Appendix E.1）。

**Section 4.4 (Factorial)**：TOST 量表依赖性应在此处标注（probability 通过，logit 不通过），不仅放 Limitations。

**Section 5 (SDGD)**：应引用 oracle routing 结果（Table 9, Appendix B），讨论 merge amplification 的结构性问题，简要提及替代架构。

**Section 6 (Discussion)**：
- "BCS captures a structural property" → 更审慎措辞
- 列出可能的未解释因素（prompt formatting, type definition quality, sentence complexity）
- 限定 claim 范围至 Qwen3-32B（除非提升其他模型为主分析）

**Figures/Tables**：
- Figure 1b：考虑改用 grouped line chart 或增大尺寸
- Figure 1(b) caption：标注 accuracy 定义
- Table 1：Few-NERD "trigger mentions" 应改为 NER 术语
