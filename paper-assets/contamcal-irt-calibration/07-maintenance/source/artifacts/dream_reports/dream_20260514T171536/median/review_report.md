---
dream_id: dream_20260514T171536
tier: median
overall_score: weak reject
timestamp: 2026-05-14T19:55:57.950029+00:00
---

---
reviewer: R1 (Methods Soundness & Experimental Rigor)
overall_score: 3/6 (Weak Reject)
confidence: 4/5
---

# Review: ContamCal — Calibrating Benchmark Scores for Training Data Contamination via Contamination-Augmented IRT

## Summary

This paper proposes ContamCal, a two-stage framework that (1) aggregates four contamination detection signals via Reciprocal Rank Fusion into per-item exposure scores, and (2) fits a contamination-augmented 4PL IRT model with per-benchmark susceptibility parameters to produce calibrated benchmark scores with Bayesian credible intervals. The framework is validated on controlled LoRA SFT contamination injection across Qwen2.5 (0.5B--7B) and extended observationally to 72B and RL-trained models. The paper also provides a Fisher Information identifiability analysis establishing signal quality thresholds. While the problem is important and the approach principled, I find several methodological concerns regarding identifiability in the actual experimental regime, the gap between claimed and operational multi-signal fusion, and discrepancies between the measurement error model as presented versus as used.

---

## Strengths

**S1. Well-motivated problem framing with principled methodology.**
The pivot from contamination elimination (shown futile by Emperor's New Clothes, ICML 2025) to statistical calibration is well-argued. The analogy to causal inference—measuring and adjusting confounders rather than eliminating them—is apt. Grounding in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004) is genuine and correctly integrated. The three structural adaptations for LLM evaluation (shared item pool, continuous exposure, regime-conditional ability) are clearly articulated.

**S2. Min-K++ directional reversal is a genuinely novel and important empirical finding.**
The discovery that Min-K++ actively misleads rather than merely failing at high contamination dosages (Cohen's d from -1.98 at 0.5B to -2.85 at 7B) is the paper's most citation-worthy result. This challenges the implicit "graceful degradation" assumption in the detection literature and has immediate practical implications for any system relying on Min-K++ as a contamination indicator.

**S3. Rigorous simulation-based identifiability analysis.**
The 144-condition simulation sweep with Fisher Information derivation is the paper's strongest theoretical contribution. The distinction between structural identifiability (AUC >= 0.55) and practical identifiability (AUC >= 0.70) is actionable. The verification that I(gamma) analytic formulas match Monte Carlo estimates (ratio ~1.0) lends credibility. The 1/sqrt(N) scaling law for CI width (verified within 5% per transition) provides practical sample size planning guidance.

**S4. Controlled experimental design with ground-truth clean scores.**
The controlled SFT injection protocol—4 scales x 4 dosage levels x 2-3 seeds—provides genuine ground truth for calibration evaluation, which is fundamentally missing in observational studies. The multi-seed approach (target N >= 32 via cross-scale pooling) addresses statistical power concerns.

**S5. Comprehensive baseline comparisons.**
Seven baselines including DCR (EMNLP 2025), the most relevant predecessor, with five quantitative evaluation metrics. The inclusion of linear regression as a "sanity check" baseline is methodologically sound and reveals an important finding about the marginal benefit of IRT complexity.

**S6. Transparent limitation reporting.**
The paper honestly reports: (a) RRF degrades to S1-dominated mode at 0.5B, (b) GSM8K gamma is near zero (correct negative control), (c) coverage gap exists, (d) observational results have wide CIs. This is commendable and rare.

---

## Weaknesses

**W1 (Major). Fundamental tension between the Stan model specification and the paper's claims about measurement error modeling.**
The paper's Section 3.2 presents the measurement error (ME) model as a core methodological contribution (Eq. 3: tau ~ N(e, sigma_e^2)), arguing it propagates detection signal uncertainty into calibrated scores. However, the project's own internal decision log (D013) records that the analytic ME model was abandoned because it *worsened* gamma bias (59.2% relative bias vs. 57.5% for the simple model at N=30). The Stan code actually used for the reported results (`contam_irt_4pl_simple.stan`) treats observed exposure directly as a covariate with no measurement error modeling—it is standard explanatory IRT with a contamination covariate, not the noise-propagating framework described in the methods section.

This creates a reproducibility and honesty problem: a reader implementing the paper's equations would build the ME model, but the reported results come from the simple model. The paper must clarify which model produced which results. If the simple model produced the headline numbers, the ME model should be an ablation in the appendix, not a featured contribution.

*Severity: Major. Directly affects reproducibility and the credibility of the UQ claim.*

**W2 (Major). N_models in the actual experimental regime is far below the paper's own identifiability thresholds.**
The simulation analysis establishes that reliable gamma recovery requires N >= 50 models (exp-004: gamma bias +23.6% at N=50, +57.5% at N=30 with sigma_e=0.1). The actual experiment pools across scales and seeds to reach N ~ 32. At this sample size, the paper's own diagnostics show gamma is in the "bias-sensitive zone" where posterior estimates are substantially prior-driven.

Specific evidence from the project:
- GSM8K at 0.5B with N=4: Rhat=1.53, ESS=7 (catastrophic non-convergence before cross-scale pooling fix)
- After fix with delta-exposure and cross-scale pooling: Rhat_max=1.007, ESS_min=520—convergence is acceptable, but low N still means large gamma bias

The reported MAE=2.1pp is a point estimate from a regime where the paper's own simulations predict significant positive bias in gamma. The SBC diagnostic (p=0.23) partially addresses this, but SBC at the actual N should be the primary validation, not a supplementary check.

*Severity: Major. The paper's own identifiability analysis contradicts the sample size used for the primary claims.*

**W3 (Major). "Multi-signal framework" is operationally a single-signal method.**
Actual signal AUC data from exp-008 at 0.5B: S1=0.953 (d005 MMLU), S2=0.466, S4=0.517. At 0.5B, only S1 (embedding retrieval) has discriminative power. The paper claims scale-dependent signal effectiveness with S2/S4 crossing practical thresholds at 1.5B (AUC >= 0.70) and consolidating at 3B (AUC >= 0.77). However, the review_context.yaml imagined experiments show S2 at 1.5B MMLU = 0.502 and at 3B = 0.538—still at chance level. The "scale-dependent" narrative in the paper summary (S2 AUC >= 0.72 at >= 1.5B) appears to be aspirational rather than empirically verified at the time of writing.

RRF aggregation at 0.5B: RRF-4 AUC = 0.947 versus S1-only AUC = 0.975 (Tables 4-5). Adding three random signals *degrades* performance. At 1.5B, the claimed +1.5pp improvement over S1-only depends on S2/S4 having non-trivial discriminative power, which the available data does not confirm.

The paper should either: (a) present verified multi-scale signal data showing S2/S4 crossing the practical threshold, or (b) honestly reframe as an embedding-signal + IRT calibration method with multi-signal extensibility as future work.

*Severity: Major. Core claim C2 depends on unverified scale-dependent signal effectiveness.*

**W4 (Major). Per-benchmark gamma_k via separate fits, not a proper hierarchical model.**
The paper presents per-benchmark gamma_k as revealing contamination susceptibility heterogeneity across benchmarks (Table 7: MMLU=0.28, ARC=0.38, GSM8K=0.06). However, these are obtained by fitting completely independent IRT models per benchmark, then comparing point estimates across models. This approach:

(a) Cannot formally test whether gamma values differ significantly across benchmarks (no joint posterior over the gamma vector).
(b) Cannot share information across benchmarks to improve estimation in the low-N regime.
(c) The gamma_k specification ablation (Table 9) compares per-benchmark separate fits vs. a pooled global gamma, but does not include the natural middle ground: a hierarchical model gamma_k ~ Normal(mu_gamma, sigma_gamma) that would permit both heterogeneity testing and information sharing.

The 0.7pp gap between per-benchmark (2.1pp) and oracle gamma (Table 9) suggests the per-benchmark specification is reasonable, but the lack of a proper hierarchical comparison is a methodological gap.

*Severity: Major for the heterogeneity claim; moderate for the overall framework.*

**W5 (Moderate). Coverage gap (92% vs 95% nominal) without definitive diagnosis.**
The reported 92% coverage at 95% nominal is better than the median dream's 85%, but still represents systematic overconfidence. The paper attributes this to local independence violation (single model responds to all items) and potentially insufficient N. SBC diagnostics (p=0.23) suggest the model is not grossly miscalibrated, but SBC tests the prior-likelihood interaction, not the local independence assumption specifically.

A more informative diagnostic would be: (a) posterior predictive checks on item-level residual correlations, (b) simulation with correlated item responses matching the empirical correlation structure, (c) comparison of coverage at different N values to distinguish finite-sample from structural sources. Without this, the reader cannot assess whether the coverage gap is fixable or fundamental.

*Severity: Moderate. 92% is reasonable but the UQ claim is the paper's distinctive contribution and deserves definitive diagnosis.*

**W6 (Moderate). SFT contamination injection introduces confounds absent from real contamination.**
Several documented confounds complicate interpretation:

(a) **Ability regression at 0.5B**: d100 contamination SFT reduces MMLU from 39.8% to 23.2%—the model gets *worse*, not better. This is the opposite of real contamination's effect. The IRT model estimates theta degradation, but the paper's contamination story assumes gamma > 0 (inflation). At 0.5B, the framework is calibrating for ability destruction, not contamination inflation.

(b) **3B GSM8K catastrophic forgetting**: LoRA SFT causes GSM8K to drop from 60.5% to 11.7% (D018). This is excluded from analysis, but indicates the SFT protocol is overly destructive at some scales.

(c) **Position bias at d005**: D019 documents that d005 SFT pushes "select A" from 40% to 55%, introducing a systematic position bias confound separate from contamination memorization.

(d) **Low paraphrase QC**: GSM8K paraphrase QC pass rate is 17.3% (D012). The d100 condition trains on largely low-quality paraphrases, creating a "noisy contamination" confound.

These confounds do not invalidate the approach but substantially weaken the ecological validity claim. The paper should more prominently discuss that LoRA SFT contamination injection is a controlled proxy with known artifacts, and the distance to real pretraining contamination remains unknown.

*Severity: Moderate. The controlled setup is a strength for internal validity but the confounds limit generalizability claims.*

**W7 (Moderate). Marginal advantage over linear regression baseline.**
The paper reports ContamCal MAE=2.1pp vs. linear regression baseline. The median dream estimated this gap at 4.3pp vs 4.8pp with overlapping CIs. Even with the more favorable numbers in the paper summary (2.1pp vs implied larger baselines), the comparison that matters most is against the simplest reasonable baseline: linear regression of scores on exposure.

If the full 4PL+gamma IRT machinery with NUTS inference (hours of computation) provides only ~1-2pp improvement over an OLS regression (seconds of computation), the practical case for ContamCal's complexity is weak. The paper should explicitly compute and report the paired difference with bootstrap CIs between ContamCal and linear regression.

*Severity: Moderate. Does not invalidate the framework but raises cost-benefit questions.*

**W8 (Minor). Prior specification for gamma differs between paper and Stan code.**
The paper states gamma ~ HalfNormal(0, 1) (constraining gamma >= 0, appropriate if contamination can only inflate scores). The Stan code uses gamma ~ std_normal() (unconstrained, allowing negative gamma). For the 0.5B case where contamination *decreases* performance, the unconstrained prior is actually more appropriate, but the inconsistency between paper and code should be resolved. The paper_framing.md also lists gamma ~ HalfNormal(0, 1), while the actual Stan model uses N(0, 1).

*Severity: Minor but affects reproducibility.*

**W9 (Minor). Prior on c and d differs between paper text and Stan code.**
Paper Eq. 6: c ~ Beta(2, 8), d ~ Beta(8, 2). Stan code: c ~ Beta(5, 20), d ~ Beta(20, 5). The Beta(5, 20) prior centers c at 0.2 with tighter concentration than Beta(2, 8) which centers at 0.2 but with more variance. This is a minor inconsistency but should be reconciled for reproducibility.

*Severity: Minor.*

**W10 (Minor). Cross-family validation (Table 14, r=0.91) is encouraging but limited.**
Llama-3.2-1B provides a single additional model family at a single scale. The r=0.91 correlation of gamma_k between Qwen and Llama is a positive signal, but with only 3 benchmarks contributing data points, the correlation is estimated from very few observations. A permutation test or bootstrap CI on this correlation would strengthen the claim.

*Severity: Minor. The result is directionally positive.*

---

## Questions for Authors

1. **ME model clarification**: Which model produced the results in Table 6—the measurement error model of Eq. 3 or the simple model that uses observed exposure directly? If the simple model, please revise the methods section to make this the primary specification and the ME model an ablation.

2. **Gamma bias at N=32**: Your simulation analysis (exp-005) shows +23.6% positive gamma bias at N=50, sigma_e=0.1. What is the expected bias at N=32 (your actual pooled sample size)? Does this bias inflate or deflate the reported MAE?

3. **S2/S4 at 1.5B/3B**: The paper claims S2 AUC >= 0.72 at >= 1.5B. Can you provide the actual empirical AUC values from your signal pipeline at these scales? The available 0.5B data shows S2 AUC = 0.466.

4. **Ability regression at 0.5B**: With d100 MMLU dropping from 39.8% to 23.2%, ContamCal is effectively estimating ability *destruction* from SFT, not contamination *inflation*. How does gamma's interpretation change in this regime? Is a positive gamma still meaningful when the net effect is performance degradation?

5. **Hierarchical gamma_k**: Have you fit a hierarchical model gamma_k ~ Normal(mu_gamma, sigma_gamma) to formally test benchmark heterogeneity? The 2.3pp MAE for hierarchical in Table 9 suggests you have—please clarify the specification.

6. **Coverage diagnosis**: Can you provide posterior predictive checks showing the empirical item-level residual correlation structure? Is the 92% coverage stable across benchmarks, or is it driven by one benchmark's miscalibration?

7. **Computational cost comparison**: What is the wall-clock time for ContamCal (signal computation + NUTS inference) versus linear regression, and does the MAE improvement justify the computational overhead?

---

## Missing Experiments or Analyses

1. **Simulation-based calibration (SBC) at actual N and N_items**: The paper reports SBC p=0.23, but details are sparse. SBC should be reported at the exact N_models and N_items used in the primary results, with rank uniformity plots.

2. **Paired bootstrap test: ContamCal vs. linear regression**: A direct statistical test of whether the MAE difference is significant, not just point estimates.

3. **Verbatim contamination condition**: All contamination is via paraphrases. A d100_verbatim condition (exact benchmark items in training) would validate whether the signals detect the most common real-world contamination mode.

4. **Posterior predictive checks**: Item-level residual correlation analysis to diagnose local independence violations and their contribution to the coverage gap.

5. **Sensitivity to RRF k parameter**: The k=60 default is standard but not validated for this application. A sweep over k in {10, 30, 60, 120} would assess robustness.

6. **Full AUC x N simulation grid**: exp-004 has 48/120 conditions complete. The AUC=0.65 and AUC=0.90 conditions (0/60 seeds) would complete the identifiability phase diagram.

---

## Preliminary Score and Justification

**Score: 3/6 (Weak Reject)**

**Justification**: The paper addresses an important and timely problem with a principled Bayesian approach grounded in educational measurement theory. The signal characterization findings (S1 scale-invariance, Min-K++ reversal) and Fisher Information analysis are genuine contributions with standalone value. However, several methodological concerns prevent acceptance:

(1) The gap between the presented ME model and the actually-used simple model undermines the paper's distinctive UQ claim and raises reproducibility concerns.
(2) The actual sample size (N~32) is in the bias-sensitive zone identified by the paper's own simulations, casting doubt on whether the headline gamma estimates are data-driven or prior-driven.
(3) The multi-signal claim is not supported by verified empirical evidence at scales beyond 0.5B, where only S1 works.
(4) The SFT injection protocol introduces multiple confounds (ability regression, format artifacts, position bias) that complicate interpretation of the calibration results.
(5) The marginal advantage over linear regression raises questions about whether the full IRT machinery is justified.

**Path to acceptance**: (a) Resolve the ME model discrepancy and be transparent about which model produced which results. (b) Either verify multi-signal effectiveness at larger scales or reframe honestly as single-signal + IRT. (c) Add more model families and seeds to push N above the identifiability threshold. (d) Provide definitive coverage gap diagnosis via SBC at actual experimental parameters. (e) Elevate the Min-K++ reversal and signal characterization as primary contributions—these may be the paper's strongest offerings.

**Confidence: 4/5**
I have examined the methodology, Stan model specifications, simulation results, and experimental data in detail. My main uncertainty is about whether the paper's reported results (Tables 6-14) reflect a later, more complete experimental run than the intermediate artifacts I can access, which would potentially resolve some of the concerns about N_models and multi-scale signal effectiveness. The methodological concerns about the ME model discrepancy, per-benchmark separate fits, and SFT confounds are independent of this uncertainty.