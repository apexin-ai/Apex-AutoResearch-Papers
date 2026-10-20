---
round: 13
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-23T08:27:17.176743+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 16 (Fresh)

**论文**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning
**Venue**: EMNLP 2026 ARR
**审稿模式**: Fresh（重新审稿，无上轮记忆）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+Related Work+写作质量+Claims合理性）
**交叉轮次**: 1 轮交叉分享 + 逐条 [AGREE]/[REBUT] 回应，关键问题已收敛

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取一阶逻辑约束，经去重后用 weighted partial MAX-SAT（Z3 求解）选择答案。核心发现为 null result：尽管 Z3 验证 99% 的自提取约束有效，SICA 在 6 个模型（7B–32B）、3 个推理数据集上与 majority voting 结果几乎一致（94.4% 问题答案相同），FDR 校正后无显著正效应。论文提出"Symbolic Confirmation Bias"概念（自提取约束系统性偏向模型多数答案），通过 Proposition 1（source-attribution 退化 + DPI information ceiling）给出理论论证，测试 27 种 training-free 修复策略均失败，并初步探索 cross-architecture NLI 验证作为突破路径。

---

## Strengths

**S1. 实验规模和系统性达到顶会标准。** 9 个模型 × 3 个数据集 × 60 个非退化条件 × 27 种修复策略的实验矩阵，附录 18 页包含详尽的 ablation（K sensitivity、temperature、multi-seed、oracle、error taxonomy、constraint ablation、entropy decomposition）。这种彻底性对 negative result paper 至关重要。[共识]

**S2. Oracle 控制实验设计精巧。** 用 gold FOL annotations 替换自提取约束后，FOLIO 上获得 +29.90/+13.73pp 的显著提升（Mistral-7B/Qwen2.5-14B），精确分离方法论有效性与提取质量，定位瓶颈在 extraction 而非 verification/aggregation。[共识]

**S3. 统计方法论多层次且诚实。** McNemar exact test + BH FDR 校正、bootstrap 95% CI（Table 7）、power analysis（Appendix D）、TOST equivalence test（Appendix U）、shuffle control（§5.1）。明确报告 observed power < 21%，承认 "absence of evidence is not evidence of absence"。这种统计诚实性在 NLP 社区中少见。[共识]

**S4. 诊断框架有潜在实用价值。** 三个 zero-cost diagnostics（C₀, K_eff, BR）从 K=12 pilot run 即可预测 trace-aggregation 方法是否有帮助，为实践者提供部署前筛选工具。Table 5 的 per-condition diagnostics 具体可操作。[共识，但泛化性存疑——见 W3]

**S5. Cross-architecture escape 提供建设性方向。** 不仅报告负面结果，还识别了 capability-gap 条件下 DeBERTa verifier 的显著提升路径（Mistral-7B 上 +6.67pp, p < 0.001），domain-adapted fine-tuning 进一步放大至 +12.67pp。[共识]

**S6. 附录极为详尽，可复现性强。** Prompt 模板（Appendix A）、MAX-SAT 伪代码（Appendix B）、完整 per-condition 结果、子群分析等 25 个 appendix sections。[共识]

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**W1 [Critical] Proposition 1 证明范围与声称范围不匹配 [共识]**
- **位置**: §5.1, page 6, Proposition 1 及证明
- **问题**: Proposition 1 标题 "Symbolic Confirmation Bias is Structural" 暗示普遍性，但证明由两部分组成：
  - Part (i) voting degeneration 依赖 SICA 特定的 source attribution scoring (Eq. 3)。如果用逻辑一致性（而非来源归属）对约束打分，Part (i) 不一定成立。论文 Remark 承认但未反映在 Proposition 表述中。
  - Part (ii) information ceiling 是 data processing inequality 的直接应用（I(C;Y) ≤ I(T;Y)），数学正确但平凡——只证明约束不能比 traces 包含更多信息，不排除约束通过重新组织信息打破相关模式。
- **Reviewer 共识**: R1 首提（N1 critical），R2 fully AGREE 并补充 DPI 部分是教科书推论。两者互补：R1 指出 validity/scope 问题，R2 指出 significance/novelty 问题。
- **修改建议**: 拆分为 (a) source-attribution 下的退化定理（精确但 SICA-specific）和 (b) DPI bound（普遍但弱）；正文明确区分两者适用范围。

**W2 [Critical] 统计功效 < 21% 与 negative claim 强度不匹配 [共识]**
- **位置**: Title, Abstract, §4, Appendix D
- **问题**: 
  - Observed power < 21%，MDE ≥ 1.86pp（最大样本条件）。即使 SICA 有 2pp 真实效果，~79% 概率无法检测。
  - TOST equivalence test 仅 8/16 条件达到等价显著，6 条件 underpowered，2 条件 genuinely different (negative)。±2pp equivalence margin 缺乏先验理论依据。
  - Bootstrap 95% CI（Table 7）全部包含零，宽度约 ±1.5pp。
  - 标题 "Fail to Improve" 是无条件否定声明，但论文无法排除 1-2pp 量级的正效应。
- **Reviewer 共识**: R1-N2 critical + R2-W1 major，交叉后 R2 fully AGREE R1 的详细分析。
- **修改建议**: (a) 标题软化（如 "Do Not Substantially Improve"）；(b) Abstract 加 power caveat；(c) 补充 TOST margin sensitivity analysis（±1/3/5pp）。

**W3 [Critical] Diagnostics 100% 准确率是 in-sample 评估——overfitting 风险 [共识]**
- **位置**: §5.3, §1 contributions, §7 conclusion, Abstract
- **问题**: 
  - 决策边界（C₀ < 5%, K_eff ≤ 1.30, SC < 40%）从 60 个条件推导，并在同一 60 个条件上评估 → in-sample fitting。
  - 60 个条件全为 negative cases，任何 trivial classifier（"永远预测不帮助"）都能 100%。
  - "Holdout" 验证仅 LLaMA-3.1-8B on FOLIO 1 个条件 → 不构成充分 OOD 验证。
  - 未在 positive cases（cross-architecture escape, oracle）上验证诊断框架能否正确预测"会帮助"。
- **Reviewer 共识**: R2-N3 critical，R1 fully AGREE（承认初审疏漏）。
- **修改建议**: (a) 增加完整的 held-out model family；(b) 弱化 claim 为 "correctly classify all tested conditions within our experimental scope"；(c) 讨论 OOD 失败条件。

**W4 [Critical] BR 指标存在循环论证风险——缺乏 null model [共识]**
- **位置**: §3.1 (Eq. 5), §5.1, Table 2
- **问题**: 
  - BR 通过 source attribution 衡量约束是否偏向支持多数答案。但约束从产生答案的 trace 中提取——如果 60% traces 产生答案 A，提取的约束自然更多支持 A（base-rate 效应）。
  - 论文未建立 null model：如果约束提取完全"无偏"（support 比例精确反映 trace 投票分布），BR 期望值是多少？只有观测 BR 显著超过 null expectation 才能声称"额外的" confirmation bias。
  - Shuffle control（§5.1, p.5: BR_shuffle ≈ BR_obs）确认 BR 主要反映 trace-count 分布而非提取特异性——但论文措辞混淆这两个组成部分。
- **Reviewer 共识**: R2-N2 critical，R1 fully AGREE（初审未注意此问题），但共识补充：BR 循环论证不否定 SCB 整体论证（Table 11、degeneration condition、oracle 独立支持），只影响 BR 指标本身的概念有效性。
- **修改建议**: (a) 构建 permutation-based null distribution；(b) 或将 BR 降级为描述性指标，明确声明 base-rate 组成。

### Should-Fix 问题（影响评分但不一票否决）

**W5 [Major] 新颖性定位——SCB 是已知结论的实证深化而非概念突破 [部分共识]**
- **位置**: §1 contributions, §5 "The Symbolic Mirage", Abstract
- **问题**: 
  - Huang et al. (2024) 已建立 "LLMs cannot self-correct without external feedback"。SCB 将此延伸到形式化约束自验证——可预见但不平凡。
  - Wan et al. (2025, ACL Findings) 已从认知心理学角度证明 CoT 推理中存在 confirmation bias。SCB 底层机制（model beliefs dominate downstream processing）高度重叠。
  - Proposition 1 Part (ii) 是 DPI 的教科书应用。
- **Reviewer 分歧**: R2 认为 critical（可预见的延伸），R1 partial REBUT（negative result 不应事后贬低；诊断框架 + 27 策略否证 + 机制定位是非平凡贡献）。
- **最终判定**: 部分共识——两者同意定位应从"发现"转为"系统性量化"，弱化 Proposition 1 呈现权重。R1 的反驳有一定道理：negative result paper 的价值在于提供系统性证据，不应仅因"可预见"而否定。

**W6 [Major] "Extending Huang et al. (2024) to formal verification" 是 overselling [共识]**
- **位置**: Abstract, §1 contribution 1, §5.1
- **问题**: Huang et al. 基于 value/policy iteration 分析 self-correction，本文基于 DPI + source attribution 分析 self-verification。形式化框架、假设条件和证明技术完全不同，不构成逻辑 extension。
- **修改建议**: 改为 "consistent with / complement / provide independent evidence for"。

**W7 [Major] 缺少 training-based self-verification 方法讨论 [部分共识]**
- **位置**: §2 Related Work, §7 Discussion
- **问题**: 论文几乎未讨论 S²R (Zeng et al., ACL 2025)、DuPO (2025) 等 training-based 方法。这些方法通过训练引入外部奖励信号，理论上可通过违反 Proposition 1 的 A2 假设（约束不再 trace-determined）打破信息上限。
- **Reviewer 分歧**: R2 认为 major missing，R1 partial REBUT（论文 scope 已限定为 training-free，§7 提及 trained extractors），但 R1 同意应讨论理论边界。
- **修改建议**: §2 增加一段 training-based self-verification，引用 S²R/DuPO，明确 Proposition 1 仅适用于 inference-time same-model extraction。

**W8 [Major] Multi-seed replication 不充分 [共识]**
- **位置**: Appendix X.1, Table 33
- **问题**: 仅 Mistral-7B (3 seeds) 和 Qwen2.5-14B (4 seeds) 做了 multi-seed replication。Seed-level noise ≈ ±2.34pp，而 Table 1 大部分条件 |Δ| < 3pp 且为 single-seed。许多观测效应可能完全由 seed variance 解释。
- **修改建议**: 至少对效应最大的条件补充 multi-seed，或在 Limitations 明确讨论 single-seed 局限。

**W9 [Major] Capability-gap principle 基于 n=6 条件——不足以支撑 "principle" 级别 claim [共识]**
- **位置**: §6 "Escaping the Bottleneck", Table 3, Figure 8
- **问题**: 仅约 6 个 verifier-generator 组合，Table 3 仅 Mistral-7B (SC=39.33%) 1 个条件显著。§6 标题 "Escaping the Bottleneck" 语气过强。
- **修改建议**: 降级为 "preliminary observation" 或 "hypothesis"。

**W10 [Major] "27 strategies fail" scope 不匹配 [部分共识]**
- **位置**: §5.2, Table 14, Abstract
- **问题**: 27 个策略局限于 self-extraction paradigm 内的变体（prompt-level + method-level + cross-model），不等于所有 training-free 方法都失败。
- **Reviewer 分歧**: R2 认为 scope 过宽，R1 partial REBUT（策略确实跨多个独立维度），但 R1 同意应限定 claim scope。
- **修改建议**: 限定为 "27 training-free variants within the constraint-extraction-aggregation paradigm"。

### Minor 问题（不影响接收）

**M1** [Minor] α = 0.5 缺乏理论依据和真正的 sensitivity analysis。Table 11 的 ≥99% agreement 是 ceiling effect（主效应近零时 penalty 项影响自然可忽略），非真正鲁棒性。[共识]

**M2** [Minor] "First-order logic" 描述轻微 overselling——99% 约束是 propositional level at Z3，仅 1.06% 使用真正量词。[共识]

**M3** [Minor] Figure 1 信息密度偏高；K_eff 缺乏直觉解释；Abstract 信息过载（6 个要素）。[R2 提出]

**M4** [Minor] §2 Related Work 段间逻辑衔接可改善——建议构建从 majority voting → self-correction → formal verification → this paper 的叙事线。[R2 提出]

**M5** [Minor] GSM8K (n=30) 和 AIME (n=22) 样本量过小，不应与大样本条件等权重引用。论文已标注 "exploratory"（Table 1 caption），但正文 §5.3 引用时未区分。[共识]

---

## Questions（需要作者澄清）

**Q1.** Proposition 1 Part (i) 依赖 source attribution scoring。如果使用 source-agnostic scoring（基于逻辑一致性而非来源归属评估约束-答案关系），是否仍会退化？是否测试过 source-agnostic alternatives？

**Q2.** BR 的 null expectation 是什么？如果约束提取完全"无偏"（support 比例精确反映 trace 投票分布），BR 期望值是否恰好为 1？请提供 permutation test 或 null model 分析。

**Q3.** Diagnostics 的决策边界在 positive cases（cross-architecture escape, oracle）上是否能正确预测"SICA 会帮助"？

**Q4.** TOST ±2pp equivalence margin 如何选择？如果 margin 放宽至 ±3pp 或 ±5pp，有多少额外条件达到等价显著？

**Q5.** Table 1 中 |Δ| < 3pp 的所有 single-seed 条件，作者是否承认这些差异可能完全由 seed variance 解释（given seed noise ≈ ±2.34pp）？

**Q6.** Cross-architecture NLI 验证仅在 NLI-friendly 数据集（FOLIO, ProofWriter）上测试。对非 NLI 格式推理任务是否适用？

---

## Missing References

1. **Kamoi et al. (TACL 2024)**: "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs" — self-correction 方向最全面 survey。[R2 提出，R1 AGREE]
2. **S²R (Zeng et al., ACL 2025)**: RL-based self-verification，通过训练打破 Proposition 1 信息上限。[R2 提出，R1 同意应讨论理论边界]
3. **DuPO (arXiv 2508.14460, 2025)**: Dual preference optimization self-verification。[R2 提出，R1 同意应讨论理论边界]
4. **AlphaCode / CodeT**: Constraint verification in code domain 的成功案例，可对比讨论为何逻辑推理领域失败。[R1 提出，Minor]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 完成（耗时 ~4 分钟）

**统计**: 0 critical, 1 warning, 24 info

**Warning**:
- Page 7, Figure 4: 柱状图底部 x 轴策略名称字号偏小，27 个 bar 密度高，灰度打印时 4 种颜色区分度可能下降。建议增加 marker pattern 或 hatching。

**Info 要点**:
- Figure 1 (p.2) pipeline 图 caption 自包含，Title-Abstract-Figure 1 narrative 一致，第一印象良好
- 所有 Figure/Table 出现在首次引用附近，无 float 漂移
- 表格一致使用 booktabs 风格，最优值加粗，显著性标记有脚注说明
- 公式渲染正确，无 LaTeX 错误残留或未解析引用
- Limitations section 在 page 8 底部延伸至 page 9，符合 EMNLP 2026 规定
- 参考文献约 2.5 页，格式统一

**总体**: 排版质量良好，无严重视觉问题。

---

## Reviewer Consensus

### 完全共识（14 项 AGREE）
1. Proposition 1 scope mismatch（Part (i) SICA-specific，标题 claim "structural"）
2. 统计功效 < 21% 与 negative claim 强度不匹配
3. 标题 "Fail to Improve" overclaiming
4. BR 循环论证风险（base-rate 效应未排除）
5. Diagnostics in-sample overfitting（100% 准确率无意义）
6. Multi-seed replication 不充分（2/6 模型）
7. BR 小 n_err 条件缺 CI
8. α = 0.5 sensitivity analysis 不充分
9. Capability-gap principle n=6 不足以支撑 "principle"
10. "Extending Huang et al." 是 overselling
11. GSM8K/AIME 样本量过小
12. K_eff exchangeability 假设局限
13. Cross-architecture generalizability 受限
14. "First-order logic" 轻微 overselling

### 部分分歧（3 项 partial REBUT，已记录各方理由）
1. **新颖性**: R2 认为核心洞察可预见（Huang + DPI 延伸），R1 认为不应事后贬低 negative result 且诊断框架/27 策略有独立价值 → 共识：定位为"系统性量化"而非"发现"
2. **Training-based refs**: R2 认为 major missing，R1 认为 scope 外但同意讨论理论边界
3. **"27 strategies" scope**: R1 指出策略跨多维度，但同意应限定 claim scope

---

## Overall Assessment

### 评分汇总

| 维度 | R1 | R2 (交叉后修正) | 加权综合 |
|------|-----|----------------|---------|
| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |
| Excitement | 3.0–3.5/5 | 2.5/5 | 3.0/5 |
| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |
| Overall | 3.5 | 3.0 | **3.0** |
| Confidence | 4/5 | 4/5 | 4/5 |

### Overall: 3.0 — Findings

**一句话总结**: 实验执行出色的 negative result paper，但核心理论贡献（Proposition 1）证明与声称范围不匹配、统计功效不足以支撑标题级 claim、诊断框架泛化性未验证、BR 指标概念有效性存疑，且新颖性有限（SCB 是已知结论的实证深化）。

**详细理由**:

*支持接收的因素*: (1) 实验规模大（9 模型 × 3 数据集 × 60 条件 × 27 策略），远超同类工作；(2) 统计方法论多层次且诚实（McNemar + BH + TOST + bootstrap + power analysis + shuffle control）；(3) Oracle 控制实验精巧，精确分离提取质量与方法论有效性；(4) 诊断框架有潜在实用价值；(5) Cross-architecture escape 提供建设性方向；(6) 附录极为详尽（18 页），可复现性强。作为 Findings 论文，对社区有实际指导价值——帮助避免在 self-extracted constraint verification 方向上的无效探索。

*限制接收为 Conference 的因素*: (1) Proposition 1 的 scope mismatch 使核心理论贡献被削弱——Part (i) 仅对 source-attribution 成立，Part (ii) 是平凡 DPI 推论；(2) 21% 的统计功效使 "fail to improve" 的标题级 claim 无法被统计证据充分支撑；(3) Diagnostics 的 100% 准确率是 in-sample 评估，holdout 验证不充分，这是论文三大贡献之一；(4) BR 作为 SCB 的量化基础存在循环论证风险（base-rate 效应未排除），需要 null model 才能确定"额外 bias"的存在；(5) 新颖性有限——核心洞察（自提取约束继承模型 bias）是 Huang et al. (2024) + Wan et al. (2025) 已知结论在形式化验证管道中的实证深化。

*如果以下问题得到解决，评分可提升至 3.5（Borderline Conference）*:
1. 标题软化 + Abstract 加 power caveat + TOST margin sensitivity
2. Proposition 1 拆分并明确 scope
3. BR 提供 permutation null model 或降级为描述性指标
4. Diagnostics 增加 held-out model family 验证并弱化 claim
5. §2 补充 training-based self-verification 讨论
6. "Extending Huang et al." 改为 "consistent with / provide independent evidence for"

---

## Detailed Comments（逐节）

**Title**: "Fail to Improve" 过于绝对，与 power < 21% 不匹配。建议 "Do Not Substantially Improve" 或 "The Limits of Self-Extracted Constraints for"。

**Abstract**: 信息密度高但覆盖完整。需加 power caveat（如 "though underpowered for effects below ~2pp"）。"extends the self-correction impossibility of Huang et al." 改为 "provides independent evidence consistent with"。BR 报告 "at least 1.66×" 应注明 base-rate 组成未排除。

**§1 Introduction**: Contribution 2（diagnostics 100% 准确率）需加 scope 限定。Contribution 3 "capability-gap principle" 降级为 "preliminary observation"。

**§2 Related Work**: 缺 training-based self-verification 讨论（S²R, DuPO）。缺 Kamoi et al. (TACL 2024) self-correction survey。段间逻辑衔接可改善。

**§3 Method**: α = 0.5 缺理论依据。K_eff 缺直觉解释。BR 定义（Eq. 5）需声明 base-rate 效应。

**§4 Results**: 统计诚实（报告 power 局限），但 claim 强度与证据强度仍有 gap。Single-seed 条件应标注不确定性。

**§5.1 Symbolic Confirmation Bias**: Proposition 1 需拆分。BR > 1 的解读需 null model。Table 11 的 ≥99% agreement 应加 ceiling effect caveat。

**§5.2 Why Remediation Fails**: 27 策略 claim scope 应限定为 "within constraint-extraction-aggregation paradigm"。

**§5.3 Diagnostic Framework**: 100% 准确率 claim 需大幅弱化。增加 OOD 验证。讨论 positive case 预测能力。

**§6 Escaping the Bottleneck**: 标题过强。"Capability-gap principle" → "preliminary observation"。仅 1 个条件显著。

**§7 Discussion and Conclusion**: "extending... to formal verification" 改措辞。Future work 应明确 training-based methods 如何 escape Proposition 1。

**Limitations**: 长度合规（EMNLP 2026 规定"一小段覆盖 3 个点"），覆盖了关键局限（open-source only, English only, logical reasoning only）。可考虑增加 power limitation 的一句话提及。
