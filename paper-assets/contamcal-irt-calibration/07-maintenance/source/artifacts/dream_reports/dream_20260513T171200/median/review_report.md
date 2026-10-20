---
dream_id: dream_20260513T171200
tier: median
overall_score: 5 — Marginally Below Acceptance Threshold (Borderline Reject)
timestamp: 2026-05-13T18:09:03.582593+00:00
---

# Dream Review Report — ContamCal: Calibrating LLM Benchmark Scores via Contamination-Augmented Item Response Theory

**Dream ID**: 20260513T171200
**Review Mode**: Full (2 Reviewers, 4-Step Roundtable)
**Target Venue**: AAAI 2027 (using AAAI-26 standards, 1–10 scale, ~17.6% acceptance rate)

---

## Consolidated Assessment

**Overall Score: 5/10 — Marginally Below Acceptance Threshold**

Both reviewers independently converge on 5/10. The paper addresses a genuine and important gap — no existing method produces calibrated benchmark scores with proper uncertainty quantification under contamination. The signal survival analysis is a genuinely novel empirical finding. However, the core calibration claim rests on statistically marginal evidence, the uncertainty quantification is systematically miscalibrated (87% vs 95% nominal), methodological novelty is primarily integrative rather than fundamental, and practical utility is constrained to small open-weight SFT models — precisely the regime where contamination is least consequential for the community.

---

## R1 Review: Methods + Experiments

### Summary
The methodological framework is intellectually coherent, grounded in item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004). The anti-circularity argument for RRF and the measurement error model are well-motivated. However, statistical evidence for superiority over simpler alternatives is weak, the persistent 8pp coverage gap undermines the UQ claim, and controlled experiments are limited to small models (≤7B) with a single non-Qwen family.

### Strengths (Methods)
1. **Principled theoretical grounding.** The 4PL IRT + γ_k + measurement error formulation has clear psychometric roots. The three structural adaptations for LLM evaluation (shared item pool, continuous exposure, regime-conditional ability) are non-trivial and well-motivated.
2. **Anti-circularity argument for RRF is compelling.** Supported by both theoretical reasoning and empirical evidence (calibration-weighted RRF yields only +1pp, Table 4).
3. **Measurement error model is architecturally necessary.** Regime-conditional σ_e (0.18 SFT, 0.41 RL) naturally produces appropriately wider CIs without manual tuning.
4. **Per-benchmark γ_k is empirically validated.** GSM8K (0.51) > MMLU (0.42) > ARC (0.35) > HumanEval (0.19) captures genuine heterogeneous susceptibility.
5. **Fisher Information analysis** distinguishes structural (AUC≥0.58) from practical (AUC≥0.68) identifiability — elevates the threshold from rule-of-thumb to theoretically justified.

### Strengths (Experiments)
1. **Comprehensive controlled injection.** 45 SFT runs, 3 scales, 5 dosage levels, 3 seeds, quality-validated paraphrases.
2. **Signal survival analysis is genuinely novel.** The signal×regime AUC heatmap (Table 3) has standalone value for the detection community.
3. **7 baselines** span the full spectrum of existing approaches.
4. **Near-zero γ check** validates specificity (γ=0.04, CI includes zero on clean benchmark).
5. **Transparent negative results.** Dose-response plateau, HumanEval failure, RL wide CIs, 2-signal degradation all honestly reported.

### Weaknesses (Methods)
1. **(Major) Local independence violation inadequately addressed.** The fundamental IRT assumption is violated when a single LLM produces all responses. Residual correlations (mean 0.12, max 0.23) are systematic, not moderate. The residual 7pp coverage gap is directly attributable. No formal analysis quantifies expected coverage under observed violation levels. This undermines the UQ claim (Claim 1).
2. **(Major) Additive γ specification may be misspecified.** The constant contamination effect on the logit scale regardless of item difficulty is challenged by dose-response non-monotonicity at 25%→50% and large cross-benchmark γ_k variation (0.19–0.51). A γ×difficulty interaction or hierarchical γ model may be needed.
3. **(Moderate) 4PL heavily parameterized for available data.** With N_models ~15–50, estimating 4 item parameters per item plus γ from limited "examinees" strains the model. HumanEval's failure (N=164, CI spanning zero) is a symptom.
4. **(Moderate) Counterfactual "exposure=0" calibration lacks causal identification.** Setting τ=0 to recover "clean" scores depends on correct model specification. If γ is estimated with bias (θ-γ posterior correlation -0.38 at AUC=0.70), the counterfactual inherits this bias.
5. **(Minor) NUTS scalability.** 35 min/benchmark for MMLU's 14K items limits practical deployment.

### Weaknesses (Experiments)
1. **(Major) Marginal/absent statistical significance for key comparisons.** DCR: p=0.042 (would not survive Bonferroni correction across 7 baselines). Linear regression: p=0.087 (not significant). The claim of "significantly outperforming seven baselines" is overstated — 5/7 are beaten, but the two most relevant (DCR, linear regression) have thin evidence. The 1.0pp MAE advantage over DCR (3.1 vs 4.1) is practically meaningful but statistically fragile.
2. **(Major) Scale limitation.** Controlled experiments cover 0.5B–7B only. Models of greatest practical interest (70B+) yield inconclusive observational results (Table 15). The framework may primarily solve a problem for small models where contamination is less consequential.
3. **(Major) Single non-Qwen family is insufficient.** Llama-3.2-1B shows 1.8pp MAE gap, 5pp coverage gap, 0.05 AUC gap. These are substantial and suggest family-dependent performance. One non-Qwen family cannot establish generalizability.
4. **(Moderate) Coverage gap 87% vs 95% nominal is systematic.** Credible intervals are permanently miscalibrated. The measurement error model halves the gap (14pp→7pp) but cannot close it.
5. **(Moderate) Dose-response non-monotonicity** in 2/12 conditions (MMLU-3B, ARC-3B at 25%→50%) — the "marginal memorization return" explanation is post-hoc and unverified.
6. **(Moderate) RL case study evidential value is limited.** 8% convergence issues, RRF AUC 0.56 barely above identifiability threshold, CI widths 10.5–18.0pp. The 55% regret reduction is compelling but the wide CIs carry very little information. "Wide CIs are the correct answer" is defensible but unfalsifiable.
7. **(Moderate) HumanEval invalidates 1/4 benchmark claims.** N=164 insufficient for 4PL+γ. Paper correctly notes this but should not count HumanEval in headline results.
8. **(Minor) No principled model selection** between per-benchmark γ_k and global γ (e.g., WAIC, LOO-CV).

### R1 Questions for Authors
1. Formal analysis of expected coverage gap given observed residual correlations (mean=0.12, max=0.23)?
2. Have you tested γ×difficulty interaction to address dose-response non-monotonicity?
3. Computational cost of the full pipeline for a single benchmark?
4. Was the signal pipeline recalibrated for Llama's tokenizer/embedding space?
5. Could DCR with bootstrap CIs enable fair coverage/sharpness comparison?
6. Why was SBC (Talts et al. 2018) not used to validate posterior inference?
7. Were the 8% convergent-failure RL models excluded from regret analysis?

### R1 Scores
- Soundness: 5/10
- Experiments: 5/10
- Overall: 5/10
- Confidence: 4/5

---

## R2 Review: Novelty + Related Work

### Summary
The paper fills a structural gap — bridging detection signals to calibrated scores with UQ — but the novelty is primarily integrative. Each component (RRF, 4PL IRT, measurement error, Bayesian inference) is borrowed from existing literature. The three structural adaptations from educational IRT are individually either standard or engineering decisions. The signal survival analysis is the most genuinely novel finding but remains descriptive rather than explanatory. Several important related work areas (DIF literature, ML calibration disambiguation, conformal prediction, data attribution) are underengaged.

### Strengths (Novelty)
1. **Detection-to-calibration bridge** is a genuine conceptual contribution. No prior work answers "what would the score be absent contamination?" with proper UQ.
2. **Signal survival analysis** is genuinely novel and independently valuable — the systematic signal×regime AUC mapping has not been done before.
3. **Measurement error model** for noisy exposure propagation through IRT posteriors is a non-trivial design element, even if errors-in-variables modeling is classical.
4. **Meta-circularity argument** for RRF shows intellectual honesty — positioning it as a design choice rather than a contribution.
5. **Per-benchmark γ_k** captures heterogeneous susceptibility with empirical validation.

### Strengths (Related Work & Positioning)
1. Related work covers contamination detection (8 methods), mitigation, IRT for LLM evaluation, and item compromise literature comprehensively.
2. Emperor's New Clothes (Xu et al. 2024) is well-leveraged as paradigm-shift motivation.
3. Educational measurement roots properly credited (Eckerly, Sinharay, De Boeck & Wilson, Mislevy).
4. DCR appropriately positioned as closest predecessor with fair distinction (lacks UQ and RL handling).
5. Honest limitation framing enhances credibility ("wide CIs are correct behavior, not limitation").

### Weaknesses (Novelty)
1. **(Moderate) Core IRT model is a direct application of item compromise IRT.** The contamination-augmented 4PL adds a single linear covariate — precisely what Eckerly (2017) and Sinharay (2017) do. A psychometrician would recognize Stage 2 as routine explanatory IRT fitting. The adaptations are necessary but individually standard.
2. **(Moderate) RRF is an off-the-shelf technique** applied straightforwardly from information retrieval (Cormack et al. 2009). The meta-circularity argument justifies the choice but does not make it a contribution.
3. **(Moderate) Signal survival analysis is descriptive, not explanatory.** Why RL erases embedding fingerprints but not meta-cognitive signatures is asserted but not validated. Without testing across different RL algorithms (PPO vs GRPO vs DPO), the generalizability of the degradation pattern is assumed.
4. **(Minor) "Dual-track validation" is experimental design, not a contribution.** Using both controlled and observational experiments is standard practice, not a separate contribution.
5. **(Minor) Identifiability simulation is standard SBC** — methodological due diligence, not a contribution. Fisher Information derivation is missing, preventing verification of the AUC≥0.68 threshold.
6. **(Minor) Causal inference analogy is undeveloped.** No DAG, no formal identification argument, no sensitivity analysis for unmeasured confounding.

### Weaknesses (Related Work & Positioning)
1. **(Major) Missing engagement with Differential Item Functioning (DIF) literature.** The γ_k parameter essentially measures DIF between exposure groups. Holland & Wainer (1993), Thissen et al. (1993), Zumbo (1999) are the direct statistical predecessors and are entirely absent. Significant omission given the psychometric grounding claimed.
2. **(Moderate) No disambiguation from ML calibration.** "Calibration" in ML means probability calibration (Guo et al. 2017, Platt 1999). The paper uses it for decontamination adjustment. This ambiguity will confuse AAAI reviewers.
3. **(Moderate) Missing discussion of conformal prediction** (Angelopoulos & Bates 2023) as alternative UQ with distribution-free coverage guarantees — potentially attractive given IRT's local independence assumption issues.
4. **(Moderate) Data attribution methods not considered** as alternative exposure signals (TracIn, TRAK, influence functions).
5. **(Minor) Multidimensional IRT not discussed.** Unidimensional θ for MMLU (57 subjects) is questionable.
6. **(Minor) Broader benchmark ecosystem** (HELM, BIG-bench, Chatbot Arena) underengaged.
7. **(Minor) San Martin et al. (2009)** directly relevant to identifiability analysis but underutilized.

### R2 Questions for Authors
1. How does ContamCal relate to DIF analysis? Is γ_k measuring DIF between exposure groups?
2. Sensitivity to unmeasured contamination channels (undetected by all four signals)?
3. Would signal degradation pattern hold for PPO, DPO, or other RL variants?
4. Why Bayesian CIs over conformal prediction?
5. Can you provide the Fisher Information derivation?
6. Is unidimensional θ defensible for MMLU's 57 subjects?
7. How are per-benchmark θ estimates reconciled for cross-benchmark comparison?

### Missing References (Critical)
- Holland & Wainer (1993), Thissen et al. (1993), Zumbo (1999) — DIF literature
- Guo et al. (2017) — ML calibration disambiguation
- Angelopoulos & Bates (2023) — conformal prediction as alternative UQ
- Pruthi et al. (2020), Park et al. (2023) — data attribution as alternative exposure signals

### R2 Scores
- Novelty: 5/10
- Related Work: 5/10
- Clarity: 6/10
- Overall: 5/10
- Confidence: 4/5

---

## Roundtable Convergence (Step 3)

### Areas of Agreement
1. **Overall: 5/10 (borderline reject).** Both reviewers independently arrive at the same score.
2. **Signal survival analysis is the strongest contribution** — genuinely novel, independently valuable.
3. **Local independence violation is the fundamental methodological concern** — systematic, inadequately addressed, directly causes the 8pp coverage gap.
4. **Marginal statistical significance** for the two most relevant baselines (DCR, linear regression) weakens the core calibration superiority claim.
5. **Novelty is primarily integrative** — competent assembly of existing techniques for an important new application.
6. **Honest reporting** of limitations is commendable and unusual.
7. **Scale limitation** (controlled ≤7B, observational 72B inconclusive) constrains practical impact.

### Areas of Disagreement
- R1 weights scale limitation and model misspecification (additive γ) more heavily
- R2 weights missing related work (DIF, ML calibration) and descriptive nature of signal survival more heavily
- Both agree these are moderate-to-major concerns; the disagreement is on relative importance

### What Would Move This to Accept
1. **Stronger statistical evidence**: More seeds/conditions to achieve p<0.01 vs DCR, or a new comparison metric where ContamCal clearly dominates (e.g., decision-theoretic regret in SFT regime)
2. **Address coverage gap formally**: Derive expected coverage under measured local independence violation; or adopt a method with formal coverage guarantees (conformal prediction)
3. **Deeper signal survival analysis**: Mechanistic explanation + testing across RL algorithms
4. **Engage DIF literature**: Formal connection to established psychometric framework
5. **Larger scale controlled experiments**: At least 13B controlled, ideally 70B
6. **Additional model families**: At least 2–3 non-Qwen families with recalibrated signals

---

## Final Recommendation

**Score: 5/10 — Marginally Below Acceptance Threshold**

The paper addresses a genuine gap in the LLM evaluation landscape and proposes a principled framework grounded in established psychometric theory. The signal survival analysis is a valuable empirical contribution. However, for AAAI at 17.6% acceptance rate, the paper needs either (a) stronger statistical evidence for calibration superiority, (b) deeper methodological novelty beyond integration, or (c) broader empirical validation. The most promising path to acceptance is reframing around signal survival + identifiability diagnostics as primary contributions, with the calibration pipeline as application, and addressing the DIF literature gap and coverage miscalibration formally.

**Verdict: Borderline reject. Resubmission with targeted revisions could yield acceptance.**

---

## Experiment Coverage Assessment

Comparing against `review_context.yaml` imagined experiments:

| Experiment | Status in Paper | Coverage |
|---|---|---|
| exp-001: Controlled SFT injection | Fully covered (Table 1, §4.1, §5.1) | ✓ Complete |
| exp-002: Stage 1 signal pipeline | Fully covered (Table 2, §5.2) | ✓ Complete |
| exp-003: RRF aggregation ablation | Fully covered (Table 4, §5.4) | ✓ Complete |
| exp-004: Simulation identifiability sweep | Fully covered (Tables 10–11, §5.9) | ✓ Complete |
| exp-005: Noise propagation / ME model | Fully covered (Table 7, §5.6) | ✓ Complete |
| exp-006: IRT calibration + baselines | Fully covered (Tables 5–6, §5.5) | ✓ Complete |
| exp-007: Scale bridging 7B | Fully covered (Table 8, §5.7) | ✓ Complete |
| exp-008: Signal survival analysis | Fully covered (Table 3, §5.3) | ✓ Complete |
| exp-009: RL observational case study | Fully covered (Tables 12–13, §5.10) | ✓ Complete |
| exp-012: 72B observational | Fully covered (Table 15, §5.12) | ✓ Complete |
| exp-013: 2-signal closed-weight mode | Fully covered (Table 14, §5.11) | ✓ Complete |
| exp-014: Multi-family (Llama) | Fully covered (Table 9, §5.8) | ✓ Complete |

**Coverage: 12/12 imagined experiments present in paper.** All experiments from the design are reflected in the manuscript. The paper is comprehensive in its experimental coverage relative to the design plan.
