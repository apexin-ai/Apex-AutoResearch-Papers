## Table 3: Baselines & Grid Sweep (ρ=0.4, seed42)

### Baselines

| Method | PPL | Δ vs uniform | Notes |
|--------|-----|--------------|-------|
| Golden ratio | 17.654 | -0.040 | golden_ratio_seed42 |
| Detect & remove | RUNNING | — | RUNNING |

### Grid b Sweep

| b | PPL | Δ vs uniform | Notes |
|---|-----|--------------|-------|
| 0.1 | RUNNING | — | RUNNING |
| 0.3 | 17.640 | -0.054 | Independent run (grid_b0_3_seed42) |
| 0.5 | 17.651 | -0.043 | grid_b_seed42_batch |
| 1.0 | 17.692 | -0.002 | grid_b_seed42_batch |
| 1.5 | 17.718 | +0.024 | grid_b_seed42_batch |
| 2.0 | 17.741 | +0.047 | grid_b_seed42_batch |
| 3.0 | 17.774 | +0.080 | grid_b_seed42_batch |
| 5.0 | 17.818 | +0.124 | grid_b_seed42_batch |

**Notes:**
- Uniform baseline (seed42): PPL = 17.694
- Negative Δ = better than uniform
- Best grid point: b=0.3 (PPL=17.640, Δ=-0.054)
- Monotonic degradation as b increases past 0.5
