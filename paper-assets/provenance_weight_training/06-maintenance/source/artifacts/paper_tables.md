# Paper Data Tables — Provenance Weight Training

All PPL values from registry `eval_ppl_holdout` (or `eval_ppl` where noted). Eval on held-out human data (~4.08M tokens).

---

## Table 1: Grid-b Baseline (PPL vs b)

| b | seed42 | seed123 | seed456 | Mean | Std |
|---:|-------:|--------:|--------:|-----:|----:|
| 0.5 | 17.651 | 17.638 | 17.650 | 17.646 | 0.007 |
| 1.0 | 17.692 | 17.674 | 17.680 | 17.682 | 0.009 |
| 1.5 | 17.718 | 17.701 | 17.710 | 17.710 | 0.009 |
| 2.0 | 17.741 | 17.725 | 17.989† | 17.733 | 0.011 |
| 3.0 | 17.774 | 17.760 | 17.921† | 17.767 | 0.010 |
| 5.0 | 17.818 | 17.804 | 17.993† | 17.811 | 0.010 |

† Checkpoint resume artifact (training interrupted, resumed from checkpoint). PPL systematically inflated. Mean/std computed from seed42 + seed123 only.

---

## Table 2: Method Comparison

| Method | seed42 | seed123 | seed456 | Mean | Std |
|--------|-------:|--------:|--------:|-----:|----:|
| Uniform (no provenance) | 17.690 | 17.690 | 17.700 | 17.693 | 0.006 |
| Grid-best (b=0.5) | 17.651 | 17.638 | 17.650 | 17.646 | 0.007 |
| Adaptive (n_min=3, old) | 17.690 | 17.630 | 17.640 | 17.653 | 0.032 |
| Adaptive-fix (n_min=2) | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 |
| Golden Ratio oracle | 17.654 | — | — | 17.654 | — |
| ESS-only (max-intervention) | 17.730 | — | — | 17.730 | — |
| n_min=1 (ESS constraint off) | 17.789 | — | — | 17.789 | — |

Notes:
- Adaptive (old) high std (0.032) due to seed42 outlier at 17.69 (= uniform); n_min=3 bug caused under-weighting for that seed.
- Adaptive-fix resolves this: all 3 seeds consistently beat uniform by 0.03–0.06 PPL.
- Golden Ratio oracle requires known contamination labels (impractical). Adaptive-fix achieves comparable PPL (17.651 vs 17.654) without oracle access.
- ESS-only uses eval_ppl (not eval_ppl_holdout) from registry.

---

## Table 3: τ Sensitivity (seed42)

| τ | PPL | Δ vs τ=0.8 |
|---:|------:|------:|
| 0.5 | — | pending |
| 0.6 | 17.681 | +0.031 |
| 0.7 | — | pending |
| 0.8 | 17.650 | 0.000 |
| 0.9 | — | pending |
| 0.95 | — | pending |

Notes:
- τ=0.8 baseline from adaptive_fix_seed42.
- τ=0.6 from tau_06_seed42 (conclusion=negative; more aggressive α_eff cap degraded PPL by +0.031).
- Remaining τ values pending experiments.

---

*Generated 2026-05-15 from experiment registry. All experiments: Qwen3-0.6B, 200M tokens, batch_size=4, grad_accum=4, lr=5e-5, contamination_ratio=0.4.*
