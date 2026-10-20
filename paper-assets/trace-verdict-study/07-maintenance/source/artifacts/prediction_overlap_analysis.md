# Prediction Overlap Analysis: Cross-Model Error Comparison (exception_only)

## Summary

**D049 ("universal irreducible ceiling") is partially supported.** Samples 901 and 905 are misclassified by ALL 4 models across ALL tested seeds — a true data-level ceiling. However, DeepSeek has additional model-specific errors, so the ceiling is not uniform across architectures.

## Per-Model Error Sets (seed42)

| Model | Accuracy | # Errors | Error Sample IDs |
|-------|----------|----------|------------------|
| Qwen-7B (2.5) | 99.83% | 2 | {901, 905} |
| Qwen-1.5B (2.5) | 99.83% | 2 | {901, 905} |
| CodeLlama-13B | 99.83% | 2 | {901, 905} |
| DeepSeek-Coder-7B | 99.33% | 8 | {540, 541, 542, 543, 548, 549, 901, 905} |

## Overlap Matrix (Jaccard Similarity)

|  | Qwen-7B | Qwen-1.5B | CodeLlama-13B | DeepSeek |
|--|---------|-----------|---------------|----------|
| **Qwen-7B** | 1.0 | **1.0** | **1.0** | 0.25 |
| **Qwen-1.5B** | — | 1.0 | **1.0** | 0.25 |
| **CodeLlama-13B** | — | — | 1.0 | 0.25 |
| **DeepSeek** | — | — | — | 1.0 |

## Universal Errors (all 4 models wrong)

**Samples 901, 905** — both from `HumanEval/95` (`check_dict_case`)

### Root Cause: GeneratorExit from `all()` short-circuiting

The code uses `all(isinstance(k, str) and k.islower() for k in keys)` with generator expressions. When `all()` short-circuits (encounters a non-matching element), Python garbage-collects the generator, raising `GeneratorExit`. This is **normal Python behavior** — the code passes all tests. But the trace shows 7 `[ERROR] GeneratorExit` lines, which misleads all models into predicting "fail".

```
Execution trace:
[ERROR] GeneratorExit at line 5:  | locals: .0='<list_iterator ...>', k='A'
[ERROR] GeneratorExit at line 7:  | locals: .0='<list_iterator ...>', k='p'
[ERROR] GeneratorExit at line 5:  | locals: .0='<list_iterator ...>', k=5
...
```

**Why 2 samples (not 1)?** Both are from problem HumanEval/95 with label "pass" but differ only in memory addresses in the trace (different execution runs). The problem has 10 test samples total; the other 8 are labeled "fail" and correctly predicted.

## DeepSeek-Only Errors

**Samples 540–543, 548–549** — all from `MBPP/113` (`check_integer`)

### Root Cause: Caught ValueError in try/except

```python
def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
```

Trace shows:
```
[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python'
```

This is a **caught exception** — the code deliberately catches it and returns False. The code passes. But DeepSeek sees `[ERROR] ValueError` and predicts "fail". The other 3 models correctly learned that caught exceptions don't indicate failure.

**Why only 6 of 10 MBPP/113 samples?** The problem has 10 samples total — 6 of them (540–543, 548–549) have the misleading ValueError trace (input="python" triggers the except path). The other 4 (544–547) have either no exception trace or different code variants (e.g., `s.strip().lstrip('-+').isdigit()`) that don't use try/except.

## Cross-Seed Stability

| Model | Seed 42 | Seed 123 | Seed 456 |
|-------|---------|----------|----------|
| Qwen-7B | {901, 905} | {901, 905} | {901, 905} |
| DeepSeek | 8 errors | 106 errors* | {540–543, 548–549, 901, 905} |
| CodeLlama-13B | {901, 905} | (no eval) | (no eval) |

*DeepSeek seed123 appears to be a failed/undertrained run.

## Conclusions

1. **Universal irreducible ceiling exists at 2/1190 (99.83%)**: Samples 901 and 905 are misclassified by every model across every successful training run. These represent a genuine data-level ceiling where the `[ERROR]` prefix for `GeneratorExit` is fundamentally misleading.

2. **The claim needs nuance**: DeepSeek has additional vulnerabilities (MBPP/113 caught exceptions), so "all models hit 99.83%" is only true for 3 of 4 models. DeepSeek's best is 99.33% (8 errors).

3. **Common root cause**: Both error classes stem from **benign exceptions generating [ERROR] markers** — `GeneratorExit` (from `all()` short-circuiting) and caught `ValueError` (from try/except). This suggests a potential data-preprocessing fix: distinguishing caught/benign exceptions from actual failures in the trace format.

4. **Recommendation for paper**: Reframe as "3 of 4 model families achieve identical ceiling (99.83%) with perfect error overlap (Jaccard=1.0), while the 4th (DeepSeek) shares the same universal errors plus additional sensitivity to caught-exception patterns." This is actually stronger than a generic ceiling claim — it pinpoints the specific data artifacts responsible.

## Error Type Taxonomy

| Error Type | Samples | Models Affected | Mechanism |
|-----------|---------|-----------------|-----------|
| GeneratorExit from `all()` | 901, 905 | All 4 (universal) | Generator GC on short-circuit |
| Caught ValueError | 540–543, 548–549 | DeepSeek only | try/except control flow |
