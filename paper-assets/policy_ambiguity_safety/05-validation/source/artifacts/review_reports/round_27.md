---
round: 27
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-23T13:36:07.882699+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 27

**Paper**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
**Venue**: EMNLP 2026 via ARR May 2026 cycle
**Reviewers**: R1 (方法严谨性, 3.5/5), R2 (新颖性/完整性, 3.0/5)
**交叉回应**: 完成，1 轮收敛

---

## Summary

本文使用匹配对因果设计研究 LLM agent 在自然语言策略规范中遇到歧义时的安全违规问题。在 τ²-bench 上构建 300 个匹配 clause pair（6 种歧义类型，5 个模型，2,997 episodes），发现歧义条款使违规率增加 34.0 pp（排除 incompleteness 后 31.0 pp）。论文进一步提出 type-mechanism dissociation（V=0.45 vs 0.14，LLM-coded）、disambiguation neglect（4.6% awareness）和 systematic nocuity（41.3% convergent violations，77% permissive bias）。SOPBench 跨基准复制显示方向一致（+12.7 pp）。

---

## Strengths

**S1 [共识]** 匹配对因果设计是本文最大的方法论优势。Perturbation control (Δ_perturb = -0.67 pp, 95% CI [-8.0, 6.67]) 有效排除表面文本变化。在 agent safety 文献中将 observational association 升级为 causal claim 是质的提升。

**S2 [共识]** 统计分析系统且透明：Holm-Bonferroni 多重比较校正、七个 margin TOST 敏感性分析、方差分解、ICC 可重复性 (0.919)、bootstrap clustering。几乎所有统计选择都有 sensitivity check。

**S3 [共识]** Claim 分级诚实：C3 标注 "inconclusive"（p=0.017 vs threshold 0.0125），C4 标注 "exploratory"。

**S4 [共识]** 实验规模（300 clause pairs × 5 models × 2 conditions = 2,997 episodes）和 Appendix 深度（13 pages）远超同类工作，可复现性高。

**S5 [共识]** Authorization scope 的透明处理——多处标注低 κ (0.385)、高跨模型方差 (52 pp range)、质量审计的 borderline pairs (16%)，并报告排除后的所有核心分析。

**S6 [R2]** SOPBench 跨基准复制和两个额外模型族扩展增加外部效度。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [共识, R1-N1 + R2-W2]** 信息添加混淆是系统性的，"confound-free" 标签不准确

论文仅将 incompleteness 标记为有 information-addition confound，但 Appendix Q 数据显示所有类型的消歧版本都系统性更长：auth scope +36.1 words, incompleteness +34.6, lexical +25.7, scopal +17.8, cond. prec. +17.5。消歧版本不仅消除歧义，还添加具体决策信息。Token count logistic regression 不能分离 disambiguation 与 information-addition 两种因果路径。Coreferential (Δtoken≈0, 18.7 pp) 是唯一干净的因果估计。

**修改要求**：(a) 承认所有类型信息添加混淆；(b) "confound-free" → "reduced-confound"；(c) 报告 per-type Δtoken vs Δviolation rate rank correlation；(d) 突出 coreferential 18.7 pp 为 confound-free 下限。

**MF2 [共识, R1-N2 + R2 AGREE]** Type-mechanism dissociation (V=0.45) 缺乏可靠人工验证

V=0.45 完全来自 LLM 编码（Gwet's AC₁=0.62, κ=0.52），存在 circularity risk。人工 mechanism 编码 κ=0.15（合并后 0.38），远低于 substantial agreement。Abstract 表述给人印象远超 "exploratory"。

**修改要求**：(a) 降级 C3 为 exploratory，Abstract 标注 "exploratory, LLM-coded"；(b) 提供 human-coded (4-cat, κ=0.38) V 值；(c) 讨论 LLM vs human 编码差异含义。

**MF3 [共识, R1-N3 + R2 AGREE]** 跨判官组类型排序 ρ=0.09 威胁 C2 稳健性

两个判官组类型排序 ρ=0.09 (p=0.87)。排除 auth scope 后 ρ=0.90，但 auth scope 占 16.7%，选择性排除不可接受。Judge-model identity 完全交织，ρ=0.09 可能同时反映 type ordering instability 和 judge-model interaction。

**修改要求**：(a) 正文充分讨论 ρ=0.09 对 C2 影响；(b) 用三个判官族重算 C2；(c) 考虑降级 C2。

**MF4 [共识, R2-N1 + R1 AGREE]** "Nocuous" 术语语义反转论证不足

Berry 原意 divergent=harmful，本文 convergent wrong interpretation 在 Berry 框架下更接近 innocuous。仅一句话完成术语重定义。与 Gur-Arieh et al. "ambiguity collapse" 高度重叠但讨论不足。

**修改要求**：(a) 明确 convergent nocuity vs divergent nocuity 区分；(b) 深入讨论与 ambiguity collapse 的关系；(c) 论证 convergent wrong interpretation 在 agentic 语境下的 harm 模式。

### Should-Fix

**SF1 [分歧→降级]** 增量贡献论证（R2 认为 "better methodology for known finding"；R1 反驳因果识别是质的提升。共识：C1 有方法论价值，但需更明确论述 matched-pair 独有发现）

**SF2 [共识降级]** 标题 domain scope 应限定为 customer-service（Abstract 已限定，但标题暗示 general）

**SF3 [共识]** SESOI ±15 pp 缺乏领域锚定，cluster structure margin-dependent（±10pp 3/6, ±12pp 5/6, ±15pp 6/6）

**SF4 [共识]** SOPBench 2/5 模型未显著但 Abstract 未披露（GPT-5.4 p=0.052, DeepSeek p=0.163）

**SF5 [共识]** "Ambiguity" 广义使用需引用 Poesio/van Deemter underspecification 区分文献

**SF6 [共识]** Temperature=0 限制需更充分讨论（测量 default interpretation 非 outcome distribution）

**SF7 [R1+R2]** Clause pair 质量——scopal 示例更像 vagueness/incompleteness 而非 scope ambiguity

### Minor

- **M1**: "Tier" → "Cluster"，"conditional OR" → "McNemar OR"
- **M2**: Conclusion 过于简略（一句话），应扩展
- **M3**: Prevalence audit "55-87%" 应附 CI 并更谨慎
- **M4**: Cramér's V 跨维度比较应标注 caveat

---

## Reviewer Consensus [AGREE]

1. "Confound-free" 标签不准确——信息添加是系统性的（R1-N1, R2-W2）
2. Type-mechanism dissociation 缺乏人工验证（R1-N2, R2 AGREE）
3. ρ=0.09 威胁 C2（R1-N3, R2 AGREE）
4. "Nocuous" 术语论证不足（R2-N1, R1 AGREE）
5. C1 因果设计的方法论价值是真实贡献（S1）
6. Temperature=0 需更充分讨论（R1-W4, R2-Q5）
7. SOPBench 报告透明度不足（R1-W2, R2 AGREE）
8. Poesio/van Deemter 文献遗漏（R2-W5, R1 AGREE）

## Reviewer Divergence [REBUT]

**增量贡献评估**：R2 认为 "better methodology for a known finding" (3.0)；R1 反驳因果识别是质的提升而非 incremental improvement (3.5)。R1 论证有力——DRIP-R correlational design 无法区分因果与共现。但两位均同意：type-level contributions (C2/C3) 的证据链缺陷削弱 overall novelty。

**60.8% 残差方差**：R2 认为削弱因果叙事；R1 反驳匹配对因果识别不依赖解释总方差比例。R1 反驳正确——高残差反映 clause-level heterogeneity，是 C2 的 qualification 而非 C1 的缺陷。

---

## Questions

**Q1 [共识]**: 人工合并后编码 (4-cat, κ=0.38) 的 Cramér's V 值？直接决定 C3 证据强度。
**Q2 [共识]**: Per-type Δtoken vs Δviolation rate 的 rank correlation？量化信息添加 confound severity。
**Q3 [共识]**: Cross-judge 非对称分配（3:2）的理由？为何不用 full cross-design？
**Q4 [R1]**: 跨 provider ICC？Kendall's W=0.398 (p=0.072) 暗示跨 provider 一致性较低。
**Q5 [R2]**: V=0.45 的置信区间？CI 下限接近 0.3 则 "diagnostic instrument" reframing 削弱。
**Q6 [共识]**: 是否有 temperature>0 pilot data？

---

## Missing References

1. **Poesio (1996) / van Deemter (2004)** [共识] — ambiguity vs underspecification 经典区分
2. **Zhu et al. (2025)** [共识] — "Ambiguity in LLMs is a concept missing problem"
3. **AgentSpec (Poskitt et al., ICSE 2026)** [R2] — runtime enforcement for LLM agents
4. **"The Illusion of Certainty" (arXiv:2511.04418)** [R2] — LLM uncertainty quantification
5. **Rosenbaum (2002)** [R1] — matched-pair hidden bias sensitivity analysis

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

视觉审查已完成（1 critical + 3 warning + 5 info）：

- **[critical] p.23**: 最后一页仅 5 行文字（~5% 页面），其余全部空白。建议合并或补充内容。
- **[warning] p.7**: Table 2 + Figure 3 + Figure 4 三个 display item 挤在同一页。建议 Figure 4 移至 p.8。
- **[warning] p.13**: 附录 6 张表格挤在同一页，间距极小。
- **[warning] p.18**: 附录 5 张表格挤在同一页，Table 14 字号偏小。
- **[info]**: Figure 1/3/4 内部文字偏小；Figure 2 颜色方案应验证色盲友好性；主文约 8.5 页，符合 EMNLP 8 页限制。

---

## Overall Assessment

**评分: 3.0 (Findings)**
**置信度: 4/5**
**Reviewer 分歧**: R1 3.5 (Borderline Conference) / R2 3.0 (Findings)

C1（二元因果效应，+31.0 pp reduced-confound）方法论执行质量高——匹配对设计 + perturbation control + 七模型复制 + 跨基准方向一致性。R1 正确指出因果识别相对于 DRIP-R 的 correlational design 是质的提升。

但论文呈现的是三个 contributions 的整体叙事：
- **C2 (type partial ordering)**：被 ρ=0.09 和 margin-dependent cluster structure 严重削弱
- **C3 (type-mechanism dissociation)**：核心证据 V=0.45 完全依赖 LLM 编码，人工验证不足
- **Framing**："confound-free" 标签不准确；"nocuous" 术语反转论证不足

三个 contributions 中两个的证据链存在实质性缺陷，加上术语框架问题，论文整体处于 Findings 级别。

**修改后可达 3.5 的条件**：(a) 报告 human-coded V' 和 Δtoken-Δviolation correlation 来量化两个核心 confound；(b) 降级 C3 为 exploratory；(c) 不再依赖选择性排除 auth scope；(d) 扩展 nocuous 术语论证。

---

## Detailed Comments

**Introduction**: "Nocuous" 反转需展开论证（MF4）；C3 应标注 "exploratory, LLM-coded"（MF2）
**Section 3**: 引用 Poesio/van Deemter（SF5）；Appendix M 排除论证可补充 ellipsis/pragmatic implication 示例
**Section 4.2**: 承认所有类型信息添加混淆（MF1）
**Section 4.4**: 说明 cross-judge 非对称分配理由（Q3）
**Section 4.6**: 明确 cluster structure margin-dependency（SF3）
**Section 5.2**: ρ=0.09 从 qualification 提升为正式讨论（MF3）；所有 "confound-free" → "reduced-confound"（MF1）
**Section 6**: C3 降级为 exploratory（MF2）；提供 human-coded V'（Q1）
**Section 7**: 扩展 convergent nocuity 论证（MF4）；讨论 information-addition confound（MF1）
**Abstract**: "+12.7 pp" 注明 3/5 显著（SF4）；V=0.45 标注 "exploratory, LLM-coded"；"confound-free" → "reduced-confound"
**Conclusion**: 扩展 implications 和 future work（M2）