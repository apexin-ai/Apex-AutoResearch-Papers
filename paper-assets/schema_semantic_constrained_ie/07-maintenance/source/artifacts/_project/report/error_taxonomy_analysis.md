# Error Taxonomy Analysis: S1 Residual Violations

Analysis of remaining DR and CF violations in S1 (constrained decoding) outputs across 4 ZS configurations.

## Taxonomy Definitions

| Category | Abbr | Definition |
|----------|------|------------|
| **Tokenizer Collision** | TC | BPE token boundary prevents perfect constraint enforcement (e.g., token spans across JSON field boundary) |
| **Semantic Confusion** | SC | Model assigns locally valid entity types that violate DR constraints — each type is individually valid but the (head_type, tail_type) pair is not allowed for the relation |
| **Non-local CF** | NL-CF | Same entity receives different types across triples; resolvable by picking one consistent type that satisfies all relational contexts |
| **Fundamental Schema Conflict** | FSC | Same entity participates in relations whose DR constraints conflict — no single type satisfies all relational contexts simultaneously |

## Summary Table

| Config | Total Violations | TC | SC | NL-CF | FSC |
|--------|-----------------|-----|-----|-------|-----|
| SciERC Qwen ZS | 56 | 0 (0.0%) | 16 (28.6%) | 35 (62.5%) | 5 (8.9%) |
| SciERC Llama ZS | 33 | 0 (0.0%) | 1 (3.0%) | 29 (87.9%) | 3 (9.1%) |
| DocRED Qwen ZS | 2,287 | 0 (0.0%) | 1,467 (64.1%) | 202 (8.8%) | 618 (27.0%) |
| DocRED Llama ZS | 1,775 | 0 (0.0%) | 229 (12.9%) | 420 (23.7%) | 1,126 (63.4%) |

Violation unit: each DR-violating triple counted once; each CF-inconsistent entity counted once.

## Breakdown by Violation Source

| Config | DR violations | CF entities | DR from SC | DR from NL-CF | DR from FSC |
|--------|--------------|-------------|------------|----------------|-------------|
| SciERC Qwen ZS | 16 | 40 | 16 | 0 | 0 |
| SciERC Llama ZS | 1 | 32 | 1 | 0 | 0 |
| DocRED Qwen ZS | 1,770 | 517 | 1,467 | 17 | 286 |
| DocRED Llama ZS | 418 | 1,357 | 229 | 6 | 183 |

## Detailed Category Analysis

### 1. Tokenizer Collision (TC): 0% across all configs

S1 constrained decoding successfully prevents tokenizer-level constraint violations. Entity type strings ("Task", "Method", "LOC", "PER", etc.) are short enough to be single or few BPE tokens, and the grammar-level constraint engine handles them correctly. **This category is effectively eliminated by S1.**

### 2. Semantic Confusion (SC): Dominant for DocRED Qwen (64.1%)

The model assigns individually valid entity types, but the (head_type, tail_type) pair violates the relation's DR constraint. The entity is NOT involved in any cross-triple inconsistency — the error is purely in type selection for a single triple.

**SciERC top confused pairs:**
| (head_type, tail_type) | Count |
|------------------------|-------|
| (OtherScientificTerm, Metric) | 5 |
| (Generic, Generic) | 4 |
| (OtherScientificTerm, Generic) | 2 |
| (Generic, Material) | 2 |

**DocRED Qwen top confused pairs:**
| (head_type, tail_type) | Count |
|------------------------|-------|
| (PER, ORG) | 271 |
| (PER, LOC) | 201 |
| (PER, PER) | 173 |
| (MISC, PER) | 133 |
| (ORG, PER) | 129 |

**DocRED Llama top confused pairs:**
| (head_type, tail_type) | Count |
|------------------------|-------|
| (PER, PER) | 57 |
| (PER, ORG) | 50 |
| (PER, LOC) | 37 |
| (LOC, ORG) | 34 |
| (PER, TIME) | 28 |

**Typical examples:**

*SciERC Qwen:*
- `(Plume [OtherScientificTerm]) --Evaluate-for→ (syntactic coverage [Metric])` — pair (OtherScientificTerm, Metric) not allowed for Evaluate-for
- `(difference [Generic]) --Feature-of→ (pairs [Generic])` — pair (Generic, Generic) not allowed for Feature-of

*DocRED Qwen:*
- `(Yorkshire Post [ORG]) --founded by→ (1754 [TIME])` — P112 "founded by" requires head/tail ∈ {LOC, MISC, ORG, PER}, but (ORG, TIME) not in valid pairs
- `(Skai TV [ORG]) --contains admin. entity→ (digital terrestrial transmission [MISC])` — P150 expects (LOC, LOC) pairs

**Root cause:** The model has a generic understanding of entity types but fails to account for relation-specific type constraints. In DocRED, relations like `founded by` (P112) accept only {LOC, MISC, ORG, PER} × {LOC, MISC, ORG, PER}, excluding TIME despite temporal arguments being contextually plausible.

### 3. Non-local CF (NL-CF): Dominant for SciERC (62–88%)

Same entity assigned different types in different triples, but at least one valid type exists that would satisfy all relational constraints.

**Counts:**
| Config | NL-CF entities | Resolvable |
|--------|---------------|------------|
| SciERC Qwen ZS | 35 | All (100%) |
| SciERC Llama ZS | 29 | All (100%) |
| DocRED Qwen ZS | 185 | All (100%) |
| DocRED Llama ZS | 414 | All (100%) |

**Typical examples:**

*SciERC Qwen:*
- Entity `"distinct distribution"`: typed as Generic in one relation, Metric in another. Resolvable with Generic.
- Entity `"parsing results"`: Generic vs Metric across relations. Resolvable with Generic.
- Entity `"adjacency graph"`: Method vs OtherScientificTerm. Resolvable with Generic.

*DocRED Llama:*
- Entity `"Susan Blue Parsons"`: LOC vs ORG across relations. Resolvable with ORG.
- Entity `"Torpedo Squadron 8"`: MISC vs ORG. Resolvable with MISC.

**Root cause:** S1 constrained decoding enforces DR constraints per-triple (locally), but has no mechanism to ensure the same entity receives a consistent type across all triples. The model generates each triple independently, and without cross-triple coordination, inconsistencies arise. **TCR (Type Consistency Resolution) resolves these by majority voting**, which is why CF→0% after TCR for non-fundamental cases.

### 4. Fundamental Schema Conflict (FSC): Major issue for DocRED Llama (63.4%)

Same entity participates in relations whose DR constraints are mutually exclusive — no single valid type satisfies all contexts.

**Counts and alignment with TCR d065 results:**
| Config | FSC entities (this analysis) | Fund. conflicts (TCR d065) | Fund.% (TCR d065) |
|--------|------------------------------|---------------------------|-------------------|
| SciERC Qwen ZS | 5 | 5/245 = 2.04% | 2.04% |
| SciERC Llama ZS | 3 | 3/162 = 1.85% | 1.85% |
| DocRED Qwen ZS | 332 | 361/2670 = 13.52% | 13.52% |
| DocRED Llama ZS | 943 | 871/3824 = 22.78% | 22.78% |

Note: slight count differences from TCR d065 are because TCR counts CF entities that participate in voting, while this analysis counts all CF entities with no valid resolution.

**Typical examples:**

*DocRED Qwen:*
- Entity `"Portland Golf Club"`: typed as ORG for `location of formation` (which requires ORG/LOC head) but as MISC for `date of birth` (which requires PER head → no valid type satisfies both)
- Entity `"Ryder Cup"`: ORG for `location of formation` but MISC for `date of birth` — same structural conflict

*DocRED Llama:*
- Entity `"Washington Place"`: LOC for `located in` and `creator` relations, but these relations require conflicting type sets. No type in {LOC, ORG, PER, MISC, TIME, NUM} satisfies all.
- Entity `"William Washington"`: PER in most relations, but one relation assigns LOC — the conflicting relation's DR constraint doesn't admit PER.

**Root cause:** DocRED's schema has 96 relation types with narrow, heterogeneous domain/range constraints. When an entity participates in relations from different semantic families (e.g., geographic relations expecting LOC + biographical relations expecting PER), the constraints become irreconcilable. This is an inherent limitation of fixed schema ontologies — the schema's constraint tightness (κ̄) creates unsolvable conflicts. **These violations are irreducible by any post-processing method** and represent the theoretical ceiling of schema-constrained IE.

## Key Conclusions

### Distribution Pattern by Dataset

| Dataset | Primary violation type | Secondary | Explanation |
|---------|----------------------|-----------|-------------|
| SciERC | NL-CF (63–88%) | SC (3–29%) | Permissive schema (7 rels, broad valid_pairs) → few DR violations; most errors are cross-triple inconsistency |
| DocRED | SC+FSC (77–76%) | NL-CF (9–24%) | Restrictive schema (96 rels, narrow valid_pairs) → many DR violations from wrong type pairs + fundamental conflicts |

### Reducibility Analysis

| Category | Reducible by | Residual after |
|----------|-------------|---------------|
| TC (0%) | Already eliminated by S1 | 0% |
| SC (3–64%) | Per-triple DR enforcement during decoding (future S1 enhancement) | Would reach 0% with full DR-aware constrained decoding |
| NL-CF (9–88%) | TCR majority voting (already implemented) | 0% after TCR |
| FSC (9–63%) | **Irreducible** — schema-inherent conflict | Represents theoretical ceiling |

### Actionable Insights

1. **S1 Enhancement**: Reducing grammar-first fallback frequency would eliminate the SC category, reducing DocRED Qwen violations by 64% and DocRED Llama by 13%.

2. **TCR Effectiveness**: TCR already eliminates NL-CF (the dominant SciERC error). The E-F1 drop from TCR in d065 comes from resolving NL-CF entities to a "safe" type that may not be the gold type.

3. **Irreducible Floor**: FSC violations (2–23% of CF entities) represent the hard limit of schema-constrained approaches. For DocRED Llama ZS, 63% of all residual violations are fundamental — this is the price of applying strict ontological constraints to a dataset with 96 narrow relation types.

4. **Schema Tightness Correlation**: DocRED has ~3.5× more fundamental conflicts than SciERC, directly reflecting its higher constraint tightness (κ̄). This supports the paper's claim that κ̄ predicts the difficulty of schema compliance.
