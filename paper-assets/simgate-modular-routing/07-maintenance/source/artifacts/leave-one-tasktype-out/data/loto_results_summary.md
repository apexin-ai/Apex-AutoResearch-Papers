# LOTO Results Summary

## 2-class task types (bal_acc, mean across 8 seeds)
| Task Type | bal_acc | s42 | s43 | s44 | s45 | s46 | s47 | s48 | s49 |
|-----------|---------|-----|-----|-----|-----|-----|-----|-----|-----|
| chemistry-mix | 0.5503 | 0.508 | 0.586 | 0.550 | 0.561 | 0.550 | 0.517 | 0.558 | 0.572 |
| find-non-living-thing | 0.5986 | 0.583 | 0.638 | 0.594 | 0.564 | 0.628 | 0.605 | 0.590 | 0.587 |
| grow-fruit | 0.6715 | 0.678 | 0.711 | 0.567 | 0.639 | 0.694 | 0.661 | 0.733 | 0.689 |
| lifespan-longest-lived-then-shortest-lived | 0.5700 | 0.437 | 0.470 | 0.687 | 0.663 | 0.597 | 0.620 | 0.507 | 0.580 |

## Grand mean (2-class): 0.5976 ± 0.0184
## Majority-vote baseline: 0.5000
## Cross-split reference: 0.4711 ± 0.0221

## Single-class task types (all deterministic, bal_acc N/A)
find-animal, freeze, identify-life-stages-1, identify-life-stages-2, inclined-plane-determine-angle, lifespan-longest-lived, measure-melting-point-unknown-substance

Remote file: westb-13313:/root/autodl-tmp/simgate-modular-routing/results/leave_one_tasktype_out/results.json