# exp_084_frozen_dt_emb_walker_s0 Analysis

## Experiment Summary
- **Task**: Walker Walk (DMC)
- **Config**: Frozen dt_embedding (requires_grad=False, random init), subsample ON, fixed dt=2, H=8
- **Seed**: 0 | **Steps**: 105K → completed at step 112K (EXIT_CODE=0)
- **Server**: bjb1-45299 (cuda:0)
- **Parent**: exp_042_frozen_dt_emb_walker
- **Hypothesis**: Frozen dt_embedding does not trigger CIVO — proving dt_emb TRAINING is the necessary condition for CIVO onset.

## Eval/Return Trajectory

| Step | eval_return | ve_ratio | delta_ve | alert |
|------|-------------|----------|----------|-------|
| 5K   | 37.4        | —        | —        | —     |
| 15K  | 129.1       | 0.0      | 0.0      | 0.0   |
| 25K  | 161.6       | 0.1      | 0.1      | 0.0   |
| 35K  | 253.7       | 0.2      | 0.1      | 0.0   |
| 45K  | 312.7       | 0.2      | 0.1      | 0.0   |
| 55K  | 234.0       | 0.4      | 0.2      | 0.0   |
| 65K  | 246.8       | 0.4      | 0.0      | 0.0   |
| 75K  | 90.1        | 0.9      | 0.5      | 0.0   |
| 85K  | 188.9       | 0.4      | -0.5     | 0.0   |
| 95K  | 334.1       | 0.2      | -0.2     | 0.0   |
| 105K | 281.5       | 0.2      | 0.0      | 0.0   |

- **eval_return_final**: 281.5
- **eval_return_peak**: 334.1 @ 95K

## CIVO / NVE Analysis

### ve_ratio Pattern
- Peak ve_ratio = 0.9 @ 75K — **transient, single-point spike** coinciding with eval dip (90.1)
- Immediately corrected: 0.4 @ 85K → 0.2 @ 95K → 0.2 @ 105K
- delta_ve oscillates bidirectionally (-0.5 to +0.5), **not monotonically increasing**
- civo/alert = 0.0 at all steps

### Value Function Diagnostic
- value_mean @ 75K: 77.7 (eval=90.1) → v/e = 0.86
- value_mean @ 95K: 68.9 (eval=334.1) → v/e = 0.21
- value_mean @ 105K: 62.1 (eval=281.5) → v/e = 0.22
- Value function is **declining** (77→69→62) while eval **rises** — opposite of CIVO pattern
- ve_ratio spike driven by eval crash (denominator), NOT value inflation (numerator)

### NVE Computation
- Baseline Walker Walk ve_ratio reference: ~0.4 (from exp_009e step-matched baseline @55K = 0.4035)
- NVE_peak = 0.9 / 0.4 = **2.25x** (transient, NOT sustained — single checkpoint)
- NVE_final = 0.2 / 0.4 = **0.5x**
- NVE_median (last 5 checkpoints) = 0.2 / 0.4 = **0.5x**
- **No sustained NVE > 1.5x** over 2+ consecutive checkpoints

### CIVO Diagnostic Comparison

| Criterion | Trained dt_emb (exp_009e) | Frozen dt_emb (exp_084) |
|-----------|---------------------------|-------------------------|
| ve_ratio sustained >1.0 | Yes (3+ checkpoints) | No (single spike) |
| delta_ve monotonic | Yes (all positive) | No (oscillating) |
| value inflation | Yes (increasing) | No (decreasing) |
| eval decline | Yes (systematic) | No (volatile but recovering) |
| civo/alert | Triggered | Never triggered |

### Classification: **NO CIVO** (nve_classification: no_civo)

## Comparison

### vs Baseline (exp_009a_baseline_walker_s2 @ 105K)
- Baseline eval @ 105K: 836.5
- Frozen eval @ 105K: 281.5 (33.6% of baseline)
- Performance gap expected: frozen random dt_emb hurts representation quality without providing adaptive benefits

### vs Parent (exp_042_frozen_dt_emb_walker, 210K steps)
- exp_042 eval_final: 612.5, eval_peak: 682.4
- exp_084 only ran 105K steps vs 210K — performance still ramping up
- exp_042 nve_peak: 0.194, nve_final: 0.051 — consistent with our finding

### vs Trained dt_emb (exp_009e_008d_walker_s1)
- Trained: ve_ratio monotonically rose to 1.67, NVE 4.13x, eval collapsed to 82.8
- Frozen: ve_ratio stable ≤ 0.4 (except transient spike), eval volatile but not collapsing
- **Stark contrast confirms hypothesis**

## Gate Behavior
- gate_dt_mean = 2.0 constant (all steps)
- gate_dt_2_frac = 1.0 (100% of gates at dt=2)
- gate_empirical_entropy = 0.0, gate_entropy_ratio = 0.0
- Frozen embedding correctly produces constant dt=2 (no learned temporal gating)

## Conclusion: **SUCCESS**
Frozen dt_embedding with random init does not trigger CIVO. The hypothesis is supported: dt_emb TRAINING (gradient flow through the embedding layer) is the necessary condition for CIVO onset, not the mere presence of the embedding.
