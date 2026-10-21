IRT 2PL+γ input data v3 (seed=42, 5 families × 5 dosages = 25 respondents)

Coverage: 25/25 respondents, no missing data.
Data source: westd eval_results_v2/ (correct source)

| File | Shape | Description |
|------|-------|-------------|
| response_matrix_mmlu.csv | 25×14042 | Binary correctness matrix |
| response_matrix_arc.csv | 25×1172 | Binary correctness matrix |
| exposure_scores.csv | 25 rows | family, dosage, oracle exposure |
| item_metadata_mmlu.csv | 14042 rows | subject, domain, difficulty |
| item_metadata_arc.csv | 1172 rows | difficulty |

MMLU domains: STEM 3153, Humanities 4705, Social Sci 3077, Other 3107
Script: westd:/root/contamcal-irt-calibration/analysis/irt_data_v3/irt_data_prep_v3.py