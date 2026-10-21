# Table 1: Provenance-Weighted Pre-training Results

All PPL values are eval_ppl_holdout on human-written holdout set (4,077,068 tokens).

## Main Results (Multi-seed)

| Method | Seed 42 | Seed 123 | Seed 456 | Mean | Std | Delta vs Uniform |
|--------|---------|----------|----------|------|-----|-----------------|
| Uniform Baseline | 17.6939 | 17.6861 | 17.7015 | 17.6938 | 0.0077 | 0.0000 |
| Grid b=0.5 | 17.6510 | 17.6380 | 17.6500 | 17.6463 | 0.0072 | -0.0475 |
| Grid b=1.0 | 17.6920 | 17.6740 | 17.6800 | 17.6820 | 0.0092 | -0.0118 |
| Grid b=1.5 | 17.7180 | 17.7010 | 17.7100 | 17.7097 | 0.0085 | +0.0159 |
| Adaptive (n_min=2) | 17.6527 | 17.6432 | 17.6566 | 17.6508 | 0.0069 | -0.0430 |
| Adaptive (n_min=3, bug) | 17.6440 | 17.6308 | 17.6419 | 17.6389 | 0.0071 | -0.0549 |
| ESS-only | 17.7300 | 17.7200 | 17.7190 | 17.7230 | 0.0061 | +0.0292 |

## Grid-b (b >= 2.0, seed456 excluded)

| Method | Seed 42 | Seed 123 | Mean | Std | Delta vs Uniform | Seed 456 (excluded) |
|--------|---------|----------|------|-----|-----------------|---------------------|
| Grid b=2.0 | 17.7410 | 17.7250 | 17.7330 | 0.0113 | +0.0392 | 17.9890 |
| Grid b=3.0 | 17.7740 | 17.7600 | 17.7670 | 0.0099 | +0.0732 | 17.9210 |
| Grid b=5.0 | 17.8180 | 17.8039 | 17.8109 | 0.0100 | +0.1171 | 17.9930 |

## Single-seed Methods

| Method | PPL | Delta vs Uniform |
|--------|-----|-----------------|
| Golden Ratio Oracle | 17.6540 | -0.0398 |
| Batch Size 8, n_min=2 | 17.7300 | +0.0362 |
| Baseline Pretrained (Qwen3-0.6B) | 22.9700 | +5.2762 |

## n_min Sensitivity (seed=42, tau=0.8)

| n_min | Experiment | PPL | Delta vs Uniform |
|-------|-----------|-----|-----------------|
| 1 | nmin1_seed42 | 17.7890 | +0.0952 |
| 2 | adaptive_fix_seed42 | 17.6527 | -0.0411 |
| 3 | adaptive_seed42 | 17.6440 | -0.0498 |
| 4 | nmin4_seed42 | 17.6947 | +0.0009 |

## tau Sweep (seed=42, n_min=2)

| tau | Experiment | PPL | Delta vs Uniform |
|-----|-----------|-----|-----------------|
| 0.5 | tau_05_seed42 | 17.6880 | -0.0058 |
| 0.6 | tau_06_seed42 | 17.6805 | -0.0133 |
| 0.7 | tau_07_seed42 | 17.6793 | -0.0145 |
| 0.8 | adaptive_fix_seed42 | 17.6527 | -0.0411 |
| 0.9 | tau_09_seed42 | 17.7120 | +0.0182 |
| 0.95 | tau_095_seed42 | 17.7230 | +0.0292 |

## Notes

- All PPL values are eval_ppl_holdout from registry (some recorded as eval_ppl, same holdout eval)
- seed456 grid b>=2.0 excluded due to checkpoint resume artifact
- adaptive_old uses n_min=3 (bug version)
- Grid b seed42 values come from grid_b_seed42_batch experiment (serial batch run)
- ess_only_seed42 and ess_only_seed456 recorded as eval_ppl (not eval_ppl_holdout) but same eval set