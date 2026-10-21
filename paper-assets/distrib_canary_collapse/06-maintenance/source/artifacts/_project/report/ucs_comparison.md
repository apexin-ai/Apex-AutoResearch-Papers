# Universal Cascade Signature (UCS) — Cross-Domain Comparison

## Hypothesis
The Entropy→Diversity→Calibration cascade observed in synthetic-data collapse
extends to other domains where model distributions shift.

Hypothesized ordering: token_entropy → ece → distinct_n → perplexity

Onset detection: first checkpoint with ≥5% change from baseline (robust to near-zero variance).

## Domain: pythia_pretraining
Checkpoints: 20, Onset threshold: 5.0%

### Onset Table
| Metric | Onset Idx | Onset Label | % at Onset | Baseline | Final | Total Δ% |
|--------|-----------|-------------|------------|----------|-------|----------|
| token_entropy | 8 | step128 | 18.8% | 10.625558 | 4.034487 | -62.0% |
| ece | 5 | step16 | 20538.7% | 0.00025 | 0.074663 | 29804.0% |
| distinct_1 | 5 | step16 | 11.7% | 0.789491 | 0.3172 | -59.8% |
| distinct_2 | 6 | step32 | 44.6% | 0.955158 | 0.701184 | -26.6% |
| distinct_3 | 6 | step32 | 38.6% | 0.969374 | 0.882834 | -8.9% |
| perplexity | 4 | step8 | 11.7% | 60041.443838 | 42.075218 | -99.9% |

### Cascade Order: perplexity → ece → distinct_1 → distinct_2 → distinct_3 → token_entropy
Kendall τ vs hypothesis: -0.667 (p=0.333)

## Domain: olmo_rlhf
Checkpoints: 4, Onset threshold: 5.0%

### Onset Table
| Metric | Onset Idx | Onset Label | % at Onset | Baseline | Final | Total Δ% |
|--------|-----------|-------------|------------|----------|-------|----------|
| token_entropy | 1 | sft | 18.5% | 2.205625 | 1.821485 | -17.4% |
| ece | 1 | sft | 51.3% | 0.070506 | 0.060188 | -14.6% |
| distinct_1 | 1 | sft | 8.2% | 0.349304 | 0.412805 | 18.2% |
| distinct_2 | 2 | dpo | 10.4% | 0.761791 | 0.827921 | 8.7% |
| distinct_3 | - | - | - | 0.9094 | 0.935563 | 2.9% |
| perplexity | 1 | sft | 10.5% | 5.793056 | 6.309701 | 8.9% |

### Cascade Order: ece → token_entropy → perplexity → distinct_1 → distinct_2
Kendall τ vs hypothesis: 0.333 (p=0.75)

## Cross-Domain Summary

- **pythia_pretraining**: first onset = perplexity, ordering = perplexity → ece → distinct_1 → distinct_2
- **olmo_rlhf**: first onset = ece, ordering = ece → token_entropy → perplexity → distinct_1

### Comparison with Synthetic-Data Collapse
In synthetic-data collapse (our project): **entropy → ECE → distinct_n → perplexity**

Domains with entropy-first onset: 0/2

**Conclusion**: Cascade ordering is domain-specific. In pretraining, perplexity
(prediction error) changes first, while entropy (distributional shape) lags.
In collapse, the reverse holds — entropy is the earliest canary signal.
This suggests the cascade is a signature of *distributional degradation*,
not a universal property of distribution shift.