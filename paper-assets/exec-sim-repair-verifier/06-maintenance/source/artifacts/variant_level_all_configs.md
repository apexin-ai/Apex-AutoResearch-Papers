# Variant-Level Aggregation Results (AND Rule, n=48)

Generated: 2026-05-18

## Setup
- 48 unique variants (problem_id + mutation_type)
- 9784 per-test predictions aggregated to variant level
- AND rule: variant = resolved iff ALL tests predicted pass
- Ground truth: 26 resolved, 22 unresolved (majority baseline = 54.17%)

## Summary Table

| Config | Form | Model | Seed | Per-test Acc | Variant Acc | Coverage |
|--------|------|-------|------|-------------|-------------|----------|
| DeepSeek-6.7B TRAJ s42 | TRAJ | DeepSeek-6.7B | 42 | N/A | **81.25%** | N/A |
| DeepSeek-6.7B TRAJ s123 | TRAJ | DeepSeek-6.7B | 123 | N/A | **75.00%** | N/A |
| Qwen3-8B CLS s42 | CLS | Qwen3-8B | 42 | 84.48% | **72.92%** | 9784/9784 |
| Qwen3-8B CLS s123 | CLS | Qwen3-8B | 123 | 85.60% | **81.25%** | 9784/9784 |
| Qwen3-4B CLS s42 | CLS | Qwen3-4B | 42 | 76.92% | **68.75%** | 9784/9784 |
| DeepSeek CLS s123 (seq8192) | CLS | DeepSeek-6.7B | 123 | 74.93% | **56.25%** | 9784/9784 |
| DeepSeek CLS s123 (seq2048) | CLS | DeepSeek-6.7B | 123 | 82.62% | **72.92%** | 9784/9784 |
| DeepSeek CLS s42 (v4, seq8192) | CLS | DeepSeek-6.7B | 42 | 71.29% | **58.33%** | 9784/9784 |
| Qwen3-8B CWM s42 | CWM | Qwen3-8B | 42 | 65.17% | **52.08%** | 9784/9784 |
| DeepSeek CWM s123 | CWM | DeepSeek-6.7B | 123 | 61.46% | **47.92%** | 7210/9784 * |
| DeepSeek CWM s42 | CWM | DeepSeek-6.7B | 42 | 56.79% | **47.92%** | 7668/9784 * |

\* Incomplete predictions; AND rule applied only to covered tests. May overestimate "resolved" for partially covered variants.

## Per-Config Error Details

### Qwen3-8B CLS s42 (72.92%, 13 errors)

| Variant | GT | Pred | #Tests | #Pass | #Fail |
|---------|---:|-----:|-------:|------:|------:|
| astropy__astropy-7336__gold | 1 | 0 | 357 | 355 | 2 |
| django__django-11848__gold | 1 | 0 | 79 | 61 | 18 |
| django__django-12406__gold | 1 | 0 | 219 | 182 | 37 |
| django__django-14315__gold | 1 | 0 | 198 | 144 | 54 |
| django__django-14351__mutation_boundary_removal | 1 | 0 | 76 | 75 | 1 |
| django__django-15037__gold | 1 | 0 | 32 | 14 | 18 |
| django__django-15037__mutation_operator_swap | 0 | 1 | 32 | 32 | 0 |
| pydata__xarray-6992__gold | 1 | 0 | 1161 | 1143 | 18 |
| pydata__xarray-6992__mutation_operator_swap | 1 | 0 | 1161 | 1143 | 18 |
| pytest-dev__pytest-7490__gold | 1 | 0 | 114 | 89 | 25 |
| sphinx-doc__sphinx-11445__gold | 1 | 0 | 44 | 42 | 2 |
| sphinx-doc__sphinx-11445__mutation_off_by_one | 1 | 0 | 44 | 42 | 2 |
| sympy__sympy-17655__mutation_return_value | 0 | 1 | 45 | 45 | 0 |

### Qwen3-8B CLS s123 (81.25%, 9 errors)

| Variant | GT | Pred | #Tests | #Pass | #Fail |
|---------|---:|-----:|-------:|------:|------:|
| astropy__astropy-7336__gold | 1 | 0 | 357 | 356 | 1 |
| django__django-11848__gold | 1 | 0 | 79 | 61 | 18 |
| django__django-12325__mutation_operator_swap | 0 | 1 | 237 | 237 | 0 |
| django__django-14351__mutation_boundary_removal | 1 | 0 | 76 | 74 | 2 |
| django__django-14351__mutation_return_value | 0 | 1 | 76 | 76 | 0 |
| django__django-15037__mutation_operator_swap | 0 | 1 | 32 | 32 | 0 |
| pytest-dev__pytest-6202__mutation_return_value | 0 | 1 | 90 | 90 | 0 |
| sphinx-doc__sphinx-11445__mutation_off_by_one | 1 | 0 | 44 | 42 | 2 |
| sympy__sympy-17655__mutation_return_value | 0 | 1 | 45 | 45 | 0 |

### Qwen3-4B CLS s42 (68.75%, 15 errors)

| Variant | GT | Pred | #Tests | #Pass | #Fail |
|---------|---:|-----:|-------:|------:|------:|
| astropy__astropy-7336__gold | 1 | 0 | 357 | 326 | 31 |
| django__django-11848__gold | 1 | 0 | 79 | 61 | 18 |
| django__django-12406__gold | 1 | 0 | 219 | 175 | 44 |
| django__django-14315__gold | 1 | 0 | 198 | 11 | 187 |
| django__django-14351__mutation_boundary_removal | 1 | 0 | 76 | 73 | 3 |
| django__django-15037__gold | 1 | 0 | 32 | 14 | 18 |
| django__django-15037__mutation_operator_swap | 0 | 1 | 32 | 32 | 0 |
| matplotlib__matplotlib-24177__gold | 1 | 0 | 786 | 785 | 1 |
| pydata__xarray-6992__gold | 1 | 0 | 1161 | 1143 | 18 |
| pydata__xarray-6992__mutation_operator_swap | 1 | 0 | 1161 | 1143 | 18 |
| pytest-dev__pytest-7490__gold | 1 | 0 | 114 | 83 | 31 |
| sphinx-doc__sphinx-11445__gold | 1 | 0 | 44 | 19 | 25 |
| sphinx-doc__sphinx-11445__mutation_off_by_one | 1 | 0 | 44 | 19 | 25 |
| sympy__sympy-16886__mutation_off_by_one | 0 | 1 | 60 | 60 | 0 |
| sympy__sympy-17655__mutation_return_value | 0 | 1 | 45 | 45 | 0 |

### DeepSeek CLS s123 seq8192 (56.25%, 21 errors)

| Variant | GT | Pred | #Tests | #Pass | #Fail |
|---------|---:|-----:|-------:|------:|------:|
| astropy__astropy-7336__gold | 1 | 0 | 357 | 326 | 31 |
| django__django-10880__gold | 1 | 0 | 73 | 72 | 1 |
| django__django-11848__gold | 1 | 0 | 79 | 63 | 16 |
| django__django-12143__gold | 1 | 0 | 70 | 69 | 1 |
| django__django-12325__gold | 1 | 0 | 237 | 216 | 21 |
| django__django-12406__gold | 1 | 0 | 219 | 174 | 45 |
| django__django-13109__gold | 1 | 0 | 206 | 205 | 1 |
| django__django-14315__gold | 1 | 0 | 198 | 5 | 193 |
| django__django-14351__gold | 1 | 0 | 76 | 75 | 1 |
| django__django-14351__mutation_boundary_removal | 1 | 0 | 76 | 73 | 3 |
| django__django-14376__gold | 1 | 0 | 60 | 58 | 2 |
| django__django-14434__gold | 1 | 0 | 151 | 150 | 1 |
| django__django-14631__gold | 1 | 0 | 153 | 152 | 1 |
| django__django-15037__gold | 1 | 0 | 32 | 14 | 18 |
| django__django-15037__mutation_operator_swap | 0 | 1 | 32 | 32 | 0 |
| django__django-17029__gold | 1 | 0 | 61 | 60 | 1 |
| pydata__xarray-6992__gold | 1 | 0 | 1161 | 1127 | 34 |
| pydata__xarray-6992__mutation_operator_swap | 1 | 0 | 1161 | 1125 | 36 |
| pytest-dev__pytest-7490__gold | 1 | 0 | 114 | 88 | 26 |
| sphinx-doc__sphinx-11445__gold | 1 | 0 | 44 | 31 | 13 |
| sphinx-doc__sphinx-11445__mutation_off_by_one | 1 | 0 | 44 | 30 | 14 |

### DeepSeek CLS s123 seq2048 (72.92%, 13 errors)

| Variant | GT | Pred | #Tests | #Pass | #Fail |
|---------|---:|-----:|-------:|------:|------:|
| astropy__astropy-7336__gold | 1 | 0 | 357 | 297 | 60 |
| django__django-11848__gold | 1 | 0 | 79 | 62 | 17 |
| django__django-12325__gold | 1 | 0 | 237 | 216 | 21 |
| django__django-12406__gold | 1 | 0 | 219 | 173 | 46 |
| django__django-14315__gold | 1 | 0 | 198 | 4 | 194 |
| django__django-14351__mutation_boundary_removal | 1 | 0 | 76 | 73 | 3 |
| django__django-15037__gold | 1 | 0 | 32 | 14 | 18 |
| django__django-15037__mutation_operator_swap | 0 | 1 | 32 | 32 | 0 |
| pydata__xarray-6992__gold | 1 | 0 | 1161 | 1132 | 29 |
| pydata__xarray-6992__mutation_operator_swap | 1 | 0 | 1161 | 1132 | 29 |
| pytest-dev__pytest-7490__gold | 1 | 0 | 114 | 82 | 32 |
| sphinx-doc__sphinx-11445__gold | 1 | 0 | 44 | 17 | 27 |
| sphinx-doc__sphinx-11445__mutation_off_by_one | 1 | 0 | 44 | 14 | 30 |

### DeepSeek CLS s42 v4 seq8192 (58.33%, 20 errors)

| Variant | GT | Pred | #Tests | #Pass | #Fail |
|---------|---:|-----:|-------:|------:|------:|
| astropy__astropy-7336__gold | 1 | 0 | 357 | 321 | 36 |
| django__django-10973__gold | 1 | 0 | 90 | 89 | 1 |
| django__django-11848__gold | 1 | 0 | 79 | 62 | 17 |
| django__django-12325__gold | 1 | 0 | 237 | 218 | 19 |
| django__django-12406__gold | 1 | 0 | 219 | 171 | 48 |
| django__django-13109__gold | 1 | 0 | 206 | 205 | 1 |
| django__django-14315__gold | 1 | 0 | 198 | 4 | 194 |
| django__django-14351__gold | 1 | 0 | 76 | 75 | 1 |
| django__django-14351__mutation_boundary_removal | 1 | 0 | 76 | 73 | 3 |
| django__django-14434__gold | 1 | 0 | 151 | 150 | 1 |
| django__django-14631__gold | 1 | 0 | 153 | 152 | 1 |
| django__django-15037__gold | 1 | 0 | 32 | 14 | 18 |
| django__django-15037__mutation_operator_swap | 0 | 1 | 32 | 32 | 0 |
| django__django-17029__gold | 1 | 0 | 61 | 60 | 1 |
| pydata__xarray-6992__gold | 1 | 0 | 1161 | 1130 | 31 |
| pydata__xarray-6992__mutation_operator_swap | 1 | 0 | 1161 | 1128 | 33 |
| pytest-dev__pytest-7490__gold | 1 | 0 | 114 | 87 | 27 |
| sphinx-doc__sphinx-11445__gold | 1 | 0 | 44 | 30 | 14 |
| sphinx-doc__sphinx-11445__mutation_off_by_one | 1 | 0 | 44 | 29 | 15 |
| sympy__sympy-17655__mutation_return_value | 0 | 1 | 45 | 45 | 0 |

### Qwen3-8B CWM s42 (52.08%, 23 errors)

| Variant | GT | Pred | #Tests | #Pass | #Fail |
|---------|---:|-----:|-------:|------:|------:|
| astropy__astropy-7336__gold | 1 | 0 | 357 | 6 | 351 |
| django__django-10880__gold | 1 | 0 | 73 | 45 | 28 |
| django__django-11848__gold | 1 | 0 | 79 | 47 | 32 |
| django__django-12143__gold | 1 | 0 | 70 | 69 | 1 |
| django__django-12325__gold | 1 | 0 | 237 | 83 | 154 |
| django__django-12406__gold | 1 | 0 | 219 | 113 | 106 |
| django__django-13109__gold | 1 | 0 | 206 | 7 | 199 |
| django__django-14315__gold | 1 | 0 | 198 | 134 | 64 |
| django__django-14351__gold | 1 | 0 | 76 | 69 | 7 |
| django__django-14351__mutation_boundary_removal | 1 | 0 | 76 | 38 | 38 |
| django__django-14376__gold | 1 | 0 | 60 | 5 | 55 |
| django__django-14434__gold | 1 | 0 | 151 | 136 | 15 |
| django__django-14631__gold | 1 | 0 | 153 | 67 | 86 |
| django__django-15037__gold | 1 | 0 | 32 | 14 | 18 |
| django__django-15037__mutation_operator_swap | 0 | 1 | 32 | 32 | 0 |
| django__django-17029__gold | 1 | 0 | 61 | 9 | 52 |
| matplotlib__matplotlib-24177__gold | 1 | 0 | 786 | 605 | 181 |
| psf__requests-6028__gold | 1 | 0 | 221 | 88 | 133 |
| pydata__xarray-6992__gold | 1 | 0 | 1161 | 498 | 663 |
| pydata__xarray-6992__mutation_operator_swap | 1 | 0 | 1161 | 491 | 670 |
| pytest-dev__pytest-7490__gold | 1 | 0 | 114 | 45 | 69 |
| sphinx-doc__sphinx-11445__gold | 1 | 0 | 44 | 27 | 17 |
| sphinx-doc__sphinx-11445__mutation_off_by_one | 1 | 0 | 44 | 26 | 18 |

### DeepSeek CWM s123 (47.92%, 25 errors, INCOMPLETE 7210/9784)

| Variant | GT | Pred | #Tot | #Cov | #Pass | #Fail |
|---------|---:|-----:|-----:|-----:|------:|------:|
| astropy__astropy-7336__gold | 1 | 0 | 357 | 271 | 4 | 267 |
| django__django-10880__gold | 1 | 0 | 73 | 53 | 42 | 11 |
| django__django-10973__gold | 1 | 0 | 90 | 71 | 1 | 70 |
| django__django-11848__gold | 1 | 0 | 79 | 64 | 36 | 28 |
| django__django-11880__gold | 1 | 0 | 132 | 98 | 83 | 15 |
| django__django-12143__gold | 1 | 0 | 70 | 53 | 35 | 18 |
| django__django-12325__gold | 1 | 0 | 237 | 177 | 153 | 24 |
| django__django-12406__gold | 1 | 0 | 219 | 165 | 118 | 47 |
| django__django-13109__gold | 1 | 0 | 206 | 138 | 109 | 29 |
| django__django-14315__gold | 1 | 0 | 198 | 150 | 33 | 117 |
| django__django-14351__gold | 1 | 0 | 76 | 58 | 22 | 36 |
| django__django-14351__mutation_boundary_removal | 1 | 0 | 76 | 58 | 11 | 47 |
| django__django-14376__gold | 1 | 0 | 60 | 42 | 4 | 38 |
| django__django-14434__gold | 1 | 0 | 151 | 117 | 111 | 6 |
| django__django-14631__gold | 1 | 0 | 153 | 124 | 69 | 55 |
| django__django-15037__gold | 1 | 0 | 32 | 25 | 8 | 17 |
| django__django-17029__gold | 1 | 0 | 61 | 48 | 11 | 37 |
| matplotlib__matplotlib-24177__gold | 1 | 0 | 786 | 564 | 437 | 127 |
| psf__requests-6028__gold | 1 | 0 | 221 | 162 | 130 | 32 |
| pydata__xarray-6992__gold | 1 | 0 | 1161 | 849 | 651 | 198 |
| pydata__xarray-6992__mutation_operator_swap | 1 | 0 | 1161 | 865 | 714 | 151 |
| pytest-dev__pytest-6202__gold | 1 | 0 | 90 | 67 | 42 | 25 |
| pytest-dev__pytest-7490__gold | 1 | 0 | 114 | 82 | 73 | 9 |
| scikit-learn__scikit-learn-14053__gold | 1 | 0 | 23 | 16 | 15 | 1 |
| sphinx-doc__sphinx-11445__gold | 1 | 0 | 44 | 33 | 16 | 17 |

### DeepSeek CWM s42 (47.92%, 25 errors, INCOMPLETE 7668/9784)

| Variant | GT | Pred | #Tot | #Cov | #Pass | #Fail |
|---------|---:|-----:|-----:|-----:|------:|------:|
| astropy__astropy-7336__gold | 1 | 0 | 357 | 282 | 41 | 241 |
| django__django-10880__gold | 1 | 0 | 73 | 53 | 43 | 10 |
| django__django-10973__gold | 1 | 0 | 90 | 71 | 0 | 71 |
| django__django-11848__gold | 1 | 0 | 79 | 64 | 27 | 37 |
| django__django-11880__gold | 1 | 0 | 132 | 104 | 89 | 15 |
| django__django-12143__gold | 1 | 0 | 70 | 53 | 26 | 27 |
| django__django-12325__gold | 1 | 0 | 237 | 191 | 102 | 89 |
| django__django-12406__gold | 1 | 0 | 219 | 173 | 123 | 50 |
| django__django-13109__gold | 1 | 0 | 206 | 145 | 115 | 30 |
| django__django-14315__gold | 1 | 0 | 198 | 152 | 43 | 109 |
| django__django-14351__gold | 1 | 0 | 76 | 58 | 36 | 22 |
| django__django-14351__mutation_boundary_removal | 1 | 0 | 76 | 59 | 17 | 42 |
| django__django-14376__gold | 1 | 0 | 60 | 49 | 31 | 18 |
| django__django-14434__gold | 1 | 0 | 151 | 122 | 107 | 15 |
| django__django-14631__gold | 1 | 0 | 153 | 128 | 88 | 40 |
| django__django-15037__gold | 1 | 0 | 32 | 26 | 8 | 18 |
| django__django-17029__gold | 1 | 0 | 61 | 49 | 45 | 4 |
| matplotlib__matplotlib-24177__gold | 1 | 0 | 786 | 598 | 441 | 157 |
| psf__requests-6028__gold | 1 | 0 | 221 | 173 | 131 | 42 |
| pydata__xarray-6992__gold | 1 | 0 | 1161 | 900 | 655 | 245 |
| pydata__xarray-6992__mutation_operator_swap | 1 | 0 | 1161 | 917 | 677 | 240 |
| pytest-dev__pytest-6202__gold | 1 | 0 | 90 | 70 | 57 | 13 |
| pytest-dev__pytest-7490__gold | 1 | 0 | 114 | 84 | 72 | 12 |
| sphinx-doc__sphinx-11445__gold | 1 | 0 | 44 | 35 | 34 | 1 |
| sphinx-doc__sphinx-11445__mutation_off_by_one | 1 | 0 | 44 | 36 | 35 | 1 |

## Key Observations

1. **CLS outperforms CWM at variant level**: Best CLS (Qwen3-8B s123) = 81.25% vs best CWM (Qwen3-8B s42) = 52.08%. The AND rule severely penalizes CWM's higher per-test error rate.

2. **Gap amplification**: Qwen3-8B CLS s42 has 84.48% per-test accuracy but only 72.92% variant accuracy. CWM drops from 65.17% per-test to 52.08% variant. This confirms the gap amplification effect under AND aggregation.

3. **CWM error pattern**: CWM errors are almost exclusively false negatives (predicting fail when GT is resolved). All 23 CWM errors for Qwen3-8B are GT=1, Pred=0. CWM rarely produces false positives, which is expected since getting ALL tests to predicted-pass requires high confidence.

4. **Common hard variants across CLS models**: django__django-11848__gold and sphinx-doc__sphinx-11445__* are consistently misclassified across models.

5. **DeepSeek CWM incomplete**: Both DeepSeek CWM configs have ~74-78% test coverage. Results should be interpreted cautiously.

## Missing Configs (Not Available)
- Qwen3-4B CWM s42: No prediction file found
- Qwen3-8B CWM s123: No prediction file found

## Data Files
- Script: `/home/sonny/exec-sim-repair-verifier/aggregate_variant_level_v2.py`
- JSON results: `/home/sonny/exec-sim-repair-verifier/artifacts/variant_level_all_configs.json`
