---
round: 2
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-19T03:04:14.298259+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 3 审稿报告（Fresh Review）

**论文**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study
**Venue**: EMNLP 2026 (ACL Rolling Review)
**审稿模式**: Fresh（重新审稿，无上轮记忆）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+写作质量+格式合规）
**外部审稿**: 已跳过（用户未提交）

---

## Summary

本文对三种 execution-free code verification formulation（per-test classification CLS、execution output generation CWM、trajectory-level patch scoring TRAJ）进行了系统对比，使用两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别（function-level, repo-level）、多个随机种子。核心发现：function-level 三种 formulation 准确率等价（TOST $p=0.007$）；repo-level CLS 显著优于 CWM（19-26pp）；CWM 在 repo-level 因 format collapse 失效（51-74% 不可解析输出）；CLS 和 CWM 存在互补错误模式（oracle ensemble 90.63%）。

---

## Strengths

**S1. 研究问题重要且定义清晰。** 三种 execution-free verification formulation 之间缺乏系统比较，论文将工程选择问题提升为科学问题，对 LLM-based repair pipeline 从业者有直接实用价值。[R1-S1, R2 共识]

**S2. 统计方法论水准高。** 使用 TOST 等价性检验（非仅 NHST）、clustered bootstrap（尊重 problem-level 相关结构）、ICC 量化 within-problem correlation、margin sensitivity analysis。这在 NLP 实证研究中属于高标准。[R1-S2, R2 优势 #1]

**S3. Function-level 结果稳健。** 5 seeds × 2 model families × 3 formulations 的 function-level 比较有充分统计效力，TOST 等价性结论和 clustered bootstrap CI 互相印证。[R1-S3]

**S4. Failure mode taxonomy 有实用价值。** Table 4 的三种 failure mode 分类（format collapse, decision collapse, aggregation penalty）和 Appendix G 的 qualitative error analysis 为从业者选择 formulation 提供了实用参考。[R1-S4, R2 优势 #3]

**S5. 对自身局限的透明度。** 论文明确讨论了 NaN validation loss、单种子限制、val-test distribution mismatch、eval seq_length sensitivity 等问题。这种坦诚在投稿论文中不常见。[R2 优势 #2]

**S6. 消融实验覆盖面广。** LoRA rank ablation、majority voting、sequence-length ablation、relaxed matching、constrained decoding 讨论，涵盖了审稿人可能提出的多数 "what if" 问题。[R2 优势 #4]

**S7. Efficiency 分析有部署价值。** CLS 217× throughput 和 CLS-TRAJ crossover 分析（|T| ≈ 50）提供了实用的工程指导。[R2 优势 #5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [critical] TRAJ 训练数据量差异 175× 根本性破坏 "controlled comparison" 框架** [R2 提出, R1 AGREE]

CLS/CWM 使用 ~70K 训练样本，TRAJ 仅 ~400 实例（175× 差异）。Abstract 声称 "training on identical data with controlled model sizes"，在 effective training examples 数量上构成 overclaim。所有涉及 TRAJ 的结论（包括 TOST equivalence、per-test vs trajectory-level 的 contribution #4）无法可靠归因于 formulation 差异而非数据量差异。R1 补充指出此数据不对称部分是 formulation-inherent（TRAJ 按设计只有 patch-level 标注），但论文应明确讨论这一点。

*建议*：(1) Abstract/Introduction 明确披露数据量差异；(2) 将 TRAJ 降级为 secondary baseline 而非 controlled comparison 的平等 formulation；(3) 或在 function-level 做 data-size matched 实验（downsample CLS 到与 TRAJ 相同数量）。

**N2 [critical] Repo-level 统计效力严重不足** [R1 提出, R2 AGREE]

多数 repo-level 配置仅 1-2 个 seed。DeepSeek CLS 跨 seed/config 波动 7.68pp，Qwen3-4B CLS 仅 seed 42。在如此高的 seed variance 下，1-2 seed 无法区分 formulation effect 和 seed noise。但主文 "CLS achieves 19-26pp higher accuracy"、"divergence is formulation-inherent" 的表述暗示了远超实际证据的 robustness。

*建议*：增加到 ≥3 seeds per key comparison，或显著弱化 repo-level 结论表述为 "preliminary observations"。

**N3 [critical] NaN validation loss 导致 checkpoint 选择策略跨配置不一致** [R2 提出, R1 AGREE]

DeepSeek s123 + 所有 CWM runs 出现 NaN validation loss，被迫使用 final epoch checkpoint，而其他配置使用 val-best。论文 Section 4.4 自己承认 "Val-based selection optimizes per-test accuracy, which biases toward predicting pass"，但 "Cross-model validation" 段落仍用包含此 confound 的结果声称 "confirms the divergence is formulation-inherent"。这构成 internal inconsistency。

*建议*：(1) 对所有配置统一报告 final-epoch checkpoint 的结果作为 ablation；(2) 修复 NaN loss 根因（truncate preprocessing）。

**N4 [critical] CWM 4-8B LoRA 结论不能外推为 generation formulation 的普遍判断** [R1, R2 独立发现]

论文承认 "Our CWM baseline is a LoRA fine-tuned variant, not a reproduction of the 32B Code World Model"，但叙事层面仍做 formulation-general 的 claim。CWM 的失败可能反映 (a) formulation-inherent 属性（论文所称），(b) 4-8B 容量不足（原始 CWM 32B），或 (c) 缺乏 execution trace mid-training。论文仅在 4-8B 范围验证了 (b)，远不足以排除。

*建议*：将所有 CWM 结论限定为 "at 4-8B LoRA fine-tuning scale"；讨论 execution trace mid-training 可能改变结论的可能性。

### Should-Fix（影响评分但不一票否决）

**W1 [high-priority] Limitations 不是独立 section，有 desk reject 风险** [R2 提出, R1 AGREE on fact]

当前是 Conclusion 中的 `\paragraph{Limitations and future work.}`，ARR 要求独立 `\section*{Limitations}` 置于 Conclusion 之后 References 之前。R1 认为 30 秒 LaTeX 修复不构成 critical，但投稿前必须修复。

**W2 Abstract 数据密度过高** [R2 提出, R1 AGREE]

~211 词内塞入大量具体数字，审稿人 30 秒内难以提取核心 message。建议保留 2-3 个关键数字，其余定性描述。

**W3 "No single formulation dominates" framing 与证据不符** [R1 提出, R2 AGREE]

CLS 在所有条件下 ≥ 其他 formulation。"No single formulation dominates" 仅在非 accuracy 维度（error complementarity）成立，当前表述易误导 practitioners。建议改为更精确的 framing。

**W4 CWM 跨模型 eval seq_length 不一致** [R2 提出, R1 AGREE]

Qwen3 CWM eval 8192, DeepSeek CWM eval 4096。论文承认 "not directly comparable" 但仍声称 cross-model validation。与 N3 的 checkpoint confound 共同削弱 "formulation-inherent" causal claim。

**W5 Re-repair pilot (n=44, power<0.3) 不足以作为 contribution** [R1, R2 独立发现]

n=44, p=0.42, power ~0.3。应从 contribution list 移除或降级为 "inconclusive preliminary result"。

**W6 Oracle ensemble (90.63%) 缺乏 practical routing 验证** [R1, R2 独立发现]

Oracle 是 upper bound。Conclusion 提出 "complexity-aware routing" 但未实现任何 routing 机制。建议弱化 claim 或实现 simple routing baseline。

**W7 TOST ±2pp margin sensitivity 主文披露不足** [R1 提出, R2 AGREE]

±1pp → 不等价 (p=0.871), ±2pp → 等价 (p=0.007)。核心 equivalence 结论高度 margin-sensitive。主文应增加 sensitivity 结果和 margin 选择 rationale。

**W8 缺失重要相关工作** [R1, R2 交叉确认]

R1: ScratchPad (Nye et al., 2021), Math-Shepherd/OmegaPRM, CodeExecutor (Liu et al., 2024 ACL)。R2: REDO (Chen et al., 2024), constrained decoding 文献。

**W9 推理时 context length asymmetry** [R1 提出, R2 REBUT 并降级]

CWM ~1536 tokens vs CLS 5120-8192 tokens。R2 提供论文 Appendix B 证据：matched-context ablation (CLS@2048 vs CWM@2048) 显示 input context 差异仅解释 <3% 的 gap。R1 未反驳。降级为 Should-Fix，建议补充说明 effective input tokens 差异。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成完全共识（独立发现 + 交叉确认）：

1. **Repo-level 统计效力不足**（N2）：证据最薄弱的环节恰是论文最核心的贡献
2. **"Controlled comparison" 被多个 confounds 削弱**（N1, N3, N4）：TRAJ 数据量 175×、checkpoint 不一致、CWM capacity 限制
3. **Re-repair pilot 证据不足**（W5）：n=44 不支撑 contribution claim
4. **Oracle routing 无实际验证**（W6）：upper bound ≠ 可行性
5. **CWM 结论需限定规模**（N4）：4-8B LoRA ≠ formulation 普遍判断

## Reviewer Divergence [REBUT]

以下分歧已在交叉回应中解决：

1. **R1-N1 context length asymmetry**：R1 列为 critical，R2 REBUT 引用 Appendix B 消融证据（<3%），R1 未反驳 → 降级为 Should-Fix (W9)
2. **R1-N3c LR 4× 差异**：R2 正确指出同一模型内 CLS/CWM 使用相同 LR，跨模型差异是标准做法 → 不构成 formulation confound，已消解
3. **R2-W4 Related Work 论文堆砌**：R1 反驳 page constraints 下 2/3 column 是 norm，thematic organization 正确 → 降级为 minor（第一段 citation density 偏高可改善）
4. **R2-N3 Limitations 格式**：R1 同意事实但降级（30 秒修复）→ 共识为高优先 Should-Fix (W1)
5. **R1-W5 ICC 外推**：R2 引用 Appendix A conservative lower bound 论证 → 已消解，无需修改

---

## Questions for Authors

1. 是否可在 rebuttal 期间为 key repo-level comparison（至少 CLS vs CWM at 8B）补充到 ≥3 seeds？
2. TRAJ 如果使用 ~70K 聚合数据训练（per-test labels → variant-level），function-level TOST equivalence 是否仍然成立？
3. 对所有配置统一使用 final-epoch checkpoint 后，core conclusions 是否仍成立？
4. 论文是否考虑过在更大规模（如 32B inference-only）验证 CWM formulation 的 repo-level 表现？
5. Repo-level oracle ensemble 结果是什么？如果 repo-level error complementarity 不存在，routing motivation 不成立。

---

## Missing References

1. **ScratchPad** (Nye et al., 2021) — execution trace generation foundational work
2. **REDO** (Chen et al., 2024, arXiv:2410.09117) — execution-free runtime error detection
3. **CodeExecutor** (Liu et al., 2024, ACL) — code execution simulation
4. **Math-Shepherd** (Wang et al., 2024) / **OmegaPRM** (Luo et al., 2024) — process reward model training
5. **Constrained decoding** 代表性工作 — 与 Section 4.4 CWM format compliance 讨论相关

---

## External Review (Stanford Agentic Reviewer)

**状态：已跳过**（用户未提交至 paperreview.ai）。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3/5 | 3/5 |
| Excitement | 3/5 | 2.5/5 | 2.75/5 |
| Reproducibility | 4/5 | 3.5/5 | 3.75/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**理由**：

论文提出了一个重要的研究问题并展示了值得认可的统计方法论意识。Function-level 的等价性结论有充分证据支撑（5 seeds, TOST, clustered bootstrap），failure mode taxonomy 和 efficiency 分析有实用价值。

但 "controlled comparison" 这一核心定位被多个未控制的混淆因素实质性削弱：(1) TRAJ 训练数据量差异 175×，Abstract "identical data" 构成 overclaim；(2) repo-level 多数配置仅 1-2 seeds，seed variance 可达 7-8pp，远超 formulation 间差异的可靠检测范围；(3) NaN validation loss 导致 checkpoint 选择策略不一致，与 "formulation-inherent" causal claim 冲突；(4) 4-8B LoRA fine-tuned CWM 的结论不能外推为 generation formulation 的普遍判断。

主要发现的非显然性有限：CWM 在 long-output + exact match 条件下失败可从 formulation first principles 推导；function-level equivalence 符合 "short output → generation ≈ classification" 的直觉。

建议作为 Findings 考虑接收，前提是解决 N1-N4 的核心 confound 问题并适当弱化 repo-level claims 的 strength。若能在 rebuttal 期间补充多种子实验和统一 checkpoint 的 ablation，论文质量将显著提升。

---

## Detailed Comments by Section

**Abstract**: 数据密度过高（W2）。"identical data" 表述需修正（N1）。建议精简至 2-3 个关键数字。

**Introduction**: Contribution #4 中 re-repair pilot 应移除或降级（W5）。"No single formulation dominates" 需修正为更精确的 framing（W3）。

**Method**: Oracle Accuracy-Utility Framework 使用 function-level ICC=0.191，Appendix 已论证为 conservative lower bound（已消解），但建议同时报告 repo-level ICC 下的结果。

**Experiments (Function-level)**: 稳健，统计方法论到位。TOST ±2pp margin sensitivity 应在主文补充（W7）。

**Experiments (Repo-level)**: 论文最核心但证据最薄弱的部分。N2（统计效力）、N3（checkpoint confound）、N4（scale generalizability）共同削弱。"Cross-model validation confirms formulation-inherent" 的 claim 需大幅弱化：CWM eval seq_length 不一致（W4）、checkpoint 策略不一致（N3）、context length asymmetry 未完全消除（W9，虽影响 <3%）。

**Related Work**: 总体组织合理（thematic grouping），但第一段 citation density 过高。缺失 5 篇重要引用（W8）。

**Conclusion**: "complexity-aware routing" 缺乏 empirical support（W6）。Limitations 需改为独立 section（W1）。

**Appendix**: 内容充实，消融覆盖面广。Extended Limitations 的坦诚值得认可。