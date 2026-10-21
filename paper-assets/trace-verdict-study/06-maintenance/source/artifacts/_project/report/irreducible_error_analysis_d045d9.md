# Irreducible Error Analysis: exception_only Condition

## Summary

The `exception_only` condition achieves 99.83% accuracy across all 3 seeds (42/123/456) on Qwen-2.5-Coder-7B, with exactly 2/1190 errors per seed. All 3 seeds misclassify the **identical 2 samples**, confirming these are deterministic, irreducible errors — not stochastic training variance.

## Error Samples

| Sample ID | Problem | True Label | Predicted | Error Type |
|-----------|---------|------------|-----------|------------|
| 901 | HumanEval/95 | pass | fail | False Negative |
| 905 | HumanEval/95 | pass | fail | False Negative |

Both samples contain the **same correct code** for `check_dict_case()`. The only difference between them is memory addresses in the execution trace (runtime artifacts, semantically identical).

## Root Cause: `GeneratorExit` as Misleading Error Signal

### The Code (correct, passes all tests)

```python
def check_dict_case(d):
    if not d:
        return False
    keys = list(d.keys())
    if all(isinstance(k, str) and k.islower() for k in keys):
        return True
    if all(isinstance(k, str) and k.isupper() for k in keys):
        return True
    return False
```

### The Trace (misleading)

```
[ERROR] GeneratorExit at line 5:  | locals: .0='<list_iterator ...>', k='A'
[ERROR] GeneratorExit at line 7:  | locals: .0='<list_iterator ...>', k='p'
[ERROR] GeneratorExit at line 5:  | locals: .0='<list_iterator ...>', k=5
[ERROR] GeneratorExit at line 7:  | locals: .0='<list_iterator ...>', k='p'
[ERROR] GeneratorExit at line 5:  | locals: .0='<list_iterator ...>', k='Name'
[ERROR] GeneratorExit at line 7:  | locals: .0='<list_iterator ...>', k='Name'
[ERROR] GeneratorExit at line 5:  | locals: .0='<list_iterator ...>', k='STATE'
```

### Why `GeneratorExit` appears

`GeneratorExit` is a Python internal exception (inherits from `BaseException`, not `Exception`) raised when a generator is garbage-collected before being fully consumed. When `all()` short-circuits — finding a `False` value before exhausting the generator — it discards the generator object, triggering `GeneratorExit`.

For example, with input `{"p": "pineapple", "A": "banana", "B": "banana"}`:
1. `all(isinstance(k, str) and k.islower() for k in keys)` evaluates:
   - k="p" → True (continue)
   - k="A" → False → `all()` returns False, generator discarded → **GeneratorExit**
2. `all(isinstance(k, str) and k.isupper() for k in keys)` evaluates:
   - k="p" → False → `all()` returns False, generator discarded → **GeneratorExit**

The tracer captured these as `[ERROR]` because `GeneratorExit` is technically an exception. But it is **completely benign** — the code works correctly.

### Why the model is misled

In the `exception_only` condition, the model sees:
- 7 lines tagged `[ERROR]`
- Exception type `GeneratorExit`
- No other context to distinguish this from genuine errors

For comparison, actual **fail** samples from the same problem (HumanEval/95) show:
- id=902: `[ERROR] AttributeError: 'int' object has no attribute 'islower'` — real bug
- id=903: `[ERROR] AssertionError: Third test error: True` — real test failure

The model has learned that `[ERROR]` lines indicate failing code. With 7 `[ERROR]` lines in a single trace, the "fail" prediction is a reasonable but wrong inference.

## Context: HumanEval/95 in the Test Set

HumanEval/95 has 10 samples total: 8 fail + 2 pass. The model correctly classifies all 8 fail samples. Only the 2 pass samples (which uniquely contain `GeneratorExit`) are misclassified.

No other samples in the entire 1190-sample test set contain `GeneratorExit`.

## Why This Is Truly Irreducible

1. **Representation limitation**: In the exception_only condition, the model has no access to control flow, return values, or assertion outcomes — only exception data. `GeneratorExit` from `all()` short-circuiting is indistinguishable from a real error in this representation.
2. **Deterministic across seeds**: All 3 random seeds produce the same errors, confirming this is a property of the data/representation, not model initialization.
3. **Unique phenomenon**: `GeneratorExit` only appears in these 2 samples. The model has no training signal to learn that `GeneratorExit` can be benign.
4. **Even a human would struggle**: Given only the exception trace (7 `[ERROR]` lines), a human reviewer would likely also predict "fail" without specific knowledge of Python's generator protocol.

## Implications for the Paper

- **Headline result stands**: 99.83% accuracy with 2 irreducible errors is effectively a ceiling for the exception_only representation on this test set.
- **Cross-model consistency**: DeepSeek exception_only seed42 also achieves 99.83% — verify if it errors on the same 2 samples.
- **Discussion point**: These errors illustrate a fundamental gap between Python's exception hierarchy (where `GeneratorExit` is a `BaseException` but not an error) and the tracer's `[ERROR]` tagging. A more nuanced tracer that distinguishes `BaseException` subclasses from `Exception` subclasses could potentially eliminate these errors.
- **Labeling is correct**: The code genuinely passes all tests. The trace is technically accurate (GeneratorExit does occur). The issue is in the interpretation layer — the `[ERROR]` tag applied by the tracer to all caught exceptions, regardless of severity.
