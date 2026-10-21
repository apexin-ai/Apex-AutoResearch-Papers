---
dream_id: dream_20260522T023801
tier: best
overall_score: 5 - Marginally below acceptance threshold
timestamp: 2026-05-22T03:24:45.301030+00:00
---


---
reviewer: R1 (Methods & Experiments Focus)
venue: ICLR 2027
paper: "Cross-Lingual Knowledge Conflict Signals in Multilingual LLMs: Directional Asymmetry, Layer Structure, and Causal Probing"
---

### Summary

This paper investigates how cross-lingual knowledge conflict signals are encoded in the residual stream of multilingual LLMs, using linear probes, CKA/SVCCA analysis, SAE feature decomposition, and representation steering across three architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B-IT) and two language pairs (EN-ZH, EN-JA). The central finding is a directional asymmetry in cross-lingual probe transfer: transfer toward English (X->EN) consistently outperforms transfer away from English (EN->X) by 6.3-7.9pp across all model-language-pair combinations. The paper frames this within a hypothesis-testing structure (H1: English-anchored universal detection vs. H2: language-pair-specific encoding) and marshals three tracks of evidence -- probing, SAE decomposition, and causal steering -- to support H1. The paper is ambitious in scope and commendably transparent about limitations.

### Strengths

**S1. Hypothesis-driven structure is exemplary for interpretability research.** The H1 vs. H2 framework generates specific, falsifiable predictions (mid-layer > late-layer Jaccard; directional consistency across language pairs) that are then tested. This elevates the work above typical exploratory probing studies. The pre-registered competing hypotheses are the methodological highlight of the paper.

**S2. Three-track convergence provides increasingly strong evidence types.** The detection (probing) -> decomposition (SAE) -> intervention (steering) pipeline is well-conceived. The fact that the steering flip rate asymmetry (ZH->EN 24.3% > EN->ZH 17.8% for Llama probe-based; ZH->EN 31.0% > EN->ZH 24.0% for SAE-based) mirrors the probe transfer asymmetry is the paper's strongest individual result, because it moves the asymmetry claim from correlational to causal territory. This triangulation design is a genuine methodological contribution.

**S3. Cross-architecture effect size consistency is striking.** The asymmetry gaps of +7.2pp / +7.2pp / +7.9pp across three architectures with CV < 6% is remarkably homogeneous. The Cochran's Q test (p=0.68, I-squared=0%) provides appropriate meta-analytic justification. Even if individual models have borderline significance, this homogeneity is itself strong evidence that the effect is real rather than artifactual.

**S4. Confound exclusion pipeline is thorough and well-designed.** The COMET tercile ablation is the right experiment: rather than imposing an arbitrary quality threshold, the authors directly test whether translation quality predicts probe accuracy, finding a null/reversed relationship (delta = -1.6pp Llama, -5.6pp Qwen, Fisher p > 0.69). The token overlap analysis (per-sample Jaccard 3-4%, negative correlation in Llama) correctly addresses a plausible alternative explanation. The label noise robustness curve (graceful degradation at ~2.6pp per 5% noise) provides appropriate safety margins given the pipeline's estimated <5% error rate. These three controls together form a solid confound exclusion argument.

**S5. The steering experiment includes appropriate controls.** Random orthogonal directions as control (5-6% flip rate vs. 18-34% active) is the right baseline. Coherence preservation at 91% addresses the concern that steering simply degrades outputs. The feature-set ablation (shared features 28% vs. language-specific 9-11%) is a particularly incisive test of H1.

**S6. Honest reporting of negative/inconclusive results.** The SAE base-instruct mismatch (Appendix B), the Qwen CI including zero at n~1000, the EN-JA gap not reaching significance -- these are reported straightforwardly without spin. This builds credibility.

### Weaknesses

**W1 (Major). The "English-anchored conflict detection" claim is confounded with general English-anchored cross-lingual transfer.** The X->EN > EN->X asymmetry could be a general property of any cross-lingual semantic probing task on English-dominant models, not specific to conflict detection. English occupies a privileged position in the representation space of all three models due to pre-training data composition. The paper provides no non-conflict semantic baseline (e.g., probing for entailment, factual category, or sentiment across languages) to demonstrate that the asymmetry is conflict-specific. Without this control, the contribution reduces from "novel mechanistic finding about conflict encoding" to "replication of known cross-lingual transfer asymmetry on a new task." This is computationally trivial to add -- the entire probing pipeline exists, only the labels change -- making its absence particularly conspicuous.

**W2 (Major). Statistical power is insufficient for the central claim (C2).** At the reported sample sizes, only 2/3 models (or 3/4 model-language-pair combinations in the best-case scenario) reach 95% CI significance for the asymmetry. The paper's use of Cumming (2014) "new statistics" framing -- emphasizing effect sizes and CIs over NHST -- is legitimate in principle but risks appearing as post-hoc rationalization when applied selectively to the one model that fails significance. Specific issues:

- Bootstrap n=100 is below the conventional minimum of n>=1000 (Efron & Tibshirani 1993). At n=100, the 2.5th percentile is literally the 2nd or 3rd most extreme value, making CI endpoints highly volatile. For a claim where the lower CI bound matters (Qwen's -1.2pp), this is consequential. This is cheap to fix.
- The permutation test uses n=1000, which is adequate for p<0.001 claims but the paper does not report exact permutation p-values for the asymmetry itself (only for the per-direction probe accuracy vs. chance).
- The dataset expansion from n~1000 to n~1800 (Section 4.1) tightens the Qwen CI to [2.3, 11.7], which does exclude zero. But the paper presents both the original and expanded results, and the expanded dataset is not used for all subsequent analyses (CKA, steering, etc.), creating an inconsistency in the evidence base.

**W3 (Major). Both language pairs are CJK languages -- typological diversity is insufficient for "universal" claims.** EN-ZH and EN-JA share the CJK cultural sphere and similar embedding in English-dominant training corpora. H2 predicts language-pair-specific patterns; testing only pairs where the non-English languages are typologically similar cannot meaningfully falsify H2. An Indo-European pair (EN-DE, EN-FR) or a morphologically rich language (EN-TR, EN-FI) would provide a genuine test. The paper uses "universal" language in the H1 formulation but the evidence supports only "consistent across two CJK pairs."

**W4 (Moderate). SAE analysis operates on base model while probing operates on instruct model -- the cross-validation is weaker than claimed.** The Qwen-Scope SAEs are trained on Qwen3-8B-Base. RLHF/instruction tuning systematically reorganizes representations, particularly in mid-to-late layers -- precisely where the paper claims critical conflict processing occurs. The paper's acknowledgment (Appendix B) that base-instruct cosine similarity is only 0.71 and only 35% of features are interpretable on the instruct model actually undermines rather than supports cross-track validation. The Jaccard analysis (Table 8) operates entirely in the SAE's base-model feature space, and projecting these results onto instruct-model behavior is a logical gap. Furthermore, SAE analysis covers only Qwen -- there is no cross-architecture SAE validation.

**W5 (Moderate). Probe accuracy of 69-77% is substantially below prior monolingual work (~90+ F1) without adequate explanation.** The 23-31% undetectable fraction is non-trivial. The paper claims conflict signals are "linearly detectable" but does not characterize what fraction of the signal is linear vs. non-linear (the MLP analysis addresses only the cross-lingual transfer direction, not within-language detectability ceiling). Possible explanations -- intrinsic difficulty of the cross-lingual setting, label noise from the verification pipeline, genuinely distributed/non-linear signal -- are not systematically investigated or distinguished.

**W6 (Moderate). The CKA-probe correlation (r = -0.71) is computed over 3 data points.** This cannot be presented as a statistical finding. Three points always produce a correlation that appears large. The paper should report the raw numbers and qualitative pattern without computing a correlation coefficient or implying statistical meaning.

**W7 (Moderate). Steering captures a minority of samples without characterization of non-responding samples.** Flip rates of 17-35% mean 65-83% of samples are unaffected. The paper does not analyze which samples respond to steering vs. which do not. If non-responding samples are systematically different (e.g., higher model confidence, different entity types, different conflict types), this would significantly refine the mechanistic story. The Cohen's d of 0.41 is a small-to-medium effect, honestly reported, but the paper would benefit from connecting this to the probe accuracy ceiling (W5).

**W8 (Minor). Small feature counts make Jaccard statistics fragile.** The mid-layer Jaccard of 0.28 is based on 8 shared features out of 21 EN and 18 ZH features. The late-layer Jaccard of 0.12 is based on 3 shared features out of 14 EN and 10 ZH features. Reclassifying a single feature (e.g., by shifting the MI threshold by 0.01) could move mid-layer Jaccard from 0.28 to 0.23 or 0.33. No sensitivity analysis over the MI > 0.15 threshold or filtering criteria is provided.

**W9 (Minor). MLP probe overfitting risk is not addressed.** A single hidden layer with 256 units trained on ~1000 samples risks overfitting, especially in the EN->ZH direction where the MLP gain is largest (up to 6.1pp for Gemma). The paper does not report the train-test accuracy gap for MLP probes. Without this, the MLP gains could partially reflect overfitting rather than genuine non-linear signal.

**W10 (Minor). Using the same model for translation and probing introduces circularity potential.** The target models themselves generate the Chinese/Japanese translations. If the model's translation biases systematically correlate with its internal conflict representations, the translated text could contain subtle cues that inflate probe accuracy for within-model transfer. Using an independent translation model (or professional human translation for a subset) would control for this.

### Questions for Authors

**Q1 (Critical).** Have you tested the X->EN > EN->X asymmetry on a non-conflict semantic task using the same pipeline? This is the single most important experiment missing from the paper. If the same asymmetry appears for sentiment or topic probing, the conflict-specificity claim is falsified.

**Q2.** Why was bootstrap n set to 100 rather than the conventional >=1000? The entire probing pipeline uses logistic regression, so each bootstrap iteration takes seconds. Was this a deliberate choice or an oversight?

**Q3.** For the steering experiment, how was the optimal alpha (reported as 2.5 for probe-based, 3.5 in the summary) selected? Was it tuned on a held-out validation set or on the test set? If the latter, flip rates are optimistically biased.

**Q4.** How is "coherence preserved at 91%" operationalized? Is this human evaluation, an automated metric (e.g., perplexity delta), or something else? The paper does not define this metric.

**Q5.** In Table 3 (MLP non-linearity), the text claims the gain anti-correlates with Chinese pre-training data proportion. What are the actual Chinese data proportions for these three models? Gemma-2-9B-IT having the largest non-linear gain (+6.1pp) seems surprising given Google's substantial multilingual training data.

**Q6.** For the SAE analysis, why not run the probing track on the base model as well, to enable direct comparison within the same model version? This would eliminate the base-instruct mismatch entirely for at least one architecture.

**Q7.** The paper reports balanced accuracy throughout. What is the class balance in the test sets? If close to 50/50, balanced and unbalanced accuracy are equivalent and reporting both would increase transparency.

### Missing Experiments/Controls

1. **Non-conflict semantic baseline (Critical).** Probe for a non-conflict binary semantic distinction (entailment, sentiment, factual category) and measure whether the X->EN > EN->X asymmetry persists. If it does, reframe the contribution. If it does not, the conflict-specificity claim is validated. Computationally trivial.

2. **Non-CJK language pair (High).** EN-DE, EN-FR, or EN-TR would test whether the pattern holds across typological families. Without this, "universal" framing is unsupported.

3. **Bootstrap n >= 2000 (Medium).** Increase bootstrap iterations for all CI computations. Cheap, strengthens all CI-based claims.

4. **MLP train-test gap analysis (Medium).** Report MLP probe accuracy on training data alongside test data to assess overfitting, especially for the EN->ZH direction where gains are largest.

5. **Steering alpha selection protocol (Medium).** Clarify whether alpha was tuned on test data (leakage) or a held-out validation split. If the former, re-run with proper held-out tuning.

6. **Characterization of steering non-responders (Low-Medium).** Analyze properties of the 65-83% of samples that do not flip under steering: model confidence, entity type, COMET score, conflict type.

7. **SAE sensitivity analysis (Low-Medium).** Vary the MI > 0.15 threshold and filtering criteria to demonstrate that the mid-layer > late-layer Jaccard finding is robust to these choices.

8. **Independent translation control (Low).** Use an independent translation model (not the probing target) for a subset to verify that same-model translation does not inflate results.

### Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | **3 / 4** | Methods are generally appropriate and correctly applied. Probing framework, permutation testing, CKA analysis, and steering controls are sound. Deductions for: missing non-conflict baseline (the largest methodological gap), bootstrap n=100 inadequacy, base-instruct SAE mismatch, r=-0.71 on 3 points, and no MLP overfitting control. The statistical framework is competent but not airtight. |
| **Presentation** | **3 / 4** | Paper is clearly written with a logical structure. H1/H2 framework aids readability. 13 tables create visual density but are individually well-designed. Limitations section is honest. Deductions for: thin bibliography (8 references), missing definition of "coherence preservation," and some overclaiming relative to evidence (e.g., "universal" with only CJK pairs). |
| **Contribution** | **3 / 4** | Novel intersection of mechanistic interpretability and multilingual NLP. The three-track convergence design and the specific finding of probe-steering asymmetry alignment are genuine contributions. However, if the non-conflict baseline reveals the asymmetry is a general cross-lingual transfer property (W1), the contribution drops to incremental. Current contribution is conditional on this experiment's outcome. |
| **Overall** | **5** | Marginally below acceptance threshold. The paper asks a genuinely interesting question and designs a methodologically sophisticated multi-track investigation. Cross-architecture consistency is impressive, confound controls are thorough, and the steering-probing alignment is a strong result. However, the missing non-conflict baseline (W1) introduces fundamental interpretive ambiguity in the central claim, both language pairs are CJK (W3), bootstrap n=100 is inadequate for the precision required (W2), and the SAE base-instruct mismatch (W4) weakens the cross-track validation that is the paper's structural signature. These are addressable in revision -- the non-conflict baseline and bootstrap increase are computationally trivial, and one non-CJK language pair would significantly strengthen the "universal" framing. I would raise my score to 6 if the non-conflict baseline confirms conflict-specificity and one non-CJK pair is added. |
| **Confidence** | **4 / 5** | I have examined the source code, experimental artifacts, bootstrap results, and paper text in detail. I am confident in my assessment of the methods and statistical procedures. My main uncertainty is whether the SAE analysis (Track 2) results in the "best" tier are imagined vs. actual -- this does not affect my evaluation of Track 1, which is grounded in real experimental results. |

### Recommendation

**Marginally below acceptance threshold (5/10). Revise and resubmit.**

The paper presents a well-motivated investigation at a productive intersection of two fields, with a commendable hypothesis-driven design and multi-track evidence structure. The cross-architecture consistency of the asymmetry effect and the probing-steering alignment are strong results.

However, three issues prevent acceptance in current form:

1. **The missing non-conflict baseline is a fatal gap for the central claim.** Without demonstrating that the directional asymmetry is conflict-specific rather than a general property of cross-lingual transfer, the paper's main contribution is underdetermined. This is a cheap experiment that must be run.

2. **Typological diversity is insufficient for "universal" claims.** Two CJK language pairs cannot distinguish H1 (universal English anchoring) from a CJK-specific pattern. One Indo-European pair would substantially strengthen the evidence.

3. **Statistical infrastructure needs tightening.** Bootstrap n=100 is below standard for the precision required by the paper's claims. The r=-0.71 on 3 points should not be reported as a statistical finding. MLP overfitting needs to be ruled out.

The paper's strengths -- novel question, clean experimental design, honest reporting, and genuine triangulation -- position it well for acceptance after revision. The required experiments are computationally inexpensive (non-conflict baseline, bootstrap increase) or moderately expensive (one non-CJK language pair). I encourage the authors to address W1-W3 and resubmit.
