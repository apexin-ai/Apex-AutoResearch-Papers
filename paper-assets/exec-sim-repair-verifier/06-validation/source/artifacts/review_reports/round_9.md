---
round: 9
review_mode: continue
overall_score: 3.0
timestamp: 2026-05-23T03:17:49.095172+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 9 审稿报告（Continue Review）

**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
**Venue**: EMNLP 2026 via ARR (Long Paper)
**审稿模式**: Continue（基于上轮 R10 审稿意见的修订评估）
**Reviewer 编排**: 2 人（R1 统计方法论 + 实验严谨性 / R2 Framing + Novelty + 完整性）

---

## Summary

本轮为继续审稿，评估论文在收到上轮（Round 10 Fresh Review, Overall 3.0）审稿意见后的修订质量。主要修改包括：(1) 14B 探索性结果（Table 2, CLS 89.21% vs CWM 89.26%，gap ≈ 0），(2) Bayesian ROPE 分析补充 TOST 等价检验（P(ROPE)=0.975 for CLS-CWM），(3) TOST 功效透明讨论（n_eff≈86, power~0.3），(4) variant-level 分析标注为 exploratory，(5) routing 负结果（<0.4pp of oracle gap），(6) GEE logistic regression robustness check，(7) checkpoint 证据整合，(8) wall-clock 时间（48ms vs 16.3s）。

---

## 修订评估：Issue Tracker 逐条验证

### 全部 RESOLVED（两位 Reviewer 共识）

**[R6-N1] RESOLVED** — Variant-level exploratory 标注 ✅
§3.5 开头明确标注 "Variant-level comparisons (n=48) are exploratory due to limited seed coverage"。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 "definitive causal attribution requires multi-seed replication"。两位 Reviewer 一致确认标注充分。

**[R8-W1] RESOLVED** — TOST 功效 + Bayesian ROPE ✅
三处修改完整解决：(a) §3.4 Statistical power 段落透明披露 n_eff≈86, power~0.3；(b) Bayesian ROPE（Jeffreys prior, ±2pp ROPE）独立验证 CLS-CWM 等价（P(ROPE)=0.975, 95% HDI [+0.10, +2.00pp]）和 CLS-TRAJ 不确定性（P(ROPE)=0.542, inconclusive）；(c) Abstract "not confirmed after multiple comparison correction" 准确审慎。R1 称为"教科书级处理"，R2 同意。TOST + Bayesian ROPE 双框架的一致性显著增强了证据质量。

**[R8-M2] RESOLVED** — Logistic regression robustness ✅
Appendix M 补充 GEE logistic regression（binomial family, exchangeable correlation, robust sandwich SEs）。CWM×repo interaction OR=0.31 (0.15, 0.65), p=0.002，与 LPM 一致。Model identity LPM (p=0.002) vs GEE (p=0.410) 差异透明披露——commit 0b38a2b 修正了过强显著性声明。Primary effects 在两种框架下均 robust。

**[R6-M3] RESOLVED** — Figure y-axis ✅
Figure 2 y-axis 非零起始，caption 标注 "y-axis does not start at zero"。两位 Reviewer 均确认：对 0-3pp 差异展示，非零起始合理且有标注。Figure 3 (Appendix) 也已标注。

### STILL_OPEN / WONT_FIX（Inherent Limitation）

**[R6-N4] WONT_FIX** — Novelty ceiling（inherent）
R2 标 STILL_OPEN（改善但核心贡献类型未变），R1 AGREE on assessment。所有可行 action items 已完成：routing 实验（negative result）、Bayesian ROPE、14B 验证。Excitement 从 2.5 提升至 3.0，但核心贡献类型（empirical comparison of existing formulations）是 inherent limitation，无法通过进一步修改解决。标记为 wont_fix。

**[R8-W7] WONT_FIX** — Conference-level excitement（合并至 R6-N4）

---

## 新发现的问题

### Minor（3 个，两位 Reviewer 共识）

**[R11-M1] Figure 2 中 14B 单 seed 视觉权重**
R1 提出，R2 AGREE。14B 数据点与多 seed 的 4B/8B 数据点在图中视觉等权，读者快速浏览可能过度解读 gap reversal (CWM 89.26% vs CLS 89.21%)。建议在 14B 数据点加星号/虚线或图内 "n=1" 标注。

**[R11-M2] §3.5 LPM vs GEE model identity 不一致需 qualifier**
R1 提出，R2 AGREE。§3.5 引用 LPM model identity 效应 (p=0.001)，但 Appendix M 的 GEE 给出 p=0.410——从"高度显著"到"完全不显著"。建议加 qualifier："model identity reaches significance under LPM but not under GEE logistic regression (Appendix M); this effect is specification-dependent."

**[R11-M3] Abstract "motivate routing" 需限定**
R2 提出，R1 AGREE。Abstract "motivate complexity-aware formulation routing" 暗示 routing 有前景，但 §3.6 报告 simple routing capture <0.4pp of oracle gap。建议改为 "motivate **learned** complexity-aware routing" 或加半句限定。

### 分歧记录

**R2-NEW-2（Abstract "not confirmed" 精确性）**：R2 担心可能被误读为 "disconfirmed"，R1 REBUT——"not confirmed" 是统计标准用语，上下文和 Bayesian ROPE 提供消歧。Director 裁定：R1 REBUT 成立，不构成 actionable issue。

---

## Strengths（延续上轮 + 本轮新增）

**S1. 统计方法论达到 NLP 领域顶级水平。** TOST + Bayesian ROPE 双框架、ICC-clustered bootstrap、Holm-Bonferroni、GEE robustness check、transparent power analysis——在 NLP empirical papers 中极为罕见。[R1-S2, R2-S1 共识，本轮进一步强化]

**S2. Claim calibration 系统性改善。** 从上轮的"偶有 overclaim"提升至"系统性 well-calibrated"：exploratory/confirmatory 区分清晰，≤8B 限定一致，TRAJ 措辞审慎，14B 标注恰当。[R2 Framing 一致性检查全部通过]

**S3. 14B capacity-dependent convergence 是有意义的新 insight。** CLS-CWM gap 从 2.62pp (8B) 收窄至 -0.05pp (14B) 暗示 CWM 退化是 capacity-dependent 而非 formulation-inherent——对社区的 resource allocation 有前瞻价值。虽为 single seed / exploratory，但标注恰当。[R2 认为这是本轮最有价值的新增]

**S4. 负结果文档化增加分析深度。** Routing heuristic negative result（<0.4pp of oracle gap）将未验证假设转化为文档化实验结论，比"future work"声明更有价值。[R1, R2 共识]

---

## Weaknesses

### Must-Fix（无）

本轮无新增 Must-Fix。所有上轮 tracked CRITICAL issues 均已 RESOLVED 或标记为 inherent limitation (wont_fix)。

### Should-Fix（无新增）

上轮 Should-Fix 均已 RESOLVED。

### Minor（3 个，均为 consensus）

R11-M1, R11-M2, R11-M3（见上文"新发现的问题"）。均为低成本 polish 级修改。

---

## Missing References

本轮未发现新的遗漏引用。上轮要求的 CodeRM (Ma et al., ACL 2025) 和 ORM/PRM 映射已在 Related Work 中加入。Kruschke (2013, 2018) 和 Cohen (1988) 正确引用于 Bayesian ROPE 和 power analysis。

---

## External Review

未配置外部审稿。

---

## Visual Layout Check（非评分项）

视觉审查完成（0 critical, 1 warning, 7 info）：

- **[WARNING]** p.24 附录最后一页仅约 14 行（<20% 页面），大面积空白。建议紧凑化或合并。
- **[INFO]** p.1-2 无 display item，Figure 1 在 p.3 出现（可接受但非最优）。
- **[INFO]** p.7 Figure 2 y-axis 非零开始，caption 已标注——与 Reviewer 评估一致。
- **[INFO]** p.8 最后一页极度紧凑（Related Work 续段 + Conclusion + Limitations），reviewer 可能觉得 conclusion 仓促。
- **[INFO]** p.6 双表格密度较高但未溢出。
- **[INFO]** p.12 ARR Checklist 在 PDF 中——按用户规则应在 OpenReview form 填写。需确认当前投稿要求。
- **[INFO]** p.13 Figure 3 单色柱状图，caption 清晰。
- **[INFO]** p.15 高密度页面但无溢出。

---

## Overall Assessment

### 分项评分

| 维度 | R1 Round 10 | R1 Round 11 | R2 Round 10 | R2 Round 11 | 共识 |
|------|------------|------------|------------|------------|------|
| Soundness | 3/5 | **4/5** | 3.5/5 | **4/5** | **4/5** ✅ |
| Excitement | 3/5 | 3/5 | 2.5/5 | **3/5** | **3/5** ✅ |
| Reproducibility | 4/5 | 4/5 | — | — | 4/5 |
| Overall | 3.5 | 3.5 | 3.0 | 3.0 | **见下** |
| Confidence | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 |

### Overall 评分分歧与裁定

**R1: 3.5 (Borderline Conference)** — 理由：Soundness 3→4 是实质性改善；方法论严谨性本身构成 methodological demonstration value；exceptional soundness 应部分补偿 moderate excitement。引用 Dodge et al. (2019), Card et al. (2020) 等方法论贡献论文作为 precedent。

**R2: 3.0 (Findings)** — 理由：ARR 将 soundness 和 excitement 分开评分是有原因的；soundness 4/5 已充分反映方法论贡献；excitement ceiling（比较已有方法）无法被 soundness 跨维度补偿。Findings 定位恰好匹配。

**Director 裁定：Overall 3.0 (Findings)**

R2 的论点更符合 ARR 评分体系设计：soundness 和 excitement 是独立维度，exceptional soundness 已在 Soundness 4/5 中得到反映，不应 double-count 到 Overall。论文的方法论严谨性是 NLP 领域的示范，但核心贡献类型（empirical comparison without new methods）限制了 excitement。Findings track 是这篇论文的正确归属。

R1 的 3.5 评估是可辩护的——如果 AC 对 empirical comparison papers 有更高的包容度，或认为方法论示范价值有独立 excitement，则 Borderline Conference 成立。两个分数都在合理范围内。

### 与上轮对比

| | Round 10 (Fresh) | Round 11 (Continue) | 变化 |
|---|---|---|---|
| 所有 tracked issues resolved | 6 open/in_progress | 0 open（+ 3 新 MINOR） | ✅ 全部解决 |
| Soundness | 3-3.5/5 | **4/5 共识** | ↑ 显著提升 |
| Excitement | 2.5-3/5 | **3/5 共识** | ↑ 小幅提升 |
| Overall | 3.0 | **3.0** | = 维持 |

**修订质量评价**：优秀。所有 tracked issues 均得到充分回应，无一敷衍。Bayesian ROPE、GEE robustness、transparent power analysis 等修改展现了高水平的方法论能力。新增的 3 个 MINOR 问题均为 polish 级别，不影响论文的核心质量。

### 建议定位

**推荐 Findings 接收**。论文在 soundness 维度达到 NLP 领域高水平（TOST + Bayesian ROPE + GEE + ICC + Holm-Bonferroni），failure mode taxonomy 和 14B convergence insight 有实用价值。Excitement 限制为 inherent（贡献类型为 empirical comparison），不影响 Findings 的合格性。

---

## Detailed Comments

### 给作者的修改建议（按优先级）

1. **[R11-M1]** Figure 2 中 14B 数据点加视觉区分（星号/虚线/图内 "n=1"），避免 gap reversal 被过度解读。
2. **[R11-M2]** §3.5 model identity 效应加 LPM vs GEE qualifier（"specification-dependent"），保持与 Appendix M 的 claim 强度一致。
3. **[R11-M3]** Abstract "motivate routing" 改为 "motivate **learned** complexity-aware routing" 或加限定半句。
4. **[视觉]** p.24 空白页紧凑化。
5. **[视觉]** 确认 ARR Checklist 是否应在 PDF 中还是仅在 OpenReview form 中。

### 无需修改的确认

- Abstract ≤8B 限定、TRAJ 措辞、Conclusion 限定、14B exploratory 标注、variant-level exploratory 标注——全部通过 framing 一致性检查。
- Limitations 覆盖充分（Python-only、≤8B LoRA、synthetic mutation）。
- 格式合规（8 页正文 + 不计入限制的 Limitations）。