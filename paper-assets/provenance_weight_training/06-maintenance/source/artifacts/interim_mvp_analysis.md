# Interim MVP Analysis — Provenance Weight Training

**Date**: 2026-05-14  
**Status**: Interim (grid-b sweep incomplete)

---

## 1. Completed Experiment Results (from registry)

### Uniform Baseline (3 seeds)

| Experiment | Seed | eval_ppl_holdout | eval_loss | train_loss | gpu_hours |
|---|---|---|---|---|---|
| uniform_seed42 | 42 | 17.69 | — | 7.310 | 3.43 |
| uniform_seed123 | 123 | 17.69 | — | 7.312 | 3.43 |
| uniform_seed456 | 456 | 17.70 | — | 7.290 | 3.43 |

**Mean ± Std**: 17.693 ± 0.006

### Adaptive b* (3 seeds)

| Experiment | Seed | eval_ppl_holdout | eval_loss | train_loss | b* range | alpha_eff range | gpu_hours |
|---|---|---|---|---|---|---|---|
| adaptive_seed42 | 42 | 17.69 | — | 9.267 | 0.0–3.8 | 0.03–0.80 | 4.21 |
| adaptive_seed123 | 123 | 17.63 | — | 9.267 | 0.0–3.8 | 0.04–0.80 | 4.21 |
| adaptive_seed456 | 456 | 17.64 | — | 9.235 | 0.0–3.8 | 0.09–0.80 | 4.21 |

**Mean ± Std**: 17.653 ± 0.032

### Grid-b (completed runs only)

| Experiment | Seed | b | eval_ppl_holdout | eval_loss | train_loss | gpu_hours |
|---|---|---|---|---|---|---|
| grid_b0_5_seed123 | 123 | 0.5 | 17.638 | 2.870 | 9.601 | 3.80 |
| grid_b1_0_seed123 | 123 | 1.0 | 17.674 | 2.872 | 10.218 | 3.88 |
| grid_b_seed42_batch | 42 | 0.5 | 17.651 | — | — | — |
| grid_b_seed42_batch | 42 | 1.0 | 17.692 | — | — | — |

### Grid-b (still running)

| Experiment | Seed | b | Status |
|---|---|---|---|
| grid_b1_5_seed123 | 123 | 1.5 | RUNNING |
| grid_b2_0_seed123 | 123 | 2.0 | RUNNING |
| grid_b3_0_seed123 | 123 | 3.0 | RUNNING |
| grid_b_seed42_batch | 42 | 1.5–5.0 | RUNNING (serial) |

---

## 2. Adaptive vs Uniform

| Metric | Uniform | Adaptive | Δ | Δ% |
|---|---|---|---|---|
| Mean PPL | 17.693 | 17.653 | −0.040 | −0.23% |
| Std PPL | 0.006 | 0.032 | — | — |

**Adaptive reduces held-out PPL by 0.040 points (0.23%) on average relative to uniform.**

Per-seed breakdown:
- seed42: adaptive 17.69 vs uniform 17.69 → **no improvement** (0.00)
- seed123: adaptive 17.63 vs uniform 17.69 → **−0.06** (−0.34%)
- seed456: adaptive 17.64 vs uniform 17.70 → **−0.06** (−0.34%)

Observation: seed42 is an outlier where adaptive shows no gain. Seeds 123 and 456 both show a consistent −0.06 improvement. The higher variance of adaptive (std=0.032 vs 0.006) is largely driven by seed42.

---

## 3. Grid-b Trend (preliminary)

For seed123 (2 b-values completed):
- b=0.5: **17.638** (best so far)
- b=1.0: 17.674

For seed42 (2 b-values completed):
- b=0.5: **17.651** (best so far)
- b=1.0: 17.692

**Trend**: Lower b yields lower PPL. b=0.5 outperforms b=1.0 for both seeds. Remaining b-values (1.5, 2.0, 3.0, 5.0) are expected to yield higher PPL if this monotonic trend continues, meaning b=0.5 may be the grid-search optimum.

Cross-seed b=0.5 mean (2 seeds): (17.638 + 17.651) / 2 = **17.645**

---

## 4. MVP Criterion Assessment (TENTATIVE)

**Criterion**: adaptive b* mean PPL improvement ≥ 90% of grid-search best-b PPL improvement (both relative to uniform).

### Using available data

| Quantity | Value | Notes |
|---|---|---|
| Uniform mean PPL | 17.693 | 3 seeds |
| Adaptive mean PPL | 17.653 | 3 seeds |
| Grid-best PPL (b=0.5, seed123) | 17.638 | Best single completed run |
| Grid-best mean PPL (b=0.5, 2 seeds) | 17.645 | seed42+seed123 only |

**Using grid-best mean (b=0.5, 2 seeds available):**
- Grid improvement over uniform: 17.693 − 17.645 = 0.048
- Adaptive improvement over uniform: 17.693 − 17.653 = 0.040
- **Capture ratio: 0.040 / 0.048 = 83.3%** → below 90% threshold

**Per-seed comparison (seed123 only, both methods complete):**
- Grid b=0.5: 17.638, Adaptive: 17.63 → adaptive is *better* by 0.008
- Capture ratio: >100%

**Per-seed comparison (seed42 only):**
- Grid b=0.5: 17.651, Adaptive: 17.69 → adaptive is *worse* by 0.039
- Uniform: 17.69 → adaptive captures 0% of grid improvement

### Preliminary verdict: **INCONCLUSIVE — leaning toward marginal FAIL**

- The mean-level capture ratio (83.3%) is below the 90% threshold, but this is based on only 2 grid-b seeds.
- High seed variance in adaptive (seed42 anomaly) is the main issue.
- For seed123, adaptive actually outperforms the best grid-b point — the method works well.
- For seed42, adaptive provides zero benefit over uniform — the method fails entirely.

---

## 5. Key Observations

1. **The effect size is small.** The entire range of PPL variation across all methods and seeds is ~17.63–17.70, a span of only 0.07 (0.4%). At this scale, seed variance is a significant fraction of the signal.

2. **Uniform is remarkably stable** (std=0.006), while adaptive has 5× higher variance (std=0.032). This suggests the adaptive mechanism introduces stochasticity that doesn't always help.

3. **Seed42 is problematic for adaptive.** Adaptive_seed42 exactly matches uniform_seed42 (17.69), suggesting the adaptive weighting had effectively no impact for this random seed. Investigation into why (e.g., batch composition, α_eff dynamics) may be warranted.

4. **Grid-b b=0.5 is consistently the best fixed-b value** across both seeds tested. If this holds, it suggests the optimal weighting is *mild* down-weighting of low-provenance data, and b=0.5 may be close to the grid optimum.

5. **Adaptive's b* range (0.0–3.8)** is much wider than the apparent optimal fixed b (~0.5). The adaptive method may be over-weighting in some batches, which could explain the inconsistency.

---

## 6. What Changes When Grid-b Completes

- If b=0.5 remains optimal (likely given the trend), the current numbers are near-final.
- If a higher b (e.g., 1.5) turns out optimal for some seeds, it would reduce the grid-best improvement and increase the adaptive capture ratio.
- Grid-b seed456 is not yet scheduled — needed for a fair 3-seed comparison.
- **Minimum data still needed**: grid-b b=0.5 for seed456, to compute a proper 3-seed grid-best mean.

---

## 7. Summary Table

| Method | Mean PPL (↓ better) | Std | Seeds | Δ vs Uniform |
|---|---|---|---|---|
| Uniform | 17.693 | 0.006 | 3 | — |
| Adaptive b* | 17.653 | 0.032 | 3 | −0.040 (−0.23%) |
| Grid b=0.5 | 17.645 | 0.009 | 2 | −0.048 (−0.27%) |
| Grid b=1.0 | 17.683 | 0.013 | 2 | −0.010 (−0.06%) |

**Adaptive captures ~83% of grid-best improvement (tentative, grid incomplete).**

---

*This is an interim analysis. Final MVP verdict requires completed grid-b sweep (all 6 b-values × at least 2 seeds, ideally 3).*
