# Full Experiment Data — Provenance Weight Training

All values sourced from project registry (`provenance_weight_training`). Generated 2026-05-15.

**Setup**: Qwen3-0.6B, 200M train tokens (371K samples, 40% synthetic contamination), eval on held-out human data (4.08M tokens), 6103 training steps per run.

---

## Table A: Grid-b Sweep (eval_ppl_holdout)

| b | seed42 | seed123 | seed456 | Mean ± Std | Valid Seeds |
|-----|--------|---------|---------|------------|-------------|
| 0.5 | 17.651 | 17.638 | 17.650 | 17.646 ± 0.007 | 3 |
| 1.0 | 17.692 | 17.674 | 17.680 | 17.682 ± 0.009 | 3 |
| 1.5 | 17.718 | 17.701 | 17.710 | 17.710 ± 0.009 | 3 |
| 2.0 | 17.741 | 17.725 | 17.989† | 17.733 ± 0.011 | 2\* |
| 3.0 | 17.774 | 17.760 | 17.921† | 17.767 ± 0.010 | 2\* |
| 5.0 | 17.818 | 17.804 | 17.993† | 17.811 ± 0.010 | 2\* |

†INVALIDATED: seed456 b∈{2.0, 3.0, 5.0} training was interrupted and resumed from checkpoint (D026), causing systematic PPL inflation of +0.15 to +0.25. These values are excluded from Mean/Std.

\*Mean/Std computed from seed42 + seed123 only.

**Observations**:
- PPL increases monotonically with b (best b = 0.5)
- Effect is consistent across all seeds
- Std is small (0.007–0.011), confirming reproducibility

---

## Table B: Method Comparison (eval_ppl_holdout)

| Method | seed42 | seed123 | seed456 | Mean | Std |
|-------------------|--------|---------|---------|-------|-------|
| Uniform (w=1) | 17.690 | 17.690 | 17.700 | 17.693 | 0.006 |
| Grid-best (b=0.5) | 17.651 | 17.638 | 17.650 | 17.646 | 0.007 |
| Adaptive_fix (τ=0.8) | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 |

### Improvement Analysis

| Metric | seed42 | seed123 | seed456 | Mean |
|-----------------------------|---------|---------|---------|---------|
| Δ(adaptive vs uniform) | 0.040 | 0.047 | 0.040 | 0.042 |
| Δ(grid-best vs uniform) | 0.039 | 0.052 | 0.050 | 0.047 |
| Per-seed ratio (Δ_a/Δ_g %) | 102.6% | 90.4% | 80.0% | 91.0% |

### Ratio-of-Means (论文口径)

$$\text{ratio-of-means} = \frac{\bar{PPL}_{\text{adaptive}} - \bar{PPL}_{\text{uniform}}}{\bar{PPL}_{\text{grid}} - \bar{PPL}_{\text{uniform}}} = \frac{17.651 - 17.693}{17.646 - 17.693} = \frac{-0.042}{-0.047} = 89.4\%$$

Adaptive_fix recovers **89.4%** of grid-best improvement without grid search (ratio-of-means). Mean-of-ratios = 91.0% — reported for reference but not used as paper headline.

---

## Table C: b\* Distribution Statistics (from adaptive_fix, τ=0.8)

| Statistic | seed42 | seed123 | seed456 | Mean | CV |
|---------------|--------|---------|---------|-------|------|
| b\* Mean | 1.399 | 1.431 | 1.416 | 1.415 | 1.1% |
| b\* Median | 0.871 | 0.880 | 0.880 | 0.877 | 0.6% |
| b\* Std | 1.933 | 2.029 | 1.993 | 1.985 | 2.4% |
| b\* P25 | 0.540 | 0.540 | 0.540 | 0.540 | 0.0% |
| b\* P75 | 1.512 | 1.520 | 1.520 | 1.517 | 0.3% |
| % below 0.5 | 20.9% | 20.9% | 20.9% | 20.9% | 0.0% |
| % above 2.0 | 16.1% | 16.1% | 16.1% | 16.1% | 0.0% |

**Observations**:
- b\* distribution is highly stable across seeds (CV < 2.5% for all statistics)
- Median b\* ≈ 0.88, reflecting moderate downweighting for most batches
- Right-skewed: mean (1.415) > median (0.877), driven by ~16% of batches with b\* > 2.0
- ~21% of batches receive strong downweighting (b\* < 0.5)

---

## Table D: Complete Experiment Index

### D.1 — DONE experiments (26 total)

| exp_id | type | seed | b / τ | eval_ppl | status | conclusion |
|-------------------------------|---------------|------|------------|----------|--------|-------------------------------------|
| grid_b_seed42_batch | grid_b_sweep | 42 | b=0.5–5.0 | 17.651\* | DONE | success (\*best_b=0.5) |
| grid_b0_5_seed123 | grid_b_sweep | 123 | b=0.5 | 17.638 | DONE | success |
| grid_b1_0_seed123 | grid_b_sweep | 123 | b=1.0 | 17.674 | DONE | success |
| grid_b1_5_seed123 | grid_b_sweep | 123 | b=1.5 | 17.701 | DONE | success |
| grid_b2_0_seed123 | grid_b_sweep | 123 | b=2.0 | 17.725 | DONE | success |
| grid_b3_0_seed123 | grid_b_sweep | 123 | b=3.0 | 17.760 | DONE | success |
| grid_b5_0_seed123 | grid_b_sweep | 123 | b=5.0 | 17.804 | DONE | success |
| grid_b0_5_seed456 | grid_b_sweep | 456 | b=0.5 | 17.650 | DONE | success |
| grid_b1_0_seed456 | grid_b_sweep | 456 | b=1.0 | 17.680 | DONE | success |
| grid_b1_5_seed456 | grid_b_sweep | 456 | b=1.5 | 17.710 | DONE | success |
| grid_b2_0_seed456 | grid_b_sweep | 456 | b=2.0 | 17.989 | DONE | INVALIDATED (D026 checkpoint resume) |
| grid_b3_0_seed456 | grid_b_sweep | 456 | b=3.0 | 17.921 | DONE | INVALIDATED (D026 checkpoint resume) |
| grid_b5_0_seed456 | grid_b_sweep | 456 | b=5.0 | 17.993 | DONE | INVALIDATED (D026 checkpoint resume) |
| grid_b_low_seed42 | grid_b_low | 42 | b=0.1/0.2/0.3 | — | DONE | failed (infra: cron killed process) |
| uniform_seed42 | uniform | 42 | — | 17.690 | DONE | success |
| uniform_seed123 | uniform | 123 | — | 17.690 | DONE | success |
| uniform_seed456 | uniform | 456 | — | 17.700 | DONE | success |
| adaptive_seed42 | adaptive | 42 | τ=0.8 | 17.690 | DONE | success (n_min=3 bug, superseded) |
| adaptive_seed123 | adaptive | 123 | τ=0.8 | 17.630 | DONE | success (n_min=3 bug, superseded) |
| adaptive_seed456 | adaptive | 456 | τ=0.8 | 17.640 | DONE | success (n_min=3 bug, superseded) |
| adaptive_fix_seed42 | adaptive_fix | 42 | τ=0.8 | 17.650 | DONE | success |
| adaptive_fix_seed123 | adaptive_fix | 123 | τ=0.8 | 17.643 | DONE | success |
| adaptive_fix_seed456 | adaptive_fix | 456 | τ=0.8 | 17.660 | DONE | success |
| datagen_synthetic_4gpu | datagen | — | — | — | DONE | success (340992 docs, 132M tokens) |
| detector_tfidf_lr | detector | — | — | — | DONE | success (AUC=0.939, ECE_cal=0.048) |
| diagnostic_contamination100 | diagnostic | — | — | — | DONE | killed (freed GPU for grid-b seed123) |

### D.2 — RUNNING experiments (4 total)

| exp_id | type | seed | params | status |
|---------------------|-------------------|------|--------------|---------|
| ess_only_seed42 | ess_only_baseline | 42 | n_min=2 | RUNNING |
| golden_ratio_seed42 | golden_ratio | 42 | w=1/φ oracle | RUNNING |
| nmin1_seed42 | n_min_sensitivity | 42 | n_min=1, τ=0.8 | RUNNING |
| tau_06_seed42 | tau_sweep | 42 | τ=0.6 | RUNNING |

### D.3 — PREPARING / QUEUED experiments (9 total)

| exp_id | type | seed | params | status | conclusion |
|-----------------------|-----------|------|--------|-----------|------------|
| adaptive_v2_seed42 | adaptive_v2 | 42 | — | PREPARING | killed |
| adaptive_v2_seed123 | adaptive_v2 | 123 | — | PREPARING | killed |
| adaptive_v2_seed456 | adaptive_v2 | 456 | — | PREPARING | killed |
| tau_0.6_seed42 | tau_sweep | 42 | τ=0.6 | QUEUED | killed (replaced by tau_06_seed42) |
| detector_modernbert | detector | — | — | QUEUED | success (superseded by TF-IDF) |
| tau_05_seed42 | tau_sweep | 42 | τ=0.5 | PREPARING | — |
| tau_07_seed42 | tau_sweep | 42 | τ=0.7 | PREPARING | — |
| tau_09_seed42 | tau_sweep | 42 | τ=0.9 | PREPARING | — |
| tau_095_seed42 | tau_sweep | 42 | τ=0.95 | PREPARING | — |

---

## Summary

| Category | Total | Success | Invalidated | Failed | Killed | Running/Pending |
|------------------|-------|---------|-------------|--------|--------|-----------------|
| grid_b_sweep | 20 | 15 | 3 | 1 | 0 | 0+1\*\* |
| uniform | 3 | 3 | 0 | 0 | 0 | 0 |
| adaptive (orig) | 3 | 3 | 0 | 0 | 0 | 0 |
| adaptive_v2 | 3 | 0 | 0 | 0 | 3 | 0 |
| adaptive_fix | 3 | 3 | 0 | 0 | 0 | 0 |
| tau_sweep | 6 | 0 | 0 | 0 | 1 | 1+4 |
| n_min_sensitivity | 1 | 0 | 0 | 0 | 0 | 1 |
| ess_only | 1 | 0 | 0 | 0 | 0 | 1 |
| golden_ratio | 1 | 0 | 0 | 0 | 0 | 1 |
| datagen | 1 | 1 | 0 | 0 | 0 | 0 |
| detector | 2 | 2 | 0 | 0 | 0 | 0 |
| diagnostic | 1 | 0 | 0 | 0 | 1 | 0 |
| **Total** | **39** | **24\*** | **3** | **1** | **5** | **4+5** |

\*\*grid_b_low_seed42 = failed (infra bug, not re-run).
\*24 DONE with conclusion=success (includes 3 invalidated experiments which completed but have unreliable metrics).
