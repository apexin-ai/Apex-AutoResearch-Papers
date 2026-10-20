# SF2: Crossover Verification Across All Sparsity Levels (DeepSeek, n=500)

## Summary

Crossover (strategy ranking reversal between phases) is confirmed at **all 4 sparsity levels**, all p < 0.001.

| Sparsity | Crossover | High Diff [CI] | Low Diff [CI] | Reversal Mag |
|----------|-----------|----------------|---------------|--------------|
| s015 | YES *** | 0.087 [0.063, 0.108] | 0.261 [0.212, 0.317] | 2.99x |
| s020 | YES *** | 0.259 [0.227, 0.317] | 0.733 [0.598, 0.868] | 2.83x |
| s025 | YES *** | 1.038 [0.909, 1.141] | 2.214 [1.590, 2.883] | 2.13x |
| s030 | YES *** | 2.856 [2.403, 3.572] | 4.735 [3.261, 6.004] | 1.66x |

High Diff = rand_ii_high − imp_ii_high (positive = random worse in high phase)
Low Diff = imp_ii_low − rand_ii_low (positive = importance worse in low phase)

## Key Findings

1. **s015 concern resolved**: Despite random s015 being NS in the main D analysis (overall II_low − II_high), the per-phase crossover is highly significant (high: p=1.35e-21, low: p=2.59e-17). The crossover exists but at small absolute magnitude.

2. **Reversal magnitude decreases with sparsity**: 2.99x (s015) → 1.66x (s030). At low sparsity, low-phase dominance is relatively stronger; at high sparsity, the high-phase difference grows faster, narrowing the ratio.

3. **Absolute differences scale monotonically**: Both high-phase and low-phase differences grow with sparsity, consistent with the dose-response pattern.

## Paper Implication

**"across all sparsity levels" is supported.** No need to restrict the claim to s ≥ 0.20.

## Per-Phase Detail

### s015
- High phase: imp II = 0.003 [0.001, 0.005], rand II = 0.083 [0.065, 0.099], diff = 0.087, p < 0.0001
- Low phase: imp II = 0.353 [0.319, 0.391], rand II = 0.089 [0.073, 0.115], diff = 0.261, p < 0.0001

### s020
- High phase: imp II = 0.008 [0.003, 0.011], rand II = 0.270 [0.241, 0.325], diff = 0.259, p < 0.0001
- Low phase: imp II = 1.198 [1.089, 1.304], rand II = 0.349 [0.303, 0.440], diff = 0.733, p < 0.0001

### s025
- High phase: imp II = 0.021 [0.017, 0.027], rand II = 1.113 [1.020, 1.292], diff = 1.038, p < 0.0001
- Low phase: imp II = 3.971 [3.476, 4.405], rand II = 1.498 [1.230, 1.710], diff = 2.214, p < 0.0001

### s030
- High phase: imp II = 0.038 [0.033, 0.048], rand II = 3.112 [2.698, 3.608], diff = 2.856, p < 0.0001
- Low phase: imp II = 8.456 [7.780, 9.762], rand II = 3.840 [3.224, 4.426], diff = 4.735, p < 0.0001
