# analysis r14 a4 bca r1 8b fpr

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942_result.json`
- **Structured JSON:** [`6fccad94cad252d939e6.json`](../../sessions/6f/6fccad94cad252d939e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

```
BCa 95% CI for ΔFPR (text - HS): [0.005817, 0.158995]
Contains 0: No
BCa p-value: 0.0331

Leave-one-out sensitivity:
- 5/43 traces: removal causes p > 0.05
- Most influential trace: idx 3 (p without = 0.062)
- Least influential: idx 30 (p without = 0.010)

Leave-two-out:
- 193/903 pairs: removal causes p > 0.05 (21.4%)
```

BCa CI excludes 0 with a tighter p-value (0.033) than the original percentile bootstrap (0.044), confirming the FPR difference is statistically robust. The bias correction (z0=0.037) and acceleration (a=0.021) are both small, indicating the original percentile CI was already reasonable.

Sensitivity: 5 individual traces (idx 3, 6, 8, 28, 38) can individually flip significance if removed. All 5 are high-leverage outliers with ΔFPR 0.5-0.7 (text FPR far exceeding HS FPR). 21.4% of trace pairs can flip significance. The signal is real but partly driven by these extreme cases.

---
