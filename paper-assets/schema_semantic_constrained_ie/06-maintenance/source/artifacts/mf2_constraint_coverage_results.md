# MF2/Q1: Constraint Table Coverage Analysis

## Summary

| Dataset | Unique Type Triples | Covered | Coverage (type) | Instances | Coverage (instance) |
|---------|-------------------|---------|-----------------|-----------|-------------------|
| SciERC (test) | 115 | 106 | **92.2%** | 974 | **99.0%** |
| DocRED (dev) | 360 | 313 | **86.9%** | 12,275 | **99.4%** |

Type-level coverage gap exists (7.8% SciERC, 13.1% DocRED), but instance-level impact is minimal (1.0% and 0.6% respectively) because uncovered triples are all low-frequency.

---

## SciERC (test set, 100 docs)

### Overall
- Unique (relation, head_type, tail_type) triples: 115
- Covered: 106 (92.2%)
- Uncovered: 9 (7.8%)
- Total instances: 974, covered instances: 964 (99.0%)

### Per-relation Coverage
| Relation | Type Coverage | Instance Coverage |
|----------|-------------|-------------------|
| Compare | 8/9 (89%) | 37/38 (97.4%) |
| Conjunction | 13/14 (93%) | 122/123 (99.2%) |
| Evaluate-for | 15/20 (75%) | 85/91 (93.4%) |
| Feature-of | 14/14 (100%) | 59/59 (100.0%) |
| Hyponym-of | 12/12 (100%) | 67/67 (100.0%) |
| Part-of | 13/14 (93%) | 62/63 (98.4%) |
| Used-for | 31/32 (97%) | 532/533 (99.8%) |

### Uncovered Type Pairs (9 triples, 10 instances)
| Relation | (Head, Tail) | Count |
|----------|-------------|-------|
| Compare | (Method, OtherScientificTerm) | 1 |
| Conjunction | (OtherScientificTerm, Task) | 1 |
| Evaluate-for | (Generic, Metric) | 1 |
| Evaluate-for | (Material, OtherScientificTerm) | 2 |
| Evaluate-for | (Metric, Metric) | 1 |
| Evaluate-for | (OtherScientificTerm, Material) | 1 |
| Evaluate-for | (OtherScientificTerm, Task) | 1 |
| Part-of | (Material, OtherScientificTerm) | 1 |
| Used-for | (Metric, Metric) | 1 |

---

## DocRED (dev set, 998 docs)

### Overall
- Unique (relation, head_type, tail_type) triples: 360
- Covered: 313 (86.9%)
- Uncovered: 47 (13.1%)
- Total instances: 12,275, covered instances: 12,199 (99.4%)

### Uncovered Type Pairs (47 triples, 76 instances)
| Relation | (Head, Tail) | Count |
|----------|-------------|-------|
| P102 member of political party | (ORG, ORG) | 1 |
| P1056 product or material produced | (MISC, MISC) | 2 |
| P108 employer | (PER, MISC) | 1 |
| P123 publisher | (PER, PER) | 1 |
| P127 owned by | (MISC, LOC) | 1 |
| P127 owned by | (MISC, MISC) | 8 |
| P1344 participant of | (PER, LOC) | 1 |
| P1365 replaces | (LOC, ORG) | 2 |
| P1366 replaced by | (LOC, ORG) | 1 |
| P137 operator | (LOC, MISC) | 1 |
| P137 operator | (MISC, MISC) | 1 |
| P1376 capital of | (LOC, MISC) | 1 |
| P1376 capital of | (MISC, LOC) | 1 |
| P140 religion | (MISC, ORG) | 6 |
| P1441 present in work | (PER, ORG) | 2 |
| P155 follows | (LOC, PER) | 1 |
| P155 follows | (MISC, ORG) | 1 |
| P155 follows | (MISC, PER) | 1 |
| P156 followed by | (ORG, MISC) | 1 |
| P156 followed by | (PER, MISC) | 1 |
| P176 manufacturer | (MISC, MISC) | 1 |
| P178 developer | (MISC, MISC) | 10 |
| P179 series | (MISC, ORG) | 2 |
| P179 series | (PER, ORG) | 1 |
| P241 military branch | (LOC, ORG) | 1 |
| P264 record label | (PER, PER) | 1 |
| P27 country of citizenship | (LOC, PER) | 1 |
| P272 production company | (MISC, MISC) | 1 |
| P276 location | (MISC, ORG) | 1 |
| P276 location | (ORG, ORG) | 2 |
| P31 instance of | (MISC, LOC) | 1 |
| P31 instance of | (MISC, PER) | 1 |
| P31 instance of | (PER, PER) | 1 |
| P36 capital | (MISC, LOC) | 1 |
| P37 official language | (ORG, LOC) | 2 |
| P449 original network | (MISC, TIME) | 1 |
| P50 author | (NUM, PER) | 1 |
| P551 residence | (LOC, LOC) | 2 |
| P607 conflict | (LOC, ORG) | 1 |
| P674 characters | (ORG, PER) | 1 |
| P710 participant | (PER, ORG) | 1 |
| P737 influenced by | (PER, MISC) | 1 |
| P749 parent organization | (MISC, MISC) | 1 |
| P749 parent organization | (ORG, LOC) | 1 |
| P800 notable work | (ORG, MISC) | 1 |
| P800 notable work | (PER, ORG) | 1 |
| P86 composer | (TIME, PER) | 2 |

---

## Training vs Test/Dev Type Pair Overlap

| Dataset | Train Unique Triples | Test/Dev Unique Triples | Overlap | Test-only |
|---------|---------------------|------------------------|---------|-----------|
| SciERC | 168 | 115 | 106 | **9** |
| DocRED | 545 | 360 | 313 | **47** |

**All 9 SciERC uncovered triples and all 47 DocRED uncovered triples are exactly the test/dev-only triples unseen in training.** The constraint table was built from training data, so coverage gap = zero-shot type pairs.

---

## Conclusions

1. **Instance-level coverage is near-perfect (99.0%/99.4%)**: the constraint table covers virtually all relation instances in test/dev. Uncovered triples are rare (10/974 SciERC, 76/12275 DocRED).

2. **Coverage gap is purely from unseen type pairs**: the uncovered triples are exactly those that never appeared in training. The constraint table faithfully captures all training-observed type combinations.

3. **DocRED gap is driven by MISC type ambiguity**: most DocRED uncovered pairs involve MISC (a catch-all type), reflecting annotation noise rather than genuine ontology gaps. Examples: P178 developer (MISC, MISC) x10, P127 owned by (MISC, MISC) x8, P140 religion (MISC, ORG) x6.

4. **SciERC gap is in Evaluate-for**: 5 of 9 uncovered triples belong to Evaluate-for, suggesting this relation has more flexible type compatibility than others.

5. **Practical implication**: the constraint table is tight enough for effective constrained decoding. The <1% uncovered instances are predominantly annotation edge cases, not systematic gaps. No constraint table expansion needed.
