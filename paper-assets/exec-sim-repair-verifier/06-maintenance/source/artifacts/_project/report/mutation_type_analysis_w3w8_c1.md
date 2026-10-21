# Mutation Type Per-Type Accuracy & Seed Variance Root Cause
## W3/W8 + C1 Response Analysis — 2026-05-15

---

## 1. Eval Set Composition

The CLS model is evaluated on `swebench_full/swebench_{split}.jsonl`:
- **Test set**: 9,784 instances (100% SWE-bench verified data)
- **Val set**: 9,335 instances (100% SWE-bench verified data)

Each instance has a `mutation_type`:
- `gold` — original gold patch (always label=pass)
- `mutation_operator_swap` — operator substitution in patch
- `mutation_boundary_removal` — boundary condition removed
- `mutation_return_value` — return value changed
- `mutation_off_by_one` — off-by-one error injected

---

## 2. Val → Test Mutation Type Distribution Shift

| Mutation Type             |  Val %  | Test %  | Shift (pp) |
|---------------------------|---------|---------|------------|
| gold                      |  45.2%  |  47.4%  |    +2.1    |
| mutation_operator_swap    |  19.1%  |  34.3%  |   **+15.2**|
| mutation_boundary_removal |  15.0%  |  10.7%  |    -4.3    |
| mutation_return_value     |  10.7%  |   5.7%  |    -5.0    |
| mutation_off_by_one       |  10.0%  |   1.9%  |    -8.1    |

**Key shift**: operator_swap nearly doubles from 19.1% → 34.3%, while off_by_one collapses from 10.0% → 1.9%.

---

## 3. Label Distribution by Mutation Type

| Mutation Type             | Test N  | Pass %  | Val N   | Val Pass % |
|---------------------------|---------|---------|---------|------------|
| gold                      |  4,633  | 100.0%  |  4,223  |   100.0%   |
| mutation_operator_swap    |  3,357  |  50.4%  |  1,783  |    55.7%   |
| mutation_boundary_removal |  1,049  |  41.7%  |  1,401  |    59.2%   |
| mutation_return_value     |    562  |  43.8%  |    999  |    26.1%   |
| mutation_off_by_one       |    183  |  70.5%  |    929  |    83.5%   |

**Majority baselines differ**: off_by_one majority=83.5% (val) vs 70.5% (test); return_value=73.9% (val) vs 56.2% (test).

---

## 4. Per-Mutation-Type Accuracy

### 4.1 CLS 8B s42 (primary model, multiple checkpoints on test)

| Mutation Type             | ckpt-800 | ckpt-1200 | ckpt-1400 | ckpt-1600 |
|---------------------------|----------|-----------|-----------|-----------|
| gold                      |  94.09%  |   96.09%  |  **98.36%** |  97.13% |
| mutation_operator_swap    |  82.72%  |   81.11%  |   82.16%  |  81.62%  |
| mutation_return_value     |**83.99%**|   78.11%  |   69.04%  |  75.09%  |
| mutation_off_by_one       |  71.04%  |   67.76%  |  **89.07%** |  88.52% |
| mutation_boundary_removal |  41.47%  |   44.33%  |  **47.28%** |  46.81% |
| **OVERALL**               |  83.53%  |   83.84%  |  **85.47%** |  84.99% |

### 4.2 CLS 8B s123 (seed 123, test)

| Mutation Type             | ckpt-3000 | ckpt-6400 |
|---------------------------|-----------|-----------|
| gold                      |   99.57%  |   98.42%  |
| mutation_operator_swap    |   82.60%  |   83.23%  |
| mutation_return_value     |   66.37%  |   69.04%  |
| mutation_off_by_one       |   79.23%  |   78.69%  |
| mutation_boundary_removal |   44.90%  |   41.75%  |
| **OVERALL**               |   85.60%  |   85.08%  |

### 4.3 CLS 4B (available checkpoints only — val-best on offline server)

| Mutation Type             | 4B s42 ckpt-600 | 4B s42 ckpt-400 | 4B s123 ckpt-200 |
|---------------------------|------------------|------------------|------------------|
| gold                      |    82.80%        |    94.91%        |    50.21%        |
| mutation_operator_swap    |    75.63%        |    68.99%        |    61.45%        |
| mutation_return_value     |    73.31%        |    48.58%        |    56.58%        |
| mutation_off_by_one       |    66.12%        |    70.49%        |    56.83%        |
| mutation_boundary_removal |    58.91%        |    53.29%        |    54.91%        |
| **OVERALL**               |    76.92%        |    78.43%        |    55.06%        |

**Note**: 4B s42 val-best=ckpt-4600 (83.63%) and 4B s123 val-best=ckpt-800 (75.33%) predictions are on the offline home-1x5090 server.

---

## 5. Hardest & Easiest Mutation Types

**Ranking (8B s42 ckpt-800):**
1. **gold** (94.09%) — Easiest. All gold instances have label=pass; model just needs to recognize correct patches.
2. **mutation_return_value** (83.99%) — Return value changes are relatively detectable.
3. **mutation_operator_swap** (82.72%) — Operator substitutions; balanced precision/recall (~82%/~85%).
4. **mutation_off_by_one** (71.04%) — Off-by-one errors harder to detect; model has perfect recall_fail (100%) but only 58.9% recall_pass.
5. **mutation_boundary_removal** (41.47%) — **Hardest by far**. Near-random. Error pattern: 438 FP vs 176 FN — model overwhelmingly predicts "pass" for actual fails (fails to detect boundary removals).

### Confusion Matrix Detail (8B s42 ckpt800)

| Type                  | TP   | FP  | TN   | FN  | Prec(pass) | Rec(fail) |
|-----------------------|------|-----|------|-----|------------|-----------|
| gold                  | 4359 |  0  |  0   | 274 |  100.0%    |   N/A     |
| operator_swap         | 1433 | 320 | 1344 | 260 |   81.7%    |  80.8%    |
| return_value          |  237 |  81 |  235 |   9 |   74.5%    |  74.4%    |
| off_by_one            |   76 |   0 |   54 |  53 |  100.0%    | 100.0%    |
| boundary_removal      |  261 | 438 |  174 | 176 |   37.3%    |  28.4%    |

**boundary_removal** is dominated by false positives (predicting pass when test should fail).

---

## 6. Distribution Shift Impact on Overall Accuracy

"If the test set had the val distribution, what would accuracy be?"

| Model              | Actual (test dist) | Hypothetical (val dist) | Shift Effect |
|--------------------|--------------------:|------------------------:|--------------:|
| 8B s42 ckpt-800    |            83.53%  |               80.64%   |   **+2.89pp** |
| 8B s42 ckpt-1400   |            85.47%  |               83.54%   |    +1.93pp    |
| 8B s123 ckpt-3000  |            85.60%  |               82.55%   |    +3.05pp    |
| 4B s42 ckpt-600    |            76.92%  |               75.17%   |    +1.75pp    |

**The test distribution is FAVORABLE**: test accuracy is inflated by +1.7 to +3.1pp vs val distribution.

### Per-type contribution breakdown (8B s42 ckpt-800):

| Type                  | Type Acc | Val Weight | Test Weight | Contribution |
|-----------------------|----------|------------|-------------|--------------|
| gold                  |  94.1%   |   45.2%    |   47.4%     |  -1.99pp     |
| boundary_removal      |  41.5%   |   15.0%    |   10.7%     |  +1.78pp     |
| off_by_one            |  71.0%   |   10.0%    |    1.9%     |  +5.74pp     |
| **operator_swap**     |  82.7%   |   19.1%    |   34.3%     | **-12.58pp** |
| return_value          |  84.0%   |   10.7%    |    5.7%     |  +4.16pp     |

The operator_swap inflation from 19.1%→34.3% contributes -12.58pp (going FROM test to val dist), offset by reduced exposure to hard types (off_by_one: +5.74pp, return_value: +4.16pp).

---

## 7. Repo Distribution Shift — The Hidden Factor

| Repo                      | Val %  | Test % | Shift    |
|---------------------------|--------|--------|----------|
| django/django             | 29.7%  | 36.5%  |  +6.8    |
| **pydata/xarray**         |  0.0%  |**23.7%**| **+23.7**|
| matplotlib/matplotlib     | 18.9%  | 16.1%  |  -2.8    |
| sympy/sympy               | 19.1%  |  1.1%  | -18.0    |
| pylint-dev/pylint         | 12.1%  |  0.0%  | -12.1    |
| psf/requests              |  0.0%  |  4.5%  |  +4.5    |
| scikit-learn/scikit-learn |  6.3%  |  0.5%  |  -5.8    |

Val-only repos: 1 (pylint); Test-only repos: 2 (xarray, requests).

### Critical: xarray anomaly
- xarray = 23.7% of test, **0% of val**
- **All 2,322 xarray instances have label=pass** (both gold and operator_swap)
- Model achieves **100% accuracy** on xarray by simply predicting pass
- This is trivially inflated — xarray operator_swap mutations don't change test outcomes

### Per-repo accuracy (8B s42 ckpt800):

| Repo                      | Accuracy |   N   |
|---------------------------|----------|-------|
| pydata/xarray             | 100.00%  | 2,322 |
| matplotlib/matplotlib     | 100.00%  | 1,572 |
| scikit-learn/scikit-learn | 100.00%  |    46 |
| sympy/sympy               |  80.95%  |   105 |
| django/django             |  78.86%  | 3,572 |
| psf/requests              |  72.40%  |   442 |
| pytest-dev/pytest         |  65.71%  |   522 |
| astropy/astropy           |  57.52%  | 1,071 |
| sphinx-doc/sphinx         |  39.39%  |   132 |

---

## 8. Val Predictions (8B s42 ckpt-1600 on Val)

| Mutation Type             | Val Acc | Test Acc (ckpt-1600) |
|---------------------------|---------|----------------------|
| gold                      | 99.62%  |  97.13%              |
| mutation_operator_swap    | 82.39%  |  81.62%              |
| mutation_return_value     | 79.78%  |  75.09%              |
| mutation_off_by_one       | 81.81%  |  88.52%              |
| mutation_boundary_removal | 61.74%  |  46.81%              |
| **OVERALL**               |**86.75%**| 84.99%              |

boundary_removal drops 14.93pp from val→test, while off_by_one improves 6.71pp (due to easier test instances).

---

## 9. Seed Variance Root Cause (C1)

### 9.1 Available data

| Model | Seed | Val-best ckpt | Val Acc | Test Acc | Available on westd? |
|-------|------|---------------|---------|----------|---------------------|
| 4B    |  42  | ckpt-4600     | 90.07%  | 83.63%   | **No** (home offline) |
| 4B    | 123  | ckpt-800      | 87.92%  | 75.33%   | **No** (home offline) |
| 8B    |  42  | ckpt-1000     | 88.23%  | 83.52%   | ckpt-800 ≈ 83.53%   |
| 8B    | 123  | ckpt-3000     |   ?     | 85.60%   | Yes                  |

### 9.2 Val loss trajectory (4B s123)

```
Step   Val Loss   Trend
 200    0.0808    ← BEST (lowest val loss)
 400    0.0902    ↑
 600    0.1147    ↑
 800    0.1473    ↑↑
1000    0.2784    ↑↑↑ severe overfitting
1200    0.3039    ↑↑↑
...     oscillates 0.19-0.36 through step 3600
```

**4B s123 overfits rapidly**: val loss doubles by step 800, suggesting the ckpt-800 val-best was selected at a local minimum during an overfitting trajectory. The "best" checkpoint is actually at the inflection point where the model starts memorizing training data.

### 9.3 Val loss trajectory (4B s42)

```
Step   Val Loss
 200    0.0829    ← BEST
 400    0.1076    ↑
 600    0.0996    slight recovery
```
Only 3 checkpoints available (different training run on westd). The home server has checkpoints to ckpt-4600.

### 9.4 8B Seed Comparison (s42 ckpt-800 vs s123 ckpt-3000)

| Type                  | s42     | s123    | Diff     |
|-----------------------|---------|---------|----------|
| gold                  | 94.09%  | 99.57%  |  +5.48   |
| off_by_one            | 71.04%  | 79.23%  |  +8.20   |
| boundary_removal      | 41.47%  | 44.90%  |  +3.43   |
| operator_swap         | 82.72%  | 82.60%  |  -0.12   |
| **return_value**      |**83.99%**|**66.37%**|**-17.62**|
| OVERALL               | 83.53%  | 85.60%  |  +2.07   |

**8B s123 trades return_value detection (-17.62pp) for gold detection (+5.48pp).** s123 at ckpt-3000 heavily over-predicts "pass" (99.57% gold acc means near-perfect recall_pass but may sacrifice fail detection on return_value mutations). s42 at ckpt-800 is more balanced.

### 9.5 Root cause hypothesis for 4B s42 vs s123 gap (8.3pp)

1. **Different overfitting dynamics**: s123 overfits faster (val loss spikes by step 800), likely learning seed-dependent shortcuts in training data ordering
2. **Val-best selection at overfitting inflection**: s123's ckpt-800 is selected when overfitting is already underway, making it sensitive to distribution shift
3. **Likely return_value sensitivity**: By analogy with 8B, s123 probably has lower return_value accuracy, which is amplified by distribution differences
4. **Repo-level memorization**: Different seeds see training repos in different order; s123 may memorize repo-specific patterns that don't transfer to test repos (especially xarray which is test-only)

**Cannot confirm 4B per-type breakdown** without the val-best predictions (on offline home server). The 8B analysis suggests seed variance is driven by **trade-offs between gold recall and mutation detection**, not by operator_swap sensitivity.

---

