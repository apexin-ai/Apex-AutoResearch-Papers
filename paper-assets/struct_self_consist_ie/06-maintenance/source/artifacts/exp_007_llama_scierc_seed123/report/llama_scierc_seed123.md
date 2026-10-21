## LLaMA SciERC seed=123

| Metric | Value |
|---|---|
| Greedy F1 | 0.6454 |
| Oracle F1 | 0.7657 |
| Headroom | 12.04pp |
| Degeneracy | 26.7% (141/529) |
| DGS-Greedy | -0.38pp [-1.62, +0.78] n.s. |

### 5-Signal (n=529)
| Signal | ρ | AUROC |
|---|---|---|
| voting_conf | 0.4193 | 0.7159 |
| SJ | 0.3552 | 0.7092 |
| FK | 0.2897 | 0.6678 |
| EM | 0.2844 | 0.7468 |
| LP | 0.1970 | 0.5839 |

Structural > surface confirmed. Cross-seed consistent with seed=42.