# RankMe (Effective Rank) Trajectory Analysis

## Per-Experiment r_eff Trajectories

### r = 0 (pure synthetic collapse)

| Gen | exp_001 (s42) | exp_010 (s43) | exp_013 (s44) | **Mean** |
|-----|---------------|---------------|---------------|----------|
| 0   | 417.55        | 417.55        | 417.55        | **417.55** |
| 1   | 491.77        | 490.83        | 490.77        | **491.12** |
| 2   | 496.44        | 496.24        | 495.83        | **496.17** |
| 3   | 493.31        | 494.04        | 493.45        | **493.60** |
| 4   | 485.67        | 489.23        | 488.35        | **487.75** |
| 5   | 479.21        | 480.07        | 480.04        | **479.77** |
| 6   | 473.00        | 471.88        | 472.30        | **472.39** |
| 7   | 464.20        | 464.18        | 463.93        | **464.10** |
| 8   | 456.76        | 456.18        | 454.56        | **455.83** |
| 9   | 448.45        | 447.02        | 444.33        | **446.60** |
| 10  | 442.46        | 438.78        | 432.91        | **438.05** |

### r = 0.2

| Gen | exp_011 (s42) | exp_017 (s43) | **Mean** |
|-----|---------------|---------------|----------|
| 0   | 417.55        | 417.55        | **417.55** |
| 1   | 476.73        | 475.29        | **476.01** |
| 2   | 481.62        | 480.44        | **481.03** |
| 3   | 486.54        | 487.00        | **486.77** |
| 4   | 490.35        | 489.33        | **489.84** |
| 5   | 492.65        | 492.09        | **492.37** |
| 6   | 496.42        | 495.85        | **496.14** |
| 7   | 496.24        | 498.05        | **497.15** |
| 8   | 501.49        | 500.80        | **501.15** |
| 9   | 504.86        | 504.08        | **504.47** |
| 10  | 511.26        | 505.98        | **508.62** |

Note: exp_019 (s44) is RUNNING — not yet included. exp_007 only ran 5 gens; exp_011 is the full 10-gen continuation.

### r = 0.25

| Gen | exp_009 (s42) | exp_015 (s44) | **Mean** |
|-----|---------------|---------------|----------|
| 0   | 417.55        | 417.55        | **417.55** |
| 1   | 476.66        | 475.92        | **476.29** |
| 2   | 482.84        | 484.39        | **483.62** |
| 3   | 489.47        | 488.62        | **489.05** |
| 4   | 491.21        | 493.01        | **492.11** |
| 5   | 495.84        | 494.32        | **495.08** |
| 6   | 498.59        | 498.74        | **498.67** |
| 7   | 500.66        | 502.71        | **501.69** |
| 8   | 505.82        | 504.20        | **505.01** |
| 9   | 509.59        | 510.29        | **509.94** |
| 10  | 512.46        | 513.44        | **512.95** |

Note: exp_014b (s43) completed but only has gen0/1/2/10 in registry (gen10=515.56). Excluded from mean due to missing intermediate gens.

### r = 0.3

| Gen | exp_008 (s42) | exp_012 (s43) | exp_016 (s44) | **Mean** |
|-----|---------------|---------------|---------------|----------|
| 0   | 417.55        | 417.55        | 417.55        | **417.55** |
| 1   | 476.91        | 476.75        | 476.91        | **476.86** |
| 2   | 484.17        | 483.02        | 484.43        | **483.87** |
| 3   | 489.48        | 489.31        | 490.15        | **489.65** |
| 4   | 492.59        | 494.15        | 494.35        | **493.70** |
| 5   | 497.86        | 498.80        | 496.99        | **497.88** |
| 6   | 501.63        | 502.00        | 502.01        | **501.88** |
| 7   | 506.30        | 505.90        | 506.72        | **506.31** |
| 8   | 511.71        | 510.97        | 511.33        | **511.34** |
| 9   | 515.92        | 516.45        | 517.18        | **516.52** |
| 10  | 521.26        | 521.19        | 520.89        | **521.11** |

### r = 0.5

| Gen | exp_004 (s42) |
|-----|---------------|
| 0   | 417.55        |
| 1   | 477.89        |
| 2   | 487.92        |
| 3   | 496.57        |
| 4   | 502.05        |
| 5   | 512.78        |
| 6   | 519.78        |
| 7   | 527.47        |
| 8   | 536.39        |
| 9   | 545.73        |
| 10  | 554.51        |

## Summary Table (Mean r_eff across seeds)

| Gen | r=0     | r=0.2   | r=0.25  | r=0.3   | r=0.5   |
|-----|---------|---------|---------|---------|---------|
| 0   | 417.55  | 417.55  | 417.55  | 417.55  | 417.55  |
| 1   | 491.12  | 476.01  | 476.29  | 476.86  | 477.89  |
| 2   | 496.17  | 481.03  | 483.62  | 483.87  | 487.92  |
| 3   | 493.60  | 486.77  | 489.05  | 489.65  | 496.57  |
| 4   | 487.75  | 489.84  | 492.11  | 493.70  | 502.05  |
| 5   | 479.77  | 492.37  | 495.08  | 497.88  | 512.78  |
| 6   | 472.39  | 496.14  | 498.67  | 501.88  | 519.78  |
| 7   | 464.10  | 497.15  | 501.69  | 506.31  | 527.47  |
| 8   | 455.83  | 501.15  | 505.01  | 511.34  | 536.39  |
| 9   | 446.60  | 504.47  | 509.94  | 516.52  | 545.73  |
| 10  | 438.05  | 508.62  | 512.95  | 521.11  | 554.51  |
| **Δ(0→10)** | **+20.50** | **+91.07** | **+95.40** | **+103.56** | **+136.96** |
| **Peak gen** | **Gen 2** | **Gen 10** | **Gen 10** | **Gen 10** | **Gen 10** |

## Phase Diagram Comparison: r_eff vs SLV

### SLV classification (from paper)
- **Type I** (r=0): Unbounded collapse — SLV peaks at Gen 2 then monotonically declines
- **Type II** (r=0.2): Transient dip — SLV dips at Gen 2 (Δ≈−8) then recovers and rises
- **Type III** (r≥0.25): Monotonic expansion — SLV rises from Gen 1 onward

### r_eff classification
- **r=0**: Peak at Gen 2 (496.17), then monotonic decline to 438.05. **Matches Type I.**
- **r=0.2**: Monotonic increase from Gen 1 (476.01) to Gen 10 (508.62). No dip. **Does NOT match Type II — looks identical to Type III.**
- **r=0.25**: Monotonic increase to 512.95. Same pattern as r=0.2.
- **r=0.3**: Monotonic increase to 521.11. Same pattern.
- **r=0.5**: Monotonic increase to 554.51. Strongest expansion.

### Key finding

**r_eff shows a 2-type phase diagram, not the 3-type structure of SLV.** The Type II / Type III boundary (r=0.2 vs r≥0.25) visible in SLV is invisible in r_eff. All mixing ratios r≥0.2 produce monotonic r_eff expansion; they differ only in rate (higher r → faster expansion). The Type I / non-collapse boundary is clearly visible: r=0 shows peak-then-decline, r≥0.2 shows sustained growth.

This supports the paper's argument that SLV (log-determinant) is a more sensitive early warning signal than RankMe (effective rank). SLV detects the transient instability at r=0.2 that r_eff completely misses. The r_eff metric only distinguishes "collapse" from "no collapse" but cannot resolve the intermediate regime where spectral structure is transiently stressed before stabilizing.

### Rate of expansion (Δr_eff per generation, Gen 2→10)

| r     | Δ/gen (mean) | Relative to r=0.5 |
|-------|-------------|-------------------|
| 0.0   | −7.27       | collapse           |
| 0.2   | +3.45       | 40%                |
| 0.25  | +3.67       | 43%                |
| 0.3   | +4.66       | 54%                |
| 0.5   | +8.32       | 100%               |

The expansion rate scales roughly linearly with mixing ratio for r≥0.2.
