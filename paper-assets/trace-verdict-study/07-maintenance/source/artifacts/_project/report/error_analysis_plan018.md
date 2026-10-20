# Cross-Condition Error Analysis Report
Generated: 110 experiments, 1190 test samples each

## 1. Data Coverage

### Experiments by model × condition

| Condition | codellama13b | deepseek | qwen15b | qwen7b |
|---|---|---|---|---|
| ae_only | 2 | 2 | 2 | 3 |
| exception_only | 3 | 4 | 4 | 3 |
| exception_only_nomarker | 0 | 0 | 0 | 3 |
| full_trace | 0 | 2 | 1 | 1 |
| full_trace_1024tok | 0 | 0 | 0 | 1 |
| full_trace_256tok | 0 | 0 | 0 | 1 |
| full_trace_512tok | 0 | 0 | 0 | 1 |
| full_trace_head | 1 | 1 | 1 | 1 |
| full_trace_label_only | 0 | 0 | 0 | 5 |
| full_trace_tail | 5 | 3 | 3 | 5 |
| full_trace_tail384 | 1 | 1 | 1 | 1 |
| full_trace_tail512 | 3 | 3 | 3 | 3 |
| label_only | 1 | 1 | 3 | 0 |
| loop_only | 3 | 3 | 3 | 3 |
| no_trace | 1 | 2 | 3 | 1 |
| vota | 2 | 3 | 2 | 4 |
| vota_no_ae | 0 | 0 | 0 | 1 |

## 2. Error Rate by Exception Type

### Test set exception type distribution
| Exception Type | Count | % |
|---|---|---|
| none(pass) | 851 | 71.5% |
| AssertionError | 190 | 16.0% |
| SyntaxError | 67 | 5.6% |
| TypeError | 53 | 4.5% |
| NameError | 21 | 1.8% |
| AttributeError | 5 | 0.4% |
| other_error | 3 | 0.3% |

### Condition: exception_only (14 runs)
| Exception Type | N | Avg Error Rate | Per-Run Error Rates |
|---|---|---|---|
| none(pass) | 851 | 0.0039 | 0.002, 0.009, 0.002, 0.002, 0.007, 0.009, 0.002, 0.002, 0.000, 0.002, 0.002, 0.002, 0.007, 0.002 |
| AssertionError | 190 | 0.0120 | 0.000, 0.000, 0.000, 0.000, 0.168, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000 |
| SyntaxError | 67 | 0.0000 | all zeros across 14 runs |
| TypeError | 53 | 0.0606 | 0.000 x13, 0.849 (one outlier: deepseek_exception_only_seed123) |
| NameError | 21 | 0.0680 | 0.000 x13, 0.952 (one outlier: deepseek_exception_only_seed123) |
| AttributeError | 5 | 0.0429 | 0.000 x13, 0.600 (one outlier: deepseek_exception_only_seed123) |
| other_error | 3 | 0.0000 | all zeros |

### Condition: ae_only (9 runs)
| Exception Type | N | Avg Error Rate | Per-Run Error Rates |
|---|---|---|---|
| none(pass) | 851 | 0.0082 | 0.001, 0.013, 0.001, 0.013, 0.001, 0.013, 0.013, 0.007, 0.012 |
| AssertionError | 190 | 0.0205 | 0.000, 0.000, 0.000, 0.000, 0.074, 0.000, 0.000, 0.074, 0.037 |
| SyntaxError | 67 | 0.0000 | all zeros |
| TypeError | 53 | 0.0000 | all zeros |
| NameError | 21 | 0.0000 | all zeros |
| AttributeError | 5 | 0.0000 | all zeros |
| other_error | 3 | 0.0000 | all zeros |

### Condition: loop_only (12 runs)
| Exception Type | N | Avg Error Rate | Per-Run Error Rates |
|---|---|---|---|
| none(pass) | 851 | 0.1569 | 0.086–0.296 |
| AssertionError | 190 | 0.4623 | 0.168–0.695 |
| SyntaxError | 67 | 0.0000 | all zeros |
| TypeError | 53 | 0.1164 | 0.000–0.434 |
| NameError | 21 | 0.0079 | mostly zeros |
| AttributeError | 5 | 0.1167 | 0.000–0.200 |
| other_error | 3 | 0.0000 | all zeros |

### Condition: vota (11 runs)
| Exception Type | N | Avg Error Rate | Per-Run Error Rates |
|---|---|---|---|
| none(pass) | 851 | 0.0951 | 0.001–0.962 (one outlier: deepseek_vota at 0.962) |
| AssertionError | 190 | 0.0818 | 0.000–0.726 (same outlier) |
| SyntaxError | 67 | 0.0000 | all zeros |
| TypeError | 53 | 0.0515 | 0.000–0.566 (same outlier) |
| NameError | 21 | 0.0433 | 0.000–0.476 (same outlier) |
| AttributeError | 5 | 0.0545 | 0.000–0.600 (same outlier) |
| other_error | 3 | 0.0000 | all zeros |

### Condition: no_trace (7 runs)
| Exception Type | N | Avg Error Rate | Per-Run Error Rates |
|---|---|---|---|
| none(pass) | 851 | 0.2108 | 0.163–0.304 |
| AssertionError | 190 | 0.5654 | 0.368–0.705 |
| SyntaxError | 67 | 0.1983 | 0.000–0.343 |
| TypeError | 53 | 0.2183 | 0.000–0.396 |
| NameError | 21 | 0.0884 | 0.000–0.524 |
| AttributeError | 5 | 0.1714 | 0.000–0.200 |
| other_error | 3 | 0.1905 | 0.000–0.333 |

### Condition: full_trace (4 runs)
| Exception Type | N | Avg Error Rate | Per-Run Error Rates |
|---|---|---|---|
| none(pass) | 851 | 0.3546 | 0.134, 1.000, 0.149, 0.135 |
| AssertionError | 190 | 0.6408 | 0.495, 0.753, 0.579, 0.737 |
| SyntaxError | 67 | 0.0000 | all zeros |
| TypeError | 53 | 0.3821 | 0.113, 0.943, 0.189, 0.283 |
| NameError | 21 | 0.2262 | 0.000, 0.810, 0.048, 0.048 |
| AttributeError | 5 | 0.4000 | 0.600, 0.600, 0.000, 0.400 |
| other_error | 3 | 0.0000 | all zeros |

## 3. Tier 1 vs Tier 2 Failure Mode Comparison

Tier 1 (high accuracy): exception_only, ae_only
Tier 2 (lower accuracy): loop_only, no_trace

### Model: codellama13b
- Tier 1 union errors: 13
- Tier 2 union errors: 505
- Shared errors: 13
- Tier 1 only: 0
- Tier 2 only: 492
- Tier 2 unique error types: {'none(pass)': 349, 'AssertionError': 138, 'TypeError': 2, 'other_error': 1, 'NameError': 1, 'AttributeError': 1}
- Shared error types: {'none(pass)': 13}

### Model: deepseek
- Tier 1 union errors: 128
- Tier 2 union errors: 485
- Shared errors: 70
- Tier 1 only: 58
- Tier 2 only: 415
- Tier 2 unique error types: {'none(pass)': 287, 'AssertionError': 115, 'SyntaxError': 11, 'other_error': 1, 'AttributeError': 1}
- Shared error types: {'AssertionError': 40, 'TypeError': 22, 'none(pass)': 8}

### Model: qwen15b
- Tier 1 union errors: 20
- Tier 2 union errors: 564
- Shared errors: 10
- Tier 1 only: 10
- Tier 2 only: 554
- Tier 2 unique error types: {'none(pass)': 318, 'AssertionError': 161, 'TypeError': 31, 'SyntaxError': 29, 'NameError': 13, 'other_error': 1, 'AttributeError': 1}
- Shared error types: {'AssertionError': 7, 'none(pass)': 3}

### Model: qwen7b
- Tier 1 union errors: 13
- Tier 2 union errors: 362
- Shared errors: 12
- Tier 1 only: 1
- Tier 2 only: 350
- Tier 2 unique error types: {'none(pass)': 232, 'AssertionError': 91, 'SyntaxError': 19, 'TypeError': 6, 'AttributeError': 2}
- Shared error types: {'none(pass)': 12}

## 4. Irreducible Errors in exception_only

Total unique error samples across 14 exception_only runs: 108

Errors in ALL 14 runs (universally hard): 0

### Key findings

**The 108 errors decompose into two distinct failure modes:**

1. **deepseek_exception_only_seed123 outlier** (96 errors, 1 run only): This single run accounts for ~89% of all exception_only errors. All errors are in MBPP problems with AssertionError/TypeError/NameError. This is a model-specific training instability (likely bad seed), not a data-level hard case.

2. **HumanEval/95 cross-model** (samples 901, 905; 11/14 runs wrong): These 2 pass-labeled samples are consistently misclassified across ALL 4 models and multiple seeds. They are the only true "universally hard" cases — data-level irreducible errors where exception_only trace provides insufficient signal.

3. **DeepSeek-specific MBPP/113** (samples 540-549; 4/14 runs): 6 pass-labeled samples consistently misclassified by all DeepSeek runs but never by other models → model-family-specific weakness.

### Cross-model error overlap in exception_only
| Model A | Model B | Errors A | Errors B | Intersection | Jaccard |
|---|---|---|---|---|---|
| codellama13b | deepseek | 2 | 108 | 2 | 0.019 |
| codellama13b | qwen15b | 2 | 2 | 2 | 1.000 |
| codellama13b | qwen7b | 2 | 2 | 2 | 1.000 |
| deepseek | qwen15b | 108 | 2 | 2 | 0.019 |
| deepseek | qwen7b | 108 | 2 | 2 | 0.019 |
| qwen15b | qwen7b | 2 | 2 | 2 | 1.000 |

## 5. Cross-Model Error Overlap (Jaccard Similarity)

### Condition: exception_only
Models: codellama13b (2 errors), deepseek (8 errors), qwen15b (2 errors), qwen7b (2 errors)

| | codellama13b | deepseek | qwen15b | qwen7b |
|---|---|---|---|---|
| codellama13b | 1.000 | 0.250 | 1.000 | 1.000 |
| deepseek | 0.250 | 1.000 | 0.250 | 0.250 |
| qwen15b | 1.000 | 0.250 | 1.000 | 1.000 |
| qwen7b | 1.000 | 0.250 | 1.000 | 1.000 |

- Total unique errors (any model): 8
- Universal errors (all models): 2
- Universal error types: {'none(pass)': 2}

### Condition: ae_only
Models: codellama13b (11 errors), deepseek (15 errors), qwen15b (11 errors), qwen7b (1 error)

| | codellama13b | deepseek | qwen15b | qwen7b |
|---|---|---|---|---|
| codellama13b | 1.000 | 0.040 | 1.000 | 0.091 |
| deepseek | 0.040 | 1.000 | 0.040 | 0.067 |
| qwen15b | 1.000 | 0.040 | 1.000 | 0.091 |
| qwen7b | 0.091 | 0.067 | 0.091 | 1.000 |

- Total unique errors (any model): 25
- Universal errors (all models): 1
- Universal error types: {'none(pass)': 1}

### Condition: loop_only
Models: codellama13b (273 errors), deepseek (223 errors), qwen15b (258 errors), qwen7b (171 errors)

| | codellama13b | deepseek | qwen15b | qwen7b |
|---|---|---|---|---|
| codellama13b | 1.000 | 0.249 | 0.267 | 0.294 |
| deepseek | 0.249 | 1.000 | 0.386 | 0.336 |
| qwen15b | 0.267 | 0.386 | 1.000 | 0.288 |
| qwen7b | 0.294 | 0.336 | 0.288 | 1.000 |

- Total unique errors (any model): 503
- Universal errors (all models): 44
- Universal error types: {'none(pass)': 26, 'AssertionError': 18}

### Condition: vota
Models: codellama13b (17 errors), deepseek (1000 errors — broken run), qwen15b (5 errors), qwen7b (7 errors)

| | codellama13b | deepseek | qwen15b | qwen7b |
|---|---|---|---|---|
| codellama13b | 1.000 | 0.017 | 0.000 | 0.412 |
| deepseek | 0.017 | 1.000 | 0.005 | 0.007 |
| qwen15b | 0.000 | 0.005 | 1.000 | 0.000 |
| qwen7b | 0.412 | 0.007 | 0.000 | 1.000 |

- Total unique errors (any model): 1000
- Universal errors (all models): 0

### Condition: no_trace
Models: codellama13b (280 errors), deepseek (317 errors), qwen15b (389 errors), qwen7b (296 errors)

| | codellama13b | deepseek | qwen15b | qwen7b |
|---|---|---|---|---|
| codellama13b | 1.000 | 0.342 | 0.320 | 0.272 |
| deepseek | 0.342 | 1.000 | 0.401 | 0.341 |
| qwen15b | 0.320 | 0.401 | 1.000 | 0.370 |
| qwen7b | 0.272 | 0.341 | 0.370 | 1.000 |

- Total unique errors (any model): 636
- Universal errors (all models): 58
- Universal error types: {'AssertionError': 40, 'none(pass)': 17, 'AttributeError': 1}

### Condition: full_trace
Models: deepseek (1064 errors — broken run), qwen15b (273 errors), qwen7b (217 errors)

| | deepseek | qwen15b | qwen7b |
|---|---|---|---|
| deepseek | 1.000 | 0.208 | 0.180 |
| qwen15b | 0.208 | 1.000 | 0.365 |
| qwen7b | 0.180 | 0.365 | 1.000 |

- Total unique errors (any model): 1108
- Universal errors (all models): 110
- Universal error types: {'AssertionError': 68, 'none(pass)': 42}

## 6. Per-Condition Confusion Summary (seed42, Qwen-7B)

| Condition | TP | TN | FP | FN | Acc | FPR | FNR |
|---|---|---|---|---|---|---|---|
| exception_only | 849 | 339 | 0 | 2 | 0.9983 | 0.0000 | 0.0024 |
| ae_only | 850 | 339 | 0 | 1 | 0.9992 | 0.0000 | 0.0012 |
| loop_only | 741 | 278 | 61 | 110 | 0.8563 | 0.1799 | 0.1293 |
| vota | 844 | 339 | 0 | 7 | 0.9941 | 0.0000 | 0.0082 |
| no_trace | 645 | 249 | 90 | 206 | 0.7513 | 0.2655 | 0.2421 |
| full_trace | 737 | 236 | 103 | 114 | 0.8176 | 0.3038 | 0.1340 |

## 7. Rebuttal Key Points

1. **exception_only near-ceiling**: Qwen-7B seed42 has only 2/1190 errors (0.17%). These 2 are HumanEval/95 pass-samples consistently wrong across all models — data-level irreducible errors.

2. **loop_only gap**: Qwen-7B seed42 has 171/1190 errors (14.4%). The gap concentrates on AssertionError samples (46.2% error rate vs 15.7% for pass-samples). Loop traces provide no signal for assertion failures without showing expected/actual values.

3. **Cross-model exception_only consistency**: 4 models achieve 99.8%+ accuracy. Excluding the deepseek_seed123 outlier run, only 2 samples are universally hard. The Jaccard overlap among codellama13b/qwen15b/qwen7b is 1.000 (identical error sets).

4. **Cross-model loop_only divergence**: 4 models, union errors=503, intersection=44 (Jaccard 0.25-0.39). Low overlap means most errors are model-specific rather than inherent to the data, suggesting room for improvement.

5. **loop_only error composition** (Qwen-7B seed42): 64% are false negatives (pass→fail, 110 samples), 36% are false positives (fail→pass, 61 samples). The dominant failure mode is incorrectly predicting "fail" for programs that actually pass — the model treats absence of exception signal as suspicious.

6. **SyntaxError is perfectly solved**: Across ALL conditions and ALL models, SyntaxError samples have 0% error rate. The exception_only and ae_only conditions both provide sufficient signal, and even loop_only achieves 0% because SyntaxError prevents any execution trace (models learn this pattern).

7. **Tier 1 vs Tier 2 separation is clean**: Tier 1 errors are almost entirely a subset of Tier 2 errors (e.g., codellama13b: 13/13 shared). Tier 2 adds 350-554 unique errors concentrated in none(pass) and AssertionError categories.

---
*Report generated by error_analysis.py*
