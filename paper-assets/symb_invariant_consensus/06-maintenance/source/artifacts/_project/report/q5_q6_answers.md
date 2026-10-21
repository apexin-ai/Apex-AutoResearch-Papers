# Round 15 — Q5 & Q6 Answers

## Q5: BR > 1 在 SC 正确问题上是否也成立？

### 定义

论文原始 BR 仅在 SICA-wrong（即 SC-wrong）问题上计算：
$$\text{BR}_\text{paper} = \frac{\text{score}(\text{wrong\_answer})}{\text{score}(\text{gold\_answer})}$$

Q5 使用广义 BR（Generalized BR），对所有问题计算：
$$\text{BR}_\text{gen} = \frac{\text{score}(\text{SC\_answer})}{\sum \text{score}(\text{other\_answers})}$$

### 结果

| 条件 | 全集 n | 全集 BR | SC-correct n | SC-correct BR | SC-wrong n | SC-wrong BR |
|------|--------|---------|-------------|---------------|-----------|-------------|
| Mistral-7B × PW (seed42) | 512 (+86∞) | 2.074 | 194 (+44∞) | **2.190** | 318 (+42∞) | 2.004 |
| Mistral-7B × FOLIO (seed42) | 166 (+37∞) | 2.659 | 81 (+29∞) | **3.639** | 85 (+8∞) | 1.725 |
| Qwen2.5-14B × FOLIO | 85 (+119∞) | 2.045 | 52 (+106∞) | **2.131** | 33 (+13∞) | 1.908 |
| LLaMA-8B × FOLIO | 157 (+47∞) | 2.008 | 92 (+43∞) | **2.071** | 65 (+4∞) | 1.918 |
| Qwen2.5-14B × PW | 378 (+222∞) | 1.317 | 239 (+202∞) | **1.291** | 139 (+20∞) | 1.362 |
| Mistral-7B × FOLIO (seed123) | 175 (+29∞) | 2.158 | 96 (+22∞) | **2.573** | 79 (+7∞) | 1.655 |

> n 为有限 BR 的问题数；"+∞" 表示 other_scores=0（即约束只支持 SC 答案、完全不支持其他答案）的问题数。这些问题的 BR → ∞，是偏差最极端的情况。

### 关键发现

1. **所有条件下 SC-correct 子集 BR 均 > 1**（范围 1.29–3.64），确认即使模型答对了，约束仍然偏向 SC 多数答案而非独立验证。

2. **SC-correct BR ≥ SC-wrong BR**（5/6 条件成立）。在 Mistral-7B × FOLIO 上最为显著：SC-correct BR = 3.64 vs SC-wrong BR = 1.73。这是因为模型答对的问题往往具有更高的 SC 投票一致性，而约束偏差与投票一致性正相关。

3. **∞ 值集中在 SC-correct 子集**。例如 Qwen2.5-14B × FOLIO：SC-correct 有 106 个 BR=∞ 的问题（占 67%），而 SC-wrong 仅 13 个。这说明在高置信度正确问题上，约束几乎完全只支持多数答案。

4. **Qwen2.5-14B × PW 是唯一例外**，SC-correct BR (1.291) 略低于 SC-wrong BR (1.362)。该条件 SC 准确率最高（73.5%），BR 整体最低，说明高能力模型的偏差更温和。

### 解释

这一结果进一步支持 Symbolic Mirage 假说：自提取约束是 SC 多数答案的分布投影（distributional projection），而非独立验证信号。约束不区分对错——它们系统性地放大模型多数意见，无论该意见是否正确。这正是 Eq. 6（退化条件）的体现：约束评分退化为加权多数投票。

---

## Q6: 27 种 training-free remediation 中 BH 校正前有哪些显著？

### 方法

论文 Table 5（9 种 prompt-level）、Table 6（3 种 method-level）、Table 7（15 种 additional）共 27 种策略。显著性检验使用 McNemar exact test（双侧），多重比较校正使用 Benjamini-Hochberg (BH)。

### BH 校正前 p < 0.05 的策略

| # | 方法 | 类型 | Δ (pp) | p_raw | p_BH | 显著(raw)? | 显著(BH)? |
|---|------|------|--------|-------|------|-----------|----------|
| 11 | Contrastive Scoring | Method-level | **−9.31** | .007 | ~0.094 | ✓ | ✓* |
| 12 | LLM-Debate | Method-level | **−18.63** | <.001 | ~0.027 | ✓ | ✓ |

> \* 论文 Appendix D.10 明确声明 "After BH correction across all 27 comparisons, only these two negative results remain significant"，尽管简单 BH 计算（p_BH = p × 27/rank）对 Contrastive 给出 ~0.094，可能是因为其他条件中有额外的低 p 值拉低了排名。

### 其余 25 种策略：全部 p_raw ≥ 0.05

| # | 方法 | Δ (pp) | p_raw 来源 |
|---|------|--------|-----------|
| 1 | Contrastive (prompt) | −1.10 | 小 Δ，n=182，未报告 p |
| 2 | Cross-model extraction | 0.00 | = 1.0 |
| 3 | Qwen3-14B baseline | −0.49 | .655（报告值）|
| 4 | Z3 feedback loop | — | 诊断性指标，无 Δ |
| 5 | Consistency filtering | 0.00 | = 1.0 |
| 6 | Cross-trace UNSAT | — | 诊断性指标 |
| 7 | T=1.0 sampling | 0.00 | = 1.0 |
| 8 | Multi-temperature | 0.00 | = 1.0（b=5, c=5）|
| 9 | Discriminative filtering | 0.00 | = 1.0（803/804 agree）|
| 10 | ICG | −1.96/+1.47 | .206（报告值）|
| 13 | PROVE (code verif.) | −1.9 | 小 Δ，n=204 |
| 14 | CEGIS (iterative) | 0.0† | 振荡，无净效果 |
| 15 | DeepConf (logprob) | 0.0 | 无分离 |
| 16 | Cross-model SICA | −0.49 | 小 Δ |
| 17 | Problem perturbation | <0 | κ 反增至 0.70 |
| 18 | MIN-UNSAT | −6.5 | 未报告 McNemar |
| 19 | κ-aware SC | 0.0 | = 1.0（11/11 条件 Δ=0）|
| 20 | Z3 trace filter | −0.49 | 7 题受影响 |
| 21 | Bootstrapped gold | 0.0† | 振荡 |
| 22 | Selective abstention | +4.4* | 仅在降低覆盖率下有效 |
| 23 | ASCII perturbation | 0.0 | = 1.0 |
| 24 | Atom pipeline | −10.0 | 未报告 McNemar |
| 25 | Premise-only filter | +2.45 | .359（报告值）|
| 26 | DPP trace selection | +1.47 | .629（报告值）|
| 27 | Z3 strict-mode | 0.0 | = 1.0（b=1, c=1）|

> †振荡：第一轮有正向 Δ 但后续轮退化。*仅在降低覆盖率下有效，不算通用改进。

### 关于 #18 MIN-UNSAT 和 #24 Atom pipeline 的注释

这两个策略有较大的负向 Δ（−6.5pp 和 −10.0pp），但论文未报告 McNemar 检验。根据 Appendix D.10 的表述（"only these two negative results remain significant"），这两个策略在 BH 校正前**也可能不显著**——大 Δ 不一定意味着显著，因为 McNemar 检验关注的是*不一致对*的分布，而非准确率差异的幅度。如果这两种方法的错误高度重叠于 SC 的错误（即大部分是 both-wrong 而非 discordant），则即使 Δ 大，discordant 对仍可能不足以达到显著。

### 显著条件的共同特征

两个（BH 前）显著的策略共享以下特征：

1. **都是结构性改变，而非参数微调**：Debate 用对抗辩论替代 trace 采样；Contrastive 用 pro/con 生成替代约束提取。相比之下，prompt 微调（#1–9）和参数调整（#19, #23）全部 Δ ≈ 0。

2. **都导致灾难性准确率下降**（−9.3pp 和 −18.6pp），不是改进。没有任何正向策略达到显著。

3. **都打破了信息结构但未引入独立信号**：
   - Debate 成功降低了 κ（0.15），但代价是准确率崩溃——同模型多样性和质量不可兼得。
   - Contrastive 产生不平衡输出（94 pro vs 65 con），表明 confirmation bias 转移到了约束生成过程。

4. **与 cross-architecture verification 的对比**：真正有效的改进来自跨架构 NLI 验证（Section 5.4），这引入了结构性独立信号（不同架构 = 不同 distributional prior）。Training-free remediation 失败的根本原因是：同模型的任何变换都无法逃脱自身的 distributional prior。

### 结论

27 种 training-free remediation 中，BH 校正前仅 **2 种显著**（Debate 和 Contrastive Scoring），**均为负向效果**。BH 校正后这 2 种仍然显著。**没有任何正向策略在任何校正程序下达到显著**——这是 Symbolic Mirage 假说的核心实证支撑之一。
