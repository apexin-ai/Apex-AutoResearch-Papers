---
round: 12
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-23T14:01:46.712083+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 14 审稿报告（Fresh Review）

**投稿**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
**Venue**: EMNLP 2026 (ARR)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）
**轮次**: Round 14 (Fresh Review), 1 轮独立审稿 + 1 轮交叉分享

---

## Summary

本文首次在匹配条件下系统比较了 LLM 代码修复中三种 execution-free 验证公式（CLS 分类、CWM 生成、TRAJ 轨迹级），跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别和多个 seeds。核心发现为三层结构：(1) fine-tuning 必要（35-36pp 增益）；(2) function-level 三种公式近等价（CLS-CWM TOST 确认，CLS-TRAJ Holm 校正后未确认但 gap 单调收窄至 1.07pp@14B）；(3) repo-level 在 ≤8B LoRA 下等价崩塌（CLS-CWM gap 18-26pp，由 format collapse 驱动）。论文同时提供了 failure mode taxonomy 和 error complementarity 分析。

---

## Strengths

**S1. 首个匹配条件的系统比较。** 控制模型容量、训练数据、超参数和评估协议进行 CLS-CWM 比较（TRAJ 为 exploratory），直接回答从业者的 formulation 选择问题。Cross-family 一致性（Qwen3 和 DeepSeek-Coder 在 CLS-CWM 差异方向一致）增强结论可信度。[两人共识]

**S2. 统计框架出色。** TOST 等价检验 + Bayesian ROPE 双验证、clustered bootstrap（114 clusters, 10K resamples）、Holm-Bonferroni 校正（k=5）、ICC/DEFF 修正——在 NLP 实证论文中属上乘水准。[两人共识, R1 Soundness 3.5, R2 Soundness 3.5]

**S3. 透明的局限性标注。** §3.5 将 variant-level 分析标注为 exploratory，§3.7 列出 5 个 confounds 逐项分析（worst-case compounding ~11.5pp），CLS-TRAJ Holm 校正后不成立也如实报告。TOST power ~0.3 在 §3.4 明确讨论。SESOI 未预注册在正文而非 appendix 中诚实披露。[两人共识]

**S4. 实用的 failure mode taxonomy。** Table 4 的三类失败模式（format collapse, decision collapse, aggregation penalty）提供可迁移的诊断框架。四项 failed interventions（LoRA rank doubling, majority voting, relaxed matching, scaling）增强 format collapse 结论可信度。[两人共识]

**S5. 保守的报告策略。** 系统性选择更保守的分析路径（seed-level TOST 而非 problem-level bootstrap），体现方法论诚信。[R1 提出, R2 在交叉回应中确认]

**S6. GenRM 领域特异性观察。** 代码验证中 generation ≤ discrimination（与 GenRM 在数学推理中的发现相反），辅以 output structure 假设和 >50% unparseable 数据。[两人共识, 均认为分析可更深入]

---

## Weaknesses

### Must-Fix（0 项）

*经交叉分享和 Director 裁定，所有初审 Critical 级别 issue 均被降级或合并为 Should-Fix。详见"裁定分歧"部分。*

### Should-Fix（7 项）

**W1. [warning] [consensus] CWM baseline 公平性——≤8B LoRA vs 原版 32B。**
- R2 提出 (Critical), R1 AGREE。Director 裁定降为 Should-Fix。
- 论文 CWM 是 4-8B LoRA 微调，14B function-level 收敛至 0.43pp 暗示差异可能主要源于 capacity。Abstract "equivalence collapses" 倾向于将差异归因于 formulation 而非 capacity。
- 论文已有 qualification（Abstract "under our ≤8B LoRA protocol"、§3.3 scaling、Limitations），但可在 Conclusion 更显著讨论 "32B+ CWM 是否会消除 format collapse" 作为 open question。
- **裁定理由**：论文已有多处 qualifier，但 Abstract/Conclusion 的 framing 仍倾向 formulation-inherent 解读。降为 Should-Fix 因为 (a) qualifier 已存在, (b) 14B 收敛已报告, (c) 进一步修改空间有限。

**W2. [warning] [consensus, R2 downgrade] SESOI ±2pp 阈值未预注册且结论敏感。**
- R1 提出 (Critical), R2 AGREE with downgrade to Should-Fix。Director 采纳降级。
- 鲁棒窗口仅 0.48pp (±2.00→±1.52pp)。但 Bayesian ROPE 独立佐证 (P(ROPE)=0.975)、部署合理性论证 (2pp ≈ 2-3 problems out of 114)、DeepSeek CLS-CWM gap 仅 0.02pp 使等价性在实质上不依赖阈值。
- **建议**：§3.4 增加一句将 Appendix G 的 deployment-relevance 论证提到正文；引用 Bayesian ROPE 作为 sensitivity robustness 补充。

**W3. [warning] [consensus, R2 downgrade] TRAJ 配置非对称性使 "matched comparison" 需限定。**
- R1 提出 (Critical), R2 AGREE with qualification, 建议 Should-Fix。Director 采纳。
- TRAJ 与 CLS/CWM 存在 lr 4×、数据量 175×、标签粒度三重差异。论文已有 ★ 标记 + §3.5 "exploratory" 标注 + Appendix N。但 Abstract "No prior work compares them under matched conditions" 应更早限定 TRAJ。
- **建议**：Abstract 或 §1 中明确 "matched for CLS and CWM; TRAJ comparison is exploratory due to formulation-inherent training regime differences"。

**W4. [warning] [consensus] CWM default-to-pass 使 repo-level 准确率系统性失真。**
- R1 提出, R2 AGREE。
- 53-74% unparseable → default pass。Appendix K 揭示 unparseable pass rate 74.6% vs parseable 68.3% (χ² p=5.9×10⁻¹⁰)。Table 3 脚注仅简要提及。
- **建议**：Table 3 增加 "Parseable Acc (%)" 列，让读者直接看到 CWM 判别能力。

**W5. [warning] [consensus] CLS-TRAJ label granularity confound 无法消除。**
- R2 提出, R1 AGREE。
- CLS per-test labels vs TRAJ variant-level labels 的粒度差异无法通过 downsample 控制。CLS 优势可能来自 label granularity 而非 formulation。
- 论文 §3.5 已标注 "exploratory...formulation-inherent confound"。
- **建议**：维持当前标注。这是 formulation-inherent confound，无进一步实验修改空间。

**W6. [warning] [consensus] PRM/ORM 映射粒度讨论不够精确。**
- R2 提出, R1 AGREE。
- CLS per-test ≠ PRM per-step（粒度不同）；GenRM 在 code 中未胜出的 "output structure" 解释未充分展开。
- **建议**：§4 加 1-2 句 qualify 粒度差异：per-test granularity 对应 per-step PRM，per-patch verdict 对应 outcome-level ORM。

**W7. [warning] [consensus] 缺少 TOST one-sided p-values。**
- R1 提出, R2 AGREE。
- 报告 p_upper 和 p_lower 对诊断 CLS-TRAJ 非确认原因有价值——可揭示是上界还是下界被违反。
- **建议**：Appendix G 补充两个 one-sided p 值。

### 裁定分歧

**R2-N1 (novelty/confirmation study)**: R2 标 Critical (Excitement 2.5/5), R1 REBUT。
- **Director 裁定：不采纳为独立 issue。** R1 的 REBUT 有说服力——function-level 等价的定量阈值、failure mode taxonomy 的具体分布和机制、capacity-dependent convergence 的量化特征（Figure 2, Table 2）均超越 §2.2 的理论预测。论文的贡献是 "rigorous quantification with methodological framework" 而非纯 confirmation。Excitement 受限是 inherent limitation (R6-N4, wont_fix)，不是可修复的 weakness。

**R1-N2 (repo-level 因果归因)**: R1 标 Critical, R2 REBUT (事实错误)。
- **Director 裁定：部分采纳，合并入 W1。** R2 正确指出 R1 混淆了两个不同统计模型——z=-23.7 来自 139-cluster formulation×complexity 交互 LPM（Appendix J），GEE p=0.449 来自 25-cluster cross-model model 的 model identity 效应。这是不同模型检验不同效应，R1 将两者并列论证因果推断不可靠的推理不成立。Director 核实论文原文（§3.5 最后段）确认 R2 事实核查正确。但 R1 的更广泛关注（2-3 seeds, n=48 variants, 5 confounds）仍有效，论文 §3.5/§3.7 的 hedging（"exploratory", "Limited seed coverage and multiple confounds limit causal attribution"）已相当充分。"collapses" 描述的是统计交互效应的显著性变化，不是因果机制归因。合并入 W1 的 framing concern。

**R2-W3 (error complementarity 无实用信号)**: R2 标 Should-Fix, R1 REBUT。
- **Director 裁定：不采纳。** Negative result（4 种 heuristic 均 <0.4pp）有独立信息量，排除 naive approaches。论文 framing 诚实（"motivation for future learned routers"），篇幅仅 ~1/3 column，定位恰当。

**R1-W2 (14B hedging 不一致)**: R1 标 Should-Fix, R2 REBUT。
- **Director 裁定：不采纳。** "consistent with" 是标准科学 hedging（"数据不矛盾"而非"数据确认"），与 Abstract "preliminary observation consistent with" 语义强度一致。§3.3 已提及 "low power inherent in 3-seed comparisons"。

**R1-W3 (ICC 外推)**: R1 标 Should-Fix, R2 部分 AGREE。
- **Director 裁定：降为 Minor (M7)。** 论文在 Appendix A 已讨论 function-level ICC 作为 conservative lower bound（repo-level ICC 更高会进一步放大 per-test 优势）；TOST 使用 seed-level paired analysis (df=4)，不直接依赖 ICC-derived n_eff。

---

## 小问题（不影响接收）

- **M1**: Figure 2 "inverted-U trajectory" 仅 3 数据点，建议改为 "non-monotonic pattern"。[两人共识]
- **M2**: Abstract 中 z=-23.7 和 18-26pp 并列。R2 认为可能混淆不同统计量，R1 REBUT（有明确 context 区分）。Director：不需修改，context 已足够。
- **M3**: Precision ablation seeds (789/0 NF4) 混入主 seed pool。需确认与 main seeds 独立性。[两人共识]
- **M4**: Table 3 "Var." 列名应在 caption 注明全称 "Variant-level accuracy"。[两人共识]
- **M5**: Figure 2 caption 应标注 "y-axis does not start at zero"（Figure 3 已有此标注）。[R2 提出, R1 同意]
- **M6**: Table 1 TRAJ "★" 标记不够醒目，建议脚注加粗或其他视觉区分。[R1 提出, R2 同意]
- **M7**: ICC 在 Oracle 分析中的 conservative lower bound 论证在 Appendix A，建议在正文更显著位置简要提及。[R1 提出, R2 部分同意, Director 从 Should-Fix 降级]

---

## Questions for Authors

1. 如果 32B+ CWM 消除 format collapse（如 14B 收敛趋势所暗示），论文的 formulation comparison 结论需如何修正？是否本质上是 "capacity moderates formulation choice" 而非 "complexity moderates formulation choice"？[R2-Q1, R1 支持]
2. 是否考虑过使用更窄的 SESOI（如 ±1pp）并接受等价性不确认？在 deployment 场景中，±1pp 和 ±2pp 的实际差异是什么？[R1-Q1]
3. TRAJ 使用 lr=2×10⁻⁴ 的理由是 "due to the smaller training set"，为什么不将 TRAJ 的 lr 也设为 5×10⁻⁵ 并增加 epochs？[R1-Q2]
4. CWM default-to-pass 是否考虑过替代方案（如 default-to-fail 或 abstain）？替代方案下 gap 会如何变化？[R1-Q4]
5. §2.2 的 Expected Failure Modes 在实验中是否有任何发现违反了预测？如果没有，实验贡献如何区别于 confirmation study？[R2-Q2, R1 partial REBUT]

---

## Missing References

- **RLTF** (Liu et al., 2023): 使用 execution feedback 训练 code generation 的 RL 方法，与 execution-free 方向形成对比。[R2 提出]
- **CodeBERTScore** (Zhou et al., 2023): 已引用但仅一次。在 formulation taxonomy 中讨论排除原因（metric vs verification formulation）。[R2 提出]
- 整体 Related Work 覆盖充分，无重大遗漏。[两人共识]

---

## External Review

**状态**: 未请求。

---

## Visual Layout Check（非评分项）

**状态**: 完成 (2026-05-23T13:31-13:34)
**发现**: 0 critical, 1 warning, 16 info

- ⚠️ **Warning**: 连续 2 页纯文本（Abstract + Introduction），首个视觉锚点（Figure 1）延迟到 page 3。审稿人前 2 页只看到密集文字。考虑将 Figure 1 或 teaser table 提前到 page 2。
- ✓ Figure 1 三面板概念图清晰可读，颜色区分度好
- ✓ Figure 2 + Table 2 同页，密度高但不拥挤
- ✓ 所有表格 booktabs 风格一致，最优值加粗，小数位一致
- ✓ References 无未解析引用，排版正常
- ✓ Limitations 简短（~1/3 栏），符合 EMNLP 要求
- ✓ Appendix 表格格式规范，Prompt Templates 代码块清晰

---

## Overall Assessment

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 2.5 | 2.75 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.0 | **3.0** |

**Overall: 3.0 / 5 — Findings**

**裁定依据**：
1. **方法论贡献真实**——统计框架（TOST+ROPE+Holm+clustered bootstrap）在 NLP 实证研究中属标杆级别，failure mode taxonomy 有独立实践价值。
2. **三层叙事结构逻辑清晰**——fine-tuning necessary → function-level equivalence → repo-level divergence，数据支撑充分。
3. **Excitement 受限于研究类型**——核心发现在概念上可预期（短输出时 formulation 无差异、长输出时 generation 困难），量化的 surprise factor 不足以达到主会议标准。这是 empirical comparison 论文的 inherent limitation (R6-N4, wont_fix since round 11)。
4. **交叉分享后无未解决 Critical issue**——R1 的 3 个 Critical 均被 R2 成功 downgrade/rebut（SESOI→Should-Fix, 因果归因→事实错误, TRAJ→Should-Fix）；R2 的 2 个 Critical 中 novelty 被 R1 REBUT，CWM baseline 两人共识降为 Should-Fix。
5. **7 项 Should-Fix 均可在修改周期内解决**——Table 3 加列、Appendix G 补 p-values、§3.4/§4 微调措辞等，不影响核心结论。
6. R1 (3.5) 和 R2 (3.0) 均认为论文处于 Findings 到 Borderline Conference 区间。Director 采纳更保守的评估 (3.0)，因为 novelty ceiling 是 binding constraint。

---

## Detailed Comments

### Reviewer 1（方法严谨性 + 实验有效性）

**初审**: Overall 3.5, Soundness 3.5, Excitement 3.0, Reproducibility 4.0, Confidence 4.0
- 3 Must-Fix: SESOI 预注册 (N1), repo-level 因果归因 (N2), TRAJ 非对称 (N3)
- 4 Should-Fix: CWM default-to-pass (W1), 14B hedging (W2), ICC 外推 (W3), TOST p-values (W4)

**交叉回应（对 R2）**:
- R2-N1 (novelty): **[REBUT]** — function-level 等价性反直觉、failure mode taxonomy 纯经验发现、capacity-dependent convergence 需实验建立；建议降为 Should-Fix
- R2-N2 (CWM baseline): **[AGREE]** — ≤8B capacity confound 成立，但论文已有部分 qualification
- R2-W1 (checkpoint): **[AGREE]**
- R2-W2 (label granularity): **[AGREE]**
- R2-W3 (complementarity): **[REBUT]** — negative result 有独立价值，framing 诚实
- R2-W4 (PRM/ORM): **[AGREE]**

### Reviewer 2（新颖性 + 完整性 + 写作质量）

**初审**: Overall 3.0, Soundness 3.5, Excitement 2.5, Reproducibility 4.0, Confidence 4.0
- 2 Must-Fix: novelty/confirmation (N1), CWM baseline fairness (N2)
- 4 Should-Fix: checkpoint (W1), CLS-TRAJ confound (W2), complementarity (W3), PRM/ORM (W4)

**交叉回应（对 R1）**:
- R1-N1 (SESOI): **[AGREE with downgrade]** — 论文透明披露 + Bayesian ROPE + 部署合理性 → Should-Fix
- R1-N2 (因果归因): **[REBUT]** — R1 混淆 139-cluster 交互 LPM 与 25-cluster 跨模型模型，核心论证基于事实错误
- R1-N3 (TRAJ 非对称): **[AGREE with qualification]** — 论文已多处限定，但应更早标注 → Should-Fix
- R1-W1 (default-to-pass): **[AGREE]**
- R1-W2 (14B hedging): **[REBUT]** — "consistent with" 本身即为 hedging
- R1-W3 (ICC 外推): **[AGREE with qualification]** — 论文实际做法比 R1 描述的更审慎
- R1-W4 (TOST p-values): **[AGREE]**