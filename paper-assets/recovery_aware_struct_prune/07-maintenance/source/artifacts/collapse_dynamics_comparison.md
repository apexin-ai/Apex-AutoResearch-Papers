# Collapse Dynamics Comparison (2026-05-17)

## Summary

| Run | Step Observed | frac_zero_std | reward | grad_norm | Collapse Status |
|-----|--------------|---------------|--------|-----------|-----------------|
| **grpo_random_20** | 30 | 0.325 | 0.1663 | 3.672 | **NO COLLAPSE** |
| **grpo_cka_only_20** | 20 | 0.200 | 0.2181 | 1.250 | **NO COLLAPSE** |
| grpo_stage2_rasp_20_v9 | 10 | 0.875 | 0.015 | 0.007 | **IMMEDIATE COLLAPSE** |
| grpo_stage2_standard_20_v8 | 60 | 0.525 | 0.041 | 0.013 | **PARTIAL (grad collapse at step 60)** |

## Detailed Metrics

### grpo_random_20 (running, step 30/100)

| Step | reward | frac_zero_std | grad_norm | loss | mean_length | entropy |
|------|--------|---------------|-----------|------|-------------|---------|
| 10 | 0.1606 | 0.300 | 3.750 | -0.02128 | 341.5 | 0.2313 |
| 20 | 0.1419 | 0.325 | 8.625 | -0.03658 | 387.1 | 0.2282 |
| 30 | 0.1663 | 0.325 | 3.672 | 0.00272 | 433.9 | 0.2353 |

Interpretation: Stable training. Reward recovering at step 30 after dip at step 20. frac_zero_std flat at 0.3, entropy high (0.23), grad_norm active. No collapse signal.

### grpo_cka_only_20 (running, step 21/100)

| Step | reward | frac_zero_std | grad_norm | loss | mean_length | entropy |
|------|--------|---------------|-----------|------|-------------|---------|
| 10 | 0.2531 | 0.175 | 1.891 | 0.03907 | 500.5 | 0.08297 |
| 20 | 0.2181 | 0.200 | 1.250 | 0.1502 | 515.7 | 0.07487 |

Interpretation: Best reward and lowest frac_zero_std of all runs. However, concerning signals: grad_norm declining (1.89 -> 1.25), loss rising rapidly (0.039 -> 0.150), entropy very low (0.08 vs 0.23 for Random). Low entropy suggests less exploration, which could lead to eventual mode collapse.

### grpo_stage2_rasp_20_v9 (finished, 30 steps total)

| Step | reward | frac_zero_std | grad_norm | loss | mean_length |
|------|--------|---------------|-----------|------|-------------|
| 10 | 0.015 | 0.875 | 0.007 | 0.00694 | 991.4 |
| 20 | 0.039 | 0.800 | 0.008 | -0.00259 | 1010.0 |
| 30 | 0.021 | 0.950 | 1.398 | 0.00686 | 995.8 |

Interpretation: Collapsed from the very first step. frac_zero_std=0.875 at step 10, completions near max length (1024) with near-zero reward. The SFT-RASP-20 checkpoint entered GRPO already in a degenerate state. Not "collapse at step 10" but "entered already collapsed."

### grpo_stage2_standard_20_v8 (crashed at ~step 90)

| Step | reward | frac_zero_std | grad_norm | loss | mean_length |
|------|--------|---------------|-----------|------|-------------|
| 10 | 0.058 | 0.500 | 2.906 | 0.0599 | 749 |
| 20 | 0.061 | 0.675 | 1.586 | 0.0556 | 762 |
| 30 | 0.065 | 0.525 | 2.281 | 0.0817 | 705 |
| 40 | 0.096 | 0.450 | 3.453 | 0.0827 | 674 |
| 50 | 0.037 | 0.600 | 2.094 | 0.0583 | 760 |
| 60 | 0.041 | 0.525 | **0.013** | 0.0805 | 724 |
| 70 | 0.081 | 0.500 | 2.812 | 0.0776 | 762 |
| 80 | 0.045 | 0.550 | 2.312 | 0.0593 | 692 |
| 90 | 0.065 | 0.475 | 2.141 | 0.0898 | 721 |

Interpretation: Not a full collapse (frac_zero_std stays 0.45-0.675), but reward stuck in 0.04-0.10 range with no upward trend. Gradient briefly collapsed at step 60 (grad_norm drops to 0.013) but recovered. "Stuck" pattern rather than outright collapse.

## Key Judgments

### 1. grpo_random_20 at step 30: NOT collapsed
- frac_zero_std = 0.325 (threshold: 0.8)
- reward = 0.1663 (higher than both reference runs at any point)
- grad_norm = 3.67 (active)
- Verdict: Healthy training, significantly outperforming RASP v9 and Standard v8

### 2. grpo_cka_only_20 at step 21: NOT collapsed
- frac_zero_std = 0.200 (best diversity of all runs)
- reward = 0.218 (highest of all runs)
- grad_norm = 1.25 (declining but still active)
- Risk factors: low entropy (0.075), rising loss (0.15), declining grad_norm
- Verdict: Currently healthy and best-performing, but needs monitoring for potential late collapse

### 3. Collapse Ordering (C2 gradient)

```
RASP v9:     ████████████████ collapsed from step 0 (frac_zero_std=0.875 at first log)
Standard v8: ░░░░░░████░░░░░ stuck/partial (frac_zero_std 0.5-0.7, grad collapse at step 60)
Random:      ░░░░░░░░░░░░░░░ no collapse through step 30 (frac_zero_std=0.325)
CKA-only:    ░░░░░░░░░░░░░░░ no collapse through step 21 (frac_zero_std=0.200)
```

Relative to reference:
- Random and CKA-only are **dramatically better** than RASP v9 (which never trained)
- Random and CKA-only are **better** than Standard v8 (stuck at reward 0.04-0.10)
- Random maintains higher entropy/exploration (0.23 vs CKA-only's 0.08)
- CKA-only has higher reward but lower entropy: different risk profiles

### 4. Projection

- **Random**: At current trajectory (frac_zero_std flat at 0.32, high entropy), unlikely to collapse before step 60+. Starting from a much higher reward baseline than Standard v8.
- **CKA-only**: Higher immediate reward but lower entropy is a risk factor. If entropy continues declining, may see issues around step 40-60. Very low frac_zero_std (0.2) provides margin.

## Corrections to Prior Assumptions

- RASP v9's "collapse at step ~10" is actually "already collapsed when GRPO started." The SFT checkpoint was degenerate before RL.
- Standard v8's "collapse at step ~60" is a transient gradient collapse (grad_norm 0.013) within an otherwise stuck-but-not-dead training run. frac_zero_std never exceeds 0.675.
- New runs (Random, CKA-only) use 100 total steps vs 250 for older runs, with different hyperparameters.
