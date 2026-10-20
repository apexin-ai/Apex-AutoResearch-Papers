# VLA Safety + 3D: Distilled Research Patterns

Source: 11 papers (8 deep, 3 abstract), 2024-2026.

## Benchmark & Metrics

**LIBERO is the standard** (6/11). Success Rate (%) is universal. Safety benchmarks are fragmented: Safety-CHORES / SafeLIBERO / custom—no shared benchmark. Safety metrics diverge: Cumulative Cost vs CAR vs collision count. Real-world validation sparse (4/8 deep-read). **Confidence**: high.

## Baseline Landscape

**Tier-1** (4+ papers): OpenVLA, Diffusion Policy, pi0. **Tier-2** (2-3): SpatialVLA, CoT-VLA, OpenVLA-OFT, Octo. Median count: 8. Papers with <5 baselines look weak (CoFreeVLA: 2, VLSA: 2).

## Method Trends

**Implicit 3D supervision rising** (4/11): Align VLA features with frozen 3D encoders (VGGT/DepthAnything/occupancy/Gaussian). Pattern: 3D encoder supervises training, skippable at inference. **Source**: SpatialForcing, DepthVLA, GST-VLA, OccVLA.

**CBF safety filters rising** (3/11): VLSA, OGM-CBF, Learning to Nudge. Plug-and-play at inference, no retraining, mathematical guarantee. Trend: decoupling safety from policy training.

## Competitor Claims

| Paper | Type | Key Number |
|-------|------|-----------|
| SafeVLA | safe RL | 83.58% CC↓, +3.85% SR |
| VLSA | CBF filter | +59.16% CAR, 0.356ms overhead |
| SpatialForcing | implicit 3D | 98.5% LIBERO SR, 0 inference cost |
| GST-VLA | structured 3D | 96.4% LIBERO, 83.1% LIBERO-Pro |
| OccVLA | occ supervision | camera-only = GT-occ input |
| DepthVLA | depth expert | predicted depth > GT depth |

## Critical Gap

**No paper combines 3D representations with safety for VLA.** 3D papers ignore safety; safety papers lack 3D. OGM-CBF bridges occupancy+CBF but predates VLA. **Support**: 11/11 absence. **Confidence**: high.

## Common Limitations

- Sim-only safety validation (5/8). Single-run, no mean±std (6/8).
- Depth fails on reflective/transparent surfaces (DepthVLA, GST-VLA).
- Safety corrections cause distribution shift (VLSA, CoFreeVLA).

## Experimental Consensus

Multi-stage training (2-3 stages) dominates. 8×A100/H100 standard. LoRA for task adaptation. **Confidence**: high.
