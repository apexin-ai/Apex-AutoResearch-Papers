---
round: 16
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T03:17:26.341997+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 18 审稿报告 — exec-sim-repair-verifier

**论文**: "A Systematic Comparison of Execution-Free Verification Formulations for Code Repair"
**Venue**: EMNLP 2026 via ACL Rolling Review
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性; R2: 新颖性/完整性）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛，无需 Round 2）

---

## Summary

本文首次在匹配条件下系统比较三种 execution-free code repair verification formulations（CLS 分类、CWM 生成、TRAJ 轨迹级评分），使用两个代码 LLM 家族（Qwen3, DeepSeek-Coder）、两个复杂度层级（function-level, repo-level）和多个训练种子。核心发现为 complexity-moderated formulation choice：function-level 三种 formulation 近等价（CLS-CWM TOST p=0.007），repo-level 在 ≤8B LoRA 条件下 CLS 显著优于 CWM（18-26pp gap），伴随 format collapse failure mode。论文的统计方法论（TOST + clustered bootstrap + Bayesian ROPE + mixed-effects LPM + Holm-Bonferroni）在同类实证论文中属上乘。

---

## Strengths

**S1. 匹配实验框架设计良好。** 三种 formulation 在同一 LoRA 配置、同一基座模型、同一数据集上训练，控制了 model capacity、optimizer、data 等变量。跨两个模型家族和两个复杂度层级的设计增强了结论的外部效度。[共识]

**S2. 统计方法论在同类论文中属上乘。** TOST 等价性检验 + clustered bootstrap + Bayesian ROPE + Holm-Bonferroni 多重比较校正 + mixed-effects LPM，形成完整推断链。TOST margin sensitivity analysis（±1.52pp 最小等价边界）比仅报 p-value 更有信息量。§3.1 已声明统计层次（primary vs robustness check）。[共识]

**S3. Failure mode taxonomy 有实践指导价值。** Table 4 的三种 failure mode（format collapse, decision collapse, aggregation penalty）来自 per-mutation 和 repo-level 错误分析，为从业者选择 formulation 提供了可操作的诊断标准。[共识]

**S4. 写作密度高效、局限性诚实。** Abstract ~172 词（≤200 限制），正文 8 页，信息密度高。§3.7 Threats to Validity 主动识别 5 个潜在混淆。Limitations 坦承 seed 数量不足和 Python-only 限制。14B 结果诚实标注 "Preliminary"。[共识]

**S5. Matched-context ablation 有效排除输入长度混淆。** CLS@2048 仅损失 1.44pp（gap 保留 98%），确认 repo-level gap 来自 output 而非 input 差异。[R1 提出, R2 隐含同意]

---

## Weaknesses

### Must-Fix（影响接收决定）

*本轮无 Must-Fix 共识。R1 的两个 Must-Fix 项在交叉讨论后被 R2 部分反驳或降级。Director 裁定如下：*

### Should-Fix（影响评分但不一票否决）

**SF1. [Should-Fix] CWM constrained decoding 未测试，但 Appendix (c) 间接证据应提升到正文。**
- R1 标 Must-Fix，R2 REBUT 降为 Should-Fix。
- 论文测试了 4 种干预（rank 扩展、relaxed matching、model scaling、majority voting）均失败，但未测试 constrained decoding——最直接针对 format collapse 的工程手段。
- **R2 反驳的关键证据**：Appendix (c) 报告了 CWM 误训 CLS-format 数据后达 86.05% accuracy + 0% unparseable（等价于完美 constrained decoding）——这仅恢复到 CLS 水平，说明 format compliance ≠ semantic accuracy 提升。同时 parseable CWM 准确率仅 38-43%，远低于 72.96% majority baseline——即使 constrained decoding 消除 format collapse，语义准确率仍不足。
- **Director 裁定**：间接证据充分，降为 Should-Fix。但这些关键证据埋在 Appendix 中，正文可见度不足。**建议将 Appendix (c) 的两项证据（误训实验 + parseable-only accuracy）提升到 §3.5 或 §3.6 正文，并增加 constrained decoding 相关引用（Willard & Louf 2023; Synchromesh）。**

**SF2. [Should-Fix] TRAJ 训练配置差异过大，CLS-TRAJ 比较属 observational 而非 controlled。**
- R1 标 Must-Fix，R2 部分同意但降为 Should-Fix。
- 差异：~100× 数据量、4× 学习率、不同标签粒度。论文框架为 "inherent to the formulation"，但这使得 CLS-TRAJ 等价性可能来自过拟合而非 formulation 等价。
- **缓解因素**：(1) downsample ablation 控制了数据量（CLS 80.74% vs TRAJ 72.92%）；(2) function-level 近等价证明 formulation 本身可行；(3) Abstract 已标注 "inherently confounded"。
- **Director 裁定**：降为 Should-Fix。论文已有 caveats 但可更明确。**建议 §3.4 结论中加入 caveat：CLS-TRAJ equivalence holds under their respective optimal training recipes, but the recipes differ substantially。**

**SF3. [Should-Fix] Repo-level 仅 2-3 seeds，点估计 (18-26pp) 精度高于 CI 支撑范围。**
- 两位 Reviewer 共识。
- Variant-level bootstrap HDI 宽度 ~25pp（Table 14），远大于 function-level ~2pp。§3.5 已标注 "exploratory"。
- **建议 Abstract 中补充 CI 信息或弱化精度表述。**

**SF4. [Should-Fix] GenRM domain contrast 是最有 novelty 潜力的发现，但严重低估。**
- 两位 Reviewer 强烈共识。
- Generative verification（CWM）在 code 中不优于 discriminative（CLS），与 math reasoning 中 GenRM 的结论相反。这一 domain-specific 发现可能是论文最有影响力的贡献，但仅 Conclusion 一句话带过。
- **建议在 §4 Related Work 或 §5 Conclusion 中增加一小段讨论，分析 code domain 差异的可能机制（exact match 严格性、output space 结构化程度等）。**

**SF5. [Should-Fix] Error complementarity overclaim：oracle 90.63% 但 heuristic <0.4pp。**
- 两位 Reviewer 共识。
- Oracle-to-achievable gap 过大，"suggesting a learned router is needed (Appendix A)" 但 Appendix A 未实验 learned routing。论文 §1 已将 complementarity 合并为 Contribution #1 子句（R17 修复），但正文 §3.6 和 Conclusion 表述仍偏乐观。
- **建议弱化 routing 方向的表述或增加 "the large oracle-to-achievable gap suggests this may not be practically exploitable with current methods" 的 caveat。**

**SF6. [Should-Fix] Abstract 中 "all three formulations achieve comparable accuracy" 表述过强。**
- R1 交叉回应中明确提出，R2-W1 亦提及。
- CLS-TRAJ 在 Holm-Bonferroni 校正后 inconclusive（p_adj=0.075），Abstract 不应声称 "all three comparable"。
- **建议改为 "CLS and CWM achieve statistical equivalence; TRAJ equivalence is inconclusive after multiple comparison correction at current power (~0.3)"——与论文 §3.4 表述一致。**

**SF7. [Should-Fix] Re-repair 实验数字不一致（n=44 vs n=14）且结论过强。**
- R1-W3 提出。Appendix I(j) 报告 n=44 instances 但后文出现 n=14。Power ~0.3 不支撑 "does not translate" 的结论。
- **建议澄清 n 值关系并弱化结论。**

### Minor（不影响接收）

**M1.** CWM exact string matching 未讨论 near-match 敏感性（如浮点数差异）。§2.1 footnote 2 引用了 CWM 原文协议但未展开。[R1-M3]

**M2.** Figure 2 y-axis 截断（~80% 起始）可能夸大视觉差异。Caption 已标注 "y-axis does not start at zero"。[R1-M2, 已有 disclosure]

**M3.** Table 4 caption 过于简短。[R2-M3]

**M4.** Constrained decoding 相关文献（Synchromesh / Poesia et al. 2022; XGrammar）应在正文或 Limitations 中引用。Appendix (c) 已引用 Willard & Louf 2023。[R1+R2 missing refs]

**M5.** Abstract "(~0.3)" 指 TOST power 但缺乏上下文解释。[R2-M1]

---

## Reviewer Consensus [AGREE]

1. **统计方法论出色**——TOST + clustered bootstrap + Bayesian ROPE + LPM + Holm-Bonferroni 在同类论文中属上乘。
2. **Failure mode taxonomy 有实践价值**——三种 failure mode 的识别为从业者提供可操作诊断。
3. **CWM format collapse 讨论需要更多工程干预证据**——constrained decoding 未测试是明确的 gap，但 Appendix (c) 间接证据已部分缓解。
4. **TRAJ 比较本质上是 observational**——训练配置差异使 formulation-level attribution 打折扣。
5. **GenRM domain contrast 被严重低估**——generative ≠ better for code 是最有影响力的发现之一。
6. **Error complementarity 实际可操作性不足**——oracle gap 大但 achievable gain 接近零。
7. **Repo-level seed 覆盖不足**——2-3 seeds 的 CI 过宽，点估计精度高于数据支撑。
8. **Abstract TRAJ 表述过强**——应区分 confirmed（CLS-CWM）和 inconclusive（CLS-TRAJ）。

## Reviewer Divergence [REBUT]

1. **Overall 评分分歧（R1: 3.5 vs R2: 3.0）**——核心在于 empirical comparison paper 的 novelty 标准。R1 认为 rigorous methodology + actionable insights 足以支撑 Borderline Conference；R2 认为无新方法且核心发现方向可预期，适合 Findings。
2. **Constrained decoding 严重等级（R1: Must-Fix vs R2: Should-Fix）**——R2 有效反驳了 R1 的"自相矛盾"指控（R1 混淆了 CWM format collapse 和 CLS decision collapse 两种不同 failure mode 的归因），并指出 Appendix (c) 的间接证据已足以回应。Director 采纳 R2 的降级判断（Should-Fix）。
3. **实验规模（R1: 中上水平 vs R2: 严重限制）**——R1 指出 2 families 已超出同类论文常规（多数工作仅 1 个家族），LoRA-only 是合理的控制变量选择。Director 采纳 R1 的判断——scope 限定已到位（Abstract "≤8B LoRA fine-tuning"），非 critical 问题。

---

## Questions（需作者澄清）

**Q1.** CWM repo-level 的 unparseable outputs 施加 constrained decoding 后，预期 format compliance 率和准确率的变化？是否有初步实验数据？

**Q2.** TRAJ 学习率从 2×10⁻⁴ 降至 5×10⁻⁵（与 CLS/CWM 匹配）后准确率如何变化？

**Q3.** Re-repair 实验中 n=44 和 n=14 的关系是什么？

**Q4.** GenRM 在 math reasoning 中 generative > discriminative，为何 code domain 相反？作者认为关键差异因素是什么（exact match vs semantic equivalence? output space structure? training data properties?）？

**Q5.** Error complementarity 是否在特定 mutation type 上更集中？oracle gap 的来源是 systematic pattern 还是 random noise？

---

## Missing References

1. **Synchromesh** (Poesia et al., 2022) — constrained decoding for code generation，与 CWM format collapse 干预讨论直接相关
2. **XGrammar** — grammar-constrained decoding，同上
3. **ThinkPRM** (2026) — process reward model，与 §4 Process vs. Outcome Supervision 讨论相关（建议作者判断相关性）
4. **SecCodePRM** (2026) — 安全相关 code PRM（建议作者判断相关性）
5. **"Towards Effectively Leveraging Execution Traces for Program Repair"** (2025) — 与 TRAJ formulation 可能相关（建议作者核实是否已 cite）

---

## External Review (Stanford Agentic Reviewer)

未配置，跳过。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 5 info）：

**Warning:**
- **Pages 1-2**: 正文开头连续 2 页纯文本（Title/Abstract/Introduction），审稿人在第 3 页才看到第一个视觉锚点（Figure 1）。建议若空间允许将 Figure 1 提前到 page 2。
- **Pages 7-8**: Table 4 后约 1.5 页连续纯文本（Related Work + Conclusion），结尾段落视觉单调。

**Info:**
- Page 5 三个 display items 密度高，Table 2 可考虑移至 page 6 平衡节奏。
- Figure 2 坐标轴标签字号偏小（~7-8pt），打印可读性处于下限。
- Figure 1 绿色/粉红色对红绿色盲区分度不足，建议改为 blue/orange 或增加纹理。
- 附录 pages 16-17 连续纯文本密度较高。
- 附录末页约 40% 空白。

---

## Overall Assessment

**Overall: 3.0 (Findings)**
**Confidence: 4/5**

**评分理由：**

本文是一篇方法论严谨的实证研究论文，统计分析远超同领域平均水平，failure mode taxonomy 对从业者有实用价值。论文回答了一个有实际意义的问题，实验设计在控制变量方面做得出色。

然而，核心贡献为 "systematic comparison of existing formulations"——无新方法提出，无 novel formulation 设计，核心发现的方向（generation harder at longer outputs）虽然幅度和细节不可先验预测，但方向上不够 surprising。Excitement 稳定在 2.5-3.0/5（R1: 3/5, R2: 2.5/5），反映了这一 inherent limitation。

关键未解决的 weakness：(1) constrained decoding 未直接测试（有间接证据但正文可见度不足）；(2) TRAJ 比较本质上是 observational；(3) GenRM domain contrast 严重低估，错失了提升 novelty 的最佳机会。

**Director 综合判断**：R1 (3.5) 和 R2 (3.0) 的分歧在于 empirical comparison paper 的 novelty 标准。Director 倾向 R2 的判断——在 EMNLP 2026 ARR 评分体系下，3.0 (Findings) 准确反映了本文的贡献层级：方法论扎实、有实用价值，但 intellectual novelty 未达主会议门槛。以 Findings 投稿是合理定位。

**可提升至 3.5 (Borderline Conference) 的条件：**
1. 将 Appendix (c) 关键证据（CWM 误训实验 + parseable-only accuracy）提升到正文
2. 展开 GenRM domain contrast 讨论（code vs math reasoning 的 generative verification 差异机制）
3. 修正 Abstract 中 TRAJ 表述

---

## Detailed Comments

### Abstract
- ~172 词，合规（≤200）。
- "all three formulations achieve comparable accuracy" 过强——CLS-TRAJ 在 Holm 校正后 inconclusive。建议区分。
- "Preliminary 14B results (3 seeds, single family)" 限定到位。

### Introduction (§1)
- Three-layer structure（fine-tuning necessity → function equivalence → repo divergence）叙事清晰。
- Contribution #1 已合并 error complementarity 为子句（R17 修复），权重合理。
- Contribution #2（failure mode taxonomy）是最有实践价值的贡献。
- Mechanistic pathway（"operating through output format"）限定到位（R16 修复）。

### Method (§2)
- 三种 formulation 的形式化定义清晰。
- §2.2 Expected Failure Modes 提供了合理的先验框架。
- §2.3 Oracle Framework 预测与实验一致（R2 的 W3 矛盾指控被 R1 有效反驳）。
- CWM world model 术语辨析脚注到位（R17 修复）。

### Experiments (§3)
- §3.1 Setup 充分（hyperparams 在 Appendix，统计层次已声明）。
- §3.4 Equivalence 中 power ~0.3 的 caveat 到位，14B TOST 完成。
- §3.5 Repo-level 的 "exploratory due to limited seed coverage" 标注到位。
- §3.6 Analysis 中 failed interventions 列表有价值但缺少 constrained decoding——建议增补 Appendix (c) 间接证据到正文。
- §3.7 Threats 诚实、全面。

### Related Work (§4)
- 覆盖较完整。GenRM/CodeRM/CodeScaler/GenPRM/Aletheia 均已 cite。
- DreamPRM/CodePRM 已展开讨论（R17 修复）。
- 缺少 constrained decoding 方向引用（Synchromesh, XGrammar）。

### Conclusion (§5) + Limitations
- "under ≤8B LoRA fine-tuning" 限定到位（R17 修复）。
- GenRM contrast 仅一句话，应展开。
- Limitations section 位置正确（正文内），长度合适。
- Constrained decoding 和 32B+ scaling 作为 open question 合理。
- AI assistants disclosure（Appendix P）符合 ACL 政策。

### Format Compliance
- 8 页正文 ✓
- Double-blind（author = "Anonymous"）✓
- ACL template（\usepackage[review]{acl}）✓
- Limitations section in main text ✓
- ARR checklist in OpenReview form（PDF 中已注释）✓
- Abstract ≤200 词 ✓
