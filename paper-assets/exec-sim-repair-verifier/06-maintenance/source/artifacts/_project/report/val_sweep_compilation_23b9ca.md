# Eval Sweep Compilation — exec-sim-repair-verifier

Generated: 2026-05-15 (updated)

---

## 1. 8B s42 Val@8192 Sweep (n=9335)

| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
|-----------|-------------|-------------|------------|------------|---------------|
| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |
| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |
| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |
| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |
| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |
| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |
| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |
| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |

**Val best = ckpt-1000 (88.23%)** — confirmed.

Majority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).

Notes:
- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑
- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)
- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)
- 72.96% is the test set majority baseline, not val — corrected 2026-05-15

---

## 2. 8B s42 Test@8192 Sweep (n=9784)

| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
|-----------|-------------|-------------|------------|------------|---------------|
| ckpt-200 | 70.07 | 68.18 | 75.90 | 60.40 | cls8b-s42-ckpt200-test8192-eval ⚠️ |
| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |
| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |
| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |
| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |
| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |
| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |
| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |

Majority baseline accuracy = 72.96% (test set, n=9784).

Notes:
- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)
- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)
- Val-test disagreement: val-best ckpt-1000 is not test-best
- ⚠️ ckpt-200: below majority baseline (72.96%), model not yet effective at this point
- ckpt-1600 test = 84.99% — sweep complete (8 val + 8 test checkpoints)

---

## 3. 4B v5 Val@5120 Sweep (n=9335)

| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
|-----------|-------------|-------------|------------|------------|---------------|
| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |
| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |
| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |
| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |
| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |

**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.

4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).

---

## 3b. 4B v5 Test@5120 (n=9784)

| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
|-----------|-------------|-------------|------------|------------|---------------|
| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |
| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |

Majority baseline accuracy = 72.96% (test set, n=9784).

Notes:
- Val-selected ckpt-4600 test = 83.63%
- Val-test gap consistent with 8B pattern

---

## 3c. 4B seed123 Test@5120 (n=9784)

| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
|-----------|-------------|-------------|------------|------------|---------------|
| ckpt-800 (val-best) | 75.33 | 67.03 | 83.60 | 50.50 | cls4b-seed123-ckpt800-test5120-eval-v2 ⚠️ |

Notes:
- Val-best ckpt-800 (val=87.92%) → test=75.33%, val-test gap = 12.59pp
- Only +2.37pp above majority baseline — negative result

---

## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)

| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
|-----------|-------------|-------------|------------|------------|---------------|
| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |
| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |
| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |
| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |
| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |

**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.

### 8B seed123 Test@8192 (n=9784, 6/6 complete)

| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
|-----------|-------------|-------------|------------|------------|---------------|
| ckpt-200 | 72.55 | 70.18 | 78.58 | 61.78 | cls8b-seed123-ckpt200-test-eval ⚠️ |
| **ckpt-3000** | **85.60** | **78.38** | **90.87** | **65.89** | cls8b-seed123-ckpt3000-test8192-eval-v2 |
| ckpt-6200 | 84.70 | 77.01 | 90.31 | 63.71 | cls8b-seed123-ckpt6200-test8192-eval-v2 |
| ckpt-6400 | 85.08 | 77.91 | 90.49 | 65.32 | cls8b-seed123-ckpt6400-test8192-eval-v2 |
| ckpt-6600 | 84.90 | 77.58 | 90.40 | 64.80 | cls8b-seed123-ckpt6600-test-eval |
| ckpt-6633 | 84.89 | 77.56 | 90.40 | 64.70 | cls8b-seed123-ckpt6633-test-eval |

**Test best = ckpt-3000 (85.60% acc, 78.38 f1_macro)** — same as val-best.

Majority baseline accuracy = 72.96% (test set, n=9784).

Notes:
- ⚠️ ckpt-200: 72.55% < majority baseline (72.96%), model not yet effective
- Val-best = ckpt-3000 (88.69%) → test = 85.60% (also test-best), val-test gap = 3.09 pp
- Late checkpoints (6200–6633) cluster tightly: 84.70–85.08% acc, 77.01–77.91 f1_macro
- Unlike s42, val-best and test-best agree (both ckpt-3000)

---

## 5. Summary

| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |
|--------|----------|----------|----------|----------------|
| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |
| 8B s42 test@8192 (8/8) | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |
| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |
| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |
| 4B seed123 test@5120 (val-selected) | ckpt-800 | 75.33 | 67.03 | +2.37 pp ⚠️ |
| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |
| 8B seed123 test@8192 (6/6 complete) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |

---

## 6. JSON (for plotting)

```json
{
  "8b_s42_val8192": {
    "majority_baseline": 75.88,
    "checkpoints": {
      "ckpt-200":  {"accuracy": 63.52, "f1_macro": 61.17, "f1_pass": 70.7,  "f1_fail": 51.6,  "exp_id": "cls8b-s42-ckpt200-val8192-eval-v2"},
      "ckpt-400":  {"accuracy": 80.96, "f1_macro": null,  "f1_pass": null,  "f1_fail": null,  "exp_id": "repo-level-cls-8b-conda"},
      "ckpt-600":  {"accuracy": 85.00, "f1_macro": null,  "f1_pass": null,  "f1_fail": null,  "exp_id": "repo-level-cls-8b-conda"},
      "ckpt-800":  {"accuracy": 84.50, "f1_macro": 79.20, "f1_pass": null,  "f1_fail": null,  "exp_id": "cls8b-s42-ckpt800-val8192-eval"},
      "ckpt-1000": {"accuracy": 88.23, "f1_macro": 82.72, "f1_pass": 92.5,  "f1_fail": 73.0,  "exp_id": "cls8b-s42-ckpt1000-val8192-eval"},
      "ckpt-1200": {"accuracy": 87.76, "f1_macro": 81.25, "f1_pass": 92.3,  "f1_fail": 70.2,  "exp_id": "cls8b-s42-ckpt1200-val8192-v3"},
      "ckpt-1400": {"accuracy": 85.97, "f1_macro": 77.15, "f1_pass": 91.34, "f1_fail": 62.95, "exp_id": "cls8b-s42-ckpt1400-val8192-eval"},
      "ckpt-1600": {"accuracy": 86.75, "f1_macro": 78.94, "f1_pass": 91.76, "f1_fail": 66.12, "exp_id": "cls8b-s42-ckpt1600-val8192-v2"}
    }
  },
  "8b_s42_test8192": {
    "majority_baseline": 72.96,
    "checkpoints": {
      "ckpt-200":  {"accuracy": 70.07, "f1_macro": 68.18, "f1_pass": 75.90, "f1_fail": 60.40, "exp_id": "cls8b-s42-ckpt200-test8192-eval"},
      "ckpt-400":  {"accuracy": 84.79, "f1_macro": 81.18, "f1_pass": 89.43, "f1_fail": 72.93, "exp_id": "cls8b-s42-ckpt400-test8192-eval"},
      "ckpt-600":  {"accuracy": 79.05, "f1_macro": 75.12, "f1_pass": 85.00, "f1_fail": 65.24, "exp_id": "cls8b-s42-ckpt600-test8192-eval"},
      "ckpt-800":  {"accuracy": 83.53, "f1_macro": 78.97, "f1_pass": 88.77, "f1_fail": 69.17, "exp_id": "cls8b-s42-ckpt800-test8192-eval"},
      "ckpt-1000": {"accuracy": 83.52, "f1_macro": 77.50, "f1_pass": 89.14, "f1_fail": 65.85, "exp_id": "cls8b-s42-ckpt1000-test8192-eval"},
      "ckpt-1200": {"accuracy": 83.84, "f1_macro": 77.47, "f1_pass": 89.45, "f1_fail": 65.49, "exp_id": "cls8b-s42-ckpt1200-test8192-eval"},
      "ckpt-1400": {"accuracy": 85.47, "f1_macro": 78.90, "f1_pass": 90.67, "f1_fail": 67.13, "exp_id": "cls8b-s42-ckpt1400-test8192-eval"},
      "ckpt-1600": {"accuracy": 84.99, "f1_macro": 78.94, "f1_pass": 90.22, "f1_fail": 67.65, "exp_id": "cls8b-s42-ckpt1600-test8192-eval"}
    }
  },
  "4b_v5_val5120": {
    "majority_baseline": 75.88,
    "checkpoints": {
      "ckpt-600":  {"accuracy": 82.82, "f1_macro": 79.81, "f1_pass": 87.60, "f1_fail": 72.03, "exp_id": "cls4b-v5-ckpt600-val5120-eval"},
      "ckpt-4000": {"accuracy": 89.84, "f1_macro": 84.25, "f1_pass": 93.64, "f1_fail": 74.85, "exp_id": "cls4b-v5-ckpt4000-val5120-eval"},
      "ckpt-4200": {"accuracy": 89.06, "f1_macro": 83.07, "f1_pass": 93.1,  "f1_fail": 73.0,  "exp_id": "cls4b-v5-val-sweep-ckpt4200"},
      "ckpt-4400": {"accuracy": 89.96, "f1_macro": 84.94, "f1_pass": 93.64, "f1_fail": 76.25, "exp_id": "cls4b-v5-val-sweep-ckpt4400-v3"},
      "ckpt-4600": {"accuracy": 90.07, "f1_macro": 85.04, "f1_pass": 93.71, "f1_fail": 76.37, "exp_id": "cls4b-v5-val-sweep-ckpt4600"}
    }
  },
  "4b_v5_test5120": {
    "majority_baseline": 72.96,
    "checkpoints": {
      "ckpt-4400": {"accuracy": 83.24, "f1_macro": 74.44, "f1_pass": 89.44, "f1_fail": 59.45, "exp_id": "cls4b-v5-ckpt4400-test5120-eval"},
      "ckpt-4600": {"accuracy": 83.63, "f1_macro": 75.63, "f1_pass": 89.59, "f1_fail": 61.67, "exp_id": "cls4b-v5-ckpt4600-test5120-eval"}
    }
  },
  "4b_seed123_test5120": {
    "majority_baseline": 72.96,
    "checkpoints": {
      "ckpt-800": {"accuracy": 75.33, "f1_macro": 67.03, "f1_pass": 83.6, "f1_fail": 50.5, "exp_id": "cls4b-seed123-ckpt800-test5120-eval-v2", "note": "val-best, barely above baseline"}
    }
  },
  "8b_seed123_val8192": {
    "majority_baseline": 75.88,
    "checkpoints": {
      "ckpt-3000": {"accuracy": 88.69, "f1_macro": 81.73, "f1_pass": 93.0,  "f1_fail": 70.5,  "exp_id": "cls8b-seed123-ckpt3000-val8192-eval"},
      "ckpt-6200": {"accuracy": 87.52, "f1_macro": 79.26, "f1_pass": 92.35, "f1_fail": 66.16, "exp_id": "cls8b-seed123-ckpt6200-val8192-eval"},
      "ckpt-6400": {"accuracy": 87.48, "f1_macro": 79.66, "f1_pass": 92.27, "f1_fail": 67.04, "exp_id": "cls8b-seed123-ckpt6400-val8192-eval"},
      "ckpt-6600": {"accuracy": 87.23, "f1_macro": 79.02, "f1_pass": 92.14, "f1_fail": 65.9,  "exp_id": "cls8b-seed123-ckpt6600-val8192-eval"},
      "ckpt-6633": {"accuracy": 87.10, "f1_macro": 78.79, "f1_pass": 92.07, "f1_fail": 65.52, "exp_id": "cls8b-seed123-ckpt6633-val8192-eval"}
    }
  },
  "8b_seed123_test8192": {
    "majority_baseline": 72.96,
    "checkpoints": {
      "ckpt-200":  {"accuracy": 72.55, "f1_macro": 70.18, "f1_pass": 78.58, "f1_fail": 61.78, "exp_id": "cls8b-seed123-ckpt200-test-eval"},
      "ckpt-3000": {"accuracy": 85.60, "f1_macro": 78.38, "f1_pass": 90.87, "f1_fail": 65.89, "exp_id": "cls8b-seed123-ckpt3000-test8192-eval-v2"},
      "ckpt-6200": {"accuracy": 84.70, "f1_macro": 77.01, "f1_pass": 90.31, "f1_fail": 63.71, "exp_id": "cls8b-seed123-ckpt6200-test8192-eval-v2"},
      "ckpt-6400": {"accuracy": 85.08, "f1_macro": 77.91, "f1_pass": 90.49, "f1_fail": 65.32, "exp_id": "cls8b-seed123-ckpt6400-test8192-eval-v2"},
      "ckpt-6600": {"accuracy": 84.90, "f1_macro": 77.58, "f1_pass": 90.40, "f1_fail": 64.80, "exp_id": "cls8b-seed123-ckpt6600-test-eval"},
      "ckpt-6633": {"accuracy": 84.89, "f1_macro": 77.56, "f1_pass": 90.40, "f1_fail": 64.70, "exp_id": "cls8b-seed123-ckpt6633-test-eval"}
    }
  }
}
```
