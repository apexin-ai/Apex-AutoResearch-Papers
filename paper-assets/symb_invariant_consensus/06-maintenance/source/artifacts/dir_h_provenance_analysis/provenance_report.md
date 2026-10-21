# Dir-H: Constraint Provenance Analysis — FOLIO 204

**Date**: 2026-05-21 00:21
**Problems**: 204
**SC baseline**: 111/204 = 54.41%

## 1. Source Step Distribution

| Bin | Range | Count | Proportion |
|-----|-------|-------|------------|
| early | 1-3 | 6837 | 48.61% |
| mid | 4-6 | 5392 | 38.34% |
| late | 7-+ | 1836 | 13.05% |
| **total** | | **14065** | |

## 2. Correct vs Incorrect Problems

| Bin | Correct (norm) | Incorrect (norm) |
|-----|---------------|-----------------|
| early | 49.86% | 46.99% |
| mid | 37.86% | 38.96% |
| late | 12.28% | 14.05% |

Mann-Whitney U: stat=23416810.50, p=0.000173
Mean source_step — correct: 3.834, incorrect: 3.987

## 3. Conclusion Leakage by Step

| Bin | Leakage Rate | Leaks / Total |
|-----|-------------|---------------|
| early | 22.00% | 1504/6837 |
| mid | 23.11% | 1246/5392 |
| late | 27.23% | 500/1836 |

Chi-squared (3-way): χ²=22.3254, p=0.000014, dof=2
Fisher exact (early vs late): OR=0.7536, p=0.000003

## 4. Accuracy by Step Filter

Only constraints from the specified step bin are used for SICA scoring.

| Filter | Accuracy | Correct/Total | Δ vs SC |
|--------|----------|---------------|---------|
| all | 55.88% | 114/204 | +1.47% |
| early | 56.37% | 115/204 | +1.96% |
| mid | 56.86% | 116/204 | +2.45% |
| late | 44.12% | 90/204 | -10.29% |

## 5. Cross-Trace Consistency by Step

Fraction of unique expressions appearing in >1 trace.

| Bin | Consistency Rate | Multi-trace / Total |
|-----|-----------------|---------------------|
| early | 24.50% | 1018/4155 |
| mid | 16.73% | 646/3861 |
| late | 9.53% | 153/1606 |

## 6. Key Findings

- Late-step leakage rate (27.23%) vs early-step (22.00%): Fisher p=0.000003
  → **Significant**: late-step constraints have higher conclusion leakage
- Early-only SICA accuracy: 56.37% vs full SICA: 55.88%
- This supports the Dir-C finding that conclusion-referencing constraints are more prevalent in later reasoning steps.

---
*Analysis completed in 167.4s*