# arXiv Cross-Scorer Experiments: Full Results Summary

Generated: 2026-05-18

> **Note**: The ± values are population std across 5 CV folds. No bootstrap CI was computed in these experiments.

---

## 1. Qwen-7B (`exp_arXiv_qwen7b_crossscorer`)

**K\* = 2** | Ordinal Accuracy = 0.4255 | Ordinal MAE = 0.9617

### Pairwise AUC (5-fold CV)

| Pair | Mean AUC | ± Std | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 |
|------|----------|-------|--------|--------|--------|--------|--------|
| 0v1  | **0.9575** | 0.0074 | 0.9614 | 0.9561 | 0.9680 | 0.9454 | 0.9567 |
| 1v2  | **0.8171** | 0.0166 | 0.7892 | 0.8093 | 0.8265 | 0.8236 | 0.8372 |
| 2v3  | 0.5989 | 0.0135 | 0.5920 | 0.6006 | 0.6108 | 0.5768 | 0.6142 |
| 3v4  | 0.5417 | 0.0220 | 0.5285 | 0.5249 | 0.5639 | 0.5187 | 0.5725 |
| 4v5  | 0.5192 | 0.0162 | 0.5019 | 0.5365 | 0.5167 | 0.5017 | 0.5391 |

### Per-Depth JSD

| Pair | JSD |
|------|-----|
| 0v1  | 0.1371 |
| 1v2  | 0.0597 |
| 2v3  | 0.0135 |
| 3v4  | 0.0091 |
| 4v5  | 0.0067 |

### Top-10 Feature Importance

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | freq_entropy | 9853.2 |
| 2 | surp_std | 7917.2 |
| 3 | surp_d1_skew | 7895.0 |
| 4 | surp_mean | 7603.0 |
| 5 | surp_d2_mean | 7329.4 |
| 6 | surp_d1_mean | 7247.6 |
| 7 | freq_kurtosis | 6881.6 |
| 8 | surp_kurt | 6452.8 |
| 9 | hapax_ratio | 5941.0 |
| 10 | surp_d1_std | 5913.8 |

---

## 2. Qwen-1.5B (`exp_arXiv_qwen1b5_crossscorer`)

**K\* = 3** | Ordinal Accuracy = 0.4402 | Ordinal MAE = 0.9017

### Pairwise AUC (5-fold CV)

| Pair | Mean AUC | ± Std | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 |
|------|----------|-------|--------|--------|--------|--------|--------|
| 0v1  | **0.9748** | 0.0031 | 0.9723 | 0.9715 | 0.9796 | 0.9732 | 0.9774 |
| 1v2  | **0.8105** | 0.0083 | 0.8070 | 0.8248 | 0.8138 | 0.8006 | 0.8063 |
| 2v3  | **0.6317** | 0.0124 | 0.6533 | 0.6260 | 0.6296 | 0.6157 | 0.6340 |
| 3v4  | 0.5437 | 0.0118 | 0.5577 | 0.5480 | 0.5228 | 0.5499 | 0.5403 |
| 4v5  | 0.5294 | 0.0250 | 0.5197 | 0.5551 | 0.5102 | 0.5625 | 0.4994 |

### Per-Depth JSD

| Pair | JSD |
|------|-----|
| 0v1  | 0.1543 |
| 1v2  | 0.0668 |
| 2v3  | 0.0193 |
| 3v4  | 0.0089 |
| 4v5  | 0.0070 |

### Top-10 Feature Importance

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | freq_entropy | 9540.4 |
| 2 | surp_std | 8015.4 |
| 3 | surp_d1_skew | 7848.6 |
| 4 | surp_d1_mean | 7427.4 |
| 5 | surp_mean | 7402.2 |
| 6 | surp_d2_mean | 7324.8 |
| 7 | freq_kurtosis | 6931.2 |
| 8 | surp_kurt | 6623.8 |
| 9 | surp_d1_std | 6006.8 |
| 10 | hapax_ratio | 5892.6 |

---

## 3. LLaMA-8B (`exp_arXiv_llama8b_crossscorer`)

**K\* = 3** | Ordinal Accuracy = 0.4407 | Ordinal MAE = 0.9025

### Pairwise AUC (5-fold CV)

| Pair | Mean AUC | ± Std | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 |
|------|----------|-------|--------|--------|--------|--------|--------|
| 0v1  | **0.9629** | 0.0013 | 0.9641 | 0.9612 | 0.9614 | 0.9638 | 0.9639 |
| 1v2  | **0.8433** | 0.0091 | 0.8432 | 0.8552 | 0.8354 | 0.8315 | 0.8515 |
| 2v3  | **0.6201** | 0.0118 | 0.6306 | 0.6115 | 0.6073 | 0.6136 | 0.6377 |
| 3v4  | 0.5230 | 0.0195 | 0.5430 | 0.5343 | 0.5386 | 0.5036 | 0.4955 |
| 4v5  | 0.5245 | 0.0112 | 0.5036 | 0.5229 | 0.5289 | 0.5330 | 0.5341 |

### Per-Depth JSD

| Pair | JSD |
|------|-----|
| 0v1  | 0.1214 |
| 1v2  | 0.0815 |
| 2v3  | 0.0195 |
| 3v4  | 0.0083 |
| 4v5  | 0.0082 |

### Top-10 Feature Importance

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | freq_entropy | 9355.8 |
| 2 | surp_std | 7733.0 |
| 3 | surp_d1_skew | 7571.0 |
| 4 | surp_d2_mean | 7287.4 |
| 5 | surp_d1_mean | 7257.8 |
| 6 | surp_mean | 7244.6 |
| 7 | freq_kurtosis | 6973.4 |
| 8 | surp_kurt | 6458.4 |
| 9 | ttr | 6356.2 |
| 10 | surp_d1_std | 6010.8 |

---

## 4. Mistral-7B (`exp_arXiv_mistral7b_crossscorer`)

**K\* = 3** | Ordinal Accuracy = 0.4412 | Ordinal MAE = 0.9061

### Pairwise AUC (5-fold CV)

| Pair | Mean AUC | ± Std | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 |
|------|----------|-------|--------|--------|--------|--------|--------|
| 0v1  | **0.9798** | 0.0033 | 0.9817 | 0.9792 | 0.9803 | 0.9739 | 0.9838 |
| 1v2  | **0.8141** | 0.0140 | 0.7874 | 0.8256 | 0.8225 | 0.8223 | 0.8125 |
| 2v3  | **0.6075** | 0.0147 | 0.6052 | 0.5803 | 0.6210 | 0.6113 | 0.6195 |
| 3v4  | 0.5489 | 0.0053 | 0.5560 | 0.5450 | 0.5426 | 0.5464 | 0.5544 |
| 4v5  | 0.5391 | 0.0093 | 0.5291 | 0.5448 | 0.5309 | 0.5364 | 0.5542 |

### Per-Depth JSD

| Pair | JSD |
|------|-----|
| 0v1  | 0.1356 |
| 1v2  | 0.0780 |
| 2v3  | 0.0205 |
| 3v4  | 0.0110 |
| 4v5  | 0.0088 |

### Top-10 Feature Importance

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | freq_entropy | 9818.0 |
| 2 | surp_std | 7749.8 |
| 3 | surp_d1_skew | 7712.2 |
| 4 | surp_d1_mean | 7251.0 |
| 5 | surp_mean | 7194.0 |
| 6 | surp_d2_mean | 6990.4 |
| 7 | freq_kurtosis | 6794.0 |
| 8 | surp_kurt | 6635.0 |
| 9 | ttr | 5977.4 |
| 10 | hapax_ratio | 5948.8 |

---

## 5. Cross-Model Comparison Summary

### Pairwise AUC Comparison

| Pair | Qwen-7B | Qwen-1.5B | LLaMA-8B | Mistral-7B |
|------|---------|-----------|----------|------------|
| 0v1  | 0.9575 ± 0.0074 | 0.9748 ± 0.0031 | 0.9629 ± 0.0013 | **0.9798 ± 0.0033** |
| 1v2  | 0.8171 ± 0.0166 | 0.8105 ± 0.0083 | **0.8433 ± 0.0091** | 0.8141 ± 0.0140 |
| 2v3  | 0.5989 ± 0.0135 | **0.6317 ± 0.0124** | 0.6201 ± 0.0118 | 0.6075 ± 0.0147 |
| 3v4  | 0.5417 ± 0.0220 | 0.5437 ± 0.0118 | 0.5230 ± 0.0195 | **0.5489 ± 0.0053** |
| 4v5  | 0.5192 ± 0.0162 | 0.5294 ± 0.0250 | 0.5245 ± 0.0112 | **0.5391 ± 0.0093** |

### K\*, Ordinal Metrics Comparison

| Model | K\* | Ordinal Acc | Ordinal MAE |
|-------|-----|-------------|-------------|
| Qwen-7B | 2 | 0.4255 | 0.9617 |
| Qwen-1.5B | **3** | 0.4402 | 0.9017 |
| LLaMA-8B | **3** | **0.4407** | **0.9025** |
| Mistral-7B | **3** | 0.4412 | 0.9061 |

### JSD Comparison

| Pair | Qwen-7B | Qwen-1.5B | LLaMA-8B | Mistral-7B |
|------|---------|-----------|----------|------------|
| 0v1  | 0.1371 | **0.1543** | 0.1214 | 0.1356 |
| 1v2  | 0.0597 | 0.0668 | **0.0815** | 0.0780 |
| 2v3  | 0.0135 | 0.0193 | 0.0195 | **0.0205** |
| 3v4  | 0.0091 | 0.0089 | 0.0083 | **0.0110** |
| 4v5  | 0.0067 | 0.0070 | 0.0082 | **0.0088** |

### Key Observations

1. **K\* = 2 for Qwen-7B, K\* = 3 for all others**: Qwen-7B's 2v3 AUC (0.5989) falls just below the 0.60 threshold, while the other three models exceed it (0.6075-0.6317).

2. **All models share the same saturation pattern**: AUC drops sharply from 0v1 (~0.96-0.98) to 1v2 (~0.81-0.84), then becomes near-chance by 3v4 (~0.52-0.55). Contamination signal is strong at shallow depths and vanishes by depth 3-4.

3. **LLaMA-8B has the highest 1v2 AUC (0.8433)**, suggesting its cross-scorer features are most discriminative at the first-to-second generation boundary.

4. **Qwen-1.5B has the highest 2v3 AUC (0.6317)**, indicating the smaller model retains more detectable contamination signal at deeper generations.

5. **Feature importance is highly consistent across all models**: freq_entropy dominates (#1 in all), followed by surp_std, surp_d1_skew. The top-7 features are identical across all four models.

6. **Ordinal classification is similar across models**: Accuracy 0.43-0.44, MAE 0.90-0.96, confirming that fine-grained depth prediction is hard but coarse-grained detection (0v1, 1v2) is reliable.
