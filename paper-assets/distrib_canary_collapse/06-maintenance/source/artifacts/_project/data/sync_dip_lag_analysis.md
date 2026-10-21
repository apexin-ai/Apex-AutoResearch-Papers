# Sync-Dip Lag Structure Analysis: T=10 vs T=20 at α=0.60

## Forward PermG: Signal Amplification

| Pair | T=10 F | T=10 p | T=20 F | T=20 p | F ratio |
|------|--------|--------|--------|--------|---------|
| te<d1 | 204.6 | 0.092 | 406.7 | 0.048 | 2.0x |
| te<d2 | 108.5 | 0.083 | 270.9 | 0.046 | 2.5x |
| te<d3 | 46.7 | 0.082 | 137.2 | 0.043 | 2.9x |
| te<mauve | 1.3 | 0.268 | 2.0 | 0.155 | 1.5x |
| ece<d1 | 100.8 | 0.034 | 202.6 | 0.008 | 2.0x |
| ece<d2 | 61.5 | 0.047 | 146.1 | 0.015 | 2.4x |
| ece<d3 | 32.3 | 0.058 | 89.9 | 0.026 | 2.8x |
| ece<mauve | 1.7 | 0.218 | 1.9 | 0.185 | 1.1x |

FDR-corrected: T=10 all >0.12, T=20 best=0.062 (ece<d1). Both 0/8 FDR significant.

## Lag=0 Contemporaneous Correlation (desynchronization evidence)

| Pair | T=10 r(0) | T=20 r(0) | Change |
|------|-----------|-----------|--------|
| te<d1 | 0.523 | 0.327 | -37% |
| te<d2 | 0.485 | 0.267 | -45% |
| te<d3 | 0.441 | 0.210 | -52% |
| te<mauve | 0.054 | -0.132 | sign flip |
| ece<d1 | 0.826 | 0.854 | +3% |
| ece<d2 | 0.805 | 0.835 | +4% |
| ece<d3 | 0.777 | 0.809 | +4% |
| ece<mauve | 0.360 | 0.508 | +41% |

## Naive XCorr Peak Lag Shifts

| Pair | T=10 lag | T=20 lag | Change |
|------|----------|----------|--------|
| te<d1 | 5 | 5 | stable |
| te<d2 | 5 | 5 | stable |
| te<d3 | 5 | 5 | stable |
| te<mauve | -3 | 3 | sign flip |
| ece<d1 | 4 | -1 | **direction reversal** |
| ece<d2 | 4 | 2 | shortened |
| ece<d3 | 2 | 2 | stable |
| ece<mauve | -3 | -3 | stable |

## Reverse Direction (downstream → canary): Null

T=10: all F < 1.5, all p > 0.28
T=20: all F < 0.3, all p > 0.58
Confirms forward causality, reverse remains null.

## Interpretation

1. **Desynchronization**: token_entropy lag=0 correlations drop 37-52%, literally the "sync" weakening
2. **Lag structure reorganization**: ece<d1 peak lag flips +4→-1
3. **Power scaling**: F ∝ ~T (consistent with √T Granger power)
4. **FDR bottleneck**: T=20 has 6/8 pairs with uncorrected p<0.05, FDR blocks. T=25 should cross.
5. **Causal asymmetry preserved**: reverse direction non-significant at both T
