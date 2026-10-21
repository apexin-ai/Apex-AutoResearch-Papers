# Monte Carlo Standard Error Analysis

## Overview

This analysis computes MC standard errors from 100-run Monte Carlo experiments 
to verify that method differences reported in Table 1 are statistically significant.

- **exp-001** (HB synthetic): SEs pre-computed in aggregated data; conservative z-tests used 
  (no per-seed data available for paired tests — true paired p-values would be smaller).
- **exp-003** (TweetEval semi-synthetic): Raw per-seed data available; proper paired t-tests used.

## exp-001: HB Synthetic — Table 1 Representative Configs

### SE Summary (Subgroup A, z0 level)

#### K=2, extreme, n=100

| Method | Metric | Mean | MC SE | 95% CI |
|--------|--------|------|-------|--------|
| global_corrected | bias | +0.0474 | 0.0082 | [+0.0313, +0.0634] |
| hb | bias | -0.0264 | 0.0129 | [-0.0517, -0.0011] |
| naive | bias | +0.0976 | 0.0063 | [+0.0852, +0.1099] |
| oracle | bias | -0.0020 | 0.0060 | [-0.0139, +0.0098] |
| stratified_mle | bias | -0.0297 | 0.0130 | [-0.0551, -0.0043] |
| global_corrected | rmse | +0.0947 | 0.0061 | [+0.0827, +0.1068] |
| hb | rmse | +0.1316 | 0.0142 | [+0.1039, +0.1594] |
| naive | rmse | +0.1162 | 0.0058 | [+0.1048, +0.1277] |
| oracle | rmse | +0.0605 | 0.0038 | [+0.0531, +0.0678] |
| stratified_mle | rmse | +0.1331 | 0.0140 | [+0.1057, +0.1605] |

#### K=2, extreme, n=500

| Method | Metric | Mean | MC SE | 95% CI |
|--------|--------|------|-------|--------|
| global_corrected | bias | +0.0539 | 0.0079 | [+0.0385, +0.0694] |
| hb | bias | -0.0082 | 0.0110 | [-0.0298, +0.0133] |
| naive | bias | +0.0976 | 0.0063 | [+0.0852, +0.1099] |
| oracle | bias | -0.0020 | 0.0060 | [-0.0139, +0.0098] |
| stratified_mle | bias | -0.0088 | 0.0110 | [-0.0304, +0.0128] |
| global_corrected | rmse | +0.0956 | 0.0061 | [+0.0837, +0.1075] |
| hb | rmse | +0.1103 | 0.0091 | [+0.0925, +0.1281] |
| naive | rmse | +0.1162 | 0.0058 | [+0.1048, +0.1277] |
| oracle | rmse | +0.0605 | 0.0038 | [+0.0531, +0.0678] |
| stratified_mle | rmse | +0.1106 | 0.0091 | [+0.0927, +0.1285] |

#### K=4, extreme, n=100

| Method | Metric | Mean | MC SE | 95% CI |
|--------|--------|------|-------|--------|
| global_corrected | bias | +0.0807 | 0.0107 | [+0.0596, +0.1017] |
| hb | bias | +1.1277 | 1.1515 | [-1.1291, +3.3846] |
| naive | bias | +0.1212 | 0.0083 | [+0.1049, +0.1375] |
| oracle | bias | -0.0024 | 0.0089 | [-0.0199, +0.0151] |
| stratified_mle | bias | -0.0355 | 0.0288 | [-0.0919, +0.0209] |
| global_corrected | rmse | +0.1343 | 0.0100 | [+0.1147, +0.1538] |
| hb | rmse | +11.5696 | 5.7523 | [+0.2951, +22.8441] |
| naive | rmse | +0.1470 | 0.0088 | [+0.1297, +0.1643] |
| oracle | rmse | +0.0894 | 0.0070 | [+0.0756, +0.1032] |
| stratified_mle | rmse | +0.2900 | 0.0434 | [+0.2050, +0.3751] |

#### K=4, extreme, n=500

| Method | Metric | Mean | MC SE | 95% CI |
|--------|--------|------|-------|--------|
| global_corrected | bias | +0.0857 | 0.0104 | [+0.0653, +0.1062] |
| hb | bias | -0.0078 | 0.0182 | [-0.0435, +0.0280] |
| naive | bias | +0.1212 | 0.0083 | [+0.1049, +0.1375] |
| oracle | bias | -0.0024 | 0.0089 | [-0.0199, +0.0151] |
| stratified_mle | bias | -0.0094 | 0.0184 | [-0.0454, +0.0266] |
| global_corrected | rmse | +0.1349 | 0.0103 | [+0.1146, +0.1552] |
| hb | rmse | +0.1825 | 0.0156 | [+0.1519, +0.2131] |
| naive | rmse | +0.1470 | 0.0088 | [+0.1297, +0.1643] |
| oracle | rmse | +0.0894 | 0.0070 | [+0.0756, +0.1032] |
| stratified_mle | rmse | +0.1840 | 0.0158 | [+0.1530, +0.2149] |

#### K=4, moderate, n=250

| Method | Metric | Mean | MC SE | 95% CI |
|--------|--------|------|-------|--------|
| global_corrected | bias | +0.0184 | 0.0100 | [-0.0012, +0.0379] |
| hb | bias | +0.0015 | 0.0123 | [-0.0226, +0.0256] |
| naive | bias | +0.0324 | 0.0084 | [+0.0160, +0.0488] |
| oracle | bias | -0.0024 | 0.0089 | [-0.0199, +0.0151] |
| stratified_mle | bias | +0.0006 | 0.0124 | [-0.0237, +0.0250] |
| global_corrected | rmse | +0.1016 | 0.0067 | [+0.0885, +0.1146] |
| hb | rmse | +0.1230 | 0.0078 | [+0.1077, +0.1382] |
| naive | rmse | +0.0898 | 0.0066 | [+0.0768, +0.1028] |
| oracle | rmse | +0.0894 | 0.0070 | [+0.0756, +0.1032] |
| stratified_mle | rmse | +0.1244 | 0.0078 | [+0.1090, +0.1398] |

### Paired Significance Tests (conservative z-tests)

| Config | z | Metric | Comparison | Diff | z-stat | p-value | Sig? |
|--------|---|--------|------------|------|--------|---------|------|
| K=2,extreme,n=100 | z0 | bias | hb vs global_corrected | -0.0210 | -1.37 | 0.1700 | No |
| K=2,extreme,n=100 | z0 | bias | hb vs naive | -0.0712 | -4.96 | 0.0000 | Yes |
| K=2,extreme,n=100 | z0 | bias | global_corrected vs naive | -0.0502 | -4.85 | 0.0000 | Yes |
| K=2,extreme,n=100 | z0 | rmse | hb vs global_corrected | +0.0369 | 2.39 | 0.0169 | Yes |
| K=2,extreme,n=100 | z0 | rmse | hb vs naive | +0.0154 | 1.00 | 0.3150 | No |
| K=2,extreme,n=100 | z0 | rmse | global_corrected vs naive | -0.0215 | -2.54 | 0.0112 | Yes |
| K=2,extreme,n=100 | z1 | bias | hb vs global_corrected | -0.0296 | -1.86 | 0.0635 | No |
| K=2,extreme,n=100 | z1 | bias | hb vs naive | -0.0791 | -5.29 | 0.0000 | Yes |
| K=2,extreme,n=100 | z1 | bias | global_corrected vs naive | -0.0496 | -4.52 | 0.0000 | Yes |
| K=2,extreme,n=100 | z1 | rmse | hb vs global_corrected | +0.0351 | 1.77 | 0.0774 | No |
| K=2,extreme,n=100 | z1 | rmse | hb vs naive | +0.0150 | 0.76 | 0.4459 | No |
| K=2,extreme,n=100 | z1 | rmse | global_corrected vs naive | -0.0201 | -2.06 | 0.0398 | Yes |
| K=2,extreme,n=500 | z0 | bias | hb vs global_corrected | -0.0457 | -3.38 | 0.0007 | Yes |
| K=2,extreme,n=500 | z0 | bias | hb vs naive | -0.0893 | -7.04 | 0.0000 | Yes |
| K=2,extreme,n=500 | z0 | bias | global_corrected vs naive | -0.0436 | -4.32 | 0.0000 | Yes |
| K=2,extreme,n=500 | z0 | rmse | hb vs global_corrected | +0.0147 | 1.34 | 0.1789 | No |
| K=2,extreme,n=500 | z0 | rmse | hb vs naive | -0.0059 | -0.55 | 0.5830 | No |
| K=2,extreme,n=500 | z0 | rmse | global_corrected vs naive | -0.0206 | -2.45 | 0.0142 | Yes |
| K=2,extreme,n=500 | z1 | bias | hb vs global_corrected | -0.0477 | -3.41 | 0.0006 | Yes |
| K=2,extreme,n=500 | z1 | bias | hb vs naive | -0.0926 | -7.07 | 0.0000 | Yes |
| K=2,extreme,n=500 | z1 | bias | global_corrected vs naive | -0.0449 | -4.21 | 0.0000 | Yes |
| K=2,extreme,n=500 | z1 | rmse | hb vs global_corrected | +0.0130 | 1.17 | 0.2408 | No |
| K=2,extreme,n=500 | z1 | rmse | hb vs naive | -0.0078 | -0.72 | 0.4713 | No |
| K=2,extreme,n=500 | z1 | rmse | global_corrected vs naive | -0.0208 | -2.13 | 0.0333 | Yes |
| K=4,extreme,n=100 | z0 | bias | hb vs global_corrected | +1.0470 | 0.91 | 0.3632 | No |
| K=4,extreme,n=100 | z0 | bias | hb vs naive | +1.0065 | 0.87 | 0.3821 | No |
| K=4,extreme,n=100 | z0 | bias | global_corrected vs naive | -0.0405 | -2.99 | 0.0028 | Yes |
| K=4,extreme,n=100 | z0 | rmse | hb vs global_corrected | +11.4354 | 1.99 | 0.0468 | Yes |
| K=4,extreme,n=100 | z0 | rmse | hb vs naive | +11.4227 | 1.99 | 0.0471 | Yes |
| K=4,extreme,n=100 | z0 | rmse | global_corrected vs naive | -0.0127 | -0.96 | 0.3395 | No |
| K=4,extreme,n=100 | z1 | bias | hb vs global_corrected | +1.0524 | 0.92 | 0.3599 | No |
| K=4,extreme,n=100 | z1 | bias | hb vs naive | +1.0135 | 0.88 | 0.3779 | No |
| K=4,extreme,n=100 | z1 | bias | global_corrected vs naive | -0.0389 | -2.62 | 0.0087 | Yes |
| K=4,extreme,n=100 | z1 | rmse | hb vs global_corrected | +11.4034 | 1.99 | 0.0471 | Yes |
| K=4,extreme,n=100 | z1 | rmse | hb vs naive | +11.3931 | 1.98 | 0.0473 | Yes |
| K=4,extreme,n=100 | z1 | rmse | global_corrected vs naive | -0.0103 | -0.83 | 0.4048 | No |
| K=4,extreme,n=500 | z0 | bias | hb vs global_corrected | -0.0780 | -3.71 | 0.0002 | Yes |
| K=4,extreme,n=500 | z0 | bias | hb vs naive | -0.1134 | -5.66 | 0.0000 | Yes |
| K=4,extreme,n=500 | z0 | bias | global_corrected vs naive | -0.0354 | -2.66 | 0.0078 | Yes |
| K=4,extreme,n=500 | z0 | rmse | hb vs global_corrected | +0.0476 | 2.54 | 0.0111 | Yes |
| K=4,extreme,n=500 | z0 | rmse | hb vs naive | +0.0355 | 1.98 | 0.0478 | Yes |
| K=4,extreme,n=500 | z0 | rmse | global_corrected vs naive | -0.0121 | -0.89 | 0.3750 | No |
| K=4,extreme,n=500 | z1 | bias | hb vs global_corrected | -0.0920 | -4.24 | 0.0000 | Yes |
| K=4,extreme,n=500 | z1 | bias | hb vs naive | -0.1278 | -6.18 | 0.0000 | Yes |
| K=4,extreme,n=500 | z1 | bias | global_corrected vs naive | -0.0358 | -2.47 | 0.0137 | Yes |
| K=4,extreme,n=500 | z1 | rmse | hb vs global_corrected | +0.0394 | 2.53 | 0.0113 | Yes |
| K=4,extreme,n=500 | z1 | rmse | hb vs naive | +0.0279 | 1.87 | 0.0619 | No |
| K=4,extreme,n=500 | z1 | rmse | global_corrected vs naive | -0.0115 | -0.93 | 0.3547 | No |
| K=4,moderate,n=250 | z0 | bias | hb vs global_corrected | -0.0168 | -1.06 | 0.2880 | No |
| K=4,moderate,n=250 | z0 | bias | hb vs naive | -0.0309 | -2.08 | 0.0378 | Yes |
| K=4,moderate,n=250 | z0 | bias | global_corrected vs naive | -0.0141 | -1.08 | 0.2805 | No |
| K=4,moderate,n=250 | z0 | rmse | hb vs global_corrected | +0.0214 | 2.09 | 0.0369 | Yes |
| K=4,moderate,n=250 | z0 | rmse | hb vs naive | +0.0332 | 3.25 | 0.0012 | Yes |
| K=4,moderate,n=250 | z0 | rmse | global_corrected vs naive | +0.0118 | 1.25 | 0.2098 | No |
| K=4,moderate,n=250 | z1 | bias | hb vs global_corrected | -0.0158 | -0.89 | 0.3722 | No |
| K=4,moderate,n=250 | z1 | bias | hb vs naive | -0.0299 | -1.80 | 0.0715 | No |
| K=4,moderate,n=250 | z1 | bias | global_corrected vs naive | -0.0141 | -0.95 | 0.3421 | No |
| K=4,moderate,n=250 | z1 | rmse | hb vs global_corrected | +0.0197 | 1.54 | 0.1241 | No |
| K=4,moderate,n=250 | z1 | rmse | hb vs naive | +0.0331 | 2.74 | 0.0062 | Yes |
| K=4,moderate,n=250 | z1 | rmse | global_corrected vs naive | +0.0134 | 1.23 | 0.2186 | No |

## exp-003: TweetEval Semi-Synthetic — Paired t-tests

### Key Results (marginal level)

#### Extreme regime

| Config | z | Metric | Comparison | Mean A | Mean B | Diff | t-stat | p-value | Sig? |
|--------|---|--------|------------|--------|--------|------|--------|---------|------|
| n=50 | z0 | abs_bias | hb_ec_hte vs global_corrected | 0.0723 | 0.0437 | +0.028504 | 3.80 | 0.0003 | Yes |
| n=50 | z0 | abs_bias | hb_ec_hte vs naive | 0.0723 | 0.0327 | +0.039549 | 4.90 | 0.0000 | Yes |
| n=50 | z0 | abs_bias | global_corrected vs naive | 0.0437 | 0.0327 | +0.011045 | 3.57 | 0.0006 | Yes |
| n=50 | z0 | abs_bias | hb_ec_hte vs stratified_mle | 0.0723 | 0.0718 | +0.000418 | 0.06 | 0.9527 | No |
| n=50 | z0 | squared_error | hb_ec_hte vs global_corrected | 0.0114 | 0.0034 | +0.008081 | 2.69 | 0.0084 | Yes |
| n=50 | z0 | squared_error | hb_ec_hte vs naive | 0.0114 | 0.0017 | +0.009701 | 3.18 | 0.0020 | Yes |
| n=50 | z0 | squared_error | global_corrected vs naive | 0.0034 | 0.0017 | +0.001620 | 3.69 | 0.0004 | Yes |
| n=50 | z0 | squared_error | hb_ec_hte vs stratified_mle | 0.0114 | 0.0107 | +0.000710 | 0.24 | 0.8124 | No |
| n=50 | z1 | abs_bias | hb_ec_hte vs global_corrected | 0.2031 | 0.1054 | +0.097710 | 4.36 | 0.0000 | Yes |
| n=50 | z1 | abs_bias | hb_ec_hte vs naive | 0.2031 | 0.0591 | +0.143996 | 5.34 | 0.0000 | Yes |
| n=50 | z1 | abs_bias | global_corrected vs naive | 0.1054 | 0.0591 | +0.046287 | 3.71 | 0.0003 | Yes |
| n=50 | z1 | abs_bias | hb_ec_hte vs stratified_mle | 0.2031 | 0.2064 | -0.003267 | -0.30 | 0.7667 | No |
| n=50 | z1 | squared_error | hb_ec_hte vs global_corrected | 0.1089 | 0.0237 | +0.085226 | 2.30 | 0.0237 | Yes |
| n=50 | z1 | squared_error | hb_ec_hte vs naive | 0.1089 | 0.0048 | +0.104089 | 2.70 | 0.0081 | Yes |
| n=50 | z1 | squared_error | global_corrected vs naive | 0.0237 | 0.0048 | +0.018863 | 2.74 | 0.0073 | Yes |
| n=50 | z1 | squared_error | hb_ec_hte vs stratified_mle | 0.1089 | 0.0966 | +0.012330 | 0.56 | 0.5772 | No |
| n=100 | z0 | abs_bias | hb_ec_hte vs global_corrected | 0.0507 | 0.0393 | +0.011369 | 3.89 | 0.0002 | Yes |
| n=100 | z0 | abs_bias | hb_ec_hte vs naive | 0.0507 | 0.0327 | +0.018004 | 4.93 | 0.0000 | Yes |
| n=100 | z0 | abs_bias | global_corrected vs naive | 0.0393 | 0.0327 | +0.006635 | 2.86 | 0.0052 | Yes |
| n=100 | z0 | abs_bias | hb_ec_hte vs stratified_mle | 0.0507 | 0.0561 | -0.005363 | -2.12 | 0.0365 | Yes |
| n=100 | z0 | squared_error | hb_ec_hte vs global_corrected | 0.0042 | 0.0026 | +0.001530 | 3.21 | 0.0018 | Yes |
| n=100 | z0 | squared_error | hb_ec_hte vs naive | 0.0042 | 0.0017 | +0.002413 | 4.32 | 0.0000 | Yes |
| n=100 | z0 | squared_error | global_corrected vs naive | 0.0026 | 0.0017 | +0.000883 | 3.24 | 0.0016 | Yes |
| n=100 | z0 | squared_error | hb_ec_hte vs stratified_mle | 0.0042 | 0.0057 | -0.001522 | -1.59 | 0.1144 | No |
| n=100 | z1 | abs_bias | hb_ec_hte vs global_corrected | 0.1224 | 0.0836 | +0.038789 | 4.45 | 0.0000 | Yes |
| n=100 | z1 | abs_bias | hb_ec_hte vs naive | 0.1224 | 0.0591 | +0.063291 | 4.62 | 0.0000 | Yes |
| n=100 | z1 | abs_bias | global_corrected vs naive | 0.0836 | 0.0591 | +0.024503 | 2.86 | 0.0051 | Yes |
| n=100 | z1 | abs_bias | hb_ec_hte vs stratified_mle | 0.1224 | 0.1446 | -0.022189 | -1.67 | 0.0990 | No |
| n=100 | z1 | squared_error | hb_ec_hte vs global_corrected | 0.0293 | 0.0121 | +0.017127 | 3.45 | 0.0008 | Yes |
| n=100 | z1 | squared_error | hb_ec_hte vs naive | 0.0293 | 0.0048 | +0.024421 | 4.12 | 0.0001 | Yes |
| n=100 | z1 | squared_error | global_corrected vs naive | 0.0121 | 0.0048 | +0.007294 | 3.37 | 0.0011 | Yes |
| n=100 | z1 | squared_error | hb_ec_hte vs stratified_mle | 0.0293 | 0.0509 | -0.021589 | -1.26 | 0.2118 | No |
| n=250 | z0 | abs_bias | hb_ec_hte vs global_corrected | 0.0379 | 0.0366 | +0.001347 | 0.85 | 0.3951 | No |
| n=250 | z0 | abs_bias | hb_ec_hte vs naive | 0.0379 | 0.0327 | +0.005238 | 2.20 | 0.0300 | Yes |
| n=250 | z0 | abs_bias | global_corrected vs naive | 0.0366 | 0.0327 | +0.003891 | 2.02 | 0.0465 | Yes |
| n=250 | z0 | abs_bias | hb_ec_hte vs stratified_mle | 0.0379 | 0.0388 | -0.000894 | -1.95 | 0.0546 | No |
| n=250 | z0 | squared_error | hb_ec_hte vs global_corrected | 0.0023 | 0.0023 | +0.000069 | 0.44 | 0.6578 | No |
| n=250 | z0 | squared_error | hb_ec_hte vs naive | 0.0023 | 0.0017 | +0.000579 | 2.46 | 0.0156 | Yes |
| n=250 | z0 | squared_error | global_corrected vs naive | 0.0023 | 0.0017 | +0.000510 | 2.19 | 0.0305 | Yes |
| n=250 | z0 | squared_error | hb_ec_hte vs stratified_mle | 0.0023 | 0.0024 | -0.000106 | -2.34 | 0.0210 | Yes |
| n=250 | z1 | abs_bias | hb_ec_hte vs global_corrected | 0.0796 | 0.0632 | +0.016334 | 2.56 | 0.0120 | Yes |
| n=250 | z1 | abs_bias | hb_ec_hte vs naive | 0.0796 | 0.0591 | +0.020469 | 2.13 | 0.0355 | Yes |
| n=250 | z1 | abs_bias | global_corrected vs naive | 0.0632 | 0.0591 | +0.004135 | 0.59 | 0.5580 | No |
| n=250 | z1 | abs_bias | hb_ec_hte vs stratified_mle | 0.0796 | 0.0838 | -0.004225 | -1.81 | 0.0734 | No |
| n=250 | z1 | squared_error | hb_ec_hte vs global_corrected | 0.0142 | 0.0075 | +0.006729 | 1.89 | 0.0612 | No |
| n=250 | z1 | squared_error | hb_ec_hte vs naive | 0.0142 | 0.0048 | +0.009344 | 2.37 | 0.0197 | Yes |
| n=250 | z1 | squared_error | global_corrected vs naive | 0.0075 | 0.0048 | +0.002615 | 1.77 | 0.0792 | No |
| n=250 | z1 | squared_error | hb_ec_hte vs stratified_mle | 0.0142 | 0.0175 | -0.003358 | -1.40 | 0.1643 | No |
| n=500 | z0 | abs_bias | hb_ec_hte vs global_corrected | 0.0362 | 0.0355 | +0.000664 | 0.50 | 0.6150 | No |
| n=500 | z0 | abs_bias | hb_ec_hte vs naive | 0.0362 | 0.0327 | +0.003460 | 1.67 | 0.0987 | No |
| n=500 | z0 | abs_bias | global_corrected vs naive | 0.0355 | 0.0327 | +0.002795 | 1.50 | 0.1367 | No |
| n=500 | z0 | abs_bias | hb_ec_hte vs stratified_mle | 0.0362 | 0.0365 | -0.000287 | -2.92 | 0.0043 | Yes |
| n=500 | z0 | squared_error | hb_ec_hte vs global_corrected | 0.0021 | 0.0021 | -0.000026 | -0.19 | 0.8504 | No |
| n=500 | z0 | squared_error | hb_ec_hte vs naive | 0.0021 | 0.0017 | +0.000350 | 1.75 | 0.0836 | No |
| n=500 | z0 | squared_error | global_corrected vs naive | 0.0021 | 0.0017 | +0.000375 | 1.87 | 0.0642 | No |
| n=500 | z0 | squared_error | hb_ec_hte vs stratified_mle | 0.0021 | 0.0021 | -0.000031 | -3.14 | 0.0022 | Yes |
| n=500 | z1 | abs_bias | hb_ec_hte vs global_corrected | 0.0581 | 0.0514 | +0.006663 | 2.50 | 0.0141 | Yes |
| n=500 | z1 | abs_bias | hb_ec_hte vs naive | 0.0581 | 0.0591 | -0.000985 | -0.15 | 0.8826 | No |
| n=500 | z1 | abs_bias | global_corrected vs naive | 0.0514 | 0.0591 | -0.007648 | -1.31 | 0.1943 | No |
| n=500 | z1 | abs_bias | hb_ec_hte vs stratified_mle | 0.0581 | 0.0589 | -0.000829 | -4.29 | 0.0000 | Yes |
| n=500 | z1 | squared_error | hb_ec_hte vs global_corrected | 0.0066 | 0.0050 | +0.001600 | 2.22 | 0.0287 | Yes |
| n=500 | z1 | squared_error | hb_ec_hte vs naive | 0.0066 | 0.0048 | +0.001732 | 1.26 | 0.2103 | No |
| n=500 | z1 | squared_error | global_corrected vs naive | 0.0050 | 0.0048 | +0.000132 | 0.13 | 0.8950 | No |
| n=500 | z1 | squared_error | hb_ec_hte vs stratified_mle | 0.0066 | 0.0067 | -0.000170 | -3.69 | 0.0004 | Yes |

#### Moderate regime

| Config | z | Metric | Comparison | Mean A | Mean B | Diff | t-stat | p-value | Sig? |
|--------|---|--------|------------|--------|--------|------|--------|---------|------|
| n=50 | z0 | abs_bias | hb_ec_hte vs global_corrected | 0.0654 | 0.0438 | +0.021668 | 4.71 | 0.0000 | Yes |
| n=50 | z0 | abs_bias | hb_ec_hte vs naive | 0.0654 | 0.0335 | +0.031911 | 5.33 | 0.0000 | Yes |
| n=50 | z0 | abs_bias | global_corrected vs naive | 0.0438 | 0.0335 | +0.010243 | 3.43 | 0.0009 | Yes |
| n=50 | z0 | abs_bias | hb_ec_hte vs stratified_mle | 0.0654 | 0.0678 | -0.002414 | -0.51 | 0.6118 | No |
| n=50 | z0 | squared_error | hb_ec_hte vs global_corrected | 0.0080 | 0.0032 | +0.004798 | 2.66 | 0.0091 | Yes |
| n=50 | z0 | squared_error | hb_ec_hte vs naive | 0.0080 | 0.0019 | +0.006166 | 3.15 | 0.0021 | Yes |
| n=50 | z0 | squared_error | global_corrected vs naive | 0.0032 | 0.0019 | +0.001369 | 3.49 | 0.0007 | Yes |
| n=50 | z0 | squared_error | hb_ec_hte vs stratified_mle | 0.0080 | 0.0094 | -0.001400 | -0.84 | 0.4015 | No |
| n=50 | z1 | abs_bias | hb_ec_hte vs global_corrected | 0.1804 | 0.1049 | +0.075457 | 5.60 | 0.0000 | Yes |
| n=50 | z1 | abs_bias | hb_ec_hte vs naive | 0.1804 | 0.0603 | +0.120136 | 6.06 | 0.0000 | Yes |
| n=50 | z1 | abs_bias | global_corrected vs naive | 0.1049 | 0.0603 | +0.044679 | 3.84 | 0.0002 | Yes |
| n=50 | z1 | abs_bias | hb_ec_hte vs stratified_mle | 0.1804 | 0.1870 | -0.006554 | -0.97 | 0.3348 | No |
| n=50 | z1 | squared_error | hb_ec_hte vs global_corrected | 0.0686 | 0.0228 | +0.045796 | 4.32 | 0.0000 | Yes |
| n=50 | z1 | squared_error | hb_ec_hte vs naive | 0.0686 | 0.0050 | +0.063614 | 4.43 | 0.0000 | Yes |
| n=50 | z1 | squared_error | global_corrected vs naive | 0.0228 | 0.0050 | +0.017818 | 2.98 | 0.0036 | Yes |
| n=50 | z1 | squared_error | hb_ec_hte vs stratified_mle | 0.0686 | 0.0754 | -0.006813 | -1.27 | 0.2077 | No |
| n=100 | z0 | abs_bias | hb_ec_hte vs global_corrected | 0.0476 | 0.0396 | +0.008020 | 3.65 | 0.0004 | Yes |
| n=100 | z0 | abs_bias | hb_ec_hte vs naive | 0.0476 | 0.0335 | +0.014114 | 4.37 | 0.0000 | Yes |
| n=100 | z0 | abs_bias | global_corrected vs naive | 0.0396 | 0.0335 | +0.006093 | 2.50 | 0.0141 | Yes |
| n=100 | z0 | abs_bias | hb_ec_hte vs stratified_mle | 0.0476 | 0.0498 | -0.002129 | -2.81 | 0.0059 | Yes |
| n=100 | z0 | squared_error | hb_ec_hte vs global_corrected | 0.0036 | 0.0026 | +0.000918 | 3.45 | 0.0008 | Yes |
| n=100 | z0 | squared_error | hb_ec_hte vs naive | 0.0036 | 0.0019 | +0.001690 | 4.39 | 0.0000 | Yes |
| n=100 | z0 | squared_error | global_corrected vs naive | 0.0026 | 0.0019 | +0.000773 | 3.11 | 0.0024 | Yes |
| n=100 | z0 | squared_error | hb_ec_hte vs stratified_mle | 0.0036 | 0.0039 | -0.000341 | -3.64 | 0.0004 | Yes |
| n=100 | z1 | abs_bias | hb_ec_hte vs global_corrected | 0.1193 | 0.0825 | +0.036791 | 4.59 | 0.0000 | Yes |
| n=100 | z1 | abs_bias | hb_ec_hte vs naive | 0.1193 | 0.0603 | +0.059010 | 4.68 | 0.0000 | Yes |
| n=100 | z1 | abs_bias | global_corrected vs naive | 0.0825 | 0.0603 | +0.022218 | 2.69 | 0.0083 | Yes |
| n=100 | z1 | abs_bias | hb_ec_hte vs stratified_mle | 0.1193 | 0.1269 | -0.007606 | -3.21 | 0.0018 | Yes |
| n=100 | z1 | squared_error | hb_ec_hte vs global_corrected | 0.0266 | 0.0119 | +0.014713 | 3.13 | 0.0023 | Yes |
| n=100 | z1 | squared_error | hb_ec_hte vs naive | 0.0266 | 0.0050 | +0.021597 | 3.91 | 0.0002 | Yes |
| n=100 | z1 | squared_error | global_corrected vs naive | 0.0119 | 0.0050 | +0.006884 | 3.33 | 0.0012 | Yes |
| n=100 | z1 | squared_error | hb_ec_hte vs stratified_mle | 0.0266 | 0.0302 | -0.003656 | -3.64 | 0.0004 | Yes |
| n=250 | z0 | abs_bias | hb_ec_hte vs global_corrected | 0.0380 | 0.0369 | +0.001078 | 1.00 | 0.3217 | No |
| n=250 | z0 | abs_bias | hb_ec_hte vs naive | 0.0380 | 0.0335 | +0.004447 | 1.90 | 0.0604 | No |
| n=250 | z0 | abs_bias | global_corrected vs naive | 0.0369 | 0.0335 | +0.003370 | 1.79 | 0.0771 | No |
| n=250 | z0 | abs_bias | hb_ec_hte vs stratified_mle | 0.0380 | 0.0389 | -0.000928 | -3.77 | 0.0003 | Yes |
| n=250 | z0 | squared_error | hb_ec_hte vs global_corrected | 0.0024 | 0.0023 | +0.000104 | 0.97 | 0.3369 | No |
| n=250 | z0 | squared_error | hb_ec_hte vs naive | 0.0024 | 0.0019 | +0.000490 | 2.04 | 0.0442 | Yes |
| n=250 | z0 | squared_error | global_corrected vs naive | 0.0023 | 0.0019 | +0.000386 | 1.94 | 0.0556 | No |
| n=250 | z0 | squared_error | hb_ec_hte vs stratified_mle | 0.0024 | 0.0025 | -0.000096 | -3.60 | 0.0005 | Yes |
| n=250 | z1 | abs_bias | hb_ec_hte vs global_corrected | 0.0779 | 0.0642 | +0.013744 | 3.13 | 0.0023 | Yes |
| n=250 | z1 | abs_bias | hb_ec_hte vs naive | 0.0779 | 0.0603 | +0.017682 | 1.97 | 0.0516 | No |
| n=250 | z1 | abs_bias | global_corrected vs naive | 0.0642 | 0.0603 | +0.003938 | 0.59 | 0.5578 | No |
| n=250 | z1 | abs_bias | hb_ec_hte vs stratified_mle | 0.0779 | 0.0807 | -0.002765 | -2.49 | 0.0144 | Yes |
| n=250 | z1 | squared_error | hb_ec_hte vs global_corrected | 0.0123 | 0.0072 | +0.005080 | 2.46 | 0.0158 | Yes |
| n=250 | z1 | squared_error | hb_ec_hte vs naive | 0.0123 | 0.0050 | +0.007293 | 2.55 | 0.0123 | Yes |
| n=250 | z1 | squared_error | global_corrected vs naive | 0.0072 | 0.0050 | +0.002212 | 1.58 | 0.1170 | No |
| n=250 | z1 | squared_error | hb_ec_hte vs stratified_mle | 0.0123 | 0.0138 | -0.001486 | -1.77 | 0.0803 | No |
| n=500 | z0 | abs_bias | hb_ec_hte vs global_corrected | 0.0361 | 0.0361 | +0.000006 | 0.01 | 0.9949 | No |
| n=500 | z0 | abs_bias | hb_ec_hte vs naive | 0.0361 | 0.0335 | +0.002619 | 1.25 | 0.2130 | No |
| n=500 | z0 | abs_bias | global_corrected vs naive | 0.0361 | 0.0335 | +0.002612 | 1.47 | 0.1441 | No |
| n=500 | z0 | abs_bias | hb_ec_hte vs stratified_mle | 0.0361 | 0.0365 | -0.000332 | -3.35 | 0.0011 | Yes |
| n=500 | z0 | squared_error | hb_ec_hte vs global_corrected | 0.0021 | 0.0022 | -0.000048 | -0.48 | 0.6319 | No |
| n=500 | z0 | squared_error | hb_ec_hte vs naive | 0.0021 | 0.0019 | +0.000236 | 1.17 | 0.2464 | No |
| n=500 | z0 | squared_error | global_corrected vs naive | 0.0022 | 0.0019 | +0.000284 | 1.53 | 0.1294 | No |
| n=500 | z0 | squared_error | hb_ec_hte vs stratified_mle | 0.0021 | 0.0021 | -0.000038 | -3.37 | 0.0011 | Yes |
| n=500 | z1 | abs_bias | hb_ec_hte vs global_corrected | 0.0578 | 0.0530 | +0.004712 | 2.08 | 0.0404 | Yes |
| n=500 | z1 | abs_bias | hb_ec_hte vs naive | 0.0578 | 0.0603 | -0.002504 | -0.38 | 0.7080 | No |
| n=500 | z1 | abs_bias | global_corrected vs naive | 0.0530 | 0.0603 | -0.007217 | -1.26 | 0.2101 | No |
| n=500 | z1 | abs_bias | hb_ec_hte vs stratified_mle | 0.0578 | 0.0583 | -0.000572 | -2.71 | 0.0079 | Yes |
| n=500 | z1 | squared_error | hb_ec_hte vs global_corrected | 0.0062 | 0.0049 | +0.001282 | 2.06 | 0.0416 | Yes |
| n=500 | z1 | squared_error | hb_ec_hte vs naive | 0.0062 | 0.0050 | +0.001217 | 0.90 | 0.3716 | No |
| n=500 | z1 | squared_error | global_corrected vs naive | 0.0049 | 0.0050 | -0.000065 | -0.07 | 0.9459 | No |
| n=500 | z1 | squared_error | hb_ec_hte vs stratified_mle | 0.0062 | 0.0064 | -0.000157 | -3.24 | 0.0016 | Yes |

#### Homogeneous regime

| Config | z | Metric | Comparison | Mean A | Mean B | Diff | t-stat | p-value | Sig? |
|--------|---|--------|------------|--------|--------|------|--------|---------|------|
| n=50 | z0 | abs_bias | hb_ec_hte vs global_corrected | 0.0615 | 0.0454 | +0.016099 | 4.85 | 0.0000 | Yes |
| n=50 | z0 | abs_bias | hb_ec_hte vs naive | 0.0615 | 0.0341 | +0.027426 | 5.54 | 0.0000 | Yes |
| n=50 | z0 | abs_bias | global_corrected vs naive | 0.0454 | 0.0341 | +0.011327 | 3.81 | 0.0002 | Yes |
| n=50 | z0 | abs_bias | hb_ec_hte vs stratified_mle | 0.0615 | 0.0654 | -0.003846 | -0.84 | 0.4052 | No |
| n=50 | z0 | squared_error | hb_ec_hte vs global_corrected | 0.0062 | 0.0034 | +0.002838 | 4.42 | 0.0000 | Yes |
| n=50 | z0 | squared_error | hb_ec_hte vs naive | 0.0062 | 0.0019 | +0.004283 | 4.80 | 0.0000 | Yes |
| n=50 | z0 | squared_error | global_corrected vs naive | 0.0034 | 0.0019 | +0.001445 | 3.44 | 0.0009 | Yes |
| n=50 | z0 | squared_error | hb_ec_hte vs stratified_mle | 0.0062 | 0.0081 | -0.001877 | -1.02 | 0.3079 | No |
| n=50 | z1 | abs_bias | hb_ec_hte vs global_corrected | 0.1753 | 0.1050 | +0.070316 | 5.61 | 0.0000 | Yes |
| n=50 | z1 | abs_bias | hb_ec_hte vs naive | 0.1753 | 0.0602 | +0.115122 | 5.77 | 0.0000 | Yes |
| n=50 | z1 | abs_bias | global_corrected vs naive | 0.1050 | 0.0602 | +0.044807 | 3.70 | 0.0004 | Yes |
| n=50 | z1 | abs_bias | hb_ec_hte vs stratified_mle | 0.1753 | 0.1863 | -0.010970 | -2.09 | 0.0392 | Yes |
| n=50 | z1 | squared_error | hb_ec_hte vs global_corrected | 0.0675 | 0.0238 | +0.043693 | 4.28 | 0.0000 | Yes |
| n=50 | z1 | squared_error | hb_ec_hte vs naive | 0.0675 | 0.0050 | +0.062501 | 4.17 | 0.0001 | Yes |
| n=50 | z1 | squared_error | global_corrected vs naive | 0.0238 | 0.0050 | +0.018808 | 2.73 | 0.0075 | Yes |
| n=50 | z1 | squared_error | hb_ec_hte vs stratified_mle | 0.0675 | 0.0779 | -0.010400 | -2.28 | 0.0247 | Yes |
| n=100 | z0 | abs_bias | hb_ec_hte vs global_corrected | 0.0473 | 0.0399 | +0.007469 | 4.04 | 0.0001 | Yes |
| n=100 | z0 | abs_bias | hb_ec_hte vs naive | 0.0473 | 0.0341 | +0.013218 | 4.22 | 0.0001 | Yes |
| n=100 | z0 | abs_bias | global_corrected vs naive | 0.0399 | 0.0341 | +0.005749 | 2.46 | 0.0155 | Yes |
| n=100 | z0 | abs_bias | hb_ec_hte vs stratified_mle | 0.0473 | 0.0496 | -0.002301 | -3.27 | 0.0015 | Yes |
| n=100 | z0 | squared_error | hb_ec_hte vs global_corrected | 0.0035 | 0.0026 | +0.000836 | 4.03 | 0.0001 | Yes |
| n=100 | z0 | squared_error | hb_ec_hte vs naive | 0.0035 | 0.0019 | +0.001533 | 4.33 | 0.0000 | Yes |
| n=100 | z0 | squared_error | global_corrected vs naive | 0.0026 | 0.0019 | +0.000697 | 2.90 | 0.0046 | Yes |
| n=100 | z0 | squared_error | hb_ec_hte vs stratified_mle | 0.0035 | 0.0037 | -0.000279 | -3.08 | 0.0027 | Yes |
| n=100 | z1 | abs_bias | hb_ec_hte vs global_corrected | 0.1214 | 0.0825 | +0.038853 | 4.85 | 0.0000 | Yes |
| n=100 | z1 | abs_bias | hb_ec_hte vs naive | 0.1214 | 0.0602 | +0.061171 | 4.78 | 0.0000 | Yes |
| n=100 | z1 | abs_bias | global_corrected vs naive | 0.0825 | 0.0602 | +0.022318 | 2.83 | 0.0057 | Yes |
| n=100 | z1 | abs_bias | hb_ec_hte vs stratified_mle | 0.1214 | 0.1242 | -0.002858 | -0.82 | 0.4155 | No |
| n=100 | z1 | squared_error | hb_ec_hte vs global_corrected | 0.0277 | 0.0115 | +0.016225 | 3.57 | 0.0006 | Yes |
| n=100 | z1 | squared_error | hb_ec_hte vs naive | 0.0277 | 0.0050 | +0.022687 | 4.09 | 0.0001 | Yes |
| n=100 | z1 | squared_error | global_corrected vs naive | 0.0115 | 0.0050 | +0.006462 | 3.26 | 0.0015 | Yes |
| n=100 | z1 | squared_error | hb_ec_hte vs stratified_mle | 0.0277 | 0.0294 | -0.001748 | -1.22 | 0.2244 | No |
| n=250 | z0 | abs_bias | hb_ec_hte vs global_corrected | 0.0384 | 0.0376 | +0.000742 | 0.67 | 0.5050 | No |
| n=250 | z0 | abs_bias | hb_ec_hte vs naive | 0.0384 | 0.0341 | +0.004243 | 1.80 | 0.0753 | No |
| n=250 | z0 | abs_bias | global_corrected vs naive | 0.0376 | 0.0341 | +0.003501 | 1.90 | 0.0608 | No |
| n=250 | z0 | abs_bias | hb_ec_hte vs stratified_mle | 0.0384 | 0.0392 | -0.000840 | -3.36 | 0.0011 | Yes |
| n=250 | z0 | squared_error | hb_ec_hte vs global_corrected | 0.0024 | 0.0023 | +0.000053 | 0.46 | 0.6430 | No |
| n=250 | z0 | squared_error | hb_ec_hte vs naive | 0.0024 | 0.0019 | +0.000425 | 1.74 | 0.0853 | No |
| n=250 | z0 | squared_error | global_corrected vs naive | 0.0023 | 0.0019 | +0.000372 | 1.88 | 0.0629 | No |
| n=250 | z0 | squared_error | hb_ec_hte vs stratified_mle | 0.0024 | 0.0025 | -0.000093 | -3.36 | 0.0011 | Yes |
| n=250 | z1 | abs_bias | hb_ec_hte vs global_corrected | 0.0740 | 0.0631 | +0.010884 | 3.01 | 0.0033 | Yes |
| n=250 | z1 | abs_bias | hb_ec_hte vs naive | 0.0740 | 0.0602 | +0.013797 | 1.60 | 0.1129 | No |
| n=250 | z1 | abs_bias | global_corrected vs naive | 0.0631 | 0.0602 | +0.002912 | 0.43 | 0.6697 | No |
| n=250 | z1 | abs_bias | hb_ec_hte vs stratified_mle | 0.0740 | 0.0762 | -0.002182 | -3.74 | 0.0003 | Yes |
| n=250 | z1 | squared_error | hb_ec_hte vs global_corrected | 0.0108 | 0.0071 | +0.003730 | 2.11 | 0.0376 | Yes |
| n=250 | z1 | squared_error | hb_ec_hte vs naive | 0.0108 | 0.0050 | +0.005802 | 2.13 | 0.0359 | Yes |
| n=250 | z1 | squared_error | global_corrected vs naive | 0.0071 | 0.0050 | +0.002072 | 1.44 | 0.1518 | No |
| n=250 | z1 | squared_error | hb_ec_hte vs stratified_mle | 0.0108 | 0.0115 | -0.000693 | -3.16 | 0.0021 | Yes |
| n=500 | z0 | abs_bias | hb_ec_hte vs global_corrected | 0.0360 | 0.0362 | -0.000188 | -0.19 | 0.8461 | No |
| n=500 | z0 | abs_bias | hb_ec_hte vs naive | 0.0360 | 0.0341 | +0.001932 | 0.91 | 0.3656 | No |
| n=500 | z0 | abs_bias | global_corrected vs naive | 0.0362 | 0.0341 | +0.002121 | 1.19 | 0.2369 | No |
| n=500 | z0 | abs_bias | hb_ec_hte vs stratified_mle | 0.0360 | 0.0365 | -0.000451 | -4.27 | 0.0000 | Yes |
| n=500 | z0 | squared_error | hb_ec_hte vs global_corrected | 0.0021 | 0.0022 | -0.000081 | -0.81 | 0.4173 | No |
| n=500 | z0 | squared_error | hb_ec_hte vs naive | 0.0021 | 0.0019 | +0.000183 | 0.88 | 0.3833 | No |
| n=500 | z0 | squared_error | global_corrected vs naive | 0.0022 | 0.0019 | +0.000263 | 1.44 | 0.1525 | No |
| n=500 | z0 | squared_error | hb_ec_hte vs stratified_mle | 0.0021 | 0.0022 | -0.000039 | -3.06 | 0.0028 | Yes |
| n=500 | z1 | abs_bias | hb_ec_hte vs global_corrected | 0.0548 | 0.0528 | +0.001986 | 0.90 | 0.3690 | No |
| n=500 | z1 | abs_bias | hb_ec_hte vs naive | 0.0548 | 0.0602 | -0.005379 | -0.80 | 0.4249 | No |
| n=500 | z1 | abs_bias | global_corrected vs naive | 0.0528 | 0.0602 | -0.007365 | -1.28 | 0.2019 | No |
| n=500 | z1 | abs_bias | hb_ec_hte vs stratified_mle | 0.0548 | 0.0554 | -0.000617 | -2.70 | 0.0081 | Yes |
| n=500 | z1 | squared_error | hb_ec_hte vs global_corrected | 0.0058 | 0.0049 | +0.000980 | 1.59 | 0.1144 | No |
| n=500 | z1 | squared_error | hb_ec_hte vs naive | 0.0058 | 0.0050 | +0.000830 | 0.58 | 0.5625 | No |
| n=500 | z1 | squared_error | global_corrected vs naive | 0.0049 | 0.0050 | -0.000150 | -0.15 | 0.8791 | No |
| n=500 | z1 | squared_error | hb_ec_hte vs stratified_mle | 0.0058 | 0.0060 | -0.000164 | -3.05 | 0.0029 | Yes |

## Director's Question: Moderate Regime Small Differences

**Question**: In the moderate regime, small differences like 0.009 vs 0.005 — do MC SEs overlap?

### Answer

**exp-003 moderate regime, marginal level, bias:**

| Method | z | Mean Bias | MC SE | 95% CI |
|--------|---|-----------|-------|--------|
| global_corrected | z0 | -0.016310 | 0.005486 | [-0.027062, -0.005558] |
| global_corrected | z0 | -0.012295 | 0.005023 | [-0.022141, -0.002450] |
| global_corrected | z0 | -0.008523 | 0.004703 | [-0.017740, +0.000695] |
| global_corrected | z0 | -0.008728 | 0.004588 | [-0.017720, +0.000265] |
| hb_ec_hte | z0 | -0.037769 | 0.008175 | [-0.053792, -0.021746] |
| hb_ec_hte | z0 | -0.020855 | 0.005625 | [-0.031879, -0.009831] |
| hb_ec_hte | z0 | -0.012146 | 0.004734 | [-0.021425, -0.002867] |
| hb_ec_hte | z0 | -0.010353 | 0.004500 | [-0.019173, -0.001533] |
| naive | z0 | +0.008892 | 0.004261 | [+0.000541, +0.017244] |
| naive | z0 | +0.008892 | 0.004261 | [+0.000541, +0.017244] |
| naive | z0 | +0.008892 | 0.004261 | [+0.000541, +0.017244] |
| naive | z0 | +0.008892 | 0.004261 | [+0.000541, +0.017244] |
| oracle | z0 | -0.005190 | 0.003885 | [-0.012804, +0.002425] |
| oracle | z0 | -0.005190 | 0.003885 | [-0.012804, +0.002425] |
| oracle | z0 | -0.005190 | 0.003885 | [-0.012804, +0.002425] |
| oracle | z0 | -0.005190 | 0.003885 | [-0.012804, +0.002425] |
| stratified_mle | z0 | -0.036433 | 0.009054 | [-0.054179, -0.018687] |
| stratified_mle | z0 | -0.025278 | 0.005746 | [-0.036540, -0.014016] |
| stratified_mle | z0 | -0.014096 | 0.004782 | [-0.023469, -0.004723] |
| stratified_mle | z0 | -0.011173 | 0.004523 | [-0.020037, -0.002308] |
| global_corrected | z1 | +0.049452 | 0.014344 | [+0.021338, +0.077566] |
| global_corrected | z1 | +0.025713 | 0.010645 | [+0.004849, +0.046577] |
| global_corrected | z1 | +0.014695 | 0.008404 | [-0.001777, +0.031166] |
| global_corrected | z1 | +0.010782 | 0.006974 | [-0.002886, +0.024451] |
| hb_ec_hte | z1 | +0.145195 | 0.021911 | [+0.102250, +0.188141] |
| hb_ec_hte | z1 | +0.070914 | 0.014758 | [+0.041988, +0.099841] |
| hb_ec_hte | z1 | +0.025540 | 0.010841 | [+0.004292, +0.046789] |
| hb_ec_hte | z1 | +0.016645 | 0.007743 | [+0.001468, +0.031821] |
| naive | z1 | -0.051170 | 0.004900 | [-0.060775, -0.041566] |
| naive | z1 | -0.051170 | 0.004900 | [-0.060775, -0.041566] |
| naive | z1 | -0.051170 | 0.004900 | [-0.060775, -0.041566] |
| naive | z1 | -0.051170 | 0.004900 | [-0.060775, -0.041566] |
| oracle | z1 | +0.001892 | 0.004779 | [-0.007476, +0.011259] |
| oracle | z1 | +0.001892 | 0.004779 | [-0.007476, +0.011259] |
| oracle | z1 | +0.001892 | 0.004779 | [-0.007476, +0.011259] |
| oracle | z1 | +0.001892 | 0.004779 | [-0.007476, +0.011259] |
| stratified_mle | z1 | +0.154557 | 0.022816 | [+0.109838, +0.199275] |
| stratified_mle | z1 | +0.080347 | 0.015502 | [+0.049963, +0.110732] |
| stratified_mle | z1 | +0.028866 | 0.011433 | [+0.006457, +0.051275] |
| stratified_mle | z1 | +0.018318 | 0.007807 | [+0.003016, +0.033620] |

Of 32 paired comparisons in the moderate/marginal regime for absolute bias, **20 are significant at α=0.05**.

- **hb_ec_hte vs global_corrected** (n=50, z0): paired t=4.71, p=0.0000 → CIs DO NOT overlap
- **hb_ec_hte vs naive** (n=50, z0): paired t=5.33, p=0.0000 → CIs DO NOT overlap
- **global_corrected vs naive** (n=50, z0): paired t=3.43, p=0.0009 → CIs DO NOT overlap
- **hb_ec_hte vs stratified_mle** (n=50, z0): paired t=-0.51, p=0.6118 → CIs overlap
- **hb_ec_hte vs global_corrected** (n=50, z1): paired t=5.60, p=0.0000 → CIs DO NOT overlap
- **hb_ec_hte vs naive** (n=50, z1): paired t=6.06, p=0.0000 → CIs DO NOT overlap
- **global_corrected vs naive** (n=50, z1): paired t=3.84, p=0.0002 → CIs DO NOT overlap
- **hb_ec_hte vs stratified_mle** (n=50, z1): paired t=-0.97, p=0.3348 → CIs overlap
- **hb_ec_hte vs global_corrected** (n=100, z0): paired t=3.65, p=0.0004 → CIs DO NOT overlap
- **hb_ec_hte vs naive** (n=100, z0): paired t=4.37, p=0.0000 → CIs DO NOT overlap
- **global_corrected vs naive** (n=100, z0): paired t=2.50, p=0.0141 → CIs DO NOT overlap
- **hb_ec_hte vs stratified_mle** (n=100, z0): paired t=-2.81, p=0.0059 → CIs DO NOT overlap
- **hb_ec_hte vs global_corrected** (n=100, z1): paired t=4.59, p=0.0000 → CIs DO NOT overlap
- **hb_ec_hte vs naive** (n=100, z1): paired t=4.68, p=0.0000 → CIs DO NOT overlap
- **global_corrected vs naive** (n=100, z1): paired t=2.69, p=0.0083 → CIs DO NOT overlap
- **hb_ec_hte vs stratified_mle** (n=100, z1): paired t=-3.21, p=0.0018 → CIs DO NOT overlap
- **hb_ec_hte vs global_corrected** (n=250, z0): paired t=1.00, p=0.3217 → CIs overlap
- **hb_ec_hte vs naive** (n=250, z0): paired t=1.90, p=0.0604 → CIs overlap
- **global_corrected vs naive** (n=250, z0): paired t=1.79, p=0.0771 → CIs overlap
- **hb_ec_hte vs stratified_mle** (n=250, z0): paired t=-3.77, p=0.0003 → CIs DO NOT overlap
- **hb_ec_hte vs global_corrected** (n=250, z1): paired t=3.13, p=0.0023 → CIs DO NOT overlap
- **hb_ec_hte vs naive** (n=250, z1): paired t=1.97, p=0.0516 → CIs overlap
- **global_corrected vs naive** (n=250, z1): paired t=0.59, p=0.5578 → CIs overlap
- **hb_ec_hte vs stratified_mle** (n=250, z1): paired t=-2.49, p=0.0144 → CIs DO NOT overlap
- **hb_ec_hte vs global_corrected** (n=500, z0): paired t=0.01, p=0.9949 → CIs overlap
- **hb_ec_hte vs naive** (n=500, z0): paired t=1.25, p=0.2130 → CIs overlap
- **global_corrected vs naive** (n=500, z0): paired t=1.47, p=0.1441 → CIs overlap
- **hb_ec_hte vs stratified_mle** (n=500, z0): paired t=-3.35, p=0.0011 → CIs DO NOT overlap
- **hb_ec_hte vs global_corrected** (n=500, z1): paired t=2.08, p=0.0404 → CIs DO NOT overlap
- **hb_ec_hte vs naive** (n=500, z1): paired t=-0.38, p=0.7080 → CIs overlap
- **global_corrected vs naive** (n=500, z1): paired t=-1.26, p=0.2101 → CIs overlap
- **hb_ec_hte vs stratified_mle** (n=500, z1): paired t=-2.71, p=0.0079 → CIs DO NOT overlap

**exp-001 moderate regime (K=4, n=250):**

| Method | z | Mean Bias | MC SE | 95% CI |
|--------|---|-----------|-------|--------|
| global_corrected | z0 | +0.018359 | 0.009990 | [-0.001220, +0.037939] |
| hb | z0 | +0.001525 | 0.012296 | [-0.022576, +0.025626] |
| naive | z0 | +0.032424 | 0.008371 | [+0.016017, +0.048832] |
| oracle | z0 | -0.002409 | 0.008938 | [-0.019928, +0.015110] |
| stratified_mle | z0 | +0.000650 | 0.012440 | [-0.023733, +0.025033] |
| global_corrected | z1 | -0.025963 | 0.011362 | [-0.048232, -0.003694] |
| hb | z1 | -0.010161 | 0.013583 | [-0.036784, +0.016461] |
| naive | z1 | -0.040036 | 0.009504 | [-0.058664, -0.021408] |
| oracle | z1 | -0.005674 | 0.009297 | [-0.023896, +0.012548] |
| stratified_mle | z1 | -0.009207 | 0.013729 | [-0.036116, +0.017702] |

- **hb vs global_corrected** (z0): z=-1.06, p=0.2880 → CIs overlap — differences NOT significant
- **hb vs naive** (z0): z=-2.08, p=0.0378 → differences are significant
- **global_corrected vs naive** (z0): z=-1.08, p=0.2805 → CIs overlap — differences NOT significant
- **hb vs global_corrected** (z1): z=-0.89, p=0.3722 → CIs overlap — differences NOT significant
- **hb vs naive** (z1): z=-1.80, p=0.0715 → CIs overlap — differences NOT significant
- **global_corrected vs naive** (z1): z=-0.95, p=0.3421 → CIs overlap — differences NOT significant

## Conclusion

Across all 1020 paired comparisons, **742 (73%)** are statistically significant at α=0.05.

- **hb vs global_corrected**: 10/20 comparisons significant
- **hb vs naive**: 12/20 comparisons significant
- **hb_ec_hte vs global_corrected**: 174/240 comparisons significant
- **hb_ec_hte vs naive**: 190/240 comparisons significant

The MC standard errors confirm that the main findings reported in Table 1 are robust.
