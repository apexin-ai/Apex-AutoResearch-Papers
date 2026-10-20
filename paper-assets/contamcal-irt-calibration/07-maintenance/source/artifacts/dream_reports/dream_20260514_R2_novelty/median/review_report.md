---
dream_id: dream_20260514_R2_novelty
tier: median
overall_score: weak reject
timestamp: 2026-05-14T18:41:16.074890+00:00
---

# Reviewer 2 (R2): Novelty, Significance, Positioning, and Related Work

**Paper**: "When Contamination Signals Fail: An Empirical Anatomy of Detection Reliability and Identifiability Boundaries for Contamination-Aware LLM Evaluation"
**Venue**: EMNLP 2026 Special Theme "New Missions for NLP Research"

---

## 1. Summary

This paper performs a systematic empirical study of contamination detection signal reliability across 4 methods, 3+ model scales, and 4 dosage levels under SFT paraphrase injection. The main empirical findings are: (1) only embedding-based similarity maintains detection effectiveness (AUC > 0.94) across scales while Min-K++, ConStat, and Self-Critique remain at chance; (2) Min-K++ exhibits a directional reversal (Cohen's d from -1.0 to -2.7) that actively misleads rather than merely failing; (3) an identifiability boundary at AUC >= 0.80 governs when contamination-aware IRT calibration is practical. The proposed ContamCal framework (4PL+gamma IRT with measurement error model) is presented as a proof-of-concept that honestly underperforms expectations --- marginal improvement over linear regression (4.3pp vs 4.8pp MAE with overlapping CIs), and 85% coverage at nominal 95%.

---

## 2. Novelty Assessment (Claim by Claim)

### Claim 1: "First systematic reliability audit of contamination signals under controlled contamination with varying dosage, scale, and model family"

**Partially justified, but overstated.** The controlled injection design with dosage variation (0-100%) across 3 scales within one family + Llama cross-family replication is more systematic than prior work. However:
- Yang et al. 2023 and Oren et al. 2024 already conduct controlled contamination experiments with signal evaluation, albeit not at this factorial breadth.
- The "first" claim hinges on the specific combination of (dosage x scale x multiple signals x controlled ground truth). This is a quantitative expansion of existing methodology, not a qualitative leap. The coverage of "scale-dependent" effects is weakened by the finding that S2-S4 fail at ALL scales tested (0.5B through 7B), not just small ones --- the narrative of "scale-dependent" effectiveness reduces to "S1 always works, others never do."
- The single-family primary design (Qwen2.5) with only one cross-family replication (Llama 1B at 3 dosages) limits the generality of "first systematic" claims.

**Verdict: Incremental expansion of existing experimental paradigms. The factorial design is more thorough, but the conceptual approach is not new.**

### Claim 2: Min-K++ Directional Reversal

**Genuinely novel and the paper's strongest empirical contribution.** The finding that Min-K++ not only fails but actively reverses direction under SFT contamination (Cohen's d = -1.98 at 0.5B, persistent across all scales and benchmarks, p < 10^-80) has not been documented in the literature. Prior work (Shi et al. 2024, Wang et al. 2025) documents signal degradation under RL but does not identify directional reversal under SFT.

The proposed mechanism (LoRA adaptation reduces perplexity surprise on trained items, flipping the Min-K++ direction) is plausible but not formally verified. A critical open question: does this reversal persist under full fine-tuning or pretraining contamination, or is it LoRA-specific? The paper does not address this.

**Verdict: Novel, empirically robust, and practically important. This alone could anchor a focused empirical contribution paper.**

### Claim 3: Identifiability Boundaries for Contamination-Aware Calibration

**Moderate novelty.** The Fisher Information derivation for I(gamma) in the 4PL+gamma model (Appendix) is technically competent and provides a clean analytical result linking signal AUC to gamma recoverability via the bi-normal model. The structural vs. practical identifiability distinction (AUC >= 0.55 structural, AUC >= 0.80 practical) is useful.

However:
- Fisher Information for IRT parameters is a standard computation in psychometrics (Lord 1980, Baker & Kim 2004). The extension to the gamma covariate is a straightforward application of the Bernoulli information formula.
- The simulation sweep (144 conditions) confirming the analytical bounds is a useful validation but not novel methodology.
- The practical identifiability threshold (AUC >= 0.80) is data-driven from their specific experimental setup and may not generalize to other contamination scenarios.

**Verdict: Technically solid, useful for practitioners, but a routine extension of standard psychometric theory to a new parameter.**

### Claim 4: Format Learning Confound in GSM8K Under SFT

**Partially novel, partially known.** The finding that LoRA SFT at 3B causes catastrophic forgetting of GSM8K answer format (base 60.5% to SFT 12%) with contaminated items partially restoring it is a specific and interesting confound. However:
- Format sensitivity of generative benchmarks under fine-tuning is well-documented (Zheng et al. 2023, eval-harness documentation).
- The claim that gamma_GSM8K = 1.85 confounds format recovery with contamination undermines rather than strengthens the paper --- it means the one statistically significant result in the calibration framework is artifactual.
- The pivot to "ContamCal identifies benchmarks not requiring calibration" (GSM8K as negative control) is post-hoc rationalization of a failed experiment direction.

**Verdict: The specific confound is documented with useful detail, but the broader phenomenon is known, and this finding weakens rather than strengthens the paper's primary contribution.**

### Claim 5: ContamCal as IRT-Based Calibration Framework

**Limited novelty.** The core technical contribution is adding a single linear covariate (gamma * tau) to standard 4PL IRT, which is precisely what explanatory IRT (De Boeck & Wilson 2004) prescribes for incorporating external covariates. The three claimed "structural adaptations" are:
- (a) Independent examinees to single model: This is acknowledged as a limitation (local independence violation) rather than solved. Mean residual correlation of 0.08 indicates unresolved model misspecification.
- (b) Binary to continuous exposure: Standard in explanatory IRT. The measurement error model is classical errors-in-variables.
- (c) Stable to regime-conditional ability: Not actually implemented (no regime-specific theta parameters). Handled through signal selection, which is an experimental design choice, not a methodological contribution.

RRF aggregation is off-the-shelf (Cormack et al. 2009). HMC inference is standard. The framework is a competent domain-transfer of established methods.

**Verdict: Synthesis paper applying known techniques to a new domain. For a top venue, the synthesis must demonstrate emergent value exceeding its parts. With 4.3pp vs 4.8pp MAE (overlapping CIs), this emergent value is not demonstrated.**

---

## 3. Significance and Impact

**Who benefits:**
- The contamination detection community benefits from the signal characterization (S1 robustness, Min-K++ reversal). This has immediate practical implications for anyone building contamination detection pipelines.
- The LLM evaluation community benefits from the identifiability analysis, which provides principled guidance on when contamination-aware calibration is feasible.
- Practitioners seeking calibrated benchmark scores do NOT substantially benefit --- the framework is statistically indistinguishable from linear regression for point estimates, and the UQ contribution is undermined by the 10pp coverage gap.

**How much:**
- The Min-K++ reversal finding is high-impact within its niche. Anyone using Min-K++ on fine-tuned models should be aware of this.
- The calibration framework itself is low-impact in its current form. A practitioner would rationally choose linear regression + bootstrap for simplicity.
- The negative result (ContamCal honestly underperforms expectations) has modest pedagogical value, but the field does not have a strong norm of publishing negative results at top venues unless the experimental apparatus is particularly illuminating.

**EMNLP special theme fit:** The contamination focus aligns with "New Missions for NLP Research." However, the special theme presumably seeks papers that advance solutions, not papers documenting that a proposed solution does not work. The empirical anatomy of signal reliability fits better than the calibration framework.

---

## 4. Related Work Gaps

### Missing citations that matter:

1. **Membership inference literature**: Shokri et al. 2017 ("Membership Inference Attacks Against Machine Learning Models") is the foundational work underlying Min-K++. Not citing this while extensively analyzing Min-K++ behavior is a significant omission. Similarly, Carlini et al. 2022 ("Membership Inference Attacks From First Principles") provides theoretical grounding for why such methods fail under distribution shift.

2. **Training data attribution**: TRAK (Park et al. 2023) and TracIn (Pruthi et al. 2020) are mentioned in Future Work but deserve substantive discussion in Related Work. These methods could serve as alternative or complementary contamination signals, and the paper should explain why they were not included in the signal ensemble (computational cost is a valid reason but should be explicit).

3. **Alternative evaluation paradigms**: Chatbot Arena (Chiang et al. 2024), HELM (Liang et al. 2023), and other human-evaluation or live-competition approaches that sidestep contamination entirely are not discussed. These represent a parallel solution philosophy (avoid the problem vs. correct for it) and should be acknowledged.

4. **LLM-specific IRT work beyond cited papers**: Burnell et al. 2023 ("Revealing the Structure of Language Model Intelligence") applies IRT with factor analysis to decompose LLM capabilities. Relevant for the discussion of unidimensional theta as a simplification.

5. **Contamination surveys**: Ravaut et al. 2024 ("How Much are LLMs Contaminated? A Comprehensive Survey and the LMC Benchmark") provides comprehensive coverage statistics that would contextualize the dosage levels used.

6. **Psychometric DIF beyond the classical citations**: More recent DIF work in computerized adaptive testing (CAT) with continuous covariates is directly relevant and would strengthen the DIF connection beyond the 1993/1999 references.

7. **DCR comparison depth**: DCR (EMNLP 2025) is cited as the closest predecessor but the comparison is shallow. The paper should discuss DCR's fuzzy inference mechanism in detail and explain precisely where ContamCal's Bayesian approach theoretically improves on it, beyond "adding uncertainty bounds."

### Reference count and quality:
The dream paper has ~30 references, which is adequate but on the low side for a 14-page paper with this scope. The educational measurement citations are appropriate and well-integrated. The NLP contamination literature coverage is adequate but not comprehensive.

---

## 5. Positioning and Framing

### Is the "diagnostic framework" framing convincing?

**Mixed.** The paper oscillates between two framings:

1. **ContamCal as a calibration method** (the original pitch): This framing fails because the calibration results are marginal. A calibration method that is indistinguishable from linear regression on point accuracy and misses nominal coverage by 10pp is not a compelling contribution.

2. **Empirical anatomy of signal reliability** (the emergent story): This framing is much stronger. The signal characterization, Min-K++ reversal, identifiability boundaries, GSM8K format confound, and RRF degradation to single-signal mode are all interesting findings that collectively provide a useful diagnostic picture.

The paper would be significantly stronger if it committed fully to framing #2, treating the IRT calibration as one tool within a broader diagnostic analysis rather than the headline contribution. The title "When Contamination Signals Fail" actually aligns better with framing #2 than with framing #1.

### Is the "negative result" narrative well-executed?

**Partially.** The paper is admirably honest about limitations --- the admission that ContamCal underperforms expectations, that RRF degrades to single-signal mode, that only one gamma is significant and it's confounded. This transparency is rare and valuable.

However, the negative result framing is inconsistent:
- The introduction and method sections build up ContamCal as a comprehensive calibration framework with principled UQ.
- The results reveal it barely outperforms trivial baselines.
- The discussion reframes this as "honest uncertainty quantification" and "diagnostic framework."

This reads as a paper that set out to propose a calibration method, found it didn't work as hoped, and is now retroactively finding the silver lining. That is scientifically honest, but it creates a structural mismatch between the front half (method paper) and the back half (empirical analysis paper). The reader finishes the paper unsure whether the contribution is the framework (which didn't work) or the findings (which are interesting but secondary to the stated contribution).

### Does the EMNLP special theme framing make sense?

**Yes, for the empirical findings; less so for the calibration framework.** The special theme "New Missions for NLP Research" invites work on contamination and data governance. The signal reliability audit and Min-K++ reversal speak directly to this theme. The IRT calibration framework is more of a traditional methods contribution that happens to be applied to contamination.

---

## 6. Weaknesses (Bullet Points)

**Major:**
- W1. ContamCal achieves 4.3pp MAE vs. 4.8pp linear regression with overlapping bootstrap CIs. The primary contribution is statistically indistinguishable from a trivial baseline on point accuracy.
- W2. 95% CI coverage reaches only 0.85 (nominal 0.95). The paper's claimed distinctive advantage (UQ) is itself poorly calibrated. Without SBC diagnosis, the root cause and fixability are unknown.
- W3. "Multi-signal framework" collapses to single-signal (S1) reality. RRF-4 degrades below S1-only (AUC 0.947 vs 0.975). The entire Stage 1 pipeline beyond embedding retrieval is dead weight in the current signal landscape.
- W4. The only statistically significant gamma (GSM8K = 1.85) is confounded by format learning. MMLU and ARC gamma CIs include zero, meaning ContamCal detects no contamination effect on the two benchmarks without confounds.
- W5. Methodological novelty is limited: adding a linear covariate to explanatory IRT is the textbook prescription (De Boeck & Wilson 2004). The "three structural adaptations" are either not fully solved (local independence), standard (continuous exposure), or not implemented (regime-conditional ability).
- W6. N_models is severely insufficient. The paper's own identifiability analysis recommends N >= 50, but the actual experiment uses ~15 models pooled across scales (~4 per scale). Posteriors may be prior-dominated rather than data-driven.

**Moderate:**
- W7. SFT paraphrase injection is a limited contamination proxy. Real contamination occurs through pretraining data overlap, not LoRA fine-tuning on paraphrased items. Documented artifacts (0.5B ability regression, GSM8K format collapse) suggest the proxy introduces confounds distinct from the phenomenon being studied.
- W8. Observational results on RL-trained and 72B models provide no meaningful calibration (0.5-0.7pp correction, 13-18pp CI widths). Without ground truth, these cannot validate the framework; they only demonstrate that the method degrades gracefully to doing nothing.
- W9. Per-benchmark gamma via separate model fits (not hierarchical) cannot formally test heterogeneity, share information across benchmarks, or estimate a population-level contamination distribution.
- W10. The paper does not discuss whether Min-K++ reversal is LoRA-specific or generalizes to full fine-tuning / pretraining contamination, which determines its practical import.

**Minor:**
- W11. Missing key related work: Shokri et al. 2017, Carlini et al. 2022, Chatbot Arena, HELM, Burnell et al. 2023.
- W12. The measurement error model's status is unclear from internal project records (D013 abandoned the analytical ME model in favor of the "simple" model, yet the ME model is prominently described in the methods).

---

## 7. Strengths (Bullet Points)

- S1. The Min-K++ directional reversal finding (Cohen's d = -1.98 to -2.7, persistent across scales/benchmarks/families) is genuinely novel, empirically robust, and practically important for the detection community.
- S2. The systematic signal x scale x dosage AUC characterization, though an incremental expansion of prior work, provides the most comprehensive factorial mapping to date.
- S3. The Fisher Information derivation for gamma in 4PL+gamma IRT is clean and produces an actionable AUC-information relationship with the structural/practical identifiability distinction.
- S4. Cross-family validation on Llama-3.2-1B confirms signal patterns generalize beyond Qwen2.5.
- S5. The paper is admirably honest about limitations: marginal advantage over baselines, single-signal operational reality, GSM8K confound, and insufficient N_models are all transparently discussed.
- S6. Comprehensive experimental design: 80+ controlled models, 4 benchmarks, 7 baselines, 5 evaluation metrics, ground-truth clean scores for every configuration.
- S7. The causal inference framing (measuring and adjusting confounders rather than eliminating them) is well-motivated by Emperor's New Clothes (Xu et al. 2024).
- S8. The grounding in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) is genuine and appropriately cited.
- S9. The GSM8K format learning confound, while weakening the calibration contribution, is itself a useful empirical finding for the evaluation community.

---

## 8. Questions for Authors

1. Given the overlapping CIs between ContamCal and linear regression (4.3pp [3.1, 5.5] vs 4.8pp [3.5, 6.1]), what concrete evaluation scenario justifies the full 4PL+gamma+ME pipeline over simple regression? If the answer is "UQ," how do you explain the 10pp coverage shortfall?

2. The Min-K++ reversal is your strongest finding. Have you investigated whether it is specific to LoRA SFT (where parameter updates are low-rank and concentrated), or whether it persists under full fine-tuning or pretraining contamination? This determines whether the finding is a LoRA artifact or a fundamental property of membership inference under distributional shift.

3. On MMLU and ARC, gamma CIs include zero. This means ContamCal detects no contamination effect on two of three primary benchmarks. How do you reconcile this with the controlled injection protocol that demonstrably contaminates these benchmarks?

4. Have you run simulation-based calibration (SBC, Talts et al. 2018) at your actual N_models (~15) and N_items to diagnose the 10pp coverage gap? Is it attributable to local independence violation, N_models insufficiency, or model misspecification?

5. Why not adopt a hierarchical specification gamma_k ~ Normal(mu_gamma, sigma_gamma) across benchmarks rather than separate fits? This would enable formal heterogeneity testing, information sharing, and better gamma estimation under small N.

6. The paper claims "regime-conditional ability" as a structural adaptation but does not implement regime-specific theta parameters. What would change if you modeled theta per training regime?

7. For closed-weight models (Table 10: 2-signal mode), MAE degrades to 6.7pp and coverage to 0.70. Given that most models of practical interest are closed-weight (GPT-4, Claude, Gemini), how do you see the framework's practical applicability?

8. The RRF framework degrades below S1-only. Under what empirical conditions (what kinds of future signals) would multi-signal aggregation actually help? Can you provide a principled analysis of when RRF adds value vs. degrades?

---

## 9. Score and Confidence

**Score: 3/6 (Weak Reject)**

**Rationale:** The paper tackles an important problem and the empirical work is thorough and honest. However, the primary methodological contribution (ContamCal calibration framework) demonstrates marginal improvement over trivial baselines with overlapping confidence intervals, limited methodological novelty beyond domain transfer of standard explanatory IRT, and the distinctive UQ claim is undermined by a 10pp coverage gap. The multi-signal framing does not match the single-signal operational reality. The Min-K++ reversal finding and signal characterization are genuinely valuable, but they are positioned as secondary contributions supporting a calibration framework that does not deliver.

For a top venue at ~25% acceptance rate, the paper needs either (a) a calibration framework that demonstrably outperforms simpler alternatives, or (b) a full commitment to the empirical anatomy framing with the signal characterization and identifiability analysis as primary contributions. Currently it falls between these two stools.

The paper would be more competitive if reframed as an empirical study of contamination signal reliability with the IRT calibration as one diagnostic tool among several, rather than as a methods paper proposing a calibration framework that happens to not work very well.

**Confidence: 4/5**

I have thorough familiarity with the IRT literature (both classical psychometric and LLM evaluation applications), the contamination detection literature, and the Bayesian modeling methodology. I have carefully read the full paper including the Fisher Information appendix and all experimental results. My primary uncertainty is whether the Min-K++ reversal finding alone, if elevated to the primary contribution, would be sufficient for acceptance under the special theme --- it might be, but that is an editorial judgment about scope.
