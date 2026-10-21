---
round: 1
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-21T07:32:21.911414+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 2 (Fresh Review)

**论文**: "Causal Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges"
**Venue**: EMNLP 2026 (ARR Long Paper)
**Reviewers**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 格式）
**审稿轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达成共识）

---

## Summary

本文提出 Causal Style Decomposition (CSD)，通过风格控制改写、NLI 内容保全门控和位置控制的成对比较来检测 LLM 评委的逐轴风格偏差。核心发现为 "Likert Blindspot"：标准 Likert 评分因 ~60% tie inflation 和信号衰减的双层结构限制，系统性地遗漏成对比较能检出的风格偏差。实验在 LLMBar (n=100) 上用 GPT-4o 和 Qwen3-32B 两个评委、三个风格轴（formality, verbosity, register）验证，七种统计方法一致确认该现象。

---

## Strengths

**S1. 统计论证扎实**（R1+R2 共识）：七种不同统计方法（BT model, sign test, t-test, binarized Likert, ordinal logistic, GEE, Wilcoxon）在同一数据上验证 Blindspot——所有成对方法达显著而所有 Likert 方法失败。Table 2 的 sensitivity hierarchy 是有力的系统性证据。

**S2. 多维度复现**（R1+R2 共识）：跨评委（GPT-4o vs Qwen3-32B）、跨风格轴（formality, verbosity, register）的复现设计。Verbosity 轴的 BT win probability 达 76-77%，效应量令人印象深刻且跨 judge 高度一致（OR = 11.34 vs 13.10）。

**S3. GEE 分解提供结构性洞察**（R1 高度评价）：GEE 逻辑回归将 style 和 originality 效应分解，揭示 per-axis confound structure 梯度（verbosity = pure style, formality = mixed, register = originality-dominated），为后续 debiasing 工作提供诊断基础。这一分析跨 judge 复现，是全新的经验发现。

**S4. Limitations 真实坦诚**（R1+R2 共识）：主动披露 quality-style confounding（OR = 2.32）、evaluator-producer bias、benchmark/axis 覆盖不足。

**S5. Position control + consistency filter 设计合理**（R1）：位置对调 + 一致性过滤 + BT 全数据 vs 过滤数据交叉验证（63.0% < 73.9%，排除 filter inflation）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W-MF1** [critical, 双 Reviewer 共识] **"Causal" 标题与方法实质不匹配**
标题 "Causal Style Decomposition" 暗示形式化因果推断，但 §3.5 明确声明 "we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions"。这不是一般的 qualification——是对因果方法论基本假设的全面放弃。两位 Reviewer 一致将此列为最突出的 framing 问题。建议改用 "Interventional Style Decomposition" 或 "Controlled Style Decomposition"；如果坚持 "Causal"，必须在 §3.5 提供明确的 identification assumptions（在什么条件下 NLI gate 实现了 do(S)）。
*（R1-N2 + R2-N2，交叉 [AGREE]）*

**W-MF2** [critical, 双 Reviewer 共识] **Holm-Bonferroni family 定义与实际实验矛盾**
§4.1 声称 "three judges × three style axes = nine tests"，但全文仅有 2 个 judge（GPT-4o, Qwen3-32B），Table 1 只有 6 行。第三个 judge 不存在。虽然 9-test 校正比 6-test 更保守（已显著结果不受影响），但声称的实验设计与实际执行不一致是严重 credibility 问题。可能是遗留了未执行的第三 judge 计划。必须修正为 "two judges × three style axes = six tests" 并重新检查 adjusted p-values。
*（R1-N1，R2 交叉 [AGREE]）*

**W-MF3** [critical, 双 Reviewer 共识] **单一 benchmark 代表性不足**
所有实验仅基于 LLMBar（n=100），NLI gate 后仅 88 pairs → 173 comparisons，bootstrap CI 宽度达 14.5pp。LLMBar 是 instruction-following 专用 benchmark。从单一小规模 benchmark 推广到 "LLM Judges" 全称论断缺乏 external validity。缺少：(a) Claude/Llama 系列评委；(b) 非 instruction-following 任务（summarization, translation）。建议至少在一个额外 benchmark 上复现核心发现，或在 title/abstract 中明确限定 scope。
*（R1-N3 + R2-W2，交叉升级为共识 Must-Fix）*

**W-MF4** [critical, R2 raised + R1 partial agree] **Abstract 过度声称**
Introduction 和 Abstract 中 "style bias is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference"：(a) 虽有三条文献引用支撑，但 Abstract 缺少 "recent work shows" 限定；(b) verbosity 本身是论文三个风格轴之一，说风格偏差 "far outweighs verbosity preference" 构成 category error——verbosity bias IS a style bias in the paper's own framework；(c) formality BT 63%，position bias 通常 55-65%，"far outweighing" 缺乏量级支撑。建议修改措辞。
*（R2-N1，R1 部分 [AGREE]——(b) 完全成立）*

**W-MF5** [critical, 视觉审查] **主正文超 8 页限制**
视觉审查确认：主正文（Abstract 至 Conclusion 末尾）溢出至第 9 页约 1/4 页。Section 6 Conclusion 从 p8 底部开始，延续到 p9 上半部分。EMNLP 2026 严格 8 页主正文限制，当前超限将直接导致 desk reject。需压缩正文或将部分内容移至 appendix。
*（视觉审查 critical finding）*

### Should-Fix（影响评分）

**W-SF1** [warning, 双 Reviewer 共识] **Evaluator-producer 三角色循环偏差**
Qwen3-32B 同时担任 rewriter、judge、NLI gate validator 三个角色。§5.1 称其为 "independent LLM annotator" 不准确（misleading）。Table 3 中 Qwen3-32B 的 formality OR (4.20) 和 originality OR (4.70) 系统性约为 GPT-4o（2.58, 2.32）的 2 倍，暗示 evaluator-producer bias 影响非 trivial。建议：(1) 删除 "independent"；(2) 明确论证仅 GPT-4o 数据是否足以支撑核心 claim；(3) 理想情况下用第三模型（不同 family）作为 rewriter 做控制实验。
*（R1-W1 + R2-W3，交叉 [AGREE]）*

**W-SF2** [warning, R1 raised + R2 agree with nuance] **Direction-aware NLI 削弱 verbosity 内容保全**
§3.2 对 verbosity 轴使用单向 NLI（仅 backward entailment），不阻止添加新 quality-relevant content。缓解因素：GEE 分解显示 verbosity originality component 不显著（OR=0.49, p=.096），且 text length 控制后 style OR 几乎不变（<2%），但 GEE "originality" operationalization 可能不捕获所有 quality dimensions。建议人工内容质量抽检。
*（R1-W2，R2 交叉 [AGREE] with nuance）*

**W-SF3** [warning, R2 raised + R1 agree] **Scale granularity 未探讨**
论文使用 1-10 Likert scale。关键问题：Blindspot 是所有 ordinal scale 的固有属性还是 1-10 特定粒度结果？如果 1-100 或 continuous scale 也有 Blindspot，那是对 Likert 范式的根本批评；如果更细粒度可缓解，则是 scale 选择问题。Table 2 ordinal regression 排除了 interval-scale 假设但不排除 granularity 影响。建议至少在 Limitations 或 Discussion 中讨论。
*（R2-W4，R1 交叉 [AGREE]——"此前遗漏的有效问题"）*

**W-SF4** [warning, R2 raised + R1 partial rebut] **缺乏 mitigation 策略**
论文诊断出 Blindspot 但仅建议 "adopt pairwise comparison"，未讨论 O(n²) scalability 或任何 calibration/debiasing 方案。R1 认为 diagnostic framework 定位合理，不必同时提出 debiasing solution，但建议简要讨论 active sampling 等 O(n log n) 方案。
*（R2-W5，R1 部分 [REBUT]——severity 有分歧但方向一致）*

**W-SF5** [warning, R1 raised + R2 agree] **BT 正则化细节和 bootstrap resamples 不一致**
§5.2 "regularized estimate" 未说明正则化类型（Bayesian prior? L2? pseudocount?）和超参数。GPT-4o 用 2,000 resamples，Qwen3-32B 用 10,000，无解释。影响 reproducibility。
*（R1-W4，R2 交叉 [AGREE]）*

**W-SF6** [warning, R1 raised + R2 agree] **DAG 遗漏关键路径**
Figure 2 缺少：(a) Position bias P → Y（虽被 position swap 控制，但应在 DAG 中表示为 conditioned out）；(b) Rewrite artifact R → Y（judge 检测到 text 是 LLM 改写的这一事实本身影响评分——与 evaluator-producer confound 直接相关）。更完整的 DAG 会加强 §3.5 的 identification argument。
*（R1-W6，R2 交叉 [AGREE]）*

### Minor

**W-M1** Figure 4 (power_curve) 疑似存在淡色 PLACEHOLDER 水印，提交前需确认并移除。
**W-M2** Table 1 Qwen3-32B Register 行缺少 Cohen's d 值，格式与其他行不一致。
**W-M3** 引用问题：wang2026fairjudge 第一作者 mismatch（bib: Wang, OpenAlex: Yang）；murugadoss2025sos 在 OpenAlex 未找到。
**W-M4** 无代码/数据可用性声明（ARR 鼓励但不要求）。

---

## Reviewer Consensus

**[AGREE] 强共识（两位 Reviewer 一致）：**
1. "Causal" framing overclaim 是最突出的 framing 问题
2. Holm-Bonferroni "9 tests" 是事实性错误（声称 3 judges，实际 2）
3. 单一 benchmark + 小样本不支持全称论断
4. Evaluator-producer 三角色循环偏差需更好处理
5. Scale granularity 是有效的未讨论问题
6. BT 正则化和 bootstrap 细节不一致
7. DAG 缺少 position bias 和 rewrite artifact 路径

---

## Reviewer Divergence

**Excitement/Novelty 评估（核心分歧，未收敛）：**
- R1 (Excitement 3.5/5)：GEE decomposition 揭示的 per-axis confound structure 梯度是全新发现，7 种统计方法的 quantitative demonstration 对 LLM 评估社区有实际价值，两层机制的具体识别此前未有
- R2 (Excitement 2.5/5)：Likert Blindspot 是心理测量学经典现象（ordinal discretization 损失连续信号）在 LLM judge 领域的迁移应用，CSD 是三个已有组件的流水线（LLM 改写 + NLI filter + BT comparison），methodological novelty 有限

**GEE correlation structure（已解决）：**
R1 建议测试 AR(1) 或 unstructured。R2 有效 REBUT：对 cluster size = 2 的设计，exchangeable/AR(1)/unstructured 在数学上等价（仅一个 off-diagonal 参数），测试 AR(1) 不提供额外信息。Appendix B 的 exchangeable vs independence 对比已充分。**本报告采纳 R2 的 rebuttal，不将此列为 weakness。**

**Mitigation 策略的 severity（轻微分歧）：**
R2 列为 Should-Fix，R1 认为 diagnostic framework 定位合理，不必同时提出 solution。本报告保留为 Should-Fix 但优先级低于其他 Should-Fix。

---

## Questions for Authors

1. §4.1 中 "three judges" 指哪三个？如果第三个 judge 未执行，Holm-Bonferroni family size 应为多少？
2. NLI gate validation（§5.1）为什么不用 GPT-4o 或人工标注替代同为 Qwen3 family 的模型？
3. Verbose rewrites 是否经过人工 content quality 检查？单向 NLI 是否足以排除 quality-relevant additions？
4. BT 正则化具体设置（类型和超参数）？Bootstrap resamples 数为何不一致（2,000 vs 10,000）？
5. 如果将 Likert scale 改为 1-100 或连续滑块，Blindspot 是否仍然存在？
6. CSD 是否在 non-instruction-following 任务（summarization, translation quality）上测试过？
7. 是否计划发布代码和数据？

---

## Missing References

两位 Reviewer 共同推荐补充以下引用：
1. **Chiang et al. (2024)** "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference" — BT model 在 LLM 评估中的 canonical reference（R1+R2 共识）
2. **Ye et al. (2024)** "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge" — 系统量化 LLM judge 多种 bias 的直接竞品文献（R1 提出，R2 同意）
3. **Feder et al. (2022, TACL)** "Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond" — 若保留 "Causal" 标题则需要此方法论综述（R2 提出，R1 同意）
4. **LLM-as-judge survey** — 帮助定位 CSD 在更广阔研究图景中的位置（R2 提出）

R2 另推荐 Oriyad &amp; Rohban (2025) "The Silent Judge" (NeurIPS 2025)，但 R1 交叉回应中未能在 OpenAlex/Semantic Scholar 确认存在，建议验证后再决定。

---

## External Review (Stanford Agentic Reviewer)

**状态：已跳过**（用户选择不提交外部审稿）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成（耗时 ~3.5 分钟）。关键发现：

**[CRITICAL]** 主正文（Abstract 至 Conclusion 末尾）溢出至第 9 页约 0.25 页。EMNLP 2026 严格 8 页正文限制，当前超限将导致 desk reject。

**[WARNING]**
- 连续 3 页（p.1-3）纯文本无任何 display item，第一个视觉锚点到 p4 才出现。建议将 Figure 1（pipeline）或 Figure 2（DAG）提前至 p2。
- 第 5 页堆叠 3 个 display item（Figure 2 + Table 1 + Figure 3），与前 3 页文本荒漠形成强烈反差。
- Figure 2（causal DAG）尺寸偏小，打印尺寸下标签可能难以辨认。

**[INFO]** Figure 3 填充/空心菱形在小尺寸下区分不明显（建议双重编码）；Figure 1 caption 过简；整体灰度方案打印友好但视觉吸引力偏低；表格排版（booktabs）专业；Section 6 heading 出现在页底有轻微孤悬感。

---

## Overall Assessment

**Overall: 3.0 (Findings)**
**Confidence: 4/5**

### 维度合成

| 维度 | R1 | R2 | 合成 |
|------|----|----|------|
| Soundness | 3.0/5 | 3.5/5 | 3.0/5 |
| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |
| Reproducibility | 3.0/5 | 4.0/5 | 3.5/5 |
| Overall | 3.0 | 3.0 | **3.0** |

### 评分理由

论文的核心贡献——七种统计方法系统性证明 Likert 评分在 LLM judge 风格偏差检测中失灵——有明确的实践价值和方法论教育意义。GEE per-axis confound structure 梯度是有洞察力的经验发现。但以下结构性问题阻止主会议接收：

1. **Framing 问题**："Causal" 标题与 §3.5 全面 disclaimer 的张力是最突出的 credibility 问题
2. **External validity 不足**：单一 benchmark（LLMBar, n=100）+ 2 个 judge 的证据基础不支持 "LLM Judges" 全称论断
3. **事实性错误**：Holm-Bonferroni 声称 "three judges × three style axes = nine tests"，第三个 judge 不存在
4. **页数超限**：主正文超出 8 页限制约 0.25 页，按 ARR 规定将 desk reject
5. **Novelty 争议**：Blindspot 是心理测量学已知现象的 domain transfer（R2 view）vs. quantification + GEE decomposition 有独立贡献（R1 view）

论文达到 Findings 级别——有实践价值的经验性发现，统计执行扎实。距离 Main Conference 需要：(a) 更广的 benchmark/judge 覆盖，(b) 解决 Causal framing 问题，(c) 修正页数和事实性错误。建议修改后投入下一 ARR 周期。

---

## Detailed Comments

### §1 Introduction
- "Recent work has converged on a striking finding" 后的三条引用支撑 "dominant source" claim，但 Abstract 缺少限定词。
- Contributions 第 2 条 "four judge×axis configurations at p < 0.001" 与 Table 1 一致（4 strong + 2 exploratory）。

### §3 Method
- §3.2 Direction-aware NLI for verbosity 的 justification 合理但应更显式讨论 quality-relevant additions 的 tradeoff。
- §3.5 "Interventional rather than formal causal evidence" 的 disclaimer 诚实但与标题矛盾。DAG 应加入 position bias（conditioned out）和 rewrite artifact 路径。

### §4 Experiments
- §4.1 "three judges × three style axes = nine tests" 是事实性错误，应为 "two judges × three style axes = six tests"。
- Table 1 Qwen3-32B Register 行应补充 Cohen's d 值。

### §5 Analysis
- §5.1 "independent LLM annotator" 描述 Qwen3-32B 不准确，应删除 "independent"。
- §5.2 BT "regularized estimate" 需说明正则化类型和超参数。Bootstrap resamples 数应统一或解释差异（2,000 vs 10,000）。

### §6 Conclusion
- 最后一段溢出至第 9 页。建议压缩 Conclusion 或将部分 Analysis 内容（如 §5.6 consistency filter）移至 Appendix。

### Appendix B
- Table 4 QIC 列仅报告 "---"（差异），未报告实际值。虽不影响结论但影响独立验证。

### 视觉布局
- 前 3 页纯文本无 display item → 建议将 Figure 1/2 提前至 p2。
- p5 堆叠 3 个 display item → 分散分布。
- Figure 2 (DAG) 偏小 → 放大或用 figure*。

---

## Issue Tracker 同步

已更新 `review_issues.yaml`。本轮共识问题（5 critical + 7 warning + 4 info）：
- **Reopened**: R1-N1（Causal framing，Round 1 resolved 但标题未改）
- **Still open**: R2-N1（Novelty ceiling）
- **New critical**: RD2-MF2（Holm-Bonferroni 错误）、RD2-MF3（单一 benchmark）、RD2-MF4（Abstract overclaim）、RD2-VIS（页数超限）
- **New warning**: RD2-SF1—SF7（evaluator-producer、NLI verbosity、scale granularity、mitigation、BT details、DAG paths、novelty divergence）、RD2-M1（Figure PLACEHOLDER）、RD2-REF（missing references）
- **New info**: RD2-M2—M4（Table formatting、citation mismatch、no code/data statement）
- Round 1 已 resolved 的 14 个 issue 中，除 R1-N1 外均未被 Round 2 Reviewer 再次提及