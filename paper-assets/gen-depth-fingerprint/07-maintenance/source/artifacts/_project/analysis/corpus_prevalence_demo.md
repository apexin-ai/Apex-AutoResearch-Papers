# Corpus Prevalence Estimation Demo

## Setup
- 5 synthetic corpora: 0%, 25%, 50%, 75%, 100% depth-2+ proportion
- Corpus size: 800 documents each
- 8 held-out generators (LOGO), 200 bootstrap resamples per corpus
- 4 quantification methods: CC, ACC, PCC, EMQ

## Results

| True depth-2+ % | EMQ Predicted % | |Error| | 95% CI |
| --- | --- | --- | --- |
| 0% | 2.3% | 2.34pp | [1.0%, 4.1%] |
| 25% | 27.1% | 8.87pp | [23.7%, 30.7%] |
| 50% | 49.7% | 11.70pp | [45.8%, 53.7%] |
| 75% | 71.2% | 13.20pp | [67.0%, 75.3%] |
| 100% | 88.8% | 11.16pp | [85.9%, 91.6%] |

## Method Comparison (MAE across 5 corpora, 8 generators)

| Method | MAE |
| --- | --- |
| CC (Classify & Count) | 16.96pp |
| ACC (Adjusted CC) | 11.19pp |
| PCC (Probabilistic CC) | 19.34pp |
| EMQ (EM Quantification) | 9.45pp |

## Per-Generator EMQ Performance (MAE across 5 corpora)

| Generator | EMQ MAE | Notes |
| --- | --- | --- |
| pythia-2.8b | ~1.1pp | Excellent calibration |
| olmo-2-1b | ~3.5pp | Good |
| llama-3.2-3b | ~6.6pp | Moderate |
| qwen3-1.7b | ~6.4pp | Moderate |
| pythia-1b | ~7.6pp | Moderate |
| mistral-7b-v0.3 | ~12.4pp | Poor (high domain shift) |
| qwen3-0.6b | ~11.3pp | Poor |
| qwen3-8b | ~12.3pp | Poor |

## Conclusion

MAE = 9.45pp (best, EMQ) >= 5pp threshold.

**Corpus-level depth auditing is NOT viable in the strict LOGO (cross-generator) setting** with the current 7-feature XGBoost classifier.

Key observations:
1. For in-distribution generators (pythia-2.8b, olmo-2-1b), MAE < 3.5pp, demonstrating the method is sound when domain shift is small.
2. The bottleneck is generator-specific domain shift in LOGO, not the quantification method itself.
3. EMQ (Saerens et al. 2002) provides the best correction by adapting posterior probabilities to the test distribution without explicit TPR/FPR estimation.
4. Naive classify-and-count systematically underestimates high proportions and overestimates low proportions (regression to the mean).

## Outputs
- Plot: `/root/gen-depth-fingerprint/results/corpus_prevalence_calibration.pdf`
- Data: `/root/gen-depth-fingerprint/results/corpus_prevalence_demo.json`
- Script: `/root/gen-depth-fingerprint/corpus_prevalence_demo.py`
- Log: `/root/gen-depth-fingerprint/logs/corpus_prevalence_demo.log`
