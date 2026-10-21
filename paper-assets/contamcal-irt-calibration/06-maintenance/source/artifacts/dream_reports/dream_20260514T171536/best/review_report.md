---
dream_id: dream_20260514T171536
tier: best
overall_score: 4/6 Borderline Reject
timestamp: 2026-05-14T18:28:41.673146+00:00
---


# Dream Review Report: ContamCal

**Paper**: ContamCal: Calibrating Benchmark Scores for Training Data Contamination via Contamination-Augmented Item Response Theory  
**Date**: 2026-05-14  
**Review Mode**: Full (2 Reviewers + Roundtable)  
**Venue Standard**: Top ML venue, ~25% acceptance, 6-point scale

---

## Step 1: Independent Reviews

### R1 (Methods & Experiments) — Score: 4/6, Confidence: 4/5

**Strengths**:
1. Well-motivated problem formulation; the "statistical safety net" framing and causal inference analogy are compelling
2. Rigorous Bayesian inference pipeline (HMC, 4 chains, R̂<1.01, zero divergences)
3. Comprehensive controlled experimental design with unambiguous ground truth (5 dosages × 3 seeds × 3 benchmarks)
4. Per-benchmark γ_k is a genuine methodological contribution revealing meaningful heterogeneity (GSM8K γ=0.85 vs MMLU γ=0.22)
5. Honest characterization of signal failures — Min-K++ directional reversal and RRF degradation at 0.5B add credibility
6. Simulation sweep with Fisher Information-grounded identifiability boundaries provides actionable practitioner guidance

**Weaknesses**:
1. **γ positive bias at realistic sample sizes**: Internal diagnostics show +57.5% bias at N=30 and +23.6% at N=50 with σ_e=0.1. The experimental setup (N~45 per benchmark) is in the bias-sensitive regime. The reported 1.8pp MAE may benefit from error cancellation rather than genuine parameter recovery.
2. **Measurement error model status unclear**: Internal decision logs suggest the analytic ME model was abandoned (performed worse than simple model), yet the paper claims it as a key contribution and Table 10 reports ME results. This contradiction needs resolution — are Table 10 results from simulation only or real data?
3. **Rank-1 exposure matrix**: The exposure matrix is an outer product of dosage and item RRF scores, meaning all models at the same dosage share identical per-item exposure patterns. This artificially constrains the information structure and may inflate identifiability relative to real-world scenarios.
4. **SFT injection is a weak contamination proxy**: LoRA SFT produces qualitatively different memorization than pre-training exposure — catastrophic forgetting on 3B GSM8K (60.5%→12.0%), position bias, format artifacts. The paper understates this severity.
5. **MMLU subsampled to 1000 items**: Full MMLU (14K items, ~56K parameters) was infeasible for NUTS. Extrapolation validity from subsample is not established.
6. **Single model family**: Controlled experiments use only Qwen2.5; Llama-3.2-1B is a single cross-family check at one scale.

**Key Questions**:
- Decompose 1.8pp MAE into γ estimation error vs θ estimation error (run with oracle γ)
- Coverage uniformity across dosage levels (d000 vs d100)?
- Rank-1 vs full exposure matrix comparison?

### R2 (Novelty & Related Work) — Score: 4/6, Confidence: 4/5

**Strengths**:
1. The reframing from contamination elimination to statistical adjustment is the right intellectual move — fills a genuine gap (detection-to-calibration bridge)
2. Grounding in item compromise IRT (Eckerly 2017, Sinharay 2017) is well-chosen; the three structural adaptations demonstrate genuine engagement with psychometric literature
3. Per-benchmark γ_k yields interpretable findings; cross-family consistency (Pearson r=0.91) suggests contamination susceptibility is a benchmark property — implications beyond this paper
4. Fisher Information derivation with structural (AUC≥0.55) and practical (AUC≥0.70) boundaries is the strongest theoretical contribution
5. Meta-circularity argument for training-free RRF is sound and unusually honest
6. Min-K++ directional reversal is a cautionary finding with independent value for the detection community

**Weaknesses**:
1. **Limited core novelty**: The 4PL+γ model adds a single linear contamination covariate to standard explanatory IRT. RRF is off-the-shelf. ME model is classical errors-in-variables. This is a competent synthesis, not a new technique. The 2PL+γ baseline (MAE 2.9pp) already captures most calibration benefit, suggesting 4PL machinery provides only incremental improvement.
2. **Causal inference analogy never formalized**: No DAG, no formal identification argument, no sensitivity analysis for unmeasured confounding. Pre-training contamination may be undetectable by all four signals. The strong ignorability assumption cannot be justified.
3. **Binary-to-continuous exposure is standard in explanatory IRT**: De Boeck & Wilson 2004 explicitly cover continuous covariates. This should not be claimed as a structural contribution.
4. **Scale-dependent claim confounded with LoRA adapter size**: Adapter sizes grow proportionally with model size (34MB→115MB). "Scale-dependent" could mean "intervention-dependent." A controlled experiment fixing adapter-to-parameter ratio would disambiguate.
5. **SFT contamination proxy**: Headline results (1.8pp MAE) obtained entirely in SFT regime where signals are strongest. Observational results show small adjustments with wide CIs but no ground truth.
6. **Missing data attribution methods**: TracIn and TRAK cited only as future work. For a paper claiming comprehensive multi-signal detection, influence function methods deserve explicit justification for exclusion.

**Key Questions**:
- S1-only ablation vs full ContamCal at 0.5B?
- Hierarchical model with partial pooling of γ_k across benchmarks?
- Total computational cost of full pipeline (signals + MCMC)?

---

## Step 2: Cross-Sharing

After exchanging reviews, both reviewers noted significant overlap in their assessments:

**R1 → R2**: "I agree the novelty concern is well-founded. The 2PL+γ to 4PL+γ improvement (2.9→1.8pp) shows the full IRT machinery matters, but R2 is correct that the individual components are standard. The Fisher Information analysis is the most original theoretical piece."

**R2 → R1**: "R1's technical concerns about γ bias and rank-1 exposure matrix are serious and were not on my radar. If γ is systematically overestimated by 23-58% at this N, the paper's central claim about accurate calibration needs qualification. The MMLU subsampling issue also warrants prominent disclosure."

**New shared concern**: R2's point about scale-dependent confounded with adapter size intersects with R1's observation about catastrophic forgetting at 3B — both point to the LoRA injection protocol as a systematic confound that the paper does not adequately address.

---

## Step 3: Convergence

### Points of Agreement
1. **Score**: Both 4/6 — above average but below top-venue acceptance threshold
2. **Strongest contribution**: Per-benchmark γ_k finding and its cross-family consistency
3. **Strongest theoretical contribution**: Fisher Information identifiability analysis
4. **Most valuable empirical contribution**: Min-K++ directional reversal characterization
5. **Primary concern (shared)**: SFT injection as weak proxy; headline results may not generalize to real-world contamination
6. **Secondary concern (shared)**: Limited model family breadth for controlled experiments
7. **Nature of work**: Well-executed synthesis of existing techniques applied to an important new problem, rather than a methodologically novel contribution

### Points of Differentiation
- **R1 prioritizes internal validity concerns**: γ bias, exposure matrix structure, ME model discrepancy — questioning whether the numbers are trustworthy as stated
- **R2 prioritizes external validity and novelty concerns**: questioning whether the contribution is sufficient for a top venue even if numbers hold up
- **Resolution**: Both concerns are legitimate and complementary. Even if internal validity issues (R1) are addressed, the novelty ceiling (R2) remains a barrier. Conversely, even high novelty wouldn't compensate for unreliable results.

### Adjusted Scores After Discussion
- R1: 4/6 → 4/6 (unchanged; R2's novelty concerns reinforce but don't lower)
- R2: 4/6 → 4/6 (unchanged; R1's technical concerns reinforce but don't lower)

---

## Step 4: Consolidated Assessment

### Overall Score: 4/6 (Borderline Reject)
### Confidence: 4/5

### Meta-Review

ContamCal addresses a genuinely important and timely problem: rather than trying to eliminate benchmark contamination (which Xu et al. 2024 showed is futile), it proposes to statistically measure and subtract contamination effects via a contamination-augmented IRT framework. The intellectual framing is correct, the psychometric grounding is well-chosen, and the experimental design (controlled SFT injection with known ground truth) enables rigorous evaluation.

**The paper's strongest contributions are empirical rather than methodological**: (1) the per-benchmark γ_k finding revealing 4× heterogeneity in contamination susceptibility across benchmark types, with cross-family consistency suggesting this is a benchmark property; (2) the Min-K++ directional reversal characterization as a cautionary finding; and (3) the Fisher Information identifiability analysis providing principled boundaries for when calibration is feasible.

**However, several concerns prevent recommendation for acceptance:**

1. **Novelty ceiling**: The core method is a straightforward application of explanatory IRT with a contamination covariate — all individual components (4PL IRT, RRF, measurement error model, HMC inference) are standard. The 2PL+γ baseline (2.9pp MAE) captures ~70% of the calibration benefit, suggesting the full 4PL+ME machinery provides diminishing returns. For a top venue, synthesis papers must demonstrate emergent value beyond the components.

2. **Internal validity concerns**: The γ parameter exhibits systematic positive bias (+23-58%) at the paper's actual sample sizes (N~45). The measurement error model's status is ambiguous (possibly abandoned per internal diagnostics but claimed as a contribution). The exposure matrix has rank-1 structure that may artificially inflate identifiability. MMLU required subsampling from 14K to 1K items. These collectively undermine confidence in the precise numbers reported.

3. **External validity gap**: All headline results (1.8pp MAE, 94% coverage) come from LoRA SFT contamination injection, which produces qualitatively different memorization patterns than real-world pre-training contamination. The observational studies (Instruct, DeepSeek, 72B) show only small adjustments with wide CIs and no ground truth for validation. The scale-dependent signal effectiveness claim is confounded with adapter size variation.

4. **Experimental scope**: Controlled experiments primarily use a single model family (Qwen2.5) with minimal cross-family validation (one Llama model at one scale). Three benchmarks, while diverse in format, represent a narrow slice of the evaluation landscape.

### Recommendations for Revision

**Critical** (must address):
- Disclose and characterize γ bias at realistic N prominently; provide oracle-γ ablation
- Clarify ME model status: what model was actually used for reported results?
- Discuss rank-1 exposure matrix limitation and its implications for real-world applicability
- Disclose MMLU subsampling and its impact on reported numbers

**Important** (would significantly strengthen):
- Add controlled experiments on at least one additional model family at multiple scales
- Formalize or downgrade the causal inference analogy (DAG, identification conditions, or explicit acknowledgment as informal motivation)
- Provide dosage-stratified coverage analysis
- Discuss LoRA adapter size confound with scale-dependent claims
- Include data attribution methods discussion in related work

**Minor**:
- Sensitivity analysis on RRF k parameter
- Disambiguate "calibration" from probability calibration more clearly in introduction
- Discuss ConStat paraphrase generator contamination circularity
- Include HELM and Chatbot Arena in related work

### Strengths Summary (for authors)
The paper has several elements of a strong contribution: the problem framing is exactly right, the psychometric grounding is unusually well-done for an ML paper, the experimental design with controlled ground truth is rigorous, and the honest characterization of method failures (signal degradation, RRF noise dilution) adds credibility. The per-benchmark γ_k finding has standalone value. With revisions addressing the internal validity concerns and expanded model family coverage, this could become a solid venue-appropriate contribution. The authors should consider whether a venue with a focus on evaluation methodology (e.g., COLM, or a workshop on LLM evaluation) might be a better initial target than a general top-tier venue.

### Weaknesses Summary (for authors)
The fundamental tension is between the importance of the problem and the incrementality of the solution. The paper's value proposition rests on the claim that IRT-based calibration substantially outperforms simpler approaches — but the 2PL+γ baseline already performs well (2.9pp), and the additional complexity of 4PL + ME + full Bayesian inference may not justify itself against a well-tuned linear baseline with bootstrap CIs (3.2pp). The authors should consider whether framing the per-benchmark γ_k characterization and signal effectiveness analysis as the primary contributions (with calibration as the application) might better match the paper's actual strength distribution.

---

*Review conducted by 2 independent reviewers (R1: Methods & Experiments; R2: Novelty & Related Work) with full roundtable protocol (Steps 1-4).*
