---
round: 19
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-24T23:39:39.646959+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告 — Round 22 (Fresh Review) [交叉回应后修订]

**论文**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning
**Venue**: EMNLP 2026 (ARR)
**审稿模式**: 重新审稿 (fresh)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验有效性；R2: 新颖性+完整性+写作）
**轮次**: 2 轮（初审 + 交叉回应，核心问题达成共识，无需第 3 轮）
**修订原因**: 交叉回应后评分从 3.0 修正为 3.5——两位 Reviewer 在交叉回应中明确维持 3.5（Borderline Conference），初次提交的 3.0 为提前合成的估计值

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束，经 Z3 MAX-SAT 验证后加权聚合答案，旨在超越 Self-Consistency 的多数投票。核心发现为否定性的：在 5 个模型、4 个 benchmark、27 种 training-free 变体上，SICA 相对 SC 无可检测的改进（FDR 校正后无条件显著为正）。论文将此归因于 Symbolic Confirmation Bias（SCB）——自提取约束系统性追随多数票答案，无法提供独立验证信号。进一步提出 DPI 框架解释该现象，探索 27 种修复策略均失败，最后展示 cross-architecture NLI verification 突破瓶颈的初步证据。

---

## Strengths

**S1. 实验规模与统计严谨性在 NLP 否定结果论文中极为突出。** 完整的统计工具链（McNemar、TOST ±2pp 等价检验、BH FDR 校正、10,000 次 bootstrap CI、基于 discordant pairs 的 power analysis）远超该领域平均水平。[R1, R2 共识]

**S2. Oracle 对照实验设计精巧。** Gold FOL/DSL 约束产生显著增益（FOLIO +14.22pp, ProofWriter +11.50pp），有力证明 MAX-SAT 框架本身有效——瓶颈在提取质量而非框架设计。[R1]

**S3. 清晰且可操作的否定结果。** 论文不仅展示"什么不工作"，还解释"为什么不工作"（SCB mechanism），并提供"怎样可能工作"（cross-architecture escape）。诊断框架（BR, K_eff, DRC）具备部署前筛查的实用价值。[R1, R2 共识]

**S4. 约束提取范式内穷举充分。** 27 个 training-free 变体覆盖四大失败类别（退化型、多样性受限型、确认偏差型等），系统封堵"也许换个 prompt 就行"的反驳。[R1]

**S5. Appendix 深度与专业排版。** ~20 页附录覆盖所有策略详细结果、case studies、power analysis、hyperparameter sensitivity，足以支撑独立验证。表格统一使用 booktabs 风格。[R2]

---

## Weaknesses

### Must-Fix（阻碍接收）

**MF1. 标题/Abstract 否定声明强度与统计证据严重不匹配** [R1-N1/N2 + R2-N2, 共识]

"No Measurable Improvement" 在语义上接近 "已证明无改进"，但：
- TOST 等价检验仅 4/16 条件确认等价（§4）
- MDE 为 1.86–4.84pp（Appendix D, Table 5），无法排除 ≤4.84pp 的正效应
- Qwen3-14B 在 FOLIO 上 Δ=+0.92±1.14pp，暗示可能存在小正效应
- 论文自身承认 "Absence of evidence is not evidence of absence for small effects"（§4），但标题直接矛盾此声明

R2 建议替代标题方向 "Self-Extracted Constraints Fail to Improve LLM Reasoning: Evidence for Symbolic Confirmation Bias"，R1 同意——将焦点从绝对无效转向 SCB 机制发现。Abstract 应明确区分 confirmatory conditions（n≥200，MDE<3pp）和 underpowered conditions。

**MF2. SCB 与 CoT confirmation bias 的新颖性分离不充分** [R2-N1 + R1 AGREE, 共识]

论文最大的方法论弱点。SCB 是核心概念贡献，但未提供直接证据将其与已有的 CoT confirmation bias（Wan 2025）区分开。

§5.1 的间接控制（majority vs minority 约束密度 6.0 vs 5.9，去除答案句后 BR 无显著下降）排除了答案泄漏，但未排除 SCB 是 CoT confirmation bias 的下游效应。R1 在交叉回应中补充关键证据：Table 20（Appendix Q）reasoning-process overlap 达 0.69，**支持** SCB 可约化为 CoT bias 的假说——如果推理过程本身高度相关，约束继承这种相关性不需要独立的 SCB 机制解释。

**缺失的关键实验**：对少数票 trace（a_M ≠ a*）中的约束，检验其支持自身答案 vs 全局多数票的比例。此分析仅需对现有数据做条件筛选。若少数票 trace 的约束仍偏向全局多数票（而非自身答案），则 SCB 独立存在的证据成立；否则 SCB 应重新定位为 "CoT confirmation bias 在 symbolic extraction pipeline 中的具体表现形式"。

**MF3. TOST ±2pp 等价 margin 缺乏先验论证** [R1-N2 + R2 AGREE, 共识]

±2pp margin 对核心否定结论有决定性影响：
- Table 23 sensitivity analysis 显示 ±1pp 时零条件通过，±3pp 时更多条件通过
- 论文未解释为何 ±2pp 是 "practically meaningful" 的边界
- 事后 sensitivity analysis 反而暴露了 margin 选择的任意性

建议在主文提供 ±2pp 的先验论证（如基于 prompt engineering 文献的典型效应量），或将 TOST 结果表述为 sensitivity range 而非单一结论。

### Should-Fix（影响质量但非阻碍性）

**SF1. Cross-architecture escape 应明确标注为 exploratory** [R1-W2 + R2-W2, 共识]

Abstract "escapes the bias (+6.67pp, p<0.001)" 给人稳健结论印象，但实际仅 DeBERTa 一种主要 NLI 架构（Appendix V 另测试了 RoBERTa/BART 但结果未在主文展示），显著 gain 仅在 Mistral-7B ProofWriter（SC=39.33%，低于 DeBERTa standalone 55.00%）上观察到。FOLIO +2.94pp 不显著，所有 SC≥72% 的 generator 均 Δ≤+1.47pp。存在结构性 ceiling effect：当 generator SC 超过 verifier standalone accuracy 时，combo 引入噪声而非信号。

建议 Abstract 和 §6 增加 "preliminary" 或 "exploratory" 限定词。

**SF2. 与 PRM/ORM/learned verification 文献讨论缺失** [R2-W3 + R1 AGREE, 共识]

论文的 DPI bound I(C;Y) ≤ I(T;Y) 直接解释了为什么 trained verifier（引入额外训练信号，打破 Markov chain）比 zero-shot self-extraction 更有效。Lightman et al. (2023) 和 Cobbe et al. (2021) 已在参考文献中但正文未建立系统性联系。Math-Shepherd (Wang et al., 2024) 和 GRACE 未引用。补充 1-2 段讨论即可将论文贡献嵌入更广阔的 verification 文献。

**SF3. GSM8K/AIME 并列呈现误导** [R1-W5 + R2 AGREE, 共识]

Table 1 将 confirmatory conditions（FOLIO/PW, n≥200）与 pilot conditions（GSM8K n=30, AIME n=22, MDE>10pp）并列呈现，造成覆盖面更广的错觉。建议 Table 1 增加分隔线或注释标记 "pilot"。

**SF4. Seed replication 对 null-result claim 偏弱** [R1-W4 + R2 AGREE, 共识]

3-4 seeds 是领域常见做法，但对否定结果声明边缘。Qwen3-14B 4-seed Δ=+0.92±1.14pp 和 Mistral-7B FOLIO std=2.70pp 显示 seed 方差可能掩盖小效应。

**SF5. Section 5 信息密度** [R2-W1, R1 部分反对]

§5 约 2.5 页覆盖 SCB 分析 + Observation 1 + DPI + 27 策略失败 + 诊断框架。R2 认为过于密集（§5.2 一段话概括 27 种策略的四类失败模式，读者无法在正文获得细节）；R1 认为在 8 页限制下叙事逻辑清晰（"是什么→为什么→能修吗→怎么判断"），细节已在 appendix 充分展开。

Director 判断：8 页限制下可接受，但建议 §5.2 增加 1-2 句对最有希望的失败案例（如 Cross-model extraction, κ≈0.40-0.47）的定量描述，让读者不必翻 appendix 也能理解关键 trade-off。

**SF6. Observation 1 constraint yield uniformity 需验证** [R1-W1 + R2 partial AGREE]

退化为 majority voting 是代数推论（R1 确认），但 "approximately uniform constraint yield" 假设仅有全局 CV=0.26 中位数。需 per-problem CV 分布直方图以验证该假设在问题级别是否成立。

**SF7. BR 诊断指标角色定位** [R1-W3 vs R2 REBUT, 分歧]

R1 认为 BR_excess≈0 使 BR 冗余于 Observation 1（BR 提供的信息已被 degeneration condition 捕获）；R2 认为 BR 作为低成本实践诊断工具有独立价值（无需运行 oracle 对照即可快速判断约束质量）。

Director 判断：双方均同意 BR 应定位为实践工具而非理论贡献。论文应在正文明确此定位。

**SF8. "Symbolic Mirage" 术语** [R2-W4, R1 部分反对]

R2 认为 "Mirage" 比典型学术用语更 dramatic，审稿人可能持保留态度；R1 认为语境中含义恰当——"mirage" 指约束在 Z3 层面 99%+ 合法但 discriminative value 为零（96.1% argmax 一致），正是"看起来有效但实际不产生区分信号"的恰当隐喻。

Director 判断：术语可保留，但首次使用时增加一句注释说明 "mirage" 指 discriminative value 而非 logical validity，避免潜在误读。

**SF9. Few-shot extraction 未测试** [R1 + R2, 共识]

27 种策略全部是 zero-shot template extraction。Few-shot ≠ trained，属于 training-free 范畴，应被纳入策略范围。Limitations 仅承认未评估 trained extractors，但 few-shot 是更低成本的覆盖缺口。

---

## Questions for Authors

**Q1** [R2 提出, R1 同意]: 能否在 ProofWriter depth-5（gold annotations 可验证 trace faithfulness）的 faithful trace 子集上测量 SCB 是否仍存在？这可直接回答 SCB 是否独立于 CoT unfaithfulness。

**Q2** [R2 提出, R1 同意]: Table 2 暗示当 generator SC 超过 verifier standalone accuracy 时，cross-arch combo 无法提供纠正信号。这是否意味着方法存在内在 ceiling effect？论文应更明确讨论此限制。

**Q3** [R2 提出, R1 回答]: Table 13 中 Cross-model（Δ≈-0.49pp）和 Contrastive Scoring 效应量极小（<1pp）。R1 认为即使增大样本量，改进幅度也不具实践意义。作者如何评估？

**Q4** [R2 提出, R1 回答]: StrategyQA 仅一个模型的数据点（LLaMA-3.1-8B, Δ=+2.00pp, n.s.），覆盖面有限。是否应增加模型或在 Limitations 中说明？

---

## Missing References

1. **Math-Shepherd** (Wang et al., 2024) — Process-level reward model，与论文 DPI 框架直接相关
2. **GRACE** — 与 learned verification 的对比讨论
3. 更系统的 CoT faithfulness 文献（beyond Turpin et al. 2023）
4. Anthropic faithfulness 研究系列

---

## External Review

**状态**：未请求。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（耗时约 3 分钟）

| 严重度 | 数量 |
|--------|------|
| Critical | 1 |
| Warning | 3 |
| Info | 9 |

**Critical**:
- Page 30 几乎全空（仅顶部 2 行文字，95% 空白）。审稿人翻到末页会留下 "赶工/未完成" 负面印象。建议上移内容至 page 29。

**Warnings**:
- Pages 1-2 无任何 display item，第一个视觉锚点（Figure 1）到 page 3 才出现。建议提前到 page 2。
- Page 8 塞入 3 个 display items（Figure 3 + Table 2 + Figure 4）+ Discussion/Conclusion/Limitations，视觉密度过高。
- Pages 6-7 连续纯文本，与 page 8 形成强烈节奏反差。建议将 Figure 3 前移至 page 7。

**Positive**:
- Table 1 排版专业（booktabs, 显著性标记, bold）
- Figure 1 清晰可读，caption 自包含
- Appendix 表格统一 booktabs，组织有序（A-Z）
- 无 margin 溢出、无 LaTeX 残留错误
- Limitations 简短，符合 EMNLP 2026 要求
- Abstract 篇幅接近限制（需核实 200 words）

---

## Overall Assessment

**评分: 3.5 — Borderline Conference**

**R1**: 3.5 | **R2**: 3.5 | **共识**: 3.5

论文在实验严谨性上达到了 conference 水准（power analysis, TOST, 27 策略穷举），SCB 概念具有一定启发价值。但三个核心问题使其无法稳定达到 4.0（Conference）:

1. **标题/claim 与证据的系统性错位**（MF1+MF3）：核心否定结论依赖于 ±2pp 的未论证 margin，且仅 4/16 条件通过等价检验，标题传递的信息远强于实际证据支撑。

2. **SCB 概念的新颖性基础不牢**（MF2）：在缺乏 per-trace 分离测试的情况下，无法排除 SCB 是 CoT confirmation bias 的下游效应而非独立现象。R1 指出 Table 20 process similarity=0.69 进一步支持可约化假说。如果 SCB 可约化为已知概念，论文的理论贡献将大幅缩水。

3. **Cross-architecture escape 过度声明**（SF1）：作为第三贡献，在特定条件下有效的证据不足以支撑 "escaping the bottleneck" 叙事。

如果作者能解决 MF1（重新定位标题和 claim）和 MF2（补充 per-trace 分离分析——仅需对现有数据做条件筛选），论文有潜力达到 4.0（Conference），因为否定结果 + 机制分析的组合在当前 self-verification 研究中具有时效性和实用性。

---

## Detailed Comments

### R1 与 R2 共识点

| # | 问题 | 共识 | 严重度 |
|---|------|------|--------|
| 1 | 标题/claim 过强 | 两人完全一致 | Must-Fix |
| 2 | SCB 新颖性分离 | R2 提出, R1 完全同意并补充 process similarity 证据 | Must-Fix |
| 3 | TOST margin 论证 | 两人完全一致 | Must-Fix |
| 4 | Cross-arch exploratory | 两人完全一致 | Should-Fix |
| 5 | PRM/ORM 讨论缺失 | 两人完全一致 | Should-Fix |
| 6 | GSM8K/AIME 呈现 | 两人完全一致 | Should-Fix |
| 7 | Seed replication | 两人基本一致 | Should-Fix |
| 8 | Few-shot extraction | 两人共识 | Should-Fix |

### R1 与 R2 分歧点

| # | 问题 | R1 | R2 | Director 裁定 |
|---|------|----|----|--------------|
| 1 | Section 5 密度 | 叙事逻辑清晰，可接受 | 过于密集 | 小幅改进即可 |
| 2 | "Symbolic Mirage" | 术语恰当 | 修辞过度 | 保留术语，首次使用加注释 |
| 3 | BR 诊断价值 | 冗余于 Obs 1 | 有独立实践价值 | 重新定位为实践工具 |

### 上轮已修复、本轮 fresh review 未重新提出的问题

- R21-N1: 'structural property' → 'robust empirical regularity'（修改有效）
- R21-N3: 'Self-Extraction Bound' 命名移除（修改有效）
- R21-VL1: Discussion 溢出 page 9（已修复）