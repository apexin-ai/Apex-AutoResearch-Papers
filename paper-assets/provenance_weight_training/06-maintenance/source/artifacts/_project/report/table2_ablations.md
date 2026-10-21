## Table 2: Ablations (ρ=0.4, seed42)

### n_min Sweep

| Setting | PPL | Δ vs default | Notes |
|---------|-----|--------------|-------|
| n_min=1 | 17.789 | +0.136 | nmin1_seed42 |
| n_min=2 (default) | 17.653 | 0.000 | adaptive_fix_seed42 |
| n_min=3 | 17.644 | -0.009 | adaptive_seed42 |
| n_min=4 | 17.695 | +0.042 | nmin4_seed42 |

### τ Sweep

| Setting | PPL | Δ vs default | Notes |
|---------|-----|--------------|-------|
| τ=0.5 | 17.688 | +0.035 | tau_05_seed42 |
| τ=0.6 | 17.681 | +0.028 | tau_06_seed42 |
| τ=0.7 | 17.679 | +0.027 | tau_07_seed42 |
| τ=0.8 (default) | 17.653 | 0.000 | adaptive_fix_seed42 |
| τ=0.9 | 17.712 | +0.059 | tau_09_seed42; **NEGATIVE** |
| τ=0.95 | 17.723 | +0.070 | tau_095_seed42; **NEGATIVE** |

### Batch Size

| Setting | PPL | Δ vs default | Notes |
|---------|-----|--------------|-------|
| bs=8 | 17.730 | +0.077 | bs8_nmin2_seed42_r2; **NEGATIVE** |

**Notes:**
- Default = adaptive_fix_seed42 (n_min=2, τ=0.8, bs=4), PPL=17.653
- Negative Δ = better than default
- NEGATIVE = conclusion marked negative in registry
