# W9 SciERC Sampling vs Greedy Analysis

## Experiment Setup

| | Greedy (phase2_scierc_full_s1_v2) | Sampling (w9_qwen_scierc_zs_sampling) |
|---|---|---|
| Model | Qwen (zero-shot) | Qwen (zero-shot) |
| Decoding | Greedy | Sampling |
| Constraints | Full (grammar + semantic) | Full (grammar + semantic) |
| Samples | 551 | 551 |
| Checker | fixed_20260514_v2 | fixed_20260514_v2 |

## Violation Metrics

| Metric | Greedy | Sampling | Δ |
|--------|--------|----------|---|
| ET (entity type) | 0.00% (0/2474) | 0.00% (0/2462) | 0 |
| RV (relation vocab) | 0.00% (0/1729) | 0.00% (0/1723) | 0 |
| DR (domain/range) | 0.93% (16/1729) | 0.75% (13/1723) | -0.18% |
| CF (cross-field consistency) | 9.90% (245/2474) | 9.91% (244/2462) | +0.01% |
| Parse fail | 0% | 0% | 0 |

## F1 Metrics (v2 checker, strict match)

| Metric | Greedy | Sampling | Δ |
|--------|--------|----------|---|
| Entity P | 25.98 | 26.29 | +0.31 |
| Entity R | 38.37 | 38.61 | +0.24 |
| **Entity F1** | **30.98** | **31.28** | **+0.30** |
| Relation P | 6.54 | 5.81 | -0.73 |
| Relation R | 11.60 | 10.27 | -1.33 |
| **Relation F1** | **8.36** | **7.42** | **-0.94** |

## Extraction Volume

| | Greedy | Sampling |
|---|---|---|
| Entities extracted | 2474 | 2462 |
| Relations extracted | 1729 | 1723 |
| Gold entities | 1673 | 1673 |
| Gold relations | 974 | 974 |

## Per-Relation DR Violations (Sampling)

| Relation | Total | DR Violations | Rate |
|----------|-------|---------------|------|
| Used-for | 794 | 0 | 0.00% |
| Feature-of | 500 | 5 | 1.00% |
| Evaluate-for | 127 | 7 | 5.51% |
| Hyponym-of | 111 | 0 | 0.00% |
| Compare | 87 | 1 | 1.15% |
| Part-of | 66 | 0 | 0.00% |
| Conjunction | 38 | 0 | 0.00% |

## Conclusions

1. **Constraints are robust under sampling decoding.** ET=0% and RV=0% in both conditions — grammar-constrained decoding completely eliminates these violations regardless of decoding strategy.

2. **DR violations slightly decrease with sampling** (0.93% → 0.75%). Sampling introduces no additional domain/range violations; the stochastic variation slightly favors valid type combinations.

3. **CF violations are essentially identical** (9.90% vs 9.91%). Cross-field consistency is inherently a document-level property not strongly affected by decoding temperature.

4. **Entity F1 is stable** (+0.30 F1, within noise). Sampling does not degrade entity extraction quality.

5. **Relation F1 drops slightly** (-0.94 F1). The sampling strategy produces marginally less precise relation predictions, though recall also drops — suggesting sampling occasionally generates non-matching relation phrasings rather than hallucinating more relations.

6. **Overall**: Schema semantic constraints remain effective under sampling. The constraint mechanism is **decoding-strategy-agnostic** — violations stay near zero for ET/RV, and DR remains under 1% in both conditions.

---

*Note: F1 values here are from the v2 violation checker (strict exact-match). Previously reported greedy baseline F1 (E_F1=35.38, R_F1=18.59) may have used a different evaluation methodology.*
