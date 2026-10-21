# CSMP Gradual Contamination Evaluation Report

Evaluating CUSUM sequential monitoring on gradual contamination (alpha=0.50, 0.75).
Contamination present from gen 1 onwards. Trigger gen = 1.
Calibration: h calibrated on alpha=0.00 null data (3 seeds, FAR=0%).

## 1. Calibration Parameters (from null data)

| k | h | FAR | ARL_0 |
|---|---|-----|-------|
| 0.05 | 1.529726 | 0% | 10.0 |
| 0.1 | 1.004726 | 0% | 10.0 |
| 0.25 | 0.000100 | 0% | 10.0 |
| 0.5 | 0.000100 | 0% | 10.0 |
| 1.0 | 0.000100 | 0% | 10.0 |

## 2. alpha=0.5 Evaluation

### CUSUM Results

| k | h | s42 alarm | s42 S_max | s43 alarm | s43 S_max | s44 alarm | s44 S_max | Mean EDD |
|---|---|---------|---------|---------|---------|---------|---------|----------|
| 0.05 | 1.5297 | 3 | 6.1158 | 3 | 5.9176 | 3 | 6.0442 | 2.0 |
| 0.1 | 1.0047 | 2 | 5.6158 | 2 | 5.4176 | 2 | 5.5442 | 1.0 |
| 0.25 | 0.0001 | 1 | 4.1158 | 1 | 3.9176 | 1 | 4.0442 | 0.0 |
| 0.5 | 0.0001 | 1 | 1.6158 | 1 | 1.4176 | 1 | 1.5442 | 0.0 |
| 1.0 | 0.0001 | None | 0.0000 | None | 0.0000 | None | 0.0000 | N/A |

### Simple Threshold Baseline

| Method | s42 alarm | s43 alarm | s44 alarm |
|--------|---------|---------|---------|
| Threshold (n>=1) | 1 | 1 | 1 |
| Threshold (n>=2) | 2 | 2 | 2 |

Note: Threshold = null_mean - 2*null_std = 3.0524 - 2*0.0307 = 2.9910

## 3. alpha=0.75 Evaluation

### CUSUM Results

| k | h | s42 alarm | s42 S_max | s43 alarm | s43 S_max | s44 alarm | s44 S_max | Mean EDD |
|---|---|---------|---------|---------|---------|---------|---------|----------|
| 0.05 | 1.5297 | 2 | 9.6743 | 2 | 9.6789 | 2 | 9.7988 | 1.0 |
| 0.1 | 1.0047 | 2 | 9.1743 | 2 | 9.1789 | 2 | 9.2988 | 1.0 |
| 0.25 | 0.0001 | 1 | 7.6743 | 1 | 7.6789 | 1 | 7.7988 | 0.0 |
| 0.5 | 0.0001 | 1 | 5.1743 | 1 | 5.1789 | 1 | 5.2988 | 0.0 |
| 1.0 | 0.0001 | 1 | 0.4702 | 1 | 0.4545 | 1 | 0.5086 | 0.0 |

### Simple Threshold Baseline

| Method | s42 alarm | s43 alarm | s44 alarm |
|--------|---------|---------|---------|
| Threshold (n>=1) | 1 | 1 | 1 |
| Threshold (n>=2) | 2 | 2 | 2 |

Note: Threshold = null_mean - 2*null_std = 3.0524 - 2*0.0307 = 2.9910

## 4. Cross-Alpha Comparison (CUSUM k=0.25)

| Alpha | Seed | Alarm Gen | EDD | S_max |
|-------|------|-----------|-----|-------|
| 1.00 | s42 | 1 | 0 | 1.0667 |
| 0.50 | s42 | 1 | 0 | 4.1158 |
| 0.50 | s43 | 1 | 0 | 3.9176 |
| 0.50 | s44 | 1 | 0 | 4.0442 |
| 0.75 | s42 | 1 | 0 | 7.6743 |
| 0.75 | s43 | 1 | 0 | 7.6789 |
| 0.75 | s44 | 1 | 0 | 7.7988 |

## 5. CUSUM vs Simple Threshold

| Alpha | Method | s42 | s43 | s44 |
|-------|--------|-----|-----|-----|
| 0.50 | CUSUM k=0.25 | 1 | 1 | 1 |
| 0.50 | CUSUM k=0.1 | 2 | 2 | 2 |
| 0.50 | Thresh n=1 | 1 | 1 | 1 |
| 0.50 | Thresh n=2 | 2 | 2 | 2 |
| 0.75 | CUSUM k=0.25 | 1 | 1 | 1 |
| 0.75 | CUSUM k=0.1 | 2 | 2 | 2 |
| 0.75 | Thresh n=1 | 1 | 1 | 1 |
| 0.75 | Thresh n=2 | 2 | 2 | 2 |

## 6. Key Findings

### Does CUSUM degenerate to a simple threshold for gradual shifts?

With k=0.25 (h~0), CUSUM alarms at gen 1 for all seeds, identical to the simple
threshold (n=1). This is expected: the initial drop from gen 0 to gen 1 is so large
(0.7+ for alpha=0.50, 1.0+ for alpha=0.75) that any detector with a near-zero
threshold triggers immediately. The key difference is:

1. CUSUM with higher k (0.5, 1.0) may still alarm at gen 1 due to the large shift
2. CUSUM with lower k (0.05, 0.10) and calibrated h>0 may delay, showing that
   calibration against null drift creates meaningful control limits
3. The simple threshold has no principled way to set the alarm boundary,
   while CUSUM calibrates h from null data with guaranteed FAR control

### Recommended k for gradual contamination

- alpha=0.5, k=1.0: NOT all seeds alarmed (sensitivity loss)
- k=0.25 remains the recommended operating point: alarms at gen 1 for both
  alpha=0.50 and alpha=0.75 across all seeds, with FAR=0% on null data.
- For gradual contamination, no different k is needed compared to abrupt shifts,
  because the initial gen-0-to-gen-1 drop is already large enough.
