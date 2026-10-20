## R2-N3 Llama DocRED Parse-Failure-Excluded Analysis

### Parse Failure Statistics

| | Unconstrained | Constrained |
|---|---|---|
| Total docs | 998 | 998 |
| Parse failures | 67 (6.7%) | 90 (9.0%) |
| Valid docs | 931 | 908 |

Parse failure overlap: 45 shared, 45 constrained-only, 22 unconstrained-only.

### Violation Rates (parse failures excluded, valid docs only)

| Metric | Unconstrained | Constrained | Delta |
|---|---|---|---|
| ET% | 0.13% | 0.00% | -0.13pp |
| RV% | 15.89% | 0.00% | -15.89pp |
| DR% (eligible) | 31.21% | 2.57% | -28.64pp |
| DR% (all triples) | 26.25% | 2.57% | -23.68pp |
| CF% | 0.17% | 9.40% | +9.23pp |

### F1 (all docs vs parse-excluded)

| Metric | Uncon (all) | Con (all) | Uncon (excl) | Con (excl) |
|---|---|---|---|---|
| E-F1 | 55.67% | 55.04% | 57.89% | 58.18% |
| R-F1 | 6.55% | 6.25% | 6.74% | 6.48% |

### Conclusions

1. Constrained has MORE parse failures (90 vs 67), so excluding parse failures actually favors unconstrained
2. DR: 31.21% → 2.57% (-28.64pp) on valid docs only
3. RV: 15.89% → 0.00% (-15.89pp)
4. F1 essentially unchanged: E-F1 +0.29pp, R-F1 -0.26pp (noise)
5. CF +9.23pp is known trade-off

Core argument: violation reduction is real constrained decoding effect, not parse failure artifact.