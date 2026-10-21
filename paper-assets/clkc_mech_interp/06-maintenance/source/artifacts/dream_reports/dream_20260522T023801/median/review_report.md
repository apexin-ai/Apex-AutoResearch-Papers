---
dream_id: dream_20260522T023801
tier: median
overall_score: 5 - Marginally below acceptance threshold
timestamp: 2026-05-22T03:28:56.687763+00:00
---

# ICLR Review Report: Cross-Lingual Knowledge Conflict Signals in Multilingual LLMs

**Paper:** Cross-Lingual Knowledge Conflict Signals in Multilingual LLMs: Directional Asymmetry, Layer Structure, and Causal Probing
**Venue:** ICLR (inferred)
**Review mode:** Full roundtable (2 Reviewers + Chair convergence)
**Date:** 2026-05-22

---

## Reviewer Panel

- **R1** — Focus: Methods + Experiments
- **R2** — Focus: Novelty + Related Work
- **Chair** — Convergence moderator

---

## Step 1: Independent Reviews

### R1 (Methods + Experiments)

**Scores:** Overall 5/10 | Soundness 3/4 | Presentation 3/4 | Contribution 2/4 | Confidence 4/5

**Strengths:**
- Hypothesis-driven H1/H2 framework with pre-registered competing hypotheses
- Three-track convergence design (probing → SAE → steering)
- Remarkable cross-architecture effect-size consistency (CV < 6%): Llama 7.22pp, Qwen 7.18pp, Gemma 5.4pp → pooled 6.60±1.04pp, I²=0%
- Thorough confound exclusion pipeline: COMET tercile ablation, token-overlap Jaccard analysis, label-noise robustness testing

**Critical/Major Weaknesses:**

1. **[CRITICAL] Missing non-conflict semantic baseline (W1).** The X→EN > EN→X asymmetry could be a general property of any cross-lingual probing task on English-dominant models, not conflict-specific. Without probing a non-conflict task (e.g., sentiment, entailment) on the same activations, the central contribution is underdetermined. This experiment is computationally trivial.

2. **[MAJOR] Statistical infrastructure gaps (W2).** Bootstrap n=100 is below the n≥1000 standard (Efron & Tibshirani 1993), making CI endpoints volatile — consequential when Qwen's lower bound is −1.2pp. The r=−0.67 CKA-probe correlation is computed on only 3–4 data points and should not be reported as an inferential statistic. MLP overfitting risk (256 units on ~1000 samples) is not ruled out via cross-validation or train/test gap reporting.

3. **[MAJOR] Insufficient typological diversity (W3).** Both language pairs (EN↔ZH, EN↔JA) are CJK. The "universal" framing of H1 requires at least one Indo-European pair (EN↔DE or EN↔FR) to distinguish English-anchored universality from a CJK-specific pattern.

4. **[MODERATE] Probe accuracy ceiling (W5).** 69–77% balanced accuracy vs. prior monolingual ~90% is unexplained. Needs explicit discussion.

5. **[MODERATE] Steering non-responders (W7).** At α=3.5, 66% of samples do not flip. No analysis of what distinguishes responders from non-responders.

**Questions for Authors:**
- If you probe a non-conflict semantic task (e.g., sentiment), does the X→EN > EN→X asymmetry persist?
- Why only n=100 bootstrap iterations instead of the standard n≥1000?
- What is the MLP probe's held-out accuracy with proper cross-validation?
- Can you characterize steering non-responders vs. responders (entity type, confidence, difficulty)?

---

### R2 (Novelty + Related Work)

**Scores:** Overall 5/10 | Soundness 2/4 | Presentation 3/4 | Contribution 2/4 | Confidence 4/5

**Strengths:**
- Well-motivated question bridging CLEAR's behavioral findings to internal representations
- H1/H2 hypothesis structure is exemplary for interpretability work
- Cross-architecture effect-size consistency (6.6±0.9pp, I²=0%) is genuinely compelling
- Confound-exclusion pipeline is thorough and sets a methodological standard

**Critical/Major Weaknesses:**

1. **[CRITICAL] Novelty underdetermined.** Without a non-conflict semantic baseline, the asymmetry finding could be a general property of English-dominant multilingual models rather than a conflict-specific mechanism. This is the single largest threat to the paper's contribution.

2. **[MAJOR] Two of three tracks incomplete.** Track 2 (SAE) is inconclusive due to base–instruct mismatch (cosine similarity 0.71). Track 3 (SAE-based steering) was not executed. The "three-track convergence" framing overpromises relative to deliverables. What remains is essentially a probing paper with supplementary analyses.

3. **[MAJOR] Language diversity insufficient.** Only CJK language pairs tested. At least one Indo-European pair needed for "universal" claims.

4. **[MAJOR] Bibliography too thin.** 18 references vs. expected 35–50 for ICLR. Missing critical citations including Conneau et al. (2020) on XLM-R probing, other multilingual interpretability work from 2024–2026, and the broader knowledge editing literature.

5. **[MODERATE] H1-vs-H2 discrimination weak.** CKA conflict/non-conflict diff = 0.08 (too small), Jaccard inconclusive (p=0.38), only probe transfer directionality is suggestive. Evidence is "consistent with H1" not "discriminates H1 from H2."

6. **[MODERATE] "First mechanistic account" claim needs qualification.** Wendler et al. (2024) and SpARE (Wu et al. 2025) overlap in scope.

**Path to acceptance (R2's view):** Add non-conflict baseline + one non-CJK language pair + fix SAE mismatch OR reframe as a focused probing paper. Any two of three would likely suffice.

---

## Step 2: Cross-Sharing

R1 and R2 exchanged reviews. Key observations:

- **Both independently identified the non-conflict baseline as the CRITICAL gap** — strong signal that this is not a niche concern but a fundamental design issue.
- R1 was more generous on soundness (3/4 vs R2's 2/4), reflecting R1's appreciation of the confound pipeline; R2 weighted the baseline gap more heavily against soundness.
- R2 identified bibliography thinness and framing overreach that R1 did not flag; R1 identified statistical methodology gaps (bootstrap n, MLP overfitting) that R2 mentioned only tangentially.

---

## Step 3: Convergence Discussion

### Consensus Points (no dispute)

1. **The research question is well-motivated.** Mechanistic explanation for CLEAR's linguistic-affinity finding is a genuine gap.
2. **Cross-architecture effect-size consistency is the paper's strongest asset.** 6.60±1.04pp with I²=0% across three architectures spanning two design families (GQA vs. parallel attention) is compelling.
3. **The confound-exclusion pipeline is thorough** and constitutes a genuine methodological contribution.
4. **[CRITICAL] Non-conflict baseline is missing.** Both reviewers independently identified this as the single largest threat.
5. **Language diversity is insufficient** for current claims.
6. **Track 2/3 incomplete** relative to framing.

### Disagreements and Chair Adjudication

**2a. Severity of three-track framing overreach:**
- R1: MODERATE. Evaluates probing results on their own merits.
- R2: MAJOR. Framing overpromises; paper is "essentially a probing paper."
- **Chair ruling: MAJOR.** R2 is correct in substance — Track 2 produced noisy results (base–instruct cosine 0.71) and Track 3 was not executed. However, the paper does deliver three distinct analytical approaches (probing + CKA/SVCCA + probe-weight steering), even if not the originally advertised SAE-based tracks. The title/framing must be revised, but the underlying work has more substance than "just probing."

**2b. Soundness score divergence (R1: 3, R2: 2):**
- **Chair ruling: 2.** The missing non-conflict baseline is a soundness issue, not just a contribution issue. Until it's addressed, we cannot determine whether the measured signal is conflict-specific.

**2c. Statistical methodology (R1 flagged, R2 did not):**
- **Chair ruling: MAJOR (aggregated).** Bootstrap n=100 is genuinely below standard and affects CI reliability. CKA-probe correlation on 3 points must be reframed as descriptive. MLP overfitting requires cross-validation. Each sub-issue is individually MODERATE but they compound.

**2d. Bibliography depth (R2 flagged, R1 did not):**
- **Chair ruling: MAJOR for submission readiness.** 18 references is inadequate for ICLR. However, this is easily fixable (writing work, not experimental work).

**2e. H1-vs-H2 discrimination:**
- **Chair ruling: MODERATE.** The paper should honestly frame this as "evidence consistent with H1" rather than "discrimination between H1 and H2."

---

## Step 4: Consolidated Assessment

### Converged Scores

| Dimension | R1 | R2 | **Converged** | Rationale |
|-----------|----|----|---------------|-----------|
| **Overall** | 5 | 5 | **5** | Below acceptance threshold. Strong empirical core but CRITICAL baseline gap and MAJOR framing/diversity issues. |
| **Soundness** | 3 | 2 | **2** | Missing non-conflict baseline is a soundness issue. Statistical methodology gaps compound. |
| **Presentation** | 3 | 3 | **3** | H1/H2 framework and experimental structure are clear. Framing overpromises relative to deliverables. |
| **Contribution** | 2 | 2 | **2** | Until non-conflict baseline is run, the contribution is underdetermined. If baseline passes, rises to 3. |
| **Confidence** | 4 | 4 | **4** | Both reviewers confident; full experimental data accessed. |

### Consolidated Strengths

**S1. Well-motivated mechanistic question** bridging CLEAR's behavioral findings to internal representations, with exemplary hypothesis-driven structure (H1 vs. H2).

**S2. Cross-architecture effect-size consistency** is the paper's most compelling result. The pooled asymmetry of 6.60±1.04pp across three architectures (Llama/Qwen/Gemma) with I²=0% and Cochran's Q p=0.68 is genuinely interesting — this is not an architecture-specific artifact.

**S3. Rigorous confound exclusion pipeline.** Token overlap analysis (Jaccard 3–4%, negative correlation), COMET translation-quality ablation, and label-noise robustness testing (4% error rate → ~1pp degradation) collectively address the most plausible confounds. This pipeline is a reusable methodological contribution.

**S4. Probe-weight steering provides preliminary causal evidence** beyond pure correlation. The 34% flip rate vs. 6% random control (Cohen's d=0.41) with an informative alpha-sensitivity curve (optimal α=3.5 balancing flip rate and coherence) elevates this above a standard probing paper.

**S5. CKA/SVCCA layer analysis** connects conflict signal peaks to the language-transition window identified by Wendler et al. (2024), providing a mechanistic narrative for why conflict signals emerge at specific depths.

### Consolidated Weaknesses (ranked by severity)

**[CRITICAL] W1 — Missing non-conflict semantic baseline.**
The central claim (asymmetry is conflict-specific) is underdetermined without probing a non-conflict cross-lingual task on the same models and activations. If sentiment or NLI probing shows the same X→EN > EN→X pattern, the paper's contribution collapses to documenting a general cross-lingual probing asymmetry on English-dominant models. This experiment is computationally trivial (hours, not days) and must be run before any resubmission.

**[MAJOR] W2 — Three-track framing overpromises.**
Track 2 (SAE) is inconclusive due to base–instruct distribution mismatch (cosine similarity 0.71). Track 3 (SAE-based steering) was not executed. The probe-weight steering partially compensates, but the paper as framed advertises convergent evidence from three independent methods and delivers one complete track (probing) plus supplementary analyses (CKA, steering). Must reframe honestly.

**[MAJOR] W3 — Language diversity insufficient for "universal" claims.**
Primary results on EN↔ZH (CJK). Supplementary EN↔JA (also CJK, n=680, not significant). No Indo-European pair tested. Cannot claim "language-independent" mechanism without typological diversity. At minimum, one EN↔DE or EN↔FR pair is needed.

**[MAJOR] W4 — Statistical methodology gaps.**
(a) Bootstrap n=100 below the n≥1000 standard, making CI endpoints volatile — consequential when Qwen's lower bound is −1.2pp. (b) CKA-probe correlation r=−0.67 computed on 3 data points — cannot be reported as an inferential statistic. (c) MLP probe (256 units on ~1000 samples) without cross-validation or train/test gap reporting leaves overfitting concern open.

**[MAJOR] W5 — Bibliography too thin.**
18 references vs. 35–50 expected for ICLR. Missing critical citations: Conneau et al. (2020) on XLM-R cross-lingual probing, broader multilingual interpretability work from 2024–2026, knowledge editing literature. For a paper claiming "first mechanistic account," engagement with the wider literature is essential.

**[MODERATE] W6 — H1-vs-H2 discrimination weak.**
CKA conflict/non-conflict diff = 0.08 (too small for strong claims). SAE Jaccard inconclusive (0.06 vs 0.04, p=0.38). Only probe transfer directionality is suggestive of H1. Should frame as "evidence consistent with H1" not "H1 confirmed."

**[MODERATE] W7 — Probe accuracy ceiling unexplained.**
69–77% balanced accuracy vs. prior monolingual ~90% needs explicit discussion of contributing factors (cross-lingual difficulty, dataset differences, probe type, metric).

**[MODERATE] W8 — Steering non-responders uncharacterized.**
At α=3.5, 66% of samples do not flip. No analysis of what distinguishes responders from non-responders (entity type, confidence, difficulty, probe margin).

**[MODERATE] W9 — SAE base–instruct mismatch acknowledged but not addressed.**
Cosine similarity 0.71 between base and instruct distributions renders all Track 2 results noisy. Honestly reported, but undermines the cross-track validation narrative.

**[MINOR] W10 — Jaccard statistics on small feature counts.**
8 overlapping features out of 45/42 without sensitivity analysis or null-model comparison beyond permutation.

### Consolidated Questions for Authors

1. If you probe a non-conflict semantic task (e.g., sentiment polarity, NLI) using the same models and activation extraction, does the X→EN > EN→X asymmetry persist? This is the single most important experiment.
2. Why was bootstrap n set to 100 rather than the standard n≥1000? What is the computational cost of increasing it?
3. What is the MLP probe's held-out accuracy with proper k-fold cross-validation? Is the train/test gap reported anywhere?
4. Can you characterize the 66% of samples that do not flip under steering? Is there a pattern by entity type, probe confidence, or question difficulty?
5. The probe accuracy ceiling (69–77%) is substantially below prior monolingual work (~90%). What factors explain this gap?
6. Given that Track 2 and 3 are incomplete, would you consider reframing the paper as a focused probing + CKA + steering paper rather than maintaining the three-track structure?

### Experiment Coverage Assessment

Relative to the full experimental design:
- **Track 1 (Probing):** All 7 experiments executed and reported (plans 102–109). Coverage: complete.
- **Track 2 (SAE):** All 3 experiments executed but results noisy/inconclusive (plans 201–203). Honestly reported in Appendix B. Coverage: complete but inconclusive.
- **Track 3 (SAE Steering):** All 3 experiments not executed (plans 301–303). Honestly reported as deferred. Coverage: absent.
- **Overall:** 10/13 experiments executed, 7/13 produce usable results. The paper faithfully reports what was done and what wasn't.

---

## Recommendation: **Reject (with encouragement to resubmit)**

**Overall Score: 5 — Marginally below acceptance threshold**

### Rationale

The paper addresses a well-motivated question and produces genuinely interesting results. The cross-architecture consistency of the asymmetry effect (6.6±1.0pp, I²=0%) is a real finding, and the confound-exclusion pipeline sets a methodological standard for cross-lingual probing studies. The honest reporting of inconclusive SAE results (Appendix B) and deferred Track 3 experiments demonstrates scientific integrity.

However, the work cannot be accepted in its current form:

1. **The CRITICAL non-conflict baseline gap** means we cannot determine whether the central finding is conflict-specific or a general cross-lingual property of English-dominant models. This alone is sufficient grounds for rejection.
2. **The three-track framing does not match deliverables** (one complete track, two supplementary analyses).
3. **Language diversity is limited to CJK**, insufficient for the universality claims made.

The distance to acceptance is moderate, not large. The core empirical finding is sound pending the baseline check.

### Prioritized Revision Plan

**Priority 0 — Must-do before resubmission (~1 week):**
1. Run non-conflict semantic baseline (sentiment or NLI probing on same activations). If asymmetry disappears → contribution confirmed. If persists → reframe around the more general finding.
2. Increase bootstrap to n≥1000. Trivial compute cost.

**Priority 1 — Strongly recommended (~2–3 weeks):**
3. Add one non-CJK language pair (EN↔DE or EN↔FR, even n=500–700 with consistent direction substantially strengthens universality claims).
4. Reframe paper honestly: "Cross-lingual conflict probing with layer-wise analysis and preliminary causal evidence." Drop three-track convergence framing.
5. Report MLP probe cross-validation results.
6. Expand bibliography to 35+ references with proper engagement with multilingual interpretability literature.

**Priority 2 — Nice-to-have for stronger paper:**
7. Reframe CKA-probe correlation as descriptive (remove r=−0.67 inferential framing on 3 points).
8. Characterize steering non-responders.
9. Expand dataset to n≈1800 for tighter CIs (partially done per Section 4.1).
10. Discuss probe accuracy ceiling with explicit comparison to prior work.

**Estimated time to address P0+P1:** 4–6 weeks with existing compute resources.

---

引用验证失败: 目录不存在: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper