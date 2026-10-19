# Paper Framing — meta_brain_lora_routing

## Target Venue
- Primary: CoRL 2026 (Austin, Nov 9-12)
- Abstract DDL: 2026-05-26
- Paper DDL: 2026-05-29

## Core Insight

VLA internal representations already encode rich perturbation-type-specific information (Phase 0: single-layer F1=1.0 at K=1), yet existing robustness methods either ignore this diagnostic signal entirely (VLA-GSE, RobustVLA) or only use it for detection without correction (SAFE). Meta-Brain closes the loop: diagnose perturbation type from frozen activations, then route to a type-specialized LoRA expert for targeted correction — achieving the "right fix for the right failure" at ~10x fewer parameters than perturbation-agnostic capacity routing.

## Core Claims (3)

1. **Perturbation Diagnosability** — Frozen VLA (pi0) internal activations at a single layer and single token (PaliGemma layer 6, first token) encode perturbation type with perfect accuracy (3-class K=1 F1=1.000 with first-token pooling), enabling real-time, zero-overhead perturbation diagnosis from a single forward pass.

2. **Targeted Correction > Uniform Correction** — Perturbation-type-specific LoRA experts (Visual/Spatial/Physical), routed by the diagnosed type, outperform a universal LoRA baseline of equivalent total parameter budget on LIBERO-Plus, demonstrating that routing by perturbation type is a more efficient use of adaptation capacity than uniform correction.

3. **Parameter-Efficient Robustness** — Meta-Brain (~12M trainable params) achieves robustness gains that a parameter-matched universal LoRA (rank 48, ~12M) cannot replicate, demonstrating that routing by perturbation type is more efficient use of adaptation capacity than uniform correction. Cross-backbone comparison with VLA-GSE (114M on Qwen3-VL-4B) is indirect/suggestive only — primary efficiency metric is within-backbone gain-over-parameter-matched-baseline.

## Story Spine

- **Problem**: VLAs achieve >90% on standard LIBERO but collapse under perturbation (pi0: 53.6% on LIBERO-Plus). Different perturbation types disrupt different processing stages — visual perturbations corrupt early representations, spatial perturbations invalidate action trajectories, physical perturbations break force assumptions. Yet all existing robustness methods apply either single-modality correction or perturbation-agnostic uniform adaptation.

- **Existing approaches & gaps**: VLA-GSE (114M params, 81.2% on LIBERO-Plus) demonstrates routing helps, but routes by per-token capacity needs — the same gating configuration handles camera (64.4%) and layout (82.6%) without perturbation awareness. FTM achieves 90% on visual perturbations with 4K params but cannot handle spatial/physical. RobustVLA adds +12.6% via uniform adversarial training. No method combines perturbation diagnosis with type-specific correction.

- **Our framing**: We propose perturbation-diagnostic routing as a new design dimension for VLA robustness, orthogonal to capacity-based routing (VLA-GSE), rank-based adaptation (LoRA-SP), and task-based routing (MoIRA/CORAL). We show that VLA internals already "know" what went wrong — they just lack the mechanism to apply the right fix. Meta-Brain adds that mechanism with minimal parameters.

- **Headline result template**: "On LIBERO-Plus, Meta-Brain achieves X% with ~12M trainable parameters, improving Y% over frozen pi0 baseline and Z% over a parameter-matched rank-48 universal LoRA (~12M), demonstrating that perturbation-diagnostic routing outperforms uniform adaptation at equivalent parameter budget."

## Contribution Structure (single system contribution, not 3 independent claims)

One well-executed systems contribution: Meta-Brain — a modular framework that diagnoses perturbation type from frozen VLA activations and routes to type-specialized LoRA experts. Supporting evidence:
1. **Empirical finding**: VLA internal representations encode perturbation type at single-layer, single-step granularity (prerequisite observation)
2. **Architecture + ablation**: PAR router + LoRA bank with comprehensive ablation ladder including parameter-matched controls (rank-48 universal), random routing baseline, and rank scaling analysis
3. **Practical insight**: Layer placement analysis reveals perturbation-type-to-layer mapping (V→early, S→mid, P→late)

Note: Correction Memory is an optional module — present as ablation footnote, NOT as a named architectural component. Dream reviewers across all tiers viewed CM (+1-2%) as padding.

## Venue Fit (CoRL 2026)

**Strengths**:
- Pi0 backbone + LIBERO-Plus eval is core CoRL territory
- Architecture operates on representations (sim evaluation methodologically sufficient)
- Parameter efficiency matters for real-robot deployment (~12M vs 114M)
- Single forward pass routing = no latency overhead for real-time control

**Risks**:
- Sim-only evaluation (mitigated: LIBERO-Plus is CVPR 2026 standard, sim-only is accepted pattern at CoRL for architecture contributions)
- Single backbone (pi0) — need gain-over-baseline framing to enable contextualized comparison with VLA-GSE (Qwen3-VL-4B)
- Absolute performance may trail SRPO (82.1%) / CorridorVLA (83.21%) which use full training — frame as parameter-efficient approach, not absolute SOTA chase

## Anticipated Reviewer Concerns

### C1: "Phase 0 classification is too easy — trivially solvable routing"
**Risk**: High Phase 0 accuracy (F1=0.993) may suggest the task is trivial and routing adds no value.
**Response**: Easy diagnosis ≠ easy correction. The value of routing is in Phase 1 (specialized vs universal LoRA), not Phase 0. Easy routing is actually desirable — it means the router adds zero overhead concern. Ablation exp-005 directly tests whether routing matters.

### C2: "Sim-only evaluation, no real robot"
**Risk**: CoRL values real-world experiments.
**Response**: LIBERO-Plus is the standard robustness benchmark (CVPR 2026). Meta-Brain operates on representations, not hardware-specific signals. Sim-only is the established evaluation pattern for VLA architecture contributions at CoRL (SAFE, VLA-GSE, RobustVLA all sim-only on LIBERO variants).

### C3: "Single backbone (pi0), limited generalizability"
**Risk**: Results may be specific to pi0's PaliGemma architecture.
**Response**: (a) Phase 0 finding (perturbation classifiability) is grounded in mechanistic evidence across multiple VLAs (SAFE on OpenVLA, probing on OpenVLA, feature steering on pi0.5 + OpenVLA). (b) Tier 3 cross-backbone experiment on SmolVLA/OpenVLA if time permits. (c) Gain-over-baseline metric enables fair comparison across backbones.

### C4: "Parameter budget comparison unfair — different backbone from VLA-GSE"
**Risk**: Comparing 6M (on pi0) vs 114M (on Qwen3-VL-4B) is apples-to-oranges.
**Response**: Compare gain-over-respective-LoRA-baseline: VLA-GSE gains +12.0% over LoRA (69.2% → 81.2%); Meta-Brain should gain X% over universal LoRA on pi0. Parameter efficiency = gain per trainable parameter. Also report absolute numbers with caveat.

### C5: "3-class taxonomy may be too coarse"
**Risk**: Lumping camera+light+background+noise into "Visual" may lose useful distinctions.
**Response**: Phase 0 6-class analysis shows intra-Visual perturbations are more similar to each other than to Spatial/Physical. 3-class matches the mechanistic distinction in VLA processing (early/mid/late layers). Ablation: 6-class routing vs 3-class routing comparison.

### C6: "Correction Memory adds complexity for marginal gain"
**Risk**: CM may seem over-engineered for routing-weight modulation.
**Response**: CM is presented as an optional module. Ablation (with/without CM) quantifies its contribution. CM adds only 1 learned parameter (alpha) + CPU-bound FAISS.

### C7: "Unseen perturbation types at deployment — open-set robustness"
**Risk**: 3-class taxonomy is fixed. Novel perturbation types (weather, sensor degradation) will be force-classified to nearest known type, potentially routing to wrong expert.
**Response**: (a) PAR outputs a probability distribution — low-confidence predictions (high entropy) can trigger fallback to universal LoRA or no correction, providing a natural open-set rejection mechanism. (b) The 3-class taxonomy covers the major perturbation axes in robotic manipulation; truly novel perturbations are an explicit limitation we acknowledge. (c) Correction Memory provides partial adaptation — retrieved exemplars from similar but not identical perturbations can modulate routing appropriately.

### C8: "Training-deployment feature dimension mismatch"
**Risk**: Phase 0 classifier trained on episode-averaged activations (~44 steps) but router uses single-step (K=1) features.
**Response**: K=1 few-shot analysis directly validates this: F1=0.898 overall, layer 6 K=1=1.0. Paper must explicitly state: (a) classifier is trained on episode-averaged features for label efficiency, (b) deployed router uses single-step features, (c) K=1 validation bridges this gap. Phase 1 PAR router will be trained directly on single-step features to eliminate any residual gap.

## Baselines & Comparisons

| Method | Type | Params | Expected Comparison |
|--------|------|--------|-------------------|
| Frozen pi0 | Lower bound | 0 | Our improvement over this = headline number |
| Universal LoRA (rank 16) | Ablation | ~3.7M | Same per-expert capacity, no routing — tests Claim 2 |
| Meta-Brain (PAR + ALB) | Ours | ~12M | Full system (3x3.7M experts + 0.5M router) |
| Meta-Brain + CM | Ours (full) | ~12M + 1 | With Correction Memory |
| Random routing | Ensemble control | ~12M | Random expert assignment — tests if routing matters vs ensemble effect |
| Oracle routing | Upper bound | ~12M | Perfect routing — gap to Meta-Brain = routing quality |
| FTM/FLA | Visual-only | 4K-4.7M | Strong on visual, cannot do spatial/physical |
| VLA-GSE | Capacity routing | 114M | Different backbone (Qwen3-VL-4B), compare gain-over-LoRA |
| RobustVLA | Adversarial training | Full model | Uniform approach, compare robustness gain |

## Key Figures (Planned)

1. **Architecture diagram**: Frozen pi0 → PAR (layer 6) → soft routing → LoRA-V/S/P bank → corrected output
2. **Phase 0 evidence**: t-SNE of layer 6 activations colored by perturbation type + confusion matrix
3. **Main result table**: LIBERO-Plus per-perturbation breakdown (7 categories × methods)
4. **Ablation ladder**: Bar chart — Frozen → Universal LoRA → Random Routing → Meta-Brain → Oracle
5. **Parameter efficiency**: Scatter plot — gain-over-baseline vs trainable parameters (Meta-Brain vs VLA-GSE vs FTM vs RobustVLA)
6. **Routing analysis**: Heatmap of PAR soft routing weights per perturbation type (should be near-diagonal)
