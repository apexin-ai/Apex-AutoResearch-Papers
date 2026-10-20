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

## 1b. 8B s42 Resume Val@8192 Sweep (n=9335, ckpt-1800→5400)

Extended training from ckpt-600 resume. All evaluated with `max_seq_length=8192`.

| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Unparseable | Source |
|-----------|-------------|-------------|------------|------------|-------------|--------|
| ckpt-1800 | 87.91 | 82.13 | 92.29 | 71.96 | 9 (0.10%) | cls8b-s42-resume-val-sweep-seq8192-v2 |
| ckpt-2000 | 87.06 | 79.32 | 91.97 | 66.67 | 9 | cls8b-s42-resume-val-sweep-seq8192-v2 |
| ckpt-2200 | 86.51 | 78.30 | 91.65 | 64.94 | 9 | cls8b-s42-resume-val-sweep-seq8192-v2 |
| ckpt-2400 | 86.82 | 80.29 | 91.64 | 68.94 | 9 | cls8b-s42-resume-val-sweep-seq8192-v2 |
| ckpt-2600 | 86.40 | 77.88 | 91.60 | 64.16 | 9 | cls8b-s42-resume-val-sweep-seq8192-v2 |
| ckpt-2800 | 88.38 | 82.58 | 92.63 | 72.52 | 9 | cls8b-s42-resume-val-sweep-seq8192-v2 |
| ckpt-3000 | 87.71 | 81.33 | 92.25 | 70.42 | 9 | cls8b-s42-resume-val-sweep-seq8192-v2 |
| ckpt-3200 | 86.16 | 77.35 | 91.48 | 63.23 | 9 | cls8b-s42-resume-val-sweep-seq8192-v2 |
| ckpt-3400 | 85.33 | 75.73 | 91.00 | 60.47 | 9 | cls8b-s42-resume-val-sweep-seq8192-v2 |
| **ckpt-3600** | **90.28** | **85.98** | **93.75** | **78.20** | 9 | cls8b-s42-resume-val-sweep-seq8192-v2 |
| ckpt-3800 | 89.78 | 84.33 | 93.57 | 75.08 | 9 | cls8b-s42-resume-val-sweep-seq8192-v2 |
| ckpt-4000 | 89.13 | 83.29 | 93.17 | 73.41 | 9 | cls8b-s42-resume-val-sweep-gpu1 |
| ckpt-4200 | 90.21 | 85.91 | 93.69 | 78.12 | 9 | cls8b-s42-resume-val-sweep-gpu1 |
| ckpt-4400 | 89.82 | 85.08 | 93.49 | 76.66 | 9 | cls8b-s42-resume-val-sweep-gpu1 |
| ckpt-4600 | 89.20 | 83.72 | 93.17 | 74.27 | 9 | cls8b-s42-resume-val-sweep-gpu1 |
| ckpt-4800 | 87.52 | 80.62 | 92.18 | 69.06 | 9 | cls8b-s42-resume-val-sweep-gpu1 |
| ckpt-5000 | 87.71 | 80.88 | 92.31 | 69.45 | 9 | cls8b-s42-resume-val-sweep-gpu1 |
| ckpt-5200 | 87.68 | 80.79 | 92.30 | 69.28 | 9 | cls8b-s42-resume-val-sweep-gpu1 |
| ckpt-5400 | 88.43 | 82.16 | 92.74 | 71.58 | 9 | cls8b-s42-resume-val-sweep-gpu1 |
| ckpt-5600 | — | — | — | — | — | 补跑中 |
| ckpt-5800 | — | — | — | — | — | 补跑中 |

**Resume val-best = ckpt-3600 (90.28%, F1_macro=85.98%)** — surpasses original val-best ckpt-1000 (88.23%) by +2.05pp.

Second peak: ckpt-4200 (90.21%). Trend: 3600-4400 sustained >89.8%, then decays to ~87.5-88.5% plateau after ckpt-4800.

All resume checkpoints have 9 unparseable (0.10%), consistent with original sweep.

Notes:
- cuda:0 covered ckpt-1800→3800, cuda:1 covered ckpt-4000→5400
- ckpt-5600/5800 补跑 pending
- GPU1 process was terminated by SeetaCloud platform (SIGTERM, not by our kill worker)

---

## 1c. 8B s42 Resume Test@8192 — Val-Best (n=9784)

| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Unparseable | Source |
|-----------|-------------|-------------|------------|------------|-------------|--------|
| **ckpt-3600** | **84.48** | **78.17** | **89.91** | **66.43** | 0 | cls8b-s42-resume-ckpt3600-test |

**Val-best ckpt-3600 test = 84.48%** — surpasses original val-best ckpt-1000 test (83.52%) by +0.96pp.

Per-mutation breakdown:
| Mutation Type | Accuracy (%) | Samples |
|---|---|---|
| gold (no mutation) | 96.24 | 4633 |
| off_by_one | 86.89 | 183 |
| operator_swap | 81.38 | 3357 |
| return_value | 75.44 | 562 |
| boundary_removal | 46.90 | 1049 |

Notes:
- boundary_removal is the weakest category (46.90%), well below majority baseline
- No variable_swap samples in test set
- Precision/Recall: fail class has high precision (80.1%) but low recall (56.8%)

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
| **8B s42 val@8192 (resume)** | **ckpt-3600** | **90.28** | **85.98** | **+14.40 pp** |
| **8B s42 test@8192 (val-selected, resume)** | **ckpt-3600** | **84.48** | **78.17** | **+11.53 pp** |
| 8B s42 val@8192 (original) | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |
| 8B s42 test@8192 (original sweep best) | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |
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
  "8b_s42_resume_val8192": {
    "majority_baseline": 75.88,
    "checkpoints": {
      "ckpt-1800": {"accuracy": 87.91, "f1_macro": 82.13, "f1_pass": 92.29, "f1_fail": 71.96, "unparseable": 9},
      "ckpt-2000": {"accuracy": 87.06, "f1_macro": 79.32, "f1_pass": 91.97, "f1_fail": 66.67, "unparseable": 9},
      "ckpt-2200": {"accuracy": 86.51, "f1_macro": 78.30, "f1_pass": 91.65, "f1_fail": 64.94, "unparseable": 9},
      "ckpt-2400": {"accuracy": 86.82, "f1_macro": 80.29, "f1_pass": 91.64, "f1_fail": 68.94, "unparseable": 9},
      "ckpt-2600": {"accuracy": 86.40, "f1_macro": 77.88, "f1_pass": 91.60, "f1_fail": 64.16, "unparseable": 9},
      "ckpt-2800": {"accuracy": 88.38, "f1_macro": 82.58, "f1_pass": 92.63, "f1_fail": 72.52, "unparseable": 9},
      "ckpt-3000": {"accuracy": 87.71, "f1_macro": 81.33, "f1_pass": 92.25, "f1_fail": 70.42, "unparseable": 9},
      "ckpt-3200": {"accuracy": 86.16, "f1_macro": 77.35, "f1_pass": 91.48, "f1_fail": 63.23, "unparseable": 9},
      "ckpt-3400": {"accuracy": 85.33, "f1_macro": 75.73, "f1_pass": 91.00, "f1_fail": 60.47, "unparseable": 9},
      "ckpt-3600": {"accuracy": 90.28, "f1_macro": 85.98, "f1_pass": 93.75, "f1_fail": 78.20, "unparseable": 9},
      "ckpt-3800": {"accuracy": 89.78, "f1_macro": 84.33, "f1_pass": 93.57, "f1_fail": 75.08, "unparseable": 9},
      "ckpt-4000": {"accuracy": 89.13, "f1_macro": 83.29, "f1_pass": 93.17, "f1_fail": 73.41, "unparseable": 9},
      "ckpt-4200": {"accuracy": 90.21, "f1_macro": 85.91, "f1_pass": 93.69, "f1_fail": 78.12, "unparseable": 9},
      "ckpt-4400": {"accuracy": 89.82, "f1_macro": 85.08, "f1_pass": 93.49, "f1_fail": 76.66, "unparseable": 9},
      "ckpt-4600": {"accuracy": 89.20, "f1_macro": 83.72, "f1_pass": 93.17, "f1_fail": 74.27, "unparseable": 9},
      "ckpt-4800": {"accuracy": 87.52, "f1_macro": 80.62, "f1_pass": 92.18, "f1_fail": 69.06, "unparseable": 9},
      "ckpt-5000": {"accuracy": 87.71, "f1_macro": 80.88, "f1_pass": 92.31, "f1_fail": 69.45, "unparseable": 9},
      "ckpt-5200": {"accuracy": 87.68, "f1_macro": 80.79, "f1_pass": 92.30, "f1_fail": 69.28, "unparseable": 9},
      "ckpt-5400": {"accuracy": 88.43, "f1_macro": 82.16, "f1_pass": 92.74, "f1_fail": 71.58, "unparseable": 9}
    }
  },
  "8b_s42_resume_test8192_valbest": {
    "majority_baseline": 72.96,
    "checkpoints": {
      "ckpt-3600": {"accuracy": 84.48, "f1_macro": 78.17, "f1_pass": 89.91, "f1_fail": 66.43, "unparseable": 0, "exp_id": "cls8b-s42-resume-ckpt3600-test",
        "mutation_breakdown": {
          "gold": {"accuracy": 96.24, "n": 4633},
          "off_by_one": {"accuracy": 86.89, "n": 183},
          "operator_swap": {"accuracy": 81.38, "n": 3357},
          "return_value": {"accuracy": 75.44, "n": 562},
          "boundary_removal": {"accuracy": 46.90, "n": 1049}
        }
      }
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
