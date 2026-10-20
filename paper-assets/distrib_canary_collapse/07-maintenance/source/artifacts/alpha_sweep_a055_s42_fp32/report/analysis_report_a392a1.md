# 5-Method Lead-Lag Analysis: alpha_sweep_a055_s42_fp32

## Experiment Configuration

| Parameter | Value |
|-----------|-------|
| Model | EleutherAI/pythia-410m |
| Dataset | WikiText-103 |
| Seed | 42 |
| Precision | fp32 |
| Alpha (synthetic ratio) | 0.55 |
| Generations | 10 (gen_0 = baseline) |
| Steps/gen | 5000 |
| Batch size | 4 |
| LR | 5e-05 |
| Top-p | 0.95 |
| Intervention | none |

## Per-Generation Metrics

| Gen | token_entropy | ece | perplexity | distinct_1 | distinct_2 | distinct_3 | mauve | eff_rank |
|-----|--------------|------|------------|-----------|-----------|-----------|-------|----------|
| 0 | 3.2342 | 0.0108 | 26.95 | 0.0980 | 0.5141 | 0.8127 | 0.0311 | 46.61 |
| 1 | 2.2356 | 0.1197 | 27.68 | 0.0976 | 0.5125 | 0.8122 | 0.0314 | 66.50 |
| 2 | 2.2057 | 0.1379 | 32.52 | 0.0846 | 0.4378 | 0.7243 | 0.0360 | 71.24 |
| 3 | 2.2467 | 0.1412 | 34.57 | 0.0774 | 0.3902 | 0.6486 | 0.0335 | 71.78 |
| 4 | 2.2411 | 0.1478 | 36.90 | 0.0726 | 0.3548 | 0.5937 | 0.0320 | 73.53 |
| 5 | 2.2557 | 0.1511 | 38.79 | 0.0702 | 0.3292 | 0.5434 | 0.0316 | 73.49 |
| 6 | 2.2484 | 0.1579 | 40.14 | 0.0685 | 0.3135 | 0.5123 | 0.0297 | 73.02 |
| 7 | 2.2930 | 0.1595 | 41.28 | 0.0677 | 0.3043 | 0.4939 | 0.0288 | 73.63 |
| 8 | 2.3159 | 0.1593 | 42.40 | 0.0671 | 0.3012 | 0.4869 | 0.0264 | 71.66 |
| 9 | 2.3561 | 0.1586 | 43.67 | 0.0669 | 0.2987 | 0.4813 | 0.0258 | 72.07 |
| 10 | 2.3578 | 0.1623 | 44.77 | 0.0667 | 0.2968 | 0.4779 | 0.0259 | 71.48 |

## Drift Statistics (gen_0 → gen_10)

| Metric | gen_0 | gen_10 | Delta | % Change | Direction |
|--------|-------|--------|-------|----------|-----------|
| token_entropy | 3.234 | 2.358 | -0.876 | -27.1% | Collapsed (worse) |
| ece | 0.011 | 0.162 | +0.151 | +1400% | Degraded (worse) |
| perplexity | 26.95 | 44.77 | +17.82 | +66.1% | Degraded (worse) |
| distinct_1 | 0.098 | 0.067 | -0.031 | -31.6% | Collapsed (worse) |
| distinct_2 | 0.514 | 0.297 | -0.217 | -42.2% | Collapsed (worse) |
| distinct_3 | 0.813 | 0.478 | -0.335 | -41.2% | Collapsed (worse) |
| mauve | 0.031 | 0.026 | -0.005 | -16.8% | Degraded (worse) |
| eff_rank | 46.61 | 71.48 | +24.87 | +53.4% | Increased |

All quality metrics degrade substantially over 10 generations. The token_entropy sharp drop (gen_0→gen_1: 3.23→2.24) followed by plateau is the characteristic canary pattern. ECE shows strong monotonic increase. Diversity metrics (distinct_1/2/3) show continuous decline. Perplexity rises 66%.

## 5-Method Lead-Lag Summary

| Pair | NaiveXcorr | DiffXcorr (FDR) | Threshold 3sigma | PermG (FDR) | TY Granger | K (votes) |
|------|-----------|----------------|-----------------|------------|-----------|-----------|
| token_entropy→distinct_1 | lag=+5 (reverse) | lag=-5, p_FDR=0.045 **SIG** | onset=None | F=330.7, p_FDR=0.072 | p=0.176 | **1/5** [diff] |
| token_entropy→distinct_2 | lag=+5 (reverse) | lag=-5, p_FDR=0.045 **SIG** | onset=None | F=362.1, p_FDR=0.072 | p=0.053 | **1/5** [diff] |
| token_entropy→distinct_3 | lag=+5 (reverse) | lag=-5, p_FDR=0.045 **SIG** | onset=None | F=217.1, p_FDR=0.072 | p=0.219 | **1/5** [diff] |
| token_entropy→mauve | lag=+1 (reverse) | lag=-1, p_FDR=0.007 **SIG** | onset=None | F=47.5, p_FDR=0.072 | p=0.057 | **1/5** [diff] |
| ece→distinct_1 | lag=+2 (reverse) | lag=-5, p_FDR=0.045 **SIG** | onset=None | F=274.1, p_FDR=0.072 | p=0.020 **SIG** | **2/5** [diff, ty] |
| ece→distinct_2 | lag=+2 (reverse) | lag=-5, p_FDR=0.045 **SIG** | onset=None | F=228.1, p_FDR=0.072 | p=0.545 | **1/5** [diff] |
| ece→distinct_3 | lag=+2 (reverse) | lag=-5, p_FDR=0.045 **SIG** | onset=None | F=210.4, p_FDR=0.072 | p=0.360 | **1/5** [diff] |
| ece→mauve | lag=-5 (forward) | lag=-1, p_FDR=0.011 **SIG** | onset=None | F=38.0, p_FDR=0.072 | p=0.207 | **2/5** [naive, diff] |

### Method-Level Counts

| Method | Forward Sig | Notes |
|--------|------------|-------|
| Naive xcorr | 1/8 | Only ece→mauve (lag=-5); rest have positive lags (reverse direction) |
| Diff xcorr (FDR) | 8/8 | All pairs significant, all negative lags (forward direction) |
| Threshold onset (3sigma) | 0/8 | No downstream 3sigma onset detected for any pair |
| Perm Granger (FDR) | **0/8** | All p_FDR=0.072, just above α=0.05 threshold |
| TY Granger | 1/8 | Only ece→distinct_1 (p=0.020) |

### Consensus

- K≥3 pairs: **0/8**
- K≥4 pairs: **0/8**
- PermG forward sig: **0/8**

## PermG Forward Detail

| Pair | F-stat | p_raw | p_FDR | Sig? |
|------|--------|-------|-------|------|
| token_entropy→distinct_1 | 330.654 | 0.092 | 0.092 | No |
| token_entropy→distinct_2 | 362.067 | 0.072 | 0.072 | No |
| token_entropy→distinct_3 | 217.112 | 0.072 | 0.072 | No |
| token_entropy→mauve | 47.534 | 0.072 | 0.072 | No |
| ece→distinct_1 | 274.078 | 0.072 | 0.072 | No |
| ece→distinct_2 | 228.116 | 0.072 | 0.072 | No |
| ece→distinct_3 | 210.398 | 0.072 | 0.072 | No |
| ece→mauve | 37.950 | 0.072 | 0.072 | No |

Note: F-statistics are very large (38–362), indicating strong Granger signal, but permutation p-values cluster at 0.072 — just above FDR threshold. This is consistent with a borderline signal that doesn't survive multiple comparison correction.

## PermG Reverse Detail

| Pair | F-stat | p_raw | p_FDR | Sig? |
|------|--------|-------|-------|------|
| distinct_1→token_entropy | 0.156 | 0.072 | 0.072 | No |
| distinct_2→token_entropy | 0.033 | 0.072 | 0.072 | No |
| distinct_3→token_entropy | 0.027 | 0.072 | 0.072 | No |
| mauve→token_entropy | 0.551 | 0.072 | 0.072 | No |
| distinct_1→ece | 0.048 | 0.072 | 0.072 | No |
| distinct_2→ece | 0.215 | 0.072 | 0.072 | No |
| distinct_3→ece | 0.760 | 0.072 | 0.072 | No |
| mauve→ece | 0.151 | 0.072 | 0.072 | No |

Forward F-stats (38–362) >> Reverse F-stats (0.03–0.76) confirms strong directional asymmetry: canaries lead downstream, but the permutation test lacks power at T=11 to declare significance.

## Conclusion

**PermG = 0/8, K≥3 = 0/8.** α=0.55 shows NO detectable lead-lag signal by the PermG consensus criterion.

### Hypothesis Evaluation

Hypothesis: α=0.55 fills the onset(0.50)→sync(0.60) transition gap. α=0.50 has PermG=6/8, α=0.60 has PermG=0/8.

**Result: α=0.55 aligns with α=0.60 (PermG=0/8), not with α=0.50 (PermG=6/8).** This places the sync-collapse dip onset between α=0.50 and α=0.55 — a narrower window than expected.

### Dose-Response Context

| Alpha | PermG | K≥3 | Zone |
|-------|-------|-----|------|
| 0.45 | 0/8 | 0/8 | Blind zone |
| **0.50** | **6/8** | **—** | **Onset** |
| **0.55** | **0/8** | **0/8** | **Sync collapse (this experiment)** |
| 0.60 | 0/8 | 0/8 | Sync collapse |
| 0.75 | 6/8 | —  | Detection regime |

The sync-collapse dip starts immediately after onset at α=0.50. The 0.50→0.55 boundary is sharp — PermG drops from 6/8 to 0/8 in a Δα=0.05 step. This sharpness is itself informative: it suggests the transition from detectable lead-lag to synchronized collapse is abrupt rather than gradual.

### Caveats

- DiffXcorr shows 8/8 forward significance — the temporal signal exists but PermG (the primary consensus method) cannot confirm it at T=11.
- PermG p-values cluster at 0.072 (borderline). With more generations (T>11), some might cross the 0.05 threshold.
- TY Granger results at α=0.55 are marginal (1/8 sig), consistent with known instability at moderate α (C003 applies to α≤0.50 but the boundary zone 0.50–0.55 likely shares similar TY limitations).
