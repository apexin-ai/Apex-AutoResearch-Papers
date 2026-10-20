---
dream_id: dream_20260515T052337
tier: worst
overall_score: 3/6 Reject
timestamp: 2026-05-15T06:35:23.556082+00:00
---

# Dream Review Report: "The Limits of Post-Hoc Contamination Calibration: An IRT-Based Diagnostic Study"

**Dream ID:** 20260515T052337  
**Review Mode:** Full (2 Reviewers + Roundtable)  
**Date:** 2026-05-15

---

## Roundtable Summary

Two reviewers independently assessed the paper, then cross-shared findings and converged on a consensus evaluation.

- **R1 (Methods + Experiments):** Score 3/6, Confidence 4/5
- **R2 (Novelty + Related Work):** Score 3/6, Confidence 4/5
- **Consensus Score: 3/6 (Reject)**
- **Consensus Confidence: 4/5 (High)**

---

## Paper Overview

The paper proposes ContamCal, a two-stage framework that (1) maps item-level contamination provenance via Reciprocal Rank Fusion (RRF) of four detection signals, then (2) fits a 4PL IRT model augmented with per-benchmark contamination parameter γ_k to produce calibrated benchmark scores. Through controlled SFT contamination injection on Qwen2.5-{0.5B, 1.5B, 3B, 7B} and Llama-3.2-1B across MMLU, ARC, GSM8K, and HumanEval, the paper finds that IRT-based calibration fails systematically and reframes its results as three negative contributions: (1) contamination effects are benchmark-dependent and non-monotonic, (2) detection signals exhibit fundamental failure modes including Min-K++ directional reversal, and (3) γ is structurally unidentifiable under typical LLM evaluation conditions.

---

## Consolidated Strengths

### S1. Min-K++ directional reversal is a genuinely novel and actionable finding
**[R1, R2 — strong agreement]**

Cohen's d = −2.11 (MMLU), −1.75 (GSM8K), −2.08 (ARC) at 0.5B d100 shows that contaminated items appear *more* surprising than clean items — the opposite of the theoretical prediction. This is consistent across all three benchmarks (Table 5), ruling out benchmark-specific artifacts. The proposed mechanism (LoRA fine-tuning alters the model's overall softmax calibration, shifting token probability distributions globally) is plausible and well-articulated. This is the paper's most citation-worthy finding and genuinely could not have been trivially predicted from prior work. Practitioners using Min-K++ for contamination detection need to know that it can actively mislead rather than merely fail.

### S2. Honest negative-results framing
**[R1, R2 — strong agreement]**

The pivot from "calibration method" to "diagnostic study of why calibration fails" is intellectually courageous. The paper does not hide its failures — MMLU non-convergence (R̂=1.54, ESS=7) is declared unreportable, GSM8K calibration is shown to be 30× worse than raw baseline, and the coverage collapse is reported transparently. This honest presentation is more valuable than a mediocre positive result.

### S3. Fisher Information analysis is mathematically rigorous
**[R1, R2 — strong agreement]**

The derivation of I(γ_k) for the 4PL+γ model (Eq. 3), establishing structural identifiability (AUC≥0.55) and practical identifiability (AUC≥0.80, N≥50) thresholds, is clean and correct. The exposure–ability collinearity insight — that better exposure signals *increase* CI width because exposure correlates more strongly with correctness — is counter-intuitive and theoretically valuable. This stands as an independent reference contribution for anyone considering IRT-based contamination modeling.

### S4. Benchmark-dependent contamination characterization
**[R1, R2 — agreement with caveats]**

The three-regime characterization is empirically informative: ARC exhibits catastrophic forgetting (−17pp at 0.5B d100), GSM8K is naturally resistant (<1pp change at 0.5B/1.5B), and MMLU effects are negligible at ≥1.5B. The 7B data (Table 2) showing complete MC immunity (≤0.5pp) with HumanEval as the only affected benchmark (+7pp) adds ecological relevance. Cross-family consistency with Llama-3.2-1B (Table 3) shows these patterns are not Qwen-specific.

### S5. Thorough experimental design
**[R1 primarily]**

The controlled SFT injection with known dosage levels, multiple seeds, four model scales, and two model families provides strong internal validity. The 144-condition simulation sweep for identifiability boundaries is well-designed. Seven baselines (including DCR, linear regression, and Emperor's mitigation) provide adequate comparison context. The QC-only ablation ruling out paraphrase quality as a confound is a useful control.

### S6. Well-developed DIF connection
**[R2 primarily]**

The paper correctly identifies γ_k as a uniform DIF parameter and discusses the key difference — continuous exposure estimated with noise vs. discrete demographic categories in classical DIF. The relevant psychometrics citations (Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999) are appropriate.

---

## Consolidated Weaknesses

### W1. (Critical) Coverage collapse is devastating and insufficiently diagnosed
**[R1, R2 — strong agreement]**

The most fundamental problem: 95% CI coverage reaches only 18–63% across all conditions, *including oracle exposure*. Table 12 shows CI width is invariant to measurement error σ_e (0.0997–0.100), and coverage is stuck at 25% regardless of noise level. PPP extremes (ARC oracle = 1.0, GSM8K oracle = 0.0) indicate systematic model misspecification, not merely insufficient N.

The paper attributes coverage failure to "local independence violation and small N" but does not adequately decompose these causes. Possible root causes include: (a) additive γ is the wrong functional form — contamination effects that are item-heterogeneous or non-linear in dosage would violate this assumption; (b) 4PL overparameterization at small N (4·N_items + N_models + 1 parameters vs. 8·N_items observations); (c) cross-scale θ heterogeneity when pooling 0.5B and 1.5B models. The paper should provide simulation-based calibration (SBC) at N=8 to distinguish expected small-sample degradation from structural misspecification.

**Impact:** This undermines Contribution 3 (identifiability analysis), because even when γ IS identifiable (e.g., ARC S1-only γ excludes zero), the calibrated uncertainty quantification is broken. The Bayesian credible intervals — a core selling point — are not usable.

### W2. (Critical) N=8 is far below any reasonable IRT threshold
**[R1, R2 — strong agreement]**

The paper's real-data IRT fits use N=8 models. Standard IRT requires N>200 examinees; even "few-examinee" IRT literature assumes N>20. The paper's own simulation sweep starts at N=20 and shows marginal performance even there. Drawing conclusions about method viability from N=8 fits is problematic — coverage collapse to 25% is entirely expected at this sample size and tells us nothing about whether the method would work at N=50.

The paper acknowledges this (Section 5.3: "N=8–16 models far below the N≥50 threshold") but proceeds to fit IRT models anyway and interpret the results. The simulation sweep should have included N=8 conditions to demonstrate that coverage collapse is *expected* even under correct model specification, which would clarify whether the real-data failures are due to small N alone or also to model misspecification.

### W3. (Major) The "impossibility" result is overstated
**[R2 primarily, R1 concurs]**

Contribution 3 claims an "identifiability impossibility result," but this largely reduces to "IRT estimation is unreliable with <50 examinees" — which is well-established in the psychometrics literature. The key insight is that LLM evaluation inherently cannot provide N≥50 comparable model variants, making IRT-based calibration impractical in this domain. But this is a *mismatch between method requirements and domain constraints*, not a fundamental impossibility of the calibration concept.

The paper should reframe: "The IRT framework requires N≥50 independent models, and LLM evaluation pipelines rarely compare more than 20 models on a single benchmark. This structural mismatch makes IRT-based contamination calibration impractical under current evaluation practices, regardless of implementation quality."

### W4. (Major) SFT artifacts vs. genuine contamination effects are conflated
**[R2 primarily]**

The ARC catastrophic forgetting (−17pp at 0.5B) is a LoRA SFT side effect in a capacity-constrained model, not a contamination-specific phenomenon. Fine-tuning 0.5B on *any* new data might displace existing knowledge. The paper's own QC-only ablation (Section 5.1) shows identical results with high-quality paraphrases, confirming this is a capacity issue, not a data quality issue — but it also suggests it's a fine-tuning issue, not a contamination issue.

At 1.5B and 3B, MC benchmark effects are <2pp — effectively within noise for many conditions. The dramatic "benchmark-dependent heterogeneity" narrative is driven primarily by the 0.5B forgetting and the 3B GSM8K anomalous increase (0.353 → 0.742), which may itself be a LoRA hyperparameter artifact. The true contamination effects — isolating memorization from SFT capacity damage — may be much smaller and more homogeneous than claimed.

### W5. (Major) The multi-signal pipeline (RRF of 4 signals) is effectively a single-signal system
**[R1, R2 — strong agreement]**

Only S1 (embedding similarity) achieves practical detection accuracy, and only at 0.5B. S2 (Min-K++) fails or reverses. S3 (ConStat) appears to have never been fully computed — it is described in the method but all reported values are at chance level. S4 (Self-Critique) is at chance across all conditions. RRF fusion degrades to S1-only mode (exposure correlation r=0.97 per Table 6), offering no benefit over S1 alone.

The paper's Stage 1 is presented as a principled multi-signal aggregation framework, but in practice it is S1-only at 0.5B. This is acknowledged in the discussion ("RRF's value is architectural, not empirical") but the method section still describes a 4-signal system. The discrepancy between the presented framework and what actually works is a significant credibility issue.

### W6. (Major) Linear regression (B4) outperforms ContamCal on the key metric
**[R1 primarily, R2 concurs]**

Table 11 shows that on ARC (the only benchmark where ContamCal shows any positive signal), linear regression achieves 87.5% coverage vs. ContamCal's 62.5%, with only marginally worse MAE (0.056 vs. 0.035) and comparable ranking (τ=0.756 for both). The paper self-identifies this: "A reviewer would rightly ask: 'Why use IRT at all when linear regression provides better-calibrated uncertainty at lower complexity?'" — but does not adequately answer the question. If a simple baseline provides better-calibrated uncertainty, the complex IRT machinery is unjustified even as a diagnostic tool.

### W7. (Moderate) Missing related work
**[R2 primarily]**

The paper omits relevant literature on: (a) verbatim contamination effects (Sainz et al. 2023, Jacovi et al. 2023), which is the more common real-world scenario vs. the paraphrased contamination studied here; (b) data mixing effects during pre-training (Xie et al. 2024, Ye et al. 2024), which frames contamination as a data mixing problem; (c) the growing literature on training data attribution (Pruthi et al. 2020 is cited but influence functions literature is underexplored).

### W8. (Moderate) Closed-weight inapplicability is a severe practical limitation
**[R1, R2 — agreement]**

S1 requires model weights. The closed-weight 2-signal mode (S3+S4) produces MAE=0.142, worse than the raw baseline of 0.059 (Table 6). For the models most relevant to practitioners (GPT-4, Claude, Gemini), ContamCal is completely inapplicable. This severely limits the paper's practical impact, even if the diagnostic findings about open-weight models retain value.

### W9. (Minor) No supplementary material
**[R2 primarily]**

A 12-page paper of this technical depth — with Fisher Information derivations, SBC diagnostics, simulation sweep details, Stan model specifications, and multiple ablations — needs supplementary material. Key details are either compressed into brief text mentions or entirely absent from the paper.

---

## Questions for Authors

1. **Coverage root cause decomposition:** Your simulation sweep at N=50/AUC=0.80 shows reasonable coverage, but real-data fits at N=8 show 18–63%. Can you run the simulation sweep at N=8 to determine how much of the coverage collapse is expected from small N alone vs. model misspecification? What does SBC at N=8 show?

2. **Additive γ misspecification:** GSM8K oracle γ=3.77 is significant but MAE=0.092 is 30× worse than raw MAE=0.003. Have you considered item-level contamination effects (γ_ij instead of γ_k) or non-linear contamination functions? The additive logit shift seems fundamentally wrong for benchmarks where contamination creates qualitative capability changes.

3. **SFT vs. contamination:** After subtracting baseline SFT effects, how large are the true contamination-specific effects on MC benchmarks at 1.5B/3B? If they are <2pp (as the data suggests), doesn't this mean contamination calibration is solving a non-problem for these scales?

4. **S1 scope:** S1 requires access to model weights AND the training corpus (for paraphrase generation). For which real-world use cases is this combination available? Does this limit ContamCal to a retrospective diagnostic tool rather than a practical calibration method?

5. **Cross-family correlation:** Table 3 reports cross-family γ correlation of 0.45, which suggests contamination susceptibility is a model×benchmark interaction, not a benchmark property. With only 3 benchmarks, what is the statistical power of this comparison? Does this undermine the per-benchmark γ_k formulation?

6. **RL signal completeness:** Are the RL-post-trained model results (Table 7) from completed experiments or partially extrapolated? The total absence of signal (all AUC < 0.55) is a strong claim that requires verified data.

7. **Why not N=8 in the simulation?** This is the most obvious gap: your actual experimental condition (N=8) is not represented in the identifiability sweep (minimum N=20). Adding this would directly calibrate expectations for your real-data results.

---

## Minor Issues

- Table 1 reports some conditions with single-seed data (no ± std) — these should be marked or excluded from quantitative claims
- The prior on γ_k ~ N(0, 2) needs sensitivity analysis reported in the paper, not just mentioned
- HumanEval appears in Table 1 despite 17.3% paraphrase QC pass rate and relegation to appendix — either include it consistently or exclude it from main tables
- The measurement error extension (Section 3.2) introduces N_models × N_items latent τ parameters, making it computationally infeasible for large benchmarks — this scalability issue should be discussed
- The "per-benchmark γ_k" is obtained by fitting separate IRT models, not a hierarchical model — the paper should clarify that γ values across benchmarks cannot be formally compared
- 72B observational results (Section 5.2) lack ground-truth contamination status — the null finding (all signals at chance) is interpretable but the γ estimates are unvalidated

---

## Experiment Coverage Assessment

Comparing the paper against the imagined experiment list:

| Experiment | Status in Paper | Coverage Quality |
|---|---|---|
| exp-001 (SFT injection) | Tables 1, 2 | Full |
| exp-002 (signal pipeline) | Tables 4, 5 | Full |
| exp-003 (RRF ablation) | Table 6 | Full |
| exp-004 (simulation sweep) | Tables 8, 9 | Full but missing N=8 |
| exp-005 (noise propagation) | Table 12 | Full |
| exp-006 (IRT calibration) | Tables 10, 11 | Full |
| exp-007 (7B bridging) | Table 2 | Full |
| exp-008 (signal survival) | Tables 4, 5, 7 | Full |
| exp-009 (RL observational) | Tables 7, 13 | Full |
| exp-012 (72B observational) | Text mention | Compressed |
| exp-013 (closed-weight) | Table 6, text | Compressed |
| exp-014 (multi-family) | Table 3 | Full |
| exp-015 (QC-only ablation) | Text mention | Compressed |

All imagined experiments are represented. Coverage is generally thorough, though exp-012, exp-013, and exp-015 are compressed into brief text rather than receiving full table treatment. The missing N=8 simulation condition (exp-004) is the most significant gap.

---

## Final Assessment

### Score: 3/6 (Reject)
### Confidence: 4/5 (High)

### Verdict

The paper tackles a genuinely important problem — whether post-hoc statistical methods can correct for benchmark contamination in LLM evaluation — and arrives at a valuable negative answer. The Min-K++ directional reversal finding (Cohen's d = −1.98) is novel, actionable, and would change practitioner behavior. The Fisher Information analysis is mathematically rigorous. The benchmark-dependent contamination characterization (ARC forgetting, GSM8K resistance, MMLU immunity at scale) provides a useful empirical taxonomy.

However, the paper falls short of the acceptance bar for three reasons:

1. **The negative results are not sufficiently surprising.** The core "impossibility" — that IRT estimation fails with N=8 models — is expected by anyone familiar with psychometric estimation requirements. The real insight (LLM evaluation inherently cannot provide N≥50) is important but could be stated in a paragraph, not derived through a 144-condition simulation sweep.

2. **The SFT-vs.-contamination confound weakens the strongest empirical claim.** The benchmark-dependent heterogeneity narrative is driven by SFT capacity artifacts (0.5B forgetting) and LoRA hyperparameter effects (3B GSM8K anomaly), not by genuine contamination dynamics. True contamination effects on MC benchmarks at ≥1.5B appear to be <2pp — possibly too small to calibrate regardless of method.

3. **The framework as presented does not match what works in practice.** The paper describes a 4-signal RRF pipeline, but only 1 signal works, only at one scale, and only with model weights available. Linear regression provides better-calibrated uncertainty on the only benchmark where ContamCal shows positive results. The gap between the presented framework and its actual operational reality undermines credibility.

### Path to Acceptance

The paper could reach borderline-accept (4/6) by: (a) leading with signal failure characterization (Min-K++ reversal) rather than calibration failure; (b) cleanly separating SFT capacity artifacts from contamination effects with appropriate controls; (c) including N=8 simulation conditions to calibrate expectations; (d) being fully transparent that the pipeline is S1-only in practice; (e) adding supplementary material with Fisher Information proofs, SBC diagnostics, and full ablation tables.