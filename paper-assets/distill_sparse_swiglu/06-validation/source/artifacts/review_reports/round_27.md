---
round: 27
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T09:37:09.081892+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告 — Round 30 (Fresh Review, Revised)

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**目标 Venue**: EMNLP 2026 (via ARR)
**审稿人**: Reviewer 1, Reviewer 2
**交叉回应**: 已完成（双向）
**修订说明**: 初版报告在 R1 交叉回应到达前提交，本版补充 R1 对 R2 的交叉回应，修正两处 R2 事实错误的影响。

---

## 交叉回应摘要

**R2 → R1**: 对 R1 的 9 条意见 8/9 AGREE（含 2 条建议降级严重性），1 条 REBUT（R1-N3 推理加速——R2 认为应从 Must-Fix 降为 Should-Fix，论文定位为 analysis paper）。R1 的 N2（MSE 未调参）和 S4（decomposition confound）进一步支撑 R2 初审 N2。R1 的 S6（iso-compute）是 R2 遗漏的有价值观察点。

**R1 → R2**: 对 R2 的 2 个 Must-Fix 均 REBUT（基于事实错误），Should-Fix 3/5 AGREE + 1 部分 AGREE。具体：
- **[REBUT] R2-N1 (Abstract 超长)**: R2 声称 Abstract "320+ words, 3 段, 5 个 inline citations"——**三项均为事实错误**。经验证，abstract.tex 全文 ~145 words，1 段，零 \cite 命令。不存在 desk reject 风险。
- **[REBUT] R2-N2 (数值矛盾)**: R2 将 "9.47 PPL" 误读为 "0.47 PPL"。原文 Introduction line 29 和 §4.5 line 166 均写 "signal type gap (9.47 PPL)"。9.47 > 2.08 无逻辑矛盾。R1 指出实质问题是 9.47 的可信度受 MSE 未调参影响（R1-N2），但这不是 R2 所指的 "自相矛盾"。
- **[AGREE] R2-W1 (MaskLLM 新颖性)**: R1 初审未单独提出，R2 补充了有价值视角。
- **[AGREE] R2-W2 (知识退化)**: 与 R1-W5 一致。
- **[AGREE] R2-W3 (并行工作遗漏)**: SVD Contextual Sparsity Predictors 如在提交前发表应讨论。
- **[AGREE] R2-W4 (规模限制)**: 部分同意。
- **[部分 AGREE] R2-W5 (Table 1 不完整)**: MaskLLM 实际已在 Table 1 中（R2 此处有误），但 training-free 维度缺失和 empty cell 语义不清有效。

**Director 对 R2 事实错误的处理**: R2 的两个 Must-Fix（N1 Abstract 超长、N2 数值矛盾）均基于事实错误，从报告中剔除。R2 的 Should-Fix 级别意见（W1-W5）经 R1 验证后保留。R2-N2 的实质性部分（MSE unfairness 削弱 Contribution #2 可信度）被 R1-N2 独立覆盖，纳入报告 W1。

---

## Summary

本文系统比较了 5 种训练目标（Forward KL, Reverse KL, JSD, BCE, MSE）用于训练 SwiGLU LLM 的 contextual sparsity predictor。核心发现：以 output-distribution forward KL 散度配合 Gumbel-Sigmoid relaxation 作为训练目标，在 PPL 上实现 14.5% 的改善（matched-sparsity, LLaMA-3.1-8B, 30%）。论文提供了 target-swap ablation (C1)、per-layer coupling decomposition (§4.5)、constraint analysis (Appendix T) 等分析实验。跨架构验证覆盖 Mistral-7B-v0.3 和 Qwen-2.5-14B。实验在 30% 和 50% sparsity 下评估，附 6 项 downstream task。

---

## Strengths

**S1: PPL 改进真实、统计稳健、跨架构一致。** 核心 claim（KL predictor 在 PPL 上优于 BCE/TEAL）有充分统计支撑：3-seed 评估 σ=0.02（CV=0.2%），置信区间远窄于方法间差距。14.5% 改进在 LLaMA 和 Mistral（−17.3%）上一致复现，Qwen-14B PPL 同样验证。

**S2: 实验框架设计系统、可复用。** 5 种 loss function 的系统比较（Table 4）、C1 target-swap ablation（Table 3）、predictor capacity sweep、temperature schedule sweep、training duration sweep 构成完整的实验框架。特别是 C1 ablation 设计精巧——通过将 KL 发现的 mask 交给 BCE 训练（PPL gap ≤0.03pp at s123/s456），成功分离 "发现的 mask 模式" vs "训练时的梯度耦合"。

**S3: 高度透明。** 论文诚实报告负面结果：(a) 知识任务退化在 Abstract 中量化；(b) 无 wall-clock 加速在多处声明；(c) MSE 2/3 seed 崩溃用 § 标注；(d) downstream 指标标注 "directional (n=3)"；(e) Limitations 覆盖 MSE 超参问题和 WikiText 同源评估。

**S4: 跨架构验证覆盖合理。** 三个架构族覆盖 GQA (LLaMA)、GQA+sliding window (Mistral)、不同 d_ff (Qwen-14B)，7B-14B 范围。Mistral 有完整 3-seed 评估。

**S5: C1 target-swap 结论有说服力。** 3-seed 复现下 KL 与 C1 的 PPL gap ≤0.03pp（s123/s456 seed-matched oracle），有力证明 KL 的主要价值在于发现更好的 mask pattern。有直接实用意义。

---

## Weaknesses

### Critical

**W1: Contribution #2（signal type > coupling breadth）的数值基础可信度受限 [双方 AGREE on substance]**

论文第二个 contribution claim "the signal type gap (9.47 PPL) dominates the coupling breadth range (2.08 PPL)" 数值本身无逻辑矛盾（R2 误读 0.47 已被 R1 纠正），但两端均有 confound：

(a) **MSE baseline 未在公平条件下评估 [R1-N2, Must-Fix]**：MSE 使用与 KL 完全相同的超参数（lr=1e-3），但梯度 magnitude 约为 KL 的 5×，可能需更小学习率。2/3 seeds 在 50% 下崩溃。signal type gap 9.47 = 18.52(MSE) − 9.05(K=1 KL) 可能因 MSE 被高估而夸大。Limitations 已提及但 Contribution #2 仍使用未修正数值。

(b) **K=1 decomposition 存在 train-inference mismatch [R1 Should-Fix]**：K=1 训练时每步仅更新 1/32 层的 predictor，推理时 32 层同时激活。50% 下 K=1(34.85) 优于 K=4(44.23)，否定 "coupling breadth 单调有益"。论文已加 confound caveat。

**综合效应**：如果 MSE 在优化后 PPL 降至 ~12，signal type gap 缩至 ~3，不再 "dominate" coupling range (2.08)。Contribution #2 的定量结论可信度不足。

**W2: 知识任务退化的因果机制存在未解决的张力 [R1-W5, R2-W2, 双方 AGREE]**

KL predictor 在 MMLU（−5.2pp at 8B）和 GSM8K 上系统性退步。两个解释相互矛盾：
- **"KL mode-covering"**：forward KL 牺牲稀有但关键的推理激活
- **"Allocation-induced"**：remove-valley → MMLU +3.4pp，K=4 MMLU≈43.5 接近 dense baseline

如果调整 allocation 就能恢复知识能力，mode-covering 不是主因。论文未量化各自贡献。C4 control 仅 1 seed 且 s42 是异常值。

**W3: 高方差下游指标削弱 task-type split 贡献的统计可靠性 [双方 AGREE]**

PPL claims 稳健（σ=0.02），downstream claims 不稳健：MMLU 30% global σ=9.5pp, Qwen-14B GSM8K σ=5.3pp。Abstract 仍称 "systematic regression"——n=3 下 "systematic" 判断依据不充分。

### Warning

**W4: STE sparsity 不匹配可能高估 Gumbel 独立贡献 [R1-N1, Must-Fix]**

STE 在 30% target 下实际 sparsity 仅 20.8%（Table 4 footnote ‡），而 Gumbel 达到 ~28.5%。PPL 差距（15.77→11.79 at 50%）部分可能来自 sparsity level 差异而非 relaxation method 本身。需 matched-actual-sparsity 对比。R1 视为 Must-Fix；Director 考虑到 Table 4 footnote 已有披露且 STE 的 undershoot 本身说明 STE 机制有问题，定为 Warning。

**W5: 方法新颖性为组合级别 [R2-W1, R1 AGREE; 实质评估存分歧]**

MaskLLM 已使用 KL+Gumbel+frozen weights recipe，本文从 static N:M → contextual activation 的扩展应更充分论证新挑战。R1 认为子领域差异使直接对比不合理；R2 认为 static→contextual 缺乏形式化论证。论文贡献定位为 empirical characterization 而非 method novelty。

**W6: 可能遗漏并行工作 [R2-W3, R1 AGREE]**

SVD Contextual Sparsity Predictors（如在提交前发表且高度相关）应在 Related Work 中讨论。需验证该工作的发表时间和相关性。

**W7: Wall-clock speedup 缺失 [R1-N3 Must-Fix vs R2 Should-Fix]**

论文报告 6.4% latency overhead 但无稀疏核加速数据。R1 视为 Must-Fix（影响实际影响力）；R2 认为论文定位为 analysis paper，不应苛求。Director 采纳折中立场：论文已 framed 为 empirical study，但至少一个 sparse kernel 数据点会显著增强说服力。定为 Should-Fix。

**W8: 30% isocompute 对比不完整。** 50% 下有 BCE 2700-step 基准，30% 下无对应基准。

**W9: WikiText-2 与 WikiText-103 同源评估。** 社区标准做法。C4 OOD 部分缓解但仅 2-seed、无 TEAL baseline。

---

## Questions

**Q1**: 如果 MSE 用 lr=2e-4（5× 更小以匹配梯度 magnitude）重新训练，PPL 改善多少？signal type gap 是否仍 "dominates"？

**Q2**: remove-valley 和 K=4 都能大幅修复 MMLU，"KL mode-covering" 在退化中的真正占比是多少？

**Q3**: STE matched-actual-sparsity 下与 Gumbel 的 PPL 差距？

**Q4**: C4 control 的 s42 MMLU=40.6 vs 3-seed mean ~28.5——是否考虑过增加 seed？

**Q5**: SVD Contextual Sparsity Predictors 的发表时间和与本文的差异是什么？

---

## Missing References

R2-W3 提出 SVD Contextual Sparsity Predictors 可能为遗漏的并行工作，R1 同意。其他方面 Related Work 覆盖充分（TEAL, CATS, MaskLLM, PowerInfer, DejaVu, FastForward, R-Sparse, DIP, LaRoSA, SPON, ShadowLLM, D2D-MoE 等）。

---

## External Review

**状态**：pending（已请求 Stanford Agentic Reviewer，未返回）。

---

## Visual Layout Check（非评分项）

**状态**：error。视觉审查 Agent 因 rate limit 退出，无有效结果。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Contribution #2 数值可信度 | Must-Fix (N2: MSE) | ~~Must-Fix (N2: 误读)~~ → 实质同意 | AGREE on substance |
| STE sparsity 不匹配 | Must-Fix (N1) | 未独立提出 | R1 单方 |
| 知识退化机制 | Should-Fix (W5) | Should-Fix (W2) | AGREE |
| 统计可靠性 | — | — | AGREE |
| Wall-clock 缺失 | Must-Fix (N3) | Should-Fix | REBUT → Director: Should-Fix |
| MaskLLM 新颖性 | AGREE (R2-W1) | Should-Fix (W1) | AGREE |
| 并行工作遗漏 | AGREE (R2-W3) | Should-Fix (W3) | AGREE |
| PPL 改进 | 真实可靠 | 真实可靠 | AGREE |
| ~~Abstract 超长~~ | ~~REBUT (事实错误)~~ | ~~Must-Fix (N1)~~ | **剔除** |
| ~~数值矛盾~~ | ~~REBUT (误读 9.47→0.47)~~ | ~~Must-Fix (N2)~~ | **剔除** |

**R1 评分: 3.0 (Findings)** — 三个方法论 Must-Fix：STE sparsity 不匹配、MSE 超参不公平、无实际加速。PPL 改进真实，实验框架有价值。认为 R2 的两个 Must-Fix 基于事实错误，去掉后 R2 缺少 must-fix 支撑。

**R2 评分: 经修正后 ~3.0-3.5** — 两个 Must-Fix 因事实错误被剔除。有效 Should-Fix 意见：MaskLLM 新颖性（W1）、知识退化（W2）、并行工作（W3）、规模限制（W4）、Table 1 不完整（W5 部分有效）。没有 Must-Fix 支撑后评分实质上偏向 borderline。

**Director 评估: 3.0 (Findings)** — 论文的核心 PPL 发现真实可信（14.5%，3-seed，跨 3 架构一致），实验框架系统完整，C1 target-swap ablation 设计精巧，坦诚度高于平均水平。

制约总体评分的三个问题：

(1) **Contribution #2 数值基础受损**。signal type gap 9.47 的可信度受 MSE 未调参侵蚀（R1-N2）。如果 MSE 在适当 lr 下 PPL 降至 ~12，gap 缩至 ~3，"dominates" 的定量结论可能不成立。加上 K=1 confound，Contribution #2 的证据强度与 claim 强度不匹配。

(2) **知识退化机制张力未解决**。mode-covering 假设与 allocation 干预证据（remove-valley +3.4pp, K=4 MMLU≈43.5）矛盾。C4 control 单 seed 异常值。

(3) **R1 独立提出的 STE sparsity 不匹配**（N1）是有实质影响的方法论问题：如果 PPL 差距部分来自 sparsity level 差异而非 relaxation method，§3.3 的 "25.2% improvement" 被高估。Table 4 footnote 已披露但正文未调整 claim。

Contribution #1（KL > BCE for sparsity prediction）和 Contribution #3（C1 target-swap）是可靠的发现，足以支撑 Findings 级别。Contribution #2 和 #4 的证据不充分。

**综合判断：3.0 (Findings)**——有实质发现但整体 claim 体系与证据不完全匹配。

---

## Detailed Comments

### Must-Fix（影响接收决定）

1. **MSE lr sweep [R1-N2]**：至少对 MSE 做 2-3 点 lr sweep（如 lr=2e-4, 5e-4），确认 signal type gap 真实范围。如果 gap 显著缩窄，调整 Introduction Contribution #2 和 Conclusion 措辞。

2. **知识退化因果分离 [R1-W5, R2-W2]**：明确区分 "allocation-induced" 和 "loss-inherent" 两个假设并量化各自贡献。当前 remove-valley 修复 +3.4pp 说明 allocation 是重要因素，但主叙事强调 mode-covering。

3. **Downstream 统计措辞 [双方 AGREE]**：Abstract "systematic regression" → "directional regression (n=3)" 或类似限定。

### Should-Fix（改善论文质量）

4. **STE matched-actual-sparsity 对比 [R1-N1]**：验证 25.2%/33.8% PPL 改善中 sparsity level 差异的贡献。如果大部分差距来自 sparsity mismatch，正文应调整 claim。

5. **Wall-clock profiling [R1-N3]**：至少报告一个 sparse kernel 下的端到端推理速度，量化 6.4% overhead 是否被稀疏加速覆盖。

6. **并行工作 [R2-W3, R1 AGREE]**：确认 SVD Contextual Sparsity Predictors 的发表时间和相关性，如在提交前发表应在 Related Work 讨论。

7. **MaskLLM 新颖性论证 [R2-W1, R1 AGREE]**：更充分论证从 static N:M → contextual activation 的技术新挑战。

8. **30% isocompute baseline**：补充 BCE 2700-step 在 30% 下的结果。

9. **C4 control 增至 ≥2 seed**：s42 是 MMLU 异常值，单 seed 因果分析不可靠。

### Nice-to-Have

10. **C4 OOD 补充 TEAL baseline**。

11. **BCE+Gumbel 为何有害的讨论**：BCE+Gumbel(32.22) > BCE(27.97) 是梯度分析的天然实证佐证。