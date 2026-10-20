---
round: 11
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T08:57:00.555430+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 11 审稿报告 — policy_ambiguity_safety

**论文**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 via ARR May cycle
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）
**轮次**: 1 轮（交叉分享后关键问题达成共识，无需第二轮）

---

## Summary

本文研究 LLM agent 在自然语言策略规范下因歧义类型不同而产生的安全违规差异。采用 matched-pair 因果设计，在 τ²-bench 上构建 300 对歧义/消歧 clause pair（六类歧义 taxonomy），跨 5 个模型（2,997 episodes）评估。主要发现：(1) 歧义条款使违规率增加 34.0pp（OR=15.1）；(2) incompleteness 一致排名最高（46-62%），其余五类呈现 risk gradient；(3) error analysis 揭示 Disambiguation Neglect（≤11% awareness）和 systematic nocuity（41.3% clauses 触发模型趋同违规）。

---

## Strengths

**S1. 首个因果性 ambiguity→violation 类型映射 [共识]。** Matched-pair design + perturbation control（Δ_perturb = −0.67pp, CI 包含零）在 NLP agent safety 领域确属创新。与 DRIP-R（correlational）、PolicyBank（iterative refinement）、AgentPex（trace detection）的差异化清晰且准确。C1 证据充分（OR=15.1, 7 模型一致, p < 10⁻¹⁰⁵），因果推断具有说服力。

**S2. 统计方法论异常充分 [共识]。** McNemar + TOST equivalence（7 margin 敏感性）+ margin-free bootstrap cluster + Holm-Bonferroni 三组校正 + post-hoc 功效分析（C1/C2 power > 0.99）。在该子领域中不常见且值得肯定。对 SESOI 的 domain-anchored justification 和 margin dependence 的 acknowledgment 体现方法论自觉。

**S3. Claim 标定诚实 [共识]。** C3 明确标注为 inconclusive（未通过 Holm-Bonferroni），C4 标注 [Exploratory]，authorization scope κ=0.385 在全文五处反复标注，incompleteness confound 多层控制（logistic regression, coreferential lower bound, sans-incompleteness analysis）。

**S4. Error analysis 有实质洞见 [共识]。** 三种 failure mechanism（structural misparse, information gap-filling, boundary violation）与 ambiguity type 的对应关系超越聚合统计。Systematic nocuity（41.3% majority-convergent violations）揭示 agreement-based evaluation 盲区。

**S5. 实验规模与覆盖度 [共识]。** 5+2 models, 6 providers, 2997 episodes, 覆盖 proprietary/open-source/dense/MoE。Replication 在独立 model families 上确认 C1 和 C2。

---

## Weaknesses

### MUST-FIX

**W1. Authorization scope κ=0.385 严重削弱 C4（52pp range claim）[R1 MUST-FIX, R2 AGREE]**

Authorization scope 的 cross-judge κ 仅 0.385（低于 fair agreement 门槛 0.40），是所有类型中最低的。C4 的核心发现——52pp cross-model range（Claude 12% → GPT-5.4 64%）——正是基于这个最不可靠的类型。三层问题：

(1) Cross-judge κ=0.385 与 human-LLM κ=0.644（Appendix G）是不同指标，§5.4 引用 "raw agreement 85.3%" 时数据来源不明确，读者可能混淆。
(2) Within-judge bootstrap ranking preservation（99.5%）仅证明单个 judge 内部一致性，无法弥补 cross-judge 不一致——稳定偏差仍是偏差。
(3) Appendix P within-judge-group type ranking ρ=−0.03（p=0.96），auth scope rank reversal（GPT-4.1 judged: rank 1 vs GPT-5.4 judged: rank 6）中 agent composition 和 judge bias 不可分离。

**修改要求**: (a) 计算 auth scope 的 PABAK 或 Gwet's AC1 区分 prevalence paradox 和真实分歧；(b) C4 从 numbered claim 降级为 Discussion observation；(c) Abstract/Conclusion 中 52pp 改为定性描述；(d) §5.4 明确区分 cross-judge κ 和 human-LLM κ 的数据来源。

### SHOULD-FIX

**W2. C2 "two-tier hierarchy" 表述强度超过证据 [R1 SHOULD-FIX, R2 AGREE]**

"Two-tier hierarchy" 暗示稳定的层级结构，但实际受四个因素制约：(1) ±10pp 仅 3/6 mid-tier pairs equivalent, TOST power 降至 0.57；(2) Bootstrap incompleteness singleton 仅 34.3% 重现, AU p=0.47；(3) Kendall's W=0.398 (p=0.072) 不显著；(4) Incompleteness upper bound 稳健（7 模型 ≥46%），但 mid-tier cohesion 是 margin-dependent 的。

R2 REBUT R1 sub-point：coreferential 31.6% 是 confound-free lower bound 非 incompleteness adjusted effect（logistic regression 控制 token delta 后 incompleteness 仍显著 p=0.018）——不应将 31.6% 视为 incompleteness 的 adjusted rate。

**修改要求**: 弱化为 "incompleteness consistently separates as the highest-violation type; the remaining types form a less differentiated cluster at the ±15pp equivalence margin, though this structure is margin-dependent"。正文报告 AU p-value，明确承认 bootstrap 不稳定性。

**W3. Taxonomy 理论基础：§3 "Scope of ambiguity" 需扩展 [R2 SHOULD-FIX, R1 partial REBUT — DIVERGENCE]**

R2 认为 incompleteness（information absence）和 conditional precedence（normative conflict）不满足 strict ambiguity 定义，§3 的论证存在循环（纳入 taxonomy → 测试 → 观察相似 pattern → 论证纳入合理性）。R1 反驳称操作性定义有效且有 RE 文献支撑（Berry et al. 2004 广义分类、Dalpiaz et al. 2018 共现研究、Li et al. 2024 11-type taxonomy），改名 "policy specification defects" 会切断文献联系。

**共识**: 无论对理论严重程度的判断如何，§3 需更清晰区分 linguistic ambiguity（狭义）和 specification ambiguity（广义），正面回应理论张力而非依赖读者接受操作性定义。

**W4. Disambiguation Neglect 新颖性被高估 [R2 SHOULD-FIX, R1 AGREE]**

Introduction contribution (3) 将 Disambiguation Neglect 列为 primary contribution，但 Liu et al. (2023, EMNLP) 已证明 LLMs collapse interpretations, Hu et al. (2025) 论证 missing conceptual representations。本文增量是在 agent policy 场景中量化（4.6% awareness），应重新定位而非暗示发现新现象。

**W5. Differential Nocuity 框架增量贡献有限 [R2 SHOULD-FIX, R1 AGREE]**

Berry & Kamsties (2004) 的 nocuous/innocuous 二分法已隐含 type-dependent risk，Willis et al. (2008) 已研究 nocuity degree。§7 的命名暗示新 framework，应定位为 "empirical validation of differential nocuity in LLM agents"。

**W6. Clause identity 22.4% variance 被误述为 type identity [R2 SHOULD-FIX, R1 AGREE]**

§5.1 明确写 "Clause identity explains 22.4% of variance"——这是 300 clause pair 的 random effect，非 6 type 的 fixed effect。Introduction contribution (2) 的 "type identity explaining 22× more variance" 措辞具有误导性。Clause identity ≠ type identity，前者主要反映 clause-level heterogeneity。

**W7. SESOI ±15pp 论证存在循环性 [R1 SHOULD-FIX, R2 AGREE]**

"≥15pp warrants distinct policy handling" 用结论论证前提；"exceeds perturbation bound by >2×" 是测量噪声标准非实质性差异标准。在安全场景下 ±15pp 相当宽松。好的一面是提供了 7-margin 敏感性分析 + margin-free bootstrap 作为补充。建议从部署角度做实质论证。

**W8. Cross-judge 仅用 OpenAI 家族模型 [R1 SHOULD-FIX, R2 AGREE]**

GPT-5.4/GPT-4.1 可能共享 type-specific correlated bias。R2 补充区分影响范围：C1/C2 的 within-pair Δpp 中 judge bias 被消除（对差值安全），C4 的 cross-model absolute rate comparison 受影响。Limitations 应增加讨论。

**W9. Human validation n=32-34/type 不足以支撑 type-level claims [R1 SHOULD-FIX, R2 AGREE]**

Scopal CI [0.00, 1.00], coreferential CI [0.00, 0.84] 完全无信息。Type-level claims (C2-C4) 的有效性依赖对自动 judge 的 type-level 信任——但 auth scope κ=0.385 表明此信任在至少一个类型上脆弱。

### MINOR

**W10. Discussion vs Appendix B 的 mitigation 数字不一致 [R1 MINOR, R2 AGREE]**

§7 报告 GPT-5.4 incompleteness +14pp (p=0.118), auth scope −12pp (p=0.070)；Table 4 同模型同类型分别为 −2.6pp 和 −40.0pp。确认为两个不同实验（§7: n=50/GPT-5.4/generic+type-specific; Appendix B: 1,256 episodes/5 models/type-specific only），但论文未明确说明两者关系。

**W11. Mitigation incompleteness worsening (+14pp, p=0.118) 的因果解释过度 [R2 MINOR, R1 AGREE]**

§7 用确定性语言 "triggers confabulation rather than caution" 解释非显著趋势（p=0.118）。应标注为 non-significant trend 并降低解释确定性。

**W12. Abstract "risk gradient" vs §5.2 "two-tier structure" 术语不一致 [R2 MINOR, R1 AGREE]**

"Gradient" 暗示连续变化，"two-tier" 暗示离散分层。应统一术语。

**W13. Coreferential 被排除在 mitigation 和 replication 之外 [R2 MINOR, R1 AGREE]**

技术原因合理（Appendix B），但 6 类 taxonomy 中 1 类在两个重要实验中完全缺席影响完整性声明。Limitations 未提及此点。

**W14. Domain 泛化性有限 [R1 MINOR, R2 AGREE]**

τ²-bench 仅覆盖零售/航空客服。医疗/金融/法律领域可能产生不同的类型层级。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识 [AGREE]：

1. **C1 证据充分**（OR=15.1, 7 模型一致），matched-pair 因果设计是本文最大贡献
2. **Auth scope κ=0.385 削弱 C4**: 52pp range 基于最低 reliability 类型, 应降级或重度 caveat
3. **C2 表述过强**: "two-tier hierarchy" 在 bootstrap 中仅 34.3% 稳定, Kendall's W 不显著, margin-dependent
4. **Clause vs type identity**: 22.4% variance 是 clause random effect 非 type fixed effect, contribution (2) 措辞误导
5. **Disambiguation Neglect 新颖性**: 已有文献记录的现象在新场景中的量化, 非新发现
6. **Differential Nocuity 增量**: empirical validation 而非新 framework
7. **Mitigation 数字不一致**: §7 和 Appendix B 是两个不同实验, 需明确区分
8. **Mitigation over-interpretation**: p=0.118 不应用确定性因果语言
9. **统计方法论优秀**: TOST + bootstrap + Holm-Bonferroni 在该领域罕见
10. **Error analysis 有价值**: failure mechanism 对应和 systematic nocuity 提供机制理解

## Reviewer Divergence

**唯一实质分歧: Taxonomy 理论基础的严重程度**

- **R2**: incompleteness/conditional precedence 不属于 ambiguity, §3 论证存在循环, 建议重新框架为 "policy specification defects" 或大幅扩展理论论证
- **R1**: 操作性定义有效且有 RE 文献充分支撑（Berry et al. 2004, Dalpiaz et al. 2018, Li et al. 2024）, 改名会切断文献联系, 但同意 §3 讨论应更清晰

**Review Director 判断**: 这是一个理论 framing 偏好问题而非 fatal flaw。论文的操作性定义有文献基础，但 §3 确实需要正面回应理论张力，而非仅依赖读者接受广义定义。按 SHOULD-FIX 处理，不升级为 MUST-FIX。

---

## Questions

**Q1 [R2]**: Bootstrap AU p=0.47 如何与 "incompleteness stands apart" 的 confident framing 调和？

**Q2 [R2]**: "Clause identity explains 22.4% of variance" 是 300 clause pair 的 random effect 还是 6 type 的 fixed effect？如果前者，contribution (2) 措辞需修正。

**Q3 [R2]**: Temperature=0 下 ICC=0.919 的 8.1% variance 来自 API non-determinism 还是 episode-level randomness？

**Q4 [R1]**: Auth scope cross-judge κ=0.385 的 raw agreement 是多少？可否计算 PABAK/AC1 区分 prevalence paradox？

**Q5 [R1]**: Confound-adjusted effect size 重做 TOST，C2 是否仍成立？

**Q6 [R1]**: Perturbation control 的修改量是否与 ambiguity perturbation 的 token-level 变化量匹配？

**Q7 [R1]**: Kendall's W=0.398 (p=0.072) 不显著——除 incompleteness 外，type hierarchy 是否 model-dependent？

---

## Missing References

R2 建议补充（R1 部分反驳）：
- OpenAgentSafety (ICLR 2026) — comprehensive agent safety framework（如果提供 complementary perspective）
- Agent-SafetyBench (2024) — 349 interactive environment agent safety benchmark（如果与已引用 agent safety 工作有实质差异）
- Automated Repair of Ambiguous NL Requirements (2025, arxiv:2505.07270)

R1 指出 Ferrari et al. (2019) "Ambiguity in RE" 应已被引用为 ferrari_ambiguity_2019。

---

## External Review

外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。

---

## Visual Layout Check（非评分项）

状态: **done**（耗时 ~3.5 分钟）

### Findings (0 critical, 2 warning, 8 info):

**Warning:**
- Pages 4-5: 连续两页纯文本（Method + early Results），无任何 display item 穿插。建议 §4 添加模型/数据集汇总表打破视觉单调。
- Page 15: 最后一页 Appendix Q 仅 ~6 行内容，~90% 空白。建议合并到前一页或调整附录顺序。

**Info:**
- Page 2: Figure 1 左侧 taxonomy tree 叶节点标签字号偏小
- Page 6-7: Figure 2/3 热力图单元格数值和 axis label 字号较小（约正文 60%），建议增大
- Page 6: Table 2 booktabs 风格规范，最优值加粗
- Page 3: Table 1 分类表排版清晰
- Page 12: 附录含 6 个表格，密度极高但作为附录可接受
- Page 6-7: 热力图 yellow-to-red 渐变基本 colorblind-safe
- Page 9-10: 参考文献格式统一，无未解析引用

---

## Overall Assessment

**评分: 3.5 / 5 (Borderline Conference)**
**置信度: 4 / 5**
**评分对应: ARR Overall Assessment 3.5 = Borderline Conference**

### 核心判断

这是一篇**方法论扎实的实证论文**。Matched-pair causal design + perturbation control 在 NLP agent safety 领域确属首创，C1（ambiguity → violation 因果效应，OR=15.1, 7 模型一致）证据充分，统计分析（TOST + bootstrap + Holm-Bonferroni）远超该子领域平均水平。Error analysis 中的 failure mechanism 类型对应和 systematic nocuity 发现有部署价值。

### 阻碍 Conference 接收的问题

1. **测量可靠性**: C4 基于最低 reliability 类型（auth scope κ=0.385）做 numbered claim；C2 的 "two-tier hierarchy" 在 bootstrap 中仅 34.3% 稳定，Kendall's W 不显著
2. **Framing 校准**: clause vs type identity 的 22× claim 有误导性；Disambiguation Neglect 和 Differential Nocuity 的增量贡献被高估——它们是已有概念的 domain application 而非独立理论创新
3. **SESOI 论证**: ±15pp 的实质性论证不足，影响 C2 的核心表述

### 升级路径

如果 revision 中：(1) 将 C4 降级为 Discussion observation 或补充 prevalence-adjusted agreement；(2) 弱化 C2 为 "incompleteness consistently highest, remaining types form less differentiated cluster"；(3) 修正 clause/type identity 归因；(4) 降低 coined terms 的 novelty claim——可升至 **4.0 (Conference)**。核心实证贡献（C1 + error analysis）已达 Conference 水平，framing 调整即可达标。

---

## Detailed Comments

### §1 Introduction
- Contribution (2): "type identity explaining 22× more variance" 需修正为 "clause identity"，并补充 type fixed effect variance
- 52pp range 的 caveat 权重不足——κ < 0.4 的维度上不应作为核心 finding 突出
- Contribution (3) 降低 Disambiguation Neglect 的 novelty claim

### §3 Taxonomy
- "Scope of ambiguity" 段落需扩展：更清晰区分 linguistic ambiguity vs specification ambiguity，正面回应理论张力
- 引用 Dalpiaz et al. (2018) 和 Berry et al. (2004) 的论证可以更充分

### §4 Method
- SESOI ±15pp: 增加部署场景论证或将 ±10pp 并列为 primary
- Pages 4-5 考虑添加 model summary table 打破纯文本节奏

### §5 Results
- §5.2: "two-tier structure"/"stands apart" 弱化为更谨慎的表述，正文报告 AU p=0.47
- §5.4: 明确区分 cross-judge κ=0.385 和 human-LLM κ=0.644 的数据来源
- C4 降级为 Discussion observation 或在 abstract/conclusion 中不引用 52pp

### §6 Analysis
- §6.2: Disambiguation Neglect 定位为 "已知现象在 agent policy 场景中的首次量化"
- Incompleteness wording 已较好但 §6.2 引用 good-enough processing 的 analogy 需加 mechanism-level caveat

### §7 Discussion
- Differential Nocuity: 改为 "empirical validation" 定位
- Mitigation: (a) 明确标注 §7 和 Appendix B 是两个独立实验；(b) incompleteness +14pp (p=0.118) 标注为 non-significant trend
- "Abstract 'risk gradient' vs 正文 'two-tier'" 术语统一

### §8 Limitations
- 增加 single-family judge bias 讨论
- 提及 coreferential 排除对 taxonomy 完整性的影响
- 更强调 type-level human validation gap