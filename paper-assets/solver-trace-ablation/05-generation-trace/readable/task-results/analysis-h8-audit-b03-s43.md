# analysis h8 audit b03 s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_h8-audit-b03-s43_20260516T071533_result.json`
- **Structured JSON:** [`0539133edde31d989cd7.json`](../../sessions/05/0539133edde31d989cd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Audit complete. Here's the report.

---

## H8 Conjunction Collapse Audit — exp1-isr-b03-s43-r3

### Result: 1 H8 found out of 23 genuine

**Corrected genuine: 22/86 = 25.6%** (was 23/86 = 26.7%)

### H8 Sample

**folio_558** (ISR=0.6667)
```
P1: ∀x (¬AdministersInternationally(x))
P2: ∃x AdministersInternationally(x)
C:  ∃x AdministersInternationally(x) ∧ ∀x ¬AdministersInternationally(x)
```
Conclusion = P2 ∧ P1. Classic conjunction collapse — model just AND'd both premises as the conclusion.

**Root cause of automated detection miss**: `normalize_for_match()` in classify_h7.py doesn't strip body-parens after quantifiers. So `∀x (¬A(x))` (premise) ≠ `∀x ¬A(x)` (conjunct) during matching, even though they're identical.

### Additional classifier bugs found (same normalization issue)

| Sample | Type | Issue |
|--------|------|-------|
| folio_732 | H7 miss | P1=`∃x (Hard(x))`, C=`∃x Hard(x)` — tautology missed due to parens |
| folio_959 | H1-near | P2=`∃x ClumsyFoodie(x) ∧ GoesOut(x)`, C=`∃x (ClumsyFoodie(x) ∧ GoesOut(x))` — parens diff |

Per C013, H1-near stays genuine but should be tagged. folio_732 is a true H7 miss (would reduce genuine to 21 if fixed).

### Borderline case examined but NOT classified as H8

**folio_212** (ISR=0.6667): C=`∃x SonOfGP(x) ∧ ¬Author(x)`. Second conjunct `¬Author(x)` is a ∀-instantiation of P1, not P1 itself. Trivial proof but doesn't meet the strict "C = P1 ∧ P2" criterion.

### Recommended fix

`normalize_for_match()` should use `parse_quantifier_chain()` to strip body-parens after quantifiers before comparison. This would fix folio_558 (H8), folio_732 (H7), and folio_959 (H1-near) detection.

---
