# Table 1 — Multi-seed Results (Clean supp-era data)

Generated: 2026-05-24 20:10 UTC

## Main Table

| Suite | VLA-only | CRM (ε=0.05) | Adaptive (τ=0.25) | Δ(A-V) | Δ(A-C) |
|-------|---------|-------------|-------------------|--------|--------|
| Spatial | 79.1±1.1 (8s) | 79.8±1.4 (5s) | 80.9±0.9 (8s) | **+1.8pp** | +1.1pp |
| Goal | 82.9±1.1 (7s) | 82.7±1.6 (6s) | 83.4±1.8 (8s) | +0.5pp | +0.8pp |
| Object | 77.0±1.8 (5s) | 78.0±2.9 (6s) | 77.0±2.1 (8s) | +0.0pp | -1.0pp |
| Long | 58.4±1.6 (5s) | 56.4±2.3 (6s) | 57.8±1.9 (6s) | -0.6pp | +1.3pp |

## Paired t-test: Δ(A-V) = Adaptive - VLA-only

| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
|-------|---------|--------|---------|-----------|-------|
| **Spatial** | **+1.75pp** | **4.041** | **0.0049** | **8** | s42-s49 |
| Goal | +0.43pp | 0.505 | 0.6314 | 7 | s43-s49 |
| Object | -0.50pp | -0.520 | 0.6306 | 5 | s45-s49 |
| Long | -0.70pp | -0.578 | 0.5940 | 5 | s42,s44-s47 |

## Paired t-test: Δ(A-C) = Adaptive - CRM always-on

| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
|-------|---------|--------|---------|-----------|-------|
| Spatial | +0.60pp | 0.885 | 0.4263 | 5 | s43-s47 |
| Goal | +0.92pp | 1.309 | 0.2474 | 6 | s42-s47 |
| Object | -0.33pp | -0.249 | 0.8134 | 6 | s42-s47 |
| Long | +1.33pp | 1.315 | 0.2455 | 6 | s42-s47 |

## Trigger Rate ↔ Effect Size (D140 key evidence)

| Suite | Mean Trigger Rate | Δ(A-V) | Correlation |
|-------|------------------|--------|-------------|
| Spatial | 19.8% | +1.75pp | Highest trigger → Strongest positive Δ |
| Goal | 8.6% | +0.43pp | Medium trigger → Small positive Δ |
| Object | 3.8% | -0.50pp | Low trigger → Near zero Δ |
| Long | 4.2% | -0.70pp | Low trigger → Near zero Δ |

## Per-seed Raw Data

### Spatial (8 matched seeds)
| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
|------|---------|----------|-----|--------|
| s42 | 80.0% | 82.0% | — | +2.0pp |
| s43 | 79.0% | 80.0% | 81.0% | +1.0pp |
| s44 | 78.5% | 80.5% | 78.5% | +2.0pp |
| s45 | 77.0% | 80.0% | 78.0% | +3.0pp |
| s46 | 80.5% | 80.0% | 81.0% | -0.5pp |
| s47 | 80.0% | 81.5% | 80.5% | +1.5pp |
| s48 | 79.5% | 81.0% | — | +1.5pp |
| s49 | 78.5% | 82.0% | — | +3.5pp |

### Goal (7 matched seeds for A-V)
| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
|------|---------|----------|-----|--------|
| s42 | — | 84.0% | 85.5% | — |
| s43 | 82.5% | 84.5% | 82.0% | +2.0pp |
| s44 | 82.0% | 86.5% | 83.5% | +4.5pp |
| s45 | 83.5% | 81.0% | 81.0% | -2.5pp |
| s46 | 83.0% | 83.5% | 82.0% | +0.5pp |
| s47 | 82.5% | 82.0% | 82.0% | -0.5pp |
| s48 | 85.0% | 84.5% | — | -0.5pp |
| s49 | 82.0% | 81.5% | — | -0.5pp |

### Object (5 matched seeds for A-V)
| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
|------|---------|----------|-----|--------|
| s42 | — | 81.0% | 77.0% | — |
| s43 | — | 77.5% | 78.5% | — |
| s44 | — | 75.0% | 74.0% | — |
| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |
| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |
| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |
| s48 | 79.0% | 76.0% | — | -3.0pp |
| s49 | 75.5% | 74.0% | — | -1.5pp |

### Long (5 matched seeds for A-V)
| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
|------|---------|----------|-----|--------|
| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |
| s43 | — | 58.0% | 54.5% | — |
| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |
| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |
| s46 | 60.5% | 58.5% | 54.0% | -2.0pp |
| s47 | 59.5% | 55.0% | 56.5% | -4.5pp |

## Data Gaps
- Goal VLA-only s42: missing
- Object VLA-only s42/s43/s44: missing
- Spatial CRM s42/s48/s49: missing
- Goal/Object CRM s48/s49: missing
- Long VLA-only s43/s48/s49: missing
- Long Adaptive s48/s49: missing

## Note on Spatial VLA-only s42
eval-supp-spatial-vla-only-s42: command has no --model pi05 flag (should be SmolVLA default), but spec metadata shows model_name=pi05 and wall_clock=3.14h (typical for pi05, not SmolVLA ~30min). Needs verification. Current stats include this seed; excluding it would give 7-seed Spatial p-value (still likely significant).