---
round: 8
overall_score: 3.0 — Findings
timestamp: 2026-05-18T14:27:58.575519+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 8 (Fresh Review)

**论文**: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: Fresh review（两位 Reviewer 独立初审 + 交叉分享，1 轮收敛）

---

## Summary

本文研究用 forward KL 蒸馏替代 per-neuron BCE 训练 SwiGLU LLM 的激活稀疏性预测器。核心论点：BCE 梯度对每个 neuron 独立（Eq. 9-10），而 KL 梯度通过下游层 Jacobian 耦合所有 neuron（Eq. 11），更适合 TEAL 的 global top-k 推理分配。在 LLaMA-3.1-8B 上，轻量预测器（75.9M 参数，<1% base）在 30-70% 稀疏度下 PPL 优于 TEAL 18-82%，使补偿网络（+67.2M 参数）冗余。跨架构验证覆盖 Mistral-7B 和 Qwen-2.5-14B。论文还分析了三个 allocation-dependent 的 operating regions。

---

## Strengths

**S1.** 梯度结构分析清晰有力（§3.6）：BCE gradient 仅依赖 neuron j，KL gradient 通过 factor (b) 耦合所有 neuron。简洁且有启发性。

**S2.** F1-PPL 反向解耦是有说服力的实证发现：BCE 在 oracle F1 上领先 +7pp 却 PPL 差 139%（Table 3），说明 per-neuron accuracy 是错误的代理指标。

**S3.** 诚实报告负面结果：14B MMLU gap（-8.1pp）、无 wall-clock speedup、30% global allocation seed 不稳定性（σ=9.5pp）均如实报告。

**S4.** 消融设计较完整（Table 3）：覆盖 divergence direction、relaxation method、loss isolation、compensation redundancy。

**S5.** 跨架构 PPL 优势一致（Table 6）：LLaMA-8B、Mistral-7B、Qwen-14B 三架构 30-70% 稀疏度优势比 1.22-5.59×。

**S6.** 写作质量高：结构紧凑，数学符号一致，表格信息密度高，自我定位准确（"primarily empirical"）。

---

## Weaknesses

### Critical（影响接收决定）

**C1. Coupling vs oracle quality confound 未隔离** [R1-N1 + R2-W5, 交叉全 AGREE]
- BCE 使用 magnitude-based oracle masks，KL 直接优化输出分布——gradient coupling 和 optimization target 两个变量同时变化。
- 论文在 §4.3 自行承认 "an ablation using KL-derived masks as BCE targets would isolate the effect" 但未执行。
- Oracle F1 分析不能区分是 coupling 还是 target quality 的贡献。BCE isolation ablation（BCE+Gumbel+Penalty = 38.02 vs vanilla BCE 27.97）反而说明 Gumbel+Penalty 框架与 BCE 不兼容，非有效隔离。
- 这是 contribution 1 和 2 的根基。如果改善主要来自 target quality，核心叙事需重构。
- **所需修改**: 执行 KL-derived masks as BCE targets 消融。

**C2. 14B MMLU 反转与核心叙事矛盾** [R1-N3 + R2-N2, 交叉全 AGREE]
- Qwen-2.5-14B 30%: KL PPL 7.62（最优）但 MMLU 63.72 vs TEAL 71.83（-8.1pp），GSM8K 48.82 vs BCE 53.07（-4.3pp）。Uniform 仅恢复 +0.8pp。
- 核心叙事 "output-distribution preservation beats per-neuron classification" 在 14B downstream 上被反驳。
- §4.6 "knowledge density" 解释是未验证推测。
- Abstract "confirms the PPL advantage across 7-14B" 是 selective reporting——PPL 确认但 downstream 反转。
- **所需修改**: (1) Abstract/Intro 将 scope 限定为 7-8B，14B 作为 limitation 而非 confirmation；(2) 14B 补充 per-layer retention 分析和更多稀疏度点。

**C3. Three Operating Regions 证据不足** [R1-N2, R2 AGREE with nuance]
- 每个 regime 仅一个数据点（30%/40%/50%），40% 为单 seed。
- 30% global MMLU σ=9.5pp，40% 的 global-uniform 差异 7.4pp 可能在 seed variance 内。
- 边界（35%? 45%?）完全未知。论文承认需 denser sampling（L151）但 framing 仍为确定性 "three operating regions"。
- **所需修改**: 补充 25%/35%/45% 至少 2-seed 实验，或将 framing 弱化为 "non-monotonic allocation preference observed at sampled sparsity levels"。

**C4. `\enlargethispage{10\baselineskip}` 格式违规** [R2-N3 critical + R1-W1 high warning]
- experiments.tex L253 人为扩展第 8 页约 10 行。第 8 页内容密度远超其他页（Tables 5-7、regime 分析、SPON、cross-arch、14B、latency、Conclusion）。
- ACL 模板禁止修改 margins/layout。R2 认为有 desk reject 风险，R1 认为更可能要求修改。两人一致要求移除。
- **所需修改**: 移除 `\enlargethispage`，将 SPON 详细分析或部分 Table 移至 appendix。

### Should-Fix（影响评分但不一票否决）

**W1. 方法论新颖性有限** [R2-N1 critical, R1 AGREE with nuance]
- Forward KL、Gumbel-Sigmoid、adaptive penalty 均为成熟技术。MaskLLM 已将 frozen weights + learnable masks + KL + Gumbel 用于 LLM sparsity。
- R1 指出 MaskLLM 是 static N:M weight sparsity，与本文 dynamic per-token activation sparsity 是不同问题，技术栈重叠是表面层面的。
- 共识：方法论创新不足以支撑 Main Conference；作为 empirical contribution 适合 Findings。

**W2. 50% downstream collapse 与 Abstract framing 不一致** [R2-W1, R1 AGREE]
- Abstract 突出 "PPL advantage widens to 49%" 但 50% MMLU ≈ 28%（≈random）、GSM8K <2.2%。
- 后半句 hedge 不足。读者首先记住 "49% advantage"。

**W3. BCE 30% baseline 缺失** [R1-W2, R2 AGREE]
- 30% 是 recommended operating point，但 Table 2 无 BCE 30% 行。且 BCE 和 KL 的 allocation protocol 不同（FastForward compensation + no TEAL vs TEAL allocation）。

**W4. 训练/评估域重叠** [R1-W3 + R2-W2, 全 AGREE]
- WikiText-103 训练 → WikiText-2 评估（同族）。C4 OOD 在 30% 退化 1.74× vs WikiText-2 1.47×。C4 30% 仅 2-seed，无 downstream。

**W5. SNR 分析覆盖不足** [R1-W4, R2 AGREE]
- SNR 仅测到 step 300（训练 1000 步），但 PPL 在 step 800+ 才收敛。Step 300 称 "convergence" 不准确。Non-monotonic trajectory 可能在 300 步后再次反转。Bootstrap 参数未报告。

**W6. 无实际推理加速** [R1-W6 + R2-W4, 全 AGREE]
- Pipeline +6.4% overhead，unstructured masks 无硬件加速。Limitations 讨论了但 Introduction 应更早 set expectations。

---

## Reviewer Consensus

以下问题两位 Reviewer 在交叉分享后达成一致 [AGREE]：
1. Coupling vs oracle quality confound 是核心 claim 的关键缺陷（C1）
2. 14B MMLU 反转与 output-preservation 叙事矛盾（C2）
3. 格式操纵需移除（C4）
4. 无实际推理加速（W6）
5. 训练/评估域重叠（W4）
6. 论文作为 empirical contribution 适合 Findings 而非 Main（W1）

## Reviewer Divergence

1. **格式操纵严重性**: R2 评为 Critical（desk reject 风险），R1 评为 high-priority Warning（AC 更可能要求修改）。→ 本报告采纳 Critical，因 ARR desk reject checklist 明确列出 margin 修改。
2. **引用数量**: R2 认为 39 篇偏少，R1 REBUT 认为对聚焦论文足够。→ 不列为 issue。
3. **Penalty controller 28.5% 偏差**: R1 列为 Warning（unfair 1.5% sparsity 优势），R2 partial REBUT（interpolation 论证合理，<0.3 PPL 影响）。→ 降为 Info。

---

## Questions for Authors

1. 能否提供 KL-derived masks 作为 BCE targets 的消融？这是隔离 gradient coupling vs target quality 的关键实验。
2. 14B per-layer retention 分布是否与 8B 有质的不同？Late-layer starvation pattern 是否在 14B 上更严重？
3. 论文承认 "PPL is a poor proxy for reasoning"，那为什么核心对比仍以 PPL 为主？是否考虑过以 downstream 为主要指标重新组织叙事？
4. 40% regime 的 global-uniform MMLU 差异（7.4pp）在 multi-seed 下是否可复现？
5. BCE 在 30% 稀疏度下使用 TEAL allocation 的 PPL 和 downstream 是多少？

---

## Missing References

两位 Reviewer 在引用覆盖上有分歧（R2 认为偏少，R1 认为足够）。39 篇引用基本覆盖了关键方向。可考虑补充：
- Expert Choice routing（MoE 方向与 activation sparsity 的交叉）
- Griffin / gated linear unit variants 的稀疏性工作

---

## External Review (Stanford Agentic Reviewer)

未配置。项目 `external_review.paperreview_ai.enabled` 未启用。

---

## Overall Assessment

**评分: 3.0 — Findings**（两位 Reviewer 一致）

**置信度: 4/5**（两位 Reviewer 均熟悉 activation sparsity 和 KL distillation 方向）

**理由**:
8B 上的实证贡献扎实且有启发性——F1-PPL 反向解耦、compensation 冗余性验证、regime 分析定性观察——足以进入 Findings。但三个问题阻止进入 Main Conference：(1) 核心因果 claim（gradient coupling 解释性能差异）存在已知且可解的混淆变量；(2) 14B downstream 结果反转核心叙事（PPL 好但 MMLU -8pp），限制了 generalization claim；(3) 方法是成熟技术的工程组合，无方法论创新。格式违规（`\enlargethispage`）需在提交前修复以避免 desk reject 风险。

**EMNLP 2026 评分标准映射**:
- 3.0 = Findings（可被 Findings 接收）
- 论文的 empirical insights（KL > BCE for sparsity prediction、compensation redundancy、allocation-dependent behavior）对社区有参考价值，但 claim 的因果强度和 scale generalization 不足以支撑 Main。

---

## Detailed Comments

### Abstract (abstract.tex)
- 7 句包含 ~11 个数字，密度偏高。建议减至 3-4 个关键数字。
- "confirms the PPL advantage across 7-14B" 是 selective reporting；downstream 在 14B 反转。
- 50% "PPL advantage widens to 49%" 的强调与 downstream collapse 不匹配。

### Introduction (introduction.tex)
- 叙事线清晰：mismatch → gradient analysis → KL → results → contributions。
- Contribution 1 "Empirical observation and quantification" 定位准确。
- 缺少对推理加速的早期 expectation setting。

### Method (method.tex)
- §3.3 Gumbel-Sigmoid relaxation 使用合理。但 Appendix B.1 显示 fixed τ=0.5 略优于 default annealing（PPL 11.861 vs 11.963），与 annealing 动机（exploration→exploitation）矛盾。
- §3.5 Adaptive penalty controller：footnote 诚实承认非 formal dual method。但 30% 处 λ 命中 cap、actual sparsity 28.5% 的影响应在正文注明。
- §3.6 Gradient analysis 数学正确，但本质是 "end-to-end gradient couples variables" 这一公知原则在 sparsity prediction 场景的实例化，analytical novelty 有限。
- Table 1 Taxonomy：在自定义坐标系中填充空白 cell，positioning 价值 > 独立贡献价值。

### Experiments (experiments.tex)
- Table 2 main results 在 multi-seed 覆盖上有进步（30% KL global 3-seed, 50% MMLU 3-seed, BCE 3-seed），但 30% KL uniform PPL（recommended config）仍为单 seed，40% 全部单 seed。
- §4.3 Extended Training Analysis（原 iso-compute）：wall-clock 匹配合理（~46 vs ~45 min），但未报告 BCE 2700 步是否已 converge（training loss plateau？）。
- §4.5 Table 5 三区域分析：定性观察有价值但统计证据不足以支撑 "three operating regions" 的确定性表述。
- §4.6 14B：最弱的一节。"knowledge density" 解释是 post-hoc 推测，无实证。建议大幅弱化 claim scope。
- L253 `\enlargethispage{10\baselineskip}`：必须移除。

### Conclusion (conclusion.tex)
- 3 句，长度合适但内容聚焦 positive findings。"scale-dependent tradeoff warranting further investigation" 对 14B MMLU -8pp 的 hedge 不够。

### Limitations (limitations.tex)
- 覆盖了关键局限（PPL proxy、单目标 predictor、scale、OOD、wall-clock、coupling confound）。质量高于平均水平。

### Format
- `\enlargethispage{10\baselineskip}` 违规（C4）。
- `\label{sec:14b}` 在 `\paragraph` 后，`\ref{sec:14b}` 解析为父级 section 编号。
- Table 2 caption "50% uniform PPL 3-seed (11.92±0.07)" 与 body 中 11.96 不一致。
- Appendix C Figure 3 可能为 placeholder（lagrangian_dynamics.pdf）。