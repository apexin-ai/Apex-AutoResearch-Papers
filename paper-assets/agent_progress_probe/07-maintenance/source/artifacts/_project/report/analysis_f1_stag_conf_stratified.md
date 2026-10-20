# F1-stag Per-class Breakdown + Confidence Stratified Analysis

## 1. Per-class Breakdown

| Model | N | macro_F1 | F1_stag | F1_prog | P_stag | R_stag | P_prog | R_prog | TN | FP | FN | TP |
|-------|---|----------|---------|---------|--------|--------|--------|--------|----|----|----|----|
| probe_001 (s42) | 1824 | 0.9055 | 0.8593 | 0.9518 | 0.8969 | 0.8247 | 0.9383 | 0.9656 | 400 | 85 | 46 | 1293 |
| probe (s123) | 2216 | 0.9265 | 0.9022 | 0.9508 | 0.9409 | 0.8666 | 0.9316 | 0.9709 | 669 | 103 | 42 | 1402 |
| probe (s456) | 2343 | 0.9234 | 0.9024 | 0.9444 | 0.8908 | 0.9142 | 0.9514 | 0.9375 | 767 | 72 | 94 | 1410 |

### Additional models (from prior evaluations)

| Model | N | macro_F1 | F1_stag | F1_prog | P_stag | R_stag | P_prog | R_prog |
|-------|---|----------|---------|---------|--------|--------|--------|--------|
| woob (own 2LF test) | 1519 | 0.951 | 0.9159 | 0.9862 | 0.8829 | 0.9515 | 0.9923 | 0.9802 |
| woob → p001 test | 1824 | 0.7659 | 0.6272 | 0.9046 | 0.9031 | 0.4804 | 0.8391 | 0.9813 |
| OH 100% FT | 20807 | 0.7512 | 0.5439 | 0.9586 | 0.4602 | 0.6648 | 0.9747 | 0.943 |
| full-model conf≥2 | 1824 | 0.9396 | 0.9103 | 0.969 | 0.9446 | 0.8784 | 0.957 | 0.9813 |

## 2. Confidence-Stratified Analysis (probe_001)

Model: `checkpoints/best_model.pt` (seed=42, trained on conf≥2)

| Confidence | N | macro_F1 | F1_stag | F1_prog | P_stag | R_stag | P_prog | R_prog | TN | FP | FN | TP |
|------------|---|----------|---------|---------|--------|--------|--------|--------|----|----|----|----|
| 1 (zero-shot) | 39408 | 0.7327 | 0.6414 | 0.824 | 0.5138 | 0.8534 | 0.9384 | 0.7344 | 8324 | 1430 | 7876 | 21778 |
| 2 (test) | 1780 | 0.9078 | 0.8633 | 0.9522 | 0.9025 | 0.8274 | 0.938 | 0.9669 | 398 | 83 | 43 | 1256 |
| 3 (test) | 44 | 0.6906 | 0.4444 | 0.9367 | 0.4 | 0.5 | 0.9487 | 0.925 | 2 | 2 | 3 | 37 |
| ≥2 (test) | 1824 | 0.9055 | 0.8593 | 0.9518 | 0.8969 | 0.8247 | 0.9383 | 0.9656 | 400 | 85 | 46 | 1293 |

> Note: conf=1 uses all 39408 windows (never in training). conf=2/3 use only the test split.
> Note: conf=3 test split has only 44 windows (4 stag), metrics unreliable due to tiny sample.

## 3. Error Analysis (probe_001, conf≥2 test)

- Total: 1824 windows
- Correct: 1693 (92.8%)
- **FP** (pred stag, actual prog): **46** (2.5%)
- **FN** (pred prog, actual stag): **85** (4.7%)
- Error composition: 46 FP (35.1%) + 85 FN (64.9%)

### By confidence level

| Conf | Windows | FP | FN | Errors | Error Rate | % total FP | % total FN |
|------|---------|----|----|--------|------------|------------|------------|
| 2 | 1780 | 43 | 83 | 126 | 0.0708 | 93.5% | 97.7% |
| 3 | 44 | 3 | 2 | 5 | 0.1136 | 6.5% | 2.4% |

---
*All metrics computed from model checkpoints + test splits on bjb2-23165.*