# Gold Set Evaluation Report

**Date**: 2026-05-15 17:12:02

## Gold Label Distribution

- Total gold windows: **199**
- Stagnation (0): **67** (33.7%)
- Progress (1): **132** (66.3%)

## Per-Model Results vs Gold

| Model | N | Macro-F1 | F1(stag) | F1(prog) | Prec(stag) | Rec(stag) | Accuracy |
|---|---|---|---|---|---|---|---|
| MV Labels | 195 | 0.7184 | 0.6260 | 0.8108 | 0.6119 | 0.6406 | 0.7487 |
| GRU Probe | 132 | 0.7348 | 0.7328 | 0.7368 | 0.7059 | 0.7619 | 0.7348 |
|   gold_in_train | 39 | 0.8436 | 0.8636 | 0.8235 | 0.9048 | 0.8261 | 0.8462 |
|   gold_in_test | 17 | 0.8712 | 0.8333 | 0.9091 | 1.0000 | 0.7143 | 0.8824 |
| Structural RF | 195 | 0.7516 | 0.6765 | 0.8268 | 0.6389 | 0.7188 | 0.7744 |
| Structural GB | 195 | 0.7644 | 0.6870 | 0.8417 | 0.6716 | 0.7031 | 0.7897 |
| TWV Labels | 136 | 0.7184 | 0.6667 | 0.7702 | 0.8222 | 0.5606 | 0.7279 |
| TWV Probe | 132 | 0.7684 | 0.7368 | 0.8000 | 0.8235 | 0.6667 | 0.7727 |

## MV vs Gold Agreement (Circular Eval Indicator)

- MV-Gold agreement rate: **0.7487**
- MV-Gold disagreement count: **49** / 195
- Implication: models trained on MV labels have a ceiling of ~74.9% accuracy when evaluated against gold.
