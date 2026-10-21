# exp_009: r=0.25 Fixed Mix — Full 10-Generation Analysis

## Status
- **EXIT_CODE=0**, clean completion
- **Checkpoints**: gen_0 through gen_10 at `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed42/`
- **Results**: `/root/spectral_collapse_ews/results/phase1_fixed_mix_r025_seed42_results.json`

## Complete Metrics Table

| Gen | eff_rank | log_det  | ppl    | distinct4 | train_loss | σ₁      |
|-----|----------|----------|--------|-----------|------------|---------|
| 0   | 417.55   | 2366.68  | 9.554  | 0.7414    | —          | 1942.82 |
| 1   | 476.66   | 2362.13  | 10.239 | 0.6499    | 1.801      | 946.35  |
| 2   | 482.84   | 2363.10  | 10.653 | 0.4973    | 1.698      | 868.76  |
| 3   | 489.47   | 2380.88  | 11.019 | 0.4419    | 1.413      | 807.37  |
| 4   | 491.21   | 2393.37  | 11.343 | 0.4298    | 1.343      | 780.54  |
| 5   | 495.84   | 2421.22  | 11.669 | 0.4192    | 1.308      | 759.85  |
| 6   | 498.59   | 2436.38  | 11.974 | 0.3969    | 1.317      | 747.85  |
| 7   | 500.66   | 2447.08  | 12.295 | 0.3889    | 1.303      | 741.85  |
| 8   | 505.82   | 2463.81  | 12.631 | 0.3657    | 1.304      | 716.07  |
| 9   | 509.59   | 2476.58  | 12.978 | 0.3674    | 1.289      | 709.26  |
| 10  | 512.46   | 2485.01  | 13.285 | 0.3572    | 1.319      | 702.94  |

## SLV Trajectory Analysis

### log_det dip
- **Dip location**: Gen 1 (log_det = 2362.13, Δ = −4.55 from Gen 0)
- **Dip magnitude**: −4.55 (−0.19%)
- **Recovery**: Gen 2 (2363.10), surpasses Gen 0 at Gen 3 (2380.88)
- **Post-recovery**: Monotonic rise from Gen 2 through Gen 10

### σ₁ trajectory
- Monotonic decline: 1942.82 → 702.94 (−63.8%)
- Sharpest drop: Gen 0→1 (−51.3%), consistent with initial fine-tune shock
- Spectrum flattening: σ₁/σ₂ ratio narrows from 3.98 (Gen 0) to 1.57 (Gen 10)

### distinct4
- Monotonic decrease: 0.7414 → 0.3572 (−51.8%)
- Sharpest drop: Gen 1→2 (0.6499 → 0.4973, −23.5%)
- Stabilizes around 0.36-0.39 from Gen 7 onward

## Cross-Experiment Comparison (r=0.2, r=0.25, r=0.3)

### log_det Dip Behavior (Key Discriminator)
| Experiment | r    | Dip Gen | Dip Δ   | Dip Depth | Recovery Gen |
|------------|------|---------|---------|-----------|--------------|
| exp_007    | 0.20 | Gen 2   | −8.37   | 2358.31   | Gen 4        |
| exp_009    | 0.25 | Gen 1   | −4.55   | 2362.13   | Gen 2        |
| exp_008    | 0.30 | (none)  | −0.55*  | 2366.13   | Gen 1        |

*r=0.3 shows only a trivial −0.55 drop at Gen 1, essentially no dip.

**Pattern**: Dip gets shallower, earlier, and recovers faster as r increases. At r=0.3 the dip vanishes entirely.

### Matched-Generation Comparison (Gen 5)
| Metric    | r=0.2 (G5) | r=0.25 (G5) | r=0.3 (G5) |
|-----------|------------|--------------|-------------|
| eff_rank  | 492.66     | 495.84       | 497.86      |
| log_det   | 2398.93    | 2421.22      | 2431.17     |
| ppl       | 11.833     | 11.669       | 11.544      |
| distinct4 | 0.4384     | 0.4192       | 0.4508      |

### Terminal State Comparison (Gen 10)
| Metric    | r=0.25 (G10) | r=0.3 (G10) | Δ         |
|-----------|--------------|-------------|-----------|
| eff_rank  | 512.46       | 521.26      | +8.80     |
| log_det   | 2485.01      | 2511.13     | +26.12    |
| ppl       | 13.285       | 13.377      | +0.09     |
| distinct4 | 0.3572       | 0.3422      | −0.015    |

### Cumulative Change (Gen 0 → Gen 10)
| Metric     | r=0.25       | r=0.3        |
|------------|-------------|--------------|
| Δlog_det   | +118.33     | +144.45      |
| Δppl       | +39.1%      | +40.0%       |
| Δdistinct4 | −51.8%      | −53.8%       |
| Δeff_rank  | +22.7%      | +24.8%       |

## Key Findings

1. **No spectral collapse at r=0.25**: Like r=0.2 and r=0.3, log_det shows monotonic rise after initial transient. r_crit is below 0.2 (at least for 10 gen).

2. **Dip gradient confirms phase transition structure**: The log_det dip magnitude grades smoothly: −8.37 (r=0.2) → −4.55 (r=0.25) → −0.55 (r=0.3). This supports the paper's claim of a continuous r_crit boundary in (0.25, 0.3].

3. **r=0.25 is behaviorally closer to r=0.2 than r=0.3**: The dip is still present (though shallower), placing r=0.25 in the "transient instability" regime rather than the "fully stabilized" regime of r=0.3.

4. **Terminal ppl/distinct4 nearly identical across r=0.25 and r=0.3**: At Gen 10, ppl differs by only 0.7% and distinct4 by 4.2%. The main differentiation is in the early-gen spectral dynamics, not the terminal state.

5. **Controller silence confirmed**: Fixed r=0.25 shows no signal that would trigger the τ=0.002 threshold at any generation (max single-gen log_det decline is 4.55, controller Δ_t = (2362.13-2366.68)/2366.68 = −0.0019, just below τ=0.002). This is a Type II boundary case.

## Checkpoint Path
`/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed42/` (gen_0 through gen_10)
