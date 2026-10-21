# Paper Data Tables

> All metrics sourced from experiment registry (2026-05-15). N=1190 test samples per condition. Majority baseline accuracy = 0.7151.

---

## Table 1: Main Results — Qwen-2.5-Coder-7B (seed=42)

| Condition | Accuracy | 95% CI | Pass F1 | Fail F1 | ECE ↓ | Brier ↓ | Lift vs no_trace |
|---|---|---|---|---|---|---|---|
| no_trace | 0.7513 | [0.7277, 0.7748] | 0.8134 | 0.6272 | 0.1715 | 0.1972 | — |
| full_trace | 0.8176 | [0.7970, 0.8390] | 0.8717 | 0.6851 | 0.0958 | 0.1439 | +0.0664 |
| label_only | 0.8622 | [0.8437, 0.8807] | 0.9063 | 0.7397 | 0.1107 | 0.1201 | +0.1109 |
| loop_only | 0.8563 | [0.8353, 0.8756] | 0.8966 | 0.7648 | 0.0831 | 0.1183 | +0.1050 |
| ae_only | 0.9992 | [0.9975, 1.0000] | — | — | 0.0004 | 0.0008 | +0.2479 |
| exception_only | 0.9983 | [0.9958, 1.0000] | 0.999 | 0.997 | 0.0027 | 0.0013 | +0.2471 |
| VOTA_no_ae | 0.994 | [0.989, 0.998] | 0.996 | 0.989 | — | — | +0.243 |
| VOTA | 0.9941 | [0.9882, 0.9983] | 0.9941 | 0.9855 | 0.0054 | 0.0052 | +0.2428 |

**Registry sources:**
- no_trace → `no_trace_seed42_v5`
- full_trace → `full_trace_seed42_v5`
- label_only → `full_trace_label_only_seed42`
- loop_only → `vota_loop_only_seed42`
- ae_only → `vota_ae_only_seed42`
- exception_only → `vota_exception_only_seed42_v2`
- VOTA_no_ae → `vota_no_ae_seed42`
- VOTA → `vota_seed42_v5`
- ECE/Brier → `calibration_analysis_seed42`

**Notes:**
- ae_only Pass/Fail F1 not recorded in registry (1 error in 1190 samples)
- VOTA_no_ae not included in calibration analysis; ECE/Brier unavailable
- Lift values from paired bootstrap (N=10,000) where available

---

## Table 2: Cross-Model Comparison — DeepSeek-Coder-6.7B

| Condition | Qwen Accuracy | DeepSeek Accuracy | Cross-model Gap |
|---|---|---|---|
| no_trace | 0.7513 | 0.7336 | +0.0177 |
| full_trace | 0.8176 | *pending (v3)* | — |
| VOTA | 0.9941 | 0.8445 | +0.1496 |
| exception_only (epoch 1) | 0.9983 | 0.9983 | 0.0000 |
| exception_only (epoch 3) | 0.9983 | 0.9933 | +0.0050 |

**Registry sources:**
- Qwen: `no_trace_seed42_v5`, `full_trace_seed42_v5`, `vota_seed42_v5`, `vota_exception_only_seed42_v2`
- DeepSeek: `deepseek_no_trace_seed42`, `deepseek_vota_seed42`, `deepseek_exception_only_seed42`

**Notes:**
- DeepSeek full_trace v1 failed (label truncation during training, accuracy 10.59%); v2 killed for GPU reallocation; v3 pending
- DeepSeek exception_only epoch 1 checkpoint eval: accuracy=0.9983, identical to Qwen — zero cross-model gap at early stopping
- DeepSeek exception_only epoch 3 (final): accuracy=0.9933, slight overfitting degradation (−0.50pp)
- Qwen exception_only: no epoch-level breakdown in registry; 0.9983 is final (epoch 3) accuracy
- DeepSeek VOTA: accuracy 0.8445, CI [0.826, 0.864]; fail_recall=0.454 (vs Qwen fail_recall=1.0)
- DeepSeek no_trace: accuracy 0.7336, CI [0.708, 0.757]; lift +1.85pp not statistically significant (CI crosses 0)

---

## Table 3: Seed Robustness — Qwen exception_only (3 seeds)

| Seed | Accuracy | 95% CI | Errors | Error Sample IDs |
|---|---|---|---|---|
| 42 | 0.9983 | [0.9958, 1.0000] | 2/1190 | see predictions.jsonl |
| 123 | 0.9983 | [0.9958, 1.0000] | 2/1190 | see predictions.jsonl |
| 456 | 0.9983 | [0.9958, 1.0000] | 2/1190 | see predictions.jsonl |

**Registry sources:** `vota_exception_only_seed42_v2`, `exception_only_seed123`, `exception_only_seed456`

**Notes:**
- Identical accuracy to 4 decimal places across all 3 seeds (max_diff = 0)
- Each seed has exactly 2/1190 errors — high probability same irreducible samples
- Error sample IDs available in predictions.jsonl on server, not recorded in registry
- train_loss: seed42 N/A (not in v2 metrics), seed123 0.1096, seed456 0.1087

---

## Table 4: DeepSeek exception_only Seed Comparison (provisional)

| Seed | Epoch 1 Acc | Epoch 3 Acc | Δ | fail_recall |
|---|---|---|---|---|
| 42 | 0.9983 | 0.9933 | −0.0050 | 1.000 |
| 123 | — | 0.9109 | — | 0.705 |
| 456 | *pending* | *pending* | — | — |

**Registry sources:** `deepseek_exception_only_seed42`, `deepseek_exception_only_seed123`

**Notes:**
- Seed 42 epoch 1 outperforms epoch 3 by 0.50pp (eval_loss 0.413→0.476, continued training overfits)
- Seed 123: accuracy 91.09%, CI [0.894, 0.926], train_loss=0.122 (high vs seed42)
- Seed 123 fail_recall=0.705 vs seed42 fail_recall=1.000 — DeepSeek exception_only NOT seed-robust
- Seed 123 no epoch-level checkpoint eval in registry
- Seed 456 not yet submitted

---

## Table 5: Calibration Summary

| Condition | ECE ↓ | MCE | Brier ↓ |
|---|---|---|---|
| no_trace | 0.1715 | 0.4756 | 0.1972 |
| full_trace | 0.0958 | 0.2491 | 0.1439 |
| label_only | 0.1107 | 0.4171 | 0.1201 |
| loop_only | 0.0831 | 0.1834 | 0.1183 |
| ae_only | 0.0004 | 0.0004 | 0.0008 |
| exception_only | 0.0027 | 0.8355 | 0.0013 |
| VOTA | 0.0054 | 0.6225 | 0.0052 |

**Registry source:** `calibration_analysis_seed42`

**Notes:**
- ae_only achieves near-perfect calibration across all metrics (ECE=0.0004, Brier=0.0008)
- exception_only: lowest Brier (0.0013) but highest MCE (0.8355) — errors concentrated in one confidence bin
- VOTA: moderate MCE (0.6225) despite low ECE, similar concentration pattern
- loop_only: best MCE (0.1834) among mid-tier conditions, well-spread calibration
- VOTA_no_ae not included in calibration analysis
