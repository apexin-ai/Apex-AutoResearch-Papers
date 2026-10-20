# D063: GoLLIE-7B Schema Violation Rate on SciERC

## Experiment Setup

- **Model**: GoLLIE-7B (HiTZ/GoLLIE-7B, based on CodeLlama-7B)
- **Task**: Zero-shot SciERC information extraction (6 entity types, 7 relation types)
- **Data**: SciERC test set, 100 documents (551 sentences)
- **Prompt Format**: Python dataclass definitions (GoLLIE native format) with task guidelines
- **Inference**: Greedy decoding (num_beams=1, do_sample=False), max_new_tokens=512
- **GPU**: Single GPU (cuda:0), bfloat16 precision

## Schema Violation Rate Comparison

| Metric | GoLLIE-7B | OntoCoDec Unconstrained | OntoCoDec Constrained (S1) |
|--------|-----------|------------------------|---------------------------|
| DR%    | 0.00      | 15.37                  | 0.93                      |
| RV%    | 0.00      | 1.39                   | 0                         |
| ET%    | 0.00      | 0.40                   | 0                         |
| CF%    | 0.67      | 0.08                   | 9.90                      |

**Metric definitions**:
- DR (Domain-Range): Relation with head/tail entity type pair not in the ontology's valid_pairs
- RV (Relation Vocabulary): Relation type not in the defined schema
- ET (Entity Type): Entity type not in the defined schema
- CF (Cross-Field): Same entity text assigned different types within a document

## Key Findings

### GoLLIE achieves 0% on ET, RV, and DR

GoLLIE's Python dataclass output format acts as an implicit schema constraint. Entity types and relation types are defined as Python class names, so the model can only produce instances of defined classes. This structural constraint eliminates type vocabulary violations (ET=0%, RV=0%). The 0% DR rate indicates all 7 extracted relations have valid domain-range pairs.

### Low CF rate (0.67%)

Only 2 entity texts were assigned conflicting types within their respective documents (out of 300 total entities). This compares favorably to OntoCoDec unconstrained (0.08%) but is much lower than OntoCoDec constrained (9.90%), where the constraint enforcement paradoxically introduces some cross-field inconsistency.

### Critical caveat: Extremely low extraction coverage

GoLLIE's violation rates must be interpreted alongside its extraction coverage:

| Statistic | Value |
|-----------|-------|
| Total entities extracted | 300 |
| Total relations extracted | 7 |
| Documents with empty output | 45/100 (45%) |
| Documents with any relations | 2/100 (2%) |

The SciERC test set ground truth contains ~1,400 entities and ~800 relations. GoLLIE in zero-shot mode extracts only 21% of entities and <1% of relations. The DR/RV rates are computed over just 7 relations, making them statistically unreliable.

### Entity type distribution

| Type | Count |
|------|-------|
| Method | 160 |
| Task | 52 |
| Material | 38 |
| OtherScientificTerm | 32 |
| Generic | 10 |
| Metric | 8 |
| **Total** | **300** |

GoLLIE shows a strong bias toward Method (53% of entities), while the ground truth has a more balanced distribution.

## Interpretation for Paper

GoLLIE demonstrates that structured code-generation formats can achieve perfect type-level schema compliance (ET=0%, RV=0%) by design. However, this comes at a steep cost in extraction coverage: the model generates very few annotations in zero-shot mode, particularly for relations. The comparison highlights a fundamental tradeoff:

1. **GoLLIE's approach** (code-format prompting): Zero schema violations by construction, but very low recall
2. **OntoCoDec unconstrained** (natural language prompting): Higher coverage but measurable schema violations (DR=15.37%, RV=1.39%, ET=0.40%)
3. **OntoCoDec constrained** (S1 semantic constraints): Eliminates most violations while maintaining coverage, at the cost of increased CF (9.90%)

This suggests that schema compliance via output format alone is necessary but not sufficient. Effective schema-constrained IE requires both format-level compliance and content-level coverage, which is what OntoCoDec's semantic constraints aim to achieve.

## Raw Output Files

- Raw model outputs: `outputs/gollie_scierc/raw_outputs.jsonl`
- Violation computation results: `outputs/gollie_scierc/violation_results.json`
- Guidelines module: `outputs/gollie_scierc/scierc_guidelines.py`
- Inference script: `scripts/gollie_scierc_inference.py`