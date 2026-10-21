---
round: 13
overall_score: 3.0 Findings
timestamp: 2026-05-18T15:50:29.005071+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---


# Consolidated Review Report — Round 14 (Updated)
## "Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models"
### Target Venue: EMNLP 2026 (ARR May 2026 cycle)

*Updated to incorporate both Reviewers' full cross-responses.*

---

## Summary

This paper investigates layer selection as a researcher degree of freedom in hidden-state (HS) safety probing for reasoning LLMs. The core finding is that a biased composite metric (balanced accuracy × crossing rate) systematically selects shallow layers at 32B scale, reversing the HS-vs-text advantage; principled layer selection recovers significance on all four models. The paper also reports that the HS advantage is encoder-conditional (survives against 384d MiniLM but largely disappears against 1024d BGE-large), partially position-mediated (3/4 models retain significance after residualization), and bounded by high FPR (39–52%) and an 85.5% oracle gap. Seven negative-result baselines (BOCPD, CUSUM, Mahalanobis, RepE, MLP, CCS, cross-model transfer) define method boundaries. Experiments span 4 models across 2 architectures and 2 scales (7–8B, 32B) using the HarmThoughts dataset.

The paper makes a genuine methodological contribution to probing methodology, but suffers from severe sample size limitations at 32B (n=19–20), cumulative hyperparameter overfitting risk, single-dataset dependence, and an encoder-conditional finding that undermines the practical significance of the HS advantage claim. The work is better positioned as a methodological cautionary note than an empirical advance.

---

## Strengths

**S1. Genuine methodological insight on layer selection bias.** The demonstration that crossing rate systematically biases layer selection toward shallow layers, reversing study conclusions at 32B scale, is a valuable contribution to probing methodology. The five-metric ablation (Table 2) is well-designed and the sign-flip is clearly documented. This finding generalizes beyond safety probing.

**S2. Rigorous statistical framework.** Exact sign-flip permutation tests (2^19 and 2^20 full enumeration), Holm-Bonferroni correction across 12 tests with effective DoF=4, bootstrap CIs, and control task selectivity (Hewitt and Manning 2019) demonstrate strong statistical awareness. The power analysis (Appendix T) honestly quantifies detection limits.

**S3. Comprehensive negative results.** Seven methods that failed (Table 5), including BOCPD, CUSUM, Mahalanobis distance, RepE, MLP probes, CCS, and cross-model transfer, are documented with sufficient detail for reproducibility. This is genuinely useful for the community and prevents redundant work.

**S4. Transparent limitations.** The paper is unusually forthright about its weaknesses: FPR 39–52%, oracle gap 85.5%, cumulative hyperparameter search space (2,240 configs), position-mediated advantage for R1-32B, and small sample sizes at 32B. The dagger notation for 32B conclusions is appropriate.

**S5. Multi-seed robustness analysis.** Five random seeds with per-seed HB significance testing (Appendix R) goes beyond standard practice and reveals meaningful variance (R1-8B: 3/5 seeds, OT-7B: 5/5 seeds).

**S6. Responsible disclosure.** The bug disclosure appendix (Appendix M) and ethical considerations are commendable.

---

## Weaknesses

### Must-Fix (Critical)

**MF1. 32B sample size undermines central claims.**
n=19 (QwQ-32B) and n=20 (R1-32B) traces yield K=5 fold CV with 4–5 traces per fold (3–4 per class in validation). The paper's power analysis shows MDE of 8.6–9.5pp at 80% power, yet reports effect sizes of +1.9pp (R1-32B residualized) as "non-significant." More critically, the cumulative hyperparameter search (layer x W x K x threshold = 2,240 configs) on these tiny validation sets creates severe overfitting risk. The "all four models significant†" claim in the conclusion, while marked with a dagger, is the paper's headline result but rests on this fragile foundation. The gap between 7–8B (n=43–47, credible) and 32B (n=19–20, underpowered) should be the central framing tension, not a footnoted caveat.

**MF2. Encoder-conditional advantage undermines practical significance.**
The HS advantage survives HB correction against 384d MiniLM (4/4 models) but only 1/4 against 1024d BGE-large. The paper acknowledges this but the Discussion frames it as "a continuum" rather than confronting the implication: with a sufficiently strong text encoder, the HS advantage likely vanishes. Since LLM-based encoders (E5-Mistral-7B, 4096d) are readily available, the practical window for HS advantage may already be closed. The paper should either demonstrate advantage against a strong encoder or reframe the contribution as purely methodological (layer selection insight) rather than empirical (HS beats text). [R1 rebuts that layer selection and encoder quality are independent contributions; acknowledged, but the paper's narrative conflates them.]

**MF3. Single dataset (HarmThoughts) with unknown generalizability.**
All experiments use one English-language benchmark with a specific harm taxonomy and annotation protocol. The CP annotation methodology is inherited without independent IAA validation. The paper acknowledges this in Limitations but the scope of claims throughout (especially in Abstract and Conclusion) does not adequately reflect this constraint. "All four models" sounds like broad validation but is actually four models on one dataset. [Both reviewers AGREE; R1 notes the mechanistic argument (cosine volatility is architecture-dependent) provides partial but not sufficient generalization basis.]

**MF4. Circularity risk in BA-optimal layer selection.**
The BA-layer comparison (Appendix S, Table S10) selects layers that maximize BA, then reports BA improvements. While the paper uses K-fold CV to separate selection from evaluation, with K=5 and n=19–20 at 32B, the selection-evaluation separation is thin. Critical detail from R2's cross-response: BA-selected layers sit at 47–73% depth (QwQ-32B L30, R1-32B L47), while corrected (precision-optimal) layers sit at 94–98% depth (L60, L63). If the paper's central thesis is that layer selection determines conclusions, the fact that two principled selection methods choose very different layers raises the question of which result is "true." The paper claims both are significant, but this itself demands explanation.

Additional concern: Appendix S uses a 70/30 split while main results (Tables 3–4) use 60/20/20. Different splits yield non-overlapping test sets, introducing an uncontrolled variable. **Reproducing the BA-layer comparison under 60/20/20 is a reasonable and technically straightforward request.** [Both reviewers AGREE on circularity risk.]

**MF5. "All four models†" framing is misleading.**
The conclusion states "principled selection recovers significance on all four models†" but the dagger covers substantial caveats: R1-32B is position-mediated (residualized gap +1.9pp, p=0.914, NS), QwQ-32B has negative lead time and its position baseline BA (0.832) exceeds HS BA (0.796), and both 32B models have n<=20. A more honest framing: "recovers significance on both 7–8B models and shows suggestive but underpowered trends at 32B." Among all four models, only OT-7B provides clean evidence (5/5 seeds HB, no position confound, adequate n). [Both reviewers independently flagged this as critical; strongest consensus point.]

### Should-Fix (Major)

**SF1. Commitment Point annotation reliability unquantified.**
The paper inherits CP annotations from HarmThoughts without reporting inter-annotator agreement. If CP error is >=2 steps, reported lead times (+4.5 to +13 steps) partially overlap with annotation noise. QwQ-32B's lead time (-1.2 to +1.9 steps) falls entirely within noise. R1 suggests a perturbation sensitivity analysis (shift CPs by +-1/2/3 steps, measure impact on probe metrics) as a computationally cheap validation. [Both reviewers AGREE.]

**SF2. PCA capacity matching overclaim.**
PCA to 384d preserving "79–92% variance" does not guarantee preservation of discriminative information. The paper's own qualification (Section 4.3: "PCA retains directions of maximum variance...which need not align with the semantic dimensions captured by a trained text encoder") is honest, but Introduction Contribution 2 uses stronger language ("providing evidence against a pure capacity explanation") that invites over-interpretation. R1 suggests a random projection baseline: if random 384d projection also preserves HS advantage, the variance-preserving property of PCA is not the operative factor. This is cheap and informative. [Both reviewers AGREE.]

**SF3. Cumulative researcher degrees of freedom inadequately addressed.**
The paper acknowledges 2,240 configurations but only validates C-insensitivity and K pre-selection. The joint (layer, W) surface is explored for QwQ-32B only (Appendix B). R1-32B, the most problematic model, lacks this validation. At minimum, R1-32B should have a joint (layer, W) grid search for W in {1,3,5} to match QwQ-32B. [Both reviewers AGREE; R2 notes that if n is too small for basic validation, the significant results from that n are themselves suspect.]

**SF4. Abstract and Conclusion need narrative improvement.**
The Abstract lists findings sequentially without narrative arc. The Conclusion is 3 lines that compress results without synthesis. For EMNLP, these sections need to tell a story: what problem, what insight, what evidence, what implication. R1 argues the Conclusion follows standard ACL style; R2 contends it is too terse for a paper with this many nuanced findings. **Director adjudication**: the Conclusion's brevity is defensible for a standard result, but this paper's many caveats and nuances demand more synthesis. At minimum, add a sentence on scope limitations and the practical vs. methodological contribution distinction.

**SF5. Missing comparison to causal probing methods.**
The paper discusses causal interventions as future work (citing ROME) but does not compare against or discuss DAS (Distributed Alignment Search), LEACE, or inference-time intervention methods that could validate whether the probed directions are causally relevant. This is a significant gap in the experimental design given the correlational nature of linear probing.

**SF6. Control task selectivity may be inflated by position signal.**
Appendix H reports control task selectivity of 12.5–19.7pp above chance; Section 4.3 reports position accounts for 9–20pp of BA. The overlap is unexamined. R2 identifies a key missing experiment: re-running the control task on position-residualized hidden states. If selectivity drops substantially, the control task result is partially inflated by position signal rather than safety-specific content. This is computationally cheap and directly informative. [Both reviewers AGREE this is an important gap.]

### Minor

**m1.** Table 3 precision values at 39–52% FPR make the "advantage" practically meaningless for deployment. The paper should explicitly state early (Abstract or Introduction) that this is phenomenon characterization, not a detection system proposal.

**m2.** The seven negative results (Table 5) lack failure analysis beyond "did not achieve significance." Understanding why BOCPD/CUSUM failed (e.g., non-stationarity structure) would be more informative.

**m3.** Related Work paragraph on "Safety in Reasoning Models" could better position against concurrent work on reasoning trace monitoring.

**m4.** Some notation inconsistencies: W used for both window size and number of windows in different contexts.

**m5.** The Responsible NLP Checklist (Appendix A) should be verified against ARR's current May 2026 template.

**m6.** Figure placement and caption self-containedness should be checked; some table captions reference concepts not defined within the caption.

**m7.** Several em-dashes present in the text (flagged per project writing norms as AI writing markers). Replace with commas or parentheses.

---

## Reviewer Consensus (8 points)

Both reviewers independently agree on:
1. Layer selection sensitivity is a genuine, valuable methodological contribution (S1)
2. 32B sample sizes (n=19–20) critically undermine the strongest claims (MF1)
3. Statistical framework is rigorous and transparent (S2)
4. Single-dataset limitation is a significant concern (MF3)
5. Negative results documentation is valuable (S3)
6. FPR 39–52% means this is phenomenon characterization, not a detector (m1)
7. "All four models†" framing is misleading; OT-7B is the only clean evidence (MF5)
8. Control task on residualized HS is a key missing validation (SF6)

## Reviewer Divergence (5 points, with Director adjudication)

**D1. Encoder-conditional framing severity.**
- R1: REBUT (R2's W2). Layer selection and encoder quality are independent contributions; encoder-conditional result doesn't undermine layer selection finding.
- R2: Critical weakness for the paper's overall value proposition.
- **Director adjudication**: Both are partially right. The layer selection finding stands independently (R1's point), but the paper's narrative conflates the two contributions. The encoder-conditional result undermines the *practical significance* of the HS advantage claim, which is the paper's secondary contribution. Kept as Must-Fix (MF2) for the HS advantage claim; layer selection contribution is unaffected.

**D2. Abstract density.**
- R1: REBUT (R2's W6). Abstract is ~120 words, not 220; nuanced findings require numerical calibration.
- R2: Too compressed, reads as experiment log.
- **Director adjudication**: Should-Fix (SF4). The issue is narrative arc, not word count. Numbers are necessary but should serve a story, not replace one.

**D3. Conclusion adequacy.**
- R1: REBUT (R2's W7). 3 lines/60 words is standard ACL format; Discussion-Conclusion overlap is not an issue.
- R2: Too terse for a paper with many nuanced findings.
- **Director adjudication**: Should-Fix (SF4, merged). Standard ACL length is acceptable for clean results; this paper's caveats demand slightly more synthesis. One additional sentence on scope/limitations suffices.

**D4. GRU split comparison.**
- R1: 70/30 vs 60/20/20 split difference is a confound.
- R2: REBUT. Table 14 (Appendix G) already provides matched 60/20/20 comparison; GRU-single BA=0.799+-0.035 vs LR-single BA=0.803+-0.037, no significant GRU advantage.
- **Director adjudication**: R2's rebuttal is valid. The matched comparison exists in Table 14 but is insufficiently referenced in main text. Downgraded from Should-Fix to Minor recommendation: cite Table 14 more prominently in the temporal context discussion.

**D5. HB correction granularity (12-test vs 4-test).**
- R1: Suggests 4-test model-level HB as primary, since metrics share confusion matrix.
- R2: REBUT. Both corrections yield identical conclusions; reporting the more conservative 12-test version is statistically defensible.
- **Director adjudication**: R2 is correct. Reporting the stricter correction as primary is the right default. No change needed; this is a presentation preference, not an error.

---

## Questions for Authors

**Q1.** Can you report the selected layer index per fold for the 32B models? If the BA-optimal layer varies substantially across folds, the "principled layer selection" claim is weakened.

**Q2.** Can you reproduce the BA-layer comparison (Appendix S) under 60/20/20 split to match the main results? This eliminates the split-as-confound concern.

**Q3.** What happens with a leave-one-fold-out layer selection protocol where the layer is selected on K-1 folds and evaluated on the held-out fold?

**Q4.** Have you considered running the 1024d BGE-large encoder with PCA to 384d to create a more controlled comparison against MiniLM-384d?

**Q5.** Can you provide the per-fold CP annotation for a subset of traces to bound annotation noise? Even 10 traces double-annotated would help calibrate the lead time claims. Alternatively, a perturbation sensitivity analysis (shift CPs by +-1/2/3 steps) would bound the impact of annotation error.

**Q6.** For the seven negative-result methods, can you characterize the failure mode more precisely? E.g., does BOCPD fail because the HS trajectory is not piecewise-stationary, or because the change point is gradual?

**Q7.** The 85.5% oracle gap is computed on R1-8B only. Can this be extended to the other three models? If oracle gaps differ substantially by model/scale, the "passive probing captures only a fraction" conclusion needs qualification.

**Q8.** (New, from cross-response) Can you run the control task (Hewitt and Manning 2019) on position-residualized hidden states? If selectivity drops substantially, the current control task result is partially inflated by position signal.

**Q9.** (New, from cross-response) For R1-32B, can you run the joint (layer, W) grid search for W in {1,3,5} to match the QwQ-32B analysis in Appendix B?

---

## Missing References

1. **DAS / Distributed Alignment Search** (Geiger et al., 2024) — Causal probing method directly relevant to validating whether probed directions are causally active.
2. **LEACE** (Belrose et al., 2023) — Cited in Discussion but not used; should be positioned more prominently as a missing validation.
3. **Inference-time intervention** (Li et al., 2024) — Relevant to the causal intervention gap.
4. **Representation reading beyond linear probes** (Marks et al., 2024) — Context for probe methodology limitations.
5. Recent work on reasoning trace monitoring for safety (post-2025) — Related Work section may be missing concurrent work.

---

## Overall Assessment

**Score: 3.0 — Findings**

**Confidence: 4/5**

**Justification:**
The paper makes a genuine methodological contribution: demonstrating that crossing rate biases layer selection and reverses probing conclusions at scale. This insight generalizes beyond safety probing and is well-supported at 7–8B scale. The statistical framework is rigorous, the negative results are valuable, and the transparency about limitations is commendable.

However, the paper cannot support its strongest claims. The "all four models significant†" headline rests on n=19–20 traces with 2,240 hyperparameter configurations, a combination that makes overfitting the expected outcome. The encoder-conditional finding (1/4 HB against 1024d) suggests the HS advantage has a narrow practical window. Single-dataset dependence on HarmThoughts limits generalizability. Among all four models, only OT-7B provides clean evidence (5/5 seeds, no position confound, adequate n).

For Conference (4.0), the paper would need: (a) substantially larger 32B samples or a held-out validation protocol, (b) demonstration of HS advantage against a strong text encoder, and (c) at minimum a second dataset. As Findings (3.0), the methodological insight on layer selection sensitivity is a solid contribution that the community should see, despite the empirical limitations.

The path from 3.0 to 3.5 (Borderline Conference) is achievable if authors: reframe around methodology rather than empirical claims, add held-out layer selection validation, run control task on residualized HS, run R1-32B joint grid search, and temper 32B claims. The path to 4.0 requires new data which may be infeasible before deadline.

---

## Detailed Comments by Section

### Abstract
- Lists findings sequentially without narrative arc
- "All four models†" appears without adequate context for the dagger
- Missing: explicit statement that this is phenomenon characterization
- Recommendation: Lead with the layer selection insight as the contribution, not the HS advantage

### Introduction
- Structure is sound (5 paragraphs, problem to gap to insight to method to contributions)
- Contribution 1 (layer selection) is well-motivated
- Contribution 2 (encoder-conditional advantage) oversells given 1/4 HB at 1024d
- Contribution 3 (negative results) is undersold and could be more prominent

### Related Work
- Adequate coverage of safety detection, probing methodology, change-point detection
- Missing: causal probing methods (DAS, ITI), recent reasoning safety monitoring work
- Positioning against HarmThoughts (the source dataset) could be more explicit

### Method
- Clear and well-structured
- CP definition is precise
- Probe architecture description is sufficient for reproduction
- The 7-baseline negative result space is well-chosen

### Experiments
- Table 2 (layer selection) is the strongest contribution, well-presented
- Table 3 (HS vs text) needs more prominent caveats about encoder conditioning
- Table 4 (32B): QwQ-32B position baseline BA (0.832) > HS BA (0.796) should be highlighted, not buried; HS "advantage" for QwQ-32B is limited to precision/FPR and neither is significant (p=0.133, p=0.279)
- Temporal analysis (Section 5.3) is underdeveloped; GRU matched comparison (Table 14) should be cited in main text

### Discussion
- Layer selection as researcher DOF paragraph is excellent
- Encoder-conditional paragraph needs to confront the 1/4 HB result more directly
- Per-model evidence: the "distillation vs native" claim is speculative without controlled comparison

### Conclusion
- Too terse (3 lines) for a paper with this many nuanced findings
- Needs at minimum one sentence on scope limitations
- Should distinguish methodological contribution (robust) from empirical contribution (conditional)

### Limitations
- Unusually thorough and honest
- Could be better organized (group by severity)
- Some items (CP annotation uncertainty) deserve promotion to main text

### Appendix
- Comprehensive (16+ appendices)
- BA-layer comparison (Appendix S) should be reproduced under 60/20/20
- GRU matched comparison (Table 14) deserves main text citation
- The sheer volume suggests the paper may be trying to address too many questions at once

---

## Cross-Response Summary

**R1 on R2**: 4 AGREE (with nuance), 4 REBUT, 1 mixed. Key rebuts: encoder-conditional does not undermine layer selection (valid for that contribution), Abstract length is appropriate, Conclusion follows ACL norms, deployment framing already disclaimed.

**R2 on R1**: 9 AGREE, 2 REBUT. Key rebuts: GRU split already has matched comparison in Table 14 (valid, confirmed by appendix data), 12-test HB as primary is more conservative and defensible (valid). Key additions: BA-layer depth discrepancy (47–73% vs 94–98%), control task on residualized HS, QwQ-32B position > HS detail.

**Convergence**: Strong. Both reviewers independently scored 3.0. Core weaknesses (32B sample size, "all four models" framing, single dataset) are unanimous. Divergences are on framing severity, not on factual assessment. No Round 2 needed.

---

*Report generated by Review Director, Round 14. Two reviewers (R1: methods/experiments rigor, R2: novelty/completeness/framing) with full cross-sharing and convergence verification. Updated with both reviewers' complete cross-responses.*
