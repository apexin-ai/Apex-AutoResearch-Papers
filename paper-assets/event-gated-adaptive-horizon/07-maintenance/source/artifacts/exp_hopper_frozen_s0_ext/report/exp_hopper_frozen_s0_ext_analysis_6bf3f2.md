# exp_hopper_frozen_s0_ext Analysis Report

**Date**: 2026-05-27
**Status**: DONE (negative)
**Hypothesis**: Extending frozen_s0 from 105K→150K will show eval_return recovery (rising like trained_s0_ext: 3.26→81.58) with ve_ratio declining, confirming frozen_s0's 'degenerate CIVO' @95K is transient instability.

## Result: HYPOTHESIS FALSIFIED

Frozen_s0 shows **persistent performance collapse** with no recovery through 152K steps. This contrasts starkly with trained_s0_ext's full recovery.

## Eval Return Comparison

| Step | Baseline | Trained_s0 | Frozen_s0 |
|------|----------|-----------|-----------|
| 5K   | 0.06     | 0.04      | 0.04      |
| 35K  | 6.55     | 0.33      | 0.43      |
| 65K  | 3.50     | 0.00      | 0.00      |
| 85K  | 67.62    | 8.01      | 3.58      |
| 95K  | 86.47    | 5.00      | 1.08      |
| 105K | 96.43    | 3.26      | 0.00      |
| 112K | -        | 5.43      | 1.53      |
| 122K | -        | -         | 0.71      |
| 128K | -        | 2.06      | -         |
| 132K | -        | -         | 0.01      |
| 138K | -        | 47.40     | -         |
| 142K | -        | -         | 0.42      |
| 148K | -        | 46.90     | -         |
| 152K | -        | -         | 0.56      |
| 158K | -        | 81.58     | -         |

**Trained_s0_ext**: 3.26 → 81.58 (RECOVERED to 85% of baseline)
**Frozen_s0_ext**: 0.00 → 0.56 (NO RECOVERY, stays <2% of baseline)

## VE Ratio Trajectory (Extension Period)

### Trained_s0_ext
| Step | ve_ratio | Pattern |
|------|----------|---------|
| 105K | 0.897   | elevated |
| 118K | 0.376   | declining |
| 128K | 5.519   | transient spike |
| 138K | 0.370   | recovered |
| 148K | 0.550   | stable |
| 158K | 0.439   | stable |

### Frozen_s0_ext
| Step | ve_ratio | Pattern |
|------|----------|---------|
| 105K | 4,335,664 | artifact (eval=0/ε) |
| 122K | 10.15   | elevated |
| 132K | 955.03  | spike |
| 142K | 18.05   | elevated |
| 152K | 15.08   | elevated |

## Phantom Value Analysis

Frozen_s0's value function learns increasing value magnitudes completely disconnected from actual returns:

| Step | value_mean | target_mean | eval_return |
|------|-----------|-------------|-------------|
| 105K | 4.34      | 4.39        | 0.000       |
| 122K | 7.18      | 7.19        | 0.708       |
| 132K | 7.08      | 7.11        | 0.007       |
| 142K | 7.62      | 7.66        | 0.422       |
| 152K | 8.46      | 8.49        | 0.561       |

The value function converges (value_mean ≈ target_mean, value_loss stable ~1.0-1.1) but on **imaginary trajectories that don't correspond to achievable returns**. This is "phantom value" — the critic is well-calibrated to its own imagined world, but that world doesn't match reality.

Compare with trained_s0_ext where value growth tracks actual performance recovery:
- value_mean 2.93 → 35.81 (12x) while eval_return 3.26 → 81.58 (25x)

## NVE Analysis (step ≥ 35K, baseline-normalized)

| Step | Frozen VE | Baseline VE | NVE | Classification |
|------|-----------|------------|-----|----------------|
| 35K  | 0.456     | 0.166      | 2.75x | > 1.5x threshold |
| 45K  | 0.216     | 0.190      | 1.14x | below threshold |
| 55K  | 14,441    | 0.279      | 51,802x | extreme (eval=0 artifact) |
| 65K  | 819,655   | 3.479      | 235,602x | extreme (eval=0 artifact) |
| 75K  | 0.513     | 0.341      | 1.50x | borderline |
| 85K  | 0.559     | 0.502      | 1.11x | below threshold |
| 95K  | 2.690     | 0.517      | 5.20x | confirmed CIVO |
| 105K | 4,335,664 | 0.559      | 7.76M x | extreme (eval=0 artifact) |

Extension period (no baseline match, using baseline@105K=0.559 as reference):
- 122K: NVE ≈ 18.2x
- 132K: NVE ≈ 1,709x
- 142K: NVE ≈ 32.3x
- 152K: NVE ≈ 27.0x

All massively above 1.5x CIVO threshold throughout the extension.

## Mechanistic Interpretation

1. **Frozen dt_emb creates a persistent learning trap**: The frozen random embedding produces a constant, uninformative signal for dt=2 transitions. The RSSM and actor-critic learn around this noise, but the policy never discovers useful behaviors.

2. **Phantom value without policy improvement**: The critic learns stable value estimates on imagined trajectories (value_loss=1.05, well-converged), but these trajectories don't correspond to achievable real-world returns. The actor optimizes for phantom rewards.

3. **This is NOT transient instability**: Unlike trained_s0_ext where the dt_emb eventually adapted and the system recovered, frozen_s0's embedding can never adapt. The learning failure is structural, not transient.

4. **Different from standard CIVO**: Standard CIVO involves value overestimation causing policy divergence. Frozen_s0's pathology is more fundamental — the policy never learns in the first place because the frozen embedding corrupts the imagined trajectory space.

## Implications for CIVO Theory

- The "degenerate CIVO" label for frozen_s0 was misleading — the high ve_ratio values are artifacts of near-zero eval_return, not genuine value overestimation driving policy collapse.
- Frozen dt_emb does NOT prevent CIVO by preventing value overestimation; it prevents CIVO by preventing **all learning**, which is a trivially different (and worse) outcome.
- The C6 claim (frozen dt_emb as CIVO mitigation) needs reframing: frozen dt_emb is not a viable mitigation because it causes complete learning failure in Hopper.
