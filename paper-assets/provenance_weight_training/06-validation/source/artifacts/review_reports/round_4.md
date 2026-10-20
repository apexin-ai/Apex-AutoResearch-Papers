---
round: 4
review_mode: fresh
overall_score: weak accept (findings)
timestamp: 2026-05-19T07:26:11.575320+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 5 (Fresh Review)

**论文**: When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in LM Pretraining
**Venue**: EMNLP 2026 (ARR May 2025 cycle, Findings track)
**Reviewers**: R1 (方法/实验/统计), R2 (新颖性/完整性/写作/格式)
**审稿模式**: Fresh (重新审稿)

---

## Summary

论文研究 detect-and-reweight 方法中权重指数 b 的自适应选择问题。核心贡献：(1) 揭示 Detect-and-Remove 的 PPL 优势完全是 multi-epoch artifact（epoch-matched 后 Δ=0.006）；(2) 提出 dual-constrained adaptive b*（α_eff≥τ + ESS≥n_min），在 Qwen3-0.6B continued pretraining 上改善 uniform weighting（Δ=-0.043, p<0.003, N=3）；(3) 发现检测器信号类型（discriminative vs generative）比 AUC 更重要。方法在 ρ=0.2 失效，1.7B 上无改善。

---

## Strengths

**S1. [Consensus] Epoch confound 分析是最强贡献。** Table 2 + Figure 3 清晰展示 D&R 的 PPL 优势完全来自 multi-epoch exposure。控制 content epochs 后 D&R 与 adaptive 仅差 0.006 PPL。这一发现对领域有实际指导意义，实验设计（3 seeds，epoch-matched controls）严谨。

**S2. [Consensus] 诚实、全面的效果报告。** 论文不回避失败模式（ρ=0.2 失效、1.7B 无改善、downstream 4/5 略差）、报告 95% CI 包含 degradation、详细讨论 Limitations。这在提交论文中较为少见。

**S3. [Consensus] 消融设计合理且层次清晰。** Adaptive < Uniform < ESS-only < Random 的 hierarchy 分离了 detector signal 和 minimum intervention 两个因素。跨 ρ（0.4, 0.6）一致。Golden Ratio oracle 和 Grid-best post-hoc oracle 提供有意义的上下文。

**S4. [Consensus] 数学框架清晰完整。** Proposition 1（α_eff 单调性）和 Proposition 2（ESS 单调性）证明正确。Algorithm 1 伪代码完整。符号定义清晰。

**S5. [Consensus] 写作质量和格式合规。** 无 AI 写作痕迹（em-dash, 黑名单词），ACL template [review] 模式正确，double-blind 合规，Limitations section 和 Responsible NLP Checklist 完整。Related Work 覆盖五个维度，与 Drayson et al. (2025) 的差异表述清晰。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [Consensus, Critical] Effect size 极小且随规模递减，实用价值成疑。**
- 0.6B, ρ=0.4: Δ=-0.043 PPL (0.24% relative)；95% CI of adaptive-vs-grid gap [-0.039, 0.101] 包含 0.10 PPL 退化
- 0.6B, ρ=0.6: Δ=-0.028, 效果缩小
- 1.7B: Δ=-0.01, 仅 2 seeds, "no evidence of improvement or degradation"
- Downstream (Table 11): 5 tasks 中 4 个 adaptive 略差于 uniform
- 论文的 "eliminates grid search (9 runs to 1)" 卖点在 1.7B 无效的情况下价值有限
- **Action**: 重新 frame 为 empirical findings paper；1.7B 移入 main results table；讨论 0.043 PPL 在什么场景下 meaningful

**W2. [Consensus, Critical] PPL 改善可能是 tautological 的分布匹配，非真实质量提升。**
- Eval set = FineWeb human-only subset；adaptive reweighting 增大 human-authored text 的有效权重
- 在同分布 eval set 上的 PPL 改善是预期结果，不构成独立 quality evidence
- Discussion 自己承认 "PPL gain may reflect distribution matching"
- 4/5 downstream tasks negative 方向一致
- **Action**: 在 non-FineWeb eval set (Wikipedia, C4) 上评估 PPL；multi-seed downstream evaluation；如确认为分布匹配效应，在 Abstract/Conclusion 中明确

**W3. [Consensus, Critical] Self-contamination 实验设计严重限制外部效度。**
- Generator = trainee (Qwen3-0.6B)，最容易检测的污染形式
- Real web contamination: multi-source (GPT-4, Claude, Llama...), multi-style, domain-skewed
- Cross-model (Appendix G, Llama-3.2-3B): single-seed, 无 PPL, "checkpoints not retained" — 不可接受的实验管理疏忽
- **Action**: 至少 1 个 cross-model 完整实验（retained checkpoints + PPL）；或将 scope 限定为 "self-contamination continued pretraining"

**W4. [Consensus, Critical] N=3 统计可靠性不足。**
- Paired t-test with 2 df，无法验证正态性
- Per-seed gaps (0.044, 0.047, 0.040) CV≈8% 异常一致，可能是 B=4 下 seed 间差异系统性偏小
- 0.043 PPL 仅 0.24% relative improvement
- **Action**: 增至 5-8 seeds；或使用 permutation test / bootstrap CI；报告 Cohen's d；弱化 Abstract/Conclusion framing

**W5. [Consensus, Critical] B=4 micro-batch 使 dual-constraint 框架退化为离散查表。**
- α_eff ∈ {0, 0.25, 0.5, 0.75, 1.0}，bisection 在阶梯函数上搜索
- τ=0.8 时决策逻辑可用简单 if-else 表达，无需 bisection
- B∈{4,8,16} PPL 差异 <0.01 反而削弱 continuous formulation 的必要性
- Proposition 1/2 的 monotonicity proof 和 bisection algorithm 在 B=4 下 over-engineering
- **Action**: 在 B≥16 上展示 continuous 特性优于离散规则；或重新定位 contribution 为可移植到大 batch 的框架

**W6. [Consensus, Critical] 方法贡献增量有限，适合 Findings 而非 Main。**
- 核心公式 w=(1-q)^b 来自 Drayson et al. (2025)
- Dual constraint (α_eff + ESS) 是标准 IS 技术的直接应用
- Minimum intervention 是标准 constrained optimization
- 论文的真正价值在 empirical findings（epoch confound, detector type），而非 method innovation
- **Action**: 以 analysis-driven paper 重新定位：epoch confound + detector type findings 为主，adaptive b* 为 practical byproduct

### Should-Fix（影响评分但不一票否决）

**W7. [Consensus, Warning] τ 选择需要调参，"eliminates grid search" 过强。**
- τ=0.8 通过 single-seed 6-point sweep 选出
- ρ=0.4 最优 τ=0.8，ρ=0.6 最优 τ=0.7 — 非 universal default
- 从 9 次 b grid search 减到 1 次 run，但仍需 6 次 τ sweep
- **Action**: 弱化为 "reduces b grid search to a single τ default robust within [0.5, 0.8]"；3-seed τ sweep evidence

**W8. [Consensus, Warning] "Detector signal type > AUC" claim 证据不足。**
- 仅 3 detectors (1 discriminative, 2 generative), all seed 42
- Limitations 承认无法区分 type effect 和 calibration effect，但 Abstract/Conclusion claim 未相应弱化
- **Action**: 弱化 claim（"our results suggest..."）或增加 detector 种类

**W9. [Consensus, Warning] Table 11 caption "preserves downstream performance" 与数据矛盾。**
- 4/5 tasks 方向一致为 negative（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008）
- "preserves" implies neutral；实际数据 pattern 更接近 "slightly degrades"
- **Action**: 修改 caption；multi-seed downstream evaluation

**W10. [Consensus, Warning] Abstract 数据密度过高（~280 words），读起来像 Results 摘要而非叙事。**
- 具体数字过多（Δ=-0.043, p<0.003, AUC up to 0.91）
- **Action**: 裁减至 ≤250 words，核心 findings 用定性描述，数字移至正文

### Minor Issues

**M1.** "Content epochs" 概念在 Introduction / Table 2 使用但未正式定义
**M2.** GPU 类型仅在 Checklist C1，未出现在 Section 4 正文
**M3.** Grid results at ρ=0.6 (Table 14) 仅 seed 42，asterisk 标注不够醒目
**M4.** vehtari2024psis 年份（bib 标 2024，可能应为 JMLR published version year）需核实
**M5.** wang2026survive (arXiv:2602.16065) 存在性需验证
**M6.** Proposition 1 Cov≥0 by construction of r_i=1[q_i≤0.5]，应简化证明表述

---

## Reviewer Consensus

以下为两位 Reviewer 达成共识的关键判断：

| 问题 | R1 | R2 | 状态 |
|------|----|----|------|
| Effect size 过小 + 1.7B 无效 | [AGREE] | [AGREE] | 共识 |
| PPL 可能是分布匹配 | [AGREE] | [AGREE] | 共识 |
| Self-contamination 限制泛化 | [AGREE] | [AGREE] | 共识 |
| N=3 统计不足 | [AGREE] | [AGREE] | 共识 |
| B=4 使框架退化 | [AGREE] | [AGREE] | 共识 |
| 方法贡献 incremental (Findings-level) | [AGREE] | [AGREE] | 共识 |
| τ 需调参 | [AGREE] | [AGREE] | 共识 |
| Detector type claim 证据不足 | [AGREE] | [AGREE] | 共识 |
| Epoch confound 是最强贡献 | [AGREE] | [AGREE] | 共识 |
| 诚实的效果报告 | [AGREE] | [AGREE] | 共识 |

---

## Reviewer Divergence

仅有两处 minor 分歧：

**1. Epoch-matched LR schedule confound (R1-W5)**
- R1: 未控制混淆因素，需 schedule-matched 对比
- R2: [REBUT] 论文的保守性论证成立（较高 LR 有利于 D&R，因此 epoch-matched 结论是 conservative estimate）
- **评估**: R2 的反驳有道理——confound 方向有利于论文结论。但补充 schedule-matched 对比仍有价值作为 robustness check，不影响核心判断。

**2. Table 11 caption "preserves" 措辞 (R2-W6)**
- R2: "preserves" 与 4/5 negative 数据矛盾
- R1: [REBUT] 统计学意义上成立（|Δ| < SE），但同意方向一致性需多 seed resolve
- **评估**: R1 的反驳在技术上正确，但 R2 的实质关切有效——caption 应更精确。Minor 措辞问题，不影响评分。

---

## Questions to Authors

1. **B=4 的选择动机**：为什么不用更大 micro-batch 使 α_eff 的 continuous formulation 更有意义？如果是 GPU memory 限制，请在正文说明。
2. **Distribution matching hypothesis**: 在 non-FineWeb eval set 上 PPL 是否仍改善？这是区分真实质量提升和分布匹配的关键实验。
3. **τ transfer**: 在全新 model family + corpus 上，用户应用 τ=0.8 还是需要重新 sweep？
4. **1.7B 无效的原因**: 方法本身在大 scale 无效？还是仅 2 seeds 检测不到小效果？有计划补充 3+ seed 吗？
5. **Multi-source contamination**: 对 mixed generators (GPT-4 + Claude + Llama) 的 realistic web contamination，方法的预期表现如何？

---

## Missing References

无明显缺失。R2 确认 48 条引用覆盖 model collapse、detection、domain mixing、instance selection、theory 五个维度。References with Feng et al. (2025), Zibakhsh et al. (2025), Yi et al. (2025), Kang et al. (2025) 均已引用。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。项目配置中无 `external_review.paperreview_ai.enabled` 字段。

---

## Overall Assessment

**Score: Weak Accept (Findings) — 3.0/5**
**Confidence: 4/5**

**理由**：

论文是一篇扎实、诚实的 empirical study，有两个有价值的发现：

1. **Epoch confound**（最强贡献）：清晰揭示 D&R vs reweighting 比较中的 multi-epoch 混淆，对后续研究有指导意义
2. **Detector signal type**（有启发但证据薄弱）：discriminative vs generative 的区分有实践价值，但仅 3 detectors 不足以支撑 definitive claim

**核心问题**：
- 方法贡献增量有限（dual constraint 是标准 IS + constrained optimization 的直接应用）
- Effect size 极小（0.24% relative PPL），随规模递减（1.7B 无效），downstream 不支持
- PPL 改善可能仅为 tautological 分布匹配
- Self-contamination 设计限制外部效度
- N=3 统计证据薄弱
- B=4 使精巧的连续框架退化为离散查表

**适合 Findings track**：主要价值在 empirical findings 而非 method innovation。如果作者按以下方向修改，论文可以在 Findings track 获得更好的评价：
1. 以 empirical analysis paper 重新定位（epoch confound + detector type 为主，method 为辅）
2. 补充 non-FineWeb eval set 和 multi-seed downstream 以消除分布匹配疑虑
3. 至少 1 个 cross-model 完整实验（或显著缩小 scope claim）
4. 弱化统计 claim 并增加 seeds
5. 坦诚讨论 B=4 离散化和 continuous framework 的落差

---

## Detailed Comments (Per-Section)

**Abstract**: 偏数据密集（~280 words），应裁减至 ≤250 words。具体数字过多，保留定性 narrative。需明确 scope 为 continued pretraining。

**Introduction**: 故事线基本连贯，scope caveat ("does not address from-scratch pretraining at web scale") 已在第11行出现。但 contribution list 的 claim 强度与证据不匹配（"eliminates grid search" 过强，"competitive" 暗示等价性）。

**Method**: 数学严谨，Proposition 1/2 正确。但 B=4 discretization 应更早提及（当前在 Section 3.3 第二行才出现）。"Minimum intervention" 应标记为 design choice 而非 principle。

**Experiments**: 设置描述充分，6 种方法对比合理。Detector details（Appendix J）完整。GPU 类型应加入正文。

**Results**: 报告风格诚实。但 Grid-best post-hoc oracle 的优势应更充分讨论（在实际 validation-based selection 下 adaptive 的优势更大）。Table 11 caption 需修正。

**Discussion**: 5 段结构覆盖了 minimum intervention、failure modes、PPL-downstream divergence、soft vs hard filtering、τ deployment。内容合理但可进一步深入分布匹配假说。

**Conclusion**: 简洁，三个 findings 总结准确。但 "confirms generalization" (referring to 1.7B Δ=-0.01) 措辞过强。

**Limitations**: 覆盖 6 个维度（self-contamination, scale, contamination range, detector, threshold, evaluation），诚实且全面。

**Related Work**: 组织良好，5 个维度（model collapse, detection, domain mixing, instance selection, theory），与 Drayson 的 3-point differentiation 清晰。

**Appendix**: 内容丰富（proofs, grid details, τ sweep, regime decomposition, τ-ρ rank, hybrid comparison, downstream, ρ=0.6, α_eff validation, detector comparison, detector details, ρ=0.2, cross-model）。Appendix G cross-model 实验的 "checkpoints not retained" 是严重疏忽。

**Format**: ACL template [review] ✓, Anonymous ✓, Limitations ✓, Checklist ✓, 引用格式 ✓, 预估 7-8 页正文。