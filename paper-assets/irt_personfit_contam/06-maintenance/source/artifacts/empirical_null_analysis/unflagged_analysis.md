# Unflagged Cells Deep Analysis

## Yi-Lightning / arc_c

- **Observed lz***: 1.6643
- **Empirical p-value** (v2): 0.0950
- **BH-adjusted p-value**: 0.0983
- **Bootstrap null**: mean=0.0381, std=1.0077, skew=-0.0352, kurtosis=-0.3677
- **KS test vs N(0,1)**: D=0.0389, p=0.09392
- **Observed lz* percentile** in null: 94.5%
- **P(|lz*| >= |obs|)**: 9.5%

The observed lz* (1.664) is moderate — within the range that the bootstrap null can plausibly produce. Unlike most other cells where |lz*| >> 3, this cell's response pattern is not dramatically inconsistent with the 4PL model.

arc_c has 295 items. 
ARC-Challenge has 295 items — moderate size. Yi-Lightning's lz* is positive but not extreme enough to reject after multiple testing correction.


## 360GPT2-Pro / humaneval

- **Observed lz***: 1.5036
- **Empirical p-value** (v2): 0.1320
- **BH-adjusted p-value**: 0.1342
- **Bootstrap null**: mean=0.0753, std=1.0020, skew=-0.2651, kurtosis=-0.1147
- **KS test vs N(0,1)**: D=0.0598, p=0.00151
- **Observed lz* percentile** in null: 93.0%
- **P(|lz*| >= |obs|)**: 13.2%

The observed lz* (1.504) is moderate — within the range that the bootstrap null can plausibly produce. Unlike most other cells where |lz*| >> 3, this cell's response pattern is not dramatically inconsistent with the 4PL model.

humaneval has 164 items. 
HumanEval's small item count (164) limits the power of lz* — fewer items mean higher variance in the statistic, making it harder to reject the null even when some misfit exists.


## Yi-Lightning / humaneval

- **Observed lz***: 1.3537
- **Empirical p-value** (v2): 0.1810
- **BH-adjusted p-value**: 0.1810
- **Bootstrap null**: mean=0.0275, std=1.0148, skew=-0.3448, kurtosis=0.1090
- **KS test vs N(0,1)**: D=0.0630, p=0.0006733
- **Observed lz* percentile** in null: 91.9%
- **P(|lz*| >= |obs|)**: 18.1%

The observed lz* (1.354) is moderate — within the range that the bootstrap null can plausibly produce. Unlike most other cells where |lz*| >> 3, this cell's response pattern is not dramatically inconsistent with the 4PL model.

humaneval has 164 items. 
HumanEval's small item count (164) limits the power of lz* — fewer items mean higher variance in the statistic, making it harder to reject the null even when some misfit exists.

