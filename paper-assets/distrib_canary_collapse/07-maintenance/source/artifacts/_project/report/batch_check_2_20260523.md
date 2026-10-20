# Batch Check 2 — 2026-05-23 20:55 UTC

## Experiment Status

| Experiment | Server | PID | Status | Gens | ETA |
|---|---|---|---|---|---|
| t10_a050_s44_fp32_14b | westd-17855 | 781724 | **DONE** | 11/11 | - |
| t10_a045_s44_fp32_14b | westd-17855 | 796624 | RUNNING (8h21m) | 9/11 | ~2h |
| t15_a045_s43_fp32_14b | westd-17855 | 762806 | RUNNING (15h57m) | 15/16 | ~1h |
| t15_a075_s43_fp32_14b | westd-19828 | 857058 | RUNNING (14h12m) | 14/16 | ~2h |
| t10_a075_s44_fp32_14b | westd-19828 | 865467 | RUNNING (11h52m) | 11/11 (training gen_10) | <1h |

## Completed: t10_a050_s44_fp32_14b (α=0.50, seed=44, T=10, 1.4B)

### Metrics Trajectory

| Gen | token_entropy | ece | distinct_3 | perplexity |
|-----|--------------|------|-----------|-----------|
| 0 | 2.9731 | 0.0081 | 0.8190 | 19.83 |
| 1 | 2.1888 | 0.0968 | 0.8208 | 20.59 |
| 2 | 2.1701 | 0.1188 | 0.7524 | 24.53 |
| 3 | 2.1905 | 0.1278 | 0.6774 | 26.80 |
| 4 | 2.1784 | 0.1335 | 0.6139 | 28.22 |
| 5 | 2.2086 | 0.1359 | 0.5705 | 29.31 |
| 6 | 2.2213 | 0.1393 | 0.5383 | 30.57 |
| 7 | 2.2196 | 0.1444 | 0.5211 | 31.94 |
| 8 | 2.2104 | 0.1493 | 0.5155 | 33.11 |
| 9 | 2.2364 | 0.1502 | 0.5079 | 33.83 |
| 10 | 2.2427 | 0.1504 | 0.5031 | 34.45 |

- distinct_3: 0.819 → 0.503 (↓38.6%)
- perplexity: 19.8 → 34.4 (↑73.7%)
- token_entropy: sharp drop gen_0→gen_1 (2.97→2.19), then stable ~2.2
- ece: sharp rise gen_0→gen_1 (0.008→0.097), then gradual to 0.150

### D102 Analysis (distinct_3 only)

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy→distinct_3 | 2/5 | diff, perm |
| ece→distinct_3 | 2/5 | diff, perm |

- **Robust pairs (≥3/5): 0/2** — consistent with α=0.50 onset boundary behavior
- PermG forward sig: 2/2 (both canaries → distinct_3)
- Threshold onset: 0/2 (canary onset gen 1, distinct_3 onset null under true_3sigma)
- TY Granger: 0/2 (dmax=0, all nan — expected per C003)
- Naive xcorr: peak_lag > 0 for both pairs (filtered as reverse per C009)

### Cross-seed Comparison (α=0.50, T=10, 1.4B)

| Seed | PermG fwd | K≥3 d3 | d3 final | ppl final |
|------|----------|--------|----------|----------|
| s42 | 4/8 | TBD | TBD | TBD |
| s43 | 6/8 | 1/8 | TBD | TBD |
| s44 | 6/8 | 0/8 (d3: 0/2) | 0.503 | 34.45 |

Observation: K≥3 consensus weak (0-1/8) despite moderate PermG rates — characteristic of onset boundary where canary signal exists but doesn't clearly lead downstream.

## Registry Updates

- `scale_14b_t10_a050_s44_fp32` → DONE (success)

## Artifacts

- `D102_14b_t10_a050_s44_fp32_d3.json` — D102 analysis (distinct_3)
- Full 5-method JSON on server: `results/phase_diagram/t10_a050_s44_fp32_14b/analysis/5method_leadlag.json`
