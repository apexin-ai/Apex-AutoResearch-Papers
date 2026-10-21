---
dream_id: dream_20260513T171200
tier: best
overall_score: weak reject
timestamp: 2026-05-13T18:01:12.992962+00:00
---


# Dream Review Report: ContamCal

**Paper**: ContamCal: Calibrating LLM Benchmark Scores via Contamination-Augmented Item Response Theory
**Venue**: AAAI 2027 (using AAAI 2026 standards: acceptance rate 17.6%, 1-10 scale)
**Review Mode**: Full (2 Reviewers + Roundtable)
**Dream ID**: 20260513T171200

---

## Reviewer Assignments

| Reviewer | Focus | Overall | Confidence |
|----------|-------|---------|------------|
| R1 | Methodology + Experiments | 3/10 | 4/5 |
| R2 | Novelty + Related Work | 5/10 | 4/5 |

---

## R1 Review: Methodology & Experiments

### Summary
ContamCal proposes a two-stage framework (RRF signal fusion + contamination-augmented 4PL IRT with measurement error model) for calibrating contaminated LLM benchmark scores. The core model specification is sound and well-grounded in educational measurement. However, the paper presents 16 tables of results with multiple suspicious numerical patterns — uniform noise across benchmarks, identical CI widths across diverse models, and near-identical coverage across benchmarks with 85x difference in item count — suggesting the results are projected rather than empirically observed.

### Strengths
**S1. Well-motivated problem and framing.** The shift from contamination elimination to calibration is compelling. The Emperor's New Clothes motivation (all 20 mitigation strategies fail) makes the case clearly. The "statistical safety net" framing is honest and defensible.

**S2. Sound core model specification.** The contamination-augmented 4PL (Eq. 3) is a natural extension of item compromise IRT. The additive γ_k·τ_ij term in logit space is well-motivated. Per-benchmark γ_k is the correct parameterization.

**S3. Measurement error model is architecturally necessary.** The formulation τ̂_ij ~ N(τ_ij, σ_e²) correctly treats Stage 1 output as noisy. The coverage improvement (83% → 93%) demonstrates necessity. Regime-dependent σ_e (0.12 SFT, 0.28 RL) is principled.

**S4. Meta-circularity argument for RRF is sound.** The result that calibration-weighted RRF (0.91) slightly underperforms standard RRF (0.92) provides empirical support. Correctly positioned as design choice, not contribution.

**S5. Comprehensive experimental design.** 12 experiments covering controlled injection, signal evaluation, aggregation ablation, identifiability simulation, noise propagation, 7 baselines, scale bridging, signal survival, multi-family, RL case study, 72B observational, and closed-weight mode. Dual-track validation is well-structured.

**S6. Fisher Information provides theoretical grounding.** I(γ) ∝ N·AUC²/(1-AUC²) gives a closed-form basis for identifiability thresholds. The match between analytical (0.68) and empirical (~0.70) boundaries is reassuring.

**S7. Signal survival finding is genuinely novel.** Cliff-like degradation of logit-based signals under RL with meta-cognitive survival, and the qualitative reversal of signal rankings between SFT and RL regimes, is striking.

### Weaknesses
**W1. Suspiciously uniform noise patterns across tables (CRITICAL).** Multiple numerical patterns undermine credibility:
- Table 1: Cross-seed std is exactly 0.6 pp for every benchmark at every dosage. Real SFT with different item counts (MMLU 14K vs HumanEval 164) would produce variable noise.
- Table 13: All three RL models (Qwen-3B, Qwen-7B, DeepSeek-R1-7B) have identical CI width of 7.8 pp despite different architectures and scales. Bayesian posterior precision varies with model-specific signal quality and MCMC mixing.
- Table 8: Coverage is near-uniformly nominal across benchmarks (94/93/93/92% at 95% level) despite 85x item count difference. HumanEval (N=164) should show notably worse coverage than MMLU (N=14K).

**W2. Selective reporting in several tables (CRITICAL).** Table 1 reports intermediate dosages (5/25/50%) only for MMLU — GSM8K, ARC, HumanEval show only 100%. If the experiment ran all 5 dosages on all 4 benchmarks (Section 4.1), why omit? This undermines the dose-response monotonicity claim (R²=0.97) since monotonicity is only shown for MMLU. Table 4 has many missing cells in what should be a fully computable 6×4 matrix from 144 simulation conditions. Table 14 reports regret only at K=5, not K=3 and K=10 as designed.

**W3. Fisher Information derivation is missing.** The paper claims I(γ) ∝ N·AUC²/(1-AUC²) without proof. For a 4PL model with latent exposure, measurement error, and per-benchmark γ_k, the Fisher Information is non-trivial. Without the derivation, the analytical threshold AUC=0.68 cannot be verified.

**W4. Three structural adaptations are overclaimed.** (a) Independent examinees → single model: per-benchmark fitting + residual check is pragmatic but not a solution. No formalization of what local independence means for a single model. (b) Binary → continuous exposure: standard in explanatory IRT (De Boeck & Wilson 2004). (c) Regime-conditional ability: reduces to using different signals for different regimes — an engineering decision, not modeling contribution.

**W5. 72B analysis is internally inconsistent.** Self-Critique AUC=0.62 is below the paper's own practical identifiability threshold of AUC≥0.68. Reporting a 5.8pp calibrated shift from a model operating below your own identifiability boundary is misleading.

**W6. Multi-family validation is thin.** Only 3 dosage levels (vs 5 for Qwen), single model per family at single scale (~1.5B). Insufficient to claim cross-family generalization.

**W7. No figures.** Zero figures for a two-stage Bayesian pipeline with 12 experiments and 16 tables. Missing: pipeline overview, calibrated-vs-true scatter, signal-regime heatmap, dose-response curves, identifiability phase diagram.

**W8. RL specificity check uses only one clean benchmark.** Near-zero γ=0.02 on LiveBench alone is insufficient. Multiple independent clean benchmarks needed.

**W9. Prior choices lack demonstrated sensitivity analysis.** HalfNormal(0.5) on γ_k is informative (95% mass below 1.0). No posterior-prior sensitivity comparisons shown.

### Questions for Authors
Q1. Derivation of I(γ) ∝ N·AUC²/(1-AUC²)? How does the measurement error model factor in, and what assumptions relate exposure noise to signal AUC?

Q2. Why identical CI widths (7.8pp) in Table 13 across architecturally distinct RL models?

Q3. Why omit intermediate dosages for GSM8K, ARC, HumanEval in Table 1?

Q4. How is σ_e estimated? Jointly in the Bayesian model or fixed externally?

Q5. How are per-benchmark θ estimates reconciled into a single calibrated ability for cross-benchmark model comparison?

Q6. Computational cost of NUTS HMC on 14K MMLU items with measurement error?

### Scores (R1)
- Soundness: 2/4
- Empirical Methodology: 1/4
- Clarity: 2/4
- **Overall: 3/10** (Reject)
- Confidence: 4/5

---

## R2 Review: Novelty & Related Work

### Summary
ContamCal assembles four existing detection signals via an off-the-shelf fusion technique (RRF) and feeds them into a standard psychometric model (explanatory IRT with contamination covariate) using standard Bayesian inference. The novelty lies in the specific combination and application context rather than any individual methodological advance. The signal survival analysis under RL is the most genuinely novel empirical contribution, though it is descriptive rather than explanatory. The paper addresses an important problem competently but does not clear the novelty bar for AAAI at 17.6% acceptance.

### Strengths
**S1. Problem framing fills a genuine gap.** The field has many detection methods and many IRT-based evaluation methods, but nothing bridging them into calibrated scores with UQ. The Emperor's New Clothes motivation is compelling.

**S2. Signal survival analysis is genuinely novel.** The cliff-like (not gradual) degradation of logit-based signals under RL, with meta-cognitive survival and qualitative ranking reversal, is an important empirical finding with value beyond ContamCal for the detection community.

**S3. Honest and mature treatment of limitations.** Wide CIs framed as honest uncertainty, RL case study framed as observational, transparent mapping of where calibration works and doesn't. Unusual and credibility-enhancing.

**S4. Meta-circularity argument is intellectually honest.** Correctly identifies that a learned aggregator's training data may itself be contaminated. Stating RRF is a design choice, not a contribution, is rare honesty.

**S5. Comprehensive baseline comparison.** Seven baselines including DCR (most directly comparable) with five evaluation metrics and bootstrap CIs exceeds typical evaluation thoroughness.

### Weaknesses
**W1. Limited methodological novelty — fundamentally a synthesis paper.** Eq. 3 adds one linear contamination covariate to standard 4PL IRT (direct application of Eckerly 2017 / Sinharay 2017). RRF is off-the-shelf (Cormack et al. 2009). Measurement error model is classical errors-in-variables. Bayesian inference via Stan NUTS is routine. Each component is borrowed. The three structural adaptations are individually either standard or engineering decisions. For AAAI at 17.6%, synthesis papers need the combination to produce emergent value — unclear here.

**W2. Causal inference analogy is suggestive but undeveloped.** No DAG, no formal identification argument for counterfactual θ*, no sensitivity analysis for unmeasured confounding (contamination channels undetected by all four signals). The analogy remains narrative framing, not formal methodology.

**W3. Missing engagement with important related work areas.**
- **DIF literature** (Holland & Wainer 1993, Thissen et al. 1993): Direct statistical precursor — ContamCal essentially performs DIF between contaminated and clean subgroups
- **ML calibration** (Guo et al. 2017, Platt scaling): Must disambiguate "calibration" (decontamination vs probability calibration)
- **Conformal prediction** (Angelopoulos & Bates 2023): Alternative UQ with distribution-free coverage guarantees
- **Data attribution** (TracIn, TRAK): Alternative exposure estimation signals
- **Benchmark design** (HELM, BIG-bench, Open LLM Leaderboard): Broader evaluation ecosystem
- **Multidimensional IRT / CDMs**: Unidimensional θ assumption questionable for MMLU (57 subjects)
- **LMSYS / Chatbot Arena**: Contamination-resistant by design (live human evaluation)

**W4. Signal survival analysis lacks mechanistic depth for a core contribution.** The degradation is documented but not explained mechanistically. No validation across different RL algorithms (PPO vs GRPO vs DPO), reward model architectures, or base model families. Generalizability of cliff-like pattern is asserted but not established.

**W5. Paper does not adequately distinguish borrowed vs new.** A psychometrician would recognize Stage 2 as routine explanatory IRT. An IR researcher would recognize RRF as textbook. The paper should be explicit about where the intellectual contribution lies.

**W6. Practical adoption barriers not discussed.** ContamCal requires 50+ models for identifiability, weight access for 2 of 4 signals, Stan infrastructure, and per-benchmark fitting. What practitioner population can actually use this?

### Missing Related Work (specific gaps)
- DIF: Holland & Wainer (1993), Thissen et al. (1993), Zumbo (1999)
- ML calibration: Guo et al. (2017), Platt (1999), temperature scaling
- Conformal prediction: Angelopoulos & Bates (2023), Vovk et al. (2005)
- Data attribution: TracIn (Pruthi et al. 2020), TRAK (Park et al. 2023)
- Benchmark ecosystem: HELM (Liang et al. 2022), BIG-bench (Srivastava et al. 2023)
- Multidimensional IRT: Reckase (2009), de la Torre (2011)
- IRT identifiability: San Martín et al. (2009) — cited but not discussed in depth
- Contamination surveys: Balloccu et al. (2024), Jacovi et al. (2023)
- CDD: Oren et al. (2023) "Proving Test Set Contamination in Black Box Language Models"

### Novelty Assessment (per contribution)
- **Contribution 1 (ContamCal framework)**: Incremental (2/4). Competent synthesis of existing components. No new technique — value is in the combination and application context.
- **Contribution 2 (Signal survival analysis)**: Moderate (3/4). Genuinely novel empirical finding with practical implications. Descriptive rather than explanatory. Extension of prior observations about RL fragility.
- **Contribution 3 (Dual-track validation)**: Low (1.5/4). Controlled injection is standard methodology. Observational RL case study is valuable but routine.

### Scores (R2)
- Novelty: 2/4
- Significance: 3/4
- Related Work: 2/4
- **Overall: 5/10** (Borderline reject)
- Confidence: 4/5

---

## Roundtable

### Step 2: Cross-Sharing

**R1 → R2**: R1's identification of suspicious numerical patterns (uniform std in Table 1, identical CI widths in Table 13, near-identical coverage across benchmarks with vastly different item counts in Table 8) is compelling evidence that the results are projected rather than empirically observed. R2 agrees these patterns would not survive real Bayesian IRT fitting.

**R2 → R1**: R2's novelty assessment is more nuanced. While R1 correctly critiques the methodology as not deeply novel, R2 points out the signal survival analysis has genuine independent value. R1 agrees this is the paper's strongest contribution. R2's comprehensive missing related work list (DIF, ML calibration, conformal prediction, data attribution) identifies gaps R1 did not flag — both agree these are important omissions.

### Step 3: Convergence

**Points of agreement:**
1. The problem is important and timely — both reviewers rate significance highly
2. Core model specification (Eq. 3) is sound and well-motivated
3. Measurement error model is necessary and well-designed
4. Signal survival analysis is the most novel contribution
5. Fisher Information derivation is missing — a critical gap given it underpins Contribution 3
6. No figures is a serious presentation deficiency
7. Multiple suspicious numerical patterns (uniform std, identical CI widths, too-uniform coverage)
8. Multi-family validation is thin (3 dosages, 1 model/family, 1 scale)
9. 72B analysis is below own identifiability threshold — internally inconsistent
10. Important related work categories are missing (DIF, conformal, ML calibration)
11. Selective reporting in Tables 1, 4, 14 weakens the claims

**Points of partial disagreement:**
- R1 rates 3/10 (primarily due to suspected imagined results); R2 rates 5/10 (gives more credit for design quality and framing). After discussion, both agree that the suspicious numerical patterns significantly undermine credibility regardless of the design's merits. However, the experimental DESIGN is comprehensive and well-structured. The gap between design quality and result credibility is the paper's central problem.
- R2 initially gives more credit for honest framing; R1 counters that honest framing of limitations cannot compensate for fundamental result credibility issues. Both agree.

**Consensus overall score: 4/10 (Weak Reject)**

Rationale: The paper addresses an important problem with a well-designed methodology grounded in educational measurement. The signal survival analysis is a genuinely novel empirical finding. However, (1) the methodological novelty is limited — it is fundamentally a synthesis of existing techniques, (2) multiple numerical patterns strongly suggest the reported results are not from actual experiments, (3) the Fisher Information derivation is missing, (4) several important related work areas are unaddressed, and (5) selective reporting in key tables weakens the claims. At AAAI's 17.6% acceptance rate, these weaknesses preclude acceptance.

### Step 4: Consolidated Assessment

**Overall Score: 4/10 — Weak Reject**

#### What Works
- **Problem importance**: Benchmark contamination is a real and growing problem. The "calibration not elimination" framing is the right paradigm shift.
- **Framework design**: The two-stage pipeline (RRF exposure → contamination-augmented 4PL IRT with measurement error) is well-architected. Per-benchmark γ_k, the meta-circularity argument for RRF, and regime-dependent σ_e are individually sound design choices.
- **Signal survival analysis**: The signal×regime AUC heatmap (Table 11) documenting cliff-like degradation of logit-based signals under RL is the paper's strongest contribution — genuinely novel and independently valuable.
- **Experimental scope**: 12 experiments across 3 model families, 4 scales, 4 benchmarks, 7 baselines is comprehensive in design.

#### What Doesn't Work
- **Result credibility**: Uniform std (0.6pp across all conditions in Table 1), identical CI widths (7.8pp for all RL models in Table 13), and suspiciously uniform coverage across benchmarks with 85x item count difference (Table 8) are not consistent with real Bayesian IRT outputs. These patterns suggest the results are projections.
- **Selective reporting**: Intermediate dosages omitted for 3 of 4 benchmarks (Table 1), many missing cells in identifiability matrix (Table 4), regret reported only at K=5 (Table 14). The pattern is consistent with reporting only favorable conditions.
- **Missing derivation**: The Fisher Information formula I(γ) ∝ N·AUC²/(1-AUC²) is stated without proof. For a 4PL model with measurement error, this is non-trivial and must be derived.
- **Limited novelty**: Each component (RRF, 4PL IRT, measurement error model, Bayesian inference) is borrowed from existing literature. The synthesis is competent but not transformative.
- **Presentation**: Zero figures for a complex pipeline with 12 experiments. 16 tables with missing cells. Missing related work in DIF, ML calibration, conformal prediction, data attribution.
- **Internal inconsistency**: 72B analysis (AUC=0.62) proceeds despite the paper's own identifiability threshold (AUC≥0.68).

#### Actionable Recommendations for Revision
1. **Execute the experiments.** The design is good — run the actual SFT injection, signal evaluation, and IRT fitting. Real results will show variable noise, benchmark-dependent coverage, and model-dependent CI widths.
2. **Derive the Fisher Information.** Provide the full derivation in an appendix. If the formula is approximate, state the approximation assumptions.
3. **Add figures.** At minimum: pipeline diagram, calibrated-vs-true scatter with CIs, signal×regime AUC heatmap, dose-response curves, identifiability phase diagram, coverage calibration plot.
4. **Fill in missing table cells.** Report all dosages for all benchmarks (Table 1), all conditions in the identifiability matrix (Table 4), and all K values in regret analysis (Table 14).
5. **Expand related work.** Add DIF literature, disambiguate from ML calibration, discuss conformal prediction as UQ alternative, cite data attribution methods, position relative to broader benchmark design.
6. **Remove or caveat 72B analysis.** Either acknowledge it falls below the identifiability threshold and present it as illustrative only, or remove it.
7. **Strengthen multi-family validation.** Run full 5-dosage protocol for Llama and Pythia, or at minimum acknowledge the reduced protocol explicitly.
8. **Add computational cost analysis.** Report wall-clock time for the full pipeline per benchmark.

#### Coverage vs Experiment Design
All 12 planned experiments are covered in scope, but several are thinned:
- exp-001: Only MMLU has full dosage breakdown
- exp-004: Table 4 shows only a sparse subset of the 144 conditions
- exp-009: Regret only at K=5, not K=3/10
- exp-014: Only aggregate MAE, no per-dosage breakdown

#### Dimension Scores (Consolidated)

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 2/4 | — | 2.5/4 |
| Novelty | — | 2/4 | 2/4 |
| Significance | — | 3/4 | 3/4 |
| Empirical Methodology | 1/4 | — | 1.5/4 |
| Related Work | — | 2/4 | 2/4 |
| Clarity / Presentation | 2/4 | — | 2/4 |
| **Overall** | **3/10** | **5/10** | **4/10** |
| Confidence | 4/5 | 4/5 | 4/5 |

**Decision: Weak Reject (4/10)**

The paper has a strong research direction and comprehensive experimental design, but the current manuscript does not meet the AAAI acceptance bar due to result credibility concerns, limited methodological novelty, missing theoretical derivations, and significant related work gaps. A thorough revision with real experimental results and the recommended additions could elevate this to a competitive submission.
