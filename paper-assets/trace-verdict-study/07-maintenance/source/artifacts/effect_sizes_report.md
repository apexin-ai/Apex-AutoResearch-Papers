# Cohen's d Effect Sizes

All effect sizes computed on accuracy proportions (0–1 scale).
Std source: multi-seed std when available; Wilson approximation sqrt(p(1−p)/1190) when std=0 or single-seed.
Pooled std = sqrt((std₁² + std₂²) / 2).

## 1. Tier Boundary: ae_only vs loop_only

| Model | ae_only | loop_only | Δ (pp) | Cohen's d | Interpretation |
|-------|---------|-----------|--------|-----------|----------------|
| Qwen-7B | 99.64% | 86.05% | 13.59 | 26.90 | Large |
| DeepSeek | 98.53% | 81.26% | 17.27 | 20.87 | Large |
| CodeLlama-13B | 99.08% | 77.40% | 21.68 | 19.60 | Large |
| Qwen-1.5B | 99.08% | 79.54% | 19.54 | 19.10 | Large |

**Range: 19.10–26.90 | Mean: 21.62**

## 2. Exception Dominance: exception_only vs no_trace

| Model | exception_only | no_trace | Δ (pp) | Cohen's d | Interpretation |
|-------|----------------|----------|--------|-----------|----------------|
| Qwen-7B | 99.83% | 75.13% | 24.70 | 27.75 | Large |
| DeepSeek | 99.39% | 73.36% | 26.03 | 28.64 | Large |
| CodeLlama-13B | 99.89% | 76.47% | 23.42 | 26.85 | Large |
| Qwen-1.5B | 99.83% | 67.31% | 32.52 | 33.69 | Large |

**Range: 26.85–33.69 | Mean: 29.23**

## 3. VOTA vs no_trace

| Model | VOTA | no_trace | Δ (pp) | Cohen's d | Interpretation |
|-------|------|----------|--------|-----------|----------------|
| Qwen-7B | 99.05% | 75.13% | 23.92 | 25.83 | Large |
| DeepSeek | 99.25% | 73.36% | 25.89 | 28.45 | Large |
| CodeLlama-13B | 98.74% | 76.47% | 22.27 | 25.14 | Large |
| Qwen-1.5B | 99.54% | 67.31% | 32.23 | 33.49 | Large |

**Range: 25.14–33.49 | Mean: 28.23**

## Summary

All 12 effect sizes exceed Cohen's "large" threshold (d ≥ 0.8) by at least an order of magnitude:

- **Tier boundary** (ae_only vs loop_only): d = 19.10–26.90 (mean 21.62). The gap between assertion-error traces and loop-only traces is massive and consistent across all four models.
- **Exception dominance** (exception_only vs no_trace): d = 26.85–33.69 (mean 29.23). Exception traces alone recover nearly all classification accuracy lost without traces. Largest effect for Qwen-1.5B (d = 33.69), where no_trace accuracy is lowest.
- **VOTA vs no_trace**: d = 25.14–33.49 (mean 28.23). The voted multi-trace ensemble similarly dominates the no-trace baseline with uniformly extreme effect sizes.

The extreme magnitudes reflect (a) large accuracy gaps (13–33 pp) and (b) very low within-condition seed variance (< 1.6 pp), yielding small pooled standard deviations. By Cohen's conventions (0.2 = small, 0.5 = medium, 0.8 = large), every comparison is unambiguously "large."
