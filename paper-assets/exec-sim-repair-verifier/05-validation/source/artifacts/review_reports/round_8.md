---
round: 8
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T16:00:48.533982+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---


# Round 10 审稿报告

**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
**Venue**: EMNLP 2026 via ARR (Long Paper)
**审稿模式**: Fresh (初审)
**Reviewer 编排**: 2 人（R1 方法严谨性 / R2 新颖性与完整性）

---

## Summary

本文对三种 execution-free 代码修复验证公式（CLS 逐测试分类、CWM 执行输出生成、TRAJ 轨迹级评分）进行了首次系统性匹配比较，使用相同 base model（Qwen3-4B/8B、DeepSeek-Coder-6.7B）、相同 LoRA 配置、相同训练数据，在 function-level 和 repo-level 两个复杂度层次上评估。核心发现是"三层结构"：(1) fine-tuning 必要（35-36pp 提升），(2) function-level 公式间统计等价（TOST p=0.007），(3) repo-level 下 CWM 显著退化（低于 CLS 18-26pp），driven by format collapse。论文还提供了 failure mode taxonomy 和 error complementarity 分析。

---

## Strengths

**S1. 匹配实验框架设计在 NLP 论文中属罕见严谨。** 相同 base model、LoRA rank、optimizer、training schedule、5 seeds（function-level），DeepSeek-Coder 作为 cross-model consistency check。这是实验比较研究的标杆（Section 3.1, Table 1）。[R1-S1, R2-S1 共识]

**S2. 统计方法论深度远超 NLP 领域平均。** TOST 等价检验（而非仅 NHST）、ICC-based clustered bootstrap（114 clusters, 10K resamples）、Holm-Bonferroni 多重比较校正、mixed-effects LPM——这套工具链在 NLP 论文中极为少见（Section 3.1, 3.4, Appendix A/J/M）。[R1-S2, R2-S1 共识]

**S3. Failure mode taxonomy 有独立实用价值。** Format collapse / decision collapse / aggregation penalty 三类 failure modes 有定量分析和定性例证（Section 3.5, Table 4, Appendix H），为从业者选择 formulation 提供可操作指导。[R1-S3, R2-S3 共识]

**S4. Error complementarity 发现有 ensemble/routing 研究价值。** Oracle combination 90.63%（function）/ 95.83%（repo），证明公式犯互补错误。Cross-seed oracle 94.27±2.59% 确认跨 seed 稳定性（Section 3.6）。[R2-S4]

**S5. 附录极其详尽且自我批评诚实。** 16 个 Appendix（14 页）覆盖全部 ablation、convergence、power analysis、prompt templates、qualitative errors。Limitations 和 Threats to Validity 主动识别并讨论多个潜在问题。[R1-S4/S5, R2-S5 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**[Must-Fix 1] Novelty 受限：核心贡献为比较已有 formulations，excitement 不足 main conference**
- 来源：R2-N1 提出，R1 AGREE
- 详情：三种 formulation 均为已有方法（CLS: Ni et al. 2023; CWM: FAIR 2025; TRAJ: Shum et al. 2025）。核心发现"复杂任务→公式选择更重要"数据支撑充分但从直觉可预期。论文描述了 what happens 但缺少深层 why 的理论理解——为什么恰好在 repo level 而非某个中间复杂度出现分歧？"三层结构"是描述性的而非解释性的。
- 影响：两位 Reviewer 共识 Excitement 2.5-3.0/5，一致认为 Findings 合适但 Main 不够。
- 建议：(a) 增加轻量 routing/ensemble 实验将贡献从"比较"提升为"比较+方案"；(b) 或提供 complexity threshold 的理论分析。

**[Must-Fix 2] TOST 统计功效不足，CLS-TRAJ 等价性无法确认**
- 来源：R1-N2 提出，R2 AGREE（交叉分享后升级关注度）
- 详情：n_eff ≈ 86，TOST 对 medium effect size 功效仅 ~0.3（70% 概率将真实中等差异误判为等价）。CLS-TRAJ adjusted p=0.075 未通过 Holm-Bonferroni。Abstract "TRAJ parity differs between the two tested families" 措辞不够精确——实际是等价检验功效不足、无法下结论，而非 TRAJ 显著不等价。
- 建议：(a) 正文讨论 TOST 功效限制（目前仅 Appendix J/K）；(b) Abstract 措辞改为"TRAJ equivalence could not be confirmed after multiple comparison correction"；(c) 考虑补充 Bayesian equivalence test（ROPE-based）。

### Should-Fix（影响评分但不一票否决）

**[Should-Fix 1] ≤8B LoRA 规模限制——Conclusion 缺少限定语**
- 来源：R2-N2 提出 CRITICAL，R1 部分 REBUT（4B→8B gap 扩大数据反驳纯容量假说）
- Director 裁定：降为 Should-Fix。R1 反驳有效——4B→8B 时 CLS-CWM gap 从 1.32pp 扩大到 2.62pp（Figure 2），说明增加参数量不缩小差距。且 Appendix I qualitative analysis 表明 format collapse 源于 output format complexity（formulation 固有属性）。但 ≤8B→32B 跨越量级不同，不能完全排除。Abstract 已有"≤8B LoRA protocol"限定，但 Conclusion 和部分正文 claims 仍缺。
- 建议：Conclusion 加入 ≤8B LoRA 限定；讨论更大规模下结论可能如何变化。

**[Should-Fix 2] Checkpoint selection 混杂——正文讨论不够显著**
- 来源：R1-N1 标 CRITICAL，R2 REBUT
- Director 裁定：降为 Should-Fix。R2 反驳有效——Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp range（val-selected 反而最低）。Checkpoint 差异无法解释 18-26pp gap。但缓解证据分散在 Section 3.5 半段和 Appendix O，正文应更显著讨论。
- 建议：正文中合并讨论 checkpoint 缓解证据（matched epoch-3 gap + CLS ablation range），而非仅依赖 Appendix。

**[Should-Fix 3] 训练数据量差异（CLS ~70K vs TRAJ ~386）+ 信号粒度不同**
- 来源：R1-W1 提出，R2 AGREE
- 详情：~180× 数据量差异。Downsampling ablation 控制了 volume（CLS 80.74% vs TRAJ 72.92%，仍高 7.82pp）但未控制 signal granularity（per-test vs variant-level）。两人共识：应将此框架为 formulation 固有属性。
- 建议：正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性而非可控实验变量。

**[Should-Fix 4] Repo-level seed 覆盖不足（2-3 seeds）**
- 来源：R1-W2 提出，R2 AGREE
- 详情：Repo-level 仅 2-3 seeds（vs function-level 5 seeds），variance 更大。正文 claims 读起来像 definitive 结论但仅 2-3 独立观测。
- 建议：正文中显式标注 repo-level 分析的 seed 数和相应不确定性。

**[Should-Fix 5] SESOI ±2pp 描述从 "a priori" 改为 "practically motivated"**
- 来源：R1-W4 提出，R2 部分 AGREE
- 详情：±2pp 依赖于 accuracy range（85-89%）和 test set size（114 problems），难以验证为纯 a priori。Appendix J sensitivity analysis 部分缓解。
- 建议：§3.4 将 SESOI 描述从 "set a priori" 改为 "practically motivated"；引用 Appendix J sensitivity 作为 robustness check。

**[Should-Fix 6] Python-only 评估未在 Limitations 提及**
- 来源：R2-W1 提出，R1 AGREE
- 详情：HumanEval+MBPP 和 SWE-bench 均为 Python。不同语言（Java/C++）的 test output 格式差异可能影响 CWM formal collapse rate。
- 建议：Limitations 增加一句关于语言覆盖单一性的讨论。

**[Should-Fix 7] Related Work 缺 CodeRM + ORM/PRM 映射**
- 来源：R2-W2 提出，R1 AGREE
- 详情：遗漏 CodeRM (Diao et al., ACL 2025 "Dynamic Scaling of Unit Tests for Code Reward Modeling")——研究 test-level 粒度对 reward signal 质量的影响，直接相关 CLS 设计。另需加强 CLS↔ORM / CWM↔generative verifier 的框架映射讨论。
- 建议：验证 CodeRM 真实性后加入；加半段 ORM/PRM 映射讨论。

**[Should-Fix 8] Overclaim 措辞："governed by" 等**
- 来源：R2-M1 提出，R1 AGREE
- 详情："formulation choice is governed by code complexity"（Introduction, p.1）暗示 deterministic/因果关系，但证据仅 2 complexity levels × 2-3 seeds × ≤8B models。
- 建议：改为 "moderated by" 或 "depends on"。

### Minor（不影响接收）

**[Minor 1]** Figure 2 y-axis 从 55% 起始（截断），视觉上夸大 CLS-CWM gap。Caption 已标注但对快速浏览读者可能误导。考虑从 0 起始或改用差值图。[R1-M2, R2 AGREE, 视觉审查标记]

**[Minor 2]** Mixed-effects model 使用 LPM 而非 logistic regression 作为主分析。Appendix M 建议并列展示 logistic regression marginal effects。[R1-M1, R2 AGREE]

**[Minor 3]** 3-shot ICL collapse to always-predict-unresolved（45.83%）是重要 negative result，但正文仅一句带过。值得增加半段讨论 fine-tuning 作为 verification 必要条件的 implication。[R2-M2, R1 AGREE]

**[Minor 4]** 16 个 Appendix（A-P）导航不便。考虑加 Appendix 目录索引。[R2-M3, R1 轻度 AGREE]

---

## Reviewer Consensus

| 议题 | 状态 | 详情 |
|------|------|------|
| Novelty 受限 | [AGREE] | 两人共识 Findings 合适，Main 不够 |
| TOST 功效不足 | [AGREE] | R1 提出，R2 交叉后升级关注度 |
| Seed 覆盖 | [AGREE] | 两人共识 repo-level 2-3 seeds 不足以支撑 definitive claims |
| Data volume 差异 | [AGREE] | 两人共识应框架为 formulation 固有属性 |
| Python-only | [AGREE] | 两人共识应在 Limitations 提及 |
| SESOI a priori | [AGREE] | 两人共识改为 "practically motivated" |
| Overclaim 措辞 | [AGREE] | "governed by" 改 "moderated by" |
| CodeRM 遗漏 | [AGREE] | 验证后加入 |

## Reviewer Divergence

| 议题 | R1 | R2 | Director 裁定 |
|------|-----|-----|-------------|
| Checkpoint confound (R1-N1) | CRITICAL | REBUT（matched analysis 仍 20-23pp gap） | **Should-Fix**：R2 反驳有效，checkpoint 差异无法解释 18-26pp gap，但正文讨论应更显著 |
| Scale limitation (R2-N2) | 部分 REBUT（4B→8B gap 扩大） | CRITICAL | **Should-Fix**：R1 反驳部分有效，但 ≤8B→32B 不能完全排除。Conclusion 需加限定 |
| Exact match penalty (R1-W3) | WARNING | REBUT（relaxed matching 扩大 gap） | **Resolved**：R2 反驳成功，relaxed matching 使 gap 从 26pp 扩大到 27pp，parseable accuracy 仅 38-43%。瓶颈是语义的不是格式的 |
| Routing 未验证 (R2-W3) | REBUT（scope 合理） | WARNING | **Minor**：R1 反驳合理——"motivate" 非 "propose"，属 future direction |
| TRAJ 探索不充分 (R2-W4) | REBUT（scope 限定） | WARNING | **不作为 issue**：论文 scope 是比较现有 formulations，非设计新方法 |
| Overall 评分 | 3.5 (Borderline Conference) | 3.0 (Findings) | 见下方 |

---

## Questions（需要作者澄清）

**Q1.** 能否在正文中更显著地讨论 checkpoint 缓解证据？目前 matched epoch-3 分析和 CLS ablation 分散在 Section 3.5 半段和 Appendix O。[R1-Q1, R2 交叉中提供了证据]

**Q2.** Cross-seed oracle（90.63% function / 94.27±2.59% repo）是 any-correct（任一公式正确即正确）还是 majority voting？请在正文明确标注。[R1-Q4, R2 AGREE]

**Q3.** 是否尝试过不依赖 oracle 的简单 routing 启发式（如基于 input token 数或 CLS 预测置信度）？即使 negative result 也有价值。[R2-Q2]

**Q4.** CLS vs CWM 的实际 wall-clock time 差异在 SWE-bench 端到端评估中有多大？Section 3.6 报告了 throughput 但未报告 wall-clock。[R2-Q5]

**Q5.** 结论是否可推广到 code generation（无 buggy source 对比）场景？建议在 Limitations 讨论。[R2-Q4]

---

## Missing References

| 引用 | 来源 | 状态 |
|------|------|------|
| CodeRM (Diao et al., ACL 2025 "Dynamic Scaling of Unit Tests for Code Reward Modeling") | R2-W2 | 需验证真实性后加入 |
| Cohen (1988) *Statistical Power Analysis* | R1 Missing Refs | 建议加入（power analysis 讨论） |
| Kruschke (2013/2018) Bayesian ROPE methods | R1 Missing Refs | 可选（若补充 Bayesian equivalence test） |

---

## External Review

外部审稿：未启用。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical / 0 warning / 10 info）。主要发现：

- **Page 1-2**：前两页纯文本，无 display item。Figure 1 出现在第 3 页顶部——刚好在 3 页窗口内，但提前至第 2 页会改善审稿人第一印象。
- **Figure 1（p.3）**：三种 formulation 对比图，caption 自包含，颜色区分清晰，信息传达有效。
- **Page 4**：Table 1 + Table 2 同页，数据密度较高但布局紧凑合理。
- **Figure 2（p.7）**：y-axis 从 55% 起始（截断），caption 已标注。与 R1-M2 / R2 AGREE 的审稿意见一致——建议从 0 起始或改用差值图。
- **Page 12**：PDF 内包含 ARR Responsible NLP Research Checklist。根据 EMNLP 2026 规则，此 checklist 应在 OpenReview form 中填写，PDF 内包含不算错误但可能冗余。
- **末页（p.23）**：约 1/3 内容 + 2/3 空白，Appendix 最后一页，影响不大。

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | Director 综合 |
|------|-----|-----|-------------|
| Soundness | 3.0 | 3.5 | **3.5** — R2 REBUT 成功缓解了 R1 的 checkpoint concern；TOST 功效问题真实但不足以否定 CLS-CWM equivalence 结论（p=0.007 仍显著）。核心结论 robust。 |
| Excitement | 3.0 | 2.5 | **2.5** — 两人共识 novelty 受限于比较已有方法。Failure mode taxonomy 有独立贡献但属增量。核心发现可从直觉预期。 |
| Reproducibility | 4.0 | 4.0 | **4.0** — 超参数、数据构造、compute budget 报告极为详尽。 |
| **Overall** | **3.5** | **3.0** | **3.0 (Findings)** |
| Confidence | 4.0 | 4.0 | **4.0** |

### Overall: 3.0 — Findings

**一句话判断**：方法论执行严谨、failure mode 分析有洞察力的系统比较研究，适合 Findings 而非 Main Conference。

**核心理由**：

1. **方法论是亮点但不足以弥补 novelty 缺口。** TOST/ICC/clustered bootstrap/Holm-Bonferroni 在 NLP 中确实罕见，但方法论规范性是"做对了应该做的事"，不构成 excitement 来源。核心发现（复杂任务→formulation 选择更重要，classification > generation at repo level）从直觉可预期。

2. **两个 Must-Fix 问题分别影响接受度和可信度。** (a) Novelty 不足 Main——两位 Reviewer 共识；(b) TOST 功效不足使 function-level equivalence claim 从"强支撑"降为"有支撑但需审慎解读"。

3. **Should-Fix 问题可修复但不改变 track。** ≤8B scale limitation（Conclusion 加限定语）、checkpoint 讨论（正文更显著）、SESOI 描述（改为 practically motivated）、Python-only（Limitations 加一句）等均为 framing/writing 层面修改，可在 revision 中解决，但不会提升 novelty 到 Main Conference 水平。

4. **上调至 3.5（Borderline Conference）的条件：** (a) 补充轻量 routing/ensemble 实验，将贡献从"比较"提升为"比较+方案"；(b) 补充 Bayesian equivalence test 增强 function-level equivalence 证据；(c) 补充至少一个 ≥14B 模型的单点验证。满足其中 2/3 可考虑上调。

### 修改优先级

| 优先级 | 问题 | 工作量 |
|--------|------|--------|
| P0 | Abstract/Conclusion "TRAJ parity differs" 改为审慎措辞 | 极低 |
| P0 | Conclusion 加 ≤8B LoRA 限定语 | 极低 |
| P0 | "governed by" → "moderated by" | 极低 |
| P1 | 正文讨论 TOST 功效限制 | 低 |
| P1 | 正文合并讨论 checkpoint 缓解证据 | 低 |
| P1 | SESOI "a priori" → "practically motivated" | 极低 |
| P1 | Limitations 加 Python-only + code generation scope | 极低 |
| P1 | TRAJ data volume/granularity 框架为 formulation 固有 | 低 |
| P2 | 验证并加入 CodeRM + ORM/PRM 映射讨论 | 中 |
| P2 | 正文增加 3-shot ICL collapse 讨论 | 低 |
| P2 | Figure 2 y-axis 修改 | 低 |
| P2 | Appendix M 补充 logistic regression | 低 |
| P3（可选，提升 track） | 轻量 routing/ensemble 实验 | 高 |
| P3（可选，提升 track） | Bayesian equivalence test | 中 |
