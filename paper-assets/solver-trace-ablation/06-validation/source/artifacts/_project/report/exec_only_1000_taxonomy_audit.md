# Exec-only 1000-step Taxonomy Audit (2026-05-15)

## Classify_h7.py Results

### plan001-exec-only-s42-r2 (from registry, H8 audited 2026-05-15)
| Metric | Value |
|--------|-------|
| PR | 0.93 (93/100) |
| Mean ISR | 0.1232 |
| H7 | 0 (0%) |
| H1 | 81 (87.1%) |
| H8 | 6 (6.5%) |
| Genuine | 7 (7.5%) |

### plan001-exec-only-s43-1000-r2 (fresh classify_h7 run)
| Metric | Value |
|--------|-------|
| PR | 0.90 (90/100) |
| Mean ISR | 0.5308 |
| H7a | 90 (100%) |
| H7b | 0 |
| H1 | 0 |
| H8 | 0 |
| Genuine | 0 (0%) |
| Pattern | All single-premise tautology (P therefore P) |

### plan001-exec-only-s44-1000-r2 (fresh classify_h7 run)
| Metric | Value |
|--------|-------|
| PR | 1.00 (100/100) |
| Mean ISR | 0.002 |
| H7 | 0 (0%) |
| H1 | 85 (85%) |
| H8 | 15 (15%) |
| Genuine | 3 (3%) |
| Pattern | H1-dominant with H8 conjunction collapse |

## S44 Genuine Sample Investigation

3 samples escaped all classifiers (folio_1296, folio_1428, folio_1051). All have ISR=0.

1. **folio_1296**: Conclusion `(S(a)∧A(a))∨(F(a)∧G(a))` is the commuted disjunction of premise 2 `∀x((S(x)∧A(x))∨(F(x)∧G(x)))` instantiated at a. H1 misses due to disjunct reordering.
2. **folio_1428**: Conclusion `U(a)∨C(a)` is a disjunction of two ground fact premises. Neither H1 (no exact text match) nor H8 (disjunction, not conjunction).
3. **folio_1051**: Conclusion `C(a)∨S(a)` follows from premise 1 `∀x(C(x)∨S(x))` at x=a. H1 misses because the premise is universally quantified.

**Verdict**: All 3 are functionally degenerate (ISR=0, trivial derivations). They are H1-near variants that escape text-based matching. Not genuine reasoning.

## 3-Seed Pooled Statistics

| Seed | PR | genuine_count | genuine_rate |
|------|-----|---------------|-------------|
| s42 | 0.93 | 7 | 7.53% |
| s43 | 0.90 | 0 | 0.00% |
| s44 | 1.00 | 3 | 3.00% |

**Mean genuine_rate**: 3.51%
**Std genuine_rate**: 3.78% (sample std, n=3)

## Discrepancy with D090

D090 claims "1.0%±1.7%" for exec-only genuine rate. Our computed value is **3.51%±3.78%**.

Key source of discrepancy: **s42 genuine=7 (7.5%)** pulls the mean up significantly. This may indicate:
- s42 needs a fresh classify_h7 re-run with current script version (its H8 audit was done separately, not via the same batch pipeline)
- Or D090 used a different definition/version of the classifiers
- s43 H7-dominant (100% tautology) → 0 genuine, which is unambiguous
- s44 genuine=3 are all ISR=0 degenerate proofs → functionally 0% genuine reasoning
