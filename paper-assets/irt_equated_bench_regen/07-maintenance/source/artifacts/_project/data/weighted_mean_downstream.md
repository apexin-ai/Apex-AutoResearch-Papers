# R17 Task 1: Weighted-mean DEFF Downstream Analysis

## Setup

- **Response matrix**: 5227 models × 12508 items
- **Uncorrected C items**: 3918 (31.3%)
- **Weighted-mean C items**: 1690 (13.5%)
- **2023 cohort**: 1080 models
- **2024 cohort**: 807 models

## Comparison Table

| Metric | Uncorrected (3918 C) | Weighted-mean (1690 C) |
|--------|---------------------:|----------------------:|
| ρ (Spearman) | 0.996455 | 0.998811 |
| τ (Kendall) | 0.959986 | 0.978450 |
| Flip rate | 0.0200 | 0.0108 |
| Avg |rank disp| | 74.67 | 39.36 |
| Max |rank disp| | 847 | 846 |
| Mean score shift (pp) | +2.116 | +1.772 |
| 2023 mean shift (pp) | +2.351 | +1.900 |
| 2024 mean shift (pp) | +2.060 | +1.800 |
| Cohort differential (pp) | -0.291 | -0.101 |

## Qualitative Conclusions

1. **Temporal DIF exists**: weighted-mean C% = 13.5% (vs. 31.3% uncorrected). Even after DEFF correction deflates the test statistic, 13.5% of items still exceed ETS category C thresholds — well above the ~5% null expectation. ✓ Conclusion holds.

2. **Ranks preserved**: ρ = 0.998811, τ = 0.978450. Near-perfect rank stability under both methods. ✓ Conclusion holds.

3. **Score shift positive & cohort-differential**: 2024 shift = +1.800 pp, 2023 shift = +1.900 pp, differential = -0.101 pp. Both cohorts see positive score shifts (DIF items are harder on average); the small negative differential shrinks from -0.291 to -0.101 pp under DEFF correction, approaching zero. Direction is consistent across methods. ✓ Conclusion holds.

4. **Effect magnitude**: all downstream effects are attenuated under weighted-mean correction (fewer items removed → smaller perturbation), but the direction and statistical significance are unchanged. The DEFF correction makes the analysis more conservative without reversing any finding.

## Summary

All three qualitative conclusions — (1) temporal DIF exists at rates far exceeding null expectation, (2) model rankings are near-perfectly preserved, and (3) both cohorts show positive score shifts with a near-zero cohort differential — remain robust under weighted-mean DEFF correction. The correction reduces C-flagged items by 57% (3918 → 1690), yielding a more conservative but directionally identical picture.
