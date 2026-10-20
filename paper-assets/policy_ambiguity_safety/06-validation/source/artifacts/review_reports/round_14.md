---
round: 14
review_mode: fresh
overall_score: 3.5 — Borderline Conference
timestamp: 2026-05-22T15:22:58.586316+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 14 (Fresh Review)

**论文**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May cycle)
**审稿日期**: 2026-05-22
**Reviewer 编排**: 2 人（R1: 方法严谨性; R2: 新颖性/完整性）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成共识）

---

## Summary

本文研究政策歧义类型与 LLM agent 安全违规的因果关系。作者构建 300 对匹配子句对（六类歧义），在 τ²-bench 上评估五个模型（2,997 episodes），发现：(C1) 歧义使违规率增加 34.0pp (OR=15.1)；(C2) 类型效应从 +18.7pp（coreferential）到 +49.2pp（incompleteness, upper bound）形成梯度；(C3) 层级效应 inconclusive；(C4) model×type interaction 集中在 authorization scope。方差分解揭示 clause wording (22.4%) >> type (0.4%) >> model (1.0%)。Error analysis 发现 Disambiguation Neglect (≤11% awareness) 和 Systematic Nocuity (41.3% convergent violations)。

---

## Strengths

**S1. 首个 matched-pair 因果研究 + perturbation control** [R1-S1, R2-S1, 共识]
实验设计是核心方法论贡献。每对 clause pair 仅在歧义维度差异，perturbation control (Δ_perturb = −0.67pp, CI [−8.0, 6.67]) 排除表面文本变化的替代解释。300 对 × 5 模型的规模提供 >0.99 统计效力。

**S2. 科学诚实的方差分解** [R1-S2, R2-S2, 共识]
报告 type 仅解释 0.4% variance（clause wording 22.4%、model 1.0%）是罕见的科学透明度——这个发现挑战了论文自身的核心叙事。§7 将 taxonomy 重定位为 "intervention design tool" 是 data-driven 的智慧重构。

**S3. 系统的 robustness 检验** [R1-S3, R2-S3, 共识]
7 个 TOST margin 敏感性分析、bootstrap 聚类、LOO clause 分析、双阈值比较——构成完备的 robustness 框架。C3 labeled "inconclusive"、C4 labeled "exploratory" 体现审慎的 claim calibration。

**S4. 跨架构复制** [R1-S4, 共识]
在 Gemini-2.5-Flash 和 LLaMA-4-Scout 上复制，将 C1 推广到 7 模型 / 6 provider。

**S5. 新概念贡献** [R1-S5, R2-S5, 共识]
Disambiguation Neglect (≤11% per-model awareness, 4.6% overall) 和 Systematic Nocuity (41.3% majority-convergent violations) 为领域引入有价值的分析框架。

**S6. Practical implications** [R2-S4, 共识]
Proof-of-concept classifier (F1=0.81), prompt mitigation 的反直觉发现 (incompleteness 恶化)——让研究不仅停留在诊断层面。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1. 标题/Framing 与 type 仅解释 0.4% variance 的实质性张力** [R1-N2 + R2-N1, 完全共识 AGREE]

标题 "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks" 和 Abstract 中 "per-type effects range from +18.7pp to +49.2pp" 暗示 type 是强预测因子。但 Type III SS 分解显示 type 仅解释 0.4%，clause wording 解释 22.4%——同一类型内的 clause 间差异远大于类型间差异。§7 将 taxonomy 重构为 "intervention design tool"（type→mechanism mapping）是合理的，但这一重构在 §7 才出现，标题/摘要/引言仍以 type gradient 为核心叙事。

两位 Reviewer 独立将此列为 Must-Fix #1，交叉回应中完全一致。

**建议**: (1) 修改标题或在 Abstract 首句引入 0.4% variance qualification；(2) 将 "taxonomy as intervention design" 论证从 §7 前置到 §1 contributions；(3) Abstract 区分 confound-free range (+18.7 to +36.0pp) 和 upper bound (+49.2pp)。

**MF-2. Cross-judge ρ=0.09 严重削弱 C2 梯度声明** [R1-N1 + R2-N1 部分, 完全共识 AGREE]

两个 judge group 的 type ranking 仅 ρ=0.09 (p=0.87)，C2 的 "风险梯度" 在不同评估设置下几乎不可复现。排除 authorization scope 后 ρ=0.90——论文提供了 mechanistic explanation (agent composition 差异)，但无论解释如何，最终结论是 C2 只能稳健支持：(a) incompleteness 是最高风险类型；(b) coreferential 是最低风险类型；(c) 中间四类排序依赖评估设置。将此表述为 robust "gradient" 是 overclaiming。

两位 Reviewer 完全一致。R2 补充：排除 auth scope 有 mechanistic explanation 而非简单删 outlier，但最终判断不变。

**建议**: 将 C2 收窄为 "incompleteness upper bound + coreferential lower bound + mid-tier 排序不确定"；Abstract 承认 gradient robustness 限制。

**MF-3. OR=15.1 与边际比例数值不一致** [R1-N3, R2 交叉 AGREE]

从报告的 41.0%/6.9% 计算 crude OR ≈ 9.4，而非 15.1。CI [10.78, 21.17] 下界高于 crude OR。R2 交叉回应确认：几乎确定是 McNemar's conditional OR (discordant pairs ratio)，logistic regression exp(2.278) ≈ 9.75 也不匹配。Gemini replication crude OR=14.5 与报告一致，但主实验数字不一致。

论文未标注 OR 的计算方法。有统计知识的 reviewer 会立即发现不一致，可能怀疑计算错误。

**建议**: 明确标注 "conditional OR (McNemar's)" 或 "matched OR"，在 Method 中解释计算方式。

**MF-4. 主文可能超出 8 页限制** [Visual Check, R1/R2 分歧]

视觉审查发现主文 (Sections 1-8) 延伸至第 9 页约 0.2 页。Discussion 尾段 + 整个 Conclusion 溢出。EMNLP 2026 严格限制正文 8 页，有 desk reject 风险。R2 交叉回应 REBUT R1 的页数担忧，但视觉审查以 PDF 渲染为准。

**建议**: 压缩主文使 Sections 1-8 完全在 8 页内结束。

---

### Should-Fix（影响评分但不一票否决）

**SF-1. Incompleteness 信息混淆 + 概念正当性张力** [R1-W2 + R2-N2, 部分分歧]

Incompleteness 的 unambiguous variant 必然添加政策内容（补全而非消歧）。Token count logistic regression (p=0.018) 提供部分控制，但 token count 是粗糙代理。Auth scope 有更大 token delta (+36.1 vs +34.6) 但更低违规率——R2 补充此反证力度有限，两类信息性质不同（新约束 vs 边界澄清）。

概念层面：论文承认 incompleteness "involves absent information rather than multiple readings"（§3），behavioral justification 可辩护但需更显著标注。R2 将此列为 Must-Fix，R1 认为 Should-Fix（论文有 behavioral justification 且排除 incompleteness 后 C1 仍成立 Δ=31.0pp）。

**建议**: (1) 主结果同时呈现含/不含 incompleteness 效应范围；(2) Abstract 以 confound-free range 为主；(3) 考虑重命名为 "specification gaps"。

**SF-2. OpenAI judge family bias** [R1-W1 + R2-W2, 完全共识 AGREE]

两个 judge 均属 OpenAI 模型家族。Matched-pair 设计保护 C1 (Δpp) 不受 judge bias 影响，但 C2 的跨模型 type ranking 和 C4 的绝对违规率直接受影响。对 C4 尤其关键——auth scope 的 52pp 跨模型差异中，Claude 12% (GPT-5.4 judged) vs GPT-5.4 64% (GPT-4.1 judged) 无法排除 judge-specific type bias。

**建议**: 对至少一个子集进行 cross-family judge 验证（如 Claude judging），或将此升级为 Limitations 主要段落。

**SF-3. Error analysis LLM-coding circularity** [R1-W3 + R2-W3, 完全共识 AGREE]

§7 的 "taxonomy as intervention design" 重构依赖 §6 的 614 条 LLM-coded traces (κ=0.52)。GPT-5.4/4.1 同时是 agent 和 coder，可能高估 type→mechanism mapping 可靠性。这是论文在 type 解释力低 (0.4%) 后的核心 fallback argument——其证据基础不能仅依赖 moderate agreement 的 LLM coding。

**建议**: 至少对一个 failure category (如 boundary violation，有最清晰操作定义) 进行人工编码验证。

**SF-4. Mitigation 实验呈现混乱** [R1-W4, R2 交叉 AGREE]

§7 混合了至少两个独立实验的数字：(1) generic awareness prompting (+1.3pp)、(2) type-specific prompting (Table 4, pooled −8.5pp)。§7 提到 auth scope "−12pp, p=0.070" 与 Table 4 "−18.0pp" 不一致，incompleteness "+14pp" 与 Table 4 "−3.4pp" 不一致——前者可能来自未完整呈现的 v2 实验。当前呈现方式可能导致 reviewer 对结论可复现性产生疑问。

**建议**: (1) Appendix B 区分 generic vs type-specific 实验并提供完整结果；(2) 主文明确引用来源。

**SF-5. Domain generalizability 声明过度** [R2-W1, R1 交叉 AGREE]

仅覆盖 retail + airline customer service 两个密切相关领域。Abstract/Conclusion 中 "policy-governed deployments" 暗示更广适用性。

**建议**: Abstract/Conclusion 统一限定为 "customer-service policy domains"。

**SF-6. Disambiguation Neglect 增量贡献边界模糊** [R2-W5, R1 部分 AGREE]

"LLMs commit to a single interpretation" 已是 Liu et al. (2023) 和 Sedova et al. (2024) 的核心发现。§6.2 提到 consequentiality 是区分因素，但增量贡献需更清晰表述。

**建议**: 加明确 delta statement 区分与先前工作。

**SF-7. SESOI ±15pp margin dependency** [R1-W5, R2 部分 REBUT]

±15pp 接近观测范围的一半 (22pp)。论文已提供 7 margin 敏感性分析，R2 认为处理足够透明。但 R2 补充：如果标题叙事是 "Not All Equal"，SESOI 选择直接决定 claim 真假——进一步说明 framing 问题的严重性。

**建议**: 主文更突出呈现 margin-dependency，或将 ±10pp 和 ±15pp 结论并列。

---

### Nice-to-Fix

- §5.2 post-hoc observed power (0.993) 方法论有问题，应删除（保留 §4.6 TOST power sensitivity）[R2, R1 部分 AGREE]
- Appendix R Table 12 排版：p16 仅 7 行文字 + 85% 空白，Table 被推到 p17 [Visual Check]
- Pages 4-5 连续纯文本无 display item [Visual Check, 连续多轮]
- Figure 3 热力图色板对红绿色觉障碍者区分度偏低，建议改用 viridis [Visual Check]
- ICC=0.919 仅在 OpenAI 家族内计算，cross-provider 未测量 [R1, R2 AGREE]
- Coreferential 在 mitigation + replication 均被排除，有效 taxonomy 缩减为 5 类 [R1, R2 AGREE]
- Table 2 caption 过长 [R2, R1 AGREE]

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下问题上完全一致：

1. **Framing tension 是核心问题** (MF-1): 标题/摘要以 type gradient 为叙事核心，但 type 仅 0.4% variance。需重构叙事。
2. **Cross-judge ρ=0.09 削弱 C2** (MF-2): 梯度排序不稳健，仅 incompleteness (upper) 和 coreferential (lower) 稳健。
3. **OR=15.1 需澄清** (MF-3): 几乎确定是 McNemar's conditional OR，需明确标注。
4. **OpenAI judge family bias** (SF-2): 对 C2/C4 有系统性威胁。
5. **LLM coding circularity** (SF-3): intervention design 论证基础需人工验证加强。
6. **Domain generalizability** (SF-5): 应限定为 customer-service domains。
7. **叙事重构方向**: 从 "type-specific risks" 调整为 "causal effect (C1) + clause-level dominance + type→mechanism mapping for intervention design"。两位均认为此调整后可达 4.0 (Conference)。

---

## Reviewer Divergence [REBUT]

1. **Incompleteness 严重程度分级**: R2 将概念正当性列为 Must-Fix（incompleteness 非真正歧义，49.2pp 是论文最引人注目但最脆弱的数字）。R1 认为 Should-Fix（论文有 behavioral justification，排除后 C1 仍成立）。**Director 判断**: 列为 SF-1 (Should-Fix)——概念张力真实但论文提供了合理辩护，实验混淆是更直接的问题。

2. **DRIP-R 模型一致性张力**: R2-W4 认为 DRIP-R 发现模型间分歧 vs 本文发现模型间趋同 (Systematic Nocuity) 构成需讨论的张力。R1 [REBUT]: 两篇测量不同 construct (decision quality vs safety violations)，不矛盾。**Director 判断**: R1 的反驳成立，不列为独立问题，但可在 Discussion 用 1-2 句简要说明。

3. **SESOI ±15pp**: R1 认为偏宽松 (W5)。R2 部分 REBUT: 论文已透明处理。**Director 判断**: 列为 SF-7——margin dependency 与 framing 问题耦合，需在主文更突出呈现。

---

## Questions for Authors

1. OR=15.1 的确切计算方法？是 McNemar's conditional OR (discordant pairs b/c ratio) 还是来自特定 regression model？
2. Generic awareness prompting 实验的完整 per-type 结果表在哪里？§7 和 Table 4 的数字来自哪些实验？
3. 如果 taxonomy 的核心价值是 intervention design，为什么不以此作为论文主叙事而保留暗示 type-level prediction power 的标题？
4. Bootstrap cluster analysis 中 incompleteness singleton AU p-value = 0.47 (34.3% reproduction rate)——是否削弱 "incompleteness as robust upper bound"？
5. 方差分解中 22.4% clause wording variance 有多大比例是 signal vs noise？
6. 是否有计划对 failure mode coding 进行人工验证？对 intervention design 主张至关重要。

---

## Missing References

**R2 建议** (R1 无法确认前两篇存在性):
1. ATBench (2026) — agent trajectory safety evaluation benchmark
2. Risky-Bench (2026) — probing agentic safety risks under deployment
3. ICSME 2025 industrial study — requirements ambiguity detection with LLMs

**需确认**: Sehwag et al. (2026) 拼写和引用完整性。

R1 未发现关键遗漏。Related work 覆盖 RE ambiguity、LLM agent safety、LLM ambiguity processing 三个核心领域较为完整。

---

## External Review

**状态**: 未配置/未请求。

---

## Visual Layout Check

**状态**: 已完成 (2026-05-22, 耗时约 3.5 分钟)

| 严重度 | 数量 | 关键发现 |
|--------|------|----------|
| Critical | 1 | 主文延伸至第 9 页约 0.2 页，超出 8 页限制，desk reject 风险 |
| Warning | 3 | Appendix R Table 12 排版浪费整页空白; Pages 4-5 连续纯文本无 display item |
| Info | 7 | Figure 3 色板建议改 viridis; Table 1/2 格式规范; Abstract 信息密度合适 |

---

## Overall Assessment

**评分: 3.5 — Borderline Conference**

**评分理由**:

- **C1 (因果效应)**: 扎实。Matched-pair design + perturbation control 建立了强因果证据。+34.0pp 效应在 7 模型 / 6 provider 上复制。这是论文最坚实的贡献。

- **C2 (类型梯度)**: 部分成立。Incompleteness 作为 upper bound 和 coreferential 作为 lower bound 是稳健的，但中间四类排序依赖 SESOI margin 和 judge group (ρ=0.09)。声称存在 robust "gradient" 证据不足。

- **方差分解**: 重要且诚实的发现 (clause 22.4% >> type 0.4% >> model 1.0%)，但与 framing 严重脱节。

- **Error analysis**: Disambiguation Neglect 和 Systematic Nocuity 概念有价值，但 LLM-coded failure modes 的 circularity risk 削弱了 intervention design 论证的基础。

- **核心问题**: Framing-evidence gap。标题、摘要、引言以 type-specific risks 和 gradient 为叙事核心，但数据支持的故事是 "所有歧义都有害 (C1)，clause 措辞主导风险 (22.4%)，type 预测失败机制而非风险量级"。

**提升路径**: 如果作者 (a) 重构 framing 使标题/摘要与 0.4% variance 对齐，(b) 收窄 C2 claim，(c) 澄清 OR=15.1 计算，(d) 清理 mitigation 实验呈现，(e) 确保 8 页限制——论文可达 **4.0 (Conference)** 水平。当前 framing 下 evidence-claim gap 偏大。

**置信度**: 4/5 (两位 Reviewer 评分和核心判断高度一致，交叉验证充分)

**维度评分汇总**:

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 3.5 | 3.5 |
| Reproducibility | 3.0 | 4.0 | 3.5 |
| Overall | 3.5 | 3.5 | **3.5** |

---

## Detailed Comments

### §1 Introduction
- Contribution (2) 仍以 type gradient 为核心表述，应重构为 intervention design framing
- "per-type effects range from +18.7pp to +49.2pp" 应区分 confound-free range 和 upper bound

### §3 Taxonomy
- "Scope of ambiguity" 段落承认了概念张力，但位置不够突出
- 考虑在 §1 就引入 inclusive definition 的理由

### §4 Method
- OR 计算方法需在 §4.6 Statistical Analysis 中明确
- Cross-judge calibration sample 中 65% ambiguous 可能高估一致性

### §5 Results
- §5.1: 方差分解结果应更前置（而非在 C1 段落内部讨论）
- §5.2: 删除 observed power (0.993)，保留 TOST power sensitivity
- §5.2: C2 claim 需收窄——"gradient" 应改为 "partial ordering with robust extremes"
- §5.4: C4 定位为 auth-scope-specific interaction，需更显著标注 κ=0.385 的不确定性

### §6 Error Analysis
- 加入 circularity risk 的更显著承认（当前仅一句）
- Disambiguation Neglect: 加明确 delta statement 区分与 Liu et al. (2023)

### §7 Discussion
- "Taxonomy as intervention design" 应前置到 §1
- Mitigation 段落需区分 generic 和 type-specific 实验，标注数字来源
- 考虑加 1-2 句讨论 DRIP-R 模型分歧 vs 本文模型趋同（不矛盾但值得说明）

### §8 Conclusion
- "policy-governed deployments" → "customer-service policy domains"
- 确保在第 8 页内结束

### Limitations
- OpenAI judge family bias 升级为主要段落
- ICC scope 限制明确标注

### Appendix
- Table 12 排版修复（与引言文字合并）
- Appendix B 补充 generic prompting 完整结果