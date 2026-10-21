---
round: 1
overall_score: weak reject
timestamp: 2026-05-14T12:43:29.380480+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 1

**论文**: Death Avoidance Dominates Routing Signal in LLM Agent Computation
**Venue**: EMNLP 2026 Main Conference (ACL ARR May cycle)
**ARR 截止日期**: 2026-05-25
**审稿编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计+格式合规；R2: 新颖性+相关工作+写作质量）
**交叉回应**: 完成，关键问题高度共识

---

## Summary

论文提出 episode-level counterfactual analysis 方法，分析 LLM agent 在 ScienceWorld 环境中 internal reasoning 与 deterministic computation 之间的 routing signal。通过对 245 episodes（11 task types）进行配对实验，发现 Death Avoidance Factor (DAF) = 90.41%——即 deterministic computation 的优势约 90% 来自避免 agent 死亡（-100 penalty），而非正向任务指导。训练的 router 未显著优于 always-deterministic 策略。

---

## Strengths

1. **研究问题有价值**：不问"如何 route 更好"，而是问"routing 到底学到了什么"——这种分析视角在 tool-use 文献中稀缺。[R1, R2 共识]
2. **Episode-level counterfactual 方法论**：对 sparse-reward 环境中 per-step oracle 退化问题（98.2% tie rate）的解决方案简洁有效。[R1, R2 共识]
3. **统计证据在所选环境内扎实**：Pearson r = 0.9698 (p = 8.12×10⁻⁷) 跨 11 task types；DAF decomposition 干净利落。[R1, R2 共识]
4. **诚实报告 negative result**：trained router ≈ always-deterministic 的发现对社区有实际价值，避免 routing 系统的过度工程化。[R1, R2 共识]
5. **写作简洁**：逻辑线清晰，不冗余。[R1, R2 共识]

---

## Weaknesses

### Must-Fix（5 个 critical，影响接收决定）

**[C1] DAF ≈ 90% 可能是 death penalty magnitude 的数学必然** [R2 首提，R1 交叉 AGREE 并补充解析论证]
- ScienceWorld death penalty = -100，死亡率差异 (0.429−0.163)×100 = 26.6 ≈ Δ_full = 29.60。DAF 在数学上近似 δ·P/(δ·P+Δ_nd)，P=100 时只要 δ>0，DAF 就天然很高。这不是需要 245 episodes 才能发现的 empirical finding。
- **缺失**: penalty sensitivity analysis（P=10/25/50/100）来证明 DAF 不仅是 penalty 的函数。
- **严重性**: 如果成立，论文的核心贡献从"empirical discovery"降级为"已知数学关系的验证"。

**[C2] 标题/Abstract 的普遍性声明与实验 scope 严重不匹配** [R1-N1, R2-N2, R2-W4，完全共识]
- "in LLM Agent Computation" 暗示跨环境、跨模型的一般性结论。实际：1 环境 (ScienceWorld)、1 LLM (Qwen2.5-7B-Instruct)、11/30 task types、245 episodes。
- ScienceWorld 的 -100 death penalty 是极端设计；在 WebArena、ALFWorld、AgentBench 等无 catastrophic failure 的环境中，DAF 可能大幅降低。
- 论文在 Conclusion 末段承认限制，但标题和 Abstract 未做任何限定。

**[C3] Limitations 未作独立 section** [R1-N2, R2-N4，完全共识]
- conclusion.tex 使用 `\paragraph{Limitations and Future Work.}` 嵌在 Conclusion 内，违反 ACL ARR 对独立 `\section*{Limitations}` 的明确要求。可能导致格式检查不通过。

**[C4] Router 训练的 train/test 划分完全缺失** [R1-N3, R2 交叉 AGREE 并升级]
- §4.3 使用 245 episodes 训练 router，但未报告 train/test 划分、Table 1 中 Trained Router 数字来自哪个集合、是否有 cross-validation。
- R2 补充：245 episodes 中仅 9 个 internal_preferred，split 后少数类评估可能无意义。

**[C5] Related Work 严重不足** [R2-N3, R1 同意方向]
- 仅 4 小段 13 篇引用。完全缺失关键方向：
  - Safe RL / safe exploration（García & Fernández 2015; CPO, Achiam et al. 2017）——death avoidance 本质上是 safety constraint
  - Risk-sensitive RL（Dabney et al. 2018）
  - Selective prediction / abstention（Geifman & El-Yaniv 2017; Kamath et al. 2020）
  - ScienceWorld 上的其他 agent 工作
  - LLM confidence calibration
  - Agent 评估 benchmark 对比（AgentBench, WebArena, ALFWorld）

### Should-Fix（8 个 warning，影响评分但不一票否决）

**[W1] 图表严重不足** [R2-W1, R1 交叉 AGREE]：8 页长文仅 1 图 1 表。缺 method pipeline overview、per-task DAF bar chart、定性 episode trajectory 示例。

**[W2] 缺少 death-aware heuristic baseline** [R1-W4, R2 交叉 AGREE]：核心发现是 death avoidance 主导 routing，但未测试最自然的 follow-up——基于 uncertainty/danger 信号的 selective routing baseline。

**[W3] Prescreening 标准不透明** [R1-W2, R2 交叉 AGREE]：11/30 task types 的选择标准未公开。若被排除的 19 个 task types 死亡率低，DAF 90.41% 可能是 selection bias 的结果。

**[W4] Abstract 数字堆砌** [R2-W3, R1 交叉 AGREE]：Abstract 包含 ~9 个具体数值，认知负荷过高。建议精简至 3-4 个关键数字。

**[W5] 90% CI 而非 95% CI** [R1-W1, R2 交叉 AGREE]：非标准选择，未论证理由。更窄的 CI 可能误导读者对结果显著性的判断。

**[W6] Episode-to-step label noise 讨论不足** [R1-W5, R2 交叉 AGREE]：Episode-level label 赋予所有 step 会产生系统性 mislabeling（死亡前的 step 可能不需要 deterministic computation）。未分析死亡发生时间点分布和 mislabeling 比例。

**[W7] 缺少 Ethics Statement** [R1-W6, R2 交叉 AGREE]：EMNLP 鼓励包含。

**[W8] DAF 在 Δ_full 接近 0 时数值不稳定** [R1-W3, R2 部分反驳]：论文处理了 Δ_full=0（undefined），但 near-zero 时统计噪声可导致 DAF 大幅波动。R2 认为可在 appendix 补充。

---

## Reviewer Consensus

以下问题双方完全一致 [AGREE]：
- C1-C5 所有 critical 问题
- W1-W7 中的 7 个 should-fix
- 格式问题（bib key 不一致、缺 Ethics Statement）
- 优势评价（研究问题有价值、方法论对 sparse-reward 有贡献、统计扎实、negative result 有意义）

## Reviewer Divergence

仅 2 个 should-fix 级别的分歧，不影响整体判断：

1. **"Counterfactual analysis" 术语是否 overclaim** [R2-W2]：R2 认为实际是 paired strategy comparison 而非因果推断意义的 counterfactual；R1 反驳，认为在 potential outcomes framework 下用词合理。**Director 判断**：论文用法在方法论上可接受，但建议加脚注说明与 NLP counterfactual data augmentation 的区别。

2. **Router training 混淆变量是否充分控制** [R2-W5]：R2 认为 architecture/training strategy/class imbalance 未充分控制；R1 反驳，指出论文测试了两种架构、多种 class balancing 策略、gradient accumulation 影响，在 diagnostic probe 定位下控制充分。**Director 判断**：在 diagnostic probe 定位下，R1 的论证更有说服力。

---

## Questions（需作者澄清）

1. Prescreening 排除了哪 19 个 task types？排除标准是什么？全集上的 DAF 是多少？
2. Table 1 Trained Router 的分数是在训练集还是测试集上计算的？数据划分策略是什么？
3. 如果 death penalty 降至 -25 或 -10，DAF 预计会如何变化？是否做过 sensitivity analysis？
4. 245 episodes 中 9 个 internal_preferred——如此极端的类别不平衡下，router training 的评估是否有统计意义？
5. 死亡通常发生在 episode 的哪个阶段（前期/中期/末期）？这对 step-level label noise 有何影响？

---

## Missing References

两名 Reviewer 共同识别的缺失引用方向（按优先级排序）：

1. **Safe RL / Constrained RL**: García & Fernández (2015) "A comprehensive survey on safe reinforcement learning"; Achiam et al. (2017) CPO
2. **Risk-Sensitive RL**: Dabney et al. (2018) distributional RL
3. **Selective Prediction / Abstention**: Geifman & El-Yaniv (2017); Kamath et al. (2020)
4. **ScienceWorld Agent Work**: 该环境上的其他 agent 系统和分析工作
5. **Agent Benchmarks**: AgentBench, WebArena, ALFWorld——用于讨论泛化性上下文
6. **LLM Confidence Calibration**: routing 的核心是 death avoidance → LLM 对 hallucination 的 calibration 质量相关
7. **Counterfactual Methods in RL**: Kaushik et al. (2020)——R1 认为关联较弱，R2 认为应引用

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。项目未配置外部审稿功能。

---

## Overall Assessment

**Overall Score: Weak Reject (2.25/5)**

| 维度 | R1 | R2 | 合并 |
|------|----|----|------|
| Soundness | 3.0 | 3.0 | 3.0 |
| Excitement | 2.5 | 2.0 | 2.0 |
| Reproducibility | 3.0 | 3.0 | 3.0 |
| Overall | 2.5→2.0* | 2.0 | 2.25 |

*R1 在交叉回应中表示，基于 R2-N1（DAF 为 penalty 的数学必然）的论证，可能将 Overall 从 2.5 下调至 2.0。

**置信度**: 4/5（双方均为 4/5）

**判断理由**：

论文提出了一个有价值的分析视角（routing 学到了什么）和干净的方法论（episode-level counterfactual + DAF decomposition），在 sparse-reward 环境中克服了 per-step oracle 退化问题，且诚实报告了 negative result。

然而，两个根本性问题使论文在当前状态下不满足 EMNLP Main Conference 标准：

1. **核心发现的 triviality 风险 (C1)**：DAF ≈ 90% 在数学上几乎是 -100 death penalty 和死亡率差异的直接推论。如果不通过 penalty sensitivity analysis 证明 DAF 在不同 penalty 下的行为，论文的核心发现停留在"验证已知数学关系"层面，而非"发现新的经验规律"。

2. **Scope 与 claim 的根本不匹配 (C2)**：单环境、单模型、子集 task types 的实验无法支撑标题暗示的一般性结论。这不是简单的 wording 修改能解决的——要么大幅降低 claim scope（可能影响论文吸引力），要么增加实验覆盖（需要大量额外工作）。

格式问题 (C3: Limitations section, C5: Related Work 覆盖) 可在修订中解决，但 C1 和 C2 需要实质性的额外实验和分析。

**建议轨道**：如果作者能解决 C1（sensitivity analysis）并适度扩展 C2（至少 1 个额外环境或 LLM），本文适合 EMNLP 2026 **Findings** track。当前状态不适合 Main Conference。

---

## Detailed Comments

### §1 Introduction
- 第一段的 ScienceWorld boiling water 例子生动有效
- "98.2% tie rate" 的 motivation 令人信服——这是论文最有力的贡献之一
- 但 overclaiming 从第一句就开始：应限定研究范围

### §2 Method
- §2.1 counterfactual collection 的实验设计在所选环境内是合理的
- §2.2 labeling scheme 的 4 cases 逻辑清晰，但未讨论边界情况（如 both dead 时的 score 是否有信息量）
- §2.3 DAF 定义简洁，但需讨论与 penalty magnitude 的解析关系以及 near-zero 稳定性
- §2.4 rule-based baseline 的 failure 有说服力

### §4 Experiments
- §4.1 DAF decomposition 是论文最强的部分：scatter plot + correlation 构成有力证据
- §4.2 baselines：oracle degeneracy (96.3%) 是重要发现；缺 death-aware heuristic baseline
- §4.3 router diagnostic：分类 head 退化为 always-deterministic 和 implicit router 的 GA 依赖性是有价值的观察；但 train/test 不清使结果存疑
- 整体图表不足：仅 Fig 1 + Table 1 对于 8 页长文过于单薄

### §5 Related Work
- 覆盖严重不足，safe RL 是最大缺口
- 每段过于简略（2-4 句），缺乏深度对比

### §6 Conclusion
- Limitations 内容合理但格式不合规
- Future Work 方向（DAgger-style, code-interpreter, multi-LLM）合理
