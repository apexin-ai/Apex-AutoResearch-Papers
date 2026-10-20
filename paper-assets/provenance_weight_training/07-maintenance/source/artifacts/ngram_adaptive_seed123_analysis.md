# ngram_adaptive_seed123 Analysis

## Training Summary
- **Status**: Completed normally (EXIT_CODE=0)
- **Total steps**: 6,103
- **Train loss**: 9.289
- **Training time**: ~3h54m
- **Checkpoint**: `/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed123/final`

## Holdout Evaluation
| Metric | Value |
|--------|-------|
| Holdout PPL | **17.823** |
| Holdout loss | 2.8805 |
| Eval tokens | 4,077,068 |

## Comparison

| Experiment | Holdout PPL | Delta vs Uniform Mean |
|------------|------------|----------------------|
| **ngram_adaptive_seed123** | **17.823** | **+0.129 (worse)** |
| ngram_adaptive_seed42 | 17.820 | +0.126 (worse) |
| Uniform 3-seed mean | 17.694 ± 0.008 | baseline |
| uniform_seed42 | 17.694 | — |
| uniform_seed123 | 17.686 | — |
| uniform_seed456 | 17.702 | — |

## Conclusion: **Negative**

seed123 的 PPL (17.823) 与 seed42 (17.820) 高度一致，两者均显著高于 uniform baseline 均值 (17.694)，差值约 +0.13，是 uniform 标准差 (0.008) 的 16 倍。

这确认了 seed42 观察到的 negative pattern：**N-gram PPL detector (AUC=0.73) + adaptive weighting 组合在不同 seed 下稳定地劣于 uniform baseline**。该 detector 的 AUC 仅 0.73（弱统计检测器），其质量信号噪声过大，adaptive weighting 放大了噪声而非信号。
