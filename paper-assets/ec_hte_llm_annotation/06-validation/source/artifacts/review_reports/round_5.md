---
round: 5
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T10:42:52.470125+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — ec_hte_llm_annotation (Round 8 Fresh Review)

**投稿**: EMNLP 2026 (ARR Long Paper) | **Deadline**: 2026-05-25 | **Reviewers**: 2 | **Rounds**: 1（共识已达成）

---

## Summary

This paper proves that correcting LLM annotation error with a pooled confusion matrix introduces subgroup-level CATE bias proportional to δ_s · Δτ / (1−2π̄) — an exact population identity (Theorem 1, R²=0.994 for K=2). The proposed EC-HTE method uses hierarchical Bayesian subgroup-stratified confusion matrix estimation, complemented by a Δτ-free diagnostic (Proposition 3, AUC=0.86). Experiments span 520 synthetic configurations (100 MC runs each), semi-synthetic TweetEval (N=5,000), and 7 LLMs across 2 NLP datasets. The theoretical contribution is clean and independently valuable, but the method's practical advantage is narrow — in the closest-to-real semi-synthetic setting, EC-HTE does not outperform global correction.

---

## Strengths

**S1. [consensus]** Theorem 1 provides an exact bias identity (not a bound), with clean algebraic proof and strong empirical verification (R²=0.994 for K=2, 0.974 for K=4). This result is independently valuable regardless of whether one adopts EC-HTE.

**S2. [consensus]** Proposition 3's Δτ-free diagnostic breaks the circular dependency between CATE estimation and correction-method selection, requiring only pilot-sample misclassification rates (AUC=0.86). Practical and independently deployable.

**S3. [consensus]** Experimental coverage is exceptionally systematic: 520 configurations × 100 MC runs spanning extreme/moderate heterogeneity, asymmetric misclassification, class imbalance, subgroup misspecification, multiplicative treatment effects, R-learner compatibility, and PPCI composition. Thoroughness rare in this intersection.

**S4. [consensus]** Intellectual honesty: the paper forthrightly reports settings where EC-HTE fails — semi-synthetic TweetEval (Global matches or beats EC-HTE), hate speech case study (inconclusive), semi-real confusion matrix experiment (EC-HTE inferior).

**S5. [consensus]** Clear articulation of relationships with PPI/DSL/PPCI (Section 2, Appendix U), and orthogonal composability with PPCI (Appendix L, Table 5).

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [critical, consensus].** Semi-synthetic TweetEval 中 EC-HTE 不优于 Global，但正文讨论不够突出。
- Table (Appendix K): K=4, n=250 下 Global |bias|=0.023 vs EC-HTE 0.027 (p=0.395); EC-HTE RMSE=0.225 ≈ 2× Global 0.124
- 这是离真实场景最近的实验，EC-HTE 在此完全无优势
- 正文 Section 5.3 仅一句话带过，应用**完整段落**分析 failure 原因（K=4 下 expert budget 不足、HB 方差膨胀），并明确给出 EC-HTE 优势成立的 Δπ 阈值或 budget 条件
- 贡献重心应更多放在 Theorem 1 和诊断指标上
- R1: critical (N1); R2: major, AGREE with direction

**MF2 [critical, consensus].** Plug-in 方差传播（Section 4.3, Eq.5）将混淆矩阵 Ĉ_s 视为已知常数，未传播其估计不确定性。
- CausalForest 场景下 coverage=0.91 < nominal 0.95（Table 1）
- Appendix bootstrap 验证仅覆盖 DIM estimator，CausalForest 场景完全缺失
- 需对 CausalForest 场景运行 bootstrap 或 full Bayesian coverage 验证
- 如果 coverage 系统性偏低，EC-HTE 的置信区间不可靠，影响方法的实际可用性
- R1: critical (N2); R2: AGREE critical

**MF3 [severity 分歧: R1 critical / R2 warning].** 所有 CATE 均为合成注入，无真实数据 + ground-truth CATE 的端到端验证。
- R1 观点：两个 real-data case study 均无正面结论，削弱了方法的实践说服力
- R2 rebut：这是 HTE 领域的结构性限制，非本文特有缺陷（Wager & Athey 2018, Künzel et al. 2019, Kennedy 2023 同样无此验证）。论文已通过 semi-synthetic + case study + semi-real confusion matrix 提供多层缓解
- 建议：在 Limitations 中更明确讨论此限制的普遍性；AC 裁定 severity

### Should-Fix

**SF1 [major, consensus].** 核心理论与测量误差文献的区分度不够清晰。
- Greenland (1980) 讨论 confounder misclassification 的 attenuation；Frazis & Loewenstein (2003) 给出 OLS + homogeneous misclassification 的偏差公式；Ogburn & VanderWeele (2012) 讨论 nondifferential misclassification
- Theorem 1 的新颖之处在于：(a) 针对 effect modifier 而非 regressor，(b) correction-induced bias（而非 misclassification 本身），(c) subgroup-heterogeneous δ_s×Δτ 乘积结构
- Appendix F 已有部分区分，但主文 Section 2 缺失。需在主文明确声明精确技术增量
- R2: major (W1); R1: AGREE

**SF2 [major, consensus].** EC-HTE 方法论新颖性有限——核心是 Dirichlet-Multinomial hierarchical model + CausalForestDML + delta method SE 的组合。
- 贡献定位在 problem-identification 和 new method 之间有张力
- Table 1 中 Strat. MLE vs HB EC-HTE 的 bias 增量仅 0.002 (0.012→0.010)
- 建议明确选择 problem-identification + diagnostic tool 为主轴，将 EC-HTE 定位为"自然修复方案"
- R2: major (W2, W5); R1: AGREE

**SF3 [major, consensus].** 假设 (A5) τ(z,s)=τ(z) 的限制性讨论不足。
- 主文仅 theory.tex L61 一句话
- Appendix W 提供了 K=2 下 A5 violation 的实验证据（coverage 0.94-0.96），但 K=4 + correlated Δτ_s/π_s 验证缺失
- 建议将 Appendix W 核心结论提升到主文 Section 3，讨论 K>2 时的行为
- R2: major (W3); R1: AGREE with nuance

**SF4 [warning, consensus].** Corollary 1 (multi-class extension) 证明不完整：h(j,j') 未推导，g(π̄) 仅给出均匀 off-diagonal 特殊情形。
- R1: warning (W1); R2: AGREE

**SF5 [warning, R1 raised, R2 agreed].** CV(π_s) 诊断对比不充分：Figure 3A 显示 CV(π_s) setting-level AUC=0.97 高于 Proposition 3 的 0.89，但论文未讨论为何不推荐 CV(π_s)。应阐明 trade-off（理论 grounding vs 经验表现）。

**SF6 [warning, consensus].** 合成 DGP 中 equal subgroup weights (w_s=1/K) 可能高估 EC-HTE 优势。Appendix T 覆盖 Z 类不平衡但非子群 S 大小不均。

**SF7 [warning, R1 raised, R2 partial rebut].** EC-HTE vs Stratified MLE 在高预算 (n=250) 下 bias 增量仅 0.002。建议补充 n_expert∈{25,50,100} 的低预算对比实验展示 HB shrinkage 的增量价值。R2 指出 Figure 4 已暗示低预算优势，但同意显式数据更有说服力。

**SF8 [minor, consensus].** 代码和数据可用性未提及。ARR reproducibility 维度要求。

**SF9 [minor, consensus].** Figure 2 信息密度可提高：colorbar 范围不同导致子图间难以对比，建议用 diverging colormap 或标出 crossover boundary / ratio=1.0 等值线。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键判断上完全一致：
1. **Theorem 1 + Proposition 3 是论文最大亮点**——精确 bias identity 独立可用，Δτ-free 诊断打破循环依赖
2. **Semi-synthetic 失败案例讨论不充分**——EC-HTE RMSE ≈ 2× Global 在最接近真实的实验中
3. **Plug-in SE 对 CausalForest 缺乏验证**——coverage=0.91 < 0.95, bootstrap 仅覆盖 DIM
4. **方法新颖性有限**——贡献重心应偏向 problem identification + diagnostic tool
5. **(A5) 主文讨论不足**——附录有证据但未提升到主文
6. **适合 Findings 接收，解决 MF1-MF2 + SF1-SF3 可达 Conference**

## Reviewer Divergence [REBUT]

**MF3: Ground-truth CATE 验证的 severity**
- R1: critical（无端到端真实验证削弱实践说服力）
- R2: warning（HTE 领域结构性限制，Wager & Athey 2018 等同类工作同样无此验证；论文已提供 semi-synthetic + case study + semi-real confusion matrix 多层缓解）
- 建议 AC 在 meta-review 中裁定

**交叉回应中的事实修正**：
- R2-Q5 误读 Table 1 数据：K=4 CausalForest EC-HTE RMSE=0.224（非 0.231），优于 Global 0.244。R2 将 Naive RMSE 误归为 EC-HTE。
- R2-MR1/MR2 中提出的 Grimmer (2022) 和 Chernozhukov (2018) 经 R1 核实已被引用（分别在 Appendix F L212 和 Section 2 L14）。

---

## Questions

**Q1.** Assumption (A5) 放松后在 K=4 + correlated Δτ_s/π_s 下的 coverage 表现？Appendix W 仅覆盖 K=2。

**Q2.** Algorithm 1 Step 2 fallback 到 C̄ 时，Step 3 的 SE 使用 C̄^{-1} 还是 Ĉ_s^{-1}？"半 stratified"状态的统计性质需澄清。

**Q3.** Table (Appendix L): EC-HTE vs Naive 在 TweetEval 上 p=0.030 且 Δ=+0.005，EC-HTE 显著劣于 Naive。与 Section 5.3 报告的 "p>0.05" 之间是否存在不一致？（Section 5.3 的 p 值可能是与 Global 的对比而非 Naive）

**Q4.** Singularity guard κ>100 在 520 configurations × 100 MC runs 中的触发频率？

**Q5.** 子群划分粒度（K 的选择）对 EC-HTE 性能的影响？是否有"最优 K"的选择策略？过细→expert label 不足，过粗→掩盖异质性。

---

## Missing References

1. **Greenland (1980). "The effect of misclassification in the presence of covariates." American Journal of Epidemiology.** — misclassification bias 经典参考，与 Theorem 1 的概念性先驱有关。[Both reviewers agree, should-cite]

2. **Wang, McCormick, and Leek (2020). "Methods for correcting inference based on outcomes predicted by machine learning." PNAS.** — ML-predicted outcome correction 的早期工作。[R2 提出, R1 agree with caveat, nice-to-have]

3. **Yadlowsky et al. (2024). CATE estimation calibration.** — 与 EC-HTE 的 calibrated CATE estimation 目标相关。[R1 提出, R2 agree, nice-to-have]

注：R2 提出的 Grimmer et al. (2022) 和 Chernozhukov et al. (2018) 经核实**已被引用**。

---

## External Review (Stanford Agentic Reviewer)

未启用（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 于 2026-05-22T10:20 启动，300 秒后超时未完成。无排版审查结果。用户可重新触发 `dispatch_visual_check` 获取视觉审查。

---

## Overall Assessment

**Overall: 3.5 — Borderline Conference（两位 Reviewer 一致）**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 4/5 | 4/5 | **4/5** |
| Excitement | 3.5/5 | 3/5 | **3.25/5** |
| Confidence | 4/5 | 4/5 | **4/5** |
| Reproducibility | 4/5 | — | **4/5** |

**推荐**：当前状态适合 **Findings** 接收（Overall 3.0-3.5）。若解决以下问题可达 **Conference (4.0)**：
1. [MF1] 正文充分讨论 semi-synthetic failure case + 给出 EC-HTE 适用条件的明确阈值
2. [MF2] CausalForest 场景的 bootstrap/Bayesian coverage 验证
3. [SF1] 主文明确与测量误差文献的技术区分
4. [SF2] 贡献重心调整为 problem-identification + diagnostic tool
5. [SF3] 主文加强 (A5) 松弛讨论 + K=4 验证

**一句话**：理论贡献（bias identity + diagnostic）干净正确且独立有价值，但方法的实际适用窗口较窄，最接近真实场景的实验中 EC-HTE 未展现优势——论文应更诚实地将自己定位为 problem-identification paper 而非 method paper。

---

## Detailed Comments

### Section 1 (Introduction)
- 贡献列表中 EC-HTE 方法的权重应降低，Theorem 1 和诊断工具应更突出
- 应在 Intro 中预告 EC-HTE 的适用条件（sufficient error heterogeneity + adequate expert budget）

### Section 2 (Related Work)
- 需补充与 Greenland (1980) 的明确区分——本文关注 correction-induced bias 而非 misclassification 本身的 attenuation
- Frazis & Loewenstein (2003) 的区分（Appendix F 已有）应提升到主文
- 补充 Wang et al. (2020) 和 Yadlowsky et al. (2024)

### Section 3 (Theory)
- (A5) 松弛时 Theorem 1 的退化行为需讨论（至少一段）
- Appendix W 的核心结论（K=2 下 A5 violation coverage 0.94-0.96）应在此提及

### Section 4 (Method)
- Algorithm 1 fallback 时的 SE 计算需澄清（C̄^{-1} vs Ĉ_s^{-1}）
- EC-HTE 定位调整为"自然修复方案"

### Section 5 (Experiments)
- Semi-synthetic TweetEval failure case 需完整段落分析（当前仅一句）
- 应分析 RMSE=0.225 vs 0.124 的 2× 差距原因（K=4 × 16 confusion matrix cells，expert budget 不足导致 HB overfit）
- CV(π_s) vs Proposition 3 诊断的 trade-off 应说明
- κ>100 触发频率应报告
- Table (Appendix L) EC-HTE vs Naive 的 p=0.030 结果需澄清与 Section 5.3 的关系

### Appendix
- Corollary 1: h(j,j') 推导和一般 g(π̄) 表达式需完整
- 补充 n_expert∈{25,50} 低预算 EC-HTE vs Strat MLE 对比
- CausalForest bootstrap coverage 验证

### Limitations
- 代码/数据可用性声明
- Ground-truth CATE 限制的普遍性讨论
- 子群划分粒度（K 选择）的实践指导

### Minor
- Table 1 旁建议直接报告 MC SE
- Figure 2 添加 ratio=1.0 等值线
- MCMC 4000 iterations 对 2×2 Dirichlet-Multinomial 可能过多，建议说明选择依据
- Limitations 中 "full Bayesian propagation is left to future work" 出现两次