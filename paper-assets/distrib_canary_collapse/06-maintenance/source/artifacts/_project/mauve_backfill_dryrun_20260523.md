# Mauve Backfill Dry-Run Verification — 2026-05-23

## Script
`scripts/backfill_mauve.py` deployed to westd-17855:`/root/autodl-tmp/distrib_canary_collapse/scripts/backfill_mauve.py`

## Dry-Run: t15_a050_s43_fp32_14b

```
Scanning 1 experiment directories...
[SKIP] No metrics.json: results/phase_diagram/t15_a050_s43_fp32_14b/gen_13

Found 13 gens with null mauve:
  t15_a050_s43_fp32_14b/gen_0
  t15_a050_s43_fp32_14b/gen_1
  t15_a050_s43_fp32_14b/gen_2
  t15_a050_s43_fp32_14b/gen_3
  t15_a050_s43_fp32_14b/gen_4
  t15_a050_s43_fp32_14b/gen_5
  t15_a050_s43_fp32_14b/gen_6
  t15_a050_s43_fp32_14b/gen_7
  t15_a050_s43_fp32_14b/gen_8
  t15_a050_s43_fp32_14b/gen_9
  t15_a050_s43_fp32_14b/gen_10
  t15_a050_s43_fp32_14b/gen_11
  t15_a050_s43_fp32_14b/gen_12
```

13/14 gens have null mauve (gen_13 missing metrics.json — likely still running or incomplete).

## Skip Validation: t15_a060_s43_fp32_14b

Original gen_0 mauve: `0.032912636892215505`

```
Scanning 1 experiment directories...
[SKIP] No metrics.json: results/phase_diagram/t15_a060_s43_fp32_14b/gen_13

Found 0 gens with null mauve:

Nothing to backfill.
```

All 13 gens correctly skipped (valid mauve values present).

## HF_HOME Environment Check

| PID | Process | HF_HOME |
|-----|---------|---------|
| 749427 | t15_a060_s43 | `/root/autodl-tmp/.hf_cache` (set) |
| 796624 | t10_a045_s44 | **NOT SET** |

PID 796624 (t10_a045_s44) lacks HF_HOME — confirms the failure pattern for experiments launched without env setup.
