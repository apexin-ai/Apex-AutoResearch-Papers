# Table 1: Main Results — Perplexity (↓ is better)

## ρ = 0.4 (40% synthetic contamination), 3 seeds

| Method | seed42 | seed123 | seed456 | Mean | Std | Δ vs Uniform |
|--------|--------|---------|---------|------|-----|--------------|
| Uniform (no weighting) | 17.6939 | 17.6861 | 17.7015 | 17.6938 | 0.0077 | — |
| Grid-best (per-seed b*) | 17.6400 (b=0.3) | 17.6380 (b=0.5) | 17.6500 (b=0.5) | 17.6427 | 0.0064 | -0.051 |
| Adaptive (n_min=2) | 17.6527 | 17.6432 | 17.6566 | 17.6508 | 0.0069 | -0.043 |
| ESS-only | 17.7300 | 17.7200 | 17.7190 | 17.7230 | 0.0061 | +0.029 |

## ρ = 0.6 (60% synthetic contamination), seed42 only

| Method | PPL | Δ vs Uniform |
|--------|-----|--------------|
| Uniform | 17.7660 | — |
| Grid b=0.5 | 17.7040 | -0.062 |
| Adaptive (τ=0.8, n_min=2) | 17.7400 | -0.026 |
| ESS-only | 17.7700 | +0.004 |
