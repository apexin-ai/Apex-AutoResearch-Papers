---
round: 8
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-21T17:11:24.032675+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 8 (Fresh)

**Paper**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性 + 实验设计) / R2 (新颖性 + 完整性)
**审稿模式**: Fresh (重新审稿)

---

## Summary

本文研究自然语言 policy specification 中不同类型歧义对 LLM agent 安全违规的因果影响。提出六类型两层结构歧义分类体系（linguistic: scopal/lexical/coreferential; specification: authorization scope/incompleteness/conditional precedence），在 τ²-bench 上构建 300 对 matched clause pairs，评估 5 个模型共 2,997 episodes。核心发现：歧义整体增加 34.0 pp 违规率（OR=15.1, C1），类型间存在层级差异（Cramér's V=0.137, C2），layer effect inconclusive（C3），auth scope 跨模型变异最大（52 pp, C4 exploratory）。论文提出 Differential Nocuity 概念框架并报告 Ambiguity Blindness 现象（<11% awareness）。

---

## Strengths

**S1. C1 binary ambiguity effect 有强力支撑。** OR=15.1, CI=[10.78, 21.17], McNemar p<10⁻⁵, 在全部 7 模型（含 2 个 replication 模型）上显著。Matched-pair design + perturbation control（Δ_perturb=−0.67 pp, CI 含零）有效排除表层扰动解释。这是论文最可靠的贡献。[R1, R2 共识]

**S2. CL-first framing 对 EMNLP 有独特吸引力。** 从计算语言学歧义分类出发定位 agent safety 问题，与 WSD/garden-path 文献形成有意义连接。相比同期工作（如 DRIP-R 的相关性设计），因果推理框架设计更严格。[R2, R1 确认]

**S3. 统计分析分层清晰、诚实。** C1–C4 按置信度递减排列，C3 inconclusive 坦诚报告，C4 明确标记 exploratory。TOST 敏感性分析（Table 2/Appendix A）虽暴露 margin 依赖性但体现方法论严谨。[R1, R2 共识]

**S4. Ambiguity Blindness 有直接工程价值。** <11% awareness + 0% for Qwen3/DeepSeek 是一个直观且重要的经验发现，对 agent 部署有实践意义。[R2, R1 确认]

**S5. 七模型六供应商覆盖增强外部效度。** 主实验 5 模型 + 2 模型 replication，C1 跨架构一致。Limitations 诚实全面。[R1, R2 共识]

**S6. 因果设计优于同期工作。** Matched-pair + perturbation control 的双重因果推理框架是方法论贡献。DRIP-R 差异化论述（3 点）清晰。[R2, R1 确认]

---

## Weaknesses

### Critical (Must-Fix)

**N1. TOST SESOI ±15 pp 缺乏外部锚定，two-tier structure 强烈依赖 margin 选择。** [R1 raised, R2 AGREE]
- §4.6 的锚定理由（practical significance + perturbation CI upper bound）仅是作者自行设定的标准，存在逻辑跳跃。
- ±10 pp 时仅 3/6 mid-tier pairs 等价，±12 pp 时 5/6，直到 ±15 pp 才 6/6。Mid-tier cluster 内部极差 ~11 pp，SESOI 大于此极差才形成 cluster——方法论循环。
- "Robust two-tier structure"（Abstract, §5.2）的声称本质上取决于是否接受 ±15 pp 这一特定阈值。
- **影响**：C2 (type hierarchy) 是论文三大贡献之一，two-tier 稳健性不成立则 Differential Nocuity 精细化程度大打折扣。
- **建议**：提供外部锚定（如 Anvari & Lakens 2021 的 anchor-based methods）；承认 ±10–12 pp 时不稳健；补充 margin-free 方法（Bayesian estimation / bootstrap cluster analysis）。

**N2. Authorization scope cross-judge κ=0.385 过低，无法支撑 C4 "model-differentiating type" 声称。** [R1 raised, R2 AGREE]
- cross-judge κ=0.385 仅 "fair"，是六类中最低；human-LLM κ=0.644, CI=[0.35, 0.91] 下界仅 0.35。
- κ=0.385 意味着约 38.5% judge agreement 超出 chance，52 pp 跨模型变异中真实 model difference vs. 测量噪声无法可靠区分。
- Within-judge 控制仅消除 judge identity 混淆，不解决 per-instance inconsistency（R1 补充，R2 确认）。
- **影响**：C4 是 "safety training selectively mitigates boundary-type ambiguities" 的核心依据。测量不可靠则建议链条断裂。
- **建议**：C4 auth scope claims 降级为 "suggestive/tentative"；增加 bootstrap CI 量化测量不确定性对模型排名的影响；考虑增加人工标注样本量。

**N3. Incompleteness confound 分析缺乏透明度，Abstract 措辞有误导风险。** [R1 raised, R2 AGREE with nuance]
- Logistic regression 控制 token delta 后 "coefficient change <8%, p=0.022"——但未展示完整回归表（coefficients, SEs, model fit），读者无法评估回归质量。
- Token count 是 information content 的粗糙代理，"残余效应存在 ≠ 可量化歧义 vs. 信息比例"（R2 精确区分 partial-out vs. decomposition）。
- Abstract 将 incompleteness 列为 "consistently high (46–62%)" 但正文承认 "upper bound partly reflecting confound"——未分化。
- R1 补充：排除 incompleteness 后五类 omnibus χ² p=0.079，type hierarchy 本身 borderline。
- R2 nuance：coreferential（information delta=0）提供 confound-free lower bound（31.6%），确认纯歧义效应下界真实——问题是 incompleteness 在 hierarchy 中的确切位置不可信，非整体结论无效。
- **建议**：展示完整回归表；Abstract/Conclusion 对 incompleteness 排名显式降级；探索更好的 information proxy 或 information-matched control。

### Warning (Should-Fix)

**W1. 缺少 API 超参数报告。** [R1 raised, R2 AGREE] §4.3 未报告 temperature, max_tokens, top_p，直接影响 reproducibility。

**W2. ICC=0.919 仅在 OpenAI 模型族内测量。** [R1 raised, R2 AGREE] 跨 provider test-retest 未测量。方向一致性 ≠ reliability。

**W3. Per-type human-LLM agreement CI 极宽。** [R1 raised, R2 AGREE] Scopal CI=[0.00, 1.00]（统计上无信息量），源于 per-type n=32–34。正文未讨论此限制。

**W4. 无代码/数据可用性声明。** [R1 raised, R2 AGREE] 300 clause pairs、evaluation pipeline、analysis code 均未承诺发布。EMNLP 要求 reproducibility checklist。

**W5. Clause-level heterogeneity 未充分分析。** [R1 raised, R2 partial AGREE] Clause identity 解释 22.4% variance，但未分析 outlier clauses 或 type 内 clause-level variance 分布。50 clauses/type + high variance → type-level 估计可能不稳定。建议 leave-one-out sensitivity。

**W6. 人工标注者是否对 ambiguity condition 设盲未说明。** [R1 raised, R2 AGREE] §4.4 仅说 blind to LLM judge labels。

**W7. Differential Nocuity 框架概念化不足。** [R2 raised, R1 partial AGREE] 三因素交互未形式化；"channel availability" 未直接测量（推断 ≠ 测量）；与 Berry & Kamsties (2004) 理论推进关系不清。建议用 prediction table 使框架可 falsifiable，或降级为观察性建议。

**W8. C3 layer effect null result 讨论过于简短，abstract 未提及。** [R2 raised, R1 partial AGREE] §5.3 仅 3 句话。如 linguistic/specification 二分法不成立，two-layer taxonomy 的理论基础需重新论证。R1 指出 taxonomy 操作性价值独立于 layer 分组。建议补充讨论 + abstract 简要提及。

**W9. 4 条 orphan bib 条目 + 遗漏引用。** [R1+R2 共识] Orphan: ferreira_patson_2007, levy_expectation_2008, lassiter_goodman_2017, poesio_artstein_2005。应引用 Zheng et al. (2024) LLM-as-a-Judge（与 §4.4 直接相关）和 Anvari & Lakens (2021)（如保留 TOST）。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致：

1. **[AGREE] C1 (binary effect) 是论文最可靠的贡献**，统计支撑充分，7 模型 replication 增强效度。
2. **[AGREE] Incompleteness confound 是最严重的方法论问题**，影响 type hierarchy (C2) 核心 claim 的可信度。
3. **[AGREE] Authorization scope κ=0.385 过低**，C4 claims 应降级。
4. **[AGREE] TOST SESOI ±15 pp 选择方法论循环**，two-tier structure 在更严格 margin 下不稳健。
5. **[AGREE] 缺少 API 超参数、代码/数据声明、标注者 condition blinding 细节**。
6. **[AGREE] 4 条 orphan bib 应清理**。
7. **[AGREE] Overall 3.5 (Borderline Conference)**, Confidence 4/5 (High)。

---

## Reviewer Divergence

分歧较小，均为非关键问题：

1. **[REBUT by R1] Missing references 范围**：R2 建议引用 Constitutional AI (Bai et al., 2022)、AgentBench (Liu et al., 2023)、Bender & Koller (2020)。R1 反驳这些不在论文 scope 内——Constitutional AI 是 alignment 方法非 policy ambiguity，AgentBench 是通用能力 benchmark 非 safety violations，Bender & Koller 关联较远。论文已引用 5+ 个直接相关 agent safety benchmark。**决议**：这些不列为必要遗漏。

2. **[REBUT by R1] Abstract 信息密度**：R2 认为数字过多应减至 2-3 核心发现。R1 认为对经验论文保留效应量合理，真正问题在 incompleteness confound caveat 不够显眼。**决议**：问题降级为 info，重点是修复 confound caveat 可见度。

---

## Questions

**Q1** [R1+R2]: Incompleteness 的 unambiguous variant 平均添加了多少 token？Information delta 分布？完整 logistic regression 回归表（coefficients, SEs, model fit）？

**Q2** [R1]: SESOI = ±15 pp 是否有外部文献或专家调研支持？±10 pp 时 type hierarchy 如何变化？

**Q3** [R1+R2]: 能否提供 within-judge subgroup 的 authorization scope 专项 κ？Claude 12% auth scope violation rate 中的 failure mode 分布？

**Q4** [R1]: Temperature 设置为多少？是否在 temperature > 0 下测试过 stability？

**Q5** [R1+R2]: 300 clause pairs 和 evaluation code 是否计划公开？

**Q6** [R2]: 是否考虑过 information-addition perturbation（添加无关信息不消歧）作为 incompleteness confound 的更直接控制？

**Q7** [R2]: Template-based pipeline 的 template 设计是否公开？96% annotator pass rate 的 disagreement 是否集中在特定类型？

---

## Missing References

**两人共识应引用**：
- Zheng et al. (2024) "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" — 与 §4.4 LLM-as-judge 设计直接相关
- Anvari & Lakens (2021) "Using Anchor-Based Methods to Determine the Smallest Effect Size of Interest" — 若保留 TOST 方法应引用

**R1 单独建议**：
- Kadavath et al. (2022) "Language Models (Mostly) Know What They Know" — 与 Ambiguity Blindness 相关（低优先级）

**R2 建议但 R1 反驳（不列为必要）**：
- Constitutional AI (Bai et al., 2022) — 不在论文 scope 内
- AgentBench (Liu et al., 2023) — 通用能力 benchmark，非 safety
- Bender & Koller (2020) — 关联较远

**Orphan entries 需处理**：
- ferreira_patson_2007, levy_expectation_2008, lassiter_goodman_2017, poesio_artstein_2005 — 引用或删除

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

**状态**：已完成（2026-05-21T16:55 → 16:58，耗时 ~3 分钟）

**Findings (2 warning, 7 info)**：

⚠️ **Warning**:
1. **Pages 3-5**: 连续 3 页纯文本（§3 Taxonomy → §4 Method → §5.1-5.2），无 display item 穿插。§3 六类 taxonomy 仅用文字描述，缺少结构化 taxonomy table/figure 作为视觉锚点。
2. **Pages 1-8**: 主文仅 4 个 display items（1 figure + 1 table + 2 figures），低于实证论文典型密度（5-8 个）。建议增加 taxonomy 结构表/图或 matched-pair 示例表。

ℹ️ **Info**:
- Figure 1 子面板内部文字偏小，打印后可能难辨认。
- Table 1 列数较多，单栏宽度下略显拥挤。
- Figure 2 per-type effect sizes 柱状图可读性良好。
- Figure 3 heatmap 颜色梯度清晰，caption 自包含性好。
- 附录 Tables 3-7 密集排列，Table 5 行间距偏紧。
- 最后一页填充约 55-60%，底部大面积空白。
- 未发现 LaTeX 渲染错误、未解析引用 [?]、margin 溢出等问题，排版基础质量良好。

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**
**Confidence: High (4/5)**
**两位 Reviewer 独立评分一致。**

**总评**：论文研究问题重要且及时，CL-first framing 对 EMNLP 有独特贡献，C1 (binary ambiguity effect, OR=15.1) 有充分统计支撑和七模型 replication。Matched-pair + perturbation control 的因果推理框架是方法论亮点。

但从 C1 到 "type-specific differential nocuity"（C2+C4）的推理链有三个关键短板：(1) TOST SESOI ±15 pp 无外部锚定，two-tier structure 在 ±10 pp 时碎片化；(2) authorization scope 的 judge κ=0.385 无法可靠支撑 52 pp 跨模型变异的解读；(3) incompleteness confound 的 logistic regression 不够透明，且排除 incompleteness 后 omnibus p=0.079。这三个问题从独立角度挑战 C2 (type hierarchy)——论文标题所承诺的 "Not All Policy Ambiguity Is Equal" 在当前数据下支撑不够稳固。

若能：(a) 为 SESOI 提供外部锚定或补充 margin-free 方法，(b) 将 auth scope C4 claims 降级为 tentative，(c) 展示完整回归表并在 Abstract 中标注 incompleteness confound，论文有从 3.5 提升至 4.0 (Conference) 的潜力。当前状态建议 **Findings** 或 **Borderline Conference**。

---

## Detailed Comments

### Abstract
- 信息密度高但对经验论文可接受（R1 观点）。核心问题是 incompleteness confound caveat 不够显眼——"consistently high (46–62%)" 与 "upper bound partly reflecting confound" 应在同一句中出现。
- C3 null result 未提及（R1-M4, R2-W6 共识），abstract 给人 type-specific 结论全部成立的印象。

### Introduction
- 开头 retail 场景有效。Contribution (2) 中同时出现 confound 和 [exploratory] 标记可能给读者不确定感。
- Contribution list 应更 prominently 标注 C3 inconclusive / C4 exploratory。

### Related Work (§2)
- Psycholinguistics 段论证链清晰。DRIP-R 差异化论述（3 点）有效。
- 4 条 orphan bib 需清理。应引用 Zheng et al. (2024)。

### Taxonomy (§3)
- 六类型结构清晰有例子。"Frequency in operational policy documents" 作为选择标准未报告具体频率数据。
- 缺少视觉 taxonomy table/figure 是版面缺陷（视觉审查也标记）。

### Method (§4)
- Cross-judge calibration 详尽是方法论强项。
- **缺失**：API 超参数（§4.3）、标注者 condition blinding（§4.4）、SESOI 外部锚定（§4.6）。
- Model selection 未解释为何无 7B/13B 规模模型。

### Results (§5)
- C1 效应量大且显著——最强发现。
- C2 TOST 是方法论亮点但 margin 依赖性是核心弱点。
- **C3 过于简短**（3 句话），layer 二分法失败对 taxonomy 理论基础的影响未讨论。
- C4 heatmap 有效但 auth scope 结论需降级。

### Error Analysis (§6)
- 三种 failure pattern 有意义，已标 [Exploratory]。
- Inter-coder κ=0.52 (moderate)，minority category κ=0.29，完全基于 LLM coders——系统性偏差无法被 κ 捕获。

### Discussion (§7)
- Differential Nocuity 三因素缺形式化，channel availability 是推断非测量。
- Mitigation experiment across-model variance 未充分讨论。

### Conclusion
- 简洁但可能过于简短，未提 future work。

### Format Compliance
- ✅ 正文 8 页
- ✅ Double-blind（\usepackage[review]{acl}, Anonymous author）
- ✅ Limitations 存在且适当
- ❌ 无 Ethics Statement（建议添加）
- ❌ 无代码/数据可用性声明