# Rebuttal Drafts — CoRL 2026

> Generated 2026-05-19 by Reviewer. Ready for submission preparation.

## R9-N1: Single Model Scope (OpenVLA-7B only)

### Rebuttal (148 words)

Our findings derive from a structural property — the causal mask — that is shared by all decoder-only VLAs (RT-2, OpenVLA, etc.): image tokens *cannot* attend to instructions, so routing *must* occur at attended positions. We strengthen generalizability in three ways. First, a four-condition training trajectory (untrained → Llama-2 → Bridge-VLA → LIBERO-finetuned) shows consistent routing progression across training stages, not a single-checkpoint artifact. Second, results replicate across two benchmarks (LIBERO-Goal, LIBERO-Spatial; Appendix B). Third, we provide three falsifiable predictions: cross-attention VLAs (π₀, Octo) should lack L1 routing heads; decoder-only VLAs (RT-2) should exhibit similar entry-exit patterns; larger VLAs should show flatter per-head contributions. We agree that multi-model validation is valuable future work, but the architectural constraint, factorial controls (3 LLM conditions × 2 instruction conditions), and testable predictions provide a principled evidence chain beyond single-model observation.

### Second-round defense

1. **"Testable predictions ≠ evidence"**: Predictions are scope delineation, not claim. Mechanistic interpretability standard (Elhage 2021, Olsson 2022, Wang 2023) = single-model deep analysis + architectural argument.
2. **"Llama-2 base 9/32 may be text bias"**: Paper acknowledges this. +15 head delta isolates fine-tuning effect. Trained vs untrained 0→24 comparison is baseline-independent.
3. **"OXE diversity ≠ architecture generalization"**: Agree. Architecture generalization via causal mask + predictions; data generalization via OXE + dual benchmark. Two independent lines.

---

## R9-N2: No Closed-Loop Validation (Open-loop only)

### Rebuttal (143 words)

Our contribution is a representational analysis framework, not a new control policy; closed-loop success rates test a different claim. Within the open-loop regime, we establish convergent evidence through methodologically independent analyses: dose-response ablation across 8 conditions yields monotonic divergence (d = 0.48 → 0.64); counterfactual instruction perturbations produce graduated effects (d = 0.63–0.97) predicted by token novelty (ρ = 1.0); and size-matched specificity controls confirm that instruction-dominant heads exceed random baselines by 2.4σ. Critically, ablating instruction routing alters action trajectories (d = 0.65) without increasing ground-truth prediction error (ΔMSE ≈ 0), revealing an information-computation dissociation: routing controls action *direction*, not *precision*. This triangulation — interventional (dose-response + counterfactual), correlational (probes + RSA), and null-result constraining (ΔMSE) — follows established practice in representational analysis at CoRL and NeurIPS.

### Second-round defense

1. **"Open-loop divergence ≠ closed-loop failure"**: Agree — this is scope boundary. d=0.65 proves routing changes behavior; whether it causes task failure needs closed-loop. Claim is "routing causally modulates action generation", not "ablation breaks the policy".
2. **"ΔMSE≈0 means routing unimportant?"**: Opposite. d=0.65 + ΔMSE≈0 = routing controls direction not precision (information-computation dissociation, Hewitt & Liang 2019). Random ablation's larger R² gain (+0.077 vs +0.042) further supports.
3. **CoRL precedent**: Raghu et al. 2021 (ViT vs CNN), robot representation learning series — all open-loop analysis, community accepts open-loop as sufficient for representational claims.
