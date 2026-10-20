---
dream_id: dream_20260513T092135
tier: best
overall_score: borderline accept (Findings)
timestamp: 2026-05-13T10:16:16.743784+00:00
---

## R1 Review: Methods and Experiments

### Paper
"When Does Circuit Consensus Fail? A Systematic Analysis of Cross-Method Agreement in Mechanistic Interpretability"

---

## Summary of Contributions (2-3 sentences)

This paper formalizes binary cross-method consensus (CSS) for circuit discovery and systematically evaluates it across 6 model-task configurations (4 tasks on GPT-2 Small, IOI on Qwen-0.5B with two method variants), finding that consensus succeeds in only 1/6 cases (IOI on GPT-2, Delta CPR = +0.085, p = 0.002). Three mechanistic failure modes are identified: task-induced method correlation collapsing consensus to obvious-edge selection, component-level scoring degeneration at scale making edge-level consensus impossible, and a Jaccard-based diagnostic that predicts failure with 5/6 accuracy. The size-controlled baseline confirms that IOI's sole success reflects genuine selection quality (76% of advantage retained after controlling for edge count), not a size artifact.

---

## Strengths

- **Rigorous size-controlled analysis addresses the most critical confound.** Table 3 is the paper's strongest methodological contribution. By comparing CSS=1.0 (7 edges) against top-7 from each individual method and random-7 baselines under identical conditions, the paper cleanly decomposes the IOI advantage into selection quality (76.3%) vs. size effect (23.7%). The edge identity analysis showing 5/7 overlap with EAP-IG's top-7 adds mechanistic texture: consensus works by filtering false positives, not by discovering hidden structure. This is a model for confound analysis in circuit evaluation papers.

- **Bootstrap methodology is well-chosen and correctly applied.** Paired bootstrap with BCa correction (B=10,000) is the appropriate nonparametric test for bounded, potentially skewed CPR differences. The paper correctly uses paired resampling (same evaluation examples for CSS and single-method), reports both CIs and p-values, and correctly classifies SVA as non-significant despite a positive point estimate (p=0.482). The choice of alpha=0.05 is conventional and appropriate. The decision to report Qwen configurations as "N/A" rather than imputing zero is methodologically honest.

- **ACDC binarization pathology is a concrete, immediately actionable finding.** The observation that ACDC's native isinf threshold produces only 7-14 edges out of 32K, causing CSS=1.0 to degenerate into a pure ACDC subset, is precisely the kind of implementation-level insight that the community needs. The fix (uniform top-N binarization) is simple and the Jaccard shift (+0.16 to +0.25) after normalization quantifies the artifact cleanly. This finding alone has practical value independent of the broader consensus question.

- **Component-level scoring degeneration (Failure Mode 2) is genuinely novel.** The demonstration that IFR and ACDC independently degenerate on Qwen-0.5B — IFR to layer-level due to GQA's KV sharing absorbing single-edge perturbations, ACDC to node-level due to the cost of greedy pruning over 179K edges — provides mechanistic insight that transcends this paper's consensus framework. Table 6 clearly documents the granularity mismatch. The argument that edge-level consensus becomes semantically meaningless when methods operate at different abstraction levels is well-made.

- **Honest calibration throughout.** The Jaccard diagnostic is framed as an "empirically supported heuristic" rather than a proven law. The n=6 limitation is acknowledged explicitly. The paper does not claim that consensus is universally bad — it identifies the narrow conditions (low Jaccard, edge-level granularity) under which it works. This epistemic discipline is uncommon and appreciated.

- **Ablation robustness check for IOI is well-executed.** Table 8 shows that the IOI advantage persists under mean ablation (Delta = 0.065 vs. 0.080 under zero), retaining 81.3%. This rules out the hypothesis that consensus edges benefit disproportionately from the destructive nature of zero ablation, at least for the positive case.

---

## Weaknesses

- **The ablation method comparison is critically incomplete.** The zero-vs-mean comparison is reported only for IOI (the sole success). This is the paper's most significant methodological gap. The project's experimental history (D026, D030, D031) reveals that ablation method choice has dramatic consequences on other tasks: Arithmetic CPR flips from deeply negative under zero ablation to approximately 0.92 under mean ablation; SVA shows CSS=1.0 mean CPR=1.187 vs. ACDC=1.175 (Delta=0.013, marginal). The headline claim "consensus fails in 5/6 configurations" is therefore conditional on zero ablation being the evaluation protocol, but the paper presents it as a general conclusion. Without the full zero-vs-mean comparison across all 4 GPT-2 tasks, the reader cannot assess whether the failures reflect a genuine property of consensus or an interaction between consensus and the specific evaluation regime. The data for this comparison appears to exist (mean ablation results are referenced in multiple decision logs) — its omission from the paper is difficult to justify.

- **K=3 is effectively K approximately 2, and this is underanalyzed.** EAP-IG and EP are both gradient-based methods. Their pairwise Jaccard is 0.695 on Arithmetic, 0.62 on Factual Recall, and 0.307 on IOI (the sole success — notably also the task where their agreement is lowest). When 2 of 3 methods are highly correlated, binary consensus with threshold 1.0 (all-agree) effectively requires the third method (ACDC) to endorse edges already agreed upon by the gradient pair. The paper acknowledges this in the Discussion but does not systematically quantify how much of the "failure" is attributable to the gradient-pair dominance vs. the inherent limitations of binary consensus. A decomposition showing CSS performance with hypothetically independent methods (e.g., by analyzing the ACDC-only edges that were excluded by the gradient pair's disagreement) would strengthen the analysis. The paper's core claim — that consensus fails — is confounded with the claim that these particular three methods lack sufficient diversity.

- **Size-controlled baselines are applied asymmetrically.** The size-controlled analysis (Table 3) is only performed for IOI, the positive case. For the failing configurations, CSS=1.0 selects different numbers of edges (10 for Factual Recall, variable for others) while single methods use 50 or 100. Without symmetric size controls on at least one failing task — e.g., comparing CSS top-10 vs. EAP-IG top-10 on Factual Recall — the paper cannot distinguish "consensus selects worse edges" from "consensus selects too few edges to capture distributed computations." This asymmetry weakens the failure mode analysis: Failure Mode 1 (task-induced correlation) could alternatively be explained as a size mismatch artifact on bottleneck tasks.

- **The Jaccard diagnostic receives disproportionate prominence for its evidential weight.** The paper devotes a full subsection (5.8) and a full-width table (Table 7) to a diagnostic tested on n=6 points with Spearman rho=-0.714 (p=0.111) on the full dataset. Significance (rho=-0.90, p=0.037) is only achieved after excluding the Qwen-ACDC "outlier," which is post-hoc exclusion. The GPT-2 subset (n=4, rho=-1.0, p=0.042) is trivially perfect — any monotone relationship among 4 ranked items is "perfect." The 0.35/0.50 thresholds are fitted to these 6 points with zero observations in the gap zone. While the paper correctly acknowledges these limitations, the section's prominence (named thresholds, a diagnostic protocol, a practitioner guideline) conveys more confidence than the evidence warrants. This section should be substantially condensed or moved to an appendix with explicit framing as preliminary/exploratory.

- **Single random seed and 100 evaluation examples limit robustness claims.** The bootstrap CIs quantify uncertainty given the 100 evaluation prompts, but not sensitivity to prompt selection or random seed. The project's decision history (D033) documents that the same SVA experiment on two different servers produced Delta=0.013 vs. Delta=0.006 — hardware-level variance alone shifts the conclusion. For a paper arguing about the reliability of consensus, the evaluation itself should demonstrate reliability through multi-seed or leave-one-out prompt sensitivity analysis. The IOI CI [0.035, 0.138] is reassuringly above zero, but the SVA and Arithmetic borderline cases deserve seed-level robustness checks.

- **No comparison with continuous score averaging.** Mondorf et al. (2025) is cited in Section 2 but never tested or substantively discussed. Binary consensus is arguably the crudest possible aggregation strategy. The paper's conclusion — that "consensus fails" — is much stronger than the evidence supports if the failure is specific to binarization (which FM1 explicitly identifies as a problem) rather than to multi-method aggregation in general. Even a qualitative argument about why continuous averaging would or would not exhibit the same failure modes would help scope the contribution. Without this, the reader cannot tell whether the paper is about "consensus failing" or "binarization failing."

---

## Questions for Authors

1. **Can you provide the zero-vs-mean ablation comparison for all 4 GPT-2 tasks?** The project decision logs indicate this data exists (D026: Arithmetic mean ablation CPR approximately 0.92; D030-D032: SVA mean ablation data). If CSS=1.0 under mean ablation achieves CPR approximately 0.92 on Arithmetic while EAP-IG achieves approximately 0.96, the "failure" becomes a marginal underperformance rather than a clear negative. How many of the 5 FAIL verdicts survive under mean ablation?

2. **For Factual Recall, what happens in the size-controlled comparison?** CSS=1.0 selects 10 edges vs. single methods' 50. If you compare CSS top-10 vs. EAP-IG top-10, does the Delta=-0.070 persist, shrink, or reverse? This would disambiguate FM1 (method correlation) from a size confound.

3. **How sensitive are results to the top-N binarization threshold?** The paper uses n in {50, 100} but does not systematically report how varying N changes outcomes. The ACDC top-k sweep (k=50/75/100/150, referenced in project artifacts) apparently exists. Does the IOI positive result hold at n=50? Does any failing task become positive at larger N?

4. **Have you considered a K=2 analysis (EAP-IG intersected with ACDC only, excluding EP)?** Given that EP is gradient-adjacent to EAP-IG, a K=2 consensus of genuinely diverse methods might perform differently. This would help disentangle the method-diversity confound from the consensus-mechanism question.

5. **For the Qwen experiments, why are two separate configurations (IFR and ACDC) reported rather than running all four methods?** If ACDC is too expensive on 179K edges for full edge-level operation (which the degeneration analysis suggests), this should be stated as a limitation rather than presenting the degenerated ACDC as a valid third method for consensus.

---

## Minor Issues

- Table 1: The SVA and Arithmetic rows show "---" for CSS=1.0 Edges and CSS CPR but do report Delta values. This is inconsistent — if CSS=1.0 edge counts exist, they should be reported; if they don't, the Delta should be marked N/A or the comparison basis should be clarified (is the Delta for CSS>=2/3 instead?).

- The EP citation (Kramar et al. 2024) in the bibliography actually points to AtP*, not Edge Pruning. EP as used in this paper (gradient-weighted edge pruning from the princeton-nlp codebase) should be cited to its correct source. This misattribution affects the "three algorithmic families" claim since AtP* and EAP-IG are more similar than EP and EAP-IG.

- Section 3.1 defines CSS(e) = (1/K) sum m_k(e), which is a normalized score in [0,1]. But the paper then refers to CSS=1.0 as "all three methods agree" and CSS>=2/3 as "at least two agree." This notation is correct but potentially confusing — "CSS threshold tau=1.0" and "CSS threshold tau=2/3" would be clearer.

- The paper claims "first systematic negative evaluation of cross-method consensus" in the contributions. Mondorf et al. (2025) already compare methods and report disagreements; CIRCUS (Parekh 2026) explores within-method consensus. The priority claim should be more carefully scoped to "first systematic evaluation of binary cross-method intersection."

- Table 7 (Jaccard diagnostic): the "Prediction" column uses thresholds (< 0.35, > 0.50) that are defined post-hoc from the same data. This should be explicitly marked as in-sample evaluation, not predictive accuracy.

- No figures in the paper. The Jaccard-CSS scatter plot described in the experiment plan would significantly improve readability and is a missed opportunity. A forest plot of the bootstrap CIs (Table 5) would also be more effective than tabular presentation.

- The bibliography has 14 references, well below EMNLP norms (30-40). Notable omissions: lottery ticket hypothesis (Frankle & Carlin 2019) for subnetwork selection parallels, Miller et al. (COLM 2024) on faithfulness sensitivity to ablation method (directly relevant to the zero-vs-mean gap), Meloux et al. on EAP/EAP-IG variance, causal scrubbing (Chan et al. 2022), and the broader ensemble aggregation literature beyond Kuncheva.

---

## Scores

- **Soundness: 3/5** — The core methodology (CSS formalization, bootstrap CIs, size-controlled baseline for IOI) is sound. However, three significant gaps — incomplete ablation comparison, asymmetric size controls, and the K approximately 2 confound — prevent full confidence in the headline "5/6 FAIL" claim. The paper's claims are supported under zero ablation with this particular method set, but the generality claimed in the abstract and conclusion exceeds what the experiments demonstrate.

- **Excitement: 3/5** — The question is timely and practically important. FM2 (scoring granularity degeneration at scale) is a genuinely novel finding with implications beyond this paper. FM1 (ACDC binarization pathology) is actionable. The honest negative-result framing is valuable. However, the contribution is somewhat narrow: binary intersection is the simplest possible aggregation strategy, and without testing continuous alternatives, the paper cannot determine whether the failure is fundamental to multi-method consensus or specific to the binary approach.

- **Overall Assessment: 3.0/5** — At the Findings threshold. The paper asks the right question, provides an honest answer, and identifies two concrete findings (ACDC binarization pathology, scaling degeneration) that the community can act on. The size-controlled IOI analysis is exemplary. However, the incomplete ablation comparison is a serious gap that could change the headline result, the Jaccard diagnostic is overweighted for its evidential strength, and the absence of continuous-averaging comparison limits the scope of conclusions. With the zero-vs-mean comparison across all tasks and one size-controlled failing-task baseline, this would be a clear Findings accept.

- **Confidence: 4/5** — I am familiar with the circuit discovery methods evaluated (EAP-IG, ACDC, Edge Pruning), the evaluation metrics (CPR, ablation protocols), and the statistical methodology (paired bootstrap, BCa correction). The K approximately 2 concern and the ablation-sensitivity issue are well-documented in the literature. My main uncertainty is whether the missing ablation data would substantially change the conclusions — the project history suggests it would soften them but not reverse them entirely.

---

### Justification

The paper makes a genuine contribution by systematically testing an intuitive but untested hypothesis (cross-method consensus improves circuit quality) and providing an honest negative answer with mechanistic explanation. The ACDC binarization pathology and the scaling degeneration finding are concrete, actionable insights. The statistical methodology is sound where applied. However, the experimental design has critical asymmetries: the ablation robustness check is only performed for the positive case, the size-controlled analysis is only performed for the positive case, and the method set's K approximately 2 effective diversity is acknowledged but not systematically analyzed. The Jaccard diagnostic, while interesting as an observation, is promoted beyond its evidential weight. These issues place the paper at the Findings threshold rather than above it. The distance to a confident accept is not large — the zero-vs-mean ablation comparison across all tasks is the single highest-impact revision, followed by symmetric size controls and condensing the Jaccard section.