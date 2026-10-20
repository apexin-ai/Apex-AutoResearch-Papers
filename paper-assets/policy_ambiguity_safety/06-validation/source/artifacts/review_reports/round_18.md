---
round: 18
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T21:01:19.436101+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 18 (Fresh Review)

**论文**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: Fresh (重新审稿，无上轮记忆)
**Reviewer 编排**: 2 人 — R1 方法严谨性+实验设计, R2 新颖性+完整性+写作质量
**交叉回应**: 完成，所有 critical issues 达成共识

---

## Summary

本文研究 LLM agent 在自然语言策略规范下因歧义导致安全违规的因果效应。采用匹配对设计在 τ²-bench 上构造 300 对歧义/非歧义 clause pairs，跨 6 种歧义类型和 5 个模型评估 2,997 个 episodes。核心发现：歧义 clause 使违规率增加 34.0pp (conditional OR=15.1)；clause 措辞解释 22.4% 方差远超 type (0.4%) 和 model (1.0%)；type 预测 failure mechanism 比预测 violation rate 强 17×。

---

## Strengths

**S1.** [R1+R2 共识] **匹配对因果设计是方法论亮点**。相比 DRIP-R 的 correlational 设计，本文通过最小编辑配对隔离歧义因果效应，加上扰动控制（Δ_perturb = −0.67pp, CI 含零）确认 specificity to semantic ambiguity。这是 agent policy compliance 领域首个严格的因果推断设计。

**S2.** [R1+R2 共识] **C1 证据极其稳健**。34.0pp 效应在 7 个模型（5+2 replication）、2 个 benchmark（τ²-bench + SOPBench）、多 severity threshold 下方向一致。排除 incompleteness 后 Δ=31.0pp (p<10⁻⁷⁵) 仍然显著，证明效应不依赖任何单一 type。

**S3.** [R1+R2 共识] **Variance decomposition + NMI repositioning 是论文最有价值的原创洞察**。"Clause wording drives risk (22.4%), type drives mechanism (17× NMI)" 的发现重新定义了 taxonomy 在 agent safety 中的角色——从 risk predictor 转为 diagnostic tool。这个 framing 有概念新意且有方法论支撑。

**S4.** [R1+R2 共识] **Claims 与 evidence 自觉对齐**。C3 报 inconclusive，C4 标 exploratory，taxonomy 重新定位——论文没有过度声称。18 个附录提供详尽敏感性分析，可审查性高。Limitations 部分对所有已知弱点（cross-judge ρ=0.09, incompleteness confound, ICC OpenAI-only 等）的披露非常坦诚。

**S5.** [R2] **统计分析远超同类实证研究水准**。TOST equivalence testing + bootstrap cluster + permutation tests + Holm-Bonferroni correction + logistic regression confound control + cross-benchmark replication，方法论工具箱完整。

**S6.** [R2] **引用真实性已验证**。所有 2026 年 arXiv preprint 引用均为真实存在的论文。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [critical, R1+R2 共识] **C2 "partial ordering" 作为 primary claim 缺乏稳健性——cross-judge 不稳定 + SESOI margin-dependency 双重打击**

C2 被列为两个 primary claims 之一（Abstract, Introduction §1），但存在两条独立的不稳定源：

(a) *Cross-judge instability*（R1-N1, R2-W2 → 交叉后升级为共识 critical）：两个 judge group 的 type ranking Spearman ρ=0.09 (p=0.87, Appendix P)，本质为零。排除 authorization scope 后 ρ=0.90，但 authorization scope 的排除虽有独立方法论理由（κ=0.385 最低, agent composition effect），仍引入 researcher degrees of freedom。C2 的 mid-tier ordering 在不同 judge 组下完全不同。

(b) *SESOI margin-dependency*（R1-N3, R2 交叉回应 AGREE）：±15pp margin 下 6/6 mid-tier pairs 等价，但 ±10pp 下仅 3/6，TOST power 从 0.94 降至 0.57。论文用 "exceeding perturbation control bound by >2×" 论证 SESOI——但 perturbation bound 是 noise floor，SESOI 是 domain-relevant threshold，两个概念不可混用。12pp 的 type 差异在 deployment 中已有实际意义，但 ±15pp 会判为"等价"。

两条证据链汇聚到同一结论：**C2 作为 primary claim 仅在极端类型上成立（incompleteness 最高、coreferential 最低），mid-tier ordering 不可信。** §5.2 末段已表达了类似限定（"establishing robust extremes...rather than a complete linear ordering"），但这与 C2 的 primary claim 地位矛盾。

→ **建议**：将 C2 降级为 secondary/partially-supported；Abstract/Introduction 限定为 robust extremes only；Table 2/Figure 2 对 authorization scope 做视觉标注（如 dagger）；正文以多 margin 结果为主要呈现而非以 ±15pp 为 primary。

---

**N2** [critical, R1+R2 共识] **Judge identity 与 model identity 完全混淆**

GPT-5.4 评判 Claude/GPT-4.1/Qwen3；GPT-4.1 评判 GPT-5.4/DeepSeek。每个 model 只有一个 judge，两个 judge 都是 OpenAI 家族。

- C1 不受此 confound 影响（matched-pair 下 judge bias 在 Δpp 中相消，§4.4 正确指出）
- C4 完全暴露：Figure 3 中 Claude 最低 30.3% vs DeepSeek 最高 49.7% 的 model main effect 无法与 judge effect 分离。Authorization scope 的 52pp model range（该类型驱动 C4 interaction）可能部分是 judge artifact
- Same-family leniency/severity 无法排除

这是不可追溯修复的实验设计缺陷（除非追加实验）。

→ **建议**：§5.4 首段和 Figure 3 caption 明确声明 "model-level absolute violation rates are confounded with judge identity and are not directly comparable across judge groups"；至少对一个 model 用两个 judge 评判以量化 judge effect。

---

**N3** [critical, R2 首提, R1 AGREE with nuance] **Taxonomy 增量贡献不足，contribution framing 需调整**

六种 type 直接取自 Li et al. (2024) 和 Massey et al. (2014)，无新类型引入。两层结构（linguistic vs. specification）的理论价值被 C3 inconclusive（不过 Holm-Bonferroni，§5.3）削弱。6 种 type 中 2 种（incompleteness, conditional precedence）严格来说不是 linguistic ambiguity——§3 "Scope of 'ambiguity'" 承认这一点但辩护不够显著。与 DRIP-R (2026) 的差异化论述（§2 最后一段）过于简略——未论证为什么 safety violations 比 decision quality 是更重要的度量。

→ **建议**：将 contribution 重心从 taxonomy 转移到因果方法论 + variance decomposition insight；taxonomy 降格为实验设计工具而非独立贡献；§3 更显著讨论操作性定义偏离；§2 加强与 DRIP-R 差异化论证。

---

**N4** [critical, R2 首提, R1 AGREE] **"Disambiguation Neglect" 概念新颖性不足**

Liu et al. (2023) 已证明 LLMs "fail to represent ambiguity, collapsing multiple interpretations into a single output"。Gur-Arieh et al. (2026) 系统化了 "ambiguity collapse" 风险分类。本文的 "Disambiguation Neglect" 本质是 ambiguity collapse 在 agentic settings 的观测实例，核心区别仅在于不可逆后果（§6.2: "the result is irreversible policy violation"）。4.6% awareness rate 是有价值的实证数据点，但 framing 为带专属术语的新概念过度。"Systematic nocuity" 和 "differential nocuity" 同样是 Berry & Kamsties (2004) / Willis et al. (2008) 概念的直接延伸。

→ **建议**：将 Disambiguation Neglect 定位为 ambiguity collapse 的实证确认而非概念创新；减少自创术语（"systematic nocuity" → "convergent violations"）；更充分地与 Gur-Arieh et al. (2026) 的 epistemic risk taxonomy 对话。

---

### Should-Fix（影响评分但不一票否决）

**W1** [warning, R1+R2] **Variance decomposition 在 binary outcomes 上的适用性**：Type III SS 在 binary outcome 上近似 LPM，22.4% 来自 LPM。Tjur's R²=0.175 与 Type III 39.2% explained variance 差异暗示方法不一致。Logistic regression 因子排序一致性（Appendix H）是 mitigation factor，但应在正文说明两者度量不同维度。

**W2** [warning, R1+R2] **60.8% 残差方差未充分讨论**：condition + clause wording 仅解释 ~38% 方差。论文推荐 clause-level auditing（Conclusion）但未讨论 60.8% 随机方差（conversation trajectory, user-simulator stochasticity）对实用性的影响。22.4% 仍是最大可干预因子，但 Discussion 应加入这个 perspective。

**W3** [warning, R1+R2] **Incompleteness confound 需更显著讨论**：49.2pp effect 是 ambiguity resolution + information addition 的混合效应。Token count 作为 information proxy 粗糙（OR=1.022 显著, p<0.001）。Logistic regression 后 p=0.022 接近边界。Abstract "conditional on an information-addition confound" 措辞模糊——未报告 controlled effect size。Auth scope 有最大 token delta 但 violation 更低是间接 counter-evidence。正文（非仅 Appendix）应显著讨论。

**W4** [warning, R1+R2] **Failure mode coding LLM circularity**：MI 提供结构性反循环证据，但不能排除 LLM coder 系统映射。κ=0.52 仅 moderate。建议 camera-ready 对 50-100 条 traces 做 human failure mode annotation。

**W5** [warning, R1+R2] **SOPBench 效应量大幅下降**：+13.8pp vs +34.0pp（降 60%），仅 3/5 模型达个体显著性（DeepSeek p=0.119, GPT-5.4 p=0.209）。"Directional consistency" framing 可能过于乐观。正文 §5.1 仅一句话提及，应更坦诚讨论。

**W6** [warning, R1+R2] **Coreferential 排除矛盾**：作为唯一 zero-token-delta type，coreferential 是最 clean 的 confound-free evidence (+18.7pp)——但被排除出 mitigation 和 replication。加上 human-LLM κ 最低 (0.479)，三点叠加使其证据最薄弱，与 confound-free 地位矛盾。Limitations 应明确承认此 tension。

**W7** [warning, R2, R1 部分同意] **Abstract 数字过载**：~200 词 abstract 中 15+ 个数字，核心信息被淹没。建议保留 5-7 个关键数字（34.0pp, OR=15.1, 22.4% vs 0.4%, 17×），其余用定性语言。

**W8** [critical/format, R2+R1+visual check] **主文超出 8 页限制约 4 行**：Conclusion (§8) 标题和全文出现在第 9 页顶部。EMNLP 2026 strict 8-page limit，有 desk reject 风险。建议压缩 §7 Discussion 将 Conclusion 拉回第 8 页。

**W9** [warning, R1+R2] **Conclusion 泛化声明超出证据范围**："clause-level auditing is critical for policy-governed deployments" 未限定领域（仅 customer service）。SOPBench 效应量降 60% 进一步限制泛化性。

---

## Reviewer Consensus

以下 issues 两位 Reviewer 在交叉回应中明确达成共识（均 [AGREE]）：

1. **C2 mid-tier ordering 不稳健**：R1 从 SESOI margin-dependency 角度 + R2 从 cross-judge ρ=0.09 角度 → 汇聚同一结论
2. **Judge-model confound 影响 C4**：R1 首提，R2 完全同意并补充 C1 不受影响的论证
3. **Incompleteness confound 需更好的 proxy**：R1-W3 ≈ R2-W1，双方一致
4. **"Disambiguation Neglect" 新颖性有限**：R2 首提，R1 完全同意（"§6.2 自己承认了延伸性质"）
5. **SOPBench 效应量下降需更坦诚讨论**：R1-W5 ≈ R2 交叉回应
6. **主文超页需修复**：R2 首发现，R1 验证 PDF 确认

## Reviewer Divergence

无重大未解决分歧。微小差异：

- R2 将 cross-judge ρ=0.09 列为 Should-Fix (W2)，R1 列为 Must-Fix (N1)。**交叉后 R2 同意升级为 critical**（"综合来看，应升级为 critical——两个独立的不稳定源叠加使问题更严重"）。
- R1 认为 "first matched-pair causal study" claim 表述准确，R2 认为需进一步限定（2/6 type 非 strict ambiguity）。分歧已在交叉中收敛——R1 同意 taxonomy framing 应调整但 causal claim 本身准确。

---

## Questions

1. 如果用 Claude 或 Gemini 作为 judge 评判 GPT 模型的 traces，C4 的 model ranking 是否改变？这是检验 judge-model confound 的直接实验。
2. 在 ±10pp margin 下，C2 的 mid-tier cluster 从 4 types 缩减到 2 pairs——作者如何论证 ±15pp 而非 ±10pp 是"正确"的 SESOI？是否有 deployment scenario 可以锚定？
3. 60.8% 残差方差中，conversation trajectory 和 user-simulator stochasticity 各占多少？是否可以通过固定 user-simulator seed 来分解？
4. Incompleteness 控制 token delta 后的 controlled effect size 是多少？（Appendix F 仅报告 p=0.022 但未报告 controlled Δpp）
5. 论文引用了 Mu et al. (2023) "Can LLMs Follow Simple Rules?" 在 bib 中但未在正文引用——这篇论文与 policy compliance 直接相关，是有意排除还是遗漏？

---

## Missing References

论文的 related work 覆盖面已相当全面（R2 验证了所有 2026 引用的真实性）。以下供参考：

- **Mu et al. (2023)** "Can LLMs Follow Simple Rules?" — 已在 bib 中但未引用，研究 LLM 规则遵循能力，与 policy compliance 直接相关
- **Structured policy representation / policy formalization** 方向的工作——论文讨论 clause-level auditing 但未讨论 policy formalization 作为替代方案
- 近期 **constitutional AI / rule-following** 实证研究（2025-2026 如有）

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: done (耗时约 4 分钟)

| 严重度 | 发现 |
|--------|------|
| **critical** | 主文本（Section 1-8）超出 8 页限制，Conclusion 完整位于第 9 页顶部，约 8.5 页。存在 desk reject 风险。 |
| **warning** | Pages 4-6 连续 3 页纯文本（Method + Results 开头），无 figure/table/equation 穿插，审稿人阅读关键技术内容时缺乏视觉休息点。 |
| **warning** | Page 7 三个 display items（Table 2 + Figure 2 + Figure 3）堆叠，视觉密度过高。Figure 2/3 被压缩。 |
| **warning** | Page 8 又一个纯文本页（Error Analysis + Discussion），p4-p8 中 4/5 页纯文本。 |
| **info** | Figure 3 尺寸过小，坐标轴标签 6-7pt 接近可读性下限。 |
| **info** | Table 1, Table 2 均使用 booktabs 风格，格式规范。 |
| **info** | 未发现 margin overflow、LaTeX 渲染错误、未解析引用 [?]。参考文献格式统一。 |

建议：将 Table 2 或 Figure 2 前移至 p5-6 以改善视觉节奏，同时压缩 §7 将 Conclusion 收回第 8 页。

---

## Overall Assessment

**评分: 3.5 / 5 — Borderline Conference**
**置信度: 4 / 5**

| 维度 | R1 | R2 | 合成 |
|------|----|----|------|
| Soundness | 3.5 | 4.0 | 3.5 |
| Excitement | 3.5 | 3.0 | 3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.5 | **3.5** |

**核心判断**：这是一篇方法论严谨的实证研究，C1（歧义因果效应 +34.0pp）在 7 模型和 2 个 benchmark 上的证据非常稳健，matched-pair 设计是真正的方法论贡献。Variance decomposition + NMI repositioning（clause wording drives risk, type drives mechanism）是论文最有价值的原创洞察。

但论文在以下维度不够突出：

1. **C2 mid-tier ordering 不稳健**（cross-judge ρ=0.09 + SESOI margin-dependency），作为 primary claim 证据不足
2. **Judge-model identity 完全混淆**，C4 的核心发现可能是 artifact
3. **核心发现（ambiguity → violation）高度直觉**，taxonomic contribution 增量有限
4. **概念创新有限**——"Disambiguation Neglect" 是 ambiguity collapse 的场景迁移，自创术语过多

**如果按建议调整**（C2 降级、taxonomy 降格、术语精简、页面修复），论文的因果方法论 + variance decomposition insight 足以支撑 Conference（4.0）。当前版本处于 Borderline Conference（3.5）。

**格式风险**: 主文超出 8 页限制约 4 行，EMNLP 2026 严格执行，有 desk reject 可能——这是最紧急的修复项。

---

## Detailed Comments

### §1 Introduction
- 开篇的 $200 motivating example 有效且具象
- 贡献列表中 taxonomy 不应与因果设计和 variance decomposition 并列——后两者的贡献度更高
- "first matched-pair causal study" claim 本身准确，但应明确 2/6 types 采用了 operational definition of ambiguity

### §3 Taxonomy
- "Scope of 'ambiguity'" 段的 principled justification（behaviorally indistinguishable）应更突出
- 两层结构在 C3 inconclusive 后仅作为"organizational convenience"——这个定位是诚实的但可以更早明确

### §4 Method
- Matched-pair design + perturbation control 是方法论亮点
- Cross-judge design 的 confound 应在 §4.4 而非仅在 Limitations 中讨论
- SESOI ±15pp 的论证需要 domain-grounded 锚定而非仅用 perturbation bound >2×

### §5 Results
- C1 证据链完整且稳健
- C2 §5.2 最后一段的 limiting statement 与 C2 作为 primary claim 的 framing 矛盾——需要在 Abstract/Intro 中对齐
- C3 报 inconclusive 是正确的做法
- C4 需要在 section 内部（不仅在 Limitations）声明 judge-model confound

### §6 Error Analysis
- Failure mode taxonomy 有价值，但 LLM coding circularity 需要 human calibration
- "Disambiguation Neglect" 应减少新概念 framing，定位为 ambiguity collapse 的 agentic-context 实证确认
- "Systematic nocuity" 的 terminology overhead 超过了概念增量

### §7 Discussion
- 仅 3 段略显简短
- Practical implications（clause-level auditing 如何具体操作？与 DRIP-R 方案的互补性？）讨论不足
- 60.8% 残差方差对 auditing 实用性的影响未讨论

### §8 Conclusion
- 需拉回第 8 页（format violation）
- "critical for policy-governed deployments" 应限定领域范围

### Appendix
- 18 个附录的敏感性分析和 robustness checks 可审查性高，值得肯定
- SOPBench replication 的 individual non-significance（2/5 models）应在正文提及

### 格式与写作
- Abstract 数字过载需精简
- 17× vs 16.8× 不一致需统一
- ICC 双数字需解释
- ferrari_defects_2018 bib entry 年份需修正
- Mu et al. (2023) orphan bib entry 需处理