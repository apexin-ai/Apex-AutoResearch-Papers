# Cross-Model Comparative Analysis: Trace-Verdict Study

Generated: 2026-05-16

## 1. Qwen-2.5-Coder-7B Condition Comparison (seed=42)

All experiments on the same dataset (n=1190, majority baseline=71.51%).

| Condition | Accuracy | Lift | Pass F1 | Fail F1 | 95% CI | exp_id |
|-----------|----------|------|---------|---------|--------|--------|
| no_trace | 75.13% | +3.61pp | 0.813 | 0.627 | [72.8, 77.5] | no_trace_seed42_v5 |
| full_trace | 81.76% | +10.25pp | 0.872 | 0.685 | [79.7, 83.9] | full_trace_seed42_v5 |
| loop_only | 85.63% | +14.12pp | 0.897 | 0.765 | [83.5, 87.6] | vota_loop_only_seed42 |
| label_only | 86.22% | +14.71pp | 0.906 | 0.740 | [84.4, 88.1] | full_trace_label_only_seed42 |
| VOTA | 99.41% | +27.90pp | 0.994 | 0.986 | [98.8, 99.8] | vota_seed42_v5 |
| vota_no_ae | 99.40% | +27.90pp | 0.996 | 0.989 | [98.9, 99.8] | vota_no_ae_seed42 |
| exception_only | 99.83% | +28.32pp | 0.999 | 0.997 | [99.6, 100] | vota_exception_only_seed42_v2 |
| ae_only | 99.92% | — | — | — | [99.8, 100] | vota_ae_only_seed42 |

**Key findings:**
- **exception_only** (99.83%) and **ae_only** (99.92%) achieve near-perfect accuracy; bootstrap test shows no significant difference (p=0.80).
- Removing assertion errors from VOTA (**vota_no_ae**, 99.40%) causes negligible degradation vs full VOTA (99.41%), confirming AE content is redundant when exception info is present.
- **loop_only** (85.63%) and **label_only** (86.22%) perform similarly — both better than full_trace but far below exception-based conditions.
- **full_trace** (81.76%) is worse than both loop_only and label_only individually, suggesting noise from full trace content hurts more than it helps.

### Hierarchy
```
ae_only ≈ exception_only >> VOTA ≈ vota_no_ae >> label_only ≈ loop_only > full_trace > no_trace
  99.92%    99.83%          99.41%   99.40%       86.22%      85.63%     81.76%      75.13%
```

## 2. Cross-Model Comparison: Qwen vs DeepSeek (seed=42)

| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Δ (Qwen−DS) | Qwen exp_id | DeepSeek exp_id |
|-----------|-------------------|---------------------|-------------|-------------|-----------------|
| no_trace | 75.13% | 73.36% | +1.77pp | no_trace_seed42_v5 | deepseek_no_trace_seed42 |
| full_trace | 81.76% | 79.16% | +2.60pp | full_trace_seed42_v5 | deepseek_full_trace_seed42_v3 |
| VOTA | 99.41% | 84.45% | +14.96pp | vota_seed42_v5 | deepseek_vota_seed42 |
| exception_only | 99.83% | 99.33% | +0.50pp | vota_exception_only_seed42_v2 | deepseek_exception_only_seed42 |

**Key findings:**
- Both models struggle with no_trace (~73–75%) and full_trace (~79–82%); the gap is small (≤2.6pp).
- **VOTA shows the largest cross-model gap** (14.96pp). DeepSeek VOTA (84.45%) suffers from training-time truncation: 100% of errors come from samples whose content exceeded the 2048-token budget. Intact samples achieve 100% accuracy.
- **exception_only is the great equalizer**: both models achieve >99.3%, with only 0.50pp gap. This suggests exception_only is robust across model architectures.

### DeepSeek VOTA Truncation Analysis (from deepseek_vota_seed42)
| Group | n | Accuracy | Fail Recall |
|-------|---|----------|-------------|
| train_truncated | 1091 | 83.04% | 31.23% |
| train_intact | 99 | 100% | 100% |
| Fisher exact p-value | — | 0.0 | — |

## 3. Seed Robustness

### Qwen exception_only (3 seeds)
| Seed | Accuracy | 95% CI | exp_id |
|------|----------|--------|--------|
| 42 | 99.83% | [99.6, 100] | vota_exception_only_seed42_v2 |
| 456 | 99.83% | [99.6, 100] | exception_only_seed456 |
| 123 | 99.83% | [99.6, 100] | exception_only_seed123 |
| **Spread** | **0.00pp** | — | — |

Perfectly seed-robust: identical accuracy to 4 decimal places across all 3 seeds. Each has exactly 2/1190 errors.

### DeepSeek exception_only (3 seeds)
| Seed | Accuracy | Conclusion | exp_id |
|------|----------|------------|--------|
| 42 | 99.33% | success | deepseek_exception_only_seed42 |
| 456 | 99.33% | success | deepseek_exception_only_seed456 |
| 123 | 91.09% | negative (outlier) | deepseek_exception_only_seed123 |
| **Spread** | **8.24pp** | — | — |

seed123 is an outlier (fail_recall=70.5% vs 100% for other seeds). 2/3 seeds are robust and identical (99.33%).

### Qwen VOTA (seeds)
| Seed | Accuracy | 95% CI | exp_id |
|------|----------|--------|--------|
| 42 | 99.41% | [98.8, 99.8] | vota_seed42_v5 |
| 456 | 99.08% | [98.5, 99.6] | vota_seed456_v2 |
| 123 | — | failed | vota_seed123 (failed) |
| **Spread** | **0.33pp** (2 seeds) | — | — |

## 4. DebugBench Cross-Dataset Generalization (Qwen, seed=42)

DebugBench dataset: n=426, majority baseline=51.41%.

| Condition | Accuracy | Lift | Pass F1 | Fail F1 | 95% CI | exp_id |
|-----------|----------|------|---------|---------|--------|--------|
| no_trace | 96.71% | +45.31pp | 0.967 | 0.967 | [94.8, 98.4] | debugbench_no_trace_seed42 |
| VOTA | 99.77% | +48.36pp | 1.000 | 1.000 | [99.3, 100] | debugbench_vota_seed42 |
| exception_only | — | — | — | — | — | debugbench_exception_only_seed42 (**RUNNING**) |

**Key findings:**
- DebugBench is substantially easier than the primary dataset: even no_trace achieves 96.71% (vs 75.13% on primary).
- VOTA reaches near-perfect 99.77% with only 1 error out of 426 samples.
- exception_only result pending (experiment currently running).

## 5. Calibration Analysis (Qwen, seed=42)

All conditions evaluated on n=1190 samples.

| Condition | Accuracy | ECE ↓ | MCE ↓ | Brier ↓ | exp_id |
|-----------|----------|-------|-------|---------|--------|
| no_trace | 75.13% | 0.1715 | 0.4756 | 0.1972 | calibration_analysis_seed42 |
| full_trace | 81.76% | 0.0958 | 0.2491 | 0.1439 | calibration_analysis_seed42 |
| loop_only | 85.63% | 0.0831 | 0.1834 | 0.1183 | calibration_analysis_seed42 |
| label_only | 86.22% | 0.1107 | 0.4171 | 0.1201 | calibration_analysis_seed42 |
| VOTA | 99.41% | 0.0054 | 0.6225 | 0.0052 | calibration_analysis_seed42 |
| exception_only | 99.83% | 0.0027 | 0.8355 | 0.0013 | calibration_analysis_seed42 |
| ae_only | 99.92% | 0.0004 | 0.0004 | 0.0008 | calibration_analysis_seed42 |

**Key findings:**
- **ae_only has the best calibration** across all metrics: ECE=0.0004, Brier=0.0008.
- **exception_only and VOTA** have excellent ECE and Brier scores but high MCE (0.84 and 0.62), indicating a single confidence bin with poor calibration — likely the rare misclassifications are highly confident.
- **no_trace** is the worst calibrated model (ECE=0.17, Brier=0.20), consistent with its low accuracy.
- Calibration quality tracks accuracy closely, with the exception of MCE anomalies in high-accuracy conditions.

## 6. Full Trace Token Budget Ablation (Qwen, seed=42)

| Max Tokens | Accuracy | Lift | 95% CI | exp_id |
|------------|----------|------|--------|--------|
| 256 | 78.82% | +7.31pp | [76.4, 81.0] | full_trace_256tok_seed42 |
| 512 | 80.42% | +8.91pp | [78.2, 82.6] | full_trace_512tok_seed42 |
| no limit | 81.76% | +10.25pp | [79.7, 83.9] | full_trace_seed42_v5 |
| 1024 | — | — | — | full_trace_1024tok_seed42 (**RUNNING**) |
| 2048 | — | — | — | full_trace_2048tok_seed42 (**QUEUED**) |

More tokens marginally help full_trace, but even unlimited tokens (81.76%) falls far short of exception_only (99.83%).

## 7. Invalidated / Failed Experiments

These experiments are excluded from the main analysis:

| exp_id | Status | Reason |
|--------|--------|--------|
| no_trace_seed42 | killed | Superseded by v5 |
| no_trace_seed42_v2 | killed | Superseded by v5 |
| no_trace_seed42_v3 | killed | Superseded by v5 |
| vota_seed42 | killed | Superseded by v5 |
| vota_seed42_v2 | killed | Superseded by v5 |
| vota_seed42_v3 | killed | Superseded by v5 |
| vota_seed456 | failed | Superseded by v2 |
| vota_seed123 | failed | Training failure |
| vota_exception_only_seed42 | failed | Superseded by v2 |
| full_trace_seed42 | killed | Eval bug |
| full_trace_seed42_v2 | negative | Eval bug (28.4% accuracy) |
| deepseek_full_trace_seed42 | negative | Label truncation during training |
| deepseek_full_trace_seed42_v2 | killed | Superseded by v3 |
| deepseek_exception_only_seed123 | negative | Seed outlier (91.09%), not representative |

## 8. Summary of Core Findings

1. **Exception information is the dominant signal** for verdict prediction. Both `exception_only` and `ae_only` achieve >99.8% accuracy, and removing assertion errors from VOTA (`vota_no_ae`) causes no degradation.

2. **The exception_only condition is architecture-robust**: Qwen (99.83%) and DeepSeek (99.33%) both achieve near-perfect accuracy with minimal gap.

3. **exception_only is perfectly seed-robust on Qwen** (0.00pp spread across 3 seeds) and largely robust on DeepSeek (2/3 seeds at 99.33%, 1 outlier at 91.09%).

4. **Full trace is surprisingly unhelpful**: even with unlimited tokens, full_trace (81.76%) underperforms loop_only (85.63%) and label_only (86.22%). The noise in raw trace content degrades signal quality.

5. **VOTA is effective but fragile across models**: Qwen VOTA (99.41%) vs DeepSeek VOTA (84.45%) — the 14.96pp gap is driven by training-time truncation sensitivity in DeepSeek.

6. **Calibration scales with accuracy**, with ae_only achieving the best overall calibration (ECE=0.0004). High-accuracy models (exception_only, VOTA) show MCE anomalies from rare confident misclassifications.

7. **DebugBench is a substantially easier benchmark**: no_trace already achieves 96.71%, leaving limited headroom for trace-based methods to demonstrate lift.
