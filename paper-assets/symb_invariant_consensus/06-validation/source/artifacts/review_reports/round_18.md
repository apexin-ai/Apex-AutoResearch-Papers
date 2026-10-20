---
round: 18
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T20:33:02.041331+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 21 (Fresh Review)

**论文**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning
**Venue**: EMNLP 2026 (ARR)
**审稿模式**: 重新审稿 (fresh)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验有效性；R2: 新颖性+完整性+写作）
**轮次**: Round 1（一轮收敛，无需第二轮）

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束，经 Z3 MAX-SAT 验证后加权聚合答案，旨在超越 Self-Consistency 的多数投票。核心发现为否定性的：在 6-9 个模型（7B–frontier）、4 个 benchmark、27 种 training-free 变体上，SICA 相对 SC 无可检测的改进（FDR 校正后无条件显著为正）。论文将此归因于 "Symbolic Confirmation Bias"（SCB）——自提取约束系统性追随多数票答案，并提出三个零成本诊断指标（K_eff, BR, CCR）。附带展示跨架构 NLI verifier 可突破自提取瓶颈的初步证据。

---

## Strengths

**S1. 实验规模与统计严谨性在 NLP 否定结果论文中极为突出。** 完整的统计工具链（McNemar 配对检验、TOST ±2pp 等价检验、BH FDR 校正、10,000 次 bootstrap CI、基于 discordant pairs 的 power analysis）远超该领域平均水平。[R1, R2 共识]

**S2. Oracle 对照实验设计精巧。** Gold FOL/DSL 约束产生 +17–30pp 增益（Appendix G），有力证明 MAX-SAT 框架本身有效——瓶颈在提取质量。"Framework works, extraction fails" 的对照逻辑是论文论证的关键支柱。[R1]

**S3. 清晰且可操作的否定结果。** 论文不仅展示"什么不工作"，还解释"为什么不工作"（SCB mechanism），并提供"怎样可能工作"（cross-architecture escape）。诊断框架（BR > 2, K_eff < 3.62, ProcessSim > 0.6）具备部署前筛查的实用价值。[R1, R2 共识]

**S4. 在约束提取范式内穷举充分。** 27 个 training-free 变体覆盖四大失败类别（退化型、多样性受限型、确认偏差型等），系统性地封堵了"也许换个 prompt 就行"的反驳。[R1]

**S5. Appendix 深度。** 20 页附录覆盖 prompt 模板、所有 27 种策略详细结果、case studies、power analysis、hyperparameter sensitivity、cross-model analysis 等，材料足以支撑独立验证。[R2]

---

## Weaknesses

### Must-Fix（阻碍接收）

**MF1. "Structural property" 断言超出纯经验证据所能支撑的范围** [R2-N1, R1 AGREE]
- 位置：Abstract、§5.1、§7
- 问题：论文将 SCB 定性为自提取管线的"结构性属性"，暗示理论必然性。但支撑证据全部是经验性的。27 种 remediation 策略均属同一类型（zero-shot template extraction），而 Appendix Y 自己承认 few-shot/iterative refinement 可能不同。如果未测试的提取策略能打破 M→T→A→C 的 Markov 假设，"structural property"就不成立。
- 要求：将 "structural property" 改为 "robust empirical regularity" 或 "persistent pattern under zero-shot template extraction"，并在 Discussion 中明确界定 SCB 的适用边界。

**MF2. SCB 与 CoT confirmation bias 的实证分离不充分——核心概念新颖性受威胁** [R2-N2, R1 AGREE]
- 位置：§2 "Distinction from CoT confirmation bias"、§5.1
- 问题：论文在概念上区分了 SCB（聚合层面）与 CoT confirmation bias（trace 层面），但缺少关键分离测试：在产生**少数票答案**的 trace 中，提取的约束支持该 trace 自身的少数票答案（CoT bias 预测），还是全局多数票答案（SCB 预测）？BR 指标是 aggregate-level，无法区分两个竞争假说。此分析仅需对现有数据做条件筛选，无需新实验。
- 要求：在主文 §5.1 增加 per-trace 少数票约束指向分析。若约束主要支持各自 trace 答案而非全局多数票，应诚实修正 SCB 定义为 CoT bias 在约束层面的表现。

**MF3. Remark 1 "Self-Extraction Bound" 命名制造不存在的理论新颖性** [R1-N2, R2 AGREE]
- 位置：§5.1 Remark 1、§7 Discussion
- 问题：DPI 对**任何**确定性后处理都成立（I(g(X);Y) ≤ I(X;Y)），这是信息论的基础定理。命名为 "Self-Extraction Bound" 并赋予 Remark 编号暗示了理论创新。更关键的是，DPI **不能解释** SICA 为何失败——DPI 仅说明约束信息量 ≤ traces，但 MAX-SAT 仍可能从相同信息中提取比简单计数更有用的投影。真正解释退化的是经验发现（BR > 1、|C'| ≈ 0、degeneration condition Eq. 4），而非 DPI。
- 要求：移除 "Self-Extraction Bound" 命名；Remark 1 降为一句话 DPI 引用（"By the data processing inequality..."），明确声明 "this is a necessary condition, not a sufficient explanation"；论证重心放在 Observation 1 + BR + degeneration condition 上。

### Should-Fix（影响评分但不一票否决）

**SF1. Cross-architecture escape (Contribution 3) 应降级为 exploratory finding** [R1-N1 raised as Must-Fix; R2 partial REBUT + Director 降级为 Should-Fix]
- 位置：Abstract、§1、§6、Table 3
- 问题：Capability-gap pattern 基于 n=6 Spearman rank correlation；K=12 pilot run。R2 纠正了 R1 的事实错误——Appendix V 实际测试了 3 种 NLI verifier（DeBERTa/RoBERTa/BART），非"单一 verifier"。但 n=6 capability-gap 和 pilot 规模仍偏弱。主文 §6 已使用 "preliminary evidence" 措辞，但 Abstract/Intro 将其与 SCB 诊断并列为主贡献。
- Director 判断：论文措辞已较谨慎且有多 verifier 证据支撑，严重程度从 R1 的 critical 降为 warning。但 Abstract/Intro 应更明确标注 "preliminary/exploratory"。

**SF2. 标题/Abstract 否定声明强于统计证据支撑范围** [R1-W1, R2 AGREE]
- 位置：Title、Abstract
- 问题：仅 4/11 条件通过 TOST ±2pp 等价检验（n ≥ 200 的 confirmatory conditions），7/11 条件 MDE > 5pp（underpowered）。标题 "No Detectable Improvement" 技术上可辩护但读者自然理解为"已证明无改进"。
- 建议：Abstract 中更早限定 "across four confirmatory conditions (n ≥ 200)"。

**SF3. GSM8K (n=30) / AIME (n=22) 对否定论证几乎无贡献** [R1-W3, R2 AGREE]
- MDE 远超 10pp，与 FOLIO/ProofWriter 并列呈现造成"4 个 benchmark 都支持否定结论"的错觉。
- 建议：明确区分 "2 confirmatory + 2 pilot benchmarks" 或将 GSM8K/AIME 移至 appendix。

**SF4. Section 5 信息密度过高——§5.2 压缩过度** [R2-W3, R1 AGREE]
- 约 2.5 页覆盖 SCB 定义、DPI 论证、27 种策略失败、三个诊断指标。§5.2 仅一段话概括 27 种策略的四类失败模式。
- 建议：展开至少 2 个代表性失败案例（如 degenerate 类 + diversity-limited 类）。

**SF5. BR permutation null model 描述不足** [R1-W4, R2 AGREE]
- Within-problem vs across-problem permutation 的区别直接影响 null distribution 和 p-value 的解释。
- 建议：§5.1 或附录补充 permutation 步骤的伪代码。

**SF6. 与 PRM/learned verification 文献的 trade-off 讨论不足** [R2-W5, R1 AGREE]
- SICA 是 formal verification，PRM/ORM 是 learned verification，两者 failure mode 不同。诊断框架（BR/K_eff）可能适用于 learned verifiers。
- 建议：Related Work 或 Discussion 增加 formal vs learned verification trade-off 讨论（1-2 句）。

**SF7. Observation 1 "approximately uniform constraint yield" 假设缺乏敏感性分析** [R1-W5, R2 AGREE with caveats]
- 如果高质量 traces 系统性产出更多约束，SICA 可能通过数量差异隐式质量加权。间接证据存在（Appendix K）但直接敏感性分析缺失。
- 建议：Appendix 补充 constraint yield CV 分析。

**SF8. Seed replication (3-4 seeds) 对 null-result claim 偏弱** [R1-W2, R2 AGREE at lower severity]
- 跨 seed 相关性未建模。3-4 seeds 是领域常见做法但对否定结果声明边缘。
- 建议：Limitations 增加 seed 数量局限性讨论。

---

## Reviewer Consensus [AGREE]

1. **Remark 1 (DPI) 是平凡结论**：双方一致认为 DPI 对任何确定性后处理都成立，命名 "Self-Extraction Bound" 制造不存在的理论新颖性。应降权。
2. **"Structural property" 过强**：双方一致认为应改为 "robust empirical regularity"，因为所有证据是经验性的，且 SCB 适用边界（zero-shot template extraction）未被充分界定。
3. **SCB/CoT bias 分离缺口**：双方一致认为需要 per-trace 少数票约束指向测试来区分两个竞争假说。R1 补充了具体分离测试设计。
4. **n=6 capability-gap 统计不稳健**：双方一致认为 Contribution 3 应降级为 exploratory finding。
5. **GSM8K/AIME 贡献有限**：双方一致认为应明确区分 confirmatory vs pilot benchmarks。
6. **BR permutation 描述不足**：双方一致认为需补充精确构造方式。
7. **统计严谨性是核心优势**：双方一致高度评价统计方法论（TOST/FDR/bootstrap/power analysis）。

## Reviewer Divergence [REBUT]

1. **常识推理基准缺失**（R2-W2 raised, R1 REBUT）：R1 认为论文的 "best-case scenario" 论证策略有效——在最有利条件（形式逻辑任务）下证明失败比在不利条件下证明失败更有说服力。**Director 判断**：R1 的反驳有说服力，降级为 minor（abstract 应限定 "logical/mathematical reasoning benchmarks"）。
2. **标题与 cross-architecture 正面结果的张力**（R2-W4 raised, R1 REBUT）：R1 指出标题限定词 "Self-Extracted" 已准确界定范围，§6 的正面结果不在此范围内。**Director 判断**：R1 的反驳成立，标题无需修改；但 Abstract 应更突出 §6 正面结果。
3. **Cross-architecture escape 严重程度**（R1 rated critical, R2 partial REBUT）：R2 纠正了 R1 的"单一 verifier"事实错误（实际 Appendix V 测试了 3 种 NLI verifier），但同意 n=6 和 pilot 规模偏弱。**Director 判断**：降级为 Should-Fix（warning），因为论文主文已使用 "preliminary evidence" 措辞且有多 verifier 证据。

---

## Questions for Authors

1. **[关键]** 在产生少数票答案的 trace 中，提取的约束更倾向于支持该 trace 自身的少数票答案，还是全局多数票答案？这是区分 SCB（聚合层面偏差）与 CoT bias（trace 层面偏差传递到约束）的关键测试。[R2-Q1, R1 AGREE]

2. K=12 traces 是否不足以让 MAX-SAT 交叉验证机制发挥作用？K=50/100 时 degeneration condition（|C'| ≈ 0）是否仍成立？Appendix I.1 的 K-sensitivity 仅测到 K=20。[R1-Q1]

3. 27 种策略全部使用 zero-shot template extraction。是否考虑过 few-shot extraction 或 iterative refinement？如果未测试，"structural property" 的断言基础是什么？[R2-Q2]

4. Remark 1 的 Markov 假设（constraints are trace-determined: c_i = f(t_i)）在什么条件下可能不成立？是否有 trace perturbation 实验验证此假设近似成立？[R2-Q3]

5. BR 在高精度模型上（SC > 90%）估计不稳定。这些条件的 BR 值是否应排除在 cross-model 结论之外？[R1-Q2]

6. 用更强模型（GPT-4）作为 extractor 提取弱模型 traces 的约束，结果是否不同？论文的 Markov chain 论证预测不会改变（SCB 是 trace-answer coupling 的属性），但值得实验验证。[R1-Q4]

---

## Missing References

- **Wang et al. (2024), "Math-shepherd"**: step-level verification 的 learned 范式，与 SICA 的 formal verification 形成直接对比 [R2]
- **Khalifa et al. (2023), "GRACE"**: 判别器引导 CoT，learned verification 的另一个相关 baseline [R2]
- **Universal Self-Consistency (Chen et al., 2024)**: 论文已引用但 Related Work 中与 SICA 的 failure mode 对比讨论不足 [R1]
- **Self-Debate (Du et al., 2023 / Liang et al., 2024)**: 作为 training-free self-improvement 的重要类别，应在 Related Work 中说明排除理由 [R1]

---

## External Review

外部审稿未配置（`external_review.paperreview_ai.enabled: false`）。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时约 5 分钟）

| 严重度 | 位置 | 发现 |
|--------|------|------|
| ⚠️ warning | Page 9 | **Section 7 (Discussion) 溢出约 1 行到第 9 页顶部**（Limitations 之前）。EMNLP 2026 严格 8 页限制，部分 AC 可能视为超页 desk reject。建议缩紧正文使 Discussion 收在第 8 页内。 |
| ⚠️ warning | Page 7 | **Figure 4（27 策略汇总）字号过小**（≤6pt），策略名称在打印时难以辨认。建议改为 figure*（全宽）或减少展示条目。 |
| ℹ️ info | Page 1 | 首页无视觉锚点（纯文本），第一个 display item 是 Figure 1（p.2 顶部），pipeline 图清晰。 |
| ℹ️ info | Pages 2-8 | Figure 1/2/3/4、Table 1/2/3 布局规范，booktabs 风格一致，颜色方案对色盲友好。 |
| ℹ️ info | Page 9 | Limitations 简短（~3 个要点），符合 EMNLP 要求。 |
| ℹ️ info | Pages 9-11 | 参考文献格式统一（author-year），无 [?] 未解析引用。 |
| ℹ️ info | Pages 12-28 | Appendix A-Z（26 个附录）内容丰富，表格格式一致。 |

---

## Overall Assessment

**Overall Score: 3.5 / 5 — Borderline Conference**

**综合评价**：这是一篇实验设计严谨、规模充分的否定结果论文，对 neuro-symbolic reasoning 和 LLM self-improvement 社区有重要实践意义。统计方法论（TOST/FDR/bootstrap/power analysis）远超领域平均水平，oracle 对照实验设计精巧，SCB 诊断框架有实用部署价值。

三个 Must-Fix 问题阻碍当前版本达到 Conference（4.0）水平：
1. **"Structural property" 断言过强**：需改为 "robust empirical regularity"，明确界定 SCB 适用边界
2. **SCB 与 CoT bias 的实证分离缺失**：需补充 per-trace 少数票约束指向分析（仅需对现有数据做条件筛选）
3. **Remark 1 DPI 命名制造虚假理论贡献**：需移除 "Self-Extraction Bound" 命名，降权处理

若以上三项在 rebuttal/revision 中充分解决（特别是 #2 的实证分离测试），且 Contribution 3 被明确标注为 exploratory finding，论文有望上调至 **4.0（Conference）** 水平。

**Soundness**: 3.5/5（统计方法论严谨，但理论包装有虚假成分）
**Excitement**: 3.25/5（否定结果有实践价值+诊断框架可操作，但受限于结论保守性）
**Reproducibility**: 4/5（方法细节充分，代码承诺开源）
**Confidence**: 4/5

---

## Detailed Comments

### §1 Introduction
- "structural property of self-extraction pipelines" → "robust empirical regularity observed under zero-shot template extraction"
- Contribution 3 的表述应加 "preliminary/exploratory" 限定词
- 三大贡献中 Remark 1 (DPI) 不应作为独立贡献列出

### §2 Related Work
- "Distinction from CoT confirmation bias" 段落：概念区分清晰但缺乏实证支撑——应在此预告 §5.1 中的分离分析
- 补引 Math-Shepherd (Wang et al., 2024)、GRACE (Khalifa et al., 2023)
- 增加 formal vs. learned verification trade-off 讨论

### §3 Methodology
- Eq. 5 (BR) 的 permutation null model 需补充构造细节（within-problem vs across-problem）

### §4 Results
- 明确区分 confirmatory conditions (FOLIO/ProofWriter, n ≥ 200) 与 pilot conditions (GSM8K/AIME, n ≤ 30)
- 考虑将 GSM8K/AIME 结果移至 appendix

### §5 The Symbolic Mirage
- §5.1: 增加 per-trace 少数票约束指向分析（MF2 的核心要求）
- §5.1 Remark 1: 移除 "Self-Extraction Bound" 命名，降为一句话 DPI 引用
- §5.2: 展开至少 2 个代表性失败案例（当前一段话过于压缩）
- §5.3: 诊断指标部分细节可移至 appendix 以腾出空间

### §6 Cross-Architecture Escape
- 主文应引用 Appendix V 的多 verifier 结果（DeBERTa/RoBERTa/BART），不应只提 DeBERTa
- Capability-gap pattern 的 n=6 Spearman correlation 应标注统计局限性

### §7 Discussion
- 溢出约 1 行到 page 9，需缩紧以避免 desk reject 风险

### Limitations
- 增加 seed 数量局限性讨论
- 增加 Observation 1 constraint yield uniformity 假设的局限性

### Figures
- Figure 4 (p.7): 改为 figure*（全宽）或减少条目数，当前字号 ≤6pt 打印难辨