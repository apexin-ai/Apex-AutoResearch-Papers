---
round: 17
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T04:12:16.859887+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 19 审稿报告 — exec-sim-repair-verifier

**论文**: "A Systematic Comparison of Execution-Free Verification Formulations for Code Repair"
**Venue**: EMNLP 2026 via ACL Rolling Review
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性; R2: 新颖性/完整性）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛，无需 Round 2）

---

## Summary

本文首次在匹配条件下系统比较三种 execution-free code repair verification formulations（CLS 分类、CWM 生成、TRAJ 轨迹级评分），使用两个代码 LLM 家族（Qwen3, DeepSeek-Coder）、两个复杂度层级（function-level, repo-level）和多个训练种子。核心发现为 complexity-moderated formulation choice：function-level CLS 和 CWM 统计等价（TOST p=0.007），repo-level 在 ≤8B LoRA 条件下 CLS 显著优于 CWM（18-26pp gap），伴随 format collapse。统计方法论（TOST + clustered bootstrap + Bayesian ROPE + mixed-effects LPM + Holm-Bonferroni）在同类实证论文中属上乘。

---

## Strengths

**S1. 匹配实验框架设计良好。** 三种 formulation 在同一 LoRA 配置、同一基座模型、同一数据集上训练，控制了 model capacity、optimizer、data 等变量。跨两个模型家族和两个复杂度层级增强外部效度。[共识]

**S2. 统计方法论出色。** TOST 等价性检验（非仅 non-significance）+ clustered bootstrap（114 problem clusters）+ Bayesian ROPE + Holm-Bonferroni 多重比较校正 + mixed-effects LPM，形成完整推断链。SESOI sensitivity analysis（±1.52pp 最小等价边界）比仅报 p-value 更有信息量。§3.1 已声明统计层次（primary vs robustness check）。[共识]

**S3. Failure mode taxonomy 有实践价值。** Table 4 的三种 failure mode（format collapse, decision collapse, aggregation penalty）来自 per-mutation 和 repo-level 错误分析，为从业者选择 formulation 提供可操作的诊断标准。[共识]

**S4. 诚实的局限性披露。** §3.5 标注 "exploratory due to limited seed coverage"；§3.7 主动识别 5 个潜在混淆；Abstract 标注 "Preliminary 14B results (3 seeds, single family)"；TRAJ 标注 "inherently confounded"。[共识]

**S5. Matched-context ablation 排除输入长度混淆。** CLS@2048 仅损失 1.44pp（gap 保留 98%），确认 repo-level gap 来自 output 而非 input 差异。[共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

*本轮无 Must-Fix 共识。R1 将 TRAJ confounding（R1-N1）和 constrained decoding（隐含同意 R2-N2）各标为接近 Must-Fix，R2 均降为 Should-Fix 级别（有间接证据和 caveats 缓解）。Director 采纳降级。*

### Should-Fix（影响评分但不一票否决）

**SF1. [Should-Fix] TRAJ 训练配置差异使 CLS-TRAJ 比较属 observational 而非 controlled。**
- R1 标为最关键问题之一（R1-N1），R2 同意问题存在但降级。
- 差异：~100× 数据量、4× 学习率、不同标签粒度（per-test vs variant-level）。这些差异 inherent to formulation design，但使 CLS-TRAJ 等价性结论的 formulation-level attribution 打折扣。
- 缓解因素：(1) downsample ablation 控制了数据量（CLS 80.74% vs TRAJ 72.92%）；(2) function-level 近等价证明 formulation 本身可行；(3) Abstract 已标注 "inherently confounded"；(4) §3.1 有显式配置说明。
- 两人共识此 confound 无法完全消除——属 formulation-inherent。

**SF2. [Should-Fix] Constrained decoding 未测试，CWM "formulation-inherent" 归因不稳固。**
- R2-N2 标为最关键问题之一，R1 同意。
- CWM format collapse（53-74% unparseable）是 repo-level gap 的主要机制，但四种干预均未包含 constrained decoding——最直接针对 format compliance 的工程手段。
- Appendix (c) 间接证据已部分缓解：CWM 误训 CLS-format 数据 → 86.05% + 0% unparseable（等价于完美 constrained decoding），仅恢复到 CLS 水平；parseable CWM 仅 38-43%，远低于 majority baseline。说明 format compliance ≠ semantic accuracy。
- Limitations 已引用 Synchromesh/XGrammar/Outlines（R18 修复），§3.6 提及 Appendix (c)。但关键证据仍主要在 Appendix 中，正文可见度不足。
- **建议将 Appendix (c) 两项关键证据（误训实验 + parseable-only accuracy）提升到正文 §3.5 或 §3.6。**

**SF3. [Should-Fix] Repo-level 仅 2-3 seeds，CI 宽度与点估计精度不匹配。**
- 两人共识。18-26pp 报告精度高，但 variant-level bootstrap HDI 宽度 ~25pp。§3.5 "exploratory" 标注到位，但 Abstract 和 Conclusion 数字精度暗示更高确定性。
- **建议 Abstract 中报告 CI 范围或使用更审慎的区间表述。**

**SF4. [Should-Fix] GenRM domain contrast 被严重低估——最有 novelty 潜力的发现。**
- 两人强烈共识。Generative verification（CWM）在 code domain 不优于 discriminative（CLS），与 math reasoning 中 GenRM 结论相反。这一 domain-specific 对比可能是论文最有影响力的潜在贡献之一，但 Conclusion 仅一句话带过。
- Code domain 的 exact match 严格性、output space 结构化程度、training data 性质等可能机制均未展开。
- **建议在 §4 Related Work 或 §5 Conclusion 中增加一段讨论 code vs math 的 generative verification 差异机制。**

**SF5. [Should-Fix] Error complementarity 实际可操作性不足——oracle-to-achievable gap 过大。**
- 两人共识。Oracle 90.63% 但 simple heuristics <0.4pp。§1 已将 complementarity 合并为 Contribution #1 子句，但 §3.6 和 Conclusion 中 routing 表述仍偏乐观。
- **建议弱化 routing 方向表述或增加 "the large oracle-to-achievable gap suggests this may not be practically exploitable with current methods" caveat。**

**SF6. [Should-Fix] ≤8B LoRA 范围限制下标题泛化声明偏广。**
- R2 持续关注，R1 部分同意。Abstract 已有 "≤8B LoRA fine-tuning" 限定，但标题 "A Systematic Comparison..." 暗示通用性。R1 反驳：2 families 已超出同类论文常规，"systematic" 指方法论系统性而非穷举性。分歧存在但非 critical。

### Minor（不影响接收）

**M1.** CWM exact string matching 未讨论 near-match 敏感性（浮点数差异等）。Appendix (c) relaxed matching 部分回应但未在正文展开。[R1]

**M2.** Figure 2 y-axis 截断（~85% 起始）可能夸大视觉差异。Caption 已标注 "y-axis does not start at zero"。[已有 disclosure]

**M3.** Figure 2 axis labels 和 legend 字号偏小（约正文 60-65%），150dpi 下辨识困难。[视觉审查]

---

## Reviewer Consensus [AGREE]

1. **统计方法论出色**——TOST + clustered bootstrap + Bayesian ROPE + LPM + Holm-Bonferroni 在同类论文中属上乘。
2. **Failure mode taxonomy 有实践价值**——三种 failure mode 为从业者提供可操作诊断。
3. **TRAJ 比较本质上是 observational**——训练配置差异使 formulation-level attribution 打折扣。
4. **Constrained decoding 未测试是明确 gap**——但 Appendix (c) 间接证据已部分缓解。
5. **GenRM domain contrast 被严重低估**——最有 novelty 潜力的观点仅一句话。
6. **Error complementarity 实际不可操作**——oracle gap 大但 achievable gain 接近零。
7. **核心发现方向可预测**——generation harder at longer outputs 方向直觉可预期，但幅度和具体失败机制不可先验推导。
8. **论文适合 Findings**——方法论扎实有实用价值，但 novelty 未达主会议门槛。

## Reviewer Divergence [REBUT]

1. **Overall 评分（R1: 3.5 vs R2: 3.0）**——R1 认为 rigorous methodology + actionable failure taxonomy 足以支撑 Borderline Conference；R2 认为无新方法且核心发现方向可预期，Findings 更准确。分歧核心在于 empirical comparison paper 的 novelty 标准。
2. **核心发现新颖性**——R1 认为 TRAJ 等价性、failure taxonomy 细节、14B convergence 有非平凡发现；R2 认为这些属 expected from first principles，不构成 intellectual contribution 的独立来源。

---

## Questions（需作者澄清）

**Q1.** CWM 施加 constrained decoding 后，预期 format compliance 率和准确率的变化？Appendix (c) 的误训实验是否等价于完美 constrained decoding 的上界？

**Q2.** TRAJ 在 CLS/CWM 匹配学习率（5×10⁻⁵）下的准确率如何？当前 4× 学习率差异是否显著影响结论？

**Q3.** GenRM 在 math reasoning 中 generative > discriminative，code domain 相反——作者认为关键差异因素是什么（exact match vs semantic equivalence? output space structure? training data properties?）？

**Q4.** Error complementarity 在特定 mutation type 上是否更集中？oracle gap 来源是 systematic pattern 还是 random noise？

**Q5.** 14B CWM repo-level 结果是否可用？若 gap 在 14B 收窄，这如何影响 "formulation-inherent vs capacity-contingent" 的结论？

---

## Missing References

1. **ThinkPRM** (2026) — process reward model，与 §4 Process vs Outcome Supervision 讨论相关（建议作者判断相关性）
2. **SecCodePRM** (2026) — 安全相关 code PRM（建议作者判断相关性）

*注：Synchromesh (Poesia 2022), XGrammar (Dong 2025), Outlines (Willard 2023) 已在 Limitations 中引用（R18 修复）。*

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 1 warning, 5 info）：

**Warning:**
- **Pages 1-2**: 连续 2 页纯文本（Title/Abstract/Introduction），审稿人在第 3 页才看到首个视觉锚点（Figure 1）。

**Info:**
- Page 5 三个 display items（Table 1 + Figure 2 + Table 2）密度偏高，正文空间被压缩。
- Figure 2 axis labels 和 legend 字号偏小（~正文 60-65%）。
- Page 8 Related Work + Conclusion 纯文本，属结构性需要。
- Figure 3 仅单一蓝色，视觉层次略单调（灰度打印可区分）。
- Page 15 排版紧凑但格式清晰。

---

## Overall Assessment

**Overall: 3.0 (Findings)**
**Confidence: 4/5**

**评分理由：**

本文是一篇方法论严谨的实证研究论文。统计分析（TOST + Bayesian ROPE + Holm-Bonferroni + clustered bootstrap + LPM）远超同领域平均水平。Failure mode taxonomy 对从业者有实用价值。论文对自身局限性的诚实披露值得肯定。

核心限制在于贡献类型：systematic comparison of existing formulations——无新方法提出，无 novel formulation 设计。核心发现方向（generation harder at longer outputs）虽然幅度和机制细节不可先验预测，但方向上缺少 surprise。Excitement 稳定在 2.5-3.0/5（R1: 3/5, R2: 2.5/5），反映了 empirical comparison paper 的 inherent novelty limitation。

关键未解决的 weakness：(1) constrained decoding 未直接测试，间接证据充分但正文可见度不足；(2) TRAJ 比较本质上是 observational；(3) GenRM domain contrast 严重低估，错失了提升 novelty 的最佳机会。

**Director 综合判断**：R1 (3.5) 和 R2 (3.0) 的分歧在于 empirical comparison paper 的 novelty 标准。Director 倾向 R2 的判断——在 EMNLP 2026 ARR 评分体系下，3.0 (Findings) 准确反映了本文的贡献层级：方法论扎实、有实用价值，但 intellectual novelty 未达主会议门槛。以 Findings 投稿是合理定位。

**可提升至 3.5 (Borderline Conference) 的条件：**
1. 展开 GenRM domain contrast 讨论（code vs math 的 generative verification 差异机制）
2. 将 Appendix (c) 关键证据（CWM 误训实验 + parseable-only accuracy）提升到正文
3. Repo-level 补充 seeds 或在 Abstract 弱化精度表述

---

## Detailed Comments

### Abstract
- ~172 词，合规（≤200）。
- CLS-CWM 等价与 TRAJ inconclusive 已正确区分（R18 修复）。
- "Preliminary 14B results (3 seeds, single family)" 限定到位。
- TOST p=0.007 与 §3.4/Conclusion 三处统一。

### Introduction (§1)
- Three-layer structure（fine-tuning necessity → function equivalence → repo divergence）叙事清晰。
- Mechanistic pathway（"operating through output format"）限定到位。
- Contribution #1 已合并 error complementarity 为子句，权重合理。
- Contribution #2（failure mode taxonomy）是最有实践价值的贡献。

### Method (§2)
- 三种 formulation 形式化定义清晰。
- §2.2 Expected Failure Modes 提供合理先验框架。
- CWM world model 术语辨析脚注到位。

### Experiments (§3)
- §3.1 Setup 充分，统计层次已声明。
- §3.4 Equivalence 中 power ~0.3 caveat 到位。Bayesian ROPE 提供独立佐证。
- §3.5 Repo-level "exploratory due to limited seed coverage" 标注到位。
- §3.6 Analysis 中 Appendix (c) 间接证据应提升到正文——这是最主要的改进建议。
- §3.7 Threats 诚实、全面（5 个 confounds 主动识别）。

### Related Work (§4)
- GenRM/CodeRM/CodeScaler/GenPRM/Aletheia/DreamPRM/CodePRM 均已 cite 并展开。
- Constrained decoding 引用在 Limitations 中到位。

### Conclusion (§5) + Limitations
- "under ≤8B LoRA fine-tuning" 限定到位。
- GenRM contrast 仍仅一句话——应展开为论文最有影响力的方向。
- Limitations 位置正确（正文内），长度合适。
- Constrained decoding 和 32B+ scaling 作为 open question 合理。

### Format Compliance
- 8 页正文 ✓
- Double-blind（Anonymous）✓
- ACL template（\usepackage[review]{acl}）✓
- Limitations section in main text ✓
- Abstract ≤200 词 ✓