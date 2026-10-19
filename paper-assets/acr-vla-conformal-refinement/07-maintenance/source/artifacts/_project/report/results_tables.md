# ACR-VLA Experiment Results Tables

> Generated: 2026-05-15 | All numbers from registry. Percentages = success rate (%).

---

## Table 1: Object Benchmark 6-way Comparison (seed=42, all FINAL 10/10 tasks)

| Method | Exp ID | **Overall SR** | alphabet_soup | cream_cheese | salad_dressing | bbq_sauce | ketchup | tomato_sauce | butter | milk | chocolate_pudding | orange_juice |
|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **obs_only (norm=0.1)** | `eval-acr-object-v4-obs-only` | **19%** | 0 | 10 | 20 | 40 | 10 | 0 | 10 | 20 | 50 | 30 |
| argmin (K=10) | `eval-reconvla-object` | **12%** | 0 | 0 | 10 | 30 | 0 | 0 | 10 | 10 | 30 | 30 |
| VLA-only (K=1) | `eval-vla-only-object` | **12%** | 0 | 10 | 20 | 20 | 0 | 10 | 0 | 10 | 20 | 30 |
| VLA-mean (K=10) | `eval-vla-mean-object` | **12%** | 0 | 0 | 10 | 30 | 10 | 10 | 0 | 20 | 30 | 10 |
| perdof (norm=0.1) | `eval-acr-object-v4-perdof` | **11%** | 0 | 0 | 20 | 30 | 0 | 0 | 10 | 0 | 20 | 30 |
| scalar (norm=0.1) | `eval-acr-object-v4-scalar` | **9%** | 0 | 0 | 10 | 10 | 0 | 0 | 10 | 10 | 30 | 20 |

**Key findings:**
- obs_only leads by +7pp over all baselines
- All methods cluster on chocolate_pudding and bbq_sauce (easiest tasks)
- alphabet_soup is universally 0% across all methods

---

## Table 2: Spatial Benchmark 6-way Comparison (seed=42, all FINAL 10/10 tasks)

Task abbreviations: T0=between_plate_and_ramekin, T1=next_to_ramekin, T2=from_table_center, T3=on_cookie_box, T4=in_top_drawer, T5=on_ramekin, T6=next_to_cookie_box, T7=on_stove, T8=next_to_plate, T9=on_wooden_cabinet

| Method | Exp ID | **Overall SR** | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **obs_only (norm=0.1)** | `eval-acr-spatial-v4-obs-only-r3` | **35%** | 90 | 100 | 0 | 40 | 10 | 0 | 90 | 0 | 20 | 0 |
| **perdof (norm=0.1)** | `eval-acr-spatial-v4-small-r2` | **35%** | 60 | 100 | 10 | 40 | 0 | 0 | 90 | 10 | 40 | 0 |
| argmin (K=10) | `eval-argmin-only-spatial-r2` | **34%** | 60 | 100 | 0 | 30 | 10 | 10 | 90 | 0 | 30 | 10 |
| scalar (norm=0.1) | `eval-acr-spatial-v4-scalar-r2` | **32%** | 60 | 100 | 10 | 40 | 0 | 0 | 90 | 0 | 10 | 10 |
| VLA-mean (K=10) | `eval-vla-mean-spatial` | **32%** | 70 | 100 | 0 | 30 | 0 | 0 | 80 | 0 | 30 | 10 |
| VLA-only (K=1) | `eval-spatial-v7-full` | **30%** | 60 | 100 | 0 | 20 | 0 | 0 | 90 | 0 | 30 | 0 |

**Key findings:**
- CRM methods (obs_only, perdof) lead by +1pp over argmin, +5pp over VLA-only
- T1 (next_to_ramekin) is saturated at 100% for all methods
- T2 (from_table_center), T5 (on_ramekin), T7 (on_stove), T9 (on_wooden_cabinet) are near-zero for all methods

---

## Table 3: Magnitude Sweep — Spatial Benchmark (perdof vs obs_only, seed=42)

| norm | perdof SR | perdof exp_id | obs_only SR | obs_only exp_id | gap (obs−perdof) |
|:----:|:---------:|---------------|:-----------:|-----------------|:----------------:|
| 0.03 | 30% | `eval-mag-perdof-norm003` | **7/10 partial** ¹ | `eval-mag-obsonly-norm003-b2` | — |
| 0.05 | 31% | `eval-mag-perdof-norm005` | 35% | `eval-mag-obsonly-norm005` | +4pp |
| 0.1 | 35% | `eval-acr-spatial-v4-small-r2` | 35% | `eval-acr-spatial-v4-obs-only-r3` | 0pp |
| 0.2 | **6/10 partial** ² | `eval-mag-perdof-norm02` | 35% | `eval-mag-obsonly-norm02` | — |
| 0.3 | 26% | `eval-mag-perdof-norm03` | 36% | `eval-mag-obsonly-norm03-r2` | +10pp |

¹ obs_only norm=0.03 (`eval-mag-obsonly-norm003-b2`): RUNNING, 7/10 tasks done. Partial per-task:
  T0=90, T1=100, T2=0, T3=30, T4=10, T5=0, T6=80. Running avg (7-task) ≈ 44%.

² perdof norm=0.2 (`eval-mag-perdof-norm02`): killed (SIGTERM), 6/10 tasks partial:
  T0=60, T1=90, T2=0, T3=20, T4=0, T5=0. Running avg (6-task) ≈ 28%.

### Per-task breakdown — Completed magnitude experiments

**perdof per-task (spatial):**

| norm | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
|:----:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0.03 | 60 | 100 | 0 | 30 | 10 | 0 | 80 | 0 | 20 | 0 |
| 0.05 | 50 | 100 | 0 | 30 | 0 | 0 | 100 | 0 | 30 | 0 |
| 0.1 | 60 | 100 | 10 | 40 | 0 | 0 | 90 | 10 | 40 | 0 |
| 0.3 | 70 | 50 | 10 | 10 | 0 | 0 | 90 | 10 | 20 | 0 |

**obs_only per-task (spatial):**

| norm | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
|:----:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0.05 | 80 | 90 | 0 | 40 | 10 | 0 | 80 | 0 | 50 | 0 |
| 0.1 | 90 | 100 | 0 | 40 | 10 | 0 | 90 | 0 | 20 | 0 |
| 0.2 | 90 | 100 | 0 | 30 | 10 | 0 | 90 | 0 | 30 | 0 |
| 0.3 | 90 | 100 | 0 | 30 | 10 | 0 | 100 | 0 | 30 | 0 |

---

## Table 4: Object Benchmark — Magnitude Results (mixed status)

### FINAL (seed=42, 10/10 tasks)

| Method | norm | Overall SR | Exp ID |
|--------|:----:|:---------:|--------|
| obs_only | 0.1 | **19%** | `eval-acr-object-v4-obs-only` |
| obs_only | 0.2 | **22%** | `eval-acr-object-obs-only-norm02` |

obs_only norm=0.2 per-task: alphabet_soup=0, cream_cheese=0, salad_dressing=30, bbq_sauce=40, ketchup=20, tomato_sauce=10, butter=10, milk=20, chocolate_pudding=60, orange_juice=30

### IN PROGRESS (seed=42, RUNNING)

| Method | norm | Exp ID | Tasks Done | Partial per-task |
|--------|:----:|--------|:----------:|------------------|
| obs_only | 0.03 | `eval-mag-obsonly-norm003-object` | 2/10 | alphabet_soup=0, cream_cheese=20 |
| obs_only | 0.05 | `eval-mag-obsonly-norm005-object` | 2/10 | alphabet_soup=0, cream_cheese=0 |
| obs_only | 0.3 | `eval-mag-obsonly-norm03-object` | 2/10 | alphabet_soup=0, cream_cheese=0 |
| perdof | 0.03 | `eval-mag-perdof-norm003-object` | 1/10 | alphabet_soup=0 |
| perdof | 0.05 | `eval-mag-perdof-norm005-object` | 1/10 | alphabet_soup=0 |
| perdof | 0.2 | `eval-mag-perdof-norm02-object` | 2/10 | alphabet_soup=0, cream_cheese=10 |
| perdof | 0.3 | `eval-mag-perdof-norm03-object-r3` | 0/10 | — |

---

## Table 5: Seed=43 Object Benchmark — Progress Tracker

| Method | Exp ID | Status | Tasks Done | Partial Per-task SR |
|--------|--------|:------:|:----------:|---------------------|
| VLA-only (K=1) | `eval-vla-only-object-seed43` | **DONE** | 10/10 | **Overall: 12%** — alphabet_soup=0, cream_cheese=10, salad_dressing=10, bbq_sauce=30, ketchup=0, tomato_sauce=0, butter=0, milk=10, chocolate_pudding=40, orange_juice=20 |
| obs_only (norm=0.1) | `eval-obs-only-object-seed43` | RUNNING | 6/10 | alphabet_soup=0, cream_cheese=10, salad_dressing=10, bbq_sauce=30, ketchup=0, tomato_sauce=0 |
| argmin (K=10) | `eval-argmin-object-seed43` | RUNNING | 6/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20, bbq_sauce=20, ketchup=10, tomato_sauce=10 |
| perdof (norm=0.1) | `eval-perdof-object-seed43` | RUNNING | 4/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20, bbq_sauce=30 |
| VLA-mean (K=10) | `eval-vla-mean-object-seed43` | RUNNING | 3/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20 |
| scalar (norm=0.1) | `eval-scalar-object-seed43` | RUNNING | 2/10 | alphabet_soup=0, cream_cheese=0 |

**Notes:**
- VLA-only seed=43 (12%) matches seed=42 (12%) exactly — baseline is consistent across seeds
- All running experiments last confirmed alive at 2026-05-16T03:55:00

---

## Cross-reference: Registry ID → Method Mapping

| Exp ID | Method | Benchmark | Seed | Norm | Status |
|--------|--------|-----------|:----:|:----:|:------:|
| `eval-acr-object-v4-obs-only` | obs_only | object | 42 | 0.1 | DONE |
| `eval-reconvla-object` | argmin (ReconVLA) | object | 42 | — | DONE |
| `eval-vla-only-object` | VLA-only K=1 | object | 42 | — | DONE |
| `eval-vla-mean-object` | VLA-mean K=10 | object | 42 | — | DONE |
| `eval-acr-object-v4-perdof` | perdof | object | 42 | 0.1 | DONE |
| `eval-acr-object-v4-scalar` | scalar | object | 42 | 0.1 | DONE |
| `eval-acr-object-obs-only-norm02` | obs_only | object | 42 | 0.2 | DONE |
| `eval-acr-spatial-v4-obs-only-r3` | obs_only | spatial | 42 | 0.1 | DONE |
| `eval-acr-spatial-v4-small-r2` | perdof | spatial | 42 | 0.1 | DONE |
| `eval-argmin-only-spatial-r2` | argmin (ReconVLA) | spatial | 42 | — | DONE |
| `eval-acr-spatial-v4-scalar-r2` | scalar | spatial | 42 | 0.1 | DONE |
| `eval-vla-mean-spatial` | VLA-mean K=10 | spatial | 42 | — | DONE |
| `eval-spatial-v7-full` | VLA-only K=1 | spatial | 42 | — | DONE |
