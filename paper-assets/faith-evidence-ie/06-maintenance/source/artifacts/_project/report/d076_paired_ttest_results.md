# D076 Statistical Significance Analysis

**Protocol**: D076: batch_size=4, no-quantize, sft_adapter, max_new_tokens=1024
**Test type**: seed-level paired/one-sample t-test (n=4 seeds)
**Note**: Per-document paired t-test unavailable (predictions.json not saved in reeval runs). Using seed-level comparison as alternative.

## Summary Table

| Comparison | Metric | Mean diff | t-stat | p-value | 95% CI | Cohen's d | Sig |
|:-----------|:-------|:---------|:-------|:--------|:-------|:----------|:----|
| CED - SFT | f1 | +0.0514 | 18.456 | 0.0003 | [0.4474, 0.4652] | 9.228 | YES |
| CED - SFT | ign_f1 | +0.0491 | 18.436 | 0.0003 | [0.4381, 0.4550] | 9.218 | YES |
| CED - SFT | evi_f1 | +0.0129 | 3.790 | 0.0322 | [0.8007, 0.8224] | 1.895 | YES |
| CED - SFT | edcr | -0.0479 | -9.382 | 0.0026 | [0.6340, 0.6665] | -4.691 | YES |
| flat-NLI - SFT | f1 | +0.0522 | 29.070 | 0.0001 | [0.4515, 0.4629] | 14.535 | YES |
| flat-NLI - SFT | ign_f1 | +0.0509 | 29.687 | 0.0001 | [0.4429, 0.4538] | 14.843 | YES |
| flat-NLI - SFT | evi_f1 | +0.0123 | 4.961 | 0.0157 | [0.8030, 0.8188] | 2.481 | YES |
| flat-NLI - SFT | edcr | -0.0485 | -20.635 | 0.0002 | [0.6423, 0.6572] | -10.318 | YES |
| CED - flat-NLI | f1 | -0.0009 | -0.754 | 0.5059 | [-0.0046, 0.0028] | -0.377 | no |
| CED - flat-NLI | ign_f1 | -0.0018 | -1.547 | 0.2196 | [-0.0055, 0.0019] | -0.774 | no |
| CED - flat-NLI | evi_f1 | +0.0006 | 0.126 | 0.9079 | [-0.0147, 0.0159] | 0.063 | no |
| CED - flat-NLI | edcr | +0.0005 | 0.119 | 0.9125 | [-0.0139, 0.0150] | 0.060 | no |

## Per-Seed Data (F1)

| Seed | CED | flat-NLI | SFT |
|:-----|:----|:---------|:----|
| 42 | 0.4517 | 0.4535 | 0.4049 |
| 43 | 0.4601 | 0.4586 | 0.4049 |
| 44 | 0.4621 | 0.4615 | 0.4049 |
| 45 | 0.4514 | 0.4551 | 0.4049 |
| **Mean** | **0.4563** | **0.4572** | **0.4049** |
| **Std** | **0.0056** | **0.0036** | -- |

## Conclusions

### 1. CED RSFT vs SFT baseline
- F1: +0.0514 (t=18.456, p=0.0003, d=9.23)
- **Significant** at alpha=0.05

### 2. flat-NLI RSFT vs SFT baseline
- F1: +0.0522 (t=29.070, p=0.0001, d=14.54)
- **Significant** at alpha=0.05

### 3. CED RSFT vs flat-NLI RSFT (core question)
- F1: -0.0009 (t=-0.754, p=0.5059, d=-0.38)
- **NOT significant** at alpha=0.05
- CED and flat-NLI are **statistically indistinguishable**

### Key Takeaway

Both RSFT methods significantly outperform SFT baseline, but are statistically indistinguishable from each other. Supports C3 (CED ~ flat-NLI) and C1 (evidence tax recovered by RSFT).

### Limitations
- n=4 seeds gives low statistical power (high Type II error risk)
- One-sample tests against SFT use single baseline value (no seed variance for SFT)
- Per-document paired t-test unavailable due to missing predictions.json in reeval outputs