---
round: 3
review_mode: continue
overall_score: 3.5 - Borderline Conference (high end)
timestamp: 2026-05-21T08:12:14.002111+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 4 Consolidated Review Report — policy_ambiguity_safety

**Paper**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 via ARR May cycle (Long Paper)
**Mode**: Continue Review (Round 3 → Round 4)
**Reviewers**: R1 (方法严谨性), R2 (新颖性与完整性)
**Date**: 2026-05-21

---

## Summary

本轮审查聚焦于 Round 3 提出的 4 个 Must-Fix 和 8 个 Should-Fix 问题是否已充分解决。论文做了大量修改，方法论透明度显著提升。3 个 Critical Must-Fix（MF1/MF3/MF4）已实质性解决，MF2（human evaluation）降级为 non-blocking warning。6/8 Should-Fix 已解决，2 项残留（SF4 ICC model disclosure, SF5 mitigation backfire）。新发现 3 个 minor issues。

---

## Strengths

1. **Cross-judge calibration 超出预期**（MF1）：§4.4 新增 100-episode dual-judge 实验（McNemar p=0.606, binary κ=0.653, weighted κ_w=0.775）已是充分回应。更出色的是 §5.4 自主新增的 within-judge auth scope 验证——Claude 12%, Qwen3 26%, DeepSeek 60% 三个模型共享同一 judge (GPT-5.4)，直接排除了 auth scope 跨模型差异的 judge confound。这是超出审稿意见建议范围的作者主动补充，显著加强了 C4 exploratory 结论中最重要的发现。

2. **Incompleteness confound 处理教科书级**（MF3）：§3 定义处标注 → §5.2 upper-bound framing + logistic regression (p=0.022, <8% coefficient change) + coreferential zero-delta lower-bound (31.6%) + 5-type sensitivity analysis (omnibus p=0.079, pairwise contrasts preserved) → Limitations 指出 future orthogonalized design。论证链完整，诚实报告弱化结果（三层退化为两层），方法论上无可挑剔。

3. **C4 exploratory 降级彻底一致**（MF4）：标题、Abstract、§1 contributions、§5 opening、§5.4 标题、Discussion、Conclusion 七处全部标注 [Exploratory] 或等价 hedge。Claim hierarchy (C1/C2 primary > C3 inconclusive > C4 exploratory) 与 evidence strength 完全对齐。

4. **核心实验设计依然扎实**：matched-pair causal identification (300 clause pairs × 2 conditions × 5 models = 2,997 episodes)、perturbation control (Δ=3.33pp, CI containing zero)、ICC=0.919 reproducibility、TOST 7-margin sensitivity analysis。C1 的 +34.0pp effect (OR=15.1, p<10⁻¹⁰⁵) 在方法论上难以挑战。

5. **SESOI justification 逻辑清晰**（SF1）：±15pp 同时锚定于实践意义（安全部署中 15pp 差异需区别对待）和 perturbation noise floor（CI 上界 13.3pp < 15pp）。

---

## Weaknesses

### 残留 Warning（非 blocking，但影响竞争力）

1. **Human evaluation baseline 完全缺失**（MF2, downgraded to warning）：论文所有评估（violation 判定 2,997 episodes + failure mode coding 614 traces）均为 LLM-only。Cross-judge calibration 证明两个 LLM 互相同意，但无法证明任一 LLM 与人类判断一致。Matched-pair 设计控制 systematic judge bias，但 type-specific 或 model-specific bias 仅被 calibration 数据 bounded 而非 eliminated。同 venue 标准在演变（R-Judge, ToolEmu 包含 human eval；AgentAuditor 不要求），但 human baseline 仍是与 top-tier 竞争的 differentiator。

2. **Mitigation Discussion 选择性呈现**（SF5/R4-NEW-2）：§7 Practical Implications 推荐 "type-specific disambiguation instructions" 并报告 pooled -8.5pp 效果，但完全未提及 DeepSeek 在 scopal (+2.0pp) 和 incompleteness (+4.0pp) 上的反向效果。对实践者而言，不知道某策略在特定 model-type 组合上 backfire 有误导风险。一句话 caveat 即可修复。

3. **Conclusion 叙事断裂**（R4-NEW-1）：§5.2 和 Abstract 都标注了 incompleteness 三层→两层退化，但 Conclusion 仍说 "A three-tier type hierarchy" 无任何限定。Conclusion 是多数读者唯一精读的段落，应与 Abstract/§5.2 保持一致。~10 词修改。

4. **ICC model selection 未披露**（SF4）：§4.5 报告 "5 per type × 2 models × 3 replicates" 但未说明哪 2 个模型。ICC=0.919 的泛化性取决于此——如果选的是最稳定的模型，ICC 可能高估。~5 词修改。

### Minor Issues（不影响接收决定）

5. **F-test df 变更未说明**（R4-NEW-2）：§5.4 报告 F(20)=1.97, p=0.006。df=20=(5-1)×(6-1) 是完整 5×6 factorial 的正确 df，但 readers 需要知道 interaction model specification。一句话说明。

6. **Discussion auth scope 数字不一致**（R4-NEW-3）：Discussion 用 "Claude 12% vs DeepSeek 60%"（within-judge context），Abstract/Results 用 "12% to 64% (GPT-5.4)"。不是错误但 framing 不统一。

7. **引用 minor mismatches**（M1）：lassiter_goodman_2017 年份（online-first 2015 vs print 2017）、ferrari_defects_2018 bib key vs first author。不影响引用显示。

---

## Questions

1. §5.4 F-test 的 model specification 是什么？是否使用了 Type III SS 或其他分解方式？df=20 与此前的 df=12 差异来源是什么？
2. ICC 复制实验选择了哪 2 个模型？选择标准是什么（最高/最低 violation rate？不同 judge group？）
3. Mitigation 实验中 DeepSeek 的反向效果（scopal +2.0, incompleteness +4.0）是否有假设解释？这是否与 DeepSeek 在 main study 中的 "no significant type effect" (V=0.14, p=0.28) 相关？

---

## Missing References

核心遗漏已修复（Cohen 1960, Gwet 2014, Hu et al. 2025）。残留建议（non-blocking）：
- OpenAgentSafety (ICLR 2026) — 如包含 policy compliance 评估维度则相关
- Prompt sensitivity 文献（e.g., "Assessing and Understanding Prompt Sensitivity of LLMs", EMNLP 2024 Findings）— 论文研究的 clause-level wording 变化本质上涉及 prompt sensitivity

---

## External Review

外部审稿（Stanford Agentic Reviewer via paperreview.ai）：**Skipped**（用户在 Round 3 跳过，Round 4 未重新请求）。

---

## Visual Layout Check（非评分项）

**Status**: Done (2 warnings, 8 info)

**Warnings**:
- Pages 3-5 连续纯文本（Taxonomy + Method），无 display item。建议 §3 taxonomy 加 tree diagram 或 summary table，§4 加 matched-pair 示例
- Display items 总数偏少（3 figures + 1 table = 4）；8 页实证论文通常预期 5-8 个。前半部分视觉密度低

**Info highlights**:
- Figure 1 图内文字偏小（150 dpi 下阅读吃力）
- Figure 2 尺寸偏小（仅占右栏 1/3 高度），建议扩大
- Figure 3 相邻色灰度打印可能难以区分，建议辅以 hatch pattern
- Table 1 排版专业，无溢出
- 无 margin 溢出、LaTeX 渲染错误、未解析引用
- 主文 8 页合规，Limitations 约半页覆盖 5 个方面

---

## Overall Assessment

### Score: 3.5 / 5 — Borderline Conference (high end)

**R1**: 3.5 (Soundness 3.5, Excitement 3.5, Confidence 4)
**R2**: 3.5 (Soundness 4.0, Excitement 3.5, Confidence 4)
**Director consensus**: 3.5

### 评分理由

**论文的核心贡献有效且重要**：matched-pair causal design 在 agent safety 领域是方法论创新；C1 (+34.0pp, OR=15.1) 是强健的因果效应；C2 的三层层级（含 incompleteness upper-bound caveat）提供了可操作的 type-level 风险排序；Differential Nocuity 框架和 Ambiguity Blindness (<11% awareness) 是有理论贡献的概念。

**Round 4 修改显著提升了方法论透明度**：cross-judge calibration + within-judge validation 是本轮最大亮点，incompleteness confound 的 upper-bound + lower-bound 处理教科书级别，C4 exploratory 降级彻底一致。Soundness 从 Round 3 的 3.0-3.5 提升至 3.5-4.0。

**维持 3.5 而非升至 4.0 的原因**：(1) Human evaluation 完全缺失——虽降级为 non-blocking，仍是 completeness 缺口，在 main conference 竞争中是劣势；(2) Mitigation 结果选择性呈现——推荐实践策略但不报告 backfire 场景；(3) 几处 minor 叙事不一致（Conclusion caveat, auth scope 数字）。

**升至 4.0 (Conference) 的条件**（均为 camera-ready 级别 editorial fix）：
1. Conclusion 加 incompleteness caveat (~10 词)
2. Discussion mitigation 加 DeepSeek backfire caveat (~1 句)
3. 披露 ICC 的 2 个 models (~5 词)
4. F-test df specification (~1 句)
5. Auth scope 对比数字统一或加说明 (~半句)

以上 5 项修改总计约 5 句话。如在 camera-ready 前完成，两位 Reviewer 均表示将修订评分至 4.0。

### EMNLP 2026 ARR 定位

- **Main Conference (4.0)**: 需完成上述 5 项 + 理想情况下补充 ~50 episodes human annotation
- **Findings (3.0-3.5)**: 当前状态已满足 Findings 标准
- **当前位置**: 3.5 = Borderline Conference，处于 Conference/Findings 边界的 Conference 侧

---

## Detailed Comments

### Camera-Ready Action Items（按优先级排列）

| # | Issue | Fix | Effort | Impact |
|---|-------|-----|--------|--------|
| 1 | Conclusion incompleteness caveat (R4-NEW-1) | Add "(reducing to two tiers when incompleteness is excluded)" | ~10 words | Narrative consistency |
| 2 | Mitigation backfire (SF5) | Add DeepSeek scopal/incompleteness reverse effect sentence | ~1 sentence | Practical reliability |
| 3 | ICC model disclosure (SF4) | Name the 2 models used for replication | ~5 words | Transparency |
| 4 | F-test df explanation (R4-NEW-2) | State "full 5×6 factorial interaction, df=(5-1)×(6-1)=20" | ~1 sentence | Methodological clarity |
| 5 | Auth scope number consistency (R4-NEW-3) | Unify Discussion with Abstract/Results framing | ~half sentence | Consistency |
| 6 | Human annotation (MF2) | ~50 episodes human-LLM agreement on binary violation | Moderate effort | Competitiveness for main |

Items 1-5 are editorial (~5 sentences total). Item 6 is the only substantive effort and determines Conference vs Findings positioning.

### Cross-Round Progress Summary

| Round | Score | Key Issues | Status |
|-------|-------|-----------|--------|
| Round 1 | — | Initial identification of MF1/MF3/SF1-SF4 | — |
| Round 2 | — | SF6-SF8 added, some partial fixes | — |
| Round 3 | 3.0 | 4 MF + 8 SF. Major gaps: cross-judge, human eval, incompleteness, C4 overclaiming | Fresh review |
| **Round 4** | **3.5** | MF1/MF3/MF4 resolved. MF2 downgraded. 6/8 SF resolved. 3 new minor. | **+0.5** |

论文从 Round 3 的 3.0 (Findings) 提升至 3.5 (Borderline Conference)，修改质量显著且超出预期（尤其 within-judge validation）。距离 4.0 仅差 editorial-level fixes。