# Batch Check #3 — 2026-05-23 21:09 UTC

## westd-19828

### scale_14b_t10_a075_s44_fp32 — DONE
- PID 865467: EXITED
- gen_0–gen_10 complete (11/11)
- Metrics trajectory:
  - entropy: 2.9731 → 1.9102 (collapse then partial recovery)
  - distinct_3: 0.8190 → 0.6636 (monotonic decrease)
  - ppl: 19.83 → 89.59 (monotonic increase)
  - ece: 0.0081 → 0.2677 (sharp jump at gen_1, plateau)
- **D102 (distinct_3)**: 2/2 robust pairs (≥3/5 methods)
  - token_entropy→distinct_3: 3/5 [diff, perm, ty]
  - ece→distinct_3: 3/5 [naive, diff, perm]
  - PermG FDR fwd=2/2, rev=0/2
- Registry: DONE (success)
- Artifact: `D102_14b_t10_a075_s44_fp32_d3.json`

### scale_14b_t15_a075_s43_fp32 — RUNNING
- PID 857058: alive, elapsed 14h22m
- gen_0–gen_13 complete (14/16 expected for T=15)
- ETA: ~2h remaining

## westd-17855

### scale_14b_t10_a045_s44_fp32 — RUNNING
- PID 796624: alive, elapsed 8h31m
- gen_0–gen_8 complete (9/11 expected for T=10)
- ETA: ~2h remaining

### scale_14b_t15_a045_s43_fp32 — RUNNING
- PID 762806: alive, elapsed 16h07m
- gen_0–gen_14 complete (15/16 expected for T=15)
- ETA: <1h remaining

## Actions Taken
1. Patched `run_5method_analysis_d102.py` on 19828 to skip all-None downstreams (mauve)
2. Ran D102 5-method analysis on t10_a075_s44_fp32_14b
3. Updated registry: scale_14b_t10_a075_s44_fp32 → DONE (success)
4. Registered artifact: D102_14b_t10_a075_s44_fp32_d3.json

## Pending
- t15_a075_s43 (19828): ~2h to completion → need D102 after
- t15_a045_s43 (17855): <1h to completion → need D102 after
- t10_a045_s44 (17855): ~2h to completion → need D102 after
