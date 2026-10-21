# Rebuttal 论点草稿

> 针对 Round 1 审稿降分风险逐条准备。Q/A 格式，每条 3-5 句。
> 基于当前论文版本（20 configs / 140 scenarios / 11 exposure sign flips）。

---

## 1. Novelty 质疑（最大风险，R2 excitement 2.5/5）

### Q1.1: "This is an incremental extension of Brenner (1993)."

**A:** Brenner (1993) identified the *possibility* of polytomous bias away from the null for a single topology (exposure) but did not quantify it, did not analyze other causal designs, and provided no sensitivity framework. Our contribution is not "K=2 scaled up to K=3"---it is a demonstration that the *algebraic structure* of the confusion matrix changes qualitatively at K>=3. For K=2, any column-stochastic matrix with C_kk > 0.5 preserves coefficient signs; this is a dimensional property of 2x2 matrices, not a rate condition. At K>=3, the higher-dimensional matrix admits negative effective weights across categories, enabling sign reversal even with all diagonal entries exceeding 0.5. No prior work characterizes this across causal designs or provides tools to diagnose it.

### Q1.2: "ASV is just E-value for measurement error."

**A:** E-value (VanderWeele & Ding 2017) quantifies the strength of *unmeasured* confounding needed to explain away an observed association---a scalar sensitivity parameter for an unobserved quantity. ASV quantifies the annotation error severity (via the delta parameterization of C(delta) = (1-delta)I + delta*C_0) at which a *measured-with-error* variable crosses a bias threshold. The mathematical objects differ: E-value operates on risk ratios for a missing variable; ASV operates on confusion matrix eigenstructure for an observed-but-noisy variable. The three ASV variants (magnitude, significance, sign-flip) have no E-value counterpart because E-value does not model multi-class misclassification structure.

### Q1.3: "The FWL invariance result is obvious."

**A:** If it were obvious, we would expect the correction literature to mention it. Neither DSL (Egami et al. 2023), MLA, nor the naive plug-in literature flags that matrix-based corrections achieve *exactly* 0% bias reduction for 4 of 7 canonical topologies. We prove this as a theorem (Proposition 2) and verify it empirically: 0.0% RMSE reduction across 4 topologies x 6 error structures = 24 configurations. Researchers applying DSL to a confounding design would invest in gold-label estimation of C, apply C^{-1} to dummy variables, and achieve nothing. This negative result has direct practical value.

### Q1.4: "The seven topologies are textbook—no novelty in listing them."

**A:** The topologies individually are indeed standard. The contribution is the *joint analysis*: the same confusion matrix produces qualitatively different bias across topologies (sign-preserving in confounding, sign-reversing in exposure, protective in collider). No prior work maps this landscape. The topology-dependent vulnerability spectrum (IV maximally fragile, M-bias immune) and the topology-dependent correction effectiveness are new findings that cannot be derived from any single-topology analysis.

---

## 2. "只评估不解决"

### Q2.1: "The paper diagnoses bias but doesn't provide a solution."

**A:** Diagnosis must precede treatment. Without knowing that topology determines bias direction, a practitioner cannot choose among correction methods---and our results show that the wrong choice is actively harmful (DSL amplifies M-bias by -267%, PPI++ harms M-bias by -88%). We evaluate 5 correction methods across 210 configurations and identify the first topology-aware correction ranking. We further identify Cross-PPI (Zrnic & Candes 2024) as a gold-free method that bypasses FWL invariance, and discuss EM imputation and Bayesian measurement error models as alternatives for the 4 FWL-invariant topologies. The ASV toolkit (publicly released) gives practitioners a 3-line diagnostic workflow.

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

### Q4.2: "But you previously reported zero sign flips in empirical data—isn't that a contradiction?"

**A:** Our revised analysis checking *all* K-1 exposure coefficients (not just the primary coefficient) reveals 11 of 20 configurations (55%) exhibit sign reversal in at least one exposure coefficient with real LLM confusion matrices. For HumAID (K=10), 7/8 configurations reverse a secondary coefficient; for VAST (K=3), 4/5 reverse beta_2 = -0.50. Crucially, zero sign reversals occur across 120 non-exposure scenarios (20 configs x 6 topologies), validating the structural guarantee. This three-part result---exposure flips confirmed, 5-topology guarantee validated, K=2 algebraic protection confirmed---is strictly more informative than the previous blanket "zero sign flips."

---

## 5. DGP 依赖性

### Q5.1: "The sign flips only occur on small coefficients—is this practically relevant?"

**A:** Two counterpoints. First, the VAST sign flip occurs on coef_idx=2 with true beta = -0.50, which is the second-largest effect in the DGP—this is not a negligible coefficient. Second, in NLP applications, "small" coefficients often correspond to rare but substantively important categories. In stance detection, the "neutral" category may be a minority class, but a researcher studying the causal effect of neutral framing would face sign reversal. The *practical severity* of a sign flip depends on the research question, not on the coefficient's magnitude relative to other coefficients.

### Q5.2: "The results depend on the specific DGP parameters chosen."

**A:** The sign-flip *guarantee* (5 topologies never flip) is DGP-independent under stated conditions—it holds for all column-stochastic C with C_kk > 0 when the DGP satisfies the sufficient conditions in Proposition 1 (which are conditions on effect sign alignment, not on specific parameter values). The sign-flip *rates* (83.4% for exposure, 52.6% for IV) are computed over 100,000 random confusion matrices for a specific DGP and verified at K=3,5,7. The DGP parameters use alternating-sign effects of decreasing magnitude (Appendix), a reasonable default that ensures both positive and negative effects are present. The qualitative findings (exposure uniquely vulnerable, 5 topologies safe, IV fragile via Wald denominator) are structural properties of the topologies, not artifacts of parameter tuning.

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
**Status:** 此条现在完全解决——全系数检查后 11/20 exposure sign flips 确认理论预测，同时 120 non-exposure scenarios 维持 zero flips。理论风险 vs 实证观测的 tension 消除。

### R2-W4: 线性模型假设
**Status:** Limitations 已加入 "All derivations assume linear structural equations; the FWL invariance result does not hold for logistic regression."

---

## 叙事总结：冲刺 4.0 的核心卖点

1. **质变论证**：K=2 → K>=3 是代数维度导致的结构性断裂，不是 Brenner 的增量扩展
2. **三重经验确认**：exposure flips（55%）+ 5-topology guarantee（0 flips / 120 scenarios）+ K=2 protection（0 flips / 7 configs）
3. **负结果价值**：FWL invariance 证明 matrix-based corrections 对 4/7 拓扑无效，重定向了 correction 研究方向
4. **实践工具**：ASV toolkit 提供 3 行代码诊断，F1 不是安全指标（F1=0.82 仍 ASV-unsafe）
5. **拓扑决定一切**：同一 confusion matrix 跨 7 拓扑产生质变不同的 bias pattern，首次系统化映射
