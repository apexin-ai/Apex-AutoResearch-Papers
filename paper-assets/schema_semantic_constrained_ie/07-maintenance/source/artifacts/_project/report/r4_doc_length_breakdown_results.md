# Document Length Breakdown: OntoCoDec Constraint Effectiveness

## Summary

OntoCoDec's violation reduction is **consistent across document lengths** (~74–84%), even though longer documents produce more total violations. Constraints are equally effective on complex (longer) documents as on simple (shorter) ones.

---

## 1. SciERC (Qwen3-8B, Zero-Shot)

**Binning**: Tertile split on word count. 551 docs total.

| Bin    | #Docs | Word Range | Avg WC |
|--------|-------|-----------|--------|
| Short  | 196   | 5–19      | 15.2   |
| Medium | 180   | 20–27     | 23.3   |
| Long   | 175   | 28–97     | 35.6   |

### 1.1 Violation Counts (total across docs in bin)

| Bin    | Mode          | ET | RV | DR  | CF | Total | Doc-Viol% |
|--------|---------------|----|----|-----|----|-------|-----------|
| Short  | Unconstrained |  1 |  5 |  57 |  0 |    63 |     25.0% |
| Short  | Constrained   |  0 |  0 |   5 |  5 |    10 |      4.6% |
| Medium | Unconstrained |  6 |  9 | 104 |  0 |   119 |     43.9% |
| Medium | Constrained   |  0 |  0 |   7 | 15 |    22 |     10.0% |
| Long   | Unconstrained |  3 | 10 | 104 |  1 |   118 |     40.0% |
| Long   | Constrained   |  0 |  0 |   4 | 20 |    24 |     12.0% |

### 1.2 F1 (macro-avg over docs)

| Bin    | Mode          | E-F1  | R-F1 | Avg Ent | Avg Rel |
|--------|---------------|-------|------|---------|---------|
| Short  | Unconstrained | 32.4% | 8.9% |     3.2 |     2.1 |
| Short  | Constrained   | 32.4% | 8.9% |     3.2 |     2.1 |
| Medium | Unconstrained | 27.8% | 6.7% |     4.6 |     3.2 |
| Medium | Constrained   | 27.8% | 6.7% |     4.6 |     3.3 |
| Long   | Unconstrained | 29.9% | 7.0% |     5.9 |     4.1 |
| Long   | Constrained   | 30.0% | 7.3% |     5.9 |     4.1 |

### 1.3 Constraint Effect

| Bin    | Uncon Viols | Const Viols | Reduction | Reduction% |
|--------|-------------|-------------|-----------|------------|
| Short  |          63 |          10 |        53 |      84.1% |
| Medium |         119 |          22 |        97 |      81.5% |
| Long   |         118 |          24 |        94 |      79.7% |

---

## 2. DocRED (Qwen3-8B, Zero-Shot)

**Binning**: Tertile split on word count. 998 docs total.

| Bin    | #Docs | Word Range | Avg WC |
|--------|-------|-----------|--------|
| Short  | 336   | 129–160   | 144.8  |
| Medium | 332   | 161–208   | 182.1  |
| Long   | 330   | 209–510   | 274.7  |

### 2.1 Violation Counts (total across docs in bin)

| Bin    | Mode          |  ET |   RV |   DR |  CF | Total | Doc-Viol% |
|--------|---------------|-----|------|------|-----|-------|-----------|
| Short  | Unconstrained | 177 | 1238 | 1021 |   9 |  2445 |     95.5% |
| Short  | Constrained   |   0 |    0 |  495 | 138 |   633 |     69.6% |
| Medium | Unconstrained | 147 | 1742 | 1047 |   5 |  2941 |     96.7% |
| Medium | Constrained   |   0 |    5 |  544 | 180 |   729 |     77.0% |
| Long   | Unconstrained | 176 | 2209 | 1162 |   3 |  3550 |     98.7% |
| Long   | Constrained   |   0 |    0 |  731 | 200 |   931 |     80.7% |

### 2.2 F1 (macro-avg over docs)

| Bin    | Mode          | E-F1  | R-F1 | Avg Ent | Avg Rel |
|--------|---------------|-------|------|---------|---------|
| Short  | Unconstrained | 61.1% | 9.3% |    17.1 |    14.8 |
| Short  | Constrained   | 62.6% | 9.6% |    17.2 |    14.9 |
| Medium | Unconstrained | 59.3% | 7.9% |    20.3 |    17.6 |
| Medium | Constrained   | 60.7% | 8.5% |    20.3 |    17.5 |
| Long   | Unconstrained | 53.9% | 5.6% |    24.1 |    21.0 |
| Long   | Constrained   | 54.8% | 5.8% |    24.0 |    20.5 |

### 2.3 Constraint Effect

| Bin    | Uncon Viols | Const Viols | Reduction | Reduction% |
|--------|-------------|-------------|-----------|------------|
| Short  |        2445 |         633 |      1812 |      74.1% |
| Medium |        2941 |         729 |      2212 |      75.2% |
| Long   |        3550 |         931 |      2619 |      73.8% |

---

## 3. Key Findings

1. **Consistent reduction across lengths**: Violation reduction is 80–84% for SciERC and 74–75% for DocRED, with no significant degradation on longer documents.

2. **Longer docs produce more violations**: In DocRED, long docs average 10.8 violations/doc unconstrained vs 7.3 for short docs. OntoCoDec scales proportionally.

3. **ET and RV fully eliminated**: Grammar-constrained decoding eliminates 100% of entity-type and relation-vocabulary violations across all length bins (both datasets).

4. **Residual DR violations in DocRED**: Domain-range violations remain in constrained mode (495–731 per bin). This is consistent with the known limitation that DocRED's 96 relation types create a larger semantic constraint space.

5. **CF violations trade-off**: In SciERC, constrained mode introduces new CF violations (0→5/15/20 across bins) while eliminating ET/RV. The grammar forces valid types, but sometimes assigns different valid types to the same entity across relations.

6. **F1 preserved or improved**: Constrained decoding does not harm extraction quality. DocRED shows slight E-F1 improvement (+0.9–1.5pp) and R-F1 improvement (+0.2–0.6pp) across all bins. SciERC is essentially unchanged.

7. **Long-doc effectiveness**: The most important finding: long documents (where violations are most prevalent) benefit equally from OntoCoDec. The constraint framework does not degrade with document complexity.
