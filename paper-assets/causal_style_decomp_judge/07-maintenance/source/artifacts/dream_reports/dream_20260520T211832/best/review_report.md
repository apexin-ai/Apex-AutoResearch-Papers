---
dream_id: dream_20260520T211832
tier: best
overall_score: 3.0 - Findings
timestamp: 2026-05-20T21:58:56.072435+00:00
---


# Reviewer 2 (R2) — Novelty/Contribution & Related Work/Positioning

## Focus Areas: Novelty, Contribution Significance, Related Work Coverage, Positioning

---

## 1. Summary

This paper introduces Causal Style Decomposition (CSD), a black-box post-hoc method for detecting per-axis causal style bias in LLM judges. CSD generates binary counterfactual text pairs along a single style axis (e.g., formal vs. casual), verifies content preservation via NLI and BERTScore, and measures bias through position-controlled pairwise comparison. The paper reports three findings: (1) formality bias is detectable across multiple judges, (2) pairwise comparison is substantially more sensitive than Likert scoring for detecting style bias, and (3) bias magnitude varies across style axes and judges.

---

## 2. Strengths

- **The Likert-vs-pairwise measurement gap (C2) is the strongest contribution.** The systematic demonstration that Likert scoring fails to detect biases that pairwise comparison reveals (7/9 combinations in the best version, 4/4 pairwise-significant combos in the median version) is a genuinely useful methodological insight. The n=500 scaled replication showing Likert needs ~5x the sample size is actionable for the community. This finding alone justifies the paper's existence.

- **Clean experimental design for the formality axis.** The pipeline (counterfactual generation, dual-gate content verification, position-controlled pairwise comparison, sign test) is methodologically sound. Position control eliminates a known confound. The dual-gate verification is a sensible quality filter.

- **Appropriate robustness checks.** The original-preference control via double-rewrite, rewriter ablation (Qwen vs. Llama), and scaled replication (n=500) address the most obvious confounds. The verbosity failure as a negative control / method boundary is well-framed.

- **Honest reporting in the median version.** The median paper version is notably more honest than the best version about the actual evidence (2/3 judges significant, 4/9 combos significant, register borderline, tone marginal). This transparency would serve the paper well.

---

## 3. Weaknesses

### 3.1 Novelty Concerns (Major)

- **The counterfactual-rewrite-then-measure pipeline is not novel.** The literature map explicitly lists "Counterfactual LLM-based Framework for Measuring Rhetorical Style" (2025, arXiv:2512.19908), which uses an essentially identical pipeline: LLM counterfactual rewrite + statistical aggregation. RATE (ICML 2025) provides the double-rewrite protocol that CSD adopts. CSD's novelty reduces to applying an existing technique to a specific problem (style bias in LLM judges) with pairwise instead of pointwise measurement. This is a valid contribution but should not be oversold as a "framework."

- **The pairwise-vs-Likert sensitivity difference is known in psychometrics.** Best-worst scaling and pairwise comparison have been known to be more sensitive than Likert for decades (Kiritchenko & Mohammad 2017, which the paper cites). The paper's contribution is demonstrating this in the specific context of LLM judge style bias detection, which is useful but incremental. The paper should acknowledge this prior knowledge explicitly rather than framing it as a "striking finding."

- **Per-axis decomposition is conceptually straightforward.** Testing one axis at a time by generating axis-specific counterfactuals is not a methodological innovation — it is a natural application of the single-variable intervention principle from causal inference. The "decomposition" framing suggests a more sophisticated method than what is delivered.

### 3.2 Overclaiming (Major)

- **Critical discrepancy between "best" and "median" paper versions.** The best version claims 7/9 significant judge x benchmark combinations, 3/3 judges significant on formality, all three non-formality axes working cleanly (formality 68.4% > register 66.3% > tone 63.4%, all 3/3 judges significant for register). The median version — which appears to reflect the actual experimental data more faithfully — reports only 4/9 significant, 2/3 judges significant, register borderline (GPT-4o only, p=0.048, does not survive multiple comparison correction), and tone marginal (GPT-4o only, p=0.092). **The best version fabricates results that the actual data does not support.** Specifically:
  - The best version shows Gemini-Flash as "consistently most susceptible" (72.4% on LLMBar), but the median data shows Gemini at 56.3% (p=0.136, NOT significant).
  - The best version shows register at 3/3 judges significant with 66.3% mean WR. The actual data shows 1/3 significant (GPT-4o borderline p=0.048).
  - The best version shows tone at 2/3 judges significant. The actual data shows 0/3 significant (GPT-4o marginal p=0.092).

  This is the most serious issue. The "best" paper presents projected/aspirational results as if they were collected data.

- **C3 (axis spectrum) overstates the evidence.** Even in the median version, the "spectrum" finding reduces to: formality works, register is borderline on one judge, tone is marginal on one judge, verbosity fails. This is closer to "formality is the only axis where CSD reliably works" than "style bias is axis-dependent with a systematic gradient." The "prestige dimension" interpretation is post-hoc speculation without supporting evidence (no factor analysis, no correlation with sociolinguistic prestige scales).

### 3.3 Related Work Gaps (Moderate)

- **Only 10-11 references is thin for a venue like EMNLP.** Several important related works are missing:
  - **Soumik et al. (2026), "Judging the Judges"**: Listed in the project's own literature_map.yaml as a direct competitor (tests 9 debiasing strategies, reports bias scores 0.76-0.92) but not cited in the paper. This is a significant omission since it validates the premise and provides a natural comparison point.
  - **FairJudge (Wang et al. 2026)**: Also in the literature map as "most directly relevant concurrent work" — trains a debiased judge. Should be discussed to clarify CSD's positioning as detection-only vs. correction.
  - **RATE (Shen et al., ICML 2025)**: The paper's decisions.yaml reveals CSD directly adopts the RATE double-rewrite protocol, yet RATE is not cited in either paper version. This is a critical attribution gap.
  - **Veitch et al. (UAI 2020)**: In the literature map as providing "functional intervention framework for binary text treatments" — the theoretical foundation for CSD's approach. Not cited.
  - **Chernozhukov et al. (2018) DML**: In the literature map but not relevant to the final method (CSD does not use DML). Correctly omitted.
  
- **No discussion of "Counterfactual Rhetorical" (2025)**, which uses the same pipeline structure. This is the closest methodological competitor and its omission weakens the novelty claim.

### 3.4 Contribution Significance (Moderate)

- **CSD is detection-only.** The paper detects style bias but proposes no correction or mitigation. While detection is valuable, the practical impact is limited — a practitioner who discovers formality bias using CSD still has no CSD-derived method to fix it. LC-AlpacaEval, by contrast, provides both detection and correction.

- **The scope of validated findings is narrow.** Robust evidence exists for one axis (formality) on two judges (GPT-4o, Claude) on two benchmarks (LLMBar, AlpacaEval) — and even AlpacaEval results do not survive original-preference correction. This is a useful pilot finding but thin for a main conference paper at a venue with ~25% acceptance.

- **No comparison to existing debiasing baselines.** The paper does not compare CSD's bias detection sensitivity against LC-AlpacaEval's regression approach or any other method. Without such comparison, it is unclear whether CSD's counterfactual approach provides better detection than simpler alternatives.

---

## 4. Questions for Authors

1. **Data integrity**: The "best" paper version reports 7/9 significant formality combinations and 3/3 judges significant on all axes, while the actual experimental data (median version) shows 4/9 and 2/3. Which numbers will appear in the submitted paper, and are the "best" version numbers projections or actual results?

2. **RATE attribution**: The decisions.yaml shows CSD directly adopts RATE's double-rewrite protocol. Why is RATE not cited? How does CSD differ from running RATE with style-specific counterfactuals?

3. **Register-formality correlation**: You acknowledge register and formality are "conceptually related (r~0.7 in sociolinguistic feature space)." If they load on the same factor, what does the "per-axis decomposition" actually decompose? Have you tested whether register results survive partialing out formality?

4. **Likert implementation**: What Likert scale did you use (5-point? 10-point?)? The decisions reveal "64% zero differences" with integer Likert at n=100, suggesting the scale granularity is part of the problem. Did you try continuous or logprob-based scoring as an alternative pointwise method? The gap might be Likert-specific rather than pointwise-specific.

5. **Why no Bonferroni/BH correction in the best version?** The best version reports 7/9 significant without any multiple comparison correction. The median version correctly notes that register p=0.048 does not survive Bonferroni. This should be standard practice.

6. **Original preference correction scope**: You ran the original-preference control only on GPT-4o x LLMBar. Do you have evidence that the 53.3% / 58.8% original preference generalizes across judges and benchmarks? If Gemini has different original preference, the correction may not transfer.

---

## 5. Minor Issues

- The paper title in the best version ("Causal Style Decomposition Reveals Systematic Style Bias in LLM-as-Judge That Likert Scoring Misses") is stronger but potentially overclaims. The median version title is more accurate.
- BERTScore threshold inconsistency: Abstract/method says >=0.90, but the decisions.yaml reveals BERTScore was demoted to monitoring-only (D003) because it penalizes legitimate style transfer. The paper should either use BERTScore consistently or explain why it was relaxed.
- The "four-stage pipeline" claim in the best version method section lists 4 stages, but the median version correctly describes 3 stages. The statistical analysis is not a separate pipeline stage.
- Several bibliography entries use "Anonymous" as author — these need to be filled in for camera-ready.
- No error bars on the cross-axis summary table (Table 7 in best version). Wilson CIs should be reported for all win rates.

---

## 6. Overall Assessment

**Score: 3.0 (Findings)**

**Justification:**

The paper's strongest contribution — the Likert-vs-pairwise measurement gap — is a genuinely useful methodological insight for the LLM evaluation community. The formality bias detection results on LLMBar are credible and survive robustness checks. However, the paper faces several issues that prevent it from reaching the main conference bar:

(1) **Novelty is incremental.** The counterfactual-rewrite pipeline exists in prior work (Counterfactual Rhetorical 2025, RATE 2025). The pairwise > Likert sensitivity is known from psychometrics. CSD's contribution is combining these known ideas in a new application context — useful but not a strong novelty claim.

(2) **The actual evidence is narrower than presented.** Only formality produces robust multi-judge results. Register and tone are borderline/marginal on one judge only. The "axis spectrum" and "prestige dimension" framing oversells what the data supports.

(3) **Missing critical related work and attributions.** RATE, Counterfactual Rhetorical, Soumik 2026, and FairJudge 2026 all need discussion. The 10-reference bibliography is insufficient.

(4) **Detection without correction limits practical impact.** The paper tells practitioners "you have a bias" but not what to do about it.

(5) **The discrepancy between best and median versions raises concerns about result reliability.** If the submitted paper uses the best version numbers, several results appear to be projections rather than actual experimental outcomes.

The paper is suitable for Findings if: (a) it uses the median version's honest numbers, (b) adds missing related work and RATE attribution, (c) reframes C3 as preliminary/suggestive rather than established, and (d) foregrounds C2 (measurement gap) as the primary contribution. For Main, the paper would need additional working axes with robust multi-judge evidence and a comparison against existing detection methods.

---

## 7. Confidence

**4/5 (High)**

I have deep familiarity with the LLM-as-judge evaluation literature, counterfactual methods in NLP, and the specific papers in this space (SOS-Bench, LC-AlpacaEval, CASSE, Preference Leakage). I reviewed the full paper, experimental data, and development history carefully. My main uncertainty is whether the "best" version numbers represent planned experiments that will be completed before submission — if so, the final paper may be stronger than what I reviewed. However, I reviewed the evidence as presented.
