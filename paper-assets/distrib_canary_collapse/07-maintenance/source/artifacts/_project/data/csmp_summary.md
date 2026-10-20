CSMP results on westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/csmp_results/

Calibration (α=0.00 null, 3 seeds):
| k | h | FAR |
|---|---|-----|
| 0.05 | 1.5297 | 0% |
| 0.1 | 1.0047 | 0% |
| 0.25 | ~0 | 0% |

Evaluation (intervention experiments):
| k | predictive alarm | reactive alarm |
|---|-----------------|---------------|
| 0.05 | gen 3 (EDD=2) | gen 2 (EDD=0) |
| 0.1 | gen 1 (EDD=0) | gen 1 (EDD=-1) |
| 0.25 | gen 1 (EDD=0) | gen 1 (EDD=-1) |

Recommended: k=0.25, null CUSUM statistic stays at zero, immediate collapse detection.