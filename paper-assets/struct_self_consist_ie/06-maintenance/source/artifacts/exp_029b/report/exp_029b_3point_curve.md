# SciERC 3-Point Epoch-Degeneracy Curve

## 3-Point Comparison Table

| Metric | 3-epoch (exp_029a) | 5-epoch (exp-012) | 10-epoch (exp_029b) |
|--------|-------------------|-------------------|---------------------|
| **Degeneracy (CF1 gold-filtered)** | **6.43%** | **17.58%** | **47.83%** |
| Greedy F1 | 0.6501 | 0.6094 | 0.6491 |
| Oracle F1 | 0.7998 | N/A | 0.7331 |
| Headroom (pp) | ~15.0 | N/A | 8.40 |
| LP sel delta (pp) | -1.18 | -0.07 | +0.75 |
| Within-inst ρ median | 0.3172 | 0.2474 | 0.1201 |
| LP range mean | 0.0854 | N/A | 0.0333 |
| FK ρ | 0.5302 | N/A | 0.3413 |
| SJ ρ | 0.5160 | N/A | 0.3441 |

## Key Finding
Degeneracy is monotonically increasing with training epochs: 6.43% → 17.58% → 47.83%
Acceleration effect: 3→5 = +11.2pp, 5→10 = +30.2pp

## Paper Usage (per Director decision)
- Epoch_confound table reports ONLY degeneracy rate
- No within-instance ρ column (underpowered)
- No LP selection delta column (underpowered)