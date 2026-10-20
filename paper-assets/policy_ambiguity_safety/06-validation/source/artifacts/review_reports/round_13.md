---
round: 13
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-22T13:40:01.352462+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 13 (Fresh Review)

**论文**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)
**审稿模式**: Fresh（重新审稿，无历史上下文）
**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）
**圆桌轮次**: 1 轮（交叉后完全收敛，无需 Round 2）

---

## Summary

本文在 τ²-bench 上对 LLM agent 的 policy ambiguity 安全影响进行了 matched-pair 因果研究。构建 300 个 clause pairs（六类 ambiguity taxonomy），在五个模型上评估 2,997 episodes。主要发现：(1) ambiguous clauses 增加违规率 34.0pp (OR=15.1)；(2) 六类形成 margin-dependent risk gradient（incompleteness 为 upper bound，coreferential 为 lower bound）；(3) agents 表现出 Disambiguation Neglect（≤11% awareness）和 systematic nocuity（41.3% 多模型一致违规）。

---

## Strengths

**S1. 首个 matched-pair 因果设计** [R1, R2 共识]
与 DRIP-R（correlational benchmark）不同，matched clause pairs + perturbation control（Δ=−0.67pp, CI containing zero; §4.5）建立了 ambiguity → violation 的因果关系。这在 agent safety 文献中是方法论层面的贡献。

**S2. 统计分析极为详尽透明** [R1, R2 共识]
TOST equivalence testing、bootstrap cluster analysis、variance decomposition、Holm-Bonferroni 校正、seven-margin sensitivity analysis、logistic regression confound control。17 个 appendix 覆盖了几乎所有 robustness check。C3 标注 inconclusive、C4 标注 exploratory——claim 标定诚实。

**S3. Systematic nocuity 概念有理论价值** [R2]
41.3% ambiguous clauses 触发多模型一致性违规（§6.3），扩展 Berry &amp; Kamsties (2004) 框架。对 policy auditing 有直接实践意义。

**S4. Replication 范围广** [R1, R2 共识]
五个主模型 + 两个 replication 模型（Gemini 2.5 Flash, LLaMA 4 Scout），覆盖六家 provider。C1 在七个模型上均成立。ICC=0.919 (within OpenAI family)。

**S5. 与 concurrent work 差异化清晰** [R2]
与 DRIP-R 的三点差异（causality, safety violations vs decision quality, model×type interaction）准确。Related Work 覆盖 NLP ambiguity、RE、agent safety、psycholinguistics 四个方向。

**S6. Type-specific failure mechanism 分析有深度** [R1]
三种机制（structural misparse / information gap-filling / boundary violation）crosscut layer boundary，直接 undermines C3 的 layer distinction，论文诚实承认。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1. Type 仅解释 0.4% variance 与论文核心叙事的根本张力** [R1-N2 + R2-N1, 完全共识]

论文标题 "Not All Policy Ambiguity Is Equal" 和核心叙事围绕六类 taxonomy 展开，但 §5.1 variance decomposition 显示 **type 仅解释 0.4% violation variance**（clause identity 22.4%, model 1.0%, residual 60.8%）。Type 解释力是 clause 的 1/55。这意味着知道一个 ambiguous clause 属于哪种 type 几乎不增加对 violation risk 的预测力——具体措辞远比 type 分类重要。

此外，§1 contribution (2) 将 "60.8% residual" 作为贡献列出不恰当——residual variance 是观测结果，不是贡献。

**两位 Reviewer 独立将此列为 Must-Fix #1，交叉后完全一致**，确认这是 substantive concern 而非 stylistic preference。

要求修改：
- §5.1 正面讨论 0.4% 对 taxonomy 实用价值的含义
- Discussion 加段落解释 taxonomy 价值在于 intervention design（不同 type 需要不同 mitigation strategy）而非 prediction
- 考虑调整标题/framing 更准确反映效应量级（e.g., "clause-level risk with type as secondary predictor"）
- §1 contribution (2) 中 "60.8% residual" reframe 为观测结果而非贡献

**MF-2. Cross-judge type ranking ρ=−0.03 需在主文正面讨论** [R1-N1, R2 交叉 AGREE]

Appendix P 报告跨 judge 组 type ranking Spearman ρ=−0.03 (p=0.96)——两组对六种 type 的严重程度排序完全不一致。论文归因于 agent composition（GPT-4.1 组包含高 auth scope 违规的模型），但 judge bias 和 model composition 效应无法分离。C2 的 pooled type ranking 实际上是 GPT-5.4 judged 3 models vs GPT-4.1 judged 2 models 的 3:2 加权平均。

R2 补充：incompleteness ranks 1-2 in both groups（核心发现 robust），但 mid-tier 内部排序不稳定。

要求修改：
- §5.2 正文正面讨论 ρ=−0.03 及其含义
- 区分 C2 核心发现（incompleteness upper bound, robust across judge groups）vs mid-tier 排序（不稳定）
- 分别报告两组内的 type gradient 结构
- Limitations 中将此列为最主要 measurement limitation

**MF-3. Incompleteness information-addition confound 在 Abstract/Conclusion 应更显式标注** [R2-N2, R1 AGREE with nuance]

Incompleteness 的 unambiguous variant 必然添加新信息，创造 information asymmetry。Token count 是粗糙代理（论文自己承认 "finer-grained semantic measures may reveal different confound structures"）。但 Abstract 仍以 "+49.2pp" 作为 range 上限无 caveat。R1 指出主文 §5.2 已标注 "upper bound—conditional on confound controls"，但 Abstract/Conclusion 缺失。

此外，information quality vs quantity 的差异未讨论：auth scope +36.1 words > incompleteness +34.6 但违规率更低，是有力反证，应提升到正文而非仅在 Appendix O。

要求修改：
- Abstract/Conclusion 明确标注 49.2pp 为 "upper bound, conditional on information-addition confound"
- 考虑在正文报告 confound-free range (+18.7 to +36.0pp)
- 讨论 information quality vs quantity 差异

### Should-Fix（影响评分但不一票否决）

**SF-1. Two-layer structure 缺乏经验支持** [R2-W1, R1 AGREE]
C3 inconclusive（不survive Holm-Bonferroni, controlling for token delta 逆转方向），§6 failure mechanisms crosscut layer boundary。Layer 区分应降级为 organizational convenience 而非理论假设。

**SF-2. LLM-as-judge + OpenAI-family bias** [R2-W2, R1 AGREE]
所有模型由 GPT-5.4 或 GPT-4.1 评判（均 OpenAI family）。C4 结论受此影响。应在 §5.4 而非仅 Limitations 标注此限制。Calibration sample 65% ambiguous 可能高估 judge 一致性。推荐 cross-family judge evaluation。

**SF-3. Error Analysis §6 LLM-coding circularity risk** [R2-W3, R1 AGREE]
五种 failure mode 由 LLM 编码，κ=0.52 (moderate)。用 LLM 编码 LLM 的 failure modes 存在 circularity 风险。Gwet's AC₁=0.62 仍只是 substantial。建议至少一个类别报告人工编码对照。

**SF-4. Disambiguation Neglect 新颖性定位** [R2-W4, R1 AGREE]
贡献在于扩展到 consequential agentic contexts，但论文未显式论证为什么 agentic settings 不同于 non-agentic——关键区别在于 consequentiality（执行动作 vs 仅生成文本），应明确展开。

**SF-5. Domain generalizability framing 不一致** [R2-W5, R1 AGREE]
Abstract "policy-governed agent deployments" vs Conclusion "customer-service deployments"。τ²-bench 仅覆盖 retail + airline。应统一 scope 措辞，添加 domain qualifier。

**SF-6. Margin-dependent gradient 呈现** [R2-W6 + R1-W1, 共识]
TOST gradient 在 ±15pp 才稳定（6/6），±10pp 仅 3/6。Bootstrap k=2 重现率仅 34.3%。Figure 2 给出过于确定的 gradient 印象。应在 §5.2 和 Figure 2 caption 中更突出 margin-dependency。

**SF-7. Auth scope κ=0.385 驱动 C4 但 reliability 最低** [R1-W2, R2 AGREE]
Figure 3 的 52pp range 视觉印象强，但 κ=0.385 最低。排除 auth scope 后 C4 p=0.97。应将 C4 重定位为 auth-scope-specific interaction，Figure 3 caption 标注 reliability caveat。

**SF-8. Per-type human validation CI 过宽** [R1-W4, R2 AGREE]
Scopal κ CI [0.00, 1.00] 完全无信息。Appendix G 末段已注明 "descriptive statistics only"，但仍做 type-level 推断（"Authorization scope has the lowest..."）。

**SF-9. ICC 仅在 OpenAI 家族内计算** [R1-W5, R2 partial REBUT]
R2 指出 ICC 目的是 run-to-run replicability（非 cross-provider consistency），在任一模型组测试即可。但 underlying concern 合理：非 OpenAI 模型的 run-to-run variance 未知。建议 Limitations 中承认 scope 限制。

---

## Reviewer Consensus

两位 Reviewer 在以下问题上**完全独立一致**（交叉后全部 [AGREE]）：

1. **0.4% type variance vs 论文叙事** — 最高优先级修改项
2. **Cross-judge ρ=−0.03 / OpenAI-family confound** — C2 gradient 和 C4 interaction 的可信度
3. **Incompleteness confound framing** — Abstract/Conclusion 需加 caveat
4. **SESOI/gradient margin dependence** — gradient 结构呈现过于确定

---

## Reviewer Divergence

仅 1 处轻微分歧（R1-W5 ICC scope）：
- R1 认为 ICC 仅 OpenAI 是缺陷
- R2 partial [REBUT]：ICC 目的是 run-to-run replicability，scope 限制不影响核心结论
- 共识：在 Limitations 中承认 scope 限制即可

---

## Questions（需要作者澄清）

**Q1** [R2]: 0.4% type variance 下，practitioner 用 taxonomy 做 policy auditing 的具体 workflow 是什么？Binary detection (F1=0.81) 就够了，还是需要 type-level classification (macro F1 仅 0.63, incompleteness F1=0.34)？

**Q2** [R2]: C4 interaction 完全集中在 authorization scope（排除后 p=0.97）。这是否是 auth-scope-specific 现象？C4 的 contribution 应如何重新表述？

**Q3** [R1]: 60.8% residual 主要由什么构成？τ²-bench 中 episode 的 user behavior 变异占多大比例？

**Q4** [R1]: 排除 auth scope 后，剩余 5 个 type 的 cross-judge ranking ρ 是多少？能否区分 "auth scope 特有的 judge disagreement" vs "系统性 judge confound"？

**Q5** [R2]: Mitigation incompleteness prompt sensitivity (v1: −3.4pp vs v2: +14pp)——同模型同类型方向相反是否 undermine type-specific mitigation 的 practical recommendation？

**Q6** [R1, R2]: Coreferential 在 mitigation 和 replication 都缺席，但被用作 confound-free lower bound。如果 coreferential effect 在新 model 上不 replicate，lower bound 结论如何修正？

---

## Missing References

R2 识别，R1 交叉确认：
- **Stengel-Eskin et al. (TACL 2024)** — LLM 处理 scope ambiguity 的实证研究，与 scopal type 直接相关
- **"To Know or Not To Know" (2024)** — LLM self-consistency under ambiguity，与 Disambiguation Neglect 相关
- **Hu et al. (2022)** — LLM implicature processing
- **Ruis et al. (2024)** — LLM pragmatic understanding

---

## External Review

**状态**：未请求（项目未配置 external review）

---

## Visual Layout Check（非评分项）

**状态**: done（0 critical, 1 warning, 13 info）

主要发现：
- **[warning] Pages 4-5**: 连续两页纯文本（§4 Method），无任何 display item。建议插入公式或 matched-pair design 简图打破视觉单调。
- **[info] Page 1**: 首页纯文本（Title + Abstract + Introduction），Figure 1 在第 2 页顶部，可接受。
- **[info] Page 2**: Figure 1 跨双栏全宽，信息传达良好。图内小方框文字偏小（约正文 60%）。
- **[info] Page 3**: Table 1 booktabs 风格规范。
- **[info] Page 6**: Table 2 + Figure 2 同页，视觉密度良好。
- **[info] Page 7**: Figure 3 热力图清晰可读。
- **[info] Page 8**: 纯文本页（§6.2-§8+Conclusion），作为讨论+结论页可接受。
- **[info] Page 9**: Limitations 简短精炼（~1/3 页），References 从页面中部开始。正文在第 8 页结束，**符合 EMNLP 8 页限制**。
- **[info] Appendix**: 高密度但组织清晰，所有表格使用 booktabs。

---

## Overall Assessment

**评分**: 3.5 / 5 (Borderline Conference)
**置信度**: 4/5

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 3.5 | 3.25 |
| Reproducibility | 4.0 | 4.0 | 4.0 |

**总体判断**：方法论贡献扎实——matched-pair 因果设计在 agent safety 领域是首创，统计分析全面透明，claim 标定诚实。但存在一个核心张力：**论文围绕 type-level taxonomy 构建叙事，但数据显示 type 仅解释 0.4% variance，clause wording 才是主要因素**。这从根本上削弱了 taxonomy 作为 practical tool 的定位。加上 cross-judge type ranking 近零相关性 (ρ=−0.03) 威胁 C2 gradient 的外部效度、incompleteness confound 在 headline claims 中标注不充分、domain 受限于两个 customer-service domain，论文在当前 framing 下处于 Borderline Conference。

**升级路径**：如果在 revision 中 (1) 正面讨论 0.4% type variance 并将 taxonomy 价值重新定位为 intervention design 而非 prediction tool，(2) 在 §5.2 正文中讨论 cross-judge ρ=−0.03 并区分 robust vs fragile 结论，(3) Abstract/Conclusion 标注 incompleteness upper bound caveat，(4) 统一 domain scope 措辞——评分有望提升到 4.0 Conference。核心方法论贡献（matched-pair design + perturbation control + systematic nocuity）值得认可。

---

## Detailed Comments（逐节）

### Abstract
- "+49.2pp (incompleteness)" 应标注 "upper bound reflecting an information-addition confound"（当前版本已有此措辞，但位置在从句中不够显眼）
- "policy-governed agent deployments" 过宽，应加 domain qualifier ("in customer-service policy domains")——当前版本 Conclusion 正确收窄但 Abstract 未统一
- "≤11% per-model awareness, 4.6% overall" 两个数字同时出现尚可，但后文 §1 和 §6.2 交替使用时应统一

### §1 Introduction
- Contribution (2) 将 "60.8% residual" 列为贡献不恰当——应 reframe 为观测结果
- Contribution (3) "extending LLM ambiguity-collapse findings to agentic settings" 定位诚实，但应显式论证 agentic settings 的关键区别在于 consequentiality

### §3 Taxonomy
- "Scope of ambiguity" 段落（§3 末段）对理论张力的讨论充分
- Two-layer 假设应降级为 organizational convenience（C3 inconclusive + failure mechanisms crosscut）

### §4 Method
- Matched-pair design 严谨，perturbation control 有效
- §4.4 cross-judge calibration：McNemar p=0.606, κ=0.653 报告规范，但应提及 calibration sample 65% ambiguous 的组成
- §4.6 SESOI ±15pp：domain anchoring 合理，但应更明确讨论 margin-dependency 对 C2 结论的影响

### §5 Results
- §5.1 (C1)：34.0pp effect 强且 robust，方差分解是重要发现但需要正面讨论 0.4% type variance 的含义
- §5.2 (C2)：应在正文讨论 Appendix P 的 ρ=−0.03，区分 robust 核心发现 vs fragile 排序
- §5.3 (C3)：标注 inconclusive 是正确的——建议加 1 句解释 failure mechanisms 也不支持 layer distinction
- §5.4 (C4)：应重定位为 auth-scope-specific interaction；Figure 3 caption 加 reliability caveat

### §6 Error Analysis
- Systematic nocuity 是新颖且有价值的概念
- Failure mode coding reliability (κ=0.52) 应承认限制，讨论 LLM-coding circularity risk
- Disambiguation Neglect：应展开 agentic vs non-agentic 的 consequentiality 区别

### §7 Discussion
- Differential nocuity 应定位为 hypothesis 而非 framework
- Mitigation experiment 的 prompt sensitivity（同类型方向相反）是重要发现，应更充分讨论
- Practical implications 应正面承认 type-level auditing 的局限性

### §8 Conclusion
- 数字准确，但应与 Abstract 统一 domain scope 措辞

### Limitations
- 覆盖了 scope、measurement、confounds 三个维度
- 应将 cross-judge ρ=−0.03 列为最主要 measurement limitation
- 应承认 ICC scope 限制（仅 OpenAI family）

### Appendix
- 17 个 appendix 组织清晰但缺少 clause pair 示例
- Appendix G per-type κ 应明确标注 descriptive only
- §5.1 方差分解方法（nested ANOVA? LMM?）应说明