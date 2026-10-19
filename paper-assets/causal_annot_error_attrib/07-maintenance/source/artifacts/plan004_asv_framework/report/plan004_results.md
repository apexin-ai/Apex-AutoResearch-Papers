# plan004_asv_framework Results (96.3s total)

## Part 1: delta_range fix
- delta_range(diag=0.8) = [0, 5.0], delta_range(diag=0.9) = [0, 10.0] (capped)
- C(delta) column-stochastic for all delta in [0, delta_max]
- C(delta=2.0) diagonal = [0.6, 0.6, 0.6] (correct extrapolation)

## Part 2: ASV Table (3 topologies x 6 C structures)
| C_structure | Conf(V) | Med(V) | Coll(P) | d_max |
|---|---|---|---|---|
| sym_mild | None | None | 2.252 | 5.0 |
| sym_severe | None | None | 1.126 | 2.5 |
| asym_01 | None | None | 1.044 | 3.3 |
| one_weak | None | None | None* | 1.7 |
| near_perfect | None | None | 9.009 | 10.0 |
| heavy_offdiag | None | None | 0.817 | 2.0 |

Confounding/mediation ASV=None: beta_T=1.0/tau=0.5 positive; confounding bias is same-sign (never flips).
Collider protection ASV: higher accuracy C0 -> larger ASV (more robust to collider bias).

## Part 3: Monotonicity
- confounding: 753/1000 violations (|bias| NOT monotonically increasing)
- mediation: 742/1000 violations
- collider: 759/1000 violations (|bias| NOT monotonically decreasing)
- Worst violations ~1e-2 magnitude. Monotonicity is NOT a general property of linear interpolation.

## Part 4: Sharpness
Collider protection ASV verified tight: tau(ASV-eps) and tau(ASV+eps) straddle the 0.99 threshold.
Confounding/mediation: no finite ASV to verify.

## Part 5: MC Coverage (500 scenarios x 100 reps x N=5000)
- Confounding: 500/500 = 100.0% plim accuracy, 100.0% bias bounded
- Mediation: 500/500 = 100.0% plim accuracy, 100.0% bias bounded
- Collider: 500/500 = 100.0% plim accuracy, 100.0% bias bounded

## Part 6: Type I/II Error Rate (2000 MC x N=1000)

### Confounding
| C | H0 naive | H0 ASV | H1 naive | H1 ASV |
|---|---|---|---|---|
| sym_mild | 0.964 | 0.000 | 1.000 | 1.000 |
| sym_severe | 1.000 | 0.000 | 1.000 | 1.000 |
| asym_01 | 0.989 | 0.000 | 1.000 | 1.000 |

### Mediation
| C | H0 naive | H0 ASV | H1 naive | H1 ASV |
|---|---|---|---|---|
| sym_mild | 0.697 | 0.000 | 1.000 | 1.000 |
| sym_severe | 0.954 | 0.000 | 1.000 | 1.000 |
| asym_01 | 0.707 | 0.000 | 1.000 | 1.000 |

### Collider
| C | H0 naive | H0 ASV | H1 naive | H1 ASV |
|---|---|---|---|---|
| sym_mild | 0.074 | 0.000 | 1.000 | 1.000 |
| sym_severe | 0.052 | 0.000 | 1.000 | 1.000 |
| asym_01 | 0.047 | 0.000 | 1.000 | 1.000 |

ASV-informed test: Type I = 0.000, Power = 1.000 across all configurations.
Mechanism: H0 -> plim(I)[tau]=0 -> ASV=0 (fragile); H1 -> tau stays significant -> ASV=None (robust).
