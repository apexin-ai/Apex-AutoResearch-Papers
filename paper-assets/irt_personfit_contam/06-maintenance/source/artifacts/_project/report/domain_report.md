# MMLU Domain-Specific lz* Analysis Report

## Overview
- **Models**: 12
- **MMLU Subjects**: 57
- **MMLU Items**: 14,042
- **Broad Categories**: STEM, Humanities, Social Sciences, Other

## Overall MMLU lz* (all 14042 items)

| Model | θ | MMLU Acc | MMLU lz* | Flagged? |
|-------|---|----------|----------|----------|
| 360GPT2-Pro | 1.46 | 0.831 | 24.90 | ⚠️ |
| DeepSeek-V3 | 3.77 | 0.867 | 16.45 | ⚠️ |
| Doubao-pro | 1.14 | 0.844 | -14.60 |  |
| Gemini-1.5 | 0.78 | 1.000 | 34.75 | ⚠️ |
| Gemma-2B-it | -3.38 | 0.335 | 21.78 | ⚠️ |
| Hunyuan-Turbo | 1.73 | 0.821 | 12.14 | ⚠️ |
| Mistral-7B-Instruct-v0.1 | -1.37 | 0.533 | 32.89 | ⚠️ |
| Moonshot-v1 | 0.93 | 0.779 | 18.69 | ⚠️ |
| Qwen-Plus | 0.96 | 0.819 | 44.91 | ⚠️ |
| Qwen2.5-3B-Instruct | -0.13 | 0.653 | 20.27 | ⚠️ |
| Vicuna-7B-v1.3 | -1.89 | 0.391 | 29.97 | ⚠️ |
| Yi-Lightning | 0.77 | 0.819 | 48.15 | ⚠️ |

## Gemini-1.5 Deep Dive
- **Overall MMLU accuracy**: 1.0000 (14042/14042)
- **Overall MMLU lz***: 34.75
- **Subjects with 100% accuracy**: 57/57
- **Subjects with errors**: 0/57

### Subjects with 100% accuracy:
abstract_algebra, anatomy, astronomy, business_ethics, clinical_knowledge, college_biology, college_chemistry, college_computer_science, college_mathematics, college_medicine, college_physics, computer_security, conceptual_physics, econometrics, electrical_engineering, elementary_mathematics, formal_logic, global_facts, high_school_biology, high_school_chemistry, high_school_computer_science, high_school_european_history, high_school_geography, high_school_government_and_politics, high_school_macroeconomics, high_school_mathematics, high_school_microeconomics, high_school_physics, high_school_psychology, high_school_statistics, high_school_us_history, high_school_world_history, human_aging, human_sexuality, international_law, jurisprudence, logical_fallacies, machine_learning, management, marketing, medical_genetics, miscellaneous, moral_disputes, moral_scenarios, nutrition, philosophy, prehistory, professional_accounting, professional_law, professional_medicine, professional_psychology, public_relations, security_studies, sociology, us_foreign_policy, virology, world_religions

### Subjects with errors (sorted by n_wrong):

| Subject | Accuracy | N_items | N_wrong | lz* |
|---------|----------|---------|---------|-----|

## Category-Level lz*

| Model | STEM | Humanities | Social Sci | Other |
|-------|------|------------|------------|-------|
| 360GPT2-Pro | 18.91 | 6.84 | 12.07 | 12.10 |
| DeepSeek-V3 | 8.41 | 9.55 | 8.99 | 5.97 |
| Doubao-pro | -1.95 | -12.97 | -14.81 | 4.43 |
| Gemini-1.5 | 21.17 | 17.86 | 15.88 | 15.30 |
| Gemma-2B-it | 12.47 | 8.91 | 12.38 | 9.91 |
| Hunyuan-Turbo | 1.80 | 0.63 | 13.91 | 8.40 |
| Mistral-7B-Instruct-v0.1 | 18.84 | 14.97 | 18.26 | 13.48 |
| Moonshot-v1 | 10.25 | 9.55 | 9.40 | 8.75 |
| Qwen-Plus | 24.35 | 21.37 | 27.12 | 15.53 |
| Qwen2.5-3B-Instruct | 10.07 | 9.35 | 12.36 | 8.70 |
| Vicuna-7B-v1.3 | 18.37 | 14.20 | 15.99 | 10.71 |
| Yi-Lightning | 26.85 | 22.88 | 28.53 | 16.37 |

## Per-Model Flagged Subjects (lz* > 1.96)

- **360GPT2-Pro** (40/57 subjects): miscellaneous (11.8), elementary_mathematics (8.4), high_school_mathematics (8.0), high_school_psychology (8.0), moral_scenarios (6.9), high_school_macroeconomics (6.7), high_school_microeconomics (6.7), high_school_biology (6.3), high_school_statistics (5.8), professional_accounting (5.7)
- **DeepSeek-V3** (36/57 subjects): miscellaneous (6.5), philosophy (5.8), sociology (4.9), professional_psychology (4.7), moral_scenarios (4.3), high_school_psychology (4.3), security_studies (4.1), moral_disputes (4.1), prehistory (3.6), high_school_geography (3.4)
- **Doubao-pro** (12/57 subjects): elementary_mathematics (6.9), miscellaneous (6.8), high_school_mathematics (5.8), high_school_microeconomics (5.7), high_school_computer_science (4.4), high_school_government_and_politics (4.0), college_biology (3.7), marketing (3.6), high_school_psychology (3.5), high_school_biology (2.7)
- **Gemini-1.5** (50/57 subjects): miscellaneous (12.4), elementary_mathematics (11.8), high_school_psychology (10.1), professional_medicine (8.9), high_school_us_history (8.7), high_school_microeconomics (8.2), high_school_macroeconomics (8.2), high_school_biology (8.0), high_school_mathematics (7.5), marketing (7.5)
- **Gemma-2B-it** (44/57 subjects): miscellaneous (7.9), high_school_psychology (6.7), marketing (6.4), professional_medicine (5.0), moral_disputes (4.9), human_aging (4.7), logical_fallacies (4.7), security_studies (4.6), professional_psychology (4.5), high_school_microeconomics (4.1)
- **Hunyuan-Turbo** (33/57 subjects): miscellaneous (9.0), professional_law (7.3), professional_psychology (6.9), sociology (5.6), high_school_psychology (5.6), astronomy (5.0), nutrition (5.0), high_school_government_and_politics (4.8), high_school_geography (4.8), high_school_biology (4.5)
- **Mistral-7B-Instruct-v0.1** (55/57 subjects): miscellaneous (10.3), professional_law (9.4), high_school_psychology (7.9), marketing (7.1), professional_psychology (6.7), elementary_mathematics (6.6), moral_disputes (5.8), moral_scenarios (5.7), high_school_macroeconomics (5.6), prehistory (5.5)
- **Moonshot-v1** (31/57 subjects): miscellaneous (10.6), moral_scenarios (10.4), high_school_psychology (7.2), elementary_mathematics (6.3), high_school_government_and_politics (6.1), high_school_biology (5.1), professional_medicine (5.0), nutrition (4.8), high_school_microeconomics (4.8), high_school_computer_science (4.7)
- **Qwen-Plus** (56/57 subjects): professional_law (15.8), miscellaneous (12.6), professional_psychology (10.2), high_school_psychology (10.0), prehistory (9.3), high_school_biology (9.0), moral_disputes (8.5), nutrition (8.1), moral_scenarios (8.1), high_school_us_history (8.0)
- **Qwen2.5-3B-Instruct** (42/57 subjects): high_school_psychology (8.1), miscellaneous (6.7), high_school_world_history (5.7), professional_psychology (5.6), security_studies (5.0), sociology (4.9), high_school_biology (4.9), marketing (4.9), prehistory (4.7), world_religions (4.5)
- **Vicuna-7B-v1.3** (52/57 subjects): miscellaneous (8.1), high_school_psychology (7.2), professional_law (6.7), professional_psychology (6.6), prehistory (6.1), professional_medicine (6.0), moral_scenarios (5.8), moral_disputes (5.5), high_school_macroeconomics (5.5), high_school_statistics (5.5)
- **Yi-Lightning** (56/57 subjects): professional_law (16.7), miscellaneous (13.0), professional_psychology (10.7), high_school_psychology (10.4), moral_scenarios (9.6), high_school_biology (9.3), prehistory (9.3), moral_disputes (8.8), elementary_mathematics (8.6), high_school_macroeconomics (8.4)

## Domain Concentration Analysis

### Is Gemini-1.5's anomaly domain-concentrated?

- Gemini-1.5 per-subject lz* mean: 4.99, std: 3.14, CV: 0.63
- 360GPT2-Pro: mean=3.38, std=2.74, CV=0.81
- DeepSeek-V3: mean=2.15, std=1.61, CV=0.75
- Doubao-pro: mean=-1.36, std=4.42, CV=3.26
- Gemini-1.5: mean=4.99, std=3.14, CV=0.63
- Gemma-2B-it: mean=2.89, std=1.66, CV=0.58
- Hunyuan-Turbo: mean=1.54, std=4.60, CV=2.98
- Mistral-7B-Instruct-v0.1: mean=4.28, std=1.70, CV=0.40
- Moonshot-v1: mean=2.37, std=2.63, CV=1.11
- Qwen-Plus: mean=5.89, std=2.58, CV=0.44
- Qwen2.5-3B-Instruct: mean=2.74, std=1.92, CV=0.70
- Vicuna-7B-v1.3: mean=3.95, std=1.46, CV=0.37
- Yi-Lightning: mean=6.28, std=2.60, CV=0.41

## Files Generated
- `subject_lz_matrix.csv`: 12 models × 57 subjects lz*
- `category_lz_matrix.csv`: 12 models × 4 categories lz*
- `subject_accuracy_matrix.csv`: 12 models × 57 subjects accuracy
- `category_accuracy_matrix.csv`: 12 models × 4 categories accuracy
- `domain_heatmap.png`: Full heatmap (models × subjects)
- `category_heatmap.png`: Category-level heatmap
- `gemini_analysis.png`: Gemini-1.5 breakdown
- `all_models_scatter.png`: All models scatter
- `domain_summary.json`: Machine-readable summary