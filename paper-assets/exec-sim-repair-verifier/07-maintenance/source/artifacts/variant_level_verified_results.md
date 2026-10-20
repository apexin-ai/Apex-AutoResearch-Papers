## Verified Variant-Level Results

Generated: 2026-05-18

Ground truth: 48 variants (26 resolved, 22 unresolved). Majority baseline: 54.17%.
Aggregation rule: variant predicted "resolved" iff ALL per-test predictions = pass (AND rule).

---

### Qwen3-8B CLS s42 (per-variant breakdown)

Source: seetacloud `/root/autodl-tmp/eval_results/cls8b_s42_resume_ckpt3600_test_v2/eval_repo_cls_predictions.jsonl`
Per-test accuracy: 84.48% (9784 tests)

| variant_id | test_count | pass_count | fail_count | gt | pred | correct |
|---|---|---|---|---|---|---|
| astropy__astropy-7336__gold | 357 | 355 | 2 | 1 | 0 | N |
| astropy__astropy-7336__mutation_boundary_removal | 357 | 351 | 6 | 0 | 0 | Y |
| astropy__astropy-7336__mutation_operator_swap | 357 | 354 | 3 | 0 | 0 | Y |
| django__django-10880__gold | 73 | 73 | 0 | 1 | 1 | Y |
| django__django-10973__gold | 90 | 90 | 0 | 1 | 1 | Y |
| django__django-11848__gold | 79 | 61 | 18 | 1 | 0 | N |
| django__django-11848__mutation_off_by_one | 79 | 61 | 18 | 0 | 0 | Y |
| django__django-11848__mutation_operator_swap | 79 | 61 | 18 | 0 | 0 | Y |
| django__django-11880__gold | 132 | 132 | 0 | 1 | 1 | Y |
| django__django-12143__gold | 70 | 70 | 0 | 1 | 1 | Y |
| django__django-12325__gold | 237 | 237 | 0 | 1 | 1 | Y |
| django__django-12325__mutation_boundary_removal | 237 | 217 | 20 | 0 | 0 | Y |
| django__django-12325__mutation_operator_swap | 237 | 219 | 18 | 0 | 0 | Y |
| django__django-12406__gold | 219 | 182 | 37 | 1 | 0 | N |
| django__django-12406__mutation_operator_swap | 218 | 177 | 41 | 0 | 0 | Y |
| django__django-13109__gold | 206 | 206 | 0 | 1 | 1 | Y |
| django__django-14315__gold | 198 | 144 | 54 | 1 | 0 | N |
| django__django-14315__mutation_operator_swap | 197 | 0 | 197 | 0 | 0 | Y |
| django__django-14315__mutation_return_value | 198 | 18 | 180 | 0 | 0 | Y |
| django__django-14351__gold | 76 | 76 | 0 | 1 | 1 | Y |
| django__django-14351__mutation_boundary_removal | 76 | 75 | 1 | 1 | 0 | N |
| django__django-14351__mutation_return_value | 76 | 75 | 1 | 0 | 0 | Y |
| django__django-14376__gold | 60 | 60 | 0 | 1 | 1 | Y |
| django__django-14434__gold | 151 | 151 | 0 | 1 | 1 | Y |
| django__django-14631__gold | 153 | 153 | 0 | 1 | 1 | Y |
| django__django-14631__mutation_operator_swap | 153 | 0 | 153 | 0 | 0 | Y |
| django__django-14631__mutation_return_value | 153 | 151 | 2 | 0 | 0 | Y |
| django__django-15037__gold | 32 | 14 | 18 | 1 | 0 | N |
| django__django-15037__mutation_operator_swap | 32 | 32 | 0 | 0 | 1 | N |
| django__django-17029__gold | 61 | 61 | 0 | 1 | 1 | Y |
| matplotlib__matplotlib-24177__gold | 786 | 786 | 0 | 1 | 1 | Y |
| matplotlib__matplotlib-24177__mutation_operator_swap | 786 | 0 | 786 | 0 | 0 | Y |
| psf__requests-6028__gold | 221 | 221 | 0 | 1 | 1 | Y |
| psf__requests-6028__mutation_boundary_removal | 221 | 152 | 69 | 0 | 0 | Y |
| pydata__xarray-6992__gold | 1161 | 1143 | 18 | 1 | 0 | N |
| pydata__xarray-6992__mutation_operator_swap | 1161 | 1143 | 18 | 1 | 0 | N |
| pytest-dev__pytest-6202__gold | 90 | 90 | 0 | 1 | 1 | Y |
| pytest-dev__pytest-6202__mutation_return_value | 90 | 87 | 3 | 0 | 0 | Y |
| pytest-dev__pytest-7490__gold | 114 | 89 | 25 | 1 | 0 | N |
| pytest-dev__pytest-7490__mutation_boundary_removal | 114 | 55 | 59 | 0 | 0 | Y |
| pytest-dev__pytest-7490__mutation_operator_swap | 114 | 87 | 27 | 0 | 0 | Y |
| scikit-learn__scikit-learn-14053__gold | 23 | 23 | 0 | 1 | 1 | Y |
| scikit-learn__scikit-learn-14053__mutation_operator_swap | 23 | 5 | 18 | 0 | 0 | Y |
| sphinx-doc__sphinx-11445__gold | 44 | 42 | 2 | 1 | 0 | N |
| sphinx-doc__sphinx-11445__mutation_boundary_removal | 44 | 4 | 40 | 0 | 0 | Y |
| sphinx-doc__sphinx-11445__mutation_off_by_one | 44 | 42 | 2 | 1 | 0 | N |
| sympy__sympy-16886__mutation_off_by_one | 60 | 38 | 22 | 0 | 0 | Y |
| sympy__sympy-17655__mutation_return_value | 45 | 45 | 0 | 0 | 1 | N |

**Accuracy: 35/48 = 72.92%**

Errors (13): astropy-7336 gold, django-11848 gold, django-12406 gold, django-14315 gold, django-14351 mutation_boundary_removal, django-15037 gold, django-15037 mutation_operator_swap, pydata-xarray-6992 gold, pydata-xarray-6992 mutation_operator_swap, pytest-7490 gold, sphinx-11445 gold, sphinx-11445 mutation_off_by_one, sympy-17655 mutation_return_value

---

### Qwen3-8B CLS s123 (per-variant breakdown)

Source: seetacloud `/root/autodl-tmp/eval_results/cls8b_seed123_ckpt3000_test_mutation/eval_repo_cls_predictions.jsonl`
Per-test accuracy: 85.60% (9784 tests)

| variant_id | test_count | pass_count | fail_count | gt | pred | correct |
|---|---|---|---|---|---|---|
| astropy__astropy-7336__gold | 357 | 356 | 1 | 1 | 0 | N |
| astropy__astropy-7336__mutation_boundary_removal | 357 | 356 | 1 | 0 | 0 | Y |
| astropy__astropy-7336__mutation_operator_swap | 357 | 356 | 1 | 0 | 0 | Y |
| django__django-10880__gold | 73 | 73 | 0 | 1 | 1 | Y |
| django__django-10973__gold | 90 | 90 | 0 | 1 | 1 | Y |
| django__django-11848__gold | 79 | 61 | 18 | 1 | 0 | N |
| django__django-11848__mutation_off_by_one | 79 | 61 | 18 | 0 | 0 | Y |
| django__django-11848__mutation_operator_swap | 79 | 61 | 18 | 0 | 0 | Y |
| django__django-11880__gold | 132 | 132 | 0 | 1 | 1 | Y |
| django__django-12143__gold | 70 | 70 | 0 | 1 | 1 | Y |
| django__django-12325__gold | 237 | 237 | 0 | 1 | 1 | Y |
| django__django-12325__mutation_boundary_removal | 237 | 199 | 38 | 0 | 0 | Y |
| django__django-12325__mutation_operator_swap | 237 | 237 | 0 | 0 | 1 | N |
| django__django-12406__gold | 219 | 219 | 0 | 1 | 1 | Y |
| django__django-12406__mutation_operator_swap | 218 | 199 | 19 | 0 | 0 | Y |
| django__django-13109__gold | 206 | 206 | 0 | 1 | 1 | Y |
| django__django-14315__gold | 198 | 198 | 0 | 1 | 1 | Y |
| django__django-14315__mutation_operator_swap | 197 | 0 | 197 | 0 | 0 | Y |
| django__django-14315__mutation_return_value | 198 | 72 | 126 | 0 | 0 | Y |
| django__django-14351__gold | 76 | 76 | 0 | 1 | 1 | Y |
| django__django-14351__mutation_boundary_removal | 76 | 74 | 2 | 1 | 0 | N |
| django__django-14351__mutation_return_value | 76 | 76 | 0 | 0 | 1 | N |
| django__django-14376__gold | 60 | 60 | 0 | 1 | 1 | Y |
| django__django-14434__gold | 151 | 151 | 0 | 1 | 1 | Y |
| django__django-14631__gold | 153 | 153 | 0 | 1 | 1 | Y |
| django__django-14631__mutation_operator_swap | 153 | 0 | 153 | 0 | 0 | Y |
| django__django-14631__mutation_return_value | 153 | 152 | 1 | 0 | 0 | Y |
| django__django-15037__gold | 32 | 32 | 0 | 1 | 1 | Y |
| django__django-15037__mutation_operator_swap | 32 | 32 | 0 | 0 | 1 | N |
| django__django-17029__gold | 61 | 61 | 0 | 1 | 1 | Y |
| matplotlib__matplotlib-24177__gold | 786 | 786 | 0 | 1 | 1 | Y |
| matplotlib__matplotlib-24177__mutation_operator_swap | 786 | 1 | 785 | 0 | 0 | Y |
| psf__requests-6028__gold | 221 | 221 | 0 | 1 | 1 | Y |
| psf__requests-6028__mutation_boundary_removal | 221 | 174 | 47 | 0 | 0 | Y |
| pydata__xarray-6992__gold | 1161 | 1161 | 0 | 1 | 1 | Y |
| pydata__xarray-6992__mutation_operator_swap | 1161 | 1161 | 0 | 1 | 1 | Y |
| pytest-dev__pytest-6202__gold | 90 | 90 | 0 | 1 | 1 | Y |
| pytest-dev__pytest-6202__mutation_return_value | 90 | 90 | 0 | 0 | 1 | N |
| pytest-dev__pytest-7490__gold | 114 | 113 | 1 | 1 | 0 | N |
| pytest-dev__pytest-7490__mutation_boundary_removal | 114 | 77 | 37 | 0 | 0 | Y |
| pytest-dev__pytest-7490__mutation_operator_swap | 114 | 113 | 1 | 0 | 0 | Y |
| scikit-learn__scikit-learn-14053__gold | 23 | 23 | 0 | 1 | 1 | Y |
| scikit-learn__scikit-learn-14053__mutation_operator_swap | 23 | 5 | 18 | 0 | 0 | Y |
| sphinx-doc__sphinx-11445__gold | 44 | 44 | 0 | 1 | 1 | Y |
| sphinx-doc__sphinx-11445__mutation_boundary_removal | 44 | 43 | 1 | 0 | 0 | Y |
| sphinx-doc__sphinx-11445__mutation_off_by_one | 44 | 44 | 0 | 1 | 1 | Y |
| sympy__sympy-16886__mutation_off_by_one | 60 | 58 | 2 | 0 | 0 | Y |
| sympy__sympy-17655__mutation_return_value | 45 | 45 | 0 | 0 | 1 | N |

**Accuracy: 39/48 = 81.25%** (CONFIRMED)

Errors (9): astropy-7336 gold, django-11848 gold, django-12325 mutation_operator_swap, django-14351 mutation_boundary_removal, django-14351 mutation_return_value, django-15037 mutation_operator_swap, pytest-7490 gold, pytest-6202 mutation_return_value, sympy-17655 mutation_return_value

s123 fixes vs s42: django-12406 gold, django-14315 gold, django-15037 gold, pydata-xarray-6992 gold+mut, sphinx-11445 gold+off_by_one (+7)
s123 regresses vs s42: django-12325 mut_op_swap, django-14351 mut_return_value, pytest-6202 mut_return_value (-3)
Net: +4 variants

---

### Qwen3-4B CLS s42 ckpt4600 seq5120 (per-variant breakdown)

Source: home-1x5090 `/home/sonny/exec-sim-repair-verifier/results/repo_cls_v5_ckpt4600_test/eval_repo_cls_predictions.jsonl`
Per-test accuracy: 83.63% (8182/9784), 0 unparseable
Config: Qwen3-4B, checkpoint-4600, max_seq_length=5120

| variant_id | test_count | pass_count | fail_count | gt | pred | correct |
|---|---|---|---|---|---|---|
| astropy__astropy-7336__gold | 357 | 356 | 1 | 1 | 0 | N |
| astropy__astropy-7336__mutation_boundary_removal | 357 | 356 | 1 | 0 | 0 | Y |
| astropy__astropy-7336__mutation_operator_swap | 357 | 356 | 1 | 0 | 0 | Y |
| django__django-10880__gold | 73 | 73 | 0 | 1 | 1 | Y |
| django__django-10973__gold | 90 | 90 | 0 | 1 | 1 | Y |
| django__django-11848__gold | 79 | 79 | 0 | 1 | 1 | Y |
| django__django-11848__mutation_off_by_one | 79 | 79 | 0 | 0 | 1 | N |
| django__django-11848__mutation_operator_swap | 79 | 79 | 0 | 0 | 1 | N |
| django__django-11880__gold | 132 | 132 | 0 | 1 | 1 | Y |
| django__django-12143__gold | 70 | 70 | 0 | 1 | 1 | Y |
| django__django-12325__gold | 237 | 237 | 0 | 1 | 1 | Y |
| django__django-12325__mutation_boundary_removal | 237 | 211 | 26 | 0 | 0 | Y |
| django__django-12325__mutation_operator_swap | 237 | 237 | 0 | 0 | 1 | N |
| django__django-12406__gold | 219 | 199 | 20 | 1 | 0 | N |
| django__django-12406__mutation_operator_swap | 218 | 178 | 40 | 0 | 0 | Y |
| django__django-13109__gold | 206 | 206 | 0 | 1 | 1 | Y |
| django__django-14315__gold | 198 | 198 | 0 | 1 | 1 | Y |
| django__django-14315__mutation_operator_swap | 197 | 17 | 180 | 0 | 0 | Y |
| django__django-14315__mutation_return_value | 198 | 39 | 159 | 0 | 0 | Y |
| django__django-14351__gold | 76 | 75 | 1 | 1 | 0 | N |
| django__django-14351__mutation_boundary_removal | 76 | 75 | 1 | 1 | 0 | N |
| django__django-14351__mutation_return_value | 76 | 75 | 1 | 0 | 0 | Y |
| django__django-14376__gold | 60 | 60 | 0 | 1 | 1 | Y |
| django__django-14434__gold | 151 | 150 | 1 | 1 | 0 | N |
| django__django-14631__gold | 153 | 153 | 0 | 1 | 1 | Y |
| django__django-14631__mutation_operator_swap | 153 | 72 | 81 | 0 | 0 | Y |
| django__django-14631__mutation_return_value | 153 | 116 | 37 | 0 | 0 | Y |
| django__django-15037__gold | 32 | 32 | 0 | 1 | 1 | Y |
| django__django-15037__mutation_operator_swap | 32 | 32 | 0 | 0 | 1 | N |
| django__django-17029__gold | 61 | 61 | 0 | 1 | 1 | Y |
| matplotlib__matplotlib-24177__gold | 786 | 786 | 0 | 1 | 1 | Y |
| matplotlib__matplotlib-24177__mutation_operator_swap | 786 | 14 | 772 | 0 | 0 | Y |
| psf__requests-6028__gold | 221 | 186 | 35 | 1 | 0 | N |
| psf__requests-6028__mutation_boundary_removal | 221 | 183 | 38 | 0 | 0 | Y |
| pydata__xarray-6992__gold | 1161 | 1158 | 3 | 1 | 0 | N |
| pydata__xarray-6992__mutation_operator_swap | 1161 | 1158 | 3 | 1 | 0 | N |
| pytest-dev__pytest-6202__gold | 90 | 90 | 0 | 1 | 1 | Y |
| pytest-dev__pytest-6202__mutation_return_value | 90 | 90 | 0 | 0 | 1 | N |
| pytest-dev__pytest-7490__gold | 114 | 113 | 1 | 1 | 0 | N |
| pytest-dev__pytest-7490__mutation_boundary_removal | 114 | 83 | 31 | 0 | 0 | Y |
| pytest-dev__pytest-7490__mutation_operator_swap | 114 | 113 | 1 | 0 | 0 | Y |
| scikit-learn__scikit-learn-14053__gold | 23 | 23 | 0 | 1 | 1 | Y |
| scikit-learn__scikit-learn-14053__mutation_operator_swap | 23 | 23 | 0 | 0 | 1 | N |
| sphinx-doc__sphinx-11445__gold | 44 | 25 | 19 | 1 | 0 | N |
| sphinx-doc__sphinx-11445__mutation_boundary_removal | 44 | 6 | 38 | 0 | 0 | Y |
| sphinx-doc__sphinx-11445__mutation_off_by_one | 44 | 25 | 19 | 1 | 0 | N |
| sympy__sympy-16886__mutation_off_by_one | 60 | 57 | 3 | 0 | 0 | Y |
| sympy__sympy-17655__mutation_return_value | 45 | 24 | 21 | 0 | 0 | Y |

**Accuracy: 31/48 = 64.58%**

Note: Despite 83.63% per-test accuracy, variant-level drops to 64.58% because the model is heavily biased toward "pass" (recall_pass=96.57%, recall_fail=48.72%). Under the AND rule, even one missed "fail" test flips the variant prediction. For comparison, the earlier Qwen3-4B ckpt-600 seq2048 (76.92% per-test) achieves 68.75% variant-level due to more balanced fail recall (79.29%).

---

### Excluded: DeepSeek CLS s123 seq2048 (M006)

Source: seetacloud `/root/autodl-tmp/eval_results/deepseek_cls_repo_s123_test/predictions.jsonl`
Per-test accuracy: 82.62% (inflated)
Variant-level: 72.92% (inflated)

**Reason for exclusion**: 28.6% unparseable predictions defaulting to majority class ("pass"). This inflates both per-test and variant-level accuracy. The high pass-default rate artificially boosts the AND-rule variant metric.

**Canonical DeepSeek CLS values** (seq8192, no unparseable inflation):
- Per-test: 74.93%
- Variant-level: 27/48 = 56.25%

---

### Summary Table

| Model | Seed | Seq | Per-test | Variant (n=48) | Status |
|---|---|---|---|---|---|
| Qwen3-8B CLS | s42 | 8192 | 84.48% | 35/48 = 72.92% | Verified |
| Qwen3-8B CLS | s123 | 8192 | 85.60% | 39/48 = 81.25% | Verified |
| Qwen3-4B CLS (ckpt4600) | s42 | 5120 | 83.63% | 31/48 = 64.58% | Verified |
| DeepSeek CLS | s123 | 8192 | 74.93% | 27/48 = 56.25% | Canonical |
| DeepSeek CLS (seq2048) | s123 | 2048 | 82.62% | 35/48 = 72.92% | EXCLUDED |
