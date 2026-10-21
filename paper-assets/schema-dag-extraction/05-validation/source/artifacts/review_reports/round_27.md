---
round: 27
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T21:25:45.623814+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 25 (Fresh)

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle, Long Paper)
**Deadline**: 2026-05-25
**审稿模式**: Fresh (重新审稿，无上轮记忆)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）

---

## Summary

本文通过受控实验设计研究 training-free LLM 信息抽取中 schema 复杂度的两个维度——type count 和 type confusability——如何独立预测性能下降。使用 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 量化 confusability，在 Few-NERD (NER)、FewRel (RE)、DocRED (document-level RE)、MAVEN (ED) 上通过 count curve 和 BCS-controlled 实验验证。核心发现：(1) count 驱动 recall 下降（跨任务 robust），(2) confusability 驱动 type substitution（BCS 在 FewRel 解释 ~22% batch-level RE accuracy variance），(3) NER batch-level BCS 信号未检测到（task asymmetry），(4) Schema decomposition 因 merge amplification 和 routing failure 失败。

---

## Strengths

**S1. 研究问题明确且实用。** 将 schema 复杂度分解为 count 和 confusability 两个独立维度是干净、有说服力的框架。SCS 作为无需运行抽取即可计算的 pre-hoc proxy，对 practitioners 有直接部署价值。

**S2. FewRel BCS-controlled 实验设计严谨。** Within-pool 80-relation 比较有效控制 type frequency 混淆；2×2 factorial analysis 正式检验了 interaction boundedness；TOST 等价检验引入了 NLP 领域罕见的统计严谨性。[R1, R2 共识]

**S3. 统计方法论远超同领域平均水平。** Bootstrap CIs、permutation tests、partial correlation (controlling degree centrality/type frequency)、TOST、power analysis for NER null——这种统计意识在 NLP 投稿中非常突出。[R1, R2 共识]

**S4. 负面结果的诚实报告。** §5 完整报告 SDGD 失败及其原因分析（merge amplification, routing failure）。NER batch-level null 在 3 模型上确认并明确标注可能是 insufficient power。[R1, R2 共识]

**S5. 极为丰富的补充材料。** 18 个附录（A–Y）系统性地回应可预见审稿问题：cross-model validation, prompt sensitivity, confound analysis, ecological simulation, format independence, relaxed matching 等，显示极高实验完整度。[R1, R2 共识]

**S6. 跨任务覆盖与 error taxonomy。** 跨 NER/RE/ED 三个核心 IE 任务、四个标准数据集。Error taxonomy decomposition (§4.4, Figure 2) 将 BCS 效应分解到具体错误类型（IntraSub, missed），提供 actionable 诊断信息。[R2]

---

## Weaknesses

### Must-Fix（影响接收决定，4 项，R1+R2 共识）

**C1. DocRED VIF=50.9 严重削弱 R²=58% 的可解释性** [R1-W1, R2 AGREE]
- DocRED BCS-centrality collinearity VIF=50.9（Table 11），远超阈值 10。partial r=−0.344 的解释力远低于 full model R²=58%。读者无法区分 BCS 独立贡献与 centrality 混淆效应。
- **要求**：报告 DocRED semipartial R²（BCS unique variance），或使用 ridge/LASSO 回归；在 §4.3 和 Abstract 中明确标注 VIF=50.9 的局限，将 DocRED 定位为 "directionally consistent but confounded"。
- **R2 补充**：核心证据在 FewRel（VIF=1.18），DocRED 是 supporting evidence——问题真实但对核心 claim 的威胁低于表面上看到的程度（前提是作者修正措辞）。

**C2. Confusability 发现仅在 FewRel RE 上稳健成立，generality claims 过度** [R1-W2, R2 AGREE with nuance]
- 逐数据集审计：
  - **FewRel RE**: ✓ 批次级 R²≈22%，跨模型一致（3 open-weight families）
  - **NER (Few-NERD)**: ✗ 批次级 BCS null，3 模型均未检测到（Table 5）
  - **DocRED**: △ VIF=50.9 使 BCS 独立贡献不可识别（C1）
  - **MAVEN**: △ Per-type BCS-F1 正相关主要由 frequency/centrality confound 驱动（Appendix E）
  - **Gemini Flash**: △ Leave-one-out sensitivity r: −0.80→−0.42, p=0.22（Appendix U）
- **要求**：弱化 title/abstract/conclusion 中的跨任务 generality claims；明确 confusability 证据主要来自 FewRel RE。Count degradation（跨任务 robust）可保持 general framing。
- **R2 nuance**：Abstract 已部分限定（"In RE, BCS explains..."），且 count degradation 确实跨任务稳健。论文未完全忽视此限制，但需进一步明确。

**C3. NER null result 机制解释不充分** [R2-W2, R1 AGREE]
- NER 对 BCS 无显著响应是论文最意外的发现之一，但机制解释停留在描述层面。论文同时持有两个未区分的假设：(a) NER 错误模式不同（miss/boundary/type 分散，而非集中于 type substitution）；(b) BCS range restriction（SD ratio 19%）导致 insufficient power（detectable r≈0.132 at 80% power, n=450）。两者有不同 practical implications，但论文未提供区分证据。
- **要求**：在正文（非仅附录）明确承认 "基于现有证据无法区分零效应与被噪声掩盖的效应"；加入 power analysis 定量摘要（n=25 per condition, detectable effect=5.5pp, observed r≈−0.11）；标注 Gemini NER 未测试。
- **R1 补充**：要求新实验超出 revision 范围；文字上的诚实表述即可。

**C4. 贡献定位：BCS-controlled batch design 是标准分层实验设计** [R2-W1, R1 AGREE partially]
- BCS-controlled batching 是经典 blocking/stratified experimental design，在统计学和实验心理学中已有数十年历史。论文 §1 将 "the methodology—BCS-stratified batch construction with partial-correlation controls—is the contribution" 作为首要贡献，过度抬高了实验设计技术本身的新颖性。
- **要求**：将核心贡献从 "methodology" 重新定位为 "empirical findings about confusability's independent predictive role, enabled by controlled design using SCS/BCS"。
- **R1 nuance**：领域特定的操作化（SCS 定义、greedy extreme-batch 算法、多数据集验证）有 applied methodology 价值。这是 framing 问题而非 substance 问题，不应构成 rejection 理由。

### Should-Fix（影响评分但不一票否决，8 项）

**W1. Error taxonomy / TOST / SDGD 均为 single-model** [R1-W4, R2-W4, 双方独立提出]
- 这三项分析支撑重要 claim（confusability→type substitution; count×BCS interaction bounded; decomposition fails），但均仅在 Qwen3-32B 上验证。SDGD 的 merge amplification 可能是 Qwen3-32B 特定的 instruction-following 问题。
- **建议**：至少在一个 alternative model 上复现 error taxonomy/TOST 核心结果；如资源不允许，在 Limitations 明确标注。

**W2. 跨模型验证结果未整合入正文** [R2-W4, R1 AGREE]
- 主实验全部基于 Qwen3-32B，cross-model 结果仅在 Appendix T/U。对声称 "across three open-weight model families" 的论文，核心 cross-model 结果应出现在正文。
- **建议**：§4.1 和 §4.3 末尾各加 1-2 句 cross-model summary。

**W3. Ecological amplification (1.3%→22%) 需更多 batch-level confound 控制** [R1-W3 Must-Fix, R2 REBUT → Director 降级为 Should-Fix]
- Appendix N 的 Monte Carlo simulation 使用 conditional ρ=0.35（pairs sharing common type），非 marginal r≈0.112–0.167。论文已声明 simulation 是 illustrative，核心因果证据在 §4.3 controlled experiment。但 batch-level 回归未加入 domain diversity、type frequency 等额外控制变量。
- **R2 反驳要点**：(1) ρ=0.35 来自条件子集合理；(2) simulation 是 illustrative 非 confirmatory；(3) Appendix O variance decomposition 部分回应了 confound 关切。
- **Director 判断**：R2 的反驳有说服力（核心证据在 controlled experiment 而非 simulation），但 R1 关于 batch-level confound 的关切有效。降级为 Should-Fix。
- **建议**：batch-level 回归中加入 batch-mean type frequency 和 domain diversity 控制变量，报告 R² 变化；正文明确 simulation 的 illustrative 定位。

**W4. TOST ±3pp margin: logit-scale 不一致性** [R1-W5, R2 AGREE]
- FewRel ~80% 准确率下 ±3pp 对应 ~15% 相对误差。Probability-scale TOST 通过（p=0.003），logit-scale inconclusive（p=0.209）。Back-transformed interaction at median=2.78pp 接近 boundary。Margin 缺乏 domain-specific justification。
- **建议**：正文承认 logit-scale 不一致性；讨论 probability-scale 作为 primary metric 的理由；引用附录 sensitivity analysis。

**W5. Abstract 信息密度过高** [R2-W5, R1 AGREE as minor]
- ~150 词中 6+ 具体数字（"0.72→~0.27", "85.7%→50.4%", "~22%", "~49pp" 等），核心 takeaway 被数字流淹没。
- **建议**：以定性 conceptual message 开头，保留 1-2 个最重要的数字。

**W6. Discussion/Conclusion 过度压缩** [R2-W6, R1 AGREE]
- Discussion + Conclusion 合并在 p.8 下半页约 25 行，practical implications（SCS 诊断工具、schema-aware pool selection）每个仅一句话。
- **建议**：从 §2 (Related Work) 或 Limitations 挤出空间（~0.3 页）给 Discussion。

**W7. Pairwise r²≈1.3% 实际意义未讨论** [R1-W7, R2 AGREE with nuance]
- IQR-predicted gap 仅 2.2pp。论文未讨论在什么使用场景下 2.2pp 是 actionable 的。
- **R2 nuance**：pair-level（1.3%）和 batch-level（22%）对应不同 practical scenario——pair-level 对应单个 type pair 混淆预测，batch-level 对应 prompt schema 设计。后者是 training-free IE 的典型 use case。
- **建议**：Discussion 中区分两个 granularity 的 practical implications；讨论 SCS 阈值建议。

**W8. "First controlled study" claim 需更精确限定** [R2-W7, R1 AGREE partially]
- Chen et al. (2026) 以类似设计逻辑隔离 instance count + context length。Claim 技术上成立但易引发歧义。
- **建议**：改为 "first controlled study specifically isolating type confusability from type count using embedding-based batch-level controls in zero-shot LLM IE"。

---

## Reviewer Consensus

以下问题 R1、R2 达成共识：

| 编号 | 问题 | 共识 |
|------|------|------|
| C1 | DocRED VIF=50.9 | [AGREE] 必须报告 semipartial R²，demote DocRED |
| C2 | Confusability 仅 FewRel RE 稳健 | [AGREE] 弱化 generality claims |
| C3 | NER null 机制不明 | [AGREE] 正文承认无法区分两假设 |
| C4 | 贡献定位 methodology→findings | [AGREE] reframe 核心贡献 |
| W1 | Single-model 二级分析 | [AGREE] 标注或补充验证 |
| W2 | Cross-model 不在正文 | [AGREE] 加 summary |
| W4 | TOST logit 不一致 | [AGREE] 正文讨论 |
| W5 | Abstract 数字过多 | [AGREE] 简化 |
| W6 | Discussion 压缩 | [AGREE] 扩展 |
| W7 | 2.2pp 实际意义 | [AGREE] 讨论 practical threshold |
| W8 | "First" claim | [AGREE] 更精确措辞 |

## Reviewer Divergence

| 编号 | R1 | R2 | Director 判断 |
|------|-----|-----|-------------|
| W3 (Ecological amplification) | Must-Fix: batch-level confounds 未控制 | REBUT: simulation 是 illustrative，核心证据在 §4.3 controlled experiment | **降级为 Should-Fix**。R2 反驳有说服力（因果证据在 controlled experiment 非 simulation），但 R1 的 batch-level confound 关切合理，应补充控制变量分析 |
| Limitations 长度 | REBUT: 详尽是优势 | Should-Fix: EMNLP 不应过长 | **降级为 Minor**。6 条各有实质内容，略作压缩即可（合并 items 4+5） |
| FewRel contamination | Should-Fix | REBUT: Appendix Q 已充分回应（方向相反 + BCS 效应不变） | **降级为 Minor**。论文已有力回应，正文加 1 句 summary 即可 |

---

## Questions to Authors

**Q1** [R1+R2 共同关切]: BCS-controlled 实验中 high-BCS 和 low-BCS extreme batches 在 domain distribution 上是否有系统偏差？高 BCS batches 是否聚集在同一 Wikidata semantic domain？Appendix O 的 variance decomposition 未分析 domain-level。

**Q2** [R2, R1 AGREE]: SDGD routing failure (Table 8) 在 oracle routing 下显著降低——是否意味着核心瓶颈是 routing quality 而非 decomposition strategy 本身？如果使用更强 routing model（GPT-4 级别），结论是否可能翻转？

**Q3** [R2, R1 AGREE]: Few-NERD 的 66 types 嵌套在 8 coarse categories——BCS 是否考虑了层级结构？同 coarse category 内的 high-SCS pairs 与跨 category 的 high-SCS pairs 对性能的影响是否不同？这可能影响 NER null 的解读。

**Q4** [R1]: DocRED full-model R²=58% 中 BCS 的 semipartial R²（unique variance after partialing centrality）是多少？如果远低于 58%，§4.3 的叙述应如何修正？

**Q5** [R1]: NER batch-level null 在 Gemini Flash 上是否测试过？如果 Gemini 也是 null，则 task asymmetry 的跨架构 robustness 更强。

**Q6** [R1]: Appendix N ecological simulation 的 ρ=0.35 是否代表 random batch 内平均 pair-level correlation？如果 random batch 的 within-batch ρ 远低于 0.35，simulated batch R² 会远低于 0.218。

---

## Missing References

以下由两位 Reviewer 建议，经 Director 评估后保留：
1. **Cohen (1988)** "Statistical Power Analysis for the Behavioral Sciences" — 论文使用 power analysis 和 TOST 但未引用此经典参考 [R1 建议, R2 同意]
2. **Baan et al. (2023)** "The Ecological Fallacy in Annotation" (ACL 2023) — NLP 领域对 ecological fallacy 的直接讨论，与 §4.3 的 ecological correlation 主题直接相关 [R2 建议, R1 同意]

以下需作者评估后决定：
3. **ScrapeGraphAI-100k** (Cataldo et al., 2025) — web extraction 场景的 schema complexity 研究 [R2 建议, R1 认为 task setting 差异大]
4. **Ding et al. (2024) "GraphER"** — schema-guided extraction [R1 建议, 需验证相关性]

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 项目配置中未启用外部审稿（`external_review.paperreview_ai.enabled` 未找到配置项）。

---

## Visual Layout Check（非评分项）

**状态：已完成** (2026-05-21 21:15→21:18, ~3 min)

| 严重性 | 数量 | 关键发现 |
|--------|------|----------|
| Warning | 3 | 见下 |
| Info | 6 | 见下 |

**Warning findings:**
1. **前 3 页无 display item**：审稿人打开论文前 3 页看不到视觉锚点。第一个 figure 直到 page 5 才出现。对于以实证为核心的 controlled study，建议将 Figure 1 关键 panel 提前到 page 2 或 Introduction 末尾。
2. **主文仅 4 个 display items**（2 figure + 2 table），对于 4 数据集、多维度分析的实证论文偏少（经验值 5-8）。大量关键数据被推到 14 页附录（20+ 表格），主文读起来像文字摘要而非数据驱动论证。建议从附录提升 1-2 个关键表格到主文。
3. **Page 8-9 连续 2 页纯文本**（§5 + §6 + Limitations），无 display item 穿插。§5 讨论 decomposition 效果可加对比表。

**Info findings:**
- Figure 1(b) 标注文字字号偏小，低缩放下难以阅读
- Figure 2 中 IntraSub/ExtraSub 线条颜色接近，色盲不友好——建议辅以不同 line style/marker
- 附录 14 页全部表格+文字，无 figure
- Page 26 底部约 1/3 空白
- Figure 1 caption 自包含性好（正面）
- Table 1 使用 booktabs 风格，排版专业（正面）

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| **Soundness** | 3.5/5 | 3.5/5 | **3.5/5** |
| **Excitement** | 3/5 | 3/5 | **3/5** |
| **Reproducibility** | 3/5 | 4/5 | **3.5/5** |

### Overall: **3.5 (Borderline Conference)**

**EMNLP 2026 ARR 评分标准**: 3.5 = Borderline Conference

### 综合评语

这是一篇研究问题重要、实验设计严谨、统计方法远超 NLP 平均水平的实证分析论文。SCS 作为 pre-hoc schema complexity proxy 有直接工程应用价值。18 个附录的覆盖面令人印象深刻。负面结果（NER null, SDGD failure）的诚实报告值得肯定。

然而，四个 Must-Fix 问题限制了当前版本的接收：

1. **DocRED R²=58% 因 VIF=50.9 不可信**——必须报告 semipartial R² 并降级 DocRED 在论文中的地位
2. **Confusability 核心贡献实际仅在 FewRel RE 上稳健成立**——NER null + DocRED confounded + MAVEN frequency-driven + Gemini fragile，使得 title/abstract 的跨任务推广 claims 缺乏充分支撑
3. **NER null 机制解释不充分**——论文同时持有零效应和 noise-masked 两个假设但未提供区分证据
4. **贡献定位过高**——BCS-controlled batch design 是标准分层实验设计在新领域的应用，应重新定位为 empirical findings 而非 methodology contribution

**修改路径**: 如果作者能 (a) 报告 DocRED semipartial R² 并修正措辞, (b) 将 generality claims 收窄到证据实际支撑的范围（FewRel RE for confusability, cross-task for count）, (c) 诚实承认 NER null 的 open status, (d) 将贡献重心从 methodology 转向 empirical findings——本文有潜力达到 Conference 接收水平。当前版本更接近 strong Findings 或 borderline Conference。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度过高：6+ 具体数字挤在 ~150 词中。核心 conceptual message（"confusability independently predicts type substitution in RE"）被数字淹没。
- "across NER, RE, and event detection" 暗示三任务均有 confusability 证据，但 NER 为 null、ED 被 centrality confound。建议改为 "with evidence primarily from RE"。
- 应加 "ecological (batch-aggregate) level" 修饰 R²≈22%。

### §1 Introduction
- Contribution 1 的 "methodology is the contribution" 定位需重新表述（C4）。
- "first controlled study" 应更精确限定（W8）。
- 四个 findings 的叙述清晰，RQ 设置自然。

### §2 Related Work
- "SCS novelty" 段落（p.3）明确了 metric vs methodology 区分——这个 positioning 应提前到 §1。
- §2 有压缩空间（~0.2-0.3 页），可为 Discussion 让步。

### §3 Experimental Setup
- FewRel train+val 合并使用：Appendix Q 已回应（方向相反 + BCS 不受影响），正文可加 1 句 summary。
- §3.2 SCS 定义处未指定默认 embedding model（MiniLM 在后文才提及）。

### §4 Results
- §4.1 Count Curves：跨模型验证结果（LLaMA-8B/70B, Gemini）应有 1-2 句 summary 而非仅引用 appendix。
- §4.3 BCS-Controlled：DocRED R²=58% 需降级处理（C1）；ecological qualifier 应更突出。
- §4.4 Multi-Dimensional Degradation：NER null 解释需在此处加入 power analysis summary（C3）。TOST logit 不一致性应正文提及（W4）。
- §4.5 Centrality Confound：分析仅在 MAVEN 上成立，§3.2 的引用（"centrality consistently yields equal or stronger correlations"）应更精确。

### §5 Schema Decomposition
- 过度压缩（~1/3 页）。Oracle routing 成功（72.4% vs 50.4%）意味着 decomposition 是 routing-conditional failure，非绝对失败——措辞应调整。
- 建议加 Table 7 或类似 summary 到正文。

### §6 Discussion and Conclusion
- ~25 行过度压缩。Practical implications（SCS 作为诊断、schema-aware pool selection）每个仅一句。
- 未讨论 pair-level 2.2pp vs batch-level 22% 的 practical significance 差异（W7）。

### Limitations
- 内容充实且诚实。6 条 + 2 段技术上各有实质，但总体偏长。建议合并 items 4（causal mechanism）和 5（data contamination）。
- "Across-batch correlation" 和 "Multiple comparisons" 两段可压缩或移至附录。

### References / Format
- 8 个 orphan bib entries（uncited）应清理：dee-2024, gillick-2014, novack-2023, schall-2025, tam-2024, volkanovska2025ner, wei-2023, zhou-2025-rethinking。
- 正文 8 页（含 Limitations），格式合规。
- 匿名性无问题（"Anonymous ACL submission"，无作者标识泄露）。
- 缺少 Cohen (1988) 和 Baan et al. (2023) 引用。