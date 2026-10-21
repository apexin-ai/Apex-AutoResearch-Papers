# exp-023: Civil Comments Semi-Synthetic Validation (v3)

## Design

- Dataset: Civil Comments (toxicity detection), K=2 subgroups (text_length)
- DGP: N=10000, P(Z=1)=0.30, tau(z=0)=0.0, tau(z=1)=0.5, MC=50
- Symmetric misclassification: P(Z_hat != Z | S) = pi_S (matching TweetEval)
- Methods: Oracle, Naive, Global-corrected, Stratified MLE, HB EC-HTE


## Regime: extreme

  - S0: pi=0.05
  - S1: pi=0.30


### n_expert = 100

**Z=0** (true tau=0.0):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0081 | 0.0271 | 0.0347 | 0.930 |
| naive | +0.0358 | 0.0496 | 0.0570 | 0.730 |
| global_corrected | -0.0152 | 0.0637 | 0.0765 | 0.750 |
| stratified_mle | -0.0332 | 0.0632 | 0.0913 | 0.860 |
| hb_ec_hte | -0.0302 | 0.0624 | 0.0890 | 0.840 |

**Z=1** (true tau=0.5):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0001 | 0.0441 | 0.0544 | 0.930 |
| naive | -0.1552 | 0.1590 | 0.1682 | 0.380 |
| global_corrected | +0.0426 | 0.1922 | 0.2229 | 0.410 |
| stratified_mle | +0.0773 | 0.1691 | 0.2474 | 0.740 |
| hb_ec_hte | +0.0698 | 0.1657 | 0.2388 | 0.740 |

**Per-subgroup detail:**

| Subgroup | Z | Naive Bias | Global Bias | EC-HTE Bias | Naive RMSE | Global RMSE | EC-HTE RMSE |
|----------|---|------------|-------------|-------------|------------|-------------|-------------|
| S0 | 0 | +0.0030 | -0.0707 | -0.0193 | 0.0345 | 0.0903 | 0.0471 |
| S0 | 1 | -0.0557 | +0.2279 | +0.0695 | 0.0778 | 0.2759 | 0.1791 |
| S1 | 0 | +0.0685 | +0.0404 | -0.0411 | 0.0795 | 0.0627 | 0.1310 |
| S1 | 1 | -0.2546 | -0.1426 | +0.0701 | 0.2585 | 0.1700 | 0.2986 |


### n_expert = 250

**Z=0** (true tau=0.0):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0081 | 0.0271 | 0.0347 | 0.930 |
| naive | +0.0358 | 0.0496 | 0.0570 | 0.730 |
| global_corrected | -0.0104 | 0.0609 | 0.0720 | 0.750 |
| stratified_mle | -0.0170 | 0.0482 | 0.0646 | 0.870 |
| hb_ec_hte | -0.0162 | 0.0480 | 0.0644 | 0.870 |

**Z=1** (true tau=0.5):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0001 | 0.0441 | 0.0544 | 0.930 |
| naive | -0.1552 | 0.1590 | 0.1682 | 0.380 |
| global_corrected | +0.0309 | 0.1809 | 0.2080 | 0.420 |
| stratified_mle | +0.0303 | 0.1143 | 0.1517 | 0.800 |
| hb_ec_hte | +0.0282 | 0.1132 | 0.1510 | 0.800 |

**Per-subgroup detail:**

| Subgroup | Z | Naive Bias | Global Bias | EC-HTE Bias | Naive RMSE | Global RMSE | EC-HTE RMSE |
|----------|---|------------|-------------|-------------|------------|-------------|-------------|
| S0 | 0 | +0.0030 | -0.0633 | -0.0135 | 0.0345 | 0.0807 | 0.0412 |
| S0 | 1 | -0.0557 | +0.2116 | +0.0323 | 0.0778 | 0.2504 | 0.1216 |
| S1 | 0 | +0.0685 | +0.0426 | -0.0189 | 0.0795 | 0.0633 | 0.0875 |
| S1 | 1 | -0.2546 | -0.1498 | +0.0241 | 0.2585 | 0.1656 | 0.1803 |


### n_expert = 500

**Z=0** (true tau=0.0):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0081 | 0.0271 | 0.0347 | 0.930 |
| naive | +0.0358 | 0.0496 | 0.0570 | 0.730 |
| global_corrected | -0.0109 | 0.0598 | 0.0701 | 0.760 |
| stratified_mle | -0.0161 | 0.0459 | 0.0596 | 0.880 |
| hb_ec_hte | -0.0158 | 0.0458 | 0.0594 | 0.880 |

**Z=1** (true tau=0.5):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0001 | 0.0441 | 0.0544 | 0.930 |
| naive | -0.1552 | 0.1590 | 0.1682 | 0.380 |
| global_corrected | +0.0271 | 0.1773 | 0.1999 | 0.400 |
| stratified_mle | +0.0209 | 0.0970 | 0.1267 | 0.850 |
| hb_ec_hte | +0.0201 | 0.0968 | 0.1262 | 0.850 |

**Per-subgroup detail:**

| Subgroup | Z | Naive Bias | Global Bias | EC-HTE Bias | Naive RMSE | Global RMSE | EC-HTE RMSE |
|----------|---|------------|-------------|-------------|------------|-------------|-------------|
| S0 | 0 | +0.0030 | -0.0636 | -0.0118 | 0.0345 | 0.0777 | 0.0391 |
| S0 | 1 | -0.0557 | +0.2038 | +0.0162 | 0.0778 | 0.2320 | 0.0838 |
| S1 | 0 | +0.0685 | +0.0418 | -0.0197 | 0.0795 | 0.0625 | 0.0797 |
| S1 | 1 | -0.2546 | -0.1496 | +0.0240 | 0.2585 | 0.1678 | 0.1687 |


### n_expert = 1000

**Z=0** (true tau=0.0):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0081 | 0.0271 | 0.0347 | 0.930 |
| naive | +0.0358 | 0.0496 | 0.0570 | 0.730 |
| global_corrected | -0.0091 | 0.0585 | 0.0692 | 0.760 |
| stratified_mle | -0.0127 | 0.0417 | 0.0535 | 0.890 |
| hb_ec_hte | -0.0126 | 0.0417 | 0.0535 | 0.890 |

**Z=1** (true tau=0.5):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0001 | 0.0441 | 0.0544 | 0.930 |
| naive | -0.1552 | 0.1590 | 0.1682 | 0.380 |
| global_corrected | +0.0219 | 0.1747 | 0.1961 | 0.380 |
| stratified_mle | +0.0107 | 0.0869 | 0.1087 | 0.880 |
| hb_ec_hte | +0.0103 | 0.0868 | 0.1086 | 0.870 |

**Per-subgroup detail:**

| Subgroup | Z | Naive Bias | Global Bias | EC-HTE Bias | Naive RMSE | Global RMSE | EC-HTE RMSE |
|----------|---|------------|-------------|-------------|------------|-------------|-------------|
| S0 | 0 | +0.0030 | -0.0612 | -0.0096 | 0.0345 | 0.0753 | 0.0374 |
| S0 | 1 | -0.0557 | +0.1965 | +0.0033 | 0.0778 | 0.2224 | 0.0728 |
| S1 | 0 | +0.0685 | +0.0429 | -0.0155 | 0.0795 | 0.0631 | 0.0695 |
| S1 | 1 | -0.2546 | -0.1528 | +0.0173 | 0.2585 | 0.1698 | 0.1444 |


## Regime: moderate

  - S0: pi=0.08
  - S1: pi=0.20


### n_expert = 100

**Z=0** (true tau=0.0):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0081 | 0.0271 | 0.0347 | 0.930 |
| naive | +0.0257 | 0.0383 | 0.0458 | 0.860 |
| global_corrected | -0.0151 | 0.0428 | 0.0529 | 0.850 |
| stratified_mle | -0.0256 | 0.0458 | 0.0582 | 0.870 |
| hb_ec_hte | -0.0233 | 0.0456 | 0.0578 | 0.870 |

**Z=1** (true tau=0.5):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0001 | 0.0441 | 0.0544 | 0.930 |
| naive | -0.1390 | 0.1407 | 0.1503 | 0.300 |
| global_corrected | +0.0259 | 0.1110 | 0.1391 | 0.670 |
| stratified_mle | +0.0625 | 0.1294 | 0.1990 | 0.690 |
| hb_ec_hte | +0.0565 | 0.1263 | 0.1957 | 0.710 |

**Per-subgroup detail:**

| Subgroup | Z | Naive Bias | Global Bias | EC-HTE Bias | Naive RMSE | Global RMSE | EC-HTE RMSE |
|----------|---|------------|-------------|-------------|------------|-------------|-------------|
| S0 | 0 | +0.0108 | -0.0385 | -0.0204 | 0.0374 | 0.0641 | 0.0559 |
| S0 | 1 | -0.0867 | +0.1110 | +0.0800 | 0.1045 | 0.1725 | 0.2515 |
| S1 | 0 | +0.0406 | +0.0082 | -0.0262 | 0.0541 | 0.0418 | 0.0598 |
| S1 | 1 | -0.1913 | -0.0593 | +0.0331 | 0.1961 | 0.1057 | 0.1399 |


### n_expert = 250

**Z=0** (true tau=0.0):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0081 | 0.0271 | 0.0347 | 0.930 |
| naive | +0.0257 | 0.0383 | 0.0458 | 0.860 |
| global_corrected | -0.0103 | 0.0408 | 0.0507 | 0.880 |
| stratified_mle | -0.0141 | 0.0400 | 0.0492 | 0.920 |
| hb_ec_hte | -0.0134 | 0.0401 | 0.0493 | 0.910 |

**Z=1** (true tau=0.5):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0001 | 0.0441 | 0.0544 | 0.930 |
| naive | -0.1390 | 0.1407 | 0.1503 | 0.300 |
| global_corrected | +0.0137 | 0.0992 | 0.1250 | 0.770 |
| stratified_mle | +0.0230 | 0.0957 | 0.1214 | 0.820 |
| hb_ec_hte | +0.0211 | 0.0952 | 0.1209 | 0.810 |

**Per-subgroup detail:**

| Subgroup | Z | Naive Bias | Global Bias | EC-HTE Bias | Naive RMSE | Global RMSE | EC-HTE RMSE |
|----------|---|------------|-------------|-------------|------------|-------------|-------------|
| S0 | 0 | +0.0108 | -0.0328 | -0.0139 | 0.0374 | 0.0591 | 0.0457 |
| S0 | 1 | -0.0867 | +0.0978 | +0.0341 | 0.1045 | 0.1537 | 0.1319 |
| S1 | 0 | +0.0406 | +0.0123 | -0.0129 | 0.0541 | 0.0423 | 0.0529 |
| S1 | 1 | -0.1913 | -0.0705 | +0.0081 | 0.1961 | 0.0964 | 0.1098 |


### n_expert = 500

**Z=0** (true tau=0.0):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0081 | 0.0271 | 0.0347 | 0.930 |
| naive | +0.0257 | 0.0383 | 0.0458 | 0.860 |
| global_corrected | -0.0091 | 0.0382 | 0.0472 | 0.890 |
| stratified_mle | -0.0108 | 0.0349 | 0.0428 | 0.930 |
| hb_ec_hte | -0.0106 | 0.0349 | 0.0428 | 0.930 |

**Z=1** (true tau=0.5):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0001 | 0.0441 | 0.0544 | 0.930 |
| naive | -0.1390 | 0.1407 | 0.1503 | 0.300 |
| global_corrected | +0.0059 | 0.0925 | 0.1138 | 0.800 |
| stratified_mle | +0.0079 | 0.0753 | 0.0920 | 0.890 |
| hb_ec_hte | +0.0073 | 0.0752 | 0.0918 | 0.890 |

**Per-subgroup detail:**

| Subgroup | Z | Naive Bias | Global Bias | EC-HTE Bias | Naive RMSE | Global RMSE | EC-HTE RMSE |
|----------|---|------------|-------------|-------------|------------|-------------|-------------|
| S0 | 0 | +0.0108 | -0.0312 | -0.0115 | 0.0374 | 0.0538 | 0.0416 |
| S0 | 1 | -0.0867 | +0.0871 | +0.0163 | 0.1045 | 0.1288 | 0.0916 |
| S1 | 0 | +0.0406 | +0.0130 | -0.0096 | 0.0541 | 0.0406 | 0.0440 |
| S1 | 1 | -0.1913 | -0.0752 | -0.0017 | 0.1961 | 0.0988 | 0.0921 |


### n_expert = 1000

**Z=0** (true tau=0.0):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0081 | 0.0271 | 0.0347 | 0.930 |
| naive | +0.0257 | 0.0383 | 0.0458 | 0.860 |
| global_corrected | -0.0079 | 0.0381 | 0.0469 | 0.880 |
| stratified_mle | -0.0087 | 0.0339 | 0.0416 | 0.930 |
| hb_ec_hte | -0.0086 | 0.0339 | 0.0416 | 0.940 |

**Z=1** (true tau=0.5):

| Method | Mean Bias | |Bias| | RMSE | Coverage |
|--------|-----------|-------|------|----------|
| oracle | -0.0001 | 0.0441 | 0.0544 | 0.930 |
| naive | -0.1390 | 0.1407 | 0.1503 | 0.300 |
| global_corrected | +0.0020 | 0.0928 | 0.1125 | 0.780 |
| stratified_mle | +0.0003 | 0.0672 | 0.0813 | 0.910 |
| hb_ec_hte | -0.0000 | 0.0671 | 0.0812 | 0.910 |

**Per-subgroup detail:**

| Subgroup | Z | Naive Bias | Global Bias | EC-HTE Bias | Naive RMSE | Global RMSE | EC-HTE RMSE |
|----------|---|------------|-------------|-------------|------------|-------------|-------------|
| S0 | 0 | +0.0108 | -0.0297 | -0.0094 | 0.0374 | 0.0524 | 0.0405 |
| S0 | 1 | -0.0867 | +0.0827 | +0.0035 | 0.1045 | 0.1251 | 0.0828 |
| S1 | 0 | +0.0406 | +0.0139 | -0.0078 | 0.0541 | 0.0413 | 0.0427 |
| S1 | 1 | -0.1913 | -0.0787 | -0.0036 | 0.1961 | 0.0998 | 0.0796 |


## Summary


### extreme

**n_expert=100:**
- oracle: Bias=-0.0041, |Bias|=0.0356, RMSE=0.0445, Cov=0.930
- naive: Bias=-0.0597, |Bias|=0.1043, RMSE=0.1126, Cov=0.555
- global_corrected: Bias=+0.0137, |Bias|=0.1280, RMSE=0.1497, Cov=0.580
- stratified_mle: Bias=+0.0221, |Bias|=0.1162, RMSE=0.1694, Cov=0.800
- hb_ec_hte: Bias=+0.0198, |Bias|=0.1140, RMSE=0.1639, Cov=0.790

**n_expert=250:**
- oracle: Bias=-0.0041, |Bias|=0.0356, RMSE=0.0445, Cov=0.930
- naive: Bias=-0.0597, |Bias|=0.1043, RMSE=0.1126, Cov=0.555
- global_corrected: Bias=+0.0103, |Bias|=0.1209, RMSE=0.1400, Cov=0.585
- stratified_mle: Bias=+0.0066, |Bias|=0.0813, RMSE=0.1082, Cov=0.835
- hb_ec_hte: Bias=+0.0060, |Bias|=0.0806, RMSE=0.1077, Cov=0.835

**n_expert=500:**
- oracle: Bias=-0.0041, |Bias|=0.0356, RMSE=0.0445, Cov=0.930
- naive: Bias=-0.0597, |Bias|=0.1043, RMSE=0.1126, Cov=0.555
- global_corrected: Bias=+0.0081, |Bias|=0.1186, RMSE=0.1350, Cov=0.580
- stratified_mle: Bias=+0.0024, |Bias|=0.0715, RMSE=0.0931, Cov=0.865
- hb_ec_hte: Bias=+0.0022, |Bias|=0.0713, RMSE=0.0928, Cov=0.865

**n_expert=1000:**
- oracle: Bias=-0.0041, |Bias|=0.0356, RMSE=0.0445, Cov=0.930
- naive: Bias=-0.0597, |Bias|=0.1043, RMSE=0.1126, Cov=0.555
- global_corrected: Bias=+0.0064, |Bias|=0.1166, RMSE=0.1327, Cov=0.570
- stratified_mle: Bias=-0.0010, |Bias|=0.0643, RMSE=0.0811, Cov=0.885
- hb_ec_hte: Bias=-0.0011, |Bias|=0.0642, RMSE=0.0810, Cov=0.880


### moderate

**n_expert=100:**
- oracle: Bias=-0.0041, |Bias|=0.0356, RMSE=0.0445, Cov=0.930
- naive: Bias=-0.0566, |Bias|=0.0895, RMSE=0.0980, Cov=0.580
- global_corrected: Bias=+0.0054, |Bias|=0.0769, RMSE=0.0960, Cov=0.760
- stratified_mle: Bias=+0.0184, |Bias|=0.0876, RMSE=0.1286, Cov=0.780
- hb_ec_hte: Bias=+0.0166, |Bias|=0.0860, RMSE=0.1268, Cov=0.790

**n_expert=250:**
- oracle: Bias=-0.0041, |Bias|=0.0356, RMSE=0.0445, Cov=0.930
- naive: Bias=-0.0566, |Bias|=0.0895, RMSE=0.0980, Cov=0.580
- global_corrected: Bias=+0.0017, |Bias|=0.0700, RMSE=0.0879, Cov=0.825
- stratified_mle: Bias=+0.0044, |Bias|=0.0679, RMSE=0.0853, Cov=0.870
- hb_ec_hte: Bias=+0.0039, |Bias|=0.0676, RMSE=0.0851, Cov=0.860

**n_expert=500:**
- oracle: Bias=-0.0041, |Bias|=0.0356, RMSE=0.0445, Cov=0.930
- naive: Bias=-0.0566, |Bias|=0.0895, RMSE=0.0980, Cov=0.580
- global_corrected: Bias=-0.0016, |Bias|=0.0654, RMSE=0.0805, Cov=0.845
- stratified_mle: Bias=-0.0015, |Bias|=0.0551, RMSE=0.0674, Cov=0.910
- hb_ec_hte: Bias=-0.0016, |Bias|=0.0551, RMSE=0.0673, Cov=0.910

**n_expert=1000:**
- oracle: Bias=-0.0041, |Bias|=0.0356, RMSE=0.0445, Cov=0.930
- naive: Bias=-0.0566, |Bias|=0.0895, RMSE=0.0980, Cov=0.580
- global_corrected: Bias=-0.0030, |Bias|=0.0654, RMSE=0.0797, Cov=0.830
- stratified_mle: Bias=-0.0042, |Bias|=0.0505, RMSE=0.0614, Cov=0.920
- hb_ec_hte: Bias=-0.0043, |Bias|=0.0505, RMSE=0.0614, Cov=0.925
