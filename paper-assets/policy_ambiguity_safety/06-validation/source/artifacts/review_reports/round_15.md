---
round: 15
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T16:58:41.930560+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 15 (Fresh Review)

**Paper**: "All Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性), R2 (新颖性与完整性)
**Review Mode**: Fresh (无上轮记忆)

---

## Summary

本文通过 matched-pair 因果设计研究政策歧义对 LLM agent 安全的影响。在 τ²-bench 上构建 300 组歧义/非歧义条款对（六类型两层分类），跨五个模型评估 2,997 episodes。核心发现：歧义条款使违规率增加 34.0 pp（conditional OR = 15.1）；方差分解显示 clause wording（22.4%）远超 type（0.4%）和 model（1.0%）；type 预测 failure mechanism 的 MI 是预测 violation rate 的 30×。论文将 taxonomy 从风险预测工具重新定位为干预设计框架。

---

## Strengths

**S1. 严谨的 matched-pair 因果框架** [R1, R2 共识]：这是相对于 DRIP-R 等相关性研究的真正方法论进步。Perturbation control（Δ = −0.67 pp, CI 含零）有效隔离了语义歧义的因果效应，排除了任意文本扰动的解释。

**S2. 全面且恰当的统计工具箱** [R1, R2 共识]：McNemar's test、TOST equivalence testing（7 档 margin sensitivity）、Fisher's exact、Type III SS 方差分解、bootstrap clustering、互信息分析、Holm–Bonferroni 多重比较校正——每个工具与其用途匹配良好。主动披露 margin dependence 的透明度在该领域少见。

**S3. 诚实的方差分解** [R1, R2 共识]：Type membership 仅解释 0.4% 方差 vs. clause identity 的 22.4%——这与论文分类体系导向的 framing 形成反直觉对比。论文选择报告并积极利用这一发现重新定位 taxonomy，体现科学诚实。

**S4. Taxonomy-as-diagnostic-tool 洞见非平凡** [R2 提出, R1 认可]：Type → failure mechanism 的 MI 是 type → violation 的 30×，每种 type 映射到机制不同的 failure pattern（structural misparse / gap-filling / boundary violation）。这是对 Berry & Kamsties (2004) 在 LLM agent 领域的有价值延伸。

**S5. 扎实的标注与验证** [R1, R2 共识]：96% 初始标注者一致率、κ = 0.798 / κ_w = 0.762 人工评估者间一致性、cross-judge calibration（κ = 0.653, κ_w = 0.775）、两个额外模型族复现。

**S6. Disambiguation Neglect 与 Systematic Nocuity 量化有意义** [R2]：将 LLM ambiguity collapse 从文本扩展到有不可逆后果的 agentic setting（≤11% per-model awareness, 4.6% overall）。41.3% majority-convergent violations 表明基于一致性的评估方法会完全遗漏系统性风险。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1. "Intervention-design framework" overclaim** [R2 提出, R1 AGREE]
- 论文在 Abstract、Contribution (2)、Section 7、Conclusion 反复将 taxonomy 定位为 "intervention-design framework"，但实际 intervention 内容薄弱。Appendix B 的 mitigation 实验结果参差不齐（auth scope −18.0 pp、incompleteness −3.3 pp、generic awareness +1.3 pp），无具体干预协议或决策逻辑。
- "Framework" 暗示系统性方法论贡献，但当前内容更接近 "diagnostic mapping"——从 type 到 mechanism 的映射有信息价值但不构成 framework。
- **建议**：将措辞降级为 "diagnostic taxonomy" 或 "failure-mechanism predictor"，在 Discussion 明确从 diagnostic mapping 到 concrete intervention 的后续工作。

**MF-2. Cross-judge type ranking ρ=0.09 对 C2 mid-tier ordering 的影响需更突出** [R2 提出, R1 AGREE with nuance]
- Cross-judge-group type ranking ρ = 0.09（p = 0.87）本质上是随机的。排除 auth scope 后 ρ = 0.90（p = 0.037），但这一关键的 robustness 分析仅出现在 Section 5.2 中间段落和 Limitations，不够醒目。
- R1 补充：排除 auth scope 有独立先验理由（κ 最低 0.385、cross-model range 最大 52 pp），非纯粹 post-hoc cherry-picking。但两位 judge 均来自 OpenAI family，family-level systematic bias 无法排除。
- **建议**：在 Section 5.2 更突出地展示 mid-tier ordering 的 judge-dependency，将 C2 claim 明确限定为"incompleteness 作为 upper bound 和 coreferential 作为 lower bound 是 robust 的，mid-tier ordering 依赖 judge/model 组合"。

**MF-3. Incompleteness confound-free 效应范围未在主文充分呈现** [R1 Must-Fix, R2 Should-Fix → 共识升为 Must-Fix]
- Incompleteness 是效应最大的类型（+49.2 pp），但其 unambiguous variant 必然添加 policy content（information-addition confound）。Confound 分析完整存在于 Appendix F/H，主文仅一句 "conditional on confound controls" 和 sans-incompleteness 报告。
- 多数读者只读主文——将核心 claim 的 robustness check 完全放在附录中对 soundness 评价不利。
- **建议**：在 Section 5.1 或 5.2 增加 1-2 句，报告 confound-free 效应范围（coreferential +18.7 pp 到 incompleteness +49.2 pp），并提及排除 incompleteness 后 C1 仍 large（Δ = 31.0 pp）。

### Should-Fix（影响评分但不一票否决）

**SF-1. 标题 "All Policy Ambiguity Is Nocuous" 普遍性超出实证范围** [R1, R2 共识]
- "All" 超出 2 domain（retail + airline）+ 6 type + synthetic clause 的实证范围。Limitations 承认"effects in other domains remain untested"。
- **建议**：在 Abstract 首句增加范围限定（如 "on a customer-service agent benchmark"），或删除标题中的 "All"。

**SF-2. "30×" MI ratio 需绝对值上下文** [R2 提出, R1 AGREE]
- I(type; violation) 本身极小（对应 0.4% variance），30× 一个极小量的绝对值仍不大。Ratio 跨越两个不同 target variable 的 MI 比较有些 arbitrary。
- **建议**：首次使用时添加"type explains 0.4% of violation variance but X% of mechanism variance, a 30× ratio"，同时报告 I(type; mechanism) = 0.41 bits 的实际含义。

**SF-3. C2-C4 篇幅 vs 0.4% 方差的 framing 过渡缺失** [R1 提出, R2 部分 REBUT 但同意 framing 过晚]
- Type 解释 0.4% 方差，但 Sections 5.2-5.4 占 Results 约 60% 篇幅。Discussion（Section 7）才揭示 intervention-design 定位，读者在 Results 中会困惑。
- R2 指出内容本身不应压缩（mechanism prediction 是叙事核心），但同意 framing 转折来得太晚。
- **建议**：在 Section 5.1 方差分解后、C2 之前，添加 1-2 句 bridge sentence 预告：虽然 type 解释的 violation variance 极小，但其对 failure mechanism 的预测力远大于对 violation rate 的预测力。

**SF-4. 错误分析 LLM coding 循环性** [R1 提出, R2 部分 REBUT]
- 使用 GPT-4.1 编码 LLM 失败模式引入循环性风险。Section 6 的 MI 辩护（I = 0.41 bits, V = 0.45 from exogenous type labels）提供了结构性 anti-circularity 证据，但不完全排除 systematic coding bias。
- **建议**：补充少量（50-100 episodes）人工验证的 failure mode 标签以建立 ground truth。

**SF-5. 遗漏 3 篇重要并发参考文献** [R2 提出, R1 PARTIAL AGREE]
- (a) Gur-Arieh et al. (2026), "Ambiguity Collapse by LLMs: A Taxonomy of Epistemic Risks" (arXiv:2603.05801) — 直接关于 LLM ambiguity collapse 的 epistemic risk taxonomy
- (b) OpenAgentSafety (Vijayvargiya et al., ICLR 2026) — 综合 agent safety 评估框架
- (c) "Disambiguation in Conversational Question Answering in the Era of LLMs and Agents: A Survey" (arXiv:2505.12543, 2025)
- R1 无法独立验证存在性——需作者确认并根据时间线决定是否引用。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全达成共识：

1. **C1（+34 pp 二元歧义效应）因果证据充分**，matched-pair 设计、perturbation control、统计框架扎实
2. **"Intervention-design framework" overclaim**——taxonomy 有诊断价值但不构成 framework
3. **Incompleteness confound** 需在主文更充分呈现
4. **标题 "All" 超出实证范围**
5. **Cross-judge ρ=0.09** 需在主文更突出地展示对 C2 mid-tier 的影响
6. **修复 MF-1/MF-2/MF-3 后论文有望从 3.5 提升至 4.0**

## Reviewer Divergence [REBUT → 已解决]

1. **R1-N1 vs R2 REBUT**: R1 原始 Must-Fix 称"论文未报告排除 auth scope 后的 C4 分析"——R2 指出这是事实错误：Section 5.4 末句明确报告 p = 0.97，C4 已标注 [Exploratory]。R1 的 N1 基于错误前提，**已降级**。Auth scope 测量可靠性低（κ=0.385）的担忧本身合理，但论文已主动披露。

2. **R2-W3 vs R1 REBUT**: R2 认为 taxonomy 概念边界模糊（incompleteness 和 conditional precedence 非 linguistic ambiguity）。R1 rebut：Section 3 已有显式 operational definition、非标准用法声明、Dalpiaz et al. (2018) 引用。**共识**：当前处理可接受，可在 Section 3 添加一句 cover term 说明。

3. **R1-W1 vs R2 部分 REBUT**: R1 认为 C2-C4 篇幅不成比例。R2 指出内容不应压缩（mechanism prediction 是核心），但 **同意 framing 过渡应前移**。

---

## Questions（需作者澄清）

**Q1** [R2]: Variance decomposition（Section 5.1）使用 Type III SS 对 binary outcome——为什么不用 logistic model 的 deviance decomposition？两种方法是否给出一致结论？

**Q2** [R1]: 方差分解中 clause identity 22.4% + model 1.0% + type 0.4% = ~24%。剩余 ~76% 方差来源是什么？（Episode-level 噪声、conversation trajectory、API 非确定性？）

**Q3** [R2]: Cross-judge calibration 的 100 episode 样本中 65% 为 ambiguous condition。Dataset 是 50/50 matched-pair 设计——calibration sample 是否有 oversampling bias？对 κ 估计的影响？

**Q4** [R2]: Post-hoc realism validation（Section 4.2 "plausibly natural"）的具体方法？除标注者主观判断外，是否有系统性 realism 评估？

**Q5** [R2]: Mitigation experiment 的 type-specific prompt 具体内容？Incompleteness 效果方向相反（−3.3 pp vs +14 pp）暗示 prompt sensitivity 高——是否测试了多个变体？

**Q6** [R1]: Moderate-or-above severity threshold 是否在数据收集前 pre-registered？

---

## Missing References

**R2 识别（R1 PARTIAL AGREE，需验证真实性）：**
1. Gur-Arieh, Wang, & Fazelpour (2026) — "Ambiguity Collapse by LLMs: A Taxonomy of Epistemic Risks" (arXiv:2603.05801)
2. Vijayvargiya et al. (ICLR 2026) — "OpenAgentSafety"
3. Disambiguation in CQA Survey (arXiv:2505.12543, 2025)

**历史遗留：**
- R13-M1: ATBench/Risky-Bench/ICSME 2025 — 当前版本未找到，需作者确认是否有意移除
- R10-M2: Ferrari/Ferreira 引用不一致 — R1 认为当前版本似已修正，需作者确认

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未启用 external_review）。

---

## Visual Layout Check（非评分项）

状态：✅ 已完成

**Critical (1)**:
- **Page 17**: 末页内容仅占约 1/5 页面，~4/5 为空白。建议重排附录使末页至少填充 2/3。

**Warning (2)**:
- **Pages 4-5**: 连续 2 页纯文本（Method §4.1-4.4），无 display item。建议插入方法示意图或移动 Table 1。（与 R10-M6 一致，R15 两位 Reviewer 再次指出。）
- **Pages 8-9**: 连续 2 页纯文本（Error Analysis → Discussion → Conclusion → Limitations），三个 section 转换压缩。Conclusion 仅约 8 行。

**Info (5)**:
- Figure 1 内部文字偏小（~6-7pt），建议放大或改为 figure*
- Figure 3 热力图低值区与白色背景对比度偏低，建议加深最浅色或加 cell 边框
- Table 2 字号偏小，建议每行最优值加粗
- Table 6 未加粗标注最优行
- Limitations 段落长度适当，符合 EMNLP 要求 ✅

---

## Overall Assessment

**Overall Score: 3.5 / 5 — Borderline Conference**

**ACL ARR 维度评分（综合两位 Reviewer）：**

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3.5-4 / 5 | Matched-pair 设计与 C1 统计分析扎实，controls 全面。但 cross-judge concordance 为零削弱 C2 mid-tier，incompleteness confound 的主文处理不足。 |
| Excitement | 3.5 / 5 | 重要问题 + 非平凡的 variance decomposition 洞见 + mechanism prediction 发现。但 actionable takeaway 有限——intervention framework 停留在概念层面。 |
| Reproducibility | 4 / 5 | API 参数、模型版本、评估流程完整，承诺数据公开，ICC = 0.919。主要缺口是 ICC 限于 OpenAI family。 |

**核心判断：**

论文的 C1 因果发现（+34 pp, OR = 15.1）是扎实的，matched-pair design + perturbation control + variance decomposition 构成实质性方法论贡献。Disambiguation Neglect（≤11% awareness）和 Systematic Nocuity（41.3% convergent violations）对 deployment safety 有重要警示价值。

但三个 Must-Fix 限制了当前版本的说服力：(1) "intervention-design framework" 缺乏实质性干预内容支撑；(2) cross-judge type ranking 近零相关（ρ=0.09）使 C2 mid-tier ordering 不可靠，需在主文更突出限定；(3) incompleteness confound 的 robustness check 埋在附录，主文需呈现 confound-free 范围。

三个 Must-Fix 均为 framing/presentation 问题而非 soundness 缺陷——修复所需工作量有限。修复后论文有望达到 4.0（Conference）水平。

**Confidence**: 4 / 5

---

## Detailed Comments（逐节）

### Title
- "All Policy Ambiguity Is Nocuous" 的 "All" 超出实证范围（2 domain, 6 type, synthetic clauses）。建议删除 "All" 或在 abstract 限定。

### Abstract
- "repositioning the taxonomy as an intervention-design framework" → 降级为 "diagnostic taxonomy" 或 "failure-mechanism predictor"
- "300 ambiguous/unambiguous clause pairs" → 可更精确为 "300 matched clause pairs across six types (50 per type)"
- 首次使用 "30×" 时需提供绝对量上下文

### Section 3 (Taxonomy)
- 概念边界处理可接受（有 operational definition + 显式 caveat），可在开头添加一句 cover term 说明

### Section 4 (Method)
- 连续两页纯文本（pp.4-5）无 display item，建议添加 pipeline diagram 或移动 Table 1
- Severity threshold（moderate-or-above）选择的独立论证缺失（minor）

### Section 5.1 (C1)
- Sans-incompleteness C1 已报告（Δ = 31.0 pp）✓
- 需添加 confound-free 效应范围（18.7–49.2 pp）
- Type III SS 对 binary outcome 的方差分解方法需说明或与 logistic deviance decomposition 对比
- 方差分解后、C2 前需 bridge sentence 预告 mechanism prediction 价值

### Section 5.2 (C2)
- ρ = 0.09 已披露 ✓，但 mid-tier ordering 的 judge-dependency 需更突出
- C2 claim 应明确限定：extremes robust, mid-tier judge-dependent

### Section 5.4 (C4)
- 已标注 [Exploratory]，已报告排除 auth scope 后 p = 0.97 ✓
- Auth scope κ = 0.385 的不确定性已在主文披露 ✓

### Section 6 (Error Analysis)
- MI anti-circularity 辩护有力但不完全充分，少量人工验证 failure mode 标签是有益补充
- Garden-path 类比作为 analogy 可接受，但措辞应避免暗示 LLM 有 incremental parsing 机制

### Section 7 (Discussion)
- "intervention-design framework" 定位需降级
- Mitigation 实验中 incompleteness 方向相反（−3.3 vs +14 pp）的 prompt sensitivity 需解释

### Section 8 (Conclusion)
- 几乎逐字重复 Abstract，缺乏 broader implications 反思

### Limitations
- 覆盖度适当（scope / measurement / confounds 三维度）✓
- 长度符合 EMNLP 要求 ✓

### Appendix
- Table 12 (clause pair examples) 排版可压缩
- 末页（p17）大量空白，建议重排