# CoRL 2026 Rebuttal Outline — vla-ssd

> 准备于 2026-05-24 | 基于内部 Review Overall 7/10

## Attack Surface 1: Single Benchmark (LIBERO only)

**Reviewer Objection**: All analyses confined to LIBERO. Generalization to other embodiments unclear.

**Existing Defense**:
- Cross-suite validation: 4 suites (Goal, Spatial, Object, Long), R² exit collapse consistent (Δ=0.156–0.455) at VLM→VLA transition
- OpenVLA trained on 970K OXE episodes (multi-platform), routing not LIBERO-specific
- Three distinct VLA families (Llama-2-7B, Phi-3-mini, Qwen2.5-VL-3B)

**Additional Rebuttal**:
- Exit collapse only at VLM→VLA (6/6), absent at VLA→VLA (0/4) — transition-type specificity is architecture-independent
- Two NLP controls (Llama-2-chat + Phi-3-mini-instruct, both ΔR²=0.000) confirm action-training specificity

## Attack Surface 2: No Behavioral Validation (open-loop only)

**Reviewer Objection**: All analyses correlational. No behavioral evidence that routing patterns affect task performance.

**Existing Defense**:
- ρ=0.583 correlation with LIBERO success rates (p=0.10, n=9)
- Within-suite ρ=1.0 on Goal (n=3), uniformly positive across suites
- Explicit caveat: "directional; validating requires controlled experiments"

**Additional Rebuttal**:
- CF experiments: Cohen's d≥0.45 across all trained conditions — instruction perturbation causes directional output shifts without degrading GT MSE (ΔMSE≈0), consistent with information-computation dissociation
- Three-tier routing gradient explains VLA→VLA modest CF gains (Δ=+0.04–0.24) vs VLM→VLA large gains (12× on NORA)
- Per-token normalization: 38.2× text/image ratio (trained) vs 1.5× (untrained) eliminates token-count confound

## Attack Surface 3: N=2 VLM→VLA Transitions

**Reviewer Objection**: Only 2 VLM→VLA transitions (TracVLA, NORA). N=2 insufficient for cross-architecture generality.

**Existing Defense**:
- Three architectures total, 10/12 matrix cells filled
- 6/6 VLM→VLA cells show exit collapse

**Additional Rebuttal**:
- OpenVLA as negative control: VLA→VLA transition, 0/4 cells exceed Δ>0.10 threshold — the contrast itself is the architectural validation
- Three backbone families with distinct properties: Llama-2-7B (MHA, 32L), Phi-3-mini (MHA, 32L), Qwen2.5-VL-3B (GQA, 36L)
- L1 head count variation (Phi-3: 32/32; Qwen2.5-VL: 13-14/16) shows framework sensitivity while R² collapse remains invariant
