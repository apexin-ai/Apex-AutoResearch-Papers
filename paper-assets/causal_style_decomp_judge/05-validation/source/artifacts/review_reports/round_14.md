---
round: 14
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T06:59:16.264845+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 16 (Fresh Review)

**论文**: "The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation"
**Venue**: EMNLP 2026 via ARR (May cycle), 截止 2026-05-25
**Reviewers**: R1（方法严谨性）+ R2（新颖性/完整性）
**审稿模式**: Fresh（无上轮记忆）

---

## Summary

本文提出 Controlled Style Decomposition (CSD)，一种黑盒诊断方法，通过 NLI-gated 内容控制、单轴风格改写和位置控制的 pairwise 比较，量化 LLM judge 在 Likert 与 pairwise 两种评测模式下对表层风格特征的敏感性差异。核心发现为"Likert Blindspot"——pairwise comparison 检测到统计显著的风格偏好（BT p < 0.001），而 Likert 在同一数据上无法检出（p > 0.17），跨 4 个 judge、3 个 benchmark、2 个主轴复制。GEE conditional decomposition 揭示 verbosity 为 style-dominated（Style OR 8–13），formality 为 conditional effect（Style OR 和 Originality OR 均显著）。

---

## Strengths

**S1. 研究问题重要且具实践意义。** 测量模式对 LLM judge 风格敏感性的影响此前未被严格量化。鉴于 pairwise（RLHF/DPO reward signal）与 Likert（benchmark evaluation）分别主导不同 pipeline 阶段，这一发现对 evaluation 设计有直接操作意义。[R1-S1, R2-S1 共识]

**S2. 统计框架全面且层次清晰。** 三层分析设计（6-test primary family + confirmatory + exploratory）、七种统计方法的 sensitivity hierarchy（Table 13–14）、Holm-Bonferroni 扩展至 8-test family 后结果依然显著（Appendix S）。统计框架本身是方法论贡献。[R1-S2, R2 共识]

**S3. 多 judge × 多 benchmark 系统复制。** 四个独立架构的 judge + 负控制、三个 benchmark 的交叉复制，核心发现一致性强。Verbosity 在全部四个 target judges 上均为 style-dominated（BT > 70%, all p < 0.0001; Likert 全部 NS），这是有力证据。[R1-S3, R2-S3 共识]

**S4. GEE conditional decomposition 是真正的方法论贡献。** 将聚合偏好分解为 style-specific 和 quality-correlated 成分，发现 per-axis confound structure 差异——这在 Thurstone 传统中没有对应物。Table 2 的 Style OR vs Originality OR 对比提供了超越"存在 bias"的结构性诊断。[R1-S4, R2-S2 共识]

**S5. 写作质量和附录体系。** 8 页正文内容密度高但逻辑清晰，从现象→机制→验证的叙事连贯。20 个附录覆盖广泛的 robustness 分析。[R1-S5, R2-S5 共识]

---

## Weaknesses

### Must-Fix

**MF1. NLI gate content preservation 验证不充分，削弱因果推断基础。**
[R1-W1, R2 交叉 AGREE]

NLI gate 是 CSD 因果链条的核心——阻断 R→Q 路径确保 rewrite 仅改变 style。但人工验证存在三层不足：(a) 仅 50 pairs（n=88 的 57%），2 名标注员；(b) inter-annotator κ=0.44（moderate），对核心 validity check 偏低；(c) Annotator 2 pass precision 下界仅 65.3%（Wilson CI [65.3%, 93.6%]），意味着最坏情况下约 1/3 gate-passed pairs 存在 content contamination。若此成立，pairwise 的更高敏感度可能部分源于对 content 微妙差异的检测力而非 style sensitivity 本身。GPT-4o cross-validation（92.1%/82.6%）为 LLM 验证而非独立人工验证。

**建议**：扩大人工验证至全部 88 pairs + 3+ 标注员；提供 content change taxonomy（factual error / nuance shift / elaboration）；对 human-flagged content-changed pairs 执行 sensitivity analysis。

**MF2. Negative control (Claude Sonnet 4) 证据不具说服力。**
[R1-W2, R2-W2 双方独立 Must-Fix, 交叉全部 AGREE]

TOST 在 Δ=10pp 时 power 仅 42%——未能拒绝非等价的 null 不能解释为等价的证据（absence of evidence ≠ evidence of absence）。论文转而依赖三条收敛证据，但每条单独看都不充分：
- TOST Δ=15pp p=0.01——但 15pp 等价边界过宽（GPT-4o formality BT=63% 已被论文视为显著 style preference，而 Δ=15pp 对应 BT=65%）
- GEE Style OR 跨三个 benchmark 一致 NS（1.47/1.99/1.64）——但 non-significance ≠ evidence of absence，且 OR=1.99 point estimate 非 trivial
- GPT-4o contrast——qualitative comparison，非 formal test

Negative control 是验证 CSD pipeline 不产生 false positive 的关键环节。证据不足使读者无法排除 pipeline artifact。

**建议**：(a) 将 negative control 结论降级为 suggestive 而非 definitive；(b) 明确报告达 80% power 所需 n（≈200）；(c) 考虑 Bayesian equivalence testing 或增加第二个 negative control judge。

**MF3. "Systematic" claim 基础过窄——仅 2 个主轴。**
[R2-W1 Must-Fix, R1 间接支持]

Abstract/Conclusion 反复使用"systematically divergent"，但一手证据仅来自 formality 和 verbosity，register 为 exploratory 且有 evaluator-producer overlap。两个高度相关的表层轴（FK grade d=0.50 cross-axis leakage）不足以声称"systematic"。Semantic-level axes（hedging, humor）被 NLI gate 系统性拒绝，限制了 CSD 的适用范围。

**建议**：将"systematic"降级为"consistent across tested axes"或类似限定措辞。

### Should-Fix

**SF1. GEE OR 在 n=88→355 时出现 49% shrinkage，Table 2 效应量可能普遍高估。**
[R1-W3, R2 交叉 AGREE]

Qwen3-32B formality Style OR 从 4.20 降至 2.15（−49%），远超 Nemes et al. (2009) 报告的典型校正幅度。仅此一个条件有 scaled replication——其他条件的 ORs（特别是 verbosity Style OR 8–13）可能同样存在膨胀。虽然 qualitative regime classification 在 ~50% shrinkage 下可能不变（projected verbosity 4–6.5 仍 >> Orig OR < 1），但 effect size 量级解读受影响。

**建议**：对至少一个 verbosity 条件执行 scaled replication；Table 2 增加 caveat 标明 n=88 ORs 可能为 upper bound。

**SF2. Construct divergence 讨论不充分，与 Abstract 三机制并列承诺不匹配。**
[R2-W4, R1-W8 相关]

Attenuation 获得完整 bootstrap 分析（Appendix K）和功效曲线（Figure 4），construct divergence 仅 Section 5.1 末段和 Limitations 简短提及。如果三种解释声称并列，construct divergence 需要同等深度——至少包含操作性定义（absolute quality vs ordinal preference）和可检验预测。

**SF3. Evaluator-producer overlap 缓解不充分。**
[R1-W4, R2 交叉 AGREE]

仅用 GPT-4o 作为替代 rewriter，22% OR 降幅是 lower bound。GPT-4o 与 target judge GPT-4o 存在完全重叠，且所有替代 rewriter 都是 instruction-tuned LLM——无法排除 shared training distribution 的 confound。22% 意味着约 1/5 的观测效应可能来自 overlap。

**建议**：在 Limitations 中明确讨论 22% 作为 lower bound 的含义和 instruction-tuned LLM 替代的局限。

**SF4. FK grade d=0.50 cross-axis contamination 未被充分控制。**
[R1-W5, R2 交叉 AGREE]

Length-controlled regression 和 Sobel mediation test 控制了 word count/sentence length，但 FK grade 还反映 readability/complexity。d=0.50 的 readability shift 可能独立于 verbosity 影响 judge quality perception。

**建议**：GEE 中加入 FK grade 作为协变量验证 formality Style OR 是否依然显著。

**SF5. Cross-benchmark "severity spectrum" 为 post-hoc 解释。**
[R2-W5]

Section 5.3 将不同 benchmark 效果量差异解释为 severity spectrum，但无预先假设。AlpacaEval 效应更强的归因缺乏 benchmark 特性差异的定量支撑。

**建议**：明确标记为 exploratory/post-hoc。

### Minor

**M1. Title "Blindspot" 隐含 Likert attenuation 因果偏好。**
[R1-W8, R2-W6 双方独立指出, 交叉全部 AGREE]

标题和正文将分歧框架为 Likert 的"盲点"，但论文自身承认 pairwise amplification 同样可能。等价的替代解读：pairwise 对 surface-level style 过度敏感，Likert 正确忽略了不应影响 quality judgment 的因素。

**M2. Table 1 信息密度过高。**
[R1 Minor, R2-W7 Minor, 交叉 AGREE]

15 行 + 6 行脚注挤在一张表。建议拆分为 LLMBar primary (4 judges × 2 axes) + cross-benchmark replication 两表。

**M3. 'style bias' / 'style sensitivity' / 'style preference' 术语混用。**
[R2-W8, R1 间接相关]

三个术语含义不同（bias=方向性偏差, sensitivity=双向响应性, preference=描述性），应统一或明确区分。

**M4. BT unidimensionality 假设与论文多维评估论点存在张力。**
[R1-W7, R2 交叉 AGREE]

Limitations 已提及但方法论章节缺乏预先讨论。应在 Section 3 说明 BT 在此作为 summary statistic，unidimensionality 限制由 GEE 补充。

**M5. 100-point continuous Likert 仅在 Qwen3-32B 上测试。**
[R1-W6 Should-Fix, R2 交叉 REBUT 降级为 Minor]

R2 认为 proof-of-concept 下单 judge 足够（Qwen3 是 Likert 效应最强的 judge，保守检验）。Director 采纳 R2 判断，降级为 Minor。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识（[AGREE]）：

1. **TOST underpowered** [R1-W2 = R2-W2]：negative control 证据不具说服力
2. **NLI gate validation** [R1-W1, R2 AGREE]：人工验证规模和质量不足
3. **Claim scope** [R2-W1, R1 间接]：2 axes → "systematic" 过宽
4. **GEE OR shrinkage** [R1-W3, R2 AGREE]：n=88 效应量可能高估
5. **Framing bias** [R1-W8 = R2-W6]：title 隐含 Likert 为缺陷方
6. **Evaluator-producer overlap** [R1-W4, R2 AGREE]：单一替代 rewriter 不充分
7. **Likert power** [R1-Q3 = R2-Q5]：Likert non-significance 可能仅反映 power 不足——替代解释讨论不充分

---

## Reviewer Divergence

仅一处分歧：

- **100-point Likert 复制**：R1 列为 Should-Fix（需多 judge 复制），R2 REBUT 降级（proof-of-concept 足够）。Director 采纳 R2 判断降级为 Minor。

---

## Questions

**Q1.** Likert non-significance 是否仅反映 power 不足？Formal power analysis 显示 5/6 cells 需 n ≥ 1,200。Bootstrap attenuation analysis（Appendix K）论证 d→0 是 structural 而非 power issue，但此分析以 pairwise 效应量为 benchmark——存在循环论证嫌疑。[R1-Q3, R2-Q5 独立提出]

**Q2.** Table 2 verbosity Orig OR < 1（全部四个 judges）——verbose rewrites 是否系统性引入 quality improvement？若是，pairwise 的高敏感度可能反映 content quality difference 而非 style sensitivity。[R1-Q1]

**Q3.** Direction-aware gating 额外放入的 21 pairs (32%) 是否在 BT/Likert 效应量上与原有 pairs 有系统差异？[R1-Q2, R2-Q3]

**Q4.** GEE exchangeable working correlation 是否对 AR(1)/unstructured 敏感？Appendix D 报告了 QIC 差异 < 0.001 和系数变化 < 0.02，但未报告替代结构的完整结果。[R1-Q4, R2-Q2]

**Q5.** 论文选择 formality 和 verbosity 是否因为这两个轴最容易通过 NLI gate？如果是，这引入选择偏差——论文仅展示了 CSD 最有利的案例。[R2-Q1]

**Q6.** 所有 target judges 均为 instruction-tuned chat models。Base models 上 Blindspot 是否存在？Instruction tuning 本身可能引入 style preference。[R1-Q5]

**Q7.** 4 个 target judges 均为 2024 下半年版本，风格敏感度是否随模型迭代变化（时间效度问题）？[R2-Q4]

---

## Missing References

- **Item Response Theory (IRT)**: 论文讨论 Likert 测量属性但未引用 IRT 框架。IRT 可定量回答"Likert 为什么在某些效应量下失效"。至少应引用 Embretson & Reise (2000) 或 de Ayala (2009)。[R2]
- **Bojar et al. (2016) WMT 转变经验**: 论文仅在 Section 3 脚注级别提及 WMT 从 ranking 到 rating 的转变，但未深入讨论社区积累的经验教训——这与核心论点直接相关。[R2]
- 其余引用覆盖充分。[R1]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 external_review.paperreview_ai）。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时约 3.5 分钟）

| 严重度 | 位置 | 发现 |
|--------|------|------|
| ⚠️ Warning | pp.3-4 | 连续 2 页纯文本（Related Work + Method 开头），无 display item。建议前移 Figure 2（因果 DAG）或在 Related Work 加小型 summary table |
| ℹ️ Info | p.2 | Figure 1（pipeline overview）单栏宽度，节点标签打印时可能偏小 |
| ℹ️ Info | p.5 | Figure 2 红色/橙色路径灰度打印区分度低，建议辅以不同线型 |
| ℹ️ Info | p.6 | Table 1 最优结果未加粗 |
| ℹ️ Info | p.7 | Figure 4 power 曲线图例文字偏小 |
| ℹ️ Info | p.9 | Limitations 篇幅较长但内容充实，不影响评审 |
| ℹ️ Info | pp.11-17 | Appendix 全为数值表格无 figure，视觉单调但可接受 |
| ℹ️ Info | p.20 | 最后一页 references 底部空白，正常 |

总计：0 critical, 1 warning, 7 info。排版质量整体良好，无格式违规。

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

**Confidence: 4/5**

**两位 Reviewer 一致评分 3.5，核心评估高度收敛。**

### 汇总判断

**方法论设计用心**——CSD pipeline 的三层控制（NLI gate → position swap → axis isolation）、GEE conditional decomposition、七方法 sensitivity hierarchy 展现了严谨的实验设计理念。4 judges × 3 benchmarks 的系统复制使核心发现不易被归因于 artifact。

**但因果推断链条存在两个关键缺口**：
1. NLI gate 人工验证（MF1: κ=0.44, precision 下界 65.3%）不足以建立"rewrite 仅改变 style"的因果前提
2. Negative control 证据（MF2: TOST power 42%）不足以排除 pipeline artifact

**Claim 强度超出证据**：
3. 2 个主轴 → "systematic"（MF3）
4. GEE OR 可能高估 ~50%（SF1）
5. Construct divergence 讨论深度不匹配（SF2）

**核心增量贡献（GEE decomposition）被 undersold**——论文将 "Blindspot" discovery 置于叙事中心，但 per-axis confound structure 的方法论贡献（Thurstone 传统中无对应物）更具持久价值。

### 改进路径

修复 MF1（扩大人工验证）+ MF2（增强 negative control 证据）+ MF3（限定 claim scope）后，论文有望提升至 4.0（Conference）。GEE decomposition 的方法论贡献足够支撑接收，但当前 framing 遮蔽了这一优势。

---

## Detailed Comments

### Section-by-Section

**Abstract**: "systematically divergent sensitivity" 超出 2 轴证据（→ MF3）。三机制并列但 construct divergence 在正文中发展不足（→ SF2）。

**Introduction**: 操作性定义 Blindspot 为"measurement-mode divergence"是改进。Thurstone 讨论的 3 个 LLM-specific distinctions（per-axis structure, source decomposition, binary split）有说服力。但 Title 仍偏向 attenuation 解释（→ M1）。

**Method (§3)**: CSD pipeline 设计清晰。DAG（Figure 2）有效传达设计逻辑。Direction-aware NLI gating 的理论依据充分（§3.2）。建议在 §3.3 预先讨论 BT unidimensionality 限制（→ M4）。

**Experiments (§4-5)**: 三层统计框架值得推广。Table 1 信息密度需降低（→ M2）。GEE decomposition 结果（Table 2）是论文最有价值的内容。n=88→355 shrinkage 讨论应更显著（→ SF1）。

**Robustness (§5.4)**: 六控制设计思路好，但每条证据的单独强度有限。NLI ablation（Appendix P）中 NLI-fail pairs 反转（BT 41.7%）是 gate 有效性的有力佐证。

**Limitations**: 覆盖面广（quality-style confounding, evaluator-producer, scope, validation methodology），但多个 reviewer 关切点（TOST power 含义、22% overlap 上界、FK readability）可进一步展开。

**Appendix**: 体系完整（A-Y），NLI threshold sweep（Appendix F）、GEE diagnostics（Appendix D）、rewriter independence（Appendix E）等提供了充分的技术细节。Rewriting prompts（Appendix V）已补全。