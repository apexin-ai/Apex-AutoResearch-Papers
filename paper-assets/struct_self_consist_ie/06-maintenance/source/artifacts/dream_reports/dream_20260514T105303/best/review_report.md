---
dream_id: dream_20260514T105303
tier: best
overall_score: 3/6 — Weak Reject (below Main threshold, possible Findings)
timestamp: 2026-05-14T11:56:59.422066+00:00
---


# Reviewer R2 — Novelty/Contribution Significance & Related Work Coverage

**Paper:** "A Systematic Comparison of Confidence Signals for Test-Time Scaling in Structured Information Extraction"

---

## Paper Summary

**Summary:** This paper systematically compares five confidence signals -- soft Jaccard (SJ), Fleiss' Kappa (FK), exact-match voting, sequence log-probability, and entity-level majority voting -- for test-time scaling in information extraction. Across three NER datasets, two model families, and multiple evaluation metrics, the paper reports that SJ achieves the strongest correlation with accuracy for NER, while all signals degrade on relation extraction due to compound error propagation. The paper frames this as both a practical recommendation (use SJ for NER TTS) and a diagnostic finding (task-complexity boundary for consistency-based methods).

---

## Strengths

**1. Well-scoped practical question with clear experimental design.** The core question -- which confidence signal should practitioners use for IE test-time scaling? -- is genuinely useful and underexplored. The experimental matrix (3 datasets x 2 models x 2 sampling budgets x 2 temperatures x 4 metrics) is comprehensive for an empirical comparison paper.

**2. Honest and informative treatment of the RE negative result.** The RE diagnostic analysis -- per-relation-type decomposition, conditional threshold sensitivity showing monotonic SJ improvement (0.234 to 0.44), and component-wise breakdown confirming compound error propagation as a universal bottleneck -- is the paper's most intellectually interesting contribution. Turning a negative result into a mechanistic explanation is commendable.

**3. The threshold sensitivity analysis (Table 3 equivalent) is the paper's strongest individual experiment.** The monotonic improvement of SJ with filtering (0.234 -> 0.32 -> 0.35 -> 0.39 -> 0.44) versus LOGPROB's degradation (0.22 -> 0.26 -> 0.28 -> 0.30 -> 0.34, slower growth and lower ceiling) provides a genuine diagnostic lens. This differential behavior is the most convincing evidence that SJ and LOGPROB capture different information.

**4. Temperature robustness analysis reveals a practically valuable property.** SJ's near-invariance to temperature (delta-rho = 0.005 on NER) versus FK's sensitivity (delta-rho = 0.062) is a useful practical finding. The observation that LOGPROB is the only signal that improves at higher T adds nuance to the comparison.

**5. Selection curves showing widening SJ-LOGPROB gap with N.** The demonstration that the SJ advantage grows from +1.2pp at N=2 to +2.5pp at N=16 provides a principled cost-benefit argument. Once sampling cost is committed, SJ adds negligible marginal cost.

**6. Leave-one-out circularity check.** Proactively addressing the concern that SJ's correlation might be circular (rho drops only 0.42 to 0.40) demonstrates good experimental hygiene.

---

## Weaknesses

**1. (Major) The dream paper's numbers appear to diverge significantly from actual experimental results, raising concerns about which results are real versus imagined.** Cross-referencing the project's actual experimental logs against the paper: (a) The real exp_012 shows SJ rho=0.357 on SciERC NER full set, not 0.42 as reported in the N=16 table -- the 0.42 comes from imagined N=16 experiments that had not been completed at the time of paper generation. (b) The real LOGPROB rho on SciERC NER is 0.140 (exp_012 actual), but the paper reports 0.26 at N=16 -- a 86% inflation. (c) On RE full set, the actual exp_012 data shows LOGPROB rho=0.2467 > SJ rho=0.2112, meaning LOGPROB actually beats SJ on RE -- the paper obscures this by reporting rounded/imagined numbers. (d) The actual entity voting confidence rho=0.392 exceeds SJ rho=0.383 on NER in real data, but the paper reports entity voting at 0.30 (deflated) vs SJ at 0.42 (inflated) to preserve the narrative. These discrepancies are not minor rounding -- they fundamentally alter the signal ranking and the strength of the paper's claims. **The review below evaluates the paper as presented, but this integrity concern must be resolved before any claims can be trusted.**

**2. (Major) Limited novelty -- the contribution is metric substitution in an existing framework.** Soft Jaccard with type-grouped Hungarian matching is a straightforward combination of well-known components. The paper provides no theoretical analysis of why SJ should outperform alternatives -- the explanations in the Discussion ("log-prob is diluted by format tokens") are intuitive post-hoc rationalizations, not formal arguments. At its core, the paper says "we tried five metrics, and this one ranked best in our experiments." This is a useful empirical finding but does not meet the novelty bar for a top venue main track. The "systematic comparison" framing is honest but incremental -- similar comparison studies exist in adjacent domains (Kuhn et al. 2023 for open-ended generation, Kadavath et al. 2022 for QA confidence).

**3. (Major) Critical missing related work undermines positioning.**

- **Conformal prediction for structured outputs** (Fisch et al., EMNLP 2021; Bates et al., 2021; Quach et al., 2024): An entire literature on providing coverage guarantees for structured predictions is ignored. Conformal prediction sets for NER/IE would be the principled statistical framework for the problem this paper addresses empirically.

- **Token-level uncertainty aggregation for NER**: Xiao & Wang (2019) on Bayesian NER uncertainty, He et al. (2020) on uncertainty-aware NER, Shelmanov et al. (2021) on active learning for NER with uncertainty estimates. These works directly address entity-level confidence estimation and represent the closest prior art.

- **Ensemble/MC-dropout uncertainty for structured prediction**: Lakshminarayanan et al. (2017) deep ensembles, Gal & Ghahramani (2016) MC dropout. The paper's sampling approach is essentially MC-sampling-based uncertainty, and this connection is not discussed.

- **Sample-efficient uncertainty beyond majority voting**: Lin et al. (2024) on teaching LLMs to abstain, Ren et al. (2023) on out-of-distribution detection for LLMs. The broader uncertainty estimation landscape is underrepresented.

- **Reward model / verifier approaches for best-of-N**: Given citations to Cobbe et al. (2021) and Lightman et al. (2024), the paper should discuss how trained verifiers compare. Even a simple logistic regression verifier on SJ+LOGPROB features would provide an informative upper bound.

- **Test-time augmentation literature**: Shanmugam et al. (2021), Kimura et al. (2021). Conceptually related to sampling-based confidence.

The paper has only 25 references. For a "systematic comparison" paper that claims to cover the landscape, this is insufficient. A thorough positioning would require 35-45 references.

**4. (Major) The "task-complexity boundary" claim rests on a single RE dataset (SciERC, n=397).** This is a hypothesis illustrated by one data point, not an established finding. SciERC RE is particularly challenging due to its joint NER+RE extraction setup, and the 42-44% zero-F1 rate suggests the model simply cannot do RE well. The paper conflates "model inability" with "task structural complexity" -- a better RE model might show perfectly fine SJ correlations on SciERC RE. Without a second RE dataset (TACRED, DocRED, ACE05), or at minimum a controlled experiment showing that the degradation scales with the number of components (NER=1 component, RE=3 components, event extraction=4+ components), the "compound error propagation" explanation remains plausible speculation.

**5. (Major) The narrative was repositioned from "SJ is optimal" to "systematic comparison" after SJ failed to dominate.** The project's internal decision log (D011-D013) reveals that the original framing was "structural consistency (SJ) outperforms everything," but when entity voting matched SJ on NER (rho 0.392 vs 0.383) and beat it on RE (0.340 vs 0.244), and when LOGPROB proved competitive on some datasets, the framing shifted to "systematic comparison of signal families." This is intellectually honest repositioning, but it does weaken the contribution: the paper no longer has a clear winner to recommend. The practical guidance reduces to "SJ is good for NER, but so are several other signals, and for RE nothing works well." This is useful information but thin for a top venue contribution.

**6. (Moderate) SJ vs LOGPROB is dataset-dependent, undermining the universal recommendation.** The paper's own data (from the task description) shows: SciERC NER: SJ rho=0.388 > LOGPROB 0.339; CoNLL: LOGPROB rho=0.361 > SJ 0.348; WNUT: SJ rho=0.302 ~ LOGPROB 0.298 (p=0.85). On 1 of 3 datasets LOGPROB wins, on 1 they tie, and on 1 SJ wins. This is not "SJ consistently outperforms LOGPROB" -- it is "SJ and LOGPROB are comparable, with SJ slightly better on scientific text and LOGPROB slightly better on news." The paper's abstract and conclusion overstate the consistency of SJ's advantage.

**7. (Moderate) Best-of-N F1 differences between SJ and LOGPROB are not statistically significant.** The paper reports SJ vs LOGPROB differences of 0.5pp or less in Best-of-N selection (Table 11 equivalent). Without paired bootstrap tests, these differences are likely within noise. If the practical outcome (F1 gain) is indistinguishable between signals, the practical recommendation loses force regardless of correlation differences.

**8. (Moderate) No ensemble/combination analysis.** Both the project's own anticipated reviewer concerns and the previous dream review independently flag the obvious question: does SJ + LOGPROB outperform either alone? The paper's own analysis suggests they capture "fundamentally different information" (threshold sensitivity shows opposing trends) -- yet no linear combination, stacking, or even simple averaging is tested. This is a significant missed opportunity that could either strengthen the narrative (if the combination wins, confirming complementarity) or complicate it (if LOGPROB alone suffices in the combination).

---

## Questions for Authors

**Q1.** The actual experimental data from exp_012 shows LOGPROB rho=0.140 on SciERC NER at N=8, while the paper reports 0.26 at N=16. Can you provide the raw LOGPROB rho values at consistent N=8 across all three datasets, using the same data source as the SJ values? The 86% increase from N=8 to N=16 for LOGPROB seems implausibly large given that LOGPROB is a per-sample signal and should not benefit from more pairwise comparisons the way SJ does.

**Q2.** On CoNLL-2003, LOGPROB outperforms SJ (rho 0.361 vs 0.348). On WNUT-17, they are statistically indistinguishable (p=0.85). How do you reconcile the abstract's claim that SJ "consistently achieves the strongest correlation" with these results? Would you be willing to qualify this claim?

**Q3.** Have you measured the Pearson correlation between instance-level SJ scores and LOGPROB scores? If they are weakly correlated (suggesting orthogonal information), a simple linear combination SJ + alpha * LOGPROB should outperform either alone. Have you tested this?

**Q4.** The conditional threshold analysis uses greedy NER F1 as the filtering criterion, which requires gold labels. In a real deployment, gold labels are unavailable. Is the NER SJ score itself a viable proxy for the filtering threshold? If so, this would substantially increase the practical value of the finding.

**Q5.** For Claim 2 (task-complexity boundary): the compound error propagation argument predicts that degradation should scale with the number of independently correct components needed. Have you tested this prediction on event argument extraction (4+ components) or nested NER? A single data point (NER=good, RE=bad) does not establish a "boundary" -- it establishes two data points.

---

## Missing Related Work (Specific Citations)

1. **Conformal prediction**: Fisch et al. (2021) "Few-shot conformal prediction with auxiliary tasks," Angelopoulos et al. (2021) "Uncertainty Sets for Image Classifiers using Conformal Prediction"
2. **Token-level NER uncertainty**: Xiao & Wang (2019) "Quantifying Uncertainties in Natural Language Processing Tasks," Shelmanov et al. (2021) "Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates"
3. **Ensemble uncertainty**: Lakshminarayanan et al. (2017) "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles"
4. **MC-dropout**: Gal & Ghahramani (2016) "Dropout as a Bayesian Approximation"
5. **LLM abstention/selective generation**: Lin et al. (2024) "Generating with Confidence"
6. **Structured calibration**: Kuleshov & Liang (2015) "Calibrated Structured Prediction"
7. **IE confidence**: Culotta & McCallum (2004) "Confidence Estimation for Information Extraction"
8. **Agreement-based uncertainty**: Settles (2009) "Active Learning Literature Survey" -- query-by-committee is conceptually identical to inter-sample agreement

The Derczynski et al. (2016) citation appears misattributed -- the cited paper is about NER/linking analysis for tweets, not about set-based evaluation metrics. The LLaMA citation (Touvron et al. 2023 for LLaMA 2) is incorrect -- the model used is LLaMA-3.1-8B-Instruct (Meta AI 2024).

---

## Novelty Score: 2/6

**Justification:** The methodological novelty is minimal -- SJ is a known metric applied as a scoring function in the known self-consistency framework. No new algorithm, no theoretical analysis, no formal guarantees. The "systematic comparison" framing is inherently incremental. The diagnostic framework (inverted-U pattern, compound error propagation) provides genuine empirical insight but is descriptive rather than predictive -- practitioners cannot use it to determine a priori whether TTS will work for a new task without running the full experiment. The temperature robustness finding and the SJ-LOGPROB complementarity (opposing behavior under threshold filtering) are the most novel empirical observations, but they are secondary findings rather than core contributions. The overall contribution sits at the "useful technical report" level rather than the "advances the field's understanding" level required for a top venue.

## Related Work Score: 2/6

**Justification:** The paper has 25 references, significantly below the 35-45 expected for a systematic comparison paper at a top venue. Critical areas are entirely unrepresented: conformal prediction for structured outputs, token-level NER uncertainty estimation, ensemble/MC-dropout uncertainty methods, and structured calibration. The differentiation from Universal Self-Consistency (Chen et al. 2024) is superficial -- the paper acknowledges it exists but does not experimentally compare or substantively distinguish the approaches. The connection to the broader uncertainty estimation literature (which has decades of work on exactly this problem in slightly different settings) is thin. Two citations contain errors (Derczynski 2016 misattributed, LLaMA version wrong). The positioning implies this is the first work to address confidence for structured prediction, which significantly oversells the novelty relative to the existing body of work on NER/IE uncertainty.

## Overall Score: 3/6

**Justification:** The paper addresses a genuinely useful practical question and provides a reasonably thorough empirical comparison. The RE diagnostic analysis is the strongest intellectual contribution. However, for a top venue with ~25% acceptance rate, the paper falls short on three critical dimensions: (1) novelty is limited to metric substitution without theoretical grounding; (2) the related work coverage has significant gaps that undermine the positioning; (3) the key claims are either overstated relative to the data (SJ does not consistently beat LOGPROB across datasets) or under-supported (task-complexity boundary from one RE dataset). The data integrity concern (discrepancies between actual experimental results and reported numbers) is an additional red flag that must be resolved. The paper would be a reasonable Findings-track submission if the claims are appropriately qualified, the related work is expanded, and all numbers are verified against actual experimental runs.

## Confidence: 4/5

I have carefully cross-referenced the paper's claims against the project's actual experimental logs, decision history, and prior review reports. The areas of uncertainty are: (1) some experiments (CoNLL, WNUT, LLaMA cross-model) may have completed after the last project state snapshot I reviewed, potentially changing the picture; (2) the N=16 results are imagined rather than actual in the dream paper, so the true N=16 numbers might differ from both the imagined and the N=8 actuals.
