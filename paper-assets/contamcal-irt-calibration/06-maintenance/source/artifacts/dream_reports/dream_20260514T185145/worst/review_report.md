---
dream_id: dream_20260514T185145
tier: worst
overall_score: 3/6 — Reject
timestamp: 2026-05-14T20:15:50.074633+00:00
---

# Dream Review Report: ContamCal IRT Calibration

**Paper**: "When Can We Calibrate Contaminated Benchmarks? Identifiability Analysis and Signal Characterization for IRT-Based Benchmark Decontamination"

**Review mode**: Full (2 Reviewers + Roundtable)

---

## Reviewer Assignments

- **R1** (Methods + Experiments): Methodological soundness, experimental rigor, statistical analysis
- **R2** (Novelty + Related Work): Contribution significance, novelty assessment, literature coverage

---

## R1 Review: Methods and Experiments

### Summary

ContamCal proposes a two-stage framework for post-hoc calibration of contaminated benchmark scores: RRF fusion of four detection signals into exposure scores, followed by contamination-augmented 4PL IRT with Bayesian inference. The paper is framed around "informative negative results" — the IRT calibration underperforms a simple linear regression baseline (7.9pp vs 4.8pp MAE), only one of four signals works (S1 embedding, AUC>0.95; S2–S4 at chance), and RRF aggregation provides no benefit over S1 alone. The Fisher Information analysis and signal characterization are the strongest contributions, but the core calibration claim is undermined by the method's own experimental results.

### Strengths

1. **Rigorous Fisher Information derivation.** The analysis provides I(γ) ∝ N·(AUC−0.5)²/σ²_e with clean structural (AUC≥0.55) and practical (AUC≥0.70, N≥50) thresholds. This is actionable design guidance for future work and the paper's strongest theoretical contribution.

2. **Controlled contamination design with ground truth.** The SFT injection pipeline across 4 scales, 5 dosage levels, and multiple seeds enables rigorous calibration evaluation — methodologically superior to observational studies alone.

3. **Honest reporting of negative results.** The paper does not hide that its proposed method fails to beat simpler baselines. The oracle-γ ablation (2.4pp MAE) cleanly decomposes failure into estimation noise vs. framework soundness. The 12× sim-to-real gap, SBC failure (p=0.003), and coverage shortfall (75% vs 95%) are transparently reported.

4. **Min-K++ directional reversal.** Cohen's d ∈ [−2.67, −1.22] showing that Min-K++ actively misleads rather than merely failing is a genuinely novel and practically important cautionary finding for the MIA literature, well-documented across scales and regimes.

5. **Comprehensive baseline comparison.** Seven baselines spanning naive scoring, item removal, simpler IRT variants, linear regression, mitigation strategies, and DCR provide a thorough competitive landscape. Linear regression (B4) is particularly informative — exposing that trivial models outperform the full IRT machinery.

6. **Well-grounded cross-disciplinary connection.** The three structural adaptations from item compromise IRT (independent examinees → shared item pool; binary → continuous exposure; stable → regime-conditional ability) are clearly articulated and correctly identified as non-trivial.

### Weaknesses

1. **(Major) The core method fails, raising contribution framing questions.** 4PL+γ (MAE=7.9pp) is beaten by raw scores (6.5pp) and linear regression (4.8pp). On MMLU, raw scores (3.2pp) outperform 4PL+γ (6.8pp) by 2×. The paper tries to be both a calibration method paper (which fails) and a diagnostic study (which succeeds). The current framing falls between these two stools.

2. **(Major) N=26 models is critically insufficient.** The 4PL+γ model has ~4000+ parameters estimated from ~26000 observations, but effective sample size for γ is driven by N_models=26, well below the paper's own practical threshold of N≥50. The paper's own diagnostics confirm instability: Rhat up to 1.12, ESS as low as 87. This failure was predictable from standard IRT sample-size literature (Lord 1968: N≥200 for 3PL; Hulin et al. 1982; Drasgow 1989).

3. **(Major) θ–γ confounding at r=0.72 not adequately resolved.** A posterior correlation of 0.72 on ARC is dangerously high and threatens identifiability. The Fisher Information analysis assumes other parameters known (conditional lower bound), but real-data confounding is far worse. No instrumental variable approach or staged estimation is attempted.

4. **(Moderate) Coverage gap attribution (60/25/15) lacks rigorous support.** The decomposition into 60% local independence violation, 25% insufficient N, 15% model misspecification appears asserted rather than formally derived. SBC alone cannot produce these percentages. These should be presented as rough estimates with appropriate caveats.

5. **(Moderate) RRF is an unnecessary complication given results.** Since only S1 works and RRF(0.958) < S1-only(0.964), the multi-signal framework adds complexity without benefit. Substantial paper space is devoted to four signals and their aggregation when the conclusion is "just use S1."

6. **(Moderate) SFT injection may not represent real-world contamination.** The 0.5B deflation (−16.5pp MMLU) suggests the SFT proxy introduces artifacts: small models suffer catastrophic forgetting from the SFT signal, which is not characteristic of pretraining contamination. This confounds the contamination signal with fine-tuning damage.

7. **(Moderate) The calibration paradox empties the useful operating regime.** Calibration is most needed at small scale (destructive deflation) but least feasible (violates γ>0). At large scale, it is most feasible but least needed (effects <2pp within noise). The paper should explicitly characterize whether a non-empty practical regime exists.

8. **(Minor) ME model provides minimal improvement.** Coverage improves 75%→79% (+4pp), far from the 95% target. The improvement is modest relative to the additional model complexity.

### Questions for Authors

1. Given linear regression outperforms ContamCal, what concrete path exists to close the gap between 7.9pp and 2.4pp (oracle)?
2. How do you reconcile cross-scale pooling (needed for power) with the finding that contamination effects are directionally inconsistent across scales?
3. Can you conduct posterior predictive checks on real data to identify which specific model assumptions are violated?
4. For θ–γ correlation of 0.72 on ARC: have you tried a two-stage estimation where θ is first estimated from clean benchmarks?
5. The closed-weight 2-signal mode (MAE=13.7pp, worse than raw) severely limits practical applicability to open-weight models only. How do you envision extending to closed-weight models?
6. Why was the d=100% labeling artifact not anticipated in the experimental design?

### R1 Preliminary Score: 3/6
### R1 Confidence: 4/5

---

## R2 Review: Novelty and Related Work

### Summary

The paper pivots from demonstrating successful calibration to framing around "informative negative results" — characterizing when IRT-based calibration can work rather than showing it does. The claimed contributions center on identifiability boundary analysis, signal characterization, and the calibration paradox. While the problem formulation is genuine and under-served, the methodological novelty is limited to competent synthesis of existing components, and the negative results were largely predictable from known IRT limitations.

### Strengths

1. **Genuine and under-served problem formulation.** The shift from contamination detection to post-hoc calibration with UQ fills a real gap. No prior method produces calibrated scores with uncertainty quantification for contaminated benchmarks.

2. **Deep cross-disciplinary grounding.** The connection to educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004) represents genuine intellectual engagement. The three structural adaptations are correctly identified as non-trivial.

3. **Fisher Information analysis is rigorous and actionable.** The structural vs. practical threshold distinction and the measurement error attenuation corollary provide directly usable guidance that future work would reference.

4. **Min-K++ reversal is independently citation-worthy.** This finding has direct implications for the MIA literature regardless of the calibration framework's success.

5. **Calibration paradox is a genuine structural insight.** The observation that calibration is most needed where least feasible (small scale: destructive deflation) and least needed where most feasible (large scale: negligible effects) is a real contribution to understanding the problem space.

6. **Meta-circularity argument for RRF is principled.** The reasoning that learned aggregator training data may itself be contaminated is a sound design principle.

### Weaknesses

1. **(Major) "Informative negative result" does not meet contribution threshold for a top venue.** The failure was largely predictable: (a) 4PL models require N >> 50 — operating at N=26 and observing failure is unsurprising to IRT practitioners; (b) contamination effect heterogeneity across scales is expected given task format diversity; (c) the sim-to-real gap confirms the bi-normal signal model is a simplification, inherent to any analytic bound. The primary lesson — "standard IRT needs more data than typical LLM evaluation provides" — is well-established in psychometrics.

2. **(Major) Limited methodological novelty.** The 4PL+γ model adds a single linear covariate to standard explanatory IRT. RRF is off-the-shelf. ME model is classical errors-in-variables. No individual component is new, and the synthesis does not produce emergent capabilities since linear regression outperforms the full framework.

3. **(Major) Missing engagement with IRT sample-size literature.** Lord (1968), Hulin et al. (1982), Drasgow (1989), Ames & Penfield (2015) all establish minimum N guidelines. Operating at N=26 with 4PL and reporting failure is a predictable outcome the literature would have warned against. This omission undermines the claim that the negative result is informative.

4. **(Major) Missing connections to data influence methods.** TracIn (Pruthi et al. 2020) and TRAK (Park et al. 2023) provide a fundamentally different approach to quantifying contamination exposure — measuring how training examples affected test predictions, conceptually closer to the true causal quantity γ_k·τ_{ij}. This omission means the paper doesn't discuss arguably the most principled alternative signal source for Stage 1.

5. **(Moderate) DCR comparison is superficial.** DCR (Oren et al., 2024) is the closest predecessor. The paper notes it lacks UQ and RL handling but doesn't provide structural comparison of how DCR's fuzzy inference differs from RRF+IRT mechanistically, or why DCR might fare differently under these conditions.

6. **(Moderate) Missing multidimensional IRT discussion.** Fitting unidimensional θ to MMLU (spanning diverse knowledge domains) is a clear simplification. Burnell et al. (2023) explores multidimensional IRT for LLMs. The paper does not discuss whether forced unidimensionality contributes to model misspecification and the coverage gap.

7. **(Moderate) "When can we calibrate" reframing may not rescue the contribution.** The identifiability boundaries (AUC≥0.70, N≥50) are essentially "you need good signals and enough data" — a general truth about estimation, not a contamination-specific insight. The more interesting >12× sim-to-real gap receives less analytical depth than it deserves.

8. **(Minor) Missing discussion of conformal prediction under distribution shift** (Tibshirani et al. 2019, Barber et al. 2023) as an alternative UQ approach that relaxes exchangeability.

### Questions for Authors

1. Given N=26 was known to be below the practical threshold of N≥50, why proceed with full 4PL+γ rather than restricting to 2PL+γ or framing the experiment as a feasibility boundary test from the start?
2. What is the oracle MAE decomposition — how much error comes from signal noise vs. model specification vs. insufficient N?
3. Is the 0.5B deflation an artifact of the LoRA SFT protocol (catastrophic forgetting from fine-tuning) rather than a genuine contamination effect?
4. Under what conditions would multi-signal aggregation be expected to help? Is there a theoretical result on when RRF degrades vs. improves over the best single signal?
5. Cross-family γ sign disagreement (Qwen MMLU γ=0.018 vs Llama γ=−0.085) — does this mean γ_k is a benchmark×family interaction, not a benchmark property?

### R2 Preliminary Score: 3/6
### R2 Confidence: 4/5

---

## Roundtable Discussion

### Step 2: Cross-Sharing

After exchanging reviews, both reviewers identified strong convergence on core assessments.

**R1→R2 reaction**: R1 agrees with R2's point about missing IRT sample-size literature — this is a critical gap that would have predicted the failure at N=26. R1 also endorses the concern about missing data influence methods (TracIn, TRAK) as alternative signals. R1 notes that R2's framing — "competent synthesis, not innovation" — accurately captures the methodological contribution level.

**R2→R1 reaction**: R2 agrees with R1's technical concerns about θ–γ confounding (r=0.72), coverage gap attribution being asserted rather than derived, and the SFT injection introducing artifacts. R2 notes that R1's point about the calibration paradox emptying the useful operating regime strengthens the novelty concern — if no practical regime exists, the framework's value is purely theoretical.

### Step 3: Convergence

**Points of agreement (both reviewers):**

1. **Score**: Both assign 3/6 (Reject) with 4/5 confidence
2. **Core issue**: The method fails, and the failure was largely predictable from known IRT limitations (insufficient N, model misspecification)
3. **Strongest contributions**: Fisher Information identifiability analysis and Min-K++ directional reversal are individually valuable, standalone findings
4. **RRF adds no value**: Multi-signal aggregation degrades to single-signal mode; substantial paper space wasted on a framework that doesn't contribute
5. **"Informative negative result" insufficient for top venue**: The negative result largely confirms known limitations rather than revealing new structural insights
6. **SBC sim-to-real gap is interesting but under-analyzed**: The >12× gap deserves more decomposition — why exactly does simulation performance not transfer?
7. **Honest reporting is commendable**: The transparency about failure is scientifically valuable but does not substitute for positive contribution
8. **Better venue**: Both suggest this is better suited for a workshop, Findings track, or empirical study venue

**Points of divergence:**

- R1 places more weight on specific technical issues (θ–γ confounding, coverage attribution, SFT artifacts); R2 places more weight on positioning and novelty threshold
- R1 sees the Fisher Information analysis as the paper's strongest contribution; R2 considers it somewhat standard (general power analysis dressed in IRT notation)
- R2 identifies more related work gaps (IRT sample-size literature, data influence methods, conformal prediction under shift)

Both reviewers agree these divergences do not change the overall assessment.

### Step 4: Consolidated Assessment

**Overall Score: 3/6 (Reject)**
**Confidence: 4/5**

### Decision Rationale

The paper addresses a genuine and important problem — post-hoc calibration of contaminated LLM benchmark scores with uncertainty quantification — and the controlled experimental design with ground-truth clean scores is well-executed. The intellectual honesty in reporting negative results is commendable.

However, the paper does not meet the contribution threshold for a top ML venue (~25% acceptance):

1. **The proposed method fails.** 4PL+γ IRT (MAE=7.9pp) is outperformed by linear regression (4.8pp) and even raw scores on some benchmarks (MMLU: 3.2 vs 6.8pp). RRF aggregation provides no benefit over using S1 alone. Coverage is 20pp below nominal. γ credible intervals exclude zero on only 1/4 benchmarks.

2. **The failure was predictable.** Operating a 4PL model at N=26 is well below established minimum sample sizes in the psychometric literature. The paper's own Fisher Information analysis derives N≥50 as a practical threshold, making the N=26 result a confirmatory exercise rather than a discovery.

3. **Limited methodological novelty.** Each component (RRF, 4PL IRT, errors-in-variables, NUTS inference) is standard. The synthesis does not produce emergent capabilities — a simpler baseline dominates.

4. **The "informative negative result" framing is insufficient.** For a negative result paper to succeed at a top venue, the insights must be surprising and redirect the field. Here, the main lessons are: (a) IRT needs more data than N=26, (b) contamination effects are heterogeneous across scales — neither is surprising.

**What would strengthen the paper:**

- **Close the oracle gap**: The 2.4pp oracle-γ MAE shows the IRT framework is theoretically sound. Demonstrating a concrete path to close the 7.9→2.4pp gap (e.g., larger N, hierarchical IRT with scale-conditional γ, better signals) would transform this from "it doesn't work" to "here's how to make it work."
- **Deeper sim-to-real gap analysis**: The >12× gap is the paper's most interesting quantitative finding. A formal decomposition into contributing factors (local independence, model misspecification, N insufficiency) with individual experiments isolating each factor would be a genuine contribution.
- **Commit to characterization**: Drop the calibration method framing entirely. Lead with signal characterization + identifiability analysis as standalone contributions. The Min-K++ reversal and Fisher Info bounds are publishable without the failed calibration attempt.
- **Engage with IRT sample-size literature**: Explicitly position the work relative to known minimum-N requirements and explain why LLM evaluation's few-examinee regime creates fundamental challenges.
- **Explore data influence methods as signals**: TracIn/TRAK could provide causally grounded exposure estimates that may outperform the current S1–S4 pipeline.

### Strengths Worth Preserving

- Fisher Information identifiability bounds with structural/practical threshold distinction
- Min-K++ directional reversal (Cohen's d ∈ [−2.67, −1.22]) as MIA cautionary finding
- Calibration paradox: most needed where least feasible
- Controlled experimental design with ground-truth clean scores
- Transparent SBC diagnostics and coverage analysis
- Cross-family validation revealing γ non-transferability (r=0.31)

### Critical Weaknesses

- Core method fails to beat trivial baselines
- N=26 critically insufficient; failure predictable from IRT literature
- Multi-signal aggregation adds no value (RRF ≤ S1-only)
- θ–γ confounding (r=0.72 on ARC) unresolved
- Coverage gap attribution asserted without formal derivation
- SFT injection may conflate contamination with fine-tuning artifacts
- Missing engagement with IRT sample-size literature, data influence methods
- Practical operating regime may be empty (calibration paradox)

### Experiment Coverage Assessment

The paper covers all experiments from the full design: signal pipeline, RRF ablation, IRT calibration with 7 baselines, 7B scale bridging, signal survival across training regimes, RL observational case study, 72B observational, closed-weight 2-signal mode, cross-family (Llama) validation, simulation identifiability sweep, and ME model ablation. Coverage is comprehensive. The issue is not missing experiments but that the results uniformly demonstrate failure across all dimensions.

### Recommended Venue

Workshop paper (e.g., Efficient Evaluation of LLMs) or EMNLP Findings, where the signal characterization and identifiability analysis would be well-received without the expectation of a working calibration method.