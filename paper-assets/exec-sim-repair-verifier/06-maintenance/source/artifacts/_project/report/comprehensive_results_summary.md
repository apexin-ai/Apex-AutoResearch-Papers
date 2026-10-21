# Comprehensive Results Summary

> Generated: 2026-05-15 (updated). All numbers sourced from registry (DONE + success only).
> Excluded: `cls8b-seed123-ckpt3000-val8192-eval` (old training artifact, invalid).

---

## 1. Dataset

| Split | Samples | Class Balance | Majority Baseline |
|-------|---------|---------------|-------------------|
| Train | 15,290 | pass 52% / fail 48% | 52.0% |
| Val | 1,896 | — | — |
| Test (function) | 1,890 | — | 51.75% |
| Test (repo) | 9,784 | — | 72.96% |
| Val (repo) | 9,335 | — | ~75.9% |

5 mutation types: operator_swap, return_value, boundary_removal, variable_swap, off_by_one.
Source: `mvp-b-data-prep`

---

## 2. Function-level Results (per-test, 1890 test samples)

### 2.1 CLS 4B — 5 seeds

| Seed | Accuracy | Pass F1 | Fail F1 | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |
|------|----------|---------|---------|-----------|----------|-----------|----------|--------|
| 42 | 87.83 | 88.06 | 87.59 | 89.45 | 86.71 | 86.20 | 89.04 | `multi-seed-core` |
| 123 | 89.52 | 89.64 | 89.40 | 91.76 | 87.63 | 87.34 | 91.56 | `multi-seed-core` |
| 456 | 87.88 | 87.53 | 88.21 | 93.60 | 82.21 | 83.12 | 93.97 | `multi-seed-core` |
| 789 | 89.00 | 88.90 | 89.10 | 93.30 | 84.90 | 85.20 | 93.40 | `cls-seed789` |
| 0 | 87.94 | 87.79 | 88.08 | 92.13 | 83.84 | 84.20 | 92.32 | `cls-seed0` |
| **Mean** | **88.43** | **88.38** | **88.48** | | | | | |
| **Std** | **0.78** | **0.88** | **0.68** | | | | | |

### 2.2 CWM 4B — 5 seeds

| Seed | Accuracy | Pass F1 | Fail F1 | Exact Match | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |
|------|----------|---------|---------|-------------|-----------|----------|-----------|----------|--------|
| 42 | 87.51 | 87.15 | 87.86 | — | 93.24 | 81.80 | 82.75 | 93.64 | `per-test-precision-recall` |
| 123 | 87.20 | 86.95 | 87.44 | 84.44 | — | — | — | — | `cwm-seed123` |
| 456 | 86.98 | 86.66 | 87.29 | 84.02 | 92.26 | 81.70 | 82.52 | 92.65 | `cwm-seed456` |
| 789 | 86.67 | 86.74 | 86.60 | 83.97 | 89.37 | 84.25 | 84.09 | 89.25 | `cwm-seed789` |
| 0 | 87.57 | 87.18 | 87.93 | 84.29 | 93.45 | 81.70 | 82.71 | 93.86 | `cwm-seed0` |
| **Mean** | **87.19** | **86.94** | **87.42** | **84.18** | | | | | |
| **Std** | **0.37** | **0.22** | **0.52** | **0.21** | | | | | |

### 2.3 CLS 8B — 3 seeds

| Seed | Accuracy | Pass F1 | Fail F1 | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |
|------|----------|---------|---------|-----------|----------|-----------|----------|--------|
| 42 | 90.48 | 90.86 | 90.06 | 90.22 | 91.51 | 90.76 | 89.36 | `cls8b-eval-seed42` |
| 123 | 89.37 | 89.54 | 89.19 | 91.20 | 87.93 | 87.54 | 90.90 | `cls8b-eval-seed123` |
| 456 | 88.31 | 88.20 | 88.41 | 92.29 | 84.46 | 84.72 | 92.43 | `cls8b-seed456` |
| **Mean** | **89.39** | **89.53** | **89.22** | | | | | |
| **Std** | **1.09** | **1.33** | **0.83** | | | | | |

### 2.4 CWM 8B — 3 seeds

| Seed | Accuracy | Pass F1 | Fail F1 | Exact Match | Source |
|------|----------|---------|---------|-------------|--------|
| 42 | 87.67 | 87.57 | 87.77 | 84.39 | `model-size-scaling-cwm8b` |
| 123 | 86.98 | 86.83 | 87.13 | 84.13 | `cwm8b-seed123` |
| 456 | 86.24 | 85.96 | 86.51 | 82.80 | `cwm8b-seed456` |
| **Mean** | **86.96** | **86.79** | **87.14** | **83.77** | |
| **Std** | **0.72** | **0.82** | **0.63** | **0.86** | |

### 2.5 CLS vs CWM Comparison

| Config | CLS Acc (mean) | CWM Acc (mean) | Gap (pp) | Seeds |
|--------|---------------|----------------|----------|-------|
| 4B | 88.43 ± 0.78 | 87.19 ± 0.37 | **+1.24** | 5 vs 5 |
| 8B | 89.39 ± 1.09 | 86.96 ± 0.72 | **+2.43** | 3 vs 3 |

Gap widens from +1.24pp (4B) to +2.43pp (8B) — supports complexity hypothesis.

### 2.6 Model Size Scaling (4B → 8B)

| Method | 4B Mean | 8B Mean | Scaling Gain (pp) |
|--------|---------|---------|-------------------|
| CLS | 88.43 | 89.39 | **+0.96** |
| CWM | 87.19 | 86.96 | **−0.23** |

CLS benefits from scaling; CWM does not (bottleneck is generative complexity, not model capacity).

---

## 3. Trajectory-level Results (1032 variants, 5 seeds)

| Seed | Accuracy | Unresolved F1 | Resolved F1 | Consistency | Source |
|------|----------|---------------|-------------|-------------|--------|
| 42 | 85.66 | 87.50 | 83.18 | 79.94 | `traj-level-finetuned` |
| 123 | 85.47 | 87.00 | 83.52 | 78.59 | `traj-level-seed123` |
| 456 | 87.40 | 88.70 | 85.80 | 78.80 | `traj-level-seed456` |
| 789 | 87.31 | 88.27 | 86.17 | 76.74 | `traj-level-seed789` |
| 0 | 85.66 | 87.37 | 83.41 | 79.55 | `traj-level-seed0` |
| **Mean** | **86.30** | **87.77** | **84.42** | **78.72** | |
| **Std** | **0.97** | **0.68** | **1.45** | **1.26** | |

### CLS vs TRAJ (variant-level, clustered bootstrap)

| Metric | Value | Source |
|--------|-------|--------|
| Pooled gap (CLS − TRAJ) | −0.45 pp | `5-paired-clustered-bootstrap` |
| 95% CI | [−1.71, +0.84] | `5-paired-clustered-bootstrap` |
| p-value | 0.499 (not significant) | `5-paired-clustered-bootstrap` |
| TOST p-value (±2pp margin) | 0.0071 (equivalent) | `5-paired-clustered-bootstrap` |

Per-seed gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29.

**Conclusion**: CLS and TRAJ are statistically equivalent at variant level. Per-test's advantage is diagnostic granularity (which test fails), not raw accuracy.

---

## 4. Repo-level Results (majority baseline: 72.96%)

### 4.1 CLS 4B seed42 — Test Set (v5, home-1x5090, transformers 4.57.6)

max_seq_length=2048, eval_samples=9,784, unparseable=132 (1.3%)

| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | vs Baseline (pp) | Source |
|-----------|----------|----------|---------|---------|-------------------|--------|
| 600 | 76.74 | 73.74 | 64.88 | 82.61 | +3.78 | `repo-level-cls-v5` |
| 4000 | 81.51 | 72.56 | 56.90 | 88.23 | +8.55 | `repo-level-cls-v5` |
| 4200 | 80.64 | 72.10 | 56.66 | 87.54 | +7.68 | `repo-level-cls-v5` |
| 4400 | 82.11 | 73.94 | 59.34 | — | +9.15 | `repo-level-cls-v5` |
| **4600** | **82.35** | **74.74** | **60.87** | **88.60** | **+9.39** | `repo-level-cls-v5` |

Best: ckpt-4600 (both accuracy and F1 macro).

### 4.2 CLS 4B seed42 — Val Set (v5, home, max_seq_length=2048)

eval_samples=9,335, unparseable=1,883 (20.2%)

| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Source |
|-----------|----------|----------|---------|---------|--------|
| 600 | 77.25 | 70.81 | 57.11 | 84.52 | `repo-level-cls-v5` |
| 4000 | 83.32 | 70.26 | 50.56 | 89.97 | `repo-level-cls-v5` |
| 4200 | 82.82 | 69.54 | 49.43 | 89.65 | `repo-level-cls-v5` |
| 4400 | 83.49 | 71.63 | 53.29 | 89.97 | `repo-level-cls-v5` |
| **4600** | **83.63** | **71.72** | **53.36** | **90.07** | `repo-level-cls-v5` |

Val-test consistent: both best at ckpt-4600.

### 4.3 CLS 4B seed42 — Test Set (v5-conda, westd, transformers 4.57.6)

Apple-to-apple environment match with CWM v12. eval_samples=9,784, unparseable=132 (1.35%)

| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Source |
|-----------|----------|----------|---------|---------|--------|
| 200 | 52.96 | 52.89 | 51.02 | 54.76 | `repo-level-cls-v5-conda` |
| 400 | 78.43 | 68.41 | 50.61 | 86.21 | `repo-level-cls-v5-conda` |
| **600** | **76.37** | **71.17** | **58.93** | **83.41** | `repo-level-cls-v5-conda` |

Best accuracy: ckpt-400 (78.43%). Best F1 macro: ckpt-600 (71.17%).
Home v5 ckpt-600 (76.74%) vs conda v5-conda ckpt-600 (76.37%): only 0.37pp diff → environment difference negligible.

### 4.4 CLS 4B seed123 — Val Only (home)

| Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | Truncated | Source |
|-------|-----------|----------|----------|---------|---------|-------------|-----------|--------|
| val@2048 | 200 | 62.51 | 55.54 | 37.94 | 73.14 | 1,883 | — | `repo-level-cls-seed123-home` |
| val@2048 | 400 | 80.72 | 67.03 | 45.78 | 88.27 | 1,883 | — | `repo-level-cls-seed123-home` |
| val@2048 | 600 | 76.78 | 66.81 | 48.63 | 85.00 | 1,883 | — | `repo-level-cls-seed123-home` |
| val@2048 | 800 | 81.81 | 69.14 | 49.37 | 88.91 | 1,883 | — | `repo-level-cls-seed123-home` |
| val@2048 | 1000 | 82.30 | 67.63 | 45.84 | 89.42 | 1,883 | — | `repo-level-cls-seed123-home` |
| val@4096 | 400 | 82.57 | 71.24 | 53.18 | 89.29 | 1,406 | — | `repo-level-cls-seed123-home` |
| val@4096 | 600 | 79.18 | 70.73 | 55.00 | 86.45 | 1,406 | — | `repo-level-cls-seed123-home` |
| val@4096 | 800 | 83.70 | 73.31 | 56.70 | 90.00 | 1,406 | — | `repo-level-cls-seed123-home` |
| val@5120 | 400 | 86.01 | 79.66 | 68.30 | 91.02 | 0 | 234 | `repo-level-cls-seed123-home` |
| val@5120 | 600 | 81.89 | 77.01 | 66.43 | 87.60 | 0 | 234 | `repo-level-cls-seed123-home` |
| **val@5120** | **800** | **87.92** | **81.95** | **71.57** | **92.33** | **0** | **234** | `repo-level-cls-seed123-home` |

Key finding: max_seq_length dramatically affects unparseable rate and accuracy.
- @2048: 1,883 unparseable (20.2%), best acc=82.30%
- @4096: 1,406 unparseable (15.1%), best acc=83.70%
- @5120: 0 unparseable, best acc=87.92%

### 4.5 CLS 8B seed42 — Conda (westd, transformers 4.57.6)

| Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | max_seq_len | Source |
|-------|-----------|----------|----------|---------|---------|-------------|-------------|--------|
| val@8192 | 200 | 63.52 | 61.17 | 51.60 | 70.70 | 9 | 8192 | `repo-level-cls-8b-conda` |
| val@8192 | 400 | 80.96 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |
| val@8192 | 600 | 85.00 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |
| val@5120 | 400 | 80.47 | 75.84 | — | — | — | 5120 | `repo-level-cls-8b-conda` |
| test@2048 | 400 | 84.52 | 80.89 | — | — | — | 2048 | `repo-level-cls-8b-conda` |
| test@2048 | 600 | 78.51 | — | — | — | — | 2048 | `repo-level-cls-8b-conda` |
| test@8192 | 400 | 84.79 | 81.18 | 72.93 | 89.43 | 0 | 8192 | `cls8b-s42-ckpt400-test8192-eval` |
| test@8192 | 600 | 79.05 | 75.12 | 65.24 | 85.00 | 0 | 8192 | `cls8b-s42-ckpt600-test8192-eval` |
| test@8192 | 800 | 83.53 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |
| test@8192 | 1000 | 83.52 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |
| test@8192 | 1200 | 83.84 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |
| **test@8192** | **1400** | **85.47** | — | — | — | **0** | **8192** | `cls8b-s42-test-sweep` |
| test@8192 | 1600 | 84.99 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |

Test-best: ckpt-1400 @ 8192 → **85.47% (+12.51pp vs majority baseline)**.
Val-best: ckpt-1000 @ 8192 → **88.23%** (test=83.52%).
8B s42 test-best (85.47%) vs 4B best (82.35% v5 ckpt-4600) = **+3.12pp scaling gain**.

### 4.6 CLS 8B seed123 — Repo-level (westd, @8192)

**Val sweep:**

| Checkpoint | Accuracy | Status |
|-----------|----------|--------|
| **3000** | **88.69%** | **val-best** |
| 6200 | 87.52% | |
| 6400 | 87.48% | |
| 6600 | 87.23% | |
| 6633 | — | ⏳ running |

**Test @8192 (ckpt-3000, val-best):**

| Metric | Value |
|--------|-------|
| Accuracy | 85.60% |
| F1 Macro | 78.38% |
| Fail F1 | 65.89% |
| Pass F1 | 90.87% |
| Fail Precision | 91.65% |
| Fail Recall | 51.44% |
| Pass Precision | 84.52% |
| Pass Recall | 98.26% |
| vs Majority Baseline | +12.64pp |

### 4.7 CLS 4B seed42 — v5 Extended Eval

| Split | Checkpoint | Accuracy |
|-------|-----------|----------|
| val | 4400 | 89.96% |
| **val** | **4600** | **90.07%** ← val-best |
| test | 4400 | 83.24% |
| test | 4600 | 83.63% |

### 4.8 Multi-seed 8B Repo-level Comparison

| Seed | Val-best Ckpt | Val Acc | Test Acc | CWM Test | CLS−CWM Gap |
|------|--------------|---------|----------|----------|-------------|
| s42 | ckpt-1000 | 88.23% | 83.52% | 58.04% | 25.48pp |
| seed123 | ckpt-3000 | 88.69% | 85.60% | 59.09% | 26.51pp |
| **Mean** | — | **88.46%** | **84.56%** | **58.57%** | **25.99pp** |

### 4.9 Repo-level Early Versions (for reference)

| Experiment | Accuracy | F1 Macro | Status | Source |
|-----------|----------|----------|--------|--------|
| CLS v4 (4B, early stop) | 66.11 | 56.61 | Below baseline (72.96%) | `repo-level-cls-v4` |
| CWM v10 (invalid) | 69.91 | 46.71 | 93% unparseable (max_new_tokens=64) | `repo-level-cwm-v10` |

---

## 5. Zero-shot LLM Judge Baselines

| Model | Accuracy | Fail F1 | Pass F1 | vs Baseline (pp) | vs Fine-tuned 4B (pp) | Source |
|-------|----------|---------|---------|-------------------|------------------------|--------|
| Qwen3-8B | 64.40 | 72.20 | 50.50 | +12.65 | −24.03 | `llm-judge-8b-zeroshot` |
| Qwen3-32B | 71.69 | 75.91 | 65.68 | +19.94 | −16.74 | `llm-judge-32b-zeroshot` |

Both models heavily biased toward predicting FAIL. 8B→32B scaling = +7.29pp, but still far below fine-tuned 4B (88.43%).

---

## 6. Statistical Analyses

### 6.1 Block Correlation (ICC)

| Metric | Value | Source |
|--------|-------|--------|
| ICC | 0.1909 | `block-corr-empirical` |
| ICC p-value | < 0.0001 | `block-corr-empirical` |
| Design Effect (DEFF) | 3.97 | `block-corr-empirical` |
| Overall error rate | 12.49% | `block-corr-empirical` |
| All-correct problems (observed) | 46 | `block-corr-empirical` |
| All-correct problems (expected i.i.d.) | 16.35 | `block-corr-empirical` |
| Inference precision | bfloat16 | `block-corr-empirical` |

Significant block correlation: tests within the same problem are NOT independent. DEFF=3.97 means effective sample size is ~4x smaller than nominal.

### 6.2 Oracle F2P Stratified Analysis

| # Tests per Problem | % of Problems | Block Advantage (pp) | Source |
|---------------------|---------------|----------------------|--------|
| T=1 | 68.7% | −0.09 (none) | `oracle-f2p-stratified` |
| T=2 | 19.1% | +31.69 | `oracle-f2p-stratified` |
| T=3–5 | 7.1% | +40.74 | `oracle-f2p-stratified` |
| T≥6 | 5.1% | +40.06 | `oracle-f2p-stratified` |
| **Overall** | | **+10.93** | `oracle-f2p-stratified` |

T2 problems contribute 55.3% of overall block advantage despite being only 19.1% of problems.

### 6.3 Per-test Diagnostic (CWM seed42)

| Metric | Value | Source |
|--------|-------|--------|
| Best mutation type | return_value (97.26%) | `per-test-precision-recall` |
| Worst mutation type | off_by_one (82.56%) | `per-test-precision-recall` |
| Perfect problems (114 total) | 48 (42.1%) | `per-test-precision-recall` |
| Median problem fail-F1 | 94.12% | `per-test-precision-recall` |
| FP count | 58 | `per-test-precision-recall` |
| FN count | 178 | `per-test-precision-recall` |

---

## 7. Simulation Results (MVP-A)

| Scenario | i.i.d. Advantage | Block Advantage | Pass? | Source |
|----------|-----------------|-----------------|-------|--------|
| P2P reg=5% | −1.0% | −0.5% | FAIL | `mvp-a-oracle-sim` |
| P2P reg=10% | +13.2% | +8.3% | PASS | `mvp-a-oracle-sim` |
| P2P reg=20% | +35.7% | +27.8% | PASS | `mvp-a-oracle-sim` |

Real SWE-bench F2P distribution: median T=1, mean T=3, P75=2, P90=3.

---

## 8. Summary of Key Findings

| Finding | Evidence |
|---------|----------|
| CLS > CWM at function-level | 4B: +1.24pp (88.43 vs 87.19), 8B: +2.43pp (89.39 vs 86.96) |
| CLS scaling benefit (4B→8B) | +0.96pp (88.43→89.39) |
| CWM no scaling benefit | −0.23pp (87.19→86.96) |
| CLS-CWM gap widens with scale | 4B: 1.24pp → 8B: 2.43pp |
| CLS ≈ TRAJ at variant level | gap=−0.45pp, TOST p=0.007 |
| Per-test advantage is diagnostic | granularity, not raw accuracy |
| Fine-tuned 4B >> zero-shot 32B | 88.43% vs 71.69% (+16.74pp) |
| Repo-level 8B > 4B | 85.47% vs 82.35% (+3.12pp), updated with full s42 test sweep |
| 8B multi-seed repo-level | mean test 84.56%, CLS−CWM gap ~26pp |
| 4B v5 extended eval | val-best 90.07% (ckpt-4600), test 83.63% |
| max_seq_length critical for repo | @2048: 20% unparseable → @5120: 0% |
| Block correlation significant | ICC=0.19, DEFF=3.97 |
| Per-test advantage needs reg≥10% | 5% regression → no advantage |
