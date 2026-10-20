---
dream_id: dream_20260513T092135
tier: median
overall_score: borderline reject
timestamp: 2026-05-13T10:11:23.819562+00:00
---

# Dream Review Report: "When Does Cross-Method Consensus Improve Circuit Discovery?"

**Venue:** EMNLP 2026 Findings (ARR review form)
**Review Mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-13

---

## Meta-Review Summary

This paper tests whether binary consensus scoring (CSS) — intersecting the top-N edges from K=3 circuit discovery methods (EAP-IG, Edge Pruning, ACDC) — improves circuit faithfulness. Evaluated on 4 tasks × GPT-2 Small plus IOI on Qwen-0.5B (5 configurations total). The main finding is negative: CSS produces a marginal advantage on only 1/5 configurations (IOI/GPT-2, ΔCPR=0.08, p=0.09), which attenuates to Δ=0.02 (p=0.27) after controlling for circuit size. Three failure modes are identified: ACDC binarization pathology, consensus redundancy under high agreement, and scoring granularity mismatch at scale.

The paper is honest, statistically rigorous in its reporting, and identifies one genuinely novel finding (FM3: scoring granularity degeneration). However, it suffers from low methodological novelty, critical missing experiments, and insufficient engagement with concurrent work on continuous consensus methods.

---

## R1 Review: Methods and Experiments

### Summary
The paper applies a straightforward binary intersection consensus to three circuit discovery methods across five configurations, finding that consensus rarely helps. The experimental methodology is sound in what it covers (bootstrap CIs, size-controlled baselines) but has critical gaps (no ablation method comparison, asymmetric size controls).

### Strengths
1. **Honest negative reporting with appropriate statistical hedging.** The paper does not overclaim. IOI is characterized as "marginal positive" with explicit p-values and CIs. This calibration is exemplary.
2. **Size-controlled IOI baseline is well-executed.** Table 1-2 directly addresses the most obvious confound (7 edges vs 100 edges) with proper decomposition, showing 58-87% of the advantage is attributable to size.
3. **Bootstrap methodology is sound.** BCa intervals with B=10,000 are appropriate. The choice to report one-sided p-values for directional hypotheses is correct.
4. **ACDC binarization pathology (FM1) is a concrete, actionable finding.** Practitioners can immediately apply the recommendation to use uniform top-N binarization. The observed Jaccard shift of +0.16 to +0.25 after normalization quantifies the artifact.
5. **Qwen scaling analysis (FM3) provides genuine mechanistic insight.** Tables 5-6 demonstrate that scoring granularity degrades at scale — IFR collapses to block-level, ACDC to node-level — explaining near-zero cross-method overlap as an architectural limitation rather than a bug.

### Weaknesses
1. **Missing zero-vs-mean ablation comparison is a critical gap.** All evaluations use zero ablation, which has known biases for small circuits (k=7 edges out of 32K). Zero ablation amplifies the signal of small circuits by zeroing out nearly all edges, potentially inflating or deflating CPR differences. The paper acknowledges this in §6 but the incomplete comparison (plan_011) means the headline "1/5 positive" finding may be ablation-method-specific. This is not a minor robustness check — it could fundamentally change which configurations are positive/negative.
2. **Jaccard diagnostic receives disproportionate coverage for n=5, p=0.19.** Section 4.6 and Table 7 present a diagnostic that fails conventional significance thresholds. The Spearman ρ=−0.70 looks impressive but is meaningless at n=5 (any 3 concordant pairs would produce a similar ρ). The paper appropriately calls it a "motivated conjecture," but it still receives a full section and a named practitioner guideline — this oversells the evidence.
3. **K=3 is effectively K≈2.** EAP-IG and EP are both gradient-based methods with Jaccard=0.54 on Qwen-0.5B. The consensus ensemble lacks true methodological diversity. This means binary intersection of K=3 with two correlated voters is testing a much weaker form of consensus than the ensemble theory framework (Kuncheva & Whitaker 2003) assumes. The paper acknowledges this in §6 but does not analyze how results would change with a genuinely diverse third method.
4. **Size-controlled baselines applied asymmetrically.** Table 1-2 rigorously controls for size on IOI (the positive case) but the failing configurations (Arithmetic, SVA, Factual Recall) also have size discrepancies between CSS=1.0 and top-100 circuits. Without symmetric size controls, we cannot distinguish "consensus fails" from "consensus circuits are too small to capture the task" on the failing cases.
5. **100 prompts per task with a single seed is thin.** Bootstrap CIs are wide (IOI original: [−0.01, 0.17]), reflecting limited statistical power. No analysis of prompt diversity or sensitivity to prompt sampling is provided. Hardware-level variance or prompt selection could shift borderline results between pass and fail.

### Questions for Authors
1. Do you have any partial data on mean ablation for configurations beyond IOI? Even qualitative observations about how CPR rankings change under mean ablation would help readers assess the robustness of the negative findings.
2. For the three failing configurations, what are the CSS=1.0 circuit sizes? If they are also very small (< 10 edges), the "failure" might be better characterized as "insufficient consensus edges" rather than "consensus doesn't work."
3. Have you considered Bonferroni or false discovery rate correction across the 5 configurations? The IOI original p=0.089 is already non-significant; multiple testing correction would push it further.

### Missing Experiments / Suggestions
- **Priority 1:** Zero vs mean ablation comparison across all 4 GPT-2 tasks. This could change the central claim.
- **Priority 2:** Size-controlled baselines for Arithmetic, SVA, and Factual Recall (not just IOI).
- **Priority 3:** Sensitivity analysis on the top-N threshold (currently fixed at 100). Does varying N from 50 to 200 change which configurations are positive/negative?
- **Priority 4:** Multiple random seeds for the 100-prompt evaluation sets to quantify sampling variance.

### Scores
- Soundness: 3/5 (Acceptable — main claims are supported but critical ablation is missing)
- Excitement: 2.5/5 (Between marginally interesting and interesting)
- Overall: 3.0/5 (Findings-level, but at the lower end)
- Confidence: 4/5 (Quite sure — familiar with circuit discovery and statistical methodology)

### Justification
The paper's empirical methodology is sound within its scope, and the honest negative reporting is valuable. However, the missing zero-vs-mean ablation comparison and asymmetric size controls create uncertainty about whether the headline negative result is robust. The paper is at the Findings threshold but could fall below if the ablation gap proves consequential.

---

## R2 Review: Novelty and Related Work

### Summary
The paper applies the stability index intersection framework (Nogueira & Brown 2016) to circuit discovery, finding it mostly fails. The failure mode taxonomy connects to known ensemble theory conditions. One finding (FM3: scoring granularity degeneration at scale) is genuinely novel, but the overall novelty bar is not clearly met for the target venue.

### Strengths
1. **FM3 (scoring granularity degeneration) is genuinely novel and transcends the paper's framework.** The observation that IFR and ACDC degenerate to block-level and node-level scoring on larger models (Table 5-6) is an insight about these methods' architectural limitations, not just about consensus. This finding has implications for any aggregation or comparison of circuit discovery methods at scale.
2. **Size-controlled baseline (Tables 1-2) is excellent experimental design.** The decomposition showing 58-87% of CSS advantage is attributable to circuit size is a model for how confound analysis should be done in this field.
3. **Statistical reporting is honest and appropriately calibrated.** The paper uses "marginal," "directional evidence," and "motivated conjecture" rather than overclaiming. Bootstrap CIs are reported for all key comparisons.
4. **The negative-result framing is epistemically responsible.** The field benefits from knowing that an intuitive approach (consensus = better) does not hold, and the paper frames this constructively by identifying when it might work (low Jaccard regime).

### Weaknesses
1. **CSS has zero methodological novelty.** The consensus scoring formula (Eq. 1) is a direct instance of the stability index from Nogueira & Brown (2016). The paper acknowledges this ("Our contribution is not the consensus framework itself") but then positions the failure mode analysis as the contribution. However, two of three failure modes (binarization pathology, consensus redundancy) are predictable consequences of violating the known conditions for ensemble improvement (independence, diversity) from Kuncheva & Whitaker (2003). Only FM3 adds genuinely new insight.
2. **Critical gap: no engagement with continuous averaging (Mondorf et al. 2025).** The paper cites Mondorf et al. in §2 but never tests or substantively discusses why continuous consensus might succeed where binary consensus fails. This is a potentially fatal omission: if score averaging avoids the binarization artifacts that drive FM1, and handles the granularity mismatch differently than intersection, then the paper's conclusion narrows from "consensus fails" to "this particular crude form of consensus fails" — a substantially weaker contribution.
3. **Two of three failure modes are predictable from existing theory.** FM1 (binarization pathology) = one method's output dominates when its native threshold differs from the top-N applied to others. This is an obvious consequence of mixing binarization strategies, not a discovery. FM2 (high agreement → redundant consensus) is literally the diversity requirement from Kuncheva & Whitaker (2003). Only FM3 offers new insight beyond what a reader of the ensemble literature would already expect.
4. **Only 14 references — well below venue norms.** EMNLP Findings papers typically cite 30-40 references. The sparse bibliography misses: subnetwork pruning (Frankle & Carlin 2019, lottery ticket), other circuit discovery methods (causal scrubbing, activation patching variants), negative-result papers in interpretability, and the broader ensemble learning literature beyond Kuncheva and Nogueira.
5. **IFR is used for Qwen-0.5B experiments (Tables 5-6) but is never formally defined in §2.** It is mentioned in passing as a "hybrid approach" in §1 and a "Iterative Feature Refinement" in the introduction, but the reader has no citation, no description of the algorithm, and no justification for why it replaces one of the three methods on the larger model. This is a significant methodological gap for an 8-page paper.

### Questions for Authors
1. Can you provide even a qualitative argument for why continuous averaging (Mondorf et al. 2025) would or would not exhibit the same failure modes? If FM1 is specific to binarization and FM3 is about granularity (which affects both binary and continuous methods), this decomposition would clarify the paper's scope.
2. Why was IFR used on Qwen-0.5B instead of maintaining the same K=3 method set (EAP-IG, EP, ACDC)? If ACDC was too expensive to run on 179K edges, this should be stated. If IFR was chosen for other reasons, the rationale should be explicit.
3. Given that Nogueira & Brown (2016) provide theoretical conditions under which stability index intersection improves over individual selectors, have you verified that your K=3 method set satisfies those conditions on any configuration? If the conditions are violated everywhere, the negative result is expected rather than surprising.

### Missing Related Work / Positioning Issues
- **Mondorf et al. (2025)** — cited but not tested or substantively discussed. Must engage with continuous averaging as the obvious alternative to binary consensus.
- **IFR** — used experimentally but never cited or defined. Needs a proper citation and at least a paragraph of description.
- **Subnetwork pruning / lottery ticket literature** (Frankle & Carlin 2019) — relevant to the broader question of whether consensus helps in sparse subnetwork identification.
- **Negative results in interpretability** — e.g., Bolukbasi et al. on debiasing failures, Jacovi & Goldberg (2020) on faithfulness of explanations. The paper would benefit from positioning itself within a broader tradition of useful negative results.
- **Additional circuit discovery methods** — causal scrubbing (Chan et al. 2022), path patching — would contextualize the K=3 choice and the K≈2 limitation.
- **Ensemble aggregation beyond intersection** — rank aggregation, weighted voting, stacking — to motivate why binary intersection was tested rather than these alternatives.

### Scores
- Soundness: 3/5 (Acceptable — what is tested is done correctly, but scope is too narrow)
- Excitement: 2/5 (Marginally interesting — FM3 is novel but buried under predictable findings)
- Overall: 2.5/5 (Borderline Findings — below threshold due to novelty deficit and missing Mondorf comparison)
- Confidence: 4/5 (Quite sure — strong background in both ensemble theory and mechanistic interpretability)

### Justification
The paper is honest and methodologically sound within its narrow scope, but the novelty bar is not met. CSS is a known framework, two of three failure modes are predictable, the most interesting finding (FM3) is underemphasized, and the failure to engage with continuous consensus alternatives leaves the central contribution ambiguous. A revised version that tests continuous averaging, properly introduces IFR, expands the bibliography, and reframes FM3 as the headline would likely cross the Findings threshold.

---

## Roundtable Convergence

### Points of Agreement
1. **K=3 is effectively K≈2** — both reviewers independently flag the EAP-IG/EP correlation (Jaccard=0.54) as undermining the diversity assumption required for ensemble benefit.
2. **Jaccard diagnostic is underpowered** — n=5, p=0.19 receives disproportionate prominence for a result that does not approach significance.
3. **Honest statistical reporting is a genuine strength** — appropriate hedging, bootstrap CIs, and willingness to report negative results.
4. **Size-controlled IOI analysis is well-executed** — model confound analysis for the field.
5. **FM3 (scoring granularity degeneration) is the most novel and interesting finding.**

### Points of Disagreement

**1. Severity of novelty deficit**
- R2 (harsher): CSS=stability index, FM1 and FM2 are predictable from ensemble theory → novelty is near-zero except for FM3.
- R1 (more lenient): FM1 (ACDC binarization) is actionable even if theoretically predictable → practical value compensates for limited novelty.
- **Resolution:** R2's position is stronger. Practical value of FM1 is real but modest — the fix (use uniform top-N) is obvious once the problem is stated. FM3 carries the novelty burden and should be the paper's centerpiece.

**2. Most critical missing experiment**
- R1: Zero-vs-mean ablation across all tasks — could overturn the headline negative result.
- R2: Continuous averaging comparison (Mondorf et al. 2025) — could reframe the entire contribution.
- **Resolution:** Both are needed, but R2's is more fundamental. The continuous averaging question determines whether the paper is about "consensus failing" or "binarization failing." The ablation question is important but operates within the existing framing.

**3. Overall score**
- R1: 3.0/5 (Findings)
- R2: 2.5/5 (Borderline Findings)
- **Resolution:** Consensus at 2.5–3.0. The cumulative weight of issues (low novelty + missing Mondorf comparison + K≈2 + Jaccard underpowered + missing ablation comparison) tilts toward the lower end. The paper is currently below the Findings threshold but not far from it.

### Consensus Assessment

- **Strongest contribution:** FM3 — scoring granularity degeneration at scale. This finding transcends the consensus framework and informs any future work on comparing or aggregating circuit discovery methods across model scales.
- **Most critical weakness:** Failure to test or substantively discuss continuous averaging (Mondorf et al. 2025). Without this, the paper cannot distinguish "consensus fails" from "binarization fails."
- **Consensus score range:** 2.5–3.0, centering at **2.5** (Borderline Findings).
- **Findings threshold:** Below in current form due to the combination of low methodological novelty and critical missing comparisons. The distance is not large — addressing the top two recommendations would likely push it above threshold.

### Key Recommendations for Authors (Priority Order)

1. **Test continuous averaging (Mondorf et al. 2025) on all 5 configurations.** If it also fails, the "consensus fails" claim is strengthened. If it succeeds, reframe the paper as "why binarization fails for circuit consensus." Either outcome improves the paper.
2. **Run zero-vs-mean ablation comparison across all GPT-2 tasks.** Determine whether the negative results are ablation-method-specific.
3. **Reframe FM3 as the primary contribution.** Restructure so granularity degeneration is the central finding, with FM1 as a practical note and FM2 folded into the K≈2 discussion.
4. **Properly introduce IFR** with citation and algorithm description. It is used in key experiments (Tables 5-6) but never defined.
5. **Expand bibliography to 30+ references.** Cover subnetwork pruning, additional circuit discovery methods, ensemble aggregation literature, and negative-result papers in interpretability.
6. **Apply size-controlled baselines to failing configurations** (not just IOI) for symmetric analysis.
7. **Downweight the Jaccard diagnostic** from a full section to a paragraph-level observation given n=5, p=0.19.

---

## Experiment Coverage Assessment

| Planned Experiment | Status | In Paper? | Notes |
|---|---|---|---|
| GPT-2 Factual Recall K=3 CSS | Completed, inconclusive | Yes (Table 4) | Adds 4th failure pattern (component-type preference) |
| IOI size-controlled baseline | Completed | Yes (Tables 1-2) | Well-executed confound analysis |
| Bootstrap CIs on CPR | Completed | Yes (Table 3) | Sound methodology, wide CIs reflect low power |
| Ablation method comparison (zero vs mean) | NOT completed | Mentioned in §6 | Critical gap — could change headline finding |
| IFR vs ACDC divergence analysis (Qwen) | Completed (analysis only) | Yes (Tables 5-6) | Strongest finding (FM3) |
| Jaccard-CSS scatter + correlation | Completed | Yes (Table 7) | Underpowered (n=5, p=0.19) |

Coverage: 5/6 planned experiments completed and included. The missing ablation comparison is the most consequential gap.

---

## Final Scores (Roundtable Consensus)

| Dimension | R1 | R2 | Consensus |
|---|---|---|---|
| Soundness | 3 | 3 | **3/5** (Acceptable) |
| Excitement | 2.5 | 2 | **2/5** (Marginally interesting) |
| Overall | 3.0 | 2.5 | **2.5/5** (Borderline Findings) |
| Confidence | 4 | 4 | **4/5** (Quite sure) |

**Verdict: Borderline Findings — revise and resubmit.** The paper is epistemically responsible and identifies one genuinely novel finding (FM3), but the combination of low methodological novelty, critical missing comparisons (continuous averaging, ablation methods), and insufficient experimental scope (K≈2, n=5 for diagnostic) places it below the Findings acceptance threshold in its current form.
