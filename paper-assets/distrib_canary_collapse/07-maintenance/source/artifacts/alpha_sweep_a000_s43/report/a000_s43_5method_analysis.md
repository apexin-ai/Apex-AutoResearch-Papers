# 5-Method Causal Analysis: alpha_sweep_a000_s43

## Experiment Configuration
- **Alpha**: 0.00 (null baseline — pure real-data self-distillation)
- **Seed**: 43
- **Generations**: 11 (gen0–gen10)
- **Purpose**: Validate FPR of 5-method causal framework under null hypothesis

## Drift Metrics (gen0 → gen10)

| Metric | Gen0 | Gen10 | Drift% |
|--------|------|-------|--------|
| token_entropy | 3.2342 | 3.0907 | **-4.4%** |
| ece | 0.0108 | 0.0148 | **+37.2%** |
| perplexity | 26.95 | 21.47 | **-20.3%** |
| distinct_1 | 0.0983 | 0.0847 | **-13.9%** |
| distinct_2 | 0.5132 | 0.4631 | **-9.8%** |
| distinct_3 | 0.8057 | 0.7672 | **-4.8%** |
| effective_rank | 46.61 | 43.72 | **-6.2%** |

## 5-Method Results

### Per-method significance (forward, canary→downstream)

| Method | Sig pairs / Total |
|--------|-------------------|
| Naive XCorr | 5/8 |
| Diff XCorr (FDR) | 3/8 |
| Threshold Onset | 1/8 |
| Permutation Granger (FDR) | **0/8** |
| Toda-Yamamoto | 1/8 |

### Consensus (>=3/5 methods agree)

| Pair | Votes | Agreeing Methods |
|------|-------|-----------------|
| token_entropy→distinct_1 | 2/5 | naive, ty |
| token_entropy→distinct_2 | 2/5 | naive, diff |
| token_entropy→distinct_3 | 2/5 | naive, diff |
| token_entropy→perplexity | 1/5 | diff |
| ece→distinct_1 | 2/5 | naive, threshold |
| ece→distinct_2 | 1/5 | naive |
| ece→distinct_3 | 1/5 | naive |
| ece→perplexity | 0/5 | — |

**Robust pairs (>=3/5): 0/8**

### Key Granger p-values (FDR-adjusted)

| Pair | Perm Granger p_fdr | TY p |
|------|-------------------|------|
| token_entropy→distinct_1 | 0.2122 | 0.0364* |
| token_entropy→distinct_2 | 0.2122 | 0.6661 |
| token_entropy→distinct_3 | 0.2122 | 0.5537 |
| token_entropy→perplexity | 0.9286 | 0.9913 |
| ece→distinct_1 | 0.9208 | 0.0753 |
| ece→distinct_2 | 0.9286 | 0.5282 |
| ece→distinct_3 | 0.9208 | 0.6233 |
| ece→perplexity | 0.9286 | 0.9863 |

*Note: TY token_entropy→distinct_1 shows p=0.0364 with df_resid=1 — this is the known instability issue (C003: d_max=2 leaves only 1 residual df). Not reliable.

## Cross-Seed Comparison (s42 vs s43)

| Metric | s42 drift% | s43 drift% | Consistent? |
|--------|-----------|-----------|-------------|
| token_entropy | -5.1% | -4.4% | Yes |
| ece | +51.7% | +37.2% | Yes (direction match, ECE noisy) |
| perplexity | -21.7% | -20.3% | Yes |
| distinct_1 | -13.8% | -13.9% | Yes |
| distinct_2 | -9.8% | -9.8% | Yes |
| distinct_3 | -4.5% | -4.8% | Yes |
| Granger causal | None | None | Yes |

## Conclusion

**SUCCESS** — The 5-method causal framework correctly produces no false positive causal detections under the null condition (alpha=0.00):

1. **Permutation Granger (FDR)**: 0/8 significant — FPR = 0%
2. **Robust consensus (>=3/5 methods)**: 0/8 — framework properly requires multi-method agreement
3. **Cross-seed consistency**: High — drift magnitudes and causal non-significance replicate across s42/s43

The diff_xcorr "significance" (3/8 pairs) reflects strong contemporaneous metric co-movement under training noise, not forward causality — confirmed by negative/zero peak lags and non-significance of the stricter Granger tests. The naive_xcorr (5/8) is known to have high FPR due to shared autocorrelation trends, which is precisely why the consensus approach is needed.
