# Gold Set Evaluation Report

**Date**: 2026-05-15 19:43:43

## Gold Label Distribution

- Total gold windows: **601**
- Stagnation (0): **183** (30.4%)
- Progress (1): **418** (69.6%)

## Per-Model Results vs Gold

| Model | N | Macro-F1 | F1(stag) | F1(prog) | Prec(stag) | Rec(stag) | Accuracy |
|---|---|---|---|---|---|---|---|
| MV Labels | 584 | 0.6818 | 0.5587 | 0.8049 | 0.5495 | 0.5682 | 0.7295 |
| GRU Probe | 386 | 0.7028 | 0.6667 | 0.7390 | 0.6608 | 0.6726 | 0.7073 |
|   gold_in_train | 126 | 0.7695 | 0.7603 | 0.7786 | 0.7931 | 0.7302 | 0.7698 |
|   gold_in_test | 54 | 0.8692 | 0.8571 | 0.8814 | 0.8750 | 0.8400 | 0.8704 |
| Structural RF | 584 | 0.6973 | 0.5910 | 0.8035 | 0.5517 | 0.6364 | 0.7346 |
| Structural GB | 584 | 0.7237 | 0.6162 | 0.8311 | 0.6077 | 0.6250 | 0.7654 |
| TWV Labels | 402 | 0.7392 | 0.6775 | 0.8008 | 0.7879 | 0.5943 | 0.7537 |
| TWV Probe | 386 | 0.7370 | 0.6757 | 0.7983 | 0.7812 | 0.5952 | 0.7513 |

## MV vs Gold Agreement (Circular Eval Indicator)

- MV-Gold agreement rate: **0.7295**
- MV-Gold disagreement count: **158** / 584
- Implication: models trained on MV labels have a ceiling of ~72.9% accuracy when evaluated against gold.
