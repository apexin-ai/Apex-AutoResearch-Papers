---
round: 10
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-21T19:15:47.553327+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 10 (Fresh)

**论文**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 via ARR May cycle (Deadline: 2026-05-25)
**审稿模式**: Fresh（从头初审）
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）
**轮次**: 1 轮初审 + 1 轮交叉回应（关键问题达成共识，无需第二轮）

---

## Summary

本文在 τ²-bench 上构建 300 组 matched clause pairs（6 种歧义类型 × 50 pairs），通过 5 个模型运行 2,997 episodes，因果量化了政策歧义对 LLM agent 安全违规的影响。核心发现：歧义使违规率上升 34.0 pp（OR=15.1），incompleteness 在全部 7 个模型中稳居最高风险类型（≥46%），agents 在 >89% 的情况下展现 "disambiguation deficit"（不识别歧义直接执行）。实验设计采用 matched-pair causal identification + perturbation control，统计方法全面（TOST、bootstrap cluster、Holm-Bonferroni、logistic regression），局限性透明度在同类工作中属上乘。

---

## Strengths

**S1. 严谨的因果实验设计。** Matched-pair design 是本文最大亮点——每组 clause pair 仅做 minimal edit，within-clause 比较有效控制 clause-level 混淆变量。Perturbation control（Δ=-0.67pp, CI 含零）排除表面扰动。Incompleteness 的 information-addition confound 通过 logistic regression + coreferential 下界双重控制。这种 causal identification strategy 在 agent safety 文献中确实少见。[R1-S2, R2-S1 共识]

**S2. 统计方法论全面且透明。** TOST 等价检验 + 7 级 margin 敏感性分析 + margin-free bootstrap cluster analysis（Ward's method, B=10,000）+ Holm-Bonferroni 三 test families + ICC 可复现性验证。SESOI=±15pp 有明确 domain-relevant anchoring 且给出完整敏感性分析。这是近期 agent safety 论文中统计严谨度最高的之一。[R1-S3, R2-S2 共识]

**S3. 诚实报告负面/不确定结果。** C3（layer effect）标注为 inconclusive；authorization scope κ=0.385 在正文和 Limitations 中反复标注；bootstrap AU p-value=0.47 明确报告；incompleteness 标注为 upper bound。这种透明度值得肯定。[R1-S4, R2-S3 共识]

**S4. 跨模型复制增强泛化性。** 7 个模型覆盖 6 个 provider（4 proprietary + 3 open-source），Gemini 和 LLaMA 独立复制。Incompleteness 在全部 7 个模型中 ≥46%。[R1-S5, R2-S4 共识]

**S5. Concurrent work 定位清晰。** 与 DRIP-R（2026）的三点区分具体有说服力，Appendix 的 category mapping 表明作者认真研究了 concurrent work。[R2-S5]

**S6. Failure mode taxonomy 有经验证据支撑。** 614 条 violation traces 编码为三种机制不同的失败模式，与歧义类型形成可解释的对应。Disambiguation Deficit（4.6% overall awareness, Qwen3/DeepSeek 为零）是有实用价值的定量发现。[R1-S6, R1-S7, R2-S6]

---

## Weaknesses

### MUST-FIX

**[MUST-FIX-1] Authorization scope κ=0.385 不足以支撑 C4 中 52pp range 作为核心发现。** [R1-W1 = R2-W5, 两人完全共识]
- Cross-judge κ=0.385 低于 fair agreement 门槛（0.40），human-LLM κ=0.644，CI [0.35, 0.91]。52pp range 中真实模型差异 vs 测量噪声无法分离。
- Abstract 括号注释 "though measured with the lowest inter-judge agreement, κ=0.385" 过于弱化，读者易忽略。Introduction（§1）复述 52pp 时完全无可靠性 caveat。
- **要求**: (1) Abstract 将 auth scope 从主要发现降格为初步发现，明确标注不确定性；(2) Introduction 同等篇幅讨论可靠性限制；(3) C4 分析展示去除 auth scope 后交互效应是否仍显著；(4) 52pp 标记为 upper bound with substantial measurement uncertainty。

**[MUST-FIX-2] Two-tier hierarchy (C2) 的统计稳定性不足以支撑当前表述。** [R2-W1 = R1-W6, 两人完全共识]
- Bootstrap cluster analysis 中 incompleteness singleton 仅在 34.3% 的 samples 中出现，AU p-value=0.47。TOST 在 ±10pp 时仅 3/6 mid-tier pairs 等价（power=0.57）。Kendall's W=0.398（p=0.072）五模型下不显著。
- Abstract 称 "a two-tier type hierarchy separates incompleteness from the remaining five types"，Introduction/Conclusion 同样确定性表述——远超 34.3% bootstrap support。
- **要求**: (1) 措辞弱化为 "incompleteness tends to cluster as the highest-risk type, though the tier boundary is not sharp"；(2) 正文并列呈现 ±10pp（three-tier）与 ±15pp（two-tier）叙事；(3) 考虑将 C2 核心声明缩窄为 "incompleteness is consistently the highest-risk type"（7/7 模型支持）。

### SHOULD-FIX

**[SHOULD-FIX-1] Taxonomy 理论基础需更充分讨论。** [R2-W2, R1 partial REBUT]
- Incompleteness（information absence）和 conditional precedence（normative conflict）不满足 Wasow (2005) 对 ambiguity 的 strict 定义（"multiple distinct interpretations"）。§3 "Scope of 'ambiguity'" 段落已有初步讨论，但 R2 认为不够充分。R1 认为操作性定义可辩护，但同意需扩展讨论。
- **分歧记录**: R2 认为这是根本性概念混淆（行为结果定义输入类型=循环论证），R1 认为操作性定义在实证研究中是标准做法。两人共识是需要更深入的理论讨论，但不必改变 taxonomy 设计。
- **建议**: (1) §3 扩展理论边界讨论，引用 Dalpiaz et al. (2018)；(2) 考虑在标题/abstract 中使用更精确限定。

**[SHOULD-FIX-2] Incompleteness confound 控制仅有粗粒度 proxy。** [R1-W2, R2 AGREE]
- Token count 是 coarse proxy（论文自身承认），更细粒度语义衡量可能揭示不同 confound 结构。Coreferential 下界（31.6%）约束整体 ambiguity 的下界，无法分离 incompleteness 的 information-addition component。
- **建议**: (1) hierarchy 声明中标注 "conditional on confound assumptions"；(2) 报告 per-type token delta distribution。

**[SHOULD-FIX-3] Differential Nocuity 框架增量贡献被过度表述。** [R2-W3, R1 AGREE]
- Berry & Kamsties (2004)、Willis et al. (2008) 已测量 type-specific nocuity。论文贡献是 LLM agent 场景的实证验证，但 §7 写法暗示新框架。
- **建议**: 改为 "extends Berry & Kamsties' distinction to LLM agents"，明确 credit 先驱工作。

**[SHOULD-FIX-4] Disambiguation Deficit 命名暗示 inability。** [R2-W4, R1 AGREE with nuance]
- "Deficit" 暗示能力缺失，但 mitigation experiment（-8.5pp）证明可通过 prompt 改善。§6.2 已有澄清但术语易误读。
- **建议**: 定义中明确指 "absence of disambiguation behavior in default (uninstructed) settings, not inability"；考虑 "Disambiguation Neglect" 等更精确术语。

**[SHOULD-FIX-5] Per-type 人工验证样本量不足。** [R1-W4, R2 AGREE]
- 100 episodes / 6 types = 32-34 per type。Scopal κ CI [0.00, 1.00] 完全无信息。C2 是 type-level 分析但 per-type 验证精度不足。
- **建议**: 至少在正文 §4.4 明确标注 per-type κ 不具类型间比较价值；理想情况扩大至每类 ≥80。

**[SHOULD-FIX-6] Cross-judge 设计中 judge identity 与 model identity 混淆。** [R1-W5, R2 AGREE with nuance]
- Matched-pair 消除 Δpp 中的 judge bias（C1 safe），但 C2 pooled absolute rates 和 C4 跨模型比较受影响。Within-judge-group C3 各自未达显著。
- **建议**: 报告 C2 type ranking 在两个 judge subgroup 内是否一致。

**[SHOULD-FIX-7] 条件间句子长度差异需补充分析。** [R1-W3, R2 partial REBUT]
- d=0.74 是中等到大效应量。R2 指出 matched-pair design 和 logistic regression（token delta, OR=1.022）已有部分控制，但两人同意需报告 per-type 句长分布，特别关注 incompleteness 是否系统性更长。

### MINOR

- **[MINOR-1]** Clause pair 构建 96% pass rate 未报告 type assignment κ（§4.2）。[R1-W7, R2 AGREE]
- **[MINOR-2]** 引用问题：ferrari_defects_2018 第一作者应为 Rosadini；2 orphan bib entries（tamkin_evaluating_2023, yin_safeagentbench_2025）；navigli_wsd_2009 年份待核实。[R1-W8 = R2-W7]
- **[MINOR-3]** ICC=0.919 仅覆盖 OpenAI 模型族，跨 provider 稳定性未测量。[R1-W9, R2 AGREE]
- **[MINOR-4]** Psycholinguistics 类比（garden-path, good-enough processing）需加 mechanism-level caveat。[R2-W6, R1 AGREE]
- **[MINOR-5]** Coreferential 被系统性排除在 mitigation 和 replication 之外，排除理由需更充分解释。[R1-Q6, R2-Q3]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识（标注 [AGREE]）：

1. **C1 是坚实的核心贡献**——matched-pair design + perturbation control + 7 模型复制，因果推断策略正确
2. **Authorization scope 52pp 不可靠**——κ=0.385 使得该类型的绝对违规率有极大测量不确定性，需大幅下调表述
3. **Two-tier hierarchy 声称过强**——bootstrap 34.3%、margin 依赖性、Kendall's W 不显著，需缩窄为 "incompleteness 一致性上界"
4. **Differential Nocuity 是 domain transfer 而非新框架**——需正确归属先驱工作
5. **Per-type 人工验证不足**——32-34/type 的 κ 估计无统计力度
6. **引用问题**——orphan entries + 作者/年份不一致

## Reviewer Divergence

1. **Taxonomy 概念混淆的严重程度**（轻微分歧）：
   - R2 认为是根本性概念混淆——incompleteness/conditional precedence 不满足 ambiguity 定义，§3 的 operational defense 是循环论证
   - R1 REBUT：操作性定义在实证研究中是标准做法，§3 已有初步回应，但同意需扩展讨论
   - **Director 判断**: R1 的 REBUT 有理，但 R2 的理论关切对 CL-savvy 审稿人有说服力。建议扩展 §3 讨论并引用 Dalpiaz et al. (2018)，不改变 taxonomy 设计。

2. **句子长度 confound 的严重程度**（轻微分歧）：
   - R1 认为 d=0.74 是未控制的 confound
   - R2 partial REBUT：matched-pair design 和 logistic regression（token delta）已有控制
   - **Director 判断**: R2 的反驳合理——within-pair 控制确实吸收了 pair-level variance。但两人同意需报告 per-type 句长分布。

---

## Questions

合并两位 Reviewer 提出的关键问题：

1. **Per-type 句子长度分布**: incompleteness clauses 是否系统性更长？如果是，与 W2 confound 叠加。[R1-Q1]
2. **Variance decomposition 残余 ~76% 方差来源**: 是否主要是 clause-level heterogeneity？如果 type 内 clause 间变异远大于 type 间变异，type-level 概括的信度如何？[R1-Q2]
3. **Incompleteness 与 Wasow (2005) ambiguity 定义的兼容性**: information absence 如何满足 "multiple interpretations" 要求？[R2-Q1]
4. **Bootstrap 34.3% vs continuum 假说**: 如果违规率分布是连续而非离散两层，哪些结论需要修改？[R2-Q2]
5. **Domain-specific SESOI**: ±15pp 对 high-stakes domain（医疗/金融）是否过于宽松？[R2-Q5]
6. **Coreferential 排除 mitigation 的理由**: 作为 information-delta=0 的纯粹 ambiguity 类型，其 mitigation 结果对 disambiguation deficit 解释有重要影响。[R1-Q6, R2-Q3]
7. **Perturbation control 的模型分布**: 300 episodes 是否在 5 个主模型上均匀分布？[R1-Q3]
8. **Clause pairs 的 domain 分布**: 是否在 retail/airline 间均匀分布？domain 是否混淆 type effects？[R1-Q5]

---

## Missing References

两位 Reviewer 合并建议（去重后）：

1. **Dalpiaz, van der Schalk, & Lucassen (2018)**. "Pinpointing Ambiguity and Incompleteness in Requirements Engineering via Information Visualization and NLP." REFSQ 2018. 直接相关——明确区分 ambiguity 和 incompleteness 作为不同 requirements defects。[R2, R1 同意]
2. **Yu, Carroll, & Bentley (2026)**. "The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents." arXiv:2603.20320. Concurrent matched-pair causal design for agent safety，对 "first causal quantification" claim 需更精确 scoping。[R2, R1 同意需确认存在性]
3. **Lin et al. (2025)**. "Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue." 与 disambiguation channel design 讨论相关。[R2]
4. **Willis et al. (2008)** — §7 Discussion 中需明确 credit 其 type-specific nocuity 先驱测量。[R2, R1 同意]
5. **Tamkin et al. (2023)** "Evaluating and Mitigating Discrimination in Language Model Decisions" — 与 auth scope permissiveness bias 相关。已在 bib 中但为 orphan entry。[R1]
6. **Mu et al. (2023)** "Can LLMs Follow Simple Rules?" — policy compliance benchmark。[R1]
7. **Deemter (2010)** "Not Exactly: In Praise of Vagueness"; **Lassiter & Goodman (2017)** probabilistic pragmatics — vagueness 文献扩展。[R1]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时约 3 分钟）

### Findings

**Warnings (2)**:
- **Pages 3-5**: 连续 3 页纯文本（Taxonomy + Method + Statistical Analysis），无任何 display item。Taxonomy 部分（§3, page 3）适合用汇总表或层级结构图打破纯文本节奏。
- **Pages 1-8**: 主文 8 页仅 4 个 display items（3 figures + 1 table），对实证论文偏少（通常 5-8 个）。建议 §3 加类型汇总表，§5 提炼 summary table。

**Info (7)**:
- Figure 1 内部标签字号偏小（page 2）
- Figure 2 压缩在单栏内，可考虑改为 figure*（page 6）
- Figure 3 颜色区分度良好，建议确认色盲友好性（page 7）
- 首页无视觉锚点，可考虑 teaser figure（page 1）
- Table 1 排版规范（page 6）
- Appendix Tables 紧凑但可读（page 12）
- Limitations 段落简短覆盖 3 点，符合 EMNLP 要求（page 8）

---

## Overall Assessment

**Overall Score: 3.5 / 5（Borderline Conference）**
**Soundness: 3.5 / 5**
**Excitement: 3.25 / 5**（R1: 3.5, R2: 3.0 均值）
**Reproducibility: 4 / 5**
**Confidence: 4 / 5**

### 评分理由

**C1（Binary Ambiguity Effect）是扎实的实证贡献**——+34pp, OR=15.1, perturbation control 排除表面扰动, 7 模型复制, 这一因果发现在 agent safety 文献中确有新意，单独可支撑 Findings 水平。

**C2（Type Hierarchy）的核心部分——incompleteness 一致性上界——是稳健的**（7/7 模型 ≥46%），但 "two-tier hierarchy" 的结构性声称统计支撑不足（bootstrap 34.3%, margin-dependent）。当前表述强于证据。

**C4（Model×Type Interaction）受 authorization scope 低可靠性严重影响**——52pp range 这一最引人注目的数字也是最不可靠的。去除 auth scope 后 C4 是否仍显著未知。

**Taxonomy 理论基础**有可辩护的操作性定义，但需要更充分的讨论来应对 CL-savvy 审稿人的质疑。

**Disambiguation Deficit** 是有实用价值的发现（4.6% awareness, mitigation -8.5pp），但命名和框架需要微调。

### 升分路径

如果作者在修订中：(a) 大幅弱化 auth scope / hierarchy 的确定性表述，(b) 补充 C4 去除 auth scope 后的 robustness check，(c) 扩展 §3 理论讨论，(d) 报告 per-type 句长分布和 within-judge-group C2 分析——论文有 4.0（Conference acceptance）的潜力。核心实验设计和 C1 发现是 4.0 水平的贡献，当前拖累评分的主要是 claims 与 evidence 之间的 calibration gap。

---

## Detailed Comments

### §Abstract
- "a two-tier type hierarchy separates incompleteness from the remaining five types" → 弱化为 "incompleteness consistently emerges as the highest-risk type, though tier boundaries are margin-dependent"
- "authorization scope shows the widest cross-model range (52 pp, though measured with the lowest inter-judge agreement, κ = 0.385)" → 括号内信息需提升为同等权重的正文表述，或删除 52pp 具体数字
- 整体信息密度可接受，但 R2 认为偏密集

### §1 Introduction
- Contribution (2) "a two-tier type hierarchy" → 缩窄为 "incompleteness as a consistent upper-bound risk type"
- 复述 52pp 时需同等篇幅讨论 κ=0.385 的可靠性限制
- "observed across five primary models and confirmed in two additional replication models" ✓（已修正 R9 的 'seven models' 问题）

### §3 Ambiguity Taxonomy
- "Scope of 'ambiguity'" 段落方向正确，但需扩展：引用 Dalpiaz et al. (2018) 的 ambiguity/incompleteness 区分；更深入讨论 operational vs strict definition 的 tradeoff
- Layer distinction 作为 theoretical organizing principle 保留合理（C3 已标注 inconclusive）
- 视觉审查建议增加 taxonomy 汇总表（目前 pp.3-5 连续纯文本）

### §4 Method
- §4.2: 补充 type assignment 的 Cohen's κ（当前仅有 96% pass rate）
- §4.4: 正文中标注 per-type κ 因样本量不足（n=32-34/type）不具类型间比较价值
- §4.5: ICC 仅覆盖 OpenAI，在 Limitations 中已承认但可在此处也标注
- §4.6: SESOI=±15pp 的 anchoring 合理，但建议在正文中更突出讨论 margin 敏感性

### §5 Results
- §5.2: 并列呈现 ±10pp three-tier 与 ±15pp two-tier 叙事
- §5.2: incompleteness hierarchy 声明加 "conditional on confound assumptions" caveat
- §5.4: 展示去除 authorization scope 后 C4 交互效应是否仍显著
- §5.4: auth scope 52pp range 标记为 upper bound with substantial measurement uncertainty

### §6 Error Analysis
- §6.1: Gwet's AC₁ vs Cohen's κ 差异的 prevalence paradox 解释可再充实一句
- §6.2: "Disambiguation Deficit" 定义加 "in default (uninstructed) settings, not inability" 限定
- §6.2: "paralleling human good-enough processing" 加 mechanism-level caveat

### §7 Discussion
- "Differential nocuity" → "extends Berry & Kamsties' distinction to LLM agents, where all ambiguity is nocuous but type-specific severity varies"
- 明确 credit Willis et al. (2008) 对 type-specific nocuity 的先驱测量

### Limitations
- 当前覆盖面合理（model coverage, domain scope, synthetic ambiguity, cross-judge, incompleteness confound, severity threshold, per-type reliability）
- 建议补充 sentence length confound 和 SESOI domain-specificity 的讨论

### References
- 修正 ferrari_defects_2018（第一作者 Rosadini）
- 删除或引用 tamkin_evaluating_2023, yin_safeagentbench_2025
- 核实 navigli_wsd_2009 准确性
- 补充 Dalpiaz et al. (2018), Willis et al. (2008) in §7, 以及其他建议引用

### Appendix
- Coreferential 排除理由需更充分解释（mitigation + replication 均排除）
- 报告 per-type 句长分布
- C2 within-judge-group 分析
