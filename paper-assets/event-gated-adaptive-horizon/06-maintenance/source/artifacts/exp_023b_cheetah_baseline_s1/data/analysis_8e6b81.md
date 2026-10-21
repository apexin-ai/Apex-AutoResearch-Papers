# exp_023b_cheetah_baseline_s1 Analysis

## Summary

| Item | Value |
|------|-------|
| Environment | Cheetah Run (DMC) |
| Method | Vanilla DreamerV3 (dt=1, no temporal embedding, no gate) |
| Seed | 1 |
| Total env steps | 212,000 |
| Training duration | ~5h 24m |
| FPS | 10.6-10.9 |
| Exit code | 0 (normal completion) |
| Checkpoint | `logdir/exp_023b_cheetah_baseline_s1/latest.pt` |
| W&B | Not logged |

## Eval Return Trajectory

| Step | eval_return |
|------|-------------|
| 5000 | 11.6 |
| 15000 | 38.8 |
| 25000 | 124.8 |
| 35000 | 257.5 |
| 45000 | 342.8 |
| 55000 | 235.8 |
| 65000 | 307.1 |
| 75000 | 410.6 |
| 85000 | 309.4 |
| 95000 | 456.6 |
| 105000 | 436.0 |
| 115000 | 506.4 |
| 125000 | 537.7 |
| 135000 | 542.3 |
| 145000 | 348.3 |
| 155000 | 558.4 |
| 165000 | 511.2 |
| 175000 | 546.9 |
| 185000 | 559.9 |
| 195000 | 572.9 |
| 205000 | 520.3 |

## Key Metrics

- **Final eval_return** (step 205k): 520.3
- **Peak eval_return** (step 195k): 572.9
- **Mean eval_return (last 5 evals, 165k-205k)**: 542.2
- **Final train_return** (step 212k, 4 episodes): 522.1, 629.4, 629.8, 618.1

## Loss Metrics (step 205k)

| Metric | Value |
|--------|-------|
| model_loss | 1.7 |
| value_loss | 0.7 |
| position_loss | 0.0 |
| velocity_loss | 0.1 |
| reward_loss | 0.5 |
| kl | 1.6 |
| actor_loss | -0.0 |
| model_grad_norm | 3.1 |

## Convergence Analysis

- **Learning phases**: Rapid initial learning (0-50k), mid-training consolidation (50k-125k), convergence plateau (125k-205k)
- **Variance**: Notable dips at steps 55k (235.8), 85k (309.4), 145k (348.3), consistent with eval noise over 10 episodes
- **Stability**: No collapse, no NaN, no divergence. Losses stable throughout late training.
- **Trend**: Slight upward trend in last 100k steps (mean ~530-550), not yet fully plateaued

## NVE Baseline Value

For NVE normalization (Cheetah Run, DreamerV3 dt=1):
- **Recommended baseline**: mean of last 5 evals = **542.2** (seed=1)
- Pending: seed=0 (exp_023a) for cross-seed average

## Notes

- Action space: Box(-1.0, 1.0, (6,), float32)
- Encoder: MLP only (position: 8 dims, velocity: 9 dims), no CNN
- CIVO metrics logged but alert=0.0 throughout (no value estimation issues)
- Total 212 training episodes collected (dataset size 106,000 transitions)
