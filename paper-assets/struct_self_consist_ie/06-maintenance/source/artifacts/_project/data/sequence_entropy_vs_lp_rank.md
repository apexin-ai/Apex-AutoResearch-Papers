# Sequence Entropy vs LP Rank Correlation

Dataset: FewNERD finetuned 3-epoch (mf4v2_s42_v3), N=8, seed=42

## Overall Statistics
- Mean Spearman ρ: 0.8493
- Median Spearman ρ: 1.0000
- Std: 0.3514
- ρ > 0.95: 69.2%
- ρ < 0.90: 22.7%
- Rank-1 disagreement: 10.6%

## Token Count Variance Stratification
| CV bucket | ρ | rank-1 diff % | interpretation |
|---|---|---|---|
| <0.05 (low) | 0.999 | 0.1% | essentially equivalent |
| 0.05-0.10 (mid) | 0.981 | 2.2% | near-equivalent |
| >0.10 (high) | 0.765 | 16.4% | significantly different |

63% of instances have CV > 0.10.
Token CV vs ρ correlation: r = -0.553 (p ≈ 0)

## Conclusion
NON-TRIVIALLY DIFFERENT. Mean LP and cumulative LP give different rankings 
for most instances in structured output where output lengths vary.
Using mean LP (length-normalized) is a substantive design choice, not just simplification.

Files:
- Script: code/sequence_entropy_vs_lp.py (autodl-5090)
- Results: output/sequence_entropy_vs_lp_results.txt