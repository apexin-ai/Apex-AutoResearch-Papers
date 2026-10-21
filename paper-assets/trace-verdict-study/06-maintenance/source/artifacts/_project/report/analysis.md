# Qwen-1.5B no_trace Analysis Report

## 1. Single-Seed Metrics (seed=456)

| Metric | Value |
|--------|-------|
| Accuracy | 73.87% [71.3%, 76.2%] |
| Majority baseline | 71.51% |
| Lift | +2.36pp |
| Pass P / R / F1 | 0.81 / 0.83 / 0.82 |
| Fail P / R / F1 | 0.54 / 0.51 / 0.53 |
| Eval loss | 0.7725 |

## 2. 3-Seed Summary

| Seed | Accuracy | Lift |
|------|----------|------|
| 42 | 67.31% | -4.20pp |
| 123 | 75.88% | +4.37pp |
| 456 | 73.87% | +2.36pp |
| **Mean ± Std** | **72.35% ± 4.48pp** | **+0.84pp** |

Bootstrap 95% CI (10k resamples): [67.31%, 75.88%]

Seed42 deviation: 1.13σ below mean (not outlier at 1.5σ threshold).

## 3. Cross-Model no_trace Comparison

| Model | no_trace Accuracy | Seeds |
|-------|-------------------|-------|
| Qwen-7B | 75.13% | 1 (seed42) |
| DeepSeek-7B | 73.36% | 1 (seed42) |
| CodeLlama-13B | 76.50% | 1 (seed42 Wilson CI) |
| **Qwen-1.5B** | **72.35% ± 4.48%** | **3 (42/123/456)** |

Qwen-1.5B no_trace is the lowest among all models, consistent with smaller model capacity.
Notably, Qwen-1.5B shows the highest seed variance (4.48pp vs <2pp for traced conditions),
suggesting no_trace + small model = high seed sensitivity.

## 4. Implications for C2 Decomposition

| Component | Qwen-7B | Qwen-1.5B |
|-----------|---------|-----------|
| no_trace baseline | 75.13% | 72.35% |
| label_only | 85.94±1.12% | 80.92±1.85% |
| Δ label formatting | +10.81pp | +8.57pp |
| exception_only | 99.83% | 99.83% |
| Δ trace content | +13.89pp | +18.91pp |

Trace content contribution exceeds label formatting for both scales (2.2x for 1.5B, 1.3x for 7B).
