# Provenance Weight Training: Experiment Results

All PPL values measured on `eval_holdout.jsonl` (4,077,068 tokens) with sliding-window evaluation (stride=1024, max_length=2048, fp16).

## Table A: ρ=0.4 Main Results (3 seeds)

| Method | seed42 PPL | seed123 PPL | seed456 PPL | Mean PPL | 备注 |
|--------|-----------|------------|------------|---------|------|
| uniform | 17.694 | 17.686 | 17.701 | 17.694 |  |
| adaptive (n_min=3) | 17.644 | 17.631 | 17.642 | 17.639 | τ=0.8 |
| adaptive_fix (n_min=2) | 17.653 | 17.643 | 17.657 | 17.651 | τ=0.8 |
| grid_b0.5 | 17.651 | 17.638 | 17.650 | 17.646 | fixed b=0.5 |
| grid_b1.0 | 17.692 | 17.674 | 17.680 | 17.682 | fixed b=1.0 |
| grid_b1.5 | 17.718 | 17.701 | 17.710 | 17.710 | fixed b=1.5 |
| grid_b2.0 | 17.741 | 17.725 | 17.989 | 17.818 | fixed b=2.0 |
| grid_b3.0 | 17.774 | 17.760 | 17.921 | 17.818 | fixed b=3.0 |
| grid_b5.0 | 17.818 | 17.804 | 17.993 | 17.872 | fixed b=5.0 |
| ess_only | 17.730 | 17.720 | 17.719 | 17.723 |  |
| golden_ratio | 17.654 | N/A | N/A | 17.654 | only seed42 |

## Table B: τ Sweep (ρ=0.4, n_min=2, seed42)

| τ | PPL | b*_mean | b*_median | b*_pct_above_2 |
|---|-----|---------|-----------|----------------|
| 0.5 | 17.688 | 0.392 | 0.171 | 2.900 |
| 0.6 | 17.680 | 0.590 | 0.375 | N/A |
| 0.7 | 17.679 | 0.894 | 0.580 | 7.700 |
| 0.8 | 17.653 | 1.399 | 0.871 | 16.100 |
| 0.9 | 17.712 | 2.360 | 1.320 | 33.700 |
| 0.95 | 17.723 | 3.078 | 1.520 | 40.300 |

## Table C: n_min Sensitivity (ρ=0.4, τ=0.8, seed42)

| n_min | PPL | b*_mean | 备注 |
|-------|-----|---------|------|
| 1 | 17.789 | 7.197 |  |
| 2 | 17.653 | 1.399 | τ=0.8 |
| 3 | 17.644 | N/A | τ=0.8 |
| 4 | 17.695 | 0 | b*=0 for all (ESS always >= n_min) |

## Table D: ρ=0.6 Cross-contamination (seed42)

| Method | ρ=0.6 PPL | ρ=0.4 PPL | Δ PPL |
|--------|-----------|-----------|-------|
| uniform | 17.766 | 17.694 | 0.072 |
| adaptive (τ=0.8) | 17.740 | 17.653 | 0.087 |
| grid_b0.5 | 17.704 | 17.651 | 0.053 |
| ess_only | 17.770 | 17.730 | 0.040 |

## Table E: Batch Size (ρ=0.4, τ=0.8, n_min=2, seed42)

| batch_size | n_min | PPL | 备注 |
|-----------|-------|-----|------|
| 4 | 2 | 17.653 | default |
| 8 | 2 | 17.730 |  |

## Table F: Baseline

| Model | PPL | 备注 |
|-------|-----|------|
| Qwen3-0.6B (no training) | 22.970 | base model eval on same holdout set |
