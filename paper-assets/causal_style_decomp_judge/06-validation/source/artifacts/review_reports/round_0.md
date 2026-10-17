---
round: 0
review_mode: 
overall_score: 2.5 / 5 (Borderline Findings)
timestamp: 2026-05-21T02:05:50.678937+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告 — Round 1（修正版）

**论文**: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison"
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审稿人**: R1 (Methods & Experiments) + R2 (Novelty & Related Work)
**日期**: 2026-05-21
**修正说明**: 本版修正了初版报告中基于 Director brief 的 "仅 1 clean cell" 过度解读。R2 在收敛轮确认 7/9 cells 统计显著性由 PDF 支持，original preference confound 是 marginal (p=0.072) 而非 definitive，评分从 2.0 回调至 2.5。R1 部分反驳了 BT 建模的必要性。新增 CLMM 作为判断核心 claim 的必要实验。

---

## Summary

论文提出 5 阶段反事实协议（counterfactual style rewriting → NLI content gate → position control → Likert control → original preference control），在 3 judges × 3 benchmarks 网格上比较 Likert 与 pairwise 对 formality style bias 的检测灵敏度。核心发现：pairwise 在 7/9 cells 中检测到显著 formality bias，Likert ATE 仅 1/9，binarized Likert 0/9。论文据此提出 "Likert Blindspot" 概念。

---

## Strengths

- **S1** 研究问题有直接实践意义：如果 Likert 系统性漏检 style bias，影响所有 LLM-as-judge 评估管线 [R1+R2 共识]
- **S2** Pipeline 设计系统性强，四阶段协议每步针对特定 confound，逻辑完整 [R1+R2 共识]
- **S3** 3 judges × 3 benchmarks 网格覆盖多 LLM 家族（GPT-4o / Claude / Gemini）[R2-S3]
- **S4** **Binarized-Likert 诊断设计是最强方法论贡献**——通过共用 sign test 隔离 measurement structure 作为灵敏度差异来源。这一诊断思路在 psychometrics 文献中不常见，构成独立方法论增量 [R1 独立识别，R2 部分认可]
- **S5** 人工 NLI 验证（n=100, 91% agreement）为 content preservation gate 提供可信质量保证 [R2-S5]
- **S6** Scaled replication（n=500）确认效应量稳定 [R2-S6]
- **S7** Limitations 讨论诚实：明确承认因果框架近似性、样本量限制、仅检测不纠正 [R1+R2 共识]

---

## Weaknesses（按严重程度排序）

### Must-Fix（影响接收决定）

**W1** [critical, R1+R2 共识] **"Blindspot" 实为 sample-size-dependent efficiency gap**
Binarized Likert 在 n=500 时 p=0.055（R1 报告），距显著仅一步之遥。Likert 不是 categorically blind，而是在 typical n=100 下 underpowered。标题 "The Likert Blindspot" 暗示定性测量失败，实际是定量效率差异。论文 §6 Discussion 自述 "complementary rather than adversarial"，与标题的强势措辞矛盾。

**W2** [critical, R1+R2 共识] **CLMM 是判断核心 claim 的必要实验——当前处于 underdetermined 状态**
论文用 t-test on ATE 和 binarized sign test 评估 Likert 灵敏度，但 Likert 数据是 ordinal 非 interval。CLMM（Cumulative Link Mixed Model）或 ordinal logistic regression 能更好利用 ordinal 结构。**关键**：如果 CLMM 显著，则"Likert Blindspot"不是 Likert 量表的固有缺陷，而是分析方法（ATE）的缺陷——核心 claim 的本质定义将改变。作者必须在 revision 中报告 CLMM 结果。

**W3** [critical, R1] **因果语言与实际框架严重不匹配**
大量使用 "counterfactual"、"interventional"、"ATE" 等因果术语，但无 DAG、未讨论 SUTVA、无 sensitivity analysis for unmeasured confounders。R2 建议更准确定位为 "quasi-experimental interventional study"。降调因果语言会削弱 novelty narrative 但避免不必要的审稿攻击面。

**W4** [critical, R1+R2 共识] **NLI gate 67% false-negative rate 造成的选择偏差未分析**
最终分析仅基于原始数据 ~1/3。"Lower-bound" claim 需要未验证的假设：NLI-rejected pairs 的 bias 方向与 accepted pairs 一致。R2 补充：应报告 NLI-accepted vs rejected pairs 的 style distance 分布——如果 accepted pairs 的 style distance 系统性偏小，则 bias estimate 可能被压低。

**W5** [critical, R1+R2 共识] **NLI 阈值 0.90 无 justification，per-axis 调整引入 researcher degrees of freedom**
Verbosity axis 从 bidirectional 改为 direction-aware gating 是 post-hoc 方法修改。R2 指出这削弱了论文对 RATE 方法论批评的可信度。阈值 sensitivity analysis 应在正文（非 appendix）。

**W6** [critical, R2; R1 部分反驳] **Novelty 不足——已知心理测量学现象的 domain transfer**
Likert vs forced-choice sensitivity gap 是 Thurstone (1927) 以来的共识。R1 部分反驳：binarized-Likert 诊断设计并非简单迁移，在 LLM judge 领域的系统性量化有 Findings-level 价值。**收敛后仍为核心分歧点**——R1 认为足以支撑 Findings，R2 认为 evidence breadth 不足。

**W7** [critical, R2; R1 确认版本差异] **引用系统不完整**
R2 报告 placeholder arXiv IDs（"arXiv:2406.xxxxx"）和 broken citations；R1 审阅的 best 版本有参考文献但引用数偏少。双方共识：目标 20-30 篇引用。

**W8** [critical, R2; R1 AGREE with nuance] **RATE 批评缺乏 matched replication**
§5.3 的 binarized-Likert internal comparison 是 sound 的（R1 确认），但从 internal result 到 "RATE's Likert understates bias" 的 external generalization 是 ecological validity 跨越。应弱化措辞或补充 evidence。

### Should-Fix（影响评分但不一票否决）

**W9** [warning, R1+R2 最强共识] **全文零图表**。至少需要：(1) Power curve（pairwise vs binarized Likert vs Likert ATE, x=n, y=power）——直接回应 blindspot vs efficiency gap 争论；(2) Forest plot（9 cells win rate + 95% CI）——让 pattern 自明；(3) Pipeline diagram（四阶段 + attrition）。对 borderline 论文，presentation 可能是 tipping point。

**W10** [warning, R1+R2 共识] **范围窄于标题承诺**——仅 formality 有完整 3×3 结果。Verbosity（Table 8）和 register（Table 9）各仅 1 个 cell，register 未达显著（p=0.068）。标题 "Style Bias" 与实际覆盖不匹配。

**W11** [warning, R1+R2 共识] **Original preference confound OR=1.65, p=0.072 为 marginal**——需要 per-cell logistic regression formal partial-out。注：此 confound 是 marginal 而非 definitive，7/9 cells 的统计显著性由 PDF 确认，但缺乏 per-cell 独立 confound 控制。

**W12** [warning, R1+R2 共识] **Consistency filtering ~40-50% data loss 未分析**——丢弃的 position-inconsistent pairs 可能系统性保留 formality effect 更强的 pairs，导致 win rate 高估。缺少完整 attrition 表。

**W13** [warning, R1+R2] **Likert ATE 方向反转（Claude×LLMBar）**——Likert 和 pairwise 可能测量不同构念。"Blindspot" narrative 隐含 same-construct 假设需要质疑。

**W14** [warning, R1+R2] **Multiple comparison correction 不一致**——Holm-Bonferroni 仅 Table 2，其他 ~20+ 次检验未校正。

**W15** [warning, R1+R2] **Post-hoc power analysis 方法论问题**——observed effect size 做 power analysis 是 circular（Hoenig & Heisey 2001），"5× efficiency gap" 可信度受限。

**W16** [warning, R2; R1 部分反驳] **缺少 Bradley-Terry 建模**——R1 反驳：sign test 在此场景 sufficient（nonparametric、直接回答 binary 问题、complete paired data 不需 BT 参数化假设）。BT 可作 supplementary robustness check，但非 necessary。

**W17** [warning, R2; R1 确认] **Related work 覆盖不完整**——CalibraEval、FairEval、BT for judge evaluation、心理测量学理论文献缺失。

---

## Reviewer Consensus [AGREE]

1. **Pipeline 设计在逻辑上合理**，方法论训练扎实 [R1+R2]
2. **Binarized-Likert 诊断设计是最有价值的方法论贡献** [R1 提出，R2 部分认可]
3. **"Blindspot" 实为 efficiency gap**——n=500 时 binarized Likert 接近显著 [R1+R2 强共识]
4. **CLMM 是判断核心 claim 的必要实验**——当前 underdetermined [收敛轮新增共识]
5. **全文零 figures 是严重 presentation 缺陷** [R1+R2 最强共识]
6. **标题 scope 宽于实际覆盖** [R1+R2]
7. **Limitations 讨论诚实** [R1+R2]
8. **Original preference confound 为 marginal (p=0.072)，需 formal analysis 但非 definitive** [收敛轮修正共识]
9. **NLI gate 设计意图合理，但执行和验证不够严格**——sensitivity analysis 可解决 [R1+R2]
10. **Sign test 作为 primary analysis 是 justified 的**；BT 可作 supplementary [R1 反驳 R2，R2 未再争议]

## Reviewer Divergence

1. **Novelty 是否达到 Findings 水平**（核心分歧，0.5 分差距来源）：R1 认为 binarized-Likert 诊断设计 + LLM-specific 系统量化构成 Findings-level 贡献；R2 认为 evidence breadth 不足以支撑 even Findings（但最终给 2.5 Borderline Findings，未完全否定）。
2. **引用问题严重程度**：可能存在审阅版本差异（R1 best 版本有参考文献，R2 版本有明显缺陷）。

---

## Questions for Authors

1. 请报告每个 judge×benchmark cell 的完整 attrition 数据（generated → NLI pass → consistent → final n）
2. NLI 阈值 0.90 是 pre-specified 还是 post-hoc？请提供 threshold sensitivity analysis（0.85/0.90/0.95）**在正文中**
3. NLI-rejected 但 human-valid 的 pairs 中 judge 的 formality preference 方向是什么？请同时报告 NLI-accepted vs rejected pairs 的 style distance 分布
4. 请执行 CLMM/ordinal logistic regression 分析 Likert 数据——结果决定 "Likert Blindspot" claim 的本质定义
5. 对每个 cell 做 logistic regression (judge_choice ~ is_formal + is_original)，报告 formality effect 在控制 original preference 后的变化
6. 请解释 Claude×LLMBar 的 Likert ATE 方向反转——Likert 和 pairwise 是否在测量不同构念？
7. Consistency filtering 去掉的 ~40-50% pairs 中 position bias 方向如何？
8. Abstract 的 headline win rate 是否应以 n=500 的 effect size 为主？
9. 相对于 Karpinska et al. 和 Novikova et al.，本文贡献具体超越 domain transfer 的部分是什么？
10. 所有引用是否真实可验证？Placeholder arXiv IDs 需修复。

---

## Missing References

- **CalibraEval** — LLM judge calibration
- **FairEval** (Wang et al., 2023) — judge fairness 前驱工作
- **Chatbot Arena / Bradley-Terry** 文献 — pairwise comparison in LLM evaluation
- **心理测量学理论** — DeCoster et al. (2011), Simms et al. (2019) 等 Likert vs forced-choice 理论分析
- **LLM-as-Judge 综述** — post-Zheng et al. (2023) survey papers

---

## External Review (Stanford Agentic Reviewer)

未请求。

## Visual Layout Check

未派发。

---

## Overall Assessment

### 评分汇总

| Reviewer | Overall (ARR) | Soundness | Excitement | Confidence |
|----------|---------------|-----------|------------|------------|
| R1 | **3.0** (Findings) | 3/5 | 3/5 | 4/5 |
| R2 | **2.5** (Borderline Findings) | 3/5 | 2.5/5 | 4/5 |

### Director 综合评分: **2.5 / 5 (Borderline Findings)**

**判断依据**：

R1 (3.0) 和 R2 (2.5) 的差距收敛至 0.5 分，分歧仅在 novelty 判断。Director 取 2.5 (Borderline Findings) 基于以下权衡：

**支持 Findings (3.0) 的因素**（R1 视角）：
- Binarized-Likert 诊断设计有独立方法论价值，并非简单 domain transfer
- GPT-4o×LLMBar 上的 primary evidence 在多项 confound 控制下可信
- 对 LLM-as-judge 社区有直接实践指导意义
- Pipeline 设计系统，Limitations 诚实

**支持 Borderline Findings (2.5) 的因素**（R2 视角 + 共识问题）：
- 8 个 critical issues 叠加（efficiency gap 矛盾、CLMM underdetermined、因果框架缺失、NLI 选择偏差、阈值无 justification、novelty 不足、引用缺陷、RATE 批评无支撑）
- Fully controlled evidence 集中在 1-2 个 cells，generalization 是 suggestive
- 零 figures + scope 窄于标题——presentation 不达标
- CLMM 是 existential test：如果 CLMM 显著，核心 claim 被推翻

**结论**：论文在有实践意义的问题上做了设计合理的实验，binarized-Likert 诊断设计有独立价值。但 critical issues 密度过高，且 CLMM 这一 existential test 未执行，使得核心 claim 处于 underdetermined 状态。在 CLMM 结果出来前，无法给出高于 Borderline Findings 的评分。

---

## Resubmission Roadmap

**Priority 1（解决后可达 Findings 3.0）**：
1. 执行 CLMM 分析——决定论文 contribution 的本质
2. NLI threshold sensitivity analysis（至少 3 阈值点，正文中报告）
3. 报告 NLI-rejected pairs 的 bias 方向和 style distance 分布
4. 添加 power curve + forest plot + pipeline diagram（至少 3 张 figures）
5. 修复全部引用，补充 missing references 至 20-30 篇

**Priority 2（解决后可达 Borderline Conference 3.5）**：
6. Per-cell confound analysis（logistic regression partial out original preference）
7. 补做 verbosity 完整 3×3 实验（或收窄标题至 formality）
8. 将 "blindspot" 重新框定为 "sensitivity gap at typical n"（配 power curve 支撑）
9. 完整 attrition 表 + inconsistent pairs 探索性分析

**Priority 3（解决后可达 Conference 4.0）**：
10. DAG + SUTVA 讨论（或降调因果语言为 quasi-experimental）
11. BT 建模作为 supplementary robustness check
12. 解释 Likert ATE 方向反转的理论含义
13. 弱化 RATE 批评措辞或补充 matched replication