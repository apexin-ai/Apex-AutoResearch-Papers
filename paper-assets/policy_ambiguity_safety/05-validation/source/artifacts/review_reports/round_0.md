---
round: 0
review_mode: 
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-20T17:12:50.325195+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告 — Round 1（最终版，含 R2 TeX 源码验证）

**论文**: "Not All Policy Ambiguity Is Equal: Specification-Layer Ambiguity Poses Greater Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审稿日期**: 2026-05-20
**Reviewer 编排**: R1（Methods & Experiments）+ R2（Novelty / Related Work / Completeness）
**轮次**: Round 1（初审 → 交叉回应 → R2 TeX 验证 → 收敛）

---

> **重要修订说明**：R2 在交叉回应后对 TeX 源码进行了精读，发现初审中多项"数值不一致"系 PDF 图像误读。TeX 源码确认论文数值内部完全一致。这一修正同时解释了 R1 报告中部分偏低的数值（judge F1, ICC, V）——很可能也是 PDF 误读导致。review_context.yaml 独立确认了 R2 的 TeX 读数。本最终版整合了这一关键修正。
>
> **关键数值修正（TeX 确认）**：
> - Overall binary effect: **+35.8pp**, CI **[33.1, 38.5]**（非初审的 31.9pp）
> - Layer gap effect size: **d = 0.68**（非初审的 0.86）
> - Model×Type interaction: **p = 0.41**（唯一值，非 0.062 或 0.15）
> - Judge F1: overall **0.91**, per-type **≥0.87**（非 R1 报告的 0.72/0.71）
> - ICC: overall **0.84**, per-type **0.79-0.87**（非 R1 报告的 0.72/0.65-0.66）
> - Cramér's V: **0.24**（非 R1 报告的 0.17）
> - DeBERTa F1: **0.89**（非初审的 0.78）

---

## Summary

论文提出 "Differential Nocuity" 框架，将 requirements engineering 中的歧义分类学（Berry & Kamsties, 2003）引入 LLM agent safety。通过 300 clause pairs × 5 模型 × 2 conditions = 3,000 episodes 的 matched-pair 实验（基于 τ²-bench），建立了歧义类型与 agent 安全违规之间的因果关系。核心发现：(1) 所有歧义类型显著提高违规率（+35.8pp）；(2) specification-layer 违规率约为 linguistic-layer 的 1.66 倍（gap d=0.68）；(3) 类型层级跨 5 模型 × 3 架构家族一致（interaction p=0.41）。

---

## Strengths

1. **因果设计强度在同类文献中最强**：Matched-pair + perturbation control（Δ_perturb=3.3pp vs Δ_ambig=36.5pp, ratio 0.09）清晰排除了 general prompt fragility。[R1, R2 共识]

2. **核心发现新颖且有实践价值**：Spec-layer ≈ 1.66× ling-layer（d=0.68）对 policy auditing triage 有直接指导意义。"Differential nocuity" 概念填补了 "歧义存在" → "哪种歧义最危险" 的关键 gap。[R2]

3. **测量链质量高**（TeX 确认）：Judge F1=0.91（per-type ≥0.87），ICC=0.84（good），cross-judge κ=0.86。论文的核心效应量建立在可靠的测量基础上。[R2 修正版]

4. **5 模型 × 3 架构家族复现**：Model×Type interaction p=0.41（firmly non-significant），类型排序完全一致。[R1, R2]

5. **Error analysis 揭示 layer-level separation**：Spec-layer 的 unauthorized assumption / scope escalation vs. ling-layer 的 misparse / surface adoption（χ²>35, p<0.0001）。Coreferential 的独特 avoidance behavior（44% vs 8%）。[R1, R2]——**前提是补充 ICR**。

6. **数值内部一致**（TeX 确认）：Abstract、正文、Table 三处核心数字完全一致。[R2 修正版]

7. **完整数据承诺**：300 clause pairs + evaluation scripts + annotated traces。[R1, R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [R2-N1-rev, NEW] **格式严重违规——desk reject 条件**
- 使用 `\documentclass[11pt]{article}` 而非 ACL 官方双栏模板
- 单栏约 9.5 页，转双栏预计 12-14 页，远超 8 页限制
- Limitations 作为 Discussion 的 `\paragraph` 而非独立 `\section`
- **修复要求**：(1) 切换至 ACL 模板，(2) 大幅压缩正文至 8 页，(3) Limitations 独立为 section

**MF-2** [R1-N1] **Info delta 作为层级间混淆变量未被充分控制**
- Spec-layer 消歧天然需要更多信息（auth_scope +3.4, incompleteness +4.1 tokens vs lexical +0.9, scopal +1.3）
- TeX 确认 logistic regression 中 info delta covariate p=0.50（不显著），但仅为 type-level proxy
- **修复要求**：报告 per-type info delta distribution，用 per-clause info delta 做 covariate，展示层级效应是否 robust

**MF-3** [R2-N2, R1 AGREE] **贡献数量膨胀——5 → 3 项**
- C3 是 C2 的 robustness check；C5 是 C1 的维度；C4 "mechanistic" overclaimed（待 ICR 补充）
- **修复要求**：合并为 3 项核心 contributions

**MF-4** [R2-N3, R1 AGREE] **RE 文献覆盖严重不足**
- 全文仅 16 篇引用。缺 Chantree et al. (2006, 2008)、Ferrari et al. (2017-2019)、NLP4RE 社区
- **修复要求**：补充 RE 文献 5-8 篇，Related Work 扩展至 1.2-1.5 页

**MF-5** [R1-W5, R1+R2 升级] **Error analysis 缺 inter-coder reliability**
- 300 traces 编码为 6 种 failure modes，未报告编码者、coding scheme、ICR、分歧解决机制
- 两位 Reviewer 独立升级为 Must-Fix
- **修复要求**：至少 double-code 20-30% traces，报告 κ/α

### Should-Fix（影响评分但不一票否决）

**SF-1** [R1-W1] **生态效度——synthetic clauses sentence length 显著更短 (p=0.04)**
- 建议承认差异 + length-stratified subgroup analysis

**SF-2** [R1-W3, R2 AGREE] **TOST ±15pp equivalence margin 缺乏理论论证**
- 建议多梯度 sensitivity analysis（±5/10/15/20pp）

**SF-3** [R1-W4, R2 AGREE] **Qwen3-8B 层级反转**
- TeX 确认 interaction p=0.41（非 borderline），universality claim 比初评时更稳固
- 但 Qwen3-8B layer gap 仍小，建议限定 C4 为 "robust across frontier models"

**SF-4** [R2-W1, R1 AGREE] **Disambiguation Channel "Hypothesis" overclaimed**
- TeX 确认 judge 对 coreferential F1=0.87——观察性证据比初评时更可靠
- 仍建议改称 "framework/explanation"，Future Work 提出 manipulation experiment

**SF-5** [R2-W2] **心理语言学联系浮于表面**
- 缺 Li et al. (2024)、Poesio & Artstein (2005, 2008)

**SF-6** [R2-W3, R1 AGREE] **Convergent-but-wrong 理论化不足**
- 论文未报告 convergent-but-wrong 的比例分解。建议提出 "systematic nocuity"

**SF-7** [R2-W4-rev, NEW] **可疑引用**
- τ²-bench arXiv ID "2406.12345" 疑似占位符
- DRIP-R (Li et al. 2024) 无法验证真实性
- Toolformer 标注 NeurIPS 2024 实为 2023
- 建议确认所有引用真实性

**SF-8** [R1-W6, R2 AGREE] **Perturbation control 仅 API 模型**
- R2 认为不致命。建议 Limitations 中承认

**SF-9** [R2-W5] **CL 侧内容过薄——venue fit concern**
- R2 对 *ACL venue fit 表示保留：CL 侧桥墩较弱

**SF-10** DeBERTa 分类器
- TeX 确认 F1=0.89（非 0.78），结果合理
- 仍建议区分 ambiguity detection vs nocuity prediction，报告 k-fold CV

---

## Withdrawn Issues（TeX 验证后撤回/降级）

| 原 Issue | 初始严重度 | TeX 验证结果 | 最终状态 |
|----------|-----------|-------------|---------|
| 数值不一致（R2-N3-old） | critical | TeX 确认全文统一：+35.8pp, CI [33.1, 38.5], d=0.68, p=0.41 | **撤回** |
| Judge 校准不足（R1-N2） | critical | TeX 确认 per-type F1≥0.87, overall 0.91, κ=0.86 | **降为 info** |
| ICC 仅 moderate（R1-W2） | warning | review_context 确认 ICC=0.84 (good), per-type 0.79-0.87 | **降为 info** |
| V=0.17 too small | warning | V=0.24 (≈6% variance, not 3%) | **数值修正** |
| DeBERTa F1=0.78 | warning | F1=0.89 | **降为 minor** |

**Director 注**：R1 的初审中有多项基于具体数值的 critical concerns（judge F1=0.72, ICC=0.72, V=0.17）。TeX 源码和 review_context.yaml 独立确认这些数字均偏低——很可能与 R2 的初审一样源自 PDF 图像误读。TeX 确认后的真实数值显著改善了论文测量链的评估。**R1 的方法论框架（info delta confound, error analysis ICR, perturbation scope）仍然有效，但其数值层面的 critical concerns 已被修正。**

---

## Reviewer Consensus [AGREE]

1. **Claims 证据强度三层递减**：C1（robust, +35.8pp）> C3（real, d=0.68, 但 within-layer 比较仍 noisy）> C2 6-type ranking（V=0.24, modest）。聚焦 spec > ling 2-level distinction。

2. **因果设计是最大优势**：Matched-pair + perturbation control 在 agent safety 文献中罕见。

3. **测量链比初评更可靠**（TeX 修正后）：Judge F1≥0.87, ICC=0.84, 数值内部一致。核心效应建立在 solid measurement 基础上。

4. **贡献需精简**：5 → 3 项。

5. **格式违规是最紧迫的问题**：desk reject 条件，必须首先解决。

6. **RE 文献和 error analysis ICR 是 substance 层面的主要缺口**。

7. **Disambiguation channel 应降级为 framework**，但观察性证据比初评时更可靠（judge F1=0.87）。

---

## Reviewer Divergence

**已收敛：**
1. **数值争议**：R1 报告的低数值 vs R2/TeX 的高数值——TeX 精读确认 R2 正确。**收敛**：论文数值一致。
2. **因果推断强度**：R2 初始质疑 → R1 反驳 → 收敛："first causal study" acceptable，需区分 design soundness vs estimate precision。

**未完全收敛（供 AC 参考）：**
3. **Venue fit**：R2 认为 CL 侧过薄。Director 判断：合理 concern 但不构成 rejection 理由。

---

## Questions for Authors

1. **[格式]** 是否有 ACL 双栏模板版本？计划如何压缩至 8 页？
2. **[方法论]** Per-type info delta distribution（mean±SD）？Per-clause info delta 做 covariate 后 layer coefficient 变化？
3. **[方法论]** Error analysis 300 traces 编码者身份、数量、inter-coder κ？
4. **[文献]** 为什么遗漏 Chantree et al. (2006, 2008)？
5. **[引用]** τ²-bench arXiv:2406.12345 是否为占位符？DRIP-R 是否已正式发表？Toolformer 年份？
6. **[理论]** Disambiguation channel：是否考虑过操纵实验？
7. **[理论]** Convergent-but-wrong 的 exact proportion？在 B&K 框架中的定位？
8. **[格式]** 论文标题：PDF 为 "Differential Nocuity..." vs TeX 为 "Not All Policy Ambiguity Is Equal..."——最终标题？
9. **[格式]** Table 12 列出 PolicyBank 但 References 中无此引用——遗漏还是错误？

---

## Missing References

**必须补充**：
- Chantree et al. (2006, RE'06; 2008, RLAC) — nocuous ambiguity 自动检测
- Ferrari et al. (2019, ASE Journal) — NLP-based RE ambiguity detection

**强烈建议**：
- Li et al. (2024) — LLM garden-path processing
- Poesio & Artstein (2005/2008) — anaphoric ambiguity annotation

**需确认/替换**：
- τ²-bench (Yao et al. 2024) — arXiv ID 疑似占位符
- DRIP-R (Li et al. 2024) — 真实性待确认
- Toolformer (Schick et al.) — 年份 2024→2023

---

## External Review (Stanford Agentic Reviewer)

**状态**：未请求。项目未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态**：未派发（PDF 路径未配置）。R2 的 TeX 源码分析部分替代了视觉审查功能——确认了格式违规（非 ACL 模板）。

---

## Overall Assessment

**Consolidated Score: 3.5 (Borderline Conference) / 6-point scale: 4 (Weak Accept)**
**Confidence: 4/5**

**R1 最终评分**: 4 (Weak Accept) / ARR 3.5, Confidence 4/5
**R2 最终评分**: 4 (Weak Accept) / ARR 3.5, Soundness **4/5**（↑ from 3/5 after TeX verification）, Excitement 4/5, Confidence 4/5

### 评估总结

**Substance 评估（TeX 修正后）**：论文的核心发现建立在可靠的测量链上（judge F1=0.91, ICC=0.84, 数值一致）。因果设计强，5 模型复现充分。Spec > ling 的 2-level distinction 有 solid evidence（d=0.68）。如果仅看 substance，本文接近 Conference (4.0) 水平。

**Execution 障碍**：
- **格式违规是最紧迫的 blocker**（desk reject 条件）——但纯机械性，完全可修复
- **RE 文献缺口**——可修复，补充 5-8 篇即可
- **Error analysis ICR**——需实际工作（double-coding），但 feasible
- **Info delta confound**——需补充分析，结果可能影响 C3 magnitude
- **贡献精简**——editorial level，容易解决
- **可疑引用**——需确认真实性，如有幻觉引用将是严重问题

**升级路径**：
- 解决 MF-1（格式）+ MF-4（文献）+ MF-5（ICR）→ 升至 **4.0 (Conference)**
- 同时解决 MF-2（info delta）+ MF-3（贡献精简）→ 稳固的 **4.0**
- 如果可疑引用确认为幻觉 → 可能降至 **2.5 (Borderline Findings)** 或更低

**当前状态**：Borderline Conference。Substance 够，execution 有可修复的缺口。最大风险点是格式（mechanical）和可疑引用（integrity）。

---

*Report generated by Review Director (Round 1 — Final, 2026-05-20)*
*Reviewers: R1 (Methods & Experiments, 4/3.5, Conf 4/5), R2 (Novelty & Completeness, 4/3.5, Soundness 4/5, Conf 4/5)*
*Consolidated: 3.5 (Borderline Conference), Confidence 4/5*
*TeX source verification resolved all numerical inconsistency concerns; measurement chain confirmed solid*