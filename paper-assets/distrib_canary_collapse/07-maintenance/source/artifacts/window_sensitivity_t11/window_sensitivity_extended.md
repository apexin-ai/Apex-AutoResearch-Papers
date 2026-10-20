# Observation Window Sensitivity Analysis (Extended to T=11)
## Pythia-410M, α=1.0, 4 seeds (42–45)

**Goal**: Extend window sensitivity from T=5–10 to T=5–11 to eliminate off-by-one blind spot.
Previous analysis used T data points (gen_0 to gen_{T−1}). T=11 uses all 11 data points (gen_0 to gen_10).
6 forward pairs: entropy→{d1,d2,d3}, ECE→{d1,d2,d3}.

## Table 1: Consensus Stability by Window Length

Cell = pairs (of 6) where ≥3/4 seeds show significance.

| T | Data points | Robust pairs (≥4/5) | Naive xcorr | Diff xcorr | Threshold | Perm Granger | TY |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 5 | gen_0–gen_4 | **0/6** | 6/6 | 6/6 | 6/6 | 0/6 | 0/6 |
| 6 | gen_0–gen_5 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |
| 7 | gen_0–gen_6 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |
| 8 | gen_0–gen_7 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |
| 9 | gen_0–gen_8 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |
| 10 | gen_0–gen_9 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 1/6 |
| 11 | gen_0–gen_10 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |

**TY feasibility note**: Toda-Yamamoto requires VAR(p+d) estimation with d=1.

- T=5: 0/24 feasible TY tests
- T=6: 0/24 feasible TY tests
- T=7: 0/24 feasible TY tests
- T=8: 0/24 feasible TY tests
- T=9: 24/24 feasible TY tests
- T=10: 24/24 feasible TY tests
- T=11: 1/24 feasible TY tests

## Table 2: Method Sensitivity to T

Smallest T where each method's conclusion matches T=11 and stays stable.

| Method | Stable from T= | Pairs stable ≤T=5 | Pairs stable ≤T=6 | Notes |
|---|:---:|:---:|:---:|---|
| Naive xcorr | 5 | 6/6 | 6/6 | All stable |
| Diff xcorr | 5 | 6/6 | 6/6 | All stable |
| Threshold | 5 | 6/6 | 6/6 | All stable |
| Perm Granger | 6 | 0/6 | 6/6 | All stable |
| Toda-Yamamoto | 5 | 5/6 | 5/6 | Unstable: ECE→d3 |

## Table 3: Per-pair Significance Matrix

Methods with ≥3/4 seed consensus. **Bold** = robust (≥4/5 methods).

| Pair | T=5 | T=6 | T=7 | T=8 | T=9 | T=10 | T=11 |
|---|---|---|---|---|---|---|---|
| entropy→d1 | NX,DX,TH | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** |
| entropy→d2 | NX,DX,TH | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** |
| entropy→d3 | NX,DX,TH | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** |
| ECE→d1 | NX,DX,TH | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** |
| ECE→d2 | NX,DX,TH | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** |
| ECE→d3 | NX,DX,TH | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG,TY** | **NX,DX,TH,PG** |

## Table 4: T=10 vs T=11 Detailed Comparison (TY Focus)

### Per-pair × seed TY p-values

| Pair | Seed | T=10 status | T=10 p | T=10 df_resid | T=11 status | T=11 p | T=11 df_resid | Δp | Conclusion flip? |
|---|:---:|---|---|---|---|---|---|---|---|
| entropy→d1 | 42 | ok | 0.9797 | 3 | insufficient_df | — | 1 | — | no |
| entropy→d1 | 43 | ok | 0.8855 | 3 | insufficient_df | — | 1 | — | no |
| entropy→d1 | 44 | ok | 0.9955 | 3 | insufficient_df | — | 1 | — | no |
| entropy→d1 | 45 | ok | 0.9829 | 3 | ok | 0.9974 | 4 | +0.0146 | no |
| entropy→d2 | 42 | ok | 0.8358 | 3 | insufficient_df | — | 1 | — | no |
| entropy→d2 | 43 | ok | 0.3436 | 3 | insufficient_df | — | 1 | — | no |
| entropy→d2 | 44 | ok | 0.9190 | 3 | insufficient_df | — | 1 | — | no |
| entropy→d2 | 45 | ok | 0.5351 | 3 | insufficient_df | — | 1 | — | no |
| entropy→d3 | 42 | ok | 0.7633 | 3 | insufficient_df | — | 1 | — | no |
| entropy→d3 | 43 | ok | 0.7724 | 3 | insufficient_df | — | 1 | — | no |
| entropy→d3 | 44 | ok | 0.9013 | 3 | insufficient_df | — | 1 | — | no |
| entropy→d3 | 45 | ok | 0.6625 | 3 | insufficient_df | — | 1 | — | no |
| ECE→d1 | 42 | ok | 0.9110 | 3 | insufficient_df | — | 1 | — | no |
| ECE→d1 | 43 | ok | 0.8171 | 3 | insufficient_df | — | 1 | — | no |
| ECE→d1 | 44 | ok | 0.9353 | 3 | insufficient_df | — | 1 | — | no |
| ECE→d1 | 45 | ok | 0.9155 | 3 | insufficient_df | — | 1 | — | no |
| ECE→d2 | 42 | ok | 0.0168 | 3 | insufficient_df | — | 1 | — | YES |
| ECE→d2 | 43 | ok | 0.0003 | 3 | insufficient_df | — | 1 | — | YES |
| ECE→d2 | 44 | ok | 0.4024 | 3 | insufficient_df | — | 1 | — | no |
| ECE→d2 | 45 | ok | 0.1523 | 3 | insufficient_df | — | 1 | — | no |
| ECE→d3 | 42 | ok | 0.0022 | 3 | insufficient_df | — | 1 | — | YES |
| ECE→d3 | 43 | ok | 0.0000 | 3 | insufficient_df | — | 1 | — | YES |
| ECE→d3 | 44 | ok | 0.9040 | 3 | insufficient_df | — | 1 | — | no |
| ECE→d3 | 45 | ok | 0.0006 | 3 | insufficient_df | — | 1 | — | YES |

**Analysis**: At T=10, AIC selects best_p=1 for most pairs, yielding p_aug=2, df_resid=3. At T=11, AIC frequently selects best_p=2 (the extra data point enables more complex models), yielding p_aug=3, but n_eff=11−3=8 with n_params=1+2×3=7, leaving df_resid=1 — below the feasibility threshold. Only 1/24 tests at T=11 retains p=1 selection (seed 45, entropy→d1).

The 5 "flips" are all ECE→d2/d3 pairs where TY was significant at T=10 (p<0.05 with df_resid=3) but becomes infeasible at T=11. These are not genuine reversals of evidence — they reflect TY's parametric fragility at borderline df. The T=10 TY significance on these pairs was itself unreliable (df_resid=3, Wald test on a chi-squared with 1 df from 3 effective observations).

## Table 5a: Seed-level Detail at T=10

| Pair | Seed | Naive | Diff | Threshold | PermG | TY |
|---|:---:|:---:|:---:|---|---|---|
| entropy→d1 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.980) |
| entropy→d1 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.885) |
| entropy→d1 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✗ (p=0.995) |
| entropy→d1 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✗ (p=0.983) |
| entropy→d2 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.836) |
| entropy→d2 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✗ (p=0.344) |
| entropy→d2 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✗ (p=0.919) |
| entropy→d2 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.002) | ✗ (p=0.535) |
| entropy→d3 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.763) |
| entropy→d3 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.772) |
| entropy→d3 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.003) | ✗ (p=0.901) |
| entropy→d3 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.003) | ✗ (p=0.663) |
| ECE→d1 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.004) | ✗ (p=0.911) |
| ECE→d1 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.006) | ✗ (p=0.817) |
| ECE→d1 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.002) | ✗ (p=0.935) |
| ECE→d1 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✗ (p=0.916) |
| ECE→d2 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✓ (p=0.017) |
| ECE→d2 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✓ (p=0.000) |
| ECE→d2 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.402) |
| ECE→d2 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.152) |
| ECE→d3 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✓ (p=0.002) |
| ECE→d3 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✓ (p=0.000) |
| ECE→d3 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.904) |
| ECE→d3 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✓ (p=0.001) |

## Table 5b: Seed-level Detail at T=11

| Pair | Seed | Naive | Diff | Threshold | PermG | TY |
|---|:---:|:---:|:---:|---|---|---|
| entropy→d1 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | — (insufficient_df) |
| entropy→d1 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | — (insufficient_df) |
| entropy→d1 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | — (insufficient_df) |
| entropy→d1 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✗ (p=0.997) |
| entropy→d2 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | — (insufficient_df) |
| entropy→d2 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | — (insufficient_df) |
| entropy→d2 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | — (insufficient_df) |
| entropy→d2 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | — (insufficient_df) |
| entropy→d3 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | — (insufficient_df) |
| entropy→d3 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | — (insufficient_df) |
| entropy→d3 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.002) | — (insufficient_df) |
| entropy→d3 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | — (insufficient_df) |
| ECE→d1 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.003) | — (insufficient_df) |
| ECE→d1 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.003) | — (insufficient_df) |
| ECE→d1 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | — (insufficient_df) |
| ECE→d1 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | — (insufficient_df) |
| ECE→d2 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | — (insufficient_df) |
| ECE→d2 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | — (insufficient_df) |
| ECE→d2 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | — (insufficient_df) |
| ECE→d2 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | — (insufficient_df) |
| ECE→d3 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | — (insufficient_df) |
| ECE→d3 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | — (insufficient_df) |
| ECE→d3 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | — (insufficient_df) |
| ECE→d3 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | — (insufficient_df) |

## Table 6: T=10 vs T=11 Method-level Consensus Count

| Method | T=10 sig pairs (≥3/4 seeds) | T=11 sig pairs (≥3/4 seeds) | Change |
|---|:---:|:---:|:---:|
| Naive xcorr | 6/6 | 6/6 | = |
| Diff xcorr | 6/6 | 6/6 | = |
| Threshold | 6/6 | 6/6 | = |
| Perm Granger | 6/6 | 6/6 | = |
| Toda-Yamamoto | 1/6 | 0/6 | -1 |

**4/5 consensus robust pairs: T=10=6/6, T=11=6/6**

## Conclusions

1. **Consensus stabilizes at T=6**: All 6/6 robust pairs at T=11 are already identified at T=6. The 11th data point (gen_10) does not change the 4/5 consensus conclusion.

2. **T=10→T=11 is a non-event for non-TY methods**: Naive xcorr, Diff xcorr, Threshold, and Perm Granger all produce identical results at T=10 and T=11. The extra data point adds no new information for these methods.

3. **TY at T=10 vs T=11**: 5 of 24 seed×pair combinations show a significance flip between T=10 and T=11. This confirms TY's instability at low df — adding one data point can change TY conclusions, reinforcing the C001 constraint against citing single-seed TY trends.

4. **Corrections to prior report**: The previous window sensitivity report covered T=5–10 (5 to 10 data points). With the extension to T=11 (all 11 data points, gen_0–gen_10):
   - **No numbers need correction**: The 4/5 consensus robust pair count is identical at T=10 and T=11.
   - The prior report's claim 'consensus stabilizes by T=6' remains valid through T=11.
   - TY feasibility and significance counts may differ at T=11 vs T=10 — see Table 4 for details.

5. **TY caveat** (per constraint C001): TY on T≤11 series still has very low df_resid. Its sporadic significance should not be cited for cross-α trend claims without multi-seed confirmation.

6. **Off-by-one verdict**: The previous T=10 analysis used gen_0–gen_9 (10 data points), missing gen_10. Including gen_10 (T=11, 11 data points) changes nothing for the consensus framework. The TY feasibility paradoxically *decreases* at T=11 because AIC exploits the extra data point to select higher lag orders, consuming the marginal df gain. This is an artifact of model selection, not evidence instability.
