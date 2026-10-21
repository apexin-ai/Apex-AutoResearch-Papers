# K=2 Budget Sensitivity Sweep: Llama-3.1-8B Real CMs

## Design

Merged subgroups by `has_hashtag` (K=2).

| Subgroup | Weight | FPR | FNR | π_s |
|----------|--------|-----|-----|-----|
| False | 0.604 | 0.252 | 0.269 | 0.261 |
| True | 0.396 | 0.186 | 0.233 | 0.210 |

Δπ = |π_False - π_True| = |0.261 - 0.210| = 0.051

N=5000, P(Z=1)=0.652, τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
n_expert ∈ [100, 200, 500, 1000, 2000], 50 MC seeds per budget

## Summary by n_expert

| n_expert | Method | |Bias| | RMSE | Coverage |
|----------|--------|-------|------|----------|
| 100 | naive | 0.0819 | 0.1000 | 0.675 |
| 100 | global_corrected | 0.0094 | 0.1456 | 0.840 |
| 100 | stratified_mle | 0.0128 | 0.1905 | 0.745 |
| 100 | hb_ec_hte | 0.0116 | 0.1927 | 0.745 |
|---|---|---|---|---|
| 200 | naive | 0.0819 | 0.1000 | 0.675 |
| 200 | global_corrected | 0.0161 | 0.1223 | 0.860 |
| 200 | stratified_mle | 0.0179 | 0.1540 | 0.775 |
| 200 | hb_ec_hte | 0.0168 | 0.1557 | 0.780 |
|---|---|---|---|---|
| 500 | naive | 0.0819 | 0.1000 | 0.675 |
| 500 | global_corrected | 0.0132 | 0.1070 | 0.925 |
| 500 | stratified_mle | 0.0128 | 0.1239 | 0.900 |
| 500 | hb_ec_hte | 0.0125 | 0.1242 | 0.905 |
|---|---|---|---|---|
| 1000 | naive | 0.0819 | 0.1000 | 0.675 |
| 1000 | global_corrected | 0.0073 | 0.0952 | 0.960 |
| 1000 | stratified_mle | 0.0065 | 0.0999 | 0.940 |
| 1000 | hb_ec_hte | 0.0065 | 0.0997 | 0.940 |
|---|---|---|---|---|
| 2000 | naive | 0.0819 | 0.1000 | 0.675 |
| 2000 | global_corrected | 0.0069 | 0.0908 | 0.955 |
| 2000 | stratified_mle | 0.0137 | 0.0921 | 0.950 |
| 2000 | hb_ec_hte | 0.0137 | 0.0920 | 0.950 |
|---|---|---|---|---|

## RMSE Ratio: EC-HTE / Naive

| n_expert | Naive RMSE | HB RMSE | Ratio | HB wins? |
|----------|-----------|---------|-------|----------|
| 100 | 0.1000 | 0.1927 | 1.928 | no |
| 200 | 0.1000 | 0.1557 | 1.557 | no |
| 500 | 0.1000 | 0.1242 | 1.243 | no |
| 1000 | 0.1000 | 0.0997 | 0.998 | YES |
| 2000 | 0.1000 | 0.0920 | 0.921 | YES |

## |Bias| Ratio: EC-HTE / Naive

| n_expert | Naive |Bias| | HB |Bias| | Ratio | HB wins? |
|----------|-----------|---------|-------|----------|
| 100 | 0.0819 | 0.0116 | 0.141 | YES |
| 200 | 0.0819 | 0.0168 | 0.206 | YES |
| 500 | 0.0819 | 0.0125 | 0.152 | YES |
| 1000 | 0.0819 | 0.0065 | 0.080 | YES |
| 2000 | 0.0819 | 0.0137 | 0.167 | YES |

## Bias-Variance Decomposition

| n_expert | Method | Bias² | Var | MSE |
|----------|--------|-------|-----|-----|
| 100 | naive | 0.0082 | 0.0029 | 0.0111 |
| 100 | global_corrected | 0.0001 | 0.0227 | 0.0228 |
| 100 | hb_ec_hte | 0.0002 | 0.0410 | 0.0412 |
|---|---|---|---|---|
| 200 | naive | 0.0082 | 0.0029 | 0.0111 |
| 200 | global_corrected | 0.0004 | 0.0158 | 0.0161 |
| 200 | hb_ec_hte | 0.0003 | 0.0261 | 0.0264 |
|---|---|---|---|---|
| 500 | naive | 0.0082 | 0.0029 | 0.0111 |
| 500 | global_corrected | 0.0002 | 0.0121 | 0.0123 |
| 500 | hb_ec_hte | 0.0003 | 0.0165 | 0.0168 |
|---|---|---|---|---|
| 1000 | naive | 0.0082 | 0.0029 | 0.0111 |
| 1000 | global_corrected | 0.0001 | 0.0096 | 0.0097 |
| 1000 | hb_ec_hte | 0.0001 | 0.0105 | 0.0106 |
|---|---|---|---|---|
| 2000 | naive | 0.0082 | 0.0029 | 0.0111 |
| 2000 | global_corrected | 0.0001 | 0.0088 | 0.0088 |
| 2000 | hb_ec_hte | 0.0003 | 0.0087 | 0.0090 |
|---|---|---|---|---|

## Crossover Analysis

**RMSE crossover**: EC-HTE first beats Naive at n_expert=1000
**|Bias| crossover**: EC-HTE first beats Naive at n_expert=100

## Conclusion

With K=2 and Δπ=0.051, the CM heterogeneity is small.
The bias reduction from stratified correction is limited, so the variance cost of estimating per-subgroup CMs must be overcome by larger n_expert.

At n_expert≥1000, HB EC-HTE achieves lower RMSE than Naive, indicating the variance cost is amortized.