# Llama-70B Episode Analysis Results

## Experiment: llama-70b-episodes
- **Model**: Meta-Llama-3.1-70B-Instruct-AWQ-INT4
- **Environment**: ScienceWorld (11 task types × 20 episodes = 220 total)
- **Hypothesis**: DAF > 80% (death dominance scales to 70B)
- **Conclusion**: ✓ SUCCESS (DAF = 101.0%)

## Aggregate Metrics

| Metric | Value | 95% CI |
|--------|------:|--------|
| DAF | 101.0% | [95.3, 107.5] |
| delta_full (det − int) | 29.53 | [23.40, 35.87] |
| delta_nd (both-alive) | −0.30 | [−2.10, 1.38] |
| Label fraction | 91.3% | [84.1, 97.2] |
| Int death rate | 48.6% | [41.8, 55.0] |
| Det death rate | 20.0% | [15.0, 25.4] |
| Δ death rate | +28.6pp | [22.7, 34.5] |

## Label Distribution

| Label | Count | % |
|-------|------:|--:|
| det-preferred | 67 | 30.5% |
| internal-preferred | 2 | 0.9% |
| no-preference | 151 | 68.6% |

## Counterfactual Decomposition

| Category | Count |
|----------|------:|
| death_sole | 52 |
| death_and_score | 11 |
| non_death | 6 |
| no_preference | 151 |

## Per-Task Breakdown

| Task | Int DR | Det DR | delta_full | det-pref | int-pref |
|------|-------:|-------:|-----------:|---------:|---------:|
| chemistry-mix | 55.0% | 15.0% | 41.80 | 8 | 0 |
| find-animal | 55.0% | 20.0% | 35.40 | 7 | 0 |
| find-non-living-thing | 0.0% | 0.0% | −1.70 | 4 | 2 |
| freeze | 55.0% | 30.0% | 25.00 | 5 | 0 |
| grow-fruit | 50.0% | 35.0% | 15.00 | 3 | 0 |
| identify-life-stages-1 | 55.0% | 25.0% | 32.50 | 6 | 0 |
| identify-life-stages-2 | 50.0% | 25.0% | 25.00 | 5 | 0 |
| inclined-plane-determine-angle | 55.0% | 20.0% | 36.00 | 7 | 0 |
| lifespan-longest-lived | 50.0% | 25.0% | 27.50 | 5 | 0 |
| lifespan-longest-lived-then-shortest-lived | 55.0% | 15.0% | 43.30 | 8 | 0 |
| measure-melting-point-unknown-substance | 55.0% | 10.0% | 45.00 | 9 | 0 |

## Cross-Model Comparison

| Model | Size | DAF | delta_full | Int DR | Det DR |
|-------|------|----:|----------:|-------:|-------:|
| Qwen-2.5-7B-Instruct | 7B | 90.4% | — | — | — |
| Llama-3.1-8B-Instruct | 8B | 88.2% | — | — | — |
| Gemma-2-9B-it | 9B | 89.7% | — | — | — |
| Qwen-2.5-72B-Instruct-AWQ | 72B | 92.4% | — | — | — |
| **Llama-3.1-70B-Instruct-AWQ** | **70B** | **101.0%** | **29.53** | **48.6%** | **20.0%** |

## Key Observations

1. **DAF=101.0% (>100%)**: Death-avoidance accounts for more than 100% of the deterministic agent's advantage, meaning when both agents survive, the internal agent actually performs slightly better (delta_nd=−0.30).

2. **Strongest death dominance across all models tested**: The 70B Llama shows the highest DAF and largest death rate gap (28.6pp) among all models.

3. **Near-perfect label fraction (91.3%)**: When there's a preference, 97.1% favor deterministic (67 vs 2), driven almost entirely by death avoidance.

4. **find-non-living-thing is the only zero-death task**: Both agents survive all episodes, and this is the only task showing slight internal-agent preference (2 episodes).

5. **Hypothesis confirmed**: DAF > 80% holds strongly. The death dominance pattern not only scales to 70B but intensifies.

## Bootstrap Details
- B = 10,000, seed = 42
- All 10,000 bootstrap samples produced valid DAF estimates
- DAF 95% CI lower bound (95.3%) still well above 80% threshold
