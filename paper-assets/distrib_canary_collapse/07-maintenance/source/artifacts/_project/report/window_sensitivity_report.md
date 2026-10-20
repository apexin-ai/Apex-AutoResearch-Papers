# Observation Window Sensitivity Analysis
## Pythia-410M, α=1.0, 4 seeds (42–45)

**Goal**: Test robustness of 5-method consensus to observation window length T.
For each T, we use generations 0 to T−1 (T data points).
6 forward pairs: entropy→{d1,d2,d3}, ECE→{d1,d2,d3}.

## Table 1: Consensus Stability by Window Length

Cell = pairs (of 6) where ≥3/4 seeds show significance.

| T | Robust pairs | Naive xcorr | Diff xcorr | Threshold | Perm Granger | TY |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 5 | **0/6** | 6/6 | 6/6 | 6/6 | 0/6 | 0/6 |
| 6 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |
| 7 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |
| 8 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |
| 9 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |
| 10 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 1/6 |

**TY feasibility note**: Toda-Yamamoto requires VAR(p+d) estimation. With d=1 and optimal p≥1, the augmented model needs p+d+1 parameters per equation × 2 equations. For T≤7, this often leaves insufficient residual df, producing infeasible fits. This is intrinsic to the method, not the data.

- T=5: 0/24 feasible TY tests
- T=6: 0/24 feasible TY tests
- T=7: 0/24 feasible TY tests
- T=8: 0/24 feasible TY tests
- T=9: 24/24 feasible TY tests
- T=10: 24/24 feasible TY tests

## Table 2: Method Sensitivity to T

Smallest T where each method's conclusion matches T=10 and stays stable.

| Method | Stable from T= | Pairs stable ≤T=5 | Pairs stable ≤T=6 | Notes |
|---|:---:|:---:|:---:|---|
| Naive xcorr | 5 | 6/6 | 6/6 | All stable |
| Diff xcorr | 5 | 6/6 | 6/6 | All stable |
| Threshold | 5 | 6/6 | 6/6 | All stable |
| Perm Granger | 6 | 0/6 | 6/6 | All stable |
| Toda-Yamamoto | 5 | 5/6 | 5/6 | Unstable: ECE→d3 |

## Table 3: Per-pair Significance Matrix

Methods with ≥3/4 seed consensus. **Bold** = robust (≥4/5 methods).

| Pair | T=5 | T=6 | T=7 | T=8 | T=9 | T=10 |
|---|---|---|---|---|---|---|
| entropy→d1 | NX,DX,TH | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** |
| entropy→d2 | NX,DX,TH | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** |
| entropy→d3 | NX,DX,TH | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** |
| ECE→d1 | NX,DX,TH | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** |
| ECE→d2 | NX,DX,TH | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** |
| ECE→d3 | NX,DX,TH | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG** | **NX,DX,TH,PG,TY** |

## Table 4: Seed-level Detail

### T=7

| Pair | Seed | Naive | Diff | Threshold | PermG | TY |
|---|:---:|:---:|:---:|---|---|---|
| entropy→d1 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.006) | — (insufficient_df) |
| entropy→d1 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.003) | — (insufficient_df) |
| entropy→d1 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.012) | — (insufficient_df) |
| entropy→d1 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.009) | — (insufficient_df) |
| entropy→d2 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.005) | — (insufficient_df) |
| entropy→d2 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.004) | — (insufficient_df) |
| entropy→d2 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.020) | — (insufficient_df) |
| entropy→d2 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.013) | — (insufficient_df) |
| entropy→d3 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.009) | — (insufficient_df) |
| entropy→d3 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.003) | — (insufficient_df) |
| entropy→d3 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.024) | — (insufficient_df) |
| entropy→d3 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.015) | — (insufficient_df) |
| ECE→d1 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.020) | — (insufficient_df) |
| ECE→d1 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.033) | — (insufficient_df) |
| ECE→d1 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.012) | — (insufficient_df) |
| ECE→d1 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.010) | — (insufficient_df) |
| ECE→d2 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.008) | — (insufficient_df) |
| ECE→d2 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | — (insufficient_df) |
| ECE→d2 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.003) | — (insufficient_df) |
| ECE→d2 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | — (insufficient_df) |
| ECE→d3 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.006) | — (insufficient_df) |
| ECE→d3 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.007) | — (insufficient_df) |
| ECE→d3 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.007) | — (insufficient_df) |
| ECE→d3 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.004) | — (insufficient_df) |

### T=10

| Pair | Seed | Naive | Diff | Threshold | PermG | TY |
|---|:---:|:---:|:---:|---|---|---|
| entropy→d1 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.980) |
| entropy→d1 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.885) |
| entropy→d1 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✗ (p=0.995) |
| entropy→d1 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.002) | ✗ (p=0.983) |
| entropy→d2 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✗ (p=0.836) |
| entropy→d2 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.344) |
| entropy→d2 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✗ (p=0.919) |
| entropy→d2 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.002) | ✗ (p=0.535) |
| entropy→d3 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.763) |
| entropy→d3 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.772) |
| entropy→d3 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.002) | ✗ (p=0.901) |
| entropy→d3 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.003) | ✗ (p=0.663) |
| ECE→d1 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.002) | ✗ (p=0.911) |
| ECE→d1 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.005) | ✗ (p=0.817) |
| ECE→d1 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✗ (p=0.935) |
| ECE→d1 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.002) | ✗ (p=0.915) |
| ECE→d2 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✓ (p=0.017) |
| ECE→d2 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✓ (p=0.000) |
| ECE→d2 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✗ (p=0.402) |
| ECE→d2 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✗ (p=0.152) |
| ECE→d3 | 42 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✓ (p=0.002) |
| ECE→d3 | 43 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.000) | ✓ (p=0.000) |
| ECE→d3 | 44 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✗ (p=0.904) |
| ECE→d3 | 45 | ✓ | ✓ | ✓ (1→2) | ✓ (p=0.001) | ✓ (p=0.001) |

## Conclusions

1. **Consensus stabilizes at T=6**: All 6/6 robust pairs at T=10 are already identified at T=6. The conclusion is invariant to window length for T≥6.

2. **Method sensitivity ranking**:
   - **Most robust**: Naive xcorr, Diff xcorr, Threshold — identical conclusions at all T=5–10.
   - **Moderate**: Perm Granger — requires T≥6 (needs ≥5 differenced points for reliable permutation distribution).
   - **Least robust**: Toda-Yamamoto — infeasible at low T due to VAR df constraints; sporadic significance when feasible.

3. **Rebuttal to 'T=10 too short'**: Four of five methods produce perfectly stable results from T=6. All 6/6 forward pairs are consistently identified. The only method affected by window length is TY, whose instability reflects parametric overhead (VAR with integration-order augmentation), not signal weakness. The fact that 3 independent non-parametric methods (xcorr, differenced xcorr, permutation Granger) plus threshold detection all converge by T=6 provides strong evidence that T=10 is more than sufficient.

4. **TY caveat** (per constraint C001): TY on T≤10 series has df_resid≈6, making it unreliable for trend claims across conditions. Its low power here is expected and does not undermine the consensus from the other 4 methods.
