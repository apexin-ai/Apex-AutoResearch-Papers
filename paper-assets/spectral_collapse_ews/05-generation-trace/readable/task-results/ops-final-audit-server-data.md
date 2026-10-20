# ops final audit server data

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_final-audit-server-data_20260524T042839_result.json`
- **Structured JSON:** [`0db9cb29f262d3644c6d.json`](../../sessions/0d/0db9cb29f262d3644c6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete audit:

---

## 1. Complete Gen-10 Metrics: All Pythia-410M Experiments

### r=0.0 (Pure Collapse) — 3 seeds

| Metric | seed42 | seed43 | seed44 | **Mean ± Std** |
|--------|--------|--------|--------|---------------|
| log_det | 2178.949 | 2210.766 | 2154.336 | **2181.35 ± 28.29** |
| effective_rank | 442.458 | 438.785 | 432.912 | **438.05 ± 4.82** |
| perplexity | 76.781 | 70.500 | 65.698 | **70.99 ± 5.56** |
| distinct_4 | 0.4259 | 0.3940 | 0.1515 | **0.3238 ± 0.1501** |
| train_loss | 0.978 | 0.915 | 0.327 | **0.74 ± 0.36** |
| sigma1 | 825.72 | 886.08 | 911.87 | — |

**Mean log_det trajectory:**
| gen | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-----|---|---|---|---|---|---|---|---|---|---|---|
| log_det | 2366.68 | 2462.26 | 2467.98 | 2440.45 | 2406.00 | 2365.99 | 2326.11 | 2293.24 | 2246.06 | 2210.43 | 2181.35 |

**maxΔ_t:** α=0.3: raw=33.33, norm=0.01408 | α=0.5: raw=40.38, norm=0.01706 | α=0.7: raw=43.42, norm=0.01835

---

### r=0.2 — 3 seeds

| Metric | seed42 | seed43 | seed44 | **Mean ± Std** |
|--------|--------|--------|--------|---------------|
| log_det | 2479.696 | 2455.777 | 2466.152 | **2467.21 ± 11.99** |
| effective_rank | 511.255 | 505.982 | 506.951 | **508.06 ± 2.81** |
| perplexity | 13.830 | 13.399 | 13.391 | **13.54 ± 0.25** |
| distinct_4 | 0.5203 | 0.2453 | 0.2061 | **0.3239 ± 0.1712** |
| train_loss | 1.392 | 0.938 | 0.867 | **1.07 ± 0.28** |
| sigma1 | 752.27 | 714.87 | 700.91 | — |

**Mean log_det trajectory:**
| gen | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-----|---|---|---|---|---|---|---|---|---|---|---|
| log_det | 2366.68 | 2367.40 | 2359.42 | 2364.61 | 2377.87 | 2396.84 | 2417.66 | 2429.01 | 2442.39 | 2456.01 | 2467.21 |

**maxΔ_t:** α=0.3: raw=2.24, norm=0.000948 | α=0.5: raw=3.81, norm=0.001611 | α=0.7: raw=5.44, norm=0.002297

---

### r=0.25 — 3 seeds

| Metric | seed42 | seed43 | seed44 | **Mean ± Std** |
|--------|--------|--------|--------|---------------|
| log_det | 2485.007 | 2488.577 | 2490.738 | **2488.11 ± 2.89** |
| effective_rank | 512.465 | 515.556 | 513.440 | **513.82 ± 1.58** |
| perplexity | 13.285 | 13.611 | 13.330 | **13.41 ± 0.18** |
| distinct_4 | 0.3572 | 0.3380 | 0.3315 | **0.3423 ± 0.0134** |
| train_loss | 1.319 | 1.061 | 1.172 | **1.18 ± 0.13** |
| sigma1 | 702.94 | 758.92 | 690.91 | — |

**Mean log_det trajectory:**
| gen | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-----|---|---|---|---|---|---|---|---|---|---|---|
| log_det | 2366.68 | 2364.54 | 2363.41 | 2379.82 | 2397.04 | 2417.32 | 2433.62 | 2450.76 | 2464.04 | 2478.96 | 2488.11 |

**maxΔ_t:** α=0.3: raw=0.79, norm=0.000333 | α=0.5: raw=1.10, norm=0.000465 | α=0.7: raw=1.24, norm=0.000524

---

### r=0.3 — 3 seeds

| Metric | seed42 | seed43 | seed44 | **Mean ± Std** |
|--------|--------|--------|--------|---------------|
| log_det | 2511.130 | 2508.325 | 2505.248 | **2508.23 ± 2.94** |
| effective_rank | 521.256 | 521.193 | 520.893 | **521.11 ± 0.19** |
| perplexity | 13.377 | 13.306 | 13.349 | **13.34 ± 0.04** |
| distinct_4 | 0.3422 | 0.1217 | 0.4197 | **0.2945 ± 0.1546** |
| train_loss | 1.304 | 1.032 | 1.185 | **1.17 ± 0.14** |
| sigma1 | 689.47 | 700.98 | 695.97 | — |

**Mean log_det trajectory:**
| gen | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-----|---|---|---|---|---|---|---|---|---|---|---|
| log_det | 2366.68 | 2365.17 | 2369.05 | 2388.60 | 2408.89 | 2429.22 | 2449.61 | 2464.93 | 2480.05 | 2496.79 | 2508.23 |

**maxΔ_t:** α=0.3: 0.0000 | α=0.5: 0.0000 | α=0.7: 0.0000 (monotonically increasing after EMA)

---

### r=0.5 — 2 seeds

| Metric | seed42 | seed43 | **Mean ± Std** |
|--------|--------|--------|---------------|
| log_det | 2573.198 | 2570.092 | **2571.64 ± 2.20** |
| effective_rank | 554.512 | 552.400 | **553.46 ± 1.49** |
| perplexity | 15.196 | 15.030 | **15.11 ± 0.12** |
| distinct_4 | 0.0954 | 0.2088 | **0.1521 ± 0.0802** |
| train_loss | 0.869 | 1.051 | **0.96 ± 0.13** |
| sigma1 | 607.80 | 622.69 | — |

**Mean log_det trajectory:**
| gen | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-----|---|---|---|---|---|---|---|---|---|---|---|
| log_det | 2366.68 | 2364.12 | 2394.46 | 2422.49 | 2453.31 | 2483.08 | 2507.68 | 2526.81 | 2546.02 | 2561.13 | 2571.64 |

**maxΔ_t:** all 0.0000 (monotonically increasing after EMA)

---

### Adaptive (k=10, seed42)

| gen | log_det | eff_rank | ppl | distinct_4 | train_loss | mix_ratio | sigma1 |
|-----|---------|----------|-----|------------|------------|-----------|--------|
| 0 | 2366.683 | 417.547 | 9.554 | 0.7414 | — | — | 1942.82 |
| 1 | 2365.105 | 477.309 | 10.089 | 0.7099 | 1.984 | 0.5 | 951.45 |
| 2 | 2394.006 | 487.078 | 10.416 | 0.5995 | 1.934 | 0.5 | 886.38 |
| 3 | 2423.829 | 496.030 | 10.855 | 0.5204 | 1.848 | 0.5 | 839.60 |
| 4 | 2448.261 | 501.187 | 11.135 | 0.4304 | 1.572 | 0.5 | 818.95 |
| 5 | 2488.078 | 512.499 | 11.643 | 0.3730 | 1.467 | 0.5 | 767.53 |
| 6 | 2507.623 | 518.892 | 12.144 | 0.3556 | 1.325 | 0.5 | 754.41 |
| 7 | 2526.186 | 526.887 | 12.723 | 0.2905 | 1.251 | 0.5 | 721.69 |
| 8 | 2542.886 | 535.300 | 13.397 | 0.2558 | 1.149 | 0.5 | 685.64 |
| 9 | 2560.137 | 544.501 | 14.159 | 0.2260 | 1.062 | 0.5 | 651.36 |
| 10 | 2572.220 | 553.758 | 15.100 | 0.2388 | 0.991 | 0.5 | 610.19 |

Controller never triggered (all `triggered: false`), kept r=0.5 throughout. Budget exhausted at t=9 (B_rem=0.0).

---

## 2. GPT2-M Pure Collapse (seed42) — 8 generations (0–7)

| gen | log_det | eff_rank | ppl | distinct_4 | train_loss | sigma1 |
|-----|---------|----------|-----|------------|------------|--------|
| 0 | 689.441 | 23.087 | 15.454 | 0.9127 | — | 6598.11 |
| 1 | 885.302 | 155.218 | 16.420 | 0.8907 | 2.358 | 1463.46 |
| 2 | 924.392 | 185.368 | 18.941 | 0.8682 | 2.119 | 1190.66 |
| 3 | 889.704 | 184.864 | 23.335 | 0.8368 | 2.052 | 1172.31 |
| 4 | 817.553 | 169.561 | 32.107 | 0.7636 | 1.993 | 1224.00 |
| 5 | 732.124 | 151.938 | 49.349 | 0.6583 | 1.913 | 1317.46 |
| 6 | 658.122 | 136.094 | 76.807 | 0.5590 | 1.821 | 1449.27 |
| 7 | 576.615 | 121.290 | 123.664 | 0.5008 | 1.740 | 1548.42 |

---

## 3. 1B Pilot Data — 4 generations (0–3)

| gen | log_det | eff_rank | ppl | distinct_4 | train_loss | sigma1 |
|-----|---------|----------|-----|------------|------------|--------|
| 0 | 2835.321 | 516.139 | 8.073 | 0.7510 | — | 1661.24 |
| 1 | 2905.739 | 570.747 | 9.409 | 0.6335 | 1.530 | 1052.79 |
| 2 | 2893.847 | 580.918 | 11.040 | 0.5382 | 1.218 | 916.30 |
| 3 | 2864.785 | 580.634 | 13.439 | 0.5014 | 1.027 | 873.50 |

(Stopped at gen 3; shows log_det decline from gen 1→3, matching Pythia-410M collapse pattern)

---

## 4. EWS Indicator Files

**7 files found** in `results/`:
- `alternative_ews_comparison.json` — r=0 baseline, 11 gens: attn_dense_sigma1, ffn_down_sigma1, attn_dense_stable_rank, ffn_down_stable_rank, isotropy, token_entropy, gradient_norm
- `alternative_ews_v2_exp001.json` — r=0, adds: rankme, slv_log_det, ppl, ppl_growth_rate
- `alternative_ews_v2_exp004.json` — r=0.5 fixed mix, same metrics as v2_exp001
- `alternative_ews_v2_exp006.json` — r=0.5 adaptive, same metrics
- `alternative_ews_exp004_fixedmix.json` — r=0.5 fixed (no gradient_norm)
- `alternative_ews_exp006_adaptive.json` — r=0.5 adaptive (no gradient_norm)
- `alternative_ews_r05_comparison.json` — combined r=0 vs r=0.5 comparison

### Key EWS values at gen 10 (from v2 files):

**r=0 (exp001):**
- slv_log_det: 2207.568 (gen 9) → declining
- rankme: 717.470 (gen 9)
- isotropy: 0.0698 (gen 9)
- token_entropy: 6.183 (gen 9)
- ppl_growth_rate: 14.035 (gen 9)
- attn_dense_sigma1: 2.601, ffn_down_sigma1: 8.424

**r=0.5 fixed (exp004), gen 10:**
- slv_log_det: 2572.220
- rankme: 810.617
- isotropy: 0.0327
- token_entropy: 6.912
- ppl: 15.100, ppl_growth_rate: 0.941
- attn_dense_sigma1: 2.417, ffn_down_sigma1: 8.353

**r=0.5 adaptive (exp006), gen 10:**
- slv_log_det: 2572.220
- rankme: 810.617
- isotropy: 0.0327
- token_entropy: 6.912
- ppl: 15.100, ppl_growth_rate: 0.941

(exp004 and exp006 have identical gen 10 values because adaptive controller never triggered — both ran at r=0.5)

---

## 5. Additional Analysis Files

**controller_activation_analysis.json:** τ=0.002, α=0.5. r=0 shows positive delta (decay), r=0.5 shows negative delta (growth). Controller never triggers for r=0.5.

**second_order_analysis.json:** Full EMA/delta1/delta2 trajectories for r=0, r=0.2, r=0.5 (seed42 only).

**No hellaswag data found** in any results file.

---
