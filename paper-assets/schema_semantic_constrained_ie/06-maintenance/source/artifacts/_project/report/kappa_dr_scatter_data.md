# Per-relation κ(r) vs DR Violation Rate — Data Table

**Date**: 2026-05-19
**Source files**:
- SciERC schema: `/root/schema_semantic_constrained_ie/ontology_constraints.json`
- DocRED schema: `/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json`
- SciERC unconstrained: `/root/autodl-tmp/schema_outputs/70b_scierc_unconstrained.jsonl` (551 docs)
- DocRED unconstrained: `/root/autodl-tmp/schema_outputs/d064_qwen_docred_beam4_unconstrained.jsonl` (998 docs)

**Definition**: κ(r) = 1 − |valid_pairs(r)| / |E|², where |E|² = 36 for both datasets (6 entity types each).

## Regression Summary

| Metric | Value |
|--------|-------|
| Points (n_predicted > 0) | 99 |
| Slope | −17.729 |
| Intercept | 16.770 |
| R² | 0.184 |
| p-value | 9.30e-06 |

**Note**: Negative slope is driven by cross-dataset confound (Simpson's paradox). SciERC has permissive constraints (κ ∈ [0.03, 0.53]) with higher DR%, while DocRED has tight constraints (κ ∈ [0.58, 0.97]) with mostly DR=0%. Within each dataset, the trend appears positive (tighter constraints → more violations when violated).

## SciERC (7 relations)

| Relation | κ(r) | |V_r| | n_pred | n_viol | DR% |
|----------|-------|-------|--------|--------|-----|
| Used-for | 0.028 | 35 | 619 | 1 | 0.16 |
| Feature-of | 0.278 | 26 | 434 | 36 | 8.29 |
| Conjunction | 0.306 | 25 | 50 | 1 | 2.00 |
| Evaluate-for | 0.361 | 23 | 31 | 12 | 38.71 |
| Hyponym-of | 0.417 | 21 | 105 | 5 | 4.76 |
| Part-of | 0.417 | 21 | 197 | 28 | 14.21 |
| Compare | 0.528 | 17 | 40 | 14 | 35.00 |

## DocRED — relations with DR > 0% (18 of 92 active relations)

| Relation | Name | κ(r) | |V_r| | n_pred | n_viol | DR% |
|----------|------|-------|-------|--------|--------|-----|
| P1056 | product or material produced | 0.944 | 2 | 23 | 6 | 26.09 |
| P279 | subclass of | 0.806 | 7 | 23 | 4 | 17.39 |
| P31 | instance of | 0.583 | 15 | 80 | 10 | 12.50 |
| P127 | owned by | 0.750 | 9 | 106 | 11 | 10.38 |
| P710 | participant | 0.778 | 8 | 111 | 10 | 9.01 |
| P355 | subsidiary | 0.889 | 4 | 27 | 2 | 7.41 |
| P178 | developer | 0.889 | 4 | 14 | 1 | 7.14 |
| P276 | location | 0.694 | 11 | 110 | 7 | 6.36 |
| P527 | has part | 0.667 | 12 | 94 | 5 | 5.32 |
| P364 | original language of work | 0.861 | 5 | 60 | 3 | 5.00 |
| P112 | founded by | 0.778 | 8 | 42 | 2 | 4.76 |
| P749 | parent organization | 0.861 | 5 | 47 | 2 | 4.26 |
| P361 | part of | 0.611 | 14 | 262 | 10 | 3.82 |
| P495 | country of origin | 0.778 | 8 | 260 | 8 | 3.08 |
| P39 | position held | 0.833 | 6 | 111 | 3 | 2.70 |
| P463 | member of | 0.778 | 8 | 155 | 3 | 1.94 |
| P155 | follows | 0.694 | 11 | 82 | 1 | 1.22 |
| P577 | publication date | 0.806 | 7 | 95 | 1 | 1.05 |

74 DocRED relations have DR=0% (no violations in unconstrained output).
4 DocRED relations have 0 predictions (P1198, P1336, P737, P807).
10 output relation names were unmapped to schema P-codes (model hallucinated relation types).
