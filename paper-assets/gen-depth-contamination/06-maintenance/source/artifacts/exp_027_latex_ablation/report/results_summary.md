# exp_027 Bootstrap CI Results (LaTeX Ablation)

## Method
- **Data**: exp_027_latex_ablation features.csv (13,200 rows, 15 features, depths 0-5)
- **Classifier**: LightGBM (200 trees, max_depth=6, lr=0.05)
- **OOF**: GroupKFold(5), grouped by doc_id
- **Bootstrap**: 10,000 doc-level resamples on OOF predictions, percentile CI
- **Permutation test** (2v3 only): 1,000 label permutations against fixed OOF predictions

## Results

| Pair | Point Est | CI Lower | CI Upper | Per-fold AUCs | CI lower > 0.60? |
|------|-----------|----------|----------|---------------|-------------------|
| 0v1  | 0.9944    | 0.9925   | 0.9960   | 0.9912, 0.9978, 0.9934, 0.9976, 0.9940 | Yes |
| 1v2  | 0.8315    | 0.8205   | 0.8426   | 0.8125, 0.8563, 0.8227, 0.8285, 0.8373 | Yes |
| **2v3** | **0.6248** | **0.6098** | **0.6402** | 0.6512, 0.6178, 0.6157, 0.6054, 0.6351 | **Yes** |
| 3v4  | 0.5440    | 0.5277   | 0.5598   | 0.5501, 0.5691, 0.5507, 0.5379, 0.5131 | No |
| 4v5  | 0.5425    | 0.5265   | 0.5584   | 0.5253, 0.5664, 0.5470, 0.5423, 0.5292 | No |

## 2v3 Permutation Test
- p-value: 0.000 (0/1000 permutations exceeded observed AUC)
- Null distribution: mean=0.5000, std=0.0087

## Conclusion
**2v3 CI lower = 0.6098 > theta = 0.60: CONFIRMED.**

K*=3 holds under bootstrap CI even after LaTeX removal. The 2v3 signal is statistically significant (p < 0.001) and the 95% CI lower bound clears the theta=0.60 threshold, though with only 0.0098 margin. The drop from the original 0.6436 to 0.6248 is notable but does not invalidate the K*=3 finding.

## Artifacts
- Server JSON: `/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/bootstrap_ci_results.json`
- Script: `/root/autodl-tmp/gen-depth-contamination/scripts/exp027_bootstrap_ci.py`
