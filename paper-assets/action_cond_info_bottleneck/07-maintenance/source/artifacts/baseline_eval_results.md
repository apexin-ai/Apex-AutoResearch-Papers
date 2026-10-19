# Baseline Evaluation Results

Generated: 2026-05-16

## Main Table (Paper Format)

| Model | LIBERO-Spatial | LIBERO-Object | LIBERO-Goal | LIBERO-10 | Average |
|-------|---------------|---------------|-------------|-----------|---------|
| SmolVLA (std) | 66.0±8.4 | 67.8±4.2 | 76.4±4.4 | TBD | 70.1 |
| SmolVLA+ (plus) | 81.6±6.0 | 88.8±2.6 | 87.8±4.0 | TBD | 86.1 |

- Values: Mean SR (%) ± SE across 10 tasks
- SE = std / sqrt(n_tasks), n_tasks = 10
- Average = mean of 3 suite means (excludes LIBERO-10 pending completion)

## Per-Task Breakdown (Appendix Format)

### LIBERO-Spatial (10 tasks × 50 episodes each)

| Task | SmolVLA (std) | SmolVLA+ (plus) |
|------|:------------:|:---------------:|
| task_0 | 82.0 | 98.0 |
| task_1 | 74.0 | 82.0 |
| task_2 | 88.0 | 92.0 |
| task_3 | 86.0 | 94.0 |
| task_4 | 52.0 | 74.0 |
| task_5 | 0.0 | 32.0 |
| task_6 | 90.0 | 94.0 |
| task_7 | 66.0 | 86.0 |
| task_8 | 58.0 | 80.0 |
| task_9 | 64.0 | 84.0 |
| **Mean±SE** | **66.0±8.4** | **81.6±6.0** |

### LIBERO-Object (10 tasks × 50 episodes each)

| Task | SmolVLA (std) | SmolVLA+ (plus) |
|------|:------------:|:---------------:|
| task_0 | 62.0 | 78.0 |
| task_1 | 58.0 | 92.0 |
| task_2 | 56.0 | 92.0 |
| task_3 | 56.0 | 88.0 |
| task_4 | 86.0 | 92.0 |
| task_5 | 52.0 | 78.0 |
| task_6 | 82.0 | 100.0 |
| task_7 | 64.0 | 80.0 |
| task_8 | 80.0 | 100.0 |
| task_9 | 82.0 | 88.0 |
| **Mean±SE** | **67.8±4.2** | **88.8±2.6** |

### LIBERO-Goal (10 tasks × 50 episodes each)

| Task | SmolVLA (std) | SmolVLA+ (plus) |
|------|:------------:|:---------------:|
| task_0 | 80.0 | 96.0 |
| task_1 | 96.0 | 100.0 |
| task_2 | 84.0 | 94.0 |
| task_3 | 58.0 | 72.0 |
| task_4 | 82.0 | 92.0 |
| task_5 | 64.0 | 86.0 |
| task_6 | 58.0 | 60.0 |
| task_7 | 96.0 | 98.0 |
| task_8 | 76.0 | 94.0 |
| task_9 | 70.0 | 86.0 |
| **Mean±SE** | **76.4±4.4** | **87.8±4.0** |

### LIBERO-10

Evaluation in progress. Data pending.

## Statistical Summary

| Suite | Model | Mean | Std | SE | 95% CI (t-dist, df=9) |
|-------|-------|------|-----|-----|----------------------|
| Spatial | std | 66.0 | 26.7 | 8.4 | [46.9, 85.1] |
| Spatial | plus | 81.6 | 18.9 | 6.0 | [68.1, 95.1] |
| Object | std | 67.8 | 13.1 | 4.2 | [58.5, 77.1] |
| Object | plus | 88.8 | 8.1 | 2.6 | [83.0, 94.6] |
| Goal | std | 76.4 | 13.9 | 4.4 | [66.5, 86.3] |
| Goal | plus | 87.8 | 12.7 | 4.0 | [78.7, 96.9] |

- 95% CI = mean ± t_{0.025, 9} × SE, where t_{0.025, 9} = 2.262

## Episode Counts

| Model | Suite | Tasks | Episodes/Task | Total Episodes |
|-------|-------|-------|--------------|----------------|
| SmolVLA (std) | Spatial | 10 | 50 | 500 |
| SmolVLA (std) | Object | 10 | 50 | 500 |
| SmolVLA (std) | Goal | 10 | 50 | 500 |
| SmolVLA+ (plus) | Spatial | 10 | 50 | 500 |
| SmolVLA+ (plus) | Object | 10 | 50 | 500 |
| SmolVLA+ (plus) | Goal | 10 | 50 | 500 |
| **Total** | | | | **3000** |

## Data Sources

- SmolVLA+ (plus): `/root/acib/outputs/baseline_plus_v2/{suite}/eval_info.json`
- SmolVLA (std): `/root/acib/outputs/baseline_std_v3/{suite}/eval_info.json`
- Server: westb-13953
