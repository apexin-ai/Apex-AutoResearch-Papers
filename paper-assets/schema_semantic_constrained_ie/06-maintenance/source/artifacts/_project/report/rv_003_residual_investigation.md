# RV=0.03% Residual Investigation (R2-N10)

## Summary

**Root cause: XGrammar v0.1.33 bug in JSON schema enum compilation.**

The grammar layer incorrectly allows token sequences that produce strings not in the enum set. Specifically, after accepting token "member" (id=9792), the grammar allows token "icipant" (id=22505), producing the nonexistent relation `"membericipant of"`.

## Affected Experiments

| Experiment | RV violations | Total triples | RV rate |
|---|---|---|---|
| phase2_docred_grammar_only | 5 | 17341 | 0.03% |
| phase2_docred_full_s1 | 5 | 17341 | 0.03% |

All 5 violations are in **one document** ("Souvlaki"), same corrupted relation.

## Violating Triples

All from doc "Souvlaki":

| head | tail | relation (generated) | expected valid |
|---|---|---|---|
| Souvlaki | pork | membericipant of | member of / participant of |
| Souvlaki | chicken | membericipant of | member of / participant of |
| Souvlaki | beef | membericipant of | member of / participant of |
| Souvlaki | lamb | membericipant of | member of / participant of |
| Souvlaki | fish | membericipant of | member of / participant of |

## Mechanism

Tokenization (Llama-3.1 BPE):
- `"member of"` → [9792("member"), 315(" of")]
- `"participant of"` → [59613("participant"), 315(" of")]
- `"membericipant of"` → [9792("member"), 22505("icipant"), 315(" of")]

After accepting token 9792 ("member"), XGrammar's bitmask allows 8 tokens:

```
Allowed after "member:
  72:    'i'
  220:   ' '
  292:   'ic'
  297:   ' o'
  315:   ' of'       ← correct (continues "member of")
  3457:  'ici'
  8608:  'icip'
  22505: 'icipant'   ← BUG (leaks from "participant of")
```

Tokens `[i, ic, ici, icip, icipant]` are byte-prefixes of "icipant" from the enum value "participant of". XGrammar's internal byte-level automaton incorrectly branches into a different enum value's suffix after matching a shared-nothing prefix.

## Reproduction

```python
import xgrammar as xgr
# ... (compile grammar with DocRED schema) ...
matcher = xgr.GrammarMatcher(compiled)
matcher.accept_token(quote_id)    # "
matcher.accept_token(9792)        # member
assert matcher.accept_token(22505) == True  # icipant — should be False!
```

## Why w8 (finetuned) Experiments Show RV=0

The finetuned models (w8_llama/qwen_docred_ft_grammar_only) have near-zero probability mass on token 22505 after "member" in this context, so the bug never manifests. The base model (phase2) has higher entropy and occasionally selects the spurious token when XGrammar fails to mask it.

## Verdict

- **Not a checker bug** — the checker correctly identifies these as violations
- **Not a CFG coverage issue** — the schema enum is complete
- **XGrammar v0.1.33 enum compilation bug** — allows cross-enum token leakage
- **Impact**: negligible (5/17341 = 0.03%, single document, base model only)
- **Fix**: upgrade XGrammar (check if fixed in newer versions), or add post-hoc validation as defense-in-depth
- **For paper reporting**: can legitimately report "RV≈0% under grammar constraint" with footnote noting 5 residual triples from XGrammar tokenizer edge case
