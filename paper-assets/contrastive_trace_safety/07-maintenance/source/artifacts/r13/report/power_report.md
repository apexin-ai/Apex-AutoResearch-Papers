# R13: Post-hoc Power Analysis for Paired Comparisons

## Method
Within-pair standard deviations estimated from 5-seed HB results (R12).
Back-calculated from 95% CIs: sd = CI_half_width * sqrt(n) / t_{0.975,n-1}.
Power computed via noncentral t-distribution for two-sided paired t-test at alpha=0.05.

## Estimated Within-pair SD (balanced accuracy)

| Model | SD |
|-------|----|
| R1-32B | 0.1631 |
| QwQ-32B | 0.1768 |
| 32B pooled | 0.1699 |
| R1-8B | 0.2052 |
| OT-7B | 0.1945 |

## Power Table

| Model | n | Effect (pp) | Cohen's d | Power |
|-------|---|-------------|-----------|-------|
| R1-32B | 30 | 5 | 0.31 | 0.368 |
| R1-32B | 30 | 10 | 0.61 | 0.901 |
| R1-32B | 30 | 15 | 0.92 | 0.998 |
| R1-32B | 30 | 20 | 1.23 | 1.000 |
| QwQ-32B | 29 | 5 | 0.28 | 0.313 |
| QwQ-32B | 29 | 10 | 0.57 | 0.837 |
| QwQ-32B | 29 | 15 | 0.85 | 0.993 |
| QwQ-32B | 29 | 20 | 1.13 | 1.000 |
| 32B (pooled) | 20 | 5 | 0.29 | 0.239 |
| 32B (pooled) | 20 | 10 | 0.59 | 0.704 |
| 32B (pooled) | 20 | 15 | 0.88 | 0.963 |
| 32B (pooled) | 20 | 20 | 1.18 | 0.999 |
| R1-8B | 63 | 5 | 0.24 | 0.478 |
| R1-8B | 63 | 10 | 0.49 | 0.968 |
| R1-8B | 63 | 15 | 0.73 | 1.000 |
| R1-8B | 63 | 20 | 0.97 | 1.000 |
| R1-8B | 43 | 5 | 0.24 | 0.345 |
| R1-8B | 43 | 10 | 0.49 | 0.877 |
| R1-8B | 43 | 15 | 0.73 | 0.997 |
| R1-8B | 43 | 20 | 0.97 | 1.000 |
| OT-7B | 69 | 5 | 0.26 | 0.558 |
| OT-7B | 69 | 10 | 0.51 | 0.988 |
| OT-7B | 69 | 15 | 0.77 | 1.000 |
| OT-7B | 69 | 20 | 1.03 | 1.000 |
| OT-7B | 47 | 5 | 0.26 | 0.407 |
| OT-7B | 47 | 10 | 0.51 | 0.932 |
| OT-7B | 47 | 15 | 0.77 | 0.999 |
| OT-7B | 47 | 20 | 1.03 | 1.000 |

## Minimum Detectable Effect (80% power, alpha=0.05)

| Model | n | MDE (pp) | Cohen's d |
|-------|---|----------|-----------|
| R1-32B | 30 | 8.6 | 0.53 |
| QwQ-32B | 29 | 9.5 | 0.54 |
| 32B (pooled) | 20 | 11.2 | 0.66 |
| R1-8B | 63 | 7.4 | 0.36 |
| R1-8B | 43 | 9.0 | 0.44 |
| OT-7B | 69 | 6.7 | 0.34 |
| OT-7B | 47 | 8.1 | 0.42 |

## Key Takeaway

With n=29-30 paired traces (32B models), we have 90% power to detect a 10pp BA difference at alpha=0.05 (MDE for 80% power: ~8.6-9.5pp). The 7-8B models (n=63-69) achieve >97% power for the same effect size.