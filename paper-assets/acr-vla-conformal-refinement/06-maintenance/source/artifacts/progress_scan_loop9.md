# Progress Scan — Loop 9 (2026-05-15)

All 15 processes ALIVE across 4 servers.

## Summary Table

| exp_id | server:gpu | PID | alive | tasks_done | running_avg | current_task |
|--------|-----------|-----|-------|-----------|-------------|--------------|
| **Object Eval (bjb1-32546)** | | | | | | |
| eval-reconvla-object | bjb1-32546:0 | 9659 | YES | 6/10 | 6.7% (4/60) | T6 |
| eval-acr-object-v4-perdof | bjb1-32546:1 | 11116 | YES | 6/10 | 8.3% (5/60) | T6 butter (r5) |
| eval-acr-object-v4-obs-only | bjb1-32546:2 | 13806 | YES | 6/10 | 13.3% (8/60) | T6 |
| eval-acr-object-v4-scalar | bjb1-32546:3 | 14003 | YES | 6/10 | 3.3% (2/60) | T6 |
| eval-acr-object-obs-only-norm02 | bjb1-32546:4 | 44270 | YES | 5/10 | 18.0% (9/50) | T5 tomato_sauce |
| eval-vla-mean-object | bjb1-32546:5 | 18808 | YES | 6/10 | 10.0% (6/60) | T6 |
| **Mag Sweep — perdof (bjb2-28827)** | | | | | | |
| eval-mag-perdof-norm003 | bjb2-28827:0 | 13185 | YES | 6/10 | 33.3% (20/60) | T6 next_to_cookie (r5) |
| eval-mag-perdof-norm005 | bjb2-28827:1 | 13456 | YES | 6/10 | 30.0% (18/60) | T6 |
| eval-mag-perdof-norm02 | bjb2-28827:2 | 13728 | YES | 6/10 | 28.3% (17/60) | T6 |
| eval-mag-perdof-norm03 | bjb2-28827:3 | 14260 | YES | 6/10 | 23.3% (14/60) | T6 |
| **Mag Sweep — obs_only (bjb2-28827)** | | | | | | |
| eval-mag-obsonly-norm005 | bjb2-28827:4 | 14854 | YES | 7/10 | 42.9% (30/70) | T7 |
| eval-mag-obsonly-norm02 | bjb2-28827:5 | 15190 | YES | 7/10 | 45.7% (32/70) | T7 |
| **Remaining spatial** | | | | | | |
| eval-mag-obsonly-norm03-r2 | bjb1-18228:0 | 325264 | YES | 5/10 | 46.0% (23/50) | T5 on_ramekin |
| eval-acr-spatial-v4-scalar-r2 | bjb1-18228:1 | 311881 | YES | 5/7 (from T3) | 26.0% (13/50) | T8 next_to_plate (r5) |
| eval-mag-obsonly-norm003-b2 | bjb2-40593:0 | 227434 | YES | 3/10 | 63.3% (19/30) | T3 cookie_box (r5) |

## Per-Task Results — Object Eval (bjb1-32546)

| Task | reconvla | perdof n=0.1 | obs_only n=0.1 | scalar n=0.1 | obs_only n=0.2 | vla_mean |
|------|----------|-------------|---------------|-------------|----------------|----------|
| T0 alphabet_soup | 0% | 0% | 0% | 0% | 0% | 0% |
| T1 cream_cheese | 0% | 0% | 10% | 0% | 0% | 0% |
| T2 salad_dressing | 10% | 20% | 20% | 10% | 30% | 10% |
| T3 bbq_sauce | 30% | 30% | 40% | 10% | 40% | 30% |
| T4 ketchup | 0% | 0% | 10% | 0% | 20% | 10% |
| T5 tomato_sauce | 0% | 0% | 0% | 0% | — | 10% |
| **Avg (done)** | **6.7%** | **8.3%** | **13.3%** | **3.3%** | **18.0%** | **10.0%** |

### Object Eval Analysis
- **obs_only n=0.2 leads**: 18.0%, consistently better on T2-T4
- **obs_only n=0.1 second**: 13.3%, only method with success on T1 cream_cheese
- **scalar worst**: 3.3%, far behind other CRM variants
- **reconvla vs vla_mean**: close (6.7% vs 10.0%), vla_mean has slight edge on T5
- T0 alphabet_soup = 0% for all methods (hardest task)

## Per-Task Results — Magnitude Sweep (perdof, spatial)

| Task | n=0.03 | n=0.05 | n=0.2 | n=0.3 |
|------|--------|--------|-------|-------|
| T0 between_plate_ramekin | 60% | 50% | 60% | 70% |
| T1 next_to_ramekin | 100% | 100% | 90% | 50% |
| T2 from_table_center | 0% | 0% | 0% | 10% |
| T3 on_cookie_box | 30% | 30% | 20% | 10% |
| T4 in_top_drawer | 10% | 0% | 0% | 0% |
| T5 on_ramekin | 0% | 0% | 0% | 0% |
| **Avg (6T)** | **33.3%** | **30.0%** | **28.3%** | **23.3%** |

### Perdof Magnitude Analysis
- **Small norm (0.03) best**: 33.3%, conservative correction wins
- **Large norm (0.3) worst**: 23.3%, T1 drops from 100% to 50% (overcorrection)
- Clear monotonic trend: larger norm → worse performance
- T2 and T5 near-zero for all norms

## Per-Task Results — Magnitude Sweep (obs_only, spatial)

| Task | n=0.03 (40593) | n=0.05 (28827) | n=0.2 (28827) | n=0.3 (18228) |
|------|----------------|----------------|---------------|---------------|
| T0 between_plate_ramekin | 90% | 80% | 90% | 90% |
| T1 next_to_ramekin | 100% | 90% | 100% | 100% |
| T2 from_table_center | 0% | 0% | 0% | 0% |
| T3 on_cookie_box | — | 40% | 30% | 30% |
| T4 in_top_drawer | — | 10% | 10% | 10% |
| T5 on_ramekin | — | 0% | 0% | — |
| T6 next_to_cookie_box | — | 80% | 90% | — |
| **Avg (done)** | **63.3% (3T)** | **42.9% (7T)** | **45.7% (7T)** | **46.0% (5T)** |

### Obs_only Magnitude Analysis
- obs_only dominates perdof across the board (~45% vs ~28%)
- **Norm has minimal effect on obs_only**: 0.05/0.2/0.3 within 3% of each other
- n=0.03 shows 63.3% but only 3 easy tasks completed — wait for more data
- T6 next_to_cookie_box is an obs_only strong point: 80-90%

## Scalar (spatial, from T3) — bjb1-18228

| Task | scalar n=0.1 |
|------|-------------|
| T3 on_cookie_box | 40% |
| T4 in_top_drawer | 0% |
| T5 on_ramekin | 0% |
| T6 next_to_cookie_box | 90% |
| T7 on_stove | 0% |
| **Avg (T3-T7)** | **26.0%** |

Currently on T8 (next_to_plate, r5/10).

## ETA Estimates

- **bjb1-32546 object evals**: ~60% done, ~6h remaining
- **bjb2-28827 perdof sweep**: ~60% done, ~5h remaining
- **bjb2-28827 obs_only sweep**: ~70% done, ~3h remaining
- **bjb1-18228 obs_only-norm03**: 50% done, ~5h remaining
- **bjb1-18228 scalar-r2**: 71% done (5/7), ~2h remaining
- **bjb2-40593 obs_only-norm003**: 30% done, ~12h remaining (slowest)

## Key Takeaways

1. **obs_only >> perdof >> scalar** consistent across object and spatial benchmarks
2. **Magnitude matters for perdof** (small norm better); **minimal effect on obs_only** (robust)
3. Object benchmark has very low success rates (3-18%); spatial much higher (23-63%)
4. All 15 processes running normally, no anomalies
