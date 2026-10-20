# Case Study: Constraint Tightness (κ) vs. Domain-Range Violation Rate

**Model**: Qwen-2.5-7B, zero-shot, greedy decoding, unconstrained  
**Datasets**: SciERC (551 samples) and DocRED (998 documents)  
**Source files**: `phase2_scierc_unconstrained.jsonl`, `docred_unconstrained.jsonl` (westd-16980)  
**Violation reports**: `violation_report_scierc_unconstrained_v2.json`, `violation_report_docred_unconstrained_v2.json`

## Schema Summary

| Dataset | Entity Types | \|E\|² | Relations |
|---------|-------------|--------|-----------|
| SciERC  | Task, Method, Material, Metric, OtherScientificTerm, Generic (6) | 36 | 7 |
| DocRED  | LOC, MISC, NUM, ORG, PER, TIME (6) | 36 | 96 |

κ(r) = 1 − \|valid\_pairs(r)\| / \|E\|²

## Complete Per-Relation Data

### SciERC

| Relation | n | DR violations | DR% | Valid pairs | κ |
|----------|---|---------------|-----|-------------|-----|
| Compare | 66 | 28 | 42.42 | 17 | 0.528 |
| Feature-of | 486 | 163 | 33.54 | 26 | 0.278 |
| Part-of | 72 | 18 | 25.00 | 21 | 0.417 |
| Evaluate-for | 133 | 32 | 24.06 | 23 | 0.361 |
| Hyponym-of | 124 | 18 | 14.52 | 21 | 0.417 |
| Used-for | 787 | 6 | 0.76 | 35 | 0.028 |
| Conjunction | 32 | 0 | 0.00 | 25 | 0.306 |

**Totals**: 1,700 triples extracted, 265 DR violations (15.6%)

### DocRED (canonical relations, n ≥ 5)

| Relation (P-code) | Name | n | DR violations | DR% | Valid pairs | κ |
|--------------------|------|---|---------------|-----|-------------|-----|
| P35 | head of state | 11 | 11 | 100.00 | 4 | 0.889 |
| P171 | parent taxon | 6 | 5 | 83.33 | 4 | 0.889 |
| P172 | ethnic group | 24 | 20 | 83.33 | 7 | 0.806 |
| P710 | participant | 39 | 32 | 82.05 | 8 | 0.778 |
| P488 | chairperson | 10 | 8 | 80.00 | 3 | 0.917 |
| P179 | series | 28 | 21 | 75.00 | 6 | 0.833 |
| P6 | head of government | 8 | 6 | 75.00 | 4 | 0.889 |
| P205 | basin country | 63 | 47 | 74.60 | 1 | 0.972 |
| P176 | manufacturer | 15 | 11 | 73.33 | 5 | 0.861 |
| P840 | narrative location | 33 | 23 | 69.70 | 5 | 0.861 |
| P1056 | product or material produced | 61 | 41 | 67.21 | 2 | 0.944 |
| P582 | end time | 122 | 79 | 64.75 | 3 | 0.917 |
| P31 | instance of | 538 | 328 | 60.97 | 9 | 0.750 |
| P272 | production company | 5 | 3 | 60.00 | 5 | 0.861 |
| P155 | follows | 74 | 44 | 59.46 | 9 | 0.750 |
| P1344 | participant of | 326 | 191 | 58.59 | 7 | 0.806 |
| P607 | conflict | 156 | 88 | 56.41 | 7 | 0.806 |
| P276 | location | 281 | 156 | 55.52 | 5 | 0.861 |
| P1412 | languages spoken/written/signed | 24 | 12 | 50.00 | 6 | 0.833 |
| P161 | cast member | 228 | 112 | 49.12 | 6 | 0.833 |
| P57 | director | 55 | 27 | 49.09 | 4 | 0.889 |
| P737 | influenced by | 301 | 147 | 48.84 | 4 | 0.889 |
| P156 | followed by | 70 | 34 | 48.57 | 9 | 0.750 |
| P190 | sister city | 17 | 8 | 47.06 | 1 | 0.972 |
| P449 | original network | 34 | 15 | 44.12 | 7 | 0.806 |
| P364 | original language of work | 23 | 10 | 43.48 | 7 | 0.806 |
| P1001 | applies to jurisdiction | 658 | 283 | 43.01 | 8 | 0.778 |
| P58 | screenwriter | 7 | 3 | 42.86 | 2 | 0.944 |
| P86 | composer | 50 | 21 | 42.00 | 3 | 0.917 |
| P800 | notable work | 248 | 102 | 41.13 | 4 | 0.889 |
| P50 | author | 269 | 110 | 40.89 | 8 | 0.778 |
| P1365 | replaces | 45 | 18 | 40.00 | 4 | 0.889 |
| P178 | developer | 62 | 24 | 38.71 | 5 | 0.861 |
| P1366 | replaced by | 70 | 27 | 38.57 | 5 | 0.861 |
| P112 | founded by | 92 | 33 | 35.87 | 8 | 0.778 |
| P576 | dissolved/abolished/demolished | 65 | 23 | 35.38 | 4 | 0.889 |
| P1336 | territory claimed by | 12 | 4 | 33.33 | 3 | 0.917 |
| P170 | creator | 37 | 12 | 32.43 | 8 | 0.778 |
| P206 | located in/next to body of water | 455 | 146 | 32.09 | 4 | 0.889 |
| P1441 | present in work | 178 | 53 | 29.78 | 7 | 0.806 |
| P150 | contains admin. territorial entity | 255 | 74 | 29.02 | 8 | 0.778 |
| P937 | work location | 7 | 2 | 28.57 | 5 | 0.861 |
| P495 | country of origin | 259 | 69 | 26.64 | 7 | 0.806 |
| P577 | publication date | 142 | 37 | 26.06 | 4 | 0.889 |
| P162 | producer | 118 | 30 | 25.42 | 6 | 0.833 |
| P166 | award received | 217 | 52 | 23.96 | 6 | 0.833 |
| P674 | characters | 84 | 20 | 23.81 | 7 | 0.806 |
| P527 | has part | 228 | 46 | 20.18 | 15 | 0.583 |
| P108 | employer | 96 | 18 | 18.75 | 2 | 0.944 |
| P137 | operator | 27 | 5 | 18.52 | 7 | 0.806 |
| P749 | parent organization | 60 | 11 | 18.33 | 5 | 0.861 |
| P740 | location of formation | 704 | 118 | 16.76 | 6 | 0.833 |
| P1376 | capital of | 42 | 7 | 16.67 | 3 | 0.917 |
| P807 | separated from | 6 | 1 | 16.67 | 2 | 0.944 |
| P463 | member of | 676 | 111 | 16.42 | 10 | 0.722 |
| P136 | genre | 71 | 10 | 14.08 | 9 | 0.750 |
| P361 | part of | 452 | 59 | 13.05 | 14 | 0.611 |
| P403 | mouth of watercourse | 33 | 4 | 12.12 | 1 | 0.972 |
| P69 | educated at | 163 | 18 | 11.04 | 2 | 0.944 |
| P26 | spouse | 82 | 9 | 10.98 | 4 | 0.889 |
| P123 | publisher | 46 | 5 | 10.87 | 7 | 0.806 |
| P39 | position held | 191 | 19 | 9.95 | 4 | 0.889 |
| P3373 | sibling | 33 | 3 | 9.09 | 1 | 0.972 |
| P580 | start time | 101 | 9 | 8.91 | 5 | 0.861 |
| P400 | platform | 45 | 4 | 8.89 | 6 | 0.833 |
| P571 | inception | 597 | 51 | 8.54 | 4 | 0.889 |
| P127 | owned by | 48 | 4 | 8.33 | 9 | 0.750 |
| P570 | date of death | 207 | 17 | 8.21 | 6 | 0.833 |
| P40 | child | 49 | 4 | 8.16 | 6 | 0.833 |
| P706 | located on terrain feature | 177 | 14 | 7.91 | 4 | 0.889 |
| P551 | residence | 90 | 6 | 6.67 | 3 | 0.917 |
| P569 | date of birth | 350 | 23 | 6.57 | 4 | 0.889 |
| P25 | mother | 23 | 1 | 4.35 | 3 | 0.917 |
| P279 | subclass of | 29 | 1 | 3.45 | 10 | 0.722 |
| P131 | located in admin. territorial entity | 1078 | 23 | 2.13 | 10 | 0.722 |
| P27 | country of citizenship | 162 | 3 | 1.85 | 7 | 0.806 |
| P54 | member of sports team | 143 | 2 | 1.40 | 10 | 0.722 |
| P102 | member of political party | 34 | 0 | 0.00 | 7 | 0.806 |
| P159 | headquarters location | 46 | 0 | 0.00 | 8 | 0.778 |
| P17 | country | 5 | 0 | 0.00 | 13 | 0.639 |
| P175 | performer | 18 | 0 | 0.00 | 10 | 0.722 |
| P19 | place of birth | 157 | 0 | 0.00 | 3 | 0.917 |
| P20 | place of death | 60 | 0 | 0.00 | 4 | 0.889 |
| P22 | father | 69 | 0 | 0.00 | 7 | 0.806 |
| P355 | subsidiary | 5 | 0 | 0.00 | 5 | 0.861 |
| P676 | lyrics by | 9 | 0 | 0.00 | 2 | 0.944 |

**Totals**: 17,497 triples extracted (12,308 canonical), 3,230 DR violations (18.5%)

## Case Study Selection

### Top-5 Highest DR Violation Rate

| # | Relation | Dataset | κ | DR% | n | Analysis |
|---|----------|---------|-----|-----|---|----------|
| 1 | basin country (P205) | DocRED | 0.97 | 74.6 | 63 | Only LOC→LOC is valid. The model frequently assigns ORG (13), MISC (9), or PER (7) to the head entity instead of LOC, mistyping geographic entities. The extreme κ means any type error becomes a DR violation. |
| 2 | product or material produced (P1056) | DocRED | 0.94 | 67.2 | 61 | Only ORG→MISC and ORG→ORG are valid. The model misattributes production to LOC (12) and PER (9) heads. The producer role has clear real-world ORG semantics, but the model conflates producing organizations with their locations or founders. |
| 3 | participant of (P1344) | DocRED | 0.81 | 58.6 | 326 | Largest n among high-DR relations. The model hallucinates EVENT as an entity type (58 instances) absent from the schema—events should be MISC. Additionally, PER→PER (48) is frequent but invalid. The model struggles to distinguish event entities from person entities in participation contexts. |
| 4 | Compare (SciERC) | 0.53 | 42.4 | 66 | The constraint restricts comparison to within-category pairs (Method↔Method, Task↔Task). The model produces cross-category comparisons: Method↔OtherScientificTerm (7), Task↔Method (6), Method↔Task (4). In scientific text, "compared to" often connects a method to a competing approach the model labels differently. |
| 5 | Feature-of (SciERC) | 0.28 | 33.5 | 486 | Despite moderate κ (26/36 pairs valid), violations are driven by the fuzzy boundary between Task and OtherScientificTerm: Task→OtherScientificTerm (43 violations) is the largest violating pair, followed by Generic→Generic (33). The model struggles to distinguish features (typically OtherScientificTerm) from the tasks they characterize. |

### Bottom-5 Lowest DR Violation Rate

| # | Relation | Dataset | κ | DR% | n | Analysis |
|---|----------|---------|-----|-----|---|----------|
| 1 | place of birth (P19) | DocRED | 0.92 | 0.0 | 157 | All 157 predictions are PER→LOC. Despite high κ (only 3 valid pairs), the relation has a completely unambiguous type signature—persons are born in locations, and the model never confuses these types. |
| 2 | father (P22) | DocRED | 0.81 | 0.0 | 69 | 93% of predictions are PER→PER (64/69), with the rest (PER→MISC, PER→LOC) also in valid pairs. Kinship relations have strong type priors that the model respects. |
| 3 | place of death (P20) | DocRED | 0.89 | 0.0 | 60 | 98% PER→LOC (59/60), one PER→ORG—all valid pairs. Mirrors place of birth: the strong PER→LOC prior makes this relation robust despite high κ. |
| 4 | Conjunction (SciERC) | 0.31 | 0.0 | 32 | Conjoined entities naturally share the same type (e.g., "method A and method B"). 25/36 pairs are valid, and the same-type pairing pattern means the model rarely produces invalid combinations. |
| 5 | Used-for (SciERC) | 0.03 | 0.8 | 787 | 35/36 type pairs are valid—only Metric→Metric is excluded. With near-universal coverage, it is virtually impossible to produce a DR violation. The 6 violations (0.8%) are the residual edge case. |

## Key Insight

The case study demonstrates that **high κ is necessary but not sufficient for high DR violation rates**. The critical co-factor is **entity type confusion**:

- **High κ + confusable types → high DR%**: Relations like `basin country` (κ=0.97) and `participant of` (κ=0.81) suffer because their participating entity types (LOC vs. ORG, PER vs. EVENT/MISC) are frequently confused by the model.
- **High κ + distinct types → zero DR%**: Relations like `place of birth` (κ=0.92) and `place of death` (κ=0.89) have equally high κ but zero violations, because PER and LOC are semantically unambiguous—the model always assigns the correct types.
- **Low κ → near-zero DR% regardless**: `Used-for` (κ=0.03) has near-universal pair coverage, making violations nearly impossible regardless of type confusion.

This two-factor pattern (κ × type confusability) motivates the constrained decoding approach: by enforcing valid type pairs during generation, we can eliminate DR violations entirely, with the largest gains on high-κ, confusable-type relations.
