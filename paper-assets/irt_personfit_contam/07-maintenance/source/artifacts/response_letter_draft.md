# Author Response Letter — Round 7

## Acknowledgment

We thank both reviewers for their rigorous and constructive evaluation. The feedback on CI construction, seed reporting, and inverted-U interpretation significantly strengthened the paper. Below we address each point, referencing the specific revisions made.

---

## Must-Fix Issues

### MF-1: CI systematically underestimates uncertainty + Table 1 seed-selective reporting
**Status**: ✅ Fixed

We agree this was the most serious methodological concern. Three changes were made:

1. **Table 1 (now Table 1 in §4.1)** reports multi-seed means ± SD for all Qwen MMLU conditions where replication is available (15%/25%/50%, $n{=}3$ independent QLoRA seeds 42/123/456). The table footnote explicitly marks Llama and Mistral as single-seed with bootstrap CIs reflecting clean-seed variability only.

2. **Appendix K (§Appendix: Contamination Run Reproducibility)** provides the complete per-seed breakdown for both free-$\theta$ and fixed-$\theta$ Cohen's $d$, plus HT and accuracy $z$-score per-seed values (Tables in Appendix K). The 50% free-$\theta$ CV of 59.6% is reported and discussed in the appendix note, attributing it to seed-dependent $\theta$-shift magnitude.

3. **CI interpretation** is clarified in §3 (Effect Sizes): "We report percentile bootstrap 95% CIs (10,000 resamples) reflecting clean-seed variability only; BCa correction (Appendix) generally confirms conservative coverage; multi-seed contamination-run variance appears in Appendix K."

The previous version reported seed 42's $|d|{=}1.90$ for 50% free-$\theta$; the revised Table 1 reports the multi-seed mean $|d|{=}5.08$ ($\pm$3.02), which no longer supports the inverted-U narrative (see MF-2).

### MF-2: Inverted-U (non-monotonic dose-response) over-presented; is a $\theta$-estimation artifact
**Status**: ✅ Fixed

The revised paper explicitly repositions the inverted-U as a $\theta$-estimation artifact, not a contamination-inherent feature:

1. **§4.4**: "This non-monotonicity is a $\theta$-estimation artifact: fixed-$\theta$ analysis eliminates the inverted-U and reveals a strong positive dose-response (mean $|d|$: 5.89 at 25% vs. 12.32 at 50%, no seed-level overlap), while reducing the 50% CV to 19%."

2. **Multi-seed means** show 15%→50% are essentially flat ($5.36 \to 5.08$), confirming the inverted-U disappears at the aggregate level. The single-seed inverted-U pattern from seed 42 ($6.57 \to 8.22 \to 1.90$) is no longer presented in the main text.

3. **Introduction Finding 3** now reads: "Non-monotonic dose-response under free-$\theta$ (exploratory)... The non-monotonicity is a $\theta$-estimation artifact, not a detection boundary."

4. **Abstract** marks the finding explicitly as driven by $\theta$-shift absorption, with $\theta$-anchored analysis revealing the true monotonic positive dose-response.

### MF-3: Core novelty is primarily confirmatory; most novel finding has weakest evidence
**Status**: ✅ Fixed

Three structural changes address the novelty layering:

1. **Introduction (§1)** now explicitly separates: "Findings 1–2 are confirmatory (pre-planned 15%/50% × 3 families); Finding 3 is exploratory (5%/25% added post-hoc)."

2. **Contribution framing** is revised to: "We provide the first empirical characterization of IRT person-fit behavior for LLM contamination, quantifying theoretically predicted phenomena ($\theta$-shift absorption, detection-diagnosis tradeoff) whose magnitudes and boundary conditions are not derivable from IRT theory alone." This honestly positions the work as confirmatory quantification rather than claiming novel discovery.

3. **Abstract** presents Finding 3 with the qualifier "(exploratory)" and frames it as an artifact observation rather than a co-equal contribution.

---

## Should-Fix Issues

### SF-1: Cohen's $d$ terminology — single-observation standardized departure vs. two-sample effect size
**Status**: ✅ Fixed

§3 (Effect Sizes) now explicitly defines: "$d$ is a standardized departure rather than a two-sample effect size (Hedges' $g = J \cdot d$, $J \approx 0.914$ for $n{=}10$; Hedges, 1981)." This clarification appears at the point of definition. The paper continues to use "$d$" as notation for readability, but the methodological distinction is established upfront. No comparisons to Cohen's conventional benchmarks (0.2/0.5/0.8) appear in the paper.

### SF-2: Missing comparison with existing methods (MIA/ConStat)
**Status**: ✅ Partially addressed

Three additions provide systematic method positioning:

1. **Table 3 (§4.3)** compares $\ell_z^*$ vs. HT vs. accuracy $z$-score across all three model families, establishing the detection-diagnosis tradeoff with same-information-level comparisons.

2. **GRPO MIA experiment (§Discussion + Appendix: Post-RL)**: Min-K% AUC degrades from 0.611 (SFT) to 0.493 (post-RL, indistinguishable from chance), while $\ell_z^*$ signal persists (~3.3). This directly demonstrates a scenario where $\ell_z^*$ succeeds and MIA fails.

3. **Discussion (§5)** adds an information-requirements hierarchy paragraph: "$\ell_z^*$ sits below MIA (logits) and ConStat (multi-benchmark scores) in an information-requirements hierarchy, needing only single-benchmark binary patterns and an external item bank---suited to retrospective audits where logits are unavailable."

We do not provide a head-to-head AUROC comparison with ConStat/MIA because they operate at different information levels (logits vs. binary patterns), making controlled comparison methodologically problematic. The paper's positioning as characterization rather than detection tool further reduces the need for such comparison.

### SF-3: ARC-Challenge statistical power insufficient; cross-benchmark generalizability evidence thin
**Status**: ✅ Acknowledged as limitation

The simulation power analysis (Appendix A) transparently reports ARC-C power of 0.087 at 15% contamination and 0.285 at 50% — far below the 0.80 standard. This is now explicitly noted in the Limitations section: "the framework depends on pre-calibrated 4PL item parameters from PSN-IRT, whose calibration sample may include contaminated models." The low power is a direct consequence of the 295-item count, consistent with the $\sqrt{n}$ scaling established by the power function ($R^2{=}0.957$). We include ARC-C precisely to demonstrate this boundary condition rather than to claim strong detection on small benchmarks.

### SF-4: Incomplete experimental matrix
**Status**: ✅ Acknowledged as limitation

Two locations address this:

1. **§3.3 (Method)**: "Mistral was not tested at 5% or 25% due to computational constraints" and "ARC-Challenge experiments were conducted on Qwen only, as the primary evaluation of cross-benchmark generalizability; extending to additional families was constrained by computational budget."

2. **Limitations section**: "Our controlled experiments cover three 7–8B model families with QLoRA fine-tuning; generalization to larger scales, mixture-of-experts architectures, full-parameter fine-tuning, and pretraining-stage contamination remains untested. Most contamination conditions use a single training run... the post-RL characterization is $N{=}1$."

We acknowledge that the term "systematic" may overstate coverage and have revised phrasing to avoid this implication where applicable.

### SF-5: PSN-IRT parameter circularity undiscussed
**Status**: ✅ Fixed

A dedicated paragraph in the Discussion (§5, "Scope and calibration") now addresses this:

"PSN-IRT provides pre-calibrated 4PL parameters, but classical calibration fails on contaminated data ($r_a{=}0.127$; Appendix); the calibration sample (13,000+ models) may itself include contaminated ones, though individual contamination effects are diluted across models. The robustness analysis (Appendix) provides partial reassurance ($\pm$10% noise tolerance)."

We acknowledge that Appendix F's random-noise robustness does not directly address systematic bias from contaminated calibration data. The dilution argument (each model contributes a small fraction to item parameter estimates) provides partial mitigation, but we cannot rule out systematic effects, particularly for heavily contaminated benchmarks.

### SF-6: Mistral fixed-$\theta$ missing seeds 4–7 unexplained
**Status**: ✅ Explained

Table 2 footnote (§4.2) states: "Fixed-$\theta$: 6 seeds (4–7 response vectors not retained in pipeline); free-$\theta$ uses all 10." The cause is a pipeline engineering issue: the intermediate response vectors required for fixed-$\theta$ recomputation were not saved for seeds 4–7 during the initial experimental run. The raw evaluation outputs (accuracy, free-$\theta$ $\ell_z^*$) were retained, so free-$\theta$ analysis uses all 10 seeds. This is not related to model behavior or convergence failure — it is a data management oversight. We will clarify this distinction in the footnote to preclude selection-bias concerns.

### SF-7: Contamination data mixing definition unclear
**Status**: ✅ Fixed

§3.3 now specifies: "at $X\%$ contamination, $X\%$ of SFT training examples are benchmark items (questions paired with gold answers in the standard evaluation format), with the remainder drawn from a general instruction-following dataset." This defines the mixing ratio as the proportion of training examples that are benchmark items (not the proportion of benchmark items included).

---

## Questions

### Q1: Table 1 Qwen 50% — seed 42 or aggregate? Why that specific seed?
**Answer**: The revised Table 1 reports multi-seed means ($n{=}3$, seeds 42/123/456) for all Qwen conditions where replication is available. The previous version reported seed 42 because the initial experiment used a single seed; the replication study (seeds 123, 456) was conducted subsequently. We acknowledge that reporting the single-seed result (which happened to be the most favorable for the inverted-U narrative) without the replication context was a presentation error. This has been corrected.

### Q2: Would Llama/Mistral show lower CV than Qwen's 59.6%? Is "All CIs exclude zero" too strong for these families?
**Answer**: We cannot empirically answer whether Llama/Mistral CV would be lower, as only $n{=}1$ contaminated runs are available for these families. However, the mechanism driving Qwen's high CV is $\theta$-shift absorption, which is proportional to $\Delta\theta$. Llama's much smaller $\theta$-shift ($\Delta\theta{=}0.09$ vs. Qwen's 0.47) suggests lower seed dependence. "All CIs exclude zero" refers to the bootstrap CIs constructed from $n{=}10$ clean seeds, conditional on the single contaminated observation — the statement is technically accurate but, as the reviewers correctly note, captures only one source of uncertainty. The revised text (§3 (Effect Sizes)) now makes this conditioning explicit.

### Q3: Cross-benchmark comparison scheme — any experimental validation?
**Answer**: No. The cross-benchmark comparison described in §5 is a proposed deployment framework, not an experimentally validated method. The revised Discussion marks this as "an untested deployment suggestion" to avoid implying empirical support. Validation would require models with known single-benchmark contamination evaluated across multiple benchmarks, which our current experimental design does not provide.

### Q4: Mistral seeds 4–7 unavailable in fixed-$\theta$ — specific cause?
**Answer**: See SF-6 above. The intermediate response vectors (item-level binary patterns needed for fixed-$\theta$ recomputation) were not retained in the processing pipeline for seeds 4–7. This is a data management oversight, not a convergence or behavioral issue. All 10 seeds are available for free-$\theta$ analysis, which uses only the final $\ell_z^*$ values.

### Q5: "15% contamination" — precise operational definition?
**Answer**: See SF-7 above. At $X\%$ contamination, $X\%$ of the total SFT training examples are benchmark items (question + gold answer in evaluation format). For example, at 15% contamination with MMLU, approximately 15% of the training batch consists of MMLU items and 85% consists of general instruction-following data. The total number of training examples varies by contamination level to maintain a fixed number of non-contaminated examples across conditions.

### Q6: PSN-IRT calibration — does it include contaminated models? Circularity?
**Answer**: PSN-IRT calibrates item parameters from 13,000+ models on the Open LLM Leaderboard. We cannot guarantee that none are contaminated. However, two factors mitigate circularity: (1) each model contributes a small fraction ($<0.01\%$) to item parameter estimates, diluting individual contamination effects; (2) contamination would primarily affect difficulty estimates (making contaminated items appear easier), not discrimination or asymptote parameters. The robustness analysis (Appendix F, $\pm$10% noise on all four parameters) shows detection is robust under free-$\theta$ ($<18\%$ bias at 15% contamination) and highly robust under fixed-$\theta$ ($<4\%$ bias). We acknowledge this is partial reassurance, as systematic bias differs from random noise. See the added Discussion paragraph (§5).

### Q7: Table 8 AUROC = 0.63 — near random or practically useful?
**Answer**: 0.63 is weak and near the lower bound of practical utility. The item-level AUROC (Appendix: Item-Level Detection Results) confirms that contamination is diffuse across the response pattern: no single item reliably distinguishes seen from unseen. This is why $\ell_z^*$ operates at the model level (aggregating across all items) rather than the item level. The value 0.63 represents the best item-level method (RF cross-model); the $\ell_z^*$ itemwise method achieves only 0.53. This result reinforces that the framework is a characterization tool for model-level aberrance, not an item-level detection method.

### Q8: Is Finding 3 a QLoRA rank=16 artifact?
**Answer**: We cannot rule this out. The non-monotonic dose-response under free-$\theta$ is now identified as a $\theta$-estimation artifact (MF-2), which partially subsumes the QLoRA-specificity concern: the artifact arises from MLE $\theta$ estimation dynamics rather than the fine-tuning method per se. However, the magnitude of $\theta$-shift may depend on QLoRA's capacity constraints (rank=16 limits the expressiveness of contamination absorption). Testing with full-parameter fine-tuning or different LoRA ranks would be needed to isolate this factor, which we list as future work.

### Q9: Post-RL GRPO 1,500 steps — how chosen? Would longer training change results?
**Answer**: 1,500 steps was chosen as the point where the accuracy gap between seen and unseen items had largely converged ($11.4\text{pp} \to 2.1\text{pp}$), indicating that RL had substantially reshaped the model's response distribution. We evaluated at three checkpoints (500/1000/1500 steps) to observe the trajectory. Min-K% AUC plateaued at 0.493 from step 500 onward, suggesting further training would not change the MIA result. Whether $\ell_z^*$'s persistent signal (~3.3) would eventually decay under longer RL training is an open question — our $N{=}1$ pilot cannot address this, and we explicitly note this limitation.

---

## Minor Issues

### m1: Simulation power analysis correspondence to real experiments unclear
**Acknowledged.** The simulation assumes 4PL correctness, while 57/60 real cells show $|\ell_z^*| > 1.96$. The simulation validates the $\Delta\ell_z^*$ design under controlled conditions; the real-data analysis confirms that $\Delta\ell_z^*$ functions despite systematic IRT violations because the matched-difference design cancels shared misfit. We add a sentence in Appendix A clarifying this distinction.

### m2: Figure 2 heatmap annotation font size; grayscale distinguishability
**Acknowledged.** We will increase the annotation font size and improve the gray/light-blue contrast for grayscale printing. The numeric values are also available in Table 1.

### m3: Pages 3–4 two consecutive pages of pure text; framework diagram recommended
**Acknowledged.** We will consider adding a framework overview figure if space permits within the 8-page limit. The current layout prioritizes tables and result figures.

### m4: Missing recent contamination detection survey citations
**Acknowledged.** We thank the reviewer for pointing to these surveys. Due to the 8-page limit, we were unable to incorporate them in the current revision but plan to add them in the camera-ready version to provide broader context for the detection landscape.

### m5: $\Delta\ell_z^*$ vs. Cohen's $d$ of $\Delta\ell_z^*$ notation inconsistency
**Acknowledged.** We will audit all instances to ensure consistent notation: $\Delta\ell_z^*$ for the raw difference and $d$ for the standardized effect size.

### m6: Multiple comparison correction
**Acknowledged.** We agree with R2's argument that multiple comparison correction is less critical in controlled experiments with known ground truth, where the primary inferential target is effect size magnitude rather than $p$-value significance. However, we acknowledge that selective reporting across the 10 model-benchmark-contamination combinations could inflate apparent success rates. The multi-seed aggregation (MF-1 fix) partially addresses this by reducing seed-selection degrees of freedom. We will add a brief discussion of this consideration.

---

## Summary of Changes

The revision addresses all three must-fix issues: (1) Table 1 now reports multi-seed means ± SD for Qwen, with explicit footnotes distinguishing single-seed (Llama/Mistral) from replicated conditions, and CIs are qualified as reflecting clean-seed variability only; (2) the inverted-U is repositioned as a $\theta$-estimation artifact throughout, with multi-seed means replacing single-seed values as the primary evidence; (3) contributions are layered as confirmatory quantification (Findings 1–2) vs. exploratory observation (Finding 3). Should-fix items are addressed through terminology clarification (standardized departure + Hedges' $g$), systematic method comparison (Table 3 + GRPO MIA + information hierarchy), transparent reporting of ARC-C low power and incomplete experimental matrix in Limitations, a new Discussion paragraph on PSN-IRT circularity, clarification of Mistral seeds 4–7 as a pipeline data-retention issue, and precise operational definition of contamination mixing ratios. Minor issues will be addressed in the camera-ready revision.
