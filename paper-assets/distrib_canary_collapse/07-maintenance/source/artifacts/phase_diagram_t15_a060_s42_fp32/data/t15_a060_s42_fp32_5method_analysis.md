# 5-Method Analysis: T=15 α=0.60 s42 fp32
# Date: 2026-05-21

## Key Result: SYNC-DIP PERSISTS at T=15

PermG_fwd = 0/8 — confirms α=0.60 sync-dip is continuous from T=10 through T=15 through T=20.

## Summary Metrics

| Metric | Value |
|--------|-------|
| PermG_fwd | 0/8 |
| PermG_rev | 0/8 |
| diff_xcorr_fdr_fwd | 6/8 |
| threshold_onset_3sigma | 4/8 |
| TY_granger | 4/8 |
| robust_pairs (≥3/5) | 3/8 |

## Drift Percentages (gen_0 → gen_15)

| Metric | gen_0 | gen_15 | Drift % |
|--------|-------|--------|---------|
| token_entropy | 3.2342 | 2.4088 | -25.52% |
| ece | 0.0108 | 0.1817 | +1582.4% |
| distinct_1 | 0.0980 | 0.0676 | -31.02% |
| distinct_2 | 0.5141 | 0.3093 | -39.83% |
| distinct_3 | 0.8127 | 0.5057 | -37.77% |
| mauve | 0.0311 | 0.0272 | -12.54% |

## Threshold Onset (3sigma_d105, forward)

| Pair | canary_onset | downstream_onset | lead_time |
|------|-------------|-----------------|-----------|
| token_entropy→distinct_1 | 1 | 10 | 9 |
| token_entropy→distinct_2 | 1 | 14 | 13 |
| token_entropy→distinct_3 | null | null | null |
| token_entropy→mauve | null | null | null |
| ece→distinct_1 | 2 | 10 | 8 |
| ece→distinct_2 | 2 | 14 | 12 |
| ece→distinct_3 | null | null | null |
| ece→mauve | null | null | null |

## Consensus (forward significance)

- token_entropy→distinct_1: 2/5 [diff, threshold]
- token_entropy→distinct_2: 3/5 [diff, threshold, ty]
- token_entropy→distinct_3: 2/5 [diff, ty]
- token_entropy→mauve: 0/5
- ece→distinct_1: 3/5 [naive, diff, threshold]
- ece→distinct_2: 3/5 [diff, threshold, ty]
- ece→distinct_3: 2/5 [diff, ty]
- ece→mauve: 1/5 [naive]

## Phase Diagram Context

| Experiment | T | α | PermG_fwd |
|-----------|---|---|-----------|
| T=10 α=0.60 | 10 | 0.60 | 0/8 (sync-dip) |
| **T=15 α=0.60** | **15** | **0.60** | **0/8 (sync-dip persists)** |
| T=20 α=0.60 | 20 | 0.60 | 0/8 (sync-dip) |
| T=15 α=0.45 | 15 | 0.45 | 6/8 |
| T=15 α=0.50 | 15 | 0.50 | 6/8 |

Conclusion: The sync-dip at α=0.60 is NOT a boundary effect — it spans T=10→T=15→T=20 continuously. Despite α=0.60 >> α_c(15)≈0.304, PermG cannot detect forward causation. Other methods (diff_xcorr 6/8, threshold 4/8, TY 4/8) detect degradation signal, confirming collapse IS occurring but metrics move too synchronously for PermG to establish temporal precedence.
