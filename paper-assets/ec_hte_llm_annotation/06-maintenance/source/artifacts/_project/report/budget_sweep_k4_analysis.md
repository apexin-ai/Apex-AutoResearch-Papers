# Budget Sensitivity Sweep: Llama K=4 Real CM

## Design

- N=5000, P(Z=1)=0.652, K=4 subgroups
- tau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3
- n_expert sweep: [100, 200, 500, 1000, 2000]
- 50 MC seeds per budget
- HB method: MAP-EB (Gamma(3,1) prior)
- |Bias| = avg across cells of |mean(bias) across seeds|

## Summary Table

| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_echte | HB_wins_bias? | HB_wins_rmse? |
|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|---------------|---------------|
| 100 | 0.0803 | 0.0214 | 0.0520 | 0.0578 | 0.1219 | 0.1895 | 0.3937 | 0.4020 | 0.710 | YES | no |
| 200 | 0.0803 | 0.0208 | 0.0251 | 0.0294 | 0.1219 | 0.1747 | 0.2603 | 0.2639 | 0.800 | YES | no |
| 500 | 0.0803 | 0.0167 | 0.0153 | 0.0165 | 0.1219 | 0.1544 | 0.1774 | 0.1783 | 0.892 | YES | no |
| 1000 | 0.0803 | 0.0168 | 0.0162 | 0.0166 | 0.1219 | 0.1524 | 0.1603 | 0.1608 | 0.915 | YES | no |
| 2000 | 0.0803 | 0.0167 | 0.0213 | 0.0212 | 0.1219 | 0.1491 | 0.1492 | 0.1494 | 0.940 | YES | no |

## Crossover Analysis

- **|Bias| crossover**: EC-HTE beats Naive at n_expert=100
- **RMSE crossover**: EC-HTE never beats Naive in tested range

## Bias-Variance Decomposition (per budget)

| n_expert | Method | Bias^2 | Variance | MSE |
|----------|--------|--------|----------|-----|
| 100 | naive | 0.0079 | 0.0081 | 0.0160 |
| 100 | hb_ec_hte | 0.0043 | 0.1755 | 0.1798 |
| 200 | naive | 0.0079 | 0.0081 | 0.0160 |
| 200 | hb_ec_hte | 0.0011 | 0.0746 | 0.0757 |
| 500 | naive | 0.0079 | 0.0081 | 0.0160 |
| 500 | hb_ec_hte | 0.0003 | 0.0342 | 0.0345 |
| 1000 | naive | 0.0079 | 0.0081 | 0.0160 |
| 1000 | hb_ec_hte | 0.0005 | 0.0278 | 0.0283 |
| 2000 | naive | 0.0079 | 0.0081 | 0.0160 |
| 2000 | hb_ec_hte | 0.0007 | 0.0238 | 0.0245 |
