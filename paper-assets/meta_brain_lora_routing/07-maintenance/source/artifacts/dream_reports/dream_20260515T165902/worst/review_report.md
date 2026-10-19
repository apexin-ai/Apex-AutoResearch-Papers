---
dream_id: dream_20260515T165902
tier: worst
overall_score: 5 — Marginally below acceptance threshold
timestamp: 2026-05-15T18:31:37.772083+00:00
---

# Dream Review Report — CoRL 2026 Submission

**Paper:** "VLA Internals Already Know What Went Wrong: Diagnostic Probing and the Limits of Perturbation-Routed LoRA Correction"

**Venue:** CoRL 2026 (acceptance rate ~30%, scale 1–10)
**Review mode:** full (2 Reviewers, complete roundtable)

---

## Roundtable Process

- **R1** (Methods + Experiments): Independent review → Overall **5/10**
- **R2** (Novelty + Related Work): Independent review → Overall **4/10**
- **Step 2 (Cross-sharing):** R1 flagged training data asymmetry confound and missing episode counts that R2 had not noticed; R2 flagged the thin bibliography (10 refs) and predictability of the negative result from MoE first principles that R1 underweighted. Both recognized new issues from the other's review.
- **Step 3 (Convergence):** Consensus on Soundness 3/4, Contribution 2/4. Remaining disagreement on overall score (5 vs 4) resolved to **5** — marginally below threshold — because R1's point that the experimental design is exemplary (correct critical controls, statistical rigor) merits credit even though the contribution is modest. R2 accepted this but maintained that the paper's positioning gaps keep it below the acceptance line.

---

## Consolidated Scores

| Dimension | Score | Notes |
|-----------|-------|-------|
| Soundness | 3/4 (Good) | Methodology correct, statistical testing thorough, ablation design exemplary. Deductions for uncontrolled training data confound and missing episode counts. |
| Presentation | 2/4 (Fair) | Paper is data-rich (16 tables) and logically structured, but bibliography is severely thin (10 refs), no figures in submission, and the overall metric is biased toward visual perturbations without acknowledgment. |
| Contribution | 2/4 (Fair) | Diagnostic finding is novel but narrow; negative result is honest but insufficiently investigated; oracle gap characterization is thin as standalone contribution. |
| Overall | **5/10** | Marginally below acceptance threshold |
| Confidence | 4/5 | Both reviewers report high confidence |

---

## Paper Summary

The paper investigates whether VLA internal representations encode perturbation type (visual/spatial/physical) and whether this signal can drive targeted LoRA correction. Two findings and one negative result are reported: (1) a linear probe achieves near-perfect perturbation-type classification (F1=0.993 on pi0, 0.952 on OpenVLA) with a consistent depth ordering; (2) LoRA adaptation of any form improves robustness over frozen baselines (+9.7 to +10.4 pp); (3) perturbation-type routing does NOT outperform parameter-matched universal LoRA (64.0% vs 63.3%, p=0.42). An oracle gap of 5.9pp is framed as an open problem.

---

## Consolidated Strengths

**S1. Exemplary ablation design with correct critical controls (R1).** The six-point ablation ladder (Frozen → r16 → Random → r48 → Meta-Brain → Oracle) isolates each factor systematically. The rank-48 parameter-matched control is the exact right existential test, and the random routing baseline tests the ensemble alternative hypothesis. Many papers in this space omit one or both.

**S2. Statistical rigor and transparency (R1, R2).** Five-seed evaluation with paired t-tests, exact p-values reported for all comparisons including non-significant results. The paper does not hide unfavorable results behind selective reporting. This is above the CoRL average.

**S3. Honest framing of the negative result (R1, R2).** The paper correctly identifies that routing does not outperform parameter-matched universal adaptation and presents this transparently. This intellectual honesty, including the oracle gap characterization, is valuable for the community.

**S4. Diagnostic probing finding has genuine novelty (R2).** Extending from perturbation presence detection (SAFE) to fine-grained type classification at single-layer, single-step granularity is a meaningful step. The depth ordering (V→early, S→mid, P→late) is interpretable and could inform future VLA architecture design.

**S5. Cross-backbone replication (R1, R2).** Phase 0 replicates on OpenVLA (F1=0.952, best layer at ~1/3 depth). The routing failure also replicates (+1.6pp, n.s.), confirming the findings are not architecture-specific.

**S6. Comprehensive experiment coverage (R1).** 14 experiments spanning all critical ablations. All experiments from the design document are accounted for, leaving few obvious stones unturned.

---

## Consolidated Weaknesses

**W1. (Major — R1, R2) Root cause of routing failure insufficiently investigated.** The 4.7pp cross-type drop is the root cause of the negative result, yet the paper treats it as an observation. Missing: (a) cosine similarity / subspace overlap analysis between expert weight matrices; (b) at least one alternative expert training strategy (contrastive, orthogonality-regularized). Without this, the negative result could be an artifact of standard SFT rather than a fundamental limitation. R2 adds that this failure is arguably predictable from MoE first principles — when expert capacity is low and perturbation types share representational overlap, routing fragments capacity without benefit.

**W2. (Major — R1) Training data asymmetry is an uncontrolled confound.** LoRA-V trains on 4 visual subtypes with online augmentation; LoRA-S and LoRA-P each train on 1 subtype with oracle-collected demos. The V > S > P performance gradient could partly reflect data diversity rather than intrinsic difficulty. No data-volume-matched ablation is provided.

**W3. (Major — R2) Severely underdeveloped related work — only 10 references.** For a CoRL submission, this is far below the norm. Major gaps: no foundational MoE citations (Shazeer et al., Fedus et al.), no LoRA composition literature (LoRAHub, AdaLoRA, DoRA), no representation probing methodology references from NLP (Belinkov & Glass, Hewitt & Manning), no contextualization of the depth ordering against known layer-wise structure in vision-language models.

**W4. (Major — R2) Simulation-only evaluation.** All results are in the LIBERO simulator. CoRL increasingly values real-robot validation. The diagnostic finding would be substantially more impactful if demonstrated on physical robot data with naturalistic perturbations rather than synthetic injections.

**W5. (Major — R2) Positioning relative to VLA-GSE is insufficient.** VLA-GSE achieves 81.2% on LIBERO-Plus (different backbone) via MoE routing. The paper acknowledges this but does not adequately address the 17pp gap. Either run on a comparable backbone or provide a principled argument for backbone vs. method attribution.

**W6. (Moderate — R1) Rank sweep stops short of being conclusive.** The paper observes a "weak upward trend" in routing benefit (1.0→2.0pp at r=16→64) but stops at r=64. A single point at r=128 or r=256 would test whether expert specialization emerges at higher capacity. The paper frames this as an open problem but had the resources to partially answer it.

**W7. (Moderate — R1, R2) Clean LIBERO degradation (-4.2pp, p=0.002) is underexplored.** The paper identifies that the router misclassifies clean inputs but does not test the obvious fix: adding a 4th "clean" class to the router. Given Phase 0's near-perfect accuracy, this should be straightforward and would significantly strengthen the practical contribution.

**W8. (Moderate — R1) Missing critical experimental details.** Episode counts per perturbation type per seed are never stated. If each seed evaluates ~50 episodes per condition, the success rate resolution is 2pp — meaning the 0.7pp Meta-Brain vs r48 gap is below measurement resolution. Total inference latency (3 LoRA forward passes + router + merge vs single LoRA) is also unreported.

**W9. (Moderate — R1) Overall metric is biased toward visual perturbations.** 4 of 6 subtypes are visual. The headline 64.0% is upward-biased by visual gains. A category-balanced average should be reported alongside.

**W10. (Moderate — R2) Diagnostic finding is narrow in practical impact.** The one attempted downstream use case (routing) fails. Without a successful application, the finding remains an observation without demonstrated utility.

---

## Key Questions for Authors

1. **Expert similarity analysis:** Have you measured cosine similarity or subspace overlap between the three LoRA expert weight matrices? This would definitively explain (or refute) the interchangeability hypothesis.

2. **Alternative expert training:** Did you attempt any diversity-encouraging training (contrastive loss, orthogonality regularization)? If not, can you comment on whether the negative result is specific to standard SFT?

3. **Training data volumes/balance:** How many demonstrations per perturbation type? How was the 4-subtype vs 1-subtype data asymmetry handled?

4. **Episode counts:** How many evaluation episodes per perturbation type per seed? What is the effective success rate resolution?

5. **4-class router:** Have you tested adding a "clean/nominal" class to mitigate the -4.2pp clean degradation?

6. **Higher-rank experts:** Why not test r=128+? The oracle gap and rank-sweep trend make this the single most informative missing experiment.

7. **Hard routing with PAR:** Have you tested argmax routing (hard selection using PAR's classifications) to disambiguate whether the oracle gap is due to soft-vs-hard structure or expert quality?

8. **VLA-GSE comparison:** Can you run diagnostic probing on VLA-GSE or a comparable backbone to contextualize the 17pp performance gap?

---

## Experiment Coverage Assessment

The paper covers all experiments from the design document (14 experiments total). Coverage is comprehensive. However, several experiments that would significantly strengthen the paper are absent:

- Expert weight similarity analysis (low-cost, high-diagnostic-value)
- Alternative expert training strategies (at least one)
- Higher-rank sweep (r=128+)
- 4-class router with clean category
- Hard routing with PAR classifications (argmax)
- Compound perturbation evaluation

---

## Verdict & Recommendation

**Overall: 5/10 — Marginally below acceptance threshold**

The paper presents a well-executed empirical study with exemplary ablation design and refreshingly honest treatment of a negative result. The experimental methodology is sound and the statistical practices are above average.

However, the paper falls below the CoRL acceptance bar for several reasons:

1. **Contribution depth:** The diagnostic finding (Phase 0) is novel but narrow — it extends SAFE from presence to type detection but does not demonstrate downstream utility. The negative routing result is valuable but insufficiently investigated — the paper identifies that experts learn interchangeable corrections but does not probe why (expert weight analysis) or test whether alternative training could change the outcome.

2. **Positioning gaps:** The bibliography (10 references) is severely inadequate for a top venue, leaving the work poorly contextualized against MoE, LoRA composition, and probing literatures. The VLA-GSE comparison (81.2% vs 64.0%) is inadequately addressed.

3. **Practical impact:** CoRL values methods that advance robot learning practice. This paper's main practical takeaway ("use a bigger universal LoRA") is useful but modest. The simulation-only evaluation further limits practical impact.

4. **Missing low-hanging experiments:** The 4-class router for clean handling, expert weight similarity analysis, and at least one alternative expert training strategy are all feasible and would substantially change the contribution profile.

**For acceptance, the paper would need:**
- A successful downstream application of the diagnostic finding (training curriculum design, architecture modification, or monitoring system with demonstrated value)
- OR substantially deeper investigation of the negative result (expert similarity analysis, alternative training strategies, higher-rank sweep to resolution)
- AND expanded related work (25+ references minimum)
- AND real-robot validation of at least the diagnostic finding