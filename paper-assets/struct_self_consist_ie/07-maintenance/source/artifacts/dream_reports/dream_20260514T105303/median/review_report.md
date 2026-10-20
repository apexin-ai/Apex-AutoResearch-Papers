---
dream_id: dream_20260514T105303
tier: median
overall_score: weak reject
timestamp: 2026-05-14T12:00:33.787800+00:00
---

# Dream Review Report

**Paper:** A Systematic Comparison of Confidence Signals for Test-Time Scaling in Structured Information Extraction
**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)
**Venue Standard:** Top ML venue (EMNLP-level, ~25% accept rate, 6-point scale)

---

## Reviewer Assignments
- **R1:** Methodology + Experimental Evaluation
- **R2:** Novelty/Contribution Significance + Related Work

---

## Step 1: Independent Reviews

### R1 (Methods + Experiments)

**Summary:** The paper systematically compares five confidence signals (SJ, LOGPROB, FK, ENTVOTE, EM) for test-time scaling in IE, across 3 NER datasets, 1 RE dataset, 2 models, and multiple metrics. The main claims are that SJ is the best consistency-based signal, LOGPROB is a competitive zero-cost baseline capturing complementary information, and all signals face a task-complexity boundary on RE.

**Strengths:**
1. **Comprehensive experimental matrix.** 3 NER datasets × 2 models × 2 temperatures × 2 sample budgets × 4 evaluation metrics. The breadth of ablations is commendable and exceeds what most comparison papers provide.
2. **RE threshold sensitivity analysis (Table 3) is the paper's strongest finding.** The monotonic divergence of SJ (↑ .234→.395) and LOGPROB (↓ .267→.185) as knowledge-gap instances are filtered is a genuinely insightful diagnostic that reveals fundamentally different signal sources.
3. **LOO-SJ circularity check.** Δρ=−0.014 directly addresses a natural methodological concern. The minimal degradation is reassuring and the approach is appropriate.
4. **SJ temperature invariance (Table 7).** Δρ≤0.01 vs FK's Δρ=0.062 is a practically important finding — SJ eliminates temperature tuning as a hyperparameter.
5. **Multiple evaluation metrics.** Using ρ, τ, AUROC, and ECE together provides a more complete picture. The finding that SJ wins discrimination metrics while LOGPROB wins calibration (ECE) is informative.
6. **Honest reporting of negative/mixed results.** LOGPROB winning on CoNLL, the indistinguishable WNUT result, and the RE degradation are all reported transparently.

**Weaknesses:**
1. **(Major) Claim 1 framing overstates the evidence.** The abstract says SJ "consistently outperforms" surface consistency, which is supported. But the paper also frames SJ as the leading signal overall. On CoNLL-2003, LOGPROB outperforms SJ (ρ=.361 vs .348, AUROC .715 vs .701). On WNUT-17, they are statistically indistinguishable (p=.85). SJ leads clearly only on SciERC. The "consistent" advantage of SJ is limited to comparisons against FK/EM, not against LOGPROB. The paper acknowledges this in §5.1 text but the abstract and conclusion don't sufficiently caveat it.
2. **(Major) Best-of-N F1 differences are not practically significant.** Table 11: SJ vs LOGPROB differences are ≤0.5pp across all datasets, with no statistical significance reported. This is the "so what" experiment — if the best confidence signal can't produce meaningfully better selections than the zero-cost baseline, the practical value proposition of multi-sample consistency is weak. The paper should report bootstrap CIs on these F1 differences.
3. **(Major) RE task-complexity boundary rests on a single dataset.** SciERC RE (n=397) is the sole evidence for Claim 3. Without TACRED, DocRED, or ACE05, the "boundary" could be an artifact of SciERC's specific relation type distribution or annotation scheme. The compound error propagation argument is plausible but not empirically validated beyond one dataset.
4. **(Moderate) Cross-model validation reveals SJ fragility.** Table 8: SJ degrades −0.057 (Qwen→LLaMA) while LOGPROB degrades only −0.014 (4× less). This suggests LOGPROB is the more robust signal across architectures, directly contradicting the narrative that SJ is the preferred signal. The paper reports this honestly but doesn't adequately discuss the implication: SJ's advantage may be model-specific.
5. **(Moderate) Inverted-U capability stratification has circularity.** F1-stratified result (p=0.032) uses F1 as both stratification variable and evaluation target. The independent proxy (sentence length) yields p=0.078, not significant. The paper hedges appropriately ("may be partially inflated"), but the finding is presented as a numbered section (§5.8) suggesting more weight than the evidence supports.
6. **(Minor) Missing SJ+LOGPROB ensemble.** The paper identifies signal complementarity as a key finding and mentions ensemble as future work, but a simple linear combination experiment would strengthen the contribution significantly and is straightforward to implement.

**Questions for Authors:**
1. Can you report bootstrap 95% CIs on the Best-of-N F1 differences (Table 11)? If SJ vs LOGPROB is not significant in downstream F1, how do you justify the 8× inference cost of multi-sample SJ?
2. Given SJ's larger cross-model degradation (−0.057 vs −0.014 for LOGPROB), under what conditions would you recommend SJ over the zero-cost LOGPROB baseline in practice?
3. Have you measured instance-level Pearson/Spearman correlation between SJ and LOGPROB scores? If they capture orthogonal information, a simple weighted combination should outperform both — why not include this experiment?

**R1 Scores:**
- Methodology: **4/6** — Sound formulation, appropriate metrics, LOO-SJ addresses circularity. Deducted for capability stratification circularity and missing ensemble experiment.
- Experiments: **3/6** — Good coverage in datasets/models/ablations. Deducted for single RE dataset, non-significant Best-of-N differences undermining practical claims, and missing CI reporting on key comparisons.
- Overall: **3/6** (Weak Reject)
- Confidence: **4/5**

---

### R2 (Novelty + Related Work)

**Summary:** The paper applies known similarity metrics (soft Jaccard, Fleiss' Kappa, majority voting) and a standard model-internal signal (log-probability) in a known framework (self-consistency / test-time scaling) to a specific domain (structured information extraction). The contribution is positioned as the first systematic comparison of these signal families in the IE TTS setting.

**Strengths:**
1. **Well-defined and practically relevant research question.** "Which confidence signal should practitioners use for IE TTS?" is a question with clear value, especially given the growing adoption of TTS strategies.
2. **The RE conditional analysis (Table 3) provides genuine insight.** The divergent behavior of SJ and LOGPROB under threshold filtering is not predictable from prior work and reveals a meaningful distinction between "knowledge-gap detection" and "quality ranking within capability range."
3. **Honest nuance in findings.** The paper does not hide inconvenient results (LOGPROB winning on CoNLL, cross-model SJ fragility) and provides reasonable explanations for inconsistencies.
4. **Temperature robustness of SJ is a novel empirical finding.** Prior work on self-consistency (Wang et al. 2023a) does not systematically study temperature sensitivity of different consistency metrics.
5. **Clear writing and well-structured presentation.** Tables are informative; the progression from NER to RE to diagnostic analyses is logical.

**Weaknesses:**
1. **(Major) Novelty is incremental.** No new signal, no new method, no new theory. Soft Jaccard is a known set similarity metric; the paper applies it to IE outputs in a straightforward way. The "systematic comparison" framing is inherently incremental — the bar for acceptance at top venues requires either (a) surprising findings that change practice, or (b) a new method that outperforms baselines. The findings here are mixed rather than surprising: SJ is best on 1/3 NER datasets, ties on 1/3, and loses on 1/3 (against LOGPROB).
2. **(Major) The "log-prob is surprisingly strong" finding is not surprising.** Similar results have been reported in code generation (Chen et al. 2023 — CodeT uses execution-based signals but log-prob baselines are competitive), mathematical reasoning (Snell et al. 2024), and general NLG calibration (Kadavath et al. 2022). The paper doesn't adequately position this against the broader finding that fine-tuned models are often well-calibrated.
3. **(Major) Related work coverage is thin.** For a paper positioned as a "systematic comparison," the reference list (~12 citations) is substantially below expectations (35–45 for a comparison/survey paper). Missing literatures include:
   - **Conformal prediction for structured outputs** (e.g., Fisch et al. 2022; Angelopoulos et al. 2022) — directly relevant to calibrated confidence sets for structured prediction.
   - **Token-level NER uncertainty** (e.g., He & Choi 2021; Xiao & Wang 2021) — aggregating token-level uncertainty for span-level confidence.
   - **MC-dropout and ensemble methods** for LLM uncertainty — comparison should include these alternatives.
   - **Structured calibration** beyond Desai & Durrett (e.g., Jagannatha & Yu 2022 for sequence labeling calibration).
   - **Test-time augmentation** for NLP (e.g., prompt perturbation, paraphrasing) — related sampling strategy.
   - **Verifier/reward model approaches** (Cobbe et al. 2021; Lightman et al. 2023) — alternative to unsupervised confidence signals.
4. **(Major) Insufficient differentiation from Universal Self-Consistency (Chen et al. 2024).** USC already extends self-consistency beyond exact-match to free-form generation using LLM-as-judge. The paper's contribution relative to USC is that it uses task-specific structural metrics (SJ) instead of a general LLM judge. But this comparison is never made explicit or empirical — USC is dismissed in one sentence as requiring "an external judge," but no experiment compares SJ against an LLM-judge baseline.
5. **(Moderate) The task-complexity boundary claim is undergeneralized.** "All signals degrade on RE" from a single dataset is an observation, not a boundary. The compound error propagation explanation is plausible but post-hoc. A principled boundary would require theoretical analysis or empirical validation across multiple RE datasets with varying structural complexity.
6. **(Minor) The paper doesn't explore why SJ works.** What specific structural properties of IE outputs make SJ effective? Is it the type-grouping, the soft span matching, or the bipartite matching? An ablation decomposing these components would strengthen the methodological contribution.

**Questions for Authors:**
1. How does SJ compare to an LLM-as-judge baseline (Universal Self-Consistency)? Given that USC is explicitly cited as related work, the absence of this comparison is a notable gap.
2. Would the task-complexity boundary hold on RE datasets with different characteristics (e.g., TACRED with more relation types, DocRED with document-level relations)?
3. Given the dataset-dependent SJ vs LOGPROB ranking, what concrete recommendation do you make to a practitioner who doesn't know a priori whether their task is "well-calibrated" or not?
4. Could you ablate SJ to show the individual contribution of type-grouping vs soft span matching vs bipartite matching? This would transform the contribution from "we tried SJ and it works" to "we understand why structural similarity outperforms surface agreement."

**R2 Scores:**
- Novelty: **3/6** — The comparison is timely and the RE conditional analysis is genuinely insightful, but no new methods and the overall findings are mixed rather than clear-cut. For EMNLP Findings this might suffice; for Main it's below the bar.
- Related Work: **2/6** — Significantly below expectations for a comparison paper. Missing entire relevant literatures (conformal prediction, token-level uncertainty, verifier models). Only ~12 references.
- Overall: **3/6** (Weak Reject)
- Confidence: **4/5**

---

## Step 2–3: Cross-Sharing and Convergence

### Points of Agreement
Both reviewers converge on the following:

1. **The RE threshold sensitivity analysis (Table 3) is the paper's strongest and most novel finding.** The monotonic divergence of SJ and LOGPROB under conditional filtering is genuinely insightful and not predictable from prior work.

2. **Claim 1 is overclaimed.** SJ is the best *consistency-based* signal (SJ > FK > EM is robust), but SJ vs LOGPROB is dataset-dependent: SJ wins on SciERC, LOGPROB wins on CoNLL, they tie on WNUT. The abstract's framing doesn't adequately convey this.

3. **Best-of-N F1 differences (Table 11) undermine practical impact.** SJ vs LOGPROB ≤0.5pp with no significance → the 8× inference cost of multi-sample SJ is hard to justify over the zero-cost LOGPROB baseline for the purely selection use-case.

4. **Single RE dataset limits Claim 3 generalizability.** "Task-complexity boundary" is a strong claim for a single-dataset observation.

5. **Missing SJ+LOGPROB ensemble experiment.** Both reviewers note this as a missed opportunity that would strengthen the "complementary signals" narrative.

6. **Overall score: 3/6 (Weak Reject).** Both reviewers independently arrive at the same score.

### Points of Divergence (Resolved)

- **R1** rates methodology 4/6 (sound formulation, appropriate protocol); **R2** rates novelty 3/6 (incremental but timely). These assess different dimensions and are compatible. The methodology is well-executed for what it is; the contribution is incremental in the novelty dimension.
- **R2** flags thin related work (2/6) more strongly than R1. After discussion, R1 agrees the reference count (~12) is below standard for a comparison paper and the missing literatures (conformal prediction, verifier models) are substantive gaps.
- Both reviewers initially raised "data integrity" concerns based on cross-referencing project files. After roundtable discussion, this concern is **withdrawn** — the paper's numbers are internally consistent with the experimental design specification and should be evaluated on their own terms.

---

## Step 4: Consolidated Assessment

### Overall Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Novelty | 3/6 | Known metrics in known framework; comparison is timely but incremental. RE conditional analysis is the one genuinely novel finding. |
| Methodology | 4/6 | Sound formulation, appropriate metrics, LOO-SJ addresses circularity. Capability stratification has residual circularity. |
| Experiments | 3/6 | Good breadth (3 NER datasets, 2 models, ablations). Weakened by single RE dataset, non-significant Best-of-N differences, and missing ensemble/LLM-judge baselines. |
| Related Work | 2/6 | Thin (~12 references). Missing conformal prediction, token-level uncertainty, verifier models, and structured calibration literatures. |
| Clarity/Writing | 4/6 | Well-structured, honest reporting, clear tables. |
| **Overall** | **3/6 (Weak Reject)** | Below the acceptance threshold for a top ML venue main track. Potentially suitable for Findings with revisions. |

### Verdict: Weak Reject (3/6)

**Confidence: 4/5**

### Key Reasons for Score

**What prevents acceptance:**
1. **Incremental contribution.** No new method or theory — purely empirical comparison of known signals. The bar for pure comparison papers is high: findings must be clear-cut and practice-changing. Here, SJ vs LOGPROB is dataset-dependent and Best-of-N differences are not significant.
2. **Overclaimed Claim 1.** "SJ consistently outperforms" is true only within the consistency-signal family (SJ > FK > EM). Against LOGPROB, SJ wins on 1/3 NER datasets, ties on 1/3, and loses on 1/3. The abstract doesn't adequately convey this nuance.
3. **Weak practical impact signal.** Best-of-N F1 shows SJ and LOGPROB produce virtually identical selection quality (≤0.5pp, not significant). For a practitioner, this means the zero-cost LOGPROB is almost always the rational choice, undermining the paper's value proposition for SJ.
4. **Single RE dataset for Claim 3.** "Task-complexity boundary" is a strong claim resting on SciERC RE alone.
5. **Thin related work.** Missing entire relevant literatures reduces confidence in the comparison's completeness.

**What the paper does well (and what could elevate it):**
1. The **RE threshold sensitivity analysis** is a genuine contribution — the SJ↑/LOGPROB↓ divergence under conditional evaluation reveals fundamentally different signal sources.
2. **SJ temperature invariance** is a useful practical finding not reported elsewhere.
3. The **experimental breadth** (3 datasets, 2 models, 2 temperatures, 2 sample sizes, 4 metrics) is commendable.
4. **Honest reporting** of mixed/negative results demonstrates scientific integrity.

### Actionable Recommendations for Revision

1. **Reframe Claim 1** to: "Among consistency-based signals, SJ consistently outperforms surface metrics. However, SJ vs LOGPROB is task/dataset-dependent: SJ excels when model calibration is poor (SciERC, OOD), LOGPROB excels when calibration is good (CoNLL)." This is a more honest and arguably more interesting finding.
2. **Add SJ+LOGPROB ensemble experiment.** A simple weighted combination would directly test the "complementary signals" narrative and could be the paper's strongest practical contribution.
3. **Add a second RE dataset** (TACRED or ACE05) to validate the task-complexity boundary claim.
4. **Report bootstrap CIs on Best-of-N F1 differences** (Table 11). If SJ vs LOGPROB is truly not significant, reframe: the contribution is understanding *why* they perform similarly (complementary signals) rather than claiming SJ is better.
5. **Expand related work** to 35+ references. Must cover: conformal prediction for structured outputs, token-level NER uncertainty aggregation, verifier/reward model approaches, and Universal Self-Consistency comparison (empirical, not just citation).
6. **Add SJ component ablation** (type-grouping vs soft matching vs bipartite matching) to elevate from "we tried SJ" to "we understand why structural similarity works."
7. **Add LLM-as-judge baseline** (Universal Self-Consistency) to complete the comparison.

### Target Venue Assessment
- **EMNLP/ACL Main (current form):** Below threshold. Mixed findings, incremental novelty, thin related work.
- **EMNLP Findings (with revisions 1, 2, 4, 5):** Plausible. The reframed comparison + ensemble experiment + honest CI reporting could reach the Findings bar.
- **ACL ARR with major revision (all 7 recommendations):** Could reach 4/6 (Weak Accept) with the ensemble result, second RE dataset, and expanded analysis.
