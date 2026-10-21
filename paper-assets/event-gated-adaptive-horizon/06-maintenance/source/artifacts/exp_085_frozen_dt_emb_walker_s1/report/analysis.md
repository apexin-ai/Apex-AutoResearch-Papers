# exp_085_frozen_dt_emb_walker_s1 Analysis

## Experiment Summary
- **Task**: Walker Walk (DMC)
- **Config**: Frozen dt_embedding (requires_grad=False, random init), subsample ON, fixed dt=2, H=8
- **Seed**: 1 | **Steps**: 105K → completed at step 112K (EXIT_CODE=0)
- **Server**: bjb1-45299 (cuda:1)
- **Parent**: exp_042_frozen_dt_emb_walker
- **Hypothesis**: Multi-seed validation that frozen dt_embedding does not trigger CIVO, confirming dt_emb TRAINING is the necessary condition.

## Eval/Return Trajectory

| Step | eval_return | ve_ratio | delta_ve | alert |
|------|-------------|----------|----------|-------|
| 5K   | 31.0        | —        | —        | —     |
| 15K  | 225.2       | 0.0      | 0.0      | 0.0   |
| 25K  | 128.0       | 0.2      | 0.2      | 0.0   |
| 35K  | 181.7       | 0.3      | 0.0      | 0.0   |
| 45K  | 200.4       | 0.3      | 0.0      | 0.0   |
| 55K  | 156.6       | 0.4      | 0.1      | 0.0   |
| 65K  | 281.5       | 0.2      | -0.2     | 0.0   |
| 75K  | 267.5       | 0.2      | 0.0      | 0.0   |
| 85K  | 46.2        | 1.2      | 1.0      | 0.0   |
| 95K  | 241.1       | 0.2      | -1.0     | 0.0   |
| 105K | 69.3        | 0.8      | 0.6      | 0.0   |

- **eval_return_final**: 69.3
- **eval_return_peak**: 281.5 @ 65K

## CIVO / NVE Analysis

### ve_ratio Pattern
- Peak ve_ratio = 1.2 @ 85K — **transient single-point spike** coinciding with eval crash (46.2)
- Immediately corrected to 0.2 @ 95K (eval recovered to 241.1)
- Final ve_ratio = 0.8 @ 105K (eval dropped again to 69.3)
- delta_ve alternates sign (+1.0, -1.0, +0.6) — **stochastic oscillation, not monotonic divergence**
- civo/alert = 0.0 at all steps

### Value Function Diagnostic (Critical)
- value_mean @ 65K: 55.0 (eval=281.5) → v/e = 0.20
- value_mean @ 75K: 56.4 (eval=267.5) → v/e = 0.21
- value_mean @ 85K: 57.0 (eval=46.2) → v/e = 1.23
- value_mean @ 95K: 55.8 (eval=241.1) → v/e = 0.23
- value_mean @ 105K: 54.5 (eval=69.3) → v/e = 0.79

**Key finding**: Value function is STABLE at 54-57 throughout 65K-105K. The ve_ratio spikes are caused entirely by **eval crashes** (denominator), NOT value inflation (numerator). This is the diagnostic distinction from true CIVO, where value_mean systematically inflates while eval declines.

### NVE Computation
- Baseline Walker Walk ve_ratio reference: ~0.4
- NVE_peak = 1.2 / 0.4 = **3.0x** (transient, NOT sustained — single checkpoint @ 85K)
- NVE_final = 0.8 / 0.4 = **2.0x** (but value function stable, eval volatile)
- NVE_median (last 5 checkpoints: 0.2, 0.2, 1.2, 0.2, 0.8 → median=0.2) = **0.5x**
- **No sustained NVE > 1.5x** over 2+ consecutive checkpoints

### vs True CIVO Pattern

| Criterion | Trained dt_emb CIVO (exp_009e) | Frozen s1 (exp_085) |
|-----------|-------------------------------|---------------------|
| ve_ratio sustained >1.0 | Yes: 0.41→0.69→1.67 (3 consecutive) | No: 1.2→0.2 (immediate reversal) |
| Value inflation | Yes: value increases while eval drops | No: value stable at 54-57 |
| Eval trajectory | Monotonic decline: 167→146→141→83 | Stochastic oscillation: 282→268→46→241→69 |
| delta_ve | All positive (accelerating) | Alternating sign (noise) |
| Mechanism | dt_emb training enables reward model exploitation | Eval volatility from random embedding noise |

### Classification: **NO CIVO** (nve_classification: no_civo)

The elevated ve_ratio at 85K and 105K is an artifact of eval crashes in a high-variance seed. The value function shows no delusional inflation — it remains stable around 55 while eval oscillates between 46 and 282. This is stochastic policy instability (expected with a frozen random embedding), not the systematic value-overestimation feedback loop that defines CIVO.

## Comparison

### vs Baseline (exp_009a_baseline_walker_s2 @ 105K)
- Baseline eval @ 105K: 836.5
- Frozen s1 eval @ 105K: 69.3 (8.3% of baseline)
- Seed 1 significantly more volatile than seed 0 (281.5). This cross-seed variance is high but consistent with the frozen random embedding providing inconsistent temporal information.

### vs exp_084 (frozen seed 0)
- Seed 0 eval_final: 281.5 vs Seed 1: 69.3 (large variance)
- Seed 0 ve_ratio stable ≤ 0.4 (except 0.9 spike), Seed 1 higher variance
- Both seeds: no CIVO alert, no sustained ve_ratio elevation
- Cross-seed consistency: **both confirm no CIVO**, despite different absolute performance

### vs Parent (exp_042_frozen_dt_emb_walker, 210K steps)
- exp_042 eval_final: 612.5 at 210K
- Seed 1 at 105K is underperforming — may improve with more training, or may be a weaker seed

### vs exp_087_frozen_dt_emb_cheetah_s1
- Cheetah s1: NVE = 0.33, ve_ratio_peak = 0.2, clean no-CIVO
- Walker s1 noisier (NVE_peak 3.0x transient) but same conclusion: no sustained CIVO

## Gate Behavior
- gate_dt_mean = 2.0 constant (all steps)
- gate_dt_2_frac = 1.0 (100% of gates at dt=2)
- gate_empirical_entropy = 0.0
- Frozen embedding correctly produces constant dt=2

## Conclusion: **SUCCESS**
Despite higher eval volatility and transient ve_ratio spikes (driven by eval crashes, not value inflation), frozen dt_embedding does not trigger CIVO. The hypothesis is supported across seed 1: dt_emb TRAINING is the necessary condition for CIVO onset. The value function diagnostic (stable ~55 throughout) is the strongest evidence — CIVO requires systematic value overestimation, which is absent here.
