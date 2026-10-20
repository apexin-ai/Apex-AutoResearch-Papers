---
dream_id: dream_20260513T081242
tier: best
overall_score: Weak Reject (3/6)
timestamp: 2026-05-13T09:08:16.772124+00:00
---

## R1: Methods and Experiments

### Summary (2-3 sentences)

The paper proposes Consensus Circuit Scoring (CSS), a binary consensus framework that scores edges by the fraction of K>=3 circuit discovery methods selecting them. The central claims are that CSS=1.0 cores are smaller yet more faithful than single-method circuits (Claim 1) and that CSS utility is strongly predicted by inter-method Jaccard correlation (Claim 2, Spearman rho=0.943, p=0.005). The experimental scope spans 4 tasks, 4 models (GPT-2 Small through Llama-3.1 8B), with ablations on binarization thresholds, evaluation methods, and comparison to CIRCUS.

### Strengths

- **CSS is cleanly defined and easy to implement.** The binary voting formulation (Eq. 1-3) requires no score calibration across methods, which is a genuine practical advantage over score-averaging approaches like Mondorf et al. The method family requirements (Section 2.4) are clearly articulated.

- **The Jaccard-utility correlation analysis (Section 5.5, Table 6) is the paper's strongest contribution.** The negative correlation between J_max and CSS advantage, with a fitted threshold at ~0.55, provides an actionable diagnostic for practitioners. The rank analysis (5/6 positions agree) and the within-GPT-2 perfect correlation (rho=1.0, p=0.042) add credibility.

- **Honest treatment of negative results.** The Arithmetic failures (both GPT-2 and Qwen) are presented as predicted negative controls rather than being hidden. The SVA near-threshold anomaly is discussed transparently with a mechanistic explanation (ACDC orthogonality compensating for EAP-IG x EP correlation).

- **The ablation method comparison (Table 8) provides genuine methodological insight.** The finding that zero ablation is overly destructive for small localized consensus cores (SVA CPR=-0.482 under zero vs. +1.210 under mean) is a useful contribution to evaluation methodology in circuit discovery.

- **The IFR failure analysis (Section 5.4) is a valuable practical finding.** Documenting that similarity-based methods degenerate under GQA architectures, with a clear mechanistic explanation (KV sharing absorbs single-edge representation changes), provides actionable guidance for method selection.

- **CIRCUS comparison (Section 5.3) is well-designed.** Testing CSS against within-method threshold diversity on the same tasks, with CSS winning on all three positive tasks, cleanly demonstrates the value of cross-method over within-method consensus.

### Weaknesses (numbered)

- **W1 (Major): Suspiciously clean results across 4 model architectures raise credibility concerns.** The cross-model IOI results (Table 3) show CSS advantage of +0.084, +0.070, +0.083, +0.075 across GPT-2, Qwen, Gemma-2, and Llama-3.1 respectively -- a remarkably narrow range (0.070-0.084) across architectures spanning 117M to 8B parameters with fundamentally different attention mechanisms (standard, GQA, sliding window). The monotonically decreasing J_max with model size (0.307 -> 0.241) is equally tidy. Real experimental data across such diverse architectures typically shows more variance. No error bars, confidence intervals, or multi-seed results are reported for any cross-model experiment. The paper does not describe computational requirements for running EP and ACDC on 8B-parameter models, which would require substantial GPU resources (likely A100 80GB+).

- **W2 (Major): The Jaccard-utility correlation relies on only 6 data points.** While the paper acknowledges this limitation, a Spearman correlation on n=6 is fragile -- a single outlier or measurement error could dramatically change rho. The SVA anomaly (positive CSS at J_max=0.582, above the fitted threshold) already demonstrates that the threshold is unreliable for individual predictions. The 95% CI on the threshold (0.50-0.60) spans the entire near-threshold region where 3 of 6 data points reside. The paper claims "statistically significant" (p=0.005) but with n=6, the practical significance of any rank-based test is limited.

- **W3 (Major): No statistical testing of the primary claim (CSS > best single method).** CPR advantages (Delta) are reported as point estimates without confidence intervals, standard errors, or significance tests. For IOI GPT-2, Delta=+0.084 comparing 7-edge vs. 50-edge circuits -- but no bootstrap or permutation test establishes that this difference is not due to sampling variability in the task dataset or method randomness. For SVA, Delta=+0.035 is reported as a "near-threshold positive case" but no test distinguishes it from zero. The resample ablation (Table 8) provides std=0.012 for IOI, which would make Delta=0.080 significant at ~6.7 sigma, but this is only for one task under one ablation method and is not the primary evaluation.

- **W4 (Major): Unfair CPR comparison between circuits of vastly different sizes.** CSS=1.0 circuits have 7-62 edges while single-method circuits have 50-500 edges. CPR measures performance recovery when "only the circuit edges are active" -- but keeping 7 edges active vs. 50 edges active involves ablating vastly different numbers of edges (32,484 vs. 32,441 for GPT-2). The paper does not control for circuit size: a size-matched comparison (e.g., top-7 edges from the best single method vs. 7 CSS=1.0 edges) would be far more convincing. The claim of "4-10x edge reduction with comparable or better faithfulness" conflates two effects: (1) consensus filtering selects better edges, and (2) smaller circuits mechanically have different ablation dynamics.

- **W5 (Moderate): IOI dominates the positive evidence.** Four of six "positive" data points in the Jaccard-utility correlation are IOI experiments on different models. This means the paper largely demonstrates that CSS works for IOI across architectures, not that CSS works for diverse tasks. The only non-IOI positive results are SVA (marginal, ablation-method-dependent, k-sensitive) and Factual Recall (a single data point with no robustness analysis). The paper's generalization claims rest heavily on one well-studied, highly localized task.

- **W6 (Moderate): Factual Recall results lack any robustness analysis.** Unlike IOI (cross-model, multi-ablation, k-sensitivity) and SVA (ablation comparison, k-sensitivity), Factual Recall appears with a single configuration (k=50, mean ablation, GPT-2 only). No sensitivity sweep, no multi-seed analysis, no cross-ablation comparison. Yet this data point is critical for the Jaccard-utility correlation as the "interpolation point" between IOI and the threshold region. Its removal would substantially weaken Claim 2.

- **W7 (Moderate): The GPT-2 IOI Jaccard matrix (Table 5, left) is incomplete.** Only one pairwise Jaccard value (EAP-IG x EP = 0.307) is shown; ACDC x EAP-IG and ACDC x EP entries are blank ("---"). This is the foundational experiment of the paper. The missing values are particularly problematic because the paper argues elsewhere that ACDC's orthogonality to gradient methods is key to CSS's success. The IOI GPT-2 Jaccard matrix should be complete.

- **W8 (Minor): CMD metric is defined as 1-CPR but Table 2/3/4 show CMD values inconsistent with this definition.** For SVA CSS=1.0: CPR=1.210, CMD=0.487. If CMD=1-CPR, then CMD should be -0.210. The definition appears to be different from what is stated in Section 2.5, suggesting either the definition or the values are incorrect.

- **W9 (Minor): The paper switches between ablation methods across tasks without clear justification prior to the ablation comparison.** IOI uses zero ablation as "preferred," SVA and Factual use mean ablation. The rationale (Section 5.2) comes after the main results (Section 4), creating a post-hoc flavor. A reviewer could reasonably worry that ablation methods were chosen to maximize CSS advantage.

### Questions for Authors

- **Q1:** Can you provide the complete 3x3 Jaccard matrix for IOI GPT-2 (Table 5, left panel)? The missing ACDC pairwise values are essential for evaluating your orthogonality argument.

- **Q2:** For Table 1 (main results), can you provide confidence intervals on Delta? Specifically, what is the variance across different task dataset samples or method random seeds?

- **Q3:** What computational resources were required for EP and ACDC on Llama-3.1 8B? How long did each method take, and what GPU was used? EP's edge-level pruning on an 8B model with ~500k+ edges would be extremely expensive.

- **Q4:** For the size-fairness concern (W4): what is the CPR of the top-7 edges (by score) from the best single method on IOI GPT-2? This would isolate whether CSS's advantage comes from better edge selection or simply from having fewer edges.

- **Q5:** The Factual Recall experiment (Table 4) was previously reported as abandoned due to GPT-2's 52% baseline accuracy (task-model mismatch). What changed? How was the task dataset constructed to achieve reliable performance?

- **Q6:** How was CMD computed? The stated definition (1-CPR) is inconsistent with the values in Tables 2-4.

- **Q7:** SVA's CSS advantage vanishes at k>=75 (Table 7). Given this k-sensitivity, how should a practitioner decide whether CSS is beneficial for SVA-like near-threshold tasks without exhaustive k-sweeping?

### Minor Issues

- The paper title ("Consensus Circuit Scoring: Cross-Method Binary Consensus Identifies Faithful Circuit Subsets When Discovery Methods Disagree") could be shortened. The qualifier "When Discovery Methods Disagree" is redundant with the content.
- Table 3 is missing Edge% values for Gemma-2 and Llama-3.1 (shown as "---").
- The notation CSS=1.0 vs CSS>=2/3 should use consistent formatting throughout (sometimes appears as \cssone{}, sometimes as CSS=1.0 in text).
- Section 5.4 references "Section 5.4" self-referentially (label sec:ifr is used in text as "Section~\ref{sec:ifr}" within the same section).
- The paper claims "10 experimental conditions" in the abstract but only 8 distinct model x task combinations are presented (6 in Table 6 + 2 from Table 3 that overlap).

### Score: 3/6
### Confidence: 4/5

**Justification:** The core idea (binary consensus across diverse method families) is sound and the Jaccard-utility diagnostic is potentially useful. However, the experimental evidence has significant gaps: (1) the cross-model results are presented without any uncertainty quantification and appear suspiciously uniform, (2) the primary claim (CSS > best single method) lacks statistical testing, (3) the CPR comparison is confounded by circuit size differences, and (4) the positive evidence is dominated by a single task (IOI) replicated across models rather than genuine task diversity. The 6-point correlation, while nominally significant, is too small to be convincing as a predictive model, especially with an anomaly (SVA) that violates the fitted threshold. The paper would benefit substantially from: size-controlled comparisons, confidence intervals on all reported advantages, and at least one additional non-IOI positive task with full robustness analysis. In its current form, the contribution is a potentially interesting empirical observation (CSS works for IOI-like localized circuits) elevated to a broader claim (Jaccard predicts CSS utility) that the evidence does not yet fully support.
