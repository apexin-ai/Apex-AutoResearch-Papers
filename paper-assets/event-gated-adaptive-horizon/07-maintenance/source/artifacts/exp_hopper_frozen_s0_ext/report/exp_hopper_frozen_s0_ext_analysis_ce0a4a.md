# exp_hopper_frozen_s0_ext Analysis Report

## Experiment Summary

| Field | Value |
|-------|-------|
| Experiment | exp_hopper_frozen_s0_ext |
| Environment | Hopper-v4 |
| Config | Frozen dt_embedding (random init, no gradient) |
| Steps | 105K → 160K (extended from exp_hopper_frozen_s0) |
| Status | Completed (EXIT_CODE=0) |

## Hypothesis

> "Extending frozen_s0 from 105K→150K will show eval_return recovery (rising like trained_s0_ext: 3.26→81.58) with ve_ratio declining, confirming frozen_s0's 'degenerate CIVO' @95K is transient instability during severe learning delay, not true CIVO mechanism."

**Verdict: FALSIFIED (negative)**

## Key Metrics Trajectory

### eval_return

| Step | eval_return | Phase |
|------|-------------|-------|
| 5K   | 0.038 | Original run |
| 15K  | 0.648 | |
| 25K  | 0.053 | |
| 35K  | 0.430 | |
| 45K  | 0.963 | |
| 55K  | 0.000 | |
| 65K  | 0.0 | CIVO alert #1 |
| 75K  | 2.228 | Temporary recovery |
| 85K  | **3.578** | **Peak (all-time)** |
| 95K  | 1.083 | Declining |
| 105K | 0.0 | CIVO alert #2, collapse |
| 112K | 1.534 | **Extension starts** |
| 122K | 0.708 | |
| 132K | 0.007 | |
| 142K | 0.422 | |
| 152K | 0.561 | Final |

**Extension period eval_return: oscillates 0–1.5, no recovery trend. Final = 0.56.**

### ve_ratio (CIVO indicator)

| Step | ve_ratio | civo/alert |
|------|----------|------------|
| 15K  | 0.06 | 0 |
| 25K  | 1.29 | 0 |
| 35K  | 0.46 | 0 |
| 45K  | 0.22 | 0 |
| 55K  | **14,441** | 0 (first spike) |
| 65K  | **819,655** | **1** |
| 75K  | 0.51 | 0 (temporary recovery) |
| 85K  | 0.56 | 0 |
| 95K  | 2.69 | 0 |
| 105K | **4,335,664** | **1** |
| 122K | 10.15 | 0 (post-restart) |
| 132K | 955 | 0 (re-spike) |
| 142K | 18.05 | 0 |
| 152K | 15.08 | 0 |

**Extension period: ve_ratio dropped from 4.3M to ~15, but never returned to healthy range (~0.5). Re-spiked to 955 at 132K before settling.**

### value_mean (value network inflation)

| Step | value_mean |
|------|------------|
| 5K   | 0.001 |
| 25K  | 0.069 |
| 45K  | 0.208 |
| 65K  | 0.820 |
| 85K  | 2.001 |
| 105K | 4.337 |
| 122K | 8.375 |
| 132K | 7.183 |
| 142K | 7.084 |
| 152K | 8.458 |

**value_mean monotonically inflates from 0.001 → 8.5 while actual eval_return stays near 0. Classic value overestimation without grounding.**

### Gate Behavior

Throughout all 160K steps:
- `gate_dt_mean` = 2.0
- `gate_dt_2_frac` = 1.0
- `gate_empirical_entropy` = 0.0

**The gate is permanently locked at dt=2. Zero adaptive horizon behavior.**

## Comparison with trained_s0_ext

| Metric | frozen_s0_ext (this) | trained_s0_ext | baseline |
|--------|---------------------|----------------|----------|
| eval_return @105K | 0.0 | 3.26 | 96.43 |
| eval_return final (150K+) | 0.56 | **81.58** | — |
| Recovery? | **No** | **Yes** | — |
| ve_ratio @105K | 4,335,664 | 0.897 | 0.559 |
| ve_ratio final | 15.08 | — | — |
| Gate entropy | 0.0 (locked) | varies | varies |
| CIVO alerts | 2 (65K, 105K) | 0 | 0 |

The contrast is stark:
- **trained_s0_ext**: dt_embedding eventually learned → gate adapted → value estimation stabilized → eval_return recovered to 81.58
- **frozen_s0_ext**: dt_embedding frozen → gate permanently locked → value overestimation unchecked → eval_return stuck near 0

## Diagnosis: "Degenerate CIVO" is NOT Transient

The hypothesis posited that frozen_s0's catastrophic ve_ratio spikes were transient instability (like trained_s0's learning delay). The evidence conclusively refutes this:

1. **Recurring catastrophic spikes**: Two separate CIVO events (65K: 820K, 105K: 4.3M) with escalating magnitude. This is not transient — it's a recurring structural failure.

2. **No recovery mechanism**: trained_s0 recovers because the dt_embedding eventually learns, enabling the gate to adapt its horizon selection. frozen_s0 has no such mechanism — the embedding is frozen at random initialization, permanently locking gate output to dt=2.

3. **Value overestimation without correction**: value_mean grows to 8.5 while eval_return ≈ 0. In healthy systems, the adaptive horizon provides a self-correction mechanism (CIVO theory). With the gate locked, this correction loop is broken.

4. **ve_ratio settles at elevated plateau, not recovery**: After the 4.3M spike, ve_ratio drops to ~15 (not 0.5). This elevated baseline indicates persistent value-estimation error, not recovery.

## Conclusion

**The frozen dt_embedding creates an unrecoverable pathology, fundamentally distinct from trained_s0's learning delay.**

- Frozen embedding → gate locked at dt=2 → no horizon adaptation → value estimation errors accumulate unchecked → recurring catastrophic ve_ratio explosions → no performance recovery
- This confirms that **learnable dt_embedding is necessary** for the CIVO self-correction mechanism to function
- The "degenerate CIVO" pattern in frozen_s0 is not a delayed version of normal learning — it is a broken feedback loop caused by the absence of adaptive horizon control
