# Paper Tables Data — EMNLP 2026 Submission
# Dual-Constrained Adaptive b* Provenance Weighting
# Model: Qwen3-0.6B continued pretraining
# Baseline PPL (pretrained, no training): 22.97
# Generated: 2026-05-16

---

## Table 1: Main Results (ρ=0.4, 3 seeds)

| Method | seed42 | seed123 | seed456 | Mean | Std |
|--------|--------|---------|---------|------|-----|
| Uniform | 17.694 | 17.686 | 17.701 | 17.694 | 0.008 |
| Grid-*b*=0.5 (best fixed-*b*) | 17.651 | 17.638 | 17.650 | 17.646 | 0.007 |
| Adaptive (ours) | 17.653 | 17.643 | 17.657 | 17.651 | 0.007 |
| ESS-only | 17.730 | 17.720 | 17.719 | 17.723 | 0.006 |
| Golden-ratio oracle | 17.654 | — | — | 17.654 | — |

**Data sources:**
- uniform: `uniform_seed42`, `uniform_seed123`, `uniform_seed456`
- grid-b=0.5: `grid_b_seed42_batch` (b=0.5 entry), `grid_b0_5_seed123`, `grid_b0_5_seed456`
- adaptive: `adaptive_fix_seed42`, `adaptive_fix_seed123`, `adaptive_fix_seed456`
- ess_only: `ess_only_seed42`, `ess_only_seed123`, `ess_only_seed456`
- golden_ratio: `golden_ratio_seed42`

**Metric:** eval_ppl_holdout (sliding-window PPL on human holdout set). Std = sample standard deviation (ddof=1).

---

## Table 2: Grid-*b* Sweep (ρ=0.4)

| *b* | seed42 | seed123 | seed456 | Mean±Std (2 seeds) |
|-----|--------|---------|---------|---------------------|
| 0.5 | 17.651 | 17.638 | 17.650 | 17.645±0.009 |
| 1.0 | 17.692 | 17.674 | 17.680 | 17.683±0.013 |
| 1.5 | 17.718 | 17.701 | 17.710 | 17.709±0.012 |
| 2.0 | 17.741 | 17.725 | 17.989† | 17.733±0.011 |
| 3.0 | 17.774 | 17.760 | 17.921† | 17.767±0.010 |
| 5.0 | 17.818 | 17.804 | 17.993† | 17.811±0.010 |

**Data sources:**
- seed42: `grid_b_seed42_batch` (keys: b0_5_eval_ppl through b5_0_eval_ppl)
- seed123: `grid_b1_0_seed123`, `grid_b1_5_seed123`, `grid_b2_0_seed123`, `grid_b3_0_seed123`, `grid_b5_0_seed123`
- seed456: `grid_b1_0_seed456`, `grid_b1_5_seed456`, `grid_b2_0_seed456`, `grid_b3_0_seed456`, `grid_b5_0_seed456`

† seed456 *b*≥2.0 PPL inflated due to checkpoint resume artifact. Mean±Std column reports seed42+seed123 only.

---

## Table 3: τ Sweep (seed42, ρ=0.4)

| τ | eval_ppl_holdout | exp_id |
|---|------------------|--------|
| 0.50 | 17.688 | tau_05_seed42 |
| 0.60 | 17.680 | tau_06_seed42 |
| 0.70 | 17.679 | tau_07_seed42 |
| **0.80** | **17.653** | adaptive_fix_seed42 |
| 0.90 | 17.712 | tau_09_seed42 |
| 0.95 | 17.723 | tau_095_seed42 |

τ=0.8 is the default used in all main experiments (adaptive_fix). Best performance at τ=0.8.

---

## Table 4: n_min Sensitivity (seed42, ρ=0.4)

| n_min | eval_ppl_holdout | exp_id |
|-------|------------------|--------|
| 1 | 17.789 | nmin1_seed42 |
| 2 | 17.653 | adaptive_fix_seed42 |
| **3** | **17.644** | adaptive_seed42 |
| 4 | 17.695 | nmin4_seed42 |

n_min=3 yields the best PPL. n_min=4 forces b*→0 (all weights equal, degenerates to uniform). n_min=1 allows high-variance b* values (mean b*=7.197), hurting stability.

---

## Table Notes

1. **Baseline PPL**: 22.97 (pretrained Qwen3-0.6B, no continued pretraining). All methods reduce PPL by ~23%.

2. **seed456 grid-*b* anomaly**: For *b*≥2.0, seed456 runs show inflated PPL (17.921–17.993) due to a checkpoint resume artifact. The paper reports Mean±Std over 2 seeds (seed42 + seed123) for *b*≥2.0 in Table 2, and notes this in a footnote.

3. **Metric source**: All values are `eval_ppl_holdout` except `ess_only` which uses `eval_ppl` (same holdout set, same metric computation, different key name in logging).

4. **Standard deviation**: Sample std (ddof=1) computed across 3 seeds (or 2 seeds where noted).

5. **Adaptive vs. Grid-*b*=0.5**: Adaptive (17.651±0.007) and grid-*b*=0.5 (17.646±0.007) achieve comparable PPL, but adaptive requires no *b* tuning — it discovers *b** automatically. The golden-ratio oracle (17.654) confirms the adaptive solution is near-optimal.

6. **ESS-only**: Pure ESS-based weighting (no provenance signal) underperforms even uniform mixing, confirming that the provenance constraint is the key component.
