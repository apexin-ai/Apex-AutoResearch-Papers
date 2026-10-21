# VLA-Only Baseline & CRM obs_only Summary

Generated: 2026-05-19

## 1. VLA-Only Baselines (SmolVLA, K=1, no CRM)

### LIBERO-Object

| Seed | Overall SR | exp_id |
|------|-----------|--------|
| 42 | 0.12 | eval-vla-only-object |
| 43 | 0.12 | eval-vla-only-object-seed43 |
| 44 | 0.10 | eval-vla-only-object-seed44-r2 |
| 45 | 0.11 | eval-vla-only-object-seed45-r2 |
| 46 | 0.13 | eval-vla-only-object-seed46 |
| **Mean ± Std** | **0.116 ± 0.011** | **n=5** |

Per-task breakdown (seeds with data):

| Task | s42 | s43 | s44 | s45 |
|------|-----|-----|-----|-----|
| alphabet_soup | 0.0 | 0.0 | 0.0 | 0.0 |
| cream_cheese | 0.1 | 0.1 | 0.1 | 0.3 |
| salad_dressing | 0.2 | 0.1 | 0.2 | 0.2 |
| bbq_sauce | 0.2 | 0.3 | 0.2 | 0.2 |
| ketchup | 0.0 | 0.0 | 0.0 | 0.0 |
| tomato_sauce | 0.1 | 0.0 | 0.0 | 0.1 |
| butter | 0.0 | 0.0 | 0.0 | 0.0 |
| milk | 0.1 | 0.1 | 0.1 | 0.0 |
| chocolate_pudding | 0.2 | 0.4 | 0.2 | 0.1 |
| orange_juice | 0.3 | 0.2 | 0.2 | 0.2 |

### LIBERO-Spatial

| Seed | Overall SR | exp_id |
|------|-----------|--------|
| 42 | 0.30 | eval-vla-only-spatial-seed42 |
| 43 | 0.29 | eval-vla-only-spatial-seed43 |
| 44 | 0.31 | eval-vla-only-spatial-seed44 |
| 45 | 0.27 | eval-vla-only-spatial-seed45 |
| **Mean ± Std** | **0.292 ± 0.017** | **n=4** |

Per-task breakdown:

| Task | s42 | s43 | s44 | s45 |
|------|-----|-----|-----|-----|
| between_plate_and_ramekin | 0.6 | 0.7 | 0.6 | 0.7 |
| next_to_ramekin | 1.0 | 0.8 | 1.0 | 0.9 |
| from_table_center | 0.0 | 0.1 | 0.0 | 0.0 |
| on_cookie_box | 0.2 | 0.3 | 0.3 | 0.2 |
| in_top_drawer | 0.0 | 0.0 | 0.0 | 0.0 |
| on_ramekin | 0.0 | 0.0 | 0.0 | 0.0 |
| next_to_cookie_box | 0.9 | 0.9 | 0.9 | 0.9 |
| on_stove | 0.0 | 0.0 | 0.0 | 0.0 |
| next_to_plate | 0.3 | 0.1 | 0.3 | 0.0 |
| on_wooden_cabinet | 0.0 | 0.0 | 0.0 | 0.0 |

### LIBERO-Goal

| Seed | Overall SR | exp_id |
|------|-----------|--------|
| 42 | 0.71 | eval-vla-only-goal-seed42 |
| 43 | 0.69 | eval-vla-only-goal-seed43 |
| 44 | 0.73 | eval-vla-only-goal-seed44-r2 |
| **Mean ± Std** | **0.710 ± 0.020** | **n=3** |

Per-task breakdown:

| Task | s42 | s43 | s44 |
|------|-----|-----|-----|
| open_middle_drawer | 0.9 | 0.9 | 0.8 |
| bowl_on_stove | 0.9 | 0.9 | 0.9 |
| wine_on_cabinet | 0.6 | 0.4 | 0.4 |
| drawer_bowl_inside | 0.4 | 0.5 | 0.6 |
| bowl_on_cabinet | 0.7 | 0.5 | 0.7 |
| plate_front_stove | 0.9 | 0.8 | 0.9 |
| cream_cheese_in_bowl | 0.2 | 0.4 | 0.3 |
| turn_on_stove | 0.9 | 0.9 | 0.9 |
| bowl_on_plate | 0.9 | 1.0 | 1.0 |
| wine_on_rack | 0.7 | 0.6 | 0.8 |

### LIBERO-Long

All 5 seeds (42-46) currently **RUNNING** — no results yet.

### LTO Split-A (5 held-out tasks, not LIBERO-Long)

| Run | SR | exp_id |
|-----|-----|--------|
| r2 | 0.14 | eval-lto-splitA-vla-only-r2 |
| r3 | 0.14 | eval-lto-splitA-vla-only-r3 |
| v2 | 0.14 | eval-lto-splitA-vla-only-v2 |

Tasks: ketchup, milk, orange_juice, salad_dressing, tomato_sauce (5 tasks × 10 rollouts = 50 total, 7 successes)

### OpenVLA 7B Baseline (different model)

| Seed | Suite | SR | exp_id |
|------|-------|-----|--------|
| 42 | Object | 0.69 | eval-openvla-object-vla-only-seed42-v2 |

---

## 2. CRM obs_only Comparisons (norm=0.2)

### Object K=10

| Seed | SR | exp_id |
|------|-----|--------|
| 42 | 0.22 | eval-acr-object-obs-only-norm02 |
| 43 | 0.16 | eval-obs-only-object-norm02-seed43-r2 |
| 44 | 0.16 | eval-obs-only-object-norm02-seed44-r2 |
| 45 | 0.16 | eval-obs-only-object-norm02-seed45 |
| 46 | 0.15 | eval-obs-only-object-norm02-seed46 |
| 47 | 0.20 | eval-obs-only-object-norm02-seed47 |
| 48 | 0.18 | eval-obs-only-object-norm02-seed48-r2 |
| **Mean ± Std** | **0.176 ± 0.026** | **n=7** |

### Spatial K=10

| Seed | SR | exp_id |
|------|-----|--------|
| 44 | 0.36 | eval-obs-only-spatial-norm02-seed44 |
| 45 | 0.34 | eval-obs-only-spatial-norm02-seed45 |
| 47 | 0.32 | eval-obs-only-spatial-norm02-seed47 |
| **Mean ± Std** | **0.340 ± 0.020** | **n=3** |

### Object K=5

| Seed | SR | exp_id |
|------|-----|--------|
| 42 | 0.14 | eval-obs-only-object-norm02-k5-seed42 |
| 43 | 0.19 | eval-obs-only-object-norm02-k5-seed43 |
| 44 | 0.17 | eval-obs-only-object-norm02-k5-seed44 |
| 45 | 0.15 | eval-obs-only-object-norm02-k5-seed45 |
| 46 | 0.16 | eval-obs-only-object-norm02-k5-seed46 |
| 47 | 0.13 | eval-obs-only-object-norm02-k5-seed47 |
| 48 | 0.18 | eval-obs-only-object-norm02-k5-seed48 |
| **Mean ± Std** | **0.160 ± 0.022** | **n=7** |

### Spatial K=5

| Seed | SR | exp_id |
|------|-----|--------|
| 42 | 0.35 | eval-obs-only-spatial-norm02-k5-seed42 |
| 43 | 0.32 | eval-obs-only-spatial-norm02-k5-seed43 |
| 44 | 0.37 | eval-obs-only-spatial-norm02-k5-seed44-r2 |
| 45 | 0.34 | eval-obs-only-spatial-norm02-k5-seed45-r2 |
| **Mean ± Std** | **0.345 ± 0.021** | **n=4** |

---

## 3. Comparison Summary

| Suite | VLA-only | CRM obs_only K=10 | CRM obs_only K=5 | Δ(K=10) | Δ(K=5) |
|-------|----------|-------------------|-------------------|---------|--------|
| Object | 0.116 ± 0.011 (n=5) | 0.176 ± 0.026 (n=7) | 0.160 ± 0.022 (n=7) | +6.0pp | +4.4pp |
| Spatial | 0.292 ± 0.017 (n=4) | 0.340 ± 0.020 (n=3) | 0.345 ± 0.021 (n=4) | +4.8pp | +5.3pp |
| Goal | 0.710 ± 0.020 (n=3) | — | — | — | — |
| Long | RUNNING | — | — | — | — |
