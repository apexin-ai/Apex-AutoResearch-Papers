---
round: 12
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-24T04:31:03.770601+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 13 (Fresh Review)

**论文**: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining"
**Venue**: EMNLP 2026 via ARR
**审稿模式**: Fresh（无历史轮次记忆）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+写作+格式）

---

## Summary

本文分析 detect-and-reweight 范式在 continued LM pretraining 中的有效性条件，通过 Qwen3-0.6B 的自污染实验（132M FineWeb tokens, ρ=0.4, 3 seeds）得出三个发现：(1) D&R 的 >95% PPL 优势来自 multi-epoch exposure 而非 filtering quality；(2) 有效 reweighting 需要 detector 同时具备足够 discrimination (AUC) 和 calibration (ECE)；(3) 最小干预（dual-constrained adaptive b*）优于无约束最大化。作为实用推论，提出一个无需 grid search 的 per-batch adaptive b* 方法，在 ρ≥0.4 时优于 uniform（Δ=-0.020, ρ=0.4; Δ=-0.032, ρ=0.6）。

---

## Strengths

**S1. Epoch confound 发现是论文最核心、最有价值的贡献。** [R1 AGREE, R2 AGREE]
Table 1 展示 D&R 的 0.396 PPL 优势在 epoch-matched 后缩至 Δ=0.017（3 seeds），揭示 >95% 的 reported advantage 源于数据重复而非 filtering quality。LR-controlled verification（D&R 17.651 vs shared-schedule 17.657, Δ=0.006）排除学习率混淆。Permuted-score control（+0.26 PPL）证明 detector signal 是 load-bearing。三重验证使这一发现高度可信，对后续 D&R 工作的实验设计有直接指导意义。

**S2. 实验设计结构良好，消融层次清晰。** [R1 AGREE, R2 AGREE]
六种方法（Adaptive < Uniform < ESS-only < Random + Grid oracle + D&R oracle）形成清晰的消融阶梯，每一层有明确控制变量。Ablation hierarchy 展示了 detector signal 和 minimum intervention 的各自贡献。

**S3. 结果报告异常坦诚。** [R1 AGREE, R2 AGREE]
论文主动报告：Bonferroni-Holm 校正后不显著的 p 值（p_BH=0.078/0.064）、downstream 零改善（Table 4: 0.5414 vs 0.5414）、ρ=0.2 failure case、checkpoint resume artifact（Appendix P）、cross-model mixed results（Appendix O）。这种透明度在 ML 论文中不常见，是良好的学术规范。

**S4. Related Work 全面且结构化。** [R1 AGREE, R2 AGREE]
§2 分五个 paragraph 覆盖 model collapse、detection、domain-level mixing、instance-level reweighting、theoretical foundations，引用 50+ 篇文献。与 Drayson et al. (2025) 的三点区分清晰公平。

**S5. Grid search 消除的实际价值。** [R1 AGREE, R2 AGREE]
Adaptive b* 的跨 seed 方差为 σ=0.007，远低于 grid-best 的 σ=0.033（4.7×）。Grid search 需 9 次完整训练（~16 GPU-hours at 0.6B），且 Figure 2 的 PPL plateau 使 validation-based selection 不可靠。

**S6. 理论 well-definedness 和实验规范。** [R1 AGREE, R2 AGREE]
Proposition 1-2（α_eff 单调递增、ESS 单调递减）确保 dual constraint 可解。Checkpoint resume artifact 的披露和 from-scratch 验证展示良好规范。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. [Critical] N=3 seeds 下所有核心结论均未达校正后统计显著性** [R1-N1 + R2-N1, 双方 AGREE]

论文最核心的定量 claim：
- ρ=0.4: uncorrected p=0.019, Bonferroni-Holm 校正后 p_BH=0.078（不显著）
- ρ=0.6: uncorrected p=0.010, p_BH=0.064（不显著）

BCa bootstrap CI [-0.028, -0.012] 在 N=3 下覆盖率存疑——Efron & Tibshirani (1993) 建议 N≥10-15。Cohen's d≈2.86 未报告，且 N=3 下 CI 极宽。Abstract 和 Conclusion 仍以断言性语言（"improves over uniform at ρ≥0.4"）呈现校正后不显著的结果。

对于以 "When does X work?" 为标题的 analysis paper，核心 claim 的统计支撑应当更强。

建议：增加至 N≥5 seeds，或在 Abstract/Conclusion 明确标注 "directionally consistent but not statistically significant after family-wise correction"。报告 Cohen's d 及其 CI。

**C2. [Critical] 仅在 self-contamination 设置下验证，生态效度堪忧** [R1-N2 + R2-N2, 双方 AGREE]

Generator 和 trainee 都是 Qwen3-0.6B，是最简单的检测场景——TF-IDF 可利用 128-token prefix 到 384-token continuation 的风格断裂点。所有三个 findings 建立在此设定上。唯一跨模型测试（Llama-3.2-3B, Appendix O）是 single seed、results mixed、缺 PPL 对比（"checkpoints were not retained for re-evaluation"）。

标题 "When Does Detect-and-Reweight Work?" 暗示一般性结论，但实验仅覆盖：一个模型家族、一种 contamination 设置、一个训练范式、一个数据量级。Table 3 的 practitioner decision summary（AUC≥0.9, ECE≤0.05）在 cross-model 场景下可能不适用。

建议：至少完成 cross-model 的完整 PPL 对比（3 seeds），或将标题限定为 self-contamination setting。

**C3. [Critical] 下游任务零改善，method 的实际价值存疑** [R1-N3 + R2-N3, 双方 AGREE]

Adaptive vs Uniform 的 downstream accuracy 完全相同（0.5414 vs 0.5414, 5 tasks, 3 seeds, Table 4）。论文将此归因于 Δ=-0.020 对应 ~0.1% relative improvement，低于 per-task measurement noise（σ≈0.01）。这个解释逻辑自洽，但恰恰证明方法在当前可测指标上无实际效果，与声称提供 "practical corollary" 存在矛盾。ρ=0.6 的 downstream results 缺失。

建议：报告 ρ=0.6 downstream results；或明确定位为 "analysis paper with negative practical result at current scales"。

### Should-Fix（影响评分但不一票否决）

**W1. [Warning] B=4 micro-batch 上 dual constraint 统计可靠性不足** [R1-W1, R2 AGREE]

B=4 下 true real fraction 仅取 {0, 0.25, 0.5, 0.75, 1.0}，α_eff 估计粒度极粗（Appendix K: MAE=0.114）。§5.3 展示 B=8→16 显著改善（Δ 从 -0.020 到 -0.068），反证 B=4 是次优设定。主实验在最 noisy 条件下运行，应说明选择 B=4 的 practical constraint。

**W2. [Warning] α_eff proxy 理论保证的 gap** [R1-W2, R2 AGREE]

α_eff 与 true batch-level real fraction 的 Pearson r=0.79（R²≈0.63），37% 方差未解释。Wang 2026 的 convergence theory 要求 true real fraction ≥ τ，但论文将此条件应用于 proxy α_eff，理论保证是否仍成立未讨论。ρ=0.2 下 α_eff 的 bias 方向和大小未报告。

**W3. [Warning] 3 个 detector 不足以建立 calibration 因果关系** [R1-W4, R2 AGREE（最强共识）]

TF-IDF+LR vs GPT-2 的对比同时在 AUC、模型类型、feature space、false positive pattern 上不同，不是控制实验。论文声称 "isolates calibration" 但 AUC 0.94 vs 0.91 并非严格 comparable。建议用同一 TF-IDF+LR detector + 不同 temperature scaling（T=0.204 calibrated vs T=1.0 uncalibrated）真正 isolate calibration effect。

**W4. [Warning] Epoch confound 分析缺少 uniform+multi-epoch baseline** [R1-W6, R2 AGREE]

当前比较：D&R full (~3.2 epochs) vs D&R epoch-matched (~1.0 epoch) vs Adaptive (~1.0 epoch)。缺少 "uniform + multi-epoch"（全数据重复训练 ~3.2 epochs 不做 filtering）。此 baseline 能区分 D&R 优势来自纯重复 vs filtering+repetition 交互。计算成本低，对分析完整性至关重要。

**W5. [Warning] "Minimum intervention" 原则缺乏理论依据** [R1-W5, R2 部分 REBUT]

Grid-best b≈0.3 而 adaptive b* 均值≈0.9——表面看 minimum intervention 反而 over-intervenes。R2 反驳：b* 均值是异质 batch 的平均（5.8% clean b*=0, ~50% α_eff-binding, ~44% ESS-binding），不能与固定 b 直接比较。但双方同意 median b / percentile-based b 对比有信息量——如果 fixed b=median(b*) 也能接近 adaptive 性能，per-batch adaptation 的独立价值需重新评估。

**W6. [Warning] 标题/claims scope 与实验支撑不匹配** [R2-W1, R1 AGREE]

标题暗示对 D&R 范式的全面分析，但实验仅覆盖一个模型家族、一种 contamination 设置、一个训练范式。建议标题加限定（如 "...in Self-Contaminated Continued LM Pretraining"）或在 Abstract 第一句明确 scope。

**W7. [Warning] Grid-best 与 adaptive b* 差距（0.054 PPL）来源未分析** [R2-W2, R1 AGREE]

Grid-best 17.620 显著优于 adaptive 17.674，差距是 adaptive vs uniform 改善（0.020）的 2.7 倍。论文论证 grid search 昂贵不可靠，但未分析差距来源（dual constraint 过于保守？α_eff proxy ceiling？）。

**W8. [Warning] 三个 findings 分析深度不均匀** [R2-W4, R1 AGREE]

F1（epoch confound）有三重验证，分析深入。F2（detector requirements）仅 3 个 detector 在 self-contamination 下的 observational comparison。F3（minimum intervention）主要依赖 ESS-only 退化（+0.043），缺乏机制分析。

**W9. [Warning] Batch-size scaling 趋势基于 3 个数据点** [R1-W3, R2 AGREE]

B ∈ {4, 8, 16} 三点拟合 Δ ∝ B^0.89，2-parameter model fitting 3 points 自由度接近零。指数不确定性未报告。R2 认为影响有限（次要观察），但外推可靠性确实为零。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下问题上独立达成强共识：

1. **N=3 统计效力不足** — 三轮审稿连续被独立指出，属结构性限制。p_BH=0.078/0.064 均不达传统显著性。BCa bootstrap CI 在 N=3 下覆盖率存疑。
2. **Self-contamination 生态效度** — Generator=trainee 是最简单检测场景。Cross-model test 不完整（single seed, no PPL, mixed results）。标题暗示一般性但实验不支持。
3. **Downstream 零改善** — 方法的 PPL 改善（0.11% relative）无法转化为任何可测量的下游效果。"Practical corollary" 的 framing 与实际结果矛盾。
4. **Detector 因果 claim 证据不足** — 3 个 detector 的 observational comparison 不能 isolate calibration effect。需控制实验。
5. **Epoch confound 是最强贡献** — 两位 Reviewer 一致认为 F1 是论文最核心、最有价值的发现。

## Reviewer Divergence [REBUT]

1. **评分差异**：R1=3.0 (Findings) vs R2=3.5 (Borderline Conference)。分歧在于 epoch confound finding 的独立价值是否足以支撑 Conference。R1 认为校正后不显著 + downstream 零改善使方法贡献不足；R2 认为 F1 的纠偏价值接近 main conference 门槛。
2. **α_eff 讨论位置**：R2 认为 §6 中 ~200 words 的 α_eff 讨论过长应移 Appendix；R1 认为核心讨论（r=0.79, bias 方向）应留主文，但可精简 quantitative decomposition。
3. **Minimum intervention 评价**：R1 认为 grid-best b=0.3 vs adaptive b*≈0.9 表明 over-intervention；R2 部分反驳（per-batch 均值不可与固定 b 直接比较），但同意 median b 对比有信息量。
4. **Adaptive b* 新颖性**：R2 评"中等（engineering contribution）"；R1 认为应更低——per-batch bisection 是标准方法直接应用。

---

## Questions

1. 能否用同一 TF-IDF+LR detector 改变 temperature scaling 参数（T=0.204 calibrated vs T=1.0 uncalibrated）isolate calibration effect？[R1-Q1, R2 AGREE]
2. ρ=0.6 下 downstream accuracy 是否有所改善？[R2-Q2, R1 AGREE]
3. 为什么不增加 seed 数量（N≥5）？132M tokens, 0.6B model 的训练成本不高。[R1-N1/R2-Q3]
4. 为什么不在 B=16 而非 B=4 上计算 b*？主实验是否在次优设定下运行？[R1-Q3, R2 AGREE]
5. Adaptive b* 的 per-batch b* 分布（median, percentiles）是什么？如果 median b* 也接近 0.9，minimum intervention 叙事需要修正。[R1-W5, R2 部分 AGREE]
6. 能否增加 "uniform + multi-epoch"（~3.2 epochs 无 filtering）baseline 以完善 epoch confound 分析？[R1-W6, R2 AGREE]

---

## Missing References

以下为两位 Reviewer 一致建议补充的参考文献：
- **RAID** (Dugan et al. 2024) 和 **M4** (Wang et al. 2024)：detection benchmarks，与 detector requirements 分析相关 [R2 提出, R1 AGREE]
- **Phi 系列** (Gunasekar et al. 2023, Li et al. 2023)：synthetic data 正面案例，为 D&R 必要性提供 counterpoint [R2 提出, R1 AGREE]
- **Owen 2013** (Monte Carlo Theory) 正文讨论 importance weighting failure modes（目前仅在 Appendix proof 引用）[R1 补充]

R1 对后训练阶段 contamination-aware 方法的遗漏 REBUT（scope 限定为 pretraining 合理）。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 external_review.paperreview_ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 3 warning, 11 info）。

主要发现：
- **[Warning] Pages 3-5 连续无 figure/table**：从 Page 2 的 Figure 1 到 Page 6 的 Table 1/Figure 2，约 3.5 页纯文本，视觉单调。建议将 Table 1 或 Figure 2 前移。
- **[Warning] Display items 分布不均**：主文 6 个 display items 全部集中在 Pages 6-8，前半部分仅有 Figure 1。
- **[Warning] Appendix 末页 ~85% 空白**：Appendix R (Use of AI Assistants) 仅占 ~15% 页面。建议并入前一页。
- **[Info] 正面评价**：Figure 2 清晰可读，Table 1-4 使用 booktabs 规范，Equation (1) 排版清晰，References 无 [?] 未解析引用，色彩方案色盲友好。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

### 评分维度

| 维度 | R1 | R2 | 合成 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 2.5/5 | 3/5 | 2.5/5 |
| Reproducibility | 4/5 | — | 4/5 |
| Overall | 3.0 | 3.5 | 3.0 |

### 综合判断

这是一篇分析质量高于方法贡献的 analysis paper。

**支撑 Findings 的理由**：
1. Epoch confound 发现（F1）对 D&R 文献有真实纠偏价值，独立于方法本身值得发表。
2. 实验设计结构良好，消融层次清晰，结果报告极为坦诚。
3. 论文格式完全合规，Related Work 全面。

**限制 Conference 的理由**：
1. 核心 claim 在 Bonferroni-Holm 校正后均不达传统显著性（p_BH=0.078/0.064），统计证据基础不稳固。
2. 仅在 self-contamination 设置下验证，生态效度不足以支撑标题暗示的一般性结论。
3. 方法的实际效果极小（Δ=-0.020 PPL, 0.11%），downstream 完全无改善——"practical corollary" 在当前规模下缺乏实际价值。
4. 三个 findings 的分析深度不均匀，F2 和 F3 的论证远不如 F1 充分。

**上调至 Conference (4.0) 的条件**：
- 增加 seeds 至 N≥5 使核心结果在校正后显著
- 提供至少一个 cross-model contamination 的完整实验（3 seeds + PPL + downstream）
- 用同一 detector 不同 calibration 程度的控制实验支撑 F2

### Detailed Comments

**§1 Introduction**: Narrative flow 良好，三个 research questions 清晰。Dual-constrained formulation 的动机清楚。Figure 1 可用更紧凑的形式呈现以节省空间。

**§2 Related Work**: 五段结构覆盖全面，与 Drayson et al. 的三点区分公平。可补充 detection benchmark (RAID, M4) 和 synthetic data 正面案例 (Phi 系列)。

**§3 Method**: 已压缩至 ~0.75 页，作为 analysis paper 的方法描述长度合理。Proposition 1-2 简洁正确。但 "minimum intervention" 的理论动机需加强——为什么 smallest b 是最优的？

**§4 Experimental Setup**: 训练细节充分。Self-contamination 的局限在文内已有预告（"limits ecological validity"）。Detector 选择逻辑（"first satisfying AUC ∈ [0.85, 0.98] and mid-range score ratio ≥ 5%"）可更详细说明。

**§5 Results**: Table 1 (epoch-matched) 和 Table 2 (main results) 是论文最强的部分。统计报告诚实（p_BH=0.078 写入正文）。建议补充 Cohen's d 及其 CI。§5.3 的 B^0.89 scaling 应降级为 monotonic trend 描述。

**§6 Discussion**: 自我批评充分（downstream null, effect size modest, α_eff proxy limitation）。第一段与 §5.1 内容重复，可精简。α_eff proxy 的核心讨论应保留在主文，但 quantitative decomposition 可移至 Appendix。

**§7 Conclusion**: 缺少 N=3/校正后不显著的 caveat，应与 Limitations 保持一致的审慎语气。

**Limitations**: 简短但覆盖了关键局限（self-contamination, N=3, detector coverage）。

**Appendix**: 18 个 section 组织合理，内容充实。建议合并部分高度技术性的 sections。