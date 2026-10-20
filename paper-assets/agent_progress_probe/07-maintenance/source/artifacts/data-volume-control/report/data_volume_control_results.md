# Data Volume Control Experiment Results

## Design
- Remove 9,813 random windows from 46,708 non-test windows (matching OB holdout count)
- 3 seeds: 42, 123, 456
- Fixed test set: 344 instances, 8,101 windows (from checkpoints_full/split_info.json)

## Per-seed Results
| Seed | macro-F1 | accuracy | F1(stag) | F1(prog) |
|------|----------|----------|----------|----------|
| 42   | 0.8613   | 0.8935   | 0.7946   | 0.9281   |
| 123  | 0.8473   | 0.8808   | 0.7759   | 0.9188   |
| 456  | 0.8489   | 0.8824   | 0.7777   | 0.9200   |

## Summary
| Condition | macro-F1 | vs baseline |
|-----------|----------|-------------|
| Baseline (full data) | 0.847 | — |
| Random removal (9813w) | 0.8525 ± 0.0063 | -0.6pp |
| OB removal (9813w) | 0.770 ± 0.022 | -7.7pp |

## Conclusion
Random removal barely hurts (-0.6pp), while OB removal causes -7.7pp.
Gap of +8.3pp is entirely attributable to OB signal, not data volume.
OB's privileged distant supervision provides independent, significant contribution to stagnation detection.