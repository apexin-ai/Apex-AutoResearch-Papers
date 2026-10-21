# R8-N1: Quantifier Proportion Analysis

## Motivation

Reviewer concern: constraints labeled "FOL" are mostly propositional ground clauses.
This analysis quantifies constraint types across 3 conditions (2 models × 2 datasets, 73K+ constraints).

## Classification

| Category | Definition | Z3 Encoding |
|----------|-----------|-------------|
| **Quantified** | Contains `ForAll`/`Exists` in Z3 formula | True first-order |
| **Grounded FOL** | Predicate-variable syntax `P(X) -> Q(X)` | Grounded to Bool vars |
| **Ground Atom** | Predicate with constants `student(bonnie)` | Bool var |
| **Propositional** | No predicate structure `p -> q` | Bool var |

## Detailed Breakdown

| Condition | Total | Quantified | Grounded FOL | Ground Atom | Propositional |
|-----------|-------|------------|--------------|-------------|---------------|
| Mistral-7B × FOLIO | 14084 | 429 (3.0%) | 4680 (33.2%) | 7461 (53.0%) | 1514 (10.8%) |
| Qwen2.5-14B × FOLIO | 5208 | 40 (0.8%) | 1976 (37.9%) | 1759 (33.8%) | 1433 (27.5%) |
| Mistral-7B × ProofWriter | 53972 | 286 (0.5%) | 25705 (47.6%) | 23806 (44.1%) | 4175 (7.7%) |
| **Aggregate** | **73264** | **755 (1.0%)** | **32361 (44.2%)** | **33026 (45.1%)** | **7122 (9.7%)** |

## Collapsed: Quantified vs Effectively Propositional

| Condition | Total | Truly Quantified (FOL) | Effectively Propositional |
|-----------|-------|------------------------|--------------------------|
| Mistral-7B × FOLIO | 14084 | 429 (3.0%) | 13655 (97.0%) |
| Qwen2.5-14B × FOLIO | 5208 | 40 (0.8%) | 5168 (99.2%) |
| Mistral-7B × ProofWriter | 53972 | 286 (0.5%) | 53686 (99.5%) |
| **Aggregate** | **73264** | **755 (1.0%)** | **72509 (99.0%)** |

**Key finding**: Only **1.0%** of constraints use Z3 quantifiers.
The remaining **99.0%** are propositional at the solver level, regardless of surface notation.

## Examples

### Mistral-7B × FOLIO

**quantified** (429):
- `ForAll(X, gentleman(X) -> handsome(X))`
- `ForAll(X, CEO(X) -> gentleman(X))`
- `gre_cost(X) <= 300`

**grounded_fol** (4680):
- `performs_in_school_talent_shows_often(X) -> attends_and_engaged_with_school_events(X) & student(X)`
- `performs_in_school_talent_shows_often(X) | inactive_and_disinterested_member(X)`
- `chaperones_high_school_dances(X) -> !student(X)`

**ground_atom** (7461):
- `school_talent_show(bonnie)`
- `Unknown(performs_in_school_talent_shows_often_bonnie)`
- `performs_school_talent_shows(bonnie) -> attends_school_events(bonnie) & engaged_school_events(bonnie)`

**propositional** (1514):
- `young_children_and_teenagers_who_wish_to_further_their_academic_careers_and_educational_opportunities -> student_attends_school_X`
- `Bonnie -> (attends_school_events_and_engaged_Bonnie or not_attends_school_events_and_not_engaged_Bonnie)`
- `Or(And(attends_bonnie, very_engaged_bonnie), Not(And(attends_bonnie, very_engaged_bonnie)))`

### Qwen2.5-14B × FOLIO

**quantified** (40):
- `some_objects_of_worship_are_fir_trees`
- `some_evergreens_are_objects_of_worship`
- `some_evergreens_are_not_objects_of_worship`

**grounded_fol** (1976):
- `perform_often(X) -> attend_engaged(X)`
- `perform_often(X) | inactive_disinterested(X)`
- `chaperone_dances(X) -> not_student(X)`

**ground_atom** (1759):
- `Not(perform_often(bonnie))`
- `(attend_engaged(bonnie) & student_attends_school(bonnie)) | (Not(attend_engaged(bonnie)) & Not(student_attends_school(bonnie)))`
- `perform_often(bonnie)`

**propositional** (1433):
- `P -> A`
- `P ∨ I`
- `C -> S'`

### Mistral-7B × ProofWriter

**quantified** (286):
- `furry(person)`
- `Forall(x, (quiet(x) & furry(x)) -> green(x))`
- `Forall(x, (big(x) & quiet(x)) -> Not(smart_x))`

**grounded_fol** (25705):
- `smart(X) -> nice(X)`
- `big(X) & quiet(X) -> Not(smart(X))`
- `quiet(X) & smart(X) -> round(X)`

**ground_atom** (23806):
- `green(furry_erin)`
- `smart(erin)`
- `big(green_erin)`

**propositional** (4175):
- `Not(furry_erin)`
- `Not(quiet_dave) V Or(smart_dave, Not(smart_dave))`
- `Not(round_dave)`

## Interpretation

The reviewer is correct: **99.0%** of constraints are effectively propositional.
The "FOL" notation is a structured extraction format — the LLM outputs predicate-argument expressions
which are then propositionally grounded for MaxSAT solving. Only 1.0% of 
constraints actually use Z3's first-order quantifiers (ForAll/Exists).

**Recommended paper revision**: Replace "FOL constraints" with "symbolic constraints in predicate notation"
or "propositionalized constraints" to accurately reflect the solver-level representation.
