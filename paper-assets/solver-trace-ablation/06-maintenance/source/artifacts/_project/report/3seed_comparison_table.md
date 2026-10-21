# Random β=0.1 vs ISR β=0.1: Cross-Seed Comparison Table

Generated: 2026-05-15 | Source: project registry (solver-trace-ablation)

## Data Quality Note

**plan018-additive-random-b01-s42** was reclassified on 2026-05-15 with updated classify_h7.py.
- Old values: H7=0, H1_exact=56, H1_near=8, H8=3, genuine_strict=12
- New values: H7=0, H1=58, H8=4, genuine=18
- **Consistency issue**: H7+H1+H8+genuine = 0+58+4+18 = 80 ≠ n_proved=79. One sample double-counted. Needs investigation.

All other experiments sum correctly (H7+H1+H8+genuine = n_proved).

---

## ISR β=0.1 — Per-Seed Results (3 seeds)

| Metric | s42 | s43-r2 | s44 |
|--------|-----|--------|-----|
| exp_id | plan002-additive-b01-s42 | plan002-additive-b01-s43-r2 | plan002-additive-b01-s44 |
| Prove Rate | 0.81 | 0.61 | 0.89 |
| n_proved | 81 | 61 | 89 |
| H7 | 13 (16.0%) | 61 (100%) | 89 (100%) |
| H1 | 42 (51.9%) | 0 (0%) | 0 (0%) |
| H8 | 12 (14.8%) | 0 (0%) | 0 (0%) |
| genuine | 14 (17.3%) | 0 (0%) | 0 (0%) |
| mean ISR | 0.3365 | 0.5063 | 0.803 |

### ISR β=0.1 — Pooled Statistics

| Metric | Value |
|--------|-------|
| total n_proved | 231 |
| mean PR ± std | 0.770 ± 0.144 |
| pooled genuine | 14/231 = 6.06% |
| pooled H7 | 163/231 = 70.56% |
| pooled H1 | 42/231 = 18.18% |
| pooled H8 | 12/231 = 5.19% |
| mean genuine_rate ± std | 5.77% ± 9.99% |

Per-seed genuine rates: 17.3%, 0%, 0% — high variance driven by s42.

**Key pattern**: 2/3 seeds (s43, s44) collapsed to 100% H7 tautology. Only s42 retained genuine proofs.

---

## Random β=0.1 — Per-Seed Results (2 seeds; s44-r2 RUNNING)

| Metric | s42 | s43-r3 |
|--------|-----|--------|
| exp_id | plan018-additive-random-b01-s42 | plan018-additive-random-b01-s43-r3 |
| Prove Rate | 0.79 | 0.94 |
| n_proved | 79 | 94 |
| H7 | 0 (0%) | 36 (38.3%) |
| H1 | 58 (73.4%) | 56 (59.6%) |
| H8 | 4 (5.1%) | 1 (1.1%) |
| genuine | 18 (22.8%)* | 1 (1.1%) |
| mean ISR | 0.1038 | 0.1406 |

*See data quality note above. Old genuine_strict=12 (15.19%) before reclassification.

### Random β=0.1 — Pooled Statistics (2-seed, provisional)

| Metric | Value |
|--------|-------|
| total n_proved | 173 |
| mean PR | 0.865 (range: 0.79–0.94) |
| pooled genuine | 19/173 = 10.98% |
| pooled H7 | 36/173 = 20.81% |
| pooled H1 | 114/173 = 65.90% |
| pooled H8 | 5/173 = 2.89% |
| per-seed genuine rates | 22.8%, 1.1% |

**Key pattern**: Both seeds dominated by H1 (conclusion-in-premise). s42 has 0% H7 while s43-r3 has 38.3% H7. High inter-seed variance.

---

## Side-by-Side Comparison

| Metric | ISR β=0.1 (3-seed) | Random β=0.1 (2-seed) |
|--------|--------------------|-----------------------|
| mean PR | 0.770 ± 0.144 | 0.865 |
| pooled genuine rate | 6.06% (14/231) | 10.98% (19/173) |
| pooled H7 rate | 70.56% (163/231) | 20.81% (36/173) |
| pooled H1 rate | 18.18% (42/231) | 65.90% (114/173) |
| pooled H8 rate | 5.19% (12/231) | 2.89% (5/173) |
| dominant failure mode | H7 tautology | H1 conclusion embedding |
| seeds with genuine=0 | 2/3 | 0/2 |

### Interpretation

1. **ISR reward amplifies H7 tautology**: 70.6% pooled H7 vs 20.8% for Random. ISR incentivizes maximizing indispensability → model discovers tautological shortcut (single-premise = conclusion).
2. **Random reward amplifies H1 embedding**: 65.9% pooled H1 vs 18.2% for ISR. Without ISR pressure, model defaults to embedding conclusion in premises.
3. **Neither method produces reliable genuine proofs**: ISR pooled genuine 6.1%, Random pooled genuine 11.0%. Both far below SFT baseline (~93% genuine).
4. **Both show extreme inter-seed variance**: ISR ranges 0%–17.3% genuine; Random ranges 1.1%–22.8%. Single-seed results unreliable.

---

## Pending

- [ ] Random s44-r2 (plan018-additive-random-b01-s44-r2): RUNNING. Add to table when complete.
- [ ] Investigate s42 reclassification sum mismatch (80 vs 79).
