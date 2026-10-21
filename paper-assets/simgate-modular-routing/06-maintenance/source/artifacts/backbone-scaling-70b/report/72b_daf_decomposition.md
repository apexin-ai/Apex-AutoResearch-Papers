## 72B DAF Decomposition

Data: 11 tasks x 20 eps = 220 episodes
Sources: westb-13313 (8 tasks), westb-14838 (3 tasks)
Computed: 2026-05-18

### All tasks (220 eps)
- Δ_full: 31.60
- Δ_nd (n=147 non-death eps): 2.87
- DAF: 90.9%
- DAF 95% CI: [83.9%, 97.3%]
- Label fraction (death_asymmetry / non-tie): 70/83 = 84.3%
- Label fraction 95% CI: [76.1%, 91.8%]

### Death-prone subset (200 eps, excl. find-non-living-thing)
- Δ_full: 32.77
- Δ_nd (n=127 non-death eps): 0.17
- DAF: 99.5%
- DAF 95% CI: [98.0%, 100.2%]
- Label fraction (death_asymmetry / non-tie): 70/73 = 95.9%
- Label fraction 95% CI: [90.8%, 100.0%]

### vs 7B comparison
- 7B DAF (all tasks): 90.4%
- 72B DAF (all tasks): 90.9%
- 7B DAF (death-prone): ~99%+
- 72B DAF (death-prone): 99.5%

Conclusion: DAF is nearly identical across 7B and 72B, confirming that death asymmetry is the dominant signal source regardless of backbone scale.

### Per-task breakdown

| Task | Δ_full | Δ_nd | DAF | Death eps |
|------|--------|------|-----|-----------|
| chemistry-mix | 46.10 | 0.00 | 100.0% | 10/20 |
| find-animal | 40.40 | 0.00 | 100.0% | 8/20 |
| find-non-living-thing | 20.00 | 20.00 | 0.0% | 0/20 |
| freeze | 45.00 | 0.00 | 100.0% | 9/20 |
| grow-fruit | 30.00 | 0.00 | 100.0% | 9/20 |
| identify-life-stages-1 | 40.00 | 0.00 | 100.0% | 8/20 |
| identify-life-stages-2 | 25.50 | 0.00 | 100.0% | 7/20 |
| inclined-plane-determine-angle | 28.75 | 1.67 | 94.2% | 5/20 |
| lifespan-longest-lived | 30.45 | 0.07 | 99.8% | 6/20 |
| lifespan-longest-lived-then-shortest-lived | 16.65 | 0.00 | 100.0% | 4/20 |
| measure-melting-point-unknown-substance | 24.80 | -0.31 | 101.2% | 7/20 |

Bootstrap: B=10000, seed=42
