# PCA + Leave-One-Group-Out Analysis (9-cell)

## PCA Effective Dimensions
| Threshold | 9-cell avg | Range | merged_all |
|-----------|-----------|-------|-----------|
| 90% | 6-7 pc | 6–7 | 7 |
| 95% | 7-9 pc | 7–9 | 9 |
| 99% | 11-13 pc | 11–13 | 13 |

19维特征中6-7个主成分解释90%方差，特征空间存在显著冗余。

## Leave-One-Group-Out (mean Δacc across 9 cells)
| 排除组 | 特征数 | mean Δacc |
|--------|--------|-----------|
| **perplexity** | 9 | **-0.0353** |
| surprisal | 3 | -0.0054 |
| repetition | 3 | -0.0022 |
| lexical_diversity | 2 | -0.0010 |
| ngram_entropy | 2 | -0.0006 |

Perplexity组最关键，排除后acc平均下降3.5%。Surprisal次之(-0.54%)。Lexical diversity和ngram entropy几乎无影响。

## Server artifacts
- results/feature_ablation/pca_effective_dims.json
- results/feature_ablation/leave_one_group_out.json
- results/feature_ablation/pca_scree_plot.pdf / .png
- src/pca_effective_dims.py
- src/leave_one_group_out.py