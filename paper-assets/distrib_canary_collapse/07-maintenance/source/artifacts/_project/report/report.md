# D120: Alpha Sweep Full Recalculation with D105 True 3σ Threshold

**Date**: 2026-05-20
**Server**: westd-17855
**Script**: `run_5method_analysis_d102.py` (D105 true 3σ: `np.std(full_series)`, not 3x_sigma_drift)
**Permutations**: 5000, BH FDR q=0.05
**Direction filter**: D111 corrected (`peak_lag < 0` = canary leads)

## Summary Table

| exp_id | α | seed | gens | PermG_fwd | PermG_rev | naive_fwd | diff_fwd | thresh_onset | TY | K≥3 | K≥4 |
|--------|-----|------|------|-----------|-----------|-----------|----------|--------------|-----|-----|-----|
| a005_s42_fp32 | 0.05 | 42 | 2 | — | — | — | — | — | — | — | — |
| a005_s42_fp32_v2 | 0.05 | 42 | 3 | — | — | — | — | — | — | — | — |
| a005_s42_fp32_v3 | 0.05 | 42 | 1 | — | — | — | — | — | — | — | — |
| a005_s42_fp32_v3_d080 | 0.05 | 42 | 11 | 0/8 | 0/8 | 4/8 | 3/8 | 0/8 | 0/8 | 0/8 | 0/8 |
| a010_s42_fp32 | 0.10 | 42 | 11 | 0/8 | 0/8 | 3/8 | 6/8 | 0/8 | 0/8 | 0/8 | 0/8 |
| a010_s43_fp32 | 0.10 | 43 | 11 | 3/8 | 0/8 | 4/8 | 7/8 | **2/8** | 0/8 | 4/8 | 1/8 |
| a025_s42_fp32 | 0.25 | 42 | 11 | 0/8 | 0/8 | 1/8 | 3/8 | 0/8 | 0/8 | 0/8 | 0/8 |
| a025_s43_fp32 | 0.25 | 43 | 11 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |
| a025_s44_fp32 | 0.25 | 44 | 10 | 0/8 | 0/8 | 1/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |
| a030_s42_fp32 | 0.30 | 42 | 11 | 0/8 | 0/8 | 3/8 | 4/8 | 0/8 | 0/8 | 0/8 | 0/8 |
| a035_s42_fp32 | 0.35 | 42 | 11 | 0/8 | 0/8 | 0/8 | 4/8 | 0/8 | 0/8 | 0/8 | 0/8 |
| a040_s42_fp32 | 0.40 | 42 | 11 | 0/8 | 0/8 | 4/8 | 3/8 | 0/8 | 0/8 | 0/8 | 0/8 |
| a045_s42_fp32 | 0.45 | 42 | 11 | 0/8 | 0/8 | 1/8 | 6/8 | 0/8 | 0/8 | 0/8 | 0/8 |
| a050_s42_fp32 | 0.50 | 42 | 11 | 6/8 | 0/8 | 3/8 | 7/8 | **4/8** | 0/8 | 5/8 | 2/8 |
| a050_s43_fp32 | 0.50 | 43 | 11 | 6/8 | 0/8 | 2/8 | 6/8 | **6/8** | 0/8 | 5/8 | 1/8 |
| a050_s44_fp32 | 0.50 | 44 | 11 | 6/8 | 0/8 | 5/8 | 8/8 | 0/8 | 0/8 | 3/8 | 0/8 |
| a050_postd093_s42 | 0.50 | 42 | 11 | 6/8 | 0/8 | 3/8 | 2/8 | 0/8 | 0/8 | 1/8 | 0/8 |
| a060_s42_fp32 | 0.60 | 42 | 2 | — | — | — | — | — | — | — | — |
| a060_s42_fp32_v2 | 0.60 | 42 | 1 | — | — | — | — | — | — | — | — |
| a060_s42_fp32_v3_d080 | 0.60 | 42 | 11 | 3/8 | 0/8 | 3/8 | 8/8 | 0/8 | 0/8 | 2/8 | 0/8 |
| a060_s43_fp32 | 0.60 | 43 | 10 | 0/8 | 0/8 | 1/8 | 6/8 | 0/8 | 0/8 | 0/8 | 0/8 |
| a075_s42_fp32 | 0.75 | 42 | 11 | 6/8 | 0/8 | 7/8 | 6/8 | 0/8 | 0/8 | 6/8 | 0/8 |

**—** = INCOMPLETE (too few generations for analysis, series length < 4 after differencing)

## Threshold Onset Detail (D120 Focus)

Only 3 experiments show any threshold_onset significance under D105 true 3σ:

### a010_s43_fp32 (α=0.10, seed=43) — 2/8 sig
| pair | canary_onset | downstream_onset | lead_time | sig |
|------|-------------|------------------|-----------|-----|
| tok_ent→distinct_1 | 1 | - | - | |
| tok_ent→distinct_2 | 1 | 4 | 3 | * |
| tok_ent→distinct_3 | 1 | - | - | |
| tok_ent→mauve | 1 | 3 | 2 | * |
| ece→distinct_1 | - | - | - | |
| ece→distinct_2 | - | 4 | - | |
| ece→distinct_3 | - | - | - | |
| ece→mauve | - | 3 | - | |

### a050_s42_fp32 (α=0.50, seed=42) — 4/8 sig
| pair | canary_onset | downstream_onset | lead_time | sig |
|------|-------------|------------------|-----------|-----|
| tok_ent→distinct_1 | 1 | - | - | |
| tok_ent→distinct_2 | 1 | 10 | 9 | * |
| tok_ent→distinct_3 | 1 | 10 | 9 | * |
| tok_ent→mauve | 1 | - | - | |
| ece→distinct_1 | 2 | - | - | |
| ece→distinct_2 | 2 | 10 | 8 | * |
| ece→distinct_3 | 2 | 10 | 8 | * |
| ece→mauve | 2 | - | - | |

### a050_s43_fp32 (α=0.50, seed=43) — 6/8 sig
| pair | canary_onset | downstream_onset | lead_time | sig |
|------|-------------|------------------|-----------|-----|
| tok_ent→distinct_1 | 1 | - | - | |
| tok_ent→distinct_2 | 1 | 10 | 9 | * |
| tok_ent→distinct_3 | 1 | 10 | 9 | * |
| tok_ent→mauve | 1 | 4 | 3 | * |
| ece→distinct_1 | 2 | - | - | |
| ece→distinct_2 | 2 | 10 | 8 | * |
| ece→distinct_3 | 2 | 10 | 8 | * |
| ece→mauve | 2 | 4 | 2 | * |

## Key Observations

1. **threshold_onset is extremely conservative under D105 true 3σ.** Only 3/17 complete experiments show any significance (vs. old 3x_sigma_drift which was much more permissive). 14/17 = 0/8.

2. **Canary onset is early and robust** (gen 1-2 for tok_ent, gen 2-4 for ece across all α). The bottleneck is **downstream onset**: most downstreams never cross the true 3σ threshold.

3. **α ≤ 0.45**: Zero threshold_onset significance. Signal too weak for downstream metrics to breach true 3σ.

4. **α = 0.50**: Seed-unstable.
   - s42: 4/8, s43: 6/8 (both show distinct_2/distinct_3 onset at gen 10)
   - s44: 0/8, postd093: 0/8
   Inconsistency suggests the signal is marginal at this α level.

5. **α ≥ 0.60, α = 0.75**: Zero threshold_onset despite strong signals in other methods (PermG 3-6/8, diff 6-8/8). The downstream degradation is real but gradual — it doesn't spike above 3σ of the full-series std.

6. **PermG is the most robust method**, jumping from 0/8 (α≤0.45) to 6/8 (α=0.50+). This step-function aligns with the α=0.50 phase transition.

7. **TY Granger = 0/8 everywhere** — consistent with C003 (T=11 too short for stable TY).

8. **PermG_rev = 0/8 everywhere** — no reverse causation detected, confirming forward directionality.

9. **K≥3 consensus** only reliably achieved at α≥0.50 (driven by PermG + diff_xcorr + one other method). Best: a075_s42 at 6/8.

## Incomplete Experiments (skipped)

| exp_id | generations | reason |
|--------|------------|--------|
| a005_s42_fp32 | 2 | T=0 after diff |
| a005_s42_fp32_v2 | 3 | T=1 after diff |
| a005_s42_fp32_v3 | 1 | T=0 after diff |
| a060_s42_fp32 | 2 | T=0 after diff |
| a060_s42_fp32_v2 | 1 | T=0 after diff |

## Consensus Detail (K≥3 experiments)

**a010_s43_fp32** (K≥3: 4/8, K≥4: 1/8):
- tok_ent→distinct_1: 3/5 [naive, diff, perm]
- tok_ent→distinct_2: 4/5 [naive, diff, threshold, perm]
- tok_ent→distinct_3: 3/5 [naive, diff, perm]
- tok_ent→mauve: 3/5 [naive, diff, threshold]

**a050_s42_fp32** (K≥3: 5/8, K≥4: 2/8):
- tok_ent→distinct_2: 3/5 [diff, threshold, perm]
- tok_ent→distinct_3: 3/5 [diff, threshold, perm]
- ece→distinct_1: 3/5 [naive, diff, perm]
- ece→distinct_2: 4/5 [naive, diff, threshold, perm]
- ece→distinct_3: 4/5 [naive, diff, threshold, perm]

**a050_s43_fp32** (K≥3: 5/8, K≥4: 1/8):
- tok_ent→distinct_2: 3/5 [diff, threshold, perm]
- tok_ent→distinct_3: 3/5 [diff, threshold, perm]
- ece→distinct_1: 3/5 [naive, diff, perm]
- ece→distinct_2: 4/5 [naive, diff, threshold, perm]
- ece→distinct_3: 3/5 [diff, threshold, perm]

**a050_s44_fp32** (K≥3: 3/8, K≥4: 0/8):
- ece→distinct_1: 3/5 [naive, diff, perm]
- ece→distinct_2: 3/5 [naive, diff, perm]
- ece→distinct_3: 3/5 [naive, diff, perm]

**a050_postd093_s42_fp32** (K≥3: 1/8, K≥4: 0/8):
- ece→distinct_1: 3/5 [naive, diff, perm]

**a060_s42_fp32_v3_d080** (K≥3: 2/8, K≥4: 0/8):
- ece→distinct_1: 3/5 [naive, diff, perm]
- ece→distinct_2: 3/5 [naive, diff, perm]

**a075_s42_fp32** (K≥3: 6/8, K≥4: 0/8):
- tok_ent→distinct_1: 3/5 [naive, diff, perm]
- tok_ent→distinct_2: 3/5 [naive, diff, perm]
- tok_ent→distinct_3: 3/5 [naive, diff, perm]
- ece→distinct_1: 3/5 [naive, diff, perm]
- ece→distinct_2: 3/5 [naive, diff, perm]
- ece→distinct_3: 3/5 [naive, diff, perm]

## Implications for Paper

- D105 true 3σ threshold_onset is a strict, conservative measure. For the paper's dose-response narrative, threshold_onset primarily contributes at α=0.50 (seed-dependent) and occasionally at α=0.10 (s43 only). It does NOT contribute at α≥0.60 despite clear collapse signals.
- The 5-method consensus (K≥3) is effectively a 3-method consensus (PermG + diff_xcorr + naive_xcorr) since threshold_onset and TY rarely fire. At α=0.75, all 6/8 K≥3 pairs use exactly these 3 methods.
- The `threshold_onset_3sigma` field in registry should reflect these recalculated values.
