# LP-best vs cumLP-best Selection F1

Dataset: FewNERD finetuned 3-epoch (mf4v2_s42_v3), N=8, seed=42, n=32565

## Overall Results
- LP-best mean F1: 0.7614
- cumLP-best mean F1: 0.7151
- Difference: +4.62pp (Wilcoxon p ≈ 0)

## Disagreement Subset (n=3550, 10.9%)
- LP-best F1: 0.6429
- cumLP-best F1: 0.2187
- Difference: +42.42pp (Wilcoxon p ≈ 0)

## Token CV Stratification
| Bucket | n | LP-best F1 | cumLP-best F1 | diff | p |
|--------|---|-----------|--------------|------|---|
| low (CV≤0.05) | 7123 | 0.7554 | 0.7556 | -0.01pp | 0.77 |
| mid (0.05-0.10) | 3572 | 0.8174 | 0.8159 | +0.15pp | 0.052 |
| high-mid (0.10-0.20) | 5649 | 0.7883 | 0.7878 | +0.05pp | 0.14 |
| high (CV>0.20) | 16221 | 0.7423 | 0.6499 | +9.24pp | 0.0000 |

## Conclusion
Winner: mean_LP. Cumulative LP biased toward longer sequences,
selecting substantially worse samples when token count varies (CV>0.20).
Length normalization (mean LP) is essential, not just simplification.

Files:
- Script: code/lp_best_vs_cumlp_best.py (autodl-5090)
- Results: output/lp_best_vs_cumlp_best_results.txt