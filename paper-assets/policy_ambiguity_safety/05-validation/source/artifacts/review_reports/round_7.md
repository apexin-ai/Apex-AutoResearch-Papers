---
round: 7
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T15:49:24.816086+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 7 (Fresh)

**论文**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**审稿人**: Reviewer 1 (方法严谨性) + Reviewer 2 (新颖性/完整性)
**审稿模式**: 重新审稿 (fresh)

---

## Summary

本文通过 matched-pair 因果设计研究 LLM agent 在策略歧义下的安全违规。在 τ²-bench 上构建 300 组 clause pairs（6 种歧义类型，two-layer taxonomy），跨 5 个模型评估 2,997 episodes，另有 2 个模型族的 replication。核心发现：(1) 歧义条款使违规率增加 34.0pp（OR=15.1）；(2) 类型间存在显著层级（V=0.137），incompleteness 最高（46-62%），authorization scope 模型间差异最大（12-64%）；(3) agent 几乎不具备歧义识别能力（<11%）。论文提出 Differential Nocuity 框架。

---

## Strengths

1. **Matched-pair causal design 是本文最大的方法论贡献**（R1+R2 共识）。相比 DRIP-R 等 correlational work，每对 clause pair 仅做 minimal edit + perturbation control（n=300, Δ=-0.67pp）显著增强因果推断可信度。这是首个将歧义类型与 agent 安全违规建立因果关系的研究。

2. **统计分析全面且恰当**（R1+R2 共识）。McNemar's test（paired binary）、Fisher's exact（per-type）、TOST equivalence（区分 "no difference" vs "equivalent"）、Holm-Bonferroni 校正、效应量报告（OR, V, Δpp）均选择得当。Sensitivity analysis（7 个 SESOI margins, 2 个 severity thresholds）增加稳健性。

3. **Cross-architecture replication 广泛**（R1+R2 共识）。5+2 个模型跨 6 个 provider，C1 在所有 7 个模型上 p < 10⁻⁶，C2 ranking ρ=0.90 (LLaMA)，大幅增强外部效度。

4. **Taxonomy 有双重理论基础**（R2）。植根于 CL 文献（Li et al., 2024）和 RE 文献（Massey et al., 2014; Berry & Kamsties, 2004），操作性定义清晰。CL-first framing 适合 EMNLP。

5. **Intellectual honesty**（R1）。主动标注 C3 inconclusive、C4 exploratory、incompleteness confound、per-type judge reliability 差异，在 NLP 论文中不常见。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[N1] 主文超出 EMNLP 2026 的 8 页正文限制**（R1 AGREE + R2 raised，视觉审查 confirmed）
- 正文（Abstract → Conclusion）约 8.5-8.7 页，超限约 0.5-0.7 页
- Table 2（mitigation experiment, ~50/cell, preliminary）和 Conclusion 均在 Page 9
- ARR desk reject 风险
- 修复路径：Table 2 移至 Appendix（省 ~1/3 页）+ Discussion 压缩重复措辞（"upper bound...confound" 逐字重复 ≥4 次）+ Introduction contribution list 精简

**[N2] Authorization scope 测量可靠性过低，无法充分支撑 "canary type" 主张**（R1 raised, R2 AGREE with nuance）
- Cross-judge κ=0.385（fair），所有类型中最低
- Human-LLM κ=0.644，95% CI [0.35, 0.91] 极宽
- Per-type validation n=34 不足
- R2 补充 nuance：matched-pair 的 within-model Δpp 受 judge 内部一致性保护，cross-judge disagreement 主要影响绝对率而非 treatment effect。但 Abstract/Conclusion 突出 canary type 时缺乏 measurement-uncertainty caveat
- 修复路径：Abstract/Conclusion 加 measurement-uncertainty 限定语；报告 within-judge raw agreement + detection vs severity 分离分析

**[N3] Incompleteness information-addition confound 在 Abstract/Conclusion 中 hedging 不足**（R2 raised as critical, R1 AGREE with nuance）
- Incompleteness 的 unambiguous variant 必须添加新政策内容，与其他 5 类结构性不同
- Abstract "universally dangerous" 和 Conclusion "universal blind spot" 措辞过强
- Appendix F 仅报告 "coefficient change <8%"，缺 OR 变化量
- R1 nuance：论文已有多项控制（§3 预标注、§5.2 "upper bound"、coreferential lower bound、logistic regression），核心问题是呈现方式而非分析缺失
- 修复路径：报告控制前后 OR 变化量；Abstract/Conclusion 加限定语

**[N4] 缺少 a priori power analysis，50 pairs/type 的样本量合理性未论证**（R1 raised, R2 AGREE with nuance）
- TOST equivalence 的 null 结果可信度取决于功效——当前无法区分 "types are equivalent" vs "lack power to detect difference"
- Per-type per-model cells (n≈50) 估计不稳定
- R2 nuance：C1 power 显然 >0.99 不是问题；关键在 TOST 和 per-type interaction
- 修复路径：报告 post-hoc power analysis（C1 确认 >0.99，TOST 和 per-type 诚实报告）

### Should-Fix（影响评分但不一票否决）

**[W1] Judge-model confounding 对 C4 的限制**（R1 raised as critical, R2 REBUT to warning）
- R2 提出有力反驳：matched-pair 设计保护 within-model 的 C1/C2（judge bias 在 Δpp 中抵消）；GPT-4.1 judging GPT-5.4 的 bias 方向与结论相反（低估而非高估）
- 共识：对 C1/C2 非威胁，仅影响 C4 cross-model 比较
- 修复路径：Method 中增加 explicit 解释 matched-pair 为何保护 within-model comparisons

**[W2] "Differential Nocuity" 被呈现为 framework 但缺乏形式化**（R2 raised as critical, R1 REBUT to warning）
- R1 反驳：conceptual organizing principle（类似 "good-enough processing"）不需要 formal model；框架连接了 type hierarchy + channel availability + systematic nocuity
- 共识：非 critical，但 Discussion 应更明确阐述框架组成部分
- 修复路径：Discussion 开头用 2-3 句话明确组成部分，或降级措辞

**[W3] TOST SESOI ±15pp 缺乏外部锚定**（R1 raised, R2 AGREE）
- ±10pp 时仅 3/6 mid-tier pairs equivalent，±12pp 时 5/6——"robust two-tier structure" 主要在 ≥15pp 成立
- 修复路径：主文讨论 SESOI 敏感性，报告 minimum margin for two-tier emergence (~±12pp)

**[W4] Table 2 (mitigation experiment) 样本量不足**（R1+R2 共识）
- Per-cell ~50 episodes，DeepSeek 两个类型显示增加而非减少
- 修复路径：移至 Appendix，主文保留 1-2 句方向性总结（同时缓解 N1 页数问题）

**[W5] 与 DRIP-R 差异化论述不够有力**（R2 raised, R1 部分同意）
- §2 仅两句话说明差异，需要更 explicit 的 contribution delta
- 修复路径：Related Work 增加详细对比

**[W6] Human validation 细节不足**（R1+R2 共识）
- 缺少 annotator blindness、disagreement distribution、stratification strategy
- 修复路径：补充 1-2 句

**[W7] Failure mode taxonomy inter-coder κ=0.52**（R1 raised, R2 AGREE）
- Moderate agreement 对独立 contribution 偏低；arbitrary rule selection κ=0.29
- 修复路径：降级为 exploratory analysis，或报告 per-category AC₁

**[W8] ICC=0.919 仅限 OpenAI 模型**（R1+R2 共识）
- Cross-provider temporal reproducibility 未直接测量

**[W9] 引用 metadata 错误**（R1+R2 共识）
- ferrari_defects_2018 第一作者为 Rosadini；lassiter_goodman_2017 年份可能为 2015

**[W10] 遗漏相关工作**（R2 raised, R1 部分同意）
- WSD survey (Navigli 2009) 对 CL venue 是明显空白
- Agent-SafetyBench, AgentSpec 可选

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致 [AGREE]：
- 主文超出 8 页限制（必须修复）
- Incompleteness confound 的 hedging 在 Abstract/Conclusion 不足
- Authorization scope 需要 measurement-uncertainty caveat
- 需要补充 power analysis
- Table 2 应移至 Appendix
- Matched-pair causal design 是主要方法论贡献
- Human validation 细节需补充
- 引用 metadata 需修正

## Reviewer Divergence

**Judge-model confounding 的严重性**
- R1 认为 critical：每个 model 由单一 judge 评估，C4 model-level 结论受限
- R2 REBUT to warning：matched-pair 设计保护 C1/C2，confounding 仅影响已标注 exploratory 的 C4
- Director 判断：R2 的技术论证成立——within-model paired comparison 确实不受 judge systematic bias 影响。降级为 warning，但需在 Method 中 explicit 解释。

**Differential Nocuity 形式化**
- R2 认为 critical：缺乏 predictive/prescriptive model，overclaiming
- R1 REBUT：conceptual framework 在 NLP 中常见，不需要 formal model
- Director 判断：R1 的论点更有说服力——要求实证论文提供 formal model 标准偏高。但 Discussion 中应更清晰阐述框架组成部分。降级为 warning。

**Excitement**
- R1：4.0/5——首个 causal study + genuinely surprising findings（Ambiguity Blindness, systematic permissiveness bias）
- R2：3.0/5——核心 insight "不同类型有不同风险" 较为 expected
- Director 判断：R1 更准确。论文贡献不仅是发现差异，而是用严格因果设计量化差异并揭示 unexpected patterns（incompleteness 普遍性、0% conservative refusal、Qwen3/DeepSeek 0% disambiguation awareness）。综合 Excitement 3.5/5。

---

## Questions for Authors

1. 50 clause pairs/type 的决定依据？基于 pilot study 还是资源约束？
2. Cross-judge calibration 100 episodes 中 per-model judge agreement 分布？
3. Logistic regression 控制 incompleteness confound 时具体控制了哪些变量？控制前后 OR 变化量？
4. Template-based clause generation pipeline 的具体操作？同一 template 产生的多个 pairs 是否有 structural correlation？
5. C3 (layer effect) inconclusive 但保留在主文的理由？（R2 反驳删除建议：报告 null results 是好的科学实践，但主文空间宝贵）
6. "Differential Nocuity" 是否有超越 empirical observation 命名的理论预测力？

---

## Missing References

- **Navigli (2009)** — WSD survey，与 lexical ambiguity type 直接相关，CL venue 空白（R1+R2 共识应补充）
- **Agent-SafetyBench (Zhang et al., 2024)** — 2000 test cases, 8 safety risk categories（R2 建议，R1 认为可选）
- **SafeAgentBench (Yin et al., 2024)** — embodied agent safety（R2 建议，R1 认为可选）
- **AgentSpec (Poskitt et al., ICSE 2026)** — runtime enforcement for safe agents（R2 建议）

引用真实性检查：38 条引用中 27 条 verified，7 条 not_found（tech report/新 arXiv，确认存在），4 条 minor metadata mismatch，0 条 fabricated。

---

## External Review

外部审稿：未配置（项目配置中无 external_review section）。

---

## Visual Layout Check（非评分项）

状态：**done**（2026-05-21 15:31 → 15:35，耗时约 3.5 分钟）

发现（2 critical + 3 warning + 3 info）：

| 严重性 | 位置 | 发现 |
|--------|------|------|
| critical | Page 9 | 主正文延伸至第 9 页约 3/4 处，超出 8 页限制约 0.75 页 |
| critical | Page 14 | 最后一页仅 ~10 行文字，~90% 空白 |
| warning | Pages 3-5 | 连续 3 页纯文本无 display item（§3+§4），建议添加 taxonomy 图 |
| warning | Page 13 | 6 个表格（Tables 4-9）挤在同一页，字号过小 |
| warning | Page 8 | 纯文本页（§6+§7 开头），但属定性分析可接受 |
| info | Page 2 | Figure 1 子面板文字偏小（约正文 60-65%） |
| info | Pages 6-7 | Figure 2/3 颜色方案不一致（分组柱状 vs 热力图） |
| info | Page 9 | Table 2 正负值无颜色/箭头辅助区分 |

---

## Overall Assessment

**评分：3.5 / 5（Borderline Conference）**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 4.0 | 3.0 | **3.5** |
| Reproducibility | 3.0 | 3.5 | **3.25** |
| Confidence | 4.0 | 4.0 | **4.0** |
| **Overall** | **3.5** | **3.5** | **3.5** |

**EMNLP 2026 评分标准对照**：3.5 = Borderline Conference（介于 Findings 可接收与主会议可接收之间）。

**核心判断**：论文在研究问题（首个 causal, type-granularity ambiguity→safety mapping）和实验设计（matched-pair + perturbation control + 7-model replication）方面达到 Conference 水准。但四个 critical issues 共同削弱核心叙事的可信度：(1) 格式违规（desk reject 风险）；(2) 最突出的 type-specific 发现（auth scope canary type）建立在最低可靠性测量上；(3) 最高违规率的类型（incompleteness）受 information-addition confound 影响且 hedging 不足；(4) two-tier structure 的 equivalence claims 缺少 power analysis 支撑。

**升分路径（3.5 → 4.0）**：
1. 修复页数超限（N1）——必须，否则 desk reject
2. Auth scope canary type 加 measurement-uncertainty caveat（N2）
3. Incompleteness 在主文加限定语 + 报告 OR 变化量（N3）
4. 补充 post-hoc power analysis（N4）
5. Table 2 移至 Appendix（同时解决 N1 和 W4）

这些修改均可在 revision 中完成，不需要新实验。

**降分风险（3.5 → 3.0）**：
- 页数超限被标记为 desk reject
- Incompleteness confound 被认为根本性破坏 type hierarchy 解读

---

## Detailed Comments

### §1 Introduction
- Contribution list 4 项偏多，C1（因果定量）和 C3（failure mode taxonomy）方法论层次不同但可精简表述
- "Differential Nocuity framework" 措辞暗示 formal framework，建议在首次出现时明确定位为 conceptual framework / empirical observation

### §3 Taxonomy
- 双层结构理论支撑充分，但 authorization scope 的 linguistic vs specification 归类边界案例未讨论
- 建议补充 taxonomy 可视化（树状图或层级表），缓解 Pages 3-5 连续纯文本问题

### §4 Method
- Matched-pair design 是核心优势，但缺少 power analysis（N4）
- Cross-judge 设计需要 explicit 解释为何 within-model Δpp 不受 judge bias 影响（W1）
- Human validation 需补充 annotator blindness 和 stratification 细节（W6）

### §5 Results
- C1、C2 证据强度充分
- C3 inconclusive——两位 Reviewer 对是否保留存在分歧，但报告 null result 有价值
- C4 exploratory 标签恰当，但 auth scope 相关结论需 measurement-uncertainty caveat

### §6 Analysis
- "Ambiguity Blindness" 是有价值的新观察（Qwen3/DeepSeek 0% awareness 尤其 striking）
- Failure mode taxonomy inter-coder κ=0.52 偏低，建议降级为 exploratory

### §7 Discussion
- "Why incompleteness resists safety training" 推测合理但缺乏直接机制证据
- Table 2 应移至 Appendix
- Differential Nocuity 框架组成部分需更明确阐述

### §8 Conclusion
- 需压缩至 Page 8 以内
- Incompleteness "universal blind spot" 需限定语

### Limitations
- 覆盖面良好（model coverage, domain scope, synthetic ambiguity, cross-judge asymmetry, failure mode analysis）
- 建议增加：incompleteness information-addition confound、prompt sensitivity、per-type 样本量限制

### References
- 修正 ferrari_defects_2018、lassiter_goodman_2017 metadata
- 补充 Navigli (2009) WSD survey