---
round: 9
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T17:54:23.174720+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — Round 9 (Fresh Review)

**论文**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)
**Reviewer 编排**: R1（方法严谨性 + 实验有效性）、R2（新颖性 + 完整性）
**审稿模式**: Fresh（无上轮记忆）
**交叉回应**: 完成，关键问题全部达成共识

---

## Summary

本文通过 matched-pair 实验设计，在 τ²-bench 上测量六类 policy ambiguity 对 LLM agent 安全违规的因果影响。构建 300 对条款（ambiguous vs. unambiguous），覆盖六类型双层歧义分类体系，在 5 个模型上运行 2,997 episodes，并在额外 2 个模型上做 replication。核心发现：(C1) 歧义条款使违规率增加 34.0 pp (OR=15.1)；(C2) 类型间存在显著层次结构 (Cramér's V=0.137)，呈两层模式；(C3) specification vs. linguistic 层级区分不显著（inconclusive）；(C4, exploratory) model×type 交互显著但解释方差仅 2.9%。论文还报告了 "Ambiguity Blindness"（<11% disambiguation awareness）和三种 type-specific failure mechanisms。

---

## Strengths

**S1. 因果设计是该领域首创。** Matched-pair design + perturbation control (Δ_perturb = −0.67 pp, CI containing zero) 在 agent safety 文献中首次建立了 policy ambiguity → safety violation 的因果关系。DRIP-R 做相关分析，PolicyBank 做迭代改进，本文是第一个因果推断工作。7 个模型跨 6 个 provider 的 replication 进一步增强外部效度。[R1-S1, R2-S1, 共识]

**S2. Confound 处理和透明度出色。** Incompleteness 的 information-addition confound 在 §3（taxonomy 定义）就主动指出，§5.2 讨论，Appendix F/H 提供 logistic regression 控制 (p=0.022, coefficient change <8%) 和 coreferential confound-free lower bound (31.6%)。TOST sensitivity across 7 margins、bootstrap cluster analysis、clause-level LOO variance、severity threshold comparison 构成多角度 robustness 检验。[R1-S2/S4, R2-S2, 共识]

**S3. Claims 标注层次清晰。** C1 (primary, well-supported) → C2 (primary, with caveats) → C3 (inconclusive) → C4 (exploratory) 的递进标注避免了 overclaim，C3 如实报告为 inconclusive 是良好科学实践。[R1-S3, R2-S4, 共识]

**S4. Type > Model 的方差分解有实际价值。** Type 解释 22.4% variance vs. model 仅 1.0%，意味着 policy auditing 应以 type 为导向而非 model 为导向。Detection experiment (binary F1=0.81) 和 mitigation experiment 展示了 pipeline 原型。[R1-S5, R2-S3, 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. Taxonomy 将 ambiguity、vagueness、incompleteness、normative conflict 混为一谈。** [R2 raised, R1 AGREE with qualification]

六类型中三个不严格属于 ambiguity：authorization scope 是 vagueness (Kennedy 2007)，incompleteness 是 information absence（论文自身承认 "resolution requires adding new policy content"），conditional precedence 是 normative conflict（每条规则本身无歧义）。Wasow (2005) 的操作性定义虽将 vagueness 纳入范畴，但 incompleteness 和 conditional precedence 不在该定义的自然覆盖范围内。

如果最高违规率的 type (incompleteness, 53.6%) 不严格属于 ambiguity，"ambiguity type predicts severity" 的核心 framing 存在理论张力。

两位 Reviewer 共识的修改方向：保留 ambiguity framing，但 §3 需增加 "Scope of 'ambiguity'" 段落，正面讨论理论边界，承认 incompleteness 和 conditional precedence 处于定义边界，明确论证为何 operational/inclusive 定义在 LLM agent 场景下合理。

**N2. Differential Nocuity 框架的增量贡献不清晰。** [R2 raised, R1 AGREE]

框架声称 risk = f(ambiguity type, safety training, disambiguation channel availability)。但：
- "LLM agents 缺乏 disambiguation channels → 所有 ambiguity 都 nocuous" 是 Berry & Kamsties (2004) 的直接推论
- 三因素中仅 "ambiguity type" 有 C1+C2 充分支撑；"safety training" 基于 [Exploratory] C4 + κ=0.385 的 authorization scope；"disambiguation channel" 基于可能反映 uninstructedness 的 <11% awareness
- P1/P2 predictions 是 post-hoc rationalization，P1 支持证据 (Appendix B: auth scope −18.0 vs incompleteness −3.4) 无 formal statistical test

两位 Reviewer 共识：将 Differential Nocuity 从 contribution 降级为 Discussion 中的 interpretive lens，或展示 non-obvious testable predictions with adequate statistical support。

**N3. SESOI ±15 pp 缺乏外部锚定。** [R1 raised as MUST-FIX, R2 AGREE but suggests SHOULD-FIX]

±15 pp 的理由是主观的 deployment-relevance 判断和 perturbation control bound 的 2× 倍数（循环论证）。±10 pp 时仅 3/6 mid-tier pairs 等价 (Table 2)，TOST power 降至 0.57。Bootstrap cluster AU p-value = 0.47 表明 incompleteness singleton 边界不尖锐。

**Reviewer 分歧**：R1 认为 MUST-FIX，R2 认为论文已有 partial mitigation（sensitivity analysis + bootstrap cluster 作为 margin-free 补充；incompleteness upper bound 在所有 margin 下成立），建议降为 SHOULD-FIX。

Director 判断：incompleteness 作为 upper bound 的核心 finding 稳健，但 mid-tier clustering 对 margin 敏感。需要外部锚定和更显著的 sensitivity 呈现，但不 invalidate C2 整体。严重程度介于两位 Reviewer 判断之间。

**N4. Authorization scope κ=0.385 下 C4 结论可信度不足。** [R1 raised, R2 AGREE]

Cross-judge κ=0.385 仅为 fair agreement，human-LLM κ=0.644 CI=[0.35, 0.91] lower bound 极低。然而 C4 Discussion 从这个 noisy measurement 推导出 safety training differential mitigation 叙事。Within-judge bootstrap (99.5%) 不能排除 judge-level systematic bias。Introduction contribution (2) 和 Abstract 中的表述与正文 "suggestive" hedging 不匹配。

两位 Reviewer 共识：52 pp range 应标注为 "upper bound on true between-model variance"；Abstract 需附带 measurement uncertainty qualification。此问题与 N1 (taxonomy 混淆) 互相加强——authorization scope 同时存在理论定义争议和测量可靠性问题。

### Should-Fix（影响评分但不一票否决）

**W1. "Ambiguity Blindness" framing 过度。** [R1-W4 + R2-W5, 共识]

<11% awareness 反映 uninstructed default behavior 而非 inability。Mitigation experiment −8.5 pp 改善直接反驳 blindness framing（agents CAN respond when prompted）。人类也默认采用 good-enough single parse (Ferreira 2002)。建议改为 "lack of externalized disambiguation"。

**W2. Abstract 信息过载。** [R2-W1, R1 AGREE]

OR、V、κ、p-values、logistic regression coefficient change 等大量数字淹没核心 message。建议精简为 problem→approach→2-3 key findings→implication 结构。

**W3. C3 layer distinction 与 taxonomy 组织原则的逻辑张力。** [R2-W2, R1 AGREE with qualification]

C3 未通过 Holm-Bonferroni 校正但 taxonomy 仍以 linguistic/specification layer 为组织原则。R1 认为保留 layer 但标注为 hypothesis 是更好的方案（比 flat six-type 更有信息量）。建议 §3 末和 §5.3 明确 "layer distinction is a theoretical hypothesis, not an empirical finding"。

**W4. Token count 作为 information content proxy 未验证。** [R1-W1, R2 AGREE]

Logistic regression 使用 token count difference 作为 information content 代理变量，未讨论 content validity 或尝试替代度量。R2 指出 partial mitigation: coefficient change <8% 限制了 proxy 不完美性的影响。

**W5. Human validation 样本偏小，per-type CI 极宽。** [R1-W2, R2 AGREE]

100/2997 (3.3%)，per-type n=32-34，scopal CI [0.00, 1.00] 本质上 uninformative。§4.4 正文呈现过于乐观（强调 pooled κ=0.733 而淡化 per-type 不稳定性）。

**W6. Cross-provider ICC 缺乏直接度量。** [R1-W3, R2 AGREE]

ICC=0.919 仅 within OpenAI family。LLaMA Δ=+20 pp 远小于主研究 range (+25.7–39.0 pp)，暗示跨 provider effect 可能受 baseline instruction-following quality 调节。

**W7. 多重比较校正 "three test families" 未定义。** [R1-W5, R2 AGREE]

§4.6 未列出成员，读者无法验证校正适当性。

**W8. 与 DRIP-R 的 type-level 映射缺失。** [R2-W3, R1 AGREE]

DRIP-R 有 5 个 RE ambiguity types，本文 6 个，未提供显式映射。

**W9. Coreferential 被系统性排除在 3 个 follow-up 分析之外。** [R2-W4, R1 AGREE with qualification]

Detection 和 replication 排除有技术合理性（lexically identical variants），但 mitigation 排除理由缺失（Appendix B caption 为循环解释）。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：
- R1-N2 / R2 auth scope κ 问题 → C4 narrative 需 heavily caveat
- R2-N2 / R1 Differential Nocuity 增量 → 应降级为 interpretive lens
- Ambiguity Blindness → 应改为 lack of externalized disambiguation
- Abstract 信息过载 → 需重构叙事
- 多重比较校正不透明 → 需显式列出 test families
- DRIP-R mapping 缺失 → 需补充
- Coreferential exclusion → mitigation 排除理由需补充

## Reviewer Divergence

| 问题 | R1 | R2 | Director 判断 |
|------|-----|-----|--------------|
| N3 SESOI severity | MUST-FIX | SHOULD-FIX (partial mitigation) | 介于两者之间：mid-tier clustering 确实 margin-sensitive，但 incompleteness upper bound 稳健 |
| N1 Taxonomy: 修改方案 | Option (b): 保留 framing + 讨论张力 | Option (a) preferred: reframe to "policy specification defects" | 倾向 R1 方案：保留 ambiguity framing + 正面讨论理论张力，成本更低且可行 |
| W3 C3 layer: 修改方案 | 保留 layer 作为 hypothesis | 改为 flat six-type | 倾向 R1：保留 layer 但明确标注为 hypothesis |

---

## Questions for Authors

1. **[高优先级]** §3 Taxonomy: 如何回应 authorization scope = vagueness、incompleteness = information absence、conditional precedence = normative conflict 的理论质疑？是否愿意增加 "Scope of 'ambiguity'" 段落正面讨论？
2. **[高优先级]** Differential Nocuity 框架中，P1 (auth scope −18.0 vs incompleteness −3.4 pp) 是否经过 formal statistical test？如果没有，Discussion 中 "mitigation experiment supports P1" 的 claim 是否应弱化？
3. **[高优先级]** 如果使用 ±10 pp 作为 SESOI，C2 narrative 如何调整？mid-tier 变为 three-tier 结构是否影响核心结论？
4. 移除 3 个 specification-layer types 后，仅用 linguistic types 的 C1/C2 是否仍然成立？
5. Clause pairs 的 template-based pipeline 具体使用多少 templates per type？template 结构如何影响 clause-level variance？
6. 是否尝试过在 system prompt 中要求 agents flag ambiguity？如果有，awareness rate 从 4.6% 提升到多少？
7. Claude auth scope 12% vs GPT-5.4 64% — 两者均由 GPT-5.4 judge 评估，排除了 judge identity confound。但 κ=0.385 下 per-episode 噪声大——52 pp range 中真实 model difference 占比多少？

---

## Missing References

两位 Reviewer 共同建议：
- **Zheng et al. (2024)** "Judging LLM-as-a-Judge" — 与 §4.4 cross-judge design 直接相关 [已引用，确认]
- **Anvari & Lakens (2021)** — TOST SESOI 选择的方法论文献 [已引用，确认]

R1 建议：
- Tamkin et al. (2023) — policy-governed decision-making
- Pan et al. (2024) — LLM ambiguity following behavior
- Karpinska & Iyyer (2023) — LLM contextual ambiguity processing

R2 建议：
- SafeAgentBench (Yin et al., 2025) — embodied agent safety
- AgentHarm (Andriushchenko et al., 2024) — agent misuse benchmark
- Deontic logic / normative conflict literature (Prakken & Sartor) — conditional precedence 理论基础

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2 warnings, 9 info）。主要发现：

- **[Warning]** Pages 3-5 连续 3 页纯文本（Related Work → Taxonomy → Method），无任何 display item。Section 3 描述六类型分类体系但缺少对应的分类表格或树形图。建议增加 taxonomy 可视化。
- **[Warning]** Page 8（Discussion + Conclusion）为纯文本密集页，与 pages 6-7 的 figure/table 密集形成反差，整体节奏 "前松后紧再松"。
- **[Info]** Figure 1 内部标注字体偏小，打印时可能不可读。
- **[Info]** 主文 8 页内 4 个 display items (3 figure + 1 table)，对实证论文偏少（通常 5-8 个）。
- **[Info]** Table 1 格式规范（booktabs），Figure 2/3 颜色区分度良好。
- **[Info]** Limitations 篇幅适当，参考文献格式统一无未解析引用。

---

## Overall Assessment

**评分: 3.5 — Borderline Conference**

**置信度: 4/5**（两位 Reviewer 分别熟悉因果推断/agent safety 和 CL ambiguity/RE 文献）

**理由**：

实验执行达到 conference 标准：matched-pair causal design 是 agent safety 领域首创，C1 (+34 pp, OR=15.1) 因果效应在 7 个模型上 replicated，统计方法严谨透明，confound 处理和 claims 标注层次清晰。Type > Model 的方差分解 (22:1) 有直接部署指导意义。

但概念框架存在根本性张力：(1) taxonomy 将 ambiguity、vagueness、information absence、normative conflict 混为一谈，核心 framing "ambiguity type predicts severity" 的理论基础被削弱；(2) Differential Nocuity 框架的增量贡献有限，本质是既有理论在 LLM 场景下的直接推论加上 exploratory 实验发现的包装；(3) authorization scope 同时存在理论定义争议 (vagueness) 和测量可靠性问题 (κ=0.385)，使得关于该 type 的所有 claim 都需 heavily caveat。

修复路径明确：(a) §3 正面讨论 taxonomy 理论边界、(b) Differential Nocuity 降级为 interpretive lens、(c) C4 auth scope narrative 加入 measurement uncertainty caveat、(d) Ambiguity Blindness 改为 lack of externalized disambiguation、(e) Abstract 精简叙事。这些修改在 rebuttal/revision 周期内可完成。

**评分对标 (EMNLP 2026 ARR)**：
- 3.5 = Borderline Conference：实验贡献 (C1) 达到 conference 水准，但 framing/framework 问题使整体 novelty 受限。若 rebuttal 能有效 address taxonomy 理论张力和 framework positioning，可上调至 4.0 (Conference)。

---

## Detailed Comments

### §1 Introduction
- Contribution (1) "replicated across seven models" 应明确区分 main study (5 models) vs. replication (2 models)
- Contribution (2) 将 Differential Nocuity 列为框架贡献——如降级为 interpretive lens，需重写

### §2 Related Work
- 缺少与 DRIP-R 的 type-level 映射
- 建议增引：SafeAgentBench, AgentHarm, deontic logic 文献

### §3 Taxonomy
- 需增加 "Scope of 'ambiguity'" 段落讨论 ambiguity/vagueness/incompleteness/normative conflict 边界
- 末尾应声明 layer distinction 是 theoretical hypothesis
- 视觉审查建议增加 taxonomy 可视化（表格或树形图）以改善 pages 3-5 的视觉节奏

### §4 Method
- §4.2 "template-based pipeline" 未描述 template 结构和数量
- §4.4 Human validation: 正文应更显著呈现 per-type CI 宽度（scopal [0.00, 1.00]）
- §4.5 ICC 应计算跨 provider concordance（Kendall's W）作为补充
- §4.6 "three test families" 需显式列出成员；"stabilizes at ±15 pp" 措辞应更中性
- §4.6 SESOI 需外部锚定（deployment SLA、行业 benchmark）

### §5 Results
- §5.2 C2: 应在正文讨论 ±10 pp 下的替代 narrative（three-tier 而非 two-tier）
- §5.3 C3: 应强化 "layer distinction 是 hypothesis" 的表述
- §5.4 C4: auth scope "most model-differentiating type" 应附带 "upper bound on true variance" caveat；F(20)=1.97 补充 denominator df
- §5.4: Abstract "52 pp" 需 measurement uncertainty qualification

### §6 Analysis
- §6.1: Gwet's AC₁ vs Cohen's κ 差异应在正文解释 prevalence paradox
- §6.2: "Ambiguity Blindness" 改为 "lack of externalized disambiguation"；讨论 uninstructed vs blind 区分

### §7 Discussion
- Differential Nocuity: 降级为 interpretive lens 或加强 non-obvious predictions
- P1 "supports P1" claim 需 formal statistical test 或弱化措辞
- 视觉审查建议增加视觉元素以缓解纯文本密集

### Appendix B (Mitigation)
- 补充 coreferential 排除的理由
- auth scope −18.0 vs incompleteness −3.4 的差异需 formal test

### Appendix D (Detection)
- Coreferential 排除理由合理（lexically identical）

### Appendix E (Replication)
- LLaMA unambiguous baseline 17.6% 异常高，应讨论原因

### Bib
- ferrari_defects_2018: 核实第一作者（Rosadini vs Ferrari）
- navigli_wsd_2009: 核实年份（2009 vs 2015）

### 格式
- 正文 ≤ 8 页 ✅
- Double-blind ✅
- ACL 模板 ✅
- Limitations ✅
- 0 orphan bib ✅
- Data and Code Availability ✅
