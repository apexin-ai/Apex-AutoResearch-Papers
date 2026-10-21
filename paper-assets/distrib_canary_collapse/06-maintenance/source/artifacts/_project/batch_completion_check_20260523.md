# Batch Experiment Status Check — 2026-05-23 20:45 UTC

## Completed Experiments

### scale_14b_t10_a060_s44_fp32 ✓
- **Server**: westd-17855, PID 780907 (exited)
- **Generations**: gen_0–gen_10 (11 total), all_metrics.json complete
- **Metrics trajectory**:
  - gen_0: entropy=2.973, ece=0.008, distinct_3=0.819, ppl=19.83
  - gen_10: entropy=2.013, ece=0.237, distinct_3=0.598, ppl=63.79
- **D102 (distinct_3)**: 
  - token_entropy→distinct_3: **3/5** consensus [diff, perm, ty]
  - ece→distinct_3: **4/5** consensus [naive, diff, perm, ty]
  - PermG fwd: 2/2, rev: 0/2 — strong forward asymmetry
  - Robust pairs: **2/2**
- **Registry**: DONE (success), metrics + D102 registered

## Still Running

### westd-17855
| exp_id | PID | Elapsed | GPU |
|--------|-----|---------|-----|
| scale_14b_t15_a045_s43_fp32 | 762806 | 15h48m | — |
| scale_14b_t10_a050_s44_fp32 | 781724 | 11h37m | — |
| scale_14b_t10_a045_s44_fp32 | 796624 | 8h11m | — |

### westd-19828
| exp_id | PID | Elapsed | GPU |
|--------|-----|---------|-----|
| scale_14b_t15_a075_s43_fp32 | 857058 | 14h03m | — |
| scale_14b_t10_a075_s44_fp32 | 865467 | 11h43m | — |

## Cross-seed D102 Comparison (T=10, α=0.60, 1.4B)

### s42 (all 4 downstreams, 8 pairs)
- PermG fwd: 4/8, rev: 0/8, robust ≥3: 3/8
- distinct_3 pairs: token_entropy→d3 = 1/5 [diff], ece→d3 = 3/5 [naive, diff, perm]

### s44 (distinct_3 only, 2 pairs) — NEW
- PermG fwd: 2/2, rev: 0/2, robust ≥3: 2/2
- token_entropy→d3 = 3/5 [diff, perm, ty], ece→d3 = 4/5 [naive, diff, perm, ty]

### Notes
- s43 T=10 α=0.60 D102 not yet run (only T=15 variant exists)
- s44 shows stronger consensus than s42 for distinct_3 pairs (TY now significant, likely due to s44 having cleaner signal)
- Forward asymmetry consistent across both seeds
