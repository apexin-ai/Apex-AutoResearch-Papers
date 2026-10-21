# Gen-1 Subclass Error Analysis by Generator

Binary LOGO evaluation (gen-1 vs gen-2+), with per-generator error breakdown sorted by model size.

## Results

| Generator | Size | gen-1 N | gen-1 F1 | FNR | FPR | Macro-F1 |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3-0.6B | 0.6B | 986 | 0.6684 | 0.2353 | 0.2019 | 0.7568 |
| OLMo-2-1B | 1.0B | 988 | 0.6077 | 0.1549 | 0.3388 | 0.6889 |
| Pythia-1B | 1.0B | 993 | 0.7200 | 0.1712 | 0.1831 | 0.7938 |
| Qwen3-1.7B | 1.7B | 983 | 0.6764 | 0.1475 | 0.2491 | 0.7540 |
| Pythia-2.8B | 2.8B | 989 | 0.6718 | 0.1112 | 0.2853 | 0.7427 |
| Llama-3.2-3B | 3.0B | 984 | 0.6207 | 0.0711 | 0.3876 | 0.6841 |
| Mistral-7B-v0.3 | 7.0B | 994 | 0.5097 | 0.0644 | 0.6034 | 0.5344 |
| Qwen3-8B | 8.0B | 979 | 0.6008 | 0.0776 | 0.4455 | 0.6503 |

- FNR = gen-1 misclassified as gen-2+ (false negative rate for gen-1 class)
- FPR = gen-2+ misclassified as gen-1 (false positive rate for gen-1 class)

## Spearman Correlations (model size vs metric)

| Metric | rho | p-value |
| --- | --- | --- |
| size vs FNR | -0.9222 | 0.0011 |
| size vs gen-1 F1 | -0.5868 | 0.1262 |
| size vs FPR | +0.8383 | 0.0093 |

## Key Findings

1. **FPR increases with model size (rho=+0.84, p=0.009)**: Gen-2+ outputs from larger models are frequently misclassified as gen-1. Mistral-7B has FPR=0.60 (60% of its gen-2+ is confused with gen-1) vs Pythia-1B at FPR=0.18. This directly supports the "larger models compress depth margins" claim: subsequent generation passes through a larger model fail to accumulate the statistical fingerprint that distinguishes gen-2+ from gen-1.

2. **FNR decreases with model size (rho=-0.92, p=0.001)**: Gen-1 from larger models is rarely misclassified as gen-2+. Mistral-7B has FNR=0.06 vs Qwen3-0.6B at FNR=0.24. Larger models produce a distinctive gen-1 fingerprint (one pass away from human text), but further passes do not deepen the signal proportionally.

3. **Mechanistic interpretation**: Smaller models add substantial incremental distortion at each depth, making gen-1 vs gen-2+ separable. Larger models apply a strong but saturating transformation: the first pass creates a clear fingerprint, but additional passes add negligible further drift, compressing the gen-1/gen-2+ margin.

## Method
- Classifier: sklearn HistGradientBoostingClassifier (max_iter=200, max_depth=6, lr=0.1)
- Evaluation: 8-generator Leave-One-Generator-Out binary (gen-1=0, gen-2+=1, gen-0 excluded)
- Downsampled training to balanced classes per fold
- Features: entropy_mean/std/min/max, tail_decay, ttr, hapax_ratio
