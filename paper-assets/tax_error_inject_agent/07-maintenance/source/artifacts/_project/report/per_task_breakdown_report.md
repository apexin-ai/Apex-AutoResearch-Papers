# Per-Task-Type Breakdown Report

Generated: 2026-05-15

## 1. Dose-Response Per-Task Table (fixed-size 4,358, seed=42)

All values are success rate (%). Vanilla baseline = v4_vanilla_eval.

| Task Type | Vanilla | TaxEI-10% | TaxEI-25% | TaxEI-50% | Rand-10% | Rand-25% | Rand-50% |
|-----------|---------|-----------|-----------|-----------|----------|----------|----------|
| look_at_obj_in_light | 83.3 (5/6) | 83.3 (5/6) | 66.7 (4/6) | 83.3 (5/6) | 83.3 (5/6) | 66.7 (4/6) | 83.3 (5/6) |
| pick_and_place_simple | 62.5 (5/8) | 62.5 (5/8) | 37.5 (3/8) | 37.5 (3/8) | 62.5 (5/8) | 50.0 (4/8) | 37.5 (3/8) |
| pick_clean_then_place | 45.5 (5/11) | 45.5 (5/11) | 45.5 (5/11) | 54.5 (6/11) | 54.5 (6/11) | 63.6 (7/11) | 36.4 (4/11) |
| pick_cool_then_place | 57.1 (4/7) | 57.1 (4/7) | 28.6 (2/7) | 28.6 (2/7) | 57.1 (4/7) | 28.6 (2/7) | 42.9 (3/7) |
| pick_heat_then_place | 75.0 (6/8) | 75.0 (6/8) | 62.5 (5/8) | 50.0 (4/8) | 87.5 (7/8) | 75.0 (6/8) | 75.0 (6/8) |
| pick_two_obj_and_place | 57.1 (4/7) | 57.1 (4/7) | 57.1 (4/7) | 57.1 (4/7) | 71.4 (5/7) | 42.9 (3/7) | 85.7 (6/7) |
| **Overall** | **61.7** | **61.7** | **48.9** | **51.1** | **68.1** | **55.3** | **57.4** |

### Δ vs Vanilla (dose-response)

| Task Type | TaxEI-10% | TaxEI-25% | TaxEI-50% | Rand-10% | Rand-25% | Rand-50% |
|-----------|-----------|-----------|-----------|----------|----------|----------|
| look_at_obj_in_light | 0.0 | **-16.7** | 0.0 | 0.0 | -16.7 | 0.0 |
| pick_and_place_simple | 0.0 | **-25.0** | **-25.0** | 0.0 | -12.5 | -25.0 |
| pick_clean_then_place | 0.0 | 0.0 | +9.1 | +9.1 | +18.2 | -9.1 |
| pick_cool_then_place | 0.0 | **-28.6** | **-28.6** | 0.0 | -28.6 | -14.3 |
| pick_heat_then_place | 0.0 | -12.5 | **-25.0** | +12.5 | 0.0 | 0.0 |
| pick_two_obj_and_place | 0.0 | 0.0 | 0.0 | +14.3 | -14.3 | +28.6 |
| **Overall** | **0.0** | **-12.8** | **-10.6** | **+6.4** | **-6.4** | **-4.3** |

**Key observation**: TaxEI-10% has zero per-task difference from vanilla — identical success/fail on every task.

---

## 2. Most Affected Task Types (Injection Impact)

Ranked by max absolute Δ vs vanilla across dose-response experiments:

### TaxEI injection — most vulnerable tasks:
1. **pick_cool_then_place_in_recep**: -28.6pp at both 25% and 50% dose (57.1% → 28.6%)
2. **pick_and_place_simple**: -25.0pp at both 25% and 50% (62.5% → 37.5%)
3. **pick_heat_then_place_in_recep**: -25.0pp at 50% dose (75.0% → 50.0%)
4. **look_at_obj_in_light**: -16.7pp at 25% only (83.3% → 66.7%)

### TaxEI injection — resilient tasks:
- **pick_clean_then_place_in_recep**: unaffected or slightly improved (+9.1pp at 50%)
- **pick_two_obj_and_place**: completely unaffected (57.1% across all TaxEI doses)

---

## 3. 3-Seed Eval Per-Task Breakdown

### Per-seed raw data

| Task Type | Van-s42 | Van-s0 | Van-s123 | Tax-s42 | Tax-s0 | Tax-s123 | Rnd-s42 | Rnd-s0 | Rnd-s123 |
|-----------|---------|--------|----------|---------|--------|----------|---------|--------|----------|
| look_at_obj | 83.3 | 83.3 | 83.3 | 100.0 | 83.3 | 83.3 | 100.0 | 83.3 | 83.3 |
| pick_place | 62.5 | 62.5 | 75.0 | 62.5 | 37.5 | 50.0 | 50.0 | 50.0 | 62.5 |
| pick_clean | 45.5 | 54.5 | 45.5 | 54.5 | 45.5 | 63.6 | 54.5 | 54.5 | 63.6 |
| pick_cool | 57.1 | 57.1 | 57.1 | 42.9 | 28.6 | 42.9 | 57.1 | 57.1 | 57.1 |
| pick_heat | 75.0 | 87.5 | 87.5 | 87.5 | 50.0 | 75.0 | 87.5 | 50.0 | 75.0 |
| pick_two | 57.1 | 71.4 | 57.1 | 28.6 | 42.9 | 57.1 | 57.1 | 42.9 | 71.4 |
| **Overall** | **61.7** | **68.1** | **66.0** | **61.7** | **46.8** | **61.7** | **66.0** | **55.3** | **68.1** |

### 3-Seed Averages

| Task Type | Vanilla (avg) | TaxEI (avg) | Random (avg) | TaxEI Δ | Random Δ | Tax−Rnd |
|-----------|---------------|-------------|--------------|---------|----------|---------|
| look_at_obj_in_light | 83.3 | 88.9 | 88.9 | +5.6 | +5.6 | 0.0 |
| pick_and_place_simple | 66.7 | 50.0 | 54.2 | **-16.7** | -12.5 | -4.2 |
| pick_clean_then_place | 48.5 | 54.5 | 57.5 | +6.1 | +9.1 | -3.0 |
| pick_cool_then_place | 57.1 | 38.1 | 57.1 | **-19.0** | 0.0 | **-19.0** |
| pick_heat_then_place | 83.3 | 70.8 | 70.8 | -12.5 | -12.5 | 0.0 |
| pick_two_obj_and_place | 61.9 | 42.9 | 57.1 | **-19.0** | -4.8 | **-14.3** |
| **Overall** | **65.3** | **56.7** | **63.1** | **-8.5** | **-2.2** | **-6.4** |

---

## 4. TaxEI vs Random: Taxonomy Penalty by Task Type

The "Tax−Rnd" column above isolates the taxonomy-specific penalty (beyond generic noise).

**Tasks with strong taxonomy penalty** (TaxEI hurts much more than Random):

| Task Type | TaxEI avg | Random avg | Tax−Rnd gap | Interpretation |
|-----------|-----------|------------|-------------|----------------|
| **pick_cool_then_place** | 38.1% | 57.1% | **-19.0pp** | Taxonomy targets cooling-related action sequences; random noise leaves them intact |
| **pick_two_obj_and_place** | 42.9% | 57.1% | **-14.3pp** | Multi-object coordination especially vulnerable to taxonomy-guided perturbation |
| pick_and_place_simple | 50.0% | 54.2% | -4.2pp | Small additional taxonomy effect |
| pick_clean_then_place | 54.5% | 57.5% | -3.0pp | Minimal difference |

**Tasks with no taxonomy penalty** (TaxEI ≈ Random):
| Task Type | TaxEI avg | Random avg | Tax−Rnd gap |
|-----------|-----------|------------|-------------|
| look_at_obj_in_light | 88.9% | 88.9% | 0.0pp |
| pick_heat_then_place | 70.8% | 70.8% | 0.0pp |

### Summary

- **pick_cool_then_place** and **pick_two_obj_and_place** are the two tasks where taxonomy-guided injection is clearly more harmful than random noise (-19pp and -14pp gap).
- **pick_heat_then_place** degrades equally under TaxEI and Random (-12.5pp each), suggesting its degradation comes from generic noise, not taxonomy targeting.
- **look_at_obj_in_light** is the easiest task and resilient to both injection types.
- **pick_clean_then_place** paradoxically improves slightly under both injection types.
