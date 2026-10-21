# Re-Dream Evidence Package v2 (2026-05-16)

> Compiled from registry (44 experiments), paper_framing.md, memory.md, ROADMAP.md.
> All metrics are registry-sourced with exp_id provenance. Primary aggregation: **image_mean** (fair comparison). last_preaction in supplementary unless noted.

---

## Claim 1: Vision Encoder Dominance

**Statement**: VLA action-relevant representation structure is determined by the frozen vision encoder (SigLIP). SigLIP+projector RSA (ρ=0.615) far exceeds full VLA (ρ≈0.501, image_mean) and standalone vision model (DINOv2 ρ=0.388).

### Primary Evidence

| # | Experiment | Metric | Value | CI / p-value | Notes |
|---|-----------|--------|-------|-------------|-------|
| 1 | `d027_siglip_only_rsa` | SigLIP+Projector RSA | **0.6153** | 95% CI [0.5257, 0.6954] | Smoking gun: LLM input already has peak action alignment |
| 2 | `p0_image_mean_rsa_verify` | VLA trained image_mean RSA | 0.5014 | L23 peak | Gap vs SigLIP = 0.1139 |
| 3 | `p0_image_mean_rsa_verify` | VLA untrained image_mean RSA | 0.4847 | L23 peak | Gap vs SigLIP = 0.1306 |
| 4 | `lg_rsa_analysis` | DINOv2 RSA | 0.388 | — | Vision-only baseline, lowest |
| 5 | `p0_functional_probe_v2` | Projector action R² | **0.7063** | — | Functional capacity at LLM input |
| 6 | `p0_functional_probe_v2` | DINO action R² (cls_token) | **0.7116** | DINO vs Proj: Δ=0.005, CI=[-0.008, 0.019], p=0.22 (n.s.) | DINO ≈ Projector in R² |

**Key ordering**: RSA: SigLIP (0.615) >> VLA (0.501) >> DINO (0.388). R²: DINO (0.712) ≈ SigLIP (0.706) > VLA image_mean (0.683).

### Supporting Evidence

| # | Experiment | Metric | Value | Notes |
|---|-----------|--------|-------|-------|
| 7 | `p0_functional_action_delta_probe` | Projector delta R² | 0.1181 | Delta info also traces to vision encoder |
| 8 | `p0_functional_action_delta_probe` | Untrained delta R² (L0) | 0.1174 | ≈ Projector — architecture-intrinsic |
| 9 | `mvp2_action_dino` | DINO action R² (LIBERO-10) | 0.6759 | Cross-benchmark: DINO still strong |
| 10 | `mvp2_delta_dino` | DINO delta R² (LIBERO-10) | 0.0609 | 2× lower than SigLIP-based models on delta |
| 11 | `d021_output_head_analysis` | Vision+Projector weight change | rel_change=0, cos_sim=1.0 | Frozen between trained/untrained — all action info is pretrained |
| 12 | `mvp_probe_untrained` | Untrained temporal ρ (L1) | 0.9334 | Random LLM + frozen SigLIP already ρ=0.93 |
| 13 | `dinov2_baseline` | DINO temporal ρ | 0.9008 (per-task mean) | Strong but < SigLIP-based models |

### Anticipated Attacks & Defenses

| Attack | Defense | Evidence |
|--------|---------|----------|
| SigLIP vs DINO confounded by VL pretraining | **Strengthens story**: VL pretraining contributes geometric alignment, not information content. DINO ≈ Proj in R² (p=0.22) but RSA gap 0.388 vs 0.615 is huge. VL pretraining → alignment, not information. | `p0_functional_probe_v2` |
| Single architecture (OpenVLA) | Scope limited to "OpenVLA-class architecture" in paper. OpenVLA is most widely used open-source VLA. plan_012 (CLIP-ViT) adds pretraining control. | Limitations section |
| RSA ≠ task performance | Functional probes confirm: Proj R²=0.706 decodes actions well. Geometric alignment and functional capacity are distinct dimensions — paper discusses both. | `p0_functional_action_probe` |

---

## Claim 2: LLM Redistributes Action-Relevant Structure (Training-Dependent)

**Statement**: LLM degrades distributed image token **geometric alignment** (RSA: 0.615→0.501) and functional capacity (R²: 0.706→0.683, p=0.001), but global structure preserved (CKA monotonically rises). **After training**, LLM concentrates action signal to readout token (trained R²=0.731 > projector 0.706, p=0.001). **Untrained LLM cannot do this** (untrained readout best=0.686 < projector 0.706). Readout concentration is learned behavior.

### Primary Evidence

| # | Experiment | Metric | Value | CI / p-value |
|---|-----------|--------|-------|-------------|
| 1 | `p0_functional_probe_v2` | Proj vs LLM image_mean R² | Δ=0.0231 (Proj wins) | CI=[0.0105, 0.0367], p=0.001 |
| 2 | `p0_functional_action_probe` | LLM last_preaction R² (trained, L19) | **0.7309** | vs Proj: Δ=0.0246, CI=[0.009, 0.04], p=0.0014 |
| 3 | `untrained_last_preaction_probe` | Untrained best last_preaction R² | 0.6858 (L32) | < Proj 0.706 |
| 4 | `untrained_last_preaction_probe` | Trained vs untrained last_preaction | Δ=0.0452 | CI=[0.0321, 0.0585], p<0.0001, all 10 tasks positive |
| 5 | `p0_image_mean_rsa_verify` | RSA degradation: SigLIP → VLA | 0.6153 → 0.5014 | Gap = 0.1139 |
| 6 | `plan_003_perlayer_degradation` | Proj→L1 RSA drop | 0.13–0.25 (~20–40%) | Embedding interface is bottleneck |

### Supporting Evidence

| # | Experiment | Metric | Value | Notes |
|---|-----------|--------|-------|-------|
| 7 | `plan_003_perlayer_degradation` | Per-layer pattern | Non-monotonic (3/4 conditions) | Mid-layer partial recovery; no-inst trained uniquely increasing |
| 8 | `p0_functional_action_probe` | Untrained image_mean R² (L0) | 0.7136 | Architecture-intrinsic: L0 ≈ projector |
| 9 | `p0_functional_action_delta_probe` | Delta: Proj vs trained | Δ=−0.0034, CI=[−0.0066, 0.0005], p=0.04 | ≈ tie on delta dimension |
| 10 | `p0_functional_action_probe` | Grip accuracy: Proj=0.922, LLM_img=0.918, readout=0.918 | — | Discrete action also consistent |

### RSA-CKA Dissociation (C7)

| Metric | Projector | Trained L23 | Untrained L23 | DINO | Trained last_preaction L32 |
|--------|-----------|-------------|----------------|------|---------------------------|
| **RSA** | **0.615** | 0.501 | 0.485 | 0.388 | — |
| Linear CKA | 0.0809 | 0.0834 | **0.0894** | 0.0664 | **0.127** |
| RDM CKA | 0.2568 | 0.2599 | 0.2464 | 0.2408 | **0.2898** |

Source: `plan_009_cka_verification`

**Critical finding**: CKA ordering **reverses** vs RSA for projector vs trained/untrained. RSA: projector > trained > untrained. CKA: untrained > trained > projector. 

**Interpretation**: RSA captures **local geometric alignment** (distance structure matching actions) — LLM degrades this. CKA captures **global structure preservation** — LLM preserves or improves this. **Claim 2 must be limited to "geometric (RSA) degradation"**, not generalized "representation quality degradation."

CKA last_preaction = 0.127 (highest) supports redistribution narrative: readout token has strongest global alignment with action structure.

Per-layer CKA is monotonically increasing (L0=0.081 → L32=0.098), contrasting RSA's non-monotonic pattern.

### Anticipated Attacks & Defenses

| Attack | Defense | Evidence |
|--------|---------|----------|
| CKA contradicts RSA — which to trust? | Different metrics capture different properties. RSA = local geometric alignment, CKA = global structure. Both are informative. Paper presents RSA as primary, CKA as supplementary, discusses dissociation as finding. | `plan_009_cka_verification` |
| Readout concentration might be architectural, not learned | Untrained readout R²=0.686 < projector 0.706. If architectural, untrained should also concentrate. Training is necessary. | `untrained_last_preaction_probe` |
| Aggregation bias: image_mean vs last_preaction tell different stories | Paper uses image_mean (fair, aggregation-neutral) as primary. last_preaction in supplementary. Both aggregations discussed transparently. | `p0_image_mean_rsa_verify` |
| LLM "degradation" overstated — R² only drops 0.023 | Acknowledged: marginal degradation. The story is redistribution, not destruction. Proj provides 96.6% of final capacity (0.706/0.731). | `p0_functional_action_probe` |

---

## Claim 3: Training = Routing, Not Creating

**Statement**: VLA fine-tuning does not change distributed representation structure (image_mean RSA: trained 0.501 ≈ untrained 0.485, bootstrap CI includes 0, p=0.20), but improves readout concentration (trained last_preaction R²=0.731 >> untrained 0.686, Δ=0.045, CI=[0.032, 0.058], p<0.0001). Instruction input affects neither. Training contributes information **routing**, not new action **knowledge**.

### Primary Evidence

| # | Experiment | Metric | Value | CI / p-value |
|---|-----------|--------|-------|-------------|
| 1 | `p0_bootstrap_ci_training_effect` | image_mean RSA: trained − untrained | Δ=0.0206 | CI=[−0.0314, +0.0638], p=0.20, **n.s.** |
| 2 | `p0_bootstrap_ci_training_effect` | last_preaction RSA: trained − untrained | Δ=0.0076 | CI=[−0.0395, +0.0558], p=0.37, **n.s.** |
| 3 | `untrained_last_preaction_probe` | Readout R²: trained − untrained | Δ=0.0452 | CI=[0.0321, 0.0585], p<0.0001, **significant** |
| 4 | `d027_trained_no_inst_rsa` | 2×2 matrix (all 4 conditions) | 0.480–0.501 | All within 0.021 range |
| 5 | `d021_instruction_ablation` | Instruction effect on RSA | Δ=0.0044 | << 0.10 threshold |

**The dissociation**: Distributed structure invariant (p=0.20) but readout concentration training-dependent (p<0.0001). This is the "routing not creating" signature.

### Supporting Evidence (incl. negatives that support)

| # | Experiment | Type | Finding | Support for C3 |
|---|-----------|------|---------|----------------|
| 6 | `d021_instruction_ablation` | **Negative** | No-inst RSA=0.4802 ≈ with-inst 0.4846 | Instructions don't affect structure → action info is vision-driven |
| 7 | `d021_output_head_analysis` | **Negative** | Vision+Projector identical (cos_sim=1.0); LLM weights uniformly changed | No shallow adaptation — all training effect is in LLM routing |
| 8 | `lg_pca1024_linear_pertimestep` | **Negative** | Trained ≈ untrained (both R²≈1.0, Δ=−0.0008) | Linear structure invariant to training |
| 9 | `lg_gc_trained` / `lg_gc_untrained` | **Negative** | Both 100% goal classification accuracy | Goal info present regardless of training (probe saturated) |
| 10 | `lg_rsa_analysis` | **Negative** (G2 FAIL) | Δρ=0.003 at peak, threshold 0.08 | RSA trained ≈ untrained — original G2 gate correctly identified invariance |
| 11 | `mvp_001` | **Negative** (G2 FAIL) | Temporal distance Δρ=0.043, threshold 0.15 | Trained vs untrained gap small even on temporal distance |
| 12 | `p0_functional_action_delta_probe` | Supporting | Delta R²: Proj 0.118 ≈ trained 0.122 ≈ untrained 0.117 | Delta information also training-invariant |
| 13 | `d027_trained_no_inst_rsa` | Supporting | Instruction effect trained: −0.0014; untrained: +0.0044 | Both near zero — instructions irrelevant |

### Anticipated Attacks & Defenses

| Attack | Defense | Evidence |
|--------|---------|----------|
| p=0.20 doesn't prove invariance, just fails to reject | Correct — but CI=[−0.031, +0.064] bounds the possible effect. Even upper bound (0.064) is small relative to projector-LLM gap (0.114). Combined with 6 converging methods all showing no effect, weight of evidence favors invariance. | `p0_bootstrap_ci_training_effect` |
| Maybe training creates subtle structure that RSA/CKA miss | Functional probes also show invariance on image_mean (both near 0.68-0.71). Multiple metrics converge. Only readout concentration differs. | `p0_functional_action_probe`, `p0_functional_action_delta_probe` |
| "Routing" is vague — what's the mechanism? | Self-attention redistributes information from distributed image tokens to the prediction position (last_preaction). Consistent with autoregressive next-token prediction: info flows from context to output. Per-layer curve shows non-monotonic recovery, consistent with attention-mediated routing. | `plan_003_perlayer_degradation` |
| Random instructions might produce same results as no-inst | **plan_008 tests this** (RUNNING). Placeholder — results TBD. | `plan_008_random_inst_control` |

### Pending: plan_008 Random Instruction Control (RUNNING — placeholder)

**Purpose**: Distinguish "instruction content doesn't matter" from "having any text in instruction position doesn't matter." If random instructions ≈ real instructions in RSA, confirms instruction content is irrelevant. If random < no-inst, suggests instruction position matters but content doesn't.

**Status**: RUNNING on westd-19183. Results will be integrated into this section upon completion.

---

## Overall Assessment

### D030 First Dream Failure Analysis

D030 (2026-05-15) dream evaluated three tiers, all below acceptance (best = borderline reject).

**What was available at D030**:
- SigLIP-only RSA smoking gun (0.615)
- 2×2 matrix (trained/untrained × with/no instruction)
- Instruction ablation (negative)
- Output head analysis (negative)
- Per-layer RSA degradation curve
- Aggregation robustness (image_mean)
- Bootstrap CI on training effect

**What was missing at D030**:
- Functional probes (plan_011) — no R² evidence for degradation/redistribution
- DINO three-way comparison — couldn't triangulate vision encoder dominance
- Untrained readout probe — couldn't prove redistribution is training-dependent
- CKA verification — didn't know about RSA-CKA dissociation
- Trained vs untrained last_preaction bootstrap CI — no statistical test on readout

**D030 failure diagnosis**: The framing was still "LLM degrades" without the redistribution mechanism. No functional evidence, only geometric (RSA). The story lacked a mechanistic account of what training does (routing) and what the LLM contributes (readout concentration). Reviewers saw "vision encoder good, LLM bad" as a thin finding.

### New Evidence Since D030 (itemized)

| # | Evidence | Experiment | Impact |
|---|---------|-----------|--------|
| 1 | Functional action probe: Proj 0.706 > LLM img 0.683 (p=0.001) | `p0_functional_action_probe` | Confirms RSA finding with independent metric |
| 2 | Readout concentration: LLM last_preaction 0.731 > Proj (p=0.001) | `p0_functional_action_probe` | Reveals LLM's positive contribution — redistribution not just degradation |
| 3 | DINO R²=0.712 ≈ Projector (p=0.22) | `p0_functional_probe_v2` | Geometric-functional dissociation: VL pretraining → alignment, not info |
| 4 | Action delta probe: all ~0.12, training-invariant | `p0_functional_action_delta_probe` | Extends invariance to delta dimension |
| 5 | Untrained readout R²=0.686 < Proj 0.706 | `untrained_last_preaction_probe` | Proves redistribution requires training — the "routing" evidence |
| 6 | Trained vs untrained readout: Δ=0.045, CI=[0.032, 0.058], p<0.0001 | `untrained_last_preaction_probe` | Statistical confirmation of training-dependent readout |
| 7 | CKA ordering reversal (RSA-CKA dissociation) | `plan_009_cka_verification` | New finding: metric dependency. Strengthens paper by showing nuance |
| 8 | CKA last_preaction = 0.127 (highest) | `plan_009_cka_verification` | CKA independently supports readout concentration |

### Remaining Gaps

| Gap | Priority | Status | Plan |
|-----|----------|--------|------|
| Random instruction control | P0 | RUNNING (plan_008) | Placeholder in C3, integrate when done |
| CLIP-ViT pretraining control | P1 | Planned (plan_012) | Disentangle "VL pretraining" from "SigLIP specifically" |
| LIBERO-Spatial cross-benchmark | P2 | Planned (plan_010) | Generalization across task suites |
| Delta last_preaction probe | P2 | Not started | Complete the aggregation comparison for delta |

### Strength Rating per Claim (1–5 scale)

| Claim | Rating | Justification |
|-------|--------|---------------|
| **C1: Vision Encoder Dominance** | **4.5/5** | RSA smoking gun (0.615 >> 0.501 >> 0.388) with bootstrap CI. Functional probe confirms (R² 0.706). DINO three-way comparison adds depth (geometric ≠ functional). Only deduction: single architecture and missing CLIP-ViT control (plan_012). |
| **C2: LLM Redistributes (Training-Dependent)** | **4.0/5** | RSA degradation quantified with CI. Functional degradation (p=0.001) + readout concentration (p=0.001) + training-dependency (p<0.0001). CKA dissociation adds nuance but requires careful framing ("geometric degradation" only). Deduction: must navigate metric dependency honestly; readout mechanism is inferred not directly measured (no attention analysis). |
| **C3: Training = Routing, Not Creating** | **3.5/5** | Distributed structure invariance (p=0.20, CI bounds effect). Readout training-dependency (p<0.0001). 6+ converging negative results. Deduction: absence-of-evidence framing (can't prove invariance, only fail to reject); plan_008 pending; "routing" mechanism is indirect (no attention weights). Strengthens to 4.0 if plan_008 confirms. |

### Summary for Re-Dream Input

Relative to D030's borderline-reject assessment, this package adds:
1. **Mechanistic depth**: "LLM degrades" → "LLM redistributes via training-dependent readout concentration"
2. **Functional validation**: Independent R² probes converge with RSA findings
3. **Triangulation**: DINO comparison reveals geometric-functional dissociation (new insight)
4. **Statistical rigor**: Bootstrap CIs on all key comparisons, 10-task paired tests
5. **Metric robustness**: CKA partially confirms, partially dissociates — presented as finding, not weakness
6. **Negative results as evidence**: 7 negatives systematically rule out alternatives (instruction effect, shallow adaptation, training creates structure)

The three-claim structure (dominance → redistribution → routing) forms a coherent mechanistic narrative that was absent at D030. Each claim has primary evidence with CIs, supporting evidence, and pre-addressed reviewer concerns.
