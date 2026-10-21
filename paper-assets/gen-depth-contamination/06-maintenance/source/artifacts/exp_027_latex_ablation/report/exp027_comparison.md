# exp-027: LaTeX Markup Removal Ablation

## Goal
Test whether arXiv K*=3 depends on LaTeX formatting features.

## Method
- Strip LaTeX commands (math, \cite, \ref, environments, etc.) from exp-024 arXiv depth 0-5 data
- Re-extract 15D features (Qwen2.5-1.5B scorer on cuda:3)
- Re-run GroupKFold(5) + LightGBM pairwise classification

## LaTeX Stripping Statistics
| Depth | Docs | Avg len (orig) | Avg len (stripped) | Reduction |
|-------|------|---------------|-------------------|-----------|
| 0     | 2200 | 1404          | 1396              | 0.6%      |
| 1     | 2200 | 900           | 892               | 0.9%      |
| 2     | 2200 | 989           | 970               | 2.0%      |
| 3     | 2200 | 1012          | 984               | 2.8%      |
| 4     | 2200 | 1001          | 964               | 3.6%      |
| 5     | 2200 | 966           | 923               | 4.4%      |

Note: Reduction increases with depth because the model generates more LaTeX at deeper generations.

## Pairwise AUC Comparison (theta=0.60)
| Pair | Original (exp-024) | LaTeX Stripped (exp-027) | Delta |
|------|-------------------|-------------------------|-------|
| 0v1  | **0.9948**        | **0.9948**              | 0.000 |
| 1v2  | **0.8581**        | **0.8297**              | -0.028|
| 2v3  | **0.6436**        | **0.6229**              | -0.021|
| 3v4  | 0.5440            | 0.5468                  | +0.003|
| 4v5  | 0.5299            | 0.5476                  | +0.018|

## K* Determination
- Original: K*=3 (2v3=0.6436 > 0.60, 3v4=0.544 < 0.60)
- **LaTeX Stripped: K*=3** (2v3=0.6229 > 0.60, 3v4=0.547 < 0.60)

## JSD Comparison
| Pair | Original | Stripped | Delta |
|------|----------|---------|-------|
| 0v1  | 0.2030   | 0.2015  | -0.002|
| 1v2  | 0.0773   | 0.0625  | -0.015|
| 2v3  | 0.0198   | 0.0161  | -0.004|
| 3v4  | 0.0083   | 0.0076  | -0.001|
| 4v5  | 0.0077   | 0.0076  | 0.000 |

## Feature Importance (Top-5)
| Rank | Original       | Stripped       |
|------|---------------|---------------|
| 1    | freq_entropy  | freq_entropy  |
| 2    | surp_std      | surp_std      |
| 3    | surp_mean     | surp_d1_skew  |
| 4    | surp_d1_skew  | surp_d1_mean  |
| 5    | surp_d1_mean  | surp_mean     |

## Ordinal Classification
| Metric   | Original | Stripped |
|----------|----------|---------|
| MAE      | 0.8256   | 0.8817  |
| Accuracy | 0.4767   | 0.4589  |

## Conclusion
**K*=3 is preserved after LaTeX removal.** The AUC values decrease slightly (by 0.02-0.03) for depths 1v2 and 2v3, and increase slightly for 3v4 and 4v5, but the K* boundary remains unchanged. This confirms that the depth-3 saturation point for arXiv data is NOT driven by LaTeX formatting artifacts. The signal comes from genuine statistical properties of iteratively generated text.
