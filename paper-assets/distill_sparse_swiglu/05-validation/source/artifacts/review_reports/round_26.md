---
round: 26
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T04:46:03.324911+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — Round 29 (Fresh Review)

**论文**: Distilling Sparse SwiGLU Activation Patterns from Dense Models
**目标 Venue**: EMNLP 2026 (via ARR)
**审稿人**: Reviewer 1, Reviewer 2
**交叉回应**: 已完成（双向逐条 AGREE/REBUT）

---

## Summary

本文系统研究了如何训练一个轻量级 predictor 来预测 LLM 中 SwiGLU FFN 层的 activation sparsity masks。核心发现：以 output-distribution KL 散度作为训练目标，相比传统的 magnitude-based binary cross-entropy (BCE)，在 PPL 上实现 14.5% 的改善（matched-sparsity）。论文比较了 5 种 loss function（Forward KL, Reverse KL, JSD, BCE, MSE），提供了 target-swap ablation (C1)、per-layer coupling decomposition (§4.5)、constraint analysis (Appendix T) 等实验分析。实验覆盖 LLaMA-3.1-8B（主实验）、Mistral-7B-v0.3 和 Qwen-2.5-14B（跨架构验证），在 30% 和 50% sparsity 下评估。

---

## Strengths

**S1: PPL 改进真实可靠。** 核心 claim（KL 训练的 predictor 在 PPL 上优于 BCE/TEAL）有充分统计支撑。3-seed 评估下 PPL σ=0.02（CV=0.2%），置信区间远窄于方法间差距。14.5% matched-sparsity 改进在三个架构上一致复现（LLaMA −14.5%, Mistral −17.3%）。

**S2: 实验框架设计有价值。** 5 种 loss function 的系统比较（Table 5）、C1 target-swap ablation、predictor capacity sweep（Table 6）、temperature schedule 变体（Table 7）、training duration sweep（Table 8）构成了一个可复用的实验框架。这对后续 sparsity prediction 研究有直接参考价值。

**S3: 坦诚度高于平均水平。** 论文诚实地报告了负面结果：(a) 知识任务退化并在 Abstract 中量化；(b) 无 wall-clock 加速并在多处声明；(c) MSE 不稳定（2/3 seed 崩溃）用 § 标注；(d) downstream 指标标注为 "directional (n=3)"。这种透明度值得肯定。

**S4: 跨架构验证覆盖合理。** 三个架构覆盖 GQA (LLaMA)、GQA+sliding window (Mistral)、不同 d_ff 维度 (Qwen-14B)，7B-14B 范围。Mistral 有完整 3-seed 评估（PPL + 6 downstream tasks）。对于 8 页限制的论文，验证覆盖度合理。

**S5: Gumbel-Softmax 优于 STE 的论证清晰。** §3.3 的理论论证（STE 的 discontinuous gradient 导致 oscillation）结合 33.8% 的 PPL 改善（15.77→11.79 at 50%），形成较强的论证链。

---

## Weaknesses

### Critical

**W1: §4.5 Per-layer KL decomposition 存在无法分离的 confound [双方 AGREE, 跨 10 轮未解决]**

论文试图通过 K-curve 分解将 KL 优势归因为 "signal type" vs "coupling scope" 两个维度。核心 confound：K=1 训练时每步仅更新 1/32 层的 predictor（~31 updates/predictor），推理时所有 32 层同时激活，存在严重 train-inference mismatch。论文已将 §4.5 restructure 为 observation-first 叙事并加 explicit confound statement，但：

- 50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×）使整个分解在高 sparsity 下失效
- 50% 下 K=1(34.85) 优于 K=4(44.23)，直接否定 "coupling breadth 单调有益"
- Per-layer update count confound 从 R20 至今未有解决方案
- Conclusion 中 "signal type gap (0.47 PPL)" 与 §4.5 的 9.47 (= 18.52−9.05) 疑似排版错误；若确为 0.47，则 "exceeds coupling breadth range (2.08)" 在数学上不成立

**现状评估**：论文已多轮修订降级 claim 强度，当前 framing 为 "exploratory observation" 基本可接受。但 confound 是结构性的，仅靠 framing 调整无法完全化解——严格的审稿人仍可能认为此 section 的证据不支撑其叙事。

**W2: 知识任务退化缺乏因果机制分析 [双方 AGREE, 跨 11 轮未解决]**

KL predictor 在 MMLU 上系统性退步（30% uniform: KL 40.7 vs TEAL 45.86, −5.2pp），论文解释为 "forward KL mode-covering sacrifices rare reasoning-critical activations"，但：

- Appendix T remove-valley → MMLU +3.4pp 说明退化主因可能是 allocation pattern（valley 结构）而非 KL 固有属性
- Appendix S K=4 MMLU≈43.5 接近甚至超过 dense baseline，进一步支持 allocation 而非 loss 是主因
- 论文的两个解释（"KL mode-covering" vs "allocation-induced"）之间存在未解决张力
- C4 control（排除训练数据偏差）仅 1 seed，且 s42 MMLU=40.6 vs 3-seed mean ~28.5，说明 s42 是高异常种子，单 seed 因果分析不可靠
- 缺乏 neuron-level 归因（哪些 neuron 在 KL vs BCE 下被保留/丢弃，与知识存储的关系）

**现状评估**：论文已将 task-type split 升为 C2、Conclusion 扩展 task-type 讨论。但因果机制仍停留在 "mode-covering" 直觉猜测，未回答 "如果 KL 发现了 PPL 更低的 mask，为何不能保留知识能力" 这一核心问题。

**W3: 高方差下游指标统计可靠性不足 [双方 AGREE]**

PPL claims 稳健（σ=0.02, CV=0.2%），但 downstream claims 不稳健：
- MMLU 30% global: σ=9.5pp, 95% CI ≈ [11.9, 59.5]（t-distribution, df=2）
- Qwen-14B GSM8K: σ=5.3pp, CV=16.5%
- Mistral ARC-c: σ=6.4pp, CV=14.3%

论文已加 "directional (n=3)" 限定和 CI overlap caveat，但 abstract/conclusion 仍报告具体 gap 数值，这些数值在统计上无意义。≥5 seeds 在 14B 有计算限制，应 upfront disclosure 而非作为隐含辩护。

### Warning

**W4: 方法新颖性为组合级别 [分歧: R1 认为可接受, R2 认为进一步限制贡献]**

核心组件（Gumbel-Softmax mask、KL 蒸馏、线性 predictor）均为成熟技术。MaskLLM 共享 recipe-level 原则（Gumbel-Softmax + 可微 mask + 端到端训练）。R1 反驳：MaskLLM 做 N:M weight sparsity，本文做 contextual activation sparsity，不同子领域，直接对比不合理。R2 维持：static→contextual 的技术挑战缺乏形式化论证。**此分歧未解决。** 论文真正的贡献定位是 empirical characterization（5 loss 比较 + ablation framework），不是 method novelty。

**W5: MSE baseline 可能未在最优配置下评估**

MSE 使用与 KL 完全相同的超参数，但 MSE 梯度 magnitude 约为 KL 的 5 倍，可能需更小学习率。2/3 seeds 在 50% 下崩溃（catastrophic PPL=15,789）。PPL 差距（18.52 vs 9.05）可能被高估。Table 4 有 § 标注但数据仍在主表中。

**W6: BCE+Gumbel 劣于 BCE 揭示的 Gumbel-KL 协同效应未讨论**

BCE+Gumbel PPL=32.22 vs BCE PPL=27.97（+15.2%），说明 Gumbel relaxation 对 BCE 有害。这揭示 Gumbel 的价值依赖于 loss 的 coupled gradient 结构（KL 的 Jacobian 能利用 Gumbel 探索，BCE 的 per-neuron 梯度不能）。这是 §3.6 梯度分析的重要实证佐证，但论文完全未讨论。

**W7: STE undershoot 可能高估 Gumbel 独立贡献**

§3.3 报告 Gumbel 比 STE 改善 33.8%（PPL 15.77→11.79 at 50%），但若 STE 实际 sparsity 与目标不匹配（undershoot），部分 PPL 差距可能来自 sparsity level 差异。需 matched-actual-sparsity 对比。

**W8: 主评估指标单一，OOD 评估不充分**

WikiText-2 eval 与 WikiText-103 training 同源（社区标准做法，严重程度有限）。C4 OOD 30% 仅 2-seed、无 TEAL baseline、CV=6.3% vs in-domain 0.2%。

**W9: Contribution C3/C4 标注 "Analytical" 非标准**

"Analytical" 在 ACL/EMNLP 语境通常指理论推导/complexity bounds，但 C3（target-swap ablation）和 C4（compensation redundancy）是实验发现。建议改为 "Empirical" 或 "Empirical-analytical"。Presentation issue，不影响实质。

---

## Questions

**Q1**: K=1 在 50% 优于 K=4 如何解释？是否暗示 coupling 的有益性是 sparsity-conditional 的，"primary design dimension" 需限定为 "at moderate sparsity levels"？

**Q2**: 如果 allocation 调整（remove-valley, K=4）就能大幅修复知识退化，那 "KL mode-covering" 机制在退化中的真正占比是多少？论文能否明确区分 allocation-induced vs loss-inherent regression？

**Q3**: Conclusion 中 "signal type gap (0.47 PPL)" 是否为排版错误（应为 9.47）？若确为 0.47，"exceeds coupling breadth range (2.08)" 在数学上如何成立？

**Q4**: STE 在 matched actual sparsity 下与 Gumbel 的 PPL 差距是多少？当前 33.8% 改善是否部分来自 sparsity level 差异？

**Q5**: 首次 token 延迟（prefill latency）相对于 steady-state throughput 是否有额外开销？论文仅报告了 100 forward passes 的平均值。

---

## Missing References

两位 Reviewer 均未标记缺失引用。论文的 Related Work 覆盖了 activation sparsity prediction 领域的主要工作（TEAL, CATS, MaskLLM, PowerInfer, DejaVu 等）。

---

## External Review

**状态**：未请求。

---

## Visual Layout Check（非评分项）

**状态**：已完成（0 critical, 1 warning, 7 info）

- ⚠️ **Page 20**: 最后一页仅 3 行内容（AI Assistants 声明续），约 95% 空白。建议将内容上移至 page 19 末尾合并。
- ℹ️ **Page 1**: 首页无 display item，Figure 1 出现在 page 2。若能上移可加强第一印象。
- ℹ️ **Page 7**: 三个 table（Table 2/3/4）集中在同一页，视觉密度较高。Tables 格式良好（booktabs 风格、最优值加粗）。
- ℹ️ **Page 3**: Related Work 全页纯文字，无 display item 穿插。
- ℹ️ **Page 6**: Experimental Setup 全页纯文字。
- ℹ️ **Page 16/17/18**: Figure 7/8/9 尺寸偏小，打印时细节可能难以辨认。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| §4.5 confound | Critical | Critical | AGREE |
| 知识退化机制 | Critical | Critical | AGREE |
| 统计可靠性 | Critical | Critical | AGREE |
| 方法新颖性 | Warning（可接受） | Warning（进一步限制） | 分歧 |
| PPL 改进 | 真实可靠 | 真实可靠 | AGREE |

**R1 评分: 3.5 (Borderline Conference)** — 认为 PPL 改进真实、实验框架有价值、坦诚度高。MaskLLM 重叠和跨架构验证不足被 R2 过度强调。

**R2 评分: 3.0 (Findings)** — 认为 MaskLLM recipe-level overlap 限制方法贡献，两个 critical issues 未实质解决，downstream claims 统计无效。

**Director 评估: 3.0 (Findings)** — 论文的 PPL 改进真实可信，实验框架设计有参考价值，坦诚度值得肯定。但三个 critical issues（§4.5 confound、知识退化机制、统计可靠性）均为结构性问题，已通过多轮 framing 调整部分缓解但未实质解决。方法新颖性为组合级别，论文正确定位为 empirical study，但 empirical study 对实验严谨性的要求更高——而论文恰恰在这一维度有显著缺口。§4.5 的 confounded decomposition 虽已降级为 "exploratory observation"，但仍占据论文约 1 页篇幅（含 Appendix S），其证据强度与篇幅投入不匹配。知识任务退化的两个解释之间的张力未解决，使得 C2（task-type split）的贡献价值打折。综合判断：Findings 级别——有实质发现但 claim 强度与证据不完全匹配。

---

## Detailed Comments

### Must-Fix（影响接收决定）

1. **§4.5 confound 限定**：当前 "exploratory observation" framing 方向正确，但 (a) 验证 Conclusion 0.47/9.47 数值是否正确；(b) 考虑将 §4.5 篇幅压缩（当前 confound 程度下，一页篇幅过重）。

2. **知识退化因果分离**：明确区分 "allocation-induced regression"（remove-valley/K=4 证据）和 "loss-inherent regression"（mode-covering 假设），量化各自占比。当前两个解释共存但相互矛盾。

3. **Downstream 统计声明收紧**：Abstract/Conclusion 中报告具体 downstream gap 数值时必须附带 n=3 + CI overlap 限定，或改为仅报告 directional trend 方向不报数值。

### Should-Fix（改善论文质量）

4. **Gumbel-KL 协同效应讨论**：BCE+Gumbel(32.22) vs BCE(27.97) 是 §3.6 梯度分析的天然实证佐证，值得在 §3.6 或 §4.4 中加一段讨论。

5. **MSE lr sweep**：至少在 50% 下对 MSE 做一个 2-3 点 lr sweep，确认 PPL 差距（18.52 vs 9.05）不是超参数不匹配。

6. **STE matched-sparsity 对比**：验证 33.8% 改善中有多少来自 sparsity level 差异。

7. **C3/C4 contribution label**："Analytical" → "Empirical" 或 "Empirical-analytical"。

8. **Page 20 空白**：将 AI Assistants 声明尾部上移至 page 19，消除近空白页。

### Nice-to-Have

9. **C4 control 增至 3-seed**：当前 s42 是 MMLU 高异常种子，单 seed 因果分析可信度受限。

10. **C4 OOD 补充 TEAL baseline**：无法判断 KL 的 OOD 优势是否依然存在。

11. **30% BCE isocompute (2700 steps) 对比**：当前仅 50% 有此对比。
