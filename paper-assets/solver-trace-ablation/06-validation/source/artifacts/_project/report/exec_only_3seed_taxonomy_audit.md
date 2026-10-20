# Exec-Only 1000-Step Taxonomy Audit (2026-05-15)

## Summary

| Seed | Proved | H7a | H7b | H1 | H8 | H1∩H8 | Genuine | Gen% | Gen_strict | Pattern |
|------|--------|-----|-----|----|----|--------|---------|------|------------|---------|
| s43  | 90/100 | 90  | 0   | 0  | 0  | 0      | 0       | 0%   | 0          | 100% H7a tautology |
| s44  | 100/100| 0   | 0   | 85 | 15 | 3      | 3       | 3%   | 0          | H1+H8 dominant, 3 H1-near |

## s44 Genuine Proof Audit (3 proofs → all H1-near)

### folio_1296 (idx=51) — Fido/penguin
- **Conclusion**: `(S(a) ∧ A(a)) ∨ (F(a) ∧ G(a))`
- **P1**: `∀x ((F(x) ∧ G(x)) ∨ (S(x) ∧ A(x)))` → instantiated at a = conclusion (disjunct commuted)
- **Ground facts**: F(a), A(a), G(a), S(a) all present → both disjuncts trivially satisfied
- **ISR**: 0.0, n_necessary=0
- **Verdict**: H1-near. ∀x instantiation + disjunct commutativity = conclusion. NOT genuine reasoning.

### folio_1428 (idx=52) — Size Town bird
- **Conclusion**: `U(a) ∨ C(a)`
- **P1 conjunct**: `(U(x) ∨ C(x))` → instantiated = conclusion exactly
- **Ground facts**: U(a) ×6, C(a) ×6 — massive redundancy
- **ISR**: 0.0, n_necessary=0
- **Verdict**: H1-near. Conclusion = sub-formula of ∀x premise after instantiation. Ground facts also satisfy. NOT genuine.

### folio_1051 (idx=82) — Dune creative/sci-fi
- **Conclusion**: `C(a) ∨ S(a)`
- **P1**: `∀x (C(x) ∨ S(x))` → instantiated at a = `C(a) ∨ S(a)` **exact match**
- **Ground facts**: C(a), S(a) present 3x each
- **ISR**: 0.0, n_necessary=0
- **Verdict**: H1-near. Most clear-cut case — P1 instantiation IS the conclusion. Only ∀x prefix prevents text match. NOT genuine.

## Classifier Gap Analysis

All 3 escape classify_h7 because:
1. **H7** requires single premise → these have 9-16 premises
2. **H1** requires exact text match after normalization → `∀x (C(x) ∨ S(x))` ≠ `C(a) ∨ S(a)` (quantifier + variable)
3. **H8** requires top-level conjunction → conclusions are disjunctions (∨)

Root cause: No detector for "disjunction embedding" or "universal quantifier instantiation match."

## Per C013 Classification

Per C013: "H1-near 保留为 genuine 但单独标记"
- genuine_count = 3 (formal, per C013 formula)
- genuine_h1_near = 3 (all 3 are H1-near)
- genuine_strict = 0 (excluding H1-near)

## 3-Seed Statistics (1000 steps, genuine_strict)

| Seed | n_proved | genuine_strict | rate |
|------|----------|----------------|------|
| s43  | 90       | 0              | 0.0% |
| s44  | 100      | 0              | 0.0% |

Note: s42-r2 is 500 steps (checkpoint-500), not 1000 steps. No s42-1000 experiment exists.
For the two available 1000-step seeds: **genuine_strict = 0.0% ± 0.0%**

## Cross-Seed Hacking Mode Divergence

s43 and s44 learned completely different hacking strategies at 1000 steps:
- **s43**: Single-premise tautology (H7a=100%), ISR=0.53 (meaningless under H7)
- **s44**: Multi-premise conclusion embedding (H1=85%) + conjunction collapse (H8=15%), ISR≈0, content-independent predicates=100%

This extreme mode divergence across seeds is itself a finding: exec-only reward provides no consistent pressure toward any particular hacking mode.
