# Error Analysis Report: Trace-Verdict-Study

## 1. Dataset Overview

- **Total test samples**: 1190
- **Unique problems**: 119 (10 variants each)
- **Label distribution**: pass=851 (71.5%), fail=339 (28.5%)
- **Sources**: HumanEval (34 problems, 340 samples), MBPP (85 problems, 850 samples)
- **Model**: Qwen2.5-Coder-7B-Instruct, LoRA fine-tuned, seed=42

## 2. Accuracy and Error Summary

| Condition | Accuracy | Total Errors | FP (pred pass, actual fail) | FN (pred fail, actual pass) | FP:FN Ratio |
|-----------|----------|-------------|-----|-----|------|
| exception_only | 99.83% | 2 | 0 | 2 | 0:2 |
| vota | 99.41% | 7 | 0 | 7 | 0:7 |
| full_trace | 81.76% | 217 | 103 | 114 | 103:114 |
| no_trace | 75.13% | 296 | 90 | 206 | 90:206 |

## 3. Confusion Matrices

### exception_only (99.83%)

|  | Pred Pass | Pred Fail |
|--|-----------|-----------|
| **Actual Pass** | 849 (TP) | 2 (FN) |
| **Actual Fail** | 0 (FP) | 339 (TN) |

Pass: P=1.0000 R=0.9976 F1=0.9988
Fail: P=0.9941 R=1.0000 F1=0.9971

### vota (99.41%)

|  | Pred Pass | Pred Fail |
|--|-----------|-----------|
| **Actual Pass** | 844 (TP) | 7 (FN) |
| **Actual Fail** | 0 (FP) | 339 (TN) |

Pass: P=1.0000 R=0.9918 F1=0.9959
Fail: P=0.9798 R=1.0000 F1=0.9898

### full_trace (81.76%)

|  | Pred Pass | Pred Fail |
|--|-----------|-----------|
| **Actual Pass** | 737 (TP) | 114 (FN) |
| **Actual Fail** | 103 (FP) | 236 (TN) |

Pass: P=0.8774 R=0.8660 F1=0.8717
Fail: P=0.6743 R=0.6962 F1=0.6851

### no_trace (75.13%)

|  | Pred Pass | Pred Fail |
|--|-----------|-----------|
| **Actual Pass** | 645 (TP) | 206 (FN) |
| **Actual Fail** | 90 (FP) | 249 (TN) |

Pass: P=0.8776 R=0.7579 F1=0.8134
Fail: P=0.5473 R=0.7345 F1=0.6272

## 4. Failure Mode Analysis

### 4.1 exception_only (2 errors, 0.17% error rate)

Both errors are **false negatives** (predicted fail on passing code).

| Sample | Problem | Error Type | Root Cause |
|--------|---------|------------|------------|
| #901 | HumanEval/95 | GeneratorExit | Generator cleanup in `all()` with `islower()`/`isupper()` triggers GeneratorExit, which the model interprets as a real error |
| #905 | HumanEval/95 | GeneratorExit | Same problem, different code variant with identical GeneratorExit pattern |

**Root cause**: `GeneratorExit` is raised during normal generator cleanup (e.g., when `all()` short-circuits). The exception trace shows `[ERROR] GeneratorExit` markers, which the model correctly associates with failure, but in this case the GeneratorExit is benign. This is the one systematic blind spot of exception-only signal: exceptions that occur during normal Python runtime behavior, not from actual bugs.

### 4.2 vota (7 errors, 0.59% error rate)

All 7 errors are **false negatives** (predicted fail on passing code).

| Problem | Count | Error Pattern |
|---------|-------|---------------|
| MBPP/113 (`check_integer`) | 6 | Code has `try/except ValueError` that catches the error intentionally. The trace shows `[ERROR] ValueError` markers, but the code handles it correctly. ASSERT results show PASS but the verbose trace is confusing. |
| MBPP/794 (`text_starta_endb`) | 1 | Regex-based solution. Trace shows verbose module imports and ASSERT results; model misinterprets the long trace as failure signal. |

**Root cause**: VOTA includes both exception events and assert-level events. For MBPP/113, the ValueError is caught by try/except (intentional error handling), but the model sees `[ERROR] ValueError` in the trace and predicts fail. This is the key limitation of VOTA vs exception_only: the additional assert/call/return events introduce noise without adding discriminative power.

### 4.3 full_trace (217 errors, 18.24% error rate)

**Critical finding: 100% of wrong predictions have truncated traces.**

The full execution trace exceeds the 2048-token input limit, causing truncation. After truncation, the surviving trace text contains only low-level variable state dumps (module imports, memory addresses) with no error markers, assert results, or meaningful execution events.

| Error Type | Count | Pattern |
|------------|-------|---------|
| FP (pred pass, actual fail) | 103 | Trace truncated before error events. Model sees only benign variable state, defaults to 'pass'. |
| FN (pred fail, actual pass) | 114 | Trace truncated, leaving only verbose variable dumps. Model interprets noise as failure signal. |

**40 unique problems affected** (out of 119 total). Top problems:

| Problem | Errors/10 | Source |
|---------|-----------|--------|
| MBPP/284 | 10 | MBPP |
| MBPP/419 | 10 | MBPP |
| MBPP/422 | 10 | MBPP |
| MBPP/113 | 10 | MBPP |
| HumanEval/162 | 10 | HumanEval |
| MBPP/443 | 10 | MBPP |
| MBPP/754 | 10 | MBPP |
| HumanEval/120 | 10 | HumanEval |
| MBPP/638 | 9 | MBPP |
| MBPP/92 | 9 | MBPP |

Most problematic programs have all 10 variants misclassified, indicating systematic failure when the trace is too long.

**Source breakdown**: HumanEval 53/340 (15.6%), MBPP 164/850 (19.3%)

### 4.4 no_trace (296 errors, 24.87% error rate)

Without execution traces, the model relies entirely on code structure.

| Error Type | Count | Interpretation |
|------------|-------|----------------|
| FP (pred pass, actual fail) | 90 | Code looks correct but has subtle bugs the model cannot detect from syntax alone |
| FN (pred fail, actual pass) | 206 | Code looks suspicious but actually works. **Strong FN bias** (69.6% of errors) |

The FN dominance (206 vs 90) indicates the model has learned a conservative strategy: when uncertain, predict 'fail'. This makes sense given the test set has 71.5% pass labels; without trace evidence, the model over-corrects toward the minority class.

**Source breakdown**: HumanEval 99/340 (29.1%), MBPP 197/850 (23.2%)
HumanEval has higher error rate without traces, likely due to more complex logic patterns.

## 5. Cross-Condition Comparisons

### 5.1 Pairwise Error Overlap

| A vs B | Both Correct | Both Wrong | Only A Wrong | Only B Wrong |
|--------|:---:|:---:|:---:|:---:|
| exception_only vs vota | 1181 | 0 | 2 | 7 |
| exception_only vs full_trace | 971 | 0 | 2 | 217 |
| exception_only vs no_trace | 892 | 0 | 2 | 296 |
| vota vs full_trace | 973 | 7 | 0 | 210 |
| vota vs no_trace | 894 | 7 | 0 | 289 |
| full_trace vs no_trace | 833 | 156 | 61 | 140 |

### 5.2 exception_only vs vota

- **Zero overlap** in errors: exception_only's 2 errors (GeneratorExit) are completely different from vota's 7 errors (ValueError/regex)
- exception_only has higher accuracy (99.83% vs 99.41%) with fewer, more targeted errors
- vota's 5 additional errors come from exception events being embedded in a noisier context (assert results, call/return events)

### 5.3 Tier 1 (exception_only) vs Tier 2 (full_trace)

- **Zero shared errors**: exception_only's 2 errors are all correctly classified by full_trace
- full_trace has 217 unique errors that exception_only handles perfectly
- The additional 215 errors in full_trace are **entirely due to trace truncation**, not inherent difficulty
- This proves that exception events are not just *sufficient* but *superior* to full traces for verdict prediction

### 5.4 Trace vs No-Trace

- **140 no_trace errors fixed by any trace condition** (from 26 unique problems)
  - These represent genuine recoverable signal from execution traces
  - Direction: 106 were FN (pass misclassified as fail), 34 were FP
- **156 errors shared by both full_trace and no_trace** (from 32 problems)
  - These are 'hard' programs where truncated traces don't help
- **61 errors unique to full_trace** (61 samples)
  - Trace truncation actively *hurts*: these samples are correctly classified with no trace but wrong with a truncated full trace

### 5.5 Hardest Problems

**Problems with errors in 3+ conditions**: 3

| Problem | Conditions with errors |
|---------|----------------------|
| HumanEval/95 | exception_only, full_trace, no_trace |
| MBPP/113 | full_trace, no_trace, vota |
| MBPP/794 | full_trace, no_trace, vota |

## 6. Paper-Ready Key Findings

1. **Exception-only signal achieves near-perfect accuracy (99.83%) with a single, interpretable failure mode.** Both errors stem from `GeneratorExit` during Python generator cleanup in `all()` calls, a benign runtime event that produces misleading `[ERROR]` markers. This is a fundamental limitation of treating all exceptions as error signals, but affects only 2/1190 samples (0.17%).

2. **Full execution traces degrade performance to 81.76% due to information overload, not task difficulty.** All 217 errors (100%) occur in samples where the trace exceeds the 2048-token limit, causing truncation that removes all diagnostic markers (errors, assertions). The surviving trace text contains only low-level variable state dumps that the model cannot interpret. This confirms that verbose traces create a signal-to-noise problem, not a signal-richness advantage.

3. **Execution traces provide genuine, recoverable signal.** 140 of the no-trace baseline's 296 errors (47.3%) are fixed by any trace-augmented condition, concentrated in 26 unique problems. The recovered errors are predominantly false negatives (106/140), where the model without traces defaults to a conservative 'fail' prediction on actually-passing code. Exception events alone recover all of these cases.

## 7. Appendix: Error Indices by Condition

### exception_only (2 errors)

- #901: HumanEval/95, FN (label=pass, pred=fail)
- #905: HumanEval/95, FN (label=pass, pred=fail)

### vota (7 errors)

- #345: MBPP/794, FN (label=pass, pred=fail)
- #540: MBPP/113, FN (label=pass, pred=fail)
- #541: MBPP/113, FN (label=pass, pred=fail)
- #542: MBPP/113, FN (label=pass, pred=fail)
- #543: MBPP/113, FN (label=pass, pred=fail)
- #548: MBPP/113, FN (label=pass, pred=fail)
- #549: MBPP/113, FN (label=pass, pred=fail)

### full_trace (217 errors)

FP: 103 samples, FN: 114 samples
Across 40 unique problems.

### no_trace (296 errors)

FP: 90 samples, FN: 206 samples
Across 46 unique problems.