# plan017_14b_rsft_s43_eval — Analysis Report

**Experiment**: 14B RSFT s43 dev with-evidence eval (DocRED dev, 985 docs, matched@2048)

## Core Metrics

| Metric | Value |
|--------|-------|
| **Ign-F1** | **0.5815** |
| F1 | 0.5938 |
| Precision | 0.5715 |
| Recall | 0.6180 |
| Ign-Precision | 0.5495 |
| Ign-Recall | 0.6175 |
| TP | 7,509 |
| Pred Count | 13,140 |
| Gold Count | 12,151 |
| Evi-F1 (TP) | 0.8293 |
| Evi-F1 (Joint/DREEAM) | 0.4843 |
| EDCR | 0.5938 |
| Format OK | 984/985 (99.9%) |
| Truncated | 83/985 |
| Predictions | 17,043 |
| Inference Time | 20,676s (20.99 s/doc) |

## s42 vs s43 Dev Reproducibility

| Seed | Dev Ign-F1 (with-evi) | Δ vs s42 |
|------|----------------------|----------|
| s42 | 0.5886 | — |
| s43 | 0.5815 | **−0.71pp** |

Variance of 0.71pp between two seeds — moderate but within acceptable range for DocRED dev. s43 underperforms s42 slightly, likely due to seed-dependent training dynamics.

## s43 Dev Evidence Tax

| Condition | Dev Ign-F1 |
|-----------|-----------|
| s43 with-evidence | 0.5815 |
| s43 no-evidence | 0.5713 |
| **s43 dev tax** | **−1.02pp** (evidence helps) |

## Cross-Seed Evidence Tax Comparison (Dev)

| Seed | with-evi | no-evi | Dev Tax |
|------|----------|--------|---------|
| s42 | 0.5886 | 0.5432 | **−4.54pp** |
| s43 | 0.5815 | 0.5713 | **−1.02pp** |

Both seeds show evidence helps on dev, but the magnitude varies substantially (4.54pp vs 1.02pp). s43's no-evi model is much stronger (0.5713 vs 0.5432), closing the gap.

## Dev vs Test Evidence Tax Direction

| Seed | Dev Tax | Test Tax | Direction Consistent? |
|------|---------|----------|----------------------|
| s42 | −4.54pp | +0.77pp | **No** (flips) |
| s43 | −1.02pp | +0.08pp | **No** (flips) |

Both seeds show the same pattern: evidence helps on dev but has neutral-to-slightly-negative effect on test. s43's gap between dev and test is much smaller (+1.02pp dev benefit → +0.08pp test penalty), suggesting less overfitting to dev evidence patterns compared to s42.

## Key Observations

1. **Reproducibility**: 0.71pp variance between s42/s43 on dev with-evi is moderate — the RSFT pipeline is reasonably stable but not perfectly reproducible.
2. **Evidence tax on dev is seed-dependent**: s42 shows a large 4.54pp benefit from evidence on dev, while s43 shows only 1.02pp. This is driven primarily by the no-evi model variance (s42=0.5432 vs s43=0.5713).
3. **Dev-test tax direction flip is consistent**: Both seeds show evidence helps on dev but not on test, confirming this is a systematic pattern rather than seed noise.
4. **s43 test tax near zero**: s43's test tax (+0.08pp) is essentially zero, the most encouraging result — evidence neither helps nor hurts on test for this seed.
