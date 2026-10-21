---
round: 6
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T23:08:42.998466+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 6 (Fresh Review)

**论文**: What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization
**Venue**: EMNLP 2026 via ARR (Long Paper)
**Reviewer 编排**: Reviewer 1（方法严谨性）+ Reviewer 2（新颖性/完整性）
**交叉分享**: 完成，共识度高（R2 AGREE R1 的 5/6 issues；R1 refined report after cross-sharing）

---

## Summary

本文将教育测量学中的 IRT person-fit 统计量（Snijders' ℓ_z*）应用于 LLM benchmark contamination 检测，提出 matched-difference 设计（Δℓ_z*）分离 contamination-specific aberrance。在三个 7–8B 模型家族（Qwen2.5-7B, Llama-3.1-8B, Mistral-7B）上，通过 QLoRA SFT 作为 contamination 代理，在 MMLU（14,042 items）和 ARC-Challenge（295 items）上识别出三个行为边界。研究定位为 characterization paper，核心贡献在于从 psychometrics 视角提供 contamination 行为的机制性理解。

---

## Strengths

**S1. 跨学科视角新颖且动机充分** [R1, R2 一致]
将教育测量学成熟的 person-fit statistics 引入 LLM contamination 检测是 genuinely novel 的跨领域移植。"First application" 声明在两位 Reviewer 搜索范围内成立。Figure 1 有效传达了 contaminated LLM ↔ test-taker with preknowledge 的核心类比。

**S2. Matched-difference design 设计优雅** [R1, R2 一致]
Δℓ_z* 通过差分消除 shared misfit，解决了 clean model 本身已有 high ℓ_z*（Qwen clean ℓ_z* = 7.05–9.53）的核心挑战。Appendix F.1 的 local dependence 模拟验证了设计在现实违反条件下的鲁棒性（d_ratio ≥ 0.93 for σ_τ ≤ 0.5）。

**S3. Detection-diagnosis tradeoff 的发现具有实际指导价值** [R1, R2 一致]
Table 3 诚实展示了 accuracy z-scores 在纯检测上的绝对优势（|d| 高出一个数量级），同时论证了 ℓ_z* 在诊断层面的独特价值（seen/unseen 分解、θ-shift 机制分析）。两阶段工作流建议（先筛后诊断）务实可行。

**S4. Epistemic 降级处理得当** [R1, R2 一致]
Finding 3 被标为 "exploratory"，Post-RL N=1 限制在 Appendix 并反复标注 "preliminary"。Limitations 覆盖了 SFT scope、model scale、single-run 等主要局限。

**S5. Appendix 体系完整** [R1]
Appendices A–K 覆盖 simulation validation、4PL vs 3PL、seed sensitivity、local dependence robustness、parameter perturbation、BCa check、classical IRT refit、reproducibility 等，回答了大量自然 follow-up 问题。

**S6. Fixed-θ vs. free-θ 系统对比有操作价值** [R2]
Table 2 提供了实用 guidance；Section 5 的 two-stage workflow 对从业者有直接参考价值。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1. [critical] Bootstrap CI 仅捕获 clean-seed variability，系统性低估总不确定性** [R1-N1, R2 AGREE]

Table 1 的 bootstrap resamples n=10 clean seeds，CI 完全忽略 contaminated run 的 seed-to-seed variability。Appendix K（Table 15）显示 Qwen 50% contamination 下三个独立 seed 的 free-θ |d| CV=59.6%（range 1.90–7.91）。Table 1 caption 声称 "All CIs exclude 0"，但纳入 contaminated variability 后该声明可能不成立。论文的核心量化推断（Contribution 2: "all bootstrap 95% CIs exclude zero"）建立在这些 anti-conservative CI 上。

**建议**: 将 Appendix K multi-seed data 纳入 main analysis，报告包含两种 variability 来源的 CI（prediction interval 或 nested bootstrap）；明确 Table 1 CI 含义为 "conditional on observed contaminated run"。

**MF-2. [critical] Cohen's d 实为 one-sample z-score，但被按 two-sample effect size 呈现** [R1-N4, consensus]

d = (ℓ_z*_contam − mean(ℓ_z*_clean)) / SD(ℓ_z*_clean)，contaminated condition 为单次观测（n_contam=1）。这本质上是 z-score 而非传统两组 Cohen's d，不能用 Cohen's d benchmarks（0.2/0.5/0.8）解释。Section 3.2 未给出数学定义。SD 基于 n=10（df=9），存在 ~9% positive bias，应报告 Hedges' g（J≈0.914 for df=9）。

**建议**: Section 3.2 明确给出数学公式；讨论 one-sample vs two-sample 区别；报告 Hedges' g。

**MF-3. [critical] Title/framing 三重 scope mismatch** [R2-N1, R2-N2, R1-N3, 完全共识]

(a) 标题 "Binary Response Patterns" 掩盖了对 PSN-IRT 外部 item bank 的关键依赖——没有 4PL parameters (a_i, b_i, c_i, d_i)，ℓ_z* 无法计算。
(b) "Benchmark contamination" 宽于实验覆盖的 SFT-stage QLoRA，pretraining/full FT/RLHF contamination 均未测试。
(c) "Systematic characterization" 与不完整实验矩阵矛盾（Mistral 缺 5%/25%，ARC-C 仅 Qwen，Post-RL N=1，全部 7-8B）。

**建议**: 标题包含 "IRT"（如 "What Can IRT Person-Fit Statistics Reveal..."）；Abstract 限定为 "SFT-stage contamination"；"systematic" → "controlled"/"initial"。

**MF-4. [critical] 实验条件 post-hoc 扩展引入确认偏差** [R1-N2, R2-W2, 共识]

Section 3.3 明确说 5%/25% 条件在观察到 non-monotonic dose-response 后才追加。Finding 3（inverted-U）的关键证据来自 post-hoc 数据点，p-values/CI 名义覆盖率不可靠。论文将 Finding 3 标为 "exploratory"，但 Abstract 仍将三个 findings 并列呈现，未区分 confirmatory vs exploratory。

**建议**: Abstract/Contributions 明确区分 confirmatory（15%/50% × 3 families）和 exploratory findings；对 post-hoc 条件考虑多重比较校正；Method section 透明报告实验时间线。

### Should-Fix（影响评分但不一票否决）

**SF-1. BCa vs percentile CI 选择性报告** [R1-W1, R2 强烈 AGREE]
Table 1 声称 "All CIs exclude 0"，但 BCa 校正后 Llama fixed-θ 50% CI = [−0.13, 2.21] 包含零。论文先称 BCa "confirms" percentile 保守性，又在 BCa 不利时选择性忽略。建议在 main text 标注并讨论 n=10 下方法选择依据。

**SF-2. Fixed-θ Qwen 15% 反直觉结果（0.7× ratio）解释不充分** [R1-W2, R2 AGREE]
"Snijders correction bias" 解释为 post-hoc 且未形式化——mismatch 临界阈值、bias 方向/大小均未量化。Δθ>0.2 经验阈值缺乏 simulation 支撑。

**SF-3. 缺少与 MIA/ConStat 的 head-to-head 实证对比** [R2-W3, 从 R5 延续]
Information requirements hierarchy 论述有帮助但不构成实证证据。至少应在一个条件下对比，或更充分解释无法对比的理由。

**SF-4. Findings 1&2 理论可预测性高** [R2-W1, R5-D1 延续]
θ-shift absorption 是 person-fit 文献已知现象（Snijders 2001, Meijer & Sijtsma 2001）；detection-diagnosis tradeoff 是 bias-variance 标准结果。应在正文坦诚讨论哪些 findings 理论可预测 vs 需要实证确认。

**SF-5. Finding 3（non-monotonic dose-response）证据不充分** [R2-W2, R1 认同]
仅 Qwen 表现清晰 inverted-U；Llama CIs 重叠，"directionally consistent but statistically non-significant"；Mistral 未完整测试。n=3 seeds 统计 power 有限。

**SF-6. 模型多样性不足 + QLoRA 外部效度** [R1-W3, R2-W4, 完全共识]
全部 7-8B，无不同规模模型。QLoRA low-rank 约束（rank=16）可能使 contamination signal 与 full FT/pretraining contamination 表现不同。论文未讨论 LoRA rank 对 person-fit pattern 的影响。

**SF-7. ARC-C ceiling effect 解释争议** [R1-W4, R2 部分 REBUT]
R1 认为 ceiling 解释不可证伪（替代假设：item 特性本身不利于检测）。R2 部分反驳：baseline 90.9% 是 ceiling 直接指标。共识：论文未充分检验 ceiling 预测，应报告 ARC-C item parameter 分布和 295 items 下的 statistical power。

**SF-8. Post-RL N=1 结构权重过高** [R1-W2, R2-W5, 完全共识]
Post-RL 仍在 Section 3.3 获得 paragraph-level 篇幅，Abstract 仍提及。建议从 Abstract 移除，Section 3.3 缩减至一句或移至 Discussion。

---

## Reviewer Consensus [AGREE]

1. **Framing 诚实度**：标题应反映 IRT/PSN-IRT 依赖；scope 应限定为 SFT-stage；"systematic" 应降级 [R1-N3 ≈ R2-N1/N2]
2. **CI 仅捕获 clean variability**：核心量化推断的基础不够稳固 [R1-N1, R2 AGREE]
3. **Cohen's d 标注错误**：应明确定义为 one-sample z-score 并报告 Hedges' g [R1-N4]
4. **Post-hoc 扩展**：5%/25% 条件为 confirmatory bias，应与 pre-planned findings 区分 [R1-N2 ≈ R2-W2]
5. **Post-RL N=1 权重过高**：从 Abstract 移除 [R1-W2 ≈ R2-W5]
6. **模型多样性不足**：仅 7-8B，无不同规模对比 [R1-W3 ≈ R2-W4]
7. **QLoRA 外部效度**：low-rank 约束对 person-fit pattern 的影响未讨论 [R1-W3 ≈ R2-Q4]

## Reviewer Divergence [REBUT]

1. **ARC-C ceiling effect 可证伪性**：R1 认为不可证伪（替代假设无法排除），R2 认为 baseline 90.9% 构成部分证据但论文检验不足。分歧程度轻微，不影响总评分。

---

## Questions（需要作者澄清）

Q1. Cohen's d 的精确数学公式？当 n_contam=1 时如何定义？[R1]
Q2. Bootstrap resampling 的具体对象——resample n=10 clean seeds 还是 items？coverage probability 是否有 Monte Carlo 验证？[R1]
Q3. Appendix K multi-seed 结果为何未纳入 main analysis？如果 50% 条件三个 seed 的 |d| 从 1.90 到 7.91，Table 1 的 single-seed |d| 代表性如何？[R1]
Q4. Fixed-θ 的 θ anchor 选择是否影响结论？mean θ 本身基于 n=10 的 estimation error 是否传播？[R1]
Q5. PSN-IRT item parameters 基于 ~13,000 leaderboard 模型——是否存在 circularity（contaminated models 已参与 calibration）？[R2]
Q6. n≥7,000 items for 80% power at 15% contamination——方法在多数 benchmark（<1,000 items）上是否实际不可用？[R2]
Q7. QLoRA vs full fine-tuning 选择原因？low-rank 约束是否 attenuate contamination signal？[R2]
Q8. ARC-C 为何仅覆盖 Qwen？计算预算还是设计选择？[R2]

---

## Missing References

1. **Hedges (1981)** — Cohen's d 小样本 bias correction（Hedges' g），与 n=10 设计直接相关 [R1, R2 AGREE]
2. **Efron (1987) / Efron & Tibshirani (1993)** — BCa bootstrap 小样本 coverage properties，known to be liberal when n<20 [R1, R2 AGREE]
3. **Xia & Zheng (2018)** — "Asymptotically Normally Distributed Person Fit Indices for Detecting Spuriously High Scores on Difficult Items" [R2]
4. **Wang et al. (2025)** — "On The Fragility of Benchmark Contamination Detection in Reasoning Models" (arXiv:2510.02386)——论文已引用但 R2 建议与 Post-RL extension 更深入关联 [R2]

注：Han et al. (2025) 已在论文中引用 (han2026quantifying)；Wang et al. (2025) 已在论文中引用 (wang2025fragility)。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置未开启 external_review）。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成（耗时约 3 分钟）
**结果**: 0 critical, 1 warning, 10 info

- **Warning**: Pages 3-4 连续两页纯文本（Related Work + Method §3.1-3.3），无 display item，建议将 Table 1 或方法示意图前移以改善视觉节奏。
- **Info**: Figure 2 heatmap 单元格数字字号偏小（约正文 50-60%），打印后可能不易辨读；灰色（未测试条件）与浅蓝色区分度一般。
- **Info**: 主体正文 8 页含 3 figures + 3 tables = 6 display items，密度适当。所有 float 在首次引用后 1-2 页内出现。无 LaTeX 渲染错误、margin 溢出或 section heading 孤悬。

---

## Overall Assessment

**Overall Score**: 3.5 / 5 — Borderline Conference
**Confidence**: 4 / 5

**两位 Reviewer 评分一致**: R1 = 3.5, R2 = 3.5

### 理由

**优势**: 论文提出了 genuinely novel 的跨学科视角，matched-difference design 巧妙解决了 LLM 系统性违反 IRT 假设的问题，detection-diagnosis tradeoff 的发现对 contamination 检测实践有指导意义。Appendix 体系完整，反映了严谨的实验态度。

**核心问题**: 统计推断存在结构性缺陷——CI 仅捕获 clean variability 而忽略 contaminated-run variability（Appendix K 数据表明后者在 50% contamination 下 CV=59.6%），Cohen's d 实为 one-sample z-score 但按 two-sample effect size 报告和解释。这两个问题不影响定性结论（contamination 确实改变 ℓ_z*），但影响定量推断的可信度——而 "all bootstrap 95% CIs exclude zero" 恰恰是论文的核心卖点。

Framing 三重 scope mismatch（标题掩盖 PSN-IRT 依赖、scope 宽于 SFT-stage、"systematic" overclaim）是 R5 轮次已提出但未充分解决的问题。Post-hoc 条件扩展的确认偏差风险、模型多样性不足、Findings 1&2 的理论可预测性进一步限制了贡献的独立价值。

**修改路径**: 如果 MF-1/MF-2（统计推断）和 MF-3（framing）能在 revision 中妥善处理——纳入 multi-seed variability 的 CI、正确标注效应量类型、调整标题和 scope claim——论文可达 Conference 水准（4.0）。当前版本建议 Borderline Conference / strong Findings。

---

## Detailed Comments（逐节）

### Abstract
- "n=10 independent seeds per condition" 应改为 "n=10 clean baseline seeds per model family" 以消除歧义
- "three behavior boundaries" 应区分 confirmatory vs exploratory
- Post-RL 提及应移除
- 应更突出 PSN-IRT 依赖为核心前提而非辅助条件

### Section 1 (Introduction)
- Contribution 1 "first systematic characterization" 中 "systematic" 应降级
- Contribution 3 可保留但应加 "in the LLM context"
- Post-RL 在 Introduction 末段的提及（"preliminary N=1 observation"）可保留但措辞应进一步弱化

### Section 3 (Method)
- §3.2 必须给出 Cohen's d 的数学定义，明确 n_contam=1 的含义
- §3.3 应透明报告实验时间线（哪些条件是 pre-planned，哪些是 post-hoc 追加）
- §3.3 Post-RL paragraph 应缩减或移至 Discussion

### Section 4 (Results)
- Table 1 caption 应标注 CI 仅反映 clean-seed variability
- Table 2 应讨论 Llama fixed-θ 50% BCa CI 包含零的情况
- §4.2 fixed-θ Qwen 15% 0.7× ratio 需要更充分的机制解释
- §4.4 应明确标注所有 5%/25% 数据为 post-hoc exploratory

### Section 5 (Discussion)
- "Characterization over tool" 定位清晰
- Information requirements hierarchy 有帮助但不替代实证对比
- 应讨论 Findings 1&2 的理论可预测性

### Limitations
- 覆盖范围适当
- 可补充引用 Appendix F.2 parameter sensitivity analysis
- 可增加对 Cohen's d 统计限制的讨论

### References
- 33 entries，覆盖合理
- 建议补充 Hedges (1981)、Efron (1987)