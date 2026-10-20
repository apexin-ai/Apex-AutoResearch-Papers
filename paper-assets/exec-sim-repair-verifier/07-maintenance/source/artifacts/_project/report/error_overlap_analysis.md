# Error Overlap Analysis & Per-class F1 Breakdown (4B Function-level)

**Date**: 2026-05-12
**Models**: CLS (2 seeds: 42, 0) × CWM (2 seeds: 123, 789) = 4 pairs
**Test set**: 1890 samples (978 pass, 912 fail)

---

## 1. Error Overlap Analysis

### Aggregate (4 pairs)

| Metric | Value |
|--------|-------|
| Agreement rate | 94.7% |
| Both correct | ~84.5% |
| CLS-only correct | 3.0% (~57 samples) |
| CWM-only correct | 2.3% (~44 samples) |
| Both wrong | ~10.0% (~189 samples) |
| **CLS net advantage** | **+0.7pp** |

### Mutation-type breakdown (mean CLS-only vs CWM-only correct samples)

| Mutation type | CLS-only | CWM-only | Net CLS advantage |
|---------------|----------|----------|--------------------|
| off_by_one | 28 | 18 | **+10.0** |
| original | 8 | 16 | **-8.5** (CWM better) |
| operator_swap | 12 | 6 | **+6.5** |
| variable_swap | 5 | 0 | **+4.5** |
| return_value | 2 | 2 | 0.0 |
| boundary_removal | 0 | 0 | 0.0 |

**Key finding**: CLS's advantage concentrates on mutation types (off_by_one, operator_swap, variable_swap). CWM is actually better on original (unmutated) code by ~8.5 samples per pair.

### Both-wrong samples

Both-wrong samples are heavily skewed toward the **pass class** (130-142 per pair) vs fail class (47-63). Both models share a systematic weakness in predicting pass for certain samples.

---

## 2. Per-class F1 Comparison

### Average across seeds

| Metric | CLS | CWM | Δ (CLS−CWM) |
|--------|-----|-----|-------------|
| Accuracy | 87.65 | 86.98 | **+0.67pp** |
| Pass F1 | 87.39 | 86.90 | +0.49pp |
| Fail F1 | 87.89 | 87.07 | **+0.82pp** |
| Pass Precision | 92.62 | 90.74 | **+1.88pp** |
| Pass Recall | 82.72 | 83.38 | -0.66pp (CWM better) |
| Fail Precision | 83.38 | 83.62 | -0.24pp |
| Fail Recall | 92.92 | 90.84 | **+2.08pp** |

**CLS advantage pattern**: Higher fail recall (+2.08pp) and pass precision (+1.88pp). CLS is better at catching failures (fewer FN) and more conservative in predicting pass (fewer FP).

### Per-mutation-type accuracy

| Mutation type | CLS acc | CWM acc | Δacc |
|---------------|---------|---------|------|
| variable_swap | 93.5 | 88.2 | **+5.3** |
| operator_swap | 87.1 | 84.9 | **+2.2** |
| off_by_one | 82.5 | 81.0 | **+1.5** |
| original | 85.3 | 87.4 | **-2.1** (CWM better) |
| return_value | 97.4 | 97.4 | 0.0 |
| boundary_removal | 91.7 | 91.7 | 0.0 |

---

## 3. Interpretation

1. **CLS advantage is mutation-specific, not uniform.** CLS outperforms CWM on subtle code mutations (variable_swap +5.3pp, operator_swap +2.2pp, off_by_one +1.5pp). On original code, CWM is 2.1pp better.

2. **CLS has stronger fail detection.** +2.08pp fail recall is the primary accuracy driver. Direct binary training signal provides clearer learning target for fail cases.

3. **~95% agreement.** Disagreement zone (~5%) where CLS has +0.7pp net edge. Supports "complexity-dependent advantage" hypothesis.

4. **CWM wins on original code.** Generation-based reasoning may capture semantic properties better when code is unmodified. CLS advantage is a **mutation detection** advantage specifically.

---

## 4. Data

- Script: `analysis_error_overlap.py`
- Report JSON: `analysis_error_overlap_report.json`
- Predictions: `predictions_cls_seed{42,0}.jsonl`, `predictions_cwm_seed{123,789}.jsonl`
- 2 CLS × 2 CWM = 4 pairs analyzed
