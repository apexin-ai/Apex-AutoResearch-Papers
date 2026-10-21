# Shape Test: Step vs Smooth Likelihood Ratio Test

## Version B: All Cells

| Row | N | Step α_c | Step LL | Smooth(fixed) LL | Smooth(free) LL | ΔAIC(fixed) | ΔBIC(fixed) | Preferred |
|-----|---|----------|---------|-----------------|-----------------|-------------|-------------|-----------|
| T=5_phase | 4 | 0.75 | -0.0 | -0.0 | -0.0 | 2.0 | 1.3863 | trivial (all 0) |
| T=10_phase | 4 | 0.45 | -20.0877 | -19.5036 | -16.6356 | 0.8317 | 0.218 | step |
| T=10_dense | 17 | 0.65 | -100.3599 | -44.3488 | -44.3351 | -110.0222 | -109.189 | smooth_fixed |
| T=15_phase | 4 | -0.05 | -24.5864 | -22.0435 | -21.9301 | -3.0858 | -3.6995 | smooth_fixed |
| T=20_phase | 4 | -0.05 | -25.685 | -22.1501 | -22.1182 | -5.0697 | -5.6834 | smooth_fixed |
| T=25_phase | 4 | -0.05 | -19.0933 | -19.0351 | -19.0122 | 1.8836 | 1.2699 | step |

### Detail

**T=5_phase** (N=4, total trials=32)
- All cells = 0/n → both models trivially fit (LL identical). No shape information.

**T=10_phase** (N=4, total trials=32)
- Step: α_c=0.45, LL=-20.0877, AIC=42.1754, BIC=41.5617
- Smooth(P_max=0.75): k=7.3516, α_0=0.5772, LL=-19.5036, AIC=43.0072, BIC=41.7798
  - ΔAIC=0.8317 (negative favors smooth)
  - ΔBIC=0.218
- Smooth(P_max free): k=500.0, α_0=0.475, P_max=0.5, LL=-16.6356, AIC=39.2711, BIC=37.43
  - ΔAIC=-2.9043
  - ΔBIC=-4.1317

**T=10_dense** (N=17, total trials=232)
- Step: α_c=0.65, LL=-100.3599, AIC=202.7197, BIC=203.5529
- Smooth(P_max=0.75): k=15.7243, α_0=0.7176, LL=-44.3488, AIC=92.6975, BIC=94.364
  - ΔAIC=-110.0222 (negative favors smooth)
  - ΔBIC=-109.189
- Smooth(P_max free): k=15.5094, α_0=0.7222, P_max=0.775, LL=-44.3351, AIC=94.6702, BIC=97.1698
  - ΔAIC=-108.0495
  - ΔBIC=-106.3831

**T=15_phase** (N=4, total trials=32)
- Step: α_c=-0.05, LL=-24.5864, AIC=51.1728, BIC=50.5591
- Smooth(P_max=0.75): k=0.9967, α_0=-0.5, LL=-22.0435, AIC=48.087, BIC=46.8596
  - ΔAIC=-3.0858 (negative favors smooth)
  - ΔBIC=-3.6995
- Smooth(P_max free): k=100.0, α_0=0.1, P_max=0.5625, LL=-21.9301, AIC=49.8601, BIC=48.019
  - ΔAIC=-1.3127
  - ΔBIC=-2.5401

**T=20_phase** (N=4, total trials=32)
- Step: α_c=-0.05, LL=-25.685, AIC=53.37, BIC=52.7563
- Smooth(P_max=0.75): k=0.8138, α_0=-0.5, LL=-22.1501, AIC=48.3003, BIC=47.0729
  - ΔAIC=-5.0697 (negative favors smooth)
  - ΔBIC=-5.6834
- Smooth(P_max free): k=99.8387, α_0=0.0277, P_max=0.5312, LL=-22.1182, AIC=50.2363, BIC=48.3952
  - ΔAIC=-3.1337
  - ΔBIC=-4.3611

**T=25_phase** (N=4, total trials=32)
- Step: α_c=-0.05, LL=-19.0933, AIC=40.1867, BIC=39.573
- Smooth(P_max=0.75): k=3.0727, α_0=-0.5, LL=-19.0351, AIC=42.0703, BIC=40.8429
  - ΔAIC=1.8836 (negative favors smooth)
  - ΔBIC=1.2699
- Smooth(P_max free): k=46.8511, α_0=-0.5, P_max=0.7187, LL=-19.0122, AIC=44.0243, BIC=42.1832
  - ΔAIC=3.8376
  - ΔBIC=2.6102

## Version A: Excluding Sync-Dip Cells

| Row | N | Step α_c | Step LL | Smooth(fixed) LL | Smooth(free) LL | ΔAIC(fixed) | ΔBIC(fixed) | Preferred |
|-----|---|----------|---------|-----------------|-----------------|-------------|-------------|-----------|
| T=5_phase | 3 | 0.75 | -0.0 | -0.0 | -0.0 | 2.0 | 1.0986 | trivial (all 0) |
| T=10_phase | 3 | 0.45 | -8.9974 | -8.9974 | -8.9974 | 2.0 | 1.0986 | step |
| T=10_dense | 14 | 0.48 | -72.3479 | -39.4413 | -38.9849 | -63.8132 | -63.1741 | smooth_fixed |
| T=15_phase | 3 | -0.05 | -13.496 | -13.496 | -13.496 | 2.0 | 1.0986 | step |
| T=20_phase | 3 | -0.05 | -14.5947 | -14.2899 | -14.2899 | 1.3904 | 0.489 | step |
| T=25_phase | 4 | -0.05 | -19.0933 | -19.0351 | -19.0122 | 1.8836 | 1.2699 | step |

### Detail

**T=5_phase** (N=3, total trials=24)
- All cells = 0/n → both models trivially fit (LL identical). No shape information.

**T=10_phase** (N=3, total trials=24)
- Step: α_c=0.45, LL=-8.9974, AIC=19.9947, BIC=19.0933
- Smooth(P_max=0.75): k=500.0, α_0=0.4824, LL=-8.9974, AIC=21.9947, BIC=20.192
  - ΔAIC=2.0 (negative favors smooth)
  - ΔBIC=1.0986
- Smooth(P_max free): k=500.0, α_0=0.4829, P_max=0.7501, LL=-8.9974, AIC=23.9947, BIC=21.2906
  - ΔAIC=4.0
  - ΔBIC=2.1972

**T=10_dense** (N=14, total trials=200)
- Step: α_c=0.48, LL=-72.3479, AIC=146.6958, BIC=147.3348
- Smooth(P_max=0.75): k=14.6512, α_0=0.6838, LL=-39.4413, AIC=82.8826, BIC=84.1607
  - ΔAIC=-63.8132 (negative favors smooth)
  - ΔBIC=-63.1741
- Smooth(P_max free): k=45.0774, α_0=0.5468, P_max=0.5489, LL=-38.9849, AIC=83.9698, BIC=85.887
  - ΔAIC=-62.7259
  - ΔBIC=-61.4478

**T=15_phase** (N=3, total trials=24)
- Step: α_c=-0.05, LL=-13.496, AIC=28.9921, BIC=28.0907
- Smooth(P_max=0.75): k=20.0086, α_0=-0.5, LL=-13.496, AIC=30.9921, BIC=29.1893
  - ΔAIC=2.0 (negative favors smooth)
  - ΔBIC=1.0986
- Smooth(P_max free): k=50.0089, α_0=-0.0152, P_max=0.75, LL=-13.496, AIC=32.9921, BIC=30.2879
  - ΔAIC=4.0
  - ΔBIC=2.1972

**T=20_phase** (N=3, total trials=24)
- Step: α_c=-0.05, LL=-14.5947, AIC=31.1893, BIC=30.2879
- Smooth(P_max=0.75): k=135.6696, α_0=0.4381, LL=-14.2899, AIC=32.5797, BIC=30.777
  - ΔAIC=1.3904 (negative favors smooth)
  - ΔBIC=0.489
- Smooth(P_max free): k=130.3737, α_0=0.4377, P_max=0.7501, LL=-14.2899, AIC=34.5797, BIC=31.8756
  - ΔAIC=3.3904
  - ΔBIC=1.5877

**T=25_phase** (N=4, total trials=32)
- Step: α_c=-0.05, LL=-19.0933, AIC=40.1867, BIC=39.573
- Smooth(P_max=0.75): k=3.0727, α_0=-0.5, LL=-19.0351, AIC=42.0703, BIC=40.8429
  - ΔAIC=1.8836 (negative favors smooth)
  - ΔBIC=1.2699
- Smooth(P_max free): k=46.8511, α_0=-0.5, P_max=0.7187, LL=-19.0122, AIC=44.0243, BIC=42.1832
  - ΔAIC=3.8376
  - ΔBIC=2.6102

## Interpretation

- **T=5**: All cells are 0/8 — no detectable signal at any α. Both models fit trivially. No shape discrimination possible.
- **ΔAIC/ΔBIC > 0**: Step model preferred (smooth's extra parameter not justified by improved fit)
- **ΔAIC/ΔBIC < 0**: Smooth model preferred (gradual transition fits data better)
- **Step model** has 1 free parameter (α_c), **smooth(fixed)** has 2 (k, α_0), **smooth(free)** has 3 (k, α_0, P_max)
- The step model's sharp threshold is an idealization; data with n=8 per cell has limited power to distinguish sharp vs gradual transitions
- Sync-dip (α=0.60) is a known structural non-monotonicity that penalizes smooth models; Version A removes it for a cleaner comparison
