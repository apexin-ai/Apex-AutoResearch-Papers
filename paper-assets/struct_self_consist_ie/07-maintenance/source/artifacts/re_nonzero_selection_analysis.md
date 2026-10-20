# RE Non-zero F1 Conditional Selection Analysis

**Experiment**: exp_012_rerun_1024 (Qwen SciERC joint NER+RE, N=8, seed=42, max_tokens=1024)
**Date**: 2026-05-15

## Dataset Statistics

| Metric | Count | Pct |
|--------|-------|-----|
| Total instances | 551 | 100% |
| Non-zero RE greedy F1 | 238 | 43.2% |
| Zero RE greedy F1 | 313 | 56.8% |

Over half of the instances have greedy RE F1 = 0 (no correct relations extracted).

## Selection Performance — Full Set (n=551)

| Signal | Selected F1 | Greedy F1 | Oracle F1 | Gain | p-value |
|--------|------------|-----------|-----------|------|---------|
| LP | 0.2845 | 0.2913 | 0.4215 | -0.0068 | 1.000 |
| FK | 0.2789 | 0.2913 | 0.4215 | -0.0123 | 1.000 |
| SJ | 0.2777 | 0.2913 | 0.4215 | -0.0135 | 1.000 |
| VC | 0.2588 | 0.2913 | 0.4215 | -0.0325 | 1.000 |
| EM | 0.2679 | 0.2913 | 0.4215 | -0.0233 | 1.000 |

## Selection Performance — Non-zero F1 Subset (n=238)

| Signal | Selected F1 | Greedy F1 | Oracle F1 | Gain | p-value |
|--------|------------|-----------|-----------|------|---------|
| LP | 0.5995 | 0.6743 | 0.7574 | -0.0748 | 1.000 |
| FK | 0.6063 | 0.6743 | 0.7574 | -0.0680 | 1.000 |
| SJ | 0.6035 | 0.6743 | 0.7574 | -0.0708 | 1.000 |
| VC | 0.5737 | 0.6743 | 0.7574 | -0.1005 | 1.000 |
| EM | 0.5828 | 0.6743 | 0.7574 | -0.0914 | 1.000 |

## Comparison: Full vs Non-zero

| Signal | Full Gain | Non-zero Gain | Delta |
|--------|-----------|---------------|-------|
| LP | -0.0068 | -0.0748 | -0.0680 |
| FK | -0.0123 | -0.0680 | -0.0557 |
| SJ | -0.0135 | -0.0708 | -0.0573 |
| VC | -0.0325 | -0.1005 | -0.0680 |
| EM | -0.0233 | -0.0914 | -0.0681 |

## Conclusion

**Zero-F1 instances are NOT masking good selection performance.** The opposite is true:

1. **All 5 signals fail to beat greedy** on both full and non-zero subsets (all gains negative, all p=1.0).

2. **Non-zero subset is worse, not better.** Selection gain magnitudes are 5-10x larger (more negative) on the non-zero subset. On the full set, zero-F1 instances dilute the damage because signal-based selection on zero-F1 instances often picks another zero-F1 sample (no harm done). On the non-zero subset, greedy is already strong (F1=0.6743), and signals actively pick inferior samples.

3. **Oracle gap remains large** (0.7574 vs 0.6743 on non-zero subset), confirming there is room for improvement — but current signals cannot exploit it. The signals are not just noisy; they are anti-correlated with quality for RE.

4. **VC and EM are the worst selectors**, with gains of -0.1005 and -0.0914 on the non-zero subset, likely because majority voting and exact match favor conservative (fewer relations) outputs that happen to miss correct relations.
