# Ablation: K-Value Sweep

We sweep the number of VLA samples K ∈ {2, 10, 20} drawn from the flow-matching policy and held fixed at the obs_only CRM head (ε = 0.2). The VLA-only K=1 baseline is reported for reference. Increasing K beyond 2 yields no measurable success-rate gain on either suite, supporting our adaptive K=2 configuration (Plan A) as Pareto-optimal in compute.

**Table A: Effect of K on closed-loop success rate (mean ± std across seeds).**

| K | Object SR (%) | Spatial SR (%) | n_seeds | Object exp_ids | Spatial exp_ids |
|---|--------------:|---------------:|--------:|----------------|-----------------|
| 1 (VLA-only) | 10.8 ± 1.3 | 29.4 ± 1.5 | ≥4 / ≥4 | `eval-vla-only-object-*` | `eval-pi05-vla-only-spatial-*` |
| 2 (Plan A, adaptive) | **18.3 ± 2.1** | **35.0 ± 1.0** | 3 / 3 | `eval-plan-a-object-seed{42,43,44}` | `eval-plan-a-spatial-seed{42,43,44}` |
| 10 | 16.8 ± 1.8 | 34.5 ± 1.5 | ≥3 / ≥3 | obs_only norm0.2 seed pool | spatial obs_only seed pool |
| 20 | 18.8 ± 1.0 | 34.3 ± 0.6 | 4 / 3 | `eval-k20-obs-only-object-seed{42,43,44,45}` | `eval-k20-obs-only-spatial-seed{42,43,44}` |

Per-seed K=20 raw numbers (Object): 20%, 18%, 18%, 19%. Per-seed K=20 raw (Spatial): 35%, 34%, 34%. All K=20 runs use the same CRM checkpoint (`obs_only_K10_eps02_default`) and differ only in the number of candidate actions resampled at inference.

**Diminishing returns beyond K=2.** Moving from K=1 → K=2 captures the bulk of the gain on both benchmarks (+7.5pp Object, +5.6pp Spatial). Subsequent doublings of K provide no additional improvement: on Object, K=10 (16.8%) and K=20 (18.8%) bracket the K=2 mean (18.3%) within one standard deviation; on Spatial, the three K values lie within 0.7pp of one another (34.3-35.0%) and the K=20 standard deviation (0.6%) overlaps the K=2 and K=10 confidence ranges. The pattern is consistent with the obs_only CRM's correction signal being driven by the observation features rather than by candidate diversity — once two samples provide an uncertainty estimate sufficient to trigger correction, additional candidates are absorbed by the same correction head without measurable benefit.

**Implication for compute–accuracy trade-off.** A single flow-matching forward pass dominates inference cost; K=20 requires 10× more VLA forwards than K=2 with no return on closed-loop SR. The adaptive K=2 configuration (Plan A) — which performs a second forward only when the pairwise L2 distance between the first two samples exceeds τ=P50=0.0749 — pays at most 2× VLA compute and triggers correction on roughly 84% of steps on Object and 98% on Spatial, while matching K=20 SR within noise. We therefore adopt K=2 (Plan A) as the default in all downstream experiments and recommend it as the operating point for deployment.
