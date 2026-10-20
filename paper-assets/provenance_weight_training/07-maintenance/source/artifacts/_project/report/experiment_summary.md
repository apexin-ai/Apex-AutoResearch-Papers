# Experiment Summary: Provenance Weight Training

All data sourced from project registry (`provenance_weight_training`). Generated 2026-05-15.

**Setup**: Qwen3-0.6B, 200M tokens, 371K samples (40% synthetic contamination), eval on held-out human data (4.08M tokens).

---

## Table 1: Grid-b Sweep (eval_ppl_holdout)

| b | seed42 | seed123 | seed456 | Mean | Std |
|-----|--------|---------|---------|-------|-------|
| 0.5 | 17.651 | 17.638 | 17.650 | 17.646 | 0.007 |
| 1.0 | 17.692 | 17.674 | 17.680 | 17.682 | 0.009 |
| 1.5 | 17.718 | 17.701 | 17.710 | 17.710 | 0.009 |
| 2.0 | 17.741 | 17.725 | *RUNNING* | 17.733 | 0.011 |
| 3.0 | 17.774 | 17.760 | *RUNNING* | 17.767 | 0.010 |
| 5.0 | 17.818 | 17.804 | *RUNNING* | 17.811 | 0.010 |

- Best b = 0.5 across all seeds (monotonically increasing PPL with b)
- seed456 b={2.0, 3.0, 5.0} still running; Mean/Std for those rows computed from 2 seeds only

---

## Table 2: Method Comparison (eval_ppl_holdout)

| Method | seed42 | seed123 | seed456 | Mean | Std |
|------------------|--------|---------|---------|-------|-------|
| Uniform | 17.690 | 17.690 | 17.700 | 17.693 | 0.006 |
| Grid-best (b=0.5)| 17.651 | 17.638 | 17.650 | 17.646 | 0.007 |
| Adaptive_fix | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 |

- Both grid-best and adaptive_fix improve over uniform baseline
- Adaptive_fix is within 0.005 PPL of grid-best without requiring grid search

---

## Table 3: Improvement Analysis

| Metric | seed42 | seed123 | seed456 | Mean |
|-------------------------------|---------|---------|---------|---------|
| Uniform PPL | 17.690 | 17.690 | 17.700 | 17.693 |
| Adaptive_fix PPL | 17.650 | 17.643 | 17.660 | 17.651 |
| Grid-best PPL | 17.651 | 17.638 | 17.650 | 17.646 |
| Δ(adaptive_fix vs uniform) | 0.0400 | 0.0470 | 0.0400 | 0.0423 |
| Δ(grid-best vs uniform) | 0.0390 | 0.0520 | 0.0500 | 0.0470 |
| Ratio (Δ_adaptive/Δ_grid %) | 102.6% | 90.4% | 80.0% | 91.0% |

- Adaptive_fix recovers 91.0% of grid-best improvement on average (no grid search needed)
- seed42: adaptive_fix slightly outperforms grid-best (ratio > 100%)
- seed123/456: grid-best has edge, but adaptive_fix is within 0.01 PPL

---

## Table 4: b* Distribution Statistics (from adaptive_fix)

| Statistic | seed42 | seed123 | seed456 | Mean | CV |
|---------------|--------|---------|---------|-------|------|
| b* Mean | 1.399 | 1.431 | 1.416 | 1.415 | 1.1% |
| b* Median | 0.871 | 0.880 | 0.880 | 0.877 | 0.6% |
| b* Std | 1.933 | 2.029 | 1.993 | 1.985 | 2.4% |
| b* P25 | 0.540 | 0.540 | 0.540 | 0.540 | 0.0% |
| b* P75 | 1.512 | 1.520 | 1.520 | 1.517 | 0.3% |
| % below 0.5 | 20.9% | 20.9% | 20.9% | 20.9% | 0.0% |

- b* distribution is highly stable across seeds (CV < 2.5% for all statistics)
- Median b* ≈ 0.88, close to grid-best b=0.5 but allowing batch-level adaptation
- ~21% of batches get b* < 0.5 (strong downweighting), ~16% get b* > 2.0

---

## Source Experiment IDs

| Experiment ID | Status | conclusion |
|------------------------|---------|-----------|
| grid_b_seed42_batch | DONE | success |
| grid_b0_5_seed123 | DONE | success |
| grid_b1_0_seed123 | DONE | success |
| grid_b1_5_seed123 | DONE | success |
| grid_b2_0_seed123 | DONE | success |
| grid_b3_0_seed123 | DONE | success |
| grid_b5_0_seed123 | DONE | success |
| grid_b0_5_seed456 | DONE | success |
| grid_b1_0_seed456 | DONE | success |
| grid_b1_5_seed456 | DONE | success |
| grid_b2_0_seed456 | RUNNING | — |
| grid_b3_0_seed456 | RUNNING | — |
| grid_b5_0_seed456 | RUNNING | — |
| uniform_seed42 | DONE | success |
| uniform_seed123 | DONE | success |
| uniform_seed456 | DONE | success |
| adaptive_fix_seed42 | DONE | success |
| adaptive_fix_seed123 | DONE | success |
| adaptive_fix_seed456 | DONE | success |
