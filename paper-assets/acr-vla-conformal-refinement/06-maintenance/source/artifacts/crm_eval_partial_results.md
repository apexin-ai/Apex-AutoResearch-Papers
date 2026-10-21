# CRM Eval Partial Results (killed 2026-05-23 ~08:15 UTC)

Config: crm_obs_only, K=10, obs_dim=960, checkpoint=crm_smolvla_3suite_v1/crm_best.pt

## Spatial CRM (max_steps=280, n_rollouts=20)

### Seed 42 (7/10 tasks, task 7 in-progress at kill)
| Task | SR | Count |
|------|-----|-------|
| between_plate_ramekin | 80.0% | 16/20 |
| next_to_ramekin | 75.0% | 15/20 |
| from_table_center | 75.0% | 15/20 |
| on_cookie_box | 55.0% | 11/20 |
| in_top_drawer | 55.0% | 11/20 |
| on_ramekin | 0.0% | 0/20 |
| next_to_cookie_box | ~53% | 8/15 (in-progress) |
| **Completed avg** | **56.7%** | **(68/120)** |

### Seed 43 (7/10 tasks completed)
| Task | SR | Count |
|------|-----|-------|
| between_plate_ramekin | 85.0% | 17/20 |
| next_to_ramekin | 75.0% | 15/20 |
| from_table_center | 80.0% | 16/20 |
| on_cookie_box | 80.0% | 16/20 |
| in_top_drawer | 55.0% | 11/20 |
| on_ramekin | 0.0% | 0/20 |
| next_to_cookie_box | 75.0% | 15/20 |
| **Completed avg** | **64.3%** | **(90/140)** |

### Seed 44 (7/10 tasks completed)
| Task | SR | Count |
|------|-----|-------|
| between_plate_ramekin | 75.0% | 15/20 |
| next_to_ramekin | 75.0% | 15/20 |
| from_table_center | 80.0% | 16/20 |
| on_cookie_box | 80.0% | 16/20 |
| in_top_drawer | 50.0% | 10/20 |
| on_ramekin | 0.0% | 0/20 |
| next_to_cookie_box | 70.0% | 14/20 |
| **Completed avg** | **61.4%** | **(86/140)** |

## Goal CRM (max_steps=300, n_rollouts=20)

### Seed 42 (6/10 tasks completed)
| Task | SR | Count |
|------|-----|-------|
| open_middle_drawer | 60.0% | 12/20 |
| put_bowl_on_stove | 85.0% | 17/20 |
| put_wine_bottle | 60.0% | 12/20 |
| open_top_drawer | 15.0% | 3/20 |
| put_bowl_on_cabinet | 60.0% | 12/20 |
| push_plate_to_stove | 70.0% | 14/20 |
| **Completed avg** | **58.3%** | **(70/120)** |

### Seed 43 (7/10 tasks, task 7 in-progress at kill)
| Task | SR | Count |
|------|-----|-------|
| open_middle_drawer | 70.0% | 14/20 |
| put_bowl_on_stove | 85.0% | 17/20 |
| put_wine_bottle | 55.0% | 11/20 |
| open_top_drawer | 15.0% | 3/20 |
| put_bowl_on_cabinet | 75.0% | 15/20 |
| push_plate_to_stove | 70.0% | 14/20 |
| cream_cheese_in_bowl | ~20% | 2/10 (in-progress) |
| **Completed avg** | **61.7%** | **(74/120)** |

## Cross-seed Summary (completed tasks only)

| Benchmark | Seed 42 | Seed 43 | Seed 44 | Mean |
|-----------|---------|---------|---------|------|
| Spatial (7/10) | 56.7% | 64.3% | 61.4% | 60.8% |
| Goal (6/10) | 58.3% | 61.7% | — | 60.0% |
