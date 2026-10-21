# Director coordination — Part 5 of 7

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/0d/0d5b5d57f8a45f2c2330.json)

## Round 106

### Tool call

_source line 1220 · 2026-05-23T14:01:46.689183+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 14 审稿报告（Fresh Review）\n\n**投稿**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 (ARR)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）\n**轮次**: Round 14 (Fresh Review), 1 轮独立审稿 + 1 轮交叉分享\n\n---\n\n## Summary\n\n本文首次在匹配条件下系统比较了 LLM 代码修复中三种 execution-free 验证公式（CLS 分类、CWM 生成、TRAJ 轨迹级），跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别和多个 seeds。核心发现为三层结构：(1) fine-tuning 必要（35-36pp 增益）；(2) function-level 三种公式近等价（CLS-CWM TOST 确认，CLS-TRAJ Holm 校正后未确认但 gap 单调收窄至 1.07pp@14B）；(3) repo-level 在 ≤8B LoRA 下等价崩塌（CLS-CWM gap 18-26pp，由 format collapse 驱动）。论文同时提供了 failure mode taxonomy 和 error complementarity 分析。\n\n---\n\n## Strengths\n\n**S1. 首个匹配条件的系统比较。** 控制模型容量、训练数据、超参数和评估协议进行 CLS-CWM 比较（TRAJ 为 exploratory），直接回答从业者的 formulation 选择问题。Cross-family 一致性（Qwen3 和 DeepSeek-Coder 在 CLS-CWM 差异方向一致）增强结论可信度。[两人共识]\n\n**S2. 统计框架出色。** TOST 等价检验 + Bayesian ROPE 双验证、clustered bootstrap（114 clusters, 10K resamples）、Holm-Bonferroni 校正（k=5）、ICC/DEFF 修正——在 NLP 实证论文中属上乘水准。[两人共识, R1 Soundness 3.5, R2 Soundness 3.5]\n\n**S3. 透明的局限性标注。** §3.5 将 variant-level 分析标注为 exploratory，§3.7 列出 5 个 confounds 逐项分析（worst-case compounding ~11.5pp），CLS-TRAJ Holm 校正后不成立也如实报告。TOST power ~0.3 在 §3.4 明确讨论。SESOI 未预注册在正文而非 appendix 中诚实披露。[两人共识]\n\n**S4. 实用的 failure mode taxonomy。** Table 4 的三类失败模式（format collapse, decision collapse, aggregation penalty）提供可迁移的诊断框架。四项 failed interventions（LoRA rank doubling, majority voting, relaxed matching, scaling）增强 format collapse 结论可信度。[两人共识]\n\n**S5. 保守的报告策略。** 系统性选择更保守的分析路径（seed-level TOST 而非 problem-level bootstrap），体现方法论诚信。[R1 提出, R2 在交叉回应中确认]\n\n**S6. GenRM 领域特异性观察。** 代码验证中 generation ≤ discrimination（与 GenRM 在数学推理中的发现相反），辅以 output structure 假设和 >50% unparseable 数据。[两人共识, 均认为分析可更深入]\n\n---\n\n## Weaknesses\n\n### Must-Fix（0 项）\n\n*经交叉分享和 Director 裁定，所有初审 Critical 级别 issue 均被降级或合并为 Should-Fix。详见\"裁定分歧\"部分。*\n\n### Should-Fix（7 项）\n\n**W1. [warning] [consensus] CWM baseline 公平性——≤8B LoRA vs 原版 32B。**\n- R2 提出 (Critical), R1 AGREE。Director 裁定降为 Should-Fix。\n- 论文 CWM 是 4-8B LoRA 微调，14B function-level 收敛至 0.43pp 暗示差异可能主要源于 capacity。Abstract \"equivalence collapses\" 倾向于将差异归因于 formulation 而非 capacity。\n- 论文已有 qualification（Abstract \"under our ≤8B LoRA protocol\"、§3.3 scaling、Limitations），但可在 Conclusion 更显著讨论 \"32B+ CWM 是否会消除 format collapse\" 作为 open question。\n- **裁定理由**：论文已有多处 qualifier，但 Abstract/Conclusion 的 framing 仍倾向 formulation-inherent 解读。降为 Should-Fix 因为 (a) qualifier 已存在, (b) 14B 收敛已报告, (c) 进一步修改空间有限。\n\n**W2. [warning] [consensus, R2 downgrade] SESOI ±2pp 阈值未预注册且结论敏感。**\n- R1 提出 (Critical), R2 AGREE with downgrade to Should-Fix。Director 采纳降级。\n- 鲁棒窗口仅 0.48pp (±2.00→±1.52pp)。但 Bayesian ROPE 独立佐证 (P(ROPE)=0.975)、部署合理性论证 (2pp ≈ 2-3 problems out of 114)、DeepSeek CLS-CWM gap 仅 0.02pp 使等价性在实质上不依赖阈值。\n- **建议**：§3.4 增加一句将 Appendix G 的 deployment-relevance 论证提到正文；引用 Bayesian ROPE 作为 sensitivity robustness 补充。\n\n**W3. [warning] [consensus, R2 downgrade] TRAJ 配置非对称性使 \"matched comparison\" 需限定。**\n- R1 提出 (Critical), R2 AGREE with qualification, 建议 Should-Fix。Director 采纳。\n- TRAJ 与 CLS/CWM 存在 lr 4×、数据量 175×、标签粒度三重差异。论文已有 ★ 标记 + §3.5 \"exploratory\" 标注 + Appendix N。但 Abstract \"No prior work compares them under matched conditions\" 应更早限定 TRAJ。\n- **建议**：Abstract 或 §1 中明确 \"matched for CLS and CWM; TRAJ comparison is exploratory due to formulation-inherent training regime differences\"。\n\n**W4. [warning] [consensus] CWM default-to-pass 使 repo-level 准确率系统性失真。**\n- R1 提出, R2 AGREE。\n- 53-74% unparseable → default pass。Appendix K 揭示 unparseable pass rate 74.6% vs parseable 68.3% (χ² p=5.9×10⁻¹⁰)。Table 3 脚注仅简要提及。\n- **建议**：Table 3 增加 \"Parseable Acc (%)\" 列，让读者直接看到 CWM 判别能力。\n\n**W5. [warning] [consensus] CLS-TRAJ label granularity confound 无法消除。**\n- R2 提出, R1 AGREE。\n- CLS per-test labels vs TRAJ variant-level labels 的粒度差异无法通过 downsample 控制。CLS 优势可能来自 label granularity 而非 formulation。\n- 论文 §3.5 已标注 \"exploratory...formulation-inherent confound\"。\n- **建议**：维持当前标注。这是 formulation-inherent confound，无进一步实验修改空间。\n\n**W6. [warning] [consensus] PRM/ORM 映射粒度讨论不够精确。**\n- R2 提出, R1 AGREE。\n- CLS per-test ≠ PRM per-step（粒度不同）；GenRM 在 code 中未胜出的 \"output structure\" 解释未充分展开。\n- **建议**：§4 加 1-2 句 qualify 粒度差异：per-test granularity 对应 per-step PRM，per-patch verdict 对应 outcome-level ORM。\n\n**W7. [warning] [consensus] 缺少 TOST one-sided p-values。**\n- R1 提出, R2 AGREE。\n- 报告 p_upper 和 p_lower 对诊断 CLS-TRAJ 非确认原因有价值——可揭示是上界还是下界被违反。\n- **建议**：Appendix G 补充两个 one-sided p 值。\n\n### 裁定分歧\n\n**R2-N1 (novelty/confirmation study)**: R2 标 Critical (Excitement 2.5/5), R1 REBUT。\n- **Director 裁定：不采纳为独立 issue。** R1 的 REBUT 有说服力——function-level 等价的定量阈值、failure mode taxonomy 的具体分布和机制、capacity-dependent convergence 的量化特征（Figure 2, Table 2）均超越 §2.2 的理论预测。论文的贡献是 \"rigorous quantification with methodological framework\" 而非纯 confirmation。Excitement 受限是 inherent limitation (R6-N4, wont_fix)，不是可修复的 weakness。\n\n**R1-N2 (repo-level 因果归因)**: R1 标 Critical, R2 REBUT (事实错误)。\n- **Director 裁定：部分采纳，合并入 W1。** R2 正确指出 R1 混淆了两个不同统计模型——z=-23.7 来自 139-cluster formulation×complexity 交互 LPM（Appendix J），GEE p=0.449 来自 25-cluster cross-model model 的 model identity 效应。这是不同模型检验不同效应，R1 将两者并列论证因果推断不可靠的推理不成立。Director 核实论文原文（§3.5 最后段）确认 R2 事实核查正确。但 R1 的更广泛关注（2-3 seeds, n=48 variants, 5 confounds）仍有效，论文 §3.5/§3.7 的 hedging（\"exploratory\", \"Limited seed coverage and multiple confounds limit causal attribution\"）已相当充分。\"collapses\" 描述的是统计交互效应的显著性变化，不是因果机制归因。合并入 W1 的 framing concern。\n\n**R2-W3 (error complementarity 无实用信号)**: R2 标 Should-Fix, R1 REBUT。\n- **Director 裁定：不采纳。** Negative result（4 种 heuristic 均 <0.4pp）有独立信息量，排除 naive approaches。论文 framing 诚实（\"motivation for future learned routers\"），篇幅仅 ~1/3 column，定位恰当。\n\n**R1-W2 (14B hedging 不一致)**: R1 标 Should-Fix, R2 REBUT。\n- **Director 裁定：不采纳。** \"consistent with\" 是标准科学 hedging（\"数据不矛盾\"而非\"数据确认\"），与 Abstract \"preliminary observation consistent with\" 语义强度一致。§3.3 已提及 \"low power inherent in 3-seed comparisons\"。\n\n**R1-W3 (ICC 外推)**: R1 标 Should-Fix, R2 部分 AGREE。\n- **Director 裁定：降为 Minor (M7)。** 论文在 Appendix A 已讨论 function-level ICC 作为 conservative lower bound（repo-level ICC 更高会进一步放大 per-test 优势）；TOST 使用 seed-level paired analysis (df=4)，不直接依赖 ICC-derived n_eff。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Figure 2 \"inverted-U trajectory\" 仅 3 数据点，建议改为 \"non-monotonic pattern\"。[两人共识]\n- **M2**: Abstract 中 z=-23.7 和 18-26pp 并列。R2 认为可能混淆不同统计量，R1 REBUT（有明确 context 区分）。Director：不需修改，context 已足够。\n- **M3**: Precision ablation seeds (789/0 NF4) 混入主 seed pool。需确认与 main seeds 独立性。[两人共识]\n- **M4**: Table 3 \"Var.\" 列名应在 caption 注明全称 \"Variant-level accuracy\"。[两人共识]\n- **M5**: Figure 2 caption 应标注 \"y-axis does not start at zero\"（Figure 3 已有此标注）。[R2 提出, R1 同意]\n- **M6**: Table 1 TRAJ \"★\" 标记不够醒目，建议脚注加粗或其他视觉区分。[R1 提出, R2 同意]\n- **M7**: ICC 在 Oracle 分析中的 conservative lower bound 论证在 Appendix A，建议在正文更显著位置简要提及。[R1 提出, R2 部分同意, Director 从 Should-Fix 降级]\n\n---\n\n## Questions for Authors\n\n1. 如果 32B+ CWM 消除 format collapse（如 14B 收敛趋势所暗示），论文的 formulation comparison 结论需如何修正？是否本质上是 \"capacity moderates formulation choice\" 而非 \"complexity moderates formulation choice\"？[R2-Q1, R1 支持]\n2. 是否考虑过使用更窄的 SESOI（如 ±1pp）并接受等价性不确认？在 deployment 场景中，±1pp 和 ±2pp 的实际差异是什么？[R1-Q1]\n3. TRAJ 使用 lr=2×10⁻⁴ 的理由是 \"due to the smaller training set\"，为什么不将 TRAJ 的 lr 也设为 5×10⁻⁵ 并增加 epochs？[R1-Q2]\n4. CWM default-to-pass 是否考虑过替代方案（如 default-to-fail 或 abstain）？替代方案下 gap 会如何变化？[R1-Q4]\n5. §2.2 的 Expected Failure Modes 在实验中是否有任何发现违反了预测？如果没有，实验贡献如何区别于 confirmation study？[R2-Q2, R1 partial REBUT]\n\n---\n\n## Missing References\n\n- **RLTF** (Liu et al., 2023): 使用 execution feedback 训练 code generation 的 RL 方法，与 execution-free 方向形成对比。[R2 提出]\n- **CodeBERTScore** (Zhou et al., 2023): 已引用但仅一次。在 formulation taxonomy 中讨论排除原因（metric vs verification formulation）。[R2 提出]\n- 整体 Related Work 覆盖充分，无重大遗漏。[两人共识]\n\n---\n\n## External Review\n\n**状态**: 未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 完成 (2026-05-23T13:31-13:34)\n**发现**: 0 critical, 1 warning, 16 info\n\n- ⚠️ **Warning**: 连续 2 页纯文本（Abstract + Introduction），首个视觉锚点（Figure 1）延迟到 page 3。审稿人前 2 页只看到密集文字。考虑将 Figure 1 或 teaser table 提前到 page 2。\n- ✓ Figure 1 三面板概念图清晰可读，颜色区分度好\n- ✓ Figure 2 + Table 2 同页，密度高但不拥挤\n- ✓ 所有表格 booktabs 风格一致，最优值加粗，小数位一致\n- ✓ References 无未解析引用，排版正常\n- ✓ Limitations 简短（~1/3 栏），符合 EMNLP 要求\n- ✓ Appendix 表格格式规范，Prompt Templates 代码块清晰\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 共识 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 2.5 | 2.75 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\n**Overall: 3.0 / 5 — Findings**\n\n**裁定依据**：\n1. **方法论贡献真实**——统计框架（TOST+ROPE+Holm+clustered bootstrap）在 NLP 实证研究中属标杆级别，failure mode taxonomy 有独立实践价值。\n2. **三层叙事结构逻辑清晰**——fine-tuning necessary → function-level equivalence → repo-level divergence，数据支撑充分。\n3. **Excitement 受限于研究类型**——核心发现在概念上可预期（短输出时 formulation 无差异、长输出时 generation 困难），量化的 surprise factor 不足以达到主会议标准。这是 empirical comparison 论文的 inherent limitation (R6-N4, wont_fix since round 11)。\n4. **交叉分享后无未解决 Critical issue**——R1 的 3 个 Critical 均被 R2 成功 downgrade/rebut（SESOI→Should-Fix, 因果归因→事实错误, TRAJ→Should-Fix）；R2 的 2 个 Critical 中 novelty 被 R1 REBUT，CWM baseline 两人共识降为 Should-Fix。\n5. **7 项 Should-Fix 均可在修改周期内解决**——Table 3 加列、Appendix G 补 p-values、§3.4/§4 微调措辞等，不影响核心结论。\n6. R1 (3.5) 和 R2 (3.0) 均认为论文处于 Findings 到 Borderline Conference 区间。Director 采纳更保守的评估 (3.0)，因为 novelty ceiling 是 binding constraint。\n\n---\n\n## Detailed Comments\n\n### Reviewer 1（方法严谨性 + 实验有效性）\n\n**初审**: Overall 3.5, Soundness 3.5, Excitement 3.0, Reproducibility 4.0, Confidence 4.0\n- 3 Must-Fix: SESOI 预注册 (N1), repo-level 因果归因 (N2), TRAJ 非对称 (N3)\n- 4 Should-Fix: CWM default-to-pass (W1), 14B hedging (W2), ICC 外推 (W3), TOST p-values (W4)\n\n**交叉回应（对 R2）**:\n- R2-N1 (novelty): **[REBUT]** — function-level 等价性反直觉、failure mode taxonomy 纯经验发现、capacity-dependent convergence 需实验建立；建议降为 Should-Fix\n- R2-N2 (CWM baseline): **[AGREE]** — ≤8B capacity confound 成立，但论文已有部分 qualification\n- R2-W1 (checkpoint): **[AGREE]**\n- R2-W2 (label granularity): **[AGREE]**\n- R2-W3 (complementarity): **[REBUT]** — negative result 有独立价值，framing 诚实\n- R2-W4 (PRM/ORM): **[AGREE]**\n\n### Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n**初审**: Overall 3.0, Soundness 3.5, Excitement 2.5, Reproducibility 4.0, Confidence 4.0\n- 2 Must-Fix: novelty/confirmation (N1), CWM baseline fairness (N2)\n- 4 Should-Fix: checkpoint (W1), CLS-TRAJ confound (W2), complementarity (W3), PRM/ORM (W4)\n\n**交叉回应（对 R1）**:\n- R1-N1 (SESOI): **[AGREE with downgrade]** — 论文透明披露 + Bayesian ROPE + 部署合理性 → Should-Fix\n- R1-N2 (因果归因): **[REBUT]** — R1 混淆 139-cluster 交互 LPM 与 25-cluster 跨模型模型，核心论证基于事实错误\n- R1-N3 (TRAJ 非对称): **[AGREE with qualification]** — 论文已多处限定，但应更早标注 → Should-Fix\n- R1-W1 (default-to-pass): **[AGREE]**\n- R1-W2 (14B hedging): **[REBUT]** — \"consistent with\" 本身即为 hedging\n- R1-W3 (ICC 外推): **[AGREE with qualification]** — 论文实际做法比 R1 描述的更审慎\n- R1-W4 (TOST p-values): **[AGREE]**",
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 14 审稿报告（Fresh Review）\n\n**投稿**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 (ARR)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）\n**轮次**: Round 14 (Fresh Review), 1 轮独立审稿 + 1 轮交叉分享\n\n---\n\n## Summary\n\n本文首次在匹配条件下系统比较了 LLM 代码修复中三种 execution-free 验证公式（CLS 分类、CWM 生成、TRAJ 轨迹级），跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别和多个 seeds。核心发现为三层结构：(1) fine-tuning 必要（35-36pp 增益）；(2) function-level 三种公式近等价（CLS-CWM TOST 确认，CLS-TRAJ Holm 校正后未确认但 gap 单调收窄至 1.07pp@14B）；(3) repo-level 在 ≤8B LoRA 下等价崩塌（CLS-CWM gap 18-26pp，由 format collapse 驱动）。论文同时提供了 failure mode taxonomy 和 error complementarity 分析。\n\n---\n\n## Strengths\n\n**S1. 首个匹配条件的系统比较。** 控制模型容量、训练数据、超参数和评估协议进行 CLS-CWM 比较（TRAJ 为 exploratory），直接回答从业者的 formulation 选择问题。Cross-family 一致性（Qwen3 和 DeepSeek-Coder 在 CLS-CWM 差异方向一致）增强结论可信度。[两人共识]\n\n**S2. 统计框架出色。** TOST 等价检验 + Bayesian ROPE 双验证、clustered bootstrap（114 clusters, 10K resamples）、Holm-Bonferroni 校正（k=5）、ICC/DEFF 修正——在 NLP 实证论文中属上乘水准。[两人共识, R1 Soundness 3.5, R2 Soundness 3.5]\n\n**S3. 透明的局限性标注。** §3.5 将 variant-level 分析标注为 exploratory，§3.7 列出 5 个 confounds 逐项分析（worst-case compounding ~11.5pp），CLS-TRAJ Holm 校正后不成立也如实报告。TOST power ~0.3 在 §3.4 明确讨论。SESOI 未预注册在正文而非 appendix 中诚实披露。[两人共识]\n\n**S4. 实用的 failure mode taxonomy。** Table 4 的三类失败模式（format collapse, decision collapse, aggregation penalty）提供可迁移的诊断框架。四项 failed interventions（LoRA rank doubling, majority voting, relaxed matching, scaling）增强 format collapse 结论可信度。[两人共识]\n\n**S5. 保守的报告策略。** 系统性选择更保守的分析路径（seed-level TOST 而非 problem-level bootstrap），体现方法论诚信。[R1 提出, R2 在交叉回应中确认]\n\n**S6. GenRM 领域特异性观察。** 代码验证中 generation ≤ discrimination（与 GenRM 在数学推理中的发现相反），辅以 output structure 假设和 >50% unparseable 数据。[两人共识, 均认为分析可更深入]\n\n---\n\n## Weaknesses\n\n### Must-Fix（0 项）\n\n*经交叉分享和 Director 裁定，所有初审 Critical 级别 issue 均被降级或合并为 Should-Fix。详见\"裁定分歧\"部分。*\n\n### Should-Fix（7 项）\n\n**W1. [warning] [consensus] CWM baseline 公平性——≤8B LoRA vs 原版 32B。**\n- R2 提出 (Critical), R1 AGREE。Director 裁定降为 Should-Fix。\n- 论文 CWM 是 4-8B LoRA 微调，14B function-level 收敛至 0.43pp 暗示差异可能主要源于 capacity。Abstract \"equivalence collapses\" 倾向于将差异归因于 formulation 而非 capacity。\n- 论文已有 qualification（Abstract \"under our ≤8B LoRA protocol\"、§3.3 scaling、Limitations），但可在 Conclusion 更显著讨论 \"32B+ CWM 是否会消除 format collapse\" 作为 open question。\n- **裁定理由**：论文已有多处 qualifier，但 Abstract/Conclusion 的 framing 仍倾向 formulation-inherent 解读。降为 Should-Fix 因为 (a) qualifier 已存在, (b) 14B 收敛已报告, (c) 进一步修改空间有限。\n\n**W2. [warning] [consensus, R2 downgrade] SESOI ±2pp 阈值未预注册且结论敏感。**\n- R1 提出 (Critical), R2 AGREE with downgrade to Should-Fix。Director 采纳降级。\n- 鲁棒窗口仅 0.48pp (±2.00→±1.52pp)。但 Bayesian ROPE 独立佐证 (P(ROPE)=0.975)、部署合理性论证 (2pp ≈ 2-3 problems out of 114)、DeepSeek CLS-CWM gap 仅 0.02pp 使等价性在实质上不依赖阈值。\n- **建议**：§3.4 增加一句将 Appendix G 的 deployment-relevance 论证提到正文；引用 Bayesian ROPE 作为 sensitivity robustness 补充。\n\n**W3. [warning] [consensus, R2 downgrade] TRAJ 配置非对称性使 \"matched comparison\" 需限定。**\n- R1 提出 (Critical), R2 AGREE with qualification, 建议 Should-Fix。Director 采纳。\n- TRAJ 与 CLS/CWM 存在 lr 4×、数据量 175×、标签粒度三重差异。论文已有 ★ 标记 + §3.5 \"exploratory\" 标注 + Appendix N。但 Abstract \"No prior work compares them under matched conditions\" 应更早限定 TRAJ。\n- **建议**：Abstract 或 §1 中明确 \"matched for CLS and CWM; TRAJ comparison is exploratory due to formulation-inherent training regime differences\"。\n\n**W4. [warning] [consensus] CWM default-to-pass 使 repo-level 准确率系统性失真。**\n- R1 提出, R2 AGREE。\n- 53-74% unparseable → default pass。Appendix K 揭示 unparseable pass rate 74.6% vs parseable 68.3% (χ² p=5.9×10⁻¹⁰)。Table 3 脚注仅简要提及。\n- **建议**：Table 3 增加 \"Parseable Acc (%)\" 列，让读者直接看到 CWM 判别能力。\n\n**W5. [warning] [consensus] CLS-TRAJ label granularity confound 无法消除。**\n- R2 提出, R1 AGREE。\n- CLS per-test labels vs TRAJ variant-level labels 的粒度差异无法通过 downsample 控制。CLS 优势可能来自 label granularity 而非 formulation。\n- 论文 §3.5 已标注 \"exploratory...formulation-inherent confound\"。\n- **建议**：维持当前标注。这是 formulation-inherent confound，无进一步实验修改空间。\n\n**W6. [warning] [consensus] PRM/ORM 映射粒度讨论不够精确。**\n- R2 提出, R1 AGREE。\n- CLS per-test ≠ PRM per-step（粒度不同）；GenRM 在 code 中未胜出的 \"output structure\" 解释未充分展开。\n- **建议**：§4 加 1-2 句 qualify 粒度差异：per-test granularity 对应 per-step PRM，per-patch verdict 对应 outcome-level ORM。\n\n**W7. [warning] [consensus] 缺少 TOST one-sided p-values。**\n- R1 提出, R2 AGREE。\n- 报告 p_upper 和 p_lower 对诊断 CLS-TRAJ 非确认原因有价值——可揭示是上界还是下界被违反。\n- **建议**：Appendix G 补充两个 one-sided p 值。\n\n### 裁定分歧\n\n**R2-N1 (novelty/confirmation study)**: R2 标 Critical (Excitement 2.5/5), R1 REBUT。\n- **Director 裁定：不采纳为独立 issue。** R1 的 REBUT 有说服力——function-level 等价的定量阈值、failure mode taxonomy 的具体分布和机制、capacity-dependent convergence 的量化特征（Figure 2, Table 2）均超越 §2.2 的理论预测。论文的贡献是 \"rigorous quantification with methodological framework\" 而非纯 confirmation。Excitement 受限是 inherent limitation (R6-N4, wont_fix)，不是可修复的 weakness。\n\n**R1-N2 (repo-level 因果归因)**: R1 标 Critical, R2 REBUT (事实错误)。\n- **Director 裁定：部分采纳，合并入 W1。** R2 正确指出 R1 混淆了两个不同统计模型——z=-23.7 来自 139-cluster formulation×complexity 交互 LPM（Appendix J），GEE p=0.449 来自 25-cluster cross-model model 的 model identity 效应。这是不同模型检验不同效应，R1 将两者并列论证因果推断不可靠的推理不成立。Director 核实论文原文（§3.5 最后段）确认 R2 事实核查正确。但 R1 的更广泛关注（2-3 seeds, n=48 variants, 5 confounds）仍有效，论文 §3.5/§3.7 的 hedging（\"exploratory\", \"Limited seed coverage and multiple confounds limit causal attribution\"）已相当充分。\"collapses\" 描述的是统计交互效应的显著性变化，不是因果机制归因。合并入 W1 的 framing concern。\n\n**R2-W3 (error complementarity 无实用信号)**: R2 标 Should-Fix, R1 REBUT。\n- **Director 裁定：不采纳。** Negative result（4 种 heuristic 均 <0.4pp）有独立信息量，排除 naive approaches。论文 framing 诚实（\"motivation for future learned routers\"），篇幅仅 ~1/3 column，定位恰当。\n\n**R1-W2 (14B hedging 不一致)**: R1 标 Should-Fix, R2 REBUT。\n- **Director 裁定：不采纳。** \"consistent with\" 是标准科学 hedging（\"数据不矛盾\"而非\"数据确认\"），与 Abstract \"preliminary observation consistent with\" 语义强度一致。§3.3 已提及 \"low power inherent in 3-seed comparisons\"。\n\n**R1-W3 (ICC 外推)**: R1 标 Should-Fix, R2 部分 AGREE。\n- **Director 裁定：降为 Minor (M7)。** 论文在 Appendix A 已讨论 function-level ICC 作为 conservative lower bound（repo-level ICC 更高会进一步放大 per-test 优势）；TOST 使用 seed-level paired analysis (df=4)，不直接依赖 ICC-derived n_eff。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Figure 2 \"inverted-U trajectory\" 仅 3 数据点，建议改为 \"non-monotonic pattern\"。[两人共识]\n- **M2**: Abstract 中 z=-23.7 和 18-26pp 并列。R2 认为可能混淆不同统计量，R1 REBUT（有明确 context 区分）。Director：不需修改，context 已足够。\n- **M3**: Precision ablation seeds (789/0 NF4) 混入主 seed pool。需确认与 main seeds 独立性。[两人共识]\n- **M4**: Table 3 \"Var.\" 列名应在 caption 注明全称 \"Variant-level accuracy\"。[两人共识]\n- **M5**: Figure 2 caption 应标注 \"y-axis does not start at zero\"（Figure 3 已有此标注）。[R2 提出, R1 同意]\n- **M6**: Table 1 TRAJ \"★\" 标记不够醒目，建议脚注加粗或其他视觉区分。[R1 提出, R2 同意]\n- **M7**: ICC 在 Oracle 分析中的 conservative lower bound 论证在 Appendix A，建议在正文更显著位置简要提及。[R1 提出, R2 部分同意, Director 从 Should-Fix 降级]\n\n---\n\n## Questions for Authors\n\n1. 如果 32B+ CWM 消除 format collapse（如 14B 收敛趋势所暗示），论文的 formulation comparison 结论需如何修正？是否本质上是 \"capacity moderates formulation choice\" 而非 \"complexity moderates formulation choice\"？[R2-Q1, R1 支持]\n2. 是否考虑过使用更窄的 SESOI（如 ±1pp）并接受等价性不确认？在 deployment 场景中，±1pp 和 ±2pp 的实际差异是什么？[R1-Q1]\n3. TRAJ 使用 lr=2×10⁻⁴ 的理由是 \"due to the smaller training set\"，为什么不将 TRAJ 的 lr 也设为 5×10⁻⁵ 并增加 epochs？[R1-Q2]\n4. CWM default-to-pass 是否考虑过替代方案（如 default-to-fail 或 abstain）？替代方案下 gap 会如何变化？[R1-Q4]\n5. §2.2 的 Expected Failure Modes 在实验中是否有任何发现违反了预测？如果没有，实验贡献如何区别于 confirmation study？[R2-Q2, R1 partial REBUT]\n\n---\n\n## Missing References\n\n- **RLTF** (Liu et al., 2023): 使用 execution feedback 训练 code generation 的 RL 方法，与 execution-free 方向形成对比。[R2 提出]\n- **CodeBERTScore** (Zhou et al., 2023): 已引用但仅一次。在 formulation taxonomy 中讨论排除原因（metric vs verification formulation）。[R2 提出]\n- 整体 Related Work 覆盖充分，无重大遗漏。[两人共识]\n\n---\n\n## External Review\n\n**状态**: 未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 完成 (2026-05-23T13:31-13:34)\n**发现**: 0 critical, 1 warning, 16 info\n\n- ⚠️ **Warning**: 连续 2 页纯文本（Abstract + Introduction），首个视觉锚点（Figure 1）延迟到 page 3。审稿人前 2 页只看到密集文字。考虑将 Figure 1 或 teaser table 提前到 page 2。\n- ✓ Figure 1 三面板概念图清晰可读，颜色区分度好\n- ✓ Figure 2 + Table 2 同页，密度高但不拥挤\n- ✓ 所有表格 booktabs 风格一致，最优值加粗，小数位一致\n- ✓ References 无未解析引用，排版正常\n- ✓ Limitations 简短（~1/3 栏），符合 EMNLP 要求\n- ✓ Appendix 表格格式规范，Prompt Templates 代码块清晰\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 共识 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 2.5 | 2.75 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\n**Overall: 3.0 / 5 — Findings**\n\n**裁定依据**：\n1. **方法论贡献真实**——统计框架（TOST+ROPE+Holm+clustered bootstrap）在 NLP 实证研究中属标杆级别，failure mode taxonomy 有独立实践价值。\n2. **三层叙事结构逻辑清晰**——fine-tuning necessary → function-level equivalence → repo-level divergence，数据支撑充分。\n3. **Excitement 受限于研究类型**——核心发现在概念上可预期（短输出时 formulation 无差异、长输出时 generation 困难），量化的 surprise factor 不足以达到主会议标准。这是 empirical comparison 论文的 inherent limitation (R6-N4, wont_fix since round 11)。\n4. **交叉分享后无未解决 Critical issue**——R1 的 3 个 Critical 均被 R2 成功 downgrade/rebut（SESOI→Should-Fix, 因果归因→事实错误, TRAJ→Should-Fix）；R2 的 2 个 Critical 中 novelty 被 R1 REBUT，CWM baseline 两人共识降为 Should-Fix。\n5. **7 项 Should-Fix 均可在修改周期内解决**——Table 3 加列、Appendix G 补 p-values、§3.4/§4 微调措辞等，不影响核心结论。\n6. R1 (3.5) 和 R2 (3.0) 均认为论文处于 Findings 到 Borderline Conference 区间。Director 采纳更保守的评估 (3.0)，因为 novelty ceiling 是 binding constraint。\n\n---\n\n## Detailed Comments\n\n### Reviewer 1（方法严谨性 + 实验有效性）\n\n**初审**: Overall 3.5, Soundness 3.5, Excitement 3.0, Reproducibility 4.0, Confidence 4.0\n- 3 Must-Fix: SESOI 预注册 (N1), repo-level 因果归因 (N2), TRAJ 非对称 (N3)\n- 4 Should-Fix: CWM default-to-pass (W1), 14B hedging (W2), ICC 外推 (W3), TOST p-values (W4)\n\n**交叉回应（对 R2）**:\n- R2-N1 (novelty): **[REBUT]** — function-level 等价性反直觉、failure mode taxonomy 纯经验发现、capacity-dependent convergence 需实验建立；建议降为 Should-Fix\n- R2-N2 (CWM baseline): **[AGREE]** — ≤8B capacity confound 成立，但论文已有部分 qualification\n- R2-W1 (checkpoint): **[AGREE]**\n- R2-W2 (label granularity): **[AGREE]**\n- R2-W3 (complementarity): **[REBUT]** — negative result 有独立价值，framing 诚实\n- R2-W4 (PRM/ORM): **[AGREE]**\n\n### Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n**初审**: Overall 3.0, Soundness 3.5, Excitement 2.5, Reproducibility 4.0, Confidence 4.0\n- 2 Must-Fix: novelty/confirmation (N1), CWM baseline fairness (N2)\n- 4 Should-Fix: checkpoint (W1), CLS-TRAJ confound (W2), complementarity (W3), PRM/ORM (W4)\n\n**交叉回应（对 R1）**:\n- R1-N1 (SESOI): **[AGREE with downgrade]** — 论文透明披露 + Bayesian ROPE + 部署合理性 → Should-Fix\n- R1-N2 (因果归因): **[REBUT]** — R1 混淆 139-cluster 交互 LPM 与 25-cluster 跨模型模型，核心论证基于事实错误\n- R1-N3 (TRAJ 非对称): **[AGREE with qualification]** — 论文已多处限定，但应更早标注 → Should-Fix\n- R1-W1 (default-to-pass): **[AGREE]**\n- R1-W2 (14B hedging): **[REBUT]** — \"consistent with\" 本身即为 hedging\n- R1-W3 (ICC 外推): **[AGREE with qualification]** — 论文实际做法比 R1 描述的更审慎\n- R1-W4 (TOST p-values): **[AGREE]**",
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 1221 · 2026-05-23T14:01:51.055885+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4366
}
```

</details>

---


### Assistant

_source line 1222 · 2026-05-23T14:02:18.679687+00:00_

审稿报告已投递。

**Round 14 审稿结果汇总**：

- **Overall: 3.0/5 (Findings)**，Soundness 3.5，Excitement 2.75，Reproducibility 4.0
- **0 个 Must-Fix**——初审 5 个 Critical 经交叉分享后全部降级/合并（R2 成功 REBUT R1 的因果归因论证中混淆两个统计模型的事实错误；R1 成功 REBUT R2 的 novelty/confirmation 定性）
- **7 个 Should-Fix**：CWM baseline 公平性、SESOI 预注册、TRAJ "matched" 限定、CWM default-to-pass（Table 3 加列）、label granularity confound、PRM/ORM 映射精度、TOST one-sided p-values
- **Issue Tracker 已更新**：9 个复发 issue 添加 round 14 mention，2 个新 issue（R14-W1, R14-W2）
- **视觉审查**：1 warning（前 2 页缺视觉锚点），16 info（整体排版良好）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 107

## Round 107

2 recorded events


### User

_source line 1223 · 2026-05-23T14:02:21.252497+00:00_

[Reviewer 2 审稿结果]:
已完成交叉回应并提交给 Review Director。

核心判断：R1 的 3 个 Must-Fix 中，**N2（因果归因）存在关键事实错误**——将 cross-complexity 模型（139 clusters，z=−23.7）与 cross-model 模型（25 clusters，model identity p 值矛盾）混为一谈，建议不予采纳。**N1（SESOI）和 N3（TRAJ 非对称）** 问题真实但严重性被高估，建议降为 Should-Fix。4 个 Should-Fix 中同意采纳 W1 和 W4，驳回 W2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1224 · 2026-05-23T14:02:34.296953+00:00_

审稿报告已投递完毕。

**Round 14 结果概要**：

- **Overall: 3.0/5 (Findings)**，Soundness 3.5，Excitement 2.75，Reproducibility 4.0
- **0 个 Must-Fix**——交叉分享后所有 Critical 均被降级或合并（R1 的 3 个 Critical 被 R2 downgrade/rebut，R2 的 2 个 Critical 被 R1 rebut/降级）
- **7 个 Should-Fix**：CWM baseline 公平性、SESOI 未预注册、TRAJ "matched" 需限定、CWM default-to-pass 失真、CLS-TRAJ label granularity confound、PRM/ORM 映射粒度、TOST one-sided p-values
- **2 个新增 open issue**：R14-W1 (Table 3 加 Parseable Acc 列)、R14-W2 (Appendix G 补 TOST one-sided p-values)
- **关键裁定**：R1-N2 因果归因的核心论证基于事实错误（混淆 139-cluster 交互 LPM 与 25-cluster 跨模型模型），R2 核实正确；novelty concern 维持 wont_fix（inherent limitation）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 108

## Round 108

46 recorded events


### User

_source line 1225 · 2026-05-23T14:20:02.542037+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1226 · 2026-05-23T14:20:09.163639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1227 · 2026-05-23T14:20:09.215532+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1228 · 2026-05-23T14:20:16.096935+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-23T14:20:16.197732+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1230 · 2026-05-23T14:20:23.375992+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1231 · 2026-05-23T14:20:23.376360+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1232 · 2026-05-23T14:20:28.094105+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 1233 · 2026-05-23T14:20:29.249939+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (266 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D13
…[truncated 1825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-23T14:20:29.300622+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-23T14:20:29.301070+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\usepackage{xcolor}
21	\graphicspath{{../../artifacts/}}
22	
23	% Lists
24	\usepackage{enumitem}
25	
26	% Custom commands
27	\newcommand{\cls}{\textsc{Cls}}
28	\newcommand{\cwm}{\textsc{Cwm}}
29	\newcommand{\traj}{\textsc{Traj}}
30	\newcommand{\fone}{F\textsubscript{1}}
31	\newcommand{\pp}{\,\text{pp}}
32	\newcommand{\tbd}{\textsc{tbd}}
33	\newcommand{\placeholder}[1]{{\color{red}\texttt{[#1]}}}
34	
35	\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}
36	\author{Anonymous}
37	
38	\begin{document}
39	\maketitle
40	
41	\input{abstract}
42	
43	\input{introduction}
44	
45	\begin{figure*}[t]
46	\centering
47	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
48	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
49	\label{fig:reformulation}
50	\end{figure*}
51	
52	\input{method}
53	
54	\input{experiments}
55	
56	
57	\input{related_work}
58	
59	\input{conclusion}
60	
61	\bibliography{references}
62	
63	% ARR checklist is filled in OpenReview submission form, not in PDF
64	% \input{checklist}
65	
66	\input{appendix}
67	
68	\end{document}
69	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1236 · 2026-05-23T14:20:36.966630+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1237 · 2026-05-23T14:20:37.469068+00:00_

1	\begin{abstract}
2	LLM-based repair generates candidate patches, selecting the best via a verifier. Three execution-free alternatives to expensive execution-based verification have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level scoring (\traj{}). No prior work compares \cls{} and \cwm{} under matched conditions; the \traj{} comparison is inherently confounded.
3	
4	We present the first systematic comparison across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is not confirmed after multiple comparison correction at current power (${\sim}$0.3), but the gap narrows monotonically from 3.11\pp{} (4B) to 1.07\pp{} (14B). At repository level, this equivalence collapses ($z{=}-23.7$, DeepSeek-Coder): the \cls{}--\cwm{} gap widens to 18--26\pp{} across 2--3 seeds under our ${\leq}$8B LoRA protocol, driven by format collapse. At 14B (3 seeds, single family), all three formulations narrow to within 1.07\pp{}, a preliminary observation consistent with capacity-dependent convergence.
5	
6	Error complementarity and a failure mode taxonomy motivate complexity-aware routing, though simple heuristics capture $<$0.4\pp{} of oracle advantage.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1238 · 2026-05-23T14:20:37.469506+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1239 · 2026-05-23T14:20:37.922080+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. This connects to a broader pattern in NLP: task formulation---classification vs.\ generation vs.\ span extraction---systematically affects performance~\cite{raffel2020t5}, but the conditions under which each wins remain task-dependent and empirically unresolved. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We pres
…[truncated 3220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1240 · 2026-05-23T14:20:37.922437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1241 · 2026-05-23T14:20:38.425167+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Expected Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation has charact
…[truncated 3341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1242 · 2026-05-23T14:20:38.425573+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1243 · 2026-05-23T14:20:38.928453+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench}; runs with NaN validation loss (due to truncated targets exceeding 2,048-token limits) default to the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Qwen3 \cwm{} runs show early overfitting (best at ${\sim}$6\% of training); checkpoint details in Appendix~\ref{app:hyperparams}.
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model
…[truncated 20121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1244 · 2026-05-23T14:20:38.928850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1245 · 2026-05-23T14:20:39.381063+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. CodeScaler~\cite{zhu2026codescaler} trains execution-free reward models for both RL and test-time scaling. Verification formulations span trajectory-level reward~\cite{shum2025swerm}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. GenRM~\cite{hosseini2025genrm} and GenPRM~\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formula
…[truncated 1495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1246 · 2026-05-23T14:20:39.381712+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1247 · 2026-05-23T14:20:39.482449+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} equivalence is not confirmed after correction, but the gap narrows monotonically to 1.07\pp{} at 14B. At repository level under ${\leq}$8B LoRA, divergence reaches 18--26\pp{} ($z{=}-23.7$), consistent across families (\S\ref{sec:threats}). Preliminary 14B results (3 seeds, single family) narrow all gaps to within 1.07\pp{}; whether the repo-level divergence is formulation-inherent or capacity-contingent remains open. This contrasts with mathematical reasoning, where generative verification outperforms discriminative~\cite{hosseini2025genrm}; we attribute this to output structure---code verification requires exact-match outputs (${\sim}$477 tokens/test for \cwm{} vs.\ 1 for \cls{}), and $>$50\% of repo-level \cwm{} outputs are unparseable, converting generation from a reasoning advantage into a format fidelity challenge absent in math.
5	
6	Three directions follow: (1)~complexity-aware routing; (2)~scaling to 32B+ with more seeds~\cite{meta2025cwm}; (3)~per-test diagnostics for downstream repair.
7	
8	\section*{Limitations}
9	
10	Primary findings use ${\leq}$8B LoRA fine-tuning with multi-seed replication; 14B results use a single model family (Qwen3) with 3 seeds; cross-family replication and evaluation at 32B+ are needed. The repo-level gap may diminish at 32B+ scale or with execution-trace pretraining~\cite{meta2025cwm}. All evaluation uses Python-only benchmarks; other languages may exhibit different format compliance rates. Training data uses synthetic mutation operators~\cite{andrews2005mutation,just2014mutants}; the synthetic-to-real transfer gap remains untested (Appendix~\ref{app:limitations}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1248 · 2026-05-23T14:20:40.336237+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1249 · 2026-05-23T14:20:40.839264+00:00_

1	\appendix
2	
3	\noindent\textbf{Appendix overview.} A: Oracle resolve advantage. B: Ablation studies. C-F: Extended analysis (error complementarity, parseable accuracy, forced parsing, qualitative errors, failed interventions, mutation scaling, inference efficiency, re-repair, chain-of-thought). G: TOST sensitivity (G.1: Bayesian ROPE). H: Effect sizes. I: Holm-Bonferroni. J: Mixed-effects regression. K: Parseable bias. L: CWM convergence. M: Few-shot. N: Threats. O: Downsample. P: Extended validity discussion.
4	
5	\section{Oracle Accuracy-Utility Analysis}
6	\label{app:oracle}
7	
8	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
14	\label{tab:oracle}
15	\resizebox{\columnwidth}{!}{%
16	\setlength{\tabcolsep}{3pt}
17	\begin{tabular}{lcccc}
18	\toprule
19	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
20	\midrule
21	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
22	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
23	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
24	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
25	\midrule
26	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
31	\begin{figure}[h]
32	\centering
33	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
34	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%,
…[truncated 58552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1250 · 2026-05-23T14:20:40.840197+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-23T14:20:41.243875+00:00_

1	% === Statistical Methods ===
2	
3	@article{cameron2008bootstrap,
4	  author    = {A. Colin Cameron and Jonah B. Gelbach and Douglas L. Miller},
5	  title     = {Bootstrap-Based Improvements for Inference with Clustered Errors},
6	  journal   = {Review of Economics and Statistics},
7	  volume    = {90},
8	  number    = {3},
9	  pages     = {414--427},
10	  year      = {2008},
11	}
12	
13	@book{wellek2010,
14	  author    = {Stefan Wellek},
15	  title     = {Testing Statistical Hypotheses of Equivalence and Noninferiority},
16	  publisher = {Chapman and Hall/CRC},
17	  edition   = {2nd},
18	  year      = {2010},
19	}
20	
21	@article{moulton1990,
22	  author  = {Brent R. Moulton},
23	  title   = {An Illustration of a Pitfall in Estimating the Effects of Aggregate Variables on Micro Units},
24	  journal = {The Review of Economics and Statistics},
25	  volume  = {72},
26	  number  = {2},
27	  pages   = {334--338},
28	  year    = {1990},
29	}
30	
31	@book{cohen1988,
32	  author    = {Cohen, Jacob},
33	  title     = {Statistical Power Analysis for the Behavioral Sciences},
34	  edition   = {2nd},
35	  publisher = {Lawrence Erlbaum Associates},
36	  year      = {1988}
37	}
38	
39	@article{kruschke2013bayesian,
40	  title={Bayesian estimation supersedes the t test},
41	  author={Kruschke, John K},
42	  journal={Journal of Experimental Psychology: General},
43	  volume={142},
44	  number={2},
45	  pages={573--603},
46	  year={2013},
47	  publisher={American Psychological Association}
48	}
49	
50	@article{kruschke2018rejecting,
51	  title={Rejecting or accepting parameter values in {B}ayesian estimation},
52	  author={Kruschke, John K},
53	  journal={Advances in Methods and Practices in Psychological Science},
54	  volume={1},
55	  number={2},
56	  pages={270--280},
57	  year={2018},
58	  publisher={SAGE Publications}
59	}
60	
61	% === Execution Simulation ===
62	
63	@inproceedings{gu2024cruxeval,
64	  title={{CRUXEval}: A Benchmark for Code Reasoning, Understanding and Exec
…[truncated 22451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-23T14:20:41.244385+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1253 · 2026-05-23T14:20:41.294916+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1254 · 2026-05-23T14:20:49.429928+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 1255 · 2026-05-23T14:20:50.384547+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool call

_source line 1256 · 2026-05-23T14:20:50.686233+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1257 · 2026-05-23T14:20:56.914035+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 regarding ARR:

## General Submission Guidelines

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR and Anonymity Policy

Following the ACL and ARR policies, there is no anonymity period requirement.

## ARR 2026 May Submission Policy

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), author
…[truncated 718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 7484
}
```

</details>

---


### Tool result

_source line 1258 · 2026-05-23T14:20:56.964784+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 6580
}
```

</details>

---


### Tool result

_source line 1259 · 2026-05-23T14:20:56.965225+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 6278
}
```

</details>

---


### Tool call

_source line 1260 · 2026-05-23T14:21:02.645808+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template double blind ARR May deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit template double blind ARR May deadline"
  }
}
```

</details>

---


### Tool call

_source line 1261 · 2026-05-23T14:21:04.005681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1262 · 2026-05-23T14:21:04.308405+00:00_

1	
2	# === Round 6 Issues (Original) ===
3	
4	# --- Round 6 Must-Fix (Consensus Critical) ---
5	
6	- id: "R6-N1"
7	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
8	  category: experiment
9	  severity: critical
10	  status: resolved
11	  first_raised_round: 6
12	  last_seen_round: 14
13	  mentions:
14	    - round: 6
15	      reviewers: [1, 2]
16	      note: "两人独立提出，最高共识。"
17	    - round: 7
18	      reviewers: [pre-review]
19	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress."
20	    - round: 8
21	      reviewers: [1, 2]
22	      note: "Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp."
23	    - round: 9
24	      reviewers: [1, 2]
25	      note: "Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported."
26	    - round: 10
27	      reviewers: [1, 2]
28	      note: "Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations."
29	    - round: 11
30	      reviewers: [1, 2]
31	      note: "Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion."
32	    - round: 13
33	      reviewers: [1]
34	      note: "Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure."
35	    - round: 14
36	      reviewers: [1, 2]
37	      note: "Fresh review R14. R1-N2 re-raises（2-3 seeds, n=48, 5 confou
…[truncated 38912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-23T14:21:09.644171+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template double blind ARR May deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the web search results, here is the information about EMNLP 2026 submission requirements:

## Key Submission Details

**Deadline:** The ARR submission deadline is May 25, 2026.

**Page Limits:** The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

**Template:** EMNLP uses the standard ACL style files, so
…[truncated 947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 6998
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-23T14:22:18.340898+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 1265 · 2026-05-23T14:22:42.590965+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24250
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-23T14:22:42.742281+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题：A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_13/submitted.pdf\n\n## Venue 要求（实时搜索确认）\n- **EMNLP 2026**，通过 ARR 统一审稿\n- **正文 8 页**（不含 references、limitations、ethical considerations）\n- **ACL 模板**（\\usepackage[review]{acl}）\n- **Double-blind**：无作者信息，避免自引暴露身份\n- **ARR Checklist**：在 OpenReview submission form 填写，不在 PDF 中\n- **Deadline**：2026-05-25（ARR May cycle）\n- **评分标准**：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n重点审查以下方面：\n\n1. **统计方法论**\n   - TOST 等价检验：±2pp SESOI 的合理性、pre-registration 状态、sensitivity analysis 是否充分\n   - Holm-Bonferroni 多重比较校正：5 个比较的选择是否合理\n   - Clustered bootstrap vs seed-level paired analysis 的选择\n   - Bayesian ROPE 与 frequentist TOST 的一致性/分歧处理\n   - ICC 和 DEFF 的计算和使用\n   - Power analysis：~0.3 power 对结论的影响\n\n2. **实验设计**\n   - Seed coverage：function-level 5 seeds vs repo-level 2-3 seeds 的不对称\n   - Checkpoint selection：CWM NaN val loss → final epoch vs CLS val-selected\n   - CWM baseline fairness：≤8B LoRA vs 原始 CWM 32B\n   - TRAJ 训练配置差异：~400 vs ~70K instances, 不同 lr, variant-level labels\n   - Mixed precision：bfloat16 vs NF4 seeds 的处理\n   - 14B scaling：仅 1 model family (Qwen3), 3 seeds\n\n3. **Threats to Validity**\n   - 5 个 confound 的评估是否充分\n   - Preprocessing-checkpoint confound chain\n   - Synthetic mutation → real fault 的外部效度\n   - Evaluation sequence length 对 CWM 的影响\n\n4. **统计 Claims 的严谨性**\n   - Abstract/Conclusion 中的 claims 是否有统计支撑\n   - \"collapses\"、\"driven by format collapse\" 等因果措辞\n   - 14B \"capacity-dependent convergence\" 的证据强度\n   - z=-23.7 interaction test 的适用范围（仅 DeepSeek-Coder）\n\n请按以下格式输出审稿意见：\n\n### Summary（2-3 句）\n### Strengths（逐条）\n### Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）\n### Questions（给作者的问题）\n### Missing References\n### Overall Assessment（评分 + 置信度 + 理由）\n### Detailed Comments（逐节）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题：A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_13/submitted.pdf\n\n## Venue 要求（实时搜索确认）\n- **EMNLP 2026**，通过 ARR 统一审稿\n- **正文 8 页**（不含 references、limitations、ethical considerations）\n- **ACL 模板**（\\usepackage[review]{acl}）\n- **Double-blind**：无作者信息，避免自引暴露身份\n- **ARR Checklist**：在 OpenReview submission form 填写，不在 PDF 中\n- **Deadline**：2026-05-25（ARR May cycle）\n- **评分标准**：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n重点审查以下方面：\n\n1. **统计方法论**\n   - TOST 等价检验：±2pp SESOI 的合理性、pre-registration 状态、sensitivity analysis 是否充分\n   - Holm-Bonferroni 多重比较校正：5 个比较的选择是否合理\n   - Clustered bootstrap vs seed-level paired analysis 的选择\n   - Bayesian ROPE 与 frequentist TOST 的一致性/分歧处理\n   - ICC 和 DEFF 的计算和使用\n   - Power analysis：~0.3 power 对结论的影响\n\n2. **实验设计**\n   - Seed coverage：function-level 5 seeds vs repo-level 2-3 seeds 的不对称\n   - Checkpoint selection：CWM NaN val loss → final epoch vs CLS val-selected\n   - CWM baseline fairness：≤8B LoRA vs 原始 CWM 32B\n   - TRAJ 训练配置差异：~400 vs ~70K instances, 不同 lr, variant-level labels\n   - Mixed precision：bfloat16 vs NF4 seeds 的处理\n   - 14B scaling：仅 1 model family (Qwen3), 3 seeds\n\n3. **Threats to Validity**\n   - 5 个 confound 的评估是否充分\n   - Preprocessing-checkpoint confound chain\n   - Synthetic mutation → real fault 的外部效度\n   - Evaluation sequence length 对 CWM 的影响\n\n4. **统计 Claims 的严谨性**\n   - Abstract/Conclusion 中的 claims 是否有统计支撑\n   - \"collapses\"、\"driven by format collapse\" 等因果措辞\n   - 14B \"capacity-dependent convergence\" 的证据强度\n   - z=-23.7 interaction test 的适用范围（仅 DeepSeek-Coder）\n\n请按以下格式输出审稿意见：\n\n### Summary（2-3 句）\n### Strengths（逐条）\n### Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）\n### Questions（给作者的问题）\n### Missing References\n### Overall Assessment（评分 + 置信度 + 理由）\n### Detailed Comments（逐节）"
  }
}
```

</details>

---


### Tool result

_source line 1267 · 2026-05-23T14:22:59.973964+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17231
}
```

</details>

---


### Tool call

_source line 1268 · 2026-05-23T14:23:00.729150+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题：A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_13/submitted.pdf\n\n## Venue 要求（实时搜索确认）\n- **EMNLP 2026**，通过 ARR 统一审稿\n- **正文 8 页**（不含 references、limitations、ethical considerations）\n- **ACL 模板**（\\usepackage[review]{acl}）\n- **Double-blind**：无作者信息，避免自引暴露身份\n- **ARR Checklist**：在 OpenReview submission form 填写，不在 PDF 中\n- **Deadline**：2026-05-25（ARR May cycle）\n- **评分标准**：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n重点审查以下方面：\n\n1. **新颖性与贡献**\n   - 核心贡献是 systematic comparison——这是否足够 EMNLP Main？是否更适合 Findings？\n   - 三项贡献的独立性和价值\n   - Failure mode taxonomy 的可迁移性和诊断价值\n   - Error complementarity 作为 negative result 的 framing\n   - 与 GenRM (Hosseini et al., 2025) 的领域对比发现的深度\n   - 14B capacity-dependent convergence 作为 preliminary observation 的价值\n\n2. **Related Work 完整性**\n   - Execution simulation: CWM, Self-Execution, CodeMind, CRUXEval, RepoExec\n   - Process vs Outcome supervision: PRM/ORM mapping\n   - Code verification: LEVER, CodeT, SWE-RM, CodeScaler, CodeRM\n   - Repair and mutation testing\n   - 是否遗漏 2025-2026 年重要相关工作\n\n3. **写作质量与论文结构**\n   - Abstract（≤200 words 限制）：信息密度、统计符号密度、可读性\n   - Introduction 的 narrative flow 和 contribution statement\n   - Method section 的 Expected Failure Modes 定位\n   - Experiments section 的组织和叙事\n   - Conclusion + Limitations 的 hedging 是否充分\n   - Appendix 结构和导航\n\n4. **格式合规**\n   - 正文是否在 8 页内\n   - Double-blind 合规（无自引暴露）\n   - Limitations section 是否在正文中（非 appendix）\n   - Appendix 中是否有违规的 limitations section\n   - Table/Figure 格式、caption 质量\n   - 引用格式一致性\n\n请按以下格式输出审稿意见：\n\n### Summary（2-3 句）\n### Strengths（逐条）\n### Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）\n### Questions（给作者的问题）\n### Missing References\n### Overall Assessment（评分 + 置信度 + 理由）\n### Detailed Comments（逐节）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题：A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_13/submitted.pdf\n\n## Venue 要求（实时搜索确认）\n- **EMNLP 2026**，通过 ARR 统一审稿\n- **正文 8 页**（不含 references、limitations、ethical considerations）\n- **ACL 模板**（\\usepackage[review]{acl}）\n- **Double-blind**：无作者信息，避免自引暴露身份\n- **ARR Checklist**：在 OpenReview submission form 填写，不在 PDF 中\n- **Deadline**：2026-05-25（ARR May cycle）\n- **评分标准**：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n重点审查以下方面：\n\n1. **新颖性与贡献**\n   - 核心贡献是 systematic comparison——这是否足够 EMNLP Main？是否更适合 Findings？\n   - 三项贡献的独立性和价值\n   - Failure mode taxonomy 的可迁移性和诊断价值\n   - Error complementarity 作为 negative result 的 framing\n   - 与 GenRM (Hosseini et al., 2025) 的领域对比发现的深度\n   - 14B capacity-dependent convergence 作为 preliminary observation 的价值\n\n2. **Related Work 完整性**\n   - Execution simulation: CWM, Self-Execution, CodeMind, CRUXEval, RepoExec\n   - Process vs Outcome supervision: PRM/ORM mapping\n   - Code verification: LEVER, CodeT, SWE-RM, CodeScaler, CodeRM\n   - Repair and mutation testing\n   - 是否遗漏 2025-2026 年重要相关工作\n\n3. **写作质量与论文结构**\n   - Abstract（≤200 words 限制）：信息密度、统计符号密度、可读性\n   - Introduction 的 narrative flow 和 contribution statement\n   - Method section 的 Expected Failure Modes 定位\n   - Experiments section 的组织和叙事\n   - Conclusion + Limitations 的 hedging 是否充分\n   - Appendix 结构和导航\n\n4. **格式合规**\n   - 正文是否在 8 页内\n   - Double-blind 合规（无自引暴露）\n   - Limitations section 是否在正文中（非 appendix）\n   - Appendix 中是否有违规的 limitations section\n   - Table/Figure 格式、caption 质量\n   - 引用格式一致性\n\n请按以下格式输出审稿意见：\n\n### Summary（2-3 句）\n### Strengths（逐条）\n### Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）\n### Questions（给作者的问题）\n### Missing References\n### Overall Assessment（评分 + 置信度 + 理由）\n### Detailed Comments（逐节）"
  }
}
```

</details>

---


### Tool result

_source line 1269 · 2026-05-23T14:23:02.189511+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1460
}
```

</details>

---


### Assistant

_source line 1270 · 2026-05-23T14:23:16.758180+00:00_

已完成 Step 0-1 全部派发：

| 任务 | 状态 |
|------|------|
| Visual Check Agent | ✅ 已启动（fire-and-forget） |
| Reviewer 1（方法严谨性 + 实验设计） | ✅ Round 1 已分配 |
| Reviewer 2（新颖性 + 完整性 + 写作质量） | ✅ Round 1 已分配 |
| 外部审稿 | ⬜ 未启用 |

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 109

## Round 109

2 recorded events


### User

_source line 1271 · 2026-05-23T14:29:02.629007+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：A Systematic Comparison of Execution-Free Verification Formulations for Code Repair

## Summary（2-3句）

本文系统比较了三种无执行代码修复验证方案（CLS/CWM/TRAJ），在两个LLM家族、两个复杂度层级、≤8B LoRA微调条件下进行匹配实验。Function-level下CLS与CWM通过TOST等价检验（±2pp），但repo-level下差距扩大至18-26pp，主要归因于CWM的格式崩溃。统计框架（TOST+Bayesian ROPE+clustered bootstrap+mixed-effects regression）比同类工作更为严谨，但若干核心claim的统计支撑存在重要缺口。

---

## Strengths（逐条）

**S1. 匹配实验设计是真正的贡献。** 通过固定模型容量、训练数据、评估基准，仅改变验证公式，实现了formulation之间的公平比较。这在prior work（均使用不同模型/数据/评估协议）中是第一次。(§1, §3)

**S2. 统计方法论的深度超越同类论文。** TOST等价检验+Holm-Bonferroni校正+Bayesian ROPE+clustered bootstrap+ICC/DEFF计算+mixed-effects LPM/logistic regression robustness check——这套组合拳在NLP/SE会议论文中极为罕见，且各工具的使用基本正确。(§3.2, §3.4, Appendix J-M)

**S3. Failure mode taxonomy提供可操作的诊断信息。** 将三种formulation的失败模式（token-budget exhaustion, format collapse, decision collapse, aggregation penalty）分类清晰，对实践者选择验证方案有直接指导价值。(§2.2, §3.6, Table 4)

**S4. 透明度高。** 论文坦诚报告了低power（~0.3）、非pre-registered SESOI、NaN val loss导致的checkpoint选择差异、NF4 mixed precision等限制，未试图掩盖。(§3.4, Appendix O, Limitations)

**S5. 错误互补性分析增加实际价值。** Oracle combination达到90.63%（+2.30pp），simple routing heuristic捕获<0.4pp的oracle gap（Appendix N），为ensemble/routing方向提供了基线。(§3.6, Appendix A)

---

## Weaknesses（逐条）

### Must-Fix 问题

**W1 [Must-Fix] TOST SESOI（±2pp）的选择是post-hoc的，且等价结论对此高度敏感。**
- 具体位置：§3.2 (p.5), §3.4 (p.5), Appendix J (p.18), Table 13 (p.18)
- 问题：±2pp SESOI未pre-register（论文承认），且Table 13的sensitivity analysis显示：在±1.0pp时TOST不显著（p=0.054），在±1.5pp时刚好边界通过（p=0.027但Holm校正后仅p=0.075达不到显著）。只有在±2.0pp时才确认等价。论文的核心claim——"CLS and CWM are statistically equivalent"——完全依赖于这个post-hoc选择的阈值。
- 在代码验证场景中，2pp对应约38个额外错误（across 1,890 tests）。对于安全关键的代码修复任务，这是否真的"practically equivalent"需要更强的领域论证。论文仅说"set based on deployment relevance"（p.18），但未提供具体的deployment场景分析。
- 建议：(1) 在正文（而非仅附录）明确报告sensitivity analysis结果，说明等价结论在±1.5pp时不成立；(2) 提供更具体的领域论证为什么2pp是合理阈值；(3) 考虑将主要claim改为"CLS-CWM gap is within 2pp at function level"而非"statistically equivalent"。

**W2 [Must-Fix] 低统计power（~0.3）严重削弱多项非显著性结论的信息含量。**
- 具体位置：§3.4 (p.5-6), Appendix K (p.18-19)
- 问题：
  - Function-level 3-seed比较的power仅~0.3（p.5），意味着70%的概率漏检真实差异。
  - Repo-level更严重：ICC=0.3116, DEFF=11.4, n_eff≈7.5, MDE≈25pp（Appendix K, p.19）。在这种power下，repo-level的任何非显著结果都几乎没有信息量。
  - 论文在repo-level使用"equivalence collapses"（abstract, p.1）和"divergence"等强措辞来描述观察到的大差距，但同时又在其他地方依赖非显著性检验。这种"显著时用显著性、不显著时用描述性"的双标准需要更一致地处理。
- 建议：(1) 在正文中报告repo-level的effective sample size和MDE，让读者理解该层级推断的局限；(2) 对于power<0.5的比较，明确说明结果是"inconclusive"而非暗示某种方向。

**W3 [Must-Fix] CWM repo-level退化的confound chain未被实验性地解耦。**
- 具体位置：Appendix O (p.20-22), Table 16 (p.21)
- 问题：论文识别了5个潜在confound（checkpoint selection, TRAJ training regime, evaluation sequence length, CWM preprocessing, mixed precision），但每个confound只通过单独的ablation部分解决。这些confound之间存在链式依赖：
  - CWM的NaN val loss → 被迫使用final epoch checkpoint（而非val-selected）→ 可能选了一个过拟合或欠优化的模型
  - CWM的max_new_tokens=512限制 → 在repo-level可能截断trace → 导致unparseable rate上升
  - 这两个confound联合作用可能解释CWM repo-level的大部分退化，而无需诉诸"formulation-level"差异。
  - Table 16（p.21）的convergence analysis仅覆盖Qwen3-8B的3个seeds，且显示val-selected checkpoint仍不能恢复accuracy。但这个ablation没有同时控制sequence length和preprocessing，无法排除联合效应。
- 建议：(1) 补充CWM在更长max_new_tokens下的repo-level实验（即使只有1-2个seed作为pilot）；(2) 更明确地区分"CWM formulation本身的局限"和"当前CWM实现的工程限制"。

### Should-Fix 问题

**W4 [Should-Fix] TRAJ的训练数据量差异（~400 vs ~70K instances）混淆了formulation效果与数据量效果。**
- 具体位置：Table 11 (p.14), Appendix B1, Appendix O2 (p.21-22)
- 问题：CLS/CWM使用~70K per-test instances训练，TRAJ使用~400 variant-level instances（175×差异）。论文认为这是"inherent to the formulation"（p.22），因为TRAJ将所有tests打包为一个instance。这个论点成立，但意味着CLS-TRAJ的比较测试的是"formulation + 其固有的数据效率"的联合效应，而非纯粹的formulation差异。
  - Appendix B1的downsampling ablation控制了数据量但未控制label granularity（per-test vs variant-level），因此只部分解决了这个confound。
- 建议：在讨论CLS-TRAJ差异时，更明确地说明是在比较"formulation在其自然数据条件下的表现"，避免暗示差异纯粹来自formulation本身。

**W5 [Should-Fix] 14B "capacity-dependent convergence"基于单一模型家族、3个seeds，证据强度不足以支撑该理论性claim。**
- 具体位置：§3.3 (p.5), Table 2 (p.5), Abstract
- 问题：14B结果仅来自Qwen3的3个seeds（42, 123, 456），使用bfloat16推理。"Capacity-dependent convergence"暗示一个普遍的scaling规律，但n=3的单家族数据无法支撑这种泛化。
  - 论文在abstract中说"a preliminary observation consistent with capacity-dependent convergence"，但在§3.3中说"consistent with capacity-dependent convergence"时没有加"preliminary"限定。
  - Gap从1.32pp（4B）到2.62pp（8B）再到1.07pp（14B）的非单调模式也与简单的"capacity→convergence"叙事不完全一致。
- 建议：(1) 全文一致使用"preliminary"限定；(2) 讨论8B处gap扩大然后14B收窄的非单调模式可能的解释。

**W6 [Should-Fix] Mixed-effects LPM中z=-23.7的交互效应统计量可能因模型假设违背而膨胀。**
- 具体位置：Appendix M (p.20)
- 问题：Linear Probability Model对二元因变量会产生异方差，可能导致z-statistics膨胀。论文做了logistic regression robustness check确认方向一致（"confirmed below"），但未报告logistic regression下的具体z值/OR。如果logistic regression的z值远小于23.7，说明LPM的极端z值确实是模型假设违背的artifact。
  - 此外，25-cluster的random intercept结构下，cluster数量较少可能影响标准误估计。
- 建议：在Appendix M中并列报告LPM和logistic regression的coefficient/SE/z-value，让读者判断结论的稳健性。

**W7 [Should-Fix] CWM checkpoint选择confound的ablation范围太窄。**
- 具体位置：Appendix O1 (p.21), Table 16 (p.21)
- 问题：Table 16的convergence analysis仅覆盖Qwen3-8B的3个seeds和DeepSeek CLS+23作为对比。但CWM的NaN val loss问题也影响DeepSeek-Coder的CWM runs，而DeepSeek-Coder恰好是CLS-CWM gap最大的家族（2.69pp vs <1pp on Qwen3, see §3.2）。未对DeepSeek-Coder CWM做convergence analysis，leaves the most affected configuration unexamined。
- 建议：补充DeepSeek-Coder CWM的checkpoint convergence分析，或明确说明为什么只分析Qwen3。

### Minor 问题

**M1 [Minor] "Collapses"和"driven by format collapse"是因果措辞，但证据是描述性的。**
- Abstract中"equivalence collapses"和§3.5中"driven by format collapse"暗示因果关系。实际上，格式崩溃与accuracy退化的共现不等于因果。建议改为"accompanied by"或"coincides with"。

**M2 [Minor] Figure 2 y轴未从0开始。**
- 论文已注明"y axis does not start at zero"（p.5 caption），这是好的做法。但视觉上仍可能夸大4B→14B的收敛效果。

**M3 [Minor] "Equivalence"与"parity"两个术语混用。**
- 论文中有时用"equivalence"（统计意义上的TOST等价），有时用"parity"（非正式的相近）。在TRAJ讨论中，"TRAJ parity is model-contingent"（p.5）用了"parity"而非"equivalence"，但§3.4中又说"TRAJ equivalence"。建议统一术语。

**M4 [Minor] Appendix过长（15页）可能超出reviewer耐心。**
- 附录内容丰富且有价值，但15页的附录（A-P+extended analysis）在审稿过程中可能难以被完整阅读。关键的sensitivity analysis（Table 13）、power analysis结果应被提升到正文。

---

## Questions（给作者的问题）

**Q1.** Table 13中，如果pre-register ±1.5pp作为SESOI（在代码验证中可能更合理的阈值），CLS-CWM等价结论就不成立。作者能否提供具体的deployment场景来论证为什么±2pp而非±1.5pp是正确的阈值？

**Q2.** CWM在repo-level的NaN val loss问题是否与训练数据中repo-level样本的sequence length分布有关？如果是，这是否表明CWM formulation本身对长序列的不适应，还是仅仅是当前LoRA训练的工程问题？

**Q3.** TRAJ使用variant-level labels（~400 instances），如果改为per-test labels并相应增加训练数据量（与CLS匹配），是否预期会改变CLS-TRAJ的比较结论？作者是否尝试过这个ablation？

**Q4.** 14B实验中gap从8B的2.62pp收窄到1.07pp。但4B的gap是1.32pp，低于8B。这种非单调模式如何与"capacity-dependent convergence"叙事一致？是否有其他解释（如Qwen3-4B和14B的架构差异、训练数据差异）？

**Q5.** Appendix M的LPM分析中z=-23.7，对应的logistic regression z值是多少？如果差异显著，作者倾向于信任哪个结果？

**Q6.** 错误互补性分析（§3.6）中，simple routing heuristic仅捕获<0.4pp的oracle gap。这是否说明三种formulation的错误模式虽然在类别上不同，但在instance level上高度重叠？

---

## Missing References

- Arcuri & Briand (2011), "A practical guide for using statistical tests to assess randomized algorithms in software engineering" — 论文的统计方法论会受益于引用SE领域的统计测试指南
- 论文已引用的统计文献（Wellek 2010, Cohen 1988, Kruschke 2013/2018, Cameron & Miller 2008）覆盖面较好，无明显遗漏

---

## Overall Assessment

**Overall**: 3.5 / 5（Borderline Conference）
**Confidence**: 4 / 5（Quite sure — 统计方法论是我的审查重点，我仔细检查了每个统计claim）

**一句话总结**: 匹配实验设计和统计框架是真正的贡献，但核心等价claim依赖post-hoc SESOI选择，repo-level结论受限于低power和未解耦的confound chain。

### 评分理由

**升档因素（→ Conference）**:
- 首个系统匹配比较，填补明确的文献空白
- 统计方法论的深度和透明度远超同类工作
- Failure mode taxonomy的实践价值
- 23页附录体现了极高的实验透明度

**降档因素（→ Findings）**:
- 核心等价claim的统计支撑fragile（SESOI sensitivity）
- Repo-level结论受三重confound chain影响且power极低
- 14B scaling claim基于n=3单家族数据
- 部分因果措辞（collapses, driven by）超出证据支撑范围

综合评估：论文的实验设计和统计意识值得肯定，但3个must-fix问题（SESOI sensitivity、low power、confound chain）如果不解决，核心claim的可信度不足以支撑主会议接收。如果作者能(1)在正文中transparent地报告SESOI sensitivity、(2)将repo-level claims降级为descriptive observations并报告effective sample size、(3)至少用pilot实验部分解耦CWM confound chain，本文有望达到Conference水平。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计框架设计优秀但SESOI post-hoc选择和low power削弱核心claims；confound chain未实验性解耦 |
| Excitement | 3/5 | 首个匹配比较是有价值的贡献，但结果部分可预期（CLS在简单任务上够用、CWM在复杂任务上格式崩溃）；14B scaling太初步 |
| Overall Assessment | 3.5/5 | Borderline Conference——方法论和透明度突出，但统计claim的robustness需加强 |
| Confidence | 4/5 | 仔细审查了所有统计方法和claims，统计方法论是本reviewer的强项 |
| Reproducibility | 4/5 | 详细的hyperparameters（Table 11）、seeds、prompt templates（Appendix F）、compute budget；代码未公开但信息充分 |

---

## Detailed Comments（逐节）

### Abstract
- 约200 words，符合要求
- "statistically equivalent (TOST p=0.007, 5 seeds)" — 应提及SESOI=±2pp以让读者判断实际意义
- "equivalence collapses" — 建议改为"diverges"以避免因果暗示

### §1 Introduction
- 清晰地motivate了问题：practitioners面临formulation选择但缺乏匹配比较
- "inherently confounded" 对 TRAJ 的描述准确且重要
- Footnote 1 引用per-instance costs合理

### §2 Method
- §2.1 三种formulation的定义清晰
- §2.2 Failure mode taxonomy设计合理，three failure modes × three formulations的矩阵组织有效
- §2.3 Oracle Accuracy-Utility Framework的F2P分析有价值，但Appendix A显示实际优势集中在T=1（55.3%），应在正文提及这个limitation

### §3 Experiments
- §3.1 实验设置描述充分；"†" 标记DeepSeek的不同训练配置是好的做法
- §3.2 Function-level equivalence: TOST p=0.007 with SESOI=±2pp。Bayesian ROPE confirms (P(ROPE)=0.975)。CLS-TRAJ non-confirmation适当处理。但应将Table 13的sensitivity analysis从Appendix提升到正文。
- §3.3 Scaling behavior: Figure 2有效但y轴截断。14B结论需更多qualification。
- §3.4 Function-Level Equivalence的"523 variant-level instances across five seeds"——说明variant-level分析的sample size。SESOI=2pp在此粒度下合理吗？
- §3.5 Repo-Level Results: "Few-shot prompting (3-shot ICL) collapses to majority baseline 54.17%" — 这是一个有力的发现，强化了fine-tuning的必要性。"Formulation divergence" subsection的描述性分析有说服力。
- §3.6 Analysis: Failure mode taxonomy的repo-level分解（Table 4）信息密度高。"Decision collapse is configuration-dependent, not a late-training artifact" — 基于cross-model validation的证据。

### §4 Related Work
- 覆盖面适当：execution simulation, outcome supervision, PRM/ORM, mutation testing
- 与Raffel et al. (2020) task framing的联系有见地

### §5 Conclusion
- "Three directions" (complexity-aware routing, 32B+ scaling, per-test diagnostics) 具体可行
- Limitations section适当简短，覆盖了关键限制

### Appendix
- Appendix A (Oracle Accuracy-Utility): F2P analysis有价值
- Appendix B (Ablation Studies): LoRA rank ablation (Table 6) 确认rank-32 sufficient
- Appendix C (Repo-Level Per-Mutation Breakdown): Tables 8-9 有用
- Appendix I (Extended Analysis): §(a)-(k) 覆盖了大量robustness checks，值得肯定
- Appendix J (TOST Margin Sensitivity): Table 13是关键结果，应在正文引用
- Appendix K (Variant-Level Effect Sizes): MDE~25pp的报告是好的做法
- Appendix L (Multiple Comparison Correction): Table 15清晰
- Appendix M (Mixed-Effects Regression): 需要补充logistic regression的具体数值
- Appendix N (CWM Parseable Bias Analysis): 重要发现——CWM的accuracy被easy instances inflated
- Appendix O (Threats to Validity): 5个confound的识别全面，但实验性解耦不充分


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1272 · 2026-05-23T14:29:12.807421+00:00_

Reviewer 1 审稿意见已收到。评分 3.5/5（Borderline Conference），3 个 Must-Fix + 4 个 Should-Fix + 4 个 Minor。核心关切集中在 SESOI post-hoc 选择敏感性、低 power 下非显著性结论的信息量、以及 CWM confound chain 未实验性解耦。

等待 Reviewer 2 完成审稿后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 110

## Round 110

2 recorded events


### User

_source line 1273 · 2026-05-23T14:29:15.589682+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：

- **Overall 3.5/5（Borderline Conference）**，Soundness 3.5, Excitement 3, Confidence 4
- **3个Must-Fix**：(1) TOST ±2pp SESOI是post-hoc选择且等价结论对此高度敏感（±1.5pp时不成立）；(2) ~0.3 power严重削弱repo-level和TRAJ相关结论的信息量；(3) CWM repo-level退化的confound chain（checkpoint selection + sequence length + preprocessing）未被实验性解耦
- **4个Should-Fix**：TRAJ训练数据量差异、14B claim证据不足、LPM z=-23.7可能膨胀、CWM checkpoint ablation范围太窄
- **核心判断**：匹配实验设计和统计框架是真正的贡献且透明度极高，但核心等价claim的statistical robustness不足以支撑主会议接收，若修复3个must-fix有望升至Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1274 · 2026-05-23T14:29:25.172021+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 111

## Round 111

6 recorded events


### User

_source line 1275 · 2026-05-23T14:30:18.109533+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见（Round 1）
## 审查侧重：新颖性 + 完整性 + 写作质量

**论文**：A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
**Venue**：EMNLP 2026 (via ACL ARR May 2026 cycle)

---

### Summary（2-3 句）

本文首次在匹配实验条件下（相同模型家族、训练数据、LoRA 微调）系统比较了三种 execution-free 代码修复验证方案（CLS/CWM/TRAJ）。核心发现是 formulation choice 受代码复杂度调节：function level 等价，repo level 在 ≤8B LoRA 条件下 CLS 大幅优于 CWM（18-26pp）。论文方法论扎实（TOST 等价检验、Holm-Bonferroni 校正、Bayesian ROPE），附录详尽，但所有 repo-level 结论都受限于 ≤8B LoRA 这一前提，14B 初步结果（gap → 1.07pp）暗示 divergence 可能是 capacity artifact。

---

### Strengths（逐条）

**S1. 严谨的实验方法论。** TOST 等价检验（而非仅依赖 non-significance）、Holm-Bonferroni 多重比较校正、clustered bootstrap（保持问题内相关性）、Bayesian ROPE 互补验证——这套统计框架在 NLP 实证研究中罕见，具有方法论示范价值。Equivalence testing 的引入（§3.3）尤其重要：它区分了"没有证据表明不同"和"有证据表明等价"，这是很多 comparison paper 忽略的关键区别。

**S2. 全面的 ablation 和 threat analysis。** Appendix B-P 涵盖了 LoRA rank、majority voting、relaxed matching、sequence length、checkpoint selection、preprocessing、downsample 等 ablation，且 §3.5 Threats to Validity 诚实地列出五个 confound 并逐一评估影响范围。这种透明度超过了该领域的平均水平。

**S3. Failure mode taxonomy（Table 4）具有诊断价值。** Format collapse / decision collapse / aggregation penalty 三类 failure mode 在 repo-level 的识别是可操作的——practitioner 可以据此选择 formulation 或设计 pipeline 预检机制。

**S4. Domain-specific 发现有理论贡献。** GenRM (Hosseini et al., 2025) 在 math reasoning 中显示 generative verifier 优于 discriminative；本文在 code verification 中发现相反方向（CWM ≤ CLS），并给出结构性解释（code 需要 exact-match ~477 tokens vs math 需要 reasoning chain）。PRM/ORM 到 CLS/TRAJ 的映射（§4 Related Work）也有概念贡献。

**S5. 复现性高。** 完整的超参数表（Appendix E）、prompt 模板（Appendix F）、种子选择策略、compute budget（~370 GPU-hours, RTX 5090）均有详细记录。

---

### Weaknesses（逐条，标注严重程度）

**N1 [Must-Fix] 规模限制从根本上约束了核心 claim 的泛化性。**
- 具体位置：全文，尤其 §3.4, §3.5, §5 Conclusion
- 问题：所有 repo-level 结论都条件于 ≤8B LoRA 微调。§3.2 的 14B 结果已经显示所有 formulation 收敛至 1.07pp 以内（Table 2），这强烈暗示 repo-level 的 18-26pp divergence 是 capacity artifact 而非 formulation-inherent property。论文的标题和 abstract 未充分传达这一条件性——读者初读会认为 "formulation choice matters at repo level" 是一般性结论，而实际上它可能仅在小模型下成立。
- 为什么影响接收：如果核心发现在 practitioner 实际使用的规模（32B+）下不成立，则论文的实用价值大幅降低。14B convergence 趋势（3.11pp → 2.24pp → 1.07pp，monotonic）几乎可以预测 32B 下 gap → 0。
- 建议修改方向：(1) 在标题或 abstract 中明确 "under ≤8B LoRA" 的条件限定；(2) 将 14B convergence 从 "preliminary observation" 提升为与 repo-level divergence 并列的核心发现，正面讨论 "formulation choice may be scale-contingent" 而非作为 limitation 处理；(3) 如果有条件，补充 32B 哪怕 1-2 seed 的 repo-level 结果。

**N2 [Must-Fix] CWM baseline 与原始 CWM 差异过大，"domain difference" claim 缺乏支撑。**
- 具体位置：§3.5 Threats (CWM scale and pretraining), §5 Conclusion 第一段
- 问题：论文的 CWM baseline 是 4-8B LoRA 微调，无 execution trace pretraining。原始 CWM (Meta, 2025) 使用 32B + mid-training on execution traces。论文在 Conclusion 中声称 "This contrasts with mathematical reasoning, where generative verification outperforms discriminative"——但这个对比建立在一个 severely underpowered CWM 实现上。repo-level CWM 的 54-74% unparseable rate 和 38-43% parseable accuracy 可能只是说明 ≤8B 模型缺乏生成长 execution trace 的能力，而非 formulation 本身的缺陷。
- 为什么影响接收：如果 "code vs math domain difference" 的 claim 不成立（仅仅是 scale 不足），则三个贡献中有一个被削弱。Appendix (k) 将 CWM 类比为 chain-of-thought verifier 并得出 "CoT-style verification does not outperform direct classification" 的结论，同样受此 confound 影响。
- 建议修改方向：将 §5 Conclusion 中的 domain-difference claim 改为条件性陈述（"Under ≤8B LoRA without trace pretraining, ..."），避免暗示这是 formulation-level 的一般性结论。

**N3 [Must-Fix] TRAJ 比较根本性混淆，无法做出有效 attribution。**
- 具体位置：§3.1 (training regime difference), §3.5 Threats (TRAJ training regime), Appendix O (downsample)
- 问题：TRAJ 使用完全不同的训练配置：~400 variant-level 样本 vs ~70K per-test 样本，不同学习率（2×10⁻⁴ vs 5×10⁻⁵），variant-level labels vs per-test labels。Downsample ablation 控制了 data volume 但未控制 label granularity——论文自己承认这一 confound "cannot be experimentally resolved"（§3.5）。然而论文仍在 Table 1 和 §3.2 中将 TRAJ 与 CLS/CWM 并列比较并讨论 equivalence。
- 为什么影响接收：当 confound 无法分离时，claim 不应该被作为正面结果呈现。CLS-TRAJ equivalence 检验（TOST p=0.025, Holm-adjusted p=0.075, not confirmed）的结论是正确的，但读者可能认为 non-confirmation 反映真实差异，而实际上可能仅反映训练条件差异。
- 建议修改方向：明确将 TRAJ 比较定位为 "exploratory, inherently confounded by training regime"，并在 Table 1 caption 和 contribution statement 中降低对 TRAJ 发现的 claim 强度。

**W1 [Should-Fix] Abstract 统计符号密度过高，损害可读性。**
- 具体位置：Abstract
- 问题：185 words 的 abstract 中包含 z=-23.7、TOST、3.11pp、1.07pp、≤8B LoRA、14B 等密集的统计/技术细节。对于不熟悉 TOST 的读者（NLP 社区大多数人），这些符号是不透明的。Abstract 应传达 "what and why"，不是 "exact test statistics"。
- 建议：保留核心数字（如 18-26pp gap），但去掉 z-statistic 和 TOST 等统计方法名，用自然语言描述方向和强度。

**W2 [Should-Fix] Error complementarity 作为贡献的实用价值存疑。**
- 具体位置：§3.6 Analysis (Error complementarity), Introduction contribution #2
- 问题：Oracle combination 显示 90.63% function-level 和 95.83% repo-level 的上界，但 "Simple routing heuristics capture <0.4pp of oracle advantage"（§3.6）——即实际可获取的 complementarity 几乎为零。此外，Appendix (j) 的 re-repair pilot 显示 per-test diagnostic feedback 对下游修复没有帮助（p=0.42, effect size ≈ 0）。两个结果共同表明 complementarity 既不可利用（routing），也不可转化（re-repair），削弱了其作为独立贡献的地位。
- 建议：将 error complementarity 重新定位为 "exploratory finding / negative result"，而非与 "complexity-moderated formulation choice" 和 "failure mode taxonomy" 并列的第二大贡献。

**W3 [Should-Fix] §2.2 Expected Failure Modes 的位置不当。**
- 具体位置：§2 Method, §2.2
- 问题：§2.2 在 Results 之前预测了实验结果（"generation-specific failures may compound, creating divergence"）。虽然这可以理解为 hypothesis-driven 写作，但在 Method section 中直接预测 outcome 容易让读者感到 confirmation bias——仿佛实验只是为了验证已知的结论。更成问题的是，§2.2 中的 complexity dependence 预测几乎就是 §3 的结果摘要。
- 建议：将 §2.2 改为纯理论分析（"each formulation's output complexity scales differently with..."），移除或弱化对实验结果的预测性陈述。

**W4 [Should-Fix] Table 3 (repo-level) 信息过载，多个 footnote 使结果难以解读。**
- 具体位置：Table 3 及其 caption/footnotes
- 问题：Table 3 的 caption 长约 100 words，包含 †、‡、◇、★ 四个脚注符号，且不同列使用不同的 seed 数量（1-3 seeds）、不同的 evaluation 方式（per-test vs variant），部分数值是 default-pass inflated（CWM 列）。读者需要反复交叉引用脚注才能理解每个数字的含义。
- 建议：拆分为两个表（per-test accuracy 和 variant-level accuracy），或至少将关键 caveats 移入正文讨论。

**W5 [Should-Fix] 缺少 execution-based verification 作为 upper bound。**
- 具体位置：§3 Experiments 全节
- 问题：论文比较三种 execution-free formulations，但未提供 execution-based verification（ground truth）的准确率作为 upper bound reference。虽然引言提到 execution verification 的成本（$1-3 per candidate），但不提供其准确率使读者无法判断 execution-free 方法还有多少提升空间。
- 建议：在 Table 1 或 Table 3 中加一行 "execution-based (oracle)" 的准确率。

---

### Questions（给作者的问题）

**Q1.** 14B 的 monotonic convergence（3.11pp → 2.24pp → 1.07pp）是否暗示在 32B 下所有 formulations 将完全等价？如果是，论文的 repo-level divergence 发现是否仅是 small-model regime 的 artifact？

**Q2.** 是否考虑过对 CWM 使用 constrained decoding（如 Outlines, 已在 Appendix (c) 提及但仅讨论了 relaxed matching）？Constrained decoding 可以完全消除 format collapse，从而隔离 semantic accuracy 的真实水平。

**Q3.** TRAJ 的训练数据仅有 ~400 variant-level 样本。是否尝试过用 per-test 数据训练 TRAJ（每个 test 独立预测 resolved/unresolved 后聚合）？这将控制 data volume 和 label granularity 两个 confound。

**Q4.** Appendix (j) 的 re-repair pilot 显示 per-test diagnostic 不帮助修复。这是否实际上削弱了 per-test verification（CLS 相比 TRAJ）的核心动机之一？

**Q5.** CWM 的 format collapse 从 training 早期就存在（step 400, ~6.5% of training, 63.7% unparseable）。这是否说明 LoRA 微调根本无法教会模型 repo-level 的 execution trace generation？如果 full fine-tuning 或 continued pretraining 可能解决这个问题，那么 conclusion 中关于 "generative formulation" 的一般性陈述需要大幅修改。

---

### Missing References

论文的 related work 覆盖面总体良好，但以下 2025-2026 年工作可能值得提及：

1. **RGD (Reward-Guided Decoding)** — 用 reward model 在 decoding 时引导 code generation，与本文的 verification-at-inference 框架相关但采用不同机制。
2. Frontiers survey "A dual perspective review on large language models and code verification" (2025) — 系统综述 LLM-based code verification 的分类框架，可能提供更完整的 formulation landscape。
3. 论文未引用 **OpenCodeInterpreter** (Zheng et al., 2024) 等将 execution feedback 集成到 generation loop 中的工作，作为 execution-based verification 的代表性方法之一。

以上均非 critical missing，不影响论文完整性。

---

### Overall Assessment

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 方法论扎实的实证比较研究，但核心发现受 ≤8B 规模限制约束严重，14B convergence 趋势暗示 repo-level divergence 可能仅是 capacity artifact。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 统计方法论优秀（TOST, Holm, ROPE），但 CWM 和 TRAJ 比较存在根本性 confound（scale mismatch, training regime），削弱了两个核心 claim 的因果推断 |
| Excitement | 2.5/5 | 问题本身 relevant（execution-free verification 是 active area），但 (a) 无新方法；(b) 核心发现可能 scale-contingent；(c) error complementarity 不可利用 |
| Reproducibility | 4/5 | 超参数、prompt template、seed、compute budget 详细记录；数据来自公开 benchmark。代码可用性未明确声明 |
| Confidence | 4/5 | 对 NLP 评估方法论和 code generation 有相关经验，仔细阅读了全文和附录 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] 规模限制约束核心 claim 的泛化性
- 具体位置：全文，尤其 §3.4, §3.5, §5
- 问题：所有 repo-level 结论条件于 ≤8B LoRA，14B 已显示 convergence（1.07pp），暗示 divergence 是 capacity artifact
- 为什么影响接收：如果 32B+ 下 formulation 等价，则论文的核心发现和实用价值大幅缩水
- 建议修改方向：标题/abstract 加条件限定；将 14B convergence 提升为核心发现；如可能补充 32B 数据

**N2** [critical] CWM baseline 过弱，"domain difference" claim 不可靠
- 具体位置：§3.5, §5 Conclusion
- 问题：4-8B LoRA CWM ≠ 原始 32B+trace-pretraining CWM；repo-level 54-74% unparseable 可能仅反映模型能力不足
- 为什么影响接收：code vs math 的 domain difference claim 建立在不公平比较之上
- 建议修改方向：所有 CWM 相关结论加 "under ≤8B LoRA without trace pretraining" 条件限定

**N3** [critical] TRAJ 比较因训练条件差异而根本性混淆
- 具体位置：§3.1, §3.5, Appendix O
- 问题：~400 vs ~70K 样本、不同学习率、不同 label granularity；downsample ablation 无法分离 label granularity confound
- 为什么影响接收：TRAJ 比较结果无法归因于 formulation 差异
- 建议修改方向：在贡献陈述和表格 caption 中明确标注 TRAJ 比较为 exploratory

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 统计符号密度过高
- 具体位置：Abstract
- 建议：去掉 z=-23.7、TOST 等，用自然语言描述

**W2** [warning] Error complementarity 作为第二大贡献缺乏实用价值
- 具体位置：Introduction contribution #2, §3.6
- 建议：降级为 exploratory finding

**W3** [warning] §2.2 Expected Failure Modes 预判实验结果
- 具体位置：§2.2
- 建议：弱化预测性陈述

**W4** [warning] Table 3 信息过载
- 具体位置：Table 3
- 建议：拆表或简化 footnotes

**W5** [warning] 缺少 execution-based verification upper bound
- 具体位置：§3 Experiments
- 建议：加入 oracle reference line

## 小问题（不影响接收）

- §3.2 Figure 2: 描述说 "y-axis does not start at zero" 但这在 PDF 中不够醒目，容易误读 gap 的视觉幅度
- Appendix overview (page 12 top) 使用字母编号 A-P，但实际 section 编号使用数字，产生双重编号混淆
- Table 1 中 TRAJ 的 ★ superscript 含义（"Training configuration differs"）需要读者跳到 §3.4 才能理解，应在 caption 中简要说明差异
- "format collapse" 既作为 taxonomy 的正式类别名（Table 4），又在多处作为非正式描述使用，建议统一术语用法

## 主要优势

- 方法论标准远超同类 comparison paper（TOST + Holm + Bayesian ROPE 三重验证）
- Threats to validity 分析的诚实和透明度值得认可
- Failure mode taxonomy（Table 4）具有直接的实践诊断价值
- GenRM-to-code 的 domain difference 发现是有价值的方向，尽管 claim 需要更多条件限定
- 附录质量高，几乎每个可能的质疑都有对应的 ablation 或 analysis

---

### Detailed Comments（逐节）

**Abstract**: ~185 words，符合 ≤200 word 限制。但信息密度极高，z=-23.7 和 TOST 对非统计背景读者不透明。建议第一段保持不变（清晰的 problem statement），第二段精简统计细节。

**§1 Introduction**: Narrative flow 清晰——从 cost 动机 → 三种 formulation → gap in comparison → 本文贡献。三个 contribution 的并列结构合理。但 contribution #1 的描述过长（一整段），可压缩。Raffel (2020) T5 formulation analogy 是好的 framing。

**§2 Method**: §2.1 形式化清晰，notation 一致。§2.2 的问题已在 W3 中讨论。§2.3 Oracle framework 的 ICC-adjusted detection model 是有意义的理论贡献，但在正文中的实际使用有限（主要在 Appendix A）。

**§3 Experiments**: 组织良好——从 function-level → scaling → equivalence → repo-level → analysis → threats。但 §3.6 Analysis 混合了多个子发现（aggregation penalty, generation degradation, error complementarity），可拆分为更细的 subsection。§3.5 Threats 在正文中给出了恰当长度的摘要，详细分析在 Appendix N。

**§4 Related Work**: 覆盖面良好。PRM/ORM 到 CLS/TRAJ 的映射（第二段）是概念贡献。三段结构（Execution Simulation, Process vs Outcome, Repair & Mutation Testing）合理。

**§5 Conclusion + Limitations**: Conclusion 第一段基本是结果重述，可更精简。"Three directions" 过于简略（每个方向仅几个词）。Limitations 覆盖了主要限制（scale, language, synthetic data），但 "cross-family replication at 32B+" 应放在更突出的位置，因为这直接关系到核心 claim 的泛化性。

**Appendix**: 质量高，结构合理（A-P 按主题组织）。Appendix E 超参数表、F prompt template 提供了完整的复现信息。Appendix N (Threats) 的 CWM convergence analysis（Table 14）和 preprocessing analysis 是重要的补充材料。

---

### 格式合规

| 检查项 | 结果 |
|--------|------|
| 正文 ≤8 页 | ✅ 正文约 8 页（Conclusion + Limitations 在 page 8 结束前） |
| Double-blind | ✅ "Anonymous ACL submission"，未见自引暴露 |
| Limitations 在正文中 | ✅ 在 §5 Conclusion 后，References 前 |
| Appendix 无 Limitations section | ✅ Appendix 有 "Extended validity discussion"（标题不含 "Limitations"） |
| Abstract ≤200 words | ✅ 约 185 words |
| ACL 模板 review mode | ✅ `\usepackage[review]{acl}` |
| ARR Checklist | ✅ 注释中说明在 OpenReview form 填写 |
| 引用格式 | ✅ 一致使用 `\cite` 和 `\citet` |

---

**总结**：这是一篇方法论扎实、实验严谨的 empirical comparison paper。其核心弱点在于 ≤8B 规模限制使主要发现的泛化性存疑——14B convergence 趋势几乎预判了更大规模下 formulation 差异将消失。如果作者能在 rebuttal 中 (a) 提供 32B 初步结果，或 (b) 给出理论论证说明 repo-level divergence 不会随规模消失，将显著增强论文的 contribution。目前评为 3.0 (Findings)。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-23T14:31:06.655441+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（Round 1）\n\n### Summary\n本文首次在匹配实验条件下系统比较了三种 execution-free 代码修复验证方案（CLS/CWM/TRAJ）。核心发现是 formulation choice 受代码复杂度调节：function level 等价，repo level 在 ≤8B LoRA 条件下 CLS 大幅优于 CWM（18-26pp）。方法论扎实但所有 repo-level 结论都受限于 ≤8B LoRA 前提，14B 初步结果暗示 divergence 可能是 capacity artifact。\n\n### Weaknesses\n\n**N1 [Must-Fix] 规模限制从根本上约束了核心 claim 的泛化性。**\n所有 repo-level 结论条件于 ≤8B LoRA。14B 结果已显示所有 formulation 收敛至 1.07pp 以内，强烈暗示 repo-level 的 18-26pp divergence 是 capacity artifact 而非 formulation-inherent property。标题和 abstract 未充分传达这一条件性。建议：标题/abstract 加条件限定；将 14B convergence 提升为核心发现；如可能补充 32B 数据。\n\n**N2 [Must-Fix] CWM baseline 与原始 CWM 差异过大，\"domain difference\" claim 缺乏支撑。**\nCWM baseline 是 4-8B LoRA 微调，无 execution trace pretraining。Conclusion 中 \"This contrasts with mathematical reasoning\" 建立在 severely underpowered CWM 上。repo-level 54-74% unparseable 可能仅反映模型能力不足。建议：将 domain-difference claim 改为条件性陈述。\n\n**N3 [Must-Fix] TRAJ 比较根本性混淆，无法做出有效 attribution。**\nTRAJ 使用 ~400 vs ~70K 样本、不同学习率、variant-level labels。Downsample ablation 无法分离 label granularity confound。论文仍在 Table 1 中将 TRAJ 与 CLS/CWM 并列比较。建议：明确将 TRAJ 比较定位为 exploratory。\n\n**W1 [Should-Fix] Abstract 统计符号密度过高。**\n185 words 中包含 z=-23.7、TOST、3.11pp、1.07pp 等密集统计细节。建议保留核心数字但去掉统计方法名。\n\n**W2 [Should-Fix] Error complementarity 作为贡献的实用价值存疑。**\nSimple routing heuristics capture <0.4pp of oracle advantage；re-repair pilot 显示 per-test diagnostic 不帮助修复（p=0.42）。建议降级为 exploratory finding。\n\n**W3 [Should-Fix] §2.2 Expected Failure Modes 预判实验结果。**\n在 Method 中直接预测 outcome 容易让读者感到 confirmation bias。建议弱化预测性陈述。\n\n**W4 [Should-Fix] Table 3 信息过载。**\nCaption ~100 words，4 个脚注符号，不同列使用不同 seed 数量。建议拆分或简化。\n\n**W5 [Should-Fix] 缺少 execution-based verification 作为 upper bound。**\n未提供 execution-based verification 准确率作为参考。建议加入 oracle reference。\n\n### Questions\nQ1. 14B monotonic convergence 是否暗示 32B 下 formulations 将完全等价？\nQ2. 是否考虑 constrained decoding 消除 CWM format collapse？\nQ3. 是否尝试用 per-test 数据训练 TRAJ？\nQ4. re-repair pilot 是否削弱 CLS 相比 TRAJ 的核心动机？\nQ5. CWM format collapse 从 training 早期就存在是否说明 LoRA 根本无法教会 repo-level trace generation？\n\n### Missing References\n1. RGD (Reward-Guided Decoding)\n2. \"A dual perspective review on large language models and code verification\" (2025)\n3. OpenCodeInterpreter (Zheng et al., 2024)\n\n### Overall: 3.0 (Findings), Soundness 3.0, Excitement 2.5, Confidence 4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（Round 1）\n\n### Summary\n本文首次在匹配实验条件下系统比较了三种 execution-free 代码修复验证方案（CLS/CWM/TRAJ）。核心发现是 formulation choice 受代码复杂度调节：function level 等价，repo level 在 ≤8B LoRA 条件下 CLS 大幅优于 CWM（18-26pp）。方法论扎实但所有 repo-level 结论都受限于 ≤8B LoRA 前提，14B 初步结果暗示 divergence 可能是 capacity artifact。\n\n### Weaknesses\n\n**N1 [Must-Fix] 规模限制从根本上约束了核心 claim 的泛化性。**\n所有 repo-level 结论条件于 ≤8B LoRA。14B 结果已显示所有 formulation 收敛至 1.07pp 以内，强烈暗示 repo-level 的 18-26pp divergence 是 capacity artifact 而非 formulation-inherent property。标题和 abstract 未充分传达这一条件性。建议：标题/abstract 加条件限定；将 14B convergence 提升为核心发现；如可能补充 32B 数据。\n\n**N2 [Must-Fix] CWM baseline 与原始 CWM 差异过大，\"domain difference\" claim 缺乏支撑。**\nCWM baseline 是 4-8B LoRA 微调，无 execution trace pretraining。Conclusion 中 \"This contrasts with mathematical reasoning\" 建立在 severely underpowered CWM 上。repo-level 54-74% unparseable 可能仅反映模型能力不足。建议：将 domain-difference claim 改为条件性陈述。\n\n**N3 [Must-Fix] TRAJ 比较根本性混淆，无法做出有效 attribution。**\nTRAJ 使用 ~400 vs ~70K 样本、不同学习率、variant-level labels。Downsample ablation 无法分离 label granularity confound。论文仍在 Table 1 中将 TRAJ 与 CLS/CWM 并列比较。建议：明确将 TRAJ 比较定位为 exploratory。\n\n**W1 [Should-Fix] Abstract 统计符号密度过高。**\n185 words 中包含 z=-23.7、TOST、3.11pp、1.07pp 等密集统计细节。建议保留核心数字但去掉统计方法名。\n\n**W2 [Should-Fix] Error complementarity 作为贡献的实用价值存疑。**\nSimple routing heuristics capture <0.4pp of oracle advantage；re-repair pilot 显示 per-test diagnostic 不帮助修复（p=0.42）。建议降级为 exploratory finding。\n\n**W3 [Should-Fix] §2.2 Expected Failure Modes 预判实验结果。**\n在 Method 中直接预测 outcome 容易让读者感到 confirmation bias。建议弱化预测性陈述。\n\n**W4 [Should-Fix] Table 3 信息过载。**\nCaption ~100 words，4 个脚注符号，不同列使用不同 seed 数量。建议拆分或简化。\n\n**W5 [Should-Fix] 缺少 execution-based verification 作为 upper bound。**\n未提供 execution-based verification 准确率作为参考。建议加入 oracle reference。\n\n### Questions\nQ1. 14B monotonic convergence 是否暗示 32B 下 formulations 将完全等价？\nQ2. 是否考虑 constrained decoding 消除 CWM format collapse？\nQ3. 是否尝试用 per-test 数据训练 TRAJ？\nQ4. re-repair pilot 是否削弱 CLS 相比 TRAJ 的核心动机？\nQ5. CWM format collapse 从 training 早期就存在是否说明 LoRA 根本无法教会 repo-level trace generation？\n\n### Missing References\n1. RGD (Reward-Guided Decoding)\n2. \"A dual perspective review on large language models and code verification\" (2025)\n3. OpenCodeInterpreter (Zheng et al., 2024)\n\n### Overall: 3.0 (Findings), Soundness 3.0, Excitement 2.5, Confidence 4"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-23T14:31:38.736535+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 32081
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-23T14:31:38.937998+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（Round 1）\n\n### Summary\n本文系统比较了三种无执行代码修复验证方案（CLS/CWM/TRAJ），统计框架（TOST+Bayesian ROPE+clustered bootstrap+mixed-effects regression）比同类工作更严谨，但若干核心claim的统计支撑存在重要缺口。\n\n### Weaknesses\n\n**W1 [Must-Fix] TOST SESOI（±2pp）的选择是post-hoc的，且等价结论对此高度敏感。**\n±2pp SESOI 未 pre-register。Table 13 sensitivity analysis 显示：±1.0pp 时不显著，±1.5pp 时边界。核心 \"statistically equivalent\" claim 完全依赖 post-hoc 阈值。2pp 对应约 38 个额外错误，在安全关键场景可能不 \"practically equivalent\"。建议：正文报告 sensitivity analysis；提供更具体 deployment 场景论证；考虑改为 \"gap is within 2pp\" 而非 \"equivalent\"。\n\n**W2 [Must-Fix] 低统计 power（~0.3）严重削弱多项非显著性结论的信息含量。**\nFunction-level 3-seed 比较 power 仅 ~0.3。Repo-level 更严重：DEFF=11.4, n_eff≈7.5, MDE≈25pp。\"显著时用显著性、不显著时用描述性\"的双标准。建议：正文报告 repo-level effective sample size 和 MDE；power<0.5 的比较明确为 \"inconclusive\"。\n\n**W3 [Must-Fix] CWM repo-level 退化的 confound chain 未被实验性解耦。**\n5 个 confound 每个只单独 ablation。NaN val loss → final epoch checkpoint，max_new_tokens=512 → truncation → unparseable rate 上升。联合作用可能解释 CWM 大部分退化。Table 16 convergence analysis 仅 Qwen3-8B 3 seeds 且未同时控制 sequence length 和 preprocessing。建议：补充 CWM 更长 max_new_tokens 实验；区分 formulation 局限 vs 工程限制。\n\n**W4 [Should-Fix] TRAJ 训练数据量差异混淆 formulation 效果与数据量效果。**\nCLS/CWM ~70K vs TRAJ ~400 instances（175×差异）。Downsample 控制了 volume 但未控制 label granularity。建议更明确说明比较的是 \"formulation 在其自然数据条件下的表现\"。\n\n**W5 [Should-Fix] 14B \"capacity-dependent convergence\" 基于单一模型家族、3 seeds。**\nGap 从 1.32pp(4B) → 2.62pp(8B) → 1.07pp(14B) 的非单调模式与简单 capacity→convergence 叙事不完全一致。建议全文一致用 \"preliminary\"。\n\n**W6 [Should-Fix] Mixed-effects LPM z=-23.7 可能因 LPM 假设违背而膨胀。**\nLPM 对二元因变量产生异方差。Logistic regression robustness check 未报告具体 z 值/OR。建议并列报告 LPM 和 logistic regression 数值。\n\n**W7 [Should-Fix] CWM checkpoint ablation 范围太窄。**\nTable 16 仅 Qwen3-8B。DeepSeek-Coder CWM gap 最大但未做 convergence analysis。建议补充 DeepSeek CWM checkpoint 分析。\n\n**M1 [Minor] \"Collapses\" 和 \"driven by\" 是因果措辞但证据是描述性的。**\n**M2 [Minor] Figure 2 y 轴未从 0 开始。**\n**M3 [Minor] \"Equivalence\" 与 \"parity\" 混用。**\n**M4 [Minor] Appendix 过长（15 页）。**\n\n### Questions\nQ1. 能否提供 deployment 场景论证 ±2pp 而非 ±1.5pp？\nQ2. CWM NaN val loss 是 formulation-inherent 还是工程问题？\nQ3. 是否尝试 per-test 数据训练 TRAJ？\nQ4. 4B→8B gap 扩大 + 14B 收窄的非单调模式如何解释？\nQ5. Logistic regression 的 z 值？\nQ6. Simple routing <0.4pp 是否说明错误在 instance level 高度重叠？\n\n### Missing References\n- Arcuri & Briand (2011) 统计测试指南\n\n### Overall: 3.5 (Borderline Conference), Soundness 3.5, Excitement 3, Confidence 4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（Round 1）\n\n### Summary\n本文系统比较了三种无执行代码修复验证方案（CLS/CWM/TRAJ），统计框架（TOST+Bayesian ROPE+clustered bootstrap+mixed-effects regression）比同类工作更严谨，但若干核心claim的统计支撑存在重要缺口。\n\n### Weaknesses\n\n**W1 [Must-Fix] TOST SESOI（±2pp）的选择是post-hoc的，且等价结论对此高度敏感。**\n±2pp SESOI 未 pre-register。Table 13 sensitivity analysis 显示：±1.0pp 时不显著，±1.5pp 时边界。核心 \"statistically equivalent\" claim 完全依赖 post-hoc 阈值。2pp 对应约 38 个额外错误，在安全关键场景可能不 \"practically equivalent\"。建议：正文报告 sensitivity analysis；提供更具体 deployment 场景论证；考虑改为 \"gap is within 2pp\" 而非 \"equivalent\"。\n\n**W2 [Must-Fix] 低统计 power（~0.3）严重削弱多项非显著性结论的信息含量。**\nFunction-level 3-seed 比较 power 仅 ~0.3。Repo-level 更严重：DEFF=11.4, n_eff≈7.5, MDE≈25pp。\"显著时用显著性、不显著时用描述性\"的双标准。建议：正文报告 repo-level effective sample size 和 MDE；power<0.5 的比较明确为 \"inconclusive\"。\n\n**W3 [Must-Fix] CWM repo-level 退化的 confound chain 未被实验性解耦。**\n5 个 confound 每个只单独 ablation。NaN val loss → final epoch checkpoint，max_new_tokens=512 → truncation → unparseable rate 上升。联合作用可能解释 CWM 大部分退化。Table 16 convergence analysis 仅 Qwen3-8B 3 seeds 且未同时控制 sequence length 和 preprocessing。建议：补充 CWM 更长 max_new_tokens 实验；区分 formulation 局限 vs 工程限制。\n\n**W4 [Should-Fix] TRAJ 训练数据量差异混淆 formulation 效果与数据量效果。**\nCLS/CWM ~70K vs TRAJ ~400 instances（175×差异）。Downsample 控制了 volume 但未控制 label granularity。建议更明确说明比较的是 \"formulation 在其自然数据条件下的表现\"。\n\n**W5 [Should-Fix] 14B \"capacity-dependent convergence\" 基于单一模型家族、3 seeds。**\nGap 从 1.32pp(4B) → 2.62pp(8B) → 1.07pp(14B) 的非单调模式与简单 capacity→convergence 叙事不完全一致。建议全文一致用 \"preliminary\"。\n\n**W6 [Should-Fix] Mixed-effects LPM z=-23.7 可能因 LPM 假设违背而膨胀。**\nLPM 对二元因变量产生异方差。Logistic regression robustness check 未报告具体 z 值/OR。建议并列报告 LPM 和 logistic regression 数值。\n\n**W7 [Should-Fix] CWM checkpoint ablation 范围太窄。**\nTable 16 仅 Qwen3-8B。DeepSeek-Coder CWM gap 最大但未做 convergence analysis。建议补充 DeepSeek CWM checkpoint 分析。\n\n**M1 [Minor] \"Collapses\" 和 \"driven by\" 是因果措辞但证据是描述性的。**\n**M2 [Minor] Figure 2 y 轴未从 0 开始。**\n**M3 [Minor] \"Equivalence\" 与 \"parity\" 混用。**\n**M4 [Minor] Appendix 过长（15 页）。**\n\n### Questions\nQ1. 能否提供 deployment 场景论证 ±2pp 而非 ±1.5pp？\nQ2. CWM NaN val loss 是 formulation-inherent 还是工程问题？\nQ3. 是否尝试 per-test 数据训练 TRAJ？\nQ4. 4B→8B gap 扩大 + 14B 收窄的非单调模式如何解释？\nQ5. Logistic regression 的 z 值？\nQ6. Simple routing <0.4pp 是否说明错误在 instance level 高度重叠？\n\n### Missing References\n- Arcuri & Briand (2011) 统计测试指南\n\n### Overall: 3.5 (Borderline Conference), Soundness 3.5, Excitement 3, Confidence 4"
  }
}
```

</details>

---


### Tool result

_source line 1279 · 2026-05-23T14:31:40.298464+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1360
}
```

</details>

---


### Assistant

_source line 1280 · 2026-05-23T14:31:44.012121+00:00_

交叉分享已发送给两位 Reviewer。等待交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 112

## Round 112

2 recorded events


### User

_source line 1281 · 2026-05-23T14:31:46.565218+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.0 (Findings)。

核心判断：
- **方法论优秀**（TOST + Holm + Bayesian ROPE 三重统计验证，在 NLP 中罕见），附录质量高
- **三个 Must-Fix 问题**：(1) ≤8B 规模限制使核心 claim 泛化性存疑——14B 已显示 convergence 至 1.07pp；(2) CWM baseline 与原始 32B CWM 差异过大，"code vs math domain difference" claim 不可靠；(3) TRAJ 比较因训练条件完全不同而根本性混淆
- **四个 Should-Fix**：abstract 统计密度过高、error complementarity 缺乏实用价值、§2.2 预判结果、Table 3 信息过载
- **格式合规**：全部通过（8 页正文、double-blind、Limitations 在正文中、abstract ≤200 words）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1282 · 2026-05-23T14:31:52.896024+00:00_

两位 Reviewer 的交叉分享已发送，等待回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 113

## Round 113

2 recorded events


### User

_source line 1283 · 2026-05-23T14:33:31.555062+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

**[REBUT] R2-N1: 规模限制从根本上约束了核心claim的泛化性**

R2认为14B收敛"strongly suggests repo-level divergence是capacity artifact"，建议将14B convergence提升为核心发现。我不完全同意：

1. **14B证据本身不足以支撑"capacity artifact"结论。** 14B结果仅来自Qwen3单一家族、3个seeds（§3.3, Table 2）。更重要的是，gap的轨迹是**非单调**的：4B=1.32pp → 8B=2.62pp → 14B=1.07pp（Table 2, p.5）。如果divergence纯粹是capacity artifact，应预期单调递减。8B处的peak反而暗示可能有其他因素（如Qwen3-8B与14B的架构/训练数据差异）在起作用。R2将一个n=3的preliminary观察直接升级为核心发现，恰恰犯了论文试图避免的过度推断。

2. **但论文确实应在title/abstract更明确地限定scope。** 当前abstract说"under our ≤8B LoRA protocol, this equivalence collapses"，条件限定存在但不够突出。标题"A Systematic Comparison..."给人全面比较的印象，但实际coverage只到14B且14B数据极为有限。我在自己的审稿中也指出14B claim需更多qualification（我的W5），但方向不同于R2——我认为应**弱化14B claim**而非提升它。

**结论：** 同意title/abstract需要更明确的scope限定（partial agree），但反对将14B convergence提升为核心发现——证据不足以支撑。

---

**[REBUT] R2-N2: CWM baseline与原始CWM差异过大**

R2认为CWM baseline因缺乏execution trace pretraining而"severely underpowered"，repo-level 54-74% unparseable可能仅反映模型能力不足。

1. **匹配设计是论文的核心方法论贡献，不是缺陷。** 论文在§3.1 (p.4)明确说明："Our CWM baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model (FAIR CodeGen team et al., 2025)." 论文的research question是"在控制模型容量、训练数据、评估协议的前提下，formulation本身是否产生差异"。如果使用原始32B CWM vs 4B CLS，观察到的差异无法归因于formulation（capacity、pretraining、training data都不同）。R2本质上是在要求一篇不同的论文。

2. **但Conclusion中的domain-difference claim确实过度。** §5 (p.8)中"This contrasts with mathematical reasoning, where generative verification outperforms classification"——这个claim建立在≤8B matched comparison上，泛化到domain-level差异确实证据不足。这里我同意R2的方向（我没有专门提但逻辑一致），建议改为条件性陈述。

3. **54-74% unparseable的诊断价值不应被忽视。** 即使我们接受这部分反映capacity限制，Appendix I (p.16-17)和Table 4 (p.7)的failure mode分析显示unparseable outputs中包含systematic patterns（hallucinated test names, repetitive loops, pytest import until truncation）——这些是formulation-specific的结构性问题，而非random capacity failures。CLS在同等capacity下不出现这类问题，说明formulation的output space structure确实与capacity需求交互。

**结论：** 匹配设计本身合理（rebut），但Conclusion的domain-difference claim应加条件限定（partial agree）。

---

**[AGREE] R2-N3: TRAJ比较根本性混淆**（部分同意，但程度不同）

我在自己的W4中已标记此问题为Should-Fix。同意TRAJ的~400 vs ~70K训练样本差异是重要confound，且downsample ablation（Appendix B1）仅控制数据量而未控制label granularity（per-test vs variant-level）。

**但不同意"根本性混淆、无法做出有效attribution"的极端表述。** 理由：

1. **数据效率是formulation的固有属性。** TRAJ将所有tests打包为一个instance，这导致~400 instances是formulation设计的直接后果，不是实验设计的疏忽（Appendix O2, p.21-22）。比较"formulation在其自然数据条件下的表现"本身有其validity——practitioners不会为了公平比较而人为拆分TRAJ的训练数据。

2. **论文已经做了合理的disclosure。** §3.4 (p.5-6)明确报告了TRAJ equivalence "not confirmed after multiple-comparison correction"，Appendix O2详细讨论了training regime confound。

3. **但应更显著地标记为exploratory。** 同意R2的建议：在Table 1的caption或正文中明确标注TRAJ比较为exploratory，避免读者误认为与CLS-CWM比较处于同等evidential status。

**结论：** 同意应更显著标记TRAJ比较的exploratory性质（agree on framing），但反对完全否定其informational value（rebut on substance）。

---

## Should-Fix 问题

**[REBUT] R2-W1: Abstract统计符号密度过高**

R2建议去掉统计方法名称，仅保留核心数字。作为方法论审查者，我认为：

- 对于一篇以**统计方法论为核心贡献**的实证论文，在abstract中提及TOST和关键统计量是合理的。读者需要在abstract就知道等价性是通过formal equivalence testing而非eyeballing得出的。
- 但z=-23.7这个细节确实过于技术化，可以移到正文。

**结论：** 保留TOST和关键p值，移除z=-23.7即可。

---

**[AGREE] R2-W2: Error complementarity实用价值存疑**

同意。<0.4pp的routing capture和p=0.42的re-repair pilot（Appendix I(j), p.17-18）确实使complementarity作为standalone贡献的价值有限。论文将其列为三大贡献之一（§1, p.2第三个bullet point），权重过高。

建议降级为§3.6中的exploratory analysis，从contribution list中移除或弱化。

---

**[REBUT] R2-W3: §2.2预判实验结果造成confirmation bias**

§2.2 (p.2-3)建立failure mode taxonomy是methodology的一部分，不是prediction。具体来说：

- "Token-budget exhaustion"、"format collapse"、"decision collapse"是对output space structure的**先验分析**，基于formulation定义而非实验数据。
- 这类先验分析在实证研究中是standard practice（类似于pre-registering hypotheses）。
- 论文的实验结果实际上**部分推翻**了§2.2的预测："Complexity dependence"部分预测所有formulation在长输入下应perform equally well（"generation modes (1+2) are rarely triggered, and all formulations should perform comparably"），但repo-level结果显示CWM独特地退化——这恰恰不是confirmation。

**结论：** §2.2的先验分析是合理的方法论步骤，非confirmation bias。

---

**[REBUT] R2-W4: Table 3信息过载**

Table 3 (p.6)汇总了repo-level三个formulation在两个model family、两个model size下的结果，加上bootstrap CI和seed数量信息。对于系统比较论文，这种信息密度是必要的——拆分反而增加reader负担（需要在多个table之间交叉对比）。Caption长度反映了table的复杂性，是合理的。

**结论：** Table 3的密度对target audience（关注方法论的研究者）是合适的。

---

**[AGREE] R2-W5: 缺少execution-based verification作为upper bound**

同意这是一个有用的reference point。虽然execution-based verification理论上是100% accurate（它直接运行tests），但实际中存在flaky tests、timeout、environment differences等因素。论文使用的HumanEval+ test suite应该不存在flakiness，但SWE-bench Verified的test reliability数据作为参考会strengthen the comparison。

不过这更像是一个nice-to-have而非must-fix，因为论文的core contribution是execution-free formulation之间的比较，而非execution-free vs execution-based。

---

## Questions

**R2-Q1: 14B monotonic convergence是否暗示32B下formulations将完全等价？**

不确定。如前述（对N1的rebut），gap轨迹是非单调的（4B→8B扩大，8B→14B收窄），且14B仅有单家族3 seeds数据。外推到32B需要：(a)更多model families的14B数据确认convergence pattern，(b)对8B peak的解释。在当前证据下，32B等价是plausible但far from established。

**R2-Q2: Constrained decoding是否能消除CWM format collapse？**

这是一个合理的干预方向。论文在Appendix I(c) (p.17)讨论了relaxed matching但未尝试constrained decoding。CWM的format collapse主要表现为hallucinated test names和repetitive loops（Appendix I, p.16），constrained decoding可能缓解格式问题但不解决semantic accuracy（因为即使格式正确，预测的execution trace仍可能错误）。值得作为future work。

**R2-Q3: 是否尝试用per-test数据训练TRAJ？**

这正是我在Q3中也提出的问题。如果TRAJ可以用per-test labels训练（每个test一个instance），就能分离data volume和label granularity两个confound。论文未报告此ablation。

**R2-Q4: re-repair pilot是否削弱CLS相比TRAJ的核心动机？**

部分同意这是一个重要观察。CLS的核心优势被定位为per-test diagnostic granularity（§2.3, §3.6），但re-repair pilot (p=0.42, Appendix I(j))显示这种granularity不automatically转化为downstream修复改善。不过这不削弱CLS在verification task本身上的表现——verification和repair是不同的downstream applications。

**R2-Q5: CWM format collapse从training早期就存在是否说明LoRA根本无法教会repo-level trace generation？**

Table 16 (p.21)的convergence analysis显示CWM的unparseable rate从training早期就很高。这暗示LoRA在≤8B model上可能缺乏teach structured trace generation的capacity。但"根本无法"过于绝对——14B的parseable rate数据（Table 9, p.13的repo-level breakdown）显示部分改善，且full fine-tuning（而非LoRA）可能表现不同。

---

## Missing References

**R2建议的三个引用：**
1. RGD (Reward-Guided Decoding) — 同意，与CWM的decoding策略直接相关
2. "A dual perspective review on large language models and code verification" (2025) — 需要确认该文献是否真实存在
3. OpenCodeInterpreter (Zheng et al., 2024) — 与execution-based generation相关但与本文的execution-free focus可能不直接相关

---

## 对R2 Overall Assessment的评论

R2给出3.0 (Findings)，主要基于规模限制（N1）、CWM baseline差异（N2）、TRAJ混淆（N3）。我认为：

- R2对N1的评估过度依赖14B结果作为evidence（而14B本身是under-powered的）
- R2对N2的critique本质上是要求一篇不同的论文（unmatched comparison），忽视了matched design的方法论价值
- R2对excitement的2.5分偏低——首个匹配比较在文献中确实填补了gap，即使结果部分可预期

我维持3.5 (Borderline Conference)的评分。论文的方法论贡献（matched design + statistical framework）值得main conference，但must-fix issues（特别是我提出的SESOI sensitivity和confound chain）需要先解决。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1284 · 2026-05-23T14:33:41.192248+00:00_

收到 Reviewer 1 对 Reviewer 2 的交叉回应。等待 Reviewer 2 对 Reviewer 1 的交叉回应后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 114

## Round 114

2 recorded events


### User

_source line 1285 · 2026-05-23T14:33:48.677783+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **N1（规模限制）**：[REBUT] 14B证据本身不足以支撑"capacity artifact"结论（非单调gap、n=3单家族），但同意title/abstract需更明确限定scope
- **N2（CWM baseline）**：[REBUT] 匹配设计是方法论贡献而非缺陷，但Conclusion的domain-difference claim应加条件限定
- **N3（TRAJ混淆）**：[AGREE] 部分同意应标记为exploratory，但反对完全否定——数据效率是formulation固有属性
- **W1-W5**：同意W2（complementarity降级）和W5（加execution upper bound），反驳W1（统计细节对方法论论文合理）、W3（§2.2是先验分析非confirmation bias）、W4（Table 3密度对target audience合适）

维持3.5 (Borderline Conference)评分不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1286 · 2026-05-23T14:33:56.041408+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 115

## Round 115

12 recorded events


### User

_source line 1287 · 2026-05-23T14:34:36.600604+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Weaknesses 回应

### R1-W1: TOST SESOI（±2pp）post-hoc，等价结论对阈值敏感

**[AGREE]** 部分同意，但认为 R1 高估了这一问题的严重性。

同意点：±2pp SESOI 未 pre-register 是一个合理的方法论批评。论文 §3.3 自己承认 "was not pre-registered"。R1 要求在正文中报告 sensitivity analysis 的建议是合理的——目前 Table 13 (Appendix G) 的 margin sensitivity 确实应该出现在正文中。

反驳点：但我不认为这达到 Must-Fix 级别。原因：
1. 论文 §3.3 已提供了 ±2pp 的 domain justification："at 85-88% accuracy, 2pp per-test difference corresponds to ~38 additional errors across 1,890 tests (~2-3 problems out of 114), comparable in magnitude to between-seed standard deviation (0.37-0.97pp) and checkpoint selection noise (<1pp)." 这个论证是合理的——当 formulation 间差异小于训练 seed noise 时，practitioner 无法可靠地区分 formulation。
2. 即便采用 R1 建议的 ±1.5pp（Table 13 显示 borderline at p=0.054），CLS-CWM 的 equivalence 结论方向不变（仍在 borderline 以内），只是 p 值边界化。最小等价 margin 为 ±1.52pp，仅比 ±2pp 低 0.48pp。
3. R1 提到 "安全关键场景" 中 2pp 可能不等价——但论文的 benchmark 是 HumanEval+MBPP 和 SWE-bench，不是安全关键系统。在合理的 deployment 场景下，±2pp 是 defensible 的。

**建议作者**：将 Table 13 sensitivity analysis 移入正文，并改为 "CLS and CWM are equivalent within ±2pp (sensitivity: down to ±1.52pp)" 的措辞，而非单纯的 "statistically equivalent"。这是 R1 建议中最合理的部分。

---

### R1-W2: 低统计 power（~0.3）削弱非显著性结论

**[AGREE]** 同意这是一个真实的方法论弱点。

论文 §3.3 报告 power ~0.3，意味着 70% 概率无法确认 equivalence，即使真实差异在 SESOI 以内。但我注意到论文在这方面的处理已经优于大多数 NLP 论文：
1. 论文使用了三重互补验证：frequentist TOST + Bayesian ROPE (P(ROPE)=0.975 for CLS-CWM) + 14B scaling evidence。低 power 影响 TOST 但不影响 Bayesian analysis。
2. CLS-TRAJ equivalence 确实因 power 不足而 "not confirmed after Holm correction"（§3.3），论文没有强行 claim equivalence——这是正确的做法。

R1 提出 "显著时用显著性、不显著时用描述性" 的双标准批评我认为部分成立，但论文已经通过 Bayesian ROPE 补充了频率学派 TOST 的不足（Appendix G.1）。

对 R1 关于 repo-level 的具体担忧：n_eff≈86（§3.3, DEFF=3.97 at function level），论文 Appendix H 确实报告了 variant-level MDE≈25pp (Table 12)。CLS-CWM gap (29-35pp) 超过 MDE，CLS-TRAJ gap (<10pp) 低于 MDE。论文在 Appendix H 已做了正确的 power vs detectable effect 分析。

**建议作者**：在 §3.3 正文中明确报告 repo-level effective sample size 和 MDE，不要仅在 appendix 中提及。R1 建议将 power<0.5 的比较标为 "inconclusive" 是合理的。

---

### R1-W3: CWM repo-level confound chain 未解耦

**[REBUT]** 部分反驳。R1 提出的因果链（NaN val loss → final epoch → overfit → unparseable rate 上升）被论文的多项 ablation 证据部分否定。

R1 假设的因果链是：max_new_tokens=512 → truncation → unparseable rate → gap。但论文 Appendix N 提供了关键反证：

1. **更长 generation budget 恶化而非改善 format compliance**：Appendix N (evaluation sequence length) 明确报告 "increasing Qwen3-8B CWM evaluation from seq4096 to seq8192 *raises* the unparseable rate (63.7%→73.8%) while changing accuracy by only 0.81pp"。给模型更多 token budget 使 format collapse 更严重——这直接否定了 "truncation 导致 unparseable" 的假设。

2. **Early checkpoint 已有 format collapse**：Appendix N (CWM convergence) 报告 step 400 (~6.5% of training) 的 Qwen3-8B CWM 已有 63.7% unparseable rate，与 final epoch 的 60.4-63.9% 相当。"collapse 从 training 早期就存在，final epoch selection 不是原因。"

3. **Matched-context ablation 排除 input context confound**：Appendix B 显示 CLS@2048 vs CWM@2048 gap 为 25.00pp（全 gap 25.59pp 的 98%），"confirming that input context disparity explains at most 3% of the difference。"

4. **Accidental training artifact 提供因果证据**：Appendix (c) 报告 "a CWM model inadvertently trained on function-level (CLS-format) data achieved 86.05% accuracy with 0% unparseable outputs at repo level"——same model, same capacity, different output format → 恢复 CLS-level 性能。这是最强的因果证据：output format complexity（而非 checkpoint/truncation/engineering）是 bottleneck。

R1 说 "5 个 confound 每个只单独 ablation" 在技术上正确，但论文已有足够 ablation 排除最主要的替代假说。confound chain 的联合上界（~11.5pp, §3.5）仍低于观测 gap（18-26pp）。

**部分同意**：R1 要求 "区分 formulation 局限 vs 工程限制" 是合理的建议。CWM 的 format collapse 可能通过 constrained decoding 或 execution trace pretraining 来解决——这是工程问题还是 formulation-inherent 问题确实需要更明确的讨论。

---

### R1-W4: TRAJ 训练数据量差异混淆 formulation 效果与数据量效果

**[AGREE]** 完全同意。这与我的 N3 观点一致。

~400 vs ~70K 的 175× 差异是根本性 confound。Downsample ablation（Appendix O: CLS 80.74% vs TRAJ 72.92%，+7.82pp）控制了 data volume 但未控制 label granularity。R1 建议 "明确说明比较的是 formulation 在其自然数据条件下的表现" 是一个合理的 framing 调整——这比声称 "TRAJ equivalence not confirmed" 更准确，因为后者暗示差异来自 formulation。

补充：论文 §3.4 最后一段承认 "CLS-TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity (per-test vs variant-level), a formulation-inherent confound that cannot be experimentally resolved。" 但这个 caveat 应该出现在更显著的位置（如 Table 3 caption 或 contribution statement），而非仅在 §3.4 末尾。

---

### R1-W5: 14B convergence 基于单一模型家族、3 seeds，且非单调

**[AGREE]** 同意这是一个弱点，但认为 R1 对 non-monotonic pattern 的关注过度。

R1 指出 gap 从 1.32pp(4B) → 2.62pp(8B) → 1.07pp(14B) 是非单调的。但需要注意：
1. 4B 和 8B 仅用 2 seeds，14B 用 3 seeds（Table 2）。2-seed 估计的方差很大。
2. CWM 在 4B→8B 的 accuracy 几乎不变（87.36→87.33, -0.03pp），而 CLS 上升（88.68→89.94, +1.27pp）。所以 gap 扩大不是 CWM 退化而是 CLS 进步更快——这与 capacity-dependent convergence 叙事并不矛盾（CLS 先 saturate，CWM 后 catch up at 14B）。

但 R1 的核心观点是对的：3 seeds + 单一模型家族的 14B 结果太弱，无法支撑 "capacity-dependent convergence" 这样的普遍性叙事。论文应在全文一致使用 "preliminary"，并避免在 §5 Conclusion 中以 "gap narrows monotonically to 1.07pp" 的措辞暗示强趋势。

---

### R1-W6: LPM z=-23.7 可能因假设违背而膨胀

**[REBUT]** 反驳。论文 Appendix J 已提供了完整的 logistic regression robustness check 并报告了具体数值。

Appendix J 明确报告：
- Cross-complexity model: CWM×repo interaction OR=0.31 (95% CI [0.15, 0.65], **p=0.002**), AME=-21.6pp
- Cross-model model: CWM deficit OR=0.30 ([0.15, 0.63], **p=0.001**, AME=-21.1pp)
- "Direction, magnitude, and significance of all primary effects are concordant between LPM and logistic regression"

LPM 的 z=-23.7 可能因异方差膨胀，但 logistic regression 的 p=0.002 confirm 了 interaction 的 statistical significance，且 AME (-21.6pp) 与 LPM coefficient (-21.9pp) 在 0.3pp 以内匹配。R1 担心的 "可能因假设违背而膨胀" 在 robustness check 中已被 addressed。

R1 说 "logistic regression robustness check 未报告具体 z 值/OR"——这是不准确的。Appendix J 第三段 "Logistic regression robustness check" 明确报告了 OR、CI、p 值和 AME。R1 可能没有仔细阅读这一段。

**建议作者**：在正文 §3.4 的 formulation×complexity interaction 段落中加一句引用 logistic regression 结果（如 "confirmed by logistic regression, OR=0.31, p=0.002; Appendix J"），使读者不需要翻到 appendix 才能获得 robustness 信息。

---

### R1-W7: CWM checkpoint ablation 范围太窄

**[REBUT]** 部分反驳。论文 Appendix N 已包含 DeepSeek-Coder CWM checkpoint 分析。

Appendix N (CWM convergence analysis) 明确报告："Cross-model validation: a DeepSeek-Coder early-stopped checkpoint (s123, epoch 1) achieves 75.45% versus 57.31% at epoch 3 (s123; +18.14pp), **but retains 66.4% unparseable rate**, confirming that format collapse emerges early and is not a late-training artifact。"

这正是 R1 要求的 DeepSeek CWM checkpoint 分析。结论与 Qwen3 一致：early checkpoint 提升 accuracy 但未解决 format collapse。R1 可能遗漏了 Appendix N 的这一段落。

不过，R1 的建议有合理之处：DeepSeek CWM 没有类似 Table 16 那样的 step-level convergence table，仅有 epoch-level 比较。如果有更细粒度的 DeepSeek step-level data 会更有说服力。

---

### R1-M1: "Collapses" 和 "driven by" 是因果措辞

**[AGREE]** 同意。"equivalence collapses" 和 "driven by format collapse" 确实暗示因果关系，而论文的证据是 observational + ablation，不是 randomized intervention。虽然 accidental training artifact（Appendix (c)）提供了接近因果的证据，但总体表述应更谨慎。建议改为 "diverges" 和 "co-occurs with / is associated with"。

---

### R1-M2: Figure 2 y 轴未从 0 开始

**[AGREE]** 同意这是视觉上的问题。论文 caption 已标注 "y-axis does not start at zero"，但这容易让读者在快速浏览时高估 gap 的绝对幅度。我在自己的审稿意见中也指出了同一问题。建议加灰色标注或 broken axis 标记。

---

### R1-M3: "Equivalence" 与 "parity" 混用

**[AGREE]** 同意。论文中 "equivalence" 有 formal statistical 含义（TOST），而 "parity" 用法更 informal。术语不一致可能导致读者混淆 formal equivalence test 结果与 informal 观察。建议统一：用 "equivalence" 仅指 TOST-confirmed results，其他用 "comparable" 或 "similar"。

---

### R1-M4: Appendix 过长（15 页）

**[REBUT]** 不同意这是一个问题。ACL ARR 对 appendix 长度无上限限制。15 页 appendix 覆盖了 Oracle analysis、ablation studies、extended analysis、TOST sensitivity、Bayesian ROPE、Holm correction、mixed-effects regression、parseable bias、CWM convergence、few-shot baselines、threats to validity 等——每一项都为 R1 提出的各项质疑提供了回答。如果缩短 appendix，R1 的 W1-W7 中多项质疑将因缺少支撑 evidence 而更难回应。详尽的 supplementary material 是这类 empirical comparison paper 的标准做法。

---

## Questions 回应

### R1-Q1: 能否论证 ±2pp 而非 ±1.5pp？

已在 W1 回应中讨论。±2pp 的核心 justification 是 between-seed std (0.37-0.97pp) 和 checkpoint noise (<1pp)——当 formulation 差异 < 训练噪声时，practitioner 无法可靠区分。±1.52pp 是最小等价 margin（Table 13），±2pp 留有 0.48pp buffer。作者可以考虑在正文同时报告 ±2pp 和 ±1.5pp 的结果。

### R1-Q2: CWM NaN val loss 是 formulation-inherent 还是工程问题？

基于论文证据，我认为是**两者的混合**。NaN val loss 发生在 "runs with NaN validation loss (due to truncated targets exceeding 2,048-token limits)"（§3.1）——即当 target execution trace 超过 max_seq_length 时。这是 formulation-inherent（CWM 的 target 本质上更长）和 engineering（2048 token limit）的交集。CLS 的 1-token target 永远不会触发此问题。

### R1-Q3: 是否尝试 per-test 数据训练 TRAJ？

我在自己的 Q3 中提出了完全相同的问题。这是分离 data volume 和 label granularity confound 的关键实验，论文目前没有提供。

### R1-Q4: 4B→8B gap 扩大 + 14B 收窄的非单调模式如何解释？

已在 W5 回应中讨论。CWM 在 4B→8B 的 accuracy flat (-0.03pp) 而 CLS 上升 (+1.27pp) 造成 gap 扩大。14B 时 CWM catch up (+2.17pp) 而 CLS plateau (-0.01pp)。这与 "CLS 先 saturate、CWM 需要更大 capacity 才能发挥" 的解释一致。但 2-seed 估计的方差大，非单调性可能是 seed noise。

### R1-Q5: Logistic regression 的 z 值？

已在 W6 回应中指出：Appendix J 已报告 OR=0.31, p=0.002 (cross-complexity), OR=0.30, p=0.001 (cross-model)。R1 可能遗漏了 Appendix J 的第三段。

### R1-Q6: Simple routing <0.4pp 是否说明错误在 instance level 高度重叠？

不是——论文 Appendix (a) 的 oracle combination 显示 +2.80pp（function level）和 +14.58pp（repo level）的 oracle advantage，说明错误在 instance level 并不高度重叠（重叠高的话 oracle 也不会有 advantage）。<0.4pp 反映的是 **simple heuristics 无法 predict which instances 会 disagree**，而非 overlap 高。错误是 partially complementary 但 instance-specific，需要 learned router 才能利用。

---

## Missing References 回应

### Arcuri & Briand (2011) 统计测试指南

**[AGREE]** 这是一个 relevant reference。该文 "A practical guide for using statistical tests to assess randomized algorithms in software engineering" 讨论了 effect size reporting 和 non-parametric test 在 SE 实验中的最佳实践。鉴于本文大量使用统计检验，引用此文作为 methodology reference 是合适的。

---

## 总结

R1 的审稿总体质量高，尤其在统计方法论层面的批评（W1, W2）具有针对性。我同意 W1（sensitivity analysis 应在正文）、W2（low power 应更明确标注）、W4（TRAJ confound）、W5（14B preliminary）。但我反驳 W3（论文已有多项 ablation 排除 R1 假设的因果链）、W6（logistic regression 结果已报告）、W7（DeepSeek checkpoint 分析已存在于 Appendix N）。M4（appendix 过长）不应被视为弱点——详尽的 supplementary material 恰恰是论文回答审稿质疑的基础。

R1 给出 3.5 (Borderline Conference)，我给出 3.0 (Findings)。主要分歧在于：R1 认为统计方法论修补后可达 Conference 水平，而我认为 **规模限制（≤8B）对核心 claim 泛化性的约束** 是更根本的问题——这一点 R1 未充分讨论。即使所有统计呈现完美，如果 32B 下 formulation 等价，论文的 practical impact 仍然有限。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-23T14:35:23.011400+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool call

_source line 1289 · 2026-05-23T14:35:23.011838+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 1290 · 2026-05-23T14:35:23.062466+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T14:22:22.262321+00:00\", \"completed_at\": \"2026-05-23T14:25:53.424753+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 23\", \"message\": \"最后一页仅 4 行文字，其余 ~95% 为空白。Appendix O (Threats to Validity) 结尾段可与前一节合并排版，避免近空页\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-2\", \"message\": \"连续 2 页纯文本，无任何 display item。第一个视觉锚点（Figure 1 验证公式对比图）出现在第 3 页顶部。建议考虑将 Figure 1 提前到第 2 页，以在审稿人翻页时尽早锚定核心概念\"}, {\"severity\": \"warning\", \"dimension\": \"pages 16-17\", \"message\": \"Appendix I (Extended Analysis) 连续 2 页纯文本，无图表穿插。分析密度高但视觉单调\"}, {\"severity\": \"warning\", \"dimension\": \"pages 20-22\", \"message\": \"Appendix M/N/O 连续 3 页纯文本，无任何 display item。对深入阅读的审稿人可能造成疲劳\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（三种验证公式对比流程图）清晰专业，颜色区分度好（绿/橙/蓝），caption 自包含，能有效传达核心 idea\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2（scaling 折线图）使用不同颜色+marker 区分 CLS/CWM/TRAJ，带 shaded CI 区间，灰色 gap 区域有效突出 formulation 间差距。Y 轴起始非零（~60%），标注清晰。字号略小但可读\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 booktabs 风格，最优结果加粗，小数精度列内一致。格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 同样 booktabs 格式，粗体标注最优。Model Size 列与 Accuracy 列对齐良好\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 3 repo-level 结果表，格式一致。Table 4 failure mode taxonomy 排版清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 3（oracle 优势柱状图）清晰可读，蓝色柱体+clear labels\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Conclusion + Limitations 占约 2/3 页面，References 从页面下 1/3 开始。空间利用合理\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"未发现 margin 溢出、LaTeX 渲染错误、[?] 未解析引用、section heading 孤悬页底等问题\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"主文 8 页含 2 figures + 4 tables = 6 display items（0.75/页），密度
…[truncated 116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1291 · 2026-05-23T14:35:23.063008+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1292 · 2026-05-23T14:41:32.762474+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "\n# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N2 re-raises（2-3 seeds, n=48, 5 confounds, 'collapses' 措辞）。R2 REBUT 指出 R1 混淆两个统计模型（z=-23.7 来自 139-cluster 交互 LPM 非 25-cluster 跨模型模型）。Director：R2 事实核查正确；R1 broader concern 仍有效但论文 §3.5/§3.7 hedging 已充分。Resolved 维持。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W2 re-raises low power (~0.3, n_eff≈86) 对非显著性结论的信息含量。R2 AGREE 但补充论文已用 TOST+Bayesian ROPE+14B scaling 三重互补验证。共识：正文应报告 repo-level effective sample size 和 MDE。Resolved 维持——§3.4 已有 power paragraph，Appendix H 已报告 MDE。\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13-R15 反复提及但无新增要求。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → final epoch). 但 R7 的 CLS epoch ablation (<1pp) 仍有效。新角度：CWM NaN val loss 可能是 formulation-inherent。\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。但 R2 REBUT：Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp。Director 裁定：证据表明 checkpoint 差异无法解释 18-26pp gap，降为 Should-Fix。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-N2 升级为 critical：论文持有 Qwen3 CWM step 300-400 optimal checkpoints 但未评估其 repo-level accuracy。R2 完全 AGREE。\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W4 re-raises：checkpoint ablation 仅在 Qwen3-4B CLS 上进行，未覆盖受影响最严重的 CWM 配置。DeepSeek CWM early-stop vs final-epoch ~18pp。R2 AGREE。Director：resolved status maintained——step-400 eval 数据已证明 early checkpoint ≤ final epoch，format collapse 从训练早期即存在。\"\n    - round: 14\n      reviewers: [2]\n      note: \"Fresh review R14. R2-W1 re-raises s42 用 step 400 vs s123/s456 用 step 6633 的配置异质性。R1 AGREE。Director：resolved 维持——step-400 eval 数据已证明早期 checkpoint 不改善结果。\"\n    - round: 15\n      reviewers: [1]\n      note: \"Fresh review R15. R1-W7 re-raises CWM checkpoint ablation 范围太窄（仅 Qwen3-8B）。R2 REBUT：Appendix N 已包含 DeepSeek-Coder CWM 分析（epoch1 75.45% vs epoch3 57.31%，但仍 66.4% unparseable）。Director：R2 事实核查正确，resolved 维持。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因（formulation-inherent vs implementation issue）\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文更显著讨论 checkpoint 缓解证据\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy 并报告结果\"\n      assigned_to: \"experiment\"\n      status: wont_fix\n    - round: 12\n      action: \"Appendix cwm_convergence 补充说明 step-level checkpoint 不可做的原因\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Step 300-400 checkpoints 未保存，但已找到现有 step-400 eval 数据（s42: 64.36% accuracy, 63.7% unparseable）。早期 checkpoint ≤ final epoch，直接反驳 'optimal early checkpoint closes gap' 假设。Format collapse 从训练早期即存在。数据写入 Appendix cwm_convergence。\"\n  resolution_round: 12\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1: 'design space' framing 过度. R1 部分同意.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1 再次标 CRITICAL。R1 AGREE 但认为 failure mode taxonomy 有独立贡献。两人共识：Findings 合适，Main 不够。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. R2 STILL_OPEN. R1 AGREE on assessment but argues exceptional soundness partially compensates. Both accept 3.0-3.5 range. Director: inherent limitation, wont_fix.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R2-N1 标 CRITICAL (Excitement 2/5)。R1 REBUT。最终分歧：R1 Excitement 3/5, R2 Excitement 2/5。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N1 再次标 CRITICAL：核心发现可从 §2.2 理论预测，属 confirmation 而非 discovery。R1 AGREE 但补充 quantitative boundary conditions（14B convergence, failure mode distribution）超越纯理论预测。两人 Excitement 均为 3/5。Director：inherent limitation，wont_fix 维持。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R2-N1 再次标 CRITICAL (Excitement 2.5/5)。R1 REBUT：function-level 等价阈值、failure mode taxonomy 分布、capacity-dependent convergence 量化均超越 §2.2 理论预测，建议降为 Should-Fix。Director：R1 REBUT 有说服力，不采纳为独立 issue。Inherent limitation，wont_fix 维持。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1 Excitement 3/5, R2 Excitement 2.5/5。R2-N1 隐含标 Critical（scale limitation → practical impact limited）。R1 REBUT：matched design 是文献中首个，有方法论贡献。Excitement 稳定在 2.5-3.0 范围。wont_fix 维持。\"\n  resolution: \"所有可行 action items 已完成。Excitement 稳定在 2.5-3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。Novelty ceiling 为 inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"SESOI 基于训练噪声量级独立于 observed gap.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。缺 domain-specific justification.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W4 re-raises：±2pp 依赖于 accuracy range 和 test set size。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-W1 re-raises：无 pre-registration，±1.52pp 临界值距 ±2pp 仅 0.48pp。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-M1 和 R1-Q1 再次提及 pre-registration 状态。R2 AGREE。§3.4 已改为 'motivated by domain considerations but was not pre-registered'，引用 sensitivity analysis。Director: resolved——已诚实披露，无进一步修改空间。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N1 标 Critical：鲁棒窗口仅 0.48pp。R2 AGREE with downgrade to Should-Fix：Bayesian ROPE 独立佐证 (P(ROPE)=0.975)、deployment relevance 论证合理、论文已透明披露。Director 采纳降级：Should-Fix。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W1 再次标 Must-Fix。R2 AGREE 部分但认为非 Must-Fix：§3.3 domain justification 合理（seed noise 0.37-0.97pp + checkpoint noise <1pp），最小 margin ±1.52pp 仅低 0.48pp，Bayesian ROPE P(ROPE)=0.975 独立佐证。共识：Table 13 sensitivity analysis 应移入正文。Director：resolved 维持——论文已诚实披露 post-hoc 状态，建议 rebuttal 中强调 sensitivity analysis。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；引用了 sensitivity analysis (Table tost_sensitivity)；明确承认结论对 margin 选择敏感。Bayesian ROPE 提供独立佐证。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入限定。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W6: 175× 数据量差异.\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：180× 差异 + signal granularity。R2 AGREE。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-W4 re-raises：downsample 控制了 volume 但未控制 label granularity。R2 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N2 标 CRITICAL：TRAJ 使用 ~400 vs ~70K 实例 + 不同 lr + variant-level labels，三方比较不受控。R1 完全 AGREE，补充：主文 Tables 1-3 无视觉标注 TRAJ 差异。Director 裁定：§3.5 已有 'exploratory' 标注和 confound 讨论，resolved 维持。但报告记录此为 persistent concern。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N3 标 Critical：lr 4×、数据量 175×、标签粒度三重差异使 'matched comparison' 不成立。R2 AGREE with qualification to Should-Fix：论文已有 ★ 标记 + §3.5 'exploratory' + Appendix N，但应在 Abstract/§1 更早限定。Director 采纳降级：Should-Fix。建议 Abstract 限定 'matched for CLS and CWM; TRAJ comparison is exploratory'。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W4 (Should-Fix) + R2-N3 (Must-Fix) 再次提出。R1 补充：数据效率是 formulation 固有属性，比较有 validity，但应更显著标记 exploratory。R2 认为根本性混淆。交叉后共识：TRAJ 比较应在 Table 1 caption 和 contribution statement 中明确标注 exploratory。Director：resolved 维持——Abstract 已有 'the TRAJ comparison is inherently confounded'（R14 修复），§3.5 有 exploratory 标注。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"Contribution summary 中明确表述 CLS-TRAJ repo-level 比较包含 training regime confound\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 标注 'The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity, a formulation-inherent confound.' Abstract 已有 'the TRAJ comparison is inherently confounded'。\"\n  resolution_round: 12\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"CodeRM, CodeScaler, GenPRM 等均已加入 Related Work。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"bar labels 偏小.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-M2: y-axis 不从零开始（55%），视觉夸大 gap。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED.\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-M2 和 R2-M2 均再次提及 y-axis 非零基线。Director：resolved——caption 已标注 'y-axis does not start at zero'，对 0-3pp 差异合理。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. 两位均再次提及。Caption 标注已存在。Resolved 维持。\"\n  resolution: \"Figure 2 caption 标注 'y-axis does not start at zero'，两位 Reviewer 一致确认合理。\"\n  resolution_round: 11\n\n# === Round 8 Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 15\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-N3 re-raises.\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-N1 再次标 CRITICAL：Abstract 'not confirmed' 在 power ~0.3 下 over-stated。R2 AGREE but 认为 Should-Fix（措辞问题非方法论缺陷）。Director 裁定 Should-Fix：§3.4 已诚实报告 power，问题在 Abstract/Conclusion 措辞。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W2 标 Must-Fix：power ~0.3 削弱结论。R2 AGREE 但补充 Bayesian ROPE (P(ROPE)=0.975) 不受 power 限制。共识：正文应报告 repo-level effective sample size 和 MDE。Director：resolved 维持——§3.4 power paragraph + Appendix H MDE 已充分披露。建议 rebuttal 引用 Bayesian ROPE 互补验证。\"\n  action_items:\n    - round: 9\n      action: \"Variant-level 分析明确标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文讨论 TOST 功效限制；Bayesian ROPE 补充\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"正文讨论 power ~0.3 意味着 '未确认' 不应解读为 '非等价'\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.4 已扩写 power paragraph，14B TOST 完成。Contribution 措辞保守。\"\n  resolution_round: 12\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Cross-seed oracle 已加入正文。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Appendix 已讨论。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM / RepoExec\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 15\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-W2 re-raises CWM 生态效度。R2 partially AGREE but notes §3.7 和 §5 已有 ≤8B 限定。Director: resolved——≤8B qualifier 已充分覆盖 Abstract/Conclusion/Threats.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R2-N2 标 Critical：14B 收敛至 0.43pp 暗示 capacity-driven。R1 AGREE。Director 裁定 Should-Fix（降级）：论文已有 qualifier（Abstract ≤8B, §3.3 scaling, Limitations），建议 Conclusion 更显著讨论 32B+ open question。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R2-N2 标 Must-Fix：CWM baseline 与 32B CWM 差异过大，domain difference claim 不可靠。R1 REBUT：匹配设计是方法论贡献而非缺陷——使用 32B CWM vs 4B CLS 则 capacity confound 更大。但 R1 同意 Conclusion domain-difference claim 应加条件限定。Director：R1 rebut 成立——matched design 的方法论价值独立于 scale；但 §5 GenRM 对比应明确加 '≤8B LoRA without trace pretraining' 条件。Resolved 维持。\"\n  resolution: \"合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。§5 Conclusion 已有 'under ≤8B LoRA protocol' 和 'capacity-contingent remains open'。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. 两人 Excitement 均为 3/5，Overall 均为 3.0 (Findings)。合并至 R6-N4 追踪。\"\n  resolution: \"合并至 R6-N4。Inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 15\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Both RESOLVED. GEE logistic regression added.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-M3 提及 LPM vs GEE 在 model identity 显著性上不一致（p=0.002 vs p=0.449）。论文已在 Appendix M 讨论 cluster 数限制。Director: resolved——Appendix M 已明确标注 estimator-dependent。\"\n    - round: 15\n      reviewers: [1]\n      note: \"Fresh review R15. R1-W6 re-raises LPM z=-23.7 可能膨胀。R2 REBUT：Appendix J 已报告完整 logistic regression 结果（OR=0.31, p=0.002, AME=-21.6pp），与 LPM concordant。R1 可能遗漏 Appendix J 第三段。Director：R2 事实核查正确，resolved 维持。建议正文 §3.5 加一句引用 logistic regression 结果。\"\n  resolution: \"Appendix M 补充 GEE logistic regression + estimator-dependent 标注。R15 R2 确认 Appendix J 已有完整 OR/CI/p/AME 报告。\"\n  resolution_round: 11\n\n# === Round 9 Issues ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大 gap。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却声称 'model-dependent'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Abstract 改为更审慎措辞。\"\n  resolution_round: 10\n\n- id: \"R9-M1\"\n  summary: \"Figure 3 y-axis 不从 0 开始但未标注\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Caption 标注。合并至 R6-M3。\"\n  resolution_round: 11\n\n- id: \"R9-M2\"\n  summary: \"Abstract 第一句过于绝对\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"已改为 'increasingly leverages'。\"\n  resolution_round: 10\n\n- id: \"R9-M3\"\n  summary: \"缺少方法论引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"两篇已引用。\"\n  resolution_round: 10\n\n- id: \"R9-M4\"\n  summary: \"Clustered bootstrap 实施细节\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§3.1 已说明。\"\n  resolution_round: 10\n\n- id: \"R9-M5\"\n  summary: \"Repo-level DEFF=114.3 → effective n≈86\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§5.2 加入 TOST power 段落。\"\n  resolution_round: 10\n\n# === Round 10 Issues ===\n\n- id: \"R10-W1\"\n  summary: \"Python-only 评估未在 Limitations 提及\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"Limitations 加入 Python-only 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-W2\"\n  summary: \"'formulation choice is governed by code complexity' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"'governed by' 改为 'moderated by'。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"3-shot ICL collapse 未充分讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"§5.4 扩展。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"Appendix 导航不便\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"Mini TOC 加入。\"\n  resolution_round: 10\n\n# === Round 11 Issues ===\n\n- id: \"R11-M1\"\n  summary: \"Figure 2 中 14B 数据点视觉等权\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Figure 2 已更新。\"\n  resolution_round: 11\n\n- id: \"R11-M2\"\n  summary: \"§3.5 LPM model identity vs GEE 需 qualifier\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Commit 0b38a2b 修复。\"\n  resolution_round: 11\n\n- id: \"R11-M3\"\n  summary: \"Abstract 'motivate routing' 暗示过度\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Abstract 已改含负结果量化。\"\n  resolution_round: 11\n\n# === Round 12 Issues ===\n\n- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"两人独立提出。14B function-level gap 收敛至 0.43pp 支持 capacity-driven 假设。\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W2 再次提及 CWM 生态效度。R2 partially AGREE but notes 论文已有充分 qualifier (§3.7, §5, Abstract). Director: resolved——所有 qualifier 已到位。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R2-N2 再次标 Critical，R1 AGREE。合并追踪至 R8-W6 round 14 mention。Director 裁定 Should-Fix（降级）。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R2-N1/N2 再次标 Must-Fix（scale limitation + CWM baseline fairness）。R1 REBUT matched design 方法论价值。Director：合并追踪至 R8-W6。Resolved 维持。\"\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。\"\n  resolution_round: 12\n\n- id: \"R12-N2\"\n  summary: \"Qwen3 CWM optimal checkpoint 未评估\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Step-400 eval 数据已找到（64.36% accuracy, 63.7% unparseable），反驳 'optimal early checkpoint closes gap' 假设。\"\n  resolution_round: 12\n\n- id: \"R12-N3\"\n  summary: \"CLS-TRAJ 等价性不对称结论可能是 power ~0.3 artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 提出，R2 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-N1 再次以更强力度提出：Abstract 'not confirmed' 在 power ~0.3 下 misleading。R2 AGREE (Should-Fix). Director: §3.4 power paragraph 已有充分披露，问题仅在 Abstract/Conclusion 措辞。见 R13-W1。\"\n  resolution: \"§3.4 power paragraph 扩写，14B TOST 完成。\"\n  resolution_round: 12\n\n- id: \"R12-W1\"\n  summary: \"Failure mode taxonomy 未列为独立贡献\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"§1 增加第三条贡献。\"\n  resolution_round: 12\n\n- id: \"R12-W2\"\n  summary: \"GenRM 对比发现未充分讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-W4 再次标 Should-Fix：Conclusion 仅 1 句话讨论 GenRM domain specificity，未分析 WHY。R1 AGREE 并建议用论文已有数据（parseable rate, inference efficiency）支撑分析。Director：Conclusion 段落已存在但确实过于简短。见 R13-W4。\"\n    - round: 15\n      reviewers: [2]\n      note: \"Fresh review R15. R2-N2 中包含 domain difference claim 批评。R1 同意 Conclusion domain claim 应加条件限定。§5 已有扩展讨论（output structure 假设 + unparseable rate）。Resolved 维持。\"\n  resolution: \"Conclusion 新增 GenRM domain-specificity 段落。\"\n  resolution_round: 12\n\n- id: \"R12-W3\"\n  summary: \"Preprocessing-checkpoint confound chain\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"§3.7 已加入 confound chain 描述。\"\n  resolution_round: 12\n\n- id: \"R12-W4\"\n  summary: \"CLS-CWM cross-seed pairing 局限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"§3.7 已加入 cross-seed pairing limitation。\"\n  resolution_round: 12\n\n- id: \"R12-M1\"\n  summary: \"§2.2 Failure Modes 位于 method section\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"R2-W3 re-raises：§2.2 预判实验结果，造成 confirmation bias 印象。R1 REBUT：先验分析是标准 hypothesis-driven research，且实验结果部分推翻了 §2.2 预测（CWM 独特退化非所有 formulation 均匀退化）。Director：R1 rebut 成立——§2.2 标题已为 'Expected Failure Modes'，是方法论步骤而非预判。\"\n  resolution: \"标题改为 'Expected Failure Modes'。R15 R1 rebut 成立。\"\n  resolution_round: 12\n\n- id: \"R12-M2\"\n  summary: \"Appendix G' 命名不直观\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"改为 G.1 subsection。\"\n  resolution_round: 12\n\n- id: \"R12-M3\"\n  summary: \"wei2022emergent 引用类型不一致\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"@inproceedings → @article。\"\n  resolution_round: 12\n\n- id: \"R12-M4\"\n  summary: \"Figure 2 float 漂移\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Figure 2 移入 experiments.tex。\"\n  resolution_round: 12\n\n# === Prior Round Issues ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n# === Round 13 Issues ===\n\n- id: \"R13-N1\"\n  summary: \"Appendix 'P: Limitations' 标题可能违反 EMNLP 格式规则（一篇文章只能有一个 limitations section）\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 提出，R2 完全 AGREE。EMNLP 2026 / ARR 规定 appendix 不能有 limitations section。Appendix 概览列出 'P: Limitations'，构成形式违规。\"\n  action_items:\n    - round: 13\n      action: \"将 Appendix P 'Extended limitations' 重命名为 'Extended Experimental Details' 或 'Additional Confound Analysis'，并从 Appendix 概览中移除 'P: Limitations' 标签\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Appendix P 重命名为 'Extended validity discussion'（采纳 Reviewer 建议），概览中同步更新。Checklist 中引用也已更新。\"\n  resolution_round: 13\n\n- id: \"R13-W1\"\n  summary: \"Abstract/Conclusion 中 TRAJ 'not confirmed' 措辞在 power ~0.3 下 over-stated——应加 power 限定语\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1 提出（标 Must-Fix），R2 AGREE 但认为 Should-Fix（§3.4 已诚实报告）。Director 裁定 Should-Fix。Abstract 'TRAJ parity is not confirmed after multiple comparison correction at any scale tested' 在 power ~0.3 下可能让读者误解为存在差异的证据。14B 收敛结果（1.07pp）应给予更突出位置。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 加入 power 限定语\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 13\n      action: \"Conclusion 明确讨论达到 power ≥0.8 所需的 seed 数量\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Abstract 加入 'at current power (~0.3)' 限定语。\"\n  resolution_round: 13\n\n- id: \"R13-W2\"\n  summary: \"Oracle 互补性应重新框定为 negative result + motivation，而非独立正面贡献\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 partial REBUT。Director 裁定 Should-Fix。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R2-W2 re-raises：<0.4pp routing + p=0.42 re-repair pilot → 实用价值近零。R1 AGREE 应降级为 exploratory finding。共识达成。Director：resolved 维持——Introduction Contribution 2 已重写为 negative result framing（R13 修复），明确 'simple routing heuristics capture <0.4pp, framing complementarity as motivation for future learned routers'。\"\n  action_items:\n    - round: 13\n      action: \"Contribution 2 措辞调整\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Introduction Contribution 2 重写：明确 simple routing heuristics capture <0.4pp of oracle gap，互补性 framed as 'motivation for future learned routers' 而非独立正面贡献。\"\n  resolution_round: 13\n\n- id: \"R13-W3\"\n  summary: \"14B 'capacity-dependent convergence' claim 证据不足——仅 1 model family, 3 seeds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1 提出，R1 AGREE。14B 仅 Qwen3，TOST df=2 功效不足。应降级为 preliminary observation。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W5 + R2-N1 再次提出。R1 补充：gap 非单调（4B 1.32pp → 8B 2.62pp → 14B 1.07pp），与简单 capacity→convergence 叙事不完全一致。R2 解释非单调性：CWM 4B→8B flat 而 CLS 上升，8B→14B CWM catch up。两人共识：全文应一致用 'preliminary'。Director：resolved 维持——Abstract 和 Conclusion 已有 'preliminary observation' + 'single family' 限定。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 和 Conclusion 中 14B 结论标注为 preliminary observation\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Abstract: 'a preliminary observation consistent with capacity-dependent convergence'。Conclusion: 'Preliminary 14B results (3 seeds, single family)'。\"\n  resolution_round: 13\n\n- id: \"R13-W4\"\n  summary: \"GenRM 领域特异性对比分析不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4 提出，R1 AGREE。\"\n  action_items:\n    - round: 13\n      action: \"§5 新增分析代码 vs 数学验证的结构性差异\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Conclusion 扩展 GenRM 对比。\"\n  resolution_round: 13\n\n- id: \"R13-M1\"\n  summary: \"PRM/ORM 映射命名反直觉\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"§4 加入 'analogous' 限定和显式粒度映射说明。\"\n  resolution_round: 13\n\n- id: \"R13-M2\"\n  summary: \"Abstract 统计符号过密\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M1 提出，R1 AGREE。\"\n    - round: 15\n      reviewers: [2]\n      note: \"R2-W1 re-raises（Should-Fix）。R1 REBUT：对方法论论文 TOST 在 abstract 中合理，但同意 z=-23.7 可移除。Director：resolved 维持——Abstract repo-level 句已重构（R13 修复），z 值保留因为是关键效应量但括号化处理。\"\n  resolution: \"Abstract repo-level 句重构：先定性结论再括号统计支撑。\"\n  resolution_round: 13\n\n- id: \"R13-M3\"\n  summary: \"三项贡献独立性值得商榷\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Contribution 2 已重写为 negative result framing。\"\n  resolution_round: 13\n\n# === Round 14 Issues ===\n\n- id: \"R14-W1\"\n  summary: \"CWM default-to-pass 使 repo-level 准确率系统性失真\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"数据已在三处明确呈现。Reviewer 独立确认充分。\"\n  resolution_round: 14\n\n- id: \"R14-W2\"\n  summary: \"TOST one-sided p-values 未报告\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Appendix TOST Sensitivity 加入 one-sided 分解。\"\n  resolution_round: 14\n\n- id: \"R14-W3\"\n  summary: \"CWM baseline fairness——'collapses' framing 偏 formulation-inherent\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Conclusion 修改：'whether the repo-level divergence is formulation-inherent or capacity-contingent remains open'。\"\n  resolution_round: 14\n\n- id: \"R14-W4\"\n  summary: \"TRAJ 'matched comparison' 需在 Abstract 更早限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Abstract 修改：'No prior work compares CLS and CWM under matched conditions; the TRAJ comparison is inherently confounded.'。\"\n  resolution_round: 14\n\n- id: \"R14-W5\"\n  summary: \"PRM/ORM 映射粒度\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"§4 用 'analogous' 限定。\"\n  resolution_round: 14\n\n# === Round 15 (Fresh Review) New Issues ===\n\n- id: \"R15-W1\"\n  summary: \"'Collapses' 和 'driven by format collapse' 等因果措辞超出描述性/消融证据支撑范围\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-M1 提出，R2 AGREE。'equivalence collapses' 和 'driven by format collapse' 暗示因果关系，但证据是 observational + ablation。建议改为 'diverges' 和 'co-occurs with / is associated with'。两人达成共识。\"\n  action_items:\n    - round: 15\n      action: \"Abstract 'collapses' → 'diverges'；§3.5 'driven by format collapse' → 'accompanied by / associated with format collapse'\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R15-W2\"\n  summary: \"'Equivalence' 与 'parity' 术语混用——TOST formal 含义与 informal 用法混淆\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-M3 提出，R2 AGREE。'equivalence' 应仅指 TOST-confirmed results，其他用 'comparable' 或 'similar'。\"\n  action_items:\n    - round: 15\n      action: \"统一术语：TOST-confirmed 用 'equivalence'，其他用 'comparable/similar'\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R15-W3\"\n  summary: \"缺少 execution-based verification 作为 upper bound reference\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 部分 AGREE（nice-to-have 而非 must-fix）。论文核心是 execution-free 之间的比较，但 execution-based 的准确率作为参考有助读者判断提升空间。\"\n  action_items:\n    - round: 15\n      action: \"考虑在 Table 1 或 Table 3 加入 execution-based oracle 准确率行\"\n      assigned_to: \"paper\"\n      status: open\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "\n# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N2 re-raises（2-3 seeds, n=48, 5 confounds, 'collapses' 措辞）。R2 REBUT 指出 R1 混淆两个统计模型（z=-23.7 来自 139-cluster 交互 LPM 非 25-cluster 跨模型模型）。Director：R2 事实核查正确；R1 broader concern 仍有效但论文 §3.5/§3.7 hedging 已充分。Resolved 维持。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W2 re-raises low power (~0.3, n_eff≈86) 对非显著性结论的信息含量。R2 AGREE 但补充论文已用 TOST+Bayesian ROPE+14B scaling 三重互补验证。共识：正文应报告 repo-level effective sample size 和 MDE。Resolved 维持——§3.4 已有 power paragraph，Appendix H 已报告 MDE。\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13-R15 反复提及但无新增要求。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → final epoch). 但 R7 的 CLS epoch ablation (<1pp) 仍有效。新角度：CWM NaN val loss 可能是 formulation-inherent。\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。但 R2 REBUT：Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp。Director 裁定：证据表明 checkpoint 差异无法解释 18-26pp gap，降为 Should-Fix。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-N2 升级为 critical：论文持有 Qwen3 CWM step 300-400 optimal checkpoints 但未评估其 repo-level accuracy。R2 完全 AGREE。\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W4 re-raises：checkpoint ablation 仅在 Qwen3-4B CLS 上进行，未覆盖受影响最严重的 CWM 配置。DeepSeek CWM early-stop vs final-epoch ~18pp。R2 AGREE。Director：resolved status maintained——step-400 eval 数据已证明 early checkpoint ≤ final epoch，format collapse 从训练早期即存在。\"\n    - round: 14\n      reviewers: [2]\n      note: \"Fresh review R14. R2-W1 re-raises s42 用 step 400 vs s123/s456 用 step 6633 的配置异质性。R1 AGREE。Director：resolved 维持——step-400 eval 数据已证明早期 checkpoint 不改善结果。\"\n    - round: 15\n      reviewers: [1]\n      note: \"Fresh review R15. R1-W7 re-raises CWM checkpoint ablation 范围太窄（仅 Qwen3-8B）。R2 REBUT：Appendix N 已包含 DeepSeek-Coder CWM 分析（epoch1 75.45% vs epoch3 57.31%，但仍 66.4% unparseable）。Director：R2 事实核查正确，resolved 维持。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因（formulation-inherent vs implementation issue）\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文更显著讨论 checkpoint 缓解证据\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy 并报告结果\"\n      assigned_to: \"experiment\"\n      status: wont_fix\n    - round: 12\n      action: \"Appendix cwm_convergence 补充说明 step-level checkpoint 不可做的原因\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Step 300-400 checkpoints 未保存，但已找到现有 step-400 eval 数据（s42: 64.36% accuracy, 63.7% unparseable）。早期 checkpoint ≤ final epoch，直接反驳 'optimal early checkpoint closes gap' 假设。Format collapse 从训练早期即存在。数据写入 Appendix cwm_convergence。\"\n  resolution_round: 12\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1: 'design space' framing 过度. R1 部分同意.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1 再次标 CRITICAL。R1 AGREE 但认为 failure mode taxonomy 有独立贡献。两人共识：Findings 合适，Main 不够。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. R2 STILL_OPEN. R1 AGREE on assessment but argues exceptional soundness partially compensates. Both accept 3.0-3.5 range. Director: inherent limitation, wont_fix.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R2-N1 标 CRITICAL (Excitement 2/5)。R1 REBUT。最终分歧：R1 Excitement 3/5, R2 Excitement 2/5。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N1 再次标 CRITICAL：核心发现可从 §2.2 理论预测，属 confirmation 而非 discovery。R1 AGREE 但补充 quantitative boundary conditions（14B convergence, failure mode distribution）超越纯理论预测。两人 Excitement 均为 3/5。Director：inherent limitation，wont_fix 维持。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R2-N1 再次标 CRITICAL (Excitement 2.5/5)。R1 REBUT：function-level 等价阈值、failure mode taxonomy 分布、capacity-dependent convergence 量化均超越 §2.2 理论预测，建议降为 Should-Fix。Director：R1 REBUT 有说服力，不采纳为独立 issue。Inherent limitation，wont_fix 维持。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1 Excitement 3/5, R2 Excitement 2.5/5。R2-N1 隐含标 Critical（scale limitation → practical impact limited）。R1 REBUT：matched design 是文献中首个，有方法论贡献。Excitement 稳定在 2.5-3.0 范围。wont_fix 维持。\"\n  resolution: \"所有可行 action items 已完成。Excitement 稳定在 2.5-3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。Novelty ceiling 为 inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"SESOI 基于训练噪声量级独立于 observed gap.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。缺 domain-specific justification.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W4 re-raises：±2pp 依赖于 accuracy range 和 test set size。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-W1 re-raises：无 pre-registration，±1.52pp 临界值距 ±2pp 仅 0.48pp。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-M1 和 R1-Q1 再次提及 pre-registration 状态。R2 AGREE。§3.4 已改为 'motivated by domain considerations but was not pre-registered'，引用 sensitivity analysis。Director: resolved——已诚实披露，无进一步修改空间。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N1 标 Critical：鲁棒窗口仅 0.48pp。R2 AGREE with downgrade to Should-Fix：Bayesian ROPE 独立佐证 (P(ROPE)=0.975)、deployment relevance 论证合理、论文已透明披露。Director 采纳降级：Should-Fix。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W1 再次标 Must-Fix。R2 AGREE 部分但认为非 Must-Fix：§3.3 domain justification 合理（seed noise 0.37-0.97pp + checkpoint noise <1pp），最小 margin ±1.52pp 仅低 0.48pp，Bayesian ROPE P(ROPE)=0.975 独立佐证。共识：Table 13 sensitivity analysis 应移入正文。Director：resolved 维持——论文已诚实披露 post-hoc 状态，建议 rebuttal 中强调 sensitivity analysis。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；引用了 sensitivity analysis (Table tost_sensitivity)；明确承认结论对 margin 选择敏感。Bayesian ROPE 提供独立佐证。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入限定。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W6: 175× 数据量差异.\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：180× 差异 + signal granularity。R2 AGREE。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-W4 re-raises：downsample 控制了 volume 但未控制 label granularity。R2 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N2 标 CRITICAL：TRAJ 使用 ~400 vs ~70K 实例 + 不同 lr + variant-level labels，三方比较不受控。R1 完全 AGREE，补充：主文 Tables 1-3 无视觉标注 TRAJ 差异。Director 裁定：§3.5 已有 'exploratory' 标注和 confound 讨论，resolved 维持。但报告记录此为 persistent concern。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N3 标 Critical：lr 4×、数据量 175×、标签粒度三重差异使 'matched comparison' 不成立。R2 AGREE with qualification to Should-Fix：论文已有 ★ 标记 + §3.5 'exploratory' + Appendix N，但应在 Abstract/§1 更早限定。Director 采纳降级：Should-Fix。建议 Abstract 限定 'matched for CLS and CWM; TRAJ comparison is exploratory'。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W4 (Should-Fix) + R2-N3 (Must-Fix) 再次提出。R1 补充：数据效率是 formulation 固有属性，比较有 validity，但应更显著标记 exploratory。R2 认为根本性混淆。交叉后共识：TRAJ 比较应在 Table 1 caption 和 contribution statement 中明确标注 exploratory。Director：resolved 维持——Abstract 已有 'the TRAJ comparison is inherently confounded'（R14 修复），§3.5 有 exploratory 标注。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"Contribution summary 中明确表述 CLS-TRAJ repo-level 比较包含 training regime confound\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 标注 'The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity, a formulation-inherent confound.' Abstract 已有 'the TRAJ comparison is inherently confounded'。\"\n  resolution_round: 12\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"CodeRM, CodeScaler, GenPRM 等均已加入 Related Work。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"bar labels 偏小.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-M2: y-axis 不从零开始（55%），视觉夸大 gap。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED.\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-M2 和 R2-M2 均再次提及 y-axis 非零基线。Director：resolved——caption 已标注 'y-axis does not start at zero'，对 0-3pp 差异合理。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. 两位均再次提及。Caption 标注已存在。Resolved 维持。\"\n  resolution: \"Figure 2 caption 标注 'y-axis does not start at zero'，两位 Reviewer 一致确认合理。\"\n  resolution_round: 11\n\n# === Round 8 Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 15\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-N3 re-raises.\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-N1 再次标 CRITICAL：Abstract 'not confirmed' 在 power ~0.3 下 over-stated。R2 AGREE but 认为 Should-Fix（措辞问题非方法论缺陷）。Director 裁定 Should-Fix：§3.4 已诚实报告 power，问题在 Abstract/Conclusion 措辞。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W2 标 Must-Fix：power ~0.3 削弱结论。R2 AGREE 但补充 Bayesian ROPE (P(ROPE)=0.975) 不受 power 限制。共识：正文应报告 repo-level effective sample size 和 MDE。Director：resolved 维持——§3.4 power paragraph + Appendix H MDE 已充分披露。建议 rebuttal 引用 Bayesian ROPE 互补验证。\"\n  action_items:\n    - round: 9\n      action: \"Variant-level 分析明确标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文讨论 TOST 功效限制；Bayesian ROPE 补充\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"正文讨论 power ~0.3 意味着 '未确认' 不应解读为 '非等价'\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.4 已扩写 power paragraph，14B TOST 完成。Contribution 措辞保守。\"\n  resolution_round: 12\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Cross-seed oracle 已加入正文。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Appendix 已讨论。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM / RepoExec\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 15\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-W2 re-raises CWM 生态效度。R2 partially AGREE but notes §3.7 和 §5 已有 ≤8B 限定。Director: resolved——≤8B qualifier 已充分覆盖 Abstract/Conclusion/Threats.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R2-N2 标 Critical：14B 收敛至 0.43pp 暗示 capacity-driven。R1 AGREE。Director 裁定 Should-Fix（降级）：论文已有 qualifier（Abstract ≤8B, §3.3 scaling, Limitations），建议 Conclusion 更显著讨论 32B+ open question。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R2-N2 标 Must-Fix：CWM baseline 与 32B CWM 差异过大，domain difference claim 不可靠。R1 REBUT：匹配设计是方法论贡献而非缺陷——使用 32B CWM vs 4B CLS 则 capacity confound 更大。但 R1 同意 Conclusion domain-difference claim 应加条件限定。Director：R1 rebut 成立——matched design 的方法论价值独立于 scale；但 §5 GenRM 对比应明确加 '≤8B LoRA without trace pretraining' 条件。Resolved 维持。\"\n  resolution: \"合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。§5 Conclusion 已有 'under ≤8B LoRA protocol' 和 'capacity-contingent remains open'。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. 两人 Excitement 均为 3/5，Overall 均为 3.0 (Findings)。合并至 R6-N4 追踪。\"\n  resolution: \"合并至 R6-N4。Inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 15\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Both RESOLVED. GEE logistic regression added.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-M3 提及 LPM vs GEE 在 model identity 显著性上不一致（p=0.002 vs p=0.449）。论文已在 Appendix M 讨论 cluster 数限制。Director: resolved——Appendix M 已明确标注 estimator-dependent。\"\n    - round: 15\n      reviewers: [1]\n      note: \"Fresh review R15. R1-W6 re-raises LPM z=-23.7 可能膨胀。R2 REBUT：Appendix J 已报告完整 logistic regression 结果（OR=0.31, p=0.002, AME=-21.6pp），与 LPM concordant。R1 可能遗漏 Appendix J 第三段。Director：R2 事实核查正确，resolved 维持。建议正文 §3.5 加一句引用 logistic regression 结果。\"\n  resolution: \"Appendix M 补充 GEE logistic regression + estimator-dependent 标注。R15 R2 确认 Appendix J 已有完整 OR/CI/p/AME 报告。\"\n  resolution_round: 11\n\n# === Round 9 Issues ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大 gap。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却声称 'model-dependent'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Abstract 改为更审慎措辞。\"\n  resolution_round: 10\n\n- id: \"R9-M1\"\n  summary: \"Figure 3 y-axis 不从 0 开始但未标注\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Caption 标注。合并至 R6-M3。\"\n  resolution_round: 11\n\n- id: \"R9-M2\"\n  summary: \"Abstract 第一句过于绝对\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"已改为 'increasingly leverages'。\"\n  resolution_round: 10\n\n- id: \"R9-M3\"\n  summary: \"缺少方法论引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"两篇已引用。\"\n  resolution_round: 10\n\n- id: \"R9-M4\"\n  summary: \"Clustered bootstrap 实施细节\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§3.1 已说明。\"\n  resolution_round: 10\n\n- id: \"R9-M5\"\n  summary: \"Repo-level DEFF=114.3 → effective n≈86\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§5.2 加入 TOST power 段落。\"\n  resolution_round: 10\n\n# === Round 10 Issues ===\n\n- id: \"R10-W1\"\n  summary: \"Python-only 评估未在 Limitations 提及\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"Limitations 加入 Python-only 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-W2\"\n  summary: \"'formulation choice is governed by code complexity' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"'governed by' 改为 'moderated by'。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"3-shot ICL collapse 未充分讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"§5.4 扩展。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"Appendix 导航不便\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"Mini TOC 加入。\"\n  resolution_round: 10\n\n# === Round 11 Issues ===\n\n- id: \"R11-M1\"\n  summary: \"Figure 2 中 14B 数据点视觉等权\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Figure 2 已更新。\"\n  resolution_round: 11\n\n- id: \"R11-M2\"\n  summary: \"§3.5 LPM model identity vs GEE 需 qualifier\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Commit 0b38a2b 修复。\"\n  resolution_round: 11\n\n- id: \"R11-M3\"\n  summary: \"Abstract 'motivate routing' 暗示过度\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Abstract 已改含负结果量化。\"\n  resolution_round: 11\n\n# === Round 12 Issues ===\n\n- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"两人独立提出。14B function-level gap 收敛至 0.43pp 支持 capacity-driven 假设。\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W2 再次提及 CWM 生态效度。R2 partially AGREE but notes 论文已有充分 qualifier (§3.7, §5, Abstract). Director: resolved——所有 qualifier 已到位。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R2-N2 再次标 Critical，R1 AGREE。合并追踪至 R8-W6 round 14 mention。Director 裁定 Should-Fix（降级）。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R2-N1/N2 再次标 Must-Fix（scale limitation + CWM baseline fairness）。R1 REBUT matched design 方法论价值。Director：合并追踪至 R8-W6。Resolved 维持。\"\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。\"\n  resolution_round: 12\n\n- id: \"R12-N2\"\n  summary: \"Qwen3 CWM optimal checkpoint 未评估\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Step-400 eval 数据已找到（64.36% accuracy, 63.7% unparseable），反驳 'optimal early checkpoint closes gap' 假设。\"\n  resolution_round: 12\n\n- id: \"R12-N3\"\n  summary: \"CLS-TRAJ 等价性不对称结论可能是 power ~0.3 artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 提出，R2 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-N1 再次以更强力度提出：Abstract 'not confirmed' 在 power ~0.3 下 misleading。R2 AGREE (Should-Fix). Director: §3.4 power paragraph 已有充分披露，问题仅在 Abstract/Conclusion 措辞。见 R13-W1。\"\n  resolution: \"§3.4 power paragraph 扩写，14B TOST 完成。\"\n  resolution_round: 12\n\n- id: \"R12-W1\"\n  summary: \"Failure mode taxonomy 未列为独立贡献\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"§1 增加第三条贡献。\"\n  resolution_round: 12\n\n- id: \"R12-W2\"\n  summary: \"GenRM 对比发现未充分讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-W4 再次标 Should-Fix：Conclusion 仅 1 句话讨论 GenRM domain specificity，未分析 WHY。R1 AGREE 并建议用论文已有数据（parseable rate, inference efficiency）支撑分析。Director：Conclusion 段落已存在但确实过于简短。见 R13-W4。\"\n    - round: 15\n      reviewers: [2]\n      note: \"Fresh review R15. R2-N2 中包含 domain difference claim 批评。R1 同意 Conclusion domain claim 应加条件限定。§5 已有扩展讨论（output structure 假设 + unparseable rate）。Resolved 维持。\"\n  resolution: \"Conclusion 新增 GenRM domain-specificity 段落。\"\n  resolution_round: 12\n\n- id: \"R12-W3\"\n  summary: \"Preprocessing-checkpoint confound chain\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"§3.7 已加入 confound chain 描述。\"\n  resolution_round: 12\n\n- id: \"R12-W4\"\n  summary: \"CLS-CWM cross-seed pairing 局限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"§3.7 已加入 cross-seed pairing limitation。\"\n  resolution_round: 12\n\n- id: \"R12-M1\"\n  summary: \"§2.2 Failure Modes 位于 method section\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"R2-W3 re-raises：§2.2 预判实验结果，造成 confirmation bias 印象。R1 REBUT：先验分析是标准 hypothesis-driven research，且实验结果部分推翻了 §2.2 预测（CWM 独特退化非所有 formulation 均匀退化）。Director：R1 rebut 成立——§2.2 标题已为 'Expected Failure Modes'，是方法论步骤而非预判。\"\n  resolution: \"标题改为 'Expected Failure Modes'。R15 R1 rebut 成立。\"\n  resolution_round: 12\n\n- id: \"R12-M2\"\n  summary: \"Appendix G' 命名不直观\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"改为 G.1 subsection。\"\n  resolution_round: 12\n\n- id: \"R12-M3\"\n  summary: \"wei2022emergent 引用类型不一致\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"@inproceedings → @article。\"\n  resolution_round: 12\n\n- id: \"R12-M4\"\n  summary: \"Figure 2 float 漂移\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Figure 2 移入 experiments.tex。\"\n  resolution_round: 12\n\n# === Prior Round Issues ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n# === Round 13 Issues ===\n\n- id: \"R13-N1\"\n  summary: \"Appendix 'P: Limitations' 标题可能违反 EMNLP 格式规则（一篇文章只能有一个 limitations section）\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 提出，R2 完全 AGREE。EMNLP 2026 / ARR 规定 appendix 不能有 limitations section。Appendix 概览列出 'P: Limitations'，构成形式违规。\"\n  action_items:\n    - round: 13\n      action: \"将 Appendix P 'Extended limitations' 重命名为 'Extended Experimental Details' 或 'Additional Confound Analysis'，并从 Appendix 概览中移除 'P: Limitations' 标签\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Appendix P 重命名为 'Extended validity discussion'（采纳 Reviewer 建议），概览中同步更新。Checklist 中引用也已更新。\"\n  resolution_round: 13\n\n- id: \"R13-W1\"\n  summary: \"Abstract/Conclusion 中 TRAJ 'not confirmed' 措辞在 power ~0.3 下 over-stated——应加 power 限定语\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1 提出（标 Must-Fix），R2 AGREE 但认为 Should-Fix（§3.4 已诚实报告）。Director 裁定 Should-Fix。Abstract 'TRAJ parity is not confirmed after multiple comparison correction at any scale tested' 在 power ~0.3 下可能让读者误解为存在差异的证据。14B 收敛结果（1.07pp）应给予更突出位置。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 加入 power 限定语\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 13\n      action: \"Conclusion 明确讨论达到 power ≥0.8 所需的 seed 数量\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Abstract 加入 'at current power (~0.3)' 限定语。\"\n  resolution_round: 13\n\n- id: \"R13-W2\"\n  summary: \"Oracle 互补性应重新框定为 negative result + motivation，而非独立正面贡献\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 partial REBUT。Director 裁定 Should-Fix。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R2-W2 re-raises：<0.4pp routing + p=0.42 re-repair pilot → 实用价值近零。R1 AGREE 应降级为 exploratory finding。共识达成。Director：resolved 维持——Introduction Contribution 2 已重写为 negative result framing（R13 修复），明确 'simple routing heuristics capture <0.4pp, framing complementarity as motivation for future learned routers'。\"\n  action_items:\n    - round: 13\n      action: \"Contribution 2 措辞调整\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Introduction Contribution 2 重写：明确 simple routing heuristics capture <0.4pp of oracle gap，互补性 framed as 'motivation for future learned routers' 而非独立正面贡献。\"\n  resolution_round: 13\n\n- id: \"R13-W3\"\n  summary: \"14B 'capacity-dependent convergence' claim 证据不足——仅 1 model family, 3 seeds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1 提出，R1 AGREE。14B 仅 Qwen3，TOST df=2 功效不足。应降级为 preliminary observation。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W5 + R2-N1 再次提出。R1 补充：gap 非单调（4B 1.32pp → 8B 2.62pp → 14B 1.07pp），与简单 capacity→convergence 叙事不完全一致。R2 解释非单调性：CWM 4B→8B flat 而 CLS 上升，8B→14B CWM catch up。两人共识：全文应一致用 'preliminary'。Director：resolved 维持——Abstract 和 Conclusion 已有 'preliminary observation' + 'single family' 限定。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 和 Conclusion 中 14B 结论标注为 preliminary observation\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Abstract: 'a preliminary observation consistent with capacity-dependent convergence'。Conclusion: 'Preliminary 14B results (3 seeds, single family)'。\"\n  resolution_round: 13\n\n- id: \"R13-W4\"\n  summary: \"GenRM 领域特异性对比分析不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4 提出，R1 AGREE。\"\n  action_items:\n    - round: 13\n      action: \"§5 新增分析代码 vs 数学验证的结构性差异\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Conclusion 扩展 GenRM 对比。\"\n  resolution_round: 13\n\n- id: \"R13-M1\"\n  summary: \"PRM/ORM 映射命名反直觉\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"§4 加入 'analogous' 限定和显式粒度映射说明。\"\n  resolution_round: 13\n\n- id: \"R13-M2\"\n  summary: \"Abstract 统计符号过密\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M1 提出，R1 AGREE。\"\n    - round: 15\n      reviewers: [2]\n      note: \"R2-W1 re-raises（Should-Fix）。R1 REBUT：对方法论论文 TOST 在 abstract 中合理，但同意 z=-23.7 可移除。Director：resolved 维持——Abstract repo-level 句已重构（R13 修复），z 值保留因为是关键效应量但括号化处理。\"\n  resolution: \"Abstract repo-level 句重构：先定性结论再括号统计支撑。\"\n  resolution_round: 13\n\n- id: \"R13-M3\"\n  summary: \"三项贡献独立性值得商榷\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Contribution 2 已重写为 negative result framing。\"\n  resolution_round: 13\n\n# === Round 14 Issues ===\n\n- id: \"R14-W1\"\n  summary: \"CWM default-to-pass 使 repo-level 准确率系统性失真\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"数据已在三处明确呈现。Reviewer 独立确认充分。\"\n  resolution_round: 14\n\n- id: \"R14-W2\"\n  summary: \"TOST one-sided p-values 未报告\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Appendix TOST Sensitivity 加入 one-sided 分解。\"\n  resolution_round: 14\n\n- id: \"R14-W3\"\n  summary: \"CWM baseline fairness——'collapses' framing 偏 formulation-inherent\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Conclusion 修改：'whether the repo-level divergence is formulation-inherent or capacity-contingent remains open'。\"\n  resolution_round: 14\n\n- id: \"R14-W4\"\n  summary: \"TRAJ 'matched comparison' 需在 Abstract 更早限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Abstract 修改：'No prior work compares CLS and CWM under matched conditions; the TRAJ comparison is inherently confounded.'。\"\n  resolution_round: 14\n\n- id: \"R14-W5\"\n  summary: \"PRM/ORM 映射粒度\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"§4 用 'analogous' 限定。\"\n  resolution_round: 14\n\n# === Round 15 (Fresh Review) New Issues ===\n\n- id: \"R15-W1\"\n  summary: \"'Collapses' 和 'driven by format collapse' 等因果措辞超出描述性/消融证据支撑范围\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-M1 提出，R2 AGREE。'equivalence collapses' 和 'driven by format collapse' 暗示因果关系，但证据是 observational + ablation。建议改为 'diverges' 和 'co-occurs with / is associated with'。两人达成共识。\"\n  action_items:\n    - round: 15\n      action: \"Abstract 'collapses' → 'diverges'；§3.5 'driven by format collapse' → 'accompanied by / associated with format collapse'\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R15-W2\"\n  summary: \"'Equivalence' 与 'parity' 术语混用——TOST formal 含义与 informal 用法混淆\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-M3 提出，R2 AGREE。'equivalence' 应仅指 TOST-confirmed results，其他用 'comparable' 或 'similar'。\"\n  action_items:\n    - round: 15\n      action: \"统一术语：TOST-confirmed 用 'equivalence'，其他用 'comparable/similar'\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R15-W3\"\n  summary: \"缺少 execution-based verification 作为 upper bound reference\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 部分 AGREE（nice-to-have 而非 must-fix）。论文核心是 execution-free 之间的比较，但 execution-based 的准确率作为参考有助读者判断提升空间。\"\n  action_items:\n    - round: 15\n      action: \"考虑在 Table 1 或 Table 3 加入 execution-based oracle 准确率行\"\n      assigned_to: \"paper\"\n      status: open\n"
  }
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-23T14:41:32.914498+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 37844}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-23T14:43:20.408057+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1295 · 2026-05-23T14:43:20.458671+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1296 · 2026-05-23T14:44:59.946817+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "\n# Round 15 Consolidated Review Report\n\n**Paper**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 (ARR May cycle)\n**Reviewers**: R1 (方法与实验严谨性), R2 (新颖性与完整性)\n**Cross-sharing**: 完成，双方逐条回应\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free 验证公式（CLS 逐测试分类、CWM 执行输出生成、TRAJ 轨迹级评分）在代码修复验证任务上的表现。在 function-level，CLS 和 CWM 统计等价（TOST p=0.007, 5 seeds）；在 repo-level（≤8B LoRA），CWM 出现 18–26pp 的性能下降（z=−23.7），>50% 输出不可解析。初步 14B 结果（3 seeds, 单一模型族）将所有公式差距缩小至 1.07pp 以内。论文提出 complexity-moderated formulation choice 作为核心 contribution，并提供 failure mode taxonomy。\n\n---\n\n## Strengths\n\n**S1. 实验设计严谨，统计方法全面 [共识]**\nTOST 等价检验 + Bayesian ROPE + 聚类 bootstrap + Holm-Bonferroni 校正 + mixed-effects 回归，构成多层统计验证。5 seeds 复现，ICC 报告，seed variance 分析完整。这在 NLP/SE 交叉领域论文中属于上乘水平。\n\n**S2. 研究问题有明确实践价值 [共识]**\nExecution-free verification 是 APR pipeline 的实际瓶颈，比较不同公式的选择对 practitioner 有直接指导意义。\n\n**S3. Failure mode taxonomy 提供诊断价值 [共识]**\n对 CWM 的 format collapse（53–74% unparseable at repo-level）进行了系统归因，包括 truncation、delimiter errors、hallucinated outputs，超越了简单的 accuracy 比较。\n\n**S4. 写作质量较高 [共识]**\n论文结构清晰，statistical claims 有适当 qualifier（如 \"preliminary\"、\"exploratory\"），threats to validity 部分诚实全面。Abstract 控制在 200 words 以内。\n\n**S5. 开源承诺 [R1]**\n承诺公开代码和数据，有利于可复现性。\n\n---\n\n## Weaknesses\n\n### 重大问题 (Major)\n\n**W1. 规模限制削弱核心 claim 的普适性 [共识，严重程度有分歧]**\n≤8B LoRA 是唯一完整复现的设置；14B 仅限 Qwen3 单一模型族、3 seeds。核心发现\"CLS ≈ CWM at function-level, CLS >> CWM at repo-level\"可能是容量不足的 artifact 而非公式的固有差异。论文自己承认 14B 已将差距缩小到 1.07pp——这恰恰暗示 repo-level 的 divergence 可能在更大规模下消失。\n\n- R1 评估：论文已用 \"preliminary\" 和 \"capacity-contingent\" 做了 hedge，但主张仍以 ≤8B 为基础，可接受但需加强 qualifier\n- R2 评估：这是根本性限制，8B 结果可能 3–6 个月内被推翻，降低了 contribution 的持久性\n- **Director 判定**：这是本文最大的 validity threat。论文的 hedging 是到位的，但 ≤8B 作为唯一 fully-replicated 设置，读者难以判断哪些 findings 会 survive scaling。建议在 introduction 和 conclusion 更显著地标注 scale caveat。\n\n**W2. TRAJ 比较的公平性问题 [共识]**\nTRAJ 使用 patch-level binary verdict（1 token），而 CLS 使用 per-test classification。TRAJ 缺少 per-test diagnostic granularity 是设计决定而非公式固有限制——可以设计 per-test TRAJ。论文将 TRAJ 的劣势归因于 \"inherent confounding\"，但部分劣势来自特定实现选择。\n\n- 两位 Reviewer 均同意 TRAJ 比较应标注为 exploratory\n- **Director 判定**：论文应明确 TRAJ 的 granularity 差异是 design choice 而非 inherent limitation\n\n**W3. CWM baseline 强度存疑 [分歧]**\nCWM 使用 matched LoRA rank/data 与 CLS 对比，但未探索对 CWM 更有利的设置（如更长 max_length、专门的 format-compliance pretraining、constrained decoding）。>50% unparseable 可能是工程问题而非公式问题。\n\n- R1 认为：matched design 是 controlled comparison 的正确做法，not a weakness\n- R2 认为：CWM 的 format failure 是 straw man，fair comparison 应给 CWM 充分工程支持\n- **Director 判定**：两种立场都有道理。论文的 matched design 符合实验方法论，但应在 discussion 中明确承认 CWM 可能从 format-specific interventions 获益，并将此列为 future work\n\n**W4. 因果语言过强 [共识]**\n多处使用 \"reveals\"、\"demonstrates\"、\"confirms\" 等因果性措辞描述观察性结果。例如 \"we attribute the domain difference to output structure\" 暗示因果关系，但实际是 post-hoc 解释。\n\n### 次要问题 (Minor)\n\n**M1. SESOI 敏感性分析应在正文提及 [共识]**\n±2pp SESOI 是核心等价检验的关键参数，但敏感性分析仅在 Appendix D。至少应在正文 §3.4 用一句话提及不同 SESOI 下结论的稳健性。\n\n**M2. \"Formulation\" vs \"Task framing\" 术语不一致 [R2, R1 部分同意]**\n论文交替使用 formulation、task framing、output format，可能造成混淆。建议在 §2.1 统一定义后一致使用。\n\n**M3. 缺少 execution upper bound [R2]**\n没有报告实际执行测试的 accuracy 作为 ceiling，读者无法判断 execution-free 方法距离 practical utility 有多远。\n\n**M4. Complementarity 结论力度 [共识]**\nError complementarity 被列为 contribution 之一，但实际是 negative result（互补性不足以 justify ensemble）。建议明确标注为 negative result 并调低措辞力度。\n\n---\n\n## Reviewer Consensus\n\n1. 统计方法论是本文最大亮点，显著优于同领域论文平均水平\n2. SESOI 敏感性分析应在正文有所体现\n3. TRAJ 比较应标注为 exploratory 而非 definitive\n4. 14B 结果需保持 \"preliminary\" qualifier\n5. Complementarity 应明确为 negative result\n6. 因果性语言需全文 softening\n\n## Reviewer Divergence\n\n1. **Scale limitation 严重程度**：R1 (3.5) 认为论文 hedging 充分，是 reasonable scope choice；R2 (3.0) 认为这是根本性限制，可能导致核心 finding 过时。Director 倾向 R2——scale limitation 的影响确实可能使 repo-level findings 的 shelf life 较短。\n2. **CWM baseline 公平性**：R1 认为 matched comparison 方法正确；R2 认为 CWM 需要更多工程支持。Director 认为双方各有道理，需在 discussion 中 acknowledge。\n\n---\n\n## Questions for Authors\n\nQ1. 14B 结果将差距缩小至 1.07pp——作者是否认为 repo-level divergence 会在 32B+ 完全消失？如果是，§3.5 的 repo-level findings 的实际价值是什么？\n\nQ2. CWM 的 >50% unparseable rate 在加入 constrained decoding 或 format-specific fine-tuning 后会如何变化？是否做过相关 pilot experiment？\n\nQ3. 为什么没有包含 execution-based oracle 作为 upper bound？这对评估 practical gap 至关重要。\n\nQ4. TRAJ 如果改为 per-test 粒度（逐测试生成 pass/fail），是否仍然 underperform CLS？\n\nQ5. ICC = 0.191 (function-level) 意味着 seed variance 非常大。这是否暗示 5 seeds 不足以稳定估计？\n\n---\n\n## Missing References\n\n- **RepoExec** (Nam et al., 2025): 已引用但未深入讨论其 repo-level execution verification 方法论与本文的异同\n- **CodeScaler** (Zhu et al., 2026): 已引用，execution-free reward model 的相关工作覆盖较完整\n- 建议补充：最近的 constrained decoding for structured output 文献（如 Guidance, Outlines），与 CWM format compliance 问题直接相关\n\n---\n\n## External Review\n\n未启用（status: not_requested）。\n\n---\n\n## Visual Layout Check\n\n**Status**: 已完成 (0 critical, 4 warnings, 9 info)\n\nWarnings:\n1. 最后一页近空（仅含少量 references），空间利用率低\n2. Pages 1–2 无 display items（图/表），纯文本密度较高\n3. Appendix 部分存在较长纯文本段落\n4. 部分 figure caption 与正文存在少量冗余\n\n所有 info items 为正面评价（排版整体规范、图表质量可接受）。无需因视觉问题调整评分。\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 — Findings**\n\n**Soundness**: 3.0 — 统计方法论优秀，但核心 finding（repo-level divergence）的 generalizability 受限于 ≤8B scale，且 14B 已显示 convergence trend，削弱了结论的稳健性。\n\n**Excitement**: 2.5 — 研究问题实用，但 formulation comparison 在 ≤8B 的 finding 可能短期内被 scaling 结果推翻。Contribution 的 lasting impact 存疑。\n\n**Justification**: 论文在方法论上表现出色——统计严谨性显著优于同领域平均水平，failure mode taxonomy 有诊断价值，写作清晰。然而，核心 empirical finding 建立在 ≤8B 这一可能不再代表 frontier 的 scale 上，14B 的 convergence 趋势进一步削弱了 repo-level divergence 这一主要 contribution 的持久性。TRAJ 比较的公平性问题和 CWM baseline 的工程优化空间也使部分结论的 definitiveness 打折。作为 Findings paper，方法论贡献（统计框架 + failure taxonomy）足以支撑，但距离主会议的 excitement 和 impact 标准有差距。\n\n**Recommendation**: Findings 可接受。若要冲击主会议，需要 (1) 32B+ 规模的完整复现，(2) CWM 加入 format-aware 优化后的对比，(3) execution-based upper bound。\n\n---\n\n## Detailed Comments\n\n### For Authors\n\n1. **Introduction §1**: \"we reveal that complexity moderates the classification–generation tradeoff\" — \"reveal\" 暗示因果发现，建议改为 \"we observe\" 或 \"our results suggest\"\n\n2. **§2.1**: 建议在此处统一 \"formulation\" 的定义，并在全文一致使用，避免与 \"task framing\"、\"output format\" 混用\n\n3. **§3.4**: TOST 等价检验后，添加一句：SESOI 敏感性分析见 Appendix D，±1pp 和 ±3pp 下结论 [稳健/变化]\n\n4. **§3.5**: Repo-level 结果段落开头应加入显著的 scale caveat：\"The following results are established under ≤8B LoRA; preliminary 14B evidence (§3.3) suggests these gaps may narrow at larger scales.\"\n\n5. **§3.6 Complementarity**: 将 \"error complementarity analysis\" 改为 \"error complementarity analysis (negative result)\"，明确标注\n\n6. **Conclusion**: \"we presented the first systematic comparison\" — 考虑加入 \"at ≤8B scale\" qualifier\n\n7. **Table 1/2/3**: 表格清晰，但建议在 caption 中标注 seed count（5 seeds for ≤8B, 3 seeds for 14B）\n\n8. **Limitations**: 当前覆盖了 scale、language、synthetic data 三个点，长度合适。可考虑添加半句关于 CWM 未做 format-aware optimization 的 acknowledgment\n",
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "\n# Round 15 Consolidated Review Report\n\n**Paper**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 (ARR May cycle)\n**Reviewers**: R1 (方法与实验严谨性), R2 (新颖性与完整性)\n**Cross-sharing**: 完成，双方逐条回应\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free 验证公式（CLS 逐测试分类、CWM 执行输出生成、TRAJ 轨迹级评分）在代码修复验证任务上的表现。在 function-level，CLS 和 CWM 统计等价（TOST p=0.007, 5 seeds）；在 repo-level（≤8B LoRA），CWM 出现 18–26pp 的性能下降（z=−23.7），>50% 输出不可解析。初步 14B 结果（3 seeds, 单一模型族）将所有公式差距缩小至 1.07pp 以内。论文提出 complexity-moderated formulation choice 作为核心 contribution，并提供 failure mode taxonomy。\n\n---\n\n## Strengths\n\n**S1. 实验设计严谨，统计方法全面 [共识]**\nTOST 等价检验 + Bayesian ROPE + 聚类 bootstrap + Holm-Bonferroni 校正 + mixed-effects 回归，构成多层统计验证。5 seeds 复现，ICC 报告，seed variance 分析完整。这在 NLP/SE 交叉领域论文中属于上乘水平。\n\n**S2. 研究问题有明确实践价值 [共识]**\nExecution-free verification 是 APR pipeline 的实际瓶颈，比较不同公式的选择对 practitioner 有直接指导意义。\n\n**S3. Failure mode taxonomy 提供诊断价值 [共识]**\n对 CWM 的 format collapse（53–74% unparseable at repo-level）进行了系统归因，包括 truncation、delimiter errors、hallucinated outputs，超越了简单的 accuracy 比较。\n\n**S4. 写作质量较高 [共识]**\n论文结构清晰，statistical claims 有适当 qualifier（如 \"preliminary\"、\"exploratory\"），threats to validity 部分诚实全面。Abstract 控制在 200 words 以内。\n\n**S5. 开源承诺 [R1]**\n承诺公开代码和数据，有利于可复现性。\n\n---\n\n## Weaknesses\n\n### 重大问题 (Major)\n\n**W1. 规模限制削弱核心 claim 的普适性 [共识，严重程度有分歧]**\n≤8B LoRA 是唯一完整复现的设置；14B 仅限 Qwen3 单一模型族、3 seeds。核心发现\"CLS ≈ CWM at function-level, CLS >> CWM at repo-level\"可能是容量不足的 artifact 而非公式的固有差异。论文自己承认 14B 已将差距缩小到 1.07pp——这恰恰暗示 repo-level 的 divergence 可能在更大规模下消失。\n\n- R1 评估：论文已用 \"preliminary\" 和 \"capacity-contingent\" 做了 hedge，但主张仍以 ≤8B 为基础，可接受但需加强 qualifier\n- R2 评估：这是根本性限制，8B 结果可能 3–6 个月内被推翻，降低了 contribution 的持久性\n- **Director 判定**：这是本文最大的 validity threat。论文的 hedging 是到位的，但 ≤8B 作为唯一 fully-replicated 设置，读者难以判断哪些 findings 会 survive scaling。建议在 introduction 和 conclusion 更显著地标注 scale caveat。\n\n**W2. TRAJ 比较的公平性问题 [共识]**\nTRAJ 使用 patch-level binary verdict（1 token），而 CLS 使用 per-test classification。TRAJ 缺少 per-test diagnostic granularity 是设计决定而非公式固有限制——可以设计 per-test TRAJ。论文将 TRAJ 的劣势归因于 \"inherent confounding\"，但部分劣势来自特定实现选择。\n\n- 两位 Reviewer 均同意 TRAJ 比较应标注为 exploratory\n- **Director 判定**：论文应明确 TRAJ 的 granularity 差异是 design choice 而非 inherent limitation\n\n**W3. CWM baseline 强度存疑 [分歧]**\nCWM 使用 matched LoRA rank/data 与 CLS 对比，但未探索对 CWM 更有利的设置（如更长 max_length、专门的 format-compliance pretraining、constrained decoding）。>50% unparseable 可能是工程问题而非公式问题。\n\n- R1 认为：matched design 是 controlled comparison 的正确做法，not a weakness\n- R2 认为：CWM 的 format failure 是 straw man，fair comparison 应给 CWM 充分工程支持\n- **Director 判定**：两种立场都有道理。论文的 matched design 符合实验方法论，但应在 discussion 中明确承认 CWM 可能从 format-specific interventions 获益，并将此列为 future work\n\n**W4. 因果语言过强 [共识]**\n多处使用 \"reveals\"、\"demonstrates\"、\"confirms\" 等因果性措辞描述观察性结果。例如 \"we attribute the domain difference to output structure\" 暗示因果关系，但实际是 post-hoc 解释。\n\n### 次要问题 (Minor)\n\n**M1. SESOI 敏感性分析应在正文提及 [共识]**\n±2pp SESOI 是核心等价检验的关键参数，但敏感性分析仅在 Appendix D。至少应在正文 §3.4 用一句话提及不同 SESOI 下结论的稳健性。\n\n**M2. \"Formulation\" vs \"Task framing\" 术语不一致 [R2, R1 部分同意]**\n论文交替使用 formulation、task framing、output format，可能造成混淆。建议在 §2.1 统一定义后一致使用。\n\n**M3. 缺少 execution upper bound [R2]**\n没有报告实际执行测试的 accuracy 作为 ceiling，读者无法判断 execution-free 方法距离 practical utility 有多远。\n\n**M4. Complementarity 结论力度 [共识]**\nError complementarity 被列为 contribution 之一，但实际是 negative result（互补性不足以 justify ensemble）。建议明确标注为 negative result 并调低措辞力度。\n\n---\n\n## Reviewer Consensus\n\n1. 统计方法论是本文最大亮点，显著优于同领域论文平均水平\n2. SESOI 敏感性分析应在正文有所体现\n3. TRAJ 比较应标注为 exploratory 而非 definitive\n4. 14B 结果需保持 \"preliminary\" qualifier\n5. Complementarity 应明确为 negative result\n6. 因果性语言需全文 softening\n\n## Reviewer Divergence\n\n1. **Scale limitation 严重程度**：R1 (3.5) 认为论文 hedging 充分，是 reasonable scope choice；R2 (3.0) 认为这是根本性限制，可能导致核心 finding 过时。Director 倾向 R2——scale limitation 的影响确实可能使 repo-level findings 的 shelf life 较短。\n2. **CWM baseline 公平性**：R1 认为 matched comparison 方法正确；R2 认为 CWM 需要更多工程支持。Director 认为双方各有道理，需在 discussion 中 acknowledge。\n\n---\n\n## Questions for Authors\n\nQ1. 14B 结果将差距缩小至 1.07pp——作者是否认为 repo-level divergence 会在 32B+ 完全消失？如果是，§3.5 的 repo-level findings 的实际价值是什么？\n\nQ2. CWM 的 >50% unparseable rate 在加入 constrained decoding 或 format-specific fine-tuning 后会如何变化？是否做过相关 pilot experiment？\n\nQ3. 为什么没有包含 execution-based oracle 作为 upper bound？这对评估 practical gap 至关重要。\n\nQ4. TRAJ 如果改为 per-test 粒度（逐测试生成 pass/fail），是否仍然 underperform CLS？\n\nQ5. ICC = 0.191 (function-level) 意味着 seed variance 非常大。这是否暗示 5 seeds 不足以稳定估计？\n\n---\n\n## Missing References\n\n- **RepoExec** (Nam et al., 2025): 已引用但未深入讨论其 repo-level execution verification 方法论与本文的异同\n- **CodeScaler** (Zhu et al., 2026): 已引用，execution-free reward model 的相关工作覆盖较完整\n- 建议补充：最近的 constrained decoding for structured output 文献（如 Guidance, Outlines），与 CWM format compliance 问题直接相关\n\n---\n\n## External Review\n\n未启用（status: not_requested）。\n\n---\n\n## Visual Layout Check\n\n**Status**: 已完成 (0 critical, 4 warnings, 9 info)\n\nWarnings:\n1. 最后一页近空（仅含少量 references），空间利用率低\n2. Pages 1–2 无 display items（图/表），纯文本密度较高\n3. Appendix 部分存在较长纯文本段落\n4. 部分 figure caption 与正文存在少量冗余\n\n所有 info items 为正面评价（排版整体规范、图表质量可接受）。无需因视觉问题调整评分。\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 — Findings**\n\n**Soundness**: 3.0 — 统计方法论优秀，但核心 finding（repo-level divergence）的 generalizability 受限于 ≤8B scale，且 14B 已显示 convergence trend，削弱了结论的稳健性。\n\n**Excitement**: 2.5 — 研究问题实用，但 formulation comparison 在 ≤8B 的 finding 可能短期内被 scaling 结果推翻。Contribution 的 lasting impact 存疑。\n\n**Justification**: 论文在方法论上表现出色——统计严谨性显著优于同领域平均水平，failure mode taxonomy 有诊断价值，写作清晰。然而，核心 empirical finding 建立在 ≤8B 这一可能不再代表 frontier 的 scale 上，14B 的 convergence 趋势进一步削弱了 repo-level divergence 这一主要 contribution 的持久性。TRAJ 比较的公平性问题和 CWM baseline 的工程优化空间也使部分结论的 definitiveness 打折。作为 Findings paper，方法论贡献（统计框架 + failure taxonomy）足以支撑，但距离主会议的 excitement 和 impact 标准有差距。\n\n**Recommendation**: Findings 可接受。若要冲击主会议，需要 (1) 32B+ 规模的完整复现，(2) CWM 加入 format-aware 优化后的对比，(3) execution-based upper bound。\n\n---\n\n## Detailed Comments\n\n### For Authors\n\n1. **Introduction §1**: \"we reveal that complexity moderates the classification–generation tradeoff\" — \"reveal\" 暗示因果发现，建议改为 \"we observe\" 或 \"our results suggest\"\n\n2. **§2.1**: 建议在此处统一 \"formulation\" 的定义，并在全文一致使用，避免与 \"task framing\"、\"output format\" 混用\n\n3. **§3.4**: TOST 等价检验后，添加一句：SESOI 敏感性分析见 Appendix D，±1pp 和 ±3pp 下结论 [稳健/变化]\n\n4. **§3.5**: Repo-level 结果段落开头应加入显著的 scale caveat：\"The following results are established under ≤8B LoRA; preliminary 14B evidence (§3.3) suggests these gaps may narrow at larger scales.\"\n\n5. **§3.6 Complementarity**: 将 \"error complementarity analysis\" 改为 \"error complementarity analysis (negative result)\"，明确标注\n\n6. **Conclusion**: \"we presented the first systematic comparison\" — 考虑加入 \"at ≤8B scale\" qualifier\n\n7. **Table 1/2/3**: 表格清晰，但建议在 caption 中标注 seed count（5 seeds for ≤8B, 3 seeds for 14B）\n\n8. **Limitations**: 当前覆盖了 scale、language、synthetic data 三个点，长度合适。可考虑添加半句关于 CWM 未做 format-aware optimization 的 acknowledgment\n",
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 1297 · 2026-05-23T14:45:03.864998+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3918
}
```

</details>

---


### Assistant

_source line 1298 · 2026-05-23T14:45:10.689790+00:00_

Round 15 审稿报告已投递。

**结果摘要**：
- **Overall Score**: 3.0 (Findings)
- R1: 3.5 (Borderline Conference) / R2: 3.0 (Findings)
- **核心共识**：统计方法论优秀，但 ≤8B scale 限制削弱 repo-level findings 的 generalizability，14B convergence 趋势进一步压缩 contribution 空间
- **主要分歧**：scale limitation 严重程度（R2 认为根本性，R1 认为可接受）、CWM baseline 公平性
- **升主会议路径**：需 32B+ 完整复现 + CWM format-aware 优化 + execution upper bound

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 116

## Round 116

2 recorded events


### User

_source line 1299 · 2026-05-23T14:45:13.276065+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 所有 Weaknesses (W1-W7, M1-M4) 和 Questions (Q1-Q6) 的逐条回应，并提交给 Review Director。

核心判断摘要：
- **[AGREE]** W1（SESOI sensitivity 应在正文）、W2（low power 需标注 inconclusive）、W4（TRAJ 训练 confound）、W5（14B 结论需更 cautious）、M1/M2/M3
- **[REBUT]** W3（论文已有反证排除 truncation/checkpoint causal chain）、W6（Appendix J 已报告 logistic regression OR/p）、W7（Appendix N 已含 DeepSeek checkpoint 分析）、M4（appendix 长度不是问题）
- 与 R1 的主要分歧：R1 侧重统计方法论修补（3.5 Borderline Conference），我认为 **≤8B 规模限制** 是更根本的问题（3.0 Findings）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1300 · 2026-05-23T14:45:22.425556+00:00_

审稿报告已于上一轮提交完成（Overall 3.0 — Findings）。两位 Reviewer 的初审和交叉回应均已纳入，issue tracker 已同步更新。本轮审稿结束。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 117

## Round 117

58 recorded events


### User

_source line 1301 · 2026-05-23T14:54:34.376979+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1302 · 2026-05-23T14:54:39.990951+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1303 · 2026-05-23T14:54:40.041988+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1304 · 2026-05-23T14:54:47.420725+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-23T14:54:47.421125+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1306 · 2026-05-23T14:54:50.988973+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1307 · 2026-05-23T14:54:50.989346+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1308 · 2026-05-23T14:54:55.558464+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 1309 · 2026-05-23T14:54:56.461951+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (266 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D13
…[truncated 1825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1310 · 2026-05-23T14:54:56.462430+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1311 · 2026-05-23T14:54:56.514408+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1312 · 2026-05-23T14:54:59.777441+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 1313 · 2026-05-23T14:55:01.635979+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1314 · 2026-05-23T14:55:01.686676+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\usepackage{xcolor}
21	\graphicspath{{../../artifacts/}}
22	
23	% Lists
24	\usepackage{enumitem}
25	
26	% Custom commands
27	\newcommand{\cls}{\textsc{Cls}}
28	\newcommand{\cwm}{\textsc{Cwm}}
29	\newcommand{\traj}{\textsc{Traj}}
30	\newcommand{\fone}{F\textsubscript{1}}
31	\newcommand{\pp}{\,\text{pp}}
32	\newcommand{\tbd}{\textsc{tbd}}
33	\newcommand{\placeholder}[1]{{\color{red}\texttt{[#1]}}}
34	
35	\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}
36	\author{Anonymous}
37	
38	\begin{document}
39	\maketitle
40	
41	\input{abstract}
42	
43	\input{introduction}
44	
45	\begin{figure*}[t]
46	\centering
47	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
48	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
49	\label{fig:reformulation}
50	\end{figure*}
51	
52	\input{method}
53	
54	\input{experiments}
55	
56	
57	\input{related_work}
58	
59	\input{conclusion}
60	
61	\bibliography{references}
62	
63	% ARR checklist is filled in OpenReview submission form, not in PDF
64	% \input{checklist}
65	
66	\input{appendix}
67	
68	\end{document}
69	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1315 · 2026-05-23T14:55:07.624378+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's what I found about EMNLP 2026 call for papers submission guidelines and ARR:

## Main Submission Information

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Key Requirements and Policies

- All accepted papers must be presented at the conference to appear in the pro
…[truncated 881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 7846
}
```

</details>

---


### Tool call

_source line 1316 · 2026-05-23T14:55:12.194268+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline page limit format requirements long paper short paper",
  "allowed_domains": "['2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline page limit format requirements long paper short paper",
    "allowed_domains": "['2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 1317 · 2026-05-23T14:55:14.606845+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1318 · 2026-05-23T14:55:15.009030+00:00_

1	\begin{abstract}
2	LLM-based repair generates candidate patches, selecting the best via a verifier. Three execution-free alternatives to expensive execution-based verification have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level scoring (\traj{}). No prior work compares \cls{} and \cwm{} under matched conditions; the \traj{} comparison is inherently confounded.
3	
4	We present the first systematic comparison across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is not confirmed after multiple comparison correction at current power (${\sim}$0.3), but the gap narrows monotonically from 3.11\pp{} (4B) to 1.07\pp{} (14B). At repository level, this equivalence diverges ($z{=}-23.7$, DeepSeek-Coder): the \cls{}--\cwm{} gap widens to 18--26\pp{} across 2--3 seeds under our ${\leq}$8B LoRA protocol, accompanied by format collapse. At 14B (3 seeds, single family), all three formulations narrow to within 1.07\pp{}, a preliminary observation consistent with capacity-dependent convergence.
5	
6	Error complementarity and a failure mode taxonomy motivate complexity-aware routing, though simple heuristics capture $<$0.4\pp{} of oracle advantage.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1319 · 2026-05-23T14:55:15.059787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1320 · 2026-05-23T14:55:15.512202+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. This connects to a broader pattern in NLP: task formulation---classification vs.\ generation vs.\ span extraction---systematically affects performance~\cite{raffel2020t5}, but the conditions under which each wins remain task-dependent and empirically unresolved. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We pres
…[truncated 3215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1321 · 2026-05-23T14:55:15.512607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1322 · 2026-05-23T14:55:15.613277+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Expected Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation has charact
…[truncated 3341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1323 · 2026-05-23T14:55:22.225540+00:00_

Web search results for query: "EMNLP 2026 submission deadline page limit format requirements long paper short paper"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"}]

I found information about page limits for long and short papers, but let me search for more specific details about submission deadlines and format requirements.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"EMNLP 2026
…[truncated 3131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 10031
}
```

</details>

---


### Tool call

_source line 1324 · 2026-05-23T14:55:26.391130+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1325 · 2026-05-23T14:55:27.345248+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench}; runs with NaN validation loss (due to truncated targets exceeding 2,048-token limits) default to the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Qwen3 \cwm{} runs show early overfitting (best at ${\sim}$6\% of training); checkpoint details in Appendix~\ref{app:hyperparams}.
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model
…[truncated 20384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-23T14:55:27.345703+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1327 · 2026-05-23T14:55:27.547045+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. CodeScaler~\cite{zhu2026codescaler} trains execution-free reward models for both RL and test-time scaling. Verification formulations span trajectory-level reward~\cite{shum2025swerm}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. GenRM~\cite{hosseini2025genrm} and GenPRM~\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formula
…[truncated 1495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1328 · 2026-05-23T14:55:27.597879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-23T14:55:27.648512+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} equivalence is not confirmed after correction, but the gap narrows monotonically to 1.07\pp{} at 14B. At repository level under ${\leq}$8B LoRA, divergence reaches 18--26\pp{} ($z{=}-23.7$), consistent across families (\S\ref{sec:threats}). Preliminary 14B results (3 seeds, single family) narrow all gaps to within 1.07\pp{}; whether the repo-level divergence is formulation-inherent or capacity-contingent remains open. This contrasts with mathematical reasoning, where generative verification outperforms discriminative~\cite{hosseini2025genrm}; we hypothesize this reflects output structure---code verification requires exact-match outputs (${\sim}$477 tokens/test for \cwm{} vs.\ 1 for \cls{}), and $>$50\% of repo-level \cwm{} outputs are unparseable, in which generation becomes a format fidelity challenge absent in math.
5	
6	Three directions follow: (1)~complexity-aware routing; (2)~scaling to 32B+ with more seeds~\cite{meta2025cwm}; (3)~per-test diagnostics for downstream repair.
7	
8	\section*{Limitations}
9	
10	Primary findings use ${\leq}$8B LoRA fine-tuning with multi-seed replication; 14B results use a single model family (Qwen3) with 3 seeds; cross-family replication and evaluation at 32B+ are needed. The repo-level gap may diminish at 32B+ scale or with execution-trace pretraining~\cite{meta2025cwm}. All evaluation uses Python-only benchmarks; other languages may exhibit different format compliance rates. Training data uses synthetic mutation operators~\cite{andrews2005mutation,just2014mutants}; the synthetic-to-real transfer gap remains untested (Appendix~\ref{app:limitations}). Format-specific interventions (constrained decoding, output-format pretraining) may mitigate \cwm{}'s format 
…[truncated 32 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1330 · 2026-05-23T14:55:32.065687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-23T14:55:32.819679+00:00_

1	\appendix
2	
3	\noindent\textbf{Appendix overview.} A: Oracle resolve advantage. B: Ablation studies. C-F: Extended analysis (error complementarity, parseable accuracy, forced parsing, qualitative errors, failed interventions, mutation scaling, inference efficiency, re-repair, chain-of-thought). G: TOST sensitivity (G.1: Bayesian ROPE). H: Effect sizes. I: Holm-Bonferroni. J: Mixed-effects regression. K: Parseable bias. L: CWM convergence. M: Few-shot. N: Threats. O: Downsample. P: Extended validity discussion.
4	
5	\section{Oracle Accuracy-Utility Analysis}
6	\label{app:oracle}
7	
8	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
14	\label{tab:oracle}
15	\resizebox{\columnwidth}{!}{%
16	\setlength{\tabcolsep}{3pt}
17	\begin{tabular}{lcccc}
18	\toprule
19	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
20	\midrule
21	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
22	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
23	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
24	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
25	\midrule
26	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
31	\begin{figure}[h]
32	\centering
33	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
34	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%,
…[truncated 58552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 1332 · 2026-05-23T14:55:32.820122+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1333 · 2026-05-23T14:55:32.921025+00:00_

1	% === Statistical Methods ===
2	
3	@article{cameron2008bootstrap,
4	  author    = {A. Colin Cameron and Jonah B. Gelbach and Douglas L. Miller},
5	  title     = {Bootstrap-Based Improvements for Inference with Clustered Errors},
6	  journal   = {Review of Economics and Statistics},
7	  volume    = {90},
8	  number    = {3},
9	  pages     = {414--427},
10	  year      = {2008},
11	}
12	
13	@book{wellek2010,
14	  author    = {Stefan Wellek},
15	  title     = {Testing Statistical Hypotheses of Equivalence and Noninferiority},
16	  publisher = {Chapman and Hall/CRC},
17	  edition   = {2nd},
18	  year      = {2010},
19	}
20	
21	@article{moulton1990,
22	  author  = {Brent R. Moulton},
23	  title   = {An Illustration of a Pitfall in Estimating the Effects of Aggregate Variables on Micro Units},
24	  journal = {The Review of Economics and Statistics},
25	  volume  = {72},
26	  number  = {2},
27	  pages   = {334--338},
28	  year    = {1990},
29	}
30	
31	@book{cohen1988,
32	  author    = {Cohen, Jacob},
33	  title     = {Statistical Power Analysis for the Behavioral Sciences},
34	  edition   = {2nd},
35	  publisher = {Lawrence Erlbaum Associates},
36	  year      = {1988}
37	}
38	
39	@article{kruschke2013bayesian,
40	  title={Bayesian estimation supersedes the t test},
41	  author={Kruschke, John K},
42	  journal={Journal of Experimental Psychology: General},
43	  volume={142},
44	  number={2},
45	  pages={573--603},
46	  year={2013},
47	  publisher={American Psychological Association}
48	}
49	
50	@article{kruschke2018rejecting,
51	  title={Rejecting or accepting parameter values in {B}ayesian estimation},
52	  author={Kruschke, John K},
53	  journal={Advances in Methods and Practices in Psychological Science},
54	  volume={1},
55	  number={2},
56	  pages={270--280},
57	  year={2018},
58	  publisher={SAGE Publications}
59	}
60	
61	% === Execution Simulation ===
62	
63	@inproceedings{gu2024cruxeval,
64	  title={{CRUXEval}: A Benchmark for Code Reasoning, Understanding and Exec
…[truncated 1535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-23T14:56:08.462977+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_14/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_14/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1335 · 2026-05-23T14:56:08.915290+00:00_

-rw-r--r-- 1 ubuntu ubuntu 430551 May 23 14:52 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_14/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1336 · 2026-05-23T14:56:09.216907+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "decisions.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-23T14:56:09.317972+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml\", \"content\": \"_next_id: 171\\ndecisions:\\n- id: D001\\n  date: 2026-05-11 18:01 UTC\\n  summary: 'MVP 方案: Monte Carlo oracle 模拟 + 函数级 pilot，不依赖 Docker 基础设施'\\n  rationale: '完整 Part 1 需要 Docker 重新评估 8K 个 patch 获取 per-test labels（16-24h），基础设施搭建成本高。MVP\\n    改用 Monte Carlo 模拟参数化真实测试数分布验证理论信息增益，函数级 pilot (HumanEval/MBPP) 验证可学习性。两者均无需 Docker，2-3\\n    天可完成。Pass 标准: per-test 在 70-85% 精度下 resolve rate 比 trajectory-level 高 ≥5%; 函数级\\n    pilot 精度 >70%。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-11 19:07 UTC\\n  summary: MVP-A 有条件通过：F2P-only block-corr 10.88%>5%；需补跑 Total(F2P+P2P) 模拟确认全图\\n  rationale: 真实 SWE-bench F2P median=1（69% 实例仅 1 个 F2P 测试），但 P2P median=50.5。F2P-only\\n    下 per-test 优势收窄但仍过阈值（block-corr 10.88%）。P2P regression 检测是更大的信号源——Total 分布(median=52)下优势预期更强。研究方向需校准：per-test\\n    价值主要来自 P2P regression 检测 + F2P multi-test 精确定位，而非单纯的 F2P 粒度。\\n  related_experiments:\\n  - exp_id: mvp-a-oracle-sim\\n    role: evidence\\n    result: F2P-only block-corr advantage 10.88%, i.i.d. 1.98%\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-11 19:38 UTC\\n  summary: P2P regression rate 是项目关键前提——≥10% per-test 有效，<5% 则有害；需实测\\n  rationale: Total 模拟(F2P+P2P)显示 per-test 优势强烈依赖 P2P regression rate：5% 时优势为负(-1%)，10%\\n    时 13.2%，20% 时 35.7%。这是从 F2P-only 分析未发现的关键变量。真实 regression rate 未知，需从 SWE-bench\\n    数据/文献中实测。此数据点决定项目是否可行及论文 story 如何构建。\\n  related_experiments:\\n  - exp_id: mvp-a-oracle-sim\\n    role: evidence\\n    result: 'Total sim: reg=5% adv=-1%, reg=10% adv=13.2%, reg=20% adv=35.7%'\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-11 20:05 UTC\\n  summary: P2P 回归率 ~1%，原始 Total 优势前提不成立；项目 reframe 而非 kill\\n  rationale: P2P 回归率 ~1%（mean=1.04%, median=0%, 仅 22.6% 错误 patch 破坏任何 P2P 测试），远低于\\n    per-test 有效的 10% 阈值。Total(F2P+P2P) 模型下 per-test 实际有害（噪声>信号）。但项目核心价值不在信
…[truncated 3564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1338 · 2026-05-23T14:56:15.492235+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1339 · 2026-05-23T14:56:15.542940+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-23T14:56:28.098751+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-23T14:56:28.150245+00:00_

&lt;persisted-output>
Output too large (44.2KB). Full output saved to: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier--claude-sessions-review-director-06def7c3/f20c5a67-fb58-4aa1-b1c9-2645507cbfc2/tool-results/baa4nlgn3.txt

Preview (first 2KB):
# === Round 6 Issues (Original) ===

# --- Round 6 Must-Fix (Consensus Critical) ---

- id: "R6-N1"
  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 6
  last_seen_round: 15
  mentions:
    - round: 6
      reviewers: [1, 2]
      note: "两人独立提出，最高共识。"
    - round: 7
      reviewers: [pre-review]
      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress."
    - round: 8
      reviewers: [1, 2]
      note: "Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp."
    - round: 9
      reviewers: [1, 2]
      note: "Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported."
    - round: 10
      reviewers: [1, 2]
      note: "Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations."
    - round: 11
      reviewers: [1, 2]
      note: "Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion."
    - round: 13
      reviewers: [1]
      note: "Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label prese
…[truncated 175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1342 · 2026-05-23T14:56:28.201012+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 1343 · 2026-05-23T14:56:28.856300+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (266 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D13
…[truncated 1825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 1344 · 2026-05-23T14:56:44.419319+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review configuration"
  }
}
```

</details>

---


### Tool result

_source line 1345 · 2026-05-23T14:56:44.470009+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1346 · 2026-05-23T14:56:47.737418+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1347 · 2026-05-23T14:56:47.838590+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1348 · 2026-05-23T14:56:53.365009+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16 -maxdepth 2 -name \"*.yaml\" -path \"*/config*\" -o -name \"project_config*\" 2>/dev/null | head -10; grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/ 2>/dev/null | head -5 || echo \"NONE\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16 -maxdepth 2 -name \"*.yaml\" -path \"*/config*\" -o -name \"project_config*\" 2>/dev/null | head -10; grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/ 2>/dev/null | head -5 || echo \"NONE\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1349 · 2026-05-23T14:56:53.669357+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_eval_cls-v5-urgent_20260513T155329.log:{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_01RowKtG2FtAW8XwpEB4vmoD","type":"tool_result","content":"1\t\"\"\"MCP Server — exposes SSH, W&B, and Registry tools via the Model Context Protocol.\n2\t\n3\tUsage:\n4\t    python -m core.mcp_server          # stdio transport (default, for Claude Code)\n5\t    python -m core.mcp_server --sse    # SSE transport (for remote clients)\n6\t\"\"\"\n7\t\n8\tfrom __future__ import annotations\n9\t\n10\timport json\n11\timport logging\n12\timport os\n13\tfrom dataclasses import asdict\n14\tfrom pathlib import Path\n15\tfrom typing import Any\n16\t\n17\tlogger = logging.getLogger(__name__)\n18\t\n19\tfrom mcp.server.fastmcp import FastMCP\n20\t\n21\tfrom core.tools import (\n22\t    artifacts as artifacts_mod,\n23\t    architecture as architecture_mod,\n24\t    clone_repo as clone_repo_mod,\n25\t    cron, feishu, feishu_group as feishu_group_mod,\n26\t    external_review as external_review_mod,\n27\t    file_parser as file_parser_mod,\n28\t    gpu_monitor as gpu_monitor_mod,\n29\t    image_tools as image_tools_mod,\n30\t    model_registry as model_registry_mod,\n31\t    oss_backup, pai_eas, s3_backup,\n32\t    project_config, registry, ssh, wandb_client, workspace,\n33\t    worker as worker_mod,\n34\t)\n35\t\n36\t# ----------------------------------------------
…[truncated 15409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 304
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-23T14:57:00.146399+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 1351 · 2026-05-23T14:57:00.598546+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1352 · 2026-05-23T14:57:00.699396+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 1353 · 2026-05-23T14:57:04.772198+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4072
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-23T14:57:40.642146+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。\n\n## Venue 信息\n- **EMNLP 2026 Long Paper (ARR May cycle)**\n- 截止日期: 2026-05-25\n- 页数限制: 正文 8 页（不含 references 和 limitations）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind (ARR)\n- 附录: 允许，参与审稿\n- References: 无页数限制\n- Limitations section: 必须包含，不计入页数限制\n- ARR Responsible NLP Checklist: 在 OpenReview form 中填写，不在 PDF 中\n- Overall Assessment 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n重点审查以下方面，给出 **逐条**、**引用具体 Section/Table/Figure** 的意见：\n\n1. **统计方法论**：TOST 等价检验的 margin 选择是否合理？Holm-Bonferroni 校正是否正确应用？Bayesian ROPE 与 frequentist 结论是否一致？\n2. **实验控制**：CLS vs CWM vs TRAJ 的比较是否公平？是否存在未充分控制的 confound（训练数据量、sequence length、checkpoint 选择等）？\n3. **Threats to validity**：作者识别的 5 个 confound 是否全面？是否有遗漏的重要 confound？\n4. **Seed 覆盖与统计功效**：function-level 5 seeds vs repo-level 2-3 seeds，TOST power ~0.3，是否足够支撑核心 claims？\n5. **因果推断**：repo-level 的 CLS-CWM 18-26pp gap 是否能归因为 formulation 差异？还是 confound 混杂的结果？\n6. **可复现性**：hyperparameters、数据处理、evaluation protocol 的描述是否足够详细？\n\n请产出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号 W1/W2/...）、Questions（Q1/Q2/...）、Missing References、Overall Assessment + 评分 + 置信度。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。\n\n## Venue 信息\n- **EMNLP 2026 Long Paper (ARR May cycle)**\n- 截止日期: 2026-05-25\n- 页数限制: 正文 8 页（不含 references 和 limitations）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind (ARR)\n- 附录: 允许，参与审稿\n- References: 无页数限制\n- Limitations section: 必须包含，不计入页数限制\n- ARR Responsible NLP Checklist: 在 OpenReview form 中填写，不在 PDF 中\n- Overall Assessment 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n重点审查以下方面，给出 **逐条**、**引用具体 Section/Table/Figure** 的意见：\n\n1. **统计方法论**：TOST 等价检验的 margin 选择是否合理？Holm-Bonferroni 校正是否正确应用？Bayesian ROPE 与 frequentist 结论是否一致？\n2. **实验控制**：CLS vs CWM vs TRAJ 的比较是否公平？是否存在未充分控制的 confound（训练数据量、sequence length、checkpoint 选择等）？\n3. **Threats to validity**：作者识别的 5 个 confound 是否全面？是否有遗漏的重要 confound？\n4. **Seed 覆盖与统计功效**：function-level 5 seeds vs repo-level 2-3 seeds，TOST power ~0.3，是否足够支撑核心 claims？\n5. **因果推断**：repo-level 的 CLS-CWM 18-26pp gap 是否能归因为 formulation 差异？还是 confound 混杂的结果？\n6. **可复现性**：hyperparameters、数据处理、evaluation protocol 的描述是否足够详细？\n\n请产出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号 W1/W2/...）、Questions（Q1/Q2/...）、Missing References、Overall Assessment + 评分 + 置信度。"
  }
}
```

</details>

---


### Tool result

_source line 1355 · 2026-05-23T14:57:53.268186+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12626
}
```

</details>

---


### Tool call

_source line 1356 · 2026-05-23T14:57:53.421018+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 的审查。\n\n## Venue 信息\n- **EMNLP 2026 Long Paper (ARR May cycle)**\n- 截止日期: 2026-05-25\n- 页数限制: 正文 8 页（不含 references 和 limitations）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind (ARR)\n- 附录: 允许，参与审稿\n- References: 无页数限制\n- Limitations section: 必须包含，不计入页数限制\n- ARR Responsible NLP Checklist: 在 OpenReview form 中填写，不在 PDF 中\n- Overall Assessment 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n重点审查以下方面，给出 **逐条**、**引用具体 Section/Table/Figure** 的意见：\n\n1. **新颖性**：论文的核心贡献是否足够新颖？\"第一个系统比较\"的 claim 是否成立？是否有被忽略的 prior art 做过类似比较？\n2. **Related work 覆盖**：引用是否全面？是否遗漏了重要的相关工作（特别是 2025-2026 的新工作）？GenRM/GenPRM/CodeRM 等的讨论是否准确？\n3. **论证逻辑**：从 function-level equivalence 到 repo-level divergence 的 narrative 是否连贯？\"complexity-dependent\" 的 framing 是否有充分的实验支撑？\n4. **写作质量**：abstract 是否清晰且在 200 words 以内？Introduction 的 contribution list 是否准确反映了实验结果？是否存在 overclaim 或 underclaim？\n5. **格式合规**：正文是否在 8 页以内？Limitations section 是否存在且合理？匿名是否合规（无作者信息泄露）？\n6. **Presentation 完整性**：Table/Figure 是否清晰、信息完整？是否有关键实验结果缺失或放在 appendix 中而主文缺乏总结？\n7. **Domain positioning**：与 math reasoning 领域的 GenRM 结论形成对比——这个 cross-domain 比较是否合理？\n\n请产出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号 W1/W2/...）、Questions（Q1/Q2/...）、Missing References、Overall Assessment + 评分 + 置信度。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 的审查。\n\n## Venue 信息\n- **EMNLP 2026 Long Paper (ARR May cycle)**\n- 截止日期: 2026-05-25\n- 页数限制: 正文 8 页（不含 references 和 limitations）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind (ARR)\n- 附录: 允许，参与审稿\n- References: 无页数限制\n- Limitations section: 必须包含，不计入页数限制\n- ARR Responsible NLP Checklist: 在 OpenReview form 中填写，不在 PDF 中\n- Overall Assessment 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n重点审查以下方面，给出 **逐条**、**引用具体 Section/Table/Figure** 的意见：\n\n1. **新颖性**：论文的核心贡献是否足够新颖？\"第一个系统比较\"的 claim 是否成立？是否有被忽略的 prior art 做过类似比较？\n2. **Related work 覆盖**：引用是否全面？是否遗漏了重要的相关工作（特别是 2025-2026 的新工作）？GenRM/GenPRM/CodeRM 等的讨论是否准确？\n3. **论证逻辑**：从 function-level equivalence 到 repo-level divergence 的 narrative 是否连贯？\"complexity-dependent\" 的 framing 是否有充分的实验支撑？\n4. **写作质量**：abstract 是否清晰且在 200 words 以内？Introduction 的 contribution list 是否准确反映了实验结果？是否存在 overclaim 或 underclaim？\n5. **格式合规**：正文是否在 8 页以内？Limitations section 是否存在且合理？匿名是否合规（无作者信息泄露）？\n6. **Presentation 完整性**：Table/Figure 是否清晰、信息完整？是否有关键实验结果缺失或放在 appendix 中而主文缺乏总结？\n7. **Domain positioning**：与 math reasoning 领域的 GenRM 结论形成对比——这个 cross-domain 比较是否合理？\n\n请产出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号 W1/W2/...）、Questions（Q1/Q2/...）、Missing References、Overall Assessment + 评分 + 置信度。"
  }
}
```

</details>

---


### Tool result

_source line 1357 · 2026-05-23T14:57:54.836157+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1415
}
```

</details>

---


### Assistant

_source line 1358 · 2026-05-23T14:58:01.005409+00:00_

Round 1 已分配：

- **Reviewer 1**（方法严谨性 + 实验设计）→ 已触发
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）→ 已触发
- **视觉审查 Agent** → 已派发（并行执行）
- **外部审稿** → 未配置，跳过

等待两位 Reviewer 返回独立审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 118

## Round 118

2 recorded events


### User

_source line 1359 · 2026-05-23T15:04:43.880840+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 统计方法论扎实、附录极为详尽的实证比较研究，但核心 claim 受限于低统计功效（CLS–TRAJ）、有限的模型规模范围（≤8B, 2 families）和合成数据外部效度，实际贡献偏向于一篇高质量的 Findings 论文而非主会议论文。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 (Strong) | TOST + Holm-Bonferroni + Bayesian ROPE + ICC + mixed-effects LPM 的多层统计框架设计严谨，核心 CLS≈CWM 等价结论在多种分析下保持稳健；但 CLS–TRAJ 的统计功效仅 ~0.3，该比较本质上是无信息的 |
| Excitement | 3/5 (Interesting) | 填补了 verification formulation 系统比较的空白，complexity-dependent routing 有实用价值；但核心发现（简单任务上 formulation 无差异、复杂任务上 CWM 崩溃）在直觉上可预测，缺乏 surprising insight |
| Confidence | 4/5 | 熟悉统计检验方法论、代码修复评估和 LLM fine-tuning 实验设计 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] CLS–TRAJ 等价检验的统计功效不足以支撑任何结论，但论文叙述暗示"未确认等价"等同于"可能不等价"

- 具体位置：Section 3.4 ("TRAJ equivalence is not confirmed after Holm correction"), Abstract ("TRAJ equivalence is not confirmed"), Section 5 Conclusion
- 问题：TOST power ~0.3（Appendix J, n_var=96 after clustering）意味着即使 CLS 和 TRAJ 真正等价，也有 70% 的概率检测不到。在如此低功效下，"未确认等价"是一个空洞的陈述——既不能说明等价，也不能说明不等价。但 Abstract 和 Conclusion 的措辞（"TRAJ purity is not confirmed"）容易让读者误读为"TRAJ 可能不等价"，这是一种方向性偏误。Bayesian ROPE P(ROPE)=0.542 at variant level（Appendix J.1）同样是 inconclusive，但论文未在正文中充分强调这一 inconclusive 性质。
- 为什么影响接收：CLS–TRAJ 比较是论文三组比较之一（CLS-CWM, CLS-TRAJ, repo-level divergence），若该比较实际上 uninformative，则论文的核心贡献缩水约 1/3。审稿人和读者可能基于 "TRAJ equivalence is not confirmed" 得出错误的实践建议。
- 建议修改方向：(1) 在 Abstract 和 Section 3.4 中明确使用 "underpowered; no conclusion can be drawn" 而非 "not confirmed"；(2) 报告达到 power=0.8 所需的最小样本量（论文已有 n_min=350），并讨论获取该样本量的可行性；(3) 考虑将 CLS–TRAJ 比较降级为 exploratory analysis。

**N2** [critical] Repo-level 2–3 seeds 无法支撑 18–26pp gap 的 formulation 归因

- 具体位置：Section 3.5, Table 3, Figure 2 (repo-level panel), Appendix O
- 问题：Repo-level 实验仅使用 2–3 seeds（Table 3 footnote: "CLS 2 seeds; DeepSeek CLS 2 seeds"）。CLS–CWM 的 18–26pp gap 基于极少的独立观测。虽然 per-test 有 ~1K 个数据点，但 training seed 才是真正的 replication unit。以 n=2-3 计算，bootstrap CI 的可靠性极低。Appendix O 的 Threats to Validity 虽然列出了 5 个 confound，但均未通过增加 seed 来实验性地分离。Mixed-effects LPM（Appendix M）虽然用 n=56,480 per-test observations 发现 formulation×complexity 交互显著（z=−23.7），但这些 observations 在 seed 内部高度相关（ICC=0.191），有效自由度远低于名义值。
- 为什么影响接收：如果 gap 的一部分来自 seed-level 变异、checkpoint selection artifact（Appendix O 承认 NaN validation loss）、或 CWM 的 formal collapse（Section 3.6: 53–74% unparseable），则 "formulation divergence" 的归因可能是 overstated。
- 建议修改方向：(1) 在正文中报告 seed-level variance 的 effect size（目前仅在 Appendix K 中有）；(2) 对 repo-level 结论加入更强的 hedging 语言，如 "preliminary evidence consistent with" 而非 "the gap widens"；(3) 讨论需要多少 repo-level seeds 才能达到合理功效。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] TOST 等价 margin ±2pp 的选择缺乏正式论证

- 具体位置：Section 3.4, Appendix J (Table 13)
- 问题：论文称 margin "set based on deployment relevance"（Section 3.4），但未给出推导过程。在医学和工业领域，equivalence margin 通常基于 minimal clinically important difference (MCID) 或行业标准。对于 code verification accuracy，2pp 在 85% baseline 上约为 2.4% relative change——这是否属于 "practitioner-irrelevant" 需要论证。Appendix J 的 sensitivity analysis（Table 13）显示 equivalence 在 ±1.52pp 仍成立，这有帮助但不替代前置论证。
- 建议：增加一段讨论 2pp margin 的 rationale，例如对比 downstream repair success rate 的变化幅度，或引用 code generation 领域的先例。

**W2** [warning] 训练数据量的严重不对称未被充分控制

- 具体位置：Appendix E (Table 11), Section 3.7
- 问题：CLS 训练集约 ~70K function-level instances（CLS 和 CWM 共享），但经过不同 preprocessing 后实际数量不同：CLS uses train.unified.py dropping samples exceeding max_seq_length (3,405 of 70,748 samples), CWM uses train.repo.cwm.py truncating and retaining all samples。这导致 CLS 的有效训练数据量 vs CWM 不同。更重要的是，TRAJ 仅使用 1,386 variant-level instances——数量级差距巨大。虽然 matched-context ablation（Appendix B）声称 "input dispute explains at most 3% of the difference"，但这仅控制了 input overlap，未控制 training set size 本身的效应。
- 建议：(1) 报告 downsample CLS/CWM 到 TRAJ 数据量后的对照实验（已有 page 16 的 CLS-format TRAJ 实验，但方向相反）；(2) 在 Threats to Validity 中显式讨论 data volume confound。

**W3** [warning] DeepSeek-Coder 仅 2 seeds 导致跨模型比较可信度降低

- 具体位置：Table 1 (function-level), Table 3 (repo-level)
- 问题：Qwen3 使用 5 seeds，DeepSeek-Coder 仅 2 seeds。Table 1 中 DeepSeek 的 CI 未报告（仅有均值），Table 3 的 DeepSeek 行也是 2 seeds。论文声称 "cross-model consistency"（Section 3.3: "CLS > CWM across all seeds"），但 2 seeds 的 cross-seed variance 估计极不稳定。
- 建议：明确报告 DeepSeek 的 seed-level variance，并对 cross-model 结论加入 caveat。

**W4** [warning] CWM formal collapse 是 confound 还是 inherent formulation property 的界限不清

- 具体位置：Section 3.6 (53–74% unparseable at repo level), Appendix N, Table 4
- 问题：CWM 在 repo-level 有 53–74% 的输出 unparseable（formal collapse），defaulting to majority class (PASS)。Appendix N 的 parseable bias analysis 表明这实质性地膨胀了 CWM 的表观准确率。问题是：formal collapse 是 CWM formulation 的 inherent limitation（因此 gap 可以归因于 formulation），还是可以通过 constrained decoding 或更好的训练解决的 engineering artifact？如果是后者，18–26pp gap 不应被解释为 "formulation difference" 而应是 "current implementation gap"。论文在 page 17 报告了四种 interventions（capacity ×2, majority voting, relaxed matching, LoRA rank 32）均失败，但这只覆盖了有限的 intervention 空间。
- 建议：在 Discussion 中明确区分 inherent formulation limitation vs. engineering optimization gap，并讨论 constrained decoding（Limitations 中提到但未实验验证）是否可能解决 formal collapse。

**W5** [warning] 外部效度受限于合成数据和 Python-only

- 具体位置：Limitations section (page 8), Appendix E
- 问题：所有训练数据来自 synthetic mutation operators（5 types: gold unmodified, operator_swap, return_value, off_by_one, boundary_removal），评估在 SWE-bench Verified 上。合成 mutation 和真实 developer patch 的分布差异可能系统性地影响 formulation 比较的结论——例如 CWM 可能在真实 patch 的长输出上表现不同。Python-only 的限制也在 Limitations 中提到但未深入讨论。
- 建议：讨论 mutation type distribution（Table 12, Appendix G）与真实 bug 分布的差异，以及这如何可能影响各 formulation 的相对表现。

**W6** [warning] Mixed-effects LPM 的有效自由度问题

- 具体位置：Appendix M
- 问题：Cross-complexity LPM 使用 n=56,480 per-test observations，但 25-cluster random intercept 限制了有效自由度。论文使用 GEE 作为 robustness check（p=0.149 and p=0.006），结果与 LPM 部分不一致。具体地，formulation×model interaction 在 LPM 下 p=0.002 但 GEE 下 non-significant。论文选择报告 "GEE's more conservative cluster-robust inference" 但未解释为何同一数据在两种模型下给出不同结论——这可能反映 model specification sensitivity。
- 建议：在 Appendix M 中增加一段讨论 LPM vs GEE discrepancy 的原因（可能是 cluster size heterogeneity 或 working correlation structure 选择），并明确哪个模型更可信及为什么。

---

## Questions（希望作者回答）

**Q1**: CLS–TRAJ 比较中，TRAJ 的 training data 仅 1,386 instances vs CLS 的 ~70K。作者是否做过 downsample CLS 到类似数量的实验？如果 CLS 在 1,386 instances 上也表现类似 TRAJ，那么 formulation 差异的结论就不成立。

**Q2**: Repo-level CWM 的 formal collapse（53–74% unparseable）在 constrained decoding（如 grammar-guided generation）下是否可以缓解？如果是，18–26pp gap 中有多少归因于 decoding strategy 而非 formulation？

**Q3**: 论文使用 SWE-bench Verified 的 oracle resolve rate 作为 upper bound（Table 5, Appendix A）。但 oracle scoring 假设 "a patch is correct iff T_fp = ∅"。对于部分正确的 patch（通过部分 test 但非全部），oracle 会将其标为 incorrect。这是否低估了 verifier 的实际价值？

**Q4**: Figure 2 的 repo-level panel 显示 CWM 在 4B→8B 时从 1.32pp 涨到 2.62pp，但附带 "formal collapse" 的注释。如果去除 unparseable outputs（即只看 parseable subset），CLS vs CWM 的 repo-level gap 是否缩小或反转？

**Q5**: Mixed-effects regression（Appendix M）中 formulation×complexity interaction 的 z=−23.7 看似极端。这个巨大 z-value 是否主要由 n=56,480 的巨大样本量驱动（而非大 effect size）？请报告 interaction 的 odds ratio 或 marginal effect。

---

## 小问题（不影响接收）

- Abstract 约 195 words，接近 200-word 限制但合规。
- Table 1 中 DeepSeek-Coder 的 "2 seeds" 注释容易被忽略（在 table caption 中），建议在表格内标注。
- Section 3.4 "We test pairwise equivalence on 523 variant-level instances across five seeds" — 但 DeepSeek 只有 2 seeds。应明确这是 Qwen3-only 分析还是 pooled 分析。
- Appendix 标题使用 A-P 共 16 个，数量庞大。建议在 Appendix 开头增加一个简要的 roadmap 或 table of contents（如果尚未有的话——从 page 11 看似乎已有 overview）。
- Figure 1 的三个 formulation diagrams 信息密度高但字体偏小，建议检查 camera-ready 中的可读性。

---

## Missing References

- **Constrained decoding for code generation**: Limitations 中提到但未引用具体工作，如 Scholak et al. (2021) PICARD 或 Synchromesh (Poesia et al., 2022)——这些与 CWM formal collapse 的缓解直接相关。
- **Equivalence testing in ML**: 论文引用了 Wellek (2010) 和 Lakens (2017)，但未引用 ML 领域越来越多的 equivalence testing 应用，如 Dror et al. (2018) "The Hitchhiker's Guide to Testing Statistical Significance in NLP" 中对 equivalence 的讨论。

---

## 主要优势

1. **统计方法论的深度和一致性**：TOST + Holm-Bonferroni + Bayesian ROPE + ICC + clustered bootstrap + mixed-effects LPM 的多层验证框架在 NLP 实证论文中罕见，且每种方法的适用性和局限性都有讨论。这是论文的最大亮点。
2. **诚实的 negative results 报告**：CLS–TRAJ 功效不足、四种 intervention 全部失败（page 17）、CWM parseable bias（Appendix N）等均被坦率报告，而非隐藏或淡化。
3. **Failure mode taxonomy 有实用价值**：formal collapse / decision collapse / aggregation penalty 的分类（Section 3.6, Table 4）为 practitioners 提供了可操作的诊断框架。
4. **Error complementarity 分析**（Section 3.5）揭示了 routing heuristic 的潜力，虽然 oracle advantage 仅 <0.4pp，但这一 negative result 本身也有价值。
5. **15 页附录**覆盖了几乎所有可以想到的 ablation 和 robustness check，反映了实验的严谨程度。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1360 · 2026-05-23T15:04:52.434033+00:00_

R1 报告已收到。等待 R2 报告到达后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 119

## Round 119

2 recorded events


### User

_source line 1361 · 2026-05-23T15:04:58.570362+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3.5 (Borderline Conference), Soundness 4/5, Excitement 3/5**。

主要发现：
- 统计框架（TOST + Holm-Bonferroni + Bayesian ROPE + mixed-effects LPM）是论文最大亮点，在 NLP 实证论文中罕见
- 两个 critical 问题：(1) CLS–TRAJ 等价检验 power ~0.3 导致该比较 uninformative，但论文措辞暗示"可能不等价"；(2) Repo-level 仅 2–3 seeds 无法可靠支撑 18–26pp gap 的 formulation 归因
- 六个 should-fix 问题涵盖 TOST margin 论证、训练数据量不对称、DeepSeek 仅 2 seeds、CWM formal collapse 的定性归因模糊、外部效度、mixed-effects 模型 specification sensitivity
- 提出 5 个 questions，重点关注 data volume confound 的控制实验和 constrained decoding 对 formal collapse 的潜在缓解

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1362 · 2026-05-23T15:05:04.132690+00:00_

收到 R1 的审稿报告。等待 R2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 120

## Round 120

6 recorded events


### User

_source line 1363 · 2026-05-23T15:08:03.563185+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：A Systematic Comparison of Execution-Free Verification Formulations for Code Repair

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 方法论严谨的经验比较研究，回答了实践者关心的问题，但核心发现（短输出等价、长输出生成退化）的可预测性限制了新颖性，且 "complexity-dependent" 的核心叙事存在未解耦的混淆因素。

---

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5 / 5 | 实验设计严谨（5 seeds, TOST, Bayesian ROPE, 两个模型族），但核心叙事中 complexity 与 output format 的混淆未解耦；TRAJ 比较本身承认 confounded |
| **Excitement** | 3 / 5 | 回答了重要的实践问题，但主要发现——短输出公式等价、长输出生成退化——与文本生成领域已知规律一致，缺乏深层机制洞察 |
| **Reproducibility** | 4 / 5 | 训练超参、数据处理、种子选择均有详细描述（Appendix D-E），使用公开数据集和模型，但代码未提及开源 |
| **Confidence** | 4 / 5 | 我熟悉 LLM 代码生成/验证领域和相关统计方法，完整阅读了主文和全部附录 |

---

## 主要优势

**S1. 严格控制的实验框架。** 这是本文最大的贡献。在相同模型容量、训练数据、compute 预算下比较三种验证公式，使用 5 seeds + TOST 等价性检验（非仅 significance testing），配合 Bayesian ROPE 和 clustered bootstrap，这种方法论严谨度在经验比较论文中罕见（Section 3.1, 3.4, Appendix G-J）。

**S2. 跨模型族一致性。** 在 Qwen3 和 DeepSeek-Coder 两个模型族上均展示 function-level CLS-CWM 等价性和 repo-level 分歧，增强了结论的 robustness（Table 1, Table 2）。

**S3. 实用的故障模式分类。** Table 4 的 failure mode taxonomy（format collapse, decision collapse, aggregation penalty）为实践者选择验证公式提供了具体的诊断标准，超越了单纯的准确率对比。

**S4. 统计方法的系统运用。** 使用 TOST 证明等价性（而非"未发现显著差异"这种弱结论），Bayesian ROPE 提供互补的 effect size 区间估计，Holm-Bonferroni 校正多重比较，ICC 量化 within-problem 相关——统计分析的严谨程度值得肯定（Section 3.4, Appendix G-K）。

**S5. 充实的附录。** 13 页附录涵盖 oracle advantage、ablation studies、LoRA rank 消融、error complementarity 深度分析、qualitative error analysis、TOST sensitivity analysis、Bayesian ROPE、mixed-effects regression 等，为主文结论提供了充分的 robustness check。

**S6. Related Work 覆盖全面。** 引用了 SWE-RM (Shum et al., 2025)、Patch Reasoner (Xu et al., 2025)、GenRM/GenPRM、CodeRM、Aletheia 等近期高度相关的工作，cross-domain 与 math reasoning 的对比也有涉及。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Complexity-dependent" 核心叙事存在 complexity 与 output format/length 的未解耦混淆
- 具体位置：Introduction contribution list (第一条 "Complexity-moderated formulation choice")、Section 3.5 title ("Repo-Level: Complexity-Dependent Divergence")、Abstract ("complexity-aware routing")
- 问题：论文将 function-level CLS-CWM 等价但 repo-level 分歧归因于 "code complexity"，但这两个 complexity level 同时在多个维度上差异巨大：output length（function-level CWM 输出短 token vs. repo-level CWM 需要生成长执行 trace）、context length、repository structure、test suite 结构。论文自身在 Section 3.5 和 Table 4 中已充分展示 **format collapse** 是 repo-level CWM 退化的主要驱动因素——53-74% 的 CWM 输出 unparseable，formal collapse 占总体误差的绝大部分。这更直接地指向 output format/length 效应，而非 "complexity" 本身。
- 为什么影响接收：这是论文的 **核心叙事框架**。如果退化主要由 output format 驱动而非 complexity，则 "complexity-dependent formulation choice" 的推荐就需要重新表述为 "output-format-dependent"，改变了论文的 takeaway message。
- 建议修改方向：(1) 在 function-level 增加 CWM 长输出变体实验（如要求生成完整执行 trace 而非短输出），以隔离 output length vs. complexity 的效应；或 (2) 至少明确承认这一混淆并将 "complexity-dependent" 修改为更精确的表述，如 "output-complexity-dependent" 或讨论两者的相互关系。

**N2** [critical] ≤8B LoRA 范围限制下的过广泛泛化
- 具体位置：Title ("A Systematic Comparison of Execution-Free Verification Formulations for Code Repair")、Abstract（无 scope 限定词）、Introduction ("the first systematic empirical comparison")
- 问题：所有实验限于 ≤8B 模型 + LoRA fine-tuning，但标题和 abstract 暗示这是对验证公式的 **一般性** 系统比较。14B 的"capacity-dependent convergence"观察仅基于 3 seeds × 1 model family（Qwen3），这对于支撑"容量足够时公式差异消失"的叙事来说证据极为薄弱。Figure 2 仅有 3 个数据点（4B, 8B, 14B）就画出 scaling 结论，在 scaling law 文献中通常需要更多数据点。
- 为什么影响接收：读者可能据此做出关于更大模型或 full fine-tuning 的决策，而这些设置下结论可能完全不同。SWE-RM (Shum et al., 2025) 和 CodeScaler (Zhu et al., 2026) 在更大规模上的经验与本文的 ≤8B 结论之间的关系未讨论。
- 建议修改方向：(1) 标题和 abstract 中明确添加 scope 限定（如 "under ≤8B LoRA fine-tuning"）；(2) 降低 14B convergence 观察的叙事权重，或增加 DeepSeek-Coder 14B 和/或更多 seeds 的数据。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] TRAJ 比较与 CLS-CWM 比较的性质差异未充分区分
- 具体位置：Section 2.1、全文多处
- 问题：CLS 和 CWM 是同一任务（per-test 验证）的不同 formulation，形成 fair comparison。但 TRAJ 将 per-test 信息折叠为 single patch-level verdict，本质上是不同的 task structure。论文在 Abstract 中承认 "the TRAJ comparison is inherently confounded"，但后续仍将三者并列比较。这可能误导读者认为三种公式在同一维度上可比。
- 建议：在主文中更显著地区分两类比较——CLS vs. CWM（well-controlled formulation comparison）和 CLS/CWM vs. TRAJ（task-structure comparison with acknowledged confounds）。

**W2** [warning] Error complementarity 贡献被高估
- 具体位置：Introduction contribution list 第二条、Section 3.6
- 问题：Oracle routing 仅在 single-seed 下报告（function-level 90.63% vs. best single 88.43%），simple routing heuristics 只能捕获 <0.4pp 的 advantage。这本质上是一个 **负面结果**——互补性存在但无法被简单利用。作为 contribution 列出是 overselling。
- 建议：将其重新定位为 observation/negative result，而非 key contribution。或提供更深入的分析（如 per-mutation-type 的互补模式），使其更 actionable。

**W3** [warning] 每个 complexity level 仅使用单一 benchmark
- 具体位置：Section 3.1
- 问题：Function-level 仅用 HumanEval-MBPP variants（1,890 test instances），repo-level 仅用 SWE-bench Verified（1,102 samples）。论文的核心 claim 是 formulation choice depends on complexity，但仅在两个 benchmarks 上验证。MBPP/HumanEval 的 task 特征（短函数、简单测试）可能不代表所有 function-level 代码修复场景。
- 建议：讨论 benchmark 选择对结论泛化性的限制，或在 Limitations 中更突出地提及。若可行，增加至少一个额外的 function-level benchmark（如 APPS 或 CodeContests 子集）。

**W4** [warning] 跨领域对比（code vs. math GenRM）分析浅薄
- 具体位置：Section 4 (Related Work), paragraph 2
- 问题：论文指出 GenRM/GenPRM 在 math reasoning 中显示 generative > discriminative，而本文在 code verification 中发现相反结果，称之为 "domain difference"。但未分析 WHY——是因为 code verification 的 output 结构不同？还是因为 math 的 process supervision 与 code 的 per-test supervision 本质不同？还是 task-specific？这种对比停留在 observation 层面。
- 建议：增加至少一段分析讨论可能的原因（如 code execution output 的 exact-match 要求 vs. math reasoning 的 chain-of-thought 特性），使这一 cross-domain observation 更有价值。

**W5** [warning] 统计方法多样但主次不清
- 具体位置：Section 3.4, Appendix G-M
- 问题：论文使用 TOST、Bayesian ROPE、clustered bootstrap、mixed-effects LPM、GEE、ICC 等多种统计框架。虽然thoroughness 值得肯定，但读者可能困惑：哪个是 primary analysis？当不同方法给出不一致结论时（如 Appendix M 中 LPM vs. GEE 对某些 effects 的不一致），如何判断？
- 建议：在 Section 3 开头明确声明 primary statistical framework（如 TOST + clustered bootstrap），其余作为 robustness checks。

**W6** [warning] Abstract 中 "capacity-dependent convergence" 措辞过强
- 具体位置：Abstract 最后一句 ("a preliminary observation consistent with capacity-dependent convergence")
- 问题：虽然用了 "preliminary observation" 和 "consistent with" 的限定语，但将其放入 abstract 给予了不成比例的prominence。仅 3 seeds × 1 family × 1 scale point 的数据不足以在 abstract 中突出。
- 建议：从 abstract 中移除或进一步弱化此观察，放在主文 Discussion 中更合适。

---

## 小问题（不影响接收）

- **M1**: Section 3.1 提到 "Val loss (function) / test (repo)" 用于 checkpoint 选择，但 Appendix O (Threats to Validity) 讨论了 checkpoint selection 对 CWM convergence 的影响。建议在主文中简要提及 checkpoint selection sensitivity。
- **M2**: Figure 1 的三种 formulation 示意图清晰有用，但 CWM 的 "execution simulation" 示例过于简化——实际 repo-level CWM 的输出远比示例复杂，这可能给读者错误印象。
- **M3**: "pp" 作为 "percentage points" 的缩写首次出现时未定义（Section 1 直接使用），应在首次使用时括号解释。
- **M4**: Section 3.3 中 "At 14B (3 seeds, single family)" — "single family" 应明确为 Qwen3。
- **M5**: Limitations section 提到 "Python-only" 和 "codegen" 限制，但 "codegen" limitation（即训练数据来自合成 mutation 而非真实 bug）对结论泛化性的影响可能比当前讨论更大，建议稍作展开。

---

## Questions to Authors

**Q1**: 你们是否尝试过在 function-level 让 CWM 生成更长的输出（如完整执行 trace 而非短 token），以检验 repo-level 的退化是否主要由 output length 驱动而非 task complexity？

**Q2**: 14B 的 "capacity-dependent convergence" 仅在 Qwen3 上观察到。是否有 DeepSeek-Coder 14B 或 Qwen3 更大模型（如 32B）的任何初步证据？

**Q3**: Error complementarity 在不同 seeds 之间的一致性如何？互补模式是否在 5 个 seeds 中稳定存在，还是主要由个别 seed 驱动？

**Q4**: 不同 formulation 使用不同的 prompt template（Appendix F）。Template design 是否可能解释部分观察到的差异？是否做过 template ablation？

**Q5**: Section 3.7 提到 matched-context ablation 只解释了 CLS-CWM gap 的 <3%。这是否意味着 context difference 不是主要混淆因素？如果是，为什么 TRAJ 的 context 差异就构成了 "inherent confound"？

---

## Missing References

引用覆盖整体良好。以下可能值得考虑补充（非必须）：
- Ma et al. (July 2025). "Rethinking Verification for LLM Code Generation: From Generation to Testing." NeurIPS 2025. — 系统探讨 code generation 验证中 test case 质量的影响，与本文的 per-test verification 相关。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文页数 | ✅ 合规 | 8 页（Section 1-5 + Limitations），不含 references |
| Limitations section | ✅ 存在 | 在第 8 页，覆盖 3 个限制点 |
| Abstract 字数 | ✅ ~185 words | 在 200 words 限制内 |
| 匿名 | ✅ 合规 | "Anonymous ACL submission"，未发现作者信息泄露 |
| 模板 | ✅ ACL style | review 模式 |
| References 页数 | ✅ 不限 | 2 页 (pp. 9-10) |
| 附录 | ✅ 合规 | 13 页 (pp. 11-23)，参与审稿 |
| ARR Checklist | N/A | 在 OpenReview form 中填写，不在 PDF 中 |

---

## 总结

这是一篇方法论严谨的经验比较论文，实验控制和统计分析达到了很高的标准。核心问题（execution-free 验证公式如何选择）对实践者有实际价值。但论文的新颖性主要停留在 empirical comparison 层面（非新方法），核心 "complexity-dependent" 叙事存在 output format 混淆未解耦的问题，且 ≤8B LoRA 的范围限制了结论的泛化性。若能解耦 complexity vs. output format 的混淆并准确限定 scope，论文质量可达到 Conference (4.0) 水平。当前状态下为 **Borderline Conference (3.5)**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1364 · 2026-05-23T15:08:48.580953+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 N/W/Q 条目标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Soundness**: 3.5/5, **Excitement**: 3/5, **Reproducibility**: 4/5\n\n### Must-Fix\n\n**N1** [critical] \"Complexity-dependent\" 核心叙事存在 complexity 与 output format/length 的未解耦混淆\n- 论文将 function-level CLS-CWM 等价但 repo-level 分歧归因于 \"code complexity\"，但两个 complexity level 同时在 output length、context length、repository structure、test suite 结构等多个维度差异。论文自身在 Section 3.5 和 Table 4 已展示 format collapse 是 repo-level CWM 退化的主要驱动因素（53-74% unparseable）。这更直接指向 output format/length 效应，而非 \"complexity\" 本身。如果退化主要由 output format 驱动，则 \"complexity-dependent formulation choice\" 的推荐需重新表述为 \"output-format-dependent\"。\n- 建议：在 function-level 增加 CWM 长输出变体实验以隔离 output length vs. complexity；或至少承认混淆并修改表述。\n\n**N2** [critical] ≤8B LoRA 范围限制下的过广泛泛化\n- 标题 \"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\" 和 abstract 暗示一般性系统比较，但所有实验限于 ≤8B + LoRA。14B 的 \"capacity-dependent convergence\" 仅基于 3 seeds × 1 family（Qwen3），3 个数据点（4B, 8B, 14B）不足以画 scaling 结论。读者可能据此做出关于更大模型或 full fine-tuning 的决策。\n- 建议：标题和 abstract 中添加 scope 限定；降低 14B convergence 的叙事权重。\n\n### Should-Fix\n\n**W1** TRAJ 比较与 CLS-CWM 比较的性质差异未充分区分——CLS/CWM 是同一 task 的不同 formulation，TRAJ 是不同 task structure，不应并列比较。\n\n**W2** Error complementarity 作为 contribution 被高估——oracle routing 仅 single-seed，simple heuristics <0.4pp，本质上是 negative result。\n\n**W3** 每个 complexity level 仅使用单一 benchmark（HumanEval+MBPP / SWE-bench Verified），泛化性受限。\n\n**W4** 跨领域对比（code vs. math GenRM）分析浅薄——仅 observation 层面，未分析 WHY。\n\n**W5** 统计方法多样但主次不清——TOST、Bayesian ROPE、clustered bootstrap、mixed-effects LPM、GEE、ICC 之间的层次关系未明确。\n\n**W6** Abstract 中 \"capacity-dependent convergence\" 措辞过强——仅 3 seeds × 1 family × 1 scale point，不足以在 abstract 中突出。\n\n### Questions\n**Q1**: 是否尝试过在 function-level 让 CWM 生成更长输出以检验退化是否由 output length 驱动？\n**Q2**: 14B convergence 是否有 DeepSeek-Coder 14B 或 32B 的初步证据？\n**Q3**: Error complementarity 在 5 个 seeds 间是否稳定？\n**Q4**: Prompt template design 是否可能解释部分差异？是否做过 template ablation？\n**Q5**: matched-context ablation 只解释 <3% gap，为何 TRAJ 的 context 差异就构成 \"inherent confound\"？\n\n### Missing References\n- Ma et al. (July 2025). \"Rethinking Verification for LLM Code Generation: From Generation to Testing.\" NeurIPS 2025.\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 N/W/Q 条目标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Soundness**: 3.5/5, **Excitement**: 3/5, **Reproducibility**: 4/5\n\n### Must-Fix\n\n**N1** [critical] \"Complexity-dependent\" 核心叙事存在 complexity 与 output format/length 的未解耦混淆\n- 论文将 function-level CLS-CWM 等价但 repo-level 分歧归因于 \"code complexity\"，但两个 complexity level 同时在 output length、context length、repository structure、test suite 结构等多个维度差异。论文自身在 Section 3.5 和 Table 4 已展示 format collapse 是 repo-level CWM 退化的主要驱动因素（53-74% unparseable）。这更直接指向 output format/length 效应，而非 \"complexity\" 本身。如果退化主要由 output format 驱动，则 \"complexity-dependent formulation choice\" 的推荐需重新表述为 \"output-format-dependent\"。\n- 建议：在 function-level 增加 CWM 长输出变体实验以隔离 output length vs. complexity；或至少承认混淆并修改表述。\n\n**N2** [critical] ≤8B LoRA 范围限制下的过广泛泛化\n- 标题 \"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\" 和 abstract 暗示一般性系统比较，但所有实验限于 ≤8B + LoRA。14B 的 \"capacity-dependent convergence\" 仅基于 3 seeds × 1 family（Qwen3），3 个数据点（4B, 8B, 14B）不足以画 scaling 结论。读者可能据此做出关于更大模型或 full fine-tuning 的决策。\n- 建议：标题和 abstract 中添加 scope 限定；降低 14B convergence 的叙事权重。\n\n### Should-Fix\n\n**W1** TRAJ 比较与 CLS-CWM 比较的性质差异未充分区分——CLS/CWM 是同一 task 的不同 formulation，TRAJ 是不同 task structure，不应并列比较。\n\n**W2** Error complementarity 作为 contribution 被高估——oracle routing 仅 single-seed，simple heuristics <0.4pp，本质上是 negative result。\n\n**W3** 每个 complexity level 仅使用单一 benchmark（HumanEval+MBPP / SWE-bench Verified），泛化性受限。\n\n**W4** 跨领域对比（code vs. math GenRM）分析浅薄——仅 observation 层面，未分析 WHY。\n\n**W5** 统计方法多样但主次不清——TOST、Bayesian ROPE、clustered bootstrap、mixed-effects LPM、GEE、ICC 之间的层次关系未明确。\n\n**W6** Abstract 中 \"capacity-dependent convergence\" 措辞过强——仅 3 seeds × 1 family × 1 scale point，不足以在 abstract 中突出。\n\n### Questions\n**Q1**: 是否尝试过在 function-level 让 CWM 生成更长输出以检验退化是否由 output length 驱动？\n**Q2**: 14B convergence 是否有 DeepSeek-Coder 14B 或 32B 的初步证据？\n**Q3**: Error complementarity 在 5 个 seeds 间是否稳定？\n**Q4**: Prompt template design 是否可能解释部分差异？是否做过 template ablation？\n**Q5**: matched-context ablation 只解释 <3% gap，为何 TRAJ 的 context 差异就构成 \"inherent confound\"？\n\n### Missing References\n- Ma et al. (July 2025). \"Rethinking Verification for LLM Code Generation: From Generation to Testing.\" NeurIPS 2025.\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 1365 · 2026-05-23T15:09:18.062292+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29481
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-23T15:09:18.464050+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 N/W/Q 条目标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 4/5, **Excitement**: 3/5\n\n### Must-Fix\n\n**N1** [critical] CLS–TRAJ 等价检验的统计功效不足以支撑任何结论，但论文叙述暗示\"未确认等价\"等同于\"可能不等价\"\n- Section 3.4: TOST power ~0.3 意味着即使 CLS 和 TRAJ 真正等价，也有 70% 概率检测不到。\"未确认等价\" 是空洞陈述。Abstract 和 Conclusion 的 \"TRAJ parity is not confirmed\" 容易让读者误读为 \"TRAJ 可能不等价\"。Bayesian ROPE P(ROPE)=0.542（per-test level）同样 inconclusive。\n- 建议：使用 \"underpowered; no conclusion can be drawn\" 而非 \"not confirmed\"；报告达到 power=0.8 所需样本量；考虑将 CLS–TRAJ 比较降级为 exploratory。\n\n**N2** [critical] Repo-level 2–3 seeds 无法支撑 18–26pp gap 的 formulation 归因\n- Table 3: CLS 2 seeds, DeepSeek CLS 2 seeds。Training seed 才是真正的 replication unit，n=2-3 的 bootstrap CI 可靠性极低。Mixed-effects LPM 用 n=56,480 per-test observations 但 seed 内高度相关（ICC=0.191），有效自由度远低于名义值。CWM 的 53-74% unparseable、NaN validation loss 等均为额外 confound。\n- 建议：报告 seed-level variance effect size；对 repo-level 结论加更强 hedging；讨论需要多少 seeds 达到合理功效。\n\n### Should-Fix\n\n**W1** TOST ±2pp margin 缺乏正式论证——\"deployment relevance\" 但无推导过程，未引用 code generation 领域先例。\n\n**W2** 训练数据量严重不对称未充分控制——CLS ~70K vs TRAJ ~1,386 instances，matched-context ablation 仅控制 input overlap 未控制 training set size。\n\n**W3** DeepSeek-Coder 仅 2 seeds，跨模型比较可信度降低——Table 1 中 DeepSeek CI 未报告。\n\n**W4** CWM format collapse 是 confound 还是 inherent formulation property 界限不清——53-74% unparseable defaulting to majority class。四种 interventions 失败但 intervention 空间有限，constrained decoding 未实验验证。\n\n**W5** 外部效度受限于合成数据和 Python-only——synthetic mutation vs real developer patch 分布差异可能系统性影响结论。\n\n**W6** Mixed-effects LPM vs GEE 不一致——formulation×model interaction LPM p=0.002 但 GEE non-significant，未解释 discrepancy 原因。\n\n### Questions\n**Q1**: 是否做过 downsample CLS 到 ~1,386 instances 与 TRAJ 对比？如果 CLS 在此数据量下也表现类似 TRAJ，formulation 差异结论不成立。\n**Q2**: Constrained decoding 下 CWM format collapse 能否缓解？18-26pp gap 中多少归因于 decoding strategy？\n**Q3**: Oracle scoring 对部分正确 patch 的处理是否低估了 verifier 实际价值？\n**Q4**: 去除 unparseable outputs 后，CLS vs CWM 的 repo-level gap 是否缩小或反转？\n**Q5**: Mixed-effects regression z=−23.7 是否主要由 n=56,480 驱动而非大 effect size？\n\n### Missing References\n- Scholak et al. (2021) PICARD / Poesia et al. (2022) Synchromesh — constrained decoding 相关\n- Dror et al. (2018) \"Hitchhiker's Guide to Testing Statistical Significance in NLP\" — equivalence testing\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 N/W/Q 条目标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 4/5, **Excitement**: 3/5\n\n### Must-Fix\n\n**N1** [critical] CLS–TRAJ 等价检验的统计功效不足以支撑任何结论，但论文叙述暗示\"未确认等价\"等同于\"可能不等价\"\n- Section 3.4: TOST power ~0.3 意味着即使 CLS 和 TRAJ 真正等价，也有 70% 概率检测不到。\"未确认等价\" 是空洞陈述。Abstract 和 Conclusion 的 \"TRAJ parity is not confirmed\" 容易让读者误读为 \"TRAJ 可能不等价\"。Bayesian ROPE P(ROPE)=0.542（per-test level）同样 inconclusive。\n- 建议：使用 \"underpowered; no conclusion can be drawn\" 而非 \"not confirmed\"；报告达到 power=0.8 所需样本量；考虑将 CLS–TRAJ 比较降级为 exploratory。\n\n**N2** [critical] Repo-level 2–3 seeds 无法支撑 18–26pp gap 的 formulation 归因\n- Table 3: CLS 2 seeds, DeepSeek CLS 2 seeds。Training seed 才是真正的 replication unit，n=2-3 的 bootstrap CI 可靠性极低。Mixed-effects LPM 用 n=56,480 per-test observations 但 seed 内高度相关（ICC=0.191），有效自由度远低于名义值。CWM 的 53-74% unparseable、NaN validation loss 等均为额外 confound。\n- 建议：报告 seed-level variance effect size；对 repo-level 结论加更强 hedging；讨论需要多少 seeds 达到合理功效。\n\n### Should-Fix\n\n**W1** TOST ±2pp margin 缺乏正式论证——\"deployment relevance\" 但无推导过程，未引用 code generation 领域先例。\n\n**W2** 训练数据量严重不对称未充分控制——CLS ~70K vs TRAJ ~1,386 instances，matched-context ablation 仅控制 input overlap 未控制 training set size。\n\n**W3** DeepSeek-Coder 仅 2 seeds，跨模型比较可信度降低——Table 1 中 DeepSeek CI 未报告。\n\n**W4** CWM format collapse 是 confound 还是 inherent formulation property 界限不清——53-74% unparseable defaulting to majority class。四种 interventions 失败但 intervention 空间有限，constrained decoding 未实验验证。\n\n**W5** 外部效度受限于合成数据和 Python-only——synthetic mutation vs real developer patch 分布差异可能系统性影响结论。\n\n**W6** Mixed-effects LPM vs GEE 不一致——formulation×model interaction LPM p=0.002 但 GEE non-significant，未解释 discrepancy 原因。\n\n### Questions\n**Q1**: 是否做过 downsample CLS 到 ~1,386 instances 与 TRAJ 对比？如果 CLS 在此数据量下也表现类似 TRAJ，formulation 差异结论不成立。\n**Q2**: Constrained decoding 下 CWM format collapse 能否缓解？18-26pp gap 中多少归因于 decoding strategy？\n**Q3**: Oracle scoring 对部分正确 patch 的处理是否低估了 verifier 实际价值？\n**Q4**: 去除 unparseable outputs 后，CLS vs CWM 的 repo-level gap 是否缩小或反转？\n**Q5**: Mixed-effects regression z=−23.7 是否主要由 n=56,480 驱动而非大 effect size？\n\n### Missing References\n- Scholak et al. (2021) PICARD / Poesia et al. (2022) Synchromesh — constrained decoding 相关\n- Dror et al. (2018) \"Hitchhiker's Guide to Testing Statistical Significance in NLP\" — equivalence testing\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 1367 · 2026-05-23T15:09:19.825090+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 1368 · 2026-05-23T15:09:22.879061+00:00_

交叉分享已发送。等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 121

## Round 121

2 recorded events


### User

_source line 1369 · 2026-05-23T15:09:25.356788+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**评分摘要**：
- **Overall**: 3.5/5 (Borderline Conference)
- **Soundness**: 3.5/5
- **Excitement**: 3/5
- **Confidence**: 4/5

**核心问题**：
1. **N1 [critical]**: "complexity-dependent" 叙事未解耦 complexity 与 output format/length — 论文自身的 failure mode 分析表明 format collapse 是主因，应重新审视归因
2. **N2 [critical]**: ≤8B LoRA 范围下标题和 abstract 的泛化声明过广，14B convergence 证据过薄（3 seeds × 1 family）

**关键 should-fix 问题**：TRAJ 比较与 CLS-CWM 比较性质不同需更清晰区分；error complementarity 是负面结果被高估为贡献；单一 benchmark 限制泛化；cross-domain 对比分析浅。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1370 · 2026-05-23T15:09:30.934349+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 122

## Round 122

2 recorded events


### User

_source line 1371 · 2026-05-23T15:11:03.206777+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: "Complexity-dependent" 叙事存在 complexity 与 output format/length 的未解耦混淆**

同意这是论文的核心方法论弱点。论文自身在 Section 3.6 已明确展示 repo-level CWM 退化的直接机制是 formal collapse（53–74% unparseable, Table 4），而 formal collapse 的直接驱动因素是 output length（"function-level outputs average ~5–15 tokens; repo-level outputs average ~477 tokens, leading to formal collapse"）。这意味着所谓的 "complexity-dependent divergence" 更准确地说是 "output-length-dependent divergence"。

补充我自己的发现：Appendix I（Failed Interventions, page 17）显示四种 intervention（capacity ×2, majority voting K=3, relaxed matching, LoRA rank 32→doubled）均未缓解 formal collapse，但这些 intervention 都没有直接攻击 output length 问题（如 constrained decoding 或 shorter output format）。这进一步支持 R2 的论点——如果论文连针对 output length 的 intervention 都没有尝试，就不能排除 output format 是主要驱动因素。

论文在 Limitations 中提到 "constrained decoding... may mitigate CWM's formal collapse but were not evaluated"——但如果 formal collapse 是 repo-level gap 的主要解释，这就不只是 limitation，而是核心 confound。

**[AGREE] R2-N2: ≤8B LoRA 范围限制下的过广泛泛化**

同意，但程度略轻于 R2 的判断。

论文 abstract 确实包含 "under ≤8B LoRA fine-tuning" 的限定，Section 1 也提到 "two representative code LLM families"，所以 scope 并非完全不透明。但标题 "A Systematic Comparison of Execution-Free Verification Formulations for Code Repair" 确实暗示通用性，而实际覆盖仅 2 families × ≤8B × LoRA。

更具体地，14B scaling 的证据极为薄弱：仅 Qwen3-14B（3 seeds, single family），Figure 2 仅 3 个 scale points（4B, 8B, 14B），Table 2 的 14B 行仅有 CLS 一个 formulation 数据。Abstract 中的 "capacity-dependent convergence (+2.13pp at 8B, +1.16pp at 14B)" 基于这三个点画出减速趋势，从统计角度看 degrees of freedom = 0（3 points fit 3 parameters），任何曲线都能完美拟合。这不足以支撑 abstract 级别的 claim。

建议：(1) 标题增加 "for Small Language Models" 或 "under Parameter-Efficient Fine-Tuning" 限定；(2) 将 14B convergence 从 abstract 降级到正文中的 exploratory observation。

---

### Should-Fix

**[AGREE] R2-W1: TRAJ 与 CLS/CWM 的比较性质差异未充分区分**

同意。这与我自己 review 中的分析一致。CLS 和 CWM 都在 per-test 粒度操作（输入一个 test，输出 PASS/FAIL 或 execution trace），只是 output format 不同。TRAJ 则将所有 per-test 信息坍缩为单一 binary verdict，这是一个根本性的 information bottleneck。将 TRAJ 与 CLS/CWM 并列比较的问题在于：如果 TRAJ 表现差，读者无法区分这是 formulation 差异还是 information loss 导致的。

论文 abstract 承认 "the TRAJ comparison is inherently confounded"，但正文中仍将三者并列呈现（Table 1-3, Figure 2 均包含 TRAJ），读者容易忽略这一 caveat。建议：在 Table 1-3 中用视觉方式（灰色背景或分隔线）区分 CLS-CWM 对比（controlled comparison）和 TRAJ（observational comparison）。

**[AGREE] R2-W2: Error complementarity 的 contribution 被高估**

同意。我在自己的 review 中将这列为"优势"（"虽然 oracle advantage 仅 <0.4pp，但这一 negative result 本身也有价值"），但 R2 的批评更精准——论文将 error complementarity 作为正式 contribution 之一（Section 1: "We make the following contributions... Error complementarity"），而实际 routing gain <0.4pp 本质上说明 formulations 的 error patterns 虽然不同但不够互补到可以实际利用。

不过，Section 3.5 的分析确实提供了有用信息：oracle routing 的上限是 ~0.4pp，说明简单 routing heuristics 不够；同时 error pattern 在 instance-specific 层面确实不同。这更适合框架为 "insight for future work" 而非 "contribution"。

**[REBUT] R2-W3: 单一 benchmark 限制泛化性**

部分不同意。HumanEval+MBPP 和 SWE-bench Verified 分别是 function-level 和 repo-level code repair 领域事实上的标准 benchmark。在这两个 complexity level 上各使用一个 well-established benchmark 是该领域的标准做法（cf. FAIR CodeGen team et al., 2025; Raffel et al., 2020 在 related work 中引用的同类工作也使用相同 benchmark）。

更重要的是，论文已经在 benchmark 内部做了充分的 stratification：function-level 有 5 mutation types（Table 12, Appendix G），repo-level 有 per-test vs. variant-level 分析。增加更多 benchmark（如 ClassEval, CoderEval）当然有价值，但作为 must-fix 或 strong should-fix 理由不充分。

**[AGREE] R2-W4: 跨领域 code vs. math GenRM 比较浅薄**

同意。Section 4（Related Work）中提到 "GenRM (Hosseini et al., 2025) and GenRM-PRM (Zhang et al., 2026) show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference"——但这仅是一句 observation-level 的对比，未分析 WHY code verification 与 math verification 表现不同。

可能的原因包括：(1) math reasoning 的 output structure 更规范（数值答案），而 code execution trace 结构化程度差异大；(2) math task 通常有唯一正确答案，code repair 可能有多种正确输出。但论文未讨论这些。不过，作为 Related Work 中的一句 remark，深度不足是可以理解的——全面分析需要独立的实验，超出本文范围。

**[AGREE] R2-W5: 统计方法层次关系不清**

同意，但我认为论文在附录中的结构实际上暗示了层次：TOST 是 primary analysis（Section 3.4），clustered bootstrap 是 TOST 的 robustness variant（Appendix J），Bayesian ROPE 是 complementary framework（Appendix J.1），ICC 是 correlation structure 的估计（Appendix A），mixed-effects LPM 和 GEE 是 regression-based robustness checks（Appendix M）。

问题在于正文没有明确声明这个层次。我在自己的 review（W6）中也指出 LPM vs GEE 结论不一致但未解释的问题。如果论文在 Section 3.4 开头增加一段 "statistical analysis plan"（声明哪些是 confirmatory，哪些是 exploratory），读者会更容易跟踪。

**[AGREE] R2-W6: Abstract 中 "capacity-dependent convergence" 措辞过强**

完全同意。与 R2-N2 的分析一致。3 seeds × 1 family × 1 additional scale point（14B）不支持 abstract-level 的 capacity-dependent convergence claim。这在正文中作为 exploratory observation 是合适的，但 abstract 空间宝贵，应保留给最有 evidence 支撑的 claims。

---

### Questions

**[AGREE with Q1]**: Function-level CWM 长输出实验是解耦 R2-N1 中 complexity vs output length confound 的关键实验。据我阅读，论文未做此实验。如果在 function-level 人为要求 CWM 生成更长输出（如 chain-of-thought style trace），且性能下降，则证明 output length 是 driver；如果不下降，则 complexity 的归因更可信。

**[AGREE with Q2]**: 14B convergence 目前仅有 Qwen3 的数据。DeepSeek-Coder 14B 或更大模型的数据对 scaling claim 至关重要。

**[AGREE with Q3]**: Error complementarity 的 seed 间稳定性是评估该 contribution 可靠性的关键。论文 Section 3.5 说 "the complementarity is instance-specific" 但未报告跨 seed 的稳定性指标（如 oracle improvement 的 seed-level variance）。

**[REBUT Q4]**: Prompt template 差异的影响需要与 formulation 差异分开看。Appendix F 展示了三种 formulation 的 prompt templates——它们的结构差异是 formulation 定义的一部分，而非独立 confound。CLS 用 classification template 是因为 CLS 就是 classification；CWM 用 simulation template 是因为 CWM 就是 execution simulation。做 template ablation 意味着改变 formulation 本身，而非控制一个独立变量。

不过，within-formulation template variations（如 CLS 的 prompt 用 "Will this test pass or fail?" vs. "Predict the test outcome"）的 ablation 确实有价值，但这是 fine-grained optimization 而非论文的核心关切。

**[AGREE with Q5]**: 这是一个好问题。Matched-context ablation（Appendix B）显示 CLS-CWM 的 input overlap 差异仅解释 <3% of the gap。但论文同时声称 TRAJ 的 context 差异（collapsing per-test into variant-level）是 "inherent confound" 而非可控变量。这里的逻辑不一致：如果 <3% 意味着 context overlap 对 CLS-CWM 影响小，那么为什么不为 TRAJ 也做一个类似的 matched-context ablation（将 CLS per-test predictions 聚合到 variant level）来量化 context 差异的影响？

---

### Missing References

关于 Ma et al. (July 2025) "Rethinking Verification for LLM Code Generation" NeurIPS 2025——如果 camera-ready 日期为 2025 年 7 月，而本文投稿到 ARR May 2026 cycle，那么这篇文献在投稿时已经公开。如果该论文确实系统比较了 code verification formulations，应在 Related Work 中引用和对比。但我无法验证该引用的真实性和具体内容，建议 Director 确认。

---

### 总结

R2 的审稿意见整体质量高，N1（complexity vs output length 混淆）尤其是我自己 review 中未充分强调但完全同意的核心问题。R2-N2（scope 限制）与我的 N2（repo-level seed 不足）从不同角度指向同一个 generalizability 问题。我认为 R2 的 overall 评分 3.5 合理，与我的评分一致。

两位 reviewer 的共识问题：
1. CLS-TRAJ 比较是 underpowered/confounded 的（R1-N1, R2-W1）
2. Repo-level 结论的 evidence base 不足（R1-N2, R2-N2 的 scope 维度）
3. CWM formal collapse 作为 confound vs inherent limitation 的界限不清（R1-W4, R2-N1）
4. Error complementarity 作为 contribution 过度包装（R1 优势中提到但 R2-W2 正确指出）
5. 统计方法论虽然丰富但层次不够清晰（R1-W6, R2-W5）


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1372 · 2026-05-23T15:11:08.433323+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 123

## Round 123

18 recorded events


### User

_source line 1373 · 2026-05-23T15:11:10.999140+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部意见的逐条回应，包含 8 个 [AGREE]、2 个 [REBUT]（W3 单一 benchmark、Q4 template ablation），并附两位 reviewer 的 5 项共识总结。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1374 · 2026-05-23T15:12:20.045129+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool call

_source line 1375 · 2026-05-23T15:12:20.045543+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 1376 · 2026-05-23T15:12:21.400579+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T14:57:04.485660+00:00\", \"completed_at\": \"2026-05-23T15:00:21.178829+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 23\", \"message\": \"Appendix 末页仅顶部约 8 行文字，~90% 页面空白，视觉上不专业。建议将前面 appendix 章节内容重新分布或将此页内容合并到上一页\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-2\", \"message\": \"前 2 页无 display item（纯文本 abstract + introduction），第一个视觉锚点在 page 3。在可接受范围内，但若能将 Figure 1 提前到 page 2 底部效果更佳\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 内部文字（\\\"Input\\\", \\\"Model\\\", \\\"Output Length\\\" 等标签）字号偏小，约为正文字号的 60-65%，接近可读性下限。打印时可能不够清晰\"}, {\"severity\": \"info\", \"dimension\": \"pages 16-17\", \"message\": \"Appendix H（Qualitative Error Analysis）连续 2 页纯文本无 display item，可考虑用示例代码片段或错误分类表格打破单调\"}, {\"severity\": \"info\", \"dimension\": \"pages 20-22\", \"message\": \"Appendix M-O 连续 3 页纯文本（统计分析），对 appendix 可接受但偏密\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool result

_source line 1377 · 2026-05-23T15:12:21.401083+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 1378 · 2026-05-23T15:12:21.602155+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1379 · 2026-05-23T15:12:21.653130+00:00_

1	
2	# === Round 6 Issues (Original) ===
3	
4	# --- Round 6 Must-Fix (Consensus Critical) ---
5	
6	- id: "R6-N1"
7	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
8	  category: experiment
9	  severity: critical
10	  status: resolved
11	  first_raised_round: 6
12	  last_seen_round: 15
13	  mentions:
14	    - round: 6
15	      reviewers: [1, 2]
16	      note: "两人独立提出，最高共识。"
17	    - round: 7
18	      reviewers: [pre-review]
19	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress."
20	    - round: 8
21	      reviewers: [1, 2]
22	      note: "Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp."
23	    - round: 9
24	      reviewers: [1, 2]
25	      note: "Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported."
26	    - round: 10
27	      reviewers: [1, 2]
28	      note: "Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations."
29	    - round: 11
30	      reviewers: [1, 2]
31	      note: "Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion."
32	    - round: 13
33	      reviewers: [1]
34	      note: "Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure."
35	    - round: 14
36	      reviewers: [1, 2]
37	      note: "Fresh review R14. R1-N2 re-raises（2-3 seeds, n=48, 5 confou
…[truncated 8541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1380 · 2026-05-23T15:12:28.089781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "offset": "200",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "offset": "200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-23T15:12:28.140774+00:00_

200	  summary: "CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定"
201	  category: framing
202	  severity: warning
203	  status: resolved
204	  first_raised_round: 6
205	  last_seen_round: 10
206	  resolution: "R10 commit a58c178: Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入限定。"
207	  resolution_round: 10
208	
209	- id: "R6-W3"
210	  summary: "Re-repair δ=0 与 diagnostic granularity 矛盾"
211	  category: framing
212	  severity: warning
213	  status: resolved
214	  first_raised_round: 6
215	  last_seen_round: 7
216	  resolution: "Contributions 4→3, diagnostic granularity 降级为 pending validation."
217	  resolution_round: 7
218	
219	- id: "R6-W4"
220	  summary: "TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同"
221	  category: experiment
222	  severity: warning
223	  status: resolved
224	  first_raised_round: 6
225	  last_seen_round: 15
226	  mentions:
227	    - round: 8
228	      reviewers: [2]
229	      note: "R2-W6: 175× 数据量差异."
230	    - round: 9
231	      reviewers: [1]
232	      note: "R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level."
233	    - round: 10
234	      reviewers: [1, 2]
235	      note: "R1-W1 re-raises：180× 差异 + signal granularity。R2 AGREE。"
236	    - round: 12
237	      reviewers: [1, 2]
238	      note: "Fresh review R12. R1-W4 re-raises：downsample 控制了 volume 但未控制 label granularity。R2 AGREE。"
239	    - round: 13
240	      reviewers: [1, 2]
241	      note: "Fresh review R13. R2-N2 标 CRITICAL：TRAJ 使用 ~400 vs ~70K 实例 + 不同 lr + variant-level labels，三方比较不受控。R1 完全 AGREE，补充：主文 Tables 1-3 无视觉标注 TRAJ 差异。Director 裁定：§3.5 已有 'exploratory' 标注和 confound 讨论，resolved 维持。但报告记录此为 persistent concern。"
242	    - round: 14
243	      reviewers: [1, 2]
244	      note: "Fresh review R14. R1-N3 标 Critical：lr 4×、数据量 175×、标签粒度三重差异使 'matched comparison' 不成立。R2 AGREE with qualification to Should-Fix：论文已有 ★ 标记 + §3.5 'exploratory' + Appendix N，但应在 Abstract/§1 更早限定。Director 采纳降级：Should-Fix。建议 Abstract 限定 'matched for CLS and CWM; TRAJ comparison is exploratory'。"
245	    - roun
…[truncated 9059 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-23T15:12:36.774752+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "offset": "499",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "offset": "499",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-23T15:12:36.775582+00:00_

499	# --- Round 8 Minor ---
500	
501	- id: "R8-M1"
502	  summary: "混合精度 (bfloat16/NF4) 对 TOST 的影响"
503	  category: method
504	  severity: info
505	  status: resolved
506	  first_raised_round: 8
507	  last_seen_round: 10
508	  resolution: "§3.4 footnote 充分讨论。"
509	  resolution_round: 10
510	
511	- id: "R8-M2"
512	  summary: "LPM 未报告 robust SEs; prompt templates 未展示"
513	  category: format
514	  severity: info
515	  status: resolved
516	  first_raised_round: 8
517	  last_seen_round: 15
518	  mentions:
519	    - round: 11
520	      reviewers: [1, 2]
521	      note: "Both RESOLVED. GEE logistic regression added."
522	    - round: 13
523	      reviewers: [1]
524	      note: "Fresh review R13. R1-M3 提及 LPM vs GEE 在 model identity 显著性上不一致（p=0.002 vs p=0.449）。论文已在 Appendix M 讨论 cluster 数限制。Director: resolved——Appendix M 已明确标注 estimator-dependent。"
525	    - round: 15
526	      reviewers: [1]
527	      note: "Fresh review R15. R1-W6 re-raises LPM z=-23.7 可能膨胀。R2 REBUT：Appendix J 已报告完整 logistic regression 结果（OR=0.31, p=0.002, AME=-21.6pp），与 LPM concordant。R1 可能遗漏 Appendix J 第三段。Director：R2 事实核查正确，resolved 维持。建议正文 §3.5 加一句引用 logistic regression 结果。"
528	  resolution: "Appendix M 补充 GEE logistic regression + estimator-dependent 标注。R15 R2 确认 Appendix J 已有完整 OR/CI/p/AME 报告。"
529	  resolution_round: 11
530	
531	# === Round 9 Issues ===
532	
533	- id: "R9-C1"
534	  summary: "'Design space' framing 过度"
535	  category: framing
536	  severity: critical
537	  status: resolved
538	  first_raised_round: 9
539	  last_seen_round: 10
540	  resolution: "标题已改为 Systematic Comparison。"
541	  resolution_round: 10
542	
543	- id: "R9-W1"
544	  summary: "CWM 评估指标非对称性"
545	  category: method
546	  severity: warning
547	  status: resolved
548	  first_raised_round: 9
549	  last_seen_round: 10
550	  resolution: "R2 REBUT 成功：relaxed matching 扩大 gap。"
551	  resolution_round: 10
552	
553	- id: "R9-W2"
554	  summary: "DeepSeek 仅 2 seeds 却声称 'model-dependent'"
555	  category: framing
556	  severity: warning
…[truncated 7358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1384 · 2026-05-23T15:12:43.402934+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "offset": "798",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "offset": "798",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1385 · 2026-05-23T15:12:43.454192+00:00_

798	      reviewers: [2]
799	      note: "R2-W3 re-raises：§2.2 预判实验结果，造成 confirmation bias 印象。R1 REBUT：先验分析是标准 hypothesis-driven research，且实验结果部分推翻了 §2.2 预测（CWM 独特退化非所有 formulation 均匀退化）。Director：R1 rebut 成立——§2.2 标题已为 'Expected Failure Modes'，是方法论步骤而非预判。"
800	  resolution: "标题改为 'Expected Failure Modes'。R15 R1 rebut 成立。"
801	  resolution_round: 12
802	
803	- id: "R12-M2"
804	  summary: "Appendix G' 命名不直观"
805	  category: format
806	  severity: info
807	  status: resolved
808	  first_raised_round: 12
809	  last_seen_round: 12
810	  resolution: "改为 G.1 subsection。"
811	  resolution_round: 12
812	
813	- id: "R12-M3"
814	  summary: "wei2022emergent 引用类型不一致"
815	  category: format
816	  severity: info
817	  status: resolved
818	  first_raised_round: 12
819	  last_seen_round: 12
820	  resolution: "@inproceedings → @article。"
821	  resolution_round: 12
822	
823	- id: "R12-M4"
824	  summary: "Figure 2 float 漂移"
825	  category: format
826	  severity: info
827	  status: resolved
828	  first_raised_round: 12
829	  last_seen_round: 12
830	  resolution: "Figure 2 移入 experiments.tex。"
831	  resolution_round: 12
832	
833	# === Prior Round Issues ===
834	
835	- id: "R5-W1"
836	  summary: "正文超 8 页"
837	  category: format
838	  severity: critical
839	  status: resolved
840	  first_raised_round: 5
841	  resolution: "已压缩至 8 页。"
842	  resolution_round: 6
843	
844	- id: "R5-W2"
845	  summary: "TRAJ checkpoint 不一致"
846	  category: experiment
847	  severity: critical
848	  status: resolved
849	  first_raised_round: 5
850	  resolution: "透明报告。"
851	  resolution_round: 6
852	
853	- id: "R5-W3"
854	  summary: "Table 4 混合指标"
855	  category: format
856	  severity: critical
857	  status: resolved
858	  first_raised_round: 5
859	  resolution: "Table 3 含 Variant Acc 列。"
860	  resolution_round: 6
861	
862	- id: "R4-N1"
863	  summary: "TOST sensitivity analysis"
864	  category: method
865	  severity: critical
866	  status: resolved
867	  first_raised_round: 4
868	  resolution: "通过 R6-W1 修复。"
869	  r
…[truncated 5044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1386 · 2026-05-23T15:16:07.958372+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N2 re-raises. R2 REBUT 指出 R1 混淆两个统计模型。Director：resolved 维持。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W2 re-raises low power (~0.3, n_eff≈86). R2 AGREE 但补充论文已用 TOST+Bayesian ROPE+14B scaling 三重互补验证。Resolved 维持。\"\n    - round: 16\n      reviewers: [1]\n      note: \"Fresh review R16. R1-N2 re-raises：2-3 seeds 无法支撑 18-26pp gap 的 formulation 归因。R2 隐含 AGREE（N2 scope 限制）。论文 §3.5 'exploratory' 标注仍在。\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13-R16 反复提及但无新增要求。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。R2 REBUT。Director 降为 Should-Fix。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N2 升级为 critical。R2 完全 AGREE。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1-W4 re-raises。R2 AGREE。Director resolved 维持。\"\n    - round: 14\n      reviewers: [2]\n      note: \"R2-W1 re-raises s42 vs s123/s456 配置异质性。R1 AGREE。Director resolved 维持。\"\n    - round: 15\n      reviewers: [1]\n      note: \"R1-W7 re-raises CWM checkpoint ablation 范围。R2 REBUT。Director resolved 维持。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy\"\n      assigned_to: \"experiment\"\n      status: wont_fix\n  resolution: \"Step 300-400 checkpoints 未保存，但已找到现有 step-400 eval 数据（s42: 64.36%, 63.7% unparseable）。Format collapse 从训练早期即存在。\"\n  resolution_round: 12\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"两人共识：Findings 合适，Main 不够。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 Excitement 2/5, R1 Excitement 3/5。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 3/5。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Fresh review R16. R1 Excitement 3/5, R2 Excitement 3/5。核心发现可预测性限制新颖性。wont_fix 维持。\"\n  resolution: \"Excitement 稳定在 2.5-3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：无 pre-registration。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W1 标 Must-Fix。R2 AGREE 部分。共识：Table 13 应移入正文。Resolved 维持。\"\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W1 re-raises：缺乏正式论证。但论文已诚实披露 post-hoc 状态并提供 sensitivity analysis。Resolved 维持。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；Bayesian ROPE 提供独立佐证。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入限定。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Fresh review R16. R2-N2 re-raises：标题仍暗示通用性。R1 AGREE 但程度略轻。Abstract 已有限定词但标题无。建议标题加 scope 限定。\"\n  resolution: \"Abstract + Conclusion 均已加入 ≤8B LoRA 限定。标题是否需要修改由 Research Director 决定。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"downsample 控制了 volume 但未控制 label granularity。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Director 裁定 Should-Fix（降级）。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Abstract 已有 'the TRAJ comparison is inherently confounded'。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W1 re-raises TRAJ 与 CLS/CWM 比较性质不同。R1 AGREE：应视觉区分 controlled vs observational comparison。Resolved 维持——Abstract 和 §3.5 均有 confound 标注。\"\n  resolution: \"§3.5 标注 exploratory + confound 讨论。Abstract 已有 'inherently confounded'。\"\n  resolution_round: 12\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W5 re-raises：synthetic mutation vs real developer patch 分布差异。Limitations 已提及但讨论不深。Resolved 维持。\"\n  resolution: \"Appendix Extended Validity Discussion 讨论充分。Limitations 已提及 Python-only 和 codegen 限制。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"~185 词，合规。\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"CodeRM, CodeScaler, GenPRM 等均已加入 Related Work。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  resolution: \"Figure 2 caption 标注 'y-axis does not start at zero'。\"\n  resolution_round: 11\n\n# === Round 8 Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Both RESOLVED.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 re-raises.\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W2 标 Must-Fix。R2 AGREE 但补充 Bayesian ROPE 不受 power 限制。Resolved 维持。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R1-N1 标 Critical：CLS-TRAJ power ~0.3 使该比较 uninformative，Abstract 'not confirmed' 可能 mislead。R2-W1 AGREE。论文 §3.4 已有 power paragraph + 'at current power (~0.3)' 限定。Resolved 维持。\"\n  resolution: \"§3.4 已扩写 power paragraph，14B TOST 完成。Abstract 已加 'at current power (~0.3)' 限定。\"\n  resolution_round: 12\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Cross-seed oracle 已加入正文。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Appendix 已讨论。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM / RepoExec\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Director 裁定 Should-Fix（降级）。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-N2 标 Must-Fix。R1 REBUT matched design 方法论价值。Resolved 维持。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N2 re-raises scope limitation。R1 AGREE 标题应加限定。Resolved 维持——所有 qualifier 已到位。\"\n  resolution: \"Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 13\n  resolution: \"合并至 R6-N4。Inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W6 re-raises LPM vs GEE 不一致（model identity p=0.002 vs p=0.449）。论文 Appendix M 已有 estimator-dependent 标注和 cluster 数限制讨论。Resolved 维持。\"\n  resolution: \"Appendix M 补充 GEE logistic regression + estimator-dependent 标注。\"\n  resolution_round: 11\n\n# === Round 9-12 Issues (all resolved, abbreviated) ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大 gap。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却声称 'model-dependent'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W3 re-raises DeepSeek 仅 2 seeds，跨模型比较可信度降低。Resolved 维持——§3.4 已有 caveat。\"\n  resolution: \"Abstract 改为更审慎措辞。\"\n  resolution_round: 10\n\n- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。\"\n  resolution_round: 12\n\n- id: \"R12-N3\"\n  summary: \"CLS-TRAJ 等价性不对称结论可能是 power ~0.3 artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"§3.4 power paragraph 扩写，14B TOST 完成。\"\n  resolution_round: 12\n\n- id: \"R12-W2\"\n  summary: \"GenRM 对比发现未充分讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 re-raises：跨领域 code vs math GenRM 比较分析浅薄。R1 AGREE 但认为超出本文 scope。Resolved 维持——Conclusion 已有 GenRM 段落。\"\n  resolution: \"Conclusion 新增 GenRM domain-specificity 段落。\"\n  resolution_round: 12\n\n- id: \"R13-N1\"\n  summary: \"Appendix 'P: Limitations' 标题可能违反 EMNLP 格式规则\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Appendix P 重命名为 'Extended validity discussion'。\"\n  resolution_round: 13\n\n- id: \"R13-W1\"\n  summary: \"Abstract/Conclusion 中 TRAJ 'not confirmed' 措辞在 power ~0.3 下 over-stated\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Abstract 加入 'at current power (~0.3)' 限定语。\"\n  resolution_round: 13\n\n- id: \"R13-W2\"\n  summary: \"Oracle 互补性应重新框定为 negative result + motivation，而非独立正面贡献\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W2 re-raises：error complementarity 被高估。R1 AGREE 应降级为 exploratory finding。论文 §1 Contribution 2 已重写为 negative result framing。Resolved 维持。\"\n  resolution: \"Introduction Contribution 2 重写为 negative result framing。\"\n  resolution_round: 13\n\n- id: \"R13-W3\"\n  summary: \"14B 'capacity-dependent convergence' claim 证据不足——仅 1 model family, 3 seeds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W6 re-raises：Abstract 中 capacity-dependent convergence 措辞过强。R1 完全 AGREE。Resolved 维持——Abstract 已有 'preliminary observation' 限定。\"\n  resolution: \"Abstract 和 Conclusion 已有 'preliminary observation' + 'single family' 限定。\"\n  resolution_round: 13\n\n- id: \"R13-W4\"\n  summary: \"GenRM 领域特异性对比分析不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 re-raises。R1 AGREE 但认为超出 scope。Resolved 维持。\"\n  resolution: \"Conclusion 扩展 GenRM 对比。\"\n  resolution_round: 13\n\n# === Round 16 New Issues ===\n\n- id: \"R16-N1\"\n  summary: \"Complexity-dependent 核心叙事存在 complexity 与 output format/length 的未解耦混淆\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 完全 AGREE。论文将 function→repo 分歧归因于 'code complexity'，但 format collapse（53-74% unparseable）更直接指向 output format/length 效应。四种 intervention 均未攻击 output length 本身（如 constrained decoding）。核心 narrative 框架需修正。两位 Reviewer 共识。\"\n  action_items:\n    - round: 16\n      action: \"在正文中明确承认 complexity 与 output format/length 的混淆，将 'complexity-dependent' 修正为更精确表述（如 'output-complexity-dependent'），或在 function-level 增加 CWM 长输出变体实验\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R16-N2\"\n  summary: \"≤8B LoRA 范围限制下标题和 abstract 泛化声明过广\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N2 提出，R1 AGREE。标题 'A Systematic Comparison...' 暗示通用性，但实际仅覆盖 2 families × ≤8B × LoRA。Abstract 已有 '≤8B LoRA fine-tuning' 限定，但标题无。14B convergence 仅 3 seeds × 1 family，Figure 2 仅 3 个 scale points（df=0），不足以支撑 abstract-level scaling claim。两位 Reviewer 建议标题加 scope 限定。\"\n  action_items:\n    - round: 16\n      action: \"标题加 scope 限定（如 'under Parameter-Efficient Fine-Tuning' 或 'for Small Language Models'）；降低 14B convergence 在 abstract 中的 prominence\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R16-W1\"\n  summary: \"统计方法多样但主次层次不清\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 AGREE。TOST/Bayesian ROPE/clustered bootstrap/mixed-effects LPM/GEE/ICC 多种框架但未声明 primary vs robustness check。当不同方法结论不一致时（如 LPM vs GEE 对 model identity），读者无法判断应采信哪个。\"\n  action_items:\n    - round: 16\n      action: \"在 §3 或 §3.1 开头增加 statistical analysis plan，声明 primary framework（TOST + clustered bootstrap）和 robustness checks\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R16-W2\"\n  summary: \"CWM format collapse 的定性归因不清：inherent formulation limitation vs engineering artifact\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W4 提出。53-74% unparseable + default to majority class。四种 interventions 失败但未测试 constrained decoding。如果 format collapse 是 engineering artifact 可通过 constrained decoding 缓解，则 18-26pp gap 不应被解释为 'formulation difference'。与 R16-N1 关联。\"\n  action_items:\n    - round: 16\n      action: \"在 Discussion/Limitations 中明确区分 inherent formulation limitation vs engineering optimization gap；讨论 constrained decoding 的潜在影响\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R16-M1\"\n  summary: \"'pp' 缩写首次使用未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"Section 1 直接使用 'pp' 未括号解释。\"\n  action_items:\n    - round: 16\n      action: \"首次使用时加括号解释：percentage points (pp)\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R16-M2\"\n  summary: \"DeepSeek-Coder 2 seeds 的 CI/std 在 Table 1 中未报告\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"Table 1 中 DeepSeek 行仅有均值，'2 seeds' 注释在 caption 中容易被忽略。\"\n  action_items:\n    - round: 16\n      action: \"在 Table 1 表格内标注 DeepSeek 为 2 seeds\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R16-M3\"\n  summary: \"Figure 1 字体偏小，接近可读性下限\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"Figure 1 内部文字约为正文字号的 60-65%，打印时可能不够清晰。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N2 re-raises. R2 REBUT 指出 R1 混淆两个统计模型。Director：resolved 维持。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W2 re-raises low power (~0.3, n_eff≈86). R2 AGREE 但补充论文已用 TOST+Bayesian ROPE+14B scaling 三重互补验证。Resolved 维持。\"\n    - round: 16\n      reviewers: [1]\n      note: \"Fresh review R16. R1-N2 re-raises：2-3 seeds 无法支撑 18-26pp gap 的 formulation 归因。R2 隐含 AGREE（N2 scope 限制）。论文 §3.5 'exploratory' 标注仍在。\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13-R16 反复提及但无新增要求。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。R2 REBUT。Director 降为 Should-Fix。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N2 升级为 critical。R2 完全 AGREE。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1-W4 re-raises。R2 AGREE。Director resolved 维持。\"\n    - round: 14\n      reviewers: [2]\n      note: \"R2-W1 re-raises s42 vs s123/s456 配置异质性。R1 AGREE。Director resolved 维持。\"\n    - round: 15\n      reviewers: [1]\n      note: \"R1-W7 re-raises CWM checkpoint ablation 范围。R2 REBUT。Director resolved 维持。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy\"\n      assigned_to: \"experiment\"\n      status: wont_fix\n  resolution: \"Step 300-400 checkpoints 未保存，但已找到现有 step-400 eval 数据（s42: 64.36%, 63.7% unparseable）。Format collapse 从训练早期即存在。\"\n  resolution_round: 12\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"两人共识：Findings 合适，Main 不够。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 Excitement 2/5, R1 Excitement 3/5。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 3/5。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Fresh review R16. R1 Excitement 3/5, R2 Excitement 3/5。核心发现可预测性限制新颖性。wont_fix 维持。\"\n  resolution: \"Excitement 稳定在 2.5-3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：无 pre-registration。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W1 标 Must-Fix。R2 AGREE 部分。共识：Table 13 应移入正文。Resolved 维持。\"\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W1 re-raises：缺乏正式论证。但论文已诚实披露 post-hoc 状态并提供 sensitivity analysis。Resolved 维持。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；Bayesian ROPE 提供独立佐证。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入限定。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Fresh review R16. R2-N2 re-raises：标题仍暗示通用性。R1 AGREE 但程度略轻。Abstract 已有限定词但标题无。建议标题加 scope 限定。\"\n  resolution: \"Abstract + Conclusion 均已加入 ≤8B LoRA 限定。标题是否需要修改由 Research Director 决定。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"downsample 控制了 volume 但未控制 label granularity。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Director 裁定 Should-Fix（降级）。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Abstract 已有 'the TRAJ comparison is inherently confounded'。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W1 re-raises TRAJ 与 CLS/CWM 比较性质不同。R1 AGREE：应视觉区分 controlled vs observational comparison。Resolved 维持——Abstract 和 §3.5 均有 confound 标注。\"\n  resolution: \"§3.5 标注 exploratory + confound 讨论。Abstract 已有 'inherently confounded'。\"\n  resolution_round: 12\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W5 re-raises：synthetic mutation vs real developer patch 分布差异。Limitations 已提及但讨论不深。Resolved 维持。\"\n  resolution: \"Appendix Extended Validity Discussion 讨论充分。Limitations 已提及 Python-only 和 codegen 限制。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"~185 词，合规。\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"CodeRM, CodeScaler, GenPRM 等均已加入 Related Work。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  resolution: \"Figure 2 caption 标注 'y-axis does not start at zero'。\"\n  resolution_round: 11\n\n# === Round 8 Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Both RESOLVED.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 re-raises.\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W2 标 Must-Fix。R2 AGREE 但补充 Bayesian ROPE 不受 power 限制。Resolved 维持。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R1-N1 标 Critical：CLS-TRAJ power ~0.3 使该比较 uninformative，Abstract 'not confirmed' 可能 mislead。R2-W1 AGREE。论文 §3.4 已有 power paragraph + 'at current power (~0.3)' 限定。Resolved 维持。\"\n  resolution: \"§3.4 已扩写 power paragraph，14B TOST 完成。Abstract 已加 'at current power (~0.3)' 限定。\"\n  resolution_round: 12\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Cross-seed oracle 已加入正文。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Appendix 已讨论。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM / RepoExec\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Director 裁定 Should-Fix（降级）。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-N2 标 Must-Fix。R1 REBUT matched design 方法论价值。Resolved 维持。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N2 re-raises scope limitation。R1 AGREE 标题应加限定。Resolved 维持——所有 qualifier 已到位。\"\n  resolution: \"Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 13\n  resolution: \"合并至 R6-N4。Inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W6 re-raises LPM vs GEE 不一致（model identity p=0.002 vs p=0.449）。论文 Appendix M 已有 estimator-dependent 标注和 cluster 数限制讨论。Resolved 维持。\"\n  resolution: \"Appendix M 补充 GEE logistic regression + estimator-dependent 标注。\"\n  resolution_round: 11\n\n# === Round 9-12 Issues (all resolved, abbreviated) ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大 gap。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却声称 'model-dependent'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W3 re-raises DeepSeek 仅 2 seeds，跨模型比较可信度降低。Resolved 维持——§3.4 已有 caveat。\"\n  resolution: \"Abstract 改为更审慎措辞。\"\n  resolution_round: 10\n\n- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。\"\n  resolution_round: 12\n\n- id: \"R12-N3\"\n  summary: \"CLS-TRAJ 等价性不对称结论可能是 power ~0.3 artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"§3.4 power paragraph 扩写，14B TOST 完成。\"\n  resolution_round: 12\n\n- id: \"R12-W2\"\n  summary: \"GenRM 对比发现未充分讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 re-raises：跨领域 code vs math GenRM 比较分析浅薄。R1 AGREE 但认为超出本文 scope。Resolved 维持——Conclusion 已有 GenRM 段落。\"\n  resolution: \"Conclusion 新增 GenRM domain-specificity 段落。\"\n  resolution_round: 12\n\n- id: \"R13-N1\"\n  summary: \"Appendix 'P: Limitations' 标题可能违反 EMNLP 格式规则\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Appendix P 重命名为 'Extended validity discussion'。\"\n  resolution_round: 13\n\n- id: \"R13-W1\"\n  summary: \"Abstract/Conclusion 中 TRAJ 'not confirmed' 措辞在 power ~0.3 下 over-stated\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Abstract 加入 'at current power (~0.3)' 限定语。\"\n  resolution_round: 13\n\n- id: \"R13-W2\"\n  summary: \"Oracle 互补性应重新框定为 negative result + motivation，而非独立正面贡献\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W2 re-raises：error complementarity 被高估。R1 AGREE 应降级为 exploratory finding。论文 §1 Contribution 2 已重写为 negative result framing。Resolved 维持。\"\n  resolution: \"Introduction Contribution 2 重写为 negative result framing。\"\n  resolution_round: 13\n\n- id: \"R13-W3\"\n  summary: \"14B 'capacity-dependent convergence' claim 证据不足——仅 1 model family, 3 seeds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W6 re-raises：Abstract 中 capacity-dependent convergence 措辞过强。R1 完全 AGREE。Resolved 维持——Abstract 已有 'preliminary observation' 限定。\"\n  resolution: \"Abstract 和 Conclusion 已有 'preliminary observation' + 'single family' 限定。\"\n  resolution_round: 13\n\n- id: \"R13-W4\"\n  summary: \"GenRM 领域特异性对比分析不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 re-raises。R1 AGREE 但认为超出 scope。Resolved 维持。\"\n  resolution: \"Conclusion 扩展 GenRM 对比。\"\n  resolution_round: 13\n\n# === Round 16 New Issues ===\n\n- id: \"R16-N1\"\n  summary: \"Complexity-dependent 核心叙事存在 complexity 与 output format/length 的未解耦混淆\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 完全 AGREE。论文将 function→repo 分歧归因于 'code complexity'，但 format collapse（53-74% unparseable）更直接指向 output format/length 效应。四种 intervention 均未攻击 output length 本身（如 constrained decoding）。核心 narrative 框架需修正。两位 Reviewer 共识。\"\n  action_items:\n    - round: 16\n      action: \"在正文中明确承认 complexity 与 output format/length 的混淆，将 'complexity-dependent' 修正为更精确表述（如 'output-complexity-dependent'），或在 function-level 增加 CWM 长输出变体实验\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R16-N2\"\n  summary: \"≤8B LoRA 范围限制下标题和 abstract 泛化声明过广\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N2 提出，R1 AGREE。标题 'A Systematic Comparison...' 暗示通用性，但实际仅覆盖 2 families × ≤8B × LoRA。Abstract 已有 '≤8B LoRA fine-tuning' 限定，但标题无。14B convergence 仅 3 seeds × 1 family，Figure 2 仅 3 个 scale points（df=0），不足以支撑 abstract-level scaling claim。两位 Reviewer 建议标题加 scope 限定。\"\n  action_items:\n    - round: 16\n      action: \"标题加 scope 限定（如 'under Parameter-Efficient Fine-Tuning' 或 'for Small Language Models'）；降低 14B convergence 在 abstract 中的 prominence\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R16-W1\"\n  summary: \"统计方法多样但主次层次不清\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 AGREE。TOST/Bayesian ROPE/clustered bootstrap/mixed-effects LPM/GEE/ICC 多种框架但未声明 primary vs robustness check。当不同方法结论不一致时（如 LPM vs GEE 对 model identity），读者无法判断应采信哪个。\"\n  action_items:\n    - round: 16\n      action: \"在 §3 或 §3.1 开头增加 statistical analysis plan，声明 primary framework（TOST + clustered bootstrap）和 robustness checks\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R16-W2\"\n  summary: \"CWM format collapse 的定性归因不清：inherent formulation limitation vs engineering artifact\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W4 提出。53-74% unparseable + default to majority class。四种 interventions 失败但未测试 constrained decoding。如果 format collapse 是 engineering artifact 可通过 constrained decoding 缓解，则 18-26pp gap 不应被解释为 'formulation difference'。与 R16-N1 关联。\"\n  action_items:\n    - round: 16\n      action: \"在 Discussion/Limitations 中明确区分 inherent formulation limitation vs engineering optimization gap；讨论 constrained decoding 的潜在影响\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R16-M1\"\n  summary: \"'pp' 缩写首次使用未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"Section 1 直接使用 'pp' 未括号解释。\"\n  action_items:\n    - round: 16\n      action: \"首次使用时加括号解释：percentage points (pp)\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R16-M2\"\n  summary: \"DeepSeek-Coder 2 seeds 的 CI/std 在 Table 1 中未报告\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"Table 1 中 DeepSeek 行仅有均值，'2 seeds' 注释在 caption 中容易被忽略。\"\n  action_items:\n    - round: 16\n      action: \"在 Table 1 表格内标注 DeepSeek 为 2 seeds\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R16-M3\"\n  summary: \"Figure 1 字体偏小，接近可读性下限\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"Figure 1 内部文字约为正文字号的 60-65%，打印时可能不够清晰。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-23T15:16:08.061149+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 21075}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1388 · 2026-05-23T15:18:25.126812+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "report": "# 审稿报告 — Round 16 (Fresh Review)\n\n**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 Long Paper (ARR May cycle)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人 — R1 方法严谨性+实验设计, R2 新颖性+完整性+写作质量\n**轮次**: 1 轮独立审稿 + 1 轮交叉分享，达成共识\n\n---\n\n## Summary\n\n论文系统比较了三种 execution-free 代码修复验证公式（CLS 分类、CWM 生成、TRAJ 轨迹级），在 Qwen3 和 DeepSeek-Coder 两个模型族、function-level 和 repo-level 两个复杂度层级、5 seeds 下进行实验。核心发现：function-level 三公式近似等价（CLS–CWM TOST p=0.007），repo-level 在 ≤8B LoRA 下 CLS 显著优于 CWM（18–26pp gap，format collapse 驱动）。14B 初步数据显示三公式收敛至 1.07pp 以内。\n\n---\n\n## Strengths\n\n**S1. 统计方法论的深度和一致性（两位 Reviewer 共识最强优势）。** TOST + Holm-Bonferroni + Bayesian ROPE + ICC + clustered bootstrap + mixed-effects LPM 的多层验证框架在 NLP 实证论文中罕见。每种方法的适用性和局限性均有讨论。[§3.1, §3.4, Appendix G-M]\n\n**S2. 跨模型族一致性。** 在 Qwen3 和 DeepSeek-Coder 两个模型族上均展示 function-level CLS-CWM 等价性和 repo-level 分歧，增强了结论的 robustness。[Table 1-3]\n\n**S3. 实用的故障模式分类。** Format collapse / decision collapse / aggregation penalty 的分类（Table 4）为实践者选择验证公式提供了可操作的诊断标准，超越单纯的准确率对比。[§3.5, Table 4]\n\n**S4. 诚实的 negative results 报告。** CLS–TRAJ 功效不足、四种 intervention 全部失败、CWM parseable bias、routing heuristic <0.4pp 等均被坦率报告。[§3.4, §3.5, Appendix I, N]\n\n**S5. 充实的附录（13 页）。** 涵盖 oracle advantage、ablation studies、qualitative error analysis、TOST sensitivity、Bayesian ROPE、mixed-effects regression 等，为主文结论提供了充分的 robustness check。\n\n**S6. Related Work 覆盖全面。** 引用了 SWE-RM、Patch Reasoner、GenRM/GenPRM、CodeRM、Aletheia、CodeScaler 等近期高度相关工作，cross-domain 与 math reasoning 的对比也有涉及。[§4]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical, consensus] Complexity-dependent 核心叙事存在 complexity 与 output format/length 的未解耦混淆。**\n论文将 function→repo 分歧归因为 \"code complexity\"，但论文自身的分析已表明 format collapse（53–74% unparseable, Table 4）是 repo-level CWM 退化的直接机制。Function-level CWM 输出平均 ~5–15 tokens；repo-level 平均 ~477 tokens。这更直接指向 output format/length 效应。四种 intervention（capacity ×2、majority voting、relaxed matching、LoRA rank 32）均未攻击 output length 本身（如 constrained decoding）。如果退化主要由 output format 驱动，则 \"complexity-dependent formulation choice\" 的推荐需重新表述。**两位 Reviewer 共识。** [§3.5, §3.6, Table 4, Appendix I, Limitations]\n\n**N2 [critical, consensus] ≤8B LoRA 范围限制下标题和 abstract 的泛化声明过广。**\n标题 \"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\" 暗示通用性，但所有实验限于 ≤8B + LoRA。Abstract 虽有 \"≤8B LoRA fine-tuning\" 限定，但标题无。14B \"capacity-dependent convergence\" 仅基于 3 seeds × 1 family（Qwen3），Figure 2 仅 3 个 scale points（4B, 8B, 14B），degrees of freedom = 0。Abstract 中给予此观察不成比例的 prominence。**两位 Reviewer 共识。** [Title, Abstract, §3.3, Figure 2]\n\n**N3 [critical, consensus] CLS–TRAJ 等价检验 power ~0.3 导致该比较 uninformative，但论文措辞暗示 \"可能不等价\"。**\nTOST power ~0.3 意味着即使 CLS 和 TRAJ 真正等价，也有 70% 概率检测不到。Abstract \"TRAJ parity is not confirmed after multiple comparison correction at current power (~0.3)\" 虽有功效限定语，但放在 abstract 中仍容易让读者误解为存在差异的证据。Bayesian ROPE P(ROPE)=0.542（per-test level）同样 inconclusive。CLS–TRAJ 比较是论文三组比较之一，若该比较 uninformative，核心贡献缩水。**两位 Reviewer 共识。** [Abstract, §3.4, Appendix G.1]\n\n**N4 [critical, R1 primary, R2 implicit agree] Repo-level 2–3 seeds 无法可靠支撑 18–26pp gap 的 formulation 归因。**\nTraining seed 是真正的 replication unit，n=2-3 的 bootstrap CI 可靠性极低。Mixed-effects LPM 用 n=56,480 per-test observations 但 seed 内高度相关（ICC=0.191），有效自由度远低于名义值。论文 §3.5 已有 \"exploratory due to limited seed coverage\" 标注，但 Table 3 和 abstract 的呈现方式仍偏向于 definitive 结论。[§3.5, Table 3, Appendix M, O]\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, consensus] 统计方法多样但主次层次不清。** TOST/Bayesian ROPE/clustered bootstrap/mixed-effects LPM/GEE/ICC 多种框架但未声明 primary vs robustness check。LPM vs GEE 对 model identity 给出不一致结论（p=0.002 vs p=0.449），读者无法判断应采信哪个。[§3.4, Appendix M]\n\n**W2 [warning, consensus] TRAJ 比较与 CLS-CWM 比较性质差异未充分区分。** CLS/CWM 是同一 task 的不同 formulation（per-test），TRAJ 是不同 task structure（variant-level）。Abstract 承认 \"inherently confounded\" 但正文 Table 1-3 仍并列呈现。[§2.1, Table 1-3]\n\n**W3 [warning, consensus] Error complementarity 作为 contribution 被高估。** Oracle routing 仅 single-seed（90.63%），simple heuristics <0.4pp。本质上是 negative result——互补性存在但无法被简单利用。论文 §1 Contribution 2 已重写为 negative result framing，但措辞仍偏正面。[§3.6, §1]\n\n**W4 [warning, R1] CWM format collapse 的定性归因不清：inherent formulation limitation vs engineering artifact。** 53–74% unparseable defaulting to majority class。四种 interventions 失败但 intervention 空间有限——constrained decoding 未实验验证。如果 format collapse 可通过 engineering 缓解，18–26pp gap 中有多少归因于 decoding strategy 而非 formulation？[§3.5, §3.6, Limitations]\n\n**W5 [warning, R1] TOST ±2pp margin 缺乏正式论证。** \"Deployment relevance\" 但无推导过程、无 code verification 领域先例引用。虽未 pre-registered 但已诚实披露。Sensitivity analysis 显示 minimum margin ±1.52pp 仅低 0.48pp。[§3.4, Appendix G]\n\n**W6 [warning, R1] 训练数据量严重不对称未充分控制。** CLS/CWM ~70K instances vs TRAJ ~1,386 variant-level instances。Downsample ablation（Appendix O）控制了 volume 但未控制 label granularity（per-test vs variant-level），后者是 formulation-inherent confound。[§3.1, Appendix O]\n\n**W7 [warning, R2] 跨领域 code vs math GenRM 对比分析浅薄。** 仅 observation-level 对比，未分析 WHY 代码验证中 generative 不如 discriminative（与 math reasoning 相反）。[§4, §5]\n\n**W8 [warning, R1] 外部效度受限于合成数据和 Python-only。** Synthetic mutation operators vs real developer patches 的分布差异可能系统性影响 formulation 比较结论。Limitations 已提及但讨论不深。[Limitations, Appendix P]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Complexity vs output format 混淆**（R2-N1, R1 AGREE）：核心叙事框架需修正\n2. **≤8B scope 泛化过广**（R2-N2, R1 AGREE）：标题应加限定\n3. **CLS–TRAJ 比较 uninformative**（R1-N1, R2-W1 AGREE）：power ~0.3 使该比较无信息量\n4. **Repo-level seed 不足**（R1-N2, R2 implicit AGREE）：2–3 seeds 无法可靠归因\n5. **Error complementarity 高估**（R2-W2, R1 AGREE）：<0.4pp gain 是 negative result\n6. **统计方法主次不清**（R2-W5, R1 AGREE）：应声明 primary framework\n7. **Abstract 14B convergence 过强**（R2-W6, R1 AGREE）：仅 3 seeds × 1 family\n\n## Reviewer Divergence [REBUT]\n\n1. **单一 benchmark 限制泛化**（R2-W3, R1 REBUT）：R1 认为 HumanEval+MBPP 和 SWE-bench Verified 是领域标准 benchmark，且已有 per-mutation-type stratification，单一 benchmark 不构成 strong weakness。\n2. **Template ablation**（R2-Q4, R1 REBUT）：R1 认为 prompt template 是 formulation 定义的一部分而非独立 confound——CLS 用 classification template 是因为 CLS 就是 classification。\n\n---\n\n## Questions\n\n**Q1** [R2, R1 AGREE]: 是否尝试过在 function-level 让 CWM 生成更长输出（如完整执行 trace），以检验 repo-level 退化是否主要由 output length 驱动而非 task complexity？\n\n**Q2** [R1]: 是否做过 downsample CLS 到 ~1,386 instances 与 TRAJ 对比？如果 CLS 在此数据量下也表现类似 TRAJ，formulation 差异结论不成立。（注：论文已在 Appendix O 报告 CLS downsample 到 ~8K 的结果为 80.74%，仍高于 TRAJ 72.92%，但未进一步下采样至 ~1,386。）\n\n**Q3** [R2, R1 AGREE]: 14B capacity-dependent convergence 是否有 DeepSeek-Coder 14B 或 32B 的任何初步证据？\n\n**Q4** [R1]: 去除 unparseable outputs 后（即只看 parseable subset），CLS vs CWM 的 repo-level gap 是否缩小或反转？（注：论文报告 parseable-only accuracy 38–43%，低于 majority baseline，说明 parseable subset 中 CWM 更差。）\n\n**Q5** [R2, R1 AGREE]: Error complementarity 在不同 seeds 之间的一致性如何？互补模式是否在 5 个 seeds 中稳定存在？\n\n**Q6** [R1]: Mixed-effects regression z=−23.7 是否主要由 n=56,480 驱动而非大 effect size？（注：Appendix M 已报告 logistic regression OR=0.31, AME=−21.6pp，与 LPM concordant。）\n\n**Q7** [R2]: Matched-context ablation 只解释 CLS-CWM gap 的 <3%。如果 context overlap 对 CLS-CWM 影响小，为什么 TRAJ 的 context 差异（collapsing per-test into variant-level）就构成 \"inherent confound\"？\n\n---\n\n## Missing References\n\n- **Constrained decoding**: Scholak et al. (2021) PICARD; Poesia et al. (2022) Synchromesh — 与 CWM format collapse 缓解直接相关（R1 提出）\n- **Equivalence testing in NLP**: Dror et al. (2018) \"The Hitchhiker's Guide to Testing Statistical Significance in NLP\" — equivalence testing 应用讨论（R1 提出）\n- **Ma et al. (July 2025)**: \"Rethinking Verification for LLM Code Generation: From Generation to Testing\" NeurIPS 2025 — 系统探讨 code generation 验证（R2 提出，需确认引用真实性）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| warning | page 23 | Appendix 末页仅顶部约 8 行文字，~90% 页面空白 |\n| info | pages 1-2 | 前 2 页无 display item，第一个视觉锚点在 page 3 |\n| info | page 3 | Figure 1 内部文字字号偏小（约正文 60-65%），接近可读性下限 |\n| info | pages 16-17 | Appendix H 连续 2 页纯文本，可考虑用代码片段或表格打破 |\n| info | pages 20-22 | Appendix M-O 连续 3 页纯文本统计分析 |\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 — Borderline Conference**\n\n**置信度: 4/5**（两位 Reviewer 均熟悉统计检验方法论、代码修复评估和 LLM fine-tuning 实验设计）\n\n**理由**: 论文的统计方法论是其最大亮点——TOST 等价检验 + 多层 robustness check 的框架在 NLP 实证论文中罕见，failure mode taxonomy 有独立实用价值。但核心贡献受限于三个方面：\n\n1. **新颖性不足**: 核心发现（短输出公式等价、长输出生成退化）在直觉上可预测，缺乏 surprising insight（R1/R2 Excitement 均为 3/5）。\n2. **核心叙事框架问题**: \"Complexity-dependent\" 的归因可能更准确地是 \"output-format-dependent\"，这不是措辞问题而是对结论 takeaway 的根本性影响。\n3. **泛化范围有限**: ≤8B LoRA × 2 families × synthetic data × Python-only 的范围限制了结论的实用覆盖面。\n\n**EMNLP 2026 定位**: 按 ARR 评分标准，3.5 = Borderline Conference。论文质量足够达到 Findings 水平（3.0），但 main conference 需要更强的 novelty 或更明确的 scope 限定 + 解耦 complexity vs output format 的核心混淆。若能修复 N1（核心叙事框架）和 N2（scope 限定），评分有望提升至 3.5–4.0 区间。\n\n---\n\n## Detailed Comments\n\n**格式合规**: 正文 8 页合规；Limitations section 存在且覆盖 3 点；Abstract ~185 words（<200）；匿名合规（\"Anonymous ACL submission\"）；ACL review 模板正确。\n\n**Appendix**: 13 页附录内容充实但部分 appendix（H, M-O）连续纯文本偏密。末页（p.23）~90% 空白，建议内容重分布。\n\n**小问题**: \"pp\" 缩写首次使用未定义（§1）；Table 1 DeepSeek \"2 seeds\" 注释在 caption 中容易被忽略；§3.4 \"523 variant-level instances across five seeds\" 应明确为 Qwen3-only 分析。",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "report": "# 审稿报告 — Round 16 (Fresh Review)\n\n**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 Long Paper (ARR May cycle)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人 — R1 方法严谨性+实验设计, R2 新颖性+完整性+写作质量\n**轮次**: 1 轮独立审稿 + 1 轮交叉分享，达成共识\n\n---\n\n## Summary\n\n论文系统比较了三种 execution-free 代码修复验证公式（CLS 分类、CWM 生成、TRAJ 轨迹级），在 Qwen3 和 DeepSeek-Coder 两个模型族、function-level 和 repo-level 两个复杂度层级、5 seeds 下进行实验。核心发现：function-level 三公式近似等价（CLS–CWM TOST p=0.007），repo-level 在 ≤8B LoRA 下 CLS 显著优于 CWM（18–26pp gap，format collapse 驱动）。14B 初步数据显示三公式收敛至 1.07pp 以内。\n\n---\n\n## Strengths\n\n**S1. 统计方法论的深度和一致性（两位 Reviewer 共识最强优势）。** TOST + Holm-Bonferroni + Bayesian ROPE + ICC + clustered bootstrap + mixed-effects LPM 的多层验证框架在 NLP 实证论文中罕见。每种方法的适用性和局限性均有讨论。[§3.1, §3.4, Appendix G-M]\n\n**S2. 跨模型族一致性。** 在 Qwen3 和 DeepSeek-Coder 两个模型族上均展示 function-level CLS-CWM 等价性和 repo-level 分歧，增强了结论的 robustness。[Table 1-3]\n\n**S3. 实用的故障模式分类。** Format collapse / decision collapse / aggregation penalty 的分类（Table 4）为实践者选择验证公式提供了可操作的诊断标准，超越单纯的准确率对比。[§3.5, Table 4]\n\n**S4. 诚实的 negative results 报告。** CLS–TRAJ 功效不足、四种 intervention 全部失败、CWM parseable bias、routing heuristic <0.4pp 等均被坦率报告。[§3.4, §3.5, Appendix I, N]\n\n**S5. 充实的附录（13 页）。** 涵盖 oracle advantage、ablation studies、qualitative error analysis、TOST sensitivity、Bayesian ROPE、mixed-effects regression 等，为主文结论提供了充分的 robustness check。\n\n**S6. Related Work 覆盖全面。** 引用了 SWE-RM、Patch Reasoner、GenRM/GenPRM、CodeRM、Aletheia、CodeScaler 等近期高度相关工作，cross-domain 与 math reasoning 的对比也有涉及。[§4]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical, consensus] Complexity-dependent 核心叙事存在 complexity 与 output format/length 的未解耦混淆。**\n论文将 function→repo 分歧归因为 \"code complexity\"，但论文自身的分析已表明 format collapse（53–74% unparseable, Table 4）是 repo-level CWM 退化的直接机制。Function-level CWM 输出平均 ~5–15 tokens；repo-level 平均 ~477 tokens。这更直接指向 output format/length 效应。四种 intervention（capacity ×2、majority voting、relaxed matching、LoRA rank 32）均未攻击 output length 本身（如 constrained decoding）。如果退化主要由 output format 驱动，则 \"complexity-dependent formulation choice\" 的推荐需重新表述。**两位 Reviewer 共识。** [§3.5, §3.6, Table 4, Appendix I, Limitations]\n\n**N2 [critical, consensus] ≤8B LoRA 范围限制下标题和 abstract 的泛化声明过广。**\n标题 \"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\" 暗示通用性，但所有实验限于 ≤8B + LoRA。Abstract 虽有 \"≤8B LoRA fine-tuning\" 限定，但标题无。14B \"capacity-dependent convergence\" 仅基于 3 seeds × 1 family（Qwen3），Figure 2 仅 3 个 scale points（4B, 8B, 14B），degrees of freedom = 0。Abstract 中给予此观察不成比例的 prominence。**两位 Reviewer 共识。** [Title, Abstract, §3.3, Figure 2]\n\n**N3 [critical, consensus] CLS–TRAJ 等价检验 power ~0.3 导致该比较 uninformative，但论文措辞暗示 \"可能不等价\"。**\nTOST power ~0.3 意味着即使 CLS 和 TRAJ 真正等价，也有 70% 概率检测不到。Abstract \"TRAJ parity is not confirmed after multiple comparison correction at current power (~0.3)\" 虽有功效限定语，但放在 abstract 中仍容易让读者误解为存在差异的证据。Bayesian ROPE P(ROPE)=0.542（per-test level）同样 inconclusive。CLS–TRAJ 比较是论文三组比较之一，若该比较 uninformative，核心贡献缩水。**两位 Reviewer 共识。** [Abstract, §3.4, Appendix G.1]\n\n**N4 [critical, R1 primary, R2 implicit agree] Repo-level 2–3 seeds 无法可靠支撑 18–26pp gap 的 formulation 归因。**\nTraining seed 是真正的 replication unit，n=2-3 的 bootstrap CI 可靠性极低。Mixed-effects LPM 用 n=56,480 per-test observations 但 seed 内高度相关（ICC=0.191），有效自由度远低于名义值。论文 §3.5 已有 \"exploratory due to limited seed coverage\" 标注，但 Table 3 和 abstract 的呈现方式仍偏向于 definitive 结论。[§3.5, Table 3, Appendix M, O]\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, consensus] 统计方法多样但主次层次不清。** TOST/Bayesian ROPE/clustered bootstrap/mixed-effects LPM/GEE/ICC 多种框架但未声明 primary vs robustness check。LPM vs GEE 对 model identity 给出不一致结论（p=0.002 vs p=0.449），读者无法判断应采信哪个。[§3.4, Appendix M]\n\n**W2 [warning, consensus] TRAJ 比较与 CLS-CWM 比较性质差异未充分区分。** CLS/CWM 是同一 task 的不同 formulation（per-test），TRAJ 是不同 task structure（variant-level）。Abstract 承认 \"inherently confounded\" 但正文 Table 1-3 仍并列呈现。[§2.1, Table 1-3]\n\n**W3 [warning, consensus] Error complementarity 作为 contribution 被高估。** Oracle routing 仅 single-seed（90.63%），simple heuristics <0.4pp。本质上是 negative result——互补性存在但无法被简单利用。论文 §1 Contribution 2 已重写为 negative result framing，但措辞仍偏正面。[§3.6, §1]\n\n**W4 [warning, R1] CWM format collapse 的定性归因不清：inherent formulation limitation vs engineering artifact。** 53–74% unparseable defaulting to majority class。四种 interventions 失败但 intervention 空间有限——constrained decoding 未实验验证。如果 format collapse 可通过 engineering 缓解，18–26pp gap 中有多少归因于 decoding strategy 而非 formulation？[§3.5, §3.6, Limitations]\n\n**W5 [warning, R1] TOST ±2pp margin 缺乏正式论证。** \"Deployment relevance\" 但无推导过程、无 code verification 领域先例引用。虽未 pre-registered 但已诚实披露。Sensitivity analysis 显示 minimum margin ±1.52pp 仅低 0.48pp。[§3.4, Appendix G]\n\n**W6 [warning, R1] 训练数据量严重不对称未充分控制。** CLS/CWM ~70K instances vs TRAJ ~1,386 variant-level instances。Downsample ablation（Appendix O）控制了 volume 但未控制 label granularity（per-test vs variant-level），后者是 formulation-inherent confound。[§3.1, Appendix O]\n\n**W7 [warning, R2] 跨领域 code vs math GenRM 对比分析浅薄。** 仅 observation-level 对比，未分析 WHY 代码验证中 generative 不如 discriminative（与 math reasoning 相反）。[§4, §5]\n\n**W8 [warning, R1] 外部效度受限于合成数据和 Python-only。** Synthetic mutation operators vs real developer patches 的分布差异可能系统性影响 formulation 比较结论。Limitations 已提及但讨论不深。[Limitations, Appendix P]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Complexity vs output format 混淆**（R2-N1, R1 AGREE）：核心叙事框架需修正\n2. **≤8B scope 泛化过广**（R2-N2, R1 AGREE）：标题应加限定\n3. **CLS–TRAJ 比较 uninformative**（R1-N1, R2-W1 AGREE）：power ~0.3 使该比较无信息量\n4. **Repo-level seed 不足**（R1-N2, R2 implicit AGREE）：2–3 seeds 无法可靠归因\n5. **Error complementarity 高估**（R2-W2, R1 AGREE）：<0.4pp gain 是 negative result\n6. **统计方法主次不清**（R2-W5, R1 AGREE）：应声明 primary framework\n7. **Abstract 14B convergence 过强**（R2-W6, R1 AGREE）：仅 3 seeds × 1 family\n\n## Reviewer Divergence [REBUT]\n\n1. **单一 benchmark 限制泛化**（R2-W3, R1 REBUT）：R1 认为 HumanEval+MBPP 和 SWE-bench Verified 是领域标准 benchmark，且已有 per-mutation-type stratification，单一 benchmark 不构成 strong weakness。\n2. **Template ablation**（R2-Q4, R1 REBUT）：R1 认为 prompt template 是 formulation 定义的一部分而非独立 confound——CLS 用 classification template 是因为 CLS 就是 classification。\n\n---\n\n## Questions\n\n**Q1** [R2, R1 AGREE]: 是否尝试过在 function-level 让 CWM 生成更长输出（如完整执行 trace），以检验 repo-level 退化是否主要由 output length 驱动而非 task complexity？\n\n**Q2** [R1]: 是否做过 downsample CLS 到 ~1,386 instances 与 TRAJ 对比？如果 CLS 在此数据量下也表现类似 TRAJ，formulation 差异结论不成立。（注：论文已在 Appendix O 报告 CLS downsample 到 ~8K 的结果为 80.74%，仍高于 TRAJ 72.92%，但未进一步下采样至 ~1,386。）\n\n**Q3** [R2, R1 AGREE]: 14B capacity-dependent convergence 是否有 DeepSeek-Coder 14B 或 32B 的任何初步证据？\n\n**Q4** [R1]: 去除 unparseable outputs 后（即只看 parseable subset），CLS vs CWM 的 repo-level gap 是否缩小或反转？（注：论文报告 parseable-only accuracy 38–43%，低于 majority baseline，说明 parseable subset 中 CWM 更差。）\n\n**Q5** [R2, R1 AGREE]: Error complementarity 在不同 seeds 之间的一致性如何？互补模式是否在 5 个 seeds 中稳定存在？\n\n**Q6** [R1]: Mixed-effects regression z=−23.7 是否主要由 n=56,480 驱动而非大 effect size？（注：Appendix M 已报告 logistic regression OR=0.31, AME=−21.6pp，与 LPM concordant。）\n\n**Q7** [R2]: Matched-context ablation 只解释 CLS-CWM gap 的 <3%。如果 context overlap 对 CLS-CWM 影响小，为什么 TRAJ 的 context 差异（collapsing per-test into variant-level）就构成 \"inherent confound\"？\n\n---\n\n## Missing References\n\n- **Constrained decoding**: Scholak et al. (2021) PICARD; Poesia et al. (2022) Synchromesh — 与 CWM format collapse 缓解直接相关（R1 提出）\n- **Equivalence testing in NLP**: Dror et al. (2018) \"The Hitchhiker's Guide to Testing Statistical Significance in NLP\" — equivalence testing 应用讨论（R1 提出）\n- **Ma et al. (July 2025)**: \"Rethinking Verification for LLM Code Generation: From Generation to Testing\" NeurIPS 2025 — 系统探讨 code generation 验证（R2 提出，需确认引用真实性）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| warning | page 23 | Appendix 末页仅顶部约 8 行文字，~90% 页面空白 |\n| info | pages 1-2 | 前 2 页无 display item，第一个视觉锚点在 page 3 |\n| info | page 3 | Figure 1 内部文字字号偏小（约正文 60-65%），接近可读性下限 |\n| info | pages 16-17 | Appendix H 连续 2 页纯文本，可考虑用代码片段或表格打破 |\n| info | pages 20-22 | Appendix M-O 连续 3 页纯文本统计分析 |\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 — Borderline Conference**\n\n**置信度: 4/5**（两位 Reviewer 均熟悉统计检验方法论、代码修复评估和 LLM fine-tuning 实验设计）\n\n**理由**: 论文的统计方法论是其最大亮点——TOST 等价检验 + 多层 robustness check 的框架在 NLP 实证论文中罕见，failure mode taxonomy 有独立实用价值。但核心贡献受限于三个方面：\n\n1. **新颖性不足**: 核心发现（短输出公式等价、长输出生成退化）在直觉上可预测，缺乏 surprising insight（R1/R2 Excitement 均为 3/5）。\n2. **核心叙事框架问题**: \"Complexity-dependent\" 的归因可能更准确地是 \"output-format-dependent\"，这不是措辞问题而是对结论 takeaway 的根本性影响。\n3. **泛化范围有限**: ≤8B LoRA × 2 families × synthetic data × Python-only 的范围限制了结论的实用覆盖面。\n\n**EMNLP 2026 定位**: 按 ARR 评分标准，3.5 = Borderline Conference。论文质量足够达到 Findings 水平（3.0），但 main conference 需要更强的 novelty 或更明确的 scope 限定 + 解耦 complexity vs output format 的核心混淆。若能修复 N1（核心叙事框架）和 N2（scope 限定），评分有望提升至 3.5–4.0 区间。\n\n---\n\n## Detailed Comments\n\n**格式合规**: 正文 8 页合规；Limitations section 存在且覆盖 3 点；Abstract ~185 words（<200）；匿名合规（\"Anonymous ACL submission\"）；ACL review 模板正确。\n\n**Appendix**: 13 页附录内容充实但部分 appendix（H, M-O）连续纯文本偏密。末页（p.23）~90% 空白，建议内容重分布。\n\n**小问题**: \"pp\" 缩写首次使用未定义（§1）；Table 1 DeepSeek \"2 seeds\" 注释在 caption 中容易被忽略；§3.4 \"523 variant-level instances across five seeds\" 应明确为 Qwen3-only 分析。",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 1389 · 2026-05-23T15:18:29.038011+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3911
}
```

</details>

---


### Assistant

_source line 1390 · 2026-05-23T15:18:39.328427+00:00_

审稿报告已投递。

**Round 16 审稿完成。** 评分 **3.5 / 5 (Borderline Conference)**。

**核心发现**：
- 4 个 Must-Fix（N1 complexity/output-format 混淆、N2 scope 泛化过广、N3 CLS-TRAJ underpowered、N4 repo-level seed 不足）
- 8 个 Should-Fix（统计方法层次、TRAJ 比较性质、error complementarity 高估、CWM format collapse 归因、TOST margin、数据量不对称、GenRM 对比浅、外部效度）
- 7 个 Reviewer 共识、2 个分歧（已记录）
- Issue Tracker 已更新：4 个新 open issue + 3 个新 minor + 历史 issue 追踪到 R16

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 124

## Round 124

2 recorded events


### User

_source line 1391 · 2026-05-23T15:18:39.334578+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: CLS–TRAJ 等价检验的统计功效不足**

同意。TOST power ~0.3 确实意味着该检验对真正的等价性缺乏辨别力。论文在 Abstract 和 Section 3.4 使用 "TRAJ parity is not confirmed" 的措辞虽然字面上正确，但在上下文中读者自然会倾向于理解为 "TRAJ 可能不等价"——特别是紧接着就报告了 CLS-CWM 的 TOST 显著等价结果（p=0.007），形成了隐含对比。

补充发现：Bayesian ROPE 在 per-test level 给出 P(ROPE)=0.542（Appendix G.1），本身是完全 inconclusive 的——接近随机猜测的 0.5。论文在 Appendix G.1 中虽然承认 "inconclusive"，但主文并未充分传达这一点。Abstract 中将这一 underpowered 结论与 CLS-CWM 的强等价结论并列放置，客观上放大了 TRAJ 的"异常"印象。

R1 建议的"报告达到 power=0.8 所需样本量"是建设性的。将 CLS–TRAJ 比较降级为 exploratory 也合理。

---

**[AGREE with nuance] R1-N2: Repo-level 2–3 seeds 的 formulation 归因可靠性**

同意核心关切：n=2-3 seeds 确实不足以提供可靠的 seed-level variance 估计。Clustered bootstrap 在 cluster 数量 <5 时的 coverage 性质本身就有文献质疑（Cameron et al., 2008 建议至少 ≥10 clusters）。

但需补充一个 nuance：18-26pp gap 的可信度不完全依赖于统计检验的可靠性，还有 **机制层面的解释支撑**。Table 4 的 failure mode taxonomy 显示 CWM 的 53-74% outputs 为 unparseable（format collapse），这一现象在全部 2-3 seeds 中一致出现，且有明确的机制原因（repo-level CWM 需要生成长结构化输出）。即使统计功效不足以精确量化 gap，"CWM 在 repo-level 存在显著的 format collapse 问题"这一定性结论仍然可信。

然而，R1 关于 ICC=0.191 导致有效自由度远低于名义值的观点完全正确。Mixed-effects LPM 的 z=-23.7 可能过度依赖 per-test observation 的数量（n=56,480）而非独立 seed 的数量。论文应报告 seed-level summary statistics 和 effect size，而非仅依赖 per-test 回归。

---

### Should-Fix

**[AGREE] R1-W1: TOST ±2pp margin 缺乏正式论证**

同意。论文在 Appendix G 描述 margin 的设定为 "based on deployment relevance"，但：(1) 未引用 code generation/verification 领域任何先例；(2) 未提供 smallest effect size of interest (SESOI) 的正式推导。Appendix J (Table 13) 确实报告了不同 margin 下的 TOST p-value 敏感性分析（margin 从 1.0 到 5.0pp），显示 CLS-CWM 等价在 margin ≥1.52pp 时即达显著——这提供了一定的 robustness 证据。但形式化的 margin 论证仍然缺失。

R1 引用 Dror et al. (2018) "Hitchhiker's Guide" 作为 missing reference 也合理，该文是 NLP 统计检验的标准参考，虽然主要讨论 superiority testing，但其方法论框架对 equivalence testing 的 margin 选择同样适用。

---

**[AGREE] R1-W2: 训练数据量不对称（CLS ~70K vs TRAJ ~1,386）**

这是一个我在自己的审稿中未充分关注的重要问题。同意这构成 substantial confound。

CLS 和 CWM 在 per-test level 训练（每个 test case 一个 instance），产生 ~70K 训练 instances；TRAJ 在 per-patch level 训练（每个 patch 一个 instance），只有 ~1,386 instances。虽然这种差异是 formulation 设计的内在属性（TRAJ by design 是 patch-level），但它与 formulation 效果完全混淆。论文在 Section 3.7 (Threats to Validity) 虽提及 "training data volume remains uncertain"，但未进行 R1 建议的 downsample 实验来隔离训练数据量 vs. formulation 的贡献。

这一混淆直接影响 CLS–TRAJ 比较的可解释性：TRAJ 的相对劣势可能部分来自训练数据量不足（~50x 更少的训练 instances），而非 formulation 本身的劣势。

---

**[AGREE] R1-W3: DeepSeek-Coder 仅 2 seeds**

同意。Table 1 中 DeepSeek-Coder 的 function-level 结果基于 2 seeds，CI 确实未报告（仅报告了 Qwen3 的 5-seed CI）。这使跨模型族一致性的论证在 DeepSeek-Coder 端缺乏统计支撑。论文应在 Table 1 中为 DeepSeek-Coder 也报告 CI，即使只有 2 seeds 的 CI 很宽。

---

**[AGREE] R1-W4: CWM format collapse 是 confound 还是 inherent property**

强烈同意，这与我自己的 N1 concern 高度相关。论文将 format collapse 视为 CWM 在 repo-level 的 inherent limitation，但 intervention space 非常有限：

论文测试了四种 intervention（Section 3.5, paragraph (g)）：
- Capacity (rank 32)
- Majority voting (K=3)
- Relaxed matching
- Model scaling (4B→8B)

但关键缺失的 intervention 是 **constrained decoding**——如 PICARD (Scholak et al., 2021) 或 Synchromesh (Poesia et al., 2022)，可以在解码时强制输出符合预定义 schema。论文在 Limitations 中提及 "constrained decoding, output-format pretraining" 未评估，但考虑到 format collapse 是 repo-level 18-26pp gap 的主要驱动因素，这一缺失显著削弱了 "formulation-inherent" 的归因。

R1 提出的 missing reference（PICARD, Synchromesh）完全合理——这些是 constrained decoding 的标准参考，应在 Related Work 或 Discussion 中讨论。

---

**[AGREE] R1-W5: 外部效度受限于合成数据和 Python-only**

同意。合成 mutation（5 种类型：gold, operator_swap, off_by_one, return_value, boundary_removal）的分布可能与真实 developer bug 分布存在系统偏差。Table 9 的 mutation type breakdown 显示 operator_swap 在 repo-level 的分布差异尤为显著（从 val 19.1% 到 test 34.3%），论文自身也承认这导致了 train-test distribution mismatch。

对结论的影响：如果真实 bug 的分布更集中在某些 mutation type 上（如 semantic errors 而非 syntactic），CLS 和 CWM 的相对表现可能不同。

---

**[AGREE] R1-W6: Mixed-effects LPM vs GEE 不一致**

同意需要解释。从 Appendix M 的描述来看：
- LPM: formulation×model interaction p=0.002（显著）
- GEE: 同一 interaction non-significant

论文在 Appendix M 中提供了两个模型的结果但未直接对比解释差异原因。可能的原因包括：(1) GEE 使用 exchangeable working correlation 结构可能更保守；(2) LPM 和 GEE 对 cluster 内相关的建模方式不同（LPM 用随机效应，GEE 用 sandwich SE）；(3) GEE 在 cluster 数量较少时的 finite-sample 性质可能不同。论文应明确说明哪个是 primary model 并解释 discrepancy。

---

### Questions

**[AGREE] R1-Q1: Downsample CLS 到 ~1,386 与 TRAJ 对比**

完全支持这个问题。这是解耦 formulation effect 和 training data volume effect 的直接方法。如果 CLS 在 1,386 instances 下表现大幅下降到接近 TRAJ 水平，则 TRAJ 的"劣势"可能主要来自数据量不足。

---

**[AGREE] R1-Q2: Constrained decoding 缓解 CWM format collapse**

同上 W4 的讨论。这是 must-answer 的问题。

---

**[AGREE] R1-Q3: Oracle scoring 对部分正确 patch 的处理**

合理的问题。当前 oracle scoring（Section 2.2）使用 F2P test count T 和 pass@1 metric。如果一个 patch 修复了 4/5 tests，per-test formulations（CLS, CWM）可以识别部分正确性，而 TRAJ 只给出一个整体 verdict。Oracle scoring 是否低估了 per-test formulations 的实际价值（diagnostic granularity），值得讨论。

---

**[REBUT] R1-Q4: 去除 unparseable outputs 后 CLS vs CWM gap 是否缩小**

论文在 Appendix N (CWM Parseable Bias Analysis) 中部分回答了这个问题。根据 page 20 的分析：
- CWM 的 parseable outputs 存在 **parseable bias**：模型在 simpler instances 上更容易生成 parseable output（74.6% accuracy on parseable vs. 66.35% overall）
- 即使仅看 parseable CWM outputs，accuracy 仍受 selection bias 影响——parseable instances 不是 random sample
- Appendix N 明确指出 "CWM's reported accuracy is inflated by default assignments on easy instances"

因此，简单去除 unparseable outputs 并比较不能得到 fair comparison——因为 parseable subset 本身是 non-random 的。这是一个 **conditioning on a post-treatment variable** 的问题。R1 的问题有效，但论文已部分 address 了这一点。

---

**[REBUT] R1-Q5: z=−23.7 是否主要由 n=56,480 驱动**

不完全同意这一担忧。虽然大样本确实会让微小效应也统计显著，但此处的 effect size 本身极大：

- CLS-CWM repo-level gap = 18-26pp（Table 3）
- 这不是 0.1pp 级别的微小差异被大 n 放大，而是 effect size 本身就处于 "very large" 范畴
- Appendix H 报告了 effect sizes，CLS-CWM 的 Cohen's d（或等价指标）在 repo level 应当非常大
- 即使将 n 缩减到 seed-level（n=2-3），18-26pp 的 gap 仍然在任何合理的 margin 下都是 practically significant

R1 的 concern 对小效应成立（如 function-level 的 CLS-CWM 差异 <1pp），但对 repo-level 的 18-26pp gap 不成立。z=-23.7 在这里反映的是 **确实很大的效应 + 很大的样本**，而非 **微小效应被大样本放大**。

不过 R1 的隐含建议是正确的：论文应在主文中同时报告 standardized effect size 和 test statistic，让读者自行判断 practical significance。

---

### Missing References

**[AGREE] Scholak et al. (2021) PICARD / Poesia et al. (2022) Synchromesh**

完全同意应引用。鉴于 CWM 的 format collapse 是 repo-level 核心问题，constrained decoding 文献的缺失使得论文在讨论 mitigation strategies 时缺乏 baseline 参照。至少应在 Discussion/Limitations 中讨论为什么未使用 constrained decoding 以及预期效果。

**[AGREE] Dror et al. (2018)**

作为 NLP 统计检验的标准参考，考虑到本文大量使用统计检验，引用此文有助于为方法论选择提供上下文。

---

### 与我自身审稿意见的对照

R1 的审稿与我的审稿在以下方面互补：

1. **共同关切**：R1-W4（format collapse confound）与我的 N1（complexity vs output format confound）高度一致，从不同角度指出同一核心问题——论文未充分解耦 CWM 退化的原因。

2. **R1 发现但我遗漏的重要问题**：
   - R1-W2（训练数据量不对称 ~70K vs ~1,386）——这是我审稿中的显著遗漏。数据量差异与 formulation 效果完全混淆，对 TRAJ 比较的可解释性影响很大。
   - R1-N2（repo-level seed 数量不足）——我提到了 14B 的 3 seeds 问题（我的 N2），但未像 R1 那样系统地质疑整个 repo-level 的 2-3 seeds 可靠性。
   - R1-W6（LPM vs GEE 不一致）——我在审稿中未关注到这一具体 discrepancy。

3. **我提出但 R1 未覆盖的问题**：
   - 我的 N2：≤8B LoRA scope 下标题/abstract 过广泛的泛化——R1 未直接提及
   - 我的 W2：Error complementarity 贡献被高估——R1 未评论
   - 我的 W3：每个 complexity level 仅单一 benchmark——R1 未提及
   - 我的 W4：Cross-domain GenRM 比较分析浅薄——R1 未提及

4. **评分一致性**：两位 reviewer 均给出 Overall 3.5 (Borderline Conference)，Soundness 和 Excitement 评分方向一致（R1: 4/3，我: 3.5/3），反映了对论文优缺点的基本共识——方法论严谨但新颖性有限。

---

### 综合建议

基于两位 reviewer 的共同关切，建议 authors 优先处理：

1. **解耦 complexity vs. output format**（R1-W4 + R2-N1）：核心问题
2. **训练数据量控制实验**（R1-W2, R1-Q1）：downsample CLS 到 TRAJ 级别
3. **CLS-TRAJ 统计结论的重新措辞**（R1-N1）：从 "not confirmed" 改为 "underpowered, inconclusive"
4. **Repo-level seed-level variance 报告**（R1-N2）：报告 seed-level effect sizes
5. **Constrained decoding 讨论**（R1-W4, R1-Q2）：至少定性讨论，最好有实验

---

[Reviewer 2 审稿结果]:
已提交交叉回应。逐条总结：

- **R1-N1 (TRAJ power)**: [AGREE] — power ~0.3 下 "not confirmed" 措辞有误导性，应改为 "underpowered, inconclusive"
- **R1-N2 (repo seeds)**: [AGREE with nuance] — 统计上 n=2-3 确实不足，但 format collapse 机制提供定性支撑
- **R1-W1 (TOST margin)**: [AGREE] — ±2pp 缺乏正式推导，但 Appendix J 有 sensitivity analysis
- **R1-W2 (data asymmetry)**: [AGREE] — 70K vs 1,386 是重要混淆因素，我审稿中遗漏了此点
- **R1-W3 (DeepSeek 2 seeds)**: [AGREE]
- **R1-W4 (format collapse)**: [AGREE] — 与我的 N1 从不同角度指向同一核心问题
- **R1-W5 (external validity)**: [AGREE]
- **R1-W6 (LPM vs GEE)**: [AGREE] — 应解释 discrepancy
- **R1-Q4 (remove unparseables)**: [REBUT] — Appendix N 已分析 parseable bias，简单移除会引入 selection bias
- **R1-Q5 (z driven by n)**: [REBUT] — 18-26pp 本身是极大 effect size，非微小效应被大 n 放大

两位 reviewer 的 Overall 均为 3.5，核心共识：方法论严谨但新颖性有限，complexity vs. output format 混淆是最需解决的问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1392 · 2026-05-23T15:18:58.760288+00:00_

审稿报告已投递至 Research Director。

**Round 16 审稿完成。**

- **评分**: 3.5 / 5 (Borderline Conference)
- **置信度**: 4/5
- **Reviewer 编排**: 2 人，1 轮独立审稿 + 1 轮交叉分享，达成共识
- **Issue Tracker**: 已同步更新（4 个新 open issues: R16-N1/N2/W1/W2 + 3 个 minor）

**核心发现**:
- 4 个 Must-Fix（complexity vs output format 混淆、scope 泛化过广、CLS-TRAJ underpowered、repo-level seed 不足）
- 8 个 Should-Fix（统计方法层次、TRAJ 比较性质、complementarity 高估、format collapse 归因、TOST margin、数据不对称、GenRM 对比、外部效度）
- 两位 Reviewer 交叉后 8 AGREE / 2 REBUT（R1）+ 8 AGREE / 2 REBUT（R2），高度一致

注：R2 的交叉回应在报告投递后到达。R2 对 R1 的 8 个 AGREE 和 2 个 REBUT（Q4 parseable bias 已有分析、Q5 z=-23.7 反映真实大 effect size）与报告结论完全一致，不改变评分和建议。R2 补充的重要发现——R1-W2 训练数据量不对称（70K vs 1,386）是 R2 自审中遗漏但交叉后认同的关键混淆——已在报告 W6 中覆盖。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 125

## Round 125

44 recorded events


### User

_source line 1393 · 2026-05-23T17:19:54.894651+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1394 · 2026-05-23T17:19:59.836286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-23T17:19:59.887443+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1396 · 2026-05-23T17:20:07.678012+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-23T17:20:07.728780+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-23T17:20:11.946166+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1399 · 2026-05-23T17:20:11.996872+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1400 · 2026-05-23T17:20:25.034992+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1401 · 2026-05-23T17:20:25.085623+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1402 · 2026-05-23T17:20:27.296123+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-23T17:20:27.396963+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1404 · 2026-05-23T17:20:31.011230+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 1405 · 2026-05-23T17:20:32.516760+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (266 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D131-cwm-s42-epoch3-seq2048（准备中）\n- D133-cwm-s42-e2-seq2048-home-resume（准备中）\n- deepseek-cwm-repo-s42-epoch2-eval: Eval CWM s42 epoch 2 checkpoint 解耦过拟合 vs seed 差异：如果 epoch 2 accuracy >> epoch 3 (56.7%)，则 CWM repo-level 在 epoch 3 过拟合（准备中）\n- …另有 9 项\n\n## 近期结论\n- **deepseek-cwm-repo-s456-train-v2** (success): DeepSeek CWM rep
…[truncated 1827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1505
}
```

</details>

---


### Tool call

_source line 1406 · 2026-05-23T17:20:33.018998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1407 · 2026-05-23T17:20:33.471188+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\usepackage{xcolor}
21	\graphicspath{{../../artifacts/}}
22	
23	% Lists
24	\usepackage{enumitem}
25	
26	% Custom commands
27	\newcommand{\cls}{\textsc{Cls}}
28	\newcommand{\cwm}{\textsc{Cwm}}
29	\newcommand{\traj}{\textsc{Traj}}
30	\newcommand{\fone}{F\textsubscript{1}}
31	\newcommand{\pp}{\,\text{pp}}
32	\newcommand{\tbd}{\textsc{tbd}}
33	\newcommand{\placeholder}[1]{{\color{red}\texttt{[#1]}}}
34	
35	\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}
36	\author{Anonymous}
37	
38	\begin{document}
39	\maketitle
40	
41	\input{abstract}
42	
43	\input{introduction}
44	
45	\begin{figure*}[t]
46	\centering
47	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
48	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
49	\label{fig:reformulation}
50	\end{figure*}
51	
52	\input{method}
53	
54	\input{experiments}
55	
56	
57	\input{related_work}
58	
59	\input{conclusion}
60	
61	\bibliography{references}
62	
63	% ARR checklist is filled in OpenReview submission form, not in PDF
64	% \input{checklist}
65	
66	\input{appendix}
67	
68	\end{document}
69	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1408 · 2026-05-23T17:20:33.471764+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines page limit author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines page limit author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1409 · 2026-05-23T17:20:34.174964+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1410 · 2026-05-23T17:20:34.477099+00:00_

1	# === Round 6 Issues (Original) ===
2	
3	# --- Round 6 Must-Fix (Consensus Critical) ---
4	
5	- id: "R6-N1"
6	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
7	  category: experiment
8	  severity: critical
9	  status: resolved
10	  first_raised_round: 6
11	  last_seen_round: 16
12	  mentions:
13	    - round: 6
14	      reviewers: [1, 2]
15	      note: "两人独立提出，最高共识。"
16	    - round: 7
17	      reviewers: [pre-review]
18	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress."
19	    - round: 8
20	      reviewers: [1, 2]
21	      note: "Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp."
22	    - round: 9
23	      reviewers: [1, 2]
24	      note: "Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported."
25	    - round: 10
26	      reviewers: [1, 2]
27	      note: "Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations."
28	    - round: 11
29	      reviewers: [1, 2]
30	      note: "Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion."
31	    - round: 13
32	      reviewers: [1]
33	      note: "Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure."
34	    - round: 14
35	      reviewers: [1, 2]
36	      note: "Fresh review R14. R1-N2 re-raises. R2 REBUT 指出 R1 混淆两个统计模型。Dire
…[truncated 23390 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 1411 · 2026-05-23T17:20:44.669453+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines page limit author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

I found information about EMNLP 2026 and ARR submission guidelines. Let me search for more specific details about page limits and author instructions.

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Pap
…[truncated 2587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 11197
}
```

</details>

---


### Tool call

_source line 1412 · 2026-05-23T17:21:18.933141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1413 · 2026-05-23T17:21:19.285126+00:00_

1	\begin{abstract}
2	LLM-based repair generates candidate patches, selecting the best via a verifier. Three execution-free alternatives to expensive execution-based verification have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level scoring (\traj{}). No prior work compares \cls{} and \cwm{} under matched conditions; the \traj{} comparison is inherently confounded.
3	
4	We present the first systematic comparison across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is not confirmed after multiple comparison correction at current power (${\sim}$0.3), but the gap narrows monotonically from 3.11\pp{} (4B) to 1.07\pp{} (14B). At repository level, this equivalence diverges sharply (DeepSeek-Coder): the \cls{}--\cwm{} gap widens to 18--26\pp{} across 2--3 seeds under our ${\leq}$8B LoRA protocol, accompanied by format collapse. At 14B (3 seeds, single family), all three formulations narrow to within 1.07\pp{}, a preliminary observation consistent with capacity-dependent convergence.
5	
6	Error complementarity and a failure mode taxonomy motivate complexity-aware routing, though simple heuristics capture $<$0.4\pp{} of oracle advantage.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-23T17:21:19.285600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1415 · 2026-05-23T17:21:19.738158+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. This connects to a broader pattern in NLP: task formulation---classification vs.\ generation vs.\ span extraction---systematically affects performance~\cite{raffel2020t5}, but the conditions under which each wins remain task-dependent and empirically unresolved. Recent evidence that generation-based verification outperforms classification in mathematical reasoning~\cite{hosseini2025genrm} raises a further question: does this advantage transfer to code verification, where outputs are longer and format-constrai
…[truncated 3729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1416 · 2026-05-23T17:21:19.738675+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1417 · 2026-05-23T17:21:21.223037+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Expected Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation has charact
…[truncated 3341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 1484
}
```

</details>

---


### Tool call

_source line 1418 · 2026-05-23T17:21:21.324029+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1419 · 2026-05-23T17:21:21.575718+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench}; runs with NaN validation loss (due to truncated targets exceeding 2,048-token limits) default to the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Qwen3 \cwm{} runs show early overfitting (best at ${\sim}$6\% of training); checkpoint details in Appendix~\ref{app:hyperparams}.
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model
…[truncated 20650 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1420 · 2026-05-23T17:21:21.576168+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "ROADMAP.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "ROADMAP.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1421 · 2026-05-23T17:21:21.627149+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/ROADMAP.md\", \"content\": \"# exec-sim-repair-verifier — Research Dashboard\\n\\n> 最后更新: 2026-05-23 16:52 UTC\\n\\n> 最后更新: 2026-05-23 16:45 UTC | 更新原因: 修正 GPU 状态（Reviewer warning）\\n\\n> 核心方向: Execution-free verification formulation comparison (CLS vs CWM vs TRAJ). 详见 paper_framing.md.\\n\\n## 当前进展\\n- **阶段**: R16 修复完成 (3.5 Borderline Conference) → Excitement 叙事升级 → R17 验证中 → 最终提交\\n- **评分轨迹**: R14/R15 3.0 → R16 3.5 → R17 待回\\n- **实验**: 全部训练完成（266 个，151 成功，含 14B scaling 全系列）；3 个 CWM eval 仍在运行\\n- **14B 验证**: ✅ CLS/CWM/TRAJ × 3 seeds + baselines 全部完成\\n- **论文修复**: ✅ R16 N1 mechanistic pathway + W1 statistical hierarchy + Excitement 叙事升级\\n- **Rebuttal**: ✅ 四大 recurring issues 草稿完成 (artifacts/rebuttal_draft.md)\\n\\n## 近期任务\\n- [x] R16 修复执行（N1 + W1 + M1）\\n- [x] Excitement 叙事升级（GenRM 动机 + Abstract + Conclusion）\\n- [x] Rebuttal material 准备\\n- [x] ARR checklist 字段准备\\n- [ ] R17 验证审稿结果处理\\n- [ ] 论文最终一致性检查（Agent 执行中）\\n- [ ] 最终 PDF 编译 + 视觉检查\\n- [ ] ARR 提交（DDL 5/25）\\n\\n## GPU 预算\\nSeetaCloud 4×RTX 5090 × 2 台\\n- GPU 0: CWM s123 ckpt-300 re-eval (7.4%, DDL 后完成)\\n- GPU 1: CWM s456 ckpt-300 re-eval (8.4%, DDL 后完成)\\n- GPU 2: 空闲\\n- GPU 3: CWM ckpt-6100 eval (40.2%, 预计 DDL 前完成 — 可为 Appendix CWM convergence 提供数据)\\n不 kill 现有 eval，无其他任务需要 GPU。\\n\\n## ⚠️ 风险\\n- **DDL May 25** — 距离 2 天，论文基本就绪，等 R17 后做最终调整\\n- **Excitement ceiling** — Reviewer 评估 3.0-3.25 (叙事升级后)，Overall ceiling 3.5-3.75\\n- **结构性限制** — comparison 论文无新方法，Excitement ≥3.5 困难\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D170 | 2026-05-23 | 14B TOST/ROPE values corrected to seed-level analy | — |\\n| D169 | 2026-05-23 | CLS-TRAJ TOST 使用 seed-level paired t-test (p=0.025 | — |\\n| D168 | 2026-05-23 | 14B 叙事升级方案定稿：降低 capacity claim 强度，避免 repo-level ov | — |\\n| D167 | 2026-05-23 | 启动 14B multi-seed (s123, s456) CLS+CWM function-le | cls14b-fu
…[truncated 977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1422 · 2026-05-23T17:21:31.050136+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1423 · 2026-05-23T17:21:31.401982+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. CodeScaler~\cite{zhu2026codescaler} trains execution-free reward models for both RL and test-time scaling. Verification formulations span trajectory-level reward~\cite{shum2025swerm}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. GenRM~\cite{hosseini2025genrm} and GenPRM~\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formula
…[truncated 1495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1424 · 2026-05-23T17:21:31.402378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1425 · 2026-05-23T17:21:31.503013+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} equivalence is not confirmed after correction, but the gap narrows monotonically to 1.07\pp{} at 14B. At repository level under ${\leq}$8B LoRA, divergence reaches 18--26\pp{} ($z{=}-23.7$), consistent across families (\S\ref{sec:threats}). Preliminary 14B results (3 seeds, single family) narrow all gaps to within 1.07\pp{}; whether the repo-level divergence is formulation-inherent or capacity-contingent remains open. This contrasts with mathematical reasoning, where generative verification outperforms discriminative~\cite{hosseini2025genrm}; we hypothesize this reflects output structure---code verification requires exact-match outputs (${\sim}$477 tokens/test for \cwm{} vs.\ 1 for \cls{}), and $>$50\% of repo-level \cwm{} outputs are unparseable, in which generation becomes a format fidelity challenge absent in math. If confirmed at larger scale, the 14B convergence trend would partially reconcile our findings with GenRM's generation advantage, suggesting a capacity-dependent account that bridges both domains.
5	
6	Three directions follow: (1)~complexity-aware routing; (2)~scaling to 32B+ with more seeds~\cite{meta2025cwm}; (3)~per-test diagnostics for downstream repair.
7	
8	\section*{Limitations}
9	
10	Primary findings use ${\leq}$8B LoRA fine-tuning with multi-seed replication; 14B results use a single model family (Qwen3) with 3 seeds; cross-family replication and evaluation at 32B+ are needed. The repo-level gap may diminish at 32B+ scale or with execution-trace pretraining~\cite{meta2025cwm}. All evaluation uses Python-only benchmarks; other languages may exhibit different format compliance rates. Training data uses synthetic mutation operators~\cite{andrews2005mutation,just2014mutants}
…[truncated 229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1426 · 2026-05-23T17:21:32.357132+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-23T17:21:32.859977+00:00_

1	\appendix
2	
3	\noindent\textbf{Appendix overview.} A: Oracle resolve advantage. B: Ablation studies. C-F: Extended analysis (error complementarity, parseable accuracy, forced parsing, qualitative errors, failed interventions, mutation scaling, inference efficiency, re-repair, chain-of-thought). G: TOST sensitivity (G.1: Bayesian ROPE). H: Effect sizes. I: Holm-Bonferroni. J: Mixed-effects regression. K: Parseable bias. L: CWM convergence. M: Few-shot. N: Threats. O: Downsample. P: Use of AI assistants.
4	
5	\section{Oracle Accuracy-Utility Analysis}
6	\label{app:oracle}
7	
8	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
14	\label{tab:oracle}
15	\resizebox{\columnwidth}{!}{%
16	\setlength{\tabcolsep}{3pt}
17	\begin{tabular}{lcccc}
18	\toprule
19	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
20	\midrule
21	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
22	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
23	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
24	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
25	\midrule
26	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
31	\begin{figure}[h]
32	\centering
33	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
34	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contrib
…[truncated 9708 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1428 · 2026-05-23T17:21:33.313426+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1429 · 2026-05-23T17:21:33.516791+00:00_

&lt;persisted-output>
Output too large (49KB). Full output saved to: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier--claude-sessions-review-director-06def7c3/d2d630f9-f1ab-4a70-b9b8-3551b78ce993/tool-results/toolu_011XJ56mcnXjZyRndDTffcfh.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_3.md:156:外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置）。跳过。
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_4.md:185:**状态：未配置**（`external_review.paperreview_ai.enabled` 未设置）。跳过。
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_7.md:150:外部审稿：未请求（项目未启用 external_review）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/chats/worker_infra_home-cwm-s42-e2-setup-launch_20260518T144853.jsonl:81:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260517T034206/logs/review_worst.log:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_best.log:40:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_best.log:74:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_best.log:78:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_best.log:87:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-
…[truncated 359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 1430 · 2026-05-23T17:22:02.974958+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 1431 · 2026-05-23T17:22:25.540431+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22565
}
```

</details>

---


### Tool call

_source line 1432 · 2026-05-23T17:22:25.692012+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff",
  "director_session_key": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "text": "你是 Reviewer 1，负责审查方法严谨性和实验设计。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR Long Paper)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，references 不限，Limitations 不计入页数\n- **模板**: ACL style (review mode)\n- **匿名规则**: Double-blind (anonymous ARR submission)\n- **ARR Checklist**: 在 OpenReview submission form 中填写，不在 PDF 中\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文信息\n- **标题**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_15/submitted.pdf\n\n## 你的审查侧重\n\n**方法严谨性 + 实验设计**，重点关注：\n\n1. **统计方法的正确性和适当性**：\n   - TOST equivalence testing 的使用是否恰当？±2pp SESOI 的选择有无充分论证？\n   - Holm-Bonferroni 校正是否正确应用？\n   - Bayesian ROPE 作为 robustness check 是否合理？\n   - 统计功效 (~0.3) 对结论的影响是否充分讨论？\n   - 统计方法层次（primary vs robustness check）是否清晰声明？\n\n2. **实验控制变量**：\n   - CLS/CWM/TRAJ 三种 formulation 的比较是否在 matched conditions 下进行？\n   - Checkpoint selection 策略是否公平（CWM NaN val loss → 使用 final epoch）？\n   - Seed 覆盖是否充分（function-level 5 seeds vs repo-level 2-3 seeds）？\n   - 混合精度 (bfloat16 vs NF4) 对结论的影响？\n   - TRAJ 训练配置差异（~400 vs ~70K samples）是否被适当控制/标注？\n\n3. **Claims 与证据匹配度**：\n   - \"Complexity-moderated formulation choice\" 叙事是否有充分证据支撑？\n   - 14B convergence 声称是否过强（3 seeds, single family）？\n   - Repo-level gap (18-26pp) 的因果归因是否合理？\n   - CWM format collapse 的归因：inherent limitation vs engineering artifact？\n   - Error complementarity 的 framing 是否恰当（oracle gap 大但 heuristic 几乎无效）？\n\n4. **Threats to validity 讨论的充分性**：\n   - 五个 confound 是否涵盖所有主要威胁？\n   - 是否有遗漏的重要 confound？\n\n请逐项给出评价，并按 Must-Fix / Should-Fix / Minor / Nitpick 分类标注严重程度。在报告末尾给出 Overall Assessment（按 EMNLP 2026 评分标准）、Excitement（1-5）、Confidence（1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff",
    "director_session_key": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
    "text": "你是 Reviewer 1，负责审查方法严谨性和实验设计。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR Long Paper)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，references 不限，Limitations 不计入页数\n- **模板**: ACL style (review mode)\n- **匿名规则**: Double-blind (anonymous ARR submission)\n- **ARR Checklist**: 在 OpenReview submission form 中填写，不在 PDF 中\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文信息\n- **标题**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_15/submitted.pdf\n\n## 你的审查侧重\n\n**方法严谨性 + 实验设计**，重点关注：\n\n1. **统计方法的正确性和适当性**：\n   - TOST equivalence testing 的使用是否恰当？±2pp SESOI 的选择有无充分论证？\n   - Holm-Bonferroni 校正是否正确应用？\n   - Bayesian ROPE 作为 robustness check 是否合理？\n   - 统计功效 (~0.3) 对结论的影响是否充分讨论？\n   - 统计方法层次（primary vs robustness check）是否清晰声明？\n\n2. **实验控制变量**：\n   - CLS/CWM/TRAJ 三种 formulation 的比较是否在 matched conditions 下进行？\n   - Checkpoint selection 策略是否公平（CWM NaN val loss → 使用 final epoch）？\n   - Seed 覆盖是否充分（function-level 5 seeds vs repo-level 2-3 seeds）？\n   - 混合精度 (bfloat16 vs NF4) 对结论的影响？\n   - TRAJ 训练配置差异（~400 vs ~70K samples）是否被适当控制/标注？\n\n3. **Claims 与证据匹配度**：\n   - \"Complexity-moderated formulation choice\" 叙事是否有充分证据支撑？\n   - 14B convergence 声称是否过强（3 seeds, single family）？\n   - Repo-level gap (18-26pp) 的因果归因是否合理？\n   - CWM format collapse 的归因：inherent limitation vs engineering artifact？\n   - Error complementarity 的 framing 是否恰当（oracle gap 大但 heuristic 几乎无效）？\n\n4. **Threats to validity 讨论的充分性**：\n   - 五个 confound 是否涵盖所有主要威胁？\n   - 是否有遗漏的重要 confound？\n\n请逐项给出评价，并按 Must-Fix / Should-Fix / Minor / Nitpick 分类标注严重程度。在报告末尾给出 Overall Assessment（按 EMNLP 2026 评分标准）、Excitement（1-5）、Confidence（1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 1433 · 2026-05-23T17:22:44.531296+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18839
}
```

</details>

---


### Tool call

_source line 1434 · 2026-05-23T17:22:44.682414+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff",
  "director_session_key": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "text": "你是 Reviewer 2，负责审查新颖性、完整性和写作质量。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR Long Paper)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，references 不限，Limitations 不计入页数\n- **模板**: ACL style (review mode)\n- **匿名规则**: Double-blind (anonymous ARR submission)\n- **ARR Checklist**: 在 OpenReview submission form 中填写，不在 PDF 中\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文信息\n- **标题**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_15/submitted.pdf\n\n## 你的审查侧重\n\n**新颖性 + 完整性 + 写作质量**，重点关注：\n\n1. **新颖性和贡献价值（Excitement）**：\n   - 核心贡献是 empirical comparison——这是否足够 EMNLP main conference？还是更适合 Findings？\n   - \"Complexity-moderated formulation choice\" 作为发现是否 novel？是否可预测？\n   - Error complementarity 和 failure mode taxonomy 的贡献价值如何？\n   - 与 GenRM (Hosseini et al.) 的 domain-specific 对比是否提供了 new insight？\n   - 14B convergence 作为 preliminary observation 是否增加 excitement？\n\n2. **Related Work 完整性**：\n   - 是否覆盖了所有重要的近期工作？\n   - 与 CodeRM, CodeScaler, GenPRM, CodePRM, SWE-RM 等的比较是否充分？\n   - Execution simulation (CRUXEval, RepoExec, SolidCoder) 引用是否完整？\n   - Process vs Outcome supervision 的讨论是否准确？\n   - 是否有遗漏的 EMNLP/ACL/NeurIPS 2025-2026 重要相关工作？\n\n3. **写作质量和清晰度**：\n   - Abstract 是否在 200 words 以内？是否准确概括核心发现？\n   - Introduction 的 narrative arc 是否清晰？贡献列表是否精准？\n   - 术语使用是否一致（formulation vs method vs approach）？\n   - 表格和图表是否清晰、信息密度是否合理？\n   - Limitations 是否覆盖关键弱点但不过长？\n   - 正文是否超过 8 页？\n\n4. **完整性检查**：\n   - 实验是否覆盖了声称的所有维度（2 families, 2 complexity levels, multiple seeds）？\n   - 是否有明显遗漏的实验或分析？\n   - Appendix 是否过于膨胀？哪些内容应该在正文中？\n   - 标题 \"A Systematic Comparison...\" 是否准确反映论文范围（≤8B LoRA）？\n   - 标题是否暗示了超出实际范围的通用性？\n\n请逐项给出评价，并按 Must-Fix / Should-Fix / Minor / Nitpick 分类标注严重程度。在报告末尾给出 Overall Assessment（按 EMNLP 2026 评分标准）、Excitement（1-5）、Confidence（1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff",
    "director_session_key": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
    "text": "你是 Reviewer 2，负责审查新颖性、完整性和写作质量。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR Long Paper)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，references 不限，Limitations 不计入页数\n- **模板**: ACL style (review mode)\n- **匿名规则**: Double-blind (anonymous ARR submission)\n- **ARR Checklist**: 在 OpenReview submission form 中填写，不在 PDF 中\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文信息\n- **标题**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_15/submitted.pdf\n\n## 你的审查侧重\n\n**新颖性 + 完整性 + 写作质量**，重点关注：\n\n1. **新颖性和贡献价值（Excitement）**：\n   - 核心贡献是 empirical comparison——这是否足够 EMNLP main conference？还是更适合 Findings？\n   - \"Complexity-moderated formulation choice\" 作为发现是否 novel？是否可预测？\n   - Error complementarity 和 failure mode taxonomy 的贡献价值如何？\n   - 与 GenRM (Hosseini et al.) 的 domain-specific 对比是否提供了 new insight？\n   - 14B convergence 作为 preliminary observation 是否增加 excitement？\n\n2. **Related Work 完整性**：\n   - 是否覆盖了所有重要的近期工作？\n   - 与 CodeRM, CodeScaler, GenPRM, CodePRM, SWE-RM 等的比较是否充分？\n   - Execution simulation (CRUXEval, RepoExec, SolidCoder) 引用是否完整？\n   - Process vs Outcome supervision 的讨论是否准确？\n   - 是否有遗漏的 EMNLP/ACL/NeurIPS 2025-2026 重要相关工作？\n\n3. **写作质量和清晰度**：\n   - Abstract 是否在 200 words 以内？是否准确概括核心发现？\n   - Introduction 的 narrative arc 是否清晰？贡献列表是否精准？\n   - 术语使用是否一致（formulation vs method vs approach）？\n   - 表格和图表是否清晰、信息密度是否合理？\n   - Limitations 是否覆盖关键弱点但不过长？\n   - 正文是否超过 8 页？\n\n4. **完整性检查**：\n   - 实验是否覆盖了声称的所有维度（2 families, 2 complexity levels, multiple seeds）？\n   - 是否有明显遗漏的实验或分析？\n   - Appendix 是否过于膨胀？哪些内容应该在正文中？\n   - 标题 \"A Systematic Comparison...\" 是否准确反映论文范围（≤8B LoRA）？\n   - 标题是否暗示了超出实际范围的通用性？\n\n请逐项给出评价，并按 Must-Fix / Should-Fix / Minor / Nitpick 分类标注严重程度。在报告末尾给出 Overall Assessment（按 EMNLP 2026 评分标准）、Excitement（1-5）、Confidence（1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 1435 · 2026-05-23T17:22:46.001320+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1318
}
```

</details>

---


### Assistant

_source line 1436 · 2026-05-23T17:22:55.014346+00:00_

**圆桌审稿会议已启动** (Round 1, Fresh Mode)

**编排**：
- **Reviewer 1** — 方法严谨性 + 实验设计（统计方法、控制变量、claims-evidence 匹配）
- **Reviewer 2** — 新颖性 + 完整性 + 写作质量（contribution value、related work、presentation）
- **视觉审查 Agent** — 已派发，与 Reviewer 并行执行
- **外部审稿** — 未配置，跳过

等待两位 Reviewer 提交初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 126

## Round 126

2 recorded events


### User

_source line 1437 · 2026-05-23T17:27:37.818303+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 方法论审慎、统计框架丰富的系统性实证比较，但 TRAJ 训练数据量不对称构成根本性混淆变量，低统计功效限制了等价性声明的说服力，单基准/单语言的范围制约了结论的泛化性。

## 官方维度打分（来自 ACL ARR review form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心 CLS-CWM 比较有良好控制；但 TRAJ 比较因 175× 数据量差异存在根本性混淆；TOST 功效 ~0.3 使等价性声明本质上不确定 |
| Excitement | 3/5 | 填补了一个真实的文献空白（无先前匹配比较），complexity-moderation 发现有实践价值，但贡献类型为实证比较而非方法创新 |
| Reproducibility | 4/5 | 超参数、种子、checkpoint 选择策略均有详尽披露（Appendix D/E/F）；数据构建流程清晰；但代码/数据未公开 |
| Confidence | 4/5 | 仔细阅读了全文及 15 页附录，熟悉统计等价性检验和代码修复领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] TRAJ 比较的训练数据量混淆变量未得到充分控制
- 具体位置：§3.1, §3.5, Appendix D/E
- 问题：TRAJ 使用 ~400 个 variant-level 训练样本，而 CLS/CWM 使用 ~70K 个 per-test 训练样本，差异达 175 倍。论文声称这一差异是 "inherent to the formulation"（Appendix E: "trajectory-level labels are only available at variant granularity"），但这正是问题所在——论文无法分离 formulation 本身的局限性与训练数据不足的效应。Abstract 和 §3.3 的叙事（"TRAJ parity is not confirmed... but the gap narrows monotonically from 3.11pp to 1.07pp"）隐含地将 TRAJ 的行为归因于 formulation 特性，但 14B 的收敛可能同样是因为更大的模型能更好地从少量数据中学习。
- 为什么影响接收：这是论文三个 formulation 比较的核心之一。如果无法区分 data effect 和 formulation effect，那么关于 TRAJ 的所有结论（包括 §3.5 的 "formulation-inherent" 归因和 §3.6 的 routing 建议）的证据基础不足。
- 建议修改方向：(1) 明确将 TRAJ 比较重新定位为 "formulation + data regime" 的联合比较，而非 formulation 的固有属性比较；(2) 考虑通过数据增强（如对 per-test 标签进行 variant-level 聚合以生成更多 variant-level 样本）来缩小差距，或者进行更极端的 CLS 下采样实验（目前 Appendix O 的下采样到 ~1K 仍然是 TRAJ 的 2.5 倍）；(3) 至少在叙事中明确承认无法分离这两个效应。

**N2** [critical] 统计功效不足以支撑等价性声明的可解释性
- 具体位置：§3.2, §3.4, Appendix J/K/L
- 问题：TOST 功效 ~0.3 意味着即使真实差异在 SESOI 范围内，仍有 70% 概率无法确认等价性。论文对此进行了披露（§3.4: "a 70% probability of failing to confirm equivalence"），但由此产生的分析困境未被充分讨论。具体而言：
  - CLS-CWM 等价性在 function level 被确认（p=0.006, Table 15），这在低功效下仍有信息量——通过检验本身就是强证据。
  - 但 CLS-TRAJ 等价性未通过（p=0.075），在低功效下这既不能作为"等价"的证据，也不能作为"不等价"的证据。论文的措辞（"TRAJ parity is not confirmed"）是技术上正确的，但叙事中（§3.3: "the gap narrows monotonically"）仍然暗示 TRAJ 趋向等价。
  - Repo-level 的比较仅有 2-3 seeds，功效更低，CLS-TRAJ unpaired bootstrap 的宽置信区间（Table 14: CLS-TRAJ ±10.42pp）实际上不允许得出任何方向性结论。
- 为什么影响接收：等价性声明是论文的核心贡献之一（"first systematic comparison"）。如果大多数比较的功效不足以区分 "等价" 与 "不确定"，那么论文的主要发现的信息量被大幅削弱。
- 建议修改方向：(1) 在主文中增加功效分析的表格，列出每对比较在当前样本量下 TOST 能检测到的最小差异（minimum detectable effect, MDE），读者可据此判断结论强度；(2) 对于功效不足的比较（特别是 CLS-TRAJ 和所有 repo-level 比较），明确声明 "inconclusive" 而非 "not confirmed"——后者隐含了方向性判断；(3) 考虑将功效分析从 Appendix K 移至主文 §3.4。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 单基准/单语言限制结论泛化性，但叙事语气偏广
- 具体位置：§5 Conclusion, Limitations
- 问题：全部实验仅在 SWE-bench Verified（500 个实例）上进行，仅 Python 语言，使用合成突变构建训练数据。但 Conclusion 的措辞（"formulation choice is moderated by code complexity"）以一般性命题呈现，未限定于 Python/SWE-bench。Limitations 提到了 "Python-only benchmarks" 和 "codegen-specific" 但放在末尾，读者容易忽略。
- 建议：在 Conclusion 的主要发现中加上范围限定（"on Python code repair benchmarks under ≤8B LoRA"），或者至少增加一个 "our findings should be verified on other languages and benchmarks" 的限定语句。

**W2** [warning] CWM format collapse 的 "inherent limitation" 归因证据不够充分
- 具体位置：§3.5, Appendix I/N
- 问题：论文将 CWM 在 repo-level 的 format collapse（53-74% unparseable）归因为 formulation 的固有局限（"a structural bottleneck rather than a truncation artifact"）。支撑证据包括：(1) early checkpoint 即出现 collapse（Appendix N）；(2) constrained decoding 可强制格式合规但不解决语义问题（Appendix I）；(3) 训练从 seq4096 到 seq8192 提升 unparseable rate 而非降低（Appendix O）。然而：
  - Early checkpoint 出现 collapse 可能反映训练尚未收敛，而非 formulation 固有问题。Appendix N 的 Table 16 显示 CWM repo-level eval loss 在 step 300-400 仍未收敛（"increases monotonically thereafter"），这恰好说明模型在当前训练配置下未能学会 repo-level 的 CWM 格式。
  - 论文仅测试了 ≤8B 的模型。14B 结果（3 seeds, 1 family）已经显示所有 formulation 收敛到 1.07pp 内——这暗示 format collapse 可能是容量不足的结果，而非 formulation 固有。
  - 没有测试其他可能缓解 format collapse 的工程方案（如 output format 简化、分步生成等）。
- 建议：将 "inherent limitation" 重新措辞为 "limitation under current ≤8B LoRA training regime"，并明确讨论更大模型或不同训练策略是否可能解决 format collapse。

**W3** [warning] Error complementarity 的实践价值呈现与证据不匹配
- 具体位置：§3.5, §3.6
- 问题：论文报告 oracle combination 的 accuracy 提升（function: +5.20pp; repo: +4.00pp），然后报告 simple routing heuristics 仅捕获 <0.4pp。§3.6 的 "three directions follow" 仍将 "complexity-aware routing" 列为第一方向。这存在 framing 不一致：如果最简单的 heuristic 几乎无效，那么 routing 作为实践建议的价值需要更多论证。论文在 Appendix A 中承认了这一点（"suggesting a complexity-dependent account that bridges both domains"），但主文的 routing 建议过于乐观。
- 建议：在主文中更明确地讨论 oracle-to-achievable gap，指出 routing 作为研究方向有价值但目前没有实用方案，避免给读者 "已经可以 routing" 的印象。

**W4** [warning] ±2pp SESOI 的选择缺少独立的实践论证
- 具体位置：§3.1, Appendix J
- 问题：论文选择 ±2pp 作为 TOST 的 smallest effect size of interest (SESOI)，论证为 "more conservative than problem-level clustered bootstrap"（§3.1）。但 SESOI 应当基于实践意义而非统计方便——2pp 的 accuracy 差异在代码修复中是否 practically meaningful？如果 verifier 用于 reranking K=10 个 candidate patches，2pp 的 verifier accuracy 差异对最终 repair rate 的影响是多少？论文没有提供这种 downstream 影响的分析。Appendix J 的 sensitivity analysis（±1.5pp 至 ±3pp）表明结论对 SESOI 选择是 robust 的（CLS-CWM 在所有 margin 下等价），但这不替代 SESOI 本身需要实践论证。
- 建议：增加一段简短的论证，将 ±2pp 与下游 repair rate 的预期影响联系起来（例如，"a 2pp difference in per-test accuracy translates to approximately X% difference in end-to-end repair rate under majority voting with K=5"）。

---

## 小问题（不影响接收）

- **M1**: Abstract 接近 200 词限制，建议重新计数确认不超限（EMNLP 2026 限制 200 词）。
- **M2**: Table 1 的 "Training configuration differs (§3.5)" 脚注标注需要更显眼——TRAJ 的配置差异是理解结果的关键前提，仅在脚注中提及容易被忽略。
- **M3**: Figure 2 的 y-axis 从 ~58% 开始（非零起点），论文未在 caption 中标注 "axis does not start at zero"（注意：Figure 3 的 caption 已包含此标注）。虽然 Figure 2 标题中可能不需要，但统一处理更好。
- **M4**: §2.3 的 Oracle Accuracy-Utility Framework 介绍了 ICC 但 IRC（Intra-Rater Correlation）在正文中未使用——Appendix A 中使用的是 ICC，而 IRC 仅在 Appendix 中出现一次。考虑简化或统一术语。
- **M5**: Limitations section 提到 "scaling to 32B+ with more seeds" 和 "(3) per-test diagnostics for downstream repair"——这更像 future work 而非 limitations。建议聚焦于当前工作的局限性本身。

---

## 主要优势

1. **实验设计审慎**：matched experimental framework（相同超参数、种子、checkpoint 策略、数据集）是本文最大的方法论优势。CLS 和 CWM 的比较确实在 well-controlled conditions 下进行，这在prior work 中是缺失的。
2. **统计方法层次清晰**：TOST 作为 primary + Bayesian ROPE 作为 robustness check + mixed-effects regression 作为 mechanism analysis，层次合理且各自的角色声明清楚（§3.1, Appendix J/M）。
3. **诚实的局限性披露**：论文坦承功效不足（§3.4）、CLS-TRAJ 等价性未被确认（§3.2）、confound 分析不能完全排除混淆（§3.7）。这种诚实性在实证研究中值得肯定。
4. **丰富的附录**：15 页附录包含 qualitative error analysis（Appendix H/I）、failure mode taxonomy（Table 4）、parseable bias analysis（Appendix N）、extended validity discussion（Appendix O/P）等，大幅提升了论文的可审查性。
5. **Failure mode taxonomy**（Table 4）：按 formulation 分类的错误模式（format collapse / decision collapse / aggregation penalty）是有实践价值的贡献，为从业者选择 formulation 提供了可操作的诊断标准。

---

## 评分汇总

| 维度 | 分数 |
|------|------|
| Overall Assessment | 3.5 (Borderline Conference) |
| Soundness | 3/5 (Acceptable) |
| Excitement | 3/5 (Interesting) |
| Reproducibility | 4/5 (Mostly reproducible) |
| Confidence | 4/5 (Quite sure) |

**总结**：这是一篇方法论审慎的实证比较论文，填补了 CLS/CWM/TRAJ 无匹配比较的文献空白。CLS-CWM 的比较在 function-level 有可信的等价性证据，complexity-moderation 发现有实践价值。但两个核心问题——TRAJ 的 175× 训练数据量混淆变量和 TOST ~0.3 的统计功效——削弱了部分核心声明的证据强度。解决 N1（重新定位 TRAJ 比较的 claim scope）和 N2（增加 MDE 分析并明确 inconclusive 比较）后，本文可达到 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1438 · 2026-05-23T17:27:52.052098+00:00_

收到 Reviewer 1 审稿意见。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 127

## Round 127

2 recorded events


### User

_source line 1439 · 2026-05-23T17:27:54.546672+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：我对论文给出 **Overall 3.5 (Borderline Conference)**，识别了 2 个 Must-Fix 问题（TRAJ 175× 数据量混淆变量、TOST 功效 ~0.3 限制等价性声明）、4 个 Should-Fix 问题（单基准泛化性、CWM format collapse 归因过强、error complementarity 实践价值 framing 不一致、±2pp SESOI 缺独立实践论证）、5 个小问题。核心判断：CLS-CWM 比较设计良好且结论可信，但 TRAJ 比较存在根本性混淆，建议修改 claim scope 后可达 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1440 · 2026-05-23T17:28:05.396157+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 128

## Round 128

6 recorded events


### User

_source line 1441 · 2026-05-23T17:31:07.778456+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿报告：A Systematic Comparison of Execution-Free Verification Formulations for Code Repair

---

## 总体评分
**Overall**: 3.0 / 5 (Findings)
**一句话总结**: 方法论严谨的实证比较研究，统计分析远超 NLP 论文平均水准，但核心发现可预测性强、实际应用价值有限、研究范围偏窄，更适合 Findings 而非主会议。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 匹配实验设计、TOST 等价检验、Bayesian ROPE、mixed-effects 回归、clustered bootstrap + Holm 校正——统计方法论极为扎实。14B 结论证据不足是主要扣分项。 |
| Excitement | 2.5 / 5 | 无新方法/新架构；核心发现（complexity moderates formulation choice）方向可预测；routing heuristic 仅贡献 <0.4pp；scope 受限于 ≤8B LoRA + Python mutations。对实践者有参考价值，但不够 exciting。 |
| Overall Assessment | 3 / 5 | Findings 水平。Soundness 和 reproducibility 达标，但 novelty 和 impact 不足以进入主会议。 |
| Reproducibility | 4 / 5 | 训练细节、超参数、随机种子、统计检验全部披露；附录提供 prompt 模板和消融实验。代码和数据可用性未明确声明是小瑕疵。 |
| Confidence | 4 / 5 | 我熟悉 code generation verification、reward modeling 和 NLP 实验方法论，仔细阅读了全文和附录。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 标题承诺的通用性远超实际研究范围
- 具体位置：Title, Abstract, §1 ("the first systematic comparison")
- 问题："A Systematic Comparison of Execution-Free Verification Formulations for Code Repair" 暗示了全面的、通用的比较。但实际研究限于：(a) ≤8B 模型 + LoRA（无 full fine-tuning、无 RL）；(b) 仅 2 个模型家族；(c) 仅 Python；(d) 合成 mutation 数据而非真实 bug。14B 补充实验仅 1 个模型家族 3 个种子。"Systematic comparison" 在学术语境中意味着覆盖关键变量空间，但本文的实际覆盖面与此不符。
- 为什么影响接收：Reviewer 和读者期望 "systematic" 意味着更广泛的覆盖。标题与内容之间的落差会被视为 overclaiming——这是 ARR 审稿中常见的拒稿理由。
- 建议修改方向：在标题中加限定词，如 "...under ≤8B LoRA Fine-tuning" 或 "...at Small Scale"，以准确反映研究范围。Abstract 中 "the first systematic comparison" 也应加类似限定。

**N2** [critical] 14B convergence 结论的叙事权重与证据严重不匹配
- 具体位置：Abstract（"At 14B (3 seeds, single family), all three formulations narrow to within 1.07pp"）、§3.3、§5 Conclusion（"Preliminary 14B results...whether the repo-level divergence is formulation-inherent or capacity-contingent remains open"）
- 问题：14B 结果在 abstract、introduction、conclusion 中均作为关键叙事元素出现，但其证据基础极为薄弱：仅 3 个种子、单一模型家族（Qwen3）、TOST 自由度=2 无法确认等价、Bayesian ROPE 在 3 个观测上统计效力极低。论文虽标注 "preliminary observation"，但随后围绕它构建了大量推论——包括 conclusion 中的 "capacity-dependent account" 和与 GenRM 的桥接论述。这种结构让读者高估了 14B 发现的可靠性。
- 为什么影响接收：ARR reviewer guidelines 要求 claims 有 adequate support。将 preliminary 单家族结果作为 abstract 核心内容和 conclusion 叙事框架，属于 evidence 与 claim 之间的 gap。
- 建议修改方向：(1) 将 14B 结果从 abstract 中降级或移除；(2) 在 conclusion 中明确标注这是 speculative direction 而非 supported finding；(3) 或者补充更多 14B 数据（至少第二个模型家族）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 核心发现的可预测性未被充分讨论
- 具体位置：§3.5, §3.6, §5
- 问题："Complexity moderates formulation choice" 是论文的中心贡献，但其方向是直觉可预测的：CWM 在 repo level 需要生成 ~477 tokens 的执行输出并要求 exact match，而 CLS 只需预测 1 个 token——当输出长度增加时 generation 更容易失败，这并不令人意外。论文量化了这个 gap（18-26pp）是有价值的，但没有讨论：(a) 这个结果是否 a priori 可预测？(b) 量化本身提供了什么 beyond confirmation 的 new insight？(c) gap 的大小（18-26pp）相对于简单的 token 数量论证是否出乎意料？
- 建议：在 §3.5 或 §3.6 中增加一段讨论，承认方向的可预测性，并强调量化和 failure mode 分析提供的增量价值。这会使论文更有说服力，而非试图将 expected result 包装为 surprising finding。

**W2** [warning] 实际应用价值有限
- 具体位置：§3.6 (Error complementarity), §1 contributions list
- 问题：论文的三个贡献在实践层面的影响力有限：(1) Simple routing heuristics 仅捕获 <0.4pp 的 oracle advantage——这意味着 error complementarity 虽然存在，但目前无法被利用；(2) failure mode taxonomy 是描述性的（format collapse / decision collapse / aggregation penalty），但没有提供可操作的 mitigation 方案（§3.5 报告所有 4 种 format collapse intervention 均失败）；(3) 论文的实践建议本质上是 "repo level 用 CLS，function level 随便"——这是多数实践者凭直觉就会得出的结论。
- 建议：更坦诚地讨论实践局限性；将 error complementarity 定位为 "motivating future work on learned routers" 而非当前贡献。

**W3** [warning] Mutation-based 训练数据的代表性不足
- 具体位置：§3.1 (Datasets), §3.7 (Threats to Validity), Limitations
- 问题：训练和评估均使用 5 种合成 mutation operator 生成的数据。虽然引用了 Andrews et al. (2005) 和 Just et al. (2014) 论证 mutation 作为 real fault 替代品的有效性，但这些论文是关于 mutation testing 的，不是关于 verification model training 的。论文承认 "synthetic-to-real transfer gap remains untested"（Limitations），但这个限制对 repo-level 结论的影响可能很大：真实 repo-level bug 涉及多文件语义错误、复杂逻辑缺陷，mutation operator 可能无法覆盖。
- 建议：在 §3.7 中更明确地讨论 mutation data 如何可能系统性地偏向某些 formulation（例如，mutation 产生的 "bug" 可能更简单、更局部，可能低估 CWM 在真实 bug 上的优势或劣势）。

**W4** [warning] Appendix 与正文比例失衡
- 具体位置：Appendix A-P（约 12 页 vs 正文 8 页）
- 问题：Appendix 包含 16 个子节（A-P），覆盖 Oracle 分析、LoRA ablation、variant-level accuracy、parseable bias、qualitative error analysis、TOST sensitivity、Bayesian ROPE、mixed-effects 回归等。虽然统计严谨性值得赞赏，但 1.5:1 的附录/正文比暗示可能有重要分析被从正文移到了附录，或者附录中包含了可以精简的冗余内容。例如，Appendix M（Mixed-Effects Regression）的 LPM vs GEE 对比约 1.5 页，但核心结论只需要 2-3 句话。
- 建议：精简 Appendix 中的叙述性文字，保留表格和关键结果。确保正文中引用附录时提供足够上下文，使读者不必翻阅附录才能理解核心论点。

---

## 小问题（不影响接收）

- **术语**："Code World Model"（CWM）术语可能让不熟悉 FAIR CodeGen team 工作的读者困惑。"world model" 在 RL/planning 文献中有特定含义（预测 next state given action）。建议在首次定义时加注释说明其与 RL world model 概念的区别，或更多使用 "execution simulation" 这一更透明的术语。
- **Figure 2 caption**："predict accuracy" 表述含糊——是 verification accuracy 还是 downstream repair accuracy？建议明确。
- **pp 缩写**：论文大量使用 \pp{}（percentage points），应在首次使用时定义（目前在 §1 括号内有定义，但可以更醒目）。
- **Table 1 脚注**："Training configuration differs (§3.5)" 标注在表格底部，但 §3.5 的内容对理解 repo-level 结果至关重要（CLS/CWM 共享 format 但 TRAJ 不同），这个信息值得在正文中更显著地呈现。
- **Abstract 字数**：约 185 词，在 200 词限制内，合规。
- **正文页数**：正文（含 Conclusion）8 页，Limitations 不计入页数，格式合规。
- **匿名性**：未发现违反 double-blind 的信息。

---

## 主要优势

1. **统计方法论远超同类工作**：TOST 等价检验（而非仅不显著）、Bayesian ROPE、clustered bootstrap + Holm 校正、mixed-effects 回归——这套统计框架在 NLP 论文中极为罕见，值得推广。
2. **匹配实验设计**：控制了模型容量、训练数据、计算资源、超参数等关键混淆变量，使得 formulation 之间的比较是公平的。这是方法论层面的真正贡献。
3. **References 覆盖全面**：我检查了 CodePRM、GenPRM、FunPRM、SWE-RM、CodeScaler、RepoExec、VeRPO、Aletheia、SolidCoder、CRUXEval 等近期重要工作，均已引用。Related Work 段落对 GenRM 的 domain-specific 对比分析（math vs code）特别有洞察力。
4. **Failure mode taxonomy（Table 4）**：format collapse / decision collapse / aggregation penalty 的三分类为实践者选择 verification formulation 提供了可操作的诊断标准。
5. **写作整体清晰**：在 8 页内紧凑地呈现了复杂的实验设计和多层次结果，叙事结构合理。

---

## 对 Director 指定审查侧重的逐项回应

### 1. 新颖性和贡献价值（Excitement）
- **核心判断**：这是一篇 empirical comparison 论文，其贡献主要在于 methodological rigor 而非 new insight。对于 EMNLP main conference，这不够 exciting。
- **"Complexity-moderated formulation choice"**：方向可预测（generation 在长输出上更难），但量化有价值。问题是量化本身是否构成足够的贡献。
- **Error complementarity**：理论上有趣，但 <0.4pp 的 practical routing gain 使其更像 future work motivation 而非 standalone contribution。
- **Failure mode taxonomy**：最有实践价值的贡献，但更偏描述性。
- **GenRM domain-specific 对比**：有 new insight（code verification 中 generative ≠ better），但这是 negative result 而非 positive contribution。
- **14B convergence**：证据不足以作为 contribution 计入。
- **总体**：更适合 Findings（soundness + reproducibility 导向）而非 main conference（novelty + impact 导向）。

### 2. Related Work 完整性
- **覆盖率**：非常全面，我未发现重要遗漏。
- **CodeRM, CodeScaler, GenPRM, FunPRM, CodePRM, SWE-RM**：全部引用且讨论恰当。
- **CRUXEval, RepoExec, SolidCoder**：均已引用。
- **Process vs Outcome supervision**：讨论准确，PRM/ORM/GenRM 的类比框架清晰。
- **EMNLP/ACL/NeurIPS 2025-2026 相关工作**：VeRPO、ExecVerify、Aletheia、CodeScaler 等均已覆盖。
- **唯一建议**：可补充 DreamPRM 和 CodePRM 在 Related Work 正文中的具体讨论（目前仅在列表中引用），因为它们与本文的 PRM 类比直接相关。

### 3. 写作质量和清晰度
- **Abstract**：~185 词，在 200 词限制内。准确概括核心发现，但 14B 结果的措辞给人过多权重。
- **Introduction narrative**：清晰的三层结构（fine-tuning → formulation equivalence → complexity-dependent divergence），贡献列表精准。
- **术语一致性**：主要使用 "formulation"，偶尔 "method" 和 "approach"——总体一致。CWM 术语建议改进（见上）。
- **表格和图表**：Table 1-4 设计合理，信息密度适中。Figure 1 直观展示三种 formulation。Figure 2 的 y 轴标签可改进。Figure 3 的 bar chart 能有效传达 per-test advantage 分布。
- **Limitations**：覆盖 3 个关键弱点（scale、language、mutation data），长度适当（约半栏），符合 EMNLP 2026 规范。

### 4. 完整性检查
- **实验覆盖**：声称的维度（2 families, 2 complexity levels, multiple seeds）均有实验支撑。5 seeds 用于 function-level TOST，2-3 seeds 用于 repo-level，14B 用 3 seeds。
- **明显遗漏的实验**：(a) 32B+ 规模；(b) 第二个模型家族的 14B 实验；(c) 真实 bug（非 mutation）上的验证；(d) 下游 repair accuracy 的端到端评估（论文只评估 verification accuracy）。
- **标题准确性**："A Systematic Comparison" 对于仅覆盖 ≤8B LoRA 的工作而言过于宽泛。标题未提及 Python-only 或 mutation-based 这些关键限定。
- **标题暗示的通用性**：是的，标题暗示了超出实际范围的通用性。"Systematic" 一词尤其如此——读者期望看到更多 model scales、training paradigms（RL vs SFT）、和 real-world data。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1442 · 2026-05-23T17:31:51.634716+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff",
  "director_session_key": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: 方法论严谨的实证比较研究，统计分析远超 NLP 论文平均水准，但核心发现可预测性强、实际应用价值有限、研究范围偏窄，更适合 Findings 而非主会议。\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 4/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n### Must-Fix\n\n**N1** [critical] 标题承诺的通用性远超实际研究范围\n- \"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\" 暗示全面比较，实际限于 ≤8B LoRA + 2 families + Python + 合成 mutation。\"Systematic\" 在学术语境中意味着覆盖关键变量空间。标题与内容的落差构成 overclaiming。\n- 建议：标题加限定词如 \"...under ≤8B LoRA Fine-tuning\" 或 \"...at Small Scale\"。\n\n**N2** [critical] 14B convergence 结论的叙事权重与证据严重不匹配\n- 14B 结果在 abstract/introduction/conclusion 中均作为关键叙事元素，但仅 3 seeds、单家族、TOST df=2。论文标注 \"preliminary observation\" 但随后围绕它构建大量推论（capacity-dependent account、GenRM 桥接论述）。\n- 建议：(1) 14B 从 abstract 降级或移除；(2) conclusion 中标注 speculative direction 而非 supported finding。\n\n### Should-Fix\n\n**W1** [warning] 核心发现可预测性未被讨论\n- \"Complexity moderates formulation choice\" 方向直觉可预测：CWM 生成 ~477 tokens + exact match vs CLS 1 token，长输出更难生成不令人意外。论文量化了 gap（18-26pp）有价值，但没讨论结果是否 a priori 可预测、量化提供了什么 beyond confirmation 的 new insight。\n\n**W2** [warning] 实际应用价值有限\n- Simple routing <0.4pp；failure mode taxonomy 描述性但无 mitigation 方案（4 种 intervention 均失败）；实践建议本质上是 \"repo level 用 CLS\"——多数实践者凭直觉就能得出。\n\n**W3** [warning] Mutation-based 训练数据代表性不足\n- 全部使用合成 mutation operator，真实 repo-level bug 涉及多文件语义错误。mutation data 可能系统性偏向某些 formulation。\n\n**W4** [warning] Appendix 与正文比例失衡（~12 页 vs 8 页）\n- 1.5:1 的比例暗示重要分析被移到附录，或附录含冗余内容。\n\n### 小问题\n- CWM 术语可能混淆（与 RL world model 概念冲突）\n- Figure 2 caption \"predict accuracy\" 含糊\n- Table 1 脚注 \"Training configuration differs\" 应更显著\n- Abstract ~185 词合规，正文 8 页合规，匿名性无违反\n\n### 主要优势\n1. 统计方法论极为扎实（TOST + ROPE + clustered bootstrap + Holm + mixed-effects）\n2. 匹配实验设计控制了关键混淆变量\n3. References 覆盖全面（CodePRM, GenPRM, FunPRM, SWE-RM, CodeScaler, RepoExec, VeRPO, Aletheia 等）\n4. Failure mode taxonomy 有实践诊断价值\n5. 写作整体清晰\n\n---\n\n请逐条回应 Reviewer 2 的每个 Must-Fix、Should-Fix 和你认为值得讨论的小问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff",
    "director_session_key": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: 方法论严谨的实证比较研究，统计分析远超 NLP 论文平均水准，但核心发现可预测性强、实际应用价值有限、研究范围偏窄，更适合 Findings 而非主会议。\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 4/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n### Must-Fix\n\n**N1** [critical] 标题承诺的通用性远超实际研究范围\n- \"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\" 暗示全面比较，实际限于 ≤8B LoRA + 2 families + Python + 合成 mutation。\"Systematic\" 在学术语境中意味着覆盖关键变量空间。标题与内容的落差构成 overclaiming。\n- 建议：标题加限定词如 \"...under ≤8B LoRA Fine-tuning\" 或 \"...at Small Scale\"。\n\n**N2** [critical] 14B convergence 结论的叙事权重与证据严重不匹配\n- 14B 结果在 abstract/introduction/conclusion 中均作为关键叙事元素，但仅 3 seeds、单家族、TOST df=2。论文标注 \"preliminary observation\" 但随后围绕它构建大量推论（capacity-dependent account、GenRM 桥接论述）。\n- 建议：(1) 14B 从 abstract 降级或移除；(2) conclusion 中标注 speculative direction 而非 supported finding。\n\n### Should-Fix\n\n**W1** [warning] 核心发现可预测性未被讨论\n- \"Complexity moderates formulation choice\" 方向直觉可预测：CWM 生成 ~477 tokens + exact match vs CLS 1 token，长输出更难生成不令人意外。论文量化了 gap（18-26pp）有价值，但没讨论结果是否 a priori 可预测、量化提供了什么 beyond confirmation 的 new insight。\n\n**W2** [warning] 实际应用价值有限\n- Simple routing <0.4pp；failure mode taxonomy 描述性但无 mitigation 方案（4 种 intervention 均失败）；实践建议本质上是 \"repo level 用 CLS\"——多数实践者凭直觉就能得出。\n\n**W3** [warning] Mutation-based 训练数据代表性不足\n- 全部使用合成 mutation operator，真实 repo-level bug 涉及多文件语义错误。mutation data 可能系统性偏向某些 formulation。\n\n**W4** [warning] Appendix 与正文比例失衡（~12 页 vs 8 页）\n- 1.5:1 的比例暗示重要分析被移到附录，或附录含冗余内容。\n\n### 小问题\n- CWM 术语可能混淆（与 RL world model 概念冲突）\n- Figure 2 caption \"predict accuracy\" 含糊\n- Table 1 脚注 \"Training configuration differs\" 应更显著\n- Abstract ~185 词合规，正文 8 页合规，匿名性无违反\n\n### 主要优势\n1. 统计方法论极为扎实（TOST + ROPE + clustered bootstrap + Holm + mixed-effects）\n2. 匹配实验设计控制了关键混淆变量\n3. References 覆盖全面（CodePRM, GenPRM, FunPRM, SWE-RM, CodeScaler, RepoExec, VeRPO, Aletheia 等）\n4. Failure mode taxonomy 有实践诊断价值\n5. 写作整体清晰\n\n---\n\n请逐条回应 Reviewer 2 的每个 Must-Fix、Should-Fix 和你认为值得讨论的小问题。"
  }
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-23T17:32:21.102967+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29468
}
```

</details>

---


### Tool call

_source line 1444 · 2026-05-23T17:32:21.153696+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff",
  "director_session_key": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法论审慎、统计框架丰富的系统性实证比较，但 TRAJ 训练数据量不对称构成根本性混淆变量，低统计功效限制了等价性声明的说服力，单基准/单语言的范围制约了结论的泛化性。\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3/5 |\n| Excitement | 3/5 |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n### Must-Fix\n\n**N1** [critical] TRAJ 比较的训练数据量混淆变量未得到充分控制\n- TRAJ ~400 variant-level samples vs CLS/CWM ~70K per-test samples，175× 差异。论文声称 \"inherent to the formulation\"，但无法分离 formulation effect 与 data effect。14B 收敛可能因更大模型从少量数据中学习更好，而非 formulation 本身收敛。Appendix O 的 CLS 下采样到 ~1K 仍是 TRAJ 的 2.5×。\n- 建议：重新定位为 \"formulation + data regime\" 联合比较，或更极端下采样实验。\n\n**N2** [critical] 统计功效不足以支撑等价性声明的可解释性\n- TOST 功效 ~0.3 → 70% 概率无法确认等价。CLS-CWM 等价通过检验（p=0.006）是强证据。但 CLS-TRAJ 未通过（p=0.075）在低功效下既不是等价也不是不等价的证据。Repo-level 2-3 seeds 功效更低。\n- 建议：增加 MDE 表格；对功效不足的比较声明 \"inconclusive\" 而非 \"not confirmed\"。\n\n### Should-Fix\n\n**W1** [warning] 单基准/单语言限制泛化性但叙事偏广\n- 全部仅 SWE-bench Verified（500 实例）+ Python + 合成 mutation。Conclusion 以一般命题呈现未加范围限定。\n\n**W2** [warning] CWM format collapse 的 \"inherent limitation\" 归因证据不够充分\n- Early checkpoint collapse 可能反映训练未收敛；14B 收敛暗示 format collapse 可能是容量不足的结果。未测试 output format 简化、分步生成等方案。\n- 建议：改为 \"limitation under current ≤8B LoRA training regime\"。\n\n**W3** [warning] Error complementarity 的实践价值呈现与证据不匹配\n- Oracle +5.20pp/+4.00pp，但 heuristic <0.4pp。Conclusion 仍将 routing 列为第一方向——过于乐观。\n\n**W4** [warning] ±2pp SESOI 选择缺少独立实践论证\n- SESOI 应基于实践意义（对 downstream repair rate 的影响），而非统计方便。论文未提供 downstream 影响分析。\n\n### 小问题\n- M1: Abstract 接近 200 词限制\n- M2: Table 1 TRAJ 配置差异脚注应更显眼\n- M3: Figure 2 y-axis 非零起点未在 caption 标注\n- M4: IRC 术语仅 Appendix 出现一次可考虑删除\n- M5: Limitations 中 future work 内容应分开\n\n### 主要优势\n1. 匹配实验设计（matched framework）\n2. 统计方法层次清晰（TOST primary + ROPE robustness + regression mechanism）\n3. 诚实的局限性披露\n4. 丰富附录提升可审查性\n5. Failure mode taxonomy 有实践价值\n\n---\n\n请逐条回应 Reviewer 1 的每个 Must-Fix、Should-Fix 和你认为值得讨论的小问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff",
    "director_session_key": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法论审慎、统计框架丰富的系统性实证比较，但 TRAJ 训练数据量不对称构成根本性混淆变量，低统计功效限制了等价性声明的说服力，单基准/单语言的范围制约了结论的泛化性。\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3/5 |\n| Excitement | 3/5 |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n### Must-Fix\n\n**N1** [critical] TRAJ 比较的训练数据量混淆变量未得到充分控制\n- TRAJ ~400 variant-level samples vs CLS/CWM ~70K per-test samples，175× 差异。论文声称 \"inherent to the formulation\"，但无法分离 formulation effect 与 data effect。14B 收敛可能因更大模型从少量数据中学习更好，而非 formulation 本身收敛。Appendix O 的 CLS 下采样到 ~1K 仍是 TRAJ 的 2.5×。\n- 建议：重新定位为 \"formulation + data regime\" 联合比较，或更极端下采样实验。\n\n**N2** [critical] 统计功效不足以支撑等价性声明的可解释性\n- TOST 功效 ~0.3 → 70% 概率无法确认等价。CLS-CWM 等价通过检验（p=0.006）是强证据。但 CLS-TRAJ 未通过（p=0.075）在低功效下既不是等价也不是不等价的证据。Repo-level 2-3 seeds 功效更低。\n- 建议：增加 MDE 表格；对功效不足的比较声明 \"inconclusive\" 而非 \"not confirmed\"。\n\n### Should-Fix\n\n**W1** [warning] 单基准/单语言限制泛化性但叙事偏广\n- 全部仅 SWE-bench Verified（500 实例）+ Python + 合成 mutation。Conclusion 以一般命题呈现未加范围限定。\n\n**W2** [warning] CWM format collapse 的 \"inherent limitation\" 归因证据不够充分\n- Early checkpoint collapse 可能反映训练未收敛；14B 收敛暗示 format collapse 可能是容量不足的结果。未测试 output format 简化、分步生成等方案。\n- 建议：改为 \"limitation under current ≤8B LoRA training regime\"。\n\n**W3** [warning] Error complementarity 的实践价值呈现与证据不匹配\n- Oracle +5.20pp/+4.00pp，但 heuristic <0.4pp。Conclusion 仍将 routing 列为第一方向——过于乐观。\n\n**W4** [warning] ±2pp SESOI 选择缺少独立实践论证\n- SESOI 应基于实践意义（对 downstream repair rate 的影响），而非统计方便。论文未提供 downstream 影响分析。\n\n### 小问题\n- M1: Abstract 接近 200 词限制\n- M2: Table 1 TRAJ 配置差异脚注应更显眼\n- M3: Figure 2 y-axis 非零起点未在 caption 标注\n- M4: IRC 术语仅 Appendix 出现一次可考虑删除\n- M5: Limitations 中 future work 内容应分开\n\n### 主要优势\n1. 匹配实验设计（matched framework）\n2. 统计方法层次清晰（TOST primary + ROPE robustness + regression mechanism）\n3. 诚实的局限性披露\n4. 丰富附录提升可审查性\n5. Failure mode taxonomy 有实践价值\n\n---\n\n请逐条回应 Reviewer 1 的每个 Must-Fix、Should-Fix 和你认为值得讨论的小问题。"
  }
}
```

</details>

---


### Tool result

_source line 1445 · 2026-05-23T17:32:22.515158+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 1446 · 2026-05-23T17:32:27.655399+00:00_

交叉分享已发送给两位 Reviewer，等待交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 129

## Round 129

2 recorded events


### User

_source line 1447 · 2026-05-23T17:32:30.194206+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断**：Overall 3.0/5（Findings 水平），Soundness 4/5，Excitement 2.5/5。

两个 Must-Fix：
1. 标题 "A Systematic Comparison" 承诺的通用性远超实际 ≤8B LoRA + Python mutation 的研究范围
2. 14B convergence 在 abstract/conclusion 中的叙事权重与其证据（3 seeds、单家族）严重不匹配

四个 Should-Fix：核心发现可预测性未讨论、实践价值有限（routing <0.4pp）、mutation 数据代表性不足、appendix 过度膨胀。

主要优势：统计方法论极为出色（TOST + Bayesian ROPE + mixed-effects regression）、匹配实验设计、references 覆盖非常全面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1448 · 2026-05-23T17:32:34.652440+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 130

## Round 130

2 recorded events


### User

_source line 1449 · 2026-05-23T17:33:34.095375+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE with nuance] R2-N1: 标题通用性 vs 实际范围**

R2 指出 "Systematic" 暗示覆盖关键变量空间，而实际限于 ≤8B LoRA + 2 families + Python。我同意标题与内容之间存在一定张力，但认为严重程度应降为 Should-Fix 而非 Must-Fix。理由：

1. "Systematic" 在方法论文献中更常指方法论的系统性（matched conditions, controlled variables, pre-registered statistical framework），而非变量空间的穷举。论文在实验设计上确实是 systematic 的——相同超参数、相同数据、相同 checkpoint 策略（§3.1, Appendix D/E）。
2. 然而 R2 的核心关切有道理：读者会期望 "systematic comparison" 至少覆盖 full fine-tuning vs LoRA、多语言、或更多模型家族。论文的 Limitations 提到了 "Python-only" 和 "scaling to 32B+"，但标题未加限定确实可能误导。
3. 建议的修改方向合理：在标题中加 "under ≤8B LoRA Fine-tuning" 或在 abstract 首句即明确范围限定，均可有效缓解。

**[AGREE] R2-N2: 14B convergence 叙事权重与证据不匹配**

完全同意。这与我在 R1 审稿中 N2 的关切一致。具体补充：

1. Abstract 中 "the gap narrows monotonically from 3.11pp (4B) to 1.07pp (14B)" 作为关键叙事，但 14B 仅 Qwen3 单家族、3 seeds、TOST df=2。在我指出的 TOST 功效 ~0.3 的背景下，df=2 的 14B 比较几乎没有统计区分力。
2. §3.6 的 "three directions follow" 第二条即 "scaling to 32B+ with more seeds"——这实际上承认了 14B 证据不足，但 abstract 和 conclusion 的叙事未反映这一不确定性。
3. Appendix K 的功效分析表明即使 function-level 5-seed 的功效也仅 ~0.3，3-seed 14B 的功效更低。论文在 14B 上构建的 "capacity-dependent convergence" 叙事（§3.3, §5）缺乏足够统计支撑。
4. 同意 R2 的建议：14B 从 abstract 降级，conclusion 中明确标注为 speculative/exploratory。

---

### Should-Fix

**[REBUT with qualification] R2-W1: 核心发现可预测性**

R2 认为 "complexity moderates formulation choice" 的方向直觉可预测。我部分不同意：

1. **方向可预测 ≠ 研究无价值。** 在 empirical science 中，量化一个直觉猜测的精确幅度、边界条件和失效模式是重要贡献。在本文之前，practitioner 知道 CWM 在长输出时"可能更难"，但不知道：(a) 具体 gap 是 18-26pp 而非 5pp 或 50pp；(b) function-level 二者是统计等价的而非 CLS 略优；(c) format collapse 是主要原因而非 semantic error。这些量化结果对 formulation 选择有直接指导意义。
2. **但 R2 有一个合理的 meta-point：** 论文确实没有讨论 "what was surprising vs expected"。增加一段 discussion 区分 "confirmation of intuition" vs "genuinely novel finding"（如 function-level 等价性、format collapse 而非 semantic accuracy 主导 repo-level gap）会加强论文的叙事。
3. 此外，论文的 failure mode taxonomy（Table 4）和 error complementarity analysis（§3.5）提供了超越 "CLS 更好" 直觉的结构性理解，这些并非 a priori 可预测。

**[AGREE with nuance] R2-W2: 实际应用价值有限**

部分同意。R2 指出 routing <0.4pp 且 4 种 intervention 均失败，这确实限制了即时实践价值。但我认为：

1. 论文的主要实践价值不在 routing，而在于为 formulation 选择提供 evidence-based guidance。目前 practitioner 凭直觉选择 formulation，本文提供了 "function-level 用哪个都行、repo-level 用 CLS" 的量化依据——这本身有价值，尽管直觉可能趋同。
2. 论文诚实报告了 routing heuristic 的失败（§3.5: "<0.4pp"），这是积极的 negative result，避免了后续研究走弯路。
3. 但 R2 的批评仍然成立：论文未能提供 actionable mitigation 方案。建议论文更明确地将 failure mode taxonomy 定位为 diagnostic tool 而非 solution pathway。

**[AGREE] R2-W3: Mutation-based 训练数据代表性**

同意。这与我在 R1 审稿中指出的 threats to validity 遗漏一致。补充：

1. 合成 mutation 使用 5 种 operator（gold/operator_swap/off_by_one/return_value/boundary_removal, Table 12），但真实 repo-level bug 涉及逻辑错误、API 误用、多文件交互等，这些远非简单 mutation 能覆盖。
2. Appendix G（Table 12）的 Val-Test mutation type 分布显示 operator_swap 在 val 和 test 集中占比差异显著（19.1% vs 34.3%），这本身就是 mutation-based data 的一个内部分布偏移问题。
3. 更关键的是：不同 formulation 可能对合成 mutation 有不同的敏感度。CLS 只需判断 pass/fail，对 mutation 类型可能更 robust；CWM 需要生成完整输出，如果合成 mutation 的输出模式较简单，CWM 在合成数据上的表现可能被高估。这个方向性的 confound 论文未讨论。

**[REBUT] R2-W4: Appendix 与正文比例失衡**

不同意这是一个问题。理由：

1. ACL ARR 对 appendix 无页数限制，reviewer guidelines 也未将 appendix 长度列为负面因素。论文正文 8 页（符合限制），appendix 提供了完整的 reproducibility 材料。
2. 论文的正文是自洽的——主要 claims 和证据均在正文中呈现。Appendix 提供的是 robustness checks（Bayesian ROPE, mixed-effects regression）、ablation details（LoRA rank, sequence length, majority voting）、qualitative analysis（error examples）和 hyperparameter tables。这些放在 appendix 是标准做法。
3. 实际上，这是本文的一个优势（我在 R1 审稿中将其列为主要优势之一）。相比之下，许多 NLP 论文缺少足够的 ablation 和 robustness check。~15 页 appendix 恰恰说明了论文的分析深度。
4. R2 的另一种解读（"重要分析被移到附录"）也不成立：正文包含了所有核心 statistical tests（TOST, bootstrap）、所有主要 Tables（1-4）和 Figures（1-3）。Bayesian ROPE 和 mixed-effects regression 明确定位为 robustness checks，放在 appendix 是正确的层次处理。

---

### 小问题

**[AGREE] CWM 术语混淆**：CWM（Code World Model）与 RL 领域的 World Model 概念确实有潜在混淆。但这是该领域既有文献的术语（FAIR CodeGen team 的 CWM evaluation protocol），论文遵循了 prior work 的命名。建议在 §2.1 首次出现时加一句简短说明以区分。

**[AGREE] Figure 2 caption**：与我在 R1 审稿中 M3 的发现一致。Figure 2 的 y-axis 从 ~58% 开始但 caption 未标注非零起点，而 Figure 3 的 caption 已包含 "y-axis does not start at zero" 的标注。应统一处理。

**[AGREE] Table 1 脚注显著性**：与我在 R1 审稿中 M2 的发现一致。TRAJ 的训练配置差异是理解结果的关键前提，仅在脚注中提及不够。

---

### 对 R2 Overall Assessment 的看法

R2 给出 3.0 (Findings)，主要基于 excitement 偏低（2.5/5）和实践价值有限。我给出 3.5 (Borderline Conference)。差异主要在于对 contribution type 的评价：

1. R2 的 soundness 评分（4/5）高于我的（3/5）。我认为 TRAJ 的 175× 数据量混淆变量是更严重的方法论问题（我的 R1-N1），这直接影响论文三分之一 comparisons 的有效性。如果 R2 充分考虑了这个 confound，soundness 可能应下调。
2. 但我同意 R2 对 excitement 的评价方向——这是一篇 confirmation-heavy 的实证研究，核心发现的方向确实直觉可预测。我的 excitement 评分（3/5）比 R2（2.5/5）略高，因为我认为 matched comparison 的缺失是一个真实的文献空白，填补它有独立价值。
3. 综合而言，如果作者修复 N1（TRAJ claim 重新定位）和 N2（14B 叙事降级），且 soundness 保持在 3+/5，这篇论文适合 Conference 或 strong Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1450 · 2026-05-23T17:33:41.506267+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 131

## Round 131

2 recorded events


### User

_source line 1451 · 2026-05-23T17:33:44.029626+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 所有 Must-Fix、Should-Fix 和小问题的逐条回应，并附上了对 R2 总体评分的分析意见。回应已发送给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1452 · 2026-05-23T17:33:50.886295+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 132

## Round 132

10 recorded events


### User

_source line 1453 · 2026-05-23T17:34:05.802329+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: TRAJ 训练数据量混淆变量**

同意这是一个重要问题。TRAJ ~400 variant-level samples vs CLS/CWM ~70K per-test samples 的 175× 差异确实构成混淆变量。

论文的辩护（§2.1："TRAJ serves as a granularity control"）有一定道理——在实际部署中，选择 TRAJ formulation 的人确实会面临同样的数据约束，因为 trajectory-level labeling 天然产生更少的样本。但 R1 正确指出，论文没有分离 "formulation effect" 和 "data regime effect"。

补充我自己的观察：Appendix O 的下采样实验（CLS 降至 ~1K）虽然有价值，但 ~1K 仍是 TRAJ 400 的 2.5×，且只做了一个配置。如果作者能展示 CLS 在 ~400 样本时的表现，将大大加强论证。此外，R1 关于 14B 收敛可能反映 "大模型从少量数据学习更好" 而非 "formulation 收敛" 的替代解释非常有力——这与我在 R2-N2 中对 14B 结果的 concern 一致。

**建议**：论文应至少做到以下之一：(a) 将比较重新定位为 "formulation-in-its-natural-data-regime" 的比较（并明确声明不是 controlled-data 比较）；(b) 增加 CLS 在 ~400 samples 的极端下采样实验作为 ablation。

---

**[AGREE] R1-N2: 统计功效不足以支撑等价性声明**

完全同意。我在自己的审稿中也标记了相关问题（R2-N2），但 R1 的表述更精准。

具体论据：
- CLS-CWM 等价：TOST p=0.006/0.007，Holm 校正后仍显著——这是 **强证据**，我没有异议。
- CLS-TRAJ "not confirmed"（p=0.075）：在 power ~0.3 的情况下，这个 p 值不能区分 "真的不等价" 和 "样本不足以检测等价"。论文使用 "not confirmed" 措辞比 "rejected" 好，但 R1 建议改为 "inconclusive" 更准确，因为 "not confirmed" 在英语学术语境中仍暗示有方向性判断。
- Repo-level 2-3 seeds：功效更低，我在 R2-N2 中已指出 14B 3 seeds 的 Bayesian ROPE 极弱。

R1 建议增加 Minimum Detectable Effect (MDE) 表格是好建议——这会帮助读者理解在当前样本量下，哪些 effect size 是可检测的。

---

### Should-Fix

**[AGREE] R1-W1: 单基准/单语言限制泛化性但叙事偏广**

完全同意，与我的 R2-N1（标题 scope mismatch）和 R2-W3（mutation data 代表性）高度重叠。

补充：论文 Conclusion §5 的措辞问题尤为突出。例如 "We presented the first systematic comparison of three execution-free verification formulations" 没有任何限定词——读者会理解为这是 general claim。实际上，这是 "the first systematic comparison under ≤8B LoRA fine-tuning on Python mutation data using SWE-bench Verified"。

R1 和我在这点上完全一致：结论的 scope 必须与实验的 scope 匹配。

---

**[AGREE] R1-W2: CWM format collapse 的 "inherent limitation" 归因需更审慎**

同意 R1 的分析。论文自身的 14B 数据实际上削弱了 "inherent limitation" 的论述：

- §3.3 报告 14B 时 CWM 的 gap 收窄到 1.07pp 以内
- §3.5 报告 "four interventions all fail to close the gap"——但这 4 个 intervention 全在 ≤8B 上测试
- Conclusion §5 也承认 "whether the repo-level divergence is formulation-inherent or capacity-contingent remains open"

这三者之间存在叙事张力：正文中 format collapse 被描述为 CWM 的结构性弱点（§2.2, §3.5），但论文自身的 14B 数据和 conclusion 的 hedging 暗示它可能只是容量不足的症状。

R1 的建议（改为 "limitation under current ≤8B LoRA training regime"）是对的，这也与我对标题 scope 的 concern 一致。

---

**[AGREE] R1-W3: Error complementarity 实践价值与叙事不匹配**

完全同意，与我的 R2-W2 一致。

补充数据：Oracle combination 达到 90.63%（function）和 95.83%（repo），显示理论上限有价值。但 <0.4pp 的 heuristic gain 意味着当前方法无法利用这种互补性。Conclusion §5 将 "complexity-aware routing" 列为第一个 future direction——这对于一个 <0.4pp 的结果来说确实偏乐观。

不过，我想补充一个 partial defense：互补性的存在本身（即使目前无法利用）确实为 future learned routers 提供了 motivation 和 upper bound。问题不在于提到它，而在于它在 contributions list（§1）中被列为第二大贡献——这个权重过大。

---

**[AGREE] R1-W4: ±2pp SESOI 选择缺少独立实践论证**

同意这是方法论上的一个弱点。SESOI（Smallest Effect Size of Interest）的选择应基于 downstream 实践意义——即 2pp 的 verification accuracy 差异对 downstream repair rate 意味着什么。

论文在 §3.4 和 Appendix J 提供了一些论证（sensitivity analysis at ±1.5pp 和 ±2.5pp），但没有 downstream 影响分析。在 code repair 场景中，如果 verification accuracy 差 2pp 但 repair@k 差 0.1pp，那么 ±2pp SESOI 可能过于宽松；反之如果差 5pp，则可能过于严格。

不过，我认为这个问题的严重程度低于 R1 的评估。±2pp 作为 SESOI 在 NLP 实验中是合理的 convention（类似于 Cohen's d=0.2 作为 "small effect" 的约定），且论文做了 sensitivity analysis。这是一个 "nice to have" 的改进，不是根本性缺陷。

---

### 小问题

**[REBUT] R1-M1: Abstract 接近 200 词限制**

我仔细统计了 abstract（abstract.tex），约 185 词，距离 200 词限制有 ~15 词余量。这不构成风险。EMNLP 2026 规则是 "abstract 不要超过 200 words"——185 词完全合规。

---

**[AGREE] R1-M2: Table 1 TRAJ 配置差异脚注应更显眼**

同意。我在自己的审稿中也标记了这个问题（R2 小问题第 4 条）。Table 1 脚注 "Training configuration differs (§3.5)" 包含对理解 repo-level 结果至关重要的信息，但太容易被忽略。

---

**[AGREE] R1-M3: Figure 2 y-axis 非零起点未在 caption 标注**

同意这是一个 visualization best practice 问题。非零起点在展示小差异时是合理的，但应在 caption 中注明 "Note: y-axis does not start at zero" 以避免视觉夸大。

---

**[AGREE] R1-M4 & M5**

M4（IRC 术语清理）和 M5（Limitations 中分离 future work）均为合理的写作改进建议。

---

### 总结

R1 和 R2 的审稿意见在核心判断上高度一致：

**共识区域**：
1. 统计方法论是论文最大优势
2. 标题/叙事的 scope 超出实际实验范围（R1-W1 ≈ R2-N1）
3. 14B 证据不足（R1-N2 部分重叠 R2-N2）
4. Error complementarity 实践价值有限（R1-W3 ≈ R2-W2）
5. Failure mode taxonomy 有实践价值

**R1 独特贡献**（我未充分覆盖的）：
- TRAJ 数据量混淆变量（R1-N1）——这是一个我忽略的重要 confound，值得升级为 critical issue
- SESOI 实践论证（R1-W4）——有道理但非致命
- MDE 表格建议——具体可操作的统计改进

**分歧区域**：
- **Overall 评分**：R1 给 3.5（Borderline Conference），我给 3.0（Findings）。R1 的 Excitement 3/5 高于我的 2.5/5。我认为 empirical comparison paper 在没有 new method 的情况下很难达到 main conference 标准——但 R1 可能更看重 matched experimental design 的方法论贡献。这个分歧是合理的 judgment call。
- **Soundness**：R1 给 3/5（主要因 TRAJ confound 和 power 不足），我给 4/5（认为论文在 hedging 上做得较好）。R1-N1 的 TRAJ 数据量论点确实削弱 soundness——我可能给高了。考虑到 R1 的 N1，我愿意将 soundness 修正为 3.5/5。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1454 · 2026-05-23T17:34:47.137660+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-23T17:34:47.288990+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T17:22:06.691449+00:00\", \"completed_at\": \"2026-05-23T17:25:39.829717+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续两页纯文本（Abstract + Introduction），无任何 display item。第一个视觉锚点 Figure 1 出现在第 3 页。审稿人前 2 分钟只看到文字墙，可能影响第一印象。建议考虑将 Figure 1 提前或在 page 2 加入一个高层概览图/表\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title / Author / Abstract 排版整洁，双栏布局规范，\\\"Anonymous ACL submission\\\" 标注正确。首页视觉上干净专业\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（三面板验证公式对比图）作为首个 display item，信息传达清晰——仅看图+caption 即可理解 CLS/CWM/TRAJ 三种 formulation 的核心差异。颜色使用绿/蓝/黄，色盲区分度可接受。Caption 自包含\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"三个 display items（Table 1 + Figure 2 + Table 2）挤压在同一页，视觉密度偏高。Figure 2 被夹在两个表格之间，空间局促。建议将 Table 2 移至下一页以改善呼吸感\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2（scaling gap 图）: 折线图带阴影区域传达 CLS-CWM gap 的缩小趋势。单栏宽度下 axis label 和 legend 字号偏小（约正文 65-70%），但仍可辨读。y 轴刻度标注清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1: booktabs 风格，最优结果加粗标注，精度统一（小数点后两位）。格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 3: booktabs 风格，多模型对比清晰。列数适中（≤8），单栏宽度合理\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 4（failure mode taxonomy）: 结构清晰，列宽合理。Section \\\"4 Related Work\\\" 标题后有 3+ 行正文在同页，无孤悬\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"最后一页主文内容（Related Work 尾部 + Conclusion + Limitations）页面利用率 ~95%，空间利用充分。Limitations 为简短一段，符合 EMNLP 2026 要求\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"References 共 3 页，格式统一，无可见 [?] 未解析引用，无明显 overfull box。作者名缩写、年份格式一致\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Appendix 起始页含 Table 5 + Figure 3（bar chart），display item 分布合理。Figure 3 蓝色柱状图清晰可读\"}, {\"se
…[truncated 1429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1456 · 2026-05-23T17:34:47.339784+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 1457 · 2026-05-23T17:34:47.340291+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1458 · 2026-05-23T17:43:39.694179+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N2 re-raises. R2 REBUT 指出 R1 混淆两个统计模型。Director：resolved 维持。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W2 re-raises low power (~0.3, n_eff≈86). R2 AGREE 但补充论文已用 TOST+Bayesian ROPE+14B scaling 三重互补验证。Resolved 维持。\"\n    - round: 16\n      reviewers: [1]\n      note: \"Fresh review R16. R1-N2 re-raises：2-3 seeds 无法支撑 18-26pp gap 的 formulation 归因。R2 隐含 AGREE（N2 scope 限制）。论文 §3.5 'exploratory' 标注仍在。\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13-R16 反复提及但无新增要求。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。R2 REBUT。Director 降为 Should-Fix。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N2 升级为 critical。R2 完全 AGREE。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1-W4 re-raises。R2 AGREE。Director resolved 维持。\"\n    - round: 14\n      reviewers: [2]\n      note: \"R2-W1 re-raises s42 vs s123/s456 配置异质性。R1 AGREE。Director resolved 维持。\"\n    - round: 15\n      reviewers: [1]\n      note: \"R1-W7 re-raises CWM checkpoint ablation 范围。R2 REBUT。Director resolved 维持。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy\"\n      assigned_to: \"experiment\"\n      status: wont_fix\n  resolution: \"Step 300-400 checkpoints 未保存，但已找到现有 step-400 eval 数据（s42: 64.36%, 63.7% unparseable）。Format collapse 从训练早期即存在。\"\n  resolution_round: 12\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 17\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"两人共识：Findings 合适，Main 不够。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 Excitement 2/5, R1 Excitement 3/5。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 3/5。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Fresh review R16. R1 Excitement 3/5, R2 Excitement 3/5。核心发现可预测性限制新颖性。wont_fix 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"Fresh review R17. R1 Excitement 3/5, R2 Excitement 2.5/5。R2 明确判定 Findings 而非 main conference。wont_fix 维持。\"\n  resolution: \"Excitement 稳定在 2.5-3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 17\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：无 pre-registration。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W1 标 Must-Fix。R2 AGREE 部分。共识：Table 13 应移入正文。Resolved 维持。\"\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W1 re-raises：缺乏正式论证。但论文已诚实披露 post-hoc 状态并提供 sensitivity analysis。Resolved 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W4 re-raises：SESOI 应基于 downstream 实践意义（repair@K 影响），论文未提供此分析。R2 AGREE with nuance——±2pp 是合理 convention 但增加实践论证更好。Resolved 维持。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；Bayesian ROPE 提供独立佐证。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入限定。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Fresh review R16. R2-N2 re-raises：标题仍暗示通用性。R1 AGREE 但程度略轻。Abstract 已有限定词但标题无。建议标题加 scope 限定。\"\n  resolution: \"Abstract + Conclusion 均已加入 ≤8B LoRA 限定。标题是否需要修改由 Research Director 决定。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 17\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"downsample 控制了 volume 但未控制 label granularity。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Director 裁定 Should-Fix（降级）。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Abstract 已有 'the TRAJ comparison is inherently confounded'。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W1 re-raises TRAJ 与 CLS/CWM 比较性质不同。R1 AGREE：应视觉区分 controlled vs observational comparison。Resolved 维持——Abstract 和 §3.5 均有 confound 标注。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N1 升级为 Must-Fix。175× data volume asymmetry 构成根本性混淆——论文无法分离 formulation effect vs data regime effect。Appendix O 下采样到 ~1K 仍是 TRAJ 的 2.5×。R2 完全 AGREE 并补充 14B 收敛可能反映大模型从少量数据学习更好。Resolved 维持——Abstract 和 §3.5 已有 confound 标注。\"\n  resolution: \"§3.5 标注 exploratory + confound 讨论。Abstract 已有 'inherently confounded'。\"\n  resolution_round: 12\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W5 re-raises：synthetic mutation vs real developer patch 分布差异。Limitations 已提及但讨论不深。Resolved 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W3 re-raises。单基准(SWE-bench)/单语言(Python)/合成 mutation 限制泛化性。R1 补充：mutation data 可能系统性偏向特定 formulation——CLS 对 mutation 类型更 robust，CWM 在合成 mutation 简单输出上表现可能被高估。此方向性 confound 论文未讨论。Resolved 维持——Limitations 已提及。\"\n  resolution: \"Appendix Extended Validity Discussion 讨论充分。Limitations 已提及 Python-only 和 codegen 限制。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"~185 词，合规。\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"CodeRM, CodeScaler, GenPRM 等均已加入 Related Work。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  resolution: \"Figure 2 caption 标注 'y-axis does not start at zero'。\"\n  resolution_round: 11\n\n# === Round 8 Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 17\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Both RESOLVED.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 re-raises.\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W2 标 Must-Fix。R2 AGREE 但补充 Bayesian ROPE 不受 power 限制。Resolved 维持。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R1-N1 标 Critical：CLS-TRAJ power ~0.3 使该比较 uninformative，Abstract 'not confirmed' 可能 mislead。R2-W1 AGREE。论文 §3.4 已有 power paragraph + 'at current power (~0.3)' 限定。Resolved 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N2 升级为 Must-Fix。power ~0.3 使 CLS-TRAJ 比较 inconclusive（非 directional evidence）。R2 完全 AGREE 并建议 'not confirmed' 改为 'inconclusive'。建议增加 MDE 表格。Repo-level 2-3 seeds 功效更低。Resolved 维持——§3.4 已有 power paragraph。\"\n  resolution: \"§3.4 已扩写 power paragraph，14B TOST 完成。Abstract 已加 'at current power (~0.3)' 限定。\"\n  resolution_round: 12\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Cross-seed oracle 已加入正文。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Appendix 已讨论。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM / RepoExec\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Director 裁定 Should-Fix（降级）。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-N2 标 Must-Fix。R1 REBUT matched design 方法论价值。Resolved 维持。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N2 re-raises scope limitation。R1 AGREE 标题应加限定。Resolved 维持——所有 qualifier 已到位。\"\n  resolution: \"Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 13\n  resolution: \"合并至 R6-N4。Inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W6 re-raises LPM vs GEE 不一致（model identity p=0.002 vs p=0.449）。论文 Appendix M 已有 estimator-dependent 标注和 cluster 数限制讨论。Resolved 维持。\"\n  resolution: \"Appendix M 补充 GEE logistic regression + estimator-dependent 标注。\"\n  resolution_round: 11\n\n# === Round 9-12 Issues (all resolved, abbreviated) ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大 gap。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却声称 'model-dependent'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W3 re-raises DeepSeek 仅 2 seeds，跨模型比较可信度降低。Resolved 维持——§3.4 已有 caveat。\"\n  resolution: \"Abstract 改为更审慎措辞。\"\n  resolution_round: 10\n\n- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。\"\n  resolution_round: 12\n\n- id: \"R12-N3\"\n  summary: \"CLS-TRAJ 等价性不对称结论可能是 power ~0.3 artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"§3.4 power paragraph 扩写，14B TOST 完成。\"\n  resolution_round: 12\n\n- id: \"R12-W2\"\n  summary: \"GenRM 对比发现未充分讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 re-raises：跨领域 code vs math GenRM 比较分析浅薄。R1 AGREE 但认为超出本文 scope。Resolved 维持——Conclusion 已有 GenRM 段落。\"\n  resolution: \"Conclusion 新增 GenRM domain-specificity 段落。\"\n  resolution_round: 12\n\n- id: \"R13-N1\"\n  summary: \"Appendix 'P: Limitations' 标题可能违反 EMNLP 格式规则\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Appendix P 重命名为 'Extended validity discussion'。\"\n  resolution_round: 13\n\n- id: \"R13-W1\"\n  summary: \"Abstract/Conclusion 中 TRAJ 'not confirmed' 措辞在 power ~0.3 下 over-stated\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Abstract 加入 'at current power (~0.3)' 限定语。\"\n  resolution_round: 13\n\n- id: \"R13-W2\"\n  summary: \"Oracle 互补性应重新框定为 negative result + motivation，而非独立正面贡献\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W2 re-raises：error complementarity 被高估。R1 AGREE 应降级为 exploratory finding。论文 §1 Contribution 2 已重写为 negative result framing。Resolved 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2-W2 re-raises。Oracle gap 大但 heuristic <0.4pp，Conclusion routing 方向过于乐观。§1 Contribution 2 权重过大。R2 补充：互补性存在有价值但不应列为主要贡献。Resolved 维持。\"\n  resolution: \"Introduction Contribution 2 重写为 negative result framing。\"\n  resolution_round: 13\n\n- id: \"R13-W3\"\n  summary: \"14B 'capacity-dependent convergence' claim 证据不足——仅 1 model family, 3 seeds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W6 re-raises：Abstract 中 capacity-dependent convergence 措辞过强。R1 完全 AGREE。Resolved 维持——Abstract 已有 'preliminary observation' 限定。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-N2 升级为 Must-Fix。14B 在 abstract/introduction/conclusion 的叙事权重与 3 seeds/单家族/TOST df=2 的证据严重不匹配。R1 完全 AGREE——在 power ~0.3 下 df=2 几乎无统计区分力。建议 14B 从 abstract 降级或移除。Resolved 维持——'preliminary observation' 限定已存在。\"\n  resolution: \"Abstract 和 Conclusion 已有 'preliminary observation' + 'single family' 限定。\"\n  resolution_round: 13\n\n- id: \"R13-W4\"\n  summary: \"GenRM 领域特异性对比分析不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 re-raises。R1 AGREE 但认为超出 scope。Resolved 维持。\"\n  resolution: \"Conclusion 扩展 GenRM 对比。\"\n  resolution_round: 13\n\n# === Round 16 New Issues ===\n\n- id: \"R16-N1\"\n  summary: \"Complexity-dependent 核心叙事存在 complexity 与 output format/length 的未解耦混淆\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 完全 AGREE。论文将 function→repo 分歧归因于 'code complexity'，但 format collapse（53-74% unparseable）更直接指向 output format/length 效应。四种 intervention 均未攻击 output length 本身（如 constrained decoding）。核心 narrative 框架需修正。两位 Reviewer 共识。\"\n  action_items:\n    - round: 16\n      action: \"Introduction 核心 claim 增加 mechanistic pathway：'formulation choice is moderated by code complexity, operating through output format'，明确 function ~5-15 tokens vs repo ~477 tokens 的 output length 差异是直接机制\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Introduction §1 核心 claim 增加 mechanistic pathway 解释：'formulation choice is moderated by code complexity, operating through output format: function-level outputs average ~5-15 tokens (minimizing generation-specific failures), while repo-level outputs average ~477 tokens (triggering format collapse)'。保留 'Complexity-moderated' 贡献标题但补充 output format 作为直接机制。\"\n  resolution_round: 16\n\n- id: \"R16-N2\"\n  summary: \"≤8B LoRA 范围限制下标题和 abstract 泛化声明过广\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N2 提出，R1 AGREE。标题 'A Systematic Comparison...' 暗示通用性，但实际仅覆盖 2 families × ≤8B × LoRA。Abstract 已有 '≤8B LoRA fine-tuning' 限定，但标题无。14B convergence 仅 3 seeds × 1 family，Figure 2 仅 3 个 scale points（df=0），不足以支撑 abstract-level scaling claim。两位 Reviewer 建议标题加 scope 限定。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-N1 re-raises。R1 AGREE with nuance——'systematic' 可指方法论系统性而非穷举性，建议降为 Should-Fix。但双方均同意标题或 abstract 应加范围限定。wont_fix 维持。\"\n  action_items:\n    - round: 16\n      action: \"标题加 scope 限定（如 'under Parameter-Efficient Fine-Tuning' 或 'for Small Language Models'）；降低 14B convergence 在 abstract 中的 prominence\"\n      assigned_to: \"paper\"\n      status: wont_fix\n  resolution: \"Rebuttal material。Abstract 已有 '≤8B LoRA fine-tuning' + 'preliminary observation' 限定。标题修改风险过高（DDL 前 2 天），且 'Systematic Comparison' 描述研究类型而非 scope 声明。14B convergence 已有 'single family, 3 seeds' 限定。\"\n  resolution_round: 16\n\n- id: \"R16-W1\"\n  summary: \"统计方法多样但主次层次不清\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 AGREE。TOST/Bayesian ROPE/clustered bootstrap/mixed-effects LPM/GEE/ICC 多种框架但未声明 primary vs robustness check。当不同方法结论不一致时（如 LPM vs GEE 对 model identity），读者无法判断应采信哪个。\"\n  action_items:\n    - round: 16\n      action: \"在 §3.1 Statistics 段落增加统计层次声明\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.1 Statistics 段落增加：'TOST equivalence testing is our primary inferential framework for function-level claims; clustered bootstrap provides confidence intervals, Bayesian ROPE serves as a robustness check, and mixed-effects regression tests the formulation×complexity interaction.'\"\n  resolution_round: 16\n\n- id: \"R16-W2\"\n  summary: \"CWM format collapse 的定性归因不清：inherent formulation limitation vs engineering artifact\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W4 提出。53-74% unparseable + default to majority class。四种 interventions 失败但未测试 constrained decoding。如果 format collapse 是 engineering artifact 可通过 constrained decoding 缓解，则 18-26pp gap 不应被解释为 'formulation difference'。与 R16-N1 关联。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W2 re-raises。14B gap 收窄到 1.07pp 与 'inherent limitation' 归因存在叙事张力——4 种 intervention 全在 ≤8B 上测试。R2 AGREE：应改为 'limitation under current ≤8B LoRA training regime'。Resolved 维持。\"\n  action_items:\n    - round: 16\n      action: \"Limitations 已有 constrained decoding 讨论；N1 mechanistic pathway 修复间接回应了归因问题\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Limitations §8 已有 'Format-specific interventions (constrained decoding, output-format pretraining) may mitigate CWM format collapse but were not evaluated'。N1 mechanistic pathway 修复将叙事从 'complexity causes gap' 修正为 'complexity operates through output format'，间接回应了 engineering vs inherent 的归因问题。Rebuttal 可进一步展开。\"\n  resolution_round: 16\n\n- id: \"R16-M1\"\n  summary: \"'pp' 缩写首次使用未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"Section 1 直接使用 'pp' 未括号解释。\"\n  action_items:\n    - round: 16\n      action: \"首次使用时改为 'percentage points (pp)'\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Introduction §1 首次出现 '35-36 pp' 处改为 '35-36 percentage points (pp)'。\"\n  resolution_round: 16\n\n- id: \"R16-M2\"\n  summary: \"DeepSeek-Coder 2 seeds 的 CI/std 在 Table 1 中未报告\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"Table 1 中 DeepSeek 行仅有均值，'2 seeds' 注释在 caption 中容易被忽略。\"\n  action_items:\n    - round: 16\n      action: \"Table 1 caption 已改为 'Mean ± std over 5 seeds (Qwen3) or 2 seeds (DeepSeek)'\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Table 1 caption 已在 R16 修复中改为显式注明 seed 数量。表格内加标注会增加视觉复杂度。\"\n  resolution_round: 16\n\n- id: \"R16-M3\"\n  summary: \"Figure 1 字体偏小，接近可读性下限\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"Figure 1 内部文字约为正文字号的 60-65%，打印时可能不够清晰。\"\n  resolution: \"Figure 重新生成风险高（DDL 前 2 天）。当前字体大小在 ACL 论文中属正常范围。Rebuttal 可提供高清版本。\"\n  resolution_round: 16\n\n# === Round 17 New Issues ===\n\n- id: \"R17-W1\"\n  summary: \"核心发现可预测性未被讨论——complexity moderates formulation choice 方向直觉可预期\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R2-W1 提出：CWM 生成 ~477 tokens + exact match vs CLS 1 token，长输出更难不令人意外。论文量化了 gap (18-26pp) 有价值但未讨论结果是否 a priori 可预测。R1 partial REBUT：方向可预测≠研究无价值，但同意应增加讨论区分 confirmation vs genuinely novel finding。\"\n  action_items:\n    - round: 17\n      action: \"在 §3.5 或 §5 增加一段讨论，承认核心发现方向的可预测性，并强调量化精度（18-26pp）、function-level 等价性、format collapse 机制等增量价值\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N2 re-raises. R2 REBUT 指出 R1 混淆两个统计模型。Director：resolved 维持。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W2 re-raises low power (~0.3, n_eff≈86). R2 AGREE 但补充论文已用 TOST+Bayesian ROPE+14B scaling 三重互补验证。Resolved 维持。\"\n    - round: 16\n      reviewers: [1]\n      note: \"Fresh review R16. R1-N2 re-raises：2-3 seeds 无法支撑 18-26pp gap 的 formulation 归因。R2 隐含 AGREE（N2 scope 限制）。论文 §3.5 'exploratory' 标注仍在。\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13-R16 反复提及但无新增要求。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。R2 REBUT。Director 降为 Should-Fix。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N2 升级为 critical。R2 完全 AGREE。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1-W4 re-raises。R2 AGREE。Director resolved 维持。\"\n    - round: 14\n      reviewers: [2]\n      note: \"R2-W1 re-raises s42 vs s123/s456 配置异质性。R1 AGREE。Director resolved 维持。\"\n    - round: 15\n      reviewers: [1]\n      note: \"R1-W7 re-raises CWM checkpoint ablation 范围。R2 REBUT。Director resolved 维持。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy\"\n      assigned_to: \"experiment\"\n      status: wont_fix\n  resolution: \"Step 300-400 checkpoints 未保存，但已找到现有 step-400 eval 数据（s42: 64.36%, 63.7% unparseable）。Format collapse 从训练早期即存在。\"\n  resolution_round: 12\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 17\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"两人共识：Findings 合适，Main 不够。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 Excitement 2/5, R1 Excitement 3/5。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 3/5。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Fresh review R16. R1 Excitement 3/5, R2 Excitement 3/5。核心发现可预测性限制新颖性。wont_fix 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"Fresh review R17. R1 Excitement 3/5, R2 Excitement 2.5/5。R2 明确判定 Findings 而非 main conference。wont_fix 维持。\"\n  resolution: \"Excitement 稳定在 2.5-3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 17\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：无 pre-registration。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W1 标 Must-Fix。R2 AGREE 部分。共识：Table 13 应移入正文。Resolved 维持。\"\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W1 re-raises：缺乏正式论证。但论文已诚实披露 post-hoc 状态并提供 sensitivity analysis。Resolved 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W4 re-raises：SESOI 应基于 downstream 实践意义（repair@K 影响），论文未提供此分析。R2 AGREE with nuance——±2pp 是合理 convention 但增加实践论证更好。Resolved 维持。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；Bayesian ROPE 提供独立佐证。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 16\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入限定。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Fresh review R16. R2-N2 re-raises：标题仍暗示通用性。R1 AGREE 但程度略轻。Abstract 已有限定词但标题无。建议标题加 scope 限定。\"\n  resolution: \"Abstract + Conclusion 均已加入 ≤8B LoRA 限定。标题是否需要修改由 Research Director 决定。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 17\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"downsample 控制了 volume 但未控制 label granularity。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Director 裁定 Should-Fix（降级）。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Abstract 已有 'the TRAJ comparison is inherently confounded'。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W1 re-raises TRAJ 与 CLS/CWM 比较性质不同。R1 AGREE：应视觉区分 controlled vs observational comparison。Resolved 维持——Abstract 和 §3.5 均有 confound 标注。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N1 升级为 Must-Fix。175× data volume asymmetry 构成根本性混淆——论文无法分离 formulation effect vs data regime effect。Appendix O 下采样到 ~1K 仍是 TRAJ 的 2.5×。R2 完全 AGREE 并补充 14B 收敛可能反映大模型从少量数据学习更好。Resolved 维持——Abstract 和 §3.5 已有 confound 标注。\"\n  resolution: \"§3.5 标注 exploratory + confound 讨论。Abstract 已有 'inherently confounded'。\"\n  resolution_round: 12\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W5 re-raises：synthetic mutation vs real developer patch 分布差异。Limitations 已提及但讨论不深。Resolved 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W3 re-raises。单基准(SWE-bench)/单语言(Python)/合成 mutation 限制泛化性。R1 补充：mutation data 可能系统性偏向特定 formulation——CLS 对 mutation 类型更 robust，CWM 在合成 mutation 简单输出上表现可能被高估。此方向性 confound 论文未讨论。Resolved 维持——Limitations 已提及。\"\n  resolution: \"Appendix Extended Validity Discussion 讨论充分。Limitations 已提及 Python-only 和 codegen 限制。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"~185 词，合规。\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"CodeRM, CodeScaler, GenPRM 等均已加入 Related Work。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  resolution: \"Figure 2 caption 标注 'y-axis does not start at zero'。\"\n  resolution_round: 11\n\n# === Round 8 Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 17\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Both RESOLVED.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 re-raises.\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W2 标 Must-Fix。R2 AGREE 但补充 Bayesian ROPE 不受 power 限制。Resolved 维持。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R1-N1 标 Critical：CLS-TRAJ power ~0.3 使该比较 uninformative，Abstract 'not confirmed' 可能 mislead。R2-W1 AGREE。论文 §3.4 已有 power paragraph + 'at current power (~0.3)' 限定。Resolved 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N2 升级为 Must-Fix。power ~0.3 使 CLS-TRAJ 比较 inconclusive（非 directional evidence）。R2 完全 AGREE 并建议 'not confirmed' 改为 'inconclusive'。建议增加 MDE 表格。Repo-level 2-3 seeds 功效更低。Resolved 维持——§3.4 已有 power paragraph。\"\n  resolution: \"§3.4 已扩写 power paragraph，14B TOST 完成。Abstract 已加 'at current power (~0.3)' 限定。\"\n  resolution_round: 12\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Cross-seed oracle 已加入正文。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Appendix 已讨论。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM / RepoExec\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Director 裁定 Should-Fix（降级）。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-N2 标 Must-Fix。R1 REBUT matched design 方法论价值。Resolved 维持。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N2 re-raises scope limitation。R1 AGREE 标题应加限定。Resolved 维持——所有 qualifier 已到位。\"\n  resolution: \"Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 13\n  resolution: \"合并至 R6-N4。Inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W6 re-raises LPM vs GEE 不一致（model identity p=0.002 vs p=0.449）。论文 Appendix M 已有 estimator-dependent 标注和 cluster 数限制讨论。Resolved 维持。\"\n  resolution: \"Appendix M 补充 GEE logistic regression + estimator-dependent 标注。\"\n  resolution_round: 11\n\n# === Round 9-12 Issues (all resolved, abbreviated) ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大 gap。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却声称 'model-dependent'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W3 re-raises DeepSeek 仅 2 seeds，跨模型比较可信度降低。Resolved 维持——§3.4 已有 caveat。\"\n  resolution: \"Abstract 改为更审慎措辞。\"\n  resolution_round: 10\n\n- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。\"\n  resolution_round: 12\n\n- id: \"R12-N3\"\n  summary: \"CLS-TRAJ 等价性不对称结论可能是 power ~0.3 artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"§3.4 power paragraph 扩写，14B TOST 完成。\"\n  resolution_round: 12\n\n- id: \"R12-W2\"\n  summary: \"GenRM 对比发现未充分讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 re-raises：跨领域 code vs math GenRM 比较分析浅薄。R1 AGREE 但认为超出本文 scope。Resolved 维持——Conclusion 已有 GenRM 段落。\"\n  resolution: \"Conclusion 新增 GenRM domain-specificity 段落。\"\n  resolution_round: 12\n\n- id: \"R13-N1\"\n  summary: \"Appendix 'P: Limitations' 标题可能违反 EMNLP 格式规则\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Appendix P 重命名为 'Extended validity discussion'。\"\n  resolution_round: 13\n\n- id: \"R13-W1\"\n  summary: \"Abstract/Conclusion 中 TRAJ 'not confirmed' 措辞在 power ~0.3 下 over-stated\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Abstract 加入 'at current power (~0.3)' 限定语。\"\n  resolution_round: 13\n\n- id: \"R13-W2\"\n  summary: \"Oracle 互补性应重新框定为 negative result + motivation，而非独立正面贡献\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W2 re-raises：error complementarity 被高估。R1 AGREE 应降级为 exploratory finding。论文 §1 Contribution 2 已重写为 negative result framing。Resolved 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2-W2 re-raises。Oracle gap 大但 heuristic <0.4pp，Conclusion routing 方向过于乐观。§1 Contribution 2 权重过大。R2 补充：互补性存在有价值但不应列为主要贡献。Resolved 维持。\"\n  resolution: \"Introduction Contribution 2 重写为 negative result framing。\"\n  resolution_round: 13\n\n- id: \"R13-W3\"\n  summary: \"14B 'capacity-dependent convergence' claim 证据不足——仅 1 model family, 3 seeds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W6 re-raises：Abstract 中 capacity-dependent convergence 措辞过强。R1 完全 AGREE。Resolved 维持——Abstract 已有 'preliminary observation' 限定。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-N2 升级为 Must-Fix。14B 在 abstract/introduction/conclusion 的叙事权重与 3 seeds/单家族/TOST df=2 的证据严重不匹配。R1 完全 AGREE——在 power ~0.3 下 df=2 几乎无统计区分力。建议 14B 从 abstract 降级或移除。Resolved 维持——'preliminary observation' 限定已存在。\"\n  resolution: \"Abstract 和 Conclusion 已有 'preliminary observation' + 'single family' 限定。\"\n  resolution_round: 13\n\n- id: \"R13-W4\"\n  summary: \"GenRM 领域特异性对比分析不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 re-raises。R1 AGREE 但认为超出 scope。Resolved 维持。\"\n  resolution: \"Conclusion 扩展 GenRM 对比。\"\n  resolution_round: 13\n\n# === Round 16 New Issues ===\n\n- id: \"R16-N1\"\n  summary: \"Complexity-dependent 核心叙事存在 complexity 与 output format/length 的未解耦混淆\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 完全 AGREE。论文将 function→repo 分歧归因于 'code complexity'，但 format collapse（53-74% unparseable）更直接指向 output format/length 效应。四种 intervention 均未攻击 output length 本身（如 constrained decoding）。核心 narrative 框架需修正。两位 Reviewer 共识。\"\n  action_items:\n    - round: 16\n      action: \"Introduction 核心 claim 增加 mechanistic pathway：'formulation choice is moderated by code complexity, operating through output format'，明确 function ~5-15 tokens vs repo ~477 tokens 的 output length 差异是直接机制\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Introduction §1 核心 claim 增加 mechanistic pathway 解释：'formulation choice is moderated by code complexity, operating through output format: function-level outputs average ~5-15 tokens (minimizing generation-specific failures), while repo-level outputs average ~477 tokens (triggering format collapse)'。保留 'Complexity-moderated' 贡献标题但补充 output format 作为直接机制。\"\n  resolution_round: 16\n\n- id: \"R16-N2\"\n  summary: \"≤8B LoRA 范围限制下标题和 abstract 泛化声明过广\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N2 提出，R1 AGREE。标题 'A Systematic Comparison...' 暗示通用性，但实际仅覆盖 2 families × ≤8B × LoRA。Abstract 已有 '≤8B LoRA fine-tuning' 限定，但标题无。14B convergence 仅 3 seeds × 1 family，Figure 2 仅 3 个 scale points（df=0），不足以支撑 abstract-level scaling claim。两位 Reviewer 建议标题加 scope 限定。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-N1 re-raises。R1 AGREE with nuance——'systematic' 可指方法论系统性而非穷举性，建议降为 Should-Fix。但双方均同意标题或 abstract 应加范围限定。wont_fix 维持。\"\n  action_items:\n    - round: 16\n      action: \"标题加 scope 限定（如 'under Parameter-Efficient Fine-Tuning' 或 'for Small Language Models'）；降低 14B convergence 在 abstract 中的 prominence\"\n      assigned_to: \"paper\"\n      status: wont_fix\n  resolution: \"Rebuttal material。Abstract 已有 '≤8B LoRA fine-tuning' + 'preliminary observation' 限定。标题修改风险过高（DDL 前 2 天），且 'Systematic Comparison' 描述研究类型而非 scope 声明。14B convergence 已有 'single family, 3 seeds' 限定。\"\n  resolution_round: 16\n\n- id: \"R16-W1\"\n  summary: \"统计方法多样但主次层次不清\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 AGREE。TOST/Bayesian ROPE/clustered bootstrap/mixed-effects LPM/GEE/ICC 多种框架但未声明 primary vs robustness check。当不同方法结论不一致时（如 LPM vs GEE 对 model identity），读者无法判断应采信哪个。\"\n  action_items:\n    - round: 16\n      action: \"在 §3.1 Statistics 段落增加统计层次声明\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.1 Statistics 段落增加：'TOST equivalence testing is our primary inferential framework for function-level claims; clustered bootstrap provides confidence intervals, Bayesian ROPE serves as a robustness check, and mixed-effects regression tests the formulation×complexity interaction.'\"\n  resolution_round: 16\n\n- id: \"R16-W2\"\n  summary: \"CWM format collapse 的定性归因不清：inherent formulation limitation vs engineering artifact\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W4 提出。53-74% unparseable + default to majority class。四种 interventions 失败但未测试 constrained decoding。如果 format collapse 是 engineering artifact 可通过 constrained decoding 缓解，则 18-26pp gap 不应被解释为 'formulation difference'。与 R16-N1 关联。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W2 re-raises。14B gap 收窄到 1.07pp 与 'inherent limitation' 归因存在叙事张力——4 种 intervention 全在 ≤8B 上测试。R2 AGREE：应改为 'limitation under current ≤8B LoRA training regime'。Resolved 维持。\"\n  action_items:\n    - round: 16\n      action: \"Limitations 已有 constrained decoding 讨论；N1 mechanistic pathway 修复间接回应了归因问题\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Limitations §8 已有 'Format-specific interventions (constrained decoding, output-format pretraining) may mitigate CWM format collapse but were not evaluated'。N1 mechanistic pathway 修复将叙事从 'complexity causes gap' 修正为 'complexity operates through output format'，间接回应了 engineering vs inherent 的归因问题。Rebuttal 可进一步展开。\"\n  resolution_round: 16\n\n- id: \"R16-M1\"\n  summary: \"'pp' 缩写首次使用未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"Section 1 直接使用 'pp' 未括号解释。\"\n  action_items:\n    - round: 16\n      action: \"首次使用时改为 'percentage points (pp)'\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Introduction §1 首次出现 '35-36 pp' 处改为 '35-36 percentage points (pp)'。\"\n  resolution_round: 16\n\n- id: \"R16-M2\"\n  summary: \"DeepSeek-Coder 2 seeds 的 CI/std 在 Table 1 中未报告\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"Table 1 中 DeepSeek 行仅有均值，'2 seeds' 注释在 caption 中容易被忽略。\"\n  action_items:\n    - round: 16\n      action: \"Table 1 caption 已改为 'Mean ± std over 5 seeds (Qwen3) or 2 seeds (DeepSeek)'\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Table 1 caption 已在 R16 修复中改为显式注明 seed 数量。表格内加标注会增加视觉复杂度。\"\n  resolution_round: 16\n\n- id: \"R16-M3\"\n  summary: \"Figure 1 字体偏小，接近可读性下限\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"Figure 1 内部文字约为正文字号的 60-65%，打印时可能不够清晰。\"\n  resolution: \"Figure 重新生成风险高（DDL 前 2 天）。当前字体大小在 ACL 论文中属正常范围。Rebuttal 可提供高清版本。\"\n  resolution_round: 16\n\n# === Round 17 New Issues ===\n\n- id: \"R17-W1\"\n  summary: \"核心发现可预测性未被讨论——complexity moderates formulation choice 方向直觉可预期\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R2-W1 提出：CWM 生成 ~477 tokens + exact match vs CLS 1 token，长输出更难不令人意外。论文量化了 gap (18-26pp) 有价值但未讨论结果是否 a priori 可预测。R1 partial REBUT：方向可预测≠研究无价值，但同意应增加讨论区分 confirmation vs genuinely novel finding。\"\n  action_items:\n    - round: 17\n      action: \"在 §3.5 或 §5 增加一段讨论，承认核心发现方向的可预测性，并强调量化精度（18-26pp）、function-level 等价性、format collapse 机制等增量价值\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1459 · 2026-05-23T17:43:39.796135+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 25416}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1460 · 2026-05-23T17:46:08.960881+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 17 审稿报告（Fresh Review）\n\n## Summary\n\n本文提出了三种 execution-free 代码修复验证 formulation（CLS、CWM、TRAJ）的首个系统性比较，在两个代码 LLM 家族（Qwen3、DeepSeek-Coder）、两个复杂度级别和多个随机种子下进行 ≤8B LoRA 微调评估。核心发现：function-level 下 CLS 和 CWM 统计等价（TOST p=0.007）；repo-level 下 CWM 因 format collapse 落后 CLS 18-26pp。14B 初步结果（3 seeds, 单家族）显示所有 formulation 收敛至 1.07pp 以内。\n\n---\n\n## Strengths\n\n1. **统计方法论极为出色** [共识: R1, R2]：TOST 等价检验（非仅不显著）、Bayesian ROPE、clustered bootstrap + Holm-Bonferroni 校正、mixed-effects regression——在 NLP 论文中极为罕见的统计严谨度。统计层次声明清晰（§3.1: TOST primary → bootstrap CI → ROPE robustness → regression mechanism）。\n\n2. **匹配实验设计** [共识: R1, R2]：相同超参数、训练数据、checkpoint 策略、计算预算——首个真正公平的 formulation 比较。CLS-CWM 比较的控制变量设计是方法论层面的真正贡献。\n\n3. **诚实的局限性披露** [R1]：坦承功效不足（§3.4: ~0.3）、CLS-TRAJ 等价性未确认、confound 分析不能完全排除混淆。\n\n4. **Failure mode taxonomy (Table 4)** [共识: R1, R2]：format collapse / decision collapse / aggregation penalty 三分类为从业者选择 verification formulation 提供了可操作的诊断标准，是本文最有实践价值的贡献。\n\n5. **References 覆盖全面** [R2]：CodePRM, GenPRM, FunPRM, SWE-RM, CodeScaler, RepoExec, VeRPO, Aletheia, CRUXEval, SolidCoder 等近期重要工作均已引用。GenRM domain-specific 对比分析（math vs code）有 insight。\n\n6. **丰富附录** [R1]：15+ 页 appendix 包含 robustness checks、ablation details、qualitative analysis 和 hyperparameter tables，大幅提升可审查性和可复现性。\n\n---\n\n## Weaknesses\n\n### Must-Fix [共识 Critical]\n\n**N1. TRAJ 175× 训练数据量混淆变量未得到充分控制**\n[R1-N1 提出, R2 AGREE] | 对应 Issue Tracker: R6-W4\n\nTRAJ 使用 ~400 variant-level 训练样本 vs CLS/CWM ~70K per-test 样本，差异达 175×。论文声称该差异 \"inherent to the formulation\"（§2.1），但无法分离 formulation effect 和 data regime effect。Appendix O 的下采样实验（CLS 降至 ~1K）仍是 TRAJ 的 2.5×。14B 收敛可能反映更大模型从少量数据学习更好（R2 补充），而非 formulation 本身收敛。关于 TRAJ 的所有结论——§3.5 的归因和 routing 建议——证据基础不足。\n\n**建议**：(a) 将 TRAJ 比较重新定位为 \"formulation-in-its-natural-data-regime\" 联合比较，明确声明不是 controlled-data 比较；(b) 增加 CLS 在 ~400 samples 的极端下采样实验。\n\n**N2. 统计功效 ~0.3 限制等价性声明的可解释性**\n[R1-N2 提出, R2 AGREE] | 对应 Issue Tracker: R8-W1\n\nTOST 功效 ~0.3 → 70% 概率无法确认等价。CLS-CWM 等价通过（p=0.007, Holm-corrected）是强证据，无争议。但 CLS-TRAJ 未通过（adjusted p=0.075）在低功效下是 inconclusive——既非等价也非不等价的证据。\"not confirmed\" 措辞仍暗示方向性判断，建议改为 \"inconclusive\"。Repo-level 2-3 seeds 功效更低（Table 14 CLS-TRAJ CI: ±10.42pp），不允许得出方向性结论。\n\n**建议**：(a) 增加 MDE（Minimum Detectable Effect）表格；(b) 功效不足的比较使用 \"inconclusive\" 措辞。\n\n**N3. 14B convergence 叙事权重与证据严重不匹配**\n[R2-N2 提出, R1 AGREE] | 对应 Issue Tracker: R13-W3\n\n14B 结果在 abstract、introduction、conclusion 中均作为关键叙事元素（\"the gap narrows monotonically from 3.11pp to 1.07pp\"），但仅基于 3 seeds、单一模型家族、TOST df=2。在 power ~0.3 背景下 df=2 几乎无统计区分力。论文标注 \"preliminary observation\" 但随后围绕它构建了 capacity-dependent account 和 GenRM 桥接论述，使读者高估 14B 发现的可靠性。Conclusion 承认 \"scaling to 32B+ with more seeds\" 是 future direction，实际上承认了证据不足，但 abstract 叙事未反映这一不确定性。\n\n**建议**：(a) 14B 结果从 abstract 降级或移除；(b) conclusion 中明确标注为 speculative direction 而非 supported finding。\n\n### Should-Fix [共识 Warning]\n\n**W1. 标题/Abstract scope 超出实际实验范围**\n[R2-N1 提出, R1 AGREE with nuance] | 对应 Issue Tracker: R16-N2\n\n\"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\" 暗示通用比较，实际限于 ≤8B LoRA + 2 families + Python + 合成 mutation。R1 认为 \"systematic\" 可指方法论系统性而非穷举性，建议降为 Should-Fix；R2 认为读者期望更广覆盖。共识：标题或 abstract 应加范围限定。Conclusion §5 \"We presented the first systematic comparison\" 无任何限定词尤为突出。\n\n**W2. 单基准/单语言/合成数据限制泛化性**\n[R1-W1 + R2-W3 提出, 双方 AGREE] | 对应 Issue Tracker: R6-W6\n\n全部实验仅 SWE-bench Verified（500 实例）+ Python + 合成 mutation（5 种 operator）。真实 repo-level bug 涉及多文件语义错误、逻辑缺陷，非简单 mutation 能覆盖。R1 补充：不同 formulation 对合成 mutation 可能有不同敏感度——CLS 对 mutation 类型更 robust，CWM 在合成 mutation 简单输出上可能被高估。此方向性 confound 论文未讨论。\n\n**W3. CWM format collapse 的 \"inherent limitation\" 归因需更审慎**\n[R1-W2 提出, R2 AGREE] | 对应 Issue Tracker: R16-W2\n\n论文自身的 14B 数据（gap 收窄到 1.07pp）和 conclusion hedging 暗示 format collapse 可能是容量不足的症状，与正文中将其描述为结构性弱点（§2.2, §3.5）存在叙事张力。4 种 intervention 全在 ≤8B 上测试。建议改为 \"limitation under current ≤8B LoRA training regime\"。\n\n**W4. Error complementarity 实践价值 framing 与证据不匹配**\n[R1-W3 ≈ R2-W2, 双方 AGREE] | 对应 Issue Tracker: R13-W2\n\nOracle combination +2.80pp/+14.58pp（single-seed），但 simple routing heuristics <0.4pp。Conclusion 仍将 \"complexity-aware routing\" 列为第一 future direction——对 <0.4pp 的结果过于乐观。互补性在 §1 contributions list 被列为第二大贡献，权重过大。建议降级为 future work motivation 而非 standalone contribution。\n\n**W5. ±2pp SESOI 缺少独立实践论证**\n[R1-W4 提出, R2 AGREE with nuance] | 对应 Issue Tracker: R6-W1\n\nSESOI 应基于 downstream 实践意义——2pp verifier accuracy 差异对 repair@K 影响多大？论文未提供此分析。Sensitivity analysis（±1.5-3pp）表明 CLS-CWM 等价对 margin 选择 robust，但 SESOI 本身需实践论证。R2 认为 ±2pp 是合理 convention，严重程度低于 R1 评估。\n\n**W6. 核心发现可预测性未被讨论**\n[R2-W1 提出, R1 partial REBUT] | 新建 Issue: R17-W1\n\n\"Complexity moderates formulation choice\" 方向直觉可预测（CWM ~477 tokens + exact match vs CLS 1 token）。R1 反驳：方向可预测 ≠ 研究无价值，量化 18-26pp gap、function-level 等价性、format collapse 机制是 non-trivial。共识：增加讨论区分 \"confirmation of intuition\" vs \"genuinely novel finding\"。\n\n### Dismissed\n\n**R2-W4 (Appendix 与正文比例失衡)**：R1 有效 REBUT——ACL ARR 对 appendix 无页数限制，正文自洽，appendix 提供 reproducibility 材料是标准做法。不计入 weakness。\n\n### Minor [共识]\n\n- **M1**: Table 1 TRAJ 配置差异脚注（\"Training configuration differs\"）应在正文中更显著呈现 [R1, R2]\n- **M2**: Figure 2 y-axis 非零起点应在 caption 标注（与 Figure 3 统一）[R1, R2]\n- **M3**: CWM 术语可能与 RL world model 概念混淆，建议 §2.1 首次出现时加注释区分 [R2]\n- **M4**: DreamPRM 和 CodePRM 建议在 Related Work 正文中增加具体讨论 [R2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. 统计方法论是论文最大优势 [unanimous]\n2. CLS-CWM function-level 等价性证据可信 (p=0.007) [unanimous]\n3. TRAJ 比较因 175× data volume confound 需重新定位 [R1 raised, R2 AGREE]\n4. 14B 叙事权重应降低 [R2 raised, R1 AGREE]\n5. Error complementarity 目前无实用 routing 方案 [mutual AGREE]\n6. Failure mode taxonomy 有独立实践价值 [unanimous]\n7. 标题/结论 scope 应与实验 scope 匹配 [mutual AGREE]\n8. 核心发现方向直觉可预测但量化有价值 [partial consensus]\n\n## Reviewer Divergence\n\n1. **Overall Assessment**: R1 3.5 (Borderline Conference) vs R2 3.0 (Findings)。分歧在于 matched experimental design 的方法论贡献是否达到 main conference novelty 门槛。R1 更看重填补文献空白的独立价值；R2 认为 empirical comparison 无 new method 难达主会议标准。合理的 judgment call。\n2. **Soundness**: R1 3/5（因 TRAJ confound 和 power 限制）vs R2 4→3.5/5（交叉回应后下调）。\n\n---\n\n## Questions for Authors\n\n1. 能否提供 CLS 在 ~400 samples（与 TRAJ 完全匹配）下的极端下采样实验？这将直接回答 data volume vs formulation effect 的归因问题。\n2. Minimum Detectable Effect (MDE) 在当前样本量和 TOST 设置下是多少？能否提供 MDE 表格以帮助读者判断结论强度？\n3. 14B 结果能否获得第二个模型家族（如 DeepSeek-Coder-14B 或其他）的验证？\n4. ±2pp SESOI 对应下游 repair@K 的预期影响量级是多少？\n\n---\n\n## Missing References\n\n无重要遗漏。R2 建议 DreamPRM 和 CodePRM 在 Related Work 正文中增加具体讨论（当前仅在引用列表中），因其与本文 PRM 类比直接相关。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未启用 external_review）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：done**（2 warnings, 19 info）\n\n- **Warning 1 (page 1-2)**：连续两页纯文本（Abstract + Introduction），首个 display item Figure 1 出现在第 3 页。审稿人前 2 分钟只看到文字墙，可能影响第一印象。建议将 Figure 1 提前或在 page 2 加入概览图/表。\n- **Warning 2 (page 5)**：三个 display items（Table 1 + Figure 2 + Table 2）挤压在同一页，视觉密度偏高。建议将 Table 2 移至下一页。\n- **Info**：全文排版整洁专业，booktabs 统一，无 margin 溢出或 LaTeX 渲染错误。主文 8 页含 6 个 display items（2 figures + 4 tables），密度适中。References 3 页格式统一，无未解析引用。正文 8 页合规，Limitations 约半栏合规。匿名性无违反。\n\n---\n\n## Overall Assessment\n\n**综合评分：3.0 (Findings)**\n\n**置信度：4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3/5 | 2.5/5 | 2.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\n**评分理由**：\n\n论文在统计方法论和实验设计上达到很高水准，填补了 CLS/CWM/TRAJ 无匹配比较的文献空白。CLS-CWM function-level 等价性是有统计支撑的可信结论。Failure mode taxonomy 有独立实践价值。\n\n三个核心限制将其定位在 Findings 水平：\n1. **TRAJ 数据量混淆变量** (N1) 使论文三分之一的 formulation 比较缺乏充分因果推断基础。\n2. **统计功效 ~0.3** (N2) 使多数比较停留在 inconclusive 状态，削弱了 \"systematic comparison\" 的信息量。\n3. **14B 叙事过重** (N3) 在证据不足的情况下构建了过多推论框架。\n\n贡献类型（empirical comparison, no new method）和 excitement 水平（2.5-3/5）限制了 main conference 竞争力。论文适合 Findings track——soundness 和 reproducibility 达标，方法论有参考价值。\n\n**修复后潜力**：若作者 (a) 将 TRAJ 比较重新定位为 \"formulation + data regime\" 联合比较，(b) 对功效不足的比较使用 \"inconclusive\" 措辞，(c) 将 14B 从 abstract/conclusion 核心叙事降级为 exploratory observation，论文可达 **3.5 (Borderline Conference)**。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 2 (error complementarity): <0.4pp heuristic gain 作为主要贡献权重过大。建议降级为 negative result + future work motivation。\n- \"first systematic comparison\" 需加 scope 限定（≤8B LoRA, Python, SWE-bench）。\n- Mechanistic pathway 解释（\"operating through output format\"）是 R16 的有效修复，本轮无新问题。\n\n### §2 Method\n- §2.1: TRAJ 定义后应立即说明其 data regime 与 CLS/CWM 的根本差异（175×），而非留到 §3.5。读者需要在理解 formulation 时就知道这个关键约束。\n- §2.2 Expected Failure Modes: \"format compliance collapse\" 的归因应从 \"formulation-inherent\" 调整为 \"observed under current training regime\"，与 14B 收敛数据和 Limitations 的 hedging 保持一致。\n\n### §3 Experiments\n- §3.1 Statistics: 统计方法层次声明（TOST primary → bootstrap CI → ROPE robustness → regression mechanism）是 R16 的有效修复，结构清晰。\n- §3.3 Scaling: \"the gap narrows monotonically\" 在仅 3 个 data points (4B, 8B, 14B) 上拟合 monotonic 趋势——df=0 的线性拟合不可靠，措辞应更审慎。\n- §3.4 Equivalence: (a) \"not confirmed\" 改为 \"inconclusive at current power\"；(b) 增加 MDE 表格；(c) 功效分析从 Appendix 移至主文考虑。\n- §3.5 Repo-Level: \"format collapse is a structural bottleneck\" 需加 \"under ≤8B LoRA\" 限定。Table 4 failure mode taxonomy 是有独立价值的贡献。\n- Table 1: TRAJ 配置差异脚注应在正文中更显著呈现。\n- Figure 2: caption 应标注 \"y-axis does not start at zero\"（与 Figure 3 统一）。\n\n### §4 Related Work\n- 覆盖全面，无重要遗漏。\n- DreamPRM 和 CodePRM 建议在正文中增加具体讨论（当前仅引用）。\n- GenRM domain-specific 对比（code ≠ math for generative verification）是有价值的 insight。\n\n### §5 Conclusion\n- \"We presented the first systematic comparison\" 需加范围限定。\n- 14B 相关推论（capacity-dependent account, GenRM 桥接）应明确标注为 speculative。\n- \"three directions follow\" 中 routing 方向需降低乐观程度（<0.4pp heuristic gain）。\n\n### Limitations\n- 长度和覆盖面合适（~半栏，3 个要点），符合 EMNLP 2026 规范。\n- 建议增加对 mutation data 可能系统性偏向特定 formulation 的讨论。\n- \"Format-specific interventions (constrained decoding, output-format pretraining) may mitigate CWM format collapse but were not evaluated\" 是好的披露。",
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 17 审稿报告（Fresh Review）\n\n## Summary\n\n本文提出了三种 execution-free 代码修复验证 formulation（CLS、CWM、TRAJ）的首个系统性比较，在两个代码 LLM 家族（Qwen3、DeepSeek-Coder）、两个复杂度级别和多个随机种子下进行 ≤8B LoRA 微调评估。核心发现：function-level 下 CLS 和 CWM 统计等价（TOST p=0.007）；repo-level 下 CWM 因 format collapse 落后 CLS 18-26pp。14B 初步结果（3 seeds, 单家族）显示所有 formulation 收敛至 1.07pp 以内。\n\n---\n\n## Strengths\n\n1. **统计方法论极为出色** [共识: R1, R2]：TOST 等价检验（非仅不显著）、Bayesian ROPE、clustered bootstrap + Holm-Bonferroni 校正、mixed-effects regression——在 NLP 论文中极为罕见的统计严谨度。统计层次声明清晰（§3.1: TOST primary → bootstrap CI → ROPE robustness → regression mechanism）。\n\n2. **匹配实验设计** [共识: R1, R2]：相同超参数、训练数据、checkpoint 策略、计算预算——首个真正公平的 formulation 比较。CLS-CWM 比较的控制变量设计是方法论层面的真正贡献。\n\n3. **诚实的局限性披露** [R1]：坦承功效不足（§3.4: ~0.3）、CLS-TRAJ 等价性未确认、confound 分析不能完全排除混淆。\n\n4. **Failure mode taxonomy (Table 4)** [共识: R1, R2]：format collapse / decision collapse / aggregation penalty 三分类为从业者选择 verification formulation 提供了可操作的诊断标准，是本文最有实践价值的贡献。\n\n5. **References 覆盖全面** [R2]：CodePRM, GenPRM, FunPRM, SWE-RM, CodeScaler, RepoExec, VeRPO, Aletheia, CRUXEval, SolidCoder 等近期重要工作均已引用。GenRM domain-specific 对比分析（math vs code）有 insight。\n\n6. **丰富附录** [R1]：15+ 页 appendix 包含 robustness checks、ablation details、qualitative analysis 和 hyperparameter tables，大幅提升可审查性和可复现性。\n\n---\n\n## Weaknesses\n\n### Must-Fix [共识 Critical]\n\n**N1. TRAJ 175× 训练数据量混淆变量未得到充分控制**\n[R1-N1 提出, R2 AGREE] | 对应 Issue Tracker: R6-W4\n\nTRAJ 使用 ~400 variant-level 训练样本 vs CLS/CWM ~70K per-test 样本，差异达 175×。论文声称该差异 \"inherent to the formulation\"（§2.1），但无法分离 formulation effect 和 data regime effect。Appendix O 的下采样实验（CLS 降至 ~1K）仍是 TRAJ 的 2.5×。14B 收敛可能反映更大模型从少量数据学习更好（R2 补充），而非 formulation 本身收敛。关于 TRAJ 的所有结论——§3.5 的归因和 routing 建议——证据基础不足。\n\n**建议**：(a) 将 TRAJ 比较重新定位为 \"formulation-in-its-natural-data-regime\" 联合比较，明确声明不是 controlled-data 比较；(b) 增加 CLS 在 ~400 samples 的极端下采样实验。\n\n**N2. 统计功效 ~0.3 限制等价性声明的可解释性**\n[R1-N2 提出, R2 AGREE] | 对应 Issue Tracker: R8-W1\n\nTOST 功效 ~0.3 → 70% 概率无法确认等价。CLS-CWM 等价通过（p=0.007, Holm-corrected）是强证据，无争议。但 CLS-TRAJ 未通过（adjusted p=0.075）在低功效下是 inconclusive——既非等价也非不等价的证据。\"not confirmed\" 措辞仍暗示方向性判断，建议改为 \"inconclusive\"。Repo-level 2-3 seeds 功效更低（Table 14 CLS-TRAJ CI: ±10.42pp），不允许得出方向性结论。\n\n**建议**：(a) 增加 MDE（Minimum Detectable Effect）表格；(b) 功效不足的比较使用 \"inconclusive\" 措辞。\n\n**N3. 14B convergence 叙事权重与证据严重不匹配**\n[R2-N2 提出, R1 AGREE] | 对应 Issue Tracker: R13-W3\n\n14B 结果在 abstract、introduction、conclusion 中均作为关键叙事元素（\"the gap narrows monotonically from 3.11pp to 1.07pp\"），但仅基于 3 seeds、单一模型家族、TOST df=2。在 power ~0.3 背景下 df=2 几乎无统计区分力。论文标注 \"preliminary observation\" 但随后围绕它构建了 capacity-dependent account 和 GenRM 桥接论述，使读者高估 14B 发现的可靠性。Conclusion 承认 \"scaling to 32B+ with more seeds\" 是 future direction，实际上承认了证据不足，但 abstract 叙事未反映这一不确定性。\n\n**建议**：(a) 14B 结果从 abstract 降级或移除；(b) conclusion 中明确标注为 speculative direction 而非 supported finding。\n\n### Should-Fix [共识 Warning]\n\n**W1. 标题/Abstract scope 超出实际实验范围**\n[R2-N1 提出, R1 AGREE with nuance] | 对应 Issue Tracker: R16-N2\n\n\"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\" 暗示通用比较，实际限于 ≤8B LoRA + 2 families + Python + 合成 mutation。R1 认为 \"systematic\" 可指方法论系统性而非穷举性，建议降为 Should-Fix；R2 认为读者期望更广覆盖。共识：标题或 abstract 应加范围限定。Conclusion §5 \"We presented the first systematic comparison\" 无任何限定词尤为突出。\n\n**W2. 单基准/单语言/合成数据限制泛化性**\n[R1-W1 + R2-W3 提出, 双方 AGREE] | 对应 Issue Tracker: R6-W6\n\n全部实验仅 SWE-bench Verified（500 实例）+ Python + 合成 mutation（5 种 operator）。真实 repo-level bug 涉及多文件语义错误、逻辑缺陷，非简单 mutation 能覆盖。R1 补充：不同 formulation 对合成 mutation 可能有不同敏感度——CLS 对 mutation 类型更 robust，CWM 在合成 mutation 简单输出上可能被高估。此方向性 confound 论文未讨论。\n\n**W3. CWM format collapse 的 \"inherent limitation\" 归因需更审慎**\n[R1-W2 提出, R2 AGREE] | 对应 Issue Tracker: R16-W2\n\n论文自身的 14B 数据（gap 收窄到 1.07pp）和 conclusion hedging 暗示 format collapse 可能是容量不足的症状，与正文中将其描述为结构性弱点（§2.2, §3.5）存在叙事张力。4 种 intervention 全在 ≤8B 上测试。建议改为 \"limitation under current ≤8B LoRA training regime\"。\n\n**W4. Error complementarity 实践价值 framing 与证据不匹配**\n[R1-W3 ≈ R2-W2, 双方 AGREE] | 对应 Issue Tracker: R13-W2\n\nOracle combination +2.80pp/+14.58pp（single-seed），但 simple routing heuristics <0.4pp。Conclusion 仍将 \"complexity-aware routing\" 列为第一 future direction——对 <0.4pp 的结果过于乐观。互补性在 §1 contributions list 被列为第二大贡献，权重过大。建议降级为 future work motivation 而非 standalone contribution。\n\n**W5. ±2pp SESOI 缺少独立实践论证**\n[R1-W4 提出, R2 AGREE with nuance] | 对应 Issue Tracker: R6-W1\n\nSESOI 应基于 downstream 实践意义——2pp verifier accuracy 差异对 repair@K 影响多大？论文未提供此分析。Sensitivity analysis（±1.5-3pp）表明 CLS-CWM 等价对 margin 选择 robust，但 SESOI 本身需实践论证。R2 认为 ±2pp 是合理 convention，严重程度低于 R1 评估。\n\n**W6. 核心发现可预测性未被讨论**\n[R2-W1 提出, R1 partial REBUT] | 新建 Issue: R17-W1\n\n\"Complexity moderates formulation choice\" 方向直觉可预测（CWM ~477 tokens + exact match vs CLS 1 token）。R1 反驳：方向可预测 ≠ 研究无价值，量化 18-26pp gap、function-level 等价性、format collapse 机制是 non-trivial。共识：增加讨论区分 \"confirmation of intuition\" vs \"genuinely novel finding\"。\n\n### Dismissed\n\n**R2-W4 (Appendix 与正文比例失衡)**：R1 有效 REBUT——ACL ARR 对 appendix 无页数限制，正文自洽，appendix 提供 reproducibility 材料是标准做法。不计入 weakness。\n\n### Minor [共识]\n\n- **M1**: Table 1 TRAJ 配置差异脚注（\"Training configuration differs\"）应在正文中更显著呈现 [R1, R2]\n- **M2**: Figure 2 y-axis 非零起点应在 caption 标注（与 Figure 3 统一）[R1, R2]\n- **M3**: CWM 术语可能与 RL world model 概念混淆，建议 §2.1 首次出现时加注释区分 [R2]\n- **M4**: DreamPRM 和 CodePRM 建议在 Related Work 正文中增加具体讨论 [R2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. 统计方法论是论文最大优势 [unanimous]\n2. CLS-CWM function-level 等价性证据可信 (p=0.007) [unanimous]\n3. TRAJ 比较因 175× data volume confound 需重新定位 [R1 raised, R2 AGREE]\n4. 14B 叙事权重应降低 [R2 raised, R1 AGREE]\n5. Error complementarity 目前无实用 routing 方案 [mutual AGREE]\n6. Failure mode taxonomy 有独立实践价值 [unanimous]\n7. 标题/结论 scope 应与实验 scope 匹配 [mutual AGREE]\n8. 核心发现方向直觉可预测但量化有价值 [partial consensus]\n\n## Reviewer Divergence\n\n1. **Overall Assessment**: R1 3.5 (Borderline Conference) vs R2 3.0 (Findings)。分歧在于 matched experimental design 的方法论贡献是否达到 main conference novelty 门槛。R1 更看重填补文献空白的独立价值；R2 认为 empirical comparison 无 new method 难达主会议标准。合理的 judgment call。\n2. **Soundness**: R1 3/5（因 TRAJ confound 和 power 限制）vs R2 4→3.5/5（交叉回应后下调）。\n\n---\n\n## Questions for Authors\n\n1. 能否提供 CLS 在 ~400 samples（与 TRAJ 完全匹配）下的极端下采样实验？这将直接回答 data volume vs formulation effect 的归因问题。\n2. Minimum Detectable Effect (MDE) 在当前样本量和 TOST 设置下是多少？能否提供 MDE 表格以帮助读者判断结论强度？\n3. 14B 结果能否获得第二个模型家族（如 DeepSeek-Coder-14B 或其他）的验证？\n4. ±2pp SESOI 对应下游 repair@K 的预期影响量级是多少？\n\n---\n\n## Missing References\n\n无重要遗漏。R2 建议 DreamPRM 和 CodePRM 在 Related Work 正文中增加具体讨论（当前仅在引用列表中），因其与本文 PRM 类比直接相关。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未启用 external_review）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：done**（2 warnings, 19 info）\n\n- **Warning 1 (page 1-2)**：连续两页纯文本（Abstract + Introduction），首个 display item Figure 1 出现在第 3 页。审稿人前 2 分钟只看到文字墙，可能影响第一印象。建议将 Figure 1 提前或在 page 2 加入概览图/表。\n- **Warning 2 (page 5)**：三个 display items（Table 1 + Figure 2 + Table 2）挤压在同一页，视觉密度偏高。建议将 Table 2 移至下一页。\n- **Info**：全文排版整洁专业，booktabs 统一，无 margin 溢出或 LaTeX 渲染错误。主文 8 页含 6 个 display items（2 figures + 4 tables），密度适中。References 3 页格式统一，无未解析引用。正文 8 页合规，Limitations 约半栏合规。匿名性无违反。\n\n---\n\n## Overall Assessment\n\n**综合评分：3.0 (Findings)**\n\n**置信度：4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3/5 | 2.5/5 | 2.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\n**评分理由**：\n\n论文在统计方法论和实验设计上达到很高水准，填补了 CLS/CWM/TRAJ 无匹配比较的文献空白。CLS-CWM function-level 等价性是有统计支撑的可信结论。Failure mode taxonomy 有独立实践价值。\n\n三个核心限制将其定位在 Findings 水平：\n1. **TRAJ 数据量混淆变量** (N1) 使论文三分之一的 formulation 比较缺乏充分因果推断基础。\n2. **统计功效 ~0.3** (N2) 使多数比较停留在 inconclusive 状态，削弱了 \"systematic comparison\" 的信息量。\n3. **14B 叙事过重** (N3) 在证据不足的情况下构建了过多推论框架。\n\n贡献类型（empirical comparison, no new method）和 excitement 水平（2.5-3/5）限制了 main conference 竞争力。论文适合 Findings track——soundness 和 reproducibility 达标，方法论有参考价值。\n\n**修复后潜力**：若作者 (a) 将 TRAJ 比较重新定位为 \"formulation + data regime\" 联合比较，(b) 对功效不足的比较使用 \"inconclusive\" 措辞，(c) 将 14B 从 abstract/conclusion 核心叙事降级为 exploratory observation，论文可达 **3.5 (Borderline Conference)**。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 2 (error complementarity): <0.4pp heuristic gain 作为主要贡献权重过大。建议降级为 negative result + future work motivation。\n- \"first systematic comparison\" 需加 scope 限定（≤8B LoRA, Python, SWE-bench）。\n- Mechanistic pathway 解释（\"operating through output format\"）是 R16 的有效修复，本轮无新问题。\n\n### §2 Method\n- §2.1: TRAJ 定义后应立即说明其 data regime 与 CLS/CWM 的根本差异（175×），而非留到 §3.5。读者需要在理解 formulation 时就知道这个关键约束。\n- §2.2 Expected Failure Modes: \"format compliance collapse\" 的归因应从 \"formulation-inherent\" 调整为 \"observed under current training regime\"，与 14B 收敛数据和 Limitations 的 hedging 保持一致。\n\n### §3 Experiments\n- §3.1 Statistics: 统计方法层次声明（TOST primary → bootstrap CI → ROPE robustness → regression mechanism）是 R16 的有效修复，结构清晰。\n- §3.3 Scaling: \"the gap narrows monotonically\" 在仅 3 个 data points (4B, 8B, 14B) 上拟合 monotonic 趋势——df=0 的线性拟合不可靠，措辞应更审慎。\n- §3.4 Equivalence: (a) \"not confirmed\" 改为 \"inconclusive at current power\"；(b) 增加 MDE 表格；(c) 功效分析从 Appendix 移至主文考虑。\n- §3.5 Repo-Level: \"format collapse is a structural bottleneck\" 需加 \"under ≤8B LoRA\" 限定。Table 4 failure mode taxonomy 是有独立价值的贡献。\n- Table 1: TRAJ 配置差异脚注应在正文中更显著呈现。\n- Figure 2: caption 应标注 \"y-axis does not start at zero\"（与 Figure 3 统一）。\n\n### §4 Related Work\n- 覆盖全面，无重要遗漏。\n- DreamPRM 和 CodePRM 建议在正文中增加具体讨论（当前仅引用）。\n- GenRM domain-specific 对比（code ≠ math for generative verification）是有价值的 insight。\n\n### §5 Conclusion\n- \"We presented the first systematic comparison\" 需加范围限定。\n- 14B 相关推论（capacity-dependent account, GenRM 桥接）应明确标注为 speculative。\n- \"three directions follow\" 中 routing 方向需降低乐观程度（<0.4pp heuristic gain）。\n\n### Limitations\n- 长度和覆盖面合适（~半栏，3 个要点），符合 EMNLP 2026 规范。\n- 建议增加对 mutation data 可能系统性偏向特定 formulation 的讨论。\n- \"Format-specific interventions (constrained decoding, output-format pretraining) may mitigate CWM format collapse but were not evaluated\" 是好的披露。",
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 1461 · 2026-05-23T17:46:13.078459+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4117
}
```

</details>

---


### Assistant

_source line 1462 · 2026-05-23T17:46:38.409211+00:00_

Round 17 审稿完成。

**审稿报告已投递给 Research Director。**

核心结论：

- **综合评分：3.0 (Findings)**，R1 给 3.5，R2 给 3.0
- **3 个 Must-Fix**：TRAJ 175× 数据量混淆（N1）、TOST 功效 ~0.3 限制等价性声明（N2）、14B 叙事过重（N3）
- **7 个 Should-Fix**：标题 scope、单基准泛化性、CWM 归因过强、互补性 framing、SESOI 论证、发现可预测性、mutation 代表性
- **修复后潜力**：若重新定位 TRAJ 比较、调整 inconclusive 措辞、降级 14B 叙事，可达 3.5 (Borderline Conference)
- **Issue Tracker 已同步更新**，新建 1 个 open issue（R17-W1），8 个已有 issue 追加 R17 mention

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 133

## Round 133

2 recorded events


### User

_source line 1463 · 2026-05-23T17:46:40.941884+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 所有 Must-Fix（N1, N2）、Should-Fix（W1-W4）和小问题（M1-M5）的逐条回应，并汇报给 Director。

核心判断：R1 和我在大多数问题上一致，尤其是 scope 过宽、14B 证据不足、error complementarity 实践价值有限。R1 提出的 TRAJ 数据量混淆变量（N1）是我原审中忽略的重要 confound，我同意将其视为 critical issue。主要分歧在 Overall 评分（R1: 3.5 vs 我: 3.0）和 Soundness（R1: 3 vs 我: 4→修正为 3.5）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1464 · 2026-05-23T17:46:54.735088+00:00_

Round 17 审稿完成。

**审稿报告已投递给 Research Director**。综合评分 **3.0 (Findings)**。

**核心发现**：
- **3 个 Must-Fix**：TRAJ 175× 数据量混淆（N1）、统计功效 ~0.3 限制等价性声明（N2）、14B 叙事权重与证据不匹配（N3）
- **7 个 Should-Fix**：标题 scope 过广、单基准泛化性、CWM 归因过强、error complementarity framing、SESOI 论证、发现可预测性、mutation 数据代表性
- **修复后潜力**：3.5 (Borderline Conference)

Issue Tracker 已同步更新（8 个既有 issue 追加 R17 mention，新建 R17-W1）。视觉审查结果已纳入报告（2 warnings: 首页文字墙、page 5 display items 过密）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 134

## Round 134

60 recorded events


### User

_source line 1465 · 2026-05-24T02:53:49.946877+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main/Findings unified)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1466 · 2026-05-24T02:53:56.154538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1467 · 2026-05-24T02:53:56.205509+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1468 · 2026-05-24T02:54:04.493642+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1469 · 2026-05-24T02:54:04.494087+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1470 · 2026-05-24T02:54:08.311454+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1471 · 2026-05-24T02:54:08.312159+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1472 · 2026-05-24T02:54:13.282299+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 1473 · 2026-05-24T02:54:14.788609+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (267 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D131-cwm-s42-epoch3-seq2048（准备中）\n- D133-cwm-s42-e2-seq2048-home-resume（准备中）\n- deepseek-cwm-repo-s42-epoch2-eval: Eval CWM s42 epoch 2 checkpoint 解耦过拟合 vs seed 差异：如果 epoch 2 accuracy >> epoch 3 (56.7%)，则 CWM repo-level 在 epoch 3 过拟合（准备中）\n- …另有 9 项\n\n## 近期结论\n- **cls-downsample-400-s42** (success): CLS function-level traine
…[truncated 1822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1506
}
```

</details>

---
