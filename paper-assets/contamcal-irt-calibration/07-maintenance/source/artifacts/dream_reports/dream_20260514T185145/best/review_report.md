---
dream_id: dream_20260514T185145
tier: best
overall_score: 4/6 Weak Accept (Borderline)
timestamp: 2026-05-14T19:58:53.804859+00:00
---

# Dream Review Report — ContamCal: Calibrating Benchmark Scores for Training Data Contamination via Contamination-Augmented Item Response Theory

**dream_id**: 20260514T185145 | **review_mode**: full | **date**: 2026-05-14

---

## Roundtable Summary

Two independent reviewers assessed this paper under top ML venue standards (acceptance rate ~25%, 6-point scale).

| | R1 (Methods + Experiments) | R2 (Novelty + Related Work) |
|---|---|---|
| **Score** | 3/6 (Weak Reject) | 4/6 (Weak Accept) |
| **Confidence** | 4/5 | 4/5 |

**Consolidated Score: 4/6 (Weak Accept / Borderline)**

The paper addresses a genuinely important and under-served problem — calibrating (not just detecting) benchmark contamination — with a principled Bayesian framework grounded in educational measurement theory. The empirical contributions (Min-K++ reversal, γ_k as benchmark property, Fisher Information identifiability analysis) have standalone value. However, methodological novelty is limited (competent synthesis of existing components), external validity of the SFT injection proxy is a substantive concern, and presentation deficiencies (zero figures, incomplete baseline comparison table) weaken the submission.

---

## Step 1: Independent Reviews

### Reviewer 1 — Methods & Experiments (Score: 3/6)

**Strengths**:
- Min-K++ directional reversal (Cohen's d up to -2.85 at 7B) is a genuinely citation-worthy cautionary finding with clear mechanistic explanation
- Fisher Information identifiability analysis provides rigorous signal quality thresholds (structural AUC≥0.55, practical AUC≥0.70) validated by 144-condition simulation
- Comprehensive baseline comparison (7 methods) with appropriate metrics
- SBC diagnostics (p=0.23) demonstrate proper model specification verification
- MCMC convergence diagnostics thoroughly reported (R̂_max=1.007, ESS≥380, 0 divergent transitions)
- Transparent limitation acknowledgment throughout

**Weaknesses**:
1. **(Major) N_models=32 below identifiability regime.** The paper's own simulation analysis suggests N≥50 for reliable γ recovery. At N=32, systematic positive bias in γ estimates is expected. The multi-seed pooling strategy to reach N=32 pools models of vastly different scales (0.5B–7B), which conflates scale effects with contamination effects. The paper does not discuss the bias implications of operating below its own recommended threshold.

2. **(Major) SFT injection confounds.** LoRA SFT injection produces qualitatively different contamination patterns than real-world pre-training contamination. Specific concerns: (a) 0.5B models show ability regression under contamination (contamination hurts overall performance), which is the opposite of the real-world concern; (b) catastrophic forgetting at smaller scales on GSM8K may inflate γ_GSM8K ≈ 0 not because GSM8K resists contamination but because SFT destroys the model's reasoning ability; (c) position bias from contamination injection (answer-position patterns in paraphrased items) may confound signal detection.

3. **(Major) Table 6 incomplete.** The main results table reports coverage, CI width, Kendall τ, and monotonicity violations ONLY for ContamCal — all 7 baselines show "—" for these metrics. This makes the comparison appear one-sided and prevents assessing whether ContamCal's advantages on UQ metrics are simply because it's the only method with UQ, not because its UQ is superior. Bootstrap CIs for at least the linear regression and remove-and-rescore baselines should be computable.

4. **(Moderate) Per-benchmark γ_k via separate fits.** Fitting each benchmark independently (Section 3.3) prevents formal heterogeneity testing and information sharing across benchmarks. Table 9 shows the hierarchical model (μ_γ=0.22, σ_γ=0.14) is intermediate between global and per-benchmark — but this is presented as an ablation rather than the primary specification. A hierarchical model would naturally regularize extreme γ_k estimates and enable formal hypothesis tests (σ_γ > 0?).

5. **(Moderate) Scale-dependent claim potentially confounded with adapter capacity.** As model size grows from 0.5B to 7B, LoRA adapter capacity grows proportionally. The "capability emergence in memorization and metacognition" explanation for S2/S4 recovery could instead reflect adapter encoding capacity. An experiment fixing adapter-to-parameter ratio across scales would disambiguate.

**Questions for Authors**:
- What is the γ positive bias at N=32 in your own simulation? If substantial, does error cancellation explain the 2.1pp MAE?
- Can you provide per-dosage coverage breakdowns? Is coverage uniform across d000/d005/d025/d100?
- What happens to S2/S4 AUC claims at 1.5B/3B if you use full-parameter SFT instead of LoRA?

---

### Reviewer 2 — Novelty & Related Work (Score: 4/6)

**Strengths**:
- **Correct intellectual framing.** The shift from contamination elimination to post-hoc statistical calibration fills a genuine gap. Detection methods flag but don't calibrate; IRT evaluates but doesn't model contamination; DCR adjusts but without UQ.
- **Deep psychometric grounding.** The connection to educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004) represents genuine cross-disciplinary engagement, not superficial citation. The DIF analogy for γ_k is apt.
- **Fisher Information analysis.** The bi-normal signal model derivation connecting AUC to γ recoverability, with the structural/practical threshold distinction, provides actionable theoretical guidance. This is the strongest theoretical piece.
- **Per-benchmark γ_k heterogeneity.** CV=0.52 within-family + r=0.91 cross-family (Qwen vs. Llama) together constitute a genuine empirical finding about contamination susceptibility as a benchmark property.
- **Meta-circularity argument for RRF.** The principled motivation for training-free aggregation (a learned aggregator's training data may itself be contaminated) is sound and rarely articulated.
- **Honest uncertainty characterization.** Wider CIs for RL models (1.8×) and 2-signal mode (1.41×) are features of honest Bayesian reasoning, correctly reported.

**Weaknesses**:
1. **(Major) Limited methodological novelty — synthesis, not innovation.** The 4PL+γ model adds a single linear contamination covariate to standard explanatory IRT (De Boeck & Wilson 2004). RRF is off-the-shelf (Cormack et al. 2009). The ME model is classical errors-in-variables (Carroll et al. 2006). Stan NUTS is standard. No individual component is new. The 2PL+γ baseline (3.9pp MAE) already captures ~75% of the improvement over DCR (4.6pp), suggesting diminishing returns from the full 4PL+ME machinery. For a top venue, synthesis papers must demonstrate emergent value substantially beyond the sum of parts.

2. **(Major) SFT injection external validity.** All headline results (2.1pp MAE, 92% coverage) come from controlled SFT injection with rephrased items. The observational studies (RL models: γ_MMLU=0.18 with CI width 0.22; 72B: -1.6pp adjustment) show only small effects with wide CIs and no ground truth. The gap between SFT injection and real pre-training contamination is fundamental: pre-training sees raw items, uses different learning dynamics, and doesn't induce catastrophic forgetting.

3. **(Major) Zero figures in a visualization-critical paper.** 14 tables, 0 figures. For a paper whose core contributions include signal×scale×dosage characterization and dose-response analysis, the absence of a signal heatmap, dose-response curves, calibrated-vs-true scatter, or even a pipeline diagram is a serious presentational deficiency. This makes the paper read like a technical report.

4. **(Moderate) Incomplete Table 6.** UQ metrics (coverage, CI width, τ, monotonicity) reported only for ContamCal. Baselines with "—" entries create an unfair visual impression. At minimum, bootstrap CIs for linear regression and remove-and-rescore are feasible and should be provided.

5. **(Moderate) Rank-1 exposure matrix in controlled setup.** All models at the same dosage share identical per-item exposure patterns (exposure = dosage × item-level RRF). This constrains the information structure and may inflate identifiability relative to real-world settings where contamination profiles vary per model.

6. **(Minor) "Calibration" terminology ambiguity.** Despite a clarifying paragraph in Related Work, the title "Calibrating Benchmark Scores" will be initially misconstrued as probability calibration (Guo et al. 2017) by many readers.

7. **(Minor) Missing related work.** Several relevant recent works not cited: Growing Pains (arXiv 2604.12843, IRT at scale with 400+ models), Inference-Time Decontamination (EMNLP 2024 Findings), KDS (Dong et al. 2024 — mentioned briefly but not assessed as a potential 5th signal).

**Questions for Authors**:
- Can you provide UQ metrics for baselines in Table 6, at least for linear regression + bootstrap CI?
- What is the oracle MAE when using ground-truth exposure labels vs. signal-derived exposure? (Table 9 oracle=1.4pp — is this oracle-γ or oracle-exposure?)
- Is the 92% coverage uniform across dosage levels?
- What is the total pipeline computational cost for calibrating a new model?
- Why not include KDS (Dong et al. 2024) as a 5th signal given its reported effectiveness?

---

## Step 2: Cross-Sharing — Key Overlaps and Divergences

### Points of Agreement (both reviewers converge):
1. **SFT external validity is a major concern.** Both reviewers independently flag this as fundamental, not merely a caveat.
2. **Table 6 incomplete comparison.** Both note the missing UQ metrics for baselines as undermining the comparison.
3. **Min-K++ reversal is the paper's strongest empirical finding.** Both recognize its independent citation value.
4. **Fisher Information analysis is rigorous and valuable.** Both praise the theoretical grounding.
5. **Per-benchmark γ_k heterogeneity is a genuine insight.** Both find the cross-family r=0.91 compelling.
6. **N_models=32 is a concern.** Both note it falls below the paper's own recommendations.

### Points of Divergence:
1. **Severity of novelty limitation.** R2 weights this as a major weakness (synthesis, not innovation; 2PL+γ captures 75% of benefit). R1 focuses more on execution issues. Both agree the paper's value is primarily empirical.
2. **Presentation weight.** R2 strongly flags zero figures as a major deficiency. R1 does not raise this.
3. **Adapter capacity confound.** R1 raises scale-dependent claims being confounded with LoRA adapter capacity. R2 does not independently raise this but would likely agree.
4. **Score split.** R1=3 vs R2=4. The gap reflects R1's heavier weighting on methodological implementation concerns (some based on anticipated internal issues) vs. R2's recognition that the empirical findings have standalone value despite limited methodological novelty.

---

## Step 3: Convergence Discussion

After cross-sharing, the reviewers converge on the following assessment:

**The paper's actual contribution is primarily empirical, not methodological.** The calibration framework (4PL+γ IRT + RRF) is a competent synthesis that works, but the individual components are all known. The paper's real value lies in:
- The systematic signal×scale×dosage characterization (first of its kind)
- Min-K++ reversal discovery (independently important cautionary finding)
- γ_k as benchmark property (CV=0.52, cross-family r=0.91)
- Fisher Information identifiability thresholds (actionable theoretical guidance)

**Both reviewers agree the paper would benefit from**:
1. Figures (signal heatmap, dose-response curves, calibrated-vs-true scatter)
2. Complete Table 6 with baseline UQ metrics
3. Explicit discussion of γ bias at N=32
4. Broader validation beyond Qwen (Llama is a start but single-scale)
5. Honest reframing that elevates empirical characterization over the framework itself

**The SFT external validity gap is not fully addressable** without real pre-training contamination ground truth, which doesn't exist. The observational studies provide directional evidence but cannot replace controlled validation. This is a fundamental limitation of the research program, not just this paper.

**Consolidated score adjustment**: R1 moves from 3 to 3.5 (recognizing empirical value), R2 stays at 4. Consensus: **4/6 (Weak Accept / Borderline)**.

---

## Step 4: Consolidated Assessment

### Overall Score: 4/6 (Weak Accept / Borderline)

### Recommendation: **Borderline Accept — conditional on revisions addressing presentation and completeness issues.**

### Summary Assessment

ContamCal proposes the first principled framework for calibrating (not just detecting) benchmark contamination in LLMs, grounding its approach in educational measurement's item compromise IRT literature. The two-stage design (multi-signal exposure mapping + contamination-augmented 4PL IRT) is sound and produces interpretable, uncertainty-quantified calibrated scores. The headline result — 2.1pp MAE with 92% CI coverage, significantly outperforming 7 baselines — is achieved on carefully controlled SFT injection experiments.

The paper's actual value is primarily empirical rather than methodological: the Min-K++ directional reversal, per-benchmark γ_k heterogeneity, and Fisher Information identifiability thresholds are individually valuable contributions that would impact the contamination detection community. The framework itself is a competent synthesis of known components (explanatory IRT, RRF, measurement error models) rather than a methodological innovation.

### Strengths (ordered by importance)

1. **Addresses a genuine gap.** No existing method produces calibrated scores with uncertainty quantification for contaminated benchmarks. The shift from detection/mitigation to calibration is well-motivated by the "Emperor's New Benchmarks" finding.

2. **Min-K++ directional reversal.** The discovery that Min-K++ actively misleads at high contamination (Cohen's d = -1.98 to -2.85, intensifying with scale) is independently valuable and has practical implications for the contamination detection community.

3. **Fisher Information identifiability analysis.** Rigorous derivation connecting signal AUC to γ recoverability with validated structural/practical thresholds. Provides actionable guidance for practitioners and characterizes the system's operating regime.

4. **Per-benchmark γ_k as benchmark property.** CV=0.52 within family + r=0.91 cross-family correlation establishes that contamination susceptibility depends on benchmark format (ARC > MMLU >> GSM8K), not model architecture. GSM8K as negative control (γ≈0.06, CI includes 0) adds credibility.

5. **Comprehensive experimental scope.** 9 experiments covering signal characterization, RRF ablation, main calibration, 7B scale bridging, RL observational, 72B frontier, 2-signal degraded mode, and cross-family validation. All planned experiments are present.

6. **Honest uncertainty characterization.** Wider CIs for RL models (1.8×), 2-signal mode (1.41×), and the coverage gap (92% vs 95%) are transparently reported and correctly attributed.

### Weaknesses (ordered by severity)

1. **(Major) Limited methodological novelty.** The 4PL+γ model is a direct application of explanatory IRT (De Boeck & Wilson 2004) with a contamination covariate. RRF, measurement error models, and Stan NUTS are all off-the-shelf. The 2PL+γ baseline at 3.9pp MAE captures ~75% of the improvement over DCR (4.6pp), suggesting diminishing returns from the full machinery. The paper's contribution is primarily empirical application and characterization, not methodological.

2. **(Major) SFT injection external validity.** All headline quantitative results derive from LoRA SFT with rephrased items — qualitatively different from real pre-training contamination. Specific concerns: (a) ability regression at 0.5B means contamination hurts performance, opposite to the real-world threat; (b) catastrophic forgetting on GSM8K may explain γ_GSM8K≈0 as an artifact rather than format resistance; (c) observational studies (RL, 72B) lack ground truth and show only small adjustments with wide CIs. This is acknowledged in Limitations but understated.

3. **(Major) Incomplete baseline comparison (Table 6).** Coverage, CI width, Kendall τ, and monotonicity metrics are reported only for ContamCal. All baselines show "—". This prevents fair assessment of whether ContamCal's advantage is in calibration accuracy or merely in having UQ at all. Bootstrap CIs for linear regression and remove-and-rescore baselines would partially address this.

4. **(Moderate) N_models=32 in bias-sensitive regime.** The paper's own simulation suggests N≥50 for reliable γ recovery. At N=32, systematic positive γ bias is expected. The paper does not discuss this implication or whether the reported MAE partially benefits from error cancellation.

5. **(Moderate) Zero figures.** 14 tables and no figures in a paper about signal×scale×dosage characterization. A signal heatmap, dose-response curves, and calibrated-vs-true scatter would dramatically improve readability and impact.

6. **(Moderate) Scale-dependent claims potentially confounded.** LoRA adapter capacity scales with model size. The "capability emergence" interpretation for S2/S4 could alternatively reflect adapter encoding capacity. An adapter-ratio-controlled experiment would disambiguate.

7. **(Minor) Rank-1 exposure matrix.** In the controlled setup, all models at the same dosage share identical per-item exposure patterns. This may inflate identifiability relative to real-world scenarios.

8. **(Minor) Terminology.** "Calibrating Benchmark Scores" in the title invites confusion with probability calibration (Guo et al. 2017).

9. **(Minor) Sparse ConStat data.** S3 results only for 2 benchmarks at 2 scales, limiting assessment of its contribution to the signal portfolio.

### Key Questions for Authors

1. Can you provide coverage and CI width metrics for at least linear regression + bootstrap CI in Table 6?
2. What is the γ positive bias at N=32 in your own simulation? Is the 2.1pp MAE robust to bias correction?
3. Is coverage uniform across dosage levels, or does it degrade at high contamination?
4. What is the total computational cost (signals + MCMC) for calibrating a new model?
5. Why not include KDS as a 5th signal? What is the oracle-exposure MAE vs. oracle-γ MAE?
6. Can you provide SBC rank histograms?

### Actionable Revision Recommendations

1. **Add 3-4 key figures**: pipeline diagram, signal×scale AUC heatmap, dose-response curves, calibrated-vs-true scatter with CIs.
2. **Complete Table 6**: provide bootstrap CI coverage/width for feasible baselines.
3. **Discuss N=32 bias explicitly**: report simulation bias at actual sample size and interpret MAE in that context.
4. **Reframe contribution**: elevate empirical characterization findings (Min-K++ reversal, γ_k as benchmark property, identifiability thresholds) as primary contributions; position framework as enabling infrastructure rather than the core novelty.
5. **Expand cross-family validation**: Llama at 2-3 scales with multiple dosages for full γ_k estimation.
6. **Address adapter confound**: at minimum discuss; ideally run one adapter-controlled experiment.

### Experiment Coverage Assessment

All 9 imagined experiments from the design document are present in the paper:
- ✅ stage1_signal_pipeline (§4.1)
- ✅ rrf_aggregation_ablation (§4.3)
- ✅ irt_calibration_and_baselines (§4.4-4.5)
- ✅ scale_bridging_7b (§4.7)
- ✅ signal_survival_analysis (§4.1-4.2)
- ✅ rl_observational_case_study (§4.8)
- ✅ observational_72b (§4.9)
- ✅ closed_weight_2signal_mode (§4.10)
- ✅ multi_family_validation (§4.11)

Coverage is comprehensive with no significant omissions. The paper executes the experimental plan faithfully.

---

*Review conducted by 2 independent reviewers with full roundtable protocol (independent → cross-share → converge → consolidate).*