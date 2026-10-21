---
dream_id: dream_20260515T052337
tier: median
overall_score: weak reject
timestamp: 2026-05-15T06:28:30.980937+00:00
---

# Dream Review Report: ContamCal

**Paper**: ContamCal: Calibrating LLM Benchmark Scores via Contamination-Augmented Item Response Theory
**Review Mode**: Full (2 Reviewers, complete roundtable)
**Date**: 2026-05-15

---

## Roundtable Consensus

| Reviewer | Focus | Independent Score | Post-Discussion Score |
|----------|-------|------------------|-----------------------|
| R1 | Methods + Experiments | 3/6 | 3/6 |
| R2 | Novelty + Related Work | 3/6 | 3/6 |
| **Consensus** | | | **3/6 (Weak Reject)** |

**Confidence**: High. Both reviewers converged independently on the same score and maintained it after cross-discussion. The assessment is robust.

---

## Summary

ContamCal proposes a two-stage framework bridging contamination detection and benchmark score calibration via a contamination-augmented 4PL IRT model with per-benchmark γ_k coefficients. Stage 1 computes item-level exposure scores from embedding similarity (S1), Min-K++ (S2), and Self-Critique (S4) fused via RRF. Stage 2 fits a Bayesian IRT model in Stan to produce decontaminated scores with credible intervals.

The paper's most valuable contributions are empirical characterizations — the Min-K++ directional reversal finding (Cohen's d = −1.45 to −1.98), the benchmark-dependent contamination effect heterogeneity (ARC forgetting vs. GSM8K null), and Fisher Information identifiability bounds — rather than the calibration machinery itself, which produces worse MAE than raw scores on average (0.052 vs. 0.034) and suffers from severe coverage collapse (44–62.5% at nominal 95%).

---

## Agreed Strengths

1. **Min-K++ directional reversal is a genuinely novel, citation-worthy finding.** Both reviewers independently identified this as the paper's strongest result. Cohen's d = −1.45 to −1.98 shows Min-K++ actively misleads (not merely fails) at high contamination — a cautionary finding with broad impact for the contamination detection community. The mechanistic explanation (SFT overfitting reduces token surprise, inverting the detection signal) is compelling.

2. **Benchmark-dependent contamination effects challenge simplistic narratives.** The contrast between ARC forgetting (γ = −1.46, CI excludes zero) and GSM8K null effect (γ = 0.19, CI includes zero) demonstrates that contamination is not monolithic. This is an empirically grounded and useful characterization that advances understanding beyond binary "contaminated/clean" framing.

3. **Fisher Information identifiability analysis is technically sound and actionable.** The derivation connecting signal AUC to γ recoverability (structural threshold AUC ≥ 0.55, practical AUC ≥ 0.70) is correct and the 120-condition simulation sweep provides empirical validation. The N_models as a multiplicative factor argument is well-established.

4. **Novel cross-disciplinary synthesis.** Adapting educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) to LLM contamination is original. The DIF connection (Holland & Wainer 1993, Zumbo 1999) is technically apt. No prior work has formalized this bridge.

5. **Thorough controlled experimental design.** LoRA-based SFT injection at 4 dosage levels across 3 scales, with 7 baselines and 6 evaluation metrics, represents substantial experimental infrastructure. Cross-family validation with Llama-3.2-1B and 7B scale bridging add breadth.

6. **Honest reporting of negative results.** The paper explicitly does not claim MAE improvement and frames as proof-of-concept. The coverage gap decomposition (>70% from insufficient N, ~20–25% local independence violation, <5% measurement error) is transparent and scientifically valuable.

---

## Agreed Weaknesses

### Major

**M1. Core calibration claim fails — title/framing mismatch with results.**
Both reviewers' top weakness. Mean MAE (0.052) is worse than raw scores (0.034) and linear regression (0.032). Coverage at 95% nominal ranges from 44% (MMLU) to 62.5% (ARC). Only 1 of 4 benchmarks (ARC) shows a significant γ; MMLU fails to converge entirely (R̂ = 1.08, ESS = 85). The paper is titled "Calibrating LLM Benchmark Scores" but the calibration demonstrably makes scores less accurate on average. Despite the honest limitation discussion, the current framing still foregrounds calibration rather than characterization.

**M2. N_models is structurally insufficient for the proposed model.**
With 4PL+γ, each benchmark fit has ~4×N_items + N_models + 1 parameters. For ARC (1,172 items), this is ~4,690 parameters estimated from 16 model response vectors. The paper's own simulation sweep establishes N ≥ 30 as minimum for >80% coverage, yet primary results use N = 16. This is an internal contradiction: the identifiability analysis undermines the paper's own experimental operating point.

**M3. Multi-signal pipeline degrades to S1-only; RRF is empirically vacuous.**
S2 (Min-K++) AUC = 0.465–0.513 (near chance). S4 (Self-Critique) AUC = 0.481–0.519 (near chance). RRF fusion gap over S1-only = 0.001. The multi-signal architecture is theoretically motivated but empirically dominated by a single signal. Furthermore, S3 (ConStat) appears to be described in the method section but was never actually computed — a factual inconsistency that must be corrected.

**M4. Novelty ceiling: the IRT model is standard explanatory IRT with one covariate.**
The 4PL+γ model (Eq. 2) is a direct instantiation of De Boeck & Wilson (2004) with a single external covariate. Per-benchmark γ_k is achieved by fitting separate models per benchmark, not through a novel hierarchical extension. While the application context is new, the methodological contribution is integration rather than innovation.

**M5. Additive γ model potentially misspecifies contamination mechanism.**
The model assumes contamination adds a uniform logit boost/penalty γ·e independent of item difficulty and model ability. But ARC's negative γ reflects catastrophic forgetting during SFT (general capability degradation at 0.5B scale), not item-level contamination effects. The model conflates "training on item X inflates X's score" with "SFT on contaminated data degrades general model behavior." R1 notes these require fundamentally different IRT specifications. R2 acknowledges this is inherent to any single-parameter model but agrees it limits interpretive power.

### Minor

**m1. Closed-weight mode collapses (AUC 0.515).** Without embedding access (the precise scenario for commercial models practitioners most care about), ContamCal is non-functional. This severely limits practical applicability.

**m2. Cross-family validation is weak.** Only Llama-3.2-1B at a single scale. The γ correlation r = 0.85 is computed from 3 data points — no statistical power. Generalization claims beyond Qwen2.5 are premature.

**m3. GSM8K 3B format confound.** Non-monotonic dose-response (35.3% → 20.8% → 74.2%) reflects SFT format effects on chain-of-thought, not contamination. Different LoRA hyperparameters for 3B (lr=5e-5, α=16) vs. 0.5B/1.5B (lr=2e-4, α=32) introduce an asymmetry confounding scale effects with training procedure.

**m4. Simulation sweep incomplete.** Paper claims 120 conditions (review context planned 144). Systematic failures in the AUC = 0.65 conditions at the identifiability boundary undermine the analysis meant to establish that boundary.

**m5. Presentation imbalance.** 16 tables with zero figures. The method is inherently visual — a pipeline diagram, signal AUC heatmap, identifiability phase diagram, and dose-response curves would communicate the story far more effectively.

**m6. MMLU IRT results are unreliable.** R̂ = 1.08, ESS = 85 fail standard convergence criteria. 14K items require subsampling that loses information. Results should be clearly labeled as non-converged.

---

## Questions for Authors (Consensus Priority Order)

1. **Practical value proposition**: Given that calibrated MAE is worse than raw MAE on average, what specifically does ContamCal provide that simpler approaches (e.g., running S1 embedding similarity alone for detection, or linear regression for adjustment) do not?

2. **N contradiction**: Why are primary results reported at N = 16 when the paper's own identifiability analysis establishes N ≥ 30 as minimum? Is this gap acknowledged prominently enough?

3. **γ interpretation**: For ARC, negative γ likely reflects catastrophic forgetting under SFT at 0.5B scale rather than item-level contamination effects. How do you disentangle SFT capacity displacement from the contamination effect γ is designed to capture?

4. **Real-world applicability**: S1 requires access to training data. Without it, detection AUC collapses to 0.515. How do you envision ContamCal being used when training data is unavailable (the common case for frontier models)?

5. **ConStat inconsistency**: Is S3 (ConStat) described in the method section? If so, was it actually computed in the experiments? The paper must be consistent on how many signals were used.

6. **Oracle gap**: S1-only γ amplifies ARC forgetting 2.4× relative to oracle and completely loses GSM8K's positive signal (3.77 → 0.19). What drives this systematic exposure-to-effect mapping bias?

---

## Missing Experiments / Analyses

Both reviewers identified gaps relative to the experimental plan:

1. **SBC (Simulation-Based Calibration) diagnostic** — critical for diagnosing whether coverage collapse stems from model misspecification vs. insufficient N. Listed in experimental protocol but not completed.

2. **Multi-seed pooled IRT at N ≥ 30** — the paper's own identifiability analysis identifies this as the solution to coverage collapse. Not completed.

3. **Verbatim contamination baseline** — all experiments use paraphrased contamination; the most common real-world contamination scenario (verbatim/near-verbatim during pre-training) is never tested.

4. **Item-level γ heterogeneity** — a random-slopes model (γ_j per item group) would test whether the constant γ specification is adequate.

5. **Posterior predictive checks on item residual correlations** — to quantify local independence violation severity.

6. **Hierarchical γ specification** (γ_k ~ Normal(μ_γ, σ_γ)) — could share information across benchmarks and provide a formal heterogeneity test.

---

## Experiment Coverage Assessment

The paper covers most planned experiments from the design document:
- **Well covered**: Signal pipeline (exp-002), RRF ablation (exp-003), IRT calibration (exp-006), 7B bridging (exp-007), signal survival (exp-008), RL observational (exp-009), closed-weight (exp-013), multi-family (exp-014), QC ablation (exp-015)
- **Partially covered**: Simulation sweep (exp-004, 120/144 conditions with systematic failures), noise propagation (exp-005, appendix only)
- **Briefly mentioned**: 72B observational (exp-012, one paragraph)
- **Missing from plan**: SBC diagnostic, multi-seed pooling to N ≥ 30

---

## Path to Improvement

Both reviewers agree the paper could reach **4/6 (Borderline Accept)** with:

1. **Reframe title and narrative** around empirical characterization of contamination behavior within an IRT framework, not around calibration improvement. Lead with signal effectiveness findings and Min-K++ reversal.

2. **Implement figures** — pipeline diagram, signal AUC heatmap, identifiability phase diagram, dose-response curves. Move most tables to appendix.

3. **Complete N ≥ 30 experiments** via multi-seed pooling to demonstrate coverage recovery, validating the paper's own identifiability predictions.

4. **Resolve ConStat inconsistency** — either compute S3 or accurately describe a 3-signal pipeline.

5. **Add SBC diagnostic** to distinguish model misspecification from insufficient N in the coverage gap.

6. **Foreground the Min-K++ reversal** as a primary empirical contribution with standalone value.

---

## Final Assessment

**Score: 3/6 (Weak Reject) | Confidence: High**

The paper addresses a timely problem with substantial experimental infrastructure. The Min-K++ reversal finding, benchmark-dependent contamination characterization, and Fisher Information identifiability analysis are genuine contributions. However, the central calibration claim is not supported by results, the IRT model is standard explanatory IRT without methodological novelty, the multi-signal pipeline degrades to a single signal, and the paper operates below its own recommended identifiability threshold. The honest reporting of limitations is commendable but insufficient to offset the claim-evidence mismatch at a top venue with ~25% acceptance rate. A major revision reframing the narrative around what the results actually demonstrate — systematic empirical characterization rather than calibration — could substantially improve the paper.
