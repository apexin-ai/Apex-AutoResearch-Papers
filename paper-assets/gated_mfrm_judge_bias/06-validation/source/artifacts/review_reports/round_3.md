---
round: 3
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-23T06:35:13.302075+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：G-MFRM for Judge Bias and Contamination

**论文**：Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation
**目标 Venue**：EMNLP 2026 via ARR May 2026
**审稿模式**：Fresh（Round 3）
**Reviewer 编排**：2 人（R1 方法严谨性 / R2 新颖性与完整性）

---

## Summary

本文将 LLM-as-a-judge 评估中的 judge bias 和 benchmark contamination 之间的混淆形式化为遗漏变量偏差（OVB）问题，并提出 Gated Many-Facet Rasch Model（G-MFRM），通过引入乘性 gating term c_n · e_i 联合估计 model ability、judge severity 和 contamination susceptibility。方法采用三阶段估计流程（MFRM warm-start → 外部 exposure estimation → joint MCMC），配合形式化可辨识性分析（Propositions 1–2, Theorem 1）和 Murphy-Topel 方差校正。在 Arena-Hard 上以 8 个 target models 和 9 个 LLM judges 评估，G-MFRM 产生 τ = 0.857（vs baselines 0.786），但 bootstrap Δτ 95% CI 包含零，改善不显著。

---

## Strengths

1. **问题形式化出色**：将 judge bias 与 contamination 的混淆形式化为 OVB，从计量经济学引入清晰理论框架，在 LLM evaluation 文献中是新颖视角。Figure 1 的合成验证确认偏差的方向性和可预测性。[R1+R2 共识]

2. **可辨识性分析严谨且非平凡**：Propositions 1–2 给出必要条件（exposure 变异），Theorem 1 通过 Fisher information matrix + Schur complement 给出充分条件。特别是 Proposition 2（constant exposure → unidentifiable）为三阶段估计的必要性提供了理论基础。[R1+R2 共识]

3. **消融设计系统且有说服力**：Table 3 系统消融各组件——joint vs staged（θ-RMSE 2.0×）、continuous vs binary gating（c_n-RMSE +40%）、with/without d_j——清晰展示了每个设计决策的贡献。[R1+R2 共识]

4. **Claims 校准诚实**：Abstract 使用"nominally higher"，Section 4.2 报告 bootstrap CI 跨零，Limitations 承认样本量不足和 CI coverage 问题。P(Δτ > 0) = 0.927 的单侧信息也有参考价值。[R1+R2 共识]

5. **Generated regressors 问题的正式处理**：识别 Stage 2 → Stage 3 的 error propagation 并引入 Murphy-Topel correction，方法论规范。[R1+R2 共识]

6. **Judge severity profiles 有实用诊断价值**：Table 4 展示 proprietary judges 倾向严格（Claude Opus +0.60, GPT-5.5 +0.53）、open-source 倾向宽松（Mistral −0.74），severity range 达 1.34 logits，为 judge panel 设计提供实用参考。[R1+R2 共识]

---

## Weaknesses

### Critical（影响接收决定）

**C1. 主结果 Δτ 统计不显著 + 单一 benchmark + N=8 underpowered** [R1+R2 共识]

Arena-Hard 上 8 个 target models 的评估中，G-MFRM 的 Kendall τ = 0.857 vs 所有 7 个 baseline 的 τ = 0.786，bootstrap Δτ 95% CI = [−0.227, +0.722] 跨越零。所有 baseline 产生完全相同的排名，G-MFRM 的改善仅来自 positions 2–3 的一次 rank swap。论文自身 power analysis 表明需要 N ≥ 17 才能达到 80% power。

论文用 LOO cross-validation（ΔELPD_LOO = −60.0, SE = 9.4）作为替代证据，称之为"decisive evidence"——但 ΔELPD 衡量的是模型对观测评分的预测能力（model fit），而非排名准确性（ranking accuracy）。两者之间存在逻辑跳跃：一个 better-fitting model 并不必然产生 better rankings。

对于一篇标题为"Fair Scores"、声称提出"general framework"的方法论文章，仅在 1 个 benchmark、8 个模型上评估，且关键排名改善不显著，实证证据不足以支撑 main conference 的 generality claims。

**C2. Posterior CI coverage 仅 71%，不确定性量化失准** [R1 critical + R2 agree（介于 critical/warning）]

Empirical CI coverage 仅 71%（名义 95%），posterior credible intervals 系统性偏窄。Murphy-Topel correction（Appendix C）本应解决 generated regressors 引入的额外不确定性，但在 N = 8 的有限样本下校正不充分。论文将此归因于 HalfNormal prior 边界约束和 NUTS tree-depth 限制，但这些是作者自己的设计选择，不应成为 undercoverage 的免责理由。

Table 6 中基于 c_n 的 95% CI 做出的 contamination 诊断判断（如哪些模型"CIs exclude zero"）缺乏可信度。论文虽在 Section 6 将 CI 定位为"lower bounds on true uncertainty"，但实际使用者如何基于不可靠的 CI 做决策，未给出操作化建议。

R2 补充观察：论文后验预测检验（Figure 3）显示整体 model fit 良好（predicted 0.593 vs observed 0.599），coverage 问题集中于 c_n 参数——这部分缓解了对整体框架的担忧，但不改变 CI 不可靠的事实。

### Warning（影响评分但不一票否决）

**W1. 技术新颖性偏 incremental——OVB 教科书结果 + DG-IRT gating 组合** [R2 critical → R1 partial rebut → 分歧]

R2 认为：(1) Observation 1 是 Angrist & Pischke (2009) 教科书 OVB 公式在 MFRM 上的直接应用，作为首要 contribution 定位过高；(2) G-MFRM 的核心 gating 机制 c_n · e_i 直接来自 DG-IRT（Shu et al., 2013），三点差异（连续 exposure、judge severity facet、外部估计）是工程扩展。

R1 反驳：(1) 问题识别本身有价值——此前 LLM evaluation 文献将 bias 和 contamination 视为独立问题，OVB formalization 提供了统一视角；(2) 可辨识性分析（Propositions 1–2, Theorem 1）和 error propagation 框架（Murphy-Topel）是 DG-IRT 所没有的方法论贡献，非仅工程扩展。R1 建议重写 §3.1 末段，强调方法论 advancement 而非 feature list。

Director 判断：两方论点均有效。OVB 视角的 problem identification 价值和可辨识性分析的技术贡献是真实的，但论文当前的叙事确实未充分区分"应用已知工具"和"发展新方法"。建议将 OVB 讨论重新定位为 motivating observation，将 contribution 聚焦于可辨识性分析和联合估计框架。

**W2. Stage 2 exposure estimation 包含多个启发式选择，缺乏敏感性分析** [R1+R2 共识]

75%/25% anchoring/cross-model 权重、reference model 选择（gpt-4-0314）、clipping to [0,1] 策略均缺乏理论依据。论文声称"Spearman ρ ≥ 0.998 across all configurations tested"但无支撑数据（无对应 Table/Figure）。Reference model 本身若存在轻微 contamination，估计将如何偏移，未讨论。

**W3. Murphy-Topel 校正的有限样本性能未验证** [R1+R2 共识]

Murphy-Topel（1985）是渐近方法，N = 8 远低于适用范围。虽然每个 c_n 基于数百个 item-judge 观测（总 5,661），但 c_n 参数的有效自由度受限于 model 数量。未通过模拟验证 N = 8 时的 coverage，这可能是 C2 中 71% coverage 的直接原因。

**W4. σ_crit 阈值推导假设过强** [R1 + R2 agree with mitigation]

Eq. 6 的 attenuation factor λ(σ) 假设 exposure 估计误差为加性高斯、独立、同方差——实践中难以成立。R2 补充：Table 2 的经验验证提供了定性 robustness check（退化模式与理论预测大致吻合），但论文应明确讨论假设与实践的偏离。

**W5. OVB 线性近似（Observation 1）缺乏形式化误差界** [R1 critical → R2 rebut → 降级]

R1 原列为 critical：r = 0.86 意味约 26% 方差未解释，缺 Taylor 展开余项分析。R2 反驳：线性近似仅用于 Section 2 的 motivation，实际 G-MFRM 框架（Eq. 4）使用完整 ordinal logistic model，无下游推断依赖 Observation 1 的近似公式。

Director 采纳 R2 论证，降级为 warning：论文应增加一段讨论近似的适用范围和失效条件，但无需形式化误差界。

**W6. MCMC 收敛标准引用与实际不匹配** [R1+R2 共识]

使用 Vehtari et al. (2021) 的 rank-normalized split-R̂ 方法，但采用 R̂ < 1.05 的 Gelman (2013) 标准。引用与阈值不一致。实际影响可能较小（§4.2 报告 R̂ ≤ 1.03），但形式上应修正。

**W7. Bilinear rank-1 交互假设可能过于简化** [R2 + R1 agree]

c_n · e_i 的 rank-1 结构意味着所有模型的 contamination pattern 按标量 c_n 缩放。实际中不同模型的训练数据组成不同，contamination pattern 可能是异质的。放松为低秩矩阵分解会增加参数量并可能破坏 Theorem 1 的可辨识性条件。应在 Limitations 讨论。

**W8. N = 8 缺正式 power analysis** [R1+R2 共识]

论文在 Section 4.2 括号中提到 N ≥ 17 for 80% power，但无推导过程、无 effect size 假设、无独立 section。对于以统计方法论为核心的论文，power analysis 应更正式地呈现。

### Info（不影响接收）

- Section 6 (Conclusion) 溢出至第 9 页约 3-4 行，可能违反 ARR 8 页正文限制 [R2]
- 遗漏 3 篇相关引用：Polo et al. 2024 (tinyBenchmarks)、Ye et al. 2024 (Justice or Prejudice)、Panickssery et al. 2024 (self-preference bias) [R2]
- Table 2 exposure noise σ 取值粗糙（缺 0.1 和 0.3），难以判断 σ_crit ≈ 0.2 是否为转折点 [R1]
- Figure 1 使用彩虹色谱，对色觉障碍读者不友好 [Visual Check]

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：

1. **单一 benchmark + N=8 underpowered** → 实证证据不足以支撑 generality claims [C1]
2. **Δτ 不显著 + LOO 逻辑跳跃** → "fair scores" claim 缺乏直接证据 [C1]
3. **CI coverage 71%** → 不确定性量化失准 [C2]
4. **Stage 2 ad hoc 设计** → 缺 sensitivity analysis [W2]
5. **Murphy-Topel 有限样本** → 渐近方法在 N=8 下不充分 [W3]
6. **MCMC 收敛标准** → 引用与阈值不匹配 [W6]
7. **Power analysis 不足** → 需正式呈现 [W8]

---

## Reviewer Divergence

**分歧 1：OVB 线性近似的严重性**
- R1：Must-Fix（缺形式化误差界，r=0.86 不充分）
- R2：Should-Fix（线性近似仅用于 motivation，不影响下游估计）
- Director 采纳 R2 论证，降级为 W5

**分歧 2：技术新颖性评估**
- R2：Must-Fix（OVB 教科书结果 + DG-IRT gating = incremental）
- R1：Partial rebut（可辨识性分析和 error propagation 是真正的方法论贡献）
- Director 列为 W1，建议重新组织叙事突出方法论贡献

**分歧 3：Self-judging bias 建模**
- R2：Should-Fix（应在 G-MFRM 中显式建模）
- R1：Rebut（显式建模在 N=8 下导致过拟合，Appendix G 的 empirical robustness check 合理）
- Director 采纳 R1 论证，不列为独立 weakness

---

## Questions

1. G-MFRM 对 Stage 2 中 reference model 选择（gpt-4-0314）的敏感性如何？如果 reference model 本身有轻微 contamination，估计如何偏移？
2. Theorem 1 条件 (ii) 要求每个模型被至少两个不同 exposure 值的 item 观测——这在实践中如何验证？exposure 本身是估计量，若估计误差导致条件近似不满足，后果如何？
3. 仅 8 个 target models 时，估计 8 个 c_n 参数的有效自由度是多少？HalfNormal 先验的 shrinkage 是否足以缓解过拟合？
4. Rank-1 bilinear 假设被违反时（不同模型有不同 contamination pattern），G-MFRM 的估计如何退化？
5. 71% CI coverage 下，用户应如何解读 Table 6 中的 c_n 估计和 CI？是否有操作化的 decision threshold 建议？

---

## Missing References

1. **Polo et al. (2024)** "tinyBenchmarks: evaluating LLMs with fewer examples" — IRT 应用于 LLM 评估效率 [R2]
2. **Ye et al. (2024)** "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge" — LLM judge 多种偏差量化 [R2]
3. **Panickssery et al. (2024)** "LLM Evaluators Recognize and Favor Their Own Generations" — self-preference bias [R2]

---

## External Review

**状态**：未请求（项目配置未启用外部审稿）

---

## Visual Layout Check（非评分项）

视觉审查已完成（2 warning, 4 info），不影响评分：

- ⚠️ **Pages 1-3 无 display item**：首个视觉锚点延迟到 page 4（Figure 1+2），审稿人前 2 分钟全是文字+公式。建议将 Figure 2（方法概览图）前移至 page 2
- ⚠️ **Pages 5-6 连续无 display item**：Page 6 含实验设置（§4.1），可插入 summary table
- ℹ️ 正文 8 页仅 4 个 display items（2 figure + 2 table），对含实证贡献的论文偏少
- ℹ️ Figure 1 使用彩虹渐变色谱，对色觉障碍读者不够友好
- ℹ️ Table 1 作为主结果表，仅占左栏约 1/3 高度，视觉权重不够突出
- ℹ️ 附录 page 13 四个 figure 挤在单页，图内文字字号偏小

---

## Overall Assessment

**评分：3.0 (Findings)**
**置信度：4/5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3/5 | 3/5 | 3/5 |
| Reproducibility | 4/5 | 3.5/5 | 3.5/5 |
| Overall | 3.0 | 3.0 | **3.0** |

**核心判断**：G-MFRM 在理论层面有真实贡献——OVB formalization 提供了清晰动机，可辨识性分析（Propositions 1-2, Theorem 1）技术扎实，消融实验设计全面。但三个相互关联的统计缺陷共同构成核心短板：(1) N=8 单一 benchmark 下 Δτ 不显著，(2) posterior CI coverage 仅 71%，(3) Murphy-Topel 校正在有限样本下不充分。这三个问题指向同一核心担忧——**当前实验规模不足以可靠验证方法的有效性**。

论文的 claims 校准是诚实的（Abstract 即提 "nominally higher"，Limitations 全面），这在一定程度上缓解了上述担忧。方法框架本身有价值（contamination diagnostics、judge severity profiles），但作为 EMNLP main conference 投稿，实证证据的薄弱限制了影响力。

**推荐**：适合 Findings track 接收。若能在 rebuttal 中提供：(1) 额外 benchmark 或更大 model pool 的结果，(2) Murphy-Topel 在 N=8 下的 simulation coverage 验证，可考虑上调至 3.5 (Borderline Conference)。

---

## Detailed Comments（逐节意见）

### Abstract
- "nominally higher rank agreement (τ = 0.857 vs. 0.786; bootstrap Δτ CI includes zero at this sample size)" — 校准诚实，无需修改
- "though posterior CI coverage is 71% in synthetic validation" — 合适的 qualifier

### Section 1 (Introduction)
- Contributions list item 1："identify and characterize"措辞仍偏重于暗示新理论结果。建议改为"formalize the confounding as an OVB problem, motivating the gating mechanism"
- LOO cross-validation 结果的呈现方式需修正——明确区分 model fit evidence 和 ranking accuracy evidence

### Section 2 (Confounding in LLM Evaluation)
- Observation 1 的 linear approximation qualifier 已到位
- 建议增加一段讨论近似失效条件（高 contamination effect size 或极端 score 分布下）
- Appendix B 的 γ_n explicit form 是有价值的补充

### Section 3 (The G-MFRM Framework)
- §3.1 末段与 DG-IRT 的对比读起来像 feature list。建议重写，强调可辨识性挑战和 error propagation 框架是方法论层面的贡献
- §3.2 Stage 2 需提供 sensitivity analysis 的支撑数据
- §3.4 Error Propagation 应讨论 Gaussian/独立/同方差假设的局限性，并将 Table 2 定位为 robustness check

### Section 4 (Experiments)
- §4.1 MCMC 收敛标准引用需与实际阈值一致
- §4.2 "decisive evidence" → "strong evidence for improved model fit"
- Power analysis 需从括号注升级为完整讨论（至少在 Appendix）
- 建议增加 leave-one-model-out stability analysis

### Section 5 (Related Work)
- 补充 Polo et al. 2024、Ye et al. 2024、Panickssery et al. 2024

### Section 6 (Conclusion)
- 溢出至第 9 页，需压缩至 8 页以内

### Limitations
- 增加 rank-1 bilinear 假设局限性的讨论
- 增加对 CI 不可靠情况下的操作化建议