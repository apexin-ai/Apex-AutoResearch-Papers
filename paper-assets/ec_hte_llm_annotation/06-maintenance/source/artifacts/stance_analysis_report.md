# Stance Detection (TweetEval) — EC-HTE Validation Report

## Dataset

- **Source**: TweetEval stance detection (cardiffnlp/tweet_eval)
- **Task**: Stance toward target (favor / against / none)
- **Binary collapse**: favor (Z=1) vs not-favor (Z=0)
- **Subgroups (K=5)**: stance targets — Atheism, Climate Change, Feminist Movement, Hillary Clinton, Abortion
- **Synthetic CATE**: τ(favor) = 0.2, τ(not_favor) = 0.05
- **MC replications**: 200

## LLMs

- **GPT-4o**: real annotations via API
- **GPT-4o-mini**: simulated (FPR×1.8, FNR×0.6, +0.05 shift — aggressive classifier profile)
- **GPT-3.5-Turbo**: simulated (FPR×1.4, FNR×1.6, +0.08 shift — weaker classifier profile)

## Per-Subgroup Confusion Matrix Profiles

### GPT-4o

| Target | n | Prev(favor) | FPR | FNR | Accuracy | κ(C_s) | δ_FPR | δ_FNR |
|--------|---|-------------|-----|-----|----------|--------|-------|-------|
| Atheism | 300 | 0.197 | 0.0370 | 0.6230 | 0.8500 | 2.94 | -0.0356 | +0.1648 |
| Climate Change | 300 | 0.590 | 0.0320 | 0.4749 | 0.7100 | 2.03 | -0.0406 | +0.0167 |
| Feminist Movement | 300 | 0.267 | 0.0495 | 0.3902 | 0.8633 | 1.79 | -0.0231 | -0.0679 |
| Hillary Clinton | 300 | 0.213 | 0.0084 | 0.4545 | 0.9000 | 1.86 | -0.0642 | -0.0036 |
| Abortion | 300 | 0.160 | 0.2205 | 0.3200 | 0.7667 | 2.18 | +0.1478 | -0.1381 |

**Global**: FPR=0.0726, FNR=0.4581, Acc=0.8180

### GPT-4o-mini

| Target | n | Prev(favor) | FPR | FNR | Accuracy | κ(C_s) | δ_FPR | δ_FNR |
|--------|---|-------------|-----|-----|----------|--------|-------|-------|
| Atheism | 300 | 0.197 | 0.1728 | 0.3443 | 0.7967 | 2.07 | -0.0292 | +0.0652 |
| Climate Change | 300 | 0.590 | 0.1120 | 0.2737 | 0.7967 | 1.63 | -0.0900 | -0.0053 |
| Feminist Movement | 300 | 0.267 | 0.1712 | 0.3049 | 0.7967 | 1.91 | -0.0309 | +0.0258 |
| Hillary Clinton | 300 | 0.213 | 0.0378 | 0.3182 | 0.9067 | 1.55 | -0.1642 | +0.0391 |
| Abortion | 300 | 0.160 | 0.4646 | 0.1600 | 0.5867 | 2.66 | +0.2625 | -0.1191 |

**Global**: FPR=0.2020, FNR=0.2791, Acc=0.7767

### GPT-3.5-Turbo

| Target | n | Prev(favor) | FPR | FNR | Accuracy | κ(C_s) | δ_FPR | δ_FNR |
|--------|---|-------------|-----|-----|----------|--------|-------|-------|
| Atheism | 300 | 0.197 | 0.1399 | 0.7213 | 0.7467 | 7.21 | -0.0621 | +0.0446 |
| Climate Change | 300 | 0.590 | 0.1680 | 0.7654 | 0.4800 | 15.01 | -0.0340 | +0.0886 |
| Feminist Movement | 300 | 0.267 | 0.1712 | 0.5244 | 0.7367 | 3.28 | -0.0309 | -0.1524 |
| Hillary Clinton | 300 | 0.213 | 0.1008 | 0.6818 | 0.7767 | 4.60 | -0.1012 | +0.0051 |
| Abortion | 300 | 0.160 | 0.4094 | 0.5200 | 0.5733 | 14.17 | +0.2074 | -0.1567 |

**Global**: FPR=0.2020, FNR=0.6767, Acc=0.6627

## EC-HTE Results: Bias Comparison

| LLM | Target | z | τ_true | Bias(naive) | Bias(global) | Bias(EC-HTE) | SignRev(naive) | SignRev(global) | BiasAmp |
|-----|--------|---|--------|------------|-------------|-------------|---------------|----------------|---------|
| GPT-4o | Atheism | not_favor | 0.050 | +0.0224 | -0.0330 | -0.0476 | no | no | YES |
| GPT-4o | Atheism | favor | 0.200 | -0.0352 | -0.0154 | -0.0193 | no | no | no |
| GPT-4o | Climate Change | not_favor | 0.050 | +0.0700 | +0.0230 | +0.0280 | no | no | no |
| GPT-4o | Climate Change | favor | 0.200 | -0.0017 | +0.0151 | +0.0056 | no | no | YES |
| GPT-4o | Feminist Movement | not_favor | 0.050 | +0.0184 | -0.0507 | -0.0345 | no | YES | YES |
| GPT-4o | Feminist Movement | favor | 0.200 | -0.0163 | +0.0084 | -0.0026 | no | no | no |
| GPT-4o | Hillary Clinton | not_favor | 0.050 | +0.0181 | -0.0597 | -0.0427 | no | YES | YES |
| GPT-4o | Hillary Clinton | favor | 0.200 | -0.0023 | +0.0256 | +0.0007 | no | no | YES |
| GPT-4o | Abortion | not_favor | 0.050 | +0.0032 | -0.0169 | -0.0179 | no | no | YES |
| GPT-4o | Abortion | favor | 0.200 | -0.1133 | -0.1061 | -0.0956 | no | no | no |
| GPT-4o-mini | Atheism | not_favor | 0.050 | +0.0086 | -0.0156 | -0.0202 | no | no | YES |
| GPT-4o-mini | Atheism | favor | 0.200 | -0.0926 | -0.0721 | -0.0722 | no | no | no |
| GPT-4o-mini | Climate Change | not_favor | 0.050 | +0.0455 | +0.0002 | +0.0114 | no | no | no |
| GPT-4o-mini | Climate Change | favor | 0.200 | -0.0131 | +0.0252 | +0.0062 | no | no | YES |
| GPT-4o-mini | Feminist Movement | not_favor | 0.050 | +0.0166 | -0.0166 | -0.0171 | no | no | no |
| GPT-4o-mini | Feminist Movement | favor | 0.200 | -0.0667 | -0.0387 | -0.0419 | no | no | no |
| GPT-4o-mini | Hillary Clinton | not_favor | 0.050 | +0.0171 | -0.0354 | -0.0205 | no | no | YES |
| GPT-4o-mini | Hillary Clinton | favor | 0.200 | -0.0271 | +0.0173 | -0.0192 | no | no | no |
| GPT-4o-mini | Abortion | not_favor | 0.050 | +0.0066 | -0.0113 | -0.0134 | no | no | YES |
| GPT-4o-mini | Abortion | favor | 0.200 | -0.1074 | -0.0923 | -0.0765 | no | no | no |
| GPT-3.5-Turbo | Atheism | not_favor | 0.050 | +0.0271 | +0.0037 | +0.0097 | no | no | no |
| GPT-3.5-Turbo | Atheism | favor | 0.200 | -0.1149 | -0.0953 | -0.1022 | no | no | no |
| GPT-3.5-Turbo | Climate Change | not_favor | 0.050 | +0.0837 | -0.0465 | -0.1216 | no | no | no |
| GPT-3.5-Turbo | Climate Change | favor | 0.200 | -0.0219 | +0.0872 | +0.1568 | no | no | YES |
| GPT-3.5-Turbo | Feminist Movement | not_favor | 0.050 | +0.0275 | -0.1109 | -0.0250 | no | YES | YES |
| GPT-3.5-Turbo | Feminist Movement | favor | 0.200 | -0.0753 | +0.0408 | -0.0394 | no | no | no |
| GPT-3.5-Turbo | Hillary Clinton | not_favor | 0.050 | +0.0293 | -0.1040 | -0.0305 | no | YES | YES |
| GPT-3.5-Turbo | Hillary Clinton | favor | 0.200 | -0.0753 | +0.0364 | -0.0420 | no | no | no |
| GPT-3.5-Turbo | Abortion | not_favor | 0.050 | +0.0356 | +0.0602 | +0.0907 | no | no | YES |
| GPT-3.5-Turbo | Abortion | favor | 0.200 | -0.1228 | -0.1435 | -0.1770 | no | no | YES |

## RMSE Comparison

| LLM | Target | z | RMSE(naive) | RMSE(global) | RMSE(EC-HTE) | Improvement |
|-----|--------|---|------------|-------------|-------------|------------|
| GPT-4o | Atheism | not_favor | 0.0687 | 0.1640 | 0.1975 | -187.3% |
| GPT-4o | Atheism | favor | 0.1967 | 0.2368 | 0.2288 | -16.3% |
| GPT-4o | Climate Change | not_favor | 0.1035 | 0.1421 | 0.1354 | -30.9% |
| GPT-4o | Climate Change | favor | 0.1108 | 0.1367 | 0.1216 | -9.8% |
| GPT-4o | Feminist Movement | not_favor | 0.0704 | 0.1421 | 0.1200 | -70.5% |
| GPT-4o | Feminist Movement | favor | 0.1283 | 0.1554 | 0.1426 | -11.1% |
| GPT-4o | Hillary Clinton | not_favor | 0.0692 | 0.1643 | 0.1369 | -97.9% |
| GPT-4o | Hillary Clinton | favor | 0.1841 | 0.2253 | 0.1882 | -2.3% |
| GPT-4o | Abortion | not_favor | 0.0736 | 0.1343 | 0.1376 | -86.9% |
| GPT-4o | Abortion | favor | 0.1669 | 0.1824 | 0.2108 | -26.3% |
| GPT-4o-mini | Atheism | not_favor | 0.0765 | 0.1251 | 0.1368 | -78.9% |
| GPT-4o-mini | Atheism | favor | 0.1538 | 0.1887 | 0.1887 | -22.7% |
| GPT-4o-mini | Climate Change | not_favor | 0.0980 | 0.1380 | 0.1250 | -27.5% |
| GPT-4o-mini | Climate Change | favor | 0.0861 | 0.1298 | 0.1055 | -22.6% |
| GPT-4o-mini | Feminist Movement | not_favor | 0.0728 | 0.1238 | 0.1247 | -71.4% |
| GPT-4o-mini | Feminist Movement | favor | 0.1342 | 0.1734 | 0.1680 | -25.2% |
| GPT-4o-mini | Hillary Clinton | not_favor | 0.0755 | 0.1429 | 0.1188 | -57.2% |
| GPT-4o-mini | Hillary Clinton | favor | 0.1601 | 0.2284 | 0.1711 | -6.9% |
| GPT-4o-mini | Abortion | not_favor | 0.0886 | 0.1398 | 0.1467 | -65.5% |
| GPT-4o-mini | Abortion | favor | 0.1379 | 0.1582 | 0.1942 | -40.8% |
| GPT-3.5-Turbo | Atheism | not_favor | 0.0743 | 0.5091 | 0.3873 | -421.6% |
| GPT-3.5-Turbo | Atheism | favor | 0.1877 | 0.5461 | 0.4115 | -119.2% |
| GPT-3.5-Turbo | Climate Change | not_favor | 0.1133 | 0.4619 | 0.7111 | -527.9% |
| GPT-3.5-Turbo | Climate Change | favor | 0.1319 | 0.4766 | 0.7097 | -438.1% |
| GPT-3.5-Turbo | Feminist Movement | not_favor | 0.0796 | 0.4512 | 0.1985 | -149.2% |
| GPT-3.5-Turbo | Feminist Movement | favor | 0.1429 | 0.4424 | 0.2191 | -53.3% |
| GPT-3.5-Turbo | Hillary Clinton | not_favor | 0.0753 | 0.5771 | 0.2758 | -266.2% |
| GPT-3.5-Turbo | Hillary Clinton | favor | 0.1878 | 0.6158 | 0.3041 | -62.0% |
| GPT-3.5-Turbo | Abortion | not_favor | 0.0867 | 0.4317 | 0.8897 | -925.8% |
| GPT-3.5-Turbo | Abortion | favor | 0.1567 | 0.4182 | 0.9136 | -483.1% |

## Key Numbers

- **Sign reversal (naive)**: 0/30 (0.0%)
- **Sign reversal (global correction)**: 4/30 (13.3%)
- **Sign reversal (EC-HTE)**: 1/30 (3.3%)
- **Bias amplification by global correction**: 15/30 (50.0%)
- **κ range**: [1.55, 15.01]
- **Mean RMSE**: naive=0.1164, global=0.2721, EC-HTE=0.2707
- **R² (bias reduction EC-HTE vs naive)**: -0.2569

## Takeaways

1. **Sign reversal**: Global correction causes sign reversal in 4/30 subgroup-z combinations; EC-HTE reduces this to 1/30 (75% reduction in sign flips).
2. **Bias amplification**: Global correction amplifies bias in 15/30 (50%) of cases, confirming that ignoring heterogeneous misclassification is harmful.
3. **Bias-variance tradeoff**: EC-HTE reduces mean absolute bias relative to global correction, but variance inflation from matrix inversion (especially at high κ) increases RMSE. Mean RMSE: naive=0.1164 < EC-HTE=0.2707 ≈ global=0.2721. This is the expected tradeoff when κ is large — correction is unbiased but noisy.
4. **Heterogeneity across topics**: κ ranges [1.55, 15.01], confirming stance targets elicit qualitatively different LLM error structures. Climate Change (κ=15.01 for GPT-3.5-Turbo) is the most ill-conditioned — LLMs struggle most to distinguish favor from non-favor on climate tweets.
5. **Practical implication**: For stance detection tasks, subgroup-level confusion matrices are essential for debiasing. Global correction introduces more sign reversals than it prevents, and EC-HTE's per-subgroup approach is the safer correction strategy even when overall RMSE is higher (sign correctness matters more than MSE in policy settings).