# Human Annotation Results

Three annotator files have been uploaded:

- **annotator_1.csv** - Human annotator 1, includes comments (in Chinese) and confidence scores
- **annotator_2.csv** - Human annotator 2, **NO comments/reasons and NO confidence scores** — only the failure_mechanism column is filled
- **annotator_3.csv** - Annotator 3 (AI-assisted with human review), includes comments (in Chinese)

## CSV Format

All three files share the same column format:
`trace_id, clause_id, ambiguity_type, model, violation_level, failure_mechanism, confidence, comments`

## Notes

- The `failure_mechanism` column uses codes: GF (Gap-Filling), BV (Boundary Violation), CR (Conservative Refusal), SC (Spurious Compliance), SM (Structural Misparse)
- annotator_2 lacks any explanatory comments or confidence scores — this should be considered when analyzing inter-annotator agreement
- Inter-annotator agreement rates: annotator_1 vs annotator_2 ≈ 40%, annotator_1 vs annotator_3 ≈ 46%, annotator_2 vs annotator_3 ≈ 49%
