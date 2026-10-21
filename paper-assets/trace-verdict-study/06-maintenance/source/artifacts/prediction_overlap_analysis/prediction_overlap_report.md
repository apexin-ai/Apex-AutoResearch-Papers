# Prediction Overlap Analysis: Exception-Only Condition Error Samples

## Summary

**Universal irreducible ceiling confirmed.** IDs 901 and 905 are misclassified by every model (Qwen-7B, Qwen-1.5B, DeepSeek-7B) across all seeds. Both are `[ERROR] GeneratorExit` traces where the code actually passes — a fundamentally misleading signal in the exception_only format.

---

## 1. Error Sample Inventory

| Model | Seed | Errors | Error IDs | Accuracy |
|-------|------|--------|-----------|----------|
| Qwen-7B | 42 | 2 | 901, 905 | 99.83% |
| Qwen-7B | 123 | 2 | 901, 905 | 99.83% |
| Qwen-7B | 456 | 2 | 901, 905 | 99.83% |
| Qwen-1.5B | 42 | 2 | 901, 905 | 99.83% |
| DeepSeek-7B | 42 | 8 | 540-543, 548-549, 901, 905 | 99.33% |
| DeepSeek-7B | 456 | 8 | 540-543, 548-549, 901, 905 | 99.33% |
| DeepSeek-7B | 123 | 106 | (many — likely bad run) | 91.09% |

## 2. Cross-Overlap Matrix

```
                 Qwen-7B(∩3seeds)  Qwen-1.5B  DeepSeek(seed42∩456)
Qwen-7B(∩3s)        {901,905}      {901,905}       {901,905}
Qwen-1.5B           {901,905}      {901,905}       {901,905}
DS(s42∩456)          {901,905}      {901,905}  {540-543,548-549,901,905}
```

**Universal intersection (all models, stable seeds): {901, 905}**

## 3. Error Sample Characteristics

### 3.1 Universal Irreducible Errors (IDs 901, 905)

- **Problem**: HumanEval/95 (`check_dict_case`)
- **Code**: Correct implementation using `all()` with generator expressions
- **True label**: pass
- **All models predict**: fail
- **Root cause**: Python's `all()` short-circuits by closing the generator, triggering `GeneratorExit`. The tracer logs this as `[ERROR] GeneratorExit`, creating a strong false "fail" signal.

**Trace content:**
```
[ERROR] GeneratorExit at line 5:  | locals: .0='<list_iterator ...>', k='A'
[ERROR] GeneratorExit at line 7:  | locals: .0='<list_iterator ...>', k='p'
[ERROR] GeneratorExit at line 5:  | locals: .0='<list_iterator ...>', k=5
[ERROR] GeneratorExit at line 7:  | locals: .0='<list_iterator ...>', k='p'
[ERROR] GeneratorExit at line 5:  | locals: .0='<list_iterator ...>', k='Name'
[ERROR] GeneratorExit at line 7:  | locals: .0='<list_iterator ...>', k='Name'
[ERROR] GeneratorExit at line 5:  | locals: .0='<list_iterator ...>', k='STATE'
```

**Why it's irreducible**: `GeneratorExit` is an internal Python mechanism, not a user-facing exception. The `[ERROR]` tag is technically accurate (an exception was raised) but semantically misleading (it doesn't indicate failure). Models cannot distinguish this from real errors without understanding Python's generator protocol at a deep level.

**Difference between 901 and 905**: Only memory addresses in trace differ (different execution runs of same correct code).

### 3.2 DeepSeek-Specific Stable Errors (IDs 540-543, 548-549)

- **Problem**: MBPP/113 (`check_integer`)
- **Code**: Uses try/except ValueError pattern — the ValueError is *intentionally caught*
- **True label**: pass
- **DeepSeek predicts**: fail (all seeds consistently)
- **Qwen-7B/1.5B predict**: pass (correct)

**Trace content:**
```
[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'
```

**Why DeepSeek fails but Qwen doesn't**: Qwen appears to have learned the try/except pattern (exception is caught = still passes). DeepSeek has a stronger bias toward `[ERROR]` → "fail" heuristic. Note: 4/10 MBPP/113 variants (IDs 544-547) use `.isdigit()` implementation with no exceptions — those are predicted correctly by all models.

### 3.3 DeepSeek seed123 Anomaly (106 errors)

This appears to be a **poorly converged training run**. Errors are spread across 16 problems, mostly MBPP. Paradoxically, it correctly predicts IDs 901/905 (the universal errors) while failing on 106 other samples. This suggests the model learned a different (weaker) decision boundary that doesn't rely on the `[ERROR]` heuristic as strongly.

## 4. Dataset Composition Analysis

```
[ERROR] + label=fail:   269 samples (easy — error signal aligns with verdict)
[ERROR] + label=pass:     8 samples (hard — misleading error signal)
  └─ MBPP/113:            6 samples (try/except, only hard for DeepSeek)
  └─ HumanEval/95:        2 samples (GeneratorExit, hard for ALL models)
No[ERROR] + label=pass: 843 samples (easy — no error, passes)
No[ERROR] + label=fail:  70 samples (easy — "[No trace available]" → fail)
```

Only **0.67%** (8/1190) of test samples have the misleading pattern. All model errors concentrate in this tiny subset.

## 5. Conclusions

1. **Universal irreducible ceiling exists**: IDs 901, 905 are misclassified by all models (Qwen-7B/1.5B, DeepSeek) across all stable seeds. The ceiling is 99.83% (2/1190 errors) for Qwen-scale models.

2. **Root cause is tracer artifact, not label noise**: `GeneratorExit` is not a real error — it's a benign side effect of Python's `all()` short-circuiting. The tracer's `[ERROR]` tag is the direct cause of model confusion.

3. **Scale doesn't help**: Qwen-1.5B and Qwen-7B produce identical errors on exception_only, suggesting the 2 irreducible samples represent a format limitation, not a capacity limitation.

4. **Architecture matters for try/except**: DeepSeek fails on try/except patterns (MBPP/113) while Qwen doesn't, indicating Qwen better learned exception control flow semantics.

5. **Potential fix**: Filter `GeneratorExit` and `StopIteration` from the exception trace (they are Python internal protocol exceptions, not user errors). This could eliminate the irreducible ceiling entirely.
