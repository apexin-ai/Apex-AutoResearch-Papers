---
dream_id: dream_20260515T052337
tier: best
overall_score: 3/6 Weak Reject
timestamp: 2026-05-15T06:20:39.964668+00:00
---

# Dream Review Report: ContamCal

**Paper:** ContamCal: Bridging Contamination Detection and Benchmark Calibration via Contamination-Augmented Item Response Theory

**Review Mode:** Full (2 Reviewers + Roundtable)
**Venue Standard:** Top ML venue, ~25% acceptance rate, 6-point scale

---

## Roundtable Process

- **R1** (Methods + Experiments): Score 3/6, Confidence 4/5
- **R2** (Novelty + Related Work): Score 3/6, Confidence 4/5
- **Step 1** (Independent): Both reviewers completed blind assessments
- **Step 2** (Cross-sharing): R1's experimental concerns (coverage collapse, GSM8K overcorrection) fully corroborated by R2's analysis; R2's novelty assessment (Min-K++ reversal as strongest contribution) endorsed by R1
- **Step 3** (Convergence): Strong agreement on all major points; minor difference in emphasis (R1 more concerned about N=16 vs N≥50 gap; R2 more concerned about presentation density)
- **Step 4** (Synthesis): Below

---

## Overall Score: 3/6 (Weak Reject)

**Confidence: 4/5**

The paper proposes a timely and well-motivated framework (detection→calibration bridge via IRT), but the core calibration claim is undermined by severe coverage collapse and GSM8K overcorrection. The characterization contributions (Min-K++ reversal, benchmark-dependent γ heterogeneity) are genuinely valuable but the paper's framing does not yet match what the results actually support.

---

## Consolidated Strengths

### S1. Novel cross-disciplinary framework (R1+R2 agree)
The detection-to-calibration bridge via contamination-augmented IRT is a genuinely original conceptual contribution. No prior work has formally connected contamination detection signals to calibrated score estimation through an explanatory IRT model. The three structural adaptations from educational measurement's item compromise tradition (independent examinees → single model with joint item distribution; binary leakage → continuous exposure scores; stable ability → regime-conditional ability) are clearly articulated and represent non-trivial modifications. The meta-circularity argument for RRF (training-free aggregation avoids contaminating the aggregator) is sound and well-reasoned. This framework could inspire a productive line of future work regardless of the current paper's empirical limitations.

### S2. Min-K++ directional reversal is a significant empirical finding (R1+R2 agree)
The discovery that Min-K++ actively reverses direction at small model scales (Cohen's d = −1.98 at 0.5B, diminishing to −0.35 at 3B; Table 2) is novel, practically important, and likely the paper's most citation-worthy result. This is not merely a failure mode — it is an active misleading where perplexity-based signals produce false positives by assigning *higher* perplexity to contaminated items in small models. The mechanistic explanation (catastrophic forgetting disrupts global perplexity distributions) is convincing. This finding has immediate implications for practitioners using Min-K++ on smaller models and strengthens the case for multi-signal aggregation.

### S3. Comprehensive experimental design and honest limitation disclosure (R1+R2 agree)
The controlled SFT injection protocol is well-designed: paraphrased items to evade n-gram decontamination, 4 dosage levels (0%, 5%, 25%, 100%), 4 model scales (0.5B–7B), multiple random seeds, and ground-truth clean baselines. The paper evaluates 6 metrics (MAE, coverage at multiple levels, sharpness, Kendall τ, dose-response monotonicity, SBC) against 7 baselines. The coverage of 12 experiments spanning signal characterization, aggregation ablation, identifiability analysis, noise propagation, calibration, scale bridging, cross-family validation, and observational studies is thorough. The limitations section is admirably honest about coverage gaps, model family scope, SFT-vs-real contamination, unidimensionality, and closed-weight degradation.

### S4. Fisher Information identifiability analysis (R1 primary, R2 endorses)
The derivation of Fisher Information for γ in the 4PL+γ model (Eq. 4) is technically correct and provides useful theoretical grounding. The connection between signal AUC and identifiability threshold (structural at AUC≥0.55, practical at AUC≥0.70) is clean and actionable. The counter-intuitive finding that CI width inflation reaches 1.85× at AUC=0.80 due to exposure–θ collinearity is a novel theoretical insight. The CI width scaling law (∝ N^{−0.48}, R² = 0.97) closely matching the theoretical N^{−0.5} rate provides additional validation.

### S5. Benchmark-dependent contamination characterization (R2 primary, R1 endorses)
The finding that contamination causes forgetting on ARC (γ = −1.25) while causing inflation on GSM8K (γ = +2.85) challenges the dominant narrative that contamination uniformly inflates scores. The cross-family consistency (r = 0.88 with Llama-3.2-1B) supports the interpretation that contamination susceptibility is a benchmark property rather than a model family artifact. The three-regime taxonomy (catastrophic forgetting at 0.5B, selective memorization at 3B, near-immunity at 7B; Table 13) provides a useful conceptual framework.

---

## Consolidated Weaknesses

### W1. Coverage collapse fundamentally undermines the calibration claim (R1+R2 agree, **Critical**)
The 95% CI coverage of 69% on ARC (best case) and 44% on GSM8K is far below the 95% nominal level. This is the paper's most serious problem. The SBC diagnostics and the measurement error analysis (Section 5.5) suggest the root cause is not merely insufficient N or signal noise but structural model misspecification: the additive γ term in the 4PL+γ model cannot adequately capture the full complexity of contamination effects. The ME model improves coverage by only +9.5pp (62.5% → 72%) at the cost of 3.5× fitting time and 25% wider CIs — confirming that noise propagation is not the primary issue. The paper attributes the residual gap to local independence violations and cross-scale θ bias, which is plausible but these are *inherent* to the LLM evaluation setting, not fixable without fundamental model changes. When a framework's credible intervals cover only 44–69% of the time at nominal 95%, the Bayesian uncertainty quantification — a key selling point — is not trustworthy.

**Recommendation:** The paper must foreground this limitation rather than burying it in Discussion. Consider reporting calibrated point estimates (MAE, Kendall τ) as the primary results and presenting CIs as "directional uncertainty indicators" rather than nominal credible intervals. Alternatively, investigate conformal prediction wrappers that could provide distribution-free coverage guarantees on top of the IRT point estimates.

### W2. GSM8K overcorrection contradicts the calibration narrative (R1+R2 agree, **Major**)
On GSM8K, ContamCal produces MAE = 0.055 versus raw MAE = 0.005 — the calibrated scores are 11× worse than doing nothing. The 39pp contamination effect at 3B/d100 is too extreme for the additive γ to capture linearly, leading to systematic overcorrection. This is not merely a limitation but a clear failure case: a "calibration" method that makes scores less accurate on a significant benchmark undermines the overall claim. The paper acknowledges "overcorrection" but does not provide a principled criterion for when ContamCal should vs. should not be applied.

**Recommendation:** (a) Implement a gating mechanism: test whether γ is significant AND whether calibrated MAE < raw MAE before applying correction; (b) Consider item-level heterogeneous γ_i for benchmarks with extreme effects; (c) Honestly reframe: ContamCal is most effective when the contamination effect is moderate (ARC-like), not extreme (GSM8K-like) or negligible (MMLU-like).

### W3. ConStat (S3) reporting raises transparency concerns (R2 primary, R1 endorses, **Major**)
Table 1 reports S3 (ConStat) only as "Mean" AUC (0.85/0.55/0.52) without per-benchmark breakdown, unlike S1, S2, and S4. Table 3 (signal survival across regimes) omits S3 entirely from the SFT-clean and RL-Instruct rows. Table 4 (RRF ablation) does not include an S3-only row. This inconsistent treatment suggests ConStat may not have been fully computed or integrated into the pipeline. The method section (Section 3.2) describes a 4-signal pipeline but the actual RRF aggregation and downstream IRT results may rely on fewer than 4 signals. The paper should clearly state which signals were actually used in the RRF aggregation that feeds into the IRT model, and report all signals with equal granularity.

### W4. N=16 is below the paper's own identifiability threshold (R1 primary, R2 endorses, **Major**)
The simulation sweep (Section 5.3, Table 6) establishes that practical identifiability (95% CI coverage ≥93%, CI width ≤0.12) requires AUC≥0.70 and N≥50. The actual real-data experiments use N=16 (multi-seed pooled), which falls in a regime where the simulation predicts sub-optimal coverage and wider CIs. The paper does not reconcile this gap. At N=20 and AUC=0.70, the simulation shows only 88% coverage — and the real data achieves far less (69% on ARC), suggesting additional misspecification beyond what the simulation captures. This internal inconsistency (recommending N≥50 while reporting N=16 results as primary) weakens both the simulation findings and the real-data conclusions.

**Recommendation:** Either (a) pool more model variants (additional seeds, LoRA ranks, learning rates) to reach N≥50, or (b) explicitly position the N=16 results as preliminary with appropriate caveats, or (c) develop a small-sample correction (e.g., Growing Pains-style regularization) tailored to the low-N regime.

### W5. Linear regression baseline is nearly as good with far less complexity (R1 primary, **Moderate**)
On ARC, linear regression (B4, MAE=0.040) is within 0.5pp of ContamCal (MAE=0.035). B4 also provides bootstrap CIs with 60% coverage versus ContamCal's 69%. The 9pp coverage advantage comes at the cost of substantially higher complexity: Stan MCMC with ~4000+ parameters, convergence monitoring, and ~5 minutes fitting time. The paper does not test whether the MAE difference is statistically significant (no bootstrap CI on the gap). If a simple linear model achieves 87% of ContamCal's MAE performance with simpler inference, the practical case for the IRT machinery is weakened. The IRT model's advantages (per-item parameters, Bayesian uncertainty, interpretable item characteristics) are theoretically appealing but empirically not decisive given the coverage issues.

### W6. Limited cross-family and ecological validity (R2 primary, R1 endorses, **Moderate**)
A single additional model family (Llama-3.2-1B) at a single scale, with the r=0.88 correlation computed across only 3 benchmarks (ARC, GSM8K, MMLU), does not constitute robust cross-family validation. Three data points cannot support a meaningful correlation test. The SFT contamination protocol, while well-controlled, is a weak proxy for real pre-training contamination: SFT at 0.5B causes catastrophic forgetting (−17.5pp on ARC, −16.5pp on MMLU) that is primarily a capacity displacement artifact rather than a contamination effect. The RL observational study bridges this gap partially (33% regret reduction) but lacks ground truth. The 72B observational study is inference-only without ground truth contamination labels.

---

## Questions for Authors (Priority-Ordered)

1. **Calibration gating:** Given that ContamCal makes GSM8K 11× worse, can you provide a principled pre-application diagnostic that predicts when calibration will help vs. hurt? The per-benchmark γ significance test alone is insufficient (γ is significant on GSM8K yet calibration degrades scores).

2. **Coverage root cause:** With oracle exposure (perfect ground-truth dosage), what coverage does the 4PL+γ model achieve? If coverage is still poor with perfect signals, the problem is model specification, not signal quality — and this should be stated directly.

3. **Signal pipeline transparency:** Which signals were actually used in the RRF aggregation that produced the Table 8 results? Was S3 (ConStat) included? If not, the paper should describe a 3-signal pipeline.

4. **MAE gap significance:** Can you provide bootstrap CIs on the MAE difference between ContamCal (0.035) and linear regression B4 (0.040) on ARC? Is 0.5pp statistically significant?

5. **N=16 vs N≥50 reconciliation:** The simulation recommends N≥50 for practical identifiability. The real experiments use N=16. How should readers interpret γ estimates from the under-powered regime?

6. **Fisher Information conditional validity:** The I(γ) derivation (Eq. 4) conditions on all other parameters being known (per the paper's own caveat). With ~4000 jointly estimated parameters and N=16, how tight is this bound? Can you report the actual posterior variance of γ versus the Cramér-Rao lower bound?

7. **SFT forgetting vs. contamination:** The ARC negative γ (−1.25) may largely reflect SFT-induced capacity displacement at 0.5B rather than a genuine contamination effect. At 7B, where capacity displacement is minimal, the ARC contamination effect is ~0pp (Table 13). How do you disentangle these effects?

8. **Additive γ limitations:** For benchmarks with extreme effects (GSM8K +39pp at 3B), have you explored non-additive specifications (e.g., item-level γ_i, multiplicative effects, or saturating nonlinear transformations)?

---

## Minor Issues

- The abstract packs too many specific numbers (γ_ARC, γ_GSM8K, Cohen's d, two AUC thresholds, r, regret %). Prioritize 2–3 key results.
- 19 tables in the main body is excessive. Tables 11 (ME model), 12 (7B dose-response), 18 (2-signal), and 19 (QC ablation) could move to appendix without losing narrative coherence.
- S3 (ConStat) appears only as "Mean" in Table 1 without per-benchmark breakdown — inconsistent with other signals.
- The guessing prior c_j ~ Beta(5,20) (mean 0.2) is appropriate for 4-choice MCQ but not for GSM8K (open-ended) or HumanEval (code generation). Benchmark-specific guessing priors should be used.
- The claim "CI width ∝ N^{−0.48}" in the abstract is from simulation, not real data. This should be clarified.
- Table 3 is missing S3 rows for SFT-clean and RL-Instruct regimes.
- HumanEval appears in main-body tables despite being appendix-only. Consider removing from Tables 8 and 12 to reduce clutter.
- Dose-response monotonicity (Spearman ρ = −0.89/+0.92) is computed with only 4 dosage points — a weak statistical test. Acknowledge this limitation.

---

## Experiment Coverage Assessment

Compared against the experiment design (review_context.yaml), the paper covers all 12 planned experiments:

| Experiment | Paper Section | Status |
|---|---|---|
| stage1_signal_pipeline | §5.1, Tables 1–2 | Covered |
| rrf_aggregation_ablation | §5.2, Tables 4–5 | Covered |
| simulation_identifiability_sweep | §5.3, Tables 6–7 | Covered |
| noise_propagation_analysis | §5.5, Table 11 | Covered |
| irt_calibration_and_baselines | §5.4, Tables 8–10 | Covered |
| sft_d100_qc_only | §5.11, Table 19 | Covered |
| scale_bridging_7b | §5.6, Tables 12–13 | Covered |
| signal_survival_analysis | §5.1, Table 3 | Covered |
| rl_observational_case_study | §5.7, Tables 14–15 | Covered |
| multi_family_validation | §5.8, Table 16 | Covered |
| observational_72b | §5.9, Table 17 | Covered |
| closed_weight_2signal_mode | §5.10, Table 18 | Covered |

All imagined experiments are reflected in the paper. Experiment coverage is comprehensive.

---

## Actionable Recommendations for Revision

1. **Reframe from "calibration" to "contamination characterization with calibration capability."** The paper's strongest results are the characterization findings (benchmark-dependent effects, Min-K++ reversal, scale-dependent signal reliability, identifiability theory). The calibration results are mixed (good on ARC, harmful on GSM8K, unnecessary on MMLU). Lead with characterization, present calibration as effective in the moderate-effect regime.

2. **Implement a calibration gating criterion.** Before applying the γ correction, test: (a) is γ significant? AND (b) does posterior predictive check pass (PPP in [0.1, 0.9])? AND (c) is calibrated MAE < raw MAE on held-out folds? Report calibrated scores only when all three pass; otherwise report raw scores with a contamination flag and CI.

3. **Address the N=16 limitation.** Either increase N through additional model variants or develop explicit small-sample corrections. At minimum, add bootstrap or leave-one-out sensitivity analyses showing how γ estimates change when individual models are dropped.

4. **Clarify the signal pipeline.** Be transparent about which signals contributed to each result. If ConStat was not fully integrated, say so.

5. **Add conformal prediction wrapper.** Given the Bayesian CI coverage shortfall, consider adding a conformal prediction layer (Angelopoulos & Bates, which is already cited) to provide distribution-free coverage guarantees. This would turn a weakness into a methodological contribution.

6. **Streamline presentation.** Move 4–5 tables to appendix. Reduce abstract numbers. Add a "when to use ContamCal" decision flowchart.

---

## Score Justification

| Criterion | Score | Rationale |
|---|---|---|
| Novelty | 4/6 | Genuine cross-disciplinary synthesis; Min-K++ reversal novel; but core IRT model is standard explanatory IRT with one covariate |
| Methodology | 4/6 | Well-motivated framework; Fisher Info analysis correct; but additive γ too restrictive, ME model marginal |
| Experiments | 3/6 | Comprehensive design but coverage collapse, GSM8K overcorrection, N=16 below recommended threshold |
| Statistical Rigor | 3/6 | SBC included but coverage gap diagnosis incomplete; CIs unreliable; dose-response test weak |
| Clarity | 3/6 | Method clear but 19 tables excessive; abstract overloaded; ConStat reporting inconsistent |
| Impact | 3/6 | Framework concept valuable but coverage issues destroy practitioner trust; 2-signal mode limits applicability |
| **Overall** | **3/6** | **Weak Reject** — valuable conceptual contribution and characterization findings, but the calibration claim (the paper's headline) is not supported by the experimental results |

A revised version that (a) reframes around characterization with conditional calibration, (b) addresses the coverage gap honestly in the framing (not just limitations), (c) implements calibration gating, and (d) either increases N or adds conformal coverage guarantees would likely reach 4/6 (Borderline Accept) at a top venue.