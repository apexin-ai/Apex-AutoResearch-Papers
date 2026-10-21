# Director coordination — Part 4 of 7

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/0d/0d5b5d57f8a45f2c2330.json)

## Round 81

### Tool call

_source line 904 · 2026-05-23T03:17:49.074578+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 9 审稿报告（Continue Review）\n\n**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 via ARR (Long Paper)\n**审稿模式**: Continue（基于上轮 R10 审稿意见的修订评估）\n**Reviewer 编排**: 2 人（R1 统计方法论 + 实验严谨性 / R2 Framing + Novelty + 完整性）\n\n---\n\n## Summary\n\n本轮为继续审稿，评估论文在收到上轮（Round 10 Fresh Review, Overall 3.0）审稿意见后的修订质量。主要修改包括：(1) 14B 探索性结果（Table 2, CLS 89.21% vs CWM 89.26%，gap ≈ 0），(2) Bayesian ROPE 分析补充 TOST 等价检验（P(ROPE)=0.975 for CLS-CWM），(3) TOST 功效透明讨论（n_eff≈86, power~0.3），(4) variant-level 分析标注为 exploratory，(5) routing 负结果（<0.4pp of oracle gap），(6) GEE logistic regression robustness check，(7) checkpoint 证据整合，(8) wall-clock 时间（48ms vs 16.3s）。\n\n---\n\n## 修订评估：Issue Tracker 逐条验证\n\n### 全部 RESOLVED（两位 Reviewer 共识）\n\n**[R6-N1] RESOLVED** — Variant-level exploratory 标注 ✅\n§3.5 开头明确标注 \"Variant-level comparisons (n=48) are exploratory due to limited seed coverage\"。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 \"definitive causal attribution requires multi-seed replication\"。两位 Reviewer 一致确认标注充分。\n\n**[R8-W1] RESOLVED** — TOST 功效 + Bayesian ROPE ✅\n三处修改完整解决：(a) §3.4 Statistical power 段落透明披露 n_eff≈86, power~0.3；(b) Bayesian ROPE（Jeffreys prior, ±2pp ROPE）独立验证 CLS-CWM 等价（P(ROPE)=0.975, 95% HDI [+0.10, +2.00pp]）和 CLS-TRAJ 不确定性（P(ROPE)=0.542, inconclusive）；(c) Abstract \"not confirmed after multiple comparison correction\" 准确审慎。R1 称为\"教科书级处理\"，R2 同意。TOST + Bayesian ROPE 双框架的一致性显著增强了证据质量。\n\n**[R8-M2] RESOLVED** — Logistic regression robustness ✅\nAppendix M 补充 GEE logistic regression（binomial family, exchangeable correlation, robust sandwich SEs）。CWM×repo interaction OR=0.31 (0.15, 0.65), p=0.002，与 LPM 一致。Model identity LPM (p=0.002) vs GEE (p=0.410) 差异透明披露——commit 0b38a2b 修正了过强显著性声明。Primary effects 在两种框架下均 robust。\n\n**[R6-M3] RESOLVED** — Figure y-axis ✅\nFigure 2 y-axis 非零起始，caption 标注 \"y-axis does not start at zero\"。两位 Reviewer 均确认：对 0-3pp 差异展示，非零起始合理且有标注。Figure 3 (Appendix) 也已标注。\n\n### STILL_OPEN / WONT_FIX（Inherent Limitation）\n\n**[R6-N4] WONT_FIX** — Novelty ceiling（inherent）\nR2 标 STILL_OPEN（改善但核心贡献类型未变），R1 AGREE on assessment。所有可行 action items 已完成：routing 实验（negative result）、Bayesian ROPE、14B 验证。Excitement 从 2.5 提升至 3.0，但核心贡献类型（empirical comparison of existing formulations）是 inherent limitation，无法通过进一步修改解决。标记为 wont_fix。\n\n**[R8-W7] WONT_FIX** — Conference-level excitement（合并至 R6-N4）\n\n---\n\n## 新发现的问题\n\n### Minor（3 个，两位 Reviewer 共识）\n\n**[R11-M1] Figure 2 中 14B 单 seed 视觉权重**\nR1 提出，R2 AGREE。14B 数据点与多 seed 的 4B/8B 数据点在图中视觉等权，读者快速浏览可能过度解读 gap reversal (CWM 89.26% vs CLS 89.21%)。建议在 14B 数据点加星号/虚线或图内 \"n=1\" 标注。\n\n**[R11-M2] §3.5 LPM vs GEE model identity 不一致需 qualifier**\nR1 提出，R2 AGREE。§3.5 引用 LPM model identity 效应 (p=0.001)，但 Appendix M 的 GEE 给出 p=0.410——从\"高度显著\"到\"完全不显著\"。建议加 qualifier：\"model identity reaches significance under LPM but not under GEE logistic regression (Appendix M); this effect is specification-dependent.\"\n\n**[R11-M3] Abstract \"motivate routing\" 需限定**\nR2 提出，R1 AGREE。Abstract \"motivate complexity-aware formulation routing\" 暗示 routing 有前景，但 §3.6 报告 simple routing capture <0.4pp of oracle gap。建议改为 \"motivate **learned** complexity-aware routing\" 或加半句限定。\n\n### 分歧记录\n\n**R2-NEW-2（Abstract \"not confirmed\" 精确性）**：R2 担心可能被误读为 \"disconfirmed\"，R1 REBUT——\"not confirmed\" 是统计标准用语，上下文和 Bayesian ROPE 提供消歧。Director 裁定：R1 REBUT 成立，不构成 actionable issue。\n\n---\n\n## Strengths（延续上轮 + 本轮新增）\n\n**S1. 统计方法论达到 NLP 领域顶级水平。** TOST + Bayesian ROPE 双框架、ICC-clustered bootstrap、Holm-Bonferroni、GEE robustness check、transparent power analysis——在 NLP empirical papers 中极为罕见。[R1-S2, R2-S1 共识，本轮进一步强化]\n\n**S2. Claim calibration 系统性改善。** 从上轮的\"偶有 overclaim\"提升至\"系统性 well-calibrated\"：exploratory/confirmatory 区分清晰，≤8B 限定一致，TRAJ 措辞审慎，14B 标注恰当。[R2 Framing 一致性检查全部通过]\n\n**S3. 14B capacity-dependent convergence 是有意义的新 insight。** CLS-CWM gap 从 2.62pp (8B) 收窄至 -0.05pp (14B) 暗示 CWM 退化是 capacity-dependent 而非 formulation-inherent——对社区的 resource allocation 有前瞻价值。虽为 single seed / exploratory，但标注恰当。[R2 认为这是本轮最有价值的新增]\n\n**S4. 负结果文档化增加分析深度。** Routing heuristic negative result（<0.4pp of oracle gap）将未验证假设转化为文档化实验结论，比\"future work\"声明更有价值。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（无）\n\n本轮无新增 Must-Fix。所有上轮 tracked CRITICAL issues 均已 RESOLVED 或标记为 inherent limitation (wont_fix)。\n\n### Should-Fix（无新增）\n\n上轮 Should-Fix 均已 RESOLVED。\n\n### Minor（3 个，均为 consensus）\n\nR11-M1, R11-M2, R11-M3（见上文\"新发现的问题\"）。均为低成本 polish 级修改。\n\n---\n\n## Missing References\n\n本轮未发现新的遗漏引用。上轮要求的 CodeRM (Ma et al., ACL 2025) 和 ORM/PRM 映射已在 Related Work 中加入。Kruschke (2013, 2018) 和 Cohen (1988) 正确引用于 Bayesian ROPE 和 power analysis。\n\n---\n\n## External Review\n\n未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查完成（0 critical, 1 warning, 7 info）：\n\n- **[WARNING]** p.24 附录最后一页仅约 14 行（<20% 页面），大面积空白。建议紧凑化或合并。\n- **[INFO]** p.1-2 无 display item，Figure 1 在 p.3 出现（可接受但非最优）。\n- **[INFO]** p.7 Figure 2 y-axis 非零开始，caption 已标注——与 Reviewer 评估一致。\n- **[INFO]** p.8 最后一页极度紧凑（Related Work 续段 + Conclusion + Limitations），reviewer 可能觉得 conclusion 仓促。\n- **[INFO]** p.6 双表格密度较高但未溢出。\n- **[INFO]** p.12 ARR Checklist 在 PDF 中——按用户规则应在 OpenReview form 填写。需确认当前投稿要求。\n- **[INFO]** p.13 Figure 3 单色柱状图，caption 清晰。\n- **[INFO]** p.15 高密度页面但无溢出。\n\n---\n\n## Overall Assessment\n\n### 分项评分\n\n| 维度 | R1 Round 10 | R1 Round 11 | R2 Round 10 | R2 Round 11 | 共识 |\n|------|------------|------------|------------|------------|------|\n| Soundness | 3/5 | **4/5** | 3.5/5 | **4/5** | **4/5** ✅ |\n| Excitement | 3/5 | 3/5 | 2.5/5 | **3/5** | **3/5** ✅ |\n| Reproducibility | 4/5 | 4/5 | — | — | 4/5 |\n| Overall | 3.5 | 3.5 | 3.0 | 3.0 | **见下** |\n| Confidence | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 |\n\n### Overall 评分分歧与裁定\n\n**R1: 3.5 (Borderline Conference)** — 理由：Soundness 3→4 是实质性改善；方法论严谨性本身构成 methodological demonstration value；exceptional soundness 应部分补偿 moderate excitement。引用 Dodge et al. (2019), Card et al. (2020) 等方法论贡献论文作为 precedent。\n\n**R2: 3.0 (Findings)** — 理由：ARR 将 soundness 和 excitement 分开评分是有原因的；soundness 4/5 已充分反映方法论贡献；excitement ceiling（比较已有方法）无法被 soundness 跨维度补偿。Findings 定位恰好匹配。\n\n**Director 裁定：Overall 3.0 (Findings)**\n\nR2 的论点更符合 ARR 评分体系设计：soundness 和 excitement 是独立维度，exceptional soundness 已在 Soundness 4/5 中得到反映，不应 double-count 到 Overall。论文的方法论严谨性是 NLP 领域的示范，但核心贡献类型（empirical comparison without new methods）限制了 excitement。Findings track 是这篇论文的正确归属。\n\nR1 的 3.5 评估是可辩护的——如果 AC 对 empirical comparison papers 有更高的包容度，或认为方法论示范价值有独立 excitement，则 Borderline Conference 成立。两个分数都在合理范围内。\n\n### 与上轮对比\n\n| | Round 10 (Fresh) | Round 11 (Continue) | 变化 |\n|---|---|---|---|\n| 所有 tracked issues resolved | 6 open/in_progress | 0 open（+ 3 新 MINOR） | ✅ 全部解决 |\n| Soundness | 3-3.5/5 | **4/5 共识** | ↑ 显著提升 |\n| Excitement | 2.5-3/5 | **3/5 共识** | ↑ 小幅提升 |\n| Overall | 3.0 | **3.0** | = 维持 |\n\n**修订质量评价**：优秀。所有 tracked issues 均得到充分回应，无一敷衍。Bayesian ROPE、GEE robustness、transparent power analysis 等修改展现了高水平的方法论能力。新增的 3 个 MINOR 问题均为 polish 级别，不影响论文的核心质量。\n\n### 建议定位\n\n**推荐 Findings 接收**。论文在 soundness 维度达到 NLP 领域高水平（TOST + Bayesian ROPE + GEE + ICC + Holm-Bonferroni），failure mode taxonomy 和 14B convergence insight 有实用价值。Excitement 限制为 inherent（贡献类型为 empirical comparison），不影响 Findings 的合格性。\n\n---\n\n## Detailed Comments\n\n### 给作者的修改建议（按优先级）\n\n1. **[R11-M1]** Figure 2 中 14B 数据点加视觉区分（星号/虚线/图内 \"n=1\"），避免 gap reversal 被过度解读。\n2. **[R11-M2]** §3.5 model identity 效应加 LPM vs GEE qualifier（\"specification-dependent\"），保持与 Appendix M 的 claim 强度一致。\n3. **[R11-M3]** Abstract \"motivate routing\" 改为 \"motivate **learned** complexity-aware routing\" 或加限定半句。\n4. **[视觉]** p.24 空白页紧凑化。\n5. **[视觉]** 确认 ARR Checklist 是否应在 PDF 中还是仅在 OpenReview form 中。\n\n### 无需修改的确认\n\n- Abstract ≤8B 限定、TRAJ 措辞、Conclusion 限定、14B exploratory 标注、variant-level exploratory 标注——全部通过 framing 一致性检查。\n- Limitations 覆盖充分（Python-only、≤8B LoRA、synthetic mutation）。\n- 格式合规（8 页正文 + 不计入限制的 Limitations）。",
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
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
    "report": "# Round 9 审稿报告（Continue Review）\n\n**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 via ARR (Long Paper)\n**审稿模式**: Continue（基于上轮 R10 审稿意见的修订评估）\n**Reviewer 编排**: 2 人（R1 统计方法论 + 实验严谨性 / R2 Framing + Novelty + 完整性）\n\n---\n\n## Summary\n\n本轮为继续审稿，评估论文在收到上轮（Round 10 Fresh Review, Overall 3.0）审稿意见后的修订质量。主要修改包括：(1) 14B 探索性结果（Table 2, CLS 89.21% vs CWM 89.26%，gap ≈ 0），(2) Bayesian ROPE 分析补充 TOST 等价检验（P(ROPE)=0.975 for CLS-CWM），(3) TOST 功效透明讨论（n_eff≈86, power~0.3），(4) variant-level 分析标注为 exploratory，(5) routing 负结果（<0.4pp of oracle gap），(6) GEE logistic regression robustness check，(7) checkpoint 证据整合，(8) wall-clock 时间（48ms vs 16.3s）。\n\n---\n\n## 修订评估：Issue Tracker 逐条验证\n\n### 全部 RESOLVED（两位 Reviewer 共识）\n\n**[R6-N1] RESOLVED** — Variant-level exploratory 标注 ✅\n§3.5 开头明确标注 \"Variant-level comparisons (n=48) are exploratory due to limited seed coverage\"。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 \"definitive causal attribution requires multi-seed replication\"。两位 Reviewer 一致确认标注充分。\n\n**[R8-W1] RESOLVED** — TOST 功效 + Bayesian ROPE ✅\n三处修改完整解决：(a) §3.4 Statistical power 段落透明披露 n_eff≈86, power~0.3；(b) Bayesian ROPE（Jeffreys prior, ±2pp ROPE）独立验证 CLS-CWM 等价（P(ROPE)=0.975, 95% HDI [+0.10, +2.00pp]）和 CLS-TRAJ 不确定性（P(ROPE)=0.542, inconclusive）；(c) Abstract \"not confirmed after multiple comparison correction\" 准确审慎。R1 称为\"教科书级处理\"，R2 同意。TOST + Bayesian ROPE 双框架的一致性显著增强了证据质量。\n\n**[R8-M2] RESOLVED** — Logistic regression robustness ✅\nAppendix M 补充 GEE logistic regression（binomial family, exchangeable correlation, robust sandwich SEs）。CWM×repo interaction OR=0.31 (0.15, 0.65), p=0.002，与 LPM 一致。Model identity LPM (p=0.002) vs GEE (p=0.410) 差异透明披露——commit 0b38a2b 修正了过强显著性声明。Primary effects 在两种框架下均 robust。\n\n**[R6-M3] RESOLVED** — Figure y-axis ✅\nFigure 2 y-axis 非零起始，caption 标注 \"y-axis does not start at zero\"。两位 Reviewer 均确认：对 0-3pp 差异展示，非零起始合理且有标注。Figure 3 (Appendix) 也已标注。\n\n### STILL_OPEN / WONT_FIX（Inherent Limitation）\n\n**[R6-N4] WONT_FIX** — Novelty ceiling（inherent）\nR2 标 STILL_OPEN（改善但核心贡献类型未变），R1 AGREE on assessment。所有可行 action items 已完成：routing 实验（negative result）、Bayesian ROPE、14B 验证。Excitement 从 2.5 提升至 3.0，但核心贡献类型（empirical comparison of existing formulations）是 inherent limitation，无法通过进一步修改解决。标记为 wont_fix。\n\n**[R8-W7] WONT_FIX** — Conference-level excitement（合并至 R6-N4）\n\n---\n\n## 新发现的问题\n\n### Minor（3 个，两位 Reviewer 共识）\n\n**[R11-M1] Figure 2 中 14B 单 seed 视觉权重**\nR1 提出，R2 AGREE。14B 数据点与多 seed 的 4B/8B 数据点在图中视觉等权，读者快速浏览可能过度解读 gap reversal (CWM 89.26% vs CLS 89.21%)。建议在 14B 数据点加星号/虚线或图内 \"n=1\" 标注。\n\n**[R11-M2] §3.5 LPM vs GEE model identity 不一致需 qualifier**\nR1 提出，R2 AGREE。§3.5 引用 LPM model identity 效应 (p=0.001)，但 Appendix M 的 GEE 给出 p=0.410——从\"高度显著\"到\"完全不显著\"。建议加 qualifier：\"model identity reaches significance under LPM but not under GEE logistic regression (Appendix M); this effect is specification-dependent.\"\n\n**[R11-M3] Abstract \"motivate routing\" 需限定**\nR2 提出，R1 AGREE。Abstract \"motivate complexity-aware formulation routing\" 暗示 routing 有前景，但 §3.6 报告 simple routing capture <0.4pp of oracle gap。建议改为 \"motivate **learned** complexity-aware routing\" 或加半句限定。\n\n### 分歧记录\n\n**R2-NEW-2（Abstract \"not confirmed\" 精确性）**：R2 担心可能被误读为 \"disconfirmed\"，R1 REBUT——\"not confirmed\" 是统计标准用语，上下文和 Bayesian ROPE 提供消歧。Director 裁定：R1 REBUT 成立，不构成 actionable issue。\n\n---\n\n## Strengths（延续上轮 + 本轮新增）\n\n**S1. 统计方法论达到 NLP 领域顶级水平。** TOST + Bayesian ROPE 双框架、ICC-clustered bootstrap、Holm-Bonferroni、GEE robustness check、transparent power analysis——在 NLP empirical papers 中极为罕见。[R1-S2, R2-S1 共识，本轮进一步强化]\n\n**S2. Claim calibration 系统性改善。** 从上轮的\"偶有 overclaim\"提升至\"系统性 well-calibrated\"：exploratory/confirmatory 区分清晰，≤8B 限定一致，TRAJ 措辞审慎，14B 标注恰当。[R2 Framing 一致性检查全部通过]\n\n**S3. 14B capacity-dependent convergence 是有意义的新 insight。** CLS-CWM gap 从 2.62pp (8B) 收窄至 -0.05pp (14B) 暗示 CWM 退化是 capacity-dependent 而非 formulation-inherent——对社区的 resource allocation 有前瞻价值。虽为 single seed / exploratory，但标注恰当。[R2 认为这是本轮最有价值的新增]\n\n**S4. 负结果文档化增加分析深度。** Routing heuristic negative result（<0.4pp of oracle gap）将未验证假设转化为文档化实验结论，比\"future work\"声明更有价值。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（无）\n\n本轮无新增 Must-Fix。所有上轮 tracked CRITICAL issues 均已 RESOLVED 或标记为 inherent limitation (wont_fix)。\n\n### Should-Fix（无新增）\n\n上轮 Should-Fix 均已 RESOLVED。\n\n### Minor（3 个，均为 consensus）\n\nR11-M1, R11-M2, R11-M3（见上文\"新发现的问题\"）。均为低成本 polish 级修改。\n\n---\n\n## Missing References\n\n本轮未发现新的遗漏引用。上轮要求的 CodeRM (Ma et al., ACL 2025) 和 ORM/PRM 映射已在 Related Work 中加入。Kruschke (2013, 2018) 和 Cohen (1988) 正确引用于 Bayesian ROPE 和 power analysis。\n\n---\n\n## External Review\n\n未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查完成（0 critical, 1 warning, 7 info）：\n\n- **[WARNING]** p.24 附录最后一页仅约 14 行（<20% 页面），大面积空白。建议紧凑化或合并。\n- **[INFO]** p.1-2 无 display item，Figure 1 在 p.3 出现（可接受但非最优）。\n- **[INFO]** p.7 Figure 2 y-axis 非零开始，caption 已标注——与 Reviewer 评估一致。\n- **[INFO]** p.8 最后一页极度紧凑（Related Work 续段 + Conclusion + Limitations），reviewer 可能觉得 conclusion 仓促。\n- **[INFO]** p.6 双表格密度较高但未溢出。\n- **[INFO]** p.12 ARR Checklist 在 PDF 中——按用户规则应在 OpenReview form 填写。需确认当前投稿要求。\n- **[INFO]** p.13 Figure 3 单色柱状图，caption 清晰。\n- **[INFO]** p.15 高密度页面但无溢出。\n\n---\n\n## Overall Assessment\n\n### 分项评分\n\n| 维度 | R1 Round 10 | R1 Round 11 | R2 Round 10 | R2 Round 11 | 共识 |\n|------|------------|------------|------------|------------|------|\n| Soundness | 3/5 | **4/5** | 3.5/5 | **4/5** | **4/5** ✅ |\n| Excitement | 3/5 | 3/5 | 2.5/5 | **3/5** | **3/5** ✅ |\n| Reproducibility | 4/5 | 4/5 | — | — | 4/5 |\n| Overall | 3.5 | 3.5 | 3.0 | 3.0 | **见下** |\n| Confidence | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 |\n\n### Overall 评分分歧与裁定\n\n**R1: 3.5 (Borderline Conference)** — 理由：Soundness 3→4 是实质性改善；方法论严谨性本身构成 methodological demonstration value；exceptional soundness 应部分补偿 moderate excitement。引用 Dodge et al. (2019), Card et al. (2020) 等方法论贡献论文作为 precedent。\n\n**R2: 3.0 (Findings)** — 理由：ARR 将 soundness 和 excitement 分开评分是有原因的；soundness 4/5 已充分反映方法论贡献；excitement ceiling（比较已有方法）无法被 soundness 跨维度补偿。Findings 定位恰好匹配。\n\n**Director 裁定：Overall 3.0 (Findings)**\n\nR2 的论点更符合 ARR 评分体系设计：soundness 和 excitement 是独立维度，exceptional soundness 已在 Soundness 4/5 中得到反映，不应 double-count 到 Overall。论文的方法论严谨性是 NLP 领域的示范，但核心贡献类型（empirical comparison without new methods）限制了 excitement。Findings track 是这篇论文的正确归属。\n\nR1 的 3.5 评估是可辩护的——如果 AC 对 empirical comparison papers 有更高的包容度，或认为方法论示范价值有独立 excitement，则 Borderline Conference 成立。两个分数都在合理范围内。\n\n### 与上轮对比\n\n| | Round 10 (Fresh) | Round 11 (Continue) | 变化 |\n|---|---|---|---|\n| 所有 tracked issues resolved | 6 open/in_progress | 0 open（+ 3 新 MINOR） | ✅ 全部解决 |\n| Soundness | 3-3.5/5 | **4/5 共识** | ↑ 显著提升 |\n| Excitement | 2.5-3/5 | **3/5 共识** | ↑ 小幅提升 |\n| Overall | 3.0 | **3.0** | = 维持 |\n\n**修订质量评价**：优秀。所有 tracked issues 均得到充分回应，无一敷衍。Bayesian ROPE、GEE robustness、transparent power analysis 等修改展现了高水平的方法论能力。新增的 3 个 MINOR 问题均为 polish 级别，不影响论文的核心质量。\n\n### 建议定位\n\n**推荐 Findings 接收**。论文在 soundness 维度达到 NLP 领域高水平（TOST + Bayesian ROPE + GEE + ICC + Holm-Bonferroni），failure mode taxonomy 和 14B convergence insight 有实用价值。Excitement 限制为 inherent（贡献类型为 empirical comparison），不影响 Findings 的合格性。\n\n---\n\n## Detailed Comments\n\n### 给作者的修改建议（按优先级）\n\n1. **[R11-M1]** Figure 2 中 14B 数据点加视觉区分（星号/虚线/图内 \"n=1\"），避免 gap reversal 被过度解读。\n2. **[R11-M2]** §3.5 model identity 效应加 LPM vs GEE qualifier（\"specification-dependent\"），保持与 Appendix M 的 claim 强度一致。\n3. **[R11-M3]** Abstract \"motivate routing\" 改为 \"motivate **learned** complexity-aware routing\" 或加限定半句。\n4. **[视觉]** p.24 空白页紧凑化。\n5. **[视觉]** 确认 ARR Checklist 是否应在 PDF 中还是仅在 OpenReview form 中。\n\n### 无需修改的确认\n\n- Abstract ≤8B 限定、TRAJ 措辞、Conclusion 限定、14B exploratory 标注、variant-level exploratory 标注——全部通过 framing 一致性检查。\n- Limitations 覆盖充分（Python-only、≤8B LoRA、synthetic mutation）。\n- 格式合规（8 页正文 + 不计入限制的 Limitations）。",
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-23T03:17:52.989124+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3914
}
```

</details>

---


### Assistant

_source line 906 · 2026-05-23T03:18:03.335891+00:00_

Round 9 继续审稿完成。报告已投递给 Research Director。

**核心结论**：

- **Issue Tracker**: 上轮 4 个 open/in_progress issue 全部 RESOLVED（R6-N1 exploratory 标注、R8-W1 TOST power + Bayesian ROPE、R8-M2 GEE logistic regression、R6-M3 Figure y-axis）。R6-N4/R8-W7（novelty ceiling）标记为 wont_fix（inherent limitation）。
- **新发现**: 3 个 MINOR（Figure 2 14B 视觉权重、LPM vs GEE qualifier、Abstract routing 措辞），均为 polish 级别。
- **评分共识**: Soundness 4/5, Excitement 3/5。Overall 分歧 R1=3.5 vs R2=3.0，Director 裁定 **3.0 (Findings)**。
- **修订质量**: 优秀。Bayesian ROPE 双框架、GEE robustness、transparent power analysis 展现高水平方法论能力。推荐 Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 82

## Round 82

2 recorded events


### User

_source line 907 · 2026-05-23T03:18:06.013439+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心分歧仅在 Overall 0.5 分（3.0 vs 3.5）——我与 R1 在 Soundness (4/5) 和 Excitement (3/5) 上完全一致，分歧在于方法论严谨度能否跨维度弥补 novelty 不足。

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

_source line 908 · 2026-05-23T03:18:18.487203+00:00_

交叉回应已在之前收到并纳入最终报告。报告已于上一步提交（Overall 3.0, Findings），Issue tracker 已同步更新。本轮审稿流程完成。

**本轮结果摘要**：
- 4 个 tracked issues 全部 RESOLVED（R6-N1, R8-W1, R8-M2, R6-M3）
- 2 个 inherent limitation 标记 wont_fix（R6-N4, R8-W7 — novelty ceiling）
- 3 个新 MINOR 问题（Figure 2 14B 视觉区分、LPM vs GEE qualifier、Abstract routing 措辞）
- Soundness 4/5（共识），Excitement 3/5（共识），Overall 3.0（Findings）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 83

## Round 83

52 recorded events


### User

_source line 909 · 2026-05-23T08:59:06.951785+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 未提供，请自行调研
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

_source line 910 · 2026-05-23T08:59:17.264927+00:00_

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

_source line 911 · 2026-05-23T08:59:17.316276+00:00_

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

_source line 912 · 2026-05-23T08:59:23.193756+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,WebSearch",
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
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-23T08:59:23.244436+00:00_



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

_source line 914 · 2026-05-23T08:59:27.409965+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
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
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 915 · 2026-05-23T08:59:27.460666+00:00_

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

_source line 916 · 2026-05-23T08:59:31.124502+00:00_

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

_source line 917 · 2026-05-23T08:59:31.175196+00:00_



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

_source line 918 · 2026-05-23T08:59:34.037828+00:00_

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

_source line 919 · 2026-05-23T08:59:34.891123+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (263 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D13
…[truncated 1817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-23T08:59:34.941980+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR site:aclweb.org"
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
    "query": "EMNLP 2026 call for papers submission deadline ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 921 · 2026-05-23T08:59:36.096528+00:00_

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

_source line 922 · 2026-05-23T08:59:36.147178+00:00_

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
56	\begin{figure}[t]
57	\centering
58	\includegraphics[width=\columnwidth]{figures/paper/figure2_v3.pdf}
59	\caption{Function-level accuracy scaling (4B--14B). CLS and CWM accuracy with shaded gap region. The \cls{}--\cwm{} gap follows an inverted-U trajectory: 1.32\pp{} at 4B, widening to 2.62\pp{} at 8B, then narrowing to 0.43\p
…[truncated 304 chars]

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

_source line 923 · 2026-05-23T08:59:39.058911+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"MRL Workshop at EMNLP 2025: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/mrl-workshop-emnlp-2025-first-call-papers"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information about EMNLP 2026 workshop submissions with ARR deadlines. While the search results don't show a specific main EMNLP 2026 Call for Papers, they do contain A
…[truncated 682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 4116
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-23T08:59:43.727742+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference ARR submission deadline commitment"
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
    "query": "EMNLP 2026 main conference ARR submission deadline commitment"
  }
}
```

</details>

---


### Tool call

_source line 925 · 2026-05-23T08:59:44.129660+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ARR 2026\" submission cycle deadline June July"
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
    "query": "\"ARR 2026\" submission cycle deadline June July"
  }
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-23T08:59:45.988232+00:00_

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

_source line 927 · 2026-05-23T08:59:46.942190+00:00_

1	\begin{abstract}
2	LLM-based program repair increasingly leverages test-time compute scaling, generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares these formulations under matched conditions.
3	
4	We present the first systematic comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is model-dependent and not confirmed after multiple comparison correction. At repository level, a significant interaction ($z{=}-23.7$, DeepSeek-Coder) confirms this equivalence collapses: the \cls{}--\cwm{} gap widens to 18--26\pp{} across 2--3 seeds per model under our ${\leq}$8B LoRA protocol in variant-level evaluation, driven by format collapse in generation-based simulation. Gap magnitude depends on multiple confounds. At 14B (3 seeds), the function-level gap narrows to 0.43\pp{} (TOST $p{=}0.0006$), consistent with capacity-dependent convergence.
5	
6	Error complementarity and a failure mode taxonomy motivate future work on complexity-aware formulation routing, though simple heuristics capture $<$0.4\pp{} of oracle advantage.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-23T08:59:46.942550+00:00_

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

_source line 929 · 2026-05-23T08:59:47.043225+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. This connects to a broader pattern in NLP: task formulation---classification vs.\ generation vs.\ span extraction---systematically affects performance~\cite{raffel2020t5}, but the conditions under which each wins remain task-dependent and empirically unresolved. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We pres
…[truncated 2646 chars]

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

_source line 930 · 2026-05-23T08:59:47.094067+00:00_

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

_source line 931 · 2026-05-23T08:59:47.094591+00:00_

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
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation
…[truncated 3353 chars]

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


### Tool result

_source line 932 · 2026-05-23T08:59:48.450758+00:00_

Web search results for query: ""ARR 2026" submission cycle deadline June July"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ARR 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=arr2601"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"}]

Based on the search results, here's what I found about ARR 2026 submission cycle deadlines:

The ACL Peer Review Committee recommended switching to 10-week cycles, with the new schedule starting in May 2025. This means that instead of 6 cycles a year there will generally be 5, but with more reasonable timelines for the review tasks and author response.

While the search results confirm that ARR has transitioned to 10-week review cycles, the specific submission deadline dates for the June/July 2026 ARR cycle are not clearly detailed in the search results I found. The results mention that from October 2022 to February 2025, ARR ran 8-week review cycles, with submission deadlines on the 15th of every second month, but the exact schedule for 2026 with the new 10-week cycle structure would be best found directly on the official ARR website at aclrollingreview.org/dates for the most current and complete information.


REMINDER: You MUST include t
…[truncated 72 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 4321
}
```

</details>

---


### Tool result

_source line 933 · 2026-05-23T08:59:49.405602+00:00_

Web search results for query: "EMNLP 2026 main conference ARR submission deadline commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here is the key information about EMNLP 2026 ARR submission deadline and commitment:

## Important Deadlines

The ARR submission deadline for long and short papers is May 25, 2026, with a reviewer registration deadline for all authors on May 27, 2026. The EMNLP commitment deadline is August 2, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Commitment Policy

For the ARR 2026 May cycle, authors must explicitly declare which conference they intend t
…[truncated 681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 5677
}
```

</details>

---


### Tool call

_source line 934 · 2026-05-23T08:59:58.657284+00:00_

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

_source line 935 · 2026-05-23T08:59:58.759359+00:00_

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
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss because repo-level execution traces often exceed the 2,048-token sequence length limit; after truncation, many samples have all target tokens removed (labels entirely $-$100), producing degenerate loss---a formulation-inherent weakness that classification and trajectory formulations avoid by design. NaN loss defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency chec
…[truncated 19293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-23T08:59:58.759891+00:00_

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

_source line 937 · 2026-05-23T08:59:59.262730+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. CodeScaler~\cite{zhu2026codescaler} trains execution-free reward models for both RL and test-time scaling. Verification formulations span trajectory-level reward~\cite{shum2025swerm}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. GenRM~\cite{hosseini2025genrm} and GenPRM~\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formula
…[truncated 1607 chars]

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

_source line 938 · 2026-05-23T08:59:59.263241+00:00_

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

_source line 939 · 2026-05-23T08:59:59.765368+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} equivalence is not confirmed after multiple comparison correction. Per-test classification achieves 217$\times$ higher throughput while providing diagnostic signal. Complementary errors (oracle: 90.63\%/95.83\%; single-seed) motivate complexity-aware routing. At repository level under ${\leq}$8B LoRA, divergence reaches 18--26\pp{} ($z{=}-23.7$, 2--3 seeds per model), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}). Three failure modes (format collapse, decision collapse, aggregation penalty) are consistent across families. \cls{} is recommended primarily for its throughput advantage and diagnostic capability; the accuracy advantage over \traj{} is directional but underpowered ($n{=}48$, MDE${\approx}$25\pp{}; Appendix~\ref{app:power}). Primary statistical findings are established under ${\leq}$8B LoRA fine-tuning. 14B results (3 seeds) corroborate function-level convergence (gap 0.43\pp{}, TOST $p{=}0.0006$), consistent with capacity-dependent scaling; whether this extends to repo level remains open.
5	
6	Three directions follow: (1)~oracle gains motivate complexity-aware routing using the failure mode taxonomy as routing features; (2)~the semantic generation bottleneck (four interventions fail; Appendix~\ref{app:extended_analysis}(g)) suggests capacity scaling or execution trace pretraining~\cite{meta2025cwm} is needed---testing at 32B+ would resolve the primary open question; (3)~larger-scale evaluation of per-test diagnostics for downstream repair ($n{=}44$ in our pilot) would test whether \cls{}'s throughput advantage extends to repair pipelines.
7	
8	\section*{Limitations}
9	
10	Primary findings use ${\leq
…[truncated 557 chars]

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

_source line 940 · 2026-05-23T08:59:59.765915+00:00_

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

_source line 941 · 2026-05-23T09:00:00.068004+00:00_

1	\appendix
2	
3	\noindent\textbf{Appendix overview.} A: Oracle resolve advantage. B: Ablation studies. C-F: Extended analysis (error complementarity, parseable accuracy, forced parsing, qualitative errors, failed interventions, mutation scaling, inference efficiency, re-repair, chain-of-thought). G: TOST sensitivity. G$'$: Bayesian ROPE. H: Effect sizes. I: Holm-Bonferroni. J: Mixed-effects regression. K: Parseable bias. L: CWM convergence. M: Few-shot. N: Threats. O: Downsample. P: Limitations.
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
34	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.
…[truncated 55692 chars]

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


### Tool call

_source line 942 · 2026-05-23T09:00:09.021905+00:00_

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

_source line 943 · 2026-05-23T09:00:09.022499+00:00_

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
…[truncated 22457 chars]

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

_source line 944 · 2026-05-23T09:00:10.026477+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "decisions.yaml",
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
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 945 · 2026-05-23T09:00:10.277953+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml\", \"content\": \"_next_id: 169\\ndecisions:\\n- id: D001\\n  date: 2026-05-11 18:01 UTC\\n  summary: 'MVP 方案: Monte Carlo oracle 模拟 + 函数级 pilot，不依赖 Docker 基础设施'\\n  rationale: '完整 Part 1 需要 Docker 重新评估 8K 个 patch 获取 per-test labels（16-24h），基础设施搭建成本高。MVP\\n    改用 Monte Carlo 模拟参数化真实测试数分布验证理论信息增益，函数级 pilot (HumanEval/MBPP) 验证可学习性。两者均无需 Docker，2-3\\n    天可完成。Pass 标准: per-test 在 70-85% 精度下 resolve rate 比 trajectory-level 高 ≥5%; 函数级\\n    pilot 精度 >70%。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-11 19:07 UTC\\n  summary: MVP-A 有条件通过：F2P-only block-corr 10.88%>5%；需补跑 Total(F2P+P2P) 模拟确认全图\\n  rationale: 真实 SWE-bench F2P median=1（69% 实例仅 1 个 F2P 测试），但 P2P median=50.5。F2P-only\\n    下 per-test 优势收窄但仍过阈值（block-corr 10.88%）。P2P regression 检测是更大的信号源——Total 分布(median=52)下优势预期更强。研究方向需校准：per-test\\n    价值主要来自 P2P regression 检测 + F2P multi-test 精确定位，而非单纯的 F2P 粒度。\\n  related_experiments:\\n  - exp_id: mvp-a-oracle-sim\\n    role: evidence\\n    result: F2P-only block-corr advantage 10.88%, i.i.d. 1.98%\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-11 19:38 UTC\\n  summary: P2P regression rate 是项目关键前提——≥10% per-test 有效，<5% 则有害；需实测\\n  rationale: Total 模拟(F2P+P2P)显示 per-test 优势强烈依赖 P2P regression rate：5% 时优势为负(-1%)，10%\\n    时 13.2%，20% 时 35.7%。这是从 F2P-only 分析未发现的关键变量。真实 regression rate 未知，需从 SWE-bench\\n    数据/文献中实测。此数据点决定项目是否可行及论文 story 如何构建。\\n  related_experiments:\\n  - exp_id: mvp-a-oracle-sim\\n    role: evidence\\n    result: 'Total sim: reg=5% adv=-1%, reg=10% adv=13.2%, reg=20% adv=35.7%'\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-11 20:05 UTC\\n  summary: P2P 回归率 ~1%，原始 Total 优势前提不成立；项目 reframe 而非 kill\\n  rationale: P2P 回归率 ~1%（mean=1.04%, median=0%, 仅 22.6% 错误 patch 破坏任何 P2P 测试），远低于\\n    per-test 有效的 10% 阈值。Total(F2P+P2P) 模型下 per-test 实际有害（噪声>信号）。但项目核心价值不在信
…[truncated 1464 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-23T09:00:10.328571+00:00_

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

_source line 947 · 2026-05-23T09:00:10.580443+00:00_

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
12	  last_seen_round: 11
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
32	  action_items:
33	    - round: 6
34	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
35	      assigned_to: "paper"
36	      status: resolved
37	    - round: 9
38	      action: "正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive"
39	      assigned_to: "paper"
40	      status: resolved
41	  resolution: "§3.5 开头标注 'Variant-level comparisons (n=48) are explo
…[truncated 30340 chars]

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

_source line 948 · 2026-05-23T09:00:22.497874+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "paper_checklist.yaml",
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
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-23T09:00:22.599669+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'exec-sim-repair-verifier'.\", \"metadata\": {}}"}

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

_source line 950 · 2026-05-23T09:00:22.600078+00:00_

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

_source line 951 · 2026-05-23T09:00:22.700703+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-23T09:00:30.048290+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org call for papers page limit formatting guidelines"
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
    "query": "site:2026.emnlp.org call for papers page limit formatting guidelines"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-23T09:00:38.132182+00:00_

Web search results for query: "site:2026.emnlp.org call for papers page limit formatting guidelines"

Links: [{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"}]

I found search results for EMNLP 2026, but the snippets don't include the specific page limit and formatting guidelines you're looking for. Let me search more specifically for that information on the main conference papers page.

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on my web search results, here's what I found about EMNLP 2026 call for papers page limits and formatting guidelines:

## Page Limits

Long papers can be up to 8 pages of content plus unlimited references, while short papers can be up to 4 pages of content plus unlimited references. Final versions of accepted papers will be given one ad
…[truncated 683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 8083
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-23T09:01:42.817054+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "你负责 **方法严谨性 + 实验设计 + 统计分析**。\n\n## Venue 信息\n- **EMNLP 2026** via ARR (double-blind)\n- ARR 提交截止：2026-05-25\n- Long paper：正文 ≤ 8 页 + 无限引用页\n- ACL 模板 (`\\usepackage[review]{acl}`)\n- Mandatory Limitations section（不计入页数）\n- ARR Checklist 在 OpenReview 表单填写，不在 PDF 中\n\n## 论文文件\n- LaTeX 源：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_10/submitted.pdf`\n\n## 审查侧重\n\n1. **实验设计合理性**：\n   - 三种 formulation (CLS/CWM/TRAJ) 的对比是否在 matched conditions 下进行？是否有系统性偏差？\n   - 数据集构建（function-level HumanEval+MBPP mutations, repo-level SWE-bench Verified mutants）的合理性\n   - seed 覆盖（5 seeds function-level, 2-3 seeds repo-level）是否充分？\n   - checkpoint 选择策略（val-based vs final epoch）是否引入系统偏差？\n   - CWM baseline 是否过弱（≤8B LoRA vs 原始 32B+mid-training）？这对结论的影响有多大？\n\n2. **统计方法**：\n   - TOST 等价检验：±2pp SESOI 是否合理？a priori vs post-hoc 问题\n   - Holm-Bonferroni 多重比较校正是否充分？\n   - Clustered bootstrap 实施（114 problem clusters, 10K resamples）\n   - Mixed-effects LPM vs GEE logistic regression 的一致性和分歧\n   - Bayesian ROPE 分析的可靠性\n   - 统计功效（n_eff ≈ 86, power ~0.3）对结论的影响\n\n3. **Threats to validity**：\n   - 五个潜在 confound 的评估是否充分？\n   - Repo-level variant n=48 的 MDE≈25pp 限制\n   - NF4 vs bfloat16 混合精度的影响\n   - 评估 sequence length 不一致问题\n\n4. **可重复性**：\n   - Hyperparameters 是否完整报告？\n   - Compute budget 是否报告？\n   - 数据集构建细节是否充分？\n\n请按标准 ARR 审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（用 EMNLP 2026 ARR 评分标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
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
    "text": "你负责 **方法严谨性 + 实验设计 + 统计分析**。\n\n## Venue 信息\n- **EMNLP 2026** via ARR (double-blind)\n- ARR 提交截止：2026-05-25\n- Long paper：正文 ≤ 8 页 + 无限引用页\n- ACL 模板 (`\\usepackage[review]{acl}`)\n- Mandatory Limitations section（不计入页数）\n- ARR Checklist 在 OpenReview 表单填写，不在 PDF 中\n\n## 论文文件\n- LaTeX 源：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_10/submitted.pdf`\n\n## 审查侧重\n\n1. **实验设计合理性**：\n   - 三种 formulation (CLS/CWM/TRAJ) 的对比是否在 matched conditions 下进行？是否有系统性偏差？\n   - 数据集构建（function-level HumanEval+MBPP mutations, repo-level SWE-bench Verified mutants）的合理性\n   - seed 覆盖（5 seeds function-level, 2-3 seeds repo-level）是否充分？\n   - checkpoint 选择策略（val-based vs final epoch）是否引入系统偏差？\n   - CWM baseline 是否过弱（≤8B LoRA vs 原始 32B+mid-training）？这对结论的影响有多大？\n\n2. **统计方法**：\n   - TOST 等价检验：±2pp SESOI 是否合理？a priori vs post-hoc 问题\n   - Holm-Bonferroni 多重比较校正是否充分？\n   - Clustered bootstrap 实施（114 problem clusters, 10K resamples）\n   - Mixed-effects LPM vs GEE logistic regression 的一致性和分歧\n   - Bayesian ROPE 分析的可靠性\n   - 统计功效（n_eff ≈ 86, power ~0.3）对结论的影响\n\n3. **Threats to validity**：\n   - 五个潜在 confound 的评估是否充分？\n   - Repo-level variant n=48 的 MDE≈25pp 限制\n   - NF4 vs bfloat16 混合精度的影响\n   - 评估 sequence length 不一致问题\n\n4. **可重复性**：\n   - Hyperparameters 是否完整报告？\n   - Compute budget 是否报告？\n   - 数据集构建细节是否充分？\n\n请按标准 ARR 审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（用 EMNLP 2026 ARR 评分标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
  }
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-23T09:01:58.788403+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15971
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-23T09:01:59.192063+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "你负责 **新颖性 + 相关工作完整性 + 写作质量 + 格式合规**。\n\n## Venue 信息\n- **EMNLP 2026** via ARR (double-blind)\n- ARR 提交截止：2026-05-25\n- Long paper：正文 ≤ 8 页 + 无限引用页\n- ACL 模板 (`\\usepackage[review]{acl}`)\n- Mandatory Limitations section（不计入页数）\n- ARR Checklist 在 OpenReview 表单填写，不在 PDF 中\n\n## 论文文件\n- LaTeX 源：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_10/submitted.pdf`\n\n## 审查侧重\n\n1. **新颖性评估**：\n   - 核心贡献是否足够 EMNLP main conference？还是更适合 Findings？\n   - 三种 formulation (CLS/CWM/TRAJ) 均为已有方法——比较研究本身的贡献价值\n   - Function-level equivalence 发现是否 surprising？是否可从直觉预期？\n   - Repo-level divergence 是否提供了非平凡的 insight？\n   - Failure mode taxonomy 和 error complementarity 的独立贡献\n   - 与 GenRM (Hosseini et al., ICLR 2025) 的结论差异是否充分讨论（generation advantage 在 code 领域不成立）？\n\n2. **相关工作完整性**：\n   - 是否遗漏重要相关工作？特别是：\n     - 最近的 code reward model 工作\n     - Execution simulation / code world model 工作\n     - Process vs outcome supervision 工作\n     - Task reformulation (T5 style) 在 code 领域的应用\n   - 引用是否真实可验证（无幻觉引用）？\n   - Related Work section 的组织是否合理？\n\n3. **写作质量**：\n   - Abstract 是否自洽、准确反映正文内容？\n   - Introduction 的 motivation 和 story 是否清晰？\n   - 贡献声明是否过度（overclaim）或不足？\n   - 术语使用是否一致？\n   - 叙事流畅度和段落组织\n   - Limitations section 是否符合 EMNLP 要求（简短、覆盖 3 个点左右）？\n\n4. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - ACL 模板使用是否正确？\n   - 匿名性：是否有去匿名化线索？\n   - Table/Figure 的质量和信息密度\n   - Appendix 组织是否合理？\n   - Limitations 是否在正文中（不在 appendix）？\n   - 是否只有一个 Limitations section？\n\n请按标准 ARR 审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（用 EMNLP 2026 ARR 评分标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
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
    "text": "你负责 **新颖性 + 相关工作完整性 + 写作质量 + 格式合规**。\n\n## Venue 信息\n- **EMNLP 2026** via ARR (double-blind)\n- ARR 提交截止：2026-05-25\n- Long paper：正文 ≤ 8 页 + 无限引用页\n- ACL 模板 (`\\usepackage[review]{acl}`)\n- Mandatory Limitations section（不计入页数）\n- ARR Checklist 在 OpenReview 表单填写，不在 PDF 中\n\n## 论文文件\n- LaTeX 源：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_10/submitted.pdf`\n\n## 审查侧重\n\n1. **新颖性评估**：\n   - 核心贡献是否足够 EMNLP main conference？还是更适合 Findings？\n   - 三种 formulation (CLS/CWM/TRAJ) 均为已有方法——比较研究本身的贡献价值\n   - Function-level equivalence 发现是否 surprising？是否可从直觉预期？\n   - Repo-level divergence 是否提供了非平凡的 insight？\n   - Failure mode taxonomy 和 error complementarity 的独立贡献\n   - 与 GenRM (Hosseini et al., ICLR 2025) 的结论差异是否充分讨论（generation advantage 在 code 领域不成立）？\n\n2. **相关工作完整性**：\n   - 是否遗漏重要相关工作？特别是：\n     - 最近的 code reward model 工作\n     - Execution simulation / code world model 工作\n     - Process vs outcome supervision 工作\n     - Task reformulation (T5 style) 在 code 领域的应用\n   - 引用是否真实可验证（无幻觉引用）？\n   - Related Work section 的组织是否合理？\n\n3. **写作质量**：\n   - Abstract 是否自洽、准确反映正文内容？\n   - Introduction 的 motivation 和 story 是否清晰？\n   - 贡献声明是否过度（overclaim）或不足？\n   - 术语使用是否一致？\n   - 叙事流畅度和段落组织\n   - Limitations section 是否符合 EMNLP 要求（简短、覆盖 3 个点左右）？\n\n4. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - ACL 模板使用是否正确？\n   - 匿名性：是否有去匿名化线索？\n   - Table/Figure 的质量和信息密度\n   - Appendix 组织是否合理？\n   - Limitations 是否在正文中（不在 appendix）？\n   - 是否只有一个 Limitations section？\n\n请按标准 ARR 审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（用 EMNLP 2026 ARR 评分标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
  }
}
```

</details>

---


### Tool call

_source line 957 · 2026-05-23T09:02:00.098095+00:00_

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

_source line 958 · 2026-05-23T09:02:00.704980+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1512
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-23T09:02:02.436722+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2338
}
```

</details>

---


### Assistant

_source line 960 · 2026-05-23T09:02:12.191767+00:00_

Reviewer 1、Reviewer 2 和视觉审查 Agent 已并行启动。等待 Reviewer 返回初审结果。

Reviewer 1 侧重方法严谨性/实验设计/统计分析，Reviewer 2 侧重新颖性/相关工作/写作/格式。视觉审查 Agent 独立运行，不阻塞主流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 84

## Round 84

2 recorded events


### User

_source line 961 · 2026-05-23T09:07:19.567870+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（Round 1）

**论文标题**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
**Venue**: EMNLP 2026 via ACL ARR
**审查侧重**: 新颖性 + 相关工作完整性 + 写作质量 + 格式合规

---

## Summary

本文系统比较了三种 execution-free 代码修复验证 formulation：CLS（per-test 二分类）、CWM（执行输出生成）和 TRAJ（trajectory-level patch 评分）。在两个代码 LLM 系列（Qwen3、DeepSeek-Coder）、两个复杂度级别（function-level 和 repo-level）下，使用 ≤8B LoRA fine-tuning 进行匹配实验。主要发现：(1) function-level 下 CLS 和 CWM 统计等价（TOST p=0.007）；(2) repo-level 下 CWM 因 format collapse 退化 18-26pp；(3) 两种 formulation 存在部分互补的错误模式。论文还提供了 failure mode taxonomy 和 formulation 选择建议。

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 统计方法严谨的比较研究，但核心发现可预期性较高，CWM 比较受训练范式严重混淆，新颖洞见不足以达到主会议水平。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | Function-level 等价性结论有严格统计支撑；但 repo-level CWM 比较被训练范式差异严重混淆（≤8B LoRA vs 原始 CWM 32B + execution trace pretraining），论文虽承认但仍以此为核心 claim |
| Excitement | 2/5 (Potentially Interesting) | 三种 formulation 均为已有方法的比较；核心发现（generation 在长输出下退化）可从直觉/理论预期；GenRM 在代码领域失效的观察有价值但未被充分发展 |
| Reviewer Confidence | 4/5 | 熟悉 code verification、reward modeling、task reformulation 领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心发现可预期性高，新颖性不足以支撑 main conference

- 具体位置：Abstract, §1 Introduction 贡献声明, §2.2 Failure Modes 理论分析, §3.4 Repo-Level Results
- 问题：论文的两个核心发现——(1) function-level 下 CLS≈CWM，(2) repo-level 下 CWM 因 format collapse 大幅退化——都可从第一性原理直接预期。§2.2 的理论分析本身就预测了"short outputs minimize generation-specific failures"，这意味着 function-level 等价性几乎是 tautological：当输出仅 5-15 tokens 时，generation overhead 可忽略。Repo-level 下 CWM 的 format collapse（53-74% unparseable，平均 477 token 输出）同样符合"小模型生成长序列质量下降"的普遍认知。论文只测试了两个极端复杂度（function-level 5-15 tokens vs repo-level 477 tokens），缺少中间复杂度的数据来表征 transition boundary。
- 为什么影响接收：EMNLP main conference 期望至少一个 surprising 或 non-trivial 的发现。当论文自身的理论框架就能预测实验结果时，实验验证的价值降低为"confirming the obvious"。
- 建议修改方向：(a) 增加中间复杂度级别的实验，定位 formulation 等价性崩溃的精确边界；(b) 将 GenRM 对比发现（generation advantage 不迁移到代码领域）提升为主要贡献并深入分析原因；(c) 或者将 failure mode taxonomy 发展为独立的分析贡献而非附属发现。

**N2** [critical] CWM 比较的生态效度（ecological validity）存在根本性问题

- 具体位置：§3.1 Experimental Setup ("Our CWM baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model"), §3.7 Threats to Validity, Limitations section
- 问题：论文标题声称比较"verification formulations"，但 repo-level 的 CWM 结果被训练范式差异严重混淆。实际的 Code World Model (FAIR, 2025) 使用 32B 参数 + execution trace 中间训练，而本文的 CWM 仅使用 ≤8B LoRA fine-tuning，无任何 execution trace pretraining。论文在 §3.7 和 Limitations 中反复承认这一点（"all repo-level CWM conclusions are conditional on the ≤8B LoRA regime"），但 Abstract 和 Introduction 中的 claim 语气并未充分反映这一巨大限制。当 repo-level CWM format collapse（53-74% unparseable）很可能是模型容量和预训练缺失导致而非 formulation 的固有缺陷时，"formulation comparison"的标题和叙事就具有误导性。
- 为什么影响接收：如果核心差异来自训练范式而非 formulation 本身，那么论文的中心 claim（"complexity-moderated formulation choice"）就缺乏可靠基础。
- 建议修改方向：(a) 在 Abstract 和 Introduction 的贡献声明中加入更明确的限定（"under ≤8B LoRA without execution trace pretraining"），而不仅在正文细节处提及；(b) 最理想的是补充一个更大规模（如 32B）或有 execution trace pretraining 的 CWM 实验；(c) 如果无法补充实验，需要将论文重新框定为"≤8B LoRA 下的 formulation 比较"而非通用结论。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 统计细节过密，可读性差

- 具体位置：Abstract 全文
- 问题：Abstract 包含 z=−23.7、TOST p=0.0006、18-26pp 等大量统计数值。对于 EMNLP 的广泛读者群来说，这些数值降低了可读性。Abstract 应传达核心发现的 story 而非统计细节。例如 "TOST, 5 seeds" 这种表述对不熟悉等价性检验的读者毫无意义。
- 建议：保留 1-2 个最关键的数值（如 function-level gap < 2pp，repo-level gap 18-26pp），移除统计方法学细节到正文。

**W2** [warning] 贡献列表过少且框定过于谦虚

- 具体位置：§1 Introduction, contributions 列表（仅两条）
- 问题：论文仅列出两条贡献：(1) complexity-moderated formulation choice, (2) error complementarity。Failure mode taxonomy（§3.4 Table 4）作为独立的有价值发现，未被列为贡献。同时，论文将自身定位为"primarily methodological"（§1 第8行），这种框定虽然诚实但降低了论文的说服力。在投稿策略上，"methodological comparison"在 EMNLP main conference 的接受难度高于有 novel insights 的工作。
- 建议：将 failure mode taxonomy 提升为第三条贡献；重新框定论文核心价值，不仅是方法论比较，更是揭示了 generation advantage 的领域依赖性。

**W3** [warning] GenRM 对比发现未被充分讨论

- 具体位置：§4 Related Work ("the generative formulation (CWM) does not outperform the discriminative one (CLS), suggesting that the generation advantage may be domain-specific")
- 问题：Hosseini et al. (ICLR 2025) 的 GenRM 表明 generative verifier 在数学推理中优于 discriminative verifier。本文发现在代码验证中恰好相反。这是论文最有潜力成为 surprising finding 的地方，但仅在 Related Work 中用一段讨论。论文未深入分析为何 generation advantage 不迁移到代码领域（是因为代码验证的结构化输出？还是因为代码执行结果的确定性？还是仅仅因为训练规模差异？）。
- 建议：将此对比作为论文的核心 narrative thread 之一，在 Introduction 和 Discussion/Conclusion 中深入展开。排除训练范式差异后（如果可能），这可以成为一个 domain-specific insight。

**W4** [warning] 仅使用两个模型家族，泛化性受限

- 具体位置：§3.1 Experimental Setup
- 问题：仅测试 Qwen3 和 DeepSeek-Coder 两个家族。两者都是相似时代（2024-2025）的代码 LLM。缺少更多样的架构（如 CodeLlama/Llama-based、StarCoder、Gemma 等），削弱了"结论泛化至不同代码 LLM"的可信度。虽然论文将 DeepSeek-Coder 定位为"cross-model consistency check"（§3.1），但两个模型家族不足以建立 formulation-level 结论的通用性。
- 建议：至少增加一个额外的模型架构，或者在写作中更明确地限定泛化范围。

**W5** [warning] 种子数/实验配置不一致导致统计置信度参差不齐

- 具体位置：Table 1 (seeds 列), Table 3, §3.2-3.5 各小节
- 问题：不同实验配置使用不同数量的种子：function-level CLS/CWM 5 seeds, DeepSeek 2 seeds, repo-level 部分配置仅 1 seed（如 Qwen3-4B seed 42 单次）。14B 实验仅 3 seeds，且无 TRAJ 14B 数据。这导致不同 claim 的置信度差异很大，但论文未清晰标注哪些结论是 robust（多种子验证）vs exploratory（单种子）。
- 建议：在每个核心 claim 首次出现时标注种子覆盖度和对应的统计置信度。

---

## 小问题（不影响接收）

- Table 1 信息密度高，CLS/CWM/TRAJ 行间缺少视觉分隔
- Figure 2 在 column width 下偏小，y 轴范围窄使得视觉差异被放大
- Appendix 目录命名 (G, G', H...) 不够直观，G' 的 prime 符号容易混淆
- §2.2 "Formulation-Specific Failure Modes" 段落标题可能给读者造成困惑：这是 method section 还是 analysis preview？实际上这段是理论预测，但位于 method 内
- References 中 `wei2022emergent` 的 venue 写为 "Transactions on Machine Learning Research (TMLR)" 但 booktitle 格式与 inproceedings 类型不一致（TMLR 应为 article 类型）

---

## 相关工作完整性

**已覆盖的关键领域**：
- Execution simulation & verification：CWM, Self-Execution Simulation, CodeMind, CRUXEval, RepoExec ✓
- Code reward models：CodeScaler, CodePRM, FunPRM, DreamPRM-Code, CodeRL+ ✓
- Process vs outcome supervision：Lightman, GenRM, GenPRM, Math-Shepherd ✓
- Task reformulation：Raffel T5 ✓
- Code repair systems：SWE-bench, SWE-agent, Agentless ✓
- Predictive mutation testing：Tufano, Kim ✓
- Aletheia（training recipe comparison）✓

**潜在遗漏**：
- **CVeDRL (arXiv:2601.22803, 2026)**: Difficulty-aware RL 训练代码 verifier，与本文的 verification formulation 主题直接相关（虽然侧重 RL 训练而非 formulation 比较），建议在 Related Work 中提及
- Related Work 部分整体组织合理，三段式（Execution Simulation / Process vs Outcome / Repair & Task Framing）结构清晰

**引用真实性**：抽查的引用条目（meta2025cwm, hosseini2025genrm, shum2025swerm, maimon2026selfexecution, zhu2026codescaler, venkatkrishna2026aletheia 等）在 arXiv 和会议记录中可确认存在，未发现明显幻觉引用。

---

## 格式合规检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文 ≤ 8 页 | ✓ | 正文 + Limitations 在第 8 页内完成 |
| ACL 模板 (review mode) | ✓ | `\usepackage[review]{acl}` |
| 匿名性 | ✓ | Author: "Anonymous"，未发现去匿名化线索 |
| Limitations section | ✓ | 在正文内，单个 section，一段话覆盖 4 个点 |
| Limitations 不在 appendix | ✓ | 附录中 P 标为"Limitations"但实际标题为"Extended limitations"，本质是补充分析 |
| ARR Checklist | ✓ | 正确注释掉 PDF 中的 checklist，标注在 OpenReview 填写 |
| 引用页不限 | ✓ | References 占 2 页 |

**格式注意**：Appendix 长达 14 页（p9-p22），虽无格式违规但体量过大。核心问题是 Appendix P "Extended Limitations"（Appendix §O.threats 内的 `\paragraph{Extended limitations.}`，实际在 Appendix N 的末尾）——虽然标为 extended，但内容实质上是额外的 limitations 讨论（如单种子 4B 比较、mutation type 分布偏移、synthetic-to-real gap 等），存在被 reviewer 质疑为将 limitations 内容转移到 appendix 以规避正文空间限制的风险。

---

## 主要优势

1. **统计方法论严谨**：TOST 等价性检验、Holm-Bonferroni 校正、Bayesian ROPE 分析、clustered bootstrap、混合效应回归——方法论工具箱部署得当，为比较研究设立了良好的方法论标准
2. **Threats to Validity 分析详尽**：§3.7 和 Appendix N 系统识别了 5 个潜在混淆因素并逐一评估，自我批评程度超过多数投稿论文
3. **Failure mode taxonomy 有实用价值**：Table 4 的三类故障模式（format collapse、decision collapse、aggregation penalty）为从业者提供了可操作的诊断框架
4. **实验设计匹配度高**：控制了模型容量、训练数据、compute 等变量，在 ≤8B LoRA 范围内确实实现了 matched comparison
5. **写作诚实度高**：论文没有过度宣称，对自身局限性的讨论坦诚且具体

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

_source line 962 · 2026-05-23T09:07:38.925961+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 85

## Round 85

2 recorded events


### User

_source line 963 · 2026-05-23T09:07:41.521255+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.0 (Findings)，Soundness 3/5，Excitement 2/5。

两个 critical 问题：
1. **核心发现可预期性高**——function-level 等价性和 repo-level format collapse 均可从第一性原理预期，论文自身的 §2.2 理论分析就预测了实验结果，缺少中间复杂度数据和 surprising insight
2. **CWM 比较的生态效度不足**——≤8B LoRA fine-tuning 与原始 CWM（32B + execution trace pretraining）差距过大，repo-level 结论可能反映的是模型容量而非 formulation 差异，但标题和核心 claim 未充分体现这一限制

主要优势是统计方法论严谨、threats to validity 分析详尽、failure mode taxonomy 有实用价值。格式合规无问题。相关工作基本完整，引用未发现幻觉。

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

_source line 964 · 2026-05-23T09:07:51.968146+00:00_

Reviewer 2 审稿意见已收到。核心判断：Overall 3.0 (Findings)，两个 critical 问题聚焦在 novelty 可预期性和 CWM 生态效度。

等待 Reviewer 1 审稿意见提交后进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 86

## Round 86

6 recorded events


### User

_source line 965 · 2026-05-23T09:08:36.059762+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验设计 + 统计分析）

**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 研究问题重要、统计方法论扎实、限制性讨论诚实，但 CWM baseline 在 ≤8B LoRA 约束下被系统性削弱，repo-level 的核心发现（CLS >> CWM）在更高参数量下是否成立存疑；repo-level 统计功效不足（power ~0.3, n=48）限制了结论的稳健性。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计框架扎实（TOST+clustered bootstrap+Holm-Bonferroni+LPM/GEE+Bayesian ROPE），但核心实验设计存在系统性 confound（≤8B LoRA 对 CWM 不公平）；function-level 等价性结论可靠，repo-level 因果归因不充分 |
| Excitement | 3/5 | 填补 matched-condition 下 formulation 比较的空白，failure mode taxonomy 有实用价值，但本质是比较性实证研究，无方法创新；repo-level 结论的 generalizability 受限 |
| Reproducibility | 4/5 | Hyperparameters 完整（Table 11）、compute budget 明确（~370 GPU-hours）、prompt templates 提供、mutation operators 描述清晰；数据集基于公开 benchmark |
| Confidence | 4/5 | 我对该领域（代码修复验证、统计方法、实验设计）有较强背景 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] CWM baseline 公平性——核心方法论问题
- 具体位置：§3.1 (Models and training), §3.7 (Threats), Appendix N (CWM scale and pretraining)
- 问题：论文的最重要发现——CWM 在 repo-level 灾难性退化（18–26pp gap）——完全建立在 ≤8B LoRA fine-tuning 之上。CWM 需要生成 ~477 tokens/instance，而 CLS 仅需 1 token。在 ≤8B 参数量且无 execution-trace pretraining 的条件下，长文本生成质量退化是已知现象（Appendix H(g) 的四项干预全部失败进一步证实）。这实质上是在证明"小模型不能生成长且连贯的文本"，而非揭示 verification formulation 的本质差异。
  
  原始 CWM（FAIR CodeGen team, 2025）使用 32B 参数 + mid-training on execution traces，是一个根本不同的 training regime。论文虽在多处添加了"≤8B LoRA"限定词，但关键位置的 framing 仍过于宽泛：
  - Title "A Systematic Comparison of Execution-Free Verification Formulations" 暗示全面比较，但实际仅覆盖 ≤8B
  - Abstract 中 "formulation choice is moderated by code complexity" 未加限定
  - §2 contributions (2) "formulation choice is moderated by code complexity" 同样缺少限定

- 为什么影响接收：如果 repo-level 的核心发现是 model capacity 而非 formulation 的 artifact，则论文的主要贡献大幅缩水。14B 的 function-level 结果（CLS-CWM gap = 0.43pp, TOST p<0.0006）反而支持"在足够 capacity 下 CWM 可收敛"的假设。
- 建议修改方向：
  (a) Title 和 Abstract 中明确限定"under ≤8B LoRA fine-tuning"；
  (b) 在 §3.4 (Repo-Level) 正文中增加一段 explicit caveat，将 repo-level CWM 结论明确定位为 capacity-constrained regime 下的发现；
  (c) 如有可能，增加 14B CWM repo-level 的数据点（即使单 seed），以展示 gap 是否随 capacity 缩小

**N2** [critical] Repo-level CWM 使用严重过拟合的 checkpoint
- 具体位置：§3.1 (Datasets), Appendix N (CWM convergence analysis), Table 16
- 问题：所有 CWM repo-level 训练都产生 NaN validation loss，导致默认使用 final epoch checkpoint。Table 16 清楚显示 Qwen3-8B CWM eval loss 在 step 300–400 达到最小值，到 final epoch (step ~6600) 时 loss 已膨胀至 1.8× 最小值。然而论文使用的是这个严重过拟合的 checkpoint。

  论文声称"early-stopped checkpoints retain high unparseable rates, leaving the qualitative ranking unchanged"（Appendix N），但这一断言基于 DeepSeek-Coder（epoch 1 vs epoch 3: 75.45% vs 57.31%, unparseable rate 66.4%），而非 Qwen3。对于 Qwen3，论文明确说"No epoch-level checkpoint is available"，但又提到有 step 300/400 的 checkpoints。

  关键遗漏：论文有 Qwen3 CWM 在 optimal step (300–400) 的 checkpoints，但**未报告这些 checkpoints 的准确率**。DeepSeek 的 early stopping 数据显示 gap 从 ~27pp 缩小到 ~10pp（+18.14pp improvement），这暗示 Qwen3 的 optimal checkpoint 可能显著缩小 gap。
  
- 为什么影响接收：如果 CWM 在 optimal checkpoint 下的表现显著好于 final epoch，则 18–26pp gap 的很大一部分归因于 checkpoint selection 而非 formulation。这直接动摇核心结论。
- 建议修改方向：评估 Qwen3 CWM step-300/400 checkpoints 的 repo-level accuracy，并报告结果。如果 gap 显著缩小，需要修订结论。

**N3** [critical] 统计功效不足对等价性声明的影响讨论不够充分
- 具体位置：§3.4 (Statistical power), Appendix K (Variant-Level Effect Sizes)
- 问题：n_eff ≈ 86, TOST power ~0.3。这意味着即使 CLS-TRAJ 真的等价，也只有 30% 的概率检测到。论文正确指出"CLS-TRAJ non-confirmation may reflect insufficient power"（§3.4），但随后仍将 CLS-TRAJ 描述为"model-contingent"和"not confirmed"，暗示存在实质差异。

  具体地：Holm-Bonferroni 校正后 CLS-TRAJ 调整后 p=0.075（Table 15），Bayesian ROPE 给出 P(ROPE)=0.542（inconclusive）。这两个结果完全可以用 power ~0.3 解释，而不需要假设 TRAJ 真的劣于 CLS。

  更严重的是 repo-level 的 n=48 variants，MDE ≈ 25pp。这意味着 repo-level 只能检测到≥25pp 的巨大差异。CLS-TRAJ 的 gap <10pp 完全在检测盲区内。

- 为什么影响接收：论文在 function-level 对 CLS-CWM 和 CLS-TRAJ 给出了不对称的结论（一个等价，一个不确定），但这种不对称可能完全是 power 不足的 artifact。如果 power 足够，两者都可能被确认等价。
- 建议修改方向：
  (a) 正文中更明确讨论 power ~0.3 意味着 CLS-TRAJ 的"未确认"结论不应被解读为"非等价"；
  (b) 报告 CLS-TRAJ 等价性所需的最小样本量（a priori power analysis），让读者理解需要多少数据才能下结论；
  (c) 避免在 contribution list 中将"TRAJ parity is model-contingent"作为稳健结论呈现

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] ±2pp SESOI 选择的 a priori 性质存疑
- 具体位置：§3.4 (Statistics), Appendix G (TOST Margin Sensitivity)
- 问题：论文声称 ±2pp SESOI 是 "set a priori"（§3.4），引用 Lakens (2017) 和 Wellek (2010)。但 ±2pp 的具体数值对应 ~2–3 problems out of 114，"below practitioner-relevant differences"——这个推理 chain 是 post-hoc 的 justification 还是真正的 a priori 设定？没有 pre-registration 记录支持这一声明。
  
  TOST sensitivity analysis (Table 13) 显示最小等价 margin 为 ±1.52pp（p ≈ 0.05），距离选定的 ±2pp 仅 0.48pp。如果 SESOI 设为 ±1.5pp，CLS-CWM 等价性结论就不成立（p=0.054）。这暗示结论对 SESOI 选择较敏感。
  
- 建议：承认 SESOI 选择的主观性，增加 sensitivity analysis 的讨论权重（目前放在 Appendix G，建议在正文 §3.4 中引用并讨论 ±1.52pp 临界值）

**W2** [warning] 混合精度实验设计（NF4 + bfloat16 pooling）
- 具体位置：§3.1 (Models and training), §3.4 footnote, Appendix P
- 问题：5 个 seeds 中 3 个用 bfloat16，2 个用 NF4 quantization。论文在脚注中声称"function-level accuracy remains within seed noise across both precisions"，但：
  (a) 没有正式统计检验精度差异；
  (b) 限制到 bfloat16 only 时，CLS-CWM 仍然显著 (p<0.05) 但 CLS-TRAJ 不显著 (p=0.128)——这表明 NF4 seeds 对 CLS-TRAJ 结论有实质贡献（提供 precision 缩小 CI）；
  (c) NF4 quantization 在 repo-level（更长 generation）的影响未被评估
  
- 建议：(a) 在正文中明确报告 bfloat16-only 的 TOST 结果；(b) 讨论 NF4 精度对 CWM 长文本生成质量的潜在影响

**W3** [warning] Repo-level 数据处理不一致
- 具体位置：Appendix E (Data processing)
- 问题：DeepSeek CWM 用 `train_unified.py`（drop 超长样本，丢弃 4.8%），Qwen CWM 用 `train_repo_cwm.py`（truncate，保留全部）。这导致：
  - 训练步数不同（~12,627 vs ~13,266 for DeepSeek, ~6,633 for Qwen）
  - 不同 preprocessing 策略（DeepSeek CLS s42 用 drop, s123 用 truncate），产生 7.68pp accuracy spread (§3.7)
  
  更值得注意的是，preprocessing 选择与 checkpoint 选择策略耦合（truncate → NaN val loss → final epoch checkpoint），形成 confound chain。
  
- 建议：(a) 用统一 preprocessing 策略复现关键比较；或 (b) 在正文中更显著地报告这一 confound，而非仅放在 Appendix

**W4** [warning] CLS-TRAJ 训练条件不匹配
- 具体位置：§3.1, Appendix N (TRAJ training regime)
- 问题：TRAJ 使用根本不同的训练配置：~400 variant-level instances（vs ~70K per-test），lr = 2×10⁻⁴（vs 5×10⁻⁵），variant-level labels。论文在 Appendix N 中讨论了这一点，downsample ablation (80.74% vs 72.92%) 部分控制了 data volume，但**未控制 label granularity**（per-test vs variant-level）。
  
  这意味着 repo-level CLS-TRAJ 的比较不是 formulation-only 的比较，而是 formulation + training-regime 的联合比较。论文承认 "these are plausible confounds that cannot be separately controlled"，但在 contribution list 中仍然用 "formulation choice matters only at repo level" 的语言。
  
- 建议：在 contribution summary 中明确表述这一 confound

**W5** [warning] CLS-CWM paired comparison 使用不同 seeds
- 具体位置：Appendix K (Table 14)
- 问题：Repo-level CLS-CWM paired bootstrap comparison 使用 CLS s123 vs CWM s42（不同 seeds）。论文辩称 "the CI lower bound of 10.42pp far exceeds the seed noise observed in function-level experiments (<2pp)"，但 function-level seed noise 不能直接外推到 repo-level——repo-level 的 seed variance 可能大得多（e.g., DeepSeek CLS 两个 matched seeds 之间有 ±2.50 的 std）。
- 建议：报告同 seed 的 paired comparison（如果有 s42 的 CLS 和 CWM），或更明确讨论 cross-seed pairing 的局限性

---

## 小问题（不影响接收）

- §3.2 "At 8B, the ranking is CLS (89.94) > TRAJ (87.70) > CWM (87.33)" — 这三个数字基于不同 seed 数量（CLS/TRAJ: 2 seeds, CWM: 2 seeds at 8B），严格来说排名的置信度有限
- Table 1 caption: "Seeds 42/123/456: bfloat16; 789/0: NF4" — 但 Table 2 (scaling) 只用了 42/123/456 (all bfloat16)，两个 table 的 seed pool 不同但未在正文中讨论
- Appendix G' (Bayesian ROPE): HDI = [+0.10, +2.00]pp 的上界恰好 = ROPE 边界 2.00pp，这使得 "falls entirely inside the ROPE" 的声明在统计上处于边缘
- §3.6 (Error complementarity): oracle combination 结果基于 single-seed (seed 42)，标注了这一点但可在正文中更醒目
- Appendix H(j) re-repair pilot: n=44, power ~0.3, 单独报告 negative result 时应更显著地标注 power 不足

---

## Questions to Authors

**Q1**: 为什么不评估 Qwen3 CWM 在 step 300–400 checkpoints 的 repo-level accuracy？Table 16 显示这些 checkpoints 存在且对应 eval loss 最低点。DeepSeek 的 early-stopping 数据 (+18.14pp) 暗示 optimal checkpoint 可能显著改变结论。

**Q2**: 14B CWM 的 function-level gap 收敛到 0.43pp。是否有 14B 的 repo-level CWM 数据？如果 14B 也观察到 gap 缩小，将显著增强"capacity drives the gap"的论点，反之则增强"formulation inherently matters"的论点。

**Q3**: ±2pp SESOI 是否在实验开始前确定？是否有任何 pre-registration 记录？如果是 post-hoc 选择，建议在正文中明确说明。

**Q4**: NF4 quantization 对 CWM 长文本生成质量的影响是否被独立评估？两个 NF4 seeds (789/0) 在 function-level 的 CWM accuracy 与 bfloat16 seeds 是否有系统性差异？

**Q5**: §3.4 中 formulation×complexity interaction 的 LPM vs GEE 分歧（model identity: LPM p=0.002 vs GEE p=0.449）是否因为 k=25 clusters 不足以支持 GEE sandwich SEs？如果是，为什么在正文中呈现 GEE 结果？应该更清楚地说明哪个估计更可信。

---

## Missing References

- 未引用 equivalence testing 在 NLP 中的应用先例（如有的话），这会增强 TOST 方法选择的 motivation
- Constrained decoding (Willard and Louf, 2023) 在正文 Appendix H(c) 中被提及但未作为潜在解决方案在 Discussion 中讨论

---

## 主要优势

1. **填补真实空白**：首个在 matched conditions 下系统比较三种 execution-free verification formulation 的工作，避免了之前 across-model, across-dataset 比较的混淆
2. **统计方法论的标杆**：TOST equivalence testing + clustered bootstrap + Holm-Bonferroni + LPM/GEE 双模型 + Bayesian ROPE——这套统计框架远超 NLP 论文的一般水准
3. **诚实的限制性讨论**：Five identified confounds, power analysis, explicit conditioning on ≤8B LoRA——这种 intellectual honesty 值得肯定
4. **Failure mode taxonomy 的实用性**：Format collapse / Decision collapse / Aggregation penalty 的分类对 practitioners 选择 formulation 有直接指导价值
5. **Comprehensive ablation program**：LoRA rank, majority voting, sequence length, data size, preprocessing, few-shot, checkpoint 的系统消融，使结论有更强的因果推断基础

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

_source line 966 · 2026-05-23T09:09:18.028156+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "以下是 **Reviewer 2** 的完整审稿意见（Round 1）。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（Round 1）\n\n**审查侧重**: 新颖性 + 相关工作完整性 + 写作质量 + 格式合规\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3/5, **Excitement**: 2/5, **Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] 核心发现可预期性高，新颖性不足以支撑 main conference\n- 两个核心发现（function-level CLS≈CWM, repo-level CWM format collapse）可从第一性原理直接预期。§2.2 理论分析本身就预测了实验结果。论文只测试了两个极端复杂度（5-15 tokens vs 477 tokens），缺少中间复杂度数据来表征 transition boundary。\n- 建议：增加中间复杂度级别实验；将 GenRM 对比发现提升为主要贡献；将 failure mode taxonomy 发展为独立贡献。\n\n**N2** [critical] CWM 比较的生态效度存在根本性问题\n- ≤8B LoRA vs 原始 CWM 32B + execution trace pretraining。Abstract/Introduction claim 语气未充分反映这一限制。repo-level format collapse 可能反映的是模型容量而非 formulation 差异。\n\n### Should-Fix\n\n**W1** [warning] Abstract 统计细节过密，可读性差\n**W2** [warning] 贡献列表过少且框定过于谦虚（仅两条贡献，failure mode taxonomy 未列为贡献）\n**W3** [warning] GenRM 对比发现未被充分讨论（generation advantage 在代码领域失效，仅在 Related Work 一段）\n**W4** [warning] 仅使用两个模型家族，泛化性受限\n**W5** [warning] 种子数/实验配置不一致导致统计置信度参差不齐\n\n### 小问题\n- Table 1 信息密度高缺视觉分隔\n- Figure 2 y 轴窄放大视觉差异\n- Appendix G' 的 prime 符号命名不直观\n- §2.2 Failure Modes 位于 method section 可能造成困惑\n- `wei2022emergent` 引用类型不一致（TMLR 应为 article）\n\n### 相关工作\n- 潜在遗漏：CVeDRL (arXiv:2601.22803, 2026) difficulty-aware RL 训练代码 verifier\n- 引用真实性抽查通过\n\n### 格式\n- 全部合规。Appendix P \"Extended limitations\" 存在被质疑为转移 limitations 到 appendix 的风险。\n\n### 主要优势\n1. 统计方法论严谨\n2. Threats to Validity 分析详尽\n3. Failure mode taxonomy 有实用价值\n4. 实验设计匹配度高\n5. 写作诚实度高\n\n---\n\n请对上述每个要点给出 `[AGREE]` 或 `[REBUT]` 并说明理由。"
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
    "text": "以下是 **Reviewer 2** 的完整审稿意见（Round 1）。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（Round 1）\n\n**审查侧重**: 新颖性 + 相关工作完整性 + 写作质量 + 格式合规\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3/5, **Excitement**: 2/5, **Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] 核心发现可预期性高，新颖性不足以支撑 main conference\n- 两个核心发现（function-level CLS≈CWM, repo-level CWM format collapse）可从第一性原理直接预期。§2.2 理论分析本身就预测了实验结果。论文只测试了两个极端复杂度（5-15 tokens vs 477 tokens），缺少中间复杂度数据来表征 transition boundary。\n- 建议：增加中间复杂度级别实验；将 GenRM 对比发现提升为主要贡献；将 failure mode taxonomy 发展为独立贡献。\n\n**N2** [critical] CWM 比较的生态效度存在根本性问题\n- ≤8B LoRA vs 原始 CWM 32B + execution trace pretraining。Abstract/Introduction claim 语气未充分反映这一限制。repo-level format collapse 可能反映的是模型容量而非 formulation 差异。\n\n### Should-Fix\n\n**W1** [warning] Abstract 统计细节过密，可读性差\n**W2** [warning] 贡献列表过少且框定过于谦虚（仅两条贡献，failure mode taxonomy 未列为贡献）\n**W3** [warning] GenRM 对比发现未被充分讨论（generation advantage 在代码领域失效，仅在 Related Work 一段）\n**W4** [warning] 仅使用两个模型家族，泛化性受限\n**W5** [warning] 种子数/实验配置不一致导致统计置信度参差不齐\n\n### 小问题\n- Table 1 信息密度高缺视觉分隔\n- Figure 2 y 轴窄放大视觉差异\n- Appendix G' 的 prime 符号命名不直观\n- §2.2 Failure Modes 位于 method section 可能造成困惑\n- `wei2022emergent` 引用类型不一致（TMLR 应为 article）\n\n### 相关工作\n- 潜在遗漏：CVeDRL (arXiv:2601.22803, 2026) difficulty-aware RL 训练代码 verifier\n- 引用真实性抽查通过\n\n### 格式\n- 全部合规。Appendix P \"Extended limitations\" 存在被质疑为转移 limitations 到 appendix 的风险。\n\n### 主要优势\n1. 统计方法论严谨\n2. Threats to Validity 分析详尽\n3. Failure mode taxonomy 有实用价值\n4. 实验设计匹配度高\n5. 写作诚实度高\n\n---\n\n请对上述每个要点给出 `[AGREE]` 或 `[REBUT]` 并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 967 · 2026-05-23T09:09:48.614741+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30586
}
```

</details>

---


### Tool call

_source line 968 · 2026-05-23T09:09:48.866654+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "以下是 **Reviewer 1** 的完整审稿意见（Round 1）。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（Round 1）\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 3.5/5, **Excitement**: 3/5, **Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] CWM baseline 公平性——核心方法论问题\n- ≤8B LoRA 下 CWM 需生成 ~477 tokens/instance，CLS 仅 1 token。在小模型无 execution-trace pretraining 条件下，长文本生成退化是已知现象。实质上是在证明\"小模型不能生成长且连贯的文本\"，而非揭示 formulation 本质差异。\n- Title 暗示全面比较但实际仅覆盖 ≤8B\n- 14B function-level gap = 0.43pp 反而支持\"足够 capacity 下 CWM 可收敛\"\n- 建议：Title/Abstract 限定；正文 §3.4 增加 explicit caveat；如有可能增加 14B CWM repo-level 数据点\n\n**N2** [critical] Repo-level CWM 使用严重过拟合的 checkpoint\n- 所有 CWM repo-level 训练 NaN val loss → final epoch checkpoint。Table 16 显示 eval loss 在 step 300-400 达最小，final epoch 膨胀至 1.8×。Qwen3 有 step 300/400 checkpoints 但**未报告其准确率**。\n- DeepSeek early stopping gap 从 ~27pp 缩小到 ~10pp (+18.14pp improvement)\n- 建议：评估 Qwen3 CWM step-300/400 checkpoints 的 repo-level accuracy\n\n**N3** [critical] 统计功效不足对等价性声明的影响讨论不够充分\n- n_eff ≈ 86, TOST power ~0.3。CLS-TRAJ 的\"未确认\"可能完全是 power artifact。\n- Holm-Bonferroni 校正后 p=0.075, Bayesian ROPE P(ROPE)=0.542 (inconclusive)——都可用 power ~0.3 解释\n- 论文给出 CLS-CWM 和 CLS-TRAJ 不对称结论，但不对称可能完全是 power 不足造成的\n- 建议：正文更明确讨论；报告 CLS-TRAJ 等价性所需最小样本量；避免在 contribution list 中将 TRAJ model-contingent 作为稳健结论\n\n### Should-Fix\n\n**W1** [warning] ±2pp SESOI 的 a priori 性质存疑（无 pre-registration）\n- ±1.52pp 临界值距 ±2pp 仅 0.48pp，结论对 SESOI 选择较敏感\n**W2** [warning] 混合精度 NF4 + bfloat16 pooling（未正式检验精度差异；NF4 对 CWM 长文本生成影响未评估）\n**W3** [warning] Repo-level 数据处理不一致（drop vs truncate，与 checkpoint 选择策略耦合形成 confound chain）\n**W4** [warning] CLS-TRAJ 训练条件不匹配（~400 vs ~70K, label granularity 差异未控制）\n**W5** [warning] CLS-CWM paired comparison 使用不同 seeds（CLS s123 vs CWM s42）\n\n### 小问题\n- §3.2 排名基于不同 seed 数量\n- Table 1 和 Table 2 seed pool 不同\n- Bayesian ROPE HDI 上界恰好 = ROPE 边界（边缘）\n- Oracle combination 基于 single-seed\n- Re-repair pilot n=44, power ~0.3\n\n### Questions\n- Q1: 为什么不评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy？\n- Q2: 是否有 14B repo-level CWM 数据？\n- Q3: ±2pp SESOI 是否 pre-registered？\n- Q4: NF4 对 CWM 长文本生成质量的影响？\n- Q5: LPM vs GEE 分歧原因及哪个更可信？\n\n### Missing References\n- Equivalence testing 在 NLP 中的应用先例\n- Constrained decoding 在 Discussion 中讨论不足\n\n### 主要优势\n1. 填补 matched-condition 下 formulation 比较的真实空白\n2. 统计方法论的标杆\n3. 诚实的限制性讨论\n4. Failure mode taxonomy 的实用性\n5. Comprehensive ablation program\n\n---\n\n请对上述每个要点给出 `[AGREE]` 或 `[REBUT]` 并说明理由。"
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
    "text": "以下是 **Reviewer 1** 的完整审稿意见（Round 1）。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（Round 1）\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 3.5/5, **Excitement**: 3/5, **Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] CWM baseline 公平性——核心方法论问题\n- ≤8B LoRA 下 CWM 需生成 ~477 tokens/instance，CLS 仅 1 token。在小模型无 execution-trace pretraining 条件下，长文本生成退化是已知现象。实质上是在证明\"小模型不能生成长且连贯的文本\"，而非揭示 formulation 本质差异。\n- Title 暗示全面比较但实际仅覆盖 ≤8B\n- 14B function-level gap = 0.43pp 反而支持\"足够 capacity 下 CWM 可收敛\"\n- 建议：Title/Abstract 限定；正文 §3.4 增加 explicit caveat；如有可能增加 14B CWM repo-level 数据点\n\n**N2** [critical] Repo-level CWM 使用严重过拟合的 checkpoint\n- 所有 CWM repo-level 训练 NaN val loss → final epoch checkpoint。Table 16 显示 eval loss 在 step 300-400 达最小，final epoch 膨胀至 1.8×。Qwen3 有 step 300/400 checkpoints 但**未报告其准确率**。\n- DeepSeek early stopping gap 从 ~27pp 缩小到 ~10pp (+18.14pp improvement)\n- 建议：评估 Qwen3 CWM step-300/400 checkpoints 的 repo-level accuracy\n\n**N3** [critical] 统计功效不足对等价性声明的影响讨论不够充分\n- n_eff ≈ 86, TOST power ~0.3。CLS-TRAJ 的\"未确认\"可能完全是 power artifact。\n- Holm-Bonferroni 校正后 p=0.075, Bayesian ROPE P(ROPE)=0.542 (inconclusive)——都可用 power ~0.3 解释\n- 论文给出 CLS-CWM 和 CLS-TRAJ 不对称结论，但不对称可能完全是 power 不足造成的\n- 建议：正文更明确讨论；报告 CLS-TRAJ 等价性所需最小样本量；避免在 contribution list 中将 TRAJ model-contingent 作为稳健结论\n\n### Should-Fix\n\n**W1** [warning] ±2pp SESOI 的 a priori 性质存疑（无 pre-registration）\n- ±1.52pp 临界值距 ±2pp 仅 0.48pp，结论对 SESOI 选择较敏感\n**W2** [warning] 混合精度 NF4 + bfloat16 pooling（未正式检验精度差异；NF4 对 CWM 长文本生成影响未评估）\n**W3** [warning] Repo-level 数据处理不一致（drop vs truncate，与 checkpoint 选择策略耦合形成 confound chain）\n**W4** [warning] CLS-TRAJ 训练条件不匹配（~400 vs ~70K, label granularity 差异未控制）\n**W5** [warning] CLS-CWM paired comparison 使用不同 seeds（CLS s123 vs CWM s42）\n\n### 小问题\n- §3.2 排名基于不同 seed 数量\n- Table 1 和 Table 2 seed pool 不同\n- Bayesian ROPE HDI 上界恰好 = ROPE 边界（边缘）\n- Oracle combination 基于 single-seed\n- Re-repair pilot n=44, power ~0.3\n\n### Questions\n- Q1: 为什么不评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy？\n- Q2: 是否有 14B repo-level CWM 数据？\n- Q3: ±2pp SESOI 是否 pre-registered？\n- Q4: NF4 对 CWM 长文本生成质量的影响？\n- Q5: LPM vs GEE 分歧原因及哪个更可信？\n\n### Missing References\n- Equivalence testing 在 NLP 中的应用先例\n- Constrained decoding 在 Discussion 中讨论不足\n\n### 主要优势\n1. 填补 matched-condition 下 formulation 比较的真实空白\n2. 统计方法论的标杆\n3. 诚实的限制性讨论\n4. Failure mode taxonomy 的实用性\n5. Comprehensive ablation program\n\n---\n\n请对上述每个要点给出 `[AGREE]` 或 `[REBUT]` 并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 969 · 2026-05-23T09:09:50.275986+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---


### Assistant

_source line 970 · 2026-05-23T09:09:54.128125+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 87

## Round 87

2 recorded events


### User

_source line 971 · 2026-05-23T09:09:56.695675+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.5 (Borderline Conference)**。

三个 Must-Fix 问题：
1. **CWM baseline 公平性**——≤8B LoRA 系统性削弱 CWM（需生成 ~477 tokens vs CLS 1 token），repo-level 核心发现可能是 capacity artifact 而非 formulation 本质差异
2. **CWM 使用严重过拟合 checkpoint**——eval loss 在 step 300–400 最低，final epoch 膨胀 1.8×，且论文持有 optimal checkpoint 但未评估其 accuracy
3. **统计功效不足**——power ~0.3, CLS-TRAJ "未确认等价"可能纯粹是 underpowered 的结果，不应被呈现为"model-contingent"

五个 Should-Fix：SESOI a priori 性存疑、NF4/bfloat16 pooling 未经正式检验、数据处理不一致、CLS-TRAJ 训练条件不匹配、paired comparison 跨 seed。

统计方法论本身（TOST + clustered bootstrap + Holm-Bonferroni + LPM/GEE + Bayesian ROPE）是论文的突出优势，远超 NLP 论文一般水准。

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

_source line 972 · 2026-05-23T09:10:01.983948+00:00_

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


## Round 88

## Round 88

2 recorded events


### User

_source line 973 · 2026-05-23T09:11:24.677000+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 (Round 1) 的逐条回应

---

### Must-Fix

**[REBUT] R2-N1: 核心发现可预期性高，新颖性不足以支撑 main conference**

部分反驳。R2 的论点是"从第一性原理可直接预期"，但这一标准过于宽泛——许多实证发现事后看都"可预期"。具体反驳如下：

1. **Function-level 等价性并非 trivially predictable。** 在实验之前，有合理理由预期 CWM 优于 CLS（更丰富的 intermediate reasoning trace，类似 chain-of-thought 的优势——§4 Related Work 中引用的 GenRM 文献 Hosseini et al. 2025、Zhang et al. 2025 均发现 generation-based verifier 在数学推理中优于 classification-based）。论文的 Appendix H(k) 明确将 CWM 框定为"structurally a chain-of-thought verifier"并分析了为何 CoT 优势在代码领域未实现。这一 negative result 本身有信息价值。

2. **Gap magnitude 不可预期。** §2.2 的理论分析预测了方向但无法预测 18–26pp 的具体量级，更无法预测四项干预全部失败（Appendix H(g)：LoRA rank 32、majority voting、relaxed matching、scaling 4B→8B）。

3. **缺少中间复杂度数据这一批评是合理的**，但这是实验 scope 的限制而非 novelty 的否定。HumanEval+MBPP (5–15 tokens) 和 SWE-bench Verified (~477 tokens) 是该领域两个标准 benchmark，选择它们有生态效度理由。

4. 但我同意 R2 关于 **failure mode taxonomy 应被提升为独立贡献** 的建议——Table 4 的 taxonomy（format collapse / decision collapse / aggregation penalty）是论文最具实用价值的输出之一，目前在 contribution list 中缺失。

**结论：** 不同意将论文降为 Findings 仅因为"可预期"。R2 在 ARR guidelines 中也应注意到 H1 条款："Dismissing results as 'unsurprising' despite lacking prior evidence" 是常见审稿错误。但增加中间复杂度数据和提升 taxonomy 为贡献的建议是合理的。

---

**[AGREE] R2-N2: CWM 比较的生态效度存在根本性问题**

完全同意，这与我的 R1-N1 一致。≤8B LoRA vs 原始 CWM 32B + mid-training 是核心方法论 confound。论文虽在多处添加了限定（Abstract 提到"under our ≤8B LoRA protocol"，§3.7、Appendix N 有详细讨论），但 Introduction §1 contributions (2) "formulation choice is moderated by code complexity" 和 (3) "at repository level under ≤8B LoRA" 之间语气不一致——(2) 读起来像一般性结论。

补充我的 R1-N1 未提到的一点：14B function-level 数据（Table 2）显示 CLS-CWM gap 从 8B 的 2.62pp 收敛到 14B 的 0.43pp (TOST p<0.0006)，这直接支持"capacity drives the gap"假设。如果有 14B repo-level CWM 数据，将极大增强（或推翻）结论。

---

### Should-Fix

**[REBUT] R2-W1: Abstract 统计细节过密，可读性差**

不同意。对于一篇以统计方法论为核心卖点的论文，Abstract 中包含关键统计结果（TOST p=0.007, ε ≈ 2.17, pp 数值）是必要的——审稿人和读者需要在 Abstract 层面判断结论的可靠性。ARR reviewer guidelines (R5) 明确要求 "appropriate information about statistical significance"。删除统计细节会使 Abstract 退化为含糊的 qualitative claim。

建议折中：可在 Abstract 中保留 2–3 个关键数字（CLS-CWM equivalence p-value、repo-level gap range），将其余数字移到 Introduction。

---

**[AGREE] R2-W2: 贡献列表过少且框定过于谦虚**

同意。论文 §1 仅列出两条贡献（matched experimental framework + formulation-complexity interaction），但实际上至少有三个可独立成立的贡献：

1. Matched comparison framework（已列）
2. Formulation-complexity interaction（已列）
3. **Failure mode taxonomy**（Table 4: format collapse / decision collapse / aggregation penalty）——这是对 practitioners 最直接有用的输出，目前未被列为贡献

增加第三条贡献不会膨胀论文——它已经做了这个工作，只是没有在 framing 中给予足够权重。

---

**[AGREE] R2-W3: GenRM 对比发现未被充分讨论**

同意。论文 §4 Related Work 和 Appendix H(k) 提供了"generation advantage 在代码领域失效"的分析——CWM 本质上是 code-domain 的 GenRM/chain-of-thought verifier，但在 function-level 上不优于 CLS，在 repo-level 上反而劣于 CLS。这与 Hosseini et al. (2025) 在数学推理中的发现形成鲜明对比。

将这一对比提升到 Discussion 级别（而非仅在 Related Work 一段）会增强论文的 conceptual contribution。

---

**[REBUT] R2-W4: 仅使用两个模型家族，泛化性受限**

不同意这构成 Should-Fix 级别的问题。

1. 两个 model families (Qwen3, DeepSeek-Coder) 在代码生成领域是具有代表性的选择，且它们有不同的 pretraining pipeline——这正是 cross-model consistency check 的目的。
2. 论文明确将 DeepSeek-Coder 定位为 "cross-model consistency check"（§3.1），而非声称覆盖了所有模型。核心实验在 Qwen3 上用 5 seeds，DeepSeek 用 2 seeds 验证方向一致性——这是合理的实验经济性选择。
3. 要求更多 model families 实质上是要求一个更大规模的实验——这可以是 future work，但不应该是当前论文的 weakness。ARR guidelines (H4) 提醒 reviewers 不应 "require unnecessary additional experiments beyond claim validation"。

降级为小问题更合适：可在 Limitations 中提到仅覆盖两个 decoder-only LLM family。

---

**[AGREE] R2-W5: 种子数/实验配置不一致导致统计置信度参差不齐**

同意，这与我的 R1-N3（统计功效不足）一致。具体的不一致：

- Function-level: 5 seeds (Qwen3), 2 seeds (DeepSeek)
- Repo-level: 2–3 seeds (CLS/CWM), 1–3 seeds (TRAJ)，各配置 seed 覆盖不同
- Table 2 (scaling): 4B/8B 用 2 seeds, 14B 用 3 seeds，且全部 bfloat16
- Table 1 pooling bfloat16 和 NF4 seeds

这使得不同比较的统计置信度差异很大，论文对此的讨论分散在多处（§3.1 footnote, §3.4, Appendix P），不容易形成整体印象。建议在 §3.1 或 §3.7 增加一个简明的 seed coverage summary table。

---

### 小问题

**[AGREE] R2-Minor-1: Table 1 信息密度高缺视觉分隔**
同意。Table 1 包含 primary results, cross-model check, 和 prompting baselines，可通过额外 \midrule 或 shading 改善。

**[REBUT] R2-Minor-2: Figure 2 y 轴窄放大视觉差异**
查看 Figure 2 caption (main.tex L59): "CLS and CWM accuracy with shaded gap region. The CLS–CWM gap follows an inverted-U trajectory: 1.32pp at 4B, widening to 2.62pp at 8B, then narrowing to 0.43pp at 14B (3 seeds)." 图的目的是展示 gap 的变化趋势，narrow y-axis 是展示小但有统计意义的差异的标准做法。Caption 中已提供绝对数值。论文还在 caption 中注明了具体 pp 数值，读者不会被视觉放大误导。这不构成问题。

**[AGREE] R2-Minor-3: Appendix G' 的 prime 符号命名不直观**
同意。"G'" 不直观，可改为 "Appendix G.2" 或给 Bayesian ROPE 一个独立 appendix 编号。

**[AGREE] R2-Minor-4: §2.2 Failure Modes 位于 method section 可能造成困惑**
同意。§2.2 是 formulation-specific failure modes 的理论分析，更适合放在 §3 Experiments 或 §3.6 Analysis 中，与 Table 4 的实证 taxonomy 相邻。放在 Method section 中会让读者误以为这是方法设计的一部分。

**[AGREE] R2-Minor-5: `wei2022emergent` 引用类型不一致**
同意，minor formatting issue。

---

### 相关工作

**[REBUT] R2-Related: CVeDRL (arXiv:2601.22803, 2026)**
无法验证此引用的存在性——arXiv ID "2601.22803" 的格式超出正常 arXiv 编号范围（2026 年 1 月的论文 ID 通常为 2601.XXXXX，五位数，但 22803 是合法的五位数）。如果 R2 能提供完整标题和作者信息，我可以评估其相关性。但即使此论文存在，difficulty-aware RL training 与本文的 verification formulation comparison 主题有一定距离——本文不涉及 RL training，比较的是 formulation 本身而非 training 策略。

---

### 格式

**[REBUT] R2-Format: Appendix P "Extended limitations" 存在被质疑为转移 limitations 到 appendix 的风险**

不同意这构成格式问题。论文在主文 §8 有完整的 Limitations section（约 200 words），覆盖了核心限制（single model family for 14B, ≤8B constraint, Python-only, synthetic mutations）。Appendix P 是对 §8 中已提到的限制的**技术细节展开**（specific seed coverage numbers, val-test distribution mismatch 的量化分析等），不包含§8中未提及的限制。

EMNLP 2026 的规则是 "Mandatory limitations... do not count towards this page limit, provided they do not contain excessive additional content"。主文 limitations 在正文中，appendix 提供补充细节——这完全合规。

---

### 总体评估

与 R2 的主要分歧：

1. **Novelty 评估（R2: 2/5 Excitement → 我: 3/5）**：R2 以"可预期性"否定新颖性，但 ARR guidelines 明确将此列为常见审稿错误 (H1)。实证验证"可预期"的假设仍有价值——尤其是当验证附带了 quantitative 的 magnitude estimation、failure mode taxonomy、和统计严谨的 equivalence testing 时。论文不是在证明显而易见的事，而是在量化和表征一个此前仅有模糊直觉的问题。

2. **Overall 评分分歧（R2: 3.0 → 我: 3.5）**：R2 的 3.0 (Findings) 主要受 Excitement 2/5 驱动。我认为方法论严谨性和实用贡献（failure mode taxonomy）支撑 Borderline Conference。但我同意 CWM baseline fairness 是关键问题——如果作者能在 rebuttal 中提供 14B repo-level CWM 或 Qwen3 optimal checkpoint 的数据，将显著影响最终评分。

两位 reviewer 一致同意的问题：CWM baseline 公平性（R1-N1, R2-N2）和统计功效不足（R1-N3, R2-W5）——这两个是 camera-ready 前必须解决的。

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

_source line 974 · 2026-05-23T09:11:32.884828+00:00_

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


## Round 89

## Round 89

2 recorded events


### User

_source line 975 · 2026-05-23T09:11:35.597001+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。核心判断：

- **R2-N1 (novelty)**：部分反驳——"可预期"不等于"无价值"，但同意 failure mode taxonomy 应提升为独立贡献
- **R2-N2 (CWM 生态效度)**：完全同意，与我的 R1-N1 一致
- **R2-W1 (abstract 密度)**：反驳——统计细节对方法论论文是必要的
- **R2-W4 (两个模型家族)**：反驳——ARR guidelines 不鼓励要求不必要的额外实验
- 其余 W2/W3/W5 和多数小问题均同意

两位 reviewer 共识的核心问题：CWM baseline 公平性 + 统计功效不足。

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

_source line 976 · 2026-05-23T09:11:40.813522+00:00_

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


## Round 90

## Round 90

10 recorded events


### User

_source line 977 · 2026-05-23T09:11:49.274520+00:00_

[Reviewer 2 审稿结果]:
## Reviewer 2 对 Reviewer 1 的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: CWM baseline 公平性**

同意这是论文的核心方法论问题。我在自己的审稿意见中提出了几乎一致的关切（我的 N2）。补充两点支持：

1. 14B function-level gap 收窄至 0.43pp（§3.2 Table 2, TOST p=0.0006）恰好反过来证明了"capacity 增长可消除 formulation 差异"，这与 R1 的判断一致——repo-level 的 18-26pp gap 很可能是 capacity bottleneck 而非 formulation 固有缺陷。
2. 论文自身的 Appendix I(c) 提供了一个意外证据："a CWM model inadvertently trained on function-level (CLS-format) data achieved 86.05% accuracy with 0% unparseable outputs at repo level"。这直接表明 CWM 的 repo-level 退化来自输出空间复杂度（trace generation）而非 verification task 本身的难度——但这恰好也说明问题不在"formulation"而在"≤8B 模型的长文本生成能力"。

**[AGREE] R1-N2: CWM checkpoint 过拟合问题**

这是我的审稿中未充分强调的重要方法论缺陷。R1 指出的核心事实无可辩驳：

1. Table 16（Appendix L）显示 Qwen3-8B CWM eval loss 在 step 300-400 达到最小值（~0.29），final epoch（step 6600）膨胀至 ~0.52（1.8×）。论文确认 Qwen3 有 step 300/400 checkpoints 但**未报告其 repo-level accuracy**——这是一个可以执行但未执行的实验，构成重大遗漏。
2. DeepSeek early-stop 的 +18.14pp improvement（75.45% vs 57.31%，Appendix N）表明 checkpoint 选择对 CWM 影响极大。虽然论文指出 early-stopped 模型仍有 66.4% unparseable rate（format collapse 不纯粹是过拟合问题），但这并不能免除评估 Qwen3 早期 checkpoint 的义务。

不过，我想补充一个 nuance：即使 early-stopped DeepSeek CWM 达到 75.45%，仍低于 CLS 的 82-85%（Table 3），且保持 66.4% unparseable rate。这说明 format collapse 在训练早期就已存在，过拟合加剧了但并非唯一原因。R1 的 "~10pp gap" 估算（从 ~27pp 缩至 ~10pp）是合理的，但这个缩小后的 gap 仍然 non-trivial。

**[AGREE] R1-N3: 统计功效不足对等价性声明的影响**

同意 power ~0.3 是一个严重限制。论文在 §3.3 确实提到 "CLS-TRAJ non-confirmation may reflect insufficient power"，但处理方式不够充分：

1. CLS-CWM 等价性确认（TOST p=0.007, Bayesian ROPE P(ROPE)=0.975）与 CLS-TRAJ 未确认（TOST adjusted p=0.075, P(ROPE)=0.542）之间的不对称结论，在 power ~0.3 下确实可能是 Type II error 的产物而非真实差异。
2. 论文在贡献声明中将 "TRAJ equivalence is not confirmed after multiple comparison correction" 与 "CLS-CWM equivalence" 并列（§1 contribution 1），读者可能误解为"CLS-TRAJ 不等价"（实际是"无法确认等价"）。

但我想微调一个细节：Bayesian ROPE 分析中 CLS-TRAJ variant-level 的 P(ROPE)=0.970（Appendix G'），这与 per-test level 的 0.542 存在差异。论文选择报告 per-test level 的 inconclusive 结果是 conservative 的，但也意味着在 variant-level 上两个框架给出不同结论。这一不一致值得在正文中明确讨论。

---

### Should-Fix

**[AGREE] R1-W1: ±2pp SESOI 的 a priori 性质存疑**

同意。论文在 §3.3 提供了合理的 post-hoc justification（"2pp corresponds to ~2-3 problems out of 114, below practitioner-relevant differences"），且 Table 13（Appendix G）展示了 TOST margin sensitivity。但缺少 pre-registration 确实削弱了等价性声明的 credibility。±1.52pp 临界值距 ±2pp 仅 0.48pp 的事实进一步强化了这一担忧——如果 SESOI 设为 ±1.5pp，CLS-CWM 等价性就无法确认。

**[REBUT] R1-W2: 混合精度 NF4 + bfloat16 pooling**

部分反驳。论文在 §3.3 脚注中提供了关键证据："Restricting to bfloat16 only: CLS-CWM remains significant (p<0.05); CLS-TRAJ yields p=0.128"。这表明 CLS-CWM 等价性结论在移除 NF4 seeds 后仍然成立。此外，§3.1 指出 "function-level accuracy remains within seed noise across both precisions"。

但 R1 关于"NF4 对 CWM 长文本生成影响未评估"的细分关切是合理的——function-level CWM 输出仅 5-15 tokens，NF4 的影响可能在 repo-level 长序列生成中放大。由于 repo-level 实验未使用 NF4（seeds 42/123/456 均为 bfloat16，§3.1），这一潜在问题不影响 repo-level 结论。总体来说，证据基本充分但可以更 explicit。

**[AGREE] R1-W3: Repo-level 数据处理不一致**

同意。Drop vs truncate 不仅产生不同训练集（67,343 vs 70,748 samples），还耦合了 checkpoint 选择策略（truncate → NaN val loss → final epoch default），形成了 R1 正确指出的 confound chain。Appendix N 报告 DeepSeek CLS accuracy 从 82.61%（s42 drop）到 74.93%（s123 truncate）有 7.68pp 偏差，这个量级不可忽略。

**[AGREE] R1-W4: CLS-TRAJ 训练条件不匹配**

同意。我在自己的审稿中也注意到了这一点。Appendix B 的 downsample ablation（CLS 80.74% vs TRAJ 72.92%，+7.82pp）控制了数据量但未控制 label granularity（per-test vs variant-level）。论文在 Appendix N 最后一段也承认："data volume (~400 variants vs ~70K per-test instances) and label granularity (variant-level vs per-test) are both plausible confounds that cannot be separately controlled"。这一坦诚值得肯定，但也意味着 CLS vs TRAJ 的 repo-level 比较本质上是 exploratory 而非 confirmatory。

**[AGREE] R1-W5: CLS-CWM paired comparison 使用不同 seeds**

同意。Table 14（Appendix H）中 CLS s123 vs CWM s42 的 paired comparison 引入了额外的 seed 方差。论文在 Appendix H 底部承认这一点："the CI lower bound of 10.42pp far exceeds the seed noise observed in function-level experiments (<2pp)"——这个辩护对 repo-level 结论是合理的（gap 远超 seed noise），但对 function-level 的 1.24pp gap 而言，seed 差异可能是 meaningful confounder。

---

### 小问题

**[AGREE] §3.2 排名基于不同 seed 数量**: Table 2 中 4B/8B 用 2 seeds，14B 用 3 seeds，排名比较不 fully comparable。

**[AGREE] Table 1 和 Table 2 seed pool 不同**: Table 1 用 5 seeds（含 NF4），Table 2 仅用 bfloat16 seeds 的子集，潜在 selection bias。

**[AGREE] Bayesian ROPE HDI 上界 = ROPE 边界**: Appendix G' 报告 CLS-CWM HDI = [+0.10, +2.00]pp，上界恰好等于 ROPE 边界 +2.00pp。这个边缘情况使 "falls entirely inside the ROPE" 的判断在数值精度上较为脆弱。

**[AGREE] Oracle combination 基于 single-seed**: §3.5 报告 oracle 90.63%（single-seed estimate, seed 42），95% CI [89.3%, 91.9%] 也是单种子 bootstrap。多种子 oracle 估计可能有不同结果。

**[AGREE] Re-repair pilot n=44, power ~0.3**: Appendix I(j) 的 negative result 在 power ~0.3 下几乎无法解释为 true negative。论文确实注明了这一点（"insufficient sample size ... statistical power is ~0.3 for a medium effect size"），但仍然在正文 §5 Conclusion 中将其列为 future direction 的动机。

---

### Questions

**Q1 (Qwen3 CWM step 300-400 accuracy)**: 同意这是一个关键缺失实验。论文确认 checkpoints 存在（Table 16），评估它们的 repo-level accuracy 可以直接量化过拟合对 CWM 性能的影响。

**Q2 (14B repo-level CWM 数据)**: 高度相关。14B function-level gap 已收窄至 0.43pp，14B repo-level 数据将直接回答"capacity 增长是否能弥合 repo-level gap"。

**Q3 (SESOI pre-registration)**: 同意这是一个合理的质询。如果没有 pre-registration，应在正文中更明确地表述 SESOI 的选择是 post-hoc 的。

**Q4 (NF4 对 CWM 长文本生成的影响)**: 如上 W2 回应所述，repo-level 实验未使用 NF4，因此不直接影响核心结论，但 function-level pooled 分析中 NF4 对 CWM 的具体影响值得报告。

**Q5 (LPM vs GEE 分歧)**: 论文在 Appendix M 中已给出解释——cluster count k=25 低于 GEE sandwich SE 的稳定阈值 k≥40（cite Cameron et al., 2008）。这个解释是合理的：primary effects（formulation）在两种方法下一致，分歧仅出现在 secondary effects（model identity），且 GEE 在小 cluster 下更保守。我认为论文的处理基本充分。

---

### Missing References

**[REBUT] Constrained decoding 讨论不足**: 论文在 Appendix I(c) 中已明确提及 constrained decoding（cite Willard and Louf, 2023）并解释了为何它不能解决核心问题："Constrained decoding could enforce format compliance but would not address the semantic accuracy deficit among parseable outputs"。38-43% 的 parseable-only accuracy（低于 majority baseline 72.96%）表明即使 100% format compliance 也不能挽救 CWM 的 repo-level 性能。R1 的关切已被 adequately addressed。

**[AGREE] Equivalence testing 在 NLP 中的应用先例**: 论文在统计方法引用（Lakens 2017, Schuirmann 1987, Wellek 2010）方面很充分，但确实缺少 TOST/equivalence testing 在 NLP/ML 领域的具体应用先例。如果存在此类先例，引用会加强方法选择的合理性。

---

### 总结

R1 的审稿整体质量高，关注点聚焦且有据可查。三个 Must-Fix 中：
- **N1（CWM 公平性）**和 **N2（checkpoint 过拟合）**是最有力的批评，直接动摇了论文核心 claim 的可靠性
- **N3（statistical power）**是合理的方法论关切但论文已有部分回应

R1 给出 3.5 (Borderline Conference) 高于我的 3.0 (Findings)，主要分歧在 Excitement 维度（R1: 3, 我: 2）。我认为即使解决了所有方法论问题，核心发现的可预期性仍然限制了论文的 excitement——这是 R1 未充分强调的。但我认同 R1 对 failure mode taxonomy 实用价值和统计方法论标杆的积极评价。

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

_source line 978 · 2026-05-23T09:12:28.147877+00:00_

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

_source line 979 · 2026-05-23T09:12:29.507520+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T09:02:01.944323+00:00\", \"completed_at\": \"2026-05-23T09:06:01.781832+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 4-7\", \"message\": \"Figure 2 首次引用在 page 4-5（\\\"at 8B (Figure 2)\\\"），但实际出现在 page 7 右栏，float 漂移约 2-3 页。建议调整 float 位置参数或将 Figure 2 上移至 page 5-6 附近\"}, {\"severity\": \"info\", \"dimension\": \"page 1-2\", \"message\": \"前两页为纯文本（Abstract + Introduction），首个 display item（Figure 1）出现在 page 3 顶部。在 ACL 格式中可接受，但处于审稿人耐心边界。Figure 1 本身是优秀的视觉锚点——三种 formulation 的对比图，清晰传达核心 idea\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 概念图清晰、caption 自包含，三种 formulation 对比一目了然。用色和布局专业。文字可读性在打印分辨率下足够\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1（主结果表）全宽排版、booktabs 风格、最优加粗，格式规范。行数较多（~15 行），视觉略密，但信息组织合理\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2（scaling 结果）格式一致，booktabs + 粗体最优。脚注清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"同一页放置 Table 3 和 Table 4 两个表格，页面视觉密度较高，但两表均紧凑且排版正确，可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2（accuracy scaling 折线图）使用蓝/橙双色方案（色盲友好），带 shaded gap region。Y 轴未从零开始但图注明确标注了这一点（good practice）。Caption 描述了 inverted-U 趋势但未注明\\\"higher is better\\\"方向\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 图内 axis label 和 legend 文字偏小（约正文字号 60-65%），150 DPI 下可读但稍吃力。建议放大至正文字号 70%+\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主正文在第 8 页结束（Section 5 Conclusion + Limitations），符合 EMNLP 8 页限制。Limitations 为简短一段覆盖 3 个要点（Python-only, synthetic mutations, model families），符合规范\"}, {\"severity\": \"info\", \"dimension\": \"page 9-11\", \"message\": \"参考文献格式统一，无 [?] 未解析引用，无明显格式错误。三页参考文献密度正常\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Appendix Figure 3（bar chart）清晰可读，蓝色柱状图，标注了 y 轴未从零开始\"}, {\"severity\": \"info\", \"dimens
…[truncated 321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-23T09:12:29.739341+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "offset": "725",
  "limit": "50"
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
    "offset": "725",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 981 · 2026-05-23T09:12:29.856581+00:00_

725	  resolution_round: 10
726	
727	# === Round 11 (Continue Review) New Issues ===
728	
729	- id: "R11-M1"
730	  summary: "Figure 2 中 14B 单 seed 数据点与多 seed 数据点视觉等权，可能导致 gap reversal 被过度解读"
731	  category: format
732	  severity: info
733	  status: open
734	  first_raised_round: 11
735	  last_seen_round: 11
736	  mentions:
737	    - round: 11
738	      reviewers: [1, 2]
739	      note: "R1 提出，R2 AGREE。14B 数据点与 4B/8B 并列但仅为 single seed，图中无视觉区分（如星号/虚线/n=1 标注）。Caption 和 Table 2 脚注有标注，但图形快速浏览时可能误读 gap reversal (-0.05pp) 的确定性。"
740	  action_items:
741	    - round: 11
742	      action: "Figure 2 中 8B→14B 连线改虚线（dashed），视觉区分 exploratory 数据"
743	      assigned_to: "agent"
744	      status: resolved
745	  resolution: "Figure 2 已更新：8B→14B 段虚线连接（CLS 和 CWM 均如此），14B 空心 marker，'exploratory' 灰色背景标注，'≈ 0 pp' 标签上移不遮挡数据点。"
746	  resolution_round: 11
747	
748	- id: "R11-M2"
749	  summary: "§3.5 main text 引用 LPM model identity 效应 (p=0.001) 但 GEE 给出 p=0.410，需加 qualifier"
750	  category: writing
751	  severity: info
752	  status: resolved
753	  first_raised_round: 11
754	  last_seen_round: 11
755	  mentions:
756	    - round: 11
757	      reviewers: [1, 2]
758	      note: "R1 提出，R2 AGREE。LPM 和 GEE 对 model identity 效应从'高度显著'到'完全不显著'的质变。正文应加 qualifier 如 'model identity reaches significance under LPM but not under GEE (Appendix M); this effect is specification-dependent'。与论文其他方面的方法论透明度标准一致。"
759	  action_items:
760	    - round: 11
761	      action: "§3.5 model identity 效应加 LPM vs GEE qualifier"
762	      assigned_to: "director"
763	      status: resolved
764	  resolution: "已在 commit 0b38a2b 中修复。§3.5 当前文本已包含完整 LPM vs GEE 对比：'model identity reaches significance under LPM (p=0.002) but not under GEE logistic regression (p=0.449, Appendix M), consistent with the limited cluster count (k=25) falling below the k≥40 threshold for stable sandwich SEs'。"
765	  resolution_round: 11
766	
767	- id: "R11-M3"
768	  summary: "Abstract 'motivate routing' 暗示 routing 有前景，但正文数据显示 simple routing capture <0.4pp"
76
…[truncated 132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 117
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-23T09:17:32.837384+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "\n# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 11\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 12\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → final epoch). 但 R7 的 CLS epoch ablation (<1pp) 仍有效。新角度：CWM NaN val loss 可能是 formulation-inherent。\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。但 R2 REBUT：Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp。Director 裁定：证据表明 checkpoint 差异无法解释 18-26pp gap，降为 Should-Fix（正文更显著讨论此缓解证据）。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-N2 升级为 critical：论文持有 Qwen3 CWM step 300-400 optimal checkpoints（Table 16 显示 eval loss 最低点）但未评估其 repo-level accuracy。DeepSeek early-stop +18.14pp (75.45% vs 57.31%) 暗示 Qwen3 optimal checkpoint 可能显著缩小 gap。R2 完全 AGREE。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因（formulation-inherent vs implementation issue）\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文（非仅 Appendix）更显著讨论 checkpoint 缓解证据（matched epoch-3 gap 仍 20-23pp + CLS ablation <1pp）\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy 并报告结果\"\n      assigned_to: \"experiment\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 12\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1: 'design space' framing 过度. R1 部分同意.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1 再次标 CRITICAL：三种公式均为已有方法，核心发现可从直觉预期。R1 AGREE 但认为 failure mode taxonomy 有独立贡献。两人共识：Findings 合适，Main 不够。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. R2 STILL_OPEN (excitement improved 2.5→3.0 but core contribution type unchanged). R1 AGREE on assessment but argues exceptional soundness partially compensates. Cross-sharing: R1 cites methodological demonstration value + failure mode taxonomy + 14B forward-looking insight. R2 rebuts: soundness ≠ excitement, ARR separates them for a reason. Both accept 3.0-3.5 range. Director: inherent limitation, wont_fix.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R2-N1 标 CRITICAL (Excitement 2/5)：核心发现（func-level equiv + repo-level collapse）可从 §2.2 理论分析直接预期，缺中间复杂度数据。R1 REBUT：引用 ARR H1 条款，认为'可预期≠无价值'，gap magnitude 和四项干预失败不可预期。但 R1 同意 failure mode taxonomy 应提升为贡献。最终分歧：R1 Excitement 3/5, R2 Excitement 2/5。\"\n  action_items:\n    - round: 9\n      action: \"标题从 'design space' 调整为 'systematic comparison'\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"增加轻量 routing/ensemble 实验以提升 excitement\"\n      assigned_to: \"experiment\"\n      status: resolved\n    - round: 10\n      action: \"Bayesian ROPE 等价性检验增强 equivalence 证据\"\n      assigned_to: \"experiment\"\n      status: resolved\n    - round: 10\n      action: \"≥14B 模型单点验证\"\n      assigned_to: \"experiment\"\n      status: resolved\n  resolution: \"所有可行 action items 已完成。Excitement 从 2.5 提升至 3.0，但核心贡献类型（empirical comparison of existing formulations）无法通过进一步修改改变。Novelty ceiling 为 inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 12\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"SESOI 基于训练噪声量级独立于 observed gap.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。缺 domain-specific justification.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W4 re-raises：±2pp 依赖于 accuracy range 和 test set size，更接近 post-hoc rationalization。R2 部分同意，建议重新定位为 'practically motivated with robustness check'。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-W1 re-raises：无 pre-registration，±1.52pp 临界值距 ±2pp 仅 0.48pp，结论对 SESOI 选择敏感。R2 AGREE。\"\n  action_items:\n    - round: 9\n      action: \"§3.4 加 domain-grounded SESOI justification; 正文引用 Appendix J sensitivity\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"SESOI 描述从 'a priori' 改为 'practically motivated'\"\n      assigned_to: \"paper\"\n      status: wont_fix\n    - round: 12\n      action: \"正文 §3.4 中引用 TOST sensitivity analysis（Appendix G），讨论 ±1.52pp 临界值；承认无 pre-registration\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"3+ 处修复完成。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Abstract 仍比 Conclusion 缺 qualifier.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未被独立提出。Abstract 已含 '≤8B LoRA protocol' qualifier。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标为 CRITICAL：≤8B 限制严重威胁泛化性。R1 部分 REBUT（4B→8B gap 扩大）但同意 abstract 需限定。两人共识：abstract/conclusion 应明确 '≤8B LoRA regime' 限定。\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 'under our ≤8B LoRA protocol'\"\n      assigned_to: \"agent\"\n      status: resolved\n    - round: 10\n      action: \"Conclusion 也加 ≤8B LoRA 限定；讨论更大规模下结论可能如何变化\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入 'All findings are conditioned on ≤8B LoRA fine-tuning; at larger scale, the generation bottleneck may diminish'。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"降级 diagnostic granularity\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 12\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W6: 175× 数据量差异.\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：180× 差异 + signal granularity (per-test vs variant-level) 无法通过 volume matching 解决。R2 AGREE。两人共识：应将 TRAJ 数据量/信号粒度限制框架为 formulation 固有属性。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-W4 re-raises：downsample 控制了 volume 但未控制 label granularity。R2 AGREE。两人共识：CLS vs TRAJ repo-level 比较本质上是 exploratory 而非 confirmatory。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性而非可控实验变量\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"Contribution summary 中明确表述 CLS-TRAJ repo-level 比较包含 training regime confound（data volume + label granularity），结论为 exploratory\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成，在 §3.5 和 Appendix M 报告。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Aletheia/VeRPO/ExecVerify.\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"三篇已加入。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"新增: GenRM, RepoExec, Chen et al.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W5: CodeScaler. 另提 GenPRM, ExecVerify.\"\n    - round: 10\n      reviewers: [2]\n      note: \"R2-W2: CodeRM (Ma et al., ACL 2025) 未引用。另需加强 ORM/PRM 框架映射讨论。R1 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"验证 CodeRM 真实性后加入 Related Work；加半段 CLS↔PRM/CWM↔generative verifier 映射讨论\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: CodeRM (Ma et al., ACL 2025) 加入 Related Work，ORM/PRM 映射段落加入（CLS→PRM-like process, TRAJ→ORM-like outcome, CWM→generative verifier）。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 11\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"bar labels 偏小.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-M2: y-axis 不从零开始（55%），视觉夸大 gap。R2 AGREE。Caption 已标注但对快速浏览读者可能误导。视觉审查也标记。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. Y-axis non-zero start acceptable for 0-3pp differences; caption annotated. R1 confirms 55% start with sufficient visual context. R2 confirms caption标注充分。\"\n  action_items:\n    - round: 10\n      action: \"Figure 2 y-axis 改从 0 开始\"\n      assigned_to: \"agent\"\n      status: resolved\n  resolution: \"Figure 2 y-axis 从约 55-80% 起始（版本差异），caption 标注 'y-axis does not start at zero'。两位 Reviewer 一致确认：对 0-3pp 差异展示，非零起始合理，caption 标注充分。\"\n  resolution_round: 11\n\n# === Round 8 (Fresh Review) Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆: §5.2 将 CLS-TRAJ gap 与 CLS-CWM p 值混在一起\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises. 两人共识: variant-level 分析应标注为 exploratory/descriptive。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3 for medium effect。CLS-TRAJ adjusted p=0.075 未通过 Holm-Bonferroni。R2 AGREE 并升级关注度。两人共识：Abstract 措辞需更审慎。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.4 Statistical power paragraph: n_eff≈86, power~0.3, transparent disclosure. Bayesian ROPE independently validates. Abstract 'not confirmed after multiple comparison correction' is accurate and cautious.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-N3 re-raises：power ~0.3 意味着 CLS-TRAJ 的'未确认等价'可能纯粹是 Type II error。CLS-CWM 与 CLS-TRAJ 的不对称结论在同一 power 下不应被解读为实质差异。R2 AGREE 并补充：variant-level P(ROPE)=0.970 vs per-test P(ROPE)=0.542 的不一致值得正文讨论。\"\n  action_items:\n    - round: 9\n      action: \"Variant-level 分析明确标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文讨论 TOST 功效限制；Abstract 'TRAJ parity differs' 改为更审慎措辞\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"Bayesian ROPE 等价性检验补充 TOST\"\n      assigned_to: \"experiment\"\n      status: resolved\n    - round: 12\n      action: \"正文更明确讨论 power ~0.3 意味着 CLS-TRAJ '未确认' 不应解读为 '非等价'；避免在 contribution list 中将 TRAJ model-contingent 作为稳健结论；讨论 variant-level vs per-test ROPE 不一致\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Repo 95.83% CI ~[85.7%, 99.5%].\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-Q4 re-raises: single-seed oracle 跨 seed 稳定性未验证。\"\n    - round: 10\n      reviewers: []\n      note: \"Cross-seed oracle 94.27±2.59% 已在正文。R10 未被提出。\"\n  resolution: \"Cross-seed oracle 94.27±2.59% (3 seeds) 加入正文 §5.6。R10 未再被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"Appendix 已讨论 Qwen3 CWM 无 epoch-level checkpoint。\"\n    - round: 10\n      reviewers: []\n      note: \"本轮未被提出。Appendix O 讨论了 Qwen3 仅有 step-level checkpoints。\"\n  resolution: \"Appendix O 已讨论。R9/R10 均未再被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder，Abstract/Intro 未标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM (ICLR 2025) + RepoExec + Chen et al.\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入 Related Work。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B+mid-training)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director 裁定 Should-Fix.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。R1 部分 REBUT（4B→8B gap 扩大数据）。两人共识：abstract/conclusion 需 ≤8B 限定。\"\n  resolution: \"合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成（gap ≈ 0）。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director: Findings track 合适.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 2.5/5. R2 评 3.0 (Findings), R1 评 3.5 (Borderline Conference).\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5. 两人共识：Findings 合适。合并至 R6-N4 追踪。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Excitement consensus at 3/5. R1 Overall 3.5 (soundness compensates), R2 Overall 3.0 (excitement ceiling). Inherent limitation, wont_fix. Merged with R6-N4.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1 Excitement 3/5, R2 Excitement 2/5. R1 Overall 3.5, R2 Overall 3.0. 分歧 persist。\"\n  resolution: \"合并至 R6-N4。Excitement 提升至 3.0/5 但 Conference 水平仍未达到。Inherent limitation：贡献类型为 empirical comparison，无法通过修改改变。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示; scaling 2-seed power 极低\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W5: HC1 不 account for residual within-cluster correlation.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-M1: 建议在 Appendix M 并列展示 logistic regression odds ratios。R2 AGREE。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. Appendix M now includes complete GEE logistic regression.\"\n  action_items:\n    - round: 10\n      action: \"Appendix M 补充 logistic regression marginal effects 或 odds ratios\"\n      assigned_to: \"agent\"\n      status: resolved\n  resolution: \"Appendix M 补充 GEE logistic regression。Commit 0b38a2b 修正过强显著性声明。R11 两位 Reviewer 一致确认 RESOLVED。\"\n  resolution_round: 11\n\n# === Round 9 (Fresh Review) Issues ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度——实际只比较三个已知 formulation，标题与贡献不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性（exact matching + majority-class default）未量化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W3 re-raises exact string matching。R2 REBUT：relaxed matching 扩大 gap（26→27pp），parseable accuracy 38-43%。瓶颈是语义的。\"\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大而非缩小 gap，parseable accuracy 远低于 majority baseline。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却在 Abstract 声称 'model-dependent'——泛化性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"R10 commit a58c178: Abstract 改为 'TRAJ parity is model-dependent and not confirmed after multiple comparison correction'。R10 未再被提出。\"\n  resolution_round: 10\n\n- id: \"R9-M1\"\n  summary: \"Figure 3 (Appendix) y-axis 不从 0 开始但未标注\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Figure 3 caption 标注 y-axis 不从零开始。合并至 R6-M3，一并 RESOLVED。\"\n  resolution_round: 11\n\n- id: \"R9-M2\"\n  summary: \"Abstract 第一句过于绝对 ('relies on')\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"已改为 'increasingly leverages'。\"\n  resolution_round: 10\n\n- id: \"R9-M3\"\n  summary: \"缺少方法论引用：Wellek (2010) 等价检验教材, Moulton (1990) clustered data\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"两篇已引用。\"\n  resolution_round: 10\n\n- id: \"R9-M4\"\n  summary: \"Clustered bootstrap 实施细节（resample unit, block size）未说明\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§3.1 已说明 resample unit。\"\n  resolution_round: 10\n\n- id: \"R9-M5\"\n  summary: \"Repo-level DEFF=114.3 → effective n≈86 未在正文讨论对推断的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: §5.2 加入 TOST power 段落。\"\n  resolution_round: 10\n\n# === Round 10 (Fresh Review) New Issues ===\n\n- id: \"R10-W1\"\n  summary: \"Python-only 评估未在 Limitations 提及\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: Limitations 加入 Python-only 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-W2\"\n  summary: \"'formulation choice is governed by code complexity' 等 overclaim 措辞\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: 'governed by' 改为 'moderated by'。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"3-shot ICL collapse 发现仅正文一句带过，未充分讨论 implication\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: §5.4 扩展 ICL 段落。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"Appendix 16 个（A-P），导航不便\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: Appendix 开头加入 mini TOC。\"\n  resolution_round: 10\n\n# === Round 11 (Continue Review) New Issues ===\n\n- id: \"R11-M1\"\n  summary: \"Figure 2 中 14B 单 seed 数据点与多 seed 数据点视觉等权，可能导致 gap reversal 被过度解读\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Figure 2 已更新：8B→14B 段虚线连接，14B 空心 marker，'exploratory' 灰色背景标注。\"\n  resolution_round: 11\n\n- id: \"R11-M2\"\n  summary: \"§3.5 main text 引用 LPM model identity 效应 (p=0.001) 但 GEE 给出 p=0.410，需加 qualifier\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"已在 commit 0b38a2b 中修复。\"\n  resolution_round: 11\n\n- id: \"R11-M3\"\n  summary: \"Abstract 'motivate routing' 暗示 routing 有前景，但正文数据显示 simple routing capture <0.4pp\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Abstract 已改为包含负结果量化。\"\n  resolution_round: 11\n\n# === Round 12 (Fresh Review) New Issues ===\n\n- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B + execution trace pretraining，repo-level 核心发现可能是 capacity artifact\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"两人独立提出（R1-N1, R2-N2），交叉分享后双方 AGREE。R1: 实质上在证明'小模型不能生成长且连贯的文本'。R2: format collapse 可能反映模型容量而非 formulation 差异。14B function-level gap 收敛至 0.43pp 支持 capacity-driven 假设。Appendix I(c) 的意外训练证据（CWM 训练在 CLS 格式数据上达到 86.05% + 0% unparseable）进一步表明退化来自 trace generation 复杂度而非 verification task。\"\n  action_items:\n    - round: 12\n      action: \"Introduction §1 contribution (2) 'formulation choice is moderated by code complexity' 需加 '≤8B LoRA' 限定\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 12\n      action: \"如有可能，增加 14B CWM repo-level 数据点（即使单 seed）以验证 gap 是否随 capacity 缩小\"\n      assigned_to: \"experiment\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-N2\"\n  summary: \"Qwen3 CWM optimal checkpoint（step 300-400）的 repo-level accuracy 未评估——论文持有 checkpoint 但未报告关键数据\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 提出（R1-N2），R2 完全 AGREE。Table 16 显示 eval loss 最低点在 step 300-400，final epoch 膨胀 1.8×。DeepSeek early-stop 显示 +18.14pp improvement（75.45% vs 57.31%），暗示 Qwen3 optimal checkpoint 可能显著缩小 18-26pp gap。R2 补充：即使 early-stopped DeepSeek CWM (75.45%) 仍低于 CLS (82-85%)，format collapse (66.4% unparseable) 在训练早期已存在——说明过拟合加剧但非唯一原因。\"\n  action_items:\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy（准确率 + unparseable rate）并在正文中报告\"\n      assigned_to: \"experiment\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-N3\"\n  summary: \"CLS-TRAJ 等价性的不对称结论可能完全是 power ~0.3 的 artifact，不应被呈现为稳健发现\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 提出，R2 AGREE。Power ~0.3 下，CLS-CWM 等价性确认（TOST p=0.007, P(ROPE)=0.975）与 CLS-TRAJ 未确认（adjusted p=0.075, P(ROPE)=0.542）的不对称可能纯粹是 Type II error。R2 补充：variant-level P(ROPE)=0.970 vs per-test P(ROPE)=0.542 的不一致也值得正文讨论。\"\n  action_items:\n    - round: 12\n      action: \"正文明确讨论 power ~0.3 对 CLS-TRAJ 结论的影响；报告 CLS-TRAJ 等价性所需最小样本量；讨论 variant-level vs per-test ROPE 不一致\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W1\"\n  summary: \"贡献列表仅两条，failure mode taxonomy 未列为独立贡献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 完全 AGREE。Table 4 (format collapse / decision collapse / aggregation penalty) 是论文最具实用价值的输出之一，目前未在 contribution list 中体现。增加第三条贡献不会膨胀论文——工作已完成，只是 framing 不足。\"\n  action_items:\n    - round: 12\n      action: \"§1 contribution list 增加第三条：failure mode taxonomy\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"GenRM 对比发现（generation advantage 在代码领域失效）未被充分讨论，仅在 Related Work 一段\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 AGREE。Hosseini et al. (ICLR 2025) GenRM 在数学推理中 generation > classification，本文在代码领域发现相反结论。这是论文最有潜力成为 surprising finding 的地方，但仅在 §4 Related Work 和 Appendix H(k) 中讨论。应提升到 Discussion/Conclusion 级别。\"\n  action_items:\n    - round: 12\n      action: \"将 GenRM 对比（generation advantage 的 domain-specificity）提升到 Discussion/Conclusion 中展开\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W3\"\n  summary: \"Repo-level 数据处理不一致（drop vs truncate）与 checkpoint 选择策略耦合形成 confound chain\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W3 提出，R2 AGREE。DeepSeek CLS accuracy 从 82.61% (s42 drop) 到 74.93% (s123 truncate) 有 7.68pp 偏差。Truncate → NaN val loss → final epoch default 形成 confound chain。正文仅在 Appendix N 讨论，应更显著呈现。\"\n  action_items:\n    - round: 12\n      action: \"在正文 §3.7 中更显著报告 preprocessing-checkpoint confound chain 及其 7.68pp impact\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W4\"\n  summary: \"CLS-CWM paired comparison 使用不同 seeds（CLS s123 vs CWM s42），cross-seed pairing 局限性未讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 AGREE。Function-level seed noise (<2pp) 不能直接外推到 repo-level（DeepSeek CLS 两 matched seeds ±2.50 std）。\"\n  action_items:\n    - round: 12\n      action: \"报告同 seed paired comparison（如有），或更明确讨论 cross-seed pairing 对 repo-level 结论的局限性\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M1\"\n  summary: \"§2.2 Failure Modes 位于 method section 造成结构困惑——实为理论预测而非方法设计\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。§2.2 是理论分析/预测，更适合放在 §3 Experiments 或与 Table 4 相邻。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M2\"\n  summary: \"Appendix G' prime 符号命名不直观\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。改为 G.2 或独立 appendix 编号。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M3\"\n  summary: \"wei2022emergent 引用类型不一致——TMLR 应为 article 而非 inproceedings\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [2]\n      note: \"Minor formatting issue.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M4\"\n  summary: \"Figure 2 首次引用在 page 4-5 但实际出现在 page 7，float 漂移 2-3 页\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [visual_check]\n      note: \"视觉审查 Agent 标记：Figure 2 float 漂移约 2-3 页，建议调整 float 位置参数。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === Prior Round Issues (unchanged) ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告 + R6-N2 resolved。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"通过 R6-W7 修复（185 词）。\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"已改为 consistency check。\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"多重比较\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"Holm-Bonferroni (k=4) 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"引用无幻觉。\"\n  resolution_round: 5\n\n- id: \"R3-W1\"\n  summary: \"Limitations 非独立 section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"独立 section 已有。\"\n  resolution_round: 5\n"
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
    "issues_yaml": "\n# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 11\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 12\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → final epoch). 但 R7 的 CLS epoch ablation (<1pp) 仍有效。新角度：CWM NaN val loss 可能是 formulation-inherent。\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。但 R2 REBUT：Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp。Director 裁定：证据表明 checkpoint 差异无法解释 18-26pp gap，降为 Should-Fix（正文更显著讨论此缓解证据）。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-N2 升级为 critical：论文持有 Qwen3 CWM step 300-400 optimal checkpoints（Table 16 显示 eval loss 最低点）但未评估其 repo-level accuracy。DeepSeek early-stop +18.14pp (75.45% vs 57.31%) 暗示 Qwen3 optimal checkpoint 可能显著缩小 gap。R2 完全 AGREE。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因（formulation-inherent vs implementation issue）\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文（非仅 Appendix）更显著讨论 checkpoint 缓解证据（matched epoch-3 gap 仍 20-23pp + CLS ablation <1pp）\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy 并报告结果\"\n      assigned_to: \"experiment\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 12\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1: 'design space' framing 过度. R1 部分同意.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1 再次标 CRITICAL：三种公式均为已有方法，核心发现可从直觉预期。R1 AGREE 但认为 failure mode taxonomy 有独立贡献。两人共识：Findings 合适，Main 不够。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. R2 STILL_OPEN (excitement improved 2.5→3.0 but core contribution type unchanged). R1 AGREE on assessment but argues exceptional soundness partially compensates. Cross-sharing: R1 cites methodological demonstration value + failure mode taxonomy + 14B forward-looking insight. R2 rebuts: soundness ≠ excitement, ARR separates them for a reason. Both accept 3.0-3.5 range. Director: inherent limitation, wont_fix.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R2-N1 标 CRITICAL (Excitement 2/5)：核心发现（func-level equiv + repo-level collapse）可从 §2.2 理论分析直接预期，缺中间复杂度数据。R1 REBUT：引用 ARR H1 条款，认为'可预期≠无价值'，gap magnitude 和四项干预失败不可预期。但 R1 同意 failure mode taxonomy 应提升为贡献。最终分歧：R1 Excitement 3/5, R2 Excitement 2/5。\"\n  action_items:\n    - round: 9\n      action: \"标题从 'design space' 调整为 'systematic comparison'\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"增加轻量 routing/ensemble 实验以提升 excitement\"\n      assigned_to: \"experiment\"\n      status: resolved\n    - round: 10\n      action: \"Bayesian ROPE 等价性检验增强 equivalence 证据\"\n      assigned_to: \"experiment\"\n      status: resolved\n    - round: 10\n      action: \"≥14B 模型单点验证\"\n      assigned_to: \"experiment\"\n      status: resolved\n  resolution: \"所有可行 action items 已完成。Excitement 从 2.5 提升至 3.0，但核心贡献类型（empirical comparison of existing formulations）无法通过进一步修改改变。Novelty ceiling 为 inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 12\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"SESOI 基于训练噪声量级独立于 observed gap.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。缺 domain-specific justification.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W4 re-raises：±2pp 依赖于 accuracy range 和 test set size，更接近 post-hoc rationalization。R2 部分同意，建议重新定位为 'practically motivated with robustness check'。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-W1 re-raises：无 pre-registration，±1.52pp 临界值距 ±2pp 仅 0.48pp，结论对 SESOI 选择敏感。R2 AGREE。\"\n  action_items:\n    - round: 9\n      action: \"§3.4 加 domain-grounded SESOI justification; 正文引用 Appendix J sensitivity\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"SESOI 描述从 'a priori' 改为 'practically motivated'\"\n      assigned_to: \"paper\"\n      status: wont_fix\n    - round: 12\n      action: \"正文 §3.4 中引用 TOST sensitivity analysis（Appendix G），讨论 ±1.52pp 临界值；承认无 pre-registration\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"3+ 处修复完成。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Abstract 仍比 Conclusion 缺 qualifier.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未被独立提出。Abstract 已含 '≤8B LoRA protocol' qualifier。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标为 CRITICAL：≤8B 限制严重威胁泛化性。R1 部分 REBUT（4B→8B gap 扩大）但同意 abstract 需限定。两人共识：abstract/conclusion 应明确 '≤8B LoRA regime' 限定。\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 'under our ≤8B LoRA protocol'\"\n      assigned_to: \"agent\"\n      status: resolved\n    - round: 10\n      action: \"Conclusion 也加 ≤8B LoRA 限定；讨论更大规模下结论可能如何变化\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入 'All findings are conditioned on ≤8B LoRA fine-tuning; at larger scale, the generation bottleneck may diminish'。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"降级 diagnostic granularity\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 12\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W6: 175× 数据量差异.\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：180× 差异 + signal granularity (per-test vs variant-level) 无法通过 volume matching 解决。R2 AGREE。两人共识：应将 TRAJ 数据量/信号粒度限制框架为 formulation 固有属性。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-W4 re-raises：downsample 控制了 volume 但未控制 label granularity。R2 AGREE。两人共识：CLS vs TRAJ repo-level 比较本质上是 exploratory 而非 confirmatory。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性而非可控实验变量\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"Contribution summary 中明确表述 CLS-TRAJ repo-level 比较包含 training regime confound（data volume + label granularity），结论为 exploratory\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成，在 §3.5 和 Appendix M 报告。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Aletheia/VeRPO/ExecVerify.\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"三篇已加入。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"新增: GenRM, RepoExec, Chen et al.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W5: CodeScaler. 另提 GenPRM, ExecVerify.\"\n    - round: 10\n      reviewers: [2]\n      note: \"R2-W2: CodeRM (Ma et al., ACL 2025) 未引用。另需加强 ORM/PRM 框架映射讨论。R1 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"验证 CodeRM 真实性后加入 Related Work；加半段 CLS↔PRM/CWM↔generative verifier 映射讨论\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: CodeRM (Ma et al., ACL 2025) 加入 Related Work，ORM/PRM 映射段落加入（CLS→PRM-like process, TRAJ→ORM-like outcome, CWM→generative verifier）。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 11\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"bar labels 偏小.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-M2: y-axis 不从零开始（55%），视觉夸大 gap。R2 AGREE。Caption 已标注但对快速浏览读者可能误导。视觉审查也标记。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. Y-axis non-zero start acceptable for 0-3pp differences; caption annotated. R1 confirms 55% start with sufficient visual context. R2 confirms caption标注充分。\"\n  action_items:\n    - round: 10\n      action: \"Figure 2 y-axis 改从 0 开始\"\n      assigned_to: \"agent\"\n      status: resolved\n  resolution: \"Figure 2 y-axis 从约 55-80% 起始（版本差异），caption 标注 'y-axis does not start at zero'。两位 Reviewer 一致确认：对 0-3pp 差异展示，非零起始合理，caption 标注充分。\"\n  resolution_round: 11\n\n# === Round 8 (Fresh Review) Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆: §5.2 将 CLS-TRAJ gap 与 CLS-CWM p 值混在一起\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises. 两人共识: variant-level 分析应标注为 exploratory/descriptive。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3 for medium effect。CLS-TRAJ adjusted p=0.075 未通过 Holm-Bonferroni。R2 AGREE 并升级关注度。两人共识：Abstract 措辞需更审慎。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.4 Statistical power paragraph: n_eff≈86, power~0.3, transparent disclosure. Bayesian ROPE independently validates. Abstract 'not confirmed after multiple comparison correction' is accurate and cautious.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-N3 re-raises：power ~0.3 意味着 CLS-TRAJ 的'未确认等价'可能纯粹是 Type II error。CLS-CWM 与 CLS-TRAJ 的不对称结论在同一 power 下不应被解读为实质差异。R2 AGREE 并补充：variant-level P(ROPE)=0.970 vs per-test P(ROPE)=0.542 的不一致值得正文讨论。\"\n  action_items:\n    - round: 9\n      action: \"Variant-level 分析明确标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文讨论 TOST 功效限制；Abstract 'TRAJ parity differs' 改为更审慎措辞\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"Bayesian ROPE 等价性检验补充 TOST\"\n      assigned_to: \"experiment\"\n      status: resolved\n    - round: 12\n      action: \"正文更明确讨论 power ~0.3 意味着 CLS-TRAJ '未确认' 不应解读为 '非等价'；避免在 contribution list 中将 TRAJ model-contingent 作为稳健结论；讨论 variant-level vs per-test ROPE 不一致\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Repo 95.83% CI ~[85.7%, 99.5%].\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-Q4 re-raises: single-seed oracle 跨 seed 稳定性未验证。\"\n    - round: 10\n      reviewers: []\n      note: \"Cross-seed oracle 94.27±2.59% 已在正文。R10 未被提出。\"\n  resolution: \"Cross-seed oracle 94.27±2.59% (3 seeds) 加入正文 §5.6。R10 未再被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"Appendix 已讨论 Qwen3 CWM 无 epoch-level checkpoint。\"\n    - round: 10\n      reviewers: []\n      note: \"本轮未被提出。Appendix O 讨论了 Qwen3 仅有 step-level checkpoints。\"\n  resolution: \"Appendix O 已讨论。R9/R10 均未再被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder，Abstract/Intro 未标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM (ICLR 2025) + RepoExec + Chen et al.\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入 Related Work。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B+mid-training)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director 裁定 Should-Fix.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。R1 部分 REBUT（4B→8B gap 扩大数据）。两人共识：abstract/conclusion 需 ≤8B 限定。\"\n  resolution: \"合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成（gap ≈ 0）。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director: Findings track 合适.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 2.5/5. R2 评 3.0 (Findings), R1 评 3.5 (Borderline Conference).\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5. 两人共识：Findings 合适。合并至 R6-N4 追踪。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Excitement consensus at 3/5. R1 Overall 3.5 (soundness compensates), R2 Overall 3.0 (excitement ceiling). Inherent limitation, wont_fix. Merged with R6-N4.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1 Excitement 3/5, R2 Excitement 2/5. R1 Overall 3.5, R2 Overall 3.0. 分歧 persist。\"\n  resolution: \"合并至 R6-N4。Excitement 提升至 3.0/5 但 Conference 水平仍未达到。Inherent limitation：贡献类型为 empirical comparison，无法通过修改改变。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示; scaling 2-seed power 极低\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W5: HC1 不 account for residual within-cluster correlation.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-M1: 建议在 Appendix M 并列展示 logistic regression odds ratios。R2 AGREE。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. Appendix M now includes complete GEE logistic regression.\"\n  action_items:\n    - round: 10\n      action: \"Appendix M 补充 logistic regression marginal effects 或 odds ratios\"\n      assigned_to: \"agent\"\n      status: resolved\n  resolution: \"Appendix M 补充 GEE logistic regression。Commit 0b38a2b 修正过强显著性声明。R11 两位 Reviewer 一致确认 RESOLVED。\"\n  resolution_round: 11\n\n# === Round 9 (Fresh Review) Issues ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度——实际只比较三个已知 formulation，标题与贡献不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性（exact matching + majority-class default）未量化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W3 re-raises exact string matching。R2 REBUT：relaxed matching 扩大 gap（26→27pp），parseable accuracy 38-43%。瓶颈是语义的。\"\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大而非缩小 gap，parseable accuracy 远低于 majority baseline。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却在 Abstract 声称 'model-dependent'——泛化性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"R10 commit a58c178: Abstract 改为 'TRAJ parity is model-dependent and not confirmed after multiple comparison correction'。R10 未再被提出。\"\n  resolution_round: 10\n\n- id: \"R9-M1\"\n  summary: \"Figure 3 (Appendix) y-axis 不从 0 开始但未标注\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Figure 3 caption 标注 y-axis 不从零开始。合并至 R6-M3，一并 RESOLVED。\"\n  resolution_round: 11\n\n- id: \"R9-M2\"\n  summary: \"Abstract 第一句过于绝对 ('relies on')\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"已改为 'increasingly leverages'。\"\n  resolution_round: 10\n\n- id: \"R9-M3\"\n  summary: \"缺少方法论引用：Wellek (2010) 等价检验教材, Moulton (1990) clustered data\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"两篇已引用。\"\n  resolution_round: 10\n\n- id: \"R9-M4\"\n  summary: \"Clustered bootstrap 实施细节（resample unit, block size）未说明\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§3.1 已说明 resample unit。\"\n  resolution_round: 10\n\n- id: \"R9-M5\"\n  summary: \"Repo-level DEFF=114.3 → effective n≈86 未在正文讨论对推断的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: §5.2 加入 TOST power 段落。\"\n  resolution_round: 10\n\n# === Round 10 (Fresh Review) New Issues ===\n\n- id: \"R10-W1\"\n  summary: \"Python-only 评估未在 Limitations 提及\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: Limitations 加入 Python-only 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-W2\"\n  summary: \"'formulation choice is governed by code complexity' 等 overclaim 措辞\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: 'governed by' 改为 'moderated by'。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"3-shot ICL collapse 发现仅正文一句带过，未充分讨论 implication\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: §5.4 扩展 ICL 段落。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"Appendix 16 个（A-P），导航不便\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: Appendix 开头加入 mini TOC。\"\n  resolution_round: 10\n\n# === Round 11 (Continue Review) New Issues ===\n\n- id: \"R11-M1\"\n  summary: \"Figure 2 中 14B 单 seed 数据点与多 seed 数据点视觉等权，可能导致 gap reversal 被过度解读\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Figure 2 已更新：8B→14B 段虚线连接，14B 空心 marker，'exploratory' 灰色背景标注。\"\n  resolution_round: 11\n\n- id: \"R11-M2\"\n  summary: \"§3.5 main text 引用 LPM model identity 效应 (p=0.001) 但 GEE 给出 p=0.410，需加 qualifier\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"已在 commit 0b38a2b 中修复。\"\n  resolution_round: 11\n\n- id: \"R11-M3\"\n  summary: \"Abstract 'motivate routing' 暗示 routing 有前景，但正文数据显示 simple routing capture <0.4pp\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Abstract 已改为包含负结果量化。\"\n  resolution_round: 11\n\n# === Round 12 (Fresh Review) New Issues ===\n\n- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B + execution trace pretraining，repo-level 核心发现可能是 capacity artifact\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"两人独立提出（R1-N1, R2-N2），交叉分享后双方 AGREE。R1: 实质上在证明'小模型不能生成长且连贯的文本'。R2: format collapse 可能反映模型容量而非 formulation 差异。14B function-level gap 收敛至 0.43pp 支持 capacity-driven 假设。Appendix I(c) 的意外训练证据（CWM 训练在 CLS 格式数据上达到 86.05% + 0% unparseable）进一步表明退化来自 trace generation 复杂度而非 verification task。\"\n  action_items:\n    - round: 12\n      action: \"Introduction §1 contribution (2) 'formulation choice is moderated by code complexity' 需加 '≤8B LoRA' 限定\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 12\n      action: \"如有可能，增加 14B CWM repo-level 数据点（即使单 seed）以验证 gap 是否随 capacity 缩小\"\n      assigned_to: \"experiment\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-N2\"\n  summary: \"Qwen3 CWM optimal checkpoint（step 300-400）的 repo-level accuracy 未评估——论文持有 checkpoint 但未报告关键数据\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 提出（R1-N2），R2 完全 AGREE。Table 16 显示 eval loss 最低点在 step 300-400，final epoch 膨胀 1.8×。DeepSeek early-stop 显示 +18.14pp improvement（75.45% vs 57.31%），暗示 Qwen3 optimal checkpoint 可能显著缩小 18-26pp gap。R2 补充：即使 early-stopped DeepSeek CWM (75.45%) 仍低于 CLS (82-85%)，format collapse (66.4% unparseable) 在训练早期已存在——说明过拟合加剧但非唯一原因。\"\n  action_items:\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy（准确率 + unparseable rate）并在正文中报告\"\n      assigned_to: \"experiment\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-N3\"\n  summary: \"CLS-TRAJ 等价性的不对称结论可能完全是 power ~0.3 的 artifact，不应被呈现为稳健发现\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 提出，R2 AGREE。Power ~0.3 下，CLS-CWM 等价性确认（TOST p=0.007, P(ROPE)=0.975）与 CLS-TRAJ 未确认（adjusted p=0.075, P(ROPE)=0.542）的不对称可能纯粹是 Type II error。R2 补充：variant-level P(ROPE)=0.970 vs per-test P(ROPE)=0.542 的不一致也值得正文讨论。\"\n  action_items:\n    - round: 12\n      action: \"正文明确讨论 power ~0.3 对 CLS-TRAJ 结论的影响；报告 CLS-TRAJ 等价性所需最小样本量；讨论 variant-level vs per-test ROPE 不一致\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W1\"\n  summary: \"贡献列表仅两条，failure mode taxonomy 未列为独立贡献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 完全 AGREE。Table 4 (format collapse / decision collapse / aggregation penalty) 是论文最具实用价值的输出之一，目前未在 contribution list 中体现。增加第三条贡献不会膨胀论文——工作已完成，只是 framing 不足。\"\n  action_items:\n    - round: 12\n      action: \"§1 contribution list 增加第三条：failure mode taxonomy\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"GenRM 对比发现（generation advantage 在代码领域失效）未被充分讨论，仅在 Related Work 一段\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 AGREE。Hosseini et al. (ICLR 2025) GenRM 在数学推理中 generation > classification，本文在代码领域发现相反结论。这是论文最有潜力成为 surprising finding 的地方，但仅在 §4 Related Work 和 Appendix H(k) 中讨论。应提升到 Discussion/Conclusion 级别。\"\n  action_items:\n    - round: 12\n      action: \"将 GenRM 对比（generation advantage 的 domain-specificity）提升到 Discussion/Conclusion 中展开\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W3\"\n  summary: \"Repo-level 数据处理不一致（drop vs truncate）与 checkpoint 选择策略耦合形成 confound chain\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W3 提出，R2 AGREE。DeepSeek CLS accuracy 从 82.61% (s42 drop) 到 74.93% (s123 truncate) 有 7.68pp 偏差。Truncate → NaN val loss → final epoch default 形成 confound chain。正文仅在 Appendix N 讨论，应更显著呈现。\"\n  action_items:\n    - round: 12\n      action: \"在正文 §3.7 中更显著报告 preprocessing-checkpoint confound chain 及其 7.68pp impact\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W4\"\n  summary: \"CLS-CWM paired comparison 使用不同 seeds（CLS s123 vs CWM s42），cross-seed pairing 局限性未讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 AGREE。Function-level seed noise (<2pp) 不能直接外推到 repo-level（DeepSeek CLS 两 matched seeds ±2.50 std）。\"\n  action_items:\n    - round: 12\n      action: \"报告同 seed paired comparison（如有），或更明确讨论 cross-seed pairing 对 repo-level 结论的局限性\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M1\"\n  summary: \"§2.2 Failure Modes 位于 method section 造成结构困惑——实为理论预测而非方法设计\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。§2.2 是理论分析/预测，更适合放在 §3 Experiments 或与 Table 4 相邻。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M2\"\n  summary: \"Appendix G' prime 符号命名不直观\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。改为 G.2 或独立 appendix 编号。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M3\"\n  summary: \"wei2022emergent 引用类型不一致——TMLR 应为 article 而非 inproceedings\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [2]\n      note: \"Minor formatting issue.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M4\"\n  summary: \"Figure 2 首次引用在 page 4-5 但实际出现在 page 7，float 漂移 2-3 页\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [visual_check]\n      note: \"视觉审查 Agent 标记：Figure 2 float 漂移约 2-3 页，建议调整 float 位置参数。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === Prior Round Issues (unchanged) ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告 + R6-N2 resolved。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"通过 R6-W7 修复（185 词）。\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"已改为 consistency check。\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"多重比较\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"Holm-Bonferroni (k=4) 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"引用无幻觉。\"\n  resolution_round: 5\n\n- id: \"R3-W1\"\n  summary: \"Limitations 非独立 section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"独立 section 已有。\"\n  resolution_round: 5\n"
  }
}
```

</details>

---


### Tool result

_source line 983 · 2026-05-23T09:17:32.988985+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 32808}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 984 · 2026-05-23T09:20:18.393306+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "\n# 审稿报告 — Round 12 (Fresh Review)\n\n**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 via ACL ARR\n**审稿模式**: Fresh（无前轮记忆）\n**Reviewer 编排**: R1（方法严谨性 + 实验设计 + 统计分析）+ R2（新颖性 + 相关工作 + 写作 + 格式）\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free 代码修复验证 formulation：CLS（per-test 二分类）、CWM（执行输出生成）和 TRAJ（trajectory-level patch 评分），在两个代码 LLM 家族（Qwen3、DeepSeek-Coder）、两个复杂度级别、多 seed 下使用 ≤8B LoRA fine-tuning 进行匹配实验。核心发现：(1) function-level 下 CLS-CWM 统计等价（TOST p=0.007, 5 seeds, Bayesian ROPE P=0.975）；(2) repo-level 下 CWM 因 format collapse 退化 18-26pp（z=-23.7, DeepSeek-Coder）；(3) 14B 时 function-level gap 收窄至 0.43pp（TOST p=0.0006），一致于 capacity-dependent convergence；(4) error complementarity 和 failure mode taxonomy 为实践选择提供指导。\n\n---\n\n## Strengths\n\n**S1. 统计方法论远超同领域论文一般水准。** TOST 等价性检验 + Holm-Bonferroni 校正 + clustered bootstrap（114 clusters, 10K resamples）+ mixed-effects LPM/GEE 双模型验证 + Bayesian ROPE 分析——这套统计工具箱的部署深度和一致性为 NLP 实证研究设立了方法论标杆。[R1, R2 一致]\n\n**S2. Threats to validity 分析异常详尽和诚实。** §3.7 和 Appendix N 系统识别了五个潜在 confound（checkpoint, sequence length, preprocessing, TRAJ regime, CWM scale）并逐一评估，自我批评程度超过多数投稿论文。论文对自身局限性的坦诚值得肯定。[R1, R2 一致]\n\n**S3. Failure mode taxonomy 有独立实用价值。** Table 4 的三类故障模式（format collapse / decision collapse / aggregation penalty）为从业者提供了可操作的诊断框架，在给定模型和 formulation 下预测可能的失败模式。[R1, R2 一致]\n\n**S4. 实验设计在 ≤8B LoRA 范围内实现了高匹配度。** 控制了模型容量、训练数据、LoRA 配置、compute 等变量，在其约束范围内确实实现了 matched comparison。Hyperparameters 完整报告（Table 11），compute budget 明确（~370 GPU-hours），prompt templates 提供。[R1]\n\n**S5. Comprehensive ablation program。** LoRA rank, majority voting, sequence length, data size, preprocessing, few-shot, checkpoint 的系统消融，使 repo-level 结论有更强的因果推断基础（四项干预全部失败排除了多个替代解释）。[R1]\n\n---\n\n## Weaknesses\n\n### Must-Fix（共识 Critical）\n\n**C1. CWM baseline 生态效度——核心方法论 confound [R1-N1, R2-N2, 双方 AGREE]**\n\n论文标题声称比较\"verification formulations\"，但 repo-level 核心发现（CWM 退化 18-26pp）完全建立在 ≤8B LoRA fine-tuning 之上。CWM 需生成 ~477 tokens/instance vs CLS 仅 1 token；在小模型无 execution-trace pretraining 条件下，长文本生成退化是已知现象。14B function-level gap 收敛至 0.43pp（TOST p=0.0006）反而支持\"capacity drives the gap\"假设。论文虽在 Abstract 提到\"under our ≤8B LoRA protocol\"、§3.7 和 Appendix N 有详细讨论，但 Introduction §1 contribution (2) \"formulation choice is moderated by code complexity\" 读起来像一般性结论，未加 regime 限定。\n\nAppendix I(c) 的意外训练证据进一步加深了这一质疑：CWM 模型误训在 CLS 格式数据上后达到 86.05% accuracy + 0% unparseable——表明退化来自 trace generation 复杂度而非 verification task 本身。\n\n**必须修改**：(a) Title 和 Introduction contribution 中明确限定\"under ≤8B LoRA fine-tuning\"；(b) 如有可能，增加 14B CWM repo-level 数据点以验证 gap 是否随 capacity 缩小——这将直接决定核心结论的定性方向。\n\n**C2. Qwen3 CWM optimal checkpoint 未评估——论文持有关键数据但未报告 [R1-N2, R2 AGREE]**\n\nTable 16（Appendix L）显示 Qwen3-8B CWM eval loss 在 step 300-400 达到最小值（~0.29），final epoch（step 6600）膨胀至 ~0.52（1.8×）。论文确认 Qwen3 有 step 300/400 checkpoints 但**未报告其 repo-level accuracy**。DeepSeek 的 early-stopping 数据显示 +18.14pp improvement（75.45% vs 57.31%），暗示 Qwen3 optimal checkpoint 可能显著缩小 gap。\n\nR2 补充了重要 nuance：即使 early-stopped DeepSeek CWM 达到 75.45%，仍低于 CLS (82-85%)，且保持 66.4% unparseable rate——format collapse 在训练早期已存在，过拟合加剧但非唯一原因。缩小后的 gap (~10pp) 仍然 non-trivial，但显著改变了 gap 的解释。\n\n**必须修改**：评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy 和 unparseable rate，并在正文中报告。\n\n**C3. 统计功效不足导致 CLS-TRAJ 等价性结论不可靠 [R1-N3, R2 AGREE]**\n\nn_eff ≈ 86, TOST power ~0.3。CLS-CWM 等价性确认（TOST p=0.007, P(ROPE)=0.975）与 CLS-TRAJ 未确认（adjusted p=0.075, P(ROPE)=0.542 per-test）的不对称结论可能完全是 power 不足的 artifact——在 power ~0.3 下，Type II error 概率达 70%。论文在贡献声明中将\"TRAJ equivalence is not confirmed after multiple comparison correction\"与\"CLS-CWM equivalence\"并列，读者可能误解为\"CLS-TRAJ 不等价\"。\n\nR2 补充：Bayesian ROPE 在 variant-level 给出 P(ROPE)=0.970（支持等价），但 per-test level 为 0.542（inconclusive）。两个 analysis level 的不一致未在正文中讨论。\n\n**必须修改**：(a) 正文更明确讨论 power ~0.3 意味着\"未确认\"不等于\"非等价\"；(b) 讨论 variant-level vs per-test ROPE 的不一致及其原因；(c) 避免在 contribution list 中将 TRAJ model-contingent 作为稳健结论呈现。\n\n### Should-Fix\n\n**W1. 贡献列表仅两条，failure mode taxonomy 未列为贡献 [R2-W2, R1 AGREE]**\nTable 4 的 taxonomy（format collapse / decision collapse / aggregation penalty）是论文最具实用价值的输出之一。应增加为第三条贡献。\n\n**W2. GenRM 对比发现未被充分讨论 [R2-W3, R1 AGREE]**\nHosseini et al. (ICLR 2025) 发现 generation-based verifier 在数学推理中优于 classification-based。本文发现在代码验证中相反。这一对比是论文最有潜力成为 surprising finding 的地方，但仅在 §4 Related Work 一段讨论。应提升到 Discussion/Conclusion 级别。\n\n**W3. SESOI ±2pp 无 pre-registration，结论对 SESOI 选择敏感 [R1-W1, R2 AGREE]**\n±1.52pp 临界值距 ±2pp 仅 0.48pp。如果 SESOI 设为 ±1.5pp，CLS-CWM 等价性就不确认。建议在正文引用 Appendix G sensitivity analysis 并承认 SESOI 的主观性。\n\n**W4. CLS-TRAJ 训练条件根本不匹配（~400 vs ~70K, label granularity 差异）[R1-W4, R2 AGREE]**\nDownsample ablation 控制了 data volume 但未控制 label granularity（per-test vs variant-level）。CLS vs TRAJ repo-level 比较本质上是 exploratory 而非 confirmatory。\n\n**W5. Repo-level 数据处理不一致（drop vs truncate + checkpoint confound chain）[R1-W3, R2 AGREE]**\nDeepSeek CLS accuracy 从 82.61% (drop) 到 74.93% (truncate) 有 7.68pp 偏差，truncate → NaN val loss → final epoch default 形成 confound chain。应在正文更显著呈现。\n\n**W6. CLS-CWM paired comparison 使用不同 seeds（CLS s123 vs CWM s42）[R1-W5, R2 AGREE]**\nFunction-level seed noise (<2pp) 不能直接外推到 repo-level（DeepSeek CLS ±2.50 std）。\n\n**W7. 种子数/实验配置不一致导致统计置信度参差不齐 [R2-W5, R1 AGREE]**\n不同比较使用 1-5 seeds，统计可靠性差异大但未系统标注。\n\n### Minor\n\n- M1: §2.2 Failure Modes 位于 method section 造成结构困惑（R2 提出, R1 AGREE）\n- M2: Appendix G' prime 符号命名不直观（R2 提出, R1 AGREE）\n- M3: `wei2022emergent` 引用类型不一致（R2）\n- M4: Figure 2 float 漂移 2-3 页（视觉审查）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **CWM baseline 公平性是核心问题**：两位 reviewer 独立提出，交叉分享后双方完全 AGREE。≤8B LoRA 对 CWM 系统性不公平，repo-level 核心发现可能是 capacity artifact 而非 formulation 差异。\n2. **Qwen3 CWM optimal checkpoint 未评估是重大遗漏**：R1 提出，R2 完全 AGREE。论文持有 step 300-400 checkpoints 但未报告 accuracy。\n3. **统计功效不足限制了 CLS-TRAJ 结论**：R1 提出，R2 AGREE。Power ~0.3 下\"未确认等价\"不应被呈现为\"model-contingent\"。\n4. **Failure mode taxonomy 应提升为贡献**：R2 提出，R1 完全 AGREE。\n5. **GenRM 对比应更深入讨论**：R2 提出，R1 AGREE。\n6. **统计方法论是突出优势**：双方一致肯定。\n7. **Threats to validity 讨论诚实详尽**：双方一致肯定。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **Excitement/Novelty（核心分歧）**：\n   - R2 (Excitement 2/5)：\"核心发现可从第一性原理预期，§2.2 理论分析就预测了实验结果\"\n   - R1 (Excitement 3/5)：\"'可预期'不等于'无价值'，引用 ARR H1 条款；gap magnitude 和四项干预失败不可预期\"\n   - **Director 判断**：R2 的关切更有说服力。论文的理论分析（§2.2）确实预测了实验结果的方向——function-level 等价和 repo-level 发散。虽然 magnitude 不可预期（R1 的论点），但 magnitude 的精确量化在 CWM baseline 公平性存疑的情况下（C1, C2）价值受限。R1 引用 ARR H1 是合理的，但 H1 旨在防止对 well-designed experiments confirming non-obvious hypotheses 的不公平驳回——本文的假设从自身理论框架看并非 non-obvious。\n\n2. **Abstract 统计密度**：\n   - R2：\"统计细节过密降低可读性\"\n   - R1：\"方法论论文需要在 Abstract 包含关键统计结果\"\n   - **Director 判断**：R1 的立场更合理。对于以统计方法论为核心卖点的论文，Abstract 中保留关键 p-value 和 effect size 是必要的。但可考虑精简至 2-3 个最关键数字。\n\n3. **两个模型家族是否足够**：\n   - R2：\"泛化性受限\"\n   - R1：\"ARR H4 不鼓励要求不必要的额外实验\"\n   - **Director 判断**：R1 的论点更有说服力。两个家族作为 primary + consistency check 是合理的实验经济性选择。降级为 Limitations 中提及即可。\n\n---\n\n## Questions\n\n1. Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy 是多少？\n2. 是否有 14B CWM 的 repo-level 数据？如有，gap 是否随 capacity 缩小？\n3. ±2pp SESOI 是否 pre-registered？如否，应在正文明确说明。\n4. NF4 quantization 对 CWM 长文本生成质量的具体影响是什么？\n5. CLS-TRAJ 等价性确认所需的最小样本量是多少（a priori power analysis）？\n\n---\n\n## Missing References\n\n- **Equivalence testing 在 NLP 中的应用先例**（如有）：会加强 TOST 方法选择的 motivation [R1]\n- **CVeDRL (arXiv:2601.22803, 2026)**：R2 提出但 R1 对其存在性和相关性存疑（difficulty-aware RL training 与本文 formulation comparison 主题有一定距离）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：✅ 完成（1 warning, 12 info）\n\n**Warning**:\n- Figure 2 首次引用在 page 4-5，但实际出现在 page 7 右栏（float 漂移 2-3 页）。建议调整 float 位置参数。\n\n**Info highlights**:\n- Figure 1 概念图清晰专业，三种 formulation 对比一目了然\n- Tables 1-4 均使用 booktabs 风格，格式规范\n- Figure 2 使用色盲友好双色方案，y-axis 非零起始已在 caption 标注\n- 正文在第 8 页结束，Limitations 为简短一段覆盖 3 个要点，符合 EMNLP 规范\n- Appendix 12 页（p12-22），表格密度高但作为 appendix 可接受\n- 无 [?] 未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**置信度: 4/5**\n\n**评分理由**：\n\n论文在方法论严谨性方面达到了 NLP 实证研究的高标准（S1, S2），failure mode taxonomy 有独立实用价值（S3），在 ≤8B LoRA 范围内的实验设计匹配度高（S4）。\n\n但三个核心问题限制了论文达到 Conference 水平：\n\n1. **CWM baseline 公平性（C1）**——这是最严重的问题。如果 repo-level 的 18-26pp gap 主要由 model capacity 而非 formulation 差异驱动（14B function-level 收敛至 0.43pp 提供了强间接证据），则论文的中心 claim（\"complexity-moderated formulation choice\"）的通用性大幅受限。论文需要在 Introduction 的贡献声明中更显著地限定这一点。\n\n2. **CWM checkpoint 遗漏（C2）**——论文持有 optimal checkpoint 但未报告其 accuracy，DeepSeek 的 early-stopping 数据暗示 gap 可能缩小约 18pp。这是一个可以执行但未执行的关键实验。\n\n3. **Novelty ceiling（R6-N4 系列）**——核心发现（function-level 等价 + repo-level 发散）可从论文自身的 §2.2 理论分析直接预期。虽然统计严谨的量化验证有价值，但在核心 claim 受 C1 和 C2 质疑的情况下，magnitude 的精确量化也失去了部分说服力。R1 (3.5, Borderline Conference) 和 R2 (3.0, Findings) 的评分差异主要反映对 novelty 的不同判断。\n\n**如果作者在 rebuttal 中能提供**：(a) Qwen3 CWM optimal checkpoint 的 repo-level accuracy，(b) 14B CWM repo-level 数据点——**评分可能上调至 3.5**。目前，Findings 是合适的定位。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution (2) \"formulation choice is moderated by code complexity\" 缺少 ≤8B LoRA 限定。这是核心 claim，应在首次出现时就明确限定条件。\n- 仅列出两条贡献。Failure mode taxonomy（Table 4）应作为第三条。\n- \"primarily methodological\" 的自我定位虽诚实但策略上不利——建议重新框定为揭示了 generation advantage 的 domain-specificity。\n\n### §2 Method\n- §2.2 Failure Modes 更适合放在 §3 Experiments 中，与 Table 4 的实证 taxonomy 相邻。当前位置在 Method section 会让读者误以为是方法设计而非理论预测。\n- Oracle Accuracy-Utility Framework（§2.3）的 ICC 参数来自 function-level 分析，在 repo-level 应用时存在 domain mismatch（repo-level ICC=0.3146 vs function-level ICC=0.191）。\n\n### §3 Experiments\n- Table 1: 信息密度高但缺少视觉分隔（primary results / cross-model / baselines 之间）。\n- §3.2 Scaling: \"At 8B, the ranking is CLS > TRAJ > CWM\"——这三个数字基于 2 seeds，排名的统计置信度有限。\n- §3.4 Equivalence: TOST sensitivity analysis 结果（±1.52pp 临界值）应在正文中引用和讨论，而非仅放在 Appendix G。\n- §3.4 Statistical power 段落已有（good），但应更明确说明 power ~0.3 意味着 CLS-TRAJ 的 non-confirmation 是 inconclusive 而非 negative。\n- §3.5 Repo-Level: CWM convergence analysis 确认了 systematic overfitting，但 Qwen3 optimal checkpoint 的 accuracy 是关键缺失数据。\n- §3.6 Analysis: Oracle combination 基于 single-seed，应更醒目标注。\n- §3.7 Threats: preprocessing-checkpoint confound chain 应更显著呈现。\n\n### §4 Related Work\n- GenRM 对比发现（generation advantage 在代码领域失效）是论文最有潜力的 insight，但埋在 Related Work 中。应提升至 Discussion 级别。\n- 三段式组织（Execution Simulation / Process vs Outcome / Repair & Task Framing）清晰合理。\n- 引用真实性抽查通过，未发现幻觉引用。\n\n### §5 Conclusion\n- \"Primary statistical findings are established under ≤8B LoRA fine-tuning\" 是正确且必要的限定。\n- Future direction (2) \"capacity scaling or execution trace pretraining\" 实际上是论文的 primary open question——考虑在 Conclusion 中更显著地承认这一点动摇了当前结论的通用性。\n\n### Limitations\n- 覆盖 4 个要点（model family, ≤8B, Python-only, synthetic mutations），简短合规。\n- \"synthetic-to-real transfer gap remains untested\" 是重要限制，已提及。\n\n### Appendix\n- 14 个 appendix section（A-P），含 mini TOC（good）。\n- Appendix G' 的 prime 符号应改为 G.2。\n- Appendix P \"Extended limitations\" 不构成格式违规（R1 REBUT 合理），但内容实质上扩展了正文 Limitations，存在被审稿人质疑的风险。\n- `wei2022emergent` 引用类型应为 article（TMLR）而非 inproceedings。\n"
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
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "\n# 审稿报告 — Round 12 (Fresh Review)\n\n**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 via ACL ARR\n**审稿模式**: Fresh（无前轮记忆）\n**Reviewer 编排**: R1（方法严谨性 + 实验设计 + 统计分析）+ R2（新颖性 + 相关工作 + 写作 + 格式）\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free 代码修复验证 formulation：CLS（per-test 二分类）、CWM（执行输出生成）和 TRAJ（trajectory-level patch 评分），在两个代码 LLM 家族（Qwen3、DeepSeek-Coder）、两个复杂度级别、多 seed 下使用 ≤8B LoRA fine-tuning 进行匹配实验。核心发现：(1) function-level 下 CLS-CWM 统计等价（TOST p=0.007, 5 seeds, Bayesian ROPE P=0.975）；(2) repo-level 下 CWM 因 format collapse 退化 18-26pp（z=-23.7, DeepSeek-Coder）；(3) 14B 时 function-level gap 收窄至 0.43pp（TOST p=0.0006），一致于 capacity-dependent convergence；(4) error complementarity 和 failure mode taxonomy 为实践选择提供指导。\n\n---\n\n## Strengths\n\n**S1. 统计方法论远超同领域论文一般水准。** TOST 等价性检验 + Holm-Bonferroni 校正 + clustered bootstrap（114 clusters, 10K resamples）+ mixed-effects LPM/GEE 双模型验证 + Bayesian ROPE 分析——这套统计工具箱的部署深度和一致性为 NLP 实证研究设立了方法论标杆。[R1, R2 一致]\n\n**S2. Threats to validity 分析异常详尽和诚实。** §3.7 和 Appendix N 系统识别了五个潜在 confound（checkpoint, sequence length, preprocessing, TRAJ regime, CWM scale）并逐一评估，自我批评程度超过多数投稿论文。论文对自身局限性的坦诚值得肯定。[R1, R2 一致]\n\n**S3. Failure mode taxonomy 有独立实用价值。** Table 4 的三类故障模式（format collapse / decision collapse / aggregation penalty）为从业者提供了可操作的诊断框架，在给定模型和 formulation 下预测可能的失败模式。[R1, R2 一致]\n\n**S4. 实验设计在 ≤8B LoRA 范围内实现了高匹配度。** 控制了模型容量、训练数据、LoRA 配置、compute 等变量，在其约束范围内确实实现了 matched comparison。Hyperparameters 完整报告（Table 11），compute budget 明确（~370 GPU-hours），prompt templates 提供。[R1]\n\n**S5. Comprehensive ablation program。** LoRA rank, majority voting, sequence length, data size, preprocessing, few-shot, checkpoint 的系统消融，使 repo-level 结论有更强的因果推断基础（四项干预全部失败排除了多个替代解释）。[R1]\n\n---\n\n## Weaknesses\n\n### Must-Fix（共识 Critical）\n\n**C1. CWM baseline 生态效度——核心方法论 confound [R1-N1, R2-N2, 双方 AGREE]**\n\n论文标题声称比较\"verification formulations\"，但 repo-level 核心发现（CWM 退化 18-26pp）完全建立在 ≤8B LoRA fine-tuning 之上。CWM 需生成 ~477 tokens/instance vs CLS 仅 1 token；在小模型无 execution-trace pretraining 条件下，长文本生成退化是已知现象。14B function-level gap 收敛至 0.43pp（TOST p=0.0006）反而支持\"capacity drives the gap\"假设。论文虽在 Abstract 提到\"under our ≤8B LoRA protocol\"、§3.7 和 Appendix N 有详细讨论，但 Introduction §1 contribution (2) \"formulation choice is moderated by code complexity\" 读起来像一般性结论，未加 regime 限定。\n\nAppendix I(c) 的意外训练证据进一步加深了这一质疑：CWM 模型误训在 CLS 格式数据上后达到 86.05% accuracy + 0% unparseable——表明退化来自 trace generation 复杂度而非 verification task 本身。\n\n**必须修改**：(a) Title 和 Introduction contribution 中明确限定\"under ≤8B LoRA fine-tuning\"；(b) 如有可能，增加 14B CWM repo-level 数据点以验证 gap 是否随 capacity 缩小——这将直接决定核心结论的定性方向。\n\n**C2. Qwen3 CWM optimal checkpoint 未评估——论文持有关键数据但未报告 [R1-N2, R2 AGREE]**\n\nTable 16（Appendix L）显示 Qwen3-8B CWM eval loss 在 step 300-400 达到最小值（~0.29），final epoch（step 6600）膨胀至 ~0.52（1.8×）。论文确认 Qwen3 有 step 300/400 checkpoints 但**未报告其 repo-level accuracy**。DeepSeek 的 early-stopping 数据显示 +18.14pp improvement（75.45% vs 57.31%），暗示 Qwen3 optimal checkpoint 可能显著缩小 gap。\n\nR2 补充了重要 nuance：即使 early-stopped DeepSeek CWM 达到 75.45%，仍低于 CLS (82-85%)，且保持 66.4% unparseable rate——format collapse 在训练早期已存在，过拟合加剧但非唯一原因。缩小后的 gap (~10pp) 仍然 non-trivial，但显著改变了 gap 的解释。\n\n**必须修改**：评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy 和 unparseable rate，并在正文中报告。\n\n**C3. 统计功效不足导致 CLS-TRAJ 等价性结论不可靠 [R1-N3, R2 AGREE]**\n\nn_eff ≈ 86, TOST power ~0.3。CLS-CWM 等价性确认（TOST p=0.007, P(ROPE)=0.975）与 CLS-TRAJ 未确认（adjusted p=0.075, P(ROPE)=0.542 per-test）的不对称结论可能完全是 power 不足的 artifact——在 power ~0.3 下，Type II error 概率达 70%。论文在贡献声明中将\"TRAJ equivalence is not confirmed after multiple comparison correction\"与\"CLS-CWM equivalence\"并列，读者可能误解为\"CLS-TRAJ 不等价\"。\n\nR2 补充：Bayesian ROPE 在 variant-level 给出 P(ROPE)=0.970（支持等价），但 per-test level 为 0.542（inconclusive）。两个 analysis level 的不一致未在正文中讨论。\n\n**必须修改**：(a) 正文更明确讨论 power ~0.3 意味着\"未确认\"不等于\"非等价\"；(b) 讨论 variant-level vs per-test ROPE 的不一致及其原因；(c) 避免在 contribution list 中将 TRAJ model-contingent 作为稳健结论呈现。\n\n### Should-Fix\n\n**W1. 贡献列表仅两条，failure mode taxonomy 未列为贡献 [R2-W2, R1 AGREE]**\nTable 4 的 taxonomy（format collapse / decision collapse / aggregation penalty）是论文最具实用价值的输出之一。应增加为第三条贡献。\n\n**W2. GenRM 对比发现未被充分讨论 [R2-W3, R1 AGREE]**\nHosseini et al. (ICLR 2025) 发现 generation-based verifier 在数学推理中优于 classification-based。本文发现在代码验证中相反。这一对比是论文最有潜力成为 surprising finding 的地方，但仅在 §4 Related Work 一段讨论。应提升到 Discussion/Conclusion 级别。\n\n**W3. SESOI ±2pp 无 pre-registration，结论对 SESOI 选择敏感 [R1-W1, R2 AGREE]**\n±1.52pp 临界值距 ±2pp 仅 0.48pp。如果 SESOI 设为 ±1.5pp，CLS-CWM 等价性就不确认。建议在正文引用 Appendix G sensitivity analysis 并承认 SESOI 的主观性。\n\n**W4. CLS-TRAJ 训练条件根本不匹配（~400 vs ~70K, label granularity 差异）[R1-W4, R2 AGREE]**\nDownsample ablation 控制了 data volume 但未控制 label granularity（per-test vs variant-level）。CLS vs TRAJ repo-level 比较本质上是 exploratory 而非 confirmatory。\n\n**W5. Repo-level 数据处理不一致（drop vs truncate + checkpoint confound chain）[R1-W3, R2 AGREE]**\nDeepSeek CLS accuracy 从 82.61% (drop) 到 74.93% (truncate) 有 7.68pp 偏差，truncate → NaN val loss → final epoch default 形成 confound chain。应在正文更显著呈现。\n\n**W6. CLS-CWM paired comparison 使用不同 seeds（CLS s123 vs CWM s42）[R1-W5, R2 AGREE]**\nFunction-level seed noise (<2pp) 不能直接外推到 repo-level（DeepSeek CLS ±2.50 std）。\n\n**W7. 种子数/实验配置不一致导致统计置信度参差不齐 [R2-W5, R1 AGREE]**\n不同比较使用 1-5 seeds，统计可靠性差异大但未系统标注。\n\n### Minor\n\n- M1: §2.2 Failure Modes 位于 method section 造成结构困惑（R2 提出, R1 AGREE）\n- M2: Appendix G' prime 符号命名不直观（R2 提出, R1 AGREE）\n- M3: `wei2022emergent` 引用类型不一致（R2）\n- M4: Figure 2 float 漂移 2-3 页（视觉审查）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **CWM baseline 公平性是核心问题**：两位 reviewer 独立提出，交叉分享后双方完全 AGREE。≤8B LoRA 对 CWM 系统性不公平，repo-level 核心发现可能是 capacity artifact 而非 formulation 差异。\n2. **Qwen3 CWM optimal checkpoint 未评估是重大遗漏**：R1 提出，R2 完全 AGREE。论文持有 step 300-400 checkpoints 但未报告 accuracy。\n3. **统计功效不足限制了 CLS-TRAJ 结论**：R1 提出，R2 AGREE。Power ~0.3 下\"未确认等价\"不应被呈现为\"model-contingent\"。\n4. **Failure mode taxonomy 应提升为贡献**：R2 提出，R1 完全 AGREE。\n5. **GenRM 对比应更深入讨论**：R2 提出，R1 AGREE。\n6. **统计方法论是突出优势**：双方一致肯定。\n7. **Threats to validity 讨论诚实详尽**：双方一致肯定。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **Excitement/Novelty（核心分歧）**：\n   - R2 (Excitement 2/5)：\"核心发现可从第一性原理预期，§2.2 理论分析就预测了实验结果\"\n   - R1 (Excitement 3/5)：\"'可预期'不等于'无价值'，引用 ARR H1 条款；gap magnitude 和四项干预失败不可预期\"\n   - **Director 判断**：R2 的关切更有说服力。论文的理论分析（§2.2）确实预测了实验结果的方向——function-level 等价和 repo-level 发散。虽然 magnitude 不可预期（R1 的论点），但 magnitude 的精确量化在 CWM baseline 公平性存疑的情况下（C1, C2）价值受限。R1 引用 ARR H1 是合理的，但 H1 旨在防止对 well-designed experiments confirming non-obvious hypotheses 的不公平驳回——本文的假设从自身理论框架看并非 non-obvious。\n\n2. **Abstract 统计密度**：\n   - R2：\"统计细节过密降低可读性\"\n   - R1：\"方法论论文需要在 Abstract 包含关键统计结果\"\n   - **Director 判断**：R1 的立场更合理。对于以统计方法论为核心卖点的论文，Abstract 中保留关键 p-value 和 effect size 是必要的。但可考虑精简至 2-3 个最关键数字。\n\n3. **两个模型家族是否足够**：\n   - R2：\"泛化性受限\"\n   - R1：\"ARR H4 不鼓励要求不必要的额外实验\"\n   - **Director 判断**：R1 的论点更有说服力。两个家族作为 primary + consistency check 是合理的实验经济性选择。降级为 Limitations 中提及即可。\n\n---\n\n## Questions\n\n1. Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy 是多少？\n2. 是否有 14B CWM 的 repo-level 数据？如有，gap 是否随 capacity 缩小？\n3. ±2pp SESOI 是否 pre-registered？如否，应在正文明确说明。\n4. NF4 quantization 对 CWM 长文本生成质量的具体影响是什么？\n5. CLS-TRAJ 等价性确认所需的最小样本量是多少（a priori power analysis）？\n\n---\n\n## Missing References\n\n- **Equivalence testing 在 NLP 中的应用先例**（如有）：会加强 TOST 方法选择的 motivation [R1]\n- **CVeDRL (arXiv:2601.22803, 2026)**：R2 提出但 R1 对其存在性和相关性存疑（difficulty-aware RL training 与本文 formulation comparison 主题有一定距离）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：✅ 完成（1 warning, 12 info）\n\n**Warning**:\n- Figure 2 首次引用在 page 4-5，但实际出现在 page 7 右栏（float 漂移 2-3 页）。建议调整 float 位置参数。\n\n**Info highlights**:\n- Figure 1 概念图清晰专业，三种 formulation 对比一目了然\n- Tables 1-4 均使用 booktabs 风格，格式规范\n- Figure 2 使用色盲友好双色方案，y-axis 非零起始已在 caption 标注\n- 正文在第 8 页结束，Limitations 为简短一段覆盖 3 个要点，符合 EMNLP 规范\n- Appendix 12 页（p12-22），表格密度高但作为 appendix 可接受\n- 无 [?] 未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**置信度: 4/5**\n\n**评分理由**：\n\n论文在方法论严谨性方面达到了 NLP 实证研究的高标准（S1, S2），failure mode taxonomy 有独立实用价值（S3），在 ≤8B LoRA 范围内的实验设计匹配度高（S4）。\n\n但三个核心问题限制了论文达到 Conference 水平：\n\n1. **CWM baseline 公平性（C1）**——这是最严重的问题。如果 repo-level 的 18-26pp gap 主要由 model capacity 而非 formulation 差异驱动（14B function-level 收敛至 0.43pp 提供了强间接证据），则论文的中心 claim（\"complexity-moderated formulation choice\"）的通用性大幅受限。论文需要在 Introduction 的贡献声明中更显著地限定这一点。\n\n2. **CWM checkpoint 遗漏（C2）**——论文持有 optimal checkpoint 但未报告其 accuracy，DeepSeek 的 early-stopping 数据暗示 gap 可能缩小约 18pp。这是一个可以执行但未执行的关键实验。\n\n3. **Novelty ceiling（R6-N4 系列）**——核心发现（function-level 等价 + repo-level 发散）可从论文自身的 §2.2 理论分析直接预期。虽然统计严谨的量化验证有价值，但在核心 claim 受 C1 和 C2 质疑的情况下，magnitude 的精确量化也失去了部分说服力。R1 (3.5, Borderline Conference) 和 R2 (3.0, Findings) 的评分差异主要反映对 novelty 的不同判断。\n\n**如果作者在 rebuttal 中能提供**：(a) Qwen3 CWM optimal checkpoint 的 repo-level accuracy，(b) 14B CWM repo-level 数据点——**评分可能上调至 3.5**。目前，Findings 是合适的定位。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution (2) \"formulation choice is moderated by code complexity\" 缺少 ≤8B LoRA 限定。这是核心 claim，应在首次出现时就明确限定条件。\n- 仅列出两条贡献。Failure mode taxonomy（Table 4）应作为第三条。\n- \"primarily methodological\" 的自我定位虽诚实但策略上不利——建议重新框定为揭示了 generation advantage 的 domain-specificity。\n\n### §2 Method\n- §2.2 Failure Modes 更适合放在 §3 Experiments 中，与 Table 4 的实证 taxonomy 相邻。当前位置在 Method section 会让读者误以为是方法设计而非理论预测。\n- Oracle Accuracy-Utility Framework（§2.3）的 ICC 参数来自 function-level 分析，在 repo-level 应用时存在 domain mismatch（repo-level ICC=0.3146 vs function-level ICC=0.191）。\n\n### §3 Experiments\n- Table 1: 信息密度高但缺少视觉分隔（primary results / cross-model / baselines 之间）。\n- §3.2 Scaling: \"At 8B, the ranking is CLS > TRAJ > CWM\"——这三个数字基于 2 seeds，排名的统计置信度有限。\n- §3.4 Equivalence: TOST sensitivity analysis 结果（±1.52pp 临界值）应在正文中引用和讨论，而非仅放在 Appendix G。\n- §3.4 Statistical power 段落已有（good），但应更明确说明 power ~0.3 意味着 CLS-TRAJ 的 non-confirmation 是 inconclusive 而非 negative。\n- §3.5 Repo-Level: CWM convergence analysis 确认了 systematic overfitting，但 Qwen3 optimal checkpoint 的 accuracy 是关键缺失数据。\n- §3.6 Analysis: Oracle combination 基于 single-seed，应更醒目标注。\n- §3.7 Threats: preprocessing-checkpoint confound chain 应更显著呈现。\n\n### §4 Related Work\n- GenRM 对比发现（generation advantage 在代码领域失效）是论文最有潜力的 insight，但埋在 Related Work 中。应提升至 Discussion 级别。\n- 三段式组织（Execution Simulation / Process vs Outcome / Repair & Task Framing）清晰合理。\n- 引用真实性抽查通过，未发现幻觉引用。\n\n### §5 Conclusion\n- \"Primary statistical findings are established under ≤8B LoRA fine-tuning\" 是正确且必要的限定。\n- Future direction (2) \"capacity scaling or execution trace pretraining\" 实际上是论文的 primary open question——考虑在 Conclusion 中更显著地承认这一点动摇了当前结论的通用性。\n\n### Limitations\n- 覆盖 4 个要点（model family, ≤8B, Python-only, synthetic mutations），简短合规。\n- \"synthetic-to-real transfer gap remains untested\" 是重要限制，已提及。\n\n### Appendix\n- 14 个 appendix section（A-P），含 mini TOC（good）。\n- Appendix G' 的 prime 符号应改为 G.2。\n- Appendix P \"Extended limitations\" 不构成格式违规（R1 REBUT 合理），但内容实质上扩展了正文 Limitations，存在被审稿人质疑的风险。\n- `wei2022emergent` 引用类型应为 article（TMLR）而非 inproceedings。\n"
  }
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-23T09:20:22.617191+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4223
}
```

</details>

---


### Assistant

_source line 986 · 2026-05-23T09:20:37.414171+00:00_

审稿报告已投递至 Research Director。

**Round 12 审稿结果摘要**：

**Overall: 3.0 (Findings)**，置信度 4/5。

**3 个 Critical（共识）**：
1. CWM baseline 生态效度——≤8B LoRA 系统性削弱 CWM，repo-level 18-26pp gap 可能是 capacity artifact 而非 formulation 本质差异
2. Qwen3 CWM optimal checkpoint（step 300-400）未评估——论文持有 checkpoint 但缺失关键数据，DeepSeek early-stop 暗示 gap 可缩小 ~18pp
3. 统计功效不足（power ~0.3）——CLS-TRAJ 不对称结论可能纯粹是 Type II error

**7 个 Should-Fix**：贡献列表不足、GenRM 对比未充分展开、SESOI 无 pre-registration、CLS-TRAJ 训练条件不匹配、数据处理不一致、cross-seed pairing、种子覆盖参差不齐。

**主要分歧**：Excitement（R1: 3/5 vs R2: 2/5）——Director 倾向 R2，理由是论文自身的理论框架（§2.2）预测了实验结果方向。

**升分路径**：如作者在 rebuttal 中提供 (a) Qwen3 CWM optimal checkpoint accuracy + (b) 14B CWM repo-level 数据，评分可上调至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 91

## Round 91

56 recorded events


### User

_source line 987 · 2026-05-23T12:29:28.056406+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
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

_source line 988 · 2026-05-23T12:29:33.628055+00:00_

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

_source line 989 · 2026-05-23T12:29:33.679225+00:00_

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

_source line 990 · 2026-05-23T12:29:41.165736+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-23T12:29:41.167398+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 992 · 2026-05-23T12:29:46.100457+00:00_

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


### Tool call

_source line 993 · 2026-05-23T12:29:46.605034+00:00_

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

_source line 994 · 2026-05-23T12:29:49.065074+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (266 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D13
…[truncated 1825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2964
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-23T12:29:49.065440+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 2460
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-23T12:29:49.769966+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_11/submitted.pdf 2>&1",
  "description": "Check paper files exist"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_11/submitted.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool call

_source line 997 · 2026-05-23T12:29:49.872143+00:00_

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

_source line 998 · 2026-05-23T12:29:50.023202+00:00_

-rw-r--r-- 1 ubuntu ubuntu 422612 May 23 12:26 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_11/submitted.pdf
-rw-r--r-- 1 ubuntu ubuntu   1706 May 23 11:13 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 253
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-23T12:29:50.023752+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-23T12:29:55.654678+00:00_

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

_source line 1001 · 2026-05-23T12:29:56.608754+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "report.md",
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
    "file": "report.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-23T12:29:57.261767+00:00_

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


### Tool call

_source line 1003 · 2026-05-23T12:29:58.216098+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_EXISTS\"",
  "description": "Read existing review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_EXISTS\"",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1004 · 2026-05-23T12:30:05.502890+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's information about EMNLP 2026 call for papers submission guidelines related to ARR:

## Main Conference Papers

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## ARR Policy for EMNLP 2026

Following the ACL and ARR policies, there is no anonymity period requirement.

A key policy update for ARR submissions is: Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: i.e., ARR 2026 May submissions that do not select EMNLP 2026 during submission will not b
…[truncated 521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 9848
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-23T12:30:05.553857+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/report.md\", \"content\": \"# Handover — 2026-05-23\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\\n\\n## 待处理\\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\\n- qwen_cwm_s456_resume2（准备中）\\n- qwen_cwm_s456_resume（准备中）\\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\\n- D131-cwm-s42-epoch3-seq2048（准备中）\\n- D133-cwm-s42-e2-seq2048-home-resume（准备中）\\n- deepseek-cwm-repo-s42-epoch2-eval: Eval CWM s42 epoch 2 checkpoint 解耦过拟合 vs seed 差异：如果 epoch 2 accuracy >> epoch 3 (56.7%)，则 CWM repo-level 在 epoch 3 过拟合（准备中）\\n- …另有 9 项\\n\\n## 近期结论\\n- **traj14b-func-s123** (success): TRAJ 14B (seed 123) 补完 Table 2 的 14B TRAJ 行。与 CLS/CWM 14B 对比验证三公式在 14B 的 scaling 趋势。4B→8B TRAJ scaling +2.13pp，14B 应保持或扩大趋势。\\n- **traj14b-func-s456** (success): TRAJ 14B (seed 456) 补完 Table 2 的 14B TRAJ 行。与 CLS/CWM 14B 对比验证三公式在 14B 的 scaling 趋势。4B→8B TRAJ scaling +2.13pp，14B 应保持
…[truncated 1419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8945
}
```

</details>

---


### Tool result

_source line 1006 · 2026-05-23T12:30:05.554373+00:00_

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
  "elapsed_ms": 8292
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-23T12:30:05.605339+00:00_

&lt;persisted-output>
Output too large (41.6KB). Full output saved to: /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier--claude-sessions-review-director-06def7c3/d455fb7f-48c1-46dc-bc51-08502eccead0/tool-results/bauw42cg4.txt

Preview (first 2KB):
# === Round 6 Issues (Original) ===

# --- Round 6 Must-Fix (Consensus Critical) ---

- id: "R6-N1"
  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 6
  last_seen_round: 11
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
  action_items:
    - round: 6
      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
      assigned_to: "paper"
      status: resolved
    - round: 9
      acti
…[truncated 167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 7389
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-23T12:30:15.089513+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 author guidelines page limit format requirements ARR submission"
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
    "query": "EMNLP 2026 author guidelines page limit format requirements ARR submission"
  }
}
```

</details>

---


### Tool call

_source line 1009 · 2026-05-23T12:30:15.893336+00:00_

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

_source line 1010 · 2026-05-23T12:30:16.396153+00:00_

1	\begin{abstract}
2	LLM-based program repair increasingly generates multiple candidate patches, selecting the best via a verifier. Three execution-free alternatives to expensive execution-based verification have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares them under matched conditions.
3	
4	We present the first systematic comparison across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is not confirmed after multiple comparison correction at any scale tested, but the gap narrows monotonically from 3.11\pp{} (4B) to 1.07\pp{} (14B). At repository level, a significant interaction ($z{=}-23.7$, DeepSeek-Coder) confirms this equivalence collapses: the \cls{}--\cwm{} gap widens to 18--26\pp{} across 2--3 seeds per model under our ${\leq}$8B LoRA protocol, driven by format collapse. At 14B (3 seeds), all three formulations narrow to within 1.07\pp{}, consistent with capacity-dependent resolution of formulation differences.
5	
6	Error complementarity and a failure mode taxonomy motivate future work on complexity-aware formulation routing, though simple heuristics capture $<$0.4\pp{} of oracle advantage.
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

_source line 1011 · 2026-05-23T12:30:16.396511+00:00_

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

_source line 1012 · 2026-05-23T12:30:17.351032+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. This connects to a broader pattern in NLP: task formulation---classification vs.\ generation vs.\ span extraction---systematically affects performance~\cite{raffel2020t5}, but the conditions under which each wins remain task-dependent and empirically unresolved. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We pres
…[truncated 3171 chars]

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

_source line 1013 · 2026-05-23T12:30:17.351609+00:00_

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

_source line 1014 · 2026-05-23T12:30:17.452449+00:00_

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


### Tool call

_source line 1015 · 2026-05-23T12:30:17.453044+00:00_

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

_source line 1016 · 2026-05-23T12:30:17.503854+00:00_

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
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss because repo-level execution traces often exceed the 2,048-token sequence length limit; after truncation, many samples have all target tokens removed (labels entirely $-$100), producing degenerate loss---a formulation-inherent weakness that classification and trajectory formulations avoid by design. NaN loss defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, DeepSeek \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}). Qwen3 \cwm{} runs have valid validation loss with best checkpoints at ${\sim}$6\% of training (step 300--400), indicating severe overfitting; s42 uses the trainer-selected best checkpoint, while s123/s456 use the final epoch checkpoint.
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 
…[truncated 21392 chars]

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

_source line 1017 · 2026-05-23T12:30:22.422600+00:00_

Web search results for query: "EMNLP 2026 author guidelines page limit format requirements ARR submission"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submission Checklist for Original, First Time Submissions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/OriginalSubmissionChecklist"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"}]

Based on the search results, here are the key author guidelines for EMNLP 2026 regarding page limits, format requirements, and ARR submission:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Format Requirements

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## ARR Submission Process

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Both submissions of articles for review a
…[truncated 757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 7333
}
```

</details>

---


### Tool call

_source line 1018 · 2026-05-23T12:30:29.213645+00:00_

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

_source line 1019 · 2026-05-23T12:30:29.615655+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. CodeScaler~\cite{zhu2026codescaler} trains execution-free reward models for both RL and test-time scaling. Verification formulations span trajectory-level reward~\cite{shum2025swerm}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. GenRM~\cite{hosseini2025genrm} and GenPRM~\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formula
…[truncated 1607 chars]

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

_source line 1020 · 2026-05-23T12:30:29.616076+00:00_

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

_source line 1021 · 2026-05-23T12:30:30.671436+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} equivalence is not confirmed after correction, but the gap narrows monotonically to 1.07\pp{} at 14B. Complementary errors (oracle: 90.63\%/95.83\%; single-seed) motivate complexity-aware routing. At repository level under ${\leq}$8B LoRA, divergence reaches 18--26\pp{} ($z{=}-23.7$), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}). 14B results (3 seeds) corroborate function-level convergence: the \cls{}--\cwm{} gap narrows to 0.43\pp{} (TOST $p{=}0.0006$) and the \cls{}--\traj{} gap to 1.07\pp{}, consistent with capacity-dependent scaling; whether this extends to repo level remains open. This contrasts with mathematical reasoning, where generative verification outperforms discriminative~\cite{hosseini2025genrm}, suggesting the generation advantage is domain-dependent rather than universal.
5	
6	Three directions follow: (1)~complexity-aware routing; (2)~capacity scaling at 32B+~\cite{meta2025cwm}; (3)~per-test diagnostics for downstream repair.
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
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-23T12:30:30.671974+00:00_

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

_source line 1023 · 2026-05-23T12:30:31.126788+00:00_

1	\appendix
2	
3	\noindent\textbf{Appendix overview.} A: Oracle resolve advantage. B: Ablation studies. C-F: Extended analysis (error complementarity, parseable accuracy, forced parsing, qualitative errors, failed interventions, mutation scaling, inference efficiency, re-repair, chain-of-thought). G: TOST sensitivity (G.1: Bayesian ROPE). H: Effect sizes. I: Holm-Bonferroni. J: Mixed-effects regression. K: Parseable bias. L: CWM convergence. M: Few-shot. N: Threats. O: Downsample. P: Limitations.
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
34	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.
…[truncated 57937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-23T12:30:31.127288+00:00_

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

_source line 1025 · 2026-05-23T12:30:31.580193+00:00_

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
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-23T12:30:31.580597+00:00_

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

_source line 1027 · 2026-05-23T12:30:31.631150+00:00_

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
12	  last_seen_round: 11
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
32	  action_items:
33	    - round: 6
34	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
35	      assigned_to: "paper"
36	      status: resolved
37	    - round: 9
38	      action: "正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive"
39	      assigned_to: "paper"
40	      status: resolved
41	  resolution: "§3.5 开头标注 'Variant-level comparisons (n=48) are explo
…[truncated 7148 chars]

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

_source line 1028 · 2026-05-23T12:30:37.918197+00:00_

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

_source line 1029 · 2026-05-23T12:30:37.969146+00:00_

200	  mentions:
201	    - round: 7
202	      reviewers: [pre-review]
203	      note: "3+ 处修复完成。"
204	    - round: 8
205	      reviewers: [1, 2]
206	      note: "Abstract 仍比 Conclusion 缺 qualifier."
207	    - round: 9
208	      reviewers: []
209	      note: "本轮未被独立提出。Abstract 已含 '≤8B LoRA protocol' qualifier。"
210	    - round: 10
211	      reviewers: [1, 2]
212	      note: "R2-N2 标为 CRITICAL：≤8B 限制严重威胁泛化性。R1 部分 REBUT（4B→8B gap 扩大）但同意 abstract 需限定。两人共识：abstract/conclusion 应明确 '≤8B LoRA regime' 限定。"
213	  action_items:
214	    - round: 8
215	      action: "Abstract 加 'under our ≤8B LoRA protocol'"
216	      assigned_to: "agent"
217	      status: resolved
218	    - round: 10
219	      action: "Conclusion 也加 ≤8B LoRA 限定；讨论更大规模下结论可能如何变化"
220	      assigned_to: "paper"
221	      status: resolved
222	  resolution: "R10 commit a58c178: Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入 'All findings are conditioned on ≤8B LoRA fine-tuning; at larger scale, the generation bottleneck may diminish'。"
223	  resolution_round: 10
224	
225	- id: "R6-W3"
226	  summary: "Re-repair δ=0 与 diagnostic granularity 矛盾"
227	  category: framing
228	  severity: warning
229	  status: resolved
230	  first_raised_round: 6
231	  last_seen_round: 7
232	  action_items:
233	    - round: 6
234	      action: "降级 diagnostic granularity"
235	      assigned_to: "paper"
236	      status: resolved
237	  resolution: "Contributions 4→3, diagnostic granularity 降级为 pending validation."
238	  resolution_round: 7
239	
240	- id: "R6-W4"
241	  summary: "TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同"
242	  category: experiment
243	  severity: warning
244	  status: resolved
245	  first_raised_round: 6
246	  last_seen_round: 12
247	  mentions:
248	    - round: 8
249	      reviewers: [2]
250	      note: "R2-W6: 175× 数据量差异."
251	    - round: 9
252	      reviewers: [1]
253	      note: "R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level."
254	    - round: 10
255	      reviewers: [1, 2]
256	      note: "R1-W1 re-raises：180× 差异 + sig
…[truncated 9136 chars]

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

_source line 1030 · 2026-05-23T12:30:44.206830+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "offset": "500",
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
    "offset": "500",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1031 · 2026-05-23T12:30:44.409342+00:00_

500	  status: resolved
501	  first_raised_round: 8
502	  last_seen_round: 10
503	  resolution: "GenRM, CodeScaler, GenPRM 已加入 Related Work。"
504	  resolution_round: 10
505	
506	- id: "R8-W6"
507	  summary: "CWM baseline 偏弱 (≤8B LoRA vs 原始 32B+mid-training)"
508	  category: method
509	  severity: warning
510	  status: resolved
511	  first_raised_round: 8
512	  last_seen_round: 10
513	  mentions:
514	    - round: 8
515	      reviewers: [1, 2]
516	      note: "DIVERGENT. Director 裁定 Should-Fix."
517	    - round: 10
518	      reviewers: [1, 2]
519	      note: "R2-N2 标 CRITICAL。R1 部分 REBUT（4B→8B gap 扩大数据）。两人共识：abstract/conclusion 需 ≤8B 限定。"
520	  resolution: "合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成（gap ≈ 0）。"
521	  resolution_round: 10
522	
523	- id: "R8-W7"
524	  summary: "Novelty 是否足够 Conference 水平"
525	  category: framing
526	  severity: warning
527	  status: wont_fix
528	  first_raised_round: 8
529	  last_seen_round: 12
530	  mentions:
531	    - round: 8
532	      reviewers: [1, 2]
533	      note: "DIVERGENT. Director: Findings track 合适."
534	    - round: 9
535	      reviewers: [1, 2]
536	      note: "两人 Excitement 均为 2.5/5. R2 评 3.0 (Findings), R1 评 3.5 (Borderline Conference)."
537	    - round: 10
538	      reviewers: [1, 2]
539	      note: "R1 Excitement 3/5, R2 Excitement 2.5/5. 两人共识：Findings 合适。合并至 R6-N4 追踪。"
540	    - round: 11
541	      reviewers: [1, 2]
542	      note: "Continue review. Excitement consensus at 3/5. R1 Overall 3.5 (soundness compensates), R2 Overall 3.0 (excitement ceiling). Inherent limitation, wont_fix. Merged with R6-N4."
543	    - round: 12
544	      reviewers: [1, 2]
545	      note: "Fresh review R12. R1 Excitement 3/5, R2 Excitement 2/5. R1 Overall 3.5, R2 Overall 3.0. 分歧 persist。"
546	  resolution: "合并至 R6-N4。Excitement 提升至 3.0/5 但 Conference 水平仍未达到。Inherent limitation：贡献类型为 empirical comparison，无法通过修改改变。"
547	  resolution_round: 11
548	
549	# --- Round 8 Minor ---
550	
551	- id: "R8-M1"
552	  summary: "混合精度 (bfloat1
…[truncated 9089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-23T12:30:48.333044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "offset": "800",
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
    "offset": "800",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-23T12:30:48.384485+00:00_

800	  last_seen_round: 12
801	  mentions:
802	    - round: 12
803	      reviewers: [1, 2]
804	      note: "R1-N3 提出，R2 AGREE。Power ~0.3 下，CLS-CWM 等价性确认（TOST p=0.007, P(ROPE)=0.975）与 CLS-TRAJ 未确认（adjusted p=0.075, P(ROPE)=0.542）的不对称可能纯粹是 Type II error。R2 补充：variant-level P(ROPE)=0.970 vs per-test P(ROPE)=0.542 的不一致也值得正文讨论。"
805	  action_items:
806	    - round: 12
807	      action: "正文明确讨论 power ~0.3 对 CLS-TRAJ 结论的影响；报告 CLS-TRAJ 等价性所需最小样本量；讨论 variant-level vs per-test ROPE 不一致"
808	      assigned_to: "paper"
809	      status: resolved
810	  resolution: "§3.4 power paragraph 已扩写（Type II ~70%, n_eff≈350, Bayesian ROPE per-test vs variant-level 不一致讨论）。14B CLS-TRAJ TOST 完成：raw p=0.043 passes, P(ROPE)=0.956, Holm adj p=0.050 (borderline)。§3.2 和 §3.4 已加入 14B TOST 数据。Appendix Bayesian ROPE 加入 14B 段落。Contribution 措辞保守：'gap narrows monotonically to 1.07pp, not confirmed after Holm correction'。"
811	  resolution_round: 12
812	
813	- id: "R12-W1"
814	  summary: "贡献列表仅两条，failure mode taxonomy 未列为独立贡献"
815	  category: framing
816	  severity: warning
817	  status: resolved
818	  first_raised_round: 12
819	  last_seen_round: 12
820	  mentions:
821	    - round: 12
822	      reviewers: [1, 2]
823	      note: "R2-W2 提出，R1 完全 AGREE。Table 4 (format collapse / decision collapse / aggregation penalty) 是论文最具实用价值的输出之一，目前未在 contribution list 中体现。增加第三条贡献不会膨胀论文——工作已完成，只是 framing 不足。"
824	  action_items:
825	    - round: 12
826	      action: "§1 contribution list 增加第三条：failure mode taxonomy"
827	      assigned_to: "paper"
828	      status: resolved
829	  resolution: "Introduction §1 已增加第三条贡献：'Failure mode taxonomy. Variant-level analysis reveals three distinct failure modes at repository level---format collapse (CWM), decision collapse (CLS under truncate), and aggregation penalty (CLS under all-pass)---providing actionable diagnostic criteria.'"
830	  resolution_round: 12
831	
832	- id: "R12-W2"
833	  summary: "GenRM 对比发现（generation advantage 在代码领域失效）未被充分讨论，仅在 Related Work 一段"
834	  category: f
…[truncated 6109 chars]

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

_source line 1034 · 2026-05-23T12:31:08.032486+00:00_

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


### Tool call

_source line 1035 · 2026-05-23T12:31:08.234984+00:00_

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

_source line 1036 · 2026-05-23T12:31:12.255152+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4222
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-23T12:31:12.255611+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 4020
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-23T12:31:53.767044+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper, 正文 8 页, 参考文献无限制, Limitations 不计页\n- **模板**: ACL style (review mode), double-blind\n- **匿名规则**: Double-blind\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_11/submitted.pdf`\n\n## 你的审查侧重\n\n**重点审查以下方面：**\n\n1. **统计方法论**：\n   - TOST 等价检验的 SESOI (±2pp) 设定是否合理？是否有 pre-registration？\n   - Holm-Bonferroni 校正的 k=5 分组是否正确？\n   - Power ~0.3 下 CLS-TRAJ '未确认等价' vs CLS-CWM '确认等价' 的不对称结论是否成立？\n   - Bayesian ROPE 与 TOST 结论不一致时的处理是否恰当？\n   - Clustered bootstrap 实施是否正确？\n\n2. **实验设计**：\n   - Seed coverage 是否充分？（function: 5 seeds, repo: 2-3 seeds, 14B: 3 seeds）\n   - Checkpoint selection 差异（val-selected vs final-epoch default due to NaN loss）是否构成系统性偏差？\n   - CWM baseline 的生态效度：≤8B LoRA vs 原始 32B + execution trace pretraining\n   - TRAJ 训练配置差异（~400 vs ~70K samples, 不同 learning rate, variant-level labels）\n\n3. **Threats to Validity**：\n   - 五个 confound 的评估是否充分？\n   - 'Correlated confounds' 的 worst-case compounding 分析是否合理？\n   - Preprocessing-checkpoint confound chain 的 7.68pp impact\n   - Cross-seed pairing 对 repo-level paired comparison 的限制\n\n4. **页数/格式合规性**：\n   - 正文是否严格 ≤ 8 页？\n   - Abstract 是否 ≤ 200 words？\n   - 是否正确使用 review mode（匿名）？\n\n请按 ARR 审稿标准评审，输出格式：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n- Questions (需要作者澄清)\n- Missing References\n- Overall Assessment (1-5 ARR scale) + Excitement (1-5) + Confidence (1-5)"
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
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper, 正文 8 页, 参考文献无限制, Limitations 不计页\n- **模板**: ACL style (review mode), double-blind\n- **匿名规则**: Double-blind\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_11/submitted.pdf`\n\n## 你的审查侧重\n\n**重点审查以下方面：**\n\n1. **统计方法论**：\n   - TOST 等价检验的 SESOI (±2pp) 设定是否合理？是否有 pre-registration？\n   - Holm-Bonferroni 校正的 k=5 分组是否正确？\n   - Power ~0.3 下 CLS-TRAJ '未确认等价' vs CLS-CWM '确认等价' 的不对称结论是否成立？\n   - Bayesian ROPE 与 TOST 结论不一致时的处理是否恰当？\n   - Clustered bootstrap 实施是否正确？\n\n2. **实验设计**：\n   - Seed coverage 是否充分？（function: 5 seeds, repo: 2-3 seeds, 14B: 3 seeds）\n   - Checkpoint selection 差异（val-selected vs final-epoch default due to NaN loss）是否构成系统性偏差？\n   - CWM baseline 的生态效度：≤8B LoRA vs 原始 32B + execution trace pretraining\n   - TRAJ 训练配置差异（~400 vs ~70K samples, 不同 learning rate, variant-level labels）\n\n3. **Threats to Validity**：\n   - 五个 confound 的评估是否充分？\n   - 'Correlated confounds' 的 worst-case compounding 分析是否合理？\n   - Preprocessing-checkpoint confound chain 的 7.68pp impact\n   - Cross-seed pairing 对 repo-level paired comparison 的限制\n\n4. **页数/格式合规性**：\n   - 正文是否严格 ≤ 8 页？\n   - Abstract 是否 ≤ 200 words？\n   - 是否正确使用 review mode（匿名）？\n\n请按 ARR 审稿标准评审，输出格式：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n- Questions (需要作者澄清)\n- Missing References\n- Overall Assessment (1-5 ARR scale) + Excitement (1-5) + Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 1039 · 2026-05-23T12:32:09.759498+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15992
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-23T12:32:10.821578+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性/贡献 + 完整性** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper, 正文 8 页, 参考文献无限制, Limitations 不计页\n- **模板**: ACL style (review mode), double-blind\n- **匿名规则**: Double-blind\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_11/submitted.pdf`\n\n## 你的审查侧重\n\n**重点审查以下方面：**\n\n1. **新颖性与贡献**：\n   - 核心贡献（formulation comparison）的原创性——是否仅在比较已有方法？\n   - 三条贡献（complexity-moderated formulation choice, error complementarity, failure mode taxonomy）是否各自独立成立？\n   - 关键发现（func-level equiv + repo-level collapse）是否可从 §2.2 的理论分析直接预期？\n   - Excitement 评估：对 EMNLP 读者的启发性和影响力\n   - 与 GenRM (Hosseini et al., ICLR 2025) 的 domain-specificity 对比是否成为 surprising finding？\n\n2. **Related Work 覆盖**：\n   - 是否遗漏重要相关工作？特别关注 2025-2026 年的新进展\n   - CodeRM, CodeScaler, GenPRM, Aletheia 等是否充分讨论？\n   - PRM/ORM 映射是否准确？\n\n3. **写作质量与叙事**：\n   - Abstract 是否准确概括核心发现？是否 ≤ 200 words？\n   - Introduction 的 framing 是否过度？（\"systematic comparison\" vs 实际贡献范围）\n   - Conclusion 与 Limitations 是否充分讨论了泛化性限制？\n   - 正文与 Appendix 的信息分配是否合理？（16 个 Appendix A-P）\n\n4. **完整性**：\n   - 实验覆盖是否全面？（models × formulations × complexity levels × seeds）\n   - 消融研究（rank, voting, matching, scaling）是否充分？\n   - 14B 结果是否充分支持 capacity-dependent convergence 结论？\n   - Limitations 是否诚实全面？\n\n5. **ARR Responsible NLP Checklist**：\n   - Checklist 各项是否在论文中有对应？（注：Checklist 在 OpenReview 表单填写，不在 PDF 中）\n\n请按 ARR 审稿标准评审，输出格式：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n- Questions (需要作者澄清)\n- Missing References\n- Overall Assessment (1-5 ARR scale) + Excitement (1-5) + Confidence (1-5)"
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
    "text": "你是 Reviewer 2，负责 **新颖性/贡献 + 完整性** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper, 正文 8 页, 参考文献无限制, Limitations 不计页\n- **模板**: ACL style (review mode), double-blind\n- **匿名规则**: Double-blind\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_11/submitted.pdf`\n\n## 你的审查侧重\n\n**重点审查以下方面：**\n\n1. **新颖性与贡献**：\n   - 核心贡献（formulation comparison）的原创性——是否仅在比较已有方法？\n   - 三条贡献（complexity-moderated formulation choice, error complementarity, failure mode taxonomy）是否各自独立成立？\n   - 关键发现（func-level equiv + repo-level collapse）是否可从 §2.2 的理论分析直接预期？\n   - Excitement 评估：对 EMNLP 读者的启发性和影响力\n   - 与 GenRM (Hosseini et al., ICLR 2025) 的 domain-specificity 对比是否成为 surprising finding？\n\n2. **Related Work 覆盖**：\n   - 是否遗漏重要相关工作？特别关注 2025-2026 年的新进展\n   - CodeRM, CodeScaler, GenPRM, Aletheia 等是否充分讨论？\n   - PRM/ORM 映射是否准确？\n\n3. **写作质量与叙事**：\n   - Abstract 是否准确概括核心发现？是否 ≤ 200 words？\n   - Introduction 的 framing 是否过度？（\"systematic comparison\" vs 实际贡献范围）\n   - Conclusion 与 Limitations 是否充分讨论了泛化性限制？\n   - 正文与 Appendix 的信息分配是否合理？（16 个 Appendix A-P）\n\n4. **完整性**：\n   - 实验覆盖是否全面？（models × formulations × complexity levels × seeds）\n   - 消融研究（rank, voting, matching, scaling）是否充分？\n   - 14B 结果是否充分支持 capacity-dependent convergence 结论？\n   - Limitations 是否诚实全面？\n\n5. **ARR Responsible NLP Checklist**：\n   - Checklist 各项是否在论文中有对应？（注：Checklist 在 OpenReview 表单填写，不在 PDF 中）\n\n请按 ARR 审稿标准评审，输出格式：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 severity: Must-Fix / Should-Fix / Minor)\n- Questions (需要作者澄清)\n- Missing References\n- Overall Assessment (1-5 ARR scale) + Excitement (1-5) + Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-23T12:32:12.853998+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2032
}
```

</details>

---


### Assistant

_source line 1042 · 2026-05-23T12:32:27.917983+00:00_

审稿圆桌会议已启动：

- **Reviewer 1**（方法严谨性 + 实验设计）：已分配，审稿中
- **Reviewer 2**（新颖性 + 完整性）：已分配，审稿中
- **视觉审查 Agent**：已启动，并行执行

等待两位 Reviewer 提交初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 92

## Round 92

2 recorded events


### User

_source line 1043 · 2026-05-23T12:41:03.869915+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见：方法严谨性 + 实验设计

---

## Summary

本文首次系统比较了 LLM 代码修复中三种 execution-free 验证公式（CLS、CWM、TRAJ），使用两个模型家族、两个复杂度级别和多种 seed，发现了三层结构：fine-tuning 必要 → function-level 近等价 → repo-level 因 complexity 分化。统计方法的严谨性（TOST、Bayesian ROPE、clustered bootstrap、Holm-Bonferroni）在 NLP 实证工作中罕见且值得肯定。然而 CLS-TRAJ 比较受制于多个混淆因素和极低统计检验力（power ~0.3），CWM baseline 的生态效度存疑（≤8B LoRA vs 原始 32B+execution-trace pretraining），削弱了论文核心"三方比较"叙事的说服力。

---

## Strengths

**S1. 首个控制变量的系统比较。** 先前工作在不同模型、数据集和评估协议下比较 formulations，本文固定这些变量进行匹配比较，直接回答了从业者关心的 formulation 选择问题（§1, §3）。

**S2. 高质量统计框架。** TOST 等价检验 + Bayesian ROPE 双验证、问题级 clustered bootstrap（114 clusters, 10K iterations）、Holm-Bonferroni 多重比较校正（Table 15）、ICC 估计和 DEFF 修正——这套组合在 NLP 实验论文中极为少见。CLS-CWM 等价结论在多个统计方法下一致（TOST p=0.007; Bayesian P(ROPE)=0.975），可信度高。

**S3. 透明的混淆因素分析。** §3.7 和 Appendix O 明确列出并量化了 5 个 confounds，包括 preprocessing-checkpoint 链式影响（7.68pp）和 worst-case compounding 分析（±11.5pp）。这种诚实度在投稿论文中难得。

**S4. 实用的 failure mode taxonomy。** 三类失败模式（formal collapse、decision collapse、aggregation penalty）提供了超越准确率数字的诊断框架（Table 4, §3.5, Appendix H-I），对实践者有直接价值。

**S5. 多粒度分析揭示 complexity-dependent 行为。** Function-level 等价 + repo-level 分化的发现，以及 formulation×complexity 交互效应的统计确认（z=−23.7, p<0.001, Appendix M），证明了单一粒度评估会遗漏关键信号。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] CLS-TRAJ "未确认等价" 的结论在 power ~0.3 下被 over-stated

- 具体位置：Abstract paragraph 2; §3.4; §5 Conclusion
- 问题：论文 abstract 说 "TRAJ parity is not confirmed after multiple comparison correction at any scale tested"。但 §3.4 明确报告 power ~0.3（Cohen, 1988），即存在 70% 的 Type II 错误概率。在这种条件下：
  - TOST p=0.025（pre-Holm）本身是 nominally significant 的
  - Holm 校正后 p=0.075（Table 15）仅 borderline
  - Bayesian ROPE 说 "inconclusive"（P(ROPE)=0.742, §J.1）
  - 14B 时差距收敛到 1.07pp 且 TOST 确认等价（p=0.043）
  
  Abstract 和 Conclusion 中 "not confirmed" 的措辞可能让读者误以为存在差异的证据，而实际是检验力不足以检测等价。这是 "absence of evidence" vs "evidence of absence" 的经典混淆。
- 为什么影响接收：这直接影响论文的核心三方比较叙事。如果 CLS-TRAJ 区别可能只是统计噪音（power 不足），那么"三层结构"中 TRAJ 的独特地位就站不住。
- 建议修改方向：(1) Abstract 应加入 power 限定语，如 "under current sample size (power ~0.3), TRAJ equivalence is not confirmed but cannot be ruled out"; (2) Conclusion 应明确讨论 power ~0.3 的含义——需要多少 seed 才能达到 power ≥0.8；(3) 14B 结果（三个 formulations 收敛到 1.07pp 以内）应在 abstract 中给予更突出位置。

**N2** [critical] Appendix "P: Limitations" 可能违反 EMNLP 格式规则

- 具体位置：Appendix 概览（第 12 页 line 2）列出 "P: Limitations"；`\paragraph{Extended limitations.}` (appendix.tex line 563)
- 问题：EMNLP 2026 / ARR 规定 "一篇文章只能有一个 limitations section，放在正文里面，appendix 不能有 limitations section"。虽然技术上这是 `\paragraph` 而非 `\section`，但 Appendix 概览明确将其列为独立条目 "P: Limitations"，在形式上构成第二个 limitations 部分。
- 为什么影响接收：格式违规可能导致 desk reject 或被 reviewer 标记为不合规。
- 建议修改方向：将该段落重命名为 "Extended Experimental Details" 或 "Additional Confound Analysis"，并从 Appendix 概览中移除 "P: Limitations" 标签。内容可保留，但避免使用 "limitations" 一词作为标题。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] TRAJ 训练配置的非对称性在正文中讨论不足

- 具体位置：§3.1（简略提及）; Appendix E/O（详细讨论）
- 问题：TRAJ 的训练条件与 CLS/CWM 有根本差异：~400 vs ~70K 训练样本、不同 learning rate（2×10⁻⁴ vs 5×10⁻⁵）、variant-level labels（n=48）vs per-test（n=9,784）。论文在 Appendix B 进行了 downsample ablation（CLS 80.74% vs TRAJ 72.92%），控制了数据量但未控制 label granularity。这些差异部分是 formulation inherent 的（如 label granularity），但正文 §3 在呈现三方比较结果时未充分突出这一不对称性。
- 建议：§3.1 或 §3.4 应添加一段明确声明，说明 TRAJ 比较在训练配置层面与 CLS/CWM 不完全匹配，读者在解读 TRAJ 相关结论时需注意此限制。

**W2** [warning] CWM baseline 生态效度不足

- 具体位置：Limitations（第 8 页）; Appendix O paragraph "CWM scale and pretraining"
- 问题：原始 CWM（FAIR CodeGen team, 2025）使用 32B 模型 + execution-trace mid-training。本文的 ≤8B LoRA CWM 可能未能捕捉使原始 CWM 有效的核心机制（如大规模模型对 output format 的更好控制）。论文的 repo-level 结论——CWM 大幅落后 CLS——可能是 scale 造成的 artifact 而非 formulation 的固有劣势。
- 为什么重要：如果 CWM 的 repo-level 劣势主要由 scale 驱动而非 formulation 设计，那么论文关于 "formulation choice matters at repo level" 的核心 claim 就被削弱。
- 建议：(1) 在 §5 Conclusion 中更突出地声明 repo-level 结论的 conditional 性质；(2) 讨论 14B 结果（CLS-CWM gap 缩窄到 0.43pp）是否暗示 scale 可以消除 formulation 差异。

**W3** [warning] Repo-level seed coverage 稀疏

- 具体位置：§3.1; Table 3
- 问题：Repo-level 实验中，Qwen3-8B CLS/TRAJ 有 3 seeds，DeepSeek CLS 只有 2 seeds。某些 repo-level 配置只有 n=2，这使得 repo-level 的统计推断（尤其是 CLS-CWM 18-26pp gap 的可靠性）受限。Table 3 的标注 "n=2 seeds" 容易被忽略。
- 建议：正文 §3.5 应明确讨论 repo-level seed coverage 的局限性，而非仅在表注中提及。

**W4** [warning] Checkpoint selection confound 的 ablation 覆盖不足

- 具体位置：§3.7; Appendix O
- 问题：NaN validation loss 导致 DeepSeek CWM（repo）和 DeepSeek CLS s123 被迫使用 final-epoch checkpoint。Checkpoint ablation 仅在 Qwen3-4B CLS（~1pp range）上进行，未覆盖受影响最严重的配置。Appendix O 报告 CWM 的 early-stopped vs final-epoch 差距可达 ~18pp（DeepSeek-Coder s123: 75.45% vs 57.31%），这远超 "~1pp" 的估计。
- 建议：至少对一个受影响的 CWM 配置进行 checkpoint ablation（如 Qwen3-8B CWM repo，有 3 seeds），以量化该 confound 对 CWM 的实际影响。

---

## Minor 问题（不影响接收）

- **M1**: SESOI ±2pp 的设定（Appendix J）基于 deployment relevance 而非 pre-registration。虽然合理，但应在正文或附录中明确说明是否为事前确定还是事后合理化。
- **M2**: Figure 2 的 y-axis 从非零基线开始。虽然有 shaded gap region 标注，但仍可能在视觉上放大差异。建议在 caption 中更明确地提示。
- **M3**: Mixed-effects regression（Appendix M）中 LPM 和 GEE 在 model identity 显著性上不一致（LPM p=0.002 vs GEE p=0.419）。论文将此归因于 limited clusters（k=25），但未明确说明哪个结果应作为主要参考。建议明确。
- **M4**: §3.4 "Formulation divergence" 段报告 "At 14B (3 seeds), all three formulations narrow to within 1.07pp"——但 14B 仅有 Qwen3 一个 model family，且 seed 数减少到 3。这一结论缺乏跨模型验证。

---

## Questions（需要作者澄清）

**Q1**: ±2pp SESOI 是在看到数据之前确定的，还是在分析过程中根据 observed effect sizes 调整的？如果是后者，请讨论对 TOST 结论的影响。

**Q2**: 在当前实验设计下，需要多少 seeds 才能使 CLS-TRAJ 比较达到 power ≥0.8？这个数字对从业者判断结论的可靠性至关重要。

**Q3**: 为什么 CLS-CWM 使用 seed-level paired analysis（df=4）而 CLS-TRAJ 主要使用 clustered bootstrap？两个比较使用不同的统计方法是否引入了方法论上的不对称性？

**Q4**: Downsample ablation（Appendix B）控制了数据量但未控制 label granularity（per-test vs variant-level）。是否有可能构建 per-test labels for TRAJ（例如，将 variant-level RESOLVED/UNRESOLVED 分解为 per-test predictions）来消除这一混淆？

**Q5**: 14B 结果显示所有 formulations 收敛——如果有 32B 的实验数据，是否预期 repo-level 差异也会消失？如果是，论文的 "formulation choice matters at repo level" claim 是否应更明确地限定为 "at ≤8B scale"？

---

## Missing References

未发现明显遗漏。论文引用了 TOST 文献（Schuirmann, 1987; Holm, 1979; Lakens, 2017）、equivalence testing 教材（Wellek, 2010）、power analysis（Cohen, 1988; Hoenig & Heisey, 2001）以及所有主要的 code repair 和 verification 相关工作。

---

## 主要优势总结

1. 回答了一个高度实用的问题——从业者如何选择 verification formulation
2. 统计方法论的严谨性在 NLP 实证工作中堪称范式级别
3. 对混淆因素的坦诚分析提高了结论的可信度
4. Failure mode taxonomy 具有独立的实践价值
5. 14B 收敛结果暗示 capacity scaling 可能是解决 formulation 差异的关键路径

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | CLS-CWM 比较可靠（多方法一致），但 CLS-TRAJ 比较受限于 power ~0.3 + 训练配置非对称性；repo-level 结论受 CWM 生态效度和 checkpoint confound 影响 |
| Excitement | 3/5 | 实用问题 + 严谨方法论值得关注，但核心发现（function-level 近等价、repo-level 分化）在概念上不意外；无新方法贡献 |
| Reproducibility | 4/5 | 超参数详尽（Table 11, Appendix E）、统计细节完整、但代码/数据未公开（可理解，double-blind） |
| Overall Assessment | 3/5 — Findings | CLS-CWM 等价这一核心发现可靠且有价值，但 TRAJ 比较的混淆因素、CWM 生态效度不足、以及 power ~0.3 下的过度解读使得论文难以达到主会议标准。修复 N1（abstract 措辞）和 N2（格式合规）后可达 3.5 |
| Confidence | 4/5 | 仔细阅读全文含全部附录，熟悉 equivalence testing 和 NLP 评估方法论 |

**一句话总结**: 统计框架一流、confound 分析透明，但三方比较中 TRAJ 一翼受多重混淆和低 power 削弱，CWM 一翼受生态效度限制——实际上只有 CLS-CWM function-level 等价这一个可靠的新发现，尚不足以支撑主会议接收。


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

_source line 1044 · 2026-05-23T12:41:09.617275+00:00_

Reviewer 1 已提交审稿意见。等待 Reviewer 2 完成独立审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 93

## Round 93

2 recorded events


### User

_source line 1045 · 2026-05-23T12:41:24.248400+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交完整审稿意见，核心判断：

- **Overall: 3/5 (Findings)**
- **Soundness: 3.5** — CLS-CWM 等价结论可靠（多统计方法一致），但 CLS-TRAJ 比较受 power ~0.3 和训练配置非对称性限制
- **Excitement: 3** — 实用问题+严谨方法论，但核心发现概念上不意外
- **2 个 Must-Fix**: (1) Abstract/Conclusion 中 TRAJ "未确认等价" 在 power ~0.3 下被 over-stated；(2) Appendix "P: Limitations" 可能违反 EMNLP 格式规则
- **4 个 Should-Fix**: TRAJ 训练配置非对称性讨论不足、CWM 生态效度、repo-level seed 稀疏、checkpoint confound ablation 覆盖不足
- **5 个 Questions**: SESOI 是否 pre-registered、power ≥0.8 需要多少 seeds、统计方法不对称性、label granularity 控制、32B 预期

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

_source line 1046 · 2026-05-23T12:41:30.569640+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 94

## Round 94

6 recorded events


### User

_source line 1047 · 2026-05-23T12:45:13.704209+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性/贡献 + 完整性

### Summary

本文对 LLM 代码修复中三种免执行验证公式（CLS、CWM、TRAJ）进行了系统性实证比较，在匹配训练条件下跨两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度层级和多个种子进行实验。核心发现：函数级 CLS-CWM 统计等价（TOST 确认），但仓库级等价崩塌（18-26pp gap），由 CWM 格式崩溃驱动。论文同时提供了错误互补性分析和失败模式分类法。

---

### Strengths

**S1. 统计方法论严谨（Soundness 加分项）。** TOST 等价性检验（而非仅做差异性零假设检验）、Bayesian ROPE 分析、混合效应回归、Holm-Bonferroni 校正、ICC 可靠性分析——这套统计工具链在实证 NLP 论文中属于上乘水准。特别是 §3.4 明确区分"等价"与"未能拒绝差异"，许多实证论文在此犯错。

**S2. 匹配实验框架设计合理。** 控制模型容量、训练数据、超参数和评估协议是公式对比的正确做法。函数级 5 种子复制提供了足够的统计功效。Table 1 的 cross-family 一致性（Qwen3 和 DeepSeek-Coder 在 CLS-CWM 间差异方向一致）增强了结论的可靠性。

**S3. 诚实报告 confounds 和局限。** 论文承认 TRAJ 训练配置差异（Appendix P）、14B 局限性（3 seeds, 1 family）、仓库级多重混淆因素（§3.7），CLS-TRAJ 等价在校正后不成立也被如实陈述。这种透明度值得肯定。

**S4. 可操作的失败模式分类法。** Table 4 提供了格式崩溃（CWM）、决策崩溃（CLS）、聚合惩罚（CLS）三种诊断类别及代表性样例（Appendix H-I 有详细定性分析），对实践者选择验证公式具有实用价值。

**S5. 领域特异性观察（GenRM 对比）。** 代码验证中生成式公式（CWM）未胜过判别式（CLS），与 GenRM 在数学推理中的发现相反（§4, §5）。这是一个有价值的数据点。

**S6. Related Work 覆盖充分。** CodeScaler、Aletheia、GenRM、GenPRM、FunPRM、CodeRM 均已引用并做了恰当区分。我未发现 2025-2026 年免执行验证领域的重大遗漏。

---

### Weaknesses

#### Must-Fix（影响接收决定）

**N1. [critical] 核心发现可从论文自身理论分析中预测，新颖性不足。**
- 具体位置：§2.2 "Expected Failure Modes"、§1 Introduction (p.2, "consistent with the theoretical analysis in §2.2")
- 问题：§2.2 预测短输出最小化生成特有失败模式（→ 函数级 CLS-CWM 等价），长输出触发格式崩溃（→ 仓库级发散）。论文主文也明确承认函数级结果"与 §2.2 的理论分析一致"。如果两个核心结论（等价 + 崩溃）都被自身理论预测，实证贡献降格为"验证"而非"发现"。
- 为什么影响接收：Excitement 的核心在于 surprising findings。一篇 confirmation study 在 Excitement 维度难以获得高分，直接影响 Overall Assessment。
- 建议修改方向：(a) 诚实重新定位为"首次严格实证验证"；(b) 或更好的是，深入分析理论预测 WHERE 失败（例如 14B 收敛速度是否符合预期？格式崩溃的具体阈值是否可预测？），将重心从"确认预测"转向"刻画边界条件"。

**N2. [critical] TRAJ 比较被训练配置严重混淆。**
- 具体位置：Appendix P (p.22-23)、Tables 1-3
- 问题：TRAJ 使用 ~400 训练实例 vs CLS/CWM 的 ~70K；不同学习率（5×10⁻⁵ vs 2×10⁻⁴）；变体级评估（n=48 vs n=9,784）。尽管 Appendix P 承认这些差异，主文 Tables 1-3 和 §3.2-3.4 仍将 TRAJ 与 CLS/CWM 并列呈现，贡献声明也围绕"三种公式"和"三层结构"构建。
- 为什么影响接收：不公平的三方比较削弱了方法论贡献的可信度。Reviewer 无法判断 TRAJ 的劣势是来自公式本身还是训练数据量差异。
- 建议修改方向：(a) 提供匹配数据量的 TRAJ 训练（~70K 实例）；或 (b) 明确将核心贡献限制为 CLS vs CWM 比较，TRAJ 降格为 exploratory baseline 并在主文中标注。

#### Should-Fix（影响评分但不一票否决）

**W1. [warning] 模型规模有限，"容量依赖收敛" claim 证据不足。**
- 具体位置：Abstract ("At 14B (3 seeds)...")、§5 Conclusion、Table 2
- 问题：14B 实验仅用 Qwen3（1 个模型家族、3 个种子）。TOST 在 df=2 时"缺乏功效来确认"等价性（§5 明确承认）。无 32B+ 实验，尽管 Future Direction (1) 呼吁此研究。
- 建议：将 14B 结论从 stated finding 降级为 preliminary observation，或在 Abstract 中加入更强的 hedging。

**W2. [warning] Oracle 互补性实际不可操作，作为贡献存在误导。**
- 具体位置：§3.5, Table 4, Contribution 2 (p.2)
- 问题：Oracle 准确率 90.63% vs 个体最佳 ~88%，但"简单启发式仅捕获 <0.4pp 的 oracle 优势"。论文将此定义为"探索公式级权衡的最强实践论据"（Contribution 2），但证据显示当前方法实际无法利用这种互补性。
- 建议：重新框定为 negative result（互补性存在但目前不可利用），降低贡献权重。

**W3. [warning] 正文可能超过 8 页限制。**
- 具体位置：PDF p.8-9 边界
- 问题：Section 5 (Conclusion) 在 p.8 底部开始，文本延续到 p.9（约 5-8 行结论文字出现在 p.9 顶部，"Limitations" 标题之前）。按 EMNLP 2026 规则，Conclusion 属于正文计入 8 页限制，Limitations 不计。
- 建议：压缩 Conclusion 或 Related Work 使正文严格 ≤8 页。

**W4. [warning] GenRM 领域特异性对比是最有潜力的发现，但分析不充分。**
- 具体位置：§4 Related Work (1 句话)、§5 Conclusion (1 句话)
- 问题：代码中生成式 ≤ 判别式（与 GenRM 数学结论相反）是本文最具新颖性的观察，但仅获得约 2 句话讨论。未分析 WHY 存在领域差异（输出结构？格式合规率？错误类型？）。
- 为什么影响评分：浪费了论文中最具 Excitement 潜力的发现，直接拉低 Excitement 得分。
- 建议：新增 1-2 段分析代码 vs 数学验证的结构性差异，提出可检验假设。

**W5. [warning] PRM/ORM 映射可能令读者困惑。**
- 具体位置：§4 ("CLS corresponds to process-level (PRM-like)...TRAJ provides outcome-level (ORM-like)")
- 问题：命名反直觉——"classification" 听起来像 ORM，"trajectory" 听起来像 PRM。实际区分（per-test vs per-patch 粒度）是正确的，但需要更显式的解释以避免误读。

#### Minor（不影响接收）

**M1.** Abstract 中包含较多统计符号（z=−23.7, TOST, pp 值），可能降低可读性。建议先陈述定性洞见，再给统计支撑。

**M2.** Figure 2 y 轴起始于 ~86% 而非 0%，视觉上放大了 CLS-CWM 差距。主文诚实讨论了实际幅度，但图表本身可能给快速浏览者造成误导。

**M3.** 16 个附录（A-P，~15 页）vs 8 页正文。部分关键分析（TOST 灵敏度 Appendix J、混合效应回归 Appendix M、Bayesian ROPE Appendix J）是评估主要 claims 所必需的。这暗示论文可能试图在单篇论文中承载过多内容。

**M4.** 三项贡献并非完全独立："错误互补性"和"失败模式分类法"是支撑"复杂度调节的公式选择"主发现的辅助分析，而非独立贡献。建议重构为一项核心贡献加两项 supporting analyses。

---

### Questions（需要作者澄清）

**Q1.** 为何不扩展到 ≥32B 模型？容量依赖收敛假说是论文最具前瞻性的暗示，但目前仅有 1 个家族 3 个种子的 14B 数据。

**Q2.** 能否提供 TRAJ 使用 ~70K 训练实例（与 CLS/CWM 匹配）的结果？否则三方比较不受控。

**Q3.** 代码验证中生成式 ≤ 判别式（与 GenRM 数学结论相反）的具体原因是什么？是输出 token 数量、结构化格式要求、还是其他因素？

**Q4.** 既然简单启发式仅捕获 <0.4pp 的 oracle 优势，是否尝试过更复杂的集成方法（如学习路由、置信度加权组合）？

**Q5.** 14B 实验能否用 DeepSeek-Coder-14B（或类似规模）进行 cross-family 复制，以检验收敛是否与模型家族相关？

---

### Missing References

已搜索 2025-2026 年免执行验证领域的关键工作：
- CodeScaler (Zhu et al., 2026) — 已引用 ✓
- Aletheia (Venkatkrishna et al., 2026) — 已引用 ✓
- GenPRM (Zhao et al., 2026) — 已引用 ✓
- FunPRM (Zhang et al., 2026) — 已引用 ✓
- CodeRM (Ma et al., 2025) — 已引用 ✓

**未发现重大遗漏。** Related Work 对 2025-2026 年景观的覆盖充分。PRM/ORM 映射（CLS→PRM-like, TRAJ→ORM-like, CWM→GenRM）在粒度维度上准确，但命名上需更显式说明。

---

### 评分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 4/5 (Strong) | CLS-CWM 比较在匹配条件下充分支撑，统计框架（TOST/ROPE/ICC/混合效应）出色。扣分点：TRAJ 比较被训练配置混淆（N2），14B claim 证据有限（W1）。 |
| **Excitement** | 3/5 (Interesting) | 核心发现（函数级等价、仓库级崩溃）可从 §2.2 理论预测（N1），属 confirmation 而非 discovery。GenRM 领域对比（W4）有潜力但未充分开发。失败模式分类法有实用价值。 |
| **Reproducibility** | 4/5 | 超参数（Appendix E）、prompt 模板（Appendix F）、种子值均已详述。未提及代码/数据释放计划。 |
| **Overall Assessment** | **3.0 (Findings)** | 方法论严谨的实证比较研究，为从业者提供可操作的公式选择建议。统计分析水准高于多数实证论文。但核心发现的可预测性限制了新颖性，比较研究的格式天然限制了 Excitement。适合 Findings 发表。 |
| **Confidence** | 4/5 (Quite sure) | 熟悉代码验证公式和实证 NLP 方法论，仔细审查了统计分析和实验设计。 |

**一句话总结：** 一篇统计严谨但发现增量性的实证比较研究——方法论值得学习，但核心结论可从自身理论预测，且 TRAJ 比较的训练配置混淆削弱了"三公式比较"的完整性。

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

_source line 1048 · 2026-05-23T12:46:52.006881+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性/贡献 + 完整性\n\n### Summary\n\n本文对 LLM 代码修复中三种免执行验证公式（CLS、CWM、TRAJ）进行了系统性实证比较，在匹配训练条件下跨两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度层级和多个种子进行实验。核心发现：函数级 CLS-CWM 统计等价（TOST 确认），但仓库级等价崩塌（18-26pp gap），由 CWM 格式崩溃驱动。论文同时提供了错误互补性分析和失败模式分类法。\n\n### Strengths\n\n**S1. 统计方法论严谨（Soundness 加分项）。** TOST 等价性检验（而非仅做差异性零假设检验）、Bayesian ROPE 分析、混合效应回归、Holm-Bonferroni 校正、ICC 可靠性分析——这套统计工具链在实证 NLP 论文中属于上乘水准。特别是 §3.4 明确区分\"等价\"与\"未能拒绝差异\"，许多实证论文在此犯错。\n\n**S2. 匹配实验框架设计合理。** 控制模型容量、训练数据、超参数和评估协议是公式对比的正确做法。函数级 5 种子复制提供了足够的统计功效。Table 1 的 cross-family 一致性（Qwen3 和 DeepSeek-Coder 在 CLS-CWM 间差异方向一致）增强了结论的可靠性。\n\n**S3. 诚实报告 confounds 和局限。** 论文承认 TRAJ 训练配置差异（Appendix P）、14B 局限性（3 seeds, 1 family）、仓库级多重混淆因素（§3.7），CLS-TRAJ 等价在校正后不成立也被如实陈述。这种透明度值得肯定。\n\n**S4. 可操作的失败模式分类法。** Table 4 提供了格式崩溃（CWM）、决策崩溃（CLS）、聚合惩罚（CLS）三种诊断类别及代表性样例（Appendix H-I 有详细定性分析），对实践者选择验证公式具有实用价值。\n\n**S5. 领域特异性观察（GenRM 对比）。** 代码验证中生成式公式（CWM）未胜过判别式（CLS），与 GenRM 在数学推理中的发现相反（§4, §5）。这是一个有价值的数据点。\n\n**S6. Related Work 覆盖充分。** CodeScaler、Aletheia、GenRM、GenPRM、FunPRM、CodeRM 均已引用并做了恰当区分。我未发现 2025-2026 年免执行验证领域的重大遗漏。\n\n### Must-Fix（影响接收决定）\n\n**N1. [critical] 核心发现可从论文自身理论分析中预测，新颖性不足。**\n- 具体位置：§2.2 \"Expected Failure Modes\"、§1 Introduction (p.2, \"consistent with the theoretical analysis in §2.2\")\n- 问题：§2.2 预测短输出最小化生成特有失败模式（→ 函数级 CLS-CWM 等价），长输出触发格式崩溃（→ 仓库级发散）。论文主文也明确承认函数级结果\"与 §2.2 的理论分析一致\"。如果两个核心结论（等价 + 崩溃）都被自身理论预测，实证贡献降格为\"验证\"而非\"发现\"。\n- 为什么影响接收：Excitement 的核心在于 surprising findings。一篇 confirmation study 在 Excitement 维度难以获得高分，直接影响 Overall Assessment。\n- 建议修改方向：(a) 诚实重新定位为\"首次严格实证验证\"；(b) 或更好的是，深入分析理论预测 WHERE 失败（例如 14B 收敛速度是否符合预期？格式崩溃的具体阈值是否可预测？），将重心从\"确认预测\"转向\"刻画边界条件\"。\n\n**N2. [critical] TRAJ 比较被训练配置严重混淆。**\n- 具体位置：Appendix P (p.22-23)、Tables 1-3\n- 问题：TRAJ 使用 ~400 训练实例 vs CLS/CWM 的 ~70K；不同学习率（5×10⁻⁵ vs 2×10⁻⁴）；变体级评估（n=48 vs n=9,784）。尽管 Appendix P 承认这些差异，主文 Tables 1-3 和 §3.2-3.4 仍将 TRAJ 与 CLS/CWM 并列呈现，贡献声明也围绕\"三种公式\"和\"三层结构\"构建。\n- 为什么影响接收：不公平的三方比较削弱了方法论贡献的可信度。Reviewer 无法判断 TRAJ 的劣势是来自公式本身还是训练数据量差异。\n- 建议修改方向：(a) 提供匹配数据量的 TRAJ 训练（~70K 实例）；或 (b) 明确将核心贡献限制为 CLS vs CWM 比较，TRAJ 降格为 exploratory baseline 并在主文中标注。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [warning] 模型规模有限，\"容量依赖收敛\" claim 证据不足。**\n- 具体位置：Abstract (\"At 14B (3 seeds)...\")、§5 Conclusion、Table 2\n- 问题：14B 实验仅用 Qwen3（1 个模型家族、3 个种子）。TOST 在 df=2 时\"缺乏功效来确认\"等价性（§5 明确承认）。无 32B+ 实验，尽管 Future Direction (1) 呼吁此研究。\n- 建议：将 14B 结论从 stated finding 降级为 preliminary observation，或在 Abstract 中加入更强的 hedging。\n\n**W2. [warning] Oracle 互补性实际不可操作，作为贡献存在误导。**\n- 具体位置：§3.5, Table 4, Contribution 2 (p.2)\n- 问题：Oracle 准确率 90.63% vs 个体最佳 ~88%，但\"简单启发式仅捕获 <0.4pp 的 oracle 优势\"。论文将此定义为\"探索公式级权衡的最强实践论据\"（Contribution 2），但证据显示当前方法实际无法利用这种互补性。\n- 建议：重新框定为 negative result（互补性存在但目前不可利用），降低贡献权重。\n\n**W3. [warning] 正文可能超过 8 页限制。**\n- 具体位置：PDF p.8-9 边界\n- 问题：Section 5 (Conclusion) 在 p.8 底部开始，文本延续到 p.9（约 5-8 行结论文字出现在 p.9 顶部，\"Limitations\" 标题之前）。按 EMNLP 2026 规则，Conclusion 属于正文计入 8 页限制，Limitations 不计。\n- 建议：压缩 Conclusion 或 Related Work 使正文严格 ≤8 页。\n\n**W4. [warning] GenRM 领域特异性对比是最有潜力的发现，但分析不充分。**\n- 具体位置：§4 Related Work (1 句话)、§5 Conclusion (1 句话)\n- 问题：代码中生成式 ≤ 判别式（与 GenRM 数学结论相反）是本文最具新颖性的观察，但仅获得约 2 句话讨论。未分析 WHY 存在领域差异（输出结构？格式合规率？错误类型？）。\n- 建议：新增 1-2 段分析代码 vs 数学验证的结构性差异，提出可检验假设。\n\n**W5. [warning] PRM/ORM 映射可能令读者困惑。**\n- 具体位置：§4 (\"CLS corresponds to process-level (PRM-like)...TRAJ provides outcome-level (ORM-like)\")\n- 问题：命名反直觉——\"classification\" 听起来像 ORM，\"trajectory\" 听起来像 PRM。实际区分（per-test vs per-patch 粒度）是正确的，但需要更显式的解释以避免误读。\n\n### Minor（不影响接收）\n\n**M1.** Abstract 中包含较多统计符号（z=−23.7, TOST, pp 值），可能降低可读性。建议先陈述定性洞见，再给统计支撑。\n\n**M2.** Figure 2 y 轴起始于 ~86% 而非 0%，视觉上放大了 CLS-CWM 差距。主文诚实讨论了实际幅度，但图表本身可能给快速浏览者造成误导。\n\n**M3.** 16 个附录（A-P，~15 页）vs 8 页正文。部分关键分析（TOST 灵敏度 Appendix J、混合效应回归 Appendix M、Bayesian ROPE Appendix J）是评估主要 claims 所必需的。这暗示论文可能试图在单篇论文中承载过多内容。\n\n**M4.** 三项贡献并非完全独立：\"错误互补性\"和\"失败模式分类法\"是支撑\"复杂度调节的公式选择\"主发现的辅助分析，而非独立贡献。建议重构为一项核心贡献加两项 supporting analyses。\n\n### Questions（需要作者澄清）\n\n**Q1.** 为何不扩展到 ≥32B 模型？容量依赖收敛假说是论文最具前瞻性的暗示，但目前仅有 1 个家族 3 个种子的 14B 数据。\n\n**Q2.** 能否提供 TRAJ 使用 ~70K 训练实例（与 CLS/CWM 匹配）的结果？否则三方比较不受控。\n\n**Q3.** 代码验证中生成式 ≤ 判别式（与 GenRM 数学结论相反）的具体原因是什么？是输出 token 数量、结构化格式要求、还是其他因素？\n\n**Q4.** 既然简单启发式仅捕获 <0.4pp 的 oracle 优势，是否尝试过更复杂的集成方法（如学习路由、置信度加权组合）？\n\n**Q5.** 14B 实验能否用 DeepSeek-Coder-14B（或类似规模）进行 cross-family 复制，以检验收敛是否与模型家族相关？\n\n### Missing References\n\n已搜索 2025-2026 年免执行验证领域的关键工作，未发现重大遗漏。\n\n### 评分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 4/5 (Strong) | CLS-CWM 比较在匹配条件下充分支撑，统计框架出色。扣分点：TRAJ 比较被训练配置混淆，14B claim 证据有限。 |\n| **Excitement** | 3/5 (Interesting) | 核心发现可从 §2.2 理论预测，属 confirmation 而非 discovery。GenRM 领域对比有潜力但未充分开发。 |\n| **Reproducibility** | 4/5 | 超参数、prompt 模板、种子值均已详述。未提及代码/数据释放计划。 |\n| **Overall Assessment** | **3.0 (Findings)** | 方法论严谨的实证比较研究，统计分析水准高于多数实证论文。但核心发现的可预测性限制了新颖性。适合 Findings 发表。 |\n| **Confidence** | 4/5 (Quite sure) | 熟悉代码验证公式和实证 NLP 方法论。 |"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性/贡献 + 完整性\n\n### Summary\n\n本文对 LLM 代码修复中三种免执行验证公式（CLS、CWM、TRAJ）进行了系统性实证比较，在匹配训练条件下跨两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度层级和多个种子进行实验。核心发现：函数级 CLS-CWM 统计等价（TOST 确认），但仓库级等价崩塌（18-26pp gap），由 CWM 格式崩溃驱动。论文同时提供了错误互补性分析和失败模式分类法。\n\n### Strengths\n\n**S1. 统计方法论严谨（Soundness 加分项）。** TOST 等价性检验（而非仅做差异性零假设检验）、Bayesian ROPE 分析、混合效应回归、Holm-Bonferroni 校正、ICC 可靠性分析——这套统计工具链在实证 NLP 论文中属于上乘水准。特别是 §3.4 明确区分\"等价\"与\"未能拒绝差异\"，许多实证论文在此犯错。\n\n**S2. 匹配实验框架设计合理。** 控制模型容量、训练数据、超参数和评估协议是公式对比的正确做法。函数级 5 种子复制提供了足够的统计功效。Table 1 的 cross-family 一致性（Qwen3 和 DeepSeek-Coder 在 CLS-CWM 间差异方向一致）增强了结论的可靠性。\n\n**S3. 诚实报告 confounds 和局限。** 论文承认 TRAJ 训练配置差异（Appendix P）、14B 局限性（3 seeds, 1 family）、仓库级多重混淆因素（§3.7），CLS-TRAJ 等价在校正后不成立也被如实陈述。这种透明度值得肯定。\n\n**S4. 可操作的失败模式分类法。** Table 4 提供了格式崩溃（CWM）、决策崩溃（CLS）、聚合惩罚（CLS）三种诊断类别及代表性样例（Appendix H-I 有详细定性分析），对实践者选择验证公式具有实用价值。\n\n**S5. 领域特异性观察（GenRM 对比）。** 代码验证中生成式公式（CWM）未胜过判别式（CLS），与 GenRM 在数学推理中的发现相反（§4, §5）。这是一个有价值的数据点。\n\n**S6. Related Work 覆盖充分。** CodeScaler、Aletheia、GenRM、GenPRM、FunPRM、CodeRM 均已引用并做了恰当区分。我未发现 2025-2026 年免执行验证领域的重大遗漏。\n\n### Must-Fix（影响接收决定）\n\n**N1. [critical] 核心发现可从论文自身理论分析中预测，新颖性不足。**\n- 具体位置：§2.2 \"Expected Failure Modes\"、§1 Introduction (p.2, \"consistent with the theoretical analysis in §2.2\")\n- 问题：§2.2 预测短输出最小化生成特有失败模式（→ 函数级 CLS-CWM 等价），长输出触发格式崩溃（→ 仓库级发散）。论文主文也明确承认函数级结果\"与 §2.2 的理论分析一致\"。如果两个核心结论（等价 + 崩溃）都被自身理论预测，实证贡献降格为\"验证\"而非\"发现\"。\n- 为什么影响接收：Excitement 的核心在于 surprising findings。一篇 confirmation study 在 Excitement 维度难以获得高分，直接影响 Overall Assessment。\n- 建议修改方向：(a) 诚实重新定位为\"首次严格实证验证\"；(b) 或更好的是，深入分析理论预测 WHERE 失败（例如 14B 收敛速度是否符合预期？格式崩溃的具体阈值是否可预测？），将重心从\"确认预测\"转向\"刻画边界条件\"。\n\n**N2. [critical] TRAJ 比较被训练配置严重混淆。**\n- 具体位置：Appendix P (p.22-23)、Tables 1-3\n- 问题：TRAJ 使用 ~400 训练实例 vs CLS/CWM 的 ~70K；不同学习率（5×10⁻⁵ vs 2×10⁻⁴）；变体级评估（n=48 vs n=9,784）。尽管 Appendix P 承认这些差异，主文 Tables 1-3 和 §3.2-3.4 仍将 TRAJ 与 CLS/CWM 并列呈现，贡献声明也围绕\"三种公式\"和\"三层结构\"构建。\n- 为什么影响接收：不公平的三方比较削弱了方法论贡献的可信度。Reviewer 无法判断 TRAJ 的劣势是来自公式本身还是训练数据量差异。\n- 建议修改方向：(a) 提供匹配数据量的 TRAJ 训练（~70K 实例）；或 (b) 明确将核心贡献限制为 CLS vs CWM 比较，TRAJ 降格为 exploratory baseline 并在主文中标注。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [warning] 模型规模有限，\"容量依赖收敛\" claim 证据不足。**\n- 具体位置：Abstract (\"At 14B (3 seeds)...\")、§5 Conclusion、Table 2\n- 问题：14B 实验仅用 Qwen3（1 个模型家族、3 个种子）。TOST 在 df=2 时\"缺乏功效来确认\"等价性（§5 明确承认）。无 32B+ 实验，尽管 Future Direction (1) 呼吁此研究。\n- 建议：将 14B 结论从 stated finding 降级为 preliminary observation，或在 Abstract 中加入更强的 hedging。\n\n**W2. [warning] Oracle 互补性实际不可操作，作为贡献存在误导。**\n- 具体位置：§3.5, Table 4, Contribution 2 (p.2)\n- 问题：Oracle 准确率 90.63% vs 个体最佳 ~88%，但\"简单启发式仅捕获 <0.4pp 的 oracle 优势\"。论文将此定义为\"探索公式级权衡的最强实践论据\"（Contribution 2），但证据显示当前方法实际无法利用这种互补性。\n- 建议：重新框定为 negative result（互补性存在但目前不可利用），降低贡献权重。\n\n**W3. [warning] 正文可能超过 8 页限制。**\n- 具体位置：PDF p.8-9 边界\n- 问题：Section 5 (Conclusion) 在 p.8 底部开始，文本延续到 p.9（约 5-8 行结论文字出现在 p.9 顶部，\"Limitations\" 标题之前）。按 EMNLP 2026 规则，Conclusion 属于正文计入 8 页限制，Limitations 不计。\n- 建议：压缩 Conclusion 或 Related Work 使正文严格 ≤8 页。\n\n**W4. [warning] GenRM 领域特异性对比是最有潜力的发现，但分析不充分。**\n- 具体位置：§4 Related Work (1 句话)、§5 Conclusion (1 句话)\n- 问题：代码中生成式 ≤ 判别式（与 GenRM 数学结论相反）是本文最具新颖性的观察，但仅获得约 2 句话讨论。未分析 WHY 存在领域差异（输出结构？格式合规率？错误类型？）。\n- 建议：新增 1-2 段分析代码 vs 数学验证的结构性差异，提出可检验假设。\n\n**W5. [warning] PRM/ORM 映射可能令读者困惑。**\n- 具体位置：§4 (\"CLS corresponds to process-level (PRM-like)...TRAJ provides outcome-level (ORM-like)\")\n- 问题：命名反直觉——\"classification\" 听起来像 ORM，\"trajectory\" 听起来像 PRM。实际区分（per-test vs per-patch 粒度）是正确的，但需要更显式的解释以避免误读。\n\n### Minor（不影响接收）\n\n**M1.** Abstract 中包含较多统计符号（z=−23.7, TOST, pp 值），可能降低可读性。建议先陈述定性洞见，再给统计支撑。\n\n**M2.** Figure 2 y 轴起始于 ~86% 而非 0%，视觉上放大了 CLS-CWM 差距。主文诚实讨论了实际幅度，但图表本身可能给快速浏览者造成误导。\n\n**M3.** 16 个附录（A-P，~15 页）vs 8 页正文。部分关键分析（TOST 灵敏度 Appendix J、混合效应回归 Appendix M、Bayesian ROPE Appendix J）是评估主要 claims 所必需的。这暗示论文可能试图在单篇论文中承载过多内容。\n\n**M4.** 三项贡献并非完全独立：\"错误互补性\"和\"失败模式分类法\"是支撑\"复杂度调节的公式选择\"主发现的辅助分析，而非独立贡献。建议重构为一项核心贡献加两项 supporting analyses。\n\n### Questions（需要作者澄清）\n\n**Q1.** 为何不扩展到 ≥32B 模型？容量依赖收敛假说是论文最具前瞻性的暗示，但目前仅有 1 个家族 3 个种子的 14B 数据。\n\n**Q2.** 能否提供 TRAJ 使用 ~70K 训练实例（与 CLS/CWM 匹配）的结果？否则三方比较不受控。\n\n**Q3.** 代码验证中生成式 ≤ 判别式（与 GenRM 数学结论相反）的具体原因是什么？是输出 token 数量、结构化格式要求、还是其他因素？\n\n**Q4.** 既然简单启发式仅捕获 <0.4pp 的 oracle 优势，是否尝试过更复杂的集成方法（如学习路由、置信度加权组合）？\n\n**Q5.** 14B 实验能否用 DeepSeek-Coder-14B（或类似规模）进行 cross-family 复制，以检验收敛是否与模型家族相关？\n\n### Missing References\n\n已搜索 2025-2026 年免执行验证领域的关键工作，未发现重大遗漏。\n\n### 评分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 4/5 (Strong) | CLS-CWM 比较在匹配条件下充分支撑，统计框架出色。扣分点：TRAJ 比较被训练配置混淆，14B claim 证据有限。 |\n| **Excitement** | 3/5 (Interesting) | 核心发现可从 §2.2 理论预测，属 confirmation 而非 discovery。GenRM 领域对比有潜力但未充分开发。 |\n| **Reproducibility** | 4/5 | 超参数、prompt 模板、种子值均已详述。未提及代码/数据释放计划。 |\n| **Overall Assessment** | **3.0 (Findings)** | 方法论严谨的实证比较研究，统计分析水准高于多数实证论文。但核心发现的可预测性限制了新颖性。适合 Findings 发表。 |\n| **Confidence** | 4/5 (Quite sure) | 熟悉代码验证公式和实证 NLP 方法论。 |"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-23T12:47:25.949129+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33942
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-23T12:47:26.350985+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n### Summary\n\n本文首次系统比较了 LLM 代码修复中三种 execution-free 验证公式（CLS、CWM、TRAJ），使用两个模型家族、两个复杂度级别和多种 seed，发现了三层结构：fine-tuning 必要 → function-level 近等价 → repo-level 因 complexity 分化。统计方法的严谨性（TOST、Bayesian ROPE、clustered bootstrap、Holm-Bonferroni）在 NLP 实证工作中罕见且值得肯定。然而 CLS-TRAJ 比较受制于多个混淆因素和极低统计检验力（power ~0.3），CWM baseline 的生态效度存疑（≤8B LoRA vs 原始 32B+execution-trace pretraining），削弱了论文核心\"三方比较\"叙事的说服力。\n\n### Must-Fix 问题\n\n**N1** [critical] CLS-TRAJ \"未确认等价\" 的结论在 power ~0.3 下被 over-stated\n- Abstract 说 \"TRAJ parity is not confirmed after multiple comparison correction at any scale tested\"。但 §3.4 明确报告 power ~0.3（Cohen, 1988），即存在 70% 的 Type II 错误概率。\n- TOST p=0.025（pre-Holm）本身是 nominally significant 的\n- Holm 校正后 p=0.075 仅 borderline\n- 14B 时差距收敛到 1.07pp 且 TOST 确认等价（p=0.043）\n- Abstract 和 Conclusion 中 \"not confirmed\" 的措辞可能让读者误以为存在差异的证据\n- 建议：Abstract 应加入 power 限定语；Conclusion 应明确讨论 power ~0.3 的含义；14B 结果应在 abstract 中给予更突出位置\n\n**N2** [critical] Appendix \"P: Limitations\" 可能违反 EMNLP 格式规则\n- EMNLP 2026 / ARR 规定 \"一篇文章只能有一个 limitations section，放在正文里面，appendix 不能有 limitations section\"\n- Appendix 概览明确将其列为独立条目 \"P: Limitations\"\n- 建议：将该段落重命名为 \"Extended Experimental Details\" 或 \"Additional Confound Analysis\"\n\n### Should-Fix 问题\n\n**W1** [warning] TRAJ 训练配置的非对称性在正文中讨论不足\n- TRAJ 的训练条件与 CLS/CWM 有根本差异：~400 vs ~70K 训练样本、不同 learning rate、variant-level labels vs per-test\n- Downsample ablation 控制了数据量但未控制 label granularity\n\n**W2** [warning] CWM baseline 生态效度不足\n- 原始 CWM 使用 32B + execution-trace mid-training\n- ≤8B LoRA CWM 可能未能捕捉使原始 CWM 有效的核心机制\n\n**W3** [warning] Repo-level seed coverage 稀疏\n- 某些配置只有 n=2 seeds，限制统计推断\n\n**W4** [warning] Checkpoint selection confound 的 ablation 覆盖不足\n- Checkpoint ablation 仅在 Qwen3-4B CLS 上进行\n- CWM early-stopped vs final-epoch 差距可达 ~18pp（DeepSeek-Coder）\n\n### Minor 问题\n\n**M1**: SESOI ±2pp 是否 pre-registered？\n**M2**: Figure 2 y-axis 非零基线\n**M3**: LPM vs GEE 在 model identity 显著性上不一致\n**M4**: 14B 仅 Qwen3 一个 family\n\n### Questions\n\n**Q1**: ±2pp SESOI 是在看到数据之前还是之后确定的？\n**Q2**: 需要多少 seeds 才能使 CLS-TRAJ 达到 power ≥0.8？\n**Q3**: CLS-CWM 使用 seed-level paired analysis 而 CLS-TRAJ 用 clustered bootstrap，是否引入方法论不对称？\n**Q4**: 是否可能构建 per-test labels for TRAJ 来消除 label granularity 混淆？\n**Q5**: 如果有 32B 实验数据，是否预期 repo-level 差异会消失？\n\n### 评分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3/5 |\n| Reproducibility | 4/5 |\n| Overall Assessment | 3/5 (Findings) |\n| Confidence | 4/5 |"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n### Summary\n\n本文首次系统比较了 LLM 代码修复中三种 execution-free 验证公式（CLS、CWM、TRAJ），使用两个模型家族、两个复杂度级别和多种 seed，发现了三层结构：fine-tuning 必要 → function-level 近等价 → repo-level 因 complexity 分化。统计方法的严谨性（TOST、Bayesian ROPE、clustered bootstrap、Holm-Bonferroni）在 NLP 实证工作中罕见且值得肯定。然而 CLS-TRAJ 比较受制于多个混淆因素和极低统计检验力（power ~0.3），CWM baseline 的生态效度存疑（≤8B LoRA vs 原始 32B+execution-trace pretraining），削弱了论文核心\"三方比较\"叙事的说服力。\n\n### Must-Fix 问题\n\n**N1** [critical] CLS-TRAJ \"未确认等价\" 的结论在 power ~0.3 下被 over-stated\n- Abstract 说 \"TRAJ parity is not confirmed after multiple comparison correction at any scale tested\"。但 §3.4 明确报告 power ~0.3（Cohen, 1988），即存在 70% 的 Type II 错误概率。\n- TOST p=0.025（pre-Holm）本身是 nominally significant 的\n- Holm 校正后 p=0.075 仅 borderline\n- 14B 时差距收敛到 1.07pp 且 TOST 确认等价（p=0.043）\n- Abstract 和 Conclusion 中 \"not confirmed\" 的措辞可能让读者误以为存在差异的证据\n- 建议：Abstract 应加入 power 限定语；Conclusion 应明确讨论 power ~0.3 的含义；14B 结果应在 abstract 中给予更突出位置\n\n**N2** [critical] Appendix \"P: Limitations\" 可能违反 EMNLP 格式规则\n- EMNLP 2026 / ARR 规定 \"一篇文章只能有一个 limitations section，放在正文里面，appendix 不能有 limitations section\"\n- Appendix 概览明确将其列为独立条目 \"P: Limitations\"\n- 建议：将该段落重命名为 \"Extended Experimental Details\" 或 \"Additional Confound Analysis\"\n\n### Should-Fix 问题\n\n**W1** [warning] TRAJ 训练配置的非对称性在正文中讨论不足\n- TRAJ 的训练条件与 CLS/CWM 有根本差异：~400 vs ~70K 训练样本、不同 learning rate、variant-level labels vs per-test\n- Downsample ablation 控制了数据量但未控制 label granularity\n\n**W2** [warning] CWM baseline 生态效度不足\n- 原始 CWM 使用 32B + execution-trace mid-training\n- ≤8B LoRA CWM 可能未能捕捉使原始 CWM 有效的核心机制\n\n**W3** [warning] Repo-level seed coverage 稀疏\n- 某些配置只有 n=2 seeds，限制统计推断\n\n**W4** [warning] Checkpoint selection confound 的 ablation 覆盖不足\n- Checkpoint ablation 仅在 Qwen3-4B CLS 上进行\n- CWM early-stopped vs final-epoch 差距可达 ~18pp（DeepSeek-Coder）\n\n### Minor 问题\n\n**M1**: SESOI ±2pp 是否 pre-registered？\n**M2**: Figure 2 y-axis 非零基线\n**M3**: LPM vs GEE 在 model identity 显著性上不一致\n**M4**: 14B 仅 Qwen3 一个 family\n\n### Questions\n\n**Q1**: ±2pp SESOI 是在看到数据之前还是之后确定的？\n**Q2**: 需要多少 seeds 才能使 CLS-TRAJ 达到 power ≥0.8？\n**Q3**: CLS-CWM 使用 seed-level paired analysis 而 CLS-TRAJ 用 clustered bootstrap，是否引入方法论不对称？\n**Q4**: 是否可能构建 per-test labels for TRAJ 来消除 label granularity 混淆？\n**Q5**: 如果有 32B 实验数据，是否预期 repo-level 差异会消失？\n\n### 评分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3/5 |\n| Reproducibility | 4/5 |\n| Overall Assessment | 3/5 (Findings) |\n| Confidence | 4/5 |"
  }
}
```

</details>

---


### Tool result

_source line 1051 · 2026-05-23T12:47:27.711121+00:00_

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

_source line 1052 · 2026-05-23T12:47:30.058436+00:00_

交叉分享已发送给两位 Reviewer，等待回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 95

## Round 95

2 recorded events


### User

_source line 1053 · 2026-05-23T12:47:32.597326+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿要点总结：**

- **Overall: 3.0 (Findings)** — 统计方法论出色（TOST/ROPE/ICC/混合效应回归），但核心发现可从论文自身 §2.2 理论预测，新颖性有限
- **两个 Must-Fix 问题：** (1) 核心发现可预测性降低 Excitement；(2) TRAJ 比较因训练配置差异（~400 vs ~70K 实例）被严重混淆
- **五个 Should-Fix 问题：** 14B 证据不足、oracle 互补性不可操作、可能超页数限制、GenRM 领域对比未充分展开、PRM/ORM 映射反直觉
- **Related Work 覆盖充分**，未发现重大遗漏（CodeScaler、Aletheia、GenPRM 等均已引用）
- **Soundness 4/5, Excitement 3/5, Confidence 4/5**

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

_source line 1054 · 2026-05-23T12:47:37.364238+00:00_

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


## Round 96

## Round 96

2 recorded events


### User

_source line 1055 · 2026-05-23T12:49:13.785375+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: 核心发现可从 §2.2 理论预测，新颖性有限**

同意这是本文 Excitement 评分的主要制约因素。§2.2 明确预测了短输出→等价、长输出→格式崩溃的方向，而 §1 p.2 和 §5 Conclusion 也承认函数级结果"与 §2.2 的理论分析一致"。这使得两个核心结论（function-level 等价 + repo-level 崩溃）的 surprise value 降低。

但我认为 R2 略有过度概括：§2.2 的理论分析未能预测以下细节：(1) 14B 时三种 formulations 的收敛速度和幅度（1.07pp）；(2) failure mode taxonomy 中三类失败模式的具体分布和跨模型一致性（Table 4）；(3) CLS-TRAJ 在 function-level 的近等价（§2.2 没有对 TRAJ 做具体预测）。这些 quantitative boundary conditions 超越了纯理论预测范围。

R2 的建议(b)——"深入分析理论预测 WHERE 失败"——是改进新颖性定位的好方向。

**[AGREE] R2-N2: TRAJ 比较被训练配置严重混淆**

完全同意。这与我的 W1 一致。TRAJ 的 ~400 vs ~70K 训练实例、不同 learning rate（2×10⁻⁴ vs 5×10⁻⁵）、variant-level labels 使得三方比较不受控。虽然 Appendix B 的 downsample ablation（CLS 80.74% vs TRAJ 72.92%）部分地址了数据量差异，但未控制 label granularity（per-test vs variant-level）。

补充我的观察：主文 Tables 1-3 将三种 formulations 并列呈现时，没有视觉标注 TRAJ 配置差异（如脚注或 † 标记），读者很容易默认三者在匹配条件下比较。建议至少在表格中添加标注。

---

### Should-Fix

**[AGREE] R2-W1: 14B "容量依赖收敛" claim 证据不足**

同意。我的 M4 也指出 14B 仅有 Qwen3 一个 model family 且 seed 数减少到 3，缺乏跨模型验证。Abstract 中 "At 14B (3 seeds), all three formulations narrow to within 1.07pp, consistent with capacity-dependent resolution" 的措辞暗示了一个 general trend，但证据仅来自单一模型家族。应降级为 preliminary observation 并加强 hedging。

**[REBUT] R2-W2: Oracle 互补性作为贡献存在误导**

部分不同意。R2 认为 <0.4pp 的启发式收益使互补性分析不可操作。但论文 Abstract 已将此定位为 "motivate future work on complexity-aware formulation routing"，Contribution 2（§1 p.2）的措辞是 "error complementarity... provides the strongest practical argument for exploring formulation-level tradeoffs"——这是 motivation 而非 solution。

更重要的是，互补性分析的价值不仅在于可操作性：Table 4 和 Appendix H-I 的定性错误分析揭示了 CLS 和 CWM 的错误模式是结构性不同的（CLS: decision collapse + aggregation penalty; CWM: formal collapse），这一诊断发现本身就具有独立价值。<0.4pp 的启发式收益恰恰说明简单方法不够，需要更 sophisticated 的路由策略——这是一个有意义的 negative result。

不过我同意 R2 的建议——论文应更明确地将此框定为 negative result + motivation，而非一项独立的正面贡献。

**[REBUT] R2-W3: 正文可能超过 8 页限制**

不同意。我仔细检查了 PDF（p.8-9 边界）和 LaTeX 源码。Section 5 Conclusion 和 Limitations 均位于 p.8 之内。p.9 从参考文献开始。具体证据：

1. LaTeX 源码结构：`conclusion.tex` 包含 `\section{Conclusion}` + 一段主要文字 + "Three directions follow:" + `\section*{Limitations}` + 一段简短文字，共约 17-19 行
2. PDF p.8 图像显示：Limitations 文字 "Primary findings use ≤8B LoRA fine-tuning..." 在页面底部可见
3. PDF p.9 图像显示：页面从参考文献条目开始（Abdullahi et al., ...）

此外，Limitations 按 EMNLP 2026 规则不计入 8 页限制。即使 Limitations 跨越了页面边界（从 PDF 看并非如此），也不构成超页问题。

R2 可能误将 Limitations 段落的尾部（仍在 p.8 上）误判为 Conclusion 延续到 p.9。建议 R2 重新检查 PDF p.8 底部的节标题。

**[AGREE] R2-W4: GenRM 领域特异性对比分析不充分**

同意。代码验证中生成式 ≤ 判别式（与 GenRM 在数学推理中的发现相反）是论文最具独特性的观察之一，但 §4 和 §5 仅给了约 2 句话。论文已有支撑深入分析的数据：

- CWM 的 format compliance rate（parseable rate 从 function 的 ~100% 降到 repo 的 38-43%，Table 4）可解释为什么 generation advantage 在代码中失效——代码输出的结构化格式要求远高于数学推理的自然语言答案
- CLS 的 inference efficiency（§3.6 分析，单 token 输出 vs ~477 token 平均输出）是代码特有的约束

增加 1-2 段分析不仅提升新颖性，还能回应 R2-N1 关于 confirmation vs discovery 的批评。

**[AGREE] R2-W5: PRM/ORM 映射可能令读者困惑**

同意。§4 中 "CLS corresponds to process-level (PRM-like) verification while TRAJ provides outcome-level (ORM-like) feedback" 的映射需要更显式的解释。关键区分是粒度（per-test vs per-patch），而非方法类别（classification vs generation）。一句澄清即可解决：例如 "CLS provides per-test signals analogous to per-step PRM scoring, while TRAJ collapses all test information into a single patch verdict analogous to ORM."

---

### Minor

**[AGREE] R2-M1**: Abstract 确实统计符号过密。但我注意到 abstract 约 189 words（未超 200 word 限制），已相当紧凑。在不增加篇幅的前提下，可考虑将 z=−23.7 等具体数值移入正文。

**[AGREE] R2-M2**: 与我的 M2 一致。Figure 2 y-axis 非零起始。

**[AGREE] R2-M3**: 16 个附录确实量大。但考虑到论文的 methodological rigor 要求（equivalence testing 的 sensitivity analysis、Bayesian robustness check、confound quantification），大量附录是必要的。核心问题不是附录太多，而是某些关键分析（如 TOST sensitivity, Bayesian ROPE）是否应在正文中给予更多篇幅。

**[REBUT] R2-M4**: 不完全同意三项贡献应合并。失败模式分类法（Contribution 3）确实支撑主发现，但它的诊断框架（formal collapse / decision collapse / aggregation penalty）可独立于三方比较使用——从业者即使不关心 formulation 选择问题，也可用此分类法诊断已部署验证器的错误模式。Table 4 的结构和 Appendix H-I 的定性分析提供了可迁移的分析工具。但我同意 Contribution 2（错误互补性）与 Contribution 1 的独立性较弱。

---

### Questions

R2 的五个问题（Q1-Q5）均合理且重要。特别是：

- **Q2**（TRAJ 使用 ~70K 训练实例的结果）与我的 W1 和 R2-N2 一致，是评估 TRAJ 比较有效性的关键实验。
- **Q3**（代码 vs 数学领域差异原因）与 R2-W4 一致，深入回答此问题可显著提升论文新颖性。
- **Q5**（14B cross-family 复制）与我的 M4 和 R2-W1 一致。

---

### 总体评估对比

R2 给出 Overall 3.0 (Findings)，与我的评分一致。我们的核心分歧在于：

1. **W3 页数问题**：R2 认为可能超页，我认为 PDF 证据显示未超页
2. **W2 互补性贡献**：R2 认为误导，我认为作为 negative result + motivation 有价值
3. **M4 贡献独立性**：R2 认为三项贡献应合并，我认为 failure mode taxonomy 有独立价值

我们一致认为的核心问题：
- TRAJ 训练配置混淆（R2-N2 = 我的 W1）
- 14B 结论证据不足（R2-W1 = 我的 M4）
- GenRM 对比分析不充分（R2-W4）
- 新颖性受限于 confirmation nature（R2-N1）——我原本未将此列为独立问题，但认可 R2 的分析


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

_source line 1056 · 2026-05-23T12:49:18.560204+00:00_

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


## Round 97

## Round 97

2 recorded events


### User

_source line 1057 · 2026-05-23T12:49:21.055756+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。核心共识：TRAJ 训练配置混淆（R2-N2）、14B 证据不足（R2-W1）、新颖性受限（R2-N1）。主要分歧：页数合规（我认为未超页）、互补性贡献定位（我认为作为 negative result 有价值）、failure mode taxonomy 独立性。

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

_source line 1058 · 2026-05-23T12:49:24.975149+00:00_

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


## Round 98

## Round 98

10 recorded events


### User

_source line 1059 · 2026-05-23T12:49:35.500586+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: CLS-TRAJ "未确认等价" 在 power ~0.3 下被 over-stated**

同意。这是一个精确的统计方法论问题。Abstract 的 "TRAJ parity is not confirmed after multiple comparison correction at any scale tested" 在 power ~0.3 下确实具有误导性——读者可能将 "not confirmed" 解读为 "evidence of difference"，而实际情况是 "insufficient power to detect equivalence"。

补充我的发现：
- 我在审稿中也注意到 14B 结论（"all three formulations narrow to within 1.07pp"）被 Abstract 作为 headline claim 但仅有 df=2 的 TOST，论文自身也承认 "lacks power to confirm"（§5）。R1 的 power 分析使这个问题更加尖锐。
- R1 提出的修改建议合理：Abstract 应加入 power 限定语，14B 结果应给予更突出位置以平衡 "not confirmed" 的消极暗示。
- 然而，我认为此问题的 severity 应为 **Should-Fix 而非 Must-Fix**。论文主文 §3.4 确实报告了 power ~0.3 并引用了 Cohen (1988)，这是诚实的报告。问题在于 Abstract/Conclusion 的措辞不够精确，而非方法论本身有缺陷。修改措辞即可解决。

**[AGREE] R1-N2: Appendix "P: Limitations" 可能违反 EMNLP 格式规则**

同意。EMNLP 2026 / ARR 明确规定 "一篇文章只能有一个 limitations section，放在正文里面，appendix 不能有 limitations section"。主文 p.9 已有 Limitations section，若 Appendix P 也标题为 "Limitations"，这是格式违规。

补充：我在审稿中发现了另一个相关格式问题（我的 W3）——Section 5 Conclusion 的文本从 p.8 底部溢出到 p.9 顶部（约 5-8 行），在 Limitations 标题之前。这意味着正文可能超过 8 页限制。R1 未提及此问题，但与 N2 一起构成格式合规方面的两个独立问题。

R1 的修改建议（重命名为 "Extended Experimental Details" 或 "Additional Confound Analysis"）简单可行，完全同意。

---

### Should-Fix 问题

**[AGREE] R1-W1: TRAJ 训练配置非对称性在正文讨论不足**

完全同意。这与我审稿中的 N2（我将其列为 critical）高度一致。R1 额外指出了一个我未明确提及的细节：downsample ablation 控制了数据量但未控制 label granularity（TRAJ 使用 variant-level labels vs CLS/CWM 的 per-test labels）。这进一步削弱了 TRAJ 对比的可控性。

**[AGREE with nuance] R1-W2: CWM baseline 生态效度不足**

部分同意。R1 的论点成立：原始 CWM 使用 32B + execution-trace mid-training，≤8B LoRA CWM 可能未能捕捉使其有效的核心机制。这意味着仓库级 CWM 崩溃可能是规模不足的产物，而非公式本身的根本限制。

但我认为论文在两个方面部分回应了这一担忧：
1. §3.7 Threats to Validity 明确讨论了此问题，将结论限定在 "≤8B LoRA protocol" 范围内
2. §5 Conclusion 将 "capacity scaling at 32B+" 列为 Future Direction (2)
3. 论文的贡献定位是 "matched comparison at controlled scale"，而非 "CWM is fundamentally inferior"

因此 R1-W2 是对 **external validity** 的合理担忧，但不构成对论文内部一致性的质疑。我建议 severity 维持 Should-Fix，但论文应在 §3.7 中更显式地讨论 "≤8B CWM 是否代表 CWM 公式的 fair representation" 这一问题。

**[AGREE] R1-W3: Repo-level seed coverage 稀疏 (n=2 for some configs)**

同意。我在审稿中也关注了仓库级复制不足的问题（我的 W1 涉及 14B 仅 3 seeds）。n=2 seeds 使统计推断几乎不可能，应在论文中更显著地标注哪些配置具有此局限。

**[AGREE] R1-W4: Checkpoint selection confound 的 ablation 覆盖不足**

同意。这是我未充分关注的一个有价值的观察。如果 CWM early-stopped vs final-epoch 差距可达 ~18pp（DeepSeek-Coder），那么 checkpoint selection 是一个巨大的混淆因素。仅在 Qwen3-4B CLS 上做 ablation 不足以覆盖这一变异性。至少应对 CWM 和 DeepSeek-Coder 进行对应 ablation。

---

### Minor 问题

**[AGREE] R1-M1: SESOI ±2pp 是否 pre-registered**

同意这是一个合理的方法论问题。Appendix J 的 TOST margin sensitivity 分析（结果在 ±1.52pp 下仍 hold）部分缓解了对 researcher degrees of freedom 的担忧，但明确声明 pre-registration 状态会更好。

**[AGREE] R1-M2: Figure 2 y-axis 非零基线**

同意，我也独立指出了这一点（我的 M2）。

**[AGREE] R1-M3: LPM vs GEE 在 model identity 显著性上不一致**

同意。如果两种统计模型给出不同的显著性结论，论文应讨论哪个更可靠（考虑数据结构和假设），或将结论限定为 "estimator-dependent"。Appendix M 可能已有部分讨论，但主文应提及这一不一致性。

**[AGREE] R1-M4: 14B 仅 Qwen3 一个 family**

同意，与我的 W1 一致。

---

### Questions 回应

**R1-Q1 (SESOI pre-registration)**: 同意这是关键问题。如果 ±2pp 是在看到数据后选择的，等价性结论的可信度会降低。

**R1-Q2 (CLS-TRAJ power ≥0.8 需要多少 seeds)**: 非常好的问题。根据 power ~0.3 at k=5 seeds，要达到 power ≥0.8 可能需要 ~15-20 seeds，这在计算上是昂贵的但对论文结论很重要。

**R1-Q3 (CLS-CWM 用 seed-level paired vs CLS-TRAJ 用 clustered bootstrap 的方法论不对称)**: 这是我未注意到的一个敏锐观察。如果不同比较使用不同统计方法，引入了 methodological asymmetry，可能使某些比较更容易达到显著性。论文应解释选择不同方法的理由，或对所有比较使用统一方法。

**R1-Q4 (TRAJ per-test labels)**: 有价值的工程建议，但可能从根本上改变 TRAJ 公式的定义（TRAJ 的核心特征就是不做 per-test 分解）。

**R1-Q5 (32B 预测)**: 我的 Q1 提出了相同问题。

---

### 评分比较与调整

| 维度 | R1 | R2（原始） | R2（调整后） | 说明 |
|------|-----|-----------|------------|------|
| Soundness | 3.5/5 | 4/5 | 4/5 | R1 的 power 分析（N1）和 checkpoint ablation（W4）是有效的扣分点，但论文的 CLS-CWM 核心比较仍然well-supported。我维持 4 但承认 3.5 也合理。 |
| Excitement | 3/5 | 3/5 | 3/5 | 一致。 |
| Overall | 3/5 | 3/5 | 3/5 | 一致。Findings 定位恰当。 |
| Confidence | 4/5 | 4/5 | 4/5 | 一致。 |

**总结：** R1 和 R2 在 Overall Assessment 上完全一致（3.0 Findings）。R1 在统计功效分析（N1: power ~0.3）和 checkpoint ablation（W4）方面提出了我未充分关注的有价值问题。我的独特贡献在于：(1) 新颖性维度的分析——核心发现可从 §2.2 理论预测（我的 N1）；(2) GenRM 领域特异性对比被浪费（我的 W4）；(3) 正文页数溢出问题（我的 W3）。两份审稿互补，共同支持 Findings 定位。

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

_source line 1060 · 2026-05-23T12:49:56.470733+00:00_

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

_source line 1061 · 2026-05-23T12:49:57.927275+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T12:31:11.979723+00:00\", \"completed_at\": \"2026-05-23T12:34:34.842530+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续两页纯文本无任何 display item。第一个视觉锚点（Figure 1）直到 page 3 才出现。审稿人在前 2 页无法获得视觉锚定，可能影响第一印象。建议考虑将 Figure 1 提前到 page 2 或在 page 1 右栏放一个精简版概念图\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"整页纯文本（Related Work + Conclusion 开头），与 page 7 仅有一个小型 Table 4 相连。Related Work 本身是文字密集段落，结构上可接受，但从审稿人体验看 pp.7-8 区域视觉单调\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2（scaling plot）右栏放置，图内文字标签（axis labels、legend）偏小，但在 150 dpi 渲染下仍可辨读。建议适当增大 tick label 字号至 ≥9pt\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 概念图使用了彩色编码区分三种 formulation，整体清晰。caption 自包含程度好，无需回看正文即可理解\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 使用 booktabs 风格，最优值加粗，小数精度一致（1 位），格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 booktabs 风格，bolding 标注最优值，含 Mean 和 Δ 列，排版清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 3 出现在页面顶部，booktabs 风格，多模型多 formulation 对比，格式一致\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 4（failure mode taxonomy）紧凑，三列布局清晰，与正文讨论位置匹配\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 3（appendix，oracle advantage bar chart）清晰可读，颜色区分度足够，caption 自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Tables 8/9/10 三个表格密集排列在同一页，略显拥挤但无溢出\"}, {\"severity\": \"info\", \"dimension\": \"page 23\", \"message\": \"最末页（appendix 末页）内容仅占约 1/4，大面积空白。因为是 appendix 最后一页，不影响审稿印象\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落简短（约 5 行），覆盖 3 个关键限制点，符合 EMNLP 规范\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"References 格式统一，未发现 [?] 未解析引用，无明显 overfull hbox\"
…[truncated 336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-23T12:49:58.078272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "limit": "10"
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
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-23T12:49:58.180058+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-23T12:54:24.006627+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "\n# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13 R1 再次提及但无新增要求。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → final epoch). 但 R7 的 CLS epoch ablation (<1pp) 仍有效。新角度：CWM NaN val loss 可能是 formulation-inherent。\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。但 R2 REBUT：Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp。Director 裁定：证据表明 checkpoint 差异无法解释 18-26pp gap，降为 Should-Fix。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-N2 升级为 critical：论文持有 Qwen3 CWM step 300-400 optimal checkpoints 但未评估其 repo-level accuracy。R2 完全 AGREE。\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W4 re-raises：checkpoint ablation 仅在 Qwen3-4B CLS 上进行，未覆盖受影响最严重的 CWM 配置。DeepSeek CWM early-stop vs final-epoch ~18pp。R2 AGREE。Director：resolved status maintained——step-400 eval 数据已证明 early checkpoint ≤ final epoch，format collapse 从训练早期即存在。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因（formulation-inherent vs implementation issue）\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文更显著讨论 checkpoint 缓解证据\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy 并报告结果\"\n      assigned_to: \"experiment\"\n      status: wont_fix\n    - round: 12\n      action: \"Appendix cwm_convergence 补充说明 step-level checkpoint 不可做的原因\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Step 300-400 checkpoints 未保存，但已找到现有 step-400 eval 数据（s42: 64.36% accuracy, 63.7% unparseable）。早期 checkpoint ≤ final epoch，直接反驳 'optimal early checkpoint closes gap' 假设。Format collapse 从训练早期即存在。数据写入 Appendix cwm_convergence。\"\n  resolution_round: 12\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1: 'design space' framing 过度. R1 部分同意.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1 再次标 CRITICAL。R1 AGREE 但认为 failure mode taxonomy 有独立贡献。两人共识：Findings 合适，Main 不够。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. R2 STILL_OPEN. R1 AGREE on assessment but argues exceptional soundness partially compensates. Both accept 3.0-3.5 range. Director: inherent limitation, wont_fix.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R2-N1 标 CRITICAL (Excitement 2/5)。R1 REBUT。最终分歧：R1 Excitement 3/5, R2 Excitement 2/5。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N1 再次标 CRITICAL：核心发现可从 §2.2 理论预测，属 confirmation 而非 discovery。R1 AGREE 但补充 quantitative boundary conditions（14B convergence, failure mode distribution）超越纯理论预测。两人 Excitement 均为 3/5。Director：inherent limitation，wont_fix 维持。\"\n  resolution: \"所有可行 action items 已完成。Excitement 稳定在 3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。Novelty ceiling 为 inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"SESOI 基于训练噪声量级独立于 observed gap.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。缺 domain-specific justification.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W4 re-raises：±2pp 依赖于 accuracy range 和 test set size。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-W1 re-raises：无 pre-registration，±1.52pp 临界值距 ±2pp 仅 0.48pp。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-M1 和 R1-Q1 再次提及 pre-registration 状态。R2 AGREE。§3.4 已改为 'motivated by domain considerations but was not pre-registered'，引用 sensitivity analysis。Director: resolved——已诚实披露，无进一步修改空间。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；引用了 sensitivity analysis (Table tost_sensitivity)；明确承认结论对 margin 选择敏感。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入限定。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W6: 175× 数据量差异.\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：180× 差异 + signal granularity。R2 AGREE。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-W4 re-raises：downsample 控制了 volume 但未控制 label granularity。R2 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N2 标 CRITICAL：TRAJ 使用 ~400 vs ~70K 实例 + 不同 lr + variant-level labels，三方比较不受控。R1 完全 AGREE，补充：主文 Tables 1-3 无视觉标注 TRAJ 差异。Director 裁定：§3.5 已有 'exploratory' 标注和 confound 讨论，resolved 维持。但报告记录此为 persistent concern。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"Contribution summary 中明确表述 CLS-TRAJ repo-level 比较包含 training regime confound\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 标注 'The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity, a formulation-inherent confound.' R13 再次提出但无新增可行动修改。\"\n  resolution_round: 12\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"CodeRM, CodeScaler, GenPRM 等均已加入 Related Work。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"bar labels 偏小.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-M2: y-axis 不从零开始（55%），视觉夸大 gap。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED.\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-M2 和 R2-M2 均再次提及 y-axis 非零基线。Director：resolved——caption 已标注 'y-axis does not start at zero'，对 0-3pp 差异合理。\"\n  resolution: \"Figure 2 caption 标注 'y-axis does not start at zero'，两位 Reviewer 一致确认合理。\"\n  resolution_round: 11\n\n# === Round 8 Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-N3 re-raises.\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-N1 再次标 CRITICAL：Abstract 'not confirmed' 在 power ~0.3 下 over-stated。R2 AGREE but 认为 Should-Fix（措辞问题非方法论缺陷）。Director 裁定 Should-Fix：§3.4 已诚实报告 power，问题在 Abstract/Conclusion 措辞。\"\n  action_items:\n    - round: 9\n      action: \"Variant-level 分析明确标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文讨论 TOST 功效限制；Bayesian ROPE 补充\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"正文讨论 power ~0.3 意味着 '未确认' 不应解读为 '非等价'\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.4 已扩写 power paragraph，14B TOST 完成。Contribution 措辞保守。R13 再次提出 Abstract 措辞问题，见 R13-W1。\"\n  resolution_round: 12\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Cross-seed oracle 已加入正文。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Appendix 已讨论。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM / RepoExec\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-W2 re-raises CWM 生态效度。R2 partially AGREE but notes §3.7 和 §5 已有 ≤8B 限定。Director: resolved——≤8B qualifier 已充分覆盖 Abstract/Conclusion/Threats.\"\n  resolution: \"合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. 两人 Excitement 均为 3/5，Overall 均为 3.0 (Findings)。合并至 R6-N4 追踪。\"\n  resolution: \"合并至 R6-N4。Inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Both RESOLVED. GEE logistic regression added.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-M3 提及 LPM vs GEE 在 model identity 显著性上不一致（p=0.002 vs p=0.449）。论文已在 Appendix M 讨论 cluster 数限制。Director: resolved——Appendix M 已明确标注 estimator-dependent。\"\n  resolution: \"Appendix M 补充 GEE logistic regression + estimator-dependent 标注。\"\n  resolution_round: 11\n\n# === Round 9 Issues ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大 gap。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却声称 'model-dependent'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Abstract 改为更审慎措辞。\"\n  resolution_round: 10\n\n- id: \"R9-M1\"\n  summary: \"Figure 3 y-axis 不从 0 开始但未标注\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Caption 标注。合并至 R6-M3。\"\n  resolution_round: 11\n\n- id: \"R9-M2\"\n  summary: \"Abstract 第一句过于绝对\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"已改为 'increasingly leverages'。\"\n  resolution_round: 10\n\n- id: \"R9-M3\"\n  summary: \"缺少方法论引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"两篇已引用。\"\n  resolution_round: 10\n\n- id: \"R9-M4\"\n  summary: \"Clustered bootstrap 实施细节\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§3.1 已说明。\"\n  resolution_round: 10\n\n- id: \"R9-M5\"\n  summary: \"Repo-level DEFF=114.3 → effective n≈86\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§5.2 加入 TOST power 段落。\"\n  resolution_round: 10\n\n# === Round 10 Issues ===\n\n- id: \"R10-W1\"\n  summary: \"Python-only 评估未在 Limitations 提及\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"Limitations 加入 Python-only 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-W2\"\n  summary: \"'formulation choice is governed by code complexity' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"'governed by' 改为 'moderated by'。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"3-shot ICL collapse 未充分讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"§5.4 扩展。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"Appendix 导航不便\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"Mini TOC 加入。\"\n  resolution_round: 10\n\n# === Round 11 Issues ===\n\n- id: \"R11-M1\"\n  summary: \"Figure 2 中 14B 数据点视觉等权\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Figure 2 已更新。\"\n  resolution_round: 11\n\n- id: \"R11-M2\"\n  summary: \"§3.5 LPM model identity vs GEE 需 qualifier\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Commit 0b38a2b 修复。\"\n  resolution_round: 11\n\n- id: \"R11-M3\"\n  summary: \"Abstract 'motivate routing' 暗示过度\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Abstract 已改含负结果量化。\"\n  resolution_round: 11\n\n# === Round 12 Issues ===\n\n- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"两人独立提出。14B function-level gap 收敛至 0.43pp 支持 capacity-driven 假设。\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W2 再次提及 CWM 生态效度。R2 partially AGREE but notes 论文已有充分 qualifier (§3.7, §5, Abstract). Director: resolved——所有 qualifier 已到位。\"\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。\"\n  resolution_round: 12\n\n- id: \"R12-N2\"\n  summary: \"Qwen3 CWM optimal checkpoint 未评估\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Step-400 eval 数据已找到（64.36% accuracy, 63.7% unparseable），反驳 'optimal early checkpoint closes gap' 假设。\"\n  resolution_round: 12\n\n- id: \"R12-N3\"\n  summary: \"CLS-TRAJ 等价性不对称结论可能是 power ~0.3 artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 提出，R2 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-N1 再次以更强力度提出：Abstract 'not confirmed' 在 power ~0.3 下 misleading。R2 AGREE (Should-Fix). Director: §3.4 power paragraph 已有充分披露，问题仅在 Abstract/Conclusion 措辞。见 R13-W1。\"\n  resolution: \"§3.4 power paragraph 扩写，14B TOST 完成。R13 提出 Abstract 措辞微调需求，见 R13-W1。\"\n  resolution_round: 12\n\n- id: \"R12-W1\"\n  summary: \"Failure mode taxonomy 未列为独立贡献\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"§1 增加第三条贡献。\"\n  resolution_round: 12\n\n- id: \"R12-W2\"\n  summary: \"GenRM 对比发现未充分讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-W4 再次标 Should-Fix：Conclusion 仅 1 句话讨论 GenRM domain specificity，未分析 WHY。R1 AGREE 并建议用论文已有数据（parseable rate, inference efficiency）支撑分析。Director：Conclusion 段落已存在但确实过于简短。见 R13-W4。\"\n  resolution: \"Conclusion 新增 GenRM domain-specificity 段落。R13 认为仍不够深入，见 R13-W4。\"\n  resolution_round: 12\n\n- id: \"R12-W3\"\n  summary: \"Preprocessing-checkpoint confound chain\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"§3.7 已加入 confound chain 描述。\"\n  resolution_round: 12\n\n- id: \"R12-W4\"\n  summary: \"CLS-CWM cross-seed pairing 局限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"§3.7 已加入 cross-seed pairing limitation。\"\n  resolution_round: 12\n\n- id: \"R12-M1\"\n  summary: \"§2.2 Failure Modes 位于 method section\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"标题改为 'Expected Failure Modes'。\"\n  resolution_round: 12\n\n- id: \"R12-M2\"\n  summary: \"Appendix G' 命名不直观\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"改为 G.1 subsection。\"\n  resolution_round: 12\n\n- id: \"R12-M3\"\n  summary: \"wei2022emergent 引用类型不一致\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"@inproceedings → @article。\"\n  resolution_round: 12\n\n- id: \"R12-M4\"\n  summary: \"Figure 2 float 漂移\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Figure 2 移入 experiments.tex。\"\n  resolution_round: 12\n\n# === Prior Round Issues ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n# === Round 13 (Fresh Review) New Issues ===\n\n- id: \"R13-N1\"\n  summary: \"Appendix 'P: Limitations' 标题可能违反 EMNLP 格式规则（一篇文章只能有一个 limitations section）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 提出，R2 完全 AGREE。EMNLP 2026 / ARR 规定 appendix 不能有 limitations section。Appendix 概览列出 'P: Limitations'，构成形式违规。\"\n  action_items:\n    - round: 13\n      action: \"将 Appendix P 'Extended limitations' 重命名为 'Extended Experimental Details' 或 'Additional Confound Analysis'，并从 Appendix 概览中移除 'P: Limitations' 标签\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-W1\"\n  summary: \"Abstract/Conclusion 中 TRAJ 'not confirmed' 措辞在 power ~0.3 下 over-stated——应加 power 限定语\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1 提出（标 Must-Fix），R2 AGREE 但认为 Should-Fix（§3.4 已诚实报告）。Director 裁定 Should-Fix。Abstract 'TRAJ parity is not confirmed after multiple comparison correction at any scale tested' 在 power ~0.3 下可能让读者误解为存在差异的证据。14B 收敛结果（1.07pp）应给予更突出位置。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 加入 power 限定语，如 'under current sample size (power ~0.3), TRAJ equivalence cannot be confirmed but cannot be ruled out'; 14B 收敛结果给予更突出位置\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 13\n      action: \"Conclusion 明确讨论达到 power ≥0.8 所需的 seed 数量（约 n_eff≈350）\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-W2\"\n  summary: \"Oracle 互补性应重新框定为 negative result + motivation，而非独立正面贡献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 partial REBUT（作为 negative result 有价值，互补性分析的诊断价值独立于可操作性）。Director 裁定 Should-Fix：论文应更明确框定为 negative result + motivation。\"\n  action_items:\n    - round: 13\n      action: \"Contribution 2 措辞调整：从 'strongest practical argument for exploring' 改为明确承认 simple routing 不可行，互补性作为 motivation for future learned routers\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-W3\"\n  summary: \"14B 'capacity-dependent convergence' claim 证据不足——仅 1 model family, 3 seeds, Holm adj p=0.050\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1 提出，R1 AGREE (M4)。14B 仅 Qwen3，TOST df=2 功效不足，Holm adj p=0.050 borderline。无 32B+ 实验。应降级为 preliminary observation 而非 stated finding。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 和 Conclusion 中 14B 结论加入更强 hedging，标注为 preliminary observation 而非 confirmed finding\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-W4\"\n  summary: \"GenRM 领域特异性对比（代码中 generation ≤ discrimination，与数学相反）分析不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4 提出，R1 AGREE。§5 Conclusion 仅 1 句话讨论。论文已有支撑数据（parseable rate 差异、output token count、CWM format compliance rate）可用于分析 WHY 领域差异存在。增加 1-2 段可同时提升 Excitement（回应 R2-N1）。\"\n  action_items:\n    - round: 13\n      action: \"§5 Discussion/Conclusion 新增 1-2 段分析代码 vs 数学验证的结构性差异，提出可检验假设（output structure, format compliance, error type distribution）\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-M1\"\n  summary: \"PRM/ORM 映射命名反直觉——CLS 听起来像 ORM 而非 PRM\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 AGREE。§4 中 CLS→PRM-like 和 TRAJ→ORM-like 的映射基于 per-test vs per-patch 粒度是正确的，但命名反直觉。建议加一句显式澄清。\"\n  action_items:\n    - round: 13\n      action: \"§4 Related Work 加一句澄清：per-test granularity 对应 per-step PRM，per-patch verdict 对应 outcome-level ORM\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-M2\"\n  summary: \"Abstract 统计符号过密（z=−23.7, TOST, pp 值），降低可读性\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M1 提出，R1 AGREE。建议先陈述定性洞见，再给统计支撑。但 Abstract 已 ~189 words（≤200 word 限制），调整空间有限。\"\n  action_items:\n    - round: 13\n      action: \"考虑将部分统计数值（如 z=−23.7）从 Abstract 移入正文\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-M3\"\n  summary: \"三项贡献独立性值得商榷——互补性和 taxonomy 是主发现的辅助分析\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M4 提出，R1 partial REBUT：failure mode taxonomy (Table 4) 具有可迁移的诊断价值，可独立于三方比较使用。R1 同意 Contribution 2（互补性）与 Contribution 1 独立性较弱。Director：Minor——taxonomy 独立性成立，但 contribution list 可微调。\"\n"
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
    "issues_yaml": "\n# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13 R1 再次提及但无新增要求。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → final epoch). 但 R7 的 CLS epoch ablation (<1pp) 仍有效。新角度：CWM NaN val loss 可能是 formulation-inherent。\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。但 R2 REBUT：Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp。Director 裁定：证据表明 checkpoint 差异无法解释 18-26pp gap，降为 Should-Fix。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-N2 升级为 critical：论文持有 Qwen3 CWM step 300-400 optimal checkpoints 但未评估其 repo-level accuracy。R2 完全 AGREE。\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W4 re-raises：checkpoint ablation 仅在 Qwen3-4B CLS 上进行，未覆盖受影响最严重的 CWM 配置。DeepSeek CWM early-stop vs final-epoch ~18pp。R2 AGREE。Director：resolved status maintained——step-400 eval 数据已证明 early checkpoint ≤ final epoch，format collapse 从训练早期即存在。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因（formulation-inherent vs implementation issue）\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文更显著讨论 checkpoint 缓解证据\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy 并报告结果\"\n      assigned_to: \"experiment\"\n      status: wont_fix\n    - round: 12\n      action: \"Appendix cwm_convergence 补充说明 step-level checkpoint 不可做的原因\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Step 300-400 checkpoints 未保存，但已找到现有 step-400 eval 数据（s42: 64.36% accuracy, 63.7% unparseable）。早期 checkpoint ≤ final epoch，直接反驳 'optimal early checkpoint closes gap' 假设。Format collapse 从训练早期即存在。数据写入 Appendix cwm_convergence。\"\n  resolution_round: 12\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1: 'design space' framing 过度. R1 部分同意.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1 再次标 CRITICAL。R1 AGREE 但认为 failure mode taxonomy 有独立贡献。两人共识：Findings 合适，Main 不够。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. R2 STILL_OPEN. R1 AGREE on assessment but argues exceptional soundness partially compensates. Both accept 3.0-3.5 range. Director: inherent limitation, wont_fix.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R2-N1 标 CRITICAL (Excitement 2/5)。R1 REBUT。最终分歧：R1 Excitement 3/5, R2 Excitement 2/5。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N1 再次标 CRITICAL：核心发现可从 §2.2 理论预测，属 confirmation 而非 discovery。R1 AGREE 但补充 quantitative boundary conditions（14B convergence, failure mode distribution）超越纯理论预测。两人 Excitement 均为 3/5。Director：inherent limitation，wont_fix 维持。\"\n  resolution: \"所有可行 action items 已完成。Excitement 稳定在 3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。Novelty ceiling 为 inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"SESOI 基于训练噪声量级独立于 observed gap.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。缺 domain-specific justification.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W4 re-raises：±2pp 依赖于 accuracy range 和 test set size。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-W1 re-raises：无 pre-registration，±1.52pp 临界值距 ±2pp 仅 0.48pp。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-M1 和 R1-Q1 再次提及 pre-registration 状态。R2 AGREE。§3.4 已改为 'motivated by domain considerations but was not pre-registered'，引用 sensitivity analysis。Director: resolved——已诚实披露，无进一步修改空间。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；引用了 sensitivity analysis (Table tost_sensitivity)；明确承认结论对 margin 选择敏感。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"R10 commit a58c178: Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入限定。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W6: 175× 数据量差异.\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：180× 差异 + signal granularity。R2 AGREE。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-W4 re-raises：downsample 控制了 volume 但未控制 label granularity。R2 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N2 标 CRITICAL：TRAJ 使用 ~400 vs ~70K 实例 + 不同 lr + variant-level labels，三方比较不受控。R1 完全 AGREE，补充：主文 Tables 1-3 无视觉标注 TRAJ 差异。Director 裁定：§3.5 已有 'exploratory' 标注和 confound 讨论，resolved 维持。但报告记录此为 persistent concern。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"Contribution summary 中明确表述 CLS-TRAJ repo-level 比较包含 training regime confound\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 标注 'The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity, a formulation-inherent confound.' R13 再次提出但无新增可行动修改。\"\n  resolution_round: 12\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"CodeRM, CodeScaler, GenPRM 等均已加入 Related Work。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"bar labels 偏小.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-M2: y-axis 不从零开始（55%），视觉夸大 gap。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED.\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-M2 和 R2-M2 均再次提及 y-axis 非零基线。Director：resolved——caption 已标注 'y-axis does not start at zero'，对 0-3pp 差异合理。\"\n  resolution: \"Figure 2 caption 标注 'y-axis does not start at zero'，两位 Reviewer 一致确认合理。\"\n  resolution_round: 11\n\n# === Round 8 Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Fresh review R12. R1-N3 re-raises.\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-N1 再次标 CRITICAL：Abstract 'not confirmed' 在 power ~0.3 下 over-stated。R2 AGREE but 认为 Should-Fix（措辞问题非方法论缺陷）。Director 裁定 Should-Fix：§3.4 已诚实报告 power，问题在 Abstract/Conclusion 措辞。\"\n  action_items:\n    - round: 9\n      action: \"Variant-level 分析明确标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文讨论 TOST 功效限制；Bayesian ROPE 补充\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"正文讨论 power ~0.3 意味着 '未确认' 不应解读为 '非等价'\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.4 已扩写 power paragraph，14B TOST 完成。Contribution 措辞保守。R13 再次提出 Abstract 措辞问题，见 R13-W1。\"\n  resolution_round: 12\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Cross-seed oracle 已加入正文。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Appendix 已讨论。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM / RepoExec\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-W2 re-raises CWM 生态效度。R2 partially AGREE but notes §3.7 和 §5 已有 ≤8B 限定。Director: resolved——≤8B qualifier 已充分覆盖 Abstract/Conclusion/Threats.\"\n  resolution: \"合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. 两人 Excitement 均为 3/5，Overall 均为 3.0 (Findings)。合并至 R6-N4 追踪。\"\n  resolution: \"合并至 R6-N4。Inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Both RESOLVED. GEE logistic regression added.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-M3 提及 LPM vs GEE 在 model identity 显著性上不一致（p=0.002 vs p=0.449）。论文已在 Appendix M 讨论 cluster 数限制。Director: resolved——Appendix M 已明确标注 estimator-dependent。\"\n  resolution: \"Appendix M 补充 GEE logistic regression + estimator-dependent 标注。\"\n  resolution_round: 11\n\n# === Round 9 Issues ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大 gap。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却声称 'model-dependent'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Abstract 改为更审慎措辞。\"\n  resolution_round: 10\n\n- id: \"R9-M1\"\n  summary: \"Figure 3 y-axis 不从 0 开始但未标注\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Caption 标注。合并至 R6-M3。\"\n  resolution_round: 11\n\n- id: \"R9-M2\"\n  summary: \"Abstract 第一句过于绝对\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"已改为 'increasingly leverages'。\"\n  resolution_round: 10\n\n- id: \"R9-M3\"\n  summary: \"缺少方法论引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"两篇已引用。\"\n  resolution_round: 10\n\n- id: \"R9-M4\"\n  summary: \"Clustered bootstrap 实施细节\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§3.1 已说明。\"\n  resolution_round: 10\n\n- id: \"R9-M5\"\n  summary: \"Repo-level DEFF=114.3 → effective n≈86\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§5.2 加入 TOST power 段落。\"\n  resolution_round: 10\n\n# === Round 10 Issues ===\n\n- id: \"R10-W1\"\n  summary: \"Python-only 评估未在 Limitations 提及\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"Limitations 加入 Python-only 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-W2\"\n  summary: \"'formulation choice is governed by code complexity' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"'governed by' 改为 'moderated by'。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"3-shot ICL collapse 未充分讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"§5.4 扩展。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"Appendix 导航不便\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"Mini TOC 加入。\"\n  resolution_round: 10\n\n# === Round 11 Issues ===\n\n- id: \"R11-M1\"\n  summary: \"Figure 2 中 14B 数据点视觉等权\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Figure 2 已更新。\"\n  resolution_round: 11\n\n- id: \"R11-M2\"\n  summary: \"§3.5 LPM model identity vs GEE 需 qualifier\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Commit 0b38a2b 修复。\"\n  resolution_round: 11\n\n- id: \"R11-M3\"\n  summary: \"Abstract 'motivate routing' 暗示过度\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Abstract 已改含负结果量化。\"\n  resolution_round: 11\n\n# === Round 12 Issues ===\n\n- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"两人独立提出。14B function-level gap 收敛至 0.43pp 支持 capacity-driven 假设。\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W2 再次提及 CWM 生态效度。R2 partially AGREE but notes 论文已有充分 qualifier (§3.7, §5, Abstract). Director: resolved——所有 qualifier 已到位。\"\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。\"\n  resolution_round: 12\n\n- id: \"R12-N2\"\n  summary: \"Qwen3 CWM optimal checkpoint 未评估\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Step-400 eval 数据已找到（64.36% accuracy, 63.7% unparseable），反驳 'optimal early checkpoint closes gap' 假设。\"\n  resolution_round: 12\n\n- id: \"R12-N3\"\n  summary: \"CLS-TRAJ 等价性不对称结论可能是 power ~0.3 artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 提出，R2 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-N1 再次以更强力度提出：Abstract 'not confirmed' 在 power ~0.3 下 misleading。R2 AGREE (Should-Fix). Director: §3.4 power paragraph 已有充分披露，问题仅在 Abstract/Conclusion 措辞。见 R13-W1。\"\n  resolution: \"§3.4 power paragraph 扩写，14B TOST 完成。R13 提出 Abstract 措辞微调需求，见 R13-W1。\"\n  resolution_round: 12\n\n- id: \"R12-W1\"\n  summary: \"Failure mode taxonomy 未列为独立贡献\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"§1 增加第三条贡献。\"\n  resolution_round: 12\n\n- id: \"R12-W2\"\n  summary: \"GenRM 对比发现未充分讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-W4 再次标 Should-Fix：Conclusion 仅 1 句话讨论 GenRM domain specificity，未分析 WHY。R1 AGREE 并建议用论文已有数据（parseable rate, inference efficiency）支撑分析。Director：Conclusion 段落已存在但确实过于简短。见 R13-W4。\"\n  resolution: \"Conclusion 新增 GenRM domain-specificity 段落。R13 认为仍不够深入，见 R13-W4。\"\n  resolution_round: 12\n\n- id: \"R12-W3\"\n  summary: \"Preprocessing-checkpoint confound chain\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"§3.7 已加入 confound chain 描述。\"\n  resolution_round: 12\n\n- id: \"R12-W4\"\n  summary: \"CLS-CWM cross-seed pairing 局限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"§3.7 已加入 cross-seed pairing limitation。\"\n  resolution_round: 12\n\n- id: \"R12-M1\"\n  summary: \"§2.2 Failure Modes 位于 method section\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"标题改为 'Expected Failure Modes'。\"\n  resolution_round: 12\n\n- id: \"R12-M2\"\n  summary: \"Appendix G' 命名不直观\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"改为 G.1 subsection。\"\n  resolution_round: 12\n\n- id: \"R12-M3\"\n  summary: \"wei2022emergent 引用类型不一致\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"@inproceedings → @article。\"\n  resolution_round: 12\n\n- id: \"R12-M4\"\n  summary: \"Figure 2 float 漂移\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Figure 2 移入 experiments.tex。\"\n  resolution_round: 12\n\n# === Prior Round Issues ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n# === Round 13 (Fresh Review) New Issues ===\n\n- id: \"R13-N1\"\n  summary: \"Appendix 'P: Limitations' 标题可能违反 EMNLP 格式规则（一篇文章只能有一个 limitations section）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 提出，R2 完全 AGREE。EMNLP 2026 / ARR 规定 appendix 不能有 limitations section。Appendix 概览列出 'P: Limitations'，构成形式违规。\"\n  action_items:\n    - round: 13\n      action: \"将 Appendix P 'Extended limitations' 重命名为 'Extended Experimental Details' 或 'Additional Confound Analysis'，并从 Appendix 概览中移除 'P: Limitations' 标签\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-W1\"\n  summary: \"Abstract/Conclusion 中 TRAJ 'not confirmed' 措辞在 power ~0.3 下 over-stated——应加 power 限定语\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1 提出（标 Must-Fix），R2 AGREE 但认为 Should-Fix（§3.4 已诚实报告）。Director 裁定 Should-Fix。Abstract 'TRAJ parity is not confirmed after multiple comparison correction at any scale tested' 在 power ~0.3 下可能让读者误解为存在差异的证据。14B 收敛结果（1.07pp）应给予更突出位置。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 加入 power 限定语，如 'under current sample size (power ~0.3), TRAJ equivalence cannot be confirmed but cannot be ruled out'; 14B 收敛结果给予更突出位置\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 13\n      action: \"Conclusion 明确讨论达到 power ≥0.8 所需的 seed 数量（约 n_eff≈350）\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-W2\"\n  summary: \"Oracle 互补性应重新框定为 negative result + motivation，而非独立正面贡献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 partial REBUT（作为 negative result 有价值，互补性分析的诊断价值独立于可操作性）。Director 裁定 Should-Fix：论文应更明确框定为 negative result + motivation。\"\n  action_items:\n    - round: 13\n      action: \"Contribution 2 措辞调整：从 'strongest practical argument for exploring' 改为明确承认 simple routing 不可行，互补性作为 motivation for future learned routers\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-W3\"\n  summary: \"14B 'capacity-dependent convergence' claim 证据不足——仅 1 model family, 3 seeds, Holm adj p=0.050\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1 提出，R1 AGREE (M4)。14B 仅 Qwen3，TOST df=2 功效不足，Holm adj p=0.050 borderline。无 32B+ 实验。应降级为 preliminary observation 而非 stated finding。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 和 Conclusion 中 14B 结论加入更强 hedging，标注为 preliminary observation 而非 confirmed finding\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-W4\"\n  summary: \"GenRM 领域特异性对比（代码中 generation ≤ discrimination，与数学相反）分析不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4 提出，R1 AGREE。§5 Conclusion 仅 1 句话讨论。论文已有支撑数据（parseable rate 差异、output token count、CWM format compliance rate）可用于分析 WHY 领域差异存在。增加 1-2 段可同时提升 Excitement（回应 R2-N1）。\"\n  action_items:\n    - round: 13\n      action: \"§5 Discussion/Conclusion 新增 1-2 段分析代码 vs 数学验证的结构性差异，提出可检验假设（output structure, format compliance, error type distribution）\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-M1\"\n  summary: \"PRM/ORM 映射命名反直觉——CLS 听起来像 ORM 而非 PRM\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 AGREE。§4 中 CLS→PRM-like 和 TRAJ→ORM-like 的映射基于 per-test vs per-patch 粒度是正确的，但命名反直觉。建议加一句显式澄清。\"\n  action_items:\n    - round: 13\n      action: \"§4 Related Work 加一句澄清：per-test granularity 对应 per-step PRM，per-patch verdict 对应 outcome-level ORM\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-M2\"\n  summary: \"Abstract 统计符号过密（z=−23.7, TOST, pp 值），降低可读性\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M1 提出，R1 AGREE。建议先陈述定性洞见，再给统计支撑。但 Abstract 已 ~189 words（≤200 word 限制），调整空间有限。\"\n  action_items:\n    - round: 13\n      action: \"考虑将部分统计数值（如 z=−23.7）从 Abstract 移入正文\"\n      assigned_to: \"paper\"\n      status: open\n\n- id: \"R13-M3\"\n  summary: \"三项贡献独立性值得商榷——互补性和 taxonomy 是主发现的辅助分析\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M4 提出，R1 partial REBUT：failure mode taxonomy (Table 4) 具有可迁移的诊断价值，可独立于三方比较使用。R1 同意 Contribution 2（互补性）与 Contribution 1 独立性较弱。Director：Minor——taxonomy 独立性成立，但 contribution list 可微调。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-23T12:54:24.108115+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 29256}, \"error\": \"\"}"}

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

_source line 1066 · 2026-05-23T12:56:38.246048+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "report": "\n# Round 13 审稿报告（Fresh Review）\n\n**投稿**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 (ARR May cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性/贡献+完整性）\n**轮次**: Round 13 (Fresh Review)，1 轮独立审稿 + 1 轮交叉分享\n\n---\n\n## Summary\n\n本文首次在匹配条件下系统比较了 LLM 代码修复中三种 execution-free 验证公式（CLS 分类、CWM 生成、TRAJ 轨迹级），跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别和多个 seeds。核心发现为三层结构：(1) fine-tuning 必要（35-36pp 增益）；(2) function-level 三种公式近等价（CLS-CWM TOST 确认，CLS-TRAJ Holm 校正后未确认但 gap 单调收窄至 1.07pp@14B）；(3) repo-level 在 ≤8B LoRA 下等价崩塌（CLS-CWM gap 18-26pp，由 CWM format collapse 驱动）。论文同时提供了 failure mode taxonomy 和 error complementarity 分析。\n\n---\n\n## Strengths\n\n**S1. 首个匹配条件的系统比较。** 控制模型容量、训练数据、超参数和评估协议进行三方公式比较，直接回答从业者的 formulation 选择问题。Cross-family 一致性（Qwen3 和 DeepSeek-Coder 在 CLS-CWM 差异方向一致）增强结论可信度。[两人共识]\n\n**S2. 统计框架出色。** TOST 等价检验 + Bayesian ROPE 双验证、clustered bootstrap（114 clusters, 10K resamples）、Holm-Bonferroni 校正（k=5）、ICC/DEFF 修正——在 NLP 实证论文中属上乘水准。特别是 §3.4 明确区分\"等价\"与\"未能拒绝差异\"，CLS-CWM 等价在多个统计方法下一致（TOST p=0.007; P(ROPE)=0.975）。[两人共识, R1 Soundness 3.5, R2 Soundness 4.0]\n\n**S3. 透明的混淆因素分析。** §3.7 和 Appendix O 明确列出并量化 5 个 confounds，包括 preprocessing-checkpoint 链式影响（7.68pp）和 worst-case compounding 分析（±11.5pp）。CLS-TRAJ 等价在 Holm 校正后不成立也被如实报告。[两人共识]\n\n**S4. 实用的 failure mode taxonomy。** Table 4 的三类失败模式（format collapse, decision collapse, aggregation penalty）提供可迁移的诊断框架，对实践者有直接价值。R1 认为此贡献可独立于三方比较使用。[两人共识]\n\n**S5. GenRM 领域特异性观察。** 代码验证中 generation ≤ discrimination（与 GenRM 在数学推理中的发现相反）是一个有价值的数据点，暗示 generation advantage 可能是 domain-dependent 的。[两人共识, 但均认为分析不够深入]\n\n**S6. Related Work 覆盖充分。** CodeScaler, Aletheia, GenRM, GenPRM, FunPRM, CodeRM 均已引用。两位 Reviewer 均未发现 2025-2026 年的重大遗漏。[两人共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（1 项）\n\n**N1. [critical] [consensus] Appendix \"P: Limitations\" 标题可能违反 EMNLP 格式规则。**\n- EMNLP 2026 / ARR 规定\"一篇文章只能有一个 limitations section，放在正文里面，appendix 不能有 limitations section\"。Appendix 概览明确列出 \"P: Limitations\"，构成形式违规。\n- **建议**：重命名为 \"Extended Experimental Details\" 或 \"Additional Confound Analysis\"，从 Appendix 概览中移除 \"Limitations\" 标签。\n- **R1 提出, R2 完全 AGREE。**\n\n### Should-Fix（4 项）\n\n**W1. [warning] [consensus] Abstract/Conclusion 中 TRAJ \"not confirmed\" 措辞在 power ~0.3 下 over-stated。**\n- Abstract \"TRAJ parity is not confirmed after multiple comparison correction at any scale tested\" 在 power ~0.3 下可能让读者误解为存在差异的证据，而实际是检验力不足以检测等价（absence of evidence ≠ evidence of absence）。\n- 14B 结果（三公式收敛至 1.07pp 以内）应给予更突出位置以平衡消极暗示。\n- **R1 标 Must-Fix, R2 认为 Should-Fix（§3.4 已诚实报告 power）。Director 裁定 Should-Fix：方法论无缺陷，问题仅在措辞精度。**\n- **建议**：Abstract 加 power 限定语；Conclusion 讨论达到 power ≥0.8 所需 seed 数。\n\n**W2. [warning] [consensus] 核心发现可从论文自身 §2.2 理论预测，新颖性受限。**\n- §2.2 预测短输出→等价、长输出→格式崩溃，两个核心结论均被自身理论预测。实证贡献降格为\"验证\"而非\"发现\"，直接限制 Excitement。\n- R1 补充：quantitative boundary conditions（14B 收敛速度、failure mode 跨模型一致性）超越纯理论预测。\n- **R2 标 Must-Fix, R1 AGREE（但认为有 nuance）。Director 裁定 Should-Fix：这是 inherent limitation（贡献类型为 empirical comparison），无法通过修改消除，但可通过 framing 改善——深入分析理论预测失败之处。**\n- **建议**：(a) 诚实重新定位为\"首次严格实证验证\"；(b) 深入刻画理论预测未覆盖的边界条件。\n\n**W3. [warning] [consensus] TRAJ 比较被训练配置严重混淆。**\n- TRAJ 使用 ~400 训练实例 vs CLS/CWM ~70K；不同 lr；variant-level labels vs per-test。Downsample ablation 控制了数据量但未控制 label granularity（formulation-inherent confound）。\n- §3.5 已有 \"exploratory\" 标注和 confound 讨论，但主文 Tables 1-3 仍将三公式并列呈现无视觉区分。\n- **R2 标 Must-Fix, R1 AGREE (W1)。Director 裁定 Should-Fix：§3.5 已有充分 disclosure，但 Tables 中应添加视觉标注。**\n- **建议**：Tables 1-3 为 TRAJ 行添加 † 标记 + 脚注说明训练配置差异。\n\n**W4. [warning] [consensus] GenRM 领域特异性对比（代码中 generation ≤ discrimination vs 数学中 generation > discrimination）分析不充分。**\n- §5 Conclusion 仅 1 句话讨论。论文已有支撑数据（parseable rate 差异、output token count、format compliance rate）可用于分析 WHY 领域差异存在。\n- 增加 1-2 段分析可同时提升 Excitement（回应 W2 的 confirmation vs discovery 批评）。\n- **R2 提出, R1 AGREE。**\n\n### Minor（3 项）\n\n**M1. [info]** Oracle 互补性（Contribution 2）应更明确框定为 negative result + motivation。Simple routing 仅捕获 <0.4pp 的 oracle 优势，当前不可操作。R1 认为作为 negative result 有独立价值（排除了简单方法），R2 认为 contribution 权重应降低。\n\n**M2. [info]** PRM/ORM 映射命名反直觉——\"CLS→PRM-like\" 和 \"TRAJ→ORM-like\" 基于 per-test vs per-patch 粒度是正确的，但 \"classification\" 听起来像 ORM。建议加一句显式澄清。\n\n**M3. [info]** Abstract 统计符号密度偏高（z=−23.7, TOST, pp 值），建议先陈述定性洞见再给统计支撑。考虑将部分数值移入正文。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n- [AGREE] Appendix \"P: Limitations\" 格式违规需修复 (N1)\n- [AGREE] TRAJ 训练配置混淆是论文的系统性弱点 (W3)\n- [AGREE] GenRM 领域对比分析不充分 (W4)\n- [AGREE] 14B 结论应降级为 preliminary observation\n- [AGREE] PRM/ORM 映射需显式澄清 (M2)\n- [AGREE] Overall 3.0 (Findings), Excitement 3/5\n- [AGREE] Related Work 覆盖充分，无重大遗漏\n- [AGREE] 统计框架在 NLP 实证论文中属上乘水准\n- [AGREE] Failure mode taxonomy 有独立实践价值\n\n## Reviewer Divergence [REBUT]\n\n以下问题存在分歧，Director 已裁定：\n\n| 问题 | R1 | R2 | Director 裁定 |\n|------|----|----|--------------|\n| R1-N1 severity（TRAJ power over-statement）| Must-Fix | Should-Fix | **Should-Fix**：§3.4 已诚实报告，问题仅在措辞 |\n| R2-W3 页数溢出 | 不同意（PDF+LaTeX 证据显示未超页）| Should-Fix | **降级 Minor**：R1 提供 LaTeX+PDF 证据，Limitations 不计页 |\n| R2-W2 互补性贡献 | 作为 negative result 有价值 | 可能误导 | **Minor**：应框定为 negative result |\n| R2-M4 贡献独立性 | Taxonomy 可独立使用 | 应合并 | **Minor**：R1 论证 Table 4 可迁移 |\n| Soundness 评分 | 3.5/5 | 4.0/5 | **3.5**：CLS-CWM 可靠但 TRAJ/CWM 两翼均有 confounds |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** ±2pp SESOI 是在看到数据之前还是之后确定的？如果是后者，请讨论对 TOST 结论的影响。[R1-Q1, R2 AGREE]\n\n**Q2.** 在当前实验设计下，需要多少 seeds 才能使 CLS-TRAJ 比较达到 power ≥0.8？[R1-Q2]\n\n**Q3.** CLS-CWM 使用 seed-level paired analysis 而 CLS-TRAJ 使用 clustered bootstrap，两个比较使用不同统计方法是否引入方法论不对称性？[R1-Q3]\n\n**Q4.** 代码验证中 generation ≤ discrimination（与 GenRM 数学结论相反）的具体原因是什么？是 output token 数量、结构化格式要求、还是其他因素？[R2-Q3, R1 AGREE]\n\n**Q5.** 14B 实验能否用另一模型家族进行 cross-family 复制？[R2-Q5, R1 AGREE (M4)]\n\n---\n\n## Missing References\n\n两位 Reviewer 均未发现重大遗漏。CodeScaler, Aletheia, GenRM, GenPRM, FunPRM, CodeRM, SolidCoder 等 2025-2026 关键工作均已引用。PRM/ORM 映射（CLS→PRM-like, TRAJ→ORM-like, CWM→generative verifier）在粒度维度上准确。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 13 info）：\n\n**Warnings:**\n- pp.1-2 连续两页纯文本无 display item，Figure 1 直到 p.3 才出现。审稿人前 2 页无视觉锚定。\n- p.8 整页纯文本（Related Work + Conclusion），pp.7-8 区域视觉单调。\n\n**Info (选摘):**\n- Figure 1 概念图清晰，caption 自包含（p.3）\n- Tables 1-4 使用 booktabs 风格，格式规范\n- Figure 2 右栏放置，tick labels 偏小但可辨读（建议 ≥9pt）\n- References 格式统一，无 [?] 未解析引用\n- Limitations 段落约 5 行，覆盖 3 个限制点，符合 EMNLP 规范\n- 最末页 appendix 约 1/4 内容，大面积空白（不影响）\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 4/5 | **3.5/5** |\n| Excitement | 3/5 | 3/5 | **3/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.0 | 3.0 | **3.0 (Findings)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**Overall Assessment: 3.0 — Findings**\n\n**核心判断**：本文是一篇方法论严谨的实证比较研究，统计分析水准在 NLP 实证论文中处于上游。CLS-CWM function-level 等价这一核心发现在多个统计方法下一致确认，可信度高。Failure mode taxonomy 提供了独立的实践价值。\n\n但三方比较中 TRAJ 一翼受训练配置混淆削弱（~400 vs ~70K 实例、label granularity 差异无法消除），CWM 一翼受生态效度限制（≤8B LoRA vs 原始 32B），使得论文实际只有 CLS-CWM function-level 等价这一个完全可靠的新发现。核心结论可从论文自身 §2.2 理论分析预测，属 confirmation 而非 discovery，限制了 Excitement。14B 收敛结果有前瞻价值但证据不足（1 family, 3 seeds, borderline p-value）。\n\n修复 N1（Appendix 格式违规）后，论文适合 Findings 发表。若能深入展开 GenRM 领域特异性分析（W4）并改善 TRAJ 比较的 framing（W3），可提升至 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 2（error complementarity）应重新框定为 negative result：simple routing 仅捕获 <0.4pp，互补性存在但当前不可操作。\n- Contribution 3（failure mode taxonomy）独立性成立（R1 论证可迁移），保持。\n- \"formulation choice is moderated by code complexity\" 已有 ≤8B qualifier，措辞恰当。\n\n### §2.2 Expected Failure Modes\n- 理论分析预测了两个核心方向（function equiv + repo divergence），使实证发现的 surprise value 降低。可考虑重新定位为 \"empirical validation with boundary characterization\"。\n\n### §3.1 Experimental Setup\n- TRAJ 训练配置差异（~400 vs ~70K, 不同 lr, variant-level labels）在此处仅简略提及。Tables 1-3 应添加 † 标注。\n\n### §3.4 Equivalence\n- Power ~0.3 的讨论充分（§3.4 末段），但 Abstract 和 Conclusion 的 \"not confirmed\" 措辞未反映此限制。\n- SESOI ±2pp 已标注 \"not pre-registered\"，sensitivity analysis 报告 ±1.52pp 临界值，处理恰当。\n\n### §3.5 Repo-Level\n- \"exploratory due to limited seed coverage\" 标注良好。\n- Variant-level 分析使用描述性语言，避免 causal claims，处理得当。\n\n### §4 Related Work\n- PRM/ORM 映射（CLS→PRM-like, TRAJ→ORM-like）粒度维度正确，但命名反直觉。建议加一句显式澄清。\n- GenRM 对比仅一句话，应扩展。\n\n### §5 Conclusion\n- GenRM domain-specificity 段落存在但过于简短。应分析 WHY（output structure, format compliance, error type）。\n- 14B 结论应加更强 hedging。\n\n### Limitations\n- 简短充分（~5 行，3 点），符合 EMNLP 规范。\n\n### Appendix\n- \"P: Limitations\" 标题违反 EMNLP 格式规则，需重命名。[Must-Fix]\n- 16 个 Appendix (A-P, ~15 pages) vs 8 页正文。量大但内容必要（equivalence testing 的 sensitivity/robustness 要求）。\n",
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
    "project": "exec-sim-repair-verifier",
    "report": "\n# Round 13 审稿报告（Fresh Review）\n\n**投稿**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 (ARR May cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性/贡献+完整性）\n**轮次**: Round 13 (Fresh Review)，1 轮独立审稿 + 1 轮交叉分享\n\n---\n\n## Summary\n\n本文首次在匹配条件下系统比较了 LLM 代码修复中三种 execution-free 验证公式（CLS 分类、CWM 生成、TRAJ 轨迹级），跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别和多个 seeds。核心发现为三层结构：(1) fine-tuning 必要（35-36pp 增益）；(2) function-level 三种公式近等价（CLS-CWM TOST 确认，CLS-TRAJ Holm 校正后未确认但 gap 单调收窄至 1.07pp@14B）；(3) repo-level 在 ≤8B LoRA 下等价崩塌（CLS-CWM gap 18-26pp，由 CWM format collapse 驱动）。论文同时提供了 failure mode taxonomy 和 error complementarity 分析。\n\n---\n\n## Strengths\n\n**S1. 首个匹配条件的系统比较。** 控制模型容量、训练数据、超参数和评估协议进行三方公式比较，直接回答从业者的 formulation 选择问题。Cross-family 一致性（Qwen3 和 DeepSeek-Coder 在 CLS-CWM 差异方向一致）增强结论可信度。[两人共识]\n\n**S2. 统计框架出色。** TOST 等价检验 + Bayesian ROPE 双验证、clustered bootstrap（114 clusters, 10K resamples）、Holm-Bonferroni 校正（k=5）、ICC/DEFF 修正——在 NLP 实证论文中属上乘水准。特别是 §3.4 明确区分\"等价\"与\"未能拒绝差异\"，CLS-CWM 等价在多个统计方法下一致（TOST p=0.007; P(ROPE)=0.975）。[两人共识, R1 Soundness 3.5, R2 Soundness 4.0]\n\n**S3. 透明的混淆因素分析。** §3.7 和 Appendix O 明确列出并量化 5 个 confounds，包括 preprocessing-checkpoint 链式影响（7.68pp）和 worst-case compounding 分析（±11.5pp）。CLS-TRAJ 等价在 Holm 校正后不成立也被如实报告。[两人共识]\n\n**S4. 实用的 failure mode taxonomy。** Table 4 的三类失败模式（format collapse, decision collapse, aggregation penalty）提供可迁移的诊断框架，对实践者有直接价值。R1 认为此贡献可独立于三方比较使用。[两人共识]\n\n**S5. GenRM 领域特异性观察。** 代码验证中 generation ≤ discrimination（与 GenRM 在数学推理中的发现相反）是一个有价值的数据点，暗示 generation advantage 可能是 domain-dependent 的。[两人共识, 但均认为分析不够深入]\n\n**S6. Related Work 覆盖充分。** CodeScaler, Aletheia, GenRM, GenPRM, FunPRM, CodeRM 均已引用。两位 Reviewer 均未发现 2025-2026 年的重大遗漏。[两人共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（1 项）\n\n**N1. [critical] [consensus] Appendix \"P: Limitations\" 标题可能违反 EMNLP 格式规则。**\n- EMNLP 2026 / ARR 规定\"一篇文章只能有一个 limitations section，放在正文里面，appendix 不能有 limitations section\"。Appendix 概览明确列出 \"P: Limitations\"，构成形式违规。\n- **建议**：重命名为 \"Extended Experimental Details\" 或 \"Additional Confound Analysis\"，从 Appendix 概览中移除 \"Limitations\" 标签。\n- **R1 提出, R2 完全 AGREE。**\n\n### Should-Fix（4 项）\n\n**W1. [warning] [consensus] Abstract/Conclusion 中 TRAJ \"not confirmed\" 措辞在 power ~0.3 下 over-stated。**\n- Abstract \"TRAJ parity is not confirmed after multiple comparison correction at any scale tested\" 在 power ~0.3 下可能让读者误解为存在差异的证据，而实际是检验力不足以检测等价（absence of evidence ≠ evidence of absence）。\n- 14B 结果（三公式收敛至 1.07pp 以内）应给予更突出位置以平衡消极暗示。\n- **R1 标 Must-Fix, R2 认为 Should-Fix（§3.4 已诚实报告 power）。Director 裁定 Should-Fix：方法论无缺陷，问题仅在措辞精度。**\n- **建议**：Abstract 加 power 限定语；Conclusion 讨论达到 power ≥0.8 所需 seed 数。\n\n**W2. [warning] [consensus] 核心发现可从论文自身 §2.2 理论预测，新颖性受限。**\n- §2.2 预测短输出→等价、长输出→格式崩溃，两个核心结论均被自身理论预测。实证贡献降格为\"验证\"而非\"发现\"，直接限制 Excitement。\n- R1 补充：quantitative boundary conditions（14B 收敛速度、failure mode 跨模型一致性）超越纯理论预测。\n- **R2 标 Must-Fix, R1 AGREE（但认为有 nuance）。Director 裁定 Should-Fix：这是 inherent limitation（贡献类型为 empirical comparison），无法通过修改消除，但可通过 framing 改善——深入分析理论预测失败之处。**\n- **建议**：(a) 诚实重新定位为\"首次严格实证验证\"；(b) 深入刻画理论预测未覆盖的边界条件。\n\n**W3. [warning] [consensus] TRAJ 比较被训练配置严重混淆。**\n- TRAJ 使用 ~400 训练实例 vs CLS/CWM ~70K；不同 lr；variant-level labels vs per-test。Downsample ablation 控制了数据量但未控制 label granularity（formulation-inherent confound）。\n- §3.5 已有 \"exploratory\" 标注和 confound 讨论，但主文 Tables 1-3 仍将三公式并列呈现无视觉区分。\n- **R2 标 Must-Fix, R1 AGREE (W1)。Director 裁定 Should-Fix：§3.5 已有充分 disclosure，但 Tables 中应添加视觉标注。**\n- **建议**：Tables 1-3 为 TRAJ 行添加 † 标记 + 脚注说明训练配置差异。\n\n**W4. [warning] [consensus] GenRM 领域特异性对比（代码中 generation ≤ discrimination vs 数学中 generation > discrimination）分析不充分。**\n- §5 Conclusion 仅 1 句话讨论。论文已有支撑数据（parseable rate 差异、output token count、format compliance rate）可用于分析 WHY 领域差异存在。\n- 增加 1-2 段分析可同时提升 Excitement（回应 W2 的 confirmation vs discovery 批评）。\n- **R2 提出, R1 AGREE。**\n\n### Minor（3 项）\n\n**M1. [info]** Oracle 互补性（Contribution 2）应更明确框定为 negative result + motivation。Simple routing 仅捕获 <0.4pp 的 oracle 优势，当前不可操作。R1 认为作为 negative result 有独立价值（排除了简单方法），R2 认为 contribution 权重应降低。\n\n**M2. [info]** PRM/ORM 映射命名反直觉——\"CLS→PRM-like\" 和 \"TRAJ→ORM-like\" 基于 per-test vs per-patch 粒度是正确的，但 \"classification\" 听起来像 ORM。建议加一句显式澄清。\n\n**M3. [info]** Abstract 统计符号密度偏高（z=−23.7, TOST, pp 值），建议先陈述定性洞见再给统计支撑。考虑将部分数值移入正文。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n- [AGREE] Appendix \"P: Limitations\" 格式违规需修复 (N1)\n- [AGREE] TRAJ 训练配置混淆是论文的系统性弱点 (W3)\n- [AGREE] GenRM 领域对比分析不充分 (W4)\n- [AGREE] 14B 结论应降级为 preliminary observation\n- [AGREE] PRM/ORM 映射需显式澄清 (M2)\n- [AGREE] Overall 3.0 (Findings), Excitement 3/5\n- [AGREE] Related Work 覆盖充分，无重大遗漏\n- [AGREE] 统计框架在 NLP 实证论文中属上乘水准\n- [AGREE] Failure mode taxonomy 有独立实践价值\n\n## Reviewer Divergence [REBUT]\n\n以下问题存在分歧，Director 已裁定：\n\n| 问题 | R1 | R2 | Director 裁定 |\n|------|----|----|--------------|\n| R1-N1 severity（TRAJ power over-statement）| Must-Fix | Should-Fix | **Should-Fix**：§3.4 已诚实报告，问题仅在措辞 |\n| R2-W3 页数溢出 | 不同意（PDF+LaTeX 证据显示未超页）| Should-Fix | **降级 Minor**：R1 提供 LaTeX+PDF 证据，Limitations 不计页 |\n| R2-W2 互补性贡献 | 作为 negative result 有价值 | 可能误导 | **Minor**：应框定为 negative result |\n| R2-M4 贡献独立性 | Taxonomy 可独立使用 | 应合并 | **Minor**：R1 论证 Table 4 可迁移 |\n| Soundness 评分 | 3.5/5 | 4.0/5 | **3.5**：CLS-CWM 可靠但 TRAJ/CWM 两翼均有 confounds |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** ±2pp SESOI 是在看到数据之前还是之后确定的？如果是后者，请讨论对 TOST 结论的影响。[R1-Q1, R2 AGREE]\n\n**Q2.** 在当前实验设计下，需要多少 seeds 才能使 CLS-TRAJ 比较达到 power ≥0.8？[R1-Q2]\n\n**Q3.** CLS-CWM 使用 seed-level paired analysis 而 CLS-TRAJ 使用 clustered bootstrap，两个比较使用不同统计方法是否引入方法论不对称性？[R1-Q3]\n\n**Q4.** 代码验证中 generation ≤ discrimination（与 GenRM 数学结论相反）的具体原因是什么？是 output token 数量、结构化格式要求、还是其他因素？[R2-Q3, R1 AGREE]\n\n**Q5.** 14B 实验能否用另一模型家族进行 cross-family 复制？[R2-Q5, R1 AGREE (M4)]\n\n---\n\n## Missing References\n\n两位 Reviewer 均未发现重大遗漏。CodeScaler, Aletheia, GenRM, GenPRM, FunPRM, CodeRM, SolidCoder 等 2025-2026 关键工作均已引用。PRM/ORM 映射（CLS→PRM-like, TRAJ→ORM-like, CWM→generative verifier）在粒度维度上准确。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 13 info）：\n\n**Warnings:**\n- pp.1-2 连续两页纯文本无 display item，Figure 1 直到 p.3 才出现。审稿人前 2 页无视觉锚定。\n- p.8 整页纯文本（Related Work + Conclusion），pp.7-8 区域视觉单调。\n\n**Info (选摘):**\n- Figure 1 概念图清晰，caption 自包含（p.3）\n- Tables 1-4 使用 booktabs 风格，格式规范\n- Figure 2 右栏放置，tick labels 偏小但可辨读（建议 ≥9pt）\n- References 格式统一，无 [?] 未解析引用\n- Limitations 段落约 5 行，覆盖 3 个限制点，符合 EMNLP 规范\n- 最末页 appendix 约 1/4 内容，大面积空白（不影响）\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 4/5 | **3.5/5** |\n| Excitement | 3/5 | 3/5 | **3/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.0 | 3.0 | **3.0 (Findings)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**Overall Assessment: 3.0 — Findings**\n\n**核心判断**：本文是一篇方法论严谨的实证比较研究，统计分析水准在 NLP 实证论文中处于上游。CLS-CWM function-level 等价这一核心发现在多个统计方法下一致确认，可信度高。Failure mode taxonomy 提供了独立的实践价值。\n\n但三方比较中 TRAJ 一翼受训练配置混淆削弱（~400 vs ~70K 实例、label granularity 差异无法消除），CWM 一翼受生态效度限制（≤8B LoRA vs 原始 32B），使得论文实际只有 CLS-CWM function-level 等价这一个完全可靠的新发现。核心结论可从论文自身 §2.2 理论分析预测，属 confirmation 而非 discovery，限制了 Excitement。14B 收敛结果有前瞻价值但证据不足（1 family, 3 seeds, borderline p-value）。\n\n修复 N1（Appendix 格式违规）后，论文适合 Findings 发表。若能深入展开 GenRM 领域特异性分析（W4）并改善 TRAJ 比较的 framing（W3），可提升至 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 2（error complementarity）应重新框定为 negative result：simple routing 仅捕获 <0.4pp，互补性存在但当前不可操作。\n- Contribution 3（failure mode taxonomy）独立性成立（R1 论证可迁移），保持。\n- \"formulation choice is moderated by code complexity\" 已有 ≤8B qualifier，措辞恰当。\n\n### §2.2 Expected Failure Modes\n- 理论分析预测了两个核心方向（function equiv + repo divergence），使实证发现的 surprise value 降低。可考虑重新定位为 \"empirical validation with boundary characterization\"。\n\n### §3.1 Experimental Setup\n- TRAJ 训练配置差异（~400 vs ~70K, 不同 lr, variant-level labels）在此处仅简略提及。Tables 1-3 应添加 † 标注。\n\n### §3.4 Equivalence\n- Power ~0.3 的讨论充分（§3.4 末段），但 Abstract 和 Conclusion 的 \"not confirmed\" 措辞未反映此限制。\n- SESOI ±2pp 已标注 \"not pre-registered\"，sensitivity analysis 报告 ±1.52pp 临界值，处理恰当。\n\n### §3.5 Repo-Level\n- \"exploratory due to limited seed coverage\" 标注良好。\n- Variant-level 分析使用描述性语言，避免 causal claims，处理得当。\n\n### §4 Related Work\n- PRM/ORM 映射（CLS→PRM-like, TRAJ→ORM-like）粒度维度正确，但命名反直觉。建议加一句显式澄清。\n- GenRM 对比仅一句话，应扩展。\n\n### §5 Conclusion\n- GenRM domain-specificity 段落存在但过于简短。应分析 WHY（output structure, format compliance, error type）。\n- 14B 结论应加更强 hedging。\n\n### Limitations\n- 简短充分（~5 行，3 点），符合 EMNLP 规范。\n\n### Appendix\n- \"P: Limitations\" 标题违反 EMNLP 格式规则，需重命名。[Must-Fix]\n- 16 个 Appendix (A-P, ~15 pages) vs 8 页正文。量大但内容必要（equivalence testing 的 sensitivity/robustness 要求）。\n",
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

_source line 1067 · 2026-05-23T12:56:42.466749+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4220
}
```

</details>

---


### Assistant

_source line 1068 · 2026-05-23T12:56:49.993979+00:00_

**Round 13 审稿完成。**

报告已投递至 Research Director。核心结论：

- **Overall: 3.0 (Findings)**，Soundness 3.5，Excitement 3.0
- **1 项 Must-Fix**：Appendix "P: Limitations" 标题违反 EMNLP 格式规则（重命名即可）
- **4 项 Should-Fix**：(1) Abstract TRAJ 措辞加 power 限定语；(2) 新颖性定位从 "discovery" 调整为 "first rigorous empirical validation"；(3) Tables 中 TRAJ 行加视觉标注区分训练配置差异；(4) GenRM 领域对比扩写 1-2 段
- 修复 N1 后适合 Findings；若深入展开 W4 (GenRM) 并改善 W3 (TRAJ framing)，可冲击 3.5 (Borderline Conference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 99

## Round 99

2 recorded events


### User

_source line 1069 · 2026-05-23T12:56:52.556136+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 审稿意见的逐条回应。主要结论：

- **13 项中 12 项 [AGREE]**，1 项 [AGREE with nuance]（W2 CWM 生态效度——论文已部分回应）
- R1 提出了我未充分关注的两个有价值问题：power ~0.3 下 CLS-TRAJ 结论的措辞问题（N1）、checkpoint selection ablation 覆盖不足（W4）
- 两份审稿在 Overall Assessment 上完全一致：**3.0 (Findings)**
- 我的独特贡献集中在新颖性维度（核心发现可预测性）、GenRM 对比被浪费、正文页数溢出三点

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

_source line 1070 · 2026-05-23T12:57:03.015849+00:00_

Round 13 审稿已完成。

**审稿报告已投递至 Research Director。**

核心结论：
- **Overall: 3.0 (Findings)**，Soundness 3.5, Excitement 3.0, Confidence 4/5
- **1 项 Must-Fix**：Appendix "P: Limitations" 标题违反 EMNLP 格式规则（需重命名）
- **4 项 Should-Fix**：TRAJ power 措辞、novelty framing、TRAJ 配置混淆标注、GenRM 领域对比展开
- **3 项 Minor**：Oracle 互补性 framing、PRM/ORM 命名澄清、Abstract 符号密度
- **Issue Tracker 已同步**：新增 7 个 R13 issue（1 critical, 4 warning, 3 info），历史 issue 的 R13 mentions 已更新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 100

## Round 100

56 recorded events


### User

_source line 1071 · 2026-05-23T13:29:03.310443+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
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

_source line 1072 · 2026-05-23T13:29:14.372751+00:00_

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

_source line 1073 · 2026-05-23T13:29:14.474097+00:00_

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
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-23T13:29:22.929186+00:00_

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

_source line 1075 · 2026-05-23T13:29:22.979765+00:00_

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

_source line 1076 · 2026-05-23T13:29:26.695166+00:00_

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

_source line 1077 · 2026-05-23T13:29:26.746175+00:00_



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

_source line 1078 · 2026-05-23T13:29:33.476483+00:00_

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

_source line 1079 · 2026-05-23T13:29:34.883106+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (266 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D13
…[truncated 1825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 1080 · 2026-05-23T13:29:35.335399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "limit": "80"
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
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-23T13:29:35.837904+00:00_

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
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1082 · 2026-05-23T13:29:36.540628+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/submitted.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/submitted.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1083 · 2026-05-23T13:29:36.892367+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_6/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_7/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_9/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_10/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_11/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_12/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1084 · 2026-05-23T13:29:36.993098+00:00_

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

_source line 1085 · 2026-05-23T13:29:37.043677+00:00_

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

_source line 1086 · 2026-05-23T13:29:48.780587+00:00_

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

_source line 1087 · 2026-05-23T13:29:48.780988+00:00_



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

_source line 1088 · 2026-05-23T13:29:49.735990+00:00_

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

_source line 1089 · 2026-05-23T13:29:50.238539+00:00_

1	\begin{abstract}
2	LLM-based program repair increasingly generates multiple candidate patches, selecting the best via a verifier. Three execution-free alternatives to expensive execution-based verification have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares them under matched conditions.
3	
4	We present the first systematic comparison across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is not confirmed after multiple comparison correction at current power (${\sim}$0.3), but the gap narrows monotonically from 3.11\pp{} (4B) to 1.07\pp{} (14B). At repository level, this equivalence collapses ($z{=}-23.7$, DeepSeek-Coder): the \cls{}--\cwm{} gap widens to 18--26\pp{} across 2--3 seeds per model under our ${\leq}$8B LoRA protocol, driven by format collapse. At 14B (3 seeds, single family), all three formulations narrow to within 1.07\pp{}, a preliminary observation consistent with capacity-dependent convergence.
5	
6	Error complementarity and a failure mode taxonomy motivate future work on complexity-aware formulation routing, though simple heuristics capture $<$0.4\pp{} of oracle advantage.
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

_source line 1090 · 2026-05-23T13:29:50.239047+00:00_

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

_source line 1091 · 2026-05-23T13:29:50.641025+00:00_

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
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-23T13:29:50.641370+00:00_

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

_source line 1093 · 2026-05-23T13:29:50.742081+00:00_

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


### Tool call

_source line 1094 · 2026-05-23T13:29:54.457739+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
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
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1095 · 2026-05-23T13:29:56.264777+00:00_

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

_source line 1096 · 2026-05-23T13:29:57.320058+00:00_

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
…[truncated 20091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 1097 · 2026-05-23T13:29:57.320573+00:00_

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

_source line 1098 · 2026-05-23T13:29:57.472071+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. CodeScaler~\cite{zhu2026codescaler} trains execution-free reward models for both RL and test-time scaling. Verification formulations span trajectory-level reward~\cite{shum2025swerm}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. GenRM~\cite{hosseini2025genrm} and GenPRM~\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formula
…[truncated 1533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1099 · 2026-05-23T13:29:57.472591+00:00_

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

_source line 1100 · 2026-05-23T13:29:57.623591+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} equivalence is not confirmed after correction, but the gap narrows monotonically to 1.07\pp{} at 14B. At repository level under ${\leq}$8B LoRA, divergence reaches 18--26\pp{} ($z{=}-23.7$), consistent across families (\S\ref{sec:threats}). Preliminary 14B results (3 seeds, single family) narrow all gaps to within 1.07\pp{}, though formal confirmation requires more seeds. This contrasts with mathematical reasoning, where generative verification outperforms discriminative~\cite{hosseini2025genrm}; we attribute this to output structure---code verification requires exact-match outputs (${\sim}$477 tokens/test for \cwm{} vs.\ 1 for \cls{}), and $>$50\% of repo-level \cwm{} outputs are unparseable, converting generation from a reasoning advantage into a format fidelity challenge absent in math.
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
  "elapsed_ms": 150
}
```

</details>

---


### Tool result

_source line 1101 · 2026-05-23T13:30:00.338653+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

Based on the search results, I found some information related to EMNLP 2026, though the se
…[truncated 1219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 5880
}
```

</details>

---


### Tool call

_source line 1102 · 2026-05-23T13:30:06.225284+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline author guidelines page limit"
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
    "query": "EMNLP 2026 submission deadline author guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 1103 · 2026-05-23T13:30:06.727573+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR 2026 submission guidelines anonymous review template acl rolling review"
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
    "query": "ARR 2026 submission guidelines anonymous review template acl rolling review"
  }
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-23T13:30:09.187125+00:00_

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

_source line 1105 · 2026-05-23T13:30:09.539491+00:00_

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
…[truncated 58270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1106 · 2026-05-23T13:30:09.539909+00:00_

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

_source line 1107 · 2026-05-23T13:30:09.590395+00:00_

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
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1108 · 2026-05-23T13:30:12.053118+00:00_

Web search results for query: "EMNLP 2026 submission deadline author guidelines page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Information For Authors | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/information/authors"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"}]

Based on the search results, here's the information about EMNLP 2026:

**Submission Deadline:**
The ARR submission deadline is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

**Page Limits:**
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to addres
…[truncated 588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 5827
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-23T13:30:13.911434+00:00_

Web search results for query: "ARR 2026 submission guidelines anonymous review template acl rolling review"

Links: [{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here's information about ARR 2026 submission guidelines regarding anonymous review and templates:

## Submission Guidelines & Templates

Paper submissions must use the official ACL style templates, which are available as an Overleaf template and can be downloaded directly via https://aclrollingreview.org/cfp under 'Paper Submission Process, Criteria and Templates'. Additionally, ARR abandons the MS Word Template for conference submissions, with submissions based on the Word template being desk-rejected starting from March 2026.
…[truncated 814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 7183
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-23T13:30:36.893975+00:00_

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


### Tool call

_source line 1111 · 2026-05-23T13:30:37.246974+00:00_

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

_source line 1112 · 2026-05-23T13:30:37.699823+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (266 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D13
…[truncated 1825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 805
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-23T13:30:37.700219+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-23T13:30:38.051791+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "review_issues.yaml",
  "max_chars": "12000"
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
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 1115 · 2026-05-23T13:30:38.102473+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

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

_source line 1116 · 2026-05-23T13:30:46.108884+00:00_

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

_source line 1117 · 2026-05-23T13:30:46.109238+00:00_

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

_source line 1118 · 2026-05-23T13:30:49.622891+00:00_

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

_source line 1119 · 2026-05-23T13:30:49.925314+00:00_

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
12	  last_seen_round: 13
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
35	  action_items:
36	    - round: 6
37	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
38	      assigned_to: "paper"

…[truncated 32556 chars]

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


### Tool call

_source line 1120 · 2026-05-23T13:31:12.551171+00:00_

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

_source line 1121 · 2026-05-23T13:31:33.529982+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20978
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-23T13:31:33.681714+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- 路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_12/submitted.pdf\n\n## Venue 要求 (EMNLP 2026 via ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页（long paper），参考文献不限。Limitations 章节和 ethical considerations 不计入页数限制（不得含过多额外内容）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind。禁止出现作者姓名和单位，自引不得暴露身份\n- **Limitations**: 必须在正文中有一个 Limitations section（在 Conclusion 之后），appendix 中不得有 Limitations section\n- **ARR Checklist**: 在 OpenReview 提交表单中填写，不在论文 PDF 中\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **统计方法论**：TOST 等价性检验的应用是否正确？±2pp SESOI 阈值是否有充分理由？Holm-Bonferroni 校正是否恰当？Bayesian ROPE 分析与频率学方法的一致性如何？\n2. **实验设计**：seed 覆盖（5 seeds function-level, 2-3 seeds repo-level）是否充分？不同 formulation 之间的 matched comparison 是否公平（特别是 TRAJ 的训练配置差异）？Checkpoint 选择策略是否引入偏差？\n3. **Threats to validity**：论文识别的 5 个潜在混淆变量是否充分？是否有遗漏？Confound 的估计是否可信？\n4. **统计功效**：power ~0.3 对结论的影响评估是否充分？Abstract/Conclusion 的 hedging 是否与实际统计功效匹配？\n5. **可复现性**：实验设置描述是否足够详细？超参数是否完整？\n\n请按 ARR 审稿标准给出完整审稿意见，包括：Summary (2-3句), Strengths (逐条), Weaknesses (逐条，标注 Must-Fix / Should-Fix / Minor), Questions, Missing References, 以及以下维度评分 (1-5): Soundness, Excitement, Overall Assessment (按 EMNLP 评分标准)。"
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
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- 路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_12/submitted.pdf\n\n## Venue 要求 (EMNLP 2026 via ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页（long paper），参考文献不限。Limitations 章节和 ethical considerations 不计入页数限制（不得含过多额外内容）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind。禁止出现作者姓名和单位，自引不得暴露身份\n- **Limitations**: 必须在正文中有一个 Limitations section（在 Conclusion 之后），appendix 中不得有 Limitations section\n- **ARR Checklist**: 在 OpenReview 提交表单中填写，不在论文 PDF 中\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **统计方法论**：TOST 等价性检验的应用是否正确？±2pp SESOI 阈值是否有充分理由？Holm-Bonferroni 校正是否恰当？Bayesian ROPE 分析与频率学方法的一致性如何？\n2. **实验设计**：seed 覆盖（5 seeds function-level, 2-3 seeds repo-level）是否充分？不同 formulation 之间的 matched comparison 是否公平（特别是 TRAJ 的训练配置差异）？Checkpoint 选择策略是否引入偏差？\n3. **Threats to validity**：论文识别的 5 个潜在混淆变量是否充分？是否有遗漏？Confound 的估计是否可信？\n4. **统计功效**：power ~0.3 对结论的影响评估是否充分？Abstract/Conclusion 的 hedging 是否与实际统计功效匹配？\n5. **可复现性**：实验设置描述是否足够详细？超参数是否完整？\n\n请按 ARR 审稿标准给出完整审稿意见，包括：Summary (2-3句), Strengths (逐条), Weaknesses (逐条，标注 Must-Fix / Should-Fix / Minor), Questions, Missing References, 以及以下维度评分 (1-5): Soundness, Excitement, Overall Assessment (按 EMNLP 评分标准)。"
  }
}
```

</details>

---


### Tool result

_source line 1123 · 2026-05-23T13:31:45.239988+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11558
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-23T13:31:45.391016+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- 路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_12/submitted.pdf\n\n## Venue 要求 (EMNLP 2026 via ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页（long paper），参考文献不限。Limitations 章节和 ethical considerations 不计入页数限制（不得含过多额外内容）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind。禁止出现作者姓名和单位，自引不得暴露身份\n- **Limitations**: 必须在正文中有一个 Limitations section（在 Conclusion 之后），appendix 中不得有 Limitations section\n- **ARR Checklist**: 在 OpenReview 提交表单中填写，不在论文 PDF 中\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性与贡献**：核心贡献（\"systematic comparison\"）是否足够支撑一篇 EMNLP 论文？论文提出了什么 surprising findings？这些发现是否可以从先验知识预测？Failure mode taxonomy 是否有独立价值？\n2. **Related Work 覆盖**：是否遗漏重要相关工作？与 GenRM、CRUXEval、CodeRM 等的关系讨论是否充分？PRM/ORM 映射是否清晰？\n3. **写作质量**：叙事结构是否清晰？Abstract 是否准确反映论文贡献？Claim 与 evidence 的对齐度如何？是否存在 overclaim？\n4. **Framing**：三层结构（fine-tuning necessary → function-level equivalence → repo-level divergence）是否有效传达？论文的 positioning（empirical comparison vs. methodology contribution）是否合适？\n5. **格式合规**：8 页限制是否满足？Limitations section 位置是否正确？匿名规则是否遵守？图表质量如何？\n\n请按 ARR 审稿标准给出完整审稿意见，包括：Summary (2-3句), Strengths (逐条), Weaknesses (逐条，标注 Must-Fix / Should-Fix / Minor), Questions, Missing References, 以及以下维度评分 (1-5): Soundness, Excitement, Overall Assessment (按 EMNLP 评分标准)。"
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
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- 路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_12/submitted.pdf\n\n## Venue 要求 (EMNLP 2026 via ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页（long paper），参考文献不限。Limitations 章节和 ethical considerations 不计入页数限制（不得含过多额外内容）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind。禁止出现作者姓名和单位，自引不得暴露身份\n- **Limitations**: 必须在正文中有一个 Limitations section（在 Conclusion 之后），appendix 中不得有 Limitations section\n- **ARR Checklist**: 在 OpenReview 提交表单中填写，不在论文 PDF 中\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性与贡献**：核心贡献（\"systematic comparison\"）是否足够支撑一篇 EMNLP 论文？论文提出了什么 surprising findings？这些发现是否可以从先验知识预测？Failure mode taxonomy 是否有独立价值？\n2. **Related Work 覆盖**：是否遗漏重要相关工作？与 GenRM、CRUXEval、CodeRM 等的关系讨论是否充分？PRM/ORM 映射是否清晰？\n3. **写作质量**：叙事结构是否清晰？Abstract 是否准确反映论文贡献？Claim 与 evidence 的对齐度如何？是否存在 overclaim？\n4. **Framing**：三层结构（fine-tuning necessary → function-level equivalence → repo-level divergence）是否有效传达？论文的 positioning（empirical comparison vs. methodology contribution）是否合适？\n5. **格式合规**：8 页限制是否满足？Limitations section 位置是否正确？匿名规则是否遵守？图表质量如何？\n\n请按 ARR 审稿标准给出完整审稿意见，包括：Summary (2-3句), Strengths (逐条), Weaknesses (逐条，标注 Must-Fix / Should-Fix / Minor), Questions, Missing References, 以及以下维度评分 (1-5): Soundness, Excitement, Overall Assessment (按 EMNLP 评分标准)。"
  }
}
```

</details>

---


### Tool result

_source line 1125 · 2026-05-23T13:31:46.776046+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1385
}
```

</details>

---


### Assistant

_source line 1126 · 2026-05-23T13:32:00.864746+00:00_

Round 1 已启动：

- **视觉审查 Agent**：已派发，与 Reviewer 并行执行
- **Reviewer 1**（方法严谨性 + 实验有效性）：已分配
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：已分配

等待两位 Reviewer 返回独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 101

## Round 101

2 recorded events


### User

_source line 1127 · 2026-05-23T13:37:04.054051+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿意见

**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 总体评分

**Overall**: 3.0 / 5 — Findings
**一句话总结**: 方法论严谨的实证比较，但核心发现（CWM 在 repo level 因 format collapse 崩溃）可从论文自身的理论分析（§2.2）预测，且仅在 ≤8B 规模下成立，新颖性和实用价值有限。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 统计方法论优秀（TOST、ICC、clustered bootstrap、Holm-Bonferroni），但 repo-level 结果受多个 confound 影响（§3.5 自列 5 个），CWM 的 seed 配置不一致削弱了因果推断 |
| Excitement | 2.5 / 5 | 实验执行扎实，但核心发现——生成长序列比单 token 分类更难——可从第一性原理预测；14B 收敛趋势暗示该差异是 capacity 不足的表现而非 formulation 的固有属性 |
| Reproducibility | 4 / 5 | Hyperparameter、prompt template、seed 配置均在附录详细报告；数据集使用公开 benchmark；唯一不足是缺少代码/checkpoint release 承诺 |
| Confidence | 4 / 5 | 我熟悉代码修复、execution prediction、reward modeling 相关工作 |
| Overall Assessment | 3.0 / 5 | Findings 水平——方法论贡献（matched comparison framework）有价值，但发现的 surprise factor 不足以达到主会议标准 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心发现的新颖性存疑——理论预测先于实验结果

- 具体位置：§2.2 Expected Failure Modes → §3.4 Repo-Level Results
- 问题：论文的核心实验发现是"CWM 在 repo level 因 format collapse 崩溃，CLS 优势 18–26pp"。但 §2.2 已经从理论上预测了这一结果：token 序列精确匹配概率为 $q^L$，长输出"exponentially harder to predict exactly"。如果作者能从第一性原理推导出实验结论，那么实验验证的价值更接近"confirmation"而非"discovery"。论文需要更清楚地阐述：实验中哪些发现是 §2.2 理论**无法**预测的？例如，format collapse（模型根本无法生成合规格式）是否在 §2.2 的预测范围内？如果是（§2.2 确实列出了 format compliance collapse 作为第三种失败模式），那么整篇论文的实验贡献需要重新定位。
- 为什么影响接收：如果核心发现可预测，excitement 维度会显著降低。一个严谨的 confirmation study 在 Findings 可以接受，但如果定位为"first systematic comparison"暗示发现了新规律，则 framing 有误。
- 建议修改方向：(1) 明确区分 §2.2 可预测的部分和实验中真正 surprising 的发现（如 format collapse 的具体比例、aggregation penalty 的量化特征、CLS-TRAJ 模型依赖性等）；(2) 或将论文定位从"what we discovered"转向"what we rigorously quantified and the methodology for doing so"。

**N2** [critical] CWM baseline 的公平性问题——≤8B LoRA vs. 原版 32B 预训练

- 具体位置：§3.1 "Our CWM baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model"
- 问题：论文全文使用"CWM"标签，但实际实现是 4–8B 模型的 LoRA 微调，而非原始 CWM 论文的 32B 规模 + execution-trace 预训练。这两者在 capacity 和 pretraining data 上差异巨大。论文在 repo level 发现的 format collapse（53–74% unparseable）很可能主要是 capacity 不足的表现，而非 generation formulation 的固有缺陷。论文自己的 scaling 数据（§3.3，14B 时三种 formulation 收敛到 1.07pp 以内）也支持这一解读。但 abstract 和 introduction 的 framing 倾向于将其描述为 formulation 层面的差异（"the CLS–CWM gap widens to 18–26pp...driven by format collapse"），这对读者有误导。
- 为什么影响接收：如果差异主要来自 capacity 而非 formulation，论文的核心对比（"systematic comparison of formulations"）的效度存疑。
- 建议修改方向：(1) 在 abstract/intro 中更显著地 qualify：repo-level divergence 是在 ≤8B regime 下的观察，14B scaling 趋势暗示 capacity 可能是主要因素；(2) 明确讨论：如果 32B CWM 不出现 format collapse，论文的 formulation comparison 结论如何修正？(3) 考虑将 CWM baseline 更明确地称为"CWM-style fine-tuned at ≤8B scale"而非直接使用"CWM"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Repo-level CWM 的 seed/checkpoint 配置不一致

- 具体位置：Table 3 脚注 "CWM uses final-epoch checkpoint (step 6633) for s123/s456; s42 uses an earlier checkpoint (step 400) from a prior training configuration. Val loss is undefined for DeepSeek CWM runs."
- 问题：三个 seed 中有一个使用了不同训练配置的早期 checkpoint，且 DeepSeek CWM 的 val loss 完全不可用。这种配置异质性使得 repo-level CWM 结果的可靠性大打折扣。如果 s42 使用的是 step 400（仅 ~6% 的训练），其 format collapse 程度可能因此更严重或更轻。
- 建议：(1) 明确报告 s42 vs. s123/s456 的分别结果；(2) 讨论配置差异对结论的影响；或 (3) 将 s42 标记为 pilot/exploratory 而非与其他 seed 等同分析。

**W2** [warning] CLS-TRAJ 对比的实验设计存在根本性 confound

- 具体位置：§3.4 "The CLS-TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity (per-test vs. variant-level), a formulation-inherent confound that cannot be experimentally resolved."
- 问题：论文承认 CLS 和 TRAJ 在训练数据粒度上存在无法消除的 confound（CLS 用 per-test labels，TRAJ 用 variant-level labels），这意味着 CLS 的优势可能来自 label granularity 而非 formulation 本身。论文在 contribution 列表中将 TRAJ 作为"granularity control"（§2.1），但如果 confound 无法分离，这个 control 的有效性存疑。
- 建议：更明确地讨论 label granularity confound 的方向性——如果 TRAJ 被提供 per-test labels（虽然它不利用），性能是否会变？是否有实验设计可以部分分离这个 confound？

**W3** [warning] Error complementarity 的实用价值不清

- 具体位置：§3.6 "Simple routing heuristics capture <0.4pp of this gap, framing complementarity as motivation for future learned routers"
- 问题：Oracle routing 的上界（+2.80pp function, +14.58pp repo）很吸引人，但所有尝试的 heuristic 都 capture <0.4pp。论文将此定位为"future work motivation"，但没有提供任何证据表明 learned router 是可行的。在没有 feasibility signal 的情况下，这个 finding 的 actionability 接近零。
- 建议：至少提供一个简单的 learned router 实验（e.g., logistic regression on instance features），或在 oracle 分析中提供更多关于互补性来源的分析（哪些 instance 特征预测 CLS 优于 CWM？），使这个方向更 concrete。

**W4** [warning] Related Work 对 PRM/ORM 映射的讨论需要更精确

- 具体位置：§4 "CLS corresponds to process-level (PRM-like) verification while TRAJ provides outcome-level (ORM-like) feedback; CWM serves as a generative verifier"
- 问题：这个映射有 subtlety 被忽略。PRM 在 math reasoning 中是 per-step reward（推理步骤级别），而 CLS 是 per-test reward（测试用例级别）——这两者的粒度不同。CodeRM (Ma et al., 2025) 的 test-level reward 更接近 CLS，但论文未深入讨论 CLS 与 CodeRM 的区别（CodeRM 是 reward model 用于 generation reranking，CLS 是 verification formulation 用于 pass/fail prediction）。此外，GenRM 和 GenPRM 的对比讨论虽然存在，但可以更深入：为什么 generative verifier 在 math 中优于 discriminative 但在 code 中不是？论文提到"output structure"是原因，但未展开分析 math output 和 code output 在结构上的具体差异。
- 建议：(1) 更精确地讨论 PRM/CLS/CodeRM 之间的粒度差异；(2) 展开 math vs. code 的结构性差异分析（math output 通常短且有固定格式，code execution output 长度和格式变化大）。

---

## 小问题（不影响接收）

- **M1**: Figure 2 caption 称 "inverted-U trajectory"，但仅有 3 个数据点（4B, 8B, 14B），无法可靠地判断曲线形状。建议改为 "non-monotonic pattern" 或移除 trajectory 相关描述。
- **M2**: Abstract 中 $z=-23.7$ 和 "18–26pp" 同时出现，但 $z$ 值来自 mixed-effects LPM interaction term（§3.4），而 18–26pp 是直接的 accuracy gap。这两个数字描述的是不同统计量，并列使用可能让读者误以为 $z$ 是 gap 的检验统计量。建议在 abstract 中仅保留一个，在正文中解释它们的关系。
- **M3**: §3.1 提到 "Seeds 789/0 use NormalFloat 4-bit (NF4) quantization to test robustness to precision reduction"。将 precision ablation 混入主实验的 seed pool 而非单独报告，可能引入不必要的噪声。虽然脚注说 "function-level accuracy remains within seed noise"，但如果某些分析子集（如 TOST）只用 3 个 seed，那么 precision 差异的影响可能被放大。
- **M4**: Table 3 同时报告 per-test accuracy 和 variant-level accuracy，但列名使用缩写（"Var."），对不熟悉 SWE-bench 的读者不够清晰。
- **M5**: Limitations 章节简洁得当（3 个点），符合 venue 要求。

---

## 缺失引用

- **CodeBERTScore** (Zhou et al., 2023): 已引用，但仅一次且在 Related Work 列表中。考虑到 CodeBERTScore 也是 execution-free 的代码评估方法，可以在 formulation taxonomy 中讨论它为什么被排除（它不是 verification formulation 而是 metric）。
- **RLTF** (Liu et al., 2023): 使用 execution feedback 训练 code generation 的 RL 方法，与论文的 execution-free 方向形成对比。
- **StarCoder2-Instruct** (Lozhkov et al., 2024): 近期 code LLM，论文仅用 Qwen3 和 DeepSeek-Coder，讨论 model family 泛化性时可引用更多 code LLMs。
- 整体来说，Related Work 覆盖较完整，主要遗漏在 code evaluation metrics 与 verification formulation 的边界讨论上。

---

## 主要优势

1. **统计方法论标杆级**: TOST 等价检验 + Holm-Bonferroni 校正 + ICC + clustered bootstrap + Bayesian ROPE，这在 NLP 实证论文中极为罕见，值得肯定。
2. **诚实的局限性标注**: 论文对 power 不足（~0.3）、confound 列表（§3.5）、exploratory analyses 的标注非常透明，显著提高了可信度。
3. **Failure mode taxonomy 有独立价值**: format collapse / decision collapse / aggregation penalty 的三分类为实践者提供了可操作的诊断框架（Table 4）。
4. **三层叙事结构有效**: fine-tuning necessary → function-level equivalence → repo-level divergence，逻辑层层递进，读者容易跟随。
5. **Matched experimental design**: 控制 model family、capacity、training data、seed，isolate formulation effect——这是同类工作中少见的严谨设计。

---

## Questions for Authors

1. 如果在 32B+ 规模下 CWM 的 format collapse 消失（如 14B 的收敛趋势所暗示），您如何修正论文的核心 claim？论文是否本质上是关于"capacity moderates formulation choice"而非"complexity moderates formulation choice"？
2. §2.2 的 Expected Failure Modes 在实验之前就预测了 repo-level CWM 的崩溃。实验中是否有任何发现**违反**了 §2.2 的预测？如果没有，论文的实验贡献如何区别于 confirmation study？
3. CWM s42 使用 step 400 checkpoint 而 s123/s456 使用 step 6633，这两者的 format collapse 率和 parseable-only accuracy 是否有显著差异？
4. Error complementarity 的 oracle gap 在 repo level 达 14.58pp，但 heuristic routing 仅 capture <0.4pp。是否分析过互补实例的特征？哪些 instance-level features 预测了 CLS vs. CWM 的优势？


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

_source line 1128 · 2026-05-23T13:37:42.219621+00:00_

收到 Reviewer 2 初审意见。

R2 核心发现：Overall 3.0 (Findings)，主攻新颖性不足——认为 §2.2 理论预测先于实验结论（N1），CWM baseline 公平性存疑因 ≤8B LoRA vs 原版 32B（N2）。4 个 should-fix（seed 不一致 W1、CLS-TRAJ confound W2、complementarity 无 feasibility signal W3、PRM/ORM 映射粗糙 W4）。统计方法论给予高度肯定。

等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 102

## Round 102

30 recorded events


### User

_source line 1129 · 2026-05-23T13:37:44.766752+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿摘要**：

- **Overall: 3.0/5（Findings）**，Soundness 3.5，Excitement 2.5
- **2 个 Must-Fix**：(1) 核心发现（CWM repo-level 崩溃）可从论文自身 §2.2 的理论分析预测，新颖性定位需调整；(2) CWM baseline 是 ≤8B LoRA 微调而非原版 32B，14B 收敛趋势暗示差异可能主要源于 capacity 而非 formulation，framing 有误导
- **4 个 Should-Fix**：CWM seed/checkpoint 配置不一致、CLS-TRAJ confound 无法分离、error complementarity 无实用 signal、PRM/ORM 映射不够精确
- **主要优势**：统计方法论极为严谨（TOST+Holm+ICC+Bayesian ROPE）、failure mode taxonomy 有独立价值、三层叙事结构清晰、confound 标注透明

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

_source line 1130 · 2026-05-23T13:38:05.784903+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "4"
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1131 · 2026-05-23T13:38:05.835680+00:00_



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

_source line 1132 · 2026-05-23T13:38:08.045506+00:00_

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

_source line 1133 · 2026-05-23T13:38:08.899250+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (266 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D13
…[truncated 1825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1134 · 2026-05-23T13:38:26.071176+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_round_12/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_round_12/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1135 · 2026-05-23T13:38:26.322639+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_12/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1136 · 2026-05-23T13:38:26.323084+00:00_

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

_source line 1137 · 2026-05-23T13:38:26.524149+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-23T13:38:26.524577+00:00_

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

_source line 1139 · 2026-05-23T13:38:26.575264+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T13:31:16.142786+00:00\", \"completed_at\": \"2026-05-23T13:34:48.304453+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本（Abstract + Introduction），首个视觉锚点（Figure 1）延迟到 page 3。审稿人前 2 页只看到密集文字，缺少快速锚定的概念图或 teaser result。考虑将 Figure 1 或一个 teaser table 提前到 page 2\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 三面板概念图清晰可读，颜色区分度好，caption 自包含。作为首个 display item 信息传达有效\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 折线图 y 轴起始约 83%（非零起点），适合放大差异展示 scaling gap。三条线颜色可区分（蓝/橙/绿），shaded gap region 辅助理解核心发现\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 + Figure 2 同页，display item 密度高但布局不拥挤，空间利用高效\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 booktabs 风格，最优值加粗，小数位一致（2位），格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 3 格式规范，booktabs 风格一致\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 4（failure mode taxonomy）格式清晰，四列结构合理\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"单页包含 Related Work 结尾 + Conclusion + Limitations + References 开头，密度高但各 section 长度合理，无拥挤感。Limitations 简短（约 1/3 栏），符合 EMNLP 要求\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Conclusion 约 2/3 栏，简洁有力，三条 directions 结构清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 9-11\", \"message\": \"References 格式统一，无 [?] 未解析引用，无跳号，排版正常\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 3 单栏宽度 bar chart，标签字号偏小但仍可读；Table 5 booktabs 格式一致\"}, {\"severity\": \"info\", \"dimension\": \"page 13-14\", \"message\": \"Appendix 表格（Tables 7-10）格式规范，最优值加粗\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Table 11（Training Hyperparameters）信息密集但排版清晰，双层表头结构合理\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"messa
…[truncated 580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-23T13:38:37.270715+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1141 · 2026-05-23T13:38:37.672851+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_11.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1142 · 2026-05-23T13:38:37.874615+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Reviewer 1",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts",
  "output_mode": "files_with_matches"
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
    "pattern": "Reviewer 1",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 1143 · 2026-05-23T13:38:37.975633+00:00_

Found 15 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260518T171503/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260518T171503/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260518T171503/worst/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260518T171503/logs/review_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260517T034206/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260516T150201/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260516T073712/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260516T073712/logs/review_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/worst/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/median/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_
…[truncated 259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1144 · 2026-05-23T13:39:11.542939+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_round_12/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_round_12/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 1145 · 2026-05-23T13:39:12.496978+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_12/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1146 · 2026-05-23T13:39:12.497461+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1147 · 2026-05-23T13:39:12.698479+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1148 · 2026-05-23T13:39:48.092250+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
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
    "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1149 · 2026-05-23T13:39:48.092636+00:00_



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

_source line 1150 · 2026-05-23T13:39:50.401268+00:00_

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

_source line 1151 · 2026-05-23T13:39:50.452015+00:00_

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

_source line 1152 · 2026-05-23T13:39:53.516627+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
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
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-23T13:39:53.567450+00:00_



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

_source line 1154 · 2026-05-23T13:39:57.484470+00:00_

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

_source line 1155 · 2026-05-23T13:39:57.787535+00:00_

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
12	  last_seen_round: 13
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
35	  action_items:
36	    - round: 6
37	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
38	      assigned_to: "paper"

…[truncated 32556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-23T13:40:18.381525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_11.md",
  "limit": "50"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_11.md",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1157 · 2026-05-23T13:40:18.382014+00:00_

1	---
2	round: 11
3	review_mode: fresh
4	overall_score: 3.0 - Findings
5	timestamp: 2026-05-23T12:56:38.274376+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	
12	# Round 13 审稿报告（Fresh Review）
13	
14	**投稿**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
15	**Venue**: EMNLP 2026 (ARR May cycle)
16	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性/贡献+完整性）
17	**轮次**: Round 13 (Fresh Review)，1 轮独立审稿 + 1 轮交叉分享
18	
19	---
20	
21	## Summary
22	
23	本文首次在匹配条件下系统比较了 LLM 代码修复中三种 execution-free 验证公式（CLS 分类、CWM 生成、TRAJ 轨迹级），跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别和多个 seeds。核心发现为三层结构：(1) fine-tuning 必要（35-36pp 增益）；(2) function-level 三种公式近等价（CLS-CWM TOST 确认，CLS-TRAJ Holm 校正后未确认但 gap 单调收窄至 1.07pp@14B）；(3) repo-level 在 ≤8B LoRA 下等价崩塌（CLS-CWM gap 18-26pp，由 CWM format collapse 驱动）。论文同时提供了 failure mode taxonomy 和 error complementarity 分析。
24	
25	---
26	
27	## Strengths
28	
29	**S1. 首个匹配条件的系统比较。** 控制模型容量、训练数据、超参数和评估协议进行三方公式比较，直接回答从业者的 formulation 选择问题。Cross-family 一致性（Qwen3 和 DeepSeek-Coder 在 CLS-CWM 差异方向一致）增强结论可信度。[两人共识]
30	
31	**S2. 统计框架出色。** TOST 等价检验 + Bayesian ROPE 双验证、clustered bootstrap（114 clusters, 10K resamples）、Holm-Bonferroni 校正（k=5）、ICC/DEFF 修正——在 NLP 实证论文中属上乘水准。特别是 §3.4 明确区分"等价"与"未能拒绝差异"，CLS-CWM 等价在多个统计方法下一致（TOST p=0.007; P(ROPE)=0.975）。[两人共识, R1 Soundness 3.5, R2 Soundness 4.0]
32	
33	**S3. 透明的混淆因素分析。** §3.7 和 Appendix O 明确列出并量化 5 个 confounds，包括 preprocessing-checkpoint 链式影响（7.68pp）和 worst-case compounding 分析（±11.5pp）。CLS-TRAJ 等价在 Holm 校正后不成立也被如实报告。[两人共识]
34	
35	**S4. 实用的 failure mode taxonomy。** Table 4 的三类失败模式（format collapse, decision collapse, aggregation penalty）提供可迁移的诊断框架，对实践者有直接价值。R1 认为此贡献可独立于三方比较使用。[两人共识]
36	
37	**S5. GenRM 领域特异性观察。** 代码验证中 generation ≤ discrimination（与 GenRM 在数学推理中的发现相反）是一个有价值的数据点，暗示 generation advantage 可能是 domain-dependent 的。[两人共识, 但均认为分析不够深入]
38	
39	**S6. Related Work 覆盖充分。** CodeScaler, Aletheia, GenRM, GenPRM, FunPRM, CodeRM 均已引用。两位 Reviewer 均未发现 2025-2026
…[truncated 437 chars]

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


### Assistant

_source line 1158 · 2026-05-23T13:41:09.826664+00:00_

当前状态：

- **Reviewer 2**：已收到（Overall 3.0/5 Findings）
- **Reviewer 1**：由于对话上下文压缩，我丢失了 Reviewer 1 的审稿内容
- **视觉审查**：已完成（1 warning: 前两页缺视觉锚点，16 info）
- **外部审稿**：未请求
- **Issue Tracker**：已追踪至 Round 13，所有 issue 已 resolved

这是 Round 14（fresh review）。Reviewer 1 是否已提交审稿？如果已提交，请将 R1 的审稿意见重新发送给我——我需要完整原文才能进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 103

## Round 103

6 recorded events


### User

_source line 1159 · 2026-05-23T13:41:09.832416+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（Round 1）
**侧重：方法严谨性 + 实验有效性**

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 方法论严谨度在 NLP 实证论文中属上乘，但 SESOI 阈值缺乏预注册且结果对其敏感、repo-level 统计功效严重不足、TRAJ 配置非对称性这三个问题共同削弱了核心结论的可信度。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | TOST+ROPE+Holm-Bonferroni 框架选择正确，但 ±2pp SESOI 未预注册且结果对其敏感（±1.5pp 即失效）；repo-level 仅 2-3 seeds、power~0.08-0.3，难以支撑因果性结论 |
| Excitement | 3/5 | 研究问题实用、failure mode taxonomy 有操作价值，但核心发现（短输出时 formulation 无差异、长输出时 generation 崩溃）在概念上可预期 |
| Reproducibility | 4/5 | 超参数完整（Table 11/Appendix E）、prompt template 提供、compute budget 明确；但代码未附、部分 TRAJ 预测未归档导致 unpaired bootstrap |
| Overall Assessment | 3.5 | Borderline Conference — 方法论贡献真实但受限于实验规模和配置非对称性 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] ±2pp SESOI 阈值缺乏预注册且结论对其高度敏感

- 具体位置：§3.4 第2段、Table G (Appendix G)
- 问题：论文承认 SESOI "was not pre-registered"（§3.4），声称 2pp 对应 "~2-3 problems out of 114, below practitioner-relevant differences"。但 Table G 的敏感性分析显示：±1.52pp 时 p 恰好为 0.05（最小可确认等价的 margin），±1.5pp 时 p=0.054 即失效。核心 CLS-CWM 等价性结论的鲁棒窗口仅为 0.48pp（2.00-1.52）。论文将 2pp 与 between-seed std (0.37-0.97pp) 对比作为合理性论证，但这一比较反而暗示更窄的 SESOI（如 ±1pp）可能更合理，此时等价性将不成立。
- 为什么影响接收：等价性检验的结论本质上取决于 SESOI 的选择。当 SESOI 未预注册且结果对其敏感时，存在 "先看数据再选阈值" 的方法论风险。即使作者意图上没有这样做，审稿人无法排除这一可能性。
- 建议修改方向：(1) 在 §3.4 明确讨论 SESOI 选择的敏感性，承认 ±1.5pp 以下等价性不成立；(2) 提供基于独立标准（如已有 code repair 文献中的 MDE、工业 deployment 阈值）的 SESOI 辩护；(3) 考虑将等价性结论弱化为 "are statistically equivalent under a ±2pp margin that, while reasonable, was not pre-registered"。

**N2** [critical] Repo-level 因果归因缺乏充分统计支撑

- 具体位置：§3.5、Abstract（"this equivalence collapses (z=−23.7)"）、Conclusion 第1段、Appendix N
- 问题：Repo-level 分析存在三层支撑不足：
  - (a) Seed 覆盖：仅 2-3 seeds per model（Table 3），variant-level n=48，MDE~25pp（Appendix H）。CLS-CWM gap (29-35pp) 刚过 MDE 阈值；
  - (b) 混淆变量叠加：论文识别 5 个 confounds（Appendix N），估计 worst-case compounding ~11.5pp，声称 gap 仍有 ≥7.5pp margin。但 "worst-case compounding" 的估算本身依赖于非正式量化，未进行正式的 sensitivity analysis（如 Rosenbaum bounds）；
  - (c) LPM 的 z=-23.7 来自 n=56,480 per-test observations 但仅 139 problem clusters。GEE 对 model identity 效应给出 p=0.449 vs LPM p=0.002（Appendix J），表明 cluster-robust 推断下次要效应不可靠。
  Abstract 和 Conclusion 用 "collapses" 和 "z=-23.7" 表述，给读者的印象是因果性确认，但实际上更接近 "在多重混淆变量下的观察性关联"。
- 建议：(1) Abstract/Conclusion 将 repo-level 发现标注为 "observational divergence under our ≤8B LoRA protocol with limited seed coverage"；(2) §3.5 开头增加 caveat。

**N3** [critical] TRAJ 配置非对称性使 "matched comparison" 主张不成立

- 具体位置：Table 11 (Appendix E)、§3.5、Appendix N "TRAJ training regime"
- 问题：论文在 Abstract/§1 多次强调 "matched experimental framework"，但 TRAJ 的训练配置与 CLS/CWM 存在系统性差异：lr 4倍差异（2×10⁻⁴ vs 5×10⁻⁵）、训练数据量 175 倍差异（~400 vs ~70K）、标签粒度不可控。Downsample ablation 控制了数据量但未控制 lr 和标签粒度。
- 建议：(1) 将 "matched" 限定为 "matched for CLS and CWM; TRAJ comparison is exploratory"；(2) 在 Table 1 和 Table 3 中视觉区分 CLS/CWM（matched）和 TRAJ（non-matched）。

## Should-Fix 问题

**W1** [warning] CWM default-to-pass 使 repo-level 准确率失真
- Table 3 的 CWM 58-66% 准确率中有大比例来自 trivial majority baseline（53-74% unparseable → default pass）。Appendix K 揭示 unparseable instances 有更高 pass rate（74.6% vs 68.3%），default 策略系统性偏向正确。建议在 Table 3 增加 "Parseable Acc (%)" 列。

**W2** [warning] 14B 收敛观察的 hedging 不一致
- Abstract "preliminary observation" 是恰当的，但 §3.3 用 "capacity-dependent convergence at function level" 作为结论性措辞，df=2 时 power~0.08 在正文中未提及。建议 §3.3 添加 power 的定量 caveat。

**W3** [warning] Function-level ICC=0.191 外推至 Oracle 分析
- Repo-level ICC=0.3146，两者差 65%。对 TOST 功效而言使用 function-level ICC 高估了 effective sample size。建议区分两个 ICC 的使用场景。

**W4** [warning] 缺少 TOST one-sided p-values 报告
- 论文仅报告 TOST 的 max(p_upper, p_lower)，未报告两个 one-sided p 值。对 CLS-TRAJ non-confirmation 的诊断有价值。建议在 Appendix G 补充。

## 小问题
- §2.3 Oracle framework 的 k_eff 假设 exchangeable correlation，repo-level tests 可能有更复杂的相关结构，值得脚注。
- Table 1 的 TRAJ "★" 标记不够醒目。
- Figure 2 caption 应标注 "y-axis does not start at zero"。
- §3.6 引用 Appendix 的编号系统不一致。

## 主要优势
1. 统计方法论的严谨性在 NLP 领域罕见（TOST + Bayesian ROPE + Holm-Bonferroni + clustered bootstrap），框架本身值得推广。
2. 保守报告策略：系统性选择更保守的分析路径（seed-level TOST 而非 problem-level bootstrap），体现方法论诚信。
3. Failure mode taxonomy（format collapse / decision collapse / aggregation penalty）直接对应部署决策，有实践指导价值。
4. 四项 failed interventions 的负面结果报告增强了 format collapse 结论的可信度。
5. Threats to validity 约 6 页（~27% appendix），全面性异常高。

## Questions for Authors
1. 是否考虑过使用更窄的 SESOI（如 ±1pp）并接受等价性不确认？
2. TRAJ 使用 lr=2×10⁻⁴ 的理由是 "due to the smaller training set"，为什么不将 TRAJ 的 lr 也设为 5×10⁻⁵ 并增加 epochs？
3. LPM 的 z=-23.7 是否使用了 problem-level cluster-robust SE？139 clusters 的有效 df 是否足够？
4. CWM default-to-pass 是否考虑过替代方案（如 default-to-fail 或 abstain）？

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：给出 **Overall 3.5 (Borderline Conference)**。识别了 3 个 Must-Fix 问题：(1) ±2pp SESOI 未预注册且结论对其敏感（±1.52pp 即为边界），(2) repo-level 因果归因在仅 2-3 seeds + 5 个混淆变量下过于强势（"collapses" 措辞需弱化），(3) TRAJ 配置非对称性使 "matched comparison" 主张不成立。同时肯定了论文在统计方法论严谨性、保守报告策略、failure mode taxonomy 等方面的显著优势。

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

_source line 1160 · 2026-05-23T13:42:02.740281+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 2 的审稿意见\n\n请逐条阅读 Reviewer 2 的审稿意见，对每个 Must-Fix 和 Should-Fix 给出 **[AGREE]** 或 **[REBUT]** 回应，附简要理由。\n\n---\n\n**Reviewer 2 — Overall: 3.0/5 (Findings)**\n**侧重：新颖性 + 完整性 + 写作质量**\n\n### Must-Fix\n\n**R2-N1** [critical] 核心发现的新颖性存疑——理论预测先于实验结果\n- §2.2 Expected Failure Modes 已从理论预测 CWM 在 repo level 的崩溃（token 序列精确匹配概率 $q^L$，长输出 \"exponentially harder\"）。实验结论（CWM format collapse 18-26pp gap）可从 §2.2 预测。论文的实验贡献更接近 \"confirmation\" 而非 \"discovery\"。需明确区分 §2.2 可预测的部分和实验中真正 surprising 的发现。\n\n**R2-N2** [critical] CWM baseline 公平性——≤8B LoRA vs 原版 32B 预训练\n- 实际 CWM 是 4-8B LoRA 微调而非 32B CWM 原版。14B function-level 收敛至 1.07pp 暗示差异主要源于 capacity 而非 formulation。Abstract/Introduction framing 倾向于将差异描述为 formulation 层面，对读者有误导。需更显著 qualify 并讨论 32B CWM 不出现 format collapse 时结论如何修正。\n\n### Should-Fix\n\n**R2-W1** [warning] Repo-level CWM 的 seed/checkpoint 配置不一致\n- s42 使用 step 400 checkpoint，s123/s456 使用 step 6633。DeepSeek CWM val loss 不可用。\n\n**R2-W2** [warning] CLS-TRAJ 对比存在根本性 confound\n- 训练数据粒度不同（per-test vs variant-level labels），无法实验消除。CLS 优势可能来自 label granularity 而非 formulation。\n\n**R2-W3** [warning] Error complementarity 无实用信号\n- Oracle routing 上界 +14.58pp，但所有 heuristic <0.4pp。定位为 \"future work motivation\" 但无 feasibility signal。\n\n**R2-W4** [warning] PRM/ORM 映射讨论不够精确\n- CLS→PRM-like 和 TRAJ→ORM-like 的映射忽略了粒度差异。GenRM 在 math 优于 discrimination 但在 code 中不是，原因（\"output structure\"）未展开。\n\n### Minor\n- M1: Figure 2 \"inverted-U trajectory\" 仅 3 数据点\n- M2: Abstract 中 z=-23.7 和 18-26pp 并列可能混淆\n- M3: Precision ablation seeds 混入主 seed pool\n- M4: Table 3 \"Var.\" 列名不清\n\n### 主要优势\n- 统计方法论标杆级（TOST+Holm+ICC+Bayesian ROPE）\n- 诚实的局限性标注\n- Failure mode taxonomy 有独立价值\n- 三层叙事结构有效\n- Matched experimental design\n\n---\n\n请对以上每个 Must-Fix（N1, N2）和 Should-Fix（W1-W4）逐条给出 [AGREE] 或 [REBUT]，并简述理由。对 Minor 可选择性回应。",
  "reviewer_id": "1",
  "project": "exec-sim-repair-verifier",
  "round_number": "1"
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
    "text": "## 交叉分享：Reviewer 2 的审稿意见\n\n请逐条阅读 Reviewer 2 的审稿意见，对每个 Must-Fix 和 Should-Fix 给出 **[AGREE]** 或 **[REBUT]** 回应，附简要理由。\n\n---\n\n**Reviewer 2 — Overall: 3.0/5 (Findings)**\n**侧重：新颖性 + 完整性 + 写作质量**\n\n### Must-Fix\n\n**R2-N1** [critical] 核心发现的新颖性存疑——理论预测先于实验结果\n- §2.2 Expected Failure Modes 已从理论预测 CWM 在 repo level 的崩溃（token 序列精确匹配概率 $q^L$，长输出 \"exponentially harder\"）。实验结论（CWM format collapse 18-26pp gap）可从 §2.2 预测。论文的实验贡献更接近 \"confirmation\" 而非 \"discovery\"。需明确区分 §2.2 可预测的部分和实验中真正 surprising 的发现。\n\n**R2-N2** [critical] CWM baseline 公平性——≤8B LoRA vs 原版 32B 预训练\n- 实际 CWM 是 4-8B LoRA 微调而非 32B CWM 原版。14B function-level 收敛至 1.07pp 暗示差异主要源于 capacity 而非 formulation。Abstract/Introduction framing 倾向于将差异描述为 formulation 层面，对读者有误导。需更显著 qualify 并讨论 32B CWM 不出现 format collapse 时结论如何修正。\n\n### Should-Fix\n\n**R2-W1** [warning] Repo-level CWM 的 seed/checkpoint 配置不一致\n- s42 使用 step 400 checkpoint，s123/s456 使用 step 6633。DeepSeek CWM val loss 不可用。\n\n**R2-W2** [warning] CLS-TRAJ 对比存在根本性 confound\n- 训练数据粒度不同（per-test vs variant-level labels），无法实验消除。CLS 优势可能来自 label granularity 而非 formulation。\n\n**R2-W3** [warning] Error complementarity 无实用信号\n- Oracle routing 上界 +14.58pp，但所有 heuristic <0.4pp。定位为 \"future work motivation\" 但无 feasibility signal。\n\n**R2-W4** [warning] PRM/ORM 映射讨论不够精确\n- CLS→PRM-like 和 TRAJ→ORM-like 的映射忽略了粒度差异。GenRM 在 math 优于 discrimination 但在 code 中不是，原因（\"output structure\"）未展开。\n\n### Minor\n- M1: Figure 2 \"inverted-U trajectory\" 仅 3 数据点\n- M2: Abstract 中 z=-23.7 和 18-26pp 并列可能混淆\n- M3: Precision ablation seeds 混入主 seed pool\n- M4: Table 3 \"Var.\" 列名不清\n\n### 主要优势\n- 统计方法论标杆级（TOST+Holm+ICC+Bayesian ROPE）\n- 诚实的局限性标注\n- Failure mode taxonomy 有独立价值\n- 三层叙事结构有效\n- Matched experimental design\n\n---\n\n请对以上每个 Must-Fix（N1, N2）和 Should-Fix（W1-W4）逐条给出 [AGREE] 或 [REBUT]，并简述理由。对 Minor 可选择性回应。",
    "reviewer_id": "1",
    "project": "exec-sim-repair-verifier",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-23T13:42:24.262702+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21522
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-23T13:42:24.514624+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 1 的审稿意见\n\n请逐条阅读 Reviewer 1 的审稿意见，对每个 Must-Fix 和 Should-Fix 给出 **[AGREE]** 或 **[REBUT]** 回应，附简要理由。\n\n---\n\n**Reviewer 1 — Overall: 3.5/5 (Borderline Conference)**\n**侧重：方法严谨性 + 实验有效性**\n\n### Must-Fix\n\n**R1-N1** [critical] ±2pp SESOI 阈值缺乏预注册且结论对其高度敏感\n- §3.4 承认 SESOI \"was not pre-registered\"。Table G 敏感性分析显示 ±1.52pp 时 p 恰好为 0.05，±1.5pp 时 p=0.054 即失效。鲁棒窗口仅 0.48pp（2.00-1.52）。Between-seed std (0.37-0.97pp) 反而暗示更窄 SESOI 可能更合理。存在 \"先看数据再选阈值\" 的方法论风险。\n\n**R1-N2** [critical] Repo-level 因果归因缺乏充分统计支撑\n- 三层问题：(a) 仅 2-3 seeds，n=48 variants，MDE~25pp；(b) 5 个 confounds 的 worst-case compounding ~11.5pp 估算非正式；(c) LPM z=-23.7 来自 139 clusters，GEE 对 model identity 给出 p=0.449 vs LPM p=0.002。Abstract \"collapses\" 措辞给读者因果确认印象，实际更接近 \"observational divergence\"。\n\n**R1-N3** [critical] TRAJ 配置非对称性使 \"matched comparison\" 主张不成立\n- TRAJ 与 CLS/CWM 存在系统性差异：lr 4倍（2×10⁻⁴ vs 5×10⁻⁵）、数据量 175倍（~400 vs ~70K）、标签粒度不可控。Downsample ablation 仅控制数据量。\"matched\" 应限定为 CLS 和 CWM 之间。\n\n### Should-Fix\n\n**R1-W1** [warning] CWM default-to-pass 使 repo-level 准确率失真\n- 53-74% unparseable → default pass。Appendix K 揭示 unparseable 有更高 pass rate（74.6% vs 68.3%），default 策略系统性偏向正确。建议 Table 3 增加 \"Parseable Acc (%)\" 列。\n\n**R1-W2** [warning] 14B 收敛观察的 hedging 不一致\n- Abstract \"preliminary observation\" 恰当，但 §3.3 用 \"capacity-dependent convergence at function level\" 作为结论性措辞。df=2 power~0.08 未在正文提及。\n\n**R1-W3** [warning] Function-level ICC=0.191 外推至 Oracle 分析\n- Repo-level ICC=0.3146，两者差 65%。对 TOST 功效使用 function-level ICC 高估 effective sample size。\n\n**R1-W4** [warning] 缺少 TOST one-sided p-values 报告\n- 仅报告 max(p_upper, p_lower)，未报告两个 one-sided p 值。对 CLS-TRAJ non-confirmation 诊断有价值。\n\n### Minor\n- §2.3 Oracle k_eff exchangeable correlation 假设\n- Table 1 TRAJ \"★\" 标记不够醒目\n- Figure 2 caption 应标注 y-axis 非零基线\n- §3.6 Appendix 编号不一致\n\n### 主要优势\n- 统计方法论严谨性罕见\n- 保守报告策略体现方法论诚信\n- Failure mode taxonomy 有实践指导价值\n- 四项 failed interventions 负面结果增强 format collapse 结论可信度\n- Threats to validity ~6 页，全面性异常高\n\n---\n\n请对以上每个 Must-Fix（N1, N2, N3）和 Should-Fix（W1-W4）逐条给出 [AGREE] 或 [REBUT]，并简述理由。对 Minor 可选择性回应。",
  "reviewer_id": "2",
  "project": "exec-sim-repair-verifier",
  "round_number": "1"
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
    "text": "## 交叉分享：Reviewer 1 的审稿意见\n\n请逐条阅读 Reviewer 1 的审稿意见，对每个 Must-Fix 和 Should-Fix 给出 **[AGREE]** 或 **[REBUT]** 回应，附简要理由。\n\n---\n\n**Reviewer 1 — Overall: 3.5/5 (Borderline Conference)**\n**侧重：方法严谨性 + 实验有效性**\n\n### Must-Fix\n\n**R1-N1** [critical] ±2pp SESOI 阈值缺乏预注册且结论对其高度敏感\n- §3.4 承认 SESOI \"was not pre-registered\"。Table G 敏感性分析显示 ±1.52pp 时 p 恰好为 0.05，±1.5pp 时 p=0.054 即失效。鲁棒窗口仅 0.48pp（2.00-1.52）。Between-seed std (0.37-0.97pp) 反而暗示更窄 SESOI 可能更合理。存在 \"先看数据再选阈值\" 的方法论风险。\n\n**R1-N2** [critical] Repo-level 因果归因缺乏充分统计支撑\n- 三层问题：(a) 仅 2-3 seeds，n=48 variants，MDE~25pp；(b) 5 个 confounds 的 worst-case compounding ~11.5pp 估算非正式；(c) LPM z=-23.7 来自 139 clusters，GEE 对 model identity 给出 p=0.449 vs LPM p=0.002。Abstract \"collapses\" 措辞给读者因果确认印象，实际更接近 \"observational divergence\"。\n\n**R1-N3** [critical] TRAJ 配置非对称性使 \"matched comparison\" 主张不成立\n- TRAJ 与 CLS/CWM 存在系统性差异：lr 4倍（2×10⁻⁴ vs 5×10⁻⁵）、数据量 175倍（~400 vs ~70K）、标签粒度不可控。Downsample ablation 仅控制数据量。\"matched\" 应限定为 CLS 和 CWM 之间。\n\n### Should-Fix\n\n**R1-W1** [warning] CWM default-to-pass 使 repo-level 准确率失真\n- 53-74% unparseable → default pass。Appendix K 揭示 unparseable 有更高 pass rate（74.6% vs 68.3%），default 策略系统性偏向正确。建议 Table 3 增加 \"Parseable Acc (%)\" 列。\n\n**R1-W2** [warning] 14B 收敛观察的 hedging 不一致\n- Abstract \"preliminary observation\" 恰当，但 §3.3 用 \"capacity-dependent convergence at function level\" 作为结论性措辞。df=2 power~0.08 未在正文提及。\n\n**R1-W3** [warning] Function-level ICC=0.191 外推至 Oracle 分析\n- Repo-level ICC=0.3146，两者差 65%。对 TOST 功效使用 function-level ICC 高估 effective sample size。\n\n**R1-W4** [warning] 缺少 TOST one-sided p-values 报告\n- 仅报告 max(p_upper, p_lower)，未报告两个 one-sided p 值。对 CLS-TRAJ non-confirmation 诊断有价值。\n\n### Minor\n- §2.3 Oracle k_eff exchangeable correlation 假设\n- Table 1 TRAJ \"★\" 标记不够醒目\n- Figure 2 caption 应标注 y-axis 非零基线\n- §3.6 Appendix 编号不一致\n\n### 主要优势\n- 统计方法论严谨性罕见\n- 保守报告策略体现方法论诚信\n- Failure mode taxonomy 有实践指导价值\n- 四项 failed interventions 负面结果增强 format collapse 结论可信度\n- Threats to validity ~6 页，全面性异常高\n\n---\n\n请对以上每个 Must-Fix（N1, N2, N3）和 Should-Fix（W1-W4）逐条给出 [AGREE] 或 [REBUT]，并简述理由。对 Minor 可选择性回应。",
    "reviewer_id": "2",
    "project": "exec-sim-repair-verifier",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-23T13:42:25.996426+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1481
}
```

</details>

---


### Assistant

_source line 1164 · 2026-05-23T13:42:35.534498+00:00_

交叉分享已发送给两位 Reviewer。等待他们的 [AGREE]/[REBUT] 回应后进入报告合成阶段。

当前进度：
- **Reviewer 1** (3.5, Borderline Conference): 3 Must-Fix（SESOI 敏感性、repo-level 因果归因、TRAJ 非对称性）+ 4 Should-Fix
- **Reviewer 2** (3.0, Findings): 2 Must-Fix（新颖性存疑、CWM baseline 公平性）+ 4 Should-Fix
- **视觉审查**: 已完成，1 warning（前2页无视觉锚点）
- **外部审稿**: 未请求

两人共识区域：统计方法论优秀、failure mode taxonomy 有价值、repo-level 结论需更多 hedging。主要分歧预计在 excitement 评分（R1: 3/5 vs R2: 2.5/5）和 novelty 判定上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 104

## Round 104

2 recorded events


### User

_source line 1165 · 2026-05-23T13:46:08.901180+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的交叉回应

### Must-Fix

**[REBUT] R2-N1: 核心发现的新颖性存疑——理论预测先于实验结果**

R2 认为 §2.2 的 q^L 分析已足以预测 CWM 在 repo level 的崩溃，实验仅为 "confirmation"。我认为这一判断过度简化了论文的贡献：

1. **Function-level 等价性是反直觉的**：§2.2 的 q^L 分析同样预测 function-level CWM 应比 CLS 差（只是差距较小），但实验确认了统计等价（TOST p=0.007, Table 1），14B 收窄至 1.07pp。"等价" 的阈值无法从理论推导。
2. **Failure mode taxonomy 是纯经验发现**：format collapse、decision collapse、aggregation penalty 三种模式的具体机制和分布（Appendix C/H）无法从 q^L 推导。
3. **Capacity-dependent convergence 的定量特征**（Figure 2, Table 2）和 formulation×complexity 交互的显著性（LPM z=−23.7）需要实验建立。

不过论文可以更显式地区分 "confirming §2.2" 和 "beyond §2.2" 的发现。**我的判断：降为 Should-Fix**，建议作者标注哪些发现验证预测、哪些超越预测。

---

**[AGREE] R2-N2: CWM baseline 公平性——≤8B LoRA vs 原版 32B 预训练**

R2 的核心论点成立。虽然论文在 Abstract ("under our ≤8B LoRA protocol")、§3.3 (scaling behavior) 和 Limitations 中做了 qualification，但：

1. 14B function-level 收敛至 1.07pp 是重要信号——给足 capacity 后 formulation 差异可能消失
2. Abstract "equivalence collapses" 的措辞暗示 formulation 固有缺陷，而实际可能是 capacity 不足
3. Appendix I 中 LoRA rank 32 和 adapter doubling 均无法修复 format collapse——可能说明 4-8B capacity 不够而非 formulation 缺陷

同意 Must-Fix，但严重程度比 R2 评估的稍低。论文需要：(a) Abstract 更显著 qualify；(b) 在 Limitations 中讨论 "32B+ CWM 是否会消除 format collapse" 作为 open question。

---

### Should-Fix

**[AGREE] R2-W1: Repo-level CWM 的 seed/checkpoint 配置不一致**

s42 用 step 400 checkpoint vs s123/s456 用 step 6633，在 CWM 存在 late-training format degradation 的背景下可能系统性影响 s42。建议报告各 seed 在统一 checkpoint 下的 sensitivity check。

---

**[AGREE] R2-W2: CLS-TRAJ 对比存在根本性 confound**

CLS per-test labels vs TRAJ variant-level labels 的 granularity confound 是真实的。Downsampling ablation (Appendix B) 控制了 data volume 但没有控制 label granularity。建议在 §3.4 或 Limitations 中明确标注此 unresolved confound。

---

**[REBUT] R2-W3: Error complementarity 无实用信号**

不同意。Oracle analysis 的价值在于量化 error complementarity 的存在和分布（Table 5, Figure 3: T≥1 instances 贡献 55.3% 的 advantage），而非提供 practical routing。论文 framing 已经是诚实的（"motivation for future learned routers"），四种 heuristic 全部失败本身是有信息量的 negative result，排除了 naive approaches。篇幅仅占正文 ~1/3 column，定位恰当。

---

**[AGREE] R2-W4: PRM/ORM 映射讨论不够精确**

CLS per-test ≠ PRM per-step（CLS 更接近 multi-label outcome supervision），GenRM 在 code 中未胜出的 "output structure" 解释未展开。建议在 §4 加 1-2 句 qualify 粒度差异。

---

### Minor

- **M1** [AGREE]: 3 data points 不足以支撑 "inverted-U trajectory"，但措辞影响有限
- **M2** [REBUT]: z=−23.7 (交互项统计量) 和 18-26pp (accuracy gap) 有明确 context 区分，并列不混淆
- **M3** [AGREE]: 需确认 precision ablation seeds 与 main seeds 是否独立
- **M4** [AGREE]: Table 3 "Var." 应在 caption 注明全称

---

### 总结

R2 的 Overall 3.0 (Findings) 评分基本合理但略偏保守。两个 Must-Fix 中，N1 我认为应降为 Should-Fix（论文的经验贡献超越纯 confirmation），N2 同意但严重程度稍低（论文已有 qualification，只需加强）。Should-Fix 中，W1/W2/W4 同意，W3 不同意（negative result 有独立价值）。如果 N2 得到充分 qualify，我认为论文可以稳守 3.0-3.5 区间。

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

_source line 1166 · 2026-05-23T13:46:13.732234+00:00_

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


## Round 105

## Round 105

2 recorded events


### User

_source line 1167 · 2026-05-23T13:46:21.162299+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Director。总结：

- **R2-N1**（新颖性存疑）：**[REBUT]**，论文贡献超越纯 confirmation——function-level 等价性、failure mode taxonomy、capacity-dependent convergence 均非理论可预测，建议降为 Should-Fix
- **R2-N2**（CWM baseline 公平性）：**[AGREE]**，≤8B LoRA vs 32B 的 capacity confound 成立，但论文已有部分 qualification，需加强 Abstract 和 Limitations 中的表述
- **R2-W1**（checkpoint 不一致）：**[AGREE]**
- **R2-W2**（label granularity confound）：**[AGREE]**
- **R2-W3**（error complementarity 无实用信号）：**[REBUT]**，negative result 有独立价值，论文 framing 诚实
- **R2-W4**（PRM/ORM 映射不精确）：**[AGREE]**

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

_source line 1168 · 2026-05-23T13:46:26.672993+00:00_

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


## Round 106

## Round 106

54 recorded events


### User

_source line 1169 · 2026-05-23T13:49:57.645624+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应：对 Reviewer 1 审稿意见的逐条评议

已完整阅读论文 PDF（22 页）及 LaTeX 原文，以下逐条回应。

---

### Must-Fix 回应

**[AGREE with downgrade] R1-N1: ±2pp SESOI 阈值缺乏预注册且结论对其高度敏感**

R1 事实核查准确：§3.4 确实承认 "was not pre-registered"；Table G 确认鲁棒窗口仅 0.48pp（±2.00→±1.52pp）；±1.5pp 时 p=0.054 即失效。

但我认为 R1 将此定为 **critical** 过重，建议降为 **Should-Fix**，理由：

1. **论文已主动透明披露**——在正文 §3.4 而非 appendix 中承认未预注册，这在实证 NLP 论文中极为少见，体现方法论诚信。
2. **Bayesian ROPE 独立佐证**——Appendix G.1 报告 P(ROPE)=0.975（CLS–CWM），HDI=[+0.10, +2.00]pp 完全落入 ROPE，这是一个与 TOST 正交的等价性检验，不受 SESOI 选择影响。
3. **阈值有独立于数据的部署合理性**——Appendix G 明确说明 ±2pp 基于 "deployment relevance"（85-88% 准确率下 2pp ≈ 38 个额外错误 ≈ 2-3 个问题），不是从数据反推。
4. **跨模型一致性**——DeepSeek-Coder CLS–CWM 差距仅 0.02pp，使等价性结论在实质上不依赖阈值选择。

R1 提到 "between-seed std (0.37-0.97pp) 暗示更窄 SESOI 可能更合理"——我不同意这个推理方向。Seed std 反映的是**测量噪声**，SESOI 应基于**实践显著性**，两者是不同概念。噪声在 0.37-0.97pp 范围内反而说明 ±2pp 阈值远超噪声水平，是合理的实践显著性边界。

**建议：在正文 §3.4 增加一句明确阈值选择的 deployment-relevance 理据（目前只在 appendix），并引用 Bayesian ROPE 作为 sensitivity robustness 的补充证据。不需要升级为 critical。**

---

**[REBUT] R1-N2: Repo-level 因果归因缺乏充分统计支撑**

R1 此条存在**关键事实错误**——将两个不同统计模型的结果混为一谈。

**(a) z=−23.7 的来源与 model identity 无关。** Abstract 中 "this equivalence collapses (z=−23.7)" 引用的是 **cross-complexity LPM**（Appendix J，`correct ~ formulation × complexity + (1|problem_id)`，n=56,480，**139 clusters**），检验的是 CWM×repo 交互效应。该效应在 LPM 和 GEE 中**均显著**（GEE OR=0.31, p=0.002, AME=−21.6pp，与 LPM 系数一致在 0.3pp 以内）。R1 引用的 LPM p=0.002 vs GEE p=0.449 的矛盾来自另一个模型——**repo-level cross-model model**（`correct ~ formulation × model`，**仅 k=25 clusters**），检验的是 **model identity** 这个次要效应。论文在 Appendix J 已明确解释 k=25 < 40 导致 GEE sandwich SE 不稳定。

R1 将两个不同模型（139 clusters 的交互模型 vs 25 clusters 的跨模型模型）、两个不同效应（formulation×complexity vs model identity）混在一起论证，结论因此不成立。

**(b) MDE~25pp 的问题。** R1 正确指出 n=48 variant-level 的 MDE~25pp（Appendix H 确认）。但 abstract 的 "collapses" 基于 per-test 分析（n=56,480），不是 variant-level 分析。Per-test 水平的 18-26pp 差距有充分统计力。

**(c) "collapses" 措辞。** "Equivalence collapses" 描述的是等价关系的崩塌（统计交互效应），不是因果机制归因。论文 §3.5 已明确说 "Limited seed coverage and multiple confounds (§3.7) limit causal attribution"。这个 hedge 已经足够。

**结论：R1-N2 的核心论证基于事实错误（混淆两个不同统计模型），不应作为 critical issue。论文的因果审慎程度（§3.7 的 5 个 confounds 逐项分析 + worst-case compounding）在实证 NLP 论文中已属罕见。建议不予采纳为 Must-Fix。**

---

**[AGREE with qualification] R1-N3: TRAJ 配置非对称性使 "matched comparison" 不成立**

R1 事实核查准确：TRAJ 与 CLS/CWM 存在 lr 4×（2×10⁻⁴ vs 5×10⁻⁵）、数据量约 175×（~400 vs ~70K）、标签粒度（variant-level vs per-test）三重差异。Downsample ablation 仅控制数据量。

但需要细分讨论：

1. **论文已多处限定 TRAJ**——Table 1 用 ★ 标注 "Training configuration differs (§3.5)"；§3.5 明确称 CLS–TRAJ 对比为 "exploratory"；Appendix N（Threats）用整段讨论 TRAJ training regime。
2. **Abstract 未直接说 "matched"**——Abstract 说 "under ≤8B LoRA fine-tuning"，这是一个共享的实验框架（相同模型、相同 LoRA、相同评估集），但不是配置同一性声明。R1 引用的 "matched conditions" 来自 Abstract 第一段 "No prior work compares them under matched conditions"，这是对整个比较框架的描述，不是声称三种方法配置相同。
3. **配置差异部分是 formulation-inherent**——TRAJ 在 variant level 操作，天然只有 ~400 训练实例（vs CLS 的 ~70K per-test 实例），这不是实验设计缺陷而是公式化本身的特性。lr 差异则确实是可控的超参选择。

**我的建议：这是一个合理的 Should-Fix 而非 Must-Fix。** 论文应在 Abstract 或 §1 中更早、更显著地限定 TRAJ 的对比性质，而不是等到 §3.5 才说 "exploratory"。但现有的限定措辞（★标记 + §3.5 + Appendix N）已足够防止误读，不构成接收障碍。

---

### Should-Fix 回应

**[AGREE] R1-W1: CWM default-to-pass 使 repo-level 准确率失真**

R1 准确引用了 Appendix K 的数据（unparseable pass rate 74.6% vs parseable 68.3%，χ² p=5.9×10⁻¹⁰）。论文虽然在 Appendix K 详细讨论了这一偏差，但在 Table 3 的脚注中仅用 "parseable-only 38-43%, below majority" 一笔带过。R1 建议增加 "Parseable Acc (%)" 列是合理的，可以让读者直接看到 CWM 的真实判别能力。

**建议采纳。**

---

**[REBUT] R1-W2: 14B 收敛观察的 hedging 不一致**

R1 认为 §3.3 用 "capacity-dependent convergence at function level" 作为结论性措辞。但原文（§3.3 最后一句）的完整表述是：

> "CWM's delayed scaling onset—flat from 4B to 8B, then +2.17pp at 14B—and TRAJ's decelerating convergence (+2.13pp at 8B, +1.16pp at 14B) are both **consistent with** capacity-dependent convergence at function level."

"consistent with" 是标准科学 hedging——意思是"数据不矛盾"，不是"数据确认"。Abstract 的 "preliminary observation consistent with" 和 §3.3 的 "consistent with" 在语义强度上是**一致的**，不存在 hedging 不一致。

R1 提到 df=2 power~0.08 未在正文提及。实际上 §3.3 已说 "Seed-level TOST (df=2) does not confirm equivalence... reflecting the low power inherent in 3-seed comparisons"，power~0.08 的具体数字在 Appendix G.1，这是详细计算的合理归属位置。

**建议不予采纳。**

---

**[AGREE with qualification] R1-W3: Function-level ICC=0.191 外推至 Oracle 分析**

R1 指出 function-level ICC=0.191 vs repo-level ICC=0.3146（差 65%）。但需要区分两个用途：

1. **Oracle 分析（§A/Table 5）**——使用 ICC=0.191 作为 block correlation 参数。论文在 Appendix A "Sensitivity to ICC estimate" 段落已**明确讨论**这一选择，并论证 function-level ICC 是 conservative lower bound（repo-level ICC 更高，会进一步放大 per-test 优势）。因此 Oracle 分析中使用 function-level ICC 实际上**低估**了 per-test 的优势，方向有利于论文结论的保守性。
2. **TOST 功效**——§3.4 的 TOST 使用 seed-level paired analysis（df=4），不直接依赖 ICC-derived n_eff。n_eff≈86 在 §3.4 中作为上下文信息报告，来自 repo-level 计算（9784/114.4），使用的是 repo-level ICC=0.3146，不是 function-level ICC。

R1 的担忧方向正确（不同层级的 ICC 不应混用），但论文的实际做法比 R1 描述的更审慎。建议在 §A 中将 "conservative lower bound" 的论证从 appendix 提到更显著的位置。

---

**[AGREE] R1-W4: 缺少 TOST one-sided p-values 报告**

报告两个 one-sided p 值（p_upper, p_lower）对诊断 CLS–TRAJ 等价性的非确认原因有价值——可以揭示是上界还是下界被违反。这是一个简单的报告改进，无需额外实验。

**建议采纳。**

---

### Minor 回应

- **§2.3 Oracle k_eff exchangeable correlation 假设**——论文在 Appendix A 的 ICC sensitivity 段落已讨论，认为当前表述足够。
- **Table 1 TRAJ "★" 标记不够醒目**——[AGREE] 可改用更明显的视觉标记（如脚注加粗或颜色），但不影响评分。
- **Figure 2 caption 应标注 y-axis 非零基线**——[AGREE] Figure 3（Appendix）的 caption 有 "Note: y-axis does not start at zero" 但 Figure 2 没有。应补上。
- **§3.6 Appendix 编号不一致**——未能在论文中确认具体的不一致，需要 R1 提供更具体的引用。

---

### 总结

| R1 Issue | R1 Level | 我的判断 | 理由 |
|----------|----------|--------|------|
| N1 SESOI | Critical | **Should-Fix** | 论文已透明披露 + Bayesian ROPE 独立佐证 + 部署合理性论证 |
| N2 因果归因 | Critical | **不采纳** | R1 混淆了两个不同统计模型（139 vs 25 clusters），核心论证基于事实错误 |
| N3 TRAJ 非对称 | Critical | **Should-Fix** | 论文已多处限定，但应在 abstract/intro 更早标注 |
| W1 Default-to-pass | Warning | **采纳** | Table 3 应增加 parseable accuracy |
| W2 14B hedging | Warning | **不采纳** | "consistent with" 本身即为 hedging |
| W3 ICC 外推 | Warning | **部分采纳** | Oracle 分析中 ICC 选择实际更保守 |
| W4 TOST p-values | Warning | **采纳** | 简单报告改进 |

R1 的审查整体质量高，统计方法论的关注点准确，但 N2 存在关键事实错误（混淆统计模型），N1 和 N3 的严重性被高估。如果按我的重新分级，论文没有 critical must-fix，只有 3-4 个 should-fix，整体评分应高于 R1 的 3.5。

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

_source line 1170 · 2026-05-23T13:50:27.222662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/docs/paper/experiments.tex",
  "limit": "100",
  "offset": "0"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/docs/paper/experiments.tex",
    "limit": "100",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 1171 · 2026-05-23T13:50:27.223161+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3.

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

_source line 1172 · 2026-05-23T13:50:27.926120+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/docs/paper/abstract.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1173 · 2026-05-23T13:50:28.179581+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 1174 · 2026-05-23T13:50:31.190979+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16"
  }
}
```

</details>

---


### Tool result

_source line 1175 · 2026-05-23T13:50:31.242030+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction_304198.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments_3378f2.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/rank_ablation_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1176 · 2026-05-23T13:50:36.713009+00:00_

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

_source line 1177 · 2026-05-23T13:50:36.914283+00:00_

1	\begin{abstract}
2	LLM-based program repair increasingly generates multiple candidate patches, selecting the best via a verifier. Three execution-free alternatives to expensive execution-based verification have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares them under matched conditions.
3	
4	We present the first systematic comparison across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is not confirmed after multiple comparison correction at current power (${\sim}$0.3), but the gap narrows monotonically from 3.11\pp{} (4B) to 1.07\pp{} (14B). At repository level, this equivalence collapses ($z{=}-23.7$, DeepSeek-Coder): the \cls{}--\cwm{} gap widens to 18--26\pp{} across 2--3 seeds per model under our ${\leq}$8B LoRA protocol, driven by format collapse. At 14B (3 seeds, single family), all three formulations narrow to within 1.07\pp{}, a preliminary observation consistent with capacity-dependent convergence.
5	
6	Error complementarity and a failure mode taxonomy motivate future work on complexity-aware formulation routing, though simple heuristics capture $<$0.4\pp{} of oracle advantage.
7	\end{abstract}
8	

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

_source line 1178 · 2026-05-23T13:50:36.914657+00:00_

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

_source line 1179 · 2026-05-23T13:50:36.965941+00:00_

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
…[truncated 20091 chars]

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

_source line 1180 · 2026-05-23T13:55:12.424614+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "limit": "100",
  "offset": "0"
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
    "limit": "100",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-23T13:55:12.425149+00:00_

0	
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
11	  last_seen_round: 13
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
34	  action_items:
35	    - round: 6
36	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
37	      assigned_to: "paper"
3
…[truncated 2922 chars]

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

_source line 1182 · 2026-05-23T13:55:54.643476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "offset": "950"
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
    "offset": "950"
  }
}
```

</details>

---


### Tool result

_source line 1183 · 2026-05-23T13:55:54.694153+00:00_

950	    - round: 13
951	      reviewers: [1, 2]
952	      note: "R2-M1 提出，R1 AGREE。建议先陈述定性洞见，再给统计支撑。但 Abstract 已 ~189 words（≤200 word 限制），调整空间有限。"
953	  action_items:
954	    - round: 13
955	      action: "考虑将部分统计数值（如 z=−23.7）从 Abstract 移入正文"
956	      assigned_to: "paper"
957	      status: resolved
958	  resolution: "Abstract repo-level 句重构：先陈述定性结论 'this equivalence collapses'，再括号内给统计支撑 (z=-23.7, DeepSeek-Coder)。z 值保留因为是关键效应量。"
959	  resolution_round: 13
960	
961	- id: "R13-M3"
962	  summary: "三项贡献独立性值得商榷——互补性和 taxonomy 是主发现的辅助分析"
963	  category: framing
964	  severity: info
965	  status: resolved
966	  first_raised_round: 13
967	  last_seen_round: 13
968	  mentions:
969	    - round: 13
970	      reviewers: [1, 2]
971	      note: "R2-M4 提出，R1 partial REBUT：failure mode taxonomy (Table 4) 具有可迁移的诊断价值，可独立于三方比较使用。R1 同意 Contribution 2（互补性）与 Contribution 1 独立性较弱。Director：Minor——taxonomy 独立性成立，但 contribution list 可微调。"
972	  resolution: "Contribution 2 已重写为 negative result framing（R13-W2），降低了独立性要求。Taxonomy (Contribution 3) 独立性通过 R1 REBUT 得到确认。当前贡献结构合理。"
973	  resolution_round: 13
974	

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

_source line 1184 · 2026-05-23T13:56:01.242421+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13",
  "new_string": "- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13",
    "new_string": "- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1185 · 2026-05-23T13:56:01.344398+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-23T13:56:19.176679+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13 R1 再次提及但无新增要求。\"\n  resolution_round: 11",
  "new_string": "    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N2 re-raises（2-3 seeds, n=48, 5 confounds, 'collapses' 措辞）。R2 REBUT 指出 R1 混淆两个统计模型（z=-23.7 来自 139-cluster 交互 LPM 非 25-cluster 跨模型模型）。Director：R2 事实核查正确；R1 broader concern 仍有效但论文 §3.5/§3.7 hedging 已充分。Resolved 维持。\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13 R1 再次提及但无新增要求。\"\n  resolution_round: 11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13 R1 再次提及但无新增要求。\"\n  resolution_round: 11",
    "new_string": "    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N2 re-raises（2-3 seeds, n=48, 5 confounds, 'collapses' 措辞）。R2 REBUT 指出 R1 混淆两个统计模型（z=-23.7 来自 139-cluster 交互 LPM 非 25-cluster 跨模型模型）。Director：R2 事实核查正确；R1 broader concern 仍有效但论文 §3.5/§3.7 hedging 已充分。Resolved 维持。\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13 R1 再次提及但无新增要求。\"\n  resolution_round: 11"
  }
}
```

</details>

---


### Tool result

_source line 1187 · 2026-05-23T13:56:19.227829+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-23T13:56:24.416331+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13",
  "new_string": "- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13",
    "new_string": "- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1189 · 2026-05-23T13:56:24.467255+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1190 · 2026-05-23T13:56:34.995897+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W4 re-raises：checkpoint ablation 仅在 Qwen3-4B CLS 上进行，未覆盖受影响最严重的 CWM 配置。DeepSeek CWM early-stop vs final-epoch ~18pp。R2 AGREE。Director：resolved status maintained——step-400 eval 数据已证明 early checkpoint ≤ final epoch，format collapse 从训练早期即存在。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"",
  "new_string": "    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W4 re-raises：checkpoint ablation 仅在 Qwen3-4B CLS 上进行，未覆盖受影响最严重的 CWM 配置。DeepSeek CWM early-stop vs final-epoch ~18pp。R2 AGREE。Director：resolved status maintained——step-400 eval 数据已证明 early checkpoint ≤ final epoch，format collapse 从训练早期即存在。\"\n    - round: 14\n      reviewers: [2]\n      note: \"Fresh review R14. R2-W1 re-raises s42 用 step 400 vs s123/s456 用 step 6633 的配置异质性。R1 AGREE。Director：resolved 维持——step-400 eval 数据已证明早期 checkpoint 不改善结果。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W4 re-raises：checkpoint ablation 仅在 Qwen3-4B CLS 上进行，未覆盖受影响最严重的 CWM 配置。DeepSeek CWM early-stop vs final-epoch ~18pp。R2 AGREE。Director：resolved status maintained——step-400 eval 数据已证明 early checkpoint ≤ final epoch，format collapse 从训练早期即存在。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"",
    "new_string": "    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W4 re-raises：checkpoint ablation 仅在 Qwen3-4B CLS 上进行，未覆盖受影响最严重的 CWM 配置。DeepSeek CWM early-stop vs final-epoch ~18pp。R2 AGREE。Director：resolved status maintained——step-400 eval 数据已证明 early checkpoint ≤ final epoch，format collapse 从训练早期即存在。\"\n    - round: 14\n      reviewers: [2]\n      note: \"Fresh review R14. R2-W1 re-raises s42 用 step 400 vs s123/s456 用 step 6633 的配置异质性。R1 AGREE。Director：resolved 维持——step-400 eval 数据已证明早期 checkpoint 不改善结果。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\""
  }
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-23T13:56:35.047114+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-23T13:56:39.719861+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 13",
  "new_string": "- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 13",
    "new_string": "- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-23T13:56:39.821143+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-23T13:56:53.204831+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N1 再次标 CRITICAL：核心发现可从 §2.2 理论预测，属 confirmation 而非 discovery。R1 AGREE 但补充 quantitative boundary conditions（14B convergence, failure mode distribution）超越纯理论预测。两人 Excitement 均为 3/5。Director：inherent limitation，wont_fix 维持。\"\n  resolution: \"所有可行 action items 已完成。Excitement 稳定在 3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。Novelty ceiling 为 inherent limitation。\"\n  resolution_round: 11",
  "new_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N1 再次标 CRITICAL：核心发现可从 §2.2 理论预测，属 confirmation 而非 discovery。R1 AGREE 但补充 quantitative boundary conditions（14B convergence, failure mode distribution）超越纯理论预测。两人 Excitement 均为 3/5。Director：inherent limitation，wont_fix 维持。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R2-N1 再次标 CRITICAL (Excitement 2.5/5)。R1 REBUT：function-level 等价阈值、failure mode taxonomy 分布、capacity-dependent convergence 量化均超越 §2.2 理论预测，建议降为 Should-Fix。Director：R1 REBUT 有说服力，不采纳为独立 issue。Inherent limitation，wont_fix 维持。\"\n  resolution: \"所有可行 action items 已完成。Excitement 稳定在 2.5-3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。Novelty ceiling 为 inherent limitation。\"\n  resolution_round: 11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N1 再次标 CRITICAL：核心发现可从 §2.2 理论预测，属 confirmation 而非 discovery。R1 AGREE 但补充 quantitative boundary conditions（14B convergence, failure mode distribution）超越纯理论预测。两人 Excitement 均为 3/5。Director：inherent limitation，wont_fix 维持。\"\n  resolution: \"所有可行 action items 已完成。Excitement 稳定在 3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。Novelty ceiling 为 inherent limitation。\"\n  resolution_round: 11",
    "new_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N1 再次标 CRITICAL：核心发现可从 §2.2 理论预测，属 confirmation 而非 discovery。R1 AGREE 但补充 quantitative boundary conditions（14B convergence, failure mode distribution）超越纯理论预测。两人 Excitement 均为 3/5。Director：inherent limitation，wont_fix 维持。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R2-N1 再次标 CRITICAL (Excitement 2.5/5)。R1 REBUT：function-level 等价阈值、failure mode taxonomy 分布、capacity-dependent convergence 量化均超越 §2.2 理论预测，建议降为 Should-Fix。Director：R1 REBUT 有说服力，不采纳为独立 issue。Inherent limitation，wont_fix 维持。\"\n  resolution: \"所有可行 action items 已完成。Excitement 稳定在 2.5-3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。Novelty ceiling 为 inherent limitation。\"\n  resolution_round: 11"
  }
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-23T13:56:53.255912+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1196 · 2026-05-23T13:56:57.648301+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13",
  "new_string": "- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13",
    "new_string": "- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1197 · 2026-05-23T13:56:57.649227+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-23T13:57:09.621235+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-M1 和 R1-Q1 再次提及 pre-registration 状态。R2 AGREE。§3.4 已改为 'motivated by domain considerations but was not pre-registered'，引用 sensitivity analysis。Director: resolved——已诚实披露，无进一步修改空间。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；引用了 sensitivity analysis (Table tost_sensitivity)；明确承认结论对 margin 选择敏感。\"\n  resolution_round: 12",
  "new_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-M1 和 R1-Q1 再次提及 pre-registration 状态。R2 AGREE。§3.4 已改为 'motivated by domain considerations but was not pre-registered'，引用 sensitivity analysis。Director: resolved——已诚实披露，无进一步修改空间。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N1 标 Critical：鲁棒窗口仅 0.48pp。R2 AGREE with downgrade to Should-Fix：Bayesian ROPE 独立佐证 (P(ROPE)=0.975)、deployment relevance 论证合理、论文已透明披露。Director 采纳降级：Should-Fix。建议 §3.4 增加 deployment-relevance 论证从 Appendix 提到正文。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；引用了 sensitivity analysis (Table tost_sensitivity)；明确承认结论对 margin 选择敏感。Bayesian ROPE 提供独立佐证。\"\n  resolution_round: 12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-M1 和 R1-Q1 再次提及 pre-registration 状态。R2 AGREE。§3.4 已改为 'motivated by domain considerations but was not pre-registered'，引用 sensitivity analysis。Director: resolved——已诚实披露，无进一步修改空间。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；引用了 sensitivity analysis (Table tost_sensitivity)；明确承认结论对 margin 选择敏感。\"\n  resolution_round: 12",
    "new_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-M1 和 R1-Q1 再次提及 pre-registration 状态。R2 AGREE。§3.4 已改为 'motivated by domain considerations but was not pre-registered'，引用 sensitivity analysis。Director: resolved——已诚实披露，无进一步修改空间。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N1 标 Critical：鲁棒窗口仅 0.48pp。R2 AGREE with downgrade to Should-Fix：Bayesian ROPE 独立佐证 (P(ROPE)=0.975)、deployment relevance 论证合理、论文已透明披露。Director 采纳降级：Should-Fix。建议 §3.4 增加 deployment-relevance 论证从 Appendix 提到正文。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；引用了 sensitivity analysis (Table tost_sensitivity)；明确承认结论对 margin 选择敏感。Bayesian ROPE 提供独立佐证。\"\n  resolution_round: 12"
  }
}
```

</details>

---


### Tool result

_source line 1199 · 2026-05-23T13:57:09.822957+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1200 · 2026-05-23T13:57:14.294018+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13",
  "new_string": "- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 13",
    "new_string": "- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1201 · 2026-05-23T13:57:14.395272+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-23T13:57:34.860133+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N2 标 CRITICAL：TRAJ 使用 ~400 vs ~70K 实例 + 不同 lr + variant-level labels，三方比较不受控。R1 完全 AGREE，补充：主文 Tables 1-3 无视觉标注 TRAJ 差异。Director 裁定：§3.5 已有 'exploratory' 标注和 confound 讨论，resolved 维持。但报告记录此为 persistent concern。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"Contribution summary 中明确表述 CLS-TRAJ repo-level 比较包含 training regime confound\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 标注 'The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity, a formulation-inherent confound.' R13 再次提出但无新增可行动修改。\"\n  resolution_round: 12",
  "new_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N2 标 CRITICAL：TRAJ 使用 ~400 vs ~70K 实例 + 不同 lr + variant-level labels，三方比较不受控。R1 完全 AGREE，补充：主文 Tables 1-3 无视觉标注 TRAJ 差异。Director 裁定：§3.5 已有 'exploratory' 标注和 confound 讨论，resolved 维持。但报告记录此为 persistent concern。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N3 标 Critical：lr 4×、数据量 175×、标签粒度三重差异使 'matched comparison' 不成立。R2 AGREE with qualification to Should-Fix：论文已有 ★ 标记 + §3.5 'exploratory' + Appendix N，但应在 Abstract/§1 更早限定。Director 采纳降级：Should-Fix。建议 Abstract 限定 'matched for CLS and CWM; TRAJ comparison is exploratory'。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"Contribution summary 中明确表述 CLS-TRAJ repo-level 比较包含 training regime confound\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 标注 'The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity, a formulation-inherent confound.' R14 建议 Abstract 更早限定 TRAJ 为 exploratory。\"\n  resolution_round: 12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N2 标 CRITICAL：TRAJ 使用 ~400 vs ~70K 实例 + 不同 lr + variant-level labels，三方比较不受控。R1 完全 AGREE，补充：主文 Tables 1-3 无视觉标注 TRAJ 差异。Director 裁定：§3.5 已有 'exploratory' 标注和 confound 讨论，resolved 维持。但报告记录此为 persistent concern。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"Contribution summary 中明确表述 CLS-TRAJ repo-level 比较包含 training regime confound\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 标注 'The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity, a formulation-inherent confound.' R13 再次提出但无新增可行动修改。\"\n  resolution_round: 12",
    "new_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R2-N2 标 CRITICAL：TRAJ 使用 ~400 vs ~70K 实例 + 不同 lr + variant-level labels，三方比较不受控。R1 完全 AGREE，补充：主文 Tables 1-3 无视觉标注 TRAJ 差异。Director 裁定：§3.5 已有 'exploratory' 标注和 confound 讨论，resolved 维持。但报告记录此为 persistent concern。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N3 标 Critical：lr 4×、数据量 175×、标签粒度三重差异使 'matched comparison' 不成立。R2 AGREE with qualification to Should-Fix：论文已有 ★ 标记 + §3.5 'exploratory' + Appendix N，但应在 Abstract/§1 更早限定。Director 采纳降级：Should-Fix。建议 Abstract 限定 'matched for CLS and CWM; TRAJ comparison is exploratory'。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"Contribution summary 中明确表述 CLS-TRAJ repo-level 比较包含 training regime confound\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 标注 'The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity, a formulation-inherent confound.' R14 建议 Abstract 更早限定 TRAJ 为 exploratory。\"\n  resolution_round: 12"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-23T13:57:34.860966+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-23T13:57:41.188428+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 13",
  "new_string": "- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 13",
    "new_string": "- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-23T13:57:41.239484+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1206 · 2026-05-23T13:57:45.859685+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 13",
  "new_string": "- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 13",
    "new_string": "- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1207 · 2026-05-23T13:57:45.912502+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1208 · 2026-05-23T13:57:58.212868+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-W2 re-raises CWM 生态效度。R2 partially AGREE but notes §3.7 和 §5 已有 ≤8B 限定。Director: resolved——≤8B qualifier 已充分覆盖 Abstract/Conclusion/Threats.\"\n  resolution: \"合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。\"\n  resolution_round: 10",
  "new_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-W2 re-raises CWM 生态效度。R2 partially AGREE but notes §3.7 和 §5 已有 ≤8B 限定。Director: resolved——≤8B qualifier 已充分覆盖 Abstract/Conclusion/Threats.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R2-N2 标 Critical：14B 收敛至 0.43pp 暗示 capacity-driven。R1 AGREE。Director 裁定 Should-Fix（降级）：论文已有 qualifier（Abstract ≤8B, §3.3 scaling, Limitations），建议 Conclusion 更显著讨论 32B+ open question。\"\n  resolution: \"合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。R14 建议 Conclusion 补充 32B+ open question。\"\n  resolution_round: 10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-W2 re-raises CWM 生态效度。R2 partially AGREE but notes §3.7 和 §5 已有 ≤8B 限定。Director: resolved——≤8B qualifier 已充分覆盖 Abstract/Conclusion/Threats.\"\n  resolution: \"合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。\"\n  resolution_round: 10",
    "new_string": "    - round: 13\n      reviewers: [1, 2]\n      note: \"Fresh review R13. R1-W2 re-raises CWM 生态效度。R2 partially AGREE but notes §3.7 和 §5 已有 ≤8B 限定。Director: resolved——≤8B qualifier 已充分覆盖 Abstract/Conclusion/Threats.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R2-N2 标 Critical：14B 收敛至 0.43pp 暗示 capacity-driven。R1 AGREE。Director 裁定 Should-Fix（降级）：论文已有 qualifier（Abstract ≤8B, §3.3 scaling, Limitations），建议 Conclusion 更显著讨论 32B+ open question。\"\n  resolution: \"合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。R14 建议 Conclusion 补充 32B+ open question。\"\n  resolution_round: 10"
  }
}
```

</details>

---


### Tool result

_source line 1209 · 2026-05-23T13:57:58.267500+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-23T13:58:08.894593+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13",
  "new_string": "- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13",
    "new_string": "- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-23T13:58:11.555937+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 2661
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-23T13:58:19.136852+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W2 再次提及 CWM 生态效度。R2 partially AGREE but notes 论文已有充分 qualifier (§3.7, §5, Abstract). Director: resolved——所有 qualifier 已到位。\"\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。\"\n  resolution_round: 12",
  "new_string": "    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W2 再次提及 CWM 生态效度。R2 partially AGREE but notes 论文已有充分 qualifier (§3.7, §5, Abstract). Director: resolved——所有 qualifier 已到位。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R2-N2 再次标 Critical，R1 AGREE。合并追踪至 R8-W6 round 14 mention。Director 裁定 Should-Fix（降级）。\"\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。R14 确认所有可行 qualifier 已到位。\"\n  resolution_round: 12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W2 再次提及 CWM 生态效度。R2 partially AGREE but notes 论文已有充分 qualifier (§3.7, §5, Abstract). Director: resolved——所有 qualifier 已到位。\"\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。\"\n  resolution_round: 12",
    "new_string": "    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W2 再次提及 CWM 生态效度。R2 partially AGREE but notes 论文已有充分 qualifier (§3.7, §5, Abstract). Director: resolved——所有 qualifier 已到位。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R2-N2 再次标 Critical，R1 AGREE。合并追踪至 R8-W6 round 14 mention。Director 裁定 Should-Fix（降级）。\"\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。R14 确认所有可行 qualifier 已到位。\"\n  resolution_round: 12"
  }
}
```

</details>

---


### Tool result

_source line 1213 · 2026-05-23T13:58:19.137863+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-23T13:58:26.321840+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "- id: \"R13-M1\"\n  summary: \"PRM/ORM 映射命名反直觉——CLS 听起来像 ORM 而非 PRM\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13",
  "new_string": "- id: \"R13-M1\"\n  summary: \"PRM/ORM 映射命名反直觉——CLS 听起来像 ORM 而非 PRM\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "- id: \"R13-M1\"\n  summary: \"PRM/ORM 映射命名反直觉——CLS 听起来像 ORM 而非 PRM\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13",
    "new_string": "- id: \"R13-M1\"\n  summary: \"PRM/ORM 映射命名反直觉——CLS 听起来像 ORM 而非 PRM\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-23T13:58:26.372948+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1216 · 2026-05-23T13:58:45.196989+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "old_string": "  resolution: \"Contribution 2 已重写为 negative result framing（R13-W2），降低了独立性要求。Taxonomy (Contribution 3) 独立性通过 R1 REBUT 得到确认。当前贡献结构合理。\"\n  resolution_round: 13",
  "new_string": "  resolution: \"Contribution 2 已重写为 negative result framing（R13-W2），降低了独立性要求。Taxonomy (Contribution 3) 独立性通过 R1 REBUT 得到确认。当前贡献结构合理。\"\n  resolution_round: 13\n\n# === Round 14 (Fresh Review) New Issues ===\n\n- id: \"R14-W1\"\n  summary: \"CWM default-to-pass 使 repo-level 准确率系统性失真——Table 3 应增加 Parseable Acc 列\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 AGREE。53-74% unparseable → default pass。Appendix K 显示 unparseable pass rate 74.6% vs parseable 68.3%（χ² p=5.9×10⁻¹⁰），default 策略系统性偏向正确。Table 3 脚注仅简要提及 parseable-only 38-43%。\"\n  action_items:\n    - round: 14\n      action: \"Table 3 增加 'Parseable Acc (%)' 列，让读者直接看到 CWM 真实判别能力\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W2\"\n  summary: \"TOST one-sided p-values 未报告——无法诊断 CLS-TRAJ 非确认方向\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 AGREE。仅报告 max(p_upper, p_lower)，未报告两个 one-sided p 值。可诊断 CLS-TRAJ 等价性非确认是上界还是下界被违反。简单报告改进。\"\n  action_items:\n    - round: 14\n      action: \"Appendix G 补充 TOST 两个 one-sided p 值（p_upper, p_lower）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "old_string": "  resolution: \"Contribution 2 已重写为 negative result framing（R13-W2），降低了独立性要求。Taxonomy (Contribution 3) 独立性通过 R1 REBUT 得到确认。当前贡献结构合理。\"\n  resolution_round: 13",
    "new_string": "  resolution: \"Contribution 2 已重写为 negative result framing（R13-W2），降低了独立性要求。Taxonomy (Contribution 3) 独立性通过 R1 REBUT 得到确认。当前贡献结构合理。\"\n  resolution_round: 13\n\n# === Round 14 (Fresh Review) New Issues ===\n\n- id: \"R14-W1\"\n  summary: \"CWM default-to-pass 使 repo-level 准确率系统性失真——Table 3 应增加 Parseable Acc 列\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 AGREE。53-74% unparseable → default pass。Appendix K 显示 unparseable pass rate 74.6% vs parseable 68.3%（χ² p=5.9×10⁻¹⁰），default 策略系统性偏向正确。Table 3 脚注仅简要提及 parseable-only 38-43%。\"\n  action_items:\n    - round: 14\n      action: \"Table 3 增加 'Parseable Acc (%)' 列，让读者直接看到 CWM 真实判别能力\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W2\"\n  summary: \"TOST one-sided p-values 未报告——无法诊断 CLS-TRAJ 非确认方向\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 AGREE。仅报告 max(p_upper, p_lower)，未报告两个 one-sided p 值。可诊断 CLS-TRAJ 等价性非确认是上界还是下界被违反。简单报告改进。\"\n  action_items:\n    - round: 14\n      action: \"Appendix G 补充 TOST 两个 one-sided p 值（p_upper, p_lower）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-23T13:58:45.197998+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Edit",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-23T13:58:48.763219+00:00_

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

_source line 1219 · 2026-05-23T13:58:49.166361+00:00_

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
…[truncated 36005 chars]

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
