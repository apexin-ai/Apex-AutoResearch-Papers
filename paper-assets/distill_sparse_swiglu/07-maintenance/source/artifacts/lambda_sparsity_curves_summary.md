# Lambda/Sparsity/Loss Curves Extraction Report

**Server file**: `/root/distill_sparse_swiglu/artifacts/lambda_sparsity_curves.json` (42KB)
**Extracted from**: wandb offline runs on westd-34887

## Runs Extracted

| Run | Target | Steps | Points | Source |
|-----|--------|-------|--------|--------|
| kl_30pct_s42 | 0.3 | 1000 | 109 | wandb `06u4phga` (kl_sparsity30_s42_v3) |
| kl_40pct_s42 | 0.4 | 1000 | 109 | wandb `51pvb0hh` (d030_kl40_uniform) |
| kl_50pct_s42 | 0.5 | 200 | 48 | wandb `fmgye9hu` (kl_normalized_quicktest) |
| kl_70pct_s42 | 0.7 | 1000 | 109 | wandb `9epth9zr` (kl_sparsity70_s42) |

All runs: LLaMA-3.1-8B, seed=42, kl_normalized loss, Gumbel-sigmoid relaxation, tau 1.0->0.1

## Per-Run Summary

### kl_30pct_s42 (target=0.3, lambda_max=5000)
- **Lambda final**: 5000 (saturated at cap)
- **Sparsity final**: 0.285 (within 0.015 of target)
- **Sparsity converge step**: ~110 (first enters target +/- 0.03)
- **KL final**: 0.165
- **Loss trend**: Decreasing with late-stage fluctuations (tau annealing effect)

### kl_40pct_s42 (target=0.4, lambda_max=5000)
- **Lambda final**: 625 (below cap)
- **Sparsity final**: 0.398 (within 0.002 of target)
- **Sparsity converge step**: ~1 (initial gate output ~0.4, near target already)
- **KL final**: 0.262
- **Loss trend**: Decreasing with late-stage uptick

### kl_50pct_s42 (target=0.5, lambda_max=1000)
- **Lambda final**: 8 (very low — target is easy to satisfy)
- **Sparsity final**: 0.504 (within 0.004 of target)
- **Sparsity converge step**: ~80
- **KL final**: 0.641
- **Loss trend**: KL increases as tau anneals (more binary masks = higher divergence)
- **Note**: Only 200 steps (quicktest). Full mvp_kl_norm_v2_s42 wandb data not on server.

### kl_70pct_s42 (target=0.7, lambda_max=1000)
- **Lambda final**: 1000 (saturated at cap)
- **Sparsity final**: 0.688 (within 0.012 of target)
- **Sparsity converge step**: ~40
- **KL final**: 0.609
- **Loss trend**: Decreasing with fluctuations

## Key Observations for Paper Figure

1. **Lambda dynamics**: Clear three-phase behavior:
   - Phase 1 (steps 1-10): Lambda adjusts rapidly (exponential growth/decay)
   - Phase 2 (steps 10-150): Lambda finds operating range
   - Phase 3 (150+): Lambda stabilizes or saturates

2. **Sparsity convergence**: All targets reached within ~100 steps. The 40% target converges fastest (initial gate bias ~0.4).

3. **Lambda magnitude reflects difficulty**: 
   - 50% target: lambda=8 (easiest — initial gate is 50/50)
   - 40% target: lambda=625
   - 30% target: lambda=5000 (hardest — must push gates far from initialization)
   - 70% target: lambda=1000

4. **Tau (temperature) annealing**: Linear 1.0->0.1 over training. Late-stage loss uptick is expected as masks become more binary.

## JSON Schema
```json
{
  "kl_30pct_s42": {
    "steps": [...],
    "loss": [...],        // KL divergence loss (= kl_raw for wandb runs, kl_loss for 50%)
    "kl_raw": [...],      // Raw KL divergence
    "lambda": [...],      // Lagrangian multiplier
    "sparsity": [...],    // Actual sparsity ratio (fraction of neurons pruned)
    "tau": [...],         // Gumbel-sigmoid temperature
    "constraint_loss": [...],  // |sparsity - target| penalty
    "config": { ... }
  }
}
```
