# Author Response Templates

Created: 2026-05-20 | Status: draft, do not commit
Fallback deadline: 2026-05-21 24:00 UTC

---

## Attack Surface 1: Single Dataset (HarmThoughts only)

### Baseline Response (no AdvBench probe results)

> Thank you for raising this important concern. We acknowledge that probe-level claims (Contribution 2) rely on a single benchmark and have stated this explicitly as our first limitation (§7).
>
> However, our primary finding (Contribution 1: metric-induced layer selection bias) rests on geometric properties of transformer representations, not on dataset-specific safety labels. We provide two forms of evidence that the geometric precondition generalizes:
>
> 1. **Cross-dataset volatility**: On AdvBench (Zou et al., 2023), R1-8B exhibits a deep/shallow cosine distance ratio of 1.67×, within the 1.4–2.7× range observed across all four models on HarmThoughts (Appendix C). This analysis requires no CP annotations.
> 2. **Random-label control**: The crossing-rate shallow preference persists in 100% of random-label permutations on QwQ-32B (Appendix K), confirming it arises from representation geometry rather than label structure.
>
> Control task selectivity (11.1–16.8pp above chance) and split-half internal validity further support genuine safety signal. We agree that cross-dataset validation of probe-level claims is needed and list this as future work.

**Word count: ~148**

### Upgraded Response (if AdvBench Phase 3-4 succeeds)

> Thank you for this concern. We have validated our findings on AdvBench (Zou et al., 2023) in addition to HarmThoughts:
>
> 1. **Layer selection bias replicates**: The CR-composite metric selects shallow layers (L{{ADVBENCH_CR_LAYER}}) while threshold-based metrics select deep layers (L{{ADVBENCH_THRESH_LAYER}}) on AdvBench, consistent with HarmThoughts.
> 2. **Geometric precondition confirmed**: The deep/shallow volatility ratio is 1.67× (within the 1.4–2.7× HarmThoughts range), requiring no CP annotations.
> 3. **HS advantage replicates**: Precision advantage of +{{ADVBENCH_PREC_DELTA}}pp (p={{ADVBENCH_PREC_P}}) at the threshold-based layer.
>
> Both contributions now have cross-dataset evidence: Contribution 1 (geometric + label-based) and Contribution 2 (precision advantage). We acknowledge that two benchmarks remain limited and that broader evaluation across attack taxonomies and multilingual settings is future work.

**Word count: ~130**

---

## Attack Surface 2: 3/4 Qwen Architecture Bias

### Response

> We appreciate this observation, which we discuss explicitly in §7 (Limitations, "Hyperparameter selection and scope"): "Three of four models share the Qwen architecture family; observed patterns may reflect Qwen-specific representation properties."
>
> We note that our study includes two distinct architecture families, not one:
>
> - **R1-8B** is based on Llama-3.1-8B (Meta), not Qwen. Its full-layer sweep (L0–L24; Table 8) confirms the same CR-composite shallow bias (L0) and threshold-based deep preference (L14), providing cross-architecture evidence for Contribution 1.
> - The **random-label control** was conducted on QwQ-32B (Qwen), and the **split-half replication** on OT-7B (also Qwen but independently trained via STILL). While these do not constitute a third architecture, they demonstrate robustness to training methodology within the same base model.
>
> We scope our claims accordingly: "primarily Qwen-based (3/4 models) with one Llama model for limited cross-architecture evidence" (Abstract). Whether the findings extend to encoder-only or non-reasoning architectures remains an open question we flag in §7.

**Word count: ~150**

---

## Attack Surface 3: 32B Statistical Power (n=19-20)

### Response

> We share this concern and have taken several steps to report 32B results responsibly:
>
> 1. **Explicit evidence gradient**: All 32B conclusions are marked with † throughout the paper and classified as "significant" (QwQ-32B) or "exploratory" (R1-32B), distinct from the "cross-validated" tier at 7–8B (§4.1).
> 2. **Power analysis disclosed**: The minimum detectable effect at 80% power is 8.6–9.5pp (Appendix S). R1-32B's selectivity (3.0pp) falls below the 5pp control task threshold, which we report as a limitation.
> 3. **Multi-seed stability**: 18/20 model-seed combinations pass full HB correction (Appendix P). R1-8B FPR is seed-fragile (3/5 HB), which we flag explicitly.
> 4. **Descriptive framing**: §4.5 states: "We report effect sizes as descriptive rather than confirmatory; LOO-CV and multi-seed analyses provide partial robustness checks but do not substitute for independent validation."
>
> The 32B results serve as initial characterization of scale-dependent patterns, not as confirmed findings. We recommend replication with n≥50 traces before drawing inferential conclusions (§4.5).

**Word count: ~150**

---

## Quick-Reference: Evidence Inventory per Attack Surface

| Attack Surface | Paper Sections | Key Evidence |
|---|---|---|
| Single dataset | §7¶1, App C, App K | Volatility 1.67×, random-label 100%, control 11.1-16.8pp |
| Qwen bias | §7¶3, Abstract, Tab 8 | R1-8B (Llama) full sweep, 2 arch families |
| 32B power | §4.1, §4.5, §7¶2, App S, App P | †markers, MDE 8.6-9.5pp, 18/20 seeds, descriptive framing |

---

## Meta-Strategy

- **Tone**: Acknowledge limitation honestly, then point to specific mitigations already in the paper. Never dismiss or deflect.
- **Structure**: "We agree → Here is what we did → Here is what remains → Future work"
- **Key phrase**: "responsible reporting" (for 32B), "geometric precondition" (for single dataset), "two architecture families" (for Qwen bias)
- **If reviewer insists on more datasets**: Offer AdvBench results if available; otherwise, frame as "the methodological contribution (layer selection bias) is validated through geometry and random-label controls, which are dataset-independent by construction"
