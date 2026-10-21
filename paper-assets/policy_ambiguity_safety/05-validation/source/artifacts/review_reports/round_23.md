---
round: 23
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T05:36:00.863929+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 23 审稿报告 — Policy Ambiguity Is Nocuous

**Venue**: EMNLP 2026 via ARR May cycle | **Deadline**: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）
**审稿模式**: Fresh（重新审稿）

---

## Summary

本文在 τ²-bench 上构建 300 对 matched-pair 歧义/无歧义策略条款，通过六类型×两层分类体系评估五个模型（附加两个 replication family），证明策略歧义在合成条件下使 LLM agent 安全违规率增加 34.0 pp（排除 confounded incompleteness 类型后 +18.7 至 +36.0 pp，pooled +31.0 pp）。方差分解发现条款措辞解释 22.4% 方差 vs 类型仅 0.4%，但类型对失败机制的预测能力远强于对违规率的预测（NMI = 0.23 vs 0.01）。这是一项方法论扎实的因果研究，C1 核心发现跨 7 个模型和 2 个 benchmark 稳健复制，但正文超页、authorization scope 类型不可靠性、以及生态效度限制是主要障碍。

---

## Strengths

**S1. Matched-pair causal design 是首次用于 agent safety evaluation 的方法论贡献** [R1, R2 一致]
与 DRIP-R（观察性设计）和 MANTRA（SMT 形式化验证）相比，minimal-edit 配对设计在 clause level 建立歧义→违规的因果联系。Perturbation control（n=300, Δ=-0.67pp, CI containing zero）确认语义歧义特异性。

**S2. C1 核心发现极其稳健** [R1, R2 一致]
+34.0pp 效应跨 5 主模型 + 2 replication families（7 models, 6 providers）一致显著。排除任何单一类型均不影响 C1。排除 incompleteness 后仍有 +31.0pp（p < 10⁻⁷⁵）。SOPBench 跨基准复制 (+12.6pp) 方向一致。Severity threshold robustness 确认。

**S3. Variance decomposition 发现具有实用价值** [R1, R2 一致]
条款措辞 22.4% vs 类型 0.4%——intervention 应针对具体条款而非歧义类别。Type-mechanism mapping（NMI=0.23, Cramér's V=0.45）将诊断建议落地到具体 failure mode。

**S4. 统计方法选择审慎且全面** [R1, R2 一致]
McNemar's test、TOST equivalence、Type III SS、ICC、bootstrap clustering、Holm-Bonferroni 在三个预注册测试族内校正——每种方法适合对应分析。

**S5. 高度透明的 limitation disclosure** [R1, R2 一致]
论文主动披露 ρ=0.09 cross-judge concordance、auth scope 低 κ、OpenAI-only ICC decomposition 等对自己不利的数据。但 disclosure ≠ adequate handling——R1 和 R2 的共同观察是论文承认了问题但未充分调整 claim 强度。

**S6. Error analysis 超越纯 measurement** [R2]
Disambiguation neglect（overall awareness 仅 4.6%，Qwen3/DeepSeek 为零）和 systematic nocuity（41.3% convergent violations）对 agent deployment 设计有实际意义。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [critical] 正文超 8 页限制** [R1 + R2 共识]
Discussion（§7）从 p8 延伸到 p9，Conclusion（§8）也在 p9 上半部分。正文（Abstract 到 Conclusion）约 8.4-8.5 页，超出 EMNLP 2026 long paper 严格 8 页限制。视觉审查 Agent 独立确认。可能导致 desk rejection。
→ 压缩 Discussion（三段→两段）或将部分 §6 Analysis 移入 Appendix。

**N2 [critical] Authorization scope 类型系统性不可靠，动摇 C2/C4 claims** [R1 + R2 共识]
五个独立指标同时指向不可靠：(1) κ=0.385（六类型最低）；(2) per-type ICC≈0；(3) 单独驱动跨 judge 组 ρ=0.09→排除后 0.90；(4) 单独驱动 C4 interaction（排除后 p=0.97）；(5) 52pp 跨模型方差。但 Table 2 和主分析中无显著区分标记。
→ Table 2 增加警告标注；C2 中将 auth scope 标记为 unreliable；系统性报告 excluding auth scope 后的 C2 结论。

### Should-Fix（影响评分但不一票否决）

**W1 [major] Incompleteness confound 在 headline claim 中标注不够显著** [R2 提出, R1 部分 rebut]
Abstract 中 "34.0 pp (+18.7 to +36.0 pp excluding...)" 将 confound-free range 置于括号内。R1 指出排除 incompleteness 后 pooled effect 为 +31.0pp（仅差 3pp），认为是 framing 问题而非 validity 问题。
→ 建议在 Abstract 中将 +31.0pp (excl. incompleteness) 放在更显著位置。Table 2 增加 "Overall (excl. Incomp.)" 行。

**W2 [major] ρ=0.09→0.90 的 post-hoc 排除叙述** [R1 + R2 共识]
排除 1/6 类型后从 ρ=0.09 到 ρ=0.90——即使有理论理由，这在审稿中会被高度怀疑。Three-family validation（ρ=0.71–0.89, Appendix W）是更强且不依赖 post-hoc exclusion 的证据，但仅在 Appendix。
→ 将 three-family validation 提升到主文作为 primary evidence；排除分析标记为 sensitivity check。

**W3 [major] Residual variance decomposition 的 OpenAI-only 限制** [R1 提出, R2 同意 with nuance]
15% stochastic + 46% systematic 来自 OpenAI family ICC(1) replication。§5.1 和 §7 在引用时未逐次注明。R2 指出 ICC(3,1)=0.919 是全模型指标（C1 稳健性不受影响），stochastic/systematic split 的 OpenAI-only 限制是 labeling issue。
→ 主文每次引用 stochastic/systematic split 时注明 "OpenAI-family estimate"。

**W4 [major] TOST ±15pp SESOI justification 有 pragmatic 成分** [R1 + R2 共识]
标准 (2) 本质上是主观判断。±10pp 时仅 3/15 pairs 等价，SESOI 选择对 C2 cluster structure 结论有实质影响。
→ 明确承认 pragmatic 选择而非 objectively principled；将 bootstrap clustering 提升为与 TOST 并列的主要证据。

**W5 [major] Cross-judge per-type κ 缺少 bootstrap CI** [R1 + R2 共识]
100 episodes / 6 types ≈ 17 per type。κ=0.385 for auth scope 可能有 ±0.2–0.3 的 CI。Human-LLM agreement (Appendix G) 已有 bootstrap CI，cross-judge calibration 应对齐。
→ 补充 per-type cross-judge κ 的 bootstrap CI。

**W6 [warning] 合成歧义的生态效度** [R2 提出, R1 同意但认为是固有限制]
所有 300 clause pairs 均模板合成。SOPBench 也是合成 benchmark。未提供真实企业策略文档歧义案例。R1 指出 matched-pair design 本质上需要合成操控。
→ Discussion 中更明确讨论 synthetic→real-world gap 的具体 threats（如真实歧义的上下文依赖性更强）。

### Minor（不影响接收）

**M1.** NMI=0.23 vs 0.01 的 "order of magnitude" 表述——比较层面准确（23×），但绝对值仍是 moderate association。建议补充 "moderate association in absolute terms" 限定。[R2 提出, R1 rebut; 降级 minor]

**M2.** Abstract 信息过载——约 150 词内 6+ 个定量结果。建议保留 2-3 个核心数字。[R1 + R2 共识]

**M3.** Disambiguation neglect 推断边界——应区分 internal detection 和 surface behavior。§6.2 首次定义处加入 "surface" 限定词。[R1 + R2 共识]

**M4.** Table 2 "Overall" 行增加 "Overall (excl. Incomp.)" 或脚注。[R1 + R2 共识]

**M5.** Token count 作为 confound proxy 粗糙——承认局限性即可，不需新度量。[R1 + R2 共识]

**M6.** §4.3 "five architecturally diverse models" 表述——GPT-5.4 和 GPT-4.1 同属 OpenAI，改为 "five models from four providers"。[R2]

**M7.** References 格式——部分 arXiv 引用 submission date 写法不统一。[R2]

---

## Reviewer Consensus [AGREE]

1. **C1 是稳健的、可达 Conference 水平的贡献**——matched-pair causal design + 跨 7 模型 + 跨 2 benchmark 复制
2. **正文超 8 页是必须修复的硬性问题**——EMNLP 2026 desk rejection 风险
3. **Authorization scope 不可靠性是核心方法论问题**——五个独立指标同时指向，需在 C2/C4 claim 中实质性调整
4. **ρ=0.09→0.90 的排除分析有 post-hoc 嫌疑**——three-family validation 应提升到主文
5. **TOST ±15pp 是 pragmatic 选择**——需更透明承认
6. **论文透明度值得肯定**——但 disclosure ≠ adequate claim adjustment

## Reviewer Divergence [REBUT]

1. **Incompleteness confound severity**: R2 评 critical → R1 以数据 rebut（排除后 pooled +31.0pp，仅差 3pp）→ 共识降级为 should-fix (framing 问题)
2. **Variance decomposition severity**: R1 评 critical → R2 认为是 labeling issue（ICC(3,1)=0.919 是全模型指标）→ 共识降级为 should-fix
3. **NMI "order of magnitude" 表述**: R2 评 minor-major → R1 rebut（已有 Cramér's V=0.45）→ 降级 minor

---

## Questions（需作者澄清）

**Q1.** Perturbation control CI [-8.0, 6.67] pp 对 5pp true effect 的统计功效是多少？[R1]
**Q2.** Type III SS variance decomposition 的完整模型公式是什么？是否包含 random effects？[R1]
**Q3.** Auth scope per-type cross-judge κ=0.385 的 bootstrap 95% CI 是多少？[R1, R2]
**Q4.** 是否计算过跨 provider 的 reproducibility 度量？[R1]
**Q5.** NMI 在 failure mechanism 分布高度不均衡时是否是合适度量？[R1]
**Q6.** Bootstrap clustering modal partition 仅 34.3%（AU=0.47），更高 k 值的 partition stability 如何？[R1]
**Q7.** 歧义条款注入点的选择标准是什么？注入位置是否引入系统性偏差？[R2]
**Q8.** 是否考虑过将 incompleteness 从 taxonomy 中独立出来？[R2]
**Q9.** Mitigation instruction quality 本身是否是 confound？[R2]

---

## Missing References

- **Enhancing LLM Agent Safety via Causal Influence Prompting** (2026, arXiv:2507.00979)——causal 方法 + agent safety，与本文方法论框架直接相关 [R2 提出，需验证真实性]
- 论文 Related Work 整体覆盖较好，已引用 DRIP-R、PolicyBank、MANTRA、OpenAgentSafety、SOPBench 等主要并发工作

---

## External Review

**状态**: 未配置

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成（0 critical, 2 warning, 18 info）

关键发现：
- **[warning] Pages 4-5**: 连续 2 页纯文本（§4 Method），无 display item 穿插。插入 method 示意图或 matched-pair 构造示例会改善阅读节奏。
- **[warning] Page 7**: 单页堆叠 3 个 display items（Table 2 + Figure 3 + Figure 4），密度过高。建议将 Figure 3/4 合并为双面板或分散到相邻页。
- **[info] Pages 1-9**: 正文约 7 个 display items（~0.78/页），密度合理偏紧凑。
- **[info] Page 7**: Figure 3 和 Figure 4 尺寸偏小，axis label 字号接近可读下限。
- **[info]** 正文（Sections 1-8）延伸至 page 9，**与两位 Reviewer 独立确认的超页问题一致**。
- **[info]** 无内容溢出 margin、无 LaTeX 错误残留、无 [?] 未解析引用、无 section heading 孤悬。

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**

**置信度**: 4/5（两位 Reviewer 独立给出相同评分，交叉回应后无变化）

**理由**:
- **C1 贡献可达 Conference 水平**：matched-pair causal design 在 agent safety 领域是首次；+34.0pp 效应（confound-free +31.0pp）跨 7 模型稳健复制；variance decomposition 和 type-mechanism mapping 有实用价值。
- **阻碍升至 4.0 的因素**：(1) 正文超 8 页（desk rejection 风险）；(2) authorization scope 不可靠性未充分反映在 claim 中；(3) 类型层面分析（C2-C4）的 claim 强度与证据不完全匹配。
- **如果 N1（页数）和 N2（auth scope 标注）能妥善解决**——这主要是 claim qualification 和排版压缩，不需要新实验——**论文可达 Conference (4.0) 水平**。

**ARR 评分标准对照**: 3.5 = Borderline Conference，意味着论文有 Conference 水平的方法论贡献，但需要在格式合规和 claim 校准上做出修改才能被主会议接收。

---

## Detailed Comments（按章节）

### Abstract
- 信息密度偏高（6+ 个数字）；建议精简至 3 个核心数字
- "+34.0 pp (+18.7 to +36.0 pp excluding...)" 的括号标注不够显著；建议将 +31.0pp (excl. incompleteness) 放在更显著位置
- "systematic nocuity: over 40% of clauses triggering model-convergent violations" 是有效的 anchor point

### §1 Introduction
- Figure 1 placement（page 2 顶部）合理
- Opening example（$200 退款场景）有效建立 motivation
- Contribution (2) 的 "order of magnitude" 可加 "moderate association" 限定

### §2 Related Work
- 覆盖全面，已引用主要并发工作（DRIP-R, PolicyBank, AgentPex, MANTRA）
- Appendix L 的 DRIP-R 对比分析充分

### §3 Taxonomy
- 六类型选择的三项 design criteria（attestation + minimal-pair + mutual exclusivity）有说服力
- "Scope of 'ambiguity'" 段对 inclusive definition 的论证合理
- C3 layer effect 已正确标注为 organizational convenience

### §4 Method
- Matched-pair design 严谨
- Cross-judge calibration（§4.4）需补充 per-type κ 的 bootstrap CI
- SESOI ±15pp（§4.6）需更透明承认 pragmatic 选择

### §5 Results
- C1 证据充分
- C2 partial ordering 需更谨慎处理 auth scope
- ρ=0.09 的主文呈现需调整——three-family validation 应提升为 primary evidence
- C4 已正确标注为 exploratory/suggestive only

### §6 Analysis
- Type-mechanism mapping（§6.1）是有价值的 exploratory finding
- Disambiguation neglect（§6.2）需在定义处加 "surface" 限定词
- Systematic nocuity（§6.3）发现具有实际意义

### §7 Discussion
- 需要压缩（当前占用过多页面导致超限）
- "Taxonomy as diagnostic tool" 段与 §6.1 有部分重叠
- Intervention ceiling 讨论（22.4% vs 60.8% residual）已到位

### §8 Conclusion
- 长度适中
- Confound-free range 已呈现

### Limitations
- 覆盖 5 个方面（ecological validity, scope, measurement, confounds, disambiguation channel）
- 符合 EMNLP 2026 要求（不计入页数）
- 透明度值得肯定

### Appendix
- 内容丰富（15+ 表，多项 supplementary analysis）
- 格式统一（booktabs, 一致精度）