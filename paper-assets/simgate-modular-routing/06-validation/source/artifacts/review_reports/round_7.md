---
round: 7
overall_score: borderline reject
timestamp: 2026-05-15T15:33:40.349749+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 7 (Fresh Review)

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Reviewers**: R1 (方法严谨性+实验充分性), R2 (新颖性+完整性+相关工作)
**轮次**: Round 7 (Fresh review, 1 round + cross-sharing, converged)

---

## Summary

本文提出 episode-level counterfactual analysis 方法，在 ScienceWorld 环境中比较 pure-internal (ReAct) 和 pure-deterministic 策略的 episode outcomes，发现 death avoidance 占据约 90% 的 routing signal（DAF=90.41% at P=100），78.9% 的 non-tie routing labels 由 death asymmetry 驱动。跨环境验证（MATH N=300）显示无 death penalty 时 routing signal 消失/反转。训练的 router 仅达 57-59% balanced accuracy，作者解读为 learnable signal 稀薄。

---

## Strengths

**[S1] 研究问题定位精准** [R1, R2 共识]
"What drives routing signal" 是 modular agent 设计中被忽视的先验问题。在大量工作关注 "how to route" 的背景下，本文追问 "why routing helps" 具有独立价值。

**[S2] 统计分析严谨且透明** [R1, R2 共识]
Bootstrap CI、LOO analysis、Spearman rank correlation、seed robustness、penalty sensitivity analysis 全面覆盖。主动披露 r=0.97 的结构性耦合（§4.1），展现学术诚实度。

**[S3] MATH 实验提供有效 negative control** [R1, R2 共识]
N=300 的 MATH 评估在无 death penalty 环境下显示 routing signal 消失/反转（label distribution 86:9 → 30:17），有效支撑 death avoidance 是 ScienceWorld routing signal 的核心驱动力。

**[S4] Limitations section 异常坦诚详尽** [R1, R2 共识]
主动承认单环境单模型局限、penalty sensitivity、step-level mislabeling、capability dependence 等问题。

**[S5] 写作质量高** [R1, R2 共识]
Story arc 清晰（问题→step-level degeneracy→episode-level method→finding→cross-validation），结构紧凑，语言精准。

**[S6] 当代相关工作覆盖出色** [R1]
引用多篇 2026 concurrent work（tool-overuse-illusion、when2tool、tool-use-tax、to-call-or-not），展现对领域最新进展的把握。

---

## Weaknesses

### Must-Fix (4 items)

**[MF1] ALFWorld 数据来源与方法论完全缺失** [R1-N1, R2-W5; 共识: AGREE]
Table 3 呈现 ALFWorld 数据（N=135），但论文未描述：使用什么模型、deterministic modality 具体定义、episode 长度、labeling 是否沿用 Algorithm 1。脚注关于 "capability gap" 的判断也缺乏支撑。不可追溯的数据严重削弱跨环境验证可信度。
→ **Action**: 补充完整方法论描述，或移至 Appendix 并降低论证权重。

**[MF2] Router 训练诊断结论与数据量不足存在根本性混淆** [R1-N2; R2 交叉回应 AGREE]
Router balanced accuracy 57-59% 被解读为 "thin learnable signal"（Contribution 4）。但训练集仅 81 样本（internal-preferred ~8 个），验证集 14 个。在此规模下，低准确率可能反映数据不足而非信号稀薄。Classification head 0% internal recall 在 ~8 正例下是预期行为，不构成独立证据。
→ **Action**: 明确承认数据量混淆变量，将 Contribution 4 降级为初步观察，或提供数据量消融实验。

**[MF3] 63% task types 排除构成严重选择偏差** [R1-N3, R2-N2; 共识: AGREE]
19/30 task types 因 30-step timeout 排除。被排除的长 horizon 任务可能具有不同的 routing signal 构成（如更多非 death 信号）。标题 "Dominant Routing Signal" 和 abstract "~90%" 的 headline 未充分限定适用范围。
→ **Action**: 标题/Abstract/Conclusion 增加 scope qualifier；分析被排除任务的特征；讨论 step budget 增加的潜在影响。

**[MF4] DAF "~90%" headline 过度依赖 P=100 特定设置** [R2-N1, R1-W4; 共识: AGREE, R2 主张 Must-Fix]
DAF 随 P 单调递增是数学必然。P=10→46.4%, P=25→68.4%, P=100→89.6%, P=200→94.5%。论文标题和 abstract 以 "~90%" 为 headline 完全锚定于 P=100。Penalty-independent 的 78.9% death-asymmetry label fraction 应提升为 primary metric。
注：此问题在前轮审稿（R6-C1）中已标记为 resolved，但当前论文 abstract 仍以 DAF=90.41% 领衔，78.9% 仅作为补充指标出现，未达到 "co-equal" 标准。
→ **Action**: Abstract/Title 中 78.9% 与 DAF 并列或优先呈现；明确标注 DAF 的 penalty-dependent 本质。

### Should-Fix (7 items)

**[SF1] MATH p=0.079 的不对称使用** [R1-W1; R2 AGREE]
Abstract/Conclusion 呈现 label distribution inversion 比正文更强势，但 p=0.079 未达显著性。"routing signal vanishes" 的措辞过强。
→ **Action**: 统一在所有出现处标注 "not statistically significant"。

**[SF2] Llama pilot (N=10) 作为 contribution 过度包装** [R1-W2, R2-W2; 共识: AGREE]
10 episodes 几乎无统计功效，不应与 MATH (N=300) 并列为 Contribution 3 "Cross-context validation"。
→ **Action**: 从 Contribution list 移除，仅在正文保留为方向性观察。

**[SF3] Pure-strategy → mixed-strategy gap 未分析** [R1-W3; R2 交叉回应 AGREE]
标注基于 pure-strategy trajectory，但实际部署是 mixed routing。Death 在 pure-internal 全程下发生不等于在 mixed routing 中也会发生。DAgger citation 不够——需要 death timing 分析以评估 mixed routing 可行性。
→ **Action**: 分析 death 发生时间步，讨论 mixed routing 下 death rate 的预期变化。

**[SF4] r=0.97 结构性耦合在 Abstract/Contributions 中披露不足** [R1-W5; R2 AGREE]
Δ_full ≈ δ·P + Δ_nd 且 δ·P 占 ~90% 时，δ 与 Δ_full 的高相关部分是数学同义反复。§4.1 有 caveat 但 Abstract/Contributions 未携带。
→ **Action**: Abstract 中加结构性耦合限定语，或削弱 r=0.97 的呈现权重。

**[SF5] Safe RL 文献覆盖不足** [R2-N3 raised as critical; R1 REBUT to should-fix; Director 裁定 should-fix]
核心 insight 是 "router = safety critic"（§5 Discussion），但仅引 Garcia 2015 一篇 11 年前的综述。论文贡献是分析性非算法性的，但应补充 1-2 篇代表性 safety critic 工作。
→ **Action**: 补充 CPO 或 safety Q-function 等 2020+ 代表性工作。

**[SF6] 仅测试 ReAct，未讨论其他推理策略的影响** [R2-W4; R1 AGREE]
Reflexion 的 self-correction 或 ToT 的 backtracking 可能显著降低 death rate → 降低 DAF。论文发现可能是 ReAct single-pass vulnerability 的特性而非通用结论。Limitations 讨论了 model scale 影响但未讨论 reasoning strategy 影响。
→ **Action**: Limitations 增加 reasoning strategy 泛化讨论。

**[SF7] 缺少重要引用** [R2-W3; R1 部分 AGREE]
RouteLLM (Ong et al., 2024)——直接做 routing，最为紧迫；Reflexion (Shinn et al., 2023)——与 ReAct 替代策略相关；tool-learning survey (Qu et al., 2024)。
→ **Action**: 补充上述引用至 Related Work。

### Minor (6 items)

- **[m1]** `retool-2026` bib key 与实际出版年份 2025 不一致 [R1, R2]
- **[m2]** `dynathink-2025` first author 信息可能有误 [R1, R2]
- **[m3]** Abstract 中 "90.41%" 精度暗示过高确信度，建议改为 "~90%" [R2-M5; R1 AGREE]
- **[m4]** Ethics 提及 "RTX 5090" 存在轻微去匿名化风险，建议泛化为 "consumer GPUs" [R2-M6]
- **[m5]** `find-non-living-thing` 给了 40 episodes 而其他 task types 给 20，未解释原因 [R1]
- **[m6]** 未提及代码/数据开源计划 [R1]

---

## Reviewer Consensus [AGREE]

以下问题由两位 Reviewer 独立提出并在交叉回应中确认共识：
1. **ALFWorld 数据来源缺失** (MF1) — 两位均列为 critical
2. **63% task types 排除的选择偏差** (MF3) — 两位均列为 critical
3. **DAF penalty-sensitivity → 78.9% 应为 primary metric** (MF4)
4. **Llama pilot N=10 过小** (SF2)
5. **r=0.97 结构性耦合披露不足** (SF4)
6. **Bib 细节问题** (m1, m2)

## Reviewer Divergence

**[DAF 严重性等级]** R2 列 DAF penalty-sensitivity 为 Must-Fix，R1 列为 Should-Fix。**Director 裁定**：提升为 Must-Fix——标题含 "Dominant" 一词，headline metric 的 penalty-dependence 直接影响论文核心声明的可信度。

**[Safe RL 文献]** R2 列为 Must-Fix (critical)，R1 REBUT 为 Should-Fix——论文贡献是分析性的，非算法性的。**Director 裁定**：降为 Should-Fix——R1 的论证更有说服力，"router = safety critic" 是 Discussion implication 而非 primary contribution。

---

## Questions for Authors

1. ALFWorld 实验的完整方法论——模型、deterministic modality 定义、labeling 流程？
2. 如果使用 Reflexion 或 ToT 替代 ReAct，预期 death rate 和 DAF 会如何变化？
3. Router 低准确率（57-59%）在数据量增加 5-10 倍后是否会改善？是否考虑过合成数据扩增？
4. 被排除的 19 个 task types 有哪些共同特征？增加 step budget 到 50 或 100 步是否可行？
5. Death 事件通常发生在 episode 的哪个时间步？这对 mixed routing 策略有什么启示？

## Missing References

1. **RouteLLM** (Ong et al., 2024) — 直接做 LLM routing，高度相关
2. **Reflexion** (Shinn et al., 2023) — LLM agent self-correction，与 death avoidance 机制相关
3. **Tool-learning survey** (Qu et al., 2024) — 综述性引用
4. **CPO / Safety critics** (2020+) — 支撑 "router as safety critic" 论述
5. ScienceWorld follow-up works（如有）

## External Review (Stanford Agentic Reviewer)

外部审稿未配置，无外部审稿结果。

---

## Overall Assessment

**评分：Borderline Reject（偏向 Findings track）**
**置信度：High (4/5)**

两位 Reviewer 独立给出 3/5（Borderline/Findings level）且交叉回应后维持评分。

**核心判断**：论文提出了一个有价值的研究问题（"what drives routing signal"），提供了方法论工具（episode-level counterfactual + DAF），并在 ScienceWorld 上给出了令人信服的经验发现。统计分析扎实，写作质量高。

**但存在四个 Must-Fix 问题**阻碍 main conference 接收：
1. ALFWorld 数据不可追溯（MF1）
2. Router 诊断结论与数据量不足无法区分（MF2）
3. 63% task types 排除的选择偏差未充分限定（MF3）
4. DAF headline 过度依赖 P=100（MF4）

**与前轮比较**：R6 标记为 resolved 的 4 个 issue（R6-C1 DAF penalty-dependence、R6-W1 r=0.97 overclaim、R6-W2 prescreening exclusion、R6-W8 Safe RL literature）在 fresh review 中重新浮现，说明前轮修复未达到预期效果或有回退。新增 2 个 critical issue（ALFWorld 方法论缺失、Router diagnostic confound）。

**建议**：修复 4 个 Must-Fix 问题后适合 EMNLP 2026 Findings track。冲 main conference 需额外扩展实验范围（更多 task types、更多推理策略、更多模型）。

---

## Detailed Comments by Section

### §1 Introduction
- Story arc 清晰，但 "death avoidance accounts for approximately 90%" 应在首次出现时即标注 "at P=100"
- Contribution 3 应移除 Llama pilot，仅保留 MATH
- Contribution 4 需加 data-size caveat

### §2 Method
- Problem Setup (§2.1) 形式化清晰
- Counterfactual collection (§2.2) 设计合理，97.4% tie rate 论证充分
- Algorithm 1 清晰直观
- DAF metric (§2.4) 数学定义合理，penalty sensitivity analysis (Appendix E) 充分

### §3 Experiments
- §3.1 Death decomposition 分析扎实（r=0.97 + LOO + bootstrap）
- §3.2 Baselines 完整（always-int/det/random/oracle），oracle degeneracy 有说服力
- §3.3 Router diagnostic 有方法论价值但 Contribution 4 claim 过强
- §3.4 Cross-model (N=10) 过小，应降级

### §4 Related Work
- Tool-use 和 adaptive computation 覆盖充分
- 缺 RouteLLM、Reflexion
- Safe RL 需补 1-2 篇 2020+ 工作
- Counterfactual RL 段落（Olson/Gajcin/Amitai）已有，定位清晰

### §5 Discussion
- MATH negative control 有效但 p=0.079 需统一标注
- ALFWorld 数据缺方法论（最严重问题）
- "Router as safety critic" 论述有洞察力但文献支撑不足
- Penalty sensitivity 和 capability dependence 讨论到位

### §6 Conclusion
- 与 Introduction 呼应良好
- 需同步所有 scope qualifiers 和 metric 调整

### Limitations
- 异常详尽坦诚（这是本文的一个突出优点）
- 需增加 reasoning strategy generalization 讨论（Reflexion/ToT 对 death rate 的潜在影响）

### Appendices
- 统计附录（B, C, D, E, F）质量高
- Labeling quality audit (A) 有效回应 oracle circularity concern

---

## Issue Tracker 同步状态

已更新 `review_issues.yaml`：
- 4 个前轮 resolved issue 重开（R6-C1, R6-W1, R6-W2, R6-W8）
- 3 个新 critical issue（R7-N1 ALFWorld, R7-N2 Router confound）
- 5 个新 warning issue（R7-W1 至 R7-W5）
- 3 个新 info issue（R7-m1 至 R7-m3）
- 总计 14 个 open issues（4 critical, 7 warning, 3 info）