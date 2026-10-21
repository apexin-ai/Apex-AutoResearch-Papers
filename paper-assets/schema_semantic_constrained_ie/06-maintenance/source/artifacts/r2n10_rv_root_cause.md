# R2-N10: Residual RV (0.03%) Root Cause Analysis

## Experiment
- **Run**: `phase2_docred_full_s1` (Qwen3-8B, DocRED, full_s1 constrained decoding)
- **RV rate**: 5/17341 = 0.0288%
- **xgrammar version**: 0.1.33

## Violation Cases

All 5 violations come from **a single document** ("Souvlaki") and produce the **same chimeric relation name**.

| # | doc_id | predicted_relation | head | tail | head_type | tail_type |
|---|--------|-------------------|------|------|-----------|-----------|
| 1 | Souvlaki | membericipant of | Souvlaki | pork | MISC | MISC |
| 2 | Souvlaki | membericipant of | Souvlaki | chicken | MISC | MISC |
| 3 | Souvlaki | membericipant of | Souvlaki | beef | MISC | MISC |
| 4 | Souvlaki | membericipant of | Souvlaki | lamb | MISC | MISC |
| 5 | Souvlaki | membericipant of | Souvlaki | fish | MISC | MISC |

### Valid relation names the model likely intended
- "member of" (P463) — valid pairs include (MISC, MISC) via rare usage
- "participant of" (P1344) — valid pairs do NOT include (MISC, MISC)
- Also in ontology: "member of sports team" (P54), "member of political party" (P102)

## Token-Level Mechanism

Qwen3-8B tokenization:
```
"member of"          → [9597("member"), 315(" of")]
"participant of"     → [58513("participant"), 315(" of")]
"membericipant of"   → [9597("member"), 21757("icipant"), 315(" of")]
```

The chimera "membericipant of" is formed by concatenating:
1. Token 9597 = "member" (valid start of "member of")
2. Token 21757 = "icipant" (subword fragment of "participant")
3. Token 315 = " of" (shared suffix)

## Root Cause: XGrammar Enum Automaton Bug

### Confirmed via reproduction

After feeding `{"type": "` + token "member" (9597) to xgrammar's GrammarMatcher, the token bitmask reveals **8 allowed tokens**:

```
After "member", allowed tokens:
  72:    'i'
  220:   ' '
  292:   'ic'
  297:   ' o'
  315:   ' of'        ← correct (completes "member of")
  3375:  'ici'
  8442:  'icip'
  21757: 'icipant'    ← BUG (from "participant", a different enum entry)
```

After "member", xgrammar should ONLY allow tokens continuing " of" (since "member of", "member of sports team", and "member of political party" all continue with " of"). Instead, it also allows "i", "ic", "ici", "icip", "icipant" — all prefixes/completions of the substring "icipant" from the unrelated enum entry "participant".

### State corruption propagates

After accepting "member" + "icipant" = "membericipant" (not a prefix of any valid enum entry), xgrammar allows:
```
After "membericipant", allowed tokens (14):
  1:     '"'          ← closing quote (accepts "membericipant" as complete!)
  315:   ' of'        ← continues to "membericipant of"
  21757: 'icipant'    ← ANOTHER "icipant" (recursive corruption)
  ...
```

The automaton has completely lost track of its position within the enum values.

### Why TypeConstraintProcessor (Layer 2) doesn't catch this

The TypeConstraintProcessor handles:
- `ENTITY_TYPE` → masks invalid entity types
- `RELATION_HEAD_TYPE` → constrains head_type by relation's domain
- `RELATION_TAIL_TYPE` → constrains tail_type by (relation, head_type)

It does **NOT** handle `RELATION_TYPE` — relation name strings are entirely delegated to xgrammar (Layer 1). There is no `elif position == FieldPosition.RELATION_TYPE:` branch in the `__call__` method.

The safety net (`_GRAMMAR_MASK_THRESHOLD` bypass) is also irrelevant here — it only applies to entity type masking when semantic constraints would block all grammar-valid tokens.

## Paper Agent's Description Assessment

**Current text**: "tokenization edge cases where multi-token relation names span grammar-state boundaries"

**Accuracy**: Partially correct but imprecise and potentially misleading.

### What's right
- It IS a tokenization issue (token "icipant" existing as a standalone subword)
- It IS related to multi-token enum values
- It IS about grammar state boundaries in a loose sense

### What's wrong/misleading
- "span grammar-state boundaries" implies the issue is at the boundary between grammar states (e.g., between relation type field and the next field), when the actual issue is WITHIN a single field's enum matching
- The description doesn't capture the chimeric nature: it's not that a valid relation name spans a boundary incorrectly, but that fragments from two different enum entries get concatenated
- It omits the critical detail that this is an xgrammar library bug, not an inherent limitation of constrained decoding

### Suggested revision

**Option A** (concise, suitable for a footnote or parenthetical):
> an edge case in XGrammar's byte-level enum automaton where a subword token valid for one enum entry ("icipant" from "participant of") is incorrectly admitted after a prefix token from a different entry ("member" from "member of"), producing the chimeric string "membericipant of"

**Option B** (brief, suitable for inline text):
> a rare XGrammar automaton bug where subword tokens from different enum entries combine into chimeric values (e.g., "member" + "icipant" + " of" from "member of" and "participant of")

**Option C** (if you want to keep it vague but accurate):
> a known edge case in the grammar engine's enum constraint enforcement where token-level mask computation admits subword fragments from unrelated enum entries

## Additional Notes

- All 5 violations repeat the same chimeric string for 5 different (head, tail) pairs in the same document, suggesting the model entered a "stuck pattern" after the first chimera was accepted
- The bug may be version-specific to xgrammar 0.1.33; newer versions may have fixed the enum automaton
- A potential mitigation (without upgrading xgrammar) would be adding relation-type validation to TypeConstraintProcessor Layer 2 as a secondary check
