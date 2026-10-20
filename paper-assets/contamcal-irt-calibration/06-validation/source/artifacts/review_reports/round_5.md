---
round: 5
overall_score: 3.0 - Findings
timestamp: 2026-05-18T05:06:38.292818+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 6

**Paper**: "Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study"
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 写作质量)
**Overall Score**: 3.0 / 5 (Findings)
**Confidence**: 4 / 5

---

## Summary

The paper investigates whether IRT can separate genuine ability from contamination artifacts on LLM benchmarks. Using controlled SFT injection across Qwen2.5 (0.5B–3B) and three benchmarks (MMLU, ARC, GSM8K), the authors develop ContamCal, a two-stage pipeline combining multi-signal item filtering (RRF) with a contamination-augmented IRT model (2PL+γ). The core finding is a null result: SFT-injected contamination shifts aggregate accuracy by only ~0.6–0.7pp, smaller than the estimation noise of any correction method. Signal-guided filtering improves IRT calibration; Min-K%++ exhibits directional reversal at 0.5B; domain-level γ analysis reveals a suggestive signal in Social Sciences (P(γ&lt;0)=99.1%, uncorrected). Simulation establishes J≥50 as the threshold for reliable γ recovery.

---

## Strengths

**S1. Research question is timely and well-defined.** Directly quantifying contamination's aggregate effect size fills a genuine gap where detection proliferates but measurement is absent. The question-driven framing in Introduction is well-constructed.

**S2. Honest null result without overclaiming.** The finding that raw accuracy outperforms all correction methods (Table 1) is presented transparently, with careful analysis of *why*. DCR's systematic overcorrection (MAE=0.108) is a compelling cautionary example.

**S3. Identifiability simulation study (Section 5.3, Figure 2).** The J≥50 at AUC≥0.55 threshold provides an actionable design guideline for the IRT-for-LLM community. Posterior CI width scaling as J^{-0.48} validates theoretical expectations. This has independent methodological value.

**S4. Min-K%++ directional reversal (Section 5.2).** Cohen's d = -1.55 to -1.98 at 0.5B is a striking finding with direct practical implications for detection pipeline design.

**S5. Controlled experimental design.** Within-family SFT injection with 4 dosage levels × 2 seeds × 3 scales provides ground-truth labels unavailable in naturalistic studies.

**S6. RRF meta-circularity argument.** Rank-based fusion avoiding learned aggregation that would require contamination labels is a sound design choice, well-justified.

**S7. Bayesian inference methodology.** NUTS/Stan, 4 chains, Rhat&lt;1.01, ESS>400, PPP diagnostics, and prior sensitivity analysis represent rigorous practice.

**S8. Writing quality.** Clean prose without AI writing markers. Limitations section is unusually thorough (9 items).

---

## Weaknesses

### Must-Fix (4 items — unanimous consensus)

**MF1. [Scope-Claim Gap] Title asks a general question; experiments answer a narrow one.** [R1-N1, R2-N2, unanimous AGREE]

The title "Does LLM Benchmark Contamination Need Calibration?" implies a general answer, but experiments cover only LoRA SFT injection at ≤3B (Qwen2.5 + exploratory Llama-3.2-3B). Pretraining contamination differs mechanistically: full-parameter optimization over many steps embeds contamination into representations, unlike LoRA adapters. The paper's Limitations (para 7) and Conclusion (para 3, "The framework applies directly to settings with larger effects...with no methodological changes") acknowledge the gap but the title does not. ≤3B models have lower baseline accuracy (MMLU ~0.55–0.65), potentially insufficient memorization capacity to produce aggregate effects.

**Required action**: (a) Modify title to scope the claim; (b) Remove or caveat Conclusion's "applies directly" unsupported forward claim.

**MF2. [Oracle Ablation / γ Misspecification] Even perfect detection labels yield non-significant γ — model specification not adequately addressed.** [R1-N2, R2-N3, unanimous AGREE]

Oracle ablation (AUC=1.0) produces MMLU γ = -0.012 (CI [-0.145, 0.119]). Two explanations offered: (a) effect heterogeneity (opposing domain directions cancel), (b) linear γ misspecification (threshold contamination dilutes linear coefficient). These have fundamentally different implications: (a) supports domain-level analysis; (b) undermines the 2PL+γ framework. The paper frames oracle ablation as "confirms that filtering is not circular" (Section 5.1 para 5), sidestepping the model specification question.

**Required action**: Test threshold DGP in the existing simulation framework (generate data with step-function contamination, fit linear γ, report attenuation pattern). Low computational cost, high diagnostic value.

**MF3. [Technical Novelty] 2PL+γ is standard explanatory IRT/DIF applied to a new domain.** [R2-N1, R1 AGREE in cross-response]

The paper self-acknowledges γ "is formally an instance of explanatory DIF" (Section 2 para 3). The three claimed adaptations (continuous exposure, domain stratification, counterfactual inference) are standard DIF practices. RRF is a mature IR technique. Han et al. (EACL 2026) differentiation uses "calibration focus" as a distinguishing axis, but this is self-undermining since Table 1 shows calibration doesn't improve over raw accuracy.

**Required action**: Commit to empirical study positioning; elevate identifiability analysis (J≥50) as lead contribution; reposition Han et al. differentiation around controlled testbed + identifiability thresholds + signal failure characterization.

**MF4. [J=13 Domain Conclusions vs. J≥50 Standard] Internal inconsistency in presentation weight.** [R1-N3, R2 AGREE with nuance]

The paper establishes J≥50 for reliable γ recovery (Section 5.3), then presents domain-level γ at J=13 (Section 5.4) with Social Sciences P(γ&lt;0)=99.1% in the Abstract. While "exploratory" caveats exist, their presentation weight does not match: Figure 3 and Table 4 occupy significant visual space. J=16 results (Appendix Table 4: P(γ&lt;0)=99.7%, passing Bonferroni 99.375%) are available but unused in main text. R2 notes "self-contradiction" overstates but weight mismatch is real.

**Required action**: (a) Use J=16 in main text; (b) Reduce domain γ prominence in Abstract (currently reads as key finding, should be secondary observation).

### Should-Fix (8 items)

**SF1. [Diagnostic Value Evidence Thin]** 1/8 domains significant, uncorrected, at underpowered J. "ContamCal's value lies in this decomposition" (Section 5.1 para 4) rests on one domain. Recommend reframing as "suggestive finding." Hierarchical IRT (Gelman 2012, cited but not implemented) would provide principled shrinkage. [R2-W2, R1 overlap, both AGREE]

**SF2. [SFT Data Composition Confound]** Paper does not specify whether benchmark items replace or augment general SFT data. If replacement, 0.6–0.7pp is contamination benefit minus capability loss; "model-free observation" attribution is imprecise. [R1-W6, R2 AGREE]

**SF3. [CI Coverage Diagnosis Incomplete]** MMLU over-coverage (50% CI: 83%) = uninformatively wide posteriors; ARC under-coverage (50% CI: 45%) = structural misfit. Paper lumps as "benchmark-dependent" without separate diagnosis, weakening uncertainty quantification claims. [R1-W4, R2 AGREE]

**SF4. [RRF Selection Bias / MAE Control Missing]** Random 300-item subsets report τ but no MAE. 300/14042 (2%) means extreme tail items; MAE comparison needed to assess whether filtering improves calibration accuracy or only rank correlation. [R1-W5, R2 AGREE]

**SF5. [Contribution 2 Framing Mismatch]** Signal filtering + Min-K%++ reversal partially disconnected from main question. R1 partial rebut: filtering is pipeline prerequisite. **Consensus**: reframe as "enabling analysis + standalone practical finding" rather than parallel contribution. [R2-W3, R1 partial REBUT]

**SF6. [J Value Narrative Coherence]** 7 different J values across analyses without cohesive overview at Section 5 entry. Social Sciences mixes J=13 (main text) and J=16 (appendix). [R2-W5, R1 AGREE]

**SF7. [k Index Overloading]** Same symbol changes meaning between Section 3.1 (k = benchmark) and Section 3.3 (k = stratum). Parenthetical clarification insufficient; use different symbol. [R2-W4, R1 AGREE]

**SF8. [Missing References]** Camilli &amp; Shepard (1994), Swaminathan &amp; Rogers (1990) for DIF foundations; Xu et al. (2024) "Benchmarking Benchmark Leakage"; Li et al. (2024) "Task Contamination" AAAI. [R1+R2 combined]

### Minor Issues (6 items, all agreed)

- M1: Abstract numeric density still high (~6+ quantitative claims); keep only ~0.6–0.7pp and J≥50
- M2: S4 (Self-Critique) computation details insufficient for reproduction
- M3: Appendix E (ARC, J=8, S1-only) cross-configuration comparability limited
- M4: SFT training curves not reported (convergence verification missing)
- M5: Within-family GSM8K PPP not reported
- M6: Page count near limit; compile and verify ≤8 pages main content

---

## Reviewer Consensus

Both reviewers independently converge on four critical themes:

1. **Scope-claim gap is the primary weakness**: Title asks a general question; experiments answer a narrow one. Unanimous.
2. **Oracle ablation is a methodological red flag**: Linear γ misspecification cannot be ruled out. Threshold simulation test is the agreed resolution path. Unanimous.
3. **Technical novelty is limited**: Standard IRT/DIF application. Paper should commit to empirical study positioning. Unanimous.
4. **Domain-level conclusions exceed statistical warrant**: J=13 &lt; J≥50, 1/8 significant, uncorrected for multiplicity. Unanimous.

## Reviewer Divergence

Two minor divergences (neither affects overall assessment):

1. **Contribution 2 framing (R2-W3)**: R1 partial rebut — signal filtering is a necessary pipeline component. **Resolution**: Both agree on reframing as "enabling analysis" rather than removing content.
2. **Cross-family caveat adequacy (R1-W2)**: R2 partial rebut — paper has explicit "exploratory" labels. R1's concern about missing MAE CI is valid but does not rise to the level suggested.

---

## Questions to Authors

1. Have you tested non-linear γ specifications (threshold, interaction)? Can you run the threshold DGP simulation?
2. Does SFT injection replace or augment general training data? What is the effective training set composition at each dosage?
3. Are SFT training curves available? Did all configurations converge?
4. What is within-family GSM8K's PPP?
5. When S1 is unavailable (closed-source models), what is S2+S4-only RRF performance at 1.5B+?
6. Can hierarchical IRT be implemented for camera-ready, or is it a future-work item?

---

## Missing References

- **Camilli &amp; Shepard (1994)**: DIF methodology classic (R2)
- **Swaminathan &amp; Rogers (1990)**: Logistic regression DIF with continuous covariates (R2)
- **Xu et al. (2024)**: "Benchmarking Benchmark Leakage in LLMs" (R1)
- **Li et al. (2024)**: "Task Contamination: Language Models May Not Be Few-Shot Anymore" AAAI (R1, R2 partial agree)
- **Roberts et al. (2025) or similar**: IRT identifiability with small J (R2)

---

## External Review (Stanford Agentic Reviewer)

Not requested (no external review configuration for this project).

---

## Overall Assessment

**Score: 3.0 / 5 (Findings)**
**Confidence: 4 / 5**

Both reviewers independently rate 3.0 (Findings). The paper presents a well-executed empirical study with an honest null result under controlled conditions, rigorous Bayesian methodology, and valuable side findings (identifiability thresholds, Min-K%++ reversal). However, four converging weaknesses prevent main conference recommendation:

1. The null finding's scope (SFT ≤3B) is too narrow to answer the question the title poses, and the most relevant contamination scenario (pretraining) is entirely unaddressed.
2. The oracle ablation exposes a potential fundamental model misspecification that the paper does not resolve.
3. Technical novelty is limited to standard IRT/DIF application.
4. The strongest empirical finding (domain-level γ) is undermined by the paper's own identifiability analysis (J=13 &lt;&lt; J≥50).

The identifiability analysis (J≥50 threshold) and Min-K%++ reversal documentation have standalone community value and support Findings-level acceptance. The controlled experimental design and transparent null result reporting are commendable. With scope expansion (7B+, ideally pretraining), threshold simulation for model specification, and tighter framing, this work could reach Conference level in a future cycle.

---

## Detailed Comments

### Abstract
- Reduce numeric density: keep only ~0.6–0.7pp and J≥50; replace Δτ, Cohen's d, P(γ&lt;0) with qualitative
- "Social Sciences shows a negative γ effect with high posterior confidence" overstates an exploratory finding

### Introduction
- Para 1–3 question-driven framing is well-constructed
- C1 should lead with identifiability analysis, not bury it in second sentence
- C2 should be reframed as "enabling analysis" + "standalone practical finding"
- "Additionally" paragraph should be further de-emphasized

### Method
- Fix k index: use different symbol for domain/stratum
- Add S4 computation details (prompt design, evaluation distribution)
- Fisher information argument is sound; add citation to IRT identifiability literature

### Experimental Setup
- Clarify SFT injection data composition (replacement vs augmentation)
- Report SFT training curves or convergence verification
- Consolidate model set overview early in Section 5

### Results
- Report MAE for random 300-item subsets alongside τ
- Reposition oracle ablation from "circularity check" to "model specification stress test"
- Switch to J=16 domain results in main text
- Report within-family GSM8K PPP
- Provide explicit CI coverage root-cause diagnosis (MMLU: data-to-prior ratio; ARC: structural misfit)

### Conclusion
- Remove "The framework applies directly to settings with larger effects...with no methodological changes" (unsupported)
- Strengthen diagnostic value caveats

---

## Issue Tracker Sync

Updated `review_issues.yaml`: 21 issues total (3 resolved, 18 open/in_progress). 4 new issues added (R6-W1 through R6-W4). All existing open issues re-evaluated; R4-W2 (Min-K++ causal) candidate for resolution (not re-raised). Key action items for this round: threshold DGP simulation, title scoping, J=16 switch, Abstract numeric reduction, SFT composition clarification.