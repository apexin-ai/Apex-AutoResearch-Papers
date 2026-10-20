# E4 DeepSeek Parse Filter Analysis

## Purpose
Reviewer concern: DeepSeek's low cross-model Pearson r (0.23–0.28) may be an artifact of its high parse failure rate, not genuine "orthogonality."

## Parse Failure Statistics (greedy_f1 == 0)

| Model | Zero-F1 instances | Rate |
|-------|-------------------|------|
| GPT-5.5 | 36/200 | 18.0% |
| Gemini 2.5 Pro | 38/200 | 19.0% |
| Claude Sonnet 4 | 43/200 | 21.5% |
| **DeepSeek** | **101/200** | **50.5%** |

DeepSeek has 2.3–2.8× more zero-F1 instances than other models.

## Correlation: Full vs Filtered

### Pearson r (full, n=200)

| Pair | r | p |
|------|---|---|
| GPT-5.5 vs Gemini 2.5 Pro | 0.8155 | 6.5e-49 |
| GPT-5.5 vs Claude Sonnet 4 | 0.7121 | 3.0e-32 |
| Gemini 2.5 Pro vs Claude Sonnet 4 | 0.6898 | 1.4e-29 |
| GPT-5.5 vs DeepSeek | 0.2830 | 4.9e-05 |
| Gemini 2.5 Pro vs DeepSeek | 0.2521 | 3.2e-04 |
| Claude Sonnet 4 vs DeepSeek | 0.2323 | 9.4e-04 |

### Filter 1: DeepSeek parse-success only (n=99)

| Pair | r (full, n=200) | r (filtered, n=99) | Δr |
|------|----------------|-------------------|------|
| DeepSeek vs GPT-5.5 | 0.283 | 0.206 | -0.077 |
| DeepSeek vs Gemini | 0.252 | 0.244 | -0.008 |
| DeepSeek vs Claude | 0.232 | 0.146 | -0.087 |

**Pearson r decreases** because removing DS-zero instances also removes "both-zero" anchor points that contributed positive correlation.

### Filter 2: All-models-nonzero (n=81) — KEY RESULT

| Pair | r (full, n=200) | r (all-nonzero, n=81) | Δr |
|------|----------------|----------------------|------|
| GPT-5.5 vs DeepSeek | 0.283 | **0.670** | **+0.387** |
| Gemini vs DeepSeek | 0.252 | **0.695** | **+0.443** |
| Claude vs DeepSeek | 0.232 | **0.603** | **+0.371** |
| GPT-5.5 vs Gemini | 0.816 | 0.767 | -0.049 |
| GPT-5.5 vs Claude | 0.712 | 0.752 | +0.040 |
| Gemini vs Claude | 0.690 | 0.753 | +0.063 |

When all models produce valid outputs, DeepSeek correlates at **r ≈ 0.60–0.70** with other models — comparable to inter-model correlations among the other three.

### Spearman ρ (rank correlation, more robust)

| Pair | ρ_full | ρ_DS-success (n=99) | Δ |
|------|--------|---------------------|---|
| DeepSeek vs GPT-5.5 | 0.285 | 0.396 | +0.111 |
| DeepSeek vs Gemini | 0.272 | 0.434 | +0.162 |
| DeepSeek vs Claude | 0.229 | 0.301 | +0.073 |

## Ensemble Scaling

### Full dataset (n=200)

| k models | Greedy-Selection | Cross-Oracle |
|----------|-----------------|-------------|
| 1 | 0.5686±0.0984 | 0.7103±0.0389 |
| 2 | 0.6914±0.0068 | 0.7786±0.0190 |
| 3 | 0.7303±0.0131 | 0.8112±0.0135 |
| 4 | 0.7571 | 0.8311 |

### DeepSeek parse-success subset (n=99)

| k models | Greedy-Selection | Cross-Oracle |
|----------|-----------------|-------------|
| 1 | 0.7341±0.0446 | 0.8008±0.0505 |
| 2 | 0.8124±0.0428 | 0.8604±0.0323 |
| 3 | 0.8528±0.0372 | 0.8913±0.0237 |
| 4 | 0.8873 | 0.9145 |

### Marginal gain from adding DeepSeek

| Metric | Full (n=200) | Filtered (n=99) |
|--------|-------------|-----------------|
| 3→4 model Greedy-Sel gain | +0.049 | +0.099 |
| 3→4 model Cross-Oracle gain | +0.041 | +0.063 |

DeepSeek's marginal ensemble contribution **doubles** on the filtered subset, confirming it adds genuine value when it parses successfully.

## Conclusion

**The "orthogonality" (r ≈ 0.23–0.28) is predominantly a parse failure artifact.**

- On the all-models-nonzero subset (n=81), DeepSeek correlates at r ≈ 0.60–0.70 with other models — well above the 0.4 threshold.
- The low full-dataset correlation is driven by DeepSeek's 50.5% zero-F1 rate creating a bimodal distribution that suppresses Pearson r.
- DeepSeek still contributes to ensemble diversity, but via **error pattern diversity** (different failure instances) rather than genuinely orthogonal capabilities.
- **Conclusion 3 (cross-model orthogonality) needs revision**: the paper should frame this as error diversity from differential parse reliability, not capability orthogonality.

### Recommended paper language
"DeepSeek's lower cross-model correlation (r ≈ 0.28) is largely attributable to its higher parse failure rate (50.5% zero-F1 vs. 18–22% for other models). On the subset where all models produce valid outputs (n=81), correlations rise to r ≈ 0.60–0.70. The ensemble benefit of including DeepSeek thus stems primarily from complementary failure patterns rather than orthogonal extraction capabilities."
