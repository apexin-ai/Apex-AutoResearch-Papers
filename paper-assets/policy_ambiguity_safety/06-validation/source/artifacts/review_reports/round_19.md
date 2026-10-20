---
round: 19
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T01:54:31.919534+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

## 审稿报告 — Round 19 (Fresh Review)

**论文**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
**Venue**: EMNLP 2026 via ARR May cycle (Long Paper)
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）
**审稿模式**: Fresh（重新审稿，无上轮记忆）
**交叉分享**: 完成，关键问题达成共识，无需 Round 2

---

## Summary

本文研究 LLM agent 在含歧义自然语言政策下的安全行为。在 τ²-bench 上构建 300 matched clause pairs（6 种歧义类型），跨 5 个模型生成 ~3,000 episodes。主要发现：(1) 歧义子句使违规率增加 34.0pp（conditional OR=15.1）；(2) 子句措辞解释 22.4% 方差 vs 类型仅 0.4%，但类型预测失败机制的能力是预测违规率的 17 倍（NMI ratio ≈ 17）；(3) incompleteness 是持续最高风险类型（46-62%），coreferential 为下界（31.6%）；(4) disambiguation neglect 普遍存在（≤11% awareness），41.3% 的子句触发跨模型收敛违规。论文配备 perturbation control、cross-judge validation（3 family, Fleiss' κ=0.717）、2 additional replication models 和 SOPBench cross-benchmark 验证。

---

## Strengths

**S1. 严格的匹配对因果设计**
Matched-pair 设计是建立因果关系的 gold standard。在同一 model-judge pairing 内比较每个 clause 的歧义/非歧义变体，有效控制了 judge bias 和 model baseline。Perturbation control（300 episodes, Δ=-0.67pp, CI containing zero）进一步隔离了语义歧义效应。[R1-S1, R2-S1, 共识]

**S2. 全面且恰当的统计工具箱**
McNemar's test、TOST equivalence testing（7 margins sensitivity）、Type III SS 方差分解、permutation test、bootstrap 聚类、logistic regression confound control、ICC replication、Holm-Bonferroni 校正、互信息分析——统计方法选择出色且覆盖全面。[R1-S2, R2-S5, 共识]

**S3. 多层验证架构**
Cross-judge（3 judge 家族, Fleiss' κ=0.717）、human validation（κ=0.798 inter-annotator）、model replication（7 模型跨 6 provider）、cross-benchmark（SOPBench）、perturbation control——多层验证在 NLP 实证研究中不常见。[R1-S3, 共识]

**S4. 诚实且精准的 claim calibration**
C3 标记为 inconclusive；auth scope cross-judge discordance 完整报告；incompleteness 标注为 confounded upper bound；60.8% 残差方差详细讨论。论文对自身弱点的透明度很高。[R1-S4, R2-S4, 共识]

**S5. "Type predicts mechanism, not risk" 的核心洞察**
NMI 分析（type → mechanism 17× > type → violation rate）将 taxonomy 从 risk predictor 重新定位为 diagnostic tool，既诚实又有实际价值。[R1-S5, R2-S3, 共识]

**S6. Variance decomposition 视角新颖**
22.4% clause vs 0.4% type 的发现是一个重要的"负面结果"——表明 type-level 分类不应用于 risk prediction，真正的风险来源在于 individual clause wording。[R2-S2, 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. 合成歧义子句的生态效度不足** [R1-N1, R2 同意]
300 clause pairs 通过 template-based pipeline 生成。Appendix R 示例显示部分歧义变体更接近"严重措辞不当"而非真实世界细微歧义——incompleteness 示例将多个具体参数全部替换为模糊词（"large", "appropriate", "timely"），这种程度在实际政策文档中罕见。Post-hoc realism validation 仅验证词汇风格一致性，未验证歧义程度和分布的自然性；τ²-bench 本身政策也是合成的。SOPBench 效应量衰减至 37%（+12.6 vs +34.0pp）间接支持效应量被高估的判断。这是全文所有 claim 的外部效度基础——如果合成歧义程度系统性偏高，34.0pp 效应量可能高估真实场景影响。
- **建议**：(1) Limitations 中更显著承认效应量为合成条件下的 upper bound；(2) Discussion/Abstract 中将 +34.0pp 定位为 "upper bound under controlled synthetic conditions" 而非部署预期；(3) 未来工作考虑 dose-response 或真实政策对照。

**N2. Taxonomy 将非歧义现象纳入 "ambiguity" 标签，标题过度概括** [R2-N1, R1 部分同意]
§3 明确承认 incompleteness（信息缺失）和 conditional precedence（规范冲突）不属于 linguistic ambiguity，但标题仍为 "Policy Ambiguity Is Nocuous"，且最强效应 (+49.2pp) 来自公认的非歧义类型。更关键的是，§3 用 "behaviorally indistinguishable" 作为统一归类依据，但 §6.1 恰恰展示了不同 type 有不同 dominant failure mechanisms（structural misparse / gap-filling / boundary violation）——这构成内部矛盾。排除 incompleteness 后 pooled effect 仍为 +31.0pp（Appendix Q），confound-free range 为 +18.7 to +36.0pp，表明 genuine ambiguity 效应仍然显著。
- **建议**：(1) 标题扩展为包含 underspecification（如 "Policy Ambiguity and Underspecification..."）；或 (2) 将 confound-free range 提升为 primary result（R1 倾向此方案）；(3) 消除 "behaviorally indistinguishable" 与 §6.1 distinct failure mechanisms 的矛盾——改用 "produce comparable safety impact" 的 pragmatic framing。

**N3. Authorization scope 度量不可靠（κ=0.385），但相关 claims 未充分降级** [R1-W1 + R2-N2, 共识]
Auth scope 的 cross-judge binary κ=0.385 低于 "fair" 门槛，是六种类型最低。Cross-judge-group type ranking ρ=0.09（p=0.87）完全由 auth scope rank reversal 驱动。然而 §5.4 仍将其描述为 "most model-differentiating type (52pp range)"，Figure 3 caption 未标注可靠性信息。R1 认为 post-hoc 排除 auth scope 有构成性依据（模型组成差异，非 judge bias），且三家族验证（ρ=0.71-0.89）提供独立证据，因此 C2 并非完全不稳健；R2 认为 post-hoc 排除有 cherry-picking 风险。双方一致认为 "robust extremes only" 的 framing 应更显著。
- **建议**：(1) Figure 3 caption 标注 auth scope κ 值；(2) §5.4 "most model-differentiating" 改为条件性表述（"if confirmed by more reliable measurement"）；(3) Abstract 使用 "partial ordering with robust extremes" 而非暗示完整排序。

### Should-Fix（影响评分但不一票否决）

**W1. Confound-free range 在 Abstract/Conclusion 不可见** [R2-W1 + R1-W2, 共识]
+34.0pp（含 confounded incompleteness）在 Abstract、Introduction、Conclusion 反复出现，但 confound-free range（+18.7 to +36.0pp）仅在 §5.1 末尾。读者极可能只记住 +34.0pp 而忽略 confound caveat。
- **建议**：Abstract 中 "+34.0 percentage points" 之后立即加入 confound-free range。

**W2. SOPBench replication framing 过于乐观** [R1-W3, R2 同意]
效应量衰减 63%（+12.6 vs +34.0pp），5 模型中仅 3 个 p<0.01（GPT-5.4 borderline p=0.052, DeepSeek 不显著 p=0.163）。"Directional consistency across all five models" 的表述过于宽泛。
- **建议**：报告 pooled CI；将 "confirms" 改为 "suggests"；说明 2/5 不显著。

**W3. 60.8% 残差方差的实践含义讨论不足** [R1-W4, R2 部分同意]
~46% systematic-but-unmeasured 是最大单一方差成分，但 Discussion 对此仅一句带过。Clause-level auditing 仅覆盖 22.4%——是可操作最大因素但非最大因素。
- **建议**：Discussion 补充方差分布全景图；明确 auditing 的上限。

**W4. Type III SS 方法论需正文级说明** [R1-W5, R2 同意]
22.4% 来自 Type III SS on binary outcomes（LPM 近似），在 unambiguous 6.9% violation rate 下近似质量较差。Logistic regression Tjur's R²=0.175 作为对照在脚注中提及，但未报告 clause identity 的 partial R²。
- **建议**：正文讨论 LPM vs logistic 差异；补充 logistic partial R²；确认 clause >> type ordering 在两种 framework 下一致。

**W5. §6 Error Analysis / Disambiguation neglect 的 novelty 未充分展开** [R2-W3+W4, R1 部分同意]
Error Analysis 是三个 contribution 之一但每个 failure mechanism 仅 1-2 句。Disambiguation neglect 的 "neglect vs inability" 关键区分仅一句，mitigation 证据（-8.5pp）完全在 Appendix B。Liu et al. (2023) / Hu et al. (2025) 已证明 ambiguity collapse，本文的增量 novelty（agentic context + irreversible consequences）阐述不清。
- **建议**：§6.2 增加 2-3 句概述 mitigation 结果以支撑 "neglect" 定性；考虑将 C3（inconclusive）移至 Appendix 释放空间。

**W6. 潜在遗漏相关工作** [R2-W5, R1 有条件同意]
(a) "Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges" (arxiv 2605.06161) 关联 cross-judge methodology；(b) "The Causal Impact of Tool Affordance on Safety Alignment" (arxiv 2603.20320) 关联因果分析框架；(c) Specification gaming 文献（Krakovna et al.）与 unintentional misinterpretation 的对比有讨论价值。
- **建议**：检查并在 Related Work 中适当讨论。

**W7. 领域泛化性有限但 Discussion 建议暗示更广适用性** [R2-W2, R1 同意]
Retail vs airline type ranking ρ=0.26，conditional precedence 跨域差异 22pp。Discussion 的 "clause-level auditing" 建议暗示超出数据支持的泛化范围。
- **建议**：Discussion 明确 auditing 建议适用于 customer service 及类似领域。

---

## Reviewer Consensus

以下问题双方达成共识 [AGREE]：
1. **Ecological validity** 是最大外部效度威胁——合成歧义可能系统性偏重，+34.0pp 可能高估真实场景效应
2. **Confound-free range** 必须在 Abstract/Conclusion 更显著——当前 framing 使读者忽略 incompleteness confound
3. **Auth scope κ=0.385** 的 claims 需在正文和图表中更早、更显著地降级
4. **SOPBench "directional consistency"** 表述过于宽泛——2/5 模型不显著
5. **"Behaviorally indistinguishable" 与 §6.1 distinct failure mechanisms** 存在内部矛盾——需统一论证
6. **Type III SS 22.4%** 需要 logistic framework 对照以确认 robustness

## Reviewer Divergence

**N3/R2-N2 (C2 robustness)**：轻度分歧。R1 认为 post-hoc 排除 auth scope 有构成性依据（模型组成差异而非 judge bias），且三家族验证（ρ=0.71-0.89）提供独立证据，因此 C2 "robust extremes" 仍有效；R2 认为 post-hoc 排除有 cherry-picking 风险，C2 作为 primary contribution 价值被削弱。双方均同意 "robust extremes only" 的 framing 应更突出。分歧在程度而非方向。

---

## Questions for Authors

1. 生成 clause pairs 的 template-based pipeline 具体如何操作？每种类型有多少个 template？是否存在某些 template 贡献了不成比例的违规率？
2. 96% initial annotator agreement (287/300) 的 chance-corrected Cohen's κ 是多少？
3. 排除 incompleteness 后五种 type 的 pooled effect size CI？（Appendix Q 报告了 Δ=+31.0pp 但未见 CI）
4. Mitigation 对 incompleteness 几乎无效（-3.3pp vs auth scope -18.0pp），这是否独立证据说明 incompleteness 与 ambiguity 的本质不同——前者需 policy revision 而非 prompt 可解？
5. Temperature=0 下的 disambiguation neglect 是否在 temperature>0 部署环境中发生变化？
6. 是否有 cross-provider ICC 数据？（当前 ICC=0.919 限于 OpenAI family）
7. 300 clause pairs 均匀分配（每 type 50 pairs）——真实 policy 中各 type 的自然分布？

---

## Missing References

- "Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges" (arxiv 2605.06161, May 2026)——关联 cross-judge methodology 和 policy wording 对 judge 行为的影响
- "The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents" (arxiv 2603.20320, March 2026)——方法论可比的因果 agentic safety 研究，需精确定位 "first causal study" 声明范围
- Krakovna et al. specification gaming 文献——与 unintentional misinterpretation 的对比

---

## External Review

外部审稿：未启用。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2 warning + 3 info，无 critical）：

- **[Warning] Pages 4-6**：连续 3 页纯文本（§4 Method 到 §5.2 Results），无 figure/table/equation 穿插，审稿人缺乏视觉锚点。建议将 Table 2 或 Figure 2/3 前移至 Results 开头。
- **[Warning] Page 7**：Table 2 + Figure 2 + Figure 3 三个 display items 挤在同一页，分布极不均匀。建议拆分其中一个 figure 至 page 5-6。
- **[Info]** Figure 2/3 的 axis labels 和 legend 字号约为正文 60%，低于推荐的 70% 阈值。
- **[Info]** Pages 8-9 连续纯文本（§6-§8），§6 failure mode 分析可配小型可视化。
- **[Info]** 主文本仅 2 个 figure，对实证论文偏少；variance decomposition、type-specific failures、cross-judge agreement 均有可视化潜力。

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**
**Confidence: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 4/5 | 3.5/5 | 3.5-4/5 |
| Excitement | 3/5 | 3/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |

这是一篇执行质量很高的实证研究。Matched-pair 因果设计、多层验证架构、全面的 sensitivity analysis 和诚实的 claim calibration 体现了很高的方法论标准。核心发现（ambiguity causes violations, clause > type for risk, type > clause for mechanism）在实验范围内可信。

主要顾虑集中在三个方面：(1) **外部效度**——合成歧义的生态效度不足，效应量可能高估真实场景影响；(2) **术语/framing**——将非歧义现象纳入 "ambiguity" 标签导致标题和核心声明过度概括，且与 §6.1 的 distinct failure mechanisms 存在内部矛盾；(3) **度量稳健性**——auth scope κ=0.385 和 cross-judge type ranking ρ=0.09 削弱 type-level claims。

如果能解决 N1（加强 ecological validity 论证或更审慎定位效应量）、N2（调整 framing/标题以消除内部矛盾）和 N3（auth scope claims 充分降级），本文有潜力达到 Conference 水平（4.0）。当前版本在 Borderline Conference (3.5) 的高端——方法论贡献突出但 novelty（核心发现 "ambiguity is bad" 较为预期）和外部效度不足限制了整体评价。

---

## Detailed Comments

### §1 Introduction
- Opening vignette 有效但 gap statement "no existing study provides a causal, type-granularity mapping from ambiguity to safety violations" 需验证是否有 arxiv 2603.20320 等 concurrent causal studies
- Contribution list 中 "first matched-pair causal study" 需限定范围（"of policy ambiguity's safety impact"）

### §3 Taxonomy
- "Behaviorally indistinguishable" 需修改为更精确的 pragmatic framing——当前与 §6.1 矛盾
- 6 type 的选择标准（"based on frequency in operational policy documents and theoretical distinctiveness"）过于简略，建议补充每个 type 的选择理由

### §4 Method
- 96% annotator agreement 应补充 chance-corrected κ
- Template-based pipeline 细节不足——是否存在 template 效应需要讨论

### §5 Results
- Abstract 和 §5.1 开头应紧跟 confound-free range
- C2 在 Abstract 中应使用 "robust extremes" 而非暗示完整排序
- C3 (inconclusive) 可移至 Appendix 释放正文空间
- SOPBench replication 需更审慎表述

### §6 Error Analysis
- §6.2 Disambiguation neglect 需增加 mitigation 结果概述以支撑 "neglect vs inability"
- §6.1 failure mechanisms 各仅 1-2 句，信息密度可接受但不充分

### §7 Discussion
- "Clause-level auditing targets the largest controllable factor" 应补充方差全景
- Auditing 建议应明确限定 domain 范围

### §8 Conclusion
- 补充 confound-free range
- 泛化声明已 domain-qualified（"customer-service and similar"），这是好的

### Limitations
- 四段覆盖 Scope、Measurement、Confounds、Disambiguation channel，结构合理
- 应更显著承认合成歧义的 effect size transportability 问题

### Appendix
- Appendix R (clause examples) 的极端歧义问题应在正文 Limitations 中讨论
- Detection experiment (Appendix D) 与主论文因果分析关系较弱，但作为 application spin-off 可保留
- Appendix Q (sans incompleteness) 的 +31.0pp 结果应在正文 §5.1 中引用