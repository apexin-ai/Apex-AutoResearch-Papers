# exp_arXiv_mistral7b_crossscorer — Analysis Report

## Experiment Configuration
- **Generator**: Mistral-7B
- **Domain**: arXiv
- **Original scorer**: Qwen-1.5B (exp_arXiv_mistral7b)
- **Cross-scorer**: Pythia-1.4B (this experiment)
- **Depths**: 0–5
- **Mode**: --skip_generation (reuses Mistral-7B arXiv texts, re-scores with Pythia)
- **Hypothesis**: K*=3 from Qwen scorer is scorer-independent

## Pairwise AUC Comparison

| Depth Pair | Qwen-1.5B (original) | Pythia-1.4B (cross) | Delta |
|------------|----------------------|---------------------|-------|
| 0 vs 1     | 0.9848 ± 0.0031     | 0.9798 ± 0.0033    | -0.0050 |
| 1 vs 2     | 0.8201 ± 0.0137     | 0.8141 ± 0.0140    | -0.0060 |
| 2 vs 3     | 0.6275 ± 0.0074     | 0.6075 ± 0.0147    | -0.0200 |
| 3 vs 4     | 0.5295 ± 0.0090     | 0.5489 ± 0.0053    | +0.0194 |
| 4 vs 5     | 0.5295 ± 0.0164     | 0.5391 ± 0.0093    | +0.0096 |

## Pairwise JSD Comparison

| Depth Pair | Qwen-1.5B | Pythia-1.4B | Delta |
|------------|-----------|-------------|-------|
| 0 vs 1     | 0.1425    | 0.1356      | -0.0069 |
| 1 vs 2     | 0.0762    | 0.0780      | +0.0018 |
| 2 vs 3     | 0.0190    | 0.0205      | +0.0015 |
| 3 vs 4     | 0.0099    | 0.0110      | +0.0011 |
| 4 vs 5     | 0.0089    | 0.0088      | -0.0001 |

## Ordinal Classification

| Metric   | Qwen-1.5B | Pythia-1.4B |
|----------|-----------|-------------|
| MAE      | 0.8958    | 0.9061      |
| Accuracy | 0.4474    | 0.4412      |
| K*       | 3         | 3           |

## K* Determination

Threshold: AUC > 0.60

- Pythia scorer: 2v3 AUC = 0.6075 (above threshold), 3v4 AUC = 0.5489 (below) → K* = 3
- Qwen scorer:  2v3 AUC = 0.6275 (above threshold), 3v4 AUC = 0.5295 (below) → K* = 3

Both scorers agree: the saturation boundary falls between depth 3 and depth 4.

## Top-10 Feature Importance (Pythia scorer)

1. freq_entropy (9818.0)
2. surp_std (7749.8)
3. surp_d1_skew (7712.2)
4. surp_d1_mean (7251.0)
5. surp_mean (7194.0)
6. surp_d2_mean (6990.4)
7. freq_kurtosis (6794.0)
8. surp_kurt (6635.0)
9. ttr (5977.4)
10. hapax_ratio (5948.8)

## Contrast with Wikipedia Cross-Scorer Results

Wikipedia domain showed scorer confound:
- Qwen scorer → K*=2
- Pythia scorer → K*=1

arXiv domain shows no scorer confound:
- Qwen scorer → K*=3
- Pythia scorer → K*=3

This suggests the depth signal in arXiv is stronger and more robust than in Wikipedia, making it less susceptible to scorer bias.

## Conclusion

**K*=3 is scorer-independent for Mistral-7B on arXiv.** The Pythia-1.4B cross-scorer replicates the same saturation point as the original Qwen-1.5B scorer, with very small AUC differences (max delta = 0.02 at 2v3). The arXiv K*=3 finding is a genuine signal, not an artifact of scorer choice.

This contrasts with Wikipedia, where scorer choice significantly affected K*, indicating that scorer confound is domain-dependent: stronger generation-depth signals (arXiv) are robust to scorer substitution, while weaker signals (Wikipedia) are not.
