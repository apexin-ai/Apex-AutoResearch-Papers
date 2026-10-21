## 2×2 ANOVA + Main Effects Analysis (v2 only)
## Generated: 2026-05-27 22:28 UTC

### A. Normalization Main Effect (BN vs LN)
| | BN pooled (n=7) | LN pooled (n=4) |
|---|---|---|
| mean ± sd | 0.7489 ± 0.0461 | 0.7890 ± 0.0359 |

- Mean diff (LN - BN) = +0.0401, LN > BN
- Cohen's d = 0.9344 (Reviewer estimated ~1.03)
- Hedges' g = 0.8543
- 95% Bootstrap CI (LN-BN) = [-0.0026, 0.0849]
- Permutation p = 0.1723

### B. Gradient Flow Main Effect (ON vs OFF)
| | Grad ON (n=6) | Grad OFF (n=5) |
|---|---|---|
| mean ± sd | 0.7510 ± 0.0530 | 0.7784 ± 0.0339 |

- Mean diff (ON - OFF) = -0.0274, OFF > ON
- Cohen's d = -0.6017
- Hedges' g = -0.5501
- 95% Bootstrap CI = [-0.0771, 0.0160]
- Permutation p = 0.3876

### C. 2×2 ANOVA (Type III SS)
| Source | SS | df | MS | F | p | partial η² |
|---|---|---|---|---|---|---|
| Gradient Flow | 0.002905 | 1 | 0.002905 | 1.7118 | 0.2321 | 0.1965 |
| Norm Type | 0.002832 | 1 | 0.002832 | 1.6688 | 0.2374 | 0.1925 |
| Interaction | 0.000035 | 1 | 0.000035 | 0.0205 | 0.8902 | 0.0029 |
| Residual | 0.011880 | 7 | 0.001697 | | | |

### D. Pairwise Comparisons
| Comparison | Δmean | Cohen's d | perm p | Note |
|---|---|---|---|---|
| Cell1 vs Cell2 | -0.0513 | -1.0207 | 0.2950 | |
| Cell1 vs Cell3 | -0.0412 | -0.9277 | 0.2729 | |
| Cell1 vs Cell4 | -0.1007 | -1.5835 | 0.4997 | n=1 ref |
| Cell2 vs Cell3 | +0.0102 | 0.3689 | 0.6008 | |
| Cell2 vs Cell4 | -0.0493 | -1.5467 | 0.4968 | n=1 ref |
| Cell3 vs Cell4 | -0.0595 | -2.4544 | 0.1970 | n=1 ref |

### E. vs Vanilla Baseline
| Cell | Mean | Δ vs Vanilla | Cohen's d | Direction |
|---|---|---|---|---|
| Cell1 (Grad ON + BN) | 0.7253 | -0.0200 | -0.42 | Van > Cell |
| Cell2 (Grad ON + LN) | 0.7767 | +0.0313 | 1.11 | Cell > Van |
| Cell3 (Grad OFF + BN) | 0.7665 | +0.0212 | 0.88 | Cell > Van |
| Cell4 (Grad OFF + LN) | 0.8260 | +0.0807 | 3.35 | Cell > Van (n=1) |
