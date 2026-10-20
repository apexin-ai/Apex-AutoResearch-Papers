# Gold Set Evaluation Report (Full: SWE-agent + OpenHands)

**Date**: 2026-05-15

## Gold Label Distribution

- Total gold windows: **199**
- Matched: **195** (132 SWE-agent + 63 OpenHands)
- Stagnation (0): **67** (33.7%)
- Progress (1): **132** (66.3%)

## Per-Model Results vs Gold

| Model | N | Macro-F1 | F1(stag) | F1(prog) | Prec(stag) | Rec(stag) | Accuracy |
|---|---|---|---|---|---|---|---|
| MV Labels | 195 | 0.7184 | 0.6260 | 0.8108 | 0.6119 | 0.6406 | 0.7487 |
| GRU Probe | 132 | 0.7348 | 0.7328 | 0.7368 | 0.7059 | 0.7619 | 0.7348 |
|   gold_in_train | 39 | 0.8436 | 0.8636 | 0.8235 | 0.9048 | 0.8261 | 0.8462 |
|   gold_in_test | 17 | 0.8712 | 0.8333 | 0.9091 | 1.0000 | 0.7143 | 0.8824 |
| Structural RF | 195 | 0.7564 | 0.6815 | 0.8314 | 0.6479 | 0.7188 | 0.7795 |
| Structural GB | 195 | 0.7595 | 0.6818 | 0.8372 | 0.6618 | 0.7031 | 0.7846 |
| TWV Labels | 136 | 0.7184 | 0.6667 | 0.7702 | 0.8222 | 0.5606 | 0.7279 |
| TWV Probe | 132 | 0.7684 | 0.7368 | 0.8000 | 0.8235 | 0.6667 | 0.7727 |

## MV vs Gold Agreement

- MV-Gold agreement rate: **0.7487** (146/195)
- MV-Gold disagreement count: **49** / 195
- Implication: models trained on MV labels have a ceiling of ~74.9% accuracy when evaluated against gold.

---

# Stratified Analysis

## Gold Label Distribution by Source

| Source | N | Progress | Stagnation |
|--------|---|----------|------------|
| swe-agent | 132 | 69 (52.3%) | 63 (47.7%) |
| openhands | 63 | 62 (98.4%) | 1 (1.6%) |
| all | 195 | 131 (67.2%) | 64 (32.8%) |

## MV-Gold Agreement by Source

| Source | N | Agreement | Macro-F1 | F1(stag) | F1(prog) | Accuracy |
|--------|---|-----------|----------|----------|----------|----------|
| swe-agent | 132 | 0.7348 | 0.7304 | 0.6957 | 0.7651 | 0.7348 |
| openhands | 63 | 0.7778 | 0.4989 | 0.1250 | 0.8727 | 0.7778 |
| all | 195 | 0.7487 | 0.7184 | 0.6260 | 0.8108 | 0.7487 |

## MV-Gold Agreement by Confidence

| Confidence | N | Agreement | Macro-F1 | F1(stag) | F1(prog) | Accuracy |
|------------|---|-----------|----------|----------|----------|----------|
| conf=1 | 115 | 0.6957 | 0.6377 | 0.4928 | 0.7826 | 0.6957 |
| conf=2 | 67 | 0.8358 | 0.8230 | 0.7755 | 0.8706 | 0.8358 |
| conf=3 | 13 | 0.7692 | 0.7692 | 0.7692 | 0.7692 | 0.7692 |
| conf>=2 | 80 | 0.8250 | 0.8157 | 0.7742 | 0.8571 | 0.8250 |

## Source x Confidence Cross-tabulation

| Source | Confidence | N | Agreement | Macro-F1 |
|--------|------------|---|-----------|----------|
| swe-agent | conf=1 | 76 | 0.6579 | 0.6420 |
| swe-agent | conf=2 | 48 | 0.8125 | 0.8118 |
| swe-agent | conf=3 | 8 | 1.0000 | 1.0000 |
| swe-agent | conf>=2 | 56 | 0.8393 | 0.8392 |
| openhands | conf=1 | 39 | 0.7692 | 0.4348 |
| openhands | conf=2 | 19 | 0.8947 | 0.7206 |
| openhands | conf=3 | 5 | 0.4000 | 0.2857 |
| openhands | conf>=2 | 24 | 0.7917 | 0.5819 |

## Confusion Matrices (MV predicted vs Gold)

### All (n=195)

| | Pred Prog | Pred Stag |
|---|-----------|-----------|
| Gold Prog | 105 | 26 |
| Gold Stag | 23 | 41 |

### SWE-agent (n=132)

| | Pred Prog | Pred Stag |
|---|-----------|-----------|
| Gold Prog | 57 | 12 |
| Gold Stag | 23 | 40 |

### OpenHands (n=63)

| | Pred Prog | Pred Stag |
|---|-----------|-----------|
| Gold Prog | 48 | 14 |
| Gold Stag | 0 | 1 |
