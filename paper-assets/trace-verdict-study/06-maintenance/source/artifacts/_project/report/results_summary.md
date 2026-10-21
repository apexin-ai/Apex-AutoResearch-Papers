# Cross-Model / Cross-Scale Experiment Results Summary

Generated: 2026-05-16

---

## Table A: Main Results (per Model x Condition)

All accuracy values on test set (n=1190 unless noted). CI = 95% Wilson confidence interval.

### Qwen-2.5-Coder-7B (primary model)

| Condition | Accuracy | CI 95% | exp_id |
|-----------|----------|--------|--------|
| no_trace | 0.7513 | [0.728, 0.775] | no_trace_seed42_v5 |
| full_trace | 0.8176 | [0.797, 0.839] | full_trace_seed42_v5 |
| label_only | 0.8622 | [0.844, 0.881] | full_trace_label_only_seed42 |
| loop_only | 0.8563 | [0.835, 0.876] | vota_loop_only_seed42 |
| VOTA | 0.9941 | [0.988, 0.998] | vota_seed42_v5 |
| ae_only | 0.9992 | [0.998, 1.000] | vota_ae_only_seed42 |
| exception_only | 0.9983 | [0.996, 1.000] | vota_exception_only_seed42_v2 |

### Qwen-2.5-Coder-1.5B

| Condition | Accuracy | CI 95% | exp_id |
|-----------|----------|--------|--------|
| no_trace | 0.6731 | — | qwen15b_no_trace_seed42 |
| full_trace | 0.7706 | — | qwen15b_full_trace_seed42 |
| VOTA | 0.9958 | — | qwen15b_vota_seed42 |
| exception_only | 0.9983 | [0.996, 1.000] | qwen15b_exception_only_seed42 |

### DeepSeek-Coder-6.7B

| Condition | Accuracy | CI 95% | exp_id |
|-----------|----------|--------|--------|
| no_trace | 0.7336 | [0.708, 0.757] | deepseek_no_trace_seed42 |
| full_trace | 0.7916 | [0.768, 0.813] | deepseek_full_trace_seed42_v3 |
| VOTA | 0.8445* | [0.826, 0.864] | deepseek_vota_seed42 |
| exception_only | 0.9933 | [0.988, 0.998] | deepseek_exception_only_seed42 |

*VOTA re-eval with fixed script showed 16% — discrepancy under investigation. The 84.45% value is from max_length=2048 eval; group analysis shows 100% accuracy on non-truncated training samples, 31.2% fail_recall on truncated samples.

### CodeLlama-13B-Instruct

| Condition | Accuracy | CI 95% | exp_id |
|-----------|----------|--------|--------|
| no_trace | 0.7650 | [0.738, 0.787] | codellama13b_no_trace_seed42 |
| exception_only | RUNNING | — | codellama13b_exception_only_seed42 |
| VOTA | RUNNING | — | codellama13b_vota_seed42 |

---

## Table B: Seed Robustness Summary

### Qwen-2.5-Coder-7B

| Condition | seed42 | seed123 | seed456 | Mean | σ | exp_ids |
|-----------|--------|---------|---------|------|---|---------|
| exception_only | 0.9983 | 0.9983 | 0.9983 | 0.9983 | 0.0000 | vota_exception_only_seed42_v2, exception_only_seed123, exception_only_seed456 |
| ae_only | 0.9992 | 0.9908 | 0.9992 | 0.9964 | 0.0049 | vota_ae_only_seed42, ae_only_seed123, ae_only_seed456 |
| VOTA | 0.9941 | — | 0.9908 | 0.9925 | 0.0023 | vota_seed42_v5, vota_seed456_v2 (seed123 failed) |
| loop_only | 0.8563 | 0.8588 | 0.8664 | 0.8605 | 0.0053 | vota_loop_only_seed42, loop_only_seed123, loop_only_seed456 |
| label_only | 0.8622 | 0.8706 | 0.8590 | 0.8639 | 0.0060 | full_trace_label_only_seed42, label_only_seed123, label_only_seed456 |

### DeepSeek-Coder-6.7B

| Condition | seed42 | seed123 | seed456 | Mean | σ | exp_ids |
|-----------|--------|---------|---------|------|---|---------|
| exception_only | 0.9933 | 0.9109 | 0.9933 | 0.9658 | 0.0476 | deepseek_exception_only_seed42, deepseek_exception_only_seed123, deepseek_exception_only_seed456 |

Note: DeepSeek seed123 is an outlier (91.09% vs 99.33% for seed42/456). 2/3 seeds robust.

---

## Table C: Cross-Task Generalization (DebugBench)

DefectDetection task, n=426, majority_baseline=0.5141.

| Condition | Accuracy | CI 95% | Lift vs majority | exp_id |
|-----------|----------|--------|------------------|--------|
| no_trace | 0.9671 | [0.948, 0.984] | +0.4531 | debugbench_no_trace_seed42 |
| VOTA | 0.9977 | [0.993, 1.000] | +0.4836 | debugbench_vota_seed42 |
| exception_only | 1.0000 | [0.991, 1.000] | +0.4859 | debugbench_exception_only_seed42 |

---

## Table D: Regex Baselines (Qwen-7B test set, n=1190)

| Baseline | Rule | Accuracy | exp_id |
|----------|------|----------|--------|
| B1 | ERROR keyword presence | 0.9345 | regex_baseline_analysis |
| B2 | Traceback presence | 0.7151 | regex_baseline_analysis |
| B3 | Any error keyword | 0.9345 | regex_baseline_analysis |
| B4 | Exception type extraction | 0.9361 | regex_baseline_analysis |
| B5 | Format marker | 0.9933 | regex_baseline_analysis |
| B6 | Error count >= 2 | 0.9202 | regex_baseline_analysis |
| SFT exception_only | — | 0.9983 | vota_exception_only_seed42_v2 |

Best regex (B5) vs SFT gap: -0.0050 (McNemar p=0.041, significant).

---

## Table E: Full Trace Length Ablation (Qwen-7B, seed42)

| Max tokens | Accuracy | CI 95% | exp_id |
|------------|----------|--------|--------|
| 256 | 0.7882 | [0.764, 0.810] | full_trace_256tok_seed42 |
| 512 | 0.8042 | [0.782, 0.826] | full_trace_512tok_seed42 |
| 1024 | 0.7723 | [0.749, 0.796] | full_trace_1024tok_seed42 |
| full (2048) | 0.8176 | [0.797, 0.839] | full_trace_seed42_v5 |

Non-monotonic: 512 > 1024 (information loss from mid-truncation). Best at full length but only +1.3pp over 512.

---

## Table F: Calibration (Qwen-7B, seed42)

| Condition | ECE | MCE | Brier Score | exp_id |
|-----------|-----|-----|-------------|--------|
| no_trace | 0.1715 | 0.4756 | 0.1972 | calibration_analysis_seed42 |
| full_trace | 0.0958 | 0.2491 | 0.1439 | calibration_analysis_seed42 |
| label_only | 0.1107 | 0.4171 | 0.1201 | calibration_analysis_seed42 |
| loop_only | 0.0831 | 0.1834 | 0.1183 | calibration_analysis_seed42 |
| ae_only | 0.0004 | 0.0004 | 0.0008 | calibration_analysis_seed42 |
| exception_only | 0.0027 | 0.8355 | 0.0013 | calibration_analysis_seed42 |
| VOTA | 0.0054 | 0.6225 | 0.0052 | calibration_analysis_seed42 |

---

## Key Comparisons

### 1. exception_only vs no_trace lift (per model)

| Model | no_trace | exception_only | Δ (abs) | Δ (rel%) |
|-------|----------|----------------|---------|----------|
| Qwen-7B | 0.7513 | 0.9983 | +0.2470 | +32.9% |
| Qwen-1.5B | 0.6731 | 0.9983 | +0.3252 | +48.3% |
| DeepSeek-6.7B | 0.7336 | 0.9933 | +0.2597 | +35.4% |
| CodeLlama-13B | 0.7650 | RUNNING | — | — |

Consistent +24.7 to +32.5pp lift across all completed models.

### 2. exception_only vs VOTA (per model)

| Model | VOTA | exception_only | Δ | Note |
|-------|------|----------------|---|------|
| Qwen-7B | 0.9941 | 0.9983 | +0.0042 | p=0.01 (vota_exception_only_seed42_v2) |
| Qwen-1.5B | 0.9958 | 0.9983 | +0.0025 | — |
| DeepSeek-6.7B | 0.8445* | 0.9933 | +0.1488 | VOTA compromised by truncation |

exception_only >= VOTA in all models. On Qwen-7B the difference is small but statistically significant.

### 3. Scale comparison: 1.5B vs 7B

| Condition | 1.5B | 7B | Δ (7B - 1.5B) |
|-----------|------|----|----|
| no_trace | 0.6731 | 0.7513 | +0.0782 |
| full_trace | 0.7706 | 0.8176 | +0.0470 |
| VOTA | 0.9958 | 0.9941 | -0.0017 |
| exception_only | 0.9983 | 0.9983 | 0.0000 |

Pattern: scale matters for weak signals (no_trace, full_trace) but is irrelevant for strong signals (exception_only, VOTA). The 1.5B model matches or exceeds 7B when given structured trace information.

### 4. Signal-Rich vs Signal-Poor Grouping (Qwen-7B)

**Signal-rich** (contains exception/assertion error info):
- ae_only: 0.9992
- exception_only: 0.9983
- VOTA: 0.9941
- Mean: **0.9972**

**Signal-poor** (structural/positional info only):
- label_only: 0.8622
- loop_only: 0.8563
- full_trace (raw): 0.8176
- no_trace: 0.7513
- Mean: **0.8219**

Gap: **+0.1753** (signal-rich vs signal-poor).

The assertion/exception content is the critical signal. Structural trace elements (loop counts, labels, raw output) provide moderate improvement over no_trace but plateau around 85-86%.

### 5. Ablation Component Hierarchy (Qwen-7B, seed42)

```
ae_only      0.9992  ████████████████████████████████████████  (+24.8pp vs no_trace)
except_only  0.9983  ████████████████████████████████████████  (+24.7pp)
VOTA         0.9941  ███████████████████████████████████████   (+24.3pp)
vota_no_ae   0.9940  ███████████████████████████████████████   (+24.3pp)
label_only   0.8622  ██████████████████████████████████        (+11.1pp)
loop_only    0.8563  █████████████████████████████████         (+10.5pp)
full_trace   0.8176  ██████████████████████████████            (+6.6pp)
no_trace     0.7513  █████████████████████████████             (baseline)
majority     0.7151  ████████████████████████████              (chance)
```

---

## Experiment Status Summary

| Status | Count | Notes |
|--------|-------|-------|
| DONE (usable) | 35+ | Core experiments with valid metrics |
| RUNNING | 2 | codellama13b_exception_only_seed42, codellama13b_vota_seed42 |
| QUEUED/killed | ~12 | Superseded by v2-v5 reruns or killed early |
| Failed | 3 | vota_seed123, vota_seed456, vota_exception_only_seed42 |

---

## Notes

1. **Qwen-7B canonical versions**: v5 for no_trace/full_trace/VOTA (unified eval pipeline). Earlier versions (v1-v4) had eval bugs or were killed.
2. **DeepSeek VOTA caveat**: The 84.45% accuracy may be inflated — re-eval with corrected script showed 16%. The group analysis confirms the model fails on truncated training samples. Use with asterisk.
3. **DeepSeek full_trace reeval**: Resolved — 28.5% re-eval was caused by eval max_length=16384 (OOD). Re-eval with max_length=2048 reproduces 79.16%.
4. **CodeLlama-13B**: Only no_trace complete (76.5%). exception_only and VOTA still running.
5. **DebugBench**: All three conditions near-ceiling (96.7%–100%), suggesting the DefectDetection task is easier than the main CodeNet verdict task.
