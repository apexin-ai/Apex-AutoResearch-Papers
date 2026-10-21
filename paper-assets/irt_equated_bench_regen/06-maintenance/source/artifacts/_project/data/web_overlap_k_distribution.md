# Web-Overlap Per-Subject Contamination Distribution (Li et al. 2024)

## Data
- Source: `mmlu_li2024_proxy_labels.csv` (Li et al. 2024, EMNLP)
- Total items: 12508
- Items with annotation: 9229 (excluded 3279 `no_annotation`)
- Subjects with annotated data: 57 / 57

## Per-Subject Table (sorted by prevalence descending)

| # | Subject | n_items | n_contam | prevalence% |
|---|---------|---------|----------|-------------|
| 1 | college_physics | 72 | 55 | 76.4% |
| 2 | high_school_physics | 121 | 87 | 71.9% |
| 3 | philosophy | 254 | 180 | 70.9% |
| 4 | professional_accounting | 241 | 163 | 67.6% |
| 5 | conceptual_physics | 201 | 135 | 67.2% |
| 6 | high_school_microeconomics | 219 | 143 | 65.3% |
| 7 | management | 91 | 58 | 63.7% |
| 8 | moral_disputes | 259 | 165 | 63.7% |
| 9 | high_school_macroeconomics | 269 | 171 | 63.6% |
| 10 | high_school_psychology | 282 | 179 | 63.5% |
| 11 | anatomy | 121 | 72 | 59.5% |
| 12 | college_chemistry | 81 | 47 | 58.0% |
| 13 | business_ethics | 91 | 51 | 56.0% |
| 14 | high_school_statistics | 180 | 100 | 55.6% |
| 15 | high_school_biology | 261 | 142 | 54.4% |
| 16 | high_school_geography | 183 | 98 | 53.6% |
| 17 | marketing | 222 | 110 | 49.5% |
| 18 | medical_genetics | 83 | 40 | 48.2% |
| 19 | electrical_engineering | 126 | 59 | 46.8% |
| 20 | high_school_chemistry | 180 | 84 | 46.7% |
| 21 | sociology | 185 | 86 | 46.5% |
| 22 | high_school_government_and_politics | 188 | 87 | 46.3% |
| 23 | jurisprudence | 100 | 46 | 46.0% |
| 24 | elementary_mathematics | 239 | 109 | 45.6% |
| 25 | econometrics | 102 | 44 | 43.1% |
| 26 | computer_security | 86 | 37 | 43.0% |
| 27 | prehistory | 248 | 106 | 42.7% |
| 28 | college_mathematics | 71 | 29 | 40.8% |
| 29 | nutrition | 259 | 103 | 39.8% |
| 30 | virology | 149 | 56 | 37.6% |
| 31 | high_school_computer_science | 93 | 35 | 37.6% |
| 32 | machine_learning | 86 | 32 | 37.2% |
| 33 | international_law | 103 | 38 | 36.9% |
| 34 | college_medicine | 157 | 57 | 36.3% |
| 35 | high_school_mathematics | 196 | 69 | 35.2% |
| 36 | clinical_knowledge | 240 | 83 | 34.6% |
| 37 | college_biology | 132 | 45 | 34.1% |
| 38 | public_relations | 97 | 33 | 34.0% |
| 39 | college_computer_science | 84 | 26 | 31.0% |
| 40 | formal_logic | 108 | 29 | 26.9% |
| 41 | us_foreign_policy | 95 | 25 | 26.3% |
| 42 | astronomy | 135 | 32 | 23.7% |
| 43 | world_religions | 158 | 37 | 23.4% |
| 44 | security_studies | 229 | 52 | 22.7% |
| 45 | professional_medicine | 213 | 40 | 18.8% |
| 46 | logical_fallacies | 150 | 28 | 18.7% |
| 47 | miscellaneous | 286 | 47 | 16.4% |
| 48 | human_sexuality | 115 | 16 | 13.9% |
| 49 | abstract_algebra | 90 | 12 | 13.3% |
| 50 | professional_psychology | 279 | 31 | 11.1% |
| 51 | global_facts | 82 | 8 | 9.8% |
| 52 | human_aging | 202 | 14 | 6.9% |
| 53 | professional_law | 358 | 12 | 3.4% |
| 54 | high_school_world_history | 60 | 2 | 3.3% |
| 55 | high_school_european_history | 39 | 0 | 0.0% |
| 56 | high_school_us_history | 40 | 0 | 0.0% |
| 57 | moral_scenarios | 238 | 0 | 0.0% |

## Summary Statistics

| Metric | Value |
|--------|-------|
| Subjects with data | 57 |
| Mean prevalence | 38.4% |
| Median prevalence | 39.8% |
| Std | 20.8% |
| Q25 | 23.4% |
| Q75 | 54.4% |
| Min | 0.0% |
| Max | 76.4% |
| Subjects with prevalence > 50% | 16 |
| Subjects with prevalence > 25% | 41 |
| Subjects with prevalence > 10% | 50 |
| Subjects with prevalence = 0% | 3 |

## k-Parameter Constraint

In `plan_034_multi_subject_injection`, k = number of simultaneously contaminated subjects.

From Li et al. web-overlap data:
- **54 / 57 subjects** show contamination evidence (prevalence > 0%)
- This provides an empirical upper bound of **k ≤ 54**
- However, prevalence varies widely: median 39.8%, range [0.0%, 76.4%]
- 16 subjects have majority-contaminated items (>50%)
- 41 subjects have substantial contamination (>25%)

The distribution suggests that contamination is **pervasive across subjects** rather than concentrated in a few, 
supporting the use of high k values (k ≥ 30) in multi-subject injection simulations.
