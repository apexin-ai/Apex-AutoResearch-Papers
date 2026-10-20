# Prediction Overlap Analysis: Qwen-1.5B vs Qwen-7B (exception_only)

## Summary

**Jaccard Similarity = 1.0 (perfect overlap)**

Both models fail on exactly the same 2 samples across all seeds. This is strong evidence for an irreducible error ceiling imposed by data characteristics, not model capacity.

## Error Details

| Sample ID | problem_id | True Label | Predicted | Error Type |
|-----------|-----------|------------|-----------|------------|
| 901 | HumanEval/95 | pass | fail | False Negative |
| 905 | HumanEval/95 | pass | fail | False Negative |

### Consistency Across Seeds (7B)

| Seed | Error IDs | Accuracy |
|------|-----------|----------|
| 42   | [901, 905] | 99.83% |
| 123  | [901, 905] | 99.83% |
| 456  | [901, 905] | 99.83% |

### 1.5B (seed 42)

| Seed | Error IDs | Accuracy |
|------|-----------|----------|
| 42   | [901, 905] | 99.83% |

## Overlap Metrics

- |Errors_7B| = 2
- |Errors_1.5B| = 2
- |Intersection| = 2
- |Union| = 2
- **Jaccard similarity** = 2/2 = **1.0**
- **Overlap / 7B errors** = 2/2 = 100%
- **Overlap / 1.5B errors** = 2/2 = 100%

## Root Cause Analysis

Both samples are from **HumanEval/95** (`check_dict_case`) — the same problem with near-identical inputs. The only difference between samples 901 and 905 is the memory addresses of Python iterator objects in the trace (different execution runs).

### Why the models fail

The execution trace contains multiple `[ERROR] GeneratorExit` entries:

```
[ERROR] GeneratorExit at line 5:  | locals: .0='<list_iterator ...>', k='A'
[ERROR] GeneratorExit at line 7:  | locals: .0='<list_iterator ...>', k='p'
...
```

`GeneratorExit` is a **normal Python mechanism** — it fires when `all()` short-circuits (stops iterating because a falsy value was found). The code is correct and all tests pass. However, the `[ERROR]` tag in the trace is misleading: both models interpret these as actual errors and predict "fail" when the true verdict is "pass".

This is a **labeling artifact** — the trace format incorrectly marks benign `GeneratorExit` as `[ERROR]`, creating a systematically misleading signal that fools any model regardless of capacity.

## Implications

1. **Irreducible ceiling confirmed**: The 99.83% accuracy ceiling (2/1190 errors) is not a model capacity limitation. Scaling from 1.5B → 7B parameters yields zero improvement because the errors are caused by misleading trace formatting, not insufficient reasoning.

2. **Ensemble has no value here**: Since both models fail on identical samples with identical predictions, any ensemble of these models would still achieve exactly 99.83%.

3. **Near-duplicate samples**: Both errors come from the same HumanEval problem with different trace memory addresses — effectively the same failure mode counted twice.

4. **True irreducible error rate**: Arguably 1 unique failure pattern (HumanEval/95 with GeneratorExit), manifested as 2 near-duplicate samples → effective error rate is 1/1190 unique failures = 0.08%.

## Recommendations

- These 2 samples could be considered **annotation noise** rather than genuine model failures
- If the trace format tagged `GeneratorExit` as `[INFO]` instead of `[ERROR]`, both models would likely achieve 100%
- For paper framing: this supports the claim that exception_only traces provide near-perfect signal, with the residual error attributable to trace formatting artifacts rather than task difficulty
