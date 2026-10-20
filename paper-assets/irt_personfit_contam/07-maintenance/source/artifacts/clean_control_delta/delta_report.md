# Clean-vs-Clean Δlz* Validation Report

N subjects: 500, Contamination: 25%

## Results by Benchmark

### mmlu

| Metric | Clean-vs-Clean | Clean-vs-Contam |
|--------|---------------|-----------------|
| Mean Δlz* | 0.0102 | 9.4222 |
| Std Δlz* | 1.4508 | 4.7933 |
| 95% CI | [-0.1169, 0.1374] | [9.0021, 9.8424] |
| t-stat (H0: μ=0) | 0.1578 | 43.9541 |
| p-value | 0.874698 | 0.000000 |
| Cohen's d (between groups) | -2.6578 |
| Two-sample p | 0.000000 |

### hellaswag

| Metric | Clean-vs-Clean | Clean-vs-Contam |
|--------|---------------|-----------------|
| Mean Δlz* | -0.1252 | 5.0492 |
| Std Δlz* | 1.4308 | 3.6856 |
| 95% CI | [-0.2506, 0.0002] | [4.7261, 5.3722] |
| t-stat (H0: μ=0) | -1.9570 | 30.6337 |
| p-value | 0.050909 | 0.000000 |
| Cohen's d (between groups) | -1.8509 |
| Two-sample p | 0.000000 |

### gsm8k

| Metric | Clean-vs-Clean | Clean-vs-Contam |
|--------|---------------|-----------------|
| Mean Δlz* | -0.0210 | 3.2994 |
| Std Δlz* | 1.4221 | 2.1021 |
| 95% CI | [-0.1456, 0.1037] | [3.1151, 3.4836] |
| t-stat (H0: μ=0) | -0.3301 | 35.0975 |
| p-value | 0.741468 | 0.000000 |
| Cohen's d (between groups) | -1.8502 |
| Two-sample p | 0.000000 |

### arc_c

| Metric | Clean-vs-Clean | Clean-vs-Contam |
|--------|---------------|-----------------|
| Mean Δlz* | 0.0945 | 0.6497 |
| Std Δlz* | 1.4499 | 0.9951 |
| 95% CI | [-0.0326, 0.2216] | [0.5625, 0.7369] |
| t-stat (H0: μ=0) | 1.4579 | 14.6004 |
| p-value | 0.145498 | 0.000000 |
| Cohen's d (between groups) | -0.4465 |
| Two-sample p | 0.000000 |

### humaneval

| Metric | Clean-vs-Clean | Clean-vs-Contam |
|--------|---------------|-----------------|
| Mean Δlz* | 0.0200 | 1.4053 |
| Std Δlz* | 1.3764 | 1.2127 |
| 95% CI | [-0.1007, 0.1406] | [1.2990, 1.5116] |
| t-stat (H0: μ=0) | 0.3246 | 25.9126 |
| p-value | 0.745646 | 0.000000 |
| Cohen's d (between groups) | -1.0680 |
| Two-sample p | 0.000000 |

## Validation Criteria

- **mmlu**: |mean_cc|<0.2: ✓ (0.0102), contam p<0.05: ✓ (0.000000), |d|>0.5: ✓ (2.6578) → **PASS**
- **hellaswag**: |mean_cc|<0.2: ✓ (-0.1252), contam p<0.05: ✓ (0.000000), |d|>0.5: ✓ (1.8509) → **PASS**
- **gsm8k**: |mean_cc|<0.2: ✓ (-0.0210), contam p<0.05: ✓ (0.000000), |d|>0.5: ✓ (1.8502) → **PASS**
- **arc_c**: |mean_cc|<0.2: ✓ (0.0945), contam p<0.05: ✓ (0.000000), |d|>0.5: ✗ (0.4465) → **FAIL**
- **humaneval**: |mean_cc|<0.2: ✓ (0.0200), contam p<0.05: ✓ (0.000000), |d|>0.5: ✓ (1.0680) → **PASS**

## Conclusion

**Core finding confirmed**: Clean-vs-clean Δlz* has E≈0 across all 5 benchmarks (|mean| < 0.13, no t-test significant at α=0.05), confirming that non-zero Δlz* in contamination experiments reflects genuine contamination signal, not estimation noise.

**Clean-vs-contaminated separation**: All benchmarks show highly significant contamination-induced Δlz* (p < 1e-10). Effect sizes are large for mmlu (d=2.66), hellaswag (d=1.85), gsm8k (d=1.85), and humaneval (d=1.07).

**arc_c caveat**: With only 295 items, arc_c yields a moderate effect size (d=0.45) at 25% contamination. This is expected — fewer items means fewer items actually flipped (many are already correct for high-θ subjects), producing a weaker but still significant signal (p < 1e-10). The method remains valid for arc_c but has lower power; higher contamination rates or item-level analyses may be needed for this benchmark.