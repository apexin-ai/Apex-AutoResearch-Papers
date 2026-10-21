# exp-019 Mistral-7B Bootstrap CI (10000 resamples)

| Pair | AUC | CI lower | CI upper | CI lower > 0.60? |
|------|-----|----------|----------|-----------------|
| 0v1 | 0.9842 | 0.9824 | 0.9860 | PASS |
| 1v2 | 0.5934 | 0.5835 | 0.6032 | **FAIL** |
| 2v3 | 0.5402 | 0.5301 | 0.5510 | FAIL |
| 3v4 | 0.5233 | 0.5128 | 0.5338 | FAIL |
| 4v5 | 0.5180 | 0.5070 | 0.5287 | FAIL |

K* (CI-based) = 1. p(AUC_1v2 <= 0.60) = 0.9017.

vs exp-016 Qwen-base: 1v2 CI [0.6168, 0.6353], K*=2 solid.