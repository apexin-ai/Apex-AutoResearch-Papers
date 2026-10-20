# exp_32b_c4 Analysis Report

## Experiment Info

| Field | Value |
|-------|-------|
| exp_id | exp_32b_c4 |
| server | westd-42896 |
| model | Qwen2.5-32B (fp16) |
| data | C4 web text, 5000 docs |
| depths | 0-5 |
| sampling | nucleus p=0.95, T=1.0 |
| scorer | Qwen2.5-1.5B |
| status | **completed successfully** (EXIT_CODE=0) |
| log_path | `~/runs/gen-depth-contamination/exp_32b_c4.log` |
| results_dir | `/root/autodl-tmp/gen-depth-contamination/results/exp_32b_c4` |
| W&B run | N/A (not logged) |

## K* Result

**K\* = 2** (threshold AUC > 0.60)

- AUC(0v1) = 0.9575 >= 0.60 --> distinguishable
- AUC(1v2) = 0.6183 >= 0.60 --> distinguishable
- AUC(2v3) = 0.5454 < 0.60 --> indistinguishable
- Therefore K* = 2

## Pairwise AUC (Adjacent Depths, 5-Fold CV)

| Depth Pair | AUC (mean) | Std | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 |
|------------|-----------|-----|--------|--------|--------|--------|--------|
| 0 vs 1 | **0.9575** | 0.0031 | 0.9555 | 0.9576 | 0.9579 | 0.9535 | 0.9629 |
| 1 vs 2 | **0.6183** | 0.0049 | 0.6165 | 0.6172 | 0.6157 | 0.6143 | 0.6279 |
| 2 vs 3 | 0.5454 | 0.0080 | 0.5427 | 0.5310 | 0.5526 | 0.5491 | 0.5517 |
| 3 vs 4 | 0.5219 | 0.0052 | 0.5203 | 0.5150 | 0.5299 | 0.5191 | 0.5251 |
| 4 vs 5 | 0.5155 | 0.0066 | 0.5242 | 0.5203 | 0.5109 | 0.5058 | 0.5163 |

AUC > 0.60 pairs shown in **bold**.

## Pairwise JSD (Adjacent Depths)

| Depth Pair | JSD |
|------------|-----|
| 0 vs 1 | 0.114924 |
| 1 vs 2 | 0.010109 |
| 2 vs 3 | 0.005447 |
| 3 vs 4 | 0.004048 |
| 4 vs 5 | 0.003791 |

Sharp drop from 0v1 (0.1149) to 1v2 (0.0101), then gradual decay. Consistent with the AUC pattern: depth 0 vs 1 is trivially separable, depth 1 vs 2 is marginally separable, depth 2+ converges.

## Ordinal Classification (6-class, 5-Fold CV)

| Metric | Value |
|--------|-------|
| MAE | 1.2286 |
| Accuracy | 0.3516 |

## Top-10 Feature Importance (LightGBM)

| Rank | Feature | Importance |
|------|---------|-----------|
| 1 | freq_entropy | 8815.2 |
| 2 | surp_std | 8459.4 |
| 3 | surp_d1_skew | 8339.8 |
| 4 | surp_d1_mean | 8297.6 |
| 5 | surp_d2_mean | 8037.0 |
| 6 | freq_kurtosis | 7985.4 |
| 7 | surp_mean | 7860.4 |
| 8 | surp_kurt | 7110.6 |
| 9 | hapax_ratio | 6508.4 |
| 10 | surp_skew | 6349.0 |

## Cross-Scale Comparison (C4 Domain)

| Model | Scale | K* | AUC(0v1) | AUC(1v2) | AUC(2v3) |
|-------|-------|----|----------|----------|----------|
| Qwen2.5-1.5B | 1.5B | 2 | - | - | - |
| Qwen2.5-7B | 7B | 2 | - | - | - |
| LLaMA-3.1-8B | 8B | 2 | - | - | - |
| Qwen2.5-14B | 14B | 2 | - | - | - |
| **Qwen2.5-32B** | **32B** | **2** | **0.9575** | **0.6183** | **0.5454** |

K* = 2 is confirmed across all tested scales from 1.5B to 32B on C4.

## Conclusion

**SUCCESS.** The hypothesis is confirmed: K* = 2 remains the dominant mode at the 32B scale on C4 web text.

Key findings:
1. K* = 2 is scale-invariant across 1.5B, 7B, 8B, 14B, and 32B on C4
2. The AUC decay pattern is consistent: 0v1 near-perfect (~0.96), 1v2 marginally above threshold (~0.62), 2v3 drops below (~0.55)
3. JSD shows the same rapid saturation: the 0-to-1 generation step introduces most of the distributional shift, with diminishing changes at deeper depths
4. No scale ceiling effect observed. The 32B model does not produce "higher quality" continuations that would push the saturation boundary further out

This eliminates model scale (up to 32B) as a confound for the K* = 2 finding on general web text.
