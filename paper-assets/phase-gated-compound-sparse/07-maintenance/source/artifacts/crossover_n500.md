# SF2: Crossover Verification (n=500)

## Results

| Model | Phase | Imp Median [95% CI] | Rand Median [95% CI] | Diff Median [95% CI] | Wilcoxon p | Sig | n |
|-------|-------|---------------------|----------------------|----------------------|------------|-----|---|
| deepseek | high | 0.021 [0.017, 0.027] | 1.113 [1.020, 1.292] | 1.038 [0.909, 1.141] | 0.0000 | yes | 496 |
| deepseek | low | 3.971 [3.476, 4.405] | 1.498 [1.230, 1.710] | 2.214 [1.590, 2.883] | 0.0000 | yes | 500 |
| qwen | high | 0.004 [0.001, 0.006] | 1.109 [1.002, 1.347] | 1.106 [1.014, 1.339] | 0.0000 | yes | 486 |
| qwen | low | 1.043 [0.950, 1.182] | 1.770 [1.531, 2.052] | -0.922 [-1.171, -0.628] | 0.0000 | yes | 488 |

## Comparison with n=50 (DeepSeek s025)

| Phase | n=50 Imp II | n=50 Rand II | n=500 Imp II [CI] | n=500 Rand II [CI] |
|-------|-------------|--------------|-------------------|---------------------|
| high | 0.032 | 0.818 | 0.021 [0.017, 0.027] | 1.113 [1.020, 1.292] |
| low | 7.196 | 1.363 | 3.971 [3.476, 4.405] | 1.498 [1.230, 1.710] |

## Crossover Verification

- **DeepSeek**: crossover CONFIRMED, both phases significant: YES
- **Qwen**: crossover NOT confirmed, both phases significant: YES
- **DeepSeek crossover magnitude** (low/high): 2.13x

## Qwen Divergence

Qwen shows **no crossover**: random masking produces higher II than importance in BOTH phases.
- High phase: rand (1.109) >> imp (0.004), diff = 1.106 (p < 0.0001)
- Low phase: rand (1.770) > imp (1.043), diff = -0.922 as imp-rand (p < 0.0001)

This means for Qwen, random masking is uniformly worse across all phases, without the phase-dependent strategy reversal seen in DeepSeek.

## Conclusion

Crossover is **model-dependent**:
- **DeepSeek**: Crossover robust at n=500 (both phases p < 0.0001, magnitude 2.13x). Importance masking's compound interaction concentrates in low-sparsity phase; random masking impact is more uniform.
- **Qwen**: No crossover. Random masking is uniformly worse, suggesting Qwen's attention structure responds differently to structured vs. random pruning — the phase-specific interaction pattern is a DeepSeek-specific phenomenon (or at minimum, architecture-dependent).
