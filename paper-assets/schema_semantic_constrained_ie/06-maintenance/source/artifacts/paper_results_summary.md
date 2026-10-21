# OntoCoDec Paper Results Summary

> Generated: 2026-05-14 | Model: Qwen3-8B | SciERC: 551 samples | DocRED: 998 docs

---

## A. SciERC Phase 2 Main Table (Paper Table 1 Candidate)

All experiments use identical code path (`run_constrained_extraction.py`), same prompt, same model, same test set (551 sentences).

| Mode | DR↓ | RV↓ | ET↓ | CF | R-F1 | E-F1 | Triples | Entities |
|------|-----|-----|-----|----|------|------|---------|----------|
| unconstrained | 15.37% | 1.39% | 0.40% | 0.08% | 0.0823 | 0.3101 | 1724 | 2474 |
| grammar_only | 14.84% | 0% | 0% | 0.08% | 0.0823 | 0.3098 | 1725 | 2474 |
| semantic_only | 11.65% | 1.51% | 0.40% | 2.71% | 0.0815 | 0.3101 | 1726 | 2474 |
| **full_s1** | **0.93%** | **0%** | **0%** | **9.90%** | **0.0836** | **0.3098** | **1729** | **2474** |
| full_s2 | 0.97% | 0% | 0% | 8.03% | 0.0803 | 0.3190 | 1644 | 2228 |

### Delta vs Unconstrained

| Mode | ΔDR (pp) | ΔDR (rel%) | ΔRV | ΔET | ΔCF | ΔR-F1 (pp) | ΔE-F1 (pp) |
|------|----------|------------|-----|-----|-----|-------------|-------------|
| grammar_only | -0.53 | ↓3.4% | ↓100% | ↓100% | 0 | 0.00 | -0.03 |
| semantic_only | -3.72 | ↓24.2% | +0.12pp | 0 | +2.63pp | -0.08 | 0.00 |
| **full_s1** | **-14.44** | **↓93.9%** | **↓100%** | **↓100%** | **+9.82pp** | **+0.13** | **-0.03** |
| full_s2 | -14.40 | ↓93.7% | ↓100% | ↓100% | +7.95pp | -0.20 | +0.89 |

**Experiment IDs**: `phase2_scierc_unconstrained`, `phase2_scierc_grammar_only`, `phase2_scierc_semantic_only`, `phase2_scierc_full_s1`, `phase2_scierc_full_s2`

---

## B. DocRED Phase 0 Comparison Table (Paper Table 2 Candidate)

Prompt-level intervention on complex schema (96 relation types, avg 5.68 valid pairs/relation).

| Mode | DR | RV | ET | CF | Parse Rate | Triples | Entities |
|------|----|----|----|----|------------|---------|----------|
| unconstrained | 18.70% | 28.90% | 7.50% | 0.08% | 96.40% | 16540 | 19099 |
| schema-informed | 12.84% | 18.41% | 0.61% | 0.15% | 94.49% | 16782 | 19524 |

### Delta

| Metric | Δpp | Relative ↓ |
|--------|-----|------------|
| DR | -5.86 | ↓31.3% |
| RV | -10.49 | ↓36.3% |
| ET | -6.89 | ↓91.9% |
| CF | +0.07 | — |

### Cross-Dataset Prompt Effectiveness (SciERC vs DocRED)

| Dataset | Relations | Avg Valid Pairs | DR (minimal) | DR (schema) | DR Reduction |
|---------|-----------|-----------------|--------------|-------------|--------------|
| SciERC | 7 | 26.1 | 15.37% | 5.78% | ↓62.4% |
| DocRED | 96 | 5.68 | 18.70% | 12.84% | ↓31.3% |

Prompt-level intervention scales poorly with ontology complexity: 62% reduction on 7 relations → 31% on 96 relations.

**Experiment IDs**: `mvp_phase0_violation_rate_docred`, `mvp_phase0_docred_schema`, `mvp_phase0_violation_rate`, `mvp_phase0_scierc_schema`

---

## C. Per-Relation DR Breakdown (Paper Figure Candidate)

### SciERC: DR violation rate (%) by relation type across decoding modes

| Relation | Unconstrained | Grammar | Semantic | Full S1 | Full S2 | S1 Δ (pp) |
|----------|:------------:|:-------:|:--------:|:-------:|:-------:|:---------:|
| Compare | 42.42 | 40.85 | 29.23 | 2.82 | 4.60 | -39.60 |
| Feature-of | 33.54 | 31.98 | 26.28 | 1.21 | 1.22 | -32.33 |
| Part-of | 25.00 | 23.38 | 11.27 | 0.00 | 1.25 | -25.00 |
| Evaluate-for | 24.06 | 23.13 | 23.13 | 5.76 | 5.08 | -18.30 |
| Hyponym-of | 14.52 | 14.40 | 7.09 | 0.00 | 0.00 | -14.52 |
| Used-for | 0.76 | 0.25 | 0.77 | 0.00 | 0.12 | -0.76 |
| Conjunction | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

### Per-Relation Triple Counts (denominator context)

| Relation | Unconstrained | Grammar | Semantic | Full S1 | Full S2 |
|----------|:------------:|:-------:|:--------:|:-------:|:-------:|
| Used-for | 787 | 791 | — | — | 855 |
| Feature-of | 486 | 494 | — | — | 328 |
| Evaluate-for | 133 | 134 | — | — | 118 |
| Hyponym-of | 124 | 125 | — | — | 97 |
| Part-of | 72 | 77 | — | — | 80 |
| Compare | 66 | 71 | — | — | 87 |
| Conjunction | 32 | 33 | — | — | 79 |

**Key patterns**:
- Grammar layer alone has negligible DR effect (↓3.4% relative) — expected, no D/R constraints in grammar
- Semantic-only reduces DR for high-violation relations (Compare -13pp, Feature-of -7pp) but residual remains high
- Full S1 achieves near-zero DR across all relations; residual concentrates on Evaluate-for (5.76%) and Compare (2.82%)
- S2 slightly worse than S1 on Compare (4.60 vs 2.82), Part-of (1.25 vs 0.00), Used-for (0.12 vs 0.00)

### SciERC Phase 0: Schema-Informed Prompt Per-Relation DR

| Relation | Minimal | Schema-informed | Δpp |
|----------|:-------:|:---------------:|:---:|
| Feature-of | 33.54% | ~11.2% | -22.3 |
| Part-of | 25.00% | ~2.5% | -22.5 |
| Compare | 42.42% | ~27.6% | -14.8 |
| Evaluate-for | 24.06% | ~29.9% | **+5.8** |
| Hyponym-of | 14.52% | — | — |
| Used-for | 0.76% | — | — |

Evaluate-for **regresses** with schema-informed prompt — prior-constraint conflict.

---

## D. Key Findings

### D1. Claim Support Mapping

**Claim 1 — Violation Landscape** (systematic, non-trivial violation rates):
- `mvp_phase0_violation_rate`: SciERC DR=15.37%, 3× above 5% threshold
- `mvp_phase0_violation_rate_docred`: DocRED DR=18.70%, comparable despite 14× larger ontology
- Per-relation: Compare 42.4%, Feature-of 33.5% vs Used-for 0.76% — violation driven by constraint tightness, not ontology size

**Claim 2 — Prompt Insufficiency** (prompt reduces but cannot eliminate):
- `mvp_phase0_scierc_schema`: SciERC DR 15.37%→5.78% (↓62.4%), still >5%
- `mvp_phase0_docred_schema`: DocRED DR 18.70%→12.84% (↓31.3%), scales poorly
- Evaluate-for regression +5.8pp demonstrates prompt unreliability at per-relation level

**Claim 3 — Composable Constraint Framework** (grammar enables semantic):
- `phase2_scierc_grammar_only`: RV 1.39%→0%, ET 0.40%→0%, DR unchanged (14.84%). F1 neutral.
- `phase2_scierc_semantic_only`: DR ↓24.2% but RV/ET persist — semantic needs grammar as prerequisite
- `phase2_scierc_full_s1`: DR ↓93.9%, RV→0%, ET→0%. Layers complementary with enabling dependency.

**Claim 4 — S1 vs S2 Trade-off** (architectural ablation):
- `phase2_scierc_full_s1`: DR=0.93%, CF=9.90%, R-F1=0.0836
- `phase2_scierc_full_s2`: DR=0.97%, CF=8.03%, R-F1=0.0803
- S1 recommended: simpler, marginally better DR and F1. S2 is variant showing framework flexibility.

### D2. CF Violation Root Cause Analysis

| Metric | grammar_only | full_s1 | full_s2 |
|--------|:-----------:|:-------:|:-------:|
| CF rate | 0.08% | 9.90% | 8.03% |

**CF is 100% introduced by the semantic layer** (grammar_only CF = unconstrained CF = 0.08%).

**Subtypes**:
- **EVR (entity-vs-relation type drift)**: >90% of CF. Same entity assigned different types in entity list vs relation triples.
  - S1: 245 entities (7.34% of entity mentions)
  - S2: 178 entities (5.54%, ↓27% vs S1)
- **Within-relation** (same entity typed differently across relations):
  - S1: 10 (0.36%)
  - S2: 18 (0.72%)

**Top conflict patterns** (SciERC type system ambiguity):
| Type Pair | Count |
|-----------|:-----:|
| Generic ↔ OtherScientificTerm | 60 |
| Material ↔ OtherScientificTerm | 28 |
| Material ↔ Method | 20 |

These reflect genuine semantic boundary ambiguity in SciERC's type system — the same term can be legitimately categorized as either type depending on context.

**Severity distinction**:
- DR violations = structurally invalid triples (downstream systems reject) → hard constraint
- CF violations = individual triples remain type-valid, only cross-triple consistency broken → soft preference

### D3. S1 vs S2 Trade-off Summary

| Dimension | S1 (single-pass) | S2 (two-pass) | Winner |
|-----------|:-----------------:|:-------------:|:------:|
| DR | 0.93% | 0.97% | S1 (marginal) |
| CF | 9.90% | 8.03% | S2 (not significant) |
| R-F1 | 0.0836 | 0.0803 | S1 |
| E-F1 | 0.3098 | 0.3190 | S2 |
| Triples generated | 1729 | 1644 | S1 (more output) |
| Entities generated | 2474 | 2228 | S1 (more output) |
| Simplicity | Single pass | Two passes | S1 |

**Recommendation**: S1 as primary method, S2 as ablation/appendix. S2 does NOT solve CF — the 1.87pp difference is not significant at n≈2400 entities.

### D4. F1 Neutrality Evidence

| Mode | R-F1 | vs unconstrained |
|------|:----:|:----------------:|
| unconstrained | 0.0823 | — |
| grammar_only | 0.0823 | +0.00pp |
| semantic_only | 0.0815 | -0.08pp |
| full_s1 | 0.0836 | +0.13pp |
| full_s2 | 0.0803 | -0.20pp |

All within noise on ~1700 triples, single seed. **Frame as F1-neutral, NOT F1-improvement.** No bootstrap CI computed.

---

## E. Pending Experiments

### Running
1. **DocRED Phase 2 grammar_only** (`phase2_docred_grammar_only`): 998 docs on cuda:0, started 2026-05-14T01:55
2. **DocRED Phase 2 full_s1** (`phase2_docred_full_s1`): 998 docs on cuda:1, started 2026-05-14T02:07

### Needed for Paper
3. **DocRED Phase 2 full_s1 completion** → validates cross-dataset generalization (Table 2 extension)
4. **DocRED Phase 2 semantic_only** → completes ablation story on complex schema

### Stretch Goals
5. **Cross-model validation** (Llama-3.1-8B) → addresses Reviewer C5
6. **Bootstrap CI for F1** → statistical backing for F1-neutrality claim
7. **DocRED Phase 2 full_s2** → S1/S2 comparison on complex schema

---

## Appendix: Raw Experiment Registry

| Exp ID | Status | Dataset | Mode | Samples | Wall Clock |
|--------|--------|---------|------|---------|------------|
| mvp_phase0_violation_rate | DONE | SciERC | minimal prompt | 551 | 1.13 GPU-hr |
| mvp_phase0_scierc_schema | DONE | SciERC | schema-informed prompt | 551 | 1.01 GPU-hr |
| mvp_phase0_violation_rate_docred | DONE | DocRED | minimal prompt | 998 | — |
| mvp_phase0_docred_schema | DONE | DocRED | schema-informed prompt | 998 | 3.75 GPU-hr |
| phase2_scierc_unconstrained | DONE | SciERC | unconstrained decoding | 551 | 1.44 GPU-hr |
| phase2_scierc_grammar_only | DONE | SciERC | grammar-only decoding | 551 | — |
| phase2_scierc_semantic_only | DONE | SciERC | semantic-only decoding | 551 | 0.73 GPU-hr |
| phase2_scierc_full_s1 | DONE | SciERC | full S1 (grammar+semantic) | 551 | 0.73 GPU-hr |
| phase2_scierc_full_s2 | DONE | SciERC | full S2 (two-pass) | 551 | 0.10 GPU-hr |
| phase2_s2_pilot50 | DONE | SciERC | S2 pilot (50 samples) | 50 | — |
| phase2_docred_grammar_only | RUNNING | DocRED | grammar-only decoding | 998 | — |
| phase2_docred_full_s1 | RUNNING | DocRED | full S1 (grammar+semantic) | 998 | — |
