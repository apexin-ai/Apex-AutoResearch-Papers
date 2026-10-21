# ops t10a075 kill d102 v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_t10a075-kill-d102-v2_20260522T194937_result.json`
- **Structured JSON:** [`7adbf64dff788d8da4ed.json`](../../sessions/7a/7adbf64dff788d8da4ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Gen_10 training is in progress on GPU 3 (started ~03:55 server time). Based on previous generation timing (~27 min generation + ~40 min training + eval), gen_10 should complete around ~05:02 server time (~67 min total).

Here's the current status and results:

---

## Status

- **Server**: westd-17855
- **Data path**: `results/phase_diagram/t10_a075_s42_fp32_14b/`
- **gen_0–gen_9**: Complete with metrics.json
- **gen_10**: Training restarted (PID 714525 on GPU 3), ETA ~40 min remaining
- **No process to kill**: Previous t10_a075 process died (exit code 1) before this session

## Preliminary D102 5-Method Results (gen_0–gen_9, 10 data points)

**Note**: gen_0 and gen_1 have `mauve=null`, so mauve pairs use gen_2–9 (8 points).

### Summary

| Method | Forward sig |
|--------|------------|
| **PermG (FDR)** | **4/8** |
| DiffXCorr (FDR) | 7/8 |
| Naive XCorr (D111) | 4/8 |
| Threshold 3σ | 0/8 |
| TY Granger | 0/8 |
| **K≥3 consensus** | **4/8** |
| K≥4 consensus | 0/8 |

### Consensus Detail
```
token_entropy → distinct_1:  3/5  [naive, diff, perm]
token_entropy → distinct_2:  1/5  [diff]
token_entropy → distinct_3:  1/5  [diff]
token_entropy → mauve:       0/5  [none]
ece → distinct_1:            3/5  [naive, diff, perm]
ece → distinct_2:            3/5  [naive, diff, perm]
ece → distinct_3:            3/5  [naive, diff, perm]
ece → mauve:                 0/5  [none]
```

### KEY DISCRIMINATOR Assessment

**PermG_fwd = 4/8 → Scenario C (weak detection)**

The 4 significant PermG pairs are all ece-based (ece→d1,d2,d3) plus te→d1. The te→d2 (p=0.0472 raw) and te→d3 (p=0.0676 raw) are borderline — FDR correction pushes them above 0.05. Adding gen_10 (11th data point) might tip te→d2 over the line, potentially raising PermG to 5/8, but unlikely to reach 6/8 (Scenario B threshold).

### Drift Statistics (gen_0 → gen_9)
```
token_entropy    2.9731 → 1.9053  (-35.92%)
ece              0.0081 → 0.2660  (+3185.31%)
perplexity       19.83  → 86.73   (+337.37%)
distinct_1       0.0992 → 0.0806  (-18.74%)
distinct_2       0.5222 → 0.4072  (-22.01%)
distinct_3       0.8211 → 0.6704  (-18.35%)
```

**Preliminary JSON saved at**: `/root/autodl-tmp/distrib_canary_collapse/D102_14b_t10_a075_s42_fp32_10gen.json`

The full 11-gen analysis will run automatically once gen_10 finishes. The analysis script is deployed at `run_d102_14b_t10_a075.py` — run it with `python run_d102_14b_t10_a075.py results/phase_diagram/t10_a075_s42_fp32_14b 10` after gen_10/metrics.json appears.

---
