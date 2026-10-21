---
round: 6
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-21T15:00:46.981911+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 6 (Fresh Review)

**论文**: Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**日期**: 2026-05-21
**Reviewer 编排**: 2 人（R1 方法严谨性，R2 新颖性与完整性）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成共识）

---

## Summary

本文研究 LLM agent 在自然语言策略规范下因歧义导致安全违规的因果关系。基于 τ²-bench（客服/航空双域），构建 300 组 matched clause pairs（6 类歧义 × 50 对），在 5 个模型上跑 2,997 episodes。核心发现：歧义使违规率增加 34.0 pp（OR=15.1），存在三层类型 hierarchy（incompleteness > 中间四类 > coreferential），且 model×type 交互效应显著但仅解释 2.9% 方差。提出 Differential Nocuity 框架和 Ambiguity Blindness 现象（<11% 消歧意识）。

---

## Strengths

1. **因果设计首创性**：matched-pair + perturbation control 在 agent safety 文献中极为少见，相比 DRIP-R 等 correlation-based 工作因果推断力显著更强 [R1+R2 共识]
2. **统计方法论扎实**：TOST 七档 sensitivity、Holm-Bonferroni 多重校正、Gwet's AC₁、dual-judge calibration、ICC 可复现性——统计稳健性检查全面 [R1]
3. **跨架构泛化**：5 模型 + 2 额外 model families（7 模型 × 6 providers），C1 在全部 7 模型上显著 [R1+R2]
4. **透明的 claim 分级**：C3 标注 inconclusive、C4 标注 [Exploratory]，在 agent safety 领域（常见 overclaiming）中难得 [R1]
5. **跨领域理论迁移**：将 RE 的 nocuous/innocuous 区分引入 LLM agent safety，概念贡献有实质价值 [R2]
6. **Limitations 详尽诚实**：7 段覆盖了主要方法论弱点，减少了审稿人需要"发现"的隐藏问题 [R1+R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF3 [critical, R1+R2 完全共识]** Incompleteness confound 削弱 C2 three-tier hierarchy

Incompleteness 的 unambiguous variant 必须添加新 policy content，与其他 5 类的 minimal-edit disambiguation 操作不对称。Appendix F 的 logistic regression（p=0.022, coefficient change <8%）缓解但未消除 confound：(1) token count 是 information content 的粗糙代理；(2) 8% 系数变化方向未报告；(3) 排除 incompleteness 后 omnibus p=0.079 不显著，hierarchy 实质退化为 two-tier。论文将 incompleteness 的 top-tier 地位作为核心发现呈现，但这一 ranking 受 confound 驱动的可能性未被充分承认。

→ 需要：(1) 正文中（非仅 Appendix）将 incompleteness ranking 表述为 upper bound；(2) 报告 logistic regression coefficient 变化方向和完整模型输出；(3) 以 two-tier structure（excluding incompleteness）作为 confound-robust 核心发现。

**MF4 [critical, R1+R2 完全共识]** Discussion 对 C4 [Exploratory] 做过度因果推断

C4 被标注 [Exploratory] 且仅解释 2.9% 方差，但 Discussion 做了多处强因果推断：(1) "safety training does not uniformly reduce ambiguity vulnerability" 是因果声明，需同一 base model RLHF 前后对比才能支撑；(2) "The agent never encounters a decision point that RLHF refusal mechanisms can intercept" 无 mechanistic evidence；(3) "canary type" 基于 5 模型上 1 type 的 cross-sectional 观察。Abstract 第 5-6 句缺少 [Exploratory] 限定。

→ 需要：(1) Discussion 所有 C4 推断加 "one possible explanation" / "consistent with but not evidence for" 等限定；(2) Abstract 加 [Exploratory] 或弱化措辞；(3) RLHF mechanism 段落移至 Future Work 或改为 hypothesis。

**R6-N3 [critical, R1 raised, R2 agrees with nuance]** Cross-judge asymmetry 对 C4 canary claim 的特异性影响

Authorization scope 是 C4 "canary type" 的核心证据（Claude 12% vs GPT-5.4 64%），但：(1) GPT-5.4 由 GPT-4.1 评判，其余由 GPT-5.4 评判——GPT-5.4 的 64% 无法纳入 within-judge 比较；(2) authorization scope 的 judge agreement 恰好最低（κ=0.385）；(3) within-judge 组（Claude/Qwen3/DeepSeek by GPT-5.4）内部模式一致（12%/26%/60%），但缺少 GPT-5.4 自身的可靠锚定。

→ 需要：(1) 对 dual-judge calibration 100 episodes 单独分析 authorization scope 的 judge-specific detection rates；(2) §5.4 明确讨论 GPT-5.4 64% 的 judge reliability 限制；(3) 考虑 human spot check。

### Should-Fix（影响评分但不一票否决）

**R6-W1** [R2→R1 降级] Type assignment IAA 未报告——论文有 annotation QC（§4.2 两名标注员确认单类型），但未报告类型分类本身的 inter-annotator agreement。

**R6-W2** [R2→R1 降级] Discussion 域泛化措辞（"deployed systems"、"practitioners should"）超出两域客服实验的覆盖范围，需加域限定。

**SF7** [reopened] 遗漏 clarification-seeking 文献：Structured Uncertainty guided Clarification (2025) 与 Ambiguity Blindness 直接对话；ASPI (2026) 与 disambiguation channel 框架相关。

**R6-W3** Mitigation experiment 每 cell ~50 episodes，未报告 CI，部分 Δ 近零（Claude auth scope 0.0pp）。应标注为 preliminary analysis 而非 practical implications。

**R6-W4** C4 interaction test 用 ANOVA F-test on binary outcome（n=50/cell），应补充 logistic regression with interaction terms 作为 robustness check。

**R6-W5** ICC=0.919 仅在 GPT-5.4 + GPT-4.1 上计算，不覆盖跨 provider 可复现性。

**R6-W6** 100 episodes human validation 仅报告 pooled agreement，per-type（特别是 authorization scope）的 human-LLM agreement 缺失。

**R6-W7** Perturbation control（synonym substitution + clause reordering）不覆盖 information-addition confound，对 incompleteness 无特异性控制力。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：
- **MF3**: Incompleteness confound 是最核心的方法论弱点，three-tier hierarchy 的第一 tier 不可靠
- **MF4**: Discussion 对 C4 的因果推断超出 2.9% 探索性方差的支撑范围
- **R6-N3**: Cross-judge asymmetry 在 authorization scope 上的影响（R2 with nuance）
- **SF7**: 遗漏 clarification-seeking 文献
- **R6-W3**: Mitigation experiment underpowered
- **引用元数据**: lassiter year / ferrari cite key / levy accent

## Reviewer Divergence

以下问题存在分级分歧（已通过交叉讨论解决）：
- **R2-N2 Taxonomy MECE**: R2 列为 critical → R1 rebut 降为 Should-Fix（论文有 annotation QC 但缺 type IAA）→ **共识：Should-Fix (R6-W1)**
- **R2-N3 单域泛化**: R2 列为 critical → R1 rebut 降为 Should-Fix（双域非单域，但 Discussion 措辞需收敛）→ **共识：Should-Fix (R6-W2)**
- **R1-W5 页面溢出**: R1 列为 warning → R2 rebut 为 trivial formatting fix → **共识：minor，需确认**

---

## Questions

1. Appendix F logistic regression 控制 information delta 后，incompleteness coefficient 变化方向（增大还是减小）？请提供完整模型输出。
2. Dual-judge calibration 100 episodes 中 authorization scope 子集样本量多少？κ=0.385 的 CI？
3. C4 F-test F(20)=1.97 是 cell-level proportions ANOVA 还是 individual-level ANOVA？
4. Perturbation control 中 synonym substitution / clause reordering 是否有 annotator 确认不引入新 ambiguity？
5. 单日（May 20）完成 ~5,233 multi-turn episodes 的技术可行性确认？

---

## Missing References

- **Structured Uncertainty guided Clarification for LLM Agents (2025)**: 直接研究 agent 面对歧义的 clarification-seeking 行为，与 §6.2 Ambiguity Blindness 形成核心对话 [R1+R2 共识]
- **ASPI (2026)**: clarification seeking 与 prompt injection 风险，与 disambiguation channel availability 框架相关 [R1+R2]
- OpenAgentSafety (ICLR 2026) 和 Agent-SafetyBench (2024): 间接相关，覆盖 agent safety evaluation landscape [R2，R1 认为相关性较弱]

---

## External Review (Stanford Agentic Reviewer)

状态：**已提交**（2026-05-21T14:45:37Z），结果尚未返回。

---

## Visual Layout Check（非评分项）

视觉审查已完成（1 warning + 9 info）：

- **[warning]** pp.3-5 连续 3 页纯文本（Related Work → Taxonomy → Method），无 figure/table/equation 穿插。Taxonomy 是核心贡献之一，缺少可视化表示（层次图或概览表）使审稿人难以快速建立认知结构。建议 §3 插入 taxonomy 概览图。
- [info] 主文仅 4 个 display items（2 fig + 2 table），对实证论文偏少（通常 5-8 个）
- [info] Figure 3 六色方案色盲可辨识度需验证
- [info] Figure 1 内部文字偏小（~6pt）
- [info] Figure 2 forest plot 清晰，CI 和零线标注完整
- [info] Table 1/2 格式规范
- [info] Appendix 末页空白偏多
- [info] References 无 [?] 未解析引用

---

## Overall Assessment

**Overall: 3.5 (Borderline Conference)**
**Confidence: 4/5**（两名 Reviewer 均仔细审读全文及附录，在交叉讨论中对关键问题达成共识）

**评分理由**：

论文在 agent safety 文献中引入了罕见的因果设计（matched-pair + perturbation control），C1（ambiguity causes violations, OR=15.1, 7 模型复现）的证据坚实，Differential Nocuity 框架有实质概念贡献。统计方法论全面（TOST、Holm-Bonferroni、dual-judge calibration、human validation），claim 分级透明。

但 3 个 critical 问题限制了当前版本的接收水平：(1) C2 three-tier hierarchy 的第一 tier（incompleteness）受 information-addition confound 驱动，排除后 hierarchy 退化为 two-tier 且不显著；(2) C4 [Exploratory] 在 Discussion/Abstract 中被过度推断为因果机制；(3) C4 canary claim 的核心证据（authorization scope）恰好在 judge reliability 最弱的 type 上，且 GPT-5.4 的 64% 率无法被 within-judge 验证。

**修改可行性**：MF3 和 MF4 可通过 framing 调整和补充统计输出在一轮内解决（将 incompleteness ranking 表述为 upper bound，将 two-tier 作为核心发现，收敛 Discussion 推断）。R6-N3 可能需要 human spot check 或更保守的 canary claim。修改后有潜力达到 4.0 (Conference)。

---

## Detailed Comments

### §1 Introduction
- Contribution list 清晰，C1-C4 分级得当
- "perturbation control (n=300, Δ_perturb = -0.67 pp, CI containing zero)" 与 Method 一致
- 建议：Contribution 2 中 "three-tier type hierarchy" 加注 incompleteness confound 的 caveat

### §2 Related Work
- RE ambiguity 和 psycholinguistics 文献覆盖良好
- Agent safety 部分覆盖了主体 benchmark（R-Judge, ToolEmu, InjecAgent, ShieldAgent, AgentAuditor）
- **缺失**：clarification-seeking 文献（与 Ambiguity Blindness 直接对话）

### §3 Taxonomy
- 六类两层结构设计合理，每类有清晰定义和示例
- Incompleteness 的操作不对称已在 §3 末段注明（"a confound we address in §5"），但正文处理不够突出
- **视觉审查建议**：此节纯文本，缺少 taxonomy 概览图

### §4 Method
- Matched-pair 设计严谨，300 对 × 5 模型的规模充分
- Cross-judge calibration 和 human validation 是本文方法论亮点
- ICC=0.919 excellent，但仅覆盖 2 个 OpenAI 模型（R6-W5）
- Perturbation control 对 semantic ambiguity 有特异性，但不覆盖 information-addition（R6-W7）

### §5 Results
- C1 证据坚实（OR=15.1，所有 6 types 和 5 models 均显著）
- C2 hierarchy: Cramér's V=0.137 在 df=5 下属 medium effect，三层结构在 TOST 七档 sensitivity 下稳定，但依赖 incompleteness（confounded）和 coreferential（floor effect）
- C3 诚实标注 inconclusive
- C4 标注 [Exploratory] 但方差解释力仅 2.9%——F-test on binary outcome 需补充 logistic regression robustness check

### §6 Error Analysis
- 三类 failure mechanism（structural misparse, information gap-filling, boundary violation）分类清晰
- Ambiguity Blindness 发现有力（<11% awareness, >88% surface adoption），但缺少与 clarification-seeking 文献的对话
- Per-model 差异已报告（Claude/GPT-4.1 11% vs Qwen3/DeepSeek 0%），但未深入分析原因

### §7 Discussion
- Differential Nocuity 框架有概念价值
- **核心问题**：对 C4 的因果推断超出数据支撑（MF4）
- Mitigation table (Table 2) 有实用价值但 CI 缺失（R6-W3）
- "practitioners should" 等措辞需加域限定（R6-W2）

### §8 Conclusion
- 简洁准确，但可能有 4-5 行溢出至第 9 页（待确认）

### §9 Limitations
- 7 段覆盖全面，诚实承认主要弱点
- 符合 EMNLP 2026 要求（mandatory，不计页数）

### Appendix
- TOST sensitivity (App A), mitigation (App B), severity comparison (App C), detection (App D), replication (App E), confound (App F) 均提供了有价值的补充分析
- App F 的 logistic regression 需补充完整输出（coefficient direction, all type coefficients + CIs）