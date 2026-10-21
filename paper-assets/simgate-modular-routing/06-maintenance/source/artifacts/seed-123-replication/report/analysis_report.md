# Seed-123 Replication Analysis Report

**Date**: 2026-05-18
**Experiment**: seed-123-replication (plan-012-full seed robustness check)
**Server**: westd-18266
**Status**: Completed successfully

## Summary

| Metric | Seed=42 (ref) | Seed=123 | Diff | Robust? |
|--------|:---:|:---:|:---:|:---:|
| **DAF (aggregate)** | 90.41% | 89.68% | -0.73pp | YES |
| **DAF (task-weighted)** | 90.41% | 89.18% | -1.23pp | YES |
| death_rate_int | 42.9% | 45.45% | +2.55pp | |
| death_rate_det | 16.3% | 20.91% | +4.61pp | |
| delta_full | 29.6 | 27.47 | -2.13 | |
| delta_nd | 2.84 | 2.83 | -0.01 | |
| pearson_r | 0.9698 | 0.9412 | -0.029 | |
| pearson_p | 8.12e-07 | 1.6e-05 | | |
| episodes | 245 | 220 | -25 | |
| tasks | 11 | 11 | 0 | |

## Conclusion: **SUCCESS**

DAF difference = 0.73pp (aggregate) / 1.23pp (task-weighted), both well within the 5pp threshold. Direction is consistent: death avoidance remains the dominant driver of routing preference in both seeds.

## Per-Task Comparison

### Label Distribution (Seed=123)

| Task | N | det-pref | int-pref | no-pref | Int_d% | Det_d% | DAF |
|------|:-:|:---:|:---:|:---:|:---:|:---:|:---:|
| chemistry-mix | 20 | 5 | 2 | 13 | 50% | 35% | 100% |
| find-animal | 20 | 6 | 1 | 13 | 45% | 25% | 81% |
| find-non-living-thing | 20 | 7 | 2 | 11 | 0% | 0% | 0% |
| freeze | 20 | 8 | 0 | 12 | 55% | 15% | 100% |
| grow-fruit | 20 | 7 | 0 | 13 | 50% | 15% | 100% |
| identify-life-stages-1 | 20 | 4 | 0 | 16 | 50% | 30% | 100% |
| identify-life-stages-2 | 20 | 7 | 0 | 13 | 50% | 15% | 100% |
| inclined-plane-determine-angle | 20 | 6 | 0 | 14 | 55% | 25% | 100% |
| lifespan-longest-lived | 20 | 5 | 0 | 15 | 50% | 25% | 100% |
| lifespan-longest-lived-then-shortest-lived | 20 | 6 | 1 | 13 | 45% | 20% | 100% |
| measure-melting-point-unknown-substance | 20 | 6 | 1 | 13 | 50% | 25% | 100% |
| **AGGREGATE** | **220** | **67** | **7** | **146** | **45.45%** | **20.91%** | **89.68%** |

### Label Distribution Proportions

| Label | Seed=42 | Seed=123 |
|-------|:---:|:---:|
| det-preferred | 35.1% (86/245) | 30.5% (67/220) |
| internal-preferred | 3.7% (9/245) | 3.2% (7/220) |
| no-preference | 61.2% (150/245) | 66.4% (146/220) |

Proportional distributions are consistent across seeds.

## Aggregate Statistics (Seed=123)

- **Delta_full** = +27.47, 95% CI [20.72, 34.42]
- **Delta_nd** = 2.83, 95% CI [0.37, 5.59]
- **Delta_death** = 54.46
- **DAF** = 89.68%, 95% CI [79.84%, 98.87%]
- **Delta_penalty_removed** = 2.93
- **Pearson r** (death_rate_diff vs delta) = 0.9412, p = 1.6e-05 (n=11 tasks)

## Signal Source Distribution (Seed=123)

| Source | Count | % |
|--------|:---:|:---:|
| death_asymmetry | 64 | 29.1% |
| both_dead | 41 | 18.6% |
| score_comparison | 10 | 4.5% |
| tied_alive | 105 | 47.7% |

## Key Observations

1. **DAF is seed-robust**: 89.68% (seed=123) vs 90.41% (seed=42), difference < 1pp
2. **Death dominance pattern replicates**: 10/11 tasks show DAF >= 81%, only find-non-living-thing (0 deaths) is the exception in both seeds
3. **Correlation replicates**: Pearson r = 0.94 (seed=123) vs 0.97 (seed=42), both highly significant
4. **delta_nd is near-identical**: 2.83 vs 2.84, confirming that non-death score gaps are minimal and stable
5. **Both seeds show same asymmetry**: internal policy dies much more often than deterministic (45% vs 21% in seed=123; 43% vs 16% in seed=42)
6. **Episode count difference** (220 vs 245) is due to seed=42 including prescreening/reuse episodes; seed=123 used only plan_c data (20 episodes per task)

## Data Paths

- Results: `/root/autodl-tmp/simgate-modular-routing/results/seed123-plan-c/`
- Decomposition: `/root/autodl-tmp/simgate-modular-routing/results/seed123_decomposition/`
- Log: `/root/autodl-tmp/simgate-modular-routing/logs/seed123-gpu0.log`
