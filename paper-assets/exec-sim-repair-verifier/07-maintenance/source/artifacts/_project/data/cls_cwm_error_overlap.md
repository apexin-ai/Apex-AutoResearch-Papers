## CLS vs CWM Error Overlap (seed42, n=1890)

| Category | Count | Pct |
|----------|-------|-----|
| Both correct | 1601 | 84.71% |
| CLS-only correct | 59 | 3.12% |
| CWM-only correct | 53 | 2.80% |
| Both wrong | 177 | 9.37% |

Oracle combination accuracy: 90.63%
Cohen's Kappa (predictions): 0.88
Cohen's Kappa (correctness): 0.73

Per mutation type complementarity:
- off_by_one: CWM-only 4.8%, both wrong 14.9% (most complementary)
- operator_swap: CWM-only 5.7%
- return_value: 96.8% both correct (least complementary)

CWM weakest: off_by_one (81.82%), original (85.18%), operator_swap (88.59%)
CWM strongest: return_value (97.01%), variable_swap (94.12%)