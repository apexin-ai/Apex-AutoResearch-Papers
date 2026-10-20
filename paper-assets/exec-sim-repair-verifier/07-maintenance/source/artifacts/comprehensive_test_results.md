# Comprehensive Test Results — exec-sim-repair-verifier

> Compiled: 2026-05-15 | Majority baseline (repo-level): **72.96%** | Majority baseline (function-level): **51.75%**

---

## 1. Repo-Level CLS Test Curves

All repo-level evals use full test set (n=9,784).

### CLS 8B seed123 (test@8192)

| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |
|-----------|-------------|----------|---------|---------|------|
| ckpt-200  | 72.55       | 70.18    | 61.78   | 78.58   | Near majority baseline |
| **ckpt-3000** | **85.60** | **78.38** | **65.89** | **90.87** | **Val-best (val=88.69%) & Test peak** |
| ckpt-6200 | 84.70       | 77.01    | 63.71   | 90.31   | |
| ckpt-6400 | 85.08       | 77.91    | 65.32   | 90.49   | |
| ckpt-6600 | 84.90       | 77.58    | 64.80   | 90.40   | |
| ckpt-6633 | 84.89       | 77.56    | 64.70   | 90.40   | Final checkpoint |

- **Val-selected test accuracy: 85.60%** (ckpt-3000, val=88.69%)
- Test peak: 85.60% (ckpt-3000) — val-selected = test-peak
- Gap vs majority: +12.64pp

### CLS 8B s42 (test@8192)

| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |
|-----------|-------------|----------|---------|---------|------|
| ckpt-200  | 70.07       | 68.18    | 60.40   | 75.90   | Below majority baseline |
| ckpt-400  | 84.79       | 81.18    | 72.93   | 89.43   | |
| ckpt-600  | 79.05       | 75.12    | 65.24   | 85.00   | |
| ckpt-800  | 83.53       | 78.97    | 69.17   | 88.77   | |
| ckpt-1000 | 83.52       | 77.50    | 65.85   | 89.14   | Val-best (val=88.23%) |
| ckpt-1200 | 83.84       | 77.47    | 65.49   | 89.45   | |
| **ckpt-1400** | **85.47** | **78.90** | **67.13** | **90.67** | **Test peak** |
| ckpt-1600 | 84.99       | 78.94    | 67.65   | 90.22   | |

- **Val-selected test accuracy: 83.52%** (ckpt-1000, val=88.23%)
- Test peak: 85.47% (ckpt-1400)
- Gap vs majority: +12.51pp (peak), +10.56pp (val-selected)

### CLS 4B s42 (test@5120)

| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |
|-----------|-------------|----------|---------|---------|------|
| ckpt-600  | 77.74       | 74.74    | 66.03   | 83.44   | |
| ckpt-4000 | —           | —        | —       | —       | Failed (script error) |
| ckpt-4400 | 83.24       | 74.44    | 59.45   | 89.44   | |
| **ckpt-4600** | **83.63** | **75.63** | **61.67** | **89.59** | **Val-best (val=90.07%) & Test peak** |

- **Val-selected test accuracy: 83.63%** (ckpt-4600, val=90.07%)
- Gap vs majority: +10.67pp

### CLS 4B seed123 (test@5120)

| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |
|-----------|-------------|----------|---------|---------|------|
| ckpt-800  | 75.33       | 67.03    | 50.50   | 83.60   | Val-best (val=87.92%), weak test |

- **Val-selected test accuracy: 75.33%** (ckpt-800, val=87.92%)
- Gap vs majority: +2.37pp — marginal

---

## 2. Repo-Level CWM Test Results

### CWM 4B repo-level (test@full, n=9,784)

| Variant | Test Acc (%) | F1_macro | F1_fail | F1_pass | Unparseable |
|---------|-------------|----------|---------|---------|-------------|
| s42 (v12) | 58.04     | 51.67    | 34.12   | 69.22   | 53.7% |
| seed123   | 59.09     | 43.43    | 13.67   | 73.19   | 67.2% |

- Both **below majority baseline** (72.96%) — CWM fails catastrophically at repo-level
- Massive unparseable rates (54-67%) confirm generation struggles with long repo contexts

### CWM 8B repo-level

- Training in progress (repo-level-cwm-8b-conda-v4, step ~1700/6633)
- ckpt-400 test eval running (cwm8b-ckpt400-test-eval)

---

## 3. Function-Level Results (n=1,890)

### CLS 8B function-level

| Seed | Accuracy (%) | F1_pass | F1_fail |
|------|-------------|---------|---------|
| s42  | 90.48       | 90.86   | 90.06   |
| seed123 | 89.37    | 89.54   | 89.19   |
| **Mean** | **89.93** | **90.20** | **89.63** |

### CWM 4B function-level (5-seed)

| Seed | Accuracy (%) | F1_pass | F1_fail |
|------|-------------|---------|---------|
| s42 (baseline) | 87.51 | 87.31 | 87.71 |
| seed123 | 87.20 | 86.95 | 87.44 |
| seed456 | 86.98 | 86.66 | 87.29 |
| seed789 | 86.67 | 86.74 | 86.60 |
| seed0   | 87.57 | 87.18 | 87.93 |
| **Mean** | **87.19** | **86.97** | **87.39** |

### CWM 8B function-level (3-seed)

| Seed | Accuracy (%) | F1_pass | F1_fail |
|------|-------------|---------|---------|
| s42  | 87.67       | 87.57   | 87.77   |
| seed123 | 86.98    | 86.83   | 87.13   |
| seed456 | 86.24    | 85.96   | 86.51   |
| **Mean** | **86.96** | **86.79** | **87.14** |

---

## 4. Main Results Summary

### Repo-Level Test (Val-Selected Checkpoints)

| Model | Size | Seed | Val-Best Ckpt | Val Acc (%) | Test Acc (%) | Gap vs Majority |
|-------|------|------|---------------|-------------|-------------|-----------------|
| CLS   | 8B   | seed123 | ckpt-3000 | 88.69 | **85.60** | +12.64pp |
| CLS   | 8B   | s42     | ckpt-1000 | 88.23 | **83.52** | +10.56pp |
| CLS   | 4B   | s42     | ckpt-4600 | 90.07 | **83.63** | +10.67pp |
| CLS   | 4B   | seed123 | ckpt-800  | 87.92 | **75.33** | +2.37pp  |
| CWM   | 4B   | s42     | ckpt-500  | —     | **58.04** | −14.92pp |
| CWM   | 4B   | seed123 | ckpt-500  | —     | **59.09** | −13.87pp |

### Repo-Level Test Peak (Oracle Selection)

| Model | Size | Seed | Peak Ckpt | Test Acc (%) |
|-------|------|------|-----------|-------------|
| CLS   | 8B   | seed123 | ckpt-3000 | **85.60** |
| CLS   | 8B   | s42     | ckpt-1400 | **85.47** |
| CLS   | 4B   | s42     | ckpt-4600 | **83.63** |

### Function-Level Summary

| Model | Size | Seeds | Mean Acc (%) | Std |
|-------|------|-------|-------------|-----|
| CLS   | 8B   | 2     | 89.93       | 0.78 |
| CWM   | 4B   | 5     | 87.19       | 0.35 |
| CWM   | 8B   | 3     | 86.96       | 0.72 |

---

## 5. Ablation Results

### CWM LoRA Rank Ablation (4B, function-level, n=1,890)

| Rank | Alpha | Accuracy (%) | vs Baseline (rank=16) |
|------|-------|-------------|----------------------|
| 16 (baseline) | 32 | 87.51 | — |
| 32 | 32 | 87.00 | −0.51pp |
| 64 | 128 | — | Training allocated |

### Sequence Length Ablation (CLS 8B s42, ckpt-1000, repo-level test)

| max_seq_length | Test Acc (%) | Unparseable |
|---------------|-------------|-------------|
| 8192          | 83.52       | 0 |
| 2048          | 82.83       | 136 |
| **Delta**     | **−0.69pp** | |

CLS@2048 (82.83%) still vastly outperforms CWM@2048 (58.04%), ruling out seq_length as a confound.

---

## 6. Key Takeaways

1. **CLS >> CWM at repo-level**: CLS achieves 83-86% vs CWM 58-59% — a **25+pp gap** that validates the classification reformulation for complex (repo-level) inputs
2. **CLS scales with model size**: 8B peak (85.60%) > 4B peak (83.63%) at repo-level (+1.97pp)
3. **CWM does NOT scale at function-level**: 8B CWM (86.96%) ≈ 4B CWM (87.19%) — no benefit from 2x parameters
4. **Val-selected vs test-peak gap**: seed123 shows 0pp gap (val-best = test-best), s42 shows 1.95pp gap (ckpt-1000 vs ckpt-1400)
5. **Seq_length is not a confound**: CLS@2048 still beats CWM by 24.79pp
6. **LoRA rank does not help CWM**: rank=32 marginally worse than rank=16 (−0.51pp)
