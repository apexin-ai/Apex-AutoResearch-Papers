# grpo_random_20 Complete Training Metrics (westb-23072)

**Run**: Random pruning (20% sparsity), GRPO training, 100 steps
**Status**: Step 97/100 (still running as of 2026-05-18)
**Log**: ~/runs/recovery_aware_struct_prune/grpo_random_20.log
**Data source**: Parsed from training log metric dumps (every 10 steps)

## Metrics Table

| Step | Reward | frac_zero_std | grad_norm |
|------|--------|---------------|-----------|
| 10   | 0.1606 | 0.300         | 3.750     |
| 20   | 0.1419 | 0.325         | 8.625     |
| 30   | 0.1663 | 0.325         | 3.672     |
| 40   | 0.1450 | 0.400         | 4.188     |
| 50   | 0.1750 | 0.300         | 4.750     |
| 60   | 0.1844 | 0.350         | 3.594     |
| 70   | 0.1900 | 0.300         | 7.094     |
| 80   | 0.1419 | 0.375         | 3.688     |
| 90   | 0.1725 | 0.325         | 7.531     |

## Key Observations

- **Peak reward**: Step 70 (0.190), very modest improvement over entire run
- **frac_zero_std**: Consistently high (0.30-0.40), indicating persistent reward collapse
- **grad_norm**: Highly unstable (3.5-8.6), much worse than CKA-only (1.0-3.8)
- **No meaningful learning**: Reward range 0.14-0.19 across all 90 steps, essentially flat
- Step 40 worst collapse (frac_zero_std=0.40), never fully recovers
