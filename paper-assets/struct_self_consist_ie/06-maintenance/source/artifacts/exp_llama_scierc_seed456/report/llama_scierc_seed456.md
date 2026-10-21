## LLaMA SciERC seed=456

| Metric | Value |
|---|---|
| Greedy F1 | 0.6457 |
| Oracle F1 | 0.7574 |
| Headroom | 11.17pp |
| Degeneracy | 27.6% (146/529) |
| DGS-Greedy | -0.03pp (n.s.) |

### 5-Signal (n=529)
| Signal | ρ | AUROC |
|---|---|---|
| voting_conf | 0.4135 | 0.7113 |
| SJ | 0.3663 | 0.7061 |
| FK | 0.3115 | 0.6723 |
| EM | 0.3088 | 0.7538 |
| LP | 0.1911 | 0.5636 |

### LLaMA SciERC 3-seed summary
| Seed | SJ ρ | LP ρ | Degen% | DGS |
|------|------|------|--------|-----|
| 42 | 0.363 | 0.183 | 19.1% | — |
| 123 | 0.355 | 0.197 | 26.7% | -0.38pp |
| 456 | 0.366 | 0.191 | 27.6% | -0.03pp |