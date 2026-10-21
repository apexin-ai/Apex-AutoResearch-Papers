---
dream_id: dream_20260519T034058
tier: median
overall_score: Borderline Reject (3/6)
timestamp: 2026-05-19T04:47:23.173056+00:00
---

# Dream Review Report

**Paper:** Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning

**Headline Assessment:** Borderline Reject (3/6)

**Review Mode:** Full (2 Reviewers, complete roundtable)

---

## Summary

The paper proposes SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic constraints from multiple LLM reasoning traces and uses weighted MAX-SAT solvers for answer selection. Through evaluation across 5 model families, 5 reasoning domains, and 20+ experimental conditions, the paper finds that SICA rarely outperforms simple self-consistency (SC), with the only statistically significant positive result on Mistral-7B FOLIO (+3.9pp, p=0.022) under specific hyperparameters. The paper uses the Condorcet Jury Theorem and Fleiss' kappa to explain this via an "independence bottleneck" (Effective-K metric), demonstrates with an oracle control (+14.22pp) that the MAX-SAT mechanism works with gold constraints, and shows 9 remediation strategies all fail to close this gap. A zero-cost C0+SC diagnostic is proposed for deployment decisions.

The paper is well-executed as a negative result study with thorough experimental coverage. However, it has significant issues with statistical rigor, a data presentation error that undermines a key contribution claim, and limited novelty.

---

## Reviewer 1: Methods + Experiments

### Strengths

1. **Broad experimental coverage.** 5 model families (Qwen, Mistral, LLaMA, DeepSeek, QwQ), 5 domains (FOLIO, ProofWriter, StrategyQA, ARC-Challenge, GSM8K), and 20+ conditions provide comprehensive evidence for the negative result. The breadth across model scales (7B-72B), architectures (standard vs. reasoning-specialized), and domains (logic, commonsense, math) is commendable.

2. **Oracle control is the paper's strongest experiment.** Replacing self-extracted constraints with gold FOL annotations on Qwen-14B FOLIO yields +14.22pp (p=2.0e-7), cleanly separating mechanism quality from extraction quality. This is a well-designed counterfactual that definitively shows the MAX-SAT aggregation mechanism itself is sound.

3. **MAX-SAT vs. count-only ablation is revealing.** Agreement on 803/804 questions demonstrates that the solver's combinatorial optimization provides no value over simple counting under current constraint quality. This is a strong mechanistic finding about constraint redundancy.

4. **Appropriate statistical methodology.** McNemar's test for paired binary outcomes is the correct choice. The claim scoping convention (n=60 "suggestive", n>=200 "confirm") shows statistical awareness. Bootstrap CIs for temperature sensitivity add rigor.

5. **Nine remediation strategies provide breadth-of-failure evidence.** Spanning prompting (2), architecture (2), capability (1), verification (2), and diversity (2) approaches, the systematic failure strengthens the structural bottleneck thesis.

### Weaknesses

1. **[Major - idea level] No multiple comparison correction for the only significant result.** The paper evaluates 17 conditions in Table 1 and reports the Mistral-7B FOLIO result (p=0.022) as the sole statistically significant positive finding. At alpha=0.05 with 17 tests, the expected number of false positives is ~0.85. A Bonferroni correction yields adjusted alpha=0.003, under which p=0.022 is no longer significant. The paper does not discuss multiple comparison corrections at all. Furthermore, the paper acknowledges only 2 of 3 seeds produce significant results (Section 6.4), making the finding seed-dependent.

   **Why Major:** This matches the calibration criterion "统计不显著的结果被作为 contribution 声称." The paper's Contribution 1 claims to "identify the narrow operating regime where gains occur," but if the single significant result doesn't survive multiple comparison correction, no operating regime has been reliably identified. The paper's core positive claim is undermined.

2. **[Major - idea level] Table 6 misclassification breaks Contribution 4.** StrategyQA has C0=10.0% but is listed in the "C0 >= 20%" group in Table 6. The paper's Contribution 4 claims "perfect negative predictive value: all conditions with C0 < 20% show Delta <= 0." If StrategyQA (C0=10%) is correctly placed in the C0<20% group, it shows Delta=+3.3pp, directly contradicting this claim. The "perfect NPV" becomes 4/5 = 80%. While the +3.3pp is non-significant (p=0.135), the claim is framed as a directional prediction, not a significance claim.

   **Why Major:** This matches "实验范围不足以支撑论文 claim 的 generality." A contribution's core claim is literally falsified by an error in data presentation. Even if the underlying data supports a weaker version of the claim (e.g., "no significant positive Delta when C0<20%"), the paper as written makes a stronger claim that is incorrect.

3. **[Minor - idea level] Oracle control limited to a single condition.** The oracle experiment uses Qwen-14B FOLIO but not the Mistral-7B condition where SICA actually shows positive results. Testing the oracle on Mistral-7B FOLIO would reveal how much headroom exists in the one condition that works, and whether the +3.9pp captures a meaningful fraction of the oracle upper bound for that specific condition.

4. **[Minor - idea level] Small sample sizes limit regime classification confidence.** Many conditions use n=60, making the Type A/B/C regime classification based on unstable point estimates. For example, LLaMA-8B D012 (n=60, Delta=+6.7, p=0.219) is classified as "Goldilocks?" but the evidence is too weak to reliably distinguish it from Type A or Type C.

5. **[Minor - presentation level] Seed reporting unclear for the key result.** Table 1 reports Mistral-7B FOLIO Delta=+3.9 (p=0.022) but doesn't specify which seed. Section 6.4 reveals 2/3 seeds are significant. The main table should clarify whether this is a specific seed or an average, and ideally report all 3 seeds in the main text.

### R1 Score: 3/6 (Borderline Reject)

---

## Reviewer 2: Novelty + Related Work

### Strengths

1. **Honest negative result framing.** The paper resists the temptation to oversell SICA and instead focuses on understanding why it fails. This intellectual honesty is valuable and relatively rare. The pivot from "method paper" to "analysis paper" is handled well in the body text.

2. **The Eff-K + dual bottleneck framework is a useful conceptual lens.** Even though the Eff-K formula itself is standard (see weaknesses), the application to same-model trace independence in the LLM context is novel and informative. The regime taxonomy (Type A: confirmation bias; Type B: domain informalizability; Type C: noise dominance; Goldilocks zone) provides a clear mental model.

3. **Clear narrative arc.** The paper follows a coherent story: negative result, explain via CJT, oracle shows mechanism works, bottleneck is extraction, remediation fails, practical diagnostic. Abstract/Introduction/Conclusion are aligned.

4. **The C0 + SC diagnostic is a practical contribution** (despite the Table 6 bug). The zero-cost deployment check concept is valuable for practitioners considering symbolic augmentation.

### Weaknesses

1. **[Major - idea level] Core finding is somewhat predictable, limiting novelty.** The insight that same-model LLM traces are correlated (and therefore symbolic aggregation of their outputs won't help much) is expected by practitioners familiar with self-consistency. The paper quantifies this well (kappa=0.21-0.82, Eff-K=1.08-3.63), but the qualitative finding is not surprising. The primary novelty lies in the systematic quantification and the failed remediation attempts, which is more incremental than transformative.

   **Why Major (borderline):** For a top ML venue with ~25% acceptance, the contribution bar is high. The paper's core message ("don't bother with symbolic constraints unless you solve the independence problem") is important but can be summarized in a paragraph. The detailed analysis fills 10 pages but doesn't yield surprising insights beyond "traces are correlated, constraints mirror model bias, and no simple fix works." This is borderline between Major and significant Minor.

2. **[Major - presentation level] Reference list is critically thin.** Only 14 references for a 13-page paper targeting a top ML venue is insufficient. Critical gaps:
   - DyLoS, Aristotle, FoVer are mentioned in the Related Work text but have no corresponding bibliography entries. This is a clear writing error.
   - Missing citations for verification-guided tree search methods (MCTS-based reasoning), which represent the main alternative paradigm for using formal methods at test time.
   - Missing broader neuro-symbolic reasoning literature (NeSy community work).
   - Missing more SC variants (complexity-based prompting, diverse verifier tree).
   - The multi-agent debate line (Du et al., Liang et al.) is cited but not discussed relative to the independence argument, which is directly relevant.
   - Expected reference count for this scope: 35-50 citations.

3. **[Minor - idea level] Eff-K formula provenance not acknowledged.** The formula K/(1+(K-1)*kappa) is the standard effective sample size under equicorrelated observations, well-known in survey sampling and meta-analysis (Kish 1965, design effect literature). The paper presents it as a definition (Equation 1) without noting this statistical heritage. This makes the contribution appear more novel than it is and may draw criticism from statistically-literate reviewers.

4. **[Minor - idea level] Method-vs-analysis framing inconsistency.** The Abstract opens with method framing ("a method we call Symbolic Invariant Consensus Aggregation"), then pivots to analysis findings. The Introduction does better, but the paper could benefit from explicitly framing itself as an analysis paper from the start: "We designed SICA to test whether symbolic constraints help majority voting; they don't; here's why."

5. **[Minor - presentation level] Cross-share with R1 confirms the StrategyQA Table 6 error directly undermines story consistency.** The C0 diagnostic narrative flows as: "C0<20% always means no gain" leading to the practical deployment recommendation. If StrategyQA (C0=10%) has +3.3pp gain, the narrative breaks. While the +3.3 is n.s., the paper's claim is about the direction, not significance.

### R2 Score: 3/6 (Borderline Reject)

---

## Cross-Reviewer Convergence (Step 3)

Both reviewers converge on a score of 3/6.

**Areas of agreement:**
- The paper is a well-executed negative result study with thorough experimental coverage
- The oracle control is the strongest contribution
- The Table 6 StrategyQA misclassification is a clear error undermining Contribution 4
- The positive evidence (Mistral FOLIO) is fragile and lacks multiple comparison correction
- The reference list is insufficient for a top ML venue

**Areas of mild disagreement:**
- R1 is slightly more favorable toward the experimental breadth, viewing the 9 remediation failures as strong evidence
- R2 is more critical of novelty, viewing the core insight as predictable
- Both agree this is borderline: the analysis quality is high, but the contributions are incremental and the statistical rigor has gaps

**Resolution:** No further rounds needed. Both reviewers converge at 3/6.

---

## Consolidated Assessment

### Overall Score: 3/6 (Borderline Reject)

### Major Issues (2 confirmed + 1 borderline)

1. **Statistical fragility of the sole positive result (R1-W1).** The only significant positive finding (Mistral-7B FOLIO +3.9pp, p=0.022) does not survive Bonferroni correction across 17 tested conditions (adjusted alpha=0.003). The paper neither applies nor discusses multiple comparison corrections. Combined with seed dependency (2/3 significant), this undermines Contribution 1's claim of identifying a reliable operating regime. *Fixable via revision: add correction, reframe as exploratory/suggestive.*

2. **Table 6 data presentation error breaks Contribution 4 (R1-W2, R2-W5).** StrategyQA (C0=10%) is misplaced in the C0>=20% group. Correctly classified, it violates the "perfect negative predictive value" claim (C0<20% always implies Delta<=0). *Fixable via revision: reclassify and weaken the claim to "no statistically significant positive Delta when C0<20%."*

3. **Limited novelty for a top venue (R2-W1, borderline Major).** The core finding that same-model traces are correlated and symbolic aggregation inherits model bias is qualitatively expected. The systematic quantification and remediation failures add value but are incremental. The Eff-K formula is a known statistical result repackaged. *Not easily fixable: this is a fundamental scope question. The paper may fit better as a shorter format (e.g., Findings track, workshop paper) where the contribution bar is different.*

### Minor Issues

4. Oracle control limited to single condition (R1-W3)
5. Small n=60 for regime classification (R1-W4)
6. Seed reporting unclear in main table (R1-W5)
7. Reference list critically thin: 14 refs, missing citations for named systems (R2-W2)
8. Eff-K formula statistical provenance unacknowledged (R2-W3)
9. Method-vs-analysis framing inconsistency (R2-W4)

### Calibration Check

3 Major issues identified (2 confirmed + 1 borderline). Calibration rule: "3+ Major issues → not higher than Borderline Reject, unless each has a clear minor revision path." Issues 1 and 2 are fixable; Issue 3 (novelty) is not easily fixable. Score of 3 is consistent with calibration.

### Recommendation

The paper presents a thorough negative result analysis with genuine value for the community. The experimental breadth (5 models, 5 domains, 9 remediation strategies) and the oracle control experiment demonstrate significant research effort. However, the statistical foundations of the positive claims are weak, a data error undermines a key contribution, and the novelty is limited for a top venue main track. The paper would benefit from:
1. Adding multiple comparison correction and reframing the Mistral result appropriately
2. Fixing the Table 6 StrategyQA classification and softening Contribution 4
3. Expanding the reference list substantially (aim for 35+ citations)
4. Acknowledging the Eff-K formula's statistical heritage
5. Considering a shorter format (Findings, workshop) where the negative result + analysis framing may find a more receptive audience

### Issue-Level Classification

| # | Issue | Level | Severity |
|---|-------|-------|----------|
| 1 | No multiple comparison correction | idea | Major |
| 2 | Table 6 StrategyQA misclassification | idea | Major |
| 3 | Limited novelty for top venue | idea | Major (borderline) |
| 4 | Oracle on single condition only | idea | Minor |
| 5 | Small n for regime classification | idea | Minor |
| 6 | Seed reporting unclear | presentation | Minor |
| 7 | Thin reference list (14 refs) | presentation | Major |
| 8 | Eff-K provenance unacknowledged | presentation | Minor |
| 9 | Method/analysis framing inconsistency | presentation | Minor |