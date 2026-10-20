# M3+Q3: Why Semantic-only Increases DocRED ET by +70%

## 1. The Numbers

| Dataset | Mode | ET violations | Total entities | ET rate |
|---------|------|--------------|----------------|---------|
| DocRED | Unconstrained | 500 | 20,171 | 2.48% |
| DocRED | Semantic-only | 851 | 20,185 | 4.22% |
| SciERC | Unconstrained | 10 | 2,474 | 0.40% |
| SciERC | Semantic-only | 10 | 2,474 | 0.40% |

DocRED semantic-only: +351 extra ET violations (+70%). SciERC: unchanged.

## 2. Where the Extra Violations Come From

Decomposing DocRED ET violations by source:

| Mode | Entity-list violations | Relation head/tail_type violations | Total |
|------|----------------------|-----------------------------------|-------|
| Unconstrained | 496 | 4 | 500 |
| Semantic-only | 496 | 355 | 851 |

The entity list is **identical** between the two modes (same 496 OOV types: EVENT=261, WORK=121, ETHNIC_GROUP=64, etc.). All 355 extra violations come from relation `head_type`/`tail_type` fields.

Top OOV types appearing only in semantic-only relation fields:
- `ORGB` (57), `OR` (48): truncated/garbled versions of "ORG"
- `EVENT` (55), `WORK` (55): model-invented types
- `ENTITY_TYPE` (22): literal string, model confused about what to generate
- `GENRE` (20), `JOB` (17), `MSC` (12): novel OOV types

## 3. Root Cause: D/R Mask Without Grammar Creates OOV Escape Path

### 3.1 How `_apply_type_mask` works (type_mask_processor.py:357-369)

```python
def _apply_type_mask(self, logits, allowed_types):
    disallowed_first_tokens = [
        tid for etype, tid in self._type_first_token.items()
        if etype not in allowed_types
    ]
    if disallowed_first_tokens:
        logits[disallowed_first_tokens] = float("-inf")
    return logits
```

This only masks the first tokens of **disallowed entity types** (6 tokens total for DocRED). The remaining ~150k vocabulary tokens are untouched. In `full_s1` mode, XGrammar's enum constraint guarantees the output is one of the 6 valid types. Without grammar (semantic-only), the model can escape to any of the ~150k unmasked tokens.

### 3.2 The failure path in semantic-only mode

1. Model generates a relation and reaches the `head_type` field
2. `_mask_head_type` looks up D/R constraints for the current relation type
3. D/R mask blocks certain entity type first tokens (e.g., blocks PER, TIME, NUM for relation P131)
4. Without XGrammar, the model is free to pick any non-entity-type token
5. Model generates OOV strings like "ORGB", "GENRE", "JOB" instead of a valid type

### 3.3 Why the entity list is unaffected

At entity type position, `_mask_entity_type` allows **all** entity types:
```python
def _mask_entity_type(self, logits):
    return self._apply_type_mask(logits, set(self.spec.entity_types))
```
Since all types are allowed, no tokens are blocked, and the function is a no-op. Entity-list types are generated identically to unconstrained mode.

## 4. Why SciERC is Unaffected: Zero Type-Level Blocking

### 4.1 Constraint space geometry

| Metric | SciERC | DocRED |
|--------|--------|--------|
| Entity types | 6 | 6 |
| Relation types | 7 | 96 |
| Avg valid pairs per relation | 24.0/36 (66.7%) | 5.7/36 (15.8%) |
| **Max type-level head blocking** | **0%** | **92% (NUM)** |
| **Max type-level tail blocking** | **0%** | **96% (NUM)** |

### 4.2 Type-level blocking comparison

**SciERC**: Every entity type appears as a valid head and valid tail for **every** relation (0% blocking for all 6 types across all 7 relations). The D/R mask at head_type/tail_type positions is always a no-op because `valid_head_types()` and `valid_tail_types()` always return all 6 types.

**DocRED**: Entity types are frequently blocked:
- NUM: blocked as head in 92/96 relations (92%), as tail in 96%
- TIME: blocked as head in 88%, tail in 83%
- PER: blocked as head in 27%, tail in 55%
- ORG/LOC/MISC: blocked as head in 20-24%, tail in 31-42%

With 96 relations and high blocking rates, there are many opportunities for the model to be forced away from the correct entity type and escape to an OOV string.

### 4.3 Summary

SciERC's constraint structure is **pair-restrictive but type-permissive**: individual (head_type, tail_type) pairs are constrained (66.7% valid), but no entity type is ever completely excluded from any relation's head or tail position. The D/R mask operates at the **type level** (blocking first tokens), not the pair level, so it has nothing to block.

DocRED's constraint structure is **type-restrictive**: many entity types are entirely excluded from many relations' head/tail positions. The D/R mask actively blocks entity type tokens, and without grammar to contain the output within the enum, the model escapes to OOV types.

## 5. Suggested Paper Text

> In semantic-only mode, the domain/range mask blocks specific entity-type tokens at head\_type and tail\_type positions but cannot prevent the model from generating out-of-vocabulary types, as no grammar layer constrains the output to the type enum. On DocRED, where 84% of (relation, entity-type) combinations are blocked by domain/range rules, this creates frequent "escape paths" to OOV types, accounting for the +70% ET increase. On SciERC, every entity type is a valid head and tail for every relation, so the mask is never triggered and ET remains unchanged.

## 6. Verification Details

### Data sources
- DocRED unconstrained: `outputs/docred_unconstrained.jsonl`
- DocRED semantic-only: `outputs/docred_semantic_only.jsonl`
- Violation reports: `outputs/violation_report_docred_{unconstrained,semantic_only}_v2.json`
- Constraint files: `data/docred/ontology_constraints_docred.json`, `ontology_constraints.json`

### Code references
- `_apply_type_mask`: `compiler/type_mask_processor.py:357-369`
- `_mask_entity_type`: `compiler/type_mask_processor.py:288-296`
- `_mask_head_type`: `compiler/type_mask_processor.py:298-319`
- `PositionDetector.detect`: `compiler/type_mask_processor.py:120-173`
- Semantic-only processor stack: `run_constrained_extraction.py:435-437`
- ET violation counting (DocRED v2): `violation_checker_docred.py:109-154` (counts unique (text, type) from both entity list and relation head/tail fields)
