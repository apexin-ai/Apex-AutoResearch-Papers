---
dream_id: dream_20260516T075046
tier: worst
overall_score: 5/10 — Marginally Below Acceptance
timestamp: 2026-05-16T08:50:01.868627+00:00
---

# Dream Review Report: Importance Margin Maximization for Robust VLA Token Compression

**Paper:** "Importance Margin Maximization for Robust VLA Token Compression: Navigating the Robustness-Efficiency Pareto Frontier"
**Target Venue:** CoRL 2026
**Review Mode:** Full (2 Reviewers + Roundtable)
**Rating Scale:** 1–10 (CoRL/OpenReview standard; 7=accept, 5=marginally below threshold)

---

## Reviewer Assignments
- **R1**: Methods + Experiments (soundness, rigor, reproducibility)
- **R2**: Novelty + Related Work (originality, positioning, significance)

---

## Step 1: Independent Reviews

### R1 — Methods and Experiments (Score: 5/10)

**Strengths:**
- Clean problem formulation: tracing compression fragility to vanishingly small importance margins (Δk ≈ 0.01) is intuitive and directly actionable.
- Two-stage training protocol is well-ablated (Table 10): joint G3=3.19 → grad-isolated G3=1.34 → two-stage G3=0.87 provides clear mechanistic evidence for decoupling necessity.
- Compression-agnostic plugin design (Table 5) showing +52pp preservation across 3 external methods is the strongest experimental contribution.
- Defense comparison (Table 6) is convincing: IMM dominates in preservation (88% vs next-best 61%) with lowest overhead (1.35× train, 1× infer) and smallest SR drop (−9.3pp).
- Overhead quantification (Table 13) is thorough: net 27.4% latency reduction, 28% memory savings with negligible ACIS cost.
- Honest Pareto framing — explicitly disclaiming lossless compression is commendable.

**Weaknesses:**
- **Formal bound looseness (W1):** Tightness ratio of 9.5× at ε=0.01 (Table 7) means the bound overestimates flip probability by nearly 10×. At small ε (0.005), the ratio reaches 19×. The 7.6× gap between spectral-norm L (1.07) and empirical local Lipschitz (0.14) indicates the bound is fundamentally limited by the Lipschitz estimation, not the margin. The paper acknowledges this but still features the bound prominently in contributions.
- **G3<1.0 is aloha-specific (W2):** On LIBERO, all G3 values are 1.12–1.25 (Table 3). On OpenVLA, G3=1.28 (Table 4). G3<1.0 on aloha appears to be an artifact of high token redundancy in that specific task. The paper acknowledges this but the pruning ratio sweep (Table 9) showing a U-curve with G3<1.0 sweet spot is only validated on aloha.
- **ACIS hard dependency (W3):** Bypass mode drops SR from 68% to 42% (−26pp, Table 2). Stage 2 LoRA adapts the backbone to ACIS-masked inputs, creating an irrecoverable coupling. This means ACIS cannot be disabled at deployment — it is a permanent architectural addition, not an optional module.
- **Nonlinear loss-SR relationship (W4):** v8b+prune has 13% lower action loss than baseline (0.00354 vs 0.00406) but 10pp lower SR (68% vs 78%, Table 2). This disconnect undermines action loss as a proxy metric and raises questions about whether G3 (action loss ratio) is the right measure of compression quality.
- **Statistical power (W5):** 50 episodes per evaluation may be insufficient for detecting moderate effect sizes. No confidence intervals, standard errors, or multi-seed runs reported. The 7pp difference between LIBERO-Spatial (−7pp) and LIBERO-Object (−11pp) could be noise at N=50.
- **Token importance analysis undermines denoising (W6):** Attention weight ratio between pruned/retained tokens is 0.69 (KS p=0.08, not significant at α=0.05, Table 12). Distribution overlap of 72% means pruned tokens are not "noise" — they are moderately less attended. This is consistent with the Pareto framing but weakens any residual denoising narrative.
- **Scalability concern (W7):** Margin ratio drops from 93.2× (SmolVLA 2B) to 12.5× (OpenVLA 7B) — a 7.5× reduction. G3 increases from 1.18 to 1.28. The efficiency of margin maximization appears to decrease with model scale, which is concerning for the foundation model era.

**Missing experiments/analysis:**
- Multi-seed runs with confidence intervals for all SR measurements
- LIBERO pruning ratio sweep (to confirm U-curve shifts upward)
- λ (margin loss weight) sweep to demonstrate practical Pareto navigation
- Real-world robot evaluation (acknowledged limitation)

### R2 — Novelty and Related Work (Score: 5/10)

**Strengths:**
- Compression-agnostic plugin design is the most novel and defensible contribution — enabling IMM to be applied to any importance-based compression method elevates it beyond "yet another compression module."
- The importance margin collapse diagnosis (Δk ≈ 0.01 → Δk ≈ 0.50) is a clean, measurable insight that has prescriptive value for the field.
- Two-stage training is a non-obvious engineering contribution — the necessity of full decoupling (vs. gradient isolation) is an empirical finding that required systematic iteration.
- Honest Pareto framing avoids the overclaiming trap common in compression papers.

**Weaknesses:**
- **Proposition 1 is theoretically trivial (W1):** P(top-k flip) ≤ k·ε·L/Δk follows in 3–4 lines from Lipschitz continuity + union bound over k boundary positions. This is a textbook derivation. More critically, the probabilistic framing is misleading for a deterministic scorer: the correct statement is a sufficient condition (Δk > k·ε·L implies no flip), not a probability bound over random perturbations. The paper partially acknowledges this as "design criterion" but the abstract, contributions list, and conclusion still feature it as a formal theoretical contribution.
- **Critically incomplete bibliography (W2):** Only 7 references — far below CoRL norms (typically 25–40). Major missing literatures:
  - *ViT token pruning*: DynamicViT (Rao et al., NeurIPS 2021) proposes a lightweight prediction module for learning token importance — architecturally very similar to ACIS. ToMe (Bolya et al., ICLR 2023) merges rather than prunes tokens, a potentially more robust alternative. EViT, ATS, A-ViT also relevant.
  - *Margin-based robustness*: Large-margin training (Elsayed et al., NeurIPS 2018), MMA Training (Ding et al., NeurIPS 2020), ArcFace/CosFace. The hinge-margin loss max(0, α − Δk) is structurally identical to the classical SVM margin objective. The paper cannot claim novelty in "maximizing margins for robustness" without engaging this deep lineage.
  - *Certified robustness*: IBP, CROWN, Lipschitz certificates (Tsuzuku et al., 2018). Only randomized smoothing is compared.
  - *Certified top-k stability*: Jia et al. (ICLR 2020) study certified top-k robustness directly — the most important missing reference.
  - *LLM token importance*: H2O, StreamingLLM, ScissorHands — token eviction in LLMs is directly relevant.
  - *Used but uncited*: LoRA (Hu et al., 2022) is employed throughout but never referenced.
- **Insufficient CAGE differentiation (W3):** CAGE [6] formalizes certification for VLA compression and appeared at ICML 2026. The paper dismisses it as "no training-time remedy" but does not compare threat models, bound assumptions, or scope. If CAGE provides tighter certificates under different assumptions, IMM's bound contribution is directly contested.
- **"First robustness-aware framework" overclaim (W4):** RobustVLA (Jacobian reg), ProGAL-VLA (adversarial training), and CAGE all address VLA robustness. IMM's true novelty wedge is "first to maximize importance margins as a compression-agnostic training strategy." This is a valid but narrower claim than currently stated.
- **ACIS novelty unclear without ViT context (W5):** Without discussing DynamicViT's learned importance predictor, it's unclear whether ACIS's contribution is the architecture (cross-attention scorer) or the training objective (margin loss). The paper should make this distinction explicit.
- **Token merging alternative never discussed (W6):** ToMe-style approaches that merge rather than prune tokens inherently retain information from discarded tokens, potentially offering better robustness. This alternative strategy deserves at least discussion.

---

## Step 2: Cross-Sharing

**R1 → R2:**
- The nonlinear action loss vs SR relationship (W4) has implications for novelty: if G3 (action loss ratio) is not a reliable proxy for task performance, then the formal bound on top-k stability (which doesn't directly address downstream performance) is even further from practical guarantees than the tightness gap suggests.
- The ACIS hard dependency reveals a practical limitation that affects the "plug-in" framing — adding ACIS is not optional once trained, which constrains the compression-agnostic narrative.

**R2 → R1:**
- The DynamicViT parallel raises methodological concerns: if ACIS's architecture is not novel (only the margin training objective is), then the ablation should isolate the margin loss contribution from the architecture contribution. Table 10 ablates training modes but not scoring architectures.
- The missing certified top-k stability literature (Jia et al., 2020) could provide a tighter reference bound, making the tightness analysis in Table 7 more informative.

---

## Step 3: Convergence

**Points of agreement (both reviewers):**
1. Two-stage training is a genuine, well-supported contribution.
2. Compression-agnostic plugin is the paper's strongest and most novel claim.
3. Formal bound is oversold — it is a textbook derivation that should be positioned purely as design motivation, not as a theoretical contribution.
4. G3<1.0 is aloha-specific and not generalizable.
5. ACIS hard dependency is a real limitation.
6. Token analysis shows pruned tokens are not "noise" — Pareto framing is appropriate.
7. Bibliography is critically inadequate (7 references).
8. The paper would benefit from real-world validation.
9. Statistical reporting needs improvement (no CIs, limited episodes).

**Resolved disagreement:**
- R1 initially scored 4/10 partly due to concerns from internal project documentation. After cross-sharing, both reviewers agree the paper should be evaluated on its presented content. The experiments cover all 12 planned experiments from the design document, and the breadth is commendable for a 7-page paper. R1 revises upward to 5/10.

**Remaining discussion point:**
- Whether the contribution is sufficient for CoRL even after fixing presentation issues. R1 leans toward "fixable — strong revision could reach acceptance" while R2 considers the theoretical novelty too thin but acknowledges the practical plugin contribution could suffice for a systems/empirical CoRL paper.

---

## Step 4: Consolidated Assessment

### Overall Score: 5/10 — Marginally Below Acceptance Threshold

### Headline Assessment
The paper identifies a real and important problem (adversarial fragility of VLA token compression), proposes a clean and actionable solution (importance margin maximization), and demonstrates it convincingly across a broad experimental canvas. The compression-agnostic plugin design and the two-stage training protocol are genuine contributions that could benefit the community. However, the theoretical contribution is a textbook derivation that is oversold, the bibliography is far below venue standards (7 references vs typical 25–40), and critical related work across at least four major literatures is absent. The paper is not ready for CoRL 2026 in its current form but has a clear path to acceptance with significant revision.

### Consolidated Strengths
1. **Compression-agnostic plugin (most impactful):** +52–55pp preservation uplift across FastV, VLA-IAP, VLA-Cache means the entire existing compression literature can benefit from IMM without inference-time changes.
2. **Clean problem diagnosis:** Tracing fragility to importance margin collapse (Δk ≈ 0.01) is intuitive, measurable, and prescriptively useful.
3. **Well-ablated two-stage training:** G3 progression 3.19→1.34→0.87 across joint/grad-isolated/two-stage provides convincing evidence for the decoupling necessity.
4. **Strong defense comparison:** IMM dominates all alternatives (adv training, smoothing, Jacobian reg) in preservation (88% vs 61% next-best) with lowest overhead and smallest SR drop.
5. **Honest framing:** Explicitly declining to claim lossless compression and presenting results as Pareto tradeoffs is commendable intellectual honesty.
6. **Broad experimental coverage:** 2 architectures, 4 compression methods, 4+ benchmarks, 7 perturbation dimensions in a 7-page paper.

### Consolidated Weaknesses

**Critical (must fix):**
1. **Bibliography below venue threshold:** 7 references is unacceptable for CoRL. Must expand to 25–30, covering ViT token pruning (DynamicViT, ToMe, EViT), margin-based robustness (SVM lineage, large-margin training), certified robustness (IBP, CROWN, Lipschitz certificates), certified top-k stability (Jia et al., 2020), and LLM token importance (H2O, StreamingLLM). LoRA must be cited.
2. **Formal bound oversold:** Proposition 1 is a 3-line derivation from Lipschitz + union bound. The probabilistic framing is misleading for a deterministic scorer. Remove from contributions list; position purely as design motivation throughout. Remove all "certified" and "provable guarantee" language.
3. **Insufficient CAGE differentiation:** Must provide explicit comparison of threat models, assumptions, and scope vs. CAGE (ICML 2026). The "first robustness-aware framework" claim is directly contested.

**Major (should fix):**
4. **G3<1.0 non-generalizability:** Currently acknowledged but underemphasized. The pruning ratio sweep (Table 9) showing a sweet spot is aloha-only. Must either show LIBERO pruning sweep or explicitly caveat that the U-curve with G3<1.0 region is task-specific.
5. **Statistical reporting:** Add multi-seed runs (≥3 seeds), confidence intervals, and significance tests for all SR comparisons. 50 episodes per condition may be underpowered for detecting 7pp differences.
6. **ACIS novelty clarification:** Without ViT pruning context (DynamicViT), it is unclear whether ACIS's architecture or its training objective is novel. Add ablation comparing ACIS architecture with attention-threshold scoring under margin training.
7. **Scalability concern unaddressed:** Margin ratio 93.2× (2B) → 12.5× (7B) is a 7.5× reduction. Discuss implications for scaling beyond 7B and propose mitigation (scaling-aware margin objectives).

**Minor:**
8. **Nonlinear loss-SR gap:** Action loss 13% lower but SR 10pp lower (Table 2) questions G3 as a quality metric. Discuss when G3 is/isn't a reliable proxy.
9. **ACIS hard dependency:** Bypass mode −26pp SR is a deployment constraint. Discuss graceful degradation strategies.
10. **Token merging alternative:** ToMe-style approaches are never discussed as a potentially more robust compression paradigm.
11. **Simulation-only evaluation:** Acknowledged in limitations but important for CoRL, which values real-robot experiments.

### Questions for Authors (Priority Order)
1. How does IMM's stability condition compare to CAGE's certified guarantee? Provide a side-by-side comparison of threat models and assumptions.
2. How does ACIS differ from DynamicViT's importance predictor? Is the contribution the architecture or the training objective?
3. Can you provide multi-seed results (≥3 seeds) with confidence intervals for the headline LIBERO-Plus result (Table 1)?
4. What happens to the pruning ratio U-curve on LIBERO — does it shift fully above G3=1.0?
5. Have you evaluated margin maximization with token merging (e.g., ToMe) instead of pruning?
6. What is the relationship between margin ratio improvement and model scale — is there a theoretical reason for diminishing returns at larger scale?

### Recommendation
**Reject with encouragement to resubmit.** The core contribution (compression-agnostic margin maximization for robust token selection) is sound and practically useful. The experimental coverage is unusually broad for the page count. However, the paper requires:
- A major bibliography expansion (+20 references minimum)
- Honest repositioning of the theoretical contribution as design motivation only
- Explicit CAGE differentiation
- Statistical rigor improvements (multi-seed, CIs)
- ACIS novelty clarification in context of ViT pruning literature

With these revisions, the paper could target CoRL 2027 or a comparable venue. The compression-agnostic plugin result (Table 5) and the defense comparison dominance (Table 6) are strong enough to carry an acceptance if properly contextualized.

### Score Summary
| Dimension | Score |
|-----------|-------|
| Originality | 5/10 — Core idea is sensible but margin maximization for robustness has deep roots (SVMs, large-margin training). Compression-agnostic plugin is genuinely novel. |
| Quality | 5/10 — Broad experiments but bound oversold, statistical rigor insufficient, missing ablations. |
| Clarity | 6/10 — Well-written paper with honest framing, but missing context from related work makes it hard to judge novelty. |
| Significance | 6/10 — Practical value is high (plugin across compression methods, dominates defenses), but limited to simulation. |
| Relevance | 7/10 — Directly addresses deployment efficiency+robustness for VLA models — core CoRL topic. |
| **Overall** | **5/10 — Marginally below acceptance threshold** |
| Confidence | 4/5 |
