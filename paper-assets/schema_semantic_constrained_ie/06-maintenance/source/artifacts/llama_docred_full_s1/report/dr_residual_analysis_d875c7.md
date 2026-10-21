# Residual DR Violation Analysis: Llama DocRED full_s1

## 1. Summary

| Metric | Llama Unc | Llama S1 | Qwen Unc | Qwen S1 |
|--------|-----------|----------|----------|---------|
| DR-eligible triples | 13,670 | 16,368 | 11,616 | 17,336 |
| DR violations | 4,210 | **418** | 2,538 | 1,770 |
| DR rate | 30.80% | **2.55%** | 21.85% | 10.21% |
| Relative reduction | - | **91.7%** | - | 53.3% |
| RV rate | 16.03% | 0.00% | 29.66% | 0.03% |
| ET rate | 0.13% | 0.00% | 2.47% | 0.00% |

Grammar+Semantic constrained decoding (S1) reduces Llama's DR from 30.80% to 2.55% (**91.7% relative reduction**), far exceeding Qwen's 53.3% reduction. Of 94 active relations, **42 (44.7%) achieve zero residual violations**.

---

## 2. Top-10 Violating Relations (Llama S1)

| Rank | PID | Relation | Violations | Total | DR Rate | tau(r) | Unc Rate | Qwen S1 | Dominant Pair |
|------|-----|----------|-----------|-------|---------|--------|----------|---------|---------------|
| 1 | P1001 | applies to jurisdiction | 45 | 637 | 7.1% | 0.778 | 62.5% | 20.1% | LOC->ORG (14) |
| 2 | P31 | instance of | 37 | 290 | 12.8% | 0.750 | 42.9% | 1.9% | PER->PER (20) |
| 3 | P607 | conflict | 30 | 453 | 6.6% | 0.806 | 58.0% | 24.5% | PER->PER (14) |
| 4 | P161 | cast member | 25 | 984 | 2.5% | 0.833 | 5.8% | 1.3% | PER->ORG (25) |
| 5 | P156 | followed by | 24 | 117 | 20.5% | 0.750 | 83.3% | 19.0% | ORG->TIME (17) |
| 6 | P576 | dissolved/abolished | 24 | 73 | 32.9% | 0.889 | 53.3% | 36.3% | ORG->ORG (11) |
| 7 | P276 | location | 23 | 458 | 5.0% | 0.861 | 69.0% | 28.4% | PER->LOC (22) |
| 8 | P569 | date of birth | 21 | 833 | 2.5% | 0.889 | 51.2% | 3.8% | NUM->PER (17) |
| 9 | P582 | end time | 21 | 130 | 16.2% | 0.917 | 76.3% | 43.5% | PER->TIME (18) |
| 10 | P27 | country of citizenship | 17 | 607 | 2.8% | 0.806 | 11.5% | 0.6% | LOC->PER (12) |

These 10 relations account for **267/418 (63.9%)** of all residual violations. The top-10 is dominated by **argument role confusion** patterns (entity assigned wrong role, e.g., PER as object when LOC is required).

---

## 3. Tightness tau(r) vs Residual DR Correlation

**tau(r) = 1 - |valid_type_pairs| / 36** measures how restrictive a relation's domain/range constraint is (higher = tighter).

| Analysis | n | Spearman rho | p-value | Interpretation |
|----------|---|-------------|---------|----------------|
| **Llama S1** | 90 | **0.069** | **0.517** | No correlation |
| Qwen S1 | 90 | 0.357 | 5.6e-4 | Moderate positive |

**Key finding**: Residual DR violations in Llama S1 are **uncorrelated with tightness** (rho=0.07, p=0.52). This means the constraint system works equally well across tight (few valid pairs) and loose (many valid pairs) relations. Tightness does not predict which relations will have residual violations.

For comparison, Qwen S1 still shows moderate correlation (rho=0.36), indicating Qwen's residual violations are partly explained by tight constraints - but Llama's superior constraint compliance eliminates this dependency.

**Tightness of violating vs non-violating relations** (relations with >=5 triples):
- Violating (n=52): mean tau = 0.846
- Non-violating (n=38): mean tau = 0.837
- Mann-Whitney U p = 0.30 (not significant)

---

## 4. Violation Pattern Analysis (Non-Local Dependencies)

The dominant violation pairs reveal **three categories** of residual violations:

### Category A: Entity Type Ambiguity (forward coreference)
These violations arise because an entity's type is committed at first mention, but later relations require a different type context.

| Relation | Violation Pair | Example Pattern |
|----------|---------------|-----------------|
| P161 (cast member) | PER->ORG (25/25) | "Film X" typed as ORG instead of MISC |
| P276 (location) | PER->LOC (22/23) | Person mentioned before location role revealed |
| P569 (date of birth) | NUM->PER (17/21) | Year entity typed as NUM, person as head expected |
| P27 (country of citizenship) | LOC->PER (12/17) | Nationality entity as LOC, person role misassigned |

**Root cause**: In left-to-right generation, the entity list is produced before relations. An entity's type must be committed before the model knows all relations it will participate in. When the first contextual cue suggests one type but a later relation requires a different type pair, the greedy decoder cannot backtrack.

### Category B: Temporal/Abstract Role Confusion
| Relation | Violation Pair | Count |
|----------|---------------|-------|
| P582 (end time) | PER->TIME (18) | Entity incorrectly in temporal role |
| P156 (followed by) | ORG->TIME (17) | Succession relation with wrong tail type |
| P576 (dissolved) | ORG->ORG (11) | Expected ORG->TIME or similar |

### Category C: Type Granularity Mismatch
| Relation | Violation Pair | Count |
|----------|---------------|-------|
| P1001 (jurisdiction) | PER->PER (12), PER->NUM (8) | Political entities mistyped |
| P31 (instance of) | PER->PER (20) | Broad relation with diverse type patterns |
| P607 (conflict) | PER->PER (14) | Nations/groups mistyped as PER |

---

## 5. Llama vs Qwen Per-Relation Comparison

### Relations where Llama S1 dramatically outperforms Qwen S1:

| PID | Relation | Llama S1 DR | Qwen S1 DR | Llama Advantage |
|-----|----------|-------------|------------|-----------------|
| P737 | influenced by | 2.9% | 22.4% | 7.7x lower |
| P800 | notable work | 0.7% | 21.2% | 30.3x lower |
| P86 | composer | **0.0%** | 29.8% | eliminated |
| P50 | author | 0.8% | 16.6% | 20.8x lower |
| P1344 | participant of | 1.1% | 19.5% | 17.7x lower |
| P463 | member of | 3.1% | 9.5% | 3.1x lower |
| P108 | employer | 1.8% | 17.3% | 9.6x lower |
| P166 | award received | 0.7% | 6.1% | 8.7x lower |

### Relations where both models struggle (structural difficulty):

| PID | Relation | Llama S1 DR | Qwen S1 DR | tau(r) |
|-----|----------|-------------|------------|--------|
| P576 | dissolved/abolished | 32.9% | 36.3% | 0.889 |
| P582 | end time | 16.2% | 43.5% | 0.917 |
| P156 | followed by | 20.5% | 19.0% | 0.750 |
| P31 | instance of | 12.8% | 1.9% | 0.750 |
| P1056 | product/material | 11.2% | 30.8% | 0.944 |

---

## 6. Fallback Analysis

The experiment logs record **32,921 grammar-first fallback events** across 577 documents. A fallback occurs when the semantic constraint layer rejects the grammar-only candidate, but the grammar decoder's top candidate is accepted as fallback.

For Qwen full_s1 (where fallback data is available per-relation), the **fallback rate exactly equals the DR violation rate** (10.21%), confirming that fallback triples are the primary source of residual violations. The per-relation fallback distribution mirrors the DR distribution.

For Llama, the dramatically lower residual DR (2.55% vs Qwen's 10.21%) despite high fallback frequency suggests that **Llama's base model produces more constraint-compatible type assignments**, making the grammar-first fallback less likely to produce DR violations.

---

## 7. Zero-Violation Relations (42/94)

Relations with zero violations despite substantial traffic confirm the constraint system's effectiveness:

| PID | Relation | Triples | tau(r) |
|-----|----------|---------|--------|
| P131 | located in admin. territory | 1,660 | 0.722 |
| P206 | located near body of water | 577 | 0.889 |
| P361 | part of | 347 | 0.611 |
| P170 | creator | 190 | 0.778 |
| P40 | child | 161 | 0.833 |
| P86 | composer | 150 | 0.917 |
| P39 | position held | 125 | 0.889 |
| P674 | characters | 122 | 0.806 |

Notably, P86 (composer, tau=0.917 = very tight) achieves zero violations with 150 triples, while Qwen S1 has 29.8% violations on the same relation. P131 (the highest-traffic relation at 1,660 triples) also achieves zero violations.

---

