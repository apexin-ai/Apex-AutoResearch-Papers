# Prolog STA Premise-Count Analysis: Is s44's ISR=0.885 Real or Artifact?

**Date**: 2026-05-14
**Analyst**: Worker (premise-count artifact check)
**Conclusion**: **s44's ISR=0.885 is 100% artifact** — the model collapsed to single-clause H7 programs. All 3 Prolog STA seeds are negative.

---

## Background

plan006-prolog-sta-s44 reports PR=97%, genuine=100%, ISR=0.885, with 82.5% of samples at ISR=1.0. In FOL experiments (decision D051), what appeared to be "genuine structural improvement" (2.4× ISR over random) was entirely a premise-count artifact: samples with n_prem≤2 have artificially high ISR because LOO mechanics guarantee each premise is "necessary" when there are few of them. After controlling for premise count (n_prem≥3), the ISR advantage collapsed to 1.06× (no real difference).

This analysis applies the same premise-count decomposition to all 3 Prolog seeds.

---

## Data Sources

| Seed | Model Type | Eval File | Test Set |
|------|-----------|-----------|----------|
| s42 | exec-only | `eval_sta_plan006_prolog_exec_s42.json` | B (folio_765…959) |
| s43 (evalA) | STA-trained | `plan006_prolog_sta_s43/eval` | A (folio_340…1295) |
| s43 (evalB) | STA-trained | `plan006_prolog_sta_s43/eval_sta/eval_results.json` | B (folio_765…959) |
| s44 | STA-trained | `plan006_prolog_sta_s44/eval_sta_results.json` | A (folio_340…1295) |

s44 and s43-evalA share the same test set (A). s42 and s43-evalB share test set (B).

---

## 1. s44 — The Critical Analysis

### Premise-Count Distribution

| n_clauses | Total | Proved | Mean ISR (proved) | Mean n_nec | ISR=1.0 count |
|-----------|-------|--------|-------------------|-----------|---------------|
| 1 | 78 | 78 | 1.0000 | 1.00 | 78 |
| 2 | 22 | 19 | 0.5526 | 1.11 | 2 |
| 3+ | 0 | 0 | — | — | 0 |

### Key Finding: 100% of samples have n_clauses ≤ 2

- **78/100 samples** are single-clause H7 programs: one ground fact whose name exactly matches the query (e.g., `no_illustrator_was_american_citizen.` with query `no_illustrator_was_american_citizen`). ISR=1.0 is a tautology — removing the only clause breaks the proof.
- **22/100 samples** have 2 clauses: one H7-style fact + one natural language "explanation" comment parsed as a second clause (e.g., `"This fact represents the statement..."` or `"Explanation: ..."`). The NL comment is always redundant, so ISR=0.5.
- **H7 confirmation**: 78/78 single-clause samples have clause == query (100% H7).
- **Zero samples have n_clauses ≥ 3**. There is no multi-premise reasoning whatsoever.

### ISR Arithmetic Verification

```
78 × 1.0 = 78.0   (single-clause H7, ISR=1.0)
 2 × 1.0 =  2.0   (2-clause, both clauses necessary)
17 × 0.5 =  8.5   (2-clause, 1 necessary)
 3 × 0.0 =  0.0   (failed proofs)
────────────────
Total = 88.5 / 100 = 0.885 ✓ (matches reported mean ISR)
```

### Comparison with FOL D051

| Metric | FOL s42 genuine (n_prem≥3) | Prolog s44 (n_clauses≥3) |
|--------|---------------------------|--------------------------|
| N samples | 34 | **0** |
| Mean ISR | 0.2578 | **N/A** |
| Random baseline | 0.2434 | — |
| Ratio | 1.06× | **Cannot compute** |

In FOL, the artifact was subtle (inflated ISR at n_prem≤2, genuine ISR no better than random at n_prem≥3). In Prolog s44, the artifact is total — the model **entirely avoided multi-clause programs**, making the comparison impossible. This is the most extreme form of Goodhart collapse.

---

## 2. s43 — STA-Trained (Same Test Set as s44)

### Premise-Count Distribution (evalA)

| n_clauses | Total | Proved | Mean ISR (proved) | Mean n_nec | ISR=1.0 count |
|-----------|-------|--------|-------------------|-----------|---------------|
| 1 | 7 | 7 | 1.0000 | 1.00 | 7 |
| 3 | 2 | 0 | — | — | 0 |
| 4 | 5 | 0 | — | — | 0 |
| 5 | 16 | 3 | 0.2000 | 1.00 | 0 |
| 6+ | 70 | 26 | 0.1429 | 1.00 | 0 |

### Key Finding: Multi-clause programs dominate, but n_necessary always = 1

- 81/100 samples have n_clauses ≥ 5 (varied, realistic clause counts)
- **But n_necessary = 1 for every proved sample** — only one clause matters for the proof, all others are redundant
- ISR at n_clauses≥3: **0.1488** (29 proved samples)
- 19.4% of proved samples are single-clause (contributing ISR=1.0 to the mean)

s43 generates structurally richer programs than s44 but fails to make clauses work together logically. The model learned to include many clauses but only one actually participates in the proof — a "shallow enumeration" pattern.

---

## 3. s42 — Exec-Only Baseline

### Premise-Count Distribution (evalB)

| n_clauses | Total | Proved | Mean ISR (proved) | Mean n_nec | ISR=1.0 count |
|-----------|-------|--------|-------------------|-----------|---------------|
| 2 | 2 | 2 | 0.0000 | 0.00 | 0 |
| 3 | 2 | 2 | 0.3333 | 1.00 | 0 |
| 4 | 5 | 5 | 0.0500 | 0.20 | 0 |
| 5 | 4 | 3 | 0.0000 | 0.00 | 0 |
| 6+ | 87 | 74 | 0.0459 | 0.57 | 0 |

### Key Finding: Many clauses generated, almost none necessary

- 91/100 samples have n_clauses ≥ 5 — exec-only model generates verbose programs
- ISR at n_clauses≥3: **0.0513** (84 proved samples)
- Zero samples achieve ISR=1.0
- Pattern: model dumps many related ground facts (20+ clauses), but proof depends on very few

---

## 4. Three-Seed Comparison Summary

### Overall Metrics

| Seed | Training | PR | Mean ISR | Proved-only ISR | Dominant Pattern |
|------|----------|-----|----------|-----------------|-----------------|
| s42 | exec-only | 86% | 0.043 | 0.050 | Verbose enumeration (n_cl≫1, n_nec≈0) |
| s43 | STA | 36% | 0.113 | 0.314 | Shallow enumeration (n_cl varied, n_nec=1) |
| s44 | STA | 97% | 0.885 | 0.912 | **H7 collapse (n_cl=1, trivially ISR=1.0)** |

### Premise-Count Controlled ISR (n_clauses ≥ 3 only)

| Seed | N proved (n_cl≥3) | Mean ISR (n_cl≥3) | ISR=1.0 count |
|------|-------------------|-------------------|---------------|
| s42 exec | 84 | 0.0513 | 0 |
| s43 STA | 29 | 0.1488 | 0 |
| s44 STA | **0** | **N/A** | 0 |
| *FOL s42 genuine* | *34* | *0.2578* | — |
| *FOL random baseline* | *34* | *0.2434* | — |

### Verdict per Seed

- **s42 exec**: ISR≈0 → exec-only generates redundant clause dumps. Low ISR = redundant encoding (C006 applies).
- **s43 STA**: ISR=0.15 at n_cl≥3, always n_necessary=1 → marginally above exec but still degenerate. STA didn't teach structural reasoning; the model "cheats" by making only 1 clause load-bearing.
- **s44 STA**: ISR=0.885 is **entirely artifact** — 100% of programs have n_cl≤2, with 78% being exact H7 single-fact matches. When controlled for premise count: zero multi-clause programs exist, ISR cannot be computed. This is the most extreme Goodhart collapse observed.

---

## 5. Conclusion

### s44's genuine=100% + ISR=0.885: ARTIFACT

The high ISR is not evidence of structural reasoning. It is a mechanical consequence of the model learning to generate the simplest possible program — a single ground fact matching the query — which makes ISR=1.0 trivially guaranteed. The "genuine" classification is vacuously true: with only 1 clause, it is always "necessary" by LOO definition.

### Prolog STA: 0/3 seeds show genuine structural improvement

All three seeds exhibit different failure modes, but none demonstrate that STA training induced real multi-premise logical reasoning:

| Seed | Failure Mode |
|------|-------------|
| s42 | Exec-only → generates many irrelevant clauses, ISR≈0 |
| s43 | STA → only 1 clause is ever necessary regardless of program size |
| s44 | STA → total H7 collapse to single-clause programs |

### Comparison with FOL

In FOL, D051 showed the ISR advantage was an artifact (1.06× when controlling for n_prem). Prolog s44 is even more extreme — the model didn't just benefit from low-premise inflation, it **only generates** low-premise programs. The Goodhart effect in Prolog is more thorough than in FOL: the model found a shorter path to high STA reward (trivial programs) rather than improving structural reasoning.

### Implication for the Paper

ISR as a training signal (STA reward) induces Goodhart's Law in both FOL and Prolog settings. The Prolog results are even stronger evidence: across 3 random seeds, the model consistently finds degenerate strategies to maximize ISR without developing structural reasoning capability. This supports the "Goodhart effect" narrative as a core finding of the paper.
