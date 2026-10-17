---
round: 4
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T13:01:15.636381+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：The Likert Blindspot

**论文**：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
**Venue**：EMNLP 2026 Main Conference (via ARR)
**审稿模式**：Fresh（初审）
**Reviewer 编排**：2 人（R1 方法严谨性 / R2 新颖性与完整性）
**轮次**：Round 1 独立审稿 → 交叉分享 → 共识收敛（1 轮达成）

---

## Summary

论文提出 Controlled Style Decomposition (CSD)，一个黑盒框架，通过 style-controlled rewriting、NLI content gating 和 position-controlled pairwise comparison 检测 LLM judge 的 per-axis style bias。核心发现是 Likert Blindspot：在相同数据上，Likert 评分（7 种统计方法）均无法检测到 pairwise comparison 可靠识别的 style bias（BT 63-84%, p < 0.001）。实验覆盖 2 个 target judges (GPT-4o, Qwen3-32B) + 1 个 negative control (Claude Sonnet 4)，3 个 benchmarks (LLMBar, AlpacaEval, MT-Bench)，3 个 style axes (formality, verbosity, register)。GEE 条件分解揭示 verbosity 为 clean style effect，formality/register 混淆 originality confound。

---

## Strengths

1. **统计方法论深度罕见**：7 种测量方法的 sensitivity hierarchy (Table 2)、GEE conditional decomposition (Table 3)、BT GoF diagnostics (Appendix G)、TOST equivalence testing (Appendix F) 在 NLP 评估论文中少见。两位 Reviewer 一致认可这是论文最大优势。

2. **Verbosity 轴提供了清晰的 confound-free 证据**：BT 76-77% ($p < 0.0001$)，GEE 确认 Originality OR non-significant，两个 judge 高度一致（OR 11.34 vs 13.10），且 Likert 完全无法检测（所有 $p > 0.17$）。这是 Likert Blindspot 的最干净论证。

3. **多层实验控制设计合理**：Position double-swap、NLI content gate（precision 98.9%）、consistency filter 三层控制，加上 cross-rewriter independence test (Appendix D) 和 cross-benchmark replication (Table 1)，实验设计的控制层次在同类论文中突出。

4. **Negative control 有独立方法论价值**：Claude Sonnet 4 在所有轴上未检测到 bias (BT ~56%, n.s.)，证明 CSD 不是在所有 judge 上产生假阳性，建立了 discriminant validity。

5. **对 RATE 的 head-to-head 比较公平且有洞察**：Section 5.2 在相同数据上直接比较 RATE 的 Likert ATE 与 CSD 的 pairwise comparison，揭示 RATE 的 metric 本身受 Blindspot 影响。

---

## Weaknesses

### Must-Fix（2 项，两位 Reviewer 共识）

**MF1** [R5-MF1] 遗漏关键矛盾文献：The Comparative Trap (Jeong et al., 2025, BlackboxNLP)
- Jeong et al. (2025) 系统性证明 pairwise comparison **放大** LLM evaluator 的 style bias（尤其 verbosity、authoritative tone），而非仅"检测"。
- 本文 Section 6 建议 "style bias audits should adopt pairwise comparison"，与该发现存在直接张力：pairwise 的更高检出率究竟是 **detection sensitivity**（本文主张）还是 **bias amplification**（Jeong et al. 主张）？
- 论文未讨论这一区分，也未论证 CSD 的 NLI gate + position control 是否能区分两种机制。
- 如果 amplification 解释成立，Likert 可能不是"blindspot"而是更接近真实 bias 幅度的测量；BT 63-77% 可能是 amplified signal。
- **两位 Reviewer 共识**：R2 首先识别，R1 交叉回应完全同意，认为是本轮最严重问题。

**MF2** [R5-MF2] NLI gate "approximates the do-operator" 声明过强
- Section 3.2 原文将 NLI gate 定位为 do-operator 近似，但 NLI filtering 是 post-hoc selection/conditioning，不是 intervention (Pearl, 2009)。
- Selection ≠ intervention：通过 NLI 筛选保留的样本可能在未观测维度上系统性不同（collider bias 风险）。
- 论文 Section 3.5 后半段有 caveat（"we do not claim...a complete structural causal model"），但主文叙事主调仍是 "interventional"，与 Limitations 的 "residual confounding is not fully eliminated" 矛盾。
- **两位 Reviewer 共识**：R1 识别，R2 完全同意。建议改为 "filtering-based confounder control"。

### Should-Fix（7 项）

**SF1** [R5-SF1] "first systematic quantitative verification" overclaim
- Abstract 和 Section 1 的 "first" claim 在 Jeong et al. (2025) 已做类似 systematic quantification 的情况下不成立。
- 需限定到 CSD 具体方法组合的 novelty（NLI gate + per-axis decomposition + position-controlled pairwise）。
- **R2 识别，R1 部分同意**。

**SF2** [R5-SF2] Evaluator-producer confound 主文缺 caveat
- Qwen3-32B 同时做 rewriter 和 judge，引入 self-preference bias 风险。Appendix D 的 cross-rewriter test 证明 rewriter identity 影响有限（Style OR 下降 22%），但无法排除 Qwen3-32B 作为 judge 偏好任何 LLM 产出。
- GPT-4o 结果不受此 confound 影响，但 Section 5.3 首次报告 Qwen3-32B 时无任何警示。
- **R1 识别（critical），R2 同意但建议降级（GPT-4o 是主 judge）。交叉后共识：should-fix**。

**SF3** [R5-SF3] "across three judges" framing 有误导性
- 实质仅 2 个 judge 展示 Blindspot，Claude 为 negative control。Abstract "across three judges" 可能给人 3 个 judge 都显示 bias 的印象。
- **R2 识别（critical），R1 反驳（方法论贡献 2+1 足够）。交叉后共识：should-fix**。修改措辞即可，不需新实验。

**SF4** [R5-SF4] GEE "confound-free" 措辞过强
- Table 3 和 Section 5.4 对 verbosity 使用 "confound-free"，但 GEE 仅控制已观测 confound（originality），无法排除未测量混淆（fluency、coherence 等）。
- 应改为 "no observed originality confound"。
- **两位 Reviewer 共识**。

**SF5** [R5-SF5] Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示
- Table 2 的 7 方法对比是核心方法论贡献，但仅在 formality 展示。如果 verbosity（更强轴）上也成立，论文核心论点大幅增强。
- 建议 Appendix 补 verbosity 的 7 方法表。
- **两位 Reviewer 共识**。

**SF6** [R5-SF6] Measurement attenuation vs. construct difference 主文呈现不平衡
- Limitations 承认 "Likert and pairwise modes measure different constructs" 是同等合理的替代解释，但主文 Introduction 到 Conclusion 一直以 "measurement attenuation"（Likert 失灵）为主调。
- Comparative Trap (MF1) 进一步加强了 construct difference 解释。
- 需在 Section 5.2 给两种解释同等篇幅。
- **两位 Reviewer 共识**。

**SF7** [R5-SF7] Formality/verbosity 在 Abstract 中未区分证据强度
- Abstract "three style axes" 未说明各轴证据强度不同。Verbosity = confound-free clean evidence；formality = conditional style effect with significant originality confound。
- 读者可能误以为三轴等价。
- **两位 Reviewer 共识**。

### Minor（5 项）

- **M1** [R5-M1] NLI 阈值 sensitivity sweep 仅 4 个离散点（0.70/0.80/0.90/0.95），不足以建立 plateau。建议 Appendix 补 10+ 点连续曲线。
- **M2** [R5-M2] Cross-rewriter independence test 缺 register 轴——register 是最弱轴，恰是 rewriter artifact 最可能影响结论之处。
- **M3** [R5-M3] Claude TOST "no bias" 措辞需改为 "failed to detect bias at current n"；Δ=15pp equivalence bound 缺 external justification。
- **M4** [R5-M4] Table 1 实验矩阵有空 cell 未解释原因。
- **M5** [R5-M5] Figure 2 DAG dashed/solid edges 黑白打印不清，建议颜色 + 线型双重编码。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：
- Comparative Trap 遗漏是本轮最严重问题 (MF1)
- NLI gate do-operator 声明需降级 (MF2)
- "first" claim 需限定范围 (SF1)
- GEE "confound-free" 过强 (SF4)
- Sensitivity hierarchy 需多轴验证 (SF5)
- Measurement attenuation vs. construct difference 不平衡 (SF6)
- Formality/verbosity 证据强度应在 Abstract 区分 (SF7)
- DAG 打印清晰度 (M5)

## Reviewer Divergence

| 问题 | R1 | R2 | 解决 |
|------|----|----|------|
| BT IIA 假设 | Critical (N2) | Rebut: 纯 paired comparison 无 IIA 问题 | R2 论证有力，降级为 minor（不列入正式 weakness） |
| Evaluator-producer severity | Critical (N3) | Should-fix (GPT-4o 不受影响) | 折中为 should-fix (SF2) |
| Judge 覆盖面 | Should-fix (措辞调整) | Critical (需加 judge) | 折中为 should-fix (SF3)，措辞调整而非新实验 |
| Overall 评分 | 3.5 Borderline Conf. | 3.0 Findings | 分歧源于 novelty 定义——R1 偏重方法执行质量，R2 偏重概念原创性 |

---

## Questions

1. Table 2 的 sensitivity hierarchy 在 verbosity 轴上是否成立？verbosity 的 Likert ATE 是否在 BT >70% 时也始终为 non-significant？
2. 如何区分 CSD 检测到的 bias 是 "detection sensitivity"（Likert 遗漏的真实 bias）还是 "bias amplification"（pairwise 放大的人工 bias）？NLI gate 能否在理论上阻断 amplification 机制？
3. n=355 时 Likert d→0 的证据是否在更大 n（bootstrap extrapolation 或模拟）下也收敛到 0？这对区分 attenuation 和 power gap 至关重要。
4. Qwen3-32B 作为 judge 时，是否有 self-preference 的直接证据（如在未经 style manipulation 的 pair 上是否偏好自身产出）？

---

## Missing References

1. **Jeong et al. (2025)** "The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators" (BlackboxNLP) — **必须引用**，与核心叙事直接矛盾
2. **Stureborg et al. (2024)** "Large Language Models are Inconsistent and Biased Evaluators" — LLM judge inconsistency 和 bias
3. **Park et al. (2024)** "Disentangling Length from Quality in Direct Assessments" — verbosity/length confound 相关

---

## External Review

外部审稿：未请求（项目未配置 paperreview.ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 warning / 3 info / 0 critical）：
- **[warning]** 连续 2 页纯文本无 display item，首个视觉锚点 (Figure 1) 延迟到第 3 页。建议将 Figure 1 或概念缩略图提前。
- **[warning]** 第 5 页三个 display items (Figure 2 + Table 1 + Figure 3) 挤在同一页，视觉密度过高。
- **[warning]** Display items 分布前松后紧——前 4 页仅 1 个 figure，第 5-8 页集中 6 个。建议重新平衡。
- **[info]** Figure 2 (DAG) 尺寸偏小，节点标签接近可读下限。
- **[info]** Figure 3 钻石标记偏小，axis labels 字号约 65-70% 正文，接近下限。
- **[info]** References 末页约 60% 填充，底部 ~40% 空白。

---

## Overall Assessment

**Overall**：3.5 / 5 — Borderline Conference
**Confidence**：4 / 5

**评分理由**：

论文的统计方法论深度（7 方法 hierarchy、GEE decomposition、BT diagnostics）在同类论文中突出，verbosity 轴提供了清晰且 confound-free 的 Likert Blindspot 证据。CSD 框架的多层控制设计合理，negative control 建立了 discriminant validity。

但论文存在两个结构性问题：
1. **核心叙事未与矛盾证据调和**：Comparative Trap (Jeong et al., 2025) 证明 pairwise 放大 style bias，论文未讨论 detection sensitivity 与 bias amplification 的区分。这直接影响 "adopt pairwise" 实践建议的可靠性。
2. **因果声明与证据强度不匹配**：NLI gate 的 do-operator 声明超出 filtering 操作的能力，主文"interventional"叙事与 Limitations 的 "residual confounding" 矛盾。

**Novelty 评估**：Likert Blindspot 本质是心理测量学已知现象（Thurstone 1927, Stevens 1946）在 LLM judge 领域的 domain transfer。论文诚实定位为 "first systematic quantitative verification"，但 Jeong et al. (2025) 的存在使 "first" claim 需进一步限定。增量贡献主要来自方法执行质量（per-axis decomposition + NLI gate + 7-method hierarchy），概念原创性有限。

**修改路径**：如果 MF1（Comparative Trap 讨论 + detection vs. amplification 区分）和 MF2（因果语言降级）得到充分解决，且 SF1-SF7 的 framing 调整到位，论文可达 **4.0 (Conference)**。当前状态为 Borderline Conference。

---

## Detailed Comments

### Section 1 (Introduction)
- "the first systematic quantitative verification" → 限定到具体方法组合
- "across three judges" → 明确 2 target + 1 negative control
- Contributions 列表应区分 verbosity (clean) vs. formality (confounded)

### Section 2 (Related Work)
- 必须增加 Comparative Trap (Jeong et al., 2025) 讨论
- 应增加 Stureborg et al. (2024) 和 Park et al. (2024)
- Bradley-Terry 段落可讨论 pairwise 的 amplification 风险

### Section 3 (Method)
- §3.2: "approximates the do-operator" → "provides a filtering-based confounder control"
- §3.5: 增加 selection bias 讨论，与 Limitations 的 "residual confounding" 保持一致
- DAG (Figure 2): 增加颜色编码辅助黑白打印

### Section 5 (Analysis)
- §5.2: 增加 construct difference 讨论段落，与 Comparative Trap 关联
- §5.3: Qwen3-32B 首次出现时加 evaluator-producer caveat
- §5.4/5.6: "confound-free" → "no observed originality confound"
- Table 1: 空 cell 加 footnote 说明
- Table 2: Appendix 补 verbosity 7-method 对比

### Section 6 (Conclusion)
- "style bias audits should adopt pairwise comparison" 需加限定条件
- 区分 verbosity (strongest evidence) vs. formality (conditional) vs. register (exploratory)

### Limitations
- Claude TOST: "no bias" → "failed to detect bias at current sample size"
- Equivalence bound Δ=15pp 加 justification

### Format
- "Blindspot" 大小写统一
- "style bias" vs "style preference" 区分使用