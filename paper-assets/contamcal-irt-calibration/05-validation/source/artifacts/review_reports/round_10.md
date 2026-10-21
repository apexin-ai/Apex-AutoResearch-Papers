---
round: 10
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-23T08:03:34.794123+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 12

**Paper**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families
**Venue**: EMNLP 2026 (ARR, Long Paper)
**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性/呈现)
**Cross-sharing**: Complete (R1↔R2, all points addressed)

---

## Summary

This paper introduces ContamCal, a two-stage pipeline combining Reciprocal Rank Fusion (RRF) of three contamination detection signals with a contamination-augmented 2PL IRT model (2PL+γ). Through controlled SFT injection at 5 dosage levels across 6 models from 5 families, the authors identify 4 dose-response patterns (Immune, Collapse, V-recovery, Benefit) and propose that model family characteristics—not just baseline ability—modulate contamination vulnerability. The paper includes a memorization test via Difference-in-Differences (DiD), cross-benchmark transfer analysis, and out-of-sample validation with LLaMA-3.1.

---

## Strengths

1. **Well-motivated research question**: The shift from binary contamination detection to dose-response profiling is a genuine conceptual advance. Framing contamination as a continuous, model-dependent phenomenon is more realistic than prior binary approaches.

2. **Rigorous experimental infrastructure**: Controlled SFT injection with 5 dosage levels, 3 seeds per configuration, and the AUGMENT protocol represents substantial engineering effort. The factorial design (6 models × 5 doses × 3 seeds = 90 fine-tuning runs) enables systematic analysis.

3. **Multi-method triangulation**: Combining IRT-based calibration, DiD memorization testing, signal fusion, and cross-benchmark transfer analysis provides multiple lenses on the same phenomenon. The DiD design for ruling out item-level memorization is methodologically sound.

4. **Transparent limitations**: The paper openly acknowledges single-family patterns, seed sensitivity, and ecological validity gaps. The limitations section is thorough and honest.

5. **Practical tooling contribution**: ContamCal as a diagnostic tool—if the calibration issues are resolved—addresses a real need in the evaluation ecosystem. The profile classification algorithm (Algorithm 1) is reproducible.

6. **Strong appendix**: 12 pages of supplementary material covering identifiability simulations, prior sensitivity, DGP robustness, and classification sensitivity analysis demonstrate thorough due diligence.

---

## Weaknesses

### Must-Fix (Critical)

**[W1] Taxonomy overfitting: 4 categories from 6 models, with 2 categories single-family**
Collapse and V-recovery are observed only in Qwen2.5 (7B and 14B respectively). Proposing a 4-category taxonomy where 50% of categories rest on a single model family is a serious overfitting risk. The paper frames these as general contamination response patterns, but the evidence supports only 2 replicable patterns (Immune, Benefit). The taxonomy should be restructured: present Immune and Benefit as established patterns, and Collapse/V-recovery as Qwen2.5-specific observations requiring independent replication.
*Consensus: Both reviewers agree this is critical. R2 additionally notes the taxonomy is presented as the paper's primary contribution, making this particularly damaging.*

**[W2] "65–70% vulnerability band" lacks statistical support**
The claimed vulnerability band is defined by exactly 2 data points from the same family (Qwen2.5-7B at 65.3% and Qwen2.5-14B at 70.4%). LLaMA-3.1 at 67.6% (Immune) directly contradicts the hypothesis. The paper acknowledges this but continues to use the band as a framing device. This claim must either be removed or explicitly downgraded to a preliminary observation with the counter-evidence prominently noted.
*Consensus: Both reviewers agree. R1 calls it "circular reasoning," R2 notes the LLaMA counter-evidence is buried rather than foregrounded.*

**[W3] ContamCal calibration does not improve over raw accuracy**
Table 3 shows Raw Accuracy MAE = 0.006 vs. ContamCal MAE = 0.009. The proposed method is strictly worse on the paper's own metric. The paper attempts to justify this via "contamination-aware" calibration, but never demonstrates a scenario where ContamCal provides actionable value over simply using raw accuracy. This undermines the practical motivation for the entire pipeline.
*Consensus: Both reviewers agree this is critical. R1 notes the comparison is "devastating." R2 emphasizes that the paper does not adequately address this result.*

**[W4] Signal quality concerns in RRF fusion**
S2 (Min-K%++) shows directional reversal at 0.5B parameters, and S4 (Self-Critique) achieves near-random performance in multiple configurations. Including near-random or adversarial signals in RRF fusion is empirically harmful. The paper acknowledges signal limitations but does not test RRF with signal exclusion (e.g., S1-only vs. S1+S2+S4). Appendix E.5 shows RRF ablation but does not address the core concern of whether degraded signals actively harm exposure ranking.
*Consensus: Both reviewers agree. R1 wants formal signal quality gating; R2 wants ablation showing RRF benefit over best single signal.*

**[W5] 300/14,042 item subset introduces selection bias**
IRT fitting uses only the 300 highest-exposure-variance items (2.1% of MMLU). This biases the analysis toward items where contamination signals are most divergent—precisely the items most likely to show contamination effects. The paper does not validate that conclusions generalize to the full item pool. A sensitivity analysis varying the subset size (e.g., top-100, top-500, top-1000) is necessary.
*Consensus: Both reviewers agree. R2 notes this is a "self-fulfilling prophecy" risk.*

**[W6] Seed insufficiency and statistical power**
With n=3 seeds, strict sign-consistency holds for only 3/6 models across all dosages. AICc analysis (Appendix E.18) shows Gemma-2 and OLMo-2 are statistically indistinguishable from a null (flat) model, yet both are classified as "Benefit." The paper's seed-consistency analysis in §5.2 reports only the favorable metric (direction reproducibility) while omitting magnitude instability.
*Consensus: Both reviewers agree. R1 notes OLMo-2's CI crossing zero makes its classification "borderline at best." R2 emphasizes AICc evidence against Benefit classification for 2/3 Benefit families.*

### Should-Fix

**[W7] Volume control covers only Falcon3**
The volume-matched control (§5.4, Appendix E.16) is conducted only for Falcon3-7B. Without replication in other families, the 55%/45% contamination-vs-volume decomposition cannot be generalized. At minimum, one additional family should be tested.

**[W8] Ecological validity of SFT injection**
LoRA-based SFT injection differs fundamentally from pretraining-stage contamination via web crawl. The paper acknowledges this in limitations but does not sufficiently qualify claims throughout the main text. Statements like "contamination does not uniformly inflate scores" should be qualified as "SFT-injected contamination..."

**[W9] Abstract numeric density**
The abstract contains 25+ numerical values, making it nearly unreadable. Key narrative claims are buried under statistics. Reduce to 8-10 essential numbers and move details to the introduction.

**[W10] Cross-seed reporting is selectively optimistic**
§5.2 emphasizes direction reproducibility but underplays magnitude variance. OLMo-2's cross-seed CI crossing zero should be mentioned in the main text, not just limitations.

**[W11] γ_d placement in IRT model lacks theoretical justification**
The domain-level contamination shift γ_d is added as an additive term to item difficulty. No theoretical argument or empirical comparison justifies this placement over alternatives (e.g., multiplicative, discrimination-modifying). The 2PL+γ model is presented as if the additive form is self-evident.

**[W12] Algorithm 1 thresholds (τ=2pp, σ=5pp) lack principled basis**
The classification thresholds appear arbitrary. Appendix E.18 provides sensitivity analysis, but the main text does not explain how these values were chosen or what happens at boundary cases.

**[W13] "Contamination" vs. "additional training" conceptual tension**
The AUGMENT protocol adds benchmark items as additional training data. The paper does not clearly distinguish the contamination effect from the general effect of additional supervised training on benchmark-relevant content. The volume control partially addresses this but only for one family.

### Minor

**[M1] Table 1 readability**: Pattern taxonomy table would benefit from visual indicators (color/icons) to distinguish replication status (multi-family vs. single-family).

**[M2] Figure 1 axis labels**: Y-axis "Δ Accuracy (pp)" could be confused with percentage points vs. absolute percentage. Clarify units.

**[M3] Related work positioning**: The distinction from Han et al. (2026) concurrent work could be sharper—both do controlled injection, but the dose-response profiling angle is undersold.

**[M4] Notation inconsistency**: γ is used for both item-level (Eq. 2) and domain-level (§5.5) contamination shifts without clear subscript disambiguation in early sections.

**[M5] "Not All Models Are Inflated" title**: While catchy, the title implies the paper shows some models are inflated and others not. The actual finding is more nuanced—even "Benefit" models show modest effects (2-5pp), and the title oversells the contrast.

---

## Reviewer Consensus

Both reviewers converge on the following key judgments:

1. The research question (dose-response profiling) is valuable and timely — **agreed**
2. The experimental infrastructure is impressive — **agreed**
3. The taxonomy is overfit to the data (4 categories, 2 single-family) — **agreed, critical**
4. The vulnerability band claim is unsupported — **agreed, critical**
5. ContamCal underperforming raw accuracy is a fundamental problem — **agreed, critical**
6. Signal quality in RRF needs ablation/gating — **agreed, critical**
7. 300-item subset risks selection bias — **agreed, critical**
8. n=3 seeds is insufficient for the claims made — **agreed, critical**
9. Volume control needs replication beyond Falcon3 — **agreed, should-fix**
10. Abstract is overloaded with numbers — **agreed, should-fix**

## Reviewer Divergence

Three minor divergences recorded, none blocking consensus:

1. **Benchmark diversity**: R1 considers 3 benchmarks (MMLU, ARC, GSM8K) sufficient for the paper's scope; R2 argues additional benchmarks (e.g., TruthfulQA, HellaSwag) are needed for generalizability. *Resolution*: Noted as a limitation, not a must-fix.

2. **DiD parallel trends assumption**: R2 initially flagged this as a concern; upon cross-response, acknowledged that the controlled experimental design largely mitigates it. *Resolution*: Resolved in favor of the paper.

3. **LoRA rank uniformity**: R2 initially flagged uniform r=16 as problematic; upon cross-response, acknowledged that the Phi-4/Qwen-14B same-scale comparison partially addresses the concern. *Resolution*: Downgraded from should-fix to minor consideration.

---

## Questions for Authors

1. Can you provide ContamCal calibration results on the full 14,042 MMLU items (not just the 300 highest-variance subset)? If ContamCal still underperforms raw accuracy on the full set, what is the practical use case?

2. What happens to the RRF exposure ranking if S2 and S4 are excluded (S1-only)? Does downstream IRT calibration improve?

3. For the 2 families classified as Benefit but indistinguishable from null by AICc (Gemma-2, OLMo-2): at what seed count would you expect the effect to reach significance? Is the effect size meaningful even if real?

4. Can you replicate the volume control experiment for at least one additional family (ideally one showing a different pattern, e.g., Qwen2.5)?

5. What is the theoretical motivation for additive γ in the IRT model? Have you compared against multiplicative or discrimination-modifying alternatives?

6. The LLaMA-3.1 out-of-sample result contradicts the vulnerability band hypothesis. How do you reconcile this? Is the band hypothesis still tenable?

---

## Missing References

Both reviewers identified gaps in the related work:

- **Oren et al. (2024)** — "Proving Test Set Contamination in Black Box Language Models" (ICLR 2024). Directly relevant statistical framework for contamination testing, not cited.
- **Deng et al. (2024)** — "Investigating Data Contamination in Modern Benchmarks for Large Language Models" (NAACL 2024). Benchmark-contamination measurement at scale, relevant to experimental design choices.
- **Yang et al. (2023)** — "Rethinking Benchmark and Contamination for Language Models with Rephrased Samples." Rephrasing-based contamination detection, relevant to signal design discussion.
- **Gu et al. (2024)** — "OLMES: A Standard for Language Model Evaluations" or similar standardized evaluation frameworks relevant to the protocol-dependency discussion.

---

## External Review

**Status**: Not requested (project configuration: external review not enabled).

---

## Visual Layout Check

**Status**: Complete
- **Critical issues**: 0
- **Warnings**: 3
  - Figure 3 heatmap: annotation text potentially too small for print
  - Figure 6 multi-panel: text at readability limit
  - Table 4 footnote: small font size
- **Info**: 22 items (minor spacing/layout observations)

*No visual issues affecting acceptance decision. Warnings are cosmetic and can be addressed in camera-ready.*

---

## Overall Assessment

**Score: 3.0 — Findings**

The paper addresses a timely and well-motivated research question: moving from binary contamination detection to dose-response profiling. The experimental infrastructure (90 fine-tuning runs, controlled injection, multi-signal fusion) represents substantial effort. However, six critical issues prevent a Conference-level recommendation:

1. The 4-category taxonomy is overfit—2 of 4 patterns are single-family (Qwen2.5), making the taxonomy more of an observation catalog than a generalizable framework.
2. The "vulnerability band" claim is statistically unsupported and contradicted by the out-of-sample validation.
3. The proposed calibration method (ContamCal) underperforms raw accuracy on the paper's own evaluation metric, undermining the practical contribution.
4. Signal quality concerns in RRF (near-random S2/S4) are unaddressed by ablation.
5. The 300-item subset selection introduces circularity risk.
6. Statistical power (n=3 seeds) is insufficient for the classification claims, with 2/3 "Benefit" families indistinguishable from null by AICc.

The dose-response profiling concept and the experimental methodology are publishable contributions, but the overclaimed taxonomy and calibration shortfall need significant revision. The paper would benefit from: (a) restructuring the taxonomy to separate replicated from single-family patterns, (b) either demonstrating ContamCal's value or reframing the contribution, and (c) strengthening statistical support with additional seeds or more conservative claims.

Suitable for Findings with major revisions addressing W1-W3 at minimum.

---

## Detailed Comments

### For W1 (Taxonomy Overfitting)
Suggested restructuring: Present a 2+2 framework — 2 replicated patterns (Immune: Phi-4 + LLaMA-3.1; Benefit: OLMo-2, Falcon3, Gemma-2) as primary findings, and 2 Qwen2.5-specific patterns (Collapse, V-recovery) as secondary observations pending replication. This preserves the empirical observations while avoiding overclaiming.

### For W3 (Calibration)
Consider reframing ContamCal's contribution from "better calibration" to "contamination-aware diagnostics"—i.e., the value is in identifying which items/domains are affected, not in producing a better aggregate score. If this reframing is adopted, Table 3's MAE comparison should be contextualized rather than presented as a primary result.

### For W6 (Seeds)
If additional seeds are infeasible, the minimum fix is: (a) report AICc model comparison results in the main text, (b) reclassify Gemma-2 and OLMo-2 as "Possible Benefit (not significantly different from null)" or similar hedged language, (c) adjust all claims about "3 independent families showing Benefit" accordingly.

### For W9 (Abstract)
Suggested reduction: Keep model count (6), family count (5), dosage levels (5), number of patterns found, the key negative result (ContamCal vs. raw), and the OOS validation result. Remove individual percentage points, CI bounds, and domain-level statistics from the abstract.

---

*Report synthesized from 2 independent reviews + cross-sharing round. Consensus reached on all critical issues. No Round 2 required.*