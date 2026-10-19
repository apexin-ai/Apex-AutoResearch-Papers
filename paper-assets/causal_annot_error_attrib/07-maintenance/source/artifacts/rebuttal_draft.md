# Rebuttal 论点草稿

> 针对 Round 1 审稿降分风险逐条准备。Q/A 格式，每条 3-5 句。
> 基于当前论文版本（23 configs / 161 scenarios / 14 exposure sign flips）。

---

## 1. Novelty 质疑（最大风险，R2 excitement 2.5/5）

### Q1.1: "This is an incremental extension of Brenner (1993)."

**A:** Brenner (1993) identified the *possibility* of polytomous bias away from the null for a single topology (exposure) but did not characterize sign-flip boundary conditions or analyze non-exposure topologies. Our contribution is not "K=2 scaled up to K=3"---it is a demonstration that the *algebraic structure* of the confusion matrix changes qualitatively at K>=3. For K=2, any column-stochastic matrix with C_kk > 0.5 preserves coefficient signs; this is a dimensional property of 2x2 matrices, not a rate condition. At K>=3, the higher-dimensional matrix admits negative effective weights across categories, enabling sign reversal even with all diagonal entries exceeding 0.5. Three results are entirely absent from prior work: (1) the 5-topology structural guarantee map, (2) the ASV sensitivity framework, (3) the FWL invariance negative result.

### Q1.2: "ASV is just E-value for measurement error."

**A:** The intuition is simple: E-value asks *how strong unmeasured confounding must be* to explain away an association; ASV asks *how bad annotation must be* to cross a bias threshold. But the mathematical objects are fundamentally different. E-value (VanderWeele & Ding 2017) operates on risk ratios for a *missing* variable---a scalar sensitivity parameter. ASV operates on confusion matrix eigenstructure for an *observed-but-noisy* variable via the delta parameterization C(delta) = (1-delta)I + delta*C_0. The three ASV variants (magnitude, significance, sign-flip) have no E-value counterpart because E-value does not model multi-class misclassification structure.

### Q1.3: "The FWL invariance result is obvious."

**A:** If it were obvious, we would expect the correction literature to mention it. Neither DSL (Egami et al. 2023), MLA, nor the naive plug-in literature flags that matrix-based corrections achieve *exactly* 0% bias reduction for 4 of 7 canonical topologies. We prove this as a theorem (Proposition 2) and verify it empirically: 0.0% RMSE reduction across 4 topologies x 6 error structures = 24 configurations. Researchers applying DSL to a confounding design would invest in gold-label estimation of C, apply C^{-1} to dummy variables, and achieve nothing. This negative result has direct practical value.

### Q1.4: "The seven topologies are textbook—no novelty in listing them."

**A:** The topologies individually are indeed standard. The contribution is the *joint analysis*: the same confusion matrix produces qualitatively different bias across topologies (sign-preserving in confounding, sign-reversing in exposure, protective in collider). No prior work maps this landscape. The topology-dependent vulnerability spectrum (IV maximally fragile, M-bias immune) and the topology-dependent correction effectiveness are new findings that cannot be derived from any single-topology analysis.

---

## 2. "只评估不解决"

### Q2.1: "The paper diagnoses bias but doesn't provide a solution."

**A:** Diagnosis must precede treatment. Without knowing that topology determines bias direction, a practitioner cannot choose among correction methods---and our results show that the wrong choice is actively harmful (DSL amplifies M-bias by -267%, PPI++ harms M-bias by -88%). We evaluate 5 correction methods across 210 configurations and identify the first topology-aware correction ranking. The practical workflow is: Step 1: ASV diagnoses topology-specific risk → Step 2: for FWL-invariant topologies (confounding, mediation, collider, M-bias), select Cross-PPI or EM imputation → Step 3: for non-invariant topologies, select optimal method per Table 5 (e.g., MC-SIMEX for IV, PPI++ for exposure). The ASV toolkit (publicly released) gives practitioners a 3-line diagnostic entry point.

### Q2.2: "Why not implement a new correction method?"

**A:** Our FWL invariance result proves that *any* correction reducing to C^{-1} applied to dummy-coded covariates achieves 0% bias reduction for 4 topologies. This means the solution space is constrained: effective corrections must operate on estimator outputs (like PPI++/Cross-PPI) or on latent variable imputation (EM, Bayesian), not on the confusion matrix directly. Establishing this constraint is itself a contribution---it redirects future correction research away from a provably futile approach. A novel correction method is valuable future work, but the diagnostic framework and the FWL impossibility result are prerequisites for designing one correctly.

---

## 3. 线性模型假设

### Q3.1: "All results assume linear SEMs. Logistic regression is more common in practice."

**A:** We acknowledge this limitation explicitly (Limitations section). However: (1) linear models remain the workhorse of causal inference in CSS---difference-in-means, OLS with controls, 2SLS are standard tools in the applied papers we cite (Egami et al. 2023, Lee et al. 2024, Baumann 2025); (2) the sign-flip guarantee/violation is an algebraic property of the confusion matrix and the exposure dummy coding, not of the outcome model---replacing epsilon ~ N(0,1) with a logistic link does not change the fundamental mechanism by which C maps true category probabilities to misclassified ones; (3) the FWL invariance result is specific to linear regression and we state this caveat. Nonlinear extensions are important future work but do not diminish the linear-model results.

### Q3.2: "The non-differential misclassification assumption is too strong."

**A:** Non-differential misclassification (P(A*|A,Y,Z) = P(A*|A)) holds when the LLM classifier has no access to the outcome Y at annotation time, which is the standard setup in CSS pipelines (annotate text, then estimate causal effects). We provide a stress test (Appendix) showing moderate robustness: epsilon=0.05 differential contamination increases violation rates by <3 percentage points. Fully differential misclassification is a distinct and harder problem that we identify as future work.

---

## 4. 83.4% sign reversal rate 不现实

### Q4.1: "The 83.4% headline is misleading—no real classifier is that bad."

**A:** We agree that Dirichlet(1,1,1) is a worst-case benchmark, not a practical operating point. This is why the paper *simultaneously* reports the realistic regime: at diagonal >= 0.7, violation rate drops to 13.7% with 2.1% sign reversal. The Dirichlet result establishes the *theoretical boundary*---the structural failure exists and is not a pathological edge case but the majority outcome under uniform priors. The practical rates show the residual risk under realistic classifiers. Both numbers are necessary: the first motivates the problem, the second calibrates it.

### Q4.2: "But you reported zero sign flips, then 61%—which is it?"

**A:** Both 83.4% and 61% measure any-coefficient sign reversal---they are directly comparable in *what* they check. The non-comparability comes from the CM distribution. The 83.4% uses random Dirichlet(1,1,1) CMs, which are severe enough to flip even the primary coefficient (beta_1 = 1.0, largest magnitude). The 61% uses real LLM CMs whose diagonal dominance protects the primary coefficient (0% flip across all 23 empirical configurations) but not secondary coefficients corresponding to rare categories with small |beta| (e.g., VAST beta_2 = -0.50 → +0.17). This reveals a previously undetected vulnerability: even practitioners whose primary coefficient is safe may draw wrong conclusions about secondary category effects. The 5-topology structural guarantee (0 flips across 138 non-exposure scenarios) and K=2 algebraic protection (0 flips across 7 configurations) are confirmed regardless.

---

## 5. DGP 依赖性

### Q5.1: "The sign flips only occur on small coefficients—is this practically relevant?"

**A:** Two counterpoints. First, the VAST sign flip occurs on coef_idx=2 with true beta = -0.50, which is the second-largest effect in the DGP---this is not a negligible coefficient. Second, in NLP applications, "small" coefficients often correspond to rare but substantively important categories. In stance detection, the "neutral" category may be a minority class, but a researcher studying the causal effect of neutral framing would face sign reversal. The *practical severity* of a sign flip depends on the research question, not on the coefficient's magnitude relative to other coefficients.

### Q5.2: "The results depend on the specific DGP parameters chosen."

**A:** The sign-flip *guarantee* (5 topologies never flip) is DGP-independent under stated conditions---it holds for all column-stochastic C with C_kk > 0 when the DGP satisfies the sufficient conditions in Proposition 1 (conditions on effect sign alignment, not on specific parameter values). When the true DGP is unknown, ASV provides a conservative assessment; the 5-topology guarantee holds regardless of DGP.

The alternating-sign parameter choice is not cherry-picking---it is a *necessary condition* for sign reversal to be possible. When all beta_k share the same sign, misclassification produces only attenuation (a direct consequence of the weight structure in Equation 2). The DGP must contain opposite-sign effects for sign reversal to occur, and alternating signs are the canonical way to ensure this. The qualitative findings (exposure uniquely vulnerable, 5 topologies safe, IV fragile via Wald denominator) are structural properties of the topologies, not artifacts of parameter tuning.

---

## 6. 额外准备：已修复的 R1 Issues

### R1-N1: Theorem 1 (Envelope Monotonicity) 缺解析证明
**Status:** Confounding case 已补解析证明（有理函数单调性）。其余 6 topologies 降级为 Conjecture 1（100,000 矩阵数值验证，零违反）。Collider/M-bias 方向修正为 non-increasing（保护性减弱）。

### R1-N2: Proposition 1 sign preservation 缺证明
**Status:** 已拆分为 Proposition 1（confounding/collider 已证，exposure 反例） + Empirical Finding（mediation/M-bias/front-door 数值验证）。显式充分条件已写入（sign(tau) = sign(tau_OV) 等）。

### R1-N3: ASV delta 定义域错误
**Status:** 已引入 delta_max = min_j 1/(1-(C_0)_{jj})。超出 delta_max 的 ASV 标为 infinity（实际强化结论：更多拓扑是"安全"的）。

### R2-N1: 83.4% headline framing 误导
**Status:** Abstract/Intro 现在同时报告 full prior (83.4%) 和 realistic regime (diagonal >= 0.7: 13.7% violation, 2.1% sign reversal)。

### R2-N2: "first systematic framework" 过度声明
**Status:** 已改为 "a systematic framework"。保留 "first to jointly characterize" 在有具体依据处。

### R2-N3: 4 篇关键引用缺失
**Status:** audinet2025, zrnic_candes2024, gligoric2025, keith_jensen_oconnor2020 已恢复。Cross-PPI 和 FWL bypass 讨论已加入 Correction Guidance 段落。

### R2-W2: zero sign reversals 与 sign reversal narrative 的 tension
**Status:** 完全解决——全系数检查后 14/23 exposure configs 有 secondary coefficient sign flips，同时 138 non-exposure scenarios 维持 zero flips + primary coefficient 0% flip。理论 vs 实证 tension 消除，替换为更精细的三层结果。

### R2-W4: 线性模型假设
**Status:** Limitations 已加入 "All derivations assume linear structural equations; the FWL invariance result does not hold for logistic regression."

---

## 叙事总结：冲刺 4.0 的核心卖点

三个 DGP-independent 贡献（核心叙事）：
1. **K>=3 打破 K=2 代数保护**：2x2 column-stochastic 矩阵的维度性质在高维消失，这是结构性断裂
2. **5-topology safe + 2-topology dangerous map**：首次跨 7 拓扑联合分析，产生不可从单拓扑推导的新发现
3. **FWL invariance negative result**：matrix-based corrections 对 4/7 拓扑证明无效，约束了 correction 研究方向

辅助 severity calibration：
- 83.4% / 52.6%: Dirichlet worst-case boundary
- 13.7% / 2.1%: realistic regime (diagonal >= 0.7)
- 61% empirical secondary-coefficient flips: 实证确认 exposure vulnerability 持续存在

实践价值：
- ASV toolkit 3 行代码诊断
- F1 不是安全指标（F1=0.82 仍 ASV-unsafe）
- Topology-aware correction workflow: diagnose → FWL check → method selection
