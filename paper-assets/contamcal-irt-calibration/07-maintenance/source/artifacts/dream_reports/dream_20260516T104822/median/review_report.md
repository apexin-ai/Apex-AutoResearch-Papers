---
dream_id: dream_20260516T104822
tier: median
overall_score: 3/6 Reject
timestamp: 2026-05-16T11:31:12.221750+00:00
---

# Review Report: ContamCal — Characterizing and Calibrating Benchmark Contamination via Contamination-Augmented IRT

## Meta

- **Reviewer**: R1 (full-coverage single reviewer, simple mode)
- **Paper**: ContamCal: Characterizing and Calibrating Benchmark Contamination via Contamination-Augmented Item Response Theory
- **Venue standard**: Top ML venue, ~25% acceptance rate
- **Rating**: 3/6 (Reject)
- **Confidence**: 4/5

---

## Summary

The paper proposes ContamCal, a framework that augments Item Response Theory (IRT) with a per-benchmark contamination effect parameter γ_k to characterize and calibrate LLM benchmark contamination. Through controlled SFT injection experiments across 0.5B–7B models (Qwen2.5, Llama-3.2), the paper documents: (1) a three-regime taxonomy of scale-dependent contamination effects, (2) Min-K++ directional reversal at small scales, and (3) an identifiability analysis showing N ≥ 50 models are needed for reliable γ recovery. The paper honestly concludes that calibration does not outperform simple baselines and repositions ContamCal as a diagnostic tool with explicit "When NOT to Calibrate" operational boundaries.

---

## Strengths

**S1. Intellectual honesty and self-critical framing.** The paper is unusually transparent about its method's limitations. The "When NOT to Calibrate" section (§5), the explicit admission that calibration does not outperform linear regression, the coverage collapse disclosure (33–35% vs. nominal 95%), and the GSM8K overcorrection negative result are all commendable. This level of honesty is rare and sets a positive example for the field. If more papers were written this way, the community would benefit.

**S2. Well-motivated methodological bridge.** Connecting LLM contamination to the item compromise literature in educational measurement (Eckerly 2017, Sinharay 2017) is a sound and creative methodological move. The three structural modifications (independent examinees → single model, binary leakage → continuous exposure, stable ability → regime-conditional ability) are clearly articulated.

**S3. Identifiability analysis is the strongest technical contribution.** The Fisher Information analysis (Eq. 5) combined with simulation sweeps establishing N ≥ 50 at AUC ≥ 0.55 is rigorous and practically important. The CI width ∝ N^{−0.48} scaling law provides a concrete, actionable guideline. This result explains *why* IRT calibration cannot work in the typical LLM evaluation regime (N = 8–30) and constitutes a genuine impossibility finding.

**S4. Min-K++ reversal is a useful practical warning.** The directional reversal (Cohen's d = −1.98 at 0.5B) is well-documented and practically important. Practitioners using Min-K++ at small scales would systematically flag the wrong items. The scale-dependent characterization (reversal → attenuation → ineffectiveness) is clean.

**S5. Controlled experimental design is sound.** The SFT injection protocol with 5 dosage levels, two model families, and four scales provides a well-structured factorial design. Ground-truth contamination labels enable valid signal evaluation.

**S6. Comprehensive experiment coverage.** The paper covers scale bridging (7B), cross-family validation (Llama), QC-only ablation, observational case study, 72B ecological validation, and closed-weight 2-signal ablation. All expected experiments from a thorough investigation of this framework are present.

---

## Weaknesses

**W1. The proposed method does not work in its own evaluation — the core contribution is self-defeating (Major).** The paper proposes a calibration framework and then demonstrates across multiple axes that it fails:
- Calibration MAE (0.035) vs. linear regression MAE (0.040): not statistically significant (§6).
- Expected regret: calibration (1.8pp) is *worse* than raw scores (1.5pp) and remove-and-rescore (1.2pp) (Table 7).
- Kendall τ: raw scores (0.82) outperform ContamCal (0.76) for ranking (Table 8).
- 95% coverage: 33–35% vs. nominal 95% — the uncertainty estimates are badly miscalibrated.

The pivot to "diagnostic characterization" as the primary value feels like post-hoc rationalization. If ContamCal's value is diagnostics, the paper should be structured around the diagnostic contributions from the start, not as a calibration framework that happens to fail at calibration.

**W2. Pervasive lack of statistical significance (Major).** Almost no quantitative finding in the paper reaches conventional significance thresholds:
- γ CI excludes zero only "borderline" at 0.5B (CI: [−2.3, 0.12] — this actually *includes* zero); never for any other scale or family.
- Cross-family Kendall τ = 0.60 is computed from only 4 data points (ARC across 4 model configs) — meaningless as a statistical test.
- All observational γ estimates include zero (Table 6).
- QC-only vs. all-paraphrases: no significant differences on any metric (Table 5).

The paper repeatedly uses the phrase "directionally consistent" as a substitute for "not significant." While the patterns are suggestive, a top venue paper needs at least some statistically rigorous findings. The N ≥ 50 requirement identified by the paper's own analysis means the entire experimental apparatus is designed to operate below its own identifiability threshold — this is a fundamental design problem, not just a sample size limitation.

**W3. The 0.5B catastrophic forgetting is confounded and the obvious control is missing (Major).** The most dramatic finding (−17.6pp on ARC at 0.5B) is acknowledged as possibly reflecting "general SFT capacity displacement rather than contamination-specific effects" (§6). The paper explicitly notes that "an SFT-on-random-data control would isolate this confound" — and then doesn't run it. This is a critical omission. The headline number that drives the three-regime taxonomy may not reflect contamination at all. Without this control, the 0.5B regime of the taxonomy is uninterpretable.

**W4. Multi-signal RRF is effectively single-signal (Moderate).** S2 (Min-K++, AUC = 0.465), S3 (ConStat, AUC = 0.55), and S4 (Self-Critique, AUC = 0.48) are at or below chance level. The "multi-signal fusion via RRF" framing is misleading — the system runs on S1 alone. The paper acknowledges this ("RRF degrades to S1-only," §3.2) but never tests S1-alone vs. RRF to confirm that the additional signals add zero value. If S1 is the only working signal, the multi-signal architecture is dead weight that obscures the method's actual structure.

**W5. 4PL model is severely over-parameterized for N = 8 (Moderate).** A 4PL IRT model has 4 item-level parameters (a_j, b_j, c_j, d_j) plus γ_k per benchmark. With N = 8 models, the item parameters cannot be reliably estimated — especially c_j and d_j asymptotes, which require substantial data even in classical IRT with hundreds of examinees. The paper does not discuss how c_j/d_j are handled (fixed? regularized? estimated?). The 33–35% coverage rate is likely a symptom of model misspecification from over-parameterization, not just low N. A 2PL or even 1PL model might produce more honest (if wider) intervals.

**W6. SFT injection ≠ pretraining contamination — ecological validity gap (Moderate).** Real benchmark contamination typically occurs through pretraining data overlap, not supervised fine-tuning on paraphrased items. SFT fundamentally changes the model's loss landscape in ways pretraining does not (catastrophic forgetting of pretrained knowledge, overfitting to narrow data distributions). The paper's findings — especially the catastrophic forgetting at 0.5B — may be artifacts of the SFT injection protocol rather than properties of contamination. This gap between experimental and real-world contamination is not adequately discussed.

**W7. Effective validation on a single benchmark at a single scale (Moderate).** The framework shows meaningful signal only on ARC at 0.5B. MMLU has position bias issues at 0.5B (excluded from pooling), GSM8K overcorrects (gating rejects it), HumanEval is only reported for 7B, and effects at 1.5B+ are within noise. The characterization contribution rests almost entirely on a single scale–benchmark combination that is also the most confounded (W3).

**W8. Missing baselines (Minor).** No comparison with DCR [Oren et al., 2024], which provides adjusted accuracy via fuzzy detection and is the most directly comparable method. The baseline set (raw scores, linear regression, remove-and-rescore) is minimal for a paper proposing a new calibration framework.

---

## Questions for Authors

1. Why was the SFT-on-random-data control not run for 0.5B? This is the single most important missing experiment — it would disambiguate the headline finding.
2. What is the actual performance of S1-alone vs. 4-signal RRF? If RRF adds no value over S1, the multi-signal architecture should be simplified or dropped.
3. How are the 4PL asymptote parameters (c_j, d_j) identified with N = 8? Are they fixed, regularized, or freely estimated?
4. "Borderline significant" for γ at 0.5B: the reported CI [−2.3, 0.12] includes zero. What does "borderline" mean here — a posterior probability criterion?
5. Has any evaluation been done with pretraining-style contamination (data mixing) rather than SFT injection?

---

## Detailed Scores

| Criterion | Score (1–6) | Comments |
|-----------|-------------|----------|
| Novelty | 3 | IRT + contamination covariate is a reasonable but incremental adaptation of known educational testing methods. The specific adaptation (continuous exposure, regime-conditional ability) is technically sound but conceptually straightforward. |
| Soundness | 2 | Pervasive lack of statistical significance; the 0.5B confound is unresolved; 4PL over-parameterized for N=8; coverage collapse indicates misspecified model. The identifiability analysis is sound but it invalidates the paper's own experiments. |
| Significance | 3 | The identifiability impossibility result (N ≥ 50) and Min-K++ reversal are genuinely useful findings. But the calibration framework doesn't work, limiting practical impact. The characterization findings are interesting observations in a synthetic setup with uncertain generalization. |
| Clarity | 4 | Well-written, clearly structured, transparent about limitations. Some redundancy (scale-dependent / N is binding constraint repeated ~5 times). Tables are informative. |
| Reproducibility | 4 | Experimental setup is well-specified. Model families, dosage levels, and metrics are clear. Code/data release not mentioned. |
| Experiment coverage | 4 | All major experiments are present: scale bridging (7B), cross-family (Llama), QC ablation, observational study, 72B ecological, 2-signal ablation. The missing SFT-random control is a notable gap. 72B is appropriately brief. |

---

## Minor Issues

- Table 1: 3B shows Δpp = +1.2 but γ = −0.42. The sign discrepancy (positive accuracy change, negative γ) deserves explanation — is γ estimated from pooled data rather than per-scale?
- §3.2: The RRF equation uses S signals but only S1 is effective. Consider reporting S1-only results as the primary analysis and RRF as a robustness check.
- Related work (§2): ConStat citation appears truncated — "[Golchin and Surdeanu, 202" is missing the closing year.
- §4.6: The 72B ecological validation adds minimal content (one paragraph, no table). Consider moving to appendix to save space for more substantive analysis (e.g., the missing SFT-random control).
- The paper uses "calibration" in a non-standard way for ML (decontamination adjustment vs. probability calibration). While §2 disambiguates, the title "ContamCal" may cause confusion. Consider "ContamCal: Characterizing Benchmark Contamination..." without "Calibrating" given the paper's own conclusion that calibration doesn't work.

---

## Overall Assessment

The paper addresses an important problem — what to do about benchmark contamination beyond just detecting it — and the intellectual honesty about limitations is genuinely refreshing. The identifiability analysis (N ≥ 50 threshold) and Min-K++ reversal finding are useful contributions to the community's understanding.

However, the paper suffers from a fundamental structural problem: **it proposes a calibration framework that its own analysis proves cannot work in the regime where it's needed.** The N ≥ 50 requirement means the experiments (N = 8) are fundamentally underpowered, and this shows in the pervasive non-significance of results. The pivot to "diagnostic characterization" as the primary contribution is insufficiently developed — the characterization findings (scale-dependent effects, benchmark heterogeneity) are interesting observations but are documented with only directional evidence from a synthetic SFT setup whose ecological validity to real contamination is unestablished.

The most impactful finding (−17.6pp at 0.5B) is the most confounded (SFT capacity displacement), and the obvious control experiment to resolve this confound was not conducted. The paper would be substantially stronger if it either (a) provided the random-SFT control and demonstrated contamination-specific effects, or (b) reframed entirely around the impossibility result and diagnostic toolkit, dropping the calibration framing.

As submitted, the paper falls below the acceptance threshold for a top ML venue. The gap between what is promised (calibration) and what is delivered (a diagnostic tool that produces non-significant estimates) is too large, despite the honest framing.

**Recommendation: Reject (3/6).** A major revision reframing around the impossibility result and diagnostic characterization — with the SFT-random control and simplified to 2PL — could be competitive.
