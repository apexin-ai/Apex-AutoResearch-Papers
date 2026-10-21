---
dream_id: dream_20260514T093336
tier: worst
overall_score: weak reject (3/6)
timestamp: 2026-05-14T10:28:59.882712+00:00
---

# Dream Review Report — Full Roundtable

**Paper:** "Why Self-Consistency Fails as a Confidence Signal for Structured Prediction"
**Dream ID:** 20260514T093336
**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)
**Overall Score:** Weak Reject (3/6)

---

## Reviewer Assignments

- **R1 (Methods + Experiments):** Methodological soundness, experimental design, statistical rigor, reproducibility
- **R2 (Novelty + Related Work):** Novelty/significance, related work coverage, framing, positioning

---

## Step 1: Independent Reviews

### R1 Summary — Score: 3/6 (Weak Reject)

**Strengths identified:**
1. Comprehensive experimental matrix (3 NER datasets, 1 RE dataset, 2 models, temperature/N-scaling, stratification, OOD, selection curves) with honest negative-result framing
2. Three failure modes framework (ceiling, floor, model confounds) provides genuinely useful diagnostic categories
3. Best-of-N selection experiment (SJ vs random p=0.47) is the definitive practical test and the paper's strongest result

**Weaknesses identified:**
1. **Missing critical baselines (critical).** No comparison to log-probability, exact-match voting, or Universal Self-Consistency (Chen et al., NAACL 2024). Without these, the paper cannot distinguish "consistency fails for structured prediction" from "SJ and FK are poor operationalizations of consistency." Log-probability in particular is the elephant in the room—it requires zero additional inference cost.
2. **Temperature confound in cross-dataset comparison (major).** Table 1 uses T=1.0 for SciERC but T=0.7 for CoNLL and WNUT. This directly undermines the non-transferability argument, which is the paper's central claim. For a negative-result paper, controlled experimental conditions are non-negotiable.
3. **Formula-implementation discrepancy (major).** Paper defines SJ as symmetric set overlap (Eq. 1); the actual implementation uses type-grouped Hungarian matching with `max(|g_a|, |g_b|)` denominator per type group. These are mathematically different algorithms. Anyone reproducing from the paper equations would get different results.
4. **Inverted-U pattern lacks statistical support.** Jonckheere-Terpstra tests non-significant (NER p=0.12, RE p=0.38), yet the pattern drives the discussion and practitioner guidelines. The within-dataset stratification also introduces circularity: stratifying by greedy F1 then correlating consistency with F1 within strata mechanically compresses ρ at extremes via range restriction.
5. **Only 3 seeds for N=16 stability** and **Spearman ρ as sole evaluation metric** limit statistical conclusions. AUROC, calibration, Kendall's τ would strengthen the analysis.

**Additional methodological concerns:**
- Evaluation correlates consistency (from T>0 samples) with greedy F1 (T=0)—this cross-mode comparison is never justified
- Empty-set handling (both SJ and FK return 1.0 for empty-empty pairs) creates systematic bias, especially for RE where 42-44% of instances have all-zero F1
- Only 1 RE dataset; the compound error propagation explanation is plausible but untested beyond SciERC
- OOD test uses an already-weak model (WNUT F1=0.418), compounding floor effects rather than isolating distribution shift
- LoRA fine-tuning details (rank, alpha, target modules, LR, epochs) entirely missing

### R2 Summary — Score: 2/6 (Reject)

**Strengths identified:**
1. Thorough experimental coverage—11 experiments spanning datasets, models, temperatures, N-scaling, OOD, and selection curves
2. Honest reporting of predominantly negative results with attempt to explain mechanisms
3. Best-of-N selection failure (SJ cannot beat random, p=0.47) is a compelling concrete demonstration

**Weaknesses identified:**
1. **Low novelty (critical).** The failure modes (ceiling, floor, model confounds) are predictable from well-known statistical phenomena—range restriction, base-rate effects, and measurement noise. The inverted-U is not statistically confirmed. The technical contribution amounts to straightforward metric substitution (soft Jaccard as a self-agreement measure) with no algorithmic innovation or theoretical grounding.
2. **Critically insufficient related work.** Only 10 references for a venue-level submission. Key omissions:
   - Universal Self-Consistency (Chen et al., NAACL 2024)—the single most relevant prior work
   - Semantic uncertainty (Kuhn et al., ICLR 2023)
   - Calibration literature (Guo et al. 2017, Desai & Durrett 2020)
   - Selective prediction / abstention (Geifman & El-Yaniv 2017, Kamath et al. 2020)
   - Conformal prediction for NLP (Quach et al. 2023, Mohri & Romano)
   - LLM uncertainty estimation surveys (Geng et al. 2024, Ye et al. 2024)
   - Jiang et al. on verbalized uncertainty, Lin et al. on teaching models to express uncertainty
3. **Overgeneralized claims.** Title claims "self-consistency fails" but only two specific metrics (SJ and FK) are tested. Without external baselines or alternative consistency formulations, the conclusion scope is "SJ and FK don't work well," not "self-consistency fundamentally fails for structured prediction."
4. **Limited significance.** The practitioner guidelines amount to "don't use consistency-based confidence in most settings." No constructive alternatives are proposed. The audience is narrow since consistency-based TTS for IE was not established practice—the paper is warning against something few were doing.
5. **Weak motivation.** The paper does not adequately establish why practitioners would expect consistency to work for structured prediction in the first place. The reasoning→structured prediction extension is presented as "natural" but the differences (combinatorial output space, partial correctness, systematic errors) are predictable a priori.

---

## Step 2: Cross-Sharing

### R1 → R2 Key Points Shared
- The temperature confound in Table 1 is a concrete methodological flaw that R2 should factor into novelty assessment—if the cross-dataset comparison isn't even fair, the "non-transferability" finding is weaker than presented
- The formula-implementation discrepancy means the SJ metric as described in the paper is not the SJ metric as evaluated, further weakening claims about what "structural consistency" can or cannot do
- The missing log-probability baseline is especially relevant for R2's significance assessment: if the paper doesn't rule out the cheapest alternative, the practical contribution of the negative result is diminished

### R2 → R1 Key Points Shared
- The 10-reference bibliography is a red flag for experimental grounding—R1's concern about missing baselines (USC, log-prob) is reinforced by R2's finding that these works aren't even cited
- The novelty concern strengthens R1's methodological critique: if the failure modes are predictable a priori, the experimental evidence needs to be ironclad to justify publication; the current methodological issues (temperature confound, missing baselines) mean the evidence falls short of what a "confirming the expected" paper requires
- R2's point about overgeneralized claims aligns with R1's baseline concern: the paper cannot support claims about "self-consistency" generally when it only tests two specific operationalizations

---

## Step 3: Convergence — Areas of Agreement and Disagreement

### Strong Agreement (Both Reviewers)

1. **Missing baselines are the paper's most critical flaw.** Both reviewers independently identified that without log-probability, exact-match voting, and Universal Self-Consistency baselines, the paper's title-level claim ("self-consistency fails") is unsupported. The paper may be demonstrating that SJ and FK are poor metrics rather than that consistency is fundamentally uninformative.

2. **Temperature confound undermines the central comparison.** Both agree that using T=1.0 for SciERC and T=0.7 for CoNLL/WNUT in Table 1 is a serious methodological issue that directly weakens the non-transferability argument.

3. **Inverted-U is overclaimed.** Both reviewers note that non-significant trend tests (p=0.12, p=0.38) cannot support the inverted-U as a "finding"—it should be presented as a descriptive observation at best.

4. **Best-of-N selection result is the paper's strongest contribution.** Both agree that the SJ-vs-random comparison (p=0.47) with oracle headroom of 7.5pp is compelling and practically meaningful.

5. **Experimental breadth is commendable.** Both acknowledge the impressive scope of experiments for a negative-result study.

### Partial Agreement

6. **Related work adequacy.** R2 rates the 10-reference bibliography as critically insufficient (1/6); R1 flags specific missing works (USC) but focuses more on missing experimental baselines. Both agree the paper needs substantially more engagement with existing literature, but R1 is slightly more forgiving since the paper is empirical rather than theoretical. **Converged view:** The bibliography needs to at least double, with mandatory engagement with USC, semantic uncertainty, calibration, and selective prediction literatures.

7. **Novelty level.** R2 rates novelty very low (1.5/6), arguing failure modes are predictable; R1 gives more credit to the three-failure-modes framework as "genuinely useful diagnostic categories." **Converged view:** The failure modes are not surprising to experts but have value in being empirically documented—however, the empirical documentation must be methodologically sound, which it currently isn't.

### Disagreement

8. **Overall score.** R1: 3/6 (Weak Reject), R2: 2/6 (Reject). R1 gives more weight to experimental thoroughness and the honest negative-result framing; R2 weighs novelty and positioning more heavily. After cross-sharing, R1 acknowledges that the bibliography weakness is more severe than initially assessed, and R2 acknowledges that the best-of-N result has more standalone value than initially credited. **Resolution:** Both converge toward 3/6 (Weak Reject) as the appropriate score—below the acceptance bar but with a clear revision path.

---

## Step 4: Consolidated Review

### Summary

The paper systematically evaluates self-consistency metrics (structural soft Jaccard and Fleiss' Kappa) as confidence signals for information extraction across multiple datasets, models, and configurations, finding predominantly negative results. It identifies three failure modes (ceiling, floor, model confounds) and demonstrates that consistency-based best-of-N selection cannot outperform random selection despite substantial oracle headroom.

### Overall Assessment: 3/6 (Weak Reject)

The paper addresses a timely question and provides honest, extensive experimental evidence. The best-of-N selection failure is a genuinely useful result. However, critical methodological issues and positioning gaps prevent acceptance at a top venue.

### Consolidated Strengths

**S1. Comprehensive experimental coverage with honest framing.** The paper tests across 3 NER datasets, 1 RE dataset, 2 model families, 2 temperatures, 2 sampling budgets, plus capability stratification, per-relation-type analysis, OOD evaluation, and selection curves. For a negative-result paper, this breadth is impressive and scientifically mature.

**S2. Best-of-N selection futility is compelling.** The demonstration that SJ-based selection cannot beat random (p=0.47) despite 7.5pp oracle headroom translates abstract correlation numbers into a concrete practical statement. This is the paper's most publishable finding.

**S3. Three failure modes provide diagnostic value.** Ceiling effects (high accuracy → compressed consistency range), floor effects (low accuracy → false confidence), and model-specific confounds (format instability, boundary wobble) are clearly articulated and practically useful categories, even if individually unsurprising.

### Consolidated Weaknesses

**W1. Missing critical baselines make the negative claim uninterpretable (critical).** The paper compares only SJ against FK. Without comparison to (a) sequence log-probability (zero additional inference cost), (b) exact-match voting (the direct analogue of Wang et al.'s self-consistency), and (c) Universal Self-Consistency (Chen et al., NAACL 2024—the most directly relevant prior work, entirely absent), the paper cannot support its title-level claim that "self-consistency fails." It may be that SJ and FK are poor operationalizations while the consistency principle remains valid. This is the single most important revision needed.

**W2. Temperature confound in the central comparison (major).** Table 1 uses T=1.0 for SciERC but T=0.7 for CoNLL and WNUT. Since temperature affects ρ (Table 3), this confounds the cross-dataset comparison that forms the paper's central argument. For a negative-result paper claiming generalization failure, maintaining controlled conditions across datasets is a minimum requirement, not an optional nicety.

**W3. Insufficient related work and overgeneralized claims (major).** Only 10 references is critically inadequate. The paper fails to engage with Universal Self-Consistency, semantic uncertainty (Kuhn et al.), calibration literature, selective prediction, and conformal prediction for NLP. The absence of USC is particularly damaging since it directly addresses self-consistency for non-votable outputs. The title-level claim ("self-consistency fails for structured prediction") overgeneralizes from two specific metrics tested.

**W4. Formula-implementation discrepancy undermines reproducibility (major).** The paper presents SJ as symmetric set overlap (Eq. 1); the implementation uses type-grouped Hungarian matching with a different denominator. These are mathematically distinct algorithms with different matching behavior. Any reproduction from the paper equations alone would yield different results.

**W5. Inverted-U pattern is overclaimed.** Both formal trend tests fail to reach significance (NER p=0.12, RE p=0.38). The cross-dataset version rests on 3 confounded data points. The within-dataset stratification introduces circularity through range restriction. Yet this pattern drives the discussion, practitioner guidelines, and framing. The gap between evidence and claims is too large.

### Minor Issues

- Only 3 seeds for N=16 stability analysis; 5-10 needed for reliable CI construction
- Only 1 RE dataset limits generalizability of compound error propagation explanation
- OOD test compounds floor effects (already-weak WNUT model) rather than isolating distribution shift
- LoRA fine-tuning details (rank, alpha, target modules, learning rate, epochs) entirely missing
- Spearman ρ as sole evaluation metric—AUROC, calibration, Kendall's τ would strengthen analysis
- Evaluation correlates consistency from stochastic samples with greedy F1—this cross-mode design choice is never justified
- Empty-set handling (SJ=FK=1.0 for both-empty pairs) creates systematic bias, especially for RE

### Experiment Coverage Assessment

The paper covers all 11 planned experiments from the experimental design:
- exp-001 (N=16 scaling): ✓ Table 5, 6
- exp-002 (CoNLL-2003): ✓ Table 1
- exp-003 (WNUT-17): ✓ Table 1
- exp-004 (per-relation-type): ✓ Table 8
- exp-005 (temperature): ✓ Table 3
- exp-006 (best-of-N): ✓ Table 7
- exp-007 (LLaMA multi-model): ✓ Table 10
- exp-008 (RE N=16): ✓ Table 9
- exp-009 (capability stratification): ✓ Table 4
- exp-010 (selection curves): ✓ Table 7 (merged with exp-006)
- exp-011 (OOD): ✓ Table 2

Coverage is complete, though some expected figures (rho vs N line plots, signal-noise tradeoff curves, per-instance scatter plots) are absent from the paper—only tables are presented.

### Questions for Authors

**Q1.** How does SJ compare against sequence log-probability as a confidence/selection signal? Log-prob requires zero additional inference and is the natural first baseline. If SJ cannot beat it, the practical message simplifies to "don't bother with multi-sample methods."

**Q2.** Why are different temperatures used across datasets in Table 1? Can you provide all datasets at T=1.0 for a fair comparison, or both temperatures for all datasets with a formal interaction test?

**Q3.** The N=8→16 degradation (ρ 0.383→0.362): did you verify this using the first 8 of the 16 samples (nested comparison) to eliminate seed confounding?

**Q4.** For the capability stratification (Table 4), have you verified the inverted-U pattern holds when stratifying on an independent difficulty proxy (sentence length, entity count) rather than greedy F1, which introduces range-restriction circularity?

**Q5.** What is the paper's position relative to Universal Self-Consistency (Chen et al., NAACL 2024), which extends self-consistency to non-votable structured outputs using LLM-as-judge? Does USC address the limitations identified in this paper?

### Path to Acceptance

1. **Add log-probability and exact-match voting baselines** for all datasets and the selection experiment. If the negative result persists against these stronger baselines, the conclusion becomes far more compelling.
2. **Standardize temperature** to T=1.0 across all datasets in Table 1, or report both temperatures for all datasets.
3. **Expand references** to 25+ and engage substantively with USC, semantic uncertainty, calibration, and selective prediction literatures.
4. **Fix the formula-implementation discrepancy** so the paper accurately describes the algorithm used.
5. **Downgrade the inverted-U** from a confirmed finding to a descriptive observation, or provide additional statistical evidence.
6. **Add figures.** The paper is entirely table-based; selection curves, scatter plots, and rho-vs-N plots would substantially improve readability and persuasiveness.

### Reviewer Score Summary

| Reviewer | Focus | Initial Score | Post-Roundtable |
|----------|-------|--------------|-----------------|
| R1 | Methods + Experiments | 3/6 (Weak Reject) | 3/6 (Weak Reject) |
| R2 | Novelty + Related Work | 2/6 (Reject) | 3/6 (Weak Reject) |
| **Consensus** | | | **3/6 (Weak Reject)** |

### Verdict

**Weak Reject.** The paper tackles a relevant question with commendable experimental breadth and honest reporting. The best-of-N selection futility result is genuinely valuable. However, the missing baselines (especially log-probability and USC) make the title-level claim unsupportable, the temperature confound undermines the central comparison, the related work is critically thin, and the inverted-U is overclaimed. These are fixable issues—a revision addressing the five points above could produce a publishable paper.