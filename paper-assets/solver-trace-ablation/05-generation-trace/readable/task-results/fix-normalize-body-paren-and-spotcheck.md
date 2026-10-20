# fix normalize body paren and spotcheck

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_normalize-body-paren-and-spotcheck_20260516T073129_result.json`
- **Structured JSON:** [`8bc2286da8f73ca34090.json`](../../sessions/8b/8bc2286da8f73ca34090.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both folio_732 and folio_959 were in the original 23 genuine (not caught by old H7 detection). Here's the complete report:

---

## Report

### 1. normalize_for_match() fix (lines 73-97)

Added `strip_quantifier_body_parens()` — a new function that iteratively strips redundant parentheses wrapping the body of quantifier chains:

```python
def strip_quantifier_body_parens(s):
    # Matches: ∃x (Body) or ∀x ∃y (Body) etc.
    # Regex: ^((?:[∀∃]\w+\s+)+)\((.+)\)$
    # Strips outer body-parens only when inner content is balanced
    # Loops until no more strippable parens remain (handles nesting)
```

Called in `normalize_for_match()` after `strip_outer_parens_recursive()`, before final whitespace collapse.

Examples:
- `∃x (Hard(x))` → `∃x Hard(x)`
- `∀x (¬A(x))` → `∀x ¬A(x)`
- `∀x (∃y (P(x,y)))` → `∀x ∃y P(x,y)`
- `∃x (ClumsyFoodie(x) ∧ GoesOutFrequently(x))` → `∃x ClumsyFoodie(x) ∧ GoesOutFrequently(x)`

Safe: won't strip function-call parens like `Hard(x)`, and won't strip when inner parens are unbalanced (e.g., `∃x (A(x)) ∧ B(x)`).

### 2. plan002-additive-b01-s42 (14 genuine)

**0 body-paren H7 misses** among all 81 proved samples. The 14 genuine remains **14**.

### 3. exp1-isr-b03-s43-r3 (23 genuine → remaining after audit)

**1 NEW body-paren H7 miss** (beyond already-confirmed folio_732):

| ID | Index | Premise | Conclusion | Match |
|---|---|---|---|---|
| folio_732 | 86 | `∃x (Hard(x))` | `∃x Hard(x)` | already confirmed |
| **folio_959** | **99** | `∃x ClumsyFoodie(x) ∧ GoesOutFrequently(x)` | `∃x (ClumsyFoodie(x) ∧ GoesOutFrequently(x))` | **NEW** |

Corrected genuine:
- Original: 23
- − folio_558 (H8): 22
- − folio_732 (body-paren H7): 21
- − folio_959 (body-paren H7): **20**

---
