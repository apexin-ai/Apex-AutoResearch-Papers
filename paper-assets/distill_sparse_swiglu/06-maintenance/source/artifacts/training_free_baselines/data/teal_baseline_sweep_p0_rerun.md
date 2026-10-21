# TEAL Baseline Sweep Results (2026-05-16)
## Reviewer P0 Re-evaluation — Normalization Fix Verification

### Context
Reviewer flagged 50% TEAL PPL=23.31 vs 70% predictor-TEAL=17.91 as inconsistent.
This re-evaluation confirms all vanilla TEAL numbers are correct.

### Results (LLaMA 3.1 8B, WikiText-2, seq_len=2048, 32 calibration samples)

| Sparsity | Vanilla TEAL PPL | WINA PPL | Dense PPL |
|----------|-----------------|----------|-----------|
| 30%      | 10.97           | 11.45    | 6.12      |
| 50%      | 23.31           | 27.93    | 6.12      |
| 70%      | 100.11          | 137.24   | 6.12      |

### Key Finding
- 50% TEAL=23.31 is CONFIRMED correct (identical to previous run)
- PPL monotonically increases with sparsity (physically consistent)
- The "70% < 50%" paradox was a METHOD confusion:
  - 70% TEAL=17.91 was PREDICTOR-based TEAL (trained, from kl_sparsity70_s42_v2)
  - 50% TEAL=23.31 was VANILLA TEAL (training-free baseline)
  - Trained predictor dramatically outperforms vanilla TEAL, even at higher sparsity

### Updated Claim 1 Gap (KL Predictor vs Vanilla TEAL)
| Sparsity | KL Predictor PPL | Vanilla TEAL PPL | Gap (TEAL/KL) |
|----------|-----------------|------------------|---------------|
| ~28.5%   | 8.98            | 10.97            | 1.22x         |
| 50%      | 12.00 ± 0.07    | 23.31            | 1.94x         |
| 70%      | 17.91           | 100.11           | 5.59x         |

The KL predictor advantage grows dramatically with sparsity:
- At 30%: modest 22% improvement
- At 50%: nearly 2x improvement (headline claim holds)
- At 70%: over 5x improvement (the gap widens, not narrows)
