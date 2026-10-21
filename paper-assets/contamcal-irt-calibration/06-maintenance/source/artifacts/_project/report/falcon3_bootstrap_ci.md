# Falcon3-7B-Base Bootstrap CI (Table 1)

Item-level paired bootstrap, B=10,000, seed=42, BCa confidence intervals.

## MMLU (5-shot, N=14,042 items)

| Dosage | Accuracy | 95% CI |
|--------|----------|--------|
| d000 | 58.77% | [57.97, 59.59] |
| d005 | 59.02% | [58.18, 59.85] |
| d025 | 61.23% | [60.43, 62.04] |
| d050 | 62.09% | [61.26, 62.90] |
| d100 | 62.96% | [62.15, 63.77] |

- **Δ(d100−d000) = +4.19pp, 95% BCa CI [+3.60, +4.79]**
- Pattern: **Benefit** (96.1% stable)
- Pattern distribution: Benefit 96.1%, Benefit-sat 3.9%

## ARC-Challenge (25-shot, N=1,172 items)

| Dosage | Accuracy | 95% CI |
|--------|----------|--------|
| d000 | 81.57% | [79.27, 83.79] |
| d005 | 83.11% | [80.89, 85.24] |
| d025 | 84.81% | [82.68, 86.86] |
| d050 | 83.28% | [81.14, 85.32] |
| d100 | 85.58% | [83.53, 87.54] |

- **Δ(d100−d000) = +4.01pp, 95% BCa CI [+2.22, +5.72]**
- Pattern: **Benefit-sat** (61.3% stable)
- Pattern distribution: Benefit-sat 61.3%, Benefit 38.7%

## Table 1 格式

| Model | Benchmark | Δ (pp) | 95% CI | Pattern | Stability |
|-------|-----------|--------|--------|---------|-----------|
| Falcon3-7B | MMLU | +4.19 | [+3.60, +4.79] | Benefit | 96.1% |
| Falcon3-7B | ARC | +4.01 | [+2.22, +5.72] | Benefit-sat | 61.3% |

## Notes

- Data source: westd-29999 (d000-d050), cqa1-21977 (d100), all `_aligned` suffix
- Falcon3 only has seed=42 data, no multi-seed — CI from item-level bootstrap (not cross-seed)
- ARC pattern stability is lower (61.3%) due to smaller item count (1,172 vs 14,042) and borderline Benefit/Benefit-sat classification
- ARC CI is wider ([+2.22, +5.72]) reflecting the smaller sample size
- All point estimates verified against expected values
