# grpo_cka_only_20 Complete Training Metrics (westb-23072)

**Run**: CKA-only pruning (20% sparsity), GRPO training, 100 steps
**Status**: Step 94/100 (still running as of 2026-05-18)
**Log**: ~/runs/recovery_aware_struct_prune/grpo_cka_only_20.log
**Data source**: Parsed from training log metric dumps (every 10 steps)

## Metrics Table

| Step | Reward | frac_zero_std | grad_norm |
|------|--------|---------------|-----------|
| 10   | 0.2531 | 0.175         | 1.891     |
| 20   | 0.2181 | 0.200         | 1.250     |
| 30   | 0.2500 | 0.200         | 1.102     |
| 40   | 0.2344 | 0.350         | 0.984     |
| 50   | 0.3544 | 0.150         | 1.977     |
| 60   | 0.2994 | 0.200         | 3.750     |
| 70   | 0.3075 | 0.125         | 1.164     |
| 80   | 0.3419 | 0.250         | 2.672     |
| 90   | 0.2419 | 0.300         | 1.219     |

## Key Observations

- **Peak reward**: Step 50 (0.3544) and Step 80 (0.3419)
- **Best frac_zero_std** (lowest collapse): Step 70 (0.125)
- **Post-step-70 decline**: reward drops from 0.3075 (step 70) to 0.2419 (step 90), frac_zero_std rises from 0.125 to 0.300
- **grad_norm**: Generally stable (1.0-2.0), with spikes at step 60 (3.75) and step 80 (2.67)
- Step 40 shows a brief collapse episode (frac_zero_std=0.35) that recovers by step 50
