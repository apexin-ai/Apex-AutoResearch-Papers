---
round: 10
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T18:26:21.289105+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：The Likert Blindspot

**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
**Venue**: EMNLP 2026 (ARR May cycle)
**审稿轮次**: Round 12 (fresh review)
**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+写作质量+相关工作）

---

## Summary

本文提出 Controlled Style Decomposition (CSD)，一个黑盒框架，通过 NLI 门控内容保持、单轴风格改写和位控 pairwise 比较来量化 LLM judge 的风格偏差。核心发现为 "Likert Blindspot"：Likert 评分系统性地衰减 pairwise 比较能检测到的风格偏差信号。在 4 个目标 judge（GPT-4o, Qwen3-32B, Llama-70B, Gemini-Flash）+ 1 个负控制（Claude Sonnet 4）、3 个风格轴（formality, verbosity, register）、3 个 benchmark（LLMBar, AlpacaEval, MT-Bench）上验证。GEE 条件分解揭示了逐轴混淆结构：verbosity 是 style-dominated，formality 有显著 quality confound，register 是 judge-dependent。

---

## Strengths

**S1. Verbosity 轴证据链极强。** Style OR 8.2–13.1（四个 judge 一致），Originality OR 0.38–0.49（均不显著或仅边缘），cross-rewriter 验证完整（Appendix D），direction-aware NLI 有理论和实证依据。方法论上无可挑剔。[两位共识]

**S2. 统计方法论严谨且透明。** 七种测量方法的灵敏度层级（Table 2）、Holm-Bonferroni 6 测试家族 + 8 测试敏感性分析（全部保持显著）、探索性与验证性分析的明确区分、BT GoF 检验、GEE 诊断完整（exchangeable vs independence |ΔQIC| < 0.001）、bootstrap 衰减分析区分 measurement attenuation 与 insufficient power。这在 LLM judge 评估文献中属高标准。[两位共识]

**S3. 因果声明诚实克制。** §3.5 明确声明 "we do not claim that this DAG is a complete structural causal model"，DAG 中用虚线橙色箭头标注 residual confounding，"controlled" 的定义明确限定为实验控制而非因果识别。这种克制在该领域的论文中少见。[R1 强调]

**S4. 实验控制设计充分。** 六项放大控制（NLI gate ablation、Claude 负控制、跨轴 BT 变异、rewriting artifact 吸收、debiased prompting、跨架构复现）、position swap 双向评估、NLI 阈值 11 点 sweep（BT ≤3pp 变动）、same-style double-rewrite artifact control。[两位共识]

**S5. 跨 judge 一致性强。** 四个独立架构一致复现 Blindspot（Table 1：11/11 bias-positive cells 中 8 个 Blindspot），GEE 混淆结构跨 judge 高度一致。[两位共识]

**S6. Limitations 坦诚全面。** 对 quality-style confounding、evaluator-producer overlap、construct divergence 的歧义性、样本量限制、生态效度等进行了充分讨论。[R2 强调]

---

## Weaknesses

### Must-Fix (critical) — 不修复则不可接收

**MF1. [共识] 标题和 framing 隐式预设 pairwise 为 ground truth，核心歧义未解决。**
论文标题 "Detecting Hidden Style Bias" 和 "Blindspot" 命名隐式假定 pairwise 检测到的是真实偏差、Likert 遗漏了它。然而论文自身承认三种等效解释：(a) Likert 测量衰减，(b) pairwise 放大（Comparative Trap, Jeong et al. 2025），(c) 构念分歧。六项放大控制必要但不充分——它们 bound 了 amplification 但未 eliminate。论文在 §5.1 保持 agnostic 是诚实的，但标题和 Abstract 的 framing 与此矛盾。
- **建议**：标题改为更中性的表述（如 "Measurement Divergence" 而非 "Detecting Hidden Bias"）；Abstract 前置三种解释而非在 §5.1 才讨论。
- R1 通过 formality GEE 混淆（MF2）间接支持此判断：pairwise 检测到的可能部分是 quality-style correlation 的放大。R2 直接作为 N1 (critical) 提出。

**MF2. [共识] Formality 轴 quality-style 混淆严重，"style bias" claim 对该轴偏强。**
GEE 分解显示 formality 的 Originality OR 在多个配置中 ≥ Style OR：
- GPT-4o: Style 2.58 vs Orig 2.32（几乎相等）
- Qwen3 n=355: Style 2.15 vs Orig 4.99（originality 是 style 的 2.3 倍）
- Gemini: Style 1.64 (n.s.!) vs Orig 2.51
- Direction asymmetry（formal-origin 88.9% vs casual-origin 52.6%, Fisher p=0.015）进一步确认

如果 formality 的 Blindspot 本质上是 pairwise 对 quality-style correlation 的放大，而非 Likert 遗漏了 style bias，则论文的核心叙事被削弱约一半。Appendix H stratified analysis 存在 circularity：论文核心 claim 是 Likert 对 style 不敏感，因此用 Likert 等分作为 "质量无差异" 的代理变量存在逻辑矛盾。
- **建议**：在 Abstract/Intro 区分 verbosity（纯 style-driven）和 formality（style + quality confound），不统一称 "style bias"。
- R1 N1 (critical) + R2 W1 (warning)，交叉后两位均认可此问题的重要性。

**MF3. [R2 主张，R1 部分认可] Novelty 定位不足——本质是 Thurstone (1927) 在 LLM judge 领域的实证确认。**
Forced-choice 比 rating scale 灵敏度更高是心理测量学经典结论（Thurstone 1927, Preston & Colman 2000, DeCoster & Iselin 2011），论文自己引用了这些文献。"unquantified" 的声明技术上正确，但核心机制完全可从已有理论预测。增量贡献是 (a) 实证量化 + (b) per-axis confound structure 的 GEE 分解——有价值，但不足以支撑 "demonstrates"/"identifies" 等发现性措辞。
- **建议**：明确定位为 "首次在 LLM judge 下的系统性实证量化"，深度对比 LLM judge 场景是否超越传统理论预测。
- R2 N2 (critical, Excitement 2.5/5)；R1 认为实践意义构成独立贡献（Excitement 3.5/5）。**这是本轮最大分歧点**。

**MF4. [R1 主张] Bootstrap CI vs GEE sandwich SE 在论文中的分工不清晰。**
§4.1 声明 "All bootstrap CIs use 10,000 pair-level resamples"，但 GEE 使用 sandwich standard errors。Table 3 的 CI（Appendix C Table 6）使用哪种方法不明确。如果 GEE 也用 bootstrap，需论证 pair-level resampling 是否保持 cluster 结构。
- **建议**：明确区分 BT bootstrap CI 和 GEE sandwich CI 的适用范围。
- R1 N2 (critical)；R2 未独立提出此问题。

### Should-Fix (warning) — 显著改善论文质量

**SF1. [共识] TOST 等价检验边界 Δ=15pp 偏宽，负控制说服力有限。**
Claude 的 TOST 在 Δ=15pp 时 p<0.05，但 GPT-4o formality 检测到的 bias 为 BT 63.0%（即 13pp），与 Δ=15pp 仅差 2pp。Claude 可能存在 moderate bias 但低于检测阈值。且仅一个负控制模型。
- **建议**：报告 Δ=10pp, 5pp 的 TOST 结果；承认 Δ=15pp 是 power 限制下的妥协。

**SF2. [共识] 跨 benchmark 覆盖稀疏。**
AlpacaEval 仅 3 配置，MT-Bench 仅 2 配置；verbosity（最强轴）仅在 AlpacaEval 有 1 个 cross-benchmark 数据点且为 ‡（非 Blindspot）。"three benchmarks" 声明名义上成立但实际覆盖很低。Llama-70B 和 Gemini 无 cross-benchmark 验证。

**SF3. [共识] 3 个风格轴不足以支撑 "framework" 泛化。**
第四轴（tone）因 NLI gate 拒绝率过高放弃，表明适用性受限于 content-preserving style axes。
- **建议**：软化为 "methodology for content-preserving style axes"。

**SF4. [R2 主张，R1 同意] Register 轴 evaluator-producer overlap 严重且无跨改写器验证。**
Register 所有改写用 Qwen3-32B，BT 结果也较弱（Qwen3 n.s.）。
- **建议**：降级为 "exploratory pilot axis"。

**SF5. [R1 主张] 人工标注验证规模偏小，inter-annotator agreement 仅 moderate。**
50 对，κ=0.44 (moderate)。4 个标注分歧全在 verbosity condensation 对上——正是最强 claim 的支撑轴。Wilson CI [86.7%, 100%] 和 [65.3%, 93.6%] 精度估计不够精确。
- **建议**：增加标注量（≥100 对）或第三名标注员。

**SF6. [R1 主张] Cross-axis contamination: formality→verbosity word count shift d=−0.23 超过论文自设 negligible 标准 (d<0.20)。**
dataset-level 对称不等于 pair-level 对称。
- **建议**：在 pair level 验证 word count 变化与 BT outcome 的相关性，或在 GEE 中加入 word count covariate。

### Minor (info)

- M1: Abstract 数字密度过高，建议保留 1-2 个最有力数字 [R2]
- M2: Introduction 开头单实例 caveat 应前置 [R2]
- M3: 对 RATE 的批评措辞可更委婉 [R2]
- M4: Figure 2 DAG 橙色 dashed arrow 字号过小 + 色盲可访问性 [R2 + 视觉审查]
- M5: Table 1 五种标记系统（†, ‡, †_e, †_c, ---）认知负担高 [R1 + R2]
- M6: Limitations 约 1.5 页可适当精简 [R2]
- M7: Figure 4 caption "Detection probability at observed effect magnitudes" 可能被误读为 post-hoc power [R1]
- M8: §4.1 脚注 3（IIA）篇幅长（~60 words），建议移至 Appendix [R1]
- M9: Register 正文定位不够清晰，Table 1 占 6 行但 §5.3 仅一句话 [R1]
- M10: 100-point Likert 仅选 Qwen3-32B 而非无 overlap 的 GPT-4o，选择理由缺失 [R1]

---

## Reviewer Consensus [AGREE]

1. **Formality 轴 quality confound 削弱 "style bias" 叙事**——两位独立提出，交叉后均确认。核心共识：pairwise 检测到的 formality "bias" 有相当部分是 quality-formality 相关性的反映。
2. **TOST Δ=15pp 偏宽**——两位独立提出，交叉后一致。GPT-4o 最小 bias (13pp) 与 Δ (15pp) 几乎重叠。
3. **Verbosity 轴证据令人信服**——两位一致肯定。Style OR 8–13, cross-rewriter validated, 4 judges consistent。
4. **统计方法论高标准**——两位一致肯定。七种方法 sensitivity hierarchy、Holm-Bonferroni、GEE 诊断完整。
5. **跨 benchmark 覆盖稀疏**——两位一致。verbosity 仅 1 个 cross-benchmark 数据点。
6. **因果声明克制性值得肯定**——两位一致。§3.5 的 disclaimer 在该领域少见。
7. **Register 应降级为 exploratory pilot**——两位一致。evaluator-producer overlap + BT 结果弱。

## Reviewer Divergence [分歧]

1. **Novelty/Excitement [最大分歧]**：R1 (3.5/5) 认为 Likert Blindspot 对 RLHF/DPO pipeline 有直接 actionable implications，sensitivity hierarchy 是有价值的方法论贡献；R2 (2.5/5) 认为核心发现是 Thurstone 经典结论的领域迁移，非新发现。**两位均认可 GEE per-axis decomposition 是增量贡献。**
2. **Bootstrap/GEE CI 问题**：R1 列为 Must-Fix (critical)，R2 未独立提出。这是一个技术清晰性问题而非方法论错误。

---

## Questions (供作者回应)

**Q1 [R1]**: Appendix H stratified analysis 用 Likert 等分作为 "无质量差异" 代理——如何排除 circularity？是否考虑过使用外部质量指标（如人工评分或参考答案匹配度）？

**Q2 [R1]**: Formality 轴 Qwen3 n=355 的 GEE 显示 Orig OR (4.99) 是 Style OR (2.15) 的 2.3 倍，"formality bias" 表述是否仍恰当？

**Q3 [R1]**: TOST Δ=15pp 的选择基准是 SESOI 估计还是 power-driven？如果后者，论文是否应报告基于 SESOI 的 Δ？

**Q4 [R1]**: Verbosity direction-aware NLI gate 恢复的 21 对在 Likert 质量分和 NLI 分数分布上是否与 bidirectional-pass 对系统不同？

**Q5 [R1]**: 论文声称对 RLHF/DPO pipeline 有启示，但未给出下游影响实证。是否有初步实验？

---

## Missing References

**R2 建议（需验证真实性）**：
1. Carterette et al. (2008) — forced-choice vs. graded relevance 灵敏度差异（ECIR）
2. Sedoc & Ungar (2020) — IRT 应用于 chatbot 评估（ACL）
3. Deutsch et al. (2023) — tie 处理对评估指标灵敏度的影响（EMNLP）

**R1 建议**：
4. Stureborg et al. (2024) — LLM judge calibration（论文 §2 已引用 Stureborg et al. 2024 关于 inconsistency，但 calibration 角度未充分覆盖）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置未启用）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（7 项 info，0 critical，0 warning）：
- Figure 1 pipeline 流程图内部标注文字偏小，caption 偏简略
- Table 1 脚注字号非常小（~6pt），包含重要符号说明
- Limitations 章节 ~1.5 页，内容为实质性讨论，应合规
- Figure 2 DAG 色盲可访问性需注意
- Appendix 共 19 小节、~15 张表格，体量庞大但格式规范

**格式合规确认**：正文 ≤8 页 ✓，ACL 模板 ✓，double-blind 匿名 ✓，Limitations 不计入页数 ✓。

---

## Overall Assessment

### 官方维度打分（加权合成）

| 维度 | R1 | R2 | 合成 |
|------|-----|-----|------|
| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |
| Excitement | 3.5/5 | 2.5/5 | **3.0/5** |
| Reproducibility | 4/5 | 4/5 | **4.0/5** |

### Overall: **3.0 (Findings)**

**推荐理由**：
- Verbosity 轴的证据链完整且令人信服（Style OR 8–13, 4 judges consistent）
- 统计方法论严谨，在 LLM judge 评估文献中属高标准
- GEE per-axis confound decomposition 有方法论增量贡献
- 对从业者（RLHF/DPO pipeline）有 actionable implications

**限制评分的核心因素**：
1. **Novelty 不足**：核心发现（forced-choice 灵敏度高于 rating scale）是心理测量学经典结论的领域迁移确认。增量贡献（实证量化 + GEE 分解）有价值但不足以达到主会议水平。[R2 主张，两位在 GEE 增量贡献上达成共识]
2. **Formality 轴 quality confound**：论文的两个 primary axes 之一（formality）受 quality-style confound 严重影响，削弱了 "hidden style bias" 统一叙事。[两位共识]
3. **Detection vs. amplification 核心歧义**：标题和 framing 隐式预设 pairwise 为 ground truth，但论文自身承认无法区分 measurement attenuation、pairwise amplification 和 construct divergence。[两位共识]
4. **负控制说服力有限**：TOST Δ=15pp 与 GPT-4o formality 最小 bias (13pp) 几乎重叠；仅一个负控制模型。[两位共识]

**上调至 3.5 (Borderline Conference) 的条件**：
如果作者在 rebuttal 中能 (1) 调整标题和 framing 为更中性表述；(2) 区分 formality claim 和 verbosity claim 的措辞强度；(3) 澄清 GEE CI 方法；(4) 深度论证 LLM judge 场景对 Thurstone 理论的超越——Director 愿意上调。

**上调至 4.0 (Conference) 的条件（更高门槛）**：
除上述条件外，还需 (5) 报告 TOST multi-Δ sensitivity；(6) 增加人工标注规模或提供 circularity 替代验证；(7) 增强 cross-benchmark 覆盖（尤其 verbosity）。

---

## Detailed Comments

### §1 Introduction
- 开头 formality 实例有效但需前置 caveat（formality preferences 可能反映 legitimate quality judgments——§1 第二段已有，但应更早出现）
- "no single framework integrates..." 的 gap statement 可能被视为 straw man——各工具解决的问题不同

### §3 Method
- §3.1 style-controlled rewriting 描述清晰
- §3.2 NLI gate 设计合理；direction-aware verbosity 处理有理论依据
- §3.3 measurement protocol 完整
- §3.5 因果声明克制——"controlled refers to experimentally controlled rewriting, not formal causal identification" 是重要的诚实声明

### §4 Experiments
- §4.1 统计框架严谨：primary/exploratory/confirmatory 三分法、Holm-Bonferroni 校正、BT 正则化和 bootstrap 参数明确
- Table 1 信息量大但认知负担高（5 种标记系统）
- Table 2 sensitivity hierarchy 是有价值的方法论贡献

### §5 Analysis
- §5.1 Likert Blindspot 描述清晰，n=355 scaled replication 有力区分 attenuation vs power
- §5.2 GEE decomposition 对 verbosity 令人信服；对 formality 的结果反而削弱 "bias" 叙事（Orig OR ≥ Style OR 多配置）
- §5.3 Cross-judge replication 强，但 cross-benchmark 覆盖稀疏
- §5.4 六项放大控制设计周全；人工标注 50 对规模偏小（κ=0.44）

### §6 Conclusion
- 双发现结构清晰
- "systematically misses" 需 hedge——不能排除 power 解释和 construct divergence

### Limitations
- 坦诚全面，覆盖 quality-style confounding、evaluator-producer overlap、scope、ecological validity、scale design
- 篇幅偏长（~1.5 页），可适当精简
- 建议补充 cross-axis contamination d=−0.23 的讨论