---
dream_id: dream_20260515T154653
tier: worst
overall_score: 4/10 — Reject
timestamp: 2026-05-15T16:51:31.493605+00:00
---

# Dream Review Report — Consolidated Roundtable

**Paper:** "Do VLAs Know What Went Wrong? Probing Perturbation Representations and the Limits of Diagnostic Routing"
**Venue:** CoRL 2026 (~39% acceptance rate, OpenReview 1–10 scale)
**Review Mode:** Full (2 Reviewers, 4-step roundtable)
**Date:** 2026-05-15

---

## Reviewer Assignments

| Reviewer | Focus | Independent Score |
|----------|-------|-------------------|
| R1 | Methods + Experiments | 5/10 (Borderline) |
| R2 | Novelty + Related Work | 4/10 (Weak Reject) |

---

## Step 1: Independent Reviews (Summary)

### R1 — Methods & Experiments (Score: 5/10)

**Strengths:**
- Phase 0 probing (F1=1.0 at K=1, cross-backbone replication on SmolVLA F1=0.971) is a clean, well-executed positive finding
- Honest reporting of the negative Phase 1 result with proper 5-seed statistical testing (p=0.12, 95% CI [−0.5, +3.5])
- Oracle routing ablation (67.8%) definitively caps routing benefit at +3.0%, cleanly shifting diagnosis from "bad router" to "insufficient expert differentiation"
- Comprehensive design-dimension ablations across 4 axes (CM, router architecture, granularity, layer placement) systematically rule out alternative explanations
- Cross-backbone replication confirms the negative pattern is structural, not backbone-specific
- Statistical rigor above CoRL average: per-seed reporting, paired t-tests, confidence intervals

**Weaknesses:**
- **(Critical)** The central thesis — "expert capacity is the bottleneck" — is never experimentally validated. No rank sweep (r=16/32/64). The paper diagnoses the bottleneck but does not test its prediction (that higher rank would unlock routing benefit). This is the single most damaging omission.
- **(Critical)** Parameter-mismatched primary comparison: Meta-Brain (6M) vs. Universal LoRA (2M). A rank-48 universal LoRA (~6M) is the natural parameter-matched control. Its absence makes the +1.5% delta uninterpretable — the universal LoRA may simply be under-parameterized.
- **(Major)** No random/uniform routing baseline. Without it, one cannot distinguish routing signal value from ensemble/averaging effects of combining three expert outputs. The +1.5% could come from ensembling, not routing.
- **(Major)** Training data imbalance across experts is uncontrolled. Visual perturbations span 4 subcategories (camera, light, background, noise) while Spatial and Physical have 1 each. LoRA-V sees 4× more diverse data, which confounds specialization analysis.
- **(Moderate)** Bibliography critically thin (9 references). Missing MoE-LoRA literature, probing foundations, TTA methods.

**R1 Scores:**
- Soundness: 5/10
- Empirical Rigor: 5/10
- Reproducibility: 6/10
- Overall: 5/10
- Confidence: 4/5

---

### R2 — Novelty & Related Work (Score: 4/10)

**Strengths:**
- Honest framing of a negative result with clear statistical reporting; the "split answer" narrative is effective
- Phase 0 cross-backbone replication is a genuine generalization result with standalone value
- Clear identification of the bottleneck via oracle ablation + routing weight analysis
- Routing-accuracy-to-downstream dissociation (Table 13: 98.1–99.3% routing accuracy → 66.0–66.3% downstream) is a clean falsification datapoint

**Weaknesses:**
- **(Critical)** Phase 0 is an incremental extension of existing probing work. SAFE [6] already detects perturbations from VLA internal representations. Moving from binary anomaly detection to 3-class perturbation-type classification is a natural next step, not a conceptual breakthrough. The near-perfect F1 may reflect LIBERO-Plus's categorically distinct synthetic perturbations rather than a deep VLA property.
- **(Critical)** The routing architecture (PAR + weighted LoRA combination: h' = h + Σ wk · LoRAk(h)) is architecturally identical to LoRAMoE, MoLoRA, MixLoRA, and other MoE-LoRA methods. The only distinction is the routing signal source (perturbation type vs. task/input features). This is not acknowledged in the paper.
- **(Critical)** 9 references for a CoRL submission is disqualifying. Missing entire literatures: MoE-LoRA (architecturally identical methods), test-time adaptation (alternative paradigm), probing foundations (Alain & Bengio 2017), adapter composition (AdapterFusion, Poly), PaliGemma citation. Three works named in text (MoIRA, CORAL, LoRA-SP) are absent from the bibliography.
- **(Major)** The three "contributions" are not independent: setup (Phase 0), finding (negative routing result), discussion (ablation collection). Presenting ablations as a "design-dimension analysis framework" inflates scope without theoretical grounding.
- **(Major)** The negative result may be predictable from low-rank adaptation literature. At rank 16, the top singular vectors of perturbation correction matrices are likely shared across types, making expert convergence expected. The paper provides no guidance on the rank threshold where routing becomes beneficial.
- **(Moderate)** VLA-GSE comparison in Table 11 is misleading: cross-backbone parameter efficiency ratios are meaningless. SAFE-to-Meta-Brain proximity is not discussed. The perturbation taxonomy is inherited from LIBERO-Plus, not derived from representational analysis.

**R2 Scores:**
- Novelty/Originality: 3/10
- Significance/Impact: 4/10
- Related Work Completeness: 2/10
- Clarity: 7/10
- Overall: 4/10
- Confidence: 4/5

---

## Step 2: Cross-Sharing — Points of Agreement and Disagreement

### Strong Agreement (both reviewers)
1. **Phase 0 is the strongest finding** but has limited novelty over SAFE/existing probing work
2. **Missing parameter-matched baseline** (rank-48 universal LoRA at ~6M) is a critical gap that undermines the central comparison
3. **No rank sweep** fatally weakens the "expert capacity bottleneck" thesis — the core claim is stated but never experimentally validated
4. **No random routing baseline** makes the +1.5% delta uninterpretable (routing signal vs. ensemble effect)
5. **Bibliography is severely deficient** (9 references, missing directly relevant MoE-LoRA literature)
6. **Statistical rigor is above average** for the venue — honest reporting, 5 seeds, paired t-tests, CIs
7. **Cross-backbone replication** is a genuine strength that adds scientific value
8. **Oracle ablation** is a well-designed diagnostic that cleanly identifies the ceiling

### Disagreement (resolved during convergence)
- R1 gave more weight to the thoroughness of the ablation suite (4 design axes × multiple configurations = comprehensive coverage). R2 viewed the ablations as standard practice that does not constitute a "contribution." **Resolution:** Both agree the ablations are well-executed but insufficient to compensate for limited novelty and the missing critical controls. The ablations answer secondary questions while the primary question (does routing help at higher capacity?) remains unanswered.
- R1 was slightly more generous toward the "informative negative result" framing. R2 argued the result may be predictable. **Resolution:** Both agree the negative result is *useful* but *under-diagnosed*. Without rank scaling, the paper stops at "routing doesn't help at rank 16" rather than reaching the more valuable finding of "routing requires rank X+ to unlock."

---

## Step 3: Convergence — Consolidated Assessment

### Verdict: **Reject** (Converged Score: 4/10)

The paper falls below the CoRL 2026 acceptance threshold. While Phase 0 and the honest negative-result framing are appreciated, the combination of (1) limited novelty over prior probing/MoE-LoRA work, (2) missing critical experimental controls, and (3) a disqualifyingly thin bibliography prevents acceptance.

### Dimension Scores (Converged)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| **Originality** | 3/10 | Phase 0 is an incremental step from SAFE/probing literature. Meta-Brain architecture is standard MoE-LoRA. The negative result is useful but potentially predictable. |
| **Quality / Soundness** | 5/10 | Statistical methodology is sound (5 seeds, paired t-tests, CIs). But missing three critical controls (parameter-matched universal, random routing, rank sweep) undermines the central claim. |
| **Clarity** | 7/10 | Well-structured, honest reporting, clean narrative arc. Deductions for missing architecture figure, no t-SNE visualization, and the three-contribution framing. |
| **Significance** | 4/10 | Phase 0 diagnosability has modest standalone value. The negative routing result lacks actionable guidance (no rank threshold). Limited to VLA-robustness niche. |
| **Relevance to CoRL** | 6/10 | Addresses robot learning robustness directly. Uses VLA backbones and robot manipulation benchmark. Simulation-only evaluation is acceptable for CoRL but limits impact. |
| **Related Work** | 2/10 | 9 references. Missing MoE-LoRA, TTA, probing foundations, adapter composition, PaliGemma. Three works named but uncited. |
| **Overall** | **4/10** | Below acceptance threshold. Honest but incremental, with critical experimental gaps. |
| **Confidence** | 4/5 | Both reviewers have strong familiarity with MoE, LoRA, probing, and VLA literatures. |

---

## Step 4: Consolidated Detailed Review

### Summary
This paper asks whether VLA internal representations encode perturbation type and whether this signal can improve robustness via diagnostic routing. Phase 0 shows near-perfect perturbation diagnosability from frozen activations (F1=1.0 at K=1 on pi0, F1=0.971 on SmolVLA). Phase 1 tests Meta-Brain (PAR router + 3 specialized rank-16 LoRA experts, 6M params), finding only +1.5% gain over universal LoRA (p=0.12, not significant), with oracle routing capping the benefit at +3.0%. The paper reframes this as evidence that expert capacity, not routing quality, is the binding constraint.

### Strengths

**S1 (Both): Rigorous statistical methodology.** Five-seed evaluation with paired t-tests, exact p-values, confidence intervals, and per-seed reporting (Table 6) is well above the CoRL median. The paper does not hide the null result behind selective reporting.

**S2 (Both): Oracle ablation is a well-designed diagnostic.** Replacing the learned router with ground-truth labels (Table 4: oracle=67.8%, only +3.0% over universal) cleanly separates routing quality from expert capacity. This is the most informative single experiment in the paper.

**S3 (Both): Cross-backbone replication adds genuine scientific value.** Phase 0 replicating on SmolVLA (F1=0.971, different vision encoder) and Phase 1 showing the same marginal routing pattern (Δ=+1.2) demonstrates the findings are not pi0-specific. Table 17 is well-designed.

**S4 (R1): Comprehensive ablation coverage.** The paper tests 4 design axes (correction memory, router architecture, routing granularity, layer placement) plus FTM comparison and parameter efficiency. All 11 planned experiments from the design document are present in the paper, demonstrating thorough execution.

**S5 (R2): Honest, effective narrative framing.** The "split answer" (VLAs know what went wrong, but this knowledge doesn't translate to correction gains) is clean and avoids the common trap of overselling a negative result.

**S6 (R1): Routing-accuracy-to-downstream dissociation.** Table 13 (routing accuracy 98.1–99.3% → downstream 66.0–66.3%, range 0.3%) provides a clean falsification of "better routing = better correction" at rank 16.

### Weaknesses

**W1 (Critical, Both): The "capacity bottleneck" thesis is stated but never experimentally validated.** The paper's central claim — that expert capacity at rank 16 is the binding constraint — predicts that higher-rank experts would unlock routing benefit. Yet no rank sweep (r=32/64/128) is presented. Without this, the reader cannot distinguish "routing fails because of insufficient capacity" from "routing fails for fundamental reasons." A single rank-32 experiment would either (a) show emerging specialization, validating the thesis and making the paper much stronger, or (b) show continued convergence, suggesting a deeper problem. Either outcome is informative; the absence of the experiment is not.

**W2 (Critical, Both): Missing parameter-matched universal LoRA baseline.** Meta-Brain uses ~6M parameters (3 experts × 2M each). The universal LoRA baseline uses only 2M. A rank-48 universal LoRA (~6M) is the natural parameter-matched control. If it achieves ≥66.3%, the entire Meta-Brain architecture has zero value proposition. This is the most basic experimental control for any routing/MoE paper and its absence undermines the +1.5% delta.

**W3 (Critical, R2): 9 references is critically below CoRL norms (30–50).** Missing literatures are not peripheral but directly relevant:
- **MoE-LoRA** (LoRAMoE, MoLoRA, MixLoRA): Meta-Brain's routing equation (h' = h + Σ wk · LoRAk(h)) is architecturally identical to these methods. Without citation, the paper cannot establish architectural novelty.
- **Probing foundations** (Alain & Bengio 2017, Belinkov 2022): Phase 0 uses standard linear probing without citing the methodology's origins.
- **Test-time adaptation** (TENT, TTT, MEMO): Alternative paradigm for the same problem, entirely absent.
- **Adapter composition** (AdapterFusion, Poly, AdaMix): Established frameworks for combining adapters via learned routing.
- **PaliGemma** (Beyer et al. 2024): The primary vision encoder is uncited.
- **MoIRA, CORAL**: Named in Section 2 text but absent from the bibliography.

**W4 (Major, Both): No random/uniform routing baseline.** Without testing uniform (1/3, 1/3, 1/3) routing weights, one cannot distinguish the value of the routing signal from the ensembling effect of combining three expert outputs. The +1.5% gain could come entirely from expert averaging, not diagnostic routing.

**W5 (Major, R2): Limited novelty.** Phase 0 extends SAFE's binary perturbation detection to 3-class typing — a natural increment, not a conceptual advance. The near-perfect F1 may reflect LIBERO-Plus's categorically distinct synthetic perturbations rather than a deep VLA representational property. Meta-Brain's architecture is a standard MoE-LoRA composition with perturbation type as the gating signal. The negative result, while honest, may be predictable from the low-rank adaptation literature (shared top singular vectors across perturbation correction matrices).

**W6 (Major, R2): Three claimed "contributions" are not independent.** Contribution 1 (Phase 0 diagnosability) is a prerequisite. Contribution 2 (negative routing result) is the main finding. Contribution 3 ("design-dimension analysis") is a collection of ablation tables without formal framework, composability theory, or unifying structure. These are setup, finding, and discussion — not three separable contributions.

**W7 (Moderate, R1): Training data imbalance.** Visual perturbations span 4 subcategories (camera, light, background, noise) while Spatial (layout) and Physical (robot) have 1 each. LoRA-V sees 4× more diverse training data, confounding the specialization analysis.

**W8 (Moderate, R2): VLA-GSE comparison in Table 11 is misleading.** Cross-backbone parameter efficiency ratios (pi0 vs. Qwen3-VL) are not meaningful. Despite the footnote, co-locating these in one table invites invalid comparison.

**W9 (Moderate, R2): "General property of VLA representations" is overclaimed.** Two VLAs on one synthetic benchmark does not establish generality. Real-world perturbations are continuous, co-occurring, and unlabeled — categorically different from LIBERO-Plus's simulator-applied transforms.

**W10 (Minor, R2): SAFE-to-Meta-Brain proximity not discussed.** SAFE's detection features + softmax + LoRA experts ≈ Meta-Brain. The paper claims to "close the diagnose-correct loop" but does not discuss how trivial this closure is from SAFE's starting point.

### Questions for Authors

1. What is the performance of a **rank-48 universal LoRA** (~6M params, matching Meta-Brain's total budget)? This is the most important missing experiment.
2. What is the performance under **random/uniform routing weights** (1/3, 1/3, 1/3)? This isolates routing signal from ensembling.
3. Have you tested **rank 32 or 64 experts**? Even a single datapoint would validate or refute the capacity-bottleneck thesis.
4. How does Meta-Brain differ architecturally from **LoRAMoE or MixLoRA** beyond the routing signal source?
5. Have you tested using **SAFE's detection features** as the PAR router?
6. Have you performed **unsupervised clustering** on layer-6 activations to verify the 3-class taxonomy reflects natural representational structure?
7. What is Meta-Brain's behavior under **compound perturbations** (e.g., camera + layout simultaneously)?
8. Can you report the **FTM + Universal LoRA combination** (FTM for visual, universal for non-visual) as a practical baseline?

### Experiment Coverage Assessment

The paper covers all 11 experiments from the design plan:
| # | Experiment | Covered? | Tables |
|---|-----------|----------|--------|
| 1 | LoRA expert training | ✓ | 2, 3 |
| 2 | Meta-Brain assembly | ✓ | 4, 5 |
| 3 | Oracle routing | ✓ | 4 |
| 4 | Ablation ladder (5-seed) | ✓ | 6, 7, 8 |
| 5 | FTM comparison | ✓ | 9, 10 |
| 6 | Parameter efficiency | ✓ | 11 |
| 7 | Correction Memory | ✓ | 12 |
| 8 | Router architecture | ✓ | 13 |
| 9 | 6-class vs 3-class | ✓ | 14, 15 |
| 10 | Cross-backbone SmolVLA | ✓ | 17 |
| 11 | Layer placement | ✓ | 16 |

Coverage is 11/11, but the three most important *missing* experiments (rank sweep, parameter-matched universal, random routing) were not in the original plan either — a design-phase blind spot.

### Minor Issues
- No architecture diagram / system figure
- No t-SNE or UMAP visualization of Phase 0 clusters (would strengthen the diagnosability narrative)
- Table numbering in text occasionally mismatches (e.g., "Table 5" for routing weights appears as Table 5 in the PDF but is referenced inconsistently)
- The Correction Memory module (Section 3.5) feels like an afterthought — +0.4% (p=0.38) could be dropped without loss

### Recommendation

**Reject.** The paper is below the CoRL 2026 acceptance threshold despite thorough execution.

The core issue is that the paper thoroughly documents *what* happens (routing doesn't help at rank 16) but does not experimentally validate *why* (the capacity-bottleneck thesis) or determine *when* routing would help (no rank scaling). The missing parameter-matched baseline makes even the +1.5% delta uninterpretable. The 9-reference bibliography and standard MoE-LoRA architecture further limit the contribution.

### Path to Acceptance

1. **Run rank-scaling experiments** (r=16/32/64/128). If routing benefit emerges at higher ranks, the narrative shifts to "routing requires minimum expert capacity C*" — a concrete, actionable finding.
2. **Add parameter-matched universal LoRA** (rank 48, ~6M) and **random routing baseline**.
3. **Expand bibliography to 30+ references.** Engage with MoE-LoRA, TTA, probing foundations, adapter composition.
4. **Reframe as one contribution:** "Perturbation type is diagnosable in VLAs but routing-based correction requires expert capacity beyond rank 16" — supported by the ablation suite.
5. **Add unsupervised analysis** of Phase 0 (clustering, RSA, information-theoretic measures) to elevate it beyond standard probing.
6. **Test compound perturbations** to address the taxonomy limitation.

With rank-scaling showing a clear capacity threshold, parameter-matched baselines, and proper literature engagement, this could become a solid empirical contribution at CoRL or a robotics workshop.

---

## Final Scores

| Dimension | Score |
|-----------|-------|
| Originality | 3/10 |
| Soundness / Quality | 5/10 |
| Clarity | 7/10 |
| Significance | 4/10 |
| Relevance (CoRL) | 6/10 |
| Related Work | 2/10 |
| **Overall** | **4/10 — Reject** |
| Confidence | 4/5 |
