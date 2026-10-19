---
dream_id: dream_20260520T211832
tier: median
overall_score: 3/6 Weak Reject
timestamp: 2026-05-20T22:02:15.282023+00:00
---

# Dream Review Report — Causal Style Decomposition

**Paper**: *Causal Style Decomposition: Revealing Axis-Dependent Style Bias in LLM Judges via Counterfactual Pairwise Comparison*
**Dream ID**: 20260520T211832
**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-20

---

## Reviewer Assignments

- **R1** (Method + Experiments): Focused on methodological soundness, statistical rigor, experimental design, and coverage relative to the imagined experiment plan.
- **R2** (Novelty + Related Work): Focused on contribution significance, positioning against prior work, framing, and whether the paper meets the bar for a top ML venue.

---

## R1 Review: Method and Experiments

### Summary
CSD proposes a three-stage pipeline (counterfactual generation → NLI+BERTScore verification → position-controlled pairwise comparison) to detect per-axis causal style bias in LLM judges. The paper covers 3 judges × 3 benchmarks × 4 style axes, with the headline finding that pairwise comparison is ~5× more sample-efficient than Likert scoring for detecting moderate style bias.

### Strengths
- **C2 (Likert vs Pairwise) is the strongest and most novel empirical contribution.** The systematic demonstration across 9 judge×benchmark cells that pairwise detects biases invisible to Likert (4/4 pairwise-significant combos have Likert NS) has direct methodological implications. The GPT-4o×LLMBar case is particularly striking: Likert ATE is -0.102 (wrong direction) while pairwise gives 69.1% formal win rate (p=0.006).
- **Position-controlled dual-direction pairwise design is methodologically sound.** Presenting pairs in both orders and requiring consistency cleanly separates position bias from style bias.
- **Verbosity failure is presented with intellectual honesty.** NLI 65% / BERTScore 27% correctly triggers the dual-gate filter, demonstrating the verification stage works as intended (Table 7).
- **Three-pronged robustness strategy is well-designed.** Original-preference control (58.8%, p=0.078), scaled replication (n=500, p<0.001), and rewriter ablation (Llama 67.4% vs Qwen 69.1%, Fisher p=0.812) each address a distinct alternative explanation.
- **Full experiment plan coverage.** All 9 imagined experiments (exp-001 through exp-009) are reflected in the paper.

### Weaknesses

**W1 (Major). The Likert-Pairwise comparison conflates measurement method with statistical test.** Table 4 compares Likert ATE via paired t-test against pairwise win rate via sign test on consistency-filtered data. These are different statistical tests on different data subsets (all pairs vs. ~50-55% consistent-only). The "5× sample efficiency" claim may partly reflect the sign test's greater power on filtered binary data rather than an intrinsic advantage of pairwise comparison. A critical missing control: applying a sign test to binarized Likert scores (for each pair, does the formal version score strictly higher?) would isolate the structural advantage of pairwise from the test-choice confound. Without this, C2's headline is at risk.

**W2 (Major). No multiple comparison correction across the full test battery.** The paper conducts 27+ hypothesis tests (9 formality cells × 2 metrics, plus register, tone, original preference, scaled, rewriter) but only mentions BH correction in passing. Several borderline results are directly at risk: Claude×AlpacaEval formality (p=0.047), register GPT-4o (p=0.048). The paper acknowledges register's p=0.048 doesn't survive Bonferroni (p_adj≈0.14) but doesn't apply correction systematically. After family-wise correction, the significant formality count likely drops from 4/9 to 2-3/9.

**W3 (Major). Formality and register axes likely overlap, weakening the "decomposition" framing.** The paper acknowledges register and formality are "conceptually related (r≈0.7 in sociolinguistic feature space)" but provides no empirical axis independence test. No correlation between formality and register counterfactual changes on the same items is reported. If register is a subset of formality's linguistic scope, C3's "multi-axis" claim reduces to "one axis works, and its variants also partially work."

**W4 (Moderate). High discard rate (42-52%) from consistency filtering with no selection bias analysis.** Discarding position-inconsistent pairs is methodologically motivated, but nearly half the data is removed. Consistent pairs might be those with larger quality gaps, biasing toward cases where style manipulation co-occurs with perceptible quality differences. No analysis of consistent vs. inconsistent pair characteristics (NLI score, length, task type) is provided.

**W5 (Moderate). Tone and register tested only on LLMBar.** Formality has the full 3×3 matrix, but tone and register are each tested on a single benchmark. This asymmetry prevents determining whether the axis ordering (formality > register > tone) holds across benchmarks or is benchmark-specific.

**W6 (Minor). No counterfactual examples shown.** Readers cannot evaluate the operational meaning of "formal vs. casual" rewrites, or assess whether NLI might miss subtle content changes. 2-3 annotated examples would substantially aid evaluation.

**W7 (Minor). Original-preference control is single-judge, single-benchmark (GPT-4o × LLMBar).** If original preference varies by judge or benchmark, the 0.088 correction factor may not generalize.

**W8 (Minor). Scaled replication only covers the strongest cell.** Replicating a weaker cell (e.g., Claude×AlpacaEval, which loses significance after correction) would be more informative.

### Questions for Authors
1. If you apply a sign test to binarized Likert scores (does formal version score strictly higher per pair?), does the Likert-Pairwise gap persist? This is critical for C2.
2. What is the correlation between formality and register counterfactual changes on the same items?
3. After Holm-Bonferroni correction across all 9 formality pairwise tests, how many remain significant?
4. Can you report NLI score distributions and response length for consistent vs. inconsistent pairs?
5. Does the direction asymmetry (formal→casual 78.8% vs casual→formal 54.5%) replicate across judges?

### Score: 3.5 / 6 (Borderline)
### Confidence: 4 / 5

---

## R2 Review: Novelty and Related Work

### Summary
The paper combines counterfactual text generation, content verification gates, and pairwise comparison into a pipeline (CSD) for detecting per-axis style bias in LLM judges. It claims three contributions: a detection method (C1), a measurement insight showing pairwise superiority over Likert (C2), and a multi-axis bias spectrum (C3).

### Strengths
- **C2 is a genuinely actionable methodological insight.** The demonstration that Likert scoring can yield wrong-direction estimates (GPT-4o ATE = -0.102) while pairwise comparison clearly detects the effect has direct practical implications for evaluation audit methodology.
- **Clean experimental design.** The 3×3×3 structure (judges × benchmarks × axes) with consistent methodology is above community norms. The paper does not cherry-pick settings.
- **Honest limitations section.** The paper explicitly acknowledges that "multi-axis" framing overstates evidence, that only formality produces robust multi-judge/multi-benchmark evidence, and that AlpacaEval results don't survive correction.
- **The verbosity negative control is well-used.** Rather than hiding the failure, it demonstrates principled method boundaries and validates the verification gate.
- **Rewriter robustness check** (two model families producing indistinguishable results) addresses an important confound.

### Weaknesses

**W1 (Major). Novelty is incremental — CSD combines known components.** The counterfactual generation approach follows prior work on counterfactual data augmentation for bias detection (Lu et al. 2020). The NLI+BERTScore verification is standard in style transfer evaluation. Position-controlled pairwise comparison is well-established (Zheng et al. 2024). The combination is useful but not methodologically innovative. The paper's novelty rests primarily on applying this combination to LLM judge style bias, which is an application contribution rather than a method contribution.

**W2 (Major). Significant missing related work.**
- **RATE (ICML 2025)** introduced the double-rewrite ATE protocol that Section 5.5 directly mirrors. The original-preference control in Table 8 appears to follow RATE's methodology without citation.
- **Counterfactual style/rhetorical intervention papers** (2025-2026) that apply similar counterfactual rewriting to detect bias in LLM evaluation are not discussed.
- **FairJudge and related debiasing frameworks** that also propose detection+correction pipelines are absent.
- The bibliography contains only 10 references, which is thin for a paper claiming to survey and advance the style bias detection field.

**W3 (Major). C3 (axis spectrum) is oversold relative to evidence.** The "multi-axis decomposition" framing implies systematic coverage, but the evidence supports a narrower conclusion: formality is the only axis with robust multi-judge evidence. Register is borderline on one judge only (GPT-4o, p=0.048, doesn't survive correction). Tone is marginal on one judge only (GPT-4o, p=0.092). Verbosity fails entirely. The "prestige dimension" interpretation is interesting but speculative — it's post-hoc pattern-matching on 3 data points where only 1 is robust.

**W4 (Moderate). Detection without correction limits practical impact.** Unlike LC-AlpacaEval (Dubois et al. 2024), which provides both detection and debiasing via regression, CSD only detects bias without offering a correction or mitigation strategy. The paper's "actionable guidance" amounts to "use pairwise instead of Likert," which is a measurement recommendation rather than a solution.

**W5 (Moderate). The paper frames C1 (detection method) as a contribution, but the detection capability is limited.** Only 4/9 judge×benchmark formality combinations are significant before correction, dropping to 2/9 after original-preference correction. CSD fails entirely on MT-Bench (0/3 significant). The method's detection power is narrow: it works well on short instruction-following text (LLMBar) with frontier judges, but this is a specific regime rather than a general capability.

**W6 (Minor). Framing tension between "decomposition" and single-axis results.** The title promises "Causal Style Decomposition" but the paper delivers "Causal Formality Detection." The decomposition framing implies separating style into independent axes and measuring each; instead, only one axis works, and the other two are correlated with it.

### Questions for Authors
1. How does CSD differ from the counterfactual rhetorical intervention approaches published in 2025? What does CSD offer that those methods do not?
2. Why is RATE not cited given that Section 5.5 appears to follow its protocol?
3. Could you add a concrete mitigation strategy — e.g., using CSD scores to re-weight or adjust judge outputs — to strengthen practical impact?
4. Is there evidence that formality, register, and tone capture genuinely independent bias axes, or are they all measuring the same "prestige" confound?

### Score: 3.0 / 6 (Weak Reject — Findings-level)
### Confidence: 4 / 5

---

## Roundtable Discussion

### Step 2: Cross-Sharing

**Points of agreement:**
1. **C2 is the paper's strongest and most valuable contribution.** Both reviewers identify the Likert-vs-Pairwise measurement gap as the headline finding with genuine practical implications.
2. **C3 is oversold.** Both agree that "multi-axis decomposition" overstates the evidence — only formality works robustly; register and tone provide at best suggestive single-judge results.
3. **Formality-register overlap undermines the decomposition claim.** The paper's own r≈0.7 estimate and the lack of axis independence testing weaken C3.
4. **Missing related work.** Both note the bibliography is thin (10 refs). R2 identifies specific missing citations (RATE, counterfactual rhetoric papers).
5. **Honest limitations section is appreciated.** Both credit the paper for transparently acknowledging the gaps.

**Points of disagreement:**
1. **Severity of novelty concern.** R1 rates the methodological contribution as adequate (3.5) given the empirical findings; R2 sees the combination of known techniques as insufficient for main conference (3.0). After discussion: the combination IS useful and the specific application (LLM judge style bias) is timely, but the paper needs to be more explicit about what is new vs. assembled from prior work.
2. **Severity of W1 (test-choice confound for C2).** R1 considers this a critical threat that could invalidate the headline claim; R2 accepts C2 more readily. After discussion: R1's concern is valid — the same-test control is needed. However, even if the gap narrows, the wrong-direction Likert ATE (GPT-4o = -0.102) is independently damning for Likert reliability, so C2 would survive in weakened form.

### Step 3: Convergence

**Agreed assessment:**
- The paper addresses a timely and important problem (style bias in LLM judges).
- The experimental design is systematic and above community norms in coverage.
- C2 (measurement insight) is the primary contribution and is useful regardless of novelty debates.
- C1 (detection) is valid but narrow: works on formality on LLMBar with frontier judges, much weaker elsewhere.
- C3 (axis spectrum) is oversold and should be reframed as preliminary/suggestive.
- Novelty is incremental — the pipeline assembles known components for a new application.
- Several methodological gaps need addressing: test-choice confound for C2, multiple comparison correction, consistency filter bias analysis.
- Missing key citations (RATE, counterfactual rhetoric work).

**Agreed score range: 3.0–3.5** (between Weak Reject and Borderline Conference).

### Step 4: Consolidated Assessment

**Overall Score: 3 / 6 (Weak Reject)**

**Justification:** The paper tackles a relevant problem and provides a systematic empirical study with transparent reporting. The C2 finding (Likert is ~5× less efficient than pairwise, and can give wrong-direction estimates) is the standout contribution with practical value. However, three factors prevent a higher score:

1. **Incremental novelty.** CSD assembles known components (counterfactual generation, NLI verification, pairwise comparison) without methodological innovation. The related work section misses key prior work that further narrows the novelty gap.

2. **Narrow empirical support for two of three claims.** C1 (detection) works robustly only for formality on LLMBar with frontier judges (2/9 combos survive correction). C3 (axis spectrum) has only one clean axis. The "decomposition" framing in the title overprises what is essentially a single-axis detection study with suggestive multi-axis pilots.

3. **Methodological gaps in the headline claim.** C2's "5× efficiency" conflates measurement method with statistical test choice. The missing same-test control (sign test on Likert scores) leaves open whether the gap is structural or artifactual. Multiple comparison correction is needed but not applied consistently.

**Strengths that could upgrade with revision:**
- If the sign-test-on-Likert control confirms C2, the measurement insight becomes a solid contribution for Findings.
- Adding 2-3 more style axes with clean results would substantiate C3.
- Proper citation of RATE and framing of novelty relative to counterfactual rhetoric work would improve positioning.
- Adding a mitigation strategy (not just detection) would increase impact.

**Recommendation:** Below the threshold for main conference acceptance at a top ML venue. The C2 measurement insight is Findings-worthy if the test-choice confound is addressed. Suggest reframing around C2 as primary contribution, downgrading C3 to exploratory, adding missing citations, and performing the same-test Likert control.

---

## Key Revision Recommendations

1. **Add the sign-test-on-Likert control** to isolate pairwise's structural advantage from test-choice effects.
2. **Apply Benjamini-Hochberg correction** across all hypothesis tests and report both corrected and uncorrected p-values consistently.
3. **Analyze consistency filter bias** — compare NLI scores, lengths, and task types between consistent and inconsistent pairs.
4. **Test axis independence** empirically (correlation between formality and register counterfactual shifts).
5. **Cite RATE** and position the original-preference control relative to that protocol.
6. **Expand bibliography** — 10 references is thin; add counterfactual rhetoric work, FairJudge, and other 2025-2026 style bias papers.
7. **Reframe title and C3** — "Causal Formality Bias Detection" is more honest than "Causal Style Decomposition" given current evidence.
8. **Add counterfactual examples** — 2-3 annotated formal/casual pairs with NLI/BERTScore values.
9. **Extend register/tone to AlpacaEval** to test whether the axis ordering generalizes beyond LLMBar.

---

## Scores Summary

| | R1 (Method) | R2 (Novelty) | Consolidated |
|--|-------------|-------------|-------------|
| Score | 3.5 / 6 | 3.0 / 6 | **3.0 / 6** |
| Confidence | 4 / 5 | 4 / 5 | 4 / 5 |
| Recommendation | Borderline | Weak Reject | **Weak Reject** |

**Consolidated: 3 / 6 — Weak Reject (Findings-level with revisions)**
