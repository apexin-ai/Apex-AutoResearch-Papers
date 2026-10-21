# Llama DocRED Per-Relation DR Violation & Fallback Analysis

## 1. Aggregate Summary

| Metric | Unconstrained | Full_S1 | Delta |
|--------|--------------|---------|-------|
| Total triples | 16,437 | 16,368 | -69 |
| Parse failures | 68/998 | 91/998 | +23 |
| OOV (RV) triples | 2,756 (16.8%) | 0 (0.0%) | -2,756 |
| Mapped triples | 13,681 | 16,368 | +2,687 |
| DR violations (of mapped) | 4,221 (30.9%) | 418 (2.6%) | -3,803 |
| DR violations (of total) | 4,221 (25.7%) | 418 (2.6%) | -3,803 |
| Unique OOV relation names | 625 | 0 | -625 |

## 2. Per-Relation DR Violation Rate — Unconstrained (Top 10)

| P-code | Relation Name | Total | DR | DR% |
|--------|--------------|-------|-----|-----|
| P1198 | unemployment rate | 13 | 12 | 92.3% |
| P156 | followed by | 84 | 70 | 83.3% |
| P35 | head of state | 34 | 28 | 82.4% |
| P710 | participant | 139 | 109 | 78.4% |
| P582 | end time | 139 | 106 | 76.3% |
| P6 | head of government | 28 | 21 | 75.0% |
| P86 | composer | 117 | 85 | 72.6% |
| P276 | location | 422 | 291 | 69.0% |
| P155 | follows | 164 | 112 | 68.3% |
| P170 | creator | 167 | 109 | 65.3% |

**Bottom 5 (0% DR):** P140 (religion), P22 (father), P25 (mother), P118 (league), P264 (record label)

## 3. Per-Relation DR Violation Rate — Full_S1 (Top 10)

| P-code | Relation Name | Total | DR | DR% |
|--------|--------------|-------|-----|-----|
| P576 | dissolved/demolished | 73 | 24 | 32.9% |
| P156 | followed by | 117 | 24 | 20.5% |
| P1198 | unemployment rate | 15 | 3 | 20.0% |
| P582 | end time | 130 | 21 | 16.2% |
| P31 | instance of | 290 | 37 | 12.8% |
| P1056 | product or material produced | 98 | 11 | 11.2% |
| P740 | location of formation | 81 | 8 | 9.9% |
| P35 | head of state | 41 | 3 | 7.3% |
| P1001 | applies to jurisdiction | 637 | 45 | 7.1% |
| P607 | conflict | 453 | 30 | 6.6% |

**0% DR relations (>20 triples):** P131 (located in admin entity, 1660), P206 (body of water, 577), P361 (part of, 347), P170 (creator, 190), P40 (child, 161), P86 (composer, 150), P39 (position held, 125), P674 (characters, 122)

## 4. Per-Relation DR Comparison: Unconstrained → Full_S1

| P-code | Relation | Unc DR/Tot | Unc DR% | FS1 DR/Tot | FS1 DR% | Reduction |
|--------|----------|-----------|---------|-----------|---------|-----------|
| P1001 | applies to jurisdiction | 318/509 | 62.5% | 45/637 | 7.1% | -55.4pp |
| P276 | location | 291/422 | 69.0% | 23/458 | 5.0% | -64.0pp |
| P569 | date of birth | 287/560 | 51.2% | 21/833 | 2.5% | -48.7pp |
| P607 | conflict | 262/452 | 58.0% | 30/453 | 6.6% | -51.4pp |
| P166 | award received | 171/340 | 50.3% | 3/363 | 0.8% | -49.5pp |
| P570 | date of death | 142/313 | 45.4% | 7/448 | 1.6% | -43.8pp |
| P580 | start time | 138/273 | 50.5% | 3/332 | 0.9% | -49.6pp |
| P108 | employer | 132/458 | 28.8% | 9/492 | 1.8% | -27.0pp |
| P495 | country of origin | 122/610 | 20.0% | 4/668 | 0.6% | -19.4pp |
| P155 | follows | 112/164 | 68.3% | 6/235 | 2.6% | -65.7pp |
| P170 | creator | 109/167 | 65.3% | 0/190 | 0.0% | -65.3pp |
| P31 | instance of | 109/254 | 42.9% | 37/290 | 12.8% | -30.1pp |

## 5. OOV Relation Names — Unconstrained

625 unique OOV names, 2,756 total OOV triples (16.8% of all triples).

| OOV Relation Name | Count |
|-------------------|-------|
| located in | 405 |
| date of event | 93 |
| date of release | 60 |
| parent | 53 |
| release date | 50 |
| related to | 47 |
| similar to | 41 |
| MISC | 38 |
| synonym | 35 |
| named after | 33 |

**Full_S1: 0 OOV** — constrained decoding completely eliminates OOV.

## 6. Fallback Analysis (Full_S1)

- Total token-level fallback events: 57,825
- Concentrated in only **7 out of 998 documents** (991 docs = 0 fallback)
- All 7 fallback docs parsed successfully (OK status)
- Distribution: 6 docs with 8,400-10,029 fallbacks each, 1 doc with 500
- Fallback docs are evenly spaced (indices 1, 166, 328, 485, 655, 821, 984 — every ~166 docs)
- **Not comparable to Qwen's triple-level fallback rate (10.2%)**

The even spacing (every 166 docs) suggests a systematic trigger, not random; possibly related to specific doc characteristics or batch-boundary effects.

## 7. Qwen vs Llama Comparison

### DR Rate Comparison (Unconstrained)
| Metric | Qwen | Llama |
|--------|------|-------|
| OOV rate | 5,189 triples (~30%) | 2,756 (16.8%) |
| Unique OOV names | — | 625 |
| Top DR: P31 instance_of | 60.4% | 42.9% |
| Top DR: P1001 applies_to_jurisdiction | 44.4% | 62.5% |

### DR Rate Comparison (Full_S1)
| Metric | Qwen | Llama |
|--------|------|-------|
| OOV rate | — | 0.0% |
| Aggregate DR (mapped) | — | 2.6% |
| Aggregate fallback | 10.2% (1,770/17,341 triples) | 57,825 token-level (7 docs) |

### Key Differences
1. **Llama has lower OOV rate** (16.8% vs ~30%): Llama more often generates valid ontology relation names even unconstrained
2. **Llama unconstrained DR is lower per-relation for P31** (42.9% vs 60.4%) but higher for P1001 (62.5% vs 44.4%) — different error profiles
3. **Full_S1 eliminates OOV completely** for both models
4. **Llama full_s1 residual DR is very low** (2.6%) with only 3 relations >10% (P576, P156, P1198)

## 8. Does this support the "Low RV → Low Residual DR" narrative?

**Partially yes, with nuance:**

- Llama unconstrained OOV rate (16.8%) is lower than Qwen (~30%), and Llama full_s1 residual DR (2.6%) is lower than implied Qwen residual DR
- Both models reach 0% OOV under full_s1, confirming constrained decoding fully resolves RV
- The residual DR (2.6% for Llama) persists despite 0% OOV, showing DR is a separate axis — models still occasionally produce wrong entity type pairs even with correct relation names
- The **two-factor narrative holds**: RV and DR are independent violation types; full_s1 eliminates RV entirely and dramatically reduces (but doesn't eliminate) DR
- The persistent residual DR hotspots (P576=32.9%, P156=20.5%) suggest certain relations have inherently ambiguous domain-range patterns that even semantic constraints can't fully resolve
- Llama's lower unconstrained OOV rate correlates with its lower full_s1 DR residual, consistent with the hypothesis that a model with better baseline schema adherence benefits more cleanly from constrained decoding
