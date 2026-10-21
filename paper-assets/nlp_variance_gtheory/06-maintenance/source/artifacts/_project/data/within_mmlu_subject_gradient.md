Within-MMLU Subject Gradient

| Subject | Acc | item_id% | model×item% |
|---|---|---|---|
| professional_medicine | 0.810 | 7.5% | 65.7% |
| high_school_mathematics | 0.415 | 10.9% | 46.0% |
| abstract_algebra | 0.510 | 19.6% | 42.1% |
| us_foreign_policy | 0.893 | 31.9% | 46.3% |
| college_physics | 0.501 | 39.5% | 31.4% |
| computer_security | 0.796 | 41.5% | 27.6% |
| philosophy | 0.837 | 41.2% | 28.1% |
| world_religions | 0.861 | 46.1% | 22.5% |
| clinical_knowledge | 0.620 | 57.7% | 32.0% |
| international_law | 0.772 | 57.7% | 27.0% |

item_id% CV=0.48 across subjects. Correlation(accuracy, item_id%) = 0.301 (p=0.40, not significant).
professional_medicine is extreme: model×item 65.7% dominates — item difficulty is almost entirely model-dependent.
File: results/analysis/within_mmlu_subject_gradient.json