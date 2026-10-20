# exp_019 Analysis Report: r=0.2, seed44, gen0-10

## Experiment Summary

| Field | Value |
|-------|-------|
| Experiment | exp_019 |
| Condition | fixed_mix, r=0.2 |
| Seed | 44 |
| Model | EleutherAI/pythia-410m-deduped |
| Generations | 0-10 |
| Parent | exp_017 |
| Checkpoint | /root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r02_seed44/ |
| Log | ~/runs/spectral_collapse_ews/exp_019.log |

---

## 1. Per-Generation Metrics (exp_019, seed44)

| Gen | SLV (log_det) | eff_rank | PPL | D-4 | train_loss |
|-----|---------------|----------|-------|--------|------------|
| 0 | 2366.68 | 417.55 | 9.554 | 0.7305 | — |
| 1 | 2369.43 | 476.57 | 10.277 | 0.6542 | 1.765 |
| 2 | **2361.11** | 483.16 | 10.727 | 0.5619 | 1.647 |
| 3 | 2365.55 | 486.48 | 11.137 | 0.4685 | 1.433 |
| 4 | 2377.06 | 489.16 | 11.497 | 0.3990 | 1.266 |
| 5 | 2395.62 | 493.06 | 11.834 | 0.3771 | 1.149 |
| 6 | 2411.78 | 494.10 | 12.160 | 0.3330 | 1.134 |
| 7 | 2424.37 | 495.67 | 12.440 | 0.3068 | 1.060 |
| 8 | 2436.08 | 497.18 | 12.734 | 0.2834 | 0.996 |
| 9 | 2451.25 | 502.60 | 13.072 | 0.2320 | 0.957 |
| 10 | 2466.15 | 506.95 | 13.391 | 0.2061 | 0.867 |

**Trajectory classification: Type II** — transient SLV dip at Gen2 (Δ=-5.58), followed by recovery and monotonic growth.

**Summary deltas (gen0→gen10):**
- SLV: +99.47 (+4.20%)
- eff_rank: +89.40 (+21.4%)
- PPL: +3.84 (+40.2%)
- D-4: -0.5244 (-71.8%)

---

## 2. Cross-Seed Comparison (r=0.2, 3 seeds)

### 2.1 Gen0 Baseline Consistency

| Metric | seed42 | seed43 | seed44 | Consistent? |
|--------|--------|--------|--------|-------------|
| SLV | 2366.68 | 2366.68 | 2366.68 | ✓ identical |
| eff_rank | 417.55 | 417.55 | 417.55 | ✓ identical |
| PPL | 9.554 | 9.554 | 9.554 | ✓ identical |
| D-4 | 0.7414 | 0.7415 | 0.7305 | ~1.5% var (stochastic generation) |

Same pretrained model, D-4 variance from stochastic text generation at eval time.

### 2.2 SLV Per-Generation (3 seeds)

| Gen | seed42 | seed43 | seed44 | Mean | Std |
|-----|--------|--------|--------|------|-----|
| 0 | 2366.68 | 2366.68 | 2366.68 | 2366.68 | 0.00 |
| 1 | 2367.46 | 2365.31 | 2369.43 | 2367.40 | 2.06 |
| 2 | **2358.31** | **2358.84** | **2361.11** | **2359.42** | **1.51** |
| 3 | 2362.52 | 2365.74 | 2365.55 | 2364.60 | 1.79 |
| 4 | 2379.19 | 2377.37 | 2377.06 | 2377.87 | 1.16 |
| 5 | 2398.93 | 2395.98 | 2395.62 | 2396.84 | 1.83 |
| 6 | 2429.83 | 2411.37 | 2411.78 | 2417.66 | 10.62 |
| 7 | 2436.35 | 2426.30 | 2424.37 | 2429.01 | 6.43 |
| 8 | 2454.30 | 2436.78 | 2436.08 | 2442.39 | 10.32 |
| 9 | 2463.14 | 2453.63 | 2451.25 | 2455.34 | 6.25 |
| 10 | 2479.70 | 2455.78 | 2466.15 | 2467.21 | 12.00 |

All 3 seeds show Type II trajectory with SLV dip at Gen2.

**SLV dip magnitude at Gen2:**
- seed42: Δ = -8.38
- seed43: Δ = -7.84
- seed44: Δ = -5.58
- Mean dip: **-7.27 ± 1.49**

### 2.3 D-4 Per-Generation (3 seeds)

| Gen | seed42 | seed43 | seed44 | Mean | Std |
|-----|--------|--------|--------|------|-----|
| 0 | 0.7414 | 0.7415 | 0.7305 | 0.7378 | 0.0063 |
| 1 | 0.6737 | 0.6842 | 0.6542 | 0.6707 | 0.0153 |
| 2 | 0.4978 | 0.4988 | 0.5619 | 0.5195 | 0.0367 |
| 3 | 0.4665 | 0.4780 | 0.4685 | 0.4710 | 0.0062 |
| 4 | 0.4515 | 0.4445 | 0.3990 | 0.4317 | 0.0286 |
| 5 | 0.4384 | 0.4435 | 0.3771 | 0.4197 | 0.0369 |
| 6 | 0.4627 | 0.4420 | 0.3330 | 0.4126 | 0.0700 |
| 7 | 0.4877 | 0.3433 | 0.3068 | 0.3793 | 0.0972 |
| 8 | 0.5015 | 0.3106 | 0.2834 | 0.3652 | 0.1189 |
| 9 | 0.5077 | 0.3060 | 0.2320 | 0.3486 | 0.1434 |
| 10 | **0.5203** | **0.2453** | **0.2061** | **0.3239** | **0.1713** |

### 2.4 Gen10 Cross-Seed Summary

| Metric | seed42 | seed43 | seed44 | Mean ± Std |
|--------|--------|--------|--------|------------|
| SLV | 2479.70 | 2455.78 | 2466.15 | **2467.21 ± 12.00** |
| eff_rank | 511.26 | 505.98 | 506.95 | **508.06 ± 2.81** |
| PPL | 13.830 | 13.399 | 13.391 | **13.540 ± 0.251** |
| D-4 | 0.5203 | 0.2453 | 0.2061 | **0.3239 ± 0.1713** |
| train_loss | 1.392 | 0.938 | 0.867 | **1.066 ± 0.289** |

---

## 3. D-4 Trajectory Pattern Analysis

### Key Question: Is seed42's D-4 V-shaped recovery a 1/3 outlier?

**Answer: Yes, seed42 is a 1/3 outlier.**

| Seed | D-4 pattern | Gen5→Gen10 | Classification |
|------|-------------|------------|----------------|
| seed42 | V-shaped recovery | 0.44 → 0.52 (+18.7%) | Recovery |
| seed43 | Monotonic decline | 0.44 → 0.25 (-44.7%) | Decline |
| seed44 | Monotonic decline | 0.38 → 0.21 (-45.3%) | Decline |

- Seeds 43 and 44 show consistent monotonic D-4 decline across all 10 generations
- seed42 uniquely shows D-4 bottoming at gen5 (0.44) then recovering to 0.52 at gen10
- This V-shaped recovery correlates with anomalous train_loss behavior in seed42 (see §4)

---

## 4. Anomaly: seed42 Train Loss Pattern

| Gen | seed42 loss | seed43 loss | seed44 loss |
|-----|-------------|-------------|-------------|
| 5 | 1.305 | 1.273 | 1.149 |
| 6 | 1.264 | 1.222 | 1.134 |
| 7 | **1.327** ↑ | 1.191 | 1.060 |
| 8 | **1.339** ↑ | 1.015 | 0.996 |
| 9 | **1.394** ↑ | 0.955 | 0.957 |
| 10 | **1.392** ↑ | 0.938 | 0.867 |

seed42 train_loss **increases** after gen6, while seeds 43 and 44 show normal monotonic decrease. This anomaly perfectly correlates with the D-4 V-recovery. Possible explanations:
1. Resume from different checkpoint or with different hyperparameters at gen6
2. Data mixing anomaly in later generations

**Recommendation:** The D-4 V-recovery in seed42 is likely an artifact of this train_loss anomaly rather than a genuine seed-dependent phenomenon. For paper reporting, use 2-seed stats (seeds 43+44) for D-4 at gen6-10, or flag seed42 as anomalous.

---

## 5. Data Discrepancy Note

The user context stated "exp_007 (seed42) only ran gen0-5." However, the results file `phase1_fixed_mix_r02_seed42_results.json` on the server contains gen0-10 data. The gen6-10 portion shows anomalous train_loss behavior (increasing rather than decreasing), suggesting it may have been from a separate/modified run appended to the original gen0-5 data. This should be verified.

---

## 6. Conclusions

1. **exp_019 trajectory: Type II confirmed** — SLV dip at Gen2 (Δ=-5.58), then monotonic recovery to 2466.15 at Gen10
2. **3-seed Type II consensus** — All 3 seeds show transient SLV dip at Gen2 (mean Δ = -7.27 ± 1.49), confirming Type II as the universal trajectory for r=0.2
3. **D-4 V-recovery is a 1/3 outlier** — Only seed42 shows it, correlated with anomalous train_loss increase. Seeds 43 and 44 both show monotonic D-4 decline
4. **SLV/eff_rank/PPL highly consistent** — At gen10, SLV std=12.00 (0.49% of mean), eff_rank std=2.81 (0.55%), PPL std=0.25 (1.9%). D-4 has high variance (std=0.17, 53% of mean) due to seed42 outlier
5. **Excluding seed42 anomaly**, 2-seed D-4 at gen10: mean=0.2257 ± 0.0277
