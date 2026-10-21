## 72B Backbone Scaling Death Rate Analysis

**Date**: 2026-05-17
**Model**: Qwen2.5-72B-Instruct-AWQ
**Death criterion**: `internal_final == -100.0`

### Data Completeness

| Task | 13313 eps | 14838 eps | Source used | Used (cap 20) |
|------|-----------|-----------|-------------|---------------|
| chemistry-mix | 20 | 0 | 13313 | 20 |
| find-animal | 20 | 0 | 13313 | 20 |
| find-non-living-thing | 20 | 0 | 13313 | 20 |
| freeze | 20 | 0 | 13313 | 20 |
| grow-fruit | 20 | 20 | 14838 | 20 |
| identify-life-stages-1 | 20 | 20 | 14838 | 20 |
| identify-life-stages-2 | 20 | 40 | 14838 | 20 |
| inclined-plane-determine-angle | 20 | 37 | 14838 | 20 |
| lifespan-longest-lived | 10 | 20 | 14838 | 20 |
| lifespan-longest-lived-then-shortest-lived | 0 | 20 | 14838 | 20 |
| measure-melting-point-unknown-substance | 0 | 16 | 14838 | **16 (short 4)** |

- 10/11 tasks have >= 20 episodes
- measure-melting-point-unknown-substance: only 16 episodes available (supplement in progress)
- Overlap tasks (grow-fruit, identify-life-stages-1/2, inclined-plane): used 14838 per priority rule

### Per-Task Death Rate

| Task | Deaths | Total | Death Rate |
|------|--------|-------|------------|
| chemistry-mix | 10 | 20 | **50.0%** |
| find-animal | 8 | 20 | 40.0% |
| find-non-living-thing | 0 | 20 | **0.0%** |
| freeze | 9 | 20 | 45.0% |
| grow-fruit | 8 | 20 | 40.0% |
| identify-life-stages-1 | 9 | 20 | 45.0% |
| identify-life-stages-2 | 6 | 20 | 30.0% |
| inclined-plane-determine-angle | 9 | 20 | 45.0% |
| lifespan-longest-lived | 5 | 20 | 25.0% |
| lifespan-longest-lived-then-shortest-lived | 4 | 20 | 20.0% |
| measure-melting-point-unknown-substance | 4 | 16 | 25.0% |

### Aggregate

- **Death Rate: 33.3%** (72 deaths / 216 total episodes)
- **95% CI (bootstrap 1000x): [26.9%, 40.3%]**
- vs 7B baseline (42.9%): **-9.6pp** (72B dies less than 7B)
- vs deterministic (16.3%): **+17.0pp** (72B still dies much more than deterministic)

### Key Observations

1. **Scaling helps but doesn't solve death**: 72B death rate (33.3%) is meaningfully lower than 7B (42.9%), but still far above deterministic baseline (16.3%). The 95% CI [26.9%, 40.3%] does not overlap with 16.3%.
2. **High variance across tasks**: death rates range from 0% (find-non-living-thing) to 50% (chemistry-mix). Chemistry-mix and freeze are the deadliest tasks.
3. **find-non-living-thing is death-free**: the only task with zero deaths at 72B scale.
4. **Note on data quality**: identify-life-stages-2 and inclined-plane-determine-angle on 14838 have multiple collection runs concatenated in the JSONL file (variations restart). First 20 sequential entries used for analysis.
