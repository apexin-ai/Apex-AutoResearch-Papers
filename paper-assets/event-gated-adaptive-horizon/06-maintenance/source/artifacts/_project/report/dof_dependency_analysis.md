# DoF Dependency Analysis: CIVO Onset Across Environments

Generated: 2026-05-29

## Summary Table

| Environment | DoF | Baseline Eval | Baseline ve_ratio | Gate NVE Peak | Gate Eval | CIVO Rate | Failure Mode | Baseline Health |
|---|---|---|---|---|---|---|---|---|
| Cartpole Swingup | 1 | 673.3±142.0 (n=3) | — | 0.047±0.010 | 236.3±29.7 (n=3) | 0/3 (0%) | non-CIVO degradation | healthy |
| Hopper Hop | 4 | 96.43 (n=1) | 0.559 | 1.6× | 3.26→81.58† (n=1) | 0/1 (0%) | learning delay→recovery | healthy |
| Walker Walk | 6 | 787.7±230.8 (n=4) | 0.651±0.008 | 3.32±1.61 (n=5) | 190.6±90.2 (n=4) | 3/5 (60%) | CIVO | healthy |
| Cheetah Run | 6 | 446.1±2.9 (n=2) | 0.606±0.008 | med 2.3× [0.31,127.6] (n=4) | 123.2±132.9 (n=4) | 3/4 (75%) | CIVO | healthy |
| Quadruped Walk | 12 | — (failed/running) | 6.6×‡ | — (cancelled) | — | — | N/A | **unhealthy** |
| Humanoid Walk | 21 | 1.48±0.36 (n=1) | 12.22 | — (cancelled) | — | — | N/A | **unhealthy** |

† Hopper trained_s0: 3.26 at 105K, recovered to 81.58 by 158K (85% baseline). Pattern: transient_instability_recovered.
‡ Quadruped baseline s0: NVE=6.6× at 125K, far above τ=2.0×. Retry (s0_r2) still RUNNING.

## Detailed Environment Notes

### Cartpole Swingup (1 DoF)
- All 3 gate seeds show NVE < 0.1×, far below CIVO threshold (τ=2.0×)
- Eval degrades to 35% of baseline, but degradation is NOT value-driven
- Interpretation: 1-DoF dynamics too simple for value overestimation cascade
- **Exp IDs**: baseline=exp_060, gate=exp_061

### Hopper Hop (4 DoF)
- Single seed (trained_s0): severe learning delay at 105K (eval=3.26, 3.4% baseline), NVE=1.6×
- Extended to 168K: eval recovered to 81.58 (85% baseline), ve_ratio normalized (0.44)
- Pattern: gate mechanism causes learning delay, not CIVO; agent eventually learns through the gate
- No_dt_emb control (exp_hopper_no_dt_emb_s0): NVE_peak=4.37 but not sustained, eval=10.8 (11% baseline)
- Frozen_s0: degenerate CIVO near zero magnitude (ve=4.3M is eval≈0 artifact, mechanistically distinct)
- **Exp IDs**: baseline=exp_hopper_baseline, gate=exp_hopper_trained_s0/s0_ext

### Walker Walk (6 DoF)
- 3/5 seeds show CIVO onset (NVE≥2.0×): s1 (4.13×), s4 (4.62×), s5 (4.72×)
- 2/5 seeds sub-threshold transient: s2 (1.62×), s3 (1.53×)
- Control experiments perfectly separated: 008f (dt_emb=0) 0/4, 008a (untrained) 0/4
- **Exp IDs**: baseline=exp_001_baseline/s2/s3/s4, gate=exp_009e/009b/008d_civo_trigger_s3/s4/059

### Cheetah Run (6 DoF)
- 3/4 seeds show CIVO onset; s2 extreme (127.6×, catastrophic collapse, eval→2.5)
- s1 sole no-onset seed (NVE=0.31×, eval=309.3 at 72% baseline)
- Onset timing: 45K-75K, overlapping with Walker (35K-45K)
- NVE reported as median+range due to s2 extreme outlier
- **Exp IDs**: baseline=exp_077/083, gate=exp_078/088/091/097

### Quadruped Walk (12 DoF)
- Baseline s0 failed: intrinsic NVE=6.6× at 125K (unhealthy)
- 008d cancelled (no clean baseline for CIVO isolation)
- Baseline s0_r2 retry currently RUNNING
- **Exp IDs**: baseline=exp_quadruped_baseline_s0 (failed), exp_quadruped_baseline_s0_r2 (RUNNING)

### Humanoid Walk (21 DoF)
- Baseline itself CIVO-prone: NVE=12.97×, ve_ratio=12.22, 3 CIVO alerts
- Eval return near-zero (1.48): TDMPC2 struggles with 21-DoF locomotion under current hyperparameters
- 008d cancelled: impossible to isolate gate-induced CIVO from intrinsic value overestimation
- **Exp IDs**: baseline=exp_humanoid_baseline_s0, gate=exp_humanoid_008d_s0 (killed)

## Key Findings

1. **CIVO requires intermediate DoF (6)**: Onset rate is 0% for 1-DoF (Cartpole) and 4-DoF (Hopper), but 60-75% for 6-DoF (Walker, Cheetah). Low-DoF environments either show non-CIVO degradation (Cartpole) or learning delay that self-corrects (Hopper).

2. **High-DoF baselines are intrinsically unstable**: Both 12-DoF (Quadruped, NVE=6.6×) and 21-DoF (Humanoid, NVE=12.97×) baselines exhibit value overestimation WITHOUT the gate mechanism, making CIVO isolation impossible. This is a TDMPC2 limitation, not a CIVO property.

3. **CIVO occupies a "Goldilocks zone"**: The phenomenon requires (a) sufficient dynamic complexity for value overestimation to cascade through learned temporal embeddings, and (b) a stable baseline where overestimation is NOT already present. Current evidence bounds this zone to 6-DoF multi-joint locomotion.

4. **Non-monotonic DoF-CIVO relationship**: CIVO severity does not simply increase with DoF. Instead, very high DoF environments suffer from a different pathology (intrinsic value overestimation in the base algorithm) that masks or subsumes the gate-specific CIVO mechanism.

5. **Cross-environment CIVO consistency at 6 DoF**: Walker (3/5) and Cheetah (3/4) show remarkably consistent CIVO rates (60-75%), onset timing (35K-75K), and consequence diversity (self-correction, sustained degradation, catastrophic collapse).

## Discussion Draft (for paper Limitations/Discussion)

> **Environment and DoF Dependence.** Our analysis of CIVO spans six DeepMind Control Suite environments ranging from 1 to 21 degrees of freedom. CIVO onset—defined as NVE exceeding 2.0× the baseline value estimate—occurs exclusively in 6-DoF environments (Walker Walk: 3/5 seeds, 60%; Cheetah Run: 3/4 seeds, 75%), with zero onset in lower-DoF environments (Cartpole Swingup: 0/3; Hopper Hop: 0/1). In Cartpole (1-DoF), the gate mechanism degrades performance without triggering value overestimation, suggesting the dynamics are too simple for the temporal embedding to induce optimistic value drift. In Hopper (4-DoF), the gate causes severe initial learning delay but the agent eventually recovers to 85% of baseline performance, exhibiting transient instability rather than sustained CIVO.
>
> At higher degrees of freedom, we encounter a different limitation: both Quadruped Walk (12-DoF) and Humanoid Walk (21-DoF) baselines exhibit intrinsic value overestimation (NVE = 6.6× and 12.97×, respectively) even without the gate mechanism, precluding clean CIVO isolation. This likely reflects known scaling challenges in model-based RL with high-dimensional action spaces rather than a property of CIVO itself. Consequently, our CIVO characterization is empirically grounded in 6-DoF locomotion tasks, and generalization to higher-DoF domains remains an open question contingent on improving baseline stability.
>
> These findings suggest that CIVO occupies a complexity "Goldilocks zone": environments must be sufficiently complex for learned temporal embeddings to develop exploitable value prediction biases, yet stable enough under the base algorithm for the gate-induced perturbation to be the dominant source of overestimation. Understanding the precise relationship between environment complexity and CIVO susceptibility—and whether improved base algorithms would shift the onset boundary to higher DoF—is an important direction for future work.

## Data Sources

| Data Point | Source Exp ID(s) |
|---|---|
| Cartpole baseline | exp_060 (3 seeds) |
| Cartpole 008d | exp_061 (3 seeds) |
| Hopper baseline | exp_hopper_baseline |
| Hopper trained | exp_hopper_trained_s0, exp_hopper_trained_s0_ext |
| Hopper no_dt_emb | exp_hopper_no_dt_emb_s0 |
| Hopper frozen | exp_hopper_frozen_s0, exp_hopper_frozen_s0_ext |
| Walker baseline | exp_001_baseline, exp_001_baseline_s2/s3/s4 |
| Walker 008d | exp_009e, exp_009b, exp_008d_civo_trigger_s3/s4, exp_059_walker_trained_s5 |
| Cheetah baseline | exp_077_cheetah_baseline_s0, exp_083_cheetah_baseline_s1 |
| Cheetah 008d | exp_078, exp_088, exp_091, exp_097 |
| Quadruped baseline | exp_quadruped_baseline_s0 (failed), exp_quadruped_baseline_s0_r2 (RUNNING) |
| Quadruped 008d | exp_quadruped_008d_s0 (killed) |
| Humanoid baseline | exp_humanoid_baseline_s0 |
| Humanoid 008d | exp_humanoid_008d_s0 (killed) |
| Cross-seed summary | artifacts/cross_seed_summary.md |
