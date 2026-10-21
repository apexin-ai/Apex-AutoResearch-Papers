# Error Analysis: Trace Condition Failure Modes (Plan 018)

**Date**: 2026-05-21  
**Test set**: 1190 samples  
**Conditions analyzed**: ae_only, exception_only, full_trace, full_trace_label_only, loop_only, no_trace, vota, vota_no_ae  

## 1. Confusion Matrix Summary

| Condition | Accuracy | TP | FP | TN | FN | Total Errors |
|-----------|----------|----|----|----|----|-------------|
| ae_only | 99.92% | 850 | 0 | 339 | 1 | 1 |
| exception_only | 99.83% | 849 | 0 | 339 | 2 | 2 |
| vota | 99.41% | 844 | 0 | 339 | 7 | 7 |
| vota_no_ae | 99.41% | 845 | 1 | 338 | 6 | 7 |
| full_trace_label_only | 86.22% | 793 | 106 | 233 | 58 | 164 |
| loop_only | 85.63% | 741 | 61 | 278 | 110 | 171 |
| full_trace | 81.76% | 737 | 103 | 236 | 114 | 217 |
| no_trace | 75.13% | 645 | 90 | 249 | 206 | 296 |

## 2. Error Distribution by Error Type

### ae_only (acc=99.92%)
- **All errors**: {'no_error': 1}
- **FP** (pred=pass, actual=fail): {}
- **FN** (pred=fail, actual=pass): {'no_error': 1}

### exception_only (acc=99.83%)
- **All errors**: {'no_error': 2}
- **FP** (pred=pass, actual=fail): {}
- **FN** (pred=fail, actual=pass): {'no_error': 2}

### vota (acc=99.83%)
- **All errors**: {'no_error': 7}
- **FP** (pred=pass, actual=fail): {}
- **FN** (pred=fail, actual=pass): {'no_error': 7}

### vota_no_ae (acc=99.41%)
- **All errors**: {'no_error': 6, 'AssertionError': 1}
- **FP** (pred=pass, actual=fail): {'AssertionError': 1}
- **FN** (pred=fail, actual=pass): {'no_error': 6}

### full_trace_label_only (acc=86.22%)
- **All errors**: {'AssertionError': 97, 'no_error': 58, 'SyntaxError': 5, 'Timeout': 4}
- **FP** (pred=pass, actual=fail): {'AssertionError': 97, 'SyntaxError': 5, 'Timeout': 4}
- **FN** (pred=fail, actual=pass): {'no_error': 58}

### loop_only (acc=85.63%)
- **All errors**: {'no_error': 110, 'AssertionError': 61}
- **FP** (pred=pass, actual=fail): {'AssertionError': 61}
- **FN** (pred=fail, actual=pass): {'no_error': 110}

### full_trace (acc=81.76%)
- **All errors**: {'no_error': 114, 'AssertionError': 91, 'AttributeError': 8, 'Timeout': 2, 'SyntaxError': 2}
- **FP** (pred=pass, actual=fail): {'AssertionError': 91, 'AttributeError': 8, 'Timeout': 2, 'SyntaxError': 2}
- **FN** (pred=fail, actual=pass): {'no_error': 114}

### no_trace (acc=75.13%)
- **All errors**: {'no_error': 206, 'AssertionError': 67, 'SyntaxError': 23}
- **FP** (pred=pass, actual=fail): {'AssertionError': 67, 'SyntaxError': 23}
- **FN** (pred=fail, actual=pass): {'no_error': 206}

## 3. Tier Analysis

- **Tier 1** (exception_only, vota, ae_only): 9 unique error samples
- **Tier 2** (full_trace, loop_only, no_trace, full_trace_label_only): 430 unique error samples
- **Overlap**: 7 samples wrong in both tiers
- **Tier 1 unique** (wrong in Tier 1 only): 2
- **Tier 2 unique** (wrong in Tier 2 only): 423
- **Tier 1 errors ⊂ Tier 2 errors**: False

Tier 2 unique error types: {'no_error': 260, 'AssertionError': 126, 'SyntaxError': 24, 'AttributeError': 8, 'Timeout': 5}
Tier 2 unique sources: {'humaneval': 137, 'mbpp': 286}

## 4. Cross-Condition Error Consistency

- Never wrong (all conditions correct): **758** / 1190
- Wrong in at least 1 condition: **432**
- Wrong in ALL conditions: **0** (inherently hard)
- Tier 1 all correct but Tier 2 has errors: **423**

**Distribution of errors across conditions:**

| # Conditions Wrong | # Samples |
|-------------------|-----------|
| 1 | 225 |
| 2 | 67 |
| 3 | 61 |
| 4 | 72 |
| 5 | 7 |

**Tier 1 correct / Tier 2 wrong**: error types = {'no_error': 260, 'AssertionError': 126, 'SyntaxError': 24, 'AttributeError': 8, 'Timeout': 5}
- Sources: {'humaneval': 137, 'mbpp': 286}
- Labels: {'pass': 260, 'fail': 163}

## 5. FP vs FN Bias

| Condition | FP | FP Rate | FN | FN Rate | Bias |
|-----------|----|---------|----|---------|------|
| ae_only | 0 | 0.0% | 1 | 0.12% | FN-biased |
| exception_only | 0 | 0.0% | 2 | 0.24% | FN-biased |
| vota | 0 | 0.0% | 7 | 0.82% | FN-biased |
| vota_no_ae | 1 | 0.29% | 6 | 0.71% | FN-biased |
| full_trace_label_only | 106 | 31.27% | 58 | 6.82% | FP-biased |
| loop_only | 61 | 17.99% | 110 | 12.93% | FN-biased |
| full_trace | 103 | 30.38% | 114 | 13.4% | FN-biased |
| no_trace | 90 | 26.55% | 206 | 24.21% | FN-biased |

## 6. Error Rate by Solution Length

### ae_only
| Length Bin | Errors / Total | Error Rate |
|-----------|----------------|------------|
| 1-5 lines | 1/859 | 0.12% |
| 6-10 | 0/276 | 0.0% |
| 11-20 | 0/35 | 0.0% |
| 21-50 | 0/20 | 0.0% |

### exception_only
| Length Bin | Errors / Total | Error Rate |
|-----------|----------------|------------|
| 1-5 lines | 0/859 | 0.0% |
| 6-10 | 2/276 | 0.72% |
| 11-20 | 0/35 | 0.0% |
| 21-50 | 0/20 | 0.0% |

### vota
| Length Bin | Errors / Total | Error Rate |
|-----------|----------------|------------|
| 1-5 lines | 1/859 | 0.12% |
| 6-10 | 6/276 | 2.17% |
| 11-20 | 0/35 | 0.0% |
| 21-50 | 0/20 | 0.0% |

### vota_no_ae
| Length Bin | Errors / Total | Error Rate |
|-----------|----------------|------------|
| 1-5 lines | 0/859 | 0.0% |
| 6-10 | 7/276 | 2.54% |
| 11-20 | 0/35 | 0.0% |
| 21-50 | 0/20 | 0.0% |

### full_trace_label_only
| Length Bin | Errors / Total | Error Rate |
|-----------|----------------|------------|
| 1-5 lines | 106/859 | 12.34% |
| 6-10 | 48/276 | 17.39% |
| 11-20 | 0/35 | 0.0% |
| 21-50 | 10/20 | 50.0% |

### loop_only
| Length Bin | Errors / Total | Error Rate |
|-----------|----------------|------------|
| 1-5 lines | 105/859 | 12.22% |
| 6-10 | 59/276 | 21.38% |
| 11-20 | 5/35 | 14.29% |
| 21-50 | 2/20 | 10.0% |

### full_trace
| Length Bin | Errors / Total | Error Rate |
|-----------|----------------|------------|
| 1-5 lines | 141/859 | 16.41% |
| 6-10 | 63/276 | 22.83% |
| 11-20 | 4/35 | 11.43% |
| 21-50 | 9/20 | 45.0% |

### no_trace
| Length Bin | Errors / Total | Error Rate |
|-----------|----------------|------------|
| 1-5 lines | 197/859 | 22.93% |
| 6-10 | 68/276 | 24.64% |
| 11-20 | 22/35 | 62.86% |
| 21-50 | 9/20 | 45.0% |

## 7. Key Pairwise Comparisons

### exception_only correct & no_trace wrong: 296 samples
- Error types: {'no_error': 206, 'AssertionError': 67, 'SyntaxError': 23}
- Sources: {'mbpp': 197, 'humaneval': 99}
- Labels: {'pass': 206, 'fail': 90}

### exception_only correct & full_trace wrong: 217 samples
- Error types: {'no_error': 114, 'AssertionError': 91, 'AttributeError': 8, 'Timeout': 2, 'SyntaxError': 2}
- Sources: {'humaneval': 53, 'mbpp': 164}
- Labels: {'pass': 114, 'fail': 103}

## 8. Test Set Statistics

- Total: 1190
- Labels: {'fail': 339, 'pass': 851}
- Sources: {'humaneval': 340, 'mbpp': 850}
- Error types: {'no_error': 851, 'AssertionError': 176, 'SyntaxError': 68, 'TypeError': 50, 'NameError': 21, 'Timeout': 14, 'AttributeError': 10}
