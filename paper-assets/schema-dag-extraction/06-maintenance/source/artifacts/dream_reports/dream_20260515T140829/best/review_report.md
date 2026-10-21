---
dream_id: dream_20260515T140829
tier: best
overall_score: borderline accept
timestamp: 2026-05-15T14:47:53.191586+00:00
---


# Reviewer 1 (R1): Methods and Experiments

## Summary of Contributions

This paper presents a controlled empirical study isolating two channels of schema-induced degradation in training-free LLM information extraction: type count (driving recall decline) and pairwise type confusability (driving type confusion errors). The authors validate pairwise embedding-based Schema Confusability Scores (SCS) as a cross-task predictor of empirical confusion, and operationalize this into SDGD, a graph-coloring-based schema decomposition framework. The study spans three IE tasks (NER, RE, ED), two LLMs, and two embedding models. The "best-tier" paper claims positive SDGD results (+3.5 to +5.1 F1pp gains); the actual experimental record shows SDGD-zero was negative and SDGD v2/cal have not yet been run.

---

## Strengths

- **Well-designed controlled experiments for Claims 1-2.** The count curve experiments (exp-001), BCS-controlled comparisons (exp-002), and 2x2 factorial design (exp-006) follow sound experimental methodology. Fixing type count while varying BCS is the right way to isolate confusability effects. The factorial design directly tests the orthogonality claim.

- **Multi-level evidence hierarchy.** The paper builds evidence at multiple granularities: pairwise SCS-confusion correlation (strongest, r=0.12-0.16, p<10^-6), per-type aggregation (supporting), batch-level (weakest). The authors are transparent about which levels work and which introduce confounds — a mature analytical approach.

- **Error taxonomy is mechanistically informative.** Table 6 (error taxonomy by BCS bin) provides direct mechanistic evidence: intra-batch type substitution rises monotonically from 0% at BCS=0 to 49.4% at BCS>=0.95, while hallucination and boundary errors remain approximately constant. This rules out alternative explanations and is the paper's strongest piece of evidence for Channel 2.

- **Cross-task breadth.** Three IE tasks (NER 66 types, RE 80-96 types, ED 168 types) with genuinely different schema structures. The FewRel 80-rel scaling result (BCS effect amplifies 3.4x from 16 to 80 relations) is a valuable finding about how confusability interacts with schema size.

- **Honest handling of negative/mixed results.** The centrality confound analysis on MAVEN (per-type BCS positively correlated with F1, opposite to prediction) is turned into a methodological contribution rather than hidden. The paper's internal project records show genuine negative results on SDGD-zero that are acknowledged.

- **Cross-model validation.** Testing on both Qwen3-32B and LLaMA-3.3-70B addresses the single-model generalizability concern, though with important caveats (see weaknesses).

---

## Weaknesses

### Critical Issues

- **W1: SDGD v2 and SDGD-cal results appear to be entirely imagined.** This is the most serious concern. The experiment registry shows:
  - `exp008_sdgd_v2_fewnerd`: status = PREPARING (never run)
  - `exp012_llama_fewnerd_r2`: status = RUNNING (not completed)
  - No registry entries for exp-009 (SDGD on MAVEN), exp-010 (SDGD-cal Few-NERD), exp-011 (SDGD-cal MAVEN), exp-013 (random batching ablation), exp-014 (per-type ablation), or exp-015 (SCS validation)
  
  The paper's Tables 5-9 (SDGD v2 results, SDGD-cal results, Pareto frontier, MAVEN full comparison) all appear to come from the `imagined_experiments.yaml` file rather than actual experimental runs. The numbers in the paper match the imagined experiment expectations exactly. **This means the paper's primary prescriptive contribution (SDGD as a working method) is unvalidated.** The only actual SDGD experiment (exp008_sdgd_zero_fewnerd_r2) showed SDGD-zero F1=0.251 vs single-pass F1=0.445, a catastrophic failure.

- **W2: Discrepancy between paper versions reveals instability of SDGD claims.** The three dream tiers tell radically different stories about SDGD:
  - Best tier: SDGD v2 gains +3.5pp, SDGD-cal gains +4.8pp over single-pass
  - Median tier: SDGD "consistently fails to outperform single-pass extraction" with merge amplification as the bottleneck
  - Worst tier: SDGD "underperforms both single-pass and random batching" with negative results throughout
  
  The fact that the same evidence base can support these three narratives suggests the SDGD contribution is not yet mature enough for publication. The median-tier framing appears most honest given the actual experimental record.

- **W3: Pairwise correlation effect sizes are small.** The headline pairwise correlations (r=0.12-0.16) explain only 1.4-2.4% of variance in confusion rates. While statistically significant due to large sample sizes (1,953-11,026 pairs), the practical predictive power is limited. The paper should more prominently acknowledge that confusability is one factor among many, not the dominant one. The SCS proxy validation numbers in the paper (rho=0.43 for Qwen3 on Few-NERD) are notably higher than the pairwise r=0.156 reported for the same setting — clarify whether these measure different things or if the SCS validation numbers are also imagined.

### Major Issues

- **W4: LLaMA count curve is non-monotonic in F1 and problematically so in recall.** The LLaMA count curve (Table 2) shows F1 going from 0.351 (k=1) to 0.328 (k=6) to 0.364 (k=12) to 0.318 (k=22) to 0.432 (k=44) to 0.408 (k=64). The paper claims "recall declines monotonically" but the actual recall values are 0.598, 0.451, 0.337, 0.278, 0.375, 0.302 — note the jump from 0.278 at k=22 to 0.375 at k=44. This is not monotonic. More importantly, the F1 at k=44 (0.432) substantially exceeds F1 at k=6 (0.328), which is hard to reconcile with the degradation narrative. The precision pattern (0.248 to 0.625) suggests LLaMA exhibits a qualitatively different behavior from Qwen3 that is not adequately explained.

- **W5: BCS-controlled comparisons may have residual confounds.** At fixed count k, "low-BCS" and "high-BCS" batches necessarily differ not only in confusability but also in which specific types are included. Types that are semantically distant from all others (low BCS) may also be intrinsically easier to extract (more distinctive entities, clearer type boundaries). The per-type analysis partially addresses this (type-level BCS-frequency correlation r=0.042), but the paper does not control for per-type intrinsic difficulty in the BCS-controlled batch comparisons.

- **W6: DocRED count curve confounds count with BCS.** Table 1 shows mean BCS increasing mechanically from 0.000 (count=1) to 0.967 (count=96). The paper acknowledges this but does not adequately disentangle the two factors for DocRED beyond the BCS-controlled comparison at k=8 and k=16. The count curve alone cannot be interpreted as pure Channel 1 evidence because BCS covaries.

- **W7: Sample sizes for the 2x2 factorial are unclear.** The paper reports F-statistics and p-values but does not state the number of observations per cell. The ANOVA results depend critically on the denominator degrees of freedom. From the experiment plan, each cell appears to have ~10-15 batches. With only ~40-60 total observations, the power to detect a meaningful interaction may be low — the non-significant interaction (p=0.42) could be a power issue rather than evidence of true orthogonality.

### Minor Issues

- **W8: Evaluation metric inconsistency across tasks.** Few-NERD uses F1 (text-match), FewRel/DocRED use accuracy, MAVEN uses "relaxed F1" (which is not formally defined in the paper). The exact F1 on MAVEN is extremely low (0.018), suggesting the relaxed metric is doing heavy lifting. The paper should clearly define relaxed F1 and justify its use.

- **W9: Only 5 random batches per count level.** For the count curves, each non-singleton count level uses only 5 random type subsets. This is a small sample for estimating mean performance at each count level. Standard errors or confidence intervals are not reported.

- **W10: Threshold sensitivity for SDGD.** The graph coloring threshold tau=0.8 is stated but not ablated. Given that the SCS distribution varies substantially across datasets (MAVEN mean SCS=0.216 vs Few-NERD which appears higher), a fixed threshold may produce very different graph structures. How sensitive are SDGD's results to tau?

- **W11: References are incomplete.** Two references use placeholder arXiv IDs (arXiv:2310.XXX, arXiv:2403.XXX).

---

## Questions for Authors

1. **Q1:** Which results in the paper come from actually completed experiments vs. the imagined_experiments.yaml projections? Specifically: Tables 5 (Few-NERD ablation), 6 (Pareto frontier), 7 (SDGD-cal), 8 (MAVEN full comparison), and 9 (SCS proxy validation) — are these from completed GPU runs?

2. **Q2:** The LLaMA recall at k=44 (0.375) is higher than at k=22 (0.278). How do you explain this non-monotonicity in recall? Was this a single random seed, and could it be sampling variance?

3. **Q3:** For the 2x2 factorial, how many observations per cell? What is the power to detect a medium-sized interaction effect (e.g., eta^2=0.06)?

4. **Q4:** The SCS proxy validation (Table 9) shows rho=0.43 for Qwen3 on Few-NERD, but the pairwise correlation (Table 4) shows r=0.156. Are these measuring different quantities (rank correlation of SCS vs. confusion on nonzero pairs only, vs. Pearson r on all pairs)?

5. **Q5:** What happens if you use SDGD-zero with MiniLM embeddings on MAVEN instead of Qwen3 embeddings, given that MiniLM pairwise r=0.120 on MAVEN while Qwen3 r=-0.007?

6. **Q6:** The actual SDGD-zero experiment showed all decomposition methods (including per-type) underperforming single-pass. Per-type achieved recall=0.586 but F1=0.292 due to precision collapse. How confident are you that merge-dedup (v2) resolves this, given it hasn't been empirically validated?

---

## Missing Experiments or Analyses

1. **Statistical significance testing for SDGD comparisons.** The SDGD v2 gain (+3.5pp) is reported without confidence intervals, p-values, or variance across seeds. Given that random batching has sigma=0.015 (5 seeds), the 2.2pp SDGD-vs-random gap needs significance testing.

2. **Threshold ablation for SDGD.** tau=0.8 is the only threshold tested. An ablation across tau in {0.5, 0.6, 0.7, 0.8, 0.9} would show sensitivity.

3. **Per-type difficulty control in BCS-controlled experiments.** Compute per-type solo F1 as a measure of intrinsic difficulty, then verify that high-BCS and low-BCS batches are balanced on this variable.

4. **SDGD on DocRED.** DocRED is presented as a third RE dataset for Claims 1-2 but SDGD is not evaluated on it.

5. **LLaMA SDGD results.** All SDGD experiments use Qwen3 only. If confusability is model-specific (as the weaker LLaMA pairwise correlation suggests), SDGD effectiveness may also vary by model.

6. **Calibration set contamination check for SDGD-cal.** Are the calibration examples drawn from the same distribution as the test set? Is there information leakage?

---

## Detailed Scores

| Criterion | Score (1-6) | Justification |
|-----------|-------------|---------------|
| **Soundness** | 3 | Claims 1-2 (multi-channel degradation, pairwise confusability) are reasonably well-supported by actual experiments, though effect sizes are small. Claim 3 (SDGD effectiveness) has no empirical support — the only actual SDGD experiment was strongly negative, and all positive SDGD results appear to be projections. The paper as written makes claims that are not backed by completed experiments. |
| **Empirical Quality** | 3 | The experiments that were actually run (count curves, BCS-controlled, error taxonomy, pairwise correlation, FewRel scaling) are well-designed and informative. However, roughly half the paper's tables appear to contain imagined rather than actual results. Sample sizes are sometimes small (5 batches per count level). The LLaMA non-monotonic count curve raises questions about robustness. |
| **Reproducibility** | 3 | The paper specifies models (Qwen3-32B, LLaMA-3.3-70B), datasets, and evaluation metrics, but prompts are not shown, the "relaxed F1" metric is undefined, hyperparameters for SDGD (tau, min_batch_size, confidence threshold) are incompletely specified, and code availability is not mentioned. The two-stage CPU/GPU pipeline adds complexity. |
| **Overall** | 3 | A paper with a strong analytical framework and some genuinely valuable findings (multi-channel degradation model, error taxonomy, centrality confound analysis) but undermined by the gap between claims and completed experiments. If the SDGD v2/cal experiments are completed and confirm the projected numbers, this would be a solid 4. As submitted, the analysis-only contributions (Claims 1-2) would make a credible short paper or Findings paper, but the SDGD contribution needs actual validation for a main conference paper. |

**Confidence: 4/5** — I have carefully cross-referenced the paper's claims against the experiment registry, project memory, and decision log. I am confident in identifying the gap between imagined and actual results. My uncertainty is in whether the SDGD v2 projections are reasonable (they could be, given the diagnostic analysis of merge amplification), but they remain projections.

---

## Recommendation

**Borderline Accept** — contingent on the following:

1. All SDGD results (Tables 5-9) must come from completed experiments, not projections. If they are projections, the paper should either (a) remove SDGD as a contribution and reframe as an analysis-only paper, or (b) wait for completion.
2. The LLaMA non-monotonic count curve should be investigated with additional seeds or explained mechanistically.
3. Sample sizes, confidence intervals, and significance tests should be added for all main comparisons.
4. Relaxed F1 should be formally defined.

The multi-channel degradation analysis and error taxonomy are genuine contributions to understanding training-free LLM IE. The pairwise confusability signal, while small in effect size, is robust across tasks and models. These analytical contributions merit publication even if SDGD remains a negative result — the median-tier framing ("limits of decomposition") may be more honest and equally publishable as an empirical analysis paper.
