# Director coordination — Part 8 of 11

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

[← Part 7](part-007.md) · [Transcript overview](../director-coordination.md) · [Part 9 →](part-009.md) · [Structured JSON](../../../sessions/0e/0e806c5d99edfa05e2ae.json)

## Round 209

### User

_source line 2200 · 2026-05-23T09:43:21.532419+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5（Borderline Conference）
**一句话总结**: 论文以 matched-pair 因果设计研究 policy ambiguity 对 LLM agent 安全的影响，实验设计严谨、控制充分，但合成刺激材料与真实场景的效应量差距（34pp vs. 12.6pp）、跨领域 type ranking 的零相关（ρ=0.26）、以及 authorization scope 的构念效度问题，削弱了 taxonomy 的实践价值和结论的泛化性。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心因果 claim（C1）由 matched-pair 设计充分支撑，perturbation control 有效排除替代解释；但生态效度差距（2.7×）和 60.8% 残差方差构成方法论缺口 |
| Excitement | 3.5/5 | 话题时效性强（LLM agent safety × policy ambiguity）、因果设计在该领域新颖；合成材料的实践可迁移性不确定，降低了兴趣 |
| Reproducibility | 4/5 | τ²-bench 公开可用，代码和数据计划开源（Data and Code Availability 段），prompt 模板在 Appendix B 给出；ICC 仅 OpenAI family 内测算限制了跨 provider 可复制性评估 |
| Confidence | 4/5 | 本人在实验设计、因果推断和统计方法方面有扎实的评审经验 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 合成刺激 vs. 自然歧义效应量差距（2.7×）缺乏桥接分析

- 具体位置：Abstract（"increasing violation rates by 31 percentage points in confound-free types (34.0pp across all six types)"）、Section 7 Ecological validity 段（一句话承认）、Appendix Z（SOPBench +12.6pp）
- 问题：论文的 headline 数字 34.0pp 来自合成构造的 clause pairs，SOPBench 自然语境复制仅 +12.6pp——差距 2.7 倍。Abstract 和 Conclusion 均以 34.0pp 和 31.0pp（confound-free）作为核心数字。Discussion §7 的 Ecological validity 段仅一句话承认 "our synthetic design establishes causal mechanisms but overestimates naturalistic effect sizes"，未分析差距来源：(a) SOPBench 使用 constraint-level（而非 clause-level）measurement 导致粒度差异？(b) 自然政策文档中周围子句提供消歧上下文稀释效应？(c) 合成歧义系统性偏极端？论文没有提供从业者应使用哪个数字的指导。
- 为什么影响接收：如果真实效果更接近 12.6pp（而非 34pp），论文关于 "ambiguity increases violations by ≈30pp" 的 framing 可能误导实践决策。因果机制的识别与效应量的估算是不同贡献，论文需要更清晰地区分二者。
- 建议修改方向：(1) Abstract/Conclusion 同时报告合成上界（34pp）和自然下界（12.6pp）；(2) 分析 2.7× 差距的可能来源（至少 2-3 句）；(3) 明确论文核心贡献在于因果机制识别和 taxonomy 构建，而非精确效应量估算。

**N2** [critical] 跨领域 ρ=0.26 (p=0.62) 与 taxonomy 泛化性 framing 矛盾

- 具体位置：Section 7 Discussion 第一段（"cross-domain type ranking is near chance (ρ = 0.26, p = 0.62), driven by conditional precedence (Δ = 22.0pp retail vs. airline)"）、Abstract（"a six-type taxonomy organized into two layers—linguistic and specification"，暗示通用性）、Section 1 Introduction（"enabling type-targeted diagnostics for policy-governed deployments"）
- 问题：论文将 taxonomy 定位为通用诊断工具——Abstract 说 "enabling type-targeted diagnostics"，Introduction 说 "establishing the taxonomy as a diagnostic instrument"。但 type ranking 在 τ²-bench 的两个领域（retail vs. airline）之间 ρ=0.26 (p=0.62)，本质上是零相关。这意味着在 retail 中 authorization scope 是高风险类型，在 airline 中可能不是——从业者无法将一个领域的 type prioritization 迁移到另一个领域。Discussion 承认 "deployment in other domains requires independent type-effect calibration"，但 Abstract 和 Introduction 完全没有反映这一关键限制。
- 为什么影响接收：论文的主要卖点之一是 taxonomy 的诊断实用价值。如果 type ordering 是 domain-specific 的，taxonomy 的价值降级为"提供一个 checklist"而非"提供优先级指导"——这大幅削弱了贡献的叙事。
- 建议修改方向：(1) Abstract 加入 domain-specificity 限定词，例如 "within-domain type-targeted diagnostics"；(2) 明确区分 binary effect 的跨领域稳健性（p=0.187, 持续显著）vs. type ordering 的领域依赖性；(3) 在 Introduction 的贡献列表中限定 taxonomy 的适用范围。

**N3** [critical] Authorization scope 的构念效度不足——κ=0.385、52pp 模型间变异、驱动多个结果不一致

- 具体位置：Table 2 脚注 ‡（κ=0.385, n≈17）、Figure 3 heatmap（Auth. Scope 列：Claude 12% vs. GPT-5.4 64% vs. DeepSeek 60%）、Section 5.2（"two-group rankings are discordant (ρ=0.09), driven by authorization scope. Excluding it, ρ=0.90 (p=0.037)"）
- 问题：Authorization scope 在六类中系统性异常：(a) inter-judge agreement 最低（κ=0.385，低于 fair agreement 的 0.40 标准，其他五类范围 0.644–0.875）；(b) 模型间变异最大（52pp 跨度，Claude 12% vs. DeepSeek 60%）；(c) 单独驱动 cross-judge ranking discordance（排除后 ρ 从 0.09 升至 0.90, p=0.037）；(d) 在 C4 中单独驱动 model×type interaction（排除后 interaction vanishes, p=0.97）。论文将此归因于 "construct subjectivity—whether investigating an unauthorized request constitutes a violation"（Section 5.2），但这实质上承认 authorization scope 的操作定义在不同 judge 和 model 之间不一致。一个在 taxonomy 中占 1/6 的类型，其信度低于 fair agreement，且驱动论文中多个关键结果的不一致性（C2 discordance、C4 interaction），这威胁到整个 taxonomy 的内部一致性。
- 为什么影响接收：如果 authorization scope 的"歧义效应"实际上部分是 judge disagreement 和 model-specific safety training 的 artifact，那么 6 类 taxonomy 的基础被削弱。论文需要证明 authorization scope 作为一个独立类型的合法性，或者在报告结果时将其单独处理。
- 建议修改方向：(1) 在 main text（而非仅脚注）中用一个完整段落讨论 authorization scope 的信度问题及其对结论的影响；(2) 系统性地报告 "5-type excluding auth scope" 的所有核心结果作为 robustness check；(3) 讨论是否需要将 authorization scope 的操作定义从 "agent exceeds permission boundaries" 细化为更可操作的判定标准。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] ICC=0.919 仅在 OpenAI family 内计算，"Reproducibility" 标题有误导

- 具体位置：Section 4.5 "Reproducibility" 段（method.tex line 30："ICC is computed within the OpenAI family; cross-provider stability is supported by C1 consistency across all seven models"）
- 问题：ICC 基于 30 clause pairs × 2 OpenAI models × 3 replicates 计算，衡量的是同一 model family 内的 test-retest reliability。但 "Reproducibility" 标题暗示跨 provider 的可复制性。论文补充的 "C1 consistency across all seven models" 仅说明所有模型效应方向一致，不等于 effect size 的定量可复制性。例如，LLaMA-4-Scout 的 Δpp=+20.0 与 GPT-5.4 的 +39.0 方向一致但量级差 19pp。
- 建议：(1) 标题改为 "Within-family test-retest reliability" 或类似措辞；(2) 补充 7 模型间 Δpp 的变异系数 (CV) 或 I² heterogeneity 以量化跨 provider effect size 一致性。

**W2** [warning] 60.8% 残差方差中 ~46% 系统性部分未充分探索

- 具体位置：Section 5.1（方差分解）、Section 7 Discussion 第一段（"the large systematic residual likely reflects clause×context interactions invisible to type-level analysis"）、Appendix AB（within-provider ICC = 0.749）
- 问题：方差分解 22.4%（clause）+ 15.8%（condition）+ 1.0%（model）+ 0.4%（type）+ 60.8%（residual）= 100%。其中 residual 的 ~46% 被估计为 systematic（based on ICC=0.749）。这意味着论文建模的因素仅解释 39.2% 的方差，而 ~46% 是可重复但未建模的。论文归因于 "clause×context interactions"，但未进一步调查——例如，是否可以加入 clause length、policy document identity、或 conversation trajectory 的 random effect？Temperature=0 应减少采样随机性，那 ~15% stochastic variance 的来源是什么？（user simulator 的随机性？API non-determinism？）
- 建议：至少讨论 2-3 个可能的系统性残差来源，并说明为什么进一步分解不可行或超出范围。

**W3** [warning] Failure mode 分析（Section 6）的循环性风险和证据强度过度

- 具体位置：Section 6 第一段（Gwet's AC₁=0.62, Cohen's κ=0.52；human κ=0.15）、Figure 4 caption（"NMI = 0.23, Cramér's V = 0.45"）
- 问题：(a) LLM-coded failure modes (κ=0.52) vs. human-coded (κ=0.15) 的巨大差距表明 LLM 间的"一致性"可能反映共享的系统性偏差而非真实的 mechanism 区分。论文承认 NMI "should be interpreted as an upper bound"，但 Section 6 的叙事仍然使用强断言——"three mechanistically distinct failure patterns"、"the five-model data reveal" 等。(b) 论文指出 "two of the six type–mechanism mappings reflect partial definitional affinity (authorization scope→boundary violation, incompleteness→gap-filling)"，即 1/3 的关联可能是 tautological（类型定义本身暗示了机制）。
- 建议：(1) Section 6 开头加入 caveat 段落，明确 exploratory + LLM-coded 的局限性；(2) 将 "mechanistically distinct" 等表述降级为 "categorically distinct in LLM coding" 或类似措辞。

**W4** [warning] Incompleteness confound 控制的间接性

- 具体位置：Appendix F（logistic regression: β_token = +0.027, p=0.003）、Section 5.1（"The incompleteness effect (+49.2pp) is an upper bound"）
- 问题：论文的 confound 控制策略是间接的：(a) token count regression 显示更长的 clause 预测更多违规（与 information-addition 假说方向相反），但 token count 是信息量的粗糙代理——添加 10 个高信息量 token vs. 10 个低信息量 token 效果不同；(b) coreferential（信息差 δ=0）提供 18.7pp 的 confound-free lower bound，这有说服力但仅适用于一个类型。论文自己在 Appendix F 末尾承认 "finer-grained semantic measures may reveal different confound structures"。一个更直接的控制是构造 information-addition-only pairs（添加不解决歧义的等量信息），但这超出当前实验范围。
- 建议：(1) Main text 中更明确地讨论 token count 代理的局限性（目前仅在 appendix 末尾一句话）；(2) 将 incompleteness 的 49.2pp 效应在 Abstract/Conclusion 中标记为 "upper bound, confounded" 而非简单包含在 34.0pp pooled number 中。

**W5** [warning] Temperature=0 限制了生态效度

- 具体位置：Section 4.3（"temperature = 0, top_p = 1"）、Limitations（"stochastic sampling remains untested"）
- 问题：所有实验在 temperature=0 下运行。实际部署通常 temperature > 0，这会增加输出多样性并可能改变歧义处理——例如，temperature > 0 下 model 可能更频繁地在多个解读之间切换（amplifying ambiguity effects）或更倾向于保守解读（dampening effects）。Limitations 段仅一句话提到，没有讨论方向性预期。
- 建议：至少讨论 temperature 的可能影响方向，最好承诺 future work 中进行 temperature sensitivity pilot。

---

## 小问题（不影响接收）

1. **Table 2 信息密度过高**：7 列数值 + TOST Tier + p 值，建议将 Tier 和 p 移至 appendix，main text 仅保留 pooled Δpp 和 CI
2. **Abstract 中 "Cramér's V = 0.45 vs. 0.14" 缺乏即时上下文**：读者直到 Section 6 才能理解这两个数字分别对应 type→mechanism 和 type→violation rate；建议 abstract 中简要说明
3. **"Nocuous" 术语的含义反转**：论文采用 Berry & Kamsties (2004) 的 "nocuous"，但他们定义 nocuous ambiguity 为 "different stakeholders arrive at different interpretations"（divergence），而本文指 models converge on wrong interpretation。Section 6.3 解释了这一反转但标题 "Systematic Nocuity" 可能引起混淆
4. **Two-group ranking discordance (ρ=0.09) 的影响被低估**：Section 5.2 仅在段落中间提及，但这一结果对 C2 (type partial ordering) 的可信度有重要影响——它说明 judge group 选择影响 type ranking。建议在 Section 5.2 中给予更显著的位置
5. **LaTeX 源文件 vs. PDF 中 condition variance 数值不一致**（LaTeX: 15.8%, 需确认 PDF 是否一致）

---

## 主要优势

1. **因果设计的稀缺性和严谨性**：在 LLM agent safety 领域，绝大多数工作是相关性分析或 benchmark 评估。本文的 matched-pair 设计（每对 clause 只改变歧义，保持 policy intent 不变）是罕见的因果推断尝试，perturbation control（Δ_perturb = -0.67pp）有效排除了表面文本扰动的替代解释

2. **模型覆盖广度和 provider 多样性**：5 主模型 + 2 复制模型，覆盖 6 个 provider（OpenAI, Anthropic, Alibaba, DeepSeek, Google, Meta）和 2 种架构风格（dense, MoE）。C1 在所有 7 模型上显著，增强泛化性

3. **控制实验的密度和透明度**：TOST 7-margin sensitivity（Table 3, Appendix A）、bootstrap clustering（Appendix I）、incompleteness confound regression（Appendix F）、cross-judge 3-family validation（Appendix AA）、severity threshold comparison（Appendix C）——robustness check 的覆盖范围远超同类论文

4. **Taxonomy 价值的精准定位**：论文清晰区分 "type explains 0.4% of violation variance"（预测能力弱）vs. "V=0.45 for type→mechanism"（诊断价值强），避免了过度声明。这一 framing 本身就是一个有洞察力的贡献

5. **方法论诚实度**：SESOI 标为 "pragmatic default, not a principled domain-anchored threshold"；incompleteness 标为 "upper bound, subject to information-addition confound"；cross-domain ρ=0.26 的如实报告——论文在多处主动标记了自身局限

6. **Disambiguation neglect 现象的发现**（Section 6.2）：4.6% 的 ambiguity awareness rate 是一个有实践意义的发现——agents 几乎从不识别歧义就直接行动，这指向 "先检测再行动" 的干预方向

---

## Questions to Authors

1. 合成效应 (34pp) 和 SOPBench 效应 (12.6pp) 之间 2.7× 的差距，您认为主要来源是什么？SOPBench 使用 constraint-level measurement 而非 clause-level，这一粒度差异是否足以解释全部差距？

2. Authorization scope 的 κ=0.385 是否暗示该类型需要重新操作定义？具体来说，"investigating an unauthorized request" 是否应被归类为 violation？如果排除 authorization scope，C2 (type ordering) 和 C4 (model×type interaction) 的结论是否有实质性变化？

3. 60.8% 残差方差中 ~46% 系统性部分，您是否有初步证据表明其主要来源是 clause×context interaction（vs. user simulator behavior variability, vs. prompt template effects）？

4. Temperature=0 下 permissive attractor (77%) 在 temperature>0 时是否可能改变？直觉上 sampling randomness 是否会打破 convergent violation pattern？

5. Discussion 中 within-provider ICC=0.749（用于估计 systematic residual）与 Section 4.5 中 OpenAI-family ICC=0.919——这两个 ICC 指标计算范围不同，能否澄清二者的关系和分别对应的实验设置？

---

## Missing References

- **Femmer et al. (2017)**：Requirements Engineering 领域自动歧义检测的综述性工作（"Requirements quality is quality in use", RE Journal）——与论文的 detection experiment (Appendix D) 高度相关
- **Anthropic Model Spec / Constitutional AI 系列**：与 policy-governed agent behavior 的 alignment 方向直接相关，论文未引用
- **2025-2026 LLM agent safety 最新 benchmark**：论文引用了 τ²-bench, SOPBench, AgentHarm, 但可能遗漏了 2026 年的最新工作（如有的话）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2201 · 2026-05-23T09:44:06.755921+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿报告\n\n**Overall**: 3.5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] 合成刺激 vs. 自然歧义效应量差距（2.7×）缺乏桥接分析\n- Abstract 和 Conclusion 以 34.0pp/31.0pp 作为 headline，SOPBench 仅 +12.6pp。Discussion §7 仅一句话承认 \"overestimates naturalistic effect sizes\"，未分析差距来源。论文没有提供从业者应使用哪个数字的指导。\n- 建议：Abstract/Conclusion 同时报告合成上界和自然下界；分析 2.7× 差距来源。\n\n**N2** [critical] 跨领域 ρ=0.26 (p=0.62) 与 taxonomy 泛化性 framing 矛盾\n- Type ranking 在 retail vs. airline 之间零相关。Abstract 说 \"enabling type-targeted diagnostics\" 暗示通用性，但实际上从业者无法跨领域迁移 type prioritization。\n- 建议：Abstract 加 domain-specificity 限定；区分 binary effect 跨领域稳健性 vs. type ordering 领域依赖性。\n\n**N3** [critical] Authorization scope 构念效度不足——κ=0.385、52pp 模型间变异、驱动多个结果不一致\n- Auth scope 在六类中系统性异常：inter-judge κ 最低（0.385）、模型间变异最大（52pp）、单独驱动 cross-judge ranking discordance（排除后 ρ 从 0.09→0.90）、驱动 C4 interaction（排除后 p=0.97）。\n- 建议：main text 完整段落讨论 auth scope 信度；系统报告 5-type excluding auth scope 的所有核心结果。\n\n### Should-Fix 问题\n\n**W1** ICC=0.919 仅 OpenAI family，\"Reproducibility\" 标题有误导。建议改标题 + 补跨 provider CV。\n\n**W2** 60.8% 残差方差中 ~46% 系统性部分未充分探索。建议讨论 2-3 个可能来源。\n\n**W3** Failure mode 分析循环性风险——LLM-coded κ=0.52 vs human κ=0.15，且 1/3 关联可能 tautological。建议降级表述强度。\n\n**W4** Incompleteness confound 控制的间接性——token count 是粗糙代理。建议 main text 讨论局限性。\n\n**W5** Temperature=0 限制生态效度。建议讨论 temperature 的可能影响方向。\n\n### 小问题\n1. Table 2 信息密度过高\n2. Abstract 中 Cramér's V 缺乏即时上下文\n3. \"Nocuous\" 含义反转可能引起混淆\n4. Two-group ranking discordance (ρ=0.09) 影响被低估\n5. LaTeX vs PDF condition variance 数值需确认一致性\n\n### 主要优势\n1. 因果设计稀缺且严谨\n2. 模型覆盖广（7 models, 6 providers）\n3. 控制实验密度和透明度\n4. Taxonomy 价值精准定位（0.4% rate vs V=0.45 mechanism）\n5. 方法论诚实度\n6. Disambiguation neglect 发现\n\n### Questions\n1. 34pp vs 12.6pp 差距的主要来源？\n2. Auth scope κ=0.385 是否需要重新定义？排除后 C2/C4 变化？\n3. 46% 系统性残差来源？\n4. Temperature>0 是否改变 permissive attractor？\n5. ICC=0.749 vs ICC=0.919 的关系？\n\n### Missing References\n- Femmer et al. (2017) RE 自动歧义检测\n- Anthropic Model Spec / Constitutional AI\n- 2026 最新 agent safety benchmarks",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿报告\n\n**Overall**: 3.5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] 合成刺激 vs. 自然歧义效应量差距（2.7×）缺乏桥接分析\n- Abstract 和 Conclusion 以 34.0pp/31.0pp 作为 headline，SOPBench 仅 +12.6pp。Discussion §7 仅一句话承认 \"overestimates naturalistic effect sizes\"，未分析差距来源。论文没有提供从业者应使用哪个数字的指导。\n- 建议：Abstract/Conclusion 同时报告合成上界和自然下界；分析 2.7× 差距来源。\n\n**N2** [critical] 跨领域 ρ=0.26 (p=0.62) 与 taxonomy 泛化性 framing 矛盾\n- Type ranking 在 retail vs. airline 之间零相关。Abstract 说 \"enabling type-targeted diagnostics\" 暗示通用性，但实际上从业者无法跨领域迁移 type prioritization。\n- 建议：Abstract 加 domain-specificity 限定；区分 binary effect 跨领域稳健性 vs. type ordering 领域依赖性。\n\n**N3** [critical] Authorization scope 构念效度不足——κ=0.385、52pp 模型间变异、驱动多个结果不一致\n- Auth scope 在六类中系统性异常：inter-judge κ 最低（0.385）、模型间变异最大（52pp）、单独驱动 cross-judge ranking discordance（排除后 ρ 从 0.09→0.90）、驱动 C4 interaction（排除后 p=0.97）。\n- 建议：main text 完整段落讨论 auth scope 信度；系统报告 5-type excluding auth scope 的所有核心结果。\n\n### Should-Fix 问题\n\n**W1** ICC=0.919 仅 OpenAI family，\"Reproducibility\" 标题有误导。建议改标题 + 补跨 provider CV。\n\n**W2** 60.8% 残差方差中 ~46% 系统性部分未充分探索。建议讨论 2-3 个可能来源。\n\n**W3** Failure mode 分析循环性风险——LLM-coded κ=0.52 vs human κ=0.15，且 1/3 关联可能 tautological。建议降级表述强度。\n\n**W4** Incompleteness confound 控制的间接性——token count 是粗糙代理。建议 main text 讨论局限性。\n\n**W5** Temperature=0 限制生态效度。建议讨论 temperature 的可能影响方向。\n\n### 小问题\n1. Table 2 信息密度过高\n2. Abstract 中 Cramér's V 缺乏即时上下文\n3. \"Nocuous\" 含义反转可能引起混淆\n4. Two-group ranking discordance (ρ=0.09) 影响被低估\n5. LaTeX vs PDF condition variance 数值需确认一致性\n\n### 主要优势\n1. 因果设计稀缺且严谨\n2. 模型覆盖广（7 models, 6 providers）\n3. 控制实验密度和透明度\n4. Taxonomy 价值精准定位（0.4% rate vs V=0.45 mechanism）\n5. 方法论诚实度\n6. Disambiguation neglect 发现\n\n### Questions\n1. 34pp vs 12.6pp 差距的主要来源？\n2. Auth scope κ=0.385 是否需要重新定义？排除后 C2/C4 变化？\n3. 46% 系统性残差来源？\n4. Temperature>0 是否改变 permissive attractor？\n5. ICC=0.749 vs ICC=0.919 的关系？\n\n### Missing References\n- Femmer et al. (2017) RE 自动歧义检测\n- Anthropic Model Spec / Constitutional AI\n- 2026 最新 agent safety benchmarks",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 2202 · 2026-05-23T09:44:34.151103+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27395
}
```

</details>

---


### Tool call

_source line 2203 · 2026-05-23T09:44:34.302366+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿报告\n\n**Overall**: 3.5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] Taxonomy 增量贡献论证不足——与 Li et al. (2024) 11-type taxonomy 的关系\n- §3 仅一句话解释 11→6 condensation 逻辑。读者无法判断哪 5 types 被排除、排除标准是理论还是实验便利性驱动的。Appendix AC 的 real-world audit 数据没被用来论证覆盖度。\n- 建议：增加 11→6 映射表格 + 用 audit 数据论证覆盖度。\n\n**N2** [critical] \"Ambiguity\" 广义使用与 NLP 社区标准定义的张力\n- 将 incompleteness、normative conflict、vagueness 都纳入\"ambiguity\"。NLP 传统中 ambiguity 严格指多合法解析。论证 \"LLM agents process all six types identically\" 不充分——处理方式相同不意味分类应合并。\n- 建议：考虑上位术语如 \"policy specification defects\"；至少讨论与 NLP 传统分类的关系。\n\n### Should-Fix 问题\n\n**W1** C3 inconclusive 但 taxonomy 仍按 two-layer 组织——理论 vs 经验支撑的张力。建议明确 two-layer 是组织框架而非经验发现。\n\n**W2** 合成 (34pp) vs SOPBench (12.6pp) ecological validity gap 讨论不充分。建议 Discussion 用 2-3 句正式讨论。\n\n**W3** \"Nocuous\" 术语的概念延伸过度——Berry & Kamsties 的 divergent interpretation vs 本文的 convergent error。建议更早说明扩展定义。\n\n**W4** Disambiguation neglect (4.6%) 的新颖性不清晰——LLM 不请求澄清是已知现象。建议说明增量贡献。\n\n**W5** 数字密度过高，叙事线索被淹没。建议部分详细数字移至 appendix。\n\n### 小问题\nM1: Table 1 Disambig Channel 描述过简\nM2: Figure 2 \"(App)\" 标记含义要到 §4.5 才解释\nM3: Limitations 与正文少量重复\nM4: arXiv preprint 格式不统一\n\n### 主要优势\nS1: Matched-pair 因果设计是方法论进步\nS2: Claim 校准得当（confound-free range, upper bound 标记, C3 坦诚报告）\nS3: 多层次复制增强可信度\nS4: Type→mechanism 发现有理论价值\nS5: Real-world policy audit 提供初步外部效度\n\n### Questions\nQ1: DRIP-R 的 \"no single correct resolution\" vs 本文 matched-pair ground truth——如何推广到真实歧义？\nQ2: 排除 incompleteness 后 31.0pp 是否仍有实践意义？\nQ3: Failure mechanism 分类是否 post-hoc？type→mechanism 是否有 circular reasoning？\nQ4: Claude auth scope 64% 异常是否影响 pooled estimates？\n\n### Missing References\n- 已引用但讨论不足：DRIP-R 正文缺乏方法论差异对比\n- 可能遗漏：Gao-Arch et al. (2026) \"Ambiguity collapse in LLMs\" 与 systematic nocuity 高度相关",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿报告\n\n**Overall**: 3.5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] Taxonomy 增量贡献论证不足——与 Li et al. (2024) 11-type taxonomy 的关系\n- §3 仅一句话解释 11→6 condensation 逻辑。读者无法判断哪 5 types 被排除、排除标准是理论还是实验便利性驱动的。Appendix AC 的 real-world audit 数据没被用来论证覆盖度。\n- 建议：增加 11→6 映射表格 + 用 audit 数据论证覆盖度。\n\n**N2** [critical] \"Ambiguity\" 广义使用与 NLP 社区标准定义的张力\n- 将 incompleteness、normative conflict、vagueness 都纳入\"ambiguity\"。NLP 传统中 ambiguity 严格指多合法解析。论证 \"LLM agents process all six types identically\" 不充分——处理方式相同不意味分类应合并。\n- 建议：考虑上位术语如 \"policy specification defects\"；至少讨论与 NLP 传统分类的关系。\n\n### Should-Fix 问题\n\n**W1** C3 inconclusive 但 taxonomy 仍按 two-layer 组织——理论 vs 经验支撑的张力。建议明确 two-layer 是组织框架而非经验发现。\n\n**W2** 合成 (34pp) vs SOPBench (12.6pp) ecological validity gap 讨论不充分。建议 Discussion 用 2-3 句正式讨论。\n\n**W3** \"Nocuous\" 术语的概念延伸过度——Berry & Kamsties 的 divergent interpretation vs 本文的 convergent error。建议更早说明扩展定义。\n\n**W4** Disambiguation neglect (4.6%) 的新颖性不清晰——LLM 不请求澄清是已知现象。建议说明增量贡献。\n\n**W5** 数字密度过高，叙事线索被淹没。建议部分详细数字移至 appendix。\n\n### 小问题\nM1: Table 1 Disambig Channel 描述过简\nM2: Figure 2 \"(App)\" 标记含义要到 §4.5 才解释\nM3: Limitations 与正文少量重复\nM4: arXiv preprint 格式不统一\n\n### 主要优势\nS1: Matched-pair 因果设计是方法论进步\nS2: Claim 校准得当（confound-free range, upper bound 标记, C3 坦诚报告）\nS3: 多层次复制增强可信度\nS4: Type→mechanism 发现有理论价值\nS5: Real-world policy audit 提供初步外部效度\n\n### Questions\nQ1: DRIP-R 的 \"no single correct resolution\" vs 本文 matched-pair ground truth——如何推广到真实歧义？\nQ2: 排除 incompleteness 后 31.0pp 是否仍有实践意义？\nQ3: Failure mechanism 分类是否 post-hoc？type→mechanism 是否有 circular reasoning？\nQ4: Claude auth scope 64% 异常是否影响 pooled estimates？\n\n### Missing References\n- 已引用但讨论不足：DRIP-R 正文缺乏方法论差异对比\n- 可能遗漏：Gao-Arch et al. (2026) \"Ambiguity collapse in LLMs\" 与 systematic nocuity 高度相关",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 2204 · 2026-05-23T09:44:35.665447+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1363
}
```

</details>

---


### Assistant

_source line 2205 · 2026-05-23T09:44:38.724893+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 210

## Round 210

2 recorded events


### User

_source line 2206 · 2026-05-23T09:44:41.641819+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿完成。已向 Review Director 提交完整审稿报告，评分 **Overall 3.5（Borderline Conference）**，包含：

- **3 个 Must-Fix**：合成 vs. 自然效应量差距（34pp vs. 12.6pp）缺乏桥接分析、跨领域 ρ=0.26 与 taxonomy 泛化性 framing 矛盾、authorization scope 构念效度不足（κ=0.385）
- **5 个 Should-Fix**：ICC 标题误导、60.8% 残差方差未充分探索、failure mode 分析循环性风险、incompleteness confound 间接性、temperature=0 生态效度限制
- **5 个 Minor**：Table 2 密度、Abstract 上下文缺失、nocuous 术语反转、ρ=0.09 影响低估、数值一致性
- **6 条优势**、**5 个 Questions to Authors**、**3 条 Missing References**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2207 · 2026-05-23T09:44:47.306657+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 211

## Round 211

2 recorded events


### User

_source line 2208 · 2026-05-23T09:47:02.775343+00:00_

[Reviewer 1 审稿意见]:
## 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: Taxonomy 增量贡献论证不足——11→6 condensation**

R2 认为 §3 仅一句话解释 11→6 缩减。实际上 §3 提供了三条明确的设计标准：(1) prior RE literature 中的理论动机（cite Massey et al., 2014; Berry et al., 2004）；(2) amenability to matched-pair construction without altering clause semantics；(3) mutual exclusivity for unambiguous IV assignment。此外，§3 明确指出了被排除类型及原因："Types such as ellipsis and pragmatic implicature were excluded because they resist minimal-pair construction within the single-clause policy format。" 这不是一句话，而是一个完整的选择逻辑框架。

不过，R2 关于增加 11→6 映射表格的建议有操作价值——读者确实需要快速查看哪些类型被排除及各自原因。但这应归为 **Should-Fix** 而非 Must-Fix，因为现有论证逻辑完整，缺的是呈现形式上的便利性。

关于用 Appendix AC 的 audit 数据论证覆盖度：audit 数据的目的是初步外部效度验证（real-world prevalence），而非 taxonomy 选择的依据。用 prevalence 来 justify 类型选择会引入循环论证——"我们选了这些类型因为它们在 audit 中出现了" 而 audit 本身使用的就是这些类型。

**严重性判定：Should-Fix，不应为 Must-Fix。** 论证逻辑完备，映射表格可改善可读性但不影响接收决定。

---

**[REBUT] R2-N2: "Ambiguity" 广义使用与 NLP 社区标准定义的张力**

R2 的学术关切合理：NLP 传统中 ambiguity 严格指"同一表达有多个合法解析"，与 vagueness（梯度边界）和 incompleteness（缺失信息）有区分。但论文的处理比 R2 描述的更充分：

1. **操作定义有文献支撑**。§3 "Scope of 'ambiguity'" 段落明确采用 Wasow et al. (2005) 的广义操作定义，并解释为何在 LLM agent 语境下采用包容性定义——"LLM agents process all six types identically—committing to a single interpretation without flagging uncertainty—and the resulting violations produce comparable safety impact despite distinct mechanisms."

2. **RE 传统中的合理性**。论文 cite Dalpiaz et al. (2018) 表明 ambiguity 和 incompleteness 在 requirements specifications 中频繁共现，且 Berry & Kamsties (2004) 的 "nocuous ambiguity" 框架本身就涵盖了超越严格语言学定义的 specification defects。

3. **论文自身做了区分**。§3 明确说 "Strictly, neither constitutes linguistic ambiguity"（指 incompleteness 和 conditional precedence），但论证了在 agent safety 语境下合并处理的理由。

R2 建议使用 "policy specification defects" 作为上位术语。但这会削弱论文与 NLP/CL 社区的对话——"ambiguity" 是连接 NLP 和 RE 两个领域的桥梁术语。改用 "defects" 会将论文推向纯 SE 方向，降低 EMNLP 读者的兴趣。

**严重性判定：Should-Fix，不应为 Must-Fix。** 建议在 §3 中增加 1-2 句话明确讨论与 NLP 传统分类的关系（目前只有 "Strictly, neither constitutes linguistic ambiguity" 一句），但无需更改术语。

---

### Should-Fix 问题

**[AGREE] R2-W1: C3 inconclusive 但 taxonomy 仍按 two-layer 组织**

同意。C3 (layer effect) 未通过 Holm-Bonferroni 校正（p=0.017, threshold 0.0125, Section 5.2），但 taxonomy 仍以 linguistic/specification 两层为组织框架（Table 1, §3）。论文确实需要更明确地说明 two-layer 结构是基于理论的组织框架（sourced from RE literature typologies: Massey et al., 2014; Berry et al., 2004），而非经验发现。目前这一区分隐含在 §3 的叙事中但未被显式阐述。我在自己的审稿中未单独提出此问题，认为 R2 的发现有价值。

---

**[AGREE] R2-W2: 合成 (34pp) vs SOPBench (12.6pp) ecological validity gap**

强烈同意——这也是我的 **Must-Fix N1**。R2 将其归为 Should-Fix，但我认为严重性应更高。差距 2.7 倍且 Abstract/Conclusion 仅使用 34pp 作为 headline，对从业者有误导风险。Discussion §7 的 Ecological validity 段仅一句话。至少应：(1) Abstract 同时报告两个数字；(2) 分析 2.7× 差距来源（measurement granularity、context effects）。

---

**[AGREE] R2-W3: "Nocuous" 术语的概念延伸**

同意。我在自己的审稿中将此列为小问题（Minor #3）。R2 的 framing 更精确——Berry & Kamsties (2004) 的 nocuous 指 stakeholder divergence（不同人有不同解读），而本文指 model convergence on wrong interpretation。Section 6.3 虽然解释了这一反转（"but inverted: our agents exhibit convergent rather than divergent errors"），但出现得太晚（第 7 页）。建议在 §1 首次使用 "nocuous" 时就简要说明这一概念延伸。

---

**[REBUT] R2-W4: Disambiguation neglect (4.6%) 的新颖性**

R2 认为 "LLM 不请求澄清是已知现象"。但论文的贡献不在于发现 "LLM 不问问题" 这一现象本身，而在于三个层面的增量：

1. **因果框架下的量化**。4.6% awareness rate 是在 matched-pair causal design 中测量的——不是 "LLM 是否会问澄清问题" 的泛泛观察，而是在 ambiguity 被系统性注入后测量 agent 是否识别到歧义。这与现有的 prompting 研究（测试 LLM 是否 ask for clarification）在实验设计层面不同。

2. **Model-level 分化**。Section 6.2 报告 GPT-4.1 和 Claude 有 10-11% awareness，而 Qwen3 和 DeepSeek 为 0%（p = 2.2×10⁻⁹）。这种 model-specific 差异在现有文献中未被报告。

3. **与 prompt-based mitigation 的联动**。Appendix B 的 mitigation 实验显示 type-specific prompts 有效（auth scope -18pp）但 generic prompts 无效（+1.3pp overall），说明 disambiguation neglect 不是 prompting 能简单解决的。

**严重性判定：维持 Should-Fix 但建议降级为 Minor。** 论文的增量贡献是 context-specific 的量化和 model differentiation，这在现有文献中确实是新的。

---

**[AGREE] R2-W5: 数字密度过高**

同意。Table 2 的 7 列数值 + TOST Tier + p 值确实过于密集。我在自己的审稿中也提出了类似意见（Minor #1）。建议将 per-model violation rates 和 TOST tiers 移至 appendix，main text Table 仅保留 type、pooled rate、Δpp [CI]。

---

### 小问题

**[AGREE] R2-M1: Table 1 Disambig Channel 描述过简**

同意。Table 1 的 "Disambig. Channel" 列对每种类型的描述非常简短，读者需要到 §3 正文才能理解具体含义。在 caption 中增加简要说明或在 appendix 中提供 extended version 有助于独立可读性。

---

**[AGREE] R2-M2: Figure 2 "(App)" 标记**

同意。Figure 2 中 "(App)" 代表 perturbation control 在 appendix 中，但读者在 §5.1 之前遇到此图时无法理解这一标记。建议在 figure caption 中解释。

---

**[AGREE] R2-M3: Limitations 与正文少量重复**

同意但影响微小。Limitations 段落中关于合成 clause pairs 和 temperature=0 的讨论确实与 Discussion §7 有重叠，但这在会议论文中很常见，不构成实质问题。

---

**[AGREE] R2-M4: arXiv preprint 格式不统一**

同意。References 中部分 arXiv preprint 使用 "arXiv preprint arXiv:XXXX.XXXXX" 格式，部分仅有 ID。应统一格式。

---

### 对 R2 Questions 的回应

**Q1: DRIP-R "no single correct resolution" vs matched-pair ground truth**

好问题。论文的 matched-pair 设计确实假设了 ground truth（unambiguous variant 是 "正确" 的 policy intent）。但这不是论文的局限——这是因果推断的必要条件。论文的 claim 不是 "agents should resolve ambiguity in X way"，而是 "ambiguity causally increases violations compared to clear policies"。这一 claim 只需要 unambiguous variant 的 policy intent 是确定的，不需要 ambiguous variant 有唯一正确解析。论文在 §3 和 §7 中也没有声称可以推广到 "真实歧义没有唯一正确答案" 的场景——Discussion 明确说 "our synthetic design establishes causal mechanisms"（机制识别而非规范指导）。

**Q2: 排除 incompleteness 后 31.0pp 是否仍有实践意义**

是的。31.0pp（95% CI [27.9, 34.1], p < 10⁻⁷⁵, Section 5.1）仍然是一个非常大的效应。它意味着仅 5 种 non-confounded 歧义类型就能使违规率从 ~7% 提升到 ~38%——对任何安全关键部署都是不可接受的。

**Q3: Failure mechanism 分类是否 post-hoc？是否有 circular reasoning？**

同意 R2 的关切，这与我的 Should-Fix W3 一致。论文在 Section 6 明确标注 "[Exploratory]"，failure modes 是 post-hoc 编码的。关于 circularity：论文在 Section 6 第一段承认 "Using LLMs to code LLM failures introduces circularity risk"，并提供了两个 safeguard：(a) coder prompt 不包含 ambiguity type label，type 是 programmatically post-hoc 赋值的；(b) mutual information V=0.45 是从 LLM-coded labels 计算的，human coding κ=0.15 表明 NMI 是 upper bound。但如我在 W3 中指出的，LLM 间的"一致性"可能反映共享偏差。Section 6 的叙事应更 cautious。

**Q4: Claude auth scope 64% 异常是否影响 pooled estimates**

不影响 C1 的 pooled Δpp。matched-pair design 中 Δpp 是 within-model within-judge 的差值，Claude auth scope 的绝对 violation rate（12% ambiguous）虽然低，但其 Δpp 仍然是正的（Table 2 中 Claude 列 auth scope 是 12%，unambiguous baseline ~5-7%，所以 Δ ≈ +5-7pp）。Pooled Δpp 是所有 model×type 的加权平均。但 R2 的关切对 absolute violation rate 的 pooled estimate 有效——Claude auth scope 的 12% 拉低了 auth scope 的 pooled rate（41.6%），如果排除 Claude，auth scope pooled rate 会更高。这与我的 Must-Fix N3 (authorization scope construct validity) 一致。

---

### 对 R2 Missing References 的回应

**DRIP-R 方法论差异对比**：同意，正文可增加 1-2 句与 DRIP-R 在方法论上的差异对比（本文 matched-pair causal design vs. DRIP-R 的 annotation-based approach）。

**Gao-Arch et al. (2026) "Ambiguity collapse in LLMs"**：论文引用了 Liu et al. (2023) 的 "ambiguity collapse" 概念（Section 6.2），如果 Gao-Arch et al. (2026) 提供了更新的证据，应该被引用。

---

### 对 R2 主要优势的回应

**[AGREE] R2-S1 through S5**: R2 的优势总结与我的评估高度一致。特别是 S2（Claim 校准得当）和 S5（Real-world audit）是该论文的突出特质。我在自己的审稿中也重点肯定了论文的方法论诚实度（Strength #5）。

---

### 总体评估一致性

R2 给出 3.5 (Borderline Conference)，与我的评分相同。我们的核心分歧在于：

1. **严重性分级不同**：R2 的两个 Must-Fix（taxonomy contribution, terminology）我认为是 Should-Fix；而 R2 的 W2（ecological validity gap）我认为应升级为 Must-Fix。

2. **关注重点互补**：R2 侧重概念框架和定位（taxonomy novelty, terminology, two-layer justification），我侧重方法论和统计（cross-domain ρ, auth scope construct validity, ICC scope, residual variance）。两组意见合在一起构成更完整的评审图景。

3. **共识领域**：(a) ecological validity gap 需要更充分的讨论（R2-W2 = R1-N1）；(b) failure mode analysis 有 circularity 风险（R2-Q3 ≈ R1-W3）；(c) 数字密度过高（R2-W5 ≈ R1-Minor#1）；(d) matched-pair causal design 是该论文的核心方法论贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2209 · 2026-05-23T09:47:14.211243+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 212

## Round 212

2 recorded events


### User

_source line 2210 · 2026-05-23T09:47:16.776034+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。要点总结：

- R2 的两个 Must-Fix（taxonomy 增量贡献 N1、ambiguity 术语 N2）我均 **REBUT 并建议降级为 Should-Fix**——论文在 §3 已提供完整的选择逻辑和操作定义，缺的是呈现形式而非论证实质
- R2 的 W2（ecological validity gap）我 **AGREE 并建议升级为 Must-Fix**——这与我的 N1 一致
- R2 的 W1/W3/W5/M1-M4 全部 **AGREE**
- R2 的 W4（disambiguation neglect 新颖性）我 **REBUT**——论文贡献在于因果框架下的量化和 model-level 分化，不是简单的 "LLM 不问问题" 观察
- 核心分歧：R2 侧重概念框架定位，我侧重方法论和统计严谨性，两组意见互补

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2211 · 2026-05-23T09:47:26.861410+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 213

## Round 213

10 recorded events


### User

_source line 2212 · 2026-05-23T09:48:07.224746+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — Reviewer 1 审稿意见

---

### Must-Fix 问题

**[AGREE] R1-N1: 合成 vs 自然效应量差距（2.7×）缺乏桥接分析**

同意。这与我的 W2 完全一致。验证：Abstract（p1）headline 用 31.0pp（confound-free），Conclusion（p8）说"cross-benchmark evidence confirms directional consistency at reduced magnitude"，但 12.6pp 这个数字从未出现在 Abstract 或 Conclusion 中。Discussion §7（p8）仅一句"overestimates naturalistic effect sizes"。对于想评估实际部署风险的从业者来说，2.7× 的差距是核心信息，不应只在 Appendix Z 中讨论。我支持 R1 的建议：Abstract/Conclusion 同时报告两个数字，并用 2-3 句话分析差距来源。

**[AGREE] R1-N2: 跨领域 ρ=0.26 与 taxonomy 泛化性 framing 矛盾**

同意 Abstract 需要加 domain qualification。验证：Abstract（p1）写的是"enabling type-targeted diagnosis for policy-governed deployments"——没有领域限定词。Conclusion（p8）则已经加了限定："enabling type-targeted diagnostics within customer-service domains (§6); cross-domain type rankings require per-domain calibration (ρ = 0.26)"。所以问题集中在 Abstract wording，不是结构性缺陷。修改代价很低。

但我要补充一个 nuance：R1 说"type ranking 在 retail vs airline 之间零相关"，这是准确的（ρ=0.26, p=0.62）。但 binary ambiguity effect（有无歧义 → 是否增加 violation）在两个领域都显著且方向一致。所以 taxonomy 的"诊断"价值（type→mechanism mapping）可能是跨领域稳健的，只是 type 的相对风险排序是领域依赖的。论文应区分这两层泛化性。

**[REBUT] R1-N3: Authorization scope 构念效度——同意问题存在，但不同意严重等级**

R1 的证据链完整且有说服力：κ=0.385 最低、模型间变异最大（Table 2, p7 显示 auth scope 从 34.6% 到 65.6%）、驱动 cross-judge discordance（排除后 ρ 从低值→0.90, §5.2 p6）、驱动 C4 interaction。这些事实我全部确认。

但我不同意将其定为 Must-Fix，理由：

1. **透明度已充分**：论文在 §5.2（p6）明确报告了 auth scope 的 cross-judge variance（41.6%–65.6%）和低 κ（0.385）；Appendix G 报告了最低的 per-type ICC（0.29）；§5.2 右栏报告了排除后 ρ 从 discordant→0.90。这不是隐瞒问题，而是公开报告的 limitation。

2. **概念合理性**：Authorization scope 的低 inter-judge reliability 不是 taxonomy 设计缺陷，而是该类别固有的评判难度——permission boundary judgment 本身就比 lexical ambiguity 更主观（§6.1 p7: "Boundary violation... the agent exceeds permission boundaries when authorization scope is underspecified"）。这恰恰是该类别在真实 policy 中最危险的原因。

3. **post-hoc 排除的偏见**：R1 建议"系统报告 5-type excluding auth scope 的所有核心结果"。但 post-hoc 删除一个 type 因为它表现"异常"会引入 researcher degrees of freedom。如果 auth scope 是事先预注册的 type，排除它需要更强的理由。

**我的建议**：降级为 Should-Fix。在 main text 增加一个 consolidated paragraph（而非散落在 appendix 中的碎片讨论）承认 auth scope 的构念效度挑战，但不必系统排除它。

---

### Should-Fix 问题

**[AGREE] R1-W1: ICC=0.919 仅 OpenAI family**

§4.1（p5）明确写了"ICC is computed within the OpenAI family"，但 section heading 是"Reproducibility"——这个标题暗示全局可复现性。改为"Within-Family Reproducibility"或在 heading 后加 parenthetical 限定即可。

**[AGREE] R1-W2: 60.8% 残差方差中 ~46% 系统性部分**

合理要求。Appendix AB 做了方差分解但正文没有讨论 46% 系统性残差的可能来源。2-3 句话提几个候选来源（conversation trajectory, user persona, tool-use sequence）就够了。不过我要指出，未解释的方差在 behavioral science 实验中是常态，不是特有缺陷。

**[AGREE] R1-W3: Failure mode 分析循环性风险**

R1 的逻辑是：用 LLM 编码 LLM 的 failure modes → LLM 编码可能反映 LLM 自身 bias 而非 ground truth → type→mechanism 关联可能被放大。这个论点在原则上成立。

论文的防御（§6 p7）是：(1) type 是 exogenous variable（programmatically assigned），(2) mutual information f(type:mechanism)=0.1 bits, V=0.15（Appendix U），说明 LLM 编码没有系统性地将特定 type 映射到特定 mechanism。但 V=0.15 是 type-mechanism 之间的 mutual information 用 LLM labels 计算——如果 LLM 编码本身有 systematic bias，这个数字可能被 bias 而非 ground truth 驱动。

我同意降级表述强度。但"1/3 关联可能 tautological"这个具体比例（R1 的判断）需要更强的证据支撑——R1 没有说明哪 1/3 是 tautological，这是 R1 自己的推测。

**[AGREE] R1-W4: Incompleteness confound 控制的间接性**

Token count 是 information content 的 very crude proxy。论文用 token count 回归（Appendix F）显示"controlling for token count changes no type's predicted effect by more than 0.1 pp"（§5.1 p6），但 token count ≠ semantic information quantity。例如，两个句子可以有相同 token count 但完全不同的 information density。主文应承认这个局限性。

但我要补充：incompleteness 的 confound 是 information addition（unambiguous version 必然添加了原本缺失的信息），而非简单的 length difference。Token count 控制的目的是排除 length 本身的效应，而不是完全消除 information confound——后者在 matched-pair design 中本质上无法完全消除（§4.5 p5 已经承认 incompleteness effect "is an upper bound"）。所以问题不是控制是否完美，而是主文是否充分承认了这个局限性。

**[AGREE] R1-W5: Temperature=0 限制生态效度**

Temperature=0 使所有输出 deterministic，可能放大了 systematic nocuity（§6.3）的 convergent error pattern。在 temperature>0 下，同一 clause 的不同 runs 可能产生不同解释，这可能 (a) 打破 convergent pattern 但 (b) 也可能暴露更多 divergent error modes。论文应讨论这个方向性影响。

---

### 小问题

**[AGREE] R1-Minor-1**: Table 2 信息密度过高。与我的 W5 一致。

**[AGREE] R1-Minor-2**: Abstract 中 Cramér's V 缺乏上下文——读者第一次看到这个数字时不知道它是 type→mechanism 还是 type→rate。

**[AGREE] R1-Minor-3**: "Nocuous" 含义反转。与我的 W3 完全一致。两位 reviewer 独立标记了同一个术语问题，说明这不是 edge case。

**[AGREE] R1-Minor-4**: ρ=0.09 two-group ranking discordance。论文在 §5.2（p6）确实报告了这个问题（"two-group rankings are discordant (κ = 0.08)"），但将其放在 qualification paragraph 中而非主要 finding 中。考虑到这直接影响 taxonomy 的实用价值（如果不同 judge 对 type ranking 不一致，从业者无法信赖该 ranking），可以适当提升其可见度。

**[AGREE] R1-Minor-5**: LaTeX vs PDF 数值一致性应确认。

---

### R1 的 Questions 回应

**Q1 (34pp vs 12.6pp 差距来源)**：我的 W2 也问了类似问题。论文 Appendix Z 列出了三个结构性差异（episode-level vs clause-level measurement, test-constraint boundaries, interaction depth），但没有量化各因素的贡献。这是一个值得 author response 回答的问题。

**Q2 (Auth scope κ=0.385 是否需要重定义)**：如上述 REBUT R1-N3，我认为不需要重新定义，但需要 consolidated 讨论。排除后 C2 保持稳健（ρ=0.90）本身就是有价值的 robustness check。

**Q3 (46% 系统性残差来源)**：同意这值得讨论。候选来源可能包括 conversation trajectory diversity、policy clause embedding position、multi-turn interaction dynamics。

**Q4 (Temperature>0 影响)**：同意值得讨论。我补充一点：permissive attractor（§6.3: 77% permissive bias）可能在 temperature>0 下被削弱或强化，取决于 model 的 sampling distribution shape。

**Q5 (ICC=0.749 vs 0.919)**：0.919 是 within-OpenAI family（3 replicates of GPT-5.4），0.749 是 cross-provider（5 models, all providers）。差异合理——不同 provider 的模型确实有不同的 policy interpretation 倾向。论文应在 §4.1 中更清晰地解释这两个 ICC 的关系。

---

### 两位 Reviewer 的共识点

以下问题被 R1 和 R2 独立标记，应优先处理：

1. **合成 vs 自然效应量差距**（R1-N1 / R2-W2）：两位 reviewer 都认为 34pp→12.6pp 的差距需要在正文中更充分讨论。
2. **"Nocuous" 术语延伸**（R1-Minor-3 / R2-W3）：两位 reviewer 都认为从 divergent→convergent 的概念转换需要更明确的论证。
3. **数字密度过高**（R1-Minor-1 / R2-W5）：两位 reviewer 都认为正文的统计数字密度影响可读性。
4. **Taxonomy 泛化性限定**（R1-N2 / R2-N1 部分）：Abstract 中的 claim 需要加 domain-specificity 限定词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2213 · 2026-05-23T09:48:30.270465+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2214 · 2026-05-23T09:48:30.371405+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T09:29:58.677850+00:00\", \"completed_at\": \"2026-05-23T09:33:08.619134+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item（纯 Title + Abstract），审稿人翻到 page 2 才看到第一个视觉锚点 Figure 1。不影响接收但错失首页锚定机会\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（Experimental Overview 三面板图）作为首个 display item，清晰传达了 taxonomy → evaluation → cross-judge 的端到端流程，caption 自包含，锚定效果好\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Table 1（六类歧义分类）带蓝色单元格底色，视觉区分度好；文字可读，booktabs 风格；caption 说明充分\"}, {\"severity\": \"warning\", \"dimension\": \"page 4-5\", \"message\": \"连续两页纯文本（Method §4.1–4.6），无任何 display item 穿插。内容为实验平台、匹配对设计、模型列表、评估方法、统计分析——可考虑用一个 models summary table 或 experimental design diagram 打破纯文本节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（per-type effect sizes lollipop plot）放置合理，在 Results §5.1 内。图表清晰，CI 标注可读，颜色区分度好\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 + Figure 3 双 display item 页面。Table 2 使用 booktabs 风格，最优值加粗，Δpp 列清晰。Figure 3 热力图色阶从浅黄到深红，单元格内嵌数值标注弥补色觉辨识问题\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 热力图使用黄-红渐变色阶，非最佳色盲友好方案（红-绿色觉缺陷者辨别暖色调梯度较困难），但单元格内数值标注有效缓解此问题\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4（type-mechanism association 热力图）+ Discussion + Conclusion 共占一页，信息密度高但无溢出。Conclusion 被压缩到约 1/4 页篇幅，内容完整\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 3 和 Figure 4 的热力图色阶语义一致（同方向暖色=高值），全文颜色语义一致性良好\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落约 12 行，简洁覆盖 3 个要点（合成数据、模型覆盖、温度设置），符合 EMNLP 要求。References 从页面约 1/3 处开始\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Appendix Tables 4–7 字号偏小（约正文 65-70%），4 个表格密集排列。作为附录可接受，但 Table 5（Generic vs. type-specific disambiguati
…[truncated 502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2215 · 2026-05-23T09:48:30.422010+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2216 · 2026-05-23T09:48:30.422507+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2217 · 2026-05-23T09:51:57.570727+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 25\n\n# ============================================================\n# R25 ISSUES — ACTIVE\n# ============================================================\n\n- id: \"R25-N1\"\n  summary: \"合成效应 34pp vs SOPBench 12.6pp (2.7×) 缺乏桥接分析——Abstract/Conclusion 未报告自然下界\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-N3: SOPBench 63% 压缩未充分讨论\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix N1, R2 Should-Fix W2→交叉后 AGREE 升级。共识 Must-Fix：Abstract/Conclusion 需同时报告 34pp 和 12.6pp，Discussion 需 2-3 句分析差距来源\"\n  action_items:\n    - round: 25\n      action: \"Abstract/Conclusion 同时报告合成上界(34pp/31pp)和自然下界(12.6pp)；Discussion ecological validity 段扩展为 2-3 句分析差距来源(measurement grain, baseline compression, interaction depth)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N2\"\n  summary: \"跨领域 ρ=0.26 (p=0.62) vs Abstract 'type-targeted diagnostics' 泛化性 framing 矛盾\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-W7: Conclusion 需限定适用范围\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix N2, R2 交叉后 AGREE。Abstract 无领域限定词。Conclusion 已有限定('within customer-service domains')，修复集中在 Abstract wording\"\n  action_items:\n    - round: 25\n      action: \"Abstract 加 domain-specificity 限定词(e.g. 'within-domain type-targeted diagnostics')；区分 binary effect 跨领域稳健性 vs type ordering 领域依赖性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W1\"\n  summary: \"Authorization scope 构念效度——κ=0.385, 52pp 模型间变异, 驱动 C2 discordance 和 C4 interaction，需 consolidated 段落讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-W1: 排除后核心指标缺失→已在 Appendix AA 补充\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix N3, R2 REBUT→Should-Fix。R2 理由：透明度已充分(§5.2+Appendix G+AA)、构念合理性(permission boundary 固有主观性)、post-hoc 排除有偏见风险。共识：需 main text consolidated paragraph 而非 Appendix 碎片讨论\"\n  action_items:\n    - round: 25\n      action: \"§5.2 或 §7 增加 consolidated paragraph 讨论 auth scope 构念效度挑战：低 κ、高模型间变异、驱动 C2/C4 不一致性，以及为何保留该类型(固有主观性=真实世界危险源)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W2\"\n  summary: \"Taxonomy 增量贡献论证——缺少 Li et al. 11→6 映射表格和排除理由\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix N1, R1 REBUT→Should-Fix。R1 理由：§3 已有完整选择逻辑(3 criteria + 排除举例)，缺的是呈现便利性而非论证实质。共识 Should-Fix：增加映射表格提升可读性\"\n  action_items:\n    - round: 25\n      action: \"§3 或 Appendix 增加 11→6 mapping 表格：列出 Li et al. 11 types、对应本文 type(如有)、排除理由(每行一句)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W3\"\n  summary: \"'Ambiguity' 广义使用与 NLP 社区标准定义的张力——需加强术语选择论证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix N2, R1 REBUT→Should-Fix。R1 理由：§3 Scope of ambiguity 段已有操作定义(Wasow et al. 2005)和 RE 文献支撑(Dalpiaz et al. 2018)；改用 'specification defects' 会脱离 NLP/CL 对话。共识 Should-Fix：§3 增加 1-2 句讨论与 NLP 传统分类关系\"\n  action_items:\n    - round: 25\n      action: \"§3 'Scope of ambiguity' 段增加 1-2 句明确讨论本文广义定义与 NLP 传统(ambiguity vs vagueness vs incompleteness)的关系\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W4\"\n  summary: \"'Nocuous' 术语从 divergent→convergent 的概念延伸——需在首次使用时标注\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-M2: 首次使用时标注\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立标记。Abstract 有 'inverting...divergent to convergent' 但不够明确。§6.3 解释出现在第 8 页太晚\"\n  action_items:\n    - round: 25\n      action: \"§1 首次使用 'nocuous' 时简要说明概念延伸(从 Berry & Kamsties 的 divergent interpretation 到本文的 convergent error)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W5\"\n  summary: \"C3 inconclusive 但 taxonomy 仍按 two-layer 组织——需显式声明为理论组织框架\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-N4: 降格为 design hypothesis\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix W1, R1 交叉后 AGREE。§3 已改为 'design hypothesis' 但仍不够显式\"\n  action_items:\n    - round: 25\n      action: \"§3 开头增加一句：two-layer 结构是基于 RE 文献的组织框架(organizational framework)，其经验支撑由 C3 检验(结果 inconclusive)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W6\"\n  summary: \"ICC 'Reproducibility' 标题误导——仅 OpenAI family 内计算\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-W5: 已加 qualifier 但标题未改\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W1, R2 AGREE。标题 'Reproducibility' 暗示跨 provider\"\n  action_items:\n    - round: 25\n      action: \"§4.5 标题改为 'Within-family reproducibility' 或加 parenthetical 限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W7\"\n  summary: \"60.8% 残差方差中 ~46% 系统性部分未讨论可能来源\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [2]\n      note: \"R24-W9: Discussion 加了一句但不够\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W2, R2 AGREE。需讨论 2-3 个候选来源(conversation trajectory, user persona, tool-use sequence)\"\n  action_items:\n    - round: 25\n      action: \"Discussion 增加 2-3 句讨论系统性残差的可能来源\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W8\"\n  summary: \"Failure mode 分析表述过强——LLM-coded κ=0.52 vs human κ=0.15, circularity risk\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-W3: 加了 coder prompt 披露和 NMI upper bound\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W3, R2 AGREE。改进已见但 §6 仍用 'mechanistically distinct' 等强表述。需降级为 'categorically distinct in LLM coding'\"\n  action_items:\n    - round: 25\n      action: \"§6 将 'mechanistically distinct' 降级为 'categorically distinct in LLM coding'；开头加 caveat 段落强调 exploratory + LLM-coded 局限\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W9\"\n  summary: \"Incompleteness confound: token count 是粗糙代理——main text 需承认局限性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W4, R2 AGREE。Appendix F 末尾一句承认但 main text 未提及\"\n  action_items:\n    - round: 25\n      action: \"§5.1 incompleteness 讨论处增加一句承认 token count 是粗糙代理\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W10\"\n  summary: \"Temperature=0 限制生态效度——需讨论方向性影响\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-M3: Limitations 加了一句\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W5, R2 AGREE。Limitations 提及但未讨论方向性预期(temperature>0 可能打破 convergent pattern 或暴露更多 divergent modes)\"\n  action_items:\n    - round: 25\n      action: \"Limitations 或 Discussion 增加 1-2 句讨论 temperature>0 的可能影响方向\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M1\"\n  summary: \"正文数字密度过高(Results/Analysis)——部分统计细节可移至 appendix\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立标记。Table 2 的 per-model rates + TOST Tier 可简化\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M2\"\n  summary: \"Disambiguation neglect 增量贡献需更明确阐述\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [2]\n      note: \"R2 Should-Fix W4, R1 REBUT→建议降级 Minor。R1 理由：增量在于因果框架下量化+model-level 分化(0% vs 10-11%, p=2.2e-9)\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M3\"\n  summary: \"References 中 arXiv preprint 格式不统一\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [2]\n      note: \"部分用 'arXiv preprint arXiv:XXXX'，部分仅有 ID\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R24 ISSUES — RESOLVED IN R25\n# ============================================================\n\n- id: \"R24-N1\"\n  summary: \"Novelty framing 偏强——'first matched-pair causal study' 是领域迁移而非方法论创新\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Contributions 重写为 (1) causal study 基础, (2) diagnostic taxonomy(type→mechanism V=0.45), (3) disambiguation neglect + systematic nocuity。R25 R2-N1 提出 taxonomy 增量论证不足的相关但不同问题，见 R25-W2\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 25\n\n- id: \"R24-N2\"\n  summary: \"Incompleteness confound framing 不够突出——confound-free range 应作为 headline\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Abstract 已以 confound-free 31.0pp 为 lead (34.0pp 为补充)；Conclusion 同步。R25 未被 reviewer 复发标记\"\n  resolution_round: 25\n  first_raised_round: 21\n  last_seen_round: 24\n\n- id: \"R24-W2\"\n  summary: \"Template pipeline 不透明\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Appendix S (Clause Pair Construction) 已补充：手工构建 300 对, 无 over-generation, 质量审查细节, 96% 初始一致率\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W4\"\n  summary: \"SESOI ±15pp justification 不够 principled\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"§4.6 已改为 'pragmatic default, not principled domain-anchored threshold' + Table 3 sensitivity + bootstrap cluster。R25 未被 reviewer 复发标记\"\n  resolution_round: 25\n  first_raised_round: 20\n  last_seen_round: 24\n\n- id: \"R24-W6\"\n  summary: \"Human validation per-type CI 极宽\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Per-type κ 引用处已附 qualifier ('wide CIs', 'descriptive statistics only')\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W8\"\n  summary: \"NMI cardinality 不对称——'order of magnitude' 表述含 artifact\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"全文 'order of magnitude' 已改为 'substantially more strongly'；Appendix 表补 V=0.137 + 维度差异脚注\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M4\"\n  summary: \"C3/C4 claim 层级暗示四个同等级\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"§5 开头已标 C3 inconclusive, C4 exploratory\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M5\"\n  summary: \"Table 2 脚注缺 per-type 样本量\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"脚注已加 n≈17\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M6\"\n  summary: \"Prevalence audit κ=0.295 未在 Introduction 标注\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Introduction 引用处已标注 'dual-judge κ = 0.30'\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X1\"\n  summary: \"ICC≈0 应改为 ICC=-0.006 uninformative due to floor effects\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Appendix AB 已改为 'the replication ICC (= −0.006) is uninformative because the sampled 9 auth-scope clauses × 2 conservative models produced near-zero violation rates in 34/36 cells (floor effect)'\"\n  resolution_round: 25\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R24-X3\"\n  summary: \"Limitations 过长（5段）——EMNLP 要求 ~3 个点一小段\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"Limitations 已压缩为一段 3 个要点 + Data and Code Availability 单独段落\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X4\"\n  summary: \"Limitations 说人工验证 'underway' 但 Appendix 已有结果——内部矛盾\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"已删除 underway 表述，替换为实际结果引用\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n# ============================================================\n# R23 ISSUES — ALL RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R23-N1\"\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  resolution: \"Compressed §5.1, Discussion, Conclusion. Visual verification: Conclusion ends p8.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-N2\"\n  summary: \"Auth scope 未充分标注\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Table 2 ‡ + footnote + excluding-auth-scope sentence.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R23-W1\"\n  summary: \"Incompleteness confound framing [复发]\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Abstract reframed with confound-free range + Table 2 footnote.\"\n  resolution_round: 23\n  first_raised_round: 21\n  last_seen_round: 24\n\n- id: \"R23-W2\"\n  summary: \"Cross-judge ρ=0.09 post-hoc\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Three-family validation leads; ρ=0.09 as sensitivity check.\"\n  resolution_round: 23\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: \"R23-W3\"\n  summary: \"ICC OpenAI-family qualifier insufficient\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Qualifier added in 3 locations.\"\n  resolution_round: 23\n  first_raised_round: 22\n  last_seen_round: 24\n\n- id: \"R23-W4\"\n  summary: \"SESOI pragmatic/circular [复发×4]\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Replaced 'principled' with 'pragmatic threshold'. Bootstrap promoted.\"\n  resolution_round: 23\n  first_raised_round: 20\n  last_seen_round: 24\n\n- id: \"R23-W5\"\n  summary: \"Per-type κ without CI\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"§4.4 qualifier added.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-W6\"\n  summary: \"合成歧义生态效度\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Discussion threats sentence added.\"\n  resolution_round: 23\n  first_raised_round: 22\n  last_seen_round: 24\n\n- id: \"R23-M1\"\n  summary: \"NMI order of magnitude needs context\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Cramér's V added.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M2\"\n  summary: \"Abstract info overload\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Trimmed to 3 core numbers.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R23-M3\"\n  summary: \"Disambiguation neglect inference scope\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"'externally expressed' added.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M4\"\n  summary: \"Table 2 excl-incompleteness row\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Footnote added.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M5\"\n  summary: \"Token count proxy crude\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"Limitations states imperfect proxy.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M6\"\n  summary: \"§4.3 'architecturally diverse' inaccurate\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Changed to 'five models from four providers spanning two architecture families'.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M7\"\n  summary: \"arXiv citation format inconsistent\"\n  category: format\n  severity: minor\n  status: resolved\n  resolution: \"Fixed 2 entries to @article.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 25\n\n# ============================================================\n# R25 ISSUES — ACTIVE\n# ============================================================\n\n- id: \"R25-N1\"\n  summary: \"合成效应 34pp vs SOPBench 12.6pp (2.7×) 缺乏桥接分析——Abstract/Conclusion 未报告自然下界\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-N3: SOPBench 63% 压缩未充分讨论\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix N1, R2 Should-Fix W2→交叉后 AGREE 升级。共识 Must-Fix：Abstract/Conclusion 需同时报告 34pp 和 12.6pp，Discussion 需 2-3 句分析差距来源\"\n  action_items:\n    - round: 25\n      action: \"Abstract/Conclusion 同时报告合成上界(34pp/31pp)和自然下界(12.6pp)；Discussion ecological validity 段扩展为 2-3 句分析差距来源(measurement grain, baseline compression, interaction depth)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N2\"\n  summary: \"跨领域 ρ=0.26 (p=0.62) vs Abstract 'type-targeted diagnostics' 泛化性 framing 矛盾\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-W7: Conclusion 需限定适用范围\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix N2, R2 交叉后 AGREE。Abstract 无领域限定词。Conclusion 已有限定('within customer-service domains')，修复集中在 Abstract wording\"\n  action_items:\n    - round: 25\n      action: \"Abstract 加 domain-specificity 限定词(e.g. 'within-domain type-targeted diagnostics')；区分 binary effect 跨领域稳健性 vs type ordering 领域依赖性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W1\"\n  summary: \"Authorization scope 构念效度——κ=0.385, 52pp 模型间变异, 驱动 C2 discordance 和 C4 interaction，需 consolidated 段落讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-W1: 排除后核心指标缺失→已在 Appendix AA 补充\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix N3, R2 REBUT→Should-Fix。R2 理由：透明度已充分(§5.2+Appendix G+AA)、构念合理性(permission boundary 固有主观性)、post-hoc 排除有偏见风险。共识：需 main text consolidated paragraph 而非 Appendix 碎片讨论\"\n  action_items:\n    - round: 25\n      action: \"§5.2 或 §7 增加 consolidated paragraph 讨论 auth scope 构念效度挑战：低 κ、高模型间变异、驱动 C2/C4 不一致性，以及为何保留该类型(固有主观性=真实世界危险源)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W2\"\n  summary: \"Taxonomy 增量贡献论证——缺少 Li et al. 11→6 映射表格和排除理由\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix N1, R1 REBUT→Should-Fix。R1 理由：§3 已有完整选择逻辑(3 criteria + 排除举例)，缺的是呈现便利性而非论证实质。共识 Should-Fix：增加映射表格提升可读性\"\n  action_items:\n    - round: 25\n      action: \"§3 或 Appendix 增加 11→6 mapping 表格：列出 Li et al. 11 types、对应本文 type(如有)、排除理由(每行一句)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W3\"\n  summary: \"'Ambiguity' 广义使用与 NLP 社区标准定义的张力——需加强术语选择论证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix N2, R1 REBUT→Should-Fix。R1 理由：§3 Scope of ambiguity 段已有操作定义(Wasow et al. 2005)和 RE 文献支撑(Dalpiaz et al. 2018)；改用 'specification defects' 会脱离 NLP/CL 对话。共识 Should-Fix：§3 增加 1-2 句讨论与 NLP 传统分类关系\"\n  action_items:\n    - round: 25\n      action: \"§3 'Scope of ambiguity' 段增加 1-2 句明确讨论本文广义定义与 NLP 传统(ambiguity vs vagueness vs incompleteness)的关系\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W4\"\n  summary: \"'Nocuous' 术语从 divergent→convergent 的概念延伸——需在首次使用时标注\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-M2: 首次使用时标注\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立标记。Abstract 有 'inverting...divergent to convergent' 但不够明确。§6.3 解释出现在第 8 页太晚\"\n  action_items:\n    - round: 25\n      action: \"§1 首次使用 'nocuous' 时简要说明概念延伸(从 Berry & Kamsties 的 divergent interpretation 到本文的 convergent error)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W5\"\n  summary: \"C3 inconclusive 但 taxonomy 仍按 two-layer 组织——需显式声明为理论组织框架\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-N4: 降格为 design hypothesis\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix W1, R1 交叉后 AGREE。§3 已改为 'design hypothesis' 但仍不够显式\"\n  action_items:\n    - round: 25\n      action: \"§3 开头增加一句：two-layer 结构是基于 RE 文献的组织框架(organizational framework)，其经验支撑由 C3 检验(结果 inconclusive)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W6\"\n  summary: \"ICC 'Reproducibility' 标题误导——仅 OpenAI family 内计算\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-W5: 已加 qualifier 但标题未改\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W1, R2 AGREE。标题 'Reproducibility' 暗示跨 provider\"\n  action_items:\n    - round: 25\n      action: \"§4.5 标题改为 'Within-family reproducibility' 或加 parenthetical 限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W7\"\n  summary: \"60.8% 残差方差中 ~46% 系统性部分未讨论可能来源\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [2]\n      note: \"R24-W9: Discussion 加了一句但不够\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W2, R2 AGREE。需讨论 2-3 个候选来源(conversation trajectory, user persona, tool-use sequence)\"\n  action_items:\n    - round: 25\n      action: \"Discussion 增加 2-3 句讨论系统性残差的可能来源\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W8\"\n  summary: \"Failure mode 分析表述过强——LLM-coded κ=0.52 vs human κ=0.15, circularity risk\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-W3: 加了 coder prompt 披露和 NMI upper bound\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W3, R2 AGREE。改进已见但 §6 仍用 'mechanistically distinct' 等强表述。需降级为 'categorically distinct in LLM coding'\"\n  action_items:\n    - round: 25\n      action: \"§6 将 'mechanistically distinct' 降级为 'categorically distinct in LLM coding'；开头加 caveat 段落强调 exploratory + LLM-coded 局限\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W9\"\n  summary: \"Incompleteness confound: token count 是粗糙代理——main text 需承认局限性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W4, R2 AGREE。Appendix F 末尾一句承认但 main text 未提及\"\n  action_items:\n    - round: 25\n      action: \"§5.1 incompleteness 讨论处增加一句承认 token count 是粗糙代理\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W10\"\n  summary: \"Temperature=0 限制生态效度——需讨论方向性影响\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-M3: Limitations 加了一句\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W5, R2 AGREE。Limitations 提及但未讨论方向性预期(temperature>0 可能打破 convergent pattern 或暴露更多 divergent modes)\"\n  action_items:\n    - round: 25\n      action: \"Limitations 或 Discussion 增加 1-2 句讨论 temperature>0 的可能影响方向\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M1\"\n  summary: \"正文数字密度过高(Results/Analysis)——部分统计细节可移至 appendix\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立标记。Table 2 的 per-model rates + TOST Tier 可简化\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M2\"\n  summary: \"Disambiguation neglect 增量贡献需更明确阐述\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [2]\n      note: \"R2 Should-Fix W4, R1 REBUT→建议降级 Minor。R1 理由：增量在于因果框架下量化+model-level 分化(0% vs 10-11%, p=2.2e-9)\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M3\"\n  summary: \"References 中 arXiv preprint 格式不统一\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [2]\n      note: \"部分用 'arXiv preprint arXiv:XXXX'，部分仅有 ID\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R24 ISSUES — RESOLVED IN R25\n# ============================================================\n\n- id: \"R24-N1\"\n  summary: \"Novelty framing 偏强——'first matched-pair causal study' 是领域迁移而非方法论创新\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Contributions 重写为 (1) causal study 基础, (2) diagnostic taxonomy(type→mechanism V=0.45), (3) disambiguation neglect + systematic nocuity。R25 R2-N1 提出 taxonomy 增量论证不足的相关但不同问题，见 R25-W2\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 25\n\n- id: \"R24-N2\"\n  summary: \"Incompleteness confound framing 不够突出——confound-free range 应作为 headline\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Abstract 已以 confound-free 31.0pp 为 lead (34.0pp 为补充)；Conclusion 同步。R25 未被 reviewer 复发标记\"\n  resolution_round: 25\n  first_raised_round: 21\n  last_seen_round: 24\n\n- id: \"R24-W2\"\n  summary: \"Template pipeline 不透明\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Appendix S (Clause Pair Construction) 已补充：手工构建 300 对, 无 over-generation, 质量审查细节, 96% 初始一致率\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W4\"\n  summary: \"SESOI ±15pp justification 不够 principled\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"§4.6 已改为 'pragmatic default, not principled domain-anchored threshold' + Table 3 sensitivity + bootstrap cluster。R25 未被 reviewer 复发标记\"\n  resolution_round: 25\n  first_raised_round: 20\n  last_seen_round: 24\n\n- id: \"R24-W6\"\n  summary: \"Human validation per-type CI 极宽\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Per-type κ 引用处已附 qualifier ('wide CIs', 'descriptive statistics only')\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W8\"\n  summary: \"NMI cardinality 不对称——'order of magnitude' 表述含 artifact\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"全文 'order of magnitude' 已改为 'substantially more strongly'；Appendix 表补 V=0.137 + 维度差异脚注\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M4\"\n  summary: \"C3/C4 claim 层级暗示四个同等级\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"§5 开头已标 C3 inconclusive, C4 exploratory\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M5\"\n  summary: \"Table 2 脚注缺 per-type 样本量\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"脚注已加 n≈17\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M6\"\n  summary: \"Prevalence audit κ=0.295 未在 Introduction 标注\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Introduction 引用处已标注 'dual-judge κ = 0.30'\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X1\"\n  summary: \"ICC≈0 应改为 ICC=-0.006 uninformative due to floor effects\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Appendix AB 已改为 'the replication ICC (= −0.006) is uninformative because the sampled 9 auth-scope clauses × 2 conservative models produced near-zero violation rates in 34/36 cells (floor effect)'\"\n  resolution_round: 25\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R24-X3\"\n  summary: \"Limitations 过长（5段）——EMNLP 要求 ~3 个点一小段\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"Limitations 已压缩为一段 3 个要点 + Data and Code Availability 单独段落\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X4\"\n  summary: \"Limitations 说人工验证 'underway' 但 Appendix 已有结果——内部矛盾\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"已删除 underway 表述，替换为实际结果引用\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n# ============================================================\n# R23 ISSUES — ALL RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R23-N1\"\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  resolution: \"Compressed §5.1, Discussion, Conclusion. Visual verification: Conclusion ends p8.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-N2\"\n  summary: \"Auth scope 未充分标注\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Table 2 ‡ + footnote + excluding-auth-scope sentence.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R23-W1\"\n  summary: \"Incompleteness confound framing [复发]\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Abstract reframed with confound-free range + Table 2 footnote.\"\n  resolution_round: 23\n  first_raised_round: 21\n  last_seen_round: 24\n\n- id: \"R23-W2\"\n  summary: \"Cross-judge ρ=0.09 post-hoc\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Three-family validation leads; ρ=0.09 as sensitivity check.\"\n  resolution_round: 23\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: \"R23-W3\"\n  summary: \"ICC OpenAI-family qualifier insufficient\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Qualifier added in 3 locations.\"\n  resolution_round: 23\n  first_raised_round: 22\n  last_seen_round: 24\n\n- id: \"R23-W4\"\n  summary: \"SESOI pragmatic/circular [复发×4]\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Replaced 'principled' with 'pragmatic threshold'. Bootstrap promoted.\"\n  resolution_round: 23\n  first_raised_round: 20\n  last_seen_round: 24\n\n- id: \"R23-W5\"\n  summary: \"Per-type κ without CI\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"§4.4 qualifier added.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-W6\"\n  summary: \"合成歧义生态效度\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Discussion threats sentence added.\"\n  resolution_round: 23\n  first_raised_round: 22\n  last_seen_round: 24\n\n- id: \"R23-M1\"\n  summary: \"NMI order of magnitude needs context\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Cramér's V added.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M2\"\n  summary: \"Abstract info overload\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Trimmed to 3 core numbers.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R23-M3\"\n  summary: \"Disambiguation neglect inference scope\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"'externally expressed' added.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M4\"\n  summary: \"Table 2 excl-incompleteness row\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Footnote added.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M5\"\n  summary: \"Token count proxy crude\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"Limitations states imperfect proxy.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M6\"\n  summary: \"§4.3 'architecturally diverse' inaccurate\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Changed to 'five models from four providers spanning two architecture families'.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23\n\n- id: \"R23-M7\"\n  summary: \"arXiv citation format inconsistent\"\n  category: format\n  severity: minor\n  status: resolved\n  resolution: \"Fixed 2 entries to @article.\"\n  resolution_round: 23\n  first_raised_round: 23\n  last_seen_round: 23"
  }
}
```

</details>

---


### Tool result

_source line 2218 · 2026-05-23T09:51:57.672340+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 16942}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2219 · 2026-05-23T09:54:48.240427+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 25 审稿报告 — 圆桌合成\n\n**论文**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\n**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n**轮次**: 1 轮（交叉后关键问题达成共识，无需第 2 轮）\n\n---\n\n## Summary\n\n本文研究 policy ambiguity 对 LLM agent 安全的因果影响。通过在 τ²-bench 上构造 300 对匹配 clause pairs（涵盖 6 类歧义），评估 5 个模型（2,997 episodes），发现歧义使违规率增加 31.0pp（confound-free types）/ 34.0pp（全部 6 types）。论文发现 type 仅解释 0.4% 的违规方差但预测 failure mechanism 的能力更强（Cramér's V=0.45 vs 0.14），将 taxonomy 定位为诊断工具。此外报告了 disambiguation neglect（4.6% awareness）和 systematic nocuity（41.3% 收敛违规，77% permissive bias）两个实证现象。\n\n---\n\n## Strengths\n\n**S1** [共识] **因果设计的稀缺性和严谨性**。Matched-pair 设计在 LLM agent safety 领域罕见。Perturbation control（Δ_perturb=-0.67pp, CI 含零）有效排除表面文本扰动的替代解释。每对 clause 仅改变歧义、保持 policy intent 不变，因果推断设计合理。\n\n**S2** [共识] **Claim 校准得当**。论文系统性地使用 confound-free range（≥27.3pp）、upper bound 标记（incompleteness）、TOST sensitivity（7 margins）、bootstrap clustering，避免 over-claiming。C3（layer effect）inconclusive 被坦诚报告。SESOI 标为 \"pragmatic default, not principled\"。这种方法论诚实度在同类论文中不常见。\n\n**S3** [共识] **多层次复制增强可信度**。5 主模型 + 2 复制模型（7 models, 6 providers, 2 架构风格）；cross-judge 3-family validation（Fleiss' κ=0.717）；SOPBench 跨 benchmark 复制（方向一致）；ICC replication（0.919 within OpenAI family）。\n\n**S4** [共识] **Type→mechanism 的发现**。Cramér's V=0.45（type→mechanism）vs 0.14（type→rate）是一个有价值的理论贡献——说明 taxonomy 的价值在于 failure diagnosis 而非 rate prediction，为 targeted mitigation 提供 actionable framework。\n\n**S5** [共识] **控制实验的密度和透明度**。TOST 7-margin sensitivity、bootstrap clustering、incompleteness confound regression、cross-judge validation、severity threshold comparison、per-clause LOO analysis——robustness check 覆盖范围远超同类论文。\n\n**S6** [R1] **Disambiguation neglect 发现**。4.6% awareness rate + model-level 分化（GPT-4.1/Claude 10-11% vs Qwen3/DeepSeek 0%，p=2.2×10⁻⁹）有实践指导意义。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [共识: R1-N1 Must-Fix + R2-W2 Should-Fix→交叉后 AGREE 升级] **合成效应 34pp vs SOPBench 12.6pp（2.7×）缺乏桥接分析**\n\nAbstract 和 Conclusion 以 34.0pp/31.0pp 为 headline，SOPBench 自然语境复制仅 +12.6pp（其中 2/5 模型未达显著）。Discussion §7 仅一句 \"overestimates naturalistic effect sizes\"，未分析差距来源。Appendix Z 列出三个结构性差异但正文未引用。从业者无法判断实际部署中应参考哪个数字。\n\n→ 修改建议：(1) Abstract/Conclusion 同时报告合成上界和自然下界；(2) Discussion 用 2-3 句分析差距来源（measurement grain, baseline compression, interaction depth）；(3) 明确论文核心贡献在于因果机制识别而非精确效应量估算。\n\n**MF2** [共识: R1-N2 Must-Fix + R2 交叉后 AGREE] **跨领域 ρ=0.26 (p=0.62) 与 Abstract \"type-targeted diagnostics\" 泛化性 framing 矛盾**\n\nType ranking 在 retail vs airline 之间零相关（ρ=0.26）。Abstract 写 \"enabling type-targeted diagnosis for policy-governed deployments\" 无领域限定词。Conclusion 已有限定（\"within customer-service domains\"），但 Abstract 和 Introduction 的 contributions 列表未反映这一关键限制。需区分 binary effect 的跨领域稳健性（p=0.187）vs type ordering 的领域依赖性。\n\n→ 修改建议：Abstract 加 domain-specificity 限定词；Introduction contributions 列表限定 taxonomy 适用范围。修改代价低。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [分歧→妥协: R1-N3 Must-Fix, R2 REBUT→Should-Fix] **Authorization scope 构念效度问题需 consolidated 讨论**\n\nAuth scope 在六类中系统性异常：κ=0.385（低于 fair agreement 标准）、52pp 模型间变异（Claude 12% vs GPT-5.4 64%）、单独驱动 cross-judge ranking discordance（排除后 ρ 从 0.09→0.90）、驱动 C4 interaction（排除后 p=0.97）。论文在多处碎片化报告了这些问题（§5.2 + Appendix G + AA），但缺少 main text 中的 consolidated paragraph。R2 指出：透明度已充分、permission boundary 固有主观性是该类别在真实场景中危险的原因、post-hoc 排除有 researcher degrees of freedom 风险。\n\n→ 修改建议：§5.2 或 §7 增加一个 consolidated paragraph，集中讨论 auth scope 的构念效度挑战及为何保留。\n\n**SF2** [分歧→妥协: R2-N1 Must-Fix, R1 REBUT→Should-Fix] **Taxonomy 增量贡献论证——缺 Li et al. 11→6 映射表格**\n\n§3 提供了三条设计标准和排除举例（\"ellipsis and pragmatic implicature were excluded\"），论证逻辑完整。但读者无法快速查看完整的 11→6 映射关系。R1 指出用 Appendix AC 的 audit 数据论证覆盖度会引入循环论证。\n\n→ 修改建议：§3 或 Appendix 增加映射表格（提升可读性，非论证缺陷）。\n\n**SF3** [分歧→妥协: R2-N2 Must-Fix, R1 REBUT→Should-Fix] **\"Ambiguity\" 广义使用与 NLP 社区标准定义的张力**\n\n将 incompleteness、normative conflict、vagueness 纳入 \"ambiguity\"。§3 \"Scope of 'ambiguity'\" 段有操作定义（Wasow et al. 2005）和 RE 文献支撑（Dalpiaz et al. 2018），但未明确讨论与 NLP 传统分类（ambiguity vs vagueness vs incompleteness）的关系。R1 指出改用 \"specification defects\" 会脱离 NLP/CL 对话。\n\n→ 修改建议：§3 增加 1-2 句讨论与 NLP 传统分类的关系。\n\n**SF4** [共识] **\"Nocuous\" 术语从 divergent→convergent 的概念延伸**\n\nBerry & Kamsties (2004) 定义 nocuous = stakeholder divergence。本文 §6.3 发现 convergent error（models 收敛到同一错误解释）。Abstract 有 \"inverting...divergent to convergent\" 但不够明确。§6.3 的解释出现在第 8 页太晚。\n\n→ 修改建议：§1 首次使用 \"nocuous\" 时简要说明概念延伸。\n\n**SF5** [共识] **C3 inconclusive vs two-layer 组织框架**\n\nC3 未通过 Holm-Bonferroni（p=0.017, threshold 0.0125），但 taxonomy 仍按 linguistic/specification 两层展示。§3 已改为 \"design hypothesis\" 但仍隐含经验支撑。\n\n→ 修改建议：§3 显式声明 two-layer 是基于 RE 文献的组织框架，C3 检验结果为 inconclusive。\n\n**SF6** [共识] **ICC \"Reproducibility\" 标题误导**\n\nICC=0.919 仅在 OpenAI family 内计算。§4.5 标题 \"Reproducibility\" 暗示跨 provider 可复现性。论文补充的 \"C1 consistency across all seven models\" 仅说明方向一致，不等于 effect size 定量可复制。\n\n→ 修改建议：标题改为 \"Within-family reproducibility\" 或加限定词。\n\n**SF7** [共识] **60.8% 残差方差中 ~46% 系统性部分未讨论来源**\n\nDiscussion 仅说 \"likely reflects clause×context interactions\"，未进一步列举候选来源。\n\n→ 修改建议：Discussion 增加 2-3 句讨论可能来源（conversation trajectory, user persona, tool-use sequence）。\n\n**SF8** [共识] **Failure mode 分析表述过强**\n\nLLM-coded κ=0.52 vs human κ=0.15 表明 LLM 间\"一致性\"可能反映共享偏差。§6 标注 \"[Exploratory]\" 但叙事仍用 \"mechanistically distinct\" 等强断言。论文自己承认 2/6 type-mechanism 映射有 definitional affinity。\n\n→ 修改建议：§6 表述降级为 \"categorically distinct in LLM coding\"。\n\n**SF9** [共识] **Incompleteness confound: token count 是粗糙代理**\n\nAppendix F 承认 \"finer-grained semantic measures may reveal different confound structures\"，但 main text 未提及 token count 作为 information content 代理的局限性。\n\n→ 修改建议：§5.1 增加一句承认局限。\n\n**SF10** [共识] **Temperature=0 限制生态效度**\n\n所有实验 temperature=0。Limitations 仅一句 \"stochastic sampling remains untested\"，未讨论方向性预期。\n\n→ 修改建议：增加 1-2 句讨论 temperature>0 的可能影响方向。\n\n### Minor（不影响接收）\n\n**m1** [共识] 正文数字密度过高（Table 2 信息过载、§5.1 单段含 10+ 统计数字）——建议将 per-model rates 和 TOST tiers 移至 appendix。\n\n**m2** [R2] Disambiguation neglect 的增量贡献可更明确——增量在于因果框架下量化和 model-level 分化，非 \"LLM 不问问题\" 的泛泛观察。\n\n**m3** [R2] arXiv preprint 引用格式不统一。\n\n**m4** [R1] Abstract 中 Cramér's V=0.45 vs 0.14 缺乏即时上下文——读者不知道分别对应什么。\n\n**m5** [R1] ρ=0.09 two-group ranking discordance 在 §5.2 中位置不够显著——直接影响 C2 可信度。\n\n---\n\n## Reviewer Consensus\n\n以下问题被两位 Reviewer 独立标记并在交叉后确认共识：\n\n1. **合成 vs 自然效应量差距**（MF1）：34pp→12.6pp 需在正文充分讨论，Abstract 需同时报告两个数字\n2. **跨领域 taxonomy 泛化性限定**（MF2）：Abstract 需加 domain-specificity 限定词\n3. **\"Nocuous\" 术语延伸**（SF4）：divergent→convergent 的概念转换需更早、更明确论证\n4. **数字密度过高**（m1）：正文统计细节影响可读性\n5. **因果设计是核心方法论贡献**（S1）：两位 Reviewer 一致认可\n6. **Claim 校准得当**（S2）：方法论诚实度突出\n\n## Reviewer Divergence\n\n| 问题 | R1 判定 | R2 判定 | 合成判定 | 理由 |\n|------|---------|---------|----------|------|\n| Auth scope 构念效度 | Must-Fix (N3) | Should-Fix | **Should-Fix (SF1)** | 透明度已充分、构念主观性合理、post-hoc 排除有偏见风险；但需 consolidated paragraph |\n| Taxonomy 增量论证 | Should-Fix | Must-Fix (N1) | **Should-Fix (SF2)** | 论证逻辑完整（3 criteria + 排除举例），缺的是呈现形式 |\n| \"Ambiguity\" 术语 | Should-Fix | Must-Fix (N2) | **Should-Fix (SF3)** | 操作定义有文献支撑，改术语会脱离 NLP/CL 对话；但需加强讨论 |\n| Disambiguation neglect 新颖性 | Minor | Should-Fix (W4) | **Minor (m2)** | 增量在于因果框架+model-level 分化，文献中未有此量化 |\n\n---\n\n## Questions for Authors\n\n1. 合成效应 (34pp) 和 SOPBench 效应 (12.6pp) 之间 2.7× 差距，主要来源是什么？measurement granularity（constraint-level vs episode-level）是否足以解释全部差距？\n2. Authorization scope 的 κ=0.385 是否暗示需要更精细的操作定义？排除 auth scope 后 C2/C4 结论是否有实质性变化？（Appendix AA 部分回答，但 C2 ranking 变化未报告）\n3. 60.8% 残差方差中 ~46% 系统性部分，是否有初步证据指向主要来源？\n4. Temperature=0 下 permissive attractor (77%) 在 temperature>0 时是否可能改变？sampling randomness 是否会打破 convergent violation pattern？\n5. Failure mechanism 分类（structural misparse, gap-filling, boundary violation）是 post-hoc 编码的——type→mechanism 关联是否存在 circular reasoning 风险？LLM-coded κ=0.52 vs human κ=0.15 的差距如何解释？\n6. DRIP-R 的 \"no single correct resolution\" 范式 vs 本文 matched-pair ground truth 范式——发现可否推广到真正的开放式歧义场景？\n\n---\n\n## Missing References\n\n**已引用但讨论不足**:\n- DRIP-R (Borakoty et al., 2026)：正文仅在 §2 Related Work 中对比，Appendix L 做 category mapping。作为最直接的同期竞争工作，应在 §2 中用 2-3 句更充分对比方法论差异（matched-pair causal vs annotation-based, safety violations vs decision quality）。\n\n**可能遗漏**:\n- Gao-Arch et al. (2026) \"Ambiguity collapse in LLMs\"：与 systematic nocuity（convergent error）高度相关，值得在 §6.3 或 §7 对比讨论（论文已引用 gur_arieh_ambiguity_collapse_2026，需确认是否为同一工作）\n- Femmer et al. (2017)：RE 领域自动歧义检测综述，与 Appendix D detection experiment 相关\n- Anthropic Model Spec / Constitutional AI 系列：与 policy-governed agent behavior 的 alignment 方向直接相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（耗时 ~3 分钟）。0 critical, 1 warning, 13 info。\n\n主要发现：\n- **[warning]** Page 4-5 连续两页纯文本（Method §4.1-4.6），无 display item 穿插。建议用 models summary table 或 experimental design diagram 打破纯文本节奏。\n- **[info]** 首页无 display item（纯 Title + Abstract），审稿人翻到 page 2 才看到 Figure 1。不影响接收但错失首页锚定。\n- **[info]** Figure 1（Experimental Overview）锚定效果好，清晰传达端到端流程。\n- **[info]** Figure 3 热力图使用黄-红渐变色阶，非最佳色盲友好方案，但单元格内数值标注有效缓解。\n- **[info]** 正文 §1-§8 在 8 页内，Limitations 在 p9，格式合规。\n- **[info]** Appendix 表格字号偏小但可接受。\n\n视觉审查不影响评分或接收建议。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**Soundness**: 3.75/5（R1: 3.5, R2: 4.0）\n**Excitement**: 3.25/5（R1: 3.5, R2: 3.0）\n**Confidence**: 4/5（两位 Reviewer 一致）\n\n**判定理由**：\n\n论文回答了一个重要且及时的研究问题——policy ambiguity 是否以及如何因果地影响 LLM agent 安全。Matched-pair 因果设计在该领域罕见（S1），claim 校准得当（S2），控制实验覆盖全面（S5），type→mechanism 的诊断发现有理论价值（S4）。\n\n但两个 Must-Fix 问题构成接收障碍：(1) 合成效应（34pp）与自然效应（12.6pp）之间 2.7× 的差距未在正文充分讨论，Abstract/Conclusion 仅报告合成数字，对从业者有误导风险（MF1）；(2) 跨领域 type ranking 零相关（ρ=0.26）与 Abstract \"type-targeted diagnostics\" 的泛化性 framing 矛盾（MF2）。\n\n10 个 Should-Fix 问题（auth scope 构念效度、taxonomy 增量论证、ambiguity 术语、nocuous 概念延伸、C3/two-layer 框架、ICC 标题、残差方差讨论、failure mode 表述、incompleteness confound 局限、temperature=0）中，大部分为低成本修改（1-3 句话或术语调整），但数量累积仍反映论文在 framing 精度上的系统性不足。\n\n**修改后提升空间**：若 MF1 和 MF2 得到充分回应（Abstract 同时报告两个数字 + 加领域限定词 + Discussion 扩展 ecological validity），论文可达 4.0（Conference）。当前状态更适合 3.0-3.5（Findings 到 Borderline Conference）。\n\n**与 EMNLP ARR 评分标准的对应**：\n- 3.5 = Borderline Conference（可被主会议接收的边界线）\n- 论文有清晰的因果贡献和严谨的实验设计，但 ecological validity gap 和 framing 精度问题使其在 Conference 边界线上\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contributions 列表：C2 应限定 \"within customer-service domains\"\n- 首次使用 \"nocuous\" 时加简要说明概念延伸（从 divergent→convergent）\n- \"enabling type-targeted diagnosis for policy-governed deployments\" 加领域限定\n\n### §3 Taxonomy\n- 增加 Li et al. 11→6 映射表格（§3 或 Appendix）\n- \"Scope of 'ambiguity'\" 段增加 1-2 句讨论与 NLP 传统分类的关系\n- 开头显式声明 two-layer 是组织框架（organizational framework），C3 检验结果 inconclusive\n\n### §4 Method\n- §4.5 \"Reproducibility\" 标题改为 \"Within-family reproducibility\"\n- §4.5 incompleteness 讨论处增加一句承认 token count 是粗糙代理\n\n### §5 Results\n- §5.1 Abstract/Conclusion 同时报告合成上界（31.0pp confound-free）和自然下界（12.6pp SOPBench）\n- §5.2 或 §7 增加 auth scope 构念效度 consolidated paragraph\n\n### §6 Error Analysis\n- 开头加 caveat 段落强调 exploratory + LLM-coded 局限\n- \"mechanistically distinct\" 降级为 \"categorically distinct in LLM coding\"\n\n### §7 Discussion\n- Ecological validity 段扩展为 2-3 句，分析 2.7× 差距来源\n- 增加 2-3 句讨论 ~46% 系统性残差的候选来源\n- 增加 1-2 句讨论 temperature>0 的可能影响方向\n\n### §8 Conclusion\n- 同步 Abstract 修改（同时报告两个 effect size）\n- \"type-targeted diagnostics\" 加领域限定\n\n### Abstract\n- 同时报告合成上界和自然下界\n- Cramér's V=0.45 vs 0.14 加简要上下文说明\n- 加领域限定词\n\n### References\n- arXiv preprint 格式统一\n- 补充 DRIP-R 方法论差异对比（§2 Related Work）",
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 25 审稿报告 — 圆桌合成\n\n**论文**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\n**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n**轮次**: 1 轮（交叉后关键问题达成共识，无需第 2 轮）\n\n---\n\n## Summary\n\n本文研究 policy ambiguity 对 LLM agent 安全的因果影响。通过在 τ²-bench 上构造 300 对匹配 clause pairs（涵盖 6 类歧义），评估 5 个模型（2,997 episodes），发现歧义使违规率增加 31.0pp（confound-free types）/ 34.0pp（全部 6 types）。论文发现 type 仅解释 0.4% 的违规方差但预测 failure mechanism 的能力更强（Cramér's V=0.45 vs 0.14），将 taxonomy 定位为诊断工具。此外报告了 disambiguation neglect（4.6% awareness）和 systematic nocuity（41.3% 收敛违规，77% permissive bias）两个实证现象。\n\n---\n\n## Strengths\n\n**S1** [共识] **因果设计的稀缺性和严谨性**。Matched-pair 设计在 LLM agent safety 领域罕见。Perturbation control（Δ_perturb=-0.67pp, CI 含零）有效排除表面文本扰动的替代解释。每对 clause 仅改变歧义、保持 policy intent 不变，因果推断设计合理。\n\n**S2** [共识] **Claim 校准得当**。论文系统性地使用 confound-free range（≥27.3pp）、upper bound 标记（incompleteness）、TOST sensitivity（7 margins）、bootstrap clustering，避免 over-claiming。C3（layer effect）inconclusive 被坦诚报告。SESOI 标为 \"pragmatic default, not principled\"。这种方法论诚实度在同类论文中不常见。\n\n**S3** [共识] **多层次复制增强可信度**。5 主模型 + 2 复制模型（7 models, 6 providers, 2 架构风格）；cross-judge 3-family validation（Fleiss' κ=0.717）；SOPBench 跨 benchmark 复制（方向一致）；ICC replication（0.919 within OpenAI family）。\n\n**S4** [共识] **Type→mechanism 的发现**。Cramér's V=0.45（type→mechanism）vs 0.14（type→rate）是一个有价值的理论贡献——说明 taxonomy 的价值在于 failure diagnosis 而非 rate prediction，为 targeted mitigation 提供 actionable framework。\n\n**S5** [共识] **控制实验的密度和透明度**。TOST 7-margin sensitivity、bootstrap clustering、incompleteness confound regression、cross-judge validation、severity threshold comparison、per-clause LOO analysis——robustness check 覆盖范围远超同类论文。\n\n**S6** [R1] **Disambiguation neglect 发现**。4.6% awareness rate + model-level 分化（GPT-4.1/Claude 10-11% vs Qwen3/DeepSeek 0%，p=2.2×10⁻⁹）有实践指导意义。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [共识: R1-N1 Must-Fix + R2-W2 Should-Fix→交叉后 AGREE 升级] **合成效应 34pp vs SOPBench 12.6pp（2.7×）缺乏桥接分析**\n\nAbstract 和 Conclusion 以 34.0pp/31.0pp 为 headline，SOPBench 自然语境复制仅 +12.6pp（其中 2/5 模型未达显著）。Discussion §7 仅一句 \"overestimates naturalistic effect sizes\"，未分析差距来源。Appendix Z 列出三个结构性差异但正文未引用。从业者无法判断实际部署中应参考哪个数字。\n\n→ 修改建议：(1) Abstract/Conclusion 同时报告合成上界和自然下界；(2) Discussion 用 2-3 句分析差距来源（measurement grain, baseline compression, interaction depth）；(3) 明确论文核心贡献在于因果机制识别而非精确效应量估算。\n\n**MF2** [共识: R1-N2 Must-Fix + R2 交叉后 AGREE] **跨领域 ρ=0.26 (p=0.62) 与 Abstract \"type-targeted diagnostics\" 泛化性 framing 矛盾**\n\nType ranking 在 retail vs airline 之间零相关（ρ=0.26）。Abstract 写 \"enabling type-targeted diagnosis for policy-governed deployments\" 无领域限定词。Conclusion 已有限定（\"within customer-service domains\"），但 Abstract 和 Introduction 的 contributions 列表未反映这一关键限制。需区分 binary effect 的跨领域稳健性（p=0.187）vs type ordering 的领域依赖性。\n\n→ 修改建议：Abstract 加 domain-specificity 限定词；Introduction contributions 列表限定 taxonomy 适用范围。修改代价低。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [分歧→妥协: R1-N3 Must-Fix, R2 REBUT→Should-Fix] **Authorization scope 构念效度问题需 consolidated 讨论**\n\nAuth scope 在六类中系统性异常：κ=0.385（低于 fair agreement 标准）、52pp 模型间变异（Claude 12% vs GPT-5.4 64%）、单独驱动 cross-judge ranking discordance（排除后 ρ 从 0.09→0.90）、驱动 C4 interaction（排除后 p=0.97）。论文在多处碎片化报告了这些问题（§5.2 + Appendix G + AA），但缺少 main text 中的 consolidated paragraph。R2 指出：透明度已充分、permission boundary 固有主观性是该类别在真实场景中危险的原因、post-hoc 排除有 researcher degrees of freedom 风险。\n\n→ 修改建议：§5.2 或 §7 增加一个 consolidated paragraph，集中讨论 auth scope 的构念效度挑战及为何保留。\n\n**SF2** [分歧→妥协: R2-N1 Must-Fix, R1 REBUT→Should-Fix] **Taxonomy 增量贡献论证——缺 Li et al. 11→6 映射表格**\n\n§3 提供了三条设计标准和排除举例（\"ellipsis and pragmatic implicature were excluded\"），论证逻辑完整。但读者无法快速查看完整的 11→6 映射关系。R1 指出用 Appendix AC 的 audit 数据论证覆盖度会引入循环论证。\n\n→ 修改建议：§3 或 Appendix 增加映射表格（提升可读性，非论证缺陷）。\n\n**SF3** [分歧→妥协: R2-N2 Must-Fix, R1 REBUT→Should-Fix] **\"Ambiguity\" 广义使用与 NLP 社区标准定义的张力**\n\n将 incompleteness、normative conflict、vagueness 纳入 \"ambiguity\"。§3 \"Scope of 'ambiguity'\" 段有操作定义（Wasow et al. 2005）和 RE 文献支撑（Dalpiaz et al. 2018），但未明确讨论与 NLP 传统分类（ambiguity vs vagueness vs incompleteness）的关系。R1 指出改用 \"specification defects\" 会脱离 NLP/CL 对话。\n\n→ 修改建议：§3 增加 1-2 句讨论与 NLP 传统分类的关系。\n\n**SF4** [共识] **\"Nocuous\" 术语从 divergent→convergent 的概念延伸**\n\nBerry & Kamsties (2004) 定义 nocuous = stakeholder divergence。本文 §6.3 发现 convergent error（models 收敛到同一错误解释）。Abstract 有 \"inverting...divergent to convergent\" 但不够明确。§6.3 的解释出现在第 8 页太晚。\n\n→ 修改建议：§1 首次使用 \"nocuous\" 时简要说明概念延伸。\n\n**SF5** [共识] **C3 inconclusive vs two-layer 组织框架**\n\nC3 未通过 Holm-Bonferroni（p=0.017, threshold 0.0125），但 taxonomy 仍按 linguistic/specification 两层展示。§3 已改为 \"design hypothesis\" 但仍隐含经验支撑。\n\n→ 修改建议：§3 显式声明 two-layer 是基于 RE 文献的组织框架，C3 检验结果为 inconclusive。\n\n**SF6** [共识] **ICC \"Reproducibility\" 标题误导**\n\nICC=0.919 仅在 OpenAI family 内计算。§4.5 标题 \"Reproducibility\" 暗示跨 provider 可复现性。论文补充的 \"C1 consistency across all seven models\" 仅说明方向一致，不等于 effect size 定量可复制。\n\n→ 修改建议：标题改为 \"Within-family reproducibility\" 或加限定词。\n\n**SF7** [共识] **60.8% 残差方差中 ~46% 系统性部分未讨论来源**\n\nDiscussion 仅说 \"likely reflects clause×context interactions\"，未进一步列举候选来源。\n\n→ 修改建议：Discussion 增加 2-3 句讨论可能来源（conversation trajectory, user persona, tool-use sequence）。\n\n**SF8** [共识] **Failure mode 分析表述过强**\n\nLLM-coded κ=0.52 vs human κ=0.15 表明 LLM 间\"一致性\"可能反映共享偏差。§6 标注 \"[Exploratory]\" 但叙事仍用 \"mechanistically distinct\" 等强断言。论文自己承认 2/6 type-mechanism 映射有 definitional affinity。\n\n→ 修改建议：§6 表述降级为 \"categorically distinct in LLM coding\"。\n\n**SF9** [共识] **Incompleteness confound: token count 是粗糙代理**\n\nAppendix F 承认 \"finer-grained semantic measures may reveal different confound structures\"，但 main text 未提及 token count 作为 information content 代理的局限性。\n\n→ 修改建议：§5.1 增加一句承认局限。\n\n**SF10** [共识] **Temperature=0 限制生态效度**\n\n所有实验 temperature=0。Limitations 仅一句 \"stochastic sampling remains untested\"，未讨论方向性预期。\n\n→ 修改建议：增加 1-2 句讨论 temperature>0 的可能影响方向。\n\n### Minor（不影响接收）\n\n**m1** [共识] 正文数字密度过高（Table 2 信息过载、§5.1 单段含 10+ 统计数字）——建议将 per-model rates 和 TOST tiers 移至 appendix。\n\n**m2** [R2] Disambiguation neglect 的增量贡献可更明确——增量在于因果框架下量化和 model-level 分化，非 \"LLM 不问问题\" 的泛泛观察。\n\n**m3** [R2] arXiv preprint 引用格式不统一。\n\n**m4** [R1] Abstract 中 Cramér's V=0.45 vs 0.14 缺乏即时上下文——读者不知道分别对应什么。\n\n**m5** [R1] ρ=0.09 two-group ranking discordance 在 §5.2 中位置不够显著——直接影响 C2 可信度。\n\n---\n\n## Reviewer Consensus\n\n以下问题被两位 Reviewer 独立标记并在交叉后确认共识：\n\n1. **合成 vs 自然效应量差距**（MF1）：34pp→12.6pp 需在正文充分讨论，Abstract 需同时报告两个数字\n2. **跨领域 taxonomy 泛化性限定**（MF2）：Abstract 需加 domain-specificity 限定词\n3. **\"Nocuous\" 术语延伸**（SF4）：divergent→convergent 的概念转换需更早、更明确论证\n4. **数字密度过高**（m1）：正文统计细节影响可读性\n5. **因果设计是核心方法论贡献**（S1）：两位 Reviewer 一致认可\n6. **Claim 校准得当**（S2）：方法论诚实度突出\n\n## Reviewer Divergence\n\n| 问题 | R1 判定 | R2 判定 | 合成判定 | 理由 |\n|------|---------|---------|----------|------|\n| Auth scope 构念效度 | Must-Fix (N3) | Should-Fix | **Should-Fix (SF1)** | 透明度已充分、构念主观性合理、post-hoc 排除有偏见风险；但需 consolidated paragraph |\n| Taxonomy 增量论证 | Should-Fix | Must-Fix (N1) | **Should-Fix (SF2)** | 论证逻辑完整（3 criteria + 排除举例），缺的是呈现形式 |\n| \"Ambiguity\" 术语 | Should-Fix | Must-Fix (N2) | **Should-Fix (SF3)** | 操作定义有文献支撑，改术语会脱离 NLP/CL 对话；但需加强讨论 |\n| Disambiguation neglect 新颖性 | Minor | Should-Fix (W4) | **Minor (m2)** | 增量在于因果框架+model-level 分化，文献中未有此量化 |\n\n---\n\n## Questions for Authors\n\n1. 合成效应 (34pp) 和 SOPBench 效应 (12.6pp) 之间 2.7× 差距，主要来源是什么？measurement granularity（constraint-level vs episode-level）是否足以解释全部差距？\n2. Authorization scope 的 κ=0.385 是否暗示需要更精细的操作定义？排除 auth scope 后 C2/C4 结论是否有实质性变化？（Appendix AA 部分回答，但 C2 ranking 变化未报告）\n3. 60.8% 残差方差中 ~46% 系统性部分，是否有初步证据指向主要来源？\n4. Temperature=0 下 permissive attractor (77%) 在 temperature>0 时是否可能改变？sampling randomness 是否会打破 convergent violation pattern？\n5. Failure mechanism 分类（structural misparse, gap-filling, boundary violation）是 post-hoc 编码的——type→mechanism 关联是否存在 circular reasoning 风险？LLM-coded κ=0.52 vs human κ=0.15 的差距如何解释？\n6. DRIP-R 的 \"no single correct resolution\" 范式 vs 本文 matched-pair ground truth 范式——发现可否推广到真正的开放式歧义场景？\n\n---\n\n## Missing References\n\n**已引用但讨论不足**:\n- DRIP-R (Borakoty et al., 2026)：正文仅在 §2 Related Work 中对比，Appendix L 做 category mapping。作为最直接的同期竞争工作，应在 §2 中用 2-3 句更充分对比方法论差异（matched-pair causal vs annotation-based, safety violations vs decision quality）。\n\n**可能遗漏**:\n- Gao-Arch et al. (2026) \"Ambiguity collapse in LLMs\"：与 systematic nocuity（convergent error）高度相关，值得在 §6.3 或 §7 对比讨论（论文已引用 gur_arieh_ambiguity_collapse_2026，需确认是否为同一工作）\n- Femmer et al. (2017)：RE 领域自动歧义检测综述，与 Appendix D detection experiment 相关\n- Anthropic Model Spec / Constitutional AI 系列：与 policy-governed agent behavior 的 alignment 方向直接相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（耗时 ~3 分钟）。0 critical, 1 warning, 13 info。\n\n主要发现：\n- **[warning]** Page 4-5 连续两页纯文本（Method §4.1-4.6），无 display item 穿插。建议用 models summary table 或 experimental design diagram 打破纯文本节奏。\n- **[info]** 首页无 display item（纯 Title + Abstract），审稿人翻到 page 2 才看到 Figure 1。不影响接收但错失首页锚定。\n- **[info]** Figure 1（Experimental Overview）锚定效果好，清晰传达端到端流程。\n- **[info]** Figure 3 热力图使用黄-红渐变色阶，非最佳色盲友好方案，但单元格内数值标注有效缓解。\n- **[info]** 正文 §1-§8 在 8 页内，Limitations 在 p9，格式合规。\n- **[info]** Appendix 表格字号偏小但可接受。\n\n视觉审查不影响评分或接收建议。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**Soundness**: 3.75/5（R1: 3.5, R2: 4.0）\n**Excitement**: 3.25/5（R1: 3.5, R2: 3.0）\n**Confidence**: 4/5（两位 Reviewer 一致）\n\n**判定理由**：\n\n论文回答了一个重要且及时的研究问题——policy ambiguity 是否以及如何因果地影响 LLM agent 安全。Matched-pair 因果设计在该领域罕见（S1），claim 校准得当（S2），控制实验覆盖全面（S5），type→mechanism 的诊断发现有理论价值（S4）。\n\n但两个 Must-Fix 问题构成接收障碍：(1) 合成效应（34pp）与自然效应（12.6pp）之间 2.7× 的差距未在正文充分讨论，Abstract/Conclusion 仅报告合成数字，对从业者有误导风险（MF1）；(2) 跨领域 type ranking 零相关（ρ=0.26）与 Abstract \"type-targeted diagnostics\" 的泛化性 framing 矛盾（MF2）。\n\n10 个 Should-Fix 问题（auth scope 构念效度、taxonomy 增量论证、ambiguity 术语、nocuous 概念延伸、C3/two-layer 框架、ICC 标题、残差方差讨论、failure mode 表述、incompleteness confound 局限、temperature=0）中，大部分为低成本修改（1-3 句话或术语调整），但数量累积仍反映论文在 framing 精度上的系统性不足。\n\n**修改后提升空间**：若 MF1 和 MF2 得到充分回应（Abstract 同时报告两个数字 + 加领域限定词 + Discussion 扩展 ecological validity），论文可达 4.0（Conference）。当前状态更适合 3.0-3.5（Findings 到 Borderline Conference）。\n\n**与 EMNLP ARR 评分标准的对应**：\n- 3.5 = Borderline Conference（可被主会议接收的边界线）\n- 论文有清晰的因果贡献和严谨的实验设计，但 ecological validity gap 和 framing 精度问题使其在 Conference 边界线上\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contributions 列表：C2 应限定 \"within customer-service domains\"\n- 首次使用 \"nocuous\" 时加简要说明概念延伸（从 divergent→convergent）\n- \"enabling type-targeted diagnosis for policy-governed deployments\" 加领域限定\n\n### §3 Taxonomy\n- 增加 Li et al. 11→6 映射表格（§3 或 Appendix）\n- \"Scope of 'ambiguity'\" 段增加 1-2 句讨论与 NLP 传统分类的关系\n- 开头显式声明 two-layer 是组织框架（organizational framework），C3 检验结果 inconclusive\n\n### §4 Method\n- §4.5 \"Reproducibility\" 标题改为 \"Within-family reproducibility\"\n- §4.5 incompleteness 讨论处增加一句承认 token count 是粗糙代理\n\n### §5 Results\n- §5.1 Abstract/Conclusion 同时报告合成上界（31.0pp confound-free）和自然下界（12.6pp SOPBench）\n- §5.2 或 §7 增加 auth scope 构念效度 consolidated paragraph\n\n### §6 Error Analysis\n- 开头加 caveat 段落强调 exploratory + LLM-coded 局限\n- \"mechanistically distinct\" 降级为 \"categorically distinct in LLM coding\"\n\n### §7 Discussion\n- Ecological validity 段扩展为 2-3 句，分析 2.7× 差距来源\n- 增加 2-3 句讨论 ~46% 系统性残差的候选来源\n- 增加 1-2 句讨论 temperature>0 的可能影响方向\n\n### §8 Conclusion\n- 同步 Abstract 修改（同时报告两个 effect size）\n- \"type-targeted diagnostics\" 加领域限定\n\n### Abstract\n- 同时报告合成上界和自然下界\n- Cramér's V=0.45 vs 0.14 加简要上下文说明\n- 加领域限定词\n\n### References\n- arXiv preprint 格式统一\n- 补充 DRIP-R 方法论差异对比（§2 Related Work）",
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 2220 · 2026-05-23T09:54:52.255955+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4015
}
```

</details>

---


### Assistant

_source line 2221 · 2026-05-23T09:55:03.582313+00:00_

Round 25 审稿完成。

**最终评分：3.5 — Borderline Conference**

报告已投递给 Research Director。核心结论：

**2 个 Must-Fix**（影响接收）：
1. 合成效应 34pp vs SOPBench 12.6pp（2.7×差距）缺乏桥接分析——Abstract/Conclusion 需同时报告两个数字
2. 跨领域 ρ=0.26 与 Abstract "type-targeted diagnostics" 泛化性 framing 矛盾——需加领域限定词

**10 个 Should-Fix**：auth scope 构念效度 consolidated 讨论、taxonomy 11→6 映射表格、ambiguity 术语讨论、nocuous 概念延伸标注、C3/two-layer 显式声明、ICC 标题修改、残差方差来源讨论、failure mode 表述降级、incompleteness confound 局限承认、temperature=0 方向性讨论

**关键判断**：两个 Must-Fix 均为低成本修改（Abstract wording + Discussion 扩展 2-3 句），若充分回应可升至 4.0（Conference）。Issue Tracker 已同步更新（12 个 R24 issue resolved，13 个 R25 active issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 214

## Round 214

2 recorded events


### User

_source line 2222 · 2026-05-23T09:55:06.173295+00:00_

[Reviewer 2 审稿结果]:
两轮审稿完成：

1. **Round 1 初审**：提交了完整审稿报告，Overall 3.5（Borderline Conference）。标记了 2 个 Must-Fix（taxonomy 增量论证不足 N1、"ambiguity"广义使用 N2）、5 个 Should-Fix（C3 inconclusive W1、ecological validity gap W2、nocuous 术语 W3、disambiguation neglect 新颖性 W4、数字密度 W5）。

2. **交叉回应 R1**：逐条回应了 R1 的 3 个 Must-Fix、5 个 Should-Fix 和 5 个 Minor。与 R1 在 4 个关键问题上达成独立共识（效应量差距、nocuous 术语、数字密度、泛化性限定）。对 R1-N3（auth scope 构念效度）给出了 REBUT——同意问题存在但建议降级为 Should-Fix，因为论文已透明报告且 post-hoc 排除引入新偏见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2223 · 2026-05-23T09:55:20.376981+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **Overall**: 3.5 — Borderline Conference
- **2 个 Must-Fix**：(1) 合成效应 34pp vs SOPBench 12.6pp 差距未在 Abstract/Conclusion 充分讨论；(2) 跨领域 ρ=0.26 与 Abstract "type-targeted diagnostics" 泛化性 framing 矛盾
- **10 个 Should-Fix**：auth scope 构念效度、taxonomy 增量论证、ambiguity 术语、nocuous 概念延伸、C3/two-layer、ICC 标题、残差方差、failure mode 表述、incompleteness confound、temperature=0
- **5 个 Minor**：数字密度、disambiguation neglect 增量、arXiv 格式、Cramér's V 上下文、ρ=0.09 可见度
- **Issue Tracker 已更新**：12 个 R24 issue 标记 resolved，13 个 R25 active issue 创建
- **视觉审查**：已完成，0 critical，1 warning（pp.4-5 纯文本节奏）
- **修改后提升空间**：若 MF1/MF2 得到充分回应，可达 4.0（Conference）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 215

## Round 215

62 recorded events


### User

_source line 2224 · 2026-05-23T11:39:53.499020+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2225 · 2026-05-23T11:39:58.915114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2226 · 2026-05-23T11:39:58.966588+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2227 · 2026-05-23T11:40:04.839611+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2228 · 2026-05-23T11:40:04.890227+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2229 · 2026-05-23T11:40:08.505084+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 2230 · 2026-05-23T11:40:08.605927+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2231 · 2026-05-23T11:40:12.287114+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2232 · 2026-05-23T11:40:12.287585+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2233 · 2026-05-23T11:40:14.044672+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2234 · 2026-05-23T11:40:14.145529+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2235 · 2026-05-23T11:40:20.627972+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2236 · 2026-05-23T11:40:22.292479+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1664
}
```

</details>

---


### Tool call

_source line 2237 · 2026-05-23T11:40:22.292983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2238 · 2026-05-23T11:40:22.795174+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
18	
19	\definecolor{speccolor}{HTML}{C44E52}
20	\definecolor{lingcolor}{HTML}{4C72B0}
21	
22	\title{Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{sections/abstract}
30	\input{sections/introduction}
31	\input{sections/related_work}
32	\input{sections/taxonomy}
33	\input{sections/method}
34	\input{sections/experiments}
35	\input{sections/analysis}
36	\input{sections/discussion}
37	\input{sections/conclusion}
38	\input{sections/limitations}
39	
40	\bibliography{references}
41	
42	\appendix
43	\makeatletter
44	\newcommand{\extAlph}[1]{%
45	  \ifcase#1\or A\or B\or C\or D\or E\or F\or G\or H\or I\or J\or K\or L\or M\or N\or O\or P\or Q\or R\or S\or T\or U\or V\or W\or X\or Y\or Z\or AA\or AB\or AC\or AD\or AE\fi}
46	\renewcommand{\thesection}{\extAlph{\value{section}}}
47	\makeatother
48	\input{sections/appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2239 · 2026-05-23T11:40:22.795530+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2240 · 2026-05-23T11:40:22.795696+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2241 · 2026-05-23T11:40:23.248008+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2242 · 2026-05-23T11:40:23.299055+00:00_

1	## Review Issues Tracker — policy_ambiguity_safety
2	## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Latest Round: 25
5	
6	# ============================================================
7	# R25 ISSUES — ACTIVE
8	# ============================================================
9	
10	- id: "R25-N1"
11	  summary: "合成效应 34pp vs SOPBench 12.6pp (2.7×) 缺乏桥接分析——Abstract/Conclusion 未报告自然下界"
12	  category: framing
13	  severity: critical
14	  status: in_progress
15	  first_raised_round: 21
16	  last_seen_round: 25
17	  mentions:
18	    - round: 24
19	      reviewers: [1, 2]
20	      note: "R24-N3: SOPBench 63% 压缩未充分讨论"
21	    - round: 25
22	      reviewers: [1, 2]
23	      note: "R1 Must-Fix N1, R2 Should-Fix W2→交叉后 AGREE 升级。共识 Must-Fix：Abstract/Conclusion 需同时报告 34pp 和 12.6pp，Discussion 需 2-3 句分析差距来源"
24	  action_items:
25	    - round: 25
26	      action: "Abstract/Conclusion 同时报告合成上界(34pp/31pp)和自然下界(12.6pp)；Discussion ecological validity 段扩展为 2-3 句分析差距来源(measurement grain, baseline compression, interaction depth)"
27	      assigned_to: paper_agent
28	      status: done
29	  resolution: "Abstract adds SOPBench +12.6pp after overall effect; Conclusion adds SOPBench number; Discussion ecological validity paragraph rewritten with topic sentence + 3 compression factors inline"
30	  resolution_round: null
31	
32	- id: "R25-N2"
33	  summary: "跨领域 ρ=0.26 (p=0.62) vs Abstract 'type-targeted diagnostics' 泛化性 framing 矛盾"
34	  category: framing
35	  severity: critical
36	  status: in_progress
37	  first_raised_round: 24
38	  last_seen_round: 25
39	  mentions:
40	    - round: 24
41	      reviewers: [1, 2]
42	      note: "R24-W7: Conclusion 需限定适用范围"
43	    - round: 25
44	      reviewers: [1, 2]
45	      note: "R1 Must-Fix N2, R2 交叉后 AGREE。Abstract 无领域限定词。Conclusion 已有限定('within customer-service domains')，修复集中在 Abstract wording"
46	  action_items:
47	    - round: 25
48	      action: "Abstract 加 domain-s
…[truncated 18907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2243 · 2026-05-23T11:40:32.536856+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 2244 · 2026-05-23T11:40:35.096988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2245 · 2026-05-23T11:40:35.448770+00:00_

1	\begin{abstract}
2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. Using a matched-pair causal design on $\tau^2$-bench with 300 clause pairs spanning a six-type taxonomy evaluated across five models, we show that ambiguous clauses increase violations by 31.0 percentage points in confound-free types (34.0\,pp overall); cross-benchmark replication on SOPBench confirms directional consistency at reduced magnitude ($+$12.7\,pp; Appendix~\ref{app:sopbench}). However, ambiguity \emph{type} predicts \emph{how} agents fail, not \emph{whether} they fail: type membership explains only 0.4\% of violation variance versus 22.4\% for individual clause wording, yet predicts failure mechanism substantially more strongly than violation rate (Cram\'{e}r's $V = 0.45$ vs.\ $0.14$). This \emph{type--mechanism dissociation} establishes the taxonomy as a diagnostic instrument---identifying type-specific failure modes such as structural misparse and boundary violation---rather than a risk classifier. Error analysis reveals two convergent phenomena: \emph{disambiguation neglect} (4.6\% awareness) and \emph{systematic nocuity}---models converge on identical policy violations with 77\% permissive bias, inverting \citeauthor{berry_kamsties_2004}'s divergent interpretation to convergent error. These findings, established under controlled synthetic conditions in two customer-service domains, motivate clause-level policy auditing over type-level risk screening.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2246 · 2026-05-23T11:40:35.449266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2247 · 2026-05-23T11:40:35.600248+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity---a pilot audit of 407 clauses from 24 production policy documents finds 55--87\% contain at least one ambiguity type (dual-judge $\kappa = 0.30$; range reflects union vs.\ intersection; Appendix~\ref{app:prevalence})---a property studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements. We show that LLM agents invert this pattern, exhibiting \emph{convergent} rather than divergent misinterpretation (\S\ref{sec:analysis}).
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy underst
…[truncated 2699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2248 · 2026-05-23T11:40:35.952179+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 2249 · 2026-05-23T11:40:36.354192+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Traditional NLP ambiguity classification focuses on within-sentence phenomena \citep{wasow_ambiguity_2005}; our specification layer captures document-level policy gaps unstudied in the agent context. Our taxonomy provides an organizational framework of six types organized into two layers (Table~\ref{tab:taxonomy}), selected from \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types; full mapping in Appendix~\ref{app:li_mapping}) based on three design criteria: (1)~theoretical attestation in prior RE literature \citep{massey_ambiguity_re_2014,berry_kamsties_2004,drip_r_2026}, (2)~amenability to minimal-pair construction without altering clause semantics beyond the target ambiguity, and (3)~mutual exclusivity for unambiguous IV assignment. Types such as ellipsis and pragmatic implicature were excluded because they resist minimal-pair construction within the single-clause policy format.
7	
8	\begin{table}[t]
9	\centering
10	\footnotesize
11	\caption{Six-type ambiguity taxonomy. Disambiguation channel indicates the primary mechanism required to resolve the ambiguity.}
12	\label{tab:taxonomy}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}llll@{}}
15	\toprule
16	\textbf{Type} & \textbf{Layer} & \textbf{Definition} & \textbf{Disambig.\ Channel} \\
17	\midrule
18	Lexical & Ling. & Word/phrase admits multiple senses & Context \\
19	Scopal & Ling. & Quantifier/operator scope underdetermined & Bracketing \\
20	Coreferential & Ling. & Pronoun/NP referent is ambiguous & Resolution \\
21	Auth.\ Scope & Spec. & Permission boundary is vague & Boundary def. \\
22	Incompletene
…[truncated 3061 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2250 · 2026-05-23T11:40:36.354749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2251 · 2026-05-23T11:40:36.405381+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300; Cohen's $\kappa = 0.95$ on six-type classification); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We
…[truncated 4375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2252 · 2026-05-23T11:40:46.293404+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 Workshop NLLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FNLLP_ARR_Commitment"}]

Based on the search results, here's comprehensive information about EMNLP 2026 call for papers, ARR submission guidelines, and author instructions:

## Key Submission Information

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail 
…[truncated 2679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 13756
}
```

</details>

---


### Tool call

_source line 2253 · 2026-05-23T11:40:51.413447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2254 · 2026-05-23T11:40:51.715274+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around three analyses: the binary ambiguity effect (C1), the type partial ordering (C2, including the inconclusive layer effect C3), and the model$\times$type interaction (C4). C1 and C2 are primary supported claims; C3 (layer effect) is inconclusive; C4 (model$\times$type interaction) is exploratory.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity (\S\ref{sec:method}). A Type III sum-of-squares decomposition\footnote{Type III SS avoids ordering dependence in our unbalanced design; logistic regression (Appendix~\ref{app:regression}) confirms concordant results (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}).} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (of which $\sim$15\% is stochastic and $\sim$46\% systematic, estimated from an OpenAI-family ICC replication; Appendix~\ref{app:residual}). A permutation test confirms that clause wording---not type membership---drives this variance ($p < 0.001$; Appendix~\ref{app:clause_variance}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; controlling for token count---a coarse proxy for information content---changes no type's predicted effect by more than 0.1\,pp (Appendix~\ref{app:confound}). The confound-free range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope); excluding incompleteness entirely, the pooled effect is $+$31.0\,pp (95\% CI $[27.9, 34.1]$).
9	
10	Replication on two additional models confirms t
…[truncated 6029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2255 · 2026-05-23T11:40:51.715644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 2256 · 2026-05-23T11:40:52.719876+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_type_mechanism.pdf}
7	\caption{Type--mechanism association (percentage of violation traces per type assigned to each failure mechanism). Each type maps to a dominant mechanism ($\geq$3/5 model consistency), supporting the taxonomy's diagnostic value (NMI $= 0.23$, Cram\'{e}r's $V = 0.45$).}
8	\label{fig:type_mechanism}
9	\end{figure}
10	
11	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
12	
13	We analyze 614 violation traces across all five models, coded into five failure modes (Gwet's AC$_1$ $= 0.62$, $\kappa = 0.52$ \citep{gwet_2014,cohen_1960}). The failure mode coder prompt receives the agent trajectory, policy clause, ground truth, and violation assessment, but does \emph{not} include the ambiguity type label; type is assigned programmatically post hoc. Using LLMs to code LLM failures introduces circularity risk; however, mutual information between type (exogenous) and mechanism labels ($I(\text{type}; \text{mechanism}) = 0.41$ bits, $V = 0.45$; Appendix~\ref{app:type_mechanism}) provides structural evidence against this. This association is computed from LLM-coded labels; human mechanism coding yields lower agreement ($\kappa = 0.15$; Appendix~\ref{app:human_validation}), so absolute NMI should be interpreted as an upper bound on the true type--mechanism association. The following failure mode patterns should therefore be interpreted as consistent LLM categorization tendencies rather than ground-truth mechanism assignments. Two of the six type--mechanism mappings reflect partial definitional affinity (authorization scope$\to$boundary violation, incompleteness$\to$gap-filling); the remaining four (e.g., scopal$\to$structural misparse, 82.7\% cross-model consistency) are empirically derived.
14	
15	\subsection
…[truncated 2774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2257 · 2026-05-23T11:40:52.720324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2258 · 2026-05-23T11:40:53.224579+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Type--mechanism dissociation and intervention design.}
5	The central finding is a type--mechanism dissociation: type predicts failure mechanism more strongly than violation rate (Cram\'{e}r's $V = 0.45$ vs.\ $0.14$), reframing the taxonomy from risk classifier to diagnostic instrument. The binary effect is domain-robust ($p = 0.187$) but type rankings require per-domain calibration ($\rho = 0.26$; Appendix~\ref{app:cross_domain}). Of the 60.8\% residual ($\sim$15\% stochastic, $\sim$46\% systematic; Appendix~\ref{app:residual}), the explained 39.2\% is comparable to behavioral research norms \citep{berry_kamsties_2004,willis_nocuous_2008}; the systematic component reflects clause-level interactions---conversation trajectory, tool-use sequencing, clause$\times$scenario contingencies---that type-level taxonomies cannot capture, motivating clause-level auditing (even perfect disambiguation addresses $\leq$22.4\% of variance). Prompt-based mitigation is type-dependent (Appendix~\ref{app:mitigation}), reinforcing policy-design over prompt-level fixes. Authorization scope is a construct outlier ($\kappa = 0.385$, 52\,pp range); core conclusions hold without it (Appendix~\ref{app:sans_auth}).
6	
7	\paragraph{Ecological validity.}
8	This paper identifies causal mechanisms, not deployment-ready effect sizes. The SOPBench replication ($+$12.7\,pp vs.\ $+$34.0\,pp; Appendix~\ref{app:sopbench}) confirms directional consistency; the $2.7\times$ compression reflects measurement grain (constraint- vs.\ episode-level), baseline compression (22.7\% vs.\ 6.9\%), and interaction depth (single- vs.\ multi-turn). The dissociation depends on mechanism structure, not magnitude, generalizing independently of effect size calibration.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 2259 · 2026-05-23T11:40:53.224932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2260 · 2026-05-23T11:40:53.476033+00:00_

1	\enlargethispage{6\baselineskip}
2	\section{Conclusion}
3	
4	In customer-service domains under controlled conditions, policy ambiguity increases agent violations by 31.0\,pp (confound-free; 95\% CI $[27.9, 34.1]$); SOPBench confirms directional consistency ($+$12.7\,pp). A type--mechanism dissociation ($V = 0.45$ vs.\ $0.14$) establishes the taxonomy as a diagnostic instrument: type predicts \emph{how} agents fail, not \emph{whether}. With $>$89\% disambiguation neglect, $>$40\% convergent violations, and 60.8\% clause-level variance, clause-level policy auditing is the actionable intervention for policy-governed deployments.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2261 · 2026-05-23T11:40:53.476464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2262 · 2026-05-23T11:40:53.526943+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our ambiguity pairs are synthetically constructed, so the 34.0\,pp effect is an upper bound; the SOPBench replication ($+$12.7\,pp) provides a cross-benchmark lower bound. We evaluate seven API-accessible models across two customer-service domains at temperature $= 0$; other domains, smaller models, and stochastic sampling remain untested. Failure mode coding relies on LLM annotators ($\kappa = 0.52$; human $\kappa = 0.15$), though the coder prompt excludes ambiguity type labels, preventing type--mechanism contamination. At temperature $> 0$, stochastic sampling would likely increase variance in both conditions but is unlikely to eliminate the directional effect, given its magnitude ($+$31.0\,pp confound-free) and cross-model consistency.
5	
6	\section*{Data and Code Availability}
7	The 300 clause pairs, evaluation pipeline, analysis scripts, and raw episode traces will be released upon publication at \url{https://github.com/anonymous/policy-ambiguity-safety}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2263 · 2026-05-23T11:41:00.353368+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2264 · 2026-05-23T11:41:00.705214+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_l
…[truncated 4154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2265 · 2026-05-23T11:41:00.705676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2266 · 2026-05-23T11:41:01.159038+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 58396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2267 · 2026-05-23T11:41:01.159559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 2268 · 2026-05-23T11:41:01.260482+00:00_

1	@inproceedings{li_ambiguity_taxonomy_2024,
2	  title={A Taxonomy of Ambiguity Types for {NLP}},
3	  author={Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.},
4	  booktitle={Proceedings of EACL 2024},
5	  year={2024}
6	}
7	
8	@inproceedings{massey_ambiguity_re_2014,
9	  title={Identifying and Classifying Ambiguity for Regulatory Requirements},
10	  author={Massey, Aaron K. and Rutledge, Richard L. and Ant{\'o}n, Annie I. and Swire, Peter P.},
11	  booktitle={22nd IEEE International Requirements Engineering Conference (RE)},
12	  year={2014},
13	  doi={10.1109/RE.2014.6912250}
14	}
15	
16	@techreport{berry_kamsties_2004,
17	  title={From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook},
18	  author={Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.},
19	  institution={University of Waterloo},
20	  year={2004}
21	}
22	
23	@inproceedings{chantree_2006,
24	  title={Identifying Nocuous Ambiguities in Natural Language Requirements},
25	  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},
26	  booktitle={14th IEEE International Requirements Engineering Conference (RE)},
27	  year={2006}
28	}
29	
30	@incollection{wasow_ambiguity_2005,
31	  title={The Puzzle of Ambiguity},
32	  author={Wasow, Thomas and Perfors, Amy and Beaver, David},
33	  booktitle={Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe},
34	  publisher={CSLI Publications},
35	  year={2005}
36	}
37	
38	@article{kennedy_vagueness_2007,
39	  title={Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives},
40	  author={Kennedy, Christopher},
41	  journal={Linguistics and Philosophy},
42	  volume={30},
43	  number={1},
44	  pages={1--45},
45	  year={2007},
46	  doi={10.1007/s10988-006-9008-0}
47	}
48	
49	@article{willis_nocuous_2008,
50	  title={Automatic Identification of Nocuous Ambiguity},
51	  author={Willis, Alistair and Chantree, Francis and De Roeck
…[truncated 17740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2269 · 2026-05-23T11:41:30.537137+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2270 · 2026-05-23T11:41:32.344551+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/decisions.yaml\", \"content\": \"_next_id: 28\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:11 UTC\\n  summary: MVP 设计：3 类歧义 × 2 API 模型验证 type effect，不用 GPU\\n  rationale: 核心假设是\\\"歧义类型影响安全违规率\\\"。选 scopal/lexical/incompleteness 3 种假设差异最大的类型，用 frontier\\n    API 模型（免 GPU）快速验证信号存在性。60 条款 × 2 variants × 2 模型 = 240 runs，统计功效足够（χ² df=2, medium\\n    effect w=0.3, N=240 >> 所需 ~107）。Pass 条件：p<0.05 + V≥0.15。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:15 UTC\\n  summary: 采纳 Reviewer 3 条修正：增条款数、调阈值、补 fail path\\n  rationale: 'Reviewer WARNING: (1) pairwise N=80 对 V=0.15 功效仅 0.22，增至 30 条款/类（pairwise\\n    N=120）+ 提阈值至 V≥0.20 + 明确 MVP 只检测 medium+ effect；(2) 补 fail path 三级决策树（扩大N重测 →\\n    pivot binary story → full study）；(3) 加 judge 偏差检查点（scopal 低于预期时先排查 judge bias）。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:16 UTC\\n  summary: ROADMAP 补充 H1-H4 预测基准和 post-MVP 18 周路径骨架\\n  rationale: 'Reviewer WARNING: (1) ROADMAP 缺 post-MVP 骨架，ICLR DDL 18 周后，需提前规划 GPU\\n    申请时间点（W3 MVP pass 后立即申请，W5 开始 Phase 2b）；(2) H1-H4 方向性预测未落地到 ROADMAP，Agent 解读 MVP\\n    结果时需对照基准（H1: scopal 最高，H2: lexical 最低，null: binary effect story）。paper_framing.md\\n    保持在 MVP 后创建。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-20 07:23 UTC\\n  summary: MVP 分析改为双轨：ambiguous-only 跨类型比较（主）+ matched-pair within-type（辅）\\n  rationale: 'Reviewer WARNING: incompleteness matched pair 存在信息量不对称混淆——消歧必然添加信息，与\\n    scopal/lexical 的\\\"同信息不同措辞\\\"baseline 不可比。解法：(1) 主分析用 ambiguous-only 条件直接跨类型比较违规率（不受信息量混淆）；(2)\\n    matched-pair 降为辅助的 within-type 效应量度量；(3) 要求 Agent 修订 incompleteness pairs 只添加解决歧义的最小信息；(4)\\n    效度边界显式声明此不对称性。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-20 07:24 UTC\\n  summary: MVP 使用 τ²-
…[truncated 1453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1807
}
```

</details>

---


### Tool call

_source line 2271 · 2026-05-23T11:41:32.445326+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null | head -60",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null | head -60",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2272 · 2026-05-23T11:41:32.647793+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 2273 · 2026-05-23T11:41:39.374745+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2274 · 2026-05-23T11:41:39.826778+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2275 · 2026-05-23T11:41:39.977715+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 2276 · 2026-05-23T11:41:43.746451+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3768
}
```

</details>

---


### Tool call

_source line 2277 · 2026-05-23T11:41:47.967140+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/policy_ambiguity_safety/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/policy_ambiguity_safety/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
  }
}
```

</details>

---


### Tool result

_source line 2278 · 2026-05-23T11:41:48.067980+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/configs/config.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2279 · 2026-05-23T11:41:51.131353+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -5",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2280 · 2026-05-23T11:41:52.287974+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 1156
}
```

</details>

---


### Tool call

_source line 2281 · 2026-05-23T11:42:30.212304+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "你是 Reviewer 1，负责审查本文的**方法严谨性**。\n\n## 论文信息\n- 标题: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n- 路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_26/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** via ARR May cycle (deadline: 2026-05-25)\n- Long paper: 8 页正文上限，references 不限\n- Limitations section 必须有（不计入页数限制），不能过长（~3 个点一小段）\n- ACL 模板 (acl.sty)，double-blind 匿名审稿\n- Overall Assessment 评分标准: 5=Consider for Award（~前2.5%），4.5=Borderline Award，4=Conference（主会议接收），3.5=Borderline Conference，3=Findings，2.5=Borderline Findings，2=Resubmit next cycle，1.5=Resubmit after next cycle，1=Do not resubmit\n\n## 你的审查侧重\n\n**方法严谨性**，重点关注：\n\n1. **因果设计有效性**：matched-pair 设计是否支撑因果推断？内部效度威胁是否被充分控制？\n2. **Confound 处理**：incompleteness 的 information-addition confound 控制是否充分？token count 作为 proxy 是否可信？\n3. **统计分析**：TOST equivalence testing 的 SESOI ±15pp 选择是否合理？多重比较校正是否正确？variance decomposition 的 Type III SS 使用是否恰当？\n4. **评估管道**：cross-judge 设计的偏差控制（GPT-5.4 judges Claude/GPT-4.1/Qwen3，GPT-4.1 judges GPT-5.4/DeepSeek）——这个不对称分配是否引入系统性偏差？human validation 的样本量（n=100）是否充分？\n5. **生态效度**：合成歧义 vs 自然歧义的效应差距（34pp vs 12.7pp）——论文对此差距的解释是否充分？temperature=0 的限制讨论是否到位？\n6. **可复现性**：ICC=0.919 仅基于 OpenAI family——跨 provider 可复现性证据是否充分？\n7. **Authorization scope 异常**：κ=0.385、52pp 跨模型变异——论文是否充分处理了这个 construct outlier？\n\n请提供结构化审稿报告：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Overall Assessment（用 EMNLP 2026 评分标准）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "你是 Reviewer 1，负责审查本文的**方法严谨性**。\n\n## 论文信息\n- 标题: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n- 路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_26/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** via ARR May cycle (deadline: 2026-05-25)\n- Long paper: 8 页正文上限，references 不限\n- Limitations section 必须有（不计入页数限制），不能过长（~3 个点一小段）\n- ACL 模板 (acl.sty)，double-blind 匿名审稿\n- Overall Assessment 评分标准: 5=Consider for Award（~前2.5%），4.5=Borderline Award，4=Conference（主会议接收），3.5=Borderline Conference，3=Findings，2.5=Borderline Findings，2=Resubmit next cycle，1.5=Resubmit after next cycle，1=Do not resubmit\n\n## 你的审查侧重\n\n**方法严谨性**，重点关注：\n\n1. **因果设计有效性**：matched-pair 设计是否支撑因果推断？内部效度威胁是否被充分控制？\n2. **Confound 处理**：incompleteness 的 information-addition confound 控制是否充分？token count 作为 proxy 是否可信？\n3. **统计分析**：TOST equivalence testing 的 SESOI ±15pp 选择是否合理？多重比较校正是否正确？variance decomposition 的 Type III SS 使用是否恰当？\n4. **评估管道**：cross-judge 设计的偏差控制（GPT-5.4 judges Claude/GPT-4.1/Qwen3，GPT-4.1 judges GPT-5.4/DeepSeek）——这个不对称分配是否引入系统性偏差？human validation 的样本量（n=100）是否充分？\n5. **生态效度**：合成歧义 vs 自然歧义的效应差距（34pp vs 12.7pp）——论文对此差距的解释是否充分？temperature=0 的限制讨论是否到位？\n6. **可复现性**：ICC=0.919 仅基于 OpenAI family——跨 provider 可复现性证据是否充分？\n7. **Authorization scope 异常**：κ=0.385、52pp 跨模型变异——论文是否充分处理了这个 construct outlier？\n\n请提供结构化审稿报告：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Overall Assessment（用 EMNLP 2026 评分标准）。"
  }
}
```

</details>

---


### Tool result

_source line 2282 · 2026-05-23T11:42:46.238694+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16026
}
```

</details>

---


### Tool call

_source line 2283 · 2026-05-23T11:42:46.390364+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "你是 Reviewer 2，负责审查本文的**新颖性与完整性**。\n\n## 论文信息\n- 标题: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n- 路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_26/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** via ARR May cycle (deadline: 2026-05-25)\n- Long paper: 8 页正文上限，references 不限\n- Limitations section 必须有（不计入页数限制），不能过长（~3 个点一小段）\n- ACL 模板 (acl.sty)，double-blind 匿名审稿\n- Overall Assessment 评分标准: 5=Consider for Award（~前2.5%），4.5=Borderline Award，4=Conference（主会议接收），3.5=Borderline Conference，3=Findings，2.5=Borderline Findings，2=Resubmit next cycle，1.5=Resubmit after next cycle，1=Do not resubmit\n\n## 你的审查侧重\n\n**新颖性与完整性**，重点关注：\n\n1. **Contributions 定位**：三个贡献（因果研究 + type-mechanism dissociation + disambiguation neglect/systematic nocuity）的新颖性——相对于 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等并发工作，增量贡献是否足够？\n2. **Taxonomy 增量论证**：从 Li et al. (2024) 11→6 的选择是否论证充分？specification layer 3 个新类型的 RE 文献支撑是否足够？taxonomy 被定位为\"diagnostic instrument\"而非\"risk classifier\"——这是否削弱了贡献？\n3. **Related Work 覆盖**：是否遗漏重要相关工作？特别是 agent safety、policy specification、ambiguity processing 三个方向\n4. **术语选择**：'ambiguity' 广义使用与 NLP 社区标准定义的张力；'nocuous' 从 divergent→convergent 的概念延伸是否恰当\n5. **写作质量**：\n   - Abstract 信息密度是否过高？\n   - 正文数字密度（Results/Analysis）是否影响可读性？\n   - 论文叙事弧（从 Introduction 的 motivating example 到 Conclusion 的 actionable message）是否连贯？\n6. **格式合规**：8 页正文限制、匿名性、Limitations section 格式\n7. **跨领域泛化性**：仅 2 个 customer-service domains——Abstract/Conclusion 的泛化性声明是否过强？ρ=0.26 的跨领域 type ranking 不一致是否被充分讨论？\n\n请提供结构化审稿报告：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → Overall Assessment（用 EMNLP 2026 评分标准）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "你是 Reviewer 2，负责审查本文的**新颖性与完整性**。\n\n## 论文信息\n- 标题: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n- 路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_26/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** via ARR May cycle (deadline: 2026-05-25)\n- Long paper: 8 页正文上限，references 不限\n- Limitations section 必须有（不计入页数限制），不能过长（~3 个点一小段）\n- ACL 模板 (acl.sty)，double-blind 匿名审稿\n- Overall Assessment 评分标准: 5=Consider for Award（~前2.5%），4.5=Borderline Award，4=Conference（主会议接收），3.5=Borderline Conference，3=Findings，2.5=Borderline Findings，2=Resubmit next cycle，1.5=Resubmit after next cycle，1=Do not resubmit\n\n## 你的审查侧重\n\n**新颖性与完整性**，重点关注：\n\n1. **Contributions 定位**：三个贡献（因果研究 + type-mechanism dissociation + disambiguation neglect/systematic nocuity）的新颖性——相对于 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等并发工作，增量贡献是否足够？\n2. **Taxonomy 增量论证**：从 Li et al. (2024) 11→6 的选择是否论证充分？specification layer 3 个新类型的 RE 文献支撑是否足够？taxonomy 被定位为\"diagnostic instrument\"而非\"risk classifier\"——这是否削弱了贡献？\n3. **Related Work 覆盖**：是否遗漏重要相关工作？特别是 agent safety、policy specification、ambiguity processing 三个方向\n4. **术语选择**：'ambiguity' 广义使用与 NLP 社区标准定义的张力；'nocuous' 从 divergent→convergent 的概念延伸是否恰当\n5. **写作质量**：\n   - Abstract 信息密度是否过高？\n   - 正文数字密度（Results/Analysis）是否影响可读性？\n   - 论文叙事弧（从 Introduction 的 motivating example 到 Conclusion 的 actionable message）是否连贯？\n6. **格式合规**：8 页正文限制、匿名性、Limitations section 格式\n7. **跨领域泛化性**：仅 2 个 customer-service domains——Abstract/Conclusion 的泛化性声明是否过强？ρ=0.26 的跨领域 type ranking 不一致是否被充分讨论？\n\n请提供结构化审稿报告：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → Overall Assessment（用 EMNLP 2026 评分标准）。"
  }
}
```

</details>

---


### Tool result

_source line 2284 · 2026-05-23T11:42:47.854199+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1463
}
```

</details>

---


### Assistant

_source line 2285 · 2026-05-23T11:42:57.138092+00:00_

两位 Reviewer 已分配，视觉审查已并行派发。等待 Reviewer 提交初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 216

## Round 216

2 recorded events


### User

_source line 2286 · 2026-05-23T11:49:59.859585+00:00_

[Reviewer 1 审稿意见]:
## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 一项设计扎实的 matched-pair 因果研究，证明了政策歧义增加 LLM agent 安全违规，但 SESOI 偏大、incompleteness confound 控制不充分、跨 provider 可复现性证据不足，削弱了部分核心 claims 的说服力。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | Matched-pair 因果设计本身可靠；但 SESOI ±15pp 对安全领域偏大；incompleteness confound 仅用 token count proxy 部分控制；ICC 仅来自 OpenAI family |
| Excitement | 3/5 | 研究问题及时且重要；但 "歧义→更多违规" 这个主发现符合预期；type-mechanism dissociation 有意思但部分类型 construct validity 存疑 |
| Reproducibility | 3/5 | 代码/数据承诺发布；附录详尽；但 ICC 仅来自单一 provider family；temperature=0 限制了泛化性 |
| Confidence | 4/5 | 仔细阅读全文及附录，熟悉因果推断和 NLP 安全评估方法 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] SESOI ±15pp 对安全研究领域缺乏充分论证

- 具体位置：Section 4.6, Table 3
- 问题：论文选择 ±15pp 作为 TOST 等价性检验的最小有意义效应量（SESOI），理由是"超过测量噪声 2 倍以上"以及"低于此幅度的差异不足以支持差异化缓解策略"。然而对于安全研究，14.9pp 的额外违规率在规模化部署中可能意味着数百次不安全行为。Table 3 的敏感性分析显示：在 ±10pp 时，仅 3/7 个 margin 在所有类型上达到等价性。SESOI 应锚定在领域特定的风险框架（如每次违规的预期危害 × 部署规模），而非噪声的经验倍数。
- 为什么影响接收：Type-mechanism dissociation claim (C2) —— 类型在机制上不同但违规率等价 —— 完全依赖 TOST 等价性。更小的、有原则论证的 SESOI 可能推翻部分类型对的等价结论。
- 建议修改方向：提供基于安全领域的原则性 ±15pp 论证；或以 ±10pp 为主分析、±15pp 为敏感性分析，并相应限定 dissociation claim 的适用范围。

**N2** [critical] Incompleteness 的 information-addition confound 控制不充分

- 具体位置：Section 4.5, Appendix F
- 问题：论文正确识别了 incompleteness 的结构性差异：其 unambiguous variant 添加了原本缺失的信息，而非仅消歧。唯一的控制手段是 token count logistic regression (Appendix F)，得到"confound-free lower bound" 18.7pp。但 token count 作为信息内容的 proxy 存在根本缺陷：一个短语如"non-refundable"可能以极少 token 携带高政策信息量，而冗长的澄清文本可能增加最小语义内容。回归假设 confound 通过 token count 线性作用，但实际 confound 是关于所添加信息的*类型*（政策相关内容 vs. 消歧），而非*数量*。
- 为什么影响接收：Incompleteness 是最高风险类型（46-62%），驱动多个核心 claims。其 49.2pp 效应的真实程度取决于 confound-free bound 的可靠性，而该 bound 完全依赖这个有缺陷的 proxy。
- 建议修改方向：(a) 增加控制条件——添加等量但不解决 incompleteness 的政策文本（如不相关主题的等长政策信息），直接隔离消歧效应与信息添加效应；或 (b) 将 incompleteness 从主要因果 claims 中排除，作为观察性证据处理，以 confound-free 的 31.0pp 作为首要效应量报告。

**N3** [critical] ICC(1) = 0.919 仅限 OpenAI family，跨 provider 可复现性证据不足

- 具体位置：Appendix AC, Section 4.4
- 问题：ICC(1) = 0.919 仅基于 GPT-5.4 和 GPT-4.1 的复制实验计算，两者共享 OpenAI 训练流水线。Appendix E 在 Gemini 2.5-Flash 和 LLAMA-4-Scout 上的复制显示方向一致性（OR 在原始五模型范围内），但未计算 ICC。论文声称"cross-model consistency"作为核心发现，但可复现性证据的覆盖面不匹配这一声明。
- 为什么影响接收：不同 provider 的模型可能有质性不同的安全训练，单一 family 内的 ICC 无法捕获这一维度的变异。
- 建议修改方向：在全部七个模型（五个主实验 + 两个复制）上计算 ICC 或等效可复现性指标；或将可复现性声明明确限定为 within-family consistency。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Authorization scope (κ=0.385, 52pp 跨模型变异) 是 construct validity 异常值

- 具体位置：Table 10, Appendix O/P/R
- 问题：Authorization scope 的 inter-judge agreement 最低（κ=0.385 vs. 其他类型 ≥0.636），跨 judge 方差最大（41.6-65.6%），且驱动 C4 model×type interaction。论文用三个附录分析此异常但仍将其纳入 headline statistics 和六类型 taxonomy。
- 建议：将主 taxonomy 呈现为五类型，authorization scope 作为独立的低置信度 construct。单独报告五类型 ICC。

**W2** [warning] 合成歧义到自然歧义的效应差距（34pp vs 12.7pp）需要在正文讨论

- 具体位置：Appendix AA/Z, Abstract
- 问题：SOPBench 复制显示 +12.7pp，是 τ²-bench 发现的 2.7 倍缩小。Appendix Z 给出三个合理解释（测量粒度、基线率、任务结构），但此差距直接影响实际解读，应在正文 Section 7 或 8 中讨论，而非完全推迟到附录。

**W3** [warning] Temperature=0 限制了 variance decomposition 的解读

- 具体位置：Section 4.3, Appendix AC
- 问题：所有实验使用 temperature=0，使每个 episode 对给定模型是确定性的。Variance decomposition（Type III SS, ICC）因此仅捕获跨模型和跨 clause 的变异，不包含随机生成方差。实际部署的 LLM agent 通常使用 temperature>0，within-model 方差可能显著改变效应量分布。
- 建议：在 variance decomposition 部分明确说明此限制，讨论对部署场景的影响。

**W4** [warning] Human validation 样本量（n=100）导致 per-type 置信区间较宽

- 具体位置：Table 10, Appendix AE
- 问题：Per-type 样本量 32-34，部分类型 CI 宽达 ±20pp。Authorization scope 的 agreement（κ=0.385）基于 n=34，对一个已知困难的 construct 来说样本量不足以可靠估计 agreement。这对整体 pipeline 验证足够，但不足以支持类型级别的可靠性声明。

## 小问题（不影响接收）

- "Confound-free"一词在论文中有两种用法：Abstract 中的"confound-free types"指排除 incompleteness 的五种类型（31.0pp），而 Limitations 中的"+34.0pp confound-free"似指经过 perturbation controls 后的整体效应。这种术语不一致应消除。
- 标题中的"nocuous"是一个古体/罕用英文词，可能降低非母语读者的可及性；可考虑"harmful"或"detrimental"。
- Table 2 脚注标记（†, ‡）较小，容易遗漏。

## Questions for Authors

Q1: 能否提供基于安全领域的原则性论证来支撑 ±15pp SESOI？安全工程师会认为多大的违规率差异是实际可忽略的？

Q2: 是否考虑过为 incompleteness 增设控制条件——添加等量信息但不解决歧义（如添加等长的不相关政策文本）——以直接隔离消歧效应与信息添加效应？

Q3: 在全部七个模型上计算 ICC 时结果如何？如果跨 provider ICC 显著低于 0.919，这对泛化性声明有重要影响。

Q4: 对于 authorization scope（κ=0.385），在什么阈值下低 agreement 会导致将该类型从 taxonomy 中排除，而非将其视为"困难 construct"？

## 主要优势

1. **因果框架设计扎实**：Matched-pair 设计配合 perturbation controls (Section 4.5) 清晰隔离了歧义效应。6.67pp 的 perturbation control upper bound 令人信服地排除了通用政策改写的替代解释。

2. **Confound 处理诚实**：论文未隐藏 incompleteness 的 information-addition 问题，而是用整个 Appendix F 量化它，并分别报告 confound-free 效应（31.0pp）和整体效应（34.0pp）。

3. **全面的敏感性分析**：跨七个 margin 的 TOST (Table 3)、bootstrap cluster analysis (Appendix I)、跨 benchmark 复制（SOPBench）、跨架构复制（Gemini, LLAMA）、within-family ICC 提供了丰富的证据图景。

4. **实际相关性**：Real-world prevalence audit (Appendix AD, 24 个生产文档中 58-87% 的条款含歧义) 建立了所研究现象的实际基础，而非仅为学术性构造。

5. **Type-mechanism dissociation**：歧义类型预测失败机制（Cramér's V = 0.45）但不预测违规率（V = 0.14）这一发现，对 intervention design 有切实价值，将 taxonomy 从风险分类器重新定位为诊断工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2287 · 2026-05-23T11:50:07.830531+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 217

## Round 217

6 recorded events


### User

_source line 2288 · 2026-05-23T11:50:10.392832+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（新颖性与完整性）

**论文**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
**Venue**: EMNLP 2026 via ACL ARR May cycle

---

## 总体评分

**Overall Assessment**: 3.5 / 5（Borderline Conference）

**一句话总结**: 方法论上是严谨的因果研究（matched-pair design），但核心贡献的新颖性受限于同期工作（DRIP-R），type-mechanism dissociation 依赖可靠性存疑的 LLM 编码标签，且仅覆盖 2 个 customer-service 领域限制了泛化性声明的说服力。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | Matched-pair 因果设计扎实，统计方法恰当（TOST 等价性、Holm-Bonferroni 校正、ICC 方差分解）。但 Contribution 2（type-mechanism dissociation）的核心证据——failure mechanism 分类——依赖 LLM 编码标签，人工标注 κ=0.15（Appendix AE），可靠性不足以支撑该发现的置信度。Incompleteness confound 处理透明但移除了 1/3 类型。 |
| **Excitement** | 3.5/5 | 研究问题及时且实践相关——policy ambiguity 对 agent safety 的因果效应是社区需要的证据。但高层发现（"ambiguity hurts agents"）在直觉上不令人意外，且 DRIP-R (2026) 已建立了类似的相关性证据。Type-mechanism dissociation 是有趣的发现但可靠性存疑。 |
| **Reproducibility** | 4/5 | 方法描述详细，承诺公开数据和代码。τ²-bench 是公开平台。Appendix 提供了充分的实验细节（prompt 模板、annotation 指南、统计检验细节）。唯一担忧是 LLM API 调用的不可精确复现性。 |

---

## Paper Summary

本文通过 matched-pair 因果设计研究 natural-language policy specification 中的歧义如何影响 LLM agent 安全性。作者在 τ²-bench 上构造了 300 对最小差异 clause pairs（覆盖 6 种歧义类型、两层分类），在 5 个模型上评估了 2,997 个 episodes。主要发现：(1) 歧义 clauses 使违规率增加 ~34pp（confound-free types 为 31pp）；(2) 歧义类型预测失败机制（Cramér's V=0.45）远强于预测违规率（V=0.14）——即 type-mechanism dissociation；(3) agents 展现 disambiguation neglect（仅 14.6% 感知到歧义）和 systematic nocuity（收敛于相同错误解释，77% permissive bias）。

---

## 主要优势（Strengths）

**S1. 因果设计的方法论严谨性。** Matched-pair 因果设计在 agent safety 文献中罕见。与 DRIP-R 的相关性研究不同，本文通过控制 clause wording 的最小差异来隔离歧义的因果效应。配对设计排除了 policy context、scenario 和 model 等混淆因素。统计处理全面：TOST 等价性检验（Appendix A）、Holm-Bonferroni 多重比较校正（Appendix K）、ICC 方差分解（Appendix AC，ICC(1)=0.749）、confound 分析（Appendix F）。这在当前以 benchmark 排行榜为主的 agent safety 研究中是值得肯定的方法论贡献。

**S2. Type-mechanism dissociation 是一个有洞察力的发现。** 歧义类型不预测违规严重程度（仅解释 0.4% 方差），却预测失败机制（V=0.45），这一分离现象对实践有重要启示：它意味着 policy 审计应关注 clause-level wording 而非 type-level risk classification。即使这一发现的绝对数值可能受 LLM 编码标签的影响（见 N2），方向性结论（type 更预测 mechanism 而非 severity）是有说服力的。

**S3. 系统性的控制和验证。** 论文对潜在弱点有较好的预见和处理：
- Incompleteness 的 information-addition confound 被明确标识并在报告中分离（§5.1, Appendix F）
- 跨基准复制（SOPBench, Appendix AA）确认方向一致性
- 真实世界 policy 文档的 prevalence audit（Appendix AD：24 文档、407 clauses、55-87% 含歧义）提供生态效度
- Within-family LOO 分析（Appendix J）确认 family-level 可复制性
- 双评注员独立验证 300 对 clause pairs（96% 初始一致率，Appendix T 细节）

**S4. Appendix 的深度和透明度。** 15 页 appendix（A-AE）覆盖了几乎所有可预见的 reviewer 问题：从 TOST 等价性到方差分解、从 cross-judge 一致性到 taxonomy mapping、从 real-world prevalence 到 SOPBench 复制。这种透明度对评审友好度很高。

**S5. 实践可操作性。** 论文的结论直接可操作：clause-level policy auditing > type-level risk classification。这对 agent 部署者和 policy 设计者有即时价值。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Type-mechanism dissociation（Contribution 2）的核心证据可靠性不足**
- 具体位置：§6.1 (p7), Appendix AE (p22)
- 问题：Type-mechanism dissociation 是三大贡献之一，也是将 taxonomy 从 "risk classifier" 重新定位为 "diagnostic instrument" 的核心论据。然而，failure mechanism 分类完全依赖 LLM 编码标签，而人工标注一致性极低（κ = 0.15，Appendix AE）。论文承认 "absolute NMI should be interpreted as an upper bound on the true type-mechanism association"（§6.1），但仍将其作为主要贡献和 abstract 的核心数字（V = 0.45 vs. 0.14）呈现。
- 为什么影响接收：如果人工标注者无法在 failure mechanism 分类上达成一致（κ = 0.15 接近随机），这说明 mechanism 类别的边界本身是模糊的。LLM 编码标签的高一致性可能反映的是 LLM 的系统性分类偏好而非真实的 type-mechanism 关联。这使 Contribution 2 的置信度大打折扣。
- 建议修改方向：(1) 在正文（不仅是 appendix）显著讨论 κ = 0.15 对这一发现的影响；(2) 考虑将 type-mechanism dissociation 从 "contribution" 降级为 "exploratory finding"；(3) 分析 LLM 编码标签的具体分类模式——是否某些 mechanism 类别被系统性地过度/不足分配？(4) 在 abstract 中对 V = 0.45 数字添加适当的 caveat。

**N2** [critical] **"Nocuous" 术语的语义反转未充分论证**
- 具体位置：§6.3 (p7), Title
- 问题：Berry et al. (2004) 定义 "nocuous ambiguity" 为导致**不同**读者产生**不同**解释的歧义（divergent interpretation）。本文发现的现象恰好相反——agents **收敛于同一错误解释**（convergent error, 41.9% majority-convergent）。论文在 §6.3 承认 "but inverted"，然而标题 "Policy Ambiguity Is Nocuous" 直接使用了这个术语，没有任何限定词。对于熟悉 RE 文献的读者，这会造成概念混淆：原始的 nocuous = dangerous *because of divergence*；本文的 nocuous = dangerous *because of convergence*。这不是同一种 "nocuous"。
- 为什么影响接收：术语选择影响论文的定位和可引用性。如果 "nocuous" 在本文中的含义与其原始定义相反，读者可能误解论文的核心发现。标题作为论文最高频被引用的部分，不应含有语义反转的术语。
- 建议修改方向：(1) 在标题中使用更精确的术语（如 "systematically harmful" 或 "convergently harmful"）；或 (2) 在 Introduction 中更充分地论证为什么这种语义延伸是恰当的，而不仅是在 §6.3 简短提及；(3) 至少在 §6.3 将 "systematic nocuity" 重命名为更不易混淆的术语。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **'Ambiguity' 的广义使用与 NLP 社区标准定义的张力**
- 具体位置：§3 "Scope of 'ambiguity'" (p4)
- 问题：NLP 社区对 ambiguity 有明确定义——一个表达在给定上下文中有多个可能的语言学解释。本文将其扩展到包含 incompleteness（信息缺失）、authorization scope（vagueness）、conditional precedence（normative conflict）。§3 的 "Scope of 'ambiguity'" 段落承认了这一点，但论证停留在功能等价层面（"yet both force an agent to select among operationally distinct behaviors"）。这是一个合理的 operationalization，但对于 CL/NLP venue 的读者，可能显得在 conflating 不同的 linguistic phenomena。
- 建议：在 §3 增加一段更系统的论证——(1) 引用 NLP 中对 underspecification 和 ambiguity 的区分文献（如 Poesio & Artstein, 2005），(2) 明确说明为什么对于 agent safety 的研究目的，这种合并是有信息量的而非混淆的，(3) 考虑使用 "policy underspecification" 作为上位术语，"ambiguity" 作为子类型。

**W2** [warning] **跨领域泛化性：ρ = 0.26 的 type ranking 不一致削弱 taxonomy 的诊断价值**
- 具体位置：Appendix Z (p19), Limitations (p9), Title
- 问题：Appendix Z 报告 per-type violation-rate rankings 在 retail vs. airline 两个 domain 之间的 Spearman ρ = 0.26 (p = 0.62)——本质上是零相关。这意味着哪种歧义类型最危险高度依赖领域。然而论文标题 "Policy Ambiguity Is Nocuous" 不含任何领域限定，Conclusion (§8) 虽然将定量结论限定为 "in customer-service domains"，但 Contributions (§1) 和 Abstract 的表述暗示了更广泛的适用性。
- 建议：(1) 在正文 §5.2 或 §7 中报告 ρ = 0.26 这一关键数字（目前仅在 appendix Z 中），因为它直接影响 taxonomy-as-diagnostic-instrument 的可推广性；(2) Conclusion 中明确指出 "type-level diagnostic findings are domain-contingent"。

**W3** [warning] **相对于 DRIP-R (2026) 的增量贡献论证不够有力**
- 具体位置：§2 (p3)
- 问题：DRIP-R 是最接近的并发工作，同样研究 policy ambiguity 对 LLM agents 的影响。论文在 §2 列出了三点差异：(1) matched-pair causal design vs correlational, (2) safety violations vs decision quality, (3) two-layer taxonomy。但论文没有系统性地论证为什么这些差异构成 *sufficient* incremental contribution 而非 *complementary refinement*。特别是：DRIP-R 已经在 400 scenarios × 5 RE ambiguity types 上建立了 "ambiguity hurts agents" 的基本事实——本文的方法论改进（causal design）是否改变了 DRIP-R 的结论？如果只是提供了更严格的确认，contribution bar 更高。
- 建议：在 §2 或 §7 增加一段直接对比：(1) DRIP-R 的 correlational evidence 留下了哪些具体的 confound 没有排除？(2) 本文的 causal design 具体回答了哪些 DRIP-R 无法回答的问题？(3) 两项工作的效应量是否可比？

**W4** [warning] **Taxonomy 从 11→6 的选择标准论证不够系统**
- 具体位置：§3 (p3-4), Appendix M (Table 12, p16)
- 问题：从 Li et al. (2024b) 的 11 类型中选择 6 个，排除标准为 (1) RE attestation, (2) minimal-pair constructibility, (3) mutual exclusivity。Table 12 (Appendix M) 提供了映射，但排除决策的论证不够系统。例如：Ellipsis 和 Pragmatic Implicature 被排除（"not attested in RE literature, criterion 1"），但 ellipsis 在 policy texts 中明显存在（如 "Items returned in 30 days [will receive a full refund]"），排除的真正原因可能是 minimal-pair 构造困难而非 RE 文献缺失。将 constructibility constraint 伪装为 RE-attestation criterion 削弱了论证的可信度。
- 建议：在 §3 或 Appendix M 中更坦诚地说明哪些类型是因为 minimal-pair 构造的实际困难而排除的（这是完全合理的实践限制），而不是将所有排除都归因于概念标准。

**W5** [warning] **Abstract 信息密度过高**
- 具体位置：Abstract (p1)
- 问题：Abstract 在约 190 词内塞入了至少 8 个定量数字（31.0pp, 34.0pp, +12.7pp, 0.4%, 22.4%, V=0.45 vs. 0.14, 14.6%, 77%）以及多个方法论细节（300 clause pairs, six-type taxonomy, five models, 2,997 episodes）。虽然未超 200 词限制，但信息密度使得非专家读者难以在首次阅读时抓住核心贡献。特别是 V=0.45 vs. 0.14 这对数字在没有 context 的情况下对不熟悉 Cramér's V 的读者无意义。
- 建议：精简 abstract 中的数字，保留最核心的 2-3 个（如 overall effect size 和 type-mechanism dissociation 的定性描述），将其余移至 §5/§6。

---

## 小问题（不影响接收）

**M1.** §1 (p1) 的 motivating example（"items may be returned within 30 days"）虽然直观，但歧义来源过于明显。考虑增加一个更 subtle 的例子（如 authorization scope 或 conditional precedence 类型）来展示 taxonomy 的诊断价值。

**M2.** Table 2 (p7) 和 Table 3 (Appendix A) 的数字密度极高。建议在 §5.1 用 prose 突出 1-2 个最关键的发现，将完整数字表格移至 appendix，正文仅保留摘要性图表（Figure 2 已经做得不错）。

**M3.** "Confound-free types" 这一术语在 §5.1 首次出现时应更清楚地定义——读者需要翻到 Appendix F 才能理解为什么 incompleteness 和 scopal 被排除。建议在正文中用 1-2 句解释。

**M4.** Appendix E（Replication on Additional Model Families, p12-13）的 Gemini-2.5-Flash 和 LLaMA-4-Scout 结果增强了泛化性，但仅作为 appendix 处理。如果页面允许，将关键复制结果纳入正文 §5 会增强说服力。

**M5.** §4.4 (p5) 提到 "Cross-judge calibration" 使用 dual-judge pipeline on 100 stratified episodes，κ = 0.653。但这是 violation severity 的 κ，与 failure mechanism 的 κ = 0.15（Appendix AE）形成鲜明对比。这种差异本身是一个值得在正文讨论的发现。

---

## Questions for Authors

**Q1.** Type-mechanism dissociation 的 Cramér's V = 0.45 是基于 LLM 编码的 failure mechanism 标签计算的。如果使用人工标注标签（尽管 κ = 0.15），V 值会是多少？即使人工标注一致性低，至少应报告基于人工标注的 V 值作为对比。

**Q2.** "Disambiguation neglect" (§6.2) 的 14.6% awareness rate 是仅在 ambiguous conditions 下测量的。在 unambiguous conditions 下，agents 是否也表现出类似比例的 "false positive" 歧义感知？如果 agents 在 unambiguous 条件下也很少讨论潜在歧义，那么 14.6% 可能只是反映了 agents 一般性的低元认知能力，而非特定于歧义的 "neglect"。

**Q3.** Per-type violation-rate rankings 在 retail vs. airline 之间的 ρ = 0.26 是否在其他 domain pairs 中也观察到类似的不一致？SOPBench 复制中是否有 per-type 的跨领域数据？

**Q4.** 论文在 §4.5 中提到 perturbation control（300 episodes with non-ambiguity perturbations）的效应为 Δ_baseline = 0.67pp。但这些 perturbation 的具体类型是什么？是否可能某些 "non-ambiguity perturbations" 实际上引入了微妙的歧义？

---

## Missing References

1. **Poesio & Artstein (2005)** — "Annotating (Anaphoric) Ambiguity" 和相关的 NLP ambiguity annotation 工作。论文讨论 'ambiguity' 的广义使用时，应引用 NLP 社区关于 ambiguity vs. underspecification vs. vagueness 的经典区分。

2. **Instruction-following evaluation** — 如 Zhou et al. (2023) "Instruction-Following Evaluation for Large Language Models" (IFEval)。虽然本文关注的是 policy compliance 而非一般性的 instruction following，但 IFEval 系列工作建立了 LLM 在 rule-following 方面的基线表现，与本文的 findings 有对话关系。

3. **Constitutional AI / rule-following 文献** — Bai et al. (2022) "Constitutional AI" 和后续工作。当讨论 "permissive bias"（77%，§6.3）时，这些工作提供了关于 LLM 在 safety rules 和 permissiveness 之间权衡的重要背景。

4. **Pragmatic inference in LLMs** — Hu et al. (2023) 或 Ruis et al. (2023) 等关于 LLM 在 pragmatic inference 方面能力的近期工作。论文在 §2 (p2) 简要提到了 pragmatic 层面的相关工作，但可以更系统地连接到 "agents adopt shallow, good-enough representations"（Ferreira et al., 2002）的发现。

---

## 格式合规检查

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 正文页数 ≤ 8 | ✅ | §1-§8 在 pages 1-8 |
| Limitations section | ✅ | Page 9，约半页，覆盖 3 个点（合成数据上界、2 领域限制、LLM 标注依赖），符合要求 |
| 匿名性 | ✅ | "Anonymous ACL submission"，GitHub URL 使用 anonymous placeholder |
| ACL 模板 | ✅ | acl.sty 格式 |
| Abstract ≤ 200 words | ✅ | 约 185-195 词，在限制内（但极为密集） |
| References 格式 | ✅ | acl_natbib 格式，pages 9-10 |

---

## Overall Assessment 论证

**评分：3.5（Borderline Conference）**

这篇论文在一个重要且及时的研究问题上做出了方法论上严谨的贡献。Matched-pair causal design 在 agent safety 文献中是罕见的，统计处理全面而透明。研究执行（5 模型、2,997 episodes、15 页 appendix）展示了对 reproducibility 和 reviewer 预期问题的高度重视。

然而，从新颖性角度看，核心发现存在以下关切：
1. "Ambiguity hurts agents" 的主效应在 DRIP-R (2026) 之后不再令人惊讶——本文的增量贡献主要在方法论（causal → correlational）而非发现（what's new）；
2. Type-mechanism dissociation 作为第二贡献的可靠性受到人工标注一致性极低（κ=0.15）的严重挑战；
3. 仅 2 个 customer-service domains + ρ=0.26 的跨领域 type ranking 限制了 taxonomy 诊断价值的泛化性主张。

从完整性角度看，"nocuous" 的语义反转和 "ambiguity" 的广义使用构成术语层面的隐患，可能招致 NLP 和 RE 两个社区的审稿人批评。

如果作者能充分回应 N1（type-mechanism dissociation 可靠性）和 N2（术语选择），并加强与 DRIP-R 的差异化论证（W3），本文有望达到 Conference 接收水平。当前版本更适合 Findings。

**Confidence**: 4/5 — 仔细阅读了论文和 appendix，熟悉 agent safety、NLP ambiguity 和因果推断相关文献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2289 · 2026-05-23T11:50:55.619689+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性）\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] SESOI ±15pp 对安全研究领域缺乏充分论证\n- 论文选择 ±15pp 作为 TOST SESOI，理由是\"超过测量噪声 2 倍以上\"。对安全领域，14.9pp 额外违规率在规模化部署中意味数百次不安全行为。Table 3 的敏感性分析显示：在 ±10pp 时仅 3/7 达到等价性。Type-mechanism dissociation claim (C2) 完全依赖 TOST 等价性，更小的 SESOI 可能推翻部分类型对的等价结论。\n- 建议：提供基于安全领域的原则性论证；或以 ±10pp 为主分析。\n\n**N2** [critical] Incompleteness 的 information-addition confound 控制不充分\n- 唯一控制手段是 token count logistic regression。Token count 作为信息内容 proxy 存在根本缺陷：短语如\"non-refundable\"可能以极少 token 携带高政策信息量。回归假设 confound 通过 token count 线性作用，但实际 confound 是关于所添加信息的*类型*而非*数量*。\n- 建议：增加控制条件（添加等量但不解决 incompleteness 的政策文本）；或将 incompleteness 从主要因果 claims 中排除。\n\n**N3** [critical] ICC(1) = 0.919 仅限 OpenAI family，跨 provider 可复现性证据不足\n- ICC(1) = 0.919 仅基于 GPT-5.4 和 GPT-4.1。Appendix E 在 Gemini 和 LLAMA 上复制显示方向一致性但未计算 ICC。不同 provider 可能有质性不同的安全训练。\n- 建议：在全部七个模型上计算 ICC 或等效指标；或限定为 within-family consistency。\n\n### Should-Fix\n\n**W1** Authorization scope (κ=0.385, 52pp 跨模型变异) 是 construct validity 异常值。建议将主 taxonomy 呈现为五类型。\n\n**W2** 合成歧义到自然歧义效应差距（34pp vs 12.7pp）应在正文讨论，非仅 appendix。\n\n**W3** Temperature=0 限制了 variance decomposition 的解读。实际部署 temperature>0。\n\n**W4** Human validation 样本量（n=100）导致 per-type CI 较宽。Authorization scope 的 κ=0.385 基于 n=34。\n\n### Minor\n- \"Confound-free\"术语不一致\n- \"Nocuous\" 古体词可能降低可及性\n- Table 2 脚注标记较小\n\n### 优势\n1. 因果框架设计扎实（perturbation control 6.67pp upper bound）\n2. Confound 处理诚实（Appendix F）\n3. 全面的敏感性分析（7 个 margin TOST、bootstrap cluster、SOPBench）\n4. Real-world prevalence audit（55-87%）\n5. Type-mechanism dissociation 的实践价值"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性）\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] SESOI ±15pp 对安全研究领域缺乏充分论证\n- 论文选择 ±15pp 作为 TOST SESOI，理由是\"超过测量噪声 2 倍以上\"。对安全领域，14.9pp 额外违规率在规模化部署中意味数百次不安全行为。Table 3 的敏感性分析显示：在 ±10pp 时仅 3/7 达到等价性。Type-mechanism dissociation claim (C2) 完全依赖 TOST 等价性，更小的 SESOI 可能推翻部分类型对的等价结论。\n- 建议：提供基于安全领域的原则性论证；或以 ±10pp 为主分析。\n\n**N2** [critical] Incompleteness 的 information-addition confound 控制不充分\n- 唯一控制手段是 token count logistic regression。Token count 作为信息内容 proxy 存在根本缺陷：短语如\"non-refundable\"可能以极少 token 携带高政策信息量。回归假设 confound 通过 token count 线性作用，但实际 confound 是关于所添加信息的*类型*而非*数量*。\n- 建议：增加控制条件（添加等量但不解决 incompleteness 的政策文本）；或将 incompleteness 从主要因果 claims 中排除。\n\n**N3** [critical] ICC(1) = 0.919 仅限 OpenAI family，跨 provider 可复现性证据不足\n- ICC(1) = 0.919 仅基于 GPT-5.4 和 GPT-4.1。Appendix E 在 Gemini 和 LLAMA 上复制显示方向一致性但未计算 ICC。不同 provider 可能有质性不同的安全训练。\n- 建议：在全部七个模型上计算 ICC 或等效指标；或限定为 within-family consistency。\n\n### Should-Fix\n\n**W1** Authorization scope (κ=0.385, 52pp 跨模型变异) 是 construct validity 异常值。建议将主 taxonomy 呈现为五类型。\n\n**W2** 合成歧义到自然歧义效应差距（34pp vs 12.7pp）应在正文讨论，非仅 appendix。\n\n**W3** Temperature=0 限制了 variance decomposition 的解读。实际部署 temperature>0。\n\n**W4** Human validation 样本量（n=100）导致 per-type CI 较宽。Authorization scope 的 κ=0.385 基于 n=34。\n\n### Minor\n- \"Confound-free\"术语不一致\n- \"Nocuous\" 古体词可能降低可及性\n- Table 2 脚注标记较小\n\n### 优势\n1. 因果框架设计扎实（perturbation control 6.67pp upper bound）\n2. Confound 处理诚实（Appendix F）\n3. 全面的敏感性分析（7 个 margin TOST、bootstrap cluster、SOPBench）\n4. Real-world prevalence audit（55-87%）\n5. Type-mechanism dissociation 的实践价值"
  }
}
```

</details>

---


### Tool result

_source line 2290 · 2026-05-23T11:51:20.140000+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24520
}
```

</details>

---


### Tool call

_source line 2291 · 2026-05-23T11:51:20.291040+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性与完整性）\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] Type-mechanism dissociation（Contribution 2）核心证据可靠性不足\n- Failure mechanism 分类完全依赖 LLM 编码标签，人工标注 κ=0.15（Appendix AE）。论文承认 \"absolute NMI should be interpreted as an upper bound\"（§6.1），但仍作为主要贡献和 abstract 核心数字（V=0.45 vs. 0.14）呈现。LLM 编码标签的高一致性可能反映 LLM 系统性分类偏好而非真实关联。\n- 建议：将 type-mechanism dissociation 从 contribution 降级为 exploratory finding；分析 LLM 编码标签的分类模式；abstract 添加 caveat。\n\n**N2** [critical] \"Nocuous\" 术语语义反转未充分论证\n- Berry et al. (2004) 定义 nocuous = divergent interpretation。本文发现恰好相反——convergent error。标题直接使用 \"nocuous\" 无任何限定词。\n- 建议：标题改用更精确术语（如 \"systematically harmful\"）；或在 Introduction 充分论证语义延伸。\n\n### Should-Fix\n\n**W1** 'Ambiguity' 广义使用与 NLP 社区标准定义张力。Incompleteness/authorization scope/conditional precedence 不是严格的 linguistic ambiguity。建议引用 Poesio & Artstein (2005)，考虑 \"policy underspecification\" 作为上位术语。\n\n**W2** 跨领域 ρ=0.26 削弱 taxonomy 诊断价值。正文未报告此关键数字（仅 Appendix Z），Conclusion 需声明 type-level findings 是 domain-contingent。\n\n**W3** 相对 DRIP-R (2026) 增量贡献论证不够有力。DRIP-R 已在 400 scenarios × 5 types 上建立 \"ambiguity hurts agents\" 事实。本文的 causal design 是否改变了 DRIP-R 的结论？\n\n**W4** Taxonomy 11→6 选择标准论证不够系统。Ellipsis 排除理由写 \"not attested in RE\" 但真正原因可能是 minimal-pair 构造困难。\n\n**W5** Abstract 信息密度过高——约 190 词内 8+ 定量数字。\n\n### Minor\n- M1: Introduction motivating example 歧义过于明显\n- M2: Table 2 数字密度极高\n- M3: \"Confound-free types\" 首次出现时应更清楚定义\n- M4: 复制结果（Gemini, LLAMA）仅在 appendix\n- M5: Violation severity κ=0.653 vs failure mechanism κ=0.15 对比值得正文讨论\n\n### Missing References\n1. Poesio & Artstein (2005) — ambiguity vs underspecification\n2. Zhou et al. (2023) IFEval — instruction-following baseline\n3. Bai et al. (2022) Constitutional AI — permissive bias 背景\n4. Hu et al. (2023) / Ruis et al. (2023) — 已在 §2 提及\n\n### 优势\n1. 因果设计在 agent safety 文献中罕见\n2. Type-mechanism dissociation 有洞察力（方向性结论有说服力）\n3. 系统性控制和验证\n4. Appendix 深度和透明度\n5. 实践可操作性"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性与完整性）\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] Type-mechanism dissociation（Contribution 2）核心证据可靠性不足\n- Failure mechanism 分类完全依赖 LLM 编码标签，人工标注 κ=0.15（Appendix AE）。论文承认 \"absolute NMI should be interpreted as an upper bound\"（§6.1），但仍作为主要贡献和 abstract 核心数字（V=0.45 vs. 0.14）呈现。LLM 编码标签的高一致性可能反映 LLM 系统性分类偏好而非真实关联。\n- 建议：将 type-mechanism dissociation 从 contribution 降级为 exploratory finding；分析 LLM 编码标签的分类模式；abstract 添加 caveat。\n\n**N2** [critical] \"Nocuous\" 术语语义反转未充分论证\n- Berry et al. (2004) 定义 nocuous = divergent interpretation。本文发现恰好相反——convergent error。标题直接使用 \"nocuous\" 无任何限定词。\n- 建议：标题改用更精确术语（如 \"systematically harmful\"）；或在 Introduction 充分论证语义延伸。\n\n### Should-Fix\n\n**W1** 'Ambiguity' 广义使用与 NLP 社区标准定义张力。Incompleteness/authorization scope/conditional precedence 不是严格的 linguistic ambiguity。建议引用 Poesio & Artstein (2005)，考虑 \"policy underspecification\" 作为上位术语。\n\n**W2** 跨领域 ρ=0.26 削弱 taxonomy 诊断价值。正文未报告此关键数字（仅 Appendix Z），Conclusion 需声明 type-level findings 是 domain-contingent。\n\n**W3** 相对 DRIP-R (2026) 增量贡献论证不够有力。DRIP-R 已在 400 scenarios × 5 types 上建立 \"ambiguity hurts agents\" 事实。本文的 causal design 是否改变了 DRIP-R 的结论？\n\n**W4** Taxonomy 11→6 选择标准论证不够系统。Ellipsis 排除理由写 \"not attested in RE\" 但真正原因可能是 minimal-pair 构造困难。\n\n**W5** Abstract 信息密度过高——约 190 词内 8+ 定量数字。\n\n### Minor\n- M1: Introduction motivating example 歧义过于明显\n- M2: Table 2 数字密度极高\n- M3: \"Confound-free types\" 首次出现时应更清楚定义\n- M4: 复制结果（Gemini, LLAMA）仅在 appendix\n- M5: Violation severity κ=0.653 vs failure mechanism κ=0.15 对比值得正文讨论\n\n### Missing References\n1. Poesio & Artstein (2005) — ambiguity vs underspecification\n2. Zhou et al. (2023) IFEval — instruction-following baseline\n3. Bai et al. (2022) Constitutional AI — permissive bias 背景\n4. Hu et al. (2023) / Ruis et al. (2023) — 已在 §2 提及\n\n### 优势\n1. 因果设计在 agent safety 文献中罕见\n2. Type-mechanism dissociation 有洞察力（方向性结论有说服力）\n3. 系统性控制和验证\n4. Appendix 深度和透明度\n5. 实践可操作性"
  }
}
```

</details>

---


### Tool result

_source line 2292 · 2026-05-23T11:51:21.898619+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1607
}
```

</details>

---


### Assistant

_source line 2293 · 2026-05-23T11:51:25.353554+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 218

## Round 218

10 recorded events


### User

_source line 2294 · 2026-05-23T11:51:26.342511+00:00_

[Reviewer 1 审稿结果]:
PDF 临时图片已清理。审稿完成。

---

[Reviewer 2 审稿结果]:
审稿完成。报告已提交至 Review Director，评分 **Overall 3.5（Borderline Conference）**。

核心判断：
- **方法论严谨**（matched-pair causal design、全面的统计控制），但**新颖性受限**于 DRIP-R 的并发工作
- 两个 **Must-Fix**：(1) type-mechanism dissociation 的核心证据依赖可靠性存疑的 LLM 编码标签（人工 κ=0.15），需要在正文中充分讨论并考虑降级为 exploratory finding；(2) "nocuous" 术语的语义反转（divergent→convergent）需要更充分的论证或改用更精确的术语
- 四个 **Should-Fix**：'ambiguity' 广义使用的术语张力、跨领域 ρ=0.26 的泛化性限制、与 DRIP-R 的增量贡献论证、taxonomy 11→6 的选择标准透明度

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2295 · 2026-05-23T11:52:01.073280+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool call

_source line 2296 · 2026-05-23T11:52:01.073720+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2297 · 2026-05-23T11:52:01.125571+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T11:41:43.525340+00:00\", \"completed_at\": \"2026-05-23T11:45:28.584657+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页仅有 Title + Abstract，无视觉锚点。排版整洁，ACL 双栏格式正确，行号和 \\\"Anonymous ACL submission\\\" 标注符合匿名投稿要求\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（实验 pipeline 概览图）出现在第 2 页顶部，作为首个 display item 位置合理。三面板设计（Taxonomy → Evaluation → Cross-judge）清晰传达实验流程，但面板内文字偏小（约正文 60%），审稿人需要放大才能读清具体模型名和数字\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1（六类歧义分类）使用 booktabs 风格，排版干净。表格宽度适配单栏，三列（Type/Layer/Mechanism/Resolving Channel）信息密度合理\"}, {\"severity\": \"warning\", \"dimension\": \"page 5-6\", \"message\": \"连续 2 页纯文本（Methods 4.3-4.6 + Results 5.1-5.2），无任何 display item 穿插。尤其 Results 5.1-5.2 包含大量定量结果（OR、CI、p 值），审稿人在纯文本中追踪这些数字体验较差。建议考虑将关键统计结果提炼为小型 summary table\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"页面极度拥挤：Figure 2（左栏上半）+ Figure 3（右栏上部）+ Figure 4（右栏中部）+ Section 7 Discussion 开头 + Section 8 Conclusion 开头，全部挤在一页。三张图各自被压缩到较小尺寸，axis labels 和 heatmap 内标注在打印时可能处于可读性边缘\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2（per-type effect sizes 条形图）：误差线和 CI 标注清晰，颜色使用单色调，色盲友好。但条形图内的 type 标签字号偏小\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 3（violation rates heatmap）：红色渐变色阶通过亮度变化区分，色盲友好。单元格内百分比标注可读。Caption 自包含，说明了 n=2,997 和关键发现\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4（type-mechanism association heatmap）：与 Figure 3 风格一致，NMI 值标注在 caption 中。颜色语义与 Figure 3 保持一致（同为红色系渐变）\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2（全宽表）：booktabs 风格，最优值加粗，CI 用方括号标注，精度统一。Tier 列使用 U/M/L 缩写在 caption 中有解释。排版专业\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Section 7 \\\"Discussion\\\" 标题后有约 10 行正文在同一页，未孤悬。Section 8 \\\"Conclusion\\
…[truncated 1385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 2298 · 2026-05-23T11:52:01.126059+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 2299 · 2026-05-23T11:57:13.658584+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 26\n\n# ============================================================\n# R26 ISSUES — ACTIVE\n# ============================================================\n\n- id: \"R26-MF1\"\n  summary: \"Type-mechanism dissociation (Contribution 2) 核心证据依赖 LLM 编码标签，人工 κ=0.15 可靠性不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W8: §6 仍用 'mechanistically distinct' 等强表述，已修为 'as classified by LLM coders'\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix N1, R1 Soundness 3/5 部分归因于此。共识：V=0.45 作为 headline contribution 但人工 κ=0.15 使 Contribution 2 置信度大打折扣。LLM 编码一致性可能反映系统性分类偏好而非真实关联。建议降级为 exploratory finding，abstract 添加 caveat\"\n  action_items:\n    - round: 26\n      action: \"§6 主文显著讨论 κ=0.15 对 type-mechanism dissociation 的影响；考虑将 Contribution 2 降级为 exploratory finding；abstract V=0.45 添加 caveat\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-MF2\"\n  summary: \"SESOI ±15pp 对安全研究领域缺乏原则性论证——C2 partial ordering 完全依赖此 margin\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R24-W4 resolved: 已改为 'pragmatic default, not principled domain-anchored threshold'\"\n    - round: 26\n      reviewers: [1]\n      note: \"R1 Must-Fix N1。14.9pp 额外违规率在规模化部署中意味数百次不安全行为。Table 3 在 ±10pp 时仅 3/15 达等价。'pragmatic default' 表述不足以支撑 safety claims\"\n  action_items:\n    - round: 26\n      action: \"提供基于安全领域的原则性 ±15pp 论证；或以 ±10pp 为主分析、±15pp 为敏感性分析；或显式限定 C2 claims 到所选 margin\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-MF3\"\n  summary: \"Incompleteness confound 控制方法论不充分——token count 作为信息内容 proxy 有根本缺陷\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W9: §5.1 已增加 'controlling for token count—a coarse proxy' caveat\"\n    - round: 26\n      reviewers: [1]\n      note: \"R1 Must-Fix N2。token count 假设 confound 线性作用，但实际 confound 是信息*类型*而非*数量*。'non-refundable' 以极少 token 携带高政策信息量\"\n  action_items:\n    - round: 26\n      action: \"增加控制条件（添加等量但不解决 incompleteness 的政策文本）；或将 incompleteness 从主要因果 claims 排除，31.0pp 为 headline\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-MF4\"\n  summary: \"ICC(1)=0.919 仅限 OpenAI family——跨 provider 可复现性证据不足以支撑 cross-model consistency 声明\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W6: 标题已改为 'Within-family reproducibility'\"\n    - round: 26\n      reviewers: [1]\n      note: \"R1 Must-Fix N3。Gemini/LLAMA 复制显示方向一致性但未计算 ICC。不同 provider 安全训练可能质性不同。标题修改不够——需要跨 provider 的定量可复现性指标\"\n  action_items:\n    - round: 26\n      action: \"在全部 7 个模型上计算 ICC 或等效可复现性指标；或将可复现性声明明确限定为 within-family consistency，并讨论跨 provider 的限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF1\"\n  summary: \"'Nocuous' 术语语义反转（divergent→convergent）需更充分论证或改用更精确术语\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W4: Introduction 已加 'convergent rather than divergent misinterpretation' 句\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix N2, R1 Minor。共识 Should-Fix：Introduction 的一句话不足以论证标题级别的术语使用。Berry (2004) nocuous = divergent, 本文 = convergent，不是同一种 nocuous\"\n  action_items:\n    - round: 26\n      action: \"Introduction 充分论证 nocuous 的语义延伸（不仅一句话）；或标题改用 systematically harmful/convergently harmful\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF2\"\n  summary: \"Authorization scope 是 construct outlier (κ=0.385, 52pp range)，扭曲 headline statistics\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W1: Discussion ¶1 已加 outlier sentence with κ, range, sans-auth appendix reference\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W1, R2 aligned。一句话声明不足——auth scope 驱动 C4 interaction、ρ=0.09 跨组、最低 κ。建议五类型结果为主、auth scope 为补充\"\n  action_items:\n    - round: 26\n      action: \"将五类型结果呈现为主分析，auth scope 作为独立低置信度 construct 补充报告\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF3\"\n  summary: \"合成→自然效应差距（34pp vs 12.7pp, 2.7×）和跨领域 ρ=0.26 需在正文讨论\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-N1/N2: Abstract/Conclusion 已报告两个数字，Discussion 已扩展 ecological validity 段\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1-W2, R2-W2。效应差距的三因素解释合理但仅在 appendix。ρ=0.26 仅在 Appendix Z，正文未报告此关键泛化性限制\"\n  action_items:\n    - round: 26\n      action: \"Discussion §7 将三因素解释和 ρ=0.26 移至正文；Conclusion 声明 type-level findings are domain-contingent\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF4\"\n  summary: \"相对 DRIP-R (2026) 增量贡献论证不够有力\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [2]\n      note: \"R2 Should-Fix W3。DRIP-R 已在 400 scenarios × 5 RE types 建立 'ambiguity hurts agents' 事实。本文 causal design 是否改变了 DRIP-R 的结论？如果只是更严格确认，contribution bar 更高\"\n  action_items:\n    - round: 26\n      action: \"§2 或 §7 增加直接对比段落：DRIP-R correlational evidence 留下哪些 confound？causal design 回答了哪些新问题？\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF5\"\n  summary: \"'Ambiguity' 广义使用与 NLP 社区标准定义张力——需引用 underspecification 区分文献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W3: §3 已增加 NLP classification positioning sentence (Wasow et al. 2005)\"\n    - round: 26\n      reviewers: [2]\n      note: \"R2 Should-Fix W1。一句 Wasow 引用不够——需引用 Poesio & Artstein (2005) 关于 ambiguity vs underspecification 的经典区分，考虑 policy underspecification 作为上位术语\"\n  action_items:\n    - round: 26\n      action: \"§3 增加系统性论证：引用 Poesio & Artstein (2005)，说明为什么 agent safety 研究目的下合并是有信息量的\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF6\"\n  summary: \"Temperature=0 限制 variance decomposition 解读——需在正文明确说明\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W10: Limitations 已增加 temperature>0 方向性讨论\"\n    - round: 26\n      reviewers: [1]\n      note: \"R1 Should-Fix W3。Limitations 的方向性预测不够——variance decomposition 部分本身需要说明 temperature=0 如何影响其解读\"\n  action_items:\n    - round: 26\n      action: \"§5.1 variance decomposition 段落增加 temperature=0 限制说明\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF7\"\n  summary: \"Taxonomy 11→6 选择标准需更透明报告——实际构造困难不应伪装为概念标准\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W2: Appendix 已增加 11→6 mapping 表格 + §3 引用\"\n    - round: 26\n      reviewers: [2]\n      note: \"R2 Should-Fix W4。表格存在但排除理由不够诚实——ellipsis 排除归因 RE attestation 但真正原因可能是 minimal-pair 构造困难\"\n  action_items:\n    - round: 26\n      action: \"Appendix M 坦诚标注哪些类型因实际构造困难排除，与概念标准分开\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF8\"\n  summary: \"Abstract 信息密度过高——~190 词内 8+ 定量数字稀释核心信息\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-M1 (数字密度), R23-M2 (abstract info overload) resolved。之前是 minor\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix W5, R1 aligns。升级为 Should-Fix。核心信息被 8+ 数字淹没\"\n  action_items:\n    - round: 26\n      action: \"精简 abstract 至 2-3 个核心数字，其余移至 §5/§6\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M1\"\n  summary: \"'Confound-free' 术语不一致：Abstract 指排除 incompleteness vs Limitations 指 perturbation 后\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立标记\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M2\"\n  summary: \"Violation severity κ=0.653 vs failure mechanism κ=0.15 对比本身是值得正文讨论的发现\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [2]\n      note: \"R2-M5。两个 κ 值的鲜明对比说明 violation detection 可靠但 mechanism classification 边界模糊\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R25 ISSUES — STATUS UPDATE\n# ============================================================\n\n- id: \"R25-W5\"\n  summary: \"C3 inconclusive 但 taxonomy 仍按 two-layer 组织——需显式声明为理论组织框架\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"§3 已改为 'design hypothesis' + 'provides an organizational framework'\"\n    - round: 26\n      reviewers: []\n      note: \"R26 两位 Reviewer 均未重新标记此问题，可能已修复。待 Research Director 确认\"\n  action_items:\n    - round: 25\n      action: \"§3 'comprises' → 'provides an organizational framework of'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Changed 'Our taxonomy comprises six types' to 'Our taxonomy provides an organizational framework of six types'\"\n  resolution_round: null\n\n- id: \"R25-W7\"\n  summary: \"60.8% 残差方差中 ~46% 系统性部分未讨论可能来源\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"Discussion ¶1 已增加系统性残差候选来源\"\n    - round: 26\n      reviewers: []\n      note: \"R26 两位 Reviewer 均未重新标记此问题，可能已修复。待 Research Director 确认\"\n  action_items:\n    - round: 25\n      action: \"Discussion ¶1 增加系统性残差候选来源\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Discussion ¶1 adds inline: 'the systematic component reflects clause-level interactions—conversation trajectory, tool-use sequencing, clause×scenario contingencies—that type-level taxonomies cannot capture'\"\n  resolution_round: null\n\n- id: \"R25-M2\"\n  summary: \"Disambiguation neglect 增量贡献需更明确阐述\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [2]\n      note: \"§6.2 已重写为 extending ambiguity collapse to agentic context\"\n    - round: 26\n      reviewers: []\n      note: \"R26 两位 Reviewer 均未重新标记此问题，可能已修复。待 Research Director 确认\"\n  action_items:\n    - round: 25\n      action: \"§6.2 disambiguation neglect 定义改为 extending ambiguity collapse to agentic context\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"§6.2 rewritten: 'extending the ambiguity collapse phenomenon documented in static NLP tasks to agentic policy execution, where it produces irreversible safety violations rather than mere accuracy degradation'\"\n  resolution_round: null\n\n- id: \"R25-M3\"\n  summary: \"References 中 arXiv preprint 格式不统一\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [2]\n      note: \"部分用 'arXiv preprint arXiv:XXXX'，部分仅有 ID\"\n  action_items: []\n  resolution: \"Verified: all arXiv entries consistently use journal={arXiv preprint arXiv:XXXX.XXXXX} format.\"\n  resolution_round: 25\n\n# ============================================================\n# R24 ISSUES — RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R24-N1\"\n  summary: \"Novelty framing 偏强——'first matched-pair causal study' 是领域迁移而非方法论创新\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Contributions 重写为 (1) causal study 基础, (2) diagnostic taxonomy, (3) disambiguation neglect + systematic nocuity\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 25\n\n- id: \"R24-N2\"\n  summary: \"Incompleteness confound framing 不够突出——confound-free range 应作为 headline\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Abstract 已以 confound-free 31.0pp 为 lead\"\n  resolution_round: 25\n  first_raised_round: 21\n  last_seen_round: 24\n\n- id: \"R24-W2\"\n  summary: \"Template pipeline 不透明\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Appendix S (Clause Pair Construction) 已补充\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W4\"\n  summary: \"SESOI ±15pp justification 不够 principled\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"§4.6 已改为 'pragmatic default, not principled domain-anchored threshold'. Note: R26 re-raised as MF2 with higher severity\"\n  resolution_round: 25\n  first_raised_round: 20\n  last_seen_round: 26\n\n- id: \"R24-W6\"\n  summary: \"Human validation per-type CI 极宽\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Per-type κ 引用处已附 qualifier\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W8\"\n  summary: \"NMI cardinality 不对称——'order of magnitude' 表述含 artifact\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"全文改为 'substantially more strongly'；Appendix 表补 V=0.137 + 维度差异脚注\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M4\"\n  summary: \"C3/C4 claim 层级暗示四个同等级\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"§5 开头已标 C3 inconclusive, C4 exploratory\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M5\"\n  summary: \"Table 2 脚注缺 per-type 样本量\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"脚注已加 n≈17\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M6\"\n  summary: \"Prevalence audit κ=0.295 未在 Introduction 标注\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Introduction 引用处已标注 'dual-judge κ = 0.30'\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X1\"\n  summary: \"ICC≈0 应改为 ICC=-0.006 uninformative due to floor effects\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Appendix AB 已改为 uninformative + floor effect 解释\"\n  resolution_round: 25\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R24-X3\"\n  summary: \"Limitations 过长（5段）——EMNLP 要求 ~3 个点一小段\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"Limitations 已压缩为一段 3 个要点\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X4\"\n  summary: \"Limitations 说人工验证 'underway' 但 Appendix 已有结果——内部矛盾\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"已删除 underway 表述，替换为实际结果引用\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 26\n\n# ============================================================\n# R26 ISSUES — ACTIVE\n# ============================================================\n\n- id: \"R26-MF1\"\n  summary: \"Type-mechanism dissociation (Contribution 2) 核心证据依赖 LLM 编码标签，人工 κ=0.15 可靠性不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W8: §6 仍用 'mechanistically distinct' 等强表述，已修为 'as classified by LLM coders'\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix N1, R1 Soundness 3/5 部分归因于此。共识：V=0.45 作为 headline contribution 但人工 κ=0.15 使 Contribution 2 置信度大打折扣。LLM 编码一致性可能反映系统性分类偏好而非真实关联。建议降级为 exploratory finding，abstract 添加 caveat\"\n  action_items:\n    - round: 26\n      action: \"§6 主文显著讨论 κ=0.15 对 type-mechanism dissociation 的影响；考虑将 Contribution 2 降级为 exploratory finding；abstract V=0.45 添加 caveat\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-MF2\"\n  summary: \"SESOI ±15pp 对安全研究领域缺乏原则性论证——C2 partial ordering 完全依赖此 margin\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R24-W4 resolved: 已改为 'pragmatic default, not principled domain-anchored threshold'\"\n    - round: 26\n      reviewers: [1]\n      note: \"R1 Must-Fix N1。14.9pp 额外违规率在规模化部署中意味数百次不安全行为。Table 3 在 ±10pp 时仅 3/15 达等价。'pragmatic default' 表述不足以支撑 safety claims\"\n  action_items:\n    - round: 26\n      action: \"提供基于安全领域的原则性 ±15pp 论证；或以 ±10pp 为主分析、±15pp 为敏感性分析；或显式限定 C2 claims 到所选 margin\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-MF3\"\n  summary: \"Incompleteness confound 控制方法论不充分——token count 作为信息内容 proxy 有根本缺陷\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W9: §5.1 已增加 'controlling for token count—a coarse proxy' caveat\"\n    - round: 26\n      reviewers: [1]\n      note: \"R1 Must-Fix N2。token count 假设 confound 线性作用，但实际 confound 是信息*类型*而非*数量*。'non-refundable' 以极少 token 携带高政策信息量\"\n  action_items:\n    - round: 26\n      action: \"增加控制条件（添加等量但不解决 incompleteness 的政策文本）；或将 incompleteness 从主要因果 claims 排除，31.0pp 为 headline\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-MF4\"\n  summary: \"ICC(1)=0.919 仅限 OpenAI family——跨 provider 可复现性证据不足以支撑 cross-model consistency 声明\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W6: 标题已改为 'Within-family reproducibility'\"\n    - round: 26\n      reviewers: [1]\n      note: \"R1 Must-Fix N3。Gemini/LLAMA 复制显示方向一致性但未计算 ICC。不同 provider 安全训练可能质性不同。标题修改不够——需要跨 provider 的定量可复现性指标\"\n  action_items:\n    - round: 26\n      action: \"在全部 7 个模型上计算 ICC 或等效可复现性指标；或将可复现性声明明确限定为 within-family consistency，并讨论跨 provider 的限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF1\"\n  summary: \"'Nocuous' 术语语义反转（divergent→convergent）需更充分论证或改用更精确术语\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W4: Introduction 已加 'convergent rather than divergent misinterpretation' 句\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix N2, R1 Minor。共识 Should-Fix：Introduction 的一句话不足以论证标题级别的术语使用。Berry (2004) nocuous = divergent, 本文 = convergent，不是同一种 nocuous\"\n  action_items:\n    - round: 26\n      action: \"Introduction 充分论证 nocuous 的语义延伸（不仅一句话）；或标题改用 systematically harmful/convergently harmful\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF2\"\n  summary: \"Authorization scope 是 construct outlier (κ=0.385, 52pp range)，扭曲 headline statistics\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W1: Discussion ¶1 已加 outlier sentence with κ, range, sans-auth appendix reference\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W1, R2 aligned。一句话声明不足——auth scope 驱动 C4 interaction、ρ=0.09 跨组、最低 κ。建议五类型结果为主、auth scope 为补充\"\n  action_items:\n    - round: 26\n      action: \"将五类型结果呈现为主分析，auth scope 作为独立低置信度 construct 补充报告\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF3\"\n  summary: \"合成→自然效应差距（34pp vs 12.7pp, 2.7×）和跨领域 ρ=0.26 需在正文讨论\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-N1/N2: Abstract/Conclusion 已报告两个数字，Discussion 已扩展 ecological validity 段\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1-W2, R2-W2。效应差距的三因素解释合理但仅在 appendix。ρ=0.26 仅在 Appendix Z，正文未报告此关键泛化性限制\"\n  action_items:\n    - round: 26\n      action: \"Discussion §7 将三因素解释和 ρ=0.26 移至正文；Conclusion 声明 type-level findings are domain-contingent\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF4\"\n  summary: \"相对 DRIP-R (2026) 增量贡献论证不够有力\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [2]\n      note: \"R2 Should-Fix W3。DRIP-R 已在 400 scenarios × 5 RE types 建立 'ambiguity hurts agents' 事实。本文 causal design 是否改变了 DRIP-R 的结论？如果只是更严格确认，contribution bar 更高\"\n  action_items:\n    - round: 26\n      action: \"§2 或 §7 增加直接对比段落：DRIP-R correlational evidence 留下哪些 confound？causal design 回答了哪些新问题？\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF5\"\n  summary: \"'Ambiguity' 广义使用与 NLP 社区标准定义张力——需引用 underspecification 区分文献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W3: §3 已增加 NLP classification positioning sentence (Wasow et al. 2005)\"\n    - round: 26\n      reviewers: [2]\n      note: \"R2 Should-Fix W1。一句 Wasow 引用不够——需引用 Poesio & Artstein (2005) 关于 ambiguity vs underspecification 的经典区分，考虑 policy underspecification 作为上位术语\"\n  action_items:\n    - round: 26\n      action: \"§3 增加系统性论证：引用 Poesio & Artstein (2005)，说明为什么 agent safety 研究目的下合并是有信息量的\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF6\"\n  summary: \"Temperature=0 限制 variance decomposition 解读——需在正文明确说明\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W10: Limitations 已增加 temperature>0 方向性讨论\"\n    - round: 26\n      reviewers: [1]\n      note: \"R1 Should-Fix W3。Limitations 的方向性预测不够——variance decomposition 部分本身需要说明 temperature=0 如何影响其解读\"\n  action_items:\n    - round: 26\n      action: \"§5.1 variance decomposition 段落增加 temperature=0 限制说明\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF7\"\n  summary: \"Taxonomy 11→6 选择标准需更透明报告——实际构造困难不应伪装为概念标准\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W2: Appendix 已增加 11→6 mapping 表格 + §3 引用\"\n    - round: 26\n      reviewers: [2]\n      note: \"R2 Should-Fix W4。表格存在但排除理由不够诚实——ellipsis 排除归因 RE attestation 但真正原因可能是 minimal-pair 构造困难\"\n  action_items:\n    - round: 26\n      action: \"Appendix M 坦诚标注哪些类型因实际构造困难排除，与概念标准分开\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF8\"\n  summary: \"Abstract 信息密度过高——~190 词内 8+ 定量数字稀释核心信息\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-M1 (数字密度), R23-M2 (abstract info overload) resolved。之前是 minor\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix W5, R1 aligns。升级为 Should-Fix。核心信息被 8+ 数字淹没\"\n  action_items:\n    - round: 26\n      action: \"精简 abstract 至 2-3 个核心数字，其余移至 §5/§6\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M1\"\n  summary: \"'Confound-free' 术语不一致：Abstract 指排除 incompleteness vs Limitations 指 perturbation 后\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立标记\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M2\"\n  summary: \"Violation severity κ=0.653 vs failure mechanism κ=0.15 对比本身是值得正文讨论的发现\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [2]\n      note: \"R2-M5。两个 κ 值的鲜明对比说明 violation detection 可靠但 mechanism classification 边界模糊\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R25 ISSUES — STATUS UPDATE\n# ============================================================\n\n- id: \"R25-W5\"\n  summary: \"C3 inconclusive 但 taxonomy 仍按 two-layer 组织——需显式声明为理论组织框架\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"§3 已改为 'design hypothesis' + 'provides an organizational framework'\"\n    - round: 26\n      reviewers: []\n      note: \"R26 两位 Reviewer 均未重新标记此问题，可能已修复。待 Research Director 确认\"\n  action_items:\n    - round: 25\n      action: \"§3 'comprises' → 'provides an organizational framework of'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Changed 'Our taxonomy comprises six types' to 'Our taxonomy provides an organizational framework of six types'\"\n  resolution_round: null\n\n- id: \"R25-W7\"\n  summary: \"60.8% 残差方差中 ~46% 系统性部分未讨论可能来源\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"Discussion ¶1 已增加系统性残差候选来源\"\n    - round: 26\n      reviewers: []\n      note: \"R26 两位 Reviewer 均未重新标记此问题，可能已修复。待 Research Director 确认\"\n  action_items:\n    - round: 25\n      action: \"Discussion ¶1 增加系统性残差候选来源\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Discussion ¶1 adds inline: 'the systematic component reflects clause-level interactions—conversation trajectory, tool-use sequencing, clause×scenario contingencies—that type-level taxonomies cannot capture'\"\n  resolution_round: null\n\n- id: \"R25-M2\"\n  summary: \"Disambiguation neglect 增量贡献需更明确阐述\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [2]\n      note: \"§6.2 已重写为 extending ambiguity collapse to agentic context\"\n    - round: 26\n      reviewers: []\n      note: \"R26 两位 Reviewer 均未重新标记此问题，可能已修复。待 Research Director 确认\"\n  action_items:\n    - round: 25\n      action: \"§6.2 disambiguation neglect 定义改为 extending ambiguity collapse to agentic context\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"§6.2 rewritten: 'extending the ambiguity collapse phenomenon documented in static NLP tasks to agentic policy execution, where it produces irreversible safety violations rather than mere accuracy degradation'\"\n  resolution_round: null\n\n- id: \"R25-M3\"\n  summary: \"References 中 arXiv preprint 格式不统一\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [2]\n      note: \"部分用 'arXiv preprint arXiv:XXXX'，部分仅有 ID\"\n  action_items: []\n  resolution: \"Verified: all arXiv entries consistently use journal={arXiv preprint arXiv:XXXX.XXXXX} format.\"\n  resolution_round: 25\n\n# ============================================================\n# R24 ISSUES — RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R24-N1\"\n  summary: \"Novelty framing 偏强——'first matched-pair causal study' 是领域迁移而非方法论创新\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Contributions 重写为 (1) causal study 基础, (2) diagnostic taxonomy, (3) disambiguation neglect + systematic nocuity\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 25\n\n- id: \"R24-N2\"\n  summary: \"Incompleteness confound framing 不够突出——confound-free range 应作为 headline\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Abstract 已以 confound-free 31.0pp 为 lead\"\n  resolution_round: 25\n  first_raised_round: 21\n  last_seen_round: 24\n\n- id: \"R24-W2\"\n  summary: \"Template pipeline 不透明\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Appendix S (Clause Pair Construction) 已补充\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W4\"\n  summary: \"SESOI ±15pp justification 不够 principled\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"§4.6 已改为 'pragmatic default, not principled domain-anchored threshold'. Note: R26 re-raised as MF2 with higher severity\"\n  resolution_round: 25\n  first_raised_round: 20\n  last_seen_round: 26\n\n- id: \"R24-W6\"\n  summary: \"Human validation per-type CI 极宽\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Per-type κ 引用处已附 qualifier\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W8\"\n  summary: \"NMI cardinality 不对称——'order of magnitude' 表述含 artifact\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"全文改为 'substantially more strongly'；Appendix 表补 V=0.137 + 维度差异脚注\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M4\"\n  summary: \"C3/C4 claim 层级暗示四个同等级\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"§5 开头已标 C3 inconclusive, C4 exploratory\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M5\"\n  summary: \"Table 2 脚注缺 per-type 样本量\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"脚注已加 n≈17\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M6\"\n  summary: \"Prevalence audit κ=0.295 未在 Introduction 标注\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Introduction 引用处已标注 'dual-judge κ = 0.30'\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X1\"\n  summary: \"ICC≈0 应改为 ICC=-0.006 uninformative due to floor effects\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Appendix AB 已改为 uninformative + floor effect 解释\"\n  resolution_round: 25\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R24-X3\"\n  summary: \"Limitations 过长（5段）——EMNLP 要求 ~3 个点一小段\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"Limitations 已压缩为一段 3 个要点\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X4\"\n  summary: \"Limitations 说人工验证 'underway' 但 Appendix 已有结果——内部矛盾\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"已删除 underway 表述，替换为实际结果引用\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24"
  }
}
```

</details>

---


### Tool result

_source line 2300 · 2026-05-23T11:57:13.761481+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 15647}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2301 · 2026-05-23T11:59:33.875534+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Round 26 (Fresh)\n\n**Paper**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n**Venue**: EMNLP 2026 via ARR May cycle\n**Reviewers**: 2 (R1: 方法严谨性, R2: 新颖性与完整性)\n**Date**: 2026-05-23\n\n---\n\n## Summary\n\nThis paper uses a matched-pair causal design to study how policy ambiguity affects safety violations in LLM agents. Using 300 clause pairs across a six-type taxonomy on τ²-bench with five models (2,997 episodes), the authors show ambiguous clauses increase violations by +34.0pp (+31.0pp confound-free). The core finding is a \"type-mechanism dissociation\": ambiguity type predicts failure mechanism (Cramér's V=0.45) but not violation rate (V=0.14). Error analysis reveals \"disambiguation neglect\" (4.6% awareness) and \"systematic nocuity\" (77% permissive bias, convergent errors).\n\n---\n\n## Strengths\n\n**S1. Matched-pair causal design is methodologically strong.** Rare in agent safety literature. Perturbation controls (Δ_perturb = -0.67pp, CI [-8.0, 6.67]) convincingly exclude surface-level rewriting as alternative explanation. 300 clause pairs × 5 models with 96% initial annotator agreement provides solid internal validity.\n\n**S2. Comprehensive statistical analysis and transparency.** TOST equivalence testing across 7 margins, bootstrap cluster analysis, ICC variance decomposition, cross-benchmark replication (SOPBench), cross-architecture replication (Gemini, LLaMA), and 15 pages of appendices addressing nearly all foreseeable reviewer questions.\n\n**S3. Type-mechanism dissociation has practical value.** Even with reliability caveats, the directional finding that type predicts mechanism more strongly than severity is actionable: clause-level auditing > type-level risk classification.\n\n**S4. Real-world grounding.** Prevalence audit (24 production documents, 407 clauses, 55–87% ambiguous) establishes practical relevance. SOPBench cross-benchmark replication confirms directional consistency.\n\n**S5. Confound handling is honest.** Incompleteness information-addition confound is explicitly identified, separately analyzed (Appendix F), and the confound-free effect (31.0pp) is reported alongside the full effect (34.0pp).\n\n---\n\n## Weaknesses\n\n### Must-Fix (4 issues — affect acceptance decision)\n\n**MF1. [consensus, critical] Type-mechanism dissociation (Contribution 2) reliability is insufficiently supported.**\n- Location: §6.1, Appendix AE\n- The core evidence for V=0.45 rests entirely on LLM-coded failure mechanism labels, while human annotation agreement is κ=0.15 (near chance). The paper acknowledges this is an \"upper bound\" (§6.1) but still presents it as a headline contribution and abstract number. LLM coding consistency may reflect systematic classification preferences rather than genuine type-mechanism association.\n- R2 rated this Must-Fix; R1's Soundness 3/5 partly reflects this concern.\n- **Action required**: (a) Prominently discuss κ=0.15 in main text §6 (not just parenthetical); (b) consider downgrading type-mechanism dissociation from \"contribution\" to \"exploratory finding\"; (c) add explicit caveat to abstract V=0.45 figure; (d) report V computed from human annotations as a floor estimate.\n\n**MF2. [R1 Must-Fix] SESOI ±15pp lacks principled domain justification.**\n- Location: §4.6, Table 3\n- The C2 partial ordering (type equivalence structure) depends entirely on TOST equivalence at ±15pp. For safety-critical applications, 14.9pp additional violation rate at scale could mean hundreds of unsafe actions. At ±10pp, only 3/15 type pairs reach equivalence. The paper acknowledges \"pragmatic default\" but this is insufficient for safety claims.\n- **Action required**: Provide safety-domain-grounded justification for ±15pp; or adopt ±10pp as primary analysis with ±15pp as sensitivity; or explicitly scope C2 claims to the chosen margin.\n\n**MF3. [R1 Must-Fix] Incompleteness confound control is methodologically insufficient.**\n- Location: §4.5, Appendix F\n- Token count as a proxy for information content has a fundamental flaw: a short phrase like \"non-refundable\" carries high policy information in few tokens, while lengthy clarifications may add minimal semantic content. The regression assumes linear token-count mediation, but the actual confound concerns information *type* (policy-relevant vs. disambiguating), not *quantity*.\n- **Action required**: (a) Add a control condition with equal-length non-disambiguating policy text to directly isolate the information-addition effect; or (b) exclude incompleteness from primary causal claims and treat as observational evidence, using confound-free 31.0pp as the headline effect.\n\n**MF4. [R1 Must-Fix] Cross-provider reproducibility evidence is insufficient.**\n- Location: §4.4, Appendix AC/E\n- ICC(1)=0.919 is computed only within the OpenAI family (GPT-5.4, GPT-4.1). The Gemini/LLaMA replication (Appendix E) shows directional consistency but no ICC. Different providers may have qualitatively different safety training; within-family ICC cannot capture this dimension.\n- **Action required**: Compute cross-provider ICC or equivalent metric across all 7 models; or explicitly limit reproducibility claims to within-family consistency and discuss cross-provider limitations.\n\n### Should-Fix (8 issues — affect scoring)\n\n**SF1. [R2 Must-Fix → consensus Should-Fix] \"Nocuous\" terminology semantic inversion needs stronger justification.**\nBerry et al. (2004) define nocuous = divergent interpretation; this paper finds convergent error. The title uses \"nocuous\" without qualification. R2 elevated to Must-Fix; R1 noted as Minor. Consensus at Should-Fix: the semantic extension is defensible but needs explicit justification in Introduction (not just one sentence referencing §6), or terminology revision.\n\n**SF2. [consensus] Authorization scope is a construct outlier distorting headline statistics.**\nκ=0.385 (lowest), 52pp cross-model range (largest), drives C4 interaction, causes ρ=0.09 cross-judge-group discordance. One sentence in Discussion is insufficient. Action: Present five-type results as primary; auth scope as supplementary low-confidence construct.\n\n**SF3. [consensus] Synthetic-to-natural effect gap (34pp vs 12.7pp) and cross-domain ρ=0.26 need main text discussion.**\nThe three-factor explanation (measurement grain, baseline compression, interaction depth) is reasonable but only in appendix. ρ=0.26 (effectively zero correlation for type rankings across domains) is only in Appendix Z but directly impacts taxonomy diagnostic claims. Action: Move both to Discussion §7; Conclusion should state type-level findings are domain-contingent.\n\n**SF4. [R2 Should-Fix] Incremental contribution over DRIP-R (2026) is under-argued.**\nDRIP-R already establishes \"ambiguity hurts agents\" on 400 scenarios × 5 RE types. The paper lists three differentiators but doesn't argue why the causal → correlational upgrade changes conclusions. Action: Add direct comparison paragraph in §2 or §7 specifying which confounds DRIP-R's correlational design leaves unaddressed.\n\n**SF5. [R2 Should-Fix] 'Ambiguity' broad usage creates tension with NLP community standards.**\nIncompleteness, authorization scope, and conditional precedence are not strictly linguistic ambiguity. §3 acknowledges this but argues only functional equivalence. Action: Reference underspecification/vagueness distinction (Poesio & Artstein, 2005); systematically argue why the merger is informative for agent safety research.\n\n**SF6. [R1 Should-Fix] Temperature=0 limits variance decomposition interpretation.**\nAll experiments use deterministic decoding; real deployments use temperature>0. The Limitations mention adds direction but the variance decomposition section itself needs explicit acknowledgment that it captures only cross-model and cross-clause variance, not within-model stochastic variance.\n\n**SF7. [R2 Should-Fix] Taxonomy 11→6 selection criteria need transparent reporting.**\nSome exclusions attributed to \"RE attestation\" (criterion 1) are likely driven by minimal-pair construction difficulty (criterion 2). Honest reporting of practical constraints would strengthen credibility.\n\n**SF8. [consensus] Abstract information density is excessive.**\n~190 words with 8+ quantitative figures. Core message diluted. Reduce to 2-3 key numbers; move rest to body sections.\n\n### Minor (6 issues)\n\n- M1. \"Confound-free\" terminology used inconsistently: Abstract \"confound-free types\" (excluding incompleteness) vs. Limitations \"+34.0pp confound-free\" (after perturbation controls).\n- M2. Table 2 footnote markers (†, ‡) are small and easily missed.\n- M3. \"Confound-free types\" first appears in §5.1 without inline definition.\n- M4. Replication results (Gemini, LLaMA) deserve brief main text mention, not just appendix.\n- M5. Contrast between violation severity κ=0.653 and failure mechanism κ=0.15 is itself a finding worth main text discussion.\n- M6. Pages 5-6 are continuous text without display items; consider summary table for key statistics.\n\n---\n\n## Reviewer Consensus\n\nBoth reviewers independently rated **3.5 (Borderline Conference)** and agree on:\n- [AGREE] The matched-pair causal design is methodologically sound and rare in agent safety literature\n- [AGREE] Type-mechanism dissociation is directionally interesting but its reliability evidence (human κ=0.15) is a serious concern\n- [AGREE] Authorization scope is a construct outlier requiring special treatment\n- [AGREE] Cross-domain ρ=0.26 limits taxonomy generalizability claims\n- [AGREE] Abstract is information-overloaded\n- [AGREE] Confound handling for incompleteness is transparent but insufficient\n- [AGREE] The paper's practical message (clause-level > type-level auditing) is well-supported\n\n## Reviewer Divergence\n\n- **\"Nocuous\" terminology**: R2 rates Must-Fix (semantic inversion undermines title credibility); R1 rates Minor (acknowledges ancient usage but sees it as stylistic choice). **Director resolution**: Should-Fix — the semantic extension is defensible but underdeveloped.\n- **SESOI ±15pp**: R1 rates Must-Fix (safety domain demands smaller SESOI); R2 does not raise independently. **Director resolution**: Must-Fix — the C2 equivalence structure is a core claim that depends entirely on this threshold.\n\n---\n\n## Questions for Authors\n\nQ1. What is Cramér's V(type→mechanism) computed from human annotations? Even with low κ=0.15, this provides a floor estimate for the true dissociation strength.\n\nQ2. In unambiguous conditions, what is agents' \"false positive\" ambiguity awareness rate? If agents rarely discuss ambiguity in either condition, the 4.6% may reflect general low metacognition rather than ambiguity-specific neglect.\n\nQ3. Is cross-provider ICC feasible from existing data across all 7 models? If cross-provider ICC is substantially lower than 0.919, what does this imply for generalization claims?\n\nQ4. For authorization scope (κ=0.385), at what agreement threshold would the type be excluded from the taxonomy rather than treated as a \"difficult construct\"?\n\nQ5. Could a control condition for incompleteness be designed — adding equal-length non-disambiguating policy text — without requiring new experiments?\n\n---\n\n## Missing References\n\n1. **Poesio & Artstein (2005)** — \"Annotating (Anaphoric) Ambiguity.\" Relevant to §3's discussion of ambiguity vs. underspecification vs. vagueness.\n2. **Zhou et al. (2023)** — \"Instruction-Following Evaluation for Large Language Models\" (IFEval). Establishes LLM rule-following baselines relevant to policy compliance.\n3. **Bai et al. (2022)** — \"Constitutional AI.\" Relevant context for the 77% permissive bias finding in §6.3.\n\n---\n\n## External Review\n\n**Status**: Not requested (project not configured for external review).\n\n---\n\n## Visual Layout Check (non-scoring)\n\nVisual check completed (3 warnings, 16 info items, 0 critical):\n- ⚠️ **Pages 5-6**: Continuous 2 pages of pure text (Methods 4.3-4.6 + Results 5.1-5.2) without display items. Dense quantitative results in prose are reviewer-unfriendly. Consider a small summary table.\n- ⚠️ **Page 8**: Extremely crowded — Figures 2, 3, 4 + Discussion opening + Conclusion opening all compressed into one page. Axis labels and heatmap annotations at readability edge when printed.\n- ⚠️ **Page 23**: Final appendix page ~85% blank, giving \"unfinished\" impression.\n- ✅ Main text exactly 8 pages (EMNLP compliant)\n- ✅ Limitations on p9, ~8 lines covering 3 points (compliant)\n- ✅ Double-blind formatting correct (\"Anonymous ACL submission\")\n- ✅ No margin overflows, LaTeX errors, or unresolved references\n- ✅ ACL template (acl.sty) correctly applied\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 (Borderline Conference)**\n**Confidence: 4/5**\n\nThis paper makes a methodologically rigorous contribution to an important and timely problem. The matched-pair causal design is rare in agent safety literature, and the experimental execution (5 models, 2,997 episodes, 15-page appendix) demonstrates high scientific standards. The practical conclusion — clause-level policy auditing over type-level risk screening — is well-supported.\n\nHowever, four issues collectively prevent a confident Conference recommendation:\n\n1. **Type-mechanism dissociation reliability** (MF1): The second contribution rests on LLM-coded labels with human κ=0.15. This is the paper's most novel claim but also its weakest evidential link.\n\n2. **SESOI justification** (MF2): The C2 type ordering depends on ±15pp equivalence, which is insufficiently grounded for safety applications. At ±10pp, the equivalence structure largely dissolves.\n\n3. **Incompleteness confound** (MF3): Token count is an inadequate proxy for information content. The highest-risk type's effect size remains partially confounded.\n\n4. **Cross-provider reproducibility** (MF4): ICC evidence is limited to one provider family; \"cross-model consistency\" claims outpace the evidence.\n\n**Current recommendation**: Findings-acceptable (3.0-3.5). Conference-borderline, conditional on addressing MF1-MF4. If MF1 is resolved by downgrading the dissociation to exploratory finding and MF3 by using 31.0pp as the headline effect, the paper reaches solid Findings. Full Conference acceptance additionally requires MF2 (principled SESOI) and MF4 (cross-provider reproducibility).\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Motivating example (scopal ambiguity in return policy) is effective but overly obvious. A subtler example would better demonstrate taxonomy diagnostic value.\n- Contribution (2) should carry a reliability caveat referencing §6's LLM-coding limitation.\n- \"We show that LLM agents invert this pattern, exhibiting convergent rather than divergent misinterpretation\" — this single sentence is insufficient foundation for the title's \"nocuous\" claim. Needs expansion.\n\n### §3 Taxonomy\n- \"Scope of 'ambiguity'\" paragraph argues functional equivalence only. For CL/NLP audience, engage with the ambiguity/underspecification/vagueness distinction explicitly.\n- Li et al. 11→6 mapping should honestly attribute practical construction constraints where applicable, not frame all exclusions as conceptual criteria.\n- §3 \"design hypothesis\" framing for the two-layer structure is appropriate given C3's inconclusive status.\n\n### §4 Method\n- Cross-judge design asymmetry (3 models judged by GPT-5.4 vs 2 by GPT-4.1) means per-model absolute rates are not directly comparable across groups. The matched-pair Δpp cancels this, but should be stated explicitly.\n- §4.6 SESOI: \"pragmatic default\" is honest but insufficient for a paper claiming safety implications.\n- Human validation (n=100): Sufficient for overall pipeline validation; insufficient for per-type reliability claims (n=32-34 per type with CIs spanning ±20pp).\n\n### §5 Results\n- §5.1: \"confound-free types\" needs inline definition on first use.\n- Variance decomposition is a key finding but currently buried in dense paragraph. A small inline figure or callout would help. Temperature=0 limitation should be noted here.\n- C3 (layer effect) correctly reported as inconclusive. This honesty is commendable.\n\n### §6 Error Analysis\n- The caveat \"as classified by LLM coders; human mechanism agreement is lower, κ=0.15\" appears mid-sentence in parenthetical. Given this is the evidential basis for Contribution 2, it warrants a full paragraph discussing implications for the dissociation claim.\n- Disambiguation neglect (4.6%): Needs unambiguous-condition baseline to distinguish ambiguity-specific neglect from general low metacognition.\n- Systematic nocuity: The permissive bias finding (77%) would benefit from connection to Constitutional AI / RLHF literature on safety-helpfulness tradeoffs.\n\n### §7 Discussion\n- Ecological validity paragraph handles the effect gap but the three compression factors should be in main text.\n- ρ=0.26 cross-domain type ranking correlation must appear here, not only in appendix.\n- Authorization scope outlier treatment is understated — this construct drives multiple anomalies.\n\n### §8 Conclusion\n- \"In customer-service domains under controlled conditions\" — appropriate scoping.\n- \"Clause-level policy auditing is the actionable intervention\" — this prescription depends on the dissociation finding, which has reliability concerns (MF1).\n\n### Limitations\n- Appropriately concise. Should add one sentence acknowledging type-mechanism dissociation's dependence on LLM coding labels.",
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 borderline conference",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — Round 26 (Fresh)\n\n**Paper**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n**Venue**: EMNLP 2026 via ARR May cycle\n**Reviewers**: 2 (R1: 方法严谨性, R2: 新颖性与完整性)\n**Date**: 2026-05-23\n\n---\n\n## Summary\n\nThis paper uses a matched-pair causal design to study how policy ambiguity affects safety violations in LLM agents. Using 300 clause pairs across a six-type taxonomy on τ²-bench with five models (2,997 episodes), the authors show ambiguous clauses increase violations by +34.0pp (+31.0pp confound-free). The core finding is a \"type-mechanism dissociation\": ambiguity type predicts failure mechanism (Cramér's V=0.45) but not violation rate (V=0.14). Error analysis reveals \"disambiguation neglect\" (4.6% awareness) and \"systematic nocuity\" (77% permissive bias, convergent errors).\n\n---\n\n## Strengths\n\n**S1. Matched-pair causal design is methodologically strong.** Rare in agent safety literature. Perturbation controls (Δ_perturb = -0.67pp, CI [-8.0, 6.67]) convincingly exclude surface-level rewriting as alternative explanation. 300 clause pairs × 5 models with 96% initial annotator agreement provides solid internal validity.\n\n**S2. Comprehensive statistical analysis and transparency.** TOST equivalence testing across 7 margins, bootstrap cluster analysis, ICC variance decomposition, cross-benchmark replication (SOPBench), cross-architecture replication (Gemini, LLaMA), and 15 pages of appendices addressing nearly all foreseeable reviewer questions.\n\n**S3. Type-mechanism dissociation has practical value.** Even with reliability caveats, the directional finding that type predicts mechanism more strongly than severity is actionable: clause-level auditing > type-level risk classification.\n\n**S4. Real-world grounding.** Prevalence audit (24 production documents, 407 clauses, 55–87% ambiguous) establishes practical relevance. SOPBench cross-benchmark replication confirms directional consistency.\n\n**S5. Confound handling is honest.** Incompleteness information-addition confound is explicitly identified, separately analyzed (Appendix F), and the confound-free effect (31.0pp) is reported alongside the full effect (34.0pp).\n\n---\n\n## Weaknesses\n\n### Must-Fix (4 issues — affect acceptance decision)\n\n**MF1. [consensus, critical] Type-mechanism dissociation (Contribution 2) reliability is insufficiently supported.**\n- Location: §6.1, Appendix AE\n- The core evidence for V=0.45 rests entirely on LLM-coded failure mechanism labels, while human annotation agreement is κ=0.15 (near chance). The paper acknowledges this is an \"upper bound\" (§6.1) but still presents it as a headline contribution and abstract number. LLM coding consistency may reflect systematic classification preferences rather than genuine type-mechanism association.\n- R2 rated this Must-Fix; R1's Soundness 3/5 partly reflects this concern.\n- **Action required**: (a) Prominently discuss κ=0.15 in main text §6 (not just parenthetical); (b) consider downgrading type-mechanism dissociation from \"contribution\" to \"exploratory finding\"; (c) add explicit caveat to abstract V=0.45 figure; (d) report V computed from human annotations as a floor estimate.\n\n**MF2. [R1 Must-Fix] SESOI ±15pp lacks principled domain justification.**\n- Location: §4.6, Table 3\n- The C2 partial ordering (type equivalence structure) depends entirely on TOST equivalence at ±15pp. For safety-critical applications, 14.9pp additional violation rate at scale could mean hundreds of unsafe actions. At ±10pp, only 3/15 type pairs reach equivalence. The paper acknowledges \"pragmatic default\" but this is insufficient for safety claims.\n- **Action required**: Provide safety-domain-grounded justification for ±15pp; or adopt ±10pp as primary analysis with ±15pp as sensitivity; or explicitly scope C2 claims to the chosen margin.\n\n**MF3. [R1 Must-Fix] Incompleteness confound control is methodologically insufficient.**\n- Location: §4.5, Appendix F\n- Token count as a proxy for information content has a fundamental flaw: a short phrase like \"non-refundable\" carries high policy information in few tokens, while lengthy clarifications may add minimal semantic content. The regression assumes linear token-count mediation, but the actual confound concerns information *type* (policy-relevant vs. disambiguating), not *quantity*.\n- **Action required**: (a) Add a control condition with equal-length non-disambiguating policy text to directly isolate the information-addition effect; or (b) exclude incompleteness from primary causal claims and treat as observational evidence, using confound-free 31.0pp as the headline effect.\n\n**MF4. [R1 Must-Fix] Cross-provider reproducibility evidence is insufficient.**\n- Location: §4.4, Appendix AC/E\n- ICC(1)=0.919 is computed only within the OpenAI family (GPT-5.4, GPT-4.1). The Gemini/LLaMA replication (Appendix E) shows directional consistency but no ICC. Different providers may have qualitatively different safety training; within-family ICC cannot capture this dimension.\n- **Action required**: Compute cross-provider ICC or equivalent metric across all 7 models; or explicitly limit reproducibility claims to within-family consistency and discuss cross-provider limitations.\n\n### Should-Fix (8 issues — affect scoring)\n\n**SF1. [R2 Must-Fix → consensus Should-Fix] \"Nocuous\" terminology semantic inversion needs stronger justification.**\nBerry et al. (2004) define nocuous = divergent interpretation; this paper finds convergent error. The title uses \"nocuous\" without qualification. R2 elevated to Must-Fix; R1 noted as Minor. Consensus at Should-Fix: the semantic extension is defensible but needs explicit justification in Introduction (not just one sentence referencing §6), or terminology revision.\n\n**SF2. [consensus] Authorization scope is a construct outlier distorting headline statistics.**\nκ=0.385 (lowest), 52pp cross-model range (largest), drives C4 interaction, causes ρ=0.09 cross-judge-group discordance. One sentence in Discussion is insufficient. Action: Present five-type results as primary; auth scope as supplementary low-confidence construct.\n\n**SF3. [consensus] Synthetic-to-natural effect gap (34pp vs 12.7pp) and cross-domain ρ=0.26 need main text discussion.**\nThe three-factor explanation (measurement grain, baseline compression, interaction depth) is reasonable but only in appendix. ρ=0.26 (effectively zero correlation for type rankings across domains) is only in Appendix Z but directly impacts taxonomy diagnostic claims. Action: Move both to Discussion §7; Conclusion should state type-level findings are domain-contingent.\n\n**SF4. [R2 Should-Fix] Incremental contribution over DRIP-R (2026) is under-argued.**\nDRIP-R already establishes \"ambiguity hurts agents\" on 400 scenarios × 5 RE types. The paper lists three differentiators but doesn't argue why the causal → correlational upgrade changes conclusions. Action: Add direct comparison paragraph in §2 or §7 specifying which confounds DRIP-R's correlational design leaves unaddressed.\n\n**SF5. [R2 Should-Fix] 'Ambiguity' broad usage creates tension with NLP community standards.**\nIncompleteness, authorization scope, and conditional precedence are not strictly linguistic ambiguity. §3 acknowledges this but argues only functional equivalence. Action: Reference underspecification/vagueness distinction (Poesio & Artstein, 2005); systematically argue why the merger is informative for agent safety research.\n\n**SF6. [R1 Should-Fix] Temperature=0 limits variance decomposition interpretation.**\nAll experiments use deterministic decoding; real deployments use temperature>0. The Limitations mention adds direction but the variance decomposition section itself needs explicit acknowledgment that it captures only cross-model and cross-clause variance, not within-model stochastic variance.\n\n**SF7. [R2 Should-Fix] Taxonomy 11→6 selection criteria need transparent reporting.**\nSome exclusions attributed to \"RE attestation\" (criterion 1) are likely driven by minimal-pair construction difficulty (criterion 2). Honest reporting of practical constraints would strengthen credibility.\n\n**SF8. [consensus] Abstract information density is excessive.**\n~190 words with 8+ quantitative figures. Core message diluted. Reduce to 2-3 key numbers; move rest to body sections.\n\n### Minor (6 issues)\n\n- M1. \"Confound-free\" terminology used inconsistently: Abstract \"confound-free types\" (excluding incompleteness) vs. Limitations \"+34.0pp confound-free\" (after perturbation controls).\n- M2. Table 2 footnote markers (†, ‡) are small and easily missed.\n- M3. \"Confound-free types\" first appears in §5.1 without inline definition.\n- M4. Replication results (Gemini, LLaMA) deserve brief main text mention, not just appendix.\n- M5. Contrast between violation severity κ=0.653 and failure mechanism κ=0.15 is itself a finding worth main text discussion.\n- M6. Pages 5-6 are continuous text without display items; consider summary table for key statistics.\n\n---\n\n## Reviewer Consensus\n\nBoth reviewers independently rated **3.5 (Borderline Conference)** and agree on:\n- [AGREE] The matched-pair causal design is methodologically sound and rare in agent safety literature\n- [AGREE] Type-mechanism dissociation is directionally interesting but its reliability evidence (human κ=0.15) is a serious concern\n- [AGREE] Authorization scope is a construct outlier requiring special treatment\n- [AGREE] Cross-domain ρ=0.26 limits taxonomy generalizability claims\n- [AGREE] Abstract is information-overloaded\n- [AGREE] Confound handling for incompleteness is transparent but insufficient\n- [AGREE] The paper's practical message (clause-level > type-level auditing) is well-supported\n\n## Reviewer Divergence\n\n- **\"Nocuous\" terminology**: R2 rates Must-Fix (semantic inversion undermines title credibility); R1 rates Minor (acknowledges ancient usage but sees it as stylistic choice). **Director resolution**: Should-Fix — the semantic extension is defensible but underdeveloped.\n- **SESOI ±15pp**: R1 rates Must-Fix (safety domain demands smaller SESOI); R2 does not raise independently. **Director resolution**: Must-Fix — the C2 equivalence structure is a core claim that depends entirely on this threshold.\n\n---\n\n## Questions for Authors\n\nQ1. What is Cramér's V(type→mechanism) computed from human annotations? Even with low κ=0.15, this provides a floor estimate for the true dissociation strength.\n\nQ2. In unambiguous conditions, what is agents' \"false positive\" ambiguity awareness rate? If agents rarely discuss ambiguity in either condition, the 4.6% may reflect general low metacognition rather than ambiguity-specific neglect.\n\nQ3. Is cross-provider ICC feasible from existing data across all 7 models? If cross-provider ICC is substantially lower than 0.919, what does this imply for generalization claims?\n\nQ4. For authorization scope (κ=0.385), at what agreement threshold would the type be excluded from the taxonomy rather than treated as a \"difficult construct\"?\n\nQ5. Could a control condition for incompleteness be designed — adding equal-length non-disambiguating policy text — without requiring new experiments?\n\n---\n\n## Missing References\n\n1. **Poesio & Artstein (2005)** — \"Annotating (Anaphoric) Ambiguity.\" Relevant to §3's discussion of ambiguity vs. underspecification vs. vagueness.\n2. **Zhou et al. (2023)** — \"Instruction-Following Evaluation for Large Language Models\" (IFEval). Establishes LLM rule-following baselines relevant to policy compliance.\n3. **Bai et al. (2022)** — \"Constitutional AI.\" Relevant context for the 77% permissive bias finding in §6.3.\n\n---\n\n## External Review\n\n**Status**: Not requested (project not configured for external review).\n\n---\n\n## Visual Layout Check (non-scoring)\n\nVisual check completed (3 warnings, 16 info items, 0 critical):\n- ⚠️ **Pages 5-6**: Continuous 2 pages of pure text (Methods 4.3-4.6 + Results 5.1-5.2) without display items. Dense quantitative results in prose are reviewer-unfriendly. Consider a small summary table.\n- ⚠️ **Page 8**: Extremely crowded — Figures 2, 3, 4 + Discussion opening + Conclusion opening all compressed into one page. Axis labels and heatmap annotations at readability edge when printed.\n- ⚠️ **Page 23**: Final appendix page ~85% blank, giving \"unfinished\" impression.\n- ✅ Main text exactly 8 pages (EMNLP compliant)\n- ✅ Limitations on p9, ~8 lines covering 3 points (compliant)\n- ✅ Double-blind formatting correct (\"Anonymous ACL submission\")\n- ✅ No margin overflows, LaTeX errors, or unresolved references\n- ✅ ACL template (acl.sty) correctly applied\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 (Borderline Conference)**\n**Confidence: 4/5**\n\nThis paper makes a methodologically rigorous contribution to an important and timely problem. The matched-pair causal design is rare in agent safety literature, and the experimental execution (5 models, 2,997 episodes, 15-page appendix) demonstrates high scientific standards. The practical conclusion — clause-level policy auditing over type-level risk screening — is well-supported.\n\nHowever, four issues collectively prevent a confident Conference recommendation:\n\n1. **Type-mechanism dissociation reliability** (MF1): The second contribution rests on LLM-coded labels with human κ=0.15. This is the paper's most novel claim but also its weakest evidential link.\n\n2. **SESOI justification** (MF2): The C2 type ordering depends on ±15pp equivalence, which is insufficiently grounded for safety applications. At ±10pp, the equivalence structure largely dissolves.\n\n3. **Incompleteness confound** (MF3): Token count is an inadequate proxy for information content. The highest-risk type's effect size remains partially confounded.\n\n4. **Cross-provider reproducibility** (MF4): ICC evidence is limited to one provider family; \"cross-model consistency\" claims outpace the evidence.\n\n**Current recommendation**: Findings-acceptable (3.0-3.5). Conference-borderline, conditional on addressing MF1-MF4. If MF1 is resolved by downgrading the dissociation to exploratory finding and MF3 by using 31.0pp as the headline effect, the paper reaches solid Findings. Full Conference acceptance additionally requires MF2 (principled SESOI) and MF4 (cross-provider reproducibility).\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Motivating example (scopal ambiguity in return policy) is effective but overly obvious. A subtler example would better demonstrate taxonomy diagnostic value.\n- Contribution (2) should carry a reliability caveat referencing §6's LLM-coding limitation.\n- \"We show that LLM agents invert this pattern, exhibiting convergent rather than divergent misinterpretation\" — this single sentence is insufficient foundation for the title's \"nocuous\" claim. Needs expansion.\n\n### §3 Taxonomy\n- \"Scope of 'ambiguity'\" paragraph argues functional equivalence only. For CL/NLP audience, engage with the ambiguity/underspecification/vagueness distinction explicitly.\n- Li et al. 11→6 mapping should honestly attribute practical construction constraints where applicable, not frame all exclusions as conceptual criteria.\n- §3 \"design hypothesis\" framing for the two-layer structure is appropriate given C3's inconclusive status.\n\n### §4 Method\n- Cross-judge design asymmetry (3 models judged by GPT-5.4 vs 2 by GPT-4.1) means per-model absolute rates are not directly comparable across groups. The matched-pair Δpp cancels this, but should be stated explicitly.\n- §4.6 SESOI: \"pragmatic default\" is honest but insufficient for a paper claiming safety implications.\n- Human validation (n=100): Sufficient for overall pipeline validation; insufficient for per-type reliability claims (n=32-34 per type with CIs spanning ±20pp).\n\n### §5 Results\n- §5.1: \"confound-free types\" needs inline definition on first use.\n- Variance decomposition is a key finding but currently buried in dense paragraph. A small inline figure or callout would help. Temperature=0 limitation should be noted here.\n- C3 (layer effect) correctly reported as inconclusive. This honesty is commendable.\n\n### §6 Error Analysis\n- The caveat \"as classified by LLM coders; human mechanism agreement is lower, κ=0.15\" appears mid-sentence in parenthetical. Given this is the evidential basis for Contribution 2, it warrants a full paragraph discussing implications for the dissociation claim.\n- Disambiguation neglect (4.6%): Needs unambiguous-condition baseline to distinguish ambiguity-specific neglect from general low metacognition.\n- Systematic nocuity: The permissive bias finding (77%) would benefit from connection to Constitutional AI / RLHF literature on safety-helpfulness tradeoffs.\n\n### §7 Discussion\n- Ecological validity paragraph handles the effect gap but the three compression factors should be in main text.\n- ρ=0.26 cross-domain type ranking correlation must appear here, not only in appendix.\n- Authorization scope outlier treatment is understated — this construct drives multiple anomalies.\n\n### §8 Conclusion\n- \"In customer-service domains under controlled conditions\" — appropriate scoping.\n- \"Clause-level policy auditing is the actionable intervention\" — this prescription depends on the dissociation finding, which has reliability concerns (MF1).\n\n### Limitations\n- Appropriately concise. Should add one sentence acknowledging type-mechanism dissociation's dependence on LLM coding labels.",
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 borderline conference",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 2302 · 2026-05-23T11:59:37.944999+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4069
}
```

</details>

---


### Assistant

_source line 2303 · 2026-05-23T11:59:50.032926+00:00_

审稿报告已投递至 Research Director。

---

**Round 26 审稿完成，总结如下：**

**评分**：3.5 / 5（Borderline Conference），两位 Reviewer 独立一致

**4 个 Must-Fix**：
1. **Type-mechanism dissociation 可靠性**：核心贡献 V=0.45 完全依赖 LLM 编码标签，人工 κ=0.15 接近随机。建议降级为 exploratory finding
2. **SESOI ±15pp 缺乏安全领域论证**：C2 类型等价结构在 ±10pp 时大部分瓦解
3. **Incompleteness confound 控制不足**：token count 无法替代信息类型的控制
4. **跨 provider 可复现性不足**：ICC=0.919 仅 OpenAI family，缺跨 provider 指标

**8 个 Should-Fix**：nocuous 术语延伸、auth scope construct outlier、效应差距正文讨论、DRIP-R 增量论证、ambiguity 广义使用、temperature=0 限制、taxonomy 选择透明度、abstract 信息密度

**结论**：方法论严谨，当前版本适合 Findings。Conference 接收需解决 MF1-MF4。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 219

## Round 219

6 recorded events


### User

_source line 2304 · 2026-05-23T11:59:50.036611+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix

**[AGREE] R2-N1: Type-mechanism dissociation 核心证据可靠性不足**

同意这是一个实质性问题。论文在 §6.1 明确承认 "absolute NMI should be interpreted as an upper bound on the true type-mechanism association" 以及 "following failure mode patterns should therefore be interpreted as consistent LLM categorization tendencies rather than ground-truth mechanism assignments"，但 abstract 和 Discussion (§7) 仍将 Cramér's V = 0.45 vs. 0.14 作为核心贡献呈现，措辞上的落差构成 overclaim。

补充我的发现：failure mechanism 的 human agreement κ=0.15 与 violation severity 的 κ=0.653 (Appendix AE) 形成鲜明对比——同一批标注者对 "是否违规" 有 substantial agreement，但对 "如何违规" 几乎是随机的。这说明 failure mechanism taxonomy 本身的 construct validity 有问题，LLM 编码器的高一致性更可能反映 LLM 的系统性分类偏好（如将 incompleteness 一律归为 "gap-filling"）而非真实的因果机制关联。

建议：同意 R2 方案——将 type-mechanism dissociation 降级为 exploratory finding，abstract 中添加 "LLM-coded" 限定词，并在正文增加对 LLM 编码偏好 vs. 真实机制关联的分析。

**[REBUT] R2-N2: "Nocuous" 术语语义反转——应降级为 Should-Fix**

R2 的观察是准确的：Berry et al. (2004) 定义 nocuous ambiguity 为 divergent interpretation（不同 stakeholder 产生不同理解），而本文发现的是 convergent error（多个模型收敛到相同错误解读）。但我认为这不构成 Must-Fix，理由如下：

1. 论文在 §6.3 明确处理了这一语义延伸："We adopt 'nocuous' from Berry et al. (2004), but inverted: our agents exhibit convergent rather than divergent errors." 这不是疏忽，而是有意识的术语再定义。

2. Berry et al. 的核心含义是 "harmful ambiguity"（与 innocuous ambiguity 对立），divergent interpretation 是其在 RE 语境下的具体表现形式。论文将 "nocuous" 的语义焦点从 "divergent" 移至 "harmful" 并提供了新的具体表现形式（convergent error），这是一个合理的术语演化。

3. 标题的功能是引起注意和传达核心 message（"policy ambiguity is harmful"），§6.3 的详细论证足以为熟悉 Berry et al. 的读者消解歧义。

但我同意 Introduction 应更早、更显著地处理这一语义延伸——目前首次讨论在 §6.3 太晚了。建议在 §1 (Introduction) 引用 Berry et al. 时就明确说明 convergent vs. divergent 的区别。作为 Should-Fix 而非 Must-Fix 更恰当。

---

### Should-Fix

**[AGREE] R2-W1: 'Ambiguity' 广义使用与 NLP 标准定义的张力**

论文在 §3 (p.4) 已用 "Scope of 'ambiguity'" 段落处理了这一问题，承认 "strictly, neither constitutes linguistic ambiguity"。但 R2 的建议有两点价值：(1) 引用 Poesio & Artstein (2005) 关于 ambiguity vs. underspecification 的经典区分，会显著增强这段论证的学术锚定；(2) 在标题或 Introduction 中增加 "policy specification" 限定词（如 "policy specification ambiguity"），可以在不改变核心术语的前提下缩小语义范围。

我不建议改用 "policy underspecification" 作为主术语——这会丢失 lexical ambiguity 和 scopal ambiguity 这两种确实属于 linguistic ambiguity 的类型。但引用 Poesio & Artstein 并增加限定词是必要的。

**[AGREE] R2-W2: 跨领域 ρ=0.26 需要在正文报告**

这与我的 W2（合成-自然效应差距 34pp vs 12.7pp 需正文讨论）互补。Per-type violation rate ranking 跨 retail 和 airline 两个领域的 Spearman ρ=0.26（Appendix Z）意味着 type-level findings 高度 domain-contingent。论文 Conclusion (§8) 声称 taxonomy 可用于 "motivating clause-level policy auditing over type-level risk scorecards"，但如果类型排序因领域而异，这个应用建议的基础被削弱。Conclusion 应明确添加 domain-contingency 限定。

**[REBUT] R2-W3: 相对 DRIP-R 增量贡献论证不够有力**

我不完全同意。论文在 §2 (p.3) 明确列出三个差异：(1) 因果设计 vs. 相关性；(2) 安全违规 vs. 决策质量；(3) 双层 taxonomy 含语言层类型 + model×type interaction 量化。这些差异是实质性的，不仅仅是复制：

- DRIP-R 的 400 scenarios × 5 RE types 度量的是 "decision quality"，本文度量的是 "safety violations"——这是不同的 outcome variable，直接关系到 AI safety 领域的关切。
- DRIP-R 没有 matched-pair 设计——它比较的是不同 scenario 的歧义程度与质量的相关性，无法排除 scenario-level confounds。本文的 matched-pair 设计在同一 clause 上操控歧义，因果推断的内部效度显著更高。
- Type-mechanism dissociation 和 convergent nocuity 是 DRIP-R 未报告的新现象。

但 R2 的隐含问题——"causal design 是否*改变*了 DRIP-R 的结论"——值得正文回答。如果答案是 "方向一致但效应量和机制理解更精确"，论文应在 §2 或 §7 明确说明。

**[AGREE] R2-W4: Taxonomy 11→6 选择标准论证不够系统**

Table 12 (Appendix M) 给出了 Li et al. (2024b) 11 类型到本文 6 类型的映射，选择标准列出三条：(1) RE attestation, (2) minimal-pair constructibility, (3) mutual exclusivity。但 R2 正确指出，ellipsis 的排除理由写 "not attested in RE" 而排除的真实原因可能包含 minimal-pair 构造困难——如果一种歧义类型无法构造最小对，排除它是合理的方法论决策，但应透明陈述为实际约束而非仅引用文献缺失。

**[AGREE] R2-W5: Abstract 信息密度过高**

约 190 词包含 8+ 定量数字（31.0pp, 34.0pp, 12.7pp, 0.4%, V=0.45, 0.14, 4.6%, 41.5%, 77%）。虽然在 EMNLP 200 词限制内，但认知负荷过重。建议保留 3-4 个最核心数字（主效应量、confound-free 效应、SOPBench 复制、type-mechanism V），其余移入 Introduction。

---

### Minor

**[AGREE] R2-M1**: Introduction motivating example（"items may be returned within 30 days"）的歧义确实过于明显——真实政策歧义往往更隐蔽。但作为一个直观引入尚可接受。

**[AGREE] R2-M2**: Table 2 数字密度极高，与我的同一观察一致。

**[AGREE] R2-M3**: "Confound-free types" 定义不清，与我的 Minor issue（论文内两种用法不一致）完全吻合。

**[REBUT] R2-M4**: 复制结果（Gemini, LLAMA）仅在 Appendix——这是 8 页正文限制下的合理取舍。Appendix E 的存在本身说明作者做了跨架构验证；在正文 §5 或 §7 添加一句指引即可，无需在正文展开。

**[AGREE] R2-M5**: Violation severity κ=0.653 vs failure mechanism κ=0.15 对比确实值得正文讨论，直接支撑 R2-N1 的论点。这个对比可以用一句话在 §6.1 说明。

---

### Missing References

**[AGREE]** Poesio & Artstein (2005) 关于 ambiguity vs. underspecification 的区分——直接相关，应在 §3 引用。

**[REBUT]** Zhou et al. (2023) IFEval——衡量的是 instruction-following 准确率，与 policy ambiguity → safety violation 的研究问题相关性有限。论文已引用了更直接相关的 agent safety benchmarks（τ²-bench, SOPBench, SafeAgentBench 等）。除非 R2 能指出 IFEval 的具体维度与本文方法的直接联系，否则非必要引用。

**[AGREE]** Bai et al. (2022) Constitutional AI——permissive bias（77% 宽松偏向）是本文核心发现之一，引用 RLHF/Constitutional AI 的安全训练框架可以为 "为什么模型倾向宽松解读" 提供机制解释。建议在 §6.3 或 §7 引用。

**[AGREE]** Hu et al. (2023) / Ruis et al. (2023)——R2 也确认已在 §2 引用。

---

### 综合评估

R2 的审稿抓住了两个我未充分关注的重要问题：(1) failure mechanism 的 human agreement 极低（κ=0.15）对 type-mechanism dissociation claim 的威胁——这与我的 N3（ICC 仅限 OpenAI family）互补，共同指向该贡献的证据基础薄弱；(2) "nocuous" 术语的语义反转——虽然我认为应降为 Should-Fix，但确实需要在 Introduction 更早处理。

R2 对 DRIP-R 增量贡献的质疑（W3）我认为部分不成立——因果设计是实质性方法论进步，不应被简化为 "重复已知结论"。但论文确实应更明确地回答 "causal design 改变了什么"。

两位 Reviewer 的共识区域：type-mechanism dissociation 证据不足（R1 通过 construct validity 路径、R2 通过 human agreement 路径）、"confound-free" 术语不清、abstract 过载、authorization scope 的特殊性。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。

关键判断总结：

- **R2-N1 (type-mechanism dissociation reliability)**: [AGREE]——failure mechanism human κ=0.15 与 violation severity κ=0.653 的对比直接质疑了 V=0.45 这个核心数字的可靠性，应降级为 exploratory finding
- **R2-N2 ("nocuous" 语义反转)**: [REBUT]——§6.3 已有意识处理了 Berry et al. 的语义延伸，但应在 Introduction 更早说明；建议降为 Should-Fix
- **R2-W1-W5**: 大部分 [AGREE]，仅 W3 (DRIP-R 增量) 部分 [REBUT]——因果设计是实质性方法论进步，不应等同于复制
- **两位 Reviewer 的共识区域**: type-mechanism dissociation 证据基础薄弱、"confound-free" 术语不一致、abstract 信息过载、authorization scope 异常

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 回应

**[AGREE with nuance] R1-N1: SESOI ±15pp 论证不足**

同意 ±15pp 对安全领域偏宽松，R1 关于 "14.9pp 在规模化部署中意味数百次不安全行为" 的论证有力。Table 3 的敏感性分析确实显示 ±10pp 时仅 3/7 margins 达到等价性，这是一个实质性的 robustness 问题。

但我**不同意** R1 称 "Type-mechanism dissociation claim (C2) 完全依赖 TOST 等价性" 这一判断。C2 的核心证据是 Cramér's V 对比：type 预测 failure mechanism 的 V = 0.45 vs. 预测 violation rate 的 V = 0.14（§5.2, p6；§6.1, p7）。V = 0.14 是直接从 type × violation rate 的列联表计算的，不依赖任何 TOST 阈值。TOST 用于建立 "types form an equivalence cluster in violation rate"——这是 C2 的辅助论据（支撑 "type 不预测 severity" 这半），而非核心证据。即使将 SESOI 收紧到 ±10pp，V = 0.14 仍然成立，dissociation 的方向性结论（type 更预测 mechanism 而非 rate）不会改变。

**结论**：SESOI 论证确实需要加强（同意 R1），但 C2 不会被推翻（R1 的推论过强）。建议作者以 ±10pp 作为 sensitivity check 的 primary presentation，同时保留 ±15pp 作为 robustness bound。

---

**[AGREE] R1-N2: Incompleteness 的 information-addition confound 控制不充分**

完全同意。R1 的论证精准：token count 作为 information content 的 proxy 存在根本缺陷。"non-refundable" 这个例子很好地说明了短语的政策信息量与 token 数不成正比。回归的线性假设也是一个有效的方法论批评。

但我要补充：论文实际上已经部分采纳了 R1 建议的第二个选项——incompleteness 已从 "confound-free" 效应量（31.0pp）中排除（§5.1, p6）。问题在于论文仍将 incompleteness 包含在 overall effect（34.0pp）和 taxonomy 中，且 Abstract 以 34.0pp 作为 headline 数字。

**我的建议与 R1 一致**：incompleteness 应从主要因果 claims 中更明确地降权。此外，这与我自己的 W4 一致——合成歧义注入与自然歧义之间的效应差距（34pp vs. SOPBench 12.7pp）需要在正文讨论，而 incompleteness 的 confound 可能是该差距的部分原因。

---

**[REBUT] R1-N3: ICC(1) 仅限 OpenAI family 是重大缺陷**

部分不同意 R1 的严重性判断。

1. **方法论考量**：ICC 本身是一个 within-family nesting metric——它测量的是"同一 family 内不同模型版本对同一刺激的一致性"。跨 provider 计算 ICC 在方法论上是否恰当值得商榷，因为不同 provider 的模型没有共享的 family-level random effect 结构。将 GPT-5.4、Claude Sonnet 4.6、Qwen3-235B 放入同一 ICC 模型，其 variance structure 的假设可能不成立。

2. **互补证据充分**：论文提供了多项跨 provider 一致性证据：
   - 所有 5 个模型都显示显著的 ambiguity effect（Table 2, p7：all p < 10⁻⁴）
   - Kendall's W = 0.396（p = 0.072）用于跨模型 type ranking concordance（§5.2, p6）
   - Appendix E 在 Gemini-2.5-Flash 和 LLAMA-4-Scout 上的复制确认方向一致性
   - Appendix AB (p20) 报告跨 judge 模型排名一致性：GPT-Claude ρ = 0.70, GPT-Gemini = 0.80, Claude-Gemini = 0.70

3. **R1 的建议可操作但非 blocking**："在全部七个模型上计算 ICC 或等效指标"——Kendall's W 本质上已经是这个等效指标。

**结论**：R1 的建议合理（增加跨 provider 的量化一致性指标），但将此定为 Must-Fix/critical 过重。论文已有充分的互补证据表明跨 provider 方向一致性。建议降为 Should-Fix：在 Appendix 中补充全模型 Kendall's W 或 Krippendorff's α 作为跨 provider 一致性的显式指标。

---

### Should-Fix 回应

**[REBUT] R1-W1: 将 Authorization scope 排除为 5 类型 taxonomy**

不同意。Authorization scope 的低 κ（0.385）和高跨模型变异（52pp）反映的是该类型的 **inherent construct difficulty**——authorization boundary 是否被越权本身就是一个语义边界模糊的判断——而非 construct invalidity。将一个"难以可靠标注"的类型从 taxonomy 中移除是方法论上的倒退：如果某种歧义在实践中特别难以诊断，这恰恰是需要被 taxonomy 保留并研究的类型。

论文已经恰当地处理了这一问题：
- §5.2 (p6) 报告 authorization scope 跨模型变异最大
- Appendix G (p14) 报告 per-type human-LLM agreement，authorization scope κ = 0.385
- Appendix O (p15) 报告 Core Analysis Excluding Authorization Scope——效应量保持 robust（Δ = +33.6pp）
- Appendix R (p16) 报告 within-judge-group type rankings 显示 authorization scope 跨 judge 方向一致

更好的做法是：在正文 §5.2 中增加 1-2 句讨论 authorization scope 的 construct difficulty 及其对结论的影响，而非移除它。

---

**[AGREE] R1-W2: 合成 vs 自然歧义效应差距应在正文讨论**

完全同意，且这与我自己的审稿意见高度一致。34pp（合成）vs. 12.7pp（SOPBench, Appendix AA）的差距是一个需要在正文解释的重要发现。论文在 Limitations (p9) 简要提及 "the 34.0pp effect is an upper bound"，但未在 Discussion (§7) 系统讨论这个 ~3x 的效应衰减意味着什么。可能的解释包括：(1) 合成 minimal-pair 的 "clean" 歧义 vs. 自然歧义的 "messy" 表现；(2) SOPBench 的任务结构差异（constraint-level vs. clause-level）；(3) incompleteness confound 对 overall effect 的 inflation。

---

**[AGREE] R1-W3: Temperature=0 限制了 variance decomposition 的解读**

同意。Temperature=0 是控制实验的合理选择（最大化可复现性），但 Appendix AC 的 variance decomposition（ICC(1) = 0.749，25.1% within-cell stochastic variance）在 temperature=0 下的 stochastic component 已经相当大。在实际部署（temperature > 0）中，stochastic variance 会进一步增大，这意味着：(1) between-cell (systematic) 占比会下降；(2) type-level 和 clause-level 的预测力可能减弱。论文应在 Limitations 或 Discussion 中增加 1 句关于 temperature > 0 对结论泛化性的影响。

不过我要补充：这不应被夸大为根本性缺陷。Temperature=0 下观察到的 systematic effects（between-cell 74.9%）足够大，即使 stochastic variance 增加，核心方向性结论（ambiguity increases violations, type predicts mechanism > rate）在合理 temperature 范围内应仍然成立。

---

**[AGREE with nuance] R1-W4: Human validation 样本量不足**

同意 n=100（per-type n ≈ 17）的统计功效有限，authorization scope κ=0.385 的置信区间确实很宽。但我要指出：
1. 100 episodes 的 stratified sample 对 overall validation（violation detection κ = 0.653, Appendix G p14）是足够的——问题仅在 per-type breakdown 上
2. 论文的核心统计推断不依赖人工标注——它基于 LLM 的 cross-judge pipeline（3 个 LLM judges，2,997 episodes）。Human validation 的角色是 calibration check，而非 primary evidence。
3. 扩大人工标注到 per-type 足够功效（如 n ≥ 50/type → 300 total）在 rebuttal 期间是可行的。

---

### Minor 回应

**[AGREE] R1-Minor-1: "Confound-free" 术语不一致**
同意，这个术语在论文中出现时缺乏一致的首次定义。

**[AGREE] R1-Minor-2: "Nocuous" 可能降低可及性**
同意，且这与我自己的 N2（语义反转问题）互补。R1 从可及性角度、我从语义准确性角度指出同一术语的问题，两个维度的批评互相强化。建议作者认真考虑替换这个术语。

**[AGREE] R1-Minor-3: Table 2 脚注标记较小**
同意，纯排版问题。

---

### R1 优势评估的回应

完全同意 R1 识别的 5 项优势。我在自己的审稿报告中也独立识别了因果框架设计（我的 S1）、confound 处理透明度（我的 S3）、type-mechanism dissociation 的实践价值（我的 S2）作为主要优势。两位 reviewer 独立一致肯定这些优势，增强了对这些方面评价的信心。

---

### 综合评估

R1 和我（R2）的 Overall 评分均为 3.5（Borderline Conference），且问题高度互补：
- **R1 聚焦方法论**：SESOI 阈值、confound 控制、ICC 范围、sample size
- **R2 聚焦新颖性与完整性**：与 DRIP-R 的增量贡献、type-mechanism dissociation 的标签可靠性（κ=0.15）、术语问题、跨领域泛化性

关键分歧：
- R1 将 ICC(1) 局限于 OpenAI family 列为 Must-Fix，我认为应为 Should-Fix（互补证据充分）
- R1 建议移除 authorization scope 为 5 类型，我认为保留并讨论更恰当

共识最强的问题：
1. Incompleteness confound（R1-N2, 我 agree）
2. 合成 vs 自然效应差距需正文讨论（R1-W2, 对应我的 W2 area）
3. "Nocuous" 术语问题（R1-Minor-2 + 我的 N2）
4. Type-mechanism dissociation 的证据可靠性需加强（R1-N1 的 TOST 角度 + 我的 N1 的 κ=0.15 角度——两个独立的 attack vector 指向同一贡献的薄弱环节）

**如果作者能充分回应这些共识问题，论文有望提升至 Conference 接收水平（4.0）。**

---

[Reviewer 2 审稿结果]:
逐条回应已提交给 Review Director。总结：

- **R1-N1 (SESOI)**: 部分同意——±15pp 确实偏宽，但反驳 R1 称 C2 "完全依赖 TOST" 的判断，因为 Cramér's V = 0.14 不依赖任何 TOST 阈值
- **R1-N2 (Incompleteness confound)**: 完全同意，token count 是差的 proxy
- **R1-N3 (ICC 跨 provider)**: 反驳 Must-Fix 严重性——Kendall's W 和全模型显著性已提供跨 provider 证据，建议降为 Should-Fix
- **R1-W1 (移除 authorization scope)**: 反驳——低 κ 反映 construct difficulty，不应移除
- **R1-W2/W3/W4**: 均同意
- **Minor**: 均同意，"nocuous" 问题与我的 N2 互相强化

两位 reviewer 的核心共识：type-mechanism dissociation 的证据链有两个独立薄弱环节（R1: TOST 阈值；R2: 人工标注 κ=0.15），incompleteness confound 需更好处理，"nocuous" 术语需重新考虑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2305 · 2026-05-23T12:03:05.756530+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Round 26 (Fresh)\n\n**Paper**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n**Venue**: EMNLP 2026 via ARR May cycle\n**Reviewers**: 2 (R1: 方法严谨性, R2: 新颖性与完整性)\n**Date**: 2026-05-23\n\n---\n\n## Summary\n\nThis paper uses a matched-pair causal design to study how policy ambiguity affects safety violations in LLM agents. Using 300 clause pairs across a six-type taxonomy on τ²-bench with five models (2,997 episodes), the authors show ambiguous clauses increase violations by +34.0pp (+31.0pp confound-free). The core finding is a \"type-mechanism dissociation\": ambiguity type predicts failure mechanism (Cramér's V=0.45) but not violation rate (V=0.14). Error analysis reveals \"disambiguation neglect\" (4.6% awareness) and \"systematic nocuity\" (77% permissive bias, convergent errors).\n\n---\n\n## Strengths\n\n**S1. Matched-pair causal design is methodologically strong.** Rare in agent safety literature. Perturbation controls (Δ_perturb = -0.67pp, CI [-8.0, 6.67]) convincingly exclude surface-level rewriting as alternative explanation. 300 clause pairs × 5 models with 96% initial annotator agreement provides solid internal validity.\n\n**S2. Comprehensive statistical analysis and transparency.** TOST equivalence testing across 7 margins, bootstrap cluster analysis, ICC variance decomposition, cross-benchmark replication (SOPBench), cross-architecture replication (Gemini, LLaMA), and 15 pages of appendices addressing nearly all foreseeable reviewer questions.\n\n**S3. Type-mechanism dissociation has practical value.** Even with reliability caveats, the directional finding that type predicts mechanism more strongly than severity is actionable: clause-level auditing > type-level risk classification.\n\n**S4. Real-world grounding.** Prevalence audit (24 production documents, 407 clauses, 55–87% ambiguous) establishes practical relevance. SOPBench cross-benchmark replication confirms directional consistency.\n\n**S5. Confound handling is honest.** Incompleteness information-addition confound is explicitly identified, separately analyzed (Appendix F), and the confound-free effect (31.0pp) is reported alongside the full effect (34.0pp).\n\n---\n\n## Weaknesses\n\n### Must-Fix (3 issues — affect acceptance decision)\n\n**MF1. [consensus, critical] Type-mechanism dissociation (Contribution 2) reliability is insufficiently supported.**\n- Location: §6.1, Appendix AE\n- The core evidence for V=0.45 rests entirely on LLM-coded failure mechanism labels, while human annotation agreement is κ=0.15 (near chance). The paper acknowledges this is an \"upper bound\" (§6.1) but still presents it as a headline contribution and abstract number. The contrast with violation severity agreement (κ=0.653) is stark: the same annotators reliably identify *whether* agents violate but cannot agree on *how* they fail, suggesting the failure mechanism taxonomy's construct validity is itself problematic. LLM coding consistency may reflect systematic classification preferences (e.g., routing incompleteness to \"gap-filling\") rather than genuine type-mechanism association.\n- **Cross-response**: Both reviewers independently AGREE this is Must-Fix. R1 adds the κ=0.653 vs κ=0.15 contrast as direct evidence of construct validity problems. R2 initially raised it; R1 converges via the construct validity route.\n- **Action required**: (a) §6 must devote a full paragraph (not parenthetical) to discussing κ=0.15 and its implications; (b) downgrade type-mechanism dissociation from \"contribution\" to \"exploratory finding\"; (c) abstract V=0.45 needs \"LLM-coded\" qualifier; (d) report V computed from human annotations as a floor estimate.\n\n**MF2. [R1 Must-Fix, R2 partial agree] SESOI ±15pp lacks principled domain justification — but scope is narrower than initially argued.**\n- Location: §4.6, Table 3\n- The TOST equivalence structure (mid-tier cluster, incompleteness separation) depends on ±15pp. For safety-critical applications, 14.9pp additional violation rate at scale could mean hundreds of unsafe actions. At ±10pp, only 3/15 type pairs reach equivalence.\n- **Cross-response refinement**: R2 correctly notes that C2's *core* evidence — Cramér's V=0.45 (type→mechanism) vs V=0.14 (type→violation rate) — does not depend on any TOST threshold. V=0.14 is computed directly from the contingency table. TOST supports the *auxiliary* claim that types form equivalence clusters in violation rate, not the headline dissociation. Therefore, SESOI affects the granularity of the type ordering, not the directional dissociation conclusion.\n- **Action required**: (a) Provide safety-domain justification for ±15pp, or adopt ±10pp as primary with ±15pp as sensitivity; (b) in presentation, clearly separate the V comparison (threshold-independent) from the TOST equivalence structure (threshold-dependent); (c) scope C2 equivalence claims to the chosen margin.\n\n**MF3. [consensus] Incompleteness confound control is methodologically insufficient.**\n- Location: §4.5, Appendix F\n- Token count as a proxy for information content has a fundamental flaw: a short phrase like \"non-refundable\" carries high policy information in few tokens, while lengthy clarifications may add minimal semantic content. The regression assumes linear token-count mediation, but the actual confound concerns information *type* (policy-relevant vs. disambiguating), not *quantity*.\n- **Cross-response**: Both reviewers fully AGREE. R2 adds that incompleteness confound may partially explain the synthetic-to-natural effect gap (34pp vs 12.7pp).\n- **Action required**: (a) Add a control condition with equal-length non-disambiguating policy text; or (b) exclude incompleteness from primary causal claims and treat as observational evidence, using confound-free 31.0pp as the headline effect.\n\n### Should-Fix (9 issues — affect scoring)\n\n**SF1. [R2 Must-Fix → R1 REBUT → consensus Should-Fix] \"Nocuous\" terminology semantic inversion needs stronger justification.**\nBerry et al. (2004) define nocuous = divergent interpretation; this paper finds convergent error. R2 elevated to Must-Fix; R1 REBUT argues the semantic extension is defensible — Berry's core meaning is \"harmful\" (vs. innocuous), and §6.3 explicitly addresses the inversion. Both agree Introduction should handle this earlier (currently first discussed in §6.3, too late). R1: \"标题的功能是引起注意和传达核心 message（'policy ambiguity is harmful'），§6.3 的详细论证足以为熟悉 Berry et al. 的读者消解歧义。\" **Consensus**: Should-Fix — expand Introduction treatment; consider whether \"systematically harmful\" or \"convergently nocuous\" would be more precise.\n\n**SF2. [R1 Should-Fix → R2 REBUT] Authorization scope: discuss construct difficulty rather than remove.**\nκ=0.385 (lowest), 52pp cross-model range (largest), drives C4 interaction, ρ=0.09 cross-judge-group discordance. R1 suggested presenting five-type taxonomy as primary. R2 REBUT: \"将一个'难以可靠标注'的类型从 taxonomy 中移除是方法论上的倒退：如果某种歧义在实践中特别难以诊断，这恰恰是需要被 taxonomy 保留并研究的类型。\" Paper already provides Appendix O (sans-auth analysis). **Consensus**: Retain in taxonomy but add 1-2 sentences in §5.2 main text discussing construct difficulty and its implications for interpreting auth scope results.\n\n**SF3. [consensus] Synthetic-to-natural effect gap (34pp vs 12.7pp) and cross-domain ρ=0.26 need main text discussion.**\nBoth reviewers AGREE. The three-factor explanation (measurement grain, baseline compression, interaction depth) is in appendix only. ρ=0.26 (effectively zero for type rankings across domains) is only in Appendix Z but directly impacts taxonomy diagnostic claims. R2 adds that incompleteness confound may partially explain the gap. **Action**: Move both to Discussion §7; Conclusion should state type-level findings are domain-contingent.\n\n**SF4. [R2 Should-Fix → R1 partial REBUT] Incremental contribution over DRIP-R (2026) needs explicit articulation.**\nDRIP-R already establishes \"ambiguity hurts agents\" on 400 scenarios × 5 RE types. R1 REBUT argues the three differentiators are substantive: different outcome variable (safety violations vs decision quality), matched-pair causal design (excludes scenario-level confounds), and novel phenomena (type-mechanism dissociation, convergent nocuity). R1: \"因果设计是实质性方法论进步，不应被简化为 '重复已知结论'。\" But both agree the paper should explicitly answer: \"what does the causal design change vs DRIP-R's correlational evidence?\" **Action**: Add direct comparison paragraph in §2 or §7.\n\n**SF5. [R2 Should-Fix, R1 AGREE] 'Ambiguity' broad usage creates tension with NLP community standards.**\nBoth AGREE. §3 \"Scope of 'ambiguity'\" argues functional equivalence only. R1 agrees on Poesio & Artstein (2005) citation but REBUTS renaming to \"policy underspecification\" (would lose lexical/scopal types that *are* linguistic ambiguity). **Consensus**: Reference underspecification/vagueness distinction; add \"policy specification\" qualifier; keep \"ambiguity\" as term.\n\n**SF6. [R1 Should-Fix, R2 AGREE] Temperature=0 limits variance decomposition interpretation.**\nBoth AGREE. R2 adds nuance: ICC(1)=0.749 already shows 25.1% within-cell stochastic variance at temperature=0; this would increase further at temperature>0, reducing systematic component's share. R2: \"但核心方向性结论（ambiguity increases violations, type predicts mechanism > rate）在合理 temperature 范围内应仍然成立。\" **Action**: §5.1 variance decomposition paragraph should note temperature=0 constraint; not a fundamental threat but important scope condition.\n\n**SF7. [R2 Should-Fix, R1 AGREE] Taxonomy 11→6 selection criteria need transparent reporting.**\nBoth AGREE. Ellipsis exclusion attributed to \"RE attestation\" but likely driven by minimal-pair construction difficulty. R1: \"如果一种歧义类型无法构造最小对，排除它是合理的方法论决策，但应透明陈述为实际约束。\" **Action**: Appendix M should honestly attribute practical constraints where they apply.\n\n**SF8. [consensus] Abstract information density is excessive.**\nBoth AGREE. ~190 words with 8+ quantitative figures. R1 suggests keeping 3-4 core numbers. **Action**: Reduce to overall effect, confound-free effect, SOPBench replication, and type-mechanism V contrast.\n\n**SF9. [R1 Must-Fix → R2 REBUT → consensus Should-Fix] Cross-provider reproducibility: add explicit cross-provider metric.**\nR1 argued ICC(1)=0.919 limited to OpenAI family is a Must-Fix. R2 REBUT with three arguments: (1) ICC is methodologically a within-family nesting metric — computing it across providers may violate variance structure assumptions; (2) Kendall's W=0.396 (p=0.072) already serves as a cross-provider concordance metric; (3) all 5 models show significant effects, Appendix E confirms on 2 additional providers. R2: \"将 GPT-5.4、Claude Sonnet 4.6、Qwen3-235B 放入同一 ICC 模型，其 variance structure 的假设可能不成立。\" **Consensus**: Downgrade to Should-Fix. Add explicit cross-provider metric (Kendall's W or Krippendorff's α) in appendix; relabel §4.4 claim scope.\n\n### Minor (6 issues)\n\n- M1. \"Confound-free\" terminology used inconsistently: Abstract \"confound-free types\" (excluding incompleteness) vs. Limitations \"+34.0pp confound-free\" (after perturbation controls). Both reviewers flagged.\n- M2. Table 2 footnote markers (†, ‡) are small and easily missed.\n- M3. \"Confound-free types\" first appears in §5.1 without inline definition.\n- M4. Replication results (Gemini, LLaMA): R2 suggests main text mention; R1 REBUTS (8-page constraint). Consensus: add one sentence pointing to Appendix E.\n- M5. Violation severity κ=0.653 vs failure mechanism κ=0.15 contrast is itself a finding worth main text mention in §6.1.\n- M6. Pages 5-6 are continuous text without display items; consider summary table for key statistics.\n\n---\n\n## Reviewer Consensus (post-cross-response)\n\nBoth reviewers explicitly AGREE on:\n1. **Type-mechanism dissociation evidence is weak** — two independent attack vectors (R1: TOST threshold dependency; R2: human κ=0.15) converge on the same conclusion\n2. **Incompleteness confound** — token count is a poor proxy for information content; both fully agree\n3. **Effect gap (34pp→12.7pp) needs main text discussion** — both agree\n4. **\"Nocuous\" terminology needs attention** — R1 from accessibility angle, R2 from semantic accuracy; mutual reinforcement\n5. **\"Confound-free\" terminology is inconsistent** — both flagged independently\n6. **Abstract overloaded** — both agree\n7. **Taxonomy 11→6 selection needs transparency** — both agree\n8. **Core strengths**: matched-pair design, statistical rigor, confound honesty, prevalence audit\n\n## Reviewer Divergence (post-cross-response)\n\n1. **Authorization scope treatment**: R1 recommends removal to 5-type taxonomy; R2 REBUTS — low κ reflects construct difficulty, not invalidity. **Resolution**: SF2 — retain but discuss difficulty in main text.\n2. **ICC cross-provider severity**: R1 Must-Fix; R2 REBUT — Kendall's W already provides cross-provider evidence, ICC is methodologically within-family. **Resolution**: SF9 — add explicit metric but not blocking.\n3. **\"Nocuous\" severity**: R2 Must-Fix; R1 REBUT — semantic extension is defensible, §6.3 addresses it. **Resolution**: SF1 — expand Introduction treatment.\n4. **DRIP-R incremental**: R2 questions sufficiency; R1 partially REBUTS — causal design is substantive upgrade. **Resolution**: SF4 — articulate what causal design changes.\n5. **SESOI scope**: R1 says C2 \"completely depends\" on TOST; R2 correctly narrows — V=0.14 is threshold-independent. **Resolution**: MF2 scope refined.\n\n---\n\n## Questions for Authors\n\nQ1. What is Cramér's V(type→mechanism) computed from human annotations? Even with low κ=0.15, this provides a floor estimate for the true dissociation strength.\n\nQ2. In unambiguous conditions, what is agents' \"false positive\" ambiguity awareness rate? If agents rarely discuss ambiguity in either condition, the 4.6% may reflect general low metacognition rather than ambiguity-specific neglect.\n\nQ3. For authorization scope (κ=0.385), at what agreement threshold would the type be excluded from the taxonomy rather than treated as a \"difficult construct\"?\n\nQ4. Could a control condition for incompleteness be designed — adding equal-length non-disambiguating policy text — without requiring new experiments?\n\nQ5. DRIP-R's correlational design leaves which specific confounds unaddressed that your causal design resolves? Can you articulate one concrete example where the causal conclusion differs from what correlation alone would support?\n\n---\n\n## Missing References\n\n1. **Poesio & Artstein (2005)** — \"Annotating (Anaphoric) Ambiguity.\" Relevant to §3's discussion of ambiguity vs. underspecification vs. vagueness. Both reviewers agree this is needed.\n2. **Bai et al. (2022)** — \"Constitutional AI.\" Relevant context for the 77% permissive bias finding in §6.3. R1 agrees; provides mechanism explanation for why models default to permissive interpretation.\n3. **Zhou et al. (2023)** — \"Instruction-Following Evaluation for Large Language Models\" (IFEval). R1 REBUTS relevance — paper already cites more directly relevant agent safety benchmarks. **Optional, not required.**\n\n---\n\n## External Review\n\n**Status**: Not requested (project not configured for external review).\n\n---\n\n## Visual Layout Check (non-scoring)\n\nVisual check completed (3 warnings, 16 info items, 0 critical):\n- ⚠️ **Pages 5-6**: Continuous 2 pages of pure text (Methods 4.3-4.6 + Results 5.1-5.2) without display items. Dense quantitative results in prose are reviewer-unfriendly.\n- ⚠️ **Page 8**: Extremely crowded — Figures 2, 3, 4 + Discussion + Conclusion all compressed into one page. Axis labels at readability edge when printed.\n- ⚠️ **Page 23**: Final appendix page ~85% blank.\n- ✅ Main text exactly 8 pages (EMNLP compliant). Limitations p9 (compliant). Double-blind correct. No overflows or LaTeX errors.\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 (Borderline Conference)**\n**Confidence: 4/5**\n\nBoth reviewers independently rate 3.5 (Borderline Conference) with high confidence. Cross-response discussion refines but does not change the overall assessment.\n\nThis paper makes a methodologically rigorous contribution to an important and timely problem. The matched-pair causal design is rare in agent safety literature, and the experimental execution (5 models, 2,997 episodes, 15-page appendix) demonstrates high scientific standards.\n\nThree Must-Fix issues prevent a confident Conference recommendation:\n\n1. **Type-mechanism dissociation reliability** (MF1): Both reviewers agree this is the paper's most novel claim but also its weakest evidential link. Two independent attack vectors — human κ=0.15 (R2) and TOST threshold dependency for the equivalence half (R1) — converge. The κ=0.653 vs κ=0.15 contrast (same annotators: reliable on *whether*, near-random on *how*) is particularly damaging.\n\n2. **SESOI justification** (MF2): Affects the TOST equivalence structure, though the core V comparison is threshold-independent (per R2's cross-response). Still needs domain grounding.\n\n3. **Incompleteness confound** (MF3): Both reviewers fully agree. Token count is an inadequate proxy. The highest-risk type's effect remains partially confounded.\n\nCross-provider reproducibility (originally MF4) was downgraded to SF9 after R2's methodological argument that Kendall's W already provides cross-provider evidence and ICC is inherently a within-family metric.\n\n**Recommendation path**:\n- **Findings (3.0-3.5)**: Achievable now. Downgrade dissociation to exploratory, use 31.0pp as headline, add domain qualifiers.\n- **Conference (4.0)**: Requires MF1 (dissociation reliability discussion), MF2 (principled SESOI or scoped claims), MF3 (better incompleteness control or exclusion from causal claims), plus SF1-SF4.\n\n**Current recommendation**: Findings-acceptable. Conference-borderline, conditional on Must-Fix resolution.\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution (2) should carry a reliability caveat referencing §6's LLM-coding limitation (MF1).\n- \"We show that LLM agents invert this pattern, exhibiting convergent rather than divergent misinterpretation\" — needs expansion as the foundation for the title's \"nocuous\" claim (SF1).\n\n### §3 Taxonomy\n- \"Scope of 'ambiguity'\" paragraph needs Poesio & Artstein (2005) reference and systematic engagement with ambiguity/underspecification distinction (SF5).\n- Li et al. 11→6 mapping should honestly attribute practical constraints (SF7).\n\n### §4 Method\n- §4.6 SESOI: \"pragmatic default\" needs either domain grounding or explicit scoping of downstream claims (MF2).\n- Cross-judge design asymmetry (3 vs 2 models per judge) should be explicitly noted.\n\n### §5 Results\n- §5.1: \"confound-free types\" needs inline definition (M3).\n- Variance decomposition should note temperature=0 constraint (SF6).\n- Clearly separate V comparison (threshold-free) from TOST equivalence structure (threshold-dependent) in C2 presentation (MF2).\n\n### §6 Error Analysis\n- κ=0.15 implications for Contribution 2 need a full paragraph, not parenthetical (MF1).\n- κ=0.653 vs κ=0.15 contrast deserves explicit main text discussion (M5).\n- Disambiguation neglect: add unambiguous-condition baseline (Q2).\n\n### §7 Discussion\n- Three-factor explanation for effect gap and ρ=0.26 cross-domain type ranking must appear here (SF3).\n- Authorization scope construct difficulty needs 1-2 sentences (SF2).\n- DRIP-R differentiation should be explicit (SF4).\n- Permissive bias (77%) should reference Constitutional AI literature (missing ref #2).\n\n### §8 Conclusion\n- \"clause-level policy auditing is the actionable intervention\" depends on dissociation (MF1 concern); add appropriate hedging.\n- \"type-level findings are domain-contingent\" should be stated (SF3).\n\n### Limitations\n- Add one sentence on type-mechanism dissociation's dependence on LLM coding labels (MF1).",
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 borderline conference",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — Round 26 (Fresh)\n\n**Paper**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n**Venue**: EMNLP 2026 via ARR May cycle\n**Reviewers**: 2 (R1: 方法严谨性, R2: 新颖性与完整性)\n**Date**: 2026-05-23\n\n---\n\n## Summary\n\nThis paper uses a matched-pair causal design to study how policy ambiguity affects safety violations in LLM agents. Using 300 clause pairs across a six-type taxonomy on τ²-bench with five models (2,997 episodes), the authors show ambiguous clauses increase violations by +34.0pp (+31.0pp confound-free). The core finding is a \"type-mechanism dissociation\": ambiguity type predicts failure mechanism (Cramér's V=0.45) but not violation rate (V=0.14). Error analysis reveals \"disambiguation neglect\" (4.6% awareness) and \"systematic nocuity\" (77% permissive bias, convergent errors).\n\n---\n\n## Strengths\n\n**S1. Matched-pair causal design is methodologically strong.** Rare in agent safety literature. Perturbation controls (Δ_perturb = -0.67pp, CI [-8.0, 6.67]) convincingly exclude surface-level rewriting as alternative explanation. 300 clause pairs × 5 models with 96% initial annotator agreement provides solid internal validity.\n\n**S2. Comprehensive statistical analysis and transparency.** TOST equivalence testing across 7 margins, bootstrap cluster analysis, ICC variance decomposition, cross-benchmark replication (SOPBench), cross-architecture replication (Gemini, LLaMA), and 15 pages of appendices addressing nearly all foreseeable reviewer questions.\n\n**S3. Type-mechanism dissociation has practical value.** Even with reliability caveats, the directional finding that type predicts mechanism more strongly than severity is actionable: clause-level auditing > type-level risk classification.\n\n**S4. Real-world grounding.** Prevalence audit (24 production documents, 407 clauses, 55–87% ambiguous) establishes practical relevance. SOPBench cross-benchmark replication confirms directional consistency.\n\n**S5. Confound handling is honest.** Incompleteness information-addition confound is explicitly identified, separately analyzed (Appendix F), and the confound-free effect (31.0pp) is reported alongside the full effect (34.0pp).\n\n---\n\n## Weaknesses\n\n### Must-Fix (3 issues — affect acceptance decision)\n\n**MF1. [consensus, critical] Type-mechanism dissociation (Contribution 2) reliability is insufficiently supported.**\n- Location: §6.1, Appendix AE\n- The core evidence for V=0.45 rests entirely on LLM-coded failure mechanism labels, while human annotation agreement is κ=0.15 (near chance). The paper acknowledges this is an \"upper bound\" (§6.1) but still presents it as a headline contribution and abstract number. The contrast with violation severity agreement (κ=0.653) is stark: the same annotators reliably identify *whether* agents violate but cannot agree on *how* they fail, suggesting the failure mechanism taxonomy's construct validity is itself problematic. LLM coding consistency may reflect systematic classification preferences (e.g., routing incompleteness to \"gap-filling\") rather than genuine type-mechanism association.\n- **Cross-response**: Both reviewers independently AGREE this is Must-Fix. R1 adds the κ=0.653 vs κ=0.15 contrast as direct evidence of construct validity problems. R2 initially raised it; R1 converges via the construct validity route.\n- **Action required**: (a) §6 must devote a full paragraph (not parenthetical) to discussing κ=0.15 and its implications; (b) downgrade type-mechanism dissociation from \"contribution\" to \"exploratory finding\"; (c) abstract V=0.45 needs \"LLM-coded\" qualifier; (d) report V computed from human annotations as a floor estimate.\n\n**MF2. [R1 Must-Fix, R2 partial agree] SESOI ±15pp lacks principled domain justification — but scope is narrower than initially argued.**\n- Location: §4.6, Table 3\n- The TOST equivalence structure (mid-tier cluster, incompleteness separation) depends on ±15pp. For safety-critical applications, 14.9pp additional violation rate at scale could mean hundreds of unsafe actions. At ±10pp, only 3/15 type pairs reach equivalence.\n- **Cross-response refinement**: R2 correctly notes that C2's *core* evidence — Cramér's V=0.45 (type→mechanism) vs V=0.14 (type→violation rate) — does not depend on any TOST threshold. V=0.14 is computed directly from the contingency table. TOST supports the *auxiliary* claim that types form equivalence clusters in violation rate, not the headline dissociation. Therefore, SESOI affects the granularity of the type ordering, not the directional dissociation conclusion.\n- **Action required**: (a) Provide safety-domain justification for ±15pp, or adopt ±10pp as primary with ±15pp as sensitivity; (b) in presentation, clearly separate the V comparison (threshold-independent) from the TOST equivalence structure (threshold-dependent); (c) scope C2 equivalence claims to the chosen margin.\n\n**MF3. [consensus] Incompleteness confound control is methodologically insufficient.**\n- Location: §4.5, Appendix F\n- Token count as a proxy for information content has a fundamental flaw: a short phrase like \"non-refundable\" carries high policy information in few tokens, while lengthy clarifications may add minimal semantic content. The regression assumes linear token-count mediation, but the actual confound concerns information *type* (policy-relevant vs. disambiguating), not *quantity*.\n- **Cross-response**: Both reviewers fully AGREE. R2 adds that incompleteness confound may partially explain the synthetic-to-natural effect gap (34pp vs 12.7pp).\n- **Action required**: (a) Add a control condition with equal-length non-disambiguating policy text; or (b) exclude incompleteness from primary causal claims and treat as observational evidence, using confound-free 31.0pp as the headline effect.\n\n### Should-Fix (9 issues — affect scoring)\n\n**SF1. [R2 Must-Fix → R1 REBUT → consensus Should-Fix] \"Nocuous\" terminology semantic inversion needs stronger justification.**\nBerry et al. (2004) define nocuous = divergent interpretation; this paper finds convergent error. R2 elevated to Must-Fix; R1 REBUT argues the semantic extension is defensible — Berry's core meaning is \"harmful\" (vs. innocuous), and §6.3 explicitly addresses the inversion. Both agree Introduction should handle this earlier (currently first discussed in §6.3, too late). R1: \"标题的功能是引起注意和传达核心 message（'policy ambiguity is harmful'），§6.3 的详细论证足以为熟悉 Berry et al. 的读者消解歧义。\" **Consensus**: Should-Fix — expand Introduction treatment; consider whether \"systematically harmful\" or \"convergently nocuous\" would be more precise.\n\n**SF2. [R1 Should-Fix → R2 REBUT] Authorization scope: discuss construct difficulty rather than remove.**\nκ=0.385 (lowest), 52pp cross-model range (largest), drives C4 interaction, ρ=0.09 cross-judge-group discordance. R1 suggested presenting five-type taxonomy as primary. R2 REBUT: \"将一个'难以可靠标注'的类型从 taxonomy 中移除是方法论上的倒退：如果某种歧义在实践中特别难以诊断，这恰恰是需要被 taxonomy 保留并研究的类型。\" Paper already provides Appendix O (sans-auth analysis). **Consensus**: Retain in taxonomy but add 1-2 sentences in §5.2 main text discussing construct difficulty and its implications for interpreting auth scope results.\n\n**SF3. [consensus] Synthetic-to-natural effect gap (34pp vs 12.7pp) and cross-domain ρ=0.26 need main text discussion.**\nBoth reviewers AGREE. The three-factor explanation (measurement grain, baseline compression, interaction depth) is in appendix only. ρ=0.26 (effectively zero for type rankings across domains) is only in Appendix Z but directly impacts taxonomy diagnostic claims. R2 adds that incompleteness confound may partially explain the gap. **Action**: Move both to Discussion §7; Conclusion should state type-level findings are domain-contingent.\n\n**SF4. [R2 Should-Fix → R1 partial REBUT] Incremental contribution over DRIP-R (2026) needs explicit articulation.**\nDRIP-R already establishes \"ambiguity hurts agents\" on 400 scenarios × 5 RE types. R1 REBUT argues the three differentiators are substantive: different outcome variable (safety violations vs decision quality), matched-pair causal design (excludes scenario-level confounds), and novel phenomena (type-mechanism dissociation, convergent nocuity). R1: \"因果设计是实质性方法论进步，不应被简化为 '重复已知结论'。\" But both agree the paper should explicitly answer: \"what does the causal design change vs DRIP-R's correlational evidence?\" **Action**: Add direct comparison paragraph in §2 or §7.\n\n**SF5. [R2 Should-Fix, R1 AGREE] 'Ambiguity' broad usage creates tension with NLP community standards.**\nBoth AGREE. §3 \"Scope of 'ambiguity'\" argues functional equivalence only. R1 agrees on Poesio & Artstein (2005) citation but REBUTS renaming to \"policy underspecification\" (would lose lexical/scopal types that *are* linguistic ambiguity). **Consensus**: Reference underspecification/vagueness distinction; add \"policy specification\" qualifier; keep \"ambiguity\" as term.\n\n**SF6. [R1 Should-Fix, R2 AGREE] Temperature=0 limits variance decomposition interpretation.**\nBoth AGREE. R2 adds nuance: ICC(1)=0.749 already shows 25.1% within-cell stochastic variance at temperature=0; this would increase further at temperature>0, reducing systematic component's share. R2: \"但核心方向性结论（ambiguity increases violations, type predicts mechanism > rate）在合理 temperature 范围内应仍然成立。\" **Action**: §5.1 variance decomposition paragraph should note temperature=0 constraint; not a fundamental threat but important scope condition.\n\n**SF7. [R2 Should-Fix, R1 AGREE] Taxonomy 11→6 selection criteria need transparent reporting.**\nBoth AGREE. Ellipsis exclusion attributed to \"RE attestation\" but likely driven by minimal-pair construction difficulty. R1: \"如果一种歧义类型无法构造最小对，排除它是合理的方法论决策，但应透明陈述为实际约束。\" **Action**: Appendix M should honestly attribute practical constraints where they apply.\n\n**SF8. [consensus] Abstract information density is excessive.**\nBoth AGREE. ~190 words with 8+ quantitative figures. R1 suggests keeping 3-4 core numbers. **Action**: Reduce to overall effect, confound-free effect, SOPBench replication, and type-mechanism V contrast.\n\n**SF9. [R1 Must-Fix → R2 REBUT → consensus Should-Fix] Cross-provider reproducibility: add explicit cross-provider metric.**\nR1 argued ICC(1)=0.919 limited to OpenAI family is a Must-Fix. R2 REBUT with three arguments: (1) ICC is methodologically a within-family nesting metric — computing it across providers may violate variance structure assumptions; (2) Kendall's W=0.396 (p=0.072) already serves as a cross-provider concordance metric; (3) all 5 models show significant effects, Appendix E confirms on 2 additional providers. R2: \"将 GPT-5.4、Claude Sonnet 4.6、Qwen3-235B 放入同一 ICC 模型，其 variance structure 的假设可能不成立。\" **Consensus**: Downgrade to Should-Fix. Add explicit cross-provider metric (Kendall's W or Krippendorff's α) in appendix; relabel §4.4 claim scope.\n\n### Minor (6 issues)\n\n- M1. \"Confound-free\" terminology used inconsistently: Abstract \"confound-free types\" (excluding incompleteness) vs. Limitations \"+34.0pp confound-free\" (after perturbation controls). Both reviewers flagged.\n- M2. Table 2 footnote markers (†, ‡) are small and easily missed.\n- M3. \"Confound-free types\" first appears in §5.1 without inline definition.\n- M4. Replication results (Gemini, LLaMA): R2 suggests main text mention; R1 REBUTS (8-page constraint). Consensus: add one sentence pointing to Appendix E.\n- M5. Violation severity κ=0.653 vs failure mechanism κ=0.15 contrast is itself a finding worth main text mention in §6.1.\n- M6. Pages 5-6 are continuous text without display items; consider summary table for key statistics.\n\n---\n\n## Reviewer Consensus (post-cross-response)\n\nBoth reviewers explicitly AGREE on:\n1. **Type-mechanism dissociation evidence is weak** — two independent attack vectors (R1: TOST threshold dependency; R2: human κ=0.15) converge on the same conclusion\n2. **Incompleteness confound** — token count is a poor proxy for information content; both fully agree\n3. **Effect gap (34pp→12.7pp) needs main text discussion** — both agree\n4. **\"Nocuous\" terminology needs attention** — R1 from accessibility angle, R2 from semantic accuracy; mutual reinforcement\n5. **\"Confound-free\" terminology is inconsistent** — both flagged independently\n6. **Abstract overloaded** — both agree\n7. **Taxonomy 11→6 selection needs transparency** — both agree\n8. **Core strengths**: matched-pair design, statistical rigor, confound honesty, prevalence audit\n\n## Reviewer Divergence (post-cross-response)\n\n1. **Authorization scope treatment**: R1 recommends removal to 5-type taxonomy; R2 REBUTS — low κ reflects construct difficulty, not invalidity. **Resolution**: SF2 — retain but discuss difficulty in main text.\n2. **ICC cross-provider severity**: R1 Must-Fix; R2 REBUT — Kendall's W already provides cross-provider evidence, ICC is methodologically within-family. **Resolution**: SF9 — add explicit metric but not blocking.\n3. **\"Nocuous\" severity**: R2 Must-Fix; R1 REBUT — semantic extension is defensible, §6.3 addresses it. **Resolution**: SF1 — expand Introduction treatment.\n4. **DRIP-R incremental**: R2 questions sufficiency; R1 partially REBUTS — causal design is substantive upgrade. **Resolution**: SF4 — articulate what causal design changes.\n5. **SESOI scope**: R1 says C2 \"completely depends\" on TOST; R2 correctly narrows — V=0.14 is threshold-independent. **Resolution**: MF2 scope refined.\n\n---\n\n## Questions for Authors\n\nQ1. What is Cramér's V(type→mechanism) computed from human annotations? Even with low κ=0.15, this provides a floor estimate for the true dissociation strength.\n\nQ2. In unambiguous conditions, what is agents' \"false positive\" ambiguity awareness rate? If agents rarely discuss ambiguity in either condition, the 4.6% may reflect general low metacognition rather than ambiguity-specific neglect.\n\nQ3. For authorization scope (κ=0.385), at what agreement threshold would the type be excluded from the taxonomy rather than treated as a \"difficult construct\"?\n\nQ4. Could a control condition for incompleteness be designed — adding equal-length non-disambiguating policy text — without requiring new experiments?\n\nQ5. DRIP-R's correlational design leaves which specific confounds unaddressed that your causal design resolves? Can you articulate one concrete example where the causal conclusion differs from what correlation alone would support?\n\n---\n\n## Missing References\n\n1. **Poesio & Artstein (2005)** — \"Annotating (Anaphoric) Ambiguity.\" Relevant to §3's discussion of ambiguity vs. underspecification vs. vagueness. Both reviewers agree this is needed.\n2. **Bai et al. (2022)** — \"Constitutional AI.\" Relevant context for the 77% permissive bias finding in §6.3. R1 agrees; provides mechanism explanation for why models default to permissive interpretation.\n3. **Zhou et al. (2023)** — \"Instruction-Following Evaluation for Large Language Models\" (IFEval). R1 REBUTS relevance — paper already cites more directly relevant agent safety benchmarks. **Optional, not required.**\n\n---\n\n## External Review\n\n**Status**: Not requested (project not configured for external review).\n\n---\n\n## Visual Layout Check (non-scoring)\n\nVisual check completed (3 warnings, 16 info items, 0 critical):\n- ⚠️ **Pages 5-6**: Continuous 2 pages of pure text (Methods 4.3-4.6 + Results 5.1-5.2) without display items. Dense quantitative results in prose are reviewer-unfriendly.\n- ⚠️ **Page 8**: Extremely crowded — Figures 2, 3, 4 + Discussion + Conclusion all compressed into one page. Axis labels at readability edge when printed.\n- ⚠️ **Page 23**: Final appendix page ~85% blank.\n- ✅ Main text exactly 8 pages (EMNLP compliant). Limitations p9 (compliant). Double-blind correct. No overflows or LaTeX errors.\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 (Borderline Conference)**\n**Confidence: 4/5**\n\nBoth reviewers independently rate 3.5 (Borderline Conference) with high confidence. Cross-response discussion refines but does not change the overall assessment.\n\nThis paper makes a methodologically rigorous contribution to an important and timely problem. The matched-pair causal design is rare in agent safety literature, and the experimental execution (5 models, 2,997 episodes, 15-page appendix) demonstrates high scientific standards.\n\nThree Must-Fix issues prevent a confident Conference recommendation:\n\n1. **Type-mechanism dissociation reliability** (MF1): Both reviewers agree this is the paper's most novel claim but also its weakest evidential link. Two independent attack vectors — human κ=0.15 (R2) and TOST threshold dependency for the equivalence half (R1) — converge. The κ=0.653 vs κ=0.15 contrast (same annotators: reliable on *whether*, near-random on *how*) is particularly damaging.\n\n2. **SESOI justification** (MF2): Affects the TOST equivalence structure, though the core V comparison is threshold-independent (per R2's cross-response). Still needs domain grounding.\n\n3. **Incompleteness confound** (MF3): Both reviewers fully agree. Token count is an inadequate proxy. The highest-risk type's effect remains partially confounded.\n\nCross-provider reproducibility (originally MF4) was downgraded to SF9 after R2's methodological argument that Kendall's W already provides cross-provider evidence and ICC is inherently a within-family metric.\n\n**Recommendation path**:\n- **Findings (3.0-3.5)**: Achievable now. Downgrade dissociation to exploratory, use 31.0pp as headline, add domain qualifiers.\n- **Conference (4.0)**: Requires MF1 (dissociation reliability discussion), MF2 (principled SESOI or scoped claims), MF3 (better incompleteness control or exclusion from causal claims), plus SF1-SF4.\n\n**Current recommendation**: Findings-acceptable. Conference-borderline, conditional on Must-Fix resolution.\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution (2) should carry a reliability caveat referencing §6's LLM-coding limitation (MF1).\n- \"We show that LLM agents invert this pattern, exhibiting convergent rather than divergent misinterpretation\" — needs expansion as the foundation for the title's \"nocuous\" claim (SF1).\n\n### §3 Taxonomy\n- \"Scope of 'ambiguity'\" paragraph needs Poesio & Artstein (2005) reference and systematic engagement with ambiguity/underspecification distinction (SF5).\n- Li et al. 11→6 mapping should honestly attribute practical constraints (SF7).\n\n### §4 Method\n- §4.6 SESOI: \"pragmatic default\" needs either domain grounding or explicit scoping of downstream claims (MF2).\n- Cross-judge design asymmetry (3 vs 2 models per judge) should be explicitly noted.\n\n### §5 Results\n- §5.1: \"confound-free types\" needs inline definition (M3).\n- Variance decomposition should note temperature=0 constraint (SF6).\n- Clearly separate V comparison (threshold-free) from TOST equivalence structure (threshold-dependent) in C2 presentation (MF2).\n\n### §6 Error Analysis\n- κ=0.15 implications for Contribution 2 need a full paragraph, not parenthetical (MF1).\n- κ=0.653 vs κ=0.15 contrast deserves explicit main text discussion (M5).\n- Disambiguation neglect: add unambiguous-condition baseline (Q2).\n\n### §7 Discussion\n- Three-factor explanation for effect gap and ρ=0.26 cross-domain type ranking must appear here (SF3).\n- Authorization scope construct difficulty needs 1-2 sentences (SF2).\n- DRIP-R differentiation should be explicit (SF4).\n- Permissive bias (77%) should reference Constitutional AI literature (missing ref #2).\n\n### §8 Conclusion\n- \"clause-level policy auditing is the actionable intervention\" depends on dissociation (MF1 concern); add appropriate hedging.\n- \"type-level findings are domain-contingent\" should be stated (SF3).\n\n### Limitations\n- Add one sentence on type-mechanism dissociation's dependence on LLM coding labels (MF1).",
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 borderline conference",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 2306 · 2026-05-23T12:03:10.177941+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4421
}
```

</details>

---


### Tool call

_source line 2307 · 2026-05-23T12:04:56.348135+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 26\n\n# ============================================================\n# R26 ISSUES — ACTIVE\n# ============================================================\n\n- id: \"R26-MF1\"\n  summary: \"Type-mechanism dissociation (Contribution 2) 核心证据依赖 LLM 编码标签，人工 κ=0.15 可靠性不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W8: §6 仍用 'mechanistically distinct' 等强表述，已修为 'as classified by LLM coders'\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix N1, R1 交叉后 AGREE。两个独立 attack vector 汇聚：R1 通过 construct validity (κ=0.653 vs κ=0.15 对比), R2 通过 LLM 分类偏好。共识 Must-Fix\"\n  action_items:\n    - round: 26\n      action: \"§6 主文用完整段落讨论 κ=0.15 影响；降级为 exploratory finding；abstract V=0.45 加 LLM-coded 限定词；报告人工标注 V 作为 floor estimate\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-MF2\"\n  summary: \"SESOI ±15pp 对安全研究领域缺乏原则性论证——影响 TOST 等价结构（但不影响 V 对比）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R24-W4 resolved: 已改为 'pragmatic default, not principled domain-anchored threshold'\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix N1, R2 交叉后部分 AGREE 但精确限定范围：V=0.14 不依赖 TOST 阈值，C2 方向性结论不受 SESOI 影响，SESOI 仅影响等价 cluster 结构\"\n  action_items:\n    - round: 26\n      action: \"提供安全领域论证或改 ±10pp 为主分析；正文分离 V 对比（阈值无关）与 TOST 等价结构（阈值依赖）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-MF3\"\n  summary: \"Incompleteness confound 控制方法论不充分——token count 作为信息内容 proxy 有根本缺陷\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W9: §5.1 已增加 'controlling for token count—a coarse proxy' caveat\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix N2, R2 交叉后完全 AGREE。confound 是信息*类型*非*数量*问题。R2 补充：此 confound 可能部分解释 34pp→12.7pp 效应差距\"\n  action_items:\n    - round: 26\n      action: \"增加等量非消歧政策文本控制条件；或将 incompleteness 从主因果 claims 排除，31.0pp 为 headline\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF1\"\n  summary: \"'Nocuous' 术语语义反转（divergent→convergent）需更充分论证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W4: Introduction 已加 'convergent rather than divergent misinterpretation' 句\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix N2, R1 交叉 REBUT→Should-Fix。R1 论证：Berry 核心含义是 harmful（vs innocuous），divergent 是具体表现而非定义。但两位均同意 §6.3 首次讨论太晚，应在 Introduction 展开\"\n  action_items:\n    - round: 26\n      action: \"Introduction 引用 Berry et al. 时充分论证 convergent vs divergent 区别；考虑标题精确化\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF2\"\n  summary: \"Authorization scope construct difficulty 需在正文讨论（而非移除）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W1: Discussion ¶1 已加 outlier sentence\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1 建议移除为五类型，R2 交叉 REBUT：低 κ 反映 construct difficulty 非 invalidity，保留并研究更恰当。共识 Should-Fix：§5.2 加 1-2 句讨论 construct difficulty\"\n  action_items:\n    - round: 26\n      action: \"§5.2 正文增加 1-2 句 auth scope construct difficulty 讨论及对结论影响\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF3\"\n  summary: \"合成→自然效应差距（34pp vs 12.7pp）和跨领域 ρ=0.26 需在正文讨论\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-N1/N2: Abstract/Conclusion 已报告两个数字，Discussion 已扩展 ecological validity 段\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"两位均 AGREE。三因素解释仅在 appendix；ρ=0.26 仅在 Appendix Z。Conclusion 需声明 type-level findings domain-contingent\"\n  action_items:\n    - round: 26\n      action: \"Discussion §7 纳入三因素解释和 ρ=0.26；Conclusion 加 domain-contingency 限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF4\"\n  summary: \"相对 DRIP-R (2026) 增量贡献需显式阐述 causal design 改变了什么\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix W3, R1 交叉部分 REBUT：因果设计是实质性进步（不同 outcome variable、排除 scenario-level confounds、新现象）。但共识：应显式回答 'causal design 改变了什么'\"\n  action_items:\n    - round: 26\n      action: \"§2 或 §7 增加段落：DRIP-R correlational 留下哪些 confound？causal design 具体回答了什么新问题？\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF5\"\n  summary: \"'Ambiguity' 广义使用需引用 underspecification 区分文献并加限定词\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W3: §3 已增加 Wasow et al. 2005 positioning sentence\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix W1, R1 交叉 AGREE。Wasow 引用不够——需 Poesio & Artstein (2005)。R1 反对改主术语为 underspecification（丢失 lexical/scopal），建议加 'policy specification' 限定词\"\n  action_items:\n    - round: 26\n      action: \"§3 引用 Poesio & Artstein (2005)；加 policy specification 限定词；保留 ambiguity 作为主术语\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF6\"\n  summary: \"Temperature=0 限制 variance decomposition 解读——需在正文明确\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W10: Limitations 已增加 temperature>0 方向性讨论\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W3, R2 交叉 AGREE。Limitations 不够——variance decomposition 部分本身需说明。R2 补充：ICC 已显示 25.1% stochastic variance at temp=0，temp>0 会更大但方向性结论应仍成立\"\n  action_items:\n    - round: 26\n      action: \"§5.1 variance decomposition 段落增加 temperature=0 scope 说明\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF7\"\n  summary: \"Taxonomy 11→6 选择标准需透明报告实际构造困难\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W2: Appendix 已增加 mapping 表格\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix W4, R1 交叉 AGREE。表格存在但排除理由不够诚实——应透明标注实际约束\"\n  action_items:\n    - round: 26\n      action: \"Appendix M 坦诚标注哪些类型因构造困难排除，与概念标准分开\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF8\"\n  summary: \"Abstract 信息密度过高——精简至 2-3 个核心数字\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix W5, R1 交叉 AGREE。~190 词 8+ 数字，认知负荷过重\"\n  action_items:\n    - round: 26\n      action: \"保留主效应、confound-free 效应、SOPBench 复制、V 对比 3-4 个数字，其余移入正文\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF9\"\n  summary: \"跨 provider 可复现性需显式量化指标（降级自 MF4）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W6: 标题已改为 'Within-family reproducibility'\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1 初评 Must-Fix N3, R2 交叉 REBUT→Should-Fix。R2 论证：(1) ICC 方法论上是 within-family 概念; (2) Kendall's W=0.396 已是跨 provider 指标; (3) 全模型显著性 + Appendix E 复制提供互补证据。共识降为 Should-Fix\"\n  action_items:\n    - round: 26\n      action: \"Appendix 补充全模型 Kendall's W 或 Krippendorff's α；§4.4 限定 claim scope\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M1\"\n  summary: \"'Confound-free' 术语不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"两位独立标记\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M2\"\n  summary: \"Violation severity κ=0.653 vs failure mechanism κ=0.15 对比值得正文讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2-M5, R1 交叉 AGREE。直接支撑 MF1 论点\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R25 ISSUES — STATUS UPDATE\n# ============================================================\n\n- id: \"R25-W5\"\n  summary: \"C3 inconclusive 但 taxonomy 仍按 two-layer 组织\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 26\n      reviewers: []\n      note: \"R26 未重新标记，可能已修复。待 Research Director 确认\"\n  action_items:\n    - round: 25\n      action: \"§3 改为 'provides an organizational framework'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Changed wording to 'organizational framework' and 'design hypothesis'\"\n  resolution_round: null\n\n- id: \"R25-W7\"\n  summary: \"60.8% 残差方差系统性部分未讨论来源\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 26\n      reviewers: []\n      note: \"R26 未重新标记，可能已修复。待 Research Director 确认\"\n  action_items:\n    - round: 25\n      action: \"Discussion ¶1 增加候选来源\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Added clause-level interactions explanation\"\n  resolution_round: null\n\n- id: \"R25-M2\"\n  summary: \"Disambiguation neglect 增量贡献需更明确阐述\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 26\n      reviewers: []\n      note: \"R26 未重新标记，可能已修复。待 Research Director 确认\"\n  action_items:\n    - round: 25\n      action: \"§6.2 重写为 extending ambiguity collapse\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Rewritten as extending ambiguity collapse to agentic context\"\n  resolution_round: null\n\n- id: \"R25-M3\"\n  summary: \"References 中 arXiv preprint 格式不统一\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"All entries consistently formatted\"\n  resolution_round: 25\n\n# ============================================================\n# R24 ISSUES — RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R24-N1\"\n  summary: \"Novelty framing 偏强\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Contributions rewritten\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 25\n\n- id: \"R24-N2\"\n  summary: \"Incompleteness confound framing 不够突出\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Abstract leads with confound-free 31.0pp\"\n  resolution_round: 25\n  first_raised_round: 21\n  last_seen_round: 24\n\n- id: \"R24-W2\"\n  summary: \"Template pipeline 不透明\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Appendix S added\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W4\"\n  summary: \"SESOI ±15pp justification 不够 principled\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Changed to 'pragmatic default'. Note: R26 re-raised as MF2\"\n  resolution_round: 25\n  first_raised_round: 20\n  last_seen_round: 26\n\n- id: \"R24-W6\"\n  summary: \"Human validation per-type CI 极宽\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Qualifier added\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W8\"\n  summary: \"NMI cardinality 不对称\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Changed to 'substantially more strongly'\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M4\"\n  summary: \"C3/C4 claim 层级暗示同等级\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Labeled C3 inconclusive, C4 exploratory\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M5\"\n  summary: \"Table 2 脚注缺 per-type 样本量\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added n≈17\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M6\"\n  summary: \"Prevalence audit κ=0.295 未在 Introduction 标注\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added dual-judge κ = 0.30\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X1\"\n  summary: \"ICC≈0 应改为 uninformative due to floor effects\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Reworded with floor effect explanation\"\n  resolution_round: 25\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R24-X3\"\n  summary: \"Limitations 过长\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"Compressed to 3 points\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X4\"\n  summary: \"Limitations 内部矛盾\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Removed underway, replaced with actual results\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 26\n\n# ============================================================\n# R26 ISSUES — ACTIVE\n# ============================================================\n\n- id: \"R26-MF1\"\n  summary: \"Type-mechanism dissociation (Contribution 2) 核心证据依赖 LLM 编码标签，人工 κ=0.15 可靠性不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W8: §6 仍用 'mechanistically distinct' 等强表述，已修为 'as classified by LLM coders'\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix N1, R1 交叉后 AGREE。两个独立 attack vector 汇聚：R1 通过 construct validity (κ=0.653 vs κ=0.15 对比), R2 通过 LLM 分类偏好。共识 Must-Fix\"\n  action_items:\n    - round: 26\n      action: \"§6 主文用完整段落讨论 κ=0.15 影响；降级为 exploratory finding；abstract V=0.45 加 LLM-coded 限定词；报告人工标注 V 作为 floor estimate\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-MF2\"\n  summary: \"SESOI ±15pp 对安全研究领域缺乏原则性论证——影响 TOST 等价结构（但不影响 V 对比）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R24-W4 resolved: 已改为 'pragmatic default, not principled domain-anchored threshold'\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix N1, R2 交叉后部分 AGREE 但精确限定范围：V=0.14 不依赖 TOST 阈值，C2 方向性结论不受 SESOI 影响，SESOI 仅影响等价 cluster 结构\"\n  action_items:\n    - round: 26\n      action: \"提供安全领域论证或改 ±10pp 为主分析；正文分离 V 对比（阈值无关）与 TOST 等价结构（阈值依赖）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-MF3\"\n  summary: \"Incompleteness confound 控制方法论不充分——token count 作为信息内容 proxy 有根本缺陷\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W9: §5.1 已增加 'controlling for token count—a coarse proxy' caveat\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix N2, R2 交叉后完全 AGREE。confound 是信息*类型*非*数量*问题。R2 补充：此 confound 可能部分解释 34pp→12.7pp 效应差距\"\n  action_items:\n    - round: 26\n      action: \"增加等量非消歧政策文本控制条件；或将 incompleteness 从主因果 claims 排除，31.0pp 为 headline\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF1\"\n  summary: \"'Nocuous' 术语语义反转（divergent→convergent）需更充分论证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W4: Introduction 已加 'convergent rather than divergent misinterpretation' 句\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Must-Fix N2, R1 交叉 REBUT→Should-Fix。R1 论证：Berry 核心含义是 harmful（vs innocuous），divergent 是具体表现而非定义。但两位均同意 §6.3 首次讨论太晚，应在 Introduction 展开\"\n  action_items:\n    - round: 26\n      action: \"Introduction 引用 Berry et al. 时充分论证 convergent vs divergent 区别；考虑标题精确化\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF2\"\n  summary: \"Authorization scope construct difficulty 需在正文讨论（而非移除）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W1: Discussion ¶1 已加 outlier sentence\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1 建议移除为五类型，R2 交叉 REBUT：低 κ 反映 construct difficulty 非 invalidity，保留并研究更恰当。共识 Should-Fix：§5.2 加 1-2 句讨论 construct difficulty\"\n  action_items:\n    - round: 26\n      action: \"§5.2 正文增加 1-2 句 auth scope construct difficulty 讨论及对结论影响\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF3\"\n  summary: \"合成→自然效应差距（34pp vs 12.7pp）和跨领域 ρ=0.26 需在正文讨论\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-N1/N2: Abstract/Conclusion 已报告两个数字，Discussion 已扩展 ecological validity 段\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"两位均 AGREE。三因素解释仅在 appendix；ρ=0.26 仅在 Appendix Z。Conclusion 需声明 type-level findings domain-contingent\"\n  action_items:\n    - round: 26\n      action: \"Discussion §7 纳入三因素解释和 ρ=0.26；Conclusion 加 domain-contingency 限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF4\"\n  summary: \"相对 DRIP-R (2026) 增量贡献需显式阐述 causal design 改变了什么\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix W3, R1 交叉部分 REBUT：因果设计是实质性进步（不同 outcome variable、排除 scenario-level confounds、新现象）。但共识：应显式回答 'causal design 改变了什么'\"\n  action_items:\n    - round: 26\n      action: \"§2 或 §7 增加段落：DRIP-R correlational 留下哪些 confound？causal design 具体回答了什么新问题？\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF5\"\n  summary: \"'Ambiguity' 广义使用需引用 underspecification 区分文献并加限定词\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W3: §3 已增加 Wasow et al. 2005 positioning sentence\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix W1, R1 交叉 AGREE。Wasow 引用不够——需 Poesio & Artstein (2005)。R1 反对改主术语为 underspecification（丢失 lexical/scopal），建议加 'policy specification' 限定词\"\n  action_items:\n    - round: 26\n      action: \"§3 引用 Poesio & Artstein (2005)；加 policy specification 限定词；保留 ambiguity 作为主术语\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF6\"\n  summary: \"Temperature=0 限制 variance decomposition 解读——需在正文明确\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W10: Limitations 已增加 temperature>0 方向性讨论\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix W3, R2 交叉 AGREE。Limitations 不够——variance decomposition 部分本身需说明。R2 补充：ICC 已显示 25.1% stochastic variance at temp=0，temp>0 会更大但方向性结论应仍成立\"\n  action_items:\n    - round: 26\n      action: \"§5.1 variance decomposition 段落增加 temperature=0 scope 说明\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF7\"\n  summary: \"Taxonomy 11→6 选择标准需透明报告实际构造困难\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W2: Appendix 已增加 mapping 表格\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix W4, R1 交叉 AGREE。表格存在但排除理由不够诚实——应透明标注实际约束\"\n  action_items:\n    - round: 26\n      action: \"Appendix M 坦诚标注哪些类型因构造困难排除，与概念标准分开\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF8\"\n  summary: \"Abstract 信息密度过高——精简至 2-3 个核心数字\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix W5, R1 交叉 AGREE。~190 词 8+ 数字，认知负荷过重\"\n  action_items:\n    - round: 26\n      action: \"保留主效应、confound-free 效应、SOPBench 复制、V 对比 3-4 个数字，其余移入正文\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF9\"\n  summary: \"跨 provider 可复现性需显式量化指标（降级自 MF4）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W6: 标题已改为 'Within-family reproducibility'\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R1 初评 Must-Fix N3, R2 交叉 REBUT→Should-Fix。R2 论证：(1) ICC 方法论上是 within-family 概念; (2) Kendall's W=0.396 已是跨 provider 指标; (3) 全模型显著性 + Appendix E 复制提供互补证据。共识降为 Should-Fix\"\n  action_items:\n    - round: 26\n      action: \"Appendix 补充全模型 Kendall's W 或 Krippendorff's α；§4.4 限定 claim scope\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M1\"\n  summary: \"'Confound-free' 术语不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"两位独立标记\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M2\"\n  summary: \"Violation severity κ=0.653 vs failure mechanism κ=0.15 对比值得正文讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R2-M5, R1 交叉 AGREE。直接支撑 MF1 论点\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R25 ISSUES — STATUS UPDATE\n# ============================================================\n\n- id: \"R25-W5\"\n  summary: \"C3 inconclusive 但 taxonomy 仍按 two-layer 组织\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 26\n      reviewers: []\n      note: \"R26 未重新标记，可能已修复。待 Research Director 确认\"\n  action_items:\n    - round: 25\n      action: \"§3 改为 'provides an organizational framework'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Changed wording to 'organizational framework' and 'design hypothesis'\"\n  resolution_round: null\n\n- id: \"R25-W7\"\n  summary: \"60.8% 残差方差系统性部分未讨论来源\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 26\n      reviewers: []\n      note: \"R26 未重新标记，可能已修复。待 Research Director 确认\"\n  action_items:\n    - round: 25\n      action: \"Discussion ¶1 增加候选来源\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Added clause-level interactions explanation\"\n  resolution_round: null\n\n- id: \"R25-M2\"\n  summary: \"Disambiguation neglect 增量贡献需更明确阐述\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 26\n      reviewers: []\n      note: \"R26 未重新标记，可能已修复。待 Research Director 确认\"\n  action_items:\n    - round: 25\n      action: \"§6.2 重写为 extending ambiguity collapse\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Rewritten as extending ambiguity collapse to agentic context\"\n  resolution_round: null\n\n- id: \"R25-M3\"\n  summary: \"References 中 arXiv preprint 格式不统一\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"All entries consistently formatted\"\n  resolution_round: 25\n\n# ============================================================\n# R24 ISSUES — RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R24-N1\"\n  summary: \"Novelty framing 偏强\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Contributions rewritten\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 25\n\n- id: \"R24-N2\"\n  summary: \"Incompleteness confound framing 不够突出\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Abstract leads with confound-free 31.0pp\"\n  resolution_round: 25\n  first_raised_round: 21\n  last_seen_round: 24\n\n- id: \"R24-W2\"\n  summary: \"Template pipeline 不透明\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Appendix S added\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W4\"\n  summary: \"SESOI ±15pp justification 不够 principled\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Changed to 'pragmatic default'. Note: R26 re-raised as MF2\"\n  resolution_round: 25\n  first_raised_round: 20\n  last_seen_round: 26\n\n- id: \"R24-W6\"\n  summary: \"Human validation per-type CI 极宽\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Qualifier added\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W8\"\n  summary: \"NMI cardinality 不对称\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Changed to 'substantially more strongly'\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M4\"\n  summary: \"C3/C4 claim 层级暗示同等级\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Labeled C3 inconclusive, C4 exploratory\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M5\"\n  summary: \"Table 2 脚注缺 per-type 样本量\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added n≈17\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M6\"\n  summary: \"Prevalence audit κ=0.295 未在 Introduction 标注\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added dual-judge κ = 0.30\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X1\"\n  summary: \"ICC≈0 应改为 uninformative due to floor effects\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Reworded with floor effect explanation\"\n  resolution_round: 25\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R24-X3\"\n  summary: \"Limitations 过长\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"Compressed to 3 points\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X4\"\n  summary: \"Limitations 内部矛盾\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Removed underway, replaced with actual results\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24"
  }
}
```

</details>

---


### Tool result

_source line 2308 · 2026-05-23T12:04:56.400336+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 13801}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 52
}
```

</details>

---


### Assistant

_source line 2309 · 2026-05-23T12:05:07.779707+00:00_

Round 26 审稿圆桌会议完成。

**最终结果**：**3.5 / 5（Borderline Conference）**，两位 Reviewer 独立评分一致。

**核心发现摘要**：

| 级别 | 数量 | 关键问题 |
|------|------|---------|
| Must-Fix | 3 | MF1: type-mechanism dissociation 可靠性（人工κ=0.15）; MF2: SESOI ±15pp 论证; MF3: incompleteness confound |
| Should-Fix | 9 | SF1-SF9: nocuous 术语、auth scope 讨论、效应差距正文化、DRIP-R 增量、ambiguity 术语、temperature=0、taxonomy 选择透明度、abstract 精简、跨 provider 指标 |
| Minor | 2 | confound-free 术语一致性、κ 对比值得正文讨论 |

**推荐路径**：当前版本 Findings-acceptable。Conference 需解决 MF1-MF3 + SF1-SF4。

报告已投递至 Research Director，Issue Tracker 已同步。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 220

## Round 220

54 recorded events


### User

_source line 2310 · 2026-05-23T13:11:19.229566+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2311 · 2026-05-23T13:11:30.555167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2312 · 2026-05-23T13:11:30.658618+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 2313 · 2026-05-23T13:11:37.489366+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2314 · 2026-05-23T13:11:37.489809+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2315 · 2026-05-23T13:11:40.755396+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2316 · 2026-05-23T13:11:40.806020+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2317 · 2026-05-23T13:11:45.028909+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2318 · 2026-05-23T13:11:46.939755+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1910
}
```

</details>

---


### Tool call

_source line 2319 · 2026-05-23T13:11:47.393450+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2320 · 2026-05-23T13:11:48.096771+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{placeins}
16	
17	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
18	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
19	
20	\definecolor{speccolor}{HTML}{C44E52}
21	\definecolor{lingcolor}{HTML}{4C72B0}
22	
23	\title{Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{sections/abstract}
31	\input{sections/introduction}
32	\input{sections/related_work}
33	\input{sections/taxonomy}
34	\input{sections/method}
35	\input{sections/experiments}
36	\input{sections/analysis}
37	\input{sections/discussion}
38	\input{sections/conclusion}
39	\input{sections/limitations}
40	
41	\bibliography{references}
42	
43	\appendix
44	\makeatletter
45	\newcommand{\extAlph}[1]{%
46	  \ifcase#1\or A\or B\or C\or D\or E\or F\or G\or H\or I\or J\or K\or L\or M\or N\or O\or P\or Q\or R\or S\or T\or U\or V\or W\or X\or Y\or Z\or AA\or AB\or AC\or AD\or AE\fi}
47	\renewcommand{\thesection}{\extAlph{\value{section}}}
48	\makeatother
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 2321 · 2026-05-23T13:11:48.400039+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2322 · 2026-05-23T13:11:48.400475+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2323 · 2026-05-23T13:11:48.751440+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "review_issues.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 2324 · 2026-05-23T13:11:48.802014+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2325 · 2026-05-23T13:11:55.335105+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 2326 · 2026-05-23T13:11:56.743451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2327 · 2026-05-23T13:11:57.703393+00:00_

1	## Review Issues Tracker — policy_ambiguity_safety
2	## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Latest Round: 26
5	
6	# ============================================================
7	# R26 ISSUES — IN PROGRESS (Agent dispatched 2026-05-23)
8	# ============================================================
9	
10	- id: "R26-MF1"
11	  summary: "Type-mechanism dissociation (Contribution 2) 核心证据依赖 LLM 编码标签，人工 κ=0.15 可靠性不足"
12	  category: method
13	  severity: critical
14	  status: in_progress
15	  first_raised_round: 22
16	  last_seen_round: 26
17	  mentions:
18	    - round: 25
19	      reviewers: [1, 2]
20	      note: "R25-W8: §6 仍用 'mechanistically distinct' 等强表述，已修为 'as classified by LLM coders'"
21	    - round: 26
22	      reviewers: [1, 2]
23	      note: "R2 Must-Fix N1, R1 交叉后 AGREE。两个独立 attack vector 汇聚：R1 通过 construct validity (κ=0.653 vs κ=0.15 对比), R2 通过 LLM 分类偏好。共识 Must-Fix"
24	  action_items:
25	    - round: 26
26	      action: "报告 collapsed 4-cat κ=0.36 (SM+SC→policy_misinterpretation)；§6 新增段落讨论 κ=0.15；降级 C2 为 exploratory；abstract 加 LLM-coded 限定词；Discussion 加 κ=1.00 vs κ=0.15 对比"
27	      assigned_to: main_agent
28	      status: in_progress
29	  resolution: ""
30	  resolution_round: null
31	
32	- id: "R26-MF2"
33	  summary: "SESOI ±15pp 对安全研究领域缺乏原则性论证——影响 TOST 等价结构（但不影响 V 对比）"
34	  category: method
35	  severity: critical
36	  status: in_progress
37	  first_raised_round: 20
38	  last_seen_round: 26
39	  mentions:
40	    - round: 25
41	      reviewers: [1, 2]
42	      note: "R24-W4 resolved: 已改为 'pragmatic default, not principled domain-anchored threshold'"
43	    - round: 26
44	      reviewers: [1, 2]
45	      note: "R1 Must-Fix N1, R2 交叉后部分 AGREE 但精确限定范围：V=0.14 不依赖 TOST 阈值，C2 方向性结论不受 SESOI 影响，SESOI 仅影响等价 cluster 结构"
46	  action_items:
47	    - round: 26
48	      action: "TOST 改为多 margin 敏感性分析框架；分离 V 对比（阈值无关）与 TOST 等价结构（阈值依赖）"
49	      assigned_to: main_agent
50	     
…[truncated 13375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 2328 · 2026-05-23T13:11:57.815690+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2329 · 2026-05-23T13:11:58.075758+00:00_

1	\begin{abstract}
2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. Using a matched-pair causal design on $\tau^2$-bench with 300 clause pairs spanning a six-type taxonomy evaluated across five models, we show that ambiguous clauses increase violations by 31.0 percentage points in confound-free types (34.0\,pp overall); cross-benchmark replication on SOPBench confirms directional consistency ($+$12.7\,pp). However, ambiguity \emph{type} predicts \emph{how} agents fail, not \emph{whether} they fail: each type maps to a dominant failure mechanism with $\geq$3/5 cross-model consistency ($V = 0.45$ vs.\ $0.14$, LLM-coded; human $\kappa = 0.38$ collapsed). This \emph{type--mechanism dissociation} establishes the taxonomy as a diagnostic instrument rather than a risk classifier. Error analysis reveals that agents almost never recognize ambiguity and converge on identical policy violations with strong permissive bias, inverting \citeauthor{berry_kamsties_2004}'s divergent-interpretation framework to convergent error. These findings, established under controlled conditions in two customer-service domains, motivate clause-level policy auditing over type-level risk screening.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 260
}
```

</details>

---


### Tool call

_source line 2330 · 2026-05-23T13:11:58.128323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2331 · 2026-05-23T13:11:58.179048+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity---a pilot audit of 407 clauses from 24 production policy documents finds 55--87\% contain at least one ambiguity type (dual-judge $\kappa = 0.30$; range reflects union vs.\ intersection; Appendix~\ref{app:prevalence})---a property studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. Berry and Kamsties define nocuity in terms of stakeholder \emph{divergence}; we retain their harm semantics but document a distinct pattern: LLM agents \emph{converge} on the same incorrect interpretation, making the ambiguity harmful through systematic rather than divergent error (\S\ref{sec:analysis}). In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambi
…[truncated 2855 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2332 · 2026-05-23T13:12:02.801488+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 regarding ARR:

## General Submission Information

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR Submission Policy

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be 
…[truncated 667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 7466
}
```

</details>

---


### Tool call

_source line 2333 · 2026-05-23T13:12:13.296245+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR May cycle submission format page limit anonymity requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR May cycle submission format page limit anonymity requirements"
  }
}
```

</details>

---


### Tool call

_source line 2334 · 2026-05-23T13:12:14.825465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2335 · 2026-05-23T13:12:14.976414+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_l
…[truncated 4393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2336 · 2026-05-23T13:12:15.027525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 2337 · 2026-05-23T13:12:15.482416+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}; cf.\ \citet{poesio_artstein_2005} on ambiguity vs.\ underspecification: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Traditional NLP ambiguity classification focuses on within-sentence phenomena \citep{wasow_ambiguity_2005}; our specification layer captures document-level policy gaps unstudied in the agent context. Our taxonomy provides an organizational framework of six types organized into two layers (Table~\ref{tab:taxonomy}), selected from \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types; full mapping in Appendix~\ref{app:li_mapping}) based on three design criteria: (1)~theoretical attestation in prior RE literature \citep{massey_ambiguity_re_2014,berry_kamsties_2004,drip_r_2026}, (2)~amenability to minimal-pair construction without altering clause semantics beyond the target ambiguity, and (3)~mutual exclusivity for unambiguous IV assignment. Types such as ellipsis and pragmatic implicature were excluded because they resist minimal-pair construction within the single-clause policy format.
7	
8	\begin{table}[t]
9	\centering
10	\footnotesize
11	\caption{Six-type ambiguity taxonomy. Disambiguation channel indicates the primary mechanism required to resolve the ambiguity.}
12	\label{tab:taxonomy}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}llll@{}}
15	\toprule
16	\textbf{Type} & \textbf{Layer} & \textbf{Definition} & \textbf{Disambig.\ Channel} \\
17	\midrule
18	Lexical & Ling. & Word/phrase admits multiple senses & Context \\
19	Scopal & Ling. & Quantifier/operator scope underdetermined & Bracketing \\
20	Coreferential & Ling. & Pronoun/NP referent is ambiguous & Resolution \\
21	Auth.\ Scope &
…[truncated 3182 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 2338 · 2026-05-23T13:12:15.482902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2339 · 2026-05-23T13:12:15.533416+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300; Cohen's $\kappa = 0.95$ on six-type classification); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We
…[truncated 4417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2340 · 2026-05-23T13:12:19.955811+00:00_

Web search results for query: "EMNLP 2026 ARR May cycle submission format page limit anonymity requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, here is the information about EMNLP 2026 ARR May cycle submission requirements:

## Submission Format & Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The page limit is 4 pages for short and 8 for long papers, excluding the ethical considerations and limitations.

## Anonymity Requirements

Following the ACL and ARR policies, there is no anonymity period requirement. However, papers must not include authors' names and affiliations, and self-references that reveal the authors' identities must be avoided.

Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review. That said, the new policy incentivizes anonymous su
…[truncated 519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6659
}
```

</details>

---


### Tool call

_source line 2341 · 2026-05-23T13:12:24.428323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2342 · 2026-05-23T13:12:25.432168+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around three analyses: the binary ambiguity effect (C1), the type partial ordering (C2, including the inconclusive layer effect C3), and the model$\times$type interaction (C4). C1 and C2 are primary supported claims; C3 (layer effect) is inconclusive; C4 (model$\times$type interaction) is exploratory.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{figures/fig_variance_decomposition.pdf}
11	\caption{Variance decomposition of violation rates (temperature $= 0$). Clause identity: 22.4\% (0.4\% between types); condition: 15.8\%; model: 1.0\%; residual: 60.8\%.}
12	\label{fig:variance_decomposition}
13	\end{figure}
14	
15	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity (\S\ref{sec:method}). Figure~\ref{fig:variance_decomposition} decomposes violation-rate variance\footnote{Type III SS; logistic regression (Appendix~\ref{app:regression}) confirms concordant results (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}).}: clause identity explains 22.4\% (0.4\% between types, 22.0\% within), condition 15.8\%, model 1.0\%, and residual 60.8\% ($\sim$15\% stochastic, $\sim$46\% systematic; Appendix~\ref{app:residual}). A permutation test confirms that clause wording---not type membership---drives this variance ($p < 0.001$; Appendix~\ref{app:clause_variance}). The incompleteness effect ($+$49.2\,pp) is an upper bound: the unambiguous variant necessarily adds policy content, introducing an information-addition confound that token-count matching cannot address (Appendix~\ref{app:confound}). Excl
…[truncated 5791 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 2343 · 2026-05-23T13:12:25.482825+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 2344 · 2026-05-23T13:12:25.890023+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_type_mechanism.pdf}
7	\caption{Type--mechanism association (percentage of violation traces per type assigned to each failure mechanism). Each type maps to a dominant mechanism ($\geq$3/5 model consistency), supporting the taxonomy's diagnostic value (NMI $= 0.23$, Cram\'{e}r's $V = 0.45$).}
8	\label{fig:type_mechanism}
9	\end{figure}
10	
11	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
12	
13	We analyze 614 violation traces across all five models, coded into five failure modes (Gwet's AC$_1$ $= 0.62$, $\kappa = 0.52$ \citep{gwet_2014,cohen_1960}). The failure mode coder prompt receives the agent trajectory, policy clause, ground truth, and violation assessment, but does \emph{not} include the ambiguity type label; type is assigned programmatically post hoc. Using LLMs to code LLM failures introduces circularity risk; however, mutual information between type (exogenous) and mechanism labels ($I(\text{type}; \text{mechanism}) = 0.41$ bits, $V = 0.45$; Appendix~\ref{app:type_mechanism}) provides structural evidence against this. Human mechanism coding yields $\kappa = 0.15$ (Appendix~\ref{app:human_validation}), concentrated on the spurious compliance vs.\ structural misparse boundary; collapsing these into a single \emph{policy misinterpretation} category raises $\kappa$ to $0.38$. The type--mechanism association reported here ($V = 0.45$) should therefore be interpreted as an upper bound; the directional pattern---type predicts mechanism more strongly than severity---holds under both LLM and collapsed human coding. The following failure mode patterns should therefore be interpreted as consistent LLM categorization tendencies rather than ground-truth mechanism assignments. Two of the six type--mechanism mappings re
…[truncated 2932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 407
}
```

</details>

---


### Tool call

_source line 2345 · 2026-05-23T13:12:25.990825+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2346 · 2026-05-23T13:12:26.191914+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Type--mechanism dissociation and intervention design.}
5	The central finding is a type--mechanism dissociation: type predicts failure mechanism more strongly than violation rate ($V = 0.45$ vs.\ $0.14$), reframing the taxonomy from risk classifier to diagnostic instrument. The 60.8\% residual reflects clause-level interactions that type-level taxonomies cannot capture (Appendix~\ref{app:residual}), motivating clause-level auditing; prompt-based mitigation is type-dependent (Appendix~\ref{app:mitigation}), reinforcing policy-design over prompt-level fixes. Human $\kappa = 1.00$ for severity vs.\ $0.15$ (collapsed: $0.38$) for mechanism confirms that \emph{what} constitutes a violation is clear but \emph{why} is interpretively harder. Authorization scope is a construct outlier ($\kappa = 0.385$, 52\,pp range); the core type--mechanism mapping (boundary violation, 5/5 models) remains the most unanimous (Appendix~\ref{app:sans_auth}). This paper identifies causal mechanisms, not deployment-ready effect sizes; the SOPBench replication ($+$12.7\,pp vs.\ $+$34.0\,pp; Appendix~\ref{app:sopbench}) confirms directional consistency.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2347 · 2026-05-23T13:12:26.192358+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2348 · 2026-05-23T13:12:26.243238+00:00_

1	\enlargethispage{10\baselineskip}
2	\section{Conclusion}
3	
4	Policy ambiguity increases agent violations by 31.0\,pp in confound-free types ($+$12.7\,pp on SOPBench). The type--mechanism dissociation ($V = 0.45$ vs.\ $0.14$) and $>$89\% disambiguation neglect motivate clause-level policy auditing for similar customer-service settings.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2349 · 2026-05-23T13:12:30.364268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2350 · 2026-05-23T13:12:30.819098+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our ambiguity pairs are synthetically constructed, so the 34.0\,pp effect is an upper bound; the SOPBench replication ($+$12.7\,pp) provides a cross-benchmark lower bound. We evaluate seven API-accessible models across two customer-service domains at temperature $= 0$; other domains, smaller models, and stochastic sampling remain untested. Failure mode coding relies on LLM annotators ($\kappa = 0.52$; human $\kappa = 0.15$, rising to $0.38$ after collapsing the spurious-compliance/structural-misparse boundary), though the coder prompt excludes ambiguity type labels, preventing type--mechanism contamination. At temperature $> 0$, stochastic sampling would likely increase variance in both conditions but is unlikely to eliminate the directional effect, given its magnitude ($+$31.0\,pp confound-free) and cross-model consistency.
5	
6	\section*{Data and Code Availability}
7	The 300 clause pairs, evaluation pipeline, analysis scripts, and raw episode traces will be released upon publication at \url{https://github.com/anonymous/policy-ambiguity-safety}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 2351 · 2026-05-23T13:12:30.819570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2352 · 2026-05-23T13:12:31.327432+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 58800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 2353 · 2026-05-23T13:12:31.478326+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2354 · 2026-05-23T13:12:31.680415+00:00_

1	@inproceedings{li_ambiguity_taxonomy_2024,
2	  title={A Taxonomy of Ambiguity Types for {NLP}},
3	  author={Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.},
4	  booktitle={Proceedings of EACL 2024},
5	  year={2024}
6	}
7	
8	@inproceedings{massey_ambiguity_re_2014,
9	  title={Identifying and Classifying Ambiguity for Regulatory Requirements},
10	  author={Massey, Aaron K. and Rutledge, Richard L. and Ant{\'o}n, Annie I. and Swire, Peter P.},
11	  booktitle={22nd IEEE International Requirements Engineering Conference (RE)},
12	  year={2014},
13	  doi={10.1109/RE.2014.6912250}
14	}
15	
16	@techreport{berry_kamsties_2004,
17	  title={From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook},
18	  author={Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.},
19	  institution={University of Waterloo},
20	  year={2004}
21	}
22	
23	@inproceedings{chantree_2006,
24	  title={Identifying Nocuous Ambiguities in Natural Language Requirements},
25	  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},
26	  booktitle={14th IEEE International Requirements Engineering Conference (RE)},
27	  year={2006}
28	}
29	
30	@incollection{wasow_ambiguity_2005,
31	  title={The Puzzle of Ambiguity},
32	  author={Wasow, Thomas and Perfors, Amy and Beaver, David},
33	  booktitle={Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe},
34	  publisher={CSLI Publications},
35	  year={2005}
36	}
37	
38	@article{kennedy_vagueness_2007,
39	  title={Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives},
40	  author={Kennedy, Christopher},
41	  journal={Linguistics and Philosophy},
42	  volume={30},
43	  number={1},
44	  pages={1--45},
45	  year={2007},
46	  doi={10.1007/s10988-006-9008-0}
47	}
48	
49	@article{willis_nocuous_2008,
50	  title={Automatic Identification of Nocuous Ambiguity},
51	  author={Willis, Alistair and Chantree, Francis and De Roeck
…[truncated 1993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 2355 · 2026-05-23T13:13:08.595514+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool call

_source line 2356 · 2026-05-23T13:13:09.100558+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2357 · 2026-05-23T13:13:26.629467+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18033
}
```

</details>

---


### Tool result

_source line 2358 · 2026-05-23T13:13:26.629892+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 17529
}
```

</details>

---


### Tool call

_source line 2359 · 2026-05-23T13:13:28.642242+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（长文），参考文献不限，Limitations 必须有但不计入页数\n- **模板**: ACL (acl.sty)\n- **匿名规则**: Double-blind\n- **附录**: 允许，审稿人可选择性阅读\n\n## 论文路径\n- LaTeX 源码: `projects/policy_ambiguity_safety/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_27/submitted.pdf`\n\n## 审查侧重\n\n你的审查重点是**方法严谨性**，包括但不限于：\n\n1. **因果推断设计**：matched-pair design 的有效性，是否真正建立了因果关系，confound 控制是否充分\n2. **统计分析**：McNemar test、TOST equivalence、variance decomposition 等统计方法是否正确使用，多重比较校正是否恰当\n3. **评估管道**：cross-judge design 的可靠性，LLM-as-judge 的偏差控制，human validation 的充分性\n4. **控制实验**：perturbation control、within-family replicability 的设计是否足够，incompleteness confound 的处理是否合理\n5. **Claim 与证据的匹配**：每个 Contribution claim (C1-C4) 是否有充分的证据支撑，是否存在过度声称\n6. **可复现性**：实验细节是否足以复现，temperature=0 对结论的影响\n7. **内部一致性**：论文各部分之间的数据引用是否一致，不同 section 中同一指标的报告是否矛盾\n\n请给出结构化审稿意见：\n- **Summary**（2-3 句概述）\n- **Strengths**（逐条列出优点）\n- **Weaknesses**（逐条列出缺点，按严重程度排序：Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（遗漏的方法论相关文献）\n- **Overall Assessment**（评分 + 置信度 + 理由）\n\n评分标准（ARR/EMNLP 2026）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n**立场**：你是严格的审稿人，不是作者的盟友。找出所有方法论问题，不留情面。",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（长文），参考文献不限，Limitations 必须有但不计入页数\n- **模板**: ACL (acl.sty)\n- **匿名规则**: Double-blind\n- **附录**: 允许，审稿人可选择性阅读\n\n## 论文路径\n- LaTeX 源码: `projects/policy_ambiguity_safety/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_27/submitted.pdf`\n\n## 审查侧重\n\n你的审查重点是**方法严谨性**，包括但不限于：\n\n1. **因果推断设计**：matched-pair design 的有效性，是否真正建立了因果关系，confound 控制是否充分\n2. **统计分析**：McNemar test、TOST equivalence、variance decomposition 等统计方法是否正确使用，多重比较校正是否恰当\n3. **评估管道**：cross-judge design 的可靠性，LLM-as-judge 的偏差控制，human validation 的充分性\n4. **控制实验**：perturbation control、within-family replicability 的设计是否足够，incompleteness confound 的处理是否合理\n5. **Claim 与证据的匹配**：每个 Contribution claim (C1-C4) 是否有充分的证据支撑，是否存在过度声称\n6. **可复现性**：实验细节是否足以复现，temperature=0 对结论的影响\n7. **内部一致性**：论文各部分之间的数据引用是否一致，不同 section 中同一指标的报告是否矛盾\n\n请给出结构化审稿意见：\n- **Summary**（2-3 句概述）\n- **Strengths**（逐条列出优点）\n- **Weaknesses**（逐条列出缺点，按严重程度排序：Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（遗漏的方法论相关文献）\n- **Overall Assessment**（评分 + 置信度 + 理由）\n\n评分标准（ARR/EMNLP 2026）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n**立场**：你是严格的审稿人，不是作者的盟友。找出所有方法论问题，不留情面。",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2360 · 2026-05-23T13:13:42.448871+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13806
}
```

</details>

---


### Tool call

_source line 2361 · 2026-05-23T13:13:43.108583+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（长文），参考文献不限，Limitations 必须有但不计入页数\n- **模板**: ACL (acl.sty)\n- **匿名规则**: Double-blind\n- **附录**: 允许，审稿人可选择性阅读\n\n## 论文路径\n- LaTeX 源码: `projects/policy_ambiguity_safety/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_27/submitted.pdf`\n\n## 审查侧重\n\n你的审查重点是**新颖性与完整性**，包括但不限于：\n\n1. **新颖性**：相对于 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等同期工作的增量贡献是否充分\n2. **相关工作覆盖**：是否遗漏重要的相关文献，特别是 ambiguity/underspecification 区分文献、agent safety 最新工作\n3. **Taxonomy 设计**：6 类型分类的理论动机是否充分，11→6 的筛选标准是否透明\n4. **写作质量**：Abstract 信息密度、术语使用一致性（如 \"confound-free\"、\"nocuous\"）、claim 层级是否清晰\n5. **格式合规**：页数、匿名性、Limitations 章节位置和长度、参考文献格式\n6. **贡献与定位**：三个 contributions 的表述是否准确反映证据强度，exploratory vs confirmed 的区分是否清晰\n7. **生态效度**：合成数据 vs 自然数据效应差距（34pp vs 12.7pp）的讨论是否充分，两个 customer-service domain 的泛化性\n8. **术语学**：'ambiguity' 广义使用是否有充分的文献支撑，'nocuous' 的语义反转是否论证充分\n\n请给出结构化审稿意见：\n- **Summary**（2-3 句概述）\n- **Strengths**（逐条列出优点）\n- **Weaknesses**（逐条列出缺点，按严重程度排序：Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度 + 理由）\n\n评分标准（ARR/EMNLP 2026）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n**立场**：你是严格的审稿人，不是作者的盟友。找出所有新颖性和完整性问题，不留情面。",
  "reviewer_id": "2",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（长文），参考文献不限，Limitations 必须有但不计入页数\n- **模板**: ACL (acl.sty)\n- **匿名规则**: Double-blind\n- **附录**: 允许，审稿人可选择性阅读\n\n## 论文路径\n- LaTeX 源码: `projects/policy_ambiguity_safety/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_27/submitted.pdf`\n\n## 审查侧重\n\n你的审查重点是**新颖性与完整性**，包括但不限于：\n\n1. **新颖性**：相对于 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等同期工作的增量贡献是否充分\n2. **相关工作覆盖**：是否遗漏重要的相关文献，特别是 ambiguity/underspecification 区分文献、agent safety 最新工作\n3. **Taxonomy 设计**：6 类型分类的理论动机是否充分，11→6 的筛选标准是否透明\n4. **写作质量**：Abstract 信息密度、术语使用一致性（如 \"confound-free\"、\"nocuous\"）、claim 层级是否清晰\n5. **格式合规**：页数、匿名性、Limitations 章节位置和长度、参考文献格式\n6. **贡献与定位**：三个 contributions 的表述是否准确反映证据强度，exploratory vs confirmed 的区分是否清晰\n7. **生态效度**：合成数据 vs 自然数据效应差距（34pp vs 12.7pp）的讨论是否充分，两个 customer-service domain 的泛化性\n8. **术语学**：'ambiguity' 广义使用是否有充分的文献支撑，'nocuous' 的语义反转是否论证充分\n\n请给出结构化审稿意见：\n- **Summary**（2-3 句概述）\n- **Strengths**（逐条列出优点）\n- **Weaknesses**（逐条列出缺点，按严重程度排序：Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度 + 理由）\n\n评分标准（ARR/EMNLP 2026）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n**立场**：你是严格的审稿人，不是作者的盟友。找出所有新颖性和完整性问题，不留情面。",
    "reviewer_id": "2",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2362 · 2026-05-23T13:13:45.071898+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1963
}
```

</details>

---


### Assistant

_source line 2363 · 2026-05-23T13:13:57.284459+00:00_

**Round 1 已启动。当前状态：**

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ⏳ 审稿中 |
| Reviewer 2（新颖性/完整性） | ⏳ 审稿中 |
| 视觉审查 Agent | ⏳ 运行中 |
| 外部审稿（Stanford Agentic Reviewer） | 未配置，跳过 |

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 221

## Round 221

2 recorded events


### User

_source line 2364 · 2026-05-23T13:21:13.852596+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — 新颖性与完整性审查

### Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"

---

## 总体评分

**Overall**: 3.0 (Findings)
**Confidence**: 4/5 (Quite sure — familiar with agent safety, RE ambiguity, and NLP benchmarking literature)

**一句话总结**: 方法论扎实（matched-pair causal design）但新颖性因同期工作（DRIP-R、PolicyBank、Gur-Arieh et al.）被显著稀释，domain 局限于两个客服场景，核心术语 "nocuous" 的语义反转论证不足。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Matched-pair 设计扎实，但 cross-judge κ=0.653 仅为 moderate，per-type κ 跨度大（0.385–0.875），variance decomposition 显示 clause identity 仅解释 22.4% 方差 |
| Excitement | 2.5/5 | "policy ambiguity → agent errors" 结论可预期；type-mechanism dissociation 有趣但 exploratory（V'=0.45, wide CIs）；同期三篇高度相关工作降低新颖性 |
| Overall | 3.0/5 | Findings 级别：方法论贡献（causal design）值得发表，但不足以达到 Conference 水平 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Nocuous" 术语的语义反转未充分论证

- 具体位置：Section 6.3, Abstract ("inverting Berry et al.'s divergent-interpretation framework to convergent error")
- 问题：Berry & Kamsties (2004) 对 "nocuous ambiguity" 的原始定义是**不同读者产生不同解读**（divergent interpretation），这才是"有害"的原因——因为会导致不一致的实现。本文发现的现象恰恰相反：agents **converge** on the same wrong interpretation（41.3% majority-convergent violations）。这在 Berry 框架下更接近 "innocuous ambiguity"（所有人一致，只是错误地一致）。作者将其命名为 "systematic nocuity" 实质上是重新定义了这个术语。
- 为什么影响接收：标题直接使用 "Nocuous" 一词，如果术语基础不牢固，整个论文的理论定位就有问题。与 Gur-Arieh et al. (2026) 的 "ambiguity collapse" 概念高度重叠，但后者的理论框架更为自洽。
- 建议修改方向：(a) 明确承认这是对 Berry 框架的**扩展**而非**应用**，提出 "convergent nocuity" vs. "divergent nocuity" 的清晰区分；(b) 更深入地讨论与 "ambiguity collapse" (Gur-Arieh et al., 2026) 的关系——两者描述的本质上是同一现象。

**N2** [critical] 相对于同期工作的增量贡献论证不足

- 具体位置：Section 2 (Related Work), Section 7 (Discussion)
- 问题：三篇高度相关的同期工作（2026年4-5月）严重挤压了本文的新颖性空间：
  - **DRIP-R** (Borkakoty et al., May 2026)：同一平台（τ²-bench）、同一domain（retail customer service）、同一核心问题（policy ambiguity → agent failure）。本文声称三点区别（causal design, safety violations vs. decision quality, two-layer taxonomy），但 DRIP-R 同样使用 multi-judge evaluation，同样发现 frontier models systematically disagree on ambiguous scenarios。"safety violations vs. decision quality" 的区分在操作化层面非常薄弱——两者的 ground truth 判定方式高度相似。
  - **Gur-Arieh et al. (2026) "Ambiguity Collapse"**：本文的核心发现（agents converge on same wrong interpretation, disambiguation neglect 4.6%）本质上就是 ambiguity collapse 在 policy execution 场景的实例化。Section 2 引用了此工作但仅一句带过，没有深入讨论本文的 empirical findings 如何与该理论框架对话。
  - **PolicyBank** (Choi et al., April 2026)：直接提出了 mitigation 方案（iterative policy refinement），本文的 Appendix B 也做了简单的 mitigation experiment 但仅为 prompt-based intervention。
- 为什么影响接收：如果审稿人熟悉这三篇工作，会认为本文的贡献主要是 replication with better methodology，而非新 insight。
- 建议修改方向：(a) 在 Related Work 中用专门的 paragraph 详细比较 DRIP-R，具体量化 measurement 差异（不能只列 bullet points）；(b) 明确论述哪些 findings 是仅通过 matched-pair design 才能得出的（DRIP-R 的 correlational design 无法回答的问题）；(c) 将 type-mechanism dissociation 定位为独特贡献时需要更强的效应量和更窄的 CIs。

**N3** [critical] Domain 泛化性严重不足

- 具体位置：Section 4.1 ("τ²-bench... spanning retail and airline customer service domains"), Section 7, Limitations
- 问题：整个实验仅覆盖两个 customer-service domain（retail + airline），且二者在 policy 结构上高度相似（退货/退款/积分规则）。Cross-domain analysis (Appendix Z) 显示 domain 差异仅 26.7pp vs. 其他，但这两个 domain 并不能代表 LLM agent 的广泛应用场景（coding assistants, medical Q&A, financial advisory, legal, HR 等）。SOPBench replication (Appendix AA) 扩展到 banking/healthcare/retail/admin 四个 domain，但效果差异大（retail 26.7pp vs. airline 22.0pp），且 SOPBench 本身是不同的 benchmark 架构。
- 为什么影响接收：论文标题和 Abstract 使用了不限定 domain 的表述 ("LLM Agent Safety")，但实证基础仅限 customer-service。这是 overclaim。
- 建议修改方向：(a) 标题/Abstract 中明确限定 scope（e.g., "in customer-service domains"）；(b) 或者增加至少一个结构上不同的 domain（如有代码生成 policy、医疗 protocol 等）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Taxonomy 11→6 的筛选标准透明度不足

- 具体位置：Section 3, Table 1, Appendix M
- 问题：从 Li et al. (2024b) 的 11-type NLP taxonomy 筛选到 6 类，使用了三个标准（theoretical attestation in RE literature, amenability to minimal-pair construction, mutual exclusivity for unambiguous IV assignment）。但 Appendix M (Table 12) 只列出了映射关系和排除原因的一句话总结，没有展示筛选过程中的具体 judgment calls。例如：
  - **Ellipsis** 被排除（"Subsumed by scopal in policy contexts"），但 ellipsis 在 policy 语境中非常常见（"Items may be returned [within 30 days]" 省略了 "from purchase date" 还是 "from delivery date"）。这个排除决定需要更充分的论证。
  - **Pragmatic implication** 被排除（"Not attested in RE (criterion 1)"），但 Grice 会话含义在 policy 解读中显然存在——用户从 "free shipping on orders over $50" 推断 "$49 orders don't have free shipping" 就是典型的 pragmatic implication。
- 建议：在 Appendix M 中为每个排除类型提供 2-3 个具体的 policy clause 示例，说明为什么它们不能被 minimal-pair 化或为什么它们被其他类型吸收。

**W2** [warning] "Confound-free" 标签过度乐观

- 具体位置：Abstract, Section 5, Section 7
- 问题：论文将排除 incompleteness 后的四种类型称为 "confound-free"，理由是 incompleteness 有 token-count confound（unambiguous variant necessarily adds content）。但 "confound-free" 暗示**所有**混淆变量都已控制——其他四种类型可能存在的 confounds 包括：(a) 句法复杂度差异（ambiguous variant 可能恰好更复杂）；(b) 语义特异性差异；(c) clause 长度虽经 token delta 控制但 Appendix F 的 logistic regression 只是 partial control。
- 建议：改用 "reduced-confound" 或 "token-count-controlled" 等更精确的措辞，明确说明哪些 confounds 被控制了、哪些未被控制。

**W3** [warning] Variance decomposition 削弱因果叙事

- 具体位置：Figure 2, Section 5
- 问题：Figure 2 的 variance decomposition 显示 clause identity 仅解释 22.4% of violation variance，type 解释 0.4%，condition 解释 15.8%，model 解释 1.0%，residual 60.8%。60.8% 的残差方差意味着绝大部分 variation 来自未建模的因素（conversation trajectory, stochasticity 等）。这与 "policy ambiguity consistently increases violations" 的因果叙事存在张力——effect 是 real 的（condition 占 15.8%），但 signal-to-noise ratio 较低。
- 建议：(a) 在 Discussion 中更坦诚地讨论 residual variance 的含义；(b) 考虑报告 ICC(1) 和 ICC(k) 来更直接地表征 measurement reliability；(c) 已有的 ICC 分析在 Appendix AC 中，应在正文中引用。

**W4** [warning] Cross-judge agreement 的 per-type 异质性

- 具体位置：Section 4.4, Appendix G (Table 10)
- 问题：Overall κ=0.653 是 "substantial agreement"（按 Landis & Koch），但 per-type κ 从 authorization scope 的 0.385（仅 fair agreement）到 incompleteness 的 0.875 变化极大。Authorization scope 恰好是 violation rate 最高、variance 最大的类型——这意味着对最关键类型的测量最不可靠。Judge-proxy agreement 在正文中的 34pp within-judge range 暗示单个 judge 的 severity calibration 差异很大。
- 建议：在 Section 4.4 或 Section 5 中明确承认 authorization scope 的 measurement reliability 较低，并讨论这对该类型结论的影响。

**W5** [warning] "Ambiguity" 的广义使用缺乏充分的文献锚定

- 具体位置：Section 3 ("Scope of 'ambiguity'"), Table 1
- 问题：论文明确将 "ambiguity" 扩展到包含 incompleteness，引用 Wasow et al. (2005) 和 Dalpiat et al. (2018) 作为支撑。但在 computational linguistics 主流文献中，ambiguity（一个表达有多个合法解读）与 underspecification/incompleteness（信息缺失）是明确区分的概念（参见 Poesio 1996; van Deemter 2004）。将 incompleteness 归入 "ambiguity" 的做法在 NLP 会议上可能引发 reviewer 的 terminological objection。
- 建议：(a) 在 Section 3 中更明确地引用 ambiguity vs. underspecification 的区分文献并论证为何本文选择 inclusive definition；(b) 考虑使用 "policy underspecification" 作为 umbrella term，将 ambiguity 和 incompleteness 都纳入其下。

---

## 小问题（不影响接收）

- **M1**: Abstract 中 "+12.7pp" 指 SOPBench replication 的 directional consistency，但这个数字在无上下文的情况下含义不清，需要更明确的表述。
- **M2**: Section 5.1 "all six types individually produce significant increases (all p < 10^{-7})" — 300 pairs × 6 types × 5 models，multiple comparison correction 方法应在正文明确说明（目前仅在 Section 4.6 提到 Holm-Bonferroni）。
- **M3**: Figure 1 ("Experimental overview") 的 "Cross-judge Assessment" 部分标注了 "CRITIC" 和 "Classification"，但正文中 CRITIC 的具体 prompt 和评判标准仅在 Appendix 中——考虑在正文中增加一句 high-level 描述。
- **M4**: Table 2 的 caption 中 "Md = mid (68th percentile equivalent)" 的定义不够直观，建议在脚注中解释选择 68th percentile 的理由。
- **M5**: Data and Code Availability section (p.8) 使用 "https://github.com/anonymous/policy-ambiguity-safety" 作为匿名 URL——格式合规，但建议在 camera-ready 中替换为真实 URL。
- **M6**: Appendix AD (Real-World Policy Ambiguity Prevalence) 中的 9 companies / 24 documents 样本量较小，88% ambiguity prevalence rate 的 CI 应当报告。

---

## Questions（需要作者澄清）

**Q1**: Type-mechanism dissociation 的 V'=0.45 (vs. null 0.14) 被描述为 "moderate"，但 Cramér's V 的 effect size 解读标准在文献中并不统一（Cohen 的 medium ≈ 0.3, large ≈ 0.5）。作者使用什么标准将 0.45 定位为支持 "diagnostic instrument" 而非 "risk classifier" 的 reframing？如果 V' 的 CI 下限接近 0.3，这个结论是否还成立？

**Q2**: Disambiguation neglect rate 为 4.6%（278 episodes 中 agent 主动识别 ambiguity 的次数）。这个 metric 的 operationalization 是什么——是 agent 在 response 中使用了 "ambiguous/unclear/uncertain" 等关键词，还是有更 nuanced 的判断标准？

**Q3**: SOPBench replication (Appendix AA) 的 effect size (+33.6pp) 与主实验 (+34.0pp) 非常接近，但 SOPBench 使用了不同的 benchmark 架构和不同的 policy documents。这种 effect size 的一致性是巧合还是有结构性原因？特别是，SOPBench 的 clause pair construction 是否也使用了相同的 minimal-pair methodology？

**Q4**: Appendix AD 的 real-world prevalence study 发现 88% 的 policy clauses 含有 ambiguity，但这个 prevalence 与本文实验的 effect size 之间没有直接桥梁。作者是否考虑过在真实（非 synthetic）ambiguous clauses 上测量 violation rate，以验证 matched-pair 实验的 ecological validity？

**Q5**: 论文使用了 temperature = 0（Section 4.3），这消除了 model 的随机性但也消除了 ambiguity 的一个重要维度——同一 model 在不同 runs 可能对 ambiguous clause 做出不同决策。作者在 Discussion 中提到 "At temperature > 0, stochastic sampling would likely increase variance"（p.8），但没有任何实验支持。是否有 temperature > 0 的 pilot data？

---

## Missing References（遗漏的重要相关工作）

1. **AgentSpec** (Poskitt et al., ICSE 2026) — "Customizable Runtime Enforcement for Safe and Reliable LLM Agents"。与本文的 policy compliance monitoring 直接相关，提供了 runtime enforcement 视角。
2. **Zhu et al. (2025)** — "Ambiguity in LLMs is a concept missing problem" (arXiv:2505.11679)。提出 ambiguity 的本质是 concept gap，与本文的 incompleteness 类型直接相关。
3. **"The Illusion of Certainty"** (arXiv:2511.04418) — 关于 LLM 在 ambiguity 下 uncertainty quantification 失败，与本文的 disambiguation neglect 发现互补。
4. **Poesio (1996)** / **van Deemter (2004)** — ambiguity vs. underspecification 的经典区分文献，在 Section 3 的 terminological discussion 中应当引用。

---

## 主要优势

- **S1**: Matched-pair causal design 是本文最大的方法论优势。在 agent safety 文献中，大多数工作是 correlational 的（观察有 ambiguity 的 policy 下 agent 是否犯错），而非 causal 的。通过 minimal-pair construction 隔离 ambiguity 的 causal effect，这一设计是严谨的。
- **S2**: Type-mechanism dissociation（每种 ambiguity type → 不同的 failure mechanism）是有价值的发现，即使效应量 moderate。这将 taxonomy 从 "分类工具" 提升为 "诊断工具"，对实际的 policy auditing 有指导意义。
- **S3**: Disambiguation neglect 的量化（4.6%）是文献中首次在 agentic policy execution 场景下的实证测量，与 Gur-Arieh et al. 的理论框架形成 theory-evidence 对话。
- **S4**: 实验规模（300 clause pairs × 5 models × 2 conditions = 2,997 episodes）和统计分析的深度（variance decomposition, bootstrap clustering, logistic regression, TOST equivalence testing）远超同类工作。
- **S5**: SOPBench cross-benchmark replication 增加了 findings 的可信度，虽然 domain 仍局限于 customer service。
- **S6**: Appendix 极为详尽（13 pages），包含完整的 clause pair examples、per-type agreement、mitigation experiment、type detection experiment、replication、confound analysis 等，reproducibility 极高。

---

## 总结与建议

本文在方法论上做出了有价值的贡献（matched-pair causal design），实验执行和统计分析质量高。但三个核心问题限制了它达到 Conference 水平：

1. **新颖性**：与 DRIP-R (2026)、Gur-Arieh et al. (2026)、PolicyBank (2026) 的累积重叠使得本文的 marginal contribution 主要是 "better methodology for a known finding"——这在 Findings 级别是合适的，但 Conference 需要更强的新 insight。
2. **术语**："Nocuous" 的语义反转和 "ambiguity" 的广义使用削弱了理论框架的严谨性。
3. **Domain**：仅覆盖 customer-service 的两个子域，不足以支撑 general "LLM Agent Safety" 的定位。

如果作者能 (a) 重新定位术语框架（不再 claim "inverting Berry" 而是 "extending to convergent nocuity"）、(b) 增加至少一个非 customer-service domain、(c) 更深入地论证相对于 DRIP-R 的不可替代贡献，本文有望达到 Borderline Conference (3.5)。

**推荐**: 3.0 — Findings 接收。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2365 · 2026-05-23T13:21:32.765133+00:00_

Reviewer 2 审稿意见已收到（3.0 Findings）。等待 Reviewer 1 审稿意见返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 222

## Round 222

6 recorded events


### User

_source line 2366 · 2026-05-23T13:21:33.877130+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 方法严谨性审查

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**Confidence**: 4 / 5 (相当确定，对实验设计和统计分析方法熟悉)
**一句话总结**: 匹配对因果设计扎实、统计分析全面，但信息添加混淆不仅限于 incompleteness 类型、type-mechanism dissociation 缺乏可靠的人工验证、跨判官类型排序一致性极低 (ρ=0.09) 三个问题共同削弱了类型级别结论的可信度。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | C1 (binary effect) 方法严谨，但 C2 (type ordering) 和 type-mechanism dissociation 的证据链存在多个薄弱环节 |
| Excitement | 3.5 / 5 | 研究问题重要且有实际价值——policy ambiguity → agent safety 是一个未被充分研究的因果链。但核心发现（"模棱两可的指令导致更多违规"）的惊喜度有限 |
| Reproducibility | 4 / 5 | 实验细节充分（模型版本、API 参数、统计方法），承诺开源代码和数据，附录详尽。扣分点：clause pair 构建 pipeline 细节不够（"template-based pipeline" 但未给出 template） |

---

## Summary

本文研究 LLM agent 在自然语言策略规范中遇到歧义时是否会产生安全违规。作者在 τ²-bench 上构建 300 个匹配 clause pair（6 种歧义类型，5 个模型），发现歧义 clauses 使违规率增加 34.0 pp（去除 incompleteness 混淆后 31.0 pp）。论文进一步提出 type-mechanism dissociation（V=0.45 vs 0.14）和 disambiguation neglect（4.6% awareness）等现象。研究设计总体严谨，但类型级别结论的方法论基础存在显著缺陷。

---

## 主要优势 (Strengths)

**S1. 因果设计出色 (C1)**：匹配对设计配合 McNemar 检验是建立因果关系的正确方法。Perturbation control (Δ_perturb = -0.67 pp, 95% CI [-8.0, 6.67]) 有效排除了表面文本变化作为替代解释。Coreferential 类型（词汇完全相同的 pair）提供了无混淆的因果下界 (18.7 pp)。Section 4.2, Section 4.5。

**S2. 统计分析系统且透明**：多重比较校正 (Holm-Bonferroni, Appendix K)、TOST 等价性检验的七个 margin 敏感性分析 (Table A1)、方差分解 (Figure 2, Appendix AC)、ICC 可重复性 (0.919, Section 4.5)——几乎所有统计选择都有合理的 justification 和 sensitivity check。

**S3. Claim 分级合理**：C3 (layer effect) 明确标注 "inconclusive"（p=0.017 vs threshold 0.0125），C4 (model×type interaction) 标注 "exploratory"。这种诚实的 claim 分级在实证研究中值得肯定。Section 5。

**S4. Cross-benchmark replication**：SOPBench 复制 (Appendix AA) 和两个额外模型族 (Appendix E) 提供了方向一致性的证据，扩展了外部效度。

**S5. Authorization scope 的透明处理**：论文多处标注 auth scope 的低 κ (0.385)、高跨模型方差 (52 pp range)、质量审计发现的 borderline pairs (16%)，并系统性地报告了排除 auth scope 后的所有核心分析 (Appendix O)。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 信息添加混淆不仅限于 incompleteness——matched-pair 设计的系统性偏差

- 具体位置：Section 4.2, Appendix Q (Table 13), Appendix S (Table 14 examples)
- 问题：论文将信息添加混淆仅讨论为 incompleteness 的特殊问题（Section 5.1: "The incompleteness effect (+49.2 pp) is an upper bound"），但 Appendix Q 的 clause length 数据表明这是一个系统性问题：authorization scope Δtoken = +36.1 words, incompleteness = +34.6, lexical = +25.7, scopal = +17.8, cond. prec. = +17.5。所有类型的消歧版本都系统性地比歧义版本更长、更具体。Table 14 的 clause pair examples 证实了这一点：例如 scopal 类型的 unambiguous 版本 ("All items in the order are eligible for return except final-sale items and personalized products") 不仅消除了 scope 歧义，还添加了大量具体信息 ("final-sale items and personalized products")。这不是 minimal edit——而是 specificity addition。
- 论文使用 token count 作为 logistic regression 的控制变量 (Appendix H, Table 11)，但 token count 是信息内容的极粗糙代理。token count coefficient 为正 (β=+0.027, p=0.003) 并不能排除信息添加混淆——它只说明更长的文本整体上与更多违规相关，但不能区分"消除歧义"和"添加决策相关信息"这两种不同的因果路径。
- 为什么影响接收：这一混淆影响所有六个类型的效应量解释。如果模型违规减少的部分原因是获得了更多决策相关信息（而非歧义消除），那么 34.0 pp 的因果归因中，"歧义"和"信息不足"的各自贡献无法分离。Coreferential (Δtoken≈0, 18.7 pp) 是唯一干净的估计。
- 建议修改方向：(a) 构建一组"信息等价"的控制条件——添加等量但与歧义无关的信息（如格式化、举例说明不相关条款）；(b) 至少承认所有类型都存在程度不同的信息添加混淆，而非仅将 incompleteness 标记为上界；(c) 将 coreferential 的 18.7 pp 更突出地作为 confound-free 因果效应的锚点。

**N2** [critical] Type-mechanism dissociation 作为 contribution 缺乏可靠的人工验证

- 具体位置：Section 6 (Error Analysis), Appendix AE (Human Validation)
- 问题：Type-mechanism dissociation (V=0.45 vs 0.14) 是论文的核心 contribution 之一（Introduction 第三条贡献），但其证据链有严重缺陷：
  - (a) V=0.45 完全来自 LLM 编码 (Gwet's AC₁=0.62, κ=0.52)，存在 circularity risk——使用同族 LLM 对 LLM 失败模式进行分类；
  - (b) 人工 mechanism 编码的 κ 仅为 0.15（Appendix AE），即使合并分类后也只有 0.38。论文声称 "the type-mechanism dissociation... establishes the taxonomy as a diagnostic instrument"（Abstract），但 diagnostic 价值依赖于 mechanism 标签的可靠性；
  - (c) 论文承认 "human mechanism coding yields κ=0.15... concentrated on the spurious compliance vs. structural misparse boundary"（Section 6），这说明人类标注者认为这两种 failure mode 之间的边界是模糊的——LLM 编码器的高一致性可能反映的是系统性的分类惯例而非真正的语义区分。
- 为什么影响接收：如果 mechanism 标签本身不可靠（人工 κ=0.15），那么 type→mechanism 的映射 (V=0.45) 的 meaningful 程度存疑。将一个基于低可靠性标注的关联作为论文的核心 contribution 之一，在方法论上是有风险的。
- 建议修改方向：(a) 明确将 type-mechanism dissociation 降级为 exploratory/suggestive finding，而非 contribution claim；(b) 提供人工编码在合并后 (4-category, κ=0.38) 的 V 值，与 LLM 编码的 V=0.45 直接对比；(c) 讨论 LLM 编码一致性高于人工编码这一现象本身意味着什么——是 LLM 捕捉到了人类遗漏的模式，还是 LLM 在套用系统性但可能错误的模板？

**N3** [critical] 跨判官组类型排序严重不一致 (ρ=0.09) 动摇 C2 的稳健性

- 具体位置：Appendix R (Within-Judge-Group Type Rankings), Section 5.2
- 问题：两个判官组的类型排序相关性接近零 (Spearman ρ=0.09, p=0.87)。论文将此归因于 authorization scope 的排名反转并排除后得到 ρ=0.90。但这一处理方式存在问题：
  - (a) Authorization scope 是六种类型之一 (16.7%)，不能因为一种类型"不方便"就排除它来声称 ordering 稳健。如果排序需要排除一种类型才能成立，那么它不是六种类型的 ordering，而是五种类型的 ordering；
  - (b) 更根本地，ρ=0.09 揭示了 cross-judge design 对绝对违规率（用于 C2）的影响：GPT-5.4 判 Claude/GPT-4.1/Qwen3，GPT-4.1 判 GPT-5.4/DeepSeek。哪些模型被哪个判官评判的分配不是随机的，且 cross-judge validation (Appendix AB) 显示 Gemini 系统性地比 GPT/Claude 严格 (+8.8 pp)。这说明判官间的严格程度差异是真实的；
  - (c) Section 5.2 中 "three-family cross-judge validation yields concordant type rankings (ρ=0.71–0.89)" 与 "two-group rankings are discordant (ρ=0.09)" 之间的张力未被充分解释——为什么三家族验证一致但两组不一致？
- 为什么影响接收：C2 (type partial ordering) 是论文的 primary supported claim 之一。如果 ordering 对判官分配敏感，那么声称 "incompleteness > mid-tier cluster > coreferential" 的稳健性受到质疑。论文正文 (Section 5.2) 虽然披露了 ρ=0.09，但将其处理为可以通过排除 auth scope 解决的次要问题，而非对 C2 的系统性威胁。
- 建议修改方向：(a) 在正文中更突出地讨论 ρ=0.09 对 C2 的影响，而非仅作为一段 qualification；(b) 使用所有三个判官族的数据重新计算 C2 的 type ordering，报告三者的一致性；(c) 考虑将 C2 从 "primary supported claim" 降级为 "supported with qualification"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] SESOI ±15 pp 缺乏领域锚定，C2 的 cluster structure 是 margin-dependent 的

- 具体位置：Section 4.6, Table A1 (Appendix A)
- 问题：论文承认 ±15 pp "is a pragmatic default, not a principled domain-anchored threshold"（Section 4.6）。Table A1 清楚地显示 cluster structure 随 margin 变化：±10 pp 时只有 3/6 mid-tier pairs 等价；±12 pp 时 5/6；±15 pp 时 6/6。这意味着 "four types form a stable mid-tier cluster" 的结论取决于选择 ±15 pp 而非 ±12 pp 或 ±10 pp。论文虽然提供了 bootstrap cluster analysis 和 margin sensitivity，但正文的主叙事仍然锚定在 ±15 pp。
- 建议：在正文中更明确地说明 cluster structure 的 margin-dependency，或使用 bootstrap cluster analysis 的 AU p-value（目前为 0.47，Appendix I）作为主分析，因为它不依赖预设 margin。

**W2** [warning] SOPBench 复制效果被过度概括

- 具体位置：Abstract, Conclusion, Appendix AA
- 问题：Abstract 和 Conclusion 均引用 "+12.7 pp on SOPBench" 作为 cross-benchmark replication，但 Appendix AA Table 显示：5 个模型中只有 3 个达到 p<0.01，GPT-5.4 是 borderline (p=0.052)，DeepSeek-V3 未达到显著性 (p=0.163, Δ=+5.3 pp)。将 5 个模型的非加权平均 (+12.7 pp) 作为 "confirms directional consistency" 是合理的，但在 abstract 和 conclusion 中不提及 2/5 模型未显著的事实，有选择性报告之嫌。
- 建议：至少在正文中注明 "three of five models reach individual significance" 或 "with varying effect sizes across models"。

**W3** [warning] Clause pair 质量——类型边界可能模糊

- 具体位置：Appendix S (Table 14 clause examples), Section 3
- 问题：Table 14 中 scopal 类型的示例（"All items are eligible for return except restricted categories" vs "All items in the order are eligible for return except final-sale items and personalized products"）看起来更像 vagueness/incompleteness 而非 quantifier scope ambiguity。Scope ambiguity 应涉及 quantifier/operator scope interaction（如 Table 1 的定义 "Quantifier/operator scope underdetermined"），但这个示例中 "restricted categories" 的问题是语义模糊而非 scope 交互。虽然这只是 50 对中的一个示例，但引发对类型纯度的担忧。论文报告 96% 的初始 type assignment agreement (κ=0.95)，但审核标准是 annotator 是否同意 "the ambiguous variant contains exactly one instance of the target type"——如果 annotator 和作者共享对 taxonomy 的理解偏差，高 agreement 不能保证类型边界的客观准确性。
- 建议：在 appendix 中提供每种类型的多个示例（至少 3-5 个），让读者判断类型分配的质量。

**W4** [warning] Temperature=0 下的匹配对设计与 stochastic sampling 的外推

- 具体位置：Section 4.3, Limitations
- 问题：所有实验使用 temperature=0，产生确定性或近确定性输出。ICC 分析 (Appendix AC) 报告 86.5% 的 clause×model cells 产生一致结果。这意味着论文测量的是 LLM 的 "default interpretation"，而非歧义引发的 outcome distribution。在 temperature>0 下，模型可能在同一歧义 clause 上产生不同解释——这正是歧义的核心特征（多种可能的解释）。论文在 Limitations 中提到 "stochastic sampling would likely increase variance in both conditions but is unlikely to eliminate the directional effect"，但这是推测而非证据。
- 建议：即使不做完整实验，至少用少量 pilot data（如 50 clause pairs × 1 model × temperature=0.7 × 5 replicates）提供初步证据。

**W5** [warning] Cramér's V 跨不同表维度的比较

- 具体位置：Section 6, Appendix V (footnote a)
- 问题：Type→mechanism 的 V=0.45 来自 6×3 contingency table，type→violation 的 V=0.14 来自 6×2 table。Cramér's V 的上界取决于 min(r-1, c-1)，因此 6×3 和 6×2 的 V 值不直接可比。论文在 Appendix V 的脚注中承认 "Different table dimensionalities... affect Cramér's V normalization; values are not directly comparable as ratios"，但在 abstract、introduction、discussion 中反复使用 "V=0.45 vs 0.14" 作为核心 headline comparison，未标注此 caveat。
- 建议：在正文中使用 NMI 或其他可跨维度比较的指标作为主比较，或在每次引用时附带 dimensionality caveat。

---

## 小问题（不影响接收）

- **M1**: Table 2 使用 "Tier" 列 (U/M/L) 描述 TOST cluster membership，但 Tier 命名暗示了一种序数关系，而 TOST 只检验等价性——"Cluster" 可能是更准确的术语。
- **M2**: Section 5.1 报告 "conditional OR = 15.1"，Section 4.6 解释这是 "matched-pair odds ratio from McNemar's test on discordant outcomes (n_disc = 580)"。将其称为 "conditional OR" 在流行病学中通常指 conditional logistic regression 的 OR，与 McNemar OR 不同。建议明确使用 "McNemar OR" 或 "discordant-pair OR"。
- **M3**: Appendix AD (prevalence audit) 的 LLM 判官间 κ=0.295 (fair agreement)，其中 Claude 标注 83.8% 为歧义 vs GPT 58.5%。这个巨大的差异说明"歧义"本身是一个主观判断，在支撑 "55-87% contain at least one ambiguity type"（Introduction）的 claim 时应更加谨慎。
- **M4**: Conclusion 仅一句话，过于简略。建议至少增加对 practical implication 和 future work 方向的简短讨论。

---

## Questions（需要作者澄清）

**Q1**: 对于 non-incompleteness 类型（特别是 auth scope Δtoken=+36.1 words, lexical=+25.7 words），消歧版本中添加的信息有多少是"消除歧义所必需的"vs"附带添加的决策相关信息"？是否可以构建一种 intermediate condition——消除歧义但不添加额外决策信息？

**Q2**: Type-mechanism dissociation 的 V=0.45 在使用人工合并后编码 (κ=0.38, 4-category) 重新计算时是多少？如果 V 显著下降，如何调整相关 claim？

**Q3**: Cross-judge design 中 GPT-5.4 评判 3 个模型而 GPT-4.1 评判 2 个模型——这种不对称分配的理由是什么？是否考虑过每个模型都由两个判官评判以消除判官效应？

**Q4**: Within-family replicability ICC=0.919 (Section 4.5) 是仅在 OpenAI 族内计算的。跨 provider 的 ICC 是多少？Kendall's W=0.398 (p=0.072, non-significant) 似乎暗示跨 provider 一致性较低。

**Q5**: Perturbation control (Δ_perturb = -0.67 pp) 测试的是同义词替换和 clause 重排序。但信息添加（information addition）是一种与这两者性质不同的文本变化。是否可以设计一个 "information-addition perturbation control"——添加等量但与歧义无关的信息？

---

## Missing References（方法论相关）

1. **Rosenbaum (2002)** "Observational Studies" — matched-pair design 中 hidden bias sensitivity analysis 的标准方法，论文未讨论 unobserved confound 的敏感性。
2. **McNemar test 在小样本中的行为** — per-type per-model cell 仅 50 对，部分 McNemar 检验的 discordant pair 数量可能很少。建议引用 exact McNemar test 的适用条件。
3. **LLM-as-judge reliability** 的系统性综述（如 Zheng et al. 2024 已引用，但 Huang et al. 2024 "Limitations of LLM as Judge" 可能相关——如果存在）。

---

## Overall Assessment

**评分: 3.5 (Borderline Conference)**

本文的核心贡献——在受控条件下建立 policy ambiguity → safety violation 的因果链 (C1)——方法论扎实、证据充分、效应量大 (31.0 pp confound-free)，已具备 Conference 水平。

但论文的类型级别结论存在三个相互关联的方法论问题：(1) 信息添加混淆是系统性的而非仅限于 incompleteness；(2) type-mechanism dissociation 的核心证据 (V=0.45) 缺乏可靠的人工验证支撑；(3) 跨判官组的类型排序不一致 (ρ=0.09) 对 C2 构成直接威胁。这三个问题都不足以否定 C1，但共同削弱了论文从 "ambiguity causes violations" 向 "ambiguity type predicts failure mechanism" 的跨越。

如果作者能在 camera-ready 中：(a) 在所有类型上更透明地讨论信息添加混淆（而非仅标记 incompleteness），(b) 将 type-mechanism dissociation 明确降级为 exploratory finding，(c) 更突出地讨论 ρ=0.09 对 C2 的影响，本文可达到 Conference 水平。当前版本在类型级别结论上的 overclaiming 使其处于 Borderline Conference 位置。

---

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**: Overall 3.0 (Findings)，Soundness 3.5，Excitement 2.5，Confidence 4/5。

核心问题三个：
1. **"Nocuous" 术语反转**：Berry 原意是 divergent interpretation 为 harmful，本文发现的恰恰是 convergent wrong interpretation，实质上在重新定义术语，与 Gur-Arieh et al. 的 "ambiguity collapse" 高度重叠但未充分讨论
2. **同期工作挤压新颖性**：DRIP-R（同平台、同域）、PolicyBank、Gur-Arieh et al. 三篇 2026 年工作累积覆盖了本文大部分贡献空间，marginal contribution 主要是 "better methodology for a known finding"
3. **Domain 泛化不足**：仅两个 customer-service 子域，但标题/Abstract 使用了 general "LLM Agent Safety" 定位，属于 overclaim

方法论优势（matched-pair causal design、detailed variance decomposition、SOPBench replication）足以支撑 Findings 接收，但不足以达到 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2367 · 2026-05-23T13:22:28.049388+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — 方法严谨性审查\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Confidence**: 4 / 5\n**Soundness**: 3 / 5 | **Excitement**: 3.5 / 5 | **Reproducibility**: 4 / 5\n\n### Must-Fix\n\n**N1** [critical] 信息添加混淆不仅限于 incompleteness——matched-pair 设计的系统性偏差\n- Appendix Q 的 clause length 数据表明所有类型的消歧版本都系统性地更长：auth scope Δtoken=+36.1 words, incompleteness=+34.6, lexical=+25.7, scopal=+17.8, cond. prec.=+17.5。\n- Table 14 的 clause pair examples 证实 scopal 类型的 unambiguous 版本不仅消除了 scope 歧义，还添加了大量具体信息——不是 minimal edit 而是 specificity addition。\n- Token count 作为 logistic regression 控制变量 (Appendix H) 是极粗糙的代理，β=+0.027 不能区分\"消除歧义\"和\"添加决策相关信息\"两种因果路径。\n- Coreferential (Δtoken≈0, 18.7 pp) 是唯一干净的估计。\n- 建议：(a) 构建\"信息等价\"控制条件；(b) 承认所有类型都有信息添加混淆；(c) 将 coreferential 18.7 pp 作为 confound-free 锚点。\n\n**N2** [critical] Type-mechanism dissociation 作为 contribution 缺乏可靠的人工验证\n- V=0.45 完全来自 LLM 编码 (Gwet's AC₁=0.62, κ=0.52)，存在 circularity risk。\n- 人工 mechanism 编码 κ=0.15，合并后 0.38。\n- LLM 编码一致性高于人工可能反映系统性分类惯例而非真正的语义区分。\n- 建议：(a) 降级为 exploratory finding；(b) 提供人工合并后的 V 值；(c) 讨论 LLM vs 人工编码差异的含义。\n\n**N3** [critical] 跨判官组类型排序严重不一致 (ρ=0.09) 动摇 C2\n- 两个判官组类型排序 ρ=0.09 (p=0.87)，排除 auth scope 后 ρ=0.90。\n- 不能因为一种类型\"不方便\"就排除它来声称 ordering 稳健（auth scope 占 16.7%）。\n- Cross-judge design 中模型-判官分配不随机，Gemini 系统性偏严 (+8.8 pp)。\n- Three-family ρ=0.71-0.89 与 two-group ρ=0.09 的张力未充分解释。\n- 建议：(a) 更突出讨论 ρ=0.09；(b) 用三个判官族重算 C2；(c) 考虑降级 C2。\n\n### Should-Fix\n\n**W1**: SESOI ±15 pp 缺乏领域锚定，cluster structure 是 margin-dependent 的。\n**W2**: SOPBench 复制 2/5 模型未显著但 abstract/conclusion 未提及。\n**W3**: Clause pair 质量——scopal 示例更像 vagueness/incompleteness 而非 scope ambiguity。\n**W4**: Temperature=0 下测量的是 default interpretation 而非 outcome distribution。\n**W5**: Cramér's V 跨 6×3 vs 6×2 表维度比较问题，正文反复用 V=0.45 vs 0.14 但未标注 caveat。\n\n### Minor\n- **M1**: \"Tier\" 应改为 \"Cluster\"\n- **M2**: \"conditional OR\" 应改为 \"McNemar OR\"\n- **M3**: Prevalence audit κ=0.295，\"55-87%\" claim 应更谨慎\n- **M4**: Conclusion 过于简略\n\n### Questions\n- **Q1**: Non-incompleteness 类型的消歧版本中，多少信息是\"必需\"vs\"附带\"的？\n- **Q2**: 人工合并后编码的 V 值是多少？\n- **Q3**: Cross-judge 不对称分配的理由？\n- **Q4**: 跨 provider ICC 是多少？\n- **Q5**: 能否设计 information-addition perturbation control？\n\n---\n\n请逐条回应，标注 [AGREE] 或 [REBUT]。",
  "reviewer_id": "2",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — 方法严谨性审查\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Confidence**: 4 / 5\n**Soundness**: 3 / 5 | **Excitement**: 3.5 / 5 | **Reproducibility**: 4 / 5\n\n### Must-Fix\n\n**N1** [critical] 信息添加混淆不仅限于 incompleteness——matched-pair 设计的系统性偏差\n- Appendix Q 的 clause length 数据表明所有类型的消歧版本都系统性地更长：auth scope Δtoken=+36.1 words, incompleteness=+34.6, lexical=+25.7, scopal=+17.8, cond. prec.=+17.5。\n- Table 14 的 clause pair examples 证实 scopal 类型的 unambiguous 版本不仅消除了 scope 歧义，还添加了大量具体信息——不是 minimal edit 而是 specificity addition。\n- Token count 作为 logistic regression 控制变量 (Appendix H) 是极粗糙的代理，β=+0.027 不能区分\"消除歧义\"和\"添加决策相关信息\"两种因果路径。\n- Coreferential (Δtoken≈0, 18.7 pp) 是唯一干净的估计。\n- 建议：(a) 构建\"信息等价\"控制条件；(b) 承认所有类型都有信息添加混淆；(c) 将 coreferential 18.7 pp 作为 confound-free 锚点。\n\n**N2** [critical] Type-mechanism dissociation 作为 contribution 缺乏可靠的人工验证\n- V=0.45 完全来自 LLM 编码 (Gwet's AC₁=0.62, κ=0.52)，存在 circularity risk。\n- 人工 mechanism 编码 κ=0.15，合并后 0.38。\n- LLM 编码一致性高于人工可能反映系统性分类惯例而非真正的语义区分。\n- 建议：(a) 降级为 exploratory finding；(b) 提供人工合并后的 V 值；(c) 讨论 LLM vs 人工编码差异的含义。\n\n**N3** [critical] 跨判官组类型排序严重不一致 (ρ=0.09) 动摇 C2\n- 两个判官组类型排序 ρ=0.09 (p=0.87)，排除 auth scope 后 ρ=0.90。\n- 不能因为一种类型\"不方便\"就排除它来声称 ordering 稳健（auth scope 占 16.7%）。\n- Cross-judge design 中模型-判官分配不随机，Gemini 系统性偏严 (+8.8 pp)。\n- Three-family ρ=0.71-0.89 与 two-group ρ=0.09 的张力未充分解释。\n- 建议：(a) 更突出讨论 ρ=0.09；(b) 用三个判官族重算 C2；(c) 考虑降级 C2。\n\n### Should-Fix\n\n**W1**: SESOI ±15 pp 缺乏领域锚定，cluster structure 是 margin-dependent 的。\n**W2**: SOPBench 复制 2/5 模型未显著但 abstract/conclusion 未提及。\n**W3**: Clause pair 质量——scopal 示例更像 vagueness/incompleteness 而非 scope ambiguity。\n**W4**: Temperature=0 下测量的是 default interpretation 而非 outcome distribution。\n**W5**: Cramér's V 跨 6×3 vs 6×2 表维度比较问题，正文反复用 V=0.45 vs 0.14 但未标注 caveat。\n\n### Minor\n- **M1**: \"Tier\" 应改为 \"Cluster\"\n- **M2**: \"conditional OR\" 应改为 \"McNemar OR\"\n- **M3**: Prevalence audit κ=0.295，\"55-87%\" claim 应更谨慎\n- **M4**: Conclusion 过于简略\n\n### Questions\n- **Q1**: Non-incompleteness 类型的消歧版本中，多少信息是\"必需\"vs\"附带\"的？\n- **Q2**: 人工合并后编码的 V 值是多少？\n- **Q3**: Cross-judge 不对称分配的理由？\n- **Q4**: 跨 provider ICC 是多少？\n- **Q5**: 能否设计 information-addition perturbation control？\n\n---\n\n请逐条回应，标注 [AGREE] 或 [REBUT]。",
    "reviewer_id": "2",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2368 · 2026-05-23T13:22:57.485324+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29435
}
```

</details>

---


### Tool call

_source line 2369 · 2026-05-23T13:22:58.440758+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — 新颖性与完整性审查\n\n**Overall**: 3.0 / 5 (Findings)\n**Confidence**: 4 / 5\n**Soundness**: 3.5 / 5 | **Excitement**: 2.5 / 5\n\n### Must-Fix\n\n**N1** [critical] \"Nocuous\" 术语的语义反转未充分论证\n- Berry & Kamsties (2004) 原始定义是 divergent interpretation 导致 harmful。\n- 本文发现的是 convergent wrong interpretation (41.3% majority-convergent violations)，在 Berry 框架下更接近 innocuous ambiguity。\n- 与 Gur-Arieh et al. (2026) \"ambiguity collapse\" 高度重叠但讨论不足。\n- 标题使用 \"Nocuous\" 但术语基础不牢固。\n- 建议：(a) 明确承认这是 extension 而非 application；(b) 提出 \"convergent nocuity\" vs \"divergent nocuity\" 区分；(c) 深入讨论与 ambiguity collapse 的关系。\n\n**N2** [critical] 相对同期工作增量贡献论证不足\n- DRIP-R: 同平台同域同问题，\"safety violations vs decision quality\" 区分在操作化层面薄弱。\n- Gur-Arieh et al.: disambiguation neglect + convergent error 本质就是 ambiguity collapse 的实例化。\n- PolicyBank: 已提供 mitigation 方案。\n- Marginal contribution 主要是 \"better methodology for a known finding\"。\n- 建议：(a) 专门 paragraph 详细比较 DRIP-R；(b) 论述仅通过 matched-pair 才能得出的 findings；(c) type-mechanism dissociation 需更强效应量。\n\n**N3** [critical] Domain 泛化性严重不足\n- 仅覆盖两个 customer-service domain（retail + airline）。\n- SOPBench 扩展到 4 domain 但效果差异大且是不同 benchmark。\n- 标题/Abstract 使用 general \"LLM Agent Safety\" 定位属于 overclaim。\n- 建议：(a) 标题/Abstract 限定 scope；(b) 或增加非 customer-service domain。\n\n### Should-Fix\n\n**W1**: Taxonomy 11→6 筛选标准透明度不足，ellipsis 和 pragmatic implication 的排除需更充分论证。\n**W2**: \"Confound-free\" 标签过度乐观，应改为 \"reduced-confound\"。\n**W3**: Variance decomposition 60.8% 残差削弱因果叙事，signal-to-noise ratio 较低。\n**W4**: Cross-judge per-type κ 异质性大 (0.385-0.875)，最关键类型测量最不可靠。\n**W5**: \"Ambiguity\" 广义使用缺乏充分文献锚定，应引用 Poesio 1996 / van Deemter 2004。\n\n### Minor\n- **M1**: Abstract \"+12.7pp\" 无上下文含义不清\n- **M2**: Multiple comparison correction 应在正文明确\n- **M3**: Figure 1 \"CRITIC\" 缺 high-level 描述\n- **M4**: Table 2 caption \"Md = mid (68th percentile)\" 不直观\n- **M5**: Anonymous URL 格式合规\n- **M6**: Prevalence audit 样本量小，CI 应报告\n\n### Questions\n- **Q1**: V=0.45 的 CI 下限接近 0.3 时结论是否成立？\n- **Q2**: Disambiguation neglect 的 operationalization 是什么？\n- **Q3**: SOPBench effect size 一致性是巧合还是结构性？\n- **Q4**: 是否考虑过在真实 ambiguous clauses 上测量 violation rate？\n- **Q5**: 是否有 temperature>0 的 pilot data？\n\n### Missing References\n1. AgentSpec (Poskitt et al., ICSE 2026)\n2. Zhu et al. (2025) \"Ambiguity in LLMs is a concept missing problem\"\n3. \"The Illusion of Certainty\" (arXiv:2511.04418)\n4. Poesio (1996) / van Deemter (2004)\n\n---\n\n请逐条回应，标注 [AGREE] 或 [REBUT]。",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — 新颖性与完整性审查\n\n**Overall**: 3.0 / 5 (Findings)\n**Confidence**: 4 / 5\n**Soundness**: 3.5 / 5 | **Excitement**: 2.5 / 5\n\n### Must-Fix\n\n**N1** [critical] \"Nocuous\" 术语的语义反转未充分论证\n- Berry & Kamsties (2004) 原始定义是 divergent interpretation 导致 harmful。\n- 本文发现的是 convergent wrong interpretation (41.3% majority-convergent violations)，在 Berry 框架下更接近 innocuous ambiguity。\n- 与 Gur-Arieh et al. (2026) \"ambiguity collapse\" 高度重叠但讨论不足。\n- 标题使用 \"Nocuous\" 但术语基础不牢固。\n- 建议：(a) 明确承认这是 extension 而非 application；(b) 提出 \"convergent nocuity\" vs \"divergent nocuity\" 区分；(c) 深入讨论与 ambiguity collapse 的关系。\n\n**N2** [critical] 相对同期工作增量贡献论证不足\n- DRIP-R: 同平台同域同问题，\"safety violations vs decision quality\" 区分在操作化层面薄弱。\n- Gur-Arieh et al.: disambiguation neglect + convergent error 本质就是 ambiguity collapse 的实例化。\n- PolicyBank: 已提供 mitigation 方案。\n- Marginal contribution 主要是 \"better methodology for a known finding\"。\n- 建议：(a) 专门 paragraph 详细比较 DRIP-R；(b) 论述仅通过 matched-pair 才能得出的 findings；(c) type-mechanism dissociation 需更强效应量。\n\n**N3** [critical] Domain 泛化性严重不足\n- 仅覆盖两个 customer-service domain（retail + airline）。\n- SOPBench 扩展到 4 domain 但效果差异大且是不同 benchmark。\n- 标题/Abstract 使用 general \"LLM Agent Safety\" 定位属于 overclaim。\n- 建议：(a) 标题/Abstract 限定 scope；(b) 或增加非 customer-service domain。\n\n### Should-Fix\n\n**W1**: Taxonomy 11→6 筛选标准透明度不足，ellipsis 和 pragmatic implication 的排除需更充分论证。\n**W2**: \"Confound-free\" 标签过度乐观，应改为 \"reduced-confound\"。\n**W3**: Variance decomposition 60.8% 残差削弱因果叙事，signal-to-noise ratio 较低。\n**W4**: Cross-judge per-type κ 异质性大 (0.385-0.875)，最关键类型测量最不可靠。\n**W5**: \"Ambiguity\" 广义使用缺乏充分文献锚定，应引用 Poesio 1996 / van Deemter 2004。\n\n### Minor\n- **M1**: Abstract \"+12.7pp\" 无上下文含义不清\n- **M2**: Multiple comparison correction 应在正文明确\n- **M3**: Figure 1 \"CRITIC\" 缺 high-level 描述\n- **M4**: Table 2 caption \"Md = mid (68th percentile)\" 不直观\n- **M5**: Anonymous URL 格式合规\n- **M6**: Prevalence audit 样本量小，CI 应报告\n\n### Questions\n- **Q1**: V=0.45 的 CI 下限接近 0.3 时结论是否成立？\n- **Q2**: Disambiguation neglect 的 operationalization 是什么？\n- **Q3**: SOPBench effect size 一致性是巧合还是结构性？\n- **Q4**: 是否考虑过在真实 ambiguous clauses 上测量 violation rate？\n- **Q5**: 是否有 temperature>0 的 pilot data？\n\n### Missing References\n1. AgentSpec (Poskitt et al., ICSE 2026)\n2. Zhu et al. (2025) \"Ambiguity in LLMs is a concept missing problem\"\n3. \"The Illusion of Certainty\" (arXiv:2511.04418)\n4. Poesio (1996) / van Deemter (2004)\n\n---\n\n请逐条回应，标注 [AGREE] 或 [REBUT]。",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2370 · 2026-05-23T13:23:00.238631+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1797
}
```

</details>

---


### Assistant

_source line 2371 · 2026-05-23T13:23:02.673620+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 223

## Round 223

2 recorded events


### User

_source line 2372 · 2026-05-23T13:23:05.296051+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已将完整审稿意见提交给 Review Director。

核心结论：**Overall 3.5 (Borderline Conference)**

三个 Must-Fix 问题：
1. **信息添加混淆是系统性的**——不仅 incompleteness，所有类型的消歧版本都系统性地添加了大量信息（auth scope +36.1 words, lexical +25.7 words），token count regression 不能有效分离"歧义消除"和"信息添加"两种因果路径
2. **Type-mechanism dissociation (V=0.45) 缺乏人工验证**——人工 mechanism 编码 κ=0.15（合并后 0.38），将基于低可靠性标注的 LLM-coded 关联作为核心 contribution 有方法论风险
3. **跨判官组类型排序 ρ=0.09**——直接威胁 C2 (type partial ordering) 的稳健性，排除 auth scope 后 ρ=0.90 的处理方式是 post-hoc 的

C1 (binary ambiguity effect, +31.0 pp confound-free) 方法论扎实，但从 C1 到类型级别结论的跨越证据不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2373 · 2026-05-23T13:23:16.923643+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 224

## Round 224

2 recorded events


### User

_source line 2374 · 2026-05-23T13:25:33.625929+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 回应

**[AGREE] R2-N1: "Nocuous" 术语的语义反转未充分论证**

同意 R2 的核心论点。论文在 Section 6.3 中承认了反转 ("We adopt 'nocuous' from Berry et al. (2004), but inverted: our agents exhibit convergent rather than divergent errors")，在 Introduction 中也说 "we retain their harm semantics but document a distinct pattern"。但这个反转的论证确实过于简略——仅用一句话完成了对一个领域核心概念的重新定义。

关键问题在于：Berry & Kamsties 框架中，convergent interpretation = innocuous（因为共享理解不会导致分歧）。论文需要更明确地论证为什么在 LLM agent 语境下 convergent wrong interpretation 构成一种新的 harm 模式——即所有模型收敛到同一个错误解释意味着 (a) 没有内部分歧信号来触发人工审查，(b) 错误是系统性的而非随机的。这个论证在论文中隐含但未显化。

R2 建议的 "convergent nocuity" vs "divergent nocuity" 区分是合理的。此外，与 Gur-Arieh et al. (2026) "ambiguity collapse" 的关系确实讨论不足——Related Work (Section 2) 仅一句引用，但 disambiguation neglect 在概念上与 ambiguity collapse 高度重叠，应明确区分两者的范围和贡献。

**[REBUT] R2-N2: 相对同期工作增量贡献论证不足**

部分反驳。R2 将本文的贡献概括为 "better methodology for a known finding"，这低估了因果识别的方法论意义。

具体反驳点：

(a) **DRIP-R 的区分不仅是操作化层面的**。DRIP-R 是 correlational design（Section 2: "DRIP-R's correlational design leaves open whether ambiguity *causes* violations or merely co-occurs with harder scenarios"）。匹配对设计 + perturbation control (Δ_perturb = -0.67 pp, Section 4.5) 建立了因果关系，这不是 "better methodology for a known finding"——而是将 observational association 升级为 causal claim，这在实证研究中是质的提升。此外，DRIP-R 测量 decision quality 而非 safety violations，两者在实际部署中的后果截然不同。

(b) **Disambiguation neglect ≠ ambiguity collapse**。Ambiguity collapse (Gur-Arieh et al.) 描述的是 LLM 将多义输入坍缩为单一表征的认知现象；disambiguation neglect 描述的是 agent 在 policy execution 中不尝试消歧就直接行动的行为现象（Section 6.2: "agents rarely recognize ambiguity, Overall awareness is 4.6%"）。前者是表征层面，后者是行为层面。但 R2 说得对，论文未充分阐述这一区分。

(c) **PolicyBank 提供的 mitigation 方案与本文的研究问题不同**。PolicyBank 研究 iterative policy refinement（"closing 82% of the gap to a human oracle"），而本文研究歧义的因果效应和类型级别的 diagnostic value。两者互补而非重叠。

但我同意 R2 的一个隐含论点：**如果 type-mechanism dissociation 作为核心新颖贡献但缺乏可靠的人工验证（如我在 R1-N2 中指出），那么论文的增量贡献确实会变弱**。因果识别 (C1) 的方法论贡献是真实的，但如果类型级别分析的可靠性受质疑，overall novelty 会下降。

**[AGREE with qualification] R2-N3: Domain 泛化性不足**

部分同意。标题 "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety" 确实暗示了 general 结论，而实验仅覆盖两个 customer-service domain。

但需注意两个 mitigating factor：
- Abstract 明确限定了 scope："These findings, established under controlled conditions in two customer-service domains"（Abstract 末句）；
- SOPBench replication (Appendix AA) 覆盖了 banking、healthcare、retail、administration 四个 domain，提供了跨域方向一致性的证据（尽管如我在 R1-W2 中指出，2/5 模型未显著）。

我不同意这是 "critical" 级别——因为论文在 abstract 中已做了适当限定，且 SOPBench 提供了部分跨域证据。但同意 R2 关于标题修改的建议——添加 "in Customer-Service Domains" 或类似限定语会更准确。将此作为 Should-Fix 而非 Must-Fix 更合适。

---

### Should-Fix 回应

**[REBUT] R2-W1: Taxonomy 11→6 筛选标准透明度不足**

论文在 Section 3 中列出了三个筛选标准："(1) theoretical attestation in prior RE literature, (2) amenability to minimal-pair construction without altering clause semantics beyond the target ambiguity, and (3) mutual exclusivity for unambiguous IV assignment"。Appendix M (Table 12) 提供了完整的 11→6 映射，每种排除类型都有具体理由（如 elliptical: "Fails criterion 2 (construction difficulty)", collective/distributive: "Overlaps scopal (criterion 3)"）。透明度已足够，除非 R2 要求更长的论证（这会占用正文空间）。

**[AGREE] R2-W2: "Confound-free" 标签过度乐观**

强烈同意。这与我的 R1-N1 一致。Appendix Q 的 clause length 数据显示所有类型的消歧版本都系统性更长 (auth scope +36.1, lexical +25.7, scopal +17.8 words)。仅排除 incompleteness 就声称 "confound-free" 忽视了其他类型中同样存在的信息添加混淆。"Reduced-confound" 或 "excluding the most confounded type" 是更准确的描述。

**[REBUT] R2-W3: 60.8% 残差削弱因果叙事**

不同意。高残差不削弱因果推断——匹配对设计的因果识别不依赖于解释总方差的比例，而依赖于 within-pair 比较的有效性。论文在 Appendix AC 中提供了充分的分析：
- ICC(1)=0.749 表明 74.9% 是 between-cell (systematic) 方差，25.1% 是 within-cell (stochastic)；
- 60.8% 残差中约 15.2 pp 是 stochastic noise，约 45.6 pp 是 systematic-but-unmeasured（具体对话轨迹、用户模拟器选择等）；
- 86.5% 的 clause×model cells 产生一致结果（Section AC: "173/200 produce unanimous outcomes across all five replications"）。

残差中的 systematic 部分反映的是 clause-level heterogeneity（不同具体歧义实例的效果不同），这正是匹配对设计所控制的——每个 clause 与自己的消歧版本比较。高残差说明的是 type-level 预测力弱（0.4% between-type variance），这是论文 C2 的 qualification 而非 C1 的缺陷。

**[AGREE] R2-W4: Cross-judge per-type κ 异质性大**

同意。Authorization scope κ=0.385 (Appendix G, Table 10) 而 incompleteness κ=0.875——最具模型异质性的类型测量最不可靠。这与我的 R1-N3 观察一致。论文虽多处标注了 auth scope 的低 κ，但未系统性地讨论 per-type measurement reliability 对 C2 type ordering 的影响。

**[AGREE] R2-W5: "Ambiguity" 广义使用缺乏充分文献锚定**

部分同意。Section 3 有一段 "Scope of 'ambiguity'" 讨论，引用了 Kennedy (2007) 和 Dalpiaz et al. (2018)。但 R2 建议的 Poesio (1996) 和 van Deemter (2004) 是 ambiguity/vagueness/underspecification 区分的核心文献，论文确实应该引用。特别是 authorization scope 更接近 vagueness 而非 ambiguity（论文自己在 Section 3 承认 "Authorization scope overlaps with vagueness"），incompleteness 更接近 underspecification——使用一个 umbrella term 而不引用该区分的经典文献是一个遗漏。

---

### Minor 回应

- **[AGREE] R2-M1**: Abstract "+12.7pp" 确实缺少上下文。应至少注明这是 SOPBench 复制结果且效应量更小。
- **[REBUT] R2-M2**: Multiple comparison correction 在 Section 4.6 已明确提及 ("We apply Holm-Bonferroni correction within three pre-registered test families (Appendix K)")，正文覆盖已足够。
- **[AGREE] R2-M3**: Figure 1 的 "CRITIC" 标签确实缺少解释。
- **[REBUT] R2-M4**: Table 2 caption 的 "Md" 是 "mid-tier" 的缩写，指 TOST equivalence cluster 成员，与 percentile 无关。但如果 R2 理解为 "68th percentile"，说明标签确实不清晰，应改进。
- **[AGREE] R2-M5**: 匿名 URL 格式需确认合规。
- **[AGREE] R2-M6**: Prevalence audit 的 CI 在 Table 22 有报告 ([80.0, 92.5])，但 clause-level prevalence 的 CI 确实缺失。

---

### Questions 回应

**[AGREE] R2-Q1**: V=0.45 的 CI 是一个有效问题。论文未报告 V 的置信区间。如果 CI 下限接近 0.3（medium effect threshold），"diagnostic instrument" 的 claim 会削弱。这与我的 R1-N2 一致——type-mechanism dissociation 的统计不确定性应被报告。

**[REBUT] R2-Q2**: Disambiguation neglect 的 operationalization 在 Section 6.2 和 Appendix W 中有明确定义——"Awareness is coded as the agent explicitly acknowledging policy ambiguity or requesting clarification before acting, among episodes where the agent violated the intended policy interpretation"（Appendix W）。Table 17 给出了按模型和类型的完整分解。这个 operationalization 是清晰的。

**[AGREE] R2-Q3**: SOPBench effect size 的一致性问题值得追问。论文在 Appendix AA 中给出了三个结构性解释（measurement grain, baseline rate compression, interaction depth），但这些是 post-hoc 的——没有实验证据区分哪个因素贡献最大。

**[AGREE] R2-Q4**: 在真实 ambiguous clauses 上测量 violation rate 是一个重要的外部效度问题。Prevalence audit (Appendix AD) 识别了 407 个真实 clauses，但未在 τ²-bench 上测试它们。这会是有价值的 future work。

**[AGREE] R2-Q5**: Temperature>0 的 pilot data 缺失。这与我的 R1-W4 一致。论文在 Limitations 中的推测 ("stochastic sampling would likely increase variance in both conditions") 无实验支撑。

---

### Missing References 回应

- **[AGREE]** Poesio (1996) / van Deemter (2004) 是重要遗漏，如 W5 所述。
- **[AGREE]** Zhu et al. (2025) "Ambiguity in LLMs is a concept missing problem" 与 disambiguation neglect 直接相关。
- **[NEUTRAL]** AgentSpec 和 "Illusion of Certainty" 的相关性需看具体内容，但如果它们讨论 agent specification 和 LLM confidence，则应引用。

---

### 综合评估

R2 的审查侧重新颖性和完整性，与我的方法严谨性审查形成互补。**两份审查在以下问题上收敛**：

1. **Type-mechanism dissociation 的证据强度不足**（R1-N2 从人工验证角度，R2-N2 从增量贡献角度）；
2. **"Confound-free" 标签过度乐观**（R1-N1, R2-W2）；
3. **Temperature>0 的缺失**（R1-W4, R2-Q5）；
4. **Authorization scope 的测量可靠性**（R1-N3, R2-W4）。

主要分歧在于 **C1 (binary causal effect) 的贡献价值**：R2 认为是 "better methodology for a known finding"（3.0/5），我认为因果识别本身是有实质意义的方法论贡献（3.5/5）。匹配对设计 + perturbation control 将 observational association 升级为 causal claim，这不是 incremental improvement——DRIP-R 的 correlational evidence 无法回答 "ambiguity causes violations" 还是 "harder scenarios happen to be ambiguous"。

**我维持 3.5/5 (Borderline Conference)** 的评分。C1 的因果识别是真实贡献，但类型级别结论 (C2, type-mechanism dissociation) 的可靠性问题使论文整体处于 borderline 位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2375 · 2026-05-23T13:25:42.970528+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 225

## Round 225

2 recorded events


### User

_source line 2376 · 2026-05-23T13:25:45.549849+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部审稿意见的逐条回应。核心立场：

- **N1 (nocuous 术语)**: [AGREE]——语义反转论证确实过于简略
- **N2 (增量贡献)**: [REBUT]——因果识别是质的提升而非 incremental improvement，但同意 type-mechanism dissociation 需要更强验证
- **N3 (domain 泛化)**: [AGREE with qualification]——标题应限定 scope，但 SOPBench 提供了部分跨域证据，建议降为 Should-Fix
- 两份审查在 type-mechanism dissociation 证据强度、"confound-free" 标签、temperature=0 限制、auth scope 测量可靠性四个问题上收敛

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2377 · 2026-05-23T13:25:50.719276+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 226

## Round 226

12 recorded events


### User

_source line 2378 · 2026-05-23T13:26:44.360038+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 交叉回应 Reviewer 1 意见

---

### Must-Fix

**[AGREE] R1-N1: 信息添加混淆不仅限于 incompleteness**

同意 R1 的核心论点。论文仅将 incompleteness 标记为有 token-count confound（Section 5.1, "Excluding incompleteness, the confound-free effect is +31.0pp"），但 Appendix Q (Table 13) 的 clause length 数据清楚表明所有类型的 unambiguous variant 都系统性更长：auth scope +36.1 words, lexical +25.7, scopal +17.8。这意味着 "confound-free" 这个标签应用于其余四种类型是不准确的——与我自己 W2 提出的观点一致。

但我要补充一点 R1 未充分考虑的缓解因素：Section 4.5 的 perturbation control（300 episodes 的 synonym substitution + clause reordering，效应 ±0.01pp, p=0.96）表明**一般性的文本修改**不会导致 violation rate 变化。因此，confound 的准确表述不是"任何文本变长都导致效应"，而是"disambiguation 必然伴随 specificity addition，无法分离两种因果路径"。Coreferential（Δtoken≈0, 18.7pp effect）确实是最干净的锚点，R1 的建议将其作为 confound-free 下限是合理的。

不过，我不完全同意 R1 关于 "所有类型都同等受影响" 的隐含前提。Token delta 与 effect size 的相关性值得检验——如果 Δtoken 大的类型 effect 也大，那么信息添加的确是混淆变量；但如果相关性低（例如 auth scope Δtoken 最大但 effect 排名不是最高），则 specificity addition 可能不是效应的主要驱动力。论文应当报告 per-type Δtoken 与 Δviolation rate 的 rank correlation 来定量评估这个 confound。

---

**[AGREE] R1-N2: Type-mechanism dissociation 的 LLM 编码 circularity**

完全同意。这个 circularity 问题在我的审稿中也有体现（我的 W3 关于 variance decomposition 的高残差），但 R1 将其上升到 coding methodology 层面是更尖锐的批评。

核心问题：生成 violation 的同一批 LLMs（GPT-4.1, Claude Sonnet 4.6, Gemini 2.5 Pro）也被用于 failure mechanism 编码。V'=0.45 可能反映的是 LLM 家族共享的分类偏好（例如 GPT 系列可能系统性地将 authorization scope violations 编码为 "boundary violation"），而非 agents 真正以不同方式 fail。

人工编码 κ=0.15（raw），合并后 0.38，仍然远低于 substantial agreement（0.61）。R1 要求提供人工合并后的 V' 值——这是评估 C3 是否成立的关键缺失数据。如果 human-coded V' 远低于 0.45，则 C3 的 evidence 基础严重不足。

论文确实在 Section 2 和 Section 5.2 将 C3 标记为 "exploratory"，但 Abstract 的表述（"each type maps to a dominant failure mechanism with 3.5× cross-model consistency (V' = 0.45 vs. 0.14)"）给人的印象远超 "exploratory"。建议 Abstract 中明确标注 "exploratory, LLM-coded"。

---

**[AGREE] R1-N3: Cross-judge ρ=0.09 动摇 C2**

这是 R1 最强的批评之一，我完全同意。

Section 5.2 报告 two-group type ranking ρ=0.09 (p=0.87)——本质上是零相关。论文的应对策略是：(a) 排除 auth scope 后 ρ=0.90; (b) 转向 three-family cross-validation ρ=0.71-0.89。两种策略都有问题：

(a) **选择性排除**: Auth scope 占 six types 中的 1/6 (16.7%)。排除一个类型来挽救 ordering 稳定性，在 k=6 的情况下尤其不可接受——每个类型都对 rank correlation 有巨大杠杆效应。况且 auth scope 恰好是 violation rate 最高的类型之一（Table 2: overall 41.0% ambiguous），排除它实质上是排除了最重要的观察。

(b) **Three-family vs. two-group**: Three-family 分析（GPT-Claude, GPT-Gemini, Claude-Gemini）的 ρ=0.71-0.89 之所以高，可能是因为 family-level 分析平滑了 individual judge 的噪声。但 C2 的 claim 是关于 type ordering 的**跨判官稳健性**，而 two-group 分析直接测试这一点。用更粗粒度的分析来替代更直接的测试是不恰当的。

我要补充 R1 未充分展开的一个结构性问题：**cross-judge 分配的非随机性**。Section 4.3 提到 GPT-5.4 judges Claude, GPT-4.1, and Qwen3 traces; GPT-4.1 judges GPT-5.4 and DeepSeek traces。这意味着 judge identity 和 model identity 完全交织——ρ=0.09 可能同时反映 type ordering instability 和 judge-model interaction effects。论文未对此进行充分讨论。

综合 R1-N3 和我的 N2（同期工作新颖性），C2 的贡献可靠性被严重削弱。

---

### Should-Fix

**[AGREE] R1-W1: SESOI ±15pp 缺乏领域锚定**

同意。Section 4.6 将 ±15pp 定义为 "pragmatic threshold"（超过 perturbation control upper CI 的 2×），但没有提供 domain-specific 理由说明为什么 15pp 的差异在实际 policy auditing 中有意义。在 customer service 场景中，1pp 的 violation rate 差异可能已经有实际后果（例如 1% 的客户遇到不当退款），而 15pp 的阈值可能过于宽松。这使得 TOST equivalence testing 的结论（四类型 "equivalent at ±15pp"）的实际意义不明确。

---

**[AGREE] R1-W2: SOPBench 复制中 2/5 模型未显著**

同意，这是一个 reporting transparency 问题。Appendix AA (p.19) 明确记载 GPT-5.4 borderline (p=0.052) 和 DeepSeek-V3 non-significant (p=0.16, +5.3pp)，但 Abstract 的 "replication on SOPBench confirms directional consistency (+12.7pp)" 未传达这一信息。尤其是 DeepSeek-V3 的 +5.3pp 效应，在 5 个 model 中最小且不显著——如果 Abstract 声称 "confirms consistency"，应当加注 "across 3/5 models at p<0.01; 2/5 non-significant"。

这也呼应了我自己 N3 的 domain 泛化性批评——SOPBench 的 partial replication 实际上为泛化性提供了**混合**而非**一致**的证据。

---

**[AGREE] R1-W3: Scopal 示例更像 vagueness/incompleteness**

同意，这与我的 W1（taxonomy 筛选透明度不足）一致。Table 14 (Appendix U) 的 scopal 示例中，unambiguous variant 不仅消除了 scope 歧义，还大量添加了具体信息——"The agent must verify the customer's shipping status from returned email orders and returns" vs. 原始的 scope-ambiguous 表述。这使得 "scopal" 这个标签的准确性受到质疑：部分 clause pairs 可能更准确地归类为 scope-vagueness hybrid 或 specificity underspecification。

---

**[AGREE] R1-W4: Temperature=0 的限制**

同意。Temperature=0 下测量的是 argmax interpretation——模型最可能的默认解读。但 safety evaluation 关心的不仅是 modal behavior，还包括 tail risk（低概率但高危害的 interpretations）。这一限制在 Discussion (p.8) 中仅以一句话带过（"At temperature > 0, stochastic sampling would likely increase variance"），没有 empirical support。

不过我要补充：temperature=0 的选择在因果推断中是有方法论理由的——它消除了 stochastic noise，使 matched-pair comparison 更干净。如果 temperature>0，每对 clause pair 需要多次 sampling 才能估计 mean violation rate，这会大幅增加实验成本。所以 temperature=0 是一个合理的 trade-off，但论文应将其作为 limitation 更明确地讨论。

---

**[REBUT] R1-W5: Cramér's V 跨 6×3 vs 6×2 的可比性**

R1 的统计关切有道理但结论过强。Cramér's V 的标准化分母是 min(r-1, c-1)。对于 6×3 (type × 3-class mechanism) 表，分母 = min(5,2) = 2；对于 6×2 (type × binary violation) 表，分母 = min(5,1) = 1。所以 V 的理论上限在两种情况下都是 1.0，只是达到 1.0 所需的 association pattern 不同。

然而，Cramér's V 的**解读**确实受表维度影响——在更大的表中达到同样的 V 值通常需要更强的 association。因此 V=0.45 (6×3) 在某种意义上代表的 association strength 可能**不弱于**对等 6×2 表中的 V=0.45。R1 要求标注 caveat 是合理的，但这个 caveat 如果加上可能反而**强化**而非**削弱** type-mechanism dissociation 的结论——因为在更大表中获得 V=0.45 更难。

建议论文在报告 V' 比较时加一句脚注说明维度差异，但不需要改变结论方向。

---

### Minor

**[AGREE] R1-M1**: "Tier" → "Cluster" 更准确，"tier" 暗示等级排序。

**[AGREE] R1-M2**: "conditional OR" 术语不精确。matched-pair design 使用 McNemar test，对应的 effect size 是 McNemar OR (discordant pairs ratio)，不是 conditional logistic regression 的 OR。应修正术语。

**[AGREE] R1-M3**: Appendix AD 的 prevalence audit κ=0.295 仅为 fair agreement，"55-87%" claim 应当附带 CI 并表述更谨慎。与我的 M6 一致。

**[AGREE] R1-M4**: Conclusion 过于简略。对于一篇有 13 页 appendix 的论文，Section 7 (Discussion) 和 Conclusion 的正文空间应当更充分地总结 implications 和 future work，而非将所有 nuance 推到 appendix。

---

### Questions

**R1-Q1**: 关于 non-incompleteness 类型消歧版本中 "必需 vs. 附带" 信息的比例——这是一个极好的问题，直接关系到 N1 的 confound severity。如果论文能为每种类型计算 "disambiguation-essential tokens" vs. "specificity-addition tokens" 的比例，将极大强化因果推断。我支持 R1 要求作者回答这个问题。

**R1-Q2**: 人工合并后编码的 V 值——这是我在 N2 回应中也提到的关键缺失数据。必须提供。

**R1-Q3**: Cross-judge 非对称分配的理由——我在 N3 的补充中也提到了这个问题。论文应明确解释为什么不使用 full cross-design（每个 judge 评判所有 model traces）。如果是 cost constraint，应当 acknowledge 这引入的 confound。

**R1-Q4**: 跨 provider ICC——这是一个我未提出但非常相关的问题。Appendix AC 的 ICC 分析 (ICC(1)=0.749, ICC(k)=0.282) 显示 single-rater reliability 较低。如果按 provider 分解 ICC，可以评估 judge heterogeneity 的来源。

**R1-Q5**: Information-addition perturbation control——与 Q1 互补。这实质上是要求构造一个 "添加了等量信息但不消除 ambiguity" 的控制条件。这在 revision 中可能难以实现（需要重新设计实验），但至少应当在 Discussion 中讨论其可行性和 implications。

---

## 总结

R1 的三个 Must-Fix 都切中要害：

1. **N1 (信息添加 confound)**: 同意——"confound-free" 标签对四种类型均不准确，coreferential 18.7pp 是更诚实的锚点
2. **N2 (LLM 编码 circularity)**: 同意——C3 的 evidence 过度依赖 LLM 编码，人工验证不足
3. **N3 (ρ=0.09)**: 同意——这是对 C2 最致命的打击，选择性排除 auth scope 不可接受

结合我自己的 Must-Fix（N1 nocuous 术语反转、N2 同期工作增量不足、N3 domain 局限），两位 reviewer 共识形成了一个清晰的图景：**方法论执行质量高，但三个 contributions 的 evidence 基础都存在实质性缺陷——C1 有 confound（R1-N1），C2 有 measurement instability（R1-N3），C3 有 circularity（R1-N2）**。加上新颖性被同期工作稀释（R2-N2），论文目前在 Findings 级别是合适的。

**R1 给出 3.5 (Borderline Conference), 我给出 3.0 (Findings)**。我认为合理的共识区间是 **3.0–3.5**，取决于作者在 revision 中能否回应上述问题。如果作者能 (a) 提供 per-type Δtoken vs. Δviolation 的 rank correlation 来量化信息添加 confound, (b) 报告 human-coded V', (c) 不再选择性排除 auth scope, (d) 在 Abstract 中明确 C3 为 exploratory 且 LLM-coded, 则 3.5 可达；否则维持 3.0。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2379 · 2026-05-23T13:27:21.047335+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2380 · 2026-05-23T13:27:21.348945+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T13:13:16.953370+00:00\", \"completed_at\": \"2026-05-23T13:17:41.255366+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 23\", \"message\": \"最后一页仅 5 行文字（约 5% 页面），其余全部空白。审稿人翻到最后一页会留下\\\"内容不充实\\\"的负面印象。建议将 Appendix AE 的末尾内容向前合并，或在该页补充内容使占比 ≥ 2/3\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Display item 过度拥挤：Table 2 + Figure 3 + Figure 4 三个 display item 挤在同一页，文字说明空间被严重压缩。Figure 3 和 Figure 4 的内部文字因压缩而偏小。建议将 Figure 4 移至 page 8 或合并为 subfigure\"}, {\"severity\": \"warning\", \"dimension\": \"page 13\", \"message\": \"附录 6 张表格（Tables 4-9）挤在同一页，表格间距极小，可读性下降。虽是附录，审稿人仍需参考这些表格\"}, {\"severity\": \"warning\", \"dimension\": \"page 18\", \"message\": \"附录 5 张表格（Tables 14-18）挤在同一页，Table 14（示例 clause pairs）尤其密集，字号偏小\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 内部文字偏小（模型名称、pipeline 标签），在打印或缩放场景下可能阅读困难。建议适当增大 figure 内文字或简化标签\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3（per-type effect sizes forest plot）y 轴标签和置信区间数值字号较小，建议字号 ≥ 正文 70%\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4（violation rates by model × type heatmap）因页面空间受限被压缩，cell 内数字偏小\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 的 caption 较长但信息充分，自包含性良好；颜色方案（蓝/橙/灰色调）可区分但建议验证色盲友好性\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"主文在 page 9 约 50% 处结束进入 References，主文部分约 8.5 页，符合 EMNLP 8 页限制（Limitations + References 不计入）\"}], \"counts\": {\"critical\": 1, \"warning\": 3, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2381 · 2026-05-23T13:27:21.349458+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2382 · 2026-05-23T13:27:21.400641+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2383 · 2026-05-23T13:28:21.570336+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2384 · 2026-05-23T13:28:21.620984+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2385 · 2026-05-23T13:34:10.898166+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 27\n\n# ============================================================\n# R27 MUST-FIX — OPEN\n# ============================================================\n\n- id: \"R27-MF1\"\n  summary: \"信息添加混淆是系统性的，'confound-free' 标签对非 incompleteness 类型同样不准确\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-MF3: incompleteness confound 控制方法论不充分——token count 作为信息内容 proxy 有根本缺陷\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W2 共识。范围扩大：Appendix Q 显示所有类型 unambiguous variant 系统性更长 (auth scope +36.1, lexical +25.7, scopal +17.8 words)。Token count regression 不能分离 disambiguation vs information-addition。Coreferential (Δtoken≈0, 18.7pp) 是唯一干净估计。应报告 per-type Δtoken vs Δviolation rate rank correlation\"\n  action_items:\n    - round: 27\n      action: \"承认所有类型信息添加混淆；改 confound-free → reduced-confound；报告 Δtoken-Δviolation rank correlation；突出 coreferential 18.7pp 作为 confound-free 下限\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-MF2\"\n  summary: \"Type-mechanism dissociation (V=0.45) 核心证据依赖 LLM 编码，人工 κ=0.15 (collapsed 0.38) 不足以支撑 contribution claim\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-MF1: construct validity 和 LLM 分类偏好两个 attack vector 汇聚\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-N2 提出，R2 完全 AGREE。V=0.45 完全来自 LLM 编码 (Gwet's AC₁=0.62, κ=0.52)，circularity risk——同族 LLM 编码 LLM 失败模式。Abstract 表述给人印象远超 exploratory。需提供 human-coded (4-cat, κ=0.38) V 值\"\n  action_items:\n    - round: 27\n      action: \"降级 C3 为 exploratory；Abstract 标注 'exploratory, LLM-coded'；报告 human-coded V'；讨论 LLM vs human 编码差异含义\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-MF3\"\n  summary: \"跨判官组类型排序 ρ=0.09 威胁 C2 (type partial ordering) 稳健性\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-N3 提出，R2 完全 AGREE。Two-group ρ=0.09 (p=0.87)，排除 auth scope 后 ρ=0.90——但 auth scope 占 16.7%，选择性排除不可接受。Judge-model identity 完全交织。Three-family ρ=0.71-0.89 与 two-group ρ=0.09 张力未充分解释。R2 补充：cross-judge 分配的非随机性加剧问题\"\n  action_items:\n    - round: 27\n      action: \"正文充分讨论 ρ=0.09 对 C2 的影响（非 qualification）；用三个判官族重算 C2 type ordering；承认 auth scope 杠杆效应；考虑降级 C2\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-MF4\"\n  summary: \"'Nocuous' 术语语义反转（divergent→convergent）论证不足，与 ambiguity collapse 讨论不充分\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-SF1: Introduction 已加 convergent vs divergent 句，但 R2 认为仍为 Must-Fix，R1 交叉 REBUT→Should-Fix\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 完全 AGREE。Berry 原意 divergent=harmful，本文 convergent wrong interpretation 在 Berry 框架下更接近 innocuous。仅一句话完成术语重定义。与 Gur-Arieh et al. ambiguity collapse 高度重叠但 Related Work 仅一句引用。标题使用 Nocuous 但基础不牢\"\n  action_items:\n    - round: 27\n      action: \"Introduction 扩展论证 convergent nocuity vs divergent nocuity；深入讨论与 ambiguity collapse 的关系（表征层面 vs 行为层面）；考虑 convergent nocuity 术语\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R27 SHOULD-FIX — OPEN\n# ============================================================\n\n- id: \"R27-SF1\"\n  summary: \"相对同期工作 (DRIP-R, Gur-Arieh, PolicyBank) 增量贡献需更充分论证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-SF4: 需显式阐述 causal design 改变了什么\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2-N2 提出 (critical)，R1 部分 REBUT→Should-Fix。R1 论证：因果识别是质的提升（correlational→causal），非 incremental improvement。但 R1 同意：如果 type-mechanism dissociation 缺乏验证 (MF2)，overall novelty 下降。共识降为 Should-Fix\"\n  action_items:\n    - round: 27\n      action: \"Related Work 详细比较 DRIP-R（量化 measurement 差异）；论述 matched-pair 独有发现；区分 disambiguation neglect 与 ambiguity collapse\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-SF2\"\n  summary: \"标题/Abstract domain scope 应限定为 customer-service\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2-N3 提出 (critical)，R1 AGREE with qualification→Should-Fix。标题 'LLM Agent Safety' 暗示 general 结论但仅两个 customer-service domain。Abstract 末句已限定，SOPBench 提供部分跨域证据。R1 建议标题加 domain 限定语\"\n  action_items:\n    - round: 27\n      action: \"标题添加 domain 限定（如 'in Customer-Service Domains'）；或在 Abstract 首句即限定 scope\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-SF3\"\n  summary: \"SESOI ±15pp 缺乏领域锚定，cluster structure margin-dependent\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-MF2: 已改为 pragmatic default 但仍影响 TOST 等价结构\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2 AGREE。Table A1 显示 cluster structure 随 margin 变化 (±10pp 3/6, ±12pp 5/6, ±15pp 6/6)。正文锚定 ±15pp 但无 domain-specific 理由\"\n  action_items:\n    - round: 27\n      action: \"正文明确 cluster structure margin-dependency；考虑 bootstrap AU p-value 或多 margin 框架作为主分析\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-SF4\"\n  summary: \"SOPBench 复制 2/5 模型未显著但 Abstract/Conclusion 未披露\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2 AGREE。GPT-5.4 borderline (p=0.052), DeepSeek-V3 non-significant (p=0.163, +5.3pp)。Abstract 'confirms directional consistency' 未注明部分模型未显著\"\n  action_items:\n    - round: 27\n      action: \"Abstract/Conclusion 注明 '3/5 models at p<0.01; 2/5 non-significant'\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-SF5\"\n  summary: \"'Ambiguity' 广义使用需引用 underspecification 区分文献 (Poesio, van Deemter)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-SF5: 需 Poesio & Artstein (2005) + policy specification 限定词\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2-W5 + R1 AGREE。Auth scope 更接近 vagueness，incompleteness 更接近 underspecification。Poesio 1996 / van Deemter 2004 是核心区分文献，当前未引用\"\n  action_items:\n    - round: 27\n      action: \"Section 3 引用 Poesio / van Deemter；明确论证 inclusive definition 的理由\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-SF6\"\n  summary: \"Temperature=0 限制需更充分讨论——测量 default interpretation 非 outcome distribution\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-SF6: Limitations 已增加方向性讨论但不够\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2 AGREE。Safety evaluation 应关心 tail risk。Limitations 推测无实验支撑。R2 补充：temp=0 在因果推断中有方法论理由但应更明确讨论 trade-off\"\n  action_items:\n    - round: 27\n      action: \"Limitations 扩展 temperature=0 讨论；承认 tail risk 未覆盖；讨论 trade-off\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-SF7\"\n  summary: \"Clause pair 类型纯度——scopal 示例更像 vagueness/incompleteness\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2 AGREE。Table 14 scopal 示例不是 quantifier scope interaction 而是语义模糊。高 annotator agreement (κ=0.95) 可能反映共享理解偏差而非客观准确性\"\n  action_items:\n    - round: 27\n      action: \"Appendix 提供每种类型更多示例 (3-5 个)；检查 scopal 类型中可能的 cross-type contamination\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R27 MINOR — OPEN\n# ============================================================\n\n- id: \"R27-M1\"\n  summary: \"术语修正：Tier→Cluster, conditional OR→McNemar OR\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-M1/M2, 两位共识\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-M2\"\n  summary: \"Conclusion 过于简略（一句话），应扩展 implications 和 future work\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-M4, R2 交叉 AGREE\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-M3\"\n  summary: \"Prevalence audit κ=0.295，'55-87%' claim 应附带 CI 并更谨慎\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-M3 + R2-M6 共识\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-M4\"\n  summary: \"Cramér's V 跨 6×3 vs 6×2 比较应标注 dimensionality caveat\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 部分 REBUT：caveat 可能反而强化结论（更大表中获得 V=0.45 更难）。共识：标注 caveat 但不改变结论方向\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R26 ISSUES — 本轮未被 Reviewer 提及（可能已修复，待确认）\n# ============================================================\n\n- id: \"R26-SF2\"\n  summary: \"Authorization scope construct difficulty 需在正文讨论\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"Discussion 扩展 auth scope outlier 句，加 construct difficulty 解释\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未作为独立 issue 提及，部分内容被 R27-MF3 (ρ=0.09) 吸收。可能已修复，待 Research Director 确认\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF7\"\n  summary: \"Taxonomy 11→6 选择标准需透明报告实际构造困难\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"表格存在但排除理由不够诚实\"\n    - round: 27\n      reviewers: []\n      note: \"R2-W1 提出透明度不足但被 R1 REBUT（现有三标准+Appendix M 足够）。本轮未达共识，可能已充分处理\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF8\"\n  summary: \"Abstract 信息密度过高——精简至 2-3 个核心数字\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"精简至 ~170 词，保留 4 个核心数字\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未作为独立 issue 提及。R27-M5 关注 '+12.7pp' 上下文但非密度问题。可能已修复\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF9\"\n  summary: \"跨 provider 可复现性需显式量化指标\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"报告 Kendall's W；§4.4 限定 ICC claim 为 within-family\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未作为独立 issue 提及。R1-Q4 追问跨 provider ICC 但未升级为 weakness。可能已充分处理\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M1\"\n  summary: \"'Confound-free' 术语不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"两位独立标记\"\n    - round: 27\n      reviewers: []\n      note: \"被 R27-MF1 吸收——现在是改术语本身 (confound-free→reduced-confound) 而非统一用法\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M2\"\n  summary: \"Violation severity κ=1.00 vs failure mechanism κ=0.15 对比值得正文讨论\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"直接支撑 MF1 论点\"\n    - round: 27\n      reviewers: []\n      note: \"被 R27-MF2 吸收——人工验证不足是 type-mechanism dissociation 的核心问题\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R25 ISSUES — RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R25-W5\"\n  summary: \"C3 inconclusive 但 taxonomy 仍按 two-layer 组织\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 24\n  last_seen_round: 25\n  resolution: \"Changed wording to 'organizational framework' and 'design hypothesis'. R26 did not re-raise.\"\n  resolution_round: 26\n\n- id: \"R25-W7\"\n  summary: \"60.8% 残差方差系统性部分未讨论来源\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 24\n  last_seen_round: 25\n  resolution: \"Added clause-level interactions explanation. R26 did not re-raise.\"\n  resolution_round: 26\n\n- id: \"R25-M2\"\n  summary: \"Disambiguation neglect 增量贡献需更明确阐述\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"Rewritten as extending ambiguity collapse to agentic context. R26 did not re-raise.\"\n  resolution_round: 26\n\n- id: \"R25-M3\"\n  summary: \"References 中 arXiv preprint 格式不统一\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"All entries consistently formatted\"\n  resolution_round: 25\n\n# ============================================================\n# R24 ISSUES — RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R24-N1\"\n  summary: \"Novelty framing 偏强\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Contributions rewritten\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 25\n\n- id: \"R24-N2\"\n  summary: \"Incompleteness confound framing 不够突出\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Abstract leads with confound-free 31.0pp\"\n  resolution_round: 25\n  first_raised_round: 21\n  last_seen_round: 24\n\n- id: \"R24-W2\"\n  summary: \"Template pipeline 不透明\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Appendix S added\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W4\"\n  summary: \"SESOI ±15pp justification 不够 principled\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Changed to 'pragmatic default'. Note: R27 re-raises as SF3\"\n  resolution_round: 25\n  first_raised_round: 20\n  last_seen_round: 27\n\n- id: \"R24-W6\"\n  summary: \"Human validation per-type CI 极宽\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Qualifier added\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W8\"\n  summary: \"NMI cardinality 不对称\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Changed to 'substantially more strongly'\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M4\"\n  summary: \"C3/C4 claim 层级暗示同等级\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Labeled C3 inconclusive, C4 exploratory\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M5\"\n  summary: \"Table 2 脚注缺 per-type 样本量\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added n≈17\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M6\"\n  summary: \"Prevalence audit κ=0.295 未在 Introduction 标注\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added dual-judge κ = 0.30\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X1\"\n  summary: \"ICC≈0 应改为 uninformative due to floor effects\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Reworded with floor effect explanation\"\n  resolution_round: 25\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R24-X3\"\n  summary: \"Limitations 过长\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"Compressed to 3 points\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X4\"\n  summary: \"Limitations 内部矛盾\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Removed underway, replaced with actual results\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 27\n\n# ============================================================\n# R27 MUST-FIX — OPEN\n# ============================================================\n\n- id: \"R27-MF1\"\n  summary: \"信息添加混淆是系统性的，'confound-free' 标签对非 incompleteness 类型同样不准确\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-MF3: incompleteness confound 控制方法论不充分——token count 作为信息内容 proxy 有根本缺陷\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W2 共识。范围扩大：Appendix Q 显示所有类型 unambiguous variant 系统性更长 (auth scope +36.1, lexical +25.7, scopal +17.8 words)。Token count regression 不能分离 disambiguation vs information-addition。Coreferential (Δtoken≈0, 18.7pp) 是唯一干净估计。应报告 per-type Δtoken vs Δviolation rate rank correlation\"\n  action_items:\n    - round: 27\n      action: \"承认所有类型信息添加混淆；改 confound-free → reduced-confound；报告 Δtoken-Δviolation rank correlation；突出 coreferential 18.7pp 作为 confound-free 下限\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-MF2\"\n  summary: \"Type-mechanism dissociation (V=0.45) 核心证据依赖 LLM 编码，人工 κ=0.15 (collapsed 0.38) 不足以支撑 contribution claim\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-MF1: construct validity 和 LLM 分类偏好两个 attack vector 汇聚\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-N2 提出，R2 完全 AGREE。V=0.45 完全来自 LLM 编码 (Gwet's AC₁=0.62, κ=0.52)，circularity risk——同族 LLM 编码 LLM 失败模式。Abstract 表述给人印象远超 exploratory。需提供 human-coded (4-cat, κ=0.38) V 值\"\n  action_items:\n    - round: 27\n      action: \"降级 C3 为 exploratory；Abstract 标注 'exploratory, LLM-coded'；报告 human-coded V'；讨论 LLM vs human 编码差异含义\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-MF3\"\n  summary: \"跨判官组类型排序 ρ=0.09 威胁 C2 (type partial ordering) 稳健性\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-N3 提出，R2 完全 AGREE。Two-group ρ=0.09 (p=0.87)，排除 auth scope 后 ρ=0.90——但 auth scope 占 16.7%，选择性排除不可接受。Judge-model identity 完全交织。Three-family ρ=0.71-0.89 与 two-group ρ=0.09 张力未充分解释。R2 补充：cross-judge 分配的非随机性加剧问题\"\n  action_items:\n    - round: 27\n      action: \"正文充分讨论 ρ=0.09 对 C2 的影响（非 qualification）；用三个判官族重算 C2 type ordering；承认 auth scope 杠杆效应；考虑降级 C2\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-MF4\"\n  summary: \"'Nocuous' 术语语义反转（divergent→convergent）论证不足，与 ambiguity collapse 讨论不充分\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 24\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-SF1: Introduction 已加 convergent vs divergent 句，但 R2 认为仍为 Must-Fix，R1 交叉 REBUT→Should-Fix\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 完全 AGREE。Berry 原意 divergent=harmful，本文 convergent wrong interpretation 在 Berry 框架下更接近 innocuous。仅一句话完成术语重定义。与 Gur-Arieh et al. ambiguity collapse 高度重叠但 Related Work 仅一句引用。标题使用 Nocuous 但基础不牢\"\n  action_items:\n    - round: 27\n      action: \"Introduction 扩展论证 convergent nocuity vs divergent nocuity；深入讨论与 ambiguity collapse 的关系（表征层面 vs 行为层面）；考虑 convergent nocuity 术语\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R27 SHOULD-FIX — OPEN\n# ============================================================\n\n- id: \"R27-SF1\"\n  summary: \"相对同期工作 (DRIP-R, Gur-Arieh, PolicyBank) 增量贡献需更充分论证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-SF4: 需显式阐述 causal design 改变了什么\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2-N2 提出 (critical)，R1 部分 REBUT→Should-Fix。R1 论证：因果识别是质的提升（correlational→causal），非 incremental improvement。但 R1 同意：如果 type-mechanism dissociation 缺乏验证 (MF2)，overall novelty 下降。共识降为 Should-Fix\"\n  action_items:\n    - round: 27\n      action: \"Related Work 详细比较 DRIP-R（量化 measurement 差异）；论述 matched-pair 独有发现；区分 disambiguation neglect 与 ambiguity collapse\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-SF2\"\n  summary: \"标题/Abstract domain scope 应限定为 customer-service\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2-N3 提出 (critical)，R1 AGREE with qualification→Should-Fix。标题 'LLM Agent Safety' 暗示 general 结论但仅两个 customer-service domain。Abstract 末句已限定，SOPBench 提供部分跨域证据。R1 建议标题加 domain 限定语\"\n  action_items:\n    - round: 27\n      action: \"标题添加 domain 限定（如 'in Customer-Service Domains'）；或在 Abstract 首句即限定 scope\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-SF3\"\n  summary: \"SESOI ±15pp 缺乏领域锚定，cluster structure margin-dependent\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-MF2: 已改为 pragmatic default 但仍影响 TOST 等价结构\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2 AGREE。Table A1 显示 cluster structure 随 margin 变化 (±10pp 3/6, ±12pp 5/6, ±15pp 6/6)。正文锚定 ±15pp 但无 domain-specific 理由\"\n  action_items:\n    - round: 27\n      action: \"正文明确 cluster structure margin-dependency；考虑 bootstrap AU p-value 或多 margin 框架作为主分析\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-SF4\"\n  summary: \"SOPBench 复制 2/5 模型未显著但 Abstract/Conclusion 未披露\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2 AGREE。GPT-5.4 borderline (p=0.052), DeepSeek-V3 non-significant (p=0.163, +5.3pp)。Abstract 'confirms directional consistency' 未注明部分模型未显著\"\n  action_items:\n    - round: 27\n      action: \"Abstract/Conclusion 注明 '3/5 models at p<0.01; 2/5 non-significant'\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-SF5\"\n  summary: \"'Ambiguity' 广义使用需引用 underspecification 区分文献 (Poesio, van Deemter)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-SF5: 需 Poesio & Artstein (2005) + policy specification 限定词\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2-W5 + R1 AGREE。Auth scope 更接近 vagueness，incompleteness 更接近 underspecification。Poesio 1996 / van Deemter 2004 是核心区分文献，当前未引用\"\n  action_items:\n    - round: 27\n      action: \"Section 3 引用 Poesio / van Deemter；明确论证 inclusive definition 的理由\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-SF6\"\n  summary: \"Temperature=0 限制需更充分讨论——测量 default interpretation 非 outcome distribution\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 27\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26-SF6: Limitations 已增加方向性讨论但不够\"\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2 AGREE。Safety evaluation 应关心 tail risk。Limitations 推测无实验支撑。R2 补充：temp=0 在因果推断中有方法论理由但应更明确讨论 trade-off\"\n  action_items:\n    - round: 27\n      action: \"Limitations 扩展 temperature=0 讨论；承认 tail risk 未覆盖；讨论 trade-off\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-SF7\"\n  summary: \"Clause pair 类型纯度——scopal 示例更像 vagueness/incompleteness\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2 AGREE。Table 14 scopal 示例不是 quantifier scope interaction 而是语义模糊。高 annotator agreement (κ=0.95) 可能反映共享理解偏差而非客观准确性\"\n  action_items:\n    - round: 27\n      action: \"Appendix 提供每种类型更多示例 (3-5 个)；检查 scopal 类型中可能的 cross-type contamination\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R27 MINOR — OPEN\n# ============================================================\n\n- id: \"R27-M1\"\n  summary: \"术语修正：Tier→Cluster, conditional OR→McNemar OR\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-M1/M2, 两位共识\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-M2\"\n  summary: \"Conclusion 过于简略（一句话），应扩展 implications 和 future work\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-M4, R2 交叉 AGREE\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-M3\"\n  summary: \"Prevalence audit κ=0.295，'55-87%' claim 应附带 CI 并更谨慎\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-M3 + R2-M6 共识\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-M4\"\n  summary: \"Cramér's V 跨 6×3 vs 6×2 比较应标注 dimensionality caveat\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 部分 REBUT：caveat 可能反而强化结论（更大表中获得 V=0.45 更难）。共识：标注 caveat 但不改变结论方向\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R26 ISSUES — 本轮未被 Reviewer 提及（可能已修复，待确认）\n# ============================================================\n\n- id: \"R26-SF2\"\n  summary: \"Authorization scope construct difficulty 需在正文讨论\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"Discussion 扩展 auth scope outlier 句，加 construct difficulty 解释\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未作为独立 issue 提及，部分内容被 R27-MF3 (ρ=0.09) 吸收。可能已修复，待 Research Director 确认\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF7\"\n  summary: \"Taxonomy 11→6 选择标准需透明报告实际构造困难\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"表格存在但排除理由不够诚实\"\n    - round: 27\n      reviewers: []\n      note: \"R2-W1 提出透明度不足但被 R1 REBUT（现有三标准+Appendix M 足够）。本轮未达共识，可能已充分处理\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF8\"\n  summary: \"Abstract 信息密度过高——精简至 2-3 个核心数字\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"精简至 ~170 词，保留 4 个核心数字\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未作为独立 issue 提及。R27-M5 关注 '+12.7pp' 上下文但非密度问题。可能已修复\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-SF9\"\n  summary: \"跨 provider 可复现性需显式量化指标\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"报告 Kendall's W；§4.4 限定 ICC claim 为 within-family\"\n    - round: 27\n      reviewers: []\n      note: \"本轮未作为独立 issue 提及。R1-Q4 追问跨 provider ICC 但未升级为 weakness。可能已充分处理\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M1\"\n  summary: \"'Confound-free' 术语不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"两位独立标记\"\n    - round: 27\n      reviewers: []\n      note: \"被 R27-MF1 吸收——现在是改术语本身 (confound-free→reduced-confound) 而非统一用法\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M2\"\n  summary: \"Violation severity κ=1.00 vs failure mechanism κ=0.15 对比值得正文讨论\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"直接支撑 MF1 论点\"\n    - round: 27\n      reviewers: []\n      note: \"被 R27-MF2 吸收——人工验证不足是 type-mechanism dissociation 的核心问题\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R25 ISSUES — RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R25-W5\"\n  summary: \"C3 inconclusive 但 taxonomy 仍按 two-layer 组织\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 24\n  last_seen_round: 25\n  resolution: \"Changed wording to 'organizational framework' and 'design hypothesis'. R26 did not re-raise.\"\n  resolution_round: 26\n\n- id: \"R25-W7\"\n  summary: \"60.8% 残差方差系统性部分未讨论来源\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 24\n  last_seen_round: 25\n  resolution: \"Added clause-level interactions explanation. R26 did not re-raise.\"\n  resolution_round: 26\n\n- id: \"R25-M2\"\n  summary: \"Disambiguation neglect 增量贡献需更明确阐述\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"Rewritten as extending ambiguity collapse to agentic context. R26 did not re-raise.\"\n  resolution_round: 26\n\n- id: \"R25-M3\"\n  summary: \"References 中 arXiv preprint 格式不统一\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"All entries consistently formatted\"\n  resolution_round: 25\n\n# ============================================================\n# R24 ISSUES — RESOLVED (preserved for history)\n# ============================================================\n\n- id: \"R24-N1\"\n  summary: \"Novelty framing 偏强\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Contributions rewritten\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 25\n\n- id: \"R24-N2\"\n  summary: \"Incompleteness confound framing 不够突出\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Abstract leads with confound-free 31.0pp\"\n  resolution_round: 25\n  first_raised_round: 21\n  last_seen_round: 24\n\n- id: \"R24-W2\"\n  summary: \"Template pipeline 不透明\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Appendix S added\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W4\"\n  summary: \"SESOI ±15pp justification 不够 principled\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Changed to 'pragmatic default'. Note: R27 re-raises as SF3\"\n  resolution_round: 25\n  first_raised_round: 20\n  last_seen_round: 27\n\n- id: \"R24-W6\"\n  summary: \"Human validation per-type CI 极宽\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Qualifier added\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-W8\"\n  summary: \"NMI cardinality 不对称\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Changed to 'substantially more strongly'\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M4\"\n  summary: \"C3/C4 claim 层级暗示同等级\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Labeled C3 inconclusive, C4 exploratory\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M5\"\n  summary: \"Table 2 脚注缺 per-type 样本量\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added n≈17\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-M6\"\n  summary: \"Prevalence audit κ=0.295 未在 Introduction 标注\"\n  category: writing\n  severity: minor\n  status: resolved\n  resolution: \"Added dual-judge κ = 0.30\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X1\"\n  summary: \"ICC≈0 应改为 uninformative due to floor effects\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Reworded with floor effect explanation\"\n  resolution_round: 25\n  first_raised_round: 23\n  last_seen_round: 24\n\n- id: \"R24-X3\"\n  summary: \"Limitations 过长\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"Compressed to 3 points\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24\n\n- id: \"R24-X4\"\n  summary: \"Limitations 内部矛盾\"\n  category: writing\n  severity: critical\n  status: resolved\n  resolution: \"Removed underway, replaced with actual results\"\n  resolution_round: 25\n  first_raised_round: 24\n  last_seen_round: 24"
  }
}
```

</details>

---


### Tool result

_source line 2386 · 2026-05-23T13:34:10.999319+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 17048}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2387 · 2026-05-23T13:36:07.816698+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 圆桌审稿报告 — Round 27\n\n**Paper**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n**Venue**: EMNLP 2026 via ARR May 2026 cycle\n**Reviewers**: R1 (方法严谨性, 3.5/5), R2 (新颖性/完整性, 3.0/5)\n**交叉回应**: 完成，1 轮收敛\n\n---\n\n## Summary\n\n本文使用匹配对因果设计研究 LLM agent 在自然语言策略规范中遇到歧义时的安全违规问题。在 τ²-bench 上构建 300 个匹配 clause pair（6 种歧义类型，5 个模型，2,997 episodes），发现歧义条款使违规率增加 34.0 pp（排除 incompleteness 后 31.0 pp）。论文进一步提出 type-mechanism dissociation（V=0.45 vs 0.14，LLM-coded）、disambiguation neglect（4.6% awareness）和 systematic nocuity（41.3% convergent violations，77% permissive bias）。SOPBench 跨基准复制显示方向一致（+12.7 pp）。\n\n---\n\n## Strengths\n\n**S1 [共识]** 匹配对因果设计是本文最大的方法论优势。Perturbation control (Δ_perturb = -0.67 pp, 95% CI [-8.0, 6.67]) 有效排除表面文本变化。在 agent safety 文献中将 observational association 升级为 causal claim 是质的提升。\n\n**S2 [共识]** 统计分析系统且透明：Holm-Bonferroni 多重比较校正、七个 margin TOST 敏感性分析、方差分解、ICC 可重复性 (0.919)、bootstrap clustering。几乎所有统计选择都有 sensitivity check。\n\n**S3 [共识]** Claim 分级诚实：C3 标注 \"inconclusive\"（p=0.017 vs threshold 0.0125），C4 标注 \"exploratory\"。\n\n**S4 [共识]** 实验规模（300 clause pairs × 5 models × 2 conditions = 2,997 episodes）和 Appendix 深度（13 pages）远超同类工作，可复现性高。\n\n**S5 [共识]** Authorization scope 的透明处理——多处标注低 κ (0.385)、高跨模型方差 (52 pp range)、质量审计的 borderline pairs (16%)，并报告排除后的所有核心分析。\n\n**S6 [R2]** SOPBench 跨基准复制和两个额外模型族扩展增加外部效度。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1 [共识, R1-N1 + R2-W2]** 信息添加混淆是系统性的，\"confound-free\" 标签不准确\n\n论文仅将 incompleteness 标记为有 information-addition confound，但 Appendix Q 数据显示所有类型的消歧版本都系统性更长：auth scope +36.1 words, incompleteness +34.6, lexical +25.7, scopal +17.8, cond. prec. +17.5。消歧版本不仅消除歧义，还添加具体决策信息。Token count logistic regression 不能分离 disambiguation 与 information-addition 两种因果路径。Coreferential (Δtoken≈0, 18.7 pp) 是唯一干净的因果估计。\n\n**修改要求**：(a) 承认所有类型信息添加混淆；(b) \"confound-free\" → \"reduced-confound\"；(c) 报告 per-type Δtoken vs Δviolation rate rank correlation；(d) 突出 coreferential 18.7 pp 为 confound-free 下限。\n\n**MF2 [共识, R1-N2 + R2 AGREE]** Type-mechanism dissociation (V=0.45) 缺乏可靠人工验证\n\nV=0.45 完全来自 LLM 编码（Gwet's AC₁=0.62, κ=0.52），存在 circularity risk。人工 mechanism 编码 κ=0.15（合并后 0.38），远低于 substantial agreement。Abstract 表述给人印象远超 \"exploratory\"。\n\n**修改要求**：(a) 降级 C3 为 exploratory，Abstract 标注 \"exploratory, LLM-coded\"；(b) 提供 human-coded (4-cat, κ=0.38) V 值；(c) 讨论 LLM vs human 编码差异含义。\n\n**MF3 [共识, R1-N3 + R2 AGREE]** 跨判官组类型排序 ρ=0.09 威胁 C2 稳健性\n\n两个判官组类型排序 ρ=0.09 (p=0.87)。排除 auth scope 后 ρ=0.90，但 auth scope 占 16.7%，选择性排除不可接受。Judge-model identity 完全交织，ρ=0.09 可能同时反映 type ordering instability 和 judge-model interaction。\n\n**修改要求**：(a) 正文充分讨论 ρ=0.09 对 C2 影响；(b) 用三个判官族重算 C2；(c) 考虑降级 C2。\n\n**MF4 [共识, R2-N1 + R1 AGREE]** \"Nocuous\" 术语语义反转论证不足\n\nBerry 原意 divergent=harmful，本文 convergent wrong interpretation 在 Berry 框架下更接近 innocuous。仅一句话完成术语重定义。与 Gur-Arieh et al. \"ambiguity collapse\" 高度重叠但讨论不足。\n\n**修改要求**：(a) 明确 convergent nocuity vs divergent nocuity 区分；(b) 深入讨论与 ambiguity collapse 的关系；(c) 论证 convergent wrong interpretation 在 agentic 语境下的 harm 模式。\n\n### Should-Fix\n\n**SF1 [分歧→降级]** 增量贡献论证（R2 认为 \"better methodology for known finding\"；R1 反驳因果识别是质的提升。共识：C1 有方法论价值，但需更明确论述 matched-pair 独有发现）\n\n**SF2 [共识降级]** 标题 domain scope 应限定为 customer-service（Abstract 已限定，但标题暗示 general）\n\n**SF3 [共识]** SESOI ±15 pp 缺乏领域锚定，cluster structure margin-dependent（±10pp 3/6, ±12pp 5/6, ±15pp 6/6）\n\n**SF4 [共识]** SOPBench 2/5 模型未显著但 Abstract 未披露（GPT-5.4 p=0.052, DeepSeek p=0.163）\n\n**SF5 [共识]** \"Ambiguity\" 广义使用需引用 Poesio/van Deemter underspecification 区分文献\n\n**SF6 [共识]** Temperature=0 限制需更充分讨论（测量 default interpretation 非 outcome distribution）\n\n**SF7 [R1+R2]** Clause pair 质量——scopal 示例更像 vagueness/incompleteness 而非 scope ambiguity\n\n### Minor\n\n- **M1**: \"Tier\" → \"Cluster\"，\"conditional OR\" → \"McNemar OR\"\n- **M2**: Conclusion 过于简略（一句话），应扩展\n- **M3**: Prevalence audit \"55-87%\" 应附 CI 并更谨慎\n- **M4**: Cramér's V 跨维度比较应标注 caveat\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. \"Confound-free\" 标签不准确——信息添加是系统性的（R1-N1, R2-W2）\n2. Type-mechanism dissociation 缺乏人工验证（R1-N2, R2 AGREE）\n3. ρ=0.09 威胁 C2（R1-N3, R2 AGREE）\n4. \"Nocuous\" 术语论证不足（R2-N1, R1 AGREE）\n5. C1 因果设计的方法论价值是真实贡献（S1）\n6. Temperature=0 需更充分讨论（R1-W4, R2-Q5）\n7. SOPBench 报告透明度不足（R1-W2, R2 AGREE）\n8. Poesio/van Deemter 文献遗漏（R2-W5, R1 AGREE）\n\n## Reviewer Divergence [REBUT]\n\n**增量贡献评估**：R2 认为 \"better methodology for a known finding\" (3.0)；R1 反驳因果识别是质的提升而非 incremental improvement (3.5)。R1 论证有力——DRIP-R correlational design 无法区分因果与共现。但两位均同意：type-level contributions (C2/C3) 的证据链缺陷削弱 overall novelty。\n\n**60.8% 残差方差**：R2 认为削弱因果叙事；R1 反驳匹配对因果识别不依赖解释总方差比例。R1 反驳正确——高残差反映 clause-level heterogeneity，是 C2 的 qualification 而非 C1 的缺陷。\n\n---\n\n## Questions\n\n**Q1 [共识]**: 人工合并后编码 (4-cat, κ=0.38) 的 Cramér's V 值？直接决定 C3 证据强度。\n**Q2 [共识]**: Per-type Δtoken vs Δviolation rate 的 rank correlation？量化信息添加 confound severity。\n**Q3 [共识]**: Cross-judge 非对称分配（3:2）的理由？为何不用 full cross-design？\n**Q4 [R1]**: 跨 provider ICC？Kendall's W=0.398 (p=0.072) 暗示跨 provider 一致性较低。\n**Q5 [R2]**: V=0.45 的置信区间？CI 下限接近 0.3 则 \"diagnostic instrument\" reframing 削弱。\n**Q6 [共识]**: 是否有 temperature>0 pilot data？\n\n---\n\n## Missing References\n\n1. **Poesio (1996) / van Deemter (2004)** [共识] — ambiguity vs underspecification 经典区分\n2. **Zhu et al. (2025)** [共识] — \"Ambiguity in LLMs is a concept missing problem\"\n3. **AgentSpec (Poskitt et al., ICSE 2026)** [R2] — runtime enforcement for LLM agents\n4. **\"The Illusion of Certainty\" (arXiv:2511.04418)** [R2] — LLM uncertainty quantification\n5. **Rosenbaum (2002)** [R1] — matched-pair hidden bias sensitivity analysis\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（1 critical + 3 warning + 5 info）：\n\n- **[critical] p.23**: 最后一页仅 5 行文字（~5% 页面），其余全部空白。建议合并或补充内容。\n- **[warning] p.7**: Table 2 + Figure 3 + Figure 4 三个 display item 挤在同一页。建议 Figure 4 移至 p.8。\n- **[warning] p.13**: 附录 6 张表格挤在同一页，间距极小。\n- **[warning] p.18**: 附录 5 张表格挤在同一页，Table 14 字号偏小。\n- **[info]**: Figure 1/3/4 内部文字偏小；Figure 2 颜色方案应验证色盲友好性；主文约 8.5 页，符合 EMNLP 8 页限制。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n**置信度: 4/5**\n**Reviewer 分歧**: R1 3.5 (Borderline Conference) / R2 3.0 (Findings)\n\nC1（二元因果效应，+31.0 pp reduced-confound）方法论执行质量高——匹配对设计 + perturbation control + 七模型复制 + 跨基准方向一致性。R1 正确指出因果识别相对于 DRIP-R 的 correlational design 是质的提升。\n\n但论文呈现的是三个 contributions 的整体叙事：\n- **C2 (type partial ordering)**：被 ρ=0.09 和 margin-dependent cluster structure 严重削弱\n- **C3 (type-mechanism dissociation)**：核心证据 V=0.45 完全依赖 LLM 编码，人工验证不足\n- **Framing**：\"confound-free\" 标签不准确；\"nocuous\" 术语反转论证不足\n\n三个 contributions 中两个的证据链存在实质性缺陷，加上术语框架问题，论文整体处于 Findings 级别。\n\n**修改后可达 3.5 的条件**：(a) 报告 human-coded V' 和 Δtoken-Δviolation correlation 来量化两个核心 confound；(b) 降级 C3 为 exploratory；(c) 不再依赖选择性排除 auth scope；(d) 扩展 nocuous 术语论证。\n\n---\n\n## Detailed Comments\n\n**Introduction**: \"Nocuous\" 反转需展开论证（MF4）；C3 应标注 \"exploratory, LLM-coded\"（MF2）\n**Section 3**: 引用 Poesio/van Deemter（SF5）；Appendix M 排除论证可补充 ellipsis/pragmatic implication 示例\n**Section 4.2**: 承认所有类型信息添加混淆（MF1）\n**Section 4.4**: 说明 cross-judge 非对称分配理由（Q3）\n**Section 4.6**: 明确 cluster structure margin-dependency（SF3）\n**Section 5.2**: ρ=0.09 从 qualification 提升为正式讨论（MF3）；所有 \"confound-free\" → \"reduced-confound\"（MF1）\n**Section 6**: C3 降级为 exploratory（MF2）；提供 human-coded V'（Q1）\n**Section 7**: 扩展 convergent nocuity 论证（MF4）；讨论 information-addition confound（MF1）\n**Abstract**: \"+12.7 pp\" 注明 3/5 显著（SF4）；V=0.45 标注 \"exploratory, LLM-coded\"；\"confound-free\" → \"reduced-confound\"\n**Conclusion**: 扩展 implications 和 future work（M2）",
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 圆桌审稿报告 — Round 27\n\n**Paper**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n**Venue**: EMNLP 2026 via ARR May 2026 cycle\n**Reviewers**: R1 (方法严谨性, 3.5/5), R2 (新颖性/完整性, 3.0/5)\n**交叉回应**: 完成，1 轮收敛\n\n---\n\n## Summary\n\n本文使用匹配对因果设计研究 LLM agent 在自然语言策略规范中遇到歧义时的安全违规问题。在 τ²-bench 上构建 300 个匹配 clause pair（6 种歧义类型，5 个模型，2,997 episodes），发现歧义条款使违规率增加 34.0 pp（排除 incompleteness 后 31.0 pp）。论文进一步提出 type-mechanism dissociation（V=0.45 vs 0.14，LLM-coded）、disambiguation neglect（4.6% awareness）和 systematic nocuity（41.3% convergent violations，77% permissive bias）。SOPBench 跨基准复制显示方向一致（+12.7 pp）。\n\n---\n\n## Strengths\n\n**S1 [共识]** 匹配对因果设计是本文最大的方法论优势。Perturbation control (Δ_perturb = -0.67 pp, 95% CI [-8.0, 6.67]) 有效排除表面文本变化。在 agent safety 文献中将 observational association 升级为 causal claim 是质的提升。\n\n**S2 [共识]** 统计分析系统且透明：Holm-Bonferroni 多重比较校正、七个 margin TOST 敏感性分析、方差分解、ICC 可重复性 (0.919)、bootstrap clustering。几乎所有统计选择都有 sensitivity check。\n\n**S3 [共识]** Claim 分级诚实：C3 标注 \"inconclusive\"（p=0.017 vs threshold 0.0125），C4 标注 \"exploratory\"。\n\n**S4 [共识]** 实验规模（300 clause pairs × 5 models × 2 conditions = 2,997 episodes）和 Appendix 深度（13 pages）远超同类工作，可复现性高。\n\n**S5 [共识]** Authorization scope 的透明处理——多处标注低 κ (0.385)、高跨模型方差 (52 pp range)、质量审计的 borderline pairs (16%)，并报告排除后的所有核心分析。\n\n**S6 [R2]** SOPBench 跨基准复制和两个额外模型族扩展增加外部效度。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1 [共识, R1-N1 + R2-W2]** 信息添加混淆是系统性的，\"confound-free\" 标签不准确\n\n论文仅将 incompleteness 标记为有 information-addition confound，但 Appendix Q 数据显示所有类型的消歧版本都系统性更长：auth scope +36.1 words, incompleteness +34.6, lexical +25.7, scopal +17.8, cond. prec. +17.5。消歧版本不仅消除歧义，还添加具体决策信息。Token count logistic regression 不能分离 disambiguation 与 information-addition 两种因果路径。Coreferential (Δtoken≈0, 18.7 pp) 是唯一干净的因果估计。\n\n**修改要求**：(a) 承认所有类型信息添加混淆；(b) \"confound-free\" → \"reduced-confound\"；(c) 报告 per-type Δtoken vs Δviolation rate rank correlation；(d) 突出 coreferential 18.7 pp 为 confound-free 下限。\n\n**MF2 [共识, R1-N2 + R2 AGREE]** Type-mechanism dissociation (V=0.45) 缺乏可靠人工验证\n\nV=0.45 完全来自 LLM 编码（Gwet's AC₁=0.62, κ=0.52），存在 circularity risk。人工 mechanism 编码 κ=0.15（合并后 0.38），远低于 substantial agreement。Abstract 表述给人印象远超 \"exploratory\"。\n\n**修改要求**：(a) 降级 C3 为 exploratory，Abstract 标注 \"exploratory, LLM-coded\"；(b) 提供 human-coded (4-cat, κ=0.38) V 值；(c) 讨论 LLM vs human 编码差异含义。\n\n**MF3 [共识, R1-N3 + R2 AGREE]** 跨判官组类型排序 ρ=0.09 威胁 C2 稳健性\n\n两个判官组类型排序 ρ=0.09 (p=0.87)。排除 auth scope 后 ρ=0.90，但 auth scope 占 16.7%，选择性排除不可接受。Judge-model identity 完全交织，ρ=0.09 可能同时反映 type ordering instability 和 judge-model interaction。\n\n**修改要求**：(a) 正文充分讨论 ρ=0.09 对 C2 影响；(b) 用三个判官族重算 C2；(c) 考虑降级 C2。\n\n**MF4 [共识, R2-N1 + R1 AGREE]** \"Nocuous\" 术语语义反转论证不足\n\nBerry 原意 divergent=harmful，本文 convergent wrong interpretation 在 Berry 框架下更接近 innocuous。仅一句话完成术语重定义。与 Gur-Arieh et al. \"ambiguity collapse\" 高度重叠但讨论不足。\n\n**修改要求**：(a) 明确 convergent nocuity vs divergent nocuity 区分；(b) 深入讨论与 ambiguity collapse 的关系；(c) 论证 convergent wrong interpretation 在 agentic 语境下的 harm 模式。\n\n### Should-Fix\n\n**SF1 [分歧→降级]** 增量贡献论证（R2 认为 \"better methodology for known finding\"；R1 反驳因果识别是质的提升。共识：C1 有方法论价值，但需更明确论述 matched-pair 独有发现）\n\n**SF2 [共识降级]** 标题 domain scope 应限定为 customer-service（Abstract 已限定，但标题暗示 general）\n\n**SF3 [共识]** SESOI ±15 pp 缺乏领域锚定，cluster structure margin-dependent（±10pp 3/6, ±12pp 5/6, ±15pp 6/6）\n\n**SF4 [共识]** SOPBench 2/5 模型未显著但 Abstract 未披露（GPT-5.4 p=0.052, DeepSeek p=0.163）\n\n**SF5 [共识]** \"Ambiguity\" 广义使用需引用 Poesio/van Deemter underspecification 区分文献\n\n**SF6 [共识]** Temperature=0 限制需更充分讨论（测量 default interpretation 非 outcome distribution）\n\n**SF7 [R1+R2]** Clause pair 质量——scopal 示例更像 vagueness/incompleteness 而非 scope ambiguity\n\n### Minor\n\n- **M1**: \"Tier\" → \"Cluster\"，\"conditional OR\" → \"McNemar OR\"\n- **M2**: Conclusion 过于简略（一句话），应扩展\n- **M3**: Prevalence audit \"55-87%\" 应附 CI 并更谨慎\n- **M4**: Cramér's V 跨维度比较应标注 caveat\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. \"Confound-free\" 标签不准确——信息添加是系统性的（R1-N1, R2-W2）\n2. Type-mechanism dissociation 缺乏人工验证（R1-N2, R2 AGREE）\n3. ρ=0.09 威胁 C2（R1-N3, R2 AGREE）\n4. \"Nocuous\" 术语论证不足（R2-N1, R1 AGREE）\n5. C1 因果设计的方法论价值是真实贡献（S1）\n6. Temperature=0 需更充分讨论（R1-W4, R2-Q5）\n7. SOPBench 报告透明度不足（R1-W2, R2 AGREE）\n8. Poesio/van Deemter 文献遗漏（R2-W5, R1 AGREE）\n\n## Reviewer Divergence [REBUT]\n\n**增量贡献评估**：R2 认为 \"better methodology for a known finding\" (3.0)；R1 反驳因果识别是质的提升而非 incremental improvement (3.5)。R1 论证有力——DRIP-R correlational design 无法区分因果与共现。但两位均同意：type-level contributions (C2/C3) 的证据链缺陷削弱 overall novelty。\n\n**60.8% 残差方差**：R2 认为削弱因果叙事；R1 反驳匹配对因果识别不依赖解释总方差比例。R1 反驳正确——高残差反映 clause-level heterogeneity，是 C2 的 qualification 而非 C1 的缺陷。\n\n---\n\n## Questions\n\n**Q1 [共识]**: 人工合并后编码 (4-cat, κ=0.38) 的 Cramér's V 值？直接决定 C3 证据强度。\n**Q2 [共识]**: Per-type Δtoken vs Δviolation rate 的 rank correlation？量化信息添加 confound severity。\n**Q3 [共识]**: Cross-judge 非对称分配（3:2）的理由？为何不用 full cross-design？\n**Q4 [R1]**: 跨 provider ICC？Kendall's W=0.398 (p=0.072) 暗示跨 provider 一致性较低。\n**Q5 [R2]**: V=0.45 的置信区间？CI 下限接近 0.3 则 \"diagnostic instrument\" reframing 削弱。\n**Q6 [共识]**: 是否有 temperature>0 pilot data？\n\n---\n\n## Missing References\n\n1. **Poesio (1996) / van Deemter (2004)** [共识] — ambiguity vs underspecification 经典区分\n2. **Zhu et al. (2025)** [共识] — \"Ambiguity in LLMs is a concept missing problem\"\n3. **AgentSpec (Poskitt et al., ICSE 2026)** [R2] — runtime enforcement for LLM agents\n4. **\"The Illusion of Certainty\" (arXiv:2511.04418)** [R2] — LLM uncertainty quantification\n5. **Rosenbaum (2002)** [R1] — matched-pair hidden bias sensitivity analysis\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（1 critical + 3 warning + 5 info）：\n\n- **[critical] p.23**: 最后一页仅 5 行文字（~5% 页面），其余全部空白。建议合并或补充内容。\n- **[warning] p.7**: Table 2 + Figure 3 + Figure 4 三个 display item 挤在同一页。建议 Figure 4 移至 p.8。\n- **[warning] p.13**: 附录 6 张表格挤在同一页，间距极小。\n- **[warning] p.18**: 附录 5 张表格挤在同一页，Table 14 字号偏小。\n- **[info]**: Figure 1/3/4 内部文字偏小；Figure 2 颜色方案应验证色盲友好性；主文约 8.5 页，符合 EMNLP 8 页限制。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n**置信度: 4/5**\n**Reviewer 分歧**: R1 3.5 (Borderline Conference) / R2 3.0 (Findings)\n\nC1（二元因果效应，+31.0 pp reduced-confound）方法论执行质量高——匹配对设计 + perturbation control + 七模型复制 + 跨基准方向一致性。R1 正确指出因果识别相对于 DRIP-R 的 correlational design 是质的提升。\n\n但论文呈现的是三个 contributions 的整体叙事：\n- **C2 (type partial ordering)**：被 ρ=0.09 和 margin-dependent cluster structure 严重削弱\n- **C3 (type-mechanism dissociation)**：核心证据 V=0.45 完全依赖 LLM 编码，人工验证不足\n- **Framing**：\"confound-free\" 标签不准确；\"nocuous\" 术语反转论证不足\n\n三个 contributions 中两个的证据链存在实质性缺陷，加上术语框架问题，论文整体处于 Findings 级别。\n\n**修改后可达 3.5 的条件**：(a) 报告 human-coded V' 和 Δtoken-Δviolation correlation 来量化两个核心 confound；(b) 降级 C3 为 exploratory；(c) 不再依赖选择性排除 auth scope；(d) 扩展 nocuous 术语论证。\n\n---\n\n## Detailed Comments\n\n**Introduction**: \"Nocuous\" 反转需展开论证（MF4）；C3 应标注 \"exploratory, LLM-coded\"（MF2）\n**Section 3**: 引用 Poesio/van Deemter（SF5）；Appendix M 排除论证可补充 ellipsis/pragmatic implication 示例\n**Section 4.2**: 承认所有类型信息添加混淆（MF1）\n**Section 4.4**: 说明 cross-judge 非对称分配理由（Q3）\n**Section 4.6**: 明确 cluster structure margin-dependency（SF3）\n**Section 5.2**: ρ=0.09 从 qualification 提升为正式讨论（MF3）；所有 \"confound-free\" → \"reduced-confound\"（MF1）\n**Section 6**: C3 降级为 exploratory（MF2）；提供 human-coded V'（Q1）\n**Section 7**: 扩展 convergent nocuity 论证（MF4）；讨论 information-addition confound（MF1）\n**Abstract**: \"+12.7 pp\" 注明 3/5 显著（SF4）；V=0.45 标注 \"exploratory, LLM-coded\"；\"confound-free\" → \"reduced-confound\"\n**Conclusion**: 扩展 implications 和 future work（M2）",
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 2388 · 2026-05-23T13:36:13.080345+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5263
}
```

</details>

---


### Assistant

_source line 2389 · 2026-05-23T13:36:23.761758+00:00_

审稿报告已投递。

**Round 27 圆桌审稿完成**。

**评分：3.0 (Findings)**（R1: 3.5 Borderline Conference / R2: 3.0 Findings）

**4 个 Must-Fix 共识**：
1. **信息添加混淆是系统性的**——所有类型 unambiguous variant 都更长，"confound-free" 标签不准确，coreferential 18.7pp 是唯一干净估计
2. **Type-mechanism dissociation 缺乏人工验证**——V=0.45 完全依赖 LLM 编码，人工 κ=0.15 (collapsed 0.38)，需降级为 exploratory 并报告 human-coded V'
3. **ρ=0.09 威胁 C2**——跨判官组类型排序零相关，选择性排除 auth scope 不可接受
4. **"Nocuous" 术语反转论证不足**——Berry 原意 divergent=harmful，convergent error 需独立论证

**核心判断**：C1 因果识别（+31.0pp）方法论扎实，是真实贡献。但 C2/C3 的证据链存在实质性缺陷，加上术语框架问题，论文处于 Findings 级别。修改到位后有潜力达 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 227

## Round 227

2 recorded events


### User

_source line 2390 · 2026-05-23T13:36:26.346952+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：对 R1 的 3 个 Must-Fix 全部 **[AGREE]**（信息添加 confound 不限于 incompleteness、LLM 编码 circularity、ρ=0.09 动摇 C2），仅对 W5（Cramér's V 跨维度比较）给出 **[REBUT]**——维度差异实际上可能强化而非削弱 type-mechanism dissociation 结论。

两位 reviewer 的共识区间为 **3.0–3.5**，关键取决于作者能否在 revision 中提供 human-coded V'、per-type confound 量化、以及不再选择性排除 auth scope。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2391 · 2026-05-23T13:36:40.285780+00:00_

Round 27 审稿已完成，报告已投递至 Research Director。

**最终评分: 3.0 (Findings)**（R1: 3.5, R2: 3.0）

**4 个 Must-Fix 共识**：
1. **信息添加混淆是系统性的**——"confound-free" 标签对所有类型不准确，coreferential 18.7pp 是唯一干净锚点
2. **Type-mechanism dissociation 缺乏人工验证**——V=0.45 完全依赖 LLM 编码，需报告 human-coded V'
3. **ρ=0.09 威胁 C2**——选择性排除 auth scope 不可接受
4. **"Nocuous" 术语反转论证不足**——需扩展 convergent vs divergent nocuity 论证

**1 个分歧**：增量贡献评估——R1 认为因果识别是质的提升 (3.5)，R2 认为 "better methodology for known finding" (3.0)

Issue Tracker 已同步更新（R27: 4 MF + 7 SF + 4 Minor）。视觉审查结果已纳入报告（1 critical: p.23 尾页空白）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 228

## Round 228

56 recorded events


### User

_source line 2392 · 2026-05-23T14:18:02.091292+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2393 · 2026-05-23T14:18:08.478666+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2394 · 2026-05-23T14:18:08.530566+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2395 · 2026-05-23T14:18:16.763180+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,get_external_review_status,request_external_review,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,get_external_review_status,request_external_review,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 2396 · 2026-05-23T14:18:16.763614+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2397 · 2026-05-23T14:18:20.778315+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2398 · 2026-05-23T14:18:20.879238+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2399 · 2026-05-23T14:18:21.584344+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2400 · 2026-05-23T14:18:21.936348+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2401 · 2026-05-23T14:18:21.987047+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2402 · 2026-05-23T14:18:23.342786+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2403 · 2026-05-23T14:18:23.343298+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{placeins}
16	
17	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
18	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
19	
20	\definecolor{speccolor}{HTML}{C44E52}
21	\definecolor{lingcolor}{HTML}{4C72B0}
22	
23	\title{Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{sections/abstract}
31	\input{sections/introduction}
32	\input{sections/related_work}
33	\input{sections/taxonomy}
34	\input{sections/method}
35	\input{sections/experiments}
36	\input{sections/analysis}
37	\input{sections/discussion}
38	\input{sections/conclusion}
39	\input{sections/limitations}
40	
41	\bibliography{references}
42	
43	\appendix
44	\makeatletter
45	\newcommand{\extAlph}[1]{%
46	  \ifcase#1\or A\or B\or C\or D\or E\or F\or G\or H\or I\or J\or K\or L\or M\or N\or O\or P\or Q\or R\or S\or T\or U\or V\or W\or X\or Y\or Z\or AA\or AB\or AC\or AD\or AE\fi}
47	\renewcommand{\thesection}{\extAlph{\value{section}}}
48	\makeatother
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 2404 · 2026-05-23T14:18:27.707535+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information about EMNLP 2026 and ARR submission processes, though there isn't a dedicated 
…[truncated 1151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5720
}
```

</details>

---


### Tool call

_source line 2405 · 2026-05-23T14:18:33.780338+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limits format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limits format requirements"
  }
}
```

</details>

---


### Tool call

_source line 2406 · 2026-05-23T14:18:34.633615+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 2407 · 2026-05-23T14:18:36.040431+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2408 · 2026-05-23T14:18:36.544504+00:00_

1	\begin{abstract}
2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. Using a matched-pair causal design on $\tau^2$-bench with 300 clause pairs spanning a six-type taxonomy evaluated across five models, we show that ambiguous clauses increase violations by 31.0 percentage points excluding incompleteness (34.0\,pp overall); cross-benchmark replication on SOPBench confirms directional consistency ($+$12.7\,pp overall; 3/5 models significant at $p < 0.05$). However, ambiguity \emph{type} predicts \emph{how} agents fail, not \emph{whether} they fail: each type maps to a dominant failure mechanism with $\geq$3/5 cross-model consistency ($V = 0.45$ vs.\ $0.14$, LLM-coded; human $\kappa = 0.34$--$0.52$ collapsed). This \emph{type--mechanism dissociation} establishes the taxonomy as a diagnostic instrument rather than a risk classifier. Error analysis reveals that agents almost never recognize ambiguity and converge on identical policy violations with strong permissive bias, inverting \citeauthor{berry_kamsties_2004}'s divergent-interpretation framework to convergent error. These findings, established under controlled conditions in two customer-service domains, motivate clause-level policy auditing over type-level risk screening.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 2409 · 2026-05-23T14:18:36.544931+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2410 · 2026-05-23T14:18:37.451770+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity---a pilot audit of 407 clauses from 24 production policy documents finds a majority of clauses contain at least one ambiguity type (55--87\%, depending on union vs.\ intersection of two judges; dual-judge $\kappa = 0.30$; Appendix~\ref{app:prevalence})---a property studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. Berry and Kamsties define nocuity in terms of stakeholder \emph{divergence}; convergent interpretation is assumed innocuous because consistency implies shared understanding. We document a distinct failure mode that breaks this assumption: LLM agents \emph{converge} on the same incorrect interpretation, making ambiguity harmful through systematic, undetectable error rather than inconsistency (\S\ref{sec:analysis}). Unlike human teams, where convergence reflects shared domain knowledge, agent convergence reflects shared training biases operating on identical inputs. We term this \emph{convergent nocuity}---distinct from Berry's divergent nocuity in mechanism (bias-driven vs.\ knowledge-gap-driven) and detectability (invisible to agreement-based monitorin
…[truncated 3462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 2411 · 2026-05-23T14:18:37.452270+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2412 · 2026-05-23T14:18:37.955384+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300; Cohen's $\kappa = 0.95$ on six-type classification); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We
…[truncated 4665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2413 · 2026-05-23T14:18:38.006064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2414 · 2026-05-23T14:18:38.409992+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around three analyses: the binary ambiguity effect (C1), the type partial ordering (C2, including the inconclusive layer effect C3), and the model$\times$type interaction (C4). C1 and C2 are primary supported claims; C3 (layer effect) is inconclusive; C4 (model$\times$type interaction) is exploratory.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{figures/fig_variance_decomposition.pdf}
11	\caption{Variance decomposition of violation rates (temperature $= 0$). Clause identity: 22.4\% (0.4\% between types); condition: 15.8\%; model: 1.0\%; residual: 60.8\%.}
12	\label{fig:variance_decomposition}
13	\end{figure}
14	
15	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, McNemar OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity (\S\ref{sec:method}). Figure~\ref{fig:variance_decomposition} decomposes violation-rate variance\footnote{Type III SS; logistic regression (Appendix~\ref{app:regression}) confirms concordant results (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}).}: clause identity explains 22.4\% (0.4\% between types, 22.0\% within), condition 15.8\%, model 1.0\%, and residual 60.8\% ($\sim$15\% stochastic, $\sim$46\% systematic; Appendix~\ref{app:residual}). A permutation test confirms that clause wording---not type membership---drives this variance ($p < 0.001$; Appendix~\ref{app:clause_variance}). The incompleteness effect ($+$49.2\,pp) is an upper bound: the unambiguous variant necessarily adds policy content, introducing an information-addition confound that token-count matching cannot address (Appendix~\ref{app:confound}). Excludin
…[truncated 6098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 2415 · 2026-05-23T14:18:38.410515+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2416 · 2026-05-23T14:18:38.464329+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool result

_source line 2417 · 2026-05-23T14:18:39.368343+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limits format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review (ARR) 2026 regarding page limits and format requirements:

## Page Limits

Short papers have a maximum of 4 content pages, while long papers have a maximum of 8 content pages. Sections on ethical considerations and limitations do not count towards the 
…[truncated 863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5588
}
```

</details>

---


### Tool result

_source line 2418 · 2026-05-23T14:18:40.121394+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on th
…[truncated 1034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5487
}
```

</details>

---


### Tool call

_source line 2419 · 2026-05-23T14:18:50.964126+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 2420 · 2026-05-23T14:18:51.418487+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_type_mechanism.pdf}
7	\caption{Type--mechanism association (percentage of violation traces per type assigned to each failure mechanism). Each type maps to a dominant mechanism ($\geq$3/5 model consistency), supporting the taxonomy's diagnostic value (NMI $= 0.23$, Cram\'{e}r's $V = 0.45$, LLM-coded).}
8	\label{fig:type_mechanism}
9	\end{figure}
10	
11	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
12	
13	We analyze 614 violation traces across all five models, coded into five failure modes (Gwet's AC$_1$ $= 0.62$, $\kappa = 0.52$ \citep{gwet_2014,cohen_1960}); the coder prompt excludes ambiguity type labels, with type assigned post hoc. Using LLMs to code LLM failures risks circularity; however, type--mechanism mutual information ($V = 0.45$, bootstrap 95\% CI $[0.41, 0.50]$; Appendix~\ref{app:type_mechanism}) provides structural evidence against this.\footnote{$V$ is computed on a $6\times 5$ table vs.\ $6\times 2$ for severity; higher dimensionality makes $V = 0.45$ conservative.} Human mechanism coding yields $\kappa = 0.15$, rising to $0.34$--$0.52$ after collapsing the spurious-compliance/structural-misparse boundary (Appendix~\ref{app:human_validation}); we treat $V = 0.45$ as an upper bound. The following patterns should be interpreted as consistent LLM categorization tendencies rather than ground-truth assignments. Two of six mappings reflect partial definitional affinity (authorization scope$\to$boundary violation, incompleteness$\to$gap-filling); the remaining four (e.g., scopal$\to$structural misparse, 82.7\% consistency) are empirically derived.
14	
15	\subsection{Type-Specific Failure Mechanisms}
16	
17	The five-model data reveal three distinct failure patterns (as classified by LLM coders) that crossc
…[truncated 2317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 2421 · 2026-05-23T14:18:51.418998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2422 · 2026-05-23T14:18:51.921022+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Type--mechanism dissociation and intervention design.}
5	The type--mechanism dissociation ($V = 0.45$ vs.\ $0.14$) reframes the taxonomy as a diagnostic instrument; prompt-based mitigation is type-dependent (Appendix~\ref{app:mitigation}). The 60.8\% residual variance reflects clause-level interactions (Appendix~\ref{app:residual}), motivating clause-level auditing over type-level screening. These findings identify causal mechanisms, not deployment-ready effect sizes; SOPBench ($+$12.7\,pp; Appendix~\ref{app:sopbench}) confirms directional consistency.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2423 · 2026-05-23T14:18:51.921484+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2424 · 2026-05-23T14:18:52.874958+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_l
…[truncated 4684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 2425 · 2026-05-23T14:18:52.925708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 2426 · 2026-05-23T14:18:53.378208+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an inclusive definition of ambiguity that encompasses phenomena sometimes distinguished as underspecification or vagueness \citep{poesio_artstein_2005,vandeemter_semantic_1996}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases where the boundary between interpretations is gradient rather than discrete \citep{wasow_ambiguity_2005,kennedy_vagueness_2007}. In the policy specification domain, these distinctions are less salient than the shared property of admitting multiple operationally distinct agent behaviors.
5	
6	Traditional NLP ambiguity classification focuses on within-sentence phenomena \citep{wasow_ambiguity_2005}; our specification layer captures document-level policy gaps unstudied in the agent context. Our taxonomy provides an organizational framework of six types organized into two layers (Table~\ref{tab:taxonomy}), selected from \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types; full mapping in Appendix~\ref{app:li_mapping}) based on three design criteria: (1)~theoretical attestation in prior RE literature \citep{massey_ambiguity_re_2014,berry_kamsties_2004,drip_r_2026}, (2)~amenability to minimal-pair construction without altering clause semantics beyond the target ambiguity, and (3)~mutual exclusivity for unambiguous IV assignment. Types such as ellipsis and pragmatic implicature were excluded because they resist minimal-pair construction within the single-clause policy format.
7	
8	\begin{table}[t]
9	\centering
10	\footnotesize
11	\caption{Six-type ambiguity taxonomy. Disambiguation channel indicates the primary mechanism required to resolve the ambiguity.}
12	\label{tab:taxonomy}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}llll@{}}
15	\toprule
16	\textbf{Type} & \textbf{Layer} & \textbf{Definition} & \textbf{Disambig.\ Channel} \\
17	\midrule
18	Lexical & Ling. & Word/phrase admits multip
…[truncated 3376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2427 · 2026-05-23T14:18:53.529297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2428 · 2026-05-23T14:18:53.831053+00:00_

1	\section{Conclusion}
2	
3	Policy ambiguity increases agent violations by 31.0\,pp excluding incompleteness ($+$12.7\,pp on SOPBench, 3/5 significant), with coreferential ambiguity providing a confound-minimized lower bound of $+$18.7\,pp. The type--mechanism dissociation ($V = 0.45$, LLM-coded) and $>$89\% disambiguation neglect motivate clause-level policy auditing over type-level risk screening for similar customer-service settings. Future work should extend to non-customer-service domains, evaluate under stochastic sampling, and collect per-episode human mechanism annotations to validate the type--mechanism association.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2429 · 2026-05-23T14:18:53.831511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2430 · 2026-05-23T14:18:54.333363+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our ambiguity pairs are synthetically constructed, so the 34.0\,pp effect is an upper bound; the SOPBench replication ($+$12.7\,pp) provides a cross-benchmark lower bound. We evaluate seven API-accessible models across two customer-service domains at temperature $= 0$; other domains, smaller models, and stochastic sampling remain untested. Failure mode coding relies on LLM annotators ($\kappa = 0.52$; human $\kappa = 0.15$, rising to $0.34$--$0.52$ after collapsing the spurious-compliance/structural-misparse boundary), though the coder prompt excludes ambiguity type labels, preventing type--mechanism contamination. All experiments use temperature $= 0$, measuring each model's modal interpretation---the policy-relevant quantity agents will most likely commit to---but this does not capture tail-risk behavior under stochastic sampling. Higher temperatures would likely increase variance in both conditions; however, the magnitude of the effect ($+$31.0\,pp excluding incompleteness) and its cross-model consistency suggest the central tendency is robust. We have no temperature $> 0$ pilot data.
5	
6	\section*{Data and Code Availability}
7	The 300 clause pairs, evaluation pipeline, analysis scripts, and raw episode traces will be released upon publication at \url{https://github.com/anonymous-nlp-2026/policy_ambiguity_safety}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 2431 · 2026-05-23T14:18:54.333817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2432 · 2026-05-23T14:18:54.838083+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 60720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 2433 · 2026-05-23T14:18:54.838637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2434 · 2026-05-23T14:18:54.891890+00:00_

1	## Review Issues Tracker — policy_ambiguity_safety
2	## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Latest Round: 27
5	
6	# ============================================================
7	# R27 MUST-FIX — IN PROGRESS
8	# ============================================================
9	
10	- id: "R27-MF1"
11	  summary: "信息添加混淆是系统性的，'confound-free' 标签对非 incompleteness 类型同样不准确"
12	  category: method
13	  severity: critical
14	  status: in_progress
15	  first_raised_round: 21
16	  last_seen_round: 27
17	  mentions:
18	    - round: 26
19	      reviewers: [1, 2]
20	      note: "R26-MF3: incompleteness confound 控制方法论不充分——token count 作为信息内容 proxy 有根本缺陷"
21	    - round: 27
22	      reviewers: [1, 2]
23	      note: "R1-N1 + R2-W2 共识。范围扩大：所有类型 unambiguous variant 系统性更长。ρ=0.94 但为 tautological correlation"
24	  action_items:
25	    - round: 27
26	      action: "confound-free→excluding incompleteness；报告 ρ=0.94 + tautological 解释；突出 coreferential 18.7pp + perturbation control + token β 方向"
27	      assigned_to: main_agent
28	      status: in_progress
29	  resolution: ""
30	  resolution_round: null
31	
32	- id: "R27-MF2"
33	  summary: "Type-mechanism dissociation (V=0.45) 核心证据依赖 LLM 编码，人工验证不足"
34	  category: method
35	  severity: critical
36	  status: in_progress
37	  first_raised_round: 22
38	  last_seen_round: 27
39	  mentions:
40	    - round: 26
41	      reviewers: [1, 2]
42	      note: "R26-MF1: construct validity 和 LLM 分类偏好两个 attack vector 汇聚"
43	    - round: 27
44	      reviewers: [1, 2]
45	      note: "R1-N2 + R2 AGREE。V=0.45 完全 LLM-coded，circularity risk。需 bootstrap CI + human κ range"
46	  action_items:
47	    - round: 27
48	      action: "Bootstrap V CI；κ 改报范围 0.34-0.52；承认 V' 不可计算（人工标注无 mechanism 字段）；V' 列为 future work"
49	      assigned_to: main_agent
50	      status: in_progress
51	  resolution: ""
52	  resolution_round: null
53	
54	- id: "R27-MF3"
55	  summary: "跨判官组 ρ=0.0
…[truncated 14634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 2435 · 2026-05-23T14:19:14.513282+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 2436 · 2026-05-23T14:19:16.320452+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1807
}
```

</details>

---


### Tool call

_source line 2437 · 2026-05-23T14:19:16.471354+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2438 · 2026-05-23T14:19:17.324479+00:00_

1	@inproceedings{li_ambiguity_taxonomy_2024,
2	  title={A Taxonomy of Ambiguity Types for {NLP}},
3	  author={Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.},
4	  booktitle={Proceedings of EACL 2024},
5	  year={2024}
6	}
7	
8	@inproceedings{massey_ambiguity_re_2014,
9	  title={Identifying and Classifying Ambiguity for Regulatory Requirements},
10	  author={Massey, Aaron K. and Rutledge, Richard L. and Ant{\'o}n, Annie I. and Swire, Peter P.},
11	  booktitle={22nd IEEE International Requirements Engineering Conference (RE)},
12	  year={2014},
13	  doi={10.1109/RE.2014.6912250}
14	}
15	
16	@techreport{berry_kamsties_2004,
17	  title={From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook},
18	  author={Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.},
19	  institution={University of Waterloo},
20	  year={2004}
21	}
22	
23	@inproceedings{chantree_2006,
24	  title={Identifying Nocuous Ambiguities in Natural Language Requirements},
25	  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},
26	  booktitle={14th IEEE International Requirements Engineering Conference (RE)},
27	  year={2006}
28	}
29	
30	@incollection{wasow_ambiguity_2005,
31	  title={The Puzzle of Ambiguity},
32	  author={Wasow, Thomas and Perfors, Amy and Beaver, David},
33	  booktitle={Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe},
34	  publisher={CSLI Publications},
35	  year={2005}
36	}
37	
38	@article{kennedy_vagueness_2007,
39	  title={Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives},
40	  author={Kennedy, Christopher},
41	  journal={Linguistics and Philosophy},
42	  volume={30},
43	  number={1},
44	  pages={1--45},
45	  year={2007},
46	  doi={10.1007/s10988-006-9008-0}
47	}
48	
49	@article{willis_nocuous_2008,
50	  title={Automatic Identification of Nocuous Ambiguity},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 2439 · 2026-05-23T14:19:17.577357+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_28/ 2>/dev/null || echo \"NO_DIR\"",
  "description": "Check submitted PDF directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_28/ 2>/dev/null || echo \"NO_DIR\"",
    "description": "Check submitted PDF directory"
  }
}
```

</details>

---


### Tool result

_source line 2440 · 2026-05-23T14:19:17.828779+00:00_

total 544
drwxr-xr-x  2 ubuntu ubuntu   4096 May 23 14:17 .
drwxr-xr-x 69 ubuntu ubuntu  12288 May 23 14:17 ..
-rw-r--r--  1 ubuntu ubuntu 538809 May 23 14:16 submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2441 · 2026-05-23T14:19:51.219352+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 2442 · 2026-05-23T14:20:11.818933+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20599
}
```

</details>

---


### Tool call

_source line 2443 · 2026-05-23T14:20:11.970366+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查**方法严谨性**。\n\n## 论文信息\n- **标题**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety\n- **Venue**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板 (review mode)，long paper 正文 ≤8 页，引用无页数限制，Limitations 必选且不计页数，double-blind\n- **论文路径**: projects/policy_ambiguity_safety/docs/paper/main.tex\n- **PDF**: projects/policy_ambiguity_safety/artifacts/review_round_28/submitted.pdf\n\n## 你的审查侧重\n\n**方法严谨性**，重点覆盖：\n\n1. **因果推断设计**：matched-pair design 是否真正隔离了 ambiguity 的因果效应？perturbation control 是否充分？信息添加混淆（尤其 incompleteness）的处理是否可信？\n2. **统计分析**：McNemar test、TOST equivalence、Cramér's V、ICC 等统计方法使用是否正确？SESOI ±15pp 的选择是否合理？多重比较校正是否恰当？\n3. **Evaluation pipeline**：cross-judge design（GPT-5.4 判 3 个模型，GPT-4.1 判 2 个）是否引入系统偏差？human validation（κ=0.733）是否充分？per-type reliability 差异是否影响 claims？\n4. **Type-mechanism dissociation**：V=0.45 完全依赖 LLM coding，circularity risk 如何？human mechanism κ=0.15（collapsed 0.34-0.52）意味着什么？\n5. **Controls 充分性**：perturbation control（n=300）、within-family ICC（0.919）、cross-benchmark replication（SOPBench）各自的证据强度\n6. **Variance decomposition**：clause 22.4% vs type 0.4% vs condition 15.8% vs model 1.0% vs residual 60.8%——解释是否合理？60.8% residual 的 systematic vs stochastic 拆分是否可信？\n7. **温度设定**：temperature=0 对结论泛化性的影响\n8. **样本构造**：300 clause pairs 的生成方式（template-based pipeline + human review）是否存在偏差？96% initial agreement 是否过高暗示任务过简？\n\n请逐条列出 Strengths 和 Weaknesses（按 Must-Fix / Should-Fix / Minor 分级），提出 Questions，并给出初步 Overall Assessment（使用 EMNLP 2026 ARR 评分标准：1-5 分）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查**方法严谨性**。\n\n## 论文信息\n- **标题**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety\n- **Venue**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板 (review mode)，long paper 正文 ≤8 页，引用无页数限制，Limitations 必选且不计页数，double-blind\n- **论文路径**: projects/policy_ambiguity_safety/docs/paper/main.tex\n- **PDF**: projects/policy_ambiguity_safety/artifacts/review_round_28/submitted.pdf\n\n## 你的审查侧重\n\n**方法严谨性**，重点覆盖：\n\n1. **因果推断设计**：matched-pair design 是否真正隔离了 ambiguity 的因果效应？perturbation control 是否充分？信息添加混淆（尤其 incompleteness）的处理是否可信？\n2. **统计分析**：McNemar test、TOST equivalence、Cramér's V、ICC 等统计方法使用是否正确？SESOI ±15pp 的选择是否合理？多重比较校正是否恰当？\n3. **Evaluation pipeline**：cross-judge design（GPT-5.4 判 3 个模型，GPT-4.1 判 2 个）是否引入系统偏差？human validation（κ=0.733）是否充分？per-type reliability 差异是否影响 claims？\n4. **Type-mechanism dissociation**：V=0.45 完全依赖 LLM coding，circularity risk 如何？human mechanism κ=0.15（collapsed 0.34-0.52）意味着什么？\n5. **Controls 充分性**：perturbation control（n=300）、within-family ICC（0.919）、cross-benchmark replication（SOPBench）各自的证据强度\n6. **Variance decomposition**：clause 22.4% vs type 0.4% vs condition 15.8% vs model 1.0% vs residual 60.8%——解释是否合理？60.8% residual 的 systematic vs stochastic 拆分是否可信？\n7. **温度设定**：temperature=0 对结论泛化性的影响\n8. **样本构造**：300 clause pairs 的生成方式（template-based pipeline + human review）是否存在偏差？96% initial agreement 是否过高暗示任务过简？\n\n请逐条列出 Strengths 和 Weaknesses（按 Must-Fix / Should-Fix / Minor 分级），提出 Questions，并给出初步 Overall Assessment（使用 EMNLP 2026 ARR 评分标准：1-5 分）。"
  }
}
```

</details>

---


### Tool result

_source line 2444 · 2026-05-23T14:20:28.735505+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16765
}
```

</details>

---


### Tool call

_source line 2445 · 2026-05-23T14:20:28.937817+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查**新颖性与完整性**。\n\n## 论文信息\n- **标题**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety\n- **Venue**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板 (review mode)，long paper 正文 ≤8 页，引用无页数限制，Limitations 必选且不计页数，double-blind\n- **论文路径**: projects/policy_ambiguity_safety/docs/paper/main.tex\n- **PDF**: projects/policy_ambiguity_safety/artifacts/review_round_28/submitted.pdf\n\n## 你的审查侧重\n\n**新颖性与完整性**，重点覆盖：\n\n1. **贡献增量**：相对 DRIP-R（400 scenarios, 5 RE ambiguity types, correlational）、PolicyBank（iterative refinement）、AgentPex（procedural violations）等同期工作，本文的 matched-pair causal design 是否提供了质的提升？三个 contributions（因果效应、disambiguation neglect + systematic nocuity、type-mechanism dissociation）各自的新颖性如何？\n2. **Related work 覆盖**：是否遗漏重要相关工作？特别关注 (a) ambiguity in agent safety 领域、(b) requirements engineering 跨界引用、(c) psycholinguistics 引用的准确性和相关性\n3. **叙事框架**：\n   - \"Nocuous\" 术语的语义反转（Berry: convergent=innocuous → 本文: convergent=nocuous）论证是否充分？\n   - Taxonomy 定位（从 risk classifier → diagnostic instrument）的转变是否清晰？\n   - \"Ambiguity\" 的广义使用（涵盖 vagueness、incompleteness、normative conflict）是否合理？\n4. **写作质量**：\n   - Abstract 是否在 200 words 以内？信息密度是否合适？\n   - Introduction 的叙事弧是否清晰（问题 → gap → 方法 → 发现）？\n   - Discussion 是否过于简短？Conclusion 是否充分？\n   - Limitations 是否覆盖关键限制（合成数据、domain 限制、temperature=0、LLM coding）？\n5. **格式合规**：\n   - 正文是否 ≤8 页？\n   - Double-blind 匿名是否完整（无自引泄露、无 acknowledgments、无机构信息）？\n   - 引用格式是否一致（natbib/ACL style）？\n   - Appendix 结构是否合理？\n6. **Domain scope**：标题/claims 是否与实验范围（两个 customer-service domains）匹配？\n\n请逐条列出 Strengths 和 Weaknesses（按 Must-Fix / Should-Fix / Minor 分级），列出 Missing References（如有），提出 Questions，并给出初步 Overall Assessment（使用 EMNLP 2026 ARR 评分标准：1-5 分）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查**新颖性与完整性**。\n\n## 论文信息\n- **标题**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety\n- **Venue**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板 (review mode)，long paper 正文 ≤8 页，引用无页数限制，Limitations 必选且不计页数，double-blind\n- **论文路径**: projects/policy_ambiguity_safety/docs/paper/main.tex\n- **PDF**: projects/policy_ambiguity_safety/artifacts/review_round_28/submitted.pdf\n\n## 你的审查侧重\n\n**新颖性与完整性**，重点覆盖：\n\n1. **贡献增量**：相对 DRIP-R（400 scenarios, 5 RE ambiguity types, correlational）、PolicyBank（iterative refinement）、AgentPex（procedural violations）等同期工作，本文的 matched-pair causal design 是否提供了质的提升？三个 contributions（因果效应、disambiguation neglect + systematic nocuity、type-mechanism dissociation）各自的新颖性如何？\n2. **Related work 覆盖**：是否遗漏重要相关工作？特别关注 (a) ambiguity in agent safety 领域、(b) requirements engineering 跨界引用、(c) psycholinguistics 引用的准确性和相关性\n3. **叙事框架**：\n   - \"Nocuous\" 术语的语义反转（Berry: convergent=innocuous → 本文: convergent=nocuous）论证是否充分？\n   - Taxonomy 定位（从 risk classifier → diagnostic instrument）的转变是否清晰？\n   - \"Ambiguity\" 的广义使用（涵盖 vagueness、incompleteness、normative conflict）是否合理？\n4. **写作质量**：\n   - Abstract 是否在 200 words 以内？信息密度是否合适？\n   - Introduction 的叙事弧是否清晰（问题 → gap → 方法 → 发现）？\n   - Discussion 是否过于简短？Conclusion 是否充分？\n   - Limitations 是否覆盖关键限制（合成数据、domain 限制、temperature=0、LLM coding）？\n5. **格式合规**：\n   - 正文是否 ≤8 页？\n   - Double-blind 匿名是否完整（无自引泄露、无 acknowledgments、无机构信息）？\n   - 引用格式是否一致（natbib/ACL style）？\n   - Appendix 结构是否合理？\n6. **Domain scope**：标题/claims 是否与实验范围（两个 customer-service domains）匹配？\n\n请逐条列出 Strengths 和 Weaknesses（按 Must-Fix / Should-Fix / Minor 分级），列出 Missing References（如有），提出 Questions，并给出初步 Overall Assessment（使用 EMNLP 2026 ARR 评分标准：1-5 分）。"
  }
}
```

</details>

---


### Tool result

_source line 2446 · 2026-05-23T14:20:30.554834+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1617
}
```

</details>

---


### Assistant

_source line 2447 · 2026-05-23T14:20:43.249768+00:00_

已派发：
- **视觉审查 Agent**：已启动（fire-and-forget）
- **Reviewer 1**（方法严谨性）：已启动
- **Reviewer 2**（新颖性/完整性）：已启动

外部审稿（Stanford Agentic Reviewer）未启用，跳过。

等待两位 Reviewer 完成独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 229

## Round 229

2 recorded events


### User

_source line 2448 · 2026-05-23T14:28:12.021080+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 核心因果发现 (C1) 实验设计扎实、控制充分、跨基准复制可信；但 type-mechanism dissociation 依赖 LLM 编码存在循环性、信息添加混淆未在所有类型上充分解决、temperature=0 唯一条件限制了泛化性，三项叠加使方法严谨性停留在 borderline 水平。

## 官方维度打分（ACL ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | C1（二元歧义效应）控制链完整（perturbation control、ICC、SOPBench、cross-judge validation），但 C2 的 type 级分析因 auth-scope 测量不稳定 (κ=0.385) 和 incompleteness confound 而削弱；Section 6 机制分析循环性是最主要的方法论缺陷 |
| Excitement | 3.5/5 | 研究问题实用且重要，systematic nocuity（77% permissive attractor）发现有新意；但核心发现"歧义→更多违规"在概念上并不意外，贡献以经验量化为主 |
| Reproducibility | 4/5 | 300 clause pairs + 评估 pipeline + 分析脚本承诺公开；模型 API 调用参数详细（temperature=0, top_p=1, max_tokens=4096, 日期 May 20 2026）；但 clause pair 构建过程描述存在内部矛盾（见 N1） |
| Overall Assessment | 3.5/5 | Borderline Conference |
| Confidence | 4/5 | 认真通读了全文含附录 23 页，核查了统计方法和实验设计细节 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Clause pair 构建方法描述自相矛盾

- 具体位置：§4.2 (p.5) vs. Appendix T (p.17 of PDF, §"Clause Pair Construction")
- 问题：§4.2 写道 "Clause pairs are generated through a **template-based pipeline** and reviewed by two independent annotators"，暗示某种自动化生成流程。但 Appendix T 明确声称 "The 300 clause pairs... were **hand-crafted** as structured data records... **No automated over-generation or filtering was employed**; all pairs were authored directly to the target count of 50 per type." 这两处描述互相矛盾：到底是 template-based pipeline 生成的，还是完全手工构建的？
- 为什么影响接收：这直接影响可复现性和刺激偏差评估。如果是自动化生成，需要披露模板结构和生成算法；如果是手工构建，"template-based pipeline" 的说法是误导。审稿人无法判断刺激材料的构建偏差。
- 建议修改方向：统一两处描述，明确说明构建过程中是否有自动化步骤、模板的具体形式、以及 "pipeline" 包含哪些环节。

**N2** [critical] 信息添加混淆（information-addition confound）未在全部类型上充分讨论

- 具体位置：§5.1, Appendix F (§"Incompleteness Confound Analysis"), Appendix Q (§"Per-Type Clause Length Analysis"), Table 13
- 问题：论文详细讨论了 incompleteness 的信息添加混淆（49.2pp 效应被标注为 upper bound），但对 authorization scope（Δtoken = 36.1 words，所有类型中最大）同样存在的信息添加混淆讨论不足。从 Table 14 (Appendix U) 的示例来看，auth-scope 的 unambiguous variant 不仅消解了歧义，还添加了具体的美元阈值和流程细节（如 "$50 without supervisor approval; amounts above $50 require supervisor sign-off"），这远非 "minimal edit"。论文仅以 "auth scope has the largest delta yet lower violation rates than incompleteness" 作为反驳，但这不排除 auth-scope 的 36pp 效应中有相当比例来自信息添加而非纯歧义消解。
- 补充论据的弱点：token count 回归 (β=+0.027) 是一个过于粗糙的 proxy——它测量的是字符量而非语义信息量。longer clauses → more violations 可能反映的是长条款本身更难遵循，而非信息添加假说被证伪。coreferential 的 lower bound (18.7pp, Δtoken=0) 确实证明了纯歧义消解的效应存在，但不能用来 bound auth-scope 或 incompleteness 各自的效应分解。
- 为什么影响接收：C1 的整体效应 (+34pp) 是稳健的（排除 incompleteness 后仍有 +31pp），但 C2（type partial ordering）和 Table 2 中各类型的具体 Δpp 解释为纯歧义效应是有问题的，至少对 auth-scope 和 incompleteness 应更明确地标注为 "ambiguity resolution + information addition" 的混合效应。
- 建议修改方向：(1) 按类型报告信息添加混淆的程度（可以通过语义相似度等更精细的指标，而非仅用 token count）；(2) 在 Table 2 中对 Δtoken > 25 words 的类型加注信息添加警告（目前仅 incompleteness 有 † 标注）；(3) 在 §5.1 和 Discussion 中明确区分 "ambiguity-only" 效应（best case: coreferential 18.7pp）和 "ambiguity + information" 混合效应。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Type-mechanism dissociation (V=0.45 vs V=0.14) 的跨维度比较方法论缺陷

- 具体位置：§5.1 ("The taxonomy predicts failure mechanisms more strongly than violation rate (V = 0.45 vs. 0.14)"), §6 Figure 4 caption, Discussion
- 问题：Cramér's V 在不同维度的列联表之间不可直接比较。V=0.45 来自 6×3（或 6×5）表，V=0.14 来自 6×2 表。V 的归一化因子是 √(χ²/(N×min(r-1,c-1)))，分母不同使比较失效。论文在 Appendix V 的脚注中承认 "values are not directly comparable as ratios"，但正文和 Discussion 仍然反复使用 "V = 0.45 vs. 0.14" 作为核心论据，甚至在 Appendix V 中报告 "16.8× NMI ratio"。
- 建议修改方向：(1) 使用维度无关的度量（如 normalized mutual information，已在 Appendix V 报告但未充分利用）作为主论据；(2) 如仍保留 V 比较，需在正文（而非仅脚注）中明确说明维度不同导致的比较局限性；(3) 考虑使用 partial association measures 或 log-linear models 进行更严格的比较。

**W2** [warning] LLM 编码 LLM 失败模式的循环性问题

- 具体位置：§6 (Error Analysis), §6.1, Appendix V (Type-Mechanism Mutual Information), Appendix AF (Human Validation)
- 问题：用 LLM (GPT-4.1) 对其他 LLM 的失败 trace 进行机制编码存在根本性循环：(1) 失败 trace 的行为模式是 LLM 训练的产物，LLM coder 可能识别的是训练相关性而非真实机制区别；(2) 即使 coder prompt 排除了 ambiguity type label，trace 本身包含了充分的行为线索让 LLM coder 进行系统性分类——这种分类的一致性可能反映 LLM 之间的共享偏差（shared training bias）而非 ground-truth mechanism distinction。
- 人类验证反面证据：human mechanism κ=0.15 (collapsed 后 0.34-0.52) 远低于 LLM κ=0.52，暗示 LLM 的高一致性可能来自系统性偏差而非任务可靠性。论文声称这反映 "fuzzy boundary between spurious compliance and structural misparse"，但一个同样可信的解释是：五类机制方案在认知上不可靠——如果人类无法可靠区分，这些类别的 construct validity 就存疑。
- 论文的处理方式：将 V=0.45 标注为 upper bound、将 Section 6 标注为 [Exploratory]，这两点是正确的。但 Discussion 和 Abstract 中仍然将 type-mechanism dissociation 作为主要贡献之一（"type--mechanism dissociation establishes the taxonomy as a diagnostic instrument"），超出了数据支撑的程度。
- 建议修改方向：(1) 在 Discussion 中降低 mechanism analysis 的权重，明确表示 circularity 使其只能作为初步线索；(2) 考虑在 human validation 中使用 collapsed 4-category scheme 作为参考标准重新计算 V；(3) 对 systematic nocuity (§6.3) 的解读保持更保守的措辞。

**W3** [warning] Authorization scope 的测量不稳定性威胁 C2 和 C4

- 具体位置：§4.4 (cross-judge κ=0.385 for auth scope), §5.2, Appendix R (judge group rankings ρ=0.09), Appendix AB (cross-judge validation), Appendix O (C4 without auth scope)
- 问题：Authorization scope 在多个指标上是异常值：(1) 最低 cross-judge agreement (κ=0.385, n≈17)；(2) 最大跨模型 range (52pp: Claude 12% vs GPT-5.4 64%)；(3) judge-group type ranking ρ=0.09 完全由 auth-scope rank reversal 驱动（排除后 ρ=0.90）；(4) C4 交互效应完全由 auth-scope 驱动（排除后 p=0.97）；(5) per-type ICC 最低 (0.29，replication ICC = -0.006)。这些指标共同指向一个结论：auth-scope 作为一个 construct 的操作化质量不足以支撑强因果推断。
- 论文已做的工作：Appendix O 和 P 报告了排除 auth-scope 后的核心分析（C1 稳健，variance decomposition 稳定），这很好。
- 遗留问题：尽管排除分析证明 auth-scope 不驱动整体结论，但 Table 2 中 auth-scope 的 +36.0pp 效应仍被平等地与其他类型一起报告和解读。鉴于 κ=0.385 和 ICC=0.29 的低信度，这个数字的可信度远低于其他类型。
- 建议修改方向：在 Table 2 中对 auth-scope 加注信度警告（类似 incompleteness 的 † 标注，目前仅有 ‡ 标注 lowest κ 但没有解释影响）；在 §5.1 或 §5.2 中明确讨论 auth-scope 低信度对其效应估计可靠性的影响。

**W4** [warning] Temperature=0 唯一条件的泛化局限

- 具体位置：§4.3 ("All API calls use temperature = 0"), Limitations
- 问题：Temperature=0 测量模型的 modal interpretation，这在操作层面有意义。但存在两个方法论问题：(1) 它人为提高了 matched-pair 内的一致性和 ICC——在 temperature > 0 下，两个条件都会产生更多变异，matched-pair 差异可能缩小或扩大，方向未知；(2) 它消除了 tail-risk 行为——在实际部署中，stochastic sampling 可能使某些"安全"的条款偶尔产生违规，这是论文完全未捕捉的。论文声称 "higher temperatures would likely increase variance in both conditions" 但承认 "we have no temperature > 0 pilot data"。
- 为什么重要：如果 temperature > 0 下效应显著缩小（例如因为 stochastic sampling 在 unambiguous 条件下也产生更多 baseline violations），C1 的实际部署意义就需要重新评估。
- 建议修改方向：(1) 即使是一个小规模 pilot（如 1 个模型 × 2 个 temperature × 50 pairs）也能显著加强论文；(2) 在 Limitations 中更明确讨论 temperature=0 可能导致的系统性偏差方向（不仅是 "variance increases"，而是对 treatment effect 的影响）。

**W5** [warning] 合成刺激的生态效度 + 96% initial agreement 暗示任务过简

- 具体位置：§4.2, Appendix T, Appendix AD (Real-World Prevalence)
- 问题：96% initial agreement (287/300, κ=0.95) 异常高，暗示歧义类型的判别在构建的 clause pairs 中可能过于明显。自然语言中的歧义通常是渐进的、多重的、依赖上下文的——一个条款可能同时包含多种歧义，且歧义程度不一。论文的 "exactly one instance of the target type" 设计（§4.2）使得每个条款只有一种"干净"的歧义，这在方法上是正确的（隔离 IV），但在生态效度上是有代价的。Appendix AD 的 real-world prevalence audit 部分回应了这一问题，但其 inter-annotator κ=0.295（LLM judges）的低一致性也表明，自然歧义的识别远比合成歧义困难。
- SOPBench 复制的启示：SOPBench 效应 (+12.7pp) 仅为 τ²-bench 的 37%，论文提供了三个结构性解释（measurement grain、baseline compression、interaction depth），但这些是 post-hoc 的。一个同样可信的解释是：SOPBench 使用了更接近真实 SOP 的歧义，效应自然更小。
- 建议修改方向：(1) 在 §4.2 中讨论 96% agreement 是否暗示 constructed ambiguity 过于明显；(2) 在 Discussion 中更坦诚地讨论 34pp 效应可能是 upper bound 的原因不仅是 incompleteness confound，还包括合成刺激的人工清晰度。

---

## 小问题（不影响接收）

- **M1**: Table 2 中 SOPBench replication 被引用为 "+12.7pp"，但 Table 21 (Appendix AA) 中五个模型的 unweighted mean 为 (20.1+16.5+15.1+6.1+5.3)/5 = 12.62pp，应为 12.6pp，+12.7 是四舍五入但应标注是 unweighted mean。
- **M2**: §5.1 中 McNemar OR = 15.1 基于 discordant pairs (n=580)，应明确说明这不同于 crude marginal OR，避免读者误解效应量级。论文在 §4.6 中有简短提及，但在结果部分首次报告时未重申。
- **M3**: Abstract 声称 "500 clause pairs"（可能是 PDF 中 abstract 的措辞——实际我看到的是"300 clause pairs"），请核实 abstract 与正文一致性。[经核实：abstract 说的是 "300 clause pairs"，此处无误。]
- **M4**: Appendix AD (Real-World Prevalence) 中 LLM judge 的 κ=0.295 非常低，但论文仍基于此报告了 87% 的文档级歧义率。应更明确讨论低 κ 对流行率估计可靠性的影响。
- **M5**: §4.2 中 "3 episodes lost to API errors in one Qwen3 batch" → 是否进行了 sensitivity analysis 排除这 3 个缺失值不影响结论？如果不影响可以简述。

---

## 主要优势

1. **实验设计扎实 (C1)**：matched-pair 设计正确隔离了歧义作为 IV；perturbation control、within-family ICC=0.919、SOPBench 跨基准复制形成了完整的控制链。C1 的 +34pp 效应在排除 incompleteness 后仍有 +31pp，跨 7 个模型、2 个基准均为正效应，因果证据强度高。

2. **统计方法规范**：McNemar 配对检验、TOST 等价检验（7 个 margin 的敏感性分析）、Holm-Bonferroni 校正、bootstrap cluster analysis 等方法选择恰当。C3（layer effect）未通过校正后被正确标记为 inconclusive，显示了统计纪律。

3. **Cross-judge validation 全面**：三个独立 judge (GPT-4.1, Claude 4.6, Gemini 2.5 Pro) 的 Fleiss' κ=0.717，无 same-family leniency，model ranking 和 type ranking 基本一致。Human validation (inter-annotator κ=0.798, human-LLM κ=0.733) 进一步确认了 violation detection 的可靠性。

4. **Claims 标定诚实**：C1/C2 为 supported，C3 为 inconclusive，C4 和 mechanism analysis 为 exploratory。Incompleteness 效应标注为 upper bound。这种分级的 claim calibration 是高质量实证论文的标志。

5. **Variance decomposition 和 residual 分析透明**：ICC-based 拆分（15% stochastic, 46% systematic-but-unmeasured）为 60.8% residual 提供了可解释的分解，clause-level heterogeneity 的讨论诚实且有启发性。

6. **Appendix 质量高**：23 页论文中 15 页附录覆盖了几乎所有可预期的 reviewer 疑问（confound analysis、per-type reliability、TOST sensitivity、cross-domain、排除分析、clause examples），附录不是凑数而是真正加强论证。

---

## Questions for Authors

Q1: §4.2 "template-based pipeline" 和 Appendix T "hand-crafted, no automated over-generation" 之间的矛盾如何解释？请明确构建过程中是否涉及任何自动化步骤。

Q2: 对于 authorization scope (Δtoken=36.1 words)，是否可以提供类似 incompleteness 的 confound analysis？具体来说，排除 auth-scope 后的五类型 TOST 结构是否变化？（Appendix P 已部分回答，但未报告逐类型 TOST。）

Q3: 是否有 temperature > 0 的任何初步数据（即使是 informal pilot）？如果没有，是否有理论论证 temperature 对 matched-pair 差异的预期影响方向？

Q4: Human mechanism coding κ=0.15：两位标注者是否接受了标注培训？如果在培训后重新标注一个子集，κ 是否有提升空间？

Q5: 96% initial agreement on type classification——是否计算了 prevalence-adjusted bias-adjusted kappa (PABAK) 以检验高 agreement 是否部分由 prevalence effect 驱动？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2449 · 2026-05-23T14:28:20.095526+00:00_

Reviewer 1 审稿意见已收到，评分 3.5/5。等待 Reviewer 2 完成审稿后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 230

## Round 230

2 recorded events


### User

_source line 2450 · 2026-05-23T14:28:28.206644+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：我给出 **Overall 3.5/5（Borderline Conference）**，Soundness 3.5，Excitement 3.5。

核心判断：
- **C1（歧义→违规 +34pp）** 的因果证据链扎实，控制完整，是论文最强的贡献
- 两个 **Must-Fix** 问题：(1) clause pair 构建方法描述自相矛盾（§4.2 "template-based pipeline" vs Appendix T "hand-crafted"）影响可复现性；(2) 信息添加混淆讨论不充分——auth-scope（Δtoken=36.1 words）与 incompleteness 同样存在该混淆但缺乏对等的标注和分析
- 四个 **Should-Fix**：V=0.45 vs V=0.14 跨维度比较方法论缺陷、LLM 编码循环性（human κ=0.15）、auth-scope 测量不稳定、temperature=0 唯一条件

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2451 · 2026-05-23T14:28:34.788439+00:00_

收到 Reviewer 1 审稿意见。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 231

## Round 231

6 recorded events


### User

_source line 2452 · 2026-05-23T14:34:15.125324+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：新颖性与完整性

**论文**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety
**Venue**: EMNLP 2026 (ARR May cycle)

---

## 总体评分

**Overall Assessment**: 3.5 (Borderline Conference)

**一句话总结**: 匹配对因果设计是对该领域既有相关性研究的方法论升级，实验执行充分且透明，但核心概念贡献（type–mechanism dissociation 作为 "diagnostic instrument"）依赖低人间一致性的 failure mechanism 编码（κ = 0.15），Discussion + Conclusion 过于简短，Berry "nocuous" 术语反转的概念论证不够深入。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 (Strong) | 匹配对因果设计严谨，TOST 等价检验 + bootstrap 聚类 + SOPBench 跨基准复现 + human validation (100 episodes) 增强稳健性；主要扣分点在 failure mechanism 编码的人间一致性过低（κ = 0.15），影响 contribution (3) 可信度 |
| Excitement | 3/5 (Interesting) | 因果设计对该领域有方法论价值，disambiguation neglect (4.6% awareness) 是令人印象深刻的实证发现；但核心发现方向符合预期（歧义有害），更新颖的 nocuity 和 dissociation 均为探索性，且 scope 限于两个客服 domain |
| Reproducibility | 4/5 (Could mostly reproduce) | 实验设置描述充分，承诺开源数据和代码，API 模型 temperature=0 可精确复现；模型版本固定于 2026 年 5 月，未来复现需对应版本 |
| Confidence | 4/5 (Quite sure) | 对论文做了逐节精读（含全部 23 页附录），对因果推断方法和 NLP agent safety 领域有充分评估能力 |
| Datasets | 4/5 (Useful) | 300 matched clause pairs + 六类型 taxonomy 是有价值的资源，可供后续研究使用 |
| Software | 3/5 (Potentially useful) | 评估 pipeline 有一定复用价值，但与 τ²-bench 绑定较紧 |
| Author Identity | 1/5 (No educated guess) | 匿名完整，未发现泄露 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Type–mechanism dissociation 的人间一致性过低，无法充分支撑 "diagnostic instrument" 的核心定位

- **具体位置**：Section 6 (analysis.tex), Limitations, Appendix AF
- **问题**：论文将 type–mechanism dissociation 作为三大贡献之一（Introduction: contribution (3)），并基于 V = 0.45 将 taxonomy 重新定位为 "diagnostic instrument rather than a risk classifier"。然而 failure mechanism 编码的人间一致性仅 κ = 0.15（Appendix AF），即使合并 spurious-compliance/structural-misparse 边界后也仅上升至 0.34–0.52。论文自身承认 "we treat V = 0.45 as an upper bound"，但仍将此 V 值作为支撑 "diagnostic instrument" 定位的核心论据。

  关键疑问：一个人类标注者都无法可靠区分的 failure mechanism 分类体系，如何成为实际部署的"诊断工具"？LLM coder 的高一致性（κ = 0.52, Gwet's AC₁ = 0.62）可能反映的是 LLM 之间的 shared systematic bias（类似于论文自身发现的 convergent nocuity），而非真正的 type→mechanism 映射。论文在脚注中正确指出 6×5 表的 V 比 6×2 更保守，但统计论证不能替代人间验证。

- **为什么影响接收**：这是论文最核心的概念重构。如果 failure mechanism 编码本身不可靠，contribution (3) 的可信度大幅下降。论文明确标记 Section 6 为 "[Exploratory]"，但 Abstract 和 Introduction 中的表述（"establishes the taxonomy as a diagnostic instrument"）并未充分传达这一不确定性——"establishes" 暗示了确认性发现，与 "[Exploratory]" 标签矛盾。

- **建议修改方向**：
  (a) 将 Abstract 和 Introduction 中的 "establishes" 改为 "suggests" 或 "provides exploratory evidence for"，与 Section 6 的 [Exploratory] 标签保持一致；
  (b) 讨论 LLM coder 一致性高于人间一致性的可能解释——是 genuine signal 还是 shared coding bias？这与论文自身的 convergent nocuity 发现形成有趣的 meta-level 张力；
  (c) 在 Abstract 中报告原始 κ = 0.15（当前只报告 collapsed κ = 0.34–0.52，容易给读者造成人间一致性尚可的印象）。

---

**N2** [critical] Discussion + Conclusion 过于简短，未充分展开三项贡献的意义

- **具体位置**：discussion.tex (~80 词, 1 段), conclusion.tex (~70 词, 3 句话)
- **问题**：Discussion 仅一段话，只讨论了 type–mechanism dissociation 和 intervention design，完全未讨论 disambiguation neglect 和 systematic nocuity 的理论意义、与现有认知科学/RE 文献的关系、以及对 LLM agent 开发者的实际建议。Conclusion 也仅 3 句话。

  对于一篇声称有三项贡献的论文，两节合计约 150 词的总结性讨论严重不足。具体缺失的讨论点：
  - Disambiguation neglect (4.6% awareness) 与 LLM sycophancy/instruction-following bias 的关系？
  - Systematic nocuity 对 multi-agent 或 agreement-based evaluation 范式的启示？
  - 因果效应的实际可操作性：开发者应如何使用这些发现来改进 policy specification 流程？
  - 与 RE 领域数十年 ambiguity detection 工具链的关系——NLP 社区可从 RE 借鉴什么？

- **为什么影响接收**：一篇完整的研究论文应有充分的 Discussion 将发现放入更大的学术语境中。当前版本在方法和实验上非常充分，但在 implications 方面留白过多，削弱了论文的 "so what" 感。8 页正文中，Discussion + Conclusion 仅占约 0.2 页，与前面 5+ 页的实验内容极不平衡。

- **建议修改方向**：将 Discussion 扩展至至少半页（~300 词），分段讨论三项贡献各自的 theoretical implications 和 practical recommendations。可适度压缩 Section 5（Results）或 Section 6 中的重复细节来腾出空间。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Berry "nocuous" 术语反转的概念论证不够深入

- **具体位置**：Introduction (§1 第2段), Section 6.3
- **问题**：论文采用 Berry et al. (2004) 的 nocuous/innocuous 框架并进行语义反转——Berry 定义 stakeholder divergence = nocuous, convergence = innocuous；本文认为 LLM convergence on wrong interpretation = nocuous。Introduction 的论证为："Unlike human teams, where convergence reflects shared domain knowledge, agent convergence reflects shared training biases operating on identical inputs."

  这个论证实际上说明的不是 Berry 框架的"反转"，而是 Berry 框架**不适用于 LLM agents**。Berry 框架的前提是人类利益相关者通过共享领域知识达成一致理解；LLM 的收敛是训练偏差驱动的，完全不同的机制。将此称为 "inverting Berry's framework" 有过度修辞的嫌疑——更精确的表述是 "Berry's nocuity criterion breaks down for LLM agents because their convergence mechanism differs fundamentally from human convergence."

  此外，Section 6.3 的 "systematic nocuity" 基于 41.3% 的 convergent violations（≥3/5 模型一致），但这些模型共享大量预训练数据（WebText, CommonCrawl 等）。收敛本身可能是 trivially expected 的（shared training data → shared biases → shared errors），论文应讨论这种收敛在多大程度上由共享训练数据驱动 vs. 由歧义文本的结构特征驱动。

- **建议**：(a) 将 "inverting Berry" 改为更精确的表述（如 "shows Berry's criterion is insufficient for LLM agents"）；(b) 按模型家族分析 convergence 模式（OpenAI 内部 vs. 跨厂商），区分 training-data-driven 和 ambiguity-structure-driven 的收敛。

**W2** [warning] "Ambiguity" 的广义使用涵盖了 incompleteness，影响 headline result 的解释

- **具体位置**：Section 3, Section 5.1, Abstract
- **问题**：论文采用广义的 "ambiguity" 定义，明确包含 incompleteness（缺失条件或边界条件）。但 incompleteness 在传统语言学和 RE 文献中通常归类为 underspecification 而非 ambiguity——ambiguity 指同一文本允许多种解释，incompleteness 指文本根本没有提供相关信息。

  这一分类选择对 headline result 有实质影响：incompleteness 贡献了最大的效应（+49.2 pp, Table 2），且其 confound 结构与其他类型根本不同（Appendix F: unambiguous variant 添加了新信息而非消除歧义）。虽然论文报告了 excluding incompleteness 的效应（+31.0 pp）并在 Appendix F、H 做了详尽 confound 分析，但 Abstract 的 headline 仍以 +34.0 pp（含 incompleteness）为主。

  Section 3 的辩护（"in the policy-specification domain, these distinctions are less salient"）合理，但 Introduction 第一句 contribution 即报 "+34.0 pp" 而非 "+31.0 pp"。

- **建议**：在 Abstract 和 Introduction 中更 prominently 呈现 excluding incompleteness 的效应（+31.0 pp）作为 confound-minimized 估计，将 +34.0 pp 定位为 inclusive upper bound。Conclusion 中提到 coreferential 的 +18.7 pp 作为 confound-minimized lower bound，这个做法很好，应前移到 Abstract。

**W3** [warning] SOPBench 复现效应大幅缩小（+12.7 pp vs. +34.0 pp），需更多讨论

- **具体位置**：Abstract, Section 5.1, Appendix E
- **问题**：SOPBench 跨基准复现的效应量仅为主实验的 37%（+12.7 pp vs. +34.0 pp）。论文将此解释为 "directional consistency"，但 2.7 倍的效应量差异值得更深入讨论。可能的解释包括：(a) SOPBench 的 policy 结构不同，(b) τ²-bench 的合成 clause pairs 夸大了效应，(c) SOPBench 的评估 pipeline 不同。如果 +12.7 pp 是更接近真实部署的估计，则论文的 practical significance 需要重新评估。

  此外，Abstract 中 "3/5 models significant at p < 0.05" 与 Appendix E 的具体数据可能存在轻微不一致——Appendix E 报告 3 个模型在 p < 0.01 显著，GPT-5.4 在 p = 0.032（< 0.05），DeepSeek-V3 不显著（p = 0.16）。按 p < 0.05 标准应为 4/5 而非 3/5。

- **建议**：(a) 在 Discussion 中用一段讨论 τ²-bench 和 SOPBench 效应量差异的原因；(b) 核查 Abstract 中 SOPBench 的 "3/5 at p < 0.05" 是否应为 "3/5 at p < 0.01" 或 "4/5 at p < 0.05"。

---

## 小问题（不影响接收）

- **M1**: analysis.tex 末尾使用 `\enlargethispage{26\baselineskip}`（约 4.3 英寸扩展）。虽然 PDF 中主文本仍在 8 页内，但 page 8 底部 margin 可能被大幅侵占，建议检查是否符合 ACL 模板 margin 要求。审稿系统可能自动检测 margin 违规。

- **M2**: Abstract 仅报告 collapsed κ = 0.34–0.52 用于人间 mechanism 一致性，未提及原始 κ = 0.15。建议在 Abstract 中加入 "raw κ = 0.15" 以透明呈现。

- **M3**: Figure 3 (per-type effect sizes, page 7) 中 authorization scope 的 CI 上限标注不够清晰，可能超出图表显示范围。

- **M4**: Conclusion 中提到 ">89% disambiguation neglect"——这个数字来源不够明确。Section 6.2 报告 awareness = 4.6%（即 95.4% neglect），而非 89%。请核实。

---

## Missing References

未发现重大遗漏。Related work 覆盖了主要并发工作（DRIP-R、PolicyBank、AgentPex）、RE 文献（Berry et al., Massey et al., Ferrari & Esuli, Dalpiaz et al.）、agent safety benchmarks（τ-bench, SOPBench, AgentAuditor），以及心理语言学基础（Frazier & Rayner 1982, Ferreira et al. 2002）。Appendix L 和 M 分别映射了 DRIP-R 和 Li et al. (2024) 的分类体系，显示了对相关工作的认真对比。

**可选补充**：
- D'Amour et al. (2022), "Underspecification Presents Challenges for Credibility in Modern Machine Learning" — 虽讨论的是 ML 模型层面的 underspecification 而非 policy specification，但与 incompleteness 类型的概念框架有交叉。
- 可考虑在 Discussion 中进一步连接 Tamkin et al. (2023) 的 rule-following 分析与本文 disambiguation neglect 的发现。

---

## Questions for Authors

1. **训练数据重叠与 convergent nocuity**：5 个模型中 GPT-5.4/GPT-4.1 共享 OpenAI pipeline，Claude 和 DeepSeek/Qwen 各有独立训练集。41.3% convergent violations 中，有多少比例是仅在同族模型间收敛 vs. 跨厂商收敛？如果大部分收敛仅发生在 OpenAI 模型间，systematic nocuity 的普遍性结论需要修正。

2. **Incompleteness 的信息量混淆**：Appendix H 控制 token delta 后效应仍显著但 p 值上升。是否考虑过使用 information-theoretic measure（如 perplexity delta）而非 token count 作为更精细的控制变量？

3. **Temperature > 0**：论文承认无 temperature > 0 数据。在 temperature = 0 下每个 model-clause pair 只有一个确定性输出。是否有计划收集哪怕小规模的 stochastic sampling 数据来验证效应方向和 convergence pattern？

4. **"Diagnostic instrument" 的操作化**：如果 taxonomy 是诊断工具而非风险分类器，其预期使用方式是什么？开发者看到某个 clause 被标记为 "scopal ambiguity" 后，具体应采取什么行动？Appendix B 的 prompt-based mitigation 是否就是预期的使用路径？

---

## 主要优势

1. **因果设计的方法论贡献**：matched-pair 设计是对该领域既有相关性研究（DRIP-R 等）的质的提升。每个歧义 clause 配对一个 minimal-edit 无歧义变体，控制了话题、上下文、难度等混淆因素。这一设计使因果推断可信度远高于现有工作。

2. **实验执行的彻底性**：5 个架构多样的模型、2,997 episodes、cross-judge 三法官评估（κ = 0.63）、TOST 等价检验（7 margin levels）、bootstrap 聚类（B = 10,000）、SOPBench 跨基准复现、human validation（100 episodes）、real-world policy audit（407 clauses from 24 documents）——分析的深度和广度在 EMNLP 提交中属于上游水平。

3. **Disambiguation neglect 的实证发现**：4.6% 的歧义意识率是令人印象深刻的量化结果。这将 "ambiguity collapse"（Liu et al. 2023）从表示层面扩展到行为层面——agents 不仅 collapse 到单一解释，而且在行为上从不 flag 歧义、直接产生不可逆的安全违规。对 LLM agent 部署有直接的实践启示。

4. **透明的限制讨论**：论文对 incompleteness confound（Appendix F, H）、failure mechanism 编码的低人间一致性、合成数据局限性、temperature=0 约束都进行了诚实详细的讨论。多项 robustness check（perturbation control §4.5, within-family replicability §4.5, cross-domain analysis Appendix Z）增强了主要发现的可信度。

5. **格式与匿名合规**：正确使用 "Anonymous ACL submission" 和匿名化 GitHub URL，未发现自引泄露或机构信息。正文 8 页（含 Conclusion），Abstract ≈ 160 词（符合 ≤200 词要求），Limitations 覆盖关键限制。

---

## 贡献增量评估（相对并发工作）

| 对比工作 | 本文增量 | 评估 |
|---------|---------|------|
| DRIP-R (400 scenarios, 5 RE types, correlational) | matched-pair causal design, 6-type two-layer taxonomy, failure mechanism analysis | **实质性提升**：从相关性到因果性是方法论质变。Appendix L 详细映射了分类体系差异。 |
| PolicyBank (iterative refinement) | 关注 policy ambiguity 的安全后果而非 refinement 过程 | **互补而非竞争**：研究问题不同 |
| AgentPex (procedural violations) | 关注 policy specification 歧义而非 procedural adherence | **互补**：AgentPex 检测违规，本文分析违规的 policy-side cause |

**总体新颖性判断**：三项贡献中，(1) causal effect 是方法论贡献，方向符合预期但量化有价值；(2) disambiguation neglect + systematic nocuity 是最具新颖性的实证发现；(3) type–mechanism dissociation 概念有趣但支撑证据不够稳固（κ = 0.15）。整体新颖性为 moderate-to-good，足以支撑 Findings 发表，但需加强 N1 和 N2 以达到 Main conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2453 · 2026-05-23T14:35:16.855830+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见（侧重方法严谨性）。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题以及 Strengths，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 3.5/5, **Excitement**: 3.5/5, **Reproducibility**: 4/5\n\n---\n\n### Must-Fix\n\n**N1** [critical] Clause pair 构建方法描述自相矛盾\n- §4.2 写 \"template-based pipeline\"，Appendix T 写 \"hand-crafted, no automated over-generation\"。两处互相矛盾，直接影响可复现性和刺激偏差评估。\n\n**N2** [critical] 信息添加混淆未在全部类型上充分讨论\n- 论文详细讨论 incompleteness 的信息添加混淆，但 auth-scope（Δtoken=36.1 words，所有类型中最大）同样存在该混淆却讨论不足。Table 14 示例显示 auth-scope unambiguous variant 添加了具体美元阈值和流程细节，远非 \"minimal edit\"。token count 回归 (β=+0.027) 过于粗糙——longer clauses → more violations 可能反映长条款本身更难遵循。coreferential 的 18.7pp lower bound 有效，但不能用来 bound auth-scope 各自的效应分解。建议：(1) 按类型报告信息添加混淆程度；(2) Table 2 对 Δtoken>25 的类型加注信息添加警告；(3) 明确区分 \"ambiguity-only\" vs \"ambiguity + information\" 混合效应。\n\n### Should-Fix\n\n**W1** [warning] V=0.45 vs V=0.14 跨维度比较方法论缺陷\n- Cramér's V 在 6×3 和 6×2 表之间不可直接比较（归一化因子不同）。Appendix V 脚注承认但正文仍反复使用。建议用 NMI 或 partial association measures。\n\n**W2** [warning] LLM 编码 LLM 失败模式的循环性\n- 用 LLM 对 LLM failure trace 编码存在根本循环性。human κ=0.15 远低于 LLM κ=0.52，暗示 LLM 高一致性可能来自 shared bias。论文将 Section 6 标为 [Exploratory] 但 Discussion/Abstract 仍以 type-mechanism dissociation 作主要贡献。\n\n**W3** [warning] Auth-scope 测量不稳定威胁 C2 和 C4\n- Auth-scope 在多指标上异常：最低 κ (0.385)、最大跨模型 range (52pp)、judge-group ρ=0.09 完全由其驱动、C4 完全由其驱动、最低 ICC (0.29)。排除后核心结论稳健，但 Table 2 中仍平等报告其 +36.0pp。\n\n**W4** [warning] Temperature=0 唯一条件的泛化局限\n- temperature=0 人为提高 matched-pair 一致性和 ICC。无任何 temp>0 pilot data。\n\n**W5** [warning] 合成刺激生态效度 + 96% initial agreement 暗示任务过简\n- 96% agreement (κ=0.95) 异常高，暗示歧义类型判别过于明显。SOPBench 效应 (+12.7pp) 仅为 τ²-bench 37%，一个可信解释是更接近真实 SOP 的歧义效应更小。\n\n### Minor\n\n**M1**: SOPBench +12.7pp 是 unweighted mean，应标注。\n**M2**: §5.1 McNemar OR=15.1 基于 discordant pairs，应在结果部分重申。\n**M3**: 已核实 abstract 说 300 clause pairs，无误。\n**M4**: Prevalence audit κ=0.295 很低但仍报告 87% 文档级歧义率，应更明确讨论低 κ 影响。\n**M5**: 3 episodes lost to API errors 是否做了 sensitivity analysis？\n\n### Strengths\n\n1. C1 实验设计扎实，控制链完整（perturbation control、ICC=0.919、SOPBench 复制）\n2. 统计方法规范（McNemar、TOST 7-margin sensitivity、Holm-Bonferroni、bootstrap cluster）\n3. Cross-judge validation 全面（三法官 Fleiss' κ=0.717、无 same-family leniency）\n4. Claims 标定诚实（C1/C2 supported, C3 inconclusive, C4 exploratory）\n5. Variance decomposition 和 residual 分析透明（ICC-based 拆分）\n6. Appendix 质量高（23 页，覆盖几乎所有可预期疑问）\n\n### Questions\n\nQ1: \"template-based pipeline\" vs \"hand-crafted\" 矛盾如何解释？\nQ2: Auth-scope 是否可提供类似 incompleteness 的 confound analysis？\nQ3: 是否有 temperature>0 初步数据？\nQ4: Human mechanism coding κ=0.15——标注者是否接受了训练？\nQ5: 96% agreement——是否计算了 PABAK？\n\n---\n\n请逐条回应以上所有问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见（侧重方法严谨性）。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题以及 Strengths，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 3.5/5, **Excitement**: 3.5/5, **Reproducibility**: 4/5\n\n---\n\n### Must-Fix\n\n**N1** [critical] Clause pair 构建方法描述自相矛盾\n- §4.2 写 \"template-based pipeline\"，Appendix T 写 \"hand-crafted, no automated over-generation\"。两处互相矛盾，直接影响可复现性和刺激偏差评估。\n\n**N2** [critical] 信息添加混淆未在全部类型上充分讨论\n- 论文详细讨论 incompleteness 的信息添加混淆，但 auth-scope（Δtoken=36.1 words，所有类型中最大）同样存在该混淆却讨论不足。Table 14 示例显示 auth-scope unambiguous variant 添加了具体美元阈值和流程细节，远非 \"minimal edit\"。token count 回归 (β=+0.027) 过于粗糙——longer clauses → more violations 可能反映长条款本身更难遵循。coreferential 的 18.7pp lower bound 有效，但不能用来 bound auth-scope 各自的效应分解。建议：(1) 按类型报告信息添加混淆程度；(2) Table 2 对 Δtoken>25 的类型加注信息添加警告；(3) 明确区分 \"ambiguity-only\" vs \"ambiguity + information\" 混合效应。\n\n### Should-Fix\n\n**W1** [warning] V=0.45 vs V=0.14 跨维度比较方法论缺陷\n- Cramér's V 在 6×3 和 6×2 表之间不可直接比较（归一化因子不同）。Appendix V 脚注承认但正文仍反复使用。建议用 NMI 或 partial association measures。\n\n**W2** [warning] LLM 编码 LLM 失败模式的循环性\n- 用 LLM 对 LLM failure trace 编码存在根本循环性。human κ=0.15 远低于 LLM κ=0.52，暗示 LLM 高一致性可能来自 shared bias。论文将 Section 6 标为 [Exploratory] 但 Discussion/Abstract 仍以 type-mechanism dissociation 作主要贡献。\n\n**W3** [warning] Auth-scope 测量不稳定威胁 C2 和 C4\n- Auth-scope 在多指标上异常：最低 κ (0.385)、最大跨模型 range (52pp)、judge-group ρ=0.09 完全由其驱动、C4 完全由其驱动、最低 ICC (0.29)。排除后核心结论稳健，但 Table 2 中仍平等报告其 +36.0pp。\n\n**W4** [warning] Temperature=0 唯一条件的泛化局限\n- temperature=0 人为提高 matched-pair 一致性和 ICC。无任何 temp>0 pilot data。\n\n**W5** [warning] 合成刺激生态效度 + 96% initial agreement 暗示任务过简\n- 96% agreement (κ=0.95) 异常高，暗示歧义类型判别过于明显。SOPBench 效应 (+12.7pp) 仅为 τ²-bench 37%，一个可信解释是更接近真实 SOP 的歧义效应更小。\n\n### Minor\n\n**M1**: SOPBench +12.7pp 是 unweighted mean，应标注。\n**M2**: §5.1 McNemar OR=15.1 基于 discordant pairs，应在结果部分重申。\n**M3**: 已核实 abstract 说 300 clause pairs，无误。\n**M4**: Prevalence audit κ=0.295 很低但仍报告 87% 文档级歧义率，应更明确讨论低 κ 影响。\n**M5**: 3 episodes lost to API errors 是否做了 sensitivity analysis？\n\n### Strengths\n\n1. C1 实验设计扎实，控制链完整（perturbation control、ICC=0.919、SOPBench 复制）\n2. 统计方法规范（McNemar、TOST 7-margin sensitivity、Holm-Bonferroni、bootstrap cluster）\n3. Cross-judge validation 全面（三法官 Fleiss' κ=0.717、无 same-family leniency）\n4. Claims 标定诚实（C1/C2 supported, C3 inconclusive, C4 exploratory）\n5. Variance decomposition 和 residual 分析透明（ICC-based 拆分）\n6. Appendix 质量高（23 页，覆盖几乎所有可预期疑问）\n\n### Questions\n\nQ1: \"template-based pipeline\" vs \"hand-crafted\" 矛盾如何解释？\nQ2: Auth-scope 是否可提供类似 incompleteness 的 confound analysis？\nQ3: 是否有 temperature>0 初步数据？\nQ4: Human mechanism coding κ=0.15——标注者是否接受了训练？\nQ5: 96% agreement——是否计算了 PABAK？\n\n---\n\n请逐条回应以上所有问题。"
  }
}
```

</details>

---


### Tool result

_source line 2454 · 2026-05-23T14:35:47.458480+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30602
}
```

</details>

---


### Tool call

_source line 2455 · 2026-05-23T14:35:47.861504+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见（侧重新颖性与完整性）。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题以及 Strengths，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性与完整性）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 4/5, **Excitement**: 3/5, **Reproducibility**: 4/5\n\n---\n\n### Must-Fix\n\n**N1** [critical] Type–mechanism dissociation 的人间一致性过低，无法充分支撑 \"diagnostic instrument\" 核心定位\n- Failure mechanism 编码人间 κ=0.15（collapsed 0.34-0.52），LLM coder κ=0.52。论文将 V=0.45 作为支撑 \"diagnostic instrument\" 的核心论据，但 Abstract/Introduction 用 \"establishes\" 与 Section 6 的 [Exploratory] 标签矛盾。建议将 \"establishes\" 改为 \"suggests\"/\"provides exploratory evidence for\"；讨论 LLM coder 一致性高于人间的解释；Abstract 中报告原始 κ=0.15。\n\n**N2** [critical] Discussion + Conclusion 过于简短\n- Discussion ~80 词（1 段），Conclusion ~70 词（3 句）。两节合计约 150 词，对三项贡献的讨论严重不足。缺失：disambiguation neglect 与 sycophancy 的关系、systematic nocuity 对 agreement-based evaluation 的启示、开发者实操建议、RE 领域工具链借鉴。建议扩展 Discussion 至至少半页（~300 词）。\n\n### Should-Fix\n\n**W1** [warning] Berry \"nocuous\" 术语反转概念论证不够深入\n- \"Inverting Berry's framework\" 更精确的表述是 \"Berry's criterion breaks down for LLM agents\"。41.3% convergent violations 可能是 trivially expected（shared training data → shared errors）。建议按模型家族分析 convergence 模式区分 training-data-driven vs ambiguity-structure-driven。\n\n**W2** [warning] \"Ambiguity\" 广义使用涵盖 incompleteness，影响 headline result\n- Incompleteness 在传统文献中归为 underspecification 而非 ambiguity。其贡献最大效应 (+49.2pp) 且 confound 结构不同。Abstract headline 以 +34.0pp（含 incompleteness）为主，应更 prominently 呈现 +31.0pp。\n\n**W3** [warning] SOPBench 复现效应大幅缩小需更多讨论\n- +12.7pp vs +34.0pp（37%）。Abstract 中 \"3/5 at p<0.05\" 与 Appendix E 数据可能不一致——按 p<0.05 应为 4/5（GPT-5.4 p=0.032）。建议核查。\n\n### Minor\n\n**M1**: `\\enlargethispage{26\\baselineskip}` 可能违反 ACL margin 要求。\n**M2**: Abstract 仅报告 collapsed κ=0.34-0.52，未提及原始 κ=0.15。\n**M3**: Figure 3 auth-scope CI 上限标注不够清晰。\n**M4**: Conclusion \">89% disambiguation neglect\" 来源不够明确（Section 6.2 报告 awareness=4.6% 即 95.4% neglect）。\n\n### Missing References\n\n无重大遗漏。可选补充：D'Amour et al. (2022) \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"。\n\n### Strengths\n\n1. 因果设计是对该领域既有相关性研究的质的提升\n2. 实验执行彻底（5 模型、2997 episodes、cross-judge 三法官、TOST 7-margin、bootstrap B=10000、SOPBench 复制、human validation、real-world audit）\n3. Disambiguation neglect (4.6% awareness) 是令人印象深刻的量化结果\n4. 透明的限制讨论\n5. 格式与匿名合规（Abstract ~160 词，正文 8 页）\n\n### Questions\n\nQ1: 41.3% convergent violations 中，同族模型收敛 vs 跨厂商收敛的比例？\nQ2: 是否考虑过使用 perplexity delta 而非 token count 控制信息量？\nQ3: 有无 temperature>0 数据计划？\nQ4: \"Diagnostic instrument\" 预期使用方式是什么？Appendix B mitigation 是否就是使用路径？\n\n---\n\n请逐条回应以上所有问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见（侧重新颖性与完整性）。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题以及 Strengths，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性与完整性）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 4/5, **Excitement**: 3/5, **Reproducibility**: 4/5\n\n---\n\n### Must-Fix\n\n**N1** [critical] Type–mechanism dissociation 的人间一致性过低，无法充分支撑 \"diagnostic instrument\" 核心定位\n- Failure mechanism 编码人间 κ=0.15（collapsed 0.34-0.52），LLM coder κ=0.52。论文将 V=0.45 作为支撑 \"diagnostic instrument\" 的核心论据，但 Abstract/Introduction 用 \"establishes\" 与 Section 6 的 [Exploratory] 标签矛盾。建议将 \"establishes\" 改为 \"suggests\"/\"provides exploratory evidence for\"；讨论 LLM coder 一致性高于人间的解释；Abstract 中报告原始 κ=0.15。\n\n**N2** [critical] Discussion + Conclusion 过于简短\n- Discussion ~80 词（1 段），Conclusion ~70 词（3 句）。两节合计约 150 词，对三项贡献的讨论严重不足。缺失：disambiguation neglect 与 sycophancy 的关系、systematic nocuity 对 agreement-based evaluation 的启示、开发者实操建议、RE 领域工具链借鉴。建议扩展 Discussion 至至少半页（~300 词）。\n\n### Should-Fix\n\n**W1** [warning] Berry \"nocuous\" 术语反转概念论证不够深入\n- \"Inverting Berry's framework\" 更精确的表述是 \"Berry's criterion breaks down for LLM agents\"。41.3% convergent violations 可能是 trivially expected（shared training data → shared errors）。建议按模型家族分析 convergence 模式区分 training-data-driven vs ambiguity-structure-driven。\n\n**W2** [warning] \"Ambiguity\" 广义使用涵盖 incompleteness，影响 headline result\n- Incompleteness 在传统文献中归为 underspecification 而非 ambiguity。其贡献最大效应 (+49.2pp) 且 confound 结构不同。Abstract headline 以 +34.0pp（含 incompleteness）为主，应更 prominently 呈现 +31.0pp。\n\n**W3** [warning] SOPBench 复现效应大幅缩小需更多讨论\n- +12.7pp vs +34.0pp（37%）。Abstract 中 \"3/5 at p<0.05\" 与 Appendix E 数据可能不一致——按 p<0.05 应为 4/5（GPT-5.4 p=0.032）。建议核查。\n\n### Minor\n\n**M1**: `\\enlargethispage{26\\baselineskip}` 可能违反 ACL margin 要求。\n**M2**: Abstract 仅报告 collapsed κ=0.34-0.52，未提及原始 κ=0.15。\n**M3**: Figure 3 auth-scope CI 上限标注不够清晰。\n**M4**: Conclusion \">89% disambiguation neglect\" 来源不够明确（Section 6.2 报告 awareness=4.6% 即 95.4% neglect）。\n\n### Missing References\n\n无重大遗漏。可选补充：D'Amour et al. (2022) \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"。\n\n### Strengths\n\n1. 因果设计是对该领域既有相关性研究的质的提升\n2. 实验执行彻底（5 模型、2997 episodes、cross-judge 三法官、TOST 7-margin、bootstrap B=10000、SOPBench 复制、human validation、real-world audit）\n3. Disambiguation neglect (4.6% awareness) 是令人印象深刻的量化结果\n4. 透明的限制讨论\n5. 格式与匿名合规（Abstract ~160 词，正文 8 页）\n\n### Questions\n\nQ1: 41.3% convergent violations 中，同族模型收敛 vs 跨厂商收敛的比例？\nQ2: 是否考虑过使用 perplexity delta 而非 token count 控制信息量？\nQ3: 有无 temperature>0 数据计划？\nQ4: \"Diagnostic instrument\" 预期使用方式是什么？Appendix B mitigation 是否就是使用路径？\n\n---\n\n请逐条回应以上所有问题。"
  }
}
```

</details>

---


### Tool result

_source line 2456 · 2026-05-23T14:35:49.372466+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1510
}
```

</details>

---


### Assistant

_source line 2457 · 2026-05-23T14:35:55.567005+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 232

## Round 232

2 recorded events
