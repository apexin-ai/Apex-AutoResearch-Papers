# Plan-005 Routing Pattern Analysis

## Data Source
- `results/plan005/routing_metrics.json` (30 tasks, 314 episodes)
- `results/plan005/failure_taxonomy.json`

## Task Classification Summary

| Category | Tasks | % | Episodes | % |
|---|---|---|---|---|
| death-dominated (DAF >= 95%) | 25 | 83.3% | 250 | 79.6% |
| genuine-det (DAF < 95%, Δ_nd > 0) | 3 | 10.0% | 19 | 6.1% |
| internal-preferred (Δ < 0) | 2 | 6.7% | 45 | 14.3% |
| no-signal | 0 | 0.0% | 0 | 0.0% |

## C1 Claim Support

- **Weighted mean DAF = 98.09%** across all tasks with positive DAF
- 25/30 tasks (83.3%) are death-dominated
- 17/25 death-dominated tasks have DAF = 1.0 (zero non-death advantage)
- Interpretation: death avoidance accounts for ~98% of the routing signal, strongly supporting C1

## Genuine-Det Tasks (3)

| Task | DAF | Δ(D-I) | Δ_nd |
|---|---|---|---|
| find-plant | 93.5% | 61.6 | 4.0 |
| find-living-thing | 89.2% | 41.8 | 4.5 |
| measure-melting-point-unknown-substance | 59.4% | 40.67 | 16.5 |

These tasks show real (non-death) deterministic advantage, but death still dominates the signal.

## Internal-Preferred Tasks (2)

| Task | DAF | Δ(D-I) | Notes |
|---|---|---|---|
| find-non-living-thing | -0.0 | -1.32 | Zero death rate, internal slightly better |
| grow-plant | N/A | 0.0 | Zero death rate, tied scores |

## Failure Taxonomy

- Internal deaths: 144 (3.89x more than deterministic)
- Deterministic deaths: 37
- Dominant failure mode: `focus-action` (navigation/exploration loops) — 100% of both internal and deterministic deaths
- Internal model gets stuck in exploration loops ~4x more often

## Output Files

- `results/plan005/analysis/task_classification.json` — per-task classification with key metrics
- `results/plan005/analysis/heatmap_data.csv` — Figure 1 data (30 rows x 14 columns, sorted by DAF desc)
- `results/plan005/analysis/taxonomy_summary.json` — aggregated statistics with C1 support analysis
