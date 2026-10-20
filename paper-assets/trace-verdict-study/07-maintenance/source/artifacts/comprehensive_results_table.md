# Comprehensive Experiment Results — Trace-Verdict Study

> Compiled: 2026-05-16 | All results from registry (status=DONE, conclusion=success)
> Dataset: MBPP+ (n=1190) unless noted | Metric: accuracy % [95% Wilson CI]

---

## Table 1 — Model × Condition (Primary Results)

| Model | no_trace | full_trace | label_only | loop_only | exception_only | ae_only | VOTA |
|:------|:--------:|:----------:|:----------:|:---------:|:--------------:|:-------:|:----:|
| **Qwen-2.5-Coder-7B** | 75.13 [72.77, 77.48] | 81.76 [79.70, 83.90] | 86.22 [84.37, 88.07] | 85.63 [83.53, 87.56] | 99.83 [99.58, 100.00] | 99.92 [99.75, 100.00] | 99.41 [98.82, 99.83] |
| **Qwen-2.5-Coder-1.5B** | 67.31 [64.59, 69.92] | 77.06 [74.59, 79.36] | — | — | 99.83 [99.58, 100.00] | — | 99.58 [99.02, 99.82] |
| **DeepSeek-Coder-6.7B** | — | 79.16 [76.80, 81.30] | — | — | 99.33 [98.68, 99.66] | — | 84.45 [82.60, 86.40] |
| **CodeLlama-13B** | 76.50 [73.80, 78.70] | — | — | — | 99.83 [99.39, 99.95] | — | — |

**Key observations:**
- exception_only achieves ≥99.33% across all 4 models
- VOTA degraded on DeepSeek (84.45%) due to max_length=2048 truncation (verified)
- DeepSeek full_trace also impacted by truncation (79.16%)

---

## Table 2 — Seed Robustness (Qwen-2.5-Coder-7B, MBPP+)

| Condition | seed42 | seed123 | seed456 | Mean ± σ |
|:----------|:------:|:-------:|:-------:|:--------:|
| **exception_only** | 99.83 | 99.83 | 99.83 | 99.83 ± 0.00 |
| **ae_only** | 99.92 | 99.08 | 99.92 | 99.64 ± 0.48 |
| **VOTA** | 99.41 | — | 99.08 | 99.25 ± 0.23 |
| **label_only** | 86.22 | 87.06 | 85.90 | 86.39 ± 0.60 |
| **loop_only** | 85.63 | 85.88 | 86.64 | 86.05 ± 0.53 |

**Key observations:**
- exception_only: perfectly seed-robust (identical 99.83% across 3 seeds, each with exactly 2/1190 errors)
- ae_only: near-perfect; seed123 slightly lower (99.08%) but still >99%
- loop_only and label_only: stable within ~1pp

---

## Table 3 — Cross-Dataset Generalization (DebugBench, n=426)

| Condition | DebugBench Acc | n | MBPP+ Acc | Δ (DB − MBPP+) |
|:----------|:--------------:|:---:|:---------:|:---------------:|
| **no_trace** | 96.71 [94.56, 98.03] | 426 | 75.13 | +21.58 |
| **exception_only** | 100.00 [99.14, 100.00] | 426 | 99.83 | +0.17 |
| **VOTA** | 99.77 [98.69, 99.96] | 426 | 99.41 | +0.36 |

**Key observations:**
- DebugBench has balanced labels (majority baseline 51.41% vs MBPP+ 71.51%), making no_trace much easier
- exception_only and VOTA both transfer perfectly (≥99.77%)

---

## Table 4 — Format Marker Ablation (Nomarker)

| Model | with_markers | without_markers | Δ |
|:------|:------------:|:---------------:|:---:|
| **Qwen-2.5-Coder-7B** | 99.83 | 96.55 [95.50, 97.60] | −3.28 |
| **Qwen-2.5-Coder-1.5B** | 99.83 | 97.80 [97.00, 98.60] | −2.03 |

**Key observations:**
- Removing format markers costs 2–3pp; models still achieve >96% without them
- Smaller model (1.5B) is less affected by marker removal

---

## Table 5 — Regex Baseline Comparison (MBPP+, n=1190)

| Baseline | Accuracy | vs SFT Gap |
|:---------|:--------:|:----------:|
| B1: ERROR keyword presence | 93.45 | −6.38 |
| B2: Traceback presence | 71.51 | −28.32 |
| B3: Any error keyword | 93.45 | −6.38 |
| B4: Exception type match | 93.61 | −6.22 |
| B5: Format marker match | 99.33 | −0.50 |
| B6: Error count ≥ 2 | 92.02 | −7.81 |
| **SFT (exception_only)** | **99.83** | **ref** |

**Key observations:**
- Best regex (B5: format marker) reaches 99.33% — only 0.50pp below SFT
- B5 vs SFT: McNemar p = 0.041 (significant at α=0.05)
- B2 (Traceback presence) equals majority baseline (71.51%), providing no discriminative value

---

## Supplementary: DeepSeek Seed Comparison (exception_only)

| Seed | Accuracy | Note |
|:-----|:--------:|:-----|
| seed42 | 99.33 | |
| seed123 | 91.09 | outlier |
| seed456 | 99.33 | |
| **Mean ± σ** | **96.58 ± 4.76** | 2/3 seeds robust; seed123 anomalous |

---

## Supplementary: Per-Condition Lift vs no_trace (Qwen-7B)

| Condition | Accuracy | Lift vs no_trace | 95% CI of lift |
|:----------|:--------:|:----------------:|:--------------:|
| no_trace | 75.13 | ref | — |
| full_trace | 81.76 | +6.64 | [4.37, 8.99] |
| label_only | 86.22 | +11.09 | [8.49, 13.70] |
| loop_only | 85.63 | +10.50 | [8.24, 12.86] |
| VOTA | 99.41 | +24.28 | [21.85, 26.81] |
| ae_only | 99.92 | +24.79 | [22.35, 27.31] |
| exception_only | 99.83 | +24.71 | [22.27, 27.14] |

---

## Supplementary: Calibration (Qwen-7B, seed42)

| Condition | ECE ↓ | MCE ↓ | Brier ↓ |
|:----------|:-----:|:-----:|:-------:|
| no_trace | 0.1715 | 0.4756 | 0.1972 |
| full_trace | 0.0958 | 0.2491 | 0.1439 |
| label_only | 0.1107 | 0.4171 | 0.1201 |
| loop_only | 0.0831 | 0.1834 | 0.1183 |
| exception_only | 0.0027 | 0.8355 | 0.0013 |
| ae_only | 0.0004 | 0.0004 | 0.0008 |
| VOTA | 0.0054 | 0.6225 | 0.0052 |
