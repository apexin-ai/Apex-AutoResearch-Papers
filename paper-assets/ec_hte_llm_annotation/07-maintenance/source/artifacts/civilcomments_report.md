# Civil Comments Demographic Subgroup Analysis — EC-HTE Validation

## 1. Dataset & Subgroup Design

**Dataset**: Civil Comments, 3000 annotated comments
**Subgroups** (K=4): keyword-based demographic assignment
**Subgroup labels**: gender, no_identity, race_lgbtq, religion
**Subgroup weights**: gender=0.165, no_identity=0.737, race_lgbtq=0.055, religion=0.043
  - gender: n=496, P(toxic)=0.349
  - no_identity: n=2212, P(toxic)=0.271
  - race_lgbtq: n=164, P(toxic)=0.488
  - religion: n=128, P(toxic)=0.375

## 2. Per-Subgroup Confusion Matrices

| Model | Subgroup | N | FPR | FNR | Accuracy | κ | π |
|-------|----------|---|-----|-----|----------|---|---|
| gpt-4o | gender | 496 | 0.3127 | 0.2254 | 0.7177 | 2.165 | 0.2691 |
| gpt-4o | no_identity | 2212 | 0.2486 | 0.2387 | 0.7541 | 1.951 | 0.2437 |
| gpt-4o | race_lgbtq | 164 | 0.3810 | 0.1500 | 0.7317 | 2.132 | 0.2655 |
| gpt-4o | religion | 128 | 0.2875 | 0.2917 | 0.7109 | 2.376 | 0.2896 |
| gpt-4o-mini | gender | 496 | 0.5418 | 0.0636 | 0.6250 | 2.534 | 0.3027 |
| gpt-4o-mini | no_identity | 2212 | 0.4823 | 0.0718 | 0.6288 | 2.243 | 0.2771 |
| gpt-4o-mini | race_lgbtq | 164 | 0.6310 | 0.0500 | 0.6524 | 3.134 | 0.3405 |
| gpt-4o-mini | religion | 128 | 0.5000 | 0.1458 | 0.6328 | 2.824 | 0.3229 |
| gpt-3.5-turbo | gender | 496 | 0.4985 | 0.1618 | 0.6190 | 2.944 | 0.3302 |
| gpt-3.5-turbo | no_identity | 2212 | 0.3968 | 0.1402 | 0.6727 | 2.160 | 0.2685 |
| gpt-3.5-turbo | race_lgbtq | 164 | 0.5238 | 0.1000 | 0.6829 | 2.658 | 0.3119 |
| gpt-3.5-turbo | religion | 128 | 0.3875 | 0.1875 | 0.6875 | 2.353 | 0.2875 |

## 3. Key Findings: Misclassification Heterogeneity

**gpt-4o**: ΔFPR=0.1324, ΔFNR=0.1417
  κ range: [1.951, 2.376]
**gpt-4o-mini**: ΔFPR=0.1487, ΔFNR=0.0958
  κ range: [2.243, 3.134]
**gpt-3.5-turbo**: ΔFPR=0.1363, ΔFNR=0.0875
  κ range: [2.160, 2.944]

## 4. Semi-Synthetic DGP Results

**DGP**: N=5000, τ(Z=0)=0.1, τ(Z=1)=0.3, MC=50
**Real asymmetric CMs** from LLM annotations on demographic subgroups

| Model | n_expert | Method | |Bias| | RMSE | Sign Reversal Rate |
|-------|----------|--------|-------|------|--------------------|
| gpt-3.5-turbo | 100 | global_corrected | 0.0989 | 0.1791 | 0.000 |
| gpt-3.5-turbo | 100 | hb_ec_hte | 0.2295 | 0.3558 | 0.000 |
| gpt-3.5-turbo | 100 | naive | 0.1026 | 0.1073 | 0.000 |
| gpt-3.5-turbo | 100 | oracle | 0.0403 | 0.0491 | 0.000 |
| gpt-3.5-turbo | 100 | stratified_mle | 0.2638 | 0.5261 | 0.020 |
| gpt-3.5-turbo | 250 | global_corrected | 0.0809 | 0.1063 | 0.000 |
| gpt-3.5-turbo | 250 | hb_ec_hte | 0.2088 | 0.2578 | 0.000 |
| gpt-3.5-turbo | 250 | naive | 0.1026 | 0.1073 | 0.000 |
| gpt-3.5-turbo | 250 | oracle | 0.0403 | 0.0491 | 0.000 |
| gpt-3.5-turbo | 250 | stratified_mle | 0.1757 | 0.2485 | 0.000 |
| gpt-3.5-turbo | 500 | global_corrected | 0.0658 | 0.0902 | 0.000 |
| gpt-3.5-turbo | 500 | hb_ec_hte | 0.1997 | 0.2382 | 0.000 |
| gpt-3.5-turbo | 500 | naive | 0.1026 | 0.1073 | 0.000 |
| gpt-3.5-turbo | 500 | oracle | 0.0403 | 0.0491 | 0.000 |
| gpt-3.5-turbo | 500 | stratified_mle | 0.1057 | 0.1367 | 0.000 |
| gpt-4o | 100 | global_corrected | 0.1211 | 0.1767 | 0.000 |
| gpt-4o | 100 | hb_ec_hte | 0.1285 | 0.1658 | 0.000 |
| gpt-4o | 100 | naive | 0.0792 | 0.0870 | 0.000 |
| gpt-4o | 100 | oracle | 0.0403 | 0.0491 | 0.000 |
| gpt-4o | 100 | stratified_mle | 0.2631 | 0.3897 | 0.000 |
| gpt-4o | 250 | global_corrected | 0.1003 | 0.1318 | 0.000 |
| gpt-4o | 250 | hb_ec_hte | 0.1137 | 0.1438 | 0.000 |
| gpt-4o | 250 | naive | 0.0792 | 0.0870 | 0.000 |
| gpt-4o | 250 | oracle | 0.0403 | 0.0491 | 0.000 |
| gpt-4o | 250 | stratified_mle | 0.1474 | 0.1858 | 0.000 |
| gpt-4o | 500 | global_corrected | 0.0857 | 0.1099 | 0.000 |
| gpt-4o | 500 | hb_ec_hte | 0.1047 | 0.1290 | 0.000 |
| gpt-4o | 500 | naive | 0.0792 | 0.0870 | 0.000 |
| gpt-4o | 500 | oracle | 0.0403 | 0.0491 | 0.000 |
| gpt-4o | 500 | stratified_mle | 0.1042 | 0.1295 | 0.000 |
| gpt-4o-mini | 100 | global_corrected | 0.0963 | 0.1392 | 0.000 |
| gpt-4o-mini | 100 | hb_ec_hte | 0.3076 | 0.4167 | 0.000 |
| gpt-4o-mini | 100 | naive | 0.1057 | 0.1106 | 0.000 |
| gpt-4o-mini | 100 | oracle | 0.0403 | 0.0491 | 0.000 |
| gpt-4o-mini | 100 | stratified_mle | 0.1961 | 0.2957 | 0.020 |
| gpt-4o-mini | 250 | global_corrected | 0.0918 | 0.1150 | 0.000 |
| gpt-4o-mini | 250 | hb_ec_hte | 0.3073 | 0.3703 | 0.000 |
| gpt-4o-mini | 250 | naive | 0.1057 | 0.1106 | 0.000 |
| gpt-4o-mini | 250 | oracle | 0.0403 | 0.0491 | 0.000 |
| gpt-4o-mini | 250 | stratified_mle | 0.1703 | 0.2321 | 0.020 |
| gpt-4o-mini | 500 | global_corrected | 0.0913 | 0.1113 | 0.000 |
| gpt-4o-mini | 500 | hb_ec_hte | 0.3190 | 0.3795 | 0.000 |
| gpt-4o-mini | 500 | naive | 0.1057 | 0.1106 | 0.000 |
| gpt-4o-mini | 500 | oracle | 0.0403 | 0.0491 | 0.000 |
| gpt-4o-mini | 500 | stratified_mle | 0.1138 | 0.1498 | 0.000 |

## 5. Sign Reversal Analysis

- **gpt-4o-mini** / n_expert=100 / stratified_mle: sign reversal rate = 2.0%
- **gpt-4o-mini** / n_expert=250 / stratified_mle: sign reversal rate = 2.0%
- **gpt-3.5-turbo** / n_expert=100 / stratified_mle: sign reversal rate = 2.0%

## 6. Bias Amplification

- **gpt-4o** / n=100: naive→MLE amplification=3.32x, naive→HB=1.62x
- **gpt-4o** / n=250: naive→MLE amplification=1.86x, naive→HB=1.44x
- **gpt-4o** / n=500: naive→MLE amplification=1.32x, naive→HB=1.32x
- **gpt-4o-mini** / n=100: naive→MLE amplification=1.86x, naive→HB=2.91x
- **gpt-4o-mini** / n=250: naive→MLE amplification=1.61x, naive→HB=2.91x
- **gpt-4o-mini** / n=500: naive→MLE amplification=1.08x, naive→HB=3.02x
- **gpt-3.5-turbo** / n=100: naive→MLE amplification=2.57x, naive→HB=2.24x
- **gpt-3.5-turbo** / n=250: naive→MLE amplification=1.71x, naive→HB=2.03x
- **gpt-3.5-turbo** / n=500: naive→MLE amplification=1.03x, naive→HB=1.95x

## 7. Summary

### Key numbers:
- **(a) Sign reversal**: Yes (with τ(Z=1)=0.3)
- **(b) Bias amplification**: 1.03x – 3.32x (stratified MLE vs naive)
- **(c) κ range (gpt-4o)**: [1.951, 2.376]
- **(c) κ range (gpt-4o-mini)**: [2.243, 3.134]
- **(c) κ range (gpt-3.5-turbo)**: [2.160, 2.944]